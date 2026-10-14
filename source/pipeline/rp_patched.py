#!/usr/bin/env python3
r"""
render_paper.py — render the four-era Qubitick canon as a formal LaTeX paper (PDF).

Usage:
    python3 render_paper.py                    # -> paper/qubitick_corpus.{tex,pdf}
                                               #    (preface + Parts 1-4 + Census)
    python3 render_paper.py --include-histlog  # also render the HistLog annex
    python3 render_paper.py --engine xelatex
    python3 render_paper.py --fetch-engine     # download a self-contained tectonic

Pipeline: a corpus-aware Markdown -> LaTeX converter (math spans pass through
verbatim — the corpus is already LaTeX math), then a compile-and-repair loop:

  1. compile with tectonic (XeLaTeX; auto re-runs for TOC/refs) or the engine
     selected via --engine;
  2. parse the log for overfull boxes:
       * "detected at line N"      -> the enclosing display \[...\] is too wide:
                                      it is first BROKEN into stacked displays
                                      at the corpus's own top-level clause
                                      separators (stage 1 \qquad, stage 2
                                      \quad, stage 3 top-level ; , and
                                      relations =, \implies, \iff, ... —
                                      never inside braces, \begin..\end
                                      environments, \left..\right or
                                      \bigl..\bigr groups, or parentheses),
                                      and only the still-too-wide unbreakable
                                      residue is progressively scaled (\small
                                      -> \footnotesize -> \scriptsize ->
                                      \resizebox to \textwidth); wide displays
                                      are also broken proactively at build
                                      time (measured with the table estimator);
       * "in paragraph at lines"   -> the paragraph is wrapped in sloppypar
                                      with a local \emergencystretch bump;
       * "in alignment at lines"   -> the enclosing longtable drops one font
                                      size (tables start at a size chosen from
                                      measured rendered cell widths);
  3. recompile; iterate until the log is clean of >8pt overfulls
     (--max-repair-rounds, default 8; the loop also stops when a round
     applies no further fixes).

Tables are laid out with measured widths: every cell's *rendered* length is
estimated (LaTeX markup stripped, math reduced to its visible glyphs) and the
longest unbreakable chunk in each column sets a width floor, so math-heavy
cells no longer bleed into their neighbours. All columns are wrapping
p-columns (ragged right); nothing uses the non-wrapping `l` spec.

Pure stdlib. Exit 0 = PDF written.
"""
import argparse
import datetime
import html
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

CANON = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
         "Part4_Baryomesonic_era.md"]

CANON_TITLES = {
    "Part1_Qubit_era.md": "Part 1 · Qubit\\_era --- Axioms, Conventions, Definitions, Pair Canon, Ledger Dynamics",
    "Part2_Bosonic_era.md": "Part 2 · Bosonic\\_era --- Geometry, Electroweak, Electromagnetic, Colour, Saturation",
    "Part3_Fermion_era.md": "Part 3 · Fermion\\_era --- Bound Chains, Termini, Floors, Carriers, Channels",
    "Part4_Baryomesonic_era.md": "Part 4 · Baryomesonic\\_era --- Colour-Sealed Composites",
    "Census.md": "Census --- The Computed Cells and Their Consumption",
    "HistLog.md": "HistLog --- The Historical and Open Ledger",
    "README.md": "Preface --- The Corpus Map",
    "Summary.md": "Summary of Record --- Axioms, Definitions, Postulates, Theorem Statements, Open Gaps",
    "Summary_subset.md": "Summary Subset --- Derivation Trace",
}

# ---------------------------------------------------------------- math protection

class Protector:
    """Replace math/code spans with opaque placeholders; restore after text ops."""
    def __init__(self):
        self.store = {}
        self.n = 0

    def _key(self, s):
        self.n += 1
        k = f"\x00P{self.n}\x00"
        self.store[k] = s
        return k

    def protect(self, text):
        out = []
        i = 0
        n = len(text)
        while i < n:
            c = text[i]
            if c == "`" and text.startswith("```", i):
                j = text.find("```", i + 3)
                j = j + 3 if j >= 0 else n
                out.append(self._key(text[i:j])); i = j; continue
            if c == "`":
                j = text.find("`", i + 1)
                if j > i:
                    out.append(self._key(text[i:j + 1])); i = j + 1; continue
            if c == "$":
                if text.startswith("$$", i):
                    j = text.find("$$", i + 2)
                    j = j + 2 if j >= 0 else n
                    out.append(self._key(text[i:j])); i = j; continue
                j = i + 1
                while j < n:
                    if text[j] == "\\" and j + 1 < n:
                        j += 2; continue
                    if text[j] == "$":
                        break
                    if text[j] == "\n":
                        j = -1; break
                    j += 1
                if j > i and j < n:
                    out.append(self._key(text[i:j + 1])); i = j + 1; continue
            out.append(c); i += 1
        return "".join(out)

    def restore(self, text):
        for _ in range(6):
            done = True
            for k, v in self.store.items():
                if k in text:
                    text = text.replace(k, v)
                    done = False
            if done:
                break
        return text

# ---------------------------------------------------------------- text conversion

UNICODE_MAP = {
    "→": "$\\to$", "↦": "$\\mapsto$", "⟹": "$\\implies$", "⇒": "$\\Rightarrow$",
    "↔": "$\\leftrightarrow$", "⇔": "$\\iff$", "∈": "$\\in$", "∉": "$\\notin$",
    "¬": "$\\neg$", "∧": "$\\wedge$", "∨": "$\\vee$", "⊆": "$\\subseteq$",
    "∅": "$\\varnothing$", "∂": "$\\partial$", "∇": "$\\nabla$", "∀": "$\\forall$",
    "∃": "$\\exists$", "∞": "$\\infty$", "≈": "$\\approx$", "≠": "$\\ne$",
    "≤": "$\\le$", "≥": "$\\ge$", "×": "$\\times$", "±": "$\\pm$",
    "∑": "$\\sum$", "∏": "$\\prod$", "⊗": "$\\otimes$", "⊕": "$\\oplus$",
    "⟨": "$\\langle$", "⟩": "$\\rangle$", "∴": "$\\therefore$",
    "γ": "$\\gamma$", "Ω": "$\\Omega$", "ω": "$\\omega$", "α": "$\\alpha$",
    "β": "$\\beta$", "μ": "$\\mu$", "δ": "$\\delta$", "Θ": "$\\Theta$",
    "ℤ": "$\\mathbb{Z}$", "ℚ": "$\\mathbb{Q}$", "ℝ": "$\\mathbb{R}$",
    "ℂ": "$\\mathbb{C}$", "ℕ": "$\\mathbb{N}$", "ℓ": "$\\ell$",
    "𝔥": "$\\mathfrak{h}$", "𝔏": "$\\mathfrak{L}$", "𝔖": "$\\mathfrak{S}$",
    "𝔗": "$\\mathfrak{T}$", "𝔉": "$\\mathfrak{F}$", "𝔐": "$\\mathfrak{M}$",
    "𝔑": "$\\mathfrak{N}$", "𝔈": "$\\mathfrak{E}$", "𝔘": "$\\mathfrak{U}$",
    "𝔇": "$\\mathfrak{D}$", "𝔎": "$\\mathfrak{N}$", "𝔠": "$\\mathfrak{c}$",
    "₂": "$_2$", "₃": "$_3$", "₄": "$_4$", "₅": "$_5$", "₁": "$_1$", "₀": "$_0$",
    "½": "$\\tfrac12$", "′": "$'$", "✓": "\\checkmark{}", "✗": "$\\times$",
    "∎": "$\\blacksquare$", "⌈": "$\\lceil$", "⌉": "$\\rceil$",
    "⌊": "$\\lfloor$", "⌋": "$\\rfloor$",
}

def escape_specials(s):
    """Escape bare LaTeX specials in a text span (backslash sequences kept)."""
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            out.append(s[i:i + 2]); i += 2; continue
        if c in "#%&_{}~^":
            out.append({
                "#": "\\#", "%": "\\%", "&": "\\&", "_": "\\_",
                "{": "\\{", "}": "\\}", "~": "\\textasciitilde{}",
                "^": "\\textasciicircum{}",
            }[c]); i += 1; continue
        out.append(c); i += 1
    return "".join(out)

def md_inline(s):
    """Markdown inline formatting on an escaped, math-protected span."""
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r"\\href{\2}{\1}", s)
    s = re.sub(r"\*\*([^*]+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"\\textit{\1}", s)
    return s

CODE_ESC = {"#": "\\#", "%": "\\%", "&": "\\&", "_": "\\_",
            "{": "\\{", "}": "\\}", "~": "\\textasciitilde{}",
            "^": "\\textasciicircum{}", " ": "\\ ", "$": "\\$",
            "\\": "\\textbackslash{}"}

def _code_ttf(inner):
    inner = re.sub(r"[#%&_{}~^ $\\]", lambda x: CODE_ESC[x.group(0)], inner)
    # break opportunities inside long tt names (checker filenames etc.);
    # {} terminates the control-sequence name (\allowbreakQ... would be one token)
    inner = inner.replace("\\_", "\\_\\allowbreak{}").replace("/", "/\\allowbreak{}")
    return "\\texttt{" + inner + "}"

def conv_text(raw, prot):
    """Full inline conversion of one text span (math/code as placeholders)."""
    s = prot.protect(raw)

    s = escape_specials(s)

    def repl(m):
        v = prot.store[m.group(0)]
        if v.startswith("```"):
            inner = v[3:-3]
            inner = inner.replace("\\", "\\textbackslash{}").replace("{", "\\{").replace("}", "\\}")
            return "\\begin{verbatim}" + inner + "\\end{verbatim}"
        if v.startswith("`"):
            return _code_ttf(v[1:-1])
        return m.group(0)

    s = re.sub(r"\x00P\d+\x00", repl, s)
    for u, rep in UNICODE_MAP.items():
        s = s.replace(u, rep)
    s = md_inline(s)
    # restore, promoting huge inline-math spans to displays (they cannot
    # break across lines and would overflow the text block)
    def promote(k):
        v = prot.store[k]
        if v.startswith("$$"):
            return v
        if v.startswith("$") and v.endswith("$") and len(v) > 2:
            inner = v[1:-1]
            if visible_len(inner) > 140:
                b = repair_display(inner).strip()
                frags = _proactive_frags(b) if ("\\begin{" not in b
                                                and visible_len(b) > DSP_WIDTH) else [b]
                return "\n" + "\n".join(
                    DSP_MARKER_EARLY + "\n\\[\n" + f + "\n\\]" for f in frags) + "\n"
        return v
    for _ in range(6):
        done = True
        for k in list(prot.store):
            if k in s:
                s = s.replace(k, promote(k))
                done = False
        if done:
            break
    return s

# ---------------------------------------------------------------- display-math repair

MATH_ENVS = ("array", "aligned", "cases", "matrix", "pmatrix", "bmatrix",
             "Bmatrix", "vmatrix", "smallmatrix", "substack", "tabular",
             "split", "gathered", "align", "flalign", "multline")

def repair_display(body):
    """Neutralize \\\\ line breaks outside tabular-like environments, and brace
    array rows that start with '[' (the optional-argument trap of \\\\)."""
    out = []
    i = 0
    depth = 0
    while i < len(body):
        m = re.match(r"\\begin\{(" + "|".join(MATH_ENVS) + r")\}", body[i:])
        if m:
            depth += 1; out.append(m.group(0)); i += m.end(); continue
        m = re.match(r"\\end\{(" + "|".join(MATH_ENVS) + r")\}", body[i:])
        if m:
            depth = max(0, depth - 1); out.append(m.group(0)); i += m.end(); continue
        if body[i:i + 2] == "\\\\" and depth == 0:
            out.append("\\ "); i += 2; continue
        out.append(body[i]); i += 1
    s = "".join(out)
    # a row break '\\' immediately followed by '[' is read by LaTeX as the
    # optional vertical-space argument, so a cell that begins with a literal '['
    # dies with "Illegal unit of measure (pt inserted)".  Insert {} unless the
    # bracket really is a length.  The newline in \1 is optional: the corpus
    # writes some arrays on one line.
    s = re.sub(r"\\\\(\s*\n?\s*)\[(?!\s*-?[\d.]+\s*(?:pt|mm|cm|bp|in|ex|em)\s*\])",
               r"\\\\\1{}[", s)
    return s

# ---------------------------------------------------------------- display-math hygiene
#
# Two source-level defects used to reach the engine and halt it with the
# unhelpful "! Display math should end with $$":
#
#   * a display delimiter written as two lines each holding a single `$`
#     instead of one line holding `$$`.  check_format.py counts `$$` per line,
#     so such a line contributed nothing and the file passed validation.
#   * inline `$...$` sitting directly in math mode inside a display.  Inside
#     \[ ... \] we are already in math mode, so a bare `$` ends the display
#     early.  The same `$...$` *inside a text-mode argument* (\text, \textbf,
#     \emph, \mbox, ...) is required and legal, so those are preserved.
#     Verified against xelatex: bare -> fatal, in-text -> fine, delimiters
#     removed -> fine.
TEXT_ARG_CMDS = ("text", "textbf", "textit", "textrm", "textsf", "texttt",
                 "textsc", "textup", "textmd", "textsl", "textnormal",
                 "emph", "mbox", "hbox", "intertext", "caption", "makecell")
_TEXT_ARG_RE = re.compile(r"\\(?:" + "|".join(TEXT_ARG_CMDS) + r")\s*\{")


def _escaped(body, i):
    """is body[i] preceded by an odd number of backslashes (i.e. escaped)?"""
    k, j = 0, i - 1
    while j >= 0 and body[j] == "\\":
        k += 1
        j -= 1
    return k % 2 == 1


def _text_arg_spans(body):
    """(start, end) index spans of every text-mode argument body"""
    spans = []
    n = len(body)
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


def desugar_inline_math(body):
    """drop `$` delimiters that sit in math mode; keep those inside \text-like
    arguments.  Returns (new_body, n_dropped)."""
    spans = _text_arg_spans(body)
    out, dropped = [], 0
    for i, ch in enumerate(body):
        if ch == "$" and not _escaped(body, i):
            if any(a <= i < b for a, b in spans):
                out.append(ch)
            else:
                dropped += 1
            continue
        out.append(ch)
    return "".join(out), dropped


def lone_dollar_lines(src):
    """line numbers whose only content is a single `$`: a `$$` split in two"""
    return [i for i, l in enumerate(src.split("\n"), 1) if l.strip() == "$"]


# ---------------------------------------------------------------- smart display breaking

DSP_WIDTH = 80          # visible chars that comfortably fit one display line at normalsize
STATS = {"desugared": 0, "norm_delims": 0}

SPLIT_TOKENS = {
    1: [("before", "\\qquad", False)],
    2: [("before", "\\quad", True)],
    3: [("after", ";", False), ("after", ",", False),
        ("before", "\\Longleftrightarrow", True), ("before", "\\Longrightarrow", True),
        ("before", "\\longrightarrow", True), ("before", "\\implies", True),
        ("before", "\\iff", True), ("before", "\\Rightarrow", True),
        ("before", "\\mapsto", True), ("before", "\\equiv", True),
        ("before", "\\neq", True), ("before", "\\ne", True),
        ("before", "\\subseteq", True), ("before", "\\in", True),
        ("before", "\\le", True), ("before", "\\ge", True),
        ("before", "=", False)],
}
_OPEN_DELIMS = ("left", "bigl", "Bigl", "biggl", "Biggl")
_CLOSE_DELIMS = ("right", "bigr", "Bigr", "biggr", "Biggr")
_DELIM_RE = re.compile(r"\\(" + "|".join(_OPEN_DELIMS + _CLOSE_DELIMS) + r")(?![a-zA-Z])")
_DELIM_ARG_RE = re.compile(r"\\[a-zA-Z]+|\\.")


def _split_display(body, stage):
    """Split a display body at the stage's top-level separators.

    Depth-tracked (never split inside): braces {}, \\begin..\\end environments,
    \\left..\\right and \\bigl..\\bigr families, bare parentheses. 'before'
    tokens open the next fragment; 'after' tokens close the current one.
    Returns a list of >= 2 fragments, or [] when the body does not break.
    """
    toks = SPLIT_TOKENS[stage]
    parts, cur = [], []
    depth = envd = deld = pard = 0
    i, n = 0, len(body)
    while i < n:
        if body.startswith("\\begin{", i):
            m = re.match(r"\\begin\{[a-zA-Z*]+\}", body[i:])
            if m:
                envd += 1; cur.append(m.group(0)); i += m.end(); continue
        if body.startswith("\\end{", i):
            m = re.match(r"\\end\{[-\w*]+\}", body[i:])
            if m:
                envd = max(0, envd - 1); cur.append(m.group(0)); i += m.end(); continue
        if depth == 0 and envd == 0 and deld == 0 and pard == 0:
            hit = None
            for kind, tok, alpha in toks:
                if body.startswith(tok, i):
                    if alpha:
                        j = i + len(tok)
                        if j < n and (body[j].isalpha() or body[j] == "\\") and tok.startswith("\\"):
                            continue        # a longer command with this prefix
                    hit = (kind, tok); break
            if hit:
                kind, tok = hit
                if kind == "before":
                    frag = "".join(cur).strip(" \n")
                    if frag:
                        parts.append(frag)
                    cur = [tok + " "]; i += len(tok)
                else:
                    cur.append(tok); i += len(tok)
                    frag = "".join(cur).strip(" \n")
                    if frag:
                        parts.append(frag)
                    cur = []
                while i < n and body[i] in " \n":
                    i += 1
                continue
        ch = body[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth = max(0, depth - 1)
        elif ch in "([":
            pard += 1
        elif ch in ")]":
            pard = max(0, pard - 1)
        elif ch == "\\":
            m = _DELIM_RE.match(body, i)
            if m:
                deld = deld + 1 if m.group(1) in _OPEN_DELIMS else max(0, deld - 1)
                cur.append(m.group(0)); i = m.end()
                m2 = _DELIM_ARG_RE.match(body, i)      # the delimiter itself
                if m2:
                    cur.append(m2.group(0)); i = m2.end()
                elif i < n:
                    cur.append(body[i]); i += 1
                continue
        cur.append(ch); i += 1
    frag = "".join(cur).strip(" \n")
    if frag:
        parts.append(frag)
    if len(parts) > 1 and len(parts[-1]) <= 18:
        parts[-2] = parts[-2] + "\\qquad " + parts[-1]
        parts.pop()
    if len(parts) > 1 and len(parts[0]) <= 2:
        parts[1] = parts[0] + " " + parts[1]
        parts.pop(0)
    return parts if len(parts) > 1 else []


def _proactive_frags(body):
    """Break fragments wider than DSP_WIDTH at progressively deeper stages."""
    frags = [body]
    for stage in (1, 2, 3):
        if all(visible_len(f) <= DSP_WIDTH for f in frags):
            break
        nxt = []
        for f in frags:
            if visible_len(f) > DSP_WIDTH:
                pieces = _split_display(f, stage)
                if pieces:
                    nxt.extend(pieces)
                    continue
            nxt.append(f)
        frags = nxt
    return frags


def display_latex(body):
    """Emit one display (or a stack of them) for a $$-body: wide clause-
    structured bodies are broken proactively at build time; the compile-and-
    repair loop owns the residue."""
    body = repair_display(body).strip()
    frags = [body]
    if "\\begin{" not in body and visible_len(body) > DSP_WIDTH:
        frags = _proactive_frags(body)
    if len(frags) > 1:
        rows = []
        for f in frags:
            rows += [DSP_MARKER_EARLY, "\\[", f, "\\]", ""]
        return "\n".join(rows)
    return DSP_MARKER_EARLY + "\n\\[\n" + body + "\n\\]\n"


DSP_MARKER_EARLY = "%dsp-level:0"

# ---------------------------------------------------------------- measured tables

CMD_UNWRAP = re.compile(
    r"\\(?:mathrm|mathbf|mathit|mathsf|mathtt|text|textbf|textit|textrm|texttt|"
    r"operatorname|mathcal|mathfrak|mathbb|hat|widehat|tilde|bar|vec|overline|"
    r"underline|bm)\s*\{([^{}]*)\}")

def visible_len(src):
    """Approximate rendered character count of a LaTeX fragment."""
    t = src
    for _ in range(5):
        t2 = CMD_UNWRAP.sub(r"\1", t)
        if t2 == t:
            break
        t = t2
    t = re.sub(r"\\(?:begin|end)\s*\{[^{}]*\}", " ", t)
    t = re.sub(r"\\(?:left|right|bigl|bigr|Bigl|Bigr|displaystyle|quad|qquad|;|,|!| )", " ", t)
    t = re.sub(r"\\[a-zA-Z]+", "nn", t)      # a remaining command ~ 2 glyphs
    t = re.sub(r"\\.", "n", t)
    t = re.sub(r"[{}$\\^_&~\u200b]", "", t)
    t = re.sub(r"\s+", "", t)
    return len(t)

BREAK_TOKENS = ("\\iff", "\\implies", "\\longmapsto", "\\mapsto", "\\le", "\\ge",
                "\\ne", "\\in", "=", "<", ">", ",", "+")


def _math_allowbreak(cell):
    """Insert \\allowbreak at top-level relation/operator points inside inline
    math, so a wrapping p-column cell can break inside its math instead of
    bleeding into its neighbour.  Only $...$ spans are touched; braces are
    depth-tracked so nothing breaks inside a macro argument or a \\text{...}."""
    out = []
    i = 0
    n = len(cell)
    while i < n:
        c = cell[i]
        if c == "$" and not cell.startswith("$$", i):
            j = cell.find("$", i + 1)
            if j < 0:
                out.append(cell[i:])
                break
            span = cell[i + 1:j]
            out.append("$")
            depth = 0
            k = 0
            while k < len(span):
                tok = None
                if span[k] == "{":
                    depth += 1
                elif span[k] == "}":
                    depth -= 1
                elif depth == 0 and span[k] == "\\":
                    for t in BREAK_TOKENS:
                        if t.startswith("\\") and span.startswith(t, k):
                            tok = t
                            break
                elif depth == 0 and span[k] in "=<>,+":
                    tok = span[k]
                if tok:
                    out.append(tok)
                    k += len(tok)
                    # a break is useful only between two visible atoms
                    if k < len(span) and span[k] not in "})" and span[k:k + 1] != "\\":
                        out.append("\\allowbreak ")
                    elif k < len(span):
                        out.append("\\allowbreak ")
                    continue
                out.append(span[k])
                k += 1
            out.append("$")
            i = j + 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


def cell_metrics(cell):
    """(rendered length, longest unbreakable chunk) of one markdown cell."""
    total = 0
    chunk = 0
    for part in re.split(r"(\$\$[^$]*\$\$|\$[^$]*\$)", cell):
        if part.startswith("$") and part.endswith("$") and len(part) > 2:
            inner = part.strip("$").replace("\\allowbreak", "\x00")
            total += visible_len(inner.replace("\x00", ""))
            for piece in inner.split("\x00"):
                chunk = max(chunk, visible_len(piece))
        elif part:
            total += visible_len(part)
            for w in re.split(r"\s+", part):
                chunk = max(chunk, visible_len(w))
    return total, chunk

SIZE_STEPS = [("", 92), ("\\small", 112), ("\\footnotesize", 132), ("\\scriptsize", 158)]
TABLE_MARKER = "%tbl-level:"

def render_table(rows, prot):
    header = [_math_allowbreak(c) for c in split_row(rows[0], prot)]
    if len(rows) > 1 and is_sep_row(rows[1]):
        body = [[_math_allowbreak(c) for c in split_row(r, prot)] for r in rows[2:]]
    else:
        body = [[_math_allowbreak(c) for c in split_row(r, prot)] for r in rows[1:]]
    ncols = max([len(header)] + [len(r) for r in body]) if body else len(header)
    header += [""] * (ncols - len(header))
    body = [r + [""] * (ncols - len(r)) for r in body]

    tot = [0] * ncols
    chk = [0] * ncols
    for r in [header] + body:
        for c in range(ncols):
            t, k = cell_metrics(r[c])
            tot[c] = max(tot[c], t)
            chk[c] = max(chk[c], k)

    level = 0
    if ncols > 6:
        level = max(level, 1)
    while level < 3 and sum(tot) > SIZE_STEPS[level][1]:
        level += 1
    cap = SIZE_STEPS[level][1]
    while level < 3 and max(chk) * 1.12 > cap:
        level += 1
        cap = SIZE_STEPS[level][1]

    # column fractions: share of totals, floored by the unbreakable chunk
    grand = sum(tot) or 1
    fr = []
    for c in range(ncols):
        share = max(tot[c] / grand, 0.06)
        floor = min(0.85, (chk[c] * 1.15 + 3) / cap)
        fr.append(max(share, floor))
    s = sum(fr)
    fr = [f / s for f in fr]
    # re-apply chunk floors after normalization, then renormalize once more
    for c in range(ncols):
        fr[c] = max(fr[c], min(0.85, (chk[c] * 1.15 + 3) / cap / 1.0))
    s = sum(fr)
    fr = [f / s for f in fr]

    colspec = "|".join(
        ">{\\raggedright\\arraybackslash}p{\\dimexpr%.4f\\textwidth-2\\tabcolsep\\relax}" % f
        for f in fr)
    size = SIZE_STEPS[level][0]
    out = [f"{TABLE_MARKER}{level}",
           "{" + size + "\\setlength{\\tabcolsep}{4pt}"]
    out.append("\\begin{longtable}{" + colspec + "}")
    hcells = lambda cells: " & ".join(conv_text(c, Protector()) for c in cells)
    out += ["\\toprule", hcells(header) + " \\\\", "\\addlinespace[2pt]", "\\midrule", "\\endfirsthead"]
    out += ["\\toprule", hcells(header) + " \\\\", "\\addlinespace[2pt]", "\\midrule", "\\endhead"]
    out += ["\\bottomrule", "\\endlastfoot"]
    for r in body:
        out.append(hcells(r) + " \\\\")
    out += ["\\end{longtable}", "}"]
    return "\n".join(out)

def split_row(line, prot):
    p = prot.protect(line)
    cells = [c.strip() for c in p.strip().strip("|").split("|")]
    return [prot.restore(c) for c in cells]

def is_sep_row(line):
    return bool(re.fullmatch(r"\|?[\s:|-]+\|?", line)) and "-" in line

# ---------------------------------------------------------------- headings

TAG_IN_HEAD = re.compile(
    r"((?:Def-(?:H|BM|EM)\.\d+|(?:FT|BM)\.\d+|CT\d+\.\d+[ab]?|EW\.\d+a?|EM\.\d+[ab]?|"
    r"L[0-5]a?|A[1-9]|C1[0-3]|D[0-4]\.\d+|P[1-5])\b)")

def pdf_safe(s):
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?", " ", s)
    s = re.sub(r"[{}\\]", " ", s)
    s = html.unescape(s)
    s = (s.replace("—", "-").replace("–", "-").replace("§", "S").replace("·", "-")
          .replace("“", '"').replace("”", '"').replace("’", "'").replace("…", "..."))
    s = re.sub(r"[^\x20-\x7e]", "", s)
    return re.sub(r"\s+", " ", s).strip()

def short_head(text, limit=52):
    """the running-head / TOC form of a heading: everything before the first
    em dash, else the leading tag, else a truncated prefix.  Tier titles run to
    150+ characters and an untruncated mark overflows the header box."""
    for dash in ("\u2014", "---", "\u2013"):
        if dash in text:
            head = text.split(dash)[0].strip()
            if head:
                return head[:limit]
    t = text.strip()
    return t if len(t) <= limit else t[:limit - 1].rstrip() + "\u2026"


def render_heading(level, text, prot):
    conv = conv_text(text, prot)
    safe = pdf_safe(text)
    m = TAG_IN_HEAD.search(text)
    label = ""
    if level >= 3 and m:
        label = "\\label{tag:" + re.sub(r"[^A-Za-z0-9]", "-", m.group(1)) + "}"
    cmd = {1: "chapter", 2: "section", 3: "subsection", 4: "subsubsection"}[level]
    # a short optional argument keeps the running head and the TOC readable;
    # the full title still reaches the PDF bookmark through \texorpdfstring
    opt = ""
    if level == 2:
        opt = "[" + conv_text(short_head(text), prot).replace("[", "{[").replace("]", "]}") + "]"
    return (f"\\phantomsection\n\\{cmd}{opt}{{\\texorpdfstring{{{conv}}}{{{safe}}}}}"
            f"{label}\n")

# ---------------------------------------------------------------- block conversion

def convert_md(src, prot):
    lines = src.split("\n")
    out = []
    i = 0
    n = len(lines)
    para = []

    def flush_para():
        if para:
            out.append(conv_text(" ".join(x.strip() for x in para), prot))
            out.append("")
            para.clear()

    while i < n:
        ln = lines[i]
        st = ln.strip()
        if st.startswith("```"):
            flush_para()
            j = i + 1
            buf = []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j]); j += 1
            code = "\n".join(buf)
            code = code.replace("\\", "\\textbackslash{}").replace("{", "\\{").replace("}", "\\}")
            out.append("\\begin{verbatim}\n" + code + "\n\\end{verbatim}\n")
            i = j + 1
            continue
        if st.startswith("$$") or st == "$":
            flush_para()
            # normalise a display delimiter that was split across two lone-$ lines
            norm = ["$$" if l.strip() == "$" else l for l in lines[i:]]
            STATS["norm_delims"] += sum(1 for l in lines[i:] if l.strip() == "$")
            buf = [norm[0]]
            closed = norm[0].strip().endswith("$$") and len(norm[0].strip()) > 2
            j = i + 1
            while not closed and j < n:
                cur = norm[j - i]
                buf.append(cur)
                if cur.strip().endswith("$$"):
                    closed = True
                j += 1
            block = "\n".join(buf)
            block = block.replace("$$", "", 1)
            k = block.rfind("$$")
            if k >= 0:
                block = block[:k]
            block, nd = desugar_inline_math(block)
            STATS["desugared"] += nd
            out.append(display_latex(block))
            i = j
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            flush_para()
            out.append(render_heading(min(len(m.group(1)), 4), m.group(2).strip(), prot))
            i += 1
            continue
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", st):
            flush_para()
            out.append("\\vspace{2pt}\\noindent\\rule{\\textwidth}{0.4pt}\\vspace{2pt}")
            out.append("")
            i += 1
            continue
        if st.startswith("|") and st.endswith("|"):
            flush_para()
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i]); i += 1
            out.append(render_table(rows, prot))
            out.append("")
            continue
        if st.startswith("> "):
            flush_para()
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append("\\begin{quote}\n" + conv_text(" ".join(buf), prot) + "\n\\end{quote}\n")
            continue
        if re.match(r"^\s*[-*]\s+", ln):
            flush_para()
            out.append("\\begin{itemize}")
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[i])
                out.append("\\item " + conv_text(item, prot))
                i += 1
            out.append("\\end{itemize}\n")
            continue
        if st == "":
            flush_para()
            i += 1
            continue
        para.append(ln)
        i += 1
    flush_para()
    return "\n".join(out)

# ---------------------------------------------------------------- document assembly

PREAMBLE = r"""\documentclass[11pt,openany]{book}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage[margin=1in,headheight=17pt,headsep=14pt]{geometry}
\usepackage{booktabs,longtable,array}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=NavyBlue,citecolor=NavyBlue,urlcolor=Mahogany]{hyperref}
\makeatletter
\@ifundefined{IfFontExistsTF}{\newcommand{\IfFontExistsTF}[3]{#3}}{}
\makeatother
\IfFontExistsTF{TeX Gyre Pagella}{\setmainfont{TeX Gyre Pagella}}{%
  \IfFontExistsTF{texgyrepagella-regular.otf}{\setmainfont{texgyrepagella-regular.otf}}{}}
\IfFontExistsTF{TeX Gyre Heros}{\setsansfont{TeX Gyre Heros}}{}
\IfFontExistsTF{Latin Modern Mono}{\setmonofont{Latin Modern Mono}[Scale=0.92]}{%
  \IfFontExistsTF{lmmono10-regular.otf}{\setmonofont{lmmono10-regular.otf}[Scale=0.92]}{}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\thepage}
\fancyhead[RO]{\small\thepage}
\fancyhead[RE]{\nouppercase{\small\leftmark}}
\fancyhead[LO]{\nouppercase{\small\rightmark}}
\renewcommand{\headrulewidth}{0.4pt}
\setlength{\parskip}{2pt plus 1pt}
\renewcommand{\arraystretch}{1.08}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}}
\titleformat{\chapter}[hang]{\normalfont\Large\bfseries}{\thechapter}{1em}{}
\titleformat{\section}{\normalfont\large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries}{\thesubsection}{1em}{}
\titlespacing{\subsection}{0pt}{8pt plus 2pt minus 1pt}{3pt}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{3}
\allowdisplaybreaks
\emergencystretch=3em
\hbadness=10000
\vbadness=10000
\hfuzz=2pt
\begin{document}
"""

def title_page(stats, date):
    return rf"""
\begin{{titlepage}}
\centering
\vspace*{{2.2cm}}
{{\Huge\bfseries The Qubitick Corpus\par}}
\vspace{{0.5cm}}
{{\LARGE The Four-Era Canon\par}}
\vspace{{0.9cm}}
{{\large Qubit\_era $\longrightarrow$ Bosonic\_era $\longrightarrow$ Fermion\_era $\longrightarrow$ Baryomesonic\_era\par}}
\vspace{{1.4cm}}
\begin{{tabular}}{{rl}}
\toprule
axioms & A1--A9 \\
conventions & C1--C12 \\
definitions & D0.1--D4.3, Def-H.1--Def-H.43, Def-BM.1--Def-BM.2 \\
tagged results & {stats['thms']} \\
computed cells & {stats['cells']} (Census) \\
free dimensionful scales & $1$ ($\mathfrak h$, P1) \\
\bottomrule
\end{{tabular}}
\vfill
{{\large Edition of {date}\par}}
\vspace{{0.2cm}}
{{\normalsize Machine-verified: \texttt{{checks/run\_all.py}} --- exact arithmetic, no floating point.\par}}
\vspace{{0.3cm}}
{{\small This volume is generated from the canon files by \texttt{{render\_paper.py}}; the mathematics is transplanted unmodified.\par}}
\end{{titlepage}}
"""

def build_tex(files, date):
    texts = {}
    for fn in files:
        path = os.path.join(HERE, fn)
        texts[fn] = open(path, encoding="utf-8").read()
    stats = {"thms": sum(len(re.findall(r"(?m)^### ", t)) for t in texts.values()),
             "cells": len(re.findall(r"(?m)^### FT\.", texts.get("Census.md", "")))}
    doc = [PREAMBLE, title_page(stats, date), "\\frontmatter", "\\tableofcontents"]
    body_started = False
    use_parts = any(f.startswith("Part") for f in files)
    for fn in files:
        src = texts[fn]
        body = re.sub(r"(?m)^# .*$", "", src, count=1)
        prot = Protector()
        conv = convert_md(body, prot)
        if fn == "README.md":
            t = CANON_TITLES[fn]
            doc.append("\\chapter*{\\texorpdfstring{" + t + "}{" + pdf_safe(t) + "}}")
            doc.append("\\addcontentsline{toc}{chapter}{" + pdf_safe(t) + "}")
        else:
            if not body_started:
                doc.append("\\mainmatter")
                if use_parts:
                    doc.append("\\part{The Era Canon}")
                body_started = True
            if fn == "Census.md" and use_parts:
                doc.append("\\part{Annexes}")
            t = CANON_TITLES[fn]
            doc.append("\\chapter{\\texorpdfstring{" + t + "}{" + pdf_safe(t) + "}}")
        doc.append(conv)
    doc.append("\\end{document}")
    return "\n".join(doc)

# ---------------------------------------------------------------- build hygiene
AUX_SUFFIXES = (".aux", ".toc", ".out", ".lof", ".lot", ".xdv")


def aux_is_corrupt(path):
    """True when an auxiliary file looks truncated or unbalanced.

    An interrupted engine run leaves a partial .aux; LaTeX then dies on the
    *next* build while reading it at \\begin{document}, with a message that
    points at the preamble and not at the real cause.  Two cheap tests catch it:
    the file must end on a line boundary, and its braces must balance.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            txt = f.read()
    except OSError:
        return False
    if not txt:
        return False                      # an empty aux is fine, LaTeX rebuilds it
    if not txt.endswith("\n"):
        return True                       # cut off mid-line
    depth = 0
    i = 0
    while i < len(txt):
        c = txt[i]
        if c == "\\":
            i += 2                        # skip an escaped character (\{ \} \\)
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0:
                return True
        i += 1
    return depth != 0


def clean_aux(outdir, base, force=False, quiet=False):
    """Remove corrupt (or, with force, all) auxiliary files for this build."""
    removed = []
    for suf in AUX_SUFFIXES:
        p = os.path.join(outdir, base + suf)
        if not os.path.exists(p):
            continue
        if force or suf == ".xdv" or aux_is_corrupt(p):
            try:
                os.remove(p)
                removed.append(base + suf)
            except OSError:
                pass
    if removed and not quiet:
        why = "removed as requested" if force else "truncated by an earlier interrupted build"
        print("  build hygiene: %s stale aux file(s) %s: %s"
              % (len(removed), why, ", ".join(removed)))
    return removed


AUX_POISON_MARKERS = ("\\@newl@bel", "Runaway argument", "File ended while scanning")


def log_shows_aux_poison(log_path):
    """True when the log shows the truncated-.aux failure signature."""
    if not log_path or not os.path.exists(log_path):
        return False
    try:
        with open(log_path, "r", encoding="utf-8", errors="replace") as f:
            head = f.read(200000)
    except OSError:
        return False
    return sum(1 for m in AUX_POISON_MARKERS if m in head) >= 2


# ---------------------------------------------------------------- pre-flight
HEAD_LINE_RE = re.compile(r"\\(?:chapter|section|subsection)\*?\{(?:\\texorpdfstring\{)?([^{}]*)")
# a row break immediately followed by a bracket that is not a length
ROWBREAK_BRACKET = re.compile(r"\\\\\[(?!\s*-?[\d.]+\s*(?:pt|mm|cm|bp|in|ex|em)\s*\])")
# array-syntax defect classes (HistLog §0.4(e)): an inflated row-end backslash
# run (>=4 adjacent) scatters empty rows; an even run before 'hline' swallows the
# command into literal text; a \hline not directly after a row end, another
# \hline, a table preamble or an endhead-family token is the fatal '! Misplaced
# \noalign'.  check_format.py rejects all three at the source.
BEGIN_ENV_RE = re.compile(r"\\begin\{(array|tabular|longtable)\}(\{[^{}]*\})?\s*$")
ENDHEAD_RE = re.compile(r"\\end(head|firsthead|foot|lastfoot)\s*$")


def preflight(tex):
    """scan the generated LaTeX for constructs that halt XeTeX and report each
    with the nearest preceding heading, so the fault is findable in the canon."""
    lines = tex.split("\n")
    problems, ctx, depth = [], "(preamble)", 0
    n_open = n_close = 0
    for i, raw in enumerate(lines, 1):
        t = raw.strip()
        m = HEAD_LINE_RE.search(t)
        if m and m.group(1).strip():
            ctx = m.group(1).strip()[:70]
        if t == "\\[":
            depth += 1; n_open += 1; continue
        if t == "\\]":
            depth = max(0, depth - 1); n_close += 1; continue
        if depth:
            spans = _text_arg_spans(raw)
            if any(ch == "$" and not _escaped(raw, j)
                   and not any(a <= j < b for a, b in spans)
                   for j, ch in enumerate(raw)):
                problems.append((i, ctx, raw.strip()[:110]))
            elif "$$" in re.sub(r"\\\$", "", raw):
                problems.append((i, ctx, "$$ inside a display: " + raw.strip()[:80]))
            m2 = ROWBREAK_BRACKET.search(raw)
            if m2:
                problems.append((i, ctx, "a row break \\\\[...] that LaTeX reads as a "
                                 "length: " + raw.strip()[max(0, m2.start() - 24):m2.start() + 34]))
    if n_open != n_close:
        problems.append((0, "(document)",
                         "\\[ and \\] do not balance: %d against %d" % (n_open, n_close)))

    # ---- the array-syntax classes: full-text scans with heading context ----
    heads = []
    for i, raw in enumerate(lines, 1):
        m = HEAD_LINE_RE.search(raw.strip())
        if m and m.group(1).strip():
            heads.append((i, m.group(1).strip()[:70]))

    def ctx_of(pos):
        ln = tex.count("\n", 0, pos) + 1
        c = "(preamble)"
        for hln, hctx in heads:
            if hln <= ln:
                c = hctx
            else:
                break
        return ln, c

    for m in re.finditer(r"\\{4,}", tex):
        ln, c = ctx_of(m.start())
        problems.append((ln, c, "an inflated row-end backslash run (%d adjacent): "
                         "extra empty table rows" % len(m.group(0))))
    for m in re.finditer(r"hline", tex):
        j, k = m.start() - 1, 0
        while j >= 0 and tex[j] == "\\":
            k += 1; j -= 1
        if k > 0 and k % 2 == 0:
            ln, c = ctx_of(m.start())
            problems.append((ln, c, "a swallowed \\hline (even backslash run): "
                             "'hline' typesets as literal text"))
        elif k == 1:
            pre = tex[:j + 1].rstrip()
            m2 = re.search(r"\\+$", pre)
            if (m2 and len(m2.group(0)) >= 2 and len(m2.group(0)) % 2 == 0) \
                    or pre.endswith("hline") or BEGIN_ENV_RE.search(pre) \
                    or ENDHEAD_RE.search(pre):
                continue
            ln, c = ctx_of(m.start())
            problems.append((ln, c, "a misplaced \\hline: XeTeX halts with "
                             "'! Misplaced \\noalign'"))
    return problems


def report_preflight(problems, tex_path):
    print()
    print("!" * 78)
    print("pre-flight FAILED: the generated LaTeX cannot compile (%d problem(s))" % len(problems))
    for ln, ctx, ex in problems[:12]:
        print("  %s:%d   [%s]" % (os.path.basename(tex_path), ln, ctx))
        print("      %s" % ex)
    if len(problems) > 12:
        print("  ... and %d more" % (len(problems) - 12))
    print()
    print("  A bare $ inside a \\[...\\] display ends the display early and halts the")
    print("  engine. In the canon that is an inline $...$ written inside a $$...$$")
    print("  block, or a $$ delimiter split across two lines that each hold one $.")
    print("  An inflated backslash run, a swallowed \\hline or a misplaced \\hline")
    print("  breaks the generated tables (the last one fatally, with '! Misplaced")
    print("  \\noalign'); in the canon all three are array-syntax defects that")
    print("  check_format.py rejects at the source.")
    print("!" * 78)

# ---------------------------------------------------------------- engines

TECTONIC_URL = ("https://github.com/tectonic-typesetting/tectonic/releases/"
                "download/tectonic%400.17.0/tectonic-0.17.0-x86_64-unknown-linux-musl.tar.gz")

def find_engine(pref):
    if pref and pref != "auto":
        p = shutil.which(pref)
        return [p] if p else None
    for cand in (shutil.which("tectonic"),
                 os.environ.get("TECTONIC"),
                 os.path.normpath(os.path.join(HERE, "..", "tools", "tectonic")),
                 os.path.normpath(os.path.join(HERE, "..", "..", "tools", "tectonic")),
                 os.path.expanduser("~/tools/tectonic"),
                 "/tmp/tk/tectonic"):
        if cand and os.path.exists(cand) and os.access(cand, os.X_OK):
            return [cand]
    for cand in ("xelatex", "lualatex", "pdflatex"):
        p = shutil.which(cand)
        if p:
            return [p]
    return None

def fetch_engine():
    dst = os.path.normpath(os.path.join(HERE, "..", "..", "tools"))
    if not os.path.isdir(os.path.dirname(dst)):
        dst = os.path.join(HERE, "tools")
    os.makedirs(dst, exist_ok=True)
    print("fetching tectonic ...")
    data = urllib.request.urlopen(TECTONIC_URL, timeout=300).read()
    with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as f:
        f.write(data); tmp = f.name
    with tarfile.open(tmp) as t:
        t.extractall(dst)
    os.remove(tmp)
    os.chmod(os.path.join(dst, "tectonic"), 0o755)
    print("engine at", os.path.join(dst, "tectonic"))

def compile_once(tex_path, outdir, engine, keep_logs=True):
    base = os.path.splitext(os.path.basename(tex_path))[0]
    name = os.path.basename(engine[0])
    if name == "tectonic":
        cmd = engine + (["--keep-logs"] if keep_logs else []) + ["--outdir", outdir, tex_path]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-4000:]); print(r.stderr[-2000:])
        log = None
        for cand in (os.path.join(outdir, base + ".log"), os.path.join(os.getcwd(), base + ".log")):
            if os.path.exists(cand):
                log = cand
        return r.returncode == 0, log
    cwd = os.getcwd()
    os.chdir(outdir)
    try:
        ok = True
        for k in range(3):
            cmd = engine + ["-interaction=nonstopmode", tex_path]
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode != 0:
                ok = False
                break          # later passes cannot fix a fatal error
        log = os.path.join(outdir, base + ".log")
        if not ok:
            report_latex_errors(log if os.path.exists(log) else None)
            if r.stderr.strip():
                print("--- engine stderr (tail) ---")
                print(r.stderr[-2000:])
        return ok, (log if os.path.exists(log) else None)
    finally:
        os.chdir(cwd)


def report_latex_errors(log_path, blocks=6):
    """Print the first fatal errors from a failed engine run's log, so a
    'compile failed' is diagnosable at the terminal instead of buried."""
    if not log_path:
        print("no log file was produced — the engine did not start "
              "(binary present but not runnable, or a missing format)")
        return
    try:
        lines = open(log_path, encoding="utf-8", errors="replace").read().splitlines()
    except OSError as e:
        print(f"cannot read {log_path}: {e}")
        return
    print(f"--- first errors from {log_path} ---")
    idxs = [i for i, l in enumerate(lines) if l.startswith("! ")][:blocks]
    if not idxs:
        idxs = [max(0, i - 2) for i, l in enumerate(lines)
                if ("Emergency stop" in l or "Fatal error" in l)][:1]
    for i in idxs:
        for l in lines[i:i + 8]:
            print("   ", l)
        print()
    if not idxs:
        print("    (no '! ' error lines found — inspect the log directly)")

# ---------------------------------------------------------------- overfull repair

OVER_DISPLAY = re.compile(r"Overfull \\hbox \((\d+(?:\.\d+)?)pt too wide\) detected at line (\d+)")
OVER_PARA = re.compile(r"Overfull \\hbox \((\d+(?:\.\d+)?)pt too wide\) in paragraph at lines (\d+)--(\d+)")
OVER_ALIGN = re.compile(r"Overfull \\hbox \((\d+(?:\.\d+)?)pt too wide\) in alignment at lines (\d+)--(\d+)")
THRESHOLD = 8.0

def parse_overfull(log_path):
    txt = open(log_path, encoding="utf-8", errors="replace").read()
    # TeX log wraps at 79 chars: rejoin wrapped lines before matching
    txt = re.sub(r"\n(?=[^\n])", "", txt) if False else txt
    disp, para, align = [], [], []
    for m in OVER_DISPLAY.finditer(txt):
        if float(m.group(1)) > THRESHOLD:
            disp.append((float(m.group(1)), int(m.group(2))))
    for m in OVER_PARA.finditer(txt):
        if float(m.group(1)) > THRESHOLD:
            para.append((float(m.group(1)), int(m.group(2)), int(m.group(3))))
    for m in OVER_ALIGN.finditer(txt):
        if float(m.group(1)) > THRESHOLD:
            align.append((float(m.group(1)), int(m.group(2)), int(m.group(3))))
    return disp, para, align

DSP_MARKER = "%dsp-level:"
PARA_MARKER = "%para-level:"
WRAP_OPEN = {"{\\small", "{\\footnotesize", "{\\scriptsize", "\\resizebox"}

def _find_display(lines, ln0):
    """Given a 0-based log line, locate the enclosing \\[ ... \\] block."""
    i = min(ln0, len(lines) - 1)
    if lines[i].strip() == "\\]":
        c = i
        o = c - 1
        while o >= 0 and lines[o].strip() != "\\[":
            if lines[o].strip() == "\\]":
                return None
            o -= 1
        return (o, c) if o >= 0 else None
    o = i
    while o >= 0 and lines[o].strip() != "\\[":
        if lines[o].strip() == "\\]":
            return None
        o -= 1
    if o < 0:
        return None
    c = o + 1
    while c < len(lines) and lines[c].strip() != "\\]":
        c += 1
    return (o, c) if c < len(lines) else None


RESIZE_OPEN = "\\resizebox{\\textwidth}{!}{$\\displaystyle"
RESIZE_CLOSE = "$}"

def _marker_above(lines, o):
    """Find the dsp marker + any wrapper-open lines above the \\[ line o."""
    k = o - 1
    wraps = []
    while k >= 0 and k >= o - 3:
        st = lines[k].strip()
        if st.startswith(DSP_MARKER):
            return k, int(st[len(DSP_MARKER):]), wraps
        if any(st.startswith(w) for w in WRAP_OPEN):
            wraps.append(k)
            k -= 1
            continue
        break
    return None, 0, wraps

def apply_fixes(tex_path, disp, para, align):
    with open(tex_path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    nfix = 0

    # ---------- collect target regions ----------
    dsp_regions = {}
    for width, ln in disp:
        blk = _find_display(lines, ln - 1)
        if not blk:
            continue
        dsp_regions[blk] = max(dsp_regions.get(blk, 0), width)

    tbl_markers = set()
    for width, a, b in align:
        i = min(a - 1, len(lines) - 1)
        o = i
        while o >= 0 and not lines[o].strip().startswith(TABLE_MARKER):
            if lines[o].strip().startswith("\\begin{longtable}"):
                o = -2
                break
            o -= 1
        if o >= 0:
            tbl_markers.add(o)

    fixed_spans = sorted(dsp_regions.keys())

    # table/verbatim regions: never wrap or promote inside them; table-cell
    # overfulls escalate the enclosing table's font ladder instead
    blocked = [False] * len(lines)
    blk_marker = [None] * len(lines)
    stack = None
    marker = None
    for i, l in enumerate(lines):
        st = l.strip()
        if st.startswith(TABLE_MARKER):
            marker = i
        elif st.startswith("\\begin{longtable}") or st.startswith("\\begin{verbatim}"):
            stack = i
        elif st.startswith("\\end{longtable}") or st.startswith("\\end{verbatim}"):
            if stack is not None:
                for k in range(stack, i + 1):
                    blocked[k] = True
                    blk_marker[k] = marker
                stack = None
                marker = None

    def is_struct(i):
        st = lines[i].strip()
        return (st in ("\\[", "\\]", "}", "$}")
                or st.startswith(DSP_MARKER) or st.startswith(TABLE_MARKER)
                or st.startswith(PARA_MARKER)
                or any(st.startswith(w) for w in WRAP_OPEN)
                or st.startswith("\\begin{longtable}") or st.startswith("\\end{longtable}")
                or st.startswith("\\begin{verbatim}") or st.startswith("\\end{verbatim}")
                or st.startswith("\\begin{") or st.startswith("\\end{")
                or st.startswith("\\item"))

    para_regions = {}
    for width, a, b in para:
        a0, b0 = a - 1, min(b - 1, len(lines) - 1)
        # clamp: wrappers must never land inside a display/table block
        while a0 < b0 and is_struct(a0):
            a0 += 1
        while b0 > a0 and is_struct(b0):
            b0 -= 1
        if a0 > b0 or is_struct(a0) or is_struct(b0):
            continue
        if any(blocked[a0:b0 + 1]):
            # inside a longtable/verbatim: the table font ladder owns it
            mi = next((blk_marker[k] for k in range(a0, b0 + 1)
                       if blk_marker[k] is not None), None)
            if mi is not None:
                tbl_markers.add(mi)
            continue
        if any(not (b0 < o or a0 > c) for (o, c) in fixed_spans):
            continue           # overlaps a display fix: skip this round
        para_regions[(a0, b0)] = max(para_regions.get((a0, b0), 0), width)

    # ---------- apply bottom-up ----------
    ops = []   # (sort_pos, callable(lines))
    for (o, c), width in dsp_regions.items():
        ops.append((o, ("dsp", o, c, width)))
    for o in tbl_markers:
        ops.append((o, ("tbl", o)))
    for (a, b), width in para_regions.items():
        ops.append((a, ("para", a, b, width)))
    ops.sort(key=lambda t: -t[0])

    for _, op in ops:
        kind = op[0]
        if kind == "dsp":
            _, o, c, width = op
            mo, cur, wraps = _marker_above(lines, o)
            if cur >= 4:
                continue                      # already resizeboxed: nothing left
            # remove any existing outer wrapper
            if wraps:
                for k in sorted(wraps, reverse=True):
                    del lines[k]
                o -= len(wraps); c -= len(wraps)
                for j in range(c + 1, min(c + 4, len(lines))):
                    if lines[j].strip() in ("}", "$}"):
                        del lines[j]
                        break
            # split-first: intelligent line breaks before any font reduction.
            # Each round deepens the separator stage (\qquad -> \quad ->
            # top-level ; , relations); a split consumes its separators, so
            # the rounds strictly progress and terminate in the font ladder.
            if cur == 0:
                body = "\n".join(lines[o + 1:c])
                frags = []
                for stg in (1, 2, 3):
                    frags = _split_display(body, stg)
                    if frags:
                        break
                if frags:
                    repl = []
                    for fg in frags:
                        repl += [DSP_MARKER + "0", "\\[", fg, "\\]", ""]
                    lines[o:c + 1] = repl[:-1]
                    if mo is not None and mo < o:
                        lines[mo] = DSP_MARKER + "0"
                    nfix += 1
                    continue
            nxt = cur + 1 if cur else (1 if width < 25 else 2 if width < 120 else 3)
            if nxt <= 3:
                lines.insert(c + 1, "}")
                lines.insert(o, ["", "{\\small", "{\\footnotesize", "{\\scriptsize"][nxt])
                if mo is None:
                    lines.insert(o, DSP_MARKER + str(nxt))
                else:
                    lines[mo] = DSP_MARKER + str(nxt)
                nfix += 1
            else:
                lines.insert(c, RESIZE_CLOSE)
                lines.insert(o + 1, RESIZE_OPEN)
                if mo is None:
                    lines.insert(o, DSP_MARKER + "4")
                else:
                    lines[mo] = DSP_MARKER + "4"
                nfix += 1
        elif kind == "tbl":
            _, o = op
            cur = int(lines[o].strip()[len(TABLE_MARKER):])
            if cur < 3:
                lines[o] = TABLE_MARKER + str(cur + 1)
                newsize = ["\\small", "\\footnotesize", "\\scriptsize"][cur]
                # NOTE: the replacement is passed as a function — a size command
                # such as "\small" is a bad escape (\s) inside a re.sub template.
                lines[o + 1] = re.sub(r"^\{(?:\\small|\\footnotesize|\\scriptsize)?",
                                      lambda _m, _s="{" + newsize: _s, lines[o + 1])
                nfix += 1
            else:
                # last rung: tighten the column separation (math-heavy cells are
                # already breakable via _math_allowbreak at emission time)
                if "\\setlength{\\tabcolsep}{4pt}" in lines[o + 1]:
                    lines[o + 1] = lines[o + 1].replace(
                        "\\setlength{\\tabcolsep}{4pt}",
                        "\\setlength{\\tabcolsep}{2pt}\\setlength{\\LTleft}{0pt}"
                        "\\setlength{\\LTright}{0pt}")
                    lines[o] = TABLE_MARKER + "4"
                    nfix += 1
        else:
            _, a, b, width = op
            mk = None
            for k in range(a - 1, max(a - 5, -1), -1):
                st = lines[k].strip()
                if st.startswith(PARA_MARKER):
                    mk = k; break
                if st == "" or st.startswith("\\begin{sloppypar}"):
                    continue
                break
            already = mk is not None
            lvl = int(lines[mk].strip()[len(PARA_MARKER):]) if already else 0
            if lvl >= 3:
                # last resort: promote the longest inline-math span of the
                # paragraph to a display (one span per round)
                best = None
                for li in range(a, b + 1):
                    for m in re.finditer(r"\$[^$\n]+\$", lines[li]):
                        if len(m.group(0)) > 60 and (best is None or len(m.group(0)) > len(best[2])):
                            best = (li, m.start(), m.group(0))
                if best is None:
                    continue
                li, _ix, span = best
                L = lines[li]
                idx = L.find(span)
                inner = span[1:-1]
                lines[li:li + 1] = [L[:idx], "\\[", repair_display(inner).strip(), "\\]",
                                    L[idx + len(span):]]
                nfix += 1
                continue
            lvl_new = lvl + 1
            stretch = {1: "", 2: "\\setlength{\\emergencystretch}{8em}",
                       3: "\\setlength{\\emergencystretch}{16em}"}[lvl_new]
            if already:
                lines[mk] = PARA_MARKER + str(lvl_new)
                for k in range(mk + 1, min(mk + 4, len(lines))):
                    if lines[k].strip().startswith("\\begin{sloppypar}"):
                        lines[k] = "\\begin{sloppypar}" + stretch
                        break
            else:
                lines.insert(b + 1, "")
                lines.insert(b + 1, "\\end{sloppypar}")
                lines.insert(a, "\\begin{sloppypar}" + stretch)
                lines.insert(a, "")
                lines.insert(a, PARA_MARKER + str(lvl_new))
            nfix += 1

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return nfix

# ---------------------------------------------------------------- compile loop

def compile_and_repair(tex_path, outdir, engine, rounds=8, force_clean=False):
    """Compile; parse overfull boxes; repair; recompile. True on success."""
    base = os.path.splitext(os.path.basename(tex_path))[0]
    clean_aux(outdir, base, force=force_clean)
    for rnd in range(1, rounds + 1):
        ok, log = compile_once(tex_path, outdir, engine)
        if not ok:
            if log_shows_aux_poison(log):
                print("\n  diagnosis: the engine died reading a TRUNCATED .aux left by an")
                print("  earlier interrupted build, not on anything in the .tex. The stale")
                print("  auxiliary files have been removed - simply re-run this command.")
                clean_aux(outdir, base, force=True, quiet=True)
            else:
                # a genuine failure can itself leave a truncated .aux behind,
                # which would poison the next run: clear it now
                clean_aux(outdir, base, force=True, quiet=True)
            print("compile failed; the .tex is kept for local compilation")
            print("hints: missing LaTeX packages or fonts are the usual cause "
                  "(see the errors above).")
            print("       self-contained engine:  python3 render_paper.py --fetch-engine "
                  "&& python3 render_paper.py")
            print("       or install the packages named in the errors "
                  "(TeX Live: tlmgr / scheme-full; NixOS: texlive in the profile "
                  "with the needed packages, and fontspec needs Latin Modern).")
            return False
        if not log:
            print(f"PDF written (no log to scan; round {rnd})")
            return True
        disp, para, align = parse_overfull(log)
        print(f"round {rnd}: overfull >{THRESHOLD:.0f}pt — displays {len(disp)}, "
              f"paragraphs {len(para)}, tables {len(align)}")
        if not disp and not para and not align:
            return True
        if rnd == rounds:
            print("repair budget exhausted; remaining overfulls left as-is")
            return True
        n = apply_fixes(tex_path, disp, para, align)
        if n == 0:
            print("no further fixes applicable; stopping repair loop")
            return True
    return True

# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Render the four-era canon as a formal LaTeX paper.")
    ap.add_argument("--engine", default="auto",
                    help="auto | tectonic | xelatex | lualatex | pdflatex")
    ap.add_argument("--include-histlog", action="store_true",
                    help="also render the HistLog annex (default: canon + census only)")
    ap.add_argument("--no-preface", action="store_true", help="exclude the README preface")
    ap.add_argument("--outdir", default=os.path.join(HERE, "paper"))
    ap.add_argument("--fetch-engine", action="store_true",
                    help="download a self-contained tectonic binary and exit")
    ap.add_argument("--tex-only", action="store_true", help="write the .tex, do not compile")
    ap.add_argument("--max-repair-rounds", type=int, default=8)
    ap.add_argument("--clean", action="store_true",
                    help="delete the auxiliary files (.aux/.toc/.out/.xdv) before "
                         "compiling; use after an interrupted build")
    ap.add_argument("--wide", action="store_true",
                    help="reading build: landscape 11x8.5in page with 0.7in margins "
                         "(~9.6in text block), display-breaking threshold raised from "
                         "80 to 118 visible chars and the table font caps rescaled, so "
                         "far fewer displays are split. Writes *_wide.tex/.pdf.")
    args = ap.parse_args()

    if args.fetch_engine:
        fetch_engine()
        return 0

    if args.wide:
        global DSP_WIDTH, SIZE_STEPS
        DSP_WIDTH = 118
        SIZE_STEPS = [("", 135), ("\\small", 165), ("\\footnotesize", 194),
                      ("\\scriptsize", 232)]

    files = ([] if args.no_preface else ["README.md"]) + CANON + ["Census.md"]
    if args.include_histlog:
        files.append("HistLog.md")
    missing = [f for f in files if not os.path.exists(os.path.join(HERE, f))]
    if missing:
        print("missing canon files:", missing); return 2

    os.makedirs(args.outdir, exist_ok=True)
    date = datetime.date.today().isoformat()
    tex = build_tex(files, date)
    if args.wide:
        tex = tex.replace(
            "\\usepackage[margin=1in,headheight=15pt]{geometry}",
            "\\usepackage[paperwidth=11in,paperheight=8.5in,margin=0.7in,"
            "headheight=15pt]{geometry}\n\\linespread{1.04}")
    stem = "qubitick_corpus_wide" if args.wide else "qubitick_corpus"
    tex_path = os.path.join(args.outdir, stem + ".tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex)
    print(f"LaTeX written: {tex_path} ({len(tex.splitlines())} lines)")
    if STATS["desugared"] or STATS["norm_delims"]:
        print("  display hygiene: removed %d spurious inline-$ delimiter(s) inside "
              "displays, normalised %d split $$ delimiter(s)"
              % (STATS["desugared"], STATS["norm_delims"]))
    problems = preflight(tex)
    if problems:
        report_preflight(problems, tex_path)
        return 4
    print("  pre-flight: no bare $ inside a display, \\[ and \\] balance, "
          "no array-row defects - the .tex is compilable")
    if args.tex_only:
        return 0

    engine = find_engine(args.engine)
    if not engine:
        print("no LaTeX engine found. Install one (tectonic: `--fetch-engine`) "
              "or compile the .tex locally:  tectonic " + os.path.basename(tex_path))
        return 3
    print("engine:", engine[0])

    if not compile_and_repair(tex_path, args.outdir, engine, args.max_repair_rounds,
                              force_clean=args.clean):
        return 1

    pdf = os.path.join(args.outdir, stem + ".pdf")
    if os.path.exists(pdf):
        print(f"PDF written: {pdf} ({os.path.getsize(pdf)/1e6:.1f} MB)")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())
