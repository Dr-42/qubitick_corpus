# M1‴ — THE MAGNETIC READ AS A FLICKER FUNCTIONAL

**Reframe accepted.** "Find the value of `w_i` on a formed configuration" is **withdrawn**.
Summary:3427(3) bars it: `w_i` is a functional of the ambient configuration, `C ↦ w_i(C)`
*"from per-edge sector coordinates … sampled at `O(𝔥)` [CT1.19], coarse-grained to `(M,g)`
under CT2.6's hypotheses"* — and its verdict is exact: *"the datum exists in principle,
**the coupling does not**."* There is no configuration-independent `w_i` to pin.

**Constructed instead:** the magnetic read as an ensemble average over the flicker, BM.89-style.
Verified by `era2/magnetic_functional.py` — **23/23 exact**.
**Level 5 total: 219 exact checks, 0 failures.**

---

## I. Does BM.90 reach it? The four grounds, tested

BM.90's hypothesis (W) is *"the retention probability of a registration datum depends on the
state's **defect** value, `P(edge is real | D_S)`"*. All four grounds bar that specific map:

| ground | what it bars | reaches `w_i(R)`? | verdict |
|---|---|---|---|
| **(i) field degree** | `D_S` generates a degree-16 extension of `ℚ`; the measure's reads are integer/binary, so a rational formula lands in degree < 16 | **no** — if `w_i(R)` is built from `|R|` | **evaded, and constraining** |
| **(ii) two-torsion image** | the register lift of the defect angle reaches `{0,π}` only; 4 of 6 states unreachable at every winding | **no** — `w_i(R)` never touches the defect angle | **evaded** |
| **(iii) calibration weight** | `Θ_R = 2πk` carries `𝔥`-weight −2 against 0 for a rate | **no** — `w_i` carries the dimension of `1/(ϰβ)`, not `𝔥⁻²` | **evaded** |
| **(iv) strength bar** | `¬∃` a count→strength theorem; capacity ratios `(⅓, 8, 1/25)` are `¬`couplings | **YES** — `w_i(R) ∝ |R|` *is* a count→coefficient map | **BITES** |

**The structural reason (i)–(iii) miss:** BM.90 bars conditioning the **measure** on a *pole-currency*
datum. `w_i(R)` is the opposite composition — a **read** composed with the measure. That is
precisely what BM.89(3) does with `⟨m_hid⟩_ℰ` and `m_hid(R) = |R|ln2/𝔥`. So the M1′
disjoint-alphabet objection is **dissolved**, as you said: the flicker ranges over configurations
and `w_i` is determined per configuration, whence `⟨w_i⟩_ℰ = ω_i⟨E_int⟩_ℰ` is immediate.

**Ground (i) is not merely evaded — it constrains.** It forces `w_i(R)` to be built from
integer/binary ledger reads and **bars `w_i(R) = f(D_S)`**. That is consistent with BM.90(4)'s
own conclusion: *"the six states act in the pole currency alone."*

**Ground (iv) bites, and the corpus already shows the way through.** BM.89(4) states its
crystallization weight and then: *"the Bernoulli specialization `w = 1−4ε_q` **marked and
¬adopted**"*; *"the strict decrease is derived **on the marked specialization** below, and in
general is (R4)'s content."* Ground (iv) bars a **derived** coupling; it does not bar a **marked**
specialization with derived consequences. That is what follows.

---

## II. Specialization (S) — marked, ¬adopted

> **(S) SHIFT ADDITIVITY.** On a floor whose edges are homogeneous, the coarse-grained shift is
> additive in the retained-edge count:
> ```
> w_i(R) = omega_i * E_int(R),      E_int(R) = |R|      [Def-BM.5(4)]
> ```
> with `ω_i ∈ ℝ³` a per-edge shift vector, the same on every edge of the floor.

Motivation, every row derived — **but the step itself is not**:

- **Def-H.14**: `ℰ(e)` has per-edge coordinates `(a₀₀(e), q_{ij}(e), w_i(e))`, `dim_ℝ = 10`.
  So `w_i` is natively a **per-edge** object.
- **Summary:3427(3)**: `g` comes *"from **per-edge** sector coordinates"*, sampled at `O(𝔥)`,
  coarse-grained to `(M,g)`. Coarse-graining a per-edge quantity over a homogeneous floor is a
  **sum over the retained edges**.
- **FT.22**: `Θ(c) = Σ_{e∈c} dŝ²(e) = 2k ∈ 2ℤ` — the corpus's own on-shell read is **already
  additive over edges**.
- **Census FT.66(1)**: `Aut(Γ_S)` acts by channel permutation, so on a Platonic floor every edge
  is equivalent and `ω_i` cannot depend on which edge.

Status: **marked, ¬adopted**. The exact shift analogue of BM.89's Bernoulli specialization.

---

## III. The exact ADM readout under (S), from BM.34(1)

With `M_{ij} := δ_{ij} + ϰq_{ij}`, so `γ_{ij} = Ω²M_{ij}` and `γ^{ij} = Ω^{−2}M^{ij}`:

```
N_i    = Omega^2 kappa beta omega_i E
N^i    = kappa beta E M^{ij} omega_j                       -- LINEAR in E_int
gamma^{ij} N_i N_j = Omega^2 kappa^2 beta^2 E^2 ||omega||_M^2
N^2    = Omega^2 ( 1 + c^2 E^2 ),        c := kappa beta ||omega||_M
N      = Omega sqrt(1 + c^2 E^2)
```

Verified at **72 exact rational witnesses** `(Ω², c, E)` against a direct 4×4 construction,
including `N² = −1/g^{00}`. In the vacuum spatial gauge `q_{ij}=0` ⟹ `M=I`, `‖ω‖_M = |ω|`.

Consequence for BM.34(4)'s dispersion: the drag becomes `N^ip_i = ϰβE(M^{ij}ω_j)p_i` — **also
linear in `E_int`**. So both the field-side mixing and the matter-side drag are linear in the
same ledger integer, which is what makes the ensemble average close.

---

## IV. The magnetic functional

The split's mixing term [verified in `em_split.py`]: `E_i^{mix}(R) = −(1/N(R))N^j(R)F_{ij}`.
Under (S) and the vacuum spatial gauge, writing `Φ_i := ω^jF_{ij}`:

```
        E_i^{mix}(R)  =  - (kappa beta / Omega) * psi(E_int(R)) * Phi_i
        psi(E)        :=  E / sqrt(1 + c^2 E^2)

        <E_i^{mix}>_E =  - (kappa beta / Omega) * <psi>_E(eps_q) * Phi_i
```

**All the ensemble dependence is in one scalar functional**, on BM.137(1)'s materialized law:

```
P_mat(E = 2j) = C(n,j) p^j u^{n-j} / (1 - u^n),     j >= 1
p = 1 - 4 eps_q,   u = 4 eps_q
```

> **Normalizer correction (my error, not the canon's).** I first divided by `D_n`. But
> `Σ_{j≥1}C(n,j)p^ju^{n−j} = (p+u)^n − u^n = 1 − u^n = p·D_n`, and BM.137's
> `w_mat^{(n)} = 1/D_n` is the **crystallization weight** `⟨E⟩_mat/(2n)` — not the normalizer.
> Cross-checked against BM.137(2)'s closed `n=2` rows: `P_mat(E=2) = 2u/(1+u)`,
> `P_mat(E=4) = p/(1+u)`, summing to 1, at four exact `ε_q`. ✓ `⟨E⟩_mat = 2np/(pD_n) = 2n/D_n` ✓

Sample values at `c = 1/4`, `Ω = 1`:

| `n` | `ε_q=0` | `1/16` | `1/8` | `3/16` |
|---|---|---|---|---|
| 1 | 1.788854382 | 1.788854382 | 1.788854382 | 1.788854382 |
| 2 | 2.828427125 | 2.412598028 | 2.135378630 | 1.937364774 |
| 3 | 3.328201177 | 2.894105613 | 2.454292243 | 2.083327395 |

---

## V. THE MAGNETIC ATTENUATION THEOREM

BM.89's attenuation theorem is `|E^self| ≤ |E^self|_{w=1}`, equality only at `w=1` — *"the
flicker strictly attenuates the correction."* The magnetic read has the same shape, for exact
reasons:

```
(E1)  psi(E) = E/sqrt(1+c^2E^2) is STRICTLY INCREASING in E   [disjoint enclosures, every even E in 2..60]
(E2)  psi(E) < 1/c for every finite E, and psi -> 1/c as E -> infinity   [saturation]
(E3a) <psi>_E never increases with eps_q on [0, 1/4)
(E3b) <psi>_E is STRICTLY decreasing for every n >= 2, and EXACTLY CONSTANT at n = 1
      -- "a single materialized pair has no flicker" [BM.137(1): D_1 = 1, w_mat^(1) = 1]
(E4)  |<E_i^mix>| <= |<E_i^mix>|_{eps_q=0}, equality only at eps_q = 0, and the bound is
      UNIFORM -- independent of eps_q AND of n:
          |<E_i^mix>| < (1/(Omega |omega|)) |Phi_i|
(E5)  the crystallized value has an EXACT closed form:
          c * psi(2n) = 2nc / sqrt(1 + 4 c^2 n^2)        [at c = 1/4:  n / sqrt(n^2 + 4)]
      verified at n = 1, 2, 3, 4, 6, 12, 30
```

| `n` | `c·⟨ψ⟩` at `ε_q=0` | closed form `2nc/√(1+4c²n²)` |
|---|---|---|
| 1 | 0.447213595 | `1/√5` |
| 2 | 0.707106781 | `1/√2` |
| 3 | 0.832050294 | `3/√13` |

**The crystallized magnetic read is a closed algebraic function of the pair count `n`.**

### Three consequences that reverse the naive expectation

**(F1) The flicker does not create magnetism — it attenuates it.** At `ε_q → 0` the ensemble
collapses to `E = 2n` [BM.19(3); Def-BM.5(5); BM.137(2)] and `⟨ψ⟩ → ψ(2n) ≠ 0`. **The magnetic
read is maximal at full crystallization** and monotonically attenuated by the flicker. That is
the exact opposite of the intuition that a fluctuating metric would *generate* the magnetic
sector; on this specialization the crystallized member carries the full read.

**(F2) The digon floor is flicker-blind.** At `n=1`, `D_1 = 1` and `w_mat^{(1)} = 1` identically,
so the one-pair magnetic read is `ε_q`-independent and equals `ψ(2)` exactly.

**(F3) T-parity survives the averaging.** `ω → −ω` flips `Φ_i` and hence `⟨E_i^{mix}⟩`, while
`N`, `γ_{ij}`, `ψ` and the *entire measure* are fixed [BM.34(3)]. The measure is a function of
`|R|` alone and `|R|` is T-even, **so the average cannot wash out the sign.** The magnetic read
stays odd under `w → −w` — consistent with `MAGNETIC_READ.md` §III, where the split was shown to
be the first formed read with that property.

---

## VI. What is derived, what is marked, what remains

**DERIVED — no specialization needed.** These hold for **any** additive-in-`E_int` shift
functional, so they are the specialization-robust content:

- BM.90's grounds (i)–(iii) do not reach `w_i(R)`; ground (i) is constraining and bars
  `w_i(R) = f(D_S)`.
- `N² = Ω²(1+c²E²)`, `N^i = ϰβE M^{ij}ω_j` — BM.34(1) composed with additivity.
- `ψ` strictly increasing, strictly bounded by `1/c`.
- `⟨E_int⟩_mat = 2n/D_n` strictly decreasing in `ε_q` [BM.137(1), already canon].
- ⟹ **monotone attenuation** and a **uniform bound**.
- T-oddness under `w → −w`, un-washable by the measure.

**MARKED, ¬ADOPTED** — specialization (S), the analogue of BM.89's `w = 1−4ε_q`:

- `w_i(R) = ω_iE_int(R)`; on it, the closed form `⟨E_i^{mix}⟩ = −(ϰβ/Ω)⟨ψ⟩_ℰΦ_i`, the
  attenuation theorem, the saturation `2nc/√(1+4c²n²)`, and the (F1)–(F3) limits.

**STILL REQUIRED — and unchanged by any of this:**

| item | nature | disposition |
|---|---|---|
| a value for `β` and `ϰ` | P4 core, value ¬issued [§Cal-2; C4] | **irreducibly calibration**; `(C-BM.1)/ρ_B`-shaped; BM.140(5)/BM.83 incommensurability bars derivation |
| the coupling `C ↦ w_i(C)` | Summary:3427(3): "the datum exists in principle, the coupling does not" | **read-specification / construction**; (S) is a stand-in |
| a formed configuration with **mixed edges** (`Δx⁰≠0 ∧ Δx^i≠0`) | else the on-shell winding never sees `w_i` [`m1pp_shift.py` PART C] | **combinatorial ledger question**, machine-checkable, no calibration input |

---

## VII. Answer to the directive

> *"Compute the magnetic read as an ensemble average over the flicker, BM.89-style … verify
> whether BM.90 applies or whether the configuration-functional structure evades it."*

**It is constructible, and BM.90 does not bar it.** Three of BM.90's four grounds are about
defect-conditioning the *measure* and do not reach a configuration-functional *read* at all;
the fourth bars a **derived** count→strength coupling, which is met by **marking** the
specialization rather than adopting it — exactly BM.89(4)'s own precedent. The M1′
disjoint-alphabet objection is dissolved.

The object constructed is the **magnetic transition functional**

```
        <E_i^{mix}>_E (eps_q)  =  - (kappa beta / Omega) <psi>_E(eps_q) Phi_i,
        psi(E) = E/sqrt(1+c^2E^2),   c = kappa beta ||omega||_M,   Phi_i = omega^j F_{ij}
```

which is conjugate to the momentum constraint in the sense you specified: `N_i` *is* the
Lagrange multiplier of the momentum constraint whose charge `P_i` generates spatial
diffeomorphisms and is itself T-odd [Summary:5093; BM.34(3)]. The functional is a transition
read across the ensemble, not a value on a cell — it takes the whole materialized distribution
`P_mat(E=2j)` as input and returns a single attenuated coefficient.

**It satisfies an attenuation theorem of exactly BM.89's species**, has a closed algebraic
crystallized value `2nc/√(1+4c²n²)`, is T-odd and un-washable, is flicker-blind at `n=1`, and
is **maximal at `ε_q = 0`** — so the flicker attenuates magnetism rather than sourcing it.

**The residual gap is not structural and not measure-theoretic.** It is one calibration value
(`β`, `ϰ`) plus the coupling `C ↦ w_i(C)`, whose existence Summary:3427(3) already settles in
principle. The one genuinely open *structural* question is the mixed-edge census — whether any
materialized chain traverses both a tick and a spatial displacement on one edge — because
without mixed edges the on-shell winding never constrains `w_i` at all.

---

## VIII. Check ledger

`era2/magnetic_functional.py` — **23/23 EXACT**, no floats (Fraction measure, `qexact.sqrt_iv`
rigorous intervals):

- **A** the four BM.90 grounds tested individually
- **B** specialization (S) stated with its four derived motivations
- **C** `N² = Ω²(1+c²E²)` and `N² = −1/g^{00}` at 72 exact rational witnesses against a direct
  4×4 construction
- **D** BM.137(2)'s closed `n=2` rows reproduced; the materialized weights sum to 1;
  the normalizer `1−u^n = p·D_n`
- **E** `ψ` monotone and bounded; `⟨ψ⟩` never increasing, strictly decreasing for `n≥2`,
  constant at `n=1`; the uniform bound; the closed form `2nc/√(1+4c²n²)` at seven `n`
- **F** the `ε_q→0` limit; `n=1` flicker-blindness (identical intervals, not equal midpoints);
  T-oddness; the specialization-robust content

**Level 5 suite: 219 exact checks, 0 failures** across 11 scripts. Errors caught by the gates:
the `D_n`-vs-`1−u^n` normalizer; an interval-equality test that needed componentwise
comparison; an over-strict monotonicity test that wrongly demanded decrease at the flicker-blind
`n=1`.

**Adopted:** nothing. **Declared:** nothing. No P4 addition, no new dimensionful scale, no
measured value, no species identification, no isolated aspect applied. **Marked:** specialization
(S). **New at L5:** the magnetic transition functional and its attenuation theorem; the closed
crystallized form `2nc/√(1+4c²n²)`; the demonstration that BM.90's four grounds do not reach a
configuration-functional read except via ground (iv), which marking discharges; and the reversal
of the naive expectation — **the flicker attenuates magnetism, it does not source it.**
