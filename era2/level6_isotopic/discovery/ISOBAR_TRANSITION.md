# Session 12 — the level rename, and the N=9 isobar transition ("tritium" → "helium-3" + ℓ + ν)

Working record for Tier **IT.4** (tags **IT.12–IT.15**). Discovery-phase document: nothing here
is adopted; the tier file is the record. House discipline: the directive entered as a conjecture
and was verified row by row against the frozen canon before any construction; corrections are
logged on the record, in-tier.

---

## 0. The rename (executed first, as its own commit)

**Directive:** *"Rename this level to isotopic. I think molecular needs to wait a before this."*

Executed mechanically, content-preserving:

| old | new |
|---|---|
| `era2/level6_molecular/` | `era2/level6_isotopic/` |
| `Part6_Molecular_era_TierML1..3.md` | `Part6_Isotopic_era_TierIT1..3.md` |
| tags `ML.1–ML.11` | `IT.1–IT.11` (bijection, n ↦ n) |
| open rows `ML-O1..O4` | `IT-O1..O4` |
| `§Cal-ML`, `§Open-ML` | `§Cal-IT`, `§Open-IT` |
| gate/runner token regexes `ML\.\d+`, `ML-O\d+` | `IT\.\d+`, `IT-O\d+` |

- **Clause content preserved verbatim.** In particular the Measurement Theorem's *"molecular
  necessity"* clause (IT.4) keeps its name: it is the derived theorem (the minimal two-currency
  instrument is the multi-seal EM-bound composite) that **motivates** the deferred molecular
  level. Renaming the level does not rename the theorem.
- `AT.63(4)`'s tree row received a **live path fix** (`level6_molecular/` → `level6_isotopic/`,
  the session-8 pattern); the closed record's *name* mentions ("Levels 6–7 (Molecular, Anthropic)")
  stay as closure-time statements — cited, never rewritten.
- **Level map:** Level 7 (Anthropic) placeholder untouched. The deferred molecular level's
  placement (between Isotopic and Anthropic, or after) is the Architect's act — recorded, ¬pre-empted.
- Suite re-run after the rename, before any new content: **4 checkers, 42 exact markers, 0
  failures; gate PASS** — the retag is content-neutral.
- `IT` prefix collision scan: **zero hits** corpus-wide before the rename.

## 1. The directive's structural claims, audited

The directive (abridged in the checker header) constructs the "tritium" β⁻ transition in six
steps: initial state (N=9, Q=+1, E_int=18) → alphabet overflow → forced carrier → final state
(N=9, Q=+2, E_int=18) → kinematic driver (W-ratio 11/8 as a mass ratio; metric dispersion) →
admissible neutral partner.

### Confirmed exactly (the combinatorial skeleton is right to the integer)

| claim | verdict | locus |
|---|---|---|
| N = 9 = 3·3 (three ε-triple nucleons) | **CONFIRMED** | IT.6(2): the family's N = 3(k+1), k=2 |
| Q = +1 initial sector, Q = +2 final | **CONFIRMED** | IT.7(3): Vandermonde census; machine B2 |
| E_int = 18 per member | **CONFIRMED as the disjoint reading** | IT.7(1): 6(k+1) = 18 at k=2; see (P3) |
| ladder E± = ½(σ₁±iσ₂), [σ₃,E±] = ±2E±, Δq = ±1 | **CONFIRMED** | BM.23(1)–(2), verbatim |
| alphabet overflow {−1,0,+1} ± 1 | **CONFIRMED** | BM.23(3); machine D1 |
| unique compensating charge; ℓ-channel forced | **CONFIRMED** | BM.23(4)–(5); machine D2; eliminations are inventory rows (coupling-invariant) |
| W₉(+1) = C(18,10) = 43758; W₉(+2) = C(18,11) = 31824; ratio 11/8 | **CONFIRMED EXACT** | IT.9(1) skeleton; machine B1–B3; gcd = 3978 |
| final state = the Q=+2 member of the N=9 ensemble | **CONFIRMED with refinement** | machine C1–C3: the sector ⊋ the species — see (P5) |

### Corrections (the rows win)

- **(P1) — the mass claim (the decisive one).** *"On the total deficit route the ensemble mass is
  proportional to W(Q) … Tritium is structurally heavier than Helium-3 … not a fitted parameter …
  thermodynamically unstable."* The proportionality is **route (ii)**, the unnormalized total
  deficit — and route (ii) is a **measure price, barred as a physical mass**: "no route is adopted
  here; adoption requires a logged declaration" [BM.30(5)]; "the three mass-route ratios are
  counting and amplitude artifacts — exact as measure prices, **barred as physical masses**"
  [BM.37(6)]; "the sector-route values are measure functionals — exact named prices, ¬masses"
  [BM.97 Rmk]; prices ¬masses [HistLog §V.32]. On **every adopted read** — informational
  (m = E_int·ln2/𝔥 with E_int equal on the doublet in both frozen readings, 18/18 and 22/22
  [IT.7(1); BM.28(1) charge-blindness]), normalized ensemble (structural charge-degeneracy
  [BM.28(4)(i); BM.30(3); FT.107(2)'s σ-free ΔS]), curvature flux (identical (E_int,V)
  [BM.20(1); BM.41(4)(c)]) — the doublet is **exactly degenerate**, so Q_β = −(m_ℓ+m_ν) < 0
  strictly and the vertex is **kinematically closed** [BM.41(4)(e) pattern at N=9]. And even
  *inside* route (ii), the Q-value **sign is undetermined without scale data**:
  Q_ii = (3/8)·T(+2) − (m_ℓ+m_ν), with two exact rational witnesses of opposite sign
  [BM.41(4)(d) pattern; machine E4]. So "thermodynamically unstable" does not follow even under
  adoption. The 11/8 stands — derived, exact — **as the route-(ii) measure price of the doublet**.
  The physical β endpoint (≈18.6 keV) is a measured datum: quarantined [P5], cited nowhere.
- **(P2) — the dispersion formula.** In E_total = N√(m²+p²) − Nⁱpᵢ [BM.34(4); BM.35(7);
  Def-BM.10(5)] the symbol **N is the lapse** and Nⁱ the shift — not the attachment count. No
  frozen row multiplies a dispersion by N = 9. The usable metric rows: vacuum gauge E² = m²+p²,
  KE = N(√(m²+p²)−m) ≥ 0 [BM.34(5)], zero-point E² ≥ (7/4)m²_hid [BM.34(6)] — instantiated at
  E_int = 18: coefficient (7/4)·324 = **567** exact (machine E5).
- **(P3) — "E_int = 18" flat.** 18 is the **disjoint** reading; the tree-connected reading is
  8k+6 = **22** at k=2 (two Σ₁₂ connectors, 2 edges each) [IT.7(1)]; the connector species is
  parametric (**IT-O4**). Both readings give E_T = E_He — *that* is what closes the Q-value —
  but the flat "18" silently selects a reading, and 18 is off the computed-cell floors
  {2,6,12,24,60} (hit at k = 0,1,3) [IT.7(1)]. Mixed readings (18 vs 22) are a currency error —
  exhibited adversarially (machine E2x: ±4u ≠ 0).
- **(P4) — the ν status under-quoted.** *"Unique admissible carrier [BM.23(6)]"* quotes the
  **pre-upgrade** status: BM.41(3) upgraded BM.23(6) **on record** — admissible →
  **conditionally forced** (kinematic + class uniqueness): the two-body vertex at equal
  parent/daughter masses has no real on-shell solution for any positive member mass
  (E_d − m = −m_ℓ²/(2m) < 0; Källén λ = m_ℓ²(m_ℓ²−4m²), both branches covered — re-derived for
  the degenerate doublet, machine D3). The forcing stays kinematic + uniqueness, ¬a number
  conservation (no lepton-number read exists in the inventory). The line index within the
  ν-triplet is ¬derived [FT.145(3)].
- **(P5) — sector ⊋ species (refinement).** "Tritium = the Q=+1 sector" is right at **ensemble
  granularity** (exactly as the proton = the whole Q=+1 sector at N=3 [BM.24(7); BM.28(2): the
  nucleon sectors contain exotic sign triples like (+1,+1,−1)]). At **species granularity** the
  sectors decompose along any pure-ε grouping (280 of them at N=9): the nucleonic (1p,2n)-class
  compositions carry **18000 of 43758** (share **1000/2431** in lowest terms) and the (2p,1n)-class
  **13500 of 31824** (share **375/884**); the complements (25758 / 18324) are exotic-class
  boundary data (machine C1–C3). The nucleonic compositions are a *minority* of their own sectors.

## 2. Derived rows (the tier's content)

- **IT.12** — the doublet as boundary sectors: g(9) = 1540 = 1260 δ-containing + 280 pure-ε
  (triple-certified; 280 = 9!/(3!³·3!)); δ share 9/11 (IT.9(5)'s frozen row re-derived);
  W₉ = C(18,Q+9) entrywise (19 classes, Σ = 262144 = 4⁹, symmetric, peak 48620); the doublet's
  sectors 43758 / 31824, price-ratio 11/8; the exhaustive 343-triple decomposition; the nucleonic
  sub-census (8000, 18000, 13500, 3375) with exact shares; E_int rows (18/22, equal per reading).
- **IT.13** — the transition: single-seed ladder (registration data — the contraction grammar is
  untouched: N, the grouping sector and the crystallized E_int are invariant); overflow →
  emission; unique compensation; forced ℓ-channel carrier q = −1 (the eliminations are
  channel-inventory rows — coupling-invariant, inherited verbatim); the neutral member
  conditionally forced (two-body impossibility re-derived); forward-only arrow; Γ a resolvent in
  ε_q, Γ = 0 at ε_q = 0; the emitted ℓ line is IT.8(1)'s unsealed lepton register coupling
  through the one global Def-H.32 sum [AT.42(2)].
- **IT.14** — the route-relative Q-value verdict: closed on every adopted read; 11/8 priced
  ¬adopted; sign-indeterminacy inside route (ii); the conditional endpoint section (hypothesis
  Q ≥ 0 face-carried, false on every adopted read): E_ℓ^max + E_rec = m_T exact, E_ℓ^max =
  m_ℓ²/(2m_T) at m_ν = 0; the zero-point instance 567u², KE_NR ≥ (27/4)u; the lapse correction.
- **IT.15** — the corrections table, the rename record, the open rows, the declaration census.

## 3. Check ledger

`era2/level6_isotopic/checks/isobar_transition.py` — **25/25 EXACT**, no floating point:

| § | markers | content |
|---|---|---|
| A | 3/3 | g(9) triple certification; 280 = multinomial; δ share 9/11; **adversarial**: corrupted seed caught |
| B | 4/4 | Laurent ≡ binomial entrywise; the sectors + 11/8 (gcd 3978); Vandermonde 3-fold; **adversarial**: corrupted W₃ caught |
| C | 4/4 | 343-triple decomposition ≡ W₉; nucleonic shares 1000/2431, 375/884 (lowest terms); sector ⊋ species; **adversarial**: share ½ refuted |
| D | 5/5 | overflow re-enumerated; balance (+1)=(+2)+(−1)+(0); two-body impossibility (witnesses + Källén, both branches); third member's charge forced to 0; **adversarial**: m_ℓ=0 witness isolates the positivity premise |
| E | 9/9 | ln2 enclosure (Fraction series + exact tail); informational degeneracy 18/18, 22/22 ⇒ Q ≤ −2u < 0; **adversarial** mixed-reading witness ±4u; normalized-route cancellation census; route-(ii) price 11/8 + opposite-sign witnesses (+2, −7); **adversarial** direction flip caught; curvature-flux identity; zero-point 567u², (27/4)u; conditional endpoint algebra |

Runner after the tier: **5 checkers, 67 exact markers, 0 failures**; gate: **4 Part 6 documents
PASS**. The Level-5 closed suite untouched (37/643).

## 4. Adjudication

- **Constructed:** the N=9 isobar doublet as boundary sectors, and its single-seed weak transition
  with the forced charged carrier and the conditionally forced neutral member — the BM.23/BM.41
  chain inherited at N=9 with every inheritance hypothesis verified, not assumed.
- **Corrected:** the mass reading (P1), the dispersion symbols (P2), the E_int reading selection
  (P3), the ν status (P4); refinement (P5).
- **Priced, ¬adopted:** the 11/8 route-(ii) measure price. **A new declaration is owed** to the
  Era-2 ledger: the mass-read route choice [BM.30(5)] — the Architect's act. If route (ii) were
  adopted, the verdict would become *sign-undetermined pending scale data*, never "structurally
  heavier".
- **Open rows, sharpened:** **IT-O2** gains a concrete locus (the Def-H.32 amplitude sum over the
  1540 grouping sectors with (−1)^ℵ dressing; the 280 pure-ε sectors carry the nucleonic
  decomposition); **IT-O4** gates the connected reading (if connector species ever distinguish
  charge composition, the per-reading degeneracy must be re-derived — flagged, ¬assumed).
- **The Architect's IT.4 exception flag is NOT triggered:** the emitted ℓ line is *unsealed*;
  electron-saturated **bound** members remain IT-O2-side. Recorded, ¬pre-empted.
- **Bars:** "tritium"/"helium-3"/"isobar" quoted [Def-BM.3(7)]; no measured datum [P5]; prices
  ¬masses [HistLog §V.32; BM.37(6)]; no currency mixing [BM.83; BM.134(5)]; declarations issued:
  **none**; §Cal-IT stays empty.
