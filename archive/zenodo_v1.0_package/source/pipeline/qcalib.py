#!/usr/bin/env python3
"""qcalib.py — build source/calibration.tex (the Calibration Policy document).

Every slot datum is quoted or mechanically extracted from the corpus's own
calibration registries (Part 1 §E P1–P5, Part 2 §Cal-2, Part 3 §Cal-F,
Part 4 §Cal-BM, Part 1 §D symbol table, Census quarantine row); the builder
asserts each verbatim anchor against the canon before use.
"""
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import qparse
import qtexify as qt
import rp_patched as rp
from qpipeline import SRC, OUT

def read(fn):
    return open(os.path.join(SRC, fn), encoding="utf-8").read()

P1TXT = read("Part1_Qubit_era.md")
P2TXT = read("Part2_Bosonic_era.md")
P3TXT = read("Part3_Fermion_era.md")
P4TXT = read("Part4_Baryomesonic_era.md")
CETXT = read("Census.md")

def anchor(text, frag, where):
    assert frag in text, f"calibration anchor missing in {where}: {frag[:70]!r}"
    return frag

# ------------------------------------------------------------------ slot sheets
# (slot-math, short id, calibrates, dependents, registration, status)
def core_slots():
    anchor(P1TXT, "except the hop length $\\mathfrak h$; $[\\mathfrak h]=\\mathfrak q^{-1/2}$; $\\mathfrak h$ fixes the absolute scale", "P1")
    anchor(P1TXT, "Independent core: $g,\\ g';\\ h_0;\\ c_W;\\ \\Lambda;\\ \\varkappa,\\ \\beta,\\ \\alpha_\\Omega$", "P4")
    anchor(P1TXT, "Functionally dependent members (properties of a solution, $\\neg$ further freedom): $\\theta_W(g,g')$ [EW.24]; $e(g,g')$ [EW.35]; $\\mu_\\star^2(c_W,\\varkappa,\\beta,h_0)$ [EW.33]; $m_W,\\ m_Z$ [EW.20, EW.23]; $m_H$ [EW.27]", "P4")
    anchor(P1TXT, "weak, hypercharge, EM couplings; Higgs background", "§D")
    anchor(P1TXT, "stretch scalar; identity on force space", "§D")
    anchor(P1TXT, "embedding scale; gravitational coupling; Newton constant", "§D")
    anchor(P1TXT, "metric embedding constants", "§D")
    dep = ("functionally dependent members (properties of a solution, $\\neg$ further "
           "freedom [P4]): $\\theta_W(g,g')$ [EW.24]; $e(g,g')$ [EW.35]; "
           "$\\mu_\\star^2(c_W,\\varkappa,\\beta,h_0)$ [EW.33]; $m_W,\\ m_Z$ [EW.20, EW.23]; "
           "$m_H$ [EW.27]")
    return [
        ("$\\mathfrak h$", "h",
         "the hop length — the single free dimensionful scale; $[\\mathfrak h]=\\mathfrak q^{-1/2}$; "
         "fixes the absolute scale (P1; D0.6)",
         "every dimensionful quantity of the corpus is a power of $\\mathfrak h$ (P1); "
         "named combinations $G_N=\\mathfrak h^2/(4\\ln2)$, $\\kappa^2=8\\pi G_N=2\\pi\\mathfrak h^2/\\ln2$ "
         "[P3; CT2.9]",
         "Part 1 §E (P1, P3); D0.6; D2.9",
         "free scale, value $\\neg$issued [P1, P5]"),
        ("$g$", "g", "the weak coupling (§D: weak, hypercharge, EM couplings)",
         "$\\theta_W(g,g')$ [EW.24]; $e(g,g')$ [EW.35]; $m_W,\\ m_Z$ [EW.20, EW.23] (" + dep + ")",
         "Part 1 §E (P4 core); EW.33", "declared, value $\\neg$issued [P4, P5]"),
        ("$g'$", "gp", "the hypercharge coupling (§D: weak, hypercharge, EM couplings)",
         "$\\theta_W(g,g')$ [EW.24]; $e(g,g')$ [EW.35] (" + dep + ")",
         "Part 1 §E (P4 core); EW.33", "declared, value $\\neg$issued [P4, P5]"),
        ("$h_0$", "h0", "the Higgs background (§D)",
         "$\\mu_\\star^2(c_W,\\varkappa,\\beta,h_0)$ [EW.33]; $m_H$ [EW.27] (" + dep + ")",
         "Part 1 §E (P4 core); EW.33", "declared, value $\\neg$issued [P4, P5]"),
        ("$c_W$", "cW", "the electroweak mixing datum entering the scalar trace mode",
         "$\\mu_\\star^2(c_W,\\varkappa,\\beta,h_0)$ [EW.33]; $\\theta_W(g,g')$ [EW.24] (" + dep + ")",
         "Part 1 §E (P4 core); EW.24, EW.33", "declared, value $\\neg$issued [P4, P5]"),
        ("$\\Lambda$", "Lam", "the stretch scalar — identity on the $D^+$ force space "
         "($F_{D^+}=\\Lambda\\,\\mathbb I$) [A8; §D]",
         "no dependent member is listed in P4; the $D^+$ sector datum [A8]",
         "Part 1 §E (P4 core); A8; §D", "declared, value $\\neg$issued [P4, P5]"),
        ("$\\varkappa$", "vark", "the sector-to-metric embedding scale [C4; D2.1]; "
         "$\\varkappa\\ne\\kappa$ (C4)",
         "$\\mu_\\star^2(c_W,\\varkappa,\\beta,h_0)$ [EW.33] (" + dep + ")",
         "Part 1 §E (P4 core); C4; D2.1", "declared, value $\\neg$issued [P4, P5]"),
        ("$\\beta$", "beta", "a metric embedding constant [§D; D2.1]",
         "$\\mu_\\star^2(c_W,\\varkappa,\\beta,h_0)$ [EW.33] (" + dep + ")",
         "Part 1 §E (P4 core); D2.1", "declared, value $\\neg$issued [P4, P5]"),
        ("$\\alpha_\\Omega$", "aOm", "a metric embedding constant [§D; D2.1]",
         "no dependent member is listed in P4",
         "Part 1 §E (P4 core); D2.1", "declared, value $\\neg$issued [P4, P5]"),
    ]

def spectral_slot():
    frag = anchor(P2TXT, "Logged spectral datum of this part: $\\alpha_{\\mathrm{EM}}^{(2)}$ — the EM-block scale read [EM.17]: operatorially defined; no theorem of the corpus fixes its numerical value under the dynamic-phase regime [EM.25(8)]; it is a spectral datum of $\\mathbf F$ at the solution level, $\\neg$a fitted constant and $\\neg$a P4 core member; no result consumes its value", "Cal-2")
    return ("$\\alpha_{\\mathrm{EM}}^{(2)}$", "aEM2",
            "the EM-block scale read [EM.17] — a spectral datum of $\\mathbf F$ at the "
            "solution level, $\\neg$a fitted constant and $\\neg$a P4 core member (Cal-2)",
            "no result consumes its value — every edge-level phase read uses the "
            "registration data $\\alpha_e\\in\\{0,\\pi\\}$ [Def-EM.20, EM.20] (Cal-2)",
            "Part 2 §Cal-2; EM.17; EM.25(8)",
            "logged spectral datum; value $\\neg$issued; any future use that needs a value "
            "requires a HistLog §I addendum entry first (Cal-2)")

def bm_slots():
    anchor(P4TXT, "the bridge's dimensionless calibration ratio $\\rho_{\\mathrm B}=\\hat\\mu'^2\\mathfrak h^2/(\\ln2)^2\\in\\mathfrak q^0$ [BM.69(2); BM.98; BM.102(5)]", "Cal-BM")
    anchor(P4TXT, "a packaging of Cal-F's $\\hat\\mu'^2$ and P1's $\\mathfrak h$, hence $\\neg$a new free parameter and $\\neg$a new dimensionful scale; no numerical value attaches to it here or anywhere [P5; BM.69(4)'s four grounds stand: the slot is declared, $\\neg$derived]", "Cal-BM")
    anchor(P4TXT, "(\\mathrm{C\\text{-}BM.2})\\quad e_0:\\ \\ \\text{the numerical value of the electric coupling}\\ [\\mathrm{EM.25}(7);\\ \\mathrm{BM.88}(8);\\ \\mathrm{BM.133}(6)];\\ \\ \\text{value}\\ \\neg\\text{issued};\\ \\neg\\text{fixed by measurement}\\ [\\mathrm{P5}]", "Cal-BM")
    anchor(P4TXT, "(\\mathrm{C\\text{-}BM.3})\\quad\\mu_\\nu,\\ \\mu,\\ \\rho_\\ell,\\ \\rho_\\nu:\\ \\ \\text{the channel scales, inherited from}\\ \\mathrm{Cal\\text{-}F},\\ \\neg\\text{declared in this part}\\ [\\mathrm{FT.145}(3);\\ \\mathrm{BM.83}(5),(7)]", "Cal-BM")
    return [
        ("$\\rho_{\\mathrm B}$", "rhoB",
         "the bridge's dimensionless calibration ratio "
         "$\\rho_{\\mathrm B}=\\hat\\mu'^2\\mathfrak h^2/(\\ln2)^2\\in\\mathfrak q^0$ — a packaging "
         "of Cal-F's $\\hat\\mu'^2$ and P1's $\\mathfrak h$, hence $\\neg$a new free parameter "
         "and $\\neg$a new dimensionful scale (C-BM.1)",
         "the organic-bridge energy audit [BM.69(2); BM.98; BM.102(5)]; no numerical value "
         "attaches to it here or anywhere [P5; BM.69(4)'s four grounds]",
         "Part 4 §Cal-BM (C-BM.1; A-BM.9, Tier BM.20); BM.143(4) consolidation",
         "slot declared, value $\\neg$issued [A-BM.9; P5]"),
        ("$e_0$", "e0",
         "the numerical value of the electric coupling (C-BM.2)",
         "the running-coupling completion [EM.25(7); BM.88(8); BM.133(6)]",
         "Part 4 §Cal-BM (C-BM.2); EM.25(7)",
         "value $\\neg$issued; $\\neg$fixed by measurement [P5]"),
        ("$\\mu_\\nu,\\ \\mu,\\ \\rho_\\ell,\\ \\rho_\\nu$", "chan",
         "the channel scales, inherited from Cal-F, $\\neg$declared in Part 4 (C-BM.3)",
         "the rung-one spectrum [FT.145(3)]; the beta-decay channel reads [BM.83(5),(7)]",
         "Part 4 §Cal-BM (C-BM.3); Part 3 §Cal-F",
         "inherited; values $\\neg$issued [P5]"),
    ]

def calF_rows():
    """Mechanically parse the §Cal-F table rows (parameter | locus | dimension | consumers)."""
    m = re.search(r"(?m)^\| parameter \| locus \| dimension \| consumers \|\n\|[-| ]+\|\n((?:\|.*\n)+)", P3TXT)
    assert m, "Cal-F table not found"
    rows = []
    for line in m.group(1).strip().split("\n"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        assert len(cells) == 4, cells
        rows.append(cells)
    return rows

# ------------------------------------------------------------------ sections
def section_chunks(docs, fn, h2_prefix, stop_at_hr=False):
    ch = docs[fn]
    i = None
    for k, c in enumerate(ch):
        if c["kind"] == "h2" and c["text"].startswith(h2_prefix):
            i = k; break
    assert i is not None, (fn, h2_prefix)
    out = []
    for c in ch[i + 1:]:
        if c["kind"] == "h2":
            break
        if c["kind"] == "hr" and stop_at_hr:
            break
        out.append(c)
    # include the h2 itself for rendering
    return [ch[i]] + out

def build(docs, numbers, ids):
    prot = rp.Protector()
    date = datetime.date.today().isoformat()
    doc = [qt.preamble("report", "Calibration Policy"), r"""
\begin{titlepage}
\centering
\vspace*{2.6cm}
{\LARGE $\langle qu(b(i(t|t))ick)\rangle$ — the four-era canon\par}
\vspace{0.8cm}
{\Huge\bfseries Calibration Policy\par}
\vspace{0.5cm}
{\LARGE The Declared Slots of the Corpus\par}
\vspace{1.0cm}
{\large Companion document to the four-era canon, Volume I\par}
\vspace{0.4cm}
{\large Every calibration slot, what it calibrates, which results depend on it,\\ and its status under P5\par}
\vfill
{\large Edition of """ + date + r"""\par}
\vspace{0.3cm}
{\small Calibration is a policy decision, not a mathematical derivation; this document therefore stands apart from the monograph. All slot data are transcribed from the corpus's own registries (Part 1 §E; Part 2 §Cal-2; Part 3 §Cal-F; Part 4 §Cal-BM).\par}
\end{titlepage}
""",
        "\\tableofcontents",
        r"""
\section*{\texorpdfstring{Purpose and standing}{Purpose and standing}}
\addcontentsline{toc}{section}{Purpose and standing}

This document lists every calibration slot of the corpus. A \emph{slot} is a
symbol the corpus declares as free internal configuration data (P4-class) or
logs as a spectral datum, without issuing a numerical value. The governing
constraints are the policy clauses P1--P5 of Part 1 \S E, reproduced verbatim
below; in particular:

\begin{itemize}
\item \textbf{P1} --- $\exists!\,$ free dimensionful scale: $\mathfrak h$; every
  other quantity is dimensionless-derived or a power of $\mathfrak h$.
\item \textbf{P4} --- free internal configuration parameters are
  $\neg$constants of the theory; predictions $:=$ dimensionless ratios among
  derived quantities at fixed core data.
\item \textbf{P5} --- $\neg\exists$ quantity identified with a measured
  external constant; comparison is a test of A9, $\neg$ an input to A1--A8.
\end{itemize}

Every slot below is \textbf{declared but $\neg$issued}: the corpus fixes its
locus, its dimension and its consumers, and no theorem, audit or annex attaches
a numerical value to it. No slot enters any machine-verified identity as a
number; the verification suite (\texttt{verification/run\_all.py}) is unaffected
by any future issuance, which would itself require a ledger addendum first.
"""]
    # §1 the policy clauses verbatim (Part 1 §E)
    doc.append("\\section*{\\texorpdfstring{The policy clauses P1--P5 "
               "(Part 1 §E, verbatim)}{The policy clauses P1-P5}}")
    doc.append("\\addcontentsline{toc}{section}{The policy clauses P1--P5}")
    secE = section_chunks(docs, "Part1_Qubit_era.md", "§E — Calibration policy")
    doc.append(qt.render_chunks(secE[1:], prot, numbers, ids))
    # §2 consolidated register table
    doc.append("\\section*{\\texorpdfstring{The consolidated slot register}"
               "{The consolidated slot register}}")
    doc.append("\\addcontentsline{toc}{section}{The consolidated slot register}")
    doc.append("One row per slot; the sheets that follow give the full record. "
               "P4-class members are free internal configuration parameters "
               "($\\neg$constants of the theory); all values are $\\neg$issued [P5].")
    rows = core_slots() + [spectral_slot()] + bm_slots()
    doc.append("\\begingroup\\small")
    doc.append("\\begin{longtable}{@{}p{0.14\\textwidth}p{0.34\\textwidth}p{0.26\\textwidth}p{0.18\\textwidth}@{}}")
    doc.append("\\toprule\n\\textbf{Slot} & \\textbf{Calibrates} & \\textbf{Registration} & \\textbf{Status} \\\\\n\\midrule\n\\endhead")
    for smath, sid, cal, dep, regloc, status in rows:
        doc.append(smath + " & " + cal + " & " + regloc + " & " + status + " \\\\")
    for cells in calF_rows():
        doc.append(cells[0] + " & " + cells[3][:220] + " & Part 3 §Cal-F & declared, value $\\neg$issued [P4, P5] \\\\")
    doc.append("\\bottomrule\n\\end{longtable}")
    doc.append("\\endgroup")
    # §3 slot sheets
    doc.append("\\section*{\\texorpdfstring{Slot sheets}{Slot sheets}}")
    doc.append("\\addcontentsline{toc}{section}{Slot sheets}}".replace("}}", "}"))
    p5line = ("\\textbf{P5 constraint.} $\\neg\\exists$ quantity identified with a "
              "measured external constant; comparison procedure: fix $\\mathfrak h$ "
              "once, read P2 $\\wedge$ P3; result $:=$ test of A9, $\\neg$ input to "
              "A1--A8 [P5].")
    for smath, sid, cal, dep, regloc, status in rows:
        doc.append("\\subsection*{Slot " + smath + "}")
        doc.append("\\begin{itemize}\\setlength{\\itemsep}{2pt}")
        doc.append("\\item \\textbf{Name.} " + smath + " — registered at " + regloc + ".")
        doc.append("\\item \\textbf{Calibrates.} " + cal + ".")
        doc.append("\\item \\textbf{Dependents.} " + dep + ".")
        doc.append("\\item " + p5line)
        doc.append("\\item \\textbf{Status.} " + status + ".")
        doc.append("\\end{itemize}")
    # Cal-F parsed sheets
    doc.append("\\subsection*{The fermion-era slots (Part 3 §Cal-F, parsed from the registry table)}")
    doc.append("\\begin{itemize}\\setlength{\\itemsep}{2pt}")
    for param, locus, dim, consumers in calF_rows():
        doc.append("\\item " + param + " — \\textbf{locus:} " + locus
                   + "; \\textbf{dimension:} " + dim + "; \\textbf{consumers:} "
                   + consumers + "; \\textbf{status:} declared, value $\\neg$issued "
                   "[P4, P5; any numerical use beyond the listed loci requires a "
                   "HistLog §I addendum entry first].")
    doc.append("\\end{itemize}")
    # §4 era registries verbatim
    doc.append("\\section*{\\texorpdfstring{The era registries (verbatim)}{The era registries (verbatim)}}")
    doc.append("\\addcontentsline{toc}{section}{The era registries (verbatim)}")
    for fn, pref, name in [("Part2_Bosonic_era.md", "§Cal-2", "Part 2 §Cal-2 — Calibration note (bosonic era)"),
                           ("Part3_Fermion_era.md", "§Cal-F", "Part 3 §Cal-F — Free internal parameters of the fermion era (P4-class)"),
                           ("Part4_Baryomesonic_era.md", "§Cal-BM", "Part 4 §Cal-BM — Free internal parameters of the baryomesonic era (P4-class)")]:
        doc.append("\\subsection*{" + rp.pdf_safe(name).replace("S", "§") + "}")
        chunks = section_chunks(docs, fn, pref, stop_at_hr=True)[1:]
        doc.append(qt.render_chunks(chunks, prot, numbers, ids))
    # §5 quarantine
    doc.append("\\section*{\\texorpdfstring{P5 and the external-data quarantine}"
               "{P5 and the external-data quarantine}}")
    doc.append("\\addcontentsline{toc}{section}{P5 and the external-data quarantine}")
    m = re.search(r"\*\*External-data quarantine\.\*\*[^\n]*", CETXT)
    assert m
    doc.append("\\begin{quote}\n" + rp.convert_md(m.group(0), prot) + "\n\\end{quote}")
    doc.append(rp.convert_md(
        "External comparison data enter only quarantined audit rows (Census FT.114, "
        "FT.120; P1, P5): tested, never trusted, entering no derivation. No slot of "
        "this register is fixed by any such row.", prot))
    doc.append("\\end{document}")
    tex = "\n".join(doc)
    path = os.path.join(OUT, "calibration.tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write(tex)
    print("wrote calibration.tex", len(tex.splitlines()), "lines")
