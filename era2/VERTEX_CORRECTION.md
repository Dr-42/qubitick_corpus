# VERTEX CORRECTION — the ledger-native anomalous read, in the fully dressed ensemble

**Session 5 discovery record.** Directive: derive the discrete analog of the QED vertex correction
Λ^μ(p′,p) by evaluating the moment operator M̂ = −q_EM(I⊗κ̂) [AT.47(3)/AT.48(2a); Def-H.43] in the
fully dressed topology-blind ensemble; isolate δ := ⟨M̂⟩_dressed − ⟨M̂⟩_tree; adjudicate BM.125(4)'s
three grounds; check the AT-O11 dictionary gap; close AT-O6 or locate the obstruction exactly.
**Machine:** `canon/era2/vertex_correction.py` → **23/23 EXACT, 0 failures** (~27 s). Suite:
**33 checkers, 587 exact markers, 0 failures, exit 0.** Candidate tags **AT.52–AT.54**, closure
**AT.55**, consolidated in `Part5_Atomic_era_TierAT9.md` together with session 4's AT.50/AT.51.

---

## 0. The standing instruction that shaped the session

The Architect, opening the session: *"Do not believe in previous era/tier no-gos head on. A lot of
no-gos become possible/unnecessary reads later on. If something is reducible to axiom and/or
definition and/or calibration floor, it is considered derived."*

That instruction paid off immediately and twice. **(1)** FT.106(3c)'s "amplitude death of k≥2 —
the winding-1 sector is amplitude-live exactly through dissolved-digon covers" reads as a general
law, and the directive itself repeats it ("dissolved digons inside covers" as the only
higher-winding content). It is not general: it is the **B=4 census total**, and the frozen canon
already knew it — Census FT.69(3)(v)/(5) records **504 four-cycles inside cube covers and 672
inside octahedron covers** (14,832 digon + 4-cycle instances at the cube). The death row is
budget-local. We then built the **minimal** revival: a V=5, six-edge cover carrying two dissolved
4-cycles (the theta pattern), value 64 = 4³, machine-exhaustive minimality at V≤4 (4095 patterns)
and V=5 (262,599 subsets), and a general tight ladder **B_min(m) = 2m + ⌈m/2⌉** with witnesses at
V = 3, 5, 8, 10, 13 for m = 1..5. **(2)** AT.48(5ii)'s "the dressing is FLICKER-SENSITIVE" is true
of ℵ's value but **false of its sign**: the master parity identity (−1)^ℵ = Π_{cov odd} σ_e makes
the A8 dressing sign **sector-locked** — (−1)^{|q|} on single open chains, +1 on closed ones. A
refinement on the record, not a retraction.

---

## I. The dressed ensemble (AT.52)

**Setup.** The lepton–baryon composite is ONE global Def-H.32 configuration sum [AT.42(1)]; the
connector's dynamics is the k-channel Janus move system [Def-H.32(7); AT.44(1)]: states = retained
sets of the k-pair floor, moves J±_i with weights x_±, strict alternation (Ĵ²=0 [BM.120(1)]),
return census N_k(2m) = 2^{−k} Σ_j C(k,j)(2j−k)^{2m}, resolvent
R_k(w) = Σ_m N_k(2m)(w²x₊x₋)^m [AT.44(1),(2)]. The ensemble measure is Def-BM.5's
sector-conditioned path integral with the derived stationary weights p = 1−4ε_q, u = 4ε_q
[FT.108(4); Def-BM.5(3)]; the pattern weights are Def-H.32(3)'s 𝒲 = v²t^{|R|}u^{L(R)} (amp) and
νt^{|R|}u^{L(R)} (norm); the amplitude classifier is FT.67(2)'s: v = 2^{|R|}(−1)^{Σκ} on exact
covers, 0 else.

**New derived rows.**

1. **The partial fractionization carries exact rational RESIDUES and an exact CONTACT term:**

   R_k(z) = c_k + Σ_{d∈{k,k−2,…}>0} a_{k,d}/(1 − d²z),  **a_{k,d} = 2^{1−k}C(k,(k+d)/2)**,
   **c_k = 2^{−k}C(k,k/2)** [k even], 0 [k odd],  z = w²x₊x₋;  sum rule c_k + Σ_d a_{k,d} = R_k(0) = 1.

   Machine: coefficient-wise in ℚ to z¹⁴, k = 1..8. k=1 recovers the bare zig-zag (a_{1,1}=1,
   c₁=0 [BM.121(2)]); k=2: a_{2,2} = ½, c₂ = ½.

2. **Attenuation is rational:** dominant residue a_{k,k} = 2^{1−k} (geometric); fixed-d ladders
   monotone: d=1: (1, ¾, ⅝, 35/64, …) strictly decreasing over k = 1,3,5,7,…; d=2: (½, ½, 15/32,
   7/16, …) over k = 2,4,6,8,… with the exact plateau a_{2,2} = a_{4,2} = ½. **Contact diversion:**
   c_k = (½, ⅜, 5/16, 35/128, 63/256) at k = (2,4,6,8,10), zero at odd k — an even channel count
   moves an exact rational fraction of the return weight OFF the pole ladder. **Answer to the
   directive's question: yes — flicker attenuation produces rational correction factors, with
   closed forms, in the alphabet {ε_q} ∪ {binomials}, no calibration.**

3. **The winding revival ladder.** Every winding m ≥ 1 is amplitude-live from budget
   **B_min(m) = 2m + ⌈m/2⌉**:
   - **Bound (hand):** a 2m-cycle inside a cover alternates m centres / m hubs [FT.69(3)]; an
     on-cycle centre is saturated (type (1,1) = exactly its two cycle edges), so each hub's extra
     edge [FT.69(3)(ii)] is read by an OFF-cycle centre; an off-cycle centre reads at most two hub
     extras (its single in- and out-edge); hence ≥ ⌈m/2⌉ off-cycle vertices.
   - **Witnesses (machine):** m=1: V=3 double-digon hub, |R|=4, |C|=2, v=16, locked — **is**
     FT.69(5)'s frozen family; m=2: V=5 theta, |R|=6, |C|=3, v=64; m=3: V=8, |R|=10, |C|=5,
     v=1024; m=4: V=10, |R|=12, |C|=6, v=4096; m=5: V=13, |R|=16, |C|=8, v=65536. Every
     classifier = brute-force sign sum (exhaustive to |R| ≤ 16); every 2m-cycle on-shell at S=m
     (κ≡1, Θ=2m [FT.32(6); FT.107(1)]).
   - **Minimality at m=2, exhaustive:** V≤4: ZERO covers with a 4-cycle among all 4095 patterns of
     the bidirectional K4 (and the tetrahedron's 48 bypass + 16 locked digon-covers reproduced —
     the frozen FT.69(4)/(5) integers); V=5: full scan of every 4..8-edge subset of the
     bidirectional K5 (262,599 subsets): exactly **60** distinct covers with a 4-cycle, all at
     |R|=6, each carrying exactly TWO 4-cycles, ONE isomorphism class (60 = 5·4·3 = (hub-out,
     hub-in, shared-path-centre) choices = 30 directed 4-cycles × 4 completions / 2); none at
     |R| = 7, 8.

4. **The theta pattern (the minimal winding-2 cover).** R = {(0,1),(1,2),(2,3),(3,0),(1,4),(4,3)}
   on V=5: 4-cycle 0→1→2→3→0 with on-cycle centres {0,2}, hubs {1,3}, one off-cycle centre 4
   threading 1→4→3. cov ≡ 1; v = 64 = 4³ = 2^{|R|}. It is a THETA: two distinct directed
   4-cycles — (0,1,2,3) and (0,1,4,3) — sharing the 2-edge path 3→0→1; both on-shell at S=2; 4
   bases each: **8 amplitude-live winding-2 instances in the smallest possible cell.** The frozen
   B=4 census never saw one: it needed the fifth vertex.

5. **The lock parity of the tight ladder (new).** lockL = (1,0,1,0,1) for m = 1..5 at the tight
   bound: **odd windings are born LOCKED, even windings born clean.** Pigeonhole: for odd m the
   ⌈m/2⌉ off-cycle centres supply m+1 hub-endpoints to m hubs, so one hub carries ≥ 2 extras, so
   k_v = 2+2 = 4 ⇒ locked [CT4.5; CT0.11]. Machine at m=3 (V=8): BOTH tight variants lock (the
   shared-target threading locks hub 3 at type (3,1); the wrap threading locks hub 1 at (2,2));
   the first UNLOCKED winding-3 cover sits at V=9 (one graft threaded to a sink: 5→7→8), value
   1024, lockL=0. m=1 reproduces FT.69(5)'s locked hub. Structural parallel to the odd-winding ↔
   fermionic-sign row [FT.32(6); BM.113(4)] — **flagged, ¬identified** [P5; Def-BM.3(7)].

6. **The k=2 connector cell, amplitude-live.** The theta skeleton's census contains the 4-edge
   DOUBLE-THREAD HUB {(1→2),(1→4),(2→3),(4→3)}: source-hub (0,2) → two centres → sink-hub (2,0);
   cov ≡ 1; v = 4² = 16. This is AT.44's two-channel floor as a concrete configuration
   [FT.67(3d)'s V-thread grammar; BM.137(1)'s independent pairs] — dressing beyond the tree pole
   is not formal, it is enumerated and weighed.

---

## II. The moment operator, dressed (AT.53): δ = 0 exactly

**The evaluation.** ⟨M̂⟩_dressed is the instance-weighted mean of the promoted read
M̂(inst) = −q(inst)(I₂⊗κ̂) [Def-H.43; AT.47(3): γ_{F₀} = I⊗κ̂; AT.48(2a)] over the sector-
conditioned ensemble [Def-BM.5(1),(2)], with the exact layer weights of Def-H.32(3)/(5).

**C1 — the chain-local telescoping extension (L5 lemma).** Σ_int f_v = ½(σ_last − σ_first) holds
on EVERY simple open path of both witness skeletons (17 + 61 paths), under EVERY assignment of the
path's own signs (124 + 1248 evaluations), **including paths whose interior vertices are HUBS of
type (2,1)/(1,2)/(3,1)/(2,2)** — far outside EM.9b's frozen type-(1,1) clause. The frozen clause
is a SCOPE, not an obstruction: the telescoping is chain-local algebra. Cyclic sums vanish on
every cycle (32 + 144 evaluations) [AT.48(1) transported]. EM.9b's locus untouched.

**C2 — sector constancy.** Full instance-resolved (q,S) censuses: theta skeleton (3⁶ = 729
configurations; both layers; (t,u) = (1,1) and (3/4,1/4)) and hexagon skeleton (3¹⁰ = 59,049;
both layers; (1,1)). Every instance of a sector carries the SAME operator (q is the sector
label); distinct sectors carry distinct 4×4 operators. On closed-chain instances the
vertex-contraction channel vanishes [AT.48(1)] while the promoted core read [FT.40 closed-core
form] does not — two reads of one aspect, kept apart (BM.134(5) species pattern).

**C3 — THE DISCRETE WARD IDENTITY.**

> **δ := ⟨M̂⟩_dressed − ⟨M̂⟩_tree = 0** as an exact 4×4 Gauss(i) matrix identity — in every
> sector (q,S), at both layers, at both fugacity specializations, over every interleaving and
> cover of the censused cells. The genuine weighted mean (ΣᵢwᵢM̂(qᵢ))/(Σᵢwᵢ), computed from the
> census charge sums, equals −q(I⊗κ̂) entrywise.

Three independent supports: the chain-local telescoping incl. hub interiors (C1); the charge
preservation on 𝓔(𝒳) [Def-BM.5(1): the ensemble is sector-conditioned on the boundary data]; the
sector-constancy of the promoted read (C2). The boundary splitting 2|q| [AT.48(5i)] is **not
renormalized by any flicker, any interleaving, any cover, any winding.**

**Non-vacuity, three rows.** (a) The ω-symmetry, split exactly as the involution σ→−σ forces it
(contribution_R(−q) = (−1)^{|R|}·contribution_R(q)): the norm layer, the cover support (|R|=2|C|
even [FT.79(2)]), and the non-cover EVEN support are symmetric; the non-cover ODD support is
**antisymmetric** — hence Z^amp_ncO(0,S) = 0 exactly (the neutral sector receives no odd
non-cover amplitude support). The hexagon cell exhibits the asymmetry LIVE:
Z^amp(−1,0) = 11348 vs Z^amp(+1,0) = 19060, difference exactly 2×(−3856) = twice the odd
non-cover part — a cell-level sharpening of FT.106(3b)'s cancelling-support row and the exact
mechanism behind FT.106(3d)'s scope clause ("amplitude layer on the cover support"). (b) The
unconditioned norm-layer mixed averages collapse to ⟨q⟩_ens = 0 — the neutral operator, by
derived symmetry, not by accident. (c) Every charged sector's own average keeps its read exactly.
**The ensemble moves the operator read ONLY through the sector MIX, never inside a sector.**

**C4 — THE MASTER PARITY IDENTITY (sharpens AT.48(5ii)).**

> **(−1)^ℵ = Π_{e: cov(e) odd} σ_e** on EVERY configuration (668 + 58,152 checked inside the
> censuses; zero violations) — FT.67(1)'s per-centre identity (−1)^{|f_v|} = σ_in σ_out
> multiplied out.

Corollaries (exhaustive): single open chains L=2..9: **(−1)^ℵ = (−1)^{|q|}** — the A8 dressing
SIGN is SECTOR-LOCKED, the flicker cannot flip it (|f| ≡ f mod 2 termwise; Σ_int f_v = −q);
closed chains L=2..7: (+1) (ℵ even); covers: (−1)^ℵ = Π_e σ_e (all cov = 1). Consequences: the
A8-dressed operator (−1)^ℵM̂ = (−1)^{|q|}M̂ is ALSO sector-constant on single-chain
configurations; ε_total = i^Θ(−1)^{|q|} closes in the fourth roots [Def-BM.16(5)]. **Record:
AT.48(5ii)'s "dressing flicker-SENSITIVE" is REFINED, not retracted** — ℵ's VALUE fluctuates
(§III.1); its PARITY is charge data. Pointwise: ℵ − |q| ∈ 2ℤ_{≥0} (exhaustive; triangle
inequality + parity).

---

## III. The anomalous read (AT.54): exact rationals on the measure layer

**1. The ℵ-excess means.** Per (L,q): ⟨ℵ⟩ = (L−1)/2 for L ≥ 3 and = |q| at the minimal cell L=2
(exhaustive L=2..9, both sectors; the interior signs are free given the ends). On the BM.137(1)
n-pair-floor measure:

⟨ℵ⟩^{(n)} = [Σ_{j≥1} C(n,j) p^j u^{n−j} g(2j)] / (1−uⁿ),  g(2) = |q|, g(2j) = (2j−1)/2 [j≥2]

— verified as a POLYNOMIAL IDENTITY in ℚ[u] (n = 1..6) and at three exact witnesses
u ∈ {½, ¼, ⅓}. At detailed balance ε_q = ⅛ (u = ½): ⟨ℵ⟩⁽²⁾ = 7/6 ⇒ **excess = 1/6** (q=±1);
⟨ℵ⟩⁽³⁾ = 10/7 ⇒ **excess = 3/7**. The anomalous magnitude is a rational function of ε_q ALONE,
calibration-free — and by AT.53 it never touches the operator layer.

**2. The first amplitude-live winding-2/3 sector censuses (new derived integers).** Engine
certified against two frozen rows: BM.137(4)'s budget-2 pincer Z₂^norm(q,1) = (4,2,2) at
q=(0,+1,−1), all other sectors zero — AND FT.106(3b)'s cancelling non-cover support at the
smallest cell: Z₂^amp(0,1) = +4, Z₂^amp(±1,1) = (−2,−2), summing to EXACTLY 0 (the digon pattern
is no cover). Norm layer matched against FT.106(3a)'s closed form m_q2^{|R|−2} per instance on
every sector. New rows at (t,u)=(1,1), as (Z^amp; Z^norm) at q = (−1, 0, +1):

| cell | S=0 | S=2 | S=3 |
|---|---|---|---|
| theta skeleton (V=5) | (263, 622, 263); (1071, 2142, 1071) | **(128, 256, 128); (288, 576, 288)** | — |
| hexagon skeleton (V=8) | (11348, 37832, 19060); (217728, 435456, 217728) | (912, 2272, 912); (11664, 23328, 11664) | **(2816, 6656, 2816); (15552, 31104, 15552)** |

with the exact three-way split Z^amp = Z^cov + Z^ncE + Z^ncO per sector (e.g. hexagon S=0, q=−1:
17060 − 1856 − 3856 = 11348). The cover part is exactly 2:1 between q=0 and q=±1 everywhere
(m_q factorization on covers); the winding-2/3 rows are the **first amplitude-live higher-winding
sector integers in the corpus**, the minimal-budget companions of FT.106(3)'s frozen B=4 table
(802/4796 at S=1; 1196/5336 at S=0). Census integers are amplitude-layer structural reads,
**barred as mass reads** [BM.111(6); FT.79(5); BM.30(5)].

**3. POSITION vs RESIDUE — the Lamb-analog row.** The pole positions W_d = 1/(d²x₊x₋) are
k-INDEPENDENT: the 1/d² ladder [AT.44(5)] is exactly position-degenerate across channel counts
(d, d+2, d+4, … ≤ 12 machine). The dressing splits the degeneracy in the RESIDUES a_{k,d}
(4 distinct values at d=1 over k=1,3,5,7; 3 at d=2 over k=2,4,6,8 including the plateau ½) and in
the contact c_k — **never in the positions**. The ledger's Lamb analog is an INTENSITY
redistribution at unshifted level prices: same 1/d², different rational pole weights, plus the
even-k contact diversion. A frequency shift would need a position-moving dressing; the move
system has none — exact, not approximate. The level-price read rule stays the marked
specification [AT.44(8iv); AT-O26], unchanged.

**4. The frozen ratio, re-certified.** 4796/802 = 2398/401 (401 prime; 2398 = 2·11·109) ≠ 2 =
m₀/m_{±1} [BM.111(4); FT.106(3a)]: the dressing breaks the charge degeneracy at the amplitude
layer and can never break it at the operator layer (AT.53(3)).

**5. BM.125(4)'s three grounds, bypassed one by one.** (i) *no single Δ(j)*: the evaluation is an
operator-valued ensemble average, ray-by-ray on ℋ_ω, sector-constant; the winding content enters
as the S-graded census and the revival ladder — BM.124's multiplet ladder never collapsed. (ii)
*no product of the two Def-H.37 clauses*: symbol census of the construction = {q, ℵ, κ̂, N_k,
C(k,j), ε_q, t, u} — no ℓ_c, no μ̂, no Θ_R, no G(c), no Δ(m); the BM.125(3) matching identity is
never invoked. (iii) *dimensions*: every ingredient is 𝔮⁰ (a PRICE in the HistLog §V.32
species); the refuted ansatz's [ℓ_c] = 𝔮⁰-vs-𝔮⁻¹ contradiction cannot arise. **BM.126(1)
untouched:** the channel count k is the connector floor's pair count [BM.137(1)] — configuration
data, ¬a spin read; a_{k,d} are binomial coefficients of the derived partial fractionization, ¬a
reweighting x_± ↦ x_±(k); the measure is the derived stationary one [FT.108(4); Def-BM.5(3)];
grounds (O1)–(O4) never engaged.

---

## IV. The adjudication (AT.55)

**AT-O6 — CLOSED AS DRESSED STRUCTURE.** AT.48 constructed the coupling; this tier evaluates it
in the fully dressed ensemble:

1. **The vertex correction to the operator read VANISHES IDENTICALLY** — δ = 0 exactly, at every
   order of the Janus dressing, both layers, every fugacity specialization tested. Not an
   approximation, not a symmetry assumption: the record's own telescoping + charge preservation +
   sector constancy. The discrete Ward analog.
2. **The anomalous read is the exact triple** (2|q| unrenormalized boundary splitting;
   sector-locked dressing sign (−1)^{|q|}; measure-side rationals: ℵ-excess means in ℚ(u),
   residues a_{k,d}, contact c_k, sector census integers, revival ladder B_min(m)).
3. **The continuous a = (g−2)/2: LEVEL-LOCAL NO-GO** (the AT.43 classification pattern), with
   three named missing definitions: **(M1′)** a declared read rule mapping the measure-side
   rationals {a_{k,d}, c_k, ⟨excess⟩, sector weights} to a chart-currency moment shift
   (AT-O26-class; a closure-phase declaration); **(M2′)** the value of ε_q (AT-O27); **(M3′)** the
   chart-side scale and e₀ [P4; EM.25(7)]. Absent those, the splitting stands unrenormalized and
   the dressing is integers and rationals — by construction, not by failure [BM.88(1): no loop;
   P5]. Sharper than AT.48(5v): not merely "no loop exists" but **no continuous locus exists** —
   every dressed operator read is sector-constant.
4. **AT-O11 DOES NOT BLOCK** (the directive's step 5): zero dictionary calls. The whole
   calculation lives on the pair arena, the k-channel resolvent, chain sign tuples, and frozen
   censuses; no n ≥ 3 carrier invariant is mapped to a metric coordinate anywhere. AT-O11
   (13 invariants vs the 26-dimensional mask space [AT.40; AT.50(6)]) gates chart-side coordinate
   identifications — excluded by the directive and by BM.134(5).
5. **Quarantine [P5]:** a_e, a_μ, a_μ/a_e ≈ 1.0054, the Lamb shift, 2S–2P — scoring targets,
   never inputs; no comparison formed anywhere in this file. The tree-level "parallel" (splitting
   2 per unit charge) remains FLAGGED, ¬IDENTIFIED [AT.48(5i); Def-BM.3(7)].

**New open row (AT-O30).** The winding-resolved cover census at B ≥ 5: the minimal cells are
computed here (theta V=5; hexagon V=8 locked/unlocked; the ladder witnesses); the frozen-cell
extension — cube/octahedron-level winding spectra, per-skeleton saturation of B_min(m), the
V=5..7 full cell censuses — is FT.69(3)(v)/FT.106(3)-type census work at the next budgets.
Growth data: FT.105. Not blocking anything; recorded as the natural continuation.

**Premise-level records of the session:** FT.106(3c) re-scoped (budget row, superseded
constructively at B=5 — the frozen Census FT.69 rows already carried the larger-budget evidence);
AT.48(5ii) refined (parity sector-locked; sensitivity lives in the value); FT.106(3d)'s scope
clause mechanized (the |R|-parity involution, three-way split); EM.9b extended chain-locally to
hub interiors (L5 lemma, locus untouched).

---

## V. Check ledger

`canon/era2/vertex_correction.py` — **23/23 EXACT**, no floating point anywhere:

- **A** (4): partial fractionization + residues + contact + sum rule (k≤8, z¹⁴); attenuation
  ladders (k≤16) + contact positivity; N_k(2m) brute-force ∧ closed form + radius; the two frozen
  winding-1 minimal covers (classifier = brute-force = 16).
- **B** (5): V≤4 exhaustive (4095 patterns: 0 four-cycle covers, 0 triangles, 48+16 digon
  covers); the theta witness (cov, 64 = brute force, two S=2 cycles); V=5 exhaustive minimality
  (262,599 subsets: 60 patterns at |R|=6, one iso class, none at 7,8); the m=1..5 tight ladder
  (witness rows incl. brute-force sign sums to 2^16); the lock parity (both V=8 variants locked,
  the V=9 unlock, lockL parity row).
- **C** (5): chain-local telescoping (1372 path evaluations + 176 cycle evaluations); sector
  constancy (668 + 58,152 configurations, both layers, two fugacities); the k=2 double-thread
  cell (16 = brute force); the Ward identity (per-sector weighted means = sector operators,
  mixed ⟨q⟩_ens = 0, ω three-way split incl. the live antisymmetry 11348/19060 = 15204 ∓ 3856);
  the master parity identity (in-census, zero violations) + exhaustive corollaries.
- **D** (4): ℵ-excess means (enumeration + ℚ[u] polynomial identity, n≤6, three u-witnesses; 1/6,
  3/7 at ε_q=⅛); the certified engine (BM.137(4) + FT.106(3b) at the smallest cell) + the new
  winding-2/3 sector integers + FT.106(3a) closed-form match + FT.106(3b) identity on both
  skeletons; position-vs-residue (degeneracy exact, residues split); the 2398/401 reduction with
  401's primality.
- **E** (4): BM.125(4)'s grounds (i),(ii),(iii) + BM.126(1).
- **F** (1): the adjudication.

**Level 5 suite: 33 checkers, 587 exact markers, 0 failures** (`run_all_era2.py`, exit 0).

**Adopted:** nothing. **Declared:** nothing. **Calibration values:** none. **Measured values:**
none [P5]. **Species identifications:** none [Def-BM.3(7)]. **CLOSED:** AT-O6 (as dressed
structure). **SHARPENED:** FT.106(3b)/(3c)/(3d) scope rows (mechanism exhibited per cell).
**NEW OPEN:** AT-O30 (the B≥5 winding-resolved cover census).
