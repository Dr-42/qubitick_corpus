# `era2_reified/` — Reified (Single-File) Reunification of Era 2

**Purpose.** Consolidates the discovery-phase tier files into single canonical documents (one per Part), mirroring the structure of `era1/canon/` (Parts 1–4 are single files each).

**Source tiers:**
- Atomic: `era2/level5_atomic/tiers/` (TierA1, TierA2, TierAT1–12 → AT.1–AT.63)
- Isotopic: `era2/level6_isotopic/tiers/` (TierIT1–26 → IT.1–IT.26)
- Extended: `Part5_Atomic_era(3).md` (Tiers 5.0–5.30, canonical + disjoint AT/DJ_AT)

## Layout

```
era2_reified/
├── README.md                  ← this file
├── canon/                     ← reified (single-file) canon
│   ├── Part5_Atomic_era.md    ← merged AT.1–AT.63 + AT.1–AT.20 + DJ_AT.1–DJ_AT.17
│   └── Part6_Isotopic_era.md  ← merged IT.1–IT.26
└── verification/              ← unified verification suite
    ├── README.md              ← verification documentation
    └── checks/
        └── verify_Atomic5_6.py ← master check runner (runs all)
```

## Run

```bash
cd era2_reified/verification/checks && python3 verify_Atomic5_6.py
```

## Cross-reference

| Reified file | Source tiers | Tags |
|---|---|---|
| `canon/Part5_Atomic_era.md` | TierA1, A2, AT1–12 + Part5_Atomic_era(3).md | AT.1–AT.63, DJ_AT.1–DJ_AT.17 |
| `canon/Part6_Isotopic_era.md` | TierIT1–26 | IT.1–IT.26 |

## Relationship to tier files

The reified files are **not** the source of truth — they are a **reification** (presentation consolidation) of the tier files. The tier files (`era2/level5_atomic/tiers/`, `era2/level6_isotopic/tiers/`) remain the canonical discovery record. The reified files serve:
- PDF/publishing pipeline ingestion (single-file input)
- Reference by other tools (quick scan, citation)
- Architect's convenience (single document per level)

## Discipline

- **No floating point in assertions** [P5]
- **Exact arithmetic only** (Fraction, Gauss(i), polynomial rings)
- **Acyclic DAG** — all citations resolve backward
- **No measured value enters** any derivation
