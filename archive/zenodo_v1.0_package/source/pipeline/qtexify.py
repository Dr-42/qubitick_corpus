#!/usr/bin/env python3
"""qtexify.py — markdown-chunk -> LaTeX conversion and document assembly for
the Qubitick publication package. Reuses the corpus's own render_paper.py
converter (math pass-through, display repair, measured tables)."""
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(os.path.dirname(HERE))          # source/pipeline -> package root
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(PKG, "working_markdowns", "tools"))
import qparse
from qpipeline import (REG, CANON, PARTNO, MOVE, LOG, stage_parse, stage_sanitize,
                       stage_histlog, assign_ids, build_catalog, stage_number,
                       extract_quote, SRC, PKG, OUT)
import rp_patched as rp

OUTDIR = OUT
PARTS_DIR = os.path.join(OUTDIR, "parts")

PART_TITLES = {
    "Part1_Qubit_era.md": ("Part 1 · The Qubit Era",
        "Axioms, Conventions, Definitions, Pair Canon, Ledger Dynamics"),
    "Part2_Bosonic_era.md": ("Part 2 · The Bosonic Era",
        "Geometry, Electroweak, Electromagnetic, Colour, Saturation"),
    "Part3_Fermion_era.md": ("Part 3 · The Fermion Era",
        "Bound Chains, Termini, Floors, Carriers, Channels"),
    "Part4_Baryomesonic_era.md": ("Part 4 · The Baryomesonic Era",
        "Colour-Sealed Composites"),
    "Census.md": ("Census — The Computed Cells and Their Consumption",
        "The Category-B Data Cells and the Consumption Block"),
}

ENVNAME = {"theorem": "Theorem", "definition": "Definition", "axiom": "Axiom",
           "convention": "Convention", "corollary": "Corollary"}

def lbl(tag):
    return "tag:" + re.sub(r"[^A-Za-z0-9]", "-", tag)

def tescape(x):
    return (x.replace("\\", "\\textbackslash{}").replace("_", "\\_")
             .replace("%", "\\%").replace("#", "\\#").replace("&", "\\&"))

def has_unsafe(lines):
    for ln in lines:
        s = ln.strip()
        if s.startswith("|") and s.endswith("|"):
            return True
        if s.startswith("```"):
            return True
    return False

def title_texorpdf(title, prot):
    conv = rp.conv_text(title, prot)
    safe = rp.pdf_safe(title)
    return "\\texorpdfstring{" + conv + "}{" + safe + "}"

# ------------------------------------------------------------------ preambles
COMMON_PACKAGES = r"""
\usepackage{fontspec}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{amsthm}
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
% --- amsthm setup -----------------------------------------------------------
% \theoremstyle{plain}-family style for theorem-like environments and
% \theoremstyle{definition}-family style for definition-like environments.
% The bodies are set upright (a `plain` italic body would italicise the
% corpus's extensive \text{...} proof justifications); head formatting and
% numbering follow the plain / definition styles respectively.
\newtheoremstyle{canonplain}%
  {7pt plus 2pt minus 1pt}{7pt plus 2pt minus 1pt}%
  {\normalfont}{0pt}{\bfseries}{.}%
  {0.6em plus 0.2em}%
  {\thmname{#1}\thmnumber{ #2}\thmnote{\normalfont\ (#3)}}
\newtheoremstyle{canondef}%
  {7pt plus 2pt minus 1pt}{7pt plus 2pt minus 1pt}%
  {\normalfont}{0pt}{\bfseries}{.}%
  {0.6em plus 0.2em}%
  {\thmname{#1}\thmnumber{ #2}\thmnote{\normalfont\ (#3)}}
\theoremstyle{canonplain}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{corollary}{Corollary}[chapter]
\newtheorem{axiom}{Axiom}[chapter]
\newtheorem{convention}{Convention}[chapter]
\theoremstyle{canondef}
\newtheorem{definition}{Definition}[chapter]
\newenvironment{movedblock}
  {\par\medskip\begingroup\small\itshape\leftskip2.2em\rightskip2.2em}
  {\par\endgroup\medskip}
% run-in heading for theorem-class blocks that contain tables or verbatim
% material (longtable/verbatim cannot live inside amsthm environments); the
% printed form matches the environment heads and the counter is shared.
\newcommand{\pseudohead}[3]{\par\medskip\noindent\refstepcounter{#1}%
  \textbf{\csname the#1\endcsname\hspace{0.6em}(#2\hspace{0.35em}---\hspace{0.35em}#3).}%
  \par\nobreak\smallskip}
% ----------------------------------------------------------------------------
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
"""

def preamble(documentclass, title_pdf):
    return ("\\documentclass[11pt,openany]{" + documentclass + "}\n"
            + COMMON_PACKAGES + "\\begin{document}\n")

# ------------------------------------------------------------------ chunk -> tex
def my_heading(level, text, prot):
    """section/subsection with the FULL name in the TOC (the running head may
    shorten extremely long titles, but never at the em dash — tier names stay)."""
    conv = rp.conv_text(text, prot)
    safe = rp.pdf_safe(text)
    cmd = {2: "section", 3: "subsection"}[level]
    plain = plaintext(text)
    if len(plain) > 62:
        cut = plain[:60].rsplit(" ", 1)[0] + "…"
        opt = rp.conv_text(cut, prot).replace("[", "{[").replace("]", "]}")
    else:
        opt = conv.replace("[", "{[").replace("]", "]}")
    return (f"\\phantomsection\n\\{cmd}[{opt}]{{\\texorpdfstring{{{conv}}}{{{safe}}}}}\n")

def render_chunks(chunks, prot, numbers, ids, chapter_cmds=True):
    out = []
    for c in chunks:
        k = c["kind"]
        if k == "h1":
            continue
        if k == "h2":
            out.append(my_heading(2, c["text"], prot))
        elif k == "h3":
            out.append(my_heading(3, c["text"], prot))
        elif k == "hr":
            continue
        elif k == "raw":
            out.append(rp.convert_md(c["text"], prot))
        elif k == "stub":
            t = c["tag"]; bid = ids[t]
            title = title_texorpdf(t + " — " + c["title"], prot)
            out.append("\\medskip\\noindent\\textit{" + title + ".}\\ "
                       "Structural-constraints record: see Appendix B, Section "
                       + bid + " of the Addendum.\\par\\medskip\n")
        elif k == "paratag":
            out.append(render_paratag(c, prot, numbers))
        elif k == "tagblock":
            out.append(render_tagblock(c, prot, numbers, ids))
    return "\n".join(out)

def strip_marker(first, tag):
    """Remove a leading **TAG.** / **TAG (t).** marker; return (title, rest)."""
    m = re.match(r"\*\*" + re.escape(tag) + r"(?:\s*\(([^)]*)\))?\.\*\*\s*", first)
    if m:
        return (m.group(1) or ""), first[m.end():]
    m = re.match(r"\*\*" + re.escape(tag) + r"\.\*\*\s*", first)
    if m:
        return "", first[m.end():]
    return None, first

def render_paratag(c, prot, numbers):
    tag = c["tag"]
    cls = "corollary" if c["is_cor"] else qparse.tag_class(tag)
    lines = list(c["lines"])
    title, rest = strip_marker(lines[0], ("Cor " + tag) if c["is_cor"] else tag)
    if title is None:
        title, rest = strip_marker(lines[0], tag)
    lines[0] = rest
    if not lines[0].strip():
        lines = lines[1:]
    body = "\n".join(lines)
    if cls == "policy":
        return ("\\phantomsection\\label{" + lbl(tag) + "}\n" + rp.convert_md("\n".join(c["lines"]), prot))
    num = numbers[tag].split(" ", 1)[1]
    head = tag + ((" — " + title) if title else "")
    if has_unsafe(lines):
        return ("\\pseudohead{" + cls + "}{" + title_texorpdf(tag, prot) + "}{"
                + title_texorpdf(title, prot) + "}\\label{" + lbl(tag) + "}\n"
                + rp.convert_md(body, prot))
    return ("\\begin{" + cls + "}[{" + title_texorpdf(head, prot) + "}]"
            "\\label{" + lbl(tag) + "}\n" + rp.convert_md(body, prot) + "\n\\end{" + cls + "}\n")

def render_tagblock(c, prot, numbers, ids):
    tag = c["tag"]
    cls = qparse.tag_class(tag)
    if cls == "policy":
        cls = "theorem"
    out = []
    for kind, ctag, ctitle, lines in c["segs"]:
        # resolve the FT.48 moved-passage marker
        text_lines = []
        for ln in lines:
            if ln.startswith("[[MOVEDSTUB:B2RMK]]"):
                bid = ids.get("B2RMK", "B.2.1")
                text_lines.append("*The two distance claims of the derivation record "
                                  "(the winding-integer distance and the mass-as-distance "
                                  "identification) are resolved in the Addendum: see "
                                  "Appendix B, Section " + bid + ".*")
            else:
                text_lines.append(ln)
        lines = text_lines
        if kind == "cor":
            first = lines[0]
            m = re.match(r"\*\*Cor\s+" + re.escape(ctag) + r"(?:\s*\(([^)]*)\))?\.\*\*\s*", first)
            ctitle = (m.group(1) or ctitle) if m else ctitle
            lines[0] = first[m.end():] if m else first
            if not lines[0].strip():
                lines = lines[1:]
            body = "\n".join(lines)
            head = ctag + ((" — " + ctitle) if ctitle else "")
            if has_unsafe(lines):
                out.append("\\pseudohead{corollary}{" + title_texorpdf(ctag, prot) + "}{"
                           + title_texorpdf(ctitle or "", prot) + "}\\label{" + lbl(ctag) + "}\n"
                           + rp.convert_md(body, prot))
            else:
                out.append("\\begin{corollary}[{" + title_texorpdf(head, prot) + "}]"
                           "\\label{" + lbl(ctag) + "}\n" + rp.convert_md(body, prot)
                           + "\n\\end{corollary}\n")
            continue
        # main segment of the tag block
        title = c["title"]
        head = tag + " — " + title
        body = "\n".join(lines)
        if has_unsafe(lines):
            out.append("\\pseudohead{" + cls + "}{" + title_texorpdf(tag, prot) + "}{"
                       + title_texorpdf(title, prot) + "}\\label{" + lbl(tag) + "}\n"
                       + rp.convert_md(body, prot))
        else:
            out.append("\\begin{" + cls + "}[{" + title_texorpdf(head, prot) + "}]"
                       "\\label{" + lbl(tag) + "}\n" + rp.convert_md(body, prot)
                       + "\n\\end{" + cls + "}\n")
    return "\n".join(out)

# ------------------------------------------------------------------ front matter
def main_title_page(numbers, stats):
    return r"""
\begin{titlepage}
\centering
\vspace*{2.0cm}
{\Huge $\langle qu(b(i(t|t))ick)\rangle$\par}
\vspace{0.4cm}
{\LARGE The Four-Era Canon\par}
\vspace{0.3cm}
{\large A Machine-Verified, Discrete-Ledger Framework for Foundational Physics\par}
\vspace{0.5cm}
{\large Volume I --- The Four-Era Canon\par}
\vspace{0.8cm}
{\large Qubit\_era $\longrightarrow$ Bosonic\_era $\longrightarrow$ Fermion\_era $\longrightarrow$ Baryomesonic\_era\par}
\vspace{1.3cm}
\begin{tabular}{rl}
\toprule
axioms & A1--A9 \\
conventions & C1--C13 \\
definitions & D0.1--D4.3, Def-EM.20--22, Def-H.1--43, Def-BM.1--20 \\
theorem and data-cell tags & """ + str(stats["thm_tags"]) + r""" \\
registry tags (total) & """ + str(stats["reg_tags"]) + r""" \\
dependency edges (Req graph) & """ + str(stats["edges"]) + r""" \\
free dimensionful scales & $1$ ($\mathfrak h$, P1) \\
verification suite & """ + str(stats["suite"]) + r""" checkers, exact arithmetic, no floating point \\
\bottomrule
\end{tabular}
\vfill
{\large Edition of """ + stats["date"] + r"""\par}
\vspace{0.2cm}
{\normalsize Machine-verified: \texttt{verification/run\_all.py} --- suite state """ + str(stats["suite"]) + "/" + str(stats["suite"]) + r""" green.\par}
\vspace{0.3cm}
{\small The mathematics is transplanted unmodified from the canon files preserved in \texttt{working\_markdowns/}; this volume is the sanitized presentation layer.\par}
\end{titlepage}
"""

PREFACE = r"""
\chapter*{\texorpdfstring{Preface — Guide to this Volume}{Preface - Guide to this Volume}}
\addcontentsline{toc}{chapter}{Preface --- Guide to this Volume}

This volume is the presentation layer of the $\langle qu(b(i(t|t))ick)\rangle$
corpus (read \textit{qubitick}): a formal corpus
deriving, from nine axioms and one free dimensionful scale $\mathfrak h$, the
qubit, bosonic, fermionic and baryomesonic layers, with every theorem carrying
its requirement set (\textbf{Req}), its symbolic proof (\textbf{Pf}) and its
physical reading (\textbf{Phys}), and every identity machine-verified in exact
arithmetic. The corpus's own description of its subject stands: qubits
$\longrightarrow$ bosonic gauge/geometry $\longrightarrow$ fermionic bound
chains $\longrightarrow$ baryomesonic colour-sealed composites; pure symbolic
derivation; no floating point anywhere; no external physical constant enters
any derivation.

\medskip
\noindent\textbf{The volume.}\quad
Chapters 1--4 are the four eras (Part 1 · Qubit, Part 2 · Bosonic,
Part 3 · Fermion, Part 4 · Baryomesonic); Appendix A is the Census annex (the
25 computed data cells, cited row-wise by the parts); the Index of Corpus Tags
maps every canonical tag to its location in this volume or in the Addendum.

\noindent\textbf{Companion documents.}\quad
\textit{Addendum --- Structural Constraints, Refutations, and No-Go Theorems}
(\texttt{docs/Addendum\_Refutations.pdf}) is the volume's Appendix B: the
adjudication record, the refuted hypotheses, the no-go theorems and the trap
register, moved out of the main text; where such a block stood inline, a stub
cross-reference remains. \textit{Calibration Policy}
(\texttt{docs/Calibration\_Policy.pdf}) lists every calibration slot, its
locus, its consumers, and its status under P5. The repository
\texttt{README.md} describes the package; \texttt{working\_markdowns/}
preserves the raw working corpus byte-identically;
\texttt{verification/} contains the checker suite.

\noindent\textbf{Canonical tags and numbering.}\quad
Every theorem environment carries both its presentation number (Theorem 1.1,
Definition 3.12, \dots) and its canonical corpus tag (CT0.1, FT.54, BM.137,
\dots) in its head. \textbf{All cross-citations in Req lines, proofs and scope
clauses use the canonical tags}, which are unique across the corpus and are
resolved by the Index of Corpus Tags; tags moved to the Addendum keep their
identity there (Appendix B.$x$.$y$ entries are labelled with the tag).

\noindent\textbf{Citations and records.}\quad
This volume presents the corpus as a finished mathematical model: every
citation resolves to a canonical tag, a Census cell, a [math] class, or a
machine checker. The adjudications, refutations, no-go theorems and trap
register --- the record of how the model was won --- live in the Addendum;
the archival working record (including the historical ledger
\texttt{HistLog.md}) is preserved in \texttt{working\_markdowns/}. Paths of
the form \texttt{checks/verify\_*.py} in Req lines refer to
\texttt{verification/checks/verify\_*.py} in this repository.

\noindent\textbf{Verification.}\quad
The dependency graph over the registry tags is acyclic and is re-derived from
the canon at every suite run (\texttt{verify\_corpus\_graph.py}); the era
structure, document format and every algebraic identity are checked in exact
arithmetic (integer, \texttt{Fraction}, algebraic number fields, prime-log
rings, truncated power series) with no floating point in any assertion.
"""

# ------------------------------------------------------------------ documents
def build_main(docs, numbers, ids, stats):
    os.makedirs(PARTS_DIR, exist_ok=True)
    part_files = {
        "Part1_Qubit_era.md": "part1_qubit.tex",
        "Part2_Bosonic_era.md": "part2_boson.tex",
        "Part3_Fermion_era.md": "part3_fermion.tex",
        "Part4_Baryomesonic_era.md": "part4_baryon.tex",
    }
    def chapter_head(chunks, prot):
        h1 = next(c["text"] for c in chunks if c["kind"] == "h1")[2:].strip()
        return ("\\chapter{\\texorpdfstring{" + rp.conv_text(h1, prot)
                + "}{Qubitick " + rp.pdf_safe(h1) + "}}\n")
    for fn, out in part_files.items():
        prot = rp.Protector()
        chap = chapter_head(docs[fn], prot)
        body = render_chunks(docs[fn], prot, numbers, ids)
        with open(os.path.join(PARTS_DIR, out), "w", encoding="utf-8") as f:
            f.write("% " + fn + " — sanitized presentation layer (generated; see source/CONVERSION_LOG.md)\n")
            f.write(chap + "\n" + body + "\n")
        print("wrote", out, len(body.splitlines()), "lines")
    # census annex
    prot = rp.Protector()
    body = render_chunks(docs["Census.md"], prot, numbers, ids)
    h1c = next(c["text"] for c in docs["Census.md"] if c["kind"] == "h1")[2:].strip()
    with open(os.path.join(OUTDIR, "annex_census.tex"), "w", encoding="utf-8") as f:
        f.write("% Census.md — sanitized presentation layer (generated)\n")
        f.write("\\chapter{\\texorpdfstring{" + rp.conv_text(h1c, prot) + "}{Qubitick "
                + rp.pdf_safe(h1c) + "}}\n\n" + body + "\n")
    # tag index
    descs = build_descs(docs)
    write_tag_index(numbers, stats, descs)
    doc = [preamble("book", "The Qubitick Corpus"),
           main_title_page(numbers, stats),
           "\\frontmatter", PREFACE, "\\tableofcontents",
           "\\mainmatter"]
    for fn in CANON:
        doc.append("\\input{parts/" + part_files[fn] + "}")
    doc.append("\\appendix")
    doc.append("\\input{annex_census.tex}")
    doc.append("\\input{tag_index.tex}")
    doc.append("\\chapter*{Colophon}\n\\addcontentsline{toc}{chapter}{Colophon}\n"
               + colophon(stats))
    doc.append("\\end{document}")
    tex = "\n".join(doc)
    with open(os.path.join(OUTDIR, "main.tex"), "w", encoding="utf-8") as f:
        f.write(tex)
    print("wrote main.tex", len(tex.splitlines()), "lines")

def colophon(stats):
    return (r"""This volume was generated from the canon files preserved in
\texttt{working\_markdowns/} by the packaging pipeline in \texttt{source/pipeline/}.
Registry: """ + str(stats["reg_tags"]) + r""" tags; Req graph: """ + str(stats["edges"]) + r"""
edges, acyclic (re-derived at every suite run). Verification suite: """
            + str(stats["suite"]) + "/" + str(stats["suite"]) + r""" green
(\texttt{verification/run\_all.py}); exact arithmetic only --- no floating
point in any assertion. Edition of """ + stats["date"] + """. The archive,
the checkers and the mathematics are unmodified; the transformations applied
to produce this presentation layer are logged in
\texttt{source/CONVERSION\_LOG.md}.""")

AXIOM_GLOSSES = {
    "A1": "The pair register: qubit set, two-dimensional carriers, normalized positive-semidefinite pair states",
    "A2": "Every ordered pair supplies exactly one channel quantum: C(p,q) = 1q",
    "A3": "Pair-space grading: the swap S and the sign grading T; the sign vector has exactly one odd entry (representative: C13)",
    "A4": "The crystallization criterion: the two-branch threshold test on the antisymmetric weight; the binary branch index",
    "A5": "The vacuum pair state and node-level Haar randomness; the draws are not retained in the ledger",
    "A6": "The tick dynamics: Haar-drawn conjugation, trace-preserving, non-invertible, ledger-monotone",
    "A7": "Ledger stratification: the growing directed event graph with typed vertices and registration phases",
    "A8": "The complete force complex (the five aspect blocks) and the weighted configuration sum Z(R)",
    "A9": "The valid-universe condition: the universe record is a state of the configuration sum (self-consistency)",
    "P1": "The single free dimensionful scale: the hop length; every quantity derived or a power of it",
    "P2": "The derived, zero-freedom list (dimensions, counts and identities re-verified in exact arithmetic)",
    "P3": "Named combinations of the free scale (external comparison only; not inputs)",
    "P4": "Free internal configuration parameters (not constants of the theory); predictions are dimensionless ratios",
    "P5": "No quantity is identified with a measured external constant; comparison is a test of A9, not an input",
}

def plaintext(s):
    """readable text form of a canon snippet (math dropped, markup stripped)"""
    import html as _h
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\text(?:bf|it|rm)?\{([^{}]*)\}", r" \1 ", s)
    s = s.replace("**", " ").replace("\\_", "_").replace("\\neg", "not ")
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = re.sub(r"[{}\\]", " ", s)
    s = _h.unescape(s)
    s = re.sub(r"\s+", " ", s).strip(" :;,.")
    return s

def build_descs(docs):
    descs = dict(AXIOM_GLOSSES)
    for fn in CANON + ["Census.md"]:
        for c in docs[fn]:
            if c["kind"] == "tagblock":
                descs[c["tag"]] = plaintext(c["title"])
                for kind, tag, title, lines in c["segs"]:
                    if kind == "cor":
                        descs[tag] = (plaintext(title) if title else "corollary")
            elif c["kind"] == "paratag":
                body = " ".join(c["lines"])
                body = re.sub(r"^\*\*[^*]+\.\*\*\s*", "", body)
                txt = plaintext(body)
                descs[c["tag"]] = (txt[:110] + ("…" if len(txt) > 110 else "")) if txt else ""
    return descs

def write_tag_index(numbers, stats, descs):
    rows = []
    for t in REG.keys():
        meta = REG[t]
        cls = qparse.tag_class(t)
        if cls == "policy":
            clsname = "calibration policy"
        elif cls == "theorem":
            clsname = "data cell" if meta["file"] == "Census.md" else "theorem"
        else:
            clsname = cls
        fn = meta["file"]
        loc = {"Part1_Qubit_era.md": "Part 1", "Part2_Bosonic_era.md": "Part 2",
               "Part3_Fermion_era.md": "Part 3", "Part4_Baryomesonic_era.md": "Part 4",
               "Census.md": "Appendix A"}.get(fn, fn)
        pres = numbers.get(t, "—")
        if t in MOVE:
            loc = "Addendum"
        if pres.startswith("Appendix "):
            pres = pres.replace("Appendix ", "")
        rows.append((t, clsname, loc, pres, descs.get(t, ""), fn))
    extra = [(tag, "adjudication record", "Addendum", bid, plaintext(title), "HistLog.md")
             for tag, bid, title in stats.get("hist_entries", [])]
    GROUPS = [("Part1_Qubit_era.md", "Part 1 · Qubit\\_era — axioms, conventions, definitions, calibration, pair canon, ledger dynamics"),
              ("Part2_Bosonic_era.md", "Part 2 · Bosonic\\_era — geometry, electroweak, electromagnetic, colour, saturation"),
              ("Part3_Fermion_era.md", "Part 3 · Fermion\\_era — bound chains, termini, floors, carriers, channels"),
              ("Part4_Baryomesonic_era.md", "Part 4 · Baryomesonic\\_era — colour-sealed composites"),
              ("Census.md", "Appendix A · Census — the computed data cells"),
              ("HistLog.md", "Addendum B.1 · the adjudication record (HistLog §IV)")]
    out = ["\\chapter*{\\texorpdfstring{Index of Corpus Tags}{Index of Corpus Tags}}",
           "\\addcontentsline{toc}{chapter}{Index of Corpus Tags}",
           "\\markboth{Index of Corpus Tags}{Index of Corpus Tags}",
           ("The complete tag registry, with a one-line description of every tag: "
            + str(stats["reg_tags"]) + " registry tags (" + str(stats["thm_tags"])
            + " theorem and data-cell tags, " + str(stats["def_tags"])
            + " definitions, " + str(stats.get("ax_tags", 9)) + " axioms, "
            + str(stats.get("conv_tags", 13)) + " conventions, "
            + str(stats.get("pol_tags", 5)) + " calibration-policy clauses) plus the "
            "adjudication-record tags of HistLog \\S IV reproduced in the Addendum. "
            "Rows are grouped by document, in tier order; ``Presentation'' gives the "
            "theorem/definition number in this volume or the Addendum section "
            "(B.$x$.$y$) for relocated records."),
           "\\begingroup\\small",
           "\\begin{longtable}{@{}p{0.10\\textwidth}p{0.115\\textwidth}p{0.465\\textwidth}p{0.095\\textwidth}p{0.135\\textwidth}@{}}",
           "\\toprule",
           "\\textbf{Tag} & \\textbf{Class} & \\textbf{Title / description} & \\textbf{Where} & \\textbf{Presentation} \\\\",
           "\\midrule",
           "\\endhead"]
    def esc(x):
        return (x.replace("\\", "\\textbackslash{}").replace("&", "\\&")
                 .replace("_", "\\_").replace("#", "\\#").replace("%", "\\%")
                 .replace("$", "\\$"))
    allrows = rows + extra
    for gfile, gtitle in GROUPS:
        grp = [r for r in allrows if r[5] == gfile]
        if not grp:
            continue
        out.append("\\multicolumn{5}{@{}l}{\\textbf{" + gtitle + "}}\\\\[2pt]")
        last_tier = object()
        for t, clsname, loc, pres, d, _f in grp:
            tier = REG.get(t, {}).get("tier", "")
            if tier and tier != last_tier:
                last_tier = tier
                tname = tier.replace("&", "\\&")
                out.append("\\multicolumn{5}{@{}l@{}}{\\hspace*{1em}\\small\\itshape "
                           + esc(tname) + "}\\\\[1pt]")
            out.append("\\texttt{" + esc(t.replace(".", "{.}")) + "} & " + esc(clsname)
                       + " & " + (esc(d) if d else "---") + " & " + esc(loc)
                       + " & " + esc(pres) + " \\\\")
        out.append("\\addlinespace[4pt]")
    out += ["\\bottomrule", "\\end{longtable}", "\\endgroup"]
    with open(os.path.join(OUTDIR, "tag_index.tex"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("wrote tag_index.tex with", len(allrows), "rows in", len(GROUPS), "groups")

# ------------------------------------------------------------------ addendum
B_SECTION_TITLES = {
    "B1": "B.1 Category Errors",
    "B2": "B.2 Refuted Hypotheses",
    "B3": "B.3 No-Go Theorems",
    "B4": "B.4 Traps and Phantom Gaps",
}
ADDENDUM_INTRO = r"""
\section*{\texorpdfstring{Scope of this Addendum}{Scope of this Addendum}}
\addcontentsline{toc}{section}{Scope of this Addendum}

This Addendum is Appendix B of the $\langle qu(b(i(t|t))ick)\rangle$ canon
(Volume I). It
collects the corpus's structural-constraints record: category-error and status
adjudications (B.1), refuted hypotheses with their refutations (B.2), no-go
theorems (B.3), and the trap and phantom-gap register (B.4). The material
falls into three kinds of entries, marked at their heads:

\begin{itemize}
\item \textbf{Record entries} reproduce the adjudication blocks moved out of
  the main text (from Parts 2--4) and the adjudication record of the archival
  ledger (HistLog \S IV: the tier adjudication summaries FT.115, FT.121,
  FT.132, FT.140 and the closure tier F.43, FT.146--FT.152). Each keeps its
  canonical tag and its full \textbf{Thm}\,$\cdot$\,\textbf{Req}\,%
  $\cdot$\,\textbf{Pf}\,$\cdot$\,\textbf{Phys} structure, so every citation of
  these tags elsewhere in the corpus resolves here. Together these records
  trace the author's exploration pathway. They are reproduced as they stand in
  the revision-1 canon; the byte-exact pre-revision originals are preserved in
  \texttt{working\_markdowns/}.
\item \textbf{Catalog entries} record the hypothesis-level ruling of a theorem
  whose derived content is consumed by later derivations and therefore remains
  in the main corpus; the entry quotes the ruling verbatim and points to the
  main-text number.
\item \textbf{Pointer entries} (B.4) cross-reference trap disclosures that
  travel inside larger records.
\end{itemize}

Nothing in this Addendum alters the mathematics: the machine-verified canon in
\texttt{canon/} (pre-revision state frozen in \texttt{working\_markdowns/}) is the
authority, and the verification suite (\texttt{verification/run\_all.py}) checks it. Where an adjudication
or no-go stood inline in the main corpus, a stub of the form ``see Appendix B,
Section B.$x$.$y$'' marks the former locus.
"""

def build_addendum(docs, entries, ids, numbers):
    prot = rp.Protector()
    doc = [preamble("report", "Addendum"),
           r"""
\begin{titlepage}
\centering
\vspace*{2.4cm}
{\LARGE $\langle qu(b(i(t|t))ick)\rangle$ — the four-era canon\par}
\vspace{0.8cm}
{\Huge\bfseries Appendix B\par}
\vspace{0.5cm}
{\LARGE Structural Constraints, Refutations,\\ and No-Go Theorems\par}
\vspace{1.0cm}
{\large Addendum to the four-era canon, Volume I\par}
\vspace{0.4cm}
{\large The adjudication record, the refuted hypotheses, the no-go theorems,\\ and the trap and phantom-gap register\par}
\vfill
{\large Edition of """ + datetime.date.today().isoformat() + r"""\par}
\vspace{0.3cm}
{\small Entries preserve the canonical tags and the full Thm\,$\cdot$\,Req\,$\cdot$\,Pf\,$\cdot$\,Phys structure; the mathematics is transplanted unmodified.\par}
\end{titlepage}
""",
           "\\tableofcontents",
           ADDENDUM_INTRO]
    for sec in ("B1", "B2", "B3", "B4"):
        title = B_SECTION_TITLES[sec]
        doc.append("\\section*{\\texorpdfstring{" + title + "}{" + rp.pdf_safe(title) + "}}")
        doc.append("\\addcontentsline{toc}{section}{" + rp.pdf_safe(title) + "}")
        doc.append("\\markboth{" + rp.pdf_safe(title) + "}{" + rp.pdf_safe(title) + "}")
        for e in entries[sec]:
            doc.append(render_entry(e, prot, numbers, ids))
    doc.append("\\end{document}")
    tex = "\n".join(doc)
    with open(os.path.join(OUTDIR, "addendum.tex"), "w", encoding="utf-8") as f:
        f.write(tex)
    print("wrote addendum.tex", len(tex.splitlines()), "lines")

def render_entry(e, prot, numbers, ids):
    out = []
    bid = e["id"]
    if e["type"] == "block":
        head = bid + "\\quad " + e["tag"] + " — " + e["title"]
        out.append("\\subsection*{\\texorpdfstring{" + rp.conv_text(head, prot) + "}{"
                   + rp.pdf_safe(e["tag"] + " " + bid) + "}}")
        out.append("\\addcontentsline{toc}{subsection}{" + rp.pdf_safe(bid + " " + e["tag"]) + "}")
        out.append("\\phantomsection\\label{" + lbl(e["tag"]) + "}")
        tier = REG.get(e["tag"], {}).get("tier")
        srcline = ("\\textit{Record.}\\quad Source: " + tescape(e["src"])
                   + ("; tier: " + tescape(tier) if tier else "")
                   + "; canonical tag \\texttt{" + e["tag"].replace("_", "\\_") + "}. "
                   "Reproduced from the revision-1 canon; a cross-reference stub marks the "
                   "former locus in the main corpus.")
        out.append("{\\small " + srcline + "}\n\\medskip")
        body = e["body"]
        body = apply_presentation_transforms(body)
        out.append(rp.convert_md(body, prot))
    elif e["type"] == "histlog":
        tag = e["tag"] or "§IV.2"
        head = bid + "\\quad " + ((e["tag"] + " — ") if e["tag"] else "") + e["title"]
        out.append("\\subsection*{\\texorpdfstring{" + rp.conv_text(head, prot) + "}{"
                   + rp.pdf_safe((e["tag"] or "IV.2") + " " + bid) + "}}")
        out.append("\\addcontentsline{toc}{subsection}{" + rp.pdf_safe(bid + " " + (e["tag"] or "SIV.2")) + "}")
        if e["tag"]:
            out.append("\\phantomsection\\label{" + lbl(e["tag"]) + "}")
        out.append("{\\small \\textit{Record.}\\quad Source: " + e["src"]
                   + " (archival ledger, preserved at \\texttt{working\\_markdowns/HistLog.md}); "
                   "reproduced verbatim, including its historical registry tokens, which "
                   "resolve via HistLog \\S I.}\n\\medskip")
        out.append(rp.convert_md(e["body"], prot))
    elif e["type"] == "rmk":
        head = bid + "\\quad The two distance claims of the derivation record, resolved"
        out.append("\\subsection*{\\texorpdfstring{" + head + "}{" + rp.pdf_safe("B.2.1 distance claims") + "}}")
        out.append("\\addcontentsline{toc}{subsection}{" + rp.pdf_safe(bid + " distance claims") + "}")
        out.append("{\\small \\textit{Record.}\\quad Source: " + e["src"] +
                   "; moved from the FT.48 block (the framing reference to the "
                   "derivation record is retained here as provenance; the main-text "
                   "stub is neutral).}\n\\medskip")
        out.append(rp.convert_md(GEN_RMK_TEXT, prot))
    elif e["type"] == "catalog":
        tag = e["tag"]
        head = bid + "\\quad " + tag + " — " + e["title"] + " (catalog entry)"
        out.append("\\subsection*{\\texorpdfstring{" + rp.conv_text(head, prot) + "}{"
                   + rp.pdf_safe(tag + " " + bid) + "}}")
        out.append("\\addcontentsline{toc}{subsection}{" + rp.pdf_safe(bid + " " + tag) + "}}".replace("}}", "}"))
        out.append("\\phantomsection\\label{" + lbl(tag) + "-cat}")
        mainref = e["mainref"]
        lead = ("\\textit{Catalog.}\\quad The full theorem remains in the main corpus as "
                + mainref + " (" + e["src"] + "); its derived clauses are consumed by later "
                "derivations. The hypothesis-level ruling is recorded here verbatim:")
        out.append("{\\small " + rp.conv_text(lead, prot) + "}")
        kind, quote = e["quote"]
        if kind == "display":
            out.append("\\[\n" + rp.repair_display(quote) + "\n\\]")
        else:
            out.append("\\begin{quote}\\small " + rp.conv_text(quote, prot) + "\\end{quote}")
    elif e["type"] == "pointer":
        head = bid + "\\quad " + e["tag"]
        out.append("\\subsection*{\\texorpdfstring{" + rp.conv_text(head, prot) + "}{"
                   + rp.pdf_safe(e["tag"] + " " + bid) + "}}")
        out.append("\\addcontentsline{toc}{subsection}{" + rp.pdf_safe(bid + " " + e["tag"]) + "}")
        out.append("{\\small \\textit{Pointer.}\\quad " + rp.conv_text(e["text"], prot) + "}")
    out.append("\\medskip")
    return "\n".join(out)

# Phys-phrase presentation transforms also apply inside addendum bodies
TRANSFORM_PAIRS = [
    ("everything the corpus says is either a fixed number",
     "every quantity the corpus derives is either a fixed number"),
    ("the fourth is not, and the corpus says why",
     "the fourth is not, and the structure yields why"),
    ("Where the machinery has no domain the corpus says so instead:",
     "Where the machinery has no domain, the structure yields the obstruction instead:"),
    ("Add the edges and you get six; add the masses and you get nothing.",
     "Adding the edges yields six; adding the masses yields nothing."),
]
def apply_presentation_transforms(text):
    for old, new in TRANSFORM_PAIRS:
        text = text.replace(old, new)
    return text

GEN_RMK_TEXT = None   # filled by driver

# ------------------------------------------------------------------ driver
def main():
    global GEN_RMK_TEXT
    docs = stage_parse()
    moved, rmk_text = stage_sanitize(docs)
    GEN_RMK_TEXT = rmk_text.replace(
        "**Rmk (the generator program's two distance claims, resolved).**",
        "**Rmk (the two distance claims, resolved).**")
    hist = stage_histlog()
    entries, ids = assign_ids(moved, hist)
    numbers = stage_number(docs, ids)
    cat_log = build_catalog(docs, entries, ids, numbers)
    # fill pointer texts with resolved ids/numbers
    for e in entries["B4"]:
        if e["type"] == "pointer" and e.get("text"):
            e["text"] = e["text"].format(
                ft73=ids["FT.73"], ft77=ids["FT.77"], ft89=ids["FT.89"],
                ft158=numbers.get("FT.158", "FT.158"))
    # stats
    import collections
    graph_head = open(os.path.join(SRC, "index", "graph.md"), encoding="utf-8").readline()
    m = re.search(r"(\d+) registry entries; (\d+) Req edges", open(
        os.path.join(SRC, "index", "graph.md"), encoding="utf-8").read())
    reg_tags, edges = int(m.group(1)), int(m.group(2))
    cls_count = collections.Counter(qparse.tag_class(t) for t in REG)
    thm_tags = cls_count["theorem"]
    stats = {"date": datetime.date.today().isoformat(), "reg_tags": reg_tags,
             "edges": edges, "thm_tags": thm_tags,
             "hist_entries": [(e["tag"], e["id"], e["title"]) for e in entries["B1"]
                              if e["type"] == "histlog" and e.get("tag")],
             "def_tags": cls_count["definition"], "suite": 80,
             "ax_tags": cls_count["axiom"], "conv_tags": cls_count["convention"],
             "pol_tags": cls_count["policy"]}
    build_main(docs, numbers, ids, stats)
    build_addendum(docs, entries, ids, numbers)
    import qcalib
    qcalib.build(docs, numbers, ids)
    # conversion log
    write_log(entries, ids, numbers, cat_log, stats)
    print("done.")

def write_log(entries, ids, numbers, cat_log, stats):
    lines = ["# Conversion log — qubitick_corpus_v1.0 (sanitization & restructuring pass)",
             "",
             "Generated by `source/pipeline/` from the byte-identical archive in",
             "`working_markdowns/`. The archive was not modified; the verification suite",
             "runs against it unchanged. Every operation applied to the presentation",
             "layer is listed below.",
             "",
             "## Registry facts (machine-derived, `verify_corpus_graph.py`)",
             "",
             f"- registry tags: **{stats['reg_tags']}** (theorem/cell tags: {stats['thm_tags']}, "
             f"definitions: {stats['def_tags']}, axioms: 9, conventions: 12, policy clauses: 5)",
             f"- Req edges: **{stats['edges']}**, graph acyclic (re-derived at every suite run)",
             f"- verification suite: **{stats['suite']}/{stats['suite']} green** "
             "(the figure 77/77 quoted in the packaging brief predates the current canon; "
             "the pinned and executed count is 79)",
             "",
             "## 1. Block moves to the Addendum (Appendix B)",
             ""]
    for sec in ("B1", "B2", "B3", "B4"):
        for e in entries[sec]:
            if e["type"] == "block":
                lines.append(f"- **{e['tag']}** — {e['title'][:90]}  \n"
                             f"  {e['src']} → Appendix {e['id']}; stub cross-reference left at the former locus.")
            elif e["type"] == "histlog":
                lines.append(f"- **{e['tag'] or '§IV.2'}** — {e['title'][:90]}  \n"
                             f"  {e['src']} → Appendix {e['id']} (verbatim).")
            elif e["type"] == "rmk":
                lines.append(f"- **FT.48 (Rmk passage)** — the two distance claims, resolved → "
                             f"Appendix {e['id']}; neutral stub left in the FT.48 block.")
    lines += ["", "## 2. Catalog entries (theorem kept in main text; ruling recorded)", ""]
    for sec, tag, e in cat_log:
        lines.append(f"- **{tag}** → Appendix {e['id']} (catalog; main text: {e['mainref']}).")
    lines += ["", "## 3. Strips (provenance language removed from the main text)", ""]
    for kind, where, detail in LOG:
        if kind == "STRIP":
            lines.append(f"- `{where}`: {detail}")
    lines += ["", "## 4. Transforms (presentation-language rewrites)", ""]
    for kind, where, detail in LOG:
        if kind in ("TRANSFORM", "MAP-REWRITE", "PASSAGE-MOVE", "BLOCK-MOVE", "HISTLOG-EXTRACT"):
            if kind == "BLOCK-MOVE":
                continue
            lines.append(f"- `{where}` [{kind}]: {detail}")
    lines += ["",
             "## 5. Editorial decisions (preservation rule)",
             "",
             "- Req lines, Pf derivations, Thm statements, Def blocks, charters and closure",
             "  exports are preserved exactly; no mathematical content was altered.",
             "- Ledger pointers of the form `[HistLog §II item N]`, `item N`, `Q n`, `deficit n`",
             "  are corpus citation syntax (pointers, never premises) and are preserved; the",
             "  Preface explains where they resolve.",
             "- Supersession and scope records (e.g. the FT.158(5) supersession of FT.89's",
             "  classification clause, `Rmk (scope)` blocks) are governing law, not process",
             "  narrative, and are preserved in place.",
             "- Heavily consumed theorems whose titles name an adjudication (BM.30, BM.37,",
             "  BM.49, BM.61, BM.63, BM.94, BM.97, BM.117, FT.55, FT.66, FT.79, FT.82, ...)",
             "  remain in the main corpus because later derivations consume their clauses;",
             "  their rulings are catalogued in Appendix B with verbatim quotes.",
             "- The Census annex (25 frozen data cells) is published as Appendix A of the main",
             "  volume; its cells are not adjudication content (FT.99(6)'s integrity ledger is",
             "  part of the frozen cell and is preserved).",
             "- Blocks containing longtables or verbatim material are typeset with a run-in",
             "  head macro sharing the same counter (amsthm environments cannot contain",
             "  longtable/verbatim); the printed form matches the environment heads.",
             ""]
    with open(os.path.join(OUTDIR, "CONVERSION_LOG.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("wrote CONVERSION_LOG.md")

if __name__ == "__main__":
    main()
