#!/usr/bin/env python3
"""
run_all_era2.py -- the Level 5 / Atomic-era check runner.

Mirrors verification/run_all.py's contract: run every checker in this folder,
report exact-arithmetic marker counts and failures, exit 0 iff all green.

Discovery order is fixed (not alphabetical) so the VALIDATION GATES run first:
nothing downstream is admissible unless the canon-reproduction gates pass.

All arithmetic is exact: Fraction, Z[x], multivariate Q[gamma,G,a],
complex-over-Fraction, exact 4x4 matrices over Fraction, the prime-log ring
Q[ln2,ln3], and rigorous Fraction intervals for transcendentals.
NO FLOATING POINT IN ANY ASSERTION.
"""
import glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GATES = ["validate_against_canon.py", "census_L5.py"]          # must pass first
HELPERS = {"qexact.py", "run_all_era2.py"}

PASS_RE = re.compile(r"\[(EXACT|OK  |COHERENT|CLOSED)\]|ALL PASS|ALL REPRODUCE")
FAIL_RE = re.compile(r"\[FAIL|\[  BROKEN|Traceback")

def run(path):
    r = subprocess.run([sys.executable, path], cwd=HERE,
                       capture_output=True, text=True)
    out = r.stdout + r.stderr
    good = len(PASS_RE.findall(out))
    bad = len(FAIL_RE.findall(out))
    return r.returncode, good, bad, out

def main():
    files = [f for f in GATES if os.path.exists(os.path.join(HERE, f))]
    files += sorted(f for f in glob.glob(os.path.join(HERE, "*.py"))
                    if os.path.basename(f) not in HELPERS
                    and os.path.basename(f) not in GATES)
    print("=" * 78)
    print("ERA 2 / LEVEL 5 -- THE ATOMIC ERA -- exact-arithmetic check suite")
    print("=" * 78)
    tot_g = tot_b = 0
    rows = []
    for f in files:
        rc, g, b, out = run(f)
        name = os.path.basename(f)
        gate = " (GATE)" if name in GATES else ""
        status = "PASS" if (rc == 0 and b == 0) else "FAIL"
        rows.append((name + gate, status, g, b))
        tot_g += g; tot_b += b
        print(f"  {status:<5} {name + gate:<34} exact={g:<4} fail={b}")
        if status == "FAIL":
            tail = "\n".join(out.strip().splitlines()[-12:])
            print("        " + tail.replace("\n", "\n        "))
    print("-" * 78)
    print(f"  {len(rows)} checkers, {tot_g} exact markers, {tot_b} failures")
    ok = (tot_b == 0 and all(r[1] == "PASS" for r in rows))
    print(f"  run_all_era2: {'ALL GREEN' if ok else 'FAILURES PRESENT'}")
    print("=" * 78)
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
