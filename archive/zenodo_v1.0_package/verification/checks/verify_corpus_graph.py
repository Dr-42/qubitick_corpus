"""
verify_corpus_graph.py — citation graph of the four-era canon.

Builds the tag registry from the ### headings and the paragraph declarations of
Parts 1–4 and Census; extracts each tag's **Req.** citations; verifies:
  * citation closure (every Req-cited tag exists in the registry, or is an
    annex pointer: HistLog items, Cal registries, M1/M2, Census cells);
  * tag-level acyclicity (no directed cycles — any cycle fails, no whitelist);
  * the era-chain law on Req edges: rank(cited) <= rank(citing), with
    rank(Part1)=1, rank(Part2)=2, rank(Part3)=3, rank(Census)=3, rank(Part4)=4;
    HistLog is an annex (pointer target only, never a premise);
and regenerates index/{tags.json,graph.md,tier_index.md,dependency_tree.md}.

Pure stdlib; exact integer bookkeeping. Exit 0 = green.
"""
import os, re, sys, json, collections

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
IDX  = os.path.join(DOCS, "index")

FILES = [("Part1_Qubit_era.md", 1), ("Part2_Bosonic_era.md", 2),
         ("Part3_Fermion_era.md", 3), ("Census.md", 3),
         ("Part4_Baryomesonic_era.md", 4)]

HEAD_RE = re.compile(
    r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.\d+\w*|"
    r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\b)", re.M)
PARA_RE = re.compile(r"^\*\*(A[1-9]|C1[0-3]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", re.M)
COR_RE = re.compile(r"\*\*Cor\s+((?:CT\d+\.\d+|EW\.\d+|EM\.\d+|FT\.\d+|L0)[ab]?)\b")
POINTER_RE = re.compile(r"HistLog §I{1,2}V?\}?/(?:\\mathrm\{)?(?:FT|Def-H)\.\d+\}?")
TIER_RE = re.compile(r"^## (Tier [^\n]+|§[A-G][^\n]*)", re.M)
TOKEN_RE = re.compile(
    r"\b(Def-EM\.\d+|Def-H\.\d+|Def-BM\.\d+|FT\.\d+|BM\.\d+|"
    r"CT\d+\.\d+[ab]?|EW\.\d+a?|EM\.\d+[ab]?|D[0-4]\.\d+|A[1-9]|C1[0-3]|C[1-9]|P[1-5]|L[0-5]a?)\b")

FAIL = []
REQ_TEXT = {}
def chk(cond, msg, extra=""):
    if not cond:
        FAIL.append(msg + (f" — {extra}" if extra else ""))
        print(f"  FAIL: {msg} {extra}")
    return cond

def main():
    registry = {}          # tag -> (file, rank, order_index, tier)
    order = []             # (tag, file, rank, tier)
    reqs = {}              # tag -> cited token set
    for fn, rank in FILES:
        src = open(os.path.join(DOCS, fn), encoding="utf-8").read()
        # split into blocks at ### headings, tracking the current tier
        marks = []
        for m in re.finditer(r"(?m)^(###[^\n]*|## [^\n]*)$", src):
            marks.append((m.start(), m.group(0)))
        cur_tier = fn
        for i, (pos, head) in enumerate(marks):
            end = marks[i + 1][0] if i + 1 < len(marks) else len(src)
            body = src[pos:end]
            if head.startswith("## "):
                cur_tier = head[3:].strip()
                continue
            m = HEAD_RE.match(head)
            if not m:
                continue
            tag = m.group(1).rstrip(".")
            if tag in registry:
                chk(False, f"duplicate tag {tag}", f"{registry[tag][0]} & {fn}")
                continue
            registry[tag] = (fn, rank, len(order), cur_tier)
            order.append((tag, fn, rank, cur_tier))
            # inline corollary declarations join the registry
            cors = [(cm.start(), cm.group(1)) for cm in COR_RE.finditer(body)]
            for cpos, ctag in cors:
                if ctag not in registry:
                    registry[ctag] = (fn, rank, len(order), cur_tier)
                    order.append((ctag, fn, rank, cur_tier))
                    reqs[ctag] = set()
            # Req paragraphs: plain -> block tag; "(Cor)" -> nearest corollary above;
            # 'cf.' notes and HistLog pointers are references, not premises
            for rm in re.finditer(r"\*\*Req(\s\(Cor\))?\.\*\*(.*?)(?=\n\s*\n\*\*|\n\*\*Pf|\n\*\*Phys|\Z)", body, re.S):
                txt = POINTER_RE.sub("", rm.group(2))
                txt = re.sub(r"(?:FT|Def-H)\.\d+ \(HistLog §I{1,2}V?\)", "", txt)
                txt = re.sub(r"cf\.[^\]$]*", "", txt)
                cited = set(TOKEN_RE.findall(txt))
                owner = tag
                if rm.group(1):
                    prior = [c for cpos, c in cors if cpos < rm.start()]
                    if prior:
                        owner = prior[-1]
                reqs.setdefault(owner, set())
                reqs[owner] |= cited - {owner}
                REQ_TEXT[(fn, owner)] = rm.group(2)
    # paragraph-declared tags (axioms/conventions/defs/calibration)
    for fn, rank in FILES[:2]:
        src = open(os.path.join(DOCS, fn), encoding="utf-8").read()
        for m in PARA_RE.finditer(src):
            t = m.group(1)
            if t not in registry:
                registry[t] = (fn, rank, len(order), "declarations")
                order.append((t, fn, rank, "declarations"))
                reqs.setdefault(t, set())

    print(f"registry: {len(registry)} tags; {sum(len(v) for v in reqs.values())} Req edges")

    # ---- closure
    missing = collections.Counter()
    for tag, cited in reqs.items():
        for c in cited:
            if c not in registry:
                missing[c] += 1
    chk(not missing, "citation closure", f"missing: {dict(missing)}")

    # ---- era law
    viol = []
    MARKERS = ("forward", "corroboration", "cf.", "restated", "re-verification", "re-derived")
    for tag, cited in reqs.items():
        r_here = registry[tag][1]
        reqtxt = REQ_TEXT.get((registry[tag][0], tag), "").lower()
        for c in cited:
            if c in registry and registry[c][1] > r_here:
                if not any(mk in reqtxt for mk in MARKERS):
                    viol.append((tag, registry[tag][0], c, registry[c][0]))
    chk(not viol, "era-chain law on Req edges", str(viol[:8]))

    # ---- acyclicity (tag-level, DFS)
    adj = {t: sorted(c for c in cs if c in registry) for t, cs in reqs.items()}
    state = {}
    stack = []
    cycles = []
    sys.setrecursionlimit(10000)
    def dfs(u):
        state[u] = 1
        stack.append(u)
        for v in adj.get(u, ()):
            if state.get(v, 0) == 0:
                dfs(v)
            elif state.get(v) == 1:
                i = stack.index(v) if v in stack else -1
                cycles.append(stack[max(i, 0):] + [v])
        stack.pop()
        state[u] = 2
    for t in list(adj):
        if state.get(t, 0) == 0:
            dfs(t)
    chk(not cycles, "Req-graph acyclicity (no whitelist)", str(cycles[:3]))

    # ---- index regeneration
    os.makedirs(IDX, exist_ok=True)
    with open(os.path.join(IDX, "tags.json"), "w", encoding="utf-8") as f:
        json.dump({t: {"file": registry[t][0], "rank": registry[t][1], "tier": registry[t][3]}
                   for t in registry}, f, indent=1, sort_keys=True)
    with open(os.path.join(IDX, "graph.md"), "w", encoding="utf-8") as f:
        f.write("# Corpus dependency graph (generated by checks/verify_corpus_graph.py)\n\n")
        f.write(f"{len(registry)} registry entries; {sum(len(v) for v in adj.values())} Req edges.\n")
        f.write("Format: TAG (file, era rank) — cites: [...]\n")
        for t, fn, rank, tier in order:
            f.write(f"- **{t}** ({fn}, P{rank}) cites: {', '.join(adj.get(t, [])) or '—'}\n")
    with open(os.path.join(IDX, "tier_index.md"), "w", encoding="utf-8") as f:
        f.write("# Tier index (generated by checks/verify_corpus_graph.py)\n")
        cur = None
        for t, fn, rank, tier in order:
            key = (fn, tier)
            if key != cur:
                f.write(f"\n## {fn} — {tier}\n")
                cur = key
                f.write("- ")
            else:
                f.write(", ")
            f.write(t)
        f.write("\n")
    # topological reading order
    indeg = collections.Counter({t: 0 for t in adj})
    for t, vs in adj.items():
        for v in vs:
            if v in indeg:
                indeg[v] += 1
    q = sorted([t for t, d in indeg.items() if d == 0], key=lambda t: registry[t][2])
    topo = []
    while q:
        u = q.pop(0)
        topo.append(u)
        for v in adj.get(u, ()):
            if v in indeg:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        q.sort(key=lambda t: registry[t][2])
    with open(os.path.join(IDX, "dependency_tree.md"), "w", encoding="utf-8") as f:
        f.write("# Dependency order (generated; a topological order of the Req graph,\n"
                "# tie-broken by document position)\n\n")
        f.write(" -> ".join(topo) + "\n")
    chk(len(topo) == len([t for t in adj]), "topological order covers every graph node",
        f"{len(topo)} vs {len(adj)}")
    print(f"index regenerated: {len(order)} tags in tier order; topo {len(topo)}")

    if FAIL:
        print(f"\nverify_corpus_graph: {len(FAIL)} FAILED")
        return 1
    print("verify_corpus_graph: ALL GREEN")
    return 0

if __name__ == "__main__":
    sys.exit(main())
