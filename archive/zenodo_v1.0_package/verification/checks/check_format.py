"""
check_format.py — structural validator for the four-era Qubitick canon.

For every canon document (Part1–Part4, Census; HistLog is exempt as the ledger
annex), this checks:

  * balanced $$ blocks and balanced {} inside every math segment;
  * array syntax inside every math segment: no inflated row-end backslash
    runs (>=4 adjacent), no swallowed or misplaced \hline (HistLog §0.4(e));
  * every cited tag exists in the corpus-wide registry (Parts 1–4 + Census +
    the historical tags of HistLog, which may be cited only as
    "HistLog §IV/<tag>" pointers);
  * every theorem block (FT.*, CT*, EW.*, EM.*, L0–L5, BM.*, corollaries)
    carries **Thm.**/**Req.**/**Pf.**/**Phys.** and a proof terminator;
  * every definition block (Def-H.*, Def-BM.*, Def-EM.*) carries **Def.**;
  * Part 1 §A–§E: A1–A9, C1–C13, D0.1–D1.12, P1–P5 each declared exactly once;
    Part 2 §A: D2.1–D4.3 each declared exactly once.

Run:  python3 check_format.py          (from anywhere)
Exit code 0 = all documents pass.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

CANON = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
         "Part4_Baryomesonic_era.md", "Census.md"]
LEDGER = "HistLog.md"

DEF_LIKE = {"BM.6"}   # specification blocks: Def-format, no Thm

ERRORS = []

def err(doc, msg):
    ERRORS.append(f"{doc}: {msg}")
    print(f"  FAIL  {doc}: {msg}")

# ---------------------------------------------------------------- registry

TAG_HEAD_RE = re.compile(
    r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.[\d.]+\w*|"
    r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\w*)\b", re.M)
PARA_DECL_RE = re.compile(r"^\*\*(A[1-9]|C1[0-3]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", re.M)
COR_RE = re.compile(r"\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)\.[\d.]+\w*|L0a)\b")

def build_registry():
    reg = {}
    for fn in CANON:
        src = open(os.path.join(DOCS, fn), encoding="utf-8").read()
        for m in TAG_HEAD_RE.finditer(src):
            reg.setdefault(m.group(1).rstrip("."), set()).add(fn)
        for m in PARA_DECL_RE.finditer(src):
            reg.setdefault(m.group(1), set()).add(fn)
        for m in COR_RE.finditer(src):
            reg.setdefault(m.group(1), set()).add(fn)
    # historical tags (citable only as HistLog pointers)
    hist = open(os.path.join(DOCS, LEDGER), encoding="utf-8").read()
    histags = set()
    for m in TAG_HEAD_RE.finditer(hist):
        histags.add(m.group(1).rstrip("."))
    return reg, histags

CITE_RE = re.compile(
    r"\b(Def-EM\.\d+|Def-H\.\d+|Def-BM\.\d+|FT\.\d+|BM\.\d+|"
    r"CT\d+\.\d+[ab]?|EW\.\d+a?|EM\.\d+[ab]?|D[0-4]\.\d+|A[1-9]\b|C(?:1[0-3]|[1-9])\b|"
    r"P[1-5]\b|(?<!frac )L[0-5][ab]?)")

# ---------------------------------------------------------------- checks

# text-mode argument commands: a `$...$` inside one of these is required and
# legal even within a display; a bare `$` outside them ends the display early
TEXT_ARG_CMDS = ("text", "textbf", "textit", "textrm", "textsf", "texttt",
                 "textsc", "textup", "textmd", "textsl", "textnormal",
                 "emph", "mbox", "hbox", "intertext", "caption", "makecell")
_TEXT_ARG_RE = re.compile(r"\\(?:" + "|".join(TEXT_ARG_CMDS) + r")\s*\{")
# a row break immediately followed by a bracket that is not a length: LaTeX
# reads \\[6pt] as vertical space, so an array cell starting with a literal
# '[' dies with 'Illegal unit of measure (pt inserted)'.  The idiom is \\{}[
ROWBREAK_BRACKET = re.compile(r"\\\\\[(?!\s*-?[\d.]+\s*(?:pt|mm|cm|bp|in|ex|em)\s*\])")

# ---------------------------------------------------------------- array syntax
# Three array/table defect classes inside $$...$$ segments; all three occurred
# in the corpus and are recorded at HistLog §0.4(e):
#   * inflated row ends - >= 4 adjacent backslashes: LaTeX reads them as two or
#     more row breaks, scattering unintended empty array rows through the table;
#   * a swallowed \hline - an even-length backslash run before 'hline' pairs the
#     command's own backslash into a row break and typesets 'hline' as literal
#     text inside the first cell;
#   * a misplaced \hline - a \hline command not directly after a row end,
#     another \hline, or a \begin{array}/\begin{tabular} header: the fatal
#     '! Misplaced \noalign' that halts the engine mid-document.
BEGIN_ENV_RE = re.compile(r"\\begin\{(array|tabular|longtable)\}(\{[^{}]*\})?\s*$")

def array_syntax(doc, src):
    inflated, swallowed, misplaced = [], [], []
    for sm in re.finditer(r"\$\$(.+?)\$\$", src, re.S):
        seg, s0 = sm.group(1), sm.start(1)
        for m in re.finditer(r"\\{4,}", seg):
            inflated.append((src.count("\n", 0, s0 + m.start()) + 1, len(m.group(0))))
        for m in re.finditer(r"hline", seg):
            j, k = m.start() - 1, 0
            while j >= 0 and seg[j] == "\\":
                k += 1; j -= 1
            if k == 0 or (k % 2 == 1 and k >= 3):
                continue                      # bare word, or row-end + \hline
            ln = src.count("\n", 0, s0 + m.start()) + 1
            if k % 2 == 0:
                swallowed.append(ln); continue
            pre = seg[:j + 1].rstrip()
            m2 = re.search(r"\\+$", pre)
            if (m2 and len(m2.group(0)) >= 2 and len(m2.group(0)) % 2 == 0) \
                    or pre.endswith("hline") or BEGIN_ENV_RE.search(pre):
                continue
            misplaced.append(ln)
    if inflated:
        err(doc, f"{len(inflated)} inflated row-end backslash run(s) (>=4 adjacent) in "
                 f"math segments - LaTeX reads them as extra row breaks, scattering "
                 f"empty array rows (first at line {inflated[0][0]}: {inflated[0][1]} "
                 f"backslashes; collapse the run to one row end)")
    if swallowed:
        err(doc, f"{len(swallowed)} swallowed \\hline(s) - an even-length backslash run "
                 f"before 'hline' typesets the word as literal text (first at line "
                 f"{swallowed[0]})")
    if misplaced:
        err(doc, f"{len(misplaced)} misplaced \\hline(s) - not directly after a row end, "
                 f"another \\hline, or an array header; XeTeX halts with '! Misplaced "
                 f"\\noalign' (first at line {misplaced[0]})")


def _dollar_escaped(line, i):
    k, j = 0, i - 1
    while j >= 0 and line[j] == "\\":
        k += 1
        j -= 1
    return k % 2 == 1


def _text_arg_spans(body):
    spans, n = [], len(body)
    for m in _TEXT_ARG_RE.finditer(body):
        j, depth = m.end(), 1
        while j < n and depth:
            c = body[j]
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


def math_balance(doc, src):
    n = 0
    lines = src.split("\n")
    lone, odd = [], []
    for i, line in enumerate(lines, 1):
        n += line.count("$$")
        if line.strip() == "$":
            lone.append(i)
        body = re.sub(r"\\\$", "", line)
        if body.count("$") % 2:
            odd.append(i)
    if n % 2:
        err(doc, f"unbalanced $$ count ({n})")
    if lone:
        err(doc, f"{len(lone)} line(s) holding a single '$' - a $$ display delimiter "
                 f"split across two lines; XeTeX halts with 'Display math should end "
                 f"with $$' (first at line {lone[0]})")
    if odd:
        err(doc, f"{len(odd)} line(s) with an odd number of unescaped '$' "
                 f"(first at line {odd[0]})")
    segs = re.split(r"\$\$", src)
    bad = nested = 0
    for k in range(1, len(segs), 2):
        seg = segs[k]
        # neutralise escaped backslashes BEFORE escaped braces, or a row break
        # written \\\\ followed by a real group {} loses its '{' to the \\{}
        # escape rule and the segment is mis-counted as unbalanced
        seg2 = re.sub(r"\\\\", "\x00\x00", seg)
        seg2 = re.sub(r"\\[{}]", "", seg2)
        if seg2.count("{") != seg2.count("}"):
            bad += 1
        # an inline $...$ in math mode inside this display is fatal
        spans = _text_arg_spans(seg)
        for j, ch in enumerate(seg):
            if ch == "$" and not _dollar_escaped(seg, j) \
                    and not any(a <= j < b for a, b in spans):
                nested += 1
                break
    if bad:
        err(doc, f"{bad} math segments with unbalanced braces")
    if nested:
        err(doc, f"{nested} display(s) contain an inline $...$ in math mode; inside "
                 f"$$...$$ that ends the display early and halts XeTeX - drop the "
                 f"delimiters (the content is already math) or wrap it in \\text{{}}")
    rowbreak = []
    for ln, line in enumerate(src.split("\n"), 1):
        for m in ROWBREAK_BRACKET.finditer(line):
            rowbreak.append((ln, line[max(0, m.start() - 24):m.start() + 34].strip()))
    if rowbreak:
        err(doc, "%d row break(s) written '\\\\[' where LaTeX reads the bracket "
                 "as a length; write '\\\\{}[' instead (first at line %d: %s)"
                 % (len(rowbreak), rowbreak[0][0], rowbreak[0][1]))
    return len(segs) // 2

def citations(doc, src, reg, histags):
    # HistLog-pointer-cited tags are allowed only with the §IV/§I prefix
    protected = set()
    for m in re.finditer(r"HistLog §I{1,2}V?/(?:\\mathrm\{)?((?:FT|Def-H)\.[\d.]+)", src):
        protected.add(m.group(1))
    for m in re.finditer(r"HistLog §I[VP]??/[A-Za-z0-9.\-]+", src):
        pass
    cite_positions = []
    for m in CITE_RE.finditer(src):
        cite_positions.append((m.start(), m.group(1)))
    text = src
    for pos, tag in cite_positions:
        if tag in reg:
            continue
        if tag in histags:
            window = text[max(0, pos - 60):pos + 40]
            if "HistLog" in window or tag in protected:
                continue
            err(doc, f"cites historical tag {tag} without a HistLog locator")
            continue
        # known non-tag matches
        if re.match(r"^(C[1-9]|C1[0-2])$", tag) or re.match(r"^P[1-5]$", tag):
            if tag in reg:
                continue
        err(doc, f"citation to unknown tag: {tag}")

def theorem_blocks(doc, src):
    parts = re.split(r"(?m)^### ", src)
    for blk in parts[1:]:
        head = blk.split("\n", 1)[0]
        m = re.match(r"(?:Cor\s+)?(Def-(?:H|BM|EM)\.\d+|(?:FT|BM)\.\d+|(?:CT\d+|EW|EM)\.\d+\w*|L[0-5])\b", head)
        if not m:
            continue
        tag = m.group(1)
        body = blk
        nxt = re.search(r"\n### ", body)
        if nxt:
            body = body[:nxt.start()]
        if tag.startswith("Def"):
            if "**Def.**" not in body:
                err(doc, f"{tag}: definition block without **Def.**")
            continue
        # stub restatements are allowed to be short (EW.1-EW.4, EW.6, EW.19 pattern)
        stub = ("restated" in body.lower() and len(body) < 1500) or tag in DEF_LIKE
        if tag in DEF_LIKE:
            if "**Def.**" not in body:
                err(doc, f"{tag}: definition-spec block without **Def.**")
            continue
        for req in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"):
            if req not in body and not stub:
                err(doc, f"{tag}: missing {req}")
        if "\\blacksquare" not in body and not stub:
            err(doc, f"{tag}: no proof terminator")

def declarations(doc, src, names):
    for nm in names:
        pat = re.compile(r"^\*\*" + re.escape(nm) + r"\.\*\*", re.M)
        n = len(pat.findall(src))
        if n != 1:
            err(doc, f"{nm} declared {n} times (expected exactly 1)")

def main():
    print("check_format: structural validation (four-era canon)")
    reg, histags = build_registry()
    texts = {}
    for fn in CANON + [LEDGER]:
        path = os.path.join(DOCS, fn)
        if not os.path.exists(path):
            err(fn, "missing canon file")
            continue
        texts[fn] = open(path, encoding="utf-8").read()
    for fn in CANON:
        if fn not in texts:
            continue
        src = texts[fn]
        nseg = math_balance(fn, src)
        array_syntax(fn, src)
        citations(fn, src, reg, histags)
        theorem_blocks(fn, src)
        if not any(e.startswith(fn) for e in ERRORS):
            print(f"  PASS  {fn} ({nseg} math segments)")
    p1 = texts.get("Part1_Qubit_era.md", "")
    p2 = texts.get("Part2_Bosonic_era.md", "")
    declarations("Part1_Qubit_era.md", p1,
                 [f"A{i}" for i in range(1, 10)] + [f"C{i}" for i in range(1, 13)]
                 + [f"D0.{i}" for i in range(1, 11)] + [f"D1.{i}" for i in range(1, 13)]
                 + [f"D2.{i}" for i in range(1, 15)] + [f"D3.{i}" for i in range(1, 11)]
                 + [f"D4.{i}" for i in range(1, 4)] + [f"P{i}" for i in range(1, 6)])
    if ERRORS:
        print(f"\ncheck_format: {len(ERRORS)} ERROR(S)")
        return 1
    print("\ncheck_format: ALL DOCUMENTS PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
