# `era2/level6_isotopic/` — Level 6 · the **Isotopic** era · Tiers IT.1–IT.4

**Status: OPENED at session 9 — discovery-phase working level. NOT frozen canon.** Nothing here
is adopted, no declaration issues, §Cal-IT is empty, and no clause of Parts 1–4 or of Level 5's
**closed** record [AT.63(2)] is modified, retracted or renumbered. Level 5 is cited as a closed
record, never edited.

**Rename record (session 12, the Architect's directive):** this level was opened as "the
Molecular era" and is renamed **the Isotopic era**; the retag is the bijection ML.n ↦ IT.n
(n = 1..11), ML-Ok ↦ IT-Ok, §Cal-ML ↦ §Cal-IT — content-preserving, executed as its own commit,
suite re-run green before any new content. The *"molecular necessity"* clause (IT.4) keeps its
name: it is the derived theorem motivating the **deferred molecular level**, whose placement in
the level map is the Architect's act. `AT.63(4)`'s tree row received a live path fix (the
session-8 pattern); the closed record's name mentions stay as closure-time statements. Full
record: IT.15(3).

| path | content |
|---|---|
| `tiers/Part6_Isotopic_era_TierIT1.md` | **Tier IT.1** — IT.1–IT.5: **the Measurement Theorem** (the Architect's directive), in four clauses plus its calibration consequence, with §Cal-IT and §Open-IT |
| `tiers/Part6_Isotopic_era_TierIT2.md` | **Tier IT.2** — IT.6–IT.8: **the 1p-kn isotopic family and the contraction-grammar phase transitions** — the triple-certified grammar engine, the family census (N = 3(k+1); first δ admission at the deuteron; 1p3n δ-dominant at 387/427 on the E_int=24 floor), the capacity adjudication, the lepton-saturation flag, the premise corrections, and §Open-IT's new row IT-O4 |
| `tiers/Part6_Isotopic_era_TierIT3.md` | **Tier IT.3** — IT.9–IT.11: **the multi-seal configuration census at N=5,6** — the channel-width skeleton (W_N(Q)=C(2N,Q+N); 1024/4096 states), the forced-mixed N=5 grammar, the mask-dimension attainment (dim 𝒦_Σ = 18), the D⁻ saturation-boundary adjudication (two mask species; structural censorship), and the IT-O2 census-side closure |
| `tiers/Part6_Isotopic_era_TierIT4.md` | **Tier IT.4** — IT.12–IT.15: **the N=9 isobar doublet and its single-seed weak transition** ("tritium" → "helium-3" + ℓ + ν, quoted) — the doublet as boundary sectors (43758/31824; sector ⊋ species at shares 1000/2431, 375/884), the BM.23 carrier chain inherited coupling-invariantly, the conditionally forced neutral member, **the route-relative Q-value verdict: kinematically CLOSED on every adopted read; 11/8 derived and exact as the route-(ii) measure PRICE — priced ¬adopted**, the conditional endpoint section, the rename record, and the new declaration owed (the mass-read route choice) |
| `checks/measurement_theorem.py` | the theorem's checker — **21/21 exact**, no floating point |
| `checks/isotopic_family.py` | Tier IT.2's checker — **8/8 exact**: the grammar engine (enumeration ∧ recurrence ∧ closed form), the family census, the Vandermonde charge convolution, the capacity census |
| `checks/multi_seal_census.py` | Tier IT.3's checker — **9/9 exact**: the width skeleton (Laurent vs binomial), the N=5,6 grammar census, both mask species, the support placement, the D⁻ status chain |
| `checks/isobar_transition.py` | Tier IT.4's checker — **25/25 exact**: g(9) triple certification, the N=9 width row (19 classes, 262144 states), the 343-triple sector decomposition with exact nucleonic shares, the overflow/balance/two-body-impossibility re-derivations, the ln2 enclosure, the route census with opposite-sign witnesses, the zero-point instance 567u² — every section with an adversarial witness |
| `checks/run_all_level6.py` | the level's runner (gate first, exit 0 iff green) |
| `checks/check_level6_format.py` | the level's format + citation gate: canon `math_balance` rules ported, IT-block anatomy (Thm/Req/Pf/Phys + ∎), and citation attestation against **three** sources — the era-1 canon registry (`era1/canon`, 640 tags), the closed Level-5 record (`../level5_atomic/tiers`, AT.n/AT-O rows), and this level's own IT definitions |
| `discovery/MEASUREMENT_THEOREM.md` | the session-9 working record: the directive's four premises verified against the canon, the four corrections logged, the check ledger |
| `discovery/ISOTOPIC_FAMILY.md` | the session-10 working record: the premise audit (three corrections, one confirmation), the family tables, the adjudication |
| `discovery/MULTI_SEAL_CENSUS.md` | the session-11 working record: the premise audit (three corrections), the width/grammar/mask tables, the synthesis, the adjudication |
| `discovery/ISOBAR_TRANSITION.md` | the session-12 working record: the rename execution, the premise audit (four corrections + one refinement + the confirmations), the check ledger, the adjudication |

**Shared libraries are borrowed, not copied:** `qexact.py` (rigorous `Fraction` intervals) and
`duality.py` (the `Gauss(i)` core) come from `../level5_atomic/checks` via `sys.path` — single
source of truth, recorded in the checker header and in AT.63(9)'s inheritance list.

## Run

```bash
cd era2/level6_isotopic/checks && python3 run_all_level6.py        # -> 5 checkers, 67 exact markers, 0 failures, exit 0
cd era2/level6_isotopic/checks && python3 check_level6_format.py   # -> 4 Part 6 documents PASS, 0 violations
```

## Tier index

**IT.1–IT.5 (Tier IT.1) the Measurement Theorem:** IT.1 the rung hierarchy of observation
(darkness = read-species separation) · IT.2 the non-transit boundary (the measurement horizon) ·
IT.3 the entanglement dichotomy (composite or vacuum, no third option; no collapse) · IT.4 the
molecular necessity (the incommensurability bar becomes operational only in the multi-seal
composite — the clause keeps its name after the level rename: it motivates the deferred
molecular level) · IT.5 the calibration consequence + the tier's status rows, §Cal-IT, §Open-IT.

**IT.6–IT.8 (Tier IT.2) the 1p-kn isotopic family:** IT.6 the triple-certified contraction
grammar + the family census (N = 3(k+1); protection at k=0; first δ admission at the deuteron,
3/5–2/5; 1p3n at N=12: g = 164395, δ share 387/427; the N=4 support adjudicated) · IT.7 the
E_int prices and floors (6(k+1) disjoint / 8k+6 tree; floors hit at k = 0,1,3), the Vandermonde
charge census (Q = +1 always), capacity-never-bites, and the (P1)–(P3) closure from k=1 · IT.8
the lepton-saturation flag (isotopy = same charge, different grammar multiplicities), the premise
corrections, IT-O4 (the nucleon–nucleon connector species), and the status rows.

**IT.9–IT.11 (Tier IT.3) the multi-seal census at N=5,6:** IT.9 the channel-width skeleton
(W_N(Q) = C(2N,Q+N); W₅ sums 1024 over 11 classes, W₆ 4096 over 13; the frozen W₂/W₃
reproduced; cross-N separation) + the grammar census (g(5)=10 all-(1,1) — forced-mixed by the
unique solution of 2a+3b=5; g(6)=25 with the frozen 3/5–2/5 mix; the protection periodicity
g_ε>0 ⟺ 3|N to N=18) · IT.10 the two mask species (rung 26 formal-only vs subnetwork ≤18 —
**attained** by the sealed EM-active members), the vertex placement (2-/3-supports, D_tick(3)=16
saturated, n=4 inadmissible), and the D⁻ status chain (placement ¬activation; masked;
nonzero-but-unreachable; void-closed — **the census terminates in a structural censorship**) ·
IT.11 the synthesis (grammar/width grow, the sink is CONSTANT 1-dim — no saturated areas exist;
the combinatorial capacity limit), the premise corrections (P1)–(P3), **IT-O2 closed on its
census side** (amplitude side = residue), **IT-O4 open, sharpened**.

**IT.12–IT.15 (Tier IT.4) the N=9 isobar doublet and its weak transition:** IT.12 the doublet as
boundary sectors (g(9)=1540=1260+280 triple-certified; W₉(Q)=C(18,Q+9): the "tritium" sector
43758, the "helium-3" sector 31824, ratio 11/8 exact; the 343-triple decomposition — sector ⊋
species, nucleonic shares 1000/2431 and 375/884; E_int = 18 disjoint / 22 tree, equal per
reading) · IT.13 the single-seed transition (registration ¬contraction: N, grouping, E_int
invariant; overflow → emission; unique compensation; the ℓ-channel carrier forced
coupling-invariantly; the neutral member **conditionally forced** — the two-body impossibility
re-derived at the degenerate doublet; forward-only; Γ a resolvent in ε_q) · IT.14 the
route-relative Q-value: **CLOSED on every adopted read** (informational, normalized ensemble,
curvature flux — exact degeneracy ⇒ Q = −(m_ℓ+m_ν) < 0); **11/8 = the route-(ii) measure PRICE,
priced ¬adopted** [BM.30(5); BM.37(6)], sign-indeterminate even under adoption; the conditional
endpoint section (hypothesis face-carried); the lapse correction; the zero-point instance 567u² ·
IT.15 the premise corrections (P1)–(P4) + the sector/species refinement, **the rename record**,
the IT.4-exception flag (¬triggered: the emitted ℓ is unsealed), the open rows (IT-O2 sharpened
to the N=9 amplitude locus; IT-O4 gating; **the route-choice declaration owed**), the status rows.

## The directive's premises, and what the canon said

The Architect's framing entered as a conjecture and was verified row by row (the standing
order). Four corrections are logged on the record at IT.1(8):

- **(P1)** the rung ladder $\mathcal A(n)$ is **CT0.13**'s frozen row, not `AT.30(7)` — AT.30 has
  clauses (1)–(6), and its (1) is the per-aspect × per-rung boundary census.
- **(P2)** *"all measurements are confined to rung 1"* reads, on the derived rows, as its
  opposite: the charge-read floor is **rung 2** [CT0.13; FT.20]. The directive's "rung-1
  restricted system" is formalized as the **EM-inactive** system (mask $\mathcal K_{n\le1}$) —
  which is what the rest of the directive describes.
- **(P3)** *"it doesn't radiate"* is formalized as: no formed radiation leg exists from anything
  [(R9''); BM.122(6)(O1)–(O4)] plus the non-transit mask census. The **dynamical** radiation leg
  stays open as (IT-O1) — named, not assumed.
- **(P4)** *"entangled with the observer"* := the ledger composite (one global Def-H.32
  configuration sum [AT.42(2)]); *"observer"* := a designated register/read apparatus
  [Def-H.9's $o$; FT.20's G-row] — no consciousness, no smooth-manifold analogy.

Tier IT.4 logged its own audit at IT.15(1)–(2), the same discipline: the directive's
combinatorics confirmed to the integer (N=9=3·3; W₉(+1)=43758, W₉(+2)=31824, 11/8 exact; the
BM.23 carrier chain), with four corrections — **(P1)** ⟨m⟩ ∝ W(Q) is the route-(ii) *measure
price*, barred as a physical mass [BM.30(5); BM.37(6)]; on every adopted read the doublet is
exactly degenerate and the β⁻ vertex kinematically **closed** [BM.41(4)(e) pattern]; **(P2)** in
E = N√(m²+p²) − Nⁱpᵢ the N is the **lapse**, not the attachment count [BM.34(4)]; **(P3)**
"E_int = 18" is the disjoint reading (the tree reading is 22; the connector residue is IT-O4);
**(P4)** the ν status is *conditionally forced* [BM.41(3)'s on-record upgrade of BM.23(6)], not
merely admissible — plus the refinement **sector ⊋ species** at species granularity [IT.12(3)].

## Known limitations, stated up front

- **The dichotomy of IT.3 is read-level, not dynamical.** It is the exhaustiveness of AT.32(1)'s
  accessible-content functional over the formed read classes — not a statement about amplitudes
  propagating between junctions. No formed transit-leg amplitude exists in the inventory
  [BM.122(6); BM.6(6)], and IT.3(6) names that as the missing definition rather than papering
  over it.
- **"Isotopic" is a quoted name** for the $N\ge4$ multi-seal EM-bound configuration class
  [BM.31(2)], not a species identification [Def-BM.3(7)]. The grammar floors are exact
  ($N=4$ first $\delta$-mixed; $N=6$ first genuine $\varepsilon/\delta$ mixture at $3/5$–$2/5$),
  but the $N\ge4$ configuration calculus itself is (IT-O2) — the census of *which* molecular
  systems, with which spectra, is not built here.
- **IT.5 is a strategy row, not a calibration.** The slot-vs-read dependency census is exact and
  machine-checked, but no value is issued, estimated or compared: the read rules (M1′)–(M3′)
  [AT.54(6)] still gate every conversion, $e_0$ is not issued [EM.25(7)], and the P5 quarantine
  is untouched. "Calibration must proceed from molecular spectroscopy" is a claim about which
  formed read families can constrain which slots — nothing more.
- **The Earth analogy is an illustration**, flagged as such in IT.1's Phys. The derived content
  is the census, the read classes and the rung ladder.
- **The Q-value verdict of Tier IT.4 is read-relative, per the canon's own discipline.** The
  closure on "every adopted read" covers the informational, normalized-ensemble and
  curvature-flux reads; the route-(ii) price 11/8 is derived and exact but **unadopted** —
  turning it into a mass statement requires the logged declaration of IT.14(3) (the Architect's
  act), and even then the Q-value sign stays scale-indeterminate. The connected (tree) reading's
  degeneracy holds while connector species are charge-blind — IT-O4 could reopen it, flagged at
  IT.12(4). The N=9 amplitude side (the Def-H.32 sum over the 1540 grouping sectors) is IT-O2's
  residue; the physical β endpoint is a quarantined [EXT] target, cited in no clause [P5].
- This folder is **not** wired into `era1/verification/run_all.py` (deliberate: the era-1 suite
  is frozen) nor into `era2/level5_atomic/checks/run_all_era2.py` (Level 5 is closed; its runner
  runs its own record). `index/`, `tags.json` and `Summary.md` are **not** regenerated —
  promotion stays an Era-2-closure act [AT.63(4)].
