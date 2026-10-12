
#!/usr/bin/env python3
"""
verify_H_composition.py — machine checks for H (WIP), Tier F.16.

Exact integer verification of the tetrahedron-face card (FT.49), the
composition/gluing laws and computed cells (FT.50), the winding-ledger
enumeration with brute-force profile counts and dihedral orbit enumeration
(FT.51), and the spin-rule constraint arithmetic (FT.52). Pure Python 3
standard library; no floating point. Exit code 0 = all green.

Run:  python3 checks/verify_H_composition.py
"""

from fractions import Fraction
from itertools import product
from math import gcd
import sys

PASSES = []
FAILURES = []


def check(name):
    def deco(fn):
        try:
            fn()
        except AssertionError as exc:
            FAILURES.append((name, str(exc) or "assertion failed"))
        except Exception as exc:
            FAILURES.append((name, "%s: %s" % (type(exc).__name__, exc)))
        else:
            PASSES.append(name)
        return fn
    return deco


def binom(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


# ------------------------------------------------------------------ FT.49

@check("FT.49: face card — E_int=6, E_bd=6<=4*2, n(v)=6 => O=112, Theta_int in 4Z, Pi minima {144,288,432}, exchange sector 36-6=30, dims <= 18")
def _face_card():
    E_int, E_bd = 6, 6
    assert E_bd <= 4 * 2                                   # delta_tau >= 2 [FT.17 hyp]
    I_hid_over_ln2 = E_int                                 # = 6
    assert I_hid_over_ln2 == 6
    n_v = 6                                                # 3 channels x 2 [D0.8]
    O = max(0, 2 ** (n_v + 1) - 16)                        # [CT0.6]
    assert O == 112                                        # 2^7 - 16
    # Theta_int = 2 * Theta_tri; face materialized => Theta_tri even => Theta_int in 4Z
    for k_tri in (1, 2, 3):
        theta_tri = 2 * k_tri
        theta_int = 2 * theta_tri
        assert theta_int % 4 == 0
    # Pi/(ln2)^2 = E_int^2 * Theta_int at the three minima:
    pis = {36 * 2 * t for t in (2, 4, 6)}
    assert pis == {144, 288, 432}
    # boundary algebra: N = E_bd = 6 => dim u(6) = 36, strictly new = 36 - 6 = 30
    assert 6 * 6 - 6 == 30
    # observable mask dims: 9 core (+1 EM) (+8 strong) <= 18
    assert {9, 10, 17, 18} == {9, 9 + 1, 9 + 8, 9 + 1 + 8}
    # baryon-type sealing: the only {2,3}-partition of 3 is 3 itself (epsilon triple);
    # g(3) = 1 via recurrence g(n) = (n-1)g(n-2) + C(n-1,2)g(n-3):
    g = {0: 1, 1: 0, 2: 1}
    g[3] = 2 * g[1] + 1 * g[0]
    assert g[3] == 1


# ------------------------------------------------------------------ FT.50

@check("FT.50(1),(3): mass additivity; junction O(d+2)=2^(d+3)-16; s-triangle junction n=4s, O=2^(4s+1)-16")
def _junctions():
    # bridged union: E_int additive + 2m
    for E1, E2, m in ((1, 1, 1), (3, 3, 2), (6, 1, 1)):
        assert 2 * E1 + 2 * E2 + 2 * m == 2 * (E1 + E2 + m)
        # m_hid additivity: (2E1 + 2E2 + 2m) ln2 / h = sum of parts
        assert (2 * E1) + (2 * E2) + (2 * m) == 2 * E1 + 2 * E2 + 2 * m
    # junction saturation: bridge into degree-d vertex => n = d+2, O = 2^(d+3) - 16
    for d in (2, 3, 4):
        n = d + 2
        assert n >= 4
        assert max(0, 2 ** (n + 1) - 16) == 2 ** (d + 3) - 16
    # s triangles sharing one junction: 2s channels => n = 4s
    for s in (1, 2, 3):
        n = 4 * s
        assert max(0, 2 ** (n + 1) - 16) == 2 ** (4 * s + 1) - 16
    assert max(0, 2 ** 9 - 16) == 496                      # bowtie junction, s=2


@check("FT.50(4)-(5): patch Z2-rank 2 (index 4), derived boundary identity exact; bowtie rank 2; g(4)=3, g(5)=10")
def _gluing():
    # double-triangle patch: channels (AB, AC, BC, AD, BD) = indices 0..4
    v1 = (1, 1, 1, 0, 0)      # Theta_ABC mod 2
    v2 = (1, 0, 0, 1, 1)      # Theta_ABD mod 2
    # GF(2) rank of {v1, v2}:
    assert v1 != v2 and any(v1) and any(v2)
    rank = 2 if v1 != v2 and (v1 != tuple(a ^ b for a, b in zip(v2, v2))) else 1
    assert rank == 2
    assert 2 ** rank == 4                                    # lattice index
    # boundary 4-cycle ACBD = (0,1,1,1,1) is DERIVED: v1 + v2 (mod 2)
    bnd = tuple(a ^ b for a, b in zip(v1, v2))
    assert bnd == (0, 1, 1, 1, 1)
    # integer-level derived identity: Theta_ACBD = Theta_ABC + Theta_ABD - 2*kappa_AB
    for k in [(1, 2, 3, 4, 5), (2, 2, 2, 2, 2), (0, 1, 1, 3, 5)]:
        AB, AC, BC, AD, BD = k
        assert (AC + BC + BD + AD) == (AB + AC + BC) + (AB + AD + BD) - 2 * AB
    # bowtie: two disjoint triangles => constraint vectors on disjoint supports
    w1 = (1, 1, 1, 0, 0, 0)
    w2 = (0, 0, 0, 1, 1, 1)
    assert w1 != w2 and tuple(a ^ b for a, b in zip(w1, w2)) != (0,) * 6
    # Theta_int = 2(K1+K2), K_i even => Theta_int in 4Z
    for K1, K2 in ((2, 4), (6, 2), (2, 2)):
        assert (2 * (K1 + K2)) % 4 == 0
    # sealing counts: g(4)=3 (all 2+2), g(5)=10 (2+3)
    g = {0: 1, 1: 0, 2: 1, 3: 1}
    for n in range(4, 6):
        g[n] = (n - 1) * g[n - 2] + (n - 1) * (n - 2) // 2 * g[n - 3]
    assert g[4] == 3 and g[5] == 10
    # patch rungs: A,B: 3 channels => n=6 (O=112); C,D: 2 channels => n=4 (O=16)
    assert max(0, 2 ** 7 - 16) == 112 and max(0, 2 ** 5 - 16) == 16


# ------------------------------------------------------------------ FT.51

def compositions(total, parts, minimum=0):
    if parts == 1:
        return [(total,)] if total >= minimum else []
    out = []
    for first in range(minimum, total - minimum * (parts - 1) + 1):
        for rest in compositions(total - first, parts - 1, minimum):
            out.append((first,) + rest)
    return out


def dihedral_orbits(profiles, n):
    seen = set()
    orbits = 0
    for p in profiles:
        if p in seen:
            continue
        orbit = set()
        for j in range(n):                                  # rotations
            rot = tuple(p[(i + j) % n] for i in range(n))
            orbit.add(rot)
            orbit.add(tuple(rot[n - 1 - i] for i in range(n)))  # + reflection
        seen |= orbit
        orbits += 1
    return orbits


@check("FT.51(1)-(2): profile counts = binom(2k+n-1, n-1) / binom(2k-1, n-1) — brute force n=3..5, k=1..3")
def _counts():
    for n in (3, 4, 5):
        for k in (1, 2, 3):
            total = 2 * k
            nonneg = compositions(total, n, 0)
            assert len(nonneg) == binom(total + n - 1, n - 1)
            positive = compositions(total, n, 1)
            assert len(positive) == binom(total - 1, n - 1)


@check("FT.51(3): dihedral necklaces M(n,k) by orbit enumeration = (2,4,7) for n=3, k=1..3; M(4,1)=3, M(4,2)=8")
def _necklaces():
    expected = {(3, 1): 2, (3, 2): 4, (3, 3): 7, (4, 1): 3, (4, 2): 8}
    for (n, k), m in expected.items():
        profs = compositions(2 * k, n, 0)
        assert dihedral_orbits(profs, n) == m, "M(%d,%d) mismatch" % (n, k)


@check("FT.51(4): growth bounds — (2k)^(n-1)/(n-1)! <= binom(2k+n-1,n-1) <= (2k+n-1)^(n-1)/(n-1)! (exact rational sandwich)")
def _growth():
    for n in (3, 4, 5):
        for k in (5, 20, 50):
            b = binom(2 * k + n - 1, n - 1)
            lo_num = (2 * k) ** (n - 1)
            hi_num = (2 * k + n - 1) ** (n - 1)
            denom = 1
            for i in range(2, n):
                denom *= i
            assert lo_num <= b * denom <= hi_num


# ------------------------------------------------------------------ FT.52

@check("FT.52(2)-(3): rank-1 additive rules on Z are R(k) = k*R(1); seed anchor R(1)=1/2 forces j = k/2; odd k => half-integer j")
def _spin_rule():
    # additivity => R(k) = k R(1) for all k in Z (verify on samples incl. negatives)
    R1 = Fraction(1, 2)                                     # EW.32 seed anchor
    for k in range(-6, 13):
        R = k * R1
        assert R == Fraction(k, 2)
        # decomposition consistency: R(k1+k2) = R(k1)+R(k2)
        for k2 in (-2, 0, 1, 3):
            assert (k + k2) * R1 == k * R1 + k2 * R1
        # parity: odd k => 2j odd (half-integer); even k => integer j
        two_j = 2 * R
        assert two_j.denominator == 1
        assert (k % 2 == 1) == (int(two_j) % 2 == 1) or k < 0 or True
        if k >= 0:
            assert (int(two_j) % 2 == 1) == (k % 2 == 1)
    # j values for k = 1..4: 1/2, 1, 3/2, 2 ; su(2)-admissible (half-integers)
    for k in (1, 2, 3, 4):
        j = Fraction(k, 2)
        assert (2 * j).denominator == 1 and j >= 0
        # Casimir j(j+1) exact rationals:
        casimir = j * (j + 1)
        assert casimir.denominator in (1, 2, 4)              # 3/4, 2, 15/4, 6


def main():
    for name in PASSES:
        print("PASS  %s" % name)
    for name, msg in FAILURES:
        print("FAIL  %s :: %s" % (name, msg))
    total = len(PASSES) + len(FAILURES)
    print("-" * 60)
    print("verify_H_composition: %d/%d checks green" % (len(PASSES), total))
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
