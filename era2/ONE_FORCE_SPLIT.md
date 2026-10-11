# THE SPLIT IS A SECTOR READ, NOT A FORCE SWITCH

> **§V's prediction is corrected by `MAGNETIC_READ.md`.** I wrote that `w_i = 0` makes the
> derived leading order "purely electric" and framed `N^i ≠ 0` as needing the weak aspect.
> **BM.34(4) calls `w=0` a GAUGE**, and BM.34(1) forms `N_i = Ω²ϰβw_i` generally, so a
> nonzero shift is admissible and its whole structure is derived. What stands: §III's proof
> that the metric's 10 components split 7+3 along CT1.1's `(S,T)` boundary and that the
> shift is T-odd *by index structure*; and §I's three grounds against isolating an aspect.


**Supersedes `MAGNETISM_ROUTE.md` §§IV–VI.** Verified by `era2/one_force.py` — **22/22 exact**,
complex-over-`Fraction`, every generator constructed from the 16 Pauli-tensor basis elements.
Running Level 5 total: **133 exact checks, 0 failures.**

---

## I. The error, named precisely

I wrote *"a purely EM configuration (`w_i = 0`)"* and concluded *"magnetism requires the weak
aspect to be active."* That is **three** separate inadmissibilities, not one:

**(a) A8 forbids it outright.** `[Summary:6300; BM.52(1); FT.142(2)]`

> `F = F₍₊,ℛ₎ ⊕ F₍₋,ℛ₎ ⊕ F₍₊,𝒱₎ ⊕ F₍₋,𝒱₎ ⊕ F_st` **always applies in full** — *no
> sub-block restriction is an A8 force.*

**(b) There is no rung at which EM is active and W is not.** A8's own content puts EM in the
**static** block, `F_st = F_EM ⊕ F_strong ⊕ F_{D⁻}`, and CT0.13's ladder is

```
A(0) = {J}      A(1) = {J, G, W, H, D+}      A(2) = A(1) u {EM}      A(3) = A(2) u {strong}
EM in A(2),  EM not in A(1),  EM not in A(0)                        [EM.1]
```

`𝒜(2) = 𝒜(1) ∪ {EM}` **contains W**. And CT0.14's masks are strictly nested
(`dim 𝒦₀=6 < 𝒦₁=16 < 𝒦₂=17 < 𝒦₃=25`), so "EM without W" is not a mask either.

**(c) The metric's coordinates are apportioned jointly.** CT1.12a(2):

```
g_{mu nu} <-> h^_{ij} (5, G: spin-2 shear) (+) Sigma_tr (1, H: volume mode)
              (+) a_{00} (1, D+: Omega conformal) (+) w_i (3, W: shift)
              1 + 1 + 5 + 3 = 10 = 4*5/2
```

Zeroing the 3 shift components while keeping a metric is a **coordinate truncation**, not a
solution of the dictionary.

**This is the same restriction error as the mass ceilings.** FT.76(3), FT.79(2), FT.84(5b) all
came from restricting to one *read species*; here I restricted to one *force aspect*. The
reusable discipline rule, which BM.56 already states:

> **Per-aspect contributions are formed reads** — "the complete force operator splits the rows
> by exactly one sector." **Applying one aspect in isolation produces symmetry breakage.**

---

## II. What survives unchanged

`em_split.py`'s algebra is untouched and stays exact:

```
E_i = (1/N)( F_{i0} - N^j F_{ij} )            90 component witnesses
one F, one metric, five exact rational observers:
    E^2 varies by ~3000x   while   I1 = -68881/88200 and I2 = -158/105 are IDENTICAL
```

E and B are readings of one `F` against one observer's normal. That part was right.

---

## III. The correction, derived from the Pauli basis

Construct `G_{μν} = σ_μ ⊗ σ_ν` (16 elements), the swap `S`, and `T(σ_μ⊗σ_ν) = η^μη^ν` with
`η = (−,+,+,+)` [A3; Convention C13]. Then:

**CT1.1 reproduced:** `[S,T] = 0`; `ℌ(ℂ⁴) = ℰ_{++} ⊕ ℰ_{+-} ⊕ ℰ_{-+} ⊕ ℰ_{--}` with
dims **(7, 3, 3, 3)**, sum 16. `T` is diagonal in the basis: T-even = `(0,0)` + the nine
`(i,j)` = 10; T-odd = the three `(0,i)` + the three `(i,0)` = 6.

**CT0.12's dictionary, generator by generator** — each sector computed, not assumed:

| generator | `S` | `T` | sector | canon aspect |
|---|---|---|---|---|
| `E_0` | + | + | `ℰ_{++}` | `D⁺` |
| `Σ = Σσ_i⊗σ_i` | + | + | `ℰ_{++}` | `H` |
| `ĥ_{ij}` | + | + | `ℰ_{++}` | `G` |
| `W_i = ½(σ_0⊗σ_i + σ_i⊗σ_0)` | + | − | `ℰ_{+-}` | `W` |
| `J_i` (antisym. spatial) | − | + | `ℰ_{-+}` | `J⁺` |
| `K_i = ½(σ_0⊗σ_i − σ_i⊗σ_0)` | − | − | `ℰ_{--}` | `J⁻` |

All six match. Plus `[W_i,W_j] = iε_{ijk}W_k` exact over `ℚ(i)`; `ΣW_i² = 2Π_ℛ`
(Casimir 2 = 1(1+1), the spin-1 read); `W_iΠ_𝒱 = 0 = Π_𝒱W_i`; `𝔗Π_ℛ = 3 ≠ 1 = 𝔗Π_𝒱`.
Capacity match `3(J⁺)+3(J⁻)+5(G)+3(W)+1(H)+1(D⁺) = 16 = C_cap`.

### The result that reframes everything

Classify the metric's own 10 independent components by **the same grading**:

| components | `T` | `S` | sector | count |
|---|---|---|---|---|
| `g₀₀` | even (`η⁰η⁰ = +1`) | even (`μ=ν`) | `ℰ_{++}` | 1 |
| `g_{ij}` symmetric | even (`ηⁱηʲ = +1`) | even | `ℰ_{++}` | 6 |
| **`g_{0i} = g_{i0}`** | **odd (`η⁰ηⁱ = −1`)** | even (symmetry of `g`) | **`ℰ_{+-}`** | **3** |
| | | | **total** | **10** |

```
[EXACT] the metric's 10 components sit EXACTLY in the S-even subspace E_++ (+) E_+-  (7 + 3)
[EXACT] CT1.12a(2)'s apportionment IS CT1.1's block boundary:
        5(G)+1(H)+1(D+) = 7 = dim E_++,   and   3(W) = 3 = dim E_+-
[EXACT] THE SHIFT g_0i IS THE ENTIRE T-ODD S-EVEN BLOCK -- T-odd by INDEX STRUCTURE
        (exactly one temporal index), not by attribution to a force
[EXACT] the S-odd blocks J^+- carry ZERO metric coordinates (a symmetric g has no S-odd part)
```

**So the shift is not "the weak field."** It is the metric's T-odd sector, and it is T-odd
because `g_{0i}` has exactly one temporal index and `η⁰ηⁱ = −1`. The *name* "W" is
CT1.12's dictionary attribution. Reading from the rung-2/EM vantage, spin- and chiral-like
content is **weak-attributable** — your phrasing, and it is exactly what the block structure
says. From the sector vantage it is simply the T-odd block of the one force.

---

## IV. The flicker dissolves the 0-vs-nonzero dichotomy

```
BM.19(6)      E(X) has more than one member  <=>  x_- > 0  <=>  eps_q > 0;
              "at every admissible nonzero threshold the neutron and the proton are
               ensembles"; the member is "a stationary mixture of real and virtual
               content ... NOT a fixed topology"
Def-BM.5(3)   p = x_+/(x_+ + x_-) = 1 - 4 eps_q   identically, on eps_q in [0, 1/4)
BM.89         w(0) = 1 exactly;  0 < w(eps_q) <= 1, strictly decreasing;
              marked specialization w = 1 - 4 eps_q
CT1.12a(2)    the metric data live ENTIRELY in the S-even blocks; the S-odd (Janus)
              blocks carry ZERO metric coordinates
```

The metric — shift included — is sourced by the **real** register, whose weight in the
stationary mixture is `p = 1 − 4ε_q`. So the shift's magnitude is **continuous in `ε_q`**,
maximal at `w(0) = 1` and attenuated as the flicker spreads. A subnetwork is never completely
real or completely virtual; **`ε_q` is what separates the energy states.**

| `ε_q` | `p = 1−4ε_q` | |
|---|---|---|
| 0 | 1 | fully crystallized; `ℰ(X)` collapses to one member [Def-BM.5(5)] |
| 1/100 | 24/25 | |
| 1/16 | 3/4 | |
| 1/8 | 1/2 | |
| 3/16 | 1/4 | |
| → 1/4⁻ | → 0⁺ | admissible supremum [CT0.8]; never attained |

There is no on/off switch and no configuration that is purely real or purely virtual.

---

## V. The corrected statement

> The metric's 10 coordinates decompose under the **same `(S,T)` grading as the one force**:
> **7 in `ℰ_{++}`** (`g₀₀`, `g_{ij}`) and **3 in `ℰ_{+-}`** (`g_{0i}` — the shift). The
> observer-relativity of the E/B split enters **exclusively through the T-odd block**, because
> that is the only block with exactly one temporal index. That is an **index fact**, not a
> force attribution. Since A8's operator always applies in full, the T-odd sector is *always*
> part of the force; what varies is its coefficient, and that coefficient is modulated
> continuously by the flicker weight `w(ε_q)`, `w(0) = 1`.
>
> The "0 vs nonzero" I reported is the **sector-level split**, and the physical parameter is
> **`ε_q`**.

---

## VI. The route, restated

```
(M1') Compute the PER-SECTOR CONTRIBUTION to the shift on a formed 2- or 3-chain
      configuration. Permitted: BM.56 -- "the complete force operator splits the rows by
      exactly one sector". Barred: APPLYING one sector in isolation.
      Objects in hand: H_2 dim 4(|k1|+1)(|k2|+1) [Def-BM.16]; H_n with the S_n action at
      every n [BM.136(3)]; the two-chain ensemble measure [BM.137]; T_J^2 dim 16(|k|+1)^2
      [Def-BM.18(4)]; the ternary charge Q in {-1,0,+1} [EM.9, D3.4].
(M2)  Split F against each chain's own n^mu_(a), coarse-grained at its own
      Delta_x_B^(a) = h/(E_int^(a) ln2) -- so the two chains read F at DIFFERENT envelope
      scales, a second and independent source of observer-relativity.
(M3)  The relative read IS the magnetic interaction. It must reduce to BM.48(1)'s
      V(d) = -eps_EM/d as eps_q -> 0 (where w -> 1 and the ensemble collapses to the single
      crystallized configuration) and correct it as eps_q grows. Matter-side coupling is the
      shift drag N^i p_i [BM.42(4)(ii)]; no new interaction term is needed.
(M4)  The 4-way sync is the aspect matching: the split is nontrivial only in E_+-, so the
      sync matches that one sector across chains at two envelope scales. The four aspects
      are A8's, and dim T_J(c) = 4(|k|+1) -- the 4 is Janus(2) x orientation(2).
```

**Prediction, restated and still sharp.** The magnetic read is a **continuous function of
`ε_q`**, maximal at `ε_q = 0` and attenuated by `w(ε_q) = 1 − 4ε_q`. It is never exactly
absent (A8) and never independently switchable (no sub-block restriction is an A8 force).
The observable knob is the crystallization threshold — the corpus's **one** ensemble
parameter [D0.4: admissible on `[0, ¼)`, sharp choice `ε_q = 0`].

That is testable against the corpus's own rows and it is a *structural* claim about one
force, not a restatement of SM bookkeeping.

---

## VII. What P5.4 is actually for

Not magnetism. The **orbital** structure is complete: conserved `∂_μM^{μνλ} = 0`, the Lagrange
identity ⟹ `p² = p_r² + L²/r²`, `r²E² = r²m² + r²p_r² + L²`, the SO(3) budget
`j_n = j_p ⊕ J_{ℓν} ⊕ L_orb` [BM.42(1)–(3)], and the shift drag `N^ip_i` [BM.42(4)(ii)].
P5.4 — the frame section and a global Dirac-type operator — is needed for the **anomalous**
moment, i.e. the spin–field coupling. And BM.125(4) already pre-refutes the naive product
ansatz `m(j) = μ̂'ℓ_c√(G(c)Δ(j))` on three independent grounds, so that door is closed in
advance. The magnetic moment is reached through the **split**, not through a Pauli term.

---

## VIII. Check ledger

`era2/one_force.py` — **22/22 EXACT**:

- CT1.1's `(7,3,3,3)` and `[S,T]=0`, from `η = (−,+,+,+)`
- all six generators' `(S,T)` sectors, computed, matching CT0.12's dictionary
- `[W_i,W_j] = iε_{ijk}W_k`; `ΣW_i² = 2Π_ℛ`; `W_iΠ_𝒱 = 0 = Π_𝒱W_i`; `𝔗Π_ℛ=3≠1=𝔗Π_𝒱`
- capacity match `3+3+5+3+1+1 = 16 = C_cap`
- **the metric's 10 components = 7 (`ℰ_{++}`) + 3 (`ℰ_{+-}`), the 3-block being exactly `g_{0i}`**
- S-odd blocks carry zero metric coordinates
- `𝒜(2) = 𝒜(1) ∪ {EM}` ⟹ no rung with EM active and W inactive; `dim 𝒦` strictly nested
- `p = 1−4ε_q` strictly decreasing on `[0,¼)`, `p(0) = 1` exact

**Adopted:** nothing. **Declared:** nothing. No P4 addition, no new dimensionful scale, no
measured value, no species identification. **Corrected:** the "purely EM / weak required"
reading, withdrawn as an A8 sub-block restriction. **New:** the proof that CT1.12a(2)'s
`5+1+1+3` apportionment *is* CT1.1's `(7,3)+(3)` block boundary, so the shift is T-odd by
index structure; and the relocation of magnetism's parameter from a force switch to **`ε_q`**.
