# LEVEL 5 DATA CENSUS — the Atomic Era opening move

**Status:** discovery-phase working document. Not canon. No mass read adopted, no
bridge adopted, no scale declared, no `g`-branch selected.
**Engine:** `era2/qexact.py` + `era2/census_L5.py` + `era2/build_census.py`.
**Arithmetic:** exact. Integers, `Fraction`, `ℤ[x]`, and rigorous `Fraction` intervals
for transcendentals (Machin π, the `ln2 = Σ1/(n2ⁿ)` series, Archimedes cross-check).
No floating point in any assertion.
**Quarantine:** every `[EXT]` value below is a *scoring target*, never an input. No
number in this census is fitted to measurement.

---


> **CORRECTION (found later, `verify_spin_stats.py`).** The `D_S/4E²` column in §B is
> **wrong by a factor of 4**. `build_census.py` divided by `4·E_int²` where
> Census FT.63(6) and BM.140(6) divide by `4·E²` with **`E` the undirected edge count**
> (`E_int = 2E`). Correct values: tetra `1/72` (not `1/288`), octa `1/576` (not `1/2304`),
> dodeca `(2−2cos(π/10))/3600`, icosa `(2−√3)/3600`. `validate_against_canon.py` used the
> right formula and passed; the census builder used the wrong one. The six-state bridge
> span is `ℛ_max/ℛ_min = 100/(2−𝔲) = 1021.586454727`.
>
> **Also withdrawn:** §E/§F's "shortfalls" (695.5×, 544.0×) — HistLog §V.32 and
> Def-H.39's nomenclature rule make the `r²`/`D_S`/`E_int` reads *prices*, not masses.
> See `COHERENCE_CENSUS.md`.

---

## 0. Validation gates (both must pass before any Level 5 row is trusted)

**Gate 1 — reproduce the canon's structural tables from cardinals alone**
(`validate_against_canon.py`, **ALL PASS**, 0.10 s):

| reproduced | source | result |
|---|---|---|
| `δ_v/π = (1, ½, ⅔, ⅕, ⅓)` | Census FT.63(4) | exact rationals ✓ |
| `V·δ_v = 4π` on all five solids | FT.63(4) / Gauss–Bonnet | exact ✓ |
| `D_S = 4sin²(δ_v/4)` → `(2, 2−√2, 1, 2−2cos(π/10), 2−√3)` | FT.63(6) | ✓ |
| minimal polynomials incl. dodecahedral `x⁴−8x³+19x²−12x+1` | FT.63(6) | exact `ℤ[x]` substitution ✓ |
| `D_S/4E²` anchors `1/72`, `1/576` | FT.63(6) | exact rationals ✓ |
| tetra weight ladder `D_S(m) = (2,4,2,0)` at `m=(1,2,3,4)` | BM.60(2) | ✓ |
| `E_int = 2E → (12,24,24,60,60)`, ladder `1:2:5` | FT.63(5), BM.115(2) | ✓ |
| `Δ₁=2 > Δ₂=√2−1 > Δ₃=2cos(π/10)−√3 > 0` | Def-BM.14(5), BM.81 | ✓ |

**Gate 2 — reproduce the canon's own [EXT] audits** (`census_L5.py` Stage 1, **ALL REPRODUCE**):

| reproduced | source | our value |
|---|---|---|
| `r^(q) = (2.410335463511094…, 0.204193367808662…, 0.385471168680242…)` | FT.119(3) | enclosure-intersect ✓ |
| `m₂/m₃ = 0.025575776…`, `m₁/m₃ = 0.007176757…` | FT.120(4) | ✓ |
| margins `0.0064 < 0.01` and `0.0839 > 0.05` | FT.120(4) | ✓ |
| q outer `139.3386880284…`, ℓ outer `3477.472837104…`, ℓ mid `206.770315972…` | FT.113/FT.119(5) | ✓ |
| `r₂²/r₁² − 206.768 > 1/1000`, `r₀²/r₁² − 3477.2 > 1/10` | FT.114(1) | gaps `0.00232`, `0.273` ✓ |
| `1−shortfall ∈ (10⁻⁵,2×10⁻⁵)` and `(7×10⁻⁵,9×10⁻⁵)` | FT.114(2) | ✓ |
| hadron span `81.4955 < 82 < 139.3387` | FT.120(7) O4 | ✓ |
| `m ∝ r` gives `58.9701…` (ℓ), `1.887775…` (q) | FT.120(8) | ✓ |
| `√(4/D_S,min) = 6.3925` | FT.76(3) | ✓ |

> Methodology note: the canon quotes **truncated** decimals (`2.410335463511094…`).
> Comparing by containment of the literal decimal is wrong; the correct test is
> intersection of our rigorous interval with `[d, d+10⁻ᵏ)`, where `k` is the canon's
> own digit count. That is FT.119(4)'s "enclosure containment" method.

**Both gates pass. Level 5 material below is admissible.**

---

## A. The 2D/3D defect split — the mechanism you flagged

FT.54(4) reads the pole mass off the Gauss–Bonnet angle defect:

```
Theta_R = sum_i alpha_i - (n-2)*pi          m^2_pole = 4 mu'^2 sin^2(Theta_R/4)
```

**3D seal** (Platonic vertex figure, `d` faces meeting): `δ_v = 2π − d(L−2)π/L > 0`,
total `V·δ_v = 4π = 2πχ` with `χ = 2`. Six distinct positive defects.

**2D floor** (flat regular `n`-gon, geodesic loop bounding a disk-like `S`):
`α_i = (n−2)π/n` ⟹ `Σα_i = (n−2)π` ⟹ **`Θ_R = 0` identically, at every `n`**.
Total turning `= n(π−α) = 2π = 2πχ` with `χ = 1` — exactly half the solid's charge.

| n-gon | `E_int=2n` | `Θ_R/π` | turning/π | `D_S` | `m_hid (ln2/𝔥)` | `T₀ (𝔥/ln2)` | `G=2πE²ln2` | `g₃=1/(1+G)` |
|---|---|---|---|---|---|---|---|---|
| 3 | 6 | **0** | 2 | **0** | 6 | 6 | 156.79 | 6.34×10⁻³ |
| 4 | 8 | **0** | 2 | **0** | 8 | 8 | 278.73 | 3.58×10⁻³ |
| 5 | 10 | **0** | 2 | **0** | 10 | 10 | 435.52 | 2.29×10⁻³ |
| 6 | 12 | **0** | 2 | **0** | 12 | 12 | 627.15 | 1.59×10⁻³ |
| 8 | 16 | **0** | 2 | **0** | 16 | 16 | 1114.92 | 8.96×10⁻⁴ |
| 12 | 24 | **0** | 2 | **0** | 24 | 24 | 2508.58 | 3.99×10⁻⁴ |

### The consequence (new at Level 5, exact)

**For every 2D polygon floor the two mass currencies DECOUPLE:**

```
m_hid  = 2n ln2/h      nonzero, strictly increasing, injective in n   [FT.46(2)]
m_pole = 0             identically, at every n
bridge = m^2_pole/m^2_hid = (mu'^2 h^2/ln2^2) * (D_S/4E^2) = 0
```

**For every 3D seal they COUPLE:** bridge `> 0`, six distinct values.

Therefore, applying the BM-level theorems *downward* onto FT-level objects:

1. **BM.90 is vacuous on 2D floors.** Branch-blindness refutes hypothesis (W) — that the
   defect reweights `m_hid`. On a flat floor there is no defect to reweight; (W) cannot
   even be posed.
2. **Def-BM.19(3)'s multiplet ladder collapses.** `Δ(m) = 2 − 2T_|m|(cos(Θ_R/2)) → 0` for
   *all* `m`. The "standing zero" at `m=0` stops being a special weight and becomes every
   weight.
3. **Only two BM corrections transfer to a 2D floor object:** the metric dressing
   (`Δx_B, V_eff, ρ, G, f(k), g`) and the BM.89 self-energy. Both read off `E_int` alone —
   and `E_int = 2n` already exists on the floor side from **FT.46(2), in Part 3, before
   Part 4 was written.**
4. **A sharp structural discriminator:** an object whose mass is entirely informational is
   a 2D-floor object; an object with nonzero pole mass is a 3D seal. Exact, no parameter.

---

## B. The six sealed states — all reads, BM corrections applied

| st | branch | solid | `2E` | `D_S` | `m_hid` | `T₀` | `Δx_B` | `G` | `g₂=1+G` | `g₃=1/(1+G)` | `D_S/4E²` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| s₁ | (F₁,−) rung m=1 | tetrahedron | 12 | 2 | 12 | 12 | 0.08333 | 627.14 | 628.14 | 1.59×10⁻³ | 3.47×10⁻³ |
| s₂ | (F₁,+) rung m=2 | tetrahedron | 12 | 4 | 12 | 12 | 0.08333 | 627.14 | 628.14 | 1.59×10⁻³ | 6.94×10⁻³ |
| s₃ | (F₂,−) | cube | 24 | 2−√2 | 24 | 24 | 0.04167 | 2508.58 | 2509.58 | 3.99×10⁻⁴ | 2.54×10⁻⁴ |
| s₄ | (F₂,+) | octahedron | 24 | 1 | 24 | 24 | 0.04167 | 2508.58 | 2509.58 | 3.99×10⁻⁴ | 4.34×10⁻⁴ |
| s₅ | (F₃,−) | dodecahedron | 60 | 2−2cos(π/10) | 60 | 60 | 0.01667 | 15678.62 | 15679.62 | 6.38×10⁻⁵ | 6.80×10⁻⁶ |
| s₆ | (F₃,+) | icosahedron | 60 | 2−√3 | 60 | 60 | 0.01667 | 15678.62 | 15679.62 | 6.38×10⁻⁵ | 1.86×10⁻⁵ |

Units: `m_hid` in `ln2/𝔥`; `T₀` in `𝔥/ln2`; `Δx_B` in `𝔥/ln2`; `G`, `g` dimensionless.
`g` is shown in **both** unadopted branches — BM.88 prices three and adopts none; the
census adopts none.

Branch splittings (Def-BM.14(5), BM.81), all in the `μ̂'²` currency, strictly decreasing:

```
Delta_1 = 2                     = 2.000000000000     in Q
Delta_2 = sqrt2 - 1             = 0.414213562373     in Q(sqrt2)
Delta_3 = 2cos(pi/10) - sqrt3   = 0.170062225021     in Q(sqrt3, cos(pi/10))
```

---

## C. The three channel triplets

| channel | `δ` | provenance | `r₀` | `r₁` | `r₂` |
|---|---|---|---|---|---|
| ℓ | 2/9 | FT.109–113, FT.158, Def-BM.6(1) | 2.379438171633 | 0.040349908219 | 0.580211920148 |
| q | 2/27 | FT.118–119, BM.60(1) | 2.410335463511094733 | 0.2041933678086625958 | 0.3854711686802426152 |
| ν | 1/8 | FT.142–144, Def-BM.6(2) | 2.403179397551 | 0.145715560919 | 0.451105041530 |

**Exact invariants, all three channels, phase-independent** (from `Σcos(θ+2πi/3)=0` and
`Σcos²=3/2`, no numerics): `Σr = 3 = dim F_{J±}`, `Σr² = 6`, `Q = Σr²/(Σr)² = 2/3`.
Cross-channel identity `16δ_ν = 9δ_ℓ = 27δ_q = 2` verified exact. Spatial provenance
`δ_ℓ = (3−1)/(3·3)` verified exact [FT.158(2)–(3)].

Amplitude² ratios (`m_i = μr_i²`, the read FT.120(8)'s audit leaves standing):

| channel | `r²` sorted ascending | mid ratio | outer ratio |
|---|---|---|---|
| ℓ | 0.001628115, 0.336645872, 5.661726013 | **206.770316** | **3477.472837** |
| q | 0.041694931, 0.148588022, 5.809717047 | 3.563695 | **139.3386880284** |
| ν | 0.021233025, 0.203495758, 5.775271217 | 9.583927 | 271.994749 |

---

## D. Extension: the order-isomorphism is channel-agnostic (new at Level 5)

Def-BM.14(6) states its argument for the **q-channel only**:

> "two exact three-element ordered sets admit exactly one order-isomorphism"
> `(r^(q)_1)² < (r^(q)_2)² < (r^(q)_0)²` ⟷ `2E(F₁) < 2E(F₂) < 2E(F₃)`

The argument uses nothing q-specific. Every channel's three lines are strictly ordered and
enclosure-proven [FT.113 (ℓ); FT.119(5) (q); FT.143(1),(3) (ν)], and the three floors are
strictly ordered [Def-BM.14(1)]. **So all three channels admit the same unique isomorphism.**

| channel | gen 1 → F₁ | gen 2 → F₂ | gen 3 → F₃ |
|---|---|---|---|
| ℓ, q, ν | `E_int = 12` | `E_int = 24` | `E_int = 60` |

Every channel line thereby acquires the apparatus Section C of `build_census.py` reported
as **NOT FORMED**:

| gen | `E_int` | `Δx_B (𝔥/ln2)` | `G = 2πE²ln2` | `g₂ = 1+G` | `g₃ = 1/(1+G)` | `T₀ (𝔥/ln2)` | `m_hid (ln2/𝔥)` |
|---|---|---|---|---|---|---|---|
| 1 | 12 | 0.083333 | 627.14 | 628.14 | 1.59×10⁻³ | 12 | 12 |
| 2 | 24 | 0.041667 | 2508.58 | 2509.58 | 3.99×10⁻⁴ | 24 | 24 |
| 3 | 60 | 0.016667 | 15678.62 | 15679.62 | 6.38×10⁻⁵ | 60 | 60 |

This is the **single object that unblocks both Level 5 closure goals**: magnetism needs
`Δx_B → G → g(G)`; hydrogen needs `m_r` of the lepton–baryon pair [BM.48(2)]. Both need
`E_int`. Def-BM.14(6) supplies it by an argument the canon already proved, restricted to a
channel it never needed to restrict to.

*Caveat carried honestly:* Def-BM.14(6) also says "the scale is not supplied … the map is
an order, ¬a number," and the relating equation between the currencies is ¬derived. The
isomorphism is **derived**; the claim that the line's `E_int` *is* the floor's is the
item-13 bridge and remains a conjecture. It is, however, a **sharp** one — see §F, P2.

---

## E. The three mass currencies, priced against each other

| | Currency 1 — informational | Currency 2 — pole | Currency 3 — amplitude |
|---|---|---|---|
| formula | `m_hid = E_int ln2/𝔥` | `m²_pole = μ̂'² D_S` | `m_i = μ r_i²` |
| source | FT.42(1), FT.46(2), BM.115 | FT.54(4), Def-BM.14(3) | FT.119(4); FT.120(8) audit |
| available for | 2D floors, 3D seals, junctions, digon | **3D seals only** (2D: `Θ_R=0`) | the three channel triplets |
| six-state span | **5** (exact rational, `60/12`) | **6.3925** in `m` (40.86 in `m²`) | ℓ 3477.47 · q 139.34 · ν 271.99 |
| ceiling | BM.115: 5 (six-state), 30 (full cell ladder) | FT.76(3): `√(4/D_S) ≤ 6.3925` | none reached yet |

**Central quantitative finding (exact, new at Level 5):**

```
Currencies 1 and 2 are CEILING-BOUND at 5 and 6.3925.
Currency 3 reaches 3477.5.

  shortfall of Currency 1 on the ell-family = 695.5x
  shortfall of Currency 2 on the ell-family = 544.0x
```

**This answers the agenda question — "do the energetics that drive the proton–neutron and
baryon–meson hierarchies apply to the leptons?" — exactly, and the answer is no, for an
informative reason:**

The BM energetics produce **order-unity splittings** (`1:2:5`; `≤ 6.39` on the pole side).
That is *correct for their native domain*: the proton–neutron splitting and the
baryon–meson hierarchies **are** order-unity, and BM.91 proves `1 < m_n/m_p < 10/9` exactly
with the parameter-free bar `Nwgε_EM ≤ 1/8`. It is not a failure of the mechanism — it is
the mechanism's natural range.

The family hierarchies (`10²–10³`) live in Currency 3, which is a **different object**: a
`C₃`-covariant seal bilinear, not an edge count or a holonomy defect.

> **The two are complementary, not competing.** The Level 5 object is their *composition*:
> `m = [Currency 3: family hierarchy] × [Currency 1/2 + BM.88/BM.89 dressing: intra-family
> splitting and metric correction]`.

---

## F. Routes that "do stuff" — ranked by discriminating power

| route | span | target | shortfall | verdict |
|---|---|---|---|---|
| Currency 1 via order-isomorphism (ℓ) | 5.000 | 3477.5 | 695.5× | ceiling-bound |
| Currency 2, pole `D_S` (ℓ) | 6.392 | 3477.5 | 544.0× | ceiling-bound |
| Currency 3, amplitude `r²` (ℓ) | 3477.473 | 3477.5 | 1.0× | **reaches** |
| Currency 3, amplitude `r²` (q) | 139.339 | 139.3 | 1.0× | **reaches (native)** |
| BM.91 p–n splitting | 1.111 | 1.1 | 1.0× | **exact, native domain** |

**Discriminating predictions — what makes a route sharp rather than flat:**

- **P1.** Currency 3 predicts `m_μ/m_e = 206.770316` against `[EXT] 206.768`, with
  `1−shortfall ∈ (10⁻⁵, 2×10⁻⁵)` enclosure-proven. *Already canon (FT.114); reproduced.*
- **P2.** Currency 1 predicts the generation ladder **exactly `1:2:5`**. Currency 3 predicts
  `1 : 3.5637 : 139.3387`. They disagree by **27.9×** on generation 3. A single mass read
  cannot be both — so the composition in §E is *forced* if both currencies are real, and it
  is testable: the hierarchy must come from Currency 3 and the splitting from Currency 1/2,
  multiplicatively. **This is the sharpest open question in Level 5.**
- **P3.** Every 2D floor has `m_pole = 0` exactly. Sharp structural discriminator between
  2D-floor and 3D-seal objects, with no free parameter.
- **P4.** `Δ₁ > Δ₂ > Δ₃` means the intra-family splitting **shrinks in absolute terms down
  the family even as the family mass grows** — the opposite of naive scaling. Composed with
  Currency 3 this is checkable against the up/down-type splittings.

---

## G. Force decomposition available per object class

| object class | `E_int` | `Q` read | EM | strong | weak | grav | pole |
|---|---|---|---|---|---|---|---|
| digon floor | 2 | ternary | ✓ | — | — | ✓ | **0** |
| 2D polygon floor `P_n` | `2n` | ternary | ✓ | — | — | ✓ | **0** |
| junction `Σ₁₂` | 6 | 0, +1 | ✓ | sealed | vertex | ✓ | n/a |
| 3D seal (6 states) | 12/24/60 | ternary | ✓ | sealed | branch | ✓ | **>0** |
| ℓ-channel line | 12/24/60 *(via §D)* | −1 | ✓ | — | ? | ✓ | ? |
| q-channel line | 12/24/60 *(via §D)* | ternary | ✓ | ? | ? | ✓ | ? |
| ν-channel line | 12/24/60 *(via §D)* | 0 | — | — | ? | ✓ | ? |

`?` = not formed: the defect datum is not attached to a channel line, only to a solid.
Strong = colour-sealed by Def-BM.1's junction grammar (CT3.22: colour ¬observable, thirds
unreadable by construction). Weak = the branch/duality index (Def-BM.14(2)); chirality
itself is deficit 1 and remains open at every level. Grav = `G_N` from the single scale.

---

## H. Still hard-blocked, and why

**Magnetism.** `anomalous magnetic` = 0 hits in the canon. §D supplies the `G` argument the
muon was missing, but `a_μ = (g−2)/2` is by construction a spin–field coupling
`ψ̄ σ^{μν} F_{μν} ψ`, and HistLog item **21(i)** names the missing **spacetime spin factor**;
Part3:1864 says promoting `R(k)=k/2` "requires one missing lemma — a corpus-level spin
connection"; FT.93's pincer bars any `γ_F` from grading the weak force. **Prerequisite gap,
not derivation gap.** Def-H.21 constructs a spin connection on the emergent geometry — that
is the thread to pull.

**Hydrogen.** BM.48(1)–(2) already banked `V(d) = −ε_EM/d` on the forced pair
`(q_p,q_ℓ)=(+1,−1)` and `E_n = −ε_EM²m_r(q₁q₂)²/(2n²)`, `E₂/E₁ = 1/4` exact. Missing:
BM.48(3)'s **EM sealing grammar** ("¬∃ an EM sealing grammar in the inventory" — composites
are colour-sealed only). §D now supplies the `m_r` input; the grammar is the remaining gap.
Must respect BM.48(4)'s boxed category bar: binding energy belongs to the bound system,
never to a free member's mass.

---

## I. Disposition

```
ADOPTED      nothing. No mass read, no bridge, no scale, no g-branch, no species ID.
DECLARED     nothing. Section Cal stays empty. No P4 addition. No new dimensionful scale.
QUARANTINED  every [EXT] value used is a scoring target, never an input.
SUPERSEDED   nothing yet -- but FT.84(5b)'s demotion of the large-V route is now
             DIRECTLY TESTABLE via P2, and Def-BM.14(6)'s channel restriction is
             shown to be an artifact of where the argument was first needed.
NEW AT L5    (i)  Theta_R = 0 identically on every 2D floor => the two mass currencies
                 decouple for 2D and couple for 3D;
             (ii) the order-isomorphism extends to all three channels, so all nine
                 lines acquire E_int, dxB, G, T_0 and a self-energy;
             (iii) the exact spans of the three currencies (5 / 6.3925 / 3477.5) and
                 the complementary-not-competing conclusion, with exact shortfalls
                 695.5x and 544.0x;
             (iv) predictions P2-P4, each falsifiable.
NEXT         P2 is the live question. Then the EM sealing grammar, then Def-H.21's
             spin connection.
```
