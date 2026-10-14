# TRANSLATION_LAYER.md — the session-13r working record (Tier IT.22, tags IT.71–IT.77)

**Directive (the Architect, session 13r):** verify the hypothesis that *the rung-1 forces
(G, W, H, D⁺) are the translation layer between the discrete ledger (pre-dim) and the emergent
continuous geometry (dim)*, in four claims — and *"Do not accept the hypothesis by fiat — prove or
disprove each component."* With the note: *"the run 1 forces literally cannot reach beyond 1 hop
and this sort of looks like SM Weak boson ranges, just in my corpus it simultaneous mediates the
entire S sector. This SM framing is for your clarification of my thoughts, this doesn't enter the
corpus."*

**State verified first (the handoff's crash-recovery rule):** the sandbox booted EMPTY (only
`uploads/` survived); everything re-cloned with the delivered PAT, origin URLs scrubbed, git
identity re-set, remote state checked through the GitHub API before any conclusion. Found:
`origin/master = 576a0e4`, `era2 = 215ddbb`, **PR #13 STILL OPEN** — the directive said "prior
pull requests merged", the API says otherwise; the rows win, so this batch was built on `215ddbb`
and pushes to `era2`, joining PR #13 (recorded, not assumed). Builder channels polled: comms
`0008` (the builder's 1540-sector draw, re-struck on IT.69's closure — 1540 DERIVED / 0 UNDERIVED
pairwise, cross-certified against `opened_paths.py`), zero open issues on the lean repo, the board
thread at `qubitick_papers#1`.

---

## 1. The premise audit (six corrections — IT.71(4))

| # | the directive's premise | the frozen row | the adjudication |
|---|---|---|---|
| P1 | "BM.34(2): the shift functional g₀ᵢ = ϰβΩ²wᵢ" | BM.34(1) gives Nᵢ = Ω²ϰβwᵢ; BM.34(3) gives gᵢⱼNʲ = Nᵢ = g₀ᵢ; FT.157(1) is the block identity. BM.34(2) carries the line element + the flat vacuum | **CORRECTED** — the citation slip is recorded, never applied to a row [AT.63(2)] |
| P2 | "the shift Wᵢ is T-odd" (as if distinctive) | CT1.1/CT1.2: T-odd = 6 = {Wᵢ} ∪ {Kᵢ}; T-even = 10 | **SHARPENED** — true but not distinctive; the distinctive row is FT.156(2)'s 7/3 split *of the S-even block* |
| P3 | "they ARE the dimensions" | IT.52(3)'s four prices + IT.54(1)'s "the metric identification (10:10) — ¬ADOPTED" | **SPLIT** — the coordinate reading is derived; the identity reading is already ¬adopted and priced |
| P4 | "phase / winding / delta" | three distinct objects in the record | **DISAMBIGUATED** — δh the hop count [D0.6; D-RS3], the δ-seal/digon [IT.69], Δ the ledger increment [CT0.3; D1.5] |
| P5 | "propagate through channels" | "channel" has three frozen senses | **LOCATED** — the pair channel [A2; CT0.6; CT0.12] is the one that matters; D1.10 is the frozen force clause that uses the word |
| P6 | "pre-dim / dim" | IT.64(5)(c)/(8)(P6): builder-side vocabulary, flagged ¬adopted | **FLAGGED** — the corpus loci are the tick face [D0.7; C11; IT.53(4)] and the emergent chart projection [IT.56(2)]; the adjective "pre-dimensional" IS canon-attested [Def-H.8 Rmk] |

The SM framing: recorded as clarification of intent, ¬adopted, ¬a premise, with the bars quoted
rather than paraphrased (FT.157 Rmk, FT.158(5), P1/P5, the [EXT] quarantine). It never reaches a
derived clause.

## 2. The canon rows the four claims actually rest on

Found by grep and read in full before any machine work — the tier cites, never re-derives:

- **FT.141(1),(5)** — the 10/6 grading census; "the seal reads (J±) are S-odd with 0 metric
  coordinates"; tr Ad(𝕊) = 4, rank 16, ker = 0.
- **CT1.2** — the generator table: (S,T) = (+,+) for E₀, Σ, Ê^{ij}(5); (+,−) for Wᵢ(3); (−,+) for
  Jᵢ(3); (−,−) for Kᵢ(3). **CT1.1** — the (7,3,3,3) block dims; T = −1 exactly on the mixed index
  pairs (0,i),(i,0) — *T is the η-sign grading, not a time-reversal operator*.
- **CT0.12** — the aspect↔block table (F_G = span{Ê^{ij}} 5, F_W = ℰ_{+-} 3, F_H = span{Σ} 1,
  F_{D⁺} = span{E₀} 1, F_{J±} = span{Jᵢ}/span{Kᵢ} 3+3; total 16 = C_cap).
- **CT1.12 + CT1.12a(2)** — the metric dictionary (a₀₀, Σ_tr, ĥᵢⱼ, wᵢ) → (Ω, volume, shear,
  shift), counts 1+1+5+3 = 10 = #{g_μν = g_νμ}, "the dictionary is a bijection"; every carrier
  S-even; the S-odd blocks carry **zero** metric coordinates; g_μν orientation-even.
- **FT.30** — the block-wise dictionary + the independent-quanta audit + the **Verdict**: "No
  pair-channel block carries a block-local quantum: the geometric quantum is a *joint* S-even read
  — dŝ²(e) mixes all ten metric coordinates across G,H,D⁺,W"; and the **Rmk (the emergence chain,
  assembled)** — the six cited steps from per-edge S-even data to particles-as-poles.
- **FT.156(2),(3),(4),(5)** — the 7/3 T-split as the dictionary's (1;6;3) component split; the
  reversal transport ḡ(a₀₀,q,−w) = JḡJ; the inner spatial reversals; "time is asymmetric and
  strictly forward". **FT.157(1),(3),(5)** — the weak block IS the shift block; the weak support is
  the S-even T-odd block; space reversible, time strictly forward [A6: ¬∃τ⁻¹].
- **FT.159(1),(3),(4),(5)** — x⁰ := τₙ; Θ_𝔏 = T; "the line-element channel CONTRACTS metric data
  with tick data"; the locus discipline (one order parameter, four tags, ¬an operator equality).
- **CT2.6 + Pf + Rmk** — the bridge theorem; charts x⁰ = τₙ, **xⁱ = hop counters projected on the
  3 shift directions (Wᵢ sector)**; smoothness from "coefficients = local ledger averages; D1.9:
  updates local, finite".
- **CT1.18 + Rmk + Phys** — the linearized spin-2 operator, the TT-gauge wave equation, the
  projected-gauge correction, "the graviton of the corpus is the ℰ₊₊ quintet … propagating on the
  auxiliary background". **CT1.17** — the exact conformal law in Υ = ln Ω. **CT1.10** — Ê^{ij} = 5
  (spin 2).
- **A6, A7, D0.7, D1.9, CT0.3, C11** — the tick as a ledger event; ¬∃τ⁻¹; the monotone record; tick
  locality with **¬∃ a read at edge-distance > 1**; the (±1,±1,±1) seal clock; the node lifecycle.
- **D1.6, D1.7, D3.5, EM.20(1),(4), CT0.9** — ds²(e) = g_μν(e)Δx^μΔx^ν; Θ, Φ, Hol_spiral;
  **G(e) = σ_e·exp(iα_e dŝ²(e))**; α_e ∈ {0,π}; σ_e ∈ {±1}. **CT1.19b(1)–(4)** — Θ_𝒫 ∈ 2ℤ on
  materialized closed chains, the orientation evenness, the geometry quantum κ ∈ ℤ at m = 2,
  ds² = 4κG_N ln2, the partial-sum free parity. **CT1.19a/Def-H.18** — off shell nothing is
  quantized; the two-locus principle.
- **AT.5(1)–(5)** (Level 5) — the inverse translation: (w·Δx)(e) = [𝔥²κ_e/Ω² + (Δx⁰)² −
  M_ijΔxⁱΔxʲ]/(2ϰβΔx⁰), linear in the ledger integer; the longitudinal part DERIVED, the 2
  transverse dims per edge GAUGE because **Nᵢ is the Lagrange multiplier of the momentum
  constraint**; the codimension-1 vanishing locus.
- **FT.20** — the per-aspect observability criteria (G via the mass read; W one-directional via
  Θ_int; H folded into G; D⁺ never independently; J± never).
- **FT.144(2),(4)** — strict alternation, the prefix law, no backward materialization, Θ_𝔏 the
  formal mirror; the two-pair interleaving witnesses 2, 8, 32.
- **IT.52(3), IT.53(4)–(8), IT.65, IT.66(1),(2),(4), IT.68** — the four prices; the radar faces;
  D-RS3 and D-RS6 issued; the transit bar on three grounds; the formed o-lifted read family.

## 3. The machine work (`translation_layer.py`, 40/40 exact)

| § | what it does | the load-bearing rows |
|---|---|---|
| A | rebuilds the 16 CT1.2 generators as exact 4×4 Gauss(i) matrices from the Pauli tensors; rank 16 with the drop-one adversarial; the Ad(𝕊) census (10/6, tr 4, rank 16); the T-grading through the exact Pauli-tensor decomposition with the wrong-signature adversarial; the refined T-odd census; the three-way activation census | A1–A5 |
| B | the dictionary counts and block-wise decomposition; the bijection cell by cell (**9 linear + 1 exponential**); the ADM/Schur layer on three rational witnesses incl. the inverse-metric rows certified by g^{μα}g_{αν} = δ^μ_ν; the flat vacuum + exact rational LDL^T inertia → sig = (−,+,+,+); the zero-coordinate row with the fake-carrier adversarial; the ¬adoption discipline census | B1–B6 |
| C | the 1024-history tick census; the seal clock + the arrow combinatorics with the **new closed form 2^(2n−1)**; the tick-locality census on 66 vertex-instances (62 non-vacuous, 4 saturating); the pair-channel support rows; **the formal jet algebra**: two independent routes to G⁽¹⁾ agreeing coefficient-wise, the T/V structure identity, gauge invariance (all ξ-terms cancelling), CT1.18's Rmk correction re-certified exactly, and **the ∂₀² census → 4 constraint cells / 6 wave cells**, robust under the flipped signature; the locality-to-continuum text census; the O1 chiral-blindness commutator re-run | C1–C8 |
| D | the 16-cell transport identity ḡ(a₀₀,q,−w) = JḡJ; the carrier T-parity with the **exact adjugate identity det γ·(N²−Ω²) = Ω⁸ϰ²β²(wᵀadj(M)w)** proving N² even in w; the 8-point inertia lattice; **the line-element T-evenness** (10 increment monomials, 13 sector monomials, the parity products, two substitution identities); the radar-leg flip on the frozen witness; the 9 + 27 + 3 inner-reversal rows against ¬∃τ⁻¹; the naming bar census | D1–D7 |
| E | the ten exact partial derivatives (all coordinates enter) + the per-block non-integer witnesses (no block-local quantum); the 22620-chain product census of G(e); the on-shell parity/κ censuses with the symbolic 4κ Laurent coefficients; AT.5(1)'s round-trip + linearity + nullity 2 + the vanishing locus; **the which-side-quantizes witness pair** (off shell −3/4 ∉ ℤ); the observability census; the 160-cell radar re-run | E1–E6 |
| F | the 1-reach support census; the 2⁴ sub-collection census (max proper 9 < 10, covering set unique); the chain/trivial-chain/coarse-graining separation; the SM-flag bar census | F1–F4 |
| G | the 26-component verdict table traced to its markers; the tier-document bar scan (P5 decimals with a live-witness self-test, P1 frozen-symbol census over the boxed statements, the amplitude alphabet, the negated-line census with the frozen compounds stripped, the species paragraph scan); the declaration census; the tier anatomy + era chain + the gate re-run in-process | G1–G4 |

**Non-vacuity (mutation audit, run before the tier text was written).** Six deliberate
perturbations — the interleaving closed form 2^(2n−1) ↦ 2^(2n), the constraint-cell list, the radar
half-distance, the covering sub-collection bound 9 ↦ 8, the shift-monomial count 3 ↦ 4, the
joint-read derivative census — each turned exactly its own marker RED (39/40 or 38/40), and where
the component feeds the verdict table, G1 too. A seventh perturbation (flipping the jet algebra's
signature representative to (+,+,+,−)) did **not** break the ∂₀² census, which is itself a result:
the constraint/wave split is a structural consequence of gauge invariance, not an artifact of C13's
mostly-plus choice. It is now carried in the checker as an explicit adversarial (C6) and in the
tier at IT.73(4).

**Two self-caught bugs during the build (recorded per the session-12 scar discipline):** σ₃ was
first written with −i in its lower slot instead of −1 (caught by the A2 swap census before any tier
text); and the Christoffel route first summed η^{λρ} over ρ instead of collapsing to ρ = λ (caught
by the two-route disagreement, which is exactly what the second route is for). The edge-distance
metric in the locality census was also wrong on the first pass — line-graph distance is not D1.9's
notion; the correct one is 1 + the vertex distance to the edge's nearer endpoint, and with it the
domain is exactly the distance-1 set on all 66 instances.

## 4. The verdicts (IT.77(1), 26 components)

**CLAIM 1 — DERIVED as a dictionary; the identity reading stays ¬adopted.** All four blocks carry
metric coordinates (5+3+1+1 = 10 = #{g_μν = g_νμ}), the seals carry zero, the dictionary is a
bijection — but 9 cells linear and one exponential, which is IT.52(3)(i)'s price. "They ARE the
dimensions" is the identification IT.52(3)/IT.54(1) already refused with four prices; adopting it
is the Architect's act. **No candidate act was minted and nothing was forced** — the existing
¬adoption row is the register locus.

**CLAIM 2 — SPLIT.** "Not ticks" DERIVED (the tick is a Haar draw and a record update with no
inverse and no metric content; the metric enters as Δx⁰). "Geometric" DERIVED. "Geometric
propagators" DERIVED **for the G quintet only**: the ∂₀² census shows the lapse cell and the three
shift cells are constraint cells — AT.5(4)'s Lagrange-multiplier row re-derived from the operator
side — and CT1.18's own gauge (Υ = Nᵢ = Σ_tr = 0) switches off D⁺, W and H. For those three: a
**scoped absence, ¬a no-go** (W transports [BM.34(3),(4)], H enters ḡ_ij, D⁺ gravitates through
CT1.17's closed-form conformal law). The residue **consolidates under D-PJ7's P4 transport
profile** — no new open row. The dynamical mediation reading stays **BARRED** on three grounds
(O1 re-run by machine).

**CLAIM 3 — SPLIT, with one naming barred.** T(Wᵢ) = −Wᵢ DERIVED, and it transports exactly to
the time-reversal pullback (g₀₀, g_ij fixed; g₀ᵢ flipped; the signature invariant). Precision:
6 of 16 generators are T-odd (W **and** K), so the distinctive statement is "the unique T-odd
sub-block *of the metric sector*" = FT.156(2)'s 7/3 split. **New row:** the interval is T-EVEN
monomial by monomial (g₀ᵢ T-odd × Δx⁰ T-odd = T-even), so the shift's T-oddness does not make the
geometry T-odd; the flip is an involution. What the shift genuinely discriminates is the two radar
legs (s ↦ −s swaps dτ₊ ↔ dτ₋). "Distinguishes past from future" is therefore DERIVED **only in
the formal/read sense**: the arrow's locus is ¬∃τ⁻¹ [A6] + no backward materialization
[FT.144(2),(3)] + the monotone record [A7], and Θ_𝔏 is the formal mirror, ¬a dynamical inverse
[FT.159(3)'s locus discipline]. **"Encodes left/right" is BARRED as a naming** [FT.156 Rmk;
FT.157 Rmk; FT.101 Phys]. Bonus derived row: the two-pair completed interleavings number
**2^(2n−1)** (the frozen witnesses 2, 8, 32 re-derived by brute force; 2n = 8 → 128).

**CLAIM 4 — DERIVED as a joint capability; BARRED per block; DECLARED-and-formed as a read;
BARRED as dynamics.** The frozen formula of the translation is G(e) = σ_e·exp(iα_e dŝ²(e))
[D3.5; EM.20(4)] — one ledger bit times one geometric phase, edge-local, multiplied over edges
[A8]. All ten metric coordinates enter the interval (exact partial-derivative census) and no block
alone quantizes anything (per-block non-integer witnesses) — FT.30's Verdict, machine-certified.
On shell Θ_𝒫 ∈ 2ℤ and κ ∈ ℤ at m = 2, with ds² = 4κG_N ln2 kept symbolic [P5]. **The read runs
backwards**: AT.5(1)'s closed form is exact, round-trips into D1.6, and is linear in the ledger
integer, with 2 gauge dimensions per edge left over by design. **Which side quantizes (new row):**
the geometry supplies the quadratic form, the LEDGER supplies the discreteness (α_e ∈ {0,π} plus
the pole condition), and the integers are their on-shell contraction — off shell the flat-vacuum
witness gives −3/4 ∉ ℤ [Def-H.18's two-locus principle]. The operational radar read needed no new
act: D-RS6/D-RS3 are issued and IT.68 formed the family (the 32×5 census re-run here, 160/160
integral); D-RS4 stays deferred.

**THE NOTE — DERIVED as a theorem (IT.76).** *Reach = 1 hop* exactly: the pair-channel support
[A1; A2; CT0.12], the per-edge metric g_μν(e) [D1.6], and D1.9's distance bar — non-vacuous on 62
of 66 census instances. *Content = the entire S sector, minimally*: 5+3+1+1 = 10, and the
exhaustive 2⁴ sub-collection census shows the largest proper sub-collection reaches 9 and exactly
one sub-collection covers the ten. *The separation*: multi-hop reach is a CHAIN property [D1.4;
D1.5; EM.5's trivial chains with Θ = 0, Hol = 1] bounded per channel by δh ≤ 4δτ [Cor CT0.6a], and
the continuum is a COARSE-GRAINING property [CT2.6(ii)] — never a force range. *The two sides of
the layer*: the S-odd six PRODUCE the ledger events (the seals, the (1,1,1) clock, ¬observable),
the S-even ten TRANSLATE them (the dictionary, the chart, the contraction, the on-shell integers).

## 5. What the hypothesis looks like in corpus vocabulary

The Architect's "translation layer" is the record's own triad, and the tier cites it rather than
renaming it: **the dictionary** [D2.1; CT1.12; FT.30] · **the bridge theorem** [CT2.6: "it converts
combinatorics (edges, ticks, counters) into the differential geometry"] · **the contraction**
[D1.6; D1.7; D3.5]. Its sharpest single line is CT2.6's chart row — x⁰ = τₙ from the ticks, xⁱ =
**hop counters projected on the 3 shift directions (Wᵢ sector)** — with D1.9's 1-hop locality cited
*inside* the bridge theorem's smoothness step. So the hypothesis is right about the mechanism and
needs only the discipline: the layer is a dictionary, its 1-hop reach is an input to the continuum
rather than a limit on it, one of its four blocks is a wave and three are constraints, and its
measurements are joint and on-shell.

## 6. Status rows

- **No declaration issued** (machine-scanned, IT.77(3)); §Cal-IT unchanged and value-free.
- **No new open row.** IT-O1/IT-O2/IT-O5 unchanged; IT-O3/IT-O6 stay closed. The one named residue
  (a formed propagator role for W, H, D⁺) consolidates under D-PJ7 [IT.41(2); IT.66(4)].
- **Bars:** P1 honored (the boxed statements' dimensionful tokens are a subset of the frozen
  symbol list; nothing valued); P5 honored (zero decimals, self-tested scanner); the transit bar
  stands on three grounds; count→strength barred; no species identified; the arenas untouched; the
  incommensurability bar holds; the frozen canon cited, never edited.
- **Machines:** `translation_layer.py` 40/40 · `run_all_level6.py` **23 checkers / 390 markers /
  0 failures** · `check_level6_format.py` **22 documents PASS** (77 IT-blocks, every citation
  attested) · era-1 untouched (no file under `era1/` modified in this batch).
