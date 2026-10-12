# legacy_checks/ — session-1 checker copies (provenance, NOT live)

The early discovery-phase checkers as they first stood in the top-level `era2/` working folder
(session 1). **The live versions of everything the suite runs are in `../../checks/`** — these
copies are kept only as the provenance record of the discovery folder.

- Files identical to their live counterparts at the time of the move: `beta31.py`,
  `census_L5.py`, `em_split.py`, `m1_shift.py`, `m1pp_shift.py`, `m1ppp_bm34.py`,
  `magnetic_functional.py`, `mixed_edges.py`, `one_force.py`, `validate_against_canon.py`,
  `verify_spin_stats.py`.
- Files that had diverged from (or never entered) the live suite: `build_census.py`
  (discovery-only), `coherence_census.py` and `qexact.py` (early variants; the live ones in
  `../../checks/` are the evolved versions the runner uses).

Nothing imports from this folder. `run_all_era2.py` never sees it.
