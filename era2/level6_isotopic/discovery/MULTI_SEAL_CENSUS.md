# MULTI_SEAL_CENSUS — session 11 discovery record (Level 6 / Era 2, the Isotopic era)

> **Directive (Architect):** *"Run the Multi-Seal Configuration Census for N=5 and N=6 — The
> Channel Width Skeleton and the D⁻ Saturation Boundary … determine if the census terminates or
> encompasses D⁻ pure saturated areas … I think this does IT-O4 and IT-O2 simultaneously."*
>
> **Result: the census is run, exactly — and it corrects the question on two counts before
> answering it.** `multi_seal_census.py` **9/9 exact** (the IT.2 grammar engine reused verbatim
> per the directive). Candidate tags IT.9–IT.11 (Tier IT.3). The channel-width skeleton is
> binomial and exact (W₅ sums to 1024 over 11 classes, W₆ to 4096 over 13); N=5 is forced-mixed
> by arithmetic (2a+3b=5 has the unique solution (1,1)); the subnetwork mask bound 18 is
> **attained** by exactly these sealed EM-active composites; and the D⁻ "saturation boundary"
> dissolves under the two-mask-species distinction — the sink is one-dimensional at every rung,
> never a summand of any subnetwork mask, and the census terminates in the structural
> censorship of CT4.2/BM.143(1), not in any singularity. **IT-O2 closes on its census side;
> IT-O4 stays open, sharpened.** Declarations: none. P5 untouched; the collapse analogy is
> flagged as framing.

---

## I. The premise audit (three corrections, logged at IT.11(2))

| directive premise | the frozen rows | disposition |
|---|---|---|
| "the D⁻ scalar sink is formally active (adding exactly 1 dimension to reach dim 𝒦_{n≥4}=26)" | **FT.26(3)'s own Pf**: 𝒜(Σ;C) ⊆ {EM,G,H,W,strong} — "J±, D± never" [FT.20 table+Rmk]; dim 𝒦_Σ ≤ 1+5+1+3+8 = **18**; the 26-dim mask 𝒦_{n≥4} is a RUNG mask [D2.3] existing only at the inadmissible rung (2⁵=32>16 [CT0.5/6; AT.50(3),(4)]) | **CORRECTED (P1)**: two mask species conflated — the IT.1(6) "13 vs 26" currency lesson repeating. D⁻ is present in these composites as PLACEMENT (junction vertices D⁻-configured [Census FT.35(4); CT4.1]), never as an active summand; masked at every accessible rung [CT4.2] |
| "accessible vertex sets remain strictly bounded by C_cap = 16" | C_cap=16 bounds the PAIR channel [CT0.12 Rmk]; per-vertex D_tick(3)=16 exactly saturated (admissible), D_tick(4)=32 inadmissible; subnetwork mask bound = 18 [FT.26(3)] | **REFINED (P2)**: three spaces, three bounds — pair channel 16, vertex tick ≤16, Σ-mask ≤18 (attained) |
| "this does IT-O4 and IT-O2 simultaneously" | the grammar census names support DECOMPOSITIONS (N=5: 1+1 uniquely; N=6: 3+0 or 0+2); connectors between supports have no frozen species [IT.7(1),(4); BM.2(2)/(R10) pattern] | **ADJUDICATED (P3)**: IT-O2 closes on its CENSUS side at N=5,6 (amplitude side = residue); **IT-O4 untouched — sharpened, open** |

## II. The channel width skeleton (machine §A)

W_N(Q) = [z^Q](2+z+z⁻¹)^N = C(2N, Q+N) — Laurent convolution matched to the binomial entrywise
at N=2,3,5,6; frozen rows reproduce exactly (W₂=(1,4,6,4,1) [BM.135(3)]; W₃=(1,6,15,20,15,6,1),
Σ=64=4³ [BM.135(2); AT.41(2)]):

- **W₅ = (1,10,45,120,210,252,210,120,45,10,1)** — Σ = 4⁵ = 1024, 11 charge classes, peak 252 at Q=0.
- **W₆ = (1,12,66,220,495,792,924,792,495,220,66,12,1)** — Σ = 4⁶ = 4096, 13 classes, peak 924.
- **Cross-N census** [BM.31(3)'s pattern extended]: W₅(Q) ≠ W₆(Q) on the WHOLE overlap |Q|≤5
  (also W₃ vs W₅, W₃ vs W₆): where charge classes coincide, the probability spaces differ —
  the width skeleton separates supports the charge alone cannot. |Q|=6 is W₆-exclusive.
- Read domain: Q defined only on sealed supports (𝒞=1 [BM.135(1); D2.14; FT.19]) — every
  grammar grouping is total, hence sealed.

## III. The grammar census at N=5,6 (machine §B)

Triple-certified (enumeration ∧ recurrence ∧ closed form — the IT.2 engine, reused verbatim):

- **N=5: g(5) = 10, ALL of block type (a,b)=(1,1)** — one δ-pair + one ε-triple. The directive's
  "genuinely mixed, highly strained" is arithmetic: **2a+3b=5 has the UNIQUE nonneg solution
  (1,1) ⟹ g_ε(5)=0 is forced** — no pure-baryon (4ℤ) sector exists at N=5; the statistics
  composition is 100% mixed-class.
- **N=6: g(6) = 25 = 15 (3δ) + 10 (2ε)** — the frozen 3/5–2/5 mix [BM.31(2)] re-derived exactly.
- **The protection periodicity: g_ε(N)>0 ⟺ 3|N, verified for EVERY N=2..18** — the pure-baryon
  sector vanishes at N=4,5 (δ shares 1, 1) and RETURNS at every multiple of 3 (2/5 at N=6, 2/11
  at N=9, 40/427 at N=12): protection periodic, erosion within it monotone [IT.7(3)].
- Sequence context: N=4 all-δ (3 perfect matchings [IT.6(5)]); N=5 forced-mixed; N=6 restores
  the pure option.

## IV. Masks, placement, and the D⁻ status (machine §C)

- **Rung masks** [D2.3; CT0.12/14; AT.50(1)]: dim 𝒦_n = 6,16,17,25 (n=0..3); **26 only at the
  formal n≥4**; the lock biconditional re-run exhaustively (n=0..16): D⁻∈𝒜(n) ⟺ n≥4 ⟺ 2^{n+1}>16.
- **Subnetwork masks** [FT.20; FT.26(3); FT.28(4)]: dim 𝒦_Σ = 9 (G+W+H core) + 1·[EM active] +
  8·[strong: Colour≠∅ ∧ 𝒞=1] ≤ 18; activity census (9,10,17,18) exact; **the sealed EM-active
  N=5,6 members ATTAIN 18** — FT.28(4) Rmk's "only in the inside-sealed variant", now populated
  by a family. **D⁻ is never a summand of any 𝒦_Σ.**
- **Vertex placement**: every grouping's (a,b) blocks place attachments on 2-supports (δ: n=2,
  D_tick=8) and 3-supports (ε: n=3, D_tick=16 = C_cap **exactly saturated**); n=4 → 32>16
  inadmissible ⟹ **no vertex carries ≥4 attachments**; N=5 runs on ≥2 supports in every
  grouping (uniquely 1+1), N=6 on ≥2 (3+0 or 0+2). The connectors between supports: no frozen
  species — IT-O4, sharpened (the census names the decomposition, ¬the glue).
- **The D⁻ status chain, re-verified row-wise**: D⁻-configured junctions (placement) [Census
  FT.35(4); CT4.1] → mask annihilation ∀n≤3 (no pole of Z(𝒟,n), one-way transfer) [CT4.2] →
  formal unlocking nonzero-but-unrealized (ι₄), vertices {V₀..V₃} [AT.50(5); CT4.4a(1);
  CT0.11] → structureless even if reached (no gauge algebra/generator; dust w=0; entropy
  locked) [CT4.4/4.5/4.7] → void closure (no construction could exist inside the bound)
  [BM.143(1); AT.29(3),(4); IT.2(6)]. **THE CENSUS TERMINATES IN A STRUCTURAL CENSORSHIP, NOT
  A SMOOTH SINGULARITY** — the interior is preserved (every edge registered [D0.7]) and
  provably cannot reach the boundary.

## V. The synthesis (machine §D) — the "stellar collapse boundary" as exact ledger rows

| quantity | behaviour with N | locus |
|---|---|---|
| grammar g(N) | **GROWS strictly** (1,3,10,25,105,385,1540,7245,32725,164395 for N=3..12) | IT.9(3); IT.2 |
| channel width | **GROWS**: 4^N states, 2N+1 classes | IT.9(1) |
| δ share | **GROWS within the family**: 0, 1, 3/5, 9/11, 387/427 (N=3,5,6,9,12) | IT.9(5); IT.7(3) |
| the D⁻ sink | **CONSTANT**: dim 𝒦^{(D⁻)} = 1 at every rung — full at birth, structureless | CT4.4; D4.1; AT.50(1) |
| the per-vertex cap | **HARD**: D_tick(3)=16=C_cap saturated; D_tick(4)=32 inadmissible | CT0.5/6 |

**"D⁻ pure saturated areas" do not exist as growing regions** — there is nothing for the census
to encompass. The exact content of the collapse framing (flagged; no astrophysical species
identified [P5; Def-BM.3(7)]; no density/pressure primitive appears anywhere): **a COMBINATORIAL
CAPACITY LIMIT of the topology-blind sum [Def-H.32(1)]** — maximal grammar/width growth against
a constant one-dimensional censored sink behind a hard per-vertex cap.

## VI. Check ledger

`multi_seal_census.py` — **9/9 EXACT**, no floating point: A1 (width engine: Laurent vs
binomial at N=2,3,5,6 + frozen rows + sums + class counts), A2 (cross-N inequality census +
exclusivity + peaks), B1 (grammar triple-certified at N=5,6 + the frozen 3/5–2/5), B2 (the
unique-solution strain row + no-4ℤ-sector), B3 (periodicity N=2..18 + exact Fraction shares +
monotonicity along 3m), C1 (both mask species + the attainment + the n=0..16 biconditional),
C2 (per-grouping support placement + tick demands + the n=4 wall), C3 (the D⁻ chain, block
census + row-wise citations), D1 (growth/constancy/cap synthesis). Level runner after this
tier: **4 checkers, 42 markers**; gate: **3 Part 6 documents**.

## VII. Adjudication

- **IT-O2 CLOSED ON ITS CENSUS SIDE** at the N=5,6 boundaries (widths, grammar, masks,
  placement, D⁻ status). **RESIDUE (IT-O2 open):** the amplitude side — the Def-H.32 ensemble
  sums over the grouping sectors (10 sectors at N=5, 25 at N=6, each with its (−1)^ℵ dressing);
  AT.44/AT-O30 engines reusable.
- **IT-O4 STAYS OPEN, SHARPENED:** the (a,b) census names the exact support shapes the
  connector species must join (N=5: 2-support+3-support uniquely; N=6: three 2-supports or two
  3-supports); count per pair, winding d [FT.34(3) skeleton], fusion/sharing — still unconstructed.
- **The Architect's IT.4-exception flag** [IT.8(3)] is unchanged: this is the (p,n)-side census;
  the electron-saturated members belong to IT-O2's amplitude side.
- Declarations issued: none. §Cal-IT empty. Species bars honored throughout ("multi-seal
  EM-bound composites"; the collapse analogy flagged as framing). Level-5 record cited, never
  edited [AT.63(2)].

> *The corpus rewards: read the whole rather than the era; treat every "absent" as level-local;
> let exact arithmetic, not plausibility, decide. — AT.39 Phys*
