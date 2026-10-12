# $\langle qu(b(i(t|t))ick)\rangle$ — the four-era canon

Formal corpus: qubits → bosonic gauge/geometry → fermionic bound chains → baryomesonic colour-sealed composites. Pure symbolic derivation from nine axioms; one free dimensionful scale; exact-arithmetic machine verification; no floating point anywhere; no external physical constant enters any derivation. Era 1 — the foundational corpus of Parts 1–4 — is closed (Part 4, BM.152): the extra-axiomatic list is empty and the corpus stands on its axioms alone.

## Layout

| file | content | namespace |
| --- | --- | --- |
| `Part1_Qubit_era.md` | axioms A1–A9 · conventions C1–C13 · the definition layer D0.1–D4.3 · master symbol table · calibration P1–P5 · foundations CT0.1–CT0.14, CT1.0–CT1.11b · ledger dynamics L0–L5 | A*, C*, D*, P*, CT0.*, CT1.1–11b, L* |
| `Part2_Bosonic_era.md` | geometry CT1.12–CT2.11 · electroweak EW.1–EW.36a · electromagnetic EM.1–EM.26 (+Def-EM.20–22) · colour CT3.1–CT3.22a · saturation CT4.1–CT4.13 · Cal-2 | CT1.12+, CT2.*, EW.*, EM.*, CT3.*, CT4.* |
| `Part3_Fermion_era.md` | the fermion layer: measurement primitives, the fermion definition, floors, spin/stability, flicker, spectra, Clifford/branches, path integrals, family channels, carrier/parity, rung one, the 3+1 chiral asymmetry (Tier F.44) · the interface layer Def-H.35–Def-H.43 · the derived interface theorems FT.153–FT.155 · Cal-F | Def-H.1–43, FT.1–FT.145 (structural), FT.153–160 |
| `Part4_Baryomesonic_era.md` | colour-sealed composites: baryon/meson chain composites, junction grammar, observability, the forced family group, the invariance laws, census consumption, the mass and coupling layers, the Janus and annihilation channels, the Haar–Poisson duality, the continuum-limit tier and the foundational-era closure · Cal-BM | Def-BM.1–20, BM.1–152 (Tiers 4.0, BM.1–BM.24) |
| `Census.md` | the 25 computed data cells (Category B) + the consumption block | FT.28, FT.32, FT.35, FT.42–45, FT.49–51, FT.63–65, FT.69, FT.76, FT.78, FT.81, FT.83, FT.84, FT.96, FT.98, FT.99, FT.105, FT.114, FT.120 |
| `HistLog.md` | §0 provenance · §I declaration history + disposition ledger · §II open ledger (items 1–21, Q1–Q12, declaration requirements) · §III status ledger · §IV adjudication record (FT.115/121/132/140, FT.146–152) · §V verification history | historical tokens (P-H*, FT.146–152) live only here |
| `H_archive/` | **externalized** — the 21 first-edition files now live in a separate historical-archive repository. Not bundled here; the content checkers gate their first-edition pins on `era_paths.ARCHIVE_PRESENT` (see `checks/README.md`) | — |
| `checks/` | the verification suite (`python3 checks/run_all.py`) | — |
| `index/` | generated: tag registry, dependency graph, tier index | — |

## The era chain

Part 2 cites Part 1; Part 3 cites Parts 1–2; Part 4 cites Parts 1–3; Census and HistLog are annexes cited row-wise (Census cells and HistLog items are data/pointers, never premises). The tag-level citation graph is acyclic; `checks/verify_era_structure.py` machine-verifies ownership, closure, acyclicity, the era-chain law, the census separation, and declaration hygiene.

## Format

Per Part 1 §0.4: **Thm** (symbolic statement) · **Req** (axioms, definitions, prior theorems used) · **Pf** (symbolic derivation, justifications in $[\cdot]$) · **Phys** (English summary). Definitions carry **Def.** blocks with their constitutive and scope clauses inline. Conditional theorems carry their hypotheses in **Thm**/**Req**. Forward pointers are marked at the citing site.

## The declaration surface

The corpus's non-derived surface, in full: the axioms (Part 1 §A); the theorem-local dynamical scopes (L0's crystallization–tilt coupling; CT4.5a's ensemble scope; L4's finite incidence); the interface definitions Def-H.35–Def-H.43 with their stated non-derived clauses (each priced by a minimality, uniqueness, form-uniqueness, or irreducibility theorem — see HistLog §I.3); the materialization scope clauses M1/M2 (Def-H.20); the identification and convention declarations (A-BM.1–A-BM.13; HistLog §II.4); and the free internal configuration parameters (P4-class: Part 1 §E core; Cal-2; Cal-F; Cal-BM). The extra-axiomatic list of Part 1 §0.2a is empty: the two continuum-limit conditions CT2.6(ii)–(iii) are reclassified as derived theorems (Part 4, Tier BM.24, BM.151) — the axiom surface is the entire non-derived surface. The single free dimensionful scale is $\mathfrak h$ (P1). The former declared-choice registry (P-H0–P-H20a) is fully dispositioned: HistLog §I.3 is the map.

## Verification

```
cd checks && python3 run_all.py        # exit 0 = all green (80 checkers)
python3 checks/verify_era_structure.py # era law, ownership, census separation, hygiene
python3 checks/verify_corpus_graph.py  # citation closure, acyclicity, index regeneration
python3 checks/check_format.py         # document structure of the five canon files
```

Pure Python 3 standard library; exact arithmetic (`fractions.Fraction`, complex-over-`Fraction`, truncated power series, exact radical rings); no floating point in any assertion.

## Rendering as a formal paper

```
python3 render_paper.py                    # -> paper/qubitick_corpus.{tex,pdf}
                                           #    (preface + Parts 1–4 + Census)
python3 render_paper.py --include-histlog  # also render the HistLog annex
python3 render_paper.py --wide             # reading build -> paper/qubitick_corpus_wide.{tex,pdf}
                                           #    landscape 11x8.5in, 0.7in margins (~9.6in text
                                           #    block): the display-breaking threshold rises
                                           #    80 -> 118 visible chars and the table font caps
                                           #    rescale, so far fewer displays are split
python3 render_paper.py --tex-only         # write the LaTeX, compile locally
python3 render_paper.py --fetch-engine     # download a self-contained tectonic (XeLaTeX)
python3 render_paper.py --clean            # delete the auxiliary files first; use
                                           #   this after an interrupted build
```

Three guards make the build self-diagnosing. **Display hygiene:** a `$` written
directly inside a `$$…$$` display ends it early and halts XeTeX with
`! Display math should end with $$`, so the renderer drops math-mode `$`
delimiters inside displays — preserving those inside `\text{}`/`\textbf{}`/
`\emph{}`, where they are required — normalises a `$$` delimiter that was split
across two lone-`$` lines, and reports both counts. **Row breaks:** an `array`
row whose first cell begins with a literal `[` is read by LaTeX as a row break
carrying an optional vertical space, so a cell opening with a bracketed quantity
asks TeX for that quantity in points and halts with `! Illegal unit of measure
(pt inserted).`; the renderer inserts the standard empty group between the row
break and the bracket, unless the bracket really is a length such as `\\[6pt]`.
**Pre-flight:** the generated LaTeX is then scanned and the engine is not invoked
at all if a bare `$` survives inside a `\[…\]`, if a row break is followed by a
bracket that is not a length, or if the display delimiters do not balance; each
fault is reported with the nearest preceding heading, so it is findable in the
canon. The pre-flight also scans the tables for the array-syntax defects: an
inflated row-end backslash run (>=4 adjacent, scattering empty rows), a swallowed
`\hline` (an even-length backslash run before the word, which typesets it as
literal text) and a misplaced `\hline` (the fatal `! Misplaced \noalign`).
`check_format.py` rejects all of these defect classes at the source.

An interrupted compile leaves a **truncated `.aux`**, and the next build then
dies at `\begin{document}` with `! File ended while scanning use of
\@newl@bel` — a message that points at the preamble and not at the cause. The
renderer validates the auxiliary files before compiling, removes the corrupt
ones, removes them again after any failed compile so a failure cannot poison the
next run, and names this failure in plain language when it sees it. `--clean`
forces the removal.


## Reading on screen

```
python3 render_html.py                     # -> paper/qubitick_reader.html (single file)
python3 render_html.py --include-histlog   # + the HistLog annex
python3 render_html.py --summary           # the Summary of Record instead of the canon
python3 render_html.py --offline-mathjax   # no CDN reference; TeX left for a local MathJax
```

`render_html.py` writes one self-contained HTML file (no build step, no engine):
every tag is its own card with an anchor, the sidebar is a filterable index of
all 535 tags (press `/` to filter), proofs fold away for a statements-only read
(the fold state persists), tables and displays scroll instead of breaking, and
the layout follows the system colour scheme with a print stylesheet. Mathematics
is typeset by MathJax (CDN on first open); the TeX is passed through verbatim,
so nothing is re-flowed or split — this is the reading artifact, `render_paper.py`
remains the formal paper.

`render_paper.py` converts the canon into one book-class LaTeX document —
title page, table of contents, PDF bookmarks per tag, measured-width
`longtable` censuses (wrapping p-columns, per-table font scaling), all
mathematics passed through verbatim — and runs a compile-and-repair loop:
every overfull display is progressively scaled (small → footnotesize →
scriptsize → resize-to-width), wide paragraphs get `sloppypar`, wide tables
drop a font size, until the log is clean (>8pt threshold, max 5 rounds).
Engines: tectonic (auto-detected or `--fetch-engine`), or `--engine
xelatex/lualatex/pdflatex` locally. Corpus-level LaTeX repairs applied at
transplant are recorded in HistLog §0.4.

## Summary tools

```
python3 make_summary.py                    # -> Summary.md  (statements only)
python3 make_summary.py --pdf              # + paper/Summary.pdf
python3 trace_tags.py D1.2 FT.111          # -> Summary_subset.md
python3 trace_tags.py FT.54 --pdf --depth 6
python3 trace_tags.py BM.1 --out traces/bm1.md --no-statements
```

`make_summary.py` produces the **Summary of Record**: every axiom,
convention, definition (including the constitutive/interface clauses — the
postulate surface), calibration policy, theorem and corollary *statement*,
plus the open ledger (gap items 1–21, Q1–Q12, declaration requirements) —
no proofs, requirement lines, remarks, or commentary.

`trace_tags.py` accepts a list of tags (clause suffixes like `FT.111(3)`
are accepted and stripped) and produces a **summary subset**: the complete
dependency closure under the canonical **Req.** record, traced to the axioms
and definitions — an ancestor tree per seed, the closure table in
dependency order, and the statements of the closure, dependencies first.
Shared parsing lives in `corpus_lib.py`.
