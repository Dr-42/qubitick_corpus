#!/usr/bin/env python3
"""
run_all_level6.py -- the Level 6 / Isotopic-era check runner.

Mirrors the Level-5 runner's contract (run_all_era2.py): run every checker in this folder,
report exact-arithmetic marker counts and failures, exit 0 iff all green.  The format +
citation gate runs FIRST: nothing downstream is admissible unless the tier documents pass
(math balance, IT-block anatomy, citation attestation against the era-1 canon registry AND
the closed Level-5 record).

Shared libraries: this level borrows `qexact.py` and `duality.py` from
../level5_atomic/checks via sys.path (documented dependency, single source of truth --
recorded in the level README and in AT.63(9)'s inheritance list).

All arithmetic is exact: Fraction, Gauss(i)-over-Fraction, rigorous Fraction intervals,
truncated Q[[gamma]] series, integer certificates.  NO FLOATING POINT IN ANY ASSERTION.
"""
import glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GATES = ["check_level6_format.py"]                                 # must pass first
HELPERS = {"run_all_level6.py", "check_level6_format.py"}

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
    print("ERA 2 / LEVEL 6 -- THE ISOTOPIC ERA -- exact-arithmetic check suite")
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
    print(f"  run_all_level6: {'ALL GREEN' if ok else 'FAILURES PRESENT'}")
    print("=" * 78)
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
