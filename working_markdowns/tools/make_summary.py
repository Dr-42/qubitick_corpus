#!/usr/bin/env python3
"""
make_summary.py — the Summary of Record: every axiom, convention, definition,
postulate/interface clause, calibration policy, and theorem *statement* of the
four-era canon, plus the open ledger — with all proofs, requirement lines,
remarks, and commentary removed.

    python3 make_summary.py               # -> Summary.md
    python3 make_summary.py --pdf         # -> Summary.md + paper/qubitick_summary.pdf
    python3 make_summary.py --out X.md

Statements are extracted segment-wise: **Thm.**/**Cor**/**Def.** blocks only.
Dependency edges are NOT part of the summary (see trace_tags.py for traces).
Postulates appear in place: the interface clauses of Def-H.35–Def-H.43, the
constitutive/scope clauses of the definitions, the extra-axiomatic list
(Part 1 §0.2a), and the free-parameter registries (P4, Cal-2/Cal-F/Cal-BM).
"""
import argparse
import datetime
import os
import re
import sys

import corpus_lib as cl

HERE = os.path.dirname(os.path.abspath(__file__))

PART_HEAD = {
    "Part1_Qubit_era.md": "## Part 1 · Qubit\\_era — axioms, conventions, definitions, pair canon, ledger dynamics",
    "Part2_Bosonic_era.md": "## Part 2 · Bosonic\\_era — geometry, electroweak, electromagnetic, colour, saturation",
    "Part3_Fermion_era.md": "## Part 3 · Fermion\\_era — bound chains, termini, floors, carriers, channels",
    "Part4_Baryomesonic_era.md": "## Part 4 · Baryomesonic\\_era — colour-sealed composites",
    "Census.md": "## Census — the computed cells (statements of the data tags)",
}


def strip_self_tag(tag, stmt):
    return re.sub(r"^\*\*" + re.escape(tag) + r"\.\*\*\s*", "", stmt).strip()


def heading_for(u):
    if u.title and u.title != "(corollary)":
        return f"### {u.tag} — {u.title}"
    if u.title == "(corollary)":
        return f"### Cor {u.tag}"
    return f"### {u.tag}"


def build_summary():
    units = cl.parse_canon()
    gaps1, gaps2, gaps3 = cl.parse_open_ledger()
    cals = cl.calibration_sections()
    pols = cl.policy_paragraphs()

    from collections import Counter
    kinds = Counter(u.kind for u in units)
    n_empty = sum(1 for u in units if not u.statement.strip())

    out = []
    out.append("# Qubitick — Summary of Record")
    out.append("")
    out.append(f"*Generated {datetime.date.today().isoformat()} by `make_summary.py` from the "
               "four-era canon (`Part1–Part4`, `Census.md`, `HistLog.md` §II). "
               "Statements only: axioms, conventions, definitions (including the constitutive "
               "and interface clauses — the postulate surface), calibration policy, theorem and "
               "corollary statements, and the open ledger. Proofs, requirement lines, remarks, "
               "status notes, and commentary are excluded; the full text of every tag lives in "
               "the canon files.*")
    out.append("")
    out.append(f"**Inventory.** {len(units)} tagged units: {kinds['axiom']} axioms · "
               f"{kinds['convention']} conventions · {kinds['definition']} definitions · "
               f"{kinds['calibration']} calibration policies · {kinds['theorem']} theorem/corollary "
               f"statements; open ledger: gap items 1–21, questions Q1–Q12, declaration "
               f"requirements.")
    if n_empty:
        out.append("")
        out.append(f"*Extraction note: {n_empty} tag(s) carry no **Thm.**/**Def.** segment "
                   "(restatement stubs); their full text is in the canon files.*")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Postulates and policy")
    out.append("")
    for p in pols:
        out.append(p)
        out.append("")
    for key in ("## §Cal-2", "## §Cal-F", "## §Cal-BM"):
        if key in cals:
            out.append(cals[key].replace(key, key.replace("## ", "### ")))
            out.append("")
    out.append("---")
    out.append("")

    cur_file = None
    for u in units:
        if u.file != cur_file:
            cur_file = u.file
            out.append(PART_HEAD[cur_file])
            out.append("")
        stmt = u.statement.strip()
        if not stmt:
            continue
        stmt = strip_self_tag(u.tag, stmt)
        out.append(heading_for(u))
        out.append("")
        out.append(stmt)
        out.append("")

    out.append("---")
    out.append("")
    out.append("## Open ledger (HistLog §II)")
    out.append("")
    out.append("### Open Gaps Log (items 1–21; closed items keep one-line closure pointers)")
    out.append("")
    out.append(gaps1)
    out.append("")
    out.append("### The corpus-internal question ledger Q1–Q12")
    out.append("")
    out.append(gaps2)
    out.append("")
    out.append("### Declaration requirements (stated, ¬issued)")
    out.append("")
    out.append(gaps3)
    out.append("")
    return "\n".join(out), units


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=os.path.join(HERE, "Summary.md"))
    ap.add_argument("--pdf", action="store_true", help="also render paper/qubitick_summary.pdf")
    args = ap.parse_args()

    text, units = build_summary()
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Summary written: {args.out} ({len(text.splitlines())} lines, {len(units)} units)")

    if args.pdf:
        import datetime as _dt
        import render_paper as rp
        outdir = os.path.join(HERE, "paper")
        os.makedirs(outdir, exist_ok=True)
        name = os.path.splitext(os.path.basename(args.out))[0]
        tex = rp.build_tex([os.path.basename(args.out)], _dt.date.today().isoformat())
        tex_path = os.path.join(outdir, name + ".tex")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex)
        engine = rp.find_engine("auto")
        if not engine:
            print("no LaTeX engine found; .tex kept at", tex_path)
            return 0
        ok = rp.compile_and_repair(tex_path, outdir, engine)
        pdf = os.path.join(outdir, name + ".pdf")
        if ok and os.path.exists(pdf):
            print(f"PDF written: {pdf} ({os.path.getsize(pdf)/1e6:.1f} MB)")
        else:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
