# `era2/level6_molecular/` — Level 6 · the **Molecular** era · Tiers ML.1–ML.3

**Status: OPENED at session 9 — discovery-phase working level. NOT frozen canon.** Nothing here
is adopted, no declaration issues, §Cal-ML is empty, and no clause of Parts 1–4 or of Level 5's
**closed** record [AT.63(2)] is modified, retracted or renumbered. Level 5 is cited as a closed
record, never edited.

| path | content |
|---|---|
| `tiers/Part6_Molecular_era_TierML1.md` | **Tier ML.1** — ML.1–ML.5: **the Measurement Theorem** (the Architect's directive), in four clauses plus its calibration consequence, with §Cal-ML and §Open-ML |
| `tiers/Part6_Molecular_era_TierML2.md` | **Tier ML.2** — ML.6–ML.8: **the 1p-kn isotopic family and the contraction-grammar phase transitions** — the triple-certified grammar engine, the family census (N = 3(k+1); first δ admission at the deuteron; 1p3n δ-dominant at 387/427 on the E_int=24 floor), the capacity adjudication, the lepton-saturation flag, the premise corrections, and §Open-ML's new row ML-O4 |
| `tiers/Part6_Molecular_era_TierML3.md` | **Tier ML.3** — ML.9–ML.11: **the multi-seal configuration census at N=5,6** — the channel-width skeleton (W_N(Q)=C(2N,Q+N); 1024/4096 states), the forced-mixed N=5 grammar, the mask-dimension attainment (dim 𝒦_Σ = 18), the D⁻ saturation-boundary adjudication (two mask species; structural censorship), and the ML-O2 census-side closure |
| `checks/measurement_theorem.py` | the theorem's checker — **21/21 exact**, no floating point |
| `checks/isotopic_family.py` | Tier ML.2's checker — **8/8 exact**: the grammar engine (enumeration ∧ recurrence ∧ closed form), the family census, the Vandermonde charge convolution, the capacity census |
| `checks/multi_seal_census.py` | Tier ML.3's checker — **9/9 exact**: the width skeleton (Laurent vs binomial), the N=5,6 grammar census, both mask species, the support placement, the D⁻ status chain |
| `checks/run_all_level6.py` | the level's runner (gate first, exit 0 iff green) |
| `checks/check_level6_format.py` | the level's format + citation gate: canon `math_balance` rules ported, ML-block anatomy (Thm/Req/Pf/Phys + ∎), and citation attestation against **three** sources — the era-1 canon registry (`era1/canon`, 640 tags), the closed Level-5 record (`../level5_atomic/tiers`, AT.n/AT-O rows), and this level's own ML definitions |
| `discovery/MEASUREMENT_THEOREM.md` | the session-9 working record: the directive's four premises verified against the canon, the four corrections logged, the check ledger |
| `discovery/ISOTOPIC_FAMILY.md` | the session-10 working record: the premise audit (three corrections, one confirmation), the family tables, the adjudication |
| `discovery/MULTI_SEAL_CENSUS.md` | the session-11 working record: the premise audit (three corrections), the width/grammar/mask tables, the synthesis, the adjudication |

**Shared libraries are borrowed, not copied:** `qexact.py` (rigorous `Fraction` intervals) and
`duality.py` (the `Gauss(i)` core) come from `../level5_atomic/checks` via `sys.path` — single
source of truth, recorded in the checker header and in AT.63(9)'s inheritance list.

## Run

```bash
cd era2/level6_molecular/checks && python3 run_all_level6.py        # -> 3 checkers, 33 exact markers, 0 failures, exit 0
cd era2/level6_molecular/checks && python3 check_level6_format.py   # -> 1 Part 6 document PASS, 0 violations
```

## Tier index

**ML.1–ML.5 (Tier ML.1) the Measurement Theorem:** ML.1 the rung hierarchy of observation
(darkness = read-species separation) · ML.2 the non-transit boundary (the measurement horizon) ·
ML.3 the entanglement dichotomy (composite or vacuum, no third option; no collapse) · ML.4 the

**ML.6–ML.8 (Tier ML.2) the 1p-kn isotopic family:** ML.6 the triple-certified contraction
grammar + the family census (N = 3(k+1); protection at k=0; first δ admission at the deuteron,
3/5–2/5; 1p3n at N=12: g = 164395, δ share 387/427; the N=4 support adjudicated) · ML.7 the
E_int prices and floors (6(k+1) disjoint / 8k+6 tree; floors hit at k = 0,1,3), the Vandermonde
charge census (Q = +1 always), capacity-never-bites, and the (P1)–(P3) closure from k=1 · ML.8
the lepton-saturation flag (isotopy = same charge, different grammar multiplicities), the premise
corrections, ML-O4 (the nucleon–nucleon connector species), and the status rows.

**ML.9–ML.11 (Tier ML.3) the multi-seal census at N=5,6:** ML.9 the channel-width skeleton
(W_N(Q) = C(2N,Q+N); W₅ sums 1024 over 11 classes, W₆ 4096 over 13; the frozen W₂/W₃
reproduced; cross-N separation) + the grammar census (g(5)=10 all-(1,1) — forced-mixed by the
unique solution of 2a+3b=5; g(6)=25 with the frozen 3/5–2/5 mix; the protection periodicity
g_ε>0 ⟺ 3|N to N=18) · ML.10 the two mask species (rung 26 formal-only vs subnetwork ≤18 —
**attained** by the sealed EM-active members), the vertex placement (2-/3-supports, D_tick(3)=16
saturated, n=4 inadmissible), and the D⁻ status chain (placement ¬activation; masked;
nonzero-but-unreachable; void-closed — **the census terminates in a structural censorship**) ·
ML.11 the synthesis (grammar/width grow, the sink is CONSTANT 1-dim — no saturated areas exist;
the combinatorial capacity limit), the premise corrections (P1)–(P3), **ML-O2 closed on its
census side** (amplitude side = residue), **ML-O4 open, sharpened**.
molecular necessity (the incommensurability bar becomes operational only in the multi-seal
composite) · ML.5 the calibration consequence + the tier's status rows, §Cal-ML, §Open-ML.

## The directive's premises, and what the canon said

The Architect's framing entered as a conjecture and was verified row by row (the standing
order). Four corrections are logged on the record at ML.1(8):

- **(P1)** the rung ladder $\mathcal A(n)$ is **CT0.13**'s frozen row, not `AT.30(7)` — AT.30 has
  clauses (1)–(6), and its (1) is the per-aspect × per-rung boundary census.
- **(P2)** *"all measurements are confined to rung 1"* reads, on the derived rows, as its
  opposite: the charge-read floor is **rung 2** [CT0.13; FT.20]. The directive's "rung-1
  restricted system" is formalized as the **EM-inactive** system (mask $\mathcal K_{n\le1}$) —
  which is what the rest of the directive describes.
- **(P3)** *"it doesn't radiate"* is formalized as: no formed radiation leg exists from anything
  [(R9''); BM.122(6)(O1)–(O4)] plus the non-transit mask census. The **dynamical** radiation leg
  stays open as (ML-O1) — named, not assumed.
- **(P4)** *"entangled with the observer"* := the ledger composite (one global Def-H.32
  configuration sum [AT.42(2)]); *"observer"* := a designated register/read apparatus
  [Def-H.9's $o$; FT.20's G-row] — no consciousness, no smooth-manifold analogy.

## Known limitations, stated up front

- **The dichotomy of ML.3 is read-level, not dynamical.** It is the exhaustiveness of AT.32(1)'s
  accessible-content functional over the formed read classes — not a statement about amplitudes
  propagating between junctions. No formed transit-leg amplitude exists in the inventory
  [BM.122(6); BM.6(6)], and ML.3(6) names that as the missing definition rather than papering
  over it.
- **"Molecular" is a quoted name** for the $N\ge4$ multi-seal EM-bound configuration class
  [BM.31(2)], not a species identification [Def-BM.3(7)]. The grammar floors are exact
  ($N=4$ first $\delta$-mixed; $N=6$ first genuine $\varepsilon/\delta$ mixture at $3/5$–$2/5$),
  but the $N\ge4$ configuration calculus itself is (ML-O2) — the census of *which* molecular
  systems, with which spectra, is not built here.
- **ML.5 is a strategy row, not a calibration.** The slot-vs-read dependency census is exact and
  machine-checked, but no value is issued, estimated or compared: the read rules (M1′)–(M3′)
  [AT.54(6)] still gate every conversion, $e_0$ is not issued [EM.25(7)], and the P5 quarantine
  is untouched. "Calibration must proceed from molecular spectroscopy" is a claim about which
  formed read families can constrain which slots — nothing more.
- **The Earth analogy is an illustration**, flagged as such in ML.1's Phys. The derived content
  is the census, the read classes and the rung ladder.
- This folder is **not** wired into `era1/verification/run_all.py` (deliberate: the era-1 suite
  is frozen) nor into `era2/level5_atomic/checks/run_all_era2.py` (Level 5 is closed; its runner
  runs its own record). `index/`, `tags.json` and `Summary.md` are **not** regenerated —
  promotion stays an Era-2-closure act [AT.63(4)].
