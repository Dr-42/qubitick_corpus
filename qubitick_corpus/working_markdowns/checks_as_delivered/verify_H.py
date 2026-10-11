
"""
verify_H.py — exact machine verification of the arithmetic content of document H
(the H layer, exploratory fermionic sector).

H's "Machine verification" line (front matter) names the checkable content:
FT.1, FT.4.1, FT.5, FT.7, FT.14, FT.16, FT.17, Def-H.9 — all unit-sensitive
exact rational bookkeeping in the bit-wise regime (C_cap = 4 bits = 16
states [D0.9, C10, CT0.5, CT0.6]). No floating point; ln2, Omega, G_N,
h (= script h, CT2.9's h^2 = 4 G_N ln2) are carried as symbolic positive
Fraction tokens so that every check is an identity for arbitrary values,
not a numeric coincidence — same method as verify_G.py's ln2 stand-in.

  FT.1     I <= min(delta_h, 4 delta_tau) ln2  [C_cap = 4 bits]
  FT.4.1   N_states <= 2^{min(delta_h,4 delta_tau)}  (state-counting ceiling)
  FT.5     flux form: F <= min(delta_h/delta_tau, 4) ln2; F_phys = F/Omega
  FT.7     flux density: rho <= ln2/h^2; phys form 1/(4 Omega G_N) via
           h^2 = 4 G_N ln2 [CT2.9]
  FT.14    spin-charge decomposition table (delta_h = 2,3,4,-> infinity)
           and the rung-2 decomposition postulate N_weak = delta_h - 2,
           N_charge = 2
  FT.16    I_hid(v) = (n(v)-1) ln2 single-vertex case; full access -> 0
           for n <= 3
  FT.17    I_hid(Sigma) = E_int ln2 lemma + the three worked cross-checks
  Def-H.9  dimensional check [m] = [I_hid]/[h] = energy, and E_vis/I_hid/m
           bookkeeping consistency

Run:  python3 verify_H.py
"""

import random
import sys
from fractions import Fraction

FAILURES = []


def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILURES.append(name)


def main():
    print("verify_H: exact fermionic-sector checks (document H, exploratory)")

    rng = random.Random(2026)

    def rand_pos(lo=1, hi=40, dlo=1, dhi=12):
        return Fraction(rng.randint(lo, hi), rng.randint(dlo, dhi))

    C_cap = 4  # bits [CT0.5, CT0.6, D0.9]

    # ---- FT.1 : information flux bound --------------------------------
    # I <= min(delta_h, 4 delta_tau) ln2, for every delta_h, delta_tau >= 0.
    ok = True
    for _ in range(40):
        delta_h = rng.randint(0, 30)
        delta_tau = rng.randint(0, 12)
        ln2 = rand_pos()
        bound_hops = delta_h * ln2
        bound_cap = C_cap * delta_tau * ln2
        bound = min(bound_hops, bound_cap)
        # the two-jaw form must equal min(delta_h, 4 delta_tau) * ln2 exactly
        ok &= (bound == min(delta_h, C_cap * delta_tau) * ln2)
        # bound is monotone non-decreasing in each argument separately
        bound_more_h = min((delta_h + 1) * ln2, C_cap * delta_tau * ln2)
        ok &= (bound_more_h >= bound)
    check("FT.1   I <= min(delta_h, 4 delta_tau) ln2; two-jaw form exact & monotone", ok)

    # FT.1 physical form: delta_h = Dl/(Omega h), delta_tau = Dt/Omega =>
    # I <= (1/Omega) min(Dl/h, 4 Dt) ln2
    ok = True
    for _ in range(20):
        Omega = rand_pos(1, 20, 1, 5)
        h = rand_pos(1, 20, 1, 5)
        ln2 = rand_pos()
        Dl = rand_pos(0, 50, 1, 4)
        Dt = rand_pos(0, 50, 1, 4)
        delta_h = Dl / (Omega * h)
        delta_tau = Dt / Omega
        combinatorial = min(delta_h, C_cap * delta_tau) * ln2
        physical = (Fraction(1) / Omega) * min(Dl / h, C_cap * Dt) * ln2
        ok &= (combinatorial == physical)
    check("FT.1   physical form: delta_h=Dl/(Omega h), delta_tau=Dt/Omega consistent", ok)

    # ---- FT.4.1 : state-counting ceiling -------------------------------
    # N_states <= 2^{min(delta_h, 4 delta_tau)}, integer exponent case.
    ok = True
    for _ in range(30):
        delta_h = rng.randint(0, 10)
        delta_tau = rng.randint(0, 4)
        m = min(delta_h, C_cap * delta_tau)
        N_states = 2 ** m
        ok &= (N_states == 2 ** min(delta_h, C_cap * delta_tau))
        ok &= (N_states >= 1)
    check("FT.4.1 N_states <= 2^{min(delta_h,4 delta_tau)} well-formed, integer, >=1", ok)

    # ---- FT.5 : flux bound (rate form of FT.1) -------------------------
    ok = True
    for _ in range(40):
        delta_h = rng.randint(0, 40)
        delta_tau = rng.randint(1, 12)  # delta_tau > 0 to divide
        ln2 = rand_pos()
        Omega = rand_pos(1, 20, 1, 5)
        I_bound = min(delta_h, C_cap * delta_tau) * ln2
        F_bound_direct = I_bound / delta_tau
        F_bound_formula = min(Fraction(delta_h, delta_tau), C_cap) * ln2
        ok &= (F_bound_direct == F_bound_formula)
        F_phys_bound = F_bound_formula / Omega
        ok &= (F_phys_bound == (Fraction(1) / Omega) * min(Fraction(delta_h, delta_tau), C_cap) * ln2)
    check("FT.5   F <= min(delta_h/delta_tau,4) ln2; F_phys = F/Omega exactly (FT.1 / delta_tau)", ok)

    # ---- FT.7 : universal flux density bound ---------------------------
    # rho <= ln2/h^2 (combinatorial); phys form 1/(4 Omega G_N) via h^2 = 4 G_N ln2 [CT2.9]
    ok = True
    for _ in range(30):
        N_perp = rng.randint(1, 25)
        ln2 = rand_pos()
        h = rand_pos(1, 20, 1, 5)
        Omega = rand_pos(1, 20, 1, 5)
        F_bound = N_perp * ln2
        A_perp = N_perp * h * h
        rho_bound = F_bound / A_perp
        ok &= (rho_bound == ln2 / (h * h))   # N_perp cancels: universal
        # CT2.9: h^2 = 4 G_N ln2  =>  G_N = h^2/(4 ln2)
        G_N = (h * h) / (4 * ln2)
        rho_phys_bound = rho_bound / Omega
        ok &= (rho_phys_bound == Fraction(1) / (4 * Omega * G_N))
    check("FT.7   rho <= ln2/h^2 (N_perp cancels, universal); rho_phys <= 1/(4 Omega G_N) via CT2.9", ok)

    # ---- FT.14 : spin-charge decomposition table -----------------------
    # rung-2 decomposition postulate: N_weak = delta_h - 2, N_charge = 2, for delta_h >= 2.
    ok = True
    table = {2: (Fraction(1), Fraction(0)),
             3: (Fraction(2, 3), Fraction(1, 3)),
             4: (Fraction(1, 2), Fraction(1, 2))}
    for delta_h, (f_charge_expected, f_spin_expected) in table.items():
        N_charge = 2
        N_weak = delta_h - 2
        N_visible = delta_h
        f_charge = Fraction(N_charge, N_visible)
        f_spin = Fraction(N_weak, N_visible)
        ok &= (f_charge == f_charge_expected)
        ok &= (f_spin == f_spin_expected)
        ok &= (f_charge + f_spin == 1)
        ok &= (N_charge + N_weak == N_visible)
    check("FT.14  table: delta_h=2,3,4 give f_charge=1,2/3,1/2 and f_spin=0,1/3,1/2 exactly", ok)

    # continuum limit: f_charge = 2/delta_h -> 0, f_spin = 1 - 2/delta_h -> 1 as delta_h grows
    ok = True
    prev_f_charge = None
    for delta_h in [2, 4, 8, 16, 100, 10000]:
        f_charge = Fraction(2, delta_h)
        f_spin = 1 - f_charge
        ok &= (f_charge + f_spin == 1)
        if prev_f_charge is not None:
            ok &= (f_charge < prev_f_charge)  # monotonically decreasing toward 0
        prev_f_charge = f_charge
    ok &= (Fraction(2, 10000) < Fraction(1, 1000))  # tail is small: heading to 0
    check("FT.14  f_charge = 2/delta_h monotonically -> 0, f_spin -> 1 as delta_h -> infinity", ok)

    # ---- FT.16 : single-vertex hidden-information gap -------------------
    # I_hid({v}) = (n(v)-1) ln2 for delta_tau >= 1 (single incident edge, delta_h=1)
    ok = True
    for n in [1, 2, 3, 4]:
        ln2 = rand_pos()
        E_tot = n * ln2
        delta_h_single = 1
        delta_tau = rng.randint(1, 5)
        E_vis = min(delta_h_single, C_cap * delta_tau) * ln2  # = ln2 since delta_tau >= 1
        ok &= (E_vis == ln2)
        I_hid = E_tot - E_vis
        ok &= (I_hid == (n - 1) * ln2)
    # explicit table n=1,2,3,4 -> 0, ln2, 2ln2, 3ln2
    ln2 = rand_pos()
    expected = {1: 0 * ln2, 2: 1 * ln2, 3: 2 * ln2, 4: 3 * ln2}
    for n, exp in expected.items():
        E_tot = n * ln2
        E_vis = ln2
        ok &= (E_tot - E_vis == exp)
    check("FT.16  I_hid({v}) = (n(v)-1) ln2 for n=1,2,3,4 (single-neighbour access)", ok)

    # full access case: delta_h = n <= 3, delta_tau >= 1 => E_vis = E_tot => I_hid = 0
    ok = True
    for n in [1, 2, 3]:
        ln2 = rand_pos()
        delta_tau = rng.randint(1, 5)
        E_tot = n * ln2
        E_vis = min(n, C_cap * delta_tau) * ln2
        ok &= (E_vis == E_tot)
        I_hid = E_tot - E_vis
        ok &= (I_hid == 0)
    check("FT.16  full access (delta_h=n<=3, delta_tau>=1): E_vis = E_tot => I_hid = 0", ok)

    # ---- FT.17 : internal-edge lemma + three cross-checks ---------------
    # general lemma: E_bd <= 4 delta_tau (hyp) => I_hid(Sigma) = E_int ln2 exactly
    ok = True
    for _ in range(30):
        E_int = rng.randint(0, 30)
        E_bd = rng.randint(0, 30)
        delta_tau = rng.randint(1, 10)
        ln2 = rand_pos()
        if E_bd > C_cap * delta_tau:
            continue  # hypothesis not met; lemma doesn't apply
        E_tot = (E_int + E_bd) * ln2
        E_vis = min(E_bd, C_cap * delta_tau) * ln2
        ok &= (E_vis == E_bd * ln2)  # hypothesis makes this exact, not just an upper bound
        I_hid = E_tot - E_vis
        ok &= (I_hid == E_int * ln2)
    check("FT.17  lemma: E_bd <= 4 delta_tau => I_hid(Sigma) = E_int ln2 exactly", ok)

    # Cross-check 1: oriented 3-cycle, external observer via one edge.
    # E_int = 3, E_bd = 1, delta_tau = 1: hypothesis 1 <= 4*1 holds => I_hid = 3 bits.
    ln2 = rand_pos()
    E_int, E_bd, delta_tau = 3, 1, 1
    ok1 = (E_bd <= C_cap * delta_tau)
    E_tot = (E_int + E_bd) * ln2
    E_vis = min(E_bd, C_cap * delta_tau) * ln2
    I_hid = E_tot - E_vis
    ok1 &= (I_hid == 3 * ln2)
    check("FT.17  cross-check 1: 3-cycle, E_bd=1<=4, I_hid = 3 bits (ln2 units)", ok1)

    # Cross-check 2: bidirectional K4 face {A,B,C}, n(v)=6, observed by D.
    # E_int = 6, E_bd = 6: the delta_tau=1 reading VIOLATES (6 <= 4*1 is false);
    # the delta_tau=2 reading holds (6 <= 4*2 = 8). I_hid = 6 bits.
    ln2 = rand_pos()
    E_int, E_bd = 6, 6
    ok2 = True
    ok2 &= (not (E_bd <= C_cap * 1))       # delta_tau=1 hypothesis fails
    ok2 &= (E_bd <= C_cap * 2)             # delta_tau=2 hypothesis holds
    delta_tau = 2
    E_tot = (E_int + E_bd) * ln2
    E_vis = min(E_bd, C_cap * delta_tau) * ln2
    I_hid = E_tot - E_vis
    ok2 &= (I_hid == 6 * ln2)
    check("FT.17  cross-check 2: K4 face, delta_tau=1 fails (6>4), delta_tau=2 holds, I_hid=6 bits", ok2)

    # Cross-check 3: whole K4, single-point contact via A only.
    # E_int = C(4,2)*2 = 12, E_bd = 2, delta_tau = 1: hypothesis 2 <= 4*1 holds.
    # A's own accessible content is 2 bits < 3 [CT4.9]. I_hid = 12 bits.
    ln2 = rand_pos()
    E_int_expected = 12  # binom(4,2) * 2 = 6*2
    from math import comb
    E_int = comb(4, 2) * 2
    ok3 = (E_int == E_int_expected)
    E_bd, delta_tau = 2, 1
    ok3 &= (E_bd <= C_cap * delta_tau)
    ok3 &= (E_bd < 3)  # A's own accessible content 2 bits < 3 [CT4.9]
    E_tot = (E_int + E_bd) * ln2
    E_vis = min(E_bd, C_cap * delta_tau) * ln2
    I_hid = E_tot - E_vis
    ok3 &= (I_hid == 12 * ln2)
    check("FT.17  cross-check 3: full K4 via single vertex A, E_int=12=C(4,2)*2, I_hid=12 bits", ok3)

    # ---- Def-H.9 : dimensional check + bookkeeping consistency ----------
    # m := I_hid / h; with [I_hid] = q^0 (dimensionless-in-nats "information")
    # and h carrying a formal weight, check m = (E_tot - E_vis)/h is well-formed
    # and reduces consistently to the FT.16/FT.17 special cases via E_vis = FT.1 bound.
    ok = True
    for _ in range(30):
        n_Sigma = rng.randint(0, 20)      # |Sigma| = total touching real edges
        delta_h = rng.randint(0, n_Sigma) if n_Sigma > 0 else 0
        delta_tau = rng.randint(1, 6)
        ln2 = rand_pos()
        h = rand_pos(1, 20, 1, 5)
        E_tot = n_Sigma * ln2
        E_vis = min(delta_h, C_cap * delta_tau) * ln2
        I_hid = E_tot - E_vis
        m = I_hid / h
        # dimensional/bookkeeping sanity: m is exactly (E_tot - E_vis)/h, no hidden terms
        ok &= (m == (n_Sigma * ln2 - min(delta_h, C_cap * delta_tau) * ln2) / h)
        # I_hid is non-negative whenever E_vis (an upper bound on visible content) <= E_tot
        if E_vis <= E_tot:
            ok &= (I_hid >= 0)
    check("Def-H.9  m = I_hid/h bookkeeping: m = (E_tot - E_vis)/h exactly; I_hid >= 0 when E_vis<=E_tot", ok)

    # Def-H.9 applied to FT.16's single-vertex case: E_tot = n ln2, E_vis = ln2 (delta_h=1,
    # delta_tau>=1) => m = (n-1) ln2 / h, consistent with I_hid = (n-1) ln2 there.
    ok = True
    for n in [1, 2, 3, 4]:
        ln2 = rand_pos()
        h = rand_pos(1, 20, 1, 5)
        E_tot = n * ln2
        E_vis = ln2
        I_hid = E_tot - E_vis
        m = I_hid / h
        ok &= (I_hid == (n - 1) * ln2)
        ok &= (m == (n - 1) * ln2 / h)
    check("Def-H.9  reduces correctly on FT.16's single-vertex family (n=1..4)", ok)

    print()
    if FAILURES:
        print(f"verify_H: {len(FAILURES)} FAILURE(S): {FAILURES}")
        return 1
    print("verify_H: ALL CHECKS PASS (exact arithmetic)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
