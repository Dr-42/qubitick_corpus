# CROSS_CURRENCY_MATRIX.md — the session-13j working record (Tier IT.14 candidate, IT.43–IT.45)

**Directive (Architect, session 13j).** *"Audit a New Cross-Currency Mass Matrix, Its Tensor Product,
S-T Decomposition, and the Photon/Observer Derivative Asymmetry … M = [[m_L, ρ_B],[ε_q, m_S]] … Placing
ρ_B (baryon currency) and ε_q (lepton currency) as off-diagonal entries in the same matrix does NOT
violate the incommensurability bar … a matrix is a structural container where their product ρ_B ε_q
appears in the determinant and eigenvalues — which is the exact algebraic seat of the IT.4 handshake
indicator … S carries (ρ_B + ε_q) … T carries (ρ_B − ε_q) … ∂ε_q/∂ρ_B = 0 (the photon view) vs
∂ρ_B/∂ε_q ≠ 0 (the ideal observer view) … Scenario A (new structure) or Scenario B (redundancy)."*

**Machine.** `checks/cross_currency_matrix.py` → **19/19 EXACT**, no floating point, no measured value
(multivariate Laurent polynomials over Gauss(i) over `Fraction`; formal partial derivatives; integer/set
censuses; the canon's own B3 swap basis re-used verbatim).

**Session context.** First session after the crash that ended session 13i mid-flight. Environment
restored: PR #7 confirmed MERGED via the API (merge commit `43dcb8d`, 2026-10-13T07:06:47Z); fresh
clone at master = origin/master = `43dcb8d`; era-1 suite 80/80, Level-5 runner 37/643 + gate, Level-6
runner 14/211 + gate — all green from the fresh clone before any new content; canary green. New
sandbox quirk logged: a *script file* that `open()`s a credential path gets a phantom
`FileNotFoundError` while bash and inline `python3 -c` read it fine — pass credentials via argv from
bash instead (MEMORY §7).

---

## 0. Stance

The object enters as a conjecture (standing order 1). Every entry, every claimed identity, and every
claimed seat is checked against the frozen canon and the Level-6 record before anything is built. The
prior mass-matrix adjudication (Tier IT.12, IT.37–IT.39) is the closest precedent and is treated as a
row, not as a vibe: its verdict (redundant + parametric, not adopted) is re-derived for the new
object rather than assumed. Where the directive and the rows diverge, the rows win — and this record
says so six times (P1–P6 below).

## A. Entry-by-entry audit (→ IT.43(1))

| entry | the directive's meaning | the canon's verdict |
|---|---|---|
| m_L | Lyapunov/informational mass, m_L = E_int ln2/𝔥 | ✓ the derived informational read [FT.44(4); the neutron floor row BM.17(3): m_hid^(n) = 6ln2/𝔥]; alphabet {E_int, ln2, 𝔥}; degree 𝔮^{1/2} |
| m_S | "seal mass — quantum free charge of rung 1, related to the lightest neutrino mass scale" | ⚠ **"quantum free charge" is not a canon term** (the only "free charge" occurrence is Part 3's fermion-core prose, a different object). Two candidate reads, BOTH existing rows: (a) the rung-1 seal informational mass 2ln2/𝔥 [IT.37(1); E_int=2 floor, FT.28] — equal to the two-bit ν floor m_ν𝔥 ≥ 2ln2 at equality [BM.70(2),(3) re-cited at BM.83(8)]; (b) the lightest-ν scale σ_ν z₁ ln2/𝔥 with σ_ν UNDECLARED [BM.83(4),(8); FT.143(3): the absolute ν mass ¬derived]. Read (b) makes even Tr M a barred cross-currency sum [IT.4(3) pattern]. |
| ρ_B | baryon pole parameter, dimensionless, undeclared | ✓ exactly as cited: ρ_B = μ̂'²𝔥²/(ln2)² ∈ 𝔮⁰, a restatement of undeclared data [BM.83(4)]; baryon/pole family [IT.5(1)] |
| ε_q | flicker threshold, dimensionless, 1/8 distinguished five ways, adoption ¬issued | ✓ exactly as cited: the A4 threshold [BM.19(2); D0.4], x₊=1−4ε_q, x₋=4ε_q [BM.19(2)]; AT-O27 status correct |

The currency labels are right; the disjointness of the two alphabets is IT.4(2)'s census and is
re-certified by machine (shared symbols only 𝔥, ln2, π).

## B. Step 1 — the tensor product (→ IT.43(2)): CORRECT

The directive's explicit 4×4 equals the Kronecker rule (M⊗M)_{(i,k),(j,l)} = M_ij M_kl entrywise
(16/16 symbolic equalities). The pure product ρ_B ε_q sits at exactly (2,3),(3,2) (1-based), in
det M = m_L m_S − ρ_B ε_q with coefficient −1, in the discriminant (m_L−m_S)² + 4ρ_B ε_q with
coefficient +4, and in the IT.38(1)-style combination C₁₁ + C₂₂ = 4ρ_B ε_q.

**But the seat is unformed.** IT.4(2) is an exhaustiveness row: the formed MIXED loci are EXACTLY
THREE — 𝓑_ens^(n) [BM.137(3)], 𝓦_channel = x₊²χ_{NE≥𝒯₀} [BM.122(3)], and the handshake χ_{NE≥𝒯₀}
itself [Def-BM.17(3); BM.122(2); BM.134(5)] — and the handshake is BINARY, built from {E_int, 𝔥, ln2,
NE}. BM.134(5): the two resolvent species "meet only through the threshold indicator χ_{NE≥𝒯₀}".
Machine: none of the three loci's alphabets contains ρ_B or μ̂'²; the product ρ_B ε_q appears in NO
formed read. "The exact algebraic seat of the IT.4 handshake indicator" is contradicted by the
census: cross-currency VALUES do not exist pre-calibration [IT.4(2)].

## C. The new obstruction IT.37's M did not have — 𝔮-inhomogeneity (→ IT.43(3))

The corpus's own dimension bookkeeping (BM.83(4)'s exponent arithmetic: [m] = 𝔮^{1/2} from m = μz;
ρ_B ∈ 𝔮⁰; ε_q a threshold in 𝔮⁰):

- deg(diagonal entries) = 𝔮^{1/2}; deg(off-diagonal) = 𝔮⁰ — M is not graded-homogeneous;
- det M sums 𝔮¹ (m_L m_S) with 𝔮⁰ (ρ_B ε_q) — a dimensionally inhomogeneous sum;
- the eigenvalue discriminant (m_L−m_S)² + 4ρ_B ε_q does the same.

IT.37(1)'s M kept w mass-dimensioned, so its determinant was homogeneous (machine contrast: deg
entries {1/2}, deg det {1}). Homogenizing the new M needs a declared mass² scale — a P4-class act;
none issued [BM.6(4)]. So the object is *worse-formed* than the mass matrix IT.12 already declined.

## D. Step 2 — the S-T decomposition (→ IT.43(4),(5)): algebra exact, one claim corrected, one gem

S + T = M⊗M, S^T = S, T^T = −T verified symbolically (16/16 each). Explicit entries:

- S: ½m_L(ρ_B+ε_q) at (1,2),(1,3),(2,1),(3,1); ½(ρ_B²+ε_q²) at (1,4)/(4,1); ½m_S(ρ_B+ε_q) at
  (4,2),(4,3),(2,4),(3,4); m_L², m_L m_S, ρ_B ε_q, m_S² on the diagonal positions.
- T: ½m_L(ρ_B−ε_q), ½m_S(ρ_B−ε_q) analogues; ½(ρ_B²−ε_q²) at (1,4)/(4,1); zeros on the diagonal.

**Correction:** T's (1,4) entry factors as ½(ρ_B−ε_q)(ρ_B+ε_q) — T carries the SUM as a factor too,
so "T carries (ρ_B−ε_q)" is true but incomplete (verified as a polynomial identity).

**The gem (the one true structural fact):** ι(M) = M^T, where ι is the currency involution ρ_B↔ε_q
(the diagonal is ι-fixed). Hence ι(M⊗M) = (M⊗M)^T, ι(S) = +S, ι(T) = −T: **for this object the
transpose S-T split IS the currency-exchange symmetrization.** It is elegant — and it exposes the
bar rather than bypassing it, because S's entries are then LITERALLY the cross-currency sums.

**The container argument fails (the key-claim adjudication).** The bar forbids sums/conversions *as
formed reads* [BM.83(3),(9); BM.140(5): "the comparison is arithmetic, ¬a bridge … no derived
equation converts them"; IT.4(3): the reduced mass μ = m₁m₂/(m₁+m₂) "requires a SUM across the
disjoint value alphabets — a cross-currency equation, barred … formable only as a SYMBOLIC
expression carrying undeclared slots"]. A matrix is not exempt: its scalar reads ARE sums. Already
at 2×2 the Pauli coefficient v₁ = Tr(Mσ₁) = ρ_B + ε_q (machine), and v₂ = i(ρ_B−ε_q); the tensor
layer propagates them: C_μν = v_μ v_ν (all 16 verified symbolically) and 12 of the 16 carry
(ρ_B+ε_q) or (ρ_B−ε_q) as a factor. Verdict: the ARRAY is formable as a symbolic expression with
undeclared slots (IT.4(3)'s precedent — exactly the status of the reduced-mass formula); every
scalar invariant (Tr, det, λ±, S entries, T entries) is barred as a formed read/value. The
container launders nothing.

**The CT1.12a(2) grading map is REFUTED on the canon's own operators.** The S-T split is the ±1
eigensplit of the TRANSPOSE involution on End(ℂ⁴); CT1.12a(2)'s S-grading is the ±1 eigensplit of
the pair-channel SWAP CONJUGATION (re-certified: J_i, K_i anti-invariant; E₀, Σ, W_i, E^ii
invariant — the measurement_theorem.py B3 basis, verbatim). The two involutions CROSS-CUT: of the
six S-odd operators, exactly THREE — J₂, K₁, K₃ — are transpose-EVEN (they sit in S, the
"cooperative" part), and the S-even carrier W₂ is transpose-ODD (it sits in T, the "gap" part).
Neither S ⊆ S-even nor T ⊆ S-odd holds. Both involutions split 16 = 10+6 and their joint refinement
is 7+3+3+3, rhyming with CT1.12a(2)'s 10 = 1+1+5+3 and CT1.1's 7+3+3+3 — a numerology flag, NOT an
identification [BM.134(5) dictionary discipline]. AT.56's six bivectors: only 2 of 6 transpose-odd
(dim(bivector ∩ T) = 2), and swap conjugation sends σ^{12} = −(σ₃⊗σ₀) to −(σ₀⊗σ₃), proportional to
none of the six (exact Pauli-coordinate comparison). And the IT.38(2) 16-vs-8 over-count carries
over: against the derived 8-dim force algebra span{I₄, σᵢ⊗I₂, σᵢ⊗κ̂, I⊗κ̂} (κ̂ = σ₃ [AT.56(1)]),
S has FOUR directions outside and T has FOUR outside — any force reading of S/T is a stipulation.

## E. Step 3 — the derivative asymmetry (→ IT.44): NO SEAT

Machine census over the IT.5(1) formed-read table (m_hid, Δx_B, r_s, Δx_B·r_s, ρ_B, m²_pole,
𝓦_channel, 𝓦_round, 𝓑_ens^(2), W_d), encoded exactly with formal partial derivatives (a polynomial
operation — no smooth-manifold import):

1. **No formed read contains BOTH slots** — ρ_B and ε_q share no formed read, so no derived
   functional dependence exists IN EITHER DIRECTION. The independence is SYMMETRIC.
2. ∂ε_q/∂ρ_B = 0 AND ∂ρ_B/∂ε_q = 0 exactly (ρ_B's derived read μ̂'²𝔥²/(ln2)² has alphabet
   {μ̂'², 𝔥, ln2}). The claimed pair (0, ≠0) has no seat in any derived row.
3. The directive's premise fails: ∂m_hid/∂ε_q = 0 and ∂Δx_B/∂ε_q = 0 — "the informational mass …
   governed by the flicker threshold" is FALSE on the derived rows [FT.44(4); Def-BM.4(1)]. The
   ONLY nonzero flicker partials are at the composite loci: ∂𝓦_channel/∂ε_q = −8(1−4ε_q)χ ≠ 0 while
   ∂𝓦_channel/∂ρ_B = 0 [BM.122(3); IT.4(2)].
4. A nonzero ∂ρ_B/∂ε_q would require a DECLARED functional link across the currencies — exactly the
   conversion BM.140(5)/BM.83(9) bar ("no derived equation converts them"), and a P4-class
   declaration; none issued.
5. **The framing is rejected row by row:** "perspectives" are not ledger primitives — the observer
   is a designated register [Def-H.9; IT.1(8)(P4): ¬consciousness, ¬smooth analogy]; the photon has
   NO formed perspective reads at all (the transit-leg amplitude ¬formed [(R9''); BM.122(6);
   IT.3(6)]; D3.7 trivial chains are out of Def-H.38's scope [IT.41]; the pair channel's amplitude
   ¬formed [BM.122(6)]); ε_q is a GLOBAL A4-threshold slot [BM.19(2); D0.4], not a per-species
   possession; and ρ_B (an undeclared 𝔮⁰ slot) is NOT a seal class — the proton class 15 of 64 is
   the derived integer census W₃(Q) = C(6,Q+3) [AT.41(2),(3); IT.4(4)] — a category error.
6. **The IT.10 citation is inverted.** The anchor's bypass licenses the geometric/cardinal/sign
   reads BECAUSE they never mix currencies [IT.32(3): "NONE is a cross-currency mass sum"];
   Δx_B·r_s = 𝔥²/(2ln2) re-derived symbolically, E_int-independent, alphabet {𝔥, ln2} — shared
   currency. Citing IT.10 for a ρ_B(ε_q) dependence uses the row to license the very thing its
   proof excludes.

**The salvageable kernel (already derived):** the LOCUS distinction — ε_q enters the observer's
formed reads only through the three composite mixed loci (𝓦_channel = (1−4ε_q)²χ; the Born-width
distribution sharpening at zero flicker [BM.122(3)]), while the geometric reads (Δx_B, Δx_B·r_s)
are ε_q-free [IT.31(1); IT.32(3)]. What the Architect's intuition reaches for is IT.4(2)'s
exhaustiveness, not a derivative asymmetry.

## F. Step 4/5 — redundancy and the verdict (→ IT.45): SCENARIO B

- **Species census (machine):** M − M† ≠ 0 symbolically (the (1,2) entry ρ_B − ε_q; v₂ purely
  imaginary) — NON-HERMITIAN, unlike IT.37(1)'s M and BM.22's F_ext. The line: F_ext reduced =
  h·I + q·σ₁ (2 slots, symmetric flip, DERIVED q ∈ {−1,0,+1} [BM.22(7); EM.9]) ⊂ IT.37's M
  (3 slots, Hermitian, conjugate flip) ⊂ the new M = the GENERAL 2×2 (4 slots: two derived diagonal
  reads + the two undeclared currency slots). The new M is a specialization of the same parametric
  construction class recorded at IT.37–IT.39 — same Pauli anatomy (v_μ re-derived), same tensor
  factorization C_μν = v_μ v_ν, same 8-dim force algebra over-count. **Redundant** [IT.38(3)].
- **The S-T split adds no new content:** S and T live in the same span{σ_μ⊗σ_ν} (their supports
  are the 10 transpose-even / 6 transpose-odd directions — 16 total, zero new operators), and they
  create no new mixed locus (IT.4(2) exhaustiveness). The split's only new fact (ι = transpose) is
  a property of the slot placement, and its consequence is a bar exposure, not a bypass.
- **m_S:** maps to existing rows under both candidate reads (see §A); the choice between them is
  undeclared, and the audit's verdict holds under BOTH — no route-choice declaration is forced.

**VERDICT — Scenario B (redundancy), sharpened:** M is CONSTRUCTIBLE and its algebra is EXACT, but
it is (i) REDUNDANT — the general-2×2 non-Hermitian specialization of IT.37–IT.39's parametric
construction class (BM.22 species; AT.56–58 anatomy); (ii) PARAMETRIC — ρ_B, ε_q undeclared
[IT.5(1)]; (iii) newly BARRED as a formed read — 𝔮-inhomogeneous (det sums 𝔮¹ with 𝔮⁰) and every
scalar invariant is a cross-currency sum/difference [BM.83(3),(9); IT.4(3); BM.140(5)]; (iv) the
handshake-seat claim REFUTED [IT.4(2); BM.134(5)]; (v) the grading map REFUTED on the canon's own
basis (the J₂/K₁/K₃ vs W₂ cross-cut); (vi) the derivative asymmetry SEATLESS (symmetric
independence; the nonzero direction would be a barred conversion + an unissued declaration).
**NOT ADOPTED. No declaration issues. §Cal-IT stays empty. No new open row.**

If the Architect ever wants M as a derived object, THREE declaration acts would be owed (none
forced, none issued): a mass² scale to homogenize the determinant; a functional link ρ_B(ε_q)
(a cross-currency conversion — the bar itself); and the restriction of any S/T force reading to
AT.56's 8-dim algebra.

## Check ledger (`cross_currency_matrix.py`, 19/19)

| # | marker | content |
|---|---|---|
| A1 | tensor product | the directive's 4×4 = the Kronecker rule, entrywise (16/16 symbolic) |
| A2 | seat census | ρ_B ε_q at exactly (2,3),(3,2); det coefficient −1; discriminant +4 |
| A3 | 𝔮-grading | entries {0, ½}; det {0, 1}; discriminant {0, 1}; IT.37 contrast {½}/{1} |
| A4 | alphabet census | generators disjoint; the three formed mixed loci carry ¬both slots |
| B1 | S-T split | S+T = M⊗M, S^T=S, T^T=−T (16/16 each) |
| B2 | content claims | the S/T entries verified; T's (1,4) factorization correction |
| B3 | the gem | ι(M)=M^T; ι(M⊗M)=(M⊗M)^T; ι(S)=S; ι(T)=−T |
| B4 | Pauli layer | v₀..v₃; all 16 C_μν = v_μ v_ν; 12/16 factor count; C₁₁+C₂₂ = 4ρ_B ε_q |
| C1 | B3 grading | the swap conjugation re-certified on the canon's basis |
| C2 | cross-cut | S-odd ∩ transpose-even = {J₂,K₁,K₃}; S-even ∩ transpose-odd = {W₂} |
| C3 | dimensions | 10+6 both ways; joint refinement 7+3+3+3 (numerology flag) |
| C4 | bivectors | 2/6 transpose-odd; σ^{12} swap image ∝ none of the six |
| C5 | force algebra | S: 4 outside directions; T: 4 outside [IT.38(2) carried over] |
| D1 | slot census | no formed read contains both slots; no both-partials-nonzero read |
| D2 | asymmetry | both formal partials vanish; m_hid, Δx_B ε_q-free; 𝓦_channel contrast |
| D3 | anchor | Δx_B·r_s = 𝔥²/(2ln2) exactly, alphabet {𝔥, ln2}; the bypass direction corrected |
| E1 | species | M − M† ≠ 0; v₂ purely imaginary; the 2/3/4-slot species line |
| E2 | m_S | read (a) = the BM.70 floor at equality; read (b) barred trace [IT.4(3)] |
| E3 | verdict | support(S∪T) = 16 of 16 directions: zero new operators, zero new loci — Scenario B |
