# `canon/era2/` — Level 5 · the **Atomic** era · Tier A.1

**Status: discovery-phase working tier. NOT frozen canon.** Nothing here is adopted, no
declaration issues, §Cal-A is empty, and no clause of Parts 1–4 is modified or retracted.

| file | content |
|---|---|
| `Part5_Atomic_era_TierA1.md` | **Tier A.1** — tags A.1–A.8 in canon format (Thm · Req · Pf · Phys), plus §Cal-A and §Open-A |
| `Part5_Atomic_era_TierA2.md` | **Tier A.2** — tags A.9–A.14: the tensor form of the bit/qubit distinction through BM.131's Haar–Poisson duality, **no global tick** |
| `run_all_era2.py` | the tier's runner — gates first, exit 0 iff all green |
| `qexact.py` | shared exact-arithmetic core (see below) |
| `SESSION_SUMMARY_AND_REVIEW.md` | session ledger, the model's error profile, and interaction review notes |
| the 12 `*.py` checkers | the machine verification; each cites the canon tags it reproduces or extends |

## Run

```bash
cd canon/era2 && python3 run_all_era2.py     # -> 13 checkers, 0 failures, exit 0
```

## The arithmetic covenant

Inherited unchanged from `verification/`: **exact arithmetic only, no floating point in any
assertion.** `Fraction`; `ℤ[x]` and multivariate `ℚ[γ,G,a]`; complex-over-`Fraction`; exact 4×4
matrices over `Fraction`; the prime-log ring `ℚ[ln2,ln3]`; and rigorous `Fraction` **intervals**
for every transcendental — Machin's formula for `π`, the `ln2 = Σ 1/(n2ⁿ)` series with an exact
tail bound, Archimedes `223/71 < π < 22/7` as a cross-check, and bisection `sqrt`.

**No measured value enters any derivation [P5].** Every `[EXT]` figure appearing anywhere in this
folder is a *scoring target*, never an input.

## The two validation gates

Nothing downstream is emitted unless both pass:

1. `validate_against_canon.py` — reproduces Census FT.63(4),(6), BM.81(1), BM.60(2), BM.115(2)
   **from the cardinals alone**, including the dodecahedral quartic `x⁴−8x³+19x²−12x+1` and the
   exact rational anchors `1/72`, `1/576`.
2. `census_L5.py` Stage 1 — reproduces the canon's own `[EXT]` audits: FT.113, FT.114(1)(2),
   FT.119(3)(5), FT.120(4)(7)(8), FT.76(3).

Gate methodology note: the canon quotes **truncated** decimals (`2.410335463511094…`). Comparing
by containment of the literal decimal is wrong; the correct test is intersection of the rigorous
interval with `[d, d+10⁻ᵏ)` at the canon's own digit count — FT.119(4)'s "enclosure containment".

## What Tier A.1 claims, in one line each

- **A.1** the bridge slot `β₃₁` is constructed: `β₃₁ = 𝔥`, per-edge coefficient `ln2` forced by
  `ln4 = 2 ln2` and `E_int = 2E_bidir + E_uni`. Def-H.39's "unconstructed" was a
  citation-direction artifact (Part 3 cannot cite Part 4).
- **A.2** the metric's ten coordinates **are** the `S`-even subspace, split `7+3` by `T`;
  CT1.12a(2)'s `5+1+1+3` apportionment *is* CT1.1's block boundary, so the shift is T-odd by
  **index structure**, not by force attribution.
- **A.3** the electromagnetic split is an observer-relative **reading**: one `F`, five exact
  rational observers, `E²` varying ~3000× while `I₁`, `I₂` are identical. It is the first formed
  read odd under `w ↦ −w` alone.
- **A.4** **every materialized edge is mixed** (`Δx⁰ ≠ 0` by D0.7; `ds² > 0` by FT.24/Def-BM.4(5)),
  so the on-shell data constrain the shift **per edge**, nullity `2E`.
- **A.5** the **longitudinal** shift is ledger-determined in closed form; the transverse `2E`
  dimensions are the momentum-constraint **gauge**.
- **A.6** the magnetic transition functional and its **attenuation theorem**, on marked
  specialization (S) — `⟨ψ⟩` maximal at `ε_q = 0`, crystallized value `2nc/√(1+4c²n²)`.
- **A.7** a **coherence defect in the frozen canon**: BM.140(6)'s boxed `ℛ_max/ℛ_min = 50/(1−𝔲)`
  is negative for a quantity provably positive, and is **unchecked** by the suite.
- **A.8** adjudication: the spine is closed end to end with no unconstructed link and exactly two
  unissued numbers (`𝔥`, `e₀`); six of my own earlier claims are withdrawn on the record.

## Tier A.2 — the bit/qubit distinction in tensor form (no global tick)

- **A.9** the carrier splits under the flip: `Π_ℛ = (I+F)/2` rank 3, `Π_𝒱` rank 1, and BM.131(4)'s
  two normalizations (`𝔗Π_ℛ = 3`, `𝔗Π_𝒱 = 1`) genuinely differ.
- **A.10** the twirl theorem verified **exactly with no integration**: the binary tetrahedral group
  `2T` (24 elements, entries in `ℤ[i]/2`, closure verified over all 576 products) acts irreducibly
  on `∨²` and trivially on `∧²`, so by Schur its average **equals** the Haar twirl.
- **A.11** the tensor form `𝒲_{ab}^{cd} = (Π_ℛ)_{ab}(Π_ℛ)^{cd}/3 + (Π_𝒱)_{ab}(Π_𝒱)^{cd}`:
  `𝒲² = 𝒲` (256 entries compared), **`rk 𝒲 = 2`**, and the rank drop **15 → 2 → 1**.
- **A.12** the commutant of `{W_i}` is exactly 2-dimensional (48 complex equations, 16 unknowns,
  nullity 2) ⟹ **`b(ρ) = 𝔗(Π_ℛρ)` is the UNIQUE free Haar-gauge-invariant parameter of the
  carrier.** This sharpens the direction given: the bit is not merely a block trace, it is the
  only invariant there is.
- **A.13** A4 thresholds the bit: `b ≥ 1−ε_q` → aligned `α=0` (weak-active), `b ≤ ε_q` →
  antialigned `α=π` (weak-blind), the open window unregistered. At `ε_q=0` only the two branch
  states register — total crystallization, no flicker.
- **A.14** the duality as the frame: Haar = exact gauge freedom of the record, Poisson = the
  recorded dynamics, unique common fixed point `¼I` at `x=3/4` (where `b = 3/4`), and
  `V_n = (1−γ/4)^{2n}V_0` depends on the **tilt count alone**. **`n` counts tilt events, not
  ticks** — no global tick is introduced anywhere in the tier.

## Known limitations, stated up front

- **A.6 rests on marked specialization (S)**, `w_i(R) = ω_i E_int(R)`, which is *not* derived —
  BM.90 ground (iv) bars a derived count→strength coupling. It is marked and ¬adopted, following
  BM.89(4)'s Bernoulli-specialization precedent. §Open-A (A-O1) is the row that would close it.
- **This is internal coherence plus exact arithmetic, not empirical validation.** `𝔥`, `e₀`,
  `ϰ`, `β` are unissued, and BM.140(5)/BM.83 prove `ρ_B` irreducibly calibration. "No structural
  gap remains in the magnetic sector" means *no gap given (S) and given calibration values*.
- The folder is **not** wired into `verification/run_all.py`, and `index/`, `tags.json` and
  `Summary.md` have **not** been regenerated. Both are deliberate: regenerating would assert that
  A.1–A.8 are canon tags, and they are not yet. Promoting this tier means running the era-chain and
  citation-closure checkers against it, which is a closure-phase act.
