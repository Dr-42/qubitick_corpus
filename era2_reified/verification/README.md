# `era2_reified/verification/` — Reified Canon Verification

**Purpose.** Verify the reified single-file documents (`Part5_Atomic_era.md`, `Part6_Isotopic_era.md`) against the same exact-arithmetic checks used for the discovery-phase tier files.

## Layout

```
verification/
├── README.md                  ← this file
├── checks/
│   ├── verify_Atomic5_6.py    ← unified verification (Part 5 + Part 6)
│   └── run_all.py             ← check runner
└── index/                     ← (future: hash index, tag registry)
```

## Run

```bash
cd era2_reified/verification/checks && python3 verify_Atomic5_6.py
```

Or with explicit paths:

```bash
python3 verify_Atomic5_6.py \
  /path/to/Part5_Atomic_era.md \
  /path/to/Part6_Isotopic_era.md \
  /path/to/era1/canon/
```

## What it checks

### Part 5 (Atomic)
| Section | Content |
|---------|---------|
| §A | Multi-baryon sealing grammar (g(N), G_ε(A)) |
| §B | Charge read, statistics, parity (CPT, W_3 census) |
| §C | Nuclear mass ledger, ensemble laws (D_n, B_ens) |
| §D | Lepton floors, reduced masses (m_r = m_p/(4+3cε)) |
| §E | Binding pole, hydrogen, ionization (E₂/E₁=¼) |
| §F | Shells, orbital ladder, exclusion (antisym rank) |
| §G | Multi-lepton atoms, neutrality, closed shells |
| §H | Document structure (AT tags, Def-AT, Thm/Pf/Req/Phys) |
| §I | Singular-force census, D⁻ cap (3/32 bound) |
| §J | Class ladders, price identity, virial rows |
| §K | Fuzziness products, envelope ratio |
| §L | MT witness, width brackets, thresholds |
| §M | Unified pole, gap, value ledger |
| §N | Extension structure (5.10–5.15) |
| §O | 2-edge transition defect (m_[2]h = 2ln2) |
| §P | Collapse census (A=2,3,4), binding functional |
| §Q | Currency bridge, integration audit |
| §R | Causal capacity (C_cap=16, 4 hops, W_round≤¼) |
| §S | Locked/connected reads, transition defect |
| §T | Seal configurations, flicker gate |
| §U | Incommensurability bar, Koide row |
| §V | Observation structure audit |
| §W | Emission-cycle extension (transition shapes) |

### Part 6 (Isotopic)
| Section | Content |
|---------|---------|
| §X | IT tag structure, section blocks |
| §Y | Header discipline |
| §IT | Isotopic arithmetic (1p-kn, su(4) dim=15, cyclotomic DFT, lock-ratio) |

## Discipline

- **No floating point in any assertion** [P5]
- **Exact arithmetic only** (Fraction, Gauss(i), polynomial rings)
- **Acyclic DAG** — all citations resolve backward
- **No measured value enters** any derivation
