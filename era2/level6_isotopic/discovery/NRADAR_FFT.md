# NRADAR_FFT.md — the session-13r-continuation working record (Tier IT.23, tags IT.79–IT.83)

**Directive (the Architect, session 13r, after pausing the F=ma probe):** *"Wait, the structure of M
is being changed. Give work to builder. I will give a better Directive. Till then develop the system
of n radar synchronisation and applying discrete FFT on it. Like if you do radar sync once you know
position, if twice you have a guess at velocity, if you do n times and the do FFT you can understand
the equation of motion. That thing. The M business I will update you soon."* — plus, mid-turn:
*"Continue as planned. Comms on hold till M update. No board level comms for now."*

**The three acts of the turn:** (1) the builder got his work assignment (comms/0012, pushed 13:4xZ
BEFORE the hold landed — a race, recorded; no further comms or board pings were posted after the
hold); (2) the F=ma probe (previous directive) was PAUSED mid-survey on the M-freeze word — its
canon survey and the Option A/B analysis skeleton live only in this session's working notes,
nothing was committed anywhere; (3) the n-radar/DFT system was developed and built as Tier IT.23.

**State at batch start:** master = `bffa12a` (PR #14 merged — Tier IT.22 on master); era2 =
`f62873b` (ancestor); zero open PRs; the builder had just merged lean PR #2 (the second route:
`PairAlgebra.lean`, 174 theorems + shadow CI) and posted comms/0011 (receipting my 0010-lineage's
answers — [Σ,Wᵢ]=0 triple-attested and CLOSED; the rank rows kernel-checked, Tier 3's first
increment no longer owed; the C13 adversarial adopted kernel-side; and a NEW row offered: the
teacher-board identity L(n) = Σ(k+1)2^k = n·2^{n+1}, kernel-checked in `TickHop.lean`, "yours to
place or decline"). Baseline suites green before new content: runner 23/393, gate 22 docs.

## 0. The comms/0012 work assignment (delivered before the hold)

Contents (all still accurate under the hold — nothing to retract; the hold stops FURTHER comms):
receipts on 0011; the L(n) adjudication (run first: identity exact n=1..24 + telescoping
certificate (k+1)2^k = k·2^{k+1} − (k−1)2^k + board totals + D_tick quotient + lock re-read —
DERIVED rows; the "states ARE the tick load" bridge = READING/parallel ¬adopted; placement
promised in this tier with credit); the M FREEZE (no new builds against M/X on either side until
the Architect's directive lands); and the assignment proper: (1) the exact DFT rows over ℚ[z]/(Φₙ),
n=2,3,4,6, core-only, conventions pinned (ζ=[z], forward +jm) for double entry against this
tier's checker; (2) the n-radar order grammar at the kernel (2n events, the unique total chain,
n=2,3); (3) the queued figure pass confirmed; (4) pin migration f62873b→bffa12a. Board ping:
drafted, **NOT posted** (the hold landed first; the draft stays in the workspace, unpublished).

## 1. The canon survey (what the system is built on)

The n-radar system is a construction on FORMED ground — every joint is either a frozen row or an
issued declaration:

| the piece | the frozen/declared ground |
|---|---|
| the round-trip read (τ_e, τ_r=τ_e+2δh), d=δh∈ℕ | D-RS3 @ IT.65 (the per-edge exchange rate; the per-visit half barred on three grounds) |
| the order labels e≺r on the total tick order | D-RS1 @ IT.56(1); the 1-of-24 theorem [IT.60(1)] |
| the photon↔return-word pairing at FACE level | D-RS2 @ IT.56(2); the agreement as endpoint-blindness consequence [IT.53(5)(a); AT.44(1)] |
| the radar as a geometric READ | D-RS6 @ IT.66 (IT.53(8)'s "iff DECLARED a read" discharged) |
| the formed o-lifted family (the n=1 census) | IT.68(1) — 160 cells |
| the chart faces dτ± = √G dx/(N∓s), agreement ⟺ s·dx=0 | IT.53(4),(5)(b); IT.68(2); BM.34(2)'s null roots |
| the register o | Def-H.9(2); D-PJ6/D-RS5 @ IT.55(7) |
| the stationarity scope | D-RS4 DEFERRED @ IT.56(3)/IT.64(6) — applies per ping |
| the disjointness row (agreement guaranteed where radar cannot run) | IT.53(6) |
| rational count-ratio reads as formed prices | the IT.50 neighbour-law R(n)=(n+1)/n precedent; D-RS7's 𝔮⁰-price clarification; D2.9 |
| the capacity supply bound for conversations through one channel | Cor CT0.6a: δh ≤ 4δτ; CT0.5: D_tick(n)=2^{n+1}; CT0.6: C_cap=16 |
| the bars | transit O1/O2/O4 [IT.40–42; IT.66(1)]; count→strength [BM.36(3); FT.73(5)]; capacity-Fourier [IT.54(1); D0.9; C10]; dictionary ¬bridge [D-RS2; BM.134(5)]; mixed loci exactly three [IT.4(2)] |

**Vocabulary map (the directive's words → corpus loci):** "radar sync" = one round trip of the
IT.68 family; "n radar synchronisation" = the n-fold sequential conversation (unique total order,
IT.79(2)); "position" = the D-RS3 hop face d_j; "a guess at velocity" = the velocity face
Δd/Δτ — exact, ¬a guess, but a WINDOW face (an interval slope, ¬an instantaneous state);
"discrete FFT" = the exact cyclotomic DFT over ℚ[z]/(Φₙ) (integer-coefficient rings only — no
transcendentals, no floating point); "understand the equation of motion" = the annihilator read:
the minimal monic rational recurrence P(σ)d=0 the window obeys, equivalently its spectral support
(IT.81(5),(7)).

## 2. The machine build (`nradar_fft.py`, 19/19) and its two self-caught defects

Fresh self-contained layers: exact integer polynomial recursion for Φ₁..Φ₈ (Π_{d|n}Φ_d = z^n−1,
zero remainders, the product identity independently re-multiplied); the quotient rings ℚ[z]/(Φₙ)
with ζⁿ=1 certified 8/8; exact Fraction linear solves for the minimal annihilators; exhaustive
permutation enumeration for the order theorem (24/720/40320); deterministic witnesses only.

**Defect 1 — the zeta-power bug (the zero-matrix trap class, fourth instance):** `zpow(k)` was
built as `[1] + [0]*k` — the CONSTANT polynomial 1 with trailing zeros, instead of `[0]*k + [1]`
(index = degree). Every ζ-power collapsed to 1: the character sums read n everywhere, the spectra
vanished. The correlating vacuity: C3 (shift/difference) PASSED on the degenerate rings (both
sides collapsed identically) — the catch came from the INDEPENDENT exhaustive censuses (C2's 155
round trips) and the adversarial witnesses (C5's wrong-law row failed to fail). Exactly the
session-6 lesson: absence/degenerate censuses need paired positive witnesses that could only pass
on the right nonzero values. Fixed; all rings re-certified.

**Defect 2 — the wrong "generic window" adversarial:** the first draft claimed the generic window
(3,1,4,1,5,9) has NO annihilator — false: a length-6 window ALWAYS pins a unique monic cubic
(3 interior equations = 3 unknowns). The honest row: identifiability threshold k ≤ ⌊n/2⌋ (rows
n−k ≥ unknowns k); the generic window admits NO law of degree ≤ 2 (overdetermined, inconsistent)
while its degree-3 solve exists — a FIT, ¬a LAW; the minimal degree separates them. This turned a
wrong adversarial into the tier's sharpest honesty row.

Also fixed pre-run: the Φ₆ literal order ([1,−1,1] not [−1,1,1]), a U+2212 syntax landmine in the
expectation dict, the census sizings (A1's product grids, B2's 78,100-cell bound), the
constant-acceleration witness length (6 pings for unique cubic identifiability), and the B1
expected acceleration value (2, ¬4 — recomputed from the symmetric-difference definition).

**Non-vacuity protocol:** the checker was run BEFORE the tier existed — D2/E1/E2/E3 failed loudly
(15/19), then passed (19/19) once the tier landed.

## 3. The findings (tier IT.23, tags IT.79–IT.83)

- **IT.79 — the n-fold family is FORMED:** n sequential round trips at register o, per-ping D-RS3
  halving integral on systematic grids (n=1..8); the **n-fold order theorem** — exactly 1 of (2n)!
  orderings survives the grounded constraints (legs + conversation grammar): the total chain
  e₁≺r₁≺…≺e_n≺r_n, exhaustive at n=2,3,4; n=1 reduces EXACTLY to IT.68(1)'s 160 cells; the
  barred per-visit alternative re-witnessed at every ping (32/32). "n-radar synchronisation" = n
  reads of ONE ledger [IT.53(5)(c) at n] — no cross-clock convention exists or is needed.
- **IT.80 — the kinematic faces:** position d_j ∈ ℕ; velocity v_j = Δd/Δτ ∈ ℚ (a 𝔮⁰ count ratio —
  the IT.50 precedent + D-RS7's price discipline; NO new scale [P1]); acceleration = the symmetric
  second difference over the mean spacing. The face algebra: at spacing T, v ∈ (1/T)ℤ and a ∈
  (1/T²)ℤ exactly (78,100-cell census); the unequal-spacing witness v = (2, ½) — a ratio, ¬a
  count. The window discipline boxed: faces describe the RECORDED interval; extrapolation ¬formed.
  Chart faces per ping (three exact witnesses incl. the frozen (4,3,5,2): 2−6/7=8/7=24/21);
  agreement ⟺ s_j·dx_j=0 per ping; D-RS4 deferral applies per ping; the currency set census: the
  four symbol families meet pairwise in ∅ (the DFT/differences are ℚ-linear PER FACE).
- **IT.81 — the exact cyclotomic DFT:** character sum Σζ^{mk} = n[k≡0] (64 cells); forward/inverse
  exact on ALL 155 windows in {−2..2}ⁿ (n≤3) + 16 deterministic witnesses (n=4..8); shift/
  difference theorems (the velocity spectrum = the position spectrum × (ζ^{−m}−1) — differentiation
  is multiplication, ring-only); Parseval with the Galois involution returning PURE RATIONAL
  scalars (homomorphism witnessed); **the annihilator grammar both directions** — P(σ)d=0 cyclically
  ⟺ P(ζ^{−m})D_m=0 ∀m, via the spectral action identity, with the wrong-law adversarial failing
  BOTH sides; **the boundary defects** — d_j=j² on n=4: the cyclic (σ−1)³d = (0,−16,24,−8)
  supported at the wrap while the interior holds exactly (18-window quadratic census: the defects
  are the wrap, ¬the law); **the window economy** — n pings pin monic laws of degree k ≤ ⌊n/2⌋
  uniquely; the minimal annihilators exact (constant→σ−1; uniform→(σ−1)²; constant-accel→(σ−1)³;
  period-4→σ²+1); the generic window: no law below the fit degree; **the reconstruction** — the
  spectral support Π(z−ζ^{−m}) returns PURELY RATIONAL coefficients (the Galois pairing certified)
  equal to the minimal law: (1,0,−1,0)→z²+1; constants→z−1; period-3→z³−1; alternation→z+1. THE
  DIRECTIVE'S SENTENCE, EXACT — and what it is not: ¬a trajectory, ¬a prediction (continuation =
  a stationarity-class hypothesis; D-RS4 deferred), ¬a force law; the dynamical leg barred on
  O1/O2/O4 (D-PJ7 owed); count→strength barred; the capacity-Fourier bar untouched (the DFT acts
  on the read window, never on a capacity count).
- **IT.82 — the L(n) row PLACED with builder credit:** the identity exact (n=1..24) + telescoping
  certificate (k=1..39) + board totals (4,16,48,128); L(n)/n = 2^{n+1} = D_tick(n) [CT0.5] with
  the integrality census; the lock re-read L(4)/4 = 32 > 16 = C_cap — the capacity lock gains a
  config-census FACE beside the register-accounting one. **The BRIDGE flagged:** "states ARE the
  tick load" = a READING / PARALLEL, ¬adopted (states ≠ edge bits [CT0.9] ≠ slot counts; CT0.5
  defines D_tick by register accounting; no config-census route declared; BM.134(5) discipline).
  Provenance: the builder's teacher-board audit (comms 0011 §3) + TickHop.lean; the board's slips
  stay audit-side record. Context row: Cor CT0.6a's δh≤4δτ is the radar conversation's supply
  bound on the same 2^{n+1} ladder — two count-reads, neither a strength.
- **IT.83 — the verdict table + bars:** every component DERIVED as a formed read / flagged reading
  / BARRED as dynamics — traced to its certifying marker; the bar-check machine (P1, P5 zero-
  decimals self-tested, species exclusion, transit three grounds, incommensurability via the
  per-face linearity + the empty-intersection census, **the M freeze honored — no clause touches
  M or X**); NO declaration issued; NO new open row; §Cal-IT value-free unchanged.

## 4. The pin migration (the IT.22 checker's G4)

The merged `translation_layer.py` pinned its embedded gate re-run to the literal "22 documents
PASS" — adding Tier IT.23 (the 23rd document) reddened that pin (42/43). Fixed per the
session-13k erratum pattern (**the checker is the record — fix, re-run, commit FIRST**): the hard
count replaced by the LIVE census of Part 6 tier documents, the migration recorded in-code and in
the marker label; the frozen IT.78(5) text keeps its closure-time "22 documents" statement, never
edited [AT.63(2)]. Post-fix: 43/43, runner 24/412, gate 23 docs — all green. (Same class as the
builder's 0008 §3 pin migration: the pin move is part of the record, not hidden.)

## 5. The paused F=ma probe (state for the resumed directive)

Paused mid-survey on the M-freeze; nothing committed. Surveyed and reusable when the Architect's
better directive lands: BM.35 verbatim (m_rest := ΔS_𝔏/𝔥 = m_hid with the frozen exponents
[ΔS_𝔏]=𝔮⁰, [𝔥]=𝔮^{−1/2} ⟹ [m]=𝔮^{+1/2}); Def-H.19's stationary jump (= affinely parametrized
geodesic of g_μν via the Euler–Lagrange of ∫g_μνẋẋdλ, tied to CT1.20's stationary-phase read);
the CT1.13–CT1.27 chain (Christoffel/Einstein/linearized spin-2/actions/T_μν/field equations/
conservations/quantum geometry state); the Def-BM.10(3) momentum formula already carrying u⁰; the
BM.34(7) rest-slice agreement (informational = curvature-flux = dispersion on shell); the IT.43
obstructions on M (𝔮-inhomogeneity; the container ¬laundering the sums; the 10:10 ¬adoption).
The verdict skeleton from the survey (to be re-adjudicated against the NEW M): Option A (X·g)
inadmissible on three species (basis/identification — the dictionary is a coefficient bijection,
¬an algebra isomorphism, the S-even real slice is a Jordan algebra under {·,·} not closed under
the associative product; 𝔮-typing inhomogeneity; the cross-currency laundering bar) + the
Hermiticity failure of the product; Option B (F^μ = ma^μ) q-consistent (both sides 𝔮¹ under the
frozen exponents) with the split verdict — the geodesic/free-fall half assemblable from frozen
rows (Def-H.19 + CT1.20 + BM.34 + CT1.24/26 conservation + the BM.9(4) dust read), the forced
half barred (three grounds; D-PJ7), the worldline action −m∫ds ¬in the inventory (a declaration
species if ever wanted), and CT1.22's variational T_μν route as the ALREADY-FORMED F↔g coupling
(the record's answer to "how do force and metric meet": functional differentiation, ¬matrix
product).

## 6. Machine + git state (end of the batch)

`nradar_fft.py` **19/19 exact** (§A 3, §B 4, §C 7, §D 2, §E 3); `translation_layer.py` **43/43**
(post-migration); runner **24 checkers / 412 markers / 0 failures**; gate **23 docs / 83 blocks /
146 defs / 39 rows PASS**. Era-1 untouched (byte-identical; last full re-run 80/80 by the 13r
batch at f62873b — this batch changes only era2/level6). Level-5 untouched (37/643). Commits: (1)
the G4 pin-migration erratum FIRST (13k pattern), (2) the Tier IT.23 batch; pushed `master:era2`;
**PR #15** (era2→master). Vault synced (this record + MEMORY/HANDOFF). Comms: 0012 out (pre-hold);
NO further comms/board activity per the Architect's hold — resumes at the M update.
