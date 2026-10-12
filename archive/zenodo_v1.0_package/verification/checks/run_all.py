
"""
run_all.py — run the whole Qubitick verification suite.

Auto-discovers every companion checker lying next to this file:

  * every  verify_*.py   (e.g. verify_B.py, verify_H.py, verify_H_loops.py, ...)
  * plus   check_format.py  (structural validator, run last)

Nothing needs editing here when new verify_*.py companions are added —
drop the file in and it is picked up on the next run. Helper modules that
are *not* checkers (q5.py, qmath.py, hcommon.py, solids.py, compute*.py,
patch_*.py, this file itself, anything starting with '_' or '.' or named
with a leading underscore) are ignored.

Each checker is run as a subprocess with the current directory set to
the folder containing this script, so relative paths and sibling imports
work exactly as when invoked by hand.

Usage:
    python3 run_all.py                 # run everything, exit 0 iff all pass
    python3 run_all.py --list          # print the discovered order and exit
    python3 run_all.py verify_H_loops.py verify_H_rungs.py
                                       # run only the named checkers

Exit code 0 = every discovered / requested script exited 0.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# -------- discovery ---------------------------------------------------------

def discover():
    """Return the ordered list of checker scripts in HERE.

    Order: check_format.py last; everything else alphabetically.
    A deterministic order keeps the SUMMARY column stable across runs.
    """
    names = []
    for fn in os.listdir(HERE):
        if not fn.endswith(".py"):
            continue
        if fn == os.path.basename(__file__):
            continue
        if fn.startswith("_") or fn.startswith("."):
            continue
        if fn == "check_format.py" or fn.startswith("verify_"):
            # skip obvious helper modules that happen to start with verify_
            # (none currently, but be defensive: a module with no __main__
            # will simply exit 0 and be reported as such)
            names.append(fn)
    # check_format.py last, if present
    tail = [n for n in names if n == "check_format.py"]
    head = sorted(n for n in names if n != "check_format.py")
    return head + tail


# -------- execution ---------------------------------------------------------

def run_one(script):
    path = os.path.join(HERE, script)
    print("=" * 72)
    print(f":: {script}")
    print("=" * 72)
    try:
        rc = subprocess.call([sys.executable, path], cwd=HERE)
    except KeyboardInterrupt:
        print(f"\n{script}: interrupted by user")
        raise
    print()
    return rc


def main(argv):
    if len(argv) > 1 and argv[1] == "--list":
        for s in discover():
            print(s)
        return 0

    if len(argv) > 1:
        # explicit selection; still verify each exists
        requested = []
        for s in argv[1:]:
            if not os.path.exists(os.path.join(HERE, s)):
                print(f"run_all: no such script: {s}", file=sys.stderr)
                return 2
            requested.append(s)
        scripts = requested
    else:
        scripts = discover()

    if not scripts:
        print("run_all: no checkers found in", HERE)
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
