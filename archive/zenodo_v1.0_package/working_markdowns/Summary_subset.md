# Qubitick — Summary Subset: derivation trace of FT.158

*Generated 2026-10-08 by `trace_tags.py`. Dependency closure of the seed tags under the canonical **Req.** record: 363 units — 8 axioms, 9 conventions, 92 definitions, 5 calibration policies, 249 theorem/corollary statements. Statements appear dependencies-first; bracketed citations inside statements are annotations, not edges. HistLog-resident tags, if cited, are pointers only.*

## Derivation trace

```
FT.158
├─ P4
├─ P5
├─ CT0.12
│  ├─ A8
│  ├─ C8
│  ├─ CT0.6
│  │  ├─ A1
│  │  ├─ A2
│  │  ├─ C9
│  │  ├─ C10
│  │  ├─ D0.6
│  │  ├─ D0.7
│  │  ├─ D0.9
│  │  ├─ D1.4
│  │  ├─ D1.5
│  │  ├─ CT0.5
│  │  │  ├─ A7
│  │  │  ├─ C10  (↩ above)
│  │  │  ├─ D0.7  (↩ above)
│  │  │  ├─ D0.8
│  │  │  ├─ D0.9  (↩ above)
│  │  │  ├─ D1.9
│  │  │  └─ CT0.9
│  │  │     ├─ A1  (↩ above)
│  │  │     ├─ A3
│  │  │     ├─ A4
│  │  │     ├─ A7  (↩ above)
│  │  │     ├─ C9  (↩ above)
│  │  │     ├─ C10  (↩ above)
│  │  │     ├─ D0.5
│  │  │     └─ D1.1
│  │  └─ CT0.9  (↩ above)
│  ├─ CT0.7
│  │  ├─ A3  (↩ above)
│  │  ├─ A8  (↩ above)
│  │  ├─ C3
│  │  ├─ C8  (↩ above)
│  │  ├─ D1.2
│  │  ├─ D3.10
│  │  ├─ CT0.6  (↩ above)
│  │  ├─ CT1.1
│  │  │  ├─ A3  (↩ above)
│  │  │  └─ C3  (↩ above)
│  │  └─ CT1.2
│  │     ├─ A3  (↩ above)
│  │     ├─ C1
│  │     ├─ C3  (↩ above)
│  │     └─ CT1.1  (↩ above)
│  ├─ CT1.1  (↩ above)
│  └─ CT1.2  (↩ above)
├─ CT1.2  (↩ above)
├─ CT1.4
│  ├─ C2
│  └─ CT1.2  (↩ above)
├─ CT1.8
│  └─ CT1.2  (↩ above)
├─ FT.14
│  ├─ A1  (↩ above)
│  ├─ A2  (↩ above)
│  ├─ A4  (↩ above)
│  ├─ C8  (↩ above)
│  ├─ C9  (↩ above)
│  ├─ C10  (↩ above)
│  ├─ D3.4
│  ├─ D3.5
│  ├─ CT0.1
│  │  ├─ A1  (↩ above)
│  │  ├─ A3  (↩ above)
│  │  ├─ A4  (↩ above)
│  │  ├─ D0.1
│  │  ├─ D0.2
│  │  └─ D0.4
│  ├─ CT0.6  (↩ above)
│  ├─ CT0.7  (↩ above)
│  ├─ CT0.9  (↩ above)
│  ├─ CT1.12
│  │  ├─ A3  (↩ above)
│  │  ├─ D2.1
│  │  ├─ CT1.1  (↩ above)
│  │  └─ CT1.10
│  │     ├─ CT1.1  (↩ above)
│  │     ├─ CT1.3
│  │     │  ├─ C1  (↩ above)
│  │     │  └─ CT1.2  (↩ above)
│  │     ├─ CT1.5
│  │     │  ├─ CT0.7  (↩ above)
│  │     │  ├─ CT1.2  (↩ above)
│  │     │  └─ CT1.3  (↩ above)
│  │     └─ CT1.8  (↩ above)
│  ├─ CT1.19
│  │  ├─ D0.6  (↩ above)
│  │  ├─ D1.6
│  │  ├─ D1.7
│  │  └─ CT2.6
│  │     ├─ A7  (↩ above)
│  │     ├─ D1.3
│  │     ├─ D1.8
│  │     ├─ D1.9  (↩ above)
│  │     ├─ D2.11
│  │     ├─ CT0.3
│  │     │  ├─ A4  (↩ above)
│  │     │  ├─ A7  (↩ above)
│  │     │  ├─ D0.1  (↩ above)
│  │     │  ├─ D0.6  (↩ above)
│  │     │  ├─ D0.7  (↩ above)
│  │     │  ├─ D1.2  (↩ above)
│  │     │  └─ D1.9  (↩ above)
│  │     └─ CT1.12  (↩ above)
│  ├─ CT1.25
│  │  ├─ A8  (↩ above)
│  │  ├─ D4.3
│  │  ├─ CT1.3  (↩ above)
│  │  ├─ CT1.21
│  │  │  ├─ D1.9  (↩ above)
│  │  │  ├─ D4.3  (↩ above)
│  │  │  ├─ CT2.7
│  │  │  │  ├─ A8  (↩ above)
│  │  │  │  ├─ D1.9  (↩ above)
│  │  │  │  ├─ D4.3  (↩ above)
│  │  │  │  └─ CT2.6  (↩ above)
│  │  │  └─ CT1.20
│  │  │     ├─ A8  (↩ above)
│  │  │     ├─ D1.7  (↩ above)
│  │  │     ├─ D2.8
│  │  │     ├─ D3.5  (↩ above)
│  │  │     ├─ CT1.12  (↩ above)
│  │  │     └─ CT2.6  (↩ above)
│  │  └─ CT1.22
│  │     ├─ A8  (↩ above)
│  │     ├─ D1.1  (↩ above)
│  │     ├─ D1.5  (↩ above)
│  │     ├─ D1.10
│  │     ├─ D4.3  (↩ above)
│  │     ├─ CT2.4
│  │     │  ├─ A8  (↩ above)
│  │     │  ├─ C8  (↩ above)
│  │     │  ├─ D2.3
│  │     │  ├─ CT0.13
│  │     │  │  ├─ A7  (↩ above)
│  │     │  │  ├─ A8  (↩ above)
│  │     │  │  ├─ C8  (↩ above)
│  │     │  │  ├─ D0.8  (↩ above)
│  │     │  │  ├─ D1.12
│  │     │  │  ├─ D2.12
│  │     │  │  ├─ D3.1
│  │     │  │  ├─ D3.2
│  │     │  │  ├─ D3.3
│  │     │  │  ├─ D4.1
│  │     │  │  ├─ D4.3  (↩ above)
│  │     │  │  ├─ CT0.1  (↩ above)
│  │     │  │  ├─ CT0.7  (↩ above)
│  │     │  │  ├─ CT0.11
│  │     │  │  │  ├─ A4  (↩ above)
│  │     │  │  │  ├─ D0.8  (↩ above)
│  │     │  │  │  ├─ D0.9  (↩ above)
│  │     │  │  │  ├─ D3.1  (↩ above)
│  │     │  │  │  ├─ D4.1  (↩ above)
│  │     │  │  │  ├─ CT0.5  (↩ above)
│  │     │  │  │  └─ CT0.6  (↩ above)
│  │     │  │  ├─ CT1.2  (↩ above)
│  │     │  │  ├─ CT1.4  (↩ above)
│  │     │  │  └─ CT1.10  (↩ above)
│  │     │  ├─ CT2.2
│  │     │  │  ├─ D2.3  (↩ above)
│  │     │  │  ├─ CT0.13  (↩ above)
│  │     │  │  └─ CT0.14
│  │     │  │     ├─ A8  (↩ above)
│  │     │  │     ├─ D2.3  (↩ above)
│  │     │  │     ├─ CT0.12  (↩ above)
│  │     │  │     ├─ CT0.13  (↩ above)
│  │     │  │     └─ CT3.8
│  │     │  │        └─ CT3.5
│  │     │  │           ├─ C2  (↩ above)
│  │     │  │           └─ CT3.4
│  │     │  │              ├─ CT3.2
│  │     │  │              │  ├─ A1  (↩ above)
│  │     │  │              │  └─ D3.1  (↩ above)
│  │     │  │              └─ CT3.3
│  │     │  │                 ├─ CT3.1
│  │     │  │                 │  └─ D3.1  (↩ above)
│  │     │  │                 └─ CT3.2  (↩ above)
│  │     │  └─ CT2.3
│  │     │     ├─ A8  (↩ above)
│  │     │     ├─ C7
│  │     │     ├─ D2.3  (↩ above)
│  │     │     └─ CT2.2  (↩ above)
│  │     ├─ CT1.19  (↩ above)
│  │     └─ CT1.21  (↩ above)
│  ├─ EW.13
│  │  ├─ CT0.12  (↩ above)
│  │  ├─ CT1.1  (↩ above)
│  │  ├─ CT1.10  (↩ above)
│  │  ├─ CT1.11
│  │  │  ├─ A8  (↩ above)
│  │  │  ├─ CT0.12  (↩ above)
│  │  │  ├─ CT1.3  (↩ above)
│  │  │  └─ CT1.5  (↩ above)
│  │  ├─ CT1.25  (↩ above)
│  │  ├─ EW.1
│  │  │  └─ CT1.1  (↩ above)
│  │  └─ EW.4
│  │     ├─ CT1.3  (↩ above)
│  │     ├─ CT1.5  (↩ above)
│  │     ├─ CT1.6
│  │     │  └─ CT1.2  (↩ above)
│  │     └─ CT1.7
│  │        ├─ CT1.1  (↩ above)
│  │        └─ CT1.2  (↩ above)
│  ├─ EW.17
│  │  ├─ D1.4  (↩ above)
│  │  ├─ D1.7  (↩ above)
│  │  └─ CT0.11  (↩ above)
│  ├─ EM.9
│  │  ├─ A7  (↩ above)
│  │  ├─ D0.8  (↩ above)
│  │  ├─ D1.4  (↩ above)
│  │  ├─ D3.3  (↩ above)
│  │  ├─ D3.4  (↩ above)
│  │  └─ CT0.9  (↩ above)
│  ├─ EM.16
│  │  ├─ D0.5  (↩ above)
│  │  ├─ D1.6  (↩ above)
│  │  ├─ D2.8  (↩ above)
│  │  ├─ D2.9
│  │  ├─ D3.5  (↩ above)
│  │  └─ CT2.1
│  │     ├─ D0.6  (↩ above)
│  │     └─ D2.9  (↩ above)
│  ├─ FT.9
│  │  ├─ D4.1  (↩ above)
│  │  ├─ CT0.14  (↩ above)
│  │  ├─ EM.17
│  │  │  ├─ D2.3  (↩ above)
│  │  │  ├─ CT0.14  (↩ above)
│  │  │  ├─ CT2.4  (↩ above)
│  │  │  ├─ EW.8
│  │  │  │  ├─ A8  (↩ above)
│  │  │  │  ├─ D2.3  (↩ above)
│  │  │  │  ├─ D2.12  (↩ above)
│  │  │  │  ├─ CT0.12  (↩ above)
│  │  │  │  ├─ CT0.13  (↩ above)
│  │  │  │  ├─ CT0.14  (↩ above)
│  │  │  │  ├─ CT1.2  (↩ above)
│  │  │  │  └─ CT2.2  (↩ above)
│  │  │  └─ EM.2
│  │  │     ├─ D2.3  (↩ above)
│  │  │     ├─ D2.12  (↩ above)
│  │  │     ├─ CT0.12  (↩ above)
│  │  │     ├─ CT0.13  (↩ above)
│  │  │     ├─ CT0.14  (↩ above)
│  │  │     ├─ CT1.2  (↩ above)
│  │  │     ├─ CT2.2  (↩ above)
│  │  │     ├─ EW.8  (↩ above)
│  │  │     └─ EW.32
│  │  │        ├─ A1  (↩ above)
│  │  │        ├─ A2  (↩ above)
│  │  │        ├─ D1.4  (↩ above)
│  │  │        ├─ D2.6
│  │  │        ├─ D2.12  (↩ above)
│  │  │        ├─ P4  (↩ above)
│  │  │        ├─ CT0.12  (↩ above)
│  │  │        ├─ CT0.13  (↩ above)
│  │  │        ├─ CT0.14  (↩ above)
│  │  │        ├─ CT1.2  (↩ above)
│  │  │        └─ EW.8  (↩ above)
│  │  ├─ EM.18
│  │  │  ├─ CT0.13  (↩ above)
│  │  │  ├─ CT0.14  (↩ above)
│  │  │  ├─ CT2.4  (↩ above)
│  │  │  ├─ EM.17  (↩ above)
│  │  │  └─ CT3.7
│  │  │     ├─ D2.12  (↩ above)
│  │  │     ├─ D3.2  (↩ above)
│  │  │     ├─ CT0.13  (↩ above)
│  │  │     ├─ EW.8  (↩ above)
│  │  │     ├─ EM.2  (↩ above)
│  │  │     ├─ CT3.4  (↩ above)
│  │  │     └─ CT3.5  (↩ above)
│  │  ├─ EM.19
│  │  │  ├─ D4.1  (↩ above)
│  │  │  ├─ CT0.6  (↩ above)
│  │  │  ├─ CT0.11  (↩ above)
│  │  │  ├─ CT0.13  (↩ above)
│  │  │  ├─ CT0.14  (↩ above)
│  │  │  ├─ EM.17  (↩ above)
│  │  │  └─ EM.18  (↩ above)
│  │  ├─ EM.20
│  │  │  ├─ A1  (↩ above)
│  │  │  ├─ A4  (↩ above)
│  │  │  ├─ A5
│  │  │  ├─ A6
│  │  │  ├─ A7  (↩ above)
│  │  │  ├─ D0.4  (↩ above)
│  │  │  ├─ D1.1  (↩ above)
│  │  │  ├─ D1.2  (↩ above)
│  │  │  ├─ D1.6  (↩ above)
│  │  │  ├─ D3.5  (↩ above)
│  │  │  ├─ CT0.9  (↩ above)
│  │  │  └─ Def-EM.20
│  │  ├─ CT3.7  (↩ above)
│  │  └─ CT3.10
│  │     ├─ D2.14
│  │     ├─ D3.5  (↩ above)
│  │     ├─ CT0.14  (↩ above)
│  │     ├─ EM.2  (↩ above)
│  │     ├─ EM.17  (↩ above)
│  │     ├─ EM.18  (↩ above)
│  │     ├─ CT3.4  (↩ above)
│  │     ├─ CT3.7  (↩ above)
│  │     ├─ CT3.8  (↩ above)
│  │     └─ CT3.9
│  │        ├─ C2  (↩ above)
│  │        ├─ CT3.5  (↩ above)
│  │        └─ CT3.8  (↩ above)
│  ├─ FT.11
│  │  ├─ A8  (↩ above)
│  │  ├─ C8  (↩ above)
│  │  ├─ D2.5
│  │  ├─ D4.3  (↩ above)
│  │  ├─ CT0.7  (↩ above)
│  │  ├─ CT0.12  (↩ above)
│  │  ├─ EW.13  (↩ above)
│  │  ├─ EW.33
│  │  │  ├─ D1.1  (↩ above)
│  │  │  ├─ CT1.12  (↩ above)
│  │  │  ├─ CT2.5
│  │  │  │  ├─ D2.4
│  │  │  │  ├─ D2.5  (↩ above)
│  │  │  │  ├─ D2.8  (↩ above)
│  │  │  │  ├─ CT0.14  (↩ above)
│  │  │  │  └─ CT2.3  (↩ above)
│  │  │  ├─ CT2.8
│  │  │  │  ├─ A8  (↩ above)
│  │  │  │  ├─ D0.7  (↩ above)
│  │  │  │  ├─ D0.10
│  │  │  │  ├─ D1.2  (↩ above)
│  │  │  │  ├─ D1.3  (↩ above)
│  │  │  │  ├─ D1.9  (↩ above)
│  │  │  │  ├─ D2.6  (↩ above)
│  │  │  │  ├─ D2.7
│  │  │  │  ├─ D2.8  (↩ above)
│  │  │  │  ├─ D3.3  (↩ above)
│  │  │  │  ├─ D3.5  (↩ above)
│  │  │  │  ├─ D3.6
│  │  │  │  └─ CT2.2  (↩ above)
│  │  │  ├─ EW.17  (↩ above)
│  │  │  └─ EW.32  (↩ above)
│  │  ├─ EW.20
│  │  │  ├─ P4  (↩ above)
│  │  │  ├─ EW.3
│  │  │  │  └─ CT1.4  (↩ above)
│  │  │  ├─ EW.32  (↩ above)
│  │  │  └─ EW.33  (↩ above)
│  │  ├─ EM.9  (↩ above)
│  │  ├─ CT3.7  (↩ above)
│  │  ├─ CT3.10  (↩ above)
│  │  ├─ CT3.22
│  │  │  ├─ D3.4  (↩ above)
│  │  │  ├─ CT0.9  (↩ above)
│  │  │  ├─ CT2.3  (↩ above)
│  │  │  ├─ CT2.5  (↩ above)
│  │  │  ├─ CT2.8  (↩ above)
│  │  │  └─ CT3.18
│  │  │     ├─ D2.3  (↩ above)
│  │  │     ├─ D2.11  (↩ above)
│  │  │     ├─ D3.1  (↩ above)
│  │  │     ├─ D3.9
│  │  │     ├─ CT2.5  (↩ above)
│  │  │     └─ CT3.17
│  │  │        ├─ A1  (↩ above)
│  │  │        ├─ D2.14  (↩ above)
│  │  │        ├─ D3.8
│  │  │        ├─ CT3.2  (↩ above)
│  │  │        └─ CT3.15
│  │  │           ├─ D3.9  (↩ above)
│  │  │           └─ CT3.2  (↩ above)
│  │  ├─ CT4.4
│  │  │  ├─ D3.2  (↩ above)
│  │  │  ├─ CT0.11  (↩ above)
│  │  │  ├─ CT0.12  (↩ above)
│  │  │  ├─ CT0.13  (↩ above)
│  │  │  ├─ CT3.20
│  │  │  │  ├─ A2  (↩ above)
│  │  │  │  ├─ D3.1  (↩ above)
│  │  │  │  ├─ CT0.5  (↩ above)
│  │  │  │  ├─ CT0.6  (↩ above)
│  │  │  │  ├─ CT0.9  (↩ above)
│  │  │  │  └─ CT0.11  (↩ above)
│  │  │  └─ CT4.2
│  │  │     ├─ D4.1  (↩ above)
│  │  │     ├─ CT0.13  (↩ above)
│  │  │     ├─ CT0.14  (↩ above)
│  │  │     └─ CT2.5  (↩ above)
│  │  └─ FT.12
│  │     ├─ D3.4  (↩ above)
│  │     ├─ EW.3  (↩ above)
│  │     ├─ EW.22
│  │     │  ├─ EW.32  (↩ above)
│  │     │  ├─ EW.33  (↩ above)
```

## Closure in dependency order (tag ⇐ its Req citations)

| # | tag | kind | cites |
| --- | --- | --- | --- |
| 1 | A1 | axiom | — |
| 2 | A2 | axiom | — |
| 3 | A3 | axiom | — |
| 4 | A4 | axiom | — |
| 5 | A5 | axiom | — |
| 6 | A6 | axiom | — |
| 7 | A7 | axiom | — |
| 8 | A8 | axiom | — |
| 9 | C1 | convention | — |
| 10 | C2 | convention | — |
| 11 | C3 | convention | — |
| 12 | C5 | convention | — |
| 13 | C7 | convention | — |
| 14 | C8 | convention | — |
| 15 | C9 | convention | — |
| 16 | C10 | convention | — |
| 17 | C11 | convention | — |
| 18 | D0.1 | definition | — |
| 19 | D0.2 | definition | — |
| 20 | D0.3 | definition | — |
| 21 | D0.4 | definition | — |
| 22 | D0.5 | definition | — |
| 23 | D0.6 | definition | — |
| 24 | D0.7 | definition | — |
| 25 | D0.8 | definition | — |
| 26 | D0.9 | definition | — |
| 27 | D0.10 | definition | — |
| 28 | D1.1 | definition | — |
| 29 | D1.2 | definition | — |
| 30 | D1.3 | definition | — |
| 31 | D1.4 | definition | — |
| 32 | D1.5 | definition | — |
| 33 | D1.6 | definition | — |
| 34 | D1.7 | definition | — |
| 35 | D1.8 | definition | — |
| 36 | D1.9 | definition | — |
| 37 | D1.10 | definition | — |
| 38 | D1.11 | definition | — |
| 39 | D1.12 | definition | — |
| 40 | D2.1 | definition | — |
| 41 | D2.2 | definition | — |
| 42 | D2.3 | definition | — |
| 43 | D2.4 | definition | — |
| 44 | D2.5 | definition | — |
| 45 | D2.6 | definition | — |
| 46 | D2.7 | definition | — |
| 47 | D2.8 | definition | — |
| 48 | D2.9 | definition | — |
| 49 | D2.11 | definition | — |
| 50 | D2.12 | definition | — |
| 51 | D2.13 | definition | — |
| 52 | D2.14 | definition | — |
| 53 | D3.1 | definition | — |
| 54 | D3.2 | definition | — |
| 55 | D3.3 | definition | — |
| 56 | D3.4 | definition | — |
| 57 | D3.5 | definition | — |
| 58 | D3.6 | definition | — |
| 59 | D3.7 | definition | — |
| 60 | D3.8 | definition | — |
| 61 | D3.9 | definition | — |
| 62 | D3.10 | definition | — |
| 63 | D4.1 | definition | — |
| 64 | D4.2 | definition | — |
| 65 | D4.3 | definition | — |
| 66 | P1 | calibration | — |
| 67 | P2 | calibration | — |
| 68 | P3 | calibration | — |
| 69 | P4 | calibration | — |
| 70 | P5 | calibration | — |
| 71 | CT0.1 | theorem | A1, A3, A4, D0.1, D0.2, D0.4 |
| 72 | CT0.2 | theorem | A1, A4, A5, D0.1, D0.3, CT0.1 |
| 73 | CT0.3 | theorem | A4, A7, D0.1, D0.6, D0.7, D1.2, D1.9 |
| 74 | CT0.9 | theorem | A1, A3, A4, A7, C9, C10, D0.5, D1.1 |
| 75 | CT0.5 | theorem | A7, C10, D0.7, D0.8, D0.9, D1.9, CT0.9 |
| 76 | CT0.6 | theorem | A1, A2, C9, C10, D0.6, D0.7, D0.9, D1.4, D1.5, CT0.5, CT0.9 |
| 77 | CT0.6a | theorem | A2, C9, C10, D0.6, D0.7, D1.4, D1.5, CT0.6, CT0.9 |
| 78 | CT1.1 | theorem | A3, C3 |
| 79 | CT1.2 | theorem | A3, C1, C3, CT1.1 |
| 80 | CT0.7 | theorem | A3, A8, C3, C8, D1.2, D3.10, CT0.6, CT1.1, CT1.2 |
| 81 | CT0.7a | theorem | CT0.7, CT1.2 |
| 82 | CT0.8 | theorem | A1, A4, A5, D0.1, D0.2, D0.4, CT0.2, CT0.7 |
| 83 | CT0.10 | theorem | A8, D0.5, D3.3 |
| 84 | CT0.11 | theorem | A4, D0.8, D0.9, D3.1, D4.1, CT0.5, CT0.6 |
| 85 | CT0.11b | theorem | A4, D0.8, D4.1, CT0.5, CT0.6, CT0.11 |
| 86 | CT0.12 | theorem | A8, C8, CT0.6, CT0.7, CT1.1, CT1.2 |
| 87 | CT1.4 | theorem | C2, CT1.2 |
| 88 | CT1.3 | theorem | C1, CT1.2 |
| 89 | CT1.5 | theorem | CT0.7, CT1.2, CT1.3 |
| 90 | CT1.8 | theorem | CT1.2 |
| 91 | CT1.10 | theorem | CT1.1, CT1.3, CT1.5, CT1.8 |
| 92 | CT0.13 | theorem | A7, A8, C8, D0.8, D1.12, D2.12, D3.1, D3.2, D3.3, D4.1, D4.3, CT0.1, CT0.7, CT0.11, CT1.2, CT1.4, CT1.10 |
| 93 | CT3.2 | theorem | A1, D3.1 |
| 94 | CT3.1 | theorem | D3.1 |
| 95 | CT3.3 | theorem | CT3.1, CT3.2 |
| 96 | CT3.4 | theorem | CT3.2, CT3.3 |
| 97 | CT3.5 | theorem | C2, CT3.4 |
| 98 | CT3.8 | theorem | CT3.5 |
| 99 | CT0.14 | theorem | A8, D2.3, CT0.12, CT0.13, CT3.8 |
| 100 | CT1.6 | theorem | CT1.2 |
| 101 | CT1.7 | theorem | CT1.1, CT1.2 |
| 102 | CT1.9 | theorem | C2, CT1.1, CT1.8 |
| 103 | CT1.11 | theorem | A8, CT0.12, CT1.3, CT1.5 |
| 104 | CT2.2 | theorem | D2.3, CT0.13, CT0.14 |
| 105 | CT2.8 | theorem | A8, D0.7, D0.10, D1.2, D1.3, D1.9, D2.6, D2.7, D2.8, D3.3, D3.5, D3.6, CT2.2 |
| 106 | EM.9 | theorem | A7, D0.8, D1.4, D3.3, D3.4, CT0.9 |
| 107 | CT1.11a | theorem | A3, A5, A7, A8, C3, D0.5, D2.6, D2.7, D3.5, D3.6, CT0.7, CT0.7a, CT0.9, CT0.10, CT0.12, CT1.1, CT1.2, CT1.6, CT1.9, CT1.11, CT2.8, EM.9 |
| 108 | L1 | theorem | A1, A4, A5, A6, D0.3, D0.4, CT0.8 |
| 109 | L2 | theorem | A1, A4, A5, D0.3, D0.4, CT0.8, L1 |
| 110 | L0 | theorem | A1, A4, A5, A6, A7, D0.2, D0.3, D0.4, D1.2, CT0.8, L1, L2 |
| 111 | L0a | theorem | A1, A5, D0.3, CT0.8, L0 |
| 112 | L3 | theorem | A1, A5, C1, D0.3, CT1.1, L1, L2 |
| 113 | L4 | theorem | A1, A4, A5, C1, D0.1, D0.3, D0.8, L3 |
| 114 | L5 | theorem | A1, A5, C1, C3, D0.3, D0.4, CT0.8, CT1.1, CT1.2, CT1.10, L0, L0a, L1, L2, L3 |
| 115 | CT1.12 | theorem | A3, D2.1, CT1.1, CT1.10 |
| 116 | CT1.13 | theorem | D2.1, D2.2 |
| 117 | CT1.14 | theorem | CT1.13 |
| 118 | CT2.1 | theorem | D0.6, D2.9 |
| 119 | CT2.3 | theorem | A8, C7, D2.3, CT2.2 |
| 120 | CT2.4 | theorem | A8, C8, D2.3, CT0.13, CT2.2, CT2.3 |
| 121 | CT2.5 | theorem | D2.4, D2.5, D2.8, CT0.14, CT2.3 |
| 122 | CT2.6 | theorem | A7, D1.3, D1.8, D1.9, D2.11, CT0.3, CT1.12 |
| 123 | CT2.7 | theorem | A8, D1.9, D4.3, CT2.6 |
| 124 | CT1.19 | theorem | D0.6, D1.6, D1.7, CT2.6 |
| 125 | CT1.19a | theorem | D0.6, D1.6, D1.7, CT2.6, CT1.19 |
| 126 | CT1.20 | theorem | A8, D1.7, D2.8, D3.5, CT1.12, CT2.6 |
| 127 | CT1.21 | theorem | D1.9, D4.3, CT2.7, CT1.20 |
| 128 | CT1.22 | theorem | A8, D1.1, D1.5, D1.10, D4.3, CT2.4, CT1.19, CT1.21 |
| 129 | CT1.23 | theorem | CT2.1, CT1.21, CT1.22 |
| 130 | CT1.25 | theorem | A8, D4.3, CT1.3, CT1.21, CT1.22 |
| 131 | CT1.29 | theorem | A2, C9, CT0.9, CT1.19 |
| 132 | CT2.9 | theorem | CT2.1, CT1.23, CT1.29 |
| 133 | CT2.11 | theorem | D2.9, P1, P2, P4, CT0.5, CT0.6, CT0.11, CT1.1, CT2.1, CT1.29, CT2.9 |
| 134 | EW.1 | theorem | CT1.1 |
| 135 | EW.2 | theorem | CT1.2 |
| 136 | EW.3 | theorem | CT1.4 |
| 137 | EW.4 | theorem | CT1.3, CT1.5, CT1.6, CT1.7 |
| 138 | EW.5 | theorem | CT1.1, CT1.2, CT1.5, CT1.6, CT1.7, EW.4 |
| 139 | EW.6 | theorem | C8, D2.1, D3.3, CT0.13, CT2.2, CT2.3 |
| 140 | EW.8 | theorem | A8, D2.3, D2.12, CT0.12, CT0.13, CT0.14, CT1.2, CT2.2 |
| 141 | EW.12 | theorem | C5, D2.1, CT1.2, CT1.12, EW.2 |
| 142 | EW.13 | theorem | CT0.12, CT1.1, CT1.10, CT1.11, CT1.25, EW.1, EW.4 |
| 143 | EW.17 | theorem | D1.4, D1.7, CT0.11 |
| 144 | EW.18 | theorem | D2.4, CT2.5, EW.17 |
| 145 | EW.19 | theorem | D2.4, D2.5, CT2.5 |
| 146 | EW.32 | theorem | A1, A2, D1.4, D2.6, D2.12, P4, CT0.12, CT0.13, CT0.14, CT1.2, EW.8 |
| 147 | EW.33 | theorem | D1.1, CT1.12, CT2.5, CT2.8, EW.17, EW.32 |
| 148 | EW.20 | theorem | P4, EW.3, EW.32, EW.33 |
| 149 | EW.22 | theorem | EW.32, EW.33, EW.20 |
| 150 | EW.23 | theorem | EW.20, EW.22 |
| 151 | EW.24 | theorem | D3.10, EW.23 |
| 152 | EW.25 | theorem | EW.19, EW.24 |
| 153 | EW.26 | theorem | CT0.12, CT0.14, EW.6, EW.19, EW.32, EW.33 |
| 154 | EW.27 | theorem | P4, CT2.5, CT1.20 |
| 155 | EW.35 | theorem | EW.22, EW.24 |
| 156 | EW.36 | theorem | D2.6, D3.4, CT0.9, EW.32, EW.20, EW.22, EM.9 |
| 157 | EW.36a | theorem | D2.6, D3.4, CT0.9, EW.32, EW.20, EW.22, EW.36, EM.9 |
| 158 | EM.2 | theorem | D2.3, D2.12, CT0.12, CT0.13, CT0.14, CT1.2, CT2.2, EW.8, EW.32 |
| 159 | EM.5 | theorem | D0.8, D1.7, D3.7, CT0.13 |
| 160 | EM.6 | theorem | D2.5, EW.18, EW.33, EW.22, EW.24, EW.25, EM.5 |
| 161 | EM.7 | theorem | C9, D1.5, CT0.9, EM.5 |
| 162 | EM.12 | theorem | D3.3, CT0.9, CT1.19, CT1.22 |
| 163 | EM.14 | theorem | CT2.6, CT1.22, EM.12 |
| 164 | EM.8 | theorem | CT2.6, CT1.22, EM.6, EM.14 |
| 165 | EM.9b | theorem | A7, D0.8, D1.4, D3.3, D3.4, CT0.9, EM.9 |
| 166 | EM.9a | theorem | A1, D1.4, D2.6, D3.4, CT0.9, EM.9 |
| 167 | EM.16 | theorem | D0.5, D1.6, D2.8, D2.9, D3.5, CT2.1 |
| 168 | EM.17 | theorem | D2.3, CT0.14, CT2.4, EW.8, EM.2 |
| 169 | CT3.7 | theorem | D2.12, D3.2, CT0.13, EW.8, EM.2, CT3.4, CT3.5 |
| 170 | EM.18 | theorem | CT0.13, CT0.14, CT2.4, EM.17, CT3.7 |
| 171 | EM.19 | theorem | D4.1, CT0.6, CT0.11, CT0.13, CT0.14, EM.17, EM.18 |
| 172 | Def-EM.20 | definition | — |
| 173 | EM.20 | theorem | A1, A4, A5, A6, A7, D0.4, D1.1, D1.2, D1.6, D3.5, CT0.9, Def-EM.20 |
| 174 | Def-EM.21 | definition | — |
| 175 | Def-EM.22 | definition | — |
| 176 | EM.23 | theorem | A4, D2.11, D2.13, CT0.9, Def-EM.20, EM.20, Def-EM.21, Def-EM.22 |
| 177 | EM.24 | theorem | A8, D0.5, D0.10, D1.6, D2.6, D2.7, D3.3, D3.4, D3.5, D3.6, CT0.9, CT2.8, EM.9, EM.9a, Def-EM.20, EM.20, Def-EM.21, EM.23 |
| 178 | CT3.20 | theorem | A2, D3.1, CT0.5, CT0.6, CT0.9, CT0.11 |
| 179 | CT3.9 | theorem | C2, CT3.5, CT3.8 |
| 180 | CT3.21 | theorem | CT3.9 |
| 181 | CT3.10 | theorem | D2.14, D3.5, CT0.14, EM.2, EM.17, EM.18, CT3.4, CT3.7, CT3.8, CT3.9 |
| 182 | CT3.10a | theorem | D2.14, D3.5, CT0.14, EM.17, EM.18, CT3.4, CT3.7, CT3.8, CT3.9, CT3.10 |
| 183 | CT3.14 | theorem | D2.5, D3.7, CT0.14, EW.18, EW.32, EW.33, EW.26 |
| 184 | CT3.12 | theorem | D0.8, D1.5, D1.7, D3.1, D3.7, CT0.13, EM.5, EM.6, CT3.14 |
| 185 | CT3.15 | theorem | D3.9, CT3.2 |
| 186 | CT3.17 | theorem | A1, D2.14, D3.8, CT3.2, CT3.15 |
| 187 | CT3.11 | theorem | D1.5, D3.1, D3.7, D3.8, D3.9, CT3.2, CT3.4, CT3.12, CT3.15, CT3.17 |
| 188 | CT3.13 | theorem | CT3.7, CT3.8 |
| 189 | CT3.16 | theorem | CT3.7, CT3.15 |
| 190 | CT3.17a | theorem | A1, D2.14, D3.8, CT3.17 |
| 191 | CT3.18 | theorem | D2.3, D2.11, D3.1, D3.9, CT2.5, CT3.17 |
| 192 | CT3.22 | theorem | D3.4, CT0.9, CT2.3, CT2.5, CT2.8, CT3.18 |
| 193 | CT4.2 | theorem | D4.1, CT0.13, CT0.14, CT2.5 |
| 194 | CT4.3 | theorem | A5, A8, D0.7, D1.11, D4.2, CT0.3, CT2.8, CT4.1, CT4.2 |
| 195 | CT4.1 | theorem | A2, A4, D0.8, D1.11, D4.1, D4.2, CT0.5, CT0.6, CT0.11, CT0.11b, CT4.2, CT4.3 |
| 196 | CT4.1a | theorem | A4, D0.8, D1.11, D4.1, D4.2, CT0.6, CT0.11, CT0.11b, CT4.1, CT4.2, CT4.3 |
| 197 | CT4.4 | theorem | D3.2, CT0.11, CT0.12, CT0.13, CT3.20, CT4.2 |
| 198 | CT4.5 | theorem | D1.5, CT1.22, CT1.23, CT4.1, CT4.2, CT4.3 |
| 199 | CT4.9 | theorem | A2, D0.8, D1.9, D4.2, CT0.9, CT0.11, CT1.29, CT4.1 |
| 200 | CT4.7 | theorem | A4, D0.3, D4.3, CT0.1, CT0.2, CT0.8, CT1.29, CT4.1, CT4.3, CT4.9 |
| 201 | CT4.6 | theorem | D4.1, D4.3, CT0.12, CT0.13, CT1.3, CT1.22, CT1.23, CT1.25, CT4.1, CT4.4, CT4.5, CT4.7 |
| 202 | CT4.5a | theorem | A7, D1.11, D4.1, D4.2, D4.3, CT0.6, CT0.11, CT1.22, CT1.23, CT1.25, CT4.1, CT4.2, CT4.3, CT4.4, CT4.5, CT4.6 |
| 203 | CT4.10 | theorem | CT0.2, CT0.12, CT1.2, CT1.10, CT1.11, EW.27, CT3.7, CT4.4 |
| 204 | Def-H.1 | definition | — |
| 205 | Def-H.2 | definition | — |
| 206 | Def-H.3 | definition | — |
| 207 | FT.1 | theorem | D0.6, D0.7, CT0.6a, CT2.6, Def-H.1 |
| 208 | FT.3 | theorem | EM.7, Def-H.1, Def-H.3, FT.1 |
| 209 | Def-H.4 | definition | — |
| 210 | FT.4 | theorem | Def-H.1, FT.1, FT.3, Def-H.4 |
| 211 | Def-H.5 | definition | — |
| 212 | FT.5 | theorem | Def-H.2, FT.1, Def-H.5 |
| 213 | FT.6 | theorem | D0.7, CT0.9, Def-H.5 |
| 214 | FT.9 | theorem | D4.1, CT0.14, EM.17, EM.18, EM.19, EM.20, CT3.7, CT3.10 |
| 215 | FT.10 | theorem | D0.10, CT2.3, CT2.5, CT3.17, CT3.18, CT3.22, FT.9 |
| 216 | FT.12 | theorem | D3.4, EW.3, EW.22, EW.36, EW.36a |
| 217 | FT.11 | theorem | A8, C8, D2.5, D4.3, CT0.7, CT0.12, EW.13, EW.33, EW.20, EM.9, CT3.7, CT3.10, CT3.22, CT4.4, FT.12 |
| 218 | FT.13 | theorem | CT0.7a, CT1.1, CT1.2 |
| 219 | Def-H.8 | definition | — |
| 220 | FT.22 | theorem | D1.4, D1.5, D1.7, D1.12, D2.4, D2.5, CT0.13, CT2.5, EW.17, EW.18, EM.20, Def-H.4, FT.9 |
| 221 | FT.23 | theorem | C3, D1.6, CT0.7, CT1.1, CT1.2, CT1.12, CT2.6 |
| 222 | FT.24 | theorem | A1, D1.1, D1.4, D1.6, D1.7, D3.7, CT1.12, CT1.19a, CT1.29, CT2.9, EM.20, Def-H.4, FT.22, FT.23 |
| 223 | FT.14 | theorem | A1, A2, A4, C8, C9, C10, D3.4, D3.5, CT0.1, CT0.6, CT0.7, CT0.9, CT1.12, CT1.19, CT1.25, EW.13, EW.17, EM.9, EM.16, FT.9, FT.11, FT.12, FT.13, Def-H.8, FT.22, FT.24 |
| 224 | Def-H.9 | definition | — |
| 225 | Def-H.14 | definition | — |
| 226 | FT.25 | theorem | D1.7, CT1.19a, FT.9, Def-H.9, Def-H.14, FT.22, FT.24 |
| 227 | FT.15 | theorem | EM.9, FT.1, FT.13, Def-H.9, FT.25 |
| 228 | FT.16 | theorem | D3.3, D3.9, CT0.6, CT0.9, CT0.13, CT1.29, CT3.17, CT3.18, CT3.22, Def-H.1, FT.1, FT.10, Def-H.9 |
| 229 | Def-H.35 | definition | — |
| 230 | FT.17 | theorem | D4.2, CT0.6, CT0.9, CT1.29, CT4.2, CT4.3, CT4.9, Def-H.1, FT.1, Def-H.9 |
| 231 | Def-H.39 | definition | — |
| 232 | Def-H.40 | definition | — |
| 233 | FT.18 | theorem | A1, D2.11, D3.8, D3.9, CT3.17, CT3.18 |
| 234 | Def-H.10 | definition | — |
| 235 | FT.19 | theorem | D3.1, CT2.5, CT2.8, CT3.2, CT3.18, CT3.22, Def-H.9, Def-H.10 |
| 236 | Def-H.11 | definition | — |
| 237 | Def-H.36 | definition | — |
| 238 | FT.20 | theorem | FT.11, FT.13, Def-H.9, FT.16, FT.19, FT.25 |
| 239 | Def-H.12 | definition | — |
| 240 | Def-H.13 | definition | — |
| 241 | Def-H.15 | definition | — |
| 242 | FT.21 | theorem | D2.12, D3.1, D3.2, D3.3, CT0.12, CT0.13, EM.9, EM.9b, FT.1, Def-H.9, FT.20, Def-H.12, Def-H.13, Def-H.15 |
| 243 | Def-H.16 | definition | — |
| 244 | FT.26 | theorem | A8, CT0.12, CT0.14, CT2.2, CT2.3, CT2.4, CT2.5, FT.19, FT.20, Def-H.15, Def-H.16 |
| 245 | FT.27 | theorem | A1, D0.8, D3.1, D3.3, D3.8, D3.9, CT0.13, CT3.11, CT3.17, FT.16, Def-H.10, FT.19, FT.20, Def-H.12, Def-H.13, Def-H.14, Def-H.15 |
| 246 | Def-H.17 | definition | — |
| 247 | FT.29 | theorem | D2.12, D3.1, D3.2, D3.5, D3.8, D3.9, CT0.13, CT0.14, CT2.5, CT2.8, EM.17, EM.18, EM.20, CT3.2, CT3.4, CT3.7, CT3.8, CT3.9, CT3.10, CT3.10a, CT3.11, CT3.13, CT3.17, CT3.18, CT3.22, FT.9, FT.10, FT.19, FT.26, Def-H.17 |
| 248 | Def-H.18 | definition | — |
| 249 | FT.30 | theorem | D1.2, D1.3, D1.6, D2.11, D4.2, D4.3, P4, CT0.6, CT0.7, CT0.7a, CT0.12, CT0.14, CT1.1, CT1.2, CT1.12, CT2.5, CT2.6, CT2.7, CT1.19, CT1.20, CT1.21, CT1.25, CT1.29, CT2.9, EW.13, EW.18, EW.32, EW.33, EM.9, CT3.18, CT3.22, CT4.4, Def-H.2, FT.3, FT.9, FT.11, FT.12, FT.20, Def-H.14, FT.22, FT.24, FT.25, Def-H.17, FT.29, Def-H.18 |
| 250 | FT.31 | theorem | C9, D1.1, D1.6, D1.7, CT0.9, CT2.6, CT1.19, CT1.19a, CT1.29, EM.20, FT.22, FT.24 |
| 251 | Def-H.19 | definition | — |
| 252 | Def-H.37 | definition | — |
| 253 | FT.28 | theorem | A1, D0.8, D1.4, D3.1, D3.3, D3.4, D3.8, D3.9, CT0.5, CT0.6, CT0.11, CT0.14, CT3.11, CT3.17, CT4.9, Def-H.4, Def-H.9, Def-H.35, FT.17, Def-H.10, FT.19, FT.20, FT.22, FT.24, FT.25, Def-H.15, Def-H.16, FT.26, FT.27 |
| 254 | FT.32 | theorem | A1, D0.8, D1.4, D3.1, D3.3, D3.8, D3.9, CT0.5, CT0.6, CT0.11, CT0.13, CT0.14, CT1.19a, CT3.11, CT3.17, CT4.9, Def-H.4, Def-H.9, Def-H.35, FT.17, Def-H.10, FT.20, FT.22, FT.24, FT.25, Def-H.15, FT.26, FT.27, FT.28 |
| 255 | FT.33 | theorem | D1.6, D2.9, CT2.9, EW.32, EW.33, EW.20, EW.22, EM.6, Def-H.2, Def-H.9, FT.23, FT.24, Def-H.37, FT.32 |
| 256 | FT.34 | theorem | D1.4, D1.7, CT3.17, CT3.17a, Def-H.10, FT.19, FT.22, FT.23, FT.24, FT.25, FT.27 |
| 257 | FT.36 | theorem | C9, D0.10, D1.5, CT0.6a, CT1.12, EM.5, EM.6, EM.7, Def-H.2, Def-H.3, FT.1, Def-H.5, FT.5, FT.6 |
| 258 | FT.37 | theorem | C9, D1.6, D1.7, CT0.9, CT1.29, FT.22, FT.24, FT.31, FT.34 |
| 259 | FT.38 | theorem | D1.6, CT0.9, CT1.12, CT2.6, CT1.19, Def-H.2, FT.1, FT.22, FT.24, Def-H.19, FT.33, FT.34 |
| 260 | FT.39 | theorem | D2.11, CT2.8, CT3.9, CT3.10, CT3.13, CT3.15, CT3.17, CT3.18, CT3.22, FT.11, Def-H.9, FT.18, Def-H.10, FT.19, Def-H.11, FT.21, Def-H.15 |
| 261 | FT.40 | theorem | D1.4, D2.6, D3.4, CT0.9, EM.9, Def-H.4, FT.28 |
| 262 | FT.41 | theorem | C10, D3.4, D3.8, P4, CT0.9, CT0.13, EW.13, EM.9, CT3.17, CT3.17a, Def-H.8, FT.14, Def-H.10, Def-H.13, FT.22, FT.34, FT.28 |
| 263 | Def-H.20 | definition | — |
| 264 | FT.42 | theorem | D0.8, D1.7, D3.1, D3.3, D4.2, CT0.5, CT0.6, CT0.11, CT0.13, CT0.14, CT3.11, CT4.1, CT4.3, CT4.9, Def-H.1, Def-H.8, Def-H.9, Def-H.35, FT.17, FT.22, FT.23, FT.24, FT.25, Def-H.15, FT.26, FT.34, FT.41, Def-H.20, FT.32 |
| 265 | FT.45 | theorem | A1, D0.8, D1.7, D3.1, D3.3, CT0.5, CT0.6, CT0.14, CT1.12, CT4.9, Def-H.35, FT.17, FT.20, FT.22, FT.23, FT.24, FT.25, FT.26, FT.27, Def-H.20, FT.28, FT.32, FT.42 |
| 266 | FT.46 | theorem | A1, A2, D0.8, D1.2, CT0.5, CT0.6, CT0.11, Def-H.20, FT.42, FT.45 |
| 267 | FT.47 | theorem | CT0.11, CT1.12, CT2.6, CT2.7, CT4.1, Def-H.19, FT.46, FT.45 |
| 268 | FT.48 | theorem | D1.6, CT2.5, CT2.6, CT1.19, CT1.20, FT.22, FT.24, FT.31, Def-H.19, FT.33, FT.34, FT.38 |
| 269 | FT.43 | theorem | D1.7, FT.22, FT.23, FT.24, FT.25, Def-H.20, FT.42 |
| 270 | FT.35 | theorem | D0.8, D1.4, D3.1, D3.9, D4.1, D4.2, CT0.6, CT0.11, CT0.13, CT0.14, CT3.11, CT3.17, CT4.1, CT4.3, Def-H.9, Def-H.35, FT.17, Def-H.10, FT.19, Def-H.12, FT.22, Def-H.15, FT.34, FT.28, FT.32 |
| 271 | FT.50 | theorem | D0.8, D1.4, D1.7, D3.1, D3.9, D4.2, CT0.5, CT0.6, CT3.17, CT4.1, CT4.3, Def-H.9, Def-H.35, FT.17, Def-H.10, Def-H.12, FT.22, FT.23, FT.24, FT.27, FT.34, FT.41, FT.35, FT.45 |
| 272 | FT.52 | theorem | CT1.2, CT1.12, CT1.13, CT1.14, EW.32, EW.33, FT.13, Def-H.8, Def-H.9, FT.25, FT.33, FT.34, FT.43, FT.50 |
| 273 | FT.53 | theorem | D1.6, CT1.12, CT2.6, CT1.19, CT1.20, FT.22, FT.24, FT.31, FT.33, FT.34, FT.38, FT.48 |
| 274 | Def-H.21 | definition | — |
| 275 | FT.54 | theorem | D2.9, CT2.9, EW.32, EW.33, FT.33, FT.47, Def-H.21, Def-H.37, FT.42, FT.45 |
| 276 | FT.55 | theorem | D2.9, CT2.11, EW.32, FT.22, FT.31, FT.34, FT.52, Def-H.21, FT.28, FT.45 |
| 277 | FT.56 | theorem | A3, A4, CT0.7, CT0.7a, CT0.9, CT1.2, EW.32, FT.13, Def-H.8, FT.23, FT.34, FT.52, FT.55 |
| 278 | FT.57 | theorem | C8, D3.10, CT0.12, CT3.5, Def-H.13, FT.41 |
| 279 | Def-H.22 | definition | — |
| 280 | FT.58 | theorem | A7, D0.8, D2.12, D3.1, D3.2, D3.9, CT0.12, CT0.13, CT0.14, CT1.4, EM.2, CT3.7, CT3.8, CT3.9, FT.20, Def-H.13, Def-H.15, Def-H.16, FT.26, FT.41, FT.57, Def-H.22 |
| 281 | FT.49 | theorem | D0.8, D3.1, D3.3, D3.9, D4.2, CT0.5, CT0.6, CT0.13, CT0.14, CT3.11, CT3.17, CT4.1, CT4.3, Def-H.9, Def-H.35, FT.17, Def-H.10, Def-H.12, FT.22, FT.23, FT.24, FT.25, Def-H.15, FT.26, FT.34, FT.41, FT.45 |
| 282 | FT.59 | theorem | A7, D2.12, D3.1, D3.2, D3.3, D3.8, D4.1, D4.2, CT0.5, CT0.6, CT0.9, CT0.11, CT0.13, CT0.14, CT1.4, CT1.6, CT1.7, CT1.9, CT3.20, CT3.17, CT4.1, CT4.3, CT4.4, FT.3, Def-H.10, FT.20, Def-H.13, FT.21, FT.40, FT.41, Def-H.22, FT.58, FT.49 |
| 283 | Def-H.38 | definition | — |
| 284 | Def-H.23 | definition | — |
| 285 | FT.60 | theorem | A3, A4, D1.5, D1.7, D3.7, CT0.7, CT0.7a, CT0.8, CT0.12, CT1.2, CT2.5, EW.32, EW.33, EM.8, FT.22, FT.25, FT.33, FT.34, FT.52, Def-H.21, FT.54, FT.55, FT.56, Def-H.38, Def-H.23, FT.43, FT.45, FT.49, FT.50 |
| 286 | FT.61 | theorem | A8, D0.7, D1.7, D2.7, D3.3, D3.5, D3.6, P4, CT0.9, CT0.10, CT2.5, CT2.6, CT2.8, CT1.20, EM.20, FT.9, FT.22, FT.24, Def-H.15, Def-H.16, FT.26, FT.31, Def-H.19, FT.34, FT.48, FT.53, Def-H.21, FT.58 |
| 287 | FT.51 | theorem | CT0.9, CT0.10, CT2.6, CT2.7, FT.45 |
| 288 | FT.62 | theorem | A7, D0.8, D0.9, D1.11, D4.1, D4.2, CT0.5, CT0.6, CT0.9, CT0.10, CT0.11, CT0.11b, CT2.5, EW.17, EM.9b, CT4.1, CT4.1a, CT4.2, CT4.3, CT4.9, FT.3, FT.17, FT.20, FT.21, Def-H.16, FT.40, Def-H.20, FT.28, FT.32, FT.42, FT.45, FT.49, FT.51 |
| 289 | Def-H.24 | definition | — |
| 290 | FT.44 | theorem | FT.41, Def-H.20, FT.28, FT.32, FT.35, FT.42, FT.43 |
| 291 | FT.63 | theorem | A4, D2.6, D2.9, D3.3, D3.4, CT0.6, CT0.7, CT0.9, CT0.10, CT0.12, CT0.13, CT0.14, CT2.5, CT1.29, CT2.9, EW.32, EW.22, EM.2, EM.6, EM.9, CT3.13, CT3.17, CT3.22, CT4.3, CT4.4, CT4.9, FT.9, FT.11, FT.12, Def-H.35, FT.19, Def-H.36, FT.20, FT.21, FT.22, FT.24, FT.25, FT.26, FT.29, FT.31, FT.33, FT.37, FT.39, FT.40, FT.41, Def-H.20, FT.47, FT.53, Def-H.37, FT.54, FT.58, FT.59, Def-H.38, Def-H.23, FT.60, FT.61, FT.62, FT.42, FT.43, FT.44, FT.49 |
| 292 | FT.66 | theorem | A8, D0.10, D1.6, D2.1, D2.3, D2.11, CT1.12, CT1.13, CT1.14, CT2.3, CT2.4, CT2.5, CT2.6, CT2.8, CT1.19, CT1.20, Def-H.14, FT.22, Def-H.16, FT.26, FT.31, Def-H.19, FT.33, FT.38, Def-H.20, FT.48, FT.53, Def-H.21, FT.61, FT.62, Def-H.24, FT.63 |
| 293 | Def-H.25 | definition | — |
| 294 | FT.67 | theorem | A4, A7, A8, D0.1, D0.5, D0.8, D0.10, D1.1, D1.2, D1.3, D1.5, D2.11, D3.3, D3.5, D3.6, CT0.9, CT0.10, CT0.11, CT0.13, CT0.14, CT2.8, CT1.20, CT4.1, CT4.4, FT.9, FT.22, FT.24, Def-H.16, FT.27, Def-H.18, Def-H.20, FT.61, FT.62, Def-H.25, FT.28, FT.32 |
| 295 | FT.68 | theorem | A4, A5, A8, D0.1, D0.10, D1.2, D1.5, D2.11, CT0.11, CT0.13, CT2.8, CT1.20, CT4.1, CT4.3, FT.17, FT.20, FT.22, Def-H.16, FT.27, Def-H.18, Def-H.20, FT.48, Def-H.38, FT.61, FT.62, Def-H.24, FT.66, Def-H.25, FT.67, FT.28, FT.32, FT.42, FT.45, FT.63 |
| 296 | Def-H.26 | definition | — |
| 297 | FT.70 | theorem | A4, D0.1, CT0.11, FT.62, Def-H.25, FT.67, FT.68, Def-H.26, FT.42, FT.45, FT.63 |
| 298 | FT.71 | theorem | D1.11, D4.1, D4.2, D4.3, CT1.22, CT1.23, CT1.25, CT4.1, CT4.2, CT4.3, CT4.4, CT4.5, CT4.6, FT.3, FT.62, Def-H.26, FT.70, FT.63 |
| 299 | FT.64 | theorem | D0.10, D1.3, D1.7, D2.4, D2.11, D3.7, CT0.9, CT0.10, CT2.5, CT2.6, CT2.7, FT.22, FT.24, Def-H.16, FT.34, Def-H.20, FT.48, FT.53, FT.61, FT.62, FT.32, FT.42, FT.43, FT.45, FT.51 |
| 300 | FT.72 | theorem | D0.1, CT1.29, Def-H.25, FT.67, Def-H.26, FT.43, FT.44, FT.63, FT.64 |
| 301 | FT.69 | theorem | A4, A8, D0.1, D0.8, D0.10, D1.4, D1.5, D3.3, CT0.11, CT4.1, FT.17, FT.22, FT.62, Def-H.25, FT.67, FT.68, FT.28, FT.32, FT.42, FT.45, FT.63 |
| 302 | FT.73 | theorem | A8, C11, D1.11, D3.1, D3.7, D4.1, D4.2, D4.3, CT1.25, EM.20, CT3.17, CT4.1, CT4.7, CT4.10, FT.3, FT.20, FT.22, Def-H.16, FT.54, FT.57, FT.59, FT.67, FT.72, FT.28, FT.32, FT.44, FT.49, FT.50, FT.63, FT.64, FT.69 |
| 303 | Def-H.27 | definition | — |
| 304 | FT.74 | theorem | A4, A8, D0.1, D0.8, D1.4, D1.5, D3.3, D3.5, CT0.9, FT.21, FT.22, FT.62, Def-H.25, FT.67, FT.68, Def-H.27, FT.28, FT.69 |
| 305 | FT.75 | theorem | A8, D1.4, D1.5, D3.3, CT2.8, CT4.1, CT4.5, FT.21, FT.22, FT.34, FT.62, Def-H.25, FT.67, FT.68, Def-H.26, FT.70, FT.71, Def-H.27, FT.74, FT.28, FT.45, FT.63, FT.69 |
| 306 | FT.76 | theorem | D2.9, CT0.7a, CT2.5, FT.22, FT.47, FT.52, Def-H.21, Def-H.37, FT.54, FT.55, Def-H.38, Def-H.23, FT.60, FT.32, FT.43, FT.44, FT.45, FT.63 |
| 307 | FT.77 | theorem | Def-H.37, Def-H.38, FT.60, FT.73, FT.44, FT.63, FT.76 |
| 308 | Def-H.28 | definition | — |
| 309 | FT.78 | theorem | A4, A8, D0.6, D0.8, D2.6, CT0.11, CT0.13, CT0.14, CT1.20, FT.27, FT.40, Def-H.25, FT.67, FT.68, Def-H.26, FT.70, FT.71, Def-H.28, FT.69 |
| 310 | FT.79 | theorem | CT0.11, CT1.20, Def-H.25, FT.67, FT.68, FT.70, FT.77, Def-H.28, FT.44, FT.69, FT.76, FT.78 |
| 311 | FT.80 | theorem | A8, D0.6, D0.7, D1.5, D2.6, CT0.13, CT0.14, CT2.5, CT2.8, Def-H.1, FT.1, Def-H.4, FT.19, Def-H.13, FT.22, Def-H.16, FT.26, FT.27, FT.38, FT.40, FT.48, Def-H.24, FT.66, Def-H.25, FT.67, FT.68, Def-H.28, FT.78 |
| 312 | Def-H.29 | definition | — |
| 313 | Def-H.30 | definition | — |
| 314 | FT.85 | theorem | A4, A5, A7, D0.5, D1.11, D4.2, D4.3, P1, P3, P5, CT0.2, CT0.9, CT0.11, CT0.12, CT0.14, CT2.1, CT2.8, CT1.22, CT1.25, CT1.29, CT2.9, CT4.1, CT4.5, CT4.7, CT4.10, CT4.9, FT.16, FT.30, FT.37, FT.47, FT.54, Def-H.25, FT.67, Def-H.26, FT.70, FT.71, FT.75, Def-H.30, FT.44, FT.63, FT.76 |
| 315 | FT.86 | theorem | D0.7, D1.2, CT0.3, CT0.6, CT0.11, CT1.12, CT1.22, CT1.29, EM.5, EM.7, CT4.2, CT4.5, FT.1, FT.38, FT.67, FT.68, Def-H.26, FT.70, Def-H.30, FT.85 |
| 316 | FT.87 | theorem | D2.6, D2.7, P1, P5, CT0.9, CT0.11, CT1.12, CT1.29, EW.33, EM.9, CT4.5, FT.20, FT.22, FT.34, FT.40, FT.47, FT.52, Def-H.21, Def-H.37, FT.54, Def-H.38, FT.60, FT.61, Def-H.24, FT.66, FT.67, FT.68, FT.70, FT.73, FT.79, Def-H.30, FT.85, FT.86, FT.44, FT.64, FT.76 |
| 317 | FT.88 | theorem | D2.6, D2.7, D3.5, D3.6, CT0.9, FT.40, FT.64, FT.78 |
| 318 | FT.81 | theorem | D1.5, D2.6, D3.4, D3.7, D3.8, D3.9, D3.10, D4.1, D4.3, P1, P5, CT0.9, CT0.12, CT0.13, CT0.14, CT1.25, CT2.9, EW.8, EW.13, EW.32, EW.33, EW.20, EW.24, EW.27, EW.35, EM.9, EM.20, CT3.20, CT3.21, CT3.15, CT3.17, CT3.18, CT3.22, CT4.1, CT4.4, CT4.5, FT.19, FT.20, FT.26, FT.27, FT.30, FT.34, FT.41, FT.52, FT.55, FT.57, FT.60, FT.71, FT.79, FT.80, Def-H.29, FT.76 |
| 319 | FT.89 | theorem | P2, P5, CT0.5, CT0.6, CT0.11, EM.20, FT.68, Def-H.26, FT.70, FT.73, FT.86, FT.63, FT.81 |
| 320 | FT.90 | theorem | C10, D0.6, D0.7, D2.6, D2.9, CT0.6, CT1.29, Def-H.1, FT.1, FT.3, FT.4, Def-H.9, FT.15, FT.16, FT.20, FT.26, FT.36, FT.38, FT.40, FT.52, FT.55, FT.60, FT.67, FT.79, FT.86, FT.87, FT.44, FT.78 |
| 321 | FT.83 | theorem | D0.8, D0.9, D1.2, D1.11, D3.1, D3.2, D4.1, D4.3, P1, P5, CT0.5, CT0.14, CT1.20, CT1.25, CT2.9, EW.13, EW.33, EW.20, EW.24, EW.27, EW.35, EM.9, EM.20, CT3.20, CT3.15, CT3.17, CT3.22, CT4.1, CT4.5, FT.20, FT.27, FT.30, FT.34, FT.59, Def-H.29 |
| 322 | FT.84 | theorem | D1.5, D2.6, D3.4, D3.9, D4.1, D4.3, P1, P5, CT0.11, CT0.14, CT2.9, EW.8, EW.13, EW.32, EW.33, EW.20, EW.23, EW.24, EW.27, EW.35, EM.9, EM.20, CT3.20, CT3.15, CT3.17, CT3.18, CT3.22, CT4.1, CT4.4, CT4.5, FT.11, FT.12, FT.19, FT.20, FT.26, FT.27, FT.30, FT.34, FT.41, FT.52, Def-H.38, FT.60, FT.71, Def-H.29, FT.76, FT.83 |
| 323 | FT.93 | theorem | A1, A3, C1, C2, C3, CT0.6, CT0.7, CT0.7a, CT0.12, CT0.14, CT1.1, CT1.2, CT1.4, CT1.8, EW.5, EW.32, Def-H.14, FT.87, FT.88, FT.89, FT.90, FT.78, FT.84 |
| 324 | FT.95 | theorem | D2.6, CT0.3, EW.18, FT.22, FT.40, Def-H.25, Def-H.26, FT.80, FT.86, FT.87, FT.88, FT.89, FT.69 |
| 325 | FT.101 | theorem | A3, A4, C1, D0.5, CT0.7, CT0.7a, CT0.8, CT0.9, CT1.1, CT1.2, CT1.11a, Def-EM.21, EM.23, EM.24, FT.13, FT.93 |
| 326 | Def-H.31 | definition | — |
| 327 | FT.102 | theorem | A4, A8, D0.3, D0.4, D1.2, CT0.6, CT0.7, CT0.7a, CT0.8, CT0.11, CT1.1, CT1.2, L2, L3, L5, CT2.8, EW.12, CT4.5a, Def-H.25, FT.67, FT.68, Def-H.26, FT.70, FT.79, FT.93, Def-H.31, FT.69 |
| 328 | FT.103 | theorem | CT0.8, L3, FT.67, FT.68, Def-H.26, FT.70, FT.79, Def-H.31, FT.102, FT.69, FT.76 |
| 329 | FT.104 | theorem | P1, P5, L2, L3, Def-H.39, Def-H.40, FT.73, FT.77, FT.79, FT.87, FT.89, FT.102, FT.103, FT.76, FT.84 |
| 330 | Def-H.32 | definition | — |
| 331 | FT.108 | theorem | A4, A8, D0.3, D1.2, D1.3, D3.3, CT0.7, CT0.7a, CT1.2, CT1.5, L0, L0a, Def-H.25, FT.67, FT.68, Def-H.26, FT.70, FT.74, Def-H.31, FT.102, FT.103, FT.104, Def-H.32, FT.69 |
| 332 | FT.109 | theorem | CT1.2, CT1.7 |
| 333 | Def-H.41 | definition | — |
| 334 | FT.110 | theorem | CT0.7, CT0.12, FT.68, Def-H.32 |
| 335 | FT.111 | theorem | CT0.12, CT1.2, CT1.8, FT.109 |
| 336 | FT.112 | theorem | FT.14, FT.70, FT.109, FT.110, FT.63 |
| 337 | FT.113 | theorem | P4, L3, L4, FT.111, FT.112 |
| 338 | FT.116 | theorem | D3.9, CT1.8, CT3.1, CT3.2, CT3.3, CT3.15, FT.111 |
| 339 | FT.117 | theorem | D3.8, D3.9, CT3.15, CT3.16, CT3.17, CT3.18, CT3.22, FT.111, FT.116 |
| 340 | Def-H.42 | definition | — |
| 341 | FT.118 | theorem | D3.8, CT0.5, CT0.6, CT0.7, CT0.11, CT0.12, CT0.14, EW.32, CT3.20, CT3.2, FT.68, FT.93, FT.109, FT.110, FT.117 |
| 342 | FT.119 | theorem | P4, CT0.12, L3, L4, CT3.13, FT.111, FT.112, FT.113, FT.118 |
| 343 | Def-H.33 | definition | — |
| 344 | FT.122 | theorem | D1.4, D1.5, D2.6, EM.24, Def-H.1, FT.22, FT.25, FT.87, FT.89 |
| 345 | Def-H.34 | definition | — |
| 346 | FT.123 | theorem | A8, D2.6, CT0.7, CT0.7a, EW.32, EW.33, EM.8, FT.22, FT.25, Def-H.38, FT.60, Def-H.33, FT.122, Def-H.34, FT.28 |
| 347 | FT.124 | theorem | D0.10, D1.4, CT0.7, CT0.7a, CT1.2, CT3.22, FT.87, FT.93, FT.95, FT.101, FT.117, FT.119, FT.123 |
| 348 | FT.125 | theorem | Def-H.38, FT.79, FT.80, FT.87, FT.89, FT.93, FT.117, FT.119, FT.122, FT.123, FT.124, Def-H.34, FT.81, FT.84 |
| 349 | FT.126 | theorem | EW.32, FT.88, FT.101, FT.122, FT.123, FT.124, Def-H.34 |
| 350 | FT.127 | theorem | A8, D1.2, D3.1, D3.4, D3.10, D4.1, D4.3, P1, P4, CT0.7, CT0.12, CT0.13, CT0.14, CT1.2, CT1.3, CT1.23, CT1.25, EW.8, EW.13, EW.32, EW.33, EW.20, EW.24, EM.9, CT3.2, CT3.8, CT3.13, CT4.1, CT4.2, CT4.3, CT4.5, CT4.6, FT.20, FT.33, Def-H.37, FT.54, FT.93, Def-H.32, FT.108, FT.109, FT.116, FT.117, Def-H.33, FT.123, Def-H.34 |
| 351 | FT.128 | theorem | CT1.2, FT.122, FT.123, Def-H.34, FT.127 |
| 352 | Def-H.43 | definition | — |
| 353 | FT.129 | theorem | D2.6, D3.4, EM.9, EM.24, FT.15, Def-H.15, FT.40, FT.87, FT.89, FT.90, Def-H.33, FT.122, FT.123, FT.126, Def-H.34, FT.128, Def-H.43 |
| 354 | FT.130 | theorem | CT1.1, CT1.2, EM.9, Def-H.34, FT.128, FT.129 |
| 355 | FT.133 | theorem | A4, A8, D0.5, D0.10, D1.6, D2.6, D2.7, D3.3, D3.4, D3.5, D3.6, CT2.8, EM.9, EM.9a, Def-EM.20, EM.20, Def-EM.21, EM.23, EM.24, FT.22, FT.40, FT.88, FT.101 |
| 356 | FT.134 | theorem | FT.40, Def-H.33, FT.122, FT.126, Def-H.34, FT.128, Def-H.43, FT.129, FT.133 |
| 357 | FT.135 | theorem | A3, A4, CT0.7, CT0.7a, CT0.8, CT1.2, Def-EM.21, EM.24, FT.93, FT.101 |
| 358 | FT.136 | theorem | CT0.7, CT0.12, CT0.13, CT1.1, CT1.2, FT.30, FT.93, FT.101, FT.122, FT.126, FT.133 |
| 359 | FT.141 | theorem | A3, A8, CT0.6, CT0.7, CT0.7a, CT0.12, CT0.13, CT0.14, CT1.1, CT1.2, CT1.3, CT1.5, FT.30, FT.93, FT.101, Def-H.33, FT.122, FT.125, FT.126, Def-H.34, FT.135, FT.136 |
| 360 | FT.142 | theorem | A1, A8, D0.8, D1.5, D3.3, P1, P4, P5, CT0.6, CT0.12, CT0.13, CT0.14, CT1.2, CT1.7, CT3.11, Def-H.4, FT.19, FT.68, FT.109, Def-H.41, FT.110, FT.111, FT.112, Def-H.42, FT.118, FT.141, FT.28 |
| 361 | FT.144 | theorem | A5, A6, A8, D1.1, D1.2, D1.3, D1.4, D1.5, D2.6, D2.7, D2.11, CT0.1, CT0.2, CT0.13, CT2.5, EW.32, EM.9, CT4.2, Def-H.4, FT.40, FT.79, FT.88, FT.108, FT.117, Def-H.33, FT.122, Def-H.34, FT.127, FT.128, Def-H.43, FT.129, FT.130, FT.133, FT.134, FT.76 |
| 362 | FT.156 | theorem | A3, A6, A7, A8, C3, D1.2, D2.1, D2.7, CT0.7, CT0.12, CT1.1, CT1.2, CT1.4, CT1.5, CT1.8, CT1.10, CT1.12, CT2.6, FT.30, FT.101, FT.111, FT.133, FT.136, FT.141, FT.144 |
| 363 | FT.158 | theorem | P4, P5, CT0.12, CT1.2, CT1.4, CT1.8, FT.14, FT.68, FT.70, FT.89, FT.109, Def-H.41, FT.110, FT.111, FT.112, FT.113, FT.119, FT.142, FT.156, FT.63 |

## Statements (dependencies first)

### A1

$$
\mathcal Q=\{q_n\}_{n\ge1};\qquad
\mathcal H_q\cong\mathbb C^2;\qquad
\forall(p,q)\in\mathcal Q\times\mathcal Q,\ p\ne q:\quad
\rho_{pq}\in\mathfrak H(\mathcal H_p\otimes\mathcal H_q),\ \ \rho_{pq}\succeq0,\ \ \mathfrak T(\rho_{pq})=1 .
$$

### A2

$$
\forall(p,q):\qquad C(p,q)=1\,\mathfrak q .
$$

### A3

$$
\mathcal H_p\otimes\mathcal H_q=\vee^2\oplus\wedge^2;
$$
$$
S(\sigma_\mu\otimes\sigma_\nu)=\sigma_\nu\otimes\sigma_\mu,\quad S^2=\mathbb1;\qquad
T(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu\,(\sigma_\mu\otimes\sigma_\nu),\quad
\eta=(-,+,+,+),\quad T^2=\mathbb1 .
$$

### A4

$$
(p,q)\in\mathcal R\iff\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\le\varepsilon_q\ \ \vee\ \ \bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\ge1-\varepsilon_q;\qquad
n_{\mathcal R}(p)=\bigl|\{q:(p,q)\in\mathcal R\}\bigr|
$$
$$
\alpha_{pq}:=\begin{cases}0&\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\le\varepsilon_q\\[1mm] \pi&\bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\ge1-\varepsilon_q\end{cases};\qquad
\alpha_{pq}\in\{0,\pi\}\quad\forall(p,q)\in\mathcal R;
$$
$$
\exists\,\rho_{pq}:\ \bigl|\Pi_{\mathcal V}\rho_{pq}\bigr|\le\varepsilon_q;\qquad
\exists\,\rho_{p'q'}:\ \bigl|\Pi_{\mathcal V}\rho_{p'q'}\bigr|\ge1-\varepsilon_q .
$$

### A5

$$
\rho_\circ=\tfrac14 I;\qquad
\rho\mapsto U\rho U^\dagger,\quad U\sim\mu_\star\bigl(\mathrm{SU}(2)\bigr),\quad U\notin\mathfrak L .
$$

### A6

$$
\mu_\star:=\mu_{\mathrm{Haar}}\bigl(\mathrm{SU}(2)\bigr);\qquad
U\sim\mu_\star;\qquad
U\notin\mathfrak L;\qquad
\mathcal T(\rho):=U\rho U^\dagger;\qquad
\mathcal T^{-1}(\rho)=U^\dagger\rho U
$$
$$
\mathfrak T\bigl(\mathcal T(\rho)\bigr)=\mathfrak T(\rho);\qquad
\mathcal T^{2}\ne\mathbb1;\qquad
\tau_n\to\tau_{n+1}:\ \ \rho\mapsto\mathcal T(\rho);\qquad
\neg\exists\,\tau^{-1}
$$
$$
\bigl|\mathfrak L(\tau_{n+1})\bigr|\ \ge\ \bigl|\mathfrak L(\tau_n)\bigr|;\qquad
\bigl|\mathfrak L(\tau_{n+1})\bigr|\ =\ \bigl|\mathfrak L(\tau_n)\bigr|\,+\,n_{\mathrm{real\_out}}(\tau_n) .
$$

### A7

$$
\forall n\ge0:\quad\Gamma=(V,E),\qquad E\subseteq V\times V
$$
$$
\tau(v):=\bigl(\partial^{\leftarrow}(v),\partial^{\rightarrow}(v)\bigr)\in\Xi_n;\qquad
e\in E_{\mathcal R}\mapsto\phi_e;\qquad
e\in E_{\mathcal R}\mapsto\alpha_e\in\{0,\pi\}
$$
$$
\mathfrak L=\bigcup_{n\ge0}\mathfrak L(\tau_n);\qquad
\mathfrak L(\tau_n)\subseteq\mathfrak L(\tau_{n+1});\qquad
\bigl|\mathfrak L(\tau_0)\bigr|=0;\qquad
\bigl|\mathfrak L(\tau_n)\bigr|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k) .
$$

### A8

$$
\mathbf F=\mathbf F_{(+,\mathcal R)}\oplus\mathbf F_{(-,\mathcal R)}\oplus\mathbf F_{(+,\mathcal V)}\oplus\mathbf F_{(-,\mathcal V)}\oplus\mathbf F_{\mathrm{st}};
$$
$$
\mathbf F_{(+,\mathcal R)}=F_G\oplus F_H\oplus F_{D^+};\qquad
\mathbf F_{(-,\mathcal R)}=F_{W^+}\oplus F_{W^-}\oplus F_Z;\qquad
\mathbf F_{(+,\mathcal V)}=F_{J^+};
$$
$$
\mathbf F_{(-,\mathcal V)}=F_{J^-};\qquad
\mathbf F_{\mathrm{st}}=F_{\mathrm{EM}}\oplus F_{\mathrm{strong}}\oplus F_{D^-};
$$
$$
F_{D^+}=\Lambda\,\mathbb I;\qquad
F_{D^-}:=\bigoplus_{n\ge4}F_n;\qquad
\mathbf F_M=P_M\,\mathbf F\,P_M;
$$
$$
w(C)=\mathcal J(C)\!\!\prod_{e\in E(C)}\!\!G(e)\ \cdot\ (-1)^{\aleph(\sigma,C)};\qquad
Z(\mathcal R)=\sum_{C\in\mathcal R}\ \sum_\sigma w(C) .
$$

### C1

$\mu,\nu,\rho,\ldots\in\{0,1,2,3\}$: Pauli basis $\sigma_0=I_2,\sigma_1,\sigma_2,\sigma_3$ / emergent spacetime coordinates where a metric exists; $i,j,k,\ldots\in\{1,2,3\}$: spatial/Pauli-spatial; $a,b,c,\ldots\in\{1,\dots,8\}$: colour adjoint. Repeated indices: summed.

### C2

$T_A^\dagger=T_A$; $\ [T_A,T_B]=i\,f_{AB}{}^{C}\,T_C$; $\ f_{AB}{}^{C}\in\mathbb R$.

### C3

$\mathcal E_{st}:=\{\,X\in\mathfrak H(\mathbb C^4):\ SX=sX\ \wedge\ TX=tX\,\}$, $s,t\in\{+,-\}$. Symbol $\wedge$: antisymmetrization only ($\wedge^2$, $\varepsilon$-contractions); $\neg$ a sector-label conjunct.

### C5

$\Sigma:=\sum_i\sigma_i\otimes\sigma_i$ (operator); $\Sigma_{\mathrm{tr}}:=\delta^{ij}q_{ij}\in\mathbb R$ (scalar, D2.1); $\neg$ interchangeable.

### C7

$P_M\equiv\mathcal P_M$ (A8). Rung-resolved: $\mathcal P_M^{(n)}$ (D2.3); $\ \mathbf F_M^{(n)}=\mathcal P_M^{(n)}\,\mathbf F\,\mathcal P_M^{(n)}$.

### C8

$F_Z\equiv F_{W^3}$: neutral-weak aspect of A8; $\ F_W:=F_{W^+}\oplus F_{W^-}\oplus F_Z$; pre-mixing seed generator: $W_3$. Bare $Z$ in a spectrum: physical neutral eigenstate (D3.10, EW.24); $Z(\cdot)$ with argument: partition function (A8) / masked resolvent (D2.4).

### C9

Entropy in nats: $S=\ln\Omega$; _bits_ only where explicit. One real edge $=1$ bit $=\ln2$ nats (CT0.9, CT1.29).

### C10

Register accounting (reality principle): registrations convert quantum data to classical alternatives at the ledger. Registering a classical alternative set $X$ for single-shot linear readout ($\mathfrak L$ must distinguish which value was carried, D0.7) assigns the alternatives mutually orthogonal register directions: register cost $=|X|$. Shannon content $=\log_2|X|$ bits is a distinct quantity: source-availability register count $\ne$ channel bit throughput. One channel quantum supplies $C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathcal H_p\otimes\mathcal H_q)=16$ register directions (A2, D0.9). Ledger-level registration data are real: edge transport acts on the reality line by $\{\pm1\}$ (D1.1, CT0.9).

### C11

A5/A6 reading: the conjugation clause is node-level — $\rho\mapsto U\rho U^\dagger$ [A6: $\mathcal T$] with $\rho\in\mathfrak H(\mathcal H_q)\cong\mathfrak H(\mathbb C^2)$ and $U\sim\mu_\star(\mathrm{SU}(2))$ ($2\times2$: well-typed); $\rho_\circ=\tfrac14I$ is the vacuum pair state ($4\times4$). Node tick lifecycle: wait $\to$ data in $\to$ Haar draw/tick [A6: $\tau_n\to\tau_{n+1}$] (virtual states as basis) $\to$ data out/hop $\to$ wait. Draws are not retained: $U\notin\mathfrak L$ [A5, A6].

### D0.1

$\mathcal R:=\{(p,q):\ \mathrm{A4}\ \text{holds}\}$; $\ \mathcal V:=(\mathcal Q\times\mathcal Q)\setminus\mathcal R$; $\ n_{\mathcal R}:=\sum_p n_{\mathcal R}(p)$; global vacuum $\iff n_{\mathcal R}=0$.

### D0.2

$\bigl|\Pi X\bigr|:=\mathfrak T(\Pi X\Pi)=\mathfrak T(\Pi X)$; $\ \ \rho\succeq0\wedge\mathfrak T\rho=1\implies\bigl|\Pi\rho\bigr|\in[0,1]$.

### D0.3

$S_{\mathrm{raw}}(\rho):=-\mathfrak T(\rho\log\rho)=\mathfrak T(\rho K)$; $\ K:=-\log\rho$ (faithful $\rho$). $\ \gamma:=1-4\varepsilon_q$ [A4, D0.4, CT0.8]; $\ \gamma\in(0,1]$ for $\varepsilon_q\in[0,\tfrac14)$. Gibbs tilt (functional calculus): $\tilde{\mathcal T}_\gamma(X):=Xe^{-\gamma X}/\mathfrak T(Xe^{-\gamma X})$ where $\mathfrak T(Xe^{-\gamma X})\ne0$; on states: $\tilde{\mathcal T}_\gamma(\rho)=\rho\,e^{-\gamma\rho}/\mathfrak T(\rho\,e^{-\gamma\rho})$; $\ \gamma=0:$ the identity on trace-$1$ states; for faithful $\rho$: $\tilde{\mathcal T}_\gamma(K)=K\rho^{\gamma}/\mathfrak T(K\rho^{\gamma})$ $\ (\gamma=1:\ =\rho(-\log\rho)/S_{\mathrm{raw}}(\rho))$. Variance functional (reference state explicit): $\mathbb V_\rho(X):=\mathfrak T(\rho X^2)-\bigl(\mathfrak T(\rho X)\bigr)^2$. Lyapunov functional of the tilt: $V(\tilde K):=\mathfrak T(\tilde K^2)$, $\ \tilde K:=K-\mathfrak T(K\rho)\,I$ — monotonicity: L1 (§F, forward pointer). $\tilde{\mathcal T}_\gamma\ne\mathcal T$ [A6]; $\neg$ interchangeable.

### D0.4

$\varepsilon_q\in[0,1]$: threshold of A4; admissible range: CT0.8; sharp choice: $\varepsilon_q=0$.

### D0.5

$\Phi$: phase alphabet of a real edge (CT0.9: $\Phi=\{0,\pi\}$); $\ \sigma_e:=e^{i\phi_e}=(-1)^{\phi_e/\pi}\in\{+1,-1\}$.

### D0.6

hop $:=$ one traversal of one $e\in E_{\mathcal R}$; $\ \delta h(\gamma):=\#\{e\in\gamma\}$; $\ \mathfrak h:=$ length assigned to one hop.

### D0.7

$\mathfrak L:=$ ordered record of retained events [A6, A7: stratification $\mathfrak L=\bigcup_{n\ge0}\mathfrak L(\tau_n)$, $|\mathfrak L(\tau_0)|=0$, monotone under ticks]; $\ \delta\tau:=$ ledger ticks (retained updates along real edges); $\ U\notin\mathfrak L$ [A5, A6].

### D0.8

$n(v):=\partial^{\leftarrow}(v)+\partial^{\rightarrow}(v)$; $\ V_n:=\{v\in V:\ n(v)=n\}$ (vertex set); $\ \Xi_n:=\tau(V_n)=\{(a,b)\in\mathbb N^2:\ a+b=n\}$ (type set); “at rung $n$” $:=$ on $V_n$.

### D0.9

$D_{\mathrm{tick}}(n):=\#\{$independent real registers a vertex of $V_n$ pushes across one pair channel per tick$\}$ — counted by the register accounting of **C10** (one orthogonal direction per admissible classical alternative: source availability, single-shot linear readout; $\neg$ Shannon $\log_2$ counting). $\ C_{\mathrm{cap}}:=\dim_{\mathbb R}\mathfrak H(\mathcal H_p\otimes\mathcal H_q)$ (register directions supplied by $1\mathfrak q$, A2); $\ O(n):=\max\bigl(0,\ D_{\mathrm{tick}}(n)-C_{\mathrm{cap}}\bigr)$.

### D0.10

$\mathfrak C(\mathcal R):=$ configuration set on $E_{\mathcal R}$: finite oriented edge sets $E(C)\subseteq E_{\mathcal R}$ with sign assignments $\sigma$, seal data (D1.2) and vertex types (A7). $w(C)$ (A8) is defined on $\mathfrak C(\mathcal R)$; valid universes (D2.11) form a subset; $Z(\mathcal R):=\sum_{C\in\mathfrak C(\mathcal R)}\sum_\sigma w(C)$ (C12).

### D1.1

$e=(p,q)\in\mathcal R_{\rightarrow}(p)\ \longmapsto\ (\mathcal G_n,\phi_e)$; $\ \mathcal G_n:=$ rung class of $q$; $\ \phi_e:$ D0.5; $\ \neg$registration $\implies e\in\mathcal V$. Reality principle of registration (C10): $\phi_e:=$ phase of the registration transport's action on the reality line $\wedge^2$ (1-dimensional, since $\dim\mathcal H_q=2$ [A1]); the transport preserves the $(S,T)$-grading [A3, A4] and the real Pauli-frame structure — registrations are classical data. On a minimal real edge ($\widehat{ds}^{\,2}=1$ [D1.6]) the geometric factor of the transfer weight $G(e)$ [D3.5] is the edge's alignment holonomy $e^{i\alpha_e}$ — the binary registration read of the A4 branch index at the seal ($\alpha_e=\alpha_{pq}$ for $e=(p,q)$ [A4]; per-edge determination read in **E**: Def-EM.20, EM.20, forward pointer).

### D1.2

seal $:=$ transition of one pair across the A4 criterion (entry/exit of either branch): $\ J^+:\ n_{\mathcal R}:0\to1$ (crystallization); $\ J^-:\ n_{\mathcal R}:1\to0$ (dissolution).

### D1.3

Janus-balanced $\iff\ \#J^+=\#J^-$.

### D1.4

chain $c=(e_1,\dots,e_k)$: $e_i\in E_{\mathcal R}$, $\ t(e_i)=s(e_{i+1})$; $\ s(c):=s(e_1)$; $\ t(c):=t(e_k)$; $\ \partial c:=t(c)-s(c)$ (formal difference of vertices); closed $\iff\ \partial c=0\ \wedge\ \#J^+=\#J^-$.

### D1.5

bound $:=$ closed self-contained chain (content: fermionic); transit $:=$ propagating open chain (content: bosonic); $\ \Delta S=\mathsf E_{\mathrm{bd}}+\mathsf E_{\mathrm{tr}}$; $\ \mathsf E_{\mathrm{bd}}:=\Delta S_{\mathrm{bound}}$; $\ \mathsf E_{\mathrm{tr}}:=\Delta S_{\mathrm{transit}}$.

### D1.6

$ds^2(e):=g_{\mu\nu}(e)\,\Delta x^\mu_e\,\Delta x^\nu_e$ [$g_{\mu\nu}:$ D2.1]; $\ \widehat{ds}^{\,2}(e):=ds^2(e)/\mathfrak h^2$.

### D1.7

$\Theta(\gamma):=\sum_{e\in\gamma}\widehat{ds}^{\,2}(e)$; $\ \Phi(\gamma):=\sum_{e\in\gamma}\alpha_e\,\widehat{ds}^{\,2}(e)$ [$\alpha_e\in\Phi:$ per-edge phase, D3.5; uniform-phase case: $\Phi=\alpha\,\Theta$]; $\ \operatorname{Hol}_{\mathrm{spiral}}(\gamma):=e^{i\Phi(\gamma)}$; $\ \gamma\in\mathsf{Trivial}\iff\forall e\in\gamma:\ \widehat{ds}^{\,2}(e)=0$; wrapping $\iff$ spatial hop projection has winding $\ne0$ around a closed ledger cycle.

### D1.8

$\tau_n:=\sum\delta\tau$ accumulated along a causal chain of real edges; emergent coordinate $x^0:=\tau_n$.

### D1.9

tick locality: $\ \operatorname{dom}\bigl(\mathrm{tick}(v)\bigr)\subseteq\{v\}\cup\{e\in E:\ e\ni v\}$, pre- and post-tick data only; $\neg\exists$ read at edge-distance $>1$.

### D1.10

node force: $\ \mathbf F\!\restriction_v$ resolves local information content into channels {bound, transit, holonomy, charge, flux}; {bound, transit} $:=$ entropy channels [D1.5]; {holonomy, charge, flux} $:=$ registration data [D1.1] $\cup$ transition amplitude [D3.3].

### D1.11

accessible information content at $v$ $\leftrightarrow n(v)$; content beyond the capacity bound (CT0.11): $\neg$accessible [D4.1].

### D1.12

$\mathcal A(n):=\{$aspects of $\mathbf F$ acting nontrivially at rung $n\}$; value derived (CT0.13), $\neg$ stipulated.

### D2.1

sector coefficients [basis: CT1.2]: $\ X_{(+)}=a_{00}E_0+q_{ij}E^{ij}$, $q_{ij}=q_{ji}$; $\ X_{(-)}=w_iW_i$;
$$
\Sigma_{\mathrm{tr}}:=\delta^{ij}q_{ij};\quad
\hat h_{ij}:=q_{ij}-\tfrac13\delta_{ij}\Sigma_{\mathrm{tr}};\quad
h:=\tfrac13\Sigma_{\mathrm{tr}};\quad
N_i:=\beta w_i;\quad
\Omega:=e^{\alpha_\Omega a_{00}};\quad
\alpha_\Omega,\beta,\varkappa\in\mathbb R;
$$
$$
\bar g_{00}:=-1;\quad
\bar g_{0i}:=\varkappa N_i;\quad
\bar g_{ij}:=\delta_{ij}+\varkappa\bigl(\hat h_{ij}+\tfrac13\delta_{ij}\Sigma_{\mathrm{tr}}\bigr);\quad
g_{\mu\nu}:=\Omega^2\,\bar g_{\mu\nu}.
$$

### D2.2

$\Upsilon:=\ln\Omega$; $\ \Upsilon_\mu:=\bar\nabla_\mu\Upsilon$.

### D2.3

$\mathcal K:$ aspect space; $\ \mathcal K^{(A)}:$ block of aspect $A$; $\ \mathcal K_n:=\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}$; $\ \mathcal P_M^{(n)}:\mathcal K\to\mathcal K_n:$ orthogonal projection.

### D2.4

$Z(\mathcal R,n):=\bigl\langle\mathrm{out}\bigl|(1-\mathbf F_M^{(n)})^{-1}\bigr|\mathrm{in}\bigr\rangle$; poles of $Z(\mathcal R,n):=$ rung-$n$ spectrum; residues $:=$ amplitudes.

### D2.5

massless $\iff$ resolvent pole at $k^2=0$; massive $\iff$ pole at $k^2=m^2>0$; $m^2:=$ pole displacement.

### D2.6

$\omega:$ orientation-reversal involution: $s(c)\leftrightarrow t(c)$; chirality $\mapsto-$chirality; charge $\mapsto-$charge.

### D2.7

$\Theta_{\mathfrak L}:$ ledger reflection: reverses ledger order; $J^+\leftrightarrow J^-$; $G(e)\mapsto G(e)^\ast$.

### D2.8

convergence sheet: $1\mapsto1+i\varepsilon$, $\ \varepsilon\to0^+$, for $\forall$ resolvents and configuration sums.

### D2.9

units $:=$ powers of $\mathfrak q$; $\ c=\hbar=k_B=1$; $\ [\mathfrak h]=\mathfrak q^{-1/2}$; $\ \mathfrak h:=$ single free scale; $\ \kappa,\ G_N:$ names for combinations of $\mathfrak h$ (CT2.9), $\neg$ independent inputs.

### D2.11

valid universe $\iff$ real-edge network closed $\ \wedge\ \#J^+=\#J^-$ [D1.3] $\ \wedge\ \in\operatorname{Im}($active mask$)$ $\ \wedge\ \neg\exists$ dangling ledger boundary beyond the sealed Janus boundary.

### D2.12

Aspect realization (slot$\to$aspect bridge): $\iota_n:\mathfrak u(n)\to\mathcal K$ — linear realization of the rung-$n$ slot algebra in aspect space, with $\iota_n\bigl(Z(\mathfrak u(2))\bigr)$ spanning $\mathcal K^{(\mathrm{EM})}$ ($n=2$) and $\iota_n\bigl(\mathfrak{su}(3)\bigr)$ spanning $\mathcal K^{(\mathrm{strong})}$ ($n=3$), per the derivation of CT0.13. Slot algebras and pair algebras remain distinct objects (F header); D3.2 “already realized at rung $m$” $:=$ the abstract isomorphism class lies in $\iota_m(\mathfrak u(m))$ or in the pair blocks of CT0.12. **Realization domain:** exactly $n\le3$ — for $n\ge4$ no aspect realization exists [CT4.4a]; the silence of this definition at $n\ge4$ is a non-existence consequence, not an underdetermination.

### D2.13

Subnetwork and microstate space *(scope clauses)*. $\Sigma\subseteq U$ [D2.11] $:=$ a finite connected vertex set together with its interior edges; $\partial\Sigma:=$ edges with exactly one endpoint in $\Sigma$. $\mathcal M(\Sigma):=$ valid microscopic configurations on $\Sigma$: restrictions $C|_\Sigma$ of valid ambient configurations $C$ [D2.11], carrying edge signs $\sigma_e$ [D0.5, CT0.9], geometric data $\widehat{ds}^{\,2}(e)$ [D1.6], seal data [D1.2] and vertex types [A7, D0.8] — subject to the rung masks [CT0.14, CT2.2] and Janus balance [D1.3], $\neg$ to colour sealing (sealing is ambient-global [CT3.18]; the completeness filter acts downstream: CT3.22a Rmk). $|\Sigma|:=\#\{\text{real edges touching}\ \Sigma\}$ (interior $+$ boundary).

### D2.14

Colour boundary and the contraction-completeness projector. $\mathrm{Colour}(U):=\{u\in\mathcal Q:\ u\ \text{carries a colour attachment}\ [\mathrm{D3.8}]\}$; for valid $C$, $\pi_C(v)\subseteq\mathrm{Colour}(U):=$ the other members of the elementary invariant contraction group of $v$ under $C$ (one for a meson pair via $\delta^i{}_j$; two for a (anti)baryon triple via $\varepsilon_{ijk}/\varepsilon^{ijk}$ [CT3.17]); $\pi_C$ is total on $\mathrm{Colour}(U)$ for valid $C$ [CT3.18 $+$ D2.11 applied to the colour ledger]. For $\Sigma$ [D2.13]: $\mathrm{Colour}(\Sigma):=\mathrm{Colour}(U)\cap\Sigma$;
$$\partial_{\mathrm{col}}(\Sigma;C):=\{v\in\mathrm{Colour}(\Sigma):\ \pi_C(v)\not\subseteq\Sigma\};\qquad
\mathcal C(\Sigma;C):=\begin{cases}1&\partial_{\mathrm{col}}(\Sigma;C)=\varnothing\\ 0&\text{otherwise}\end{cases};\qquad
\Pi_{\mathcal C}(\Sigma;C):=\mathcal C(\Sigma;C)\cdot\mathbb I^{(\mathrm{strong})}_\Sigma$$
(Hermitian scalar idempotent on the colour slot space of $\Sigma$ [D3.1]; matches the mask pattern $\mathcal P_M^{(n)}$ [CT0.14]).

### D3.1

$\mathcal H^{(n)}_{\mathrm{slot}}:=\operatorname{span}_{\mathbb C}\{|1\rangle,\dots,|n\rangle\}\cong\mathbb C^{n}$; $n=3$: slot index $i\in\{1,2,3\}$ $:=$ colour.

### D3.2

subset principle: strictly new at rung $n$ $:=$ part of the rung-$n$ structure $\neg$realized at any $m<n$.

### D3.3

at $v$ of type $(1,1)$, edge signs $\sigma_{\leftarrow}(v),\sigma_{\rightarrow}(v)$:
$$
f_v:=\frac{\sigma_{\rightarrow}(v)-\sigma_{\leftarrow}(v)}{2}\in\{-1,0,+1\};\qquad
\aleph_v:=|f_v|;\qquad
\aleph(\sigma,C):=\sum_{v\in C}\aleph_v .
$$

### D3.4

$q_{\mathrm{EM}}(c):=\dfrac{\sigma_{s(c)}-\sigma_{t(c)}}{2}$ (oriented chain $c$). Closed chains: the basepoint core read $q_{\mathrm{core}}$ is defined, ternary, and charge-conjugation odd [EM.9a].

### D3.5

$G^{(n)}(e):=\sigma_e\,\exp\!\bigl(i\,\alpha_e\,\widehat{ds}^{\,2}(e)\bigr)$ [D0.5, D1.6]; $\ \alpha_e\in\Phi:$ per-edge dynamic phase $=\alpha_{pq}$ for $e=(p,q)$ — the A4 branch index (read in Part 2 §E: Def-EM.20, EM.20, forward pointer); dimensionless; the same alphabet at every rung. $\ \alpha_{\mathrm{EM}}^{(n)}:$ EM-block spectral read at rung $n$ (EM.17, forward pointer).

### D3.6

$\mathcal J(C):=\prod_{J^+\in C}(+1)\cdot\prod_{J^-\in C}(+1)^\ast$ $\ \implies\ \mathcal J(\Theta_{\mathfrak L}C)=\mathcal J(C)^\ast$.

### D3.7

photon $:=$ trivial chain [D1.7] $\subseteq V_2$; $\ $gluon $:=$ trivial chain $\cap\,V_3\ne\varnothing$.

### D3.8

colour triplet $q^i$: one fundamental slot index; colour antitriplet $r_i$: one dual slot index; quark $:=$ bound (fermionic) loop with a triplet attachment.

### D3.9

baryon $B:=\varepsilon_{ijk}\,q^iq^jq^k$; $\ $meson $M:=\delta^i{}_j\,q^jr_i$. [Disambiguation: $M$ here $\ne$ total mask $M_\oplus$ of A9.]

### D3.10

$W^\pm:=\tfrac1{\sqrt2}\bigl(W_1\mp iW_2\bigr)$; $\ Z:=\cos\theta_W\,W_3-\sin\theta_W\,Y$; $\ A:=\sin\theta_W\,W_3+\cos\theta_W\,Y$ [$\theta_W:$ EW.24].

### D4.1

$F_{D^-}=\bigoplus_{n\ge4}F_n$ [A8]: single possibility space receiving $\forall$ configurations with rung $n\ge4$.

### D4.2

$D^-$ absorbs information at rate $\propto O(n)$ [D0.9]; absorbed $\implies$ locked $:=$ retained in $\mathfrak L$, $\neg$accessible [D1.11].

### D4.3

$F_{D^+}=\Lambda\,\mathbb I$ [A8]: uniform scalar aspect; $\neg$configuration-dependent.

### P1

$\forall$ quantities of the corpus: derived from A1–A9 $\wedge$ C1–C12 $\wedge$ D0.1–D4.3, except the hop length $\mathfrak h$; $[\mathfrak h]=\mathfrak q^{-1/2}$; $\mathfrak h$ fixes the absolute scale.

### P2

Derived, zero freedom:
$$
(\dim\mathcal E_{++},\dim\mathcal E_{+-},\dim\mathcal E_{-+},\dim\mathcal E_{--})=(7,3,3,3);\quad
C_{\mathrm{cap}}=16;\quad
D_{\mathrm{tick}}(n)=2^{n+1};\quad
n_{\max}=3;
$$
$$
N_{\text{colour}}=3;\quad
N_{\text{gluon}}=8;\quad
N_{\gamma\text{-pol}}=2;\quad
q_{\mathrm{EM}}\in\{-1,0,+1\};\quad
\alpha_e\in\{0,\pi\}\ \text{per edge};
$$
$$
m_W=m_Z\cos\theta_W;\quad
e=g\sin\theta_W;\quad
S=n_{\mathcal R}\ln2;\quad
w_{D^+}=-1 .
$$

**Audit note.** Every entry of this list is re-verified from first principles in exact arithmetic: `checks/verify_merge_tierB.py` §F (totals and cross-references; the identity-level checks live in `verify_B.py`–`verify_G.py`).

### P3

Named combinations of $\mathfrak h$ (external comparison only; $\neg$ inputs):
$$
G_N=\frac{\mathfrak h^2}{4\ln2};\qquad
\kappa^2=8\pi G_N=\frac{2\pi\,\mathfrak h^2}{\ln2}\qquad[\mathrm{CT2.9}].
$$

### P4

Free internal configuration parameters ($\neg$ constants of the theory). Independent core: $g,\ g';\ h_0;\ c_W;\ \Lambda;\ \varkappa,\ \beta,\ \alpha_\Omega$. Functionally dependent members (properties of a solution, $\neg$ further freedom): $\theta_W(g,g')$ [EW.24]; $e(g,g')$ [EW.35]; $\mu_\star^2(c_W,\varkappa,\beta,h_0)$ [EW.33]; $m_W,\ m_Z$ [EW.20, EW.23]; $m_H$ [EW.27]. Predictions $:=$ dimensionless ratios among derived quantities at fixed core data.

### P5

$\neg\exists$ quantity identified with a measured external constant. Comparison procedure: fix $\mathfrak h$ once; read P2 $\wedge$ P3; result $:=$ test of A9, $\neg$ input to A1–A8.
**Era-extension note.** The P4 core lists the bosonic-era free internal parameters (Part 2 loci). The fermion-era parameters (the Janus rate ratio $r=x_+/x_-$; the defect residues $\hat\mu^2$, $\hat\mu'^2$; the Ansatz-B formal temperature $\alpha$; the channel scales $\mu$, $\mu_\nu$; the formal fugacities) are registered in Part 3 §Cal-F under this policy; the baryomesonic era introduces none (Part 4 §Cal-BM). The former declared-choice registry is fully dispositioned: HistLog §I.3.

### CT0.1 — Real/virtual dichotomy

**Thm.** $\ \forall(p,q)\in\mathcal Q\times\mathcal Q:\quad\bigl[(p,q)\in\mathcal R\bigr]\ \underline\vee\ \bigl[(p,q)\in\mathcal V\bigr].$

### CT0.2 — Global vacuum

**Thm.** $\ n_{\mathcal R}=0\ \implies\ \forall(p,q):\ \bigl[(p,q)\in\mathcal V\ \wedge\ \rho_{pq}=\rho_\circ=\tfrac14 I\bigr]\ \wedge\ S_{\mathrm{raw}}(\rho_\circ)=\ln4=\max_{\rho}S_{\mathrm{raw}}(\rho),$ with $\arg\max=\{\tfrac14 I\}$.

### CT0.3 — Seal increments

**Thm.** $\ J^{+}:\ (\Delta n_{\mathcal R},\ \delta h,\ \delta\tau)=(+1,+1,+1);\qquad J^{-}:\ (\Delta n_{\mathcal R},\ \delta h,\ \delta\tau)=(-1,-1,-1).$

### CT0.9 — The edge phase alphabet is binary

**Thm.** $\ \phi_e\in\Phi=\{0,\pi\}\ (\mathrm{mod}\ 2\pi);\qquad\sigma_e=e^{i\phi_e}=(-1)^{\phi_e/\pi}\in\{+1,-1\};\qquad 1\ \text{real edge}=1\ \text{bit}=\ln2\ \text{nats}.$

### CT0.5 — Tick load at rung $n$

**Thm.** $\ D_{\mathrm{tick}}(n)=2^{\,n+1}.$

### CT0.6 — Channel capacity and oversubscription

**Thm.**
$$
C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=16;\qquad
O(n)=\max\bigl(0,\ 2^{\,n+1}-16\bigr);
$$
$$
O(0)=O(1)=O(2)=O(3)=0;\qquad O(4)=16;\qquad O(n)=2^{\,n+1}-16\quad(n\ge4).
$$

**Cor CT0.6a (transit-hop register bound).** Let $\gamma=(e_1,\dots,e_{\delta h})$ be a transit chain [D1.5, D1.4] of distinct directed real edges with hop count $\delta h(\gamma)$ [D0.6] whose entire edge-register content is registered through one pair channel over $\delta\tau(\gamma)$ ledger ticks [A2, D0.7]. Then:
$$
\mathsf E(\gamma)=\delta h(\gamma)\,\ln2\ \ \text{nats}\qquad(\delta h\ \ \text{independent binary registers}\ [\mathrm{CT0.9},\ \mathrm{C9}]);
$$
$$
\text{single-channel supply over}\ \delta\tau\ \text{ticks}:\ \log_2C_{\mathrm{cap}}\cdot\delta\tau=4\,\delta\tau\ \ \text{bits}\qquad[\mathrm{CT0.6}:\ C_{\mathrm{cap}}=16;\ \mathrm{C10}:\ 16\ \text{directions}\iff2^{4}\ \text{alternatives}]
$$
$$
\implies\quad\delta h(\gamma)\ \le\ 4\,\delta\tau(\gamma);\qquad
\mathsf E(\gamma)\ \le\ \min\bigl(\delta h(\gamma),\ 4\,\delta\tau(\gamma)\bigr)\,\ln2\ \ \text{nats}.
$$
A per-tick payload beyond $4$ hop-bits presents $2^{5}=32>16=C_{\mathrm{cap}}$ alternatives at the crossing — oversubscribed [CT0.6]; this is the payload counterpart of CT0.11's vertex-rung admissibility. The bound is sharp: for $\delta h\le4\,\delta\tau$ a schedule of $\delta\tau$ consecutive groups of $\le4$ hops presents $\le2^{4}=16=C_{\mathrm{cap}}$ alternatives per tick — at capacity, no oversubscription [CT0.6]. (Ledger accounting of registered content vs channel supply over a tick window [D0.7]; $\neg$a tick-to-tick transition law.)

### Cor CT0.6a

**Cor CT0.6a (transit-hop register bound).** Let $\gamma=(e_1,\dots,e_{\delta h})$ be a transit chain [D1.5, D1.4] of distinct directed real edges with hop count $\delta h(\gamma)$ [D0.6] whose entire edge-register content is registered through one pair channel over $\delta\tau(\gamma)$ ledger ticks [A2, D0.7]. Then:
$$
\mathsf E(\gamma)=\delta h(\gamma)\,\ln2\ \ \text{nats}\qquad(\delta h\ \ \text{independent binary registers}\ [\mathrm{CT0.9},\ \mathrm{C9}]);
$$
$$
\text{single-channel supply over}\ \delta\tau\ \text{ticks}:\ \log_2C_{\mathrm{cap}}\cdot\delta\tau=4\,\delta\tau\ \ \text{bits}\qquad[\mathrm{CT0.6}:\ C_{\mathrm{cap}}=16;\ \mathrm{C10}:\ 16\ \text{directions}\iff2^{4}\ \text{alternatives}]
$$
$$
\implies\quad\delta h(\gamma)\ \le\ 4\,\delta\tau(\gamma);\qquad
\mathsf E(\gamma)\ \le\ \min\bigl(\delta h(\gamma),\ 4\,\delta\tau(\gamma)\bigr)\,\ln2\ \ \text{nats}.
$$
A per-tick payload beyond $4$ hop-bits presents $2^{5}=32>16=C_{\mathrm{cap}}$ alternatives at the crossing — oversubscribed [CT0.6]; this is the payload counterpart of CT0.11's vertex-rung admissibility. The bound is sharp: for $\delta h\le4\,\delta\tau$ a schedule of $\delta\tau$ consecutive groups of $\le4$ hops presents $\le2^{4}=16=C_{\mathrm{cap}}$ alternatives per tick — at capacity, no oversubscription [CT0.6]. (Ledger accounting of registered content vs channel supply over a tick window [D0.7]; $\neg$a tick-to-tick transition law.)

### CT1.1 — Joint $(S,T)$ decomposition of $\mathfrak H(\mathbb C^4)$

**Thm.** $\ [S,T]=0;$ $\qquad\mathfrak H(\mathbb C^4)=\mathcal E_{++}\oplus\mathcal E_{+-}\oplus\mathcal E_{-+}\oplus\mathcal E_{--};$ $\qquad(\dim\mathcal E_{++},\dim\mathcal E_{+-},\dim\mathcal E_{-+},\dim\mathcal E_{--})=(7,3,3,3);\qquad7+3+3+3=16.$

### CT1.2 — Generator basis and sector assignment

**Thm.** Define
$$
E_0:=\sigma_0\otimes\sigma_0;\qquad
\Sigma:=\textstyle\sum_{i=1}^{3}\sigma_i\otimes\sigma_i;\qquad
W_i:=\tfrac12\bigl(\sigma_0\otimes\sigma_i+\sigma_i\otimes\sigma_0\bigr);
$$
$$
J_i:=\tfrac12\bigl(\sigma_j\otimes\sigma_k-\sigma_k\otimes\sigma_j\bigr)\ [(i,j,k)\ \text{cyclic}];\qquad
K_i:=\tfrac12\bigl(\sigma_0\otimes\sigma_i-\sigma_i\otimes\sigma_0\bigr);\qquad
E^{ij}:=\tfrac12\bigl(\sigma_i\otimes\sigma_j+\sigma_j\otimes\sigma_i\bigr).
$$
Then
$$
\begin{array}{c|c|c|c|c}
\text{generator} & \# & S & T & \text{sector}\\ \hline
E_0 & 1 & + & + & \mathcal E_{++}\\
\Sigma & 1 & + & + & \mathcal E_{++}\\
\hat E^{ij}\ (\text{traceless}) & 5 & + & + & \mathcal E_{++}\\
W_i & 3 & + & - & \mathcal E_{+-}\\
J_i & 3 & - & + & \mathcal E_{-+}\\
K_i & 3 & - & - & \mathcal E_{--}
\end{array}
\qquad 1+1+5+3+3+3=16\implies\text{basis of}\ \mathfrak H(\mathbb C^4);
$$
$$
W_i=\tfrac12\bigl(\sigma_i^{(p)}+\sigma_i^{(q)}\bigr)=\text{total-spin generator}.
$$

### CT0.7 — Reality is the swap grading

**Thm.** Let $\mathbb S\in\mathcal U(\mathcal H_p\otimes\mathcal H_q):\ |a\rangle\otimes|b\rangle\mapsto|b\rangle\otimes|a\rangle$. Then

$$(1)\quad \mathbb S=\tfrac12\bigl(E_0+\Sigma\bigr);\qquad
\Pi_{\mathcal R}:=\Pi_{\vee^2}=\tfrac14\bigl(3E_0+\Sigma\bigr);\qquad
\Pi_{\mathcal V}:=\Pi_{\wedge^2}=\tfrac14\bigl(E_0-\Sigma\bigr);\qquad
\mathfrak T\Pi_{\mathcal R}=3,\ \ \mathfrak T\Pi_{\mathcal V}=1 .
$$

$$(2)\quad \forall X:\ S(X)=\mathbb S X\mathbb S .
$$

$$(3)\quad SX=X\implies[\mathbb S,X]=0\implies X(\vee^2)\subseteq\vee^2\ \wedge\ X(\wedge^2)\subseteq\wedge^2;
$$
$$
SX=-X\implies\{\mathbb S,X\}=0\implies X(\vee^2)\subseteq\wedge^2\ \wedge\ X(\wedge^2)\subseteq\vee^2;
$$
$$
\underbrace{\dim_{\mathbb R}\mathfrak H(\vee^2)+\dim_{\mathbb R}\mathfrak H(\wedge^2)}_{9+1=10}\ \oplus\ \underbrace{2\dim_{\mathbb C}\operatorname{Hom}(\wedge^2,\vee^2)}_{2\cdot3=6}\ =\ 16 .
$$

$$(4)\quad \mathbf F_{(+,\mathcal R)}=\mathcal E_{++};\quad
\mathbf F_{(-,\mathcal R)}=\mathcal E_{+-};\quad
\mathbf F_{(+,\mathcal V)}=\mathcal E_{-+};\quad
\mathbf F_{(-,\mathcal V)}=\mathcal E_{--}
$$
(first label of $\mathbf F_{(\pm,\cdot)}$: $T$-parity; second label: $S$-parity, $\mathcal R\leftrightarrow+$, $\mathcal V\leftrightarrow-$); $\ F_{J^+}=\mathcal E_{-+}=\operatorname{span}\{J_i\}$, $\ F_{J^-}=\mathcal E_{--}=\operatorname{span}\{K_i\}$: the $S$-odd blocks.

**Cor CT0.7a (spin content).** $\ \sum_iW_i^2=\tfrac32E_0+\tfrac12\Sigma$; $\ \sum_iW_i^2\big|_{\vee^2}=2=1(1{+}1)$; $\ \sum_iW_i^2\big|_{\wedge^2}=0=0(0{+}1)$; i.e. $\vee^2$: spin $1$, $\wedge^2$: spin $0$.

### Cor CT0.7a

**Cor CT0.7a (spin content).** $\ \sum_iW_i^2=\tfrac32E_0+\tfrac12\Sigma$; $\ \sum_iW_i^2\big|_{\vee^2}=2=1(1{+}1)$; $\ \sum_iW_i^2\big|_{\wedge^2}=0=0(0{+}1)$; i.e. $\vee^2$: spin $1$, $\wedge^2$: spin $0$.

### CT0.8 — Admissible range of the crystallization threshold

**Thm.** $\ \bigl[\mathrm{A4}\wedge\mathrm{A5}\wedge\mathrm{D0.1}\ \text{consistent}\bigr]\implies 0\le\varepsilon_q<\tfrac14;$ $\ \ $in particular $\varepsilon_q<1-\varepsilon_q$ (A4's two branches are disjoint); $\qquad\varepsilon_q=0\implies\bigl[(p,q)\in\mathcal R\iff\operatorname{supp}\rho_{pq}\subseteq\vee^2\ \ \vee\ \ \rho_{pq}=\Pi_{\mathcal V}\bigr]$ (branch reads $\alpha_{pq}=0\ /\ \pi$ [A4]); and $\forall$ theorems of the corpus: A4 enters only via CT0.1 (valid $\forall\varepsilon_q\in[0,1]$) and CT0.2 (valid $\iff\varepsilon_q\in[0,\tfrac14)$).

### CT0.10 — The two sign structures are independent

**Thm.** With $\ P(C):=\prod_{e\in E(C)}\sigma_e\ $ and $\ \pi(C):=(-1)^{\aleph(\sigma,C)}$ :
$$
\neg\bigl[P(C)\ \text{determines}\ \pi(C)\bigr]\ \wedge\ \neg\bigl[\pi(C)\ \text{determines}\ P(C)\bigr];\qquad
L\ge4:\ \ (P,\pi)\twoheadrightarrow\{\pm1\}^2;
$$
$$
\Longrightarrow\quad w(C)=\mathcal J(C)\prod_{e\in E(C)}G(e)\cdot(-1)^{\aleph(\sigma,C)}\ \ [\mathrm{A8}]\ \text{double-counts no edge-sign data}.
$$

### CT0.11 — Maximal accessible rung

**Thm.** $\ \text{channel-admissible}(v)\iff D_{\mathrm{tick}}\bigl(n(v)\bigr)\le C_{\mathrm{cap}}\iff n(v)\le3;$ accessible vertex sets $=\{V_0,V_1,V_2,V_3\}$ (types $\{\Xi_0,\dots,\Xi_3\}$); $D_{\mathrm{tick}}(3)=C_{\mathrm{cap}}$ (saturation); $\forall v:\ n(v)\ge4\implies O\bigl(n(v)\bigr)>0\implies F_{D^-}$ [D4.1].

**Cor CT0.11a (three slots).** $\ \max\{\mathcal H^{(n)}_{\mathrm{slot}}:\ \text{admissible}\}=\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3;\qquad 3=\lfloor\log_2 C_{\mathrm{cap}}\rfloor-1=\lfloor\log_216\rfloor-1;$ i.e. $N_{\text{colour}}=3$ is derived, not chosen.

**Cor CT0.11b (directed rung of bidirectional skeletons).** A channel $\{p,q\}$, $p\ne q$, is *bidirectional* when both orientations are real: $(p,q)\in\mathcal R\ \wedge\ (q,p)\in\mathcal R$ [A4]. Let $S$ be a finite real-edge subgraph whose every used channel is bidirectional, and $d_S(v):=\#\{\text{channels of}\ S\ \text{incident on}\ v\}$. Then:
$$
n(v)\ \ge\ 2\,d_S(v)\qquad[\text{each bidirectional channel adds}\ 1\ \text{to}\ \partial^{\leftarrow}\ \text{and}\ 1\ \text{to}\ \partial^{\rightarrow}\ \text{at each endpoint}]
$$
$$
S\ \text{exhausts the real edges at}\ v\implies n(v)=2\,d_S(v);\qquad
d_S(v)\ge2\implies n(v)\ge4\implies D_{\mathrm{tick}}(n)=2^{n+1}\ge32>16\implies O\bigl(n(v)\bigr)>0\implies F_{D^-}\ [\mathrm{D4.1}]
$$
$$
\text{unoversubscribed}\iff n(v)\le3\ [\mathrm{CT0.6}]:\qquad\text{bidirectional}\ S:\ d_S(v)\le1\ (n\in\{0,2\});\qquad\text{mixed}:\ n(v)=2\,d^{\mathrm{bi}}_S(v)+d^{\mathrm{uni}}_S(v)\le3 .
$$

### Cor CT0.11b

**Cor CT0.11b (directed rung of bidirectional skeletons).** A channel $\{p,q\}$, $p\ne q$, is *bidirectional* when both orientations are real: $(p,q)\in\mathcal R\ \wedge\ (q,p)\in\mathcal R$ [A4]. Let $S$ be a finite real-edge subgraph whose every used channel is bidirectional, and $d_S(v):=\#\{\text{channels of}\ S\ \text{incident on}\ v\}$. Then:
$$
n(v)\ \ge\ 2\,d_S(v)\qquad[\text{each bidirectional channel adds}\ 1\ \text{to}\ \partial^{\leftarrow}\ \text{and}\ 1\ \text{to}\ \partial^{\rightarrow}\ \text{at each endpoint}]
$$
$$
S\ \text{exhausts the real edges at}\ v\implies n(v)=2\,d_S(v);\qquad
d_S(v)\ge2\implies n(v)\ge4\implies D_{\mathrm{tick}}(n)=2^{n+1}\ge32>16\implies O\bigl(n(v)\bigr)>0\implies F_{D^-}\ [\mathrm{D4.1}]
$$
$$
\text{unoversubscribed}\iff n(v)\le3\ [\mathrm{CT0.6}]:\qquad\text{bidirectional}\ S:\ d_S(v)\le1\ (n\in\{0,2\});\qquad\text{mixed}:\ n(v)=2\,d^{\mathrm{bi}}_S(v)+d^{\mathrm{uni}}_S(v)\le3 .
$$

### CT0.12 — Aspect–capacity match

**Thm.**
$$
\begin{array}{c|c|c}
\text{aspect} & \text{block} & \dim_{\mathbb R}\\ \hline
F_{J^+} & \mathcal E_{-+}=\operatorname{span}\{J_i\} & 3\\
F_{J^-} & \mathcal E_{--}=\operatorname{span}\{K_i\} & 3\\
F_G & \operatorname{span}\{\hat E^{ij}\}\ (\text{traceless}) & 5\\
F_W & \mathcal E_{+-}=\operatorname{span}\{W_i\} & 3\\
F_H & \operatorname{span}\{\Sigma\} & 1\\
F_{D^+} & \operatorname{span}\{E_0\} & 1\\ \hline
\text{total} & \mathfrak H(\mathbb C^4) & 16=C_{\mathrm{cap}}
\end{array}
$$

### CT1.4 — The $W_i$ close $\mathfrak{su}(2)$

**Thm.** $\ [W_i,W_j]=i\,\epsilon_{ijk}W_k;\qquad\operatorname{span}_{\mathbb R}\{W_i\}\cong\mathfrak{su}(2)\ [\mathrm{C2}].$

### CT1.3 — Centrality of the identity

**Thm.** $\ \forall X\in\mathfrak H(\mathbb C^4):\quad[E_0,X]=0.$

### CT1.5 — Commutators of $\Sigma$ with $J_i$, $K_i$, $W_i$

**Thm.** $\ [\Sigma,J_i]=4i\,K_i;\qquad[\Sigma,K_i]=-4i\,J_i;\qquad[\Sigma,W_i]=0.$

### CT1.8 — Action of $W_i$ on $J_j$ and $K_j$

**Thm.** $\ [W_i,J_j]=i\,\epsilon_{ijk}J_k;\qquad[W_i,K_j]=i\,\epsilon_{ijk}K_k;$ i.e. $\{J_i\}$, $\{K_i\}$: $SO(3)$ vectors under $\operatorname{span}\{W_i\}$.

### CT1.10 — $SO(3)$ decomposition of $\mathcal E_{++}$

**Thm.** Under $\operatorname{span}\{W_i\}$:
$$
\mathcal E_{++}\ \longrightarrow\ \mathbf 1\oplus\mathbf 5\oplus\mathbf 1\qquad(7=1+5+1);
$$
$$
E_0:\ \mathbf 1;\qquad\Sigma:\ \mathbf 1;\qquad
\hat E^{ij}:=E^{ij}-\tfrac13\delta^{ij}\Sigma:\ \mathbf 5\ (\text{spin }2),\quad\delta_{ij}\hat E^{ij}=0 .
$$

### CT0.13 — Aspect activation and the active sets

**Thm.**
$$
\mathcal A(0)=\{J\};\qquad
\mathcal A(1)=\{J,\,G,\,W,\,H,\,D^+\};\qquad
\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\};
$$
$$
\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\};\qquad
\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\};
$$
with $J:=\{J^+,J^-\}$ and $W:=F_W=F_{W^+}\oplus F_{W^-}\oplus F_Z$ [C8]; $\ \neg\exists$ independent aspect named $Z$ at any rung: neutral seed $W_3\in F_W$; physical $Z$: D3.10, EW.24.

### CT3.2 — Quantum slot space

**Thm.**
$$
|\psi\rangle=\alpha_1|1\rangle+\alpha_2|2\rangle+\alpha_3|3\rangle,\ \ \alpha_i\in\mathbb C;\qquad
\langle\psi|\phi\rangle=\textstyle\sum_i\alpha_i^\ast\beta_i;\qquad
\textstyle\sum_i|\alpha_i|^2=1;
$$
$$
\mathcal H^{(3)}_{\mathrm{slot}}=\operatorname{span}_{\mathbb C}\{|1\rangle,|2\rangle,|3\rangle\}\cong\mathbb C^3 .
$$

### CT3.1 — Classical trivalent symmetry

**Thm.** Trivalent vertex with distinguishable slots $\{s_1,s_2,s_3\}$:
$$
\text{relabeling symmetry}=\operatorname{Sym}\{s_1,s_2,s_3\}=S_3;\qquad
|S_3|=3!=6;\qquad
S_3=\{e,(12),(13),(23),(123),(132)\}.
$$

### CT3.3 — Classical permutations embed unitarily

**Thm.** $P_\pi|i\rangle:=|\pi(i)\rangle$, $\ (P_\pi)^i{}_j=\delta^i_{\pi(j)}$. Then
$$
P_\pi^\dagger P_\pi=I_3\implies P_\pi\in U(3);\qquad
P_\pi P_\rho=P_{\pi\circ\rho}\ \ (\text{homomorphism});\qquad
P_\pi=I_3\iff\pi=e\ \ (\text{faithful});\qquad
S_3\hookrightarrow U(3).
$$

### CT3.4 — Probability preservation gives $U(3)$

**Thm.**
$$
\bigl\{L\ \text{linear}:\ \langle L\psi,L\phi\rangle=\langle\psi,\phi\rangle\ \ \forall\psi,\phi\bigr\}
=\bigl\{L:\ L^\dagger L=I_3\bigr\}=U(3);\qquad
S_3\subseteq U(3)\ [\mathrm{CT3.3}].
$$

### CT3.5 — The algebra $\mathfrak u(3)$ and its decomposition

**Thm.** [C2]
$$
\mathfrak u(3)=\{X\in M_3(\mathbb C):\ X^\dagger=X\};\qquad
\mathfrak u(3)=\mathfrak{su}(3)\oplus\mathfrak u(1);
$$
$$
\mathfrak{su}(3)=\{X\in\mathfrak u(3):\ \mathfrak T(X)=0\};\qquad
\mathfrak u(1)=\operatorname{span}_{\mathbb R}\{I_3\};\qquad
[\mathfrak{su}(3),\mathfrak u(1)]=0\ \ (\text{commuting ideals});
$$
$$
\forall X\ \exists!\ (X_0,c):\ X=X_0+cI_3,\ \ \mathfrak T(X_0)=0,\ \ c=\tfrac{\mathfrak T(X)}{3}.
$$

### CT3.8 — Dimension of the colour algebra

**Thm.** $\ \dim_{\mathbb R}\mathfrak u(3)=3+3\cdot2=9;\qquad\mathfrak T(X)=0:\ 1\ \text{nontrivial real constraint}\ (\mathfrak T(I_3)=3\ne0);\qquad\dim_{\mathbb R}\mathfrak{su}(3)=9-1=8=3^2-1.$

### CT0.14 — Mask flag and block dimensions

**Thm.**
$$
\mathcal K_0\subset\mathcal K_1\subset\mathcal K_2\subset\mathcal K_3\subset\mathcal K_{n\ge4}\quad(\text{strict});\qquad
\dim\mathcal K_0=6,\ \ \dim\mathcal K_1=16,\ \ \dim\mathcal K_2=17,\ \ \dim\mathcal K_3=25;
$$
$$
\bigl(\mathcal P_M^{(n)}\bigr)^2=\mathcal P_M^{(n)}=\bigl(\mathcal P_M^{(n)}\bigr)^\dagger;\qquad
\mathfrak T\,\mathcal P_M^{(n)}=\dim\mathcal K_n;\qquad
\dim\mathcal K^{(\mathrm{EM})}=1,\ \ \dim\mathcal K^{(\mathrm{strong})}=8 .
$$

### CT1.6 — Commutators $[J_i,J_j]$ and $[K_i,K_j]$

**Thm.** $\ [J_i,J_j]=i\,\epsilon_{ijk}W_k;\qquad[K_i,K_j]=i\,\epsilon_{ijk}W_k.$

### CT1.7 — Mixed commutators $[J_i,K_j]$

**Thm.**
$$
[J_i,K_j]=i\bigl(\delta_{ij}\Sigma-E^{ij}\bigr)=\tfrac i2\Bigl(2\delta_{ij}\Sigma-\sigma_i\otimes\sigma_j-\sigma_j\otimes\sigma_i\Bigr);
$$
$$
[J_i,K_i]=i\!\!\sum_{k\ne i}\!\!\sigma_k\otimes\sigma_k;\qquad
[J_i,K_j]=-iE^{ij}=-\tfrac i2\bigl(\sigma_i\otimes\sigma_j+\sigma_j\otimes\sigma_i\bigr)\ \ (i\ne j);
$$
$$
[J_i,K_j]\in(\mathcal E_{++})_{\mathrm{sym\ spatial}};\qquad [J_i,K_j]\notin\operatorname{span}\{W_k\}.
$$

### CT1.9 — Sector closure table and the global algebra

**Thm.**
$$
\begin{array}{c|c}
\text{bracket} & \text{closes in}\\ \hline
[W_i,W_j] & \operatorname{span}\{W_k\}=\mathcal E_{+-}\\
[W_i,J_j] & \operatorname{span}\{J_k\}=\mathcal E_{-+}\\
[W_i,K_j] & \operatorname{span}\{K_k\}=\mathcal E_{--}\\
[J_i,J_j] & \operatorname{span}\{W_k\}\\
[K_i,K_j] & \operatorname{span}\{W_k\}\\
[J_i,K_j] & (\mathcal E_{++})_{\mathrm{sym\ spatial}}\\
[\Sigma,J_i] & \operatorname{span}\{K_i\}\\
[\Sigma,K_i] & \operatorname{span}\{J_i\}\\
[\Sigma,W_i] & 0\\
[E_0,X] & 0\ \ \forall X
\end{array}
$$
$$
\bigl(\mathfrak H(\mathbb C^4),\ (X,Y)\mapsto-i[X,Y]\bigr)\cong\mathfrak u(4)\ [\mathrm{C2}];\qquad
Z\bigl(\mathfrak u(4)\bigr)=\operatorname{span}_{\mathbb R}\{E_0\};
$$
$$
\mathfrak{su}(4)=\operatorname{span}_{\mathbb R}\bigl\{\Sigma,\ \hat E^{ij},\ W_i,\ J_i,\ K_i\bigr\};\qquad
\dim_{\mathbb R}\mathfrak{su}(4)=1+5+3+3+3=15 .
$$

### CT1.11 — The two scalars are distinct

**Thm.** $\ E_0\in Z\bigl(\mathfrak H(\mathbb C^4)\bigr);\qquad\Sigma\notin Z\bigl(\mathfrak H(\mathbb C^4)\bigr);\qquad\forall c\in\mathbb R\setminus\{0\}:\ E_0\ne c\,\Sigma;$ hence the A8 assignment $E_0\mapsto F_{D^+}$, $\Sigma\mapsto F_H$ [CT0.12] is well-defined and non-degenerate.

### CT2.2 — The rung mask is a projection

**Thm.**
$$
\bigl(\mathcal P_M^{(n)}\bigr)^2=\mathcal P_M^{(n)}=\bigl(\mathcal P_M^{(n)}\bigr)^\dagger;\qquad
\operatorname{Im}\mathcal P_M^{(n)}=\mathcal K_n;\qquad
\mathfrak T\,\mathcal P_M^{(n)}=\dim\mathcal K_n\in\{6,16,17,25,\dots\}.
$$

### CT2.8 — Reflection positivity and Hilbert-space closure

**Thm.** With $\ \langle A|B\rangle:=Z\bigl[\Theta_{\mathfrak L}A\cup B\bigr]\ $ on $\mathfrak C(\mathcal R)$ [D0.10]:
$$
(1)\ \ w(\Theta_{\mathfrak L}C)=w(C)^\ast;\qquad
(2)\ \ w(C)=w(C_{\mathrm{left}})\cdot w(C_{\mathrm{right}})\ \ \text{across any interior ledger-time cut};
$$
$$
(3)\ \ \langle A|A\rangle=\sum_C|w(C)|^2\ \ge\ 0;\qquad
(4)\ \ \langle A|A\rangle=0\iff A\ \text{mask-excluded}\ \ (\text{null space}=\text{mask-excluded configurations});
$$
$$
(5)\ \ \text{quotient}\wedge\text{completion}=\text{Hilbert space};\qquad
(6)\ \ Z\big|_{\text{reflected pair}}=\|\cdot\|^2,\ \ \text{convergent on the}\ \mathrm{D2.8}\ \text{sheet}.
$$

### EM.9 — Chain end-charge

**Thm.** [D3.4]
$$
q_{\mathrm{EM}}(c)=\frac{\sigma_{s(c)}-\sigma_{t(c)}}{2}\in\{-1,0,+1\};\qquad
\text{all three values attained};\qquad
\begin{array}{c|cccc}
(\sigma_s,\sigma_t) & (+,+) & (+,-) & (-,+) & (-,-)\\ \hline
q_{\mathrm{EM}} & 0 & +1 & -1 & 0
\end{array}
$$

**Cor EM.9b (chain-wall telescoping).** Let $c=(e_1,\dots,e_k)$, $k\ge2$, be an oriented chain of distinct real edges [D1.4] with interior vertices $v_1,\dots,v_{k-1}$, $v_i:=t(e_i)=s(e_{i+1})$, each of type $(1,1)$ [A7, D0.8] — the chain's two edges are $v_i$'s only incident real edges. Then the D3.3 vertex reads telescope:
$$
\sum_{i=1}^{k-1}f_{v_i}\ =\ \tfrac12\bigl(\sigma_{e_k}-\sigma_{e_1}\bigr)\ =\ -\,q_{\mathrm{EM}}(c)
\qquad\bigl[\sigma_{s(c)}=\sigma_{e_1},\ \ \sigma_{t(c)}=\sigma_{e_k}:\ \mathrm{D3.4}/\mathrm{EM.9}\ \text{end registers}\bigr]
$$
— the total interior vertex activity of a chain is carried by its two end registers alone. In particular:
$$
\sum_{i=1}^{k-1}f_{v_i}=0\iff\sigma_{e_1}=\sigma_{e_k}\iff q_{\mathrm{EM}}(c)=0;\qquad
\sum_{i=1}^{k-1}\aleph_{v_i}=\#\{i:\ \sigma_{e_{i+1}}\ne\sigma_{e_i}\}\le k-1\qquad[\mathrm{D3.3}:\ \aleph_v=|f_v|;\ \mathrm{CT0.9}].
$$

### CT1.11a — The involution table of the four sectors

**Thm.** $(0)$ **Dictionary.** A8's four sectors are CT1.1's blocks under the identification
$$
\mathbf F_{(+,\mathcal R)}=F_G\oplus F_H\oplus F_{D^+}\ (5{+}1{+}1)\ \leftrightarrow\ \mathcal E_{++};\qquad
\mathbf F_{(-,\mathcal R)}=F_{W^+}\oplus F_{W^-}\oplus F_Z\ (3)\ \leftrightarrow\ \mathcal E_{+-};
$$
$$
\mathbf F_{(+,\mathcal V)}=F_{J^+}\ (3)\ \leftrightarrow\ \mathcal E_{-+};\qquad
\mathbf F_{(-,\mathcal V)}=F_{J^-}\ (3)\ \leftrightarrow\ \mathcal E_{--}
$$
— first label $=$ the $T$-grading ($\eta^\mu\eta^\nu$ [A3]), $\mathcal R/\mathcal V=$ the $S$-grading (reality is the swap grading [CT0.7]); machine-verified on CT1.2's generator table (17 generators: $E_0,\Sigma,\hat E^{ij}{\times}5,W_i,J_i,K_i$).
$(1)$ **Status of the two gradings.** $S=\operatorname{Ad}(\mathbb S)$ with $\mathbb S=\tfrac12(E_0+\Sigma)$ [CT0.7(1)] — an *inner algebra automorphism* ($\mathbb S^2=\mathbb S$? no: $\mathbb S$ unitary involution, machine). $T$ is a *pure grading*: the diagonal $\pm1$-map $\sigma_\mu\otimes\sigma_\nu\mapsto\eta^\mu\eta^\nu\,\sigma_\mu\otimes\sigma_\nu$ [A3] — $\neg$ multiplicative (witness: $T(\sigma_0\otimes\sigma_1)\,T(\sigma_0\otimes\sigma_2)=(-1)(-1)\sigma_0\otimes(\sigma_1\sigma_2)\ne T(\sigma_0\otimes\sigma_1\sigma_2)$-type failure, machine), hence $\neg$ inner. $[S,T]=0$ on all 16 basis elements [CT1.1]; the grading group on $\mathfrak H(\mathbb C^4)$ is $\mathbb Z_2\times\mathbb Z_2$ with simultaneous eigenspaces $\mathcal E_{st}$, $\dim=(7,3,3,3)$.
$(2)$ **Table of the declared reversals.** With $\omega$ [D2.6] and $\Theta_{\mathfrak L}$ [D2.7]:
$$
\begin{array}{c|cccc|c}
& \mathbf F_{(+,\mathcal R)} & \mathbf F_{(-,\mathcal R)} & \mathbf F_{(+,\mathcal V)} & \mathbf F_{(-,\mathcal V)} & \text{edge/chain data}\\ \hline
S=\operatorname{Ad}(\mathbb S) & + & + & - & - & \text{reality grading [CT0.7]}\\
T\ (\text{grading}) & + & - & + & - & \eta^\mu\eta^\nu\ [\mathrm{A3}]\\
\omega & \text{fixed} & W^+\!\leftrightarrow\!W^-;\ Z\ \text{fixed} & \neg\text{declared} & \neg\text{declared} & s(c)\leftrightarrow t(c);\ \text{charge}\mapsto-\text{charge [D2.6, EM.9];}\ \omega^2=1;\ R\mapsto R^{\mathrm T};\ \omega\notin\operatorname{Aut}(\Gamma),\ |V|\ge3\\
\Theta_{\mathfrak L} & \text{fixed} & \text{fixed} & \leftrightarrow & \leftrightarrow & \text{ledger order}\mapsto\text{reverse};\ J^+\leftrightarrow J^-;\ G(e)\mapsto G(e)^*\ (\alpha_e\widehat{ds}^{\,2}(e)\mapsto-\alpha_e\widehat{ds}^{\,2}(e),\ \sigma_e\ \text{fixed [D3.5]});\ \mathcal J\mapsto\mathcal J^*\ \text{[D3.6]};\ w\mapsto w^*\ \text{[CT2.8(1)]};\ \Theta^2=1\\
\omega\Theta_{\mathfrak L} & \text{fixed} & W^+\!\leftrightarrow\!W^- & \leftrightarrow & \leftrightarrow & \text{the fourth class}
\end{array}
$$
$\omega$ acts on the edge set, $\Theta_{\mathfrak L}$ on phase/ledger order — disjoint data $\Rightarrow$ they commute, and $\langle\omega,\Theta_{\mathfrak L}\rangle\cong\mathbb Z_2\times\mathbb Z_2$ with classes $(1,\omega,\Theta_{\mathfrak L},\omega\Theta_{\mathfrak L})$; $\omega$ is charge-odd [D2.6; covariance of the closed-core charge read: EM.9a], $\Theta_{\mathfrak L}$ phase-odd and charge-even [D2.7, D3.5, D3.6].
$(3)$ **Edge-class answer (the sector question at edge level).** Real edges split into $\sigma_e=\pm1$ [CT0.9: $\Phi=\{0,\pi\}$]; virtual edges carry $\neg$registration [A5, A7, D0.5: $\phi_e$ defined on $E_{\mathcal R}$ only] — a proposed $(\pm,\mathcal V)$ split has no read: the virtual class is single and ungraded (weight $1$, no phase). The two sign structures ($\sigma$ vs $(-1)^{\aleph}$) are independent [CT0.10].
$(4)$ **[READING] rows (recorded, $\neg$adopted).** External CPT vocabulary maps as: $C\leftrightarrow\omega$ (the charge-odd reversal [D2.6]; sign-level realization $\sigma_e\mapsto-\sigma_e$: EM.24(1) — **E**, forward pointer); $T\leftrightarrow\Theta_{\mathfrak L}$ (ledger-time reversal [D2.7] — $\neg$ anti-unitary: no anti-unitary operator is declared; conjugation acts on weights/phases [CT2.8(1), D3.6]); $P\leftrightarrow$ the alignment-pattern reversal $\mathcal P\mapsto E_{\mathcal R}\setminus\mathcal P$ (equivalently $\alpha_e\mapsto\pi-\alpha_e$) with the mirror classification of Def-EM.21/Def-EM.22, EM.23 — **E**, forward pointers: a pattern-level reversal on configuration data (spacetime parity as a Lorentzian field-algebra read has count $0$ in Parts 1–2; the orientation read $\chi=\operatorname{sign}(k)$ remains [CANDIDATE], not adopted); "CPT" $\leftrightarrow$ the derived composition $C\circ P\circ T$ on $\mathfrak C(\mathcal R)$ with unconditional $|w|^2$-invariance [EM.24(4)–(5) — **E**, forward pointer]; at the involution-table level its reversal part is the $\omega\Theta_{\mathfrak L}$ class of $(2)$. This is the exact amount of reversal structure the axioms declare — $\neg$ a Lorentzian CPT theorem (no Lorentzian field algebra, no spinor bundle in the inventory).

### L1 — The Lyapunov function of the pair state

**Thm.** Faithful pair states $\rho$ [A1: $\rho\in\mathfrak H(\mathbb C^4)$, $\rho\succeq0$, $\mathfrak T\rho=1$, $\operatorname{spec}\rho\subset(0,1]$]; with
$$
\delta\rho:=\rho-\tfrac14I\ \ [\mathrm{A5}:\ \rho_\circ=\tfrac14I];\qquad
\mu:=\operatorname{spec}(\delta\rho)\subset\bigl[-\tfrac14,\tfrac34\bigr];\qquad
\textstyle\sum_i\mu_i=0\ \ [\mathfrak T\rho=1];
$$
$$
\gamma:=1-4\varepsilon_q\in(0,1]\ \ [\mathrm{D0.3};\ \mathrm{A4},\ \mathrm{D0.4},\ \mathrm{CT0.8}];
$$
$$
K:=-\log\rho;\qquad
\tilde K:=K-\mathfrak T(K\rho)\,I\ \ [\mathrm{D0.3}];\qquad
V(\tilde K):=\mathfrak T\bigl(\tilde K^2\bigr)\ \ge0;
$$
$(1)$ **Zero locus.** $V=0\iff\tilde K=0\iff\rho=\tfrac14I$ — the A5 vacuum.
$(2)$ **Tick invariance.** $V\bigl(\tilde K(\mathcal T(\rho))\bigr)=V\bigl(\tilde K(\rho)\bigr)$ for every draw [A6: $\mathcal T(\rho)=U\rho U^\dagger$].
$(3)$ **Decay identity ($\gamma$-dependent).** Under the Gibbs tilt $\rho':=\tilde{\mathcal T}_\gamma(\rho)$ [D0.3], with $V':=V\bigl(\tilde K(\rho')\bigr)$:
$$
V'-V=-\gamma\sum_i\phi_\gamma(\mu_i)+O(\delta\rho^4);\qquad
\phi_\gamma(x):=2x\log(1+4x)-\gamma x^2;
$$
$$
\text{leading}:\ \ V'-V=-\gamma(8-\gamma)\textstyle\sum_i\mu_i^2+O(\delta\rho^3);\qquad
\gamma=1:\ \ V'-V=-\textstyle\sum_i\phi(\mu_i)+O(\delta\rho^4),\ \ \phi:=\phi_1 .
$$
$(4)$ **$\phi_\gamma$-calculus.** $\phi_\gamma(0)=\phi_\gamma'(0)=0$; $\ \phi_\gamma=\phi_1+(1-\gamma)x^2$;
$$
\phi_\gamma''(x)=\frac{14+16x-32x^2}{(1+4x)^2}+2(1-\gamma)\quad[\text{exact rational identity}];
$$
$$
\phi_\gamma\ \text{convex on}\ W_\gamma\supseteq W:=\Bigl[\tfrac{1-2\sqrt2}{4},\tfrac{1+2\sqrt2}{4}\Bigr]\supseteq\bigl[-\tfrac14,\tfrac34\bigr]\quad\forall\gamma\in(0,1];\qquad
\phi_\gamma>0\ \ \text{on}\ \ \bigl[-\tfrac14,\tfrac34\bigr]\setminus\{0\}.
$$
$(5)$ **Monotonicity.** Jensen: $\ \sum_i\phi_\gamma(\mu_i)\ \ge\ 4\,\phi_\gamma\bigl(\tfrac14\sum_i\mu_i\bigr)=0\ $; hence, on the faithful simplex, for every $\gamma\in(0,1]$:
$$
V'\le V,\qquad V'=V\iff\tilde K=0\iff\rho=\tfrac14I .
$$

### L2 — The temporal decay law

**Thm.** Under L1's setting, per tilt step [D0.3; L1(3)], to exact leading order:
$$
V'-V=-\Bigl[1-\bigl(1-\tfrac\gamma4\bigr)^{2}\Bigr]V+O(\delta\rho^3)=-\frac{\gamma(8-\gamma)}{16}\,V+O(\delta\rho^3);\qquad
V'=\bigl(1-\tfrac\gamma4\bigr)^{2}V+O(\delta\rho^3);
$$
$$
\gamma=1:\ \ V'-V=-\tfrac7{16}\,V+O(\delta\rho^3),\ \ V'=\tfrac9{16}V+O(\delta\rho^3);\qquad
\gamma\to0:\ \ V'=V\ \ (\text{identity-tilt limit});
$$
$$
\mu'=\bigl(1-\tfrac\gamma4\bigr)\mu+O(\mu^2)\quad[\text{eigenvalue contraction}];\qquad
\gamma=1:\ \ \mu'=\tfrac34\mu;\qquad
1-\bigl(1-\tfrac\gamma4\bigr)^2=\frac{\gamma(8-\gamma)}{16}\ \ [\text{exact rationals}].
$$

### L0 — The ledger–tilt coupling

**Thm.** *Dynamical scope (declared at use — the crystallization–tilt coupling; CT4.5a precedent: A4–A7 declare the criterion, the tick and the ledger, $\neg$ a state update at the seal):* every A4 crystallization event applies exactly one Gibbs tilt step [D0.3] to the pair state of that event. Under A5 ($\rho_\circ=\tfrac14I$), A6 ($\mathcal T(\rho)=U\rho U^\dagger$, $U\sim\mu_\star$; $|\mathfrak L(\tau_{n+1})|=|\mathfrak L(\tau_n)|+n_{\mathrm{real\_out}}(\tau_n)$), A7 ($\mathfrak L=\bigcup_{n\ge0}\mathfrak L(\tau_n)$, $|\mathfrak L(\tau_n)|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k)$), D0.3/D0.4 ($\gamma:=1-4\varepsilon_q$), CT0.8:
$(1)$ **Tick preserves $V$.** $\ V\bigl(\tilde K(\mathcal T(\rho))\bigr)=V\bigl(\tilde K(\rho)\bigr)$ for every draw [A6; L1(2)].
$(2)$ **Events apply the tilt.** At tick $\tau_n$ the A4 criterion selects $n_{\mathrm{real\_out}}(\tau_n)$ edges into the ledger [A6]; under the declared scope each selection maps its pair state
$$
\rho\ \longmapsto\ \tilde{\mathcal T}_\gamma(\rho)=\frac{\rho\,e^{-\gamma\rho}}{\mathfrak T(\rho\,e^{-\gamma\rho})},\qquad
\gamma=1-4\varepsilon_q\in(0,1]\quad[\mathrm{D0.3};\ \mathrm{CT0.8}];
$$
$Z_\gamma>0$ on faithful $\rho$ [Cor L0a] $\implies\tilde{\mathcal T}_\gamma(\rho)$ faithful, $\succeq0$, $\mathfrak T=1$ [D0.3]; $\ \tilde{\mathcal T}_\gamma\ne\mathcal T$ [D0.3].
$(3)$ **Tilt contracts $V$.** $\ V'\le V$, equality iff $\rho=\tfrac14I$ [A5; L1(5)].
$(4)$ **Ledger counts tilt steps.** $\#\{\text{tilt steps at }\tau_n\}=n_{\mathrm{real\_out}}(\tau_n)$; cumulative count $|\mathfrak L(\tau_n)|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k)$ [A6, A7 — exact integer recursion]. On one pair channel with $k$ events interleaved with arbitrary draws, the $V$-sequence is that of $\tilde{\mathcal T}_\gamma^{k}(\rho_0)$ — the interleaving is spectrally inert by $(1)$; per fixed $k$: $\ \mu_k=\bigl(1-\tfrac\gamma4\bigr)^{k}\mu_0+O(\mu_0^2)$ [L2, iterated].
$(5)$ **Contraction is the ledger dynamics.** The deficits of L1–L3 are realized once per ledger increment: the deficit fraction per tilt step is $\tfrac{\gamma(8-\gamma)}{16}$ of $V$ to exact leading order [L2], accumulating as $V\mapsto\bigl(1-\tfrac\gamma4\bigr)^{2k}V+O(\delta\rho_0^3)$ after $k$ recorded events; the inertial read $m_i^2(q)=\Delta S(q)$ [L3(4)] is the deficit read per increment.

**Cor L0a (tilt modular update).** Faithful $\rho$, $K:=-\log\rho$ [D0.3], $K':=K\bigl(\tilde{\mathcal T}_\gamma(\rho)\bigr)$, $Z_\gamma:=\mathfrak T(\rho\,e^{-\gamma\rho})$:
$$
K'=K+\gamma\rho+\log Z_\gamma\cdot I;\qquad
Z_\gamma\in(0,\,e^{-\gamma/4}];\qquad
\mathfrak T(K'-K)=\gamma+4\log Z_\gamma\le0,
$$
with equality iff $\rho=\tfrac14I$; $\ \gamma=1:\ Z_1\le e^{-1/4}$, $\ \mathfrak T(K'-K)=1+4\log Z_1\le0$.

### Cor L0a

**Cor L0a (tilt modular update).** Faithful $\rho$, $K:=-\log\rho$ [D0.3], $K':=K\bigl(\tilde{\mathcal T}_\gamma(\rho)\bigr)$, $Z_\gamma:=\mathfrak T(\rho\,e^{-\gamma\rho})$:
$$
K'=K+\gamma\rho+\log Z_\gamma\cdot I;\qquad
Z_\gamma\in(0,\,e^{-\gamma/4}];\qquad
\mathfrak T(K'-K)=\gamma+4\log Z_\gamma\le0,
$$
with equality iff $\rho=\tfrac14I$; $\ \gamma=1:\ Z_1\le e^{-1/4}$, $\ \mathfrak T(K'-K)=1+4\log Z_1\le0$.

### L3 — Entropy deficit and the inertial mass reading

**Thm.** Under L1, L2:
$(1)$ **Entropy deficit.** With $\delta\rho=\tfrac14\sum_ar_aG_a$ on the Pauli-tensor basis $\{G_a\}=\{\sigma_\mu\otimes\sigma_\nu\}_{(\mu,\nu)\ne(0,0)}$ [C1; $\mathfrak T(G_aG_b)=4\delta_{ab}$: CT1.1], $|\delta\rho|^2:=\mathfrak T(\delta\rho^2)$:
$$
\Delta S_{\mathrm{pair}}:=2\,|\delta\rho|^2=\tfrac12\,|r|^2;\qquad
S\bigl(\rho\,\big\|\,\tfrac14I\bigr)=\Delta S_{\mathrm{pair}}+O(\delta\rho^3)\qquad\bigl[S(\rho\|\sigma):=\mathfrak T\bigl(\rho(\log\rho-\log\sigma)\bigr)\bigr]
$$
$(2)$ **Lyapunov identification.** $\ \tilde K=-4\,\delta\rho+O(\delta\rho^2);\qquad V(\tilde K)=16\,|\delta\rho|^2+O(\delta\rho^3)=8\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3).$
$(3)$ **Deficit decay ($\gamma$-dependent).** $\ V'-V=-\dfrac{\gamma(8-\gamma)}{2}\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3);\qquad\gamma=1:\ \ V'-V=-\tfrac72\,\Delta S_{\mathrm{pair}}+O(\delta\rho^3).$
$(4)$ **Inertial read.** $\ m_i^2(q):=\Delta S(q)\quad[\Delta S(q):\ \text{the patch deficit, L4};\ \text{dimensionless, nats};\ \neg\text{a particle identification}].$

### L4 — The patch entropy deficit

**Thm.** Vertex $q$ of finite incidence (theorem-local scope); incident pair channels $\{(q,p)\}$ [A1]; $n(q)=\partial^{\leftarrow}(q)+\partial^{\rightarrow}(q)$ [D0.8]; $n_{\mathcal R}(q)$ [A4]; $n_{\mathcal V}(q):=n(q)-n_{\mathcal R}(q)$ [D0.1]. Patch deficit:
$$
\Delta S(q)\ :=\ \sum_{(q,p)\in\mathcal V}S\bigl(\rho_{qp}\,\big\|\,\tfrac14I\bigr)
\qquad[\text{sum over the virtual incident channels of}\ q;\ \ S(\cdot\|\cdot)\ \text{as in L3}(1)]
$$
$(1)$ **Channel sum.** $\ \Delta S(q)=\sum_{(q,p)\in\mathcal V}\Delta S_{\mathrm{pair}}(pq)+O(\delta\rho^3)=2\sum_{(q,p)\in\mathcal V}|\delta\rho_{pq}|^2+O(\delta\rho^3)$ [L3(1) per channel].
$(2)$ **Mean form.** For $n_{\mathcal V}(q)\ge1$, with $\langle\Delta S_{\mathrm{pair}}\rangle_q:=\frac1{n_{\mathcal V}(q)}\sum_{(q,p)\in\mathcal V}\Delta S_{\mathrm{pair}}(pq)$:
$$
\Delta S(q)\ =\ n_{\mathcal V}(q)\,\langle\Delta S_{\mathrm{pair}}\rangle_q+O(\delta\rho^3)\ =\ 2\,n_{\mathcal V}(q)\,\langle|\delta\rho|^2\rangle_q+O(\delta\rho^3)\ =\ \tfrac12\,n_{\mathcal V}(q)\,\langle|r|^2\rangle_q+O(\delta\rho^3);
$$
$n_{\mathcal V}(q)=0\implies\Delta S(q)=0$ [empty sum].
$(3)$ **Patch Lyapunov read.** $\ V_{\mathrm{patch}}(q):=\sum_{(q,p)\in\mathcal V}V(\tilde K_{pq})=8\,\Delta S(q)+O(\delta\rho^3)$; under per-channel tilt steps [D0.3]: $\ V_{\mathrm{patch}}'-V_{\mathrm{patch}}=-\frac{\gamma(8-\gamma)}2\,\Delta S(q)+O(\delta\rho^3)$ [L3(2), (3) summed].
$(4)$ **Inertial read, grounded.** $\ m_i^2(q)=\Delta S(q)$ [L3(4)] $=2\,n_{\mathcal V}(q)\,\langle|\delta\rho|^2\rangle_q+O(\delta\rho^3)$ — an integer multiplicity $n_{\mathcal V}(q)\in\mathbb Z_{\ge0}$ times the mean channel deficit; the read vanishes to leading order iff $n_{\mathcal V}(q)=0$ or every virtual-channel deviation vanishes.

### L5 — The second-order sector flow of the tilt

**Thm.** Under L1's setting, with $c:=1-\tfrac\gamma4$, $\ d:=\tfrac{\gamma(8-\gamma)}8$ [exact rationals in $\gamma$; L2]:
$(1)$ **Quadratic flow.** With $\delta\rho':=\tilde{\mathcal T}_\gamma(\rho)-\tfrac14I$ [D0.3]:
$$
\delta\rho'\ =\ c\,\delta\rho\ -\ d\,\Bigl(\delta\rho^2-\tfrac14|\delta\rho|^2E_0\Bigr)\ +\ O(\delta\rho^3);\qquad
\mathfrak T\Bigl(\delta\rho^2-\tfrac14|\delta\rho|^2E_0\Bigr)=0;\qquad
\delta\rho^2\succeq0 .
$$
$(2)$ **Single-sector landing.** $\delta\rho\in\mathcal E_{st}$ (a single $(S,T)$ sector [C3; CT1.2]) $\implies S(\delta\rho^2)=\delta\rho^2\ \wedge\ T(\delta\rho^2)=\delta\rho^2:\ \delta\rho^2\in\mathcal E_{++}$; the traceless part lies in $\operatorname{span}\{\Sigma,\hat E^{ij}\}$ [CT1.2, CT1.10]; the square channel of $\mathcal E_{++}$ closes in $\mathcal E_{++}$ — the quadratic transport inside the real block is one-directional.
$(3)$ **Partition function.** $\ \log Z_\gamma=-\tfrac\gamma4-d\,|\delta\rho|^2+O(\delta\rho^3)=-\tfrac\gamma4-\tfrac{\gamma(8-\gamma)}{16}\Delta S_{\mathrm{pair}}+O(\delta\rho^3)$ [Cor L0a; L3(1)]; $\ \gamma=1:\ \log Z_1=-\tfrac14-\tfrac78|\delta\rho|^2=-\tfrac14-\tfrac7{16}\Delta S_{\mathrm{pair}}+O(\delta\rho^3)$.
$(4)$ **Modular trace deficit.** $\ \mathfrak T(K'-K)=\gamma+4\log Z_\gamma$ [Cor L0a] $=-4d\,|\delta\rho|^2+O(\delta\rho^3)=-\tfrac{\gamma(8-\gamma)}4\Delta S_{\mathrm{pair}}+O(\delta\rho^3)\le0$ near the vacuum; $\ \gamma=1:\ -\tfrac74\Delta S_{\mathrm{pair}}+O(\delta\rho^3)$.
$(5)$ **Sharp-crystallization table ($\gamma=1$).** $\ c=\tfrac34;\quad d=\tfrac78;\quad1-c^2=\tfrac7{16}\ [\mathrm{L2}];\quad\tfrac d2=\tfrac7{16};\quad2d=\tfrac72\quad[\text{exact rationals}]$.

### CT1.12 — Metric emergence from sector components

**Thm.** With D2.1 data $\bigl(a_{00},q_{ij},w_i\bigr)\in\mathcal E_{++}\oplus\mathcal E_{+-}$:
$$
\delta^{ij}\hat h_{ij}=0;\qquad \Omega=e^{\alpha_\Omega a_{00}}>0\ \ \forall a_{00}\in\mathbb R;\qquad
\bar g_{ij}\succ0\iff\forall a:\ 1+\varkappa\lambda_a(q)>0\quad(\Leftarrow\ \varkappa>0\wedge\varkappa\|q\|_{\mathrm{op}}<1);
$$
$$
\bar g_{ij}\succ0\implies\operatorname{sig}(\bar g_{\mu\nu})=\operatorname{sig}(g_{\mu\nu})=(-,+,+,+);
$$
$$
\begin{array}{c|c|c}
\text{sector object} & \# & \text{metric role}\\ \hline
a_{00} & 1 & \text{conformal factor}\ \Omega\\
\Sigma_{\mathrm{tr}} & 1 & \text{spatial volume mode}\\
\hat h_{ij} & 5 & \text{spin-2 shear}\\
w_i & 3 & \text{shift}\ N_i=\beta w_i\\ \hline
\text{total} & 10 & \#\{g_{\mu\nu}=g_{\nu\mu}\}=\tfrac{4\cdot5}{2}
\end{array}
$$

### CT1.13 — Christoffel symbols under conformal rescaling

**Thm.** $\ g_{\mu\nu}=\Omega^2\bar g_{\mu\nu},\ \Upsilon=\ln\Omega\implies$
$$
g^{\mu\nu}=\Omega^{-2}\bar g^{\mu\nu};\qquad
\Gamma^\lambda{}_{\mu\nu}=\bar\Gamma^\lambda{}_{\mu\nu}+\delta^\lambda{}_\mu\bar\nabla_\nu\Upsilon+\delta^\lambda{}_\nu\bar\nabla_\mu\Upsilon-\bar g_{\mu\nu}\bar g^{\lambda\rho}\bar\nabla_\rho\Upsilon .
$$

### CT1.14 — Riemann tensor under conformal rescaling

**Thm.** With $\ C^\rho{}_{\mu\nu}:=\Gamma^\rho{}_{\mu\nu}-\bar\Gamma^\rho{}_{\mu\nu}=\delta^\rho{}_\mu\Upsilon_\nu+\delta^\rho{}_\nu\Upsilon_\mu-\bar g_{\mu\nu}\Upsilon^\rho$ (tensor; $\Upsilon^\rho:=\bar g^{\rho\sigma}\Upsilon_\sigma$):
$$
R^\rho{}_{\sigma\mu\nu}=\bar R^\rho{}_{\sigma\mu\nu}+2\bar\nabla_{[\mu}C^\rho{}_{\nu]\sigma}+2C^\rho{}_{[\mu|\lambda|}C^\lambda{}_{\nu]\sigma}.
$$

### CT2.1 — Unit and dimension conventions

**Thm.** With $c=\hbar=k_B=1$, $[\mathfrak h]=\mathfrak q^{-1/2}$:
$$
[\text{length}]=\mathfrak q^{-1/2};\quad[\text{area}]=\mathfrak q^{-1};\quad[\text{energy}]=\mathfrak q^{+1/2};\quad[T_{\mu\nu}]=\mathfrak q^{+2};\quad[G_{\mu\nu}]=[\Lambda]=\mathfrak q^{+1};\quad[\kappa^2]=[G_N]=\mathfrak q^{-1};\quad[\kappa]=\mathfrak q^{-1/2};\quad[S_{\mathrm{geom}}]=\mathfrak q^{0},
$$
and every equation of Parts III–IV balances.

### CT2.3 — Masked force operator

**Thm.** $\ \mathbf F_M^{(n)}:=\mathcal P_M^{(n)}\mathbf F\,\mathcal P_M^{(n)}$ satisfies
$$
\mathbf F_M^{(n)}\big|_{\mathcal K_n^\perp}=0;\qquad
\mathbf F_M^{(n)}(\mathcal K)\subseteq\mathcal K_n;\qquad
\mathbf F^\dagger=\mathbf F\implies\bigl(\mathbf F_M^{(n)}\bigr)^\dagger=\mathbf F_M^{(n)}.
$$

### CT2.4 — Force restriction by rung

**Thm.**
$$
\mathbf F_M^{(n)}=\bigoplus_{A\in\mathcal A(n)}F_A\big|_{\mathcal K^{(A)}},\qquad
\mathcal A(n)\ \text{as in CT0.13};\qquad
\neg\exists\ \text{independent aspect}\ Z\ \text{at any rung}\ (W_3\ \text{seed}\in F_W)\ [\mathrm{C8}].
$$

### CT2.5 — Masked resolvent as spectrum generator

**Thm.** $\ \mathbf F_M^{(n)}=\sum_a\lambda_aP_a$ (spectral decomposition; $P_aP_b=\delta_{ab}P_a$, $P_a^\dagger=P_a$). Then
$$
Z(\mathcal R,n)=\Bigl\langle\mathrm{out}\Bigl|(1-\mathbf F_M^{(n)})^{-1}\Bigr|\mathrm{in}\Bigr\rangle=\sum_a\frac{\langle\mathrm{out}|P_a|\mathrm{in}\rangle}{1-\lambda_a};
$$
$$
\text{poles}\iff1\in\operatorname{spec}\mathbf F_M^{(n)};\qquad
\operatorname*{Res}_{\lambda_a\to1}=-\langle\mathrm{out}|P_a|\mathrm{in}\rangle=\text{transition amplitude};\qquad
\mathrm{D2.8}:\ 1\mapsto1+i\varepsilon\ \text{selects the branch}.
$$

### CT2.6 — Continuum manifold closure

**Thm.** Conditions: (i) valid universe [D2.11] — a definitional precondition (D2.11’s own definition in application, “there is something”), $\neg$ an extra-axiomatic hypothesis [A §0.2a]; (ii) coarse-graining cells contain unboundedly many real edges as $\mathfrak h\to0$ — reclassified as derived (Part 4, Tier BM.24: the ledger's own unbounded ladder witnesses it [BM.151(1), forward pointer]); (iii) sector coefficient fields [D2.1] of bounded variation across neighbouring cells — reclassified as derived (Part 4, Tier BM.24: the spectral bound $|r_a|\le\sqrt3$ with convex averaging [BM.151(2), forward pointer]). Then
$$
M:=\Gamma_{\mathcal R}/\!\!\sim\ \ \text{is a smooth 4-manifold};\qquad
\chi([v])=(x^0,x^1,x^2,x^3)=(\tau_n,h_1,h_2,h_3)\ \ \text{charts};
$$
$$
\text{transition maps}=\text{smooth diffeomorphisms};\qquad
g_{\mu\nu}\ [\mathrm{CT1.12}]=\text{smooth Lorentzian metric on}\ M;\qquad
\text{nondegeneracy}\iff\varkappa\|q\|_{\mathrm{op}}<1 .
$$

### CT2.7 — Exact geometric action closure

**Thm.** Under the hypotheses of CT2.6:
$$
S_{\mathrm{geom}}[g]=\frac{1}{2\kappa^2}\int d^4x\,\sqrt{-g}\,\bigl(R-2\Lambda\bigr);\qquad
\neg\exists\ \text{additional local higher-curvature terms}.
$$

### CT1.19 — Continuum limit at leading order

**Thm.** $L=\mathfrak h\,n_{\mathcal R}$ fixed; $\ \mathfrak h\to0\ \wedge\ n_{\mathcal R}\to\infty\implies$
$$
\sum_{e\in\gamma}ds^2(e)\ \longrightarrow\ \int_\gamma g_{\mu\nu}\,dx^\mu dx^\nu=L\int_0^1g_{\mu\nu}\bigl(x(\lambda)\bigr)\dot x^\mu\dot x^\nu\,d\lambda;\qquad
\text{abs.\ error}=O(\mathfrak hL),\quad\text{rel.\ error}=O(\mathfrak h).
$$

**Cor CT1.19a.** $\ \widehat{ds}^{\,2}(e)=ds^2(e)/\mathfrak h^2:$ dimensionless, $O(1)$ generically; $\ \widehat{ds}^{\,2}(e)=0\iff\Delta x_e\ \text{null}$; trivial chain [D1.7] $=$ all-null-edge chain.

### Cor CT1.19a

**Cor CT1.19a.** $\ \widehat{ds}^{\,2}(e)=ds^2(e)/\mathfrak h^2:$ dimensionless, $O(1)$ generically; $\ \widehat{ds}^{\,2}(e)=0\iff\Delta x_e\ \text{null}$; trivial chain [D1.7] $=$ all-null-edge chain.

### CT1.20 — Effective action from the partition function

**Thm.** $\ Z[g]=\sum_{C:\,g(C)=g}|w(C)|\,e^{i\Phi(C)}$ [$\Phi:$ D1.7+D3.5+parity phases]. Semiclassically ($\delta\Phi\ne0$: pairwise cancellation; $\delta\Phi=0$: dominance):
$$
S_{\mathrm{eff}}[g]:=-i\log Z[g]\ \ (\text{branch}\ [\mathrm{D2.8}]);\qquad
\frac{\delta S_{\mathrm{eff}}}{\delta g^{\mu\nu}}=0\iff\frac{\delta Z}{\delta g^{\mu\nu}}=0\ \ (Z\ne0);\qquad
\text{stationary points dominate}.
$$

### CT1.21 — The geometric part of the effective action

**Thm.** $\ S_{\mathrm{geom}}[g]=\dfrac{1}{2\kappa^2}\displaystyle\int d^4x\,\sqrt{-g}\,(R-2\Lambda).$

### CT1.22 — Stress-energy tensor from the force operator

**Thm.** With $D^+$ removed from $Z_{\mathrm{force}}$ (carried by $\Lambda$ in $S_{\mathrm{geom}}$):
$$
S_{\mathrm{force}}[g]:=-i\log Z_{\mathrm{force}}[g];\qquad
Z_{\mathrm{force}}[g]=\bigl\langle\mathrm{out}\bigl|(1-\mathbf F_M^{(n)})^{-1}\bigr|\mathrm{in}\bigr\rangle;\qquad
T_{\mu\nu}:=-\frac{2}{\sqrt{-g}}\frac{\delta S_{\mathrm{force}}}{\delta g^{\mu\nu}};
$$
$$
T_{\mu\nu}=T^{\mathrm{bd}}_{\mu\nu}+T^{\mathrm{tr}}_{\mu\nu};\qquad
T^{\mathrm{bd}}_{\mu\nu}=(\rho+p)u_\mu u_\nu+p\,g_{\mu\nu};\qquad
T^{\mathrm{tr}}_{\mu\nu}=\sum_a\Bigl(F^{(a)}_{\mu\alpha}F^{(a)\ \alpha}_{\ \ \nu}-\tfrac14g_{\mu\nu}F^{(a)}_{\alpha\beta}F^{(a)\alpha\beta}\Bigr),
$$
the sum over aspects whose leading transit representation is a connection.

### CT1.23 — Field equations

**Thm.**
$$
S_{\mathrm{eff}}=S_{\mathrm{geom}}+S_{\mathrm{force}};\qquad
\delta S_{\mathrm{eff}}=0\iff G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa^2T_{\mu\nu};
$$
$$
\text{dimensions}\ [\mathrm{CT2.1}]:\quad\mathfrak q^{+1}=\mathfrak q^{-1}\cdot\mathfrak q^{+2}=\mathfrak q^{+1};\qquad
\kappa:=\text{coefficient fixed by}\ S_{\mathrm{geom}}\ \text{normalization}.
$$

### CT1.25 — The cosmological constant is the $D^+$ aspect

**Thm.** $\ F_{D^+}=\Lambda\mathbb I\implies T^{(D^+)}_{\mu\nu}=-\dfrac{\Lambda}{\kappa^2}g_{\mu\nu};\qquad\rho_{D^+}=\dfrac{\Lambda}{\kappa^2};\quad p_{D^+}=-\rho_{D^+};\quad w_{D^+}:=\dfrac{p}{\rho}=-1.$

### CT1.29 — Boundary entropy from channel capacity

**Thm.** $\partial\mathcal B:$ closed real-edge surface separating a $D^-$-locked interior. Then
$$
\Omega_{\partial\mathcal B}=2^{\,n_{\mathcal R}(\partial\mathcal B)};\qquad
S_{\partial\mathcal B}=\ln\Omega_{\partial\mathcal B}=n_{\mathcal R}(\partial\mathcal B)\ln2\ \ \text{nats}=n_{\mathcal R}(\partial\mathcal B)\ \ \text{bits};
$$
$$
A:=n_{\mathcal R}(\partial\mathcal B)\,\mathfrak h^2\implies S_{\partial\mathcal B}=\frac{A}{\mathfrak h^2}\ln2 .
$$

### CT2.9 — Calibration closure

**Thm.** $G_N$ defined by $S_{\partial\mathcal B}\overset!=\dfrac{A}{4G_N}$; $\ \kappa$ by the CT1.23 normalization. Then
$$
\mathfrak h^2=4\,G_N\ln2\iff G_N=\frac{\mathfrak h^2}{4\ln2};\qquad
\kappa^2=8\pi G_N=\frac{2\pi\,\mathfrak h^2}{\ln2};\qquad
\frac{A}{4G_N}=\frac{A\ln2}{\mathfrak h^2}=S_{\partial\mathcal B};
$$
$$
[G_N]=[\kappa^2]=\mathfrak q^{-1}\ [\mathrm{CT2.1}];\qquad G_N,\kappa=\text{names for combinations of}\ \mathfrak h\ (\neg\text{independent}).
$$

### CT2.11 — One free scale

**Thm.**
$$
\forall Q\ \text{dimensionful}:\ \ Q=c_Q\,\mathfrak h^{k_Q},\ c_Q\ \text{fixed};\qquad
\forall q\ \text{dimensionless-derived}:\ \ q=\text{fixed number},\ \mathfrak h\text{-free};
$$
$$
\mathfrak h\mapsto\lambda\mathfrak h:\ \ Q\mapsto\lambda^{k_Q}Q,\quad\text{P2 quantities invariant}\implies\text{rescaling}=\text{symmetry}\implies\exists!\ \text{calibration d.o.f.}
$$

### EW.1 — Joint $(S,T)$ sector decomposition

**Thm.** $\equiv$ CT1.1: $\ \mathfrak H(\mathbb C^4)=\mathcal E_{++}\oplus\mathcal E_{+-}\oplus\mathcal E_{-+}\oplus\mathcal E_{--}$, $\ \dim=(7,3,3,3)$.

### EW.2 — Generator basis and sector assignment

**Thm.** $\equiv$ CT1.2: $\ \{E_0,\Sigma,\hat E^{ij}\}\subset\mathcal E_{++}\ (1,1,5);\ \ W_i\in\mathcal E_{+-}\ (3);\ \ J_i\in\mathcal E_{-+}\ (3);\ \ K_i\in\mathcal E_{--}\ (3);\ \ 1{+}1{+}5{+}3{+}3{+}3=16$.

### EW.3 — The $W_i$ close $\mathfrak{su}(2)$

**Thm.** $\equiv$ CT1.4: $\ [W_i,W_j]=i\,\epsilon_{ijk}W_k$; $\ \operatorname{span}_{\mathbb R}\{W_i\}\cong\mathfrak{su}(2)$ [C2].

### EW.4 — Central, trace, and mixed commutators

**Thm.** $\equiv$ CT1.3, CT1.5, CT1.6, CT1.7:
$$
(1)\ [E_0,X]=0\ \ \forall X;\qquad
(2)\ [\Sigma,W_i]=0;\qquad
(3)\ [\Sigma,J_i]=4iK_i,\ \ [\Sigma,K_i]=-4iJ_i;
$$
$$
(4)\ [J_i,J_j]=[K_i,K_j]=i\,\epsilon_{ijk}W_k;\qquad
(5)\ [J_i,K_j]=i\bigl(\delta_{ij}\Sigma-E^{ij}\bigr).
$$

### EW.5 — Second-order Higgs-to-weak pathways

**Thm.**
$$
\bigl[K_j,[\Sigma,J_i]\bigr]=4\,\epsilon_{ijk}W_k;\qquad
\bigl[J_j,[\Sigma,K_i]\bigr]=-4\,\epsilon_{ijk}W_k;
$$
$$
[J_j,K_i]\in\mathcal E_{++}\ \wedge\ \mathcal E_{++}\cap\operatorname{span}\{W_k\}=\{0\}\implies\text{the}\ [J,K]\ \text{pathway}\ \neg\text{reaches the weak sector}.
$$

### EW.6 — Rung masks and active aspect sets

**Thm.** $\equiv$ CT2.2, CT2.3, CT0.13:
$$
\bigl(\mathcal P_M^{(n)}\bigr)^2=\mathcal P_M^{(n)}=\bigl(\mathcal P_M^{(n)}\bigr)^\dagger;\qquad
\mathbf F_M^{(n)}=\mathcal P_M^{(n)}\mathbf F\,\mathcal P_M^{(n)};
$$
$$
\mathcal A(0)=\{J\};\quad
\mathcal A(1)=\{J,G,W,H,D^+\};\quad
\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\};\quad
\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\};\quad
\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}.
$$
$W=\operatorname{span}\{W_1,W_2,W_3\}$: neutral seed $W_3$, $\neg$ independent aspect [C8]; scalar seed $=$ trace mode $h$ of D2.1.

### EW.8 — The electromagnetic generator

**Thm.** The electromagnetic generator $Y$ is one abstract generator with three realizations:
$$
Y_{\mathrm{slot}}:=Z\bigl(\iota_2(\mathfrak u(2))\bigr)\ (1\text{-dim})\ [\mathrm{D2.12},\mathrm{CT0.13}];\qquad
Y_{\mathrm{asp}}:=\mathcal P^{(\mathrm{EM})}:\ \mathcal K\to\mathcal K^{(\mathrm{EM})},\ \ \operatorname{rk}=1,\ \mathfrak T(Y_{\mathrm{asp}})=1\ [\mathrm{D2.3},\mathrm{CT0.14}];
$$
$$
Y_{\mathrm{car}}:=\tfrac12\sigma_0\ \ \text{on}\ \mathcal H_{\mathsf v}\cong\mathbb C^2\ [\mathrm{EW.32}];
$$
$$
[Y_{\mathrm{asp}},\mathbf F_M^{(n)}]=0\ (\text{block-diagonal});\qquad
[Y_{\mathrm{slot}},\mathfrak{su}(2)]=0;\qquad
[Y_{\mathrm{car}},W_i|_{\mathrm{car}}]=0 .
$$

### EW.12 — Metric expansion and the scalar trace mode

**Thm.** With D2.1 data:
$$
\delta^{ij}\hat h_{ij}=0;\qquad q_{ij}=\hat h_{ij}+\delta_{ij}h;\qquad h=\tfrac13\Sigma_{\mathrm{tr}};\qquad
\delta_{ij}h\,E^{ij}=h\sum_{i=1}^3E^{ii}=h\,\Sigma .
$$

### EW.13 — Identification of the scalar mode

**Thm.** The electroweak scalar mode is
$$
H:=h\,\Sigma\qquad(\text{field}\ h;\ \ \text{operator representative}\ h\Sigma),
$$
the noncentral rotation scalar; the central scalar $E_0$ is unavailable (allocated to $F_{D^+}$).

### EW.17 — Rung-3 closed wrapping chains

**Thm.** $\gamma=$ chain [D1.4]; closed $\iff\#J^+=\#J^-\ \wedge\ \partial\gamma=0$; wrapping $=$ nonzero spatial winding around a closed ledger cycle [D1.7]:
$$
\Theta(\gamma)=\sum_{e\in\gamma}\widehat{ds}^{\,2}(e);\qquad
\Phi(\gamma)=\sum_{e\in\gamma}\alpha_e\,\widehat{ds}^{\,2}(e)\ \ [\mathrm{D1.7};\ \text{uniform-phase case:}\ \Phi=\alpha\,\Theta];\qquad
\operatorname{Hol}_{\mathrm{spiral}}(\gamma)=e^{i\Phi(\gamma)} .
$$
$$
\max\{n:\ \exists\ \text{closed wrapping chain at rung}\ n\}=3 .
$$

### EW.18 — Spiral pole condition

**Thm.** Closed wrapping chain materializes as a rung-3 pole $\implies$
$$
\Phi(\gamma)\in2\pi\mathbb Z\qquad\iff\qquad\sum_{e\in\gamma}\alpha_e\,\widehat{ds}^{\,2}(e)=2\pi k,\ \ k\in\mathbb Z\qquad[\Phi:\ \mathrm{D1.7}].
$$

### EW.19 — Mass as pole displacement

**Thm.** $\equiv$ D2.5 (rung-3 context): massless $\iff$ pole at $k^2=0$; massive $\iff$ pole at $k^2=m^2>0$; $m^2:=$ pole displacement of $Z(\mathcal R,3)$ [D2.4].

### EW.32 — The wrapping seed: carrier and normalization

**Thm.** Carrier: $\ \mathcal H_{\mathsf v}\cong\mathbb C^2$ (single qubit). Generator images:
$$
W_i\longmapsto\tfrac12\sigma_i;\qquad Y\longmapsto\tfrac12\sigma_0 ;
$$
$$
\mathfrak T\bigl(\mathcal G_A\mathcal G_B\bigr)=\tfrac12\,\delta_{AB},\quad\mathcal G_A\in\{W_1,W_2,W_3,Y\}\qquad(\text{unique uniform trace normalization});
$$
$$
T_a\,\mathsf v=0\qquad(a=1,\dots,8)\qquad(\text{colour neutrality}).
$$

### EW.33 — The wrapping mass form

**Thm.** With $\ \mathcal G=(gW_1,\ gW_2,\ gW_3,\ g'Y)$, $g,g'>0$:
$$
M^2_{AB}=\mu_\star^2\;\operatorname{Re}\bigl\langle\mathcal G_A\mathsf v,\ \mathcal G_B\mathsf v\bigr\rangle,\qquad
\mu_\star^2=c_W\,\varkappa^2\beta^2h_0^2>0\quad(c_W>0:\ \text{rung-3 residue});
$$
$$
M^2\ \text{real symmetric PSD (Gram)};\qquad
\ker M^2=\Bigl\{c\in\mathbb R^4:\ \Bigl(\textstyle\sum_Ac_A\mathcal G_A\Bigr)\mathsf v=0\Bigr\};\qquad
h_0=0\implies M^2\equiv0 .
$$

### EW.20 — Weak mass generation

**Thm.** $\langle h\rangle=h_0\ne0$; weak frame with $\mathsf v=$ lower weight state of $W_3$ (an $\mathrm{SU}(2)$ basis choice, always available):
$$
W_3\mathsf v=-\tfrac12\mathsf v;\qquad Y\mathsf v=+\tfrac12\mathsf v;
$$
$$
M^2=\frac{\mu_\star^2}{4}
\begin{pmatrix}
g^2&0&0&0\\
0&g^2&0&0\\
0&0&g^2&-gg'\\
0&0&-gg'&g'^2
\end{pmatrix}
\quad\text{in the ordered basis}\ (W_1,W_2,W_3,Y);
$$
$$
m_W^2:=M^2_{11}=M^2_{22}=\frac{\mu_\star^2g^2}{4}=\frac{c_W\,\varkappa^2\beta^2h_0^2\,g^2}{4}>0 .
$$

### EW.22 — The unbroken generator

**Thm.**
$$
\ker M^2=\operatorname{span}\{(0,0,g',g)\}\quad\text{in the basis}\ (W_1,W_2,W_3,Y);\qquad
Q:=W_3+Y;\qquad Q\,\mathsf v=0;
$$
$$
A:=\frac{g'W_3+gY}{\sqrt{g^2+g'^2}}\qquad(\text{normalized kernel direction}).
$$

### EW.23 — The neutral mass matrix

**Thm.** In $(W_3,Y)$:
$$
M^2_{\mathrm{neutral}}=\frac{\mu_\star^2}{4}
\begin{pmatrix}g^2&-gg'\\ -gg'&g'^2\end{pmatrix}
=\frac{\mu_\star^2}{4}\,uu^{\mathsf T},\quad u=(g,-g');
$$
$$
\det=0;\qquad\operatorname{tr}=\frac{\mu_\star^2(g^2+g'^2)}{4}=:m_Z^2;\qquad
\operatorname{spec}=\{0,\ m_Z^2\};\qquad
\text{null}=(g',g);\quad\text{massive}=(g,-g').
$$

### EW.24 — The mixing angle

**Thm.**
$$
\cos\theta_W:=\frac{g}{s};\qquad\sin\theta_W:=\frac{g'}{s};\qquad\tan\theta_W=\frac{g'}{g};\qquad s:=\sqrt{g^2+g'^2};
$$
$$
A=\sin\theta_W\,W_3+\cos\theta_W\,Y;\qquad
Z=\cos\theta_W\,W_3-\sin\theta_W\,Y\qquad[\mathrm{D3.10}];
$$
$$
M^2_{\mathrm{neutral}}\,A=0;\qquad M^2_{\mathrm{neutral}}\,Z=m_Z^2\,Z .
$$

### EW.25 — The photon direction is massless

**Thm.** $\ m_A^2=0$ (pole of $A$ at $k^2=0$).

### EW.26 — Colour modes remain massless at rung 3

**Thm.** Extending $M^2$ over $\mathcal G\cup\{T_a\}_{a=1}^{8}$:
$$
M^2_{aB}=\mu_\star^2\operatorname{Re}\langle T_a\mathsf v,\ \mathcal G_B\mathsf v\rangle=0;\qquad
M^2_{ab}=0;\qquad
\{T_a\}_{a=1}^8\subseteq\ker M^2;\qquad
m_g^2=0 .
$$

### EW.27 — The scalar excitation

**Thm.** $S_{\mathrm{eff}}[h]:=$ CT1.20 action restricted to the trace mode; $h_0:$ nondegenerate stable stationary point. Then
$$
m_H^2:=\left.\frac{\delta^2S_{\mathrm{eff}}}{\delta h^2}\right|_{h=h_0}>0;\qquad
\text{scalar pole at}\ k^2=m_H^2\ \ (\text{simple});\qquad
m_H^2=\text{configuration data}\ [\mathrm{P4}].
$$

### EW.35 — The residual coupling

**Thm.** Neutral connection $\ \mathcal A_{\mathrm{neutral}}=g\,w^3W_3+g'\,y\,Y$; in the mass eigenbasis ($w^3=\sin\theta_W\,\mathsf A+\cos\theta_W\,\mathsf Z$; $y=\cos\theta_W\,\mathsf A-\sin\theta_W\,\mathsf Z$):
$$
\mathsf A\text{-coefficient}=e\,Q;\qquad
e:=\frac{gg'}{\sqrt{g^2+g'^2}}=g\sin\theta_W=g'\cos\theta_W;\qquad
\frac1{e^2}=\frac1{g^2}+\frac1{g'^2}.
$$

### EW.36 — The charge spectrum and its consistency with the chain end-charge

**Thm.**
$$
Q\big|_{\mathcal H_{\mathsf v}}=\tfrac12\sigma_3+\tfrac12\sigma_0=\operatorname{diag}(1,0);\qquad
\operatorname{spec}Q=\{0,+1\};\qquad
\omega\ [\mathrm{D2.6}]:\ \operatorname{spec}\mapsto\{0,-1\};
$$
$$
\text{charge alphabet}=q\in\{-1,0,+1\}=q_{\mathrm{EM}}(c)\ \text{alphabet of D3.4}\ [\mathrm{EM.9}].
$$

**Cor EW.36a.** On the carrier: $Q=W_3+Y$; seed hypercharge $=+\tfrac12$ [EW.20].

### Cor EW.36a

**Cor EW.36a.** On the carrier: $Q=W_3+Y$; seed hypercharge $=+\tfrac12$ [EW.20].

### EM.2 — The electromagnetic generator

**Thm.** [EW.8 realizations]
$$
Y_{\mathrm{asp}}=\mathcal P^{(\mathrm{EM})}:\ \operatorname{rk}=1;\qquad
\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)=\dim\mathcal K^{(\mathrm{EM})}=1;\qquad
[Y_{\mathrm{asp}},\ \text{any block-diagonal operator}]=0;
$$
$$
Y_{\mathrm{car}}=\tfrac12\sigma_0;\qquad[Y_{\mathrm{car}},W_i|_{\mathrm{car}}]=0\ [\mathrm{EW.32}];
$$
$$
\text{mask fact}\ (\neg Y):\quad\mathcal P_M^{(2)}E_0\mathcal P_M^{(2)}=\mathcal P_M^{(2)},\quad\mathfrak T\bigl(\mathcal P_M^{(2)}\bigr)=\dim\mathcal K_2=17\quad(E_0\leftrightarrow F_{D^+}\ [\mathrm{CT0.12}]).
$$

### EM.5 — Photon and gluon as trivial chains

**Thm.** [D1.7, D3.7]
$$
\gamma_{\gamma}\in\mathsf{Trivial}\ \wedge\ \gamma_{\gamma}\subseteq V_2\qquad(\text{photon});\qquad
\gamma_g\in\mathsf{Trivial}\ \wedge\ \gamma_g\cap V_3\ne\varnothing\qquad(\text{gluon});
$$
$$
\forall\gamma\in\mathsf{Trivial}:\ \ \Theta(\gamma)=0\ \wedge\ \operatorname{Hol}_{\mathrm{spiral}}(\gamma)=1;\qquad
V_2\cap V_3=\varnothing;
$$
$$
\text{distinguishing datum}=\text{possibility space only}\ (V_2\ \text{vs}\ V_3\ \text{availability});\qquad\neg\text{bound loops}.
$$

### EM.6 — Photon masslessness

**Thm.** $\ m_\gamma^2=0$, with two independent supports:
$$
(\mathrm{i})\quad A=\sin\theta_W W_3+\cos\theta_W Y\ \text{spans}\ \ker M^2\ [\mathrm{EW.22},\mathrm{EW.24}];
$$
$$
(\mathrm{ii})\quad\gamma_{\gamma}\in\mathsf{Trivial}\subseteq V_2:\ \ \Theta(\gamma)=0\ \wedge\ \text{winding}=0\implies\neg\exists\ \text{wrapping holonomy}\implies\neg\exists\ \text{wrapping contribution}\ [\mathrm{EM.5},\mathrm{EW.18}].
$$

### EM.7 — Photon entropy budget

**Thm.** Photon chain of hop count $\delta h$:
$$
\mathsf E_{\mathrm{tr}}=\delta h\,\ln2\ \ \text{nats}=\delta h\ \ \text{bits};\qquad
\mathsf E_{\mathrm{bd}}=0 .
$$

### EM.12 — Discrete field strength from phase transitions

**Thm.** [D3.3]
$$
f_v=\tfrac12\bigl(\sigma_{\rightarrow}(v)-\sigma_{\leftarrow}(v)\bigr)\in\{-1,0,+1\};\qquad\aleph_v=|f_v|\in\{0,1\};
$$
$$
\aleph(\sigma,C)=0\iff\forall v:\ \sigma_{\leftarrow}(v)=\sigma_{\rightarrow}(v)\iff\sigma\ \text{constant on connected components}\ \ (\text{flat});
$$
$$
\aleph_v=1\iff\text{oriented transition at}\ v;\qquad
\text{coarse-graining}\ [\mathrm{CT1.19}]:\ f_v\longrightarrow F_{\mu\nu}\ \ (\text{circulation per plaquette})\ [\mathrm{CT1.22}].
$$

### EM.14 — Continuum gauge invariance

**Thm.**
$$
A_\mu\sim A_\mu+\nabla_\mu\chi;\qquad
F_{\mu\nu}=2\nabla_{[\mu}A_{\nu]}\ \mapsto\ F_{\mu\nu}+2\nabla_{[\mu}\nabla_{\nu]}\chi=F_{\mu\nu};
$$
$$
\implies\text{gradient direction}=\text{redundancy};\quad N_{\mathrm{pol}}\ \text{count unaffected}\ [\mathrm{EM.8}].
$$

### EM.8 — Photon polarization count

**Thm.** $D=4$; $k_\mu\ne0$ null $\bigl(k^\mu k_\mu=0\bigr)$; $\epsilon_\mu\sim\epsilon_\mu+k_\mu$ (gauge, EM.14); transversality $k^\mu\epsilon_\mu=0$ (source-free equation, CT1.22). Then
$$
N_{\mathrm{pol}}=\dim\bigl(k^\perp/\operatorname{span}\{k\}\bigr)=(4-1)-1=2,\qquad
k^\perp:=\{v:\ k_\mu v^\mu=0\}.
$$

### Cor EM.9b

**Cor EM.9b (chain-wall telescoping).** Let $c=(e_1,\dots,e_k)$, $k\ge2$, be an oriented chain of distinct real edges [D1.4] with interior vertices $v_1,\dots,v_{k-1}$, $v_i:=t(e_i)=s(e_{i+1})$, each of type $(1,1)$ [A7, D0.8] — the chain's two edges are $v_i$'s only incident real edges. Then the D3.3 vertex reads telescope:
$$
\sum_{i=1}^{k-1}f_{v_i}\ =\ \tfrac12\bigl(\sigma_{e_k}-\sigma_{e_1}\bigr)\ =\ -\,q_{\mathrm{EM}}(c)
\qquad\bigl[\sigma_{s(c)}=\sigma_{e_1},\ \ \sigma_{t(c)}=\sigma_{e_k}:\ \mathrm{D3.4}/\mathrm{EM.9}\ \text{end registers}\bigr]
$$
— the total interior vertex activity of a chain is carried by its two end registers alone. In particular:
$$
\sum_{i=1}^{k-1}f_{v_i}=0\iff\sigma_{e_1}=\sigma_{e_k}\iff q_{\mathrm{EM}}(c)=0;\qquad
\sum_{i=1}^{k-1}\aleph_{v_i}=\#\{i:\ \sigma_{e_{i+1}}\ne\sigma_{e_i}\}\le k-1\qquad[\mathrm{D3.3}:\ \aleph_v=|f_v|;\ \mathrm{CT0.9}].
$$

### EM.9a — The closed-core charge read and the end-register count

**Thm.** $(1)$ **Closed-core read.** For a closed oriented chain $c=(e_1,\dots,e_k)$ based at $v=s(c)=t(c)$ [D1.4: ordered tuple] with first edge $e_1$ (out of $v$) and last edge $e_k$ (into $v$):
$$q_{\mathrm{core}}(c;v):=\frac{\sigma_{e_1}-\sigma_{e_k}}{2}\ \in\ \{-1,0,+1\}$$
is well-defined [D3.4 applied to closed $c$; CT0.9: per-edge independent registers; EM.9: alphabet, all values attained].
$(2)$ **Charge-conjugation law.** Under rebase / orientation reversal the roles of $e_1$ and $e_k$ swap:
$$q_{\mathrm{core}}\ \mapsto\ -\,q_{\mathrm{core}}$$
— consistent with, and an instance of, D2.6's $\omega$ (charge $\mapsto$ $-$charge): the corpus's own charge-conjugation law, verbatim on the core read. At the 2-cycle floor: $q_{\mathrm{core}}=\tfrac12(\sigma_{e_1}-\sigma_{e_2})$ at base $p$, negated at base $q$.
$(3)$ **End-register count.** The EM.9/D3.4 read consumes exactly the two end registers of the chain: $N_{\mathrm{charge}}=2$ is a theorem, $\neg$an enumeration convention; the ternary alphabet is the difference of two binary registers [CT0.9], with all three values attained (witnesses $(\sigma_1,\sigma_k)=(+,-)\mapsto+1$, $(+,+)\mapsto0$, $(-,+)$ or $(-,-)\mapsto$ the remaining values; surjectivity machine-checked).
$(4)$ **Not neutral by closure.** The closed core is $\neg$forced charge-neutral: its ternary read is basepoint data. The observer-facing charge of a transit chain remains the EM.9 end-read.

### EM.16 — Edge transfer weight and the per-edge read-back

**Thm.** [D3.5] For every real edge $e$:
$$
G(e)=\sigma_e\,\exp\!\bigl(i\,\alpha_e\,\widehat{ds}^{\,2}(e)\bigr);\qquad
\alpha_e=\frac1i\,\frac{\partial}{\partial\,\widehat{ds}^{\,2}(e)}\log\!\bigl(\sigma_e^{-1}G(e)\bigr);\qquad
[\alpha_e]=\mathfrak q^{0}.
$$

### EM.17 — Spectral read of the electromagnetic block

**Thm.** $\ \forall n\ge2:$ the masked force acts as a scalar on the one-dimensional EM block [CT0.14, D2.3]:
$$
\mathbf F_M^{(n)}\big|_{\mathcal K^{(\mathrm{EM})}}=\alpha_{\mathrm{EM}}^{(n)}\cdot\mathrm{id};\qquad
\alpha_{\mathrm{EM}}^{(n)}=\frac{\mathfrak T\bigl(Y_{\mathrm{asp}}\,\mathbf F_M^{(n)}\,Y_{\mathrm{asp}}\bigr)}{\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)}=\mathfrak T\bigl(Y_{\mathrm{asp}}\,\mathbf F_M^{(n)}\,Y_{\mathrm{asp}}\bigr);\qquad
\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)=1.
$$
$\alpha_{\mathrm{EM}}^{(n)}$ is the force-space block-scale read at rung $n$; the edge phases $\alpha_e$ are per-edge registration data [D3.5, EM.20].

### CT3.7 — The strictly new rung-3 algebra is $\mathfrak{su}(3)$

**Thm.** Strictly new gauge structure at rung 3 [D3.2]:
$$
\mathfrak u(3)\big/\mathfrak u(1)\cong\mathfrak{su}(3);\qquad
\pi:\mathfrak u(3)\to\mathfrak{su}(3),\ \ \pi(X)=X-\tfrac{\mathfrak T(X)}{3}I_3:\ \ \text{Lie homomorphism},\ \ \ker\pi=\operatorname{span}_{\mathbb R}\{I_3\},\ \ \text{surjective};
$$
$$
\mathfrak T(T_a)=0\quad\forall a\ \ (\neg\exists\ \text{central component}).
$$

### EM.18 — The colour sector does not shift the block read

**Thm.** $ \alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}.$

### EM.19 — The saturation sector does not shift the block read

**Thm.** On the accessible rung-2 subspace: $ \alpha_{\mathrm{EM}}^{(n)}=\alpha_{\mathrm{EM}}^{(2)}\quad\forall n\ge4.$

### Def-EM.20 — The per-edge phase at crystallization

**Def.** For each real edge $e=(s,t)$ [A4, D0.1], the phase $\alpha_e\in\Phi$ [D0.5] is the branch index of the A4 crystallization criterion for the pair state $\rho_{st}$ at the seal [A4, D1.2]:
$$
\alpha_e\ :=\ \alpha_{st}\ :=\ \begin{cases} 0 & \text{if } \bigl|\Pi_{\mathcal V}\rho_{st}\bigr|\le\varepsilon_q \quad \text{(aligned branch)} \\ \pi & \text{if } \bigl|\Pi_{\mathcal V}\rho_{st}\bigr|\ge 1-\varepsilon_q \quad \text{(antialigned branch)} \end{cases}
$$
— A4 declares the branch phase $\alpha_{pq}$ and both branches' non-emptiness; A7 declares the edge map $e\mapsto\alpha_e\in\{0,\pi\}$; this definition is the identification $\alpha_e=\alpha_{st}$. The branch windows are disjoint exactly when $\varepsilon_q<1-\varepsilon_q$, guaranteed by the admissible range $\varepsilon_q\in[0,\tfrac14)$ [CT0.8]. The branch read is a registration alternative [D1.1: the reality principle — registration transport acts on the reality line by $\{+1,-1\}$]: aligned $\leftrightarrow+1$, antialigned $\leftrightarrow-1$, so $e^{i\alpha_e}\in\{+1,-1\}$ is the alignment holonomy. Virtual pairs ($\varepsilon_q<\bigl|\Pi_{\mathcal V}\rho_{st}\bigr|<1-\varepsilon_q$) carry no $\alpha_e$ [A4, CT0.1; clause (3) of EM.20]

### EM.20 — The dynamic edge phase

**Thm.** With $\alpha_e$ as in Def-EM.20, under A1 ($\mathbb C^2$ qubits), A4 (two-branch crystallization; branch phase $\alpha_{pq}$; both branches populated), A5 (vacuum $\rho_\circ=I/4$; Haar draws), A6 (tick dynamics), A7 (edge phase map), CT0.9 ($\Phi=\{0,\pi\}$), D0.4 ($\varepsilon_q$), D1.6 ($\widehat{ds}^{\,2}$), D3.5 (edge weight):
$(1)$ **Alphabet preservation.** $\alpha_e\in\{0,\pi\}=\Phi$ for every real edge $e$; the phase alphabet is unchanged. [A4, A7; CT0.9]
$(2)$ **Phase determination.** $\alpha_e=\alpha_{st}$ is the branch index of the A4 criterion for the pair state at the moment of crystallization [A4, D1.2]: the phase is a measurement outcome — registration data read at the seal [D1.1] — $\neg$ a declared constant.
$(3)$ **Virtual edges.** For $e\in\mathcal V$ [CT0.1: $\varepsilon_q<\bigl|\Pi_{\mathcal V}\rho_{st}\bigr|<1-\varepsilon_q$] the pair carries the full $\mathbb C^2\otimes\mathbb C^2$ statespace [A1]; $\alpha_e$ is undefined. The binary restriction scopes to real (crystallized) edges.
$(4)$ **Edge weight.** $G(e)=\sigma_e\cdot e^{i\alpha_e\,\widehat{ds}^{\,2}(e)}$ with $\alpha_e$ per-edge. [D3.5]
$(5)$ **Both values attained; distribution governed.** Both A4 branches are populated [A4 populatedness clause]; witnesses: a symmetric-dominated pair ($\bigl|\Pi_{\mathcal V}\rho\bigr|=0\Rightarrow\alpha_e=0$) and the pure singlet ($\bigl|\Pi_{\mathcal V}\rho\bigr|=1\Rightarrow\alpha_e=\pi$). Across $E_{\mathcal R}$ the distribution of $\alpha_e$ is governed by the Haar randomization [A5, A6] and the crystallization criterion [A4].

### Def-EM.21 — Alignment pattern

**Def.** For a subnetwork $\Sigma$ [D2.13] with real edge set $E_{\mathcal R}(\Sigma):=\{e\in E_{\mathcal R}:\ e\ \text{touches}\ \Sigma\}$ ($|\Sigma|=\#E_{\mathcal R}(\Sigma)$, D2.13), the alignment pattern is
$$
\mathcal P(\Sigma)\ :=\ \bigl\{\,e\in E_{\mathcal R}(\Sigma):\ \alpha_e=\pi\,\bigr\}
$$
— the set of antialigned edges [Def-EM.20]. $\mathcal P(\Sigma)\subseteq E_{\mathcal R}(\Sigma)$; on a chain $c$ [D1.4]: $\mathcal P(c):=\mathcal P(\Sigma)\cap c$; on a configuration $C$ [D0.10]: $\mathcal P(C):=\{e\in E(C):\ \alpha_e=\pi\}$.

### Def-EM.22 — Mirror operation

**Def.** A mirror $M$ on $\Sigma$ is an automorphism of the underlying graph of $\Sigma$ that reverses orientation [D2.6 $\omega$-type: $s\leftrightarrow t$]. $M$ acts on the alignment pattern:
$$
M(\mathcal P(\Sigma))\ :=\ \bigl\{M(e):\ e\in\mathcal P(\Sigma)\bigr\}
$$
where $\Sigma$ admits such an automorphism (witnesses: path and cycle reflections — machine, `checks/verify_F33_dynamic_phase.py` §B).

### EM.23 — Parity classification

**Thm.** Under Def-EM.21 and Def-EM.22, for a subnetwork $\Sigma$ with mirror $M$:
$(1)$ **Parity-preserving.** $\Sigma$ is parity-even $\iff M(\mathcal P(\Sigma))=\mathcal P(\Sigma)$: the alignment pattern is invariant under the mirror.
$(2)$ **Parity-reversing.** $\Sigma$ is parity-odd $\iff M(\mathcal P(\Sigma))=E_{\mathcal R}(\Sigma)\setminus\mathcal P(\Sigma)$: the alignment pattern inverts under the mirror.
$(3)$ **Distinguishability.** Parity-even and parity-odd subnetworks are distinguishable $\iff\mathcal P(\Sigma)\ne E_{\mathcal R}(\Sigma)\setminus\mathcal P(\Sigma)$ — the alignment pattern is not self-complementary — which holds exactly when $E_{\mathcal R}(\Sigma)\ne\varnothing$: at least one real edge ("there is something" — CT2.6(i) as the definitional precondition it is, D2.11).
$(4)$ **Degrees of freedom.** The number of distinct alignment patterns on $\Sigma$ is $2^{|E_{\mathcal R}(\Sigma)|}$: each real edge carries an independent binary phase [CT0.9, EM.20(5)]. Each pattern is a distinct parity configuration. The uniform assignments ($\mathcal P=\varnothing$ and $\mathcal P=E_{\mathcal R}$) are two points of this space; any single fixed pattern occupies one point.

### EM.24 — The CPT bridge

**Thm.** On the configuration space $\mathfrak C(\mathcal R)$ [D0.10]:
$(1)$ **C (charge conjugation).** $q_{\mathrm{EM}}=\tfrac12(\sigma_s-\sigma_t)\in\{-1,0,+1\}$ [D3.4, EM.9]; charge conjugation $C:\sigma_e\mapsto-\sigma_e\ \forall e\in E(C)$ gives $q\mapsto-q$, $f_v\mapsto-f_v$, $\aleph_v$ invariant [D3.3]; the sign-level realization of D2.6's $\omega$ on end and core reads [EM.9a(2)]. Derived.
$(2)$ **P (parity).** The alignment pattern $\mathcal P(\Sigma)$ [Def-EM.21]; parity reversal $P:\mathcal P\mapsto E_{\mathcal R}\setminus\mathcal P$ — equivalently $\alpha_e\mapsto\pi-\alpha_e$ per edge — the inversion locus of EM.23(2). Derived from the dynamic phase [Def-EM.20, EM.20(1)].
$(3)$ **T (time reversal).** The Janus reflection $\Theta_{\mathfrak L}$ [D2.7]: $w(\Theta_{\mathfrak L}C)=w(C)^\ast$ [CT2.8(1)]. Derived.
$(4)$ **CPT composition.** $\mathrm{CPT}:=C\circ P\circ T$: well-defined on $\mathfrak C(\mathcal R)$; each component an involution ($C^2=P^2=T^2=\mathrm{id}$); each component derived from the corpus — no external input.
$(5)$ **CPT invariance.** The exact phase identity and its consequences:
$$
w(\mathrm{CPT}\,C)=(-1)^{|E(C)|}\,e^{i\pi\Theta(C)}\,w(C),\qquad\Theta(C):=\!\!\sum_{e\in E(C)}\!\!\widehat{ds}^{\,2}(e)\in\mathbb R;
$$
$$
\bigl|w(\mathrm{CPT}\,C)\bigr|^2=\bigl|w(C)\bigr|^2\qquad\forall C\ \ (\text{unconditional});
$$
$$
\text{on-shell}\ [\widehat{ds}^{\,2}(e)\in\mathbb Z\ \forall e]:\ \ w(C)\in\mathbb R\ \ \wedge\ \ \bigl(|E(C)|+\Theta(C)\equiv0\ (\mathrm{mod}\ 2)\bigr)\implies w(\mathrm{CPT}\,C)=w(C)^\ast .
$$

### CT3.20 — The number of colours is forced

**Thm.**
$$
\text{admissible}(v)\iff n(v)\le3;\qquad
\max_{\text{admissible}}\mathcal H^{(n)}_{\mathrm{slot}}=\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3;
$$
$$
N_{\text{colour}}=3=\log_2C_{\mathrm{cap}}-1=\log_216-1\qquad(\text{derived from A2}+\mathrm{CT0.9};\ \neg\text{chosen}).
$$

### CT3.9 — Explicit generator basis

**Thm.** With the Gell-Mann matrices
$$
\lambda_1=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},\
\lambda_2=\begin{pmatrix}0&-i&0\\i&0&0\\0&0&0\end{pmatrix},\
\lambda_3=\begin{pmatrix}1&0&0\\0&-1&0\\0&0&0\end{pmatrix},\
\lambda_4=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix},
$$
$$
\lambda_5=\begin{pmatrix}0&0&-i\\0&0&0\\i&0&0\end{pmatrix},\
\lambda_6=\begin{pmatrix}0&0&0\\0&0&1\\0&1&0\end{pmatrix},\
\lambda_7=\begin{pmatrix}0&0&0\\0&0&-i\\0&i&0\end{pmatrix},\
\lambda_8=\frac1{\sqrt3}\begin{pmatrix}1&0&0\\0&1&0\\0&0&-2\end{pmatrix},
$$
and $T_a:=\tfrac12\lambda_a$:
$$
T_a^\dagger=T_a;\qquad\mathfrak T(T_a)=0;\qquad
\{T_a\}_{a=1}^{8}:\ \mathbb R\text{-basis of}\ \mathfrak{su}(3);\qquad
[T_a,T_b]=i\,f_{abc}\,T_c,\ \ f_{abc}\in\mathbb R;\qquad
\mathfrak T(T_aT_b)=\tfrac12\,\delta_{ab}.
$$

### CT3.21 — Structure constants

**Thm.** $\ f_{abc}:=-2i\,\mathfrak T\bigl([T_a,T_b]T_c\bigr)$ is totally antisymmetric, with independent nonzero values
$$
f_{123}=1;\qquad
f_{147}=f_{246}=f_{257}=f_{345}=\tfrac12;\qquad
f_{156}=f_{367}=-\tfrac12;\qquad
f_{458}=f_{678}=\frac{\sqrt3}{2};
$$
$\forall$ other independent components $=0$.

### CT3.10 — The colour aspect has no central component

**Thm.**
$$
F_{\mathrm{strong}}=\textstyle\sum_af_aT_a\implies\mathfrak T(F_{\mathrm{strong}})=0;\qquad
Y_{\mathrm{asp}}F_{\mathrm{strong}}Y_{\mathrm{asp}}=0;\qquad
\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}\quad[=\mathrm{EM.18},\ \text{restated}].
$$

**Cor CT3.10a (no per-edge abelian strong phase).** $(1)$ **Coefficient-read obstruction.** EM.17's read $\alpha^{(n)}=\mathfrak T\bigl(Y_{\mathrm{asp}}\mathbf F_M^{(n)}Y_{\mathrm{asp}}\bigr)/\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)$ yields a single number exactly because the EM block is one-dimensional [CT0.14: $\dim\mathcal K^{(\mathrm{EM})}=1$; EM.17]. The strong block is eight-dimensional [CT0.14, CT3.8: $\dim\mathcal K_3=25=17+8$], and
$$
F_{\mathrm{strong}}=\textstyle\sum_af_aT_a=c\,I_3\quad\iff\quad c=0\ \wedge\ f_a=0\ \ \forall a
$$
[CT3.7: $\mathfrak T(T_a)=0\implies3c=\mathfrak T(F_{\mathrm{strong}})=0$; CT3.9: the $T_a$ are linearly independent] — the read returns no scalar on the strong block: $\neg\exists$ a per-edge abelian strong phase coefficient $\alpha_{\mathrm{strong}}$ defined by derived structure.
$(2)$ **Non-canonicity.** $\mathfrak{su}(3)$ contains $\mathfrak u(1)$ subalgebras [$\operatorname{span}_{\mathbb R}\{T_a\}$, CT3.9], but no generator line is fixed by the adjoint action — all maximal tori are conjugate [math] — so no $\mathfrak u(1)$ choice is distinguished by derived structure. Explicit witnesses (integer-entry $SU(3)$ elements of the CT3.9 basis [CT3.4; $\lambda_a=2T_a$; unitary, $\det=1$ — machine]):
$$
U_2=i\lambda_2+I_3-\lambda_2^{2},\qquad U_5=i\lambda_5+I_3-\lambda_5^{2}\qquad[\lambda_2^{2}=\operatorname{diag}(1,1,0),\ \ \lambda_5^{2}=\operatorname{diag}(1,0,1)]
$$
$$
\operatorname{Ad}_{U_5}(T_1)=U_5\,T_1\,U_5^{\dagger}=-\,T_6\ \notin\ \operatorname{span}_{\mathbb R}\{T_1\};\qquad
\forall a\in\{1,\dots,8\}\ \exists U\in\{U_2,U_5\}:\ \operatorname{Ad}_U(T_a)\notin\operatorname{span}_{\mathbb R}\{T_a\}\qquad[\text{machine census}].
$$
$(3)$ **Consequence (pointer).** With $\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}$ [CT3.10; EM.18 restated], the per-edge scalar factor $e^{i\alpha_e\widehat{ds}^{\,2}(e)}$ of the transfer weight is entirely electromagnetic [D3.5: $\alpha_e\in\Phi$, the same alphabet at every rung], and CT3.22a(0)'s decomposition — EM factor $\times$ $\{0,1\}$ singlet-sealing admissibility [D2.14; CT3.17, CT3.18 — forward in-document pointers, non-load-bearing] — exhausts the per-edge strong datum: no phase factor remains.

### Cor CT3.10a

**Cor CT3.10a (no per-edge abelian strong phase).** $(1)$ **Coefficient-read obstruction.** EM.17's read $\alpha^{(n)}=\mathfrak T\bigl(Y_{\mathrm{asp}}\mathbf F_M^{(n)}Y_{\mathrm{asp}}\bigr)/\mathfrak T\bigl(Y_{\mathrm{asp}}\bigr)$ yields a single number exactly because the EM block is one-dimensional [CT0.14: $\dim\mathcal K^{(\mathrm{EM})}=1$; EM.17]. The strong block is eight-dimensional [CT0.14, CT3.8: $\dim\mathcal K_3=25=17+8$], and
$$
F_{\mathrm{strong}}=\textstyle\sum_af_aT_a=c\,I_3\quad\iff\quad c=0\ \wedge\ f_a=0\ \ \forall a
$$
[CT3.7: $\mathfrak T(T_a)=0\implies3c=\mathfrak T(F_{\mathrm{strong}})=0$; CT3.9: the $T_a$ are linearly independent] — the read returns no scalar on the strong block: $\neg\exists$ a per-edge abelian strong phase coefficient $\alpha_{\mathrm{strong}}$ defined by derived structure.
$(2)$ **Non-canonicity.** $\mathfrak{su}(3)$ contains $\mathfrak u(1)$ subalgebras [$\operatorname{span}_{\mathbb R}\{T_a\}$, CT3.9], but no generator line is fixed by the adjoint action — all maximal tori are conjugate [math] — so no $\mathfrak u(1)$ choice is distinguished by derived structure. Explicit witnesses (integer-entry $SU(3)$ elements of the CT3.9 basis [CT3.4; $\lambda_a=2T_a$; unitary, $\det=1$ — machine]):
$$
U_2=i\lambda_2+I_3-\lambda_2^{2},\qquad U_5=i\lambda_5+I_3-\lambda_5^{2}\qquad[\lambda_2^{2}=\operatorname{diag}(1,1,0),\ \ \lambda_5^{2}=\operatorname{diag}(1,0,1)]
$$
$$
\operatorname{Ad}_{U_5}(T_1)=U_5\,T_1\,U_5^{\dagger}=-\,T_6\ \notin\ \operatorname{span}_{\mathbb R}\{T_1\};\qquad
\forall a\in\{1,\dots,8\}\ \exists U\in\{U_2,U_5\}:\ \operatorname{Ad}_U(T_a)\notin\operatorname{span}_{\mathbb R}\{T_a\}\qquad[\text{machine census}].
$$
$(3)$ **Consequence (pointer).** With $\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}$ [CT3.10; EM.18 restated], the per-edge scalar factor $e^{i\alpha_e\widehat{ds}^{\,2}(e)}$ of the transfer weight is entirely electromagnetic [D3.5: $\alpha_e\in\Phi$, the same alphabet at every rung], and CT3.22a(0)'s decomposition — EM factor $\times$ $\{0,1\}$ singlet-sealing admissibility [D2.14; CT3.17, CT3.18 — forward in-document pointers, non-load-bearing] — exhausts the per-edge strong datum: no phase factor remains.

### CT3.14 — Gluons remain massless

**Thm.** $\ m_g^2=0$, by two independent routes:
$$
(\mathrm{i})\quad T_a\mathsf v=0\ [\mathrm{EW.32}]\implies M^2_{aB}=M^2_{ab}=0\implies\{T_a\}\subseteq\ker M^2\implies\text{zero pole displacement}\quad[=\mathrm{EW.26},\ \text{restated}];
$$
$$
(\mathrm{ii})\quad\gamma_g\in\mathsf{Trivial}\implies\Theta(\gamma_g)=0\implies\neg\text{wrapping holonomy}\implies\neg\text{wrapping contribution}\ [\mathrm{EW.18}].
$$

### CT3.12 — Photon and gluon are distinguished by possibility space

**Thm.**
$$
\gamma_\gamma,\ \gamma_g\in\mathsf{Trivial}:\ \ \widehat{ds}^{\,2}(e)=0\ \ \forall e,\ \ \Theta=0,\ \ \operatorname{Hol}_{\mathrm{spiral}}=1;
$$
$$
\text{distinction}:\ \ \gamma_\gamma\subseteq V_2\quad\text{vs}\quad\gamma_g\cap V_3\ne\varnothing;
$$
$$
\mathrm{strong}\in\mathcal A(3)\setminus\mathcal A(2)\implies\gamma_\gamma:\ \neg\text{colour index};\quad\gamma_g:\ \text{slot index possible}\ [\mathrm{D3.1}];
$$
$$
\text{class, entropy channel (transit, D1.5), mass}\ (0)\ \text{coincide}.
$$

### CT3.15 — Baryon invariance

**Thm.** $\ B=\varepsilon_{ijk}q^iq^jq^k;\qquad U\in SU(3):\quad B\mapsto\varepsilon_{ijk}U^i{}_aU^j{}_bU^k{}_c\,q^aq^bq^c=\det(U)\,\varepsilon_{abc}\,q^aq^bq^c=B.$

### CT3.17 — Invariant tensors

**Thm.** The invariant tensors for sealing colour indices are generated by
$$
\delta^i{}_j,\qquad\varepsilon_{ijk},\qquad\varepsilon^{ijk};
$$
$$
q^ir_i\mapsto U^i{}_aq^a\,r_b(U^{-1})^b{}_i=q^ar_a;\qquad
\varepsilon_{ijk}:\ 3\ \text{fundamentals}\ [\mathrm{CT3.15}];\qquad
\varepsilon^{ijk}:\ 3\ \text{duals}\ \bigl(\det(U^{-1})^{\mathsf T}=1\bigr);
$$
$$
\forall\ \text{invariants of}\ (\mathbf3,\bar{\mathbf3}):\ \ \text{linear combinations of products of}\ \{\delta,\varepsilon,\bar\varepsilon\}.
$$

**Cor CT3.17a (sealing partition rule; grammar counts).** $(1)$ **Partition rule.** If a colour-attachment set is sealed — $\mathcal C(\Sigma;C)=1$ [D2.14] — then $\mathrm{Colour}(\Sigma)$ partitions into elementary contraction groups of size $2$ ($\delta$-type) and size $3$ ($\varepsilon/\bar\varepsilon$-type) [CT3.17: the invariant tensors are $\delta^{i}{}_{j}$ ($2$ members), $\varepsilon_{ijk}$, $\varepsilon^{ijk}$ ($3$ members); D2.14: $\pi_C(v)=$ the other members of $v$'s elementary group]. A lone attachment is never sealed:
$$
|\mathrm{Colour}(\Sigma)|=1\implies\mathcal C(\Sigma;C)=0
$$
[a contraction partner is a distinct node — A1: $p\ne q$ — hence $\pi_C(v)\not\subseteq\{v\}$; equivalently, CT3.17's list contains no invariant of a single slot].
$(2)$ **Grammar count.** The number $g(N)$ of elementary groupings of a labelled $N$-element attachment set into groups of size $2$ and $3$ (labelled set partitions with parts in $\{2,3\}$) is
$$
g(N)=\!\!\sum_{\substack{a,b\ge0\\ 2a+3b=N}}\!\!\frac{N!}{a!\,b!\,2^{a}\,6^{b}};\qquad
g(1)=0,\quad g(2)=1,\quad g(3)=1,\quad g(4)=3,\quad g(5)=10,\quad g(6)=25\ (15+10),\quad g(7)=105 .
$$
$(3)$ **Type selection.** Attachment-type assignment (triplet/antitriplet per attachment [D3.8]) selects the type-compatible groupings — $\delta^{i}{}_{j}$ consumes one attachment of each type, $\varepsilon_{ijk}$ ($\varepsilon^{ijk}$) three of the same type [CT3.17] — configuration data refining the count of $(2)$.

### CT3.11 — Colour objects

**Thm.** Within the rung-3 structure:
$$
(1)\ \ \text{colour}:=\text{slot index}\ i\in\{1,2,3\}\ [\mathrm{D3.1}],\ \ \text{fundamental of}\ \mathfrak{su}(3);
$$
$$
(2)\ \ \text{triplet}:\ q^i\mapsto U^i{}_jq^j\ (U\in SU(3));\qquad
(3)\ \ \text{antitriplet}:\ r_i\mapsto r_j(U^{-1})^j{}_i;
$$
$$
(4)\ \ \text{gluon}:=\gamma\in\mathsf{Trivial}\wedge\gamma\cap V_3\ne\varnothing;\qquad
(5)\ \ \text{photon}:=\gamma\in\mathsf{Trivial}\wedge\gamma\subseteq V_2\qquad[\mathrm{D3.7}];
$$
$$
(6)\ \ \text{quark}:=\text{bound loop}\ [\mathrm{D1.5}:\ \text{fermionic}]\ \text{with triplet attachment}\ [\mathrm{D3.8}];
$$
$$
(7)\ \ B:=\varepsilon_{ijk}q^iq^jq^k\ (\text{baryon});\qquad M:=\delta^i{}_jq^jr_i\ (\text{meson})\qquad[\mathrm{D3.9}].
$$

### CT3.13 — Gluon count

**Thm.** $\ N_{\mathrm{gluon}}=\dim\mathfrak{su}(3)=8;\qquad\neg\exists\ \text{ninth mode}\ (\text{centre of}\ \mathfrak u(3)\ \text{allocated to}\ F_{\mathrm{EM}}).$

### CT3.16 — Infinitesimal baryon invariance

**Thm.** $\ U=I_3+i\theta^aT_a+O(\theta^2),\ \ \mathfrak T(T_a)=0\implies\det U=1+O(\theta^2)\implies B\mapsto B+O(\theta^2)$ (first-order variation vanishes).

### Cor CT3.17a

**Cor CT3.17a (sealing partition rule; grammar counts).** $(1)$ **Partition rule.** If a colour-attachment set is sealed — $\mathcal C(\Sigma;C)=1$ [D2.14] — then $\mathrm{Colour}(\Sigma)$ partitions into elementary contraction groups of size $2$ ($\delta$-type) and size $3$ ($\varepsilon/\bar\varepsilon$-type) [CT3.17: the invariant tensors are $\delta^{i}{}_{j}$ ($2$ members), $\varepsilon_{ijk}$, $\varepsilon^{ijk}$ ($3$ members); D2.14: $\pi_C(v)=$ the other members of $v$'s elementary group]. A lone attachment is never sealed:
$$
|\mathrm{Colour}(\Sigma)|=1\implies\mathcal C(\Sigma;C)=0
$$
[a contraction partner is a distinct node — A1: $p\ne q$ — hence $\pi_C(v)\not\subseteq\{v\}$; equivalently, CT3.17's list contains no invariant of a single slot].
$(2)$ **Grammar count.** The number $g(N)$ of elementary groupings of a labelled $N$-element attachment set into groups of size $2$ and $3$ (labelled set partitions with parts in $\{2,3\}$) is
$$
g(N)=\!\!\sum_{\substack{a,b\ge0\\ 2a+3b=N}}\!\!\frac{N!}{a!\,b!\,2^{a}\,6^{b}};\qquad
g(1)=0,\quad g(2)=1,\quad g(3)=1,\quad g(4)=3,\quad g(5)=10,\quad g(6)=25\ (15+10),\quad g(7)=105 .
$$
$(3)$ **Type selection.** Attachment-type assignment (triplet/antitriplet per attachment [D3.8]) selects the type-compatible groupings — $\delta^{i}{}_{j}$ consumes one attachment of each type, $\varepsilon_{ijk}$ ($\varepsilon^{ijk}$) three of the same type [CT3.17] — configuration data refining the count of $(2)$.

### CT3.18 — Colour-singlet closure

**Thm.**
$$
\text{free colour index}=\text{dangling boundary of the colour ledger}\ \neg\text{admitted by}\ \mathcal P_M^{(3)};
$$
$$
\mathcal P_M^{(3)}\big|_{\text{free index}}=0\implies\neg\exists\ \text{pole}\ [\mathrm{CT2.5}];\qquad
\text{surviving configurations}:\ \text{fully contracted by}\ \{\delta,\varepsilon,\bar\varepsilon\}\implies\text{colour singlets};
$$
$$
\text{minimal singlets}:\ M=\delta^i{}_jq^jr_i,\quad B=\varepsilon_{ijk}q^iq^jq^k\ [\mathrm{D3.9}].
$$

### CT3.22 — Sealing is confinement

**Thm.**
$$
\neg\exists\ \text{isolated triplet pole of}\ Z(\mathcal R,3);\qquad
\text{isolated triplet}:\ \text{physical norm}=0\ [\mathrm{CT2.8}];
$$
$$
\text{colour charge}\ \neg\text{observable as end-charge}\ [\mathrm{D3.4}];\qquad
\text{contrast}:\ q_{\mathrm{EM}}\ \text{observable on open chains}\ (\text{per-edge registration},\ \neg\text{contraction}).
$$

### CT4.2 — The lock is absorbing

**Thm.**
$$
\forall n\le3:\quad\mathcal P_M^{(n)}\,F_{D^-}\,\mathcal P_M^{(n)}=0;
$$
$$
\text{locked content}:\ \neg\exists\ \text{pole of}\ Z(\mathcal R,n)\ \ \forall n\le3\qquad(\text{one-way transfer w.r.t. the accessible sector}).
$$

### CT4.3 — Locked, not destroyed

**Thm.**
$$
\text{absorption conserves ledger content}:\quad\text{absorbed}\subseteq\mathfrak L;\qquad\neg\text{accessible}\ [\mathrm{D1.11}];\qquad\neg\exists\ \text{deleted entry};
$$
$$
\text{oversubscription}\ \neg\text{seal}:\ \Delta n_{\mathcal R}=0;
$$
$$
\text{locked content}:\ \ \text{physical norm}=0\ \text{at accessible rungs}\ [\mathrm{CT2.8}]\ \ \wedge\ \ w(C)\ne0\ \text{in the unmasked A8 sum}\ (\text{record survives}).
$$

### CT4.1 — Oversubscription falls to $D^-$

**Thm.**
$$
\forall n\ge4:\quad D_{\mathrm{tick}}(n)=2^{n+1}\ge32>16=C_{\mathrm{cap}}\implies O(n)=2^{n+1}-16>0;
$$
$$
O(4)=32-16=16=C_{\mathrm{cap}}\quad(\text{exactly one further channel quantum per tick});
$$
$$
F_{D^-}=\bigoplus_{n\ge4}F_n\ [\mathrm{D4.1}];\qquad
\text{absorption rate}\propto O(n)\sim2^{n+1}\ [\mathrm{D4.2}];\qquad
\text{last admissible rung}=3 .
$$
$$
\begin{array}{c|c|c|c}
n & D_{\mathrm{tick}}(n)=2^{n+1} & O(n) & \text{status}\\ \hline
0 & 2 & 0 & \text{virtual only},\ \mathcal A(0)=\{J\}\\
1 & 4 & 0 & \text{pair aspects active}\\
2 & 8 & 0 & \text{abelian aspect activates}\\
3 & 16 & 0 & \text{exact saturation};\ \text{colour activates}\\
4 & 32 & 16 & \text{locked in}\ D^-\\
5 & 64 & 48 & \text{locked in}\ D^-\\
n\ge4 & 2^{n+1} & 2^{n+1}-16 & \text{locked in}\ D^-
\end{array}
$$

**Cor CT4.1a (universal saturation of bidirectional real-edge subgraphs).** Let $S$ be a bidirectional real-edge subgraph — both orientations of every used channel in $\mathcal R$ [A4] — exhausting the incident real edges at its vertices, with channel degree $d_S(v)$. Then $n(v)=2\,d_S(v)$ [CT0.11b (Part 1), D0.8], and:
$(1)\ \ d_S(v)\ge2\implies n(v)\ge4\implies O\bigl(n(v)\bigr)>0$: every such vertex falls to $F_{D^-}$ [CT4.1, D4.1]; its content is absorbed, retained in $\mathfrak L$ and counted, $\neg$accessible [CT4.2, CT4.3, D4.2, D1.11] — no bidirectional vertex of channel degree $\ge2$ is unoversubscribed.
$(2)\ \ S\ 2$-*regular* (bidirectional cycles, any length $\ge3$): uniform minimal saturation $n(v)=4\ \forall v$; $O(4)=16=C_{\mathrm{cap}}$ — exactly one channel quantum over budget per vertex, independent of cycle length [CT0.6, CT4.1].
$(3)\ \ S\ d$-*regular*: graded oversubscription $O(2d)=2^{2d+1}-16$ [CT0.6]:
$$
O(4)=16,\qquad O(6)=112,\qquad O(8)=496,\qquad O(10)=2032,\qquad O(12)=8176 .
$$
$(4)$ The unoversubscribed real-edge family under directed rung counting is exactly $n(v)\le3$ [CT0.11b, CT0.6]: on bidirectional $S$ only single-channel vertices ($n=2$); mixed skeletons admit unidirectional attachments up to $n=3$; every vertex with $n(v)\ge4$ is saturated [CT0.11, CT4.1].

### Cor CT4.1a

**Cor CT4.1a (universal saturation of bidirectional real-edge subgraphs).** Let $S$ be a bidirectional real-edge subgraph — both orientations of every used channel in $\mathcal R$ [A4] — exhausting the incident real edges at its vertices, with channel degree $d_S(v)$. Then $n(v)=2\,d_S(v)$ [CT0.11b (Part 1), D0.8], and:
$(1)\ \ d_S(v)\ge2\implies n(v)\ge4\implies O\bigl(n(v)\bigr)>0$: every such vertex falls to $F_{D^-}$ [CT4.1, D4.1]; its content is absorbed, retained in $\mathfrak L$ and counted, $\neg$accessible [CT4.2, CT4.3, D4.2, D1.11] — no bidirectional vertex of channel degree $\ge2$ is unoversubscribed.
$(2)\ \ S\ 2$-*regular* (bidirectional cycles, any length $\ge3$): uniform minimal saturation $n(v)=4\ \forall v$; $O(4)=16=C_{\mathrm{cap}}$ — exactly one channel quantum over budget per vertex, independent of cycle length [CT0.6, CT4.1].
$(3)\ \ S\ d$-*regular*: graded oversubscription $O(2d)=2^{2d+1}-16$ [CT0.6]:
$$
O(4)=16,\qquad O(6)=112,\qquad O(8)=496,\qquad O(10)=2032,\qquad O(12)=8176 .
$$
$(4)$ The unoversubscribed real-edge family under directed rung counting is exactly $n(v)\le3$ [CT0.11b, CT0.6]: on bidirectional $S$ only single-channel vertices ($n=2$); mixed skeletons admit unidirectional attachments up to $n=3$; every vertex with $n(v)\ge4$ is saturated [CT0.11, CT4.1].

### CT4.4 — The locked sector carries no gauge structure

**Thm.**
$$
D^-:\ \ \neg\exists\ \text{nonabelian gauge algebra};\qquad\neg\exists\ \text{abelian gauge algebra};\qquad
\text{contributes}\ \neg\text{generator to any accessible algebra}.
$$

### CT4.5 — Equation of state of the locked sector

**Thm.**
$$
T^{(D^-)}_{\mu\nu}=\rho_{D^-}\,u_\mu u_\nu;\qquad
p_{D^-}=0;\qquad
w_{D^-}=\frac{p}{\rho}=0;\qquad
\rho_{D^-}\ge0\ \ \bigl(=0\iff\neg\exists v:\ n(v)\ge4\bigr).
$$

### CT4.9 — Accessible entropy bounds

**Thm.**
$$
(1)\ \ \text{per vertex}:\quad\text{accessible}(v)\implies S(v)\le3\ln2\ \ \text{nats}=3\ \ \text{bits}\qquad(\text{attained at}\ n=3);
$$
$$
(2)\ \ \text{per region}\ \mathcal B,\ \partial\mathcal B\ \text{closed real-edge surface of area}\ A:\quad
S_{\mathrm{acc}}(\mathcal B)\le\frac{A}{\mathfrak h^2}\ \ \text{bits}=\frac{A}{\mathfrak h^2}\ln2\ \ \text{nats}.
$$

### CT4.7 — The entropy triangle

**Thm.** In the plane $\bigl(S_{\mathrm{raw}},\ S_{\mathfrak L}\bigr)$ with $S_{\mathrm{raw}}(\rho)=-\mathfrak T(\rho\log\rho)$ [D0.3] and $S_{\mathfrak L}=n_{\mathcal R}\ln2$ [CT1.29], there are exactly three scalar extremes, mutually exclusive:
$$
(1)\ \ \text{Janus vacuum}:\ n_{\mathcal R}=0:\quad\bigl(S_{\mathrm{raw}},S_{\mathfrak L}\bigr)=\bigl(\ln4\ \text{per pair (max)},\ 0\bigr);
$$
$$
(2)\ \ D^+:\ \text{one configuration}:\quad(0,\ 0)\qquad(\ln1=0;\ \neg\text{real edges});
$$
$$
(3)\ \ D^-:\ \text{locked}:\quad\bigl(\min_{\mathrm{acc}},\ \max\ \wedge\ \neg\text{accessible}\bigr).
$$

### CT4.6 — The two dark aspects contrasted

**Thm.**
$$
\begin{array}{c|c|c}
& D^+ & D^-\\ \hline
\text{definition} & F_{D^+}=\Lambda\,\mathbb I\ [\mathrm{D4.3}] & F_{D^-}=\bigoplus_{n\ge4}F_n\ [\mathrm{D4.1}]\\
\text{block} & \text{central pair direction}\ E_0\ [\mathrm{CT0.12}] & \text{stack block}\perp\text{pair space}\ [\mathrm{CT0.12\ Rmk}]\\
\text{activation} & n=1\ [\mathrm{CT0.13}] & n\ge4\ [\mathrm{CT0.13}]\\
\text{config.\ dependence} & \text{none}\ [\mathrm{D4.3}] & \text{full}\ [\mathrm{CT4.1}]\\
\text{rest frame} & \text{none; isotropic}\ [\mathrm{CT1.25}] & \text{one per locked cell}\ [\mathrm{CT4.5}]\\
\text{equation of state} & w=-1\ [\mathrm{CT1.25}] & w=0\ [\mathrm{CT4.5}]\\
\text{gauge content} & \text{none; central}\ [\mathrm{CT1.3}] & \text{none; disjoint}\ [\mathrm{CT4.4}]\\
\text{entropy} & \text{none}\ [\mathrm{CT4.7}] & \text{maximal, locked}\ [\mathrm{CT4.7}]
\end{array}
$$
$$
\forall\ \text{rows differ}\implies D^+\ne D^-\ (\neg\text{two descriptions of one thing});
$$
$$
\mathrm{CT1.23}:\ D^+\ \text{geometric side}\ (\Lambda g_{\mu\nu});\quad D^-\ \text{source side}\ (\rho_{D^-}u_\mu u_\nu);\qquad\neg\text{double counting}\ [\mathrm{CT1.22}].
$$

### CT4.5a — The flicker-dust ensemble: exact density polynomial and rate-invariant $w=0$

**Thm.** Hypotheses (ensemble scope, stated): $\Gamma$ a finite skeleton [A7] with potential degrees $n(v)$; every potential edge crystallizes independently with common probability $p\in[0,1]$ (a per-edge Bernoulli ensemble; the *dynamics* realizing such an ensemble is not declared in Parts 1–2 — Merge note). Then:
$(1)$ **Exact dust density.** $k_v\sim\mathrm{Bin}(n(v),p)$, and with $f_{\mathrm{adm}}(n,p):=\sum_{k\le3}\binom{n}{k}p^k(1-p)^{n-k}$ [CT0.11: admissible $\iff k\le3$], $O(n):=\max(0,\,2^{n+1}-16)$ [CT4.1, CT0.6]:
$$\langle\rho_{D^-}\rangle_\Gamma(p)=\sum_v O(n_v)\,\bigl(1-f_{\mathrm{adm}}(n_v,p)\bigr)$$
— an exact polynomial in $p$ with **integer coefficients** [CT4.5's source criterion $\rho_{D^-}>0\iff\exists v:\ k_v\ge4$, read in expectation].
$(2)$ **Anchors.** $\langle\rho\rangle_\Gamma(1)=\sum_vO(n_v)$ — Platonic values $(448,\ 896,\ 2976,\ 2240,\ 24384)$ for (tetra, cube, octa, dodeca, icosa) [$(V,\deg)=(4,3),(8,3),(6,4),(20,3),(12,5)$; math]; at $p=\tfrac12$: $\bigl(154,\ 308,\ \tfrac{15159}{8},\ 770,\ 20193\bigr)$; the polygon family $P_n$ ($n\ge3$, $\deg=2$): the exact monomial $16\,n\,p^4$; the digon identically $0$ ($k=2$ never locks [CT0.6: $O(2)=0$]); $\langle\rho\rangle_\Gamma(0)=0$; strict increase on $(0,1)$ for every lockable $\Gamma$ ($\exists v:\ n(v)\ge4$).
$(3)$ **The flicker modulates $\rho$, never $w$.** CT4.5 applies per configuration: every locked vertex contributes pressureless dust ($w=0$, source side, coupled to geometry through CT1.23 and nothing else). A mixture of $w=0$ components is $w=0$ on the locked part at every $p$ [CT1.22's linearity in the source]; $D^+$'s $w=-1$ [CT1.25, D4.3] is configuration-independent and untouched — CT4.6's contrast table holds ensemble-wise term by term.
$(4)$ **No fluid.** The locked sector supports no further equation-of-state data: a structureless absorbing sink — one possibility space [D4.1], no gauge content [CT4.4], absorption one-way [CT4.2], content retained-and-inaccessible [CT4.3, D1.11]. Statements assigning $D^-$ a pressure response, polarization, or re-emission have no defined ledger referent (the referent would contradict CT4.2/D1.11); "the vacuum is a $D^-$ fluid" is inadmissible as stated. What is derived: locked content gravitates as dust, with the density computed here.

### CT4.10 — The triangle is exhaustive

**Thm.**
$$
\neg\exists\ \text{fourth scalar extreme}:\qquad
\{\text{rotation-scalar directions of the corpus}\}=\{E_0\to F_{D^+},\ \ \Sigma\to F_H,\ \ \text{vacuum configuration},\ \ D^-\ \text{sink}\};
$$
$$
F_H\ \neg\text{extreme}\ (\text{dynamical field}).
$$

### Def-H.1 — Observer–subnetwork channel

**Def.** $o\in\mathcal Q$ a single node; $\Sigma\subset\mathcal Q$, $\Sigma\cap\{o\}=\varnothing$. The channel is
$$
\gamma(o,\Sigma):=\bigl\{e\in\mathcal R:\ e\ \text{has one endpoint}\ o,\ \text{the other in}\ \Sigma\bigr\}\ \cup\ \bigcup_{P}E(P),
$$
the union over every valid real-edge path $P$ from $o$ to $\Sigma$ lying entirely in $\mathcal Q\setminus\Sigma$ except its terminal edge. Always:
$$
\gamma(o,\Sigma)\cap\bigl(\Sigma\setminus\partial\Sigma\bigr)=\varnothing\qquad(\text{no internal edge of}\ \Sigma\ \text{is ever a member}).
$$
Hop and tick counts over an interval: $ \delta h(\gamma):=\sum_{e\in\gamma}\delta h(e)$ [D0.6]; $ \delta\tau(\gamma)$ identically from D0.7. Bookkeeping extension of A2 by summation over the boundary edge set — $\neg$new primitive (uses A2, D0.6, D0.7 only).

### Def-H.2 — Physical (metric) channel separation

**Def.** In a region where $g_{\mu\nu}=\Omega^2\bar g_{\mu\nu}$ [CT1.12] is defined:
$$
\Delta\ell(\gamma):=\int_\gamma\sqrt{\bar g_{ij}\,dx^i\,dx^j}\;\Omega;\qquad
\Delta t(\gamma):=\int_\gamma\Omega\,dx^0 .
$$

### Def-H.3 — Extractable information

**Def.**
$$
I_{o\leftarrow\Sigma}(\gamma):=\sup\bigl\{\mathsf E_{\mathrm{tr}}(\gamma'):\ \gamma'\subseteq\gamma\ \text{valid transit configuration over the interval}\bigr\},
$$
the supremum of transit entropy carried [EM.7: $\mathsf E_{\mathrm{tr}}=\delta h\ln2$, extended additively over $\gamma$]. The identification of extractable information with carried transit entropy is constitutive of this definition; coherence with the computed cards: channel payload stays FT.1-bounded [FT.36(2)], tuple labels are superselection data [Def-H.15(4)]; ledger: HistLog §II item 3.

### FT.1 — Information flux bound

**Thm.** *(observer-channel form; the chain-level bound itself — jaws, entropy read, threshold, sharpness — is CT0.6a (Part 1)):*
$(1)$ **Observer-channel extension.** With $\mathsf B(\gamma):=$ CT0.6a's bound evaluated on $\gamma$'s hop/tick counts [D0.6, D0.7]:
$$
I_{o\leftarrow\Sigma}(\gamma)\ \le\ \mathsf B(\gamma)\qquad[\mathrm{Def\text{-}H.3}:\ \text{the sup over valid transit subconfigurations inherits the memberwise bound}]
$$
$(2)$ **Geodesic gauge form.** Geodesic $\gamma$, slowly varying $\Omega,\bar g_{ij}$: $ \delta h=\Delta\ell/(\Omega\,\mathfrak h)$, $ \delta\tau=\Delta t/\Omega$ [Def-H.2], hence
$$
I_{o\leftarrow\Sigma}(\gamma)\ \le\ \frac{1}{\Omega}\,\min\Bigl(\frac{\Delta\ell(\gamma)}{\mathfrak h},\ 4\,\Delta t(\gamma)\Bigr)\ln2 .
$$

### FT.3 — Unresolvability of $D^-$-sourced subnetwork structure

**Thm.** $\Sigma,\Sigma'$ with $(\delta h,\delta\tau)$-identical channels to $o$, $\Sigma$ containing a $D^-$-configured node ($n\ge4$, CT4.1) and $\Sigma'$ none:
$$
I_{o\leftarrow\Sigma}(\gamma)=I_{o\leftarrow\Sigma'}(\gamma);\qquad
I_{o\leftarrow\Sigma''}(\gamma)=I\bigl(\delta h(\gamma),\delta\tau(\gamma)\bigr)\ \ \forall\Sigma''\in[\gamma],
$$
$$
[\gamma]:=\bigl\{\Sigma'':\ \gamma(o,\Sigma'')\ \text{has hop/tick counts}\ (\delta h(\gamma),\delta\tau(\gamma))\bigr\}\qquad(\text{exact and total over}\ [\gamma]).
$$

**Cor FT.3.1 (computational form).** For any candidate fermion terminus $f$:
$$
I_o(f)\ \le\ \min\bigl(\delta h(\gamma(o,f)),\ 4\,\delta\tau(\gamma(o,f))\bigr)\ln2,
$$
and this bound is the only quantity distinguishing $f$ from any terminus sharing its channel signature.

### Def-H.4 — Fermion

**Def.** Let $c$ be a Janus-closed oriented chain [D1.4]: $\partial c=0\wedge\#J^+=\#J^-$ — a **bound** chain, hence fermionic content by D1.5 — realized at rung $n(v)\ge2$. A **fermion** is the terminus (basepoint) $v\in\{s(c),t(c)\}$ of $c$: a bound-chain endpoint, at either end, for any admissible $\delta h(c)$, characterized externally by whatever transit (bosonic-content, D1.5) channels connect $v$ to an observer [Def-H.1, Def-H.3] and by which aspects of A8 act nontrivially there.

### FT.4 — External state characterization of a fermion terminus

**Thm.** $v$ a fermion [Def-H.4], $\gamma(o,v)$ per Def-H.1:
$$
I_o(v)\le\min\bigl(\delta h(\gamma(o,v)),\ 4\,\delta\tau(\gamma(o,v))\bigr)\ln2,
$$
and this bound is the entire externally available description: $v,v'$ with the same $(\delta h,\delta\tau)$ are observationally identical to $o$.

**Cor FT.4.1 (state-counting ceiling).** Externally distinguishable states through a fixed channel signature:
$$
N_{\mathrm{states}}\le2^{\,\min(\delta h,\ 4\,\delta\tau)}\qquad\bigl(=\min(\delta h,4\,\delta\tau)\ \text{bits of externally resolvable state}\bigr).
$$
$\neg$yet a derivation of spin, generation number, or any specific quantum number — a ceiling on the labels any channel could support.

### Def-H.5 — Information flux

**Def.**
$$
\mathcal F(\gamma):=\frac{I_{o\leftarrow\Sigma}(\gamma)}{\delta\tau(\gamma)}\quad[\text{nats/tick};\ \mathrm{C9}];\qquad
\mathcal F_{\mathrm{phys}}(\gamma):=\frac{I_{o\leftarrow\Sigma}(\gamma)}{\Delta t(\gamma)}=\frac{\mathcal F(\gamma)}{\Omega}\quad[\Delta t=\Omega\,\delta\tau,\ \Omega\ \text{constant along}\ \gamma,\ \mathrm{Def\text{-}H.2}].
$$

### FT.5 — Flux bound (rate form of FT.1)

**Thm.**
$$
\mathcal F(\gamma)\le\min\!\Bigl(\frac{\delta h(\gamma)}{\delta\tau(\gamma)}\ln2,\ \ C_{\mathrm{cap}}\ln2\Bigr)=\min\!\Bigl(\frac{\delta h}{\delta\tau},\ 4\Bigr)\ln2;\qquad
\mathcal F_{\mathrm{phys}}(\gamma)\le\frac{1}{\Omega}\min\!\Bigl(\frac{\delta h}{\delta\tau},\ 4\Bigr)\ln2 .
$$

### FT.6 — Conformal invariance of combinatorial flux

**Thm.** $g_{\mu\nu}\mapsto\Omega'^2g_{\mu\nu}:\quad\mathcal F(\gamma)\ \text{invariant};\qquad\mathcal F_{\mathrm{phys}}\mapsto\mathcal F_{\mathrm{phys}}\cdot\Omega/\Omega'.$

### FT.9 — EM part of edge weight is rung-stable

**Thm.** $ \alpha_{\mathrm{EM}}^{(n)}=\alpha_{\mathrm{EM}}^{(2)}=\pi\quad(n=2,3,\ge4;\ \text{under EM.20's historical scope tokens Comm-min}+\text{Eff}).$

### FT.10 — Confinement is a global sum-restriction

**Thm.**
$$
Z^{(3)}(\mathcal R)=\sum_{\substack{C\in\mathfrak C(\mathcal R):\ \text{colour-sealed}}}\ \sum_\sigma\mathcal J(C)\!\!\prod_{e\in E(C)}\!\!G^{(3)}(e)\ (-1)^{\aleph(\sigma,C)}\qquad[\mathrm{D0.10},\ \mathrm{C12}];
$$
confinement restricts the summation domain; $\neg$modification of any individual edge weight.

### FT.12 — Weak has no self-charge

**Thm.** The weak sector produces $\neg$independent abelian charge; its charge content reduces entirely to $Q=W_3+Y$ (the EM generator).

### FT.11 — Complete force operator charge audit

**Thm.** Per-aspect charge determination for $\mathbf F$ [A8]:
$$
\begin{array}{c|c|c}
\text{aspect} & \text{independent charge?} & \text{basis}\\ \hline
F_{\mathrm{EM}} & \text{yes} & \mathrm{EM.9}:\ q_{\mathrm{EM}}=(\sigma_s-\sigma_t)/2\in\{-1,0,+1\},\ \text{additive end-charge}\\
F_{\mathrm{strong}} & \text{no (confined)} & \mathrm{CT3.22};\ \mathfrak T(T_a)=0\ [\mathrm{CT3.7}];\ \mathfrak T(F_{\mathrm{strong}})=0\ [\mathrm{CT3.10}]\\
F_G & \text{yes} & \mathrm{D2.5}:\ m^2=\text{pole displacement}\\
F_H & \text{yes (via mass)} & \mathrm{EW.13}:\ H=h\Sigma;\ \mathrm{EW.20},\mathrm{EW.33}\\
F_{D^+} & \text{no} & \mathrm{D4.3}:\ \Lambda\mathbb I,\ \neg\text{config.-dependent}\\
F_{D^-} & \text{no} & \mathrm{CT4.4}:\ \neg\text{gauge structure}\\
F_{J^\pm} & \text{no} & \mathrm{CT0.7}:\ \text{seals},\ \neg\text{charges}\\
F_W & \text{no} & \mathrm{FT.12}:\ \text{no weak self-charge}
\end{array}
$$

### FT.13 — Weak $=$ spin (algebraically)

**Thm.** $W_i=\tfrac12\bigl(\sigma_i^{(p)}+\sigma_i^{(q)}\bigr)=$ total-spin generators of the pair; Casimir eigenvalues $2=j(j{+}1)|_{j=1}$ on $\vee^2$, $0$ on $\wedge^2$; $W_i\in\mathcal E_{+-}$ (weak sector). Hence weak $\equiv$ spin, algebraically.

### Def-H.8 — Spin (emergent weak contribution)

**Def.** For a fermion terminus $v$ [Def-H.4, $\delta h(c)\ge2$]: spin $:=$ the coarse-grained emergent-spacetime property arising from the weak sector's contribution to $c$. Justification: weak has no self-charge [FT.12] $\Rightarrow$ its contribution cannot be charge; $W_i$ are total-spin generators [FT.13] $\Rightarrow$ the contribution *is* spin.

### FT.22 — Loop quantization of materialized bound chains

**Thm.** Let $c$ be a closed chain [D1.4] that **materializes** — contributes a spectral pole of the masked resolvent $Z(\mathcal R,n)$ [D2.4, D2.5, CT2.5] at the rung $n$ of its active mask [D1.12, CT0.13]; instances: materialized wrapping chains [EW.17, EW.18], bound chains of fermion realizations [Def-H.4, D1.5]. Then the spiral holonomy around $c$ is single-valued:
$$
\operatorname{Hol}_{\mathrm{spiral}}(c)=e^{i\Phi(c)}=+1,\qquad\Phi(c)=\alpha\,\Theta(c)=2\pi k,\quad k\in\mathbb Z\ \ (\text{winding});
$$
and under EM.20's historical scope tokens (Comm-min $+$ Eff), with rung stability [FT.9: $\alpha_{\mathrm{EM}}=\pi$ at every accessible rung]:
$$
\Theta(c)=\sum_{e\in c}\widehat{ds}^{\,2}(e)=2k\in2\mathbb Z .
$$
On rung-3 wrapping chains this reduces verbatim to EW.18 (consistency check).

### FT.23 — Orientation-evenness of the line element

**Thm.** For a bidirectional channel — both orientations $e_{pq}=(p,q)$, $e_{qp}=(q,p)$ in $\mathcal R$:
$$
\widehat{ds}^{\,2}(e_{pq})=\widehat{ds}^{\,2}(e_{qp}).
$$

### FT.24 — The minimal fermion pins the geometry quantum

**Thm.** Let $c=(e_1,e_2)$, $e_1=(p,q)$, $e_2=(q,p)$, be a materialized 2-cycle — the minimal closed chain [A1 excludes self-loops; D1.4; Def-H.4 floor: $\delta h(c)\ge2$]. Write $\widehat{ds}^{\,2}(e_1)=\widehat{ds}^{\,2}(e_2)=:\kappa$ [FT.23]. Then:
$$(1)\quad\Theta(c)=2\kappa\in2\mathbb Z\ \ [\mathrm{FT.22}]\implies\kappa\in\mathbb Z\qquad(\text{per-edge integrality at the materialized fermion floor});
$$
$$(2)\quad ds^2(e)=\kappa\,\mathfrak h^2\in\mathfrak h^2\,\mathbb Z\qquad(\text{line element quantized in hop quanta}\ [\mathrm{D1.6}]);
$$
$$(3)\quad\mathfrak h^2=4\,G_N\ln2\ \ [\mathrm{CT2.9}]\implies ds^2(e)=4\kappa\,G_N\ln2\qquad(\text{interval quantum}=\text{one Bekenstein bit-area}\ [\mathrm{CT1.29}]\ \text{per unit}\ \kappa);
$$
$$(4)\quad\text{minimal real edge}\ [\mathrm{D1.1},\ \text{Comm-min}]:\ \kappa=1\ \text{attained}\ (\text{floor tight});\qquad\kappa=0\iff\text{null edge}\ [\mathrm{CT1.19a}]\ (\text{degenerate floor};\ \text{all-null transit chains are the trivial chains}=\text{photons/gluons}\ [\mathrm{D1.7},\ \mathrm{D3.7}]);\qquad\kappa<0:\ \text{timelike}\ [\mathrm{CT1.12}:\ \operatorname{sig}(g)=(-,+,+,+)].
$$

### FT.14 — Spin–charge decomposition

**Thm.** $c$ oriented chain, $\delta h(c)\ge2$ [Def-H.4], proper separation $\Delta\ell(c)$ [CT1.12]. Decompose $N_{\mathrm{visible}}=\delta h(c)$ bits under the complete force audit [FT.11]:
$$(1)\ \ N_{\mathrm{spin}}=N_{\mathrm{weak}};\qquad(2)\ \ N_{\mathrm{charge}}=N_{\mathrm{visible}}-N_{\mathrm{weak}};\qquad(3)\ \ f_{\mathrm{charge}}=\frac{N_{\mathrm{charge}}}{N_{\mathrm{visible}}},\quad f_{\mathrm{spin}}=\frac{N_{\mathrm{weak}}}{N_{\mathrm{visible}}};$$
$$
\mathfrak h\to0,\ \Delta\ell\ \text{fixed}\ [\mathrm{CT1.19}]:\quad f_{\mathrm{charge}}\to0,\quad f_{\mathrm{spin}}\to1 .
$$

### Def-H.9 — Subnetwork coarse-graining projection

**Def.** $\Sigma$ bounded subnetwork, designated terminus $v$ [Def-H.4]. $\mathcal M(\Sigma):=$ valid microscopic configurations (signs $\sigma_e$ [CT0.9], geometric data $\widehat{ds}^{\,2}(e)$ [D1.6] — integer on-shell [FT.24–FT.25], generic $O(1)$ real off-shell [CT1.19a] — subject to rung masks and Janus balance D1.3). Projection $\Pi_v:\mathcal M(\Sigma)\to\mathcal Q_v=(q,\mathbf S,m_{\mathrm{hid}})$:
$$(1)\ \ q:=\tfrac12(\sigma_s-\sigma_t)\ [\mathrm{EM.9}];
$$
$$(2)\ \ E_{\mathrm{tot}}(C):=|\Sigma|\,\ln2,\quad|\Sigma|:=\#\{\text{real edges touching}\ \Sigma,\ \text{internal}+\text{boundary}\}\ \ (\text{ledger-retained bits, locked content included}\ [\mathrm{CT4.3}]);
$$
$$
E_{\mathrm{vis}}(\gamma):=\min\bigl(\delta h(\gamma),\ 4\,\delta\tau(\gamma)\bigr)\ln2\ [\mathrm{FT.1}];\qquad
I_{\mathrm{hid}}:=E_{\mathrm{tot}}-E_{\mathrm{vis}};\qquad
m_{\mathrm{hid}}:=I_{\mathrm{hid}}/\mathfrak h;
$$
$$(3)\ \ \Theta_{\mathrm{int}}(C):=\!\!\sum_{e\in\Sigma\setminus\partial\Sigma}\!\!\widehat{ds}^{\,2}(e);\qquad
\mathrm{Hol}_{\mathrm{int}}:=e^{i\pi\Theta_{\mathrm{int}}}=(-1)^{\Theta_{\mathrm{int}}}\in\{\pm1\}
$$
$$
[\text{on-shell}\ \Theta_{\mathrm{int}}\in\mathbb Z\ \text{— derived from materialization, not postulated}:\ \mathrm{FT.25};\ \alpha=\pi:\ \mathrm{FT.9};\ \text{completion scope}:\ \text{Open Gaps 13}];
$$
$$
\mathbf S:\ \text{the}\ \mathfrak{su}(2)\ \text{Casimir label}\ j(j{+}1)\ \text{associated with}\ \mathrm{Hol}_{\mathrm{int}}\ \text{under the weak action}\ [\mathrm{FT.13}]\quad(\text{extraction rule OPEN — Open Gaps 11}).
$$

### Def-H.14 — General-edge sector space (internal-edge slot object)

**Def.** For any real edge $e$ (boundary or internal to any $\Sigma$), let $\mathcal E(e):=\mathcal E_{++}(e)\oplus\mathcal E_{+-}(e)\subset\mathfrak H(\mathbb C^4)_e$ be $e$'s own $S$-even pair sector [CT1.1, CT1.2] — the space with coordinates $(a_{00}(e),q_{ij}(e),w_i(e))$ [D2.1] that already fix $g_{\mu\nu}(e)$ [CT1.12] and hence $\widehat{ds}^{\,2}(e)$ [D1.6]. For $\Sigma$ a bounded subnetwork:
$$
\mathcal H_{\mathrm{slot}}^{\mathrm{int}}(\Sigma):=\bigoplus_{e\in\Sigma\setminus\partial\Sigma}\mathcal E(e),\qquad\dim_{\mathbb R}\mathcal H_{\mathrm{slot}}^{\mathrm{int}}(\Sigma)=10\,|\Sigma\setminus\partial\Sigma|.
$$

### FT.25 — Internal holonomy is well-defined on-shell

**Thm.** $\Sigma$ a bounded subnetwork [Def-H.9]. Then:
$$(1)\quad\Sigma\setminus\partial\Sigma\ \text{decomposes edge-disjointly into materialized closed chains}\ \{c_i\}:\qquad\Theta_{\mathrm{int}}(\Sigma)=\sum_i\Theta(c_i)\in2\mathbb Z,\qquad\mathrm{Hol}_{\mathrm{int}}=(-1)^{\Theta_{\mathrm{int}}}=+1\ \ [\mathrm{FT.22}];
$$
$$(2)\quad\text{every internal edge carries on-shell integer line element}\ [\mathrm{FT.24};\ \text{scope}:\ \text{Open Gaps 13}]:\qquad\Theta_{\mathrm{int}}(\Sigma)\in\mathbb Z,\qquad\mathrm{Hol}_{\mathrm{int}}=(-1)^{\Theta_{\mathrm{int}}}\in\{\pm1\}\ \ \text{well-defined};
$$
$$(3)\quad\text{the surviving on-shell integer label is the winding}\ k(c)=\Theta(c)/2\in\mathbb Z\ \ [\mathrm{FT.22}];\ \ \text{at the floor}\ k=\kappa\ \ [\mathrm{FT.24}(1)];\ \ \text{full materialized loops have}\ \mathrm{Hol}_{\mathrm{spiral}}=+1,\ \text{so the binary}\ \mathrm{Hol}_{\mathrm{int}}\ \text{is nontrivial only on partial-chain internal sets (proper subsets of materialized chain edges), where}\ \Theta_{\mathrm{int}}\ \text{is a partial sum of integers with free parity}.
$$

### FT.15 — Coarse-graining invariance

**Thm.** $C_1,C_2\in\mathcal M(\Sigma)$ sharing boundary signature $(\delta h,\delta\tau)$, boundary charge $q$, and $\Theta_{\mathrm{int}}$:
$$
\Pi_v(C_1)=\Pi_v(C_2)\qquad(\text{invariance under internal rearrangement}).
$$

**Cor FT.15.1 (self-averaging).** $(q,\mathbf S,m_{\mathrm{hid}})$ are the unique self-averaging macroscopic observables of $\Sigma$: as temperature depends only on total kinetic energy, invariant under permutation of molecular velocities, the fermionic quantum numbers depend only on boundary channel capacity and total internal holonomy — invariant under permutation of individual internal edge phases.

### FT.16 — The single-vertex hidden-information gap is generic; strong's signature is contraction-incompleteness

**Thm.** $v$ observed by a single neighbour through one incident edge ($\delta\tau\ge1$):
$$
I_{\mathrm{hid}}(\{v\})=(n(v)-1)\ln2\qquad(\text{aspect-blind});
$$
$\neg$strong-specific (nonzero already at $n=2$, where strong $\notin\mathcal A(2)$ [CT0.13]); strong's distinguishing signature is structural: contraction-completeness [CT3.17/18/22], $\neg$ a bit count.

### Def-H.35 — Channel-visible content (the boundary-transport read)

**Def.** $\Sigma$ a finite vertex set; $o\notin\Sigma$ a single external vertex whose only contact is its own incident edges into $\Sigma$, so $\gamma(o,\Sigma)=E_{\mathrm{bd}}$ [Def-H.1], over an interval $(\delta h,\delta\tau)$ [D0.6, D0.7]. The **channel-visible content** of $\Sigma$ to $o$ is the boundary registration sum
$$
E_{\mathrm{vis}}(\gamma)\ :=\ \sum_{e\in E_{\mathrm{bd}}}1\ \text{bit}\ =\ |E_{\mathrm{bd}}|\ln2\ \ \text{nats}\qquad[\mathrm{CT0.9}:\ 1\ \text{real edge}=1\ \text{bit};\ \mathrm{D1.1}:\ \text{registrations are classical edge data};\ \mathrm{C9}],
$$
attained whenever a hop schedule within the channel capacity exists [$\delta h\le4\,\delta\tau$ jaw, CT0.6a; attainment on boundary sets: FT.153]. $I_{\mathrm{hid}}:=E_{\mathrm{tot}}-E_{\mathrm{vis}}$ [Def-H.9(2)] is evaluated with $E_{\mathrm{vis}}$ of this definition.

### FT.17 — Internal-edge lemma

**Thm.** $\Sigma$ finite vertex set; $o\notin\Sigma$ a single external vertex whose only contact is its own incident edges into $\Sigma$ (so $\gamma(o,\Sigma)=$ the $E_{\mathrm{bd}}$ boundary edges; no internal edges). Hypotheses: $E_{\mathrm{bd}}\le4\,\delta\tau(\gamma)$ [channel-capacity jaw, CT0.6a: the channel does not clip $o$'s view]; channel-visible content per Def-H.35's edge-transport read, attained by FT.153. Then
$$
I_{\mathrm{hid}}(\Sigma)=E_{\mathrm{int}}\,\ln2\qquad(\text{exactly; aspect-blind}).
$$

### Def-H.39 — The mass-read registry; bridge slots

**Def.** The corpus's mass reads form a registry of species; a **bridge** between two species is a map carrying a dimensional factor (a power of $\mathfrak h$) and a numeric coefficient. The registry records the loci; no bridge is constructed, and none may be silently assumed.
$$(1)\ \text{informational}:\quad m_{\mathrm{hid}}=I_{\mathrm{hid}}/\mathfrak h\qquad[\mathrm{Def\text{-}H.9}(2);\ \mathrm{FT.16},\mathrm{FT.17};\ \ [m_{\mathrm{hid}}]=\mathfrak q^{+1/2}];$$
$$(2)\ \text{pole/defect}:\quad m^2_{\mathrm{pole}}\qquad[\mathrm{Def\text{-}H.37}\ \text{— forward pointer, Tier F.17};\ \mathrm{D2.5}\ \text{vocabulary};\ \ [m^2_{\mathrm{pole}}]=\mathfrak q];$$
$$(3)\ \text{inertial/tilt}:\quad m_i^2(q)=\Delta S(q)\qquad[\mathrm{L3}(4),\mathrm{L4};\ \text{Part 1};\ \text{dimensionless nats}];$$
$$(4)\ \text{sector-expectation}:\quad m^2_B(q,S)\qquad[\mathrm{Def\text{-}H.32}(6)\ \text{— forward pointer, Tier F.36};\ \text{dimensionless nats}];$$
$$(5)\ \text{1-loop}:\quad m_i^2=V_{\mathrm{eff}}(\varepsilon_q^{(i)})/8\qquad[\mathrm{Def\text{-}H.31}(6)\ \text{— forward pointer, Tier F.35};\ \mathrm{L3}(2):\ V=8\,\Delta S;\ \text{dimensionless nats}].$$

### Def-H.40 — Chain-level tilt composition

**Def.** Let $c$ be a materialized bound chain / floor with $E_{\mathrm{int}}$ internal edges [Def-H.9]. Ledger facts (derived): every internal edge entered $\mathcal R$ through exactly one $J^+$ seal [D1.2: crystallization $n_{\mathcal R}:0\to1$; D1.4: chain edges $\in E_{\mathcal R}$]; every A4 crystallization event applies exactly one Gibbs tilt step to the pair state of that event [L0(2), its declared theorem-local dynamical scope]; the ledger counts tilt steps [L0(4)].

### FT.18 — Contraction-completeness is not $\Sigma$-local

**Thm.** $\Sigma\supseteq\{v_1,v_2,v_3\}$ triplet-carrying [D3.8], no antitriplet in $\Sigma$. $\exists\,C,C'\in\mathcal M(U)$ [D2.11] with $C|_\Sigma=C'|_\Sigma$ (identical restriction) such that $\mathcal C(\Sigma;C)=1$ and $\mathcal C(\Sigma;C')=0$ [Def-H.10]. Contraction-completeness is $\neg$ a function of $\mathcal M(\Sigma)$ alone.

### Def-H.10 — Colour boundary and the contraction-completeness projector

**Def.** $C\in\mathcal M(U)$ valid. For $v\in\mathrm{Colour}(U):=\{u\in\mathcal Q:\ u\ \text{carries a colour attachment}\ [\mathrm{D3.8}]\}$, let $\pi_C(v)\subseteq\mathrm{Colour}(U)$ be the other members of $v$'s elementary invariant contraction group under $C$ (one for a meson pair via $\delta^i{}_j$; two for a (anti)baryon triple via $\varepsilon_{ijk}/\varepsilon^{ijk}$). $\pi_C$ total on $\mathrm{Colour}(U)$ for valid $C$ [CT3.18 + D2.11 applied to the colour ledger]. For $\Sigma$: $\mathrm{Colour}(\Sigma):=\mathrm{Colour}(U)\cap\Sigma$;
$$
\partial_{\mathrm{col}}(\Sigma;C):=\{v\in\mathrm{Colour}(\Sigma):\ \pi_C(v)\not\subseteq\Sigma\};\qquad
\mathcal C(\Sigma;C):=\begin{cases}1&\partial_{\mathrm{col}}(\Sigma;C)=\varnothing\\ 0&\text{otherwise}\end{cases};
$$
$$
\Pi_{\mathcal C}(\Sigma;C):=\mathcal C(\Sigma;C)\cdot\mathbb I_\Sigma^{(\mathrm{strong})}\qquad(\text{Hermitian idempotent};\ \text{matches}\ \mathcal P_M^{(n)}\ [\mathrm{CT0.14}]\ \text{and}\ \Pi_v\ [\mathrm{Def\text{-}H.9}]).
$$

### FT.19 — Confinement is an all-or-nothing subnetwork property

**Thm.**
$$
F_{\mathrm{strong}}^\Sigma(C):=\Pi_{\mathcal C}(\Sigma;C)\,F_{\mathrm{strong}}\big|_\Sigma\,\Pi_{\mathcal C}(\Sigma;C);\qquad
\mathcal C(\Sigma;C)=0\implies F_{\mathrm{strong}}^\Sigma(C)=0
$$
— regardless of how many colour-carrying vertices $\Sigma$ contains, and even if $|\partial_{\mathrm{col}}(\Sigma;C)|=1$.

### Def-H.11 — Active aspect set of a subnetwork

**Def.**
$$
\mathcal A(\Sigma;C):=\bigl\{A\in\mathbf F:\ A\ \text{contributes nonzero physically observable content to}\ \Sigma\text{'s coarse-grained description under}\ C\bigr\},
$$
read against two channels: nonzero value in $\Sigma$'s coarse-grained tuple $(q,\mathbf S,m_{\mathrm{hid}})$ [Def-H.9] (*charge-type*), or nonzero surviving support under $\Pi_{\mathcal C}(\Sigma;C)$ [FT.19] (*selection-type*: strong). Subnetwork analogue of D1.12's $\mathcal A(n)$: $\mathcal A(n)$ asks which aspects act nontrivially on one vertex's slot algebra; $\mathcal A(\Sigma)$ asks which survive coarse-graining and masking as observables on $\Sigma$ as a whole.

### Def-H.36 — The scalar-row fold (the H read at $\Sigma$-level)

**Def.** The coarse-grained tuple $(q,\mathbf S,m_{\mathrm{hid}})$ [Def-H.9] carries no independent H slot. The $\Sigma$-level observable content of the scalar-trace-mode aspect — $F_H=\operatorname{span}\{\Sigma\}$, $\dim F_H=1$ [A8, CT0.12] — is read through the mass component:
$$
\mathrm H\in\mathcal A(\Sigma;C)\iff\text{the G-row criterion holds}\ \bigl(I_{\mathrm{hid}}(\Sigma;o)\ne0\bigr)\qquad[\mathrm{FT.20}\ \text{table}].
$$

### FT.20 — Reduction of $\mathcal A(\Sigma)$ to proven per-aspect criteria

**Thm.**
$$
\begin{array}{c|c|c|c}
\text{aspect} & \in\mathcal A(\Sigma;C)\iff & \text{locality} & \text{basis}\\ \hline
\mathrm{EM} & \exists v\in\Sigma:\ f_v\ne0 & \Sigma\text{-local, additive} & \mathrm{D3.3},\ \mathrm{EM.9},\ \mathrm{CT3.22}\ \text{step 4}\\
G\ (\text{mass}) & I_{\mathrm{hid}}(\Sigma;o)\ne0 & \text{observer-relative}\ (\text{inherits Def-H.9}) & \mathrm{Def\text{-}H.9},\ \mathrm{FT.16},\ \mathrm{FT.17}\\
H & \text{folded into}\ G\ [\mathrm{Def\text{-}H.36}] & \text{as}\ G & \mathrm{EW.13},\ \mathrm{EW.20},\ \mathrm{EW.33}\\
W\ (\text{spin}) & \Theta_{\mathrm{int}}(\Sigma)\ne0\implies\Sigma\setminus\partial\Sigma\ne\varnothing\ \ (\text{one-directional}) & \Sigma\text{-local, intrinsic} & \mathrm{Def\text{-}H.9}(3),\ \mathrm{FT.13},\ \mathrm{FT.25}\\
D^+ & \text{never (independently)} & \text{uniform} & \mathrm{D4.3}\\
D^- & \text{never (independently)} & — & \mathrm{CT4.4}\\
J^\pm & \text{never} & \text{seals},\ \neg\text{charges} & \mathrm{CT0.7}\\
\mathrm{strong} & \mathrm{Colour}(\Sigma)\ne\varnothing\ \wedge\ \mathcal C(\Sigma;C)=1 & \text{genuinely global} & \mathrm{Def\text{-}H.10},\ \mathrm{FT.19}
\end{array}
$$

### Def-H.12 — Coarse-grained slot algebra

**Def.** $\Sigma$ a bounded subnetwork, $\partial\Sigma:=\{e\in\mathcal R:\ e$ has exactly one endpoint in $\Sigma\}$ [D2.11/CT1.29 separating-surface reading, as already used in Def-H.9(2)/Def-H.10]. Let $N(\Sigma):=|\partial\Sigma|$. The **coarse-grained slot algebra** of $\Sigma$ is
$$
\mathcal H_{\mathrm{slot}}(\Sigma):=\operatorname{span}_{\mathbb C}\{|e\rangle:\ e\in\partial\Sigma\}\cong\mathbb C^{N(\Sigma)},
$$
one basis ket per boundary edge — the direct generalization of D3.1's "one ket per incident real edge," taken over $\Sigma$'s external interface in place of a single vertex's incident set.

### Def-H.13 — Compositional bridge map $\iota_\Sigma$

**Def.** For each $e\in\partial\Sigma$, let $w_e$ be $e$'s endpoint outside $\Sigma$, with its own rung $n(w_e)$, existing bridge map $\iota_{n(w_e)}$ [D2.12], and $e$'s own edge-local pair-channel decomposition [CT0.12, rung-independent, fixed 16-dim block]. Define $\iota_\Sigma:\mathfrak u(N(\Sigma))\to\mathcal K$ by requiring, on the slot direction $|e\rangle$, that $\iota_\Sigma$ **factor through** the pair $\bigl(\text{CT0.12's block for }e,\ \iota_{n(w_e)}\bigr)$:
$$
\iota_\Sigma\big|_{|e\rangle}:=\bigl(\text{CT0.12 pair-block map for }e\bigr)\,\otimes\,\iota_{n(w_e)}\qquad(e\in\partial\Sigma),
$$
extended linearly across $\partial\Sigma$. **No independent embedding is postulated**: every component of $\iota_\Sigma$ is inherited, edge-by-edge, from machinery that already exists at the single-edge (CT0.12) and single-vertex (D2.12) level.

**"Strictly new at $\Sigma$" (generalizes D3.2).** A piece of $\mathfrak u(N(\Sigma))$ is strictly new at $\Sigma$ iff it does **not** factor through $\iota_\Sigma$ as defined above — i.e. iff it is a genuinely collective effect of $\Sigma$'s boundary edges taken together, not a sum/tensor of independent single-edge and single-vertex facts already accounted for at lower structural levels. This is the precise sense in which the coarse-graining machine treats $\Sigma$ "as a single quantum object": an aspect belongs to $\mathcal A(\Sigma)$ properly only if its action on $\mathcal H_{\mathrm{slot}}(\Sigma)$ resists the boundary-edgewise factorization $\iota_\Sigma$ provides for free.

### Def-H.15 — Coarse-grained aspect space and masked force operator

**Def.** $\Sigma$ a bounded subnetwork; $C\in\mathcal M(U)$ the ambient configuration [D2.11].
$$(1)\quad\mathcal K_\Sigma(C):=\bigoplus_{A\in\mathcal A(\Sigma;C)}\mathcal K^{(A)}\qquad[\text{the aspect blocks of D2.3; membership by FT.20's criteria table}];$$
$$(2)\quad\mathcal P_M^{(\Sigma)}(C):\mathcal K\to\mathcal K_\Sigma(C)\qquad(\text{orthogonal projection}\ [\mathrm{D2.3}/\mathrm{CT2.2}\ \text{pattern}]);$$
$$(3)\quad\mathbf F_M^{(\Sigma)}(C):=\mathcal P_M^{(\Sigma)}\,\mathbf F\,\mathcal P_M^{(\Sigma)}\qquad[\mathrm{A8}/\mathrm{C7},\ \mathrm{CT2.3}\ \text{pattern}],$$
with the strong summand admissibility-filtered:
$$F_{\mathrm{strong}}\ \longmapsto\ \Pi_{\mathcal C}(\Sigma;C)\,F_{\mathrm{strong}}\big|_\Sigma\,\Pi_{\mathcal C}(\Sigma;C)\qquad[\mathrm{Def\text{-}H.10},\ \mathrm{FT.19}];$$
$$(4)\quad\text{realization}:\ \iota_\Sigma\ [\mathrm{Def\text{-}H.13}]\ \text{maps}\ \mathfrak u(N(\Sigma))\ \text{into}\ \mathcal K_\Sigma\text{'s boundary-coupled part}\ [\mathrm{FT.21}];\ \text{on-shell internal labels}\ (\Theta_{\mathrm{int}},k)\ [\mathrm{FT.25},\ \mathrm{FT.22}]\ \text{superselect the}\ W/G\ \text{reads of Def-H.9's tuple; off-shell, blocks carry arena data}\ [\mathrm{CT1.19a},\ \mathrm{Def\text{-}H.18}].$$

### FT.21 — $\mathcal A(\Sigma)$'s charge-type rows, properly derived

**Thm.** $(i)$ **EM — boundary-exact.** FT.20's EM-row *observable* is boundary-expressible: the tuple read $q=\tfrac12(\sigma_s-\sigma_t)$ [Def-H.9(1), EM.9] reads end signs on $\partial\Sigma$'s terminal edges, and interior vertex activity telescopes into end reads [EM.9b (Part 2): the identity, with its type-$(1,1)$ domain] — so the row's criterion ($\exists v\in\Sigma:\ f_v\ne0$) can exceed what is separately observable at the boundary, while its observable content factors through $\iota_\Sigma$'s per-edge CT0.12 factor [Def-H.13]. $(ii)$ **$G/H$ — boundary-expressible modulo one declared interior label.** $I_{\mathrm{hid}}(\Sigma;o)=(E_{\mathrm{int}}+E_{\mathrm{bd}})\ln2-E_{\mathrm{vis}}$, where $E_{\mathrm{bd}}=N(\Sigma)=\dim\mathcal H_{\mathrm{slot}}(\Sigma)$ [Def-H.12 Rmk] and $E_{\mathrm{vis}}=\min(\delta h(\gamma),4\,\delta\tau)\ln2$ is a boundary/channel sum [FT.1]; $E_{\mathrm{int}}=|\Sigma\setminus\partial\Sigma|$ is $\Sigma$'s own interior volume datum — a single integer carried as a c-number label alongside $\mathcal H_{\mathrm{slot}}(\Sigma)$, of the same species as Def-H.15(4)'s superselection labels $(\Theta_{\mathrm{int}},k)$, and $\neg$factored through $\iota_\Sigma$ edge-wise. $(iii)$ Consequently both rows are instances of CT0.13's active-aspect machine on $\mathcal H_{\mathrm{slot}}(\Sigma)$ — EM exactly, $G/H$ modulo the declared interior label — not case-by-case arithmetic extensions.

### Def-H.16 — Coarse-grained resolvent and the $\Sigma$-spectrum

**Def.**
$$Z(\mathcal R,\Sigma):=\Bigl\langle\mathrm{out}\Bigl|\bigl(1-\mathbf F_M^{(\Sigma)}\bigr)^{-1}\Bigr|\mathrm{in}\Bigr\rangle\qquad[\mathrm{D2.4}\ \text{pattern};\ \mathrm{D2.8}\ \text{sheet}],$$
with $|\mathrm{in}\rangle,|\mathrm{out}\rangle$ read on boundary-channel states via $\iota_\Sigma$ [Def-H.13] — a constitutive clause of this definition (the $\iota_\Sigma$ boundary-state identification). Poles of $Z(\mathcal R,\Sigma)$ $:=$ the $\Sigma$-spectrum [D2.5 pattern]: pole $\iff1\in\operatorname{spec}\mathbf F_M^{(\Sigma)}$ [CT2.5 pattern]; residues $=$ transition amplitudes; $m^2:=$ pole displacement [D2.5]. A bound chain $c$ interior to $\Sigma$ **materializes** (FT.22's sense) iff it contributes to a pole of $Z(\mathcal R,\Sigma)$: FT.22's single-valuedness condition *is* this resolvent's eigenmode condition [CT2.5 as applied in EW.18].

### FT.26 — Structural transfer: the $\Sigma$-mask inherits CT2.3–CT2.5

**Thm.** $\mathbf F_M^{(\Sigma)}(C)$ is: $(1)$ Hermitian; $(2)$ block-diagonal, $\mathbf F_M^{(\Sigma)}=\bigoplus_{A\in\mathcal A(\Sigma;C)}F_A\big|_{\mathcal K^{(A)}}$, the strong summand $\equiv0$ whenever $\mathcal C(\Sigma;C)=0$; $(3)$ finite-dimensional with
$$\dim\mathcal K_\Sigma\ \le\ 1+5+1+3+8\ =\ 18\ <\ \infty .$$
Hence the spectral theorem applies and $Z(\mathcal R,\Sigma)$ has simple poles exactly at $1\in\operatorname{spec}\mathbf F_M^{(\Sigma)}$, residues $-\langle\mathrm{out}|P_a|\mathrm{in}\rangle$ — CT2.5's statement transferred verbatim with $n\mapsto\Sigma$.

### FT.27 — Single-vertex degeneration; action versus observable

**Thm.** At $\Sigma=\{v\}$: $(a)$ the spaces degenerate on the nose — $\mathcal H_{\mathrm{slot}}(\{v\})=\mathcal H^{(n(v))}_{\mathrm{slot}}$ [Def-H.12], $\mathcal H^{\mathrm{int}}_{\mathrm{slot}}(\{v\})=0$ [Def-H.14], $\iota_{\{v\}}=\iota_{n(v)}$ [Def-H.13]; $(b)$ FT.20's criteria evaluated at $\{v\}$ agree with CT0.13's active set on the EM row (for type-$(1,1)$ states), and refine it on four rows — each refinement a proven fact, not a deviation:
$$
\mathrm{EM}\in\mathcal A(\{v\};C)\iff f_v\ne0\qquad(\text{CT0.13's type-}(1,1)\ \text{condition}\ [\mathrm{D3.3}]);
$$
$$
G\in\mathcal A(\{v\};C)\iff I_{\mathrm{hid}}(\{v\};o)\ne0\iff n(v)\ge2\qquad[\mathrm{FT.16}:\ I_{\mathrm{hid}}=(n{-}1)\ln2]\ —\ \text{refines}\ G\in\mathcal A(1):\ \text{at}\ n=1\ \text{the block acts but no observable exists};
$$
$$
W\in\mathcal A(\{v\};C)\iff\text{never}\qquad[\Theta_{\mathrm{int}}(\{v\})=0:\ \text{empty sum},\ \mathrm{Def\text{-}H.14}]\ —\ \text{weak acts from rung}\ 1\ [\mathrm{CT0.13}]\ \text{but its observable is born only at the bound floor}\ (\mathrm{FT.28});
$$
$$
\text{strong}\in\mathcal A(\{v\};C)\iff\text{never}\qquad[\text{case split}:\ \mathrm{Colour}(\{v\})=\varnothing\ (v\ \text{colourless})\implies\text{FT.20's first conjunct fails}\ \wedge\ F_{\mathrm{strong}}\big|_{\{v\}}=0\ (\neg\exists\ \text{colour content});\quad\mathrm{Colour}(\{v\})=\{v\}\implies\pi_C(v)\subseteq\{v\}\ \text{impossible}\ [\mathrm{A1}:\ \text{partners distinct}]\implies\mathcal C(\{v\};C)=0\implies\text{block}\equiv0\ [\mathrm{FT.19}]]\ \text{—}\ \text{either way the strong block is zero at a single vertex};\ \text{the smallest colour-observable}\ \Sigma\ \text{is the sealed meson-type pair}\ [\mathrm{D3.9},\ \mathrm{CT3.17};\ \text{realized at}\ \mathrm{FT.28}\ \mathrm{Rmk}];
$$
$$
J^\pm,D^\pm\notin\mathcal A(\{v\};C)\ \ \forall n\qquad[\mathrm{FT.20}\ \text{reclassification}].
$$

### Def-H.17 — Strong edge transport

**Def.** For $e\in E_{\mathcal R}$ incident on colour-carrying vertices (rung-3 attachments [D3.8]):
$$
G^{(3)}(e)\ :==\ G^{(2)}(e)\ \otimes\ \tau(e),\qquad
G^{(2)}(e)=\sigma_e\,e^{i\pi\,\widehat{ds}^{\,2}(e)}\quad[\mathrm{D3.5},\ \mathrm{FT.9}],
$$
$\tau(e):=$ the slot-index transport of $e$ on $\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3$ [D3.1, CT3.2], acting in the defining representation [CT3.11(2)–(3): triplet $\mapsto U^i{}_jq^j$, antitriplet $\mapsto r_j(U^{-1})^j{}_i$, $U\in SU(3)$], algebra image in $\iota_3(\mathfrak u(3))$ [D2.12]. Strictly-new strong content: $\pi(\tau)\in\mathfrak{su}(3)$, $\pi(X)=X-\tfrac{\mathfrak T(X)}{3}I_3$ the trace projection [CT3.7, D3.2] — the $\mathfrak u(1)$ centre of $\mathfrak u(3)$ is EM's, spent at rung 2 [CT3.7, CT3.13; CT0.13 step $n{=}3$], and already carried by $G^{(2)}$'s phase factor.

### FT.29 — Strong weight: factorization, no $\alpha_{\mathrm{strong}}$, observable sealing

**Thm.**
$$(1)\quad\text{factorization}:\ G^{(3)}(e)=G^{(2)}(e)\otimes\tau(e)\ [\mathrm{Def\text{-}H.17}],\qquad\alpha_{\mathrm{EM}}^{(3)}=\alpha_{\mathrm{EM}}^{(2)}=\pi\ [\mathrm{EM.18},\ \mathrm{CT3.10}];$$
$$(2)\quad\text{non-existence}:\ \neg\exists\ \text{per-edge abelian strong phase coefficient}\ (\text{an}\ ``\alpha_{\mathrm{strong}}\text{''})\ [\textbf{CT3.10a (F)}:\ \text{trace route};\ \text{eight-dimensional obstruction to a scalar coefficient read};\ \text{non-canonicity of}\ \mathfrak u(1)\subseteq\mathfrak{su}(3)\ \text{choices (explicit}\ SU(3)\ \text{witnesses)};\ \text{centre identification via CT3.7/CT3.13}];
$$
$$(3)\quad\text{observable content}:\ \text{under any pole read}\ [\mathrm{CT2.5}],\ \tau(e)\text{-factors survive only inside invariant contractions}\ \{\delta^i{}_j,\varepsilon_{ijk},\varepsilon^{ijk}\}\ [\mathrm{CT3.17}];\ \text{free indices are mask-annihilated}\ [\mathrm{CT3.18}];\ \text{isolated triplets have}\ \neg\text{pole and norm}\ 0\ [\mathrm{CT3.22},\ \mathrm{CT2.8}];\ \text{at}\ \Sigma\text{-level the strong summand is gated by}\ \Pi_{\mathcal C}(\Sigma;C)\in\{0,1\}\ [\mathrm{FT.19},\ \mathrm{FT.26}(2)].\ \text{Hence the effective strong weight of any materialized configuration}=(\text{its}\ G^{(2)}\ \text{factors})\times(\text{singlet-sealing factor}):\ \neg\exists\ \text{per-edge strong phase read}.
$$

### Def-H.18 — Arena and spectrum (the two-locus vocabulary)

**Def.** The **arena** of a quantity $:=$ the configuration domain over which $Z(\mathcal R)$ sums [A8, C12: $\mathfrak C(\mathcal R)$] — off-shell; continuous wherever CT1.12/CT1.19a make it so. The **spectrum** of a quantity $:=$ its values on materialized configurations — those contributing to poles of the masked resolvent [D2.4, CT2.5; $\Sigma$-level: Def-H.16] — on-shell. **Two-locus principle** (vocabulary for an already-proven distinction): discreteness claims in this corpus are spectrum claims; continuity claims are arena claims. One and the same object may be continuous in the arena and quantized in the spectrum — CT2.5 (continuous operator families, discrete pole set) and FT.22–FT.25 (continuous $\mathcal E(e)$ arena [Def-H.14 Rmk], integer winding spectrum) are the two proven instances. Vocabulary only — no new premise.

### FT.30 — Pair-channel sector quantum audit: $\bigl((5{+}3{+}1)+(3{+}3)+1\bigr)$

**Thm.** The $16$ pair-channel registers [CT0.6] tile as $(G_5+W_3+H_1)+(J^+_3+J^-_3)+D^+_1$ [CT0.12, CT1.1, CT1.2], and CT1.12's metric dictionary decomposes block-wise:
$$
g_{\mu\nu}\ \leftrightarrow\ \underbrace{\hat h_{ij}\ (5)}_{G:\ \text{spin-2 shear}}\ \oplus\ \underbrace{\Sigma_{\mathrm{tr}}\ (1)}_{H:\ \text{volume mode}}\ \oplus\ \underbrace{a_{00}\ (1)}_{D^+:\ \Omega\ \text{conformal}}\ \oplus\ \underbrace{w_i\ (3)}_{W:\ \text{shift}};\qquad
J^\pm\ (S\text{-odd}):\ 0\ \text{metric coordinates}\ [\mathrm{Def\text{-}H.14}:\ \mathcal E(e)\ \text{is}\ S\text{-even}].
$$
Independent-quanta audit:
$$
\begin{array}{c|c|c|c}
\text{block} & \text{arena data} & \text{spectrum data} & \text{independent quantum?}\\ \hline
G\ (5) & \text{continuous shear}\ [\mathrm{CT1.12}] & \text{winding}\ \kappa,k\in\mathbb Z\ [\mathrm{FT.22}/\mathrm{FT.24}],\ \text{unit}\ \mathfrak h^2=4G_N\ln2\ [\mathrm{CT2.9}] & \textbf{yes — geometric}\ (\text{joint read, }\neg\text{per-block})\\
W\ (3) & \text{shift}\ w_i\ [\mathrm{CT1.12}];\ \text{Casimir fixed}:\ \vee^2\,j{=}1,\ \wedge^2\,j{=}0\ [\mathrm{CT0.7a}];\ \text{seed}\ j{=}\tfrac12\ [\mathrm{EW.32}] & \text{integer labels}\ k,\ \Theta_{\mathrm{int}}\ [\mathrm{FT.25}(3),\ \mathrm{FT.28}(2)] & \textbf{candidate — spin}\ (\text{extraction open, Gaps 11});\ \neg\text{self-charge}\ [\mathrm{FT.12}]\\
H\ (1) & h_0\ \text{seed background},\ \text{continuous P4 data}\ [\mathrm{EW.13},\ \mathrm{P4}];\ M^2\propto h_0^2\ [\mathrm{EW.33}] & \text{via mass read only}\ [\mathrm{FT.20}\ \text{row}\ H,\ \mathrm{Def-H.36}] & \text{no — continuous configuration datum}\\
J^+\ (3) & \text{seals}\ n_{\mathcal R}:0\to1\ [\mathrm{D1.2}];\ S\text{-odd}=\text{reality grading}\ [\mathrm{CT0.7}] & \neg\text{observable}\ [\mathrm{FT.20}] & \text{no — structural};\ \#J^+=\#J^-\ [\mathrm{D1.3}/\mathrm{D2.11}];\ \neg\text{charges}\ [\mathrm{FT.11}]\\
J^-\ (3) & \text{dissolution seals}\ [\mathrm{D1.2}] & \neg\text{observable}\ [\mathrm{FT.20}] & \text{no — structural, as}\ J^+\\
D^+\ (1) & \Lambda\ \text{uniform centre}\ [\mathrm{A8},\ \mathrm{D4.3}];\ w=-1\ [\mathrm{CT1.25}];\ \Omega\ \text{channel entry}\ [\mathrm{Def\text{-}H.2}] & \neg\text{observable independently}\ [\mathrm{FT.20}] & \text{no — P4 datum}\\ \hline
\multicolumn{4}{c}{\text{stack aspects (outside the}\ 16\ [\mathrm{CT0.12\ Rmk}]):}\\
\mathrm{EM} & \sigma_e\ \text{binary}\ [\mathrm{CT0.9}];\ q\in\{-1,0,+1\}\ [\mathrm{EM.9}/\mathrm{D3.4}] & \text{parity}\ (-1)^\kappa\ \text{on-shell}\ [\mathrm{FT.24}] & \textbf{yes — charge}\ (\text{R1 reality line})\\
\text{strong} & \tau(e)\ \text{defining-rep label}\ [\mathrm{Def\text{-}H.17}];\ \neg\exists\ \text{per-edge phase}\ [\mathrm{FT.29}(2)] & \text{singlet sealing}\ \{0,1\}\ [\mathrm{FT.19}/\mathrm{FT.29}(3)] & \textbf{yes — admissibility}\ (\text{R3 selection})\\
D^- & \text{locked content}\ [\mathrm{D4.2}] & \neg\text{observable}\ [\mathrm{FT.3},\ \mathrm{CT4.4}] & \text{no}
\end{array}
$$

### FT.31 — The continuum limit survives on-shell quantization

**Thm.** Let $\{c_{\mathfrak h}\}$ be a family of materialized chains [FT.22] with $L=\mathfrak h\,n_{\mathcal R}$ fixed, $\mathfrak h\to0$ [CT1.19's regime]. Then:
$$(1)\quad\text{per edge}:\ \ \kappa_e=g_{\mu\nu}\dot x^\mu\dot x^\nu(\lambda_e)+O(\mathfrak h)\ \wedge\ \kappa_e\in\mathbb Z\ \text{on-shell}\ [\mathrm{FT.24}\ \text{scope}]:\ \text{integers sampling a smooth function with}\ O(\mathfrak h)\ \text{slack};$$
$$(2)\quad\text{sums}:\ \ \sum_e\kappa_e\mathfrak h^2=\sum_e ds^2(e)\ \text{identically}\ [\mathrm{D1.6}]\implies\mathrm{CT1.19}\ \text{applies verbatim}:\ \text{abs. error}\ O(\mathfrak hL),\ \text{rel.}\ O(\mathfrak h):\ \text{integrality adds no error term — selection acts on family membership, not on sums};$$
$$(3)\quad\text{selection in the limit}:\ \ \oint_c ds^2\in2\mathfrak h^2\mathbb Z\ [\mathrm{FT.22}\ \mathrm{Phys}];\qquad k=\frac{1}{2\mathfrak h^2}\oint_c ds^2\to\infty\ \text{at fixed classical loop}:\ \text{the lattice is classically invisible, quantally exact};$$
$$(4)\quad\text{floor relating equation (Gaps 2, minimal-edge class)}:\ \ \kappa_e\equiv1\ [\mathrm{D1.1},\ \text{Comm-min}]\implies\Theta(c)=\delta h(c)\ \text{and}\ \ \frac{S_{\mathrm{reg}}(c)}{\oint_c ds^2}=\frac{\delta h\ln2}{\delta h\,\mathfrak h^2}=\frac{\ln2}{\mathfrak h^2}=\frac{S_{\min}}{A_{\min}}\qquad[\mathrm{CT0.9},\ \mathrm{C9},\ \mathrm{CT1.29}].$$

### Def-H.19 — Stationary, stable, and unstable jumps (vocabulary)

**Def.** A **jump** $:=$ a transit path between two termini in the emergent chart [D0.6, CT2.6] — program vocabulary, no new structure. A **stationary jump**: $\delta\!\int_\gamma ds^2=0$ among fixed-endpoint variations — an affinely parametrized geodesic of $g_{\mu\nu}$ [CT1.20's stationary-phase read; Euler–Lagrange for $\int g_{\mu\nu}\dot x^\mu\dot x^\nu d\lambda$ — math]. A **stable jump**: a stationary jump that is a local minimum of $\int ds^2$ on its interval (no conjugate points [math: Morse/Synge]); **unstable**: stationary but saddle or maximal. Lorentzian read [CT1.12: $\operatorname{sig}=(-,+,+,+)$]: on timelike paths, minimizing $\int ds^2$ is *maximizing* proper time — the classical stable trajectory; on spacelike paths, shortest length. Program vocabulary (constitutive; Morse-theoretic [math]); the "relatively stable" idiom of program notes means: measured against the other stationary paths with the same endpoints — an internal comparison, no external scale.

### Def-H.37 — The defect-transfer interface

**Def.** The pole-side mass read of a materialized bound chain. Two clauses:
$(1)$ **Leading-order transfer.** For $c$ a materialized **spacelike** bound chain with weak-transport profile $c_A$ over the seed generator set [EW.33's $c_A$; EW.32's seed $\mathsf v\in\mathcal H_{\mathsf v}$], the chain's pole displacement takes EW.33's defect form for the seed weak-transported around $c$:
$$
m^2_{\mathrm{pole}}(c)=\hat\mu^2\,\ell_c^2\,G(c),\qquad
G(c)=\sum_{A,B}c_Ac_B\operatorname{Re}\langle\mathcal G_A\mathsf v,\mathcal G_B\mathsf v\rangle\ \ [\mathrm{EW.33}\ \text{Gram data};\ \mathrm{EW.20}],
$$
with $\hat\mu^2>0$ the floor-independent residue packaging $\varkappa^2\beta^2h_0^2$ (EW.33's $c_W$ with $\ell^2$ factored out), $[\hat\mu^2]=\mathfrak q^2$ [EW.33 packaging; D2.9; Cal-F], and uniform coupling profile along the chain (EW.33's own leading-order regime).
$(2)$ **Holonomy refinement.** The transfer of $(1)$ is Def-H.21's spin-connection holonomy: $\mathcal U_c=\mathcal U^{\mathrm{spin}}_c$ with frame angle $\Theta_R(c)$ [Def-H.21(5)–(6)]; then exactly
$$
m^2_{\mathrm{pole}}(c)=\hat\mu'^2\cdot4\sin^2\!\Bigl(\frac{\Theta_R(c)}{4}\Bigr),\qquad[\hat\mu'^2]=\mathfrak q\ \ [\mathrm{FT.54}(4)\ \text{packaging pattern};\ \text{Cal-F}],
$$
and clause $(2)$ implies clause $(1)$ at leading order under the matching $\hat\mu'^2\Theta_R^2/4=\hat\mu^2\ell_c^2G(c)$ — recorded, not imposed [FT.54(2), FT.33].

### FT.28 — First computation: the floor-fermion particle card

**Thm.** ($\Sigma_{\min}$ card.) Let $\Sigma_{\min}=\{p,q\}$ with the materialized 2-cycle $c=(e_1,e_2)$, $e_1=(p,q)$, $e_2=(q,p)$, as its interior [Def-H.4 floor; FT.24: $\kappa:=\widehat{ds}^{\,2}(e_1)=\widehat{ds}^{\,2}(e_2)\in\mathbb Z\setminus\{0\}$], observed by a single external neighbour $o$ through one real edge ($E_{\mathrm{bd}}=1$, $\delta\tau\ge1$; FT.17 hypotheses, Def-H.35). Then:
$$(1)\quad I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2=2\ln2,\qquad m_{\mathrm{hid}}=\frac{2\ln2}{\mathfrak h}\qquad[\mathrm{FT.17},\ \mathrm{Def\text{-}H.9}(2)];$$
$$(2)\quad\Theta_{\mathrm{int}}=\Theta(c)=2\kappa\in2\mathbb Z,\qquad k=\kappa,\qquad\mathrm{Hol}_{\mathrm{int}}=+1\qquad[\mathrm{FT.22},\ \mathrm{FT.24},\ \mathrm{FT.25}];$$
$$(3)\quad\mathcal A(\Sigma_{\min};C)\supseteq\{G,H,W\};\qquad\mathrm{EM}\in\mathcal A\iff f_p\ne0\ \vee\ f_q\ne0\ [\mathrm{D3.3}];$$
$$\text{strong}\notin\mathcal A\ \text{necessarily}:\ n(q)=2\implies q\ \text{carries no slot index}\ [\mathrm{D3.1},\ \mathrm{CT3.11}(1):\ \text{colour slots at}\ n{=}3\ \text{only}];\quad\mathrm{Colour}(\Sigma_{\min})=\{p\};\quad\pi_C(p)\subseteq\Sigma_{\min}\ \text{impossible}\ [\mathrm{A1}:\ \text{partners distinct}]\implies\mathcal C=0\implies\text{block}\equiv0\ [\mathrm{FT.19}]:\ \textbf{the single-contact floor fermion is structurally colourless}\ (\text{colour-visible variant}:\ \mathrm{Rmk}\ \text{below});$$
$$(4)\quad\dim\mathcal K_{\Sigma_{\min}}=9\ (G{+}W{+}H\ \text{core})\ +\ 1\cdot[\mathrm{EM}\ \text{active}]\ \le\ 10;\qquad\text{general bound}\ \le18\ [\mathrm{FT.26}(3),\ \mathrm{CT0.14}];\quad18\ \text{is attained only in the inside-sealed variant}\ [\mathrm{Rmk}\ \text{below}:\ 9{+}1{+}8];$$
$$(5)\quad n(p)=3\ [e_1\ \text{out},\ e_2\ \text{in},\ \text{observer edge in}],\quad n(q)=2\ [e_1\ \text{in},\ e_2\ \text{out}]\qquad[\mathrm{D0.8}];\quad D_{\mathrm{tick}}(3)=2^{4}=16=C_{\mathrm{cap}},\quad O(2)=O(3)=0\ [\mathrm{CT0.5},\ \mathrm{CT0.6}]:\ \text{no oversubscription anywhere at the floor}\ [\mathrm{CT0.11}];$$
$$(6)\quad q:\ \text{boundary-channel read; the closed core}\ (\partial c=0\ [\mathrm{D1.4}])\ \text{carries basepoint sign data}\ q_{\mathrm{core}}(c;v)=\tfrac12(\sigma_{e_1}-\sigma_{e_k})\in\{-1,0,+1\}\ [\mathrm{FT.40}:\ \text{ternary},\ \omega\text{-covariant}\ [\mathrm{D2.6}]];$$
$$(7)\quad Z(\mathcal R,\Sigma_{\min})\ \text{poles}\iff1\in\operatorname{spec}\mathbf F_M^{(\Sigma_{\min})}\ [\mathrm{FT.26}];\qquad c\ \text{materializes}\implies\Theta(c)=2\kappa\ [\mathrm{FT.22},\ \mathrm{Def\text{-}H.16}].$$

### FT.32 — The cycle floor family (single-contact $\Sigma_L$)

**Thm.** Let $\Sigma_L$ be a simple oriented $L$-cycle, $L\ge2$ [A1 excludes self-loops; D1.4], with materialized interior chain $c$ and a single observer contact at $v_1$ ($E_{\mathrm{bd}}=1\le4\,\delta\tau$, $\delta\tau\ge1$; FT.17 hypotheses, Def-H.35). Write $\kappa_e:=\widehat{ds}^{\,2}(e)$ for $e\in c$. Then:
$$(1)\quad E_{\mathrm{int}}=L,\qquad I_{\mathrm{hid}}=L\ln2,\qquad m_{\mathrm{hid}}=\frac{L\ln2}{\mathfrak h}\qquad[\mathrm{FT.17},\ \mathrm{Def\text{-}H.9}(2)];$$
$$(2)\quad n(v_1)=3,\ \ n(v_i)=2\ (i\ge2)\ [\mathrm{D0.8}];\qquad O(2)=O(3)=0,\ \ D_{\mathrm{tick}}(3)=16=C_{\mathrm{cap}}\ [\mathrm{CT0.5},\ \mathrm{CT0.6}];$$
$$(3)\quad\Theta_{\mathrm{int}}=\Theta(c)\in2\mathbb Z\ \text{if}\ c\ \text{materialized}\ [\mathrm{FT.22}];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}(1)];\qquad k=\Theta/2\in\mathbb Z;\qquad W\ \text{row fires}\iff\Theta\ne0;$$
$$(4)\quad\textbf{structural colourlessness}:\ \mathrm{Colour}(\Sigma_L)\subseteq\{v_1\}\ [\mathrm{D3.1}:\ \text{colour slots at}\ n{=}3\ \text{only};\ \mathrm{CT3.11}(1)];\ \ \pi_C(v_1)\subseteq\Sigma_L\ \text{impossible}\ [\mathrm{A1}:\ \text{partners distinct}]\implies\mathcal C=0\ \vee\ \mathrm{Colour}=\varnothing\implies\text{strong}\notin\mathcal A(\Sigma_L;C)\ \ \forall C;$$
$$(5)\quad\mathcal A(\Sigma_L;C)\supseteq\{G,H\}\ [G:\ I_{\mathrm{hid}}\ne0;\ H:\ \mathrm{Def-H.36}];\quad\mathrm{EM}\in\mathcal A\iff\exists i:\ f_{v_i}\ne0\ [\mathrm{D3.3}];\quad\dim\mathcal K_{\Sigma_L}=9\ (+1\ \mathrm{EM})\le10<18\ [\mathrm{FT.26},\ \mathrm{CT0.14}];$$
$$(6)\quad\text{minimality ladder for}\ \Theta(c)\ [\mathrm{FT.22}'\text{s constraint}\ \Theta\in2\mathbb Z]:\qquad\text{uniform-}\kappa:\ L\ \text{odd}\Rightarrow\kappa_{\min}=2,\ \Theta_{\min}=2L;\quad L\ \text{even}\Rightarrow\kappa_{\min}=1,\ \Theta_{\min}=L;$$
$$\text{all-nonnull per-edge-integral}\ [\text{scope}:\ \mathrm{FT.24}/\text{Open Gaps 13}]:\ \Theta_{\min}=L+(L\ \mathrm{mod}\ 2);\qquad\text{null-permitting}:\ \Theta_{\min}=2\ (\kappa\ \text{profile}\ (1,1,0,\dots,0)\ [\mathrm{CT1.19a}:\ \kappa=0\iff\text{null}]);$$
$$\text{scope}:\ \text{uniform/all-nonnull regimes presuppose per-edge}\ \kappa\in\mathbb Z\ —\ \text{derived at}\ L{=}2\ [\mathrm{FT.24}]\ \text{and on round-trip-closed edges}\ [\mathrm{FT.34}(4),\ \text{forward}],\ \text{conditional for bare}\ L\ge3\ \text{cycles}\ [\text{Open Gaps 13 class (iii)}:\ \mathrm{FT.22}\ \text{alone permits}\ \kappa\in(2/L)\mathbb Z];\qquad\text{unconditional floor}:\ \Theta_{\min}=2\ \ \forall L\ (\text{rational uniform witness}\ \kappa\equiv2/L);$$
$$(7)\quad\Pi(\Sigma_L)=L^2\,\Theta\,(\ln2)^2\ [\text{Open Gaps 7 diagnostic}];\qquad L=2\ \text{reproduces FT.28's card verbatim (consistency)}.$$

### FT.33 — The defect bridge: pole-side mass candidate in well-posed ratio form

**Thm.** Under Def-H.37(1) (interface transfer: the floor fermion's pole displacement takes EW.33's leading-order defect form for the seed $\mathsf v$ [EW.32] weak-transported around its materialized bound chain), for a materialized **spacelike** single-contact cycle floor $\Sigma_L$ with $\kappa_e>0$:
$$(1)\quad m_{\mathrm{pole}}^2(\Sigma_L)=\hat\mu^2\,\ell_c^2\;G(c),\qquad\ell_c=\mathfrak h\,\Lambda_c,\quad\Lambda_c:=\sum_{e\in c}\sqrt{\kappa_e}\ \ (\text{dimensionless});$$
$$G(c)=\sum_{A,B}c_Ac_B\operatorname{Re}\langle\mathcal G_A\mathsf v,\mathcal G_B\mathsf v\rangle\ \ [\mathrm{EW.33};\ \mathrm{EW.20}\ \text{Gram data}];\qquad\hat\mu^2>0:\ \text{floor-independent residue packaging}\ \varkappa^2\beta^2h_0^2\ \ [\mathrm{EW.33}\ \text{with}\ \ell^2\ \text{factored out}];$$
$$(2)\quad\frac{m_{\mathrm{pole}}^2}{m_{\mathrm{hid}}^2}=\frac{\hat\mu^2\,\mathfrak h^4\,G(c)}{(\ln2)^2}\cdot\Bigl(\frac{\Lambda_c}{L}\Bigr)^{2}\ \in\ \mathfrak q^0\qquad[\text{well-posed};\ m_{\mathrm{hid}}^2=L^2(\ln2)^2/\mathfrak h^2\ \ \mathrm{FT.32}(1)];$$
$$(3)\quad\textbf{length-universality}:\ \text{at fixed}\ \kappa\text{-profile shape and Gram data the ratio is independent of}\ L;\quad\text{uniform}\ \kappa:\ \text{ratio}=\frac{\hat\mu^2\mathfrak h^4G(c)}{(\ln2)^2}\,\kappa\ —\ \text{linear in the edge quantum, floor-free};$$
$$(4)\quad\text{Cauchy–Schwarz}:\ \Lambda_c^2\le L\,\Theta(c),\ \text{equality}\iff\kappa_e\ \text{uniform}\ [\text{math}]\implies\text{at fixed}\ (\Theta,L):\ \text{uniform floors maximize the bridge ratio};$$
$$(5)\quad h_0=0\implies\hat\mu^2=0\implies m_{\mathrm{pole}}^2=0\ \ [\mathrm{EW.33}]\ \wedge\ m_{\mathrm{hid}}\ne0\ \ [\mathrm{FT.32}(1)]:\ \text{the two reads decouple without the scalar background};$$
$$(6)\quad\textbf{kernel coherence}:\ c\in\ker M^2=\operatorname{span}\{Q\}\ [\mathrm{EW.22}]\implies G(c)=0\implies m_{\mathrm{pole}}^2=0\ [\mathrm{EW.33}:\ \text{Gram PSD}]\ —\ \text{charge-aligned (photon-direction) transport is defect-massless at every floor, matching}\ m_\gamma^2=0\ [\mathrm{EM.6}].$$
No identification $m_{\mathrm{pole}}=m_{\mathrm{hid}}$ is asserted; the ratio is the bridge datum (Open Gaps 7).

### FT.34 — Round-trip quantization between floors; integrality propagation; sealing partition rule

**Thm.** Let $\Sigma^{(1)},\Sigma^{(2)}$ carry materialized 2-cycles $c_1,c_2$ [$\Theta(c_i)=2\kappa_i$, $\kappa_i\in\mathbb Z$: FT.24], and let $P,P'$ be connector chains with $\Gamma:=c_1\cup P\cup c_2\cup P'$ a valid closed chain [D1.4: concatenation, Janus balance], edge-disjoint union. If $\Gamma$ materializes:
$$(1)\quad\Theta(P)+\Theta(P')=\Theta(\Gamma)-2\kappa_1-2\kappa_2\in2\mathbb Z\qquad[\mathrm{FT.22},\ \mathrm{D1.7}\ \text{additivity}];$$
$$(2)\quad P'=\bar P\ (\text{same bidirectional channels reversed}\ [\mathrm{FT.23}\ \text{per edge}]):\quad\Theta(P)\in\mathbb Z;\qquad d_{12}:=\Theta(P)=\textbf{geometric distance (integer)};$$
$$(3)\quad\textbf{additive winding law}:\ k(\Gamma)=\frac{\Theta(\Gamma)}{2}=\kappa_1+\kappa_2+d_{12}=k(c_1)+k(c_2)+d_{12}\qquad[\mathrm{FT.25}(3):\ k=\kappa\ \text{at 2-cycle floors}];$$
$$(4)\quad\textbf{round-trip integrality (propagation lemma)}:\ \text{let}\ e,\bar e\ \text{be both real},\ \Gamma\ \text{materialized closed with edge multiset}\ \{e,\bar e\}\sqcup E_0,\ E_0\ \text{decomposing edge-disjointly into materialized closed chains}:\quad2\kappa_e=\Theta(\Gamma)-\Theta(E_0)\in2\mathbb Z\implies\kappa_e\in\mathbb Z;$$
$$(5)\quad\textbf{sealing partition rule}\ [\textbf{CT3.17a(1) (F)}]:\ \text{the group-size structure of sealed colour-attachment sets, and the non-sealing of a lone attachment}.$$

### FT.36 — Flux ledger completion

**Thm.** $(1)$ **Saturation locus.** Jaw/threshold arithmetic — where the temporal jaw binds, and the threshold $=$ the channel constant: CT0.6a (Part 1). In FT.1's geodesic slowly-varying gauge ($\delta h=\Delta\ell/(\Omega\mathfrak h)$, $\delta\tau=\Delta t/\Omega$, $\Omega>0$ [CT1.12]) the locus reads
$$\frac{\Delta\ell(\gamma)}{\Delta t(\gamma)}=4\,\mathfrak h\qquad(\text{channel speed}=4\ \text{hop lengths per tick}),$$
with $\Omega$ cancelling: **the saturation scale is a conformal invariant** [FT.6 pattern]; only the saturated value is $\Omega$-modulated ($\mathcal F=4\ln2$, $\mathcal F_{\mathrm{phys}}=4\ln2/\Omega$ [FT.5, Def-H.5]).
$(2)$ **Attainment (FT.36(2) discharged).** Whenever Def-H.3's transit domain is nonempty, its sup is attained by an explicit photon-content schedule: partition $\gamma$'s edges into per-tick groups of $\le4$; run transit (photon) content [EM.5, EM.6: trivial chains $\subseteq V_2$; D1.5: open propagating $=$ transit] on $\mathsf B(\gamma)/\ln2$ scheduled hops [FT.1's contracted notation] — per-tick group capacity: CT0.6a's sharpness clause (Part 1) — $\mathsf E_{\mathrm{tr}}=\delta h'\ln2$ [EM.7] $\Rightarrow\sup=\mathsf B(\gamma)$ [FT.1's bound met with equality]. On channels whose edges are bound-locked in every configuration the transit domain is empty and $I=0$ (attainment vacuous; bound trivially valid).
$(3)$ Hence FT.1/FT.3/FT.4/FT.5's bounds are sup-attained equalities on exhibited configurations wherever transit content is admissible.

### FT.37 — The relating equation, complete

**Thm.** For a materialized closed chain $c$ [FT.22], with $S_{\mathrm{reg}}(c)=\delta h(c)\,\ln2$ [CT0.9, C9] and $A_{\mathrm{loop}}(c):=\oint_c ds^2=\Theta(c)\,\mathfrak h^2=2k\,\mathfrak h^2$ [D1.6, FT.22], and mean edge quantum $\bar\kappa(c):=\Theta(c)/\delta h(c)$:
$$\frac{S_{\mathrm{reg}}(c)}{A_{\mathrm{loop}}(c)}=\frac{\ln2}{\mathfrak h^2}\cdot\frac{1}{\bar\kappa(c)}=\frac{\delta h(c)\,\ln2}{2k\,\mathfrak h^2};\qquad
\frac{S_{\mathrm{reg}}}{A_{\mathrm{loop}}}=\frac{S_{\min}}{A_{\min}}=\frac{\ln2}{\mathfrak h^2}\ [\mathrm{CT1.29}]\iff\Theta(c)=\delta h(c)\ (\bar\kappa=1).$$
On all-nonnull per-edge-integer chains [FT.24/FT.34(4) scope]: $\bar\kappa\ge1$, with equality $\iff\kappa_e\equiv1$; null edges or class-(iii) rational profiles [Open Gaps 13, FT.38(3)] admit $\bar\kappa<1$ (witness $(1,1,0)$: $\bar\kappa=\tfrac23$).

### FT.38 — Non-geodesic tightening and on-shell rigidity

**Thm.** $(1)$ **Tightening.** For any spacelike path $\gamma$ with on-shell integer edge data $\kappa_e\in\mathbb Z_{\ge1}$ [FT.24/FT.34(4) scope]:
$$I_{o\leftarrow\Sigma}(\gamma)\ \le\ \min\bigl(\delta h(\gamma),\ 4\,\delta\tau(\gamma)\bigr)\ln2\ \le\ \min\Bigl(\frac{\Delta\ell(\gamma)}{\mathfrak h},\ 4\,\delta\tau(\gamma)\Bigr)\ln2,\qquad\Delta\ell(\gamma)=\mathfrak h\sum_{e\in\gamma}\sqrt{\kappa_e}\ \ [\mathrm{Def\text{-}H.2},\ \mathrm{D1.6},\ \mathrm{FT.24}(2)],$$
with no geodesic and no slow-variation hypothesis; spatial equality $\iff\kappa_e\equiv1$. FT.1's geodesic physical form is the special case; the bound is tightest on stable jumps [Def-H.19: local $\Delta\ell$-minimizers; Morse — math].
$(2)$ **On-shell rigidity.** In CT1.19's family regime ($L=\mathfrak h n_{\mathcal R}$ fixed, $\mathfrak h\to0$, $g$ smooth along $\gamma$ [CT2.6]): $\kappa_e=f(\lambda_e)+O(\mathfrak h)$ with $f:=g_{\mu\nu}\dot x^\mu\dot x^\nu$ continuous [CT1.19's Pf, midpoint Taylor; per-edge remainder uniform]. For per-edge-integer classes (i)/(ii) [Open Gaps 13]: $\exists\,\mathfrak h_0$ such that $\forall\,\mathfrak h<\mathfrak h_0$, $\kappa_e$ is **constant along each connected materialized chain** — signature included (spacelike $\kappa\ge1$, null $0$, timelike $\kappa\le-1$ are $\ge1$ apart). Hence uniform-$\kappa$ is continuum-generic on-shell: FT.33(3)'s length-universality and FT.33(4)'s Cauchy–Schwarz equality are the generic on-shell case, not specializations; signature changes are confined to $O(\mathfrak h)$ boundary layers.
$(3)$ **Rational ladder (class-(iii) arena).** Without per-edge integrality, FT.22 alone permits uniform $\kappa\in(2/L)\mathbb Z$ on an $L$-cycle ($\Theta=L\kappa\in2\mathbb Z$; witness $L=3$, $\kappa=\tfrac23$, $\Theta=2$): per-edge integrality is special to $L=2$ [FT.24: $2\mathbb Z/2=\mathbb Z$] and round-trip-closed channels [FT.34(4)]; clause (2)'s integer-step argument does not reach spacings $2/L<1$.

### FT.39 — Confinement converse, singlet diagonal, and filter placement

**Thm.** $(1)$ **Converse (Gap 8).** $\Pi_{\mathcal C}(\Sigma;C)=\mathcal C(\Sigma;C)\cdot\mathbb I$ with $\mathcal C\in\{0,1\}$ [Def-H.10: scalar idempotent] $\implies F_{\mathrm{strong}}^\Sigma(C)=\mathcal C\cdot F_{\mathrm{strong}}\big|_\Sigma$ [FT.19's definition]. Hence $\mathcal C=1\implies F_{\mathrm{strong}}^\Sigma=F_{\mathrm{strong}}\big|_\Sigma\ne0$ for nonzero aspect data ($f_a\ne0$ [CT3.9, CT3.10]) on $\ge1$ colour slot — generic nonvanishing with exact exception locus $\{f=0\}\ \cup\ \{\mathrm{Colour}(\Sigma)=\varnothing\}$. At support level [Def-H.11's selection-type read]: $\Pi_{\mathcal C}=\mathbb I\ne0$ whenever $\mathcal C=1$ — unconditional.
$(2)$ **Singlet diagonal (consistency).** On sealed (singlet) states the Lie action annihilates: $T_a|\text{singlet}\rangle=0$ [CT3.15, CT3.17 invariance] $\implies\langle\text{singlet}|F_{\mathrm{strong}}|\text{singlet}\rangle=0$ — consistent with FT.11 (no independent colour charge) and CT3.22 (colour is not an end-charge): the strong block's nonzero content is the admissibility structure and the gluon mode count [CT3.13], not singlet expectation values.
$(3)$ **Filter placement (Gap 9, decision derived).** Def-H.9's $\mathcal M(\Sigma)$ must **not** be pre-weighted by $\mathcal C(\Sigma;C)$: its members are restrictions $C|_\Sigma$ of valid ambient configurations [FT.18's setup; D2.11], whose colour sealing is ambient-global [CT3.18] — $\mathcal C(\Sigma;C)=0$ records that $\Sigma$'s partners lie outside [FT.18's non-locality], not that $C$ is invalid. Pre-weighting would delete the EM/$G$/$H$ reads of externally-sealed configurations, contradicting their colour-independence [FT.11, FT.21(i)–(ii)]; the downstream $\Pi_{\mathcal C}$ filter [Def-H.15(3)] zeroes exactly the strong block [FT.19] and keeps the rest — the corpus-consistent placement. CT2.8(3)'s null-quotient handles *universe-level* invalidity [CT3.18], a different question from $\Sigma$-relativity.

### FT.40 — Closed-core charge read

**Thm.** For a closed oriented chain $c$ based at $v=s(c)=t(c)$ with first edge $e_1$ (out of $v$) and last edge $e_k$ (into $v$) [D1.4's ordered tuple]:
$$q_{\mathrm{core}}(c;v):=\frac{\sigma_{e_1}-\sigma_{e_k}}{2}\ \in\ \{-1,0,+1\}\qquad[\mathrm{D3.4}\ \text{applied to closed}\ c;\ \mathrm{CT0.9}:\ \text{per-edge independent registers};\ \mathrm{EM.9}:\ \text{alphabet, all values attained}]$$
is well-defined; under basepoint/orientation reversal [D2.6's $\omega$: $s\leftrightarrow t$, charge $\mapsto$ $-$charge]: $q_{\mathrm{core}}\mapsto-q_{\mathrm{core}}$ — the corpus's own charge-conjugation law, verbatim on the core read. At the 2-cycle floor: $q_{\mathrm{core}}=(\sigma_{e_1}-\sigma_{e_2})/2$ at base $p$, negated at base $q$. The closed core is therefore **not** charge-neutral by closure; its ternary read is basepoint data, and the observer-facing charge remains the EM.9 end-read of the full transit chain through the channel [Def-H.4].

### FT.41 — The per-aspect ledger

**Thm.** $(a)$ **Charge count derived.** EM.9/D3.4's read consumes exactly the two end registers of a chain; $N_{\mathrm{charge}}=2$ in FT.14's decomposition is a theorem and $N_{\mathrm{weak}}=\delta h-2$ its arithmetic complement. the residual interface content is the *attribution* clause of Def-H.8 (interior weight bits read through the weak/spin channel [Def-H.8]) — reduced — Def-H.8's attribution clause.
$(b)$ **Colour ledger counted.** The sealing grammar of $\mathrm{Colour}(\Sigma)$ — admissible groupings [FT.34(5), Def-H.10], closed form, small-$N$ counts $g$, and attachment-type refinement — is **CT3.17a(2)–(3) (F)**. The ledger read defined here: $N_{\mathrm{strong}}(\Sigma):=\log_2 g\bigl(|\mathrm{Colour}(\Sigma)|\bigr)$ — the sealing-pattern information of the grammar count (a registration-type ledger, per the trichotomy below).
$(c)$ **Gravity/Higgs ledger reframed.** $G$'s on-shell ledger is the integer $\kappa$-profile modulo the single loop constraint [FT.22]: $L-1$ free integers on a materialized $L$-cycle — unbounded, hence $\neg$bit-type [C10: bit counts attach to finite registered alternative sets]; $H$'s ledger is the continuous P4 datum $h_0$ [EW.13, P4]. Per-aspect "bit counts" are well-posed exactly for the registration-type ledgers $(a),(b)$ — the trichotomy answers the original question.
$(d)$ **Strictly new at $\Sigma$, first counts [Def-H.13's filter].** $N(\Sigma)=1$: $\mathfrak u(1)$ factors per-edge entirely — nothing strictly new; single-contact floors carry no collective boundary mode. $N(\Sigma)=2$: $\dim\mathfrak u(2)=4$, factored diagonal $=2$, strictly new $=N^2-N=2$ real dimensions — the off-diagonal boundary mixings $|e_1\rangle\langle e_2|+\mathrm{h.c.}$, $i(|e_1\rangle\langle e_2|-\mathrm{h.c.})$: a collective inter-contact exchange mode, first available at two-contact floors [FT.28's variant Rmk]. Aspect identification of the mixing sector: open (folded into Open Gaps 16).

### Def-H.20 — Platonic floors (setup vocabulary)

**Def.** Let $S$ be a Platonic solid with 1-skeleton $\Gamma_S$: $V$ vertices, $E$ undirected edges, $F$ faces of uniform length $L$ ($FL=2E$), regular vertex degree $d$ ($Vd=2E$); cardinals [math]:
$$\text{tetrahedron}\ (4,6,4,3);\quad\text{cube}\ (8,12,6,3);\quad\text{octahedron}\ (6,12,8,4);\quad\text{dodecahedron}\ (20,30,12,3);\quad\text{icosahedron}\ (12,30,20,5).$$
The **Platonic floor** $\Sigma_S$ $:=$ the bounded subnetwork on $\Gamma_S$'s vertex set whose real-edge content realizes every undirected edge as a **bidirectional channel** (both orientations in $\mathcal R$) — the full bidirectional 1-skeleton. Variants: **dark** ($\partial\Sigma_S=\varnothing$: no observer contact [Def-H.1]) and **single-contact observed** (one external $o$ joined by exactly one real edge to one $v_1$). Card hypotheses, declared at each use: **(M1)** every face cycle materializes [FT.22's scope]; **(M2)** every bidirectional pair materializes as a 2-cycle [FT.24's scope] — both are spectral questions the corpus does not decide (FT.32's Status pattern). Sub-floor vocabulary: $\Sigma_{\min}$ is the $E{=}1$ cell [FT.28], $\Sigma_{12}$ the $E{=}3$ cell [FT.35], the cycle ladder $\Sigma_L$ the unidirectional family [FT.32].

### FT.42 — The Platonic card template

**Thm.** Under Def-H.20's setup, with (M2) [hence $\kappa_e\in\mathbb Z$ on every channel, FT.24] and (M1) [hence $\Theta_f\in2\mathbb Z$ per face, FT.22]:
$$(1)\quad E_{\mathrm{int}}=2E,\qquad I_{\mathrm{hid}}=2E\ln2,\qquad m_{\mathrm{hid}}=\frac{2E\ln2}{\mathfrak h}\qquad[\text{observed: FT.17},\ \text{Def-H.35};\ \text{dark: Def-H.9(2) with}\ E_{\mathrm{vis}}=0];$$
$$(2)\quad\text{rungs (rung correction, FT.62)}:\ \text{dark}\ n(v)=2d\ \forall v;\ \ \text{observed (1 directed edge)}\ n(v_1)=2d+1;\ \ \text{bidirectional contact}\ 2d+2;\ \text{others}\ 2d\ [\mathrm{D0.8}:\ \text{directed real-edge count};\ \mathrm{CT0.5}:\ \phi_e\ \text{per incident real edge}];\qquad O(2d)=112\ (d{=}3),\ 496\ (d{=}4),\ 2032\ (d{=}5);\ \ O(2d{+}1)=240,1008,4080\ [\mathrm{CT0.6}];$$
$$\text{saturation universality (the former "accessibility trichotomy" is retracted, FT.62(3))}:\ \text{every vertex of every bidirectional floor}\ (d\ge2\ \text{channels}:\ n\ge4)\ \text{is}\ D^-\text{-configured}\ [\mathrm{CT4.1}],\ \text{content locked, retained, counted}\ [\mathrm{CT4.3},\ \mathrm{D4.2}];\ \text{grade by degree}:\ O(2d);\ \ \text{the lock-free family is the unidirectional one}\ [\mathrm{FT.28}(5),\ \mathrm{FT.32}(2);\ \mathrm{FT.62}(3)];$$
$$(3)\quad\Theta_{\mathrm{int}}=2K_S,\qquad K_S:=\!\!\sum_{\text{channels}}\!\!\kappa_{\mathrm{ch}}\in\mathbb Z\qquad[\mathrm{FT.23}:\ \kappa_{\bar e}=\kappa_e;\ \mathrm{D1.7}:\ \text{additivity}];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}(2)];\qquad W\ \text{row fires}\iff K_S\ne0;$$
$$(4)\quad\mathcal A(\Sigma_S;C)\supseteq\{G,H\}\ [G:\ I_{\mathrm{hid}}\ne0;\ H:\ \mathrm{Def-H.36}];\qquad\mathrm{EM}\in\mathcal A\iff\exists v:\ f_v\ne0\ [\mathrm{D3.3}];\qquad(\text{scope}\ [\mathrm{FT.62}(5)]:\ \text{type-}(d,d)\ \text{vertices leave D3.3's literal type-}(1,1)\ \text{domain empty on dark bidirectional floors};\ \text{the row evaluates on observed variants via chain-local pass-through reads}\ [\mathrm{FT.21}(i)]);$$
$$\text{strong}\in\mathcal A\iff\text{inside-sealed phase}\ (\mathcal C=1):\ \text{exists for every}\ S\ (V\ge4\ \text{partitions into 2s and 3s}\ [\mathrm{FT.34}(5)]),\ \text{in}\ g(V)\ \text{groupings}\ [\mathrm{FT.41}(b)];\qquad\dim\mathcal K_{\Sigma_S}=9\ (+1)\ (+8)\le18\ [\mathrm{FT.26}];$$
$$(5)\quad\textbf{the card table}:\ \Pi=E_{\mathrm{int}}^2\,\Theta_{\mathrm{int}}(\ln2)^2=8E^2K_S(\ln2)^2\ [\text{Open Gaps 7 diagnostic}].$$
$$
\begin{array}{c|c|c|c|c|c|c|c|c}
S & (V,E,F,d) & m_{\mathrm{hid}}\cdot\mathfrak h/\ln2 & O(2d)\ \text{dark}\ & O(2d{+}1)\ \text{contact} & \text{face}\ (L,\kappa_{\min},\Theta_{f,\min},k_{f,\min}) & \text{indep. windings} & g(V)\ \text{groupings} & \Pi/(\ln2)^2\\ \hline
\text{tetrahedron} & (4,6,4,3) & 12 & 112 & 240 & (3,2,6,3) & 3 & 3 & 288\,K_S\\
\text{cube} & (8,12,6,3) & 24 & 112 & 240 & (4,1,4,2) & 5 & 385 & 1152\,K_S\\
\text{octahedron} & (6,12,8,4) & 24 & 496 & 1008 & (3,2,6,3) & 7 & 25 & 1152\,K_S\\
\text{dodecahedron} & (20,30,12,3) & 60 & 112 & 240 & (5,2,10,5) & 11 & 292938721075 & 7200\,K_S\\
\text{icosahedron} & (12,30,20,5) & 60 & 2032 & 4080 & (3,2,6,3) & 19 & 164395 & 7200\,K_S
\end{array}
$$
$$(6)\quad\textbf{consistency anchors}:\ \text{tetrahedron observed with a bidirectional contact reproduces FT.17 cross-check 3 verbatim}\ (E_{\mathrm{int}}=12,\ E_{\mathrm{bd}}=2\le4\cdot1,\ I_{\mathrm{hid}}=12\ln2);\ \ \text{the tetrahedron face}\ \{A,B,C\}\ \text{observed by}\ D\ \text{is cross-check 2}\ (E_{\mathrm{int}}=6,\ E_{\mathrm{bd}}=6,\ \delta\tau\ge2);$$
$$\Sigma_{\min}=E{=}1\ \text{cell}\ [\mathrm{FT.28}];\qquad\Sigma_{12}=E{=}3\ \text{cell}\ [\mathrm{FT.35}].$$

### FT.45 — The bidirectional polygon floors $P_n$: cards, minima, and the null-carrying sector

**Thm.** Let $\Sigma_{P_n}$ ($n\ge3$) be the fully bidirectional 1-skeleton of the regular $n$-gon [Def-H.20's setup class], $n\ge3$: $n$ vertices, $n$ bidirectional channels, $2n$ directed edges; sphere compactification with two length-$n$ faces (interior, exterior): $FL=2n=2E$, $V-E+F=n-n+2=2\ \checkmark$ [math]. (The digon-walk floor $\Sigma_{\min}$ [FT.28] is the taxonomy's $E{=}1$ cell, $\neg$a polygon member — clause (5).) Under **(M2$_n$)** all $n$ channels materialize as 2-cycles [FT.24: $\kappa_i\in\mathbb Z$] and **(M1$_n$)** the interior face materializes [FT.22: $\Theta_f\in2\mathbb Z$]:
$$(1)\quad E_{\mathrm{int}}=2n,\qquad I_{\mathrm{hid}}=2n\ln2,\qquad m_{\mathrm{hid}}=\frac{2n\ln2}{\mathfrak h},\qquad\Pi=8n^2K_P(\ln2)^2,\qquad K_P:=\Theta_{\mathrm{int}}/2=\textstyle\sum_{i=1}^n\kappa_i\ [\mathrm{FT.42}\ \text{template}];$$
$$(2)\quad\text{rungs (rung correction, FT.62)}: \text{dark}\ n(v)=4\ \forall v\ (2\ \text{channels each},\ \mathrm{D0.8}\ \text{directed count};\ \text{type}\ (2,2));\ \ \text{single-contact observed}\ n(v_1)=5,\ \text{others}\ 4;\qquad O(4)=16=C_{\mathrm{cap}},\ O(5)=48\ [\mathrm{CT0.5},\ \mathrm{CT0.6}]:\ \textbf{uniform minimal saturation at every vertex of every member}\ [\mathrm{CT4.1}];\ \text{locked content retained and counted}\ [\mathrm{CT4.3},\ \mathrm{D4.2}];\ \text{the lock-free family is the unidirectional one}\ [\mathrm{FT.32}(2),\ \mathrm{FT.62}(3)];$$
$$(3)\quad\textbf{walk space and the single parity constraint}:\ \beta_1(\text{directed multigraph})=2n-n+1=n+1\ [\text{math}];\qquad\text{closed-walk structure}:\ \text{flow balance at every vertex}\implies\text{per-channel net flow constant}=w\ (\text{the walk's winding});$$
$$\Theta(w)=w\,\textstyle\sum_i\kappa_i+2\sum_i\kappa_i b_i\ \ (b_i:\ \text{reverse traversals})\implies\Theta(w)\in2\mathbb Z\ \forall w\iff\textstyle\sum_i\kappa_i\in2\mathbb Z\ \ (w{=}1:\ \text{the face},\ \mathrm{M1}_n):$$
$$\textbf{exactly one independent parity constraint};\qquad\text{on-shell}\ \kappa\text{-lattice}=\{\kappa\in\mathbb Z^n:\ \textstyle\sum\kappa_i\in2\mathbb Z\}:\ \text{index}\ 2=2^{F-1}\ [\mathrm{FT.43}(3)\ \text{pattern at}\ F{=}2];\qquad\text{digons}\ (w{=}0):\ \Theta=2\sum\kappa_ib_i\in2\mathbb Z\ \text{automatic}\ [\mathrm{M2}_n,\ \mathrm{FT.24}];$$
$$(4)\quad\textbf{four minimality regimes}\ (\Theta_{\min}>0,\ \text{face materialized};\ \text{machine-enumerated for}\ n\le7):$$
$$\text{spacelike-or-null}\ [\kappa\ge0]:\ \Theta_{\min}=2\ \forall n\ge3\ (\text{profile}\ (1,1,0,\dots,0));\qquad\textbf{null-carrying dimension}=|\{i:\kappa_i=0\}|\ge n-2\ \text{in every such minimizer};$$
$$\text{strictly-spacelike}\ [\kappa\ge1]:\ \Theta_{\min}=n+(n\ \mathrm{mod}\ 2)\ (n\ \text{even}:\ \text{unique all-1 profile};\ n\ \text{odd}:\ \text{one}\ 2,\ \text{rest}\ 1);\qquad\text{uniform}\ [\kappa_i\equiv\kappa]:\ \Theta_{\min}=n\ (n\ \text{even},\ \kappa{=}1)\ /\ 2n\ (n\ \text{odd},\ \kappa{=}2)\ [\mathrm{FT.32}(6)];$$
$$\text{signature-mixed}\ [\kappa\in\mathbb Z,\ \text{timelike}\ \kappa<0\ \text{admissible}\ [\mathrm{CT1.12}]]:\ \Theta_{\min}=2\ \forall n\ge3\ (\text{witnesses}:\ n\ge4\ \text{even}:\ (1^{(n+2)/2},(-1)^{(n-2)/2});\ n\ge5\ \text{odd}:\ (1^{n-1},-(n-3));\ n{=}3:\ (2,1,-1));$$
$$(5)\quad\textbf{the digon distinction}:\ \text{the null-carrying sector has dimension}\ n-2:\ \text{at}\ n=2\ (\Sigma_{\min})\ \text{it is}\ \{-1\}\text{-dimensional}=\text{empty}:\ \Theta_{\min}=2\ \text{there forces}\ \kappa_1=\kappa_2=1\ \text{(all-nonnull, purely spacelike)}\ [\mathrm{FT.24}(4)];\ \text{for every}\ n\ge3\ \text{the minimum is null-carrying}.\ \textbf{The fermion floor is derived to be a digon, not a polygon};$$
$$(6)\quad\textbf{sealing}:\ \text{dark}\ P_n:\ \mathrm{Colour}=\varnothing\ (n(v)=2<3\ [\mathrm{D3.1}])\implies\text{strong}\ \neg\in\mathcal A\ \text{always}\ [\mathrm{FT.20}];\ \ \text{observed}:\ \mathrm{Colour}=\{v_1\}:\ \neg\exists\ \text{inside partner}\ [\mathrm{A1}]\implies\text{structurally colourless}\ [\mathrm{FT.27}\ \text{case split}];\quad\mathcal A\supseteq\{G,H\},\ W\iff K_P\ne0,\ \mathrm{EM}\iff\exists v:\ f_v\ne0;\quad\dim\mathcal K\le10<18;$$
$$(7)\quad\textbf{anchors}:\ \Sigma_{\min}\ (\text{digon walk},\ E{=}1)\ \text{is adjacent to but}\ \neg\text{a member of this family}\ [\mathrm{FT.28}/\mathrm{FT.44}(4)\ \text{taxonomy}]:\ \text{clauses}\ (3)\text{--}(5)\ \text{degenerate there}\ (\neg\exists\ \text{proper face};\ \text{its minimum forces}\ \kappa{=}1\ [\mathrm{FT.24}(4)]);\quad\text{the unidirectional}\ 3\text{-cycle}\ =\ \mathrm{FT.17}\ \text{cross-check 1}\ [\mathrm{FT.32}];\quad\text{the observed tetrahedron face is NOT}\ P_3\text{: in bidirectional}\ K_4\ \text{the face vertices carry the third (external) channel each}\ (n(v)=4,\ E_{\mathrm{bd}}=6)\ [\mathrm{FT.17}\ \text{cross-check 2}].$$

### FT.46 — Distinctness is unbounded: no upper limit on distinct regular polygons

**Thm.** $(1)$ **Combinatorial distinctness.** The regular $n$-gons are pairwise non-isomorphic for all $n\ge3$ ($n$ is the complete invariant of the 1-skeleton); $\Sigma_{P_n}$ is a valid bounded subnetwork configuration class for every $n$ [A1: $\mathcal Q$ countably infinite supplies vertices; D1.2: seals supply edges; no mask or capacity clause restricts $n(v)=4$ bidirectional vertices — oversubscription is absorbed and retained [CT4.1, CT4.3; rung correction, FT.62], CT0.6: $O(4)=16$ uniform].
$(2)$ **Ledger injectivity.** On the uniform-$\kappa$ minima, the card invariants separate every member:
$$m_{\mathrm{hid}}(n)=\frac{2n\ln2}{\mathfrak h}\ \text{strictly increasing};\qquad E_{\mathrm{int}}(n)=2n\ \text{injective};\qquad\beta_1(n)=n+1\ \text{injective};\qquad\text{null-carrying dimension}\ n-2\ \text{injective};$$
$$\Theta_{\min}(n)=\begin{cases}2 & \text{spacelike-or-null / signature-mixed}\\ n+(n\ \mathrm{mod}\ 2) & \text{strictly-spacelike}\\ n\ \text{or}\ 2n & \text{uniform (even/odd)}\end{cases}\quad\text{regime-separating};\qquad\text{lattice index}=2\ \forall n\ [\mathrm{FT.45}(3)]\ (\text{uniform, non-separating}).$$

### FT.47 — No geometric ceiling: the Gauss–Bonnet bound binds area, never $n$

**Thm.** $(1)$ **Gauss–Bonnet area bound.** A geodesic $n$-gon enclosing a topological disk in a smooth Riemannian surface of constant curvature $\bar K$, interior angles $\alpha_i$:
$$\sum_{i=1}^n\alpha_i=(n-2)\pi+\bar K\,A\qquad[\text{Gauss–Bonnet};\ \text{geodesic edges}:\ \kappa_g\equiv0;\ \text{math}],$$
and convexity ($\alpha_i<\pi\ \forall i$) forces $\bar K A<2\pi$ — a bound on the **enclosed area per polygon, with no $n$-dependence**.
$(2)$ **Model-geometry existence — every $n\ge3$, no ceiling.** Flat ($\bar K=0$): the Euclidean regular $n$-gon, $\alpha=\frac{(n-2)\pi}{n}\in(0,\pi)$ for every $n\ge3$ [math]. Spherical ($\bar K>0$): for every $A\in(0,2\pi/\bar K)$ a convex regular geodesic $n$-gon with $\alpha=\frac{(n-2)\pi+\bar KA}{n}\in\bigl(\frac{(n-2)\pi}{n},\pi\bigr)$ exists for every $n\ge3$ [math: polar construction on $S^2$; small-area members are convex]. Hyperbolic ($\bar K<0$): every $\alpha\in\bigl(0,\frac{(n-2)\pi}{n}\bigr)$ is realized by a unique regular $n$-gon of area $A=\frac{n\alpha-(n-2)\pi}{\bar K}>0$, for every $n\ge3$ [math].
$(3)$ **Local existence in the general emergent geometry.** CT2.6's spatial slices are smooth Riemannian in the perturbative regime [CT1.12: $\bar g_{ij}\succ0$]; every point has a convex normal neighborhood [math: standard existence], inside which any $n\ge3$ points on a small geodesic circle join by unique minimizing geodesics — an **equilateral geodesic $n$-gon for every $n$**. Exact regularity (equal angles too) needs a local symmetry hypothesis; equilateral local existence does not.
$(4)$ **Transfer.** Nothing in A1–A9 or Parts 1–3's definitions/theorems bounds polygon $n$: CT2.7's dynamics (Einstein–Hilbert, $\Lambda$ a P4 datum) fixes $\bar K$ per solution but no polygon ceiling — for $\bar K\le0$ clause (2) is global, for $\bar K>0$ local (small-area members), in every case for all $n\ge3$. The corpus's only numeric caps bind different objects: per-vertex accessibility ($n(v)\le3$ unoversubscribed [CT0.11, CT4.1] — polygon floors sit at $n(v)\in\{2,3\}$ [FT.45(2)], never touching it) and the spectrum (M1$_n$/M2$_n$ materialization — solution data, not a bound on $n$).
$(5)$ **Verdict.** The question "do distinct regular polygons have an upper limit" is answered **no** at all three levels — combinatorial [FT.46], model-geometric (clause 2), local emergent-geometric (clause 3) — with the two bounds that do exist precisely located: the Gauss–Bonnet area bound (per polygon, curvature-signed) and the materialization filter (spectral, per solution).

### FT.48 — Stability structure of floor-to-floor channels (Gap 18, partial)

**Thm.** Let $\gamma$ be a channel path between two floor termini, on-shell (edges of integrality classes (i)/(ii) [Open Gaps 13]) in the continuum regime of CT1.19/CT2.6.
$(1)$ **Stationarity is geodesy.** $\delta\!\int_\gamma ds^2=0$ among fixed-endpoint variations $\iff$ $\gamma$ is an affinely parametrized geodesic of $g_{\mu\nu}$ [CT1.20's stationary-phase locus; FT.31(2): the on-shell sums *are* the Riemann sums, so the ledger's stationary condition and the metric's Euler–Lagrange equation coincide; math].
$(2)$ **Two-sided distance law.** For a bidirectional round-trip connector $P$ of $m$ channels [FT.34(2)]: the ledger side is the integer distance $d_{12}=\Theta(P)=\sum_{e\in P}\kappa_e\in\mathbb Z$; the metric side is the proper length $\ell(P)=\mathfrak h\sum_{e\in P}\sqrt{\kappa_e}$ [FT.33(1) pattern, spacelike]. They are bound by
$$\ell(P)^2\ \le\ m\cdot d_{12}\cdot\mathfrak h^2\qquad[\text{Cauchy–Schwarz};\ \text{math}],\qquad\text{equality}\iff\kappa_e\ \text{uniform on}\ P;$$
uniform connectors obey $\ell^2=m\,d_{12}\,\mathfrak h^2$ exactly. Both sides are derived: the integer from materialization [FT.34(2)], the length from the metric dictionary [D1.6, FT.24(2)] — two reads of one channel, dimensionally consistent ($[\ell^2]=[\mathfrak h^2]=\mathfrak q^{-1}$, $d_{12}$ dimensionless).
$(3)$ **Stable-channel trichotomy.** Within a fixed endpoint class in the emergent geometry [Def-H.19 vocabulary]: index-0 stationary channels (no conjugate points) are exactly the local $\ell$-minimizers [math: Morse/Synge]; on-shell with $\kappa_e>0$, local $\ell$-minimality at fixed channel count $m$ coincides with local $d_{12}$-minimality along uniform families [clause (2): $\ell^2=m\,d_{12}\,\mathfrak h^2$ strictly monotone in $d_{12}$ at fixed $m$]. Saddle/maximal stationary channels exist wherever conjugate points do; CT1.20's stationary phase weights them *alike* with the minima.
$(4)$ **Derived vs. open.** Clauses (1)–(3) close the variational side of the stability program: stable channels are geodesics, their ledger distance is integer, and the two distance reads are Cauchy–Schwarz-bound with equality at uniformity. The selection side — whether the pole condition [CT2.5/Def-H.16] or the defect criterion [FT.33] *selects* index-0 channels — remains open (Open Gaps 18): it requires fluctuation-sign/Maslov-type structure on the $Z$ side, which Parts 1–3 does not develop.

### FT.43 — The winding ledger and Euler consistency

**Thm.** Under FT.42's hypotheses:
$$(1)\quad\textbf{sum rule}:\ \ \sum_{f}\Theta_f=2\!\!\sum_{\text{channels}}\!\!\kappa_{\mathrm{ch}}=\Theta_{\mathrm{int}}\quad\Longleftrightarrow\quad\sum_f k_f=K_S\qquad[\text{each channel lies in exactly two faces}:\ FL=2E;\ \mathrm{D1.7}];$$
$$(2)\quad\textbf{independent face reads}:\ F-1=E-V+1=\beta_1(\Gamma_S)\qquad[\text{one sum rule};\ \text{Euler}\ V-E+F=2;\ \text{math}:\ \text{cycle rank of a connected graph}];$$
$$(3)\quad\textbf{parity lattice}:\ \text{the on-shell}\ \kappa\text{-profiles}\ \{\kappa\in\mathbb Z^E:\ \Theta_f\in2\mathbb Z\ \forall f\}\ \text{form the kernel of the face-incidence map}\ \varphi:\mathbb Z^E\to\mathbb Z_2^F,\ \text{of index}\ 2^{F-1}\ \ [\text{math}:\ \operatorname{rk}_{\mathbb Z_2}\varphi=F-1\ \text{for spherical embeddings};\ \text{machine}:\ \text{explicit GF(2) elimination, tetrahedron and cube}];$$
$$(4)\quad\text{sector counts}:\ 2^{F-1}=2^{\beta_1}:\ \ \text{tetrahedron}\ 8,\ \text{cube}\ 32,\ \text{octahedron}\ 128,\ \text{dodecahedron}\ 2048,\ \text{icosahedron}\ 2^{19}=524288;$$
$$(5)\quad\textbf{Euler as card consistency}:\ \beta_1=E-V+1=F-1\ \text{ties the three ledgers}:\ \text{mass}\ (E\ \text{via FT.42}(1)),\ \text{colour}\ (V\ \text{via}\ g(V)),\ \text{winding}\ (F{-}1\ \text{reads})\ —\ \text{the sphere's Euler number is an identity among card entries, not an extra assumption}.$$

### FT.35 — The composite floor $\Sigma_{12}$: first colour-active, first $D^-$-carrying

**Thm.** Let $\Sigma_{12}=\{p_1,q_1\}\cup\{p_2,q_2\}$ with materialized 2-cycles $c_1=(p_1{\to}q_1{\to}p_1)$, $c_2=(p_2{\to}q_2{\to}p_2)$ [FT.24: quanta $\kappa_1,\kappa_2$], joined by the bidirectional connector $e_{12}=(q_1,p_2)$, $\bar e_{12}=(p_2,q_1)$ [both $\in\mathcal R$], single observer contact at $p_1$ ($E_{\mathrm{bd}}=1$; FT.17 hypotheses, Def-H.35). Let $\Gamma=c_1\cup e_{12}\cup c_2\cup\bar e_{12}$ [valid closed chain, D1.4]. If $\Gamma$ materializes:
$$(1)\quad\kappa_{12}\in\mathbb Z\qquad[\mathrm{FT.34}(4):\ \Gamma\setminus\{e_{12},\bar e_{12}\}=c_1\sqcup c_2\ \text{decomposes into materialized closed chains}];$$
$$(2)\quad E_{\mathrm{int}}=6\ (c_1{:}\,2,\ c_2{:}\,2,\ \text{connector}{:}\,2),\quad I_{\mathrm{hid}}=6\ln2,\quad m_{\mathrm{hid}}=\frac{6\ln2}{\mathfrak h}\qquad[\mathrm{FT.17};\ \mathrm{CT4.3}\ \text{retention, as below}];$$
$$(3)\quad\Theta_{\mathrm{int}}(\Sigma_{12})=2\kappa_1+2\kappa_2+2\kappa_{12}=2\,k(\Gamma)\in2\mathbb Z\ [\mathrm{FT.34}(3)];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}];\qquad\Pi=72\,k(\Gamma)\,(\ln2)^2;$$
$$(4)\quad\text{rungs}:\ n(p_1)=3,\ n(q_2)=2,\ n(q_1)=n(p_2)=4:\quad O(4)=2^5-16=16>0\ [\mathrm{CT0.6}]:\ \text{the junction vertices are}\ D^-\text{-configured}\ [\mathrm{CT4.1}]:\ \text{excess locked, ledger-retained}\ [\mathrm{D4.2},\ \mathrm{CT4.3}];$$
$$(5)\quad\textbf{colour phases}:\ \mathrm{Colour}(\Sigma_{12})\subseteq\{p_1,q_1,p_2\}\ [\mathrm{D3.1};\ \mathrm{CT0.13}:\ \text{strong persists at}\ n\ge4];\quad\mathcal C(\Sigma_{12};C)=1\iff\text{all three seal inside as one}\ \varepsilon\text{-type (baryon-like) triple}\ [\mathrm{D3.9},\ \mathrm{CT3.17},\ \mathrm{FT.34}(5):\ 3\ \text{admits no}\ \{2,3\}\text{-partition with an external remainder}];$$
$$\text{strong-active phase}:\ \dim\mathcal K_{\Sigma_{12}}=9+1+8=18\ —\ \text{the maximal observable mask is attained}\ [\mathrm{FT.26}(3)];\qquad\text{any external/unsealed attachment}:\ \mathcal C=0\implies\text{block}\equiv0\ [\mathrm{FT.19}].$$

### FT.50 — Composition and gluing laws

**Thm.** $(1)$ **Bridged union.** Let $\Sigma^{(1)},\Sigma^{(2)}$ be floors with bidirectional interiors [$E_{\mathrm{int}}^{(i)}=2E_i$], joined by a bidirectional connector path $P=(f_1,\dots,f_m)$ (disjoint from both interiors), single external contact; all digons materializing [M2-type]. Then
$$E_{\mathrm{int}}(\Sigma)=2E_1+2E_2+2m,\qquad m_{\mathrm{hid}}(\Sigma)=m_{\mathrm{hid}}^{(1)}+m_{\mathrm{hid}}^{(2)}+\frac{2m\ln2}{\mathfrak h}\qquad[\mathrm{FT.17},\ \text{Def-H.35}]:\ \textbf{informational mass is additive under bridged composition}.$$
$(2)$ **Generalized round-trip.** If $\Gamma=c_1\cdot P\cdot c_2\cdot\bar P$ materializes [$c_i$ materialized closed chains at the attachments; D1.4 concatenation]: $d_{12}:=\Theta(P)\in\mathbb Z$ and $k(\Gamma)=k_1+k_2+d_{12}$ [FT.34(2)–(3) generalized to $m$-channel connectors]; per-edge integrality $\kappa_{f_j}\in\mathbb Z$ requires each connector digon to materialize [FT.24] — the sum $d_{12}$ is integral without that strengthening.
$(3)$ **Junction saturation.** A bidirectional bridge into a vertex of interior degree $d\ge2$ gives $n_{\mathrm{junction}}=d+2\ge4\implies O(d{+}2)=2^{d+3}-16>0$: **composition creates darkness at every junction** [CT0.5, CT0.6, CT4.1, D4.2; FT.35's Rmk generalized]; content retained [CT4.3]. For $s$ triangular floors sharing one junction vertex: $2s$ channels meet there, $n=4s$ [D0.8], $O(4s)=2^{4s+1}-16$ — absorption rate grows exponentially in the sharing multiplicity [D4.2: rate $\propto O(n)$]: high-multiplicity junctions are maximally dark.
$(4)$ **Gluing law.** For $\Sigma=\Sigma_1\cup_G\Sigma_2$ glued along a shared subgraph $G$: $E_{\mathrm{int}}=E_{\mathrm{int}}^{(1)}+E_{\mathrm{int}}^{(2)}-|E_{\mathrm{dir}}(G)|$; the on-shell parity lattice is $\{\kappa:\ \Theta_c\in2\mathbb Z\ \forall\ \text{materialized closed chains}\ c\}$ — its index is $2^{\operatorname{rk}_{\mathbb Z_2}(\text{materialized cycle system})}$, dependencies automatic: a cycle homologous to a sum of materialized cycles inherits evenness [D1.7 additivity; FT.23 orientation-blindness].
$(5)$ **Computed cells.** **Bowtie** (two bidirectional triangles sharing one vertex $X$): $E_{\mathrm{int}}=12$, $m_{\mathrm{hid}}=12\ln2/\mathfrak h$; both faces materialized $\Rightarrow\Theta_{\mathrm{int}}=2(K_1{+}K_2)\in4\mathbb Z$; constraint rank 2 (index 4); rungs: $n(X)=8$ [$O(8)=496$], other four vertices $n=4$ [$O(4)=16$] — every vertex locked; five slots $\Rightarrow g(5)=10$ sealing groupings (one $\delta$-pair $+$ one $\varepsilon$-triple) [FT.41(b)]. **Double-triangle patch** (two tetrahedron faces glued along channel $AB$; $\Sigma=\{A,B,C,D\}$): $E_{\mathrm{int}}=10$; constraints $\Theta_{ABC},\Theta_{ABD}\in2\mathbb Z$: $\operatorname{rk}_{\mathbb Z_2}=2$ (index 4), and the boundary 4-cycle constraint is *derived*: $\Theta_{ACBD}=\Theta_{ABC}+\Theta_{ABD}-2\kappa_{AB}\in2\mathbb Z$; rungs $n(A)=n(B)=6$ [$O=112$], $n(C)=n(D)=4$ [$O=16$]; four slots $\Rightarrow g(4)=3$ groupings, all $\delta{+}\delta$ (meson–meson phases — the only $\{2,3\}$-partition of 4).

### FT.52 — Spin extraction: the constraint system, uniqueness of the stretched rule, and the localized obstruction

**Thm.** Let $R$ be an extraction rule in the sense of Def-H.9(3) — assigning admissible $\mathfrak{su}(2)$ labels $j$ to on-shell internal ledger data, under the weak action [FT.13]. Then:
$$(1)\quad R\ \text{cannot factor through}\ \mathrm{Hol}_{\mathrm{int}}\ \text{alone on chain-swept interiors}:\ (-1)^{\Theta_{\mathrm{int}}}=+1\ \text{on-shell}\ [\mathrm{FT.25}(1)];$$
$$(2)\quad R\ \text{must respect composition}:\ k(\Gamma)=k_1+k_2+d_{12}\ [\mathrm{FT.34}(3),\ \mathrm{FT.50}(2)]\ \text{and}\ k_f\text{-sums}\ \sum_fk_f=K_S\ [\mathrm{FT.43}(1)]\implies\text{the stretched values add}:\ \text{any rank-1 additive}\ R\ \text{satisfies}\ R(k_1{+}k_2)=R(k_1){+}R(k_2)\ \text{on aligned compositions}\ [\text{math}:\ \text{Cauchy equation on}\ \mathbb Z];$$
$$(3)\quad\textbf{uniqueness of the stretched rule}:\ \text{the unique rank-1 additive rule anchored at the seed}\ R(1)=\tfrac12\ [\mathrm{EW.32}]\ \text{is}\ R(k)=k/2\ \text{on the nonnegative winding cone},\ \text{with admissible labels}\ j=|k|/2\ (\text{admissibility correction}:\ \mathfrak{su}(2)\ \text{labels require}\ j\ge0,\ \text{and the Casimir distinguishes}\ \pm k/2:\ (-\tfrac32)(-\tfrac12)=\tfrac34\ne\tfrac{15}{4}=(\tfrac32)(\tfrac52)\ —\ \text{the absolute value is forced, machine-witnessed};\ \text{stretched additivity holds where all contributions are}\ \ge0\ —\ \text{spacelike-dominant compositions};\ k\ \text{is a signature datum, not orientation}\ [\mathrm{FT.23}]);\qquad k\ \text{odd}\Rightarrow j\in\tfrac12+\mathbb Z_{\ge0},\quad k\ \text{even}\Rightarrow j\in\mathbb Z_{\ge0};$$
$$(4)\quad\textbf{the obstruction}:\ \text{promoting}\ R(k)=k/2\ \text{from candidate to theorem requires one missing lemma — a corpus-level spin connection}: \text{an identification of the weak transport holonomy}\ \mathcal U_c=\mathrm P\exp\bigl(i\oint_c\textstyle\sum_Ac_A\mathcal G_A\,d\ell\bigr)\ [\mathrm{EW.33}] \text{with the frame rotation of the emergent metric along}\ c\ [\mathrm{CT1.13}\text{--}\mathrm{CT1.17}'\text{s Levi-Civita data lifted to the}\ SU(2)\ \text{carrier}\ [\mathrm{EW.32}]].$$
$$\text{Parts 1–3 contains every ingredient but the lift}:\ g_{\mu\nu}\leftrightarrow(a_{00},q_{ij},w_i)\ \text{dictionary with}\ w_i\ \text{in the}\ W\ \text{block}\ [\mathrm{CT1.12},\ \mathrm{FT.30}];\ \ \Gamma^\lambda{}_{\mu\nu},\ R^\rho{}_{\sigma\mu\nu}\ [\mathrm{CT1.13},\ \mathrm{CT1.14}];\ \ W_i=\tfrac12(\sigma_i^{(p)}+\sigma_i^{(q)})\ \text{total-spin generators}\ [\mathrm{FT.13},\ \mathrm{CT1.2}];\ \ \text{seed transport}\ [\mathrm{EW.32}/\mathrm{EW.33}]\ —\ \text{but}\ \neg\exists\ \text{tag constructing the spinor connection or tying}\ \oint\text{(weak)}\ \text{to}\ \oint\text{(frame rotation)}. \text{Without it,}\ k\ \text{(geometric winding)}\ \text{and}\ j\ \text{(weak Casimir)}\ \text{are independently derived integers/half-integers with no derived bridge};$$
$$(5)\quad\textbf{verdict}:\ j=k/2\ \text{remains the leading candidate}\ —\ \text{it passes every available consistency test}:\ (1)\ \text{parity triviality (it reads}\ k,\ \neg\text{parity});\ (2)\ \text{additive composition}\ [\mathrm{FT.34}(3)];\ (3)\ \text{seed anchor}\ R(1)=\tfrac12\ [\mathrm{EW.32}];\ (4)\ \text{half-integrality from odd winding}\ [\text{clause}(3)].\ \text{Promotion blocked exactly at Open Gaps 19 (spin connection)}\ —\ \text{not at any arithmetic step}.$$

### FT.53 — Geodesic constancy: the stationary on-shell ledger is constant-quantum

**Thm.** $(1)$ **Conservation.** Along any affinely parametrized geodesic of $g_{\mu\nu}$ [CT2.6]: $\frac{d}{d\lambda}\bigl(g_{\mu\nu}\dot x^\mu\dot x^\nu\bigr)=2\,g_{\mu\nu}\dot x^\mu(\nabla_{\dot x}\dot x)^\nu=0$ [math] — the sampled quantity $\kappa(\lambda)=g_{\mu\nu}\dot x^\mu\dot x^\nu$ is constant along the path.
$(2)$ **Constancy of the stationary on-shell ledger.** In CT1.19's regime, materialized chains contributing to the semiclassical spectrum sit at $\delta\Phi=0$ [CT1.20: $\delta\Phi\ne0$ cancels pairwise; $\delta\Phi=0$ dominates] $=$ geodesy [FT.48(1)]; CT1.19's sampling $\kappa_e=g_{\mu\nu}\dot x^\mu\dot x^\nu(\lambda_e)+O(\mathfrak h)$ then gives $\kappa_e=\kappa_0+O(\mathfrak h)$ with a single constant $\kappa_0$; on integrality-class edges [FT.24/FT.34(4): $\kappa_e\in\mathbb Z$] and small $\mathfrak h$: $\kappa_e=\kappa_0\in\mathbb Z$ **exactly** — FT.38(2)'s rigidity strengthened from eventual-local to exact-global on the stationary locus, without the integer-step $\varepsilon$-argument.
$(3)$ **Equality saturation.** On stationary on-shell channels: FT.33(4)'s Cauchy–Schwarz inequality and FT.48(2)'s two-sided law hold with **equality**: $\Lambda_c=L\sqrt{\kappa_0}$, $\ell^2=m\,d_{12}\,\mathfrak h^2$, $\overline{\sqrt\kappa}^{\,2}=\kappa_0$ — the FT.33 bridge ratio becomes a single-integer function: $m_{\mathrm{pole}}^2/m_{\mathrm{hid}}^2=\hat\mu^2\mathfrak h^4G(c)\,\kappa_0/(\ln2)^2$.
$(4)$ **Semiclassical exclusion of class (iii).** FT.38(3)'s rational non-uniform ladders ($\kappa_e\in(2/L)\mathbb Z$, varying) require $\kappa(\lambda)$ non-constant along the chain $\Rightarrow$ [contrapositive of (1)] non-geodesic support $\Rightarrow$ off-stationary $\Rightarrow$ pairwise cancellation in $Z$ [CT1.20] $\Rightarrow$ no semiclassical spectral contribution. Gap 13's class-(iii) residue reduces to finite-$\mathfrak h$ non-stationary materializations — the same $Z$-side residue as Open Gaps 18's selection question. **(item 18 closed [FT.66(5)]; the shared residue — finite-$\mathfrak h$ poles, now localized at clean-bifurcation loci [FT.66(3)], plus open-channel selection exits (a$''$)/(b) [FT.66(5)] — is tracked under item 13 alone.)**

### Def-H.21 — The spin connection on the emergent geometry (construction)

**Def.** On a spatial slice of CT2.6's $(M,g)$ [CT1.12: $\bar g_{ij}\succ0$ perturbatively], within a convex normal neighborhood [FT.47(3)] or, globally, on any orientable slice [math: orientable 3-manifolds are spin]:
$$(1)\quad\text{orthonormal frames}\ e_a=e_a{}^\mu\partial_\mu,\quad g_{\mu\nu}e_a{}^\mu e_b{}^\nu=\delta_{ab}\ (\text{spatial});\qquad(2)\quad\text{Levi-Civita connection}\ \Gamma^\lambda{}_{\mu\nu}\ [\mathrm{CT1.13}]\ \to\ \text{spin connection}\ \omega_\mu{}^{ab}=e^a{}_\lambda\nabla_\mu e^{b\lambda}\ [\text{math}];$$
$$(3)\quad SU(2)\to SO(3)\ \text{double cover}\ [\text{math}]\ \to\ \mathfrak{su}(2)\text{-connection}\ \tilde\omega;\qquad(4)\quad\text{carrier}:\ \mathcal H_{\mathsf v}\cong\mathbb C^2\ [\mathrm{EW.32}],\ \text{with}\ W_i\mapsto\tfrac12\sigma_i\ [\mathrm{EW.32}/\mathrm{CT1.2}:\ \text{the corpus's own basis match}];$$
$$(5)\quad\text{spinor holonomy around a closed loop}\ c:\ \mathcal U^{\mathrm{spin}}_c=\mathrm P\exp\bigl(i\!\oint_c\tilde\omega\bigr)\in SU(2);\qquad(6)\ \text{frame rotation angle}\ \Theta_R(c):\ \text{the}\ SO(3)\ \text{angle of the projected holonomy};\ \text{for}\ c=\partial S,\ S\ \text{disk-like in a constant-curvature slice}:\ \Theta_R=\iint_S K\,dA\ [\text{Gauss–Bonnet};\ \text{math}].$$
**No physical identification is made here**: $\mathcal U^{\mathrm{spin}}$ is *not* asserted to be EW.33's weak transport $\mathcal U$ (couplings $c_A$, P4 data) — that identification is the declared content of Def-H.37(2) (HistLog §I), and the obstruction to deriving it is Open Gaps 19. The construction is [math]-class over derived corpus objects [CT1.13, CT2.6, EW.32]; it adds no premise. A5/C11's node-level $SU(2)$ action is the corpus precedent for $SU(2)$ carriers.

### FT.54 — Exact holonomy-defect formula and the closed-form pole side (under Def-H.37(2))

**Thm.** $(1)$ **Exact SU(2) defect (state- and axis-independent).** For $U=\cos\phi\,\mathbb I+i\sin\phi\,\hat n\cdot\vec\sigma\in SU(2)$ and any unit $v\in\mathbb C^2$:
$$(U-1)^\dagger(U-1)=\bigl(2-2\cos\phi\bigr)\mathbb I=4\sin^2\!\bigl(\tfrac\phi2\bigr)\,\mathbb I\qquad\implies\qquad\|(U-1)v\|^2=2-2\cos\phi\ [\text{math; exact Pauli algebra}].$$
$(2)$ **EW.33 recovered as Taylor term.** Any traceless Hermitian $X=\vec x\cdot\vec\sigma$ satisfies $X^2=|\vec x|^2\mathbb I$; with $U=e^{iX}$, $\phi=|\vec x|$: defect $=2-2\cos|\vec x|=|\vec x|^2+O(|\vec x|^4)=\|Xv\|^2+O(X^4)$ — EW.33's leading-order defect $\ell_\gamma^2\|\sum_Ac_A\mathcal G_A\mathsf v\|^2$ is the expansion of the same exact quantity [consistency derived, not assumed].
$(3)$ **Spin-connection holonomy.** $\mathcal U^{\mathrm{spin}}_c=U(\phi=\Theta_R(c)/2)$ [Def-H.21(5)–(6); double cover: frame angle $\Theta_R$, spinor angle $\Theta_R/2$; sign convention irrelevant — $\cos$ even] $\Rightarrow$ defect$_{\mathrm{spin}}(c)=2-2\cos\bigl(\tfrac{\Theta_R(c)}{2}\bigr)=4\sin^2\bigl(\tfrac{\Theta_R(c)}{4}\bigr)$.
$(4)$ **Closed-form pole side (Def-H.37(2)).** Under Def-H.37(2) (clause (1)'s defect transport is the spin-connection holonomy):
$$m_{\mathrm{pole}}^2(c)=\hat\mu'^2\cdot4\sin^2\!\Bigl(\frac{\Theta_R(c)}{4}\Bigr),\qquad[\hat\mu'^2]=[m^2]=\mathfrak q\ [\mathrm{EW.33}\ \text{packaging pattern}];$$
for geodesic polygonal loops bounding disk-like $S$ in constant-curvature slices: $\Theta_R=\bar KA=\sum_i\alpha_i-(n-2)\pi$ [Gauss–Bonnet; FT.47(1)] — mass from the angle defect. Bridge ratio (Gap 7's well-posed object):
$$\frac{m_{\mathrm{pole}}^2}{m_{\mathrm{hid}}^2}=\frac{4\,\hat\mu'^2\,\mathfrak h^2\,\sin^2(\Theta_R/4)}{E_{\mathrm{int}}^2\,(\ln2)^2}\in\mathfrak q^0\qquad[\text{dimension check}:\ [\hat\mu'^2\mathfrak h^2]=\mathfrak q\cdot\mathfrak q^{-1}=\mathfrak q^0].$$
$(5)$ **Exact witness.** Unit-sphere octant triangle ($n=3$, $\alpha_i=\pi/2$, $A=\pi/2$): $\Theta_R=\pi/2$; defect $=2-2\cos(\pi/4)=2-\sqrt2\in\mathbb Q(\sqrt2)$ — an exact irrational ledger value, in the corpus's own radical-arithmetic class [checks/README pattern].

### FT.55 — The no-go and the surviving spin realization

**Thm.** $(0)$ **Admissibility (correction).** Throughout this tier and FT.52, the admissible spin label is $j=|k|/2$ with carrier $\mathrm{Sym}^{|k|}$: $\mathfrak{su}(2)$ labels require $j\ge0$ and the Casimir $j(j{+}1)$ distinguishes $\pm k/2$; stretched additivity is confined to the nonnegative cone (spacelike-dominant compositions) [FT.52(3) patched form]. $(1)$ **Calibration no-go.** The identification $\Theta_R(c)=2\pi k(c)$ (frame-holonomy angle $=$ winding $\times2\pi$) is **ruled out** as a corpus relation: $k=\oint ds^2/(2\mathfrak h^2)$ carries $\mathfrak h$-weight $-2$ [FT.31(3); D2.9], while $\Theta_R=\iint_S K\,dA$ is $\mathfrak h$-weight $0$ for fixed classical regions [Def-H.21(6)]; a proportionality between quantities of different calibration weight is not $\mathfrak h$-free and hence not a derived pure-number relation [CT2.11's criterion]. Consequently **the spin label cannot be read as the spin-connection holonomy angle of the same loop**.
$(2)$ **The surviving realization.** FT.52's unique rank-1 additive rule $R(k)=k/2$ has exactly one natural representation-theoretic realization: $j=|k|/2\iff$ carrier $\mathrm{Sym}^{|k|}(\mathcal H_{\mathsf v})$ — the $(|k|{+}1)$-dimensional irreducible $\mathfrak{su}(2)$ representation [math: classification; $k\ge0$ on the cone of clause (0)]. It satisfies every derived constraint: anchor $\mathrm{Sym}^1=\mathcal H_{\mathsf v}$, $j=\tfrac12$ [EW.32]; composition $\mathrm{Sym}^{k_1}\otimes\mathrm{Sym}^{k_2}\supseteq\mathrm{Sym}^{k_1+k_2}$ as maximal weight [math: Clebsch–Gordan] $=$ FT.34(3)'s additive winding law $k(\Gamma)=k_1+k_2+d_{12}$ on the stretched channel; parity triviality respected (the rule reads $k$, not $\mathrm{Hol}_{\mathrm{int}}$) [FT.52(1)]; half-integrality from odd $k$ [FT.52(3)].
$(3)$ **Scope consistency.** Elementary floors carry small $k$ [FT.28: $k=\kappa=1$ floor; FT.45/FT.42 minima: $k=O(1)$] $\Rightarrow$ small $j$; the large-$k$ regime is the classical-geometry limit [FT.31(3)], not particle territory — no macroscopic-spin contradiction.
$(4)$ **Residual, relocated.** What remains missing for promotion is neither the connection (Def-H.21 constructs it) nor the algebra (FT.52 settles it): it is a **ledger mechanism assigning $\mathrm{Sym}^k(\mathcal H_{\mathsf v})$ to a materialized chain of winding $k$** — a $k$-fold symmetric seed-tensoring tied to the winding count. EW.32 transports *one* qubit around the chain; nothing in Parts 1–3 tensors it $k$ times. Open Gaps 19, re-scoped to exactly this.

### FT.56 — Native ladder rungs, the spin–orbit decomposition, and the missing map

**Thm.** $(1)$ **The bottom rungs are native.** The candidate spin carriers for $j=0,\tfrac12,1$ are existing corpus objects with the correct dimensions $2j{+}1$ and Casimir labels:
$$j=0:\ \wedge^2\mathcal H_q\cong\mathrm{Sym}^0\ (\text{trivial},\ 1\text{-dim})\ —\ \text{the reality line}\ [\mathrm{A3},\ \mathrm{CT0.7}(1):\ \Pi_{\mathcal V}=\tfrac14(E_0-\Sigma),\ \mathfrak T\Pi_{\mathcal V}=1;\ \text{Casimir}\ 0\ [\mathrm{CT0.7a}];\ \sigma_e\ \text{lives here}\ [\mathrm{CT0.9}]];$$
$$j=\tfrac12:\ \mathcal H_{\mathsf v}\cong\mathbb C^2,\ W_i\mapsto\tfrac12\sigma_i\ —\ \text{the transported seed}\ [\mathrm{EW.32}];$$
$$j=1:\ \vee^2\mathcal H_q=\mathrm{Sym}^2(\mathcal H_q)\ (3\text{-dim})\ —\ \text{the pair channel's reality sector}\ [\mathrm{A3}:\ \mathcal H_p\otimes\mathcal H_q=\vee^2\oplus\wedge^2;\ \mathrm{CT0.7}(1):\ \Pi_{\mathcal R}=\tfrac14(3E_0+\Sigma),\ \mathfrak T\Pi_{\mathcal R}=3;\ \mathrm{CT0.7a}:\ \textstyle\sum_iW_i^2\big|_{\vee^2}=2=1(1{+}1)];$$
$$\text{and the reality grading is the placement rule}:\ \text{real edges carry}\ \vee^2\text{-weight}\ [\mathrm{A4}:\ |\Pi_{\mathcal V}\rho_{pq}|\le\varepsilon_q]\ —\ \text{the symmetric square is the corpus's own}\ \textbf{real}\ \text{sector}.$$
$(2)$ **Spin–orbit decomposition of the additive law.** $k(\Gamma)=k_1+k_2+d_{12}$ [FT.34(3)] reads, under the stretched rule on the nonnegative cone [FT.52(3), corrected form]: $j(\Gamma)=j(c_1)+j(c_2)+j_{\mathrm{rel}}$, $j_{\mathrm{rel}}=d_{12}/2$ — the connector's distance quanta contribute as a *relative* (orbital-type) term, the floors' own windings as intrinsic terms. On the cone this is exactly maximal-weight Clebsch–Gordan composition [math]; $\Theta$'s orientation-blindness [FT.23] makes $k$ (hence $j_{\mathrm{rel}}$) a **signature datum** — negative only for timelike-dominant connectors, where the cone condition fails and the read is out of scope.
$(3)$ **The missing map, stated exactly.** EW.32 transports *one* qubit around a materialized chain, regardless of its winding; no tag in Parts 1–3 (inventory) couples a $\Theta$-type ledger count to carrier multiplicity. What any candidate map winding $\to$ carrier must satisfy: (i) $k{=}1\mapsto\mathcal H_{\mathsf v}$ [EW.32 anchor]; (ii) $k{=}2$ must land in the channel's own reality sector $\vee^2=\mathrm{Sym}^2$ [clause (1) — the rung exists natively; the map must select it]; (iii) nonnegative-cone additivity [clause (2)]; (iv) admissibility $j=|k|/2$ [admissibility correction]. Gap 19 is exactly the construction of a map satisfying (i)–(iv) — or a no-go on such maps, which would reopen FT.52's constraint list to higher-rank rules.

### FT.57 — The boundary exchange algebra: root-space shape

**Thm.** $(1)$ **Decomposition.** For $N:=N(\Sigma)\ge1$: $\mathfrak u(N)=\mathfrak u(1)_{\mathrm{center}}\oplus\mathfrak{su}(N)$ [math; CT3.5's pattern at $N{=}3$]; relative to $\iota_\Sigma$'s factored diagonal $\bigoplus_e\mathfrak u(1)_e$ [Def-H.13: edge-wise assembly]:
$$\text{factored}=\text{diagonal}\ (N\ \text{dims},\ \text{incl. the centre});\qquad\text{strictly new}=\mathfrak{su}(N)\setminus\text{Cartan}=\text{root spaces}:\ (N^2{-}1)-(N{-}1)=N^2-N\ \ [\text{matches FT.41(d) exactly}].$$
$(2)$ **Shape at $N=2$.** The strictly-new sector $\{|e_1\rangle\langle e_2|+\mathrm{h.c.},\ i(|e_1\rangle\langle e_2|-\mathrm{h.c.})\}$ [FT.41(d)] is, with the factored traceless diagonal, an $\mathfrak{su}(2)$ triplet: $E_\pm=\tfrac12(\sigma_1\pm i\sigma_2)$, $[E_+,E_-]=\sigma_3$, $[\sigma_3,E_\pm]=\pm2E_\pm$ [math; machine-exact over $\mathbb Q(i)$] — the raising/lowering (charged-current) shape of D3.10's $W^\pm=\tfrac1{\sqrt2}(W_1\mp iW_2)$ [C8: $F_W=F_{W^+}\oplus F_{W^-}\oplus F_Z$], as algebra shape, not as identification.
$(3)$ **Hosting question, localized.** Which aspect block $\mathcal K^{(A)}$ the exchange modes land in under $\iota_\Sigma$ is **not determined by the current tags**: Def-H.13 defines $\iota_\Sigma$ by a factorization *requirement*, not by explicit matrices; the image of the root spaces in $\mathcal K=\bigoplus_A\mathcal K^{(A)}$ needs an explicit edge-block realization of Def-H.13's assembly [CT0.12 blocks $\otimes$ $\iota_{n(w_e)}$] — one named construction away (Open Gaps 16). Candidates remain: a second EM-type centre read is *excluded* by (1)–(2) (the exchange sector is nonabelian root-space, not central); a $W$-type hosting matches the charged-current shape; a genuinely new collective aspect remains possible.

### Def-H.22 — The explicit boundary realization (corolla and separated patterns)

**Def.** For $\Sigma$ with $N:=N(\Sigma)$ boundary edges $\partial\Sigma=\{e_1,\dots,e_N\}$, $\mathcal H_{\mathrm{slot}}(\Sigma)=\operatorname{span}\{|e_i\rangle\}$ [Def-H.12], $\iota_\Sigma$ is made explicit by contact pattern:
**(a) Corolla** (all boundary edges share one external vertex $w$; slots edge-labelled [A7: $\tau(v)$ records incident edges; D0.8] $\Rightarrow$ canonical inclusion $\mathcal H_{\mathrm{slot}}(\Sigma)\hookrightarrow\mathcal H^{(n(w))}_{\mathrm{slot}}$, equality iff $n(w)=N$):
$$\iota_\Sigma^{\mathrm{cor}}:=\iota_{n(w)}\big|_{\mathfrak u(N)}\qquad[\mathrm{D2.12}\ \text{applied to the subalgebra on the included slots}].$$
**(scope [FT.59])**: the formula is defined exactly for $n(w)\le3$ — at $n(w)\ge4$ no realization $\iota_{n(w)}$ exists [CT4.4 Pf(b): slot algebras realized only for $n\le3$]; the corolla read then degenerates to the registration/sealing ledger ($\sigma_e$, chain-local $f_v$, $q_{\mathrm{core}}$, $\mathcal C$) plus $D^-$-absorption [D4.1, D4.2], with the collective $\mathfrak u(N)$ wholly unhosted [FT.59(4)].
**(b) Separated** (boundary edges with distinct external vertices $w_1\ne w_2\cdots$): only the factored diagonal is defined — each edge's $\mathfrak u(1)_e$ maps through its own CT0.12 block and $\iota_{n(w_e)}$'s centre [D2.12: centre $\mapsto\mathcal K^{(\mathrm{EM})}$]; since $\dim\mathcal K^{(\mathrm{EM})}=1$ [CT0.14], all edge centres share one image line:
$$\iota_\Sigma^{\mathrm{sep}}\Bigl(\sum_ec_eD_e\Bigr)=\Bigl(\sum_ec_e\Bigr)Y_{\mathrm{asp}}\qquad[\mathrm{EM.2}:\ \mathfrak T(Y_{\mathrm{asp}})=1];\qquad\text{off-diagonal}\ |e_i\rangle\langle e_j|\ (i\ne j):\ \neg\exists\ \text{factored image (no cross-vertex bridge in the inventory)}.$$
No new choice is declared: (a) is the canonical edge-labelled slot inclusion composed with D2.12; (b) is forced by the 1-dimensional EM block. Every computed floor instantiates a pattern: single-contact floors [FT.28/FT.32/FT.42]: $N=1$; the face floor [FT.49]: corolla, $N=6$, $n(D)=6$ (equality) — in the void regime $n(w)\ge4$ [FT.59(4a)]: no realization, exchange sector kernel/absorbed; the two-contact $\Sigma_{\min}$ variant [FT.28 Rmk]: separated, $N=2$.

### FT.58 — Hosting classification and the no-hosting theorem

**Thm.** $(1)$ **Corolla hosting follows the CT0.13 ladder at the contact vertex.** Under Def-H.22(a): the centre of $\mathfrak u(N)$ maps to $\mathcal K^{(\mathrm{EM})}$ [D2.12]; and:
$$n(w)=2:\quad\iota_\Sigma(\mathfrak{su}(2))\subseteq\operatorname{span}\{W_i\}=\mathcal K^{(W)}\qquad[\mathrm{CT1.4}:\ W_i\ \text{close}\ \mathfrak{su}(2);\ \mathrm{D2.12}];$$
$$n(w)=3:\quad\iota_\Sigma(\mathfrak{su}(3))=\mathcal K^{(\mathrm{strong})}\qquad[\mathrm{D2.12}:\ \iota_3(\mathfrak{su}(3))\ \text{spans}\ \mathcal K^{(\mathrm{strong})};\ \mathrm{CT3.7}/\mathrm{CT3.8}:\ 8=8];$$
$$\text{the exchange generators host}\ \textbf{literally}:\quad\frac{\lambda_1+i\lambda_2}{2}=E_{12}\ (3\times3\ \text{matrix unit}):\ \ |e_1\rangle\langle e_2|\ \mapsto\ \text{the}\ \lambda_1,\lambda_2\ \text{directions};\quad D_1-D_2\mapsto\lambda_3\text{-type}\ [\mathrm{CT3.9};\ \text{machine}];$$
$$n(w)\ge4:\ \textbf{resolved (FT.59)}\ —\ \neg\exists\ \iota_n\ \text{realization at all for}\ n\ge4\ [\mathrm{CT4.4}\ \text{Pf}(b):\ \text{slot algebras realized only for}\ n\le3];\ \text{the suggested strong-hosting of}\ \mathfrak{su}(3)\ \text{subalgebras is impossible}\ [\mathrm{FT.59}(3)];\ \text{such corollas are wholly kernel}/D^-\text{-absorbed}\ [\mathrm{FT.59}(1),(4)].$$
$(2)$ **Separated contacts: the collective part is unhosted.** Under Def-H.22(b): $\operatorname{im}\iota_\Sigma^{\mathrm{sep}}=\mathcal K^{(\mathrm{EM})}$ (the total centre read, 1-dim); $\ker\iota_\Sigma^{\mathrm{sep}}\supseteq$ traceless diagonal ($D_1-D_2$: the two edge centres coincide in the 1-dim block); the off-diagonal exchange generators ($N^2-N$ dims [FT.41(d), FT.57(1)]) have **no factored image and no derived host**: no tag bridges distinct vertex slot algebras [inventory]. Ledger at $N=2$: $4=1\ (\text{image})+1\ (\text{kernel})+2\ (\text{unhosted})$.
$(3)$ **No-hosting theorem ($N\ge4$).** The observable aspect capacity is $\mathcal K_{\mathrm{pair}}^{\mathrm{obs}}\oplus\mathcal K_{\mathrm{stack}}^{\mathrm{obs}}$ with $\dim\mathcal K_{\mathrm{pair}}^{\mathrm{obs}}=5{+}1{+}3=9$ [$G,H,W$; $J^\pm,D^\pm$ never observable — FT.20] and $\dim\mathcal K_{\mathrm{stack}}^{\mathrm{obs}}=1{+}8=9$ [EM, strong; $D^-$ never — FT.20], the two commuting (distinct registers [CT0.12 Rmk]). For $N\ge4$: $\mathfrak{su}(N)$ is simple [math] with $\dim=N^2-1\ge15>9$; any Lie homomorphism $\varphi:\mathfrak{su}(N)\to\mathcal K_{\mathrm{pair}}^{\mathrm{obs}}\oplus\mathcal K_{\mathrm{stack}}^{\mathrm{obs}}$ has projections $\pi_{\mathrm{pair}}\circ\varphi$, $\pi_{\mathrm{stack}}\circ\varphi$ that are homomorphic images of a simple algebra (the factors commute) — hence trivial or injective; injective is impossible by dimension ($15>9$); therefore $\varphi\equiv0$ on $\mathfrak{su}(N)$: **the entire collective nonabelian boundary algebra maps to zero under every Lie-type-respecting hosting** [D2.12/D3.2's realization semantics] — not partially hosted: wholly kernel. The centre $\mathfrak u(1)$ still hosts in EM.
$(4)$ **Capacity ceiling, exact.** Nontrivial Lie hosting of $\mathfrak{su}(N)$ exists within the current inventory only for $N\le3$ [$\dim\mathfrak{su}(3)=8\le9$; $N{=}2$: $W$-hosting, $N{=}3$: strong-hosting, both realized by (1)]. For $N\ge4$ the coarse-grained read either kernels the collective structure (FT.26's mask keeps only hosted blocks) or the aspect inventory must grow by declaration — no derivation in Parts 1–3 supplies it. The kernel *is* the coarse-graining: $\dim\mathfrak u(N)=N^2$ vs $\dim\mathcal K_\Sigma\le18$ [FT.26(3)] forces $\ker\ne0$ already at $N=5$ by dimension alone.

### FT.49 — The tetrahedron-face floor: full card

**Thm.** Let $\Sigma_{\triangle}=\{A,B,C\}$ be the bidirectional 3-face of the bidirectional $K_4$ [FT.17 cross-check 2's setup], observed by the fourth vertex $D$ (six boundary edges). Under M2 (face-channel digons materialize [FT.24]) and M1 (both directed face triangles materialize [FT.22]):
$$(1)\quad E_{\mathrm{int}}=6,\quad E_{\mathrm{bd}}=6\le4\,\delta\tau\Rightarrow\delta\tau\ge2\ [\mathrm{FT.17}\ \text{hypotheses},\ \text{Def-H.35}];\qquad I_{\mathrm{hid}}=6\ln2,\qquad m_{\mathrm{hid}}=\frac{6\ln2}{\mathfrak h}\ \ [\text{the multi-tick observation cell of the taxonomy}];$$
$$(2)\quad\text{interior channel structure}=\Sigma_{P_3}'s\ [\mathrm{FT.45}\ \text{at}\ n{=}3]:\ \kappa\text{-lattice}\ \{\kappa\in\mathbb Z^3:\ \kappa_{AB}{+}\kappa_{BC}{+}\kappa_{CA}\in2\mathbb Z\}\ \text{of index}\ 2;\ \ \text{both directed triangles give the same constraint}\ [\mathrm{FT.23}:\ \text{orientation-even}];$$
$$(3)\quad\Theta_{\mathrm{int}}=2\,\Theta_{\triangle}=4\,k_{\triangle}\in4\mathbb Z,\qquad k_{\triangle}:=\Theta_{\triangle}/2\in\mathbb Z\ [\mathrm{FT.22}];\qquad\mathrm{Hol}_{\mathrm{int}}=+1\ [\mathrm{FT.25}(2)];\qquad W\ \text{row fires}\iff\Theta_{\triangle}\ne0;$$
$$(4)\quad\text{minimality regimes}\ [\mathrm{FT.45}(4)\ \text{at}\ n{=}3]:\quad\Theta_{\triangle,\min}=2\ (\text{null-carrying}\ (1,1,0)\text{-class}),\ 4\ (\text{strictly-spacelike}\ (1,1,2)\text{-class}),\ 6\ (\text{uniform}\ \kappa{=}2);\qquad\Pi=36\,\Theta_{\mathrm{int}}(\ln2)^2\in\{144,288,432\}(\ln2)^2;$$
$$(5)\quad\text{rungs and locks}:\ n(A)=n(B)=n(C)=6\ [\mathrm{D0.8}:\ 3\ \text{channels each in the}\ K_4];\qquad O(6)=2^7-16=112\ [\mathrm{CT0.5},\ \mathrm{CT0.6}]:\ \text{every vertex}\ D^-\text{-configured}\ [\mathrm{CT4.1}],\ \text{locked content retained and counted}\ [\mathrm{CT4.3},\ \mathrm{D4.2}];$$
$$(6)\quad\textbf{baryon-type sealing phase}:\ \text{all three vertices slot-carrying}\ (n\ge3\ [\mathrm{D3.1},\ \mathrm{CT0.13}:\ \text{rung-3 structure persists}]);\quad\mathcal C(\Sigma_{\triangle};C)=1\iff\text{the three attachments seal as one}\ \varepsilon\text{-type triple}\ [3=3\ \text{is the only}\ \{2,3\}\text{-partition}:\ \mathrm{FT.34}(5),\ g(3)=1\ \mathrm{FT.41}(b)]:\ \text{the first computed cell whose strong phase is exactly D3.9's baryon structure}\ B=\varepsilon_{ijk}q^iq^jq^k\ (\text{structural correspondence,}\ \neg\text{particle identification});$$
$$(7)\quad\mathcal A(\Sigma_{\triangle};C)\supseteq\{G,H\}\ [G:\ I_{\mathrm{hid}}\ne0;\ H:\ \mathrm{Def-H.36}];\quad\mathrm{EM}\iff\exists v:\ f_v\ne0;\quad\text{strong}\iff\varepsilon\text{-sealed};\qquad\dim\mathcal K=9\ (+1)\ (+8)\le18\ [\mathrm{FT.26}];$$
$$(8)\quad\text{boundary algebra}:\ N(\Sigma_{\triangle})=6\implies\mathcal H_{\mathrm{slot}}=\mathbb C^6,\ \iota_\Sigma:\ \mathfrak u(6)\ \text{of dimension}\ 36;\qquad\text{strictly new at}\ \Sigma:\ 36-6=30\ \text{real dimensions}\ [\mathrm{FT.41}(d)]\ —\ \text{the largest exchange sector computed}.$$

### FT.59 — The $\iota_{n\ge4}$ specification: non-existence, persistence refuted, hosting ceiling

**Thm.** $(1)$ **Non-existence (the specification question is void).** D2.12 defines $\iota_n:\mathfrak u(n)\to\mathcal K$ as the *aspect realization* of the rung-$n$ slot algebra. For $n\ge4$ no such realization exists: slot algebras are realized only for $n\le3$ [CT4.4 Pf clause (b), via CT3.20/CT0.11: $n\ge4\implies\neg$channel-admissible $\implies$ slot algebra $\neg$realized], and the locked sector that receives rung-$\ge4$ content carries no gauge structure — no generators, no internal directions [CT4.4; D4.1: $F_{D^-}$ a single possibility space; D4.2: absorption at rate $\propto O(n)$]. Hence D2.12's silence at $n\ge4$ is a non-existence consequence, not an underdetermination: **the unique derived read of rung-$n\ge4$ slot content is $D^-$-absorption at the ledger level** (locked, retained [CT4.3], never observable [FT.3, FT.20, D1.11]), while the observable reads at such vertices proceed through data that never required $\iota_n$: registration signs $\sigma_e$ and chain-local pass-through reads $f_v$ [CT0.9, D3.3, FT.21(i)], core charges [FT.40], and sealing configuration data [D3.8, CT3.17, Def-H.10].
$(2)$ **Lie-theoretic backup (if a linear $\iota$ were posited anyway).** Any Lie-homomorphic $\iota_n$, $n\ge4$, has $\iota_n(\mathfrak{su}(n))=0$: (a) observable side — $\mathfrak{su}(n\ge4)$ simple with $\dim=n^2-1\ge15>9=\max\dim$ observable factor [FT.58(3): every Lie-type-respecting hosting into $\mathcal K^{\mathrm{obs}}=9\oplus9$ is trivial]; (b) non-observable blocks admit no image either: $J^\pm$ spans are not Lie-closed ($[J_i,J_j]=i\epsilon_{ijk}W_k\notin\operatorname{span}\{J\}$ [CT1.6, CT1.9; machine over $\mathbb Q(i)$]) and a simple image inside $\operatorname{span}\{J_i\}$ is abelian-or-zero; $H$, $\mathrm{EM}$, $D^+$ blocks are $1$-dim abelian (simple nonabelian $\mathfrak{su}(n\ge4)$ has no nonzero abelian homomorphic image [math]); $G$ has $\dim5<15$; $D^-$ has no gauge structure [CT4.4]. Block-wise realization semantics [D2.12/D3.2: the isomorphism class must lie in an aspect block or the pair blocks of CT0.12] excludes spread embeddings: no single block contains an $\mathfrak{su}(n\ge4)$ isomorphism class ($\dim\le9<15$ in every block; $\mathfrak{su}(4)\not\subseteq\mathfrak{su}(3)$ [math: classification]). The centre read survives only where $\iota_n$ exists ($n\le3$): at $n\ge4$ the EM row runs on registration data, as in (1).
$(3)$ **Persistence refuted (FT.58(1)'s conditional branch resolved).** "Strong-hosting of $\mathfrak{su}(3)$ subalgebras at $n(w)\ge4$" is impossible: $\mathfrak{su}(3)_{ijk}\subset\mathfrak{su}(n\ge4)$ [machine: explicit matrix-unit embedding, bracket-closed inside the $15$-dim traceless span, CT1.9] together with (1)/(2) forces any hosted image of a slot $\mathfrak{su}(3)$ subalgebra at $n\ge4$ to vanish. CT0.13's "rung-3 structure persists" at $n\ge4$ is therefore necessarily **activation-level, not $\iota$-image-level**: strong $\in\mathcal A(n\ge4)$ means three-slot sealing substructures remain available as *configuration* data — attachments [D3.8], invariant contractions [CT3.17], the $\mathcal C$-projector [Def-H.10], the grammar $g$ [FT.41(b)] — not that $\iota_n$ hosts anything. **Hosting dies at rung 3; sealing persists at every rung.**
$(4)$ **Corollaries.** (a) *Face floor settled*: $\Sigma_\triangle$'s corolla contact has $n(D)=6$ [FT.49(5)]: no realization $\iota_6$ exists; its $30$-dim exchange sector [$\mathfrak u(6)=36=1+35$; strictly new $=30$: FT.49(8), FT.41(d)] is wholly unhosted — kernel under Lie semantics, $D^-$-absorbed ledger content under CT4.4's, observationally identical [FT.20: neither contributes an observable]. The first computed cell in this regime. (b) *Hosting ceiling, exact*: a corolla exchange algebra hosts nontrivially iff $N(\Sigma)\le n(w)\le3$: $N=2\to W$-hosted, $N=3\to$ strong-hosted literally [FT.58(1)]; every $n(w)\ge4$ corolla and every separated $N\ge2$ contact [FT.58(2)] is unhosted. FT.58(4)'s capacity ceiling $\mathfrak{su}(3)$ is now also the *realization* ceiling. (c) *Def-H.22(a) scope correction*: the corolla formula $\iota_\Sigma^{\mathrm{cor}}=\iota_{n(w)}|_{\mathfrak u(N)}$ is defined exactly for $n(w)\le3$; at $n(w)\ge4$ it is void, replaced by the absorption read of (1) — patched in place. The same domain restriction applies to Def-H.13's per-edge factor $\iota_{n(w_e)}$: a boundary edge whose external endpoint has rung $\ge4$ contributes no $\iota$-factor — its read is registration-plus-sealing data. Among computed cells only the face floor exercises the case (all six boundary edges end at $D$, $n(D)=6$); every other computed floor has environment contacts at $n(w_e)\in\{1,2\}$. (d) *Two ledgers, no identification*: the algebra-kernel ledger ($\dim\mathfrak{su}(n)=n^2-1$ unhosted) and the register-absorption ledger ($O(n)=2^{n+1}-16$ locked registers/tick [CT0.5, CT0.6, D4.2]) are different counts, both growing in $n$; neither converts into the other.

### Def-H.38 — The multiplicity–winding coupling

**Def.** A materialized closed bound chain $c$ [D1.5: bound content fermionic; FT.22: materialized] with winding $k(c)=\Theta(c)/2\ge0$ [FT.22, FT.25(3); the nonnegative (spacelike-dominant) cone, FT.52(3)] carries $k(c)$ symmetric copies of the transported seed:
$$
\textbf{multiplicity rule (constitutive clause):}\qquad \operatorname{copies}(c)\ :=\ k(c),
$$
realized on the carrier $\Psi(c)=\mathrm{Sym}^{k(c)}(\mathcal H_{\mathsf v})$ with the diagonal transport $\mathcal U_c^{\otimes k}\big|_{\mathrm{Sym}^k}$ [Def-H.23 — immediate below; EW.32: $\mathcal H_{\mathsf v}\cong\mathbb C^2$ the transported seed].

### Def-H.23 — The winding-multiplicity carrier map (under Def-H.38)

**Def.** For $c$ a **materialized closed bound chain** [D1.5: bound content fermionic; FT.22: materialized] with winding $k(c)=\Theta(c)/2\ge0$ [FT.22, FT.25(3)] — the nonnegative (spacelike-dominant) cone [FT.52(3) form]:
$$
\Psi(c)\ :=\ \mathrm{Sym}^{k(c)}\bigl(\mathcal H_{\mathsf v}\bigr)\ \subseteq\ \mathcal H_{\mathsf v}^{\otimes k(c)}\qquad[\mathrm{Def-H.38}:\ \text{multiplicity}=\text{winding};\ \ \mathcal H_{\mathsf v}\cong\mathbb C^2\ \text{the transported seed},\ \mathrm{EW.32}],
$$
where $\mathrm{Sym}^{k}$ is the common $(+1)$-eigenspace of all pairwise swaps on $\mathcal H_{\mathsf v}^{\otimes k}$ [math: the symmetric subspace; the swaps act as CT0.7's $\mathbb S$ on each tensor pair, adjacent transpositions generating $S_k$], and transport is the **diagonal action** $\mathcal U_c^{\otimes k}\big|_{\mathrm{Sym}^k}$ of EW.32's seed transport $\mathcal U_c$ around $c$ [EW.32, EW.33; Def-H.21(5) for the spin-connection form]. Boundary cases: $k=0$: $\mathrm{Sym}^0=\mathbb C$, the trivial carrier — representation-identified with $\wedge^2\cong\mathrm{Sym}^0$ [FT.56(1)], $\neg$subspace-identified; scope note: all-null trivial chains are transit objects (photons/gluons [D1.7, D3.7]) whose helicity content is a transit-side read [EM.8] — outside $\Psi$, no identification made. $k<0$ (timelike-dominant): outside the cone, $\Psi$ undefined [FT.52(3); FT.56(2)]. **Interface status (Def-H.38).** The corpus proves one seed transported per chain regardless of winding [EW.32]; the coupling *multiplicity $=k(c)$* is Def-H.38's constitutive clause — FT.60(7) proves it irreducible to decomposition, so the clause is load-bearing, not packaging.

### FT.60 — The multiplicity map: conditions, ladders, basis-relativity, and the honesty witnesses

**Thm.** Under Def-H.38, with Def-H.21's spin connection and EW.32's normalization:
$(1)$ **The four conditions hold.** $\Psi$ satisfies FT.56(3)(i)–(iv): (i) $k{=}1:\ \mathrm{Sym}^1=\mathcal H_{\mathsf v}$, $j=\tfrac12$ [EW.32 anchor]; (ii) $k{=}2:\ \mathrm{Sym}^2=\vee^2\mathcal H_{\mathsf v}$ — the channel's own reality sector, with projector $\Pi_{\mathcal R}=\tfrac14(3E_0+\Sigma)$ [CT0.7(1); A3] — and the *placement* is corpus-pinned: real $\iff$ support in $\vee^2$ at $\varepsilon_q=0$ [A4, CT0.8], so once two seeds share a materialized (real) register their symmetric grading is forced [CT0.7 Phys: reality $=$ Bose exchange symmetry]; only the multiplicity is interface content [Def-H.38]; (iii) cone-additivity: $\mathrm{Sym}^{k_1}\otimes\mathrm{Sym}^{k_2}\supseteq\mathrm{Sym}^{k_1+k_2}$ as maximal weight [math: CG] $=$ the additive winding law on the stretched channel [FT.34(3), FT.50(2), FT.56(2)]; (iv) admissibility: carrier dimension $k+1=2j+1$ with $j=|k|/2$ on the cone [FT.52(3) form; FT.55(0)].
$(2)$ **Uniqueness.** Any carrier assignment satisfying (i)–(iv) equals $\Psi$: the $(k{+}1)$-dim irreducible $\mathfrak{su}(2)$-module is unique up to isomorphism [math: classification; FT.55(2)] and the anchor fixes the seed [EW.32]. Gap 19's map exists and is unique under Def-H.38.
$(3)$ **Casimir ladder (CT0.7a generalized).** With $W_i\mapsto$ total-spin generators on $\mathcal H_{\mathsf v}$ [EW.32/CT1.2: the corpus's own basis match] and the induced diagonal action on $\mathrm{Sym}^k$:
$$
\textstyle\sum_i\bigl(W_i^{(k)}\bigr)^2=\frac{k}{2}\Bigl(\frac{k}{2}+1\Bigr)\,\mathbb I_{k+1}\qquad[\text{machine: exact rational matrices,}\ k\le6;\ \text{physics normalization}\ W=\tfrac12\cdot\text{generators}],
$$
recovering the native rungs verbatim: $k{=}0:\ 0$ on $\wedge^2$; $k{=}1:\ \tfrac34$ on the seed; $k{=}2:\ 2$ on $\vee^2$ — CT0.7a's eigenvalues are the $k\le2$ instances of one ladder [FT.56(1) extended from three rungs to all].
$(4)$ **Weight ladder.** For $\mathcal U=\exp(i\phi\,\hat n\cdot\vec\sigma)$ [FT.54's convention]: $\mathrm{Sym}^k(\mathcal U)$ has eigenvalues $e^{im\phi}$, $m\in\{k,k-2,\dots,-k\}$ — i.e. $\mathfrak{su}(2)$-weights $m/2\in\{j,j-1,\dots,-j\}$ at $j=k/2$, character $\sum_m e^{im\phi}$; on spin-connection transport $\phi=\Theta_R/2$ [Def-H.21(6)] [machine: diagonal transport over $\mathbb Q(i)$ at exact circle points; Laurent identity $(t^m-1)(t^{-m}-1)=2-t^m-t^{-m}$].
$(5)$ **Defect multiplet ladder (under Def-H.37(2)).** The CT2.5 defect read $\|(\mathcal U^{(k)}-1)\psi\|^2$ on the weight-$m$ vector [$m=k-2r$ in the $\phi$-labelling]:
$$
m^2_{\mathrm{pole}}(m)=\hat\mu'^2\bigl(2-2\cos(m\,\Theta_R/2)\bigr)=4\,\hat\mu'^2\sin^2\bigl(m\,\Theta_R/4\bigr),\qquad m\in\{k,k-2,\dots,-k\};
$$
$k{=}1$ reproduces FT.54(4) exactly and its *state-independence is special to the seed* ($m=\pm1$ agree by evenness); $k\ge2$ **splits into a multiplet**; every even $k$ carries a weight $m{=}0$ that is defect-massless at every curvature flux — the kernel coherence of FT.33(6)/FT.54 generalized to a standing zero of the ladder [machine: exact over $\mathbb Q(i)$; Chebyshev identity $2-2\cos(m\phi)=2-2T_m(\cos\phi)$ verified as integer-polynomial recursion].
$(6)$ **Composition at carrier level.** For $\Gamma=c_1\cdot P\cdot c_2\cdot\bar P$ materialized with $d_{12}=\Theta(P)\ge0$: $\Psi(\Gamma)=\mathrm{Sym}^{k_1+k_2+d_{12}}\subseteq\mathrm{Sym}^{k_1}\otimes\mathrm{Sym}^{k_2}\otimes\mathrm{Sym}^{d_{12}}$ as maximal weight [math: CG] — the spin–orbit decomposition $j(\Gamma)=j_1+j_2+j_{\mathrm{rel}}$, $j_{\mathrm{rel}}=d_{12}/2$ [FT.56(2)], now an inclusion of carriers, on the cone.
$(7)$ **Two honesty witnesses.** (a) *Basis-relativity*: the carrier assignment is per-chain, and a floor admits several admissible chain decompositions with the same total winding but different tensor carriers — witness (machine): the tetrahedron at uniform $\kappa_0=2$: the digon basis (M2) gives six chains of $k=2$: $\bigotimes^6\mathrm{Sym}^2$, dimension $3^6=729$; the face basis (M1) gives four faces of $k_f=3$: $\bigotimes^4\mathrm{Sym}^3$, dimension $4^4=256$; both have $\sum k=12=K_S$ [FT.43(1)'s sum rule is the invariance mechanism]. **Decomposition-invariant content**: $K_S$ and the stretched total $j_{\max}=K_S/2$ (and per-chain multisets up to the homology choice); the full floor-level tensor product is basis-relative — recorded, no canonical choice imposed. Only edge-disjoint decompositions [FT.25(1)] (the digon basis) support an unrestricted $\otimes$; face bases overlap on channels and their $\otimes$ is formal. (b) *Irreducibility of the multiplicity datum*: $\Psi$ is not "count materialized subloops" — the uniform-minimal triangle has $k=3$ [FT.45(4): $\kappa\equiv2$, $\Theta=6$] yet carries no materialized winding-$1$ *face* subloop ($\kappa\equiv1$ gives $\Theta=3$, odd, off-shell [FT.22; machine]), and the profile identity $(2,2,2)=(1,1,0)+(0,1,1)+(1,0,1)$ decomposes into null-carrying digon-supported profiles — different chains, not three winding-$1$ loops. EW.32 transports one seed per chain regardless of $k$; no tag ties tensor multiplicity to winding [FT.56(3)]. Def-H.38's single datum is therefore genuinely new — a transfer of exactly Def-H.37(2)s species.
$(8)$ **Inventory consequence, flagged.** $\mathrm{Sym}^k$ for $k\ge3$ ($\dim\ge4$) lies in multi-seed tensor spaces with no counterpart among the frozen $16$ pair registers [CT0.12 block dimensions $3,3,5,3,1,1$: no $4$-dim irreducible] nor the stack blocks: the carriers for $k\ge3$ exist as [math] objects on $\mathcal H_{\mathsf v}^{\otimes k}$ but exceed the registered aspect inventory — an inventory-extension consequence of Def-H.38, recorded here and joined to Gap 16's residue-(b) declaration question ($\mathcal K^{(\mathrm{exch})}$-species). No aspect claim is made for $k\ge3$ carriers.

### FT.61 — The selection side: phase inventory, index-blindness, and the two exits (Gap 18)

**Thm.** $(1)$ **Complete on-shell phase inventory.** For a configuration $C$ with on-shell integer edge data [FT.24/FT.34(4) scope], A8's weight assembles as
$$
w(C)=\mathcal J(C)\prod_{e\in E(C)}G(e)\cdot(-1)^{\aleph(\sigma,C)},\qquad\mathcal J(C)=1\ [\mathrm{D3.6}:\ (+1)\text{-factors only}],\qquad G(e)=\sigma_e\,e^{i\pi\kappa_e}\ [\mathrm{D3.5},\ \mathrm{FT.9}:\ \alpha=\pi;\ \mathrm{EM.20}],
$$
so the full phase is $\Phi(C)=\pi\bigl(\Theta(C)+\aleph(\sigma,C)+n_-(\sigma)\bigr)\ (\mathrm{mod}\ 2\pi)$ with $n_-:=\#\{e:\sigma_e=-1\}$: **the path-sum phase has exactly three $\mathbb Z_2$ registers — geometric ($\Theta$), wall ($\aleph$ [D3.3]), sign ($n_-$)** [CT0.9, CT0.10: the sign structures are independent; machine: exhaustive on $\Sigma_{\min}$ configurations].
$(2)$ **Geometric triviality on-shell.** On materialized closed chains $\Theta\in2\mathbb Z$ [FT.22] $\implies(-1)^{\Theta}=+1$: the surviving weight phase of any materialized-loop configuration is registration-only, $(-1)^{\aleph+n_-}$ — *no variational continuous component remains in the on-shell phase*. In particular the stationary channels of CT1.20's semiclassical locus carry constant $\kappa_0$ [FT.53(2)] and their complete geometric ledger record is the single integer $\kappa_0$ (plus $\delta h$ and $\Theta=2k$).
$(3)$ **Index-blindness witness.** There exist CT2.6-class geometries and pairs of closed geodesics $(\gamma_A,\gamma_B)$ with *identical* ledger records and *different* Morse indices: witness $M=S^2(R)\times S^1(2R)$ with the product metric [math: smooth complete Riemannian 3-manifold — a spatial-slice class in Def-H.21's sense; whether emergent dynamics realizes this slice is P4/solution data, recorded not claimed]: $\gamma_A=$ a great circle traversed twice — length $4\pi R$, Morse index $3$ [math: Morse index theorem; conjugate points at arc-distances $\pi R,2\pi R,3\pi R$ in the open interval; iterates of $S^2$ great circles: index $2m-1$]; $\gamma_B=\{\mathrm{pt}\}\times S^1(2R)$ — length $2\pi\cdot2R=4\pi R$ (equal), Morse index $0$ [flat factor; product formula; $\pi_1$-nontrivial so index $0$ is admissible — Synge's obstruction applies only to simply-connected slices]. At ledger scale $\mathfrak h=2\pi R/N$: both discretize to $\kappa\equiv1$ minimal-edge chains with $\delta h=\Theta=2N\in2\mathbb Z$ [FT.31(4), FT.22: materialization-eligible], $\sigma\equiv+1\implies\aleph=0,\ n_-=0$; by (1) both weights are $+1$, and $|w|^2=1$ for both [CT2.8's norms equally blind]. **No function of the weight data separates index $0$ from index $\ge1$ stationary channels.** *([FT.66(2)]: both witness members are degenerate — they sit in clean isometry-orbit critical manifolds ($\mathcal C_A=\mathbb{RP}^2\times S^1\times S^1$, nullity $4$; $\mathcal C_B=S^2\times S^1$, nullity $3$); the Bott indices remain distinct ($3$ vs $0$), the monodromy types differ ($I_2$ semisimple vs unipotent parabolic, Jordan-separated at identical trace/det), and the records and weights above are unchanged: this clause holds with "Morse index" read throughout as "Bott index" [Def-H.24].)*
$(4)$ **Two exits (theorem-shaped localization).** A selection criterion implementing "stable jumps materialize" [Def-H.19 vocabulary] must read the Morse index [math: index is the fluctuation-sign datum]. By (1)–(3) no weight-level or ledger-level read can supply it, and the mask/pole side reads stationary channels only through hosted blocks and superselection labels $(\Theta_{\mathrm{int}},k,q_{\mathrm{core}},m_{\mathrm{hid}},\mathcal C)$ [FT.26, Def-H.15(4), FT.58's inventory] — every entry index-blind by (2). Hence Gap 18's selection side is closed *against the current inventory*, with exactly two exits: **(a)** a new variational registration — a per-channel conjugate-point/Jacobi count appended to the ledger (a interface-definition species extending D0.7's retained-event vocabulary; nothing of the kind exists [inventory]) — **(reclassification [FT.66(3)]: the datum is reconstructable in principle from the ambient configuration's metric content [CT1.20's $C\mapsto g_{\mu\nu}(C)$; CT1.12/CT1.14/CT2.6] and eventually constant in $\mathfrak h$ away from bifurcation loci; the gap is a structural *coupling* — no A8/D2.11/D2.3/CT2.5 clause reads it — not a registration gap; exit (a) becomes a declared weight extension $w\mapsto w\,(-1)^{\operatorname{ind}_B}$, interface-definition species, not adopted)**; or **(b)** a spectral-side argument — positivity structure on $Z(\mathcal R,\Sigma)$ [CT2.8/CT2.5/Def-H.16] constraining which stationary families contribute poles without per-channel signs (not constructed; CT2.8 supplies norms, not pole-selection). The earlier "bridge construction" residue decomposes accordingly: the *leading* bridge is derived — materialization $\iff$ pole $\iff$ single-valued eigenmode at constant-$\kappa$ stationary channels [Def-H.16 closing line; FT.22; FT.53(2); CT2.5] — and the *next order* (fluctuation prefactors and signs) requires exactly (a) or (b).
$(5)$ **Consistency with CT1.20.** The witness pair sits inside CT1.20's own statement: stationary points dominate and are weighted alike — (3) upgrades "alike" from an absence of distinction to an identity of weights, at every ledger scale. Gap 13's finite-$\mathfrak h$ residue [FT.53(4)] inherits the localization: the excluded class-(iii) profiles were killed by *non-stationarity*; index-$\ge1$ stationary saddles are killed by nothing available.

### FT.51 — Enumeration of the winding ledger

**Thm.** For the polygon floor $\Sigma_{P_n}$ under M1/M2 [FT.45], at winding level $k$ (face constraint $\sum_i\kappa_i=2k$ [FT.45(3)]):
$$(1)\quad\#\{\text{on-shell profiles},\ \kappa\in\mathbb Z_{\ge0}^n,\ \textstyle\sum\kappa_i=2k\}=\binom{2k+n-1}{n-1}\qquad[\text{stars-and-bars};\ \text{math}];$$
$$(2)\quad\#\{\text{strictly-spacelike profiles},\ \kappa\ge1\}=\binom{2k-1}{n-1}\quad(2k\ge n;\ =0\ \text{otherwise});$$
$$(3)\quad\textbf{coarse-grained degeneracy}:\ \text{configurations related by mask-preserving relabeling are identified [CT2.6's}\ \sim\ \text{; CT2.7: weights are vertex-name independent], so the distinct ledger states at level}\ k\ \text{are the dihedral necklaces}$$
$$M(n,k)=\frac{1}{2n}\Bigl(\sum_{j=0}^{n-1}\mathrm{fix}(r^j)+\sum_{\text{reflections}}\mathrm{fix}\Bigr)\qquad[\text{Burnside};\ \text{math}],$$
with $\mathrm{fix}(r^j)=\binom{2k\,c/n+c-1}{c-1}$ if $(n/c)\mid 2k$, else $0$, where $c=\gcd(n,j)$ [rotation fixed points: $\kappa$ constant on the $c$ orbits]; machine values: $M(3,1)=2,\ M(3,2)=4,\ M(3,3)=7;\quad M(4,1)=3,\ M(4,2)=8$;
$$(4)\quad\textbf{growth}: \#\text{profiles}\sim(2k)^{n-1}/(n-1)!\ \text{as}\ k\to\infty\ [\text{math}]:\ \text{the winding ledger's state count grows polynomially in the winding at fixed}\ n,\ \text{degree}\ n{-}1\ —\ \text{a derived density of states for the floor family};$$
$$(5)\quad\text{sign registers factor}: \sigma\text{-assignments are independent of}\ \kappa\ [\mathrm{CT0.10}]:\ \text{total floor states at level}\ k=2^{2n}\cdot M(n,k)\cdot(\text{sealing/attachment data})\ —\ \text{the three registers multiply, none converts into another}.$$

### FT.62 — The bidirectional rung audit (correction theorem)

**Thm.** $(1)$ **Convention re-derivation; floor-card rungs.** The directed-rung law — $n(v)=\partial^{\leftarrow}(v)+\partial^{\rightarrow}(v)$ counts *directed real edges* [D0.8, A7]; the tick load is built from $\Phi^n\times\Phi^n$ sign configurations on the $n$ incident real edges [CT0.5 Pf; CT0.9: one bit per *directed* real edge]; every bidirectional channel contributes both orientations — is **CT0.11b (B)**. Floor-card rows [FT.28(5)'s explicit enumeration $n(p)=3=2{+}1$; Def-H.20's bidirectionality]:
$$
\text{single-directed-edge contact}:\ n(v_1)=2d+1;\qquad\text{bidirectional contact}:\ n(v_1)=2d+2;
$$
$$
\text{polygon}\ \Sigma_{P_n}:\ \text{dark}\ n(v)=4\ \forall v\ (\text{type}\ (2,2)),\ \text{contact}\ n(v_1)=5;\qquad\text{Platonic}\ \Sigma_S:\ \text{dark}\ n(v)=2d\in\{6,6,8,6,10\}.
$$
$(2)$ **Corrected lock table** [$O(n)=\max(0,2^{n+1}-16)$: CT0.6]:
$$
\begin{array}{c|c|c|c|c|c}
S & d & O(2d)\ \text{dark/vertex} & O(2d{+}1)\ \text{contact} & \sum_vO\ \text{dark} & \sum_vO\ \text{obs (1 edge)}\\ \hline
\text{tetrahedron} & 3 & 112 & 240 & 448 & 576\\
\text{cube} & 3 & 112 & 240 & 896 & 1024\\
\text{octahedron} & 4 & 496 & 1008 & 2976 & 3488\\
\text{dodecahedron} & 3 & 112 & 240 & 2240 & 2368\\
\text{icosahedron} & 5 & 2032 & 4080 & 24384 & 26432
\end{array}
$$
bidirectional-contact variants: contact $O(2d{+}2)\in\{496,496,2032,496,8176\}$, sums $\{832,1280,4512,2624,30528\}$ [machine].
$(3)$ **Saturation universality; the trichotomy retracted and replaced.** Universality — bidirectional real-edge subgraphs of channel degree $\ge2$ saturate: $D^-$-configured [CT4.1], content locked, retained, and counted [CT4.3, D4.2], inaccessible [D1.11] — the uniform minimal-saturation $2$-regular family (exactly one channel quantum over budget, length-independent), the degree-graded ladder, and the exact lock-free characterization (the *unidirectional* family on bidirectional skeletons): **CT4.1a (G)** [with CT0.11b (Part 1)]. The retraction record — FT.42(2)'s "accessibility trichotomy by degree" and FT.45(2)'s "no lock at any $n$ — the unlimited-accessibility family" are **retracted**, replaced by the frozen ladder above, with $\Sigma_{\min}$ ($n\in\{2,3\}$) and $\Sigma_L$ ($n\le3$) as its floor instances: $O=0$ [FT.28(5), FT.32(2) — unchanged by this audit]. Duality splitting survives and sharpens [FT.44(2) corrected]: cube $112$ vs octahedron $496$; dodecahedron $112$ vs icosahedron $2032$ — saturation grade splits both dual pairs.
$(4)$ **Invariance theorem.** $E_{\mathrm{int}}$, $I_{\mathrm{hid}}$, $m_{\mathrm{hid}}$, $\Theta_{\mathrm{int}}$, $K_S$, the $\kappa$-lattices and their indices, the winding sum rule, $g(V)$, $\Pi$, $S_{\mathrm{hid}}$, and every defect/holonomy entry are functions of edge-, channel-, and face-counts and of $\kappa$-profiles — none references $n(v)$: FT.42(1),(3),(4),(5) (lock columns excepted), FT.43, FT.44(1),(4), FT.45(1),(3),(4), FT.49–FT.51 stand unchanged [machine: value-by-value re-derivation]. The observed-variant information counts stand on retention: locked vertices retain and count [CT4.3; FT.17 cross-check 2 precedent]; the CT4.9(1) "visible $<3$" arithmetic anchors in FT.42(1)'s Pf (and FT.17 cross-check 3's) are **re-scoped**: at corrected contact rungs $n\ge7$ the contact vertex is locked, so its channel-visible content is governed by Def-H.35's locus-separation clause (per-vertex caps do not further reduce channel-visible content) and CT4.9(2)'s boundary form — not by CT4.9(1)'s accessible-vertex branch. Results unchanged; anchors corrected.
$(5)$ **Type ledger and the EM row (scope note).** Bidirectional-skeleton vertices with $d\ge2$ channels have type $(d,d)$ [D0.8/A7]; D3.3's literal $f_v$ domain (type-$(1,1)$ vertices) is empty on dark polygon and Platonic floors (the digon $\Sigma_{\min}$ keeps type-$(1,1)$ vertices — $\Sigma_{\min}$'s and $\Sigma_L$'s EM rows are untouched by this audit): the EM row of FT.42(4)/FT.20 evaluates on observed variants through chain-local pass-through reads along transit chains (chain-local telescoping: EM.9b (Part 2); EM.9 end-reads); dark floors carry the registration registers ($q_{\mathrm{core}}$ per closed core [FT.40]) with no channel read at all [FT.3]. Tracked as a cell-scope entry under Open Gaps 16 residue (c).
$(6)$ **Materialization sharpening.** M1/M2 at Platonic/polygon vertices are now explicitly spectral hypotheses at *locked* vertices ($n=2d\ge4$): strictly stronger than the text suggested. No contradiction with EW.17 (whose rung-$3$ claim concerns wrapping chains at channel-admissible vertices — a different existence locus): face/digon materialization, if it occurs, occurs through the generic CT2.5/Def-H.16 mechanism. Flagged for Open Gaps 13's class-(ii) wording ("under declared M2" — unchanged).

### Def-H.24 — Bott index, clean critical manifolds, and monodromy type for ledger channels (construction)

**Def.** Let $\gamma$ be a stationary channel [Def-H.19: $\delta\!\int ds^2=0$; FT.48(1)/FT.53(2): geodesic, constant $\kappa_0$] in a CT2.6 slice $(M,g)$ of the emergent geometry, closed (bound side) or fixed-endpoint (transit side). All items below are [math] constructions on derived data — $g$ from sector coordinates [CT1.12, D2.1], $\Gamma$ [CT1.13], $R^\rho{}_{\sigma\mu\nu}$ [CT1.14], sampling [CT1.19], coarse-graining [CT2.6 hypotheses (i)–(iii)] — no new physical input, in Def-H.21's construction class:
$(1)$ **Critical manifold.** $\mathcal C\ni\gamma$: the connected component of the stationary locus of the energy/ledger functional $\Theta\leftrightarrow\int ds^2$ [FT.31(2): the functionals coincide on-shell] in the coarse-grained loop space (closed case: free loops; transit case: fixed-endpoint paths). Isometry orbits of $(M,g)$ through $\gamma$ lie in $\mathcal C$; phase-shift and translation families likewise.
$(2)$ **Normal Hessian and Bott index.** $N_\gamma:=T_\gamma\Lambda/T_\gamma\mathcal C$ the normal space; $Q_\gamma$ the second variation (index form) restricted to periodic normal sections:
$$
Q_\gamma(V,V)=\int_0^L\Bigl(|\nabla_{\dot\gamma}V|^2-\bigl\langle R(V,\dot\gamma)\dot\gamma,\ V\bigr\rangle\Bigr)\,dt\qquad[R\ \text{from CT1.14 data};\ \text{math}],
$$
$$
\operatorname{ind}_B(\gamma):=\dim(\text{maximal negative-definite subspace of}\ Q_\gamma),\qquad\operatorname{nul}(\gamma):=\dim\ker Q_\gamma;
$$
$\gamma$ is **clean** iff $\ker Q_\gamma$ equals the orbit/tangential nullity (all kernel directions integrate into $\mathcal C$) — equivalently $\mathcal C$ is a nondegenerate critical submanifold [math: Morse–Bott]. $\mathcal C$-constant $\operatorname{ind}_B$; the naive Morse data of FT.61/Def-H.19 are the $\operatorname{nul}=0$ special case.
$(3)$ **Equivariant refinement (recorded, not needed scalar-wise).** Where $(M,g)$ carries an isometry group $\mathcal G$ with $\mathcal C=\mathcal G\cdot\gamma$ (the witness case), the normal Hessian is $\mathcal G_\gamma$-equivariant and the nullity carries the isotropy representation [math: equivariant Morse–Bott theory]; the selection-relevant scalar of stationary-phase weighting over $\mathcal C$ is the sign $(-1)^{\operatorname{ind}_B(\gamma)}$ with amplitude $\int_{\mathcal C}|\det{}'Q|^{-1/2}$ [math: Bott's explicit formula] — the sign datum Gap 18 asked about.
$(4)$ **Monodromy type.** The linearized Poincaré return map $P_\gamma$ on the symplectic normal space of the geodesic flow ($2(n{-}1)$-dim; $2$-dim for surface slices): semisimple/elliptic ($|\operatorname{tr}|<2$ or diagonalizable), parabolic-unipotent ($P\ne I$, $(P-I)^2=0$), hyperbolic ($|\operatorname{tr}|>2$), or $P=I$ (fully degenerate). Iterates: $\operatorname{ind}_B(\gamma^m)$ is determined by $P_\gamma$'s conjugacy class through Bott's iteration theory [math]; for $P=I$ on a surface the ladder follows from first principles by normal-mode counting — $\operatorname{ind}_B(\gamma^m)=2m-1$ (FT.66(2), machine), matching the classical spherical iterate indices [math: Bott's computation for great circles; cited as consistency, not re-derived here].
$(5)$ **Vocabulary fold.** Def-H.19's "stable" $:=$ $\operatorname{ind}_B=0$ (clean), "unstable" $:=$ $\operatorname{ind}_B\ge1$; the interface content of Def-H.19 shrinks accordingly (the Morse-theoretic vocabulary is now [math]-constructed; only the *non-coupling* clause remains declared — itself superseded in part by FT.66(4)'s derived anti-coupling for absolute rules on closed chains).

### FT.44 — Duality signature and the floor taxonomy

**Thm.** $(1)$ **Duality mass-degeneracy.** Dual solids exchange $(V,F)$ at fixed $E$ [math]: cube$\leftrightarrow$octahedron $(8,12,6)\leftrightarrow(6,12,8)$, dodecahedron$\leftrightarrow$icosahedron $(20,30,12)\leftrightarrow(12,30,20)$, tetrahedron self-dual $(4,6,4)$. Since $m_{\mathrm{hid}}=2E\ln2/\mathfrak h$ [FT.42(1)] and $\Pi=8E^2K_S(\ln2)^2$ [FT.42(5)] depend on $E$ only: **dual pairs are mass-degenerate and $\Pi$-degenerate at matched $K_S$** — cube/octahedron: $24\ln2/\mathfrak h$; dodecahedron/icosahedron: $60\ln2/\mathfrak h$; three mass values across the five solids.
$(2)$ **Ledger splitting.** The degeneracy is split by every finer ledger: independent windings $F-1$ (cube 5 vs octahedron 7; dodecahedron 11 vs icosahedron 19); lattice index $2^{F-1}$ ($32$ vs $128$; $2048$ vs $2^{19}$); sealing grammar $g(V)$ ($385$ vs $25$; $292938721075$ vs $164395$); lock profile $O(2d)$ (correction, FT.62(3): cube $112$ vs octahedron $496$; dodecahedron $112$ vs icosahedron $2032$ — saturation grade splits both dual pairs).
$(3)$ **Self-dual floor.** The tetrahedron is the unique self-paired cell ($V=F=4$): its winding and colour ledgers coincide in cardinality ($F-1=3$ independent reads; $g(4)=3$ groupings) — the smallest floor on which the full card, including a $\delta$-pair sealing grammar and a nontrivial winding ledger, is simultaneously active.
$(4)$ **Taxonomy (all computed floors).** Every fermion floor computed in this document obeys $m_{\mathrm{hid}}=E_{\mathrm{int}}\ln2/\mathfrak h$ with $E_{\mathrm{int}}=2E_{\mathrm{bidir}}+E_{\mathrm{uni}}$: $\Sigma_{\min}$: $E_{\mathrm{int}}=2$ [FT.28]; cycle ladder $\Sigma_L$: $E_{\mathrm{int}}=L$ (unidirectional) [FT.32]; $\Sigma_{12}$: $E_{\mathrm{int}}=6$ [FT.35]; Platonic family: $E_{\mathrm{int}}=2E$ [FT.42]. The informational mass is the directed-edge count, universally, across every computed cell.

### FT.63 — The Platonic physical cards: spin, charge, parity, holonomy, entropy, mass ratios, binding

**Thm.** For each Platonic floor $\Sigma_S$ [Def-H.20] under M1/M2 (interface clause), FT.62's corrected rungs, and — for the spin and defect-ladder rows — Def-H.38/Def-H.37(2) (interface clause): all seven requested computations close, per solid and universally. Write $(V,E,F,L,d)$ for the cardinals, $\kappa_{0,\min}=1$ (cube) / $2$ (all others) [FT.42(5)], $K_{S,\min}=E\kappa_{0,\min}$, $\delta_v=2\pi-d\,\frac{(L-2)\pi}{L}$ the vertex angle defect, and $k_{f,\min}=L$ ($L$ odd) / $L/2$ ($L$ even) the uniform-minimal face winding.
$(1)$ **Spin** [Def-H.38; Def-H.23, FT.60]: every materialized face chain carries winding $k_f$ with carrier $\mathrm{Sym}^{k_f}$ and label $j_f=|k_f|/2$; every channel digon carries $k=\kappa_{\mathrm{ch}}$, $j=\kappa_{\mathrm{ch}}/2$ [FT.24(1), FT.25(3)]. At the uniform minima:
$$
\begin{array}{c|c|c|c|c|c}
S & k_{f,\min} & j_f & K_{S,\min} & j_{\max}=K_S/2 & \dim:\ \text{face basis}\ /\ \text{digon basis}\\ \hline
\text{tetrahedron} & 3 & \tfrac32 & 12 & 6 & 4^4=256\ /\ 3^6=729\\
\text{cube} & 2 & 1 & 12 & 6 & 3^6=729\ /\ 2^{12}=4096\\
\text{octahedron} & 3 & \tfrac32 & 24 & 12 & 4^8=65536\ /\ 3^{12}=531441\\
\text{dodecahedron} & 5 & \tfrac52 & 60 & 30 & 6^{12}=2176782336\ /\ 3^{30}\\
\text{icosahedron} & 3 & \tfrac32 & 60 & 30 & 4^{20}=2^{40}\ /\ 3^{30}
\end{array}
$$
with the digon-basis check $\sum_{\mathrm{ch}}\kappa_{0,\min}/2=K_{S,\min}/2=j_{\max}$ [machine]. **Derived laws**: (a) $j_{\max}=K_S/2$ and the total winding sum $\sum_fk_f=K_S$ are decomposition-invariant [FT.43(1), FT.60(7a)]; the full tensor carrier is basis-relative (digon basis is the edge-disjoint one [FT.25(1)]). (b) $V,F$ even for all five solids $\Rightarrow$ at uniform minima every face $j_f$ composes to an **integer** stretched total ($F$ half-integer-or-integer summands, $F$ even) — Platonic floors are integer-spin objects in the stretched read at their minima, with half-integer face reads for the four odd-$L$ solids: fermion-like faces, boson-like stretched totals (structural observation, $\neg$particle identification). (c) Dual splitting, new column: $j_{\max}$ splits cube ($6$) from octahedron ($12$) but is *degenerate* for dodecahedron/icosahedron ($30$) — where the per-face structure splits instead ($5/2\times12$ vs $3/2\times20$) and the face-basis carrier dimensions split ($6^{12}$ vs $4^{20}$) while the digon-basis dimensions are degenerate ($3^{30}$ both).
$(2)$ **Charge** [FT.40, EM.9, D3.4]: the closed-core read $q_{\mathrm{core}}(c;v)=\tfrac12(\sigma_{e_1}-\sigma_{e_k})\in\{-1,0,+1\}$ is defined on every materialized closed core — faces, digons, and homology sums: $\beta_1=F-1$ independent core reads per solid $(3,5,7,11,19)$, ternary alphabet, all three values attained per solid [machine: explicit $\sigma$-assignments on the encoded skeletons]; $\omega$-rebase flips the sign [D2.6, FT.40]. Channel-facing charge: dark floors — no read channel [FT.3; FT.62(5)]; observed variants — EM.9 end-reads of transit chains through the contact, telescoping to boundary signs [FT.21(i)]; EM activity criterion $\exists v:\ f_v\ne0$ on chain-local reads [FT.42(4), FT.62(5) scope]. No independent weak or strong charge exists [FT.11, FT.12, CT3.22].
$(3)$ **Parity**: the on-shell $\kappa$-lattice is $\ker\varphi_S$, $\varphi_S:\mathbb Z^E\to\mathbb Z_2^F$ the face-incidence map — index $2^{F-1}=(8,32,128,2048,2^{19})$ [FT.43(3); machine: GF(2) elimination for **all five**, extending the earlier tetra/cube]; equivalently $\kappa\bmod2$ ranges over the **cut space** of $\Gamma_S$ (dimension $V-1=E-F+1$ — Euler again) [math: planar duality of the face-even lattice; machine: dimension identity + star-cut witnesses]. Consequences [machine]: $A_S(1)=0$ for all five (no bridges: single-channel $\kappa{=}1$ leaves two faces odd); $A_S(3)=V$ for $d{=}3$ solids (the vertex stars), $0$ for octahedron/icosahedron-at-$K{=}3$ (odd $K$ needs an odd cut; $|\delta S|\equiv d|S|\bmod2$); **octahedron: every face $2$-coloring balances $\sum_{\mathrm{black}}k_f=\sum_{\mathrm{white}}k_f=K_S/2$, hence $K_S\in2\mathbb Z$ and $A_{\mathrm{octa}}(\text{odd}\,K)=0$** [machine; the unique Platonic with even $d$]. On materialized loops: $\Theta\in2\mathbb Z$, $\mathrm{Hol}_{\mathrm{int}}=+1$ [FT.22, FT.25(1), FT.42(3)]; partial internal sets retain free parity [FT.25(3)]; on-shell weight phases are registration-only, $(-1)^{\aleph+n_-}$ [FT.61(1)–(2)].
$(4)$ **Holonomy**: $\mathrm{Hol}_{\mathrm{spiral}}=+1$ on every materialized loop [FT.22]; $\mathrm{Hol}_{\mathrm{int}}=+1$ [FT.25(2)]. Frame/spin-connection side [Def-H.21, FT.54]: the skeleton metric is piecewise-flat with conical defects $\delta_v$ at vertices — exact table $\delta_v/\pi=(1,\tfrac12,\tfrac23,\tfrac15,\tfrac13)$, and **Descartes/Gauss–Bonnet closes the ledger**: $V\delta_v=4\pi$ for all five [machine in exact $\pi$-units]. Hence the global spinor transport around any full sweep is $\exp(i\,\tfrac{4\pi}{2}\,\hat n\cdot\vec\sigma)=+\mathbb I$ — $4\pi$ is the SU(2) period [machine over $\mathbb Q(i)$]: spherical materialization is spinor-single-valued, a consistency anchor for M1. Loops cleanly enclosing one vertex (transverse to the singular locus — vertex-figure loops in the derived geometry) carry $\Theta_R=\delta_v$ [FT.47(1)/GB; Def-H.21(6)] and defect values $D_S=2-2\cos(\delta_v/2)=4\sin^2(\delta_v/4)$ — exact radicals, clause (6). 1-skeleton face loops sit *on* the singular locus (vertices on the loop): the smooth-enclosure defect read does not apply to them without a corner convention, undeclared — recorded, not guessed [Rmk below]. Under Def-H.38 the defect read becomes the multiplet ladder $m^2_{\mathrm{pole}}(m)=4\hat\mu'^2\sin^2(m\,\Theta_R/4)$, $m\in\{k,k{-}2,\dots,-k\}$ [FT.60(5)] — per-solid weight tables in (6). Weak-transport side: kernel coherence — charge-aligned profiles give $G(c)=0$, defect-massless, at every floor [FT.33(6), EW.22, EM.6].
$(5)$ **Entropy**: $S_{\mathrm{hid}}=I_{\mathrm{hid}}=2E\ln2=(12,24,24,60,60)\ln2$ nats [FT.42(1); FT.62(4): unchanged]; loop relating rate $S_{\mathrm{reg}}/A_{\mathrm{loop}}=(\ln2/\mathfrak h^2)/\bar\kappa$ [FT.37]: at the uniform minima $\bar\kappa=\kappa_{0,\min}$ — **the cube is the unique Platonic floor whose uniform-minimal loops saturate the CT1.29 Bekenstein rate $\ln2/\mathfrak h^2$ exactly**; the other four run at half rate ($\kappa_0=2$). Diagnostic minima $\Pi_{\min}=8E^2K_{S,\min}(\ln2)^2=(3456,13824,27648,432000,432000)(\ln2)^2$ — dual-degenerate at matched $K_S$ [FT.42(5), FT.44(1)]. Lock ledgers (corrected): $\sum_vO$ per variant from FT.62(2)'s table — the retained-but-inaccessible register rate, e.g. dark icosahedron $24384$/tick vs dark tetrahedron $448$/tick. Boundary entropy: dark floors $\partial\Sigma_S=\varnothing$; observed $E_{\mathrm{bd}}\in\{1,2\}$ [FT.42; CT1.29 applies to locked-interior separating surfaces — the Platonic lock ledger is vertex-absorption, not surface area; no identification].
$(6)$ **Mass ratios** [Def-H.37(2); FT.54(4)]: $m_{\mathrm{hid}}=2E\ln2/\mathfrak h$; the vertex-defect pole datum and the dimensionless ratio:
$$
\frac{m^2_{\mathrm{pole}}(\delta_v)}{m_{\mathrm{hid}}^2}=\frac{4\hat\mu'^2\,\mathfrak h^2\sin^2(\delta_v/4)}{4E^2(\ln2)^2}=\frac{\hat\mu'^2\mathfrak h^2}{(\ln2)^2}\cdot\frac{D_S}{4E^2}\in\mathfrak q^0\qquad[[\hat\mu'^2]=\mathfrak q,\ [\mathfrak h^2]=\mathfrak q^{-1}:\ \mathrm{D2.9}],
$$
$$
\begin{array}{c|c|c|c|c}
S & D_S=4\sin^2(\delta_v/4) & \text{exact field} & \text{min. polynomial of}\ D_S & D_S/4E^2\\ \hline
\text{tetrahedron} & 2 & \mathbb Q & x-2 & 1/72\\
\text{cube} & 2-\sqrt2 & \mathbb Q(\sqrt2) & x^2-4x+2 & (2-\sqrt2)/576\\
\text{octahedron} & 1 & \mathbb Q & x-1 & 1/576\\
\text{dodecahedron} & 2-2\cos\tfrac\pi{10} & \mathbb Q(\cos\tfrac\pi{10}) & x^4-8x^3+19x^2-12x+1 & D_S/3600\\
\text{icosahedron} & 2-\sqrt3 & \mathbb Q(\sqrt3) & x^2-4x+1 & (2-\sqrt3)/3600
\end{array}
$$
[machine: the dodecahedron quartic verified by exact substitution $x=2-2c$ into $\mathbb Z[c]/(16c^4-20c^2+5)$ — itself verified from $\cos5t=16c^5-20c^3+5c$ by de Moivre binomials at $t=\pi/10$; the cube/icosahedron quadratics from $(x-2)^2\in\{2,3\}$]. Weight-ladder values $D_S(m)=2-2\cos(m\,\delta_v/2)$, $m\le4$ [FT.60(5); machine]: tetrahedron $(2,4,2,0)$ — rational, with an exact zero at $m{=}4$; cube $(2{-}\sqrt2,2,2{+}\sqrt2,4)$; octahedron $(1,3,4,3)$ — rational; icosahedron $(2{-}\sqrt3,1,2,3)$; dodecahedron $D(2)=\tfrac{3-\sqrt5}2$, $D(4)=\tfrac{5-\sqrt5}2$ [machine in $\mathbb Q(\sqrt5)$ via $4c^2\mp2c-1$ at $c=\cos\tfrac\pi5,\cos\tfrac{2\pi}5$], $D(1),D(3)$ the two **smallest** of its four positive roots. **[precision correction [FT.76(10)]: the quartic $x^4-8x^3+19x^2-12x+1$ has four positive roots — $0.097886967410$, $0.824429495415$, $3.175570504585$, $3.902113032590$ (machine-isolated to width $2^{-60}$; $q(0..4)=(1,1,5,1,1)>0$, so no integer bracket separates them) — realized by the weights $m\in\{1,19\},\{3,17\},\{7,13\},\{9,11\}$ respectively; $D(1),D(3)$ are the two smallest.]** Def-H.37(1) form at stationarity: ratio $=\hat\mu^2\mathfrak h^4G(c)\,\kappa_{0,\min}/(\ln2)^2$ [FT.53(3)] with $\kappa_{0,\min}\in\{2,1,2,2,2\}$. **Derived law (dual splitting, pole side)**: both dual pairs share $m_{\mathrm{hid}}$ and $\Pi$ [FT.44(1)] but split on every defect datum — $\delta_v$: $\tfrac\pi2$ vs $\tfrac23\pi$; $\tfrac\pi5$ vs $\tfrac\pi3$; $D_S$: $2-\sqrt2$ vs $1$; $2-2\cos\tfrac\pi{10}$ vs $2-\sqrt3$ — FT.44(2)'s splitting template gains its first *irrational* column. Face loops carry $\Theta_R=0$ on the flat-face side (defect-massless), corner convention undeclared [Rmk].
$(7)$ **Binding-force contributions**: per-aspect ledger, all five solids:
$$
\begin{array}{c|c|c|c}
\text{aspect} & \text{criterion on}\ \Sigma_S & \dim\mathcal K^{(A)} & \text{binding read}\\ \hline
G & \text{always}\ (I_{\mathrm{hid}}=2E\ln2\ne0) & 5 & \kappa\text{-profile modulo loop constraint}\ [\mathrm{FT.41}(c)]\\
H & \text{always}\ (\mathrm{Def-H.36}\ \text{fold}) & 1 & m_{\mathrm{hid}}\ \text{read}\ [\mathrm{FT.20}]\\
W & \iff K_S\ne0\ (\text{at minima: always}) & 3 & \text{spin content of}\ (1)\ [\mathrm{FT.42}(3),\ \mathrm{Def-H.38}]\\
\mathrm{EM} & \text{observed/charged states}\ [\mathrm{FT.62}(5)] & 1 & q_{\mathrm{core}}\ \text{ternary per core}\ [(2)]\\
\text{strong} & \iff\ \text{inside-sealed phase}\ (\mathcal C=1) & 8 & g(V)\ \text{groupings; singlet-diagonal reads vanish}\ [\mathrm{FT.39}(2)]
\end{array}
$$
$\dim\mathcal K_{\Sigma_S}=9\ (+1)\ (+8)\le18$ [FT.26(3), FT.42(4)]. Sealing grammar: $g(V)=(3,385,25,292938721075,164395)$ [FT.41(b); machine: closed form vs enumeration for $V\le8$], with the **even-$\varepsilon$ theorem**: $V$ even for all five solids $\Rightarrow$ every grouping has an even number $b$ of $\varepsilon$-triples ($2a+3b=V$, $b$ even) [machine] — Platonic sealing phases are baryon-number-even by structure; the tetrahedron is meson-only ($b=0$: three $\delta\delta$-pairings), the octahedron admits $2\varepsilon$ phases ($15\,\delta^3+10\,\varepsilon^2$), the icosahedron $b\in\{0,2,4\}$, the dodecahedron $b\in\{0,2,4,6\}$, the cube $b\in\{0,2,4\}$ [machine: term breakdown]. Confinement is all-or-nothing [FT.19] with generic nonvanishing at $\mathcal C=1$ [FT.39(1)]; no per-edge strong phase exists [FT.29(2)]; strong binding contributes *admissibility structure and gluon modes*, never singlet expectation values [FT.39(2), CT3.13]. Boundary/exchange algebra: dark $N(\Sigma_S)=0$ (no boundary algebra); single-directed-edge contact $N=1$: nothing strictly new [FT.41(d)]; bidirectional contact $N=2$ corolla at $n(w)=2$: exchange doublet $W$-hosted literally [FT.58(1)]; the face-floor variant $N=6$, $n(D)=6$: exchange sector wholly kernel/$D^-$-absorbed [FT.59(4a)]. $D^-$: never observable, absorption-only [FT.20, CT4.4] — its binding contribution is the lock ledger of FT.62(2), by rate not by force.

### FT.66 — The Bott correction: witness re-evaluation, reconstructability, and the inadmissibility of absolute selection

**Thm.** $(1)$ **Framework.** Under Def-H.24, stationary ledger channels carry the Bott data $(\operatorname{ind}_B,\operatorname{nul},\mathcal C,[P_\gamma])$; for degenerate (isometry-orbit) families the stationary-phase weight is Bott's: sign $(-1)^{\operatorname{ind}_B}$, amplitude over $\mathcal C$ [Def-H.24(3); math]. The naive conjugate-point count of FT.61(3) is the fixed-endpoint special case; for closed channels the periodic count and the orbit quotient must replace it — executed in (2).
$(2)$ **The witness, re-evaluated (degeneracy critique absorbed; blindness Bott-stable).** On $M=S^2(R)\times S^1(2R)$ [FT.61(3)'s geometry]:
$$
\gamma_A\ (m{=}2\ \text{great circle}):\quad\mathcal C_A=\mathbb{RP}^2\times S^1_{\mathrm{phase}}\times S^1_{\mathrm{trans}}\ (\dim 4),\qquad\operatorname{ind}_B=3\ (=2m{-}1),\qquad\operatorname{nul}=4\ (\text{clean}),\qquad P_{\gamma_A}=I_2;
$$
$$
\gamma_B\ (\text{fiber circle}):\quad\mathcal C_B=S^2\times S^1_{\mathrm{phase}}\ (\dim 3),\qquad\operatorname{ind}_B=0\ (\forall\ \text{iterates}),\qquad\operatorname{nul}=3\ (\text{clean}),\qquad P_{\gamma_B}=\begin{pmatrix}1&L\\0&1\end{pmatrix}\ (\text{unipotent, parabolic});
$$
derivations (machine, exact): $\gamma_A$'s normal modes on the rank-1 normal bundle: $Q$-eigenvalues $\lambda_n\propto n^2-m^2$ on period-$L=2\pi Rm$ Fourier modes — negatives $\{|n|<m\}$: $2m-1$ of them; zeros $\{|n|=m\}$: the $2$-dim $\mathbb{RP}^2$ family motion; plus phase and translation tangents: $\operatorname{nul}=4=\dim\mathcal C_A$ — independent cross-check: Bott's iteration theorem at $P=I$ [math]. $\gamma_B$'s normal bundle is the trivial $TS^2$-pair with vanishing mixed curvature [product; math]: $Q=\int|J'|^2\succeq0$, kernel $=$ the $2$ constant basepoint fields: $\operatorname{ind}_B=0$, $\operatorname{nul}=3=\dim\mathcal C_B$; monodromy from $J=a+bt$: unipotent, iterates $\bigl(\begin{smallmatrix}1&mL\\0&1\end{smallmatrix}\bigr)$, Jordan type separating it from $P_{\gamma_A}=I_2$ at identical trace/det $(2,1)$ [machine]. **Verdicts**: (a) the Bott indices still differ, $3$ vs $0$, and the semiclassical signs would differ, $(-1)^3=-1$ vs $(-1)^0=+1$; (b) the ledger records and weights remain identical at every scale $\mathfrak h=2\pi R/N$: $(\kappa_0,\delta h,\Theta,n_-,\aleph)=(1,2N,2N,0,0)$, $w=+1$ both [FT.61(1),(3) re-run]; (c) hence **FT.61(3)–(4) hold with "Morse index" read as "Bott index"** — index-blindness of the weight inventory is Bott-stable, and the monodromy type (a conjugacy-class datum strictly finer than the index) is equally unregistered: no factor of $w(C)$ [A8; FT.61(1)'s complete inventory] can carry $(-1)^{\operatorname{ind}_B}$ or $[P_\gamma]$. (d) *Homotopy-class note*: $\gamma_A$ is contractible, $\gamma_B$ is not — the class is combinatorially present in the configuration [D0.10: $E(C)$ ordered], but (i) no validity/weight/mask clause reads it [A8, D2.11, D2.3/CT2.4: inventory], and (ii) it is not the index: within a fixed free homotopy class, stationary members of different $\operatorname{ind}_B$ exist [math: length-tuning by intermediate value + neck-deformation focusing], so no class read implements index selection.
$(3)$ **Reconstructability, and the true shape of exit (a).** The ambient configuration determines the metric: $C\mapsto g_{\mu\nu}(C)$ [CT1.20's own grouping map; CT1.12: $g$ from per-edge sector coordinates $(a_{00},q_{ij},w_i)$ [D2.1, D1.6, Def-H.14's arena]], sampled at $O(\mathfrak h)$ [CT1.19], coarse-grained to $(M,g)$ under CT2.6's hypotheses; hence $R^\rho{}_{\sigma\mu\nu}$ [CT1.14] along and near the channel, the normal Jacobi operator, and $(\operatorname{ind}_B,\operatorname{nul},[P_\gamma])$ are **in-principle functionals of the ambient configuration** in the CT2.6 regime — the datum is reconstructable, *not* missing. Integer-valuedness plus $O(\mathfrak h)$ convergence gives eventual $\mathfrak h$-stability away from clean-bifurcation loci [FT.38(2)'s rigidity pattern; machine: minimal mode gap $|n^2-m^2|\ge1$ in scaled units — perturbations below half the gap cannot flip signs]; at the loci themselves the index jumps — those are precisely the finite-$\mathfrak h$ residue of items 13/18. What is missing is a **structural coupling**: no clause of A8's weight [FT.61(1)], D2.11's validity, D2.3's masks, or CT2.5's pole condition reads the datum; and the resolvent side is *sign-free by hermiticity* — poles are conditions $\lambda_a=1$ on a real spectrum with residues $-\langle\mathrm{out}|P_a|\mathrm{in}\rangle$ [FT.26(1), CT2.5]: no per-saddle sign can live there without extending the structure. FT.61(4)'s exit (a) is accordingly reclassified: from "new variational registration (interface-definition species extending D0.7)" to "**a declared weight extension** $w\mapsto w\cdot(-1)^{\operatorname{ind}_B}$ (interface-definition species; well-definedness in the continuum regime supplied by the eventual-constancy lemma above) — constructible, not adopted here"; exit (b) (spectral-side positivity) unchanged, not constructed.
$(4)$ **The selection dilemma (absolute index-0 rules are inadmissible for closed chains).** Let a floor's ambient slice realization be a topological sphere carrying $K\ge0$ with $K>0$ somewhere — the class instantiated by every Platonic cone-sphere realization: faces flat, conical defects $\delta_v>0$ at vertices, total $V\delta_v=4\pi>0$ [FT.63(4); smoothed approximation; math]. On any such slice:
$$
\text{every non-constant closed geodesic has}\ \operatorname{ind}_B\ge1\qquad[\text{math: Synge/shortening — every closed geodesic on}\ S^2\ \text{bounds a disk and is exceeded by the disk-sweep};\ \text{machine: the latitude-push second variation}\ L''(0)=-2\pi/R<0\ \text{exactly},\ \text{and the round-sphere ladder}\ 2m{-}1\ge1\ \forall m].
$$
Hence an absolute selection rule — "index-0 stationary channels materialize; $\operatorname{ind}_B\ge1$ channels are suppressed" — admits **no** closed stationary channel on such a slice. Dilemma against M1/M2 (declared face/digon materialization [Def-H.20]): **horn 1** — if the declared materializations contribute semiclassically [FT.53(2)'s regime: stationary $=$ geodesic support], the absolute rule suppresses them all, contradicting M1 — the rule is inadmissible; **horn 2** — if they do not (Platonic face loops are corner loops of the cone metric, $\neg$geodesic: non-stationary in the smooth read), then closed-loop materialization lives entirely in the finite-$\mathfrak h$ non-stationary residue [FT.53(4); item 13], where no stationary-index criterion applies at all — stability selection is *vacuous* for bound chains. On either horn, **"stable jumps materialize" is refuted as the mechanism for closed (bound) chains** in this curvature class. Corollaries: (a) the class-relative variant also fails on simply-connected slices (a single free homotopy class: class-minimality collapses to global minimality, attained only by degenerate constant loops) [math]; (b) on Synge-class slices, Def-H.19's "stable jumps" ($\operatorname{ind}_B=0$) exist only among *open* fixed-endpoint channels (short arcs [FT.48(3)]) — the program's stability idiom is transit-side vocabulary by necessity, a derived clarification of Def-H.19's usage; (c) any viable selection criterion for closed chains must be spectral-side (exit (b)) or finite-$\mathfrak h$ (item 13's residue) — never an absolute variational index.
$(5)$ **Verdict (Gap 18 closed).** The four sub-questions of item 18 now carry derived answers: variational side — closed [FT.48(1)–(3)]; weight/ledger blindness — closed [FT.61(1)–(3)], Bott-stable [(2) here]; reconstructability — settled [(3) here]: the datum exists in principle, the coupling does not, and the resolvent side is sign-free; selection for **closed chains** — answered **negatively** [(4)]: no index criterion can operate, and the absolute rule is inadmissible against M1. Residue, transferred to item 13 in exact form: open (transit) channels — where index-0 minimizers exist [FT.48(3)] — remain unselected by anything in the inventory; the two exits stand: (a$''$) the declared weight extension of (3) (interface-definition species; not adopted), (b) spectral-side positivity on $Z(\mathcal R,\Sigma)$ [CT2.8/CT2.5/Def-H.16; not constructed]; plus the finite-$\mathfrak h$ bifurcation-locus residue shared with class (iii) [FT.53(4)]. This residue is the chain's honest end: closing it further requires a construction or declaration outside the frozen inventory — the same species boundary as Def-H.37(1)/Def-H.37(2)/Def-H.38.
$(6)$ **Folds.** Def-H.19's vocabulary is refined to Morse–Bott [Def-H.24(5)] — its [math] content constructed; the non-coupling clause superseded in part by clause (4)'s derived anti-coupling, itself superseded for absolute closed-chain rules by (4); Def-H.19 patched in place; FT.48(3)'s trichotomy scoped to clean fixed-endpoint problems (conjugate endpoints degenerate: read via Def-H.24) [Status note]; FT.61(3)–(4) confirmed and reclassified per (2)–(3); FT.53(4)'s "identical to item 18's residue" now points at item 13 alone.

### Def-H.25 — Skeleton configuration sums and the bypass vocabulary

**Def.** A **skeleton** $\Gamma$ $:=$ a finite bidirectional potential-edge set — the 1-skeletons of Def-H.20 (Platonic floors) and FT.45 (polygon floors), or any finite subgraph thereof. A **crystallization pattern** is a subset $R\subseteq E_{\mathrm{dir}}(\Gamma)$ [A4 per directed pair; D0.1: $\mathcal R$ membership is per-pair]; at $v$: $k_v:=\#\{e\in R: e\ni v\}=\partial^{\leftarrow}_R(v)+\partial^{\rightarrow}_R(v)$ [D0.8], potential degree $n(v)=| \{e\in E_{\mathrm{dir}}(\Gamma): e\ni v\} |$. Classification [CT0.11, CT4.1]: $v$ **channel-admissible** $\iff k_v\le3$; $v$ **$D^-$-locked** $\iff k_v\ge4$. A pattern is a **bypass configuration** iff every vertex is admissible while some has $n(v)\ge4$; the **bypass deficit** at $v$ is $n(v)-k_v$ (the virtual edges at $v$). The **skeleton configuration sum** (A8's weight restricted to skeleton-supported configurations [A8, D0.10], at CT1.20's grouping layer):
$$
Z_\Gamma\ :=\ \sum_{R\subseteq E_{\mathrm{dir}}(\Gamma)}\ \sum_{\sigma\in\{\pm1\}^R} w(R,\sigma),\qquad w(R,\sigma)=\mathcal J\cdot\prod_{e\in R}G(e)\cdot(-1)^{\aleph(\sigma,R)},\qquad G(e)=\sigma_e\,e^{i\pi\kappa_e}\ [\mathrm{D3.5},\ \mathrm{FT.9}],
$$
split $Z_\Gamma=Z_{\mathrm{byp}}(\Gamma)+Z_{\mathrm{lock}}(\Gamma)$ by lock status (any $k_v\ge4$). **Scope declarations, marked at every use**: **(S1)** minimal-edge class $\kappa_e\equiv1$ on real edges [D1.1, Comm-min]; for general on-shell integer $\kappa$: every theorem below is unchanged with values scaled by $(-1)^{\sum_e\kappa_e}$ — the cover classification is $\kappa$-independent. **(S2)** $\aleph$ in D3.3's literal type-$(1,1)$ domain; $\aleph_v=0$ at all other types; the chain-local extension [FT.21(i), Open Gaps 16(d)] would change the survivor class — flagged load-bearing (Rmk of FT.67). **(S3)** seal/Janus bookkeeping suppressed: the sum is over static patterns; $\mathcal J=1$ identically [D3.6]; universe-level balance $\#J^+=\#J^-$ [D1.3, D2.11] is ambient data, not a skeleton constraint. **(S4)** virtual edges contribute weight $1$ and no phase — no registration exists for them [A4, D0.5/A7: $\phi_e$ is defined on $e\in E_{\mathcal R}$]. Finite skeleton $\Rightarrow$ finite sum: convergence is trivial; growth-rate statements are made per family (FT.68(7)).

### FT.67 — The exact-cover theorem and the single-vertex bypass

**Thm.** Under Def-H.25 with (S1)–(S4):
$(1)$ **The $\aleph$ identity.** At a type-$(1,1)$ vertex $v$ with in-edge $e_\leftarrow$, out-edge $e_\rightarrow$: $(-1)^{\aleph_v}=(-1)^{|f_v|}=\sigma_{e_\leftarrow}\sigma_{e_\rightarrow}$ [D3.3: $f_v=\tfrac12(\sigma_\rightarrow-\sigma_\leftarrow)\in\{-1,0,1\}$; $\sigma$'s binary [CT0.9]; machine].
$(2)$ **Exact-cover theorem.** For $e\in R$ let $\operatorname{cov}(e):=\#\{(1,1)\text{-type endpoints of }e\text{ in }R\}\in\{0,1,2\}$. Then the weight is the monomial
$$
w(R,\sigma)=(-1)^{\sum_e\kappa_e}\prod_{e\in R:\ \operatorname{cov}(e)\ \mathrm{even}}\sigma_e\ ,\qquad[\text{display correction: the}\ \sigma_e\text{-exponent is}\ 1+\operatorname{cov}(e),\ \text{so the surviving factors are the even-coverage edges — as this clause's own Pf records; classification and values unchanged}]
$$
and the sign sum evaluates exactly:
$$
\sum_{\sigma\in\{\pm1\}^R}w(R,\sigma)=\begin{cases}(-1)^{\sum_e\kappa_e}\,2^{|R|}=4^{\,|\mathcal C|}\,(-1)^{\sum\kappa} & \text{if}\ \operatorname{cov}(e)=1\ \forall e\in R\quad(\textbf{pass-through cover};\ \mathcal C:=\{(1,1)\text{-vertices}\}),\\[2pt] 0 & \text{otherwise,}\end{cases}
$$
with $|R|=2|\mathcal C|$ forced on covers [each center contributes its in- and out-edge; every edge once]. At (S1): value $=4^{|\mathcal C|}>0$. [Machine: exhaustive on the tetrahedron (all $4096$ patterns $=$ all $3^{12}$ (pattern,sign) pairs), on $P_3,P_4,P_5$ exhaustively, on the cube exhaustively for $K\le4$ ($12831$ configs) plus a deterministic stride sample.]
$(3)$ **Structural corollaries (what cancels, what survives).** (a) Every directed cycle cancels: along a cycle of $(1,1)$-vertices each edge has $\operatorname{cov}=2$ — **no bound cell survives at the amplitude layer**: digons (the $\Sigma_{\min}$ pattern [FT.28]), directed cycles (the $\Sigma_L$ pattern [FT.32]), face boundaries, and the fully crystallized Def-H.20 floors (all vertices type $(d,d)$, $d\ge2$: no centers at all) all have $\sum_\sigma w=0$; (b) single real edges and length-1 threads cancel ($\operatorname{cov}=0$); (c) threads of length $\ge3$ cancel (interior edges double-covered); (d) **survivors $=$ V-thread networks**: each center $v\in\mathcal C$ pairs one in-edge $(s\to v)$ with one out-edge $(v\to t)$; non-centers are sources $(0,1)$, sinks $(1,0)$, or hubs of any type $\ne(1,1)$ — *including locked hubs* ($k\ge4$) whose every edge is paired by a distinct center; every survivor has even $|R|=2|\mathcal C|$ and value $4^{|\mathcal C|}$.
$(4)$ **Single-vertex enumeration ($n\in\{4,5,6\}$, balanced types).** $2^n$ patterns, $\binom nk$ at size $k$; admissibility fractions
$$
f_{\mathrm{adm}}(4)=\tfrac{15}{16},\quad f_{\mathrm{adm}}(5)=\tfrac{13}{16},\quad f_{\mathrm{adm}}(6)=\tfrac{21}{32}\qquad\Bigl[\ =\sum_{k\le3}\binom nk/2^n\Bigr];
$$
sign-summed amplitudes: $Z_{\mathrm{byp}}^{\pm}(v,n)=1+4\,n_{\mathrm{in}}n_{\mathrm{out}}=(17,25,37)$ — vacuum $+$ the $\binom{n_{\mathrm{in}}}{1}\binom{n_{\mathrm{out}}}{1}$ pass-through patterns at $4$ each; **only $k\in\{0,2\}$ survive**; $Z_{\mathrm{lock}}^{\pm}(v,n)=0$ (locked $\Rightarrow$ type $\ne(1,1)$ $\Rightarrow$ uncovered). At $\sigma\equiv+1$: $Z_{\mathrm{byp}}=-\binom{n-1}{3}\in\{-1,-4,-10\}$, $Z_{\mathrm{lock}}=+\binom{n-1}{3}$, total $(1-1)^n=0$ [alternating partial-binomial identity; binomial theorem; machine]. Aspect activation per pattern [CT0.13]: $\mathcal A(0)=\{J\}$, $\mathcal A(1)=\{J,G,W,H,D^+\}$, $\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\}$, $\mathcal A(3)\cup\{\text{strong}\}$; mask dimensions $\dim\mathcal K_k=(6,16,17,25)$ [CT0.14]; observable strong never fires at a single vertex [FT.27]; EM is state-dependent: $f_v\ne0$ on exactly half of the pass-through sign assignments [D3.3; machine].
$(5)$ **Virtual bypass theorem (single-vertex form).** Every vertex of potential degree $n\ge4$ with $n_{\mathrm{in}},n_{\mathrm{out}}\ge1$ has strictly positive admissible-sector amplitude, $Z_{\mathrm{byp}}^{\pm}=1+4n_{\mathrm{in}}n_{\mathrm{out}}>0$, independent of the $\kappa$-class up to the global sign $(-1)^{\sum\kappa}$; its locked sector vanishes identically. **[scope: the locked-sector clause is a literal-domain (S2) theorem — in the chain-local domains E1/E2 of Def-H.27 an isolated locked vertex has strictly positive amplitude, $Z^{\pm}_{\mathrm{lock}}=(32,96,672)$ for $n=(4,5,6)$, with the locked digon-hub family at $(!a)4^a$ [FT.75(1)]. The bypass clause is domain-invariant.]** **$D^-$ locking is avoided with nonzero amplitude by partial crystallization** — the bypass mechanism is real at the amplitude layer, and its surviving content is exactly the pass-through (transit) sector [D1.5: open, propagating $=$ bosonic content].
$(6)$ **Consistency anchors and the norm layer.** (a) The $k{=}2$ survivor is the $\Sigma_{\min}$ pass-through structure verbatim [FT.28(5): $q$ of type $(1,1)$]; (b) FT.61(1)'s phase inventory $e^{i\Phi}=(-1)^{\Theta+\aleph+n_-}$ is reproduced termwise inside the monomial of (2) [machine]; (c) **no conflict with positivity**: $|w(R,\sigma)|=1$ for every pair, so CT2.8's norms $\langle A|A\rangle=\sum|w|^2>0$ never cancel — the cancellations of (2)–(3) are amplitude-layer ($Z$) facts; the spectral layer [Def-H.16: poles of the masked resolvent] and the materialization declarations M1/M2 are untouched (the layer bridge is item 13's residue — see FT.68(4)).

### FT.68 — Joint skeletons: tetrahedron, the polygon ladder, the cube; the layer dichotomy; flicker

**Thm.** Under Def-H.25/FT.67 (same scopes):
$(1)$ **Tetrahedron (exhaustive).** $V=4$, potential $n(v)=6$ [FT.62(1)], $12$ directed edges. Consistency (each directed edge real at both endpoints or virtual at both — reality is one global fact per pair [A4, D0.1]) reduces the $4$-tuple space $2^{24}$ to $2^{12}=4096$ joint patterns. Bypass configurations: $1230$; **bypass probability** $\tfrac{615}{2048}$; $K\le6$ forced ($\sum_vk_v=2K\le4\cdot3$); counts by $K$: $(1,12,66,220,435,408,88)$ for $K=0..6$ (all-patterns: the symmetric row $\binom{12}K$ minus locked); orbits under $S_4$: $70$ total, by $K$: $(1,1,5,13,23,21,6)$. Amplitudes:
$$
Z^{\pm}_{\mathrm{byp}}=1057=1+24\cdot4+60\cdot16,\qquad Z^{\pm}_{\mathrm{lock}}=448=12\cdot16+4\cdot64,\qquad Z^{\pm}_{\mathrm{all}}=1505;
$$
covering polynomials (zeta-derived values, FT.68(7)): $\mathcal Z_{\mathrm{byp}}(y)=1+24y+60y^2$, $\mathcal Z_{\mathrm{lock}}(y)=12y^2+4y^3$ — the locked sector includes the four fully bidirectional $K_{1,3}$ stars (locked $(3,3)$ hub threaded by three centers, $4^3=64$ each). **Effective mass** $m_{\mathrm{eff}}=\langle K\rangle\ln2/\mathfrak h$ (dark read: $E_{\mathrm{tot}}=K$ directed real edges [FT.17 dark pattern; Def-H.9(2)]), in three readings: (i) uniform over bypass configurations $\langle K\rangle=\tfrac{852}{205}$; (ii) amplitude-weighted $\bigl(\sum K|A_C|^2/\sum|A_C|^2\bigr)=\tfrac{62208}{15745}$; (iii) Cal-F equilibrium at $r{=}1$: equals (i). **Fractional contributions**: the equilibrium measure of a pattern with $K$ real edges is $p^K(1-p)^{12-K}$, $p=r/(1+r)$ — the per-$K$ coefficients above are the exact fractional-contribution table. Aspect-activation frequency over bypass configs by $\max_vk_v$: $(1,24,245,960)$ for $\max k=(0,1,2,3)$. Bound-content census (configurations containing $\ge1$): digons $501$, directed $3$-cycles $252$, directed $4$-cycles $90$ — with $\Theta\in\{2,3,4\}$ at (S1): digons and $4$-cycles are on-shell materializable candidates [$\Theta\in2\mathbb Z$: FT.22; $4$-cycles: $k=2$, $j=1$ under Def-H.38; digons: the $\Sigma_{\min}$ card, $j=\tfrac12$], $3$-cycles off-shell arena content [$\Theta=3$ odd; Def-H.18] — and **the bound cells themselves all cancel in amplitude** [FT.67(3a)]: standalone bound content is configuration-present, $Z$-absent. **(correction [FT.69(4)]: the census configurations are not all $Z$-absent — $48$ of the $501$ digon-containing bypass configurations are covers: dissolved digons inside thread networks [witness in FT.69(4)]; the $3$-cycle and $4$-cycle rows cancel completely — odd cycles never enter covers, and no tetrahedron cover contains a $4$-cycle [FT.69(3)].)** The fully crystallized floor cancels [machine].
$(2)$ **Polygon ladder $P_n$ (potential $n(v)=4$; transfer matrix).** Bypass $\iff$ every vertex drops $\ge1$ of its $4$ directed edges. With channel states $s_i=(f_i,r_i)\in\{0,1\}^2$ and the vertex constraint $\operatorname{pop}(s_i)+\operatorname{pop}(s_{i+1})\le3$:
$$
B_{P_n}(t)=\operatorname{tr}\bigl(T(t)^n\bigr),\qquad T(t)[s][s']=t^{|s'|}\,[\,|s|+|s'|\le3\,]\qquad[\text{math: transfer matrix}],
$$
counts $n=3..10$: $(54,207,783,2970,11259,42687,161838,613575)$; fractions $(\tfrac{27}{32},\tfrac{207}{256},\tfrac{783}{1024},\tfrac{1485}{2048},\dots)$ decaying; the polynomials $B_{P_n}(t)$ are tabulated by the machine [zeta-derived values]. **Dynamical zeta**: $\operatorname{charpoly}T(1)=x^4-3x^3-3x^2$, $\det(I-zT(1))=1-3z-3z^2$ — the bypass counts satisfy the exact recursion $\operatorname{tr}_n=3\operatorname{tr}_{n-1}+3\operatorname{tr}_{n-2}$ [machine: $n=3..12$], growth rate $\lambda_{\max}=\tfrac{3+\sqrt{21}}2<4$: **the bypass fraction decays exponentially in $n$** — bypass is a finite-cell phenomenon in the thermodynamic limit (the amplitude sector itself keeps growing, at the covering growth rate). Sign-summed amplitudes (bypass, locked): $P_3$: $(25,48)$; $P_4$: $(353,64)$; $P_5$: $(1161,80)$; $P_6$: $(3121,1632)$; $P_7$: $(11929,10864)$; $P_8$: $(53825,43136)$; $P_9$: $(229417,159888)$; $P_{10}$: $(844881,775840)$ — the locked sector is nonzero for every $n\ge3$ (single-hub coverings exist on every polygon).
$(3)$ **Cube (orbit-reduced; Directive bound respected).** Potential $n(v)=6$, $24$ directed edges, $\operatorname{Aut}$ of order $48$. Bypass configurations: $1\,580\,092$, by $K$: $(1,24,276,2024,10506,40296,115796,247704,383913,408464,270096,91392,9600)$ for $K=0..12$ (cap-admissible DP; $K\le12$ forced). **Orbit structure** (cap-aware Burnside DP over conjugacy classes): by $K$: $(1,1,11,49,250,863,2509,5211,8163,8571,5768,1922,245)$, total $33\,564>10^4$ — per the bounded-enumeration rule, orbits are reported by $K$ only, with individual weights computed for coverings alone. Covering polynomials: $\mathcal Z_{\mathrm{byp}}(y)=1+48y+648y^2+2672y^3+3624y^4$ ($6993$ configs), $\mathcal Z_{\mathrm{lock}}(y)=24y^2+728y^3+3192y^4+264y^5+4y^6$ ($4212$ configs); amplitudes $Z^{\pm}_{\mathrm{byp}}=1\,109\,313$, $Z^{\pm}_{\mathrm{lock}}=1\,150\,848$, $Z^{\pm}_{\mathrm{all}}=2\,260\,161$; the fully crystallized cube cancels. The exact-cover theorem is exhaustively verified for all bypass configs with $K\le4$ and stride-sampled beyond. Dodecahedron/icosahedron: **not run wholesale**; their covering enumeration (sparse by FT.67(3d)) is the natural next cell, deferred and recorded.
$(4)$ **Layer dichotomy (the flicker hypothesis, resolved).** (a) *Bypass is real*: $Z^{\pm}_{\mathrm{byp}}>0$ on every computed skeleton — single vertex $1+n_{\mathrm{in}}n_{\mathrm{out}}\cdot4$, tetrahedron $1057$, polygons growing, cube $1\,109\,313$: the admissible sector of an $n\ge4$ skeleton has strictly positive amplitude at the A8 configuration-sum layer. (b) *What it produces*: the survivors are exactly open V-thread networks — $1$-dimensional transit-type content [D1.5: open propagating $=$ bosonic]; the effective dimensionality of the path-integrated bypass configuration is **thread-like: neither polygon-like $2$D (faces cancel) nor solid-like $3$D (solids cancel)**; its ledger reads are $m_{\mathrm{eff}}$ of (1), aspect activation concentrated at $\max k_v\in\{2,3\}$ ($\mathcal A\supseteq\{\mathrm{EM}\}$-capable and strong-*activated* patterns [CT0.13], with observable strong still requiring $\Sigma$-level sealing [FT.27, FT.20]). (c) *What it does not produce*: bound floors — $\Sigma_{\min}$, $\Sigma_L$, $\Sigma_{P_n}$, $\Sigma_S$ — cancel exactly at this layer [(FT.67(3a))]; they live at the spectral layer [Def-H.16 poles; M1/M2 declarations], where CT2.8's norms $\sum|w|^2$ are strictly positive and no cancellation occurs. (d) **Verdict on "the path integral fuzzes the flickering 2D shape into a higher-tier solid"**: flickering thread gas — *yes*, exact and strictly positive; fuzzing into solids — *no* at the amplitude layer **[scope: a literal-domain (S2) verdict — in the chain-local domains every computed Platonic floor and every even polygon floor carries strictly positive amplitude (tetra $2^{17}$, cube $2304\cdot2^{24}$, octa $72384\cdot2^{24}$; $4\cdot2^{2L}$ for even $L$, $0$ for odd), so the verdict is domain-relative [FT.75(2)]; the thread-gas clause and the norm-layer clause (c) are domain-invariant [FT.75(6)]]**; the solid floors enter through the spectral layer, and the bridge between the two layers is precisely the open residue of item 13 [FT.66(3)–(5): structural coupling absent; exit (b) not constructed]. No identification between layers is made or forced.
$(5)$ **Flicker rate (Cal-F, declared).** The corpus supplies no $J^\pm$ rates — D1.2 is transition vocabulary, A5's draws are unrecorded, and no rate tag exists [inventory]. Declare $r:=\Gamma_{J^+}/\Gamma_{J^-}$ a free internal dynamics datum (P4-class, $\neg$constant of the theory) with per-edge independent detailed-balance equilibrium $p=r/(1+r)$ [Cal-F]. Then the vertex-admissibility fractions are the exact polynomials
$$
f_{\mathrm{adm}}(n,p)=\sum_{k\le3}\binom nk p^k(1-p)^{n-k}:\quad1-p^4\ (n{=}4),\quad1-5p^4+4p^5\ (n{=}5),\quad1-15p^4+24p^5-10p^6\ (n{=}6),
$$
with samples $f_{\mathrm{adm}}(6;r{=}1)=\tfrac{21}{32}$, $f_{\mathrm{adm}}(6;r{=}3)=\tfrac{347}{2048}$ [machine]; skeleton bypass probabilities are $B_\Gamma(p)=\sum_Kc_K\,p^K(1-p)^{|E_{\mathrm{dir}}|-K}$ with $c_K$ the by-$K$ counts of (1)–(3) — the exact fractional-contribution tables. Time-fraction reading: at equilibrium each vertex spends the fraction $f_{\mathrm{adm}}(n(v),p)$ of time channel-admissible; the fully crystallized Def-H.20 floor occupies measure $p^{2E}\to$ small as $p<1$ — the static floor is a measure-zero-corner of its own skeleton's flicker ensemble, while its spectral status is $p$-independent (declared, M1/M2).
$(6)$ **Bott connection.** Amplitude survivors contain no closed chains [FT.67(3a)] $\Rightarrow$ no closed stationary channels at the amplitude layer $\Rightarrow$ Def-H.24's Bott data is *undefined on survivors* (no loops to index); the thread networks are transit-side objects, where fixed-endpoint index-0 minimizers exist [FT.48(3)] — the amplitude layer's survivor class and the variational layer's stable class are both transit-side, a derived consistency with FT.66(4b) ("stability is transit-side vocabulary"). Bound content inside bypass configurations (the census of (1)) carries its Bott datum at the spectral layer, where FT.66(4) applies unchanged: on Synge-class slices every closed geodesic has $\operatorname{ind}_B\ge1$ — **the bypass does not evade the selection dilemma; it relocates the surviving content to the one sector where index-0 stability exists**.
$(7)$ **Convergence and zeta ledger.** Every $Z$ above is a finite exact integer (finite skeletons): the path integral converges trivially and has well-defined values — no regularization was needed and none is claimed. Derived zeta-type values recorded: polygon dynamical zeta $\det(I-zT(1))=1-3z-3z^2$ with recursion $\operatorname{tr}_n=3\operatorname{tr}_{n-1}+3\operatorname{tr}_{n-2}$ and $\lambda_{\max}=\tfrac{3+\sqrt{21}}2$; the covering polynomials $\mathcal Z_\Gamma(y)$ (tetrahedron/cube, per sector); the bypass polynomials $B_{P_n}(t)$, $n\le10$ — all exact integer data, machine-verified.

### Def-H.26 — Flicker-ensemble phase reads

**Def.** For a skeleton $\Gamma$ [Def-H.25] with $2E$ directed edges and equilibrium parameter $p\in[0,1]$ [$p=x_+/(x_++x_-)$: the unique stationary measure of the per-pair Janus generator — FT.108(4), forward pointer Tier F.36; $r:=x_+/x_-$ a P4-class rate datum (Cal-F); the per-edge independent Bernoulli scope is constitutive of the ensemble (CT4.5a-species ensemble scope)], the **flicker ensemble** is the Bernoulli product measure $\mu_p$ on crystallization patterns $R\subseteq E_{\mathrm{dir}}(\Gamma)$ (each directed edge real independently with probability $p$). Pattern-layer reads (all exact polynomials/rationals in $p$; $\neg$spectral reads):
$$
B_\Gamma(p):=\mu_p(\text{bypass})=\sum_K c_K\,p^K(1-p)^{2E-K}\quad[c_K:\ \text{cap census, CT0.11}];\qquad F_\Gamma(p):=p^{2E}\quad[\text{floor measure}];
$$
$$
L_\Gamma(p):=1-B_\Gamma(p)\quad[\text{lock fraction}];\qquad \langle K\rangle_{\mathrm{byp}}(p):=\frac{\sum_K K\,c_K\,p^K(1-p)^{2E-K}}{B_\Gamma(p)};
$$
$$
p^*_\Gamma:=\text{the unique root of }B_\Gamma(p)=F_\Gamma(p)\text{ in }(0,1)\ \ [\text{lockable }\Gamma;\ \text{FT.70(1)}];\qquad \langle\rho_{D^-}\rangle_\Gamma(p):=\sum_v O(n_v)\,\mu_p(k_v\ge4)\ \ [\mathrm{CT4.1},\mathrm{CT4.5}].
$$

### FT.70 — The flicker phase diagram: unique crossover, computed boundaries, the polygon limit

**Thm.** Under Def-H.26 (equilibrium readings under the Cal-F rate datum; the polynomial data declaration-free):
$(1)$ **Existence and uniqueness of the phase boundary.** The admissible family is downward-closed (subsets of admissible patterns are admissible: $k_v$ decreases), nonempty ($\varnothing$), and proper (the floor is locked iff $\Gamma$ is lockable, i.e. $\max_v n(v)\ge4$). Hence $B_\Gamma$ is strictly decreasing on $(0,1)$ [math: monotone coupling; strictness witness: any $3$ edges at a vertex of $n(v)\ge4$ give an admissible $R$ with $R\cup\{e\}$ locked], while $F_\Gamma(p)=p^{2E}$ is strictly increasing; $B(0)-F(0)=1>0$, $B(1)-F(1)=c_{2E}-1=-1<0$. **Every lockable skeleton has a unique crossover $p^*_\Gamma\in(0,1)$**; non-lockable skeletons (all $n(v)\le3$: the digon, unidirectional cells) have $B\equiv1$: no interior boundary, thread gas at every $p<1$.
$(2)$ **Computed boundaries** (exact dyadic isolating intervals of width $2^{-40}$; machine; decimal display $\approx$):
$$
p^*:\quad\text{icosa}\ 0.652034\ <\ \text{octa}\ 0.679217\ <\ \text{tetra}\ 0.723525\ <\ \text{dodeca}\ 0.724519\ <\ \text{cube}\ 0.725372\ <\ P_3\ 0.807901\ <\ P_5\ <\ P_7\ <\ P_9\ <\ \sqrt{\tfrac23}\ <\ P_{10}\ <\ P_8\ <\ P_6\ <\ P_4\ 0.819671 .
$$
Regions: $p<p^*_\Gamma$ thread-gas-dominant ($B>F$), $p>p^*_\Gamma$ floor-dominant ($F>B$); the locked fraction $L_\Gamma(p)=1-B_\Gamma(p)$ rises $0\to1$ across the diagram. The two degree-$\ge4$ solids cross earliest — the crossover order reproduces the lock-proneness order of clause (4).
$(3)$ **Polygon limit, closed form.** $\operatorname{charpoly}T(t)=x^2\bigl(x^2-(1+2t)x-t^2(1+2t)\bigr)$ [machine: exact at $t\in\{1,2,\tfrac13,\tfrac52\}$; generalizes FT.68(2)'s $t{=}1$ value]. Asymptotically $B_{P_n}(p)\sim(1-p)^{2n}\lambda_{\max}(t)^n$, $t=p/(1-p)$: the crossing equation tends to $\lambda_{\max}(s)=s^2$, i.e. $s^4=2s^2(1+2s)$, i.e. $s^2-4s-2=0$ with $s=p/(1-p)$: $s=2+\sqrt6$ and
$$
p^*_\infty=\frac{s}{1+s}=\frac{2+\sqrt6}{3+\sqrt6}=\frac{\sqrt6}{3}=\sqrt{\tfrac23}\qquad\Bigl[\ \bigl(\sqrt\tfrac23\bigr)^2=\tfrac23;\ (2{+}\sqrt6)^2=10{+}4\sqrt6=4(2{+}\sqrt6){+}2\ \checkmark\ \text{in}\ \mathbb Z[\sqrt6]\Bigr],
$$
approached from below by odd $n$ and from above by even $n$ (interlaced; machine through $n=10$).
$(4)$ **Lock-proneness order (the corrected "forbidden zone").** Exact identity [machine, symbolic $n=3..10$]:
$$
f_{\mathrm{adm}}(n{+}1,p)=f_{\mathrm{adm}}(n,p)-\binom{n}{3}p^4(1-p)^{n-3}\ <\ f_{\mathrm{adm}}(n,p)\qquad\forall p\in(0,1),
$$
so admissibility is strictly decreasing in potential degree: $f_{\mathrm{adm}}(2d,\tfrac12)=(1,\tfrac{15}{16},\tfrac{21}{32},\tfrac{93}{256},\tfrac{11}{64})$ for $2d=(2,4,6,8,10)$: digon $>$ polygons $>$ \{tetra, cube, dodeca\} $>$ octa $>$ icosa. **The proposed octahedron "forbidden zone" is refuted**: $f_{\mathrm{adm}}(8,p)\ge(1-p)^8>0$ for every $p<1$ and $318\,523$ admissible configurations exist at the cap level [(1)]. What is true: at fixed $p<1$ the octahedron/icosahedron are the most lock-prone Platonic skeletons, and $p=1$ locks *every* skeleton — the static floor is the $p\to1$ limit of its own ensemble [FT.68(5)], with amplitude zero there [FT.67(3a)].
$(5)$ **Effective edge content.** $\langle K\rangle_{\mathrm{byp}}(p)$ is strictly increasing on the exact grid $p\in\{\tfrac1{20},\dots,\tfrac{19}{20}\}$ (machine: tetra, cube, icosa, $P_5$), with limits $0$ (vacuum-dominated, $p\to0$) and $K_{\max}=\lfloor3V/2\rfloor$ (top bypass row, $p\to1$); at $p=\tfrac12$: $\bigl(1,\tfrac{852}{205},\tfrac{3311952}{395023},\tfrac{2124600}{318523},\tfrac{4007491093935690}{191727103387307},\tfrac{215801166207}{15519497071}\bigr)$ for digon/tetra/cube/octa/dodeca/icosa (the tetra entry is FT.68(1)'s $m_{\mathrm{eff}}$ reading (i) verbatim — $p{=}\tfrac12$ is the uniform measure) and $\bigl(\tfrac83,\tfrac{248}{69},\tfrac{130}{29},\tfrac{296}{55},\tfrac{2618}{417},\tfrac{11344}{1581},\tfrac{896}{111},\tfrac{13588}{1515}\bigr)$ for $P_3..P_{10}$. The dark mass read is $m_{\mathrm{eff}}(p)=\langle K\rangle_{\mathrm{byp}}(p)\ln2/\mathfrak h$ [FT.68(1) pattern]: light at high flicker, heavy toward the static limit, exact at every $p$.

### FT.71 — The flicker-dust equation of state

**Thm.** Under Def-H.26 (equilibrium readings under the Cal-F rate datum), for every skeleton $\Gamma$:
$(1)$ **Exact dust density.** Per-edge independence gives $k_v\sim\mathrm{Bin}(n(v),p)$, hence
$$
\langle\rho_{D^-}\rangle_\Gamma(p)=\sum_v O(n_v)\,\bigl(1-f_{\mathrm{adm}}(n_v,p)\bigr),\qquad O(n)=2^{n+1}-16\ \ [\mathrm{CT4.1};\ \mathrm{FT.62}(2)],
$$
an exact polynomial in $p$ with integer coefficients: Platonic values at $p=\tfrac12$: $\bigl(154,\ 308,\ \tfrac{15159}{8},\ 770,\ 20193\bigr)$ for (tetra, cube, octa, dodeca, icosa); polygon family the exact monomial $\langle\rho_{D^-}\rangle_{P_n}(p)=16\,n\,p^4$ (at $p{=}\tfrac12$: $n$); digon identically $0$ (never locks).
$(2)$ **Anchors.** $\langle\rho_{D^-}\rangle_\Gamma(1)=\sum_vO(n_v)=$ FT.63(5)'s dark sums $(448, 896, 2976, 2240, 24384)$ exactly [machine]; $\langle\rho_{D^-}\rangle_\Gamma(0)=0$; strict increase on $(0,1)$ for lockable $\Gamma$ [clause (4)'s $f_{\mathrm{adm}}$ strict decrease, FT.70(4)].
$(3)$ **The flicker modulates $\rho$, never $w$.** CT4.5 applies per configuration: every locked vertex contributes pressureless dust ($w=0$, source side, coupled to geometry through CT1.23 and nothing else). The ensemble's locked content is therefore dust at every $p$; the flicker parameter moves only the *density* — along the exact polynomial of (1). $D^+$'s $w=-1$ [CT1.25, D4.3] is configuration-independent and untouched: the CT4.6 contrast table holds ensemble-wise term by term.
$(4)$ **No fluid.** The locked sector supports no further equation-of-state data: it is a structureless absorbing sink — one possibility space [D4.1], no gauge content [CT4.4], absorption one-way [CT4.2], content inaccessible [D1.11] and unresolvable [FT.3]. Statements assigning $D^-$ a pressure response, polarization, or re-emission have no defined ledger referent (the referent would contradict CT4.2/D1.11); "the vacuum is a $D^-$ fluid" is inadmissible as stated — what the corpus derives is: locked content gravitates as dust with the density computed here.

### FT.64 — The filter chain and the per-solid loop lattices

**Thm.** $(1)$ **Filter chain (definition of ledger-admissible).** A loop datum on a floor $\Sigma$ is **ledger-admissible** iff it passes, in order: **(F0)** configuration validity — closed real-edge content, Janus balance, mask image, no dangling ledger boundary [D2.11, D1.3, D0.10]; **(F1)** registration — $\sigma_e\in\{\pm1\}$ per directed real edge, independent of $\kappa$ [CT0.9, CT0.10]; **(F2)** integrality — $\kappa_e\in\mathbb Z$ on edges of materialized digons and round-trip-closed channels (classes (i)/(ii) [Open Gaps 13; FT.24, FT.34(4)]; Platonic/polygon floors: under declared M2 [Def-H.20]); **(F3)** loop quantization — $\Theta(c)\in2\mathbb Z$ per materialized closed chain [FT.22; M1 on faces]: for the Platonic floors exactly $\kappa\in\ker\varphi_S$, $\varphi_S=\,$face-incidence mod $2$ [FT.43(3)]; **(F4)** stationarity (semiclassical survivors) — $\kappa\equiv\kappa_0$ constant along each connected materialized chain, geodesic support [FT.53(1)–(2), FT.48(1)]; **(F5)** regime — null-permitting ($\kappa\ge0$), strictly-spacelike ($\kappa\ge1$), uniform, or signature-mixed ($\kappa\in\mathbb Z$; fibers infinite at fixed $K$ — witness $(K{+}n,-n)$ — so enumeration is scoped to $\kappa\ge0$ [FT.45(4) pattern]); **(F6)** relabeling quotient — identification under mask-preserving relabeling [CT2.6's $\sim$, CT2.7; FT.51(3)]: $\operatorname{Aut}(\Gamma_S)$-orbits (FT.65); **(F7)** register product — signs $\times$ $\kappa$-orbits $\times$ sealing groupings, independent registers [FT.51(5), FT.65(2)]; **(F8)** spectral filter — materialization (M1/M2 declared; which admissible loops are on-spectrum is the corpus's [D2.4, CT2.5, Def-H.16]); no ledger-side criterion can further select by stability index [FT.61(4)]: **(F8) is the honest boundary of this list**.
$(2)$ **Per-solid lattice, all five by machine.** $\ker\varphi_S\subseteq\mathbb Z^E$ has index $2^{F-1}$ — GF(2) rank $F-1$ verified by explicit elimination for **all five** solids (the earlier tetra/cube checks extended): $(8,32,128,2048,2^{19})$. Equivalent formulation: $\kappa\bmod2$ lies in the **cut space** of $\Gamma_S$ — $\dim_{\mathbb Z_2}\ker\varphi_S=E-(F-1)=V-1=\dim\operatorname{Cut}(\Gamma_S)$ [Euler; math: planar duality; machine: dimensions + vertex-star cut witnesses].
$(3)$ **Face-read realizability (SNF).** For the face-read map $B:\mathbb Z^E\to\mathbb Z^F$, $\kappa\mapsto(\Theta_f)_f$: Smith invariant factors are $(1,1,1,2)$ tetrahedron, $(1^5,2)$ cube, $(1^7)$ octahedron (rank $7=F{-}1$), $(1^{11},2)$ dodecahedron, $(1^{19},2)$ icosahedron [machine]. Consequences: **(a)** tetrahedron/cube/dodecahedron/icosahedron: $(2\mathbb Z)^F\subseteq\operatorname{im}B$ — *every* integer face-winding vector $k=(k_f)\in\mathbb Z^F$ is realized by some signed $\kappa$ [machine witness: all four unit vectors $k=e_f$ realized on the tetrahedron with $\kappa\in[-2,2]^6$]; **(b)** octahedron: $\operatorname{im}B=\ker\psi$, $\psi=$ black$-$white face-sum (dual bipartite, $d$ even — the unique such Platonic): $k$ realizable $\iff\sum_{\mathrm{bl}}k_f=\sum_{\mathrm{wh}}k_f\iff K_S\in2\mathbb Z$ [machine: $\psi(\operatorname{im}B)=0$ on samples; $\psi(2e_f)=\pm2\ne0$: $k=e_f$ unrealizable]; each channel lies in exactly one black and one white face [machine].
$(4)$ **Level-set counts.** $A_S(K):=\#\{\kappa\in\mathbb Z_{\ge0}^E:\ \sum_e\kappa_e=K,\ \varphi_S(\kappa)=0\}$ (level $K=K_S=\Theta_{\mathrm{int}}/2$) [machine, DFS with face-parity pruning; cross-checked against orbit enumeration and the Burnside identity element]:
$$
\begin{array}{c|ccccccccc}
S & K{=}0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\ \hline
\text{tetrahedron} & 1 & 0 & 6 & 4 & 24 & 24 & 74 & 84 & 189\\
\text{cube} & 1 & 0 & 12 & 8 & 93 & 120 & 576 & — & —\\
\text{octahedron} & 1 & 0 & 12 & 0 & 84 & 0 & 452 & — & —\\
\text{dodecahedron} & 1 & 0 & 30 & 20 & 495 & 672 & — & — & —\\
\text{icosahedron} & 1 & 0 & 30 & 0 & 465 & 12 & — & — & —
\end{array}
$$
with the exact character-sum closed form [math: GF(2) orthogonality; machine-verified against the DFS for tetrahedron/cube/octahedron, $K\le6$]:
$$
A_S(K)=\frac{1}{2^{F-1}}\sum_{s\in\mathbb Z_2^F/\langle\mathbf1\rangle}[z^K]\prod_{e\in E}\frac{1}{1-(-1)^{s\cdot b_e}\,z}\qquad(b_e=\text{face-incidence column of}\ e),
$$
and asymptotics $A_S(K)\sim\binom{K+E-1}{E-1}/2^{F-1}\sim K^{E-1}/((E-1)!\,2^{F-1})$ [equidistribution of the $F-1$ parity conditions; machine trend: tetrahedron $A(16)=2673$ vs $20349/8$]. Structural reads [machine]: $A_S(1)=0$ for every solid (no bridges — a lone $\kappa{=}1$ channel leaves its two faces odd); $A_S(3)=V$ for the $d{=}3$ solids (the vertex stars), $0$ for the $d\ge4$ solids (octahedron: even-$d$ parity; icosahedron: its stars carry $K{=}5$); the octahedron has $A(\text{odd}\,K)=0$ [(3)(b)]; the icosahedron's $A(5)=12$ is exactly its star family — the index-$2^{19}$ lattice is sparse enough that at low levels only the symmetric families survive. The $K{=}0$ entry is the all-null bound configuration (trivial-chain content [D1.7, D3.7]; $W$-row silent [FT.42(3)]).
$(5)$ **Minimality regimes, all five** [FT.45(4)/FT.32(6) pattern; machine]:
$$
\begin{array}{c|c|c|c|c}
S & \text{R0 null-perm.}: (K_{\min},\Theta_{\mathrm{int}},\text{orbits}) & \text{R1 strict}: (\varepsilon_{\min},K_{\min},\Theta_{\mathrm{int}},\text{orbits}) & \text{R2 uniform}: \kappa_0\ \text{ladder} & \text{R1 witness type}\\ \hline
\text{tetrahedron} & (2,4,1) & (2,8,16,1) & 2,4,6,\dots & \text{opposite-edge pair at}\ 2\\
\text{cube} & (2,4,1) & (0,12,24,1) & 1,2,3,\dots & \text{all-1 profile (unique)}\\
\text{octahedron} & (2,4,1) & (4,16,32,3) & 2,4,6,\dots & \text{coset leaders, 3 orbits}\\
\text{dodecahedron} & (2,4,1) & (6,36,72,25) & 2,4,6,\dots & \text{coset leaders, 25 orbits}\\
\text{icosahedron} & (2,4,1) & (10,40,80,14) & 2,4,6,\dots & \text{coset leaders, 14 orbits}
\end{array}
$$
R0: single channel at $\kappa{=}2$ (one orbit — $\operatorname{Aut}$ edge-transitive [machine]). R1: $\kappa=1+x$, $x\ge0$: parity demands $Bx\equiv(L\bmod2)\cdot\mathbf1$; $\varepsilon_{\min}=$ minimum weight in the GF(2) coset [machine: coset enumeration, $\le2^{19}$ for the dodecahedron]. **Derived laws**: (a) $\Theta_{\mathrm{int},\min}^{\mathrm{R0}}=4$ for every solid vs $2$ for $\Sigma_{\min}$ and $2$ (face-winding) for polygons — a solid's faces are too many to be fooled by one channel [$F\ge4$ separated faces; FT.45(5)'s digon distinction extended]; (b) the **cube is the unique Platonic whose uniform-minimal profile is also its strictly-spacelike minimum** ($\varepsilon_{\min}=0$; all-1, unique up to symmetry) — for the four odd-$L$ solids R1 beats R2 strictly ($16{<}24$, $32{<}48$, $72{<}120$, $80{<}120$): their uniform minima are *not* their cheapest spacelike configurations, and the minimizers form nontrivial orbit families (up to $25$); (c) R2's stationary ladder is the semiclassical survivor list [FT.53]: one orbit per rung $\kappa_0$, $K=E\kappa_0$.
$(6)$ **Completeness, ledger side.** (F0)–(F7) are decidable and decided above (or cited closed-form: polygons [FT.51], cycles [FT.32(6)]); (F8) is declared. The list is complete as a ledger enumeration: every admissible loop datum on every computed floor is an element of $\ker\varphi$ (lattice) $\times$ sign registers $\times$ sealing groupings, modulo $\operatorname{Aut}$, within one of the four regimes, surviving semiclassically exactly on the R2 ladder.

### FT.72 — Two-fold face decomposition; the Bernoulli marginals ("coarse-grained fuzz as data")

**Thm.** Let $\Sigma_S$ be a Platonic skeleton (sphere), $E,F$ its undirected edge/face counts, all arithmetic over $\mathrm{GF}(2)$.
$(1)$ **Two-fold face-decomposition theorem.** The face-boundary map $\partial_2:\mathrm{GF}(2)^F\to\mathrm{GF}(2)^E$ has image exactly the cycle space $Z_1=\ker\partial_1$ (rank $\beta_1=F-1$ [FT.43(5), FT.64; machine: all five]) and kernel $\{0,\sum_f f\}$ (every edge lies in exactly two faces). Hence **every cycle $z\in Z_1$ has exactly two face-decompositions, $z=\partial_2 S=\partial_2(F\setminus S)$** — a set of faces and its complement. "Every subnetwork is a composition of triangles" holds exactly for the triangulated skeletons (tetrahedron $4$, octahedron $8$, icosahedron $20$ triangles [machine census]); the cube's faces are squares, and **the dodecahedron — girth $5$: zero triangles and zero $4$-cycles [machine] — admits no triangle decomposition within its skeleton at all**: its face grammar is pentagonal, and triangle compositions would require diagonals outside $\mathcal R$.
$(2)$ **Hodge-type split (corrected form).** $Z_1=\mathrm{Cut}^\perp$ under the standard pairing; $\dim Z_1+\dim\mathrm{Cut}=\beta_1+(V{-}1)=E$ [Euler], but the sum is **not** direct in general: $j:=\dim(Z_1\cap\mathrm{Cut})=(2,3,3,5,5)$ for (tetra, cube, octa, dodeca, icosa) [machine]. A pattern $R$ is decomposable ($R\in Z_1+\mathrm{Cut}$: cycle content $+$ boundary content) iff its syndrome is orthogonal to $Z_1\cap\mathrm{Cut}$; the decomposition is unique up to $2^j$ gauge choices.
$(3)$ **Exact Bernoulli marginals.** For $R\sim\mu_p$ [Def-H.26], with $q:=1-2p$:
$$
P_p(R\in Z_1)=\frac{1}{2^{V-1}}\sum_{c\in\mathrm{Cut}}q^{|c|},\qquad P_p(R\ \text{decomposable})=\frac{1}{2^{j}}\sum_{u\in Z_1\cap\mathrm{Cut}}q^{|u|},\qquad P_p(R\in\mathrm{Cut})=\frac{1}{2^{\beta_1}}\sum_{z\in Z_1}q^{|z|}
$$
[MacWilliams for $Z_1=\mathrm{Cut}^\perp$ and $(Z_1+\mathrm{Cut})^\perp=Z_1\cap\mathrm{Cut}$; machine: direct enumeration cross-check at $\beta_1\le5$]. At $p=\tfrac12$: $P(R\in Z_1)=2^{-(V-1)}=(\tfrac18,\tfrac1{128},\tfrac1{32},\tfrac1{524288},\tfrac1{2048})$ and $P(\text{decomposable})=2^{-j}=(\tfrac14,\tfrac18,\tfrac18,\tfrac1{32},\tfrac1{32})$; samples $p=\tfrac14$: $(\tfrac{27}{128},\tfrac{19}{64})$, $p=\tfrac34$: $(\tfrac{11}{128},\tfrac{19}{64})$ for the tetrahedron [machine table for all five].
$(4)$ **Dual signatures at the Hodge level.** The intersection weight-enumerators of dual pairs coincide exactly: cube $\equiv$ octahedron $\{0{:}1,6{:}4,8{:}3\}$, dodeca $\equiv$ icosa $\{0{:}1,10{:}6,16{:}15,18{:}10\}$ [machine] — a new degeneracy of the FT.44 species — while the cut enumerators split them: the octahedron's cut space is even-weight (all degrees $4$: every star even; the subgraph-level echo of FT.63(3)'s black–white parity law) while the cube's carries odd stars (weight $3$).
$(5)$ **"Fuzz as data", formalized.** The complete flicker datum of a skeleton is the measure $\mu_p$ on $\mathrm{GF}(2)^E$; every coarse-grained read computed in this document is a named marginal of it: $K\mapsto I_{\mathrm{hid}}$-type edge content [FT.68(1)], admissibility $\mapsto$ bypass/lock sectors [Def-H.25], cycle/cut class $\mapsto$ (3) above, cover support $\mapsto$ amplitude [FT.67(2)], winding lattices $\mapsto$ FT.64's index-$2^{F-1}$ sublattices (on-shell $\kappa$-side, not $\mu_p$-side — layer marked). No read is lost by coarse-graining that the measure retains; nothing in the measure is readable that the ledger's registers admit [C10 reality principle; FT.3 for locked content].

### FT.69 — Platonic amplitude census completed; the cycle-alternation lemma; one census correction

**Thm.** Under Def-H.25's scopes (S1)–(S4):
$(1)$ **Cap census, completed.** Bypass-configuration counts by $K$ (cap-DP, exact): octahedron $318\,523$ ($K\le9$; row $(1,24,276,2024,10206,35448,81344,110736,69504,8960)$; $K\le5$ exhaustively validated); dodecahedron $3\,067\,633\,654\,196\,912$ ($K\le30=3V/2$ forced); icosahedron $2\,483\,119\,531\,360$ ($K\le18=3V/2$ forced). Low-order universality: the rows of the two $60$-edge skeletons agree through $K=3$ ($(1,60,1770,34220)$: caps bind only from $K=4$: $487335$ vs $485115$, the difference $20\binom64$ vs $12\binom{10}4$ exactly the single-vertex lock counts) and diverge from $K=4$ on. Orbits: not attempted (bounded rule: cube's $33\,564$ already exceeded $10^4$ [FT.68(3)]).
$(2)$ **Coverings.** Octahedron complete (two independent enumerators agree): $\mathcal Z_{\mathrm{byp}}(y)=1+72y+852y^2+1152y^3$, $\mathcal Z_{\mathrm{lock}}(y)=36y^2+1008y^3+840y^4$; $Z^{\pm}_{\mathrm{byp}}=87\,649$, $Z^{\pm}_{\mathrm{lock}}=280\,128$, $Z^{\pm}_{\mathrm{all}}=367\,777$. Dodecahedron/icosahedron exact to $|\mathcal C|\le3$: dodecahedron $\{0{:}1,\,1{:}120,\,2{:}5880{+}60_{\mathrm{lock}},\,3{:}153\,960{+}6140_{\mathrm{lock}}\}$ ($166\,161$ covers, $Z^{\pm}\ge9\,948\,001$ byp / $393\,920$ lock from the counted range); icosahedron $\{0{:}1,\,1{:}240,\,2{:}17\,520{+}120_{\mathrm{lock}},\,3{:}478\,360{+}27\,600_{\mathrm{lock}}\}$ ($523\,841$ covers, $Z^{\pm}\ge30\,896\,321/1\,768\,320$ counted). Single-centre closed form on every skeleton: $\#\{|\mathcal C|=1\}=V\,d_{\mathrm{in}}d_{\mathrm{out}}$ minus closed-thread exclusions $=V\,d(d{-}1)$ bidirectional $=(24,48,72,120,240)$ for the five solids [machine]. Full dodeca/icosa counts deferred: the vertex-DP state width (cut-arcs $\le11$ at degree $5$; memo exhaustion) and the branch enumerator ($\sim(1+d^2)^V$ raw) both exceed the bounded rule — recorded, not guessed. Fully crystallized floors cancel: types $(3,3)^{20}$, $(5,5)^{12}$, no centres, value $0$ [FT.67(3a)].
$(3)$ **Cycle-alternation lemma.** Let $R$ be a literal-domain cover and $\gamma\subseteq R$ a directed cycle. Then along $\gamma$ the vertices **strictly alternate centre / non-centre**; consequently: (i) $|\gamma|$ is even; (ii) every non-centre vertex of $\gamma$ carries at least one further real edge outside $\gamma$ (else its type on $\gamma$ alone is $(1,1)$, forcing a centre — contradiction); (iii) a pure directed cycle is never a cover [FT.67(3a), now with its structural reason]; (iv) **no odd directed cycle — in particular no triangle — lies inside any cover**: the amplitude layer's bound content is exactly even-cycle content, dissolved into threading **[scope: clauses (i)–(v) are literal-domain theorems. Both chain-local extensions dissolve odd cycles into open threads — on the tetrahedron, of $2397$ patterns containing a directed $3$-cycle, $833$ (E2) and $1025$ (E1) have nonzero amplitude against $0$ literal [FT.75(4)]]**; (v) census (distinct cycles, canonicalized; machine): covers containing directed cycles — tetrahedron $64/101$ ($84$ digon instances; $48$ bypass $+16$ locked), cube $9060/11205$ ($14\,328$ digons, $504$ four-cycles), octahedron $3054/3961$ ($4704$ digons, $672$ four-cycles), $P_3$–$P_7$ digons only; the $P_4$ face $4$-cycle lies in *none* of its $33$ covers (clause (ii): its non-centre cycle vertices have no extra edges to carry); zero odd cycles in any enumerated cover.
$(4)$ **FT.68(1) census correction (self-audit).** The tetrahedron census numbers stand ($501/252/90$ bypass configurations containing digons/$3$-cycles/$4$-cycles, re-derived). The clause "all of it cancels in amplitude" is **false for the digon row**: $48$ of the $501$ are covers. Witness (machine, brute-force sign sum $=$ cover value $=16$): $R=\{(0{\to}1),(1{\to}0),(2{\to}1),(3{\to}2)\}$, types $\bigl((1,1),(2,1),(1,1),(0,1)\bigr)$ — the digon $\{0,1\}$ dissolved: centre $0$ reads both digon edges, vertex $1$ is a $(2,1)$ non-centre supported by centre $2$'s thread. The $3$-cycle and $4$-cycle rows cancel completely [(iii)+(i) of clause (3); machine: $0$ nonzero of $252/90$]. **[addition: these $48$ survivors are killed by *both* chain-local extensions ($N_{E2}=N_{E1}=0$ on all $48$, exhaustive), while the $16$ *locked* digon-covers of clause (5) are killed by E2 and kept by E1 at the derangement values $(!a)4^a$ [FT.75(1),(4)]. The triangle rows revive in the extensions: $833$ (E2) / $1025$ (E1) of the $2397$ tetrahedron patterns containing a directed $3$-cycle.]** Corrected statement: **bound cells cancel standalone; bound substructures survive inside covers only dissolved — even cycles threaded through supported non-centres.** FT.68(1) patched in place (marker).
$(5)$ **Minimal dissolution family.** The smallest dissolved-digon covers are double-digon hubs: two digons $\{h,c_1\},\{h,c_2\}$ sharing a locked $(2,2)$ hub $h$, centres $c_1,c_2$ ($|\mathcal C|=2$, $|R|=4$, value $16$): the tetrahedron's $12$ locked two-centre covers are exactly this family ($4$ hub choices $\times\binom32$); exhibited on cube and octahedron. The four $K_{1,3}$ stars [FT.68(1)] are the triple-digon hubs. Locked hubs are the only lock content visible in covers [FT.67 Rmk], and digons are the only bound cells they can host at $|\mathcal C|=2$.

### FT.73 — The bridge audit: dielectric non-existence, the field-degree no-go, and the surviving species

**Thm.** On the proposed bridge program (a $D^-$-medium/drag mechanism equating $m_{\mathrm{hid}}$ with $m_{\mathrm{pole}}$, with $\alpha$ emerging as a screening factor):
$(1)$ **Dielectric non-existence (inventory theorem).** A dielectric medium requires a polarization-response read (induced content vs applied read). The locked sector's complete inventory is: single possibility space [D4.1], absorption at rate $\propto O(n)$ [D4.2, CT4.1], one-way [CT4.2], retained and inaccessible [CT4.3, D1.11], no gauge structure [CT4.4], unresolvable [FT.3], never observable [FT.20], no slot realization at $n\ge4$ [FT.59]. **No response read exists**; $\varepsilon_{D^-}$ and "$D^-$ vacuum polarization" have no defined ledger referent, and any dynamics supplying one contradicts CT4.2/D1.11 — inadmissible from this part: no construction of Part 3 overturns a Parts 1–2 tag. The vacuum-side corpus data are instead: $\rho_\circ=\tfrac14 I$ [C11], $D^+=\Lambda\mathbb I$ with $w=-1$ [D4.3, CT1.25], $D^-$ dust with $w=0$ [CT4.5], and the entropy triangle's exhaustiveness [CT4.7, CT4.10] — the "equation of state of the vacuum" is computed, frozen, and two-sided.
$(2)$ **Field-degree no-go (drag refuted).** Under Def-H.37(2) the pole-side factors at the five floors are $\{2,\ 2-\sqrt2,\ 1,\ 2-2\cos\tfrac\pi{10},\ 2-\sqrt3\}$ [FT.54(4), FT.63(6)], with minimal polynomials: $2\cos\tfrac\pi{10}$: $y^4-5y^2+5$ (irreducible over $\mathbb Q$: no rational root, no $\mathbb Z$-quadratic factor [machine]); $2-2\cos\tfrac\pi{10}$: $x^4-8x^3+19x^2-12x+1$ (irreducible [machine; FT.63 anchor re-derived]). Hence the five factors generate $\mathbb Q(\sqrt2,\sqrt3,\cos\tfrac\pi{10})$, of degree $16$ over $\mathbb Q$: writing $y=2\cos\tfrac\pi{10}$, $\mathbb Q(y)/\mathbb Q$ is Galois of group $\mathbb Z_4$ (generator $y\mapsto\sqrt5/y$; machine: $y\cdot\tfrac{\sqrt5}y=\sqrt5=2y^2-5$, $(\tfrac{\sqrt5}y)^2=\tfrac{5-\sqrt5}2$), with unique quadratic subfield $\mathbb Q(\sqrt5)$; and $\sqrt5\notin\mathbb Q(\sqrt2,\sqrt3)$ [$\sigma_2/\sigma_3$-averaging forces $\sqrt5\in\mathbb Q$, machine] — so the two quartics intersect in $\mathbb Q$ and $[\mathbb Q(\sqrt2,\sqrt3,y):\mathbb Q]=4\cdot4=16$. Any bridge formula $m^2_{\mathrm{pole}}=F(n_1,\dots,n_m;c_1,\dots,c_k)$ with $F$ rational over its arguments, the $n_i$ **integer-valued combinatorial ledger reads** (including $\rho_{D^-}=\sum O(n)$, lock counts, covering counts, $Z^\pm$, $K$-reads, $m_{\mathrm{hid}}\mathfrak h/\ln2$, $g(V)$, $\beta_1$) and finitely many declared constants $c_j\in K$ places every pole value in $K$: covering the five computed floors forces $[K:\mathbb Q]\ge16$. The $\Theta_R$-read (Def-H.37(2)) attains all five factors with $K=\mathbb Q$: **curvature coupling is the unique surviving bridge species within the computed read classes** [consistent with the form-uniqueness sharpening of FT.54(1): state-independence forces $m^2_{\mathrm{pole}}=F(\Theta_R)$].
$(3)$ **Dual split and the exclusion of quadratic couplings.** The dual pairs share the informational mass — $m_{\mathrm{hid}}$: $24{=}24$ (cube/octa), $60{=}60$ (dodeca/icosa) [FT.44(2), FT.63(5)] — while the pole side splits both [FT.63(6)]: cube/octa by $(2-\sqrt2)/1\notin\mathbb Q$; dodeca/icosa because $2-2\cos\tfrac\pi{10}$ has degree $4$ over $\mathbb Q$ while $2-\sqrt3$ has degree $2$ (a rational ratio would place the quartic inside $\mathbb Q(\sqrt3)$). Stronger: even a *single declared quadratic* coupling cannot serve — all constants in one quadratic field $K_2$ would force $(2-\sqrt2)/(2-\sqrt3)=4-2\sqrt2+2\sqrt3-\sqrt6\in K_2$ [machine: exact in the $\{1,\sqrt2,\sqrt3,\sqrt6\}$ basis], which lies in no quadratic field ($\mathbb Q(\sqrt2,\sqrt3)$ has degree $4$ over $\mathbb Q$ and over $K_2$). Drag-type proposals ($m\propto$ locked-content reads, e.g. $\rho_{D^-}$: integers $896$ vs $2976$ on the cube/octa pair — the wrong splitting entirely: rational, against an irrational pole ratio) are refuted; the $\Theta_R$-read tracks both splittings natively.
$(4)$ **The $\alpha$ flag.** EM.20 derives $\alpha_{\mathrm{EM}}^{(2)}=\pi$ under Comm-min+Eff — a pure number, independent of $\mathfrak h$, $G_N$, $\kappa$, and every P4 parameter [Eff: historical scope token — Part 3 §0.2(ii); HistLog §I.4]. The proposed "$\alpha\approx1/137$ as the medium's screening factor" contradicts the frozen calibration layer and presupposes the medium refuted in (1): recorded as an inadmissible ask; no screening computation exists or is constructed.
$(5)$ **Adjudication summary (proposal transcript, audit pattern).** *Confirmed (already derived)*: per-edge binary freedom [A4, D0.1, Def-H.25]; the constraint surface $=$ the cap census [CT0.11; FT.68(1)–(3), FT.69(1)]; photon $=$ trivial chain [D3.7, frozen]; "mass $=$ time-averaged real edges" $=$ the $m_{\mathrm{eff}}$ reads [FT.68(1), FT.70(5)]; irrational mass hierarchy $=$ defect radicals [FT.63(6)]; triangle–triangle composition laws $=$ the bowtie/double-triangle/face cells [FT.49, FT.50]; locked content "sits there and gravitates" $=$ CT4.5 dust. *Corrected*: the octahedron "forbidden zone" [FT.70(4)]; "triangle minimal winding $k{=}1$" — the floor fermion is the digon ($k{=}1$, $j{=}\tfrac12$ [FT.28]); the triangle's minimal on-shell winding is $k{=}3$ ($\Theta{=}6$, $\kappa{\equiv}2$; $\kappa{\equiv}1$ gives $\Theta{=}3$, off-shell [FT.22, FT.32]); "tetrahedron $=3$ quarks $+$ singlet seal" — tetrahedron dark sealing is meson-only (even-$\varepsilon$ [FT.63(7)]); the first $\varepsilon$-phase is the face floor [FT.49]; "everything is triangles" [FT.72(1)]; "$3$ colours $=$ triangle edges" — colour is grounded at rung $3$ [D3.1, CT3.x] with the $\{2,3\}$-partition rule [FT.34(5)]; the triangle's $3$ edges supply the first $\varepsilon$-type *correspondence*, not the derivation. *Amplitude-layer verdict on the whole picture*: closed triangles cancel standalone [FT.67(3a)] and never occur inside covers [FT.69(3)(iv)] — the triangle-composition picture is spectral-layer content [Def-H.16, M1/M2], legitimate there and untouched by this tier; the two layers meet only at item 13's open bridge. *Inadmissible*: every particle/cosmological identification (electron/proton/pion/$\rho$/dark matter/black hole/orbitals) — items 5/12 discipline: no calibration data, no identifications, recorded not adopted.

### Def-H.27 — The $\aleph$-domains: literal, chain-dominant, literal-forced

**Def.** Let $R\subseteq E_{\mathrm{dir}}(\Gamma)$ be a crystallization pattern on a skeleton $\Gamma$ [Def-H.25] under scopes (S1), (S3), (S4). Three domains for the vertex-amplitude exponent $\aleph$ entering A8's weight $w=\mathcal J\prod_{e\in R}G(e)(-1)^{\aleph}$, $G(e)=\sigma_e e^{i\pi\kappa_e}$ [D3.5, FT.9]:
**(a) Literal (S2) — frozen.** $\aleph_v=|f_v|$ [D3.3] at type-$(1,1)$ vertices of $R$, $f_v=\tfrac12(\sigma_{\rightarrow}-\sigma_{\leftarrow})$; $\aleph_v=0$ at every other type. No chain data. [This is the domain of FT.67–FT.73 and of the frozen corpus.]
**(b) E1 — chain-dominant.** Configurations $(R,\sigma,D)$ with $D$ a **chain decomposition**: a partition of $R$ into directed walks (edge sequences with $t(e_i)=s(e_{i+1})$ [D1.4]). For each walk $c$: open ($s(c)\ne t(c)$) $\Rightarrow$ interior vertices $=$ all but the two endpoints; closed ($s(c)=t(c)$; D1.4's Janus clause is trivial at (S3)) $\Rightarrow$ **every** vertex of $c$ is interior, the start vertex included — arrival on the last edge, departure on the first (the **wrap read**). Then
$$
\aleph(\sigma,R,D)=\sum_{c\in D}\ \sum_{v\in\mathrm{int}(c)}\bigl|f_v(c)\bigr|,\qquad f_v(c)=\tfrac12\bigl(\sigma_{\mathrm{out}(c,v)}-\sigma_{\mathrm{in}(c,v)}\bigr)\ \text{in }c\text{'s own edges at }v,
$$
and $Z^{E1}_\Gamma=\sum_R\sum_D\sum_\sigma w^{E1}$.
**(c) E2 — literal-forced.** At type-$(1,1)$ vertices the literal D3.3 read is retained *regardless of $D$* — the chain choice there is $\aleph$-gauge: such a vertex has a unique in- and a unique out-edge in $R$, so every passage through it gives the same $f_v$ and the datum is type-determined. At higher-type vertices the reads come from chain passages. Equivalently — and this is the form computed — the summed datum is the **partial-matching system** $M=(M_v)_{v\ \mathrm{higher}}$, each $M_v$ a partial matching between $\mathrm{in}_R(v)$ and $\mathrm{out}_R(v)$; the orbits of the induced partial bijection on $R$ are the chains, and an orbit that is a *path returning to its start vertex* is a closed chain in the sense of (b) and gains the wrap read there:
$$
\aleph(\sigma,R,M)=\sum_{v\ (1,1)}|f_v|+\sum_{v\ \mathrm{higher}}\ \sum_{(e,e')\in M_v}\bigl|f(e,e')\bigr|+\sum_{\mathrm{wraps}}|f|,
\qquad Z^{E2}_\Gamma=\sum_R\sum_M\sum_\sigma w^{E2}.
$$

### FT.74 — The extended exact-cover theorems

**Thm.** Under Def-H.27, at (S1); for general on-shell integer $\kappa$ every value below scales by $(-1)^{\sum_e\kappa_e}$ and no classification changes. Write $\varepsilon(R):=(-1)^{|R|}2^{|R|}$: on the support of either classifier $|R|$ is even [each thread contributes $2$ edges], so $\varepsilon(R)=2^{|R|}>0$ and the stated values are the exact amplitudes.
$(1)$ **E1 classification.**
$$
\sum_D\ \sum_\sigma w^{E1}(R,\sigma,D)=N_{E1}(R)\cdot\varepsilon(R),
$$
where $N_{E1}(R)$ is the number of partitions of $R$ into **open directed $2$-threads** $s\to v\to t$ ($s\ne t$; the junction $v$ of any type — locked junctions included). Every other decomposition cancels: a walk of length $\ge3$ double-reads its interior edges; a length-$1$ walk leaves its edge unread ($\operatorname{cov}=0$); a closed walk double-reads every edge (all vertices interior, wrap included); a closed $2$-thread — a digon — is a closed chain [D1.4] and cancels by the same wrap read.
$(2)$ **E2 classification.**
$$
\sum_M\ \sum_\sigma w^{E2}(R,\sigma,M)=N_{E2}(R)\cdot\varepsilon(R),
$$
with $N_{E2}(R)=0$ unless **(a)** no edge of $R$ joins two type-$(1,1)$ vertices (such an edge is read literally twice), and **(b)** every literal thread at a type-$(1,1)$ vertex is open — a literal thread whose two ends coincide is a closed chain [D1.4], and its wrap read double-reads both edges. Otherwise $N_{E2}(R)$ is the number of open-$2$-thread partitions of the **higher-only remainder** $R_{\mathrm{hh}}:=\{e\in R:\ \text{neither endpoint is type-}(1,1)\}$, junctions necessarily higher-type; the forced literal threads cover exactly the edges touching type-$(1,1)$ vertices, once each.
$(3)$ **Pointwise order, and incomparability of the three domains.** $N_{E2}(R)\le N_{E1}(R)$ for every $R$ on every skeleton (an E2 structure maps injectively to its thread partition: forced literal threads are open by (2b), edges with a $(1,1)$ endpoint are covered exactly once by (2a)-(2b), and the $R_{\mathrm{hh}}$ threads are E1 threads) — machine-asserted with zero violations on $9472$ patterns (the tetrahedron and bidirectional $P_4/P_5/P_6$, exhaustively), together with $|R|$ even on both supports. The literal domain embeds into neither extension and neither into it. Witnesses (triples $(\mathrm{lit},E2,E1)$; machine: classifier $=$ brute-force sum on each row):
$$
\begin{array}{l|cccccc}
R & \text{digon} & \text{dir. }3\text{-cycle} & \text{dir. }4\text{-cycle}^{*} & \text{double-thread hub} & \text{digon-pair hub} & \text{bidir }P_4\text{ floor}\\
\hline
(\mathrm{lit},E2,E1) & (0,0,0) & (0,0,0) & (0,0,32) & (0,32,32) & (16,0,16) & (0,1024,1024)
\end{array}
$$
$^{*}$on the $4$-cycle skeleton. The **digon-pair hub** $R=\{(0{\to}1),(1{\to}0),(0{\to}2),(2{\to}0)\}$, types $\bigl((2,2),(1,1),(1,1)\bigr)$ — the FT.69(4)/FT.69(5) witness family — has literal value $16$, is killed by E2 (both literal threads are closed) and revived by E1 at the alternative threading $\{(2{\to}0),(0{\to}1)\},\{(1{\to}0),(0{\to}2)\}$: $N_{\mathrm{lit}}\not\le N_{E2}$. The **directed $4$-cycle** gives $N_{E2}=0<N_{E1}=2$ (strictness of (3)'s order). The **double-thread hub** $\{(0{\to}2),(1{\to}2),(2{\to}3),(2{\to}4)\}$ has literal value $0$ and extended value $32$: both extensions exceed the literal domain. **The digon — the $\Sigma_{\min}$ pattern [FT.28] — cancels in all three domains**: the minimal floor's absence from the amplitude layer is domain-invariant.
$(4)$ **Equality locus.** On patterns with no type-$(1,1)$ vertex, E2 $\equiv$ E1 exactly (no literal reads exist; in particular on every fully crystallized floor, all of whose vertices are type $(d,d)$, $d\ge2$ [FT.62]). There the extended value is $N\cdot\varepsilon(R)$ with $N$ the open-thread partition count, and the literal value is $0$ whenever $R\ne\varnothing$ [FT.67(3a)].
$(5)$ **Machine verification.** The classifications are verified against brute-force sign sums taken straight from Def-H.27's semantics — E1 by explicit enumeration of *all* walk partitions $D$ with interior/wrap reads, E2 by explicit enumeration of *all* partial-matching systems $M$ with orbit-wrap closure — on **every** pattern of seven families: the digon ($2^2$), the bidirectional triangle ($2^6$), bidirectional $P_4$ ($2^8$), the single-vertex stars $n\in\{4,5,6\}$ ($2^4,2^5,2^6$), and all tetrahedron patterns with $K\le4$ ($794$): **$2460$ pattern-domain checks, zero mismatches**.

### FT.75 — Domain-relativity of the amplitude layer: lock revival, floor revival, parity, and the invariant bridge gap

**Thm.** Under Def-H.27/FT.74, at (S1):
$(1)$ **Single vertex — the locked sector comes alive, in two closed forms.** For the balanced single-vertex star ($n_{\mathrm{in}}+n_{\mathrm{out}}=n\in\{4,5,6\}$, external endpoints simple), $Z^{\pm}_{\mathrm{byp}}$ is domain-invariant $=1+4n_{\mathrm{in}}n_{\mathrm{out}}=(17,25,37)$ [FT.67(5)], while
$$
Z^{\pm}_{\mathrm{lock}}:\quad\text{literal }0;\qquad E2=E1=\sum_{a\ge2}\binom{n_{\mathrm{in}}}a\binom{n_{\mathrm{out}}}a\,a!\,4^{a}=(32,\ 96,\ 672),
$$
totalling $(49,121,709)$ across both sectors. **FT.67(5)'s "its locked sector vanishes identically" is a literal-domain theorem**: in the chain-local domains an isolated locked vertex has strictly positive amplitude — the type-$(a,a)$ patterns thread *through the vertex itself*. Second family (the locked digon hub): a locked $(a,a)$ hub hosting $a$ digons with $a$ simple centres has
$$
\text{literal}=4^{a},\qquad E2=0\ \ (\text{every literal thread closed}),\qquad E1=\bigl(!a\bigr)\,4^{a},
$$
$!a$ the derangement number (each thread must leave its own centre: a fixed-point-free permutation of the $a$ digons), machine-verified for $a=2,3,4,5$ with brute force at $a\le3$: $(16,128,2304,45056)$ against literal $(16,64,256,1024)$. The tetrahedron's $16$ locked digon-covers are exactly the $a=2$ ($12$; value $16$) and $a=3$ ($4$; value $128$) instances [FT.69(5)].
$(2)$ **Floor revival — the dichotomy is domain-relative.** Every fully crystallized floor has no type-$(1,1)$ vertex, so E2 $\equiv$ E1 there [FT.74(4)], and the extended amplitude is strictly positive whenever the thread-partition count is:
$$
N(\text{tetra floor})=32\ \ (\text{value}\ 2^{17}),\quad N(\text{cube floor})=2304\ \ (2304\cdot2^{24}),\quad N(\text{octa floor})=72384\ \ (72384\cdot2^{24})
$$
— versus literal amplitude $0$ [FT.67(3a)]. Dodecahedron/icosahedron floor counts deferred (branch enumeration beyond the bounded rule; recorded, not guessed). **Bidirectional polygon floors obey an exact parity theorem**:
$$
N\bigl(\Sigma_{P_L}\ \text{floor}\bigr)=\begin{cases}4 & L\ \text{even}\quad(\text{value}\ 4\cdot2^{2L}),\\[2pt] 0 & L\ \text{odd},\end{cases}
$$
machine-verified $L=3..10$ $(0,4,0,4,0,4,0,4)$. **FT.68(4)'s verdict "fuzzing into solids — no at the amplitude layer" is the literal-domain verdict; in the chain-local domains every computed even polygon floor and the three computed Platonic floors carry strictly positive amplitude** (odd polygon floors stay dead by parity; the dodecahedron/icosahedron floors are open counts, not known-zero).
$(3)$ **Directed cycles split the domains.** The single-orientation directed cycle $C_L$: literal $0$; E2 $0$ for every $L\ge2$ (all vertices type-$(1,1)$: conditions (2a)-(2b) fail); E1 $=2\cdot2^{L}$ for even $L$ — the cycle's two perfect matchings — and $0$ for odd $L$ ($|R|$ odd). Machine: $L=3..10$, values $(0,32,0,128,0,512,0,2048)$. The on-shell winding ladder's even rungs [FT.22] are exactly the E1-survivors; the digon ($L=2$) is dead in all three [FT.74(3)].
$(4)$ **Bound content returns — the triangle census, and the digon-cover split.** On the tetrahedron (exhaustive, all $4096$ patterns): $2397$ patterns contain a directed $3$-cycle; of those, nonzero amplitude — literal $0$, E2 $833$, E1 $1025$; restricted to the bypass sector: $0/40/88$ (the FT.68(1)/FT.69(4) anchor "$0$ nonzero of $252$" is the bypass-only carrier count and stands). Exhibit: $R=\{(0{\to}1),(0{\to}3),(1{\to}2),(2{\to}0)\}$, threads $\{0{\to}1{\to}2\},\{2{\to}0{\to}3\}$, E1 value $16$ (classifier $=$ brute force). **The cycle-alternation lemma [FT.69(3)] is a literal-domain theorem and fails in both extensions** — chain-local threading dissolves odd cycles into open threads. The digon rows split by sector (machine, exhaustive): the $48$ *bypass* digon-covers of FT.69(4) are killed by **both** extensions ($N_{E2}=N_{E1}=0$ on all $48$ — a dissolved digon's centre has no alternative threading), while the $16$ *locked* digon-covers are killed by E2 and kept by E1 [clause (1)'s derangement family].
$(5)$ **Skeleton totals (exhaustive; the literal column reproduces the stored anchors exactly).**
$$
\begin{array}{l|ccc}
& Z^{\pm}_{\mathrm{byp}} & Z^{\pm}_{\mathrm{lock}} & \#\text{nonzero (byp/lock)}\\
\hline
\text{tetra, lit} & 1057 & 448 & 85/16\\
\text{tetra, E2} & 5921 & 966656 & 173/934\\
\text{tetra, E1} & 6881 & 1001536 & 227/1166\\
\hline
P_3\ \text{bidir, lit/E2/E1} & 25/121/121 & 48/0/48 & 7/13/13\ \text{byp};\ 3/0/3\ \text{lock}\\
P_4\ \text{bidir, lit/E2/E1} & 353/225/289 & 64/1536/2112 & 29/21/23;\ 4/9/13\\
P_5\ \text{bidir, lit/E2/E1} & 1161/361/1801 & 80/5760/8400 & 51/31/61;\ 5/30/60\\
P_6\ \text{bidir, lit/E2/E1} & 3121/3697/7985 & 1632/50944/80224 & 97/79/135;\ 21/67/154
\end{array}
$$
The $P_3$ locked row exhibits the second incomparability at skeleton level: E2 kills every literal locked cover there (each is a digon-pair hub — a closed literal thread), E1 keeps all $48$.
$(6)$ **Norm-layer invariance, with the exact configuration count.** In every domain every factor of $w$ is a sign — $|w(R,\sigma)|=|w(R,\sigma,D)|=|w(R,\sigma,M)|=1$ (machine: asserted on every $(R,D,\sigma)$ of the bidirectional triangle) — so CT2.8's norms $\sum|w|^2$ count configurations: strictly positive, cancellation-blind, and *form-identical across domains*. At the pattern-sign layer the count is exactly
$$
\#\{(R,\sigma)\}=\sum_{R\subseteq E_{\mathrm{dir}}}2^{|R|}=3^{\,|E_{\mathrm{dir}}(\Gamma)|}
\qquad(\text{machine:}\ 3^6=729,\ 3^8=6561,\ 3^{12}=531\,441\ \text{for}\ P_3,P_4,\text{tetra}),
$$
each directed edge contributing (absent, $+$, $-$); the extended domains refine this set by an inner sum over $D$/$M$ and cannot change it. **Item 13's bridge question is therefore invariant under the $\aleph$-domain choice**: no domain rescues or worsens it — exit (b) must operate on resolvent structure in every domain alike.
$(7)$ **Gap 16(d) verdict.** The $\aleph$-domain question of the EM row is now exact data: three domains, three provably distinct path integrals, a complete witness catalogue [(3)–(5)], the frozen answer unchanged (D3.3's literal domain governs A8's $\aleph$), and the two chain-local variants computed but not adopted. The residue — whether FT.62(5)'s observed-variant EM-row reads should govern the *weight* as well — is an author's declaration whose consequences are now fully priced on both sides.
$(8)$ **What is not domain-relative.** The cap census $c_K$ [FT.69(1)], the admissibility fractions $f_{\mathrm{adm}}(n,p)$, the phase-diagram reads $B_\Gamma(p)$, $L_\Gamma(p)$, $p^*_\Gamma$, $\langle K\rangle_{\mathrm{byp}}(p)$ [Def-H.26, FT.70] and the dust equation of state $\langle\rho_{D^-}\rangle_\Gamma(p)$ with $w=0$ [FT.71, CT4.5] are counting/type-level objects: none involves $\aleph$, so all are identical in the three domains — the phase boundaries of FT.70(2) and the dust densities of FT.71 stand as computed. Only the amplitude-side sums $Z^{\pm}$, the survivor grammar, and the censuses built from them are domain-relative. Covering *enumeration* likewise splits: the literal covers of FT.69(2) are a proper subset of the E1-survivors on every computed skeleton [clause (5)].

### FT.76 — The Platonic pole-mass multiplets; the bounded-hierarchy ceiling

**Thm.** Under Def-H.37(2) and Def-H.38, with $\Theta_R=\delta_v$ [FT.63(4)'s vertex-figure read; the corner convention of Open Gaps 16(e) is *not* declared], $D_S(m):=m^2_{\mathrm{pole}}(m)/\hat\mu'^2=2-2\cos(m\,\delta_v/2)=4\sin^2(m\,\delta_v/4)$ [FT.60(5)], and $k$ the carrier winding [Def-H.38]:
$(1)$ **Conventions and the two trivial readings.** $k_f=K_S/F=(3,2,3,5,3)$ (face winding; $K_S=(12,12,24,60,60)$ [FT.63(1), FT.43(1)], reproduced from the minimality rule $\kappa_{\min}=2$ odd-$L$ / $1$ even-$L$, $k=L\kappa_{\min}/2$ [FT.32(6), FT.45]); $k_{vf}=(3,3,2,3,5)$ (vertex-figure winding, same rule on the vertex-figure $L_{vf}=(3,3,4,3,5)$). **Variant (A)** $:=$ $(\delta_v,k_f)$ — the directive's reading; **variant (B)** $:=$ $(\delta_v,k_{vf})$ — the loop-consistent reading. Both other readings named by FT.63(4)/(6) are identically massless: $\Theta_R=0$ (flat-face side) and $\Theta_R=V\delta_v=4\pi$ (global sweep: $D(m)=2-2\cos(2m\pi)=0$ for every weight — FT.63(4)'s trivial global spinor transport).
$(2)$ **Exact multiplets.** With $c=\cos\tfrac\pi{10}$ ($16c^4-20c^2+5=0$):
$$
\begin{array}{c|c|c|c}
S & \text{(A)}\ k_f & m^2_{\mathrm{pole}}/\hat\mu'^2\ \text{on}\ \{k,k{-}2,\dots,-k\} & \text{field}\\
\hline
\text{tetra} & 3 & 2,\ 2,\ 2,\ 2\ (m=\pm1,\pm3) & \mathbb Q\\
\text{cube} & 2 & 2\ (m=\pm2),\ \mathbf 0\ (m=0) & \mathbb Q\\
\text{octa} & 3 & 4\ (m=\pm3),\ 1\ (m=\pm1) & \mathbb Q\\
\text{dodeca} & 5 & 2\ (m=\pm5),\ 2{-}2\cos\tfrac{3\pi}{10}\ (m=\pm3),\ 2{-}2c\ (m=\pm1) & \mathbb Q(c)\\
\text{icosa} & 3 & 2\ (m=\pm3),\ 2{-}\sqrt3\ (m=\pm1) & \mathbb Q(\sqrt3)
\end{array}
$$
$$
\begin{array}{c|c|c|c}
S & \text{(B)}\ k_{vf} & m^2_{\mathrm{pole}}/\hat\mu'^2 & \text{field}\\
\hline
\text{tetra} & 3 & 2,\ 2,\ 2,\ 2 & \mathbb Q\\
\text{cube} & 3 & 2{+}\sqrt2\ (m=\pm3),\ 2{-}\sqrt2\ (m=\pm1) & \mathbb Q(\sqrt2)\\
\text{octa} & 2 & 3\ (m=\pm2),\ \mathbf 0\ (m=0) & \mathbb Q\\
\text{dodeca} & 3 & 2{-}2\cos\tfrac{3\pi}{10},\ 2{-}2c & \mathbb Q(c)\\
\text{icosa} & 5 & 2{+}\sqrt3\ (m=\pm5),\ 2\ (m=\pm3),\ 2{-}\sqrt3\ (m=\pm1) & \mathbb Q(\sqrt3)
\end{array}
$$
Decimals ($m^2/\hat\mu'^2$): dodeca $(0.097886967410,\ 0.824429495415,\ 2)$; icosa $(0.267949192431,\ 2)$, (B) adds $3.732050807569$; cube (B) $(0.585786437627,\ 3.414213562373)$. Every value is exact in the stated field and was cross-checked against an exact rational Taylor series for $\cos$ to $45$ digits ($125$ values, $m=0..24$, all five solids).
$(3)$ **Periodicity, monotonicity, and the hard ceiling.** The ladder is periodic in the weight with period $P_S=4\pi/\delta_v=(4,8,6,20,12)$ and takes exactly $P_S/2+1=(3,5,4,11,7)$ distinct values, monotone increasing in $m$ on $[0,P_S/2]$; the maximum is $4\hat\mu'^2$ (attained at $m=P_S/2$; $P_S$ even for all five) and the minimum nonzero value is $D_S$ itself. Hence **every Platonic pole mass lies in $[0,4\hat\mu'^2]$** and the widest ratio attainable *within* a solid is
$$
\frac{4}{D_S}=\Bigl(2,\ \tfrac{4}{2-\sqrt2},\ 4,\ \tfrac{4}{2-2\cos\frac\pi{10}},\ \tfrac{4}{2-\sqrt3}\Bigr)=(2,\ 6.828427,\ 4,\ 40.863458,\ 14.928203)\ \ \text{in}\ m^2,
$$
maximal for the dodecahedron, whose value has minimal polynomial $x^4-48x^3+304x^2-512x+256$; in **mass** the ceiling is $\sqrt{4/D_S}=(1.414214,\ 2.613126,\ 2,\ 6.392453,\ 3.863703)$, maximal at $6.392453\ldots$ No choice of winding — $k_f$, $k_{vf}$, $K_S$, or any iterate — and no admissible $\Theta_R$ convention can exceed it: the value set is finite and bounded.
$(4)$ **Top-weight near-universality.** In variant (A) the heaviest weight of *four of the five* solids is exactly $2\hat\mu'^2$ ($k_f\delta_v\equiv\pi\bmod 2\pi$: tetra $3\pi$, cube $\pi$, dodeca $\pi$, icosa $\pi$), the octahedron's being $4\hat\mu'^2$ ($k_f\delta_v=2\pi$). The inter-solid hierarchy therefore lives **entirely at the light end**; the heavy ends are degenerate across solids.
$(5)$ **Two structural obstructions.** (a) **Tetrahedral degeneracy**: $\delta_v=\pi\Rightarrow D(m)=2-2\cos(m\pi/2)\in\{0,2,4\}$, and the $k=3$ multiplet is *fully degenerate* at $2\hat\mu'^2$ (both variants) — the tetrahedron carries no multiplet splitting at all. (b) **Even-$k$ zero modes** [FT.60(5)'s standing zero]: the cube in (A) ($k_f=2$) and the octahedron in (B) ($k_{vf}=2$) each carry an exactly massless weight $m=0$, so their literal "lightest pole mass" is $0$ and only lightest-*nonzero* reads are well defined.
$(6)$ **Inter-solid ratios (lightest nonzero, relative to the tetrahedron).**
$$
\begin{array}{c|cc|cc}
& \multicolumn2{c|}{\text{(A)}} & \multicolumn2{c}{\text{(B)}}\\
S & m^2\ \text{ratio} & m\ \text{ratio} & m^2\ \text{ratio} & m\ \text{ratio}\\
\hline
\text{tetra} & 1 & 1 & 1 & 1\\
\text{cube} & 1\ (0\ \text{with the zero mode}) & 1\ (0) & 0.292893218813 & 0.541196100146\\
\text{octa} & 0.5 & 0.707106781187 & 1.5 & 1.224744871392\\
\text{dodeca} & 0.048943483705 & 0.221231742082 & 0.048943483705 & 0.221231742082\\
\text{icosa} & 0.133974596216 & 0.366025403784 & 0.133974596216 & 0.366025403784
\end{array}
$$
Normalized to the lightest solid, in mass: (A) dodeca $1$, icosa $1.654488638651$, octa $3.196226610750$, cube $=$ tetra $4.520147021340=\sqrt{2/(2-2c)}$; (B) dodeca $1$, icosa $1.654488638651$, cube $2.446285940037$, tetra $4.520147021340$, octa $5.536026882322$.
$(7)$ **Intra-solid splittings (heaviest/lightest nonzero).**
$$
\begin{array}{c|cc|cc}
S & \text{(A)}\ m^2 & \text{(A)}\ m & \text{(B)}\ m^2 & \text{(B)}\ m\\
\hline
\text{tetra} & 1 & 1 & 1 & 1\\
\text{cube} & 1\ (+1\ \text{zero mode}) & 1 & 3{+}2\sqrt2=5.828427124746 & 1{+}\sqrt2=2.414213562373\\
\text{octa} & 4 & 2 & 1\ (+1\ \text{zero mode}) & 1\\
\text{dodeca} & \tfrac{2}{2-2c}=20.431729094531 & 4.520147021340 & \tfrac{2-2\cos(3\pi/10)}{2-2c}=8.422260053931 & 2.902113032590\\
\text{icosa} & 4{+}2\sqrt3=7.464101615138 & 1{+}\sqrt3=2.732050807569 & 7{+}4\sqrt3=13.928203230276 & 2{+}\sqrt3=3.732050807569
\end{array}
$$
Minimal polynomials of the $m^2$ splittings: dodeca (A) $x^4-24x^3+76x^2-64x+16$, dodeca (B) $x^4-14x^3+51x^2-34x+1$, icosa (A) $x^2-8x+4$, icosa (B) $x^2-14x+1$, cube (B) $x^2-6x+1$; the mass splittings $1{+}\sqrt3$, $2{+}\sqrt3$, $1{+}\sqrt2$ have $x^2-2x-2$, $x^2-4x+1$, $x^2-2x-1$ (machine; certified dyadic isolations).
$(8)$ **Dual splitting, sharpened.** The dual pairs remain degenerate in $m_{\mathrm{hid}}$ and $\Pi$ [FT.44(1)] and split on the pole side as multisets in *both* variants — cube $\{0,2\}$ vs octa $\{1,4\}$ in (A), cube $\{2{-}\sqrt2,2{+}\sqrt2\}$ vs octa $\{0,3\}$ in (B); dodeca vs icosa share only the top value $2\hat\mu'^2$ in (A) and nothing in (B). FT.44(2)'s splitting template acquires its multiplet form.
$(9)$ **Field-degree ledger.** Tetra/octa: $\mathbb Q$; cube: $\mathbb Q(\sqrt2)$; icosa: $\mathbb Q(\sqrt3)$; dodeca: $\mathbb Q(\cos\tfrac\pi{10})$, degree $4$, with $\sqrt5=8c^2-5$ its unique quadratic subfield (machine) — the requested four-field list $\{\mathbb Q,\mathbb Q(\sqrt2),\mathbb Q(\sqrt3),\mathbb Q(\sqrt5)\}$ is **insufficient for the dodecahedron**, exactly as FT.73(2)'s degree-$16$ compositum requires.
$(10)$ **FT.63(6) precision correction.** The dodecahedral quartic $x^4-8x^3+19x^2-12x+1$ has **four positive roots** (machine-isolated to width $2^{-60}$): $0.097886967410$, $0.824429495415$, $3.175570504585$, $3.902113032590$, realized by the weights $m\in\{1,19\},\{3,17\},\{7,13\},\{9,11\}$ respectively. FT.63(6)'s "$D(1),D(3)$ the two positive roots of the quartic" corrects to **the two smallest of its four positive roots**; patched in place (marker).

### FT.77 — The SM-hierarchy audit: a bounded-hierarchy negative result

**Thm.** **External-data clause.** The three hierarchies compared below — charged leptons $1{:}207{:}3477$, up-type quarks $1{:}600{:}80000$, down-type quarks $1{:}20{:}900$ — are *supplied measured data* (2–3 significant figures). They enter no derivation, no definition and no corpus result; A §0.2 admits no imported measured value, and this document identifies no particles (Open Gaps 5/12). This clause is an **adjudication cell** in the FT.73(5) pattern: its output is a verdict about a proposed identification, not a physical claim.
$(1)$ **Audit method, maximally generous to the hypothesis.** The comparison pool is *every* nonzero pole value of *every* solid at *every* weight of the full periodic ladder [FT.76(3)] — $(2,4,3,10,6)$ distinct values per solid, $25$ in all, $16$ distinct across the five solids, giving $120$ pairwise ratios and $\binom{16}{3}=560$ triples; no winding, no variant and no iterate is excluded — and ratios are taken in **mass** ($m=\sqrt{D}\,\hat\mu'$), since the ladder supplies $m^2$. A match requires an *aligned triple*: three pool values whose normalized ratios reproduce a family's two ratios simultaneously.
$(2)$ **The ceiling obstruction.** The pool's mass ratios are bounded above by $\sqrt{4/D_{\mathrm{dodeca}}}=6.392453\ldots$ [FT.76(3)] while the smallest top-ratio among the three families is $900$. Hence **no aligned triple can match any SM family**; the best achievable discrepancy factors are
$$
\times140.79\ (\text{down-type}),\qquad\times543.92\ (\text{charged leptons}),\qquad\times12514.76\ (\text{up-type}),
$$
exhaustive over all $560$ triples (machine). Pairwise, the closest single ratio is the pool maximum against the families' minimum ($m_\tau/m_\mu=16.797$): $\times2.63$ — within an order of magnitude, and structurally void: it pairs the two extremes and extends to no triple.
$(3)$ **The dimension trap, disclosed.** Comparing $m^2$-ratios to SM *mass* ratios — dimensionally wrong — produces the only near-coincidences available: $20.431729$ vs $m_s/m_d=20$ ($\times1.0216$); $40.863458$ vs $m_b/m_s=45$ ($\times1.1012$); $14.928203$ vs $m_\tau/m_\mu=16.797$ ($\times1.1252$). All three are rejected: the ladder computes $m^2_{\mathrm{pole}}$, and Def-H.37(2) supplies no square-root reassignment.
$(4)$ **Structural failures, independent of any fitting.** (a) The tetrahedron's multiplet is fully degenerate [FT.76(5a)] — it cannot carry a three-member family in either variant. (b) Even-$k$ multiplets contain an exactly massless weight [FT.76(5b)] — no charged SM fermion is massless, so the cube in (A) and the octahedron in (B) are excluded as family carriers outright. (c) Only two multiplets in the entire audit have three distinct masses — dodecahedron $k_f=5$ (A) and icosahedron $k_{vf}=5$ (B) — with mass ratios $1{:}2.902113{:}4.520147$ and $1{:}2.732051{:}3.732051$; their best discrepancies are $\times199.11$ and $\times241.15$ (down-type), $\times769$ and $\times932$ (leptons), $\times17699$ and $\times21436$ (up-type). (d) Five solids against three generations, with both dual pairs degenerate in $m_{\mathrm{hid}}$/$\Pi$ [FT.44(1)] and split only on the pole side [FT.76(8)]: no solid-to-generation assignment is available without calibration data the corpus does not supply (items 5/12). (e) Two of the four readings of $\Theta_R$ named by FT.63(4)/(6) give identically zero pole mass [FT.76(1)].
$(5)$ **Quantitative distance.** Reaching even the least hierarchical family ($1{:}900$ in mass) with the ceiling $\max=4\hat\mu'^2$ would require a lightest defect value $D\le4/810000=1/202500=4.938\times10^{-6}$, i.e. — exactly, since $D=4\sin^2(\delta_v/4)$ — a cone defect $\delta_v\le4\arcsin\tfrac1{900}=4.4444\times10^{-3}$ rad $=0.2546^\circ$. The smallest Platonic defect is $\delta_v=\pi/5=36^\circ$: the available defects are a factor $45\pi=141.37$ too **large** in angle and $19822$ too large in $D$ — equivalently, the Platonic mass span is $140.79$ times too *small*. The two shortfalls agree to $0.5\%$ because $m\propto\delta_v$ at small angles. The obstruction is one of scale, not of pattern.
$(6)$ **Verdict.** The hypothesis "Platonic vertex defects $=$ SM family hierarchies" **fails at the pole-mass layer**, conditionally on Def-H.37(2)/Def-H.38 and the vertex-figure convention, and — by the ceiling argument of (2) — unconditionally on the winding choice and on which solid is assigned to which family. No match is claimed, no parameter is fitted, and no identification is made. What survives as corpus content: the exact bounded multiplets of FT.76, the ceiling theorem, and the sharpened form of Gap 7's residue — **any replacement for the Def-H.37(2) transfer must supply a dynamical range of at least three orders of magnitude if it is ever to reach observed mass hierarchies; the defect species, on the Platonic skeletons, supplies at most $6.4\times$.**

### Def-H.28 — Cover classes, and the two class-mass ansätze

**Def.** Let $\Gamma$ be a skeleton [Def-H.25] with directed edge set $E_{\mathrm{dir}}(\Gamma)$ and automorphism group $\operatorname{Aut}(\Gamma)$ acting on vertices, hence on $E_{\mathrm{dir}}(\Gamma)$ by $(a,b)\mapsto(p(a),p(b))$. A **cover class** (orbit class) is an $\operatorname{Aut}(\Gamma)$-orbit $\mathcal O$ of crystallization patterns $R\subseteq E_{\mathrm{dir}}(\Gamma)$; its **multiplicity** is $\Omega_{\mathcal O}=|\mathcal O|$, with $\Omega_{\mathcal O}\cdot|\operatorname{Stab}(R)|=|\operatorname{Aut}(\Gamma)|$ [orbit–stabilizer] and hence $\Omega_{\mathcal O}\mid|\operatorname{Aut}(\Gamma)|$. Invariants of a class (all constant on $\mathcal O$, machine-verified): $K=|R|$; admissibility ($k_v\le3\ \forall v$) and lock status; cover status and $|\mathcal C|$; amplitude $4^{|\mathcal C|}$ [FT.67(2)]; the canonical directed-cycle content of $R$ (its **signature**: which cycles the cover shadows); the aspect mask $\mathcal A(\max_v k_v)$ and observable mask dimension [CT0.13, CT0.14]. The two class-mass reads:
$$
\textbf{A (corpus-native)}:\quad m_A(\mathcal O)=K\,\frac{\ln2}{\mathfrak h}\qquad[\text{FT.68}(1)/\text{FT.70}(5)\text{'s}\ \langle K\rangle\ln2/\mathfrak h\ \text{read, per class};\ \neg\text{new datum}],
$$
$$
\textbf{B (external ansatz, NOT a corpus read)}:\quad m_B(\mathcal O)=\Bigl(K-\alpha\ln\Omega_{\mathcal O}\Bigr)\frac{\ln2}{\mathfrak h},\qquad\alpha\ \text{a formal parameter, no value declared}.
$$

### FT.78 — The orbit decompositions: tetrahedron exhaustive, cube symmetry-reduced

**Thm.** Under Def-H.28, at (S1)–(S4):
$(1)$ **Tetrahedron, exhaustive.** The $1230$ admissible configurations [FT.68(1)] form **$70$ orbits** under $\operatorname{Aut}=S_4$ ($|\operatorname{Aut}|=24$), with $\sum_{\mathcal O}\Omega_{\mathcal O}=1230$; orbits by $K$: $(1,1,5,13,23,21,6)$ for $K=0..6$; configuration counts by $K$ reproduce the cap row $(1,12,66,220,435,408,88)$ [FT.68(1)] exactly; $\Omega\in\{1,3,4,6,8,12,24\}$, every value dividing $24$.
$(2)$ **Tetrahedron cover sector: seven orbits total.** The $85$ bypass covers form $5$ orbits and the $16$ locked covers $2$ orbits:
$$
\begin{array}{c|cccccc}
\text{sector} & K & |\mathcal C| & \Omega & 4^{|\mathcal C|} & \text{signature (cycles shadowed)} & \text{type multiset}\\
\hline
\text{byp} & 0 & 0 & 1 & 1 & () & (0,0)^4\ \text{(vacuum)}\\
\text{byp} & 2 & 1 & 24 & 4 & () & (0,0),(0,1),(1,0),(1,1)\ \text{single thread}\\
\text{byp} & 4 & 2 & 24 & 16 & (2) & (1,0),(1,1)^2,(1,2)\\
\text{byp} & 4 & 2 & 24 & 16 & (2) & (0,1),(1,1)^2,(2,1)\\
\text{byp} & 4 & 2 & 12 & 16 & () & (0,2),(1,1)^2,(2,0)\ \text{double thread}\\
\hline
\text{lock} & 4 & 2 & 12 & 16 & (2,2) & \text{double-digon }(2,2)\text{ hub}\\
\text{lock} & 6 & 3 & 4 & 64 & (2,2,2) & K_{1,3}\ \text{star hub}
\end{array}
$$
—the two locked rows being exactly FT.69(5)'s minimal dissolution family ($12$) and the four $K_{1,3}$ triple-digon stars [FT.68(1)]. The single-centre orbit's size $24=Vd(d{-}1)$ is FT.69(2)'s closed form.
$(3)$ **Orbit-level amplitude identity (new).** The amplitude sum decomposes exactly over classes:
$$
\sum_{\mathcal O}\Omega_{\mathcal O}\,4^{|\mathcal C(\mathcal O)|}=Z^{\pm},
$$
machine-verified on both skeletons: tetrahedron $1057$ (bypass) and $448$ (locked) [FT.68(1)]; cube $1\,109\,313$ and $1\,150\,848$ [FT.68(3)]. Consequently the covering-polynomial coefficients are the $|\mathcal C|$-level *configuration* counts, and the orbit counts refine them: cube bypass $|\mathcal C|=0..4\Rightarrow(1,1,19,57,88)$ orbits over $(1,48,648,2672,3624)$ configurations; locked $|\mathcal C|=2..6\Rightarrow(1,18,71,7,1)$ over $(24,728,3192,264,4)$.
$(4)$ **Cube, symmetry-reduced.** Cap row $(1,24,276,2024,10506,40296,115796,247704,383913,408464,270096,91392,9600)$, total $1\,580\,092$ configurations with $K\le12$ forced [FT.68(3)]; cap-aware Burnside over $|\operatorname{Aut}|=48$ gives orbits by $K$ $(1,1,11,49,250,863,2509,5211,8163,8571,5768,1922,245)$, total $33\,564>10^4$ — the bounded rule is observed, so full configuration enumeration is *not* attempted. The **cover sector is enumerated explicitly** (it is small): the $11\,205$ covers ($6993$ bypass $+\,4212$ locked, two independent enumerators agreeing [FT.69(2)]) form **$264$ orbits** ($166$ bypass, $98$ locked), $\sum\Omega=11\,205$, $\Omega\mid48$ throughout, with $\Omega$-histogram $\{1{:}1,\ 4{:}1,\ 8{:}1,\ 12{:}4,\ 16{:}2,\ 24{:}47,\ 48{:}208\}$ — the $208$ free orbits are the generic case, so the twenty most populated classes are all free orbits ($\Omega=48$) and are distinguished only by signature: one at $|\mathcal C|=1$ (the single thread), eight at $|\mathcal C|=2$ (four cycle-free, four shadowing one digon), eleven at $|\mathcal C|=3$. **Independent cross-validation:** explicit canonical-form enumeration of every admissible configuration with $K\le5$ ($53\,127$ of them) reproduces the Burnside row $(1,1,11,49,250,863)$ exactly — two methods, same numbers.
$(5)$ **Signatures.** Covers shadow only **even** cycles, orbit by orbit [FT.69(3)(i) recovered at class level]: tetrahedron covers contain digons only ($84$ instances, $\delta h=2$ [D0.6]); cube covers contain digons and directed $4$-cycles ($14\,832$ instances, $\delta h\in\{2,4\}$), with $10$ distinct cycle contents $\{(),(2),(2,2),(4),(2,2,2),(2,4),(2,2,2,2),(2,2,4),(2,2,2,2,2),(2,2,2,2,2,2)\}$ and no odd cycle anywhere. The signature $(K,\text{cycles},|\mathcal C|)$ is **not a complete class invariant**: $7$ tetrahedron cover orbits carry only $6$ signatures, $264$ cube cover orbits only $21$ — the completing datum is the vertex-type multiset (clause (2)'s last column).
$(6)$ **Charge-conjugation chirality of the cover sector (new).** Global orientation reversal $R\mapsto R^{\mathrm T}=\{(b,a):(a,b)\in R\}$ is an involution of the pattern space that is **not** in $\operatorname{Aut}(\Gamma)$ (it is induced by no vertex permutation). It pairs cover classes: the $48$ bypass dissolved-digon covers of FT.69(4) split into **two $\Omega=24$ orbits exchanged by reversal** (representatives with type multisets $(1,0),(1,1)^2,(1,2)$ and $(0,1),(1,1)^2,(2,1)$ — transposes of each other; machine: the reversal of one representative is canonical in the other orbit). This is the pattern-level form of charge conjugation [D2.6]. **Both mass ansätze are reversal-invariant** ($K$, $\Omega$ and $4^{|\mathcal C|}$ are), so the chirality is invisible to the mass spectrum; reading it requires a C-odd ledger of FT.40's $q_{\mathrm{core}}$ species.

### FT.79 — The combinatorial ceiling and the cover-hierarchy audit (second clean negative)

**Thm.** Under Def-H.28; the SM hierarchies of clause (4) are **external measured data**, marked, entering no derivation and no identification (A §0.2; Open Gaps 5/12).
$(1)$ **Ansatz A spectrum (exact).** Cover masses are $m_A=2|\mathcal C|\ln2/\mathfrak h$ [FT.67(2): $|R|=2|\mathcal C|$ on covers], so the nonzero values are the even ladder $K\in\{2,4,6\}$ (tetrahedron) and $\{2,4,6,8,10,12\}$ (cube); pooled, $6$ distinct masses with exactly $11$ pairwise ratios
$$
\Bigl\{\tfrac65,\tfrac54,\tfrac43,\tfrac32,\tfrac53,2,\tfrac52,3,4,5,6\Bigr\}\subset\mathbb Q,
$$
lightest $2\ln2/\mathfrak h$, heaviest $12\ln2/\mathfrak h$, median $7$ (of the distinct values) / $8$ (orbit-weighted on the cube). Every ratio is a quotient of integers $\le6$.
$(2)$ **The ceiling theorem.** For any cover on any skeleton $\Gamma$: $K=2|\mathcal C|$ [FT.67(2)]; admissibility gives $\sum_vk_v=2K\le3V$ [CT0.11], so
$$
|\mathcal C|\le\tfrac{3V}{4}\ (\text{bypass}),\qquad |\mathcal C|\le V\ (\text{locked, centres are distinct vertices}),
$$
and the widest Ansatz-A mass ratio available on $\Gamma$ is $\le3V/4$ (bypass) or $\le V$ (locked). Spanning $1{:}R$ therefore **requires** $V\ge4R/3$ (bypass) or $V\ge R$ (locked):
$$
\begin{array}{c|cccccc}
R & 20 & 207 & 600 & 900 & 3477 & 80000\\
\hline
V\ge\ (4R/3) & 27 & 276 & 800 & 1200 & 4636 & 106667
\end{array}
$$
against $V=4$ (tetrahedron, max ratio $3$) and $V=8$ (cube, max ratio $6$). The cover sector's dynamic range is bounded by **skeleton size**, exactly as the pole sector's was bounded by the defect angle [FT.76(3)] — and both bounds evaluate to $\approx6$ on the computed cells.
$(3)$ **Ansatz B: no $\alpha$-free hierarchy.** The classes are the $(K,a,b)$ triples with $\ln\Omega=a\ln2+b\ln3$: $18$ on the tetrahedron's bypass sector — $19$ including its two locked cover classes, the extra one being $(K,a,b)=(6,2,0)$ — with $K\le6$, $a\le3$, $b\le1$, and $14$ on the cube's cover sector with $K\le12$, $a\le4$, $b\le1$, so $m_B/\!(\ln2/\mathfrak h)=K-\alpha(a\ln2+b\ln3)$ lies between $K-\alpha\ln|\operatorname{Aut}|$ and $K$. A ratio exceeding (2)'s bound can arise only where some class's mass passes through zero, i.e. at the tuned values $\alpha=K/(a\ln2+b\ln3)$ — a finite set, one per class, at each of which the ratio is *infinite* rather than $207$. **The signature structure does not supply the $\ge3$ orders of magnitude required by Gap 7's residue**: the informational datum is capped by $3V/2$ and the entropic one by $\ln|\operatorname{Aut}|\le\ln48$; what the signature supplies is degeneracy, not range.
$(4)$ **The audit (external data: charged leptons $1{:}207{:}3477$; up-type $1{:}600{:}80000$; down-type $1{:}20{:}900$).** Pool $=\{2,4,6,8,10,12\}$ (all cover masses of both skeletons, both sectors):
- pairwise, the closest cover ratio to each SM ratio is always the pool maximum $6$, giving discrepancies $\times2.7995$ (vs $m_\tau/m_\mu=16.797$), $\times3.333$ (vs $20$), $\times7.5$ (vs $45$), $\times22.22$ (vs $133.3$), $\times34.5$ (vs $207$), $\times100$ (vs $600$), $\times150$ (vs $900$), $\times579.5$ (vs $3477$), $\times13333.3$ (vs $80000$). The best, $\times2.7995$, is within an order of magnitude and is structurally void: it pairs our maximum with their minimum and extends to no triple.
- aligned triples, exhaustive: the best is $(2,4,12)\mapsto1{:}2{:}6$ against every family, with discrepancy $\times150$ (down-type), $\times579.5$ (leptons), $\times13333.3$ (up-type). **No aligned triple is within a factor of $10$**, and the floor is exact: $900/6=150$.
$(5)$ **Dimension trap #2, disclosed and rejected.** The amplitudes $4^{|\mathcal C|}\in\{1,4,16,64,256,1024,4096\}$ *do* span $3.6$ orders, and produce the only near-coincidences in the whole audit: $256$ vs $207$ ($\times1.2367$), $4096$ vs $3477$ ($\times1.1780$), $16$ vs $16.797$ ($\times1.0498$), $1024$ vs $900$ ($\times1.1378$), $64$ vs $45$ ($\times1.4222$). All are rejected: $4^{|\mathcal C|}$ is the $Z$-weight of FT.67(2), not a mass; no corpus tag maps an amplitude to a mass, Def-H.37(2)/Def-H.38 declare no such read, and the square-root-corrected values ($16,64,4,32,8$) miss by $\times4.2$–$\times54$. Same species as the $m^2$-vs-$m$ trap [FT.77(3)] — recorded because it is exactly what a forced fit would seize on.
$(6)$ **Verdict.** The cover hypothesis fails at the mass layer, for a structural reason dual to FT.77's and with no parameter fitted: the observable-sector masses are the even ladder $2|\mathcal C|\ln2/\mathfrak h$ capped by the cap census, so the reachable ratio range is $\le\max(3V/4,V)$ — six on the cube, three on the tetrahedron, against SM spans of $20$–$80000$. The messiness is genuine but sits in the degeneracies ($\Omega$ up to $48$; $264$ cube cover classes; $21$ signatures; chirality pairs), and degeneracy carries no hierarchy. **Neither the roof nor the fuzz yields the SM spectrum on the computed skeletons**; both sectors point to the same requirement — a much larger subnetwork ($V\ge1200$ for the down-type family alone) or a mass read of a different species.

### FT.80 — The bridge census: covers are amplitude-real, norm-real, and spectrally un-indexed

**Thm.** Under Def-H.16/Def-H.28, at (S1)–(S4):
$(1)$ **What a cover class supplies, exactly.** For every class $\mathcal O$: the real-edge set and $K$; $|\mathcal C|$ open V-threads (each centre pairs one in-edge with one out-edge [FT.67(3d)]) $=$ transit content, bosonic-side by D1.5; the dissolved even closed chains with their exact $\delta h$ [D0.6: $\delta h=\#\{e\in\gamma\}$] $=2$ (tetrahedron) and $\in\{2,4\}$ (cube); the aspect mask $\mathcal A(\max_vk_v)$ and observable mask dimension $\in\{6,16,17,25\}$ [CT0.13, CT0.14]; the amplitude $4^{|\mathcal C|}\ne0$ [FT.67(2)]; and the CT2.8 norm weight $\Omega\cdot2^{K}$ (the class's $(R,\sigma)$ count, cancellation-blind).
$(2)$ **What it does not supply.** Def-H.16's resolvent $Z(\mathcal R,\Sigma)=\langle\mathrm{out}|(1-\mathbf F_M^{(\Sigma)})^{-1}|\mathrm{in}\rangle$ with pole $\iff1\in\operatorname{spec}\mathbf F_M^{(\Sigma)}$ takes as arguments a **subnetwork $\Sigma$ with an observer channel $C$** (Def-H.1/Def-H.13, Def-H.16), the **colour data** that $\Pi_{\mathcal C}$ requires (FT.19/FT.27 — not determined by a crystallization pattern), and a **materialization** clause for whatever bound chains are to contribute poles (Def-H.16's own iff; M1/M2 species). None of the three is a function of $R$: no rule of Parts 1–3 maps a crystallization pattern to a $(\Sigma,C)$ pair with colour assignment.
$(3)$ **Census (machine, every class).** Tetrahedron $7/7$ and cube $264/264$ cover classes have: transit content $|\mathcal C|\cdot\Omega$ threads ($180$ and $40\,200$ thread instances); bound-chain candidates exactly the even cycles ($84$ and $14\,832$ instances; every $\delta h\ge2$, satisfying Def-H.4's floor, at rung $n(v)=6\ge2$); amplitude nonzero; norm weight nonzero; and **zero spectral poles constructible within the declared inventory**. Covers are therefore neither amplitude ghosts nor poles: they are amplitude-real and norm-real, spectrally *un-indexed*.
$(4)$ **The exact resolvent condition a declaration would have to supply** (recorded, **not** adopted). Item 13's exit (b) is constructible only as a triple of declarations: (i) a rule $\mathcal O\mapsto(\Sigma(\mathcal O),C(\mathcal O))$; (ii) colour data making $\Pi_{\mathcal C}(\Sigma;C)$ computable, hence $F^{\Sigma}_{\mathrm{strong}}$ and the mask $\mathbf F_M^{(\Sigma)}$ [FT.19, FT.26]; (iii) a materialization clause for dissolved cycles (M2-species), after which the pole condition is exactly $1\in\operatorname{spec}\mathbf F_M^{(\Sigma(\mathcal O))}$ with FT.22's single-valuedness on each materialized chain. This is a interface-definition species extension of Def-H.16; it is enumerated here and **not** introduced.
$(5)$ **Content bifurcation (the $\delta h/\delta\tau$ question).** The split is structural and exact, but it is a *content-type* split, not a statistics theorem: every cover decomposes as $|\mathcal C|$ transit threads (D1.5: bosonic content) plus dissolved even closed chains (D1.5: fermionic content *if materialized*; Def-H.4's termini are then candidate fermion loci, their $\delta h\ge2$ and rung $\ge2$ floors both satisfied). $\delta h$ is exact per chain ($2$ or $4$); $\delta\tau$ is a **schedule** datum (D0.7: retained ledger updates) that $R$ does not determine — Cal-F declares the flicker *rates* $r=\Gamma_{J^+}/\Gamma_{J^-}$, not per-tick schedules — so the "finite $\delta h$ with $\delta\tau=0$ persistence" test is not evaluable from a pattern alone. The corpus contains no exchange operator and no permutation representation of particle interchange, so **the spin–statistics connection remains an external reading**; what is derived here is the bound/transit content split per class, and the FT.1/FT.38 flux bound $I\le\min(\delta h/\mathfrak h,4\delta\tau)\ln2$ applies to it only once a schedule is declared.
$(6)$ **Consistency with the selection side.** Covers contain no *materialized* closed chain, hence carry no Bott datum [Def-H.24, FT.66(4)]; their content sits wholly in the transit sector, which is the one sector where index-$0$ stability exists on such slices [FT.48(3), FT.66(4b)] — FT.68(4)(d)'s verdict recovered at class level, and the reason the cover sector is where any future selection mechanism would have to act.

### Def-H.29 — Completeness-audit vocabulary: read classes, census statuses, the external-data clause

**Def.** A **read class** is a species of quantity the corpus can attach to a configuration, chain or subnetwork:
**(R1) binary registration** — $\sigma_e\in\{\pm1\}$ [CT0.9, A7/A8], the end-charge $q_{\mathrm{EM}}(c)=\tfrac12(\sigma_{s(c)}-\sigma_{t(c)})\in\{-1,0,+1\}$ [D3.4, EM.9], the vertex phase-comparison $f_v$ and $(-1)^{\aleph_v}$ [D3.3, FT.67(1)], the edge weight $G(e)=\sigma_e e^{i\pi\kappa_e}$ [D3.5].
**(R2) integer winding and ledger** — $\widehat{ds}^{\,2}$, $\Theta(\gamma)$ [D1.6, D1.7], the on-shell quantum $\kappa_e\in\mathbb Z$ [FT.22], the winding $k$ and $\Theta_{\mathrm{int}}$ [FT.25(3), FT.34, FT.43], $\delta h$ [D0.6], the spin ladder $j=|k|/2$ on $\mathrm{Sym}^k$ carriers [CT0.7a, EW.32, FT.52, FT.55, FT.60, Def-H.38].
**(R3) singlet admissibility** — the sealing indicator $\mathcal C(\Sigma;C)\in\{0,1\}$ and its idempotent $\Pi_{\mathcal C}$ [Def-H.9, Def-H.10, FT.19, CT3.18, CT3.22], with the partition rule ($|\mathrm{Colour}(\Sigma)|$ into $2$s and $3$s) [FT.34(5), CT3.17].
Observability is decided per aspect by FT.20's criteria table and FT.26's mask ($\dim\mathcal K_\Sigma\le18$), not by block membership [CT0.12/CT0.13/CT0.14].

### Def-H.30 — The three shape states

**Def.** For a skeleton $\Gamma$ [Def-H.25] with potential degrees $n(v)$:
**(S0) VV / all-virtual.** $R=\varnothing$: every potential edge virtual, $n_{\mathcal R}=0$, every pair at $\rho_\circ=\tfrac14 I$ [A5, CT0.2]. The shape-derived vacuum.
**(S1) flicker / bypass.** $R\ne\varnothing$ admissible: $k_v\le3$ at every vertex [CT0.11], i.e. the bypass sector of Def-H.25, with its ensemble reads at $p$ [Def-H.26, Cal-F] and its cover sub-sector [FT.67(2)].
**(S2) $D^-$ trapped.** Some vertex locked ($k_v\ge4$), up to the fully crystallized floor $R=E_{\mathrm{dir}}(\Gamma)$: content absorbed at rate $\propto O(n)$ [CT4.1/D4.2], retained in $\mathfrak L$ and **not accessible** [D1.11/CT4.3], with no accessible pole [CT4.2].

### FT.85 — Vacuum census, baseline equality, and the constructible gravitational reads

**Thm.** Under Def-H.30:
$(1)$ **Vacuum census.** The corpus declares exactly three scalar extremes and proves there is no fourth: the **Janus vacuum** $n_{\mathcal R}=0$ with $(S_{\mathrm{raw}},S_{\mathfrak L})=(\ln4\ \text{per pair (max, argmax unique}=\tfrac14I),0)$ [CT0.2, CT4.7(1)]; **$D^+$** with $(0,0)$ — a *pure*, uniform, non-configuration-dependent scalar [CT4.7(2), D4.3], $w=-1$ [CT1.25]; **$D^-$ locked** with $(\min_{\mathrm{acc}},\max\wedge\neg\text{accessible})$ [CT4.7(3), D1.11, CT4.2, CT4.3]; and $\neg\exists$ a fourth extreme [CT4.10], $F_H$ being a dynamical field [EW.27].
$(2)$ **Baseline equality (proven, not measured).** For every shape $S$: $S_{\mathfrak L}(\mathrm{VV}(S))=n_{\mathcal R}\ln2=0=S_{\mathfrak L}(V_{\mathrm{raw}})$ [CT1.29]; $\Delta S_{\mathrm{raw}}=0$ on both sides [CT0.2: every pair at the argmax]; $m_{\mathrm{hid}}=S_{\mathfrak L}/\mathfrak h=0$ [FT.44(4)]; $\rho_{D^-}=0$ [CT4.5's iff]; and CT1.29's $S_{\partial\mathcal B}$ has no argument (no closed real-edge surface). Hence
$$
m_g^2\bigl(\mathrm{VV}(S)\bigr)=m_g^2\bigl(V_{\mathrm{raw}}\bigr)\quad\forall S,
$$
on every constructible read, and $\Delta S_{\text{vacuum polarization}}(S)\equiv0$. The reason is registration, not arithmetic: virtual pairs carry **no registration** [A7/D0.5: $\phi_e$ is defined on $e\in E_{\mathcal R}$; A5: the sole ledger exclusion is the Haar draw; Def-H.25(S4): virtual edges weight $1$, no phase]. Honest remark: the *absolute* raw entropy is $|\mathrm{pairs}|\cdot\ln4$ and is shape-dependent; the *deficit* is shape-independent and zero. The raw vacuum's mass reads vanish from three independent derived reads — nothing is set to zero by hand.
$(3)$ **$m_g^2:=\Delta S$ is not constructible.** (a) The inventory contains no inertial/gravitational mass distinction and no equivalence theorem (`inertial`, `Lyapunov`, `maximal mixing`, `equivalence principle`, `Theorem 11`: count $0$ in Parts 1–2); (b) $\Delta S_{\mathrm{raw}}$ of a *registered* configuration is bounded but undetermined — A4/D0.4 force a real pair strictly below $\ln4$ and no tag declares its $\rho$, so $\Delta S_{\mathrm{raw}}\in(0,n_{\mathcal R}\ln4]$ with no value; (c) the dimensionally correct entropy-based mass$^2$ *density* is $S/A=\ln2/\mathfrak h^2$ [CT1.29/CT2.9], a **state-independent constant** [FT.37: corrected by $1/\bar\kappa$], so state-dependence can enter only through $A$ or $\bar\kappa$.
$(4)$ **The constructible reads, used for every table below.** (i) $m_{\mathrm{hid}}=S_{\mathfrak L}/\mathfrak h=E_{\mathrm{int}}\ln2/\mathfrak h$ — the universal taxonomy law [FT.44(4)] — with $m_{\mathrm{hid}}^2=E_{\mathrm{int}}^2(\ln2)^2/\mathfrak h^2$, dimension $\mathfrak q$ [D2.9/CT2.1]; (ii) the locked sector's stress-energy $T^{(D^-)}_{\mu\nu}=\rho_{D^-}u_\mu u_\nu$, $p=0$, $w=0$, $\rho_{D^-}=\sum_{v\ \mathrm{locked}}O(n_v)\ge0$ [CT4.1/CT4.5] — the corpus's one derived gravitational source; (iii) $S_{\partial\mathcal B}=A\ln2/\mathfrak h^2=A/(4G_N)$ with $A=n_{\mathcal R}(\partial\mathcal B)\mathfrak h^2$ and $G_N=\mathfrak h^2/(4\ln2)$, $\kappa^2=8\pi G_N$ **derived** [CT1.29/CT2.9/P3], bounded by CT4.9 ($\le3$ bits per accessible vertex; $S_{\mathrm{acc}}(\mathcal B)\le A/\mathfrak h^2$ bits); (iv) the pole side $m^2_{\mathrm{pole}}=4\hat\mu'^2\sin^2(\Theta_R/4)$ under Def-H.37(2) [FT.54/FT.76] — which is also what a two-patch field-source read reduces to on the cone metric [Def-H.21/FT.47], i.e. clause (iii) of the audit's B3 is already bounded [FT.76(3)].
$(5)$ **The source criterion, exact.** $\rho_{D^-}>0\iff\exists v:\ k_v\ge4$ [CT4.5's iff] — machine-exhaustive over the tetrahedron's $4096$ and $P_4$'s $256$ patterns. Consequences: **every S1 configuration has exactly zero dark-dust stress-energy**, and only S2 states are dust sources; those are retained-but-inaccessible [CT4.2/CT4.3/D1.11], amplitude-zero in the literal domain [FT.67(3a)] and revived only in the chain-local domains [FT.75(2)]. So the flicker gas does not gravitate through $D^-$ at all; its only mass read is informational.
$(6)$ **The state table** ($14$ shapes; $\langle K\rangle$ at $p=\tfrac12$ reproduces FT.70(5)/FT.68(1) verbatim):
$$
\begin{array}{c|ccc|ccc}
& \multicolumn3{c|}{m_{\mathrm{hid}}\,\mathfrak h/\ln2} & \multicolumn3{c}{\rho_{D^-}}\\
\text{shape} & \text{S0} & \text{S1}\ \langle K\rangle(\tfrac12) & \text{S2}\ E_{\mathrm{int}} & \text{S0} & \text{S1} & \text{S2}\\
\hline
\text{digon} & 0 & 1 & 2 & 0 & 0 & 0\ (n(v)=2\ \text{never locks})\\
P_3..P_{10} & 0 & \tfrac83,\tfrac{248}{69},\tfrac{130}{29},\tfrac{296}{55},\tfrac{2618}{417},\tfrac{11344}{1581},\tfrac{896}{111},\tfrac{13588}{1515} & 2n & 0 & 0 & 16n\\
\text{tetra} & 0 & \tfrac{852}{205} & 12 & 0 & 0 & 448\\
\text{cube} & 0 & \tfrac{3311952}{395023} & 24 & 0 & 0 & 896\\
\text{octa} & 0 & \tfrac{2124600}{318523} & 24 & 0 & 0 & 2976\\
\text{dodeca} & 0 & \tfrac{4007491093935690}{191727103387307} & 60 & 0 & 0 & 2240\\
\text{icosa} & 0 & \tfrac{215801166207}{15519497071} & 60 & 0 & 0 & 24384
\end{array}
$$
with $S_{\mathfrak L}=(\text{that row})\cdot\ln2$, $A/\mathfrak h^2=E_{\mathrm{int}}$ in S2, and per-sector entropies **not available** (clause (7)).
$(7)$ **No per-sector $\Delta S_A$.** Four cited reasons: no declared state $\Psi_X$ for a crystallization pattern, so $\|F_A\Psi_X\|^2$ has no argument; FT.30's audit leaves only the $G$ block with a geometric read and marks it **joint** ($\neg$ per-block); $H$, $J^\pm$, $D^+$ are explicitly not independent quanta [FT.30]; CT0.14/FT.26 supply block *dimensions* $(6,16,17,25)$ and the $\le18$ observable bound, which is all the sector map can carry. The only declared per-register decomposition is $S_{\mathfrak L}=K\ln2=\sum_{e\in R}\ln2$ [CT0.9: one real edge $=$ one bit] — machine-verified per configuration.

### FT.86 — The flicker ripple: ultralocal raw dynamics, cap-induced alternation, and the quantum–classical gradient

**Thm.** Under Def-H.26/Def-H.30 at $p=\tfrac12$ (every value exact; general $p$ by the same census):
$(1)$ **The raw flicker has no spatial ripple.** $\mu_p$ is a Bernoulli **product** measure on directed edges [Def-H.26], so every connected edge–edge correlation vanishes identically: $\langle x_ex_{e'}\rangle=p^2=\langle x_e\rangle\langle x_{e'}\rangle$ for $e\ne e'$ (machine-exhaustive on $P_3$, $P_4$). Any waviness in the flicker geometry is **constraint-induced**, not dynamical.
$(2)$ **The admissible flicker carries an exact period-2 alternating ripple.** Conditioning on admissibility ($k_v\le3$, CT0.11) couples neighbours; the connected correlations, by *true ring distance* (the two directions of one undirected edge are distance $0$ — a digon — not distance $1$), are exact rationals alternating in sign:
$$
\begin{array}{c|cccccc}
& d=0 & d=1 & d=2 & d=3 & d=4 & d=5\\
\hline
P_4 & -\tfrac{133}{4761} & -\tfrac{64}{4761} & +\tfrac{28}{4761} & & & \\
P_8 & -\tfrac{71068}{2499561} & -\tfrac{33124}{2499561} & +\tfrac{6928}{2499561} & -\tfrac{1504}{2499561} & +\tfrac{604}{2499561} & \\
P_{10} & -\tfrac{1631509}{57380625} & -\tfrac{760384}{57380625} & +\tfrac{158716}{57380625} & -\tfrac{33184}{57380625} & +\tfrac{7216}{57380625} & -\tfrac{2884}{57380625}
\end{array}
$$
Short-distance values converge to $L$-independent limits ($d{=}0\to-0.0284331$, $d{=}1\to-0.0132516$): the cap makes neighbouring crystallizations anticorrelate and next-nearest correlate.
$(3)$ **The decay rate is the corpus's own transfer matrix.** With $\operatorname{charpoly}T(1)=x^2-3x-3$ [FT.68(2)/FT.70(3)], $\lambda_{1,2}=(3\pm\sqrt{21})/2$ and
$$
\frac{\lambda_2}{\lambda_1}=\frac{\sqrt{21}-5}{2}=-0.2087122\ldots\in\mathbb Q(\sqrt{21}),\qquad \xi=-1/\ln|\lambda_2/\lambda_1|=0.6382\ \text{directed edges},
$$
matching the measured ratios $C(2)/C(1)=-\tfrac{39679}{190096}=-0.2087314$ ($P_{10}$, **4 significant figures**) and $C(3)/C(2)=-\tfrac{8296}{39679}=-0.2090779$ (3 s.f.); $P_9$ gives $-\tfrac{2759}{13225}=-0.208620$. The **negative sign of $\lambda_2/\lambda_1$ is the alternation**. Deviations grow near the antipode ($d\approx L/2$) as finite-size wrap.
$(4)$ **Exact moments from the cap census** (never a Bernoulli proxy): $\langle K\rangle$, $\langle K^2\rangle$, $\sigma_K^2$ for all $14$ shapes, with $\sigma_K^2/\sigma_{K,\mathrm{ind}}^2$ (the **cap factor**, $\sigma^2_{\mathrm{ind}}=2Ep(1-p)=E/2$) equal to $1$ for the digon (the cap never binds at $n(v)=2$), $\to0.7002$ for large polygons, and $0.155$–$0.373$ for the solids (icosa $0.1547$, octa $0.2228$). Anchors: digon $\langle K\rangle=1,\langle K^2\rangle=\tfrac32,\sigma^2=\tfrac12$; $P_3$: $\tfrac83,\tfrac{73}9,1$.
$(5)$ **The ripple in the mass reads.** $\Delta S=S_{\mathfrak L}=K\ln2\Rightarrow\delta(\Delta S)=\sigma_K\ln2$ exactly; $\delta(m_{\mathrm{hid}})/m_{\mathrm{hid}}=\sigma_K/\langle K\rangle$ and $\delta(m_{\mathrm{hid}}^2)/m_{\mathrm{hid}}^2=2\sigma_K/\langle K\rangle$ (the factor $2$ exact). The raw-vacuum and VV baselines give **identical** $\delta(m_g^2)$ — by FT.85(2)'s proof, not by numerical agreement.
$(6)$ **Quantum–classical gradient.** $\sigma_K/\langle K\rangle$ decreases monotonically from the digon's $1/\sqrt2=0.707107$ (exact) through $P_3$'s $3/8=0.375$ (exact) to the icosahedron's $0.10955$; the $1/\sqrt{\langle K\rangle}$ law holds with a **family-dependent coefficient** $\sigma_K/\sqrt{\langle K\rangle}$: $1/\sqrt2$ (digon), $0.6124$ ($P_3$), $0.6248$ converged ($P_4$–$P_{10}$), $0.41$–$0.52$ (solids) — the deviation from the binomial $1/\sqrt2$ being exactly the cap factor. **Near-pure-wave limit:** $\sigma_K/\langle K\rangle=1$ requires a *single* directed edge at $p=\tfrac12$ — amplitude-zero [FT.67(3b): $\operatorname{cov}=0$], hence not a bound shape. No shape in the inventory is near-pure-wave.
$(7)$ **No frequency is constructible; one period is derived.** the Cal-F rate datum is the ratio $r=\Gamma_{J^+}/\Gamma_{J^-}$ and per-edge detailed balance, and records that the corpus supplies no $J^\pm$ *rates*, so $f_{\mathrm{ripple}}=\Gamma_{\mathrm{tot}}/2\pi$, $\tau_c=1/\Gamma_{\mathrm{tot}}$ are reported **in units of the undeclared total rate** and no absolute frequency is claimed. Rate-free and derived: one $J^\pm$ event changes $(n_{\mathcal R},\delta h,\delta\tau)$ by $(\pm1,\pm1,\pm1)$ [CT0.3], so **in ledger-tick units $\tau_c=1$ tick** and the Lorentzian half-width is $1$ rad/tick; propagation obeys $\delta\tau\ge\delta h/4$ (at most $4$ hops/tick) [FT.1/FT.38, CT0.6, EM.5–7]. Leading order (single-flip granularity) the cap correlation renormalizes the Lorentzian **amplitude** by the cap factor and leaves the **width** at $\Gamma_{\mathrm{tot}}$; the full constrained spectrum is multi-timescale and not constructible without rates.
$(8)$ **Self-modulation is not constructible.** A tick-rate/field coupling $r_q(g_q)$ has no referent: `clock`, `dilation`, `tick rate`, `r_q`, `g_q`, `local rate`, `running coupling`, `beta function` all count $0$ in Parts 1–2. The corpus has the conformal factor $\Omega=e^{\alpha_\Omega a_{00}}$ and the shift $N_i=\beta w_i$ [CT1.12], and $\delta\tau$ is defined as retained ledger updates along real edges [D0.7], but nothing couples the two. Logged as a gap (a new interface-definition species), not adopted.
$(9)$ **The trapped sector does not ripple.** CT4.5's own Pf: locked $\Rightarrow$ no accessible pole [CT4.2] $\Rightarrow$ no propagating mode $\Rightarrow\mathsf E_{\mathrm{tr}}=0\Rightarrow T^{\mathrm{tr}}=0$ — S2 states are **non-oscillatory by theorem** (pure dust, $p=0$, $w=0$).

### FT.87 — The tumbling-model adjudication (external proposal, row by row)

**Thm.** **External-data and status clause.** The proposal adjudicated here ("tumbling/rotor masses, Regge trajectories, shell magic numbers, weak $\pm2$ parity shift, cover class $=$ generation, $\ln Z$ as Yukawa, calibration from a measured lepton mass") is *external*; its SM comparisons are marked [EXT]; nothing below is adopted, and no particle is identified. Verdicts:
$(1)$ **The rotor term is not new physics — it is Def-H.37(2) leading order.** $4\sin^2(m\Theta_R/4)=\tfrac{m^2\Theta_R^2}{4}\bigl(1-\tfrac{x^2}{3}+\tfrac{2x^4}{45}+\cdots\bigr)$, $x=m\Theta_R/4$ (both Taylor coefficients machine-exact in $\mathbb Q$), so the proposed slope $1/R^2$ **is** the declared coefficient $\hat\mu'^2\Theta_R^2/4$ [FT.54/FT.60(5), EW.33 recovered as its Taylor term]. Consequences: the rotor inherits Def-H.37(2)s conditional status, and it inherits **FT.76(3)'s ceiling** — the sine saturates at $4$, so no winding ladder of this species can grow without bound.
$(2)$ **Two dimension traps (flagged, as the proposal's own rules require).** (a) $m^2=m^2_{\mathrm{static}}+\hbar^2k^2/(2I)$ adds an *energy* ($\mathfrak q^{1/2}$) to a *mass squared* ($\mathfrak q$); (b) $k^2/R^2$ with $R$ an edge count is $\mathfrak q^0$, not $\mathfrak q$ — repaired only as $k^2/(R^2\mathfrak h^2)$; (c) $I=\Delta S\cdot R^2$ has dimension $\mathfrak q^{-1}$ where a moment of inertia is $\mathfrak q^{-1/2}$. Same species as FT.77's $m^2$-vs-$m$ and FT.79's amplitude-vs-mass traps.
$(3)$ **"Regge verified linear for all 12 shapes" is a tautology.** $m^2=m^2_{\mathrm{static}}+(4/R^2)j^2$ with $j=|k|/2$ is linear in $j^2$ *by algebra*, so the check cannot fail. The derived read is **not** linear in $j^2$: its successive slopes in $j^2$ vary (cube $1.4142,0,-0.4714$; octa $1.5,-0.75,0$; dodeca $0.3633,0.2939,0.1959$; icosa $0.8660,0.4330,0$), and the tetrahedron's ladder is **exactly flat** ($4\sin^2(m\pi/4)=2$ for every odd $m$ [FT.76(5a)]).
$(4)$ **The quadratic form is a poor approximation where it is used.** At the documented uniform-minimal windings the exact-to-quadratic ratio is $0.8106$ (cube, dodeca, icosa: $18.9\%$ error), $0.4053$ (octa: $59.5\%$), $0.0901$ (tetra: $91.0\%$); the exact values reproduce FT.76(2)'s top weights $(2,2,4,2,2)$ — an independent cross-check of both sides.
$(5)$ **Shell "magic numbers" collide with a proven no-go.** Extra-stable rotational levels would require a weight-level selection criterion, and FT.66(4)'s dilemma plus FT.61/FT.66(2)'s blindness theorems prove that **no weight/ledger criterion can select** among equal-record stationary variants on the Platonic curvature class; nuclear magic numbers are external data with no corpus referent. The proposal's stability islands are not constructible.
$(6)$ **The moment-of-inertia table is exact but embedding-dependent.** $I=KR^2$ reproduces $(0.8889,2.0000,\text{ratio }2.25)$, $(1.5585,4.5000,2.8873)$, $(6.2882,18.0000,2.8625)$ for $R^2=(\tfrac13,\tfrac38,\tfrac34)$ (machine). The **ratios are embedding-free** — $R^2$ cancels and the ratio equals $E_{\mathrm{int}}/\langle K\rangle$, FT.87's own within-shape state ratio — but $I$ itself needs a Euclidean circumradius, an *embedding* datum the corpus does not supply (Def-H.21/FT.47/FT.54 give an intrinsic piecewise-flat cone metric; `circumradius` counts $0$). The "cold dark matter" conclusion is already derived without it ($w=0$ dust [CT4.5]; $T^{\mathrm{tr}}=0$; not accessible [D1.11/CT4.2/CT4.3]; FT.86(9)) and the cosmological name is inadmissible [FT.73(5), items 5/12].
$(7)$ **Composite tumbling: the spin side is derived, the mass side is not.** Winding additivity $k(\Gamma)=k_1+k_2+d_{12}$ [FT.34(3)], the cone's CG range $|k_1-k_2|\le k\le k_1+k_2$ [FT.52(3)] and maximal-weight composition [FT.60(6)] support the aligned/anti-aligned structure, and under Def-H.38 three seeds give $\mathrm{Sym}^3$ ($j=\tfrac32$) plus mixed-symmetry $j=\tfrac12$ — the proposal's "aligned $j=3/2$ / mixed $j=1/2$" pair **is** corpus-consistent. But the splitting $\Delta m^2=k^2/R^2$ is the undeclared rotor of (1)–(2); the ratio $(3^2-1^2)/(2^2-0^2)=2$ against [EXT] $\approx1.1$ is a factor $1.8$ discrepancy, not the "factor-of-2 match" claimed; and the state labels are identifications.
$(8)$ **The weak $\pm2$ shift.** No tag supplies $\varepsilon_W$, and "parity" collides with the corpus's $\mathbb Z_2$ *ledger* parity [FT.64's cut-space classes] — spacetime parity has no read (`left-handed`, $P_L$, $P_R$, $\gamma_5$: count $0$). What *is* legitimate: $\chi=\operatorname{sign}(k)$ is a **C-odd orientation read**, the coordinate that FT.78(6)'s chiral cover pairs lack — the missing ledger named there, of FT.40's $q_{\mathrm{core}}$ species. A $\chi$-dependent splitting would split those pairs; promoting it to a mass read needs a declared projector (Open item 20, deficit 1) and is not adopted.
$(9)$ **The Yukawa replacement is refuted, on its own numbers.** $4^{|\mathcal C|}$ for $|\mathcal C|=1,2,3$ is $(4,16,64)$, **not** the claimed $(8,1056,1109312)$; those are $(8,\ Z_{\mathrm{byp}}(\text{tetra})-1,\ Z_{\mathrm{byp}}(\text{cube})-1)=(8,1056,1109312)$ — total bypass amplitudes of **three different skeletons**, contradicting "the same topological core wrapped in 1, 2 or 3 layers" (and $8$ matches no cover-census value). $\ln Z$ spans $1:3.35:6.70$ against [EXT] $1:207:3477$ — short by $\times519$, so the "right order of magnitude" claim is refuted by the proposal's own arithmetic. $\ln Z$ is also **ill-defined** as an entropy: $Z$ is a signed sum $(-1)^{\sum\kappa}4^{|\mathcal C|}$ [FT.67(2)] vanishing on most patterns, while the corpus's ledger entropy is $S_{\mathfrak L}=n_{\mathcal R}\ln2$ [CT1.29]. Using $\ln Z$ as a mass is precisely the amplitude-to-mass smuggle the proposal's own rule 4 forbids [FT.79(5)].
$(10)$ **Foreign labels.** `Theorem 11`, `equivalence principle`, `N10`, `OP8`, `OP10`, `K-machine`, `moment of inertia`, `rigid rotor`, `Regge`, `tumbling`, `magic number`, `shell model`, `circumradius`: all count $0$ in Parts 1–2. Where such a label names something real, the real object is cited instead (OP10's involutions $\to$ FT.88; "mass lives in the trace" has no referent; the equivalence principle is FT.85(3)'s non-constructibility result).
$(11)$ **The calibration phase is refused.** Fixing $\mathfrak h$ from a measured lepton mass violates P1 (one free dimensionful scale, fixed once), P5 ($\neg\exists$ quantity identified with a measured external constant) and the proposal's own rule 3. Not executed.
$(12)$ **Verdict.** The tumbling model supplies **no mechanism that escapes the two ceilings**: its mass term is Def-H.37(2)s small-angle regime (bounded by FT.76(3)), its size datum is undeclared, its shell stability is excluded by FT.66(4), and its generation mechanism is an amplitude read the rules forbid. Open item 20's deficits 1 (chirality), 2 (Yukawa) and 3 (generations) are **not closed** by it; the genuinely new constructible content is FT.88's involution algebra and the C-odd orientation coordinate of clause (8).

### FT.88 — The involution algebra of the two declared reversals

**Thm.** Let $\omega$ [D2.6] and $\Theta_{\mathfrak L}$ [D2.7] be the corpus's two declared involutions.
$(1)$ **$\omega$ on patterns.** $\omega$ reverses orientation: $s(c)\leftrightarrow t(c)$, charge $\mapsto-$charge, chirality $\mapsto-$chirality [D2.6]. On a skeleton it acts as $R\mapsto R^{\mathrm T}=\{(b,a):(a,b)\in R\}$, with $\omega^2=1$ (machine: on all patterns sampled and on the tetrahedron's full orbit set), and $\omega\notin\operatorname{Aut}(\Gamma)$ — no vertex permutation induces it [FT.78(6)], where it was shown to exchange the two $\Omega=24$ dissolved-digon cover classes.
$(2)$ **$\Theta_{\mathfrak L}$ on registrations.** $\Theta_{\mathfrak L}$ reverses ledger order with $J^+\leftrightarrow J^-$ and $G(e)\mapsto G(e)^\ast$ [D2.7], i.e. $\sigma_e$ fixed and $\kappa_e\mapsto-\kappa_e$ on the edge weight $G(e)=\sigma_e e^{i\pi\kappa_e}$ [D3.5]; $\mathcal J(C)\mapsto\mathcal J(C)^\ast$ [D3.6].
$(3)$ **The algebra.** $\omega$ acts on the *edge set* and $\Theta_{\mathfrak L}$ on the *phase/ledger order*: disjoint data, hence they commute, and
$$
\langle\omega,\Theta_{\mathfrak L}\rangle\cong\mathbb Z_2\times\mathbb Z_2
$$
on skeleton registration data, with the four classes $(1,\ \omega,\ \Theta_{\mathfrak L},\ \omega\Theta_{\mathfrak L})$. $\omega$ is charge-odd [D2.6; FT.40's $\omega$-covariance of $q_{\mathrm{core}}$]; $\Theta_{\mathfrak L}$ is charge-even and phase-odd.
$(4)$ **Scope, and what this is not.** The inventory contains no C, P or T *operator*, no Lorentzian field algebra and no spinor bundle, so no CPT theorem is claimed or claimable; $\mathbb Z_2\times\mathbb Z_2$ is the exact group generated by the two declared reversals and nothing more. In particular $\omega$ is **not** a chirality projector: it is an orientation reversal whose fixed-point set is empty on chiral pairs [FT.78(6)], whereas a projector needs an eigenspace decomposition of a *state* space that the corpus does not supply for patterns (Open item 20, deficit 1). The proposal's $\chi=\operatorname{sign}(k)$ is the $\omega$-odd coordinate of $(3)$: a legitimate C-odd ledger read, still not a projector.

### FT.81 — Particle-content census (audit pass A)

**Thm.** Under Def-H.29, with the SM field content external and marked:
$(1)$ **The census.** $24$ entries, classified with their supplying tags or no-goes:
$$
\begin{array}{lll}
\textbf{PRESENT}\ (10) & \textbf{PARTIAL}\ (6) & \textbf{ABSENT}\ (8)\\
\hline
\text{gluons }(8) & \text{Higgs doublet} & \text{neutrino}\\
W^\pm & \text{quark triplet} & \text{generations/flavour}\\
Z\ (\text{mixture}) & \text{lepton doublet} & \text{CKM/PMNS, CP phase}\\
\text{photon} & \text{charged-lepton singlet} & \text{Yukawa sector}\\
\text{confinement/singlet} & \text{observable charge} & \text{chirality/Weyl}\\
\theta_W,\ e\ (\text{relations}) & \text{EW VEV} & \text{gauge anomalies}\\
G_N\ (\text{beyond SM}) & & \Lambda_{\mathrm{QCD}}\\
\text{spin ladder} & & \text{spin-statistics}\\
\text{fermion/boson content} & & \\
D^\pm\ \text{dark (beyond SM)} & &
\end{array}
$$

### FT.89 — The Koide/phase-boundary adjudication: exact arithmetic, category trap

**Thm.** Under Def-H.26/FT.70, with the Koide constant external and marked:
$(1)$ **The arithmetic is exact and re-verified.** $p^*_\Gamma$ is the unique root of $B_\Gamma(p)=p^{2E}$ in $(0,1)$ [FT.70(1)]; rational bisection of width $2^{-44}$ reproduces all eight documented polygon values ($0.807901$, $0.819671$, $0.815219$, $0.817028$, $0.816269$, $0.816596$, $0.816452$, $0.816517$ for $n=3..10$); $(p^*_n)^2$ **interlaces** $\tfrac23$ (odd $n$ below, even above) with deviations $1.40\times10^{-2},\ 2.09\times10^{-3},\ 3.72\times10^{-4},\ 7.23\times10^{-5}$ at $n=3,5,7,9$; and in $\mathbb Z[\sqrt6]$
$$
s=2+\sqrt6:\ s^2-4s-2=0\ \checkmark;\qquad p^*_\infty=\frac{s}{1+s}=\frac{(2+\sqrt6)(3-\sqrt6)}{(3+\sqrt6)(3-\sqrt6)}=\frac{\sqrt6}{3}\ \checkmark;\qquad (p^*_\infty)^2=\frac{6}{9}=\frac23\ \textbf{exactly}.
$$
So the observation's arithmetic premise is **true and exact**, not approximate.
$(2)$ **Category verdict: TRAP, on four independent grounds.**
**(a) Kind mismatch.** $p^*_\infty$ is a *probability* — the crossing point of the flicker ensemble's bypass measure with its floor measure [Def-H.26, FT.70(1)], conditional on the Cal-F rate datum's equilibrium reading. $Q$ [EXT] is a *mass-ratio functional* of three charged-lepton masses. Both are dimensionless; dimensionless is not a kind — P2/P5 keep derived dimensionless numbers, free configuration parameters and measured constants strictly separate.
**(b) No referent.** The corpus has **no lepton mass read at all**: no Yukawa sector, no lepton species, no flavour index [FT.81(5); item 20's deficits 1–3]. $Q$ therefore cannot be formed inside the corpus, and no map connects the two sides.
**(c) Precedent.** FT.73(5) already adjudicated this exact species — $\alpha_{\mathrm{EM}}=\pi$, a derived pure number and a *phase coefficient* [EM.20], against $1/137$, a *coupling* — and ruled the comparison inadmissible. The ruling transfers verbatim: a derived dimensionless corpus number is not comparable to a measured dimensionless ratio without a declared map.
**(d) Cap contingency (new, machine).** $\tfrac23$ is **not universal — it is the cap-3 value**. Repeating the identical construction with cap $c=2$ gives $(p^*_\infty)^2\to0.508004\ldots$ ($P_6,P_8,P_{10}$: $0.508193$, $0.508021$, $0.508004$), and with $c=4$ every pattern is admissible so $B\equiv1$ and **no interior boundary exists** [FT.70(1)]. Hence $(p^*_\infty)^2=\tfrac23$ is a function of $C_{\mathrm{cap}}=16$ and $D_{\mathrm{tick}}(n)=2^{n+1}$ at $n=3$ [CT0.5, CT0.6, CT0.11] — a combinatorial output of the admissibility ceiling. Genericity: $\tfrac23$ is already a derived corpus value elsewhere ($\delta_v/\pi=\tfrac23$ for the octahedron [FT.63(4)]) and is the ratio of the two smallest integers $>1$.
$(3)$ **Sequence-to-generations: refuted.** $(p^*_n)^2$ approaches $\tfrac23$ with *shrinking*, alternating deviations; a generation hierarchy requires *growing* separation. Moreover $n$ is a polygon side count (not a generation index) and the family supplies $\ge8$ values, not $3$.
$(4)$ **The A3 sub-questions, answered negatively.** (a) The transfer matrix's characteristic polynomial $x^2(x^2-3x-3)$ [FT.68(2)] has roots $(3\pm\sqrt{21})/2$ — exactly **one positive** number, the other negative, plus a double zero — so it cannot supply a three-component mass vector. (b) The $45^\circ$ cone condition ($\cos45^\circ=1/\sqrt2$) and FT.86(6)'s single-edge relative ripple $\sigma_K/\langle K\rangle=1/\sqrt2$ are the same *number* of different kinds (a cone angle versus a binomial standard deviation at $p=\tfrac12$): flagged, not used.
$(5)$ **Verdict.** Coincidence; closed. The equality $(p^*_\infty)^2=\tfrac23$ stands as a derived exact fact about the cap-3 polygon ensemble; its identification with the Koide constant is inadmissible on grounds (a)–(d). No structural claim, no identification, nothing adopted.

### FT.90 — The resolution ladder: no-hair from the channel bound, and the chiral merger refuted

**Thm.** Under FT.3/FT.4/FT.15 with C10/CT0.6:
$(1)$ **The no-hair theorem is already proved, and it is stronger than a limit.** FT.4: $I_o(v)\le\min(\delta h(\gamma),4\delta\tau(\gamma))\ln2$, and this bound *is the entire externally available description* — $v,v'$ with the same $(\delta h,\delta\tau)$ are observationally identical. FT.3: for **every** $\Sigma''\in[\gamma]$, $I_{o\leftarrow\Sigma''}(\gamma)=I(\delta h(\gamma),\delta\tau(\gamma))$ exactly and totally, *including whether $\Sigma''$ contains $D^-$-configured nodes*. So the collapse of internal structure is not a large-$\delta h$ effect: it holds at every $\delta h$. **Correction to the submitted framing:** the budget *grows* with $\delta h$, so merging is tightest at *small* $\delta h$; what is $\delta h$-independent is the invisibility of the internals.
$(2)$ **The resolution ladder, exact.** With the saturating schedule $\delta\tau=\lceil\delta h/4\rceil$ (at most $4$ hops per tick [FT.1/FT.38, CT0.6, EM.5–7], attained by photon schedules [FT.36(2)]), the budget is $\min(\delta h,4\delta\tau)=\delta h$ bits, so
$$
|\mathrm{Res}(\delta h)|\le2^{\delta h}:\qquad\delta h=1,2,3,4,5\ \mapsto\ 2,4,8,16,32\ \text{alternatives},
$$
and at $\delta h=4$ the bit budget equals $C_{\mathrm{cap}}=16$ registers exactly [CT0.6]. C10's warning is load-bearing: the **register cost** of $|X|$ alternatives is $|X|$, their **Shannon content** $\log_2|X|$ — the two budgets are different quantities and must not be identified.
$(3)$ **Exact thresholds for the computed class counts.** The hop distance at which the budget first covers a class count:
$$
\begin{array}{c|cccccc}
\text{target} & \text{tetra configs} & \text{tetra classes} & \text{tetra covers} & \text{cube configs} & \text{cube classes} & \text{cube covers}\\
\hline
\# & 1230 & 70 & 7 & 1\,580\,092 & 33\,564 & 264\\
\min\delta h & 11 & 7 & 3 & 21 & 16 & 9
\end{array}
$$
with $P_8$'s $42\,687$ admissible configurations at $\delta h\ge16$. Merge factors at $\delta h=4$ (budget $16$): tetrahedron $1230/16=615/8$, cube $1\,580\,092/16=395\,023/4$.
$(4)$ **What survives at every resolution.** FT.15's invariant tuple $\Pi_v(C)=(q,S,m_{\mathrm{hid}})$ — invariance under internal rearrangement given a shared signature $(\delta h,\delta\tau,q,\Theta_{\mathrm{int}})$ — together with the aspect set $\mathcal A(\Sigma;C)$ and $\dim\mathcal K_\Sigma\le18$ [FT.20/FT.26]. Precisely: $\mathrm{Res}(\infty)$ does **not** equal the tuple because resolution is not the limit that removes the internals; FT.3 removes them at *every* resolution, and the ladder of (2) bounds how many *classes* a channel can separate.
$(5)$ **The chiral merger is NOT forced by FT.15.** Sign-dependence of the tuple, component by component: $S=j=|k|/2$ [FT.52/FT.55, FT.60] — **sign-blind**; $m_{\mathrm{hid}}=E_{\mathrm{int}}\ln2/\mathfrak h$ [FT.16/FT.44(4)] — **sign-blind**; $q=q_{\mathrm{core}}=\tfrac12(\sigma_{e_1}-\sigma_{e_k})\mapsto-q_{\mathrm{core}}$ under $\omega$ [FT.40, D2.6] — **sign-sensitive**. Moreover FT.15's *hypothesis* already requires equal $q$, so the theorem never merges states of differing $q$. Hence a Dirac-type merger of a chiral pair would require **declaring $q$ unobservable** (or a coarser invariant): a new declaration, not a consequence. This is the same C-odd coordinate identified in FT.78(6)/FT.87(8), and no projector exists to split or merge on it [FT.84(1) deficit 1; FT.87(8)].
$(6)$ **The "information cost of generations" question: premise void, legitimate version exact.** The submitted $(8,1056,1109312)$ and $\ln Z$ gaps rest on FT.87(9)'s refuted identification (those are $(8,Z^{\rm tetra}_{\mathrm{byp}}-1,Z^{\rm cube}_{\mathrm{byp}}-1)$, three different skeletons) and $\ln$ of a *signed* sum is not an entropy [FT.67(2); the corpus entropy is $S_{\mathfrak L}=n_{\mathcal R}\ln2$, CT1.29] — an amplitude-to-entropy smuggle, void. Legitimate and derived: distinguishing $N$ classes costs $N$ registers and $\log_2N$ bits [C10], so $N=3$ costs $3$ registers / $\log_23$ bits and is available at $\delta h\ge2$. **The obstacle to generations is the absence of a label, not channel capacity** [item 20 deficit 3]. The Compton-like length $1/m_{\mathrm{hid}}=\mathfrak h/(K\ln2)$ exists [D2.9], but the threshold $\delta h\ge\lceil\log_2\#\text{classes}\rceil$ depends only on the class count, so **no Compton-wavelength relation arises**.

### FT.83 — The rung emergence ledger (audit pass C): derived, declared, open

**Thm.** Under Def-H.29, per rung $n$:
$(1)$ **The ladder is a theorem, not a picture.** $\mathcal A(0)=\{J\}$; $\mathcal A(1)=\{J,G,W,H,D^+\}$; $\mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\}$; $\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\}$; $\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}$, with a strict mask flag $\dim\mathcal K_n=(6,16,17,25)$ [CT0.13, CT0.14 — both with Pfs]. The admissibility ceiling is derived: $D_{\mathrm{tick}}(n)=2^{n+1}\le C_{\mathrm{cap}}=16\iff n\le3$, with saturation at $n=3$ [CT0.5, CT0.11, P2's $n_{\max}=3$].
$(2)$ **Rung-by-rung status.**
$$
\begin{array}{c|l|l}
n & \text{what becomes active/trackable} & \text{status}\\
\hline
0 & J^\pm\ \text{seals only};\ \dim\mathcal K_0=6 & \textbf{derived}\ [\mathrm{CT0.13}/\mathrm{CT0.7}]\\
1 & G(5)\ \text{spin-2 shear},\ W(3),\ H(1),\ D^+(1);\ \dim\mathcal K_1=16 & \textbf{derived}\ [\mathrm{CT0.12}/\mathrm{CT0.13}];\ \text{the "pretime force set"}\\
2 & +\ \mathrm{EM};\ \alpha_{\mathrm{EM}}=\pi;\ q_{\mathrm{EM}}\ \text{readable on open chains} & \textbf{derived}\ [\mathrm{CT0.13},\mathrm{EM.9},\mathrm{EM.20}]\ \text{under Comm-min}+\text{Eff (declared premises)}\\
3 & +\ \text{strong};\ N_{\text{colour}}=3,\ N_{\mathrm{gluon}}=8;\ \text{sealing}=\text{confinement};\ \text{mass reads} & \textbf{derived}\ [\mathrm{CT3.20},\mathrm{CT3.13},\mathrm{CT3.22},\mathrm{EW.20}/\mathrm{EW.33}]\\
\ge4 & D^-\ \text{absorption}\ O(n)=2^{n+1}{-}16,\ w=0\ \text{dust},\ \text{locking};\ \neg\exists\ \text{gauge structure} & \textbf{derived as a no-go}\ [\mathrm{CT0.11},\mathrm{CT4.1},\mathrm{CT4.4},\mathrm{CT4.5},\mathrm{FT.59}]
\end{array}
$$
$(3)$ **What is *not* derived at any rung.** (a) The proposal's "$n=1$: gravity, weak, Higgs, Dark$^+$, Janus" is exactly $\mathcal A(1)$ and is derived — but the *Higgs* entry is the scalar aspect $F_H$ with a P4-free background $h_0$ [EW.13, EW.20, P4], and its mass is "configuration data" [EW.27]: the mechanism is derived, the scale is not. (b) The proposal's "$n=2$: EM $+$ lepton structure" is **half derived**: EM is a theorem; "lepton structure" has no read at any rung (no lepton species, no chirality [FT.81(5)]). (c) "$n=3$: colour $+$ quarks $+$ the baryon edge budget" is derived — $\varepsilon_{ijk}$ sealing of three fundamentals [CT3.15/CT3.17/D3.9], the $2$s-and-$3$s partition rule [FT.34(5)], and $N=1$ impossibility [FT.27] — but "quark" in the corpus is D3.8's *bound fermionic loop with a triplet attachment*, i.e. a topological definition with no flavour and no chirality. (d) "$n\ge4$: lock / black-hole-matter cascade": the locking and absorption side is derived (CT4.1/CT4.2/CT4.5, $w=0$ dust, retained-and-inaccessible [D1.11]); **"black hole" has no corpus referent at all** (inventory count $0$), so the cascade reading is an external gloss, recorded and not adopted.
$(4)$ **Parameter census.** P4 declares $8$ independent internal configuration parameters $(g,g',h_0,c_W,\Lambda,\varkappa,\beta,\alpha_\Omega)$ with $6$ functionally dependent members $(\theta_W,e,\mu_\star^2,m_W,m_Z,m_H)$; P1/A §0.3 admit exactly **one** free dimensionful scale $\mathfrak h$; P3 names $G_N=\mathfrak h^2/(4\ln2)$, $\kappa^2=8\pi G_N$ for external comparison only; P5 forbids identifying any quantity with a measured constant. The SM's $19$ parameters (external count: $3$ gauge $+\,1$ VEV $+\,9$ Yukawa $+\,4$ CKM $+\,1$ $\theta_{\mathrm{QCD}}+\,1$ Higgs self-coupling) contain **$13$ flavour parameters, which alone exceed the corpus's $8$** — and the corpus's $8$ are declared *configuration* data, not constants, so no parameter-by-parameter map exists even in principle without extending P4.

### FT.84 — The deficit table and the two-ceiling synthesis (audit pass D)

**Thm.** Under Def-H.29 and FT.81–FT.83:
$(1)$ **The ranked deficit list** (load-bearing order; class: (i) missing declaration, (ii) structural no-go already proven, (iii) genuinely open):
$$
\begin{array}{c|l|l|l}
\# & \text{deficit} & \text{corpus status} & \text{class}\\
\hline
1 & \text{chirality (Weyl/projector)} & \text{no read; }\omega\text{-vocabulary only [D2.6]} & \text{(iii) open — root deficit}\\
2 & \text{Yukawa sector / fermion masses} & \text{no read; no P4 parameter} & \text{(iii) open, constrained by P1/P4}\\
3 & \text{three generations / flavour} & \text{no read (Open Gaps 12)} & \text{(iii) open}\\
4 & \text{CKM/PMNS mixing, CP phase} & \text{no read} & \text{(iii) open; needs 1 and 3}\\
5 & \text{gauge-anomaly structure} & \text{not poseable} & \text{(ii) blocked by 1}\\
6 & \text{neutrino species/mass/mixing} & \text{no read} & \text{(iii) open; needs 1 and 3}\\
7 & \Lambda_{\mathrm{QCD}}\ \text{/ any second scale} & \text{no read} & \text{(ii) no-go [A §0.3, P1, P5]}\\
8 & \text{Higgs as }4\text{ real dof} & \dim F_H=1 & \text{(ii) no-go [CT0.12 allocation]}\\
9 & \text{fractional confined charges} & \text{ternary read} & \text{(ii) partial no-go [EM.9, CT3.22]}\\
10 & |q|=2\ \text{observable states} & \text{single-chain read} & \text{(iii) open; needs a multi-chain read}\\
11 & \text{spin-statistics} & \text{external} & \text{(iii) open [FT.80(5)]}\\
12 & \text{SM masses (any species)} & \text{two ceilings proven} & \text{(ii) no-go [FT.76(3), FT.79(2)]}
\end{array}
$$
$5$ structural no-goes or blocked items (each with a cited no-go), $7$ open. Deficit $1$ is the root of $4,5,6$ and $11$; deficits $7$–$9$ and $12$ are derived impossibilities within the current inventory.
$(2)$ **The two-ceiling synthesis.** Both mass audits failed for the *same* structural reason at different loci: the pole side is bounded because a cone defect is an angle ($m^2_{\mathrm{pole}}\in[0,4\hat\mu'^2]$, widest ratio $6.39$ [FT.76(3)]), and the cover side is bounded because a mass counted in crystallized edges is bounded by the cap census ($K\le3V/2$, $|\mathcal C|\le3V/4$, widest ratio $6$ on the cube [FT.79(2)]). Deficit $2$ names the deeper cause: **there is no Yukawa sector**, so no mechanism in the inventory generates fermion mass at all — the two ceilings bound the *reads that exist*, and the SM's masses live in a sector the corpus does not contain. The mass negatives of FT.77/FT.79 are consequences of deficit $2$, not evidence against the reads themselves.
$(3)$ **What is reproduced, stated positively** (each with its citation): the gauge block dimensions and their sum $8+3+1=12$ [CT0.14, CT0.12, CT1.1]; $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$ closure with correct roots, normalizations and no ninth gluon [FT.82(2)–(3); CT3.8, CT3.13]; the derived colour count $3$ [CT3.20]; the full electroweak mixing structure with an exactly massless photon and $m_W=m_Z\cos\theta_W$, $1/e^2=1/g^2+1/g'^2$ [EW.20/23/24/35]; the vev's doublet-and-singlet quantum numbers [EW.20, EW.32]; confinement as a theorem with norm-zero isolated triplets [CT3.22, CT3.18, FT.19]; the baryon/meson sealing grammar [D3.9, CT3.15, CT3.17, FT.34(5)]; integer observable charge with the meson set exactly equal to the ternary read [EM.9, D3.4, FT.81(3)]; the spin ladder $j=|k|/2$ with $\mathrm{Sym}^k$ carriers [CT0.7a, EW.32, FT.52–FT.60, Def-H.38]; a derived Newton constant from the single scale [P3, CT2.9]; the fermion/boson *content-type* split [D1.5, Def-H.4]; and, beyond the SM, a dark sector with exact equations of state [D4.1–D4.3, CT1.25, CT4.1, CT4.5, FT.71].
$(4)$ **Verdict.** The corpus is **not** a Standard Model completion and does not claim to be: it is a derivation of the gauge-and-geometry skeleton from one scale and sixteen registers, with the chiral matter sector, the flavour sector and every dimensionful mass scale left outside the inventory. Its completeness fraction on the audited entry list is $13/24$, concentrated as $4/4$ on gauge species and $0.19$ on the fermion sector. No identification is made; Open Gaps 5/12 are unchanged and now carry a sharper form: *the mass question is not open but blocked from two sides (deficit $2$ above, ceilings below), while the gauge question is substantially answered.*
$(5)$ **Consequences.** (a) Any further mass-read search must first extend P4 with a flavour/Yukawa sector or accept that fermion masses have no read — searching for the SM hierarchy inside the existing reads is exhausted by FT.77/FT.79 and this clause. (b) The large-$V$ route of FT.79(2) is now demoted: even at $V\ge1200$ the resulting ladder would be an *even-integer* spectrum with no chirality and no flavour, so it could match a hierarchy's *range* and still not its *structure*. (c) The highest-value open direction is deficit $1$: a chirality read would unblock $4,5,6,11$ at once, and D2.6's $\omega$-action is the only existing hook — whether $\omega$ (or the FT.78(6) cover chirality) can be promoted from vocabulary to a projector is a well-posed question with no answer in the current inventory.

### FT.93 — The native Clifford census and the weak-chirality pincer (Tasks 1–3)

**Thm.** On $\mathfrak H(\mathbb C^4)$ with CT1.2's basis and CT0.7's $\mathbb S$, $\Pi_{\mathcal R}=\tfrac14(3E_0+\Sigma)$, $\Pi_{\mathcal V}=\tfrac14(E_0-\Sigma)$:
$(1)$ **Clifford frames are native (positive, new).** Among the $15$ non-identity Pauli products (each Hermitian, squaring to $+I_4$, traceless) there are exactly **$30$ pairwise-anticommuting $4$-frames** (unordered; $720$ ordered, $24$ orderings per frame). For every frame: $\gamma_{\mathcal F}$ is Hermitian, $\gamma_{\mathcal F}^2=I_4$, $\operatorname{Tr}\gamma_{\mathcal F}=0$, $\{\gamma_{\mathcal F},e_i\}=0$; the $16$ real products $\{e_{i_1}\cdots e_{i_r}\}$ are $\mathbb R$-linearly independent (rank $16$ on the example frame) — the frame generates a real subalgebra $\cong Cl(4,0)$ acting on $\mathbb C^4\cong\mathbb R^8$, **with no new axiom** (A3's Pauli facts + CT1.1's basis suffice). The override's items 1–6 are verified with two precisions: $\gamma_{\mathcal F}$ is *frame-dependent* — every ordering sign flip flips $\gamma_{\mathcal F}$ ($12/12$ witness), and $15$ distinct values occur (below) — so "$\gamma_5=\omega$" names a *choice*, not a canonical element; and A3's $\eta=(-,+,+,+)$ labels the $T$-involution only — it enters no Clifford relation (the signature is Euclidean, $e_i^2=+I_4$, as the override requires; no Minkowski structure is used anywhere).
$(2)$ **The full pseudoscalar catalog (exhaustive).** All $15$ values are attained, **each by exactly $2$ frames**, in three species:
$$
\begin{array}{c|c|c|c|c}
\text{species} & \gamma_{\mathcal F}\ (\text{up to sign}) & (S,T) & \text{commuting}\ W_i & [\gamma_{\mathcal F},\mathbb S]\\
\hline
\text{mixed}\ (6) & \sigma_0\otimes\sigma_i\ /\ \sigma_i\otimes\sigma_0 & (\neg\text{definite},-) & W_i\ \text{only} & \pm2iJ_i\\
\text{diagonal}\ (3) & \sigma_i\otimes\sigma_i & (+,+)\in\mathcal E_{++} & W_i\ \text{only}\ (\text{acomm.}\ W_j,W_k) & 0\\
\text{off-diag. spatial}\ (6) & \sigma_i\otimes\sigma_j\ (i\ne j) & (\neg\text{definite},+) & \text{none}\ (\text{acomm.}\ W_k,\ k=6{-}i{-}j) & \mp2iK_k\ (k=6{-}i{-}j)
\end{array}
$$
The example frame of the override, $\mathcal F_0=(\sigma_1\otimes\sigma_2,\ \sigma_2\otimes\sigma_2,\ \sigma_3\otimes\sigma_2,\ \sigma_0\otimes\sigma_1)$, gives exactly
$$
\gamma_{\mathcal F_0}=\sigma_0\otimes\sigma_3=\operatorname{diag}(1,-1,1,-1);\qquad
P^{(\mathcal F_0)}_+=\operatorname{diag}(0,1,0,1);\qquad
P^{(\mathcal F_0)}_-=\operatorname{diag}(1,0,1,0),
$$
both idempotent, orthogonal, summing to $I_4$, trace $2$, rank $2$ — the requested exact matrix forms. **No $\gamma_{\mathcal F}$ commutes with more than one $W_i$; none anticommutes with more than two.**
$(3)$ **The pincer (the sharpened deficit-1 obstruction).** No chirality grade on the pair register can be weak-covariant, from either side:
**(a) commuting side.** $\{M:[M,W_i]=0\ \forall i\}=\operatorname{span}_{\mathbb C}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\}$ (complex dimension $2$ — Schur on $3\oplus1$; machine-solved exactly). Its involutions are $\pm\Pi_{\mathcal R}\pm\Pi_{\mathcal V}$ with traces $3a+b\in\{\pm4,\pm2\}$; a pseudoscalar needs $\operatorname{Tr}=0$ (general: $\operatorname{Tr}(e_1e_2e_3e_4)=-\operatorname{Tr}(e_2e_3e_4e_1)$) — $3a+b=0\wedge a^2=b^2=1$ has **no solution**.
**(b) anticommuting side.** $\{M:\{M,W_i\}=0\ \forall i\}=\mathbb C\cdot\Pi_{\mathcal V}$ **exactly** (complex dimension $1$; machine-solved): rank $1$, trace $1$ — singular, never an involution. Structural reason: invertible $M$ with $\{M,W_i\}=0$ makes $\operatorname{Ad}(M)$ a Lie automorphism equal to $-\mathrm{id}$ on $\mathfrak{su}(2)$, but $-\mathrm{id}$ reverses the bracket ($[W_1,W_2]=iW_3\mapsto-iW_3\ne iW_3$) — contradiction.
**(c) exhaustive.** Every one of the $15$ attained $\gamma_{\mathcal F}$ fails (a) and (b) explicitly: $[\gamma_{\mathcal F},W_i]\ne0$ for some $i$ and $\{\gamma_{\mathcal F},W_i\}\ne0$ for some $i$ — all verified entrywise.
**(d) seed side.** On the actual matter carrier $\mathcal H_{\mathsf v}\cong\mathbb C^2$ with $W_i\mapsto\tfrac12\sigma_i$ [EW.32]: $\{m:[m,\sigma_i]=0\}=\mathbb C\cdot I_2$ and $\{m:\{m,\sigma_i\}=0\}=\{0\}$ — the weak seed representation is **irreducible**: no nontrivial projector on the matter carrier commutes with the weak action, and no grade anticommutes with it either.
$(4)$ **Task 2's claim refuted, per frame and in general.** For $\mathcal F_0$: $W_1,W_2$ *flip* the chiral halves ($P_\mp W_{1,2}P_\pm\ne0$ entrywise) and $W_3$ (the only commuting one) preserves them with $P_-W_3P_-=\operatorname{diag}(1,0,0,0)$ — nonzero, non-scalar on the $2$-dimensional image: "annihilates or acts trivially on the right eigenspace" is false for every $i$. In general, no frame can make a chiral half weak-inactive: $W_iP=0\ \forall i$ forces $\operatorname{im}P\subseteq\bigcap_i\ker W_i=\wedge^2$ [clause (5)], which is $1$-dimensional, while $\operatorname{rank}P^{(\mathcal F)}_\pm=2$. Hence **$SU(2)_L$-type chiral coupling is NOT natively derivable**, and B6's target $8+7=15$ is not reachable: on $\mathbb C^4\otimes(\mathbb C^3\oplus\mathbb C^1)$ the native counts are $8+8=16$; the missing right state is the [EXT] SM species fact ($\nu_R$ absent — deficits 2/6: no species list, no neutrino read). Two further category notes, machine-grounded: EW.32's seed is **colour-neutral by theorem** ($T_a\mathsf v=0$) and colour sits in the orthogonal stack block [CT0.12 Rmk, CT0.14: the blocks are $\oplus$-summands of $\mathcal K_\Sigma$, not tensor factors] — so "$\mathbb C^4\otimes\mathbb C^3$" is not a corpus construction; and "$8=2\times(3{+}1)$" (doublet dimension $\times$ colour reads $\{3,1\}$) is formable from derived numbers and coincides with the [EXT] left count — **flagged as coincidence, not used** (deficits 1–3 stand between; FT.89(2) precedent).
$(5)$ **The native selectivity that does exist (positive, derived).** The weak force grades the pair arena by **$S$-parity**, not by chirality: $W_i\Pi_{\mathcal V}=0$ exactly $\forall i$ (the weak annihilates the singlet $\wedge^2$), $\sum_iW_i^2=2\Pi_{\mathcal R}$ [Cor CT0.7a] (spin $1$ on $\vee^2$, spin $0$ on $\wedge^2$) — a $3$-active/$1$-inactive split, and $\bigcap_i\ker W_i=\operatorname{im}\Pi_{\mathcal V}$ exactly (machine: the joint kernel is the $1$-dimensional singlet line). This is a *force-arena* selectivity; matter chirality would have to grade a carrier on which the gauge action is trivial — the opposite pattern.
$(6)$ **Task 3, exactly.** $[\gamma_{\mathcal F},\mathbb S]=0\iff\gamma_{\mathcal F}=\pm\sigma_i\otimes\sigma_i$ — the $S$-aligned chiralities are exactly the three *diagonal* ones, and they live in $\mathcal E_{++}$, the gravity/Higgs block [CT1.1, CT1.2], each anticommuting with the two non-own $W$'s (never weak-covariant). The full commutator table is clause (2)'s last column; example: $[\sigma_0\otimes\sigma_3,\ \mathbb S]=2iJ_3$ — **chirality rotates into the Janus seal sector** under the swap. The $S$-aligned three are never weak-covariant either: $[\sigma_3\otimes\sigma_3,\ W_1]=2iE^{23}$ exactly (machine) — the weak rotation turns an $S$-aligned chirality into gravitational shear. The two splittings provably do not align: $\operatorname{rank}(P^{(\mathcal F_0)}_\pm\Pi_{\mathcal R})=2$, $\operatorname{rank}(P^{(\mathcal F_0)}_\pm\Pi_{\mathcal V})=1$ — each chiral half cuts the triplet $2{+}1$ and the singlet $1{+}1$... (the singlet line meets *both* halves), so neither grading refines the other, and $P^{(\mathcal F_0)}_\pm\notin\operatorname{span}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\}$ ($[P_\pm,\mathbb S]\ne0$). The override's hypothesis — "left-handed fermions are the S-even/S-odd states the Weak force can see" — is **false as stated**: the weak-visible split is $(\vee^2,\wedge^2)=(3,1)$ by $S$-parity, while every chiral split is $(2,2)$; the dimensions alone forbid the identification.
$(7)$ **Diagnosis and relocation of deficit 1 (the synthesis).** The override's correction is accepted where it is true: the "missing spinor bundle" framing was too strong — fiberwise, the Clifford algebra and its chiral projectors are **constructible from A1/A3 with no declaration** (clause (1)), and Def-H.14's $\mathcal E(e)\subset\mathfrak H(\mathbb C^4)_e$ already makes the register a per-edge arena bundle. But $\mathbb C^4$ is the **internal/force arena**: it carries the weak as $3\oplus1$ (clause (5)), while a Dirac-type $\gamma_5$ must commute with the gauge action on a *spacetime-side* factor. The pincer (clause (3)) is the exact incompatibility: no element of $\operatorname{End}(\mathbb C^4)$ is simultaneously a pseudoscalar and weak-scalar, and the matter carrier $\mathbb C^2$ is weak-irreducible. **Deficit 1 is therefore relocated, not closed**: what is missing is not matrices but a spacetime spin factor (a carrier on which the gauge action is trivial and a Clifford module over the emergent geometry acts) — and a global Dirac-type operator would additionally require a per-edge frame assignment $e\mapsto\mathcal F_e$ (fiberwise frames exist by clause (1); the assignment is undeclared datum) coupled to the EW.32 transport. Recorded in item 21 as an enumerated would-be declaration, **not adopted, no declaration-entry number** (the pincer blocks the chiral use regardless of the assignment, and no computable consequence was identified). The reversal structure declared by the corpus remains exactly $\langle\omega,\Theta_{\mathfrak L}\rangle\cong\mathbb Z_2\times\mathbb Z_2$ [FT.88]; the $15$ register-level $\mathbb Z_2$-grades $\gamma_{\mathcal F}$ are new *constructible* objects with no declared coupling to $\omega$ or $\Theta_{\mathfrak L}$ (different spaces: patterns vs fiber).
$(8)$ **The inventory gloss, corrected on the record.** Item 20 deficit 1's parenthetical "(no Dirac/Clifford algebra is declared)" is superseded: none is *declared*, but $Cl(4,0)$ frames are *derived* (clause (1)) — the deficit was never the algebra; it is the weak-covariant grade (clause (3), proven absent here) and the spacetime factor (clause (7), absent from the inventory). The chirality-projector non-constructibility result of stands, with its reason sharpened from "no candidate matrices" to "a proven pincer".

### FT.95 — Flicker chirality: the tautology, the absent trajectory, and the zero-expectation theorem

**Thm.** Under Cal-F, Def-H.25, D2.6:
$(1)$ **D4/D5 are tautological.** With $k(t)=(-1)^tk_0$ and $\mathrm{coupling}(t)=\mathrm{wb}\cdot\mathrm{hc}\cdot k(t)$: $\operatorname{sign}(k(t))\cdot k(t)=|k(t)|=|k_0|$ for every $t$ (machine: all $k\in\{\pm1,\dots,\pm5\}$), so $\langle\chi\rangle_T=\mathrm{wb}\cdot\mathrm{hc}\cdot|k_0|$ **for every $T\ge1$** — independent of the dynamics, the tick count and the phase boundary. "$\langle\chi\rangle_T\ne0$" is built in by the formula, not derived: the same species as FT.87(3)'s Regge-tautology verdict. D5 is void; D6 substitutes a measure parameter ($p^*_\infty=\sqrt{2/3}$ — itself FT.89(2d)'s cap-3 output, and a phase-boundary datum of the bypass measure [Def-H.26/FT.70], not a dynamics input) into the tautology and returns the tautology.
$(2)$ **D1–D3 have no flicker referent.** The winding $k$ is a read of *materialized* closed chains [EW.18, FT.22]; flicker states carry none — bound content survives only dissolved, in even cycles [FT.69's cycle-alternation lemma], and covers carry no materialized closed chain [FT.80(6)] — so no trajectory $k(t)$ exists in the flicker sector. Cal-F declares the *rates* $r=\Gamma_{J^+}/\Gamma_{J^-}$ (per-edge independent detailed balance), not per-tick schedules; $\delta\tau$ is schedule data that $R$ does not determine [FT.80(5)]; and no oscillation frequency is constructible [FT.86(7): only $\tau_c=1$ ledger tick, CT0.3]. $\mathrm{weak\_bias}$ and $\mathrm{higgs\_coupling}$ count **0** in frozen Parts 1–2 (machine-asserted). The corpus's genuine period-2 phenomenon is FT.86(2)'s alternating *correlation ripple in the crystallization indicators* (cap-induced, exact decay rate $(\sqrt{21}-5)/2$) — a different object: it is $C$-even, orientation-blind, and carries no chirality; D2's deterministic sign-alternating winding conflates the bypass and bound sectors.
$(3)$ **The zero-expectation theorem (the positive replacement for D5).** Global reversal $R\mapsto R^{\mathrm T}$ preserves admissibility, $K$, cover status and the amplitude $A(R)=(-1)^{|R|}2^{|R|}$ — **exhaustively verified on the tetrahedron**: all $1230$ bypass configurations, all $101$ covers, and all $4096$ patterns; the norm-layer class data $(K,\Omega)$ are reversal-invariant by FT.80(1). Hence both layer weights of the declared flicker ensemble are reversal-invariant, and **every $C$-odd read has exactly zero ensemble expectation**: for $f(R^{\mathrm T})=-f(R)$,
$$
\sum_R A(R)\,f(R)=0\qquad(\text{machine witness: the orientation-bias read}\ f(R)=\#\{(a,b)\in R:a<b\}-\#\{(a,b)\in R:a>b\},\ \text{exact}\ 0\ \text{over all}\ 4096).
$$
In particular $\langle q_{\mathrm{core}}\rangle=0$ ($\omega$-odd: FT.40/D2.6) and $\langle\operatorname{sign}(k)\rangle=0$ ($C$-odd: FT.87(8)) in the declared ensemble. **Parity violation is not constructible from the flicker**: producing $\langle C\text{-odd}\rangle\ne0$ requires declaring a $C$-odd state or a $C$-odd dynamics — deficits 1/2 territory; the exact declared reversal structure remains $\langle\omega,\Theta_{\mathfrak L}\rangle\cong\mathbb Z_2\times\mathbb Z_2$ [FT.88], whose elements are symmetries of the registration data, and by this clause of the equilibrium weights.

### FT.101 — The weak branch grading: the two crystallization branches are weak-inequivalent

**Thm.** Under A3 ($\mathcal H_p\otimes\mathcal H_q=\vee^2\oplus\wedge^2$), A4 (branches: $\alpha_{pq}=0$ on $|\Pi_{\mathcal V}\rho_{pq}|\le\varepsilon_q$; $\alpha_{pq}=\pi$ on $|\Pi_{\mathcal V}\rho_{pq}|\ge1-\varepsilon_q$), $\Pi_{\mathcal R}=\tfrac14(3E_0+\Sigma)$, $\Pi_{\mathcal V}=\tfrac14(E_0-\Sigma)$ [CT0.7], $W_i=\tfrac12(\sigma_0\otimes\sigma_i+\sigma_i\otimes\sigma_0)$ [CT1.2, FT.13], $\Phi=\{0,\pi\}$ [D0.5, CT0.9]:
$(1)$ **Aligned branch: weak-active.** $\ [\mathbb S,W_i]=0$; $\ W_i\Pi_{\mathcal R}=W_i=\Pi_{\mathcal R}W_i\Pi_{\mathcal R}\ne0$ for every $i$ (entrywise witnesses); $\ \sum_iW_i^2=2\,\Pi_{\mathcal R}$; Casimir read on $\vee^2$: $2=1(1{+}1)$ [CT0.7a].
$(2)$ **Antialigned branch: weak-blind.** $\ W_i\Pi_{\mathcal V}=0=\Pi_{\mathcal V}W_i$ for every $i$; $\ \bigcap_i\ker W_i=\operatorname{im}\Pi_{\mathcal V}$ (the singlet line, dimension $1$); Casimir read on $\wedge^2$: $0$ [CT0.7a, FT.93(5)].
$(3)$ **The branch flip is label-level.** The unique nontrivial automorphism $\iota$ of $\Phi$: $\iota(\alpha)=\pi-\alpha$; it exchanges the A4 branch labels ($\alpha=0\leftrightarrow\alpha=\pi$). On configuration data $\iota$ is the alignment-pattern complement $\mathcal P\mapsto E_{\mathcal R}\setminus\mathcal P$ [Def-EM.21, EM.23, EM.24(2); CT1.11a(4)] — exhaustive machine census: the complement flips $\alpha_e$ on every edge and exchanges the uniform patterns $\varnothing\leftrightarrow E_{\mathcal R}$ [EM.23(4)]. **No Hilbert-space implementation exists:** $\neg\exists\,M\in\operatorname{End}(\mathbb C^4)$ invertible with $M\Pi_{\mathcal R}M^{-1}=\Pi_{\mathcal V}$ — conjugation preserves trace and rank, and $\mathfrak T\Pi_{\mathcal R}=3\ne1=\mathfrak T\Pi_{\mathcal V}$, $\operatorname{rk}\Pi_{\mathcal R}=3\ne1=\operatorname{rk}\Pi_{\mathcal V}$ [CT0.7(1); exact witness].
$(4)$ **The weak support is not flip-invariant.** The weak support is $\Pi_{\mathcal R}$: $W_i=\Pi_{\mathcal R}W_i\Pi_{\mathcal R}$ exactly [(1)]; $\iota$ maps the branch label $\mathcal R\mapsto\mathcal V$, on which the weak read is $0$ [(2)]: weak-activity is branch-selective and $\iota$-asymmetric — the flip maps the weak-active branch to the weak-blind branch. Sharp point $\varepsilon_q=0$: branch $\alpha=0\iff\operatorname{supp}\rho\subseteq\vee^2$, branch $\alpha=\pi\iff\rho=\Pi_{\mathcal V}$ [CT0.8]; witnesses: $W_3\cdot(\Pi_{\mathcal R}/3)\ne0$, $W_i\,\Pi_{\mathcal V}=0\ \forall i$ (exact).
$(5)$ **Structural parity non-invariance.** The weak couples to one A4 branch and annihilates the other: a $\mathbb Z_2$-asymmetry of the force on the registration alphabet of the real edges; the branch exchange does not preserve the weak action. **Scope:** the force-arena $S$-parity grading [FT.93(5), FT.93(7)] — $\neg$ a matter chirality projector: the pincer [FT.93(3)] and the relocation [FT.93(7)] stand unmodified, and deficit 1 of item 20 is untouched by this theorem.

### Def-H.31 — The bridge: dictionary, family, background, fluctuation operator, effective potential

**Def.** A construction class on the prior canon (Def-H.24 pattern: no new axiom); clauses (1)–(6) are constitutive interface definitions. Domain: $\varepsilon_q\in(0,\tfrac14)$ [CT0.8]; $\ \gamma:=1-4\varepsilon_q$, $\ q:=4\varepsilon_q$ [D0.3, D0.4].

$(1)$ **Dictionary (Def-H.31(1)).** $\ p:=\gamma=1-4\varepsilon_q;\qquad 1-p=q=4\varepsilon_q;\qquad s:=p/q;\qquad y:=16s^2=\dfrac{(1-4\varepsilon_q)^2}{\varepsilon_q^2}.$
Anchors (exact): $\varepsilon_q=\tfrac18\iff p=\tfrac12\iff y=16$ — the point at which FT.68(1)'s amplitude-weighted reading is the uniform measure and $\sum|A_C|^2=15745$ on the tetrahedron [CT2.8 norm layer: $|A_C|^2=16^{|\mathcal C|}$; FT.67(2)'s value formula]; $\varepsilon_q\to0\iff p\to1$ — the static-floor corner [FT.68(5); D0.4's sharp point $\gamma=1$]; $\varepsilon_q\to\tfrac14\iff p\to0$ — the identity-tilt, vacuum-dominated corner [L2 ($\gamma\to0$); FT.70(5) ($\langle K\rangle\to0$)].

$(2)$ **Family and weights (Def-H.31(2)).** $\ \mathbb F:=\{\text{tetra},\text{cube},\text{octa}\}$ — the skeletons whose two-sector covering polynomials are complete [FT.68(1), FT.68(3), FT.69(2)]:
$$
\mathcal Z^{\mathrm{tot}}_{\mathrm{tetra}}(y)=1+24y+72y^2+4y^3;\qquad
\mathcal Z^{\mathrm{tot}}_{\mathrm{cube}}(y)=1+48y+672y^2+3400y^3+6816y^4+264y^5+4y^6;
$$
$$
\mathcal Z^{\mathrm{tot}}_{\mathrm{octa}}(y)=1+72y+888y^2+2160y^3+840y^4
\qquad(\mathcal Z^{\mathrm{tot}}=\mathcal Z_{\mathrm{byp}}+\mathcal Z_{\mathrm{lock}},\ \text{rows pooled}).
$$
With $2E_\Gamma\in(12,24,24)$ the directed-edge counts and $K=2|\mathcal C|$ [FT.79(2)], the **cover-weighted Bernoulli weight** of $\Gamma$ is
$$
W_\Gamma(p)\ :=\ \sum_k c_k(\Gamma)\,16^k\,p^{2k}\,q^{2E_\Gamma-2k}\ =\ q^{2E_\Gamma}\,\mathcal Z^{\mathrm{tot}}_\Gamma\bigl(16p^2/q^2\bigr)\ =\ \mu_p\text{-average of }|A_C|^2\text{ over covers }C\subseteq\Gamma,
$$
an integer polynomial in $p$ with $W_\Gamma(0)=1$ (the vacuum cover) and $W_\Gamma(1)=0$ (the fully crystallized floor is no cover — it cancels [FT.67(3a)]). The **family measure** is
$$
P(\Gamma\mid\varepsilon_q)\ :=\ \frac{W_\Gamma(p)}{\sum_{\Gamma'\in\mathbb F}W_{\Gamma'}(p)}\qquad(\text{ensemble scope of CT4.5a/Def-H.26: per-edge Bernoulli }p).
$$

$(3)$ **Background state.** Cover-conditioned edge content and mean real fraction:
$$
\langle K\rangle^{\mathrm{cov}}_\Gamma(p):=\frac{N_\Gamma(p)}{W_\Gamma(p)},\quad N_\Gamma:=\sum_k 2k\,c_k 16^k p^{2k}q^{2E-2k};\qquad
\hat p_\Gamma:=\frac{\langle K\rangle^{\mathrm{cov}}_\Gamma}{2E_\Gamma}\in(0,\ K_{\mathrm{top}}/2E_\Gamma].
$$
The ensemble-averaged pair state (linear in the pattern measure; per-pattern state $=$ the branch state of its real/virtual edges, Cal-F detailed balance):
$$
\bar\rho_\Gamma(\varepsilon_q)\ :=\ \hat p_\Gamma\cdot\frac{\Pi_{\mathcal R}}{3}\ +\ (1-\hat p_\Gamma)\,\Pi_{\mathcal V}
\qquad[\mathrm{CT0.7}(1):\ \Pi_{\mathcal R}=\tfrac14(3E_0+\Sigma),\ \Pi_{\mathcal V}=\tfrac14(E_0-\Sigma)];
$$
$\operatorname{spec}(\bar\rho_\Gamma)=\bigl(\tfrac{\hat p_\Gamma}3,\tfrac{\hat p_\Gamma}3,\tfrac{\hat p_\Gamma}3,\ 1-\hat p_\Gamma\bigr)$ — faithful on the whole domain; $\mathfrak T\bar\rho_\Gamma=1$.

$(4)$ **Fluctuation operator (Def-H.31(4)).** $\Delta^{-1}_\Gamma(\varepsilon_q)$: the block-diagonal operator on the $16$-mode space $\mathfrak H(\mathbb C^4)$ [CT0.6] in the $\vee^2/\wedge^2$ decomposition of the swap grading [CT0.7(3)], with the A8 aspect labels of CT0.7(4):
$$
\textbf{S-even block}\ (10=9+1=\dim\mathfrak H(\vee^2)+\dim\mathfrak H(\wedge^2);\ \text{aspects }F_{D^+},F_H,F_G,F_{W^\pm},F_Z):
$$
the Bogoliubov–Kubo–Mori Hessian of the relative entropy $S(\rho\|\bar\rho_\Gamma)$ at $\bar\rho_\Gamma$ [math: the standard quadratic fluctuation kernel of the state-space information geometry; eigenvalue $1/\lambda$ on diagonal block directions]:
$$
M^2_{\vee^2}=3/\hat p_\Gamma\ (\times 9),\qquad M^2_{\wedge^2}=1/(1-\hat p_\Gamma)\ (\times 1);
$$
$$
\textbf{S-odd block}\ (6=3+3;\ \text{the seal forces }F_{J^+}=\operatorname{span}\{J_i\},\ F_{J^-}=\operatorname{span}\{K_i\}\ [\mathrm{CT0.7}(4)]):
$$
$$
M^2_{J^+}=p\cdot G_\Gamma(p)^2\ (\times 3),\qquad M^2_{J^-}=q\cdot G_\Gamma(p)^2\ (\times 3),\qquad G_\Gamma:=B_\Gamma-p^{2E_\Gamma}\ \ [\mathrm{Def\text{-}H.26},\ \mathrm{FT.70}(1)],
$$
with the detailed-balance occupations $(p,q)$ of the two seal channels [Cal-F; A8: $\mathbf F_{(+,\mathcal V)}=F_{J^+}$, $\mathbf F_{(-,\mathcal V)}=F_{J^-}$]. $B_\Gamma(p)=\sum_K c_Kp^Kq^{2E-K}$ with the frozen cap-census rows $c_K$ [FT.68(1), FT.68(3), FT.69(1)].

$(5)$ **Effective potential.** With the **swap supertrace** $\operatorname{Str}_{\mathbb S}X:=\mathfrak T(\mathbb S X)$ (defined here; $\ne$ the C-sector supertrace [CT2.10] — collision-avoidance declared once; $\operatorname{Str}_{\mathbb S}$ grades $\mathfrak H(\mathbb C^4)$ by CT0.7(4)'s $S$-parity, $10-6=4$):
$$
V_{\text{1-loop},\Gamma}\ :=\ \tfrac12\operatorname{Str}_{\mathbb S}\log\Delta^{-1}_\Gamma\ =\ \tfrac12\Bigl(\sum_{\text{S-even}}\log M^2_i-\sum_{\text{S-odd}}\log M^2_j\Bigr)
\ =\ \tfrac92\log\tfrac3{\hat p_\Gamma}-\tfrac12\log(1-\hat p_\Gamma)-\tfrac32\log(pq)-6\log|G_\Gamma|;
$$
$$
V_{\text{tree},\Gamma}\ :=\ -\log W_\Gamma(p);\qquad
V_{\mathrm{eff}}(\varepsilon_q)\ :=\ \sum_{\Gamma\in\mathbb F}P(\Gamma\mid\varepsilon_q)\,\bigl[V_{\text{tree},\Gamma}(\varepsilon_q)+V_{\text{1-loop},\Gamma}(\varepsilon_q)\bigr].
$$
Every log argument is positive on $(0,\tfrac14)\setminus\{\varepsilon^*_\Gamma\}$, $\varepsilon^*_\Gamma:=(1-p^*_\Gamma)/4$; $V_{\mathrm{eff}}$ is smooth on the wall complement and $V_{\mathrm{eff}}\to+\infty$ at both endpoints and at every wall (FT.102(4)).

$(6)$ **Mass read (Def-H.31(6)).** For each vacuum $\varepsilon_q^{(i)}$ of $V_{\mathrm{eff}}$ (FT.103):
$$
m_i^2\ :=\ \Delta S\bigl(\varepsilon_q^{(i)}\bigr)\ :=\ \frac{V_{\mathrm{eff}}\bigl(\varepsilon_q^{(i)}\bigr)}{8}
\qquad[\mathrm{L3}(2):\ V=8\,\Delta S_{\mathrm{pair}}\ \text{exact leading};\ \mathrm{L3}(4):\ m_i^2=\Delta S\ \text{inertial read};\ \text{dimensionless, nats}].
$$
The phase-band $\leftrightarrow$ generation-label correspondence is a labelling clause of this definition, not a derived selection; no particle identification (Open Gaps 5/12); no coupling to $m_{\mathrm{pole}}$/$m_{\mathrm{hid}}$ beyond Def-H.39's bridge slots (unconstructed).

### FT.102 — The fluctuation spectrum, the tree-level limit, and the seal-softening walls

**Thm.** Under Def-H.31:
$(1)$ **Exact spectrum.** For every $\Gamma\in\mathbb F$ and $\varepsilon_q\in(0,\tfrac14)\setminus\{\varepsilon^*_\Gamma\}$:
$$
\operatorname{Spec}\bigl(\Delta^{-1}_\Gamma(\varepsilon_q)\bigr)\ =\ \underbrace{\Bigl\{\tfrac3{\hat p_\Gamma}\times9,\ \ \tfrac1{1-\hat p_\Gamma}\times1\Bigr\}}_{\text{S-even},\ 10}\ \sqcup\ \underbrace{\bigl\{p\,G_\Gamma(p)^2\times3,\ \ q\,G_\Gamma(p)^2\times3\bigr\}}_{\text{S-odd},\ 6}\qquad(16\ \text{values}),
$$
with $\hat p_\Gamma\in(0,K_{\mathrm{top}}/2E_\Gamma]$, $K_{\mathrm{top}}/2E_\Gamma=(\tfrac12,\tfrac12,\tfrac13)$ for (tetra, cube, octa) — the supremum attained exactly in the limit $p\to1$ (vanishing order $2E-K_{\mathrm{top}}+2$ of $N_\Gamma-K_{\mathrm{top}}W_\Gamma$ at $p=1$; machine). The S-even block is strictly positive on the whole domain; the S-odd block vanishes exactly at $p\in\{p^*_\Gamma\}\cup\{0,1\}$ and nowhere else.
$(2)$ **The grading is matrix-exact.** On the CT1.2 basis over $\mathbb Q(i)$: $\operatorname{Ad}(\mathbb S)$ has eigenvalue $+1$ on $\{E_0,\Sigma,\hat E^{ij}\,(5),W_i\,(3)\}$ — $10$ modes — and $-1$ on $\{J_i\}\cup\{K_i\}$ — $6$ modes [CT0.7(4) membership reproduced from the matrices]; S-even $\iff[\mathbb S,X]=0\iff X$ preserves $\vee^2,\wedge^2$; S-odd $\iff\{\mathbb S,X\}=0\iff X$ swaps them [CT0.7(3)]; basis rank $16$ [CT0.6]; $\operatorname{Str}_{\mathbb S}(I_{16})=10-6=4$; on any degenerate spectrum $\lambda I$: $V_{\text{1-loop}}=\tfrac12(10-6)\log\lambda=2\log\lambda$ — the super-dimension is the interference coefficient the trace log carries.
$(3)$ **Tree-level limit $=$ the FT.68/FT.69 covering polynomials.** Setting $V_{\text{1-loop}}\equiv0$: $e^{-V_{\text{tree},\Gamma}(p)}=W_\Gamma(p)=q^{2E}\mathcal Z^{\mathrm{tot}}_\Gamma(y)$ *identically* — verified two ways: the polynomial expansion vs the sum over the *enumerated* covers (two independent enumerators per cell, all covers: $101/11205/3961$). Static evaluation anchors (exact integers):
$$
\begin{array}{c|ccc}
&\text{tetra}&\text{cube}&\text{octa}\\ \hline
\mathcal Z^{\mathrm{tot}}(4)\ (Z^\pm_{\mathrm{all}}) & 1505 & 2260161 & 367777\\
\mathcal Z_{\mathrm{byp}}(4)\ /\ \mathcal Z_{\mathrm{lock}}(4) & 1057\ /\ 448 & 1109313\ /\ 1150848 & 87649\ /\ 280128\\
W_\Gamma(\tfrac12)\cdot2^{2E}=\mathcal Z^{\mathrm{tot}}(16) & 35201 & 804725505 & 64126081\\
\mathcal Z_{\mathrm{byp}}(16)\ /\ \mathcal Z_{\mathrm{lock}}(16) & 15745\ /\ 19456 & 248613633\ /\ 556111872 & 4937857\ /\ 59188224
\end{array}
$$
the tetrahedron's bypass norm sum $15745$ and amplitude-weighted content $\langle K\rangle=62208/15745$ are FT.68(1)(ii) verbatim; the uniform readings $852/205$, $3311952/395023$, $2124600/318523$ at $p=\tfrac12$ are FT.68(1)(i)/FT.70(5) verbatim; the single-centre closed form $c_1=Vd(d-1)=(24,48,72)$ is FT.69(2) verbatim.
$(4)$ **Seal-softening walls.** $V_{\mathrm{eff}}\to+\infty$ at each $\varepsilon^*_\Gamma=(1-p^*_\Gamma)/4$, $p^*_\Gamma$ the unique zero of $G_\Gamma$ [FT.70(1)–(2)] — dyadic isolation at width $2^{-40}$ reproduces the frozen boundaries exactly: $p^*=(0.725372,\ 0.723525,\ 0.679217)$ for (cube, tetra, octa), i.e. $\varepsilon^*=(0.068657016,\ 0.069118773,\ 0.080195792)$, order octa $>$ tetra $>$ cube in $\varepsilon^*$ [FT.70(2)'s order in $p^*$ inverted by the dictionary]. At a wall the six S-odd masses vanish quadratically — the phase boundary is exactly where the reality-exchanging (seal) fluctuations become marginal. $V_{\mathrm{eff}}\to+\infty$ also at both domain endpoints: the floor side ($\varepsilon_q\to0$) from $W_\Gamma\to0$ (the floor cancels [FT.67(3a)]) and $-\tfrac32\log q\to+\infty$; the threshold side ($\varepsilon_q\to\tfrac14$) from $3/\hat p_\Gamma\to\infty$ and $-\tfrac32\log p\to+\infty$.
$(5)$ **Directive form.** $V_{\text{1-loop},\Gamma}=\tfrac12\bigl(\sum_{\text{S-even}}\log M_i^2-\sum_{\text{S-odd}}\log M_j^2\bigr)$ — the block assembly and the $16$-term eigenvalue assembly agree by enclosures; the minus sign on the $6$ odd terms is the swap-supertrace grading, and the odd block is precisely the seal force pair $F_{J^\pm}$ [CT0.7(4): "the $S$-odd blocks"; D1.2: the seals move A4-weight $\wedge^2\!\leftrightarrow\!\vee^2$].

### FT.103 — The vacuum structure: four exact vacua, three wall-delimited phase bands, dominance windows, the susceptibility census

**Thm.** Under Def-H.31:
$(1)$ **Vacuum census (complete at the resolved scale).** $dV_{\mathrm{eff}}/d\varepsilon_q=0$ has exactly four solutions in $(0,\tfrac14)$ on the wall-delimited bands — one per band, each a strict minimum ($V'$ passes $-\to+$; exact sign census by rational $+$ log-enclosure evaluation on dyadic grids; bisection to width $2^{-36}$):
$$
\begin{array}{c|c|c|c|c}
&\text{band}&\varepsilon_q^{(i)}\ (\approx)&V_{\mathrm{eff}}\ (\approx)&m_i^2=V_{\mathrm{eff}}/8\ (\approx)\\ \hline
\mathrm V_1&(0,\varepsilon^*_{\mathrm{cube}})\ \text{floor band}&0.021337258636&24.271850813&3.033981352\\
\mathrm V_2&(\varepsilon^*_{\mathrm{cube}},\varepsilon^*_{\mathrm{tetra}})\ \text{bicritical sliver}&0.068783298916&59.645122359&7.455640295\\
\mathrm V_3&(\varepsilon^*_{\mathrm{tetra}},\varepsilon^*_{\mathrm{octa}})\ \text{mixed band}&0.080091490970&38.713071069&4.839133884\\
\mathrm V_4&(\varepsilon^*_{\mathrm{octa}},\tfrac14)\ \text{thread-gas band}&0.190792364908&10.655753803&1.331969225
\end{array}
$$
All four values are strictly positive — $\Delta S$-admissible in nats [L3]; all four positions lie in CT0.8's physical domain $(0,\tfrac14)$. $\mathrm V_3$ sits $1.04\times10^{-4}$ below the octahedron wall (wall-adjacent: its depth is set by the seal-softening balance); $\mathrm V_2$ is the sliver bottom between the near-degenerate cube/tetrahedron boundaries — its existence and depth are controlled by the frozen splitting $|\varepsilon^*_{\mathrm{tetra}}-\varepsilon^*_{\mathrm{cube}}|=4.6176\times10^{-4}$ [FT.70(2)'s own numbers].
$(2)$ **Mass order and ratios (enclosure-exact).** $m^2(\mathrm V_4)<m^2(\mathrm V_1)<m^2(\mathrm V_3)<m^2(\mathrm V_2)$ (disjoint enclosures). The phase triple $(\mathrm V_4,\mathrm V_1,\mathrm V_3)$ in mass order:
$$
m^2:\ 1:2.277816:3.633067;\qquad m:\ 1:1.509244:1.906061;
$$
all four: $m^2:\ 1:2.277816:3.633067:5.597457$ (bare $m^2$-span $<6$ — clause (6)).
$(3)$ **Dominance windows (exact).** The pairwise $W$-crossings isolate (width $2^{-30}$): tetra$|$cube at $p=0.662192$ and $p=0.035764$ ($\varepsilon_q=0.084410$ and $0.241059$); cube$|$octa at $p=0.091544$ ($\varepsilon_q=0.227062$). Windows: tetra-dominant $(0,0.084410)\cup(0.241059,\tfrac14)$; cube-dominant $(0.084410,0.227062)$; octa-dominant $(0.227062,0.241059)$. Dominant skeleton at the vacua: $\mathrm V_1,\mathrm V_2,\mathrm V_3$ tetrahedron ($P_{\mathrm{tetra}}\approx0.999/0.720/0.556$); $\mathrm V_4$ cube ($P_{\mathrm{cube}}\approx0.727$). The octa window and the tetra tail sliver carry **no vacuum**: $V'>0$ throughout both (machine census) — the octahedron enters the vacuum structure through its wall $\varepsilon^*_{\mathrm{octa}}$, not through a dominance minimum.
$(4)$ **Susceptibility census.** Per skeleton, $\chi_\Gamma(y):=d\langle K\rangle^{\mathrm{cov}}_\Gamma/dy=2\operatorname{Var}_y(|\mathcal C|)/y$ [exact identity; math] is **strictly decreasing** on the exact grid $y=2^{i/4}$, $|i|\le40$ — no interior peaks: the van-Hove structure sits in $\operatorname{Var}_y(|\mathcal C|)$ (the log-fugacity susceptibility $d\langle K\rangle/d\ln y=2\operatorname{Var}$). The cover-condensation transition scales $y=c_k/c_{k+1}$ and their exact $\varepsilon$-images ($\varepsilon=1/(4+\sqrt y)$; each the unique root in $(0,\tfrac14)$ of the integer quadratic $(16d-n)\varepsilon^2-8d\varepsilon+d=0$, $y=n/d$; machine):
$$
\begin{array}{c|c|c}
\Gamma&y=c_k/c_{k+1}&\varepsilon_q=1/(4+\sqrt y)\ (\approx)\\ \hline
\text{tetra}&\tfrac1{24},\ \tfrac13,\ 18&0.237862,\ 0.218467,\ 0.121320\\
\text{cube}&\tfrac1{48},\ \tfrac1{14},\ \tfrac{84}{425},\ \tfrac{425}{852},\ \tfrac{284}{11},\ 66&0.241293,\ 0.234342,\ 0.224993,\ 0.212482,\ 0.110118,\ 0.082481\\
\text{octa}&\tfrac1{72},\ \tfrac3{37},\ \tfrac{37}{90},\ \tfrac{18}7&0.242845,\ 0.233386,\ 0.215462,\ 0.178458
\end{array}
$$
The family trajectory $\chi_{\mathbb F}(\varepsilon_q)=d\langle K\rangle_{\mathrm{fam}}/dy$ (with $\langle K\rangle_{\mathrm{fam}}=\sum_\Gamma P_\Gamma\langle K\rangle^{\mathrm{cov}}_\Gamma$, rational in $p$) has exactly **two** interior extrema on the resolved $2^{-13}$ grid (degree-$96$ integer-Horner census): $\varepsilon_q\approx0.019724$ (adjacent to $\mathrm V_1$) and $\varepsilon_q\approx0.083699$ (adjacent to the tetra$|$cube dominance boundary $0.084410$) — a census, not an identity: the extrema do not coincide with the vacua.
$(5)$ **Phase-band reading (Def-H.31(6)).** The three wall-delimited bands that carry vacua — floor band ($\mathrm V_1$; static-crystallization side), crossover band ($\mathrm V_2,\mathrm V_3$; sliver $+$ mixed), thread-gas band ($\mathrm V_4$) — are the three topological phases of the construction; the labelling of the phase triple as three generations is declared, not derived. The band count equals $|\mathbb F|$, the declared family size: the selection principle for *three* (item 20 deficit 3) is not supplied; the sliver vacuum $\mathrm V_2$ is a bicritical artifact of FT.70(2)'s near-degenerate boundaries — reported, not suppressed.
$(6)$ **Bare-span bound on the computed cells.** The all-four $m^2$-span is $5.597457<6$ — the same order as FT.79(1)'s pool maximum $6$ and FT.76(3)'s widest ratio $6.3925$: a third independent appearance of the $\approx6$ scale on the computed cells (FT.104(1) quantifies the [EXT] consequence).

### FT.104 — The [EXT] audit, the range-species classification, and the fourth read of Gap 7

**Thm.** **External-data clause** (FT.73(5)/FT.79(4) pattern): the hierarchies compared below — charged leptons $1{:}207{:}3477$, down-type $1{:}20{:}900$, up-type $1{:}600{:}80000$ — are *supplied measured data* [EXT]; they enter no derivation, no definition, no coefficient of the construction; this document identifies no particles (Open Gaps 5/12); no parameter is fitted (P1, P5; FT.87(11) precedent).
$(1)$ **Bare 1-loop read: exact shortfalls.** The phase triple $(m_1,m_2,m_3)=(1,\,1.509244,\,1.906061)$ in $m$, $(1,\,2.277816,\,3.633067)$ in $m^2$ [FT.103(2)] against [EXT]:
$$
\begin{array}{c|cccc}
&\multicolumn2c{m\text{-read shortfall}}&\multicolumn2c{m^2\text{-read shortfall}}\\
\text{[EXT] family}&\text{middle}&\text{outer}&\text{middle}&\text{outer}\\ \hline
\text{leptons }(207,\,3477)&\times137.2&\times1824.2&\times90.9&\times957.0\\
\text{down-type }(20,\,900)&\times13.3&\times472.2&\times8.8&\times247.7\\
\text{up-type }(600,\,80000)&\times397.6&\times41971.4&\times263.4&\times22020.0
\end{array}
$$
(enclosure-proven lower bounds: every middle shortfall $>10$, every outer $>100$.) The $m$-span $1.906$ is of the *same order* as the tree proxy's flat span $2$ and the all-four $m^2$-span $5.597$ of the same order as FT.79(1)'s pool maximum $6$: **the loop correction re-shapes the vacuum geometry — bands, walls, dominance windows — without extending the computed cells' numeric range.**
$(2)$ **Range-species classification.** (a) *Bare read:* the vacuum-depth range on a family grows with the cells' size — floor-side barrier instance at $p_0=\tfrac{15}{16}$: $-\ln W_\Gamma(p_0)=(7.31,\ 16.01,\ 27.05)$ with exponents $2E-K_{\mathrm{top}}=(6,12,16)$ and the exact lower-bound law $-\ln W_\Gamma(p_0)\ge(2E-K_{\mathrm{top}})\ln\tfrac1{q_0}-\ln\mathcal Z^{\mathrm{tot}}_\Gamma(16)$ [machine] — **linear in size, unbounded in the family**: unlike the defect-angle read (hard ceiling $4\hat\mu'^2$ [FT.76(3)]) and of the same order class as the cover ladder — spanning $1{:}R$ needs $V\ge4R/3$ [FT.79(2): $V\ge276$ down-type, $V\ge4636$ leptons]. (b) *Composed tilt read* (Def-H.40 species at general $\gamma$, composed with the vacua — declared composition, NOT adopted): per-edge contraction $c(\varepsilon_q)=1-\tfrac\gamma4=\tfrac34+\varepsilon_q$ [L2], composed over $E_{\mathrm{int}}$ internal edges [Def-H.40's composition clause]:
$$
T_i(E):=c\bigl(\varepsilon_q^{(i)}\bigr)^{2E};\qquad \bigl(c(\mathrm V_1),c(\mathrm V_3),c(\mathrm V_4)\bigr)=(0.771337,\ 0.830091,\ 0.940792);
$$
$$
\beta_{\mathrm{mid}}:=\tfrac{c(\mathrm V_3)}{c(\mathrm V_1)}=1.076172;\qquad \beta_{\mathrm{out}}:=\tfrac{c(\mathrm V_4)}{c(\mathrm V_1)}=1.219690;
$$
the range is **exponential in $E$** — the first read in Gap 7's comparison set that provably escapes both hard ceilings — with exact thresholds (each strict: $E{-}1$ falls below; enclosure-proven):
$$
\beta_{\mathrm{out}}^E\ge20\iff E\ge16;\quad \ge207\iff E\ge27;\quad \ge900\iff E\ge35;\quad \ge3477\iff E\ge42.
$$
Against FT.79(2)'s $V\ge276$ (down-type, cover ladder) and $V\ge4636$ (leptons): a **two-order compression** of the size requirement, $E_{\mathrm{int}}\approx16$–$42$ — within the corpus's computed-cell scale class.
$(3)$ **Proportionality obstruction (exact).** No single $E$ carries any [EXT] triple through (2b): the triple's shape is fixed by the base pair $(\beta_{\mathrm{mid}},\beta_{\mathrm{out}})$, and
$$
\frac{\ln\beta_{\mathrm{mid}}}{\ln\beta_{\mathrm{out}}}=0.369645\qquad\text{vs}\qquad\frac{\ln207}{\ln3477}=0.654006\quad[\mathrm{EXT}]
$$
(disjoint enclosures; mismatch factor $1.7693$). At the outer threshold $E=42$: $\beta_{\mathrm{mid}}^{42}=21.83<207$ — middle shortfall $\times9.5$. The obstruction datum is the **base clustering**: the walls cluster in a band of width $0.0115$ [FT.70(2)], so the contraction bases span only $(0.771,0.941)$; an [EXT]-shaped triple would need the vacua's $\ln c$-spreads proportional to $(\ln207,\ln3477)$ — missed by the exact factor above. This is the 1-loop species' own structural obstruction, dual to FT.76(3)'s angle bound and FT.79(2)'s edge budget.
$(4)$ **Adjudication summary.** The bridge is constructed and machine-exact: the tree limit reproduces the covering census [FT.102(3)]; the loop layer produces the corpus's first multi-vacuum spectrum — four exact vacua, three wall-delimited phase bands, walls at FT.70's boundaries, dominance windows with exact crossings [FT.103]; the mass read is $\Delta S$-admissible (all positive, nats) [L3]. It does not, on the computed cells: reach the [EXT] spans (clause (1)'s exact shortfalls); derive the number three (band count $=|\mathbb F|$, declared [FT.103(5)]); relate to $m_{\mathrm{pole}}$/$m_{\mathrm{hid}}$ (Def-H.39 unchanged; the category discipline of FT.89(2) applies to every cross-read). The exponential mechanism is real but sits in the composed species (clause (2b)), whose size thresholds are exact and whose proportionality datum (clause (3)) is the new obstruction. Item 7's comparison set gains the fourth read; item 20's deficits: 12 is reclassified (two hard ceilings $+$ linear bare $+$ exponential composed, all computed cells $\le6.39$ in span), 2 and 3 unchanged.

### Def-H.32 — The topology-blind path integral

**Def.** A construction class on the prior canon (Def-H.24 pattern: no new axiom); clauses (1)–(7) are constitutive interface definitions. Scopes (S1)–(S4) of Def-H.25 are inherited at every use ($\kappa_e\equiv1$ minimal-edge class on real edges unless a $\kappa$-class is named; literal $\aleph$-domain; seal/Janus bookkeeping static, $\mathcal J=1$; virtual edges weight $1$, no phase).

$(1)$ **The topology space and the budget filtration (Def-H.32(1)).** $\mathcal G:=$ the isomorphism classes of finite connected simple graphs (self-loops excluded [A1]; skeletons read as their bidirectional digraphs, $2E$ directed edges [A7, D0.1]; connectedness per D2.13's subnetwork scope). Regularization $=$ the declared **budget filtration**
$$
\mathcal G_B:=\{\Gamma\in\mathcal G:\ V(\Gamma)\le B\},\qquad
\mathfrak C_B(\Gamma):=\{R\subseteq E_{\mathrm{dir}}(\Gamma):\ |R|\le B_K\}\quad[B_K\ \text{default}\ 2E(\Gamma)],
$$
the budget being the ledger's own content measure: $|R|=n_{\mathcal R}$, $S_{\mathfrak L}=n_{\mathcal R}\ln2$ [CT1.29]. Every filtered sum below is a finite exact sum [FT.68(7) pattern]; the $B\to\infty$ limit is not constructed (growth data: FT.105).

$(2)$ **Configurations and the two weight layers.** A configuration on $\Gamma$ is $C=(R,\sigma)\in\mathfrak C(\Gamma)$ [D0.10]: pattern $R$ with per-edge signs $\sigma_e\in\{\pm1\}$ [CT0.9, D3.4]; vertex types $(n_{\mathrm{in}},n_{\mathrm{out}})$ [A7, D0.8]; locked ($D^-$-configured) $\iff k_v\ge4$ [CT4.5 source criterion; CT0.11]. The A8 edge weight is $w(C)=\mathcal J(C)\prod_{e\in E(C)}G(e)\cdot(-1)^{\aleph(\sigma,C)}$ [A8; at (S1): $G(e)=-\sigma_e$; $\aleph=\sum_{\text{centres}}|f_v|$, $f_v=\tfrac{s_{\mathrm{out}}-s_{\mathrm{in}}}2$ [D3.3]]. Two layers [CT2.8]:
$$
\textbf{amplitude layer}:\quad v_\Gamma(R):=\sum_\sigma w(R,\sigma)\qquad[\mathrm{FT.67}(2):\ v=2^{|R|}(-1)^{\sum\kappa}\ \text{on covers},\ 0\ \text{else}];
$$
$$
\textbf{norm layer}:\quad \nu_\Gamma(R):=\sum_\sigma|w(R,\sigma)|^2=2^{|R|}\qquad[|w(R,\sigma)|=1\ \text{for every valid pair};\ \mathrm{FT.68}\ \text{Rmk}(6c)].
$$

$(3)$ **Fugacities (Def-H.32(3) — formal indeterminates over $\mathbb Q$; no rate datum, no declared value).** Per configuration:
$$
\mathcal W^{\mathrm{amp}}_\Gamma(R)\ :=\ v_\Gamma(R)^2\;t^{|R|}\,u^{L(R)};\qquad
\mathcal W^{\mathrm{norm}}_\Gamma(R)\ :=\ \nu_\Gamma(R)\;t^{|R|}\,u^{L(R)},
$$
$L(R):=\#\{v:\ k_v\ge4\}$ the locked census; $t$ the crystallization fugacity, $u$ the $D^-$-retention fugacity [CT4.1–CT4.5 vocabulary: absorption/emission/dissolution/retention enter as the static fate fugacity; the emission/dissolution *moves* live in clause (7)]. Specializations are marked at every use: $t=p/q$ with $p=x_+/(x_++x_-)$ [FT.108(4), derived]; tilt refinement $\mathcal W\mapsto\mathcal W\cdot\tau_{\mathcal R}^{|R|}\tau_{\mathcal V}^{2E-|R|}$ with spectral values $\tau_{\mathcal R}=e^{-\gamma/3}$, $\tau_{\mathcal V}=e^{-\gamma}$ [Cor L0a at the branch states; FT.108(7)].

$(4)$ **Observables (Def-H.32(4) — internal bookkeeping labels; no identification).** A configuration carries chains [D1.4: ordered tuples of distinct real edges]: **closed** directed simple cycles $c$, length $L\ge2$; **open** directed simple paths, length $\ge2$. Readings:
$$
q(c,\sigma):=\frac{\sigma_{e_1}-\sigma_{e_k}}{2}\in\{-1,0,+1\}\quad[\mathrm{EM.9}\ \text{end registers};\ \mathrm{FT.40}\ \text{closed-core form at the tuple's own base};\ \mathrm{D3.4}],
$$
$$
S(c):\ \text{the on-shell winding }k(c)=\Theta(c)/2\in\mathbb Z\quad[\mathrm{FT.22},\ \mathrm{FT.25}(3)],\qquad
\text{minimal ladder}\ [\mathrm{FT.32}(6)]:\ \ L\ \text{even}\Rightarrow(\kappa\equiv1,\ k=L/2);\ \ L\ \text{odd}\Rightarrow(\kappa\equiv2,\ k=L);
$$
open chains carry $S=0$ (no closed core — bookkeeping label, $\neg$ a spin value; the $j=|k|/2$ map is Def-H.38-declared content and is *not* imported). A **chain instance** is a pair $(c,\text{base})$ (closed: base $=$ each of the $L$ cyclic starts; open: the tuple itself). The $\delta$-constraints of the sector sum are realized by summing over instances with the readings fixed.

$(5)$ **The sector partition functions.** For labels $(q,S)$ and budget $(B,B_K)$:
$$
Z^{\bullet}_{B}(q,S)\ :=\ \sum_{\Gamma\in\mathcal G_B}\ \sum_{R\in\mathfrak C_B(\Gamma)}\ \mathcal W^{\bullet}_\Gamma(R)\cdot\#\{(c,\text{base}):\ q(c,\sigma)\text{-sector}=q,\ S(c)=S\}\Big|_{\sigma\text{-resolved}},
$$
$\bullet\in\{\mathrm{amp},\mathrm{norm}\}$: the amplitude layer with $\sigma$ resolved inside the sector condition and $w$-weights; the norm layer with $|w|^2$-weights (closed form: $m_q\,2^{|R|-2}$ per instance, $m_q=(2,1,1)$ at $q=(0,\pm1)$ [FT.106(3)]). Both are exact polynomials in $\mathbb Z[t,u]$ per budget cell.

$(6)$ **The mass expectation (Def-H.32(6)).** For sectors with $Z^{\mathrm{norm}}_B(q,S)\ne0$:
$$
m^2_B(q,S)\ :=\ \frac{1}{Z^{\mathrm{norm}}_B(q,S)}\sum_{\Gamma,R}\ \mathcal W^{\mathrm{norm}}_\Gamma(R)\cdot\#\text{inst}(q,S;\Gamma,R)\cdot\Delta S(\Gamma,R),
$$
$$
\Delta S(\Gamma,R)\ :=\ 2\,n_{\mathcal V}(\Gamma,R)\,\bigl\langle|\delta\rho|^2\bigr\rangle_{\text{branch states}}\ =\ \tfrac32\,n_{\mathcal V}(\Gamma,R)\ =\ \tfrac32\bigl(2E(\Gamma)-|R|\bigr)\qquad[\mathrm{L4};\ \mathrm{L3}(1)\ \text{exact leading};\ \mathrm{n}_\mathrm{V}:=\#\text{virtual channels}],
$$
the branch-state values $|\delta\rho|^2=(\tfrac34,\tfrac1{12})$ (virtual $\Pi_{\mathcal V}$, real $\Pi_{\mathcal R}/3$) computed matrix-exact [FT.107(2)]; dimensionless nats [L3(4) species]; no coupling to $m_{\mathrm{pole}}/m_{\mathrm{hid}}$ (item 7 residue; Def-H.39's bridge slots unconstructed); the exact relative-entropy variant ($\ln4$ per virtual channel) is a specialization remark, not the read.

$(7)$ **The Janus move system and the transition operator (Def-H.32(7)).** States $s=(\Gamma,R)$, $\Gamma$ any finite simple graph on $\le B$ labelled nodes (the path space admits disconnected and edgeless states; $\mathcal G$-membership is imposed at the sector sums). Moves, with formal weights:
$$
J^+(e):\ R\mapsto R\cup\{e\},\ e\notin R\ [\text{weight }x_+];\qquad J^-(e):\ R\mapsto R\setminus\{e\}\ [\text{weight }x_-]\qquad[\mathrm{D1.2}:\ \text{one pair across A4 per event}];
$$
$$
N^+(v,S):\ \text{add node }v\text{ with }d=|S|\ge1\ \text{virtual edges to existing nodes}\ [\text{weight }y_d];
$$
$$
N^-(v):\ \text{remove node }v\text{ of degree }d\text{ together with its }r(v)\ \text{real edges}\ [\text{weight }z_d\,x_-^{r(v)};\ \mathrm{D1.2}:\ \text{reality is per pair}].
$$
$\hat U:=\sum_{\text{moves}}w\,|t\rangle\langle s|$ over the budget-truncated state space; $\langle s'|\hat U^n|s\rangle\in\mathbb Z[x_\pm,y_d,z_d]$; the topology sum of clause (5) and the transition sum $\sum_n\langle s'|\hat U^n|s\rangle$ are the static and dynamical faces of the same move content (FT.108).

### FT.108 — The Janus sum: move algebra, budget conservation, derived detailed balance, and the Tier F.35 boundary

**Thm.** Under Def-H.32:
$(1)$ **Move-label algebra.** The move classes carry CT0.7(4)'s aspect labels — $J^\pm\leftrightarrow F_{J^\pm}=\mathcal E_{-+}/\mathcal E_{--}$ (S-odd), node moves $\leftrightarrow$ the seal-generated topology change — and the frozen identities hold matrix-exact over $\mathbb Q(i)$ on the label algebra: $[\Sigma,J_i]=4iK_i$, $[\Sigma,K_i]=-4iJ_i$ [CT1.5]; $\{\mathbb S,J_i\}=0=\{\mathbb S,K_i\}$ [CT0.7(3)].
$(2)$ **Budget conservation (the coarse-grained invariant).** The grade map $\mathrm{gr}:(\Gamma,R)\mapsto\bigl(V,\,E_{\mathrm{pot}},\,|R|\bigr)$ is a homomorphism of the move system: every monomial $x_+^{a_+}x_-^{a_-}\prod y_d^{m_d}\prod z_d^{n_d}$ of $\langle s'|\hat U^n|s\rangle$ satisfies
$$
a_+-a_-=|R'|-|R|;\qquad \textstyle\sum_d m_d-\sum_d n_d=V'-V;\qquad \sum_d d\,(m_d-n_d)=E'_{\mathrm{pot}}-E_{\mathrm{pot}}
$$
— exhaustive on every path monomial at $n\le3$ from every $V\le2$ source [machine]. Node dissolution carries its incident real edges' own $J^-$ factors [D1.2]: $z_d\,x_-^{r(v)}$ — without them the grade map fails (witnessed).
$(3)$ **Path counts (two enumerators).** Operator iteration and depth-first path enumeration agree coefficient-wise on $\hat U^n$, $n\le4$; witness: $\langle\text{digon},R{=}E\,|\,\hat U^3\,|\,\bullet\rangle=2\,x_+^2y_1+\cdots$ — the two admissible move orderings [machine].
$(4)$ **Detailed balance derived; the dictionary is a specialization.** The per-pair Janus dynamics [D1.2] on (virtual, real) has master generator $Q=\bigl(\begin{smallmatrix}-x_+&x_+\\ x_-&-x_-\end{smallmatrix}\bigr)$ over $\mathbb Z[x_+,x_-]$; $\ker Q$ is one-dimensional with span $(x_-,x_+)$ [exact: $(x_-,x_+)Q=0$; $\det Q=0\ne Q$] — the unique stationary measure, hence
$$
p\ =\ \frac{x_+}{x_++x_-}\qquad[\text{derived},\ \neg\text{imported}];
$$
the substitution $x_+=1-4\varepsilon_q$, $x_-=4\varepsilon_q$ gives $p=1-4\varepsilon_q$ identically [machine] — the fixed-topology ensemble parameter is a specialization of the derived stationary ratio, and the sealed universe-level balance $\#J^+=\#J^-$ [D1.3] is the balanced-sector restriction of $(2)$'s first identity.
$(5)$ **Resolvent structure.** On a single pair channel, $\sum_n\langle\varnothing|\hat U^n|\varnothing\rangle w^n=\dfrac{1}{1-w^2x_+x_-}$ in $\mathbb Q[w]/(w^{12})$ [machine: $(1-w^2x_+x_-)\cdot\sum\equiv1$ coefficient-wise] — the transition sum is a geometric resolvent with pole at $w^2x_+x_-=1$: an unbounded structural range direction in the formal fugacities, no value declared (P4-class datum absent; any numerical use requires a logged declaration first).
$(6)$ **The Tier F.35 boundary limit.** With node moves off ($y_d,z_d\mapsto0$) the state space decomposes into fixed-topology sectors, and on each sector $\Gamma_0$ the amplitude-layer cover generating function
$$
\Phi_{\Gamma_0}(t)\ :=\ \sum_{R\ \mathrm{cover}}v_{\Gamma_0}(R)^2\,t^{|R|}\ =\ \sum_kc_k16^kt^{2k}
$$
satisfies the exact polynomial identity
$$
q^{2E}\,\Phi_{\Gamma_0}\bigl(p/q\bigr)\ =\ W_{\Gamma_0}(p)\qquad[\text{coefficient-wise; machine on tetra/cube/octa against the frozen FT.68(1),(3)/FT.69(2) rows and on all nine live }V\le4\text{ cells}]
$$
— the fixed-topology tree layer of Def-H.31(2) [Tier F.35] is recovered identically; the lock refinement census at $(t,u)$: the tetrahedron's $16$ locked covers carry lock count $1$ each [FT.69(5) family]. Consequently the fixed-topology slice of the topology-blind integral carries Tier F.35's boundary data — its effective potential, four vacua, phase triple and FT.70 walls [FT.102–FT.104, under Def-H.31's interface definitions, cited as boundary content, not re-derived] — as the $y_d,z_d\to0$ restriction, per clause $(4)$'s specialization of $t$.
$(7)$ **Tilt spectral specialization.** At the branch states, $Z_\gamma=\mathfrak T(\rho e^{-\gamma\rho})$ [Cor L0a] evaluates exactly by spectral calculus: real branch $e^{-\gamma/3}$, virtual branch $e^{-\gamma}$; at $\gamma=1$: disjoint rational enclosures $e^{-1/3}\in[0.716531311,\ldots]$, $e^{-1}\in[0.367879441,\ldots]$, strict order enclosure-proven [machine].

### FT.109 — The diagonal seal commutator

**Thm.** Under CT1.7, with the CT1.2 basis $\{E_0,\Sigma,\hat E^{ij},W_i,J_i,K_i\}$:
$$(1)\quad\sum_{i=1}^{3}[J_i,K_i]=i\sum_{i=1}^{3}\bigl(\Sigma-E^{ii}\bigr)=i\bigl(3\Sigma-\Sigma\bigr)=2i\Sigma ;$$
$$(2)\quad\sum_{i=1}^{3}E^{ii}=\sum_{i=1}^{3}\sigma_i\otimes\sigma_i=\Sigma\qquad\bigl[E^{ii}=\tfrac12\bigl(\sigma_i\otimes\sigma_i+\sigma_i\otimes\sigma_i\bigr)=\sigma_i\otimes\sigma_i\bigr];$$
$$(3)\quad\text{basis read: in the 16-element CT1.2 basis the sum }\textstyle\sum_i[J_i,K_i]\text{ has exactly one nonzero component — the }\Sigma\text{ component, with coefficient exactly }2i;$$
$$(4)\quad 2i\Sigma\in\mathcal E_{++}\ \text{(the Higgs/gravity block)},\qquad 2i\Sigma\notin\operatorname{span}\{W_k\}.$$

### Def-H.41 — The bound-chain arena

**Def.** The **bound-chain arena** is the minimal counting space combining the two independently present structures of a bound chain $c$ [D1.4]:
$$
\mathcal H_c\ :=\ \mathcal H_{\mathrm{seal}}\otimes\mathcal H_{\mathrm{poly}},\qquad
\mathcal H_{\mathrm{seal}}:\ \text{the seal triplet at the chain's termini}\ [\mathrm{CT0.12},\ \mathrm{CT0.7}(4):\ F_{J^\pm}=\operatorname{span}\{J_i\}/\operatorname{span}\{K_i\},\ \dim=3],
$$
$$
\mathcal H_{\mathrm{poly}}:\ \text{the polygonal transfer structure along its length}\ [\mathrm{FT.68}(2):\ \text{the transfer rule}\ T(t);\ \operatorname{tr}T(1)=3];\qquad
\dim_{\mathrm{eff}}\mathcal H_c=3\times3=9\ \ [\mathrm{FT.110}(1)].
$$

### FT.110 — The bound-chain arena dimension

**Thm.** The bound-chain arena $\mathcal H_c$ is the tensor product of two independent $3$-dimensional structures:
$$(1)\quad\dim_{\mathrm{eff}}\mathcal H_c=\dim F_{J^\pm}\times\operatorname{tr}T(1)=3\times3=9;$$
$$(2)\quad\operatorname{tr}T(1)=3\qquad\bigl[\mathrm{FT.68}(2):\ \operatorname{charpoly}T(1)=x^2\bigl(x^2-3x-3\bigr)=x^4-3x^3-3x^2;\ \ \operatorname{tr}T(1)=-[x^3]\operatorname{charpoly}T(1)=3\bigr].$$

### FT.111 — The $C_3$ spectrum of the covariant seal bilinear

**Thm.** The mixed seal commutator $[J_i,K_j]$ is a bilinear in two seal triplets. Let $C_3$ be the cyclic permutation of the seal index, generated by the $SO(3)$ rotation by $2\pi/3$ about the $(1,1,1)$ axis — a subgroup of the $SO(3)$ under which $\{J_i\}$ and $\{K_i\}$ transform as vectors [CT1.8]; inner form: $U=u\otimes u$ with $u=\tfrac12\bigl(I_2-i(\sigma_1+\sigma_2+\sigma_3)\bigr)$, exact over $\mathbb Q(i)$: $U^3=I_4$, $UJ_iU^\dagger=J_{i+1}$, $UK_iU^\dagger=K_{i+1}$ (indices mod $3$). Then:
$$(1)\quad\text{bilinear}=\text{singlet}\oplus\text{doublet}:\ \ \text{the singlet is the}\ \Sigma\ \text{part (}C_3\text{-invariant); the doublet is the}\ \hat E^{ij}\ \text{part (}C_3\text{-cyclically permuted).}$$
Concretely: the diagonal triple $[J_i,K_i]/i=\Sigma-E^{ii}=\tfrac23\Sigma-\hat E^{ii}$ splits into the fixed direction $\Sigma$ and the zero-sum plane of $\bigl(\hat E^{11},\hat E^{22},\hat E^{33}\bigr)$ — $\sum_i\hat E^{ii}=0$ — on which the cyclic shift $P$ acts with minimal polynomial $x^2+x+1$, irreducible over $\mathbb Q$: the doublet.
$$(2)\quad\text{Democratic diagonalization: any}\ C_3\text{-covariant Hermitian operator on the triplet —}\ [H,P]=0,\ H^\dagger=H,\ P\ \text{the cyclic shift — has the form}$$
$$H=a\,I_3+z\,P+\bar z\,P^{T}\qquad(a\in\mathbb R,\ z\in\mathbb C),$$
$$\operatorname{spec}H:\quad\lambda_i=A+B\cos\bigl(\theta+2\pi i/3\bigr),\qquad i=0,1,2,\qquad A=a,\ \ B=2|z|,\ \ \theta=\arg z,$$
equivalently the depressed cubic $\ (\lambda-A)^3-\tfrac{3B^2}{4}(\lambda-A)-\tfrac{B^3}{4}\cos3\theta=0$.
$$(3)\quad\text{Normalization:}\ \ A=1\ \ \Bigl[\sum_i\lambda_i=3A=3=\dim F_{J^\pm}\Bigr];\qquad B=\sqrt2\ \ \Bigl[\sum_i(\lambda_i-A)^2=B^2\sum_i\cos^2(\theta+2\pi i/3)=B^2\cdot\tfrac32=3\implies B^2=2\Bigr];$$
$$\theta=\delta:\ \text{the mixing angle, determined in FT.112.}$$

### FT.112 — The mixing angle

**Thm.** The mixing angle of the $C_3$-covariant seal bilinear is the exact rational
$$\delta=\frac{\sum_i[J_i,K_i]\big|_\Sigma}{\dim F_{J^\pm}\cdot\operatorname{tr}T(1)}=\frac{2}{3\cdot3}=\frac29,$$
where the numerator $2$ is the scalar coefficient of the diagonal seal commutator [FT.109(3): $\sum_i[J_i,K_i]=2i\Sigma$] and the denominator $9$ is the bound-chain arena dimension [FT.110(1)].

### FT.113 — The bilinear spectrum and the mass-squared ratios

**Thm.** With $\delta=2/9$ [FT.112] and $A=1$, $B=\sqrt2$ [FT.111(3)], the three eigenvalues of the $C_3$-covariant bilinear are
$$r_i=1+\sqrt2\cos\Bigl(\frac29+\frac{2\pi i}{3}\Bigr),\qquad i=0,1,2,$$
with exact radical-trigonometric closed forms ($c=\cos\tfrac29$, $s=\sin\tfrac29$):
$$r_0=1+\sqrt2\,c;\qquad r_1=1-\frac{\sqrt2\,c+\sqrt6\,s}{2};\qquad r_2=1-\frac{\sqrt2\,c-\sqrt6\,s}{2};$$
$$\sum_{i}r_i=3;\qquad\sum_{i<j}r_ir_j=\frac32;\qquad 2(r-1)^3-3(r-1)-\sqrt2\cos\frac23=0\ \ \text{for each}\ r=r_i\ \ [3\delta=\tfrac23].$$
The mass-squared ratios are $r_i^2$. Ordered by magnitude — $r_1^2<r_2^2<r_0^2$, enclosure-proven —
$$m_1^2:m_2^2:m_3^2=r_{\min}^2:r_{\mathrm{mid}}^2:r_{\max}^2=r_1^2:r_2^2:r_0^2=1:\frac{r_2^2}{r_1^2}:\frac{r_0^2}{r_1^2},$$
$$\frac{r_2^2}{r_1^2}=206.770315972729\ldots,\qquad\frac{r_0^2}{r_1^2}=3477.472837104\ldots\qquad[\text{rational trigonometric enclosures, width}<2^{-50};\ \text{machine}].$$
The overall scale $\mu$ in $m_i^2=\mu\,r_i^2$ is undeclared (P4-class free internal parameter): the ratios are this tag's only content. The $m^2$ vocabulary is the corpus's own inertial read [L3(4), L4: dimensionless entropy deficit in nats; $\neg$a particle identification].

### FT.116 — The relabelling lattice, the two-level obstruction, and the $\varepsilon$-selection of $C_3$

**Thm.** On the slot carrier $\mathcal H^{(3)}_{\mathrm{slot}}\cong\mathbb C^3$ [CT3.2] with the classical relabelling embedding $P_\pi|i\rangle=|\pi(i)\rangle$, $(P_\pi)^i{}_j=\delta^i_{\pi(j)}$, $S_3\hookrightarrow U(3)$ [CT3.3]:
$$(1)\quad S_3\ \text{has exactly six subgroups, of orders}\ (1,2,2,2,3,6):\ \{e\},\ \text{three}\ \mathbb Z_2=\langle\text{transposition}\rangle,\ A_3\cong C_3,\ S_3\qquad[\text{machine: closure of all}\ 2^6\ \text{generator subsets}];$$
$$(2)\quad\textbf{commutant dimensions}\ (\text{Hermitian real form}):\qquad\{e\}\mapsto9,\qquad\mathbb Z_2\mapsto5,\qquad C_3\mapsto3,\qquad S_3\mapsto2;$$
$$(3)\quad C_3\text{-commutant}=\{aI_3+zP+z^{*}P^{T}:\ a\in\mathbb R,\ z\in\mathbb C\}\ (P=P_{(123)}),\qquad S_3\text{-commutant}=\operatorname{span}\{I_3,J\}\ (J=\text{all-ones});$$
$$(4)\quad\textbf{the two-level obstruction:}\ \ \operatorname{spec}(aI_3+bJ)=\{a+3b,\ a,\ a\}\ \text{exactly}\ \forall(a,b)\in\mathbb R^2\ (P_\pi\text{-covariance }\Rightarrow\text{ at most two distinct eigenvalues});$$
$$(5)\quad\textbf{reflection rigidity:}\ \ THT=H\ \text{for a transposition}\ T\iff z\in\mathbb R\qquad[THT=aI_3+zP^{T}+z^{*}P:\ \text{conjugation by a transposition inverts the}\ 3\text{-cycle}];$$
$$\operatorname{disc}=108\,(\operatorname{Im}z^3)^2=108\,(\operatorname{Im}z)^2\bigl(3(\operatorname{Re}z)^2-(\operatorname{Im}z)^2\bigr)\ \text{vanishes}\iff z^3\in\mathbb R\iff\arg z\in\tfrac\pi3\mathbb Z\qquad[\text{the degeneracy locus: three lines through the origin}];$$
$$S_3\text{-covariance forces}\ z\in\mathbb R\ (\arg z\in\{0,\pi\})\subset\tfrac\pi3\mathbb Z\implies\text{every}\ S_3\text{-covariant circulant has a double root};\ \text{a three-line spectrum requires}\ \operatorname{Im}z^3\ne0,\ \text{i.e.}\ S_3\text{-covariance must be broken to the cyclic subgroup};$$
$$(6)\quad\textbf{the}\ \varepsilon\textbf{-selection:}\ \ \varepsilon_{ijk}P^i{}_aP^j{}_bP^k{}_c=\det(P_\pi)\,\varepsilon_{abc}=\operatorname{sgn}(\pi)\,\varepsilon_{abc}\ \forall\pi\in S_3\ [\mathrm{CT3.15}\ \text{on permutation matrices}];\qquad\det P_\pi=\operatorname{sgn}(\pi);$$
$$\operatorname{Stab}_{S_3}(\varepsilon)=\{\pi:\det P_\pi=1\}=A_3=C_3=S_3\cap SU(3);\qquad\text{the}\ \varepsilon\text{-preserving subgroups are exactly}\ \{e\}\subset A_3,\ \text{so}\ A_3\ \text{is the unique maximal one};$$
$$(7)\quad\textbf{seal-side companion census:}\ \ \text{on the seal triplet,}\ T\cong A_4\ (|T|=12,\ T\subset SO(3))\ \text{has commutant}\ \mathbb R\cdot I_3\ (\text{full degeneracy});\ \ V_4\ \text{has commutant the diagonal matrices}\ (3\ \text{parameters, no cyclic relation});\ \ C_3\ \text{(the}\ 2\pi/3\ \text{rotation about}\ (1,1,1)\ [\mathrm{CT1.8}])\ \text{has commutant the circulants}\ (3\ \text{parameters, fixed democratic eigenvectors}).$$

### FT.117 — Confinement blindness: the one-body no-go on colour-sealed singlets

**Thm.** Let $H\in\mathfrak H(\mathbb C^3)$ be any Hermitian slot operator, and let $\varepsilon_{ijk}$, $\delta^i{}_j$ be the two sealing tensors [CT3.17]:
$$(1)\quad\textbf{baryon singlet:}\qquad\bigl(H\otimes I_3\otimes I_3+I_3\otimes H\otimes I_3+I_3\otimes I_3\otimes H\bigr)_{(ijk),(lmn)}\,\varepsilon_{lmn}=\mathfrak T(H)\,\varepsilon_{ijk};$$
$$\text{equivalently}\quad\sum_l\bigl(H_{il}\varepsilon_{ljk}+H_{jl}\varepsilon_{ilk}+H_{kl}\varepsilon_{ijl}\bigr)=\mathfrak T(H)\,\varepsilon_{ijk}\qquad[\text{all}\ 27\ \text{components, exact};\ \mathrm{CT3.16}\ \text{at finite generators}];$$
$$(2)\quad\textbf{covariant specialization:}\ \ H=aI_3+zP+z^{*}P^{T}\ [\mathrm{FT.116}(3)]:\qquad\mathfrak T(H)=3a\implies\text{the one-body baryon eigenvalue is}\ 3a,\ \textbf{independent of}\ (|z|,\arg z);$$
$$\text{hence the}\ C_3\text{-doublet content}\ B=2|z|,\ \theta=\arg z\ \text{— the entire family-splitting datum of FT.111(2)}\text{— is annihilated on the baryon singlet};$$
$$(3)\quad\textbf{meson singlet:}\qquad\bigl(H\otimes I_3-I_3\otimes H^{T}\bigr)\,\delta=H\cdot I_3-I_3\cdot H=0\qquad\forall H\ (\textbf{including the trace part});$$
$$(4)\quad\textbf{visibility locus:}\ \ [H,E_{12}]\ne0\ \text{for}\ H=0\cdot I_3+(1+i)P+(1-i)P^{T}:\ \text{the same covariant data are nonzero on the adjoint channel — but the adjoint is not a sealed singlet, so it carries no pole}\ [\mathrm{CT3.18};\ \mathrm{CT3.22}:\ \text{isolated colour has norm}\ 0];$$
$$(5)\quad\textbf{invariant census:}\qquad\dim\bigl(\mathbb C^3\otimes\mathbb C^3\otimes\mathbb C^3\bigr)^{\mathfrak{sl}(3)}=1\ \text{spanned by}\ \varepsilon_{ijk};\qquad\dim\bigl(\mathbb C^3\otimes\bar{\mathbb C}^3\bigr)^{\mathfrak{sl}(3)}=1\ \text{spanned by}\ \delta^i{}_j;$$
$$(6)\quad\textbf{Casimir spectrum:}\ \ C:=\tfrac12\bigl(\sum_{ij}\rho(E_{ij})\rho(E_{ji})-\tfrac13\rho(\textstyle\sum_iE_{ii})^2\bigr)\ \text{on}\ \mathbb C^3\otimes\mathbb C^3\otimes\mathbb C^3\ \text{satisfies}\ C(C-3)(C-6)=0,$$
$$\operatorname{spec}C=\{0,3,6\}\ \text{with multiplicities}\ (1,16,10)\ \text{from}\ (\operatorname{tr}C,\operatorname{tr}C^2)=(108,504):\qquad27=1\oplus(8\oplus8)\oplus10;\qquad C\big|_{\mathbb C^3}=\tfrac43\ (\text{normalization pin});$$
$$(7)\quad\textbf{verdict (obstruction, derived):}\ \ \text{no colour-sealed object — baryon or meson — can carry a one-body}\ C_3\text{-covariant mass splitting: the baryon reads only the singlet coefficient}\ 3a,\ \text{the meson reads nothing.}\ \text{The three-line spectrum of the channel is readable only on the triplet-attached chain itself}\ [\mathrm{D3.8}],\ \text{whose colour factor is present but unsealed.}$$

### Def-H.42 — The colour-dressed arena

**Def.** A triplet-attached bound chain [D3.8] carries, simultaneously and independently: the seal triplet at its termini [CT0.12, CT0.7(4)], the polygonal transfer structure along its length [FT.68(2)], and the colour slot at its attachment [CT3.2: $\mathbb C^3$]. The **colour-dressed arena** is their minimal combined counting space:
$$
\mathcal H_c^{(q)}\ :=\ \mathcal H_c\otimes\mathbb C^3_{\mathrm{slot}}\qquad[\mathrm{Def\text{-}H.41}],\qquad
\dim_{\mathrm{eff}}\mathcal H_c^{(q)}=3\times3\times3=27\ \ [\mathrm{FT.118}(2)],
$$
entering exactly once — as the denominator of the triplet-attached mixing angle [FT.119: $\delta_q=\tfrac2{27}$ with FT.118(4)'s spectator numerator $2$]. Singlet-sealed chains keep Def-H.41's $9$: the invariant lines of a sealed object are $1$-dimensional [FT.117(5)], so its colour factor is $1$.

### FT.118 — The colour-dressed arena and the spectator numerator

**Thm.** With the transfer rule $T(1)[s][s']=[\,|s|+|s'|\le3\,]$, $s,s'\in\{0,1\}^2$ [FT.68(2)], re-derived at the point of use:
$$(1)\quad\operatorname{tr}T(1)=3\qquad[\text{the single excluded diagonal pair is}\ (|s|,|s'|)=(2,2)];\qquad\operatorname{charpoly}T(1)=x^4-3x^3-3x^2=x^2\bigl(x^2-3x-3\bigr)\ [\mathrm{FT.68}(2);\ \text{machine: Faddeev–LeVerrier over}\ \mathbb Z];$$
$$(2)\quad\textbf{the colour-dressed arena:}\qquad\dim_{\mathrm{eff}}\mathcal H_c^{(q)}=\dim F_{J^\pm}\times\operatorname{tr}T(1)\times N_{\text{colour}}=3\times3\times3=27,$$
$$\text{the third factor being}\ N_{\text{colour}}=3=\log_2C_{\mathrm{cap}}-1=\log_216-1\ [\mathrm{CT3.20};\ \mathrm{CT0.5},\ \mathrm{CT0.6},\ \mathrm{CT0.11}];\qquad\text{scope: triplet-attached chains}\ [\mathrm{D3.8}];$$
$$(3)\quad\textbf{sealed attachments do not dress:}\qquad\text{colour factor of a sealed object}=1\ [\mathrm{FT.117}(5):\ \text{the invariant lines are}\ 1\text{-dimensional}]\implies\dim_{\mathrm{eff}}\mathcal H_c^{\mathrm{sealed}}=3\times3\times1=9\ [\mathrm{FT.110}(1)\ \text{recovered}];$$
$$(4)\quad\textbf{the spectator numerator:}\qquad\sum_{i=1}^{3}\bigl[J_i\otimes I_3,\ K_i\otimes I_3\bigr]=\Bigl(\sum_i[J_i,K_i]\Bigr)\otimes I_3=2i\,\Sigma\otimes I_3\qquad[12\times12\ \text{entrywise exact over}\ \mathbb Q(i);\ \mathrm{FT.109}\ \text{re-derived}];$$
$$(5)\quad\text{the diagonal coefficient of the colour-dressed seal commutator is therefore exactly}\ 2\ \text{— unchanged from}\ \mathrm{FT.109}(3):\ \text{colour is a spectator of the seal algebra}\ [\mathrm{EW.32}:\ T_a\mathsf v=0;\ \mathrm{CT0.12}\ \mathrm{Rmk}:\ \text{colour sits in an orthogonal stack block}];$$
$$(6)\quad\textbf{adjoint dressing (computed, NOT adopted):}\qquad\text{with}\ X^2=\textstyle\sum_aT_aT_a=C_FI_3=\tfrac43I_3\ [\text{machine: from the rational}\ E_{ij}\ \text{basis}]\ \text{and}\ [A\otimes X,\,B\otimes X]=[A,B]\otimes X^2,$$
$$\sum_i\bigl[J_i\otimes X,\ K_i\otimes X\bigr]=2i\,\Sigma\otimes X^2=\tfrac83\,i\,\Sigma\otimes I_3\implies\text{numerator}\ 2C_F=\tfrac83:\ \text{a different rational, and no corpus tag supplies the coupling};$$
$$(7)\quad\textbf{the two candidate mixing angles:}\qquad\delta_q=\frac{2}{27}\ \ (\text{spectator, adopted in FT.119});\qquad\frac{2C_F}{27}=\frac{8/3}{27}=\frac8{81}\ \ (\text{adjoint-dressed, logged not adopted}).$$

### FT.119 — The triplet-attached mixing angle $\delta_q=2/27$ and its spectrum

**Thm.** With the spectator numerator $2$ [FT.118(4)–(5)] over the colour-dressed arena $27$ [FT.118(2)], and the FT.111(3) normalization $A=1$, $B=\sqrt2$ (fixed by $\sum_i\lambda_i=3=\dim F_{J^\pm}$ and $\sum_i(\lambda_i-A)^2=3$, both seal-side and hence colour-blind):
$$(1)\quad\delta_q=\frac{2}{3\cdot3\cdot3}=\frac2{27}=0.074074074074\ldots\qquad[\text{exact rational};\ \text{machine}\ \S D];$$
$$(2)\quad3\delta_q=\delta_\ell=\frac29\qquad[\mathrm{FT.112}:\ \delta_\ell=\tfrac2{9}\ \text{from the undressed arena}\ 3\times3];$$
$$(3)\quad\textbf{the spectrum:}\qquad r^{(q)}_i=1+\sqrt2\cos\Bigl(\frac2{27}+\frac{2\pi i}3\Bigr),\qquad i=0,1,2,$$
$$\text{with}\ c=\cos\tfrac2{27},\ s=\sin\tfrac2{27}:\qquad r^{(q)}_0=1+\sqrt2\,c=2.410335463511094\ldots,$$
$$r^{(q)}_1=1-\frac{\sqrt2\,c+\sqrt6\,s}{2}=0.204193367808662\ldots,\qquad r^{(q)}_2=1-\frac{\sqrt2\,c-\sqrt6\,s}{2}=0.385471168680242\ldots;$$
$$\text{all three strictly positive}\ [\text{disjoint enclosures};\ \text{machine}]\ —\ \text{no sign branch, unlike the}\ \delta>\pi/12\ \text{regime};$$
$$(4)\quad\textbf{Vieta and the phase-free invariant:}\qquad\sum_ir^{(q)}_i=3,\qquad\sum_{i<j}r^{(q)}_ir^{(q)}_j=\frac32,\qquad\sum_i\bigl(r^{(q)}_i\bigr)^2=6,$$
$$2\bigl(r^{(q)}-1\bigr)^3-3\bigl(r^{(q)}-1\bigr)-\sqrt2\cos\frac29=0\quad\text{for each}\ r^{(q)}=r^{(q)}_i\qquad[\cos3\delta_q=\cos\tfrac29=\cos\delta_\ell:\ \text{clause}\ (2)\ \text{inside the cubic}];$$
$$Q\ :=\ \frac{\sum_im_i}{\bigl(\sum_i\sqrt{m_i}\bigr)^2}\ \overset{m_i=\mu (r^{(q)}_i)^2}{=}\ \frac{\sum_i(r^{(q)}_i)^2}{\bigl(\sum_ir^{(q)}_i\bigr)^2}=\frac6{9}=\frac23\qquad[\text{exact, and independent of}\ \delta\ \text{and of}\ \mu];$$
$$(5)\quad\textbf{the mass ratios}\ (m_i=\mu\,(r^{(q)}_i)^2,\ \mu\ \text{undeclared},\ \mathrm{P4}):\qquad(r^{(q)}_1)^2<(r^{(q)}_2)^2<(r^{(q)}_0)^2\ [\text{enclosure-proven}],$$
$$m_1:m_2:m_3=1:\frac{(r^{(q)}_2)^2}{(r^{(q)}_1)^2}:\frac{(r^{(q)}_0)^2}{(r^{(q)}_1)^2}=1:3.563695074946\ldots:139.3386880284\ldots\qquad[\text{widths}<2^{-50};\ \text{machine}];$$
$$(6)\quad\textbf{anchored forms}\ (\text{scale-free, top-normalized}):\qquad\frac{m_2}{m_3}=\frac{(r^{(q)}_2)^2}{(r^{(q)}_0)^2}=0.025575776012\ldots,\qquad\frac{m_1}{m_3}=\frac{(r^{(q)}_1)^2}{(r^{(q)}_0)^2}=0.007176757684\ldots;$$
$$(7)\quad\textbf{alternative-hypothesis table}\ (\text{computed, none adopted}):\qquad\delta=\tfrac2{81}\ (\text{per-baryon arena}\ 3\cdot27):\ 1:1.5130:84.316;$$
$$\delta=\tfrac1{36}=\tfrac2{72}\ (\text{arena}\ 9\ \text{dressed by the adjoint multiplicity}\ 8\ [\mathrm{CT3.13}]):\ 1:1.5939:86.746;\qquad\delta=\tfrac8{81}\ (\mathrm{FT.118}(6)\ \text{numerator over}\ 27):\ 1:5.6438:187.997.$$

### Def-H.33 — The chain orientation space and its chirality operator

**Def.** For a bound chain $c$ [D1.4: ordered tuple of distinct real edges $c=(e_1,\dots,e_k)$; D1.5: bound $=$ closed self-contained, fermionic content]:
- **Orientations.** $c$ and $\omega(c)$ [D2.6: $s(c)\leftrightarrow t(c)$, reversal of the traversal; $\omega^2=\mathrm{id}$]. As ordered tuples, $c\ne\omega(c)$ for every admissible $k\ge2$ [D1.4: distinct edges].
- **Orientation space.**
$$\mathcal H_\omega(c)\ :=\ \operatorname{span}_{\mathbb C}\bigl\{|c\rangle,\ |\omega(c)\rangle\bigr\}\ \cong\ \mathbb C^2,$$
with the Hermitian inner product making $\{|c\rangle,|\omega(c)\rangle\}$ an orthonormal basis.
- **Orientation involution.** $\hat\omega:\mathcal H_\omega\to\mathcal H_\omega$, $\hat\omega|c\rangle=|\omega(c)\rangle$, $\hat\omega|\omega(c)\rangle=|c\rangle$: then $\hat\omega^2=\mathrm{id}$, $\hat\omega^\dagger=\hat\omega$ [D2.6: $\omega$ is an involution].
- **Chirality operator (the exchange form).**
$$\boxed{\ \hat\chi\ :=\ i\bigl(|c\rangle\langle\omega(c)|-|\omega(c)\rangle\langle c|\bigr)\ }$$
- **Chiral projectors.** $P_L:=\tfrac12(\mathrm{id}+\hat\chi)$, $P_R:=\tfrac12(\mathrm{id}-\hat\chi)$.
- **Chiral eigenbasis.**
$$\boxed{\ |L\rangle=\tfrac1{\sqrt2}\bigl(|c\rangle-i\,|\omega(c)\rangle\bigr),\qquad |R\rangle=\tfrac1{\sqrt2}\bigl(|c\rangle+i\,|\omega(c)\rangle\bigr)\ }$$
— the $+1$ and $-1$ eigenvectors of $\hat\chi$ respectively; the labels are pinned by the boxed $\hat\chi$ together with $P_L:=\tfrac12(\mathrm{id}+\hat\chi)$ [FT.122(3), (6)].

### FT.122 — The orientation doublet is corpus-constructible

**Thm.** For every bound chain $c$ [D1.4, D1.5], the orientation space $\mathcal H_\omega(c)$, the involution $\hat\omega$, the chirality operator $\hat\chi$, and the projectors $P_L,P_R$ are constructible from Parts 1–2 data alone, with no new axiom and no declared parameter:
$$(1)\quad \hat\chi^\dagger=\hat\chi,\qquad \hat\chi^2=\mathrm{id},\qquad \operatorname{spec}\hat\chi=\{+1,-1\},\qquad\operatorname{tr}\hat\chi=0;$$
$$(2)\quad P_L^2=P_L,\quad P_R^2=P_R,\quad P_LP_R=0,\quad P_L+P_R=\mathrm{id},\quad \operatorname{tr}P_L=\operatorname{tr}P_R=1;$$
$$(3)\quad \hat\chi|L\rangle=+|L\rangle,\quad \hat\chi|R\rangle=-|R\rangle,\quad P_L|L\rangle=|L\rangle,\quad P_L|R\rangle=0,\quad P_R|R\rangle=|R\rangle,\quad P_R|L\rangle=0;$$
$$\text{equivalently, without the}\ \sqrt2\ \text{normalizers:}\quad2P_L=|L_u\rangle\langle L_u|,\ \ 2P_R=|R_u\rangle\langle R_u|\ \ \text{with}\ \ |L_u\rangle=|c\rangle-i|\omega(c)\rangle,\ |R_u\rangle=|c\rangle+i|\omega(c)\rangle\ \ [\text{exact over}\ \mathbb Q(i)];$$
$$(4)\quad\textbf{the covariance identities and the winding read:}\qquad\hat\omega\hat\chi\hat\omega^{-1}=-\hat\chi,\qquad\{\hat\chi,\hat\omega\}=0,\qquad\hat\omega P_L\hat\omega^{-1}=P_R,\qquad\hat\omega|L\rangle=-i|R\rangle,\quad\hat\omega|R\rangle=+i|L\rangle;$$
$$\text{for a materialized chain}\ c:\quad k(c)=\Theta(c)/2\in\mathbb Z\ [\mathrm{FT.22},\ \mathrm{FT.25}(3)];\qquad\omega:\ k\mapsto-k\ [\mathrm{D2.6};\ \mathrm{EM.24}(1):\ C\ \text{is}\ \omega\text{'s sign-level realization};\ \mathrm{FT.87}(8):\ \operatorname{sign}(k)\ \text{is}\ C\text{-odd}];$$
$$(5)\quad\text{the construction is exact over}\ \mathbb Q(i)\ \text{on all matrix elements in the basis}\ \{|c\rangle,|\omega(c)\rangle\}:\quad\hat\chi=i\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr),\quad\hat\omega=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr);$$
$$(6)\quad\textbf{canonicity:}\qquad\bigl\{M=M^\dagger\in\operatorname{End}(\mathcal H_\omega):\ \hat\omega M\hat\omega=-M,\ M^2=\mathrm{id},\ \langle c|M|c\rangle=\langle\omega(c)|M|\omega(c)\rangle=0\bigr\}=\{+\hat\chi,\ -\hat\chi\};$$
$$\text{without the diagonal-free condition the}\ \hat\omega\text{-odd Hermitian involutions are the circle}\ M(a,y)=\bigl(\begin{smallmatrix}a&iy\\-iy&-a\end{smallmatrix}\bigr),\ a^2+y^2=1\ \ [\text{exact rational witnesses incl.}\ (a,y)=(\tfrac35,\tfrac45),(\tfrac5{13},\tfrac{12}{13}),(\tfrac8{17},\tfrac{15}{17});\ \text{machine}];$$
$$(7)\quad\textbf{the kind flag (torsor distinction):}\qquad H^1(S^1;\mathbb Z_2)\cong\operatorname{Hom}(\mathbb Z,\mathbb Z_2)=\{h_{\mathrm R}:n\mapsto0,\ \ h_{\mathrm{NS}}:n\mapsto n\bmod2\},$$
$$\text{and the orientation-reversal pullback}\ n\mapsto-n\ \text{fixes both pointwise}\ (h(-n)=h(n)\ \text{in}\ \mathbb Z_2):\ \textbf{the spin-structure torsor is reversal-invariant, NOT exchanged};$$
$$\text{the}\ \hat\omega\text{-exchanged objects are the chiral rays of clause}\ (3)\text{: the torsor}\ \mathbb Z_2\ \text{(boundary conditions) and the ray}\ \mathbb Z_2\ \text{(the}\ \hat\chi\text{-grade) are distinct kinds}\ [\mathrm{FT.89}(2)\ \text{discipline}];\ \text{the R/NS analogy is recorded, never load-bearing}.$$

### Def-H.34 — The extended carrier basis, the chiral transform, and the partner involution

**Def.** For a bound chain $c$ [D1.4: ordered tuple of distinct real edges; D1.5: bound $=$ closed self-contained, fermionic content]:
- **Extended carrier (constitutive carrier clause).** $\mathcal H_{\mathrm{ext}}:=\mathcal H_{\mathrm{int}}\otimes\mathcal H_\omega(c)\cong\mathbb C^2\otimes\mathbb C^2\cong\mathbb C^4$, with $\mathcal H_{\mathrm{int}}=\mathcal H_{\mathsf v}$ the seed carrier, orthonormal basis $\{|\mathsf v\rangle,|\mathsf v^\perp\rangle\}$ [EW.32; the complement ray is a basis convention — all statements below are basis-covariant], and $\mathcal H_\omega$, $\hat\omega$, $\hat\chi$, $P_{L/R}$, $|L\rangle$, $|R\rangle$ as in Def-H.33.
- **Ordered orientation basis** (internal-major Kronecker order; composite index $=2\cdot\mathrm{int}+\omega$):
$$|1\rangle:=|\mathsf v\rangle\otimes|c\rangle,\qquad|2\rangle:=|\mathsf v\rangle\otimes|\omega(c)\rangle,\qquad|3\rangle:=|\mathsf v^\perp\rangle\otimes|c\rangle,\qquad|4\rangle:=|\mathsf v^\perp\rangle\otimes|\omega(c)\rangle.$$
- **Chiral carrier basis.** $\{|\mathsf v\rangle\otimes|L\rangle,\ |\mathsf v\rangle\otimes|R\rangle,\ |\mathsf v^\perp\rangle\otimes|L\rangle,\ |\mathsf v^\perp\rangle\otimes|R\rangle\}$, with $|L\rangle=\tfrac1{\sqrt2}(|c\rangle-i|\omega(c)\rangle)$, $|R\rangle=\tfrac1{\sqrt2}(|c\rangle+i|\omega(c)\rangle)$ [Def-H.33].
- **The $S$-transform.** $S:=\bigl(\begin{smallmatrix}1&1\\-i&i\end{smallmatrix}\bigr)$ (columns $=$ unnormalized chiral kets): $S^\dagger S=2I_2$; $U:=I_2\otimes S$; the conjugation $M\mapsto\tfrac12U^\dagger MU$ is exact over $\mathbb Q(i)$ and rotates the $\omega$-factor Pauli images cyclically:
$$\hat\omega\ (\sigma_1)\ \mapsto\ -\sigma_2,\qquad\hat\chi\ (-\sigma_2)\ \mapsto\ \sigma_3,\qquad\hat\kappa\ (\sigma_3)\ \mapsto\ \sigma_1.$$
- **Partner involution.** $\hat\kappa:=|c\rangle\langle c|-|\omega(c)\rangle\langle\omega(c)|$ — the unique diagonal $\hat\omega$-odd Hermitian involution up to sign [FT.122(6)'s circle at $(a,y)=(\pm1,0)$; machine]. Quaternionic triple with Def-H.33's operators:
$$\hat\omega^2=\hat\chi^2=\hat\kappa^2=\mathrm{id};\qquad\{\hat\omega,\hat\chi\}=\{\hat\chi,\hat\kappa\}=\{\hat\kappa,\hat\omega\}=0;\qquad\hat\omega\hat\chi=-i\hat\kappa,\quad\hat\chi\hat\kappa=-i\hat\omega,\quad\hat\kappa\hat\omega=-i\hat\chi.$$
- **Force-profile and read data.** $\mathbf c=(c_0,c_1,c_2,c_3)\in\mathbb Q^4$: the weak-transport profile of the chain over the seed generator set $\{W_1,W_2,W_3,Y\}$ [EW.33's $c_A$; EW.32's images] — configuration data, formal indeterminates in the Def-H.32(3) discipline, never fitted [P1, P4];
$$h(\mathbf c)=\tfrac12\sum_{a=0}^{3}c_a\,\sigma_a\qquad(\sigma_0:=I_2);\qquad|\mathbf c|^2:=c_1^2+c_2^2+c_3^2;$$
$q:=q_{\mathrm{core}}(c)\in\{-1,0,+1\}$: the ternary core-charge read of the oriented chain [D3.4, EM.9, FT.40] — registration data, $\omega$-odd [FT.40].

### FT.123 — Weak covariance and $\omega$-covariance on the extended carrier

**Thm.** Under Def-H.34's constitutive carrier clause, the matter carrier of a bound chain extends from the seed $\mathcal H_{\mathsf v}\cong\mathbb C^2$ [EW.32] to $\mathcal H_{\mathrm{int}}\otimes\mathcal H_\omega(c)$, with the weak action on the first factor alone, $W_i\mapsto\tfrac12\sigma_i\otimes I_\omega$ [EW.32], and the chiral grade on the second alone:
$$(1)\quad\textbf{weak covariance:}\qquad[W_i\otimes I_\omega,\ I_{\mathrm{int}}\otimes P_{L/R}]=0\qquad\forall i\in\{1,2,3\};$$
$$\textbf{locus sharpening:}\ \ \sum_i\bigl(\tfrac12\sigma_i\otimes I_2\bigr)^2=\tfrac34I_4\ (\text{type}\ 2\oplus2,\ \text{multiplicity}\ 2),\quad\text{while on the pair register}\ \sum_iW_i^2=2\Pi_{\mathcal R}\ (\text{type}\ 3\oplus1)\ [\text{Cor CT0.7a}]:$$
$$\text{the two weak actions are inequivalent}\ (\tfrac34I_4\ne2\Pi_{\mathcal R},\ \text{machine}),\ \text{so FT.93}(3)\text{'s pincer classifies the pair-register action and places no constraint here};$$
$$\mathrm{FT.93}(3d)\text{'s seed irreducibility}\ (\{m:[m,\sigma_i]=0\}=\mathbb CI_2)\ \text{is discharged by multiplicity, not violated:}\ \{M:[M,\sigma_i\otimes I_2]=0\ \forall i\}=I_{\mathrm{int}}\otimes\operatorname{End}(\mathcal H_\omega),\ \dim_{\mathbb C}=4\ [\text{machine}];$$
$$(2)\quad\textbf{the}\ \hat\omega\textbf{-covariance:}\qquad(I\otimes\hat\omega)\,(I\otimes P_L)\,(I\otimes\hat\omega)^{-1}=I\otimes P_R,\qquad(I\otimes\hat\omega)\,(I\otimes\hat\chi)\,(I\otimes\hat\omega)^{-1}=-(I\otimes\hat\chi);$$
$$(3)\quad\textbf{the weight-cardinality correspondence}\ [\text{conditional on Def-H.38}]:\ \ \text{a materialized chain of winding}\ k\ [\mathrm{FT.22},\ \mathrm{FT.25}(3)]\ \text{carries}\ \mathrm{Sym}^{k}(\mathcal H_{\mathsf v})\ \text{with weights}\ j,j{-}1,\dots,-j,\ j=|k|/2\ [\text{Def-H.38};\ \mathrm{FT.60}(3)\ \text{ladder}];$$
$$\text{the floor fermion}\ (\text{digon},\ k=1\ [\mathrm{FT.28}])\ \text{has}\ j=\tfrac12:\ \text{exactly two weights}\ \{+\tfrac12,-\tfrac12\}\ [\text{machine}]\ —\ \text{an unordered-pair cardinality correspondence with the two chiral rays}\ \{+1,-1\};$$
$$\text{the label-to-weight attachment is}\ \textbf{not derived}\ (\text{deficit}\ 1');\qquad\text{``chirality}=\text{helicity on-shell'' is marked external vocabulary — the corpus derives no dispersion relation, and transit-side helicity reads}\ [\mathrm{EM.8}]\ \text{are outside the bound scope}\ [\text{Def-H.38 scope note}];$$
$$(4)\quad\textbf{massive modes (structural):}\ \ \text{the}\ \hat\chi\text{-eigenspaces are defined for any mode; helicity is a frame-dependent refinement}\ [\text{math}];\ \text{on a massive mode chirality and helicity are distinct — the Dirac pattern};$$
$$(5)\quad\dim\bigl(\mathcal H_{\mathrm{int}}\otimes\mathcal H_\omega\bigr)=2\times2=4:\ \text{the Dirac-type carrier dimension of one massive mode (two Weyl halves)};\qquad\text{a weak doublet of Dirac-type carriers is}\ 2\times4=8.$$

### FT.124 — The prior obstructions do not reach the orientation space

**Thm.** The obstructions of Tiers F.26–F.28–Tiers F.31–F.34 and Tier F.38 are theorems about their own loci; the orientation-space chirality lives on a different space and evades each one — seven loci, census exact:
$$(1)\quad\textbf{the pincer}\ [\mathrm{FT.93}(3)]:\ \ \text{the classification}\ \{M:[M,W_i]=0\}=\operatorname{span}_{\mathbb C}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\},\ \{M:\{M,W_i\}=0\}=\mathbb C\cdot\Pi_{\mathcal V}\ \text{is a classification inside}\ \operatorname{End}(\mathbb C^4_{\mathrm{pair}})\ \text{for the pair-register weak action};$$
$$\mathcal H_\omega(c)\not\subseteq\operatorname{End}(\mathbb C^4_{\mathrm{pair}});\qquad\text{the extended weak action is inequivalent}\ \bigl(\tfrac34I_4\ \text{vs}\ 2\Pi_{\mathcal R}\ [\mathrm{FT.123}(1)]\bigr);\qquad I\otimes P_{L/R}\ \text{commutes with}\ W_i\otimes I_\omega\ \text{by tensor-factor disjointness, not by membership in either pincer class};$$
$$(2)\quad\textbf{the per-frame refutation}\ [\mathrm{FT.93}(4)]:\ \ \text{it concerns pair-register frame projectors}\ P^{(\mathcal F)}_\pm\ (\operatorname{rank}2\ \text{vs the}\ 1\text{-dimensional weak kernel}\ \wedge^2);\ \ \text{on the extended carrier the weak kernel is}\ \{0\}\ (\sigma_i\ \text{invertible};\ \text{machine}):$$
$$P^{\mathrm{car}}_{L/R}\ \text{are not frame projectors, and their halves are weak-blind, not weak-inactive — the refutation is silent here};$$
$$(3)\quad\textbf{the trace/rank obstruction}\ [\mathrm{FT.101}(3)]:\ \ \text{data re-derived:}\ \mathfrak T\Pi_{\mathcal R}=3\ne1=\mathfrak T\Pi_{\mathcal V};\ \text{no traceless involution in}\ \operatorname{span}\{\Pi_{\mathcal R},\Pi_{\mathcal V}\}\ (\operatorname{tr}=3a+b\in\{\pm4,\pm2\},\ \text{machine});$$
$$\hat\omega\ \text{is an honest matrix involution on}\ \mathcal H_\omega\ —\ \text{not a Hilbert-space implementation of the A4 branch flip, which stays label-level; FT.101}(3)\ \text{stands untouched on its locus};$$
$$(4)\quad\textbf{S-parity misalignment}\ [\mathrm{FT.93}(6)]:\ \ \text{catalog re-run (machine):}\ 30\ \text{frames},\ \gamma_{\mathcal F}=\pm\ \text{one Pauli product each, all}\ 15\ \text{sign-classes attained}\ \times2;\ \text{every class fails the commuting side for some}\ W_i\ \textbf{and}\ \text{the anticommuting side for some}\ W_i;$$
$$\text{exactly}\ 3\ \text{classes are}\ S\text{-aligned}\ (\pm\sigma_i\otimes\sigma_i);\qquad[\mathbb S\otimes I_2,\ I_4\otimes\hat\chi]=0\ (8\times8\ \text{machine}):\ \text{the chiral grade is}\ S\text{-invariant by disjointness — no misalignment can arise};$$
$$(5)\quad\textbf{the zero-expectation theorem}\ [\mathrm{FT.95}(3)]:\ \ \langle\psi|\hat\chi|\psi\rangle=0\ \text{for every}\ \hat\omega\text{-symmetric}\ \psi\ (\text{machine})\ —\ \text{recorded, not an obstruction:}\ \hat\chi\ \text{is a per-chain eigenvalue datum},\ \text{and the corpus's own precedent is FT.87}(8)\text{'s}\ \operatorname{sign}(k),$$
$$\text{a legitimate}\ C\text{-odd coordinate under the same vanishing theorem; a chiral read requires an oriented chain (boundary datum), not an ensemble average}\ [\text{Def-H.33 closing Rmk}];$$
$$(6)\quad\textbf{confinement blindness}\ [\mathrm{FT.117};\ \mathrm{CT3.22}]:\ \ \hat\chi\ \text{has no colour-slot argument:}\ [H_{\mathrm{slot}}\otimes I_2,\ I_3\otimes\hat\chi]=0\ \text{for every Hermitian slot operator}\ H\ (6\times6\ \text{machine witness});\ \text{sealed or not, the orientation factor persists};$$
$$(7)\quad\textbf{the}\ Q\textbf{-phase-free bound}\ [\mathrm{FT.119}(4)]:\ \ Q=\tfrac23\ \text{is the seal-side normalization content}\ (A=1,B=\sqrt2);\ \hat\chi\ \text{is a chain-level grade: the}\ C_3\ \text{structures of Tier F.37 live on the seal triplet and are untouched}.$$

### FT.125 — The deficit ledger: deficit 1 closed at the projector level; deficit 1$'$ opened

**Thm.** Under Def-H.33 and FT.122–FT.124 (and the chain-carrier lift of FT.126):
$$(1)\quad\textbf{Item 20 deficit 1 (chirality projector) — CLOSED at the projector level}\ (\text{under Def-H.34}).\ \ P_L,P_R\ \text{are corpus-constructible on}\ \mathcal H_\omega(c);\ \text{they satisfy every defining property}\ —\ \text{idempotent, orthogonal, complete, rank}\ 1\ [\mathrm{FT.122}(2)],\ \text{weak-commuting on the extended carrier}\ [\mathrm{FT.123}(1)],\ \hat\omega\text{-exchanged}\ [\mathrm{FT.123}(2)]\ —\ \text{and D2.6's vocabulary clause is an operator identity}\ [\mathrm{FT.122}(4)].$$
$$\textbf{Residue:}\ \text{item 21(i)'s frame section}\ e\mapsto\mathcal F_e,\ \text{its coupling to the EW.32 transport, and a global Dirac-type operator on the emergent geometry remain unconstructed — Tier F.39 supplies the extended carrier and its grade, not the section};$$
$$(2)\quad\textbf{Item 20 deficit 5 (gauge anomalies) — blocker RELOCATED, not removed.}\ \ \mathrm{FT.81}(4)\ \text{names three prerequisites: a chiral projector, a Weyl symbol, a hypercharge-assignment read. Tier F.39 discharges only the first. The anomaly sums}\ \bigl(\sum Y,\ \sum Y^3,\ [\mathrm{SU}(3)]^2\mathrm U(1),\ [\mathrm{SU}(2)]^2\mathrm U(1)\bigr)\ \text{are formable for any}\ \textbf{declared}\ \text{chiral assignment; no corpus-internal statement is possible until deficits}\ 1'\ (+2/3)\ \text{close};$$
$$(3)\quad\textbf{Item 20 deficit 6 (the neutrino row) — PARTIALLY UNBLOCKED, precisely:}\ \ \operatorname{im}P_R\ \text{is a constructible right-handed Weyl-type carrier}\ [\mathrm{Def\text{-}H.33}];\ \text{species content remains absent (deficits 2/3 stand) — whether the corpus spectrum contains such a state is a separate, still-unposed question};$$
$$(4)\quad\textbf{NEW deficit 1' (chiral matter assignment).}\ \ \text{Which species sits in which gauge representation on which chiral ray is not derived. The SM pattern}\ —\ \text{left}\ \mathrm{SU}(2)_L\ \text{doublets, right singlets}\ [\mathrm{FT.81}(2)]\ —\ \text{requires a rule correlating the}\ \hat\chi\text{-grade with the gauge representation and with the weak coupling itself}\ [\mathrm{FT.123}\ \text{Phys: the grade here is weak-blind}].\ \text{The algebraic}\ L/R\ \text{naming is fixed by the same rule}\ [\mathrm{FT.122}(6);\ \text{Def-H.33 canonicity Rmk}];$$
$$(5)\quad\textbf{Item 20 deficit 11 (spin–statistics) — UNCHANGED.}\ \ \text{A single-chain chiral grade is not an exchange operator on two-chain states; FT.80}(5)\text{'s inventory still contains no exchange operator. Equating the grade's}\ \mathbb Z_2\ \text{with the permutation sign's}\ \mathbb Z_2\ \text{is a kind confusion, barred by the FT.89}(2)\ \text{discipline}\ —\ \text{the same species as the torsor/ray distinction of FT.122}(7);$$
$$(6)\quad\textbf{the rest of the ledger:}\ \ \text{deficits}\ 2\ (\text{Yukawa}),\ 3\ (\text{generations/flavour}),\ 4\ (\text{CKM/PMNS})\ \text{remain open, now downstream of}\ 1'\ \text{rather than of}\ 1;\qquad\text{deficits}\ 7,8,9,10,12\ \text{unchanged}\ [\mathrm{FT.124}(6)\text{–}(7):\ \text{the mass ceilings are properties of the pole-side and colour-side reads}];$$
$$(7)\quad\textbf{the reversal accounting:}\ \ \text{every prior obstruction tag remains frozen and valid on its own locus}\ [\mathrm{FT.124},\ \text{clause by clause}];\ \text{no result of Tiers F.1–F.11–Tier F.38 is overturned — the closure is by relocation, not by refutation}.$$

### FT.126 — Weak-covariant chiral projectors on the chain carrier

**Thm.** Combining FT.123's tensor-factor separation with the branch-grading locus of FT.101: the orientation-space chirality lifts to the chain-carried Dirac-type carrier $\mathcal H_{\mathrm{int}}\otimes\mathcal H_\omega(c)$:
$$(1)\quad P_{L/R}^{\mathrm{car}}\ :=\ I_{\mathrm{int}}\otimes P_{L/R}:\qquad(P^{\mathrm{car}}_{L/R})^2=P^{\mathrm{car}}_{L/R},\qquad P^{\mathrm{car}}_LP^{\mathrm{car}}_R=0,\qquad P^{\mathrm{car}}_L+P^{\mathrm{car}}_R=\mathrm{id},\qquad\operatorname{tr}P^{\mathrm{car}}_{L/R}=2;$$
$$(2)\quad[W_i\otimes I_\omega,\ P^{\mathrm{car}}_{L/R}]=0\ \ \forall i\qquad[\text{the weak isospin acts chirality-blind}];$$
$$(3)\quad\text{each Weyl half}\ \operatorname{im}P^{\mathrm{car}}_{L/R}\ \text{carries exactly one chiral ray of the orientation factor and the full internal seed action (weak-blind, not weak-inactive:}\ \bigcap_i\ker(W_i\otimes I_\omega)=\{0\}\ \text{[machine])};$$
$$(4)\quad\textbf{independence of the two}\ \mathbb Z_2\textbf{'s:}\ \ \text{the A4 branch grading of FT.101 is label-level registration data}\ [\mathrm{FT.101}(3):\ \text{no Hilbert-space implementation on the pair register}];\ \text{the chiral grading is an implemented involution on the orientation factor. Any internal involution}\ G\otimes I_\omega\ \text{commutes with}\ I_{\mathrm{int}}\otimes\hat\omega\ \text{and their product is a third, distinct involution:}\ \mathbb Z_2\times\mathbb Z_2\ [\text{machine on}\ G\in\{\sigma_3,\sigma_1\};\ \mathrm{FT.88}\text{'s}\ \langle\omega,\Theta_{\mathfrak L}\rangle=\mathbb Z_2\times\mathbb Z_2\ \text{is the frozen precedent for the product structure}].$$

### FT.127 — The aspect census on the extended carrier

**Thm.** For the complete force operator of A8 — aspect inventory: the six pair-sector aspects [CT0.12], the rung masks and stack blocks [CT0.13, CT0.14], the two dark aspects [CT4.6, D4.1, D4.3], the Janus move classes [D1.2, FT.108(1)] — the derived-action census on $\mathcal H_{\mathrm{ext}}$ is:
$$(1)\quad F_W\ (\mathcal E_{+-}=\operatorname{span}\{W_i\},\ 3\text{-dim}\ [\mathrm{CT0.12}]):\ \textbf{acts}.\qquad W_i^{(\mathrm{ext})}=\tfrac12\sigma_i\otimes I_\omega\qquad[\mathrm{EW.32}\ \text{seed images};\ \text{Def-H.34}]\ \ [\text{exact}\ 4\times4\ \text{over}\ \mathbb Q(i)];$$
$$(2)\quad F_{\mathrm{EM}}\ (\text{stack},\ 1\text{-dim}\ [\mathrm{CT0.14}]):\ \textbf{acts on the internal factor only},\ \text{via the neutral mixing}\ A=\sin\theta_W\,W_3+\cos\theta_W\,Y\ [\mathrm{D3.10},\ \mathrm{EW.24}]:$$
$$A^{(\mathrm{ext})}=\tfrac12\bigl(\sin\theta_W\,\sigma_3+\cos\theta_W\,\sigma_0\bigr)\otimes I_\omega\qquad[\mathrm{EW.32}:\ Y\mapsto\tfrac12\sigma_0]\ —\ \text{inside clause}\ (1)\text{'s span};\ \text{chirality-blind}\ (\otimes I_\omega);$$
$$\text{the ternary end-register read}\ q_{\mathrm{core}}\ [\mathrm{D3.4},\ \mathrm{EM.9},\ \mathrm{FT.40}]\ \text{is}\ \omega\text{-odd configuration data: an orientation-side action requires the read promotion of FT.129 (Def-H.43)};$$
$$\text{a bridge between the seed neutral content and the ternary read is not derived (item 20 deficit 9 records the ternary-read situation)};$$
$$(3)\quad F_G\ (\operatorname{span}\{\hat E^{ij}\}\ \text{traceless},\ 5\text{-dim}\ [\mathrm{CT0.12}]):\ \textbf{does not act on}\ \mathcal H_{\mathrm{ext}}\ —\ \text{pair-register block}\ [\mathrm{CT1.2}];\ \text{chain-level content}= \text{geometric defect data}\ (\Theta_R\text{-type scalars under the Def-H.37(2)}\ \text{transfer}\ [\mathrm{FT.33},\ \mathrm{FT.54}(4)])\ —\ \text{scalar class};$$
$$(4)\quad F_H\ (\operatorname{span}\{\Sigma\},\ H=h\Sigma\ [\mathrm{EW.13}]):\ \textbf{does not act as a carrier matrix}\ —\ \Sigma\in\operatorname{End}(\mathbb C^4_{\mathrm{pair}})\ [\mathrm{CT1.2}];\ \text{Higgs content on chains}= \text{scalar background}\ (h_0\ \text{P4-class};\ \text{entering only through the EW.20/EW.33 defect-residue packaging})\ —\ \text{scalar class};$$
$$(5)\quad F_{D^+}\ (\operatorname{span}\{E_0\}=\Lambda\,\mathbb I\ [\mathrm{D4.3},\ \mathrm{CT4.6}]):\ \textbf{scalar class}\ —\ \text{central identity direction, configuration-independent};\ \text{if admitted on a carrier it is}\ \lambda I_4,\ \text{re-absorbed by}\ h\mapsto h+\lambda I_2\ [\mathrm{FT.130}(7)];\ \text{geometric side}\ \Lambda g_{\mu\nu}\ [\mathrm{CT1.23}],\ w=-1\ [\mathrm{CT1.25}];$$
$$(6)\quad F_{J^+},F_{J^-}\ (\operatorname{span}\{J_i\},\ \operatorname{span}\{K_i\}\ [\mathrm{CT0.12},\ \mathrm{CT0.7}(4)]):\ \textbf{do not act on}\ \mathcal H_{\mathrm{ext}}\ —\ \text{pair-register matrices}\ [\mathrm{CT1.2}]\ \text{and graph-level Janus move generators}\ [\mathrm{D1.2},\ \mathrm{FT.108}(1)];\ \text{no seed or orientation action derived};\ \text{their bilinear channel content is the seal-triplet reads of Tiers F.37–F.38}\ [\mathrm{FT.109},\ \mathrm{FT.116}];$$
$$(7)\quad F_{\mathrm{strong}}\ (8\text{-dim stack}\ [\mathrm{CT3.8},\ \mathrm{CT3.13},\ \mathrm{CT0.14}]):\ \textbf{does not act on}\ \mathcal H_{\mathrm{ext}}\ —\ \text{acts on the colour-slot carrier}\ \mathbb C^3\ \text{at trivalent vertices}\ [\mathrm{CT3.2},\ \mathrm{D3.1}];\ \text{the seed is colour-neutral by theorem}\ [\mathrm{EW.32}:\ T_a\mathsf v=0];\ \text{colour sits in an orthogonal stack block}\ [\mathrm{CT0.12}\ \mathrm{Rmk};\ \mathrm{FT.93}(4)];\ \mathcal H_{\mathrm{ext}}\ \text{has no slot factor};\ \text{sealed ends are blind in any case}\ [\mathrm{FT.117}];$$
$$(8)\quad F_{D^-}\ \bigl(\bigoplus_{n\ge4}F_n\ [\mathrm{D4.1},\ \mathrm{CT4.1},\ \mathrm{CT4.6}]\bigr):\ \textbf{does not act}\ —\ \text{ledger sink/retention verbs}\ [\mathrm{CT4.2}\text{–}\mathrm{CT4.5};\ \text{the retention census is}\ u\text{-fugacity bookkeeping}\ [\mathrm{FT.108}(3)]];\ \text{no carrier representation};$$
$$(9)\quad\textbf{census conclusion:}\ \ \text{the derived static force matrix is exactly the EW seed content},$$
$$\mathbf F_{\mathrm{ext}}(\mathbf c)=h(\mathbf c)\otimes I_\omega,\qquad h(\mathbf c)=\tfrac12\sum_{a=0}^{3}c_a\,\sigma_a,$$
$$\text{and the four images}\ \{\tfrac12\sigma_a\otimes I_2\}_{a=0}^{3}\ \text{are}\ \mathbb C\text{-independent with span}\ \operatorname{End}(\mathbb C^2)\otimes I_\omega\ [\text{machine}]:\ \text{every derived aspect action is chirality-blind}.$$

### FT.128 — The no-flip theorem at the derived locus

**Thm.** In the chiral basis of Def-H.34:
$$(1)\quad\textbf{form invariance:}\qquad U^{-1}\bigl(h(\mathbf c)\otimes I_\omega\bigr)U=h(\mathbf c)\otimes I_2\qquad[\text{the conjugation touches only the}\ \omega\text{-factor, where the derived matrix is the identity}];$$
$$(2)\quad\textbf{the block decomposition:}\qquad F_{LL}=F_{RR}=h(\mathbf c),\qquad F_{LR}=F_{RL}=0\qquad\text{exactly, for every profile}\ \mathbf c;$$
$$(3)\quad\textbf{the weak flip contribution vanishes by computation:}\qquad P_L^{\mathrm{car}}\,W_i^{(\mathrm{ext})}\,P_R^{\mathrm{car}}=0\ \ \forall i\qquad[\text{entrywise on the explicit}\ 4\times4\ \text{matrices};\ \mathrm{FT.123}(1)\ \text{re-verified, not invoked}];$$
$$(4)\quad\bigl[\mathbf F_{\mathrm{ext}}(\mathbf c),\ I_2\otimes\hat\chi\bigr]=0\ \ \forall\mathbf c:\qquad\text{chirality is an exact quantum number of the derived static force matrix};$$
$$(5)\quad\textbf{the derived spectrum:}\qquad\operatorname{charpoly}\mathbf F_{\mathrm{ext}}(\mathbf c)=\Bigl(x^2-c_0x+\tfrac{c_0^2-|\mathbf c|^2}{4}\Bigr)^2,$$
$$\operatorname{spec}=\Bigl\{\tfrac12\bigl(c_0+|\mathbf c|\bigr),\ \tfrac12\bigl(c_0-|\mathbf c|\bigr)\Bigr\},\ \text{each with multiplicity}\ 2\ \text{across the chiral rays}\ —\ \textbf{spectral parity doubling};\qquad|\mathbf c|=\sqrt{|\mathbf c|^2}\in\text{a quadratic extension of}\ \mathbb Q(\mathbf c);$$
$$(6)\quad\textbf{the static shadow, derived locus:}\qquad\langle L|\mathbf F_{\mathrm{ext}}|R\rangle=0\ —\ \text{the force aspects alone produce no parity-flipping seed on the extended carrier of a bound chain};\qquad\text{the flipping set at the derived locus}=\varnothing.$$

### Def-H.43 — The read promotion on the orientation doublet

**Def.** An $\omega$-odd A8-aspect read carried by a bound chain acts on the orientation doublet $\mathcal H_\omega$ [Def-H.33] as the multiplication operator of its eigenvalues on the orientation basis rays:
$$
\text{read}\ q\ \longmapsto\ \hat q\ :=\ q\cdot\hat\kappa\qquad(\omega\text{-odd reads}),\qquad
\hat\kappa\ =\ |c\rangle\langle c|-|\omega(c)\rangle\langle\omega(c)|\ \ [\mathrm{Def\text{-}H.34}:\ \text{the unique diagonal}\ \hat\omega\text{-odd Hermitian involution up to sign},\ \mathrm{FT.122}(6)],
$$
EM core read: $\ \hat Q_{\mathrm{EM}}=q_{\mathrm{core}}(c)\,\hat\kappa$, with $q_{\mathrm{core}}\in\{-1,0,+1\}$ ternary registration data [D3.4, EM.9, FT.40] — $\neg$fitted. $\omega$-even reads shift (no flip); the parity split is derived [FT.129(3) — immediate below], $\neg$part of this definition. The promotion is the sole source of a chirality-flipping block [FT.129(4)–(5)].

### FT.129 — The canonical flip candidate and the read promotion

**Thm.**
$$(1)\quad\textbf{canonicity:}\qquad\bigl\{M=M^\dagger:\ M\ \text{diagonal in the orientation basis},\ \hat\omega M\hat\omega=-M,\ M^2=\mathrm{id}\bigr\}=\{+\hat\kappa,\ -\hat\kappa\}\qquad[\mathrm{FT.122}(6)\text{'s circle at}\ (a,y)=(\pm1,0);\ \text{exact rational census};\ \text{machine}];$$
$$(2)\quad\textbf{chiral images:}\qquad\hat\kappa|L\rangle=|R\rangle,\quad\hat\kappa|R\rangle=|L\rangle\ (\text{ray swap, no phase});\qquad\text{in the chiral basis:}\ \hat\kappa\mapsto\sigma_1\text{-type},\ \hat\chi\mapsto\sigma_3\text{-type},\ \hat\omega\mapsto-\sigma_2\text{-type}\ [\text{the}\ S\text{-rotation of Def-H.34};\ \text{machine}];$$
$$(3)\quad\textbf{the parity split of the reads on the doublet:}\qquad\omega\text{-odd}:\ q_{\mathrm{core}}\ [\mathrm{FT.40}],\ k\ \text{and}\ \operatorname{sign}(k)\ [\mathrm{D2.6};\ \mathrm{EM.24}(1);\ \mathrm{FT.87}(8)];\qquad\omega\text{-even}:\ |k|,\ \Theta^2,\ \text{the sign-blind reads}\ [\mathrm{FT.90}(5)];$$
$$\text{an even read, promoted, multiplies}\ I_2\ (\text{chirality-blind});\ \text{an odd read, promoted, multiplies}\ \hat\kappa\ (\text{chirality-flipping}):\ \text{the flipping structure of any scalar read class is decided by its}\ \omega\text{-parity};$$
$$(4)\quad\textbf{Def-H.43 (read promotion, Def-H.43):}\ \ \text{an}\ \omega\text{-odd A8-aspect read carried by a bound chain acts on}\ \mathcal H_\omega\ \text{as the multiplication operator of its eigenvalues on the basis rays. For the EM core read:}$$
$$\hat Q_{\mathrm{EM}}:=q_{\mathrm{core}}(c)\,\hat\kappa\qquad[\text{the unique minimal promotion consistent with FT.40's eigenvalues}\ (q,-q);\ q\in\{-1,0,+1\}\ \text{registration data},\ \neg\text{fitted}];$$
$$\text{no such action is derived in Parts 1–2 (reads are labels}\ [\mathrm{Def\text{-}H.15}(4)]\text{), hence declared.}\ \textbf{Tension logged:}\ \text{the chiral rays superpose}\ \omega\text{-opposed core charges}\ (q,-q);\ \text{channel-level coarse-graining fuses only equal-}q\ \text{states}\ [\mathrm{FT.15}\ \text{hypothesis};\ \mathrm{FT.90}(5)\ \text{audit}]\ —\ \text{the relation between the carrier-level doublet and channel fusion is item 7/item 13 bridge content, open};$$
$$(5)\quad\textbf{the promoted force matrix and its flipping block:}\qquad\text{under Def-H.43,}$$
$$\mathbf F_{\mathrm{ext}}(\mathbf c,q)=h(\mathbf c)\otimes I_2+q\,I_2\otimes\hat\kappa,\qquad\bigl[h(\mathbf c)\otimes I_2,\ q\,I_2\otimes\hat\kappa\bigr]=0\ [\text{machine}];$$
$$F_{LL}=F_{RR}=h(\mathbf c),\qquad F_{LR}=q\,I_2=F_{RL}:\qquad\text{nonzero}\iff q\ne0;$$
$$\textbf{the flipping set}=\{F_{\mathrm{EM}}\ \text{core read}\}:\ \text{minimal and unique — removing the}\ \hat\kappa\ \text{term kills}\ F_{LR}\ \text{for every profile}\ [\mathrm{FT.128}(2)];\ \text{removing every internal term leaves}\ F_{LR}=qI_2\ [\text{machine}];$$
$$\text{the off-diagonal matrix elements encoding the flipping structure are the core-charge read itself:}\qquad\langle L|\mathbf F_{\mathrm{ext}}|R\rangle=q\,I_2.$$

### FT.130 — Tensor structure, Schmidt rank, and the static spectrum

**Thm.**
$$(1)\quad\textbf{derived locus:}\qquad\mathbf F_{\mathrm{ext}}(\mathbf c)=h(\mathbf c)\otimes I_\omega\ \text{is a single simple tensor for every}\ \mathbf c:\qquad\text{operator-Schmidt rank}=1\ (\text{rank}\ 0\iff\mathbf c=0)\ [\text{exact Pauli-bilinear flattening};\ \text{machine}];$$
$$(2)\quad\textbf{promoted locus:}\qquad\mathbf F_{\mathrm{ext}}(\mathbf c,q)=h\otimes I_2+q\,I_2\otimes\hat\kappa:\ \text{the two terms are Hilbert–Schmidt orthogonal}\ (\mathfrak T\hat\kappa=0);\qquad\text{Schmidt rank}=2\iff q\ne0\ \wedge\ (c_1,c_2,c_3)\ne0;$$
$$\text{rank}\ 1\ \text{when}\ h\propto I_2\ (\text{the terms share the internal factor and recombine:}\ \mathbf F_{\mathrm{ext}}=I_2\otimes(\lambda I_2+q\hat\kappa))\ \text{or exactly one term survives};\qquad\text{rank}\ 0\iff\mathbf c=0=q;$$
$$\textbf{no entangling term at any locus:}\ \ \mathbf F_{\mathrm{ext}}\ \text{is always a sum of}\ \le2\ \text{simple tensors with one-sided factors};$$
$$(3)\quad\textbf{the flipping criterion (iff):}\qquad F_{LR}\ne0\iff\text{some Schmidt term has a chiral-off-diagonal}\ \omega\text{-factor}\iff\text{the}\ \hat\kappa\ \text{term is present with}\ q\ne0\qquad[I_2\ \text{is chiral-diagonal};\ \hat\kappa\ \text{is chiral-off-diagonal}\ [\mathrm{FT.129}(2)]];$$
$$(4)\quad\textbf{derived spectrum:}\qquad\operatorname{spec}=\bigl\{\tfrac12(c_0\pm|\mathbf c|)\bigr\},\ \text{each}\times2;\qquad\text{field}\ \mathbb Q(\mathbf c)\bigl[\sqrt{|\mathbf c|^2}\bigr]:\ \text{quadratic extension};\ \text{charpoly exact over}\ \mathbb Q(\mathbf c)[x]\ [\mathrm{FT.128}(5)];$$
$$(5)\quad\textbf{promoted spectrum:}\qquad\text{the terms commute}\ [\mathrm{FT.129}(5)]:\qquad\operatorname{spec}=\bigl\{\tfrac12\bigl(c_0+s|\mathbf c|\bigr)+tq:\ s,t\in\{\pm1\}\bigr\},$$
$$\operatorname{charpoly}=\bigl((y-u)^2-q^2\bigr)\bigl((y+u)^2-q^2\bigr),\qquad y=x-\tfrac{c_0}2,\quad u^2=\tfrac{|\mathbf c|^2}4\qquad[\text{machine on all profiles}\times\text{ternary}\ q];$$
$$\textbf{the chiral-partner splitting}=2|q|\in\{0,2\}\qquad[\text{the ternary read}\ [\mathrm{EM.9}]:\ \text{charged cores split the parity doublet by exactly two read units; neutral cores keep the doubling}];$$
$$\text{simultaneous eigenbasis}=\text{internal Bloch rays}\otimes\text{orientation rays}\ \{|c\rangle,|\omega(c)\rangle\}\ (\hat\kappa\text{-eigenrays},\ \kappa\text{-eigenvalues}\ \pm1);\qquad|c\rangle=(|L\rangle+|R\rangle)/\sqrt2\ [\text{machine}]:$$
$$\text{the stationary rays carry no definite chirality — chirality is the precessing quantity, and}\ 2|q|\ \text{is the static shadow of the parity-flipping frequency (the dynamical read is deferred, FT.131}(3));$$
$$(6)\quad\textbf{collision census (exact):}\qquad q=0:\ \text{parity doubling};\qquad|\mathbf c|=0:\ \operatorname{spec}=\{\tfrac{c_0}2\pm q\},\ \text{each}\times2;\qquad\tfrac{|\mathbf c|}2=|q|:\ \text{the central eigenvalue}\ \tfrac{c_0}2\ \text{is double};\qquad\text{no further degeneracies at ternary}\ q;$$
$$(7)\quad\textbf{scalar-shift clause:}\qquad\mathbf F_{\mathrm{ext}}\mapsto\mathbf F_{\mathrm{ext}}+\lambda I_4\iff h\mapsto h+\lambda I_2:\qquad F_{LR},\ \text{Schmidt ranks, commutants and the splitting}\ 2|q|\ \text{invariant};\ \text{the spectrum translates by}\ \lambda$$
$$[\text{any scalar-class contribution}\ —\ F_{D^+}\ \text{if admitted},\ h_0\text{-type backgrounds},\ m^2\text{-type reads as identity multiples}\ —\ \text{is invisible to the flipping structure}].$$

### FT.133 — The configuration-space reversal calculus

**Thm.** On the configuration space $\mathfrak C(\mathcal R)$ [D0.10], with configuration data $(R,\ \sigma,\ \alpha,\ \kappa/\text{ledger})$ [A4, A8, D0.5, D3.5, Def-EM.20]:
$$(1)\quad\textbf{the four register involutions}\ [\text{each frozen, re-derived at the point of use}]:$$
$$\omega\text{-pattern}:\ R\mapsto R^{\mathrm T}=\{(b,a):(a,b)\in R\}\ \text{with edge data carried}\ [\mathrm{D2.6};\ \mathrm{FT.88}(1)];\qquad C:\ \sigma_e\mapsto-\sigma_e\ [\mathrm{EM.24}(1)];$$
$$P:\ \alpha_e\mapsto\pi-\alpha_e\ \ (\mathcal P\mapsto E_{\mathcal R}\setminus\mathcal P)\ [\mathrm{EM.24}(2),\ \mathrm{Def\text{-}EM.21}];\qquad T=\Theta_{\mathfrak L}:\ \text{ledger order reversed},\ J^+\leftrightarrow J^-,\ \kappa_e\mapsto-\kappa_e,\ \sigma\ \text{fixed}\ [\mathrm{D2.7};\ \mathrm{FT.88}(2)];$$
$$\text{each is an involution on configuration data}\ [\text{machine: exhaustive on}\ 17^2+5^6\ \text{configurations}\ +\ 3000\ \text{deterministic off-shell samples}];$$
$$(2)\quad\textbf{register-disjoint commutation:}\qquad[C,P]=[C,T]=[P,T]=[C,\omega]=[P,\omega]=[T,\omega]=0$$
$$[\text{the four act on pairwise-disjoint data coordinates: edge-direction set};\ \sigma;\ \alpha;\ (\kappa,\text{ledger})]\implies\langle C,P,T\rangle\cong\mathbb Z_2^3,\qquad\langle\omega\text{-pattern},\,C,\,P,\,T\rangle\cong\mathbb Z_2^4;$$
$$\mathrm{FT.88}(3)\text{'s}\ \langle\omega,\Theta_{\mathfrak L}\rangle\cong\mathbb Z_2\times\mathbb Z_2\ \text{is the frozen two-generator subalgebra}\ [\text{machine: exhaustive commutation census}];$$
$$(3)\quad\textbf{component weight identities}\ (w=\mathcal J\cdot S\cdot\Gamma\cdot A,\ S=\prod\sigma_e,\ \Gamma=\prod e^{i\alpha_e\widehat{ds}^{\,2}(e)},\ A=(-1)^{\aleph}\ [\mathrm{A8},\ \mathrm{D3.5},\ \mathrm{D3.6}]):$$
$$w(C\mathcal C)=(-1)^{|E|}\,w(\mathcal C)\ [\aleph\ \text{invariant}:\ \aleph_v=|f_v|,\ f_v\mapsto-f_v];\qquad w(T\mathcal C)=w(\mathcal C)^{*}\ [\mathrm{CT2.8}(1)];\qquad w(P\mathcal C)=e^{i\pi\Theta}\,w(\mathcal C)^{*};$$
$$\Theta:=\!\!\sum_{e\in R}\!\!\widehat{ds}^{\,2}(e)\ [\mathrm{EM.24}(5)]:\quad\Theta\ \text{is}\ P\text{-even},\ T\text{-odd}\ (\Theta\mapsto-\Theta),\ \omega\text{-even}\ (\text{an edge-set function};\ \widehat{ds}^{\,2}\ \text{direction-symmetric});$$
$$(4)\quad\textbf{the composition, in both frozen lifts:}\qquad\mathrm{CPT}:=C\circ P\circ T\ [\mathrm{EM.24}(4)];$$
$$\text{conjugation lift}\ [\mathrm{EM.24}(5)\ \mathrm{Pf}:\ T\ \text{as}\ \Gamma\mapsto\bar\Gamma]:\qquad w(\mathrm{CPT}\,\mathcal C)=(-1)^{|E|}\,e^{+i\pi\Theta}\,w(\mathcal C);$$
$$\kappa\text{-flip lift}\ [\mathrm{FT.88}(2)\ \text{register picture}:\ T:\kappa\mapsto-\kappa]:\qquad w(\mathrm{CPT}\,\mathcal C)=(-1)^{|E|}\,e^{-i\pi\Theta}\,w(\mathcal C);$$
$$\text{the two lifts agree exactly on the integer-}\Theta\ \text{locus}\ (e^{2i\pi\Theta}=1),\ \text{which contains every materialized closed chain}\ [\mathrm{FT.22}:\ \Theta\in2\mathbb Z];\qquad\bigl|w(\mathrm{CPT}\,\mathcal C)\bigr|^2=\bigl|w(\mathcal C)\bigr|^2\ \text{unconditionally in both lifts}\ [\text{machine}];$$
$$(5)\quad\textbf{on-shell reductions:}\qquad\Theta\in2\mathbb Z\implies e^{i\pi\Theta}=1:\ \text{the CPT character reduces to}\ (-1)^{|E|};\qquad|E|+\Theta\equiv0\ (\mathrm{mod}\ 2)\implies w(\mathrm{CPT}\,\mathcal C)=w(\mathcal C)=w(\mathcal C)^{*}\ [\mathrm{EM.24}(5)\ \text{third line, re-derived}];$$
$$(6)\quad\textbf{the read-covariance table}\ [\text{exact; machine on closed digon and triangle chains}]:$$
$$\begin{array}{c|cccc}
\text{read} & C & P & T & \omega\\ \hline
q_{\mathrm{core}}\ [\mathrm{FT.40}] & - & + & + & -\\
\Theta=\sum\widehat{ds}^{\,2} & + & + & - & +\\
|E|,\ K=|R| & + & + & + & +\\
\aleph\ [\mathrm{EM.24}(1)] & + & + & + & +\\
\mathcal P\ [\mathrm{Def\text{-}EM.21}] & + & \text{complement} & + & \text{transported}
\end{array}$$
$$(7)\quad\textbf{the parity naming (derived record):}\ \ \text{the parity operation on configuration space is}\ \mathrm{EM.24}(2)\text{'s}\ P\ —\ \textbf{derived}\ \text{from the dynamic phase}\ [\mathrm{Def\text{-}EM.20},\ \mathrm{EM.20}(1)]\ \text{and named inside the derived CPT bridge};\ \mathrm{FT.101}(3)\text{'s branch flip}\ \iota(\alpha)=\pi-\alpha\ \textbf{is}\ P|_{\Phi}\ \text{on the A4 label alphabet}\ [\mathrm{FT.101}(3)\ \text{cites}\ \mathrm{EM.24}(2),\ \mathrm{Def\text{-}EM.21}]:\ \text{the identification is derived content and no declaration issues}\ [\text{HistLog §IV}/\mathrm{FT.140}(1)].$$

### FT.134 — The carrier bookkeeping: the scalar-CPT theorem

**Thm.** On the orientation doublet $\mathcal H_\omega$ [Def-H.33] and the extended carrier [Def-H.34]:
$$(1)\quad\textbf{the ray census:}\ \ \omega\text{-pattern is the only involution of the FT.133 family that moves the doublet basis}\ (\hat\omega|c\rangle=|\omega(c)\rangle\ [\mathrm{FT.122}(4)]);\ \ C,P,T\ \text{fix the chain tuple pointwise}\ [\mathrm{FT.133}(1)\ \text{registers}]:\ \text{their doublet action is the identity on rays, with a label map};$$
$$\text{hence no operator identification}\ \hat\omega=C\ \text{or}\ \hat\kappa=P\ \text{exists: the two sides of each proposed equality act on different registers}\ [\text{machine witnesses}];$$
$$(2)\quad\textbf{the read-level covariance (the content the identifications reach):}\ \ \text{under Def-H.43's promotion}\ \hat Q_{\mathrm{EM}}=q_{\mathrm{core}}\hat\kappa\ [\mathrm{FT.129}(4)]:\ \text{the family}\ \{\hat Q_q=q\hat\kappa\}\ \text{is}\ C\text{-odd}\ (\hat Q_{-q}=-\hat Q_q,\ \text{matching}\ q\mapsto-q),\ P\text{-even and}\ T\text{-even}\ (q_{\mathrm{core}}\ \text{is}\ P/T\text{-even}\ [\mathrm{FT.133}(6)]),\ \text{and}\ \omega\text{-covariant}\ (\hat\kappa\ \hat\omega\text{-odd}\ \wedge\ q\ \omega\text{-odd}:\ \text{the signs cancel});$$
$$\text{consequently Tier F.40's flipping block}\ F_{LR}=q\,I_2\ \text{is}\ C\text{-odd},\ P\text{-even},\ T\text{-even}\ [\mathrm{FT.129}(5)];$$
$$(3)\quad\textbf{the scalar-CPT theorem:}\ \ \text{the CPT character}\ \lambda=(-1)^{|E|}e^{i\pi\Theta}\ \text{takes the same value on both doublet rays}\ (|E|,\Theta\ \text{are edge-set functions}\ [\mathrm{FT.133}(6)]),\ |\lambda|=1:$$
$$\mathrm{CPT}\big|_{\mathcal H_\omega}=\lambda\,\mathrm{id},\qquad\lambda=(-1)^{|E|}e^{i\pi\Theta};$$
$$\text{chirality is CPT-even: the}\ \hat\chi\text{-eigenspaces are CPT-stable};\ \hat\kappa\ \text{and}\ \hat\omega\ \text{likewise};\qquad\textbf{refutation witness:}\ \operatorname{tr}(\lambda\,\mathrm{id})=2\lambda\ne0=\operatorname{tr}(\pm\hat\kappa):\ \text{no}\ \hat\kappa\text{-multiple equals the CPT action};$$
$$(4)\quad\textbf{the uniqueness pair}\ [\text{re-derived at the point of use}]:\ \ \pm\hat\chi\ \text{are the unique diagonal-free}\ \hat\omega\text{-odd Hermitian involutions}\ [\mathrm{FT.122}(6)];\ \pm\hat\kappa\ \text{the unique diagonal ones}\ [\mathrm{FT.129}(1)];\ \text{quaternionic triple}\ [\mathrm{Def\text{-}H.34}]:\ \hat\omega\hat\chi=-i\hat\kappa,\ \hat\chi\hat\kappa=-i\hat\omega,\ \hat\kappa\hat\omega=-i\hat\chi;$$
$$(5)\quad\textbf{independence:}\ \ \text{any internal involution}\ G\otimes I_2\ \text{commutes with}\ I_2\otimes\hat\omega\ \text{and their product is a third distinct involution: the configuration-side and carrier-side}\ \mathbb Z_2\text{'s generate}\ \mathbb Z_2\times\mathbb Z_2\ [\mathrm{FT.126}(4)\ \text{pattern};\ \mathrm{FT.88}(3)\ \text{precedent};\ \text{machine}].$$

### FT.135 — The weak branch grading under parity

**Thm.**
$$(1)\quad\iota(0)=\pi,\ \iota(\pi)=0\ \text{on the branch alphabet}\ \Phi=\{0,\pi\}\ [\mathrm{FT.101}(3);\ \mathrm{D0.5}];\qquad\iota=P|_{\Phi}\ [\mathrm{EM.24}(2);\ \mathrm{FT.101}(3)\ \text{citation chain}]:\ \text{parity exchanges the two crystallization branches at the label level};$$
$$(2)\quad\textbf{aligned branch}\ (\alpha=0,\ \vee^2,\ \text{Casimir}\ 2):\ W_i=\Pi_{\mathcal R}W_i\Pi_{\mathcal R}\ne0,\ \sum_iW_i^2=2\Pi_{\mathcal R}\ [\mathrm{FT.101}(1),\ \text{Cor}\ \mathrm{CT0.7a}\ \text{re-derived}];\qquad\textbf{antialigned branch}\ (\alpha=\pi,\ \wedge^2,\ \text{Casimir}\ 0):\ W_i\Pi_{\mathcal V}=0,\ \bigcap_i\ker W_i=\operatorname{im}\Pi_{\mathcal V}\ [\mathrm{FT.101}(2),\ \mathrm{FT.93}(5)\ \text{re-derived}];$$
$$(3)\quad P\ \text{maps the weak-active branch label to the weak-blind one: the weak support is not flip-invariant}\ [\mathrm{FT.101}(4)];\ \text{structural parity non-invariance of the force arena}\ [\mathrm{FT.101}(5)];\ \text{scope: arena}\ S\text{-parity grading},\ \neg\ \text{matter chirality}\ [\mathrm{FT.93}(3),\ \mathrm{FT.93}(7)];$$
$$(4)\quad\textbf{the exchange is label-level only:}\qquad\mathfrak T\Pi_{\mathcal R}=3\ne1=\mathfrak T\Pi_{\mathcal V};\qquad M=a\Pi_{\mathcal R}+b\Pi_{\mathcal V}:\ M^2=\mathrm{id}\implies a,b\in\{\pm1\}\implies\operatorname{tr}M=3a+b\in\{\pm4,\pm2\}\ne0:$$
$$\text{no traceless involution implements the branch exchange on the pair register}\ [\mathrm{FT.101}(3),\ \mathrm{FT.93}(3a)\ \text{re-derived}];\qquad\mathbb S\Pi_{\mathcal R}=+\Pi_{\mathcal R},\ \mathbb S\Pi_{\mathcal V}=-\Pi_{\mathcal V}\ [\text{the}\ S\text{-eigenvalue labels}].$$

### FT.136 — The rung-one S-grading: the 10/6 split

**Thm.**
$$(1)\quad\textbf{the}\ \operatorname{Ad}(\mathbb S)\ \textbf{census on the CT1.2 generators}\ [\text{machine: all}\ 17]:\qquad S\text{-even}\ (+1):\ \{E_0,\ \Sigma,\ \hat E^{ij}\ (5\ \text{dims}),\ W_i\ (3)\}=10\ \text{dims}=\underbrace{G_5+W_3+H_1}_{\text{forces}}+\underbrace{D^+_1}_{\text{central}};$$
$$S\text{-odd}\ (-1):\ \{J_i\ (3),\ K_i\ (3)\}=6\ \text{dims}=J^+_3+J^-_3\qquad[\mathrm{CT1.2}\ (S,T)\ \text{table};\ \mathrm{CT0.12};\ \mathrm{FT.30}\ \text{tiling}\ (5{+}3{+}1)+(3{+}3)+1];$$
$$(2)\quad\mathcal A(1)=\{J,\,G,\,W,\,H,\,D^+\}\ [\mathrm{CT0.13}]:\ \text{the rung-one active set}\ \textbf{is}\ \text{the}\ 10/6\ \text{split};\ \text{the metric dictionary}\ [\mathrm{FT.30}]:\ \text{the}\ S\text{-even block carries every metric coordinate}\ (\hat h_{ij}\ 5,\ \Sigma_{\mathrm{tr}}\ 1,\ a_{00}\ 1,\ w_i\ 3);\ \text{the}\ S\text{-odd Janus seals carry none};$$
$$(3)\quad\textbf{register separation:}\ \ P\ (\alpha\text{-complement})\ \text{acts on configuration data and has no action on the pair algebra}\ [\mathrm{FT.133}(2)];\ \text{the only derived bridge between parity and the}\ S\text{-grading is FT.101's label}\leftrightarrow\text{arena coupling}\ (\text{branch}\ \alpha\leftrightarrow\vee^2/\wedge^2\ \text{weak support}):\ \text{a naming of the}\ S\text{-blocks as}\ P\text{-sectors has no operator content — the two}\ \mathbb Z_2\text{'s act on different spaces};$$
$$(4)\quad\textbf{the independence census:}\ \ \text{three pairwise-distinct}\ \mathbb Z_2\ \text{gradings stand in the record: the algebra}\ S\text{-grading}\ (\operatorname{Ad}\mathbb S),\ \text{the branch-label parity}\ (P/\iota\ [\mathrm{FT.101}]),\ \text{the carrier chirality}\ (\hat\chi\ [\mathrm{FT.122}])\ —\ \text{pairwise commuting where jointly defined, none reducible to another}\ [\mathrm{FT.126}(4);\ \text{machine}]:$$
$$\text{the}\ 10/6\ \text{asymmetry is the force/dynamics split of rung one; it is not the source of the carrier chirality grade};$$
$$(5)\quad\textbf{the weak location:}\ \ W\ \text{is}\ S\text{-even}\ [\text{clause}\ (1)];\ \text{its chiral selectivity is the arena}\ 3\oplus1\ \text{grading}\ [\mathrm{FT.93}(5):\ W_i\Pi_{\mathcal V}=0,\ \sum W_i^2=2\Pi_{\mathcal R}]\ —\ \text{a third structure, distinct from both the}\ S\text{-grading of the operator algebra and the}\ \hat\chi\text{-grading of the carrier}.$$

### FT.141 — The rung-one chirality theorem: the $10/6$ grading is the chirality of the complete force complex

**Thm.** With $\mathbb S=\tfrac12(E_0+\Sigma)$ and $S(X)=\mathbb SX\mathbb S=\operatorname{Ad}(\mathbb S)X$ [A3; CT0.7(1)–(2)] on the pair channel $\mathfrak H(\mathbb C^4)$:
$$(1)\quad\textbf{the grading census}\ [\mathrm{FT.136}(1)\ \text{re-derived at the point of use; machine: all}\ 17\ \mathrm{CT1.2}\ \text{generators}]:\qquad S\text{-even}\ (+1):\ \{E_0,\ \Sigma,\ \hat E^{ij}\ (5),\ W_i\ (3)\}=10\ \text{dims}=G_5+W_3+H_1+D^+_1;$$
$$S\text{-odd}\ (-1):\ \{J_i\ (3),\ K_i\ (3)\}=6\ \text{dims}=J^+_3+J^-_3;\qquad 10+6=16=C_{\mathrm{cap}}\ [\mathrm{CT0.12};\ \mathrm{CT0.6}];\qquad\text{the asymmetry}\ 10\ne6\ \text{is exact};$$
$$(2)\quad\textbf{the chirality of the complete force complex:}\ \ \text{the A8 block labels are readings of the}\ (S,T)\ \text{grades}\ [\mathrm{CT0.7}(4)]:\ \mathbf F_{(+,\mathcal R)}=F_G\oplus F_H\oplus F_{D^+}\ \text{and}\ \mathbf F_{(-,\mathcal R)}=F_W\ \text{are the}\ S\text{-even aspects},\ \mathbf F_{(+,\mathcal V)}=F_{J^+},\ \mathbf F_{(-,\mathcal V)}=F_{J^-}\ \text{the}\ S\text{-odd aspects};$$
$$\text{the chiral structure of the complete force operator}\ \mathbf F\ [\mathrm{A8}:\ \text{always applied in full}]\ \text{at rung}\ 1\ \text{is the ordered pair}\ \bigl(\dim\mathcal K_1^{+},\ \dim\mathcal K_1^{-}\bigr)=(10,\ 6)\ [\mathrm{CT0.14}:\ \mathcal K_1=\text{the rung-one mask}]:$$
$$\text{a property of the pair algebra}\ [\mathrm{A3}'\text{s swap};\ \mathrm{CT1.1},\ \mathrm{CT1.2}'\text{s basis}],\ \neg\ \text{of any single block:}\ \neg\exists\ \text{an aspect that is}\ \textbf{the}\ \text{chiral force};$$
$$(3)\quad\textbf{deletion invariance:}\ \ \forall\,\mathcal Y\subseteq\{G,\ W,\ H,\ D^+,\ J^+,\ J^-\}\ \text{(the six rung-one blocks)}:\ \text{the}\ S\text{-eigenvalue of every surviving generator is unchanged}\ (\text{the eigen-relation}\ \mathbb SX\mathbb S=\pm X\ \text{is a two-operator relation: deletion touches neither}\ \mathbb S\ \text{nor}\ X);$$
$$\text{the surviving split is}\ (10-d^+_{\mathcal Y},\ 6-d^-_{\mathcal Y}),\ d^{\pm}_{\mathcal Y}\ \text{the deleted dimensions in each grade};\qquad\text{the grading is nontrivial (both grades occupied)}\iff\ge1\ S\text{-even block and}\ \ge1\ S\text{-odd block survive}:\ 45\ \text{of the}\ 2^6=64\ \text{subsets}\ [\text{machine: exhaustive}];$$
$$\text{the six single-block deletions leave}\ (5,6),\ (7,6),\ (9,6),\ (9,6),\ (10,3),\ (10,3):\ \text{each nontrivial, each asymmetric};\qquad\text{the full}\ 10/6\ \text{is recovered}\iff\mathcal Y=\varnothing;$$
$$(4)\quad\textbf{the weak shadow:}\ \ W_i\in\mathcal E_{+-}:\ S\text{-even}\ [\mathrm{CT1.2}\ \text{table}];\qquad\operatorname{span}\{J_i,K_i\}\cap\operatorname{span}\{W_k\}=\{0\}\ [\text{disjoint basis subsets};\ \text{machine: rank}\ 9=6+3]:\ \text{the}\ S\text{-odd block carries no weak content};$$
$$\text{the branch selectivity of the weak}\ [\mathrm{FT.93}(5),\ \mathrm{FT.101}]\ \text{sits at the state-space locus of the same swap}:\qquad\Pi_{\mathcal R}=\tfrac12(E_0+\mathbb S),\quad\Pi_{\mathcal V}=\tfrac12(E_0-\mathbb S)\quad[\mathrm{CT0.7}(1)],$$
$$W_i\Pi_{\mathcal V}=0\ \ \forall i\ [\mathrm{FT.101}(2)\ \text{re-derived}];\qquad\textstyle\sum_iW_i^2=\tfrac32E_0+\tfrac12\Sigma\ [\mathrm{Cor}\ \mathrm{CT0.7a}]=E_0+\mathbb S=2\,\Pi_{\mathcal R}\qquad[\Sigma=2\mathbb S-E_0;\ \text{machine, entrywise}]:$$
$$\text{the swap operator itself enters the weak Casimir identity — the branch asymmetry}\ (2\ \text{vs}\ 0)\ \text{is derived from the}\ S\text{-grading, and}\ \mathbb S\ \text{is A3 data, prior to every force assignment}\ [\mathrm{CT0.7}(4):\ \text{the A8 labels read the grades}];$$
$$\text{locus discipline}\ [\mathrm{FT.136}(5)\ \text{stands}]:\ \text{the}\ 3\oplus1\ \text{branch split}\ (\operatorname{spec}\mathbb S\ \text{on}\ \mathbb C^4_{\mathrm{pair}})\ \text{and the}\ 10/6\ \text{operator split}\ (\operatorname{spec}\operatorname{Ad}(\mathbb S)\ \text{on}\ \operatorname{End}(\mathbb C^4_{\mathrm{pair}}))\ \text{are two loci of one swap, and neither is the carrier}\ \hat\chi\text{-grade}\ [\mathrm{FT.122}];$$
$$(5)\quad\textbf{no}\ S\textbf{-neutral observable at rung one:}\ \ \operatorname{Ad}(\mathbb S)^2=\mathrm{id}\implies\operatorname{spec}\operatorname{Ad}(\mathbb S)\subseteq\{\pm1\}\ \text{and}\ \ker\operatorname{Ad}(\mathbb S)=\{0\}\ [\operatorname{Ad}(\mathbb S)\ \text{is its own inverse};\ \text{machine: rank}\ 16\ \text{on the flattened}\ 16\text{-basis};\ \operatorname{tr}\operatorname{Ad}(\mathbb S)=10-6=4];$$
$$\text{every rung-one observable carries the unique grade decomposition}\ X=X_++X_-,\quad X_{\pm}=\tfrac12\bigl(\mathrm{id}\pm\operatorname{Ad}(\mathbb S)\bigr)X;$$
$$\text{the metric reads}\ (\hat h_{ij}\ 5,\ \Sigma_{\mathrm{tr}}\ 1,\ a_{00}\ 1)\ \text{and the weak reads}\ (w_i\ 3)\ \text{are}\ S\text{-even};\ \text{the seal reads}\ (J^{\pm})\ \text{are}\ S\text{-odd with}\ 0\ \text{metric coordinates}\ [\mathrm{FT.30}\ \text{dictionary}]:$$
$$\text{chirality at rung}\ 1\ \text{is}\ \neg\ \text{a selection rule applied by one force — it is the grading of the entire observable algebra}\ \mathcal K_1\ [\mathrm{CT0.14}\ \mathrm{Rmk}:\ \dim\mathcal K_1=16=C_{\mathrm{cap}}:\ \text{rung one exhausts the pair channel}];$$
$$(6)\quad\textbf{reconciliation — the two independent}\ \mathbb Z_2\textbf{'s:}\ \ \text{the force-arena}\ S\text{-grading acts on}\ \operatorname{End}(\mathbb C^4_{\mathrm{pair}});\ \text{the carrier chirality}\ \hat\chi\ \text{acts on}\ \mathcal H_\omega\ [\mathrm{Def\text{-}H.33},\ \mathrm{FT.122};\ \text{Def-H.34}]:\ \text{pairwise distinct, commuting where jointly defined, neither reducible to the other}\ [\mathrm{FT.126}(4),\ \mathrm{FT.136}(4)\ \text{re-derived};\ \text{machine witnesses}];$$
$$\text{the division of labour: the}\ S\text{-grading determines WHICH observables are chiral (the grade of every read); the carrier chirality determines WHICH chain orientations are chiral (the doublet's rays);}$$
$$\text{the rule coupling the two}\ \mathbb Z_2\text{'s — and the branch-label}\ \mathbb Z_2\ [\mathrm{FT.101},\ \mathrm{FT.135}]\ \text{and the Janus arrow}\ [\mathrm{FT.144}(5)] — \text{to species is the deficit}\ 1'\ \text{assignment rule}\ [\mathrm{FT.125}(4),\ \text{HistLog §IV}/\mathrm{FT.140}(3)]:\ \neg\text{constructed here};\ \text{no new declaration issues}.$$

### FT.142 — The rung-one arena and the channel angle $\delta_\nu=\tfrac18$

**Thm.** The rung-one channel — the deficit-6 ledger row, internal channel subscript $\nu$ [$\neg$a species name; Rmk below]:
$$(1)\quad\textbf{the channel class:}\ \ \text{a rung-one bound chain is a bound chain}\ [\mathrm{D1.5}]\ \text{whose terminus-active aspects lie in}\ \mathcal A(1)=\{J,\ G,\ W,\ H,\ D^+\}\ [\mathrm{CT0.13}]:$$
$$\text{EM unactivated}\ (f_v=0\ \text{reads}\ [\mathrm{D3.3};\ \mathrm{FT.28}(3):\ \mathrm{EM}\in\mathcal A\iff f_p\ne0\ \vee\ f_q\ne0]);\qquad\text{colour block vanishing}\ (\text{no slot index below trivalence}\ [\mathrm{CT3.11}(1)];\ \text{single-contact floors:}\ \mathcal C=0\implies\text{block}\equiv0\ [\mathrm{FT.19},\ \mathrm{FT.28}(3)]);$$
$$\text{the Def-H.4 floor stands:}\ \delta h(c)\ge2,\ n(v)\ge2\ [\text{self-loops}\ \bot\ \text{by A1}];\qquad\text{the minimal instance is the digon}\ \Sigma_{\min}\ [\mathrm{FT.28}];$$
$$(2)\quad\textbf{the arena:}\ \ \text{the pair-channel arena on which the complete rung-one force acts is the rung-one mask}\ \mathcal K_1:\qquad\dim\mathcal K_1=16=C_{\mathrm{cap}}\quad[\mathrm{CT0.14},\ \mathrm{CT0.12};\ \text{machine: exact rank}];$$
$$\text{the complete-force standing rule}\ [\mathrm{A8}]\ \text{fixes the arena as the full mask: no sub-block arena — isolating a force is not an A8 action};$$
$$(3)\quad\textbf{the arena adjudication}\ (\text{computed candidates; one adopted}):$$
$$\begin{array}{c|c|c}\text{candidate} & \text{source} & \text{verdict}\\ \hline 16=\dim\mathcal K_1 & \mathrm{CT0.14}\ \text{(derived mask)} & \textbf{adopted}\\ 10=S\text{-even block} & \mathrm{FT.141}(1) & \text{rejected: deleting the}\ S\text{-odd blocks violates A8's completeness}\ [\mathrm{CT0.13}:\ J\in\mathcal A(1)]\\ 9=\text{seal}\times\text{transfer} & \mathrm{FT.110}\ [\text{Def-H.41}] & \text{rejected: a interface definition for transfer-dressed chains}\ [\text{the transfer trace}\ \operatorname{tr}T(1)=3\ \text{is polygon-channel data},\ \mathrm{FT.68}(2)];\ \text{not imported in this part}\\ 27=\text{seal}\times\text{transfer}\times\text{colour} & \mathrm{FT.118}(2)\ [\text{Def-H.42}] & \text{rejected: colour slots are rung-three content}\ [\mathrm{CT0.13}];\ \text{clause}\ (1)\ \text{excludes them};\ \text{not imported}\\ 6=\dim\mathcal K_0 & \mathrm{CT0.14} & \text{rejected: seals alone; a terminus with}\ n(v)\ge2\ \text{carries metric and weak reads}\ [\mathrm{FT.28}(3):\ \{G,H,W\}\subseteq\mathcal A(\Sigma_{\min})]\end{array}$$
$$\text{the adopted arena is the unique candidate that is derived content with no interface declaration:}\ \delta_\nu\ \text{is the first channel angle whose denominator requires no declaration-entry construction};$$
$$(4)\quad\textbf{the seal coefficient, undressed:}\ \ [J_i,K_j]=i\bigl(\delta_{ij}\Sigma-E^{ij}\bigr)\ [\mathrm{CT1.7}\ \text{re-derived, all}\ 9\ \text{pairs}];\qquad\textstyle\sum_i[J_i,K_i]=i\bigl(3\Sigma-\textstyle\sum_iE^{ii}\bigr)=2i\Sigma\quad[\textstyle\sum_iE^{ii}=\Sigma];$$
$$\text{in the}\ 16\text{-element CT1.2 basis the sum has exactly one nonzero component — the}\ \Sigma\text{-component, coefficient exactly}\ 2\ [\mathrm{FT.109}(3)\ \text{pattern};\ \text{machine: exact linear solve, rank}\ 16];$$
$$\text{the rung-one channel class carries no dressing factor}\ (\neg\text{colour slots by clause}\ (1);\ \neg\text{transfer declaration imported by clause}\ (3)):\ \text{the numerator is}\ 2,\ \text{undressed}\ [\mathrm{FT.118}(5)\ \text{spectator pattern}];$$
$$(5)\quad\textbf{the channel angle:}\qquad\delta_\nu\ :=\ \frac{\sum_i[J_i,K_i]\big|_\Sigma}{\dim\mathcal K_1}\ =\ \frac{2}{16}\ =\ \frac18\qquad[\text{exact rational};\ \mathrm{FT.112}\ \text{pattern}];$$
$$\text{the democratic normalization}\ A=1,\ B=\sqrt2\ \text{is seal-side data}\ [\mathrm{FT.111}(3):\ \textstyle\sum_i\lambda_i=3=\dim F_{J^\pm};\ \sum_i(\lambda_i-A)^2=3]\ \text{and hence channel-blind}\ [\mathrm{FT.119}\ \text{precedent}]:\ \text{the rung-one channel inherits it unchanged}.$$

### FT.144 — The Janus-arrow theorem: no backward materialization, and single-sector occupancy at rung one

**Thm.**
$$(1)\quad\textbf{the valid-universe condition:}\qquad\text{valid universe}\iff\text{real-edge network closed}\ \wedge\ \#J^+=\#J^-\ \wedge\ \in\operatorname{Im}(\text{active mask})\ \wedge\ \neg\exists\ \text{dangling ledger boundary}\ [\mathrm{D2.11},\ \mathrm{D1.3}];$$
$$\text{observable fermions are termini of Janus-closed bound chains}\ [\mathrm{Def\text{-}H.4}];\qquad\text{closed}\iff\partial c=0\ \wedge\ \#J^+=\#J^-\ [\mathrm{D1.4}];\qquad\text{bound content is fermionic}\ [\mathrm{D1.5}];$$
$$(2)\quad\textbf{the forward arrow}\ (\text{per-pair transition domains}):\qquad J^+:\ n_{\mathcal R}:0\to1\ (\text{crystallization});\qquad J^-:\ n_{\mathcal R}:1\to0\ (\text{dissolution})\qquad[\mathrm{D1.2}];$$
$$J^-\ \text{is undefined at}\ n_{\mathcal R}=0\ \ \wedge\ \ J^+\ \text{is undefined at}\ n_{\mathcal R}=1:\ \text{the domains force}\ \textbf{strict alternation}\ \text{— the only admissible single-pair histories are the prefixes of the alternating word}\ (J^+J^-J^+J^-\cdots);$$
$$\text{every admissible history obeys the prefix law}\ \ \#J^+(\text{prefix})\ \ge\ \#J^-(\text{prefix}),\ \ \text{with equality}\iff n_{\mathcal R}=0;\qquad\text{the completed single-pair history of length}\ 2m\ \text{is unique:}\ (J^+J^-)^m,\ \#J^+=\#J^-=m;$$
$$\text{two-pair completed interleavings of total length}\ 2n:\qquad\sum_{m_0+m_1=n}\frac{(2n)!}{(2m_0)!\,(2m_1)!}\ =\ 2,\ 8,\ 32\quad(2n=2,4,6)\qquad[\text{machine: exhaustive enumeration}\ \le8\ (\text{single pair}),\ \le6\ (\text{two pairs})\ \text{agrees with the closed form}];$$
$$\text{a materialized closed chain with any dissolution-first edge}\ (J^-\to J^+\ \text{as its leading local transition})\ \text{violates the prefix law at its first event: it is outside the transition domains, hence excluded from every valid universe}\ [\mathrm{D2.11}];$$
$$\text{the sealed universe-level balance}\ \#J^+=\#J^-\ [\mathrm{D1.3}]\ \text{is the balanced-sector restriction of the move algebra's budget identity}\ a_+-a_-=|R'|-|R|\ [\mathrm{FT.108}(4)];$$
$$(3)\quad\textbf{not a mass statement:}\ \ \text{the obstruction of}\ (2)\ \text{is the transition domain of D1.2 conjoined with the closure of D1.4/D2.11 — a combinatorial locus statement: no scale, no P4 parameter and no mass enters it}\ [\text{inventory: the premises contain}\ \neg\mathfrak h,\ \neg\mu,\ \neg h_0];$$
$$\neg\exists\ \text{a value of any configuration datum that un-excludes the backward materialization};\qquad\text{contrast class: the deficit-12 ceilings are range bounds on reads}\ [\mathrm{FT.76}(3),\ \mathrm{FT.79}(2)]\ \text{— the present obstruction is a domain restriction, prior to every read};$$
$$(4)\quad\textbf{the vacuum residence:}\ \ \text{the reversed reading exists only as formal bookkeeping. Two distinct reversals, adjudicated separately:}$$
$$\text{(i)}\ \Theta_{\mathfrak L}\ (T):\ \text{ledger order reversed}\ \wedge\ J^+\leftrightarrow J^-\ [\mathrm{D2.7};\ \mathrm{FT.133}(1)]:\ \text{an involution on configuration data}\ [\text{machine: it bijects the completed admissible sequences onto themselves, counts preserved — the formal mirror}];$$
$$\text{(ii) the pure order reversal}\ (\text{the ledger read backwards, labels unchanged — ``running the arrow in reverse''}):\ \text{every completed nonempty admissible history ends with}\ J^-\ (n_{\mathcal R}\ \text{returns to}\ 0\ \text{only via}\ 1\to0),\ \text{so its pure reversal leads with}\ J^-:\ \text{inadmissible at the first event}\ [\text{machine: exhaustive}];$$
$$\text{and the tick sequence admits no inverse in either case}\ [\mathrm{A6}:\ \neg\exists\,\tau^{-1}]:\ \text{the ledger count}\ |\mathfrak L(\tau_n)|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k)\ \text{is non-decreasing along every admissible history}\ (n_{\mathrm{real\_out}}\ge0)\ \text{and strictly increases at every crystallization: the reversed reading of a multi-crystallization history strictly decreases somewhere, and by (ii) the reversal of every completed word is inadmissible at its first event}\ [\text{machine: exhaustive}]\implies\text{no forward tick realization of any reversed reading exists};$$
$$\text{the fluctuation content resides in the}\ \mathcal V\ \text{sector}\ [\mathrm{CT0.1}]:\quad n_{\mathcal R}=0\implies\forall(p,q):\ (p,q)\in\mathcal V\ \wedge\ \rho_{pq}=\rho_\circ=\tfrac14I,\quad S_{\mathrm{raw}}(\rho_\circ)=\ln4=\max,\quad\arg\max=\{\tfrac14I\}\quad[\mathrm{A5},\ \mathrm{CT0.2};\ \text{machine:}\ \mathfrak T\rho_\circ=1,\ \operatorname{charpoly}=(x-\tfrac14)^4,\ \text{dyadic entropy witnesses}<\ln4];$$
$$\text{virtual pairs are unregistered}\ [\mathrm{D1.1}:\ \neg\text{registration}\implies e\in\mathcal V];\qquad\text{chains require real edges}\ [\mathrm{D1.4}:\ e_i\in E_{\mathcal R}]:\ |E_{\mathcal R}|=0\implies\text{the closed-chain count is}\ 0\implies\neg\exists\ \text{fermion terminus}\ [\mathrm{Def\text{-}H.4};\ \text{machine}];$$
$$\text{the fluctuation resolvent is even in balanced pairs:}\quad\sum_n\langle\varnothing|\hat U^n|\varnothing\rangle\,w^n=\frac1{1-w^2x_+x_-}\quad[\mathrm{FT.108}(5)\ \text{re-derived};\ \text{machine in}\ \mathbb Q[w,x_+,x_-]/(w^{12})]:$$
$$\text{every nonzero return monomial carries equal}\ x_+\text{- and}\ x_-\text{-degree}\ [\text{machine degree census}]:\ \text{a}\ J^-\text{-leading monomial has zero support};$$
$$\text{the zero-projection/no-pole pattern applies}\ [\mathrm{CT4.2}:\ \mathcal P_MF\mathcal P_M=0\implies\neg\exists\ \text{accessible pole};\ \mathrm{CT2.5}:\ \text{poles}\iff1\in\operatorname{spec}\mathbf F_M]:\ \text{unregistered content supports no accessible pole at any rung};$$
$$(5)\quad\textbf{carrier reconciliation — single-sector occupancy:}\ \ P_L,P_R=\tfrac12(\mathrm{id}\pm\hat\chi)\ \text{are constructible, exact, rank-}1,\ \hat\omega\text{-exchanged}\ [\mathrm{Def\text{-}H.33},\ \mathrm{FT.122}(2)\text{–}(4);\ \text{machine}]:\ \text{mathematical objects on}\ \mathcal H_\omega\ \text{whether or not occupied};$$
$$\textbf{unconditional}\ (\text{derived}):\ \text{the rung-one materialized locus is single-arrow by}\ (2)\ \text{— one orientation sector of the doublet basis}\ (|c\rangle\ \text{carries the materialized ledger-ordered tuple}\ [\mathrm{D1.4};\ \mathrm{FT.134}(1):\ C,P,T\ \text{fix the chain tuple pointwise}];\ |\omega(c)\rangle\ \text{is the reversal image}\ [\mathrm{D2.6};\ \mathrm{FT.88}(1):\ R\mapsto R^{\mathrm T}]);$$
$$\text{its complement is unoccupied at rung one, and by}\ (4)\ \text{the reversed content is vacuum-sector content}\ (\text{all-virtual, unregistered, no accessible pole});$$
$$\textbf{conditional}\ (\text{the coupling}):\quad|c\rangle=\tfrac1{\sqrt2}\bigl(|L\rangle+|R\rangle\bigr)\quad[\mathrm{Def\text{-}H.34}\ \mathrm{Rmk};\ \text{machine}]:\ \text{the orientation rays carry no definite chirality}\implies\text{transferring single-arrow occupancy to single-ray occupancy requires an arrow}\leftrightarrow\text{ray coupling — the deficit}\ 1'\ \text{assignment rule}\ [\mathrm{FT.125}(4),\ \text{HistLog §IV}/\mathrm{FT.140}(3)];$$
$$\text{the coupling's forced shape is derived: any}\ \hat\omega\text{-covariant coupling maps the single-arrow locus into a single chiral ray}\ (\text{the locus is one sector;}\ \hat\omega\ \text{is the ray exchange}\ [\mathrm{FT.122}(4)];\ \text{machine: exhaustive on the}\ 2!\ \text{bijections}),\ \text{and the complementary ray has occupancy zero at rung one — the vacuum sector of the doublet};$$
$$\text{which of}\ P_L/P_R\ \text{names the occupied ray is reserved naming content}\ [\mathrm{Def\text{-}H.33}\ \text{canonicity Rmk}]:\ \text{the occupancy pair}\ (1,0),\ \text{up to ray exchange, is this clause's entire content};$$
$$(6)\quad\textbf{rung scope — the force-side half opens at rung two:}\ \ \text{at rung one the static force matrix on the extended carrier is}\ \mathbf F_{\mathrm{ext}}(\mathbf c)=h(\mathbf c)\otimes I_\omega\ \text{with}\ F_{LR}=F_{RL}=0\ \text{exactly}\ [\mathrm{FT.127}(9),\ \mathrm{FT.128}(2):\ \text{the no-flip theorem};\ \text{machine}]:\ \text{the two chiral sectors are force-decoupled; the flipping set at the derived locus}=\varnothing\ [\mathrm{FT.128}(6)];$$
$$\text{at rung two EM activates}\ [\mathrm{CT0.13}]\ \text{and the promoted core read opens the unique flip channel:}\quad\mathbf F_{\mathrm{ext}}(\mathbf c,q)=h(\mathbf c)\otimes I_2+q\,I_2\otimes\hat\kappa,\qquad F_{LR}=q\,I_2\ne0\iff q\ne0\quad[\mathrm{FT.129}(4)\text{–}(5),\ \text{Def-H.43};\ \mathrm{EM.9}:\ q\in\{-1,0,+1\}];$$
$$\operatorname{charpoly}\mathbf F_{\mathrm{ext}}(\mathbf c,q)=\operatorname{charpoly}_h(x-q)\cdot\operatorname{charpoly}_h(x+q):\ \text{the chiral-partner splitting}\ 2|q|\in\{0,2\}\ [\mathrm{FT.130}(5);\ \text{machine: Faddeev–LeVerrier over}\ \mathbb Q(i)]:\ \text{both chiral sectors become force-coupled for charged cores};$$
$$\text{at rung three colour adds no carrier flip: sealed ends are blind}\ [\mathrm{FT.117}],\ \text{colour acts on the slot carrier}\ [\mathrm{FT.127}(7)],\ \text{the seed is colour-neutral by theorem}\ [\mathrm{EW.32}]:\ \text{the flipping set remains}\ \{F_{\mathrm{EM}}\ \text{core read}\}\ \text{— minimal and unique}\ [\mathrm{FT.129}(5);\ \text{machine: removing the}\ \hat\kappa\ \text{term kills}\ F_{LR}\ \text{at every profile}];$$
$$\text{the arrow law of}\ (2)\ \text{is rung-blind}\ [\mathrm{D1.2}'\text{s domains carry no rung argument}]:\ \text{what is rung-one specific is the coincidence of the two obstructions — no flip channel (force side)}\ \wedge\ \text{single-arrow locus (ledger side)};\ \text{the single-sector theorem is a rung-one theorem},\ \neg\ \text{a universal law}.$$

### FT.156 — The 3+1 asymmetry theorem: one signature datum at two loci, and the manifold structure as the chiral structure

**Thm.** On the pair channel $\mathfrak H(\mathbb C^4)$ and the emergent geometry [CT2.6; conditions (ii)–(iii) inherited at the point of use — A §0.2a]:
$$(1)\quad\textbf{one signature datum, two loci:}\qquad\mathrm{A3}\ \text{declares the register involution with the Lorentz signature:}\quad T(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu\,(\sigma_\mu\otimes\sigma_\nu),\quad\eta=(-,+,+,+),\quad T^2=\mathbb1;$$
$$\mathrm{CT1.12}\ \text{derives the signature of the emergent metric:}\quad\operatorname{sig}(g_{\mu\nu})=\operatorname{sig}(\bar g_{\mu\nu})=(-,+,+,+)\quad[\varkappa\|q\|_{\mathrm{op}}<1\ \text{regime}];$$
$$\text{the same}\ (-,+,+,+)\ \text{sign pattern grades the register basis}\ [\mathrm{C3}:\ \mathcal E_{st}]\ \text{and the metric on}\ M\ [\mathrm{CT2.6}]:\ \text{one temporal sign and three spatial signs at each locus}\ [\text{machine: the}\ T\text{-table on the}\ 16\text{-element CT1.2 basis via exact Pauli-tensor decomposition over}\ \mathbb Q(i)];$$
$$(2)\quad\textbf{the block census is the component census; the}\ 7/3\ T\textbf{-split is the}\ 3{+}1\ \textbf{split of the dictionary:}\qquad(7,3,3,3)\ [\mathrm{CT1.1}];\qquad S\text{-even}=10=7+3\ [\mathrm{CT1.2};\ \mathrm{FT.141}(1)];$$
$$S\text{-even}= \text{the reality-preserving sector}\ ([\mathbb S,X]=0\ \text{preserves}\ \vee^2,\ \wedge^2\ [\mathrm{CT0.7}(3)]);\qquad S\text{-odd}=6=\{J_i\ (3),\ K_i\ (3)\}= \text{the reality-exchanging sector}\ (\text{the seals}\ [\mathrm{CT0.7}(3)\text{–}(4);\ \mathrm{D1.2}]);$$
$$\text{within the}\ S\text{-even block:}\quad T\text{-even}\ 7=\{E_0,\ \Sigma,\ \hat E^{ij}\ (5)\}=\{D^+,\ H,\ G\}\ [\mathrm{CT0.12};\ \mathrm{CT1.10}:\ \mathbf 1\oplus\mathbf 5\oplus\mathbf 1];\qquad T\text{-odd}\ 3=\{W_i\}=F_W;$$
$$\text{the dictionary}\ [\mathrm{D2.1},\ \mathrm{CT1.12}]:\qquad(a_{00},\ q_{ij})=(1{+}6)\ T\text{-even coefficients}\ \longmapsto\ \bigl(\Omega=e^{\alpha_\Omega a_{00}},\ \ \bar g_{ij}=\delta_{ij}+\varkappa q_{ij}\bigr)=\text{lapse/conformal}\ +\ \text{spatial metric};$$
$$w_i\ (3)\ T\text{-odd coefficients}\ \longmapsto\ N_i=\beta w_i=\text{shift}=\text{the time–space cross components}\ \bar g_{0i};\qquad\text{components:}\quad g_{00}:1;\quad g_{ij}:6=\tfrac{3\cdot4}2;\quad g_{0i}:3;\quad\text{total}\ 10=\tfrac{4\cdot5}2\ [\mathrm{CT1.12}];$$
$$\text{the temporal direction contributes exactly one component and one coefficient}\ (g_{00}=-\Omega^2\ \text{from the single}\ T\text{-even conformal coefficient}\ a_{00});\ \text{the spatial triad contributes the symmetric sextuple}\ q_{ij}\ \text{and the three shifts}\ w_i:$$
$$\text{the}\ 7/3\ T\text{-split of the}\ S\text{-even block is the operator-side encoding of the}\ (1;6;3)\ \text{component split with signature}\ (-,+,+,+);\qquad\text{the}\ S\text{-odd block has}\ 0\ \text{metric coordinates}\ [\mathrm{FT.141}(5);\ \mathrm{FT.30}\ \text{dictionary}];$$
$$(3)\quad\textbf{the reversal transport:}\ \ \text{the}\ T\text{-grading transports through the dictionary exactly to the time-reversal pullback:}\quad\text{with}\ J=\operatorname{diag}(-1,1,1,1)\ \text{and the}\ T\text{-action on sector data}\ (a_{00},q,w)\mapsto(a_{00},q,-w)$$
$$[T(E_0)=E_0,\ T(E^{ij})=E^{ij},\ T(W_i)=-W_i;\ \text{machine, entrywise}]:\qquad\bar g_{\mu\nu}(a_{00},q,-w)=J^{\rho}{}_{\mu}\,\bar g_{\rho\sigma}(a_{00},q,w)\,J^{\sigma}{}_{\nu}\qquad[\text{machine: exact rational witnesses}];$$
$$\text{lapse and spatial metric fixed, shift negated:}\quad\Omega\mapsto\Omega,\quad\bar g_{ij}\mapsto\bar g_{ij},\quad N_i\mapsto-N_i\qquad\Longleftrightarrow\qquad g_{00},\ g_{ij}\ \text{fixed},\quad g_{0i}\mapsto-g_{0i}\ [\Omega\ \text{depends on the}\ T\text{-even}\ a_{00}\ \text{alone}\ [\mathrm{D2.1}]];$$
$$\text{the signature is reversal-invariant:}\quad\operatorname{sig}\bar g(w)=\operatorname{sig}\bar g(-w)=(-,+,+,+)\qquad[\text{machine: exact rational}\ \mathrm{LDL}^\top\ \text{inertia on a}\ 12\text{-point witness lattice}\ (q,w);\ \text{Sylvester criterion on}\ \bar g_{ij};\ \det\bar g<0\ \text{via the CT1.12 Schur form}];$$
$$(4)\quad\textbf{space is symmetric and reversible:}\ \ \text{the spatial triad rotates innerly:}\quad\operatorname{span}\{W_i\}\cong\mathfrak{su}(2)\ [\mathrm{CT1.4}];\qquad J,K:\ \text{vectors},\quad\hat E^{ij}:\ \mathbf 5,\quad E_0,\Sigma:\ \mathbf 1\ \ \text{under the adjoint action}\ [\mathrm{CT1.8},\ \mathrm{CT1.10},\ \mathrm{CT1.5}];$$
$$\text{every permutation of the three triad indices is realized by an inner unitary that is a rational polynomial in the weak generators alone:}$$
$$\text{cyclic:}\quad U=u\otimes u,\ u=\tfrac12\bigl(I_2-i(\sigma_1+\sigma_2+\sigma_3)\bigr)\ [\mathrm{FT.111}]:\qquad U=\exp\!\bigl(-\tfrac{2\pi i}{3}\,\hat n\cdot W\bigr)=E_0-\tfrac12\mathcal W^2-\tfrac i2\mathcal W,\quad\mathcal W:=W_1{+}W_2{+}W_3,\quad\hat n=\tfrac{(1,1,1)}{\sqrt3},$$
$$\text{via the polynomial identity}\ \mathcal W^3=3\mathcal W\ [\operatorname{spec}(\hat n\cdot W)=\{1,0,-1,0\};\ \text{machine}];\qquad U^3=E_0;\qquad U X_i U^\dagger=X_{i+1}\ \ \forall X\in\{W,J,K\}\ (\text{indices mod}\ 3)\ [\mathrm{FT.111}(1)\ \text{re-derived, plus the}\ W\text{-row};\ \text{machine}];$$
$$\text{transpositions:}\quad U_{ij}=\exp\bigl(-i\pi\,\tfrac{W_i+W_j}{\sqrt2}\bigr)=E_0-(W_i+W_j)^2:\qquad U_{ij}^2=E_0;\qquad U_{ij}:\ X_i\leftrightarrow X_j,\ X_k\mapsto-X_k\ \ \forall X\in\{W,J,K\}\ [\text{machine: the full conjugation table on}\ \{W,J,K,\hat E\}];$$
$$\text{the reversal involutions are exact: on the register}\ [S^2=T^2=\mathbb1\ [\mathrm{A3}]],\ \text{on configuration data}\ [\langle C,P,T,\omega\text{-pattern}\rangle\cong\mathbb Z_2^4,\ \text{register-disjoint}\ [\mathrm{FT.133}(1)\text{–}(2)]];$$
$$(5)\quad\textbf{time is asymmetric and strictly forward:}\ \ \neg\exists\,\tau^{-1}\ [\mathrm{A6}:\ \tau_n\to\tau_{n+1}:\ \rho\mapsto\mathcal T(\rho)];\qquad|\mathfrak L(\tau_{n+1})|=|\mathfrak L(\tau_n)|+n_{\mathrm{real\_out}}(\tau_n)\ge|\mathfrak L(\tau_n)|\ [\mathrm{A6},\ \mathrm{A7}:\ \mathfrak L(\tau_n)\subseteq\mathfrak L(\tau_{n+1})];$$
$$\text{the D1.2 seal domains force strict alternation and the prefix law; every completed nonempty history ends in}\ J^-,\ \text{and its pure order reversal is inadmissible at the first event}\ [\mathrm{FT.144}(2),\ (4)(\mathrm{ii});\ \text{machine: exhaustive at lengths}\le8];$$
$$\Theta_{\mathfrak L}\ [\mathrm{D2.7}]\ \text{is the formal mirror — an involution on configuration data bijecting the completed admissible set onto itself}\ [\mathrm{FT.144}(4)(\mathrm{i});\ \text{machine}]\ —\ \neg\text{a dynamical inverse:}$$
$$\text{the asymmetry is exact: the spatial-axis reversals are inner unitaries on the force arena}\ [(4)];\qquad\text{the temporal advance reversal has no implementation}\ [\mathrm{A6};\ \mathrm{FT.144}(3):\ \text{a domain restriction, prior to every read}];$$
$$(6)\quad\textbf{the chiral structure is the manifold structure:}\ \ \text{the chirality of the complete force complex at rung one is the}\ 10/6\ S\text{-grading}\ [\mathrm{FT.141}(2)];\ \text{its}\ (S,T)\ \text{refinement}\ (7,3,3,3)\ [\mathrm{CT1.1}]\ \text{is the dictionary carrier of the metric}\ [\mathrm{CT1.12};\ (2)];$$
$$\text{the weak block is the}\ T\text{-odd part of the}\ S\text{-even block} = \text{the metric's own time–space cross block}\ [\mathrm{CT0.12}:\ F_W=\mathcal E_{+-}=\operatorname{span}\{W_i\};\ \mathrm{D2.1}:\ X_{(-)}=w_iW_i;\ \mathrm{CT1.12}:\ w_i\mapsto N_i];$$
$$\text{the chiral asymmetry}\ (10\ne6)\ \text{and the}\ 3{+}1\ \text{asymmetry are one graded structure read at three derived loci:}$$
$$\text{the operator locus}\ (10,6)=(7{+}3,\ 3{+}3);\qquad\text{the component locus}\ (1;6;3)\ \text{with}\ \operatorname{sig}=(-,+,+,+);\qquad\text{the state locus}\ \operatorname{spec}\mathbb S=(3,1)\ [\mathrm{CT0.7}(1);\ \mathrm{FT.157}];$$
$$\text{locus discipline}\ [\mathrm{FT.136}(5);\ \mathrm{FT.141}(4)]:\ \text{three distinct spaces}\ (\operatorname{End}(\mathbb C^4_{\mathrm{pair}}),\ \text{the metric on}\ M,\ \mathbb C^4_{\mathrm{pair}});\ \text{the counts are the derived content; no carrier identification is made}.$$

### FT.158 — The spatial provenance of the channel angle: $C_3$ is the weak rotation of the triad, and the Koide-form spectrum is forced

**Thm.** With the seal bilinear $[J_i,K_j]$ [FT.109], the $C_3$-covariant spectrum [FT.111], the mixing angle $\delta=\tfrac29$ [FT.112], and the bilinear spectrum $r_i$ [FT.113]:
$$(1)\quad\textbf{the}\ C_3\ \textbf{is generated by the weak generators:}\ \ \mathrm{FT.111}\text{'s inner rotation}\ U=u\otimes u,\ u=\tfrac12\bigl(I_2-i(\sigma_1+\sigma_2+\sigma_3)\bigr),\ \text{is the}\ \tfrac{2\pi}3\ \text{rotation about the}\ (1,1,1)\ \text{axis generated by the total-spin/weak generators:}$$
$$U=\exp\!\bigl(-\tfrac{2\pi i}3\,\hat n\cdot W\bigr)=E_0-\tfrac12\mathcal W^2-\tfrac i2\mathcal W,\qquad\mathcal W=W_1{+}W_2{+}W_3,\qquad\hat n=\tfrac{(1,1,1)}{\sqrt3}\qquad[\text{exact polynomial identity over}\ \mathbb Q(i),\ \text{via}\ \mathcal W^3=3\mathcal W;\ \text{machine}];$$
$$U^3=E_0;\qquad U J_i U^\dagger=J_{i+1},\quad U K_i U^\dagger=K_{i+1},\quad U W_i U^\dagger=W_{i+1}\quad(\text{indices mod}\ 3)\qquad[\mathrm{FT.111}(1)\ \text{re-derived, plus the}\ W\text{-row};\ \text{machine}]:$$
$$C_3\le SO(3)\ —\ \text{the cyclic permutation of the three spatial directions}\ [\mathrm{CT1.8}:\ \text{the triad}\ SO(3);\ \mathrm{CT1.4}:\ \operatorname{span}\{W\}\cong\mathfrak{su}(2)]\ —\ \text{is inner in the weak rotation algebra};$$
$$(2)\quad\textbf{the numerator}\ 2=3-1\ \textbf{is the doublet dimension of the spatial triad:}\qquad\text{the diagonal bilinear splits singlet}\ \oplus\ \text{doublet}\ [\mathrm{FT.111}(1)]:\ \ \text{the fixed direction}\ \Sigma\ \oplus\ \text{the zero-sum plane}\ \textstyle\sum_i\hat E^{ii}=0,\ \dim=2\ [\text{machine: exact rank}];$$
$$\text{the cyclic shift on the plane:}\quad\operatorname{charpoly}=\text{minimal polynomial}=x^2+x+1,\ \ \text{irreducible over}\ \mathbb Q\ (\pm1\mapsto3\ne0)\ [\mathrm{FT.111}(1)\ \text{re-derived};\ \text{machine}];$$
$$\textstyle\sum_i[J_i,K_i]=i\sum_i\bigl(\Sigma-E^{ii}\bigr)=i\bigl(3\Sigma-\Sigma\bigr)=2i\Sigma\qquad[\mathrm{FT.109}(1)\text{–}(3)\ \text{re-derived};\ \text{machine}]:$$
$$\text{the coefficient}\ 2=3-1\ —\ \text{the triad count minus its trace}: \text{one integer at two derived reads}\ (\dim\ \text{doublet};\ \Sigma\text{-coefficient})\ [\text{exact integers}];$$
$$(3)\quad\textbf{the denominator}\ 9=3\times3;\ \ \delta=\tfrac29\ \textbf{is a ratio of spatial counts:}\qquad\dim F_{J^\pm}=3\ [\mathrm{CT0.12};\ \text{machine: exact rank}]\ —\ \text{the seal-triplet dimension} = \text{the triad dimension on which}\ SO(3)\ \text{acts}\ [\mathrm{CT1.8}];$$
$$\operatorname{tr}T(1)=3\ [\mathrm{FT.110}(2):\ \operatorname{charpoly}T(1)=x^4-3x^3-3x^2;\ \text{machine: exact re-derivation from the transfer rule}\ T(1)[s][s']=[\,|s|+|s'|\le3\,]];$$
$$\delta=\frac{\sum_i[J_i,K_i]\big|_\Sigma}{\dim F_{J^\pm}\cdot\operatorname{tr}T(1)}=\frac{2}{3\cdot3}=\frac29\qquad[\mathrm{FT.112}\ \text{re-derived};\ \text{machine: exact Fractions}];$$
$$\text{the arena reading carries Tier F.37's interface provenance}\ [\mathrm{Def\text{-}H.41}\ —\ \text{cited},\ \neg\text{imported here}]:\qquad\text{the angle's constituents are the doublet dimension, the seal dimension, the transfer trace — integer counts of the spatial channel, no datum, no fit};$$
$$(4)\quad\textbf{the Koide-form spectrum is forced:}\qquad r_i=1+\sqrt2\cos\bigl(\tfrac29+\tfrac{2\pi i}3\bigr)\ [\mathrm{FT.113}]:\ \ \text{the shape from}\ C_3\text{-covariance}\ [\mathrm{FT.111}(2):\ \lambda_i=A+B\cos(\theta+\tfrac{2\pi i}3)\ \text{for every}\ C_3\text{-covariant Hermitian triplet operator}];$$
$$A=1,\ B=\sqrt2\ \text{from the democratic normalization to the seal dimension}\ 3\ [\mathrm{FT.111}(3):\ \textstyle\sum_i\lambda_i=3=\dim F_{J^\pm},\ \sum_i(\lambda_i-A)^2=3];\qquad\theta=\delta\ \text{from}\ (2)/(3);$$
$$\text{machine:}\quad\textstyle\sum_ir_i=3,\quad\sum_{i<j}r_ir_j=\tfrac32,\quad 2(r_i-1)^3-3(r_i-1)-\sqrt2\cos\tfrac23=0\ \ \forall i\qquad[\text{exact in}\ \mathbb Q(\sqrt2,\sqrt3)[c,s]/(c^2{+}s^2{-}1);\ \cos\tfrac23=4c^3-3c\ \text{at}\ c=\cos\tfrac29];$$
$$\text{the Koide formula is a consequence of the}\ C_3\ \text{symmetry of the}\ 3\ \text{spatial directions};\qquad\text{the scale}\ \mu\ (\text{P4-class})\ \text{enters no ratio}\ [\mathrm{FT.113}];$$
$$(5)\quad\textbf{the supersession of FT.89's classification clause:}\qquad\tfrac23=\tfrac{3-1}3=\frac{\dim\ \text{doublet}}{\dim\ \text{triplet}}\ —\ \text{the decomposition ratio of the spatial seal triad under its inner rotation subgroup}\ [\mathrm{FT.111}(1):\ \mathbf 3=\mathbf 1\oplus\mathbf 2;\ \text{machine: exact Fractions}];$$
$$\delta_\ell=\tfrac29=(\tfrac23)/3\ [\mathrm{FT.112}\ \mathrm{Rmk}]:\qquad\text{the three cross-check rationals}\ (p^*_\infty)^2=\tfrac23\ [\mathrm{FT.70}(3);\ \text{exact in}\ \mathbb Z[\sqrt6]],\quad\delta_v/\pi=2-\tfrac43=\tfrac23\ [\mathrm{FT.63}(4)],\quad f_{\mathrm{charge}}(\delta h{=}3)=\tfrac23\ [\mathrm{FT.14}]$$
$$\text{equal}\ (3-1)/3\ \text{exactly}\ [\text{machine}]:\qquad\mathrm{FT.89}(2\mathrm d)\text{'s classification of the rational}\ \tfrac23\ \text{``cap-3 combinatorial output''}\ \text{and}\ (5)\text{'s verdict on the Koide-form structure}\ \text{``coincidence;\ no structural claim''}\ \textbf{are superseded}:$$
$$\text{the corpus-side Koide-form angle and spectrum have the derived spatial provenance}\ (1)\text{–}(4);\qquad\textbf{unchanged and standing:}\ \ \mathrm{FT.89}(1)\text{'s arithmetic}\ (\text{exact, frozen});\ \ (3)\text{'s refutation};\ \ (4)\text{'s negatives};$$
$$\text{the inadmissibility grounds}\ (2\mathrm a)\text{–}(2\mathrm c)\ \text{and the identification bars: no family-mass read exists in the corpus},\ \neg\exists\ \text{a declared map relating derived rationals to measured mass ratios},\ \text{external data enters no derivation}\ [\mathrm{P1},\ \mathrm{P5}];$$
$$\text{the cap-sensitivity arithmetic}\ [(2\mathrm d):\ c=2\to0.508004\ldots;\ c=4\to\neg\exists\ \text{interior boundary}]\ \text{stands as the exact polygon-ensemble record};\qquad\text{the scale}\ \mu\ \text{remains undeclared}\ (\text{P4}).$$
