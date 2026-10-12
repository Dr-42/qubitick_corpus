# `era2/` — Era 2 · Levels 5–7 (Atomic · Molecular · Anthropic)

**The Era-2 half of the two-halves repository** (the sibling half is `/era1` — the frozen v1.0
canon, Levels 1–4). Three levels follow the v1.0 canon: **Level 5 (Atomic) is CLOSED** — twelve
tiers, tags AT.1–AT.63, closed at AT.63 (Tier AT.12); **Level 6 (Molecular) is OPEN** — Tier
ML.1: the Measurement Theorem (ML.1–ML.5), Tier ML.2: the 1p-kn isotopic family and the
contraction-grammar phase transitions (ML.6–ML.8); Level 7 (Anthropic) is unopened. **Nothing here is frozen canon.** Nothing was adopted, no declaration issued, §Cal
stays empty at every level, and no clause of Parts 1–4 is modified, retracted or renumbered.
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
├── level6_molecular/          ← Level 6 — the Molecular era (OPEN: Tiers ML.1–ML.2, tags ML.1–ML.8)
└── level7_anthropic/          ← Level 7 — the Anthropic era (not opened)
```

**One level, one folder, the same three-way split** (`tiers/` = the record, `checks/` = the
machine, `discovery/` = the working notes). Levels 6–7 inherit this shape when they open.

## Run

```bash
# Level 5 (CLOSED)
cd era2/level5_atomic/checks && python3 run_all_era2.py      # -> 37 checkers, 643 exact markers, 0 failures
cd era2/level5_atomic/checks && python3 check_era2_format.py # -> 14 tier documents PASS, 0 violations
# Level 6 (open)
cd era2/level6_molecular/checks && python3 run_all_level6.py      # -> 3 checkers, 33 exact markers, 0 failures
cd era2/level6_molecular/checks && python3 check_level6_format.py # -> Part 6 documents PASS (attestation vs
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
