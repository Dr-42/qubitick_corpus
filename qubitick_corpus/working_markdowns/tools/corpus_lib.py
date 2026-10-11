"""
corpus_lib.py — shared parsing of the four-era canon for the summary tools.

Provides, over the canon files (Part1–Part4, Census; HistLog for the open
ledger):
  * every tag unit in document order — the paragraph declarations of Part 1
    (A1–A9, C1–C12, D0.1–D4.3, P1–P5) and the ### tag blocks of all parts;
  * per unit: kind (axiom/convention/definition/calibration/theorem), title,
    statement segments (**Thm.**/**Cor**/**Def.** — no Req/Pf/Phys/Rmk),
    and the Req-citation set (the dependency edges);
  * the open-ledger sections of HistLog (§II.1–§II.3).

Pure stdlib. Used by make_summary.py and trace_tags.py.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

CANON_FILES = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
               "Part4_Baryomesonic_era.md", "Census.md"]
HISTLOG = "HistLog.md"

HEAD_RE = re.compile(
    r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.\d+\w*|"
    r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5])\s*[—–-]?\s*(.*)$")
PARA_RE = re.compile(r"^\*\*(A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", re.M)
COR_RE = re.compile(r"^\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)[\.\d]*\w*)\b[^*]*\*\*", re.M)
TOKEN_RE = re.compile(
    r"\b(Def-EM\.\d+|Def-H\.\d+|Def-BM\.\d+|FT\.\d+|BM\.\d+|"
    r"CT\d+\.\d+[ab]?|EW\.\d+a?|EM\.\d+[ab]?|D[0-4]\.\d+|A[1-9]|C1[0-2]|C[1-9]|P[1-5]|L[0-5]a?)\b")
POINTER_RE = re.compile(r"HistLog §I{1,2}V?\}?/(?:\\mathrm\{)?(?:FT|Def-H)\.\d+\}?")

SEG_RE = re.compile(r"^\*\*([A-Za-z][^*\n]{0,90}?)\.\*\*")

def _classify(head):
    """THM = statement segment; COR = corollary statement; REQ = requirement
    paragraph; SKIP = anything else (Pf/Phys/Rmk/Status/...)."""
    h = head.strip()
    if h.startswith("Thm"):
        return "THM"
    if h == "Def" or h.startswith("Def."):
        return "THM"
    if h.startswith("Cor"):
        return "COR"
    if h.startswith("Req"):
        return "REQ"
    return "SKIP"

KIND_BY_TAG = {}
def kind_of(tag):
    if re.match(r"^A[1-9]$", tag): return "axiom"
    if re.match(r"^C(1[0-2]|[1-9])$", tag): return "convention"
    if re.match(r"^D[0-4]\.\d+$", tag) or tag.startswith("Def-"): return "definition"
    if re.match(r"^P[1-5]$", tag): return "calibration"
    return "theorem"


class Unit:
    __slots__ = ("tag", "title", "kind", "file", "order", "statement", "reqs", "cor_reqs")
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

    def __repr__(self):
        return f"<Unit {self.tag} ({self.kind}) {self.file}>"


def _read(fn):
    with open(os.path.join(HERE, fn), encoding="utf-8") as f:
        return f.read()


def _req_citations(text):
    """Tokens cited in a Req paragraph: HistLog pointers and 'cf.' notes dropped."""
    t = POINTER_RE.sub("", text)
    t = re.sub(r"(?:FT|Def-H)\.\d+ \(HistLog §IV\)", "", t)
    t = re.sub(r"cf\.[^\]$]*", "", t)
    return set(TOKEN_RE.findall(t))


def _split_statements(body):
    """Extract the statement segments (Thm / Cor / Def) of one ### block.
    Returns (statement_text, req_tokens, cor_reqs{cor_tag: tokens})."""
    lines = body.split("\n")
    seg = None
    out = []
    reqs = set()
    cor_reqs = {}
    cur_cor = None
    req_buf = []
    req_is_cor = False
    for ln in lines:
        m = SEG_RE.match(ln)
        if m:
            kind = _classify(m.group(1))
            if kind == "REQ":
                if req_buf:
                    toks = _req_citations("\n".join(req_buf))
                    if req_is_cor and cur_cor:
                        cor_reqs.setdefault(cur_cor, set()).update(toks)
                    reqs |= toks
                seg = "REQ"
                req_buf = [ln[m.end():]]
                req_is_cor = "(Cor)" in m.group(1)
                continue
            if kind in ("THM", "COR"):
                if req_buf:
                    toks = _req_citations("\n".join(req_buf))
                    if req_is_cor and cur_cor:
                        cor_reqs.setdefault(cur_cor, set()).update(toks)
                    reqs |= toks
                    req_buf = []
                seg = "THM"
                if kind == "COR":
                    cm = re.match(r"\*\*Cor\s+([\w\.]+)", ln)
                    cur_cor = cm.group(1).rstrip(".") if cm else None
                    out.append("")
                out.append(ln)
                continue
            # SKIP marker: stop accumulating
            if req_buf:
                toks = _req_citations("\n".join(req_buf))
                if req_is_cor and cur_cor:
                    cor_reqs.setdefault(cur_cor, set()).update(toks)
                reqs |= toks
                req_buf = []
            seg = None
            continue
        if seg == "REQ":
            if ln.strip() == "" or ln.startswith("#") or ln.startswith("---"):
                toks = _req_citations("\n".join(req_buf))
                if req_is_cor and cur_cor:
                    cor_reqs.setdefault(cur_cor, set()).update(toks)
                reqs |= toks
                req_buf = []
                seg = None
                continue
            req_buf.append(ln)
            continue
        if seg == "THM":
            if ln.startswith("##") or ln.strip() == "---":
                seg = None
                continue
            out.append(ln)
    if req_buf:
        reqs |= _req_citations("\n".join(req_buf))
    text = "\n".join(out).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text, reqs, cor_reqs


def _fallback_statement(header, body):
    """For blocks without **Thm.**/**Def.** markers: text up to the first
    **Req.**/**Pf.** paragraph."""
    cut = len(body)
    for pat in ("**Req.", "**Pf.", "**Phys.**", "**Status.**"):
        i = body.find(pat)
        if i >= 0:
            cut = min(cut, i)
    text = body[:cut].strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def parse_canon():
    """All tag units in document order."""
    units = []
    order = 0
    for fn in CANON_FILES:
        src = _read(fn)
        # ---------- paragraph declarations (Part 1 §A–§E style)
        heads = [(m.start(), m.group(1)) for m in PARA_RE.finditer(src)]
        for i, (pos, tag) in enumerate(heads):
            end = heads[i + 1][0] if i + 1 < len(heads) else len(src)
            chunk = src[pos:end]
            # stop at section boundaries
            for stop in ("\n## ", "\n---", "\n### "):
                j = chunk.find(stop, 1)
                if j > 0:
                    chunk = chunk[:j]
            text = chunk.strip()
            stmt = re.sub(r"\n{3,}", "\n\n", text)
            order += 1
            units.append(Unit(tag=tag, title="", kind=kind_of(tag), file=fn,
                              order=order, statement=stmt, reqs=set(), cor_reqs={}))
        # ---------- ### blocks
        marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^###[^\n]*$", src)]
        for i, (pos, head) in enumerate(marks):
            m = HEAD_RE.match(head)
            if not m:
                continue
            tag = m.group(1).rstrip(".")
            title = m.group(2).strip()
            endp = marks[i + 1][0] if i + 1 < len(marks) else len(src)
            # also stop at ## section headers between
            nxt_sec = src.find("\n## ", pos + 4)
            if 0 <= nxt_sec < endp:
                endp = nxt_sec
            body = src[pos:endp]
            body_wo_head = body.split("\n", 1)[1] if "\n" in body else ""
            stmt, reqs, cor_reqs = _split_statements(body_wo_head)
            if not stmt.strip():
                stmt = _fallback_statement(head, body_wo_head)
            # corollary tags declared inside the block join the unit list
            order += 1
            units.append(Unit(tag=tag, title=title, kind=kind_of(tag), file=fn,
                              order=order, statement=stmt, reqs=reqs - {tag},
                              cor_reqs=cor_reqs))
            for cm in COR_RE.finditer(body_wo_head):
                ctag = cm.group(1).rstrip(".")
                if ctag and ctag != tag and re.match(r"^(CT|EW|EM|FT|L[0-5])", ctag):
                    order += 1
                    # corollary statement: from its marker to the next marker
                    ci = body_wo_head.find(cm.group(0))
                    rest = body_wo_head[ci:]
                    cstmt, creqs, _ = _split_statements(rest)
                    if not cstmt.strip():
                        cstmt = _fallback_statement(cm.group(0), rest)
                    units.append(Unit(tag=ctag, title="(corollary)", kind="theorem",
                                      file=fn, order=order, statement=cstmt,
                                      reqs=(creqs | {tag}) - {ctag}, cor_reqs={}))
    # de-dup keeping first occurrence
    seen = set()
    out = []
    for u in units:
        if u.tag in seen:
            continue
        seen.add(u.tag)
        out.append(u)
    return out


def parse_open_ledger():
    """HistLog §II.1 (gap log), §II.2 (Q ledger), §II.3 (declaration requirements)."""
    src = _read(HISTLOG)
    def between(a, b):
        i = src.find(a)
        if i < 0:
            return ""
        i += len(a)
        j = src.find(b, i) if b else len(src)
        return src[i:j if j >= 0 else len(src)].strip()
    g1 = between("**§II.1 Open Gaps Log (canonical ledger text).**", "**§II.2")
    g2 = between("**§II.2 The corpus-internal question ledger Q1–Q12.**", "**§II.3")
    g3 = between("**§II.3 Declaration requirements", "**§II.4")
    return g1, g2, g3


def calibration_sections():
    """Verbatim §Cal-2 / §Cal-F / §Cal-BM sections (free-parameter registries)."""
    out = {}
    for fn, marker in (("Part2_Bosonic_era.md", "## §Cal-2"),
                       ("Part3_Fermion_era.md", "## §Cal-F"),
                       ("Part4_Baryomesonic_era.md", "## §Cal-BM")):
        src = _read(fn)
        i = src.find(marker)
        if i < 0:
            continue
        j = src.find("\n## ", i + 4)
        j = src.find("\n---", i + 4) if j < 0 else min(j, src.find("\n---", i + 4) if src.find("\n---", i + 4) > 0 else j)
        out[marker] = src[i:j].strip()
    return out


def policy_paragraphs():
    """Part 1 §0.2a (hypothesis policy) and §0.3 (free data) — the postulate list."""
    src = _read("Part1_Qubit_era.md")
    out = []
    for marker in ("**0.2a Math & hypothesis policy.**", "**0.3 Free data.**"):
        i = src.find(marker)
        if i < 0:
            continue
        j = src.find("\n\n**", i + 10)
        out.append(src[i:j if j > 0 else i + 4000].strip())
    return out


def build_index(units=None):
    units = units or parse_canon()
    return {u.tag: u for u in units}


if __name__ == "__main__":
    us = parse_canon()
    print("units:", len(us))
    from collections import Counter
    print(Counter(u.kind for u in us))
    idx = {u.tag: u for u in us}
    for t in ("A4", "D1.2", "CT0.9", "FT.111", "FT.17", "Def-H.37", "BM.1", "L0a", "FT.28"):
        u = idx.get(t)
        print("---", t, "->", (u.file if u else "MISSING"),
              "| stmt chars:", len(u.statement) if u else 0,
              "| reqs:", sorted(u.reqs)[:8] if u else [])
