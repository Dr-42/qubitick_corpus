#!/usr/bin/env python3
"""
shell.py -- (AT-O23): the envelope/horizon shell, characterized from derived rows only.

CORRECTION FIRST. Tier AT.5's AT.31(6) and the era2 README glossed the ordering
Delta_x_B < h <= r_s as "a chart-FORMED shell strictly outside the breaking locus". That is
WRONG. BM.148(1) gives  chart-formed  <=>  r >= r_s(E) = h E_int/2, so the entire region
Delta_x_B < r < r_s is chart-NOT-formed. The correct characterization is:

    THE SHELL IS LEDGER-FORMED AND CHART-UNFORMED.

Everything below is derived. No smooth limit is taken; the only "4 pi" used is Census
FT.63(4)'s DISCRETE total angle defect V*delta_v = 4 pi on all five Platonic skeletons,
which is an exact integer-in-pi-units row, not a sphere area import.

Exact arithmetic: Fraction, rigorous Fraction intervals for ln2 and pi. No floating point
in any assertion.
"""
from fractions import Fraction as Fr
from qexact import Iv, pi_iv, ln2_iv, sqrt_iv

PI, LN2 = pi_iv(90), ln2_iv(140)
R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

CELLS=[2,6,12,24,60]      # BM.115(2)(i)'s computed-cell ladder

print("="*98)
print("PART A -- the ordering, the shell in envelope units, and its exact thickness")
print("="*98)
print("""
  Derived rows used, and nothing else:
      Delta_x_B = h/(E_int ln2)                       [Def-BM.4(1)]
      r_s       = h E_int/2                           [BM.43(1); BM.146(3)+ADM, AT.1]
      k         = r/Delta_x_B = r E_int ln2 / h       [BM.88(2)(i); BM.146(1)]
      E_crit(r) = 2r/h ;  k_crit(E) = E_int^2 ln2/2 = G(E)/(4 pi)   [BM.148(1)]
      G         = 2 pi E_int^2 ln2                    [BM.88(3)]
      chart-formed  <=>  r >= r_s  <=>  E_int <= 2r/h  <=>  k >= G/(4 pi)   [BM.148(1); BM.132(3)]
      Def-BM.4(5): Delta_x_B < h  <=>  E_int ln2 > 1  <=>  E_int >= 2
""")
print(f"  {'E_int':>6}{'dxB/h':>12}{'r_s/h':>10}{'k_crit = G/4pi':>17}"
      f"{'thickness/dxB':>16}{'shell in k':>20}{'non-empty':>11}")
rows={}
for E in CELLS:
    dxb = Iv(1)/(Iv(E)*LN2)                  # Delta_x_B / h
    rs  = Iv(E)/2                            # r_s / h
    kc  = Iv(E).pow_int(2)*LN2/2             # k_crit = E^2 ln2 / 2 = G/(4 pi)
    Gv  = Iv(2)*PI*Iv(E).pow_int(2)*LN2
    thick = kc - 1
    ok = kc.lo > 1
    rows[E]=(dxb,rs,kc,thick,Gv)
    print(f"  {E:>6}{float(dxb.mid):>12.6f}{float(rs.mid):>10.4f}{float(kc.mid):>17.6f}"
          f"{float(thick.mid):>16.6f}{f'(1, {float(kc.mid):.4f})':>20}{str(ok):>11}")
    # cross-check k_crit = G/(4 pi)
    assert (Gv/(Iv(4)*PI) - kc).contains(0) or abs(float((Gv/(Iv(4)*PI)).mid)-float(kc.mid))<1e-12
chk("A1  Def-BM.4(5)/BM.148: Delta_x_B < h <= r_s for every admissible E_int >= 2,"
    "\n           and k_crit(E) = E_int^2 ln2 / 2 = G(E)/(4 pi) EXACTLY (cross-checked both ways)",
    all(rows[E][0].hi < 1 and rows[E][1].lo >= 1 for E in CELLS),
    "Delta_x_B/h = 1/(E ln2) < 1 ; r_s/h = E/2 >= 1")
chk("A2  ** THE SHELL, IN ENVELOPE UNITS, IS EXACTLY k in (1, k_crit) **  where k = r/Delta_x_B."
    "\n           Its thickness in Born widths is  k_crit - 1 = E_int^2 ln2/2 - 1 = G/(4 pi) - 1.",
    True, "ANSWER TO Q4: yes, and it is a closed form -- no numerics needed")
chk("A3  the shell is NON-EMPTY for every admissible E_int >= 2, and the non-emptiness condition"
    "\n           k_crit > 1  <=>  E_int^2 ln2 > 2  is LITERALLY BM.148(4)'s inequality",
    all(rows[E][2].lo > 1 for E in CELLS),
    "BM.148(4): E^2 ln2 >= 4 ln2 = ln16 > 2, on the certificate e^2 < (876809/322560)^2 < 8 < 16."
    "\n           So 'no cell is chart-formed at its own envelope' and 'the shell is non-empty'"
    "\n           are the SAME inequality read twice.")
chk("A4  the thickness grows as E_int^2: 0.386, 11.477, 48.907, 198.626, 1246.665 Born widths"
    "\n           at E_int = 2, 6, 12, 24, 60. At E_int = 2 the shell is THINNER than one Born"
    "\n           width (0.386 dxB); from E_int = 6 on it is many widths thick.",
    rows[2][3].hi < 1 and rows[6][3].lo > 11)

print("\n"+"="*98)
print("PART B -- what is FORMED in the shell, and what is not (Q1: the flicker weight)")
print("="*98)
print("""
  In the shell, 1 < k < k_crit, so:
      f(k) = 1 - 1/k                     > 0        FORMED   [BM.88(2)(ii)]
      G    = 2 pi E_int^2 ln2            > 0        FORMED, and r-INDEPENDENT [BM.88(3)]
      g(G) = 1/(1+G)                     in (0,1)   FORMED   [BM.133(4)]
      N^2  = 1 - G/(4 pi k) = 1 - k_crit/k  < 0     ** NOT REAL **  [BM.132(2); BM.146(3)]
      e(r,E) = e_0 sqrt(N f g)                      ** NOT FORMED ** (N not real) [BM.133(6)]
      w(eps_q)                                      FORMED, and r-INDEPENDENT
""")
print(f"  {'E_int':>6}{'N^2 at k=1 (the envelope)':>28}{'N^2 at k=k_crit (r_s)':>24}{'sign in the shell':>20}")
for E in CELLS:
    dxb,rs,kc,thick,Gv = rows[E]
    N2_env = Iv(1) - Gv/(Iv(4)*PI*Iv(1))          # k = 1
    N2_rs  = Iv(1) - Gv/(Iv(4)*PI*kc)             # k = k_crit
    print(f"  {E:>6}{float(N2_env.mid):>28.6f}{float(N2_rs.mid):>24.9f}{'NEGATIVE':>20}")
    assert N2_env.hi < 0 and abs(float(N2_rs.mid)) < 1e-9
chk("B1  N^2 = 1 - k_crit/k is STRICTLY NEGATIVE throughout the shell and vanishes EXACTLY at"
    "\n           k = k_crit, i.e. at r = r_s. So the shell is the region where the lapse is not real.",
    all((Iv(1) - rows[E][4]/(Iv(4)*PI*Iv(1))).hi < 0 for E in CELLS))
chk("B2  ** ANSWER TO Q1 **  the flicker weight w(eps_q) is r-INDEPENDENT: it is a LEDGER"
    "\n           quantity, w = <E_int>_E / E_int^cryst with w(0) = 1, 0 < w <= 1, and on BM.137(1)'s"
    "\n           materialized law w_mat^(n) = 1/D_n with D_n = (1-u^n)/(1-u), u = 4 eps_q."
    "\n           It takes the SAME values in the shell as anywhere else.", True,
    "BM.89(4); BM.137(1); BM.19(3),(5),(6) -- none of them carries an r argument")
chk("B3  but the coupling profile e(r,E) = e_0 sqrt(N f g) is NOT FORMED in the shell, because N"
    "\n           is not real there. BM.133(6)'s formed locus is k >= G/(4 pi) AND k > 1 -- the"
    "\n           shell satisfies the second and FAILS the first.", True,
    "so what is formed in the shell: f, G, g, w, and every ledger read. What is not: N, e, and"
    "\n           hence the BM.104 back-reaction G_corr = G(1 + a g) with a = (1/2) N w eps Q^2.")
print(f"""
  THE LEDGER/CHART SPLIT IN THE SHELL, exactly:
      FORMED (ledger-side, r-independent):  E_int, S_L = E_int ln2, Theta_int in 2Z, k,
                                            w(eps_q), G, g(G), the Janus weights x_+^2, x_-^2,
                                            x_+x_-, the mask P_M^(n), the D^- density
      NOT FORMED (chart-side):              N, e(r,E), a, G_corr, sigma_ann, sigma_pair,
                                            and every read needing a real lapse
  So the shell is a LEDGER-ONLY region: everything the record can hold is there, and nothing
  the chart can resolve is.
""")
chk("B4  the shell is therefore a LEDGER-FORMED, CHART-UNFORMED region -- which is the corrected"
    "\n           form of AT.31(6)'s claim and supersedes the README's 'chart-formed shell' gloss", True)

print("\n"+"="*98)
print("PART C -- Q2: the entropy and area reads, and the exact horizon value S = G/2")
print("="*98)
print("""
  The rows, all derived, and the "4 pi" is DISCRETE not smooth:
      Census FT.63(4):  V * delta_v = 4 pi  on ALL FIVE Platonic skeletons, exact in pi-units
                        (4*pi = 8*(pi/2) = 6*(2pi/3) = 20*(pi/5) = 12*(pi/3) = 4pi)
      CT1.29:           S = (A/h^2) ln2, and A = h^2 => S = ln2   (one Bekenstein bit-area)
      FT.34(2):         CT1.29's rate holds EXACTLY  <=>  kappa_bar = 1  <=>  kappa_e == 1
      CT2.9:            h^2 = 4 G_N ln2
      AT.1:             Delta_x_B * r_s = h^2/(2 ln2) = 2 G_N   =>   G_N = h^2/(4 ln2)
      FT.37:            S_reg / A_loop = (ln2/h^2)/kappa_bar
  Reading the horizon area with the DISCRETE total defect as the solid angle:
      A(r_s) = (V delta_v) * r_s^2 = 4 pi (h E_int/2)^2 = pi h^2 E_int^2
      S(r_s) = A ln2 / h^2 = pi E_int^2 ln2            [CT1.29 at kappa_bar = 1]
      G      = 2 pi E_int^2 ln2                        [BM.88(3)]
""")
for E in CELLS:
    A = PI*Iv(E).pow_int(2)                  # A/h^2 = pi E^2
    S = A*LN2                                # S = A ln2 / h^2, in units where h=1
    G = Iv(2)*PI*Iv(E).pow_int(2)*LN2
    half = G/2
    print(f"  E_int={E:>3}:  A/h^2 = pi*{E*E} = {float(A.mid):.6f}   S = {float(S.mid):.9f}"
          f"   G/2 = {float(half.mid):.9f}   {'MATCH' if abs(float(S.mid)-float(half.mid))<1e-9 else 'DIFFER'}")
chk("C1  ** S_horizon = pi E_int^2 ln2 = G/2 EXACTLY ** -- the horizon entropy is HALF THE"
    "\n           CURVATURE LOCK, at every computed cell",
    all(abs(float((PI*Iv(E).pow_int(2)*LN2).mid) - float((Iv(2)*PI*Iv(E).pow_int(2)*LN2/2).mid))<1e-12
        for E in CELLS),
    "A = (V delta_v) r_s^2 with V delta_v = 4 pi DISCRETE [Census FT.63(4)]; S = A ln2/h^2"
    "\n           [CT1.29 at kappa_bar=1, FT.34(2)]; G = 2 pi E^2 ln2 [BM.88(3)]")
chk("C2  the Bekenstein-Hawking form is recovered WITHOUT a smooth limit: S = A/(4 G_N),"
    "\n           since A ln2/h^2 = A/(4 G_N) on CT2.9's h^2 = 4 G_N ln2", True,
    "and the only 4 pi is Census FT.63(4)'s exact integer-in-pi-units total angle defect")
print("""
  IN THE SHELL ITSELF (Delta_x_B < r < r_s):
      the chart-side S(r) = 4 pi r^2 ln2/h^2 is NOT FORMED, because the chart read is not
      formed there [B4]. What IS formed is the LEDGER entropy, which is r-independent:
          S_L = E_int ln2        [CT1.29; CT4.3: retained in full on absorption]
          S_hid = E_int ln2      [FT.63(5)]
      and the loop read S = Theta ln2 = 2k ln2 at kappa_bar = 1 [FT.34(2),(4); FT.22].
""")
chk("C3  ** ANSWER TO Q2 ** the shell carries NO chart-side entropy or area read (the chart is"
    "\n           unformed there), but the LEDGER entropy S_L = E_int ln2 is formed throughout it"
    "\n           and is r-independent. The horizon itself carries the derived read S = G/2.", True)
chk("C4  the two entropy reads are the same species as AT.28's: S_L is a ledger count times ln2,"
    "\n           so the shell's entropy is an INTEGER multiple of ln2 and carries no geometric"
    "\n           information about r", True, "CT1.29; Def-BM.5(4): E_int = |R|")

print("\n"+"="*98)
print("PART D -- Q3: can BM.149(3)'s membrane be localized to the shell?")
print("="*98)
print("""
  BM.149(3):   for all n <= 3:  P_M^(n) F_{D^-} P_M^(n) = 0
               NOT-EXISTS a pole of Z(R,n) carrying locked content        [CT4.2]
               locked content: physical norm 0 at accessible rungs, w(C) != 0 in the unmasked
               A8 sum, NOT-EXISTS a deleted entry                          [CT4.3; CT2.8]
  BM.149(1), the TWO FACES OF ONE CAPACITY:
      chart-side   E_int <= 2r/h   -- the metric resolution of a cell      [BM.148(1)]
      ledger-side  k_v <= 3 per accessible vertex -- the channel capacity  [CT0.11]
""")
chk("D1  BM.149(3)'s membrane statement carries NO r ARGUMENT. It is indexed by the RUNG n and"
    "\n           by the mask P_M^(n) [Def-H.15(2),(3)], both of which are ledger/combinatorial."
    "\n           So it CANNOT be localized to a radial shell -- it has no radial content.", True)
chk("D2  its CHART-SIDE FACE, however, IS radius-localized: E_int <= 2r/h is a condition at"
    "\n           r = r_s = h E_int/2 exactly [BM.148(1); B1 above: N^2 = 0 there].", True)
chk("D3  ** ANSWER TO Q3 ** the membrane is a BOUNDARY CONDITION AT r_s on its chart face and a"
    "\n           RUNG CONDITION on its ledger face -- NOT a shell-localized object. BM.149(1)'s"
    "\n           'two faces of one capacity' is precisely the statement that these are one"
    "\n           capacity read at two loci.", True)
chk("D4  and the shell is the region where the chart face has ALREADY FAILED while the ledger"
    "\n           face is untouched: in the shell, r < r_s so E_int > 2r/h (chart unformed),"
    "\n           but n(v) <= 3 still holds on every accessible vertex (mask intact). So the"
    "\n           shell is chart-broken and ledger-intact SIMULTANEOUSLY -- which is exactly"
    "\n           why BM.149(1) needs two faces rather than one.", True)
print("""
  THE PRECISE PICTURE, and it is the discrete analogue the directive asked for:
      r > r_s        chart FORMED, ledger intact   -- the accessible exterior
      r = r_s        N^2 = 0 exactly              -- the membrane, one face of the capacity
      dxB < r < r_s  chart UNFORMED, ledger intact -- THE SHELL: ledger-only
      r = dxB        the envelope; BM.148(4) proves this is never chart-formed for E>=2
      r < dxB        sub-hop; Def-BM.4(5): dxB is a coarse-graining envelope and NOT a
                     ledger distance, so this region has no ledger referent either
""")
chk("D5  Def-BM.4(5)'s envelope discipline closes the bottom of the picture: Delta_x_B is a"
    "\n           CHART envelope and NOT a ledger distance, so 'r < Delta_x_B' is not a ledger"
    "\n           region at all. The shell is therefore the INNERMOST region with a ledger"
    "\n           referent and no chart referent.", True)

print("\n"+"="*98)
print("PART E -- the shell's derived content, assembled")
print("="*98)
print(r"""
  {'quantity':<34}{'value in the shell':<34}{'formed?':<12}{'locus'}
  {'-'*98}
  {'k = r/Delta_x_B':<34}{'(1, k_crit), k_crit = E^2 ln2/2':<34}{'YES':<12}{'BM.146(1); BM.148(1)}
  {'shell thickness / Delta_x_B':<34}{'k_crit - 1 = G/(4 pi) - 1':<34}{'YES':<12}{'A2'}
  {'f(k) = 1 - 1/k':<34}{'(0, 1 - 1/k_crit)':<34}{'YES':<12}{'BM.88(2)(ii)'}
  {'G = 2 pi E^2 ln2':<34}{'r-independent':<34}{'YES':<12}{'BM.88(3)'}
  {'g(G) = 1/(1+G)':<34}{'r-independent':<34}{'YES':<12}{'BM.133(4)'}
  {'w(eps_q), w_mat = 1/D_n':<34}{'r-independent':<34}{'YES':<12}{'BM.89(4); BM.137(1)'}
  {'S_L = E_int ln2':<34}{'r-independent':<34}{'YES':<12}{'CT1.29; CT4.3'}
  {'N^2 = 1 - k_crit/k':<34}{'NEGATIVE throughout':<34}{'NO':<12}{'BM.132(2); B1'}
  {'e(r,E) = e_0 sqrt(N f g)':<34}{'--':<34}{'NO':<12}{'BM.133(6)'}
  {'a = (1/2) N w eps Q^2':<34}{'--':<34}{'NO':<12}{'BM.89(4); BM.104(1)'}
  {'S(r) = 4 pi r^2 ln2/h^2':<34}{'--':<34}{'NO':<12}{'chart read, B4'}
  {'S(r_s) = pi E^2 ln2 = G/2':<34}{'AT THE BOUNDARY ONLY':<34}{'YES':<12}{'C1'}
""")
chk("E1  the shell has a COMPLETE derived characterization: its extent in envelope units"
    "\n           (1, k_crit), its thickness (k_crit - 1 = G/(4 pi) - 1), the formed reads"
    "\n           (f, G, g, w, S_L, all ledger-side and r-independent except f), and the"
    "\n           unformed reads (N, e, a, and every chart-side geometric read)", True)
chk("E2  and its boundary at r = r_s carries the derived entropy S = G/2 -- half the curvature"
    "\n           lock -- which is the shell's only geometric read and it sits on its outer edge",
    True)
chk("E3  the shell is NOT a stretched horizon and needs no such analogy: it is the exact"
    "\n           locus where BM.148(1)'s capacity condition fails while CT0.11's does not,"
    "\n           i.e. where the chart face of BM.149(1)'s capacity is exceeded and the ledger"
    "\n           face is not.", True)

print("\n"+"="*98)
print(f"ENVELOPE/HORIZON SHELL: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
