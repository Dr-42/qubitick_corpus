# `canon/era2/` — Level 5 · the **Atomic** era · Tiers AT.1–AT.7

**Status: discovery-phase working tier. NOT frozen canon.** Nothing here is adopted, no
declaration issues, §Cal-AT is empty, and no clause of Parts 1–4 is modified or retracted.

| file | content |
|---|---|
| `Part5_Atomic_era_TierAT1.md` | **Tier AT.1** — tags AT.1–AT.8 in canon format (Thm · Req · Pf · Phys), plus §Cal-AT and §Open-AT |
| `Part5_Atomic_era_TierAT2.md` | **Tier AT.2** — tags AT.9–AT.15: the tensor form of the bit/qubit distinction through BM.131's Haar–Poisson duality, **no global tick** |
| `Part5_Atomic_era_TierAT3.md` … `TierAT5.md` | **Tiers AT.3–AT.5** — AT.16–AT.38: the capacity censor, the CP-assimilated tensor, the boundary-invariance survey, the shell, the calibration floor |
| `Part5_Atomic_era_TierAT6.md` | **Tier AT.6** — AT.39–AT.40: the closure row and the gap-closure pass (committed in session 1 as `CLOSURE.md`; renamed for the uniform TierAT1–AT7 sequence) |
| `Part5_Atomic_era_TierAT7.md` | **Tier AT.7** — AT.41–AT.45: the hydrogen spine — the EM sealing grammar, the dynamics of Q, the binding-scaling no-go, the two-body resolvent, and the tier's closure row |
| `run_all_era2.py` | the tier's runner — gates first, exit 0 iff all green |
| `check_era2_format.py` | the format + citation gate: canon `math_balance` rules ported, per-block Thm/Req/Pf/Phys anatomy, and every cited tag attested against the canon registry |
| `qexact.py` | shared exact-arithmetic core (see below) |
| `SESSION_SUMMARY_AND_REVIEW.md` | session ledger, the model's error profile, and interaction review notes |
| the 28 `*.py` checkers | the machine verification (26 content checkers + the 2 validation gates); each cites the canon tags it reproduces or extends |

## Run

```bash
cd canon/era2 && python3 run_all_era2.py     # -> 28 checkers, 497 exact markers, 0 failures, exit 0
```

**Tier index.** AT.1–AT.8 (Tier AT.1) the coherence census and the split · AT.9–AT.15 (AT.2) the
bit/qubit tensor form · AT.16–AT.20 (AT.3) the capacity censor · AT.21–AT.28 (AT.4) the
CP-assimilated tensor and subnetwork equivalence · AT.29–AT.38 (AT.5) the boundary-invariance
survey, the shell, and the calibration floor · **AT.39–AT.40 (AT.6) the closure row and the
gap-closure pass** · AT.41–AT.44 (AT.7) the hydrogen spine: the sealing grammar, the dynamics of Q,
the binding-scaling no-go, the two-body resolvent · **AT.45 (AT.7) the closure row**.

**AT.40 — the gap-closure pass: eight more rows closed.**
- **AT-O19**: the five extrema at `ε_q = ⅛` are **ONE equation** — `d/dp[p(1−p)] = 1−2p = 0` and
  `(1−p)²−p² = 2p−1 = 0` are the same linear equation. Its structural meaning: **`ε_q = ⅛ ⟺ x₊ = x₋
  ⟺ Q = Qᵀ`**, i.e. the Janus master generator is **self-adjoint** and its stationary measure
  **uniform**.
- **AT-O12**: BM.149(1)'s two capacity faces are **provably independent** (two witnesses, one
  failing each way). "Two faces of one capacity" is a *role* statement, not an identity.
- **AT-O18**: `E_int = |R|` is a cardinality, hence exactly additive; BM.17's `2+2+2 = 6` is the
  witness. No correction term.
- **AT-O8**: **no-go** — the Poisson side has no tensor form, since `δK = γρ + log Z_γ·I` and
  `log Z_γ` is not linear in `ρ`. **The asymmetry is the duality's content**: Haar is a linear
  rank-2 idempotent tensor, Poisson is a nonlinear spectral flow.
- **AT-O9/O11**: `dim End_SU(2)((ℂ²)^⊗n) = Σm_j² = C_n`, the **Catalan number** (1,2,5,14,42,132,
  429,1430); `n=2` reproduces AT.12 exactly. At `n=4` there are **13 free invariants against the
  metric's 10 coordinates** — so AT-O11 is a **DICTIONARY gap, not an invariant gap**.
- **AT-O23b**: the shell's own read is the **signature-flip magnitude** `σ_shell(k) = −N² =
  k_crit/k − 1`, whose maximum **equals the shell's thickness** `k_crit − 1 = G/(4π) − 1`.
- **AT-O7**: the checker is **written**, not proposed — `1−𝔲 = −0.902113 < 0` against
  `ℛ_max/ℛ_min > 0`; fails on the present text, passes on the fix.

**Tier AT.7 — the hydrogen spine (session 2): AT.41–AT.45.** Discovery record:
`era2/EM_SEAL_GRAMMAR.md`, `era2/Q_DYNAMICS_BORNWIDTH.md`, `era2/BINDING_SCALING_NOGO.md`,
`era2/TWO_BODY_RESOLVENT.md`.
- **AT.41** the EM sealing grammar from the neutron template: the proton **is** Σ₁₂ with its two end
  registers flipped (`W₃(+1)=15` of `64`); `Q` is boundary-exact (EM.9b telescoping, all 1016
  assignments); the seal is a colour partition **independent** of the edge signs; the grammar
  **factors** — and `Q=+1` alone does *not* select the proton: the minimal sealed `Q=+1` is the
  δ-sealed **charged meson at `E_int=4`**, the proton is the minimal ε-sealed one at `E_int=6`.
- **AT.42** the dynamics of Q: the lepton–baryon interaction is ONE global Def-H.32 configuration
  sum; **infinite range = the absence of a local EM seal** (the unbounded geometric resolvent
  `1/(1−w²x₊x₋)` against FT.19's all-or-nothing truncation); the "orbital" is the **discrete
  Born-width distribution** `P(Δx_B)`, normalized, localized by binomial concentration, collapsing
  to one width at `ε_q=0`. BM.6(5)'s "¬constructed" is level-local — superseded for the structure;
  BM.48(4)'s category bar is strict — respected.
- **AT.43** the binding-scaling **no-go**, measured: the only exact `1/E_int²` derived functionals
  are geometric (`(Δx_B)²`, `1/G` — one object up to the lock constant); the derived binding
  `𝓑_ens` is **linear with opposite monotonicity**; the derived coupling `𝗀=1/(1+G)` misses the
  exact quarter by the algebraic residue `3/(4(1+4G₁)) > 0` (the π·ln2 cancels — an identity in
  `ℚ(G₁)`). Reopening conditions (R1)/(R2)/(R3) stated.
- **AT.44** the two-body resolvent — **(R3) met**: the k-channel return census
  `N_k(2m) = 2^{−k} Σⱼ C(k,j)(2j−k)^{2m}` (brute force ∧ transfer DP ∧ closed form), the exact
  partial fractionization, the **harmonic pole ladder** `w_d = 1/(d√(x₊x₋))`; in the native even
  variable `W=w²`: **`W_d/W_1 = 1/d²` EXACTLY — the 1/n² is a theorem of the move system**, with
  AT.42's geometry as an independent witness. The **lepton price** `w_c = 1/√(4ε_q(1−4ε_q)) ≥ 2`
  (SOS certificate `(8ε_q−1)²/4`; equality iff `ε_q=⅛`), alphabet `{ε_q}` **alone** — the curvature
  flux bypassed exactly. At `ε_q=⅛` the whole ladder is rational: `w_d=2/d`, `W_d=4/d²`, zero free
  parameters. AT-O5 closed **in species**; BM.83's incommensurability reclassified from obstruction
  to **species separation** — the bar stands and no longer blocks.
- **AT.45** the closure row: the consolidated ledger, the supersessions on the record, the open
  ledger with reasons, and the house cleaning — **four content-preserving format fixes** to the
  prior tier files (TierAT3 one unclosed `$$`; TierAT4 one stray `}`; TierAT5 a split inline math
  and a bare inline `$` inside a display; TierAT6 — then `CLOSURE.md` — AT.39's Req/Pf/Phys moved
  into its block), all
  found by the new `check_era2_format.py` gate.

**The sharpened open list, in priority order:**
1. **(AT-O14/O16)** compute `dim 𝒦_{n≥4}` — CT0.14's own method; **the only row that could unlock
   the locked sector**. Cheap and decisive.
2. **(AT-O6)** the anomalous moment — unchanged and now sharp: AT.44's resolvent is ¬spin-carrying;
   the spin–field coupling still needs the frame section [BM.6(8)]; BM.125(4)'s three grounds stand.
3. **(AT-O11)** extend CT1.12's dictionary past the pair arena to `n=4`.
4. **(AT-O7)** land the BM.140(6) pin and the re-citation-pinning convention.
5. **(AT-O13)** Kerr, once **(AT-O3)** issues `(ϰ,β)`.
6. **(AT-O26)** the level-price read rule of AT.44(8iv) — if ever adopted, a logged declaration
   (BM.30(5) pattern); a closure-phase act.
7. **(AT-O27)** `ε_q`'s value — ⅛ is derived as the unique distinguished point (now four ways),
   its **adoption** is ¬issued [P5]; calibration-era content.
**By nature / by design, not gaps:** (AT-O2) the slicing choice is gauge; (AT-O3) `(ϰ,β)` is
calibration. **Closed at Tier AT.7:** (AT-O4) the EM sealing grammar — grammar AT.41(5), dynamics
AT.42, spectrum AT.44(5); residual = calibration species. (AT-O5) the lepton mass read — formed
**in species** as the k=1 resolvent price AT.44(4); the `ε_q` value and the family splitting stay
calibration/Gram-currency. AT.43(R3) — met by AT.44. **Closed earlier:** AT-O1, O7 (checker
written), O8, O9, O10, O12, O15, O16, O17, O18, O19, O20, O21, O22, O23, O23b, O24, O25.

## The arithmetic covenant

Inherited unchanged from `verification/`: **exact arithmetic only, no floating point in any
assertion.** `Fraction`; `ℤ[x]` and multivariate `ℚ[γ,G,a]`; complex-over-`Fraction`; exact 4×4
matrices over `Fraction`; the prime-log ring `ℚ[ln2,ln3]`; and rigorous `Fraction` **intervals**
for every transcendental — Machin's formula for `π`, the `ln2 = Σ 1/(n2ⁿ)` series with an exact
tail bound, Archimedes `223/71 < π < 22/7` as a cross-check, and bisection `sqrt`. Tier AT.7 adds:
formal power series over `ℚ` with coefficient-wise equality; integer word enumeration and
transfer-matrix DP over `ℤ`; the parity-projected multinomial; SOS certificates in `ℚ[ε_q]`; and
symbolic identities in `ℚ(G₁)` (the `π·ln2` cancels — no numerics needed).

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
  citation-closure checkers against it, which is a closure-phase act — `check_era2_format.py` (F3)
  is the citation-closure half, already run: **every cited token in all nine Part 5 documents is
  attested** against the 640-tag canon registry.
- **Tier AT.7's scope, stated plainly.** The lepton price `w_c` is *generation-blind* (one read for
  the species; the family splitting lives in the Gram currency and is ¬mixed in), it is a
  *dimensionless price* (𝔮⁰ — a conversion to 𝔥-units is exactly what BM.140(5)/BM.83 forbid), and
  its identification with any chart mass is **barred** by BM.134(5) (the two resolvent species meet
  only through the threshold indicator). The `1/d²` *shape* is derived twice; the *read rule*
  (level price = squared dominant pole) and the chart-side scale `−ε²m_r/2` remain marked
  specifications (AT-O26). The `B→∞` universe limit is ¬constructed [Def-H.32(1)] — "universe-level"
  means the budget filtration with no local-seal truncation, never a completed infinite sum.
