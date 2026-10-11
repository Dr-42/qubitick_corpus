# M1′ — the shift on a formed two-chain configuration

> **PARTIALLY SUPERSEDED by `MAGNETIC_READ.md`.** §F(5)'s framing "the magnetic read is
> unformed" is too strong. **BM.34** — which I had not read — forms the full ADM split with
> a *live* shift and calls `w=0` a **gauge** [BM.34(4)]. The structure is formed; only the
> *value* of `w_i` is undetermined. Parts A–E (the disjoint-alphabet refutation of `⟨w_i⟩`,
> the B=2 pincer, and the Jensen identity `⟨G⟩/G(⟨E⟩) = 1 + p(1−p)/2`) all stand.


**Directive:** compute `⟨w_i⟩` over BM.137's stationary mixture on Def-BM.18's `𝒯_𝒥²`; determine
whether it is forced nonzero on every formed configuration or vanishes for the crystallized
member at `ε_q = 0`. Both outcomes are results.

**Answer: a third option. `⟨w_i⟩` is not formed.** Not zero, not nonzero — *not a read*.
The two alphabets are disjoint. Verified by `era2/m1_shift.py`, **30/30 exact**.

Constraints honoured: no isolated aspect (every read below is of the full complex or of an
integer ledger count); `ε_q` the only knob; sector-level language with "W" as dictionary label
only; exact arithmetic, no floats; every theorem cited; sector counts machine-verified.

---

## A. The sector geometry of the shift (machine-verified from the Pauli basis)

**D2.1** [Part1:225]: `X₍₊₎ = a₀₀E₀ + q_{ij}E^{ij}`, `q_{ij}=q_{ji}`; **`X₍₋₎ = w_iW_i`**;
`Σ_tr := δ^{ij}q_{ij}`; `ĥ_{ij} := q_{ij} − ⅓δ_{ij}Σ_tr`; **`N_i := βw_i`**;
`Ω := e^{α_Ωa₀₀}`; `α_Ω, β, ϰ ∈ ℝ`.

| verified | result |
|---|---|
| `𝔗(W_iW_j) = 2δ_ij` (exact, `𝔗 = tr`, over `ℚ`) | ⟹ **`w_i = 𝔗(X₍₋₎W_i)/2`** — the projection is exact and invertible |
| `η = (−,+,+,+)` [C13]: T-even 10, T-odd 6, total 16 | `= C_cap` [CT0.14] |
| `dim_ℝ ℰ(e) = dim ℰ_{++} + dim ℰ_{+-} = 7 + 3 = 10` | [Def-H.14] |
| `1(a₀₀) + 1(Σ_tr) + 5(ĥ_{ij}) + 3(w_i) = 10 = 4·5/2` | [CT1.12; FT.30] |
| `dim_ℝ ℋ_slot^int(Σ) = 10·|Σ\∂Σ|` | [Def-H.14] |

So the shift is **3 of the 10 continuous per-edge coordinates**, and `N_i = βw_i` with `β` in the
**P4 core, value ¬issued** [§Cal-2: "`ϰ, β, α_Ω`"]. `g_{0i} = ϰβΩ²w_i` [FT.157(1)].

---

## B. The kind census — why `⟨w_i⟩` has no referent

```
THE FLICKER ENSEMBLE                       THE SHIFT
Def-BM.5(1)  E(X) = { R subset E_dir(Gamma) :    D2.1      X_(-) = w_i W_i,  w_i in R^3
             boundary data preserved on R }      Def-H.14  E(e), dim_R = 10 per real edge,
Def-BM.5(4)  E_int(R) = |R| = n_R  in Z                    CONTINUOUS
BM.19(3)     p = x_+/(x_++x_-) = 1-4 eps_q       FT.30 W-row  ARENA data: "shift w_i",
BM.137(1)    P(E=2j) = C(n,j) p^j u^{n-j}                       continuous, OFF-SHELL
             -> INTEGER-valued random variable     FT.30 W-row  SPECTRUM data: the INTEGER
                alphabet Z                                      labels k, Theta_int
                                                        -> alphabet R^3 per edge, arena
```

**Disjoint alphabets: `ℤ` vs `ℝ³`.** The ensemble's support is indexed by edge subsets `R`; it
does not range over `ℰ(e)`'s coordinates. So there is no `⟨w_i⟩` over the stationary mixture —
the measure has no `w_i` argument.

This is the *same refutation shape* the corpus already uses:
- **BM.90**: "the measure's alphabet `{ε_q}` and the defect alphabet `{δ_v, μ̂'²}` are **disjoint**
  and four independent grounds bar any count→strength coupling" — hypothesis (W) refuted.
- **BM.143(2)**: `(R2)` reclassified as a **phantom gap** — "no structure is missing, no
  selection principle is absent."
- **BM.143(1)**: `(R5)` closed as **void** — "coarse graining bounds the information flux, and no
  construction could exist inside the bound."

So `⟨w_i⟩` is a phantom read, not an open problem.

**It does not vanish at `ε_q = 0` either.** At `ε_q = 0` the ensemble collapses to the single
crystallized member [BM.19(3); Def-BM.5(5); BM.137(2): `P_mat(E=4)=1`, `w_mat=1`], but the
collapsed member *still* carries a 10-per-edge continuous arena. Collapse fixes `E_int`; it does
not fix `w_i`.

---

## C. BM.137's ensemble, reproduced exactly in `ℚ[p]`

| check | result |
|---|---|
| `(1−u)D_n = 1−u^n` for `n = 1..8`, `D_n = 1+u+⋯+u^{n−1}` | exact polynomial identity ✓ |
| `n=2`: `2u + p = 1+u = D_2` (the two materialization probabilities sum to 1) | ✓ |
| `⟨E⟩^(2)_mat = 4/(1+u) = 4/(2−p) ∈ (2,4]`; `w_mat^(2) = 1/(1+u) ∈ (½,1]` | ✓ |
| `Var^(2)/⟨E⟩^(2)2 = p(1−p)/2 ≤ 1/8`, certificate `1/8 − p(1−p)/2 = (2p−1)²/8 ≥ 0` | exact in `ℚ[p]` ✓ |
| `n=1`: `D_1 = 1` identically ⟹ `w_mat^(1) = 1` — **a single materialized pair has no flicker** | ✓ |
| `ε_q=0 ⟹ u=0 ⟹ P_mat(E=2)=0, P_mat(E=4)=1, w_mat=1` | ✓ |

---

## D. What *is* forced to vanish at the two-chain locus

**BM.137(4)'s pincer** — `𝒢₂` carries one chain-bearing skeleton, the digon `K₂`:

```
a closed chain requires |R| >= 2        [Def-H.4: delta h(c) >= 2]
the budget gives        |R| <= 2E(K_2) = 2     [Def-H.32(1)]
  =>  |R| = 2E  =>  n_V = 2E - |R| = 0  =>  DeltaS = (3/2) n_V = 0
                                            [Def-H.32(6); FT.107(2)]
  =>  m_2^2(q,S) = 0  on EVERY formed sector
      Z_2^norm(q,S) != 0 only at S = 1, with Z_2^norm = (4, 2, 2) at q = (0, +1, -1)
```

Verified: `n_𝒱 = 0`, `ΔS = 0`, `m₂² = 0`. With L4(4) — *"the read vanishes to leading order iff
`n_𝒱 = 0`"* — the **two-chain sector mass is zero at every `ε_q`, forced by the pincer, not by the
flicker.** Also verified: the transport census `W₂(Q) = C(4,Q+2) = (1,4,6,4,1)`, `Σ = 16 = 4²`,
and the CP-pair saturation `1+4+1 = 6 = W₂(0)` [BM.110(3)].

**This is the forced zero at B=2 — and it is the sector mass, not the shift.**

---

## E. What `ε_q` actually modulates, in formed reads — a new exact result

`G = 2πE_int²ln2` [BM.88(3)] is **nonlinear** in the integer `E_int`, so `⟨G⟩ ≠ G(⟨E⟩)`. The gap
is exactly the variance, and BM.137(2) supplies `Var/⟨E⟩²` in closed form:

```
<G> = 2 pi <E^2> ln2 = G(<E>) + 2 pi Var(E) ln2

        <G> / G(<E>)  =  <E^2>/<E>^2  =  1 + p(1-p)/2          EXACT identity in Q[p]
```

| `ε_q` | `p = 1−4ε_q` | `⟨G⟩/G(⟨E⟩)` |
|---|---|---|
| 0 | 1 | **1** |
| 1/16 | 3/4 | **35/32** |
| **1/8** | **1/2** | **9/8** ← maximum |
| 3/16 | 1/4 | **35/32** |
| 1/4 | 0 | **1** |

```
[EXACT] the ratio is 1 at both ends of the admissible range and maximal at 9/8, attained
        at p = 1/2, i.e. eps_q = 1/8 -- on BM.137(2)'s own certificate (2p-1)^2/8 >= 0
[EXACT] it is SYMMETRIC under p <-> 1-p, so eps_q = 1/16 and eps_q = 3/16 give the SAME
        value 35/32. That degeneracy is new and exact.
```

Second Jensen layer: `𝗀(G) = 1/(1+G)` is strictly decreasing **and convex** on `G > 0`
[BM.133(4)], so `⟨𝗀(G)⟩ ≥ 𝗀(⟨G⟩) = 𝗀(G(⟨E⟩)·(1 + p(1−p)/2))`. And the lapse
`N² = 1 − 𝔥E_int/(2r)` gives formed `⟨N⟩`, `⟨N²⟩`.

**All continuous in `ε_q`, all formed, none involving `w_i`.**

**The decisive split in the E/B read.** With `E_i = (1/N)(F_{i0} − N^jF_{ij})`:

| term | carrier | formed? | `ε_q`-dependence |
|---|---|---|---|
| `1/N` prefactor | the lapse | **yes** — `N² = 1−𝔥E_int/2r`, `E_int` is the ensemble variable | exact, via `⟨N⟩` |
| `N^jF_{ij}` mixing | the shift `N_i = βw_i` | **no** — arena `w_i` + P4-core `β`, value ¬issued | none |

So the flicker **rescales** the electric read; it does **not mix** E into B. Mixing needs the
shift, and the shift is arena + calibration data.

---

## F. Verdict, and the consequence for the magnetic read

1. **`⟨w_i⟩` is ¬formed** — disjoint alphabets (`ℤ` vs `ℝ³` per edge). A phantom read in
   BM.143's sense, refuted on BM.90's ground.
2. **It does not vanish at `ε_q = 0`** — the crystallized member still carries the
   10-per-edge arena.
3. **The forced zero at B=2 is the sector mass** `m₂² = 0` on every formed sector, by
   BM.137(4)'s pincer, at every `ε_q`.
4. **What `ε_q` modulates, exactly:** `⟨G⟩/G(⟨E⟩) = 1 + p(1−p)/2 ∈ [1, 9/8]`, maximal at
   `ε_q = 1/8`, symmetric in `p ↔ 1−p`; plus `⟨𝗀⟩ ≥ 𝗀(⟨G⟩)` and `⟨N⟩`, `⟨N²⟩`.
5. **The magnetic read is unformed for the same reason `ρ_B` is** — behind a declared
   calibration slot (`β`, P4 core, value ¬issued) *and* a read-specification act on the arena.
   **Not behind missing structure.** This is exactly the disposition shape of `(C-BM.1)/ρ_B`
   [BM.143(4)] and of `(R2)/(R5)/(R10)` [BM.143(1)–(3)].
6. **What is already a Level 5 prediction:** the Coulomb read's magnitude is `ε_q`-modulated
   through `1/N` and through the `9/8` Jensen enhancement of `G`. That is formed, exact, and
   continuous in the corpus's single ensemble parameter — a testable statement that needs no
   arena slice and no calibration value.

---

## G. M1″ — the well-posed next question

`⟨w_i⟩` cannot be averaged, but `w_i` can be **specified**. Def-H.14 says `ℰ(e)`'s coordinates
"already fix `g_{μν}(e)` [CT1.12] and hence `dŝ²(e)` [D1.6]", and BM.143(2)/BM.127(2) say
`dŝ²(e)` **is determined at crystallization** (registration data; alphabet derived [CT0.9];
per-edge value fixed [Def-EM.20, EM.20]; integer on shell [FT.24–FT.25]). So there is a map

```
E(e) -> ds^2(e),      10 -> 1,      and on shell  Theta(c) = sum_{e in c} ds^2(e) = 2k in 2Z  [FT.22]
```

The minimal admissible slice is then constrained by **five exact conditions**:

| # | condition | locus |
|---|---|---|
| (i) | `dŝ²(e)` determined at crystallization, integer on shell | BM.143(2); BM.127(2); FT.24–25 |
| (ii) | `Θ(c) = Σ_e dŝ²(e) = 2k ∈ 2ℤ` on every materialized closed chain | FT.22 |
| (iii) | stationarity: the coarse-grained `(a₀₀,q_{ij},w_i)` tick-invariant — a **declared scope**, so using it is scope inheritance, not a new datum | BM.8(2) |
| (iv) | `g_{μν}` orientation-even | CT1.12a(2); FT.23 |
| (v) | nondegeneracy `ϰ‖q‖_op < 1` | CT1.12; BM.146(4) C2 |

**Five exact constraints on a 10-per-edge arena.** Whether they determine `w_i` up to the
residual gauge — spatial diffeomorphisms, whose charge is the momentum `P_i`, itself **T-odd**
[Summary:5093: *"`N_i` is the Lagrange multiplier of the momentum constraint"*] — is
well-posed and machine-checkable. That is the real content of P5.3/P5.4, and it is reachable
without a Pauli term and without a Dirac operator.

Note the structural fit: `N_i` is the Lagrange multiplier for the constraint generated by
`P_i`, and `P_i` is T-odd — the *same* grading as `g_{0i}` and as `w_i`. The shift is the
multiplier of the T-odd momentum constraint. That is why the mixing lives in `ℰ_{+-}` and
nowhere else, and it is an index fact, not an attribution.

---

## Check ledger

`era2/m1_shift.py` — **30/30 EXACT**, no floats:

- **A** `𝔗(W_iW_j) = 2δ_ij` ⟹ `w_i = 𝔗(X₍₋₎W_i)/2`; T-even/odd = 10/6; `dim ℰ(e) = 7+3 = 10`;
  `1+1+5+3 = 10 = 4·5/2`
- **B** the alphabet census; the phantom-read disposition; the underdetermination count
- **C** `(1−u)D_n = 1−u^n` for `n=1..8`; the `n=2` rows; `Var/⟨E⟩² = p(1−p)/2 ≤ 1/8` with its
  certificate; the no-flicker collapse; `D_1 = 1`
- **D** the B=2 pincer ⟹ `n_𝒱 = ΔS = m₂² = 0`; `W₂(Q) = (1,4,6,4,1)`, `Σ=16`; CP saturation `6`
- **E** `⟨G⟩/G(⟨E⟩) = 1 + p(1−p)/2` as an identity in `ℚ[p]`; the five exact values; the
  `p ↔ 1−p` symmetry; convexity of `𝗀`; the rescale-vs-mix separation
- **F** the four verdict rows

**Level 5 running total: 163 exact checks, 0 failures** (`validate_against_canon` ALL PASS ·
`census_L5` 19/19 · `coherence_census` 25/25 · `beta31` 17/17 · `verify_spin_stats` 34/34 ·
`em_split` 16/16 · `one_force` 22/22 · `m1_shift` 30/30).

**Adopted:** nothing. **Declared:** nothing. No P4 addition, no new dimensionful scale, no
measured value, no species identification, no isolated aspect applied.
**New at L5:** the exact projection `w_i = 𝔗(X₍₋₎W_i)/2`; the disjoint-alphabet refutation of
`⟨w_i⟩`; the Jensen identity `⟨G⟩ = G(⟨E⟩)(1 + p(1−p)/2)` with its `9/8` ceiling at
`ε_q = 1/8` and its `p ↔ 1−p` degeneracy; the rescale/mix separation of the E/B split; and the
relocation of magnetism's blocker from a structural gap to **`β` (P4 core, ¬issued) plus an
arena slice**.
