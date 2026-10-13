# $\langle qu(b(i(t|t))ick)\rangle$ — the four-era canon · v1.0 (revision 1)

**A machine-verified, discrete-ledger-based framework for foundational
physics.** The wordmark $\langle qu(b(i(t|t))ick)\rangle$ — read _qubitick_ — is the corpus's own name;
it appears on every canon document's title line. The corpus derives, purely symbolically from nine axioms and a
single free dimensionful scale 𝔥, four successive eras — Qubit, Bosonic,
Fermion, and Baryomesonic — spanning 481 theorem and data-cell tags (623
registry tags in total, including the axioms, conventions, definitions and
calibration-policy clauses) joined by 8012 requirement edges in a strictly
acyclic dependency graph. Every algebraic identity, bound and census is checked
by an 80-checker suite in exact arithmetic: integer certificates, algebraic
number fields and prime-log rings — **no floating point anywhere, and no
external physical constant enters any derivation.**

## The two era halves

The repository is organized in **two clear halves**: **`era1/`** — the frozen, published v1.0
canon (Levels 1–4) with its verification suite and summary-generation pipeline — and **`era2/`**
— the Era-2 record (Levels 5–7), whose **Level 5 (the Atomic era) is CLOSED** at tag AT.63
(twelve tiers, 63 tags, 37 checkers, 643 exact markers, citation-gated against the era-1
registry). The publication (PDF) pipeline stays at the root (`source/` → `docs/`, reading the
frozen `working_markdowns/` archive and `era1/canon/index/`); the root documents (this README,
the licences, the AI policy) stay in place. Era-2 promotion into the frozen canon's
`Summary.md`/`index` is an Era-2-closure act, deliberately not taken at Level-5 closure.

## AI Usage

Extensive usage of Large Language Models has been used in the repository. In fact barring this single paragraph, all text in this corpus is written by an AI system. Initially multiple LLMs were used. The used systems were Gemini 3.1 Pro, Calaude Sonnet 5.1, Deepseek V3 Pro, Deepseek V4 Pro, Deepseek V4.1 Flash, Qwen3.7-Plus, Qwen3.8-Max, Qwen3.8-Omni-Flash. OpenAI models were not used in any capacity. After the initial calculations of Era 1, Anthropic and Google's models started to lose the ability to work on this corpus due their so called safeguards, and drift towards the mean corpus of human knowledge genrating hallucinated and ill structured responses. Thus further down the line, only Deepseek and Qwen models were used. All models used were the ones available in the free tier. The corpus was reviewed in it's entirety and any errors in the corpus are the author's fault and not any LLM system's.

## Repository structure

| path                 | content                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docs/`              | the compiled publications: `Qubitick_Corpus.pdf` (the monograph: Parts 1–4, the Census annex, the tag index), `Addendum_Refutations.pdf` (Appendix B: structural constraints, refutations, no-go theorems, traps), `Calibration_Policy.pdf` (every calibration slot and its status)                                                                                                     |
| `era1/`              | **the Era-1 half — the frozen v1.0 canon** (Levels 1–4): `era1/canon/` (the five published documents, `HistLog.md`, the regenerable `index/` and `Summary.md`, and `make_summary.py` — the summary-generation pipeline) and `era1/verification/` (the frozen 80-checker suite; its canon documents are symlinks into `era1/canon/` — the two move together). Published, DOI-pinned, never edited; see `era1/README.md`                                          |
| `era2/`              | **the Era-2 half — the canon-in-record for Levels 5–7** (Atomic, Isotopic, Anthropic): per-level folders with `tiers/` (tier documents in canon format), `checks/` (the exact-arithmetic verification suite and its runner/gates), and `discovery/` (session records). **Level 5 is CLOSED** (twelve tiers, tags AT.1–AT.63; the closure tag AT.63 records the level ledger and this reorganization); **Level 6 is OPEN** (Tiers IT.1–IT.11: the Measurement Theorem, the 1p-kn isotopic family, the multi-seal census at N=5,6, the N=9 isobar doublet and its weak transition, the hydrogen isotope sequence and its cutoff adjudication, the nucleon–nucleon connector species, the "exotic states" read-tier adjudication, the multi-seal amplitude calculus, the isotope-cutoff resolution, the macroscopic calibration anchor, the amplitude-binding verdict — IT.1–IT.36; opened as "Molecular", renamed **Isotopic** at session 12 — the molecular level is deferred); Level 7 unopened; see `era2/README.md`                                          |
| `archive/`           | `zenodo_v1.0_package/` — the self-contained packaged copy of the published v1.0 corpus as deposited (formerly the confusing repo-root-nested `qubitick_corpus/` folder; frozen, do not edit)                                                                                                                               |
| `source/`            | the LaTeX sources: `main.tex` + `parts/part1_qubit.tex` … `parts/part4_baryon.tex`, `annex_census.tex`, `tag_index.tex`, `addendum.tex`, `calibration.tex`; `build.sh` / `Makefile` regenerate the PDFs; `pipeline/` holds the generator; `CONVERSION_LOG.md` records the sanitization pass; `REVISION1_LOG.md` and `OPEN_ITEMS_REPORT.md` record the canon revision                    |
| `era1/verification/`   | the frozen machine-verification suite (inside the era-1 half): `run_all.py`, `requirements.txt`, `checks/` (the 80 checkers and their exact-arithmetic helpers); the canon documents are symlinks into `../canon/`; `index/` is regenerated at every suite run                                                                                                                                                            |
| `working_markdowns/` | **the frozen archive** — every raw working document exactly as delivered (pre-revision): the four era files, `Census.md`, `HistLog.md`, the summaries, the generated index, the original render tooling, the first compiled paper, the as-delivered checkers (`checks_as_delivered/`) and the revision-1 substitution sheet. This folder is the provenance record; it is never modified |

## How to read

- Open **`docs/Qubitick_Corpus.pdf`** for the main monograph.
- Open **`docs/Addendum_Refutations.pdf`** for structural constraints and no-go
  theorems (Appendix B: category errors and status adjudications, refuted
  hypotheses, no-go theorems, traps and phantom gaps). Where such a block stood
  inline in the main text, a stub cross-reference marks the former locus.
- Open **`docs/Calibration_Policy.pdf`** for the calibration slots: what each
  slot calibrates, which results depend on it, and its status under P5
  (declared, value ¬issued).

Theorems carry both a presentation number (Theorem 1.1, Definition 3.12, …)
and their canonical corpus tag (CT0.1, FT.54, BM.137, …). All cross-citations
use the canonical tags; the Index of Corpus Tags at the back of the monograph
resolves every tag to its location.

## How to verify

```bash
pip install -r era1/verification/requirements.txt   # a documented no-op: the suite is pure stdlib
python3 era1/verification/run_all.py                # the full frozen era-1 suite (80/80)
cd era2/level5_atomic/checks && python3 run_all_era2.py      # the era-2 Level-5 suite (37 checkers, 643 markers)
cd era2/level5_atomic/checks && python3 check_era2_format.py # the era-2 format + citation gate (14 documents)
cd era2/level6_isotopic/checks && python3 run_all_level6.py # the Level-6 suite (12 checkers, 187 markers)
```

Expected output: **80/80 passed — ALL GREEN** (exit code 0). All arithmetic is
exact; no floating point is used in any assertion. See
[`era1/verification/README.md`](era1/verification/README.md) for the verification
architecture (exact algebraic number fields, prime-log rings, integer
certificates, the acyclic dependency graph) and for the historical suite-count
note (history: the packaging brief quoted 77/77; the canon as delivered ran 79/79; revision 1 added `verify_CT10_signature.py`, giving the pinned and executed 80).

To rebuild the PDFs from the sources:

```bash
cd source && ./build.sh        # needs tectonic or xelatex; can auto-fetch tectonic
```

## The axiom set

- **A1 — Pair register.** A countable qubit set 𝒬 with two-dimensional
  carriers ℋ_q ≅ ℂ² and a normalized positive-semidefinite state ρ_pq for
  every ordered pair.
- **A2 — Channel quantum.** Every ordered pair supplies exactly one channel
  quantum: C(p,q) = 1𝔮.
- **A3 — Pair-space grading.** The pair space decomposes under the swap and
  sign-grading involutions (S, T): ℋ*p⊗ℋ_q = ∨²⊕∧², and T grades the Pauli
  basis by η^μη^ν where η ∈ {±1}⁴ has exactly one odd entry — the sign
  \_structure* is the axiom; the representative η = (−,+,+,+) is Convention
  C13, and CT1.0 proves the odd slot is uniquely the identity slot exactly
  when T is SU(2)-covariant.
- **A4 — Crystallization criterion.** A pair is real (crystallized) iff its
  antisymmetric weight falls outside the threshold window
  (|Π_∨ρ_pq| ≤ ε_q or ≥ 1−ε_q), fixing the binary branch index
  α_pq ∈ {0, π}; both branches are realized.
- **A5 — Vacuum state and node randomness.** The vacuum pair state is
  ρ_∘ = ¼I; states transform by node-level Haar conjugation U ∼ μ★(SU(2)),
  and the draws are not retained in the ledger.
- **A6 — Tick dynamics.** Time is the tick sequence τ*n → τ*{n+1} of
  Haar-drawn conjugations: trace-preserving, non-invertible (¬∃τ⁻¹), with a
  monotonically growing ledger 𝔏.
- **A7 — Ledger stratification.** Retained events accumulate into a growing
  directed graph Γ = (V, E) with typed vertices, per-edge registration phases
  and branch indices, stratified by tick level.
- **A8 — The complete force complex.** The force space decomposes into the
  real/virtual × positive/negative aspects and the static block
  (F = F₍₊,ℛ₎⊕F₍₋,ℛ₎⊕F₍₊,𝒱₎⊕F₍₋,𝒱₎⊕F_st), and configurations
  enter through the weighted configuration sum Z(ℛ) = Σ w(C).
- **A9 — Valid-universe condition.** The universe record 𝒰_⊙ must be a
  state of the configuration sum of the complete force; if it is not, the
  whole axiom system is falsified (the corpus's self-consistency clause).

Full statements: `docs/Qubitick_Corpus.pdf`, Chapter 1, §A (Axiom 1.1–1.9).

## Revision 1 (this edition)

Two author-directed revisions, recorded in `HistLog.md` §V.31 and
`source/REVISION1_LOG.md`:

1. **Signature de-axiomatization.** A3 no longer names η = (−,+,+,+); it states
   the structural fact (exactly one odd entry). New convention **C13** declares
   the representative; new theorem **CT1.0** classifies the T-grading (uniqueness
   of the odd slot, sign-blindness, the (7,3,3,3) census at every slot, the
   conjugacy classes, and SU(2)-covariance ⟺ 𝔬 = 0), machine-verified by
   `checks/verify_CT10_signature.py` including polynomial identities over
   ℚ(i)[a,b,c,d]. Downstream representative citations were swept across the canon.
2. **Open-ledger and deficit retirement.** The open-item apparatus (Open Gaps
   items, Q1–Q12, the deficit register) is Standard-Model-comparison-era
   residue: no requirement edge ever resolved to a ledger item, and the base
   layer stands self-contained. ~290 ledger pointers were removed mechanically
   from Parts 2–4 and the Census; the two register blocks (Census FT.84, the
   deficit table; FT.125, the deficit ledger) were relocated to Addendum B.4;
   and 45 curated rewrites state the completion status where the text formerly
   framed an open gap (e.g. the Yukawa-like coupling is named
   application-layer content, ¬ a structural absence). Proven no-gos and bars
   are completion facts and stand untouched. The residual sentence-level
   inventory awaits the next ruling batch: `source/OPEN_ITEMS_REPORT.md`.
   Full record: `source/REVISION1_LOG.md`.

## License and citation

Released under the **BSD-2-Clause License** — see [`LICENSE`](LICENSE).

```
The Qubitick Corpus, v1.0, canon revision 1 (2026). A machine-verified,
discrete-ledger-based framework for foundational physics: the four-era canon
with its verification suite.
DOI 10.5281/zenodo.23266001.
```
