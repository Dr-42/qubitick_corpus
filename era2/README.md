# `era2/` — Era 2 · Levels 5–8 (Atomic · Isotopic · Molecular · Anthropic) — the declared ladder runs to Level 14

**The Era-2 half of the two-halves repository** (the sibling half is `/era1` — the frozen v1.0
canon, Levels 1–4). Three levels follow the v1.0 canon: **Level 5 (Atomic) is CLOSED** — twelve
tiers, tags AT.1–AT.63, closed at AT.63 (Tier AT.12); **Level 6 (Isotopic) is OPEN** — Tier
IT.1: the Measurement Theorem (IT.1–IT.5), Tier IT.2: the 1p-kn isotopic family and the
contraction-grammar phase transitions (IT.6–IT.8), Tier IT.3: the multi-seal configuration
census at N=5,6 — channel widths, masks, and the D⁻ saturation boundary (IT.9–IT.11), Tier
IT.4: the N=9 isobar doublet and its single-seed weak transition — the route-relative Q-value
verdict and the level's first declaration owed (IT.12–IT.15), Tier IT.5: the hydrogen isotope
sequence — the forward-verified N=9 doublet, the grammar tipping point at N=3,6,9,12, and the
binding-read adjudication that opens the inter-nucleon binding as IT-O5 (IT.16–IT.18), Tier IT.6:
the nucleon–nucleon connector species — IT-O4 CLOSED (the open bidirectional Σ₁₂ connector, d=0)
and the isotope cutoff relocated to IT-O2 alone (IT.19–IT.21), Tier IT.7: the "exotic states"
read-tier adjudication — the N=4,5 support classes and the quarantined [EXT] census mapping
(IT.22–IT.24), Tier IT.8: the multi-seal amplitude calculus — IT-O2 advanced, IT-O5 open with the
obstruction named (IT.25–IT.27), Tier IT.9: the isotope-cutoff resolution — the non-dynamical
binding sign and the "neutron stability" template; IT-O5's static side closed, the cutoff relocated
to IT-O1 (IT.28–IT.30), Tier IT.10: the macroscopic calibration anchor — three ledger-native
definitions and the shared-currency bypass of the incommensurability bar (IT.31–IT.33), Tier IT.11:
the amplitude-binding verdict — the norm/amplitude layer separation (IT-O2's sign resolved, value open;
IT-O1 level-local) (IT.34–IT.36), Tier IT.12: the mass-matrix object — exact Pauli/tensor algebra,
adjudicated redundant + parametric (IT.37–IT.39); Level 7 (Anthropic) is unopened.
**Level 6 was opened as "Molecular" and renamed "Isotopic" at session 12 (the Architect's
directive); the molecular level is deferred — its placement in the level map is the Architect's
act [IT.15(3)].** **Nothing here is frozen canon.** Nothing was adopted into the frozen canon; §Cal-IT at Level 6
is a VALUE-FREE act register (Tiers IT.17 + IT.20: the Architect's logged declaration acts
D-PJ1–6 / D-RS1–3 / D-RS6–7 + the BM.113(6) sector sync — D-RS4 deferred, D-PJ7 owed — no
calibration value issued), §Cal stays empty at every other level, and no clause of Parts 1–4 is
modified, retracted or renumbered.
Promotion into the frozen canon's `index/`, `tags.json`, `Summary.md` is an **Era-2-closure act**
(after Levels 6–7), deliberately not taken at Level-5 closure [AT.63(4)].

## Layout

```
era2/
├── README.md                  ← this file: the era overview
├── level5_atomic/             ← Level 5 — the Atomic era (CLOSED at AT.63, sessions 1–8, tags AT.1–AT.63)
│   ├── README.md              ← the level's status ledger, session notes, open rows
│   ├── SESSION_SUMMARY_AND_REVIEW.md
│   ├── tiers/                 ← the tier documents in canon format (Part5_Atomic_era_*.md)
│   ├── checks/                ← ALL machine verification: checkers, runner, gates, shared libs
│   └── discovery/             ← the free-form session records (superseded by the tiers),
│       ├── logs/              ←   historical run outputs
│       └── legacy_checks/     ←   session-1 checker copies (provenance; NOT live)
├── level6_isotopic/          ← Level 6 — the Isotopic era (OPEN: Tiers IT.1–IT.21, tags IT.1–IT.70; opened as "Molecular", renamed at session 12)
├── level7_molecular/          ← Level 7 — the Molecular era (PLACED at session 13n [IT.61], not opened; prefix MO.n recommended, ¬minted)
└── level8_anthropic/          ← Level 8 — the Anthropic era (not opened; was level7_anthropic/ before the ladder act [IT.61])
```

**One level, one folder, the same three-way split** (`tiers/` = the record, `checks/` = the
machine, `discovery/` = the working notes). Levels 7–8 inherit this shape when they open.

**The declared level ladder (the Architect's act, session 13n; logged at IT.61):** 5 Atomic
(CLOSED) · 6 Isotopic (OPEN) · 7 Molecular (placed, not opened — IT.4's "molecular necessity" is
its motivating theorem) · 8 Anthropic · 9 Stellar · 10 Black holes · 11 Galactic · 12 Galactic
clusters · 13 Laniakea-like systems · **14 Universe (the target**, moved from 13 to 14 by
Isotopic's insertion**)**.

## Run

```bash
# Level 5 (CLOSED)
cd era2/level5_atomic/checks && python3 run_all_era2.py      # -> 37 checkers, 643 exact markers, 0 failures
cd era2/level5_atomic/checks && python3 check_era2_format.py # -> 14 tier documents PASS, 0 violations
# Level 6 (open)
cd era2/level6_isotopic/checks && python3 run_all_level6.py      # -> 14 checkers, 211 exact markers, 0 failures
cd era2/level6_isotopic/checks && python3 check_level6_format.py # -> Part 6 documents PASS (attestation vs
                                                                  #    era-1 canon AND the Level-5 record)
```

The runner is level-scoped by location: each level's `checks/` carries its own runner; an
era-level aggregator, if ever wanted, is a closure-phase tool.

## Discipline (inherited, unchanged)

- **Acyclic DAG:** every new theorem cites backward into Levels 1–4 or earlier tags of its own
  level. No circular logic. The format gate's F3 enforces citation attestation against the
  640-tag canon registry.
- **Exact arithmetic:** no floating point in any assertion. Algebraic number fields, prime-log
  rings, exact rationals, `Gauss(i)`, integer censuses.
- **P5 (no external imports):** no measured value enters any derivation; `[EXT]` figures are
  quarantined scoring targets.
- **No-gos are level-local:** every "barred/absent/¬constructed" is provisional until this
  level's math re-confirms it (the corpus supersedes downstream by design).
- **Block format:** `### AT.n — title`, then `**Thm.**` / `**Req.**` / `**Pf.**` (ends
  `\blacksquare`) / `**Phys.**`.
- **Path note:** tier documents written before the session-5 restructure cite the old loci
  (`canon/era2/*.py`, `era2/*.md`). Those files now live under `era2/level5_atomic/`
  (`checks/`, `tiers/`, `discovery/`); the citations are historical records and are left
  untouched. The mapping table lives in `level5_atomic/README.md`.
- **Two-halves note (Level-5 closure, AT.63(5)):** the frozen v1.0 canon and its verification
  suite moved to `/era1` (`era1/canon/`, `era1/verification/` — sibling-locked by symlinks).
  Historical citations of `canon/...` and `verification/...` in the tier documents resolve to
  `era1/canon/...` and `era1/verification/...`; they are left untouched as written. The
  publication pipeline (`/source` → `/docs`) and the frozen archive (`/working_markdowns/`)
  stayed at the root; exactly four live path constants were updated, no frozen content changed.
