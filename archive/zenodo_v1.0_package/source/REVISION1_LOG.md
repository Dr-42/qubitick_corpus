# REVISION1_LOG.md — canon revision 1 (signature de-axiomatization + open-ledger retirement)

Applied 2026-10-08 to `canon/` (the living canon). The pre-revision corpus is
frozen byte-identically in `working_markdowns/`; the author's substitution
sheet is archived at `working_markdowns/Revision1_eta_substitution_sheet.md`;
the ledger record is `canon/HistLog.md` §V.31. Suite state after the revision:
**80/80 green** (registry 623 tags, 8012 Req edges, acyclic).

## R1a — The signature pass (η de-axiomatization)

Applied verbatim from the substitution sheet (Option A), 36 asserted
single-occurrence replacements across 6 files (`build pipeline:
apply_eta_sheet.py`, archived with the generator):

* **A3 (Part 1 §A):** the vector literal `η = (-,+,+,+)` is replaced by the
  structural sign condition `η ∈ {±1}⁴`, `∃! 𝔬 : η^𝔬 = −η^μ ∀μ≠𝔬`.
* **C13 (Part 1 §B, new):** the signature convention — `𝔬 := 0`, `η⁰ := −1`,
  i.e. `η := (-,+,+,+)` (mostly-plus, matching D2.1) — with the freedom
  boundary stated openly (overall sign free; spatial odd slots SU(2)-conjugate;
  `𝔬 = 0` vs `𝔬 ≥ 1` the SU(2)-covariant selection on which CT1.2's generator
  table rests). ¬ an axiom.
* **CT1.0 (Part 1, Tier 1A, new):** the signature classification of the
  T-grading, clauses (1)–(5) + Phys + Rmk, inserted before CT1.1. The Rmk's
  "replace with your checks/ script" parenthetical was realized as
  `verification/checks/verify_CT10_signature.py` and is cited in the Rmk.
* **§D symbol table:** the `S,T` and `η` rows updated; new rows for
  `(𝔬, η^(𝔬))` and `(ζ, D_ζ, sf)`.
* **Downstream Part 1:** CT1.1 Req/Pf/Phys, CT1.2 Req + four Pf justification
  lines, CT1.11a involution-table tag rows (1516/1517/1523), CT1.11b
  native-frames clause, L5 `η_aη_b → ϑ_aϑ_b` rename (the optional item,
  applied: no checker pinned the old symbol), §0.1/§0.2/P1/§G range rows
  (C1–C13; CT1.0–CT1.11b; "signature classification" added to the §G row).
* **Corpus-wide sweep** (representative citations of A3): Part 2 Dep line;
  Part 3 FT.156(1) declare-line, FT.156 Pf(1) row, FT.156 Phys, FT.158 cite;
  Part 4 Dep line, BM.9(2) boxed line, BM.19 Thm line, BM.152 Req; HistLog
  §III FT.156 row; corpus README layout rows. CT1.12 and all metric-side
  `sig(g) = (-,+,+,+)` citations derive the signature independently of A3's
  representative (D2.1/det<0 route) and needed no edit.
* **Option B not adopted:** CT1.0(5) proves the covariance characterization;
  the selection stands openly in C13 (the axiom surface stays minimal).

## R1b — The open-ledger retirement ("nuke everything marked OPEN")

Author ruling: the open-item apparatus (Open Gaps items 1–21, Q1–Q12, the
deficits) is Standard-Model-comparison-era residue; the base layer is
self-contained; what remains is application.

**Dependency finding (the requested notify check):** no requirement edge ever
resolved to a ledger item — `verify_corpus_graph.py` builds the graph from tag
tokens only and strips HistLog pointers before extraction; the 8012 edges are
tag→tag and acyclic with the pointers removed. The removals below therefore
break no derivation. Textual loci that still *reference* open items as content
are inventoried, not rewritten (see `OPEN_ITEMS_REPORT.md`):
BM.6 (the construction specification restating HistLog §II.3), Def-H.39's
β-slot locus rows, Census FT.84 (the deficit-table cell — a frozen Category-B
cell whose deliverable IS the ranked deficit register), the Part-5 requirement
ledgers inside the BM.143/BM.144 records (Addendum B), and Part 3 §0.2's
ledger-resolution rules (kept while residual mentions exist).

**Removed mechanically (283 pointers; `revision1_open_nuke_plan.json`):**

* bracketed citations whose segments are ledger-only: `[items 7/13; Q2]`,
  `[HistLog §II item 21(b)]`, `[\text{Open Gaps 7 diagnostic}]`, …;
* ledger segments inside mixed brackets (tag citations preserved):
  `[FT.131(3); HistLog §II item 21(b)] → [FT.131(3)]`;
* locator tails glued to kept citations: `[scope: FT.24/Open Gaps 13] →
  [scope: FT.24]`;
* bare parentheticals: `(Open Gaps 13)`, `(deficit 1')`, …;
* Req-line segments consisting only of ledger tokens (including comma-lists
  and `(HistLog §I)` locator tails on item tokens).

**Protected (never removed):** tag citations glued to locators (the FT.140
`(HistLog §IV)` pattern — load-bearing for citation closure), HistLog **§I**
declaration-record pointers (not open items), `[math]`/`[machine]`/`[EXT]`
justifications, P5/A-BM guard sentences ("requires a HistLog §I addendum
entry first"), the §D/§G charter rows describing the ledger's contents, and
all mathematical uses of "open" (open chain, open path, open geodesic, …).

**Integrity verified after removal:** per-line `$$` counts unchanged, table
pipe/ampersand cell counts unchanged, line counts unchanged, `check_format.py`
/ `verify_era_structure.py` / `verify_corpus_graph.py` green.

**Reported, not removed:** 452 residual lines carry open-status language as
clause content — 325 in blocks kept in the main corpus, 127 in blocks already
relocated to Addendum B (records, verbatim by policy). Full inventory:
`OPEN_ITEMS_REPORT.md`. These await an authorial ruling; removing them changes
what theorems *say* (e.g. verdict rows, "¬constructed here" clauses, the
FT.84 deficit register, the "named for Part 5" ledgers), which is content
surgery, not pointer cleanup.

## R1c — Checker-suite updates

* `check_format.py` / `verify_corpus_graph.py`: registration and citation
  regexes extended `C1[0-2] → C1[0-3]` (C13 declared exactly once, cited
  legally); `CT1.0` registers under the existing `CT\d+\.\d+` patterns.
* `verify_H_3p1_chiral_asymmetry.py` §E: the A3 literal pin
  (`\eta=(-,+,+,+)`) replaced by two pins — the revised A3 sign-structure
  display and the C13 representative declaration.
* Three pointer pins re-expressed against the revised canon (each now asserts
  the pointer is GONE and the clause substance remains):
  `verify_H_topo_blind_neutron.py` §G (item-13), `verify_H_noether.py` §F
  (Q10), `verify_H_neutron_decay_vertex.py` §D12 (item-19).
* Suite-count pins 79 → 80 in 12 checker files (`nverify + 1 == 80` and the
  message literals) and in both READMEs ("(80 checkers)", "**80/80**").
* **New checker** `verify_CT10_signature.py` (113 assertions, exact arithmetic
  only): §A document pins; §B exhaustive sign-vector enumeration (clause 1);
  §C sign-blindness and `T = D_ζ⊗D_ζ` (clause 2); §D the (7,3,3,3) census at
  every 𝔬 with [S,T]=0 (clause 3); §E `sf` identity at 𝔬=0, axis reflections,
  the exact rational unitary `U_c = ½(𝟙 − i(σ₁+σ₂+σ₃))` conjugacies, and the
  charpoly witnesses `(x+1)³ ≠ (x−1)²(x+1)` for non-conjugacy (clause 4);
  §F SU(2)-covariance as **polynomial identities over ℚ(i)[a,b,c,d]** on the
  generic unitary form plus the U_c commutation census proving the iff
  (clause 5); §G the Rmk's CT1.2 sector census at all four 𝔬.
* No checker's mathematical assertions were weakened; the computational uses
  of `η = (-1,1,1,1)` in the existing checkers are witnesses of the C13
  representative and stand unchanged.

## R1d — Records regenerated

* `canon/HistLog.md`: §V.31 appended (the revision record; §I–§IV untouched).
* `canon/Summary.md`: regenerated (10656 lines, 626 units — now carrying the
  C13 and CT1.0 statements).
* `canon/index/`: regenerated by the suite (623 tags; 8012 edges; topo 573).
* `canon/README.md`: C1–C13 / CT1.0–CT1.11b ranges, "(80 checkers)".
* Publications rebuilt from the revised canon: `docs/Qubitick_Corpus.pdf`
  (CT1.0 = Theorem 1.15, C13 = Convention 1.13, index rows consistent),
  `docs/Addendum_Refutations.pdf`, `docs/Calibration_Policy.pdf`.

## R1e — The deficit ruling (second authorial instruction)

"The final corpus should not have any doubts of a structural absence. The text
should reflect the true state of completion." Applied in three layers:

* **Registers relocated (publication layer):** Census FT.84 (the ranked deficit
  table and two-ceiling synthesis) and Part 3 FT.125 (the deficit ledger:
  deficit 1 closed at the projector level, deficit 1' opened) join Addendum
  B.4 as full records; their cited clauses (FT.84(2), FT.125(4), FT.125(5))
  remain resolvable by tag from every Req line.
* **Curated completion-language rewrites (canon layer, 39 asserted exact-string
  edits + 6 repeated clause heads):** the boxed Yukawa ruling now reads
  "is application-layer content — ¬a structural absence of the base layer";
  "the relating equation stays open" → "is application-layer content";
  "deficit 11 (spin–statistics) is CLOSED: the connection is derived…" →
  "the spin–statistics connection is DERIVED…"; "deficit 10 is closed" →
  "the multi-chain charge read is derived"; BM.6's heading drops "open";
  BM.6's resolvent row now cites its construction (BM.134/Def-BM.20);
  "open:" clause heads → "beyond this tier:"; "the open items (named, priced,
  unfilled)" → "the residue register (named, priced; dispositioned in full at
  BM.143)"; deficit-register appositives across FT.88–FT.157, BM.17–BM.142
  and Census FT.96 replaced by their subject matter ("the chirality
  assignment", "the ternary read", "application-layer content") with the
  underlying citations ([FT.125(4)], [FT.145(3)], …) preserved.
* **Checker pins mirrored (4):** verify_H_antimatter_resonance_spectrum §G7
  closure box, verify_H_bm_closing_tier (deficit-10 closure),
  verify_H_six_objective_resolution (statistics box),
  verify_H_kinetic_energy_metric §C9 (Yukawa row).

**Deliberately preserved** (completion facts, not doubts): proven no-gos and
bars (¬derived/¬formed statements with their proofs — these assert what the
corpus proves, including impossibilities), calibration-slot status lines
(declared, value ¬issued — policy, per the Calibration Policy document), the
physical deficit vocabulary (entropy deficit, ledger deficit, deficit
currencies, arithmetic deficits such as 25−18=7), the addendum-bound
adjudication records (verbatim history), and HistLog §II itself (the archived
ledger). Tier section names that are historical labels (e.g. "Tier BM.3 —
Consumption and Open Constructions") were left untouched: renaming ## headings
ripples through pinned tier references; flagged for an authorial ruling.

**Residual after this pass:** 395 lines still carry ledger/doubt vocabulary —
260 in main-corpus blocks (mostly bare "item 7"/"item 13" prose pointers
inside long scope clauses and the P4 §0.1 charter map), 135 inside
addendum-bound records (verbatim by policy). Inventory with owners and quotes:
`OPEN_ITEMS_REPORT.md` (machine-readable twin: `revision1_open_items.json`).
These are sentence-level rewrites of verified theorem text; each needs a
truth-preserving completion phrasing, so they await the next ruling batch
rather than silent automation.

**Suite state after R1e: 80/80 green** (run in four batches of 20).

## R1f — The item-closure ruling (third authorial instruction)

"Close all the item 7 and item 13 style deficits/mentions... The main corpus
is the mathematical model... the reader must not get confused by them."
Applied as the completion of R1e:

* **Uniform policy:** the pointer retirement and completion-language rewrites
  apply to the whole published canon — both the main-corpus blocks and the
  addendum-bound records (the exploration pathway reads clean too). The
  byte-exact pre-revision corpus, with the full ledger language, is preserved
  in `working_markdowns/`; the archival HistLog keeps §II as the historical
  register.
* **Mechanical passes:** ~290 ledger pointers (bracketed locators, Req
  segments, parentheticals, glued locator tails), 21 inventory-taking
  sentences removed from prose, 30+ curated clause rewrites ("remains an open
  gap" → "is application-layer content — ¬a structural absence of the base
  layer"; "open:" clause heads → "beyond this tier:"; the BM.90-family
  "open items (named, priced, unfilled)" heads → "boundary inventory (every
  row dispositioned at BM.143)"; the item-17/19 closure boxes now name their
  constructions; BM.6 retitled "The construction interfaces"; BM.139 retitled
  off "the closure of item 16"; FT.125's deficit ledger relocated to Addendum
  B.4; Part 3 §0.2(i) restated as the retirement rule).
* **Structural labels preserved:** the (P5.1)–(P5.10) Part-5 requirement-row
  labels of BM.143 (one over-eager rewrite restored from the archive), the
  CT1.12a route classes (R1)–(R3), and all physical "deficit" vocabulary
  (entropy/ledger deficit, deficit currencies, 25−18=7).
* **Checker pins mirrored (7 total this revision):** item-17/item-19 closure
  boxes, the Yukawa row, the statistics box, the charge-read closure, the
  deficit-11 box, the item-13/Q10/item-19 pointers.
* Suite state after R1f: **80/80 green** (two halves of 40). Summary of
  Record and index regenerated; publications rebuilt.

## R1g — The residual closure batch ("run the cycle")

The stubborn tail of the item/deficit mentions, closed:

* 36 curated regex rewrites (surgery3) + 24 mechanical pointer removals:
  the BM.45 register rows relabelled to their subject matter under the head
  "the application-layer boundary rows"; the "category item 7 bars" family →
  "a category the corpus bars"; the "item 7 stands" family → "the mass-form
  bridge is application-layer"; the Q10/item-16/item-17 closure boxes →
  their constructions ("the additive multi-chain charge read…", "both
  conventions are declared", "the resolvent specification is discharged by
  BM.134"); "item 7's relating equation is derived" → "the relating equation
  is derived"; the (R9) residue in BM.123 named as the cross-section
  residue; Census FT.44/FT.76 gap references rewritten to their subject
  matter.
* surgery4/5: the last "item 7 stands/composition stands open" rows, the
  Def-BM.11 scale-data row (→ P4-class calibration), BM.51's "relation … is
  open" (→ ¬derived), BM.74's "rung datum is open" (→ not fixed here),
  Def-H.9/Def-H.43/FT.145/FT.155 locus phrases (→ application-layer
  content / dropped), BM.97's "conversion item 7 bars".
* Final token scan: **zero ledger tokens remain in KEPT blocks** except one
  physical false positive (FT.107's entropy "leading deficits $2|δρ|²$").
  Deliberate keeps: the §G archival-map row describing HistLog's contents,
  the Part 3 §0.2 retirement rule (which names the retired tokens), and the
  Part 2/3 route classes (R1)–(R3) (discreteness routes, not residues).
* 6 further checker pins mirrored (flicker_integral_restmass, bm_closing_tier
  ×2, six_objective_resolution ×2, and the earlier closure boxes).
* Suite after R1g: **80/80 green** (all checkers executed against the final
  canon). Summary of Record and index regenerated; all three PDFs rebuilt.

## R1h — De-historicization of the main corpus (fourth authorial instruction)

"Remove history from the main corpus... The main corpus is the mathematical
model... the reader must not get confused." The KEPT canon (Parts 1–4,
Census, front matter) now speaks synchronically — the model as it stands,
not how it became:

* **Front matter:** Part 1 §0.1/§0.2 no longer name the archival ledger (the
  Census is the sole annex of the citation surface); the §0.2a extra-axiomatic
  clause reads "are derived theorems of Part 4"; the axiom-provenance and
  former-registry sentences are gone; the §G archival-map row is removed.
  Part 3 §0.2 is restated as synchronous resolution rules ("This canon carries
  no ledger citations..."; scope tokens Comm-min/Eff described without
  first-edition framing). Part 4's Dep/DAG/charter rows drop the ledger
  annex, the (R5)/(R2)/(R10)/(R4') house-cleaning narration and the
  "reclassification" wording for CT2.6(ii)–(iii) (now "the derivation of").
* **Policy lines:** "requires a HistLog §I addendum entry" → "requires a
  logged declaration" (8 sites); "logged as HistLog §I/§II.4 addendum" →
  "declared"; A-BM declaration references stand on their own tokens.
* **Precedence without temporal narration:** FT.158's supersession clause →
  "the classification of the rational 2/3" with "are superseded" → "do not
  stand"; FT.93(8) "corrected on the record" → "The inventory gloss.";
  FT.66(6) folds, Def-H.24, FT.55, FT.91, Def-H.32, BM.28, BM.151
  ("one is retired" removed; "reclassification" → "derivation", title
  included), Census FT.42/FT.45/FT.120 retracted-epithet lines — all
  restated as what stands now.
* **Kept (synchronous vocabularies, by design):** ledger-word "history"
  (admissible/completed/reversed histories are mathematical objects, FT.144
  family), FT.20/FT.61/FT.66-style "reclassification" (a theorem act on
  structural aspects), grammatical "former", "frozen"/"re-verified"/"re-cited"
  (verification vocabulary).
* **Publication layer:** the monograph's preface no longer narrates the
  revision (a neutral "Citations and records" note replaces it); the
  title-page revision row is removed. The revision's own record lives here,
  in HistLog §V.31 (archival ledger), and in the archive itself.
* **Checker pins:** 8 further pins mirrored (continuum-limit §G7/§G8 ×3,
  topo-blind Def-BM.6 fragment, bm-closing box pins ×2, kinetic §C9, plus the
  earlier closure boxes); one over-eager mirror into a MOVED-block pin
  (BM.143) was reverted. Suite state after R1h: **80/80 green**.

## R1i — The mass-nomenclature reconciliation (fifth authorial instruction)

"Definition 3.11, mass read and other 'ambiguities'... The 'mass' that works
is the Lyapunov contraction mass... things are 'priced'... Clean these up."

* **Definition 3.11 = Def-H.39 (the mass-read registry; bridge slots).** Its
  read (3) — the inertial/tilt read $m_i^2(q)=\Delta S(q)$ — is named **the
  Lyapunov-contraction read** (the deficit accumulated under the L1 contraction
  law). A **nomenclature rule** joins the definition: every occurrence of
  *mass* names one registry read at the species declared at its locus; no
  unqualified *mass* crosses species; a computed variant value is a *price* —
  an exact named functional of the declaring data — and ¬a mass read. This is
  the single disambiguation point for the corpus's "priced, ¬adopted"
  vocabulary (route values, convention variants, class masses), which is
  defined terminology and stands.
* **The ruling, recorded where the identifications live (BM.97 Rmk):** the
  operative mass of the baryomesonic era — the read entering every formed
  composite quantity (rest masses, Q-values, splittings, thresholds, lapse) —
  is the Lyapunov-contraction mass, composite form $m_{rest}=\Delta S_{L}/h$
  [BM.35], foundation [BM.51]; the informational read agrees as a formed
  equation [BM.35], ¬a currency fusion; the pole read is the rest mass on the
  transport species at leading order [BM.97(1)]; sector routes are measure
  functionals (prices, ¬masses) [BM.30; BM.37]; Ansatz-B class masses remain
  non-adopted templates [Def-H.28]; numeric bridges (β-coefficients, ρ_B) are
  calibration slots, values ¬issued [§Cal-BM (C-BM.1); P5]. All citations
  respect the era chain (no Part-3 forward citations of Part-4 results).
* **BM.51:** the "deficit species" now carries its registry qualification
  [Def-H.39(3)] at the ¬derived-relation remark.
* **Ledger:** HistLog §V.32 records the reconciliation. No mathematical clause
  was altered — the ruling fixes which derived read is operative and fixes the
  vocabulary. All other terminology clashes remain governed by the Part 1 §D
  master symbol table and conventions C1–C13 (e.g. C4 ϰ≠κ, C5 Σ, C6 E_tr/E_bd,
  C8 Z).
* Suite: structural trio green; the eight touched-tier content checkers green
  (verify_H, em_self_interaction, kinetic_energy_metric, gravmass,
  flicker_integral_restmass, full_scope_mass_splitting,
  chiral_assignment_opening, 3p1_chiral_asymmetry); publications rebuilt.
