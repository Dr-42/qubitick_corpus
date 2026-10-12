# THE COHERENCE CENSUS — Level 5 (rev. 2)

**Thesis:** *1 network, 1 force, 1 metric.* **Verdict: it holds, exactly.**
**Checks: 95 exact, 0 failures.** One genuine coherence defect found in the canon (§V).

**Engine:** `era2/qexact.py` + `validate_against_canon.py`, `census_L5.py`,
`coherence_census.py`, `beta31.py`, `verify_spin_stats.py`.
Exact arithmetic only — `Fraction`, `ℤ[x]`, multivariate `ℚ[γ,G,a]`, exact 4×4 matrices
over `Fraction`, the prime-log ring `ℚ[ln2,ln3]`, rigorous `Fraction` intervals.
No floating point in any assertion.

---

## 0. Corrections to my own prior work

| # | what I said | what the canon says | status |
|---|---|---|---|
| 1 | `𝗀(G)=1/(1+G)` was unadopted (A.1 Count 3) | **BM.133(4) selects it** by S1 (unconditional Lyapunov contractivity) ∧ S2 (minimal lapse-domain loss) | **retracted** — A.1 had the right `𝗀` |
| 2 | currencies "fall short" by 695.5× / 544.0× | §V.32 + Def-H.39: `r²`, `D_S`, `E_int` are **prices**, not masses | **withdrawn** — category error |
| 3 | spin–statistics absent, "0 hits" | **BM.129, BM.136, Def-BM.16 derive it**; residue (R7) discharged at n=2, (R7′) closed at every n | **retracted** |
| 4 | magnetism "hard-blocked", no angular momentum | **BM.42** gives conserved `M^{μνλ}`, the Lagrange identity, `p²=p_r²+L²/r²`, SO(3) coupling | **retracted in part** — see §VI |
| 5 | continuum limit noted only as BM.150 | **BM.146–152** is a whole tier with an exact closed form | **understated** |
| 6 | `D_S/4E²` column | divided by `4E_int²`; canon uses `4E²`, `E` = **undirected** edges | **off by 4×**, fixed |

The pattern in all six: I read an *early* locus and treated it as final. The corpus
supersedes downstream (FT.89→FT.158; BM.88→BM.133; Def-H.39→BM.35). Lesson applied:
**read the Summary of Record and the closing tiers first, and treat every "absent /
deficit / ¬constructed" as level-local until the era-final tier says otherwise.**

---

## I. The spine (25/25 coherent)

```
L1        V(K~) = T(K~^2) >= 0,  V = 0 <=> rho = I/4,  tick-invariant under A6 Haar
L1(3)     V' - V = -gamma(8-gamma) sum mu_i^2 + O(drho^3)
BM.51     (1-gamma/4)^2 + gamma(8-gamma)/16 = 1        EXACT IDENTITY in Q[gamma]
Def-H.40  V_{E_int} = (1-gamma/4)^{2E_int} V_0 ;  gamma=1 -> (9/16)^{E_int} V_0
L3(2)     V = 16|drho|^2 + O(drho^3) = 8 DeltaS_pair + O(drho^3)
L3(4)     m_i^2(q) := DeltaS(q)                        the Lyapunov-contraction read
BM.35     m_rest := DeltaS_L / h = E_int ln2 / h        the operative composite mass
```

Verified: the contraction law expands to literally `1`; at `γ ∈ {0,¼,½,¾,1}` the pairs
`(c, decay)` are `(1,0), (15/16,31/256), (7/8,15/64), (13/16,87/256), (3/4,7/16)`, each with
`c²+decay = 1` exactly. `(9/16)^10 = 3486784401/1099511627776`.

**The registry collapses.** `V = 8ΔS` makes Def-H.39 species **(3) and (5) the same read**:
`m_i² = ΔS = V/8` *is* `m_i² = V_eff/8`. So five "species" are one operative mass, one
formed equation (species 1), one leading match (species 2), and two prices (species 4 +
the sector routes).

---

## II. β₃₁ constructed — the one link Def-H.39 called unconstructed (17/17 exact)

Built the branch states as exact 4×4 matrices from A3's swap grading:
`Π_ℛ=(I+SWAP)/2` (rank 3), `Π_𝒱=(I−SWAP)/2` (rank 1); `ρ_𝒱=Π_𝒱` (pure), `ρ_ℛ=Π_ℛ/3`.
Reproduced **FT.107(2) exactly**: `|δρ|² = (¾, 1/12)`, leading deficits `(3/2, 1/6)`.

Then the exact relative entropies, in the prime-log ring:

```
S(rho_V || I/4) = ln4       = 2 ln2
S(rho_R || I/4) = ln4 - ln3 = ln(4/3) = 2 ln2 - ln3
```

**The obstruction is real and provable:** L4's deficits are rational, FT.17's per-edge count
is `ln2`, and no rational multiple of a rational equals `ln2`. A bridge on the *leading-order*
deficit can never close. **Its cause:** L3(1) is a cubic-remainder approximation and the branch
states sit at `μ = ¾` — the *boundary* of L1's range `[−¼,¾]` — where it is worst (8.2% and
42.1% error). On the **exact** entropy the reconciliation is forced:

```
FT.17           I_hid = E_int ln2,  aspect-blind
Def-BM.5(4)     E_int = 2 E_bidir + E_uni        a bidirectional channel = TWO directed edges
                S(rho_V||I/4) = ln4 = 2 ln2 = 2 x (ln2 per directed edge)
```

**(a)** the power of `𝔥` is `+1`, uniquely: `m_hid = ΔS_𝔏/𝔥 ⟺ m_i² = 𝔥·m_hid`, and
`[𝔥·m_hid] = 𝔮^{−1/2}·𝔮^{+1/2} = 𝔮⁰ =` nats. **(b)** the per-edge coefficient is `ln2`,
forced. **(c)** the locus is Def-H.40's chain composition at its sharp point.

```
        beta_31 = h,   coefficient ln2,   DeltaS_L = I_hid = E_int ln2
```

which is BM.35 verbatim. Def-H.39 sits in **Part 3**, BM.35 in **Part 4**, and the era-chain
law forbids Part 3 citing Part 4 — so the slot was correctly marked at its own locus.
**A citation-direction artifact, not a structural gap.**

**Boundary on this result (important).** `β₃₁` closes inertial↔informational only. The
*pole*↔informational bridge is `(R1)/ρ_B = μ̂'²𝔥²/(ln2)²`, slot **(C-BM.1)**, value ¬issued —
and **BM.140(5)/BM.83(2)–(4) prove the currencies incommensurable** (`ln1280/ln960 ∉ ℚ`,
"no derived equation converts them"). So `ρ_B` is **irreducibly calibration**; it can never be
derived. `β₃₁` must not be read as reaching the pole currency.

### Bonus: BM.91's `ln(4/3)` has a provenance
`Δm·𝔥 = ln(4/3) − 3Nw𝗀ε_EM ln2`. The first term is **exactly** `S(ρ_ℛ‖¼I)` — the real-branch
Lyapunov deficit — and the second is BM.89's self-energy on the same `E_int=6` junction, the
`3` being `(2)+(2)+(2)`. Both terms of the neutron–proton splitting are structurally sourced.
The canon does not state this.

---

## III. Spin–statistics is derived (34/34 exact)

```
BM.124(1)   Theta = 2k = 4j on the nonnegative cone;  inverse j = |Theta|/4
BM.124(2)   m in {k,k-2,...,-k},  #m = k+1 = 2j+1,  Casimir j(j+1)
BM.124(3)   Delta(m) = 2 - 2 T_|m|(cos(Theta_R/2));  T_m(1/2) = cos(m pi/3) six-cycle verified
BM.124(6)   k even <=> 0 in the ladder;  Delta(0) = 0 EXACTLY at every Theta_R
            PARITY ROW: the ladder carries an exact massless weight PRECISELY WHEN
                        the exchange sign is +1   (k even <=> eps = (-1)^k = +1)
Def-BM.16   H_2 = H_w(c1)(x)Psi(c1) (x) H_w(c2)(x)Psi(c2),  dim = 4(|k1|+1)(|k2|+1)
            H_meson = H_2(c, c^CP),  dim = 4(|k|+1)^2
            P^_12 = mu^_CP o S^_12,  P^_12^2 = id
            eps(c) = mu_CP(c)|_{v^2} = i^{Theta(c)} = (-1)^{|k(c)|}
BM.129(1)   k_M = 2k  =>  eps_M = (-1)^{|2k|} = +1  and  j_M = k in Z
            THE MESON IS A BOSON, UNCONDITIONALLY
BM.129(2)   robust: k(c^CP) = -k(c) gives k_M = 0, eps_M = +1 -- statistics robust,
            total spin NOT (j_M = k vs 0)
BM.129(3)   closed connector: eps_M = (-1)^d, the connector's parity alone
BM.136(2)   the intertwiner theorem: P^_sigma|_sealed = sgn(sigma) -- the S_3 action
            IS the colour 3-vertex read on slots
BM.136(3)   H_n, dim = 2^n prod(|k_a|+1);  P_s P_t = P_{st};  chi(sigma) = d^{c(sigma)}
            eps(Gamma) = prod_a eps(c_a) at EVERY n        (R7') CLOSED
BM.136(4)a  the floor (1,1,1): eps_B = (-1)^3 = -1, j_B = 3/2 -- both named baryon
            classes FERMIONIC at E_int = 6, derived
```

**Pauli exclusion is derived, not assumed:** `dim ∧ⁿ(ℂ²) = C(2,n) = 0` for all `n ≥ 3`, on
the 2-dimensional carrier `H_v ≅ ℂ²` [BM.136(3) wedge rows]. Alongside `dim ∧³(ℂ³) = 1` and
`dim Inv((ℂ³)^⊗4) = 0` ⟹ *"four colour slots admit no singlet: the N≥4 sealings must mix
δ and ε blocks."*

**The statistics census, unified.** BM.136(4)(b) reports two convention-dependent counts,
`112/104` (variant B) and `140/76` (variant A), over `6³ = 216`. I reproduced **both exactly**
and found the single law behind them:

```
        #fermionic = 3*o*e^2 + o^3,      o = #odd-valued states,  e = 6 - o
        o = 5  ->  140   (variant A,  k = (3,2,3,3,5,3))
        o = 4  ->  112   (variant B,  k = (3,2,3,2,3,5))
```

The canon states these as two machine counts; they are one closed formula. A-BM.11 pins `o`.

---

## IV. The continuum limit is derived, and it *is* the "1 metric" (exact)

BM.146(3) gives the chart read of a cell as an exact closed form in `(E_int, r, 𝔥, ln2, ε_q)`:

```
C(E_int, r) = ( g_munu, N(k,E), T(k,E), w_mat^(n), Gamma(E,r) )

g_munu = eta_munu + (h E_int / 2r) 1_4 + O(h^2 E_int^2 / r^2)     [BM.43(4), BM.132(2)]
N      = sqrt(1 - h E_int/(2r))                                    [BM.132(2)]
T      = T_0/N = (E_int h/ln2)(1 - h E_int/(2r))^{-1/2}             [BM.115(1), BM.132(5)]
Gamma  = Gamma_tr * f * N * g * N_cal * chi                         [BM.116(1), BM.133(4)]
```

**The coherence check that closes "1 metric."** BM.132 states the lapse in the *envelope-ratio*
coordinate, `N² = 1 − G/(4πk)`, with `G = 2πE_int²ln2` and `k = rE_int ln2/𝔥`. Substituting:

```
G/(4 pi k) = (2 pi E_int^2 ln2) / (4 pi * r E_int ln2 / h) = h E_int / (2 r)      IDENTICALLY
```

Verified at 20 `(E_int, r)` cells — **all identical**. So BM.132's envelope lapse and BM.146's
Schwarzschild-type lapse are *the same function*: `r_s = 𝔥E_int/2`, `N² = 1 − r_s/r`. One
metric, two coordinate readings.

**The Newton lock is `E_int`-independent, exactly:**

```
Delta_x_B * r_s = (h/(E_int ln2)) * (h E_int/2) = h^2/(2 ln2)      -- E_int CANCELS
=> G_N = h^2/(4 ln2)        from the single scale, no second dimensionful input
```

Formed domain (BM.146(4)), all four conditions exact: `(C1) E_int ≥ 2`; `(C2) ϰ‖q‖_op < 1`;
`(C3) E_int ≤ 2r/𝔥`; `(C4) n(v) ≤ 3`. And BM.146(5): `E_crit(r) = 2r/𝔥 → ∞` as `𝔥→0` with
`𝔥₀ = 2r/E_int` **explicit**, `#{real edges per cell} ≥ 2sE_int ln2/𝔥 → ∞` — the witness by
which **BM.151 derives CT2.6(ii)–(iii) and empties the extra-axiomatic list.**

---

## V. COHERENCE DEFECT FOUND — BM.140(6), a sign error in a boxed statement

BM.82(3) [Part4:4976] states, with `𝖼 := cos(π/10)`:

```
R_max/R_min = R_2/R_5 = (1/36)/((2-2c)/3600) = 100/(2-2c) = 50/(1-c) = 1021.586454727
```
and its Pf clears `x⁴ − 1200x³ + 190000x² − 8000000x + 100000000 = 0`. **Both verified here.**

BM.140(3) then redefines `𝔲 := 2cos(π/10)`, `𝔲⁴−5𝔲²+5 = 0`, `D_S = 2−𝔲` — self-consistent.
But **BM.140(6)** [Part4:9273; Summary:9677] re-cites the span as

```
R_max/R_min = 50/(1-u)          <-- u substituted for c, unadjusted
             = -55.425426963    NEGATIVE
```

**Provably false, with no measurement used:**

1. `ℛ_s = D_S/(4E²)`, `D_S = 4sin²(δ_v/4) > 0` since `0 < δ_v < 2π`, `E ∈ {6,12,30} > 0`
   ⟹ `ℛ_max/ℛ_min > 0` **strictly**.
2. `𝔲 = 2cos(π/10) > 1` because `cos(π/10) > ½ ⟺ π/10 < π/3 ⟺ 3 < 10`. Enclosure confirms
   `𝔲 − 1 = 0.902113033 > 0`.
3. ⟹ `1−𝔲 < 0` ⟹ `50/(1−𝔲) < 0`.
4. A strictly positive quantity cannot equal a strictly negative one. ∎

**Correct form under BM.140's own `𝔲`:** `50/(1 − 𝔲/2) = 100/(2−𝔲) = 1021.586454727`, equal to
BM.82(3) exactly.

**Why 80/80 stays green:** the span value and the quartic coefficients `1200 / 190000 / 8000000`
appear **nowhere** in `verification/checks/`. BM.82(3) is the checked source; **BM.140(6) is an
unchecked re-citation.** This is precisely the defect class a coherence census exists to catch —
a sign error inside a `\boxed{}` statement, which any downstream consumer would inherit.

**Loci to fix:** `Part4_Baryomesonic_era.md:9273` and `Summary.md:9677` (generated).
**Not defective:** Part4:4976 (BM.82(3)); Part4:5303 / Summary:7678, which use `𝖼 = cos(π/10)`
correctly and also record `25 = (E(F₃)/E(F₁))² = (30/6)²`.
**Suggested checker:** assert `(1−𝔲) < 0` and `ℛ_max/ℛ_min > 0` are disjoint — a two-line
exact test that fails on the current text and passes on the fix.

---

## VI. The official Level 5 agenda — BM.143(7)'s demand rows

The canon already names what Part 5 requires. My independent analysis landed on the same two
top rows, which is a useful cross-check:

| row | demand | state after this census |
|---|---|---|
| **P5.1** | the EM binding channel — ¬∃ an EM sealing grammar; the lepton–baryon bound state is a dynamics-of-`Q` object | **open.** BM.48(1)–(2) banked `V(d)=−ε_EM/d`, `E₂/E₁=¼`. Needs P5.2 |
| **P5.2** | the lepton mass read: `E_int^(ℓ)`, `E_int^(ν)` ¬computed at any floor; `m_r` requires it | **open, and now has a candidate** — §VII |
| **P5.3** | dynamics rates, tick-rate/field coupling; emergent time a named prerequisite | open; BM.131(7)'s reparametrization read is the formed piece |
| **P5.4** | the frame section and a global Dirac-type operator | **open — this is the real magnetic-moment blocker**, not angular momentum |
| **P5.5** | generation/flavour selection — (R3)'s occupancy half | open; BM.136(5) names it for the Part-5 ledger |
| P5.6–P5.10 | item 16(c) cells; (R4′) ensemble refinement; `n≥4` sealing cells; finite-`𝔥` residue at clean-bifurcation loci; the embedding datum | open |

**On magnetism, corrected.** BM.42 already supplies `M^{μνλ} = x^νT^{μλ} − x^λT^{μν}` with
`∂_μM^{μνλ} = 0` on-shell (all 64 components verified on the dust class), the Lagrange identity
`r²δ^{ij}p_ip_j = (x·p)² + Σ_{i<j}(x_ip_j − x_jp_i)²`, hence **`p² = p_r² + L²/r²`** and the
decomposed dispersion `r²E² = r²m² + r²p_r² + L²`; the SO(3) budget `j_n = j_p ⊕ J_{ℓν} ⊕ L_orb`;
and spin's two derived metric couplings — the rest read (pole mass = spin-connection holonomy
defect) and the moving body's **shift drag `N^ip_i`, the shift being the weak block**.
So *orbital* structure is available. What P5.4 lacks is the frame section and a global
Dirac-type operator — i.e. the `σ^{μν}` for the **anomalous** moment. BM.125(4) also refutes
the product form `m(j) = μ̂'ℓ_c√(G(c)Δ(j))` on three independent grounds, so the naive
"spin × metric" ansatz is barred in advance.

---

## VII. The candidate for P5.2, now sharpened

Def-BM.14(6)'s order-isomorphism argument — *"two exact three-element ordered sets admit
exactly one order-isomorphism"* — is **channel-agnostic**. It is stated for the q-channel, but
all three channels' lines are strictly ordered and enclosure-proven [FT.113 ℓ; FT.119(5) q;
FT.143(1),(3) ν], and the three floors are strictly ordered [Def-BM.14(1)]. So all nine lines
inherit

```
gen 1 -> F_1 -> E_int = 12      gen 2 -> F_2 -> E_int = 24      gen 3 -> F_3 -> E_int = 60
```

and with it `Δx_B`, `G`, `g(G)`, `T₀`, `r_s = 𝔥E_int/2` and a BM.89 self-energy.

**Status: `C-sharp`.** It is not a fitted claim — it is the unique order-isomorphism the canon
already proved, applied where the canon did not apply it. It is falsifiable: it predicts the
informational ladder is exactly `1:2:5` while the amplitude price runs `1:3.56:139.34` (q) and
`1:206.77:3477.47` (ℓ). Since §V.32 says the amplitude reads are *prices* and not masses, that
disagreement is **not** a refutation — but it does force the question of which read carries the
family hierarchy and which carries the splitting, and BM.125(3)'s matching identity
`μ̂'²Θ_R²/4 = μ̂²ℓ_c²G(c)` is the only derived relation between a pole-side and a leading-side
quantity. That is where P5.2 meets P5.1.

*Caveat carried:* Def-BM.14(6) says "the map is an order, ¬a number," and BM.140(5) proves the
currencies incommensurable. So the isomorphism may supply `E_int` **as a ledger label** without
supplying a mass — which is enough for `Δx_B`, `G`, `T₀` and `r_s` (all keyed on `E_int` alone)
but not enough for `m_r`. Splitting those two uses is the first thing P5.2 must decide.

---

## VIII. Check ledger

| script | scope | result |
|---|---|---|
| `validate_against_canon.py` | FT.63(4),(6), BM.81(1), BM.60(2), BM.115(2) from cardinals | **ALL PASS** |
| `census_L5.py` Stage 1 | FT.113, FT.114(1)(2), FT.119(3)(5), FT.120(4)(7)(8), FT.76(3) | **19/19** |
| `coherence_census.py` | the spine, registry collapse, BM.133 S1/S2, the coupling, 1-1-1 | **25/25** |
| `beta31.py` | branch states, exact entropies, the obstruction, the construction | **17/17** |
| `verify_spin_stats.py` | BM.124/125/129/136, Def-BM.16, BM.140(1)–(4),(6), the `4E²` fix | **34/34** |

**Total 95 exact checks, 0 failures.** Errors caught by the gates rather than by assertion: a
malformed 7-field cardinal tuple; `γ=¾` decay `87/256` (not `39/256`); a missing `Poly.__eq__`;
and my own `4E_int²`-vs-`4E²` factor-of-4.

**Adopted:** nothing. **Declared:** nothing. **Quarantined:** every `[EXT]` value remains a
target, never an input.

**New at Level 5:** `β₃₁ = 𝔥` with coefficient `ln2` forced; the exact branch entropies `ln4`
and `ln(4/3)`; the provenance of BM.91's transport term; the closed statistics law
`3oe²+o³`; the identity `G/(4πk) ≡ 𝔥E_int/(2r)` unifying BM.132 and BM.146; the
`E_int`-independent Newton lock `G_N = 𝔥²/(4ln2)`; the channel-agnostic extension of
Def-BM.14(6); and **one coherence defect in the canon (BM.140(6)), with an exact proof and a
two-line checker suggestion.**
