# THE MAGNETIC READ IS FORMED — BM.34 was the missing block

**Supersedes:** `MAGNETISM_ROUTE.md` §§IV–VI, `ONE_FORCE_SPLIT.md` §V, `M1_SHIFT.md` §F(5).
**Verified by:** `era2/m1ppp_bm34.py` (13/13) and `era2/m1pp_shift.py` (20/20), exact arithmetic.
**Level 5 total: 196 exact checks, 0 failures.**

---

## 0. Two withdrawals, on the record

**(i) "The corpus never forms a non-diagonal metric" — WITHDRAWN.** I had not read **BM.34**.
It derives the full ADM split with a *live* shift and explicitly names `w=0` a **gauge**:

> BM.34(1): `γ_{ij} = Ω²(δ_{ij}+ϰq_{ij})`, `N_i = Ω²ϰβw_i`, `N^i = γ^{ij}N_j`,
> `N² = Ω² + γ^{ij}N_iN_j`, **`N²det γ = −det g`** [Schur], and
> `g^{00} = −1/N²`, `g^{0i} = N^i/N²`, `g^{ij} = γ^{ij} − N^iN^j/N²`.
>
> BM.34(4): *"the gauges: `w=0`: `E² = N²(m²+p²)`; `Ω=1 ∧ w=0`: `E² = m²+p²`."*

**(ii) "`w_i = 0` is forced on every formed cell" — OVERSTATED, corrected.** It is forced on
**BM.146(3)'s** continuum-limit cell (whose metric `η + (𝔥E_int/2r)𝟙₄` is diagonal, so
`g_{00} = −N²` and ADM gives `N_iN^i = 0`). But that cell **is** the `w=0` gauge of BM.34(4) —
a specialization, not a theorem about formed configurations. Verified at five
`(E_int, r)` cells: `−g_{00} = N²` exactly ⟹ `N_iN^i = 0` ⟹ `ϰβw_i = 0` (since
`Ω² = e^{2α_Ωa_{00}} > 0` for every `a_{00} ∈ ℝ`, CT1.12).

**What stands from the earlier documents:** the disjoint-alphabet refutation of `⟨w_i⟩`;
the B=2 pincer `m₂² = 0`; the Jensen identity `⟨G⟩/G(⟨E⟩) = 1 + p(1−p)/2 ∈ [1, 9/8]`; and the
proof that the metric's 10 components split `7+3` along CT1.1's `(S,T)` boundary with the shift
T-odd *by index structure*.

---

## I. BM.34 reproduced exactly, and reconciled with CT1.12

60 exact rational witnesses over `(Ω², ϰ, β, w_i, q_{ij})`:

| verified | result |
|---|---|
| **Schur identity** `N²det γ = −det g` | exact ✓ |
| **ADM inverse** `g^{00}=−1/N²`, `g^{0i}=N^i/N²`, `g^{ij}=γ^{ij}−N^iN^j/N²` | exact ✓ |
| **BM.34(1) ≡ CT1.12's conformal form** | exact ✓ — see below |
| `N² = Ω² + γ^{ij}N_iN_j ≥ Ω²`, equality iff `w = 0` | exact ✓ |

The third row is a **coherence result**: BM.34(1)'s ADM data are *identically* CT1.12's
`g_{μν} = Ω²ḡ_{μν}` with

```
gbar_00 = -1,     gbar_0i = kappa beta w_i,     gbar_ij = delta_ij + kappa q_ij
```

So the two loci are **one metric in two coordinate readings** — CT1.12 conformal, BM.34 ADM.
That is the `1 metric` claim verified at the level of the field parametrisation, not just the
lapse. (Cross-check: `g_{0i} = Ω²ϰβw_i` is FT.157(1) verbatim.)

## II. The dispersion already carries the magnetic coupling

BM.34(4)'s master identity, verified as an **exact equivalence** (not a mere agreement of two
falsity conditions):

```
N^2 * ( g^{mu nu} p_mu p_nu + m^2 )  +  [ (E + N^i p_i)^2 - N^2(m^2 + p^2) ]  ==  0
identically, with E := -p_0
```

using `g^{mn}p_mp_n = −(1/N²)(E+N^ip_i)² + p²`, which follows from BM.34(1)'s ADM inverse. Hence

```
        E = N sqrt(m^2 + p^2) - N^i p_i
```

and BM.34(3)'s momentum `p_i = m u⁰ g_{ij}(dx^j/dx⁰ + N^j)` with `g_{ij}N^j = N_i = g_{0i}
= Ω²ϰβw_i`. BM.34(3) states the structural point in its own words:

> *"the drag term and the metric's time–space block are **the same three coefficients `w_i`** —
> the weak aspect, one block, two derived reads."*

**So the matter-side magnetic coupling is already formed.** The dispersion carries the
observer-relative term `−N^ip_i`; the field side carries the same `w_i` through
`E_i = (1/N)(F_{i0} − N^jF_{ij})`. **No Pauli term. No Dirac operator. P5.4 is not the door.**

## III. The new result: the split breaks a degeneracy the dispersion preserves

BM.34(3)–(4)'s T-parity, verified at 60 witnesses:

```
w -> -w   =>   N_i -> -N_i,   N^i -> -N^i,   (N, gamma_ij) FIXED
the mass shell is invariant under the SIMULTANEOUS  (N^i, p_i) -> (-N^i, -p_i)
   [p_i is T-odd, matching its carrier w_i -- BM.34(3); BM.8(1)]
```

**So the dispersion cannot distinguish `w` from `−w`** — `p_i` flips with it. But the E/B split
*can*, because `F_{ij}` is held fixed:

```
E_i(N) - E_i(-N) = -(2/N) N^j F_{ij}
```

which is nonzero exactly when the mixing is nonzero.

> **The E/B split is the first formed read in the corpus that is odd under `w → −w` alone.**
> The mass shell, the lapse, the spatial metric and the dispersion are all blind to the sign
> of the shift; the split is not. That makes the magnetic read a **genuinely new observable**
> — not a repackaging of an existing one — and it is already formed.

This is also why magnetism could not be reached from the mass reads: every mass read the corpus
has is T-even in the shift. The degeneracy is exact and it is broken only by `F`.

## IV. The Jacobian: why the *value* of `w_i` is undetermined

`dŝ²(e) = (Ω²/𝔥²)[−(Δx⁰)² + 2ϰβw_iΔx⁰Δx^i + (δ_{ij}+ϰq_{ij})Δx^iΔx^j]`, so exactly

```
d dshat^2 / d w_i  =  (2 kappa beta Omega^2 / h^2) * Dx^0 * Dx^i
```

and **Summary:4931 supplies the kind of `Δx⁰`: "a tick increment [D1.8]" — ledger data**, with
the corpus's own witness `ds² = g_{00}(Δx⁰)²` on purely temporal increments.

| edge type | Jacobian row | constrains `w_i`? |
|---|---|---|
| purely temporal (`Δx^i = 0`) | `[0,0,0]` — **vanishes** | no — the corpus's own witness |
| purely spatial (`Δx⁰ = 0`) | `[0,0,0]` — **vanishes** | no |
| **mixed** (both ≠ 0) | `(2ϰβΩ²/𝔥²)Δx⁰Δx^i` — nonzero | **yes, the only case** |

The on-shell winding `Θ(c) = Σ_e dŝ²(e) = 2k ∈ 2ℤ` [FT.22] supplies at most **one** integer
equation per independent closed chain, i.e. per `β₁` [FT.63(2): `β₁ = F−1`; FT.46(2): `β₁(n)=n+1`].
Against `3E` shift coordinates:

| floor | `E` | shift coords `3E` | `β₁` | **rank deficit** | free |
|---|---|---|---|---|---|
| tetrahedron | 6 | 18 | 3 | **15** | 15/18 |
| cube | 12 | 36 | 5 | **31** | 31/36 |
| octahedron | 12 | 36 | 7 | **29** | 29/36 |
| dodecahedron | 30 | 90 | 11 | **79** | 79/90 |
| icosahedron | 30 | 90 | 19 | **71** | 71/90 |
| polygon `P_n` | n | 3n | n+1 | **2n−1** | — |

Total unconstrained shift dimensions across the five Platonic floors: **225**.

So Summary:3427(3) is exactly right and I now have the quantitative form of it: *"the datum
exists in principle, **the coupling does not**."* No formed ledger read can determine `w_i`.

---

## V. The corrected disposition

| | | |
|---|---|---|
| **`⟨w_i⟩`** | **¬formed** | disjoint alphabets: the ensemble index is `E_int ∈ ℤ`, `w_i ∈ ℝ³` per edge [M1′] |
| **the shift's structure** | **FORMED** | BM.34(1)–(4): ADM split, Schur identity, drag, dispersion, T-parity |
| **the magnetic coupling, matter side** | **FORMED** | `−N^ip_i` in BM.34(4); same three coefficients as `g_{0i}` [BM.34(3)] |
| **the magnetic read, field side** | **FORMED** | `E_i = (1/N)(F_{i0} − N^jF_{ij})`; `F_{μν}` from EM.12's plaquette circulation |
| **the magnetic observable** | **NEW and formed** | the first read odd under `w → −w` alone (§III) |
| **the value of `w_i`** | **UNDETERMINED** | rank deficit ≥ 15; needs mixed edges |
| **`β`** | **calibration** | P4 core, value ¬issued [§Cal-2]; disposition `(C-BM.1)`-shaped, irreducible |

> **The magnetic read is structurally FORMED and numerically UNDETERMINED.** It needs no Dirac
> operator and no Pauli term. It needs **(i)** a formed configuration with **mixed edges**
> (`Δx⁰ ≠ 0` and `Δx^i ≠ 0`), and **(ii)** a value for `β`.

**(i) is a combinatorial ledger question, machine-checkable, with no calibration input:** does
any *materialized* chain traverse both a tick increment and a spatial displacement on one edge?
The relevant inventory is CT1.19a's null / spacelike / timelike trichotomy
(`dŝ²(e) = 0 ⟺ Δx_e null`; trivial chain [D1.7] = all-null-edge chain), FT.24–FT.25's integer
on-shell `dŝ²`, and Def-BM.4(5)'s minimal materialized element `dŝ² = 1 ⟹ ds² = 𝔥²`.

**(ii) is irreducibly calibration** — the same disposition as `ρ_B`, and BM.140(5)/BM.83's
incommensurability theorem means it can never be derived.

---

## VI. What this does to the Part-5 agenda

BM.143(7)'s demand rows, re-graded against what is now known:

| row | BM.143's grading | corrected grading |
|---|---|---|
| **P5.4** frame section + global Dirac-type operator | the magnetic-moment blocker | **not** the blocker for magnetism. Needed for the *anomalous* moment's spin–field coupling, and BM.125(4) already pre-refutes the naive product ansatz on three grounds |
| **P5.1** EM binding channel | open | open; BM.48(1)–(2) banked `V(d)=−ε_EM/d`, `E₂/E₁=¼` |
| **P5.2** lepton mass read `E_int^(ℓ)`, `E_int^(ν)` | open | open; the channel-agnostic order-isomorphism supplies an `E_int` **label** but BM.140(5)'s incommensurability blocks a **mass** |
| **P5.3** dynamics rates, tick-rate/field coupling | open | **promoted**: `Δx⁰` *is* a tick increment [D1.8], so P5.3 is exactly where the mixed-edge question lives |
| — **new row** | — | **the mixed-edge census**: which materialized chains carry `Δx⁰ ≠ 0 ∧ Δx^i ≠ 0`. Decides whether the magnetic read is ever nonzero on a formed configuration |

**The critical path has moved.** It is not P5.4 and not P5.2. It is the **mixed-edge census** —
a purely combinatorial question about tick and spatial increments on materialized edges,
machine-checkable from the existing inventory, with no calibration value and no new datum. If
mixed edges exist on materialized chains, the magnetic read is nonzero and Level 5 has its first
genuinely new observable. If every materialized edge is purely temporal or purely spatial, then
`∂dŝ²/∂w_i ≡ 0` on the whole on-shell locus, the shift is unobservable at every order, and the
magnetic sector is **absent by theorem** — which is also a clean result, and a much stronger one
than "not yet constructed."

---

## VII. Check ledger

| script | scope | result |
|---|---|---|
| `validate_against_canon.py` | FT.63(4),(6), BM.81(1), BM.60(2), BM.115(2) | ALL PASS |
| `census_L5.py` | FT.113, FT.114(1)(2), FT.119(3)(5), FT.120(4)(7)(8), FT.76(3) | 19/19 |
| `coherence_census.py` | the spine, registry collapse, BM.133 S1∧S2, the coupling, 1-1-1 | 25/25 |
| `beta31.py` | branch states, exact entropies, the `β₃₁` construction | 17/17 |
| `verify_spin_stats.py` | BM.124/125/129/136, Def-BM.16, BM.140(1)–(4),(6), the `4E²` fix | 34/34 |
| `em_split.py` | the E/B split, one metric / five observers, the shift mixing | 16/16 |
| `one_force.py` | CT1.1 `(7,3,3,3)`, CT0.12 dictionary, the metric's 7+3 split | 22/22 |
| `m1_shift.py` | the kind census, BM.137's ensemble, the B=2 pincer, the Jensen identity | 30/30 |
| `m1pp_shift.py` | the ADM lapse bound, BM.146(3)'s zero shift, the Jacobian, the rank deficit | 20/20 |
| `m1ppp_bm34.py` | BM.34(1)–(4): Schur, ADM inverse, CT1.12 reconciliation, dispersion, T-parity | 13/13 |

**196 exact checks, 0 failures.** Errors caught by the gates rather than by assertion: a
malformed cardinal tuple; `γ=¾` decay `87/256`; a missing `Poly.__eq__`; `4E_int²` vs `4E²`;
`Poly([0,4])` read as `4x` not `4`; a cyclic-index sign error in my 3×3 inverse; and a B1 test
that was trivially satisfied until rewritten as a non-vacuous exact identity.

**Adopted:** nothing. **Declared:** nothing. No P4 addition, no new dimensionful scale, no
measured value, no species identification, no isolated aspect applied.
**Withdrawn:** "the corpus never forms a non-diagonal metric"; "`w_i = 0` forced on every formed
cell." **New:** BM.34(1) ≡ CT1.12 reconciled as one metric in two readings; the exact
mass-shell/dispersion equivalence; **the E/B split as the first formed read odd under
`w → −w` alone**; the Jacobian `∂dŝ²/∂w_i = (2ϰβΩ²/𝔥²)Δx⁰Δx^i` and its vanishing on
purely temporal and purely spatial edges; the rank deficits `3E − β₁ ≥ 15` and `2n−1`; and the
relocation of the critical path to the **mixed-edge census**.
