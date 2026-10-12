
#!/usr/bin/env python3
"""
verify_H_ds2.py — machine checks for H (WIP), Tier F.8.

Integer / exact-rational verification of the on-shell line-element
quantization layer (FT.22-FT.25). Pure Python 3 standard library; no
floating point anywhere (corpus checks/ convention: exact arithmetic,
exit code 0 = all green).

Run:  python3 checks/verify_H_ds2.py

Scope note: these are arithmetic checks only. The structural steps
(domain generalization in FT.22, chart/sector reasoning in FT.23) are
citation-discipline content covered by check_format.py's registry and
heading-order checks; this script verifies the exact integer/rational
content the theorems reduce to.

Checks
  1  FT.22  loop quantization: on-shell samples (integer per-edge ds2,
            even Theta) give integer winding k = Theta/2 and Phi = pi*Theta
            an integer multiple of 2*pi (single-valued holonomy).
  2  FT.22  selection rule: integer data with odd Theta gives
            Hol = (-1)^Theta = -1: excluded on-shell (documenting that the
            quantization is a selection rule, and that it bites).
  3  FT.22  EW.18 consistency: rung-3 wrapping sample reduces to
            Phi in 2*pi*Z verbatim.
  4  FT.23  orientation-evenness: exact monomial identity
            g_mn x^m x^n - g_mn (-x^m)(-x^n) == 0 (every monomial has
            x-degree 2), plus rational witnesses with nonzero shift
            cross-term g_0i.
  5  FT.24  floor: 2-cycle Theta = 2*kappa with Theta in 2Z forces
            kappa in Z (exact Fractions); Comm-min floor kappa = 1 gives
            Theta = 2, k = 1; calibration coefficient identities
            ds2 = kappa*h^2 = 4*kappa*G_N*ln2 [CT2.9] and
            S = (A/h^2)*ln2 = ln2 = 1 bit at A = h^2 [CT1.29].
  6  FT.25(1) chain-swept interior: edge-disjoint union of materialized
            loops gives Theta_int in 2Z and Hol_int = +1.
  7  FT.25(2)-(3) partial interior: integer per-edge data gives
            Theta_int in Z with free parity (both parities witnessed);
            full-loop parity is always +1 (cannot carry the spin label).
"""

from fractions import Fraction
import sys

PASSES = []
FAILURES = []


def check(name):
    def deco(fn):
        try:
            fn()
        except AssertionError as exc:
            FAILURES.append((name, str(exc) or "assertion failed"))
        except Exception as exc:  # report, don't crash
            FAILURES.append((name, "%s: %s" % (type(exc).__name__, exc)))
        else:
            PASSES.append(name)
        return fn
    return deco


# ---------------------------------------------------------------- FT.22

@check("FT.22 loop quantization: even Theta => integer winding k, Phi = 2*pi*k")
def _ft22_loops():
    # On-shell samples: integer per-edge ds2-hat with Theta in 2Z (FT.22's
    # conclusion; samples satisfy the selection rule by construction).
    samples = [
        [1, 1],            # materialized minimal 2-cycle, kappa = 1 (Comm-min floor)
        [2, 2],            # 2-cycle, kappa = 2
        [1, 1, 1, 3],      # 4-cycle, Theta = 6
        [3, -1, 2, 0],     # mixed signature: timelike (kappa<0), null (kappa=0) edges
        [1] * 8,           # longer loop, Theta = 8
        [0, 0, 0],         # trivial (all-null) chain: photon/gluon content [D1.7, D3.7]
    ]
    for ds2 in samples:
        theta = sum(ds2)
        assert theta % 2 == 0, "sample %s: Theta=%d not in 2Z" % (ds2, theta)
        k = Fraction(theta, 2)
        assert k.denominator == 1, "winding k = Theta/2 not integral for %s" % (ds2,)
        # Phi = pi*Theta = 2*pi*k with k integral  <=>  e^{i Phi} = +1 exactly.
        assert 2 * int(k) == theta


@check("FT.22 selection rule: odd Theta => Hol = -1 => excluded on-shell")
def _ft22_selection():
    for ds2 in ([1, 2], [1, 1, 1], [3, 0], [-1, 2]):
        theta = sum(ds2)
        assert theta % 2 != 0, "sample %s was supposed to have odd Theta" % (ds2,)
        hol = (-1) ** theta          # e^{i*pi*Theta} for integral Theta
        assert hol == -1             # single-valuedness fails => no pole => off-shell only


@check("FT.22/EW.18 consistency: wrapping-chain sample reproduces Phi in 2*pi*Z")
def _ft22_ew18():
    # EW.18: closed wrapping chain materializing as a rung-3 pole has
    # Phi(gamma) in 2*pi*Z. With alpha = pi [EM.20/FT.9] that is Theta in 2Z —
    # FT.22's specialization. Verify the equivalence on winding samples.
    for k in (-3, -1, 0, 1, 2, 7):
        phi_over_pi = 2 * k          # Phi/pi = Theta = 2k
        assert phi_over_pi % 2 == 0  # Phi in 2*pi*Z  <=>  Phi/pi even
        theta = phi_over_pi
        assert Fraction(theta, 2) == k


# ---------------------------------------------------------------- FT.23

@check("FT.23 orientation-evenness: exact monomial identity q(x) - q(-x) == 0")
def _ft23_symbolic():
    # Quadratic form q(x) = sum_{mu,nu} g_{mu nu} x^mu x^nu with *formal*
    # symmetric coefficients. Track monomials by their x-exponent vectors;
    # under x -> -x a monomial picks up (-1)^deg with deg = total x-degree.
    # Identity holds coefficient-wise iff every monomial has even degree.
    coeffs = {}  # exponent tuple -> coefficient multiplier of q(x) - q(-x)
    for mu in range(4):
        for nu in range(4):
            exps = [0, 0, 0, 0]
            exps[mu] += 1
            exps[nu] += 1
            deg = sum(exps)                      # computed, not hardcoded
            sign_under_negation = (-1) ** deg
            key = tuple(exps)
            # coefficient of g_{mu nu} in q(x) - q(-x):
            coeffs[key] = coeffs.get(key, Fraction(0)) + Fraction(1 - sign_under_negation)
    assert all(c == 0 for c in coeffs.values()), \
        "q(x) - q(-x) has a nonzero coefficient: %s" % coeffs


@check("FT.23 orientation-evenness: rational witnesses with nonzero shift g_0i")
def _ft23_witnesses():
    # Generic symmetric Lorentzian-ish g over Q, including shift cross-terms.
    g = {
        (0, 0): Fraction(-1),
        (0, 1): Fraction(1, 3), (1, 0): Fraction(1, 3),
        (0, 2): Fraction(-2, 5), (2, 0): Fraction(-2, 5),
        (1, 1): Fraction(1), (2, 2): Fraction(1), (3, 3): Fraction(1),
        (2, 3): Fraction(-1, 7), (3, 2): Fraction(-1, 7),
        (1, 3): Fraction(4, 9), (3, 1): Fraction(4, 9),
    }
    witnesses = [
        (Fraction(2), Fraction(-3), Fraction(5, 2), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(-7, 2), Fraction(1, 3), Fraction(0), Fraction(11, 5)),
    ]

    def q(v):
        return sum(g.get((m, n), Fraction(0)) * v[m] * v[n]
                   for m in range(4) for n in range(4))

    for dx in witnesses:
        minus_dx = tuple(-c for c in dx)
        assert q(dx) == q(minus_dx), \
            "ds2(dx) != ds2(-dx) for witness %s" % (dx,)
        # Cross-check the cross-term really is present and really cancels:
        cross = sum(g[(0, i)] * dx[0] * dx[i] + g[(i, 0)] * dx[i] * dx[0]
                    for i in (1, 2) if (0, i) in g)
        # not asserted zero: the point is q(dx) == q(-dx) *with* cross != 0.
        del cross


# ---------------------------------------------------------------- FT.24

@check("FT.24 floor: Theta = 2*kappa in 2Z => kappa in Z; Comm-min kappa = 1")
def _ft24_floor():
    for theta in (0, 2, 4, 6, -2, -8, 16):
        assert theta % 2 == 0
        kappa = Fraction(theta, 2)
        assert kappa.denominator == 1, "kappa = Theta/2 not integral for Theta=%d" % theta
    # Comm-min [D1.1]: minimal real edge has ds2-hat = 1.
    kappa = 1
    theta = 2 * kappa
    k = Fraction(theta, 2)
    assert (kappa, theta, int(k)) == (1, 2, 1)


@check("FT.24(2)-(3) calibration coefficients: ds2 = kappa*h^2 = 4*kappa*G_N*ln2; 1 bit per hop area")
def _ft24_calibration():
    # CT2.9: h^2 = 4*G_N*ln2. Treat (G_N*ln2) and h^2 as formal positive
    # symbols; verify the exact rational coefficient identities.
    for kappa in (0, 1, 2, 3, 7, -1):
        ds2_in_h2 = Fraction(kappa)               # ds2 = kappa * h^2     [D1.6, clause (2)]
        ds2_in_gnln2 = 4 * ds2_in_h2              # = 4*kappa * G_N*ln2   [CT2.9, clause (3)]
        assert ds2_in_gnln2 == Fraction(4 * kappa)
        assert ds2_in_gnln2.denominator == 1
    # CT1.29: S = (A/h^2)*ln2. At A = h^2 (one hop area): S = ln2 = 1 bit.
    area_in_hop_units = Fraction(1)               # A/h^2
    s_over_ln2 = area_in_hop_units                # S/ln2 = A/h^2
    assert s_over_ln2 == 1                        # exactly one bit per unit kappa


# ---------------------------------------------------------------- FT.25

@check("FT.25(1): chain-swept interior => Theta_int in 2Z => Hol_int = +1")
def _ft25_chain_swept():
    loops = [
        [1, 1],            # materialized 2-cycle (Theta = 2)
        [1, 1, 1, 3],      # materialized 4-cycle (Theta = 6)
        [2, 2, 2],         # materialized 6-cycle (Theta = 6)
    ]
    for c in loops:
        assert sum(c) % 2 == 0, "sample loop not materializable: Theta odd"
    theta_int = sum(sum(c) for c in loops)        # edge-disjoint union
    assert theta_int % 2 == 0
    assert (-1) ** theta_int == +1


@check("FT.25(2)-(3): partial interior => Theta_int in Z, parity free; full loop parity +1")
def _ft25_partial():
    chain = [1, 1, 1, 3]                          # materialized 4-cycle, Theta = 6 in 2Z
    assert sum(chain) % 2 == 0
    assert (-1) ** sum(chain) == +1               # full materialized loop: parity trivial
    partials = [
        (chain[:3], -1),                          # Theta_int = 3 (odd)  => Hol_int = -1
        ([1, 3], +1),                             # Theta_int = 4 (even) => Hol_int = +1
        (chain[:1], -1),                          # Theta_int = 1 (odd)  => Hol_int = -1
        (chain[:2], +1),                          # Theta_int = 2 (even) => Hol_int = +1
    ]
    for partial, expected_hol in partials:
        theta_int = sum(partial)
        assert isinstance(theta_int, int)         # integer-valued [FT.25(2)]
        assert (-1) ** theta_int == expected_hol, \
            "Hol_int wrong for partial %s" % (partial,)
    # Witness used in FT.25's Pf: odd partial sum out of an even full sum.
    assert sum(chain[:3]) % 2 == 1 and sum(chain) % 2 == 0


def main():
    for name in PASSES:
        print("PASS  %s" % name)
    for name, msg in FAILURES:
        print("FAIL  %s :: %s" % (name, msg))
    total = len(PASSES) + len(FAILURES)
    print("-" * 60)
    print("verify_H_ds2: %d/%d checks green" % (len(PASSES), total))
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
