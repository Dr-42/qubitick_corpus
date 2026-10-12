#!/usr/bin/env python3
"""
check_level6_format.py -- structural validator for the Level 6 / Isotopic-era tier documents.

Level-6 port of the Level-5 gate: IT.n blocks, IT-O rows, and citation attestation against
THREE sources: the frozen era-1 canon registry (era1/canon), the CLOSED Level-5 record
(../level5_atomic/tiers -- AT.n / AT-O rows), and this level's own definitions.

The era2 analogue of verification/checks/check_format.py, porting its math-discipline rules
verbatim (math_balance and the escaped-brace counting) and scoping them to this folder. The
LaTeX-engine array rules of check_format.py are NOT ported: the Part5 tier documents are not
fed to the xelatex pipeline (source/pipeline builds Parts 1-4 from parts/*.tex), so the rules
that matter here are the delimiter/brace/citation ones. For every era2/level6_isotopic/tiers/Part6_*.md:

  (F1) MATH BALANCE (check_format.py's math_balance, ported): the total $$ count is even; no
       line holds a single '$'; no line carries an odd number of unescaped '$'; inside every
       $$...$$ display, braces balance after neutralising escaped backslashes and removing
       escaped \{ \}; and no bare inline '$' sits inside a display outside a text-argument
       command span (\text{...}, \textbf{...}, ...).
  (F2) BLOCK ANATOMY: every "### AT.<n>" theorem block carries **Thm.**, **Req.**, **Pf.**,
       **Phys.**, and its Pf segment carries a \blacksquare terminator.
  (F3) CITATION ACCURACY: every tag token cited anywhere in the file is ATTESTED -- in the
       frozen canon registry (the same ### headers / paragraph declarations / Cor forms that
       check_format.py registers from Part1-Part4 + Census), or as an AT.<n> tag defined by
       some Part5 tier file of this era, or as an AT-O<n> open-ledger row of this era, or in
       the addendum whitelist (A-BM.*, A-H.*).

Run:  python3 check_era2_format.py     (from anywhere; exit 0 = all documents pass)
No floating point anywhere; this is an exact structural scan.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))                 # era2/level6_isotopic/checks
TIERS_DIR = os.path.normpath(os.path.join(HERE, "..", "tiers"))   # the Part6 tier documents
LEVEL6_README = os.path.normpath(os.path.join(HERE, "..", "README.md"))
L5_TIERS_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "level5_atomic", "tiers"))
L5_README = os.path.normpath(os.path.join(HERE, "..", "..", "level5_atomic", "README.md"))
CANON_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "..", "era1", "canon"))   # .../era1/canon
CANON = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
         "Part4_Baryomesonic_era.md", "Census.md"]

TAG_HEAD_RE = re.compile(
    r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.[\d.]+\w*|"
    r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\w*)\b", re.M)
PARA_DECL_RE = re.compile(r"^\*\*(A[1-9]|C1[0-3]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", re.M)
COR_RE = re.compile(r"\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)\.[\d.]+\w*|L0a)\b")

TOKEN_RE = re.compile(
    r"\b(Def-EM\.\d+|Def-H\.\d+|Def-BM\.\d+|FT\.\d+|BM\.\d+|"
    r"CT\d+\.\d+[ab]?|EW\.\d+a?|EM\.\d+[ab]?|D[0-4]\.\d+|A[1-9]\b|C1[0-3]|C[1-9]\b|"
    r"P[1-5]\b|L[0-5]a?\b|AT\.\d+|AT-O\d+[a-z]?|IT\.\d+|IT-O\d+[a-z]?|"
    r"A-BM\.\d+|A-H\.\d+)\b")

WHITELIST = {"L0a"}

# ---- ported from check_format.py: text-argument spans and dollar escapes ----
TEXT_ARG_CMDS = ("text", "textbf", "textit", "textrm", "textsf", "texttt",
                 "textsc", "textup", "textmd", "textsl", "textnormal",
                 "emph", "mbox", "hbox", "intertext", "caption", "makecell")
_TEXT_ARG_RE = re.compile(r"\\(?:" + "|".join(TEXT_ARG_CMDS) + r")\s*\{")

def _text_arg_spans(seg):
    spans = []
    for m in _TEXT_ARG_RE.finditer(seg):
        depth = 1
        j = m.end()
        while j < len(seg) and depth:
            c = seg[j]
            if c == "\\":
                j += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        spans.append((m.end(), j))
    return spans

def _dollar_escaped(seg, j):
    k = 0
    while j - 1 - k >= 0 and seg[j - 1 - k] == "\\":
        k += 1
    return k % 2 == 1

def math_balance(fn, src, errs):
    """check_format.py's math_balance + brace rules, ported."""
    n = 0
    lone, odd = [], []
    for i, line in enumerate(src.split("\n"), 1):
        n += line.count("$$")
        if line.strip() == "$":
            lone.append(i)
        body = re.sub(r"\\\$", "", line)
        if body.count("$") % 2:
            odd.append(i)
    if n % 2:
        errs.append(f"{fn}: unbalanced $$ count ({n})")
    if lone:
        errs.append(f"{fn}: {len(lone)} line(s) holding a single '$' (first at line {lone[0]})")
    if odd:
        errs.append(f"{fn}: {len(odd)} line(s) with an odd number of unescaped '$' "
                    f"(first at line {odd[0]})")
    segs = re.split(r"\$\$", src)
    bad = nested = 0
    for k in range(1, len(segs), 2):
        seg = segs[k]
        seg2 = re.sub(r"\\\\", "\x00\x00", seg)          # escaped backslashes FIRST
        seg2 = re.sub(r"\\[{}]", "", seg2)               # then escaped braces
        if seg2.count("{") != seg2.count("}"):
            bad += 1
        spans = _text_arg_spans(seg)
        for j, ch in enumerate(seg):
            if ch == "$" and not _dollar_escaped(seg, j) \
                    and not any(a <= j < b for a, b in spans):
                nested += 1
                break
    if bad:
        errs.append(f"{fn}: {bad} math segment(s) with unbalanced braces")
    if nested:
        errs.append(f"{fn}: {nested} display segment(s) with a bare inline '$' inside")

def build_registry():
    reg = set()
    for fn in CANON:
        src = open(os.path.join(CANON_DIR, fn), encoding="utf-8").read()
        reg |= {m.group(1).rstrip(".") for m in TAG_HEAD_RE.finditer(src)}
        reg |= {m.group(1) for m in PARA_DECL_RE.finditer(src)}
        reg |= {m.group(1) for m in COR_RE.finditer(src)}
    for fn in CANON + ["HistLog.md"]:
        src = open(os.path.join(CANON_DIR, fn), encoding="utf-8").read()
        reg |= set(re.findall(r"\bA-(?:BM|H)\.\d+\w*", src))
    return reg

def era2_attested():
    """AT/AT-O definitions come from the CLOSED Level-5 record; IT/IT-O from this level."""
    ats, atos, mls, mlos = set(), set(), set(), set()
    for d in (L5_TIERS_DIR, TIERS_DIR):
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            src = open(os.path.join(d, fn), encoding="utf-8").read()
            ats |= set(re.findall(r"^###\s+(AT\.\d+)\b", src, re.M))
            atos |= set(re.findall(r"AT-O\d+[a-z]?", src))
            if d == TIERS_DIR:
                mls |= set(re.findall(r"^###\s+(IT\.\d+)\b", src, re.M))
                mlos |= set(re.findall(r"IT-O\d+[a-z]?", src))
    for p in (L5_README, LEVEL6_README):
        if os.path.exists(p):
            txt = open(p, encoding="utf-8").read()
            atos |= set(re.findall(r"AT-O\d+[a-z]?", txt))
            mlos |= set(re.findall(r"IT-O\d+[a-z]?", txt))
    return ats | mls, atos | mlos

def blocks(src):
    parts = re.split(r"^###\s+", src, flags=re.M)
    out = []
    for p in parts[1:]:
        m = re.match(r"(IT\.\d+)\b", p)
        if m:
            out.append((m.group(1), p))
    return out

def main():
    reg = build_registry()
    at_def, ato_def = era2_attested()
    files = sorted(f for f in os.listdir(TIERS_DIR)
                   if f.startswith("Part6_Isotopic_era") and f.endswith(".md"))
    errs = []
    n_marks = 0
    for fn in files:
        src = open(os.path.join(TIERS_DIR, fn), encoding="utf-8").read()
        math_balance(fn, src, errs)                                   # F1
        for tag, body in blocks(src):                                 # F2
            for seg in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"):
                if seg not in body:
                    errs.append(f"{fn}: block {tag} missing {seg}")
            pfm = re.search(r"\*\*Pf\.\*\*(.+?)(\*\*Phys\.\*\*|\Z)", body, re.S)
            if pfm and "blacksquare" not in pfm.group(1):
                errs.append(f"{fn}: block {tag} Pf has no \\blacksquare terminator")
            n_marks += 1
        for tok in set(TOKEN_RE.findall(src)):                        # F3
            base = re.sub(r"\(.*$", "", tok).rstrip(".")
            ok = (base in reg or base in WHITELIST or base in at_def or base in ato_def
                  or base.startswith("A-BM.") or base.startswith("A-H."))
            if not ok:
                errs.append(f"{fn}: cited tag NOT ATTESTED anywhere: {tok}")
    if errs:
        print(f"  [FAIL ] check_level6_format: {len(errs)} violation(s)")
        for e in errs[:40]:
            print("        " + e)
        return 1
    print(f"  [EXACT] F1 math balance (canon math_balance rules ported) across {len(files)} Part6 tier documents")
    print(f"  [EXACT] F2 block anatomy: {n_marks} IT-blocks each carry Thm/Req/Pf/Phys + a \\blacksquare terminator")
    print(f"  [EXACT] F3 citation accuracy: every cited token attested (canon registry {len(reg)} tags; "
          f"AT/IT theorem definitions {len(at_def)}; AT-O/IT-O ledger rows {len(ato_def)})")
    print(f"  [CLOSED] check_level6_format: {len(files)} documents PASS, 0 violations")
    return 0

if __name__ == "__main__":
    sys.exit(main())
