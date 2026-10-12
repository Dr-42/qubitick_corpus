"""
verify_era_structure.py — structural laws of the four-era canon.

Verifies (exact integer bookkeeping, no floating point):
  §A ownership partition: every FT.1–FT.145 and Def-H.1–Def-H.34 occurs exactly
     once across {Part3, Census}; the interface layer Def-H.35–43, FT.153–155
     exists in Part 3; Part 4 owns Def-BM.1–2, BM.1–6; the 25 Category-B cells
     occur exactly once, in Census, and never in Parts 1–4; the adjudication
     tags FT.115/121/132/140 and the closure tier FT.146–152 occur only in
     HistLog;
  §B census separation: the consumption block carries all 25 cell rows;
  §C declaration hygiene: zero registry tokens (P-H), zero **Status.** lines,
     zero letter-series locators ((**B**)…(**T**), (H01)…(H21), part S/T) in
     the canon files; the interface definitions carry their non-derived clauses;
  §D HistLog integrity: all 22 disposition-ledger rows; the registry entries
     P-H0–P-H20a present in §I.1; gap items 1–21 present in §II.1; the Q1–Q12
     ledger present in §II.2; the status ledger nonempty;
  §E the derived-interface theorems: FT.153, FT.154, FT.155 complete
     (Thm/Req/Pf/Phys) and citing their enabling sets;
  §F era headers: each Part carries Dep/Namespace/DAG-law lines.

Exit 0 = green.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

def rd(fn):
    with open(os.path.join(DOCS, fn), encoding="utf-8") as f:
        return f.read()

P1 = rd("Part1_Qubit_era.md"); P2 = rd("Part2_Bosonic_era.md")
P3 = rd("Part3_Fermion_era.md"); P4 = rd("Part4_Baryomesonic_era.md")
CE = rd("Census.md");          HL = rd("HistLog.md")
CANON = {"Part1": P1, "Part2": P2, "Part3": P3, "Part4": P4, "Census": CE}

FAIL = []
def chk(cond, msg, extra=""):
    if not cond:
        FAIL.append(msg)
        print(f"  FAIL: {msg}" + (f" — {extra}" if extra else ""))
    return cond

def heads(src):
    return [m.group(1).rstrip(".") for m in
            re.finditer(r"(?m)^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.\d+\w*)\b", src)]

B_TAGS = [f"FT.{n}" for n in [28,32,35,42,43,44,45,49,50,51,63,64,65,69,76,78,81,83,84,96,98,99,105,114,120]]
ADJ_TAGS = [f"FT.{n}" for n in [115,121,132,140]]
CLO_TAGS = [f"FT.{n}" for n in range(146,153)]

def main():
    print("verify_era_structure: the laws of the four-era canon")
    h1, h2, h3, h4, hc = (heads(P1), heads(P2), heads(P3), heads(P4), heads(CE))

    # ---------- §A ownership
    p3set, cset = set(h3), set(hc)
    ft_all = [f"FT.{n}" for n in range(1, 146) if f"FT.{n}" not in ADJ_TAGS]
    dh_all = [f"Def-H.{n}" for n in range(1, 35)]
    owned = p3set | cset
    chk(all(t in owned for t in ft_all), "§A every FT.1–FT.145 owned by Part3 ∪ Census",
        str([t for t in ft_all if t not in owned]))
    chk(all(t in owned for t in dh_all), "§A every Def-H.1–Def-H.34 owned",
        str([t for t in dh_all if t not in owned]))
    chk(not (p3set & cset), "§A Part3/Census ownership disjoint", str(sorted(p3set & cset)))
    dup3 = [t for t in h3 if h3.count(t) > 1]; dupc = [t for t in hc if hc.count(t) > 1]
    chk(not dup3 and not dupc, "§A no duplicate headings", str(set(dup3 + dupc)))
    for t in B_TAGS:
        chk(t in cset and t not in p3set, f"§A census cell {t} exactly in Census")
    for t in ["Def-H.35","Def-H.36","Def-H.37","Def-H.38","Def-H.39","Def-H.40",
              "Def-H.41","Def-H.42","Def-H.43","FT.153","FT.154","FT.155"]:
        chk(t in p3set, f"§A interface-layer tag {t} in Part 3")
    for t in ["Def-BM.1","Def-BM.2","BM.1","BM.2","BM.3","BM.4","BM.5","BM.6"]:
        chk(t in set(h4), f"§A Part-4 tag {t} present")
    canon_blob = "\n".join(CANON.values())
    for t in ADJ_TAGS + CLO_TAGS:
        chk(f"### {t} " not in canon_blob, f"§A adjudication tag {t} not a canon section")
        chk(t in HL, f"§A adjudication tag {t} preserved in HistLog")

    # ---------- §B census consumption block
    chk("§Consumption" in CE, "§B Census carries the consumption block")
    for t in B_TAGS:
        chk(f"**{t}.** Space:" in CE, f"§B consumption row {t}")

    # ---------- §C hygiene
    chk(not re.search(r"\bP-H\d", canon_blob), "§C zero registry tokens in canon")
    chk("**Status.**" not in canon_blob, "§C zero Status lines in canon")
    for pat, name in [(r"\(\*\*[A-G]\*\*\)", "letter locators (**A**–**G**)"),
                      (r"\(\*\*[ST]\*\*\)", "letter locators (**S**/**T**)"),
                      (r"\(H\d\d\)", "archive locators (H01–H21)"),
                      (r"\(\*\*H\d\d\*\*\)", "archive locators (**H01**–**H21**)"),
                      (r"\bpart S\b", "'part S'"), (r"\bpart T\b", "'part T'"),
                      (r"letter series", "'letter series'"),
                      (r"\bnon-binding\b", "'non-binding'"),
                      (r"\bWIP\b", "'WIP'")]:
        hits = re.findall(pat, canon_blob)
        chk(not hits, f"§C zero {name} in canon", f"{len(hits)} hits")
    for d, clause in [("Def-H.35","Locus-separation clause (constitutive)"),
                      ("Def-H.36","Derived grounds"),
                      ("Def-H.37","Interface status"),
                      ("Def-H.38","Minimality (derived)"),
                      ("Def-H.39","Bridge slots"),
                      ("Def-H.40","Composition clause (constitutive scope)"),
                      ("Def-H.41","Species (constitutive)"),
                      ("Def-H.42","Species and bars"),
                      ("Def-H.43","Bars (standing)")]:
        i = P3.find(f"### {d} —")
        chk(i >= 0, f"§C {d} section exists")
        if i >= 0:
            j = P3.find("\n### ", i + 4)
            blk = P3[i:j if j > 0 else len(P3)]
            chk(clause in blk, f"§C {d} carries its '{clause}' clause")

    # ---------- §D HistLog integrity
    for n in list(range(0, 16)) + [16, 17, 18, 19, 20]:
        tok = {0:"P-H0",1:"P-H1",2:"P-H2",3:"P-H3",4:"P-H4",5:"P-H5",6:"P-H6",7:"P-H7",
               8:"P-H8",9:"P-H9",10:"P-H10",11:"P-H11",12:"P-H12",13:"P-H13",14:"P-H14",
               15:"P-H15",16:"P-H16a",17:"P-H17a",18:"P-H18a",19:"P-H19a",20:"P-H20a"}[n]
        chk(f"**({tok})**" in HL or f"({tok})" in HL, f"§D registry entry {tok} preserved in HistLog §I")
    rows = re.findall(r"(?m)^\| P-H[\d'$a-z]+.*\|.*\|.*\|", HL)
    chk(len(rows) >= 22, "§D disposition ledger has >= 22 rows", str(len(rows)))
    for n in range(1, 22):
        chk(re.search(rf"(?m)^{n}\. ", HL) is not None, f"§D gap item {n} present in §II.1")
    for q in ["Q1 ","Q2 ","Q3 ","Q4 ","Q5 ","Q6 ","Q7 ","Q8 ","Q9 ","Q10 ","Q11 ","Q12 "]:
        chk(f"| {q}(" in HL or f"| {q.strip()} " in HL or q.strip() in HL, f"§D question {q.strip()} in §II.2")
    chk("§III — The status ledger" in HL and HL.count("**FT.") > 100, "§D status ledger populated")
    chk("§IV" in HL and "FT.146" in HL and "FT.152" in HL, "§D adjudication record present")
    chk("§V" in HL and "56/57" in HL, "§D verification history present")

    # ---------- §E derived-interface theorems
    for t, needs in [("FT.153", ["CT0.6a", "EM.7", "FT.1", "Def-H.35"]),
                     ("FT.154", ["L0(2)", "L0(4)", "L2", "D1.2", "Def-H.40"]),
                     ("FT.155", ["FT.54(1)", "FT.73", "FT.76(3)", "Def-H.37"])]:
        i = P3.find(f"### {t} —")
        chk(i >= 0, f"§E {t} exists in Part 3")
        if i >= 0:
            j = P3.find("\n### ", i + 4)
            blk = P3[i:j if j > 0 else len(P3)]
            for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
                chk(mark in blk, f"§E {t} carries {mark}")
            for c in needs:
                chk(c in blk, f"§E {t} cites {c}")

    # ---------- §F era headers
    for name, src in (("Part1", P1), ("Part2", P2), ("Part3", P3), ("Part4", P4)):
        if name == "Part1":
            chk("**0.1 Corpus map.**" in src and "**0.4 Theorem format" in src,
                "§F Part 1 carries the corpus map and the format spec")
        else:
            chk("**Dep.**" in src, f"§F {name} carries Dep")
            chk("**Namespace.**" in src, f"§F {name} carries Namespace")
            chk("**DAG law.**" in src, f"§F {name} carries the DAG law")
    chk("Charter.**" in P4 and "BM.6" in P4, "§F Part 4 carries the charter and BM.6")

    if FAIL:
        print(f"\nverify_era_structure: {len(FAIL)} FAILED")
        return 1
    print("verify_era_structure: ALL GREEN")
    return 0

if __name__ == "__main__":
    sys.exit(main())
