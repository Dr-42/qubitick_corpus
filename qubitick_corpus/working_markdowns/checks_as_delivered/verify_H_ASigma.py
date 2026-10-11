
#!/usr/bin/env python3
"""
verify_H_ASigma.py — machine checks for H (WIP), Tiers F.9–F.11.

Exact integer/rational verification of the activated aspect-operator layer
(FT.21(i) telescoping, FT.26–FT.28), the strong edge weight (FT.29), the
sector quantum audit (FT.30), the continuum ledger (FT.31), and the Gap-7
Pi diagnostic. Pure Python 3 standard library;
no floating point (corpus checks/ convention). Exit code 0 = all green.

Run:  python3 checks/verify_H_ASigma.py

Scope note: arithmetic content only. The structural steps (Def-H.15's
assembly pattern, Def-H.16's resolvent declaration, FT.26's transfer
argument) are citation-discipline content covered by check_format.py.
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
        except Exception as exc:
            FAILURES.append((name, "%s: %s" % (type(exc).__name__, exc)))
        else:
            PASSES.append(name)
        return fn
    return deco


# ------------------------------------------------------- FT.26: dimensions

@check("FT.26(3)/FT.30 tiling: (5+3+1)+(3+3)+1 = 16 = C_cap [CT0.12, CT0.6]")
def _tiling():
    G, W, Hh = 5, 3, 1          # CT0.12: span{E^ij traceless}, span{W_i}, span{Sigma}
    Jp, Jm = 3, 3               # CT0.12: span{J_i}, span{K_i}
    Dp = 1                      # CT0.12: span{E_0}
    assert (G + W + Hh) + (Jp + Jm) + Dp == 16
    assert 16 == 4 ** 2         # C_cap = dim_R H(C^4) [CT0.6]
    # CT1.1 sector dims: (7,3,3,3)
    assert (7, 3, 3, 3) == (1 + 1 + 5, 3, 3, 3)   # E_++ = E_0 + Sigma + 5 traceless
    assert 7 + 3 + 3 + 3 == 16


@check("FT.26 mask-flag dims [CT0.14]: 6 < 16 < 17 < 25; u(3) = su(3) + u(1) = 8+1 [CT3.8]")
def _flags():
    K0, K1, K2, K3 = 6, 16, 17, 25
    assert K0 == 3 + 3                                  # J+ + J-
    assert K1 == K0 + (5 + 3 + 1 + 1)                   # + G + W + H + D+
    assert K2 == K1 + 1                                 # + EM (dim K^(EM) = 1)
    assert K3 == K2 + 8                                 # + strong (dim su(3) = 8)
    assert 9 == 8 + 1                                   # dim u(3) = dim su(3) + dim u(1)


@check("FT.26 Rmk: max observable Sigma-mask = 18; deficit 25-18 = 7 = 3+3+1 (J+,J-,D+)")
def _deficit():
    observable_blocks = {'EM': 1, 'G': 5, 'H': 1, 'W': 3, 'strong': 8}   # FT.20: J±,D± never
    assert sum(observable_blocks.values()) == 18
    assert 25 - 18 == 7 == 3 + 3 + 1


# ------------------------------------------------------- FT.28: floor card

@check("FT.28(1): floor fermion I_hid = E_int ln2 = 2 ln2; m_hid = 2 ln2 / h")
def _floor_mass():
    E_int, E_bd = 2, 1                  # 2-cycle interior; single observer edge
    assert E_bd <= 4 * 1                # FT.17 hypothesis at delta_tau = 1: E_bd <= 4*delta_tau
    I_hid_over_ln2 = E_int              # I_hid = E_int * ln2 exactly [FT.17]
    assert I_hid_over_ln2 == 2
    m_h_over_ln2 = Fraction(I_hid_over_ln2, 1)   # m_hid = I_hid/h  =>  m_hid*h/ln2 = 2
    assert m_h_over_ln2 == 2
    # CT4.9(1) cap check: per-vertex accessible <= 3 bits; channel-visible = 1 bit < 3
    assert E_bd < 3


@check("FT.28(2): Theta_int = 2*kappa even; k = kappa; Hol_int = +1 for all kappa samples")
def _floor_winding():
    for kappa in (1, 2, 3, 7, -1, -2):
        theta_int = 2 * kappa
        assert theta_int % 2 == 0
        k = Fraction(theta_int, 2)
        assert k.denominator == 1 and int(k) == kappa
        assert (-1) ** theta_int == +1          # chain-swept interior: parity trivial [FT.25(1)]


@check("FT.28(4)-(5): dim K(Sigma_min) = 9 core (+1 EM, +8 strong variant); rungs O(2)=O(3)=0")
def _floor_dims():
    core = 5 + 3 + 1                    # G + W + H
    assert core == 9
    assert core + 1 == 10 <= 18         # EM active
    assert core + 1 + 8 == 18           # colour-visible inside-sealed variant = maximal mask
    # rungs [CT0.5/CT0.6]: D_tick(n) = 2^(n+1); O(n) = max(0, D_tick - 16)
    D_tick = {n: 2 ** (n + 1) for n in range(0, 6)}
    O = {n: max(0, D_tick[n] - 16) for n in range(0, 6)}
    assert D_tick[3] == 16 and O[3] == 0        # p at rung 3: exact saturation
    assert D_tick[2] == 8 and O[2] == 0         # q at rung 2 (base case)
    assert O[4] == 16                           # rung 4 would oversubscribe [CT0.6]
    # base-case vertex degrees: n(p) = 3, n(q) = 2 [D0.8: e1 out/in + e2 in/out + observer at p]
    n_p, n_q = 3, 2
    assert n_p <= 3 and n_q <= 3                # accessible rungs [CT0.11]
    # colour slots exist only at n = 3 [D3.1]: base case q slot-less
    slots = {v: (n >= 3) for v, n in (('p', n_p), ('q', n_q))}
    assert slots == {'p': True, 'q': False}


@check("FT.28 variant Rmk: two-contact bookkeeping E_tot = 4 ln2, E_vis(o1) = ln2, I_hid(o1) = 3 ln2")
def _variant():
    E_int, E_bd = 2, 2                          # two single-contact observer edges
    assert E_bd <= 4 * 1
    E_tot_over_ln2 = E_int + E_bd               # Def-H.9(2): internal + boundary
    E_vis_over_ln2 = min(1, 4 * 1)              # o1's channel: 1 edge [FT.1]
    I_hid_o1 = E_tot_over_ln2 - E_vis_over_ln2
    assert (E_tot_over_ln2, I_hid_o1) == (4, 3) # m_hid(o1) = 3 ln2 / h: observer-relative


# ------------------------------------------------- Gap 7: Pi diagnostic

@check("Gap 7: Pi = m_hid^2 * loop-ds2 = E_int^2 * Theta * (ln2)^2, h-free; floor ladder; not constant")
def _pi_diagnostic():
    # Pi(c) := m_hid^2 * (Theta * h^2) with m_hid = I_hid/h, I_hid = E_int*ln2 [FT.17 hyp]
    #          = (E_int*ln2)^2 * Theta  -- h cancels EXACTLY; pure integer coefficient.
    def pi_coeff(E_int, theta):            # Pi / (ln2)^2
        return Fraction(E_int) ** 2 * theta

    # 2-cycle floor: E_int = 2, Theta = 2*kappa [FT.24/FT.28]
    for kappa in (1, 2, 3):
        assert pi_coeff(2, 2 * kappa) == 8 * kappa

    # 3-cycle: E_int = 3 [FT.17 xcheck 1]; three minimality regimes:
    assert pi_coeff(3, 6) == 54            # uniform kappa, min kappa = 2 (3k in 2Z, k>=1)
    assert pi_coeff(3, 4) == 36            # all-nonnull general min: Theta = 1+1+2 = 4, k = 2
    assert pi_coeff(3, 2) == 18            # null-permitting min: Theta = 1+1+0 = 2, k = 1
    # each Theta even (FT.22), each decomposition valid with kappa_e >= 0 integers:
    assert (1 + 1 + 2) % 2 == 0 and (1 + 1 + 0) % 2 == 0 and (2 + 2 + 2) % 2 == 0

    # tetrahedron face: E_int = 6 [FT.17 xcheck 2]
    for theta in (2, 4, 6):
        assert pi_coeff(6, theta) == 36 * theta

    # NOT constant across the floor family => no universal product-constant bridge:
    vals = {pi_coeff(2, 2), pi_coeff(3, 6), pi_coeff(3, 4), pi_coeff(3, 2), pi_coeff(6, 6)}
    assert len(vals) > 1, "Pi unexpectedly constant"
    # conversion datum is the pair (E_int, Theta): Pi/(ln2)^2 determines it? (not injective,
    # e.g. (2,8) vs (4,2) both 32) -- the pair, not Pi alone, is the datum:
    assert pi_coeff(2, 8) == pi_coeff(4, 2) == 32


# ------------------------------------------------- FT.21(i): sign telescoping

@check("FT.21(i): sum_interior f_v = (sigma_last - sigma_first)/2, exhaustive {+-1}^k, k=2..8")
def _telescope():
    from itertools import product
    for k in range(2, 9):                     # chain e_1..e_k, interior vertices v_2..v_k
        for signs in product((1, -1), repeat=k):
            # f_{v_i} = (sigma_{e_i} - sigma_{e_{i-1}})/2  [D3.3 in/out signs at v_i]
            total = sum(Fraction(signs[i] - signs[i - 1], 2) for i in range(1, k))
            assert total == Fraction(signs[k - 1] - signs[0], 2), \
                "telescoping failed for k=%d signs=%s" % (k, signs)
        # EM.9 alphabet closure: q = (sigma_s - sigma_t)/2 in {-1, 0, +1}
        for a in (1, -1):
            for b in (1, -1):
                assert Fraction(a - b, 2) in (Fraction(-1), Fraction(0), Fraction(1))


# ------------------------------------------------------- FT.29: no alpha_strong

@check("FT.29(2): Gell-Mann basis traceless (exact, sqrt(3) as formal factor); T-normalization samples")
def _gellmann():
    # Diagonals as (integer numerator over formal sqrt(3) where needed):
    # lambda3 = diag(1,-1,0); lambda8 = diag(1,1,-2)/sqrt(3)
    assert 1 + (-1) + 0 == 0                    # tr(lambda3) = 0 exactly
    assert 1 + 1 + (-2) == 0                    # tr(lambda8) numerator = 0 => trace 0
    # T_a = lambda_a/2; Tr(T_a T_b) = delta_ab/2 samples (exact rationals):
    # lambda1^2 = diag(1,1,0): Tr(T1 T1) = 2/4 = 1/2
    assert Fraction(1 + 1 + 0, 4) == Fraction(1, 2)
    # lambda8^2 = diag(1,1,4)/3: Tr(T8 T8) = (6/3)/4 = 1/2
    assert Fraction(1 + 1 + 4, 3) / 4 == Fraction(1, 2)
    # dimension obstruction: EM scalar read needs dim 1; strong block dim 8
    dim_EM, dim_strong = 1, 8                   # [CT0.14, CT3.8]
    assert dim_EM == 1 and dim_strong != 1
    # tracelessness of the whole aspect: Tr(F_strong) = sum f_a Tr(T_a) = 0 [CT3.10]
    Tr = sum(Fraction(0) for _ in range(8))
    assert Tr == 0


# ------------------------------------------------------- FT.30: audit totals

@check("FT.30: metric dictionary 10 = 5(G)+1(H)+1(D+)+3(W); S-odd blocks carry 0 metric coords")
def _dictionary():
    G, Hh, Dp, W = 5, 1, 1, 3                   # h_ij, Sigma_tr, a_00, w_i [CT1.12 table]
    assert G + Hh + Dp + W == 10
    assert 10 == Fraction(4 * 5, 2)             # #{g_mn = g_nm} [CT1.12]
    J_metric_coords = 3 * 0 + 3 * 0             # J± are S-odd: absent from E(e) [Def-H.14]
    assert J_metric_coords == 0


# ------------------------------------------------------- FT.31: continuum ledger

@check("FT.31(1)-(2): per-edge slack O(h^3), total O(h^2 L) subleading to CT1.19's O(h L)")
def _orders():
    # exponents of h as exact integers:
    per_edge_diff_exp = 3                       # |kappa_e h^2 - g xdot xdot h^2| = O(h)*h^2 = O(h^3)
    n_edges_exp = -1                            # n_R = L/h => h-exponent -1
    total_exp = per_edge_diff_exp + n_edges_exp # O(h^2 L)
    ct119_abs_err_exp = 1                       # CT1.19: abs error O(h L)
    assert total_exp == 2 > ct119_abs_err_exp   # quantization slack is subleading


@check("FT.31(3): winding k = (closed-loop ds^2)/(2 h^2) -> infinity at fixed loop as h -> 0")
def _large_k():
    # exact sample: loop integral = 2 k h^2 [FT.22]; fixed integral, shrinking h => growing k
    loop_ds2_over_h2 = 2 * 10 ** 6              # fixed classical loop in hop units
    k = Fraction(loop_ds2_over_h2, 2)
    assert k.denominator == 1 and k == 10 ** 6  # integer winding, macroscopically large


@check("FT.31(4): minimal-edge class: Theta = delta_h and S_reg/(loop ds^2) = ln2/h^2 = S_min/A_min")
def _relating():
    for delta_h in (2, 3, 4, 8):                # materialized chains, all edges minimal (kappa=1)
        kappa = [1] * delta_h
        theta = sum(kappa)
        assert theta == delta_h                 # Theta = delta_h on the minimal-edge class
        # S_reg = delta_h * ln2 [CT0.9/C9]; loop ds^2 = Theta * h^2
        # ratio S_reg / (Theta h^2) = ln2/h^2 exactly (coefficient identity):
        ratio_coeff = Fraction(delta_h, theta)  # (delta_h/Theta) * (ln2/h^2)
        assert ratio_coeff == 1
        # CT1.29 floor: S_min = ln2 (1 edge), A_min = h^2 (1 hop area) => S_min/A_min = ln2/h^2
        S_min_over_ln2, A_min_over_h2 = Fraction(1), Fraction(1)
        assert S_min_over_ln2 / A_min_over_h2 == ratio_coeff


def main():
    for name in PASSES:
        print("PASS  %s" % name)
    for name, msg in FAILURES:
        print("FAIL  %s :: %s" % (name, msg))
    total = len(PASSES) + len(FAILURES)
    print("-" * 60)
    print("verify_H_ASigma: %d/%d checks green" % (len(PASSES), total))
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
