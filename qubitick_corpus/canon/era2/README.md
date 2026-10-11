# `canon/era2/` — Level 5 · the **Atomic** era · Tier AT.1

**Status: discovery-phase working tier. NOT frozen canon.** Nothing here is adopted, no
declaration issues, §Cal-AT is empty, and no clause of Parts 1–4 is modified or retracted.

| file | content |
|---|---|
| `Part5_Atomic_era_TierAT1.md` | **Tier AT.1** — tags AT.1–AT.8 in canon format (Thm · Req · Pf · Phys), plus §Cal-AT and §Open-AT |
| `Part5_Atomic_era_TierAT2.md` | **Tier AT.2** — tags AT.9–AT.14: the tensor form of the bit/qubit distinction through BM.131's Haar–Poisson duality, **no global tick** |
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

## What Tier AT.1 claims, in one line each

- **AT.1** the bridge slot `β₃₁` is constructed: `β₃₁ = 𝔥`, per-edge coefficient `ln2` forced by
  `ln4 = 2 ln2` and `E_int = 2E_bidir + E_uni`. Def-H.39's "unconstructed" was a
  citation-direction artifact (Part 3 cannot cite Part 4).
- **AT.2** the metric's ten coordinates **are** the `S`-even subspace, split `7+3` by `T`;
  CT1.12a(2)'s `5+1+1+3` apportionment *is* CT1.1's block boundary, so the shift is T-odd by
  **index structure**, not by force attribution.
- **AT.3** the electromagnetic split is an observer-relative **reading**: one `F`, five exact
  rational observers, `E²` varying ~3000× while `I₁`, `I₂` are identical. It is the first formed
  read odd under `w ↦ −w` alone.
- **AT.4** **every materialized edge is mixed** (`Δx⁰ ≠ 0` by D0.7; `ds² > 0` by FT.24/Def-BM.4(5)),
  so the on-shell data constrain the shift **per edge**, nullity `2E`.
- **AT.5** the **longitudinal** shift is ledger-determined in closed form; the transverse `2E`
  dimensions are the momentum-constraint **gauge**.
- **AT.6** the magnetic transition functional and its **attenuation theorem**, on marked
  specialization (S) — `⟨ψ⟩` maximal at `ε_q = 0`, crystallized value `2nc/√(1+4c²n²)`.
- **AT.7** a **coherence defect in the frozen canon**: BM.140(6)'s boxed `ℛ_max/ℛ_min = 50/(1−𝔲)`
  is negative for a quantity provably positive, and is **unchecked** by the suite.
- **AT.8** adjudication: the spine is closed end to end with no unconstructed link and exactly two
  unissued numbers (`𝔥`, `e₀`); six of my own earlier claims are withdrawn on the record.

## Tier AT.2 — the bit/qubit distinction in tensor form (no global tick)

- **AT.9** the carrier splits under the flip: `Π_ℛ = (I+F)/2` rank 3, `Π_𝒱` rank 1, and BM.131(4)'s
  two normalizations (`𝔗Π_ℛ = 3`, `𝔗Π_𝒱 = 1`) genuinely differ.
- **AT.10** the twirl theorem verified **exactly with no integration**: the binary tetrahedral group
  `2T` (24 elements, entries in `ℤ[i]/2`, closure verified over all 576 products) acts irreducibly
  on `∨²` and trivially on `∧²`, so by Schur its average **equals** the Haar twirl.
- **AT.11** the tensor form `𝒲_{ab}^{cd} = (Π_ℛ)_{ab}(Π_ℛ)^{cd}/3 + (Π_𝒱)_{ab}(Π_𝒱)^{cd}`:
  `𝒲² = 𝒲` (256 entries compared), **`rk 𝒲 = 2`**, and the rank drop **15 → 2 → 1**.
- **AT.12** the commutant of `{W_i}` is exactly 2-dimensional (48 complex equations, 16 unknowns,
  nullity 2) ⟹ **`b(ρ) = 𝔗(Π_ℛρ)` is the UNIQUE free Haar-gauge-invariant parameter of the
  carrier.** This sharpens the direction given: the bit is not merely a block trace, it is the
  only invariant there is.
- **AT.13** A4 thresholds the bit: `b ≥ 1−ε_q` → aligned `α=0` (weak-active), `b ≤ ε_q` →
  antialigned `α=π` (weak-blind), the open window unregistered. At `ε_q=0` only the two branch
  states register — total crystallization, no flicker.
- **AT.14** the duality as the frame: Haar = exact gauge freedom of the record, Poisson = the
  recorded dynamics, unique common fixed point `¼I` at `x=3/4` (where `b = 3/4`), and
  `V_n = (1−γ/4)^{2n}V_0` depends on the **tilt count alone**. **`n` counts tilt events, not
  ticks** — no global tick is introduced anywhere in the tier.
- **AT.15** closes (AT-O10): the key identity `Π_ℛ = ¾E₀ + ¼Σ` gives `b = ¾ + ¼⟨Σ⟩`, so
  `⟨Σ⟩ = 4b − 3` and the bit is conjugate to the **spatial volume mode** `Σ_tr` (H aspect,
  T-even). The conjecture that the bit is the *shift's* carrier image is **refuted on an exact
  T-parity mismatch** — so specialization (S) is *not* retired and (AT-O1) survives. Of the
  metric's ten coordinates exactly one has a carrier-side gauge-invariant conjugate.

## Tier AT.3 — the capacity censor (directive executed, two steps corrected)

- **AT.16** the censor reproduced as exact integers: `D_tick(n)=2^{n+1}` [CT0.5],
  `C_cap = dim_R H(C^4) = 16` [CT0.6], `O(n)=max(0,2^{n+1}−16)` with `O(4)=16=C_cap` exactly,
  admissible `⟺ n ≤ 3` [CT0.11], and `N_colour = 3 = ⌊log₂16⌋−1` **derived** [Cor CT0.11a].
- **AT.17** **the directive's `j=0` claim is REFUTED**, on two independent exact grounds.
  `Sym^k(ℂ²)` is spin `j=k/2` (character computed to `k=8`, weights `{k,k−2,…,−k}` all multiplicity
  1); at `k=4` that is spin 2. And `𝒫_M^{(n)}F_{D⁻}𝒫_M^{(n)}=0` has **rank 0**, whereas a
  projection onto a singlet has rank 1 — **annihilation ≠ folding**. The mechanism is masking:
  retained in full, `¬∃` a deleted entry, norm 0 at accessible rungs.
- **AT.18** the density law `⟨ρ_{D⁻}⟩ = Σ_v O(n_v)(1−f_adm(n_v,p))` and its five anchors
  `(448, 896, 2976, 2240, 24384)` reproduced exactly as `V·O(2d)`; `w_{D⁻}=0` dust; the
  `D⁻`→"dark matter" naming **barred** by P5, recorded not adopted.
- **AT.19** the two faces of one capacity; the horizon form `r ≥ r_s(E) ⟺ E_int ≤ 2r/𝔥`;
  the one-hop capacity `E_crit(𝔥)=2`; **"no materialized cell is chart-formed at its own
  envelope"** on `E²ln2 ≥ ln16 > 2`; and **the formed censor is Schwarzschild-like, not Kerr** —
  BM.146(3)'s metric is diagonal, so the shift vanishes and the geometry is spherically symmetric.
- **AT.20** adjudication: three directive clauses corrected (`j=0`; "collapse"; "forbids
  higher-spin interactions" → it has *no* accessible coupling at any spin), one register fixed
  ("unbounded ladder of finite ranks", not "infinite ranked matrix"), and (AT-O12)–(AT-O14) opened.

## Tier AT.4 — the CP-assimilated tensor (directive executed, step 5 corrected)

- **AT.21** the Janus register: `Ĵ₊² = Ĵ₋² = 0`, `Q = x₊(Ĵ₊−P_𝒱) + x₋(Ĵ₋−P_ℛ)`,
  `(x₋,x₊)Q = (0,0)` exactly over `ℤ[x₊,x₋]`, and the **supply vertex is nilpotent**,
  `(Ĵ₊⊗Ĵ₊)² = 0` — "the register cannot supply a pair twice."
- **AT.22** the four exact weights `x₊²χ`, `x₋²χ`, `x₊x₋`, `x₊²x₋²`; `x₊x₋ = ¼−16(ε_q−⅛)²`
  as an identity in `ℚ[ε_q]`, maximized at **ε_q = ⅛**; detailed balance
  `𝒲_ann/𝒲_channel = 1 ⟺ ε_q = ⅛`; `σ_ann/σ_pair = (x₋/x₊)⁴·z²/(z²−4N²(2m_hid)²)`;
  `𝒯₀ = 4𝔥/ln2` at the minimal floor.
- **AT.23** the state space is **`T_J²(c) = (𝒥⊗𝒥) ⊗ H_meson(c)`, dim `16(|k|+1)²`** — and
  `H_meson` *cannot* separate the two histories, because both share orientation and winding. The
  distinction lives entirely in the 4-dimensional Janus factor.
- **AT.24** the corpus has **no history-kets**: `|Ψ⟩ = α|A⟩ + β|B⟩` is replaced by
  `Z = Z_A + Z_B`, two move-classes inside **one** Def-H.32 sum (BM.19(6) guarantees both at
  every `ε_q > 0`). `E_int` enters **four** ways — the threshold gate, `G`, `N`, and `𝗀`/`f` —
  never as a bare count.
- **AT.25** **step 5's premise is stale.** The no-annihilation row is *re-scoped, ¬retracted*:
  what stands is `¬∃` a **direct** `EM⁺→EM⁻` operator. The **mediated** channel
  `∅ →^{Ĵ₊⊗Ĵ₊} {c,c^CP} →^{Ĵ₋⊗Ĵ₋} ∅` is constructed [BM.123(5)], and **(R9), (R9′), (R9″) are
  all closed** [BM.123(6); BM.142(5),(8)] — including `σ_ann`. The real obstruction is the
  **mask**: `𝒫_M^{(n)}F_{D⁻}𝒫_M^{(n)} = 0`, so the resolvent has **no `D⁻` pole**, and `𝒯_𝒥(D⁻)`
  is undefined because `𝒥` is a *pair* register and `D⁻` is vertex excess.
- **AT.26** locus discipline: `w → −w` is the *metric* pullback [FT.156(3)], `Θ_𝔏` is the *record*
  reversal [D2.7], and FT.159(3) bars equating them. The directive's CP premise is **correct as a
  reading, barred as an operator identity**.
- **AT.27** verdict: **structurally valid on the meson floor, ¬formed on the `D⁻` sector.** Four
  missing rows named — (M1)–(M4). (AT-O15)–(AT-O19) opened.
- **AT.28 — SUBNETWORK OBSERVATIONAL EQUIVALENCE (corrects AT.27).** A locked `D⁻` interior and an
  internal `J⁺/J⁻` zig-zag network with the same boundary data are **indistinguishable by every
  accessible read**, on three independent rows: the mask (`𝒫_M^{(n)}F_{D⁻}𝒫_M^{(n)}=0`), FT.20's
  "`J^±` not observable", and CT1.12a(2)'s zero metric coordinates for the S-odd blocks — while
  both are **retained** (`¬∃` a deleted entry, `S_𝔏 = n_ℛln2` kept in full).
  **The decisive arithmetic:** `1 − f_adm(n,p) = Σ_{k≥4} C(n,k)p^k(1−p)^{n−k}` exactly in `ℚ[p]`,
  so `⟨ρ_{D⁻}⟩ = Σ_v O(n_v)·P(Binomial(n_v,p) ≥ 4)` contains **no `D⁻` datum** — the locked
  density *is* a Janus binomial tail in the retention probability `p = 1−4ε_q`.
  Valence-8 node: `O(8) = 496`, and the contribution falls strictly with `ε_q` — **the flicker
  relieves the oversubscription that feeds the lock.**
  Verdict: a **subnetwork-level gauge redundancy** (one accessible read, many unmasked
  representatives) — observational, *not* ontological, since in the unmasked A8 sum `D⁻` is a stack
  aspect and `J^±` are pair-arena aspects. **(M1) and (M2) DISSOLVE**; **(M3) sharpens** into a
  testable invariance of `w_i` across representatives, which may retire specialization (S).
  **History A and History B are two representatives of one boundary-data class, not two
  topologies.** (AT-O15)/(AT-O16) dissolved; (AT-O20)/(AT-O21) opened.

## Tier AT.5 — the boundary-invariance survey (all forces, all rungs)

- **AT.29** the coarse-graining principle is **already a theorem**, at three levels: **(P1)** the
  visibility bound `I_hid = E_tot − E_vis` [Def-H.9(2); FT.1]; **(P2)** the mask
  `F_M^(Σ) = 𝒫_M F 𝒫_M` [Def-H.15(3)]; **(P3)** the information-flux bound — *"coarse graining
  bounds the information flux, and **no construction could exist inside the bound**"*
  [BM.143(1), closing (R5) as **void**]. (P3) is a `¬∃`-statement about constructions.
- **AT.30** the per-aspect × per-rung census (9 aspects × 5 rungs). **EM.9b's telescoping
  verified exhaustively**: `Σ_i f_{v_i} = ½(σ_last − σ_first)` over **all 1016** sign assignments
  on chains of 3–9 edges. **Completeness FAILS, constructively**: FT.20's EM *criterion* is
  interior-sensitive while its *observable* is boundary-exact — **14 of 32** five-edge chains have
  `q = 0` at the termini and nonzero interior activity. So two subnetworks with identical boundary
  data can differ in **aspect membership**.
- **AT.31** the neutral baryon `Σ₁₂`: `E_int = 6 = 2+2+2`, `Θ_int = 2k ∈ 2ℤ`, `Π = 72k(ln2)²`,
  `𝒞 = 1 ⟺` one ε-type triple — and Census FT.35(4): **"the junction vertices are `D⁻`-configured."**
  So an *observable* seal already carries locked content: AT.28's configuration, realized.
  **The shatter is at the envelope, not the boundary** — and the new ordering:
  `Δx_B = 𝔥/(E ln2) < 𝔥 ≤ r_s = 𝔥E/2` for every admissible `E_int`, on BM.148(4)'s own
  certificate `ln16 > 2`. **The chart-breaking locus lies strictly inside the horizon** — a
  discrete censorship ordering, with a chart-formed shell outside it.
- **AT.32** **the generalised invariance:** the accessible content of any subnetwork is a function
  of **(the boundary-data triple, `|R|`, the rung `n`) and nothing else**. Every other datum is
  bounded out by exactly one of (P1)/(P2)/(P3). Verdict on "complete invariance": **false as
  stated, true on the accessible sector — and both halves are exact.** (AT-O22)–(AT-O24) opened.

## Known limitations, stated up front

- **AT.6 rests on marked specialization (S)**, `w_i(R) = ω_i E_int(R)`, which is *not* derived —
  BM.90 ground (iv) bars a derived count→strength coupling. It is marked and ¬adopted, following
  BM.89(4)'s Bernoulli-specialization precedent. §Open-AT (AT-O1) is the row that would close it.
- **This is internal coherence plus exact arithmetic, not empirical validation.** `𝔥`, `e₀`,
  `ϰ`, `β` are unissued, and BM.140(5)/BM.83 prove `ρ_B` irreducibly calibration. "No structural
  gap remains in the magnetic sector" means *no gap given (S) and given calibration values*.
- The folder is **not** wired into `verification/run_all.py`, and `index/`, `tags.json` and
  `Summary.md` have **not** been regenerated. Both are deliberate: regenerating would assert that
  AT.1–AT.8 are canon tags, and they are not yet. Promoting this tier means running the era-chain and
  citation-closure checkers against it, which is a closure-phase act.
