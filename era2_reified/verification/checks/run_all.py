#!/usr/bin/env python3
"""
run_all.py — Unified check runner for era2_reified.

Usage:
  cd era2_reified/verification/checks && python3 run_all.py
"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
CANON_DIR = os.path.join(PARENT, "canon")

PART5 = os.path.join(CANON_DIR, "Part5_Atomic_era.md")
PART6 = os.path.join(CANON_DIR, "Part6_Isotopic_era.md")
PRIOR = os.path.join(os.path.dirname(HERE), "..", "..", "..", "..", "era1", "canon")

print("=" * 60)
print("era2_reified verification suite")
print(f"  Part 5: {PART5}")
print(f"  Part 6: {PART6}")
print(f"  Prior parts: {PRIOR}")
print("=" * 60)
print()

result = subprocess.run(
    [sys.executable, os.path.join(HERE, "verify_Atomic5_6.py"), PART5, PART6, PRIOR],
    cwd=HERE,
)

print()
sys.exit(result.returncode)
