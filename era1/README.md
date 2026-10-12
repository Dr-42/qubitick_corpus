# `era1/` — Era 1 · Levels 1–4 · the FROZEN v1.0 canon half

**Status: FROZEN.** This is the first of the repository's two era halves. Era 1 = the published
**Qubitick Corpus v1.0 (revision 1)** — Levels 1–4, the four eras **Qubit · Bosonic · Fermion ·
Baryomesonic** — machine-verified **80/80**, deposited on Zenodo
(**DOI: 10.5281/zenodo.23266001**). Nothing in this folder is edited; corrections and
supersessions to v1.0 rows are recorded downstream in the sibling half (`../era2/`) with explicit
locus citations (e.g. the BM.140(6) coherence defect found at AT.7 is tracked as a pin checker,
never as an edit here).

## Layout

| path | content |
|---|---|
| `canon/` | **the living canon v1.0**: `Part1_Qubit_era.md` … `Part4_Baryomesonic_era.md`, `Census.md`, `HistLog.md`, the regenerable `Summary.md` (Summary of Record) and `index/` (`tags.json`, `graph.md`, `dependency_tree.md`), plus `corpus_lib.py` and `make_summary.py` — **the summary-generation pipeline** (HERE-relative; run from this folder) |
| `verification/` | **the frozen 80-checker suite**: `run_all.py`, `requirements.txt` (a documented no-op — pure stdlib), `checks/` (the 80 checkers and their exact-arithmetic helpers). The canon documents at this folder's root are **symlinks into `../canon/`** — `canon/` and `verification/` are therefore sibling-locked and move together; `index/` here is regenerated at every suite run |

## Run

```bash
python3 verification/run_all.py          # -> 80/80 passed, ALL GREEN, exit 0 (takes minutes)
cd canon && python3 make_summary.py      # regenerate Summary.md (the Summary-of-Record pipeline)
```

## Relation to the rest of the repository

- **`../era2/`** — the sibling half: the Era-2 record (Levels 5–7: Atomic · Isotopic ·
  Anthropic). **Level 5 (the Atomic era) is CLOSED** at tag AT.63 (Tier AT.12); its 14 tier
  documents cite this half's 640-tag registry and are citation-gated against it
  (`../era2/level5_atomic/checks/check_era2_format.py` reads `canon/` here).
- **`../source/`** — the publication pipeline (PDF generation): it reads `canon/index/tags.json`
  and the frozen archive `../working_markdowns/` (which stays at the repository root, unmodified),
  and writes `../docs/*.pdf`. Path constants were updated at the Level-5 closure reorganization;
  pipeline behavior is unchanged.
- **`../archive/zenodo_v1.0_package/`** — the self-contained deposited copy of v1.0 as published
  (frozen; independent of this folder's live tree).
- **`../working_markdowns/`** (root) — the byte-identical pre-revision provenance archive; never
  modified.

**Charter.** Era 1 is the dependency root: every Era-2 tag cites Parts 1–4 (this folder) and
earlier AT-tags only — the era chain is strictly acyclic (machine: the era-2 format gate's F3
citation attestation against this folder's registry).
