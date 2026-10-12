#!/usr/bin/env python3
"""run_all.py — package-level entry point for the Qubitick verification suite.

Runs every companion checker in ``checks/`` (auto-discovered: every
``verify_*.py`` plus ``check_format.py``, which runs last) as a subprocess with
the working directory set to ``checks/``, so relative paths and sibling imports
resolve exactly as when invoked by hand. This wrapper does not modify any
checker; ``checks/run_all.py`` remains the suite's own runner, and this file
provides the package entry point of the v1.0 layout.

The canon documents read by the checkers (Part1-4, Census, HistLog, Summary,
README.md) live at this folder's top level as symlinks into
``../working_markdowns/`` — the archive is read-only provenance and is never
written to by the suite. ``index/`` holds the regenerable registry/graph
outputs, rewritten by ``verify_corpus_graph.py`` at every run.

Usage:
    python3 run_all.py                 # run everything; exit 0 iff all pass
    python3 run_all.py --list          # print the discovered order and exit
    python3 run_all.py verify_B.py ... # run only the named checkers

Expected output on the delivered corpus: 79/79 passed — ALL GREEN.
Pure Python 3 standard library; exact arithmetic only, no floating point.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKS = os.path.join(HERE, "checks")

CANON = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
         "Part4_Baryomesonic_era.md", "Census.md", "HistLog.md", "Summary.md",
         "README.md", "index"]


def discover():
    """The ordered checker list in checks/: alphabetical, check_format.py last."""
    names = []
    for fn in os.listdir(CHECKS):
        if not fn.endswith(".py") or fn == "run_all.py":
            continue
        if fn.startswith("_") or fn.startswith("."):
            continue
        if fn == "check_format.py" or fn.startswith("verify_"):
            names.append(fn)
    tail = [n for n in names if n == "check_format.py"]
    head = sorted(n for n in names if n != "check_format.py")
    return head + tail


def preflight():
    missing = [f for f in CANON if not os.path.exists(os.path.join(HERE, f))]
    if missing:
        print("run_all: missing canon documents at the verification root:", missing,
              file=sys.stderr)
        print("         (they are symlinks into ../working_markdowns/ — restore the "
              "archive or the links)", file=sys.stderr)
        return False
    return True


def run_one(script):
    path = os.path.join(CHECKS, script)
    print("=" * 72)
    print(f":: {script}")
    print("=" * 72)
    rc = subprocess.call([sys.executable, path], cwd=CHECKS)
    print()
    return rc


def main(argv):
    if len(argv) > 1 and argv[1] == "--list":
        for s in discover():
            print(s)
        return 0
    if not preflight():
        return 2
    if len(argv) > 1:
        scripts = []
        for s in argv[1:]:
            if not os.path.exists(os.path.join(CHECKS, s)):
                print(f"run_all: no such checker: {s}", file=sys.stderr)
                return 2
            scripts.append(s)
    else:
        scripts = discover()
    if not scripts:
        print("run_all: no checkers found in", CHECKS, file=sys.stderr)
        return 1

    results = {}
    for s in scripts:
        try:
            results[s] = run_one(s)
        except KeyboardInterrupt:
            print(f"\nrun_all: aborted while running {s}")
            return 130

    print("=" * 72)
    print("SUMMARY")
    bad = [s for s, rc in results.items() if rc != 0]
    width = max(len(s) for s in results)
    for s, rc in results.items():
        tag = "PASS" if rc == 0 else f"FAIL({rc})"
        print(f"  {tag:<8}  {s:<{width}}")
    print("-" * 72)
    print(f"run_all: {len(results) - len(bad)}/{len(results)} passed "
          f"(discovered {len(scripts)})")
    if bad:
        print(f"run_all: FAILED ({len(bad)}): {bad}")
        return 1
    print("\nrun_all: ALL GREEN")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
