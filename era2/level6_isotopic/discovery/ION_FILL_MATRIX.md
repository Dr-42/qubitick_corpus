# ION_FILL_MATRIX.md — the session-13k working record (Tier IT.15 candidate, IT.46–IT.48)

**Directive (Architect, session 13k).** *"Audit the 4x4 Capacity-Bound Calibration Matrix, the
Parametric Ion Fills, and the 'Relative Information Flux' Renormalization … M₄ = M⊗M (dimension 16,
matching the capacity bound C_cap=16), filled parametrically … Baryon side: m_L(N) = 2N·u,
ρ_B(N) = ρ₀N, μ_B(N) = μ₀N; lepton side: ε_q(n_e) = ε₀n_e, m_S(n_e) = m₀n_e, σ_e(n_e) = σ₀n_e …
Ions: 'H+' (N=3, n_e=0), 'H' (3,1), 'H−' (3,2), 'He2+' (6,0), 'He+' (6,1), 'He' (6,2) … the
dimensional tension is resolved by the ratio ρ_Bε_q/(m_Lm_S) (interface cost vs self-cost), which is
dimensionless … the cost of crystallizing a qubit is the eigenvalue structure for single-node vs
multi-node systems … Scenario A (reconciliation) or Scenario B (refutation)."*

**Machine.** `checks/ion_fill_matrix.py` → **13/13 EXACT**, no floating point, no measured value
(multivariate Laurent polynomials over Gauss(i) over `Fraction`; formal partials; Faddeev–LeVerrier
characteristic polynomials over the polynomial ring — independently sanity-tested on diag(1,2,3,4) →
[1,−10,35,−50,24] and on a nilpotent witness → λ⁴; integer/binomial censuses; species labels stay
quoted).

**Erratum first (the house discipline):** the session-13j premise audit found that the IT.14 checker
had encoded the 𝓑_ens locus with the round-trip weight x₊x₋ = 4ε_q(1−4ε_q) instead of **BM.137(1)'s
u := 1−p = 4ε_q**. Verdict-neutral (the censuses there are alphabet-level and ε_q is the only flicker
symbol in either form) — but the checker is the record, so it was fixed in its own commit
(`ff4cf49`) and re-run 19/19 green before any new content. The distinction matters HERE: the
directive's fill m_L(N) = 2N·u uses BM.137's u, which makes the fill **exactly** the leading
numerator fragment of the formed ensemble binding.

---

## 0. Stance

The object enters as a conjecture. Tier IT.14's rows (IT.43–IT.45) are cited as existing record, not
re-litigated; the new content is the fills, the ratio claim, the cost claim, and the re-visited
derivative claim. Every one is checked against the frozen canon and the Level-6 record before
anything is built. Seven premise corrections are logged (P1–P7 below); the rows win.

## A. The fills vs the derived forms they name (→ IT.46)

**The skeleton is real — and it is the ONLY derived part.** The disjoint E_int read of the 1p-kn
family is E_int = 6(k+1) with N = 3(k+1) [IT.6(1); IT.7] ⟹ **E_int = 2N exactly** (integer census
k = 0..12), so m_L(derived) = E_int·ln2/𝔥 = 2N·(ln2/𝔥) [FT.44(4)]. The fill m_L(N) = 2N·u keeps the
skeleton and **swaps the scale factor**: ln2/𝔥 (shared currency {𝔥, ln2}, degree 𝔮^{1/2}) → u = 4ε_q
(lepton currency {ε_q}, degree 𝔮⁰) — machine-exact at the joint. Same skeleton, different species.

**The fragment identification.** With u = 4ε_q and D_n = 1+u+⋯+u^{n−1}, the formed ensemble binding
is 𝓑_ens^(n) = −(2n·u·D_{n−1}/D_n)·(ln2/𝔥) ≤ 0 [BM.137(1),(3); norm-layer read, IT.34(1)]. The
fill's m_L = 2N·u is that numerator with the **sign flipped**, the **D-ratio stripped**, and the
**norm-layer scale ln2/𝔥 stripped**. BM.137(3)'s hinge identity D_n − 1 = u·D_{n−1} verified as a
polynomial identity for n = 2,3,4. Exact rational witness at ε_q = 1/16 (u = 1/4): fragment 2n·u =
+1 > 0 vs 𝓑_ens^(2)·(𝔥/ln2) = −4/5 < 0. Binding is not mass [FT.79(5); prices ¬ masses, HistLog
§V.32]. (If u is instead meant as a sixth undeclared slot, the fill is worse: one more declaration
owed.)

**Contradiction census (machine):**

| the fill | the derived row it names | the contradiction |
|---|---|---|
| ρ_B(N) = ρ₀N | ρ_B = μ̂'²𝔥²/(ln2)², a fixed 𝔮⁰ restatement [BM.83(4)] | the derived ρ_B is N-INDEPENDENT (formal partial 0); the fill adds an N-law no formed read has |
| ε_q(n_e) = ε₀n_e | ε_q is ONE global A4-threshold slot [BM.19(2): "no P-class datum enters"; D0.4; IT.4(2)] | the ion table gives the single global slot THREE values (0, ε₀, 2ε₀) and pins every bare nucleus to the sharp crystallization point ε_q = 0 [BM.19(3)] **as a law, not a limit** |
| σ_e(n_e) = σ₀n_e | σ_e ∈ {−1,+1} is the DERIVED registration sign [CT0.9; IT.1(3)(R1)] | the fill's value at n_e=0 is 0 — outside the derived value census; or it restates σ_ℓ = μ_ℓ𝔥/ln2 [BM.83(4)] with a new slot |
| μ_B(N) = μ₀N | if μ_B = μ̂'², then BM.83(4) forces ρ₀ = μ₀𝔥²/(ln2)² | a constraint between slots the fill calls independent — either the derived identity breaks or the slot count is wrong; and μ_B enters NO entry of M₄ |
| (both μ_B, σ_e) | — | **decorative**: the M₄ entry alphabet is exactly {N, n_e, ρ₀, ε₀, m₀} (machine) |
| domain | ε_q ∈ [0,¼) [CT0.8] | at n_e = 2: ε₀ < ⅛ EXACTLY — an undeclared constraint strictly below AT-O27's five-ways distinguished value ⅛ |

**The ion table vs the derived N-ladder.** N = 3 per nucleon [IT.6(1): N = 3(k+1) for 1p-kn;
IT.12(1): the N=9 doublet = the two 3-nucleon species] — census (N, nucleons) = (3,1),(6,2),(9,3),
(12,4). So the quoted "He2+" at N=6 is a **two-nucleon** configuration class (g(6) = 25 groupings
[IT.9(2)]; the Q=+2 charge class exists: W₆(+2) = C(12,8) = 495; Σ_Q W₆(Q) = 4096 [IT.9(1)]), while
the 4-nucleon "He-4" system sits at A=4, **N=12** [IT.31(4),(5): ε=(−1)^A=+1; g(12)=164395,
δ-dominant]. Labels stay quoted [P5; Def-BM.3(7)], but the label→N map contradicts the ladder. And
the electron-saturated members are **¬constructed** — the IT.4-exception row is "to be derived,
¬assumed, at its own locus" [Tier IT.2 status row; IT.8(3)]: **n_e has no derived standing as a
ledger variable.**

**The 𝔮-dilemma (two horns, both machine-checked).** HORN 1 (keep the derived names):
deg(ρ_Bε_q) − deg(m_Lm_S) = 0 − 1 = **−1** — the ratio is 𝔮^{−1}, NOT dimensionless (the
directive's claim is false by BM.83(4)'s exponent arithmetic), and det/(m_Lm_S) = 1 − ratio is
inhomogeneous {0,−1}: the ratio trick divides the SAME barred sum through. HORN 2 (keep the fills):
every entry becomes 𝔮⁰ — "homogeneous", but then no entry of the "mass matrix" carries mass
(deg(m_L^{derived}) = ½ vs deg(fill) = 0). Unfilled, M₄'s entries span THREE degrees {0, ½, 1}: the
tensor product **spreads** the mismatch. And C_cap = 16 = D_tick(3) = 2^{3+1} (the junction capacity
with the lock biconditional, re-censused n = 0..6 [CT0.6; CT0.12; CT0.13; IT.1(1)]) vs dim End(ℂ⁴) =
4² = 16 (an entry count): no derived row connects the two sixteens — numerology [BM.134(5)
discipline; IT.44(3) pattern]; IT.38(2)'s 16-vs-8 over-count carries over.

## B. The "relative information flux" (→ IT.47)

**Not a formed read.** BM.83(5)'s localization theorem enumerates EVERY formed cross-currency mass
ratio and proves each depends on exactly (ρ_B, σ_ℓ, σ_ν) "and in no others" — machine: ε_q appears
in NONE of the three formed ratio slot-sets {σ_ℓ,z_ℓ,E}, {σ_ν,σ_ℓ}, {E,σ_ℓ,z_ℓ,ρ_B,ℛ_s}; it enters
no formed cross-currency ratio [IT.4(2),(4): the formed mixed loci are exactly three; the atomic
ladder fixes lepton slots only]. The ratio ρ_Bε_q/(m_Lm_S) is formable ONLY as a symbolic expression
with undeclared slots [IT.4(3)'s reduced-mass doctrine]. "Interface cost / self-cost / relative
information flux" has no ledger primitive: the ledger's information reads are I_hid ∈ ℤ·ln2 [IT.2(4)]
and the integer prices [HistLog §V.32]; the only "flux" on record is IT.14(2)'s adopted
**curvature-flux Q-value read** — a different object (name collision flagged).

## C. The "crystallization cost" (→ IT.47)

**Circular and blind (machine).** At n_e = 0 the fill gives ε_q = 0 ⟹ u = 0 ⟹ m_L = m_S = 0 ⟹
M = [[0, ρ₀N],[0,0]] is NILPOTENT (M² = 0 symbolically) and charpoly(M₄) = λ⁴ EXACTLY
(Faddeev–LeVerrier over the polynomial ring) — **identically for "H+" (N=3) and "He2+" (N=6)**: the
characteristic polynomial carries no N at all. The "single-node cost" cannot see the only baryon
datum — a read that cannot fail carries no information (the house non-vacuity order). At n_e = 1:
tr M = 8Nε₀ + m₀, det M = Nε₀(8m₀ − ρ₀), tr(M₄) = (tr M)², det(M₄) = (det M)⁴ (verified
symbolically) — so the entire "bare nucleus vs neutral atom" spectral contrast is the fill's own law
ε_q = ε₀n_e zeroing u at n_e = 0, **read back as a spectrum**.

**Crystallization needs no eigenvalue story** — it is already derived: ε_q = 0 ⟹ x₋ = 0 ⟹ ¬a
dissolution move ⟹ the crystallized configuration [BM.19(3); Def-BM.5(5)]; 𝓦_channel = 1 iff ε_q=0
∧ NE ≥ 𝒯₀ [BM.122(3)]; P_mat(E=4) = 1 at the no-flicker collapse [BM.137(2)]. The proposed Def-H.32
mapping is the **already-adjudicated ill-posed form**: "amplitudes over grouping sectors" [IT.26;
AT.41(3): the colour grouping is an independent register; Def-H.32(5): the amplitude is
(q,S)-sectored]; IT-O2's binding VALUE needs the three named constructions [IT.27(2)] — none
supplied. Eigenvalue-splitting-as-binding-energy is the smooth-manifold mass-matrix story the bars
exclude [FT.79(5): amplitude ≠ mass; IT.34(1): the binding is norm-layer; IT.39(2)'s BEC pattern:
the statistics is the exchange sign, ¬an eigenvalue].

## D. The derivative asymmetry, re-visited (→ IT.48)

**The verdict stands — and the fill smuggles the declaration it needs.** On the fill's own algebra
N and n_e remain independent counters and ρ₀, ε₀ independent slots: every formal partial of ρ_B(fill)
wrt a lepton variable and of ε_q(fill) wrt a baryon variable vanishes — IT.44(5),(6)'s symmetric
independence is untouched. BUT m_L(fill) = 8N·ε₀·n_e has **nonzero** formal partials wrt ε₀ and n_e
(machine: ∂m_L/∂ε₀ = 8N·n_e): the fill MANUFACTURES a baryon-named read that depends on the lepton
slot — a stipulated cross-currency functional LAW, exactly the declared conversion BM.140(5) bars
("no derived equation converts them") and IT.45(5)(ii) named as an owed declaration — none issued.
**The fill does not discover the asymmetry; it assumes it.**

**The "constant acceleration" is correct formal calculus and vacuous.** In the adapted coordinates
Σ = ρ_B+ε_q, Δ = ρ_B−ε_q (a formal linear change of variables): S₁₄ = ½(ρ_B²+ε_q²) = (Σ²+Δ²)/4,
∂S₁₄/∂Δ = Δ/2, ∂²S₁₄/∂Δ² = ½ — the directive's identities verified exactly. But the same
computation on T₁₄ = Σ·Δ/2 gives ∂²T₁₄/∂Δ² = 0: the "acceleration" measures the quadratic form's
normalization in adapted coordinates, not a ledger property — and S₁₄ remains a cross-currency SUM
under every fill [IT.43(4),(6)]: the bar is inherited by every derivative read of it.

## E. The verdict (→ IT.48): SCENARIO B (refutation)

Five new undeclared P4-class slots (ρ₀, ε₀, m₀, μ₀, σ₀ — six with a slot-u) [BM.6(4)] dressing
derived names in forms the derived rows contradict; the only derived content is the integer skeleton
E_int = 2N, re-scaled with a lepton-currency factor; the ratio unformed and 𝔮^{−1} under the true
degrees; the cost circular and N-blind; the derivative independence standing, with the fill
smuggling the conversion; C_cap-vs-16 numerology. **NOT ADOPTED; no declaration; §Cal-IT empty; no
new open row** — the ion-fill family is a parametric subclass of IT.37–39/IT.43–45's construction
class. The declared door for ion-indexed calibration data is the Calibration Era's own program
[IT.5(2): multi-seal EM-bound spectroscopy the necessary data species; IT.33: the anchor as
strategy; AT.63(4): deferred] with the read rules (M1′)–(M3′) [AT.54(6)] gating every conversion —
values by declared reads, ¬by parametric-matrix eigenvalues.

## Check ledger (`ion_fill_matrix.py`, 13/13)

| # | marker | content |
|---|---|---|
| A1 | degree spread | M₄ unfilled spans degrees {0, ½, 1}; det {0,1} — the mismatch spreads |
| A2 | two horns | deg(ratio) = −1 (horn 1, "dimensionless" FALSE); fills ⟹ all degrees 0 but no mass (horn 2) |
| A3 | the two sixteens | the lock biconditional census n=0..6; C_cap vs 4² — numerology flag |
| B1 | the skeleton | E_int = 2N (k=0..12); the scale-factor substitution ln2/𝔥 → u = 4ε_q at the joint |
| B2 | the fragment | D_n − 1 = u·D_{n−1} (n=2,3,4); the sign witness +1 vs −4/5 at ε_q=1/16 |
| B3 | contradictions | ρ_B N-independence; three ε_q values of one global slot; σ_e = 0 ∉ {±1}; the ρ₀/μ₀ constraint; decorative slots; ε₀ < ⅛ |
| B4 | the N-ladder | (3,1),(6,2),(9,3),(12,4); W₆(+2)=495; ΣW₆=4096; "He-4" at N=12 [IT.31(4),(5)] |
| C1 | localization | ε_q in none of BM.83(5)'s three formed-ratio slot-sets — the ratio is unformed |
| C2 | nilpotency | M²=0 and charpoly(M₄)=λ⁴ at n_e=0 — identically for both bare ions; N-blind |
| C3 | circularity | tr M = 8Nε₀+m₀, det M = Nε₀(8m₀−ρ₀); tr(M₄)=(trM)², det(M₄)=(detM)⁴ — the contrast is the fill's law read back |
| D1+D2 | derivatives | independence persists (all cross-partials of ρ_B, ε_q vanish); ∂m_L^{fill}/∂ε₀ = 8N·n_e ≠ 0 — the smuggled declaration |
| D3 | acceleration | S₁₄ = (Σ²+Δ²)/4, ∂²/∂Δ² = ½ ✓; T₁₄ witness ∂²/∂Δ² = 0 — correct and vacuous |
| D4 | verdict | Scenario B — the composite assembly on all machine findings |
