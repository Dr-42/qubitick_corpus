# THE MIXED-EDGE CENSUS — closed, and the shift's longitudinal part is derived

**Question:** does any *materialized* chain traverse both a tick increment and a spatial
displacement on one edge? If not, `∂dŝ²/∂w_i ≡ 0` on the whole on-shell locus and the magnetic
sector is **absent by theorem**.

**Answer: the mixed class is not merely nonempty — it is the ENTIRE materialized edge class.**
And that produces the strongest result in this chain: **the longitudinal component of the shift
is ledger-determined in closed form.**

Verified by `era2/mixed_edges.py` — **16/16 exact**. **Level 5 total: 235 exact checks, 0 failures.**

---

## I. Three derived rows close it

**(R1) Every edge has a nonzero tick increment.**
**D0.7**, cited in CT2.8(2)'s Pf: *"each edge is registered **between consecutive ticks**, wholly
on one side."* With **D1.8** (`x⁰ := τ_n`, `τ_n = Σδτ` along a causal chain of real edges) and
**CT0.3** (the derived clock `(Δn_ℛ, δh, δτ) = ±(1,1,1)` per Janus move):

```
Dx^0(e) = delta tau != 0     on EVERY registered edge
```

**(R2) Materialized chains are spacelike with integer edge data ≥ 1.** FT.24 / FT.34(4):
on-shell integer edge data `κ_e ∈ ℤ_{≥1}`; every pole-transfer locus is stated *"for a
materialized **spacelike** bound chain"*; Def-BM.4(5): *"the minimal materialized line element
is `dŝ² = 1`."*

```
dshat^2(e) = kappa_e >= 1     =>     ds^2(e) = kappa_e h^2 > 0
```

**(R3) D1.6 contracted with CT1.12/BM.34(1)'s metric.** In the vacuum spatial gauge `q=0`, `w=0`:

```
ds^2 = Omega^2 ( |Dx|^2 - (Dx^0)^2 )
=>  |Dx|^2 = (Dx^0)^2 + kappa_e h^2 / Omega^2  >  (Dx^0)^2  >  0
=>  Dx^i != 0
```

`Ω² = e^{2α_Ωa_{00}} > 0` for **every** `a_{00} ∈ ℝ` [CT1.12], so the sign is unconditional.

| `κ_e` | `Δx⁰` | `Ω²` | `|Δx|²` | `|Δx|²−(Δx⁰)²` | mixed |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | 1 | **YES** |
| 2 | 1 | 1 | 3 | 2 | **YES** |
| 6 | 1 | 1 | 7 | 6 | **YES** |
| 12 | 1 | 1 | 13 | 12 | **YES** |

**Both alternative horns are excluded.** A purely temporal edge needs `|Δx| = 0`, hence
`ds² = −Ω²(Δx⁰)² < 0` — *timelike*, contradicting (R2). A purely spatial edge needs `Δx⁰ = 0`,
contradicting (R1). Corollary: the null class (`dŝ² = 0 ⟺ Δx_e` null, CT1.19a) is **disjoint**
from the materialized spacelike class, since a null edge has `|Δx| = |Δx⁰|`.

---

## II. The constraint count improves — per edge, not per cycle

`dŝ²(e) = κ_e` is **one equation per edge** [FT.24: the on-shell integer data are per-edge], and
the cycle reads `Θ(c) = Σ_e dŝ²(e) = 2k` [D1.7; FT.34(2); FT.22] are **consequences**, not
additional independent constraints. So with `3E` shift coordinates and `E` per-edge equations:

| floor | `E` | shift coords `3E` | equations | rank | **nullity `2E`** | *(old)* `3E−β₁` |
|---|---|---|---|---|---|---|
| tetrahedron | 6 | 18 | 6 | 6 | **12** | 15 |
| cube | 12 | 36 | 12 | 12 | **24** | 31 |
| octahedron | 12 | 36 | 12 | 12 | **24** | 29 |
| dodecahedron | 30 | 90 | 30 | 30 | **60** | 79 |
| icosahedron | 30 | 90 | 30 | 30 | **60** | 71 |
| polygon `P_n` | n | 3n | n | n | **2n** | 2n−1 |

Each edge's equation is **linear** in `w_i` with coefficient `(2ϰβΩ²/𝔥²)Δx⁰Δx^i`, nonzero by §I.
So it fixes exactly **one** linear combination of that edge's three `w_i`.

---

## III. The main result: the longitudinal shift is ledger-determined, in closed form

Solving `dŝ²(e) = κ_e` for the `w`-contraction, with `M_{ij} := δ_{ij} + ϰq_{ij}`:

```
kappa_e = (Omega^2/h^2)[ -(Dx^0)^2 + 2 kappa_emb beta (w.Dx) Dx^0 + M_ij Dx^i Dx^j ]

                        h^2 kappa_e/Omega^2 + (Dx^0)^2 - M_ij Dx^i Dx^j
  (w . Dx)(e)   =   -------------------------------------------------------
                              2 kappa_emb beta Dx^0
```

**Exact, and round-trips:** substituting back into D1.6's line element returns `κ_e` at every
witness tested. Every input on the right is ledger or metric data:

| input | kind | locus |
|---|---|---|
| `κ_e` | on-shell **integer** edge datum | FT.24; FT.34(4) |
| `Δx⁰` | **tick increment** | D0.7; D1.8; CT0.3 |
| `Ω`, `M_{ij}` | conformal and spatial metric coefficients | D2.1; CT1.12 |
| `ϰ`, `β` | **P4 core, values ¬issued** | C4; §Cal-2 |

**So the longitudinal projection of the shift along the spatial hop is DERIVED from ledger data**,
up to the P4 pair. This is a strictly stronger position than `MAGNETIC_FUNCTIONAL.md` §VI claimed.

**The transverse 2 dimensions per edge are gauge — and correctly so.** Summary:5093: *"`N_i` is
the **Lagrange multiplier of the momentum constraint**, whose charge generates spatial
diffeomorphisms … the conserved quantity is the momentum `P_i`, and `P_i` is T-odd."* A Lagrange
multiplier is fixed by the slicing choice, not by dynamics. So the transverse freedom is not a
defect of the reconstruction; it is the diffeomorphism gauge, and the **gauge-invariant magnetic
content is precisely the longitudinal piece, which §III determines.**

```
w_i(e) = [ (w.Dx)(e) / |Dx|^2 ] Dx_i      +      w_i^perp(e)
         \_____________________________/          \____________/
          LEDGER-DETERMINED, closed form           GAUGE, 2 dims per edge
```

---

## IV. What this does to specialization (S)

`(S)` was `w_i(R) = ω_i·E_int(R)`, **marked and ¬adopted** because BM.90 ground (iv) bars a
*derived* count→strength coupling. §III sharpens its status considerably:

| part of `(S)` | status |
|---|---|
| the **longitudinal** content `w·Δx` | **DERIVED** — §III's closed form fixes it per edge from `(κ_e, Δx⁰, Ω, M)` |
| the **direction** `ω_i` (floor-constant) | still ansatz — motivated by Census FT.66(1)'s `Aut(Γ_S)` channel-permutation action, **not proved by it** |
| the **transverse** part | **GAUGE** — fixed by a slicing choice, a read-specification act |
| the overall scale `(ϰ, β)` | **calibration** — P4 core, ¬issued; irreducible, `(C-BM.1)/ρ_B`-shaped |

So `(S)` is not a free ansatz on the part that matters. The homogeneity step is the only genuine
content it adds, and the gauge and scale parts were never derivable in principle.

---

## V. The corrected verdict on the magnetic sector

Both horns posed in `MAGNETIC_FUNCTIONAL.md` §VII dissolve:

1. **The magnetic read is nonzero** on every materialized configuration whose longitudinal shift
   is nonzero — and that shift is ledger-determined (§III). It vanishes only where the closed
   form's numerator vanishes,
   ```
   h^2 kappa_e/Omega^2 + (Dx^0)^2 = M_ij Dx^i Dx^j
   ```
   a **codimension-1 locus in the metric data**, not a generic one.
2. **It is not absent by theorem.** The mixed-edge class is the whole materialized edge class.
3. **Correction to `MAGNETIC_READ.md` §V.** "Purely electric on every formed cell" holds only in
   the `w=0` gauge — and BM.34(4) *names* `w=0` a gauge. Withdrawn as a general statement; it
   stands for BM.146(3)'s continuum-limit cell, which is that gauge.

**Complete disposition of the magnetic sector:**

| component | status | locus |
|---|---|---|
| field strength `F_{μν}` | **derived** | EM.12 (plaquette circulation), EM.14, EM.15 |
| ADM split with live shift | **derived** | BM.34(1); `N²det γ = −det g` |
| the split `E_i = (1/N)(F_{i0} − N^jF_{ij})` | **derived** | `em_split.py`, 16/16 |
| matter-side drag `−N^ip_i` | **derived** | BM.34(4); same three coefficients as `g_{0i}` [BM.34(3)] |
| T-oddness under `w → −w`, un-washable | **derived** | BM.34(3); `magnetic_functional.py` F3 |
| longitudinal `w·Δx` | **derived, closed form** | §III |
| transverse `w^⟂` | **gauge** | slicing choice; `N_i` is the momentum multiplier |
| scale `(ϰ, β)` | **calibration, ¬issued** | C4; §Cal-2 |
| ensemble behaviour | **derived on `(S)`** | attenuation theorem; `⟨ψ⟩` monotone; bound uniform |

> **There is no structural gap left in the magnetic sector.** What remains is one gauge choice
> and one calibration pair — neither of which is a missing construction.

---

## VI. Where the chain now stands, end to end

```
network    E_int = |R|                                        [Def-BM.5(4); FT.44(4)]
   |
   +-> spine    V(K~) = T(K~^2),  (1-gamma/4)^2 + gamma(8-gamma)/16 = 1   [L1; BM.51]
   |            m_i^2 = DeltaS = V/8   (registry species (3) == (5))       [L3(2),(4)]
   |            beta_31 = h,  coefficient ln2,  DeltaS_L = I_hid = E_int ln2 [BM.35]  CONSTRUCTED
   |
   +-> metric   G = 2 pi E_int^2 ln2                          [BM.88(3)]
   |            g(G) = 1/(1+G)  SELECTED by S1 ^ S2             [BM.133(4)]
   |            N^2 = 1 - h E_int/(2r)  ==  1 - G/(4 pi k)      [BM.132; BM.146(3)]  IDENTICAL
   |            G_N = h^2/(4 ln2),  E_int CANCELS               [Def-BM.4; BM.13]
   |
   +-> force    F always applies in full; no sub-block restriction [A8; BM.52(1)]
   |            the metric's 10 coords = 7 (E_++) + 3 (E_+-);  shift is the T-odd block
   |                                                          [CT1.1; CT1.12a(2)]
   |
   +-> magnetic E_i = (1/N)(F_{i0} - N^j F_{ij});  one F, many observers, invariants fixed
   |            longitudinal w.Dx LEDGER-DETERMINED             [mixed_edges.py sec.III]
   |            transverse = gauge; scale = (kappa, beta) P4
   |            <E_i^mix>_E = -(kappa beta/Omega)<psi>_E Phi_i, psi(E)=E/sqrt(1+c^2E^2)
   |            attenuation theorem; crystallized value 2nc/sqrt(1+4c^2n^2)
   |                                                          [magnetic_functional.py]
   |
   +-> hydrogen BM.48(1)-(2) banked V(d) = -eps_EM/d, E_2/E_1 = 1/4; needs m_r  [P5.1/P5.2]
```

**Two numbers remain unissued in the entire formed theory: `𝔥` [P1] and `e₀` [EM.25(7)]** — plus
the P4 pair `(ϰ, β)` for the shift's scale. All are dimensionful calibration; none is structural.

---

## VII. Check ledger

`era2/mixed_edges.py` — **16/16 EXACT**:

- **A** `|Δx|² − (Δx⁰)² = κ_e𝔥²/Ω² > 0` strictly at every `(κ_e ≥ 1, δτ ≠ 0, Ω² > 0)`; the mixed
  class is the whole materialized edge class; the null class is disjoint from it; both pure
  horns excluded
- **B** per-edge rank `E`, nullity `2E`; the polygon ladder `2n`
- **C** the closed form for `(w·Δx)(e)`, round-tripped exactly into D1.6's line element at four
  witnesses; the gauge status of the transverse part
- **D** `(S)`'s longitudinal content derived, its direction still ansatz, its transverse part gauge
- **E** the corrected verdict and the three withdrawals

**Level 5 suite: 235 exact checks, 0 failures** across 12 scripts
(`validate_against_canon` ALL PASS · `census_L5` 19/19 · `coherence_census` 25/25 ·
`beta31` 17/17 · `verify_spin_stats` 34/34 · `em_split` 16/16 · `one_force` 22/22 ·
`m1_shift` 30/30 · `m1pp_shift` 20/20 · `m1ppp_bm34` 13/13 · `magnetic_functional` 23/23 ·
`mixed_edges` 16/16).

**Adopted:** nothing. **Declared:** nothing. No P4 addition, no new dimensionful scale, no
measured value, no species identification, no isolated aspect applied.
**Withdrawn:** "the magnetic sector may be absent by theorem"; "`w_i = 0` on every formed cell"
as a general statement (it is the `w=0` gauge). **New:** every materialized edge is mixed, from
D0.7 + FT.24 + D1.6 alone; the per-edge (not per-cycle) constraint count with nullity `2E`;
**the closed-form ledger determination of the longitudinal shift**; the identification of the
transverse freedom as the momentum-constraint gauge; and the resulting **complete disposition of
the magnetic sector with no structural gap remaining.**
