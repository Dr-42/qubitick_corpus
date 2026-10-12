# `era2/` — Era 2 · Levels 5–7 (Atomic · Molecular · Anthropic)

**The Era 2 workspace.** Discovery-phase material for the three levels that follow the frozen
v1.0 canon (Levels 1–4, Parts 1–4 in `/canon`). **Nothing here is frozen canon.** Nothing is
adopted, no declaration issues, §Cal stays empty at every level, and no clause of Parts 1–4 is
modified, retracted or renumbered. Promotion of any level is a closure-phase act (running the
era-chain and citation-closure gates, regenerating `index/`, `tags.json`, `Summary.md`).

## Layout

```
era2/
├── README.md                  ← this file: the era overview
├── level5_atomic/             ← Level 5 — the Atomic era (ACTIVE, sessions 1–5, tags AT.1–AT.55)
│   ├── README.md              ← the level's status ledger, session notes, open rows
│   ├── SESSION_SUMMARY_AND_REVIEW.md
│   ├── tiers/                 ← the tier documents in canon format (Part5_Atomic_era_*.md)
│   ├── checks/                ← ALL machine verification: checkers, runner, gates, shared libs
│   └── discovery/             ← the free-form session records (superseded by the tiers),
│       ├── logs/              ←   historical run outputs
│       └── legacy_checks/     ←   session-1 checker copies (provenance; NOT live)
├── level6_molecular/          ← Level 6 — the Molecular era (not opened)
└── level7_anthropic/          ← Level 7 — the Anthropic era (not opened)
```

**One level, one folder, the same three-way split** (`tiers/` = the record, `checks/` = the
machine, `discovery/` = the working notes). Levels 6–7 inherit this shape when they open.

## Run (Level 5)

```bash
cd era2/level5_atomic/checks && python3 run_all_era2.py     # -> 33 checkers, 587 exact markers, 0 failures, exit 0
cd era2/level5_atomic/checks && python3 check_era2_format.py # -> the tier-document format + citation gate
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
