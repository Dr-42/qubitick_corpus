# Audit_mathematical_verification.md — packaging note (not an original corpus file)

The v1.0 packaging brief listed a mathematical-verification audit document under
this filename. **No such file existed in the source archive** delivered for
packaging (the self-extracting payload containing the `qubitick/` working
tree: the four era files, `Census.md`, `HistLog.md`, the summaries, `index/`,
`checks/`, `paper/` and the render tooling). Rather than fabricate an audit,
this note records that fact and points to the actual verification-of-record
material, all preserved unmodified in this package:

* `HistLog.md` §V — the verification history: per-tier suite states, the
  checker mapped to each tier, and the retirement record.
* `../verification/checks/README.md` — the suite's own architecture document:
  the arithmetic classes (integers, `Fraction`, complex-over-`Fraction`,
  truncated power series, exact radical rings), the archive-gating mechanism
  and the retired checkers.
* `../verification/checks/*.py` — the 79 checkers. Run
  `python3 ../verification/run_all.py`; state at packaging time (2026-10-08):
  **79/79 green**, re-executed inside the package.
* `../verification/index/` — the regenerable tag registry and dependency
  graph (621 registry tags, 8004 Req edges, acyclic), rewritten from the canon
  by `verify_corpus_graph.py` at every suite run.
* `tools/` — the corpus's original render and summary tooling
  (`render_paper.py`, `make_summary.py`, `trace_tags.py`, `corpus_lib.py`), and
  `paper/` — the first compiled paper (tex/pdf/log) as delivered.

— Technical editor, corpus v1.0 sanitization & packaging pass, 2026-10-08.
