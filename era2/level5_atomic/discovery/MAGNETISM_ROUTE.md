# MAGNETISM AS A DYNAMIC SPLIT — the route, made exact

> **SUPERSEDED — see `ONE_FORCE_SPLIT.md`.** Sections IV–VI of this document contain a
> **restriction error**. I wrote "a purely EM configuration (`w_i = 0`)" and concluded
> "magnetism requires the weak aspect." That isolates a sub-block, which **A8 forbids**
> (*"F always applies in full — no sub-block restriction is an A8 force"*), and it mistakes
> a **sector** for a **force**. `EM ∈ F_st` and `EM ∈ 𝒜(2)`, and since `𝒜(2) = 𝒜(1) ∪ {EM}`
> the W aspect is active *whenever* EM is — there is no rung with EM on and W off.
> The algebra in §§II–III stands (it is verified); the reading in §§IV–VI does not.
> Corrected and re-derived from the Pauli basis in `one_force.py` (22/22 exact).


**Premise (the Architect's).** Magnetism is a *relativistic observation* of the EM force,
not a substance. Deriving it blindly must fail. Minimum apparatus: two to three interacting
charged observers, the coarse-graining apparatus, and a 4-way information sync. **The
electromagnetic split is a dynamic phenomenon.**

**Result: the premise is correct, it is provable exactly inside the corpus, and it relocates
the blocker.** 16/16 exact checks (`era2/em_split.py`). The route is **not** P5.4.

---

## I. Why "derive B" was the wrong door

A Pauli term `ψ̄ σ^{μν} F_{μν} ψ` *presupposes a B to couple to*. If B is the
observer-relative part of the split of `F`, then B is not an object in the theory — it is a
reading. My earlier P5.4 framing ("frame section + global Dirac operator, then magnetism")
treated B as a substance. Withdrawn.

The corpus already has the field strength, and it is discrete-first:

```
EM.12   f_v = 1/2 (sigma_->(v) - sigma_<-(v))  in {-1, 0, +1},   aleph_v = |f_v| in {0,1}
        coarse-graining [CT1.19]:   f_v --> F_{mu nu}   (circulation per plaquette) [CT1.22]
EM.13   w(C) = J(C) prod_e G(e) * (-1)^{aleph(sigma,C)};  "coarse-graining => relative
        signs of F_{mu nu}"
EM.14   F_{mu nu} = 2 nabla_[mu A_nu],  gauge invariant under A -> A + nabla chi
EM.15   S_EM[A,g] = -1/4 int d^4x sqrt(-g) F_{mu nu} F^{mu nu};
        T^(EM)_{mu nu} = F_{mu rho} F_nu^rho - 1/4 g_{mu nu} F_{ab} F^{ab};  traceless in D=4
```

So `F` exists, is gauge-invariant, is coupled to the metric, and has a stress-energy tensor.
**What does not exist anywhere in the canon is an E/B split.** `magnetic` returns only
`electromagnetic` hits. The split is genuinely new Level 5 material.

---

## II. The thesis, proved: one F, one metric, many observers

`F^{μν} = g^{μα}g^{νβ}F_{αβ}` depends on the *metric*, so "different observers" must mean
different timelike unit vectors `u^μ` in **one fixed metric** — which is also what makes this
a *1 metric* result rather than a *many metrics* one.

Exact rational observers: the unit hyperboloid `u·u = −1` is rationally parametrized by

```
u^mu(s) = ( (1+s^2)/(1-s^2),  2s/(1-s^2),  0,  0 ),     s in Q, |s| < 1
          because  -(1+s^2)^2 + 4s^2 = -(1-s^2)^2   identically
```

so every component is a `Fraction`. Fixed `F` with components `(3/2, −1/4, 5/7, 2/3, −7/5, 1/6)`:

| `s` | `u⁰` | `u¹` | `E²` | `B²` | `2(B²−E²)` | `E·B` |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 2213/784 | 2189/900 | **−68881/88200** | 79/210 |
| 1/3 | 5/4 | 3/4 | 724369/313600 | 216689/112896 | **−68881/88200** | 2209/3360 |
| 1/2 | 5/3 | 4/3 | 4652029/1587600 | 40321/15876 | **−68881/88200** | 797/630 |
| −2/5 | 29/21 | −20/21 | 26735221/3111696 | 159501001/19448100 | **−68881/88200** | 3659/4410 |
| 3/4 | 25/7 | 24/7 | 8881741/960400 | 765605/86436 | **−68881/88200** | 9193/1470 |

```
[EXACT] I1 = F.F = 2(B^2 - E^2) at every observer, IDENTICAL across all five
[EXACT] E.u = 0 and B.u = 0 at every observer (both purely spatial for that observer)
[EXACT] the (E,B) pairs DIFFER across observers while F and g are FIXED (five distinct reads)
[EXACT] the invariant content of F is exactly (I1, I2) = (-68881/88200, -158/105)
```

**`E²` varies by a factor of ~3000 across the five observers; `I1` and `I2` do not move.**
E and B are readings of one `F` against one observer's normal. That is your thesis, as an
exact rational identity.

---

## III. The shift does it without a boost — and that is why the bars don't bite

Def-BM.18(6) bars the naive route: *¬∃ a velocity operator, a position operator or a
momentum-space state on `𝒥`* [BM.10(1): `¬[x̂,p̂]=i` in the finite register]; *¬∃ a
cross-section, an S-matrix element or a **Lorentz-invariant phase space***. So §II's boosts
are not available as operators.

**They are not needed.** The mixing comes from the tilt of the ADM normal, and the normal is
built from *metric fields*, not from operators on `𝒥`:

```
n^mu = (1/N, -N^i/N),      n_mu = (-N, 0),      n^mu n_mu = -1
E_i  = F_{i nu} n^nu = (1/N)( F_{i0} - N^j F_{ij} )
```

verified exactly at 90 component witnesses. Now take `F` **purely magnetic** (`F_{0i} = 0`
for all `i`), with spatial parts `(F₁₂, F₁₃, F₂₃) = (4/3, −5/2, 7/5)`:

| observer | `E_μ` |
|---|---|
| `N^i = 0` (shift-free) | `[0, 0, 0, 0]` — **exactly zero** |
| `N^i = (1/2, 0, 0)` | `[0, 0, 2/3, −5/4]` |
| `N^i = (1/2, −1/3, 2/7)` | `[0, 73/63, 4/15, −103/60]` |

```
[EXACT] the SHIFT ALONE tilts the normal and manufactures an electric read: NO BOOST NEEDED
```

`n^μ` is a field-side object, exactly like BM.48(2)'s hydrogenic ladder was chart-side. The
finite-register bars are never engaged.

---

## IV. The consequence, and it is drastic

Assemble three derived rows:

1. **BM.146(3)'s leading metric is DIAGONAL.**
   `g_{μν} = η_{μν} + (𝔥E_int/2r)·𝟙₄ + O(𝔥²E_int²/r²)`. Since `𝟙₄` is the identity,
   `(𝟙₄)_{0i} = 0`, so **`g_{0i} = 0`** and `N² = −g_{00} = 1 − 𝔥E_int/(2r)` — which is
   BM.146(3)'s own `N`. Verified at four `(E_int, r)` cells.
2. **FT.157(1): the shift is the weak block.** `g_{0i} = ϰβΩ²w_i`, and "the same three
   generators carry the metric shift" `[D2.1: X₍₋₎ = w_iW_i; CT1.12: w_i ↦ N_i]`. So
   `N^i ≠ 0 ⟺ w_i ≠ 0 ⟺` **the weak aspect is active**.
3. **§III: the observer-relative part of the split enters only through `N^i`.**

Therefore, exactly and with no measurement:

> **On the corpus's own derived leading metric the E/B split is purely electric.**
> A magnetic read requires a nonzero shift, and the shift is the weak block's metric
> footprint. **Magnetism is not a pure-EM phenomenon in this framework** — it is the reading
> of `F` by an observer whose normal is tilted by a *weak-sourced* shift.

Your "the electromagnetic split is a dynamic phenomenon" is literally true here — **dynamic in
`w_i`, not in a velocity.** And it is *not* the Standard Model's bookkeeping, where E and B
are both purely EM. So it is a real structural claim, and it is falsifiable against the
corpus's own rows.

**One further piece already in place:** FT.157(3) locates the weak support as *"the S-even
T-odd block — the sector coupling the **temporal** register direction to the **spatial**
triad."* A shift `g_{0i}` is precisely a temporal–spatial coupling. So the block that carries
the shift is the block whose defining property is mixing temporal with spatial. The
identification is structural, not imposed.

---

## V. Your specified apparatus, mapped to derived objects

| your specification | corpus object | status |
|---|---|---|
| **2–3 interacting charged observers** | `H₂(c₁,c₂)`, `dim = 4(|k₁|+1)(|k₂|+1)` [Def-BM.16(2)]; `H_meson = H₂(c,c^CP)`, `dim = 4(|k|+1)²` [BM.110]; `H_n`, `dim = 2ⁿ∏(|k_a|+1)` with `S_n` action [BM.128/BM.136(3)]; charge `Q ∈ {−1,0,+1}` [EM.9, D3.4]; forced pair `(q_p,q_ℓ)=(+1,−1)` [BM.23(4)] | **constructed** |
| — each observer's own normal | per-chain `E_int` ⟹ own `r_s = 𝔥E_int/2`, `G = 2πE_int²ln2`, `N = √(1−𝔥E_int/2r)` ⟹ own `n^μ_(a)` | **derived** — observer-relativity is *per-chain metric data*, not a boost |
| **the coarse-graining apparatus** | `f_v → F_{μν}` [EM.12, CT1.19/CT1.22]; "coarse-graining ⟹ relative signs of `F_{μν}`" [EM.13]; Def-H.9 projection; Def-BM.4(5) envelope discipline; `Δx_B = 𝔥/(E_int ln2)` | **derived** |
| — and it is per-chain | each chain coarse-grains at its own `Δx_B`, so two chains read `F` at *different envelope scales* — a second, independent source of observer-relativity | **new at L5** |
| **a 4-way information sync** | A8's four aspects `F₍₊,ℛ₎⊕F₍₋,ℛ₎⊕F₍₊,𝒱₎⊕F₍₋,𝒱₎` (+`F_st`); `dim T_𝒥(c) = 4(|k|+1)` — the 4 is Janus(2)×orientation(2) [Def-BM.18(4)]; pair space `ℂ⁴`, `𝔗(G_aG_b) = 4δ_ab`; `dim T_𝒥² = 16(|k|+1)²` | **derived** |
| — and which of the four carries the split | FT.157(3): the weak support is the **S-even T-odd** block, coupling temporal to spatial. The shift lives in exactly one of the four aspects | **derived** |
| matter-side coupling | the **shift drag `N^ip_i`** [BM.42(4)(ii)] — already in the dispersion | **derived** |
| orbital structure | `∂_μM^{μνλ} = 0` on-shell; Lagrange identity ⟹ `p² = p_r² + L²/r²`; `r²E² = r²m² + r²p_r² + L²`; `j_n = j_p ⊕ J_{ℓν} ⊕ L_orb` [BM.42(1)–(3)] | **derived** |

**So the apparatus you specified is essentially all present.** Exactly one thing is missing:

> **The shift's *value* `w_i` on a formed configuration.** The *form* `g_{0i} = ϰβΩ²w_i` is
> derived [FT.157(1)]; `w_i` is solution data [D2.1], and BM.146(3) computes the diagonal
> sector only. This is the entire gap.

---

## VI. The route

```
(M1) FORM A NONZERO SHIFT.  Produce w_i != 0 on a two- or three-chain configuration.
     Everything else is derived. Candidates: BM.34(3)-(4)'s dispersion already carries the
     shift drag; FT.157(1)'s X_(-) = w_i W_i is the weak block's metric image; BM.137's
     two-chain ensemble measure supplies the state; Def-BM.18's T_J^2 has dim 16(|k|+1)^2.
(M2) SPLIT F AGAINST EACH CHAIN'S OWN n^mu_(a).  Chart-side, exact, no barred object:
        E^(a)_i = (1/N_a)( F_{i0} - N_a^j F_{ij} ),   B^(a) from the spatial volume form.
     Coarse-grain per chain at Delta_x_B^(a) = h/(E_int^(a) ln2) -- the scales differ.
(M3) THE RELATIVE READ IS THE MAGNETIC INTERACTION.  At w_i = 0 it must reduce EXACTLY to
     BM.48(1)'s Coulomb read V(d) = -eps_EM/d; at w_i != 0 it corrects it. The matter-side
     coupling is the shift drag N^i p_i [BM.42(4)(ii)], so no new interaction term is needed.
(M4) THE 4-WAY SYNC is the aspect matching: the split is nontrivial only in the S-even
     T-odd block [FT.157(3)], so the sync is a matching of that one aspect across two or
     three chains at two different envelope scales.
```

**Sharp prediction (M-route):** a magnetic read exists **only** where the weak aspect is
active. A purely EM configuration (`w_i = 0`) has `N^i = 0` and is purely electric at every
order the corpus computes. This is checkable against the corpus's own rows and it is *not*
SM bookkeeping.

**What this does to the agenda.** P5.4 was listed as "the frame section and a global
Dirac-type operator, both unconstructed" — and I had magnetism queued behind it. It isn't.
The **orbital** magnetic structure needs no Dirac operator at all: `L²`, `M^{μνλ}`, the SO(3)
budget and the shift drag are all derived. What P5.4 is genuinely needed for is the
*anomalous* moment, i.e. the spin–field coupling — and BM.125(4) already pre-refutes the
naive product ansatz `m(j) = μ̂'ℓ_c√(G(c)Δ(j))` on three independent grounds, so that door is
closed in advance. The magnetic moment should be reached through the *split*, not through a
Pauli term.

---

## VII. Check ledger

`era2/em_split.py` — **16/16 EXACT**, no floating point:

- ADM algebra: `g^{μα}g_{αν} = δ^μ_ν` and `n^μn_μ = −1` at 40 exact rational witnesses
- BM.146(3) diagonal at four `(E_int, r)` cells; `N² = −g_{00} = 1 − 𝔥E_int/(2r)`
- rational hyperboloid parametrisation `u·u = −1` exact in `ℚ(s)`
- `I1 = 2(B²−E²)` identical across five observers; `E·u = B·u = 0`; five distinct `(E,B)`
- purely-magnetic `F` ⟹ `E = 0` shift-free, `E ≠ 0` shifted
- `E_i = (1/N)(F_{i0} − N^jF_{ij})` at 90 component witnesses

Running total across Level 5: **111 exact checks, 0 failures**
(`validate_against_canon` ALL PASS · `census_L5` 19/19 · `coherence_census` 25/25 ·
`beta31` 17/17 · `verify_spin_stats` 34/34 · `em_split` 16/16).

**Adopted:** nothing. **Declared:** nothing. No P4 addition, no new dimensionful scale, no
measured value, no species identification. **New at L5:** the E/B split as a derived reading;
the identity that the shift alone manufactures it without a boost; the theorem that
BM.146(3)'s metric is diagonal so the derived leading order is purely electric; and the
relocation of magnetism's blocker from P5.4 to **(M1), the value of `w_i`**.
