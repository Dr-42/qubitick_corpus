# `era2/level5_atomic/` — Level 5 · the **Atomic** era · Tiers AT.1–AT.12 · **CLOSED**

**Status: CLOSED at AT.63 (Tier AT.12, session 8).** The level's record is closed: twelve tiers,
63 tags, no structural open row at closure. **NOT promoted into the frozen canon** — promotion is
an Era-2-closure act (after Levels 6–7) [AT.63(4)]. Nothing was adopted, no declaration issued,
§Cal-AT stayed empty through closure, and no clause of Parts 1–4 was modified or retracted. The
tier documents are the closed record: no further edits; future content opens new files with
explicit supersession rows.

| path | content |
|---|---|
| `tiers/Part5_Atomic_era_TierAT1.md` | **Tier AT.1** — tags AT.1–AT.8 in canon format (Thm · Req · Pf · Phys), plus §Cal-AT and §Open-AT |
| `tiers/Part5_Atomic_era_TierAT2.md` | **Tier AT.2** — tags AT.9–AT.15: the tensor form of the bit/qubit distinction through BM.131's Haar–Poisson duality, **no global tick** |
| `tiers/Part5_Atomic_era_TierAT3.md` … `TierAT5.md` | **Tiers AT.3–AT.5** — AT.16–AT.38: the capacity censor, the CP-assimilated tensor, the boundary-invariance survey, the shell, the calibration floor |
| `tiers/Part5_Atomic_era_TierAT6.md` | **Tier AT.6** — AT.39–AT.40: the closure row and the gap-closure pass (committed in session 1 as `CLOSURE.md`; renamed for the uniform TierAT1–AT7 sequence) |
| `tiers/Part5_Atomic_era_TierAT7.md` | **Tier AT.7** — AT.41–AT.45: the hydrogen spine — the EM sealing grammar, the dynamics of Q, the binding-scaling no-go, the two-body resolvent, and the tier's closure row |
| `tiers/Part5_Atomic_era_TierAT8.md` | **Tier AT.8** — AT.46–AT.49: the spin spine — the duality tool and the polygon spin holonomy, the frame section on the extended carrier, the ledger-native moment coupling, and the tier's closure row |
| `tiers/Part5_Atomic_era_TierAT9.md` | **Tier AT.9** — AT.50–AT.55: the locked sector (dim 𝒦_{n≥4}=26, the third branch), the electroweak curl mechanism, **the dressed vertex correction** (the discrete Ward identity δ=0, the winding revival ladder, the measure-side anomalous read), and the tier's closure row |
| `tiers/Part5_Atomic_era_TierAT10.md` | **Tier AT.10** — AT.56–AT.58: **the Pauli term as a ledger object** — the σ^{μν} bivector census on the native frame (two channels, no third, the Hodge row, the ray-wise so(4) split), the slot-free Weitzenböck identity (the Pauli term born from the Dirac skeleton's square at tree coefficient 1), the transport-curvature census (drag fiber-abelian; EW.32 Gaussian-integer), the structural F₁/F₂ dictionary, and the tier's closure row |
| `tiers/Part5_Atomic_era_TierAT11.md` | **Tier AT.11** — AT.59–AT.62: **the resolution tier** — the metric dictionary at every carrier level (AT-O11 CLOSED: the conjugacy theorem, pair bits, exchange-fed kernel), the global Dirac-type operator on the tetrahedral floor (AT-O28 CLOSED AS CONSTRUCTION: the chirality dichotomy of the lift, the dissolved base frame, the discovered vielbein), the fine-splitting grammar and the exhaustive seat census (AT-O31 resolved as grammar; AT-O6 CLOSED outright), and the tier's closure row |
| `tiers/Part5_Atomic_era_TierAT12.md` | **Tier AT.12 — THE CLOSURE TIER** — AT.63: the consolidated level ledger (twelve tiers, AT.1–AT.62), the closure adjudication, the final open ledger (no structural row), the declaration census (zero issued), the two-halves repository reorganization, and the machine state at closure |
| `tiers/Part5_Atomic_era_TierA1.md`, `TierA2.md` | the two early session-1 working drafts, kept for provenance (superseded by the TierAT1 sequence) |
| `checks/run_all_era2.py` | the level's runner — gates first, exit 0 iff all green |
| `checks/check_era2_format.py` | the format + citation gate: canon `math_balance` rules ported, per-block Thm/Req/Pf/Phys anatomy, and every cited tag attested against the canon registry (reads `../tiers/` and `../../../canon/`) |
| `checks/qexact.py` | shared exact-arithmetic core (see below) |
| `checks/duality.py` | shared View1↔View2 duality core — the dictionary rules (D1)–(D6): sector→ADM (CT1.12≡BM.34(1)), the AT.5(1) closed form, the flat/drag split, holonomy reads, exact polygons (`Quad(√d)`), the H_ω doublet over `Gauss(i)` |
| the 37 `checks/*.py` checkers | the machine verification (35 content checkers + the 2 validation gates); each cites the canon tags it reproduces or extends |
| `discovery/*.md` | the free-form session records: session 1–2 (`MAGNETISM_ROUTE.md` … `ONE_FORCE_SPLIT.md`, `CENSUS_L5.md`, `COHERENCE_CENSUS.md`, `M1_SHIFT.md`), sessions 2–3 (`EM_SEAL_GRAMMAR` … `TWO_BODY_RESOLVENT`, `SPIN_HOLONOMY`, `FRAME_SECTION`, `MOMENT_COUPLING` — cited by the tiers but never committed; they lived in the session workspaces), session 4 (`RUNG4_EW_CURL.md`), session 5 (`VERTEX_CORRECTION.md`), session 6 (`PAULI_TERM.md`), session 7 (`RESOLUTION_TIER.md`) |
| `discovery/logs/` | historical run outputs (`*_OUTPUT.txt`) |
| `discovery/legacy_checks/` | session-1 checker copies (provenance; NOT live — see its README) |
| `SESSION_SUMMARY_AND_REVIEW.md` | session ledger, the model's error profile, and interaction review notes |

**Path map for historical citations.** Tier documents and discovery records written before the
session-5 restructure cite the old loci; the files moved, the citations stay as written:

| old citation | current location |
|---|---|
| `canon/era2/<checker>.py` | `era2/level5_atomic/checks/<checker>.py` |
| `canon/era2/Part5_Atomic_era_*.md` | `era2/level5_atomic/tiers/Part5_Atomic_era_*.md` |
| `canon/era2/RUNG4_EW_CURL.md` | `era2/level5_atomic/discovery/RUNG4_EW_CURL.md` |
| `era2/<session doc>.md` | `era2/level5_atomic/discovery/<session doc>.md` |
| `qubitick_corpus/` (the nested published copy) | `archive/zenodo_v1.0_package/` |
| `canon/` (the v1.0 canon tree; cited historically) | `era1/canon/` (moved at the Level-5 closure, AT.63(5)) |
| `verification/` (the frozen 80-checker suite) | `era1/verification/` (moved with its canon, sibling-locked by symlinks) |

## Run

```bash
cd era2/level5_atomic/checks && python3 run_all_era2.py     # -> 37 checkers, 643 exact markers, 0 failures, exit 0
cd era2/level5_atomic/checks && python3 check_era2_format.py # -> 14 tier documents PASS, 0 violations
```

**Tier index.** AT.1–AT.8 (Tier AT.1) the coherence census and the split · AT.9–AT.15 (AT.2) the
bit/qubit tensor form · AT.16–AT.20 (AT.3) the capacity censor · AT.21–AT.28 (AT.4) the
CP-assimilated tensor and subnetwork equivalence · AT.29–AT.38 (AT.5) the boundary-invariance
survey, the shell, and the calibration floor · **AT.39–AT.40 (AT.6) the closure row and the
gap-closure pass** · AT.41–AT.44 (AT.7) the hydrogen spine: the sealing grammar, the dynamics of Q,
the binding-scaling no-go, the two-body resolvent · **AT.45 (AT.7) the closure row** · AT.46–AT.48
(AT.8) the spin spine: the duality tool and the polygon holonomy, the frame section, the moment
coupling · **AT.49 (AT.8) the closure row** · AT.50–AT.51 (AT.9) the locked sector and the
electroweak curl · AT.52–AT.54 (AT.9) the dressed vertex: the revival ladder, the Ward identity,
the anomalous read · **AT.55 (AT.9) the closure row** · AT.56–AT.57 (AT.10) the Pauli anatomy:
the bivector census and the two-channel decomposition, the Weitzenböck birth and the transport
curvature · **AT.58 (AT.10) the closure row** · AT.59–AT.61 (AT.11) the resolutions: the n-fold
metric dictionary, the global Dirac operator on K₄, the fine-splitting grammar and the moment
sector's exhaustive seat census · **AT.62 (AT.11) the closure row** · **AT.63 (AT.12) THE LEVEL
CLOSURE**.

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

**Session 3 — CONSOLIDATED as Tier AT.8 (AT.46–AT.49): the duality tool and the spin sector.** `duality.py` (the reusable
View1↔View2 core, rules (D1)–(D6)) + `spin_holonomy.py` (**18/18 exact**) + `frame_section.py`
(**19/19 exact**, candidate AT.47 — the spacetime spin factor is Def-H.34's triple and is MAXIMAL:
gauge-trivial Cl(3,0), no fourth gamma (nullity 0); the relocation row γ_{F₀}=σ₀⊗σ₃=I⊗κ̂ — FT.93's
example pseudoscalar IS Def-H.34's partner involution, the pincer arena-relative; the weak-scalar
frame shortlist = 6 frames, one S-orbit, the six seed-only SINGLETONS; the section reduces to one
base frame per arc-transitive floor under the marked lift; de Moivre transport exact with the
fourth-root lattice Lφ∈(π/2)ℤ; and the unification: AT.46's drag operator = exp(i(π/2)Θ_drag κ̂) —
the polygon's discrete spin connection IS the pseudoscalar's fourth-root exponential. Discovery
record `era2/FRAME_SECTION.md`.) + `moment_coupling.py` (**17/17 exact**, candidate AT.48 — the
ledger-native moment coupling: the VANISHING LEMMA (Σ_v f_v ≡ 0 on every configuration — the naive
total contraction is identically zero, proved); the two non-vanishing native channels — the
boundary-channel operator identity M̂ = (Σ_int f_v)·γ_{F₀} = −q_EM·(I⊗κ̂) (chirality-FLIPPING,
{M̂,χ̂}=0, chiral-basis off-diagonal −q·I⊗σ₁, splitting 2|q| with splitting-per-charge exactly 2)
and the frozen A8 activity dressing (−1)^ℵ; the exact dichotomy — boundary channel FLICKER-IMMUNE
(q preserved on 𝓔(𝒳) [Def-BM.5(1)]), the dressing FLICKER-SENSITIVE (the anomalous part is the
fluctuation correction); ε_total = i^Θ(−1)^ℵ closed within the fourth roots; the VECTOR contraction
Σᵢ(EM)ᵢσᵢ⊗σ₂ is a HARD NO-GO (EM is a stack aspect with zero metric coordinates — no native EM
index exists; the smooth σ^{μν}F_{μν} decomposes into the pseudoscalar channel + AT.6's
shift-mediated channel); BM.125(4)'s three grounds passed one by one, BM.126's {ε_q} alphabet
untouched. AT-O6 CLOSED AS STRUCTURE for the coupling; discovery record `era2/MOMENT_COUPLING.md`.) All three
constructions are consolidated in `Part5_Atomic_era_TierAT8.md` (AT.46–AT.48, closure row AT.49);
the open ledger now runs: AT-O14/O16 (priority 1), AT-O11, AT-O7's convention, AT-O13, AT-O26,
AT-O27, **new AT-O28** (the global Dirac-type operator — two enumerated slots away: the lift + the
base frame per floor), **new AT-O29** (a native vector EM read — proved structural absence,
by-nature row). the polygon shift
holonomy — zero for constant shift (telescoping), forced nonzero up to one scale on arc-transitive
floors (AT.34's field, by integer group transport), orientation-odd, and **Diophantine-quantized**
by FT.22/FT.24-25; the H_ω doublet splits by exact fourth-root phases, with a **statistics-flip
law** (ε₊≠ε₋ ⟺ Θ_drag odd — witnessed: one geometry, two orientations, opposite statistics
classes); the Frenet-lift vs exchange-sign census (two distinct reads, agreeing exactly on L odd ∨
L≡2 mod 4 — FT.55(1)'s bar at parity level). Adjudication: the ledger drag holonomy is the spin
connection's **dictionary partner, ¬its equal**; Open Gaps 19 stays declared; **AT-O6 sharpened** —
the drag/spin-orbit polygon sector is derived, and the exact missing definition is BM.6(8)'s frame
section e↦F_e (the polygon's symmetry gives the forced *line*, not a *section*). Candidate tag
**AT.46**; discovery record `era2/SPIN_HOLONOMY.md`; tier consolidation pending.

**Session 4: rung 4 and the electroweak curl.** `rung4_ew_curl.py` (**13/13 exact**, candidates
AT.50/AT.51): **dim 𝒦^(D⁻) = 1 by a four-row squeeze** — lower bound CT0.14's frozen strictness
𝒦₃⊂𝒦_{n≥4}, upper bound the scalar-sink rows (CT4.4 "no internal directions", D4.1 "SINGLE
possibility space" — the ⊕ collapses, CT4.6, CT4.4a(1)) — hence **dim 𝒦₄ = 26 and the flag
TERMINATES** (dim 𝒦_n = 26 for every n≥4; the method re-executed: the census reproduces
(6,16,17,25) on the nose). The lock is a **BICONDITIONAL**: D⁻∈𝒜(n) ⟺ n≥4 ⟺ 2^{n+1}≥32>16=C_cap
⟺ NOT channel-admissible (verified n=0..16) — activation and admissibility are disjoint at every
rung. The adjudication lands on a **third branch**: at n≥4 the formal projection does NOT
annihilate the sink (𝒦^(D⁻)⊆𝒦_n by D2.3) — nonzero as a formal object — but ι₄ is unrealized
[CT4.4a(1)], accessible vertex sets are {V₀..V₃} [CT0.11], and every accessible mask runs at rung
≤3 [AT.16(4),(5)]: **NONZERO-BUT-UNREACHABLE**, and even formally the sink is structureless
(CT4.4/4.5/4.7; BM.143(1)). **AT-O14/O16 CLOSED**; AT-O11 becomes fully decidable (AT.40's own
condition "once dim 𝒦_{n≥4} is known" is met). The Architect's electroweak hypothesis is verified
as **assembled derived structure**: 𝒦^(EM)=Z(u(2))=1 vs F_W=su(2)=3 (3+1=4=dim u(2)),
co-activated at every EM rung (𝒜(2)=𝒜(1)∪{EM} — no rung with EM on, W off); the curl mechanism in
four derived steps — topology-blind containment [Def-H.32(1)], the **branch gate** (ΣWᵢ²=2Π_ℛ,
WᵢΠ_𝒱=0, machine 4×4 over ℚ(i): the weak curls only the aligned branch), **cover mediation** (lone
cycles amplitude-dead [FT.106(2)]; dissolved digons live at winding one, 802/4796 [FT.106(3)]), and
the **Gram closure-detector**: M=¼NᵀN with N=[[g,0,0,0],[0,g,0,0],[0,0,g,g']] — PSD rank 3,
spectrum {g²,g²,0,g²+g'²}/4 [BM.36], kernel line (0,0,g′,−g) = the "photon" profile: G(c)=‖Nc‖²/4
= 0 **iff** kernel — a curled photon profile stays massless at every coupling, every off-kernel
profile curls into a pole mass (family circle strictly positive via the SOS
A₀−B₀=(3/8)(g−g′/3)²+g′²/48, verified coefficient-wise in ℚ[g,g′]). **The bound:** a
colour-neutral curl reaches the **polygon** ladder (2D floors, Θ_R=0 [FT.54(4)]) but NOT platonic
solids — the 3D seals are ε/δ junctions on **colour** slots [D3.9/CT3.17a(1)] and the EW seed is
colour-neutral [EW.32: T_a𝗏=0]: "polygon or platonic" SPLITS — polygons yes, platonic iff colour
attachments are present. Discovery record `discovery/RUNG4_EW_CURL.md`; consolidated in
`Part5_Atomic_era_TierAT9.md` (session 5).

**Session 5 — CONSOLIDATED as Tier AT.9 (AT.50–AT.55): the dressed vertex correction.**
`vertex_correction.py` (**23/23 exact**, candidates AT.52–AT.54; discovery record
`era2/VERTEX_CORRECTION.md`). The directive: evaluate M̂ = −q_EM(I⊗κ̂) [AT.47(3)/AT.48(2a);
Def-H.43] in the FULLY DRESSED topology-blind ensemble and isolate δ := ⟨M̂⟩_dressed −
⟨M̂⟩_tree. Results, in order of load:
- **THE DISCRETE WARD IDENTITY (AT.53): δ = 0 EXACTLY** — as a 4×4 `Gauss(i)` matrix identity, in
  every (q,S) sector, at both layers, at both fugacity specializations, over every interleaving
  and cover of the censused cells. Three independent supports: the **chain-local telescoping
  extension** (Σ_int f_v = ½(σ_last−σ_first) on every path of every configuration *including hub
  interiors* — EM.9b's type-(1,1) clause is a scope, not an obstruction), the charge preservation
  on 𝓔(𝒳) [Def-BM.5(1)], and the sector-constancy of the promoted read. The tree splitting 2|q|
  is ¬renormalized by any dressing.
- **THE MASTER PARITY IDENTITY (AT.53): (−1)^ℵ = Π_{cov odd} σ_e** on every configuration (668 +
  59,049 checked in-census, zero violations; FT.67(1) multiplied out). Corollaries: (−1)^{|q|} on
  single open chains (exhaustive L=2..9), +1 on closed, Π_eσ_e on covers. **The A8 dressing sign
  is SECTOR-LOCKED** — AT.48(5ii)'s "flicker-sensitive dressing" REFINED on the record: ℵ's value
  fluctuates, its parity is charge data; ε_total = i^Θ(−1)^{|q|}.
- **THE ω-SPLIT of the amplitude layer (AT.53):** the involution σ↦−σ forces
  contribution_R(−q) = (−1)^{|R|}contribution_R(q): norm/cover/non-cover-even symmetric,
  non-cover-ODD antisymmetric ⇒ Z^amp_ncO(0,S)=0 exactly; the hexagon cell exhibits the asymmetry
  LIVE (11,348 vs 19,060 at q=(−1,+1), S=0; difference = 2×(−3856)) — FT.106(3b)/(3d) mechanized
  per cell.
- **THE WINDING REVIVAL LADDER (AT.52): B_min(m) = 2m + ⌈m/2⌉** — every winding m≥1 is
  amplitude-live from that budget: tight witnesses at V=(3,5,8,10,13) for m=1..5 (values
  16/64/1024/4096/65536, brute-force sign sums exact); m=1 IS FT.69(5)'s locked double-digon hub.
  **The minimal winding-2 cover: the V=5 THETA pattern** (two dissolved 4-cycles sharing a 2-edge
  path, v=64, 8 live S=2 instances), minimality exhaustive (V≤4: zero 4-cycle covers in 4095
  patterns — FT.106(3c)'s death row re-derived as B=4-local; V=5: 262,599 subsets → exactly 60
  patterns at |R|=6, one isomorphism class). **FT.106(3c) RE-SCOPED on the record** (the frozen
  cube/octahedron rows already carried 504/672 four-cycles); odd cycles stay dead at every budget.
- **THE LOCK PARITY (AT.52): odd windings are born LOCKED, even born clean** — pigeonhole: for odd
  m the ⌈m/2⌉ off-cycle centres feed m+1 hub-endpoints to m hubs ⇒ a k_v=4 hub [CT4.5]; both V=8
  winding-3 threadings lock; the first unlocked hexagon cover sits at V=9. Parallel to the
  odd-winding↔fermion-sign row FLAGGED, ¬identified [P5].
- **THE ANOMALOUS READ IS MEASURE-SIDE, EXACT, RATIONAL (AT.54):** residues a_{k,d} =
  2^{1−k}C(k,(k+d)/2) and contact terms c_k = 2^{−k}C(k,k/2) [k even] in the partial
  fractionization of R_k (sum rule = 1); attenuation ladders monotone (d=1: 1, ¾, ⅝, 35/64; d=2:
  ½, ½, 15/32, 7/16); **the ℵ-excess means** ⟨ℵ⟩^{(n)} a polynomial identity in ℚ[u] — excess =
  1/6 (n=2), 3/7 (n=3) at ε_q=⅛; **the first amplitude-live winding-2/3 sector censuses** (engine
  certified on BM.137(4)'s frozen (4,2,2) row and FT.106(3b)'s cancelling support): theta cell
  Z^amp(q,2)=(128,256,128), hexagon cell Z^amp(q,3)=(2816,6656,2816), with the full three-way
  split; **POSITION vs RESIDUE (the Lamb analog): the 1/d² ladder is exactly position-degenerate
  across channel counts — the dressing splits residues and diverts contacts, NEVER positions: an
  intensity redistribution, not a frequency shift.**
- **THE ADJUDICATION:** BM.125(4)'s three grounds bypassed (operator-valued / ¬mass-product /
  all-𝔮⁰ census); BM.126(1)'s {ε_q} alphabet untouched (k = the floor's pair count, ¬a spin
  read); **AT-O6 CLOSED AS DRESSED STRUCTURE**; the continuous a=(g−2)/2 a **level-local no-go
  with three named missing definitions** (M1′ the measure→chart read rule, AT-O26-class; M2′
  ε_q's value, AT-O27; M3′ the chart scale + e₀) — sharper than AT.48(5v): **no continuous locus
  exists**, since every dressed operator read is sector-constant; **AT-O11 DOES NOT BLOCK** (zero
  dictionary calls — the calculation lives on the pair arena, the k-channel resolvent, and frozen
  censuses); **new AT-O30** (the B≥5 winding-resolved cover census — blocking nothing).
  Quarantine [P5] untouched: a_e, a_μ, a_μ/a_e≈1.0054, the Lamb shift, 2S–2P — scoring targets,
  ¬inputs, ¬compared.

**Session 6 — CONSOLIDATED as Tier AT.10 (AT.56–AT.58): the Pauli term as a ledger object.**
`pauli_term.py` (**23/23 exact**; discovery record `discovery/PAULI_TERM.md`). The directive:
*"Please continue on the Pauli things."* The threads executed: AT.48(3)'s decomposition theorem
(stated, never mechanized), AT-O28's slot-free algebraic core, and `frame_section.py`'s residue
(iv). Results, in order of load:
- **THE BIVECTOR CENSUS (AT.56): the six σ^{μν} = (i/2)[γ_μ,γ_ν] on the native frame F₀ are
  signed Pauli products** — six distinct directions of the 15, species 3 mixed + 2 off-diagonal
  + 1 diagonal — and split into the exact channel identities **σ^{ab} = −2ε_{abc}W_c^ext** (the
  magnetic bivectors ARE the gauge block of the extended carrier, index-carrying exactly as
  AT.47(2)'s maximality theorem demands) and **σ^{a4} = σ_a⊗κ̂ = (σ_a⊗I₂)γ_{F₀}** (the electric
  channel = the internal Pauli × the shortlist pseudoscalar = M̂'s matrix). The bridge
  σ^{a4} = −ε_{abc}σ^{bc}γ_{F₀} makes the two channels the two grades of ONE Cl(3,0); the
  generated algebra is exactly 8-dimensional — **the Pauli term adds ZERO new operators**.
- **THE DECOMPOSITION MECHANIZED, NO THIRD CHANNEL (AT.56): σ^{μν}F_{μν} = −4𝔅_c W_c^ext +
  2𝔈_a(σ_a⊗κ̂)** as an exact matrix identity (basis + integer trials + additivity), with a
  zero-component census in the other 9 Pauli directions, in I₄, and in I⊗κ̂ — the last is the
  **grade separation**: M̂ is never a bivector contraction, it is the electric channel's grade-4
  partner (AT-O29's vector no-go, now with its exact grade reason). Adversarial witnesses keep
  the census non-vacuous.
- **THE HODGE ROW (AT.56, new): σ^{μν}γ_{F₀} = −(*σ)^{μν}** (ε₁₂₃₄=+1, the frame's Euclidean
  read), hence **(σ^{μν}F_{μν})∘M̂ = q·σ^{μν}(*F)_{μν}: the boundary moment operator IS q × the
  Hodge rotation** — the channel exchanger electric↔magnetic. Dictionary partner of the smooth
  EM duality rotation, ¬equal [BM.134(5)].
- **THE RAY-WISE so(4) SPLIT (AT.56, new): 𝖲^±ᵢ = ½(σ^{i4} ± *σ^{i4}) = ∓(σᵢ⊗I₂)P_±** — the two
  su(2) copies of the Pauli tensor live on the TWO RAYS of the orientation doublet [Def-H.33;
  FT.93(2)'s projectors], commuting because P₊P₋=0; [𝖲^±,𝖲^±] = ∓2iε𝖲^± exact. The born term
  acts ray-wise (grade-even); M̂ flips rays [AT.48(4)] — exact grade-conjugates.
- **THE WEITZENBÖCK IDENTITY (AT.57), SLOT-FREE AND FULLY SYMBOLIC:** on 𝒟 = Σγ_a⊗T_a with the
  four transports as INDEPENDENT INDETERMINATES (16 variables; 416 monomials cancelled):
  **𝒟² = I⊗(ΣT_a²) − (i/2)σ^{μν}⊗𝔉_{μν}**, 𝔉_{ab}:=[T_a,T_b] — the Pauli term born from the
  skeleton's square **at tree coefficient exactly 1, for every slot choice**: AT-O28's two slots
  block the evaluation, never the algebra. The coefficient-is-a-theorem witness: all T equal ⟹
  𝔉≡0 ∧ 𝒟² = (Σγ)²⊗T² — **the algebraic root of AT.48(5i)'s flagged tree parallel**
  (identification with any measured g stays QUARANTINED [P5]). The born term re-splits
  symbolically into 2iW_c^ext⊗𝔅_c − i(σ_a⊗κ̂)⊗𝔈_a — curvature feeds exactly the two channels.
- **THE DRAG CONNECTION IS FIBER-ABELIAN (AT.57): diag(i^Θ,i^{−Θ}) = U(πΘ/2, ẑ)** — the drag
  exponential IS the ẑ-axis EW.32 member; all drag transports commute ⟹ **the drag NEVER births
  a Pauli term**; its whole contribution sits in ΣT_a² — the winding/statistics side [AT.46(6)].
  *Frame-dragging changes how a polygon exchanges, not what moment it couples.*
- **THE EW.32 CURVATURE (AT.57): [U_a,U_b] = −2i sinφ_a sinφ_b((n̂_a×n̂_b)·σ⃗)** — 576 exact
  identities; on the fourth-root lattice: 12 transports, 66 pairs, **exactly 12 nonzero
  curvatures, every value ±2iσ_k — Gaussian integers**: NO CONTINUOUS LOCUS at the operator
  layer, the connection-side confirmation of AT.54(6). Two ℂ⁸ integer witnesses: a PURE born
  term (Laplacian part exactly zero) and a both-channels-live square.
- **THE STRUCTURAL F₁/F₂ DICTIONARY (AT.58):** F₁-type seat = the boundary channel (flicker-
  immune, Ward-protected δ=0 [AT.53(3)]); F₂-type seat = the measure dressing (AT.54's
  rationals); operator-layer seat = the curvature-born gauge channel (Gaussian-integer valued,
  slot-dependent in evaluation only). Values stay behind (M1′)–(M3′) [AT.54(6)] — nothing
  converted, nothing compared [P5].
- **THE ADJUDICATION:** AT.48(3)'s decomposition theorem **MECHANIZED AND COMPLETED**;
  `frame_section`'s residue (iv) **SUPERSEDED IN SCOPE** (the slots were needed for the
  EVALUATION, never the algebra); **AT-O28 ADVANCED, ¬CLOSED** (the slot-free core constructed;
  the global operator still needs the two marked slots + the P4 transport profile); BM.125(4)'s
  three grounds re-passed; BM.126(1)'s {ε_q} alphabet untouched; the other Pauli (exclusion,
  dim∧³(ℂ²)=0 [BM.128(5)]) re-certified and standing; **new AT-O31** — the fine-structure-type
  read of the hydrogen connector: seats identified (the ray-wise 𝖲^± su(2), the Hodge rotation,
  the measure rationals), blocked by (M1′)–(M3′) + the AT-O28 slots, blocking nothing.
  Declarations issued: none.

**Session 7 — CONSOLIDATED as Tier AT.11 (AT.59–AT.62): THE RESOLUTION TIER.** The directive:
*"Please proceed to resolve AT-O11, 28, 06, and 31 for the next tier."* All four resolved.
Three new checkers: `dict_nfolds.py` (**13/13**), `global_dirac.py` (**12/12**),
`fine_structure.py` (**8/8**); discovery record `discovery/RESOLUTION_TIER.md`.
- **AT-O11 CLOSED (AT.59) — the conjugacy theorem.** The squeeze (isotypic projectors by exact
  Lagrange interpolation in S²_tot; Σmⱼ² = the Catalans 2/5/14 = the permutation-span ranks):
  **the commutant IS the permutation span** — invariant reads = exchange reads. The embedding
  census (160 tests, AT.12(1)'s own criterion): **exactly Σ^(ij) (volume/H) passes at every n,
  every pair** (+ E₀ = trace-fixed identity); W-embeddings fail because Wᵢ^(12) = Sᵢ *is* the
  gauge generator, G as spin-2, J± as adjoint — **the AT.15(5) "none" rows are theorems at every
  level; conformal/shear/shift NEVER acquire conjugates**. Positive supply: pair bits
  b_(ij) = ¾+¼⟨Σ_(ij)⟩ (Π_𝒭^(ij) idempotent, trace 3·2^{n−2}), **the Casimir identity
  ΣΣ_(ij) = 2S²_tot − (3n/2)I** — the total volume read IS the isotypic-weight read; ranks
  r₂,r₃,r₄ = 1,3,6, central intersection exactly the Casimir line. Accounting: 13 = 6 volume +
  7 metric-blind exchange coherences — **the "13 vs 26" framing corrected on the record as a
  cross-currency count** [BM.83]; *the higher carriers see more of each other, not more of the
  metric*. Scope: n=3 accessible; n=4 formal [CT0.5/6/11; AT.50(5)]. BM.131(6)'s Π_k shown to
  BE the top isotypic projector (matrix equality), its "k invariants" suggestion stays superseded
  by AT.40(5).
- **AT-O28 CLOSED AS CONSTRUCTION (AT.60) — the global Dirac-type operator is built.**
  𝒟_floor = Σ_edges(E_vw⊗γ_{a(e)}(F_e)⊗T_e + h.c.) on ℂ⁴_v⊗ℋ_ext⊗ℂ²_T (32-dim), 72+ operators
  censured: Hermitian by the reverse-arc-dagger convention; sections rebuilt for both marked-lift
  readings (seed-only: 6 fixed points → constant, 144 checks; diagonal: 2 orbits × 3, 12 signed
  directions over the arcs). **THE CHIRALITY DICHOTOMY: the grading nullity — a gauge invariant —
  is exactly 1 (seed-only: chiral-odd, ±-paired spectrum, kernel reads; nullities 0 on the four
  witness profiles) vs exactly 0 (diagonal: no grading, no index): the lift declaration DECIDES
  WHETHER THE GLOBAL OPERATOR HAS AN INDEX** — Open Gaps 19's exact physical content, derived.
  **Slot (b) DISSOLVED:** the S-transform Φ = Ad(I₂⊗S) (DERIVED) is an automorphism (105
  identities) with ONE orbit of 3 frames × the sign involution = the 6-menu, and
  (V⊗I)𝒟(F,T)(V⁻¹⊗I) = 𝒟(ΦF,T) exactly — **the base-frame slot is a derived gauge** (first slot
  ever retired by construction). **THE GLOBAL WEITZENBÖCK: 𝒟²_floor = 3·I₃₂ + triangle blocks
  exactly** — the diagonal is the transport-blind degree Laplacian; ALL curvature lives on the
  2-simplices; triangle holonomies: integer windings (drag, Θ∈{±1,±3}) and Gaussian integers
  (EW lattice). **NEW SLOT named: the discrete vielbein a(e)** — Rot transitive on the 6 edges ⟹
  no non-constant equivariant labeling exists (4⁶ = 4096 enumerated); derived rows verified
  labeling-independent (3 witnesses). Residue: the lift declaration + vielbein + P4 profile +
  **new AT-O32** (per-floor extension census, blocking nothing).
- **AT-O31 RESOLVED AS GRAMMAR + AT-O6 CLOSED OUTRIGHT (AT.61).** The Casimir per ray:
  Σᵢ(𝖲^±ᵢ)² = 3P_± exactly (integer). **THE SPLITTING LAW: the electric channel is
  ray-ANTISYMMETRIC (ω̂-conjugate negatives), the magnetic ray-SYMMETRIC — the born Pauli term
  splits the rays oppositely and shifts them commonly: the ledger's j = l±½-type doublet
  grammar**, flagged ¬identified [P5]; witness block-diagonal + conjugation laws exact; the
  lattice splitting census: 12 live feeds, every splitting a Gaussian integer × 2 — no continuous
  locus. The composed fine read = (unmoved position [AT.44(5)/AT.54(3)]) × (phases i^{Θ±}:
  witness (18,24) → (−1,+1), opposite statistics [AT.46(6)]) × (splittings) × (intensities:
  theta-cell Z^amp/Z^norm = **4/9 uniformly — a q-blind attenuation**); values behind
  (M1′)–(M3′). **THE SEAT CENSUS (AT-O6): the contraction image = exactly 6 directions; I₄
  spectrally inert (splitting set {0,±2} c-independent); four seats — boundary M̂, dressing
  (−1)^ℵ, shift-fed W-functional, curvature-born e-channel — each constructed, σ_c⊗I₂ proved
  seatless, every alternative excluded with its ground: NO UNNAMED DIRECTION LEFT.**
- **The open ledger now contains NO structural row**: two by-nature/by-design (AT-O2/O3), one
  convention (AT-O7), one calibration-gated (AT-O13), two closure-phase declarations
  (AT-O26/O27), one proved absence (AT-O29), two censuses (AT-O30/O32). Declarations issued:
  none; marked rows: +1 (the vielbein), −1 (the base frame, dissolved).

**The sharpened open list, in priority order:**
**Session 8 — CONSOLIDATED as Tier AT.12 (AT.63): THE CLOSURE OF LEVEL 5.** The directive:
*"Please consolidate this as closure of Level 5. Split the canon in two clear halves, era 1 and
era 2…"* Two acts, both recorded in the closure tag:
- **THE CLOSURE TAG (AT.63):** the consolidated ledger of all twelve tiers (AT.1–AT.62, one
  spine: split → bit → censor → CP tensor → boundary invariance → hydrogen spine → spin spine →
  locked sector/curl/dressed vertex → Pauli anatomy → resolutions); the final open ledger —
  **no structural row**, only natures/designs, one convention, the closure-phase declarations
  (the lift — which decides the index, AT.60(4); the vielbein; the P4 profile; the read rules
  (M1′)–(M3′); ε_q; (ϰ,β); e₀) and two blocking-nothing censuses (AT-O30, AT-O32); the
  declaration census across the whole level: **ZERO issued, §Cal-AT empty, the P5 firewall held
  at all twelve tiers**; the marked-row final census (+1 added at AT.60, −1 retired by
  dissolution); promotion into the frozen canon's Summary/index/tags.json deliberately NOT taken
  (an Era-2-closure act after Levels 6–7 [AT.63(4)]).
- **THE TWO-HALVES REORGANIZATION (AT.63(5)):** `canon/` → `era1/canon/` and `verification/` →
  `era1/verification/` (moved together — the suite's canon documents are symlinks into
  `../canon/`); `era2/` unchanged in geometry; root keeps README/licences/AI_POLICY, the PDF
  pipeline (`source/` → `docs/`), the frozen `working_markdowns/` archive (¬moved, ¬modified)
  and `archive/zenodo_v1.0_package/`; new `era1/README.md`. **Live path fixes: exactly four
  files** (`source/pipeline/qparse.py`, `qpipeline.py`, `source/Makefile`,
  `checks/check_era2_format.py`); **no frozen file's content changed**. Post-move verification:
  era-2 gate **14 docs PASS / 63 AT-blocks**, era-2 suite **37 checkers / 643 markers / 0
  failures**, era-1 suite **80/80 ALL GREEN**, pipeline registry read re-verified (623 tags from
  `era1/canon/index/tags.json`). Summary generation stays HERE-relative in `era1/canon/`
  (`make_summary.py`); PDF generation stays at the root pipeline.

**No structural row remains open after session 7.** What stands between Level 5 and contact is
declaration/calibration species, in the Architect's order of use:
1. **THE LIFT DECLARATION** (Def-H.37(2)/Open Gaps 19) — now with exact physical content: it
   decides whether the global operator has an index (AT.60(4)'s nullity dichotomy 1 vs 0); with
   it: the vielbein choice (4096 on K₄) and the P4 transport profile `(ℓ_c, 𝐜)`.
2. **(AT-O26)** the level-price read rule of AT.44(8iv) — the gate of (M1′); a closure-phase act
   (BM.30(5) pattern) if ever adopted.
3. **(AT-O27)** `ε_q`'s value — ⅛ distinguished five ways, **adoption** ¬issued [P5];
   calibration-era content. Together with (M2′)/(M3′) it gates every value conversion
   (fine grammar, continuous anomaly).
4. **(AT-O13)** Kerr, once **(AT-O3)** issues `(ϰ,β)`.
5. **(AT-O7)** land the BM.140(6) pin and the re-citation-pinning convention.
6. **(AT-O30)** the B≥5 winding-resolved cover census; **(AT-O32)** the per-floor extension
   census of 𝒟_floor (the other four platonic floors + the polygon ladder; recipe derived
   [AT.60(10)]) — both blocking nothing.
**By nature / by design, not gaps:** (AT-O2) the slicing choice is gauge; (AT-O3) `(ϰ,β)` is
calibration; **(AT-O29)** a native vector EM read — proved absent (EM is a stack aspect with zero
metric coordinates, AT.48(3)); reopening needs a new derived read-species. **(AT-O30)** the B≥5
winding-resolved cover census — open, blocking nothing: the minimal cells are computed (AT.52/
AT.54); the frozen-cell extension (cube/octahedron winding spectra, the V=5..7 full censuses) is
FT.69(3)(v)/FT.106(3)-type census work at the next budgets. **Closed at Tier AT.7:** (AT-O4) the EM sealing grammar — grammar AT.41(5), dynamics
AT.42, spectrum AT.44(5); residual = calibration species. (AT-O5) the lepton mass read — formed
**in species** as the k=1 resolvent price AT.44(4); the `ε_q` value and the family splitting stay
calibration/Gram-currency. AT.43(R3) — met by AT.44. **Closed at Tier AT.8:** (AT-O6) the
anomalous moment — **closed as structure**: the drag/spin-orbit sector derived (AT.46), the frame
section reduced to two enumerated slots (AT.47), the moment coupling constructed natively with the
anomalous read `(2|q| splitting; (−1)^ℵ dressing)` and the vector channel a proved no-go (AT.48);
**Closed in session 4 (AT.50):** (AT-O14/O16) `dim 𝒦_{n≥4}` = **26** by the squeeze, the
flag terminated, the lock a biconditional, the rung-4 projection nonzero-but-unreachable — the
locked sector is provably unreadable at every accessible rung.
**Closed in session 5 (Tier AT.9):** (AT-O6) **CLOSED AS DRESSED STRUCTURE** — the vertex
correction evaluated in the fully dressed ensemble: δ = 0 exactly (the discrete Ward identity,
AT.53), the dressing sign sector-locked (the master parity identity), the full anomalous content
censused measure-side in exact rationals (AT.54); the continuous anomaly is a level-local no-go
with its three missing definitions named (M1′)–(M3′) [AT.54(6)]; AT-O11 verified NON-BLOCKING for
this calculation (zero dictionary calls).
the continuous anomaly number is calibration-species by P5 design.
**Advanced in session 6 (Tier AT.10):** (AT-O28) the slot-free algebraic core of the global
Dirac-type operator is CONSTRUCTED — the Weitzenböck identity with the born Pauli term at tree
coefficient 1 (fully symbolic in the slots), the exact two-channel decomposition of σ^{μν}F_{μν}
(AT.48(3) mechanized and completed, with the Hodge row and the ray-wise so(4) split), and the
transport-curvature census (drag fiber-abelian; EW.32 Gaussian-integer on the fourth-root
lattice); the global evaluation still needs the two marked slots + the P4 profile. New row
(AT-O31): the fine-structure-type read of the hydrogen connector — seats identified, blocked by
(M1′)–(M3′) + AT-O28, blocking nothing.
**Closed in session 7 (Tier AT.11):** (AT-O11) **CLOSED** — the conjugacy table complete at every
level (image = volume alone; genus = the r_n = 1,3,6 pair bits; kernel = exchange coherences; the
nine "none" rows promoted to theorems). (AT-O28) **CLOSED AS CONSTRUCTION** — 𝒟_floor built on K₄;
base-frame slot dissolved as derived gauge; the lift proven physical (the index dichotomy); the
vielbein slot discovered and named; residue = declarations + calibration + AT-O32. (AT-O31)
**RESOLVED AS GRAMMAR** — the composed fine-splitting law derived and quantized; values behind
(M1′)–(M3′). (AT-O6) **CLOSED OUTRIGHT** — the exhaustive seat census: four constructed seats, no
unnamed direction left. New row (AT-O32): the per-floor extension census, blocking nothing. **Closed earlier:** AT-O1, O7 (checker
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
- The folder is **not** wired into `era1/verification/run_all.py`, and `index/`, `tags.json` and
  `Summary.md` have **not** been regenerated. Both are deliberate: regenerating would assert that
  AT.1–AT.55 are canon tags, and they are not yet. Promoting this tier means running the era-chain and
  citation-closure checkers against it, which is a closure-phase act — `check_era2_format.py` (F3)
  is the citation-closure half, already run: **every cited token in all fourteen Part 5 documents is
  attested** against the 640-tag canon registry.
- **Tier AT.7's scope, stated plainly.** The lepton price `w_c` is *generation-blind* (one read for
  the species; the family splitting lives in the Gram currency and is ¬mixed in), it is a
  *dimensionless price* (𝔮⁰ — a conversion to 𝔥-units is exactly what BM.140(5)/BM.83 forbid), and
  its identification with any chart mass is **barred** by BM.134(5) (the two resolvent species meet
  only through the threshold indicator). The `1/d²` *shape* is derived twice; the *read rule*
  (level price = squared dominant pole) and the chart-side scale `−ε²m_r/2` remain marked
  specifications (AT-O26). The `B→∞` universe limit is ¬constructed [Def-H.32(1)] — "universe-level"
  means the budget filtration with no local-seal truncation, never a completed infinite sum.
- **Tier AT.9's scope, stated plainly.** The Ward identity δ=0 is proved on the *censused cells*
  (the minimal winding-2/3 skeletons, both layers, two fugacity specializations) and generalizes by
  its three supports — each a configuration-wise identity (telescoping, charge preservation,
  sector-constancy of a label-read) — not by the census alone; the full G_B-uniform statement at
  every budget rides on those identities, not on the enumerations. The revival ladder's bound
  B_min(m) = 2m+⌈m/2⌉ is a hand proof with machine witnesses to m=5 and machine minimality at
  m=2 only (V≤4 exhaustive, V=5 exhaustive at |R|≤8); larger-m minimality rests on the counting
  argument. The new sector integers are *amplitude-layer structural reads* — barred as mass reads
  [BM.111(6); FT.79(5); BM.30(5)] like their frozen B=4 cousins. The continuous anomaly's absence
  is a *level-local* no-go with named reopening definitions (M1′)–(M3′), following AT.43's
  pattern — not an eternal bar.
- **Tier AT.10's scope, stated plainly.** The Weitzenböck identity is proved for the *skeleton*
  𝒟 = Σγ_a⊗T_a on ℋ_ext⊗ℂ²_T — four transports on a two-dimensional transport factor, the
  undeclared slots left as independent indeterminates. It is an algebraic identity of the frame
  section's own objects, not a statement about a global operator on the emergent geometry: that
  operator (AT-O28) still needs the marked lift, the base frame per floor, and the P4 transport
  profile. The "tree coefficient 1" is the Clifford-normalized coefficient of the born term in
  the square — its identification with any measured gyromagnetic ratio is quarantined behind the
  unissued e₀ [P5; EM.25(7); Def-BM.3(7)], exactly like AT.48(5i)'s splitting-per-charge 2. The
  Hodge row and the EM-duality "rotation" are internal Cl(4,0)-frame statements on the Euclidean
  read [FT.93(1) note] — dictionary partners of chart-side objects, never identifications
  [BM.134(5)]. The transport-curvature census runs on the two *constructed* families (the drag
  exponential and the EW.32 profile family) at formal phases on the fourth-root lattice and the
  Pythagorean pairs — no P4 value is issued anywhere. The F₁/F₂ dictionary assigns *seats*, not
  numbers: the conversion rules (M1′)–(M3′) [AT.54(6)] remain undeclared, so no anomaly value
  exists, is estimated, or is compared.
- **Tier AT.11's scope, stated plainly.** The dictionary theorem (AT.59) is proved for the
  carrier levels n = 2, 3, 4 — the conjugacy test is a commutant membership test on embedded
  aspect generators, and the "never at any n" claim rests on the uniform group-theoretic reason
  (W = the generator itself, G = spin-2, J± = adjoint, D+ = trace-fixed identity), verified
  exhaustively at the three levels and general by the same embedding argument; n=4 is a FORMAL
  table (channel-inadmissible rung [CT0.5/6/11]). The global operator (AT.60) is constructed on
  the TETRAHEDRAL floor — the first arc-transitive floor — with the section machinery that
  generalizes by recipe [AT.34(3)]; the other four platonic floors and the polygon ladder are
  census work (AT-O32), not open math. Its Hermiticity uses the reverse-arc-dagger convention;
  its chirality rows hold for the seed-only lift only — that IS the dichotomy, not a defect. The
  vielbein is a new ENUMERATED datum, not an adopted one: no labeling is chosen or issued. The
  fine grammar (AT.61) is a structural splitting law with quantized values; its identification
  with any measured fine structure is barred [P5; Def-BM.3(7)] and its value conversion needs
  (M1′)–(M3′). The AT-O6 seat census is exhaustive over the 8-dimensional Pauli algebra of
  AT.56(7) — an exhaustiveness relative to the derived algebra, which the tier proves is the
  whole operator content the Pauli term can carry.
- **Level-5 closure scope, stated plainly.** AT.63 is an assembly tag: it consolidates, adjudicates
  the record's status, and records the reorganization — it adds no mathematics. "Level 5 CLOSED"
  means: every structural row the level opened is resolved to a derived answer or a named
  declaration/calibration residue; it does NOT mean the declarations are issued (they are not —
  the lift, the vielbein, the read rules, ε_q, (ϰ,β), e₀ all remain the Architect's/closure-era's
  acts), does NOT mean promotion (the AT-tags are not frozen-canon tags; the era-2 Summary/index
  generation is an Era-2-closure act), and does NOT mean contact (the standing box holds:
  coherence is ¬contact, and no contact claim was made at any tier). Levels 6–7 open against this
  closed record with the inheritance list of AT.63(9).
