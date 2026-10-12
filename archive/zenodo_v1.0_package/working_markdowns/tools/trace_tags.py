#!/usr/bin/env python3
"""
trace_tags.py — summary subset by derivation trace.

Accepts a list of tags and produces the statements of their complete
dependency closure — traced through the **Req.** record all the way down to
the axioms, conventions, definitions, and calibration policies — ordered
dependencies-first, with the trace itself (per-seed ancestor trees and the
citation lists) printed ahead of the statements.

    python3 trace_tags.py D1.2 FT.111                 # -> Summary_subset.md
    python3 trace_tags.py FT.54 --pdf                 # + paper/Summary_subset.pdf
    python3 trace_tags.py BM.1 --out traces/bm1.md --depth 4

Notes:
  * clause suffixes are accepted and stripped (FT.111(3) -> FT.111);
  * dependencies are the canonical **Req.** lines (the same record the
    corpus graph checker verifies); bracketed citations inside statements
    are annotations, not edges;
  * tags that live in HistLog (the adjudication record) are resolved as
    pointers, never imported;
  * --depth N truncates the trace at N levels below the seeds (default: full).
"""
import argparse
import datetime
import os
import re
import sys

import corpus_lib as cl

HERE = os.path.dirname(os.path.abspath(__file__))
TAG_TOKEN = re.compile(r"(Def-(?:H|BM|EM)\.\d+|(?:FT|BM)\.\d+|CT\d+\.\d+[ab]?|"
                       r"EW\.\d+a?|EM\.\d+[ab]?|D[0-4]\.\d+|A[1-9]|C1[0-2]|C[1-9]|"
                       r"P[1-5]|L[0-5]a?)")


def normalize(tok):
    t = tok.strip().rstrip(".,;:")
    t = re.sub(r"\(\d+[a-z]?\).*$", "", t)          # clause suffix
    t = re.sub(r"^Cor\s+", "", t)
    m = TAG_TOKEN.match(t)
    return m.group(1) if m else t


def closure(units_idx, seeds, max_depth=None):
    """BFS over Req edges; returns {tag: depth}."""
    depth = {s: 0 for s in seeds}
    frontier = list(seeds)
    d = 0
    while frontier:
        if max_depth is not None and d >= max_depth:
            break
        nxt = []
        for t in frontier:
            u = units_idx.get(t)
            if not u:
                continue
            for r in sorted(u.reqs):
                if r not in depth and r in units_idx:
                    depth[r] = d + 1
                    nxt.append(r)
        frontier = nxt
        d += 1
    return depth


def topo_order(units_idx, members):
    """Dependencies-first order: DFS post-order over closure edges,
    tie-broken by document position."""
    order = []
    state = {}

    def visit(t):
        state[t] = 1
        u = units_idx.get(t)
        deps = sorted((r for r in (u.reqs if u else ()) if r in members),
                      key=lambda x: units_idx[x].order)
        for r in deps:
            if state.get(r, 0) == 0:
                visit(r)
        state[t] = 2
        order.append(t)

    sys.setrecursionlimit(10000)
    for t in sorted(members, key=lambda x: units_idx[x].order):
        if state.get(t, 0) == 0:
            visit(t)
    return order


def seed_tree(units_idx, seed, members, max_lines=400):
    """Indented ancestor tree for one seed (repeats marked, not expanded)."""
    lines = []
    seen = set()

    def walk(t, prefix, is_last):
        if len(lines) >= max_lines:
            return
        u = units_idx.get(t)
        label = t if u is None else f"{t}"
        conn = "└─ " if is_last else "├─ "
        if t in seen:
            lines.append(prefix + conn + label + "  (↩ above)")
            return
        seen.add(t)
        lines.append(prefix + conn + label)
        deps = sorted((r for r in (u.reqs if u else ()) if r in members),
                      key=lambda x: units_idx[x].order)
        child_prefix = prefix + ("   " if is_last else "│  ")
        for k, r in enumerate(deps):
            walk(r, child_prefix, k == len(deps) - 1)

    lines.append(seed)
    u = units_idx.get(seed)
    deps = sorted((r for r in (u.reqs if u else ()) if r in members),
                  key=lambda x: units_idx[x].order)
    for k, r in enumerate(deps):
        walk(r, "", k == len(deps) - 1)
    return "\n".join(lines)


def build_subset(seeds, max_depth=None):
    units = cl.parse_canon()
    idx = {u.tag: u for u in units}
    unknown = [s for s in seeds if s not in idx]
    if unknown:
        alltags = sorted(idx)
        for bad in unknown:
            near = [t for t in alltags if t.startswith(bad[:4])][:8]
            print(f"unknown tag: {bad}" + (f"  (did you mean: {', '.join(near)}?)" if near else ""))
        return None, None, None
    dep = closure(idx, seeds, max_depth)
    members = set(dep)
    order = topo_order(idx, members)
    from collections import Counter
    kinds = Counter(idx[t].kind for t in order)
    return idx, order, (members, dep, kinds)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tags", nargs="+", help="seed tags, e.g. D1.2 FT.111(3) Def-H.37")
    ap.add_argument("--out", default=os.path.join(HERE, "Summary_subset.md"))
    ap.add_argument("--depth", type=int, default=None,
                    help="truncate the trace N levels below the seeds (default: full)")
    ap.add_argument("--no-statements", action="store_true", help="trace only, no statements")
    ap.add_argument("--pdf", action="store_true", help="also render paper/<out>.pdf")
    args = ap.parse_args()

    seeds = [normalize(t) for t in args.tags]
    idx, order, aux = build_subset(seeds, args.depth)
    if idx is None:
        return 2
    members, dep, kinds = aux

    out = []
    out.append(f"# Qubitick — Summary Subset: derivation trace of {', '.join(seeds)}")
    out.append("")
    out.append(f"*Generated {datetime.date.today().isoformat()} by `trace_tags.py`. "
               f"Dependency closure of the seed tags under the canonical **Req.** record: "
               f"{len(order)} units — {kinds['axiom']} axioms, {kinds['convention']} conventions, "
               f"{kinds['definition']} definitions, {kinds['calibration']} calibration policies, "
               f"{kinds['theorem']} theorem/corollary statements"
               + (f"; trace truncated at depth {args.depth}" if args.depth else "")
               + ". Statements appear dependencies-first; bracketed citations inside statements "
                 "are annotations, not edges. HistLog-resident tags, if cited, are pointers only.*")
    out.append("")
    out.append("## Derivation trace")
    out.append("")
    for s in seeds:
        out.append(f"```")
        out.append(seed_tree(idx, s, members))
        out.append(f"```")
        out.append("")
    out.append("## Closure in dependency order (tag ⇐ its Req citations)")
    out.append("")
    out.append("| # | tag | kind | cites |")
    out.append("| --- | --- | --- | --- |")
    for n, t in enumerate(order, 1):
        u = idx[t]
        cites = ", ".join(sorted((r for r in u.reqs if r in members),
                                 key=lambda x: idx[x].order)) or "—"
        out.append(f"| {n} | {t} | {u.kind} | {cites} |")
    out.append("")
    if not args.no_statements:
        out.append("## Statements (dependencies first)")
        out.append("")
        for t in order:
            u = idx[t]
            stmt = u.statement.strip()
            if not stmt:
                continue
            stmt = re.sub(r"^\*\*" + re.escape(t) + r"\.\*\*\s*", "", stmt).strip()
            title = f" — {u.title}" if u.title and u.title != "(corollary)" else ""
            pre = "Cor " if u.title == "(corollary)" else ""
            out.append(f"### {pre}{t}{title}")
            out.append("")
            out.append(stmt)
            out.append("")

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Summary subset written: {args.out} ({len(order)} units in closure)")

    if args.pdf:
        import render_paper as rp
        outdir = os.path.join(HERE, "paper")
        os.makedirs(outdir, exist_ok=True)
        base = os.path.splitext(os.path.basename(args.out))[0]
        rp.CANON_TITLES[os.path.basename(args.out)] = \
            f"Summary Subset --- Derivation Trace of {', '.join(seeds)}"
        # build_tex reads from render_paper.HERE; write the subset there if needed
        src = os.path.abspath(args.out)
        dst = os.path.join(rp.HERE, os.path.basename(args.out))
        if src != dst:
            import shutil
            shutil.copyfile(src, dst)
        tex = rp.build_tex([os.path.basename(args.out)], datetime.date.today().isoformat())
        tex_path = os.path.join(outdir, base + ".tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex)
        engine = rp.find_engine("auto")
        if not engine:
            print("no LaTeX engine found; .tex kept at", tex_path)
            return 0
        ok = rp.compile_and_repair(tex_path, outdir, engine)
        pdf = os.path.join(outdir, base + ".pdf")
        if ok and os.path.exists(pdf):
            print(f"PDF written: {pdf} ({os.path.getsize(pdf)/1e6:.1f} MB)")
        else:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
