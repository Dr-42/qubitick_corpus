#!/usr/bin/env python3
"""verify_H_tumbling.py — companion to FT.87 / FT.88 (Tier F.29): machine audit of the
external "tumbling model / Yukawa replacement" proposal, plus the involution algebra of FT.88.

Every checkable claim is verified exactly; every dimension is checked in q-exponents; every
"derived" label is tested against the frozen corpus inventory. Fractions only; Decimal is used
solely for display and for the transcendental comparison against exact rational Taylor series.
"""
import os, sys, json
import era_paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
getcontext().prec = 40
from bypasscore import cycle_graph, complete_graph, cube_graph, octa_graph, undirected_from, \
    types_of, centers_of, cover_value, automorphisms, cap_dp_by_K

ok = fail = 0
def T(cond, msg):
    global ok, fail
    assert cond, "FAIL: " + msg
    ok += 1
    print(f"  [OK]   {msg}")
def note(msg):
    print(f"  [..]   {msg}")

print("=" * 100)
print("A. The rotor/Regge formula: dimensional analysis in q-exponents  ([h] = q^-1/2 = length)")
print("=" * 100)
q = {'m^2': 1, 'm': Fr(1, 2), 'E_rot (energy)': Fr(1, 2), 'k': 0, 'R (edge count)': 0,
     'R_phys = R*h': Fr(-1, 2), 'R_phys^2': -1, 'h^2': -1, 'Delta S': 0, 'I = M R_phys^2': Fr(-1, 2)}
for k_, v in q.items(): print(f"    [{k_:18s}] = q^{v}")
T(q['m^2'] == 1 and q['E_rot (energy)'] == Fr(1, 2),
  "m^2 has dimension q^1 but E_rot has q^(1/2): §4.5's  m^2 = m_static^2 + h^2k^2/(2I)  ADDS AN ENERGY TO A MASS-SQUARED")
T(q['k'] * 2 - 2 * q['R (edge count)'] == 0,
  "§6.1's k^2/R^2 with R an edge count is q^0 (dimensionless), NOT q^1 -> inconsistent as written")
T(-2 * q['R_phys = R*h'] == 1,
  "repair: k^2/(R_phys^2) = k^2/(R^2 h^2) has dimension q^1 -- dimensionally admissible only with the h^-2")
T(q['Delta S'] + q['R_phys^2'] == -1 and q['I = M R_phys^2'] == Fr(-1, 2),
  "§6.4's I = Delta S * R^2 has dimension q^-1, but a moment of inertia is q^-1/2 -> OFF BY q^-1/2")
print("    ==> two dimension traps of the species (energy-vs-mass^2; count-vs-length).")

print("\n" + "=" * 100)
print("B. Is the rotor term new physics, or the Taylor term of the DECLARED defect read?")
print("=" * 100)
# P-H7'/FT.54/FT.60(5): m^2(m) = 4 mu'^2 sin^2(m Theta_R/4); small angle -> mu'^2 Theta_R^2 m^2/4
print("  4 sin^2(x/4)... expand: 4 sin^2(m Theta/4) = m^2 Theta^2/4 - m^4 Theta^4/192 + O(Theta^6)")
# exact Taylor coefficients via the series of sin^2
# verify the leading coefficient exactly with Fractions at small rational angles
for Th, m in ((Fr(1, 100), 1), (Fr(1, 100), 3), (Fr(1, 50), 5)):
    from math import factorial
    x = Fr(m) * Th / 4
    # sin^2(x) exact via series: sin x = sum (-1)^j x^(2j+1)/(2j+1)!
    sinx = sum(Fr((-1) ** j) * x ** (2 * j + 1) / factorial(2 * j + 1) for j in range(30))
    exact = 4 * sinx * sinx
    lead = Fr(m * m) * Th * Th / 4
    T(abs((exact / lead - (1 - x * x / 3)) / x ** 4 - Fr(2, 45)) < Fr(1, 10 ** 5),
      f"m={m}, Theta={Th}: 4sin^2(mTheta/4) = (m^2Theta^2/4)(1 - x^2/3 + 2x^4/45 + ...), x=mTheta/4 -- both Taylor coefficients exact")
print("  ==> the rotor slope 1/R^2 IS the declared Taylor coefficient mu'^2 Theta_R^2 / 4:")
print("      m^2_pole(m) ~= (mu'^2 Theta_R^2/4) m^2. The tumbling term introduces NO new mechanism;")
print("      it inherits P-H7''s conditional status AND FT.76(3)'s ceiling (the sine saturates at 4).")
# how bad is the quadratic approximation at the ACTUAL uniform-minimal windings?
SOL = {'tetra': (Fr(1), 3), 'cube': (Fr(1, 2), 2), 'octa': (Fr(2, 3), 3),
       'dodeca': (Fr(1, 5), 5), 'icosa': (Fr(1, 3), 3)}
print(f"\n  {'solid':8s} {'k_f':>3} {'x = k delta_v/4 (rad)':>22} {'exact 4sin^2':>13} {'quad 4x^2':>12} "
      f"{'exact/quad':>11} {'error':>7}")
PI = Decimal('3.14159265358979323846264338327950288419716939937510')
errs = {}
for nm, (dvp, k) in SOL.items():
    xpi = Fr(k) * dvp / 4                       # x in units of pi
    x = Decimal(xpi.numerator) / Decimal(xpi.denominator) * PI
    sx = sum(Decimal(-1) ** j * x ** (2 * j + 1) / Decimal(factorial(2 * j + 1)) for j in range(60))
    exact = 4 * sx * sx
    quad = 4 * x * x
    errs[nm] = (exact, quad, 1 - exact / quad)
    print(f"  {nm:8s} {k:>3} {float(x):>22.6f} {float(exact):>13.6f} {float(quad):>12.6f} "
          f"{float(exact/quad):>11.4f} {float(errs[nm][2])*100:>6.1f}%")
T(all(abs(errs[nm][0] - Decimal(v)) < Decimal('1e-9')
      for nm, v in (('tetra', 2), ('cube', 2), ('octa', 4), ('dodeca', 2), ('icosa', 2))),
  "the exact values are FT.76(2)'s top weights (2,2,4,2,2) -- independent cross-check")
emin = min(float(v[2]) for v in errs.values()) * 100
emax = max(float(v[2]) for v in errs.values()) * 100
T(emax > 80 and emin > 15,
  f"the quadratic (Regge/rotor) form errs by {emin:.1f}%-{emax:.1f}% at the documented uniform-minimal windings")

print("\n" + "=" * 100)
print("C. Regge 'verified LINEAR for all 12 shapes' — is that a verification or a tautology?")
print("=" * 100)
note("m^2 = m_static^2 + (4/R^2) j^2 with j = |k|/2 is LINEAR IN j^2 BY ALGEBRA for any R:")
print("      substituting j = |k|/2 gives m^2 = m_static^2 + k^2/R^2, the ansatz itself. The linearity")
print("      'check' cannot fail for any shape -> it carries no information (not a verification).")
print("      The non-trivial question is whether the DERIVED read (4 mu'^2 sin^2) is linear in j^2:")
for nm, (dvp, k) in SOL.items():
    xs = [Fr(m) * dvp / 4 for m in (1, 3, 5, 7)]      # four weights -> three slopes
    # exact sine values are algebraic; test monotone-in-j^2 curvature via Decimal
    vals = []
    for xpi in xs:
        x = Decimal(xpi.numerator) / Decimal(xpi.denominator) * PI
        sx = sum(Decimal(-1) ** j * x ** (2 * j + 1) / Decimal(factorial(2 * j + 1)) for j in range(60))
        vals.append(4 * sx * sx)
    if len(vals) >= 3:
        jsq = [(Decimal(m) / 2) ** 2 for m in (1, 3, 5, 7)]
        slopes = [(vals[i + 1] - vals[i]) / (jsq[i + 1] - jsq[i]) for i in range(len(vals) - 1)]
        ss = [str(x.quantize(Decimal('1.0001'))) for x in slopes]
        if nm == 'tetra':
            T(all(abs(x) < Decimal('1e-12') for x in slopes),
              f"tetra: the DERIVED ladder is EXACTLY FLAT in j^2 (4sin^2(m pi/4) = 2 for all odd m) [FT.76(5a)]")
        else:
            T(len(set(ss)) > 1, f"{nm}: the DERIVED read's slope in j^2 is NOT constant ({ss})")

print("\n" + "=" * 100)
print("D. §6.4's moment-of-inertia table: reproduced exactly, and the ratios are embedding-free")
print("=" * 100)
R2 = {'P3': Fr(1, 3), 'tetra': Fr(3, 8), 'cube': Fr(3, 4)}     # circumradius^2 in units of edge^2
KM = {'P3': Fr(8, 3), 'tetra': Fr(852, 205), 'cube': Fr(3311952, 395023)}
KF = {'P3': 6, 'tetra': 12, 'cube': 24}
DOC = {'P3': ('0.889', '2.000', '2.25'), 'tetra': ('1.559', '4.500', '2.89'), 'cube': ('6.288', '18.000', '2.86')}
for nm in ('P3', 'tetra', 'cube'):
    I1 = KM[nm] * R2[nm]; I2 = Fr(KF[nm]) * R2[nm]
    ratio = I2 / I1
    print(f"  {nm:6s} R^2 = {R2[nm]}, <K> = {KM[nm]}: I_S1 = {float(I1):.4f} (doc {DOC[nm][0]}), "
          f"I_S2 = {float(I2):.4f} (doc {DOC[nm][1]}), ratio = {float(ratio):.4f} (doc {DOC[nm][2]})")
    T(abs(Decimal(I1.numerator) / Decimal(I1.denominator) - Decimal(DOC[nm][0])) < Decimal('0.001'),
      f"{nm}: I_S1 reproduces the stated value")
    T(ratio == Fr(KF[nm]) / KM[nm], f"{nm}: ratio S2/S1 = E_int/<K> EXACTLY -- R^2 CANCELS (embedding-free)")
print("  ==> the numbers are exact and the RATIOS are embedding-independent, but I itself needs the")
print("      Euclidean circumradius -- an EMBEDDING datum the corpus does not supply (Def-H.21/FT.47/")
print("      FT.54 give an intrinsic piecewise-flat cone metric; no circumradius read exists).")

print("\n" + "=" * 100)
print("E. §6.2 hyperfine: the arithmetic, and which parts the corpus actually supports")
print("=" * 100)
T(Fr(3 ** 2 - 1 ** 2, 2 ** 2 - 0 ** 2) == 2, "Delta m^2_baryon / Delta m^2_meson = (3^2-1^2)/(2^2-0^2) = 8/4 = 2 exact")
print(f"  SM value quoted [EXT]: (m_Delta^2-m_N^2)/(m_rho^2-m_pi^2) ~= 1.1 -> the model gives 2.0,")
print(f"  a factor {float(Decimal(2)/Decimal('1.1')):.2f} discrepancy -- the proposal's 'factor-of-2 match' overstates it.")
note("winding ADDITIVITY is corpus-derived: k(Gamma) = k_1 + k_2 + d_12 [FT.34(3)]")
note("the CG range |k_1-k_2| <= k <= k_1+k_2 on the nonnegative cone [FT.52(3), FT.60(6)]")
print("      three spin-1/2 seeds: 2(x)2(x)2 = 4 (+) 2 (+) 2 -> j in {3/2, 1/2, 1/2}; Sym^3 = spin 3/2")
print("      [P-H9] -> the 'aligned Delta (j=3/2)' and 'mixed nucleon (j=1/2)' spin content IS supported.")
note("but the MASS splitting k^2/R^2 is the undeclared rotor term, and the state labels (pion/rho/")
note("  nucleon/Delta) are particle identifications -- inadmissible under the standing rules 1-2.")

print("\n" + "=" * 100)
print("F. §7 the Yukawa replacement: Z_phys, ln(Z), and the generation claim")
print("=" * 100)
T([4 ** 1, 4 ** 2, 4 ** 3] == [4, 16, 64], "4^|C| for |C| = 1,2,3 is (4,16,64) -- NOT the claimed (8, 1056, 1109312)")
Ztet, Zcub = 1057, 1109313
T(Ztet - 1 == 1056, "1056 = Z_byp(tetra) - 1 = 1057 - 1 [FT.68(1)]")
T(Zcub - 1 == 1109312, "1109312 = Z_byp(cube) - 1 = 1109313 - 1 [FT.68(3)]")
print("  ==> the three 'generation' numbers are (8, Z_tetra - 1, Z_cube - 1): they come from THREE")
print("      DIFFERENT SKELETONS' total bypass amplitudes, not from |C| = 1,2,3 layers of ONE core.")
print("      §7.2's 'same topological core wrapped in 1, 2, or 3 layers' is inconsistent with its own")
print("      numbers. And 8 matches no cover-census value I can find (4^1 = 4, 2^3 = 8 unexplained).")
lns = [Decimal(8).ln(), Decimal(1056).ln(), Decimal(1109312).ln()]
T(abs(lns[0] - Decimal('2.0794')) < Decimal('1e-3') and abs(lns[2] - Decimal('13.9193')) < Decimal('1e-3'),
  f"ln Z_phys = ({lns[0]:.4f}, {lns[1]:.4f}, {lns[2]:.4f}) as the proposal states")
T(abs(lns[2] / lns[0] - Decimal('6.696')) < Decimal('0.01'),
  f"the claimed hierarchy spans only {lns[2]/lns[0]:.4f} -- against [EXT] 3477: short by x{Decimal(3477)/(lns[2]/lns[0]):.0f}")
print("      so §9.2's 'right ORDER OF MAGNITUDE hierarchy' is refuted by the proposal's own numbers:")
print("      1 : 3.35 : 6.70 vs [EXT] 1 : 207 : 3477.")
note("ln(Z) is ill-defined as an entropy: Z is a SIGNED sum ((-1)^sum_kappa 4^|C| [FT.67(2)]) and")
note("  vanishes on most patterns; the corpus's ledger entropy is S_L = n_R ln2 [CT1.29], not ln Z.")
note("'Delta S = ln(Z_phys)' therefore contradicts CT1.29 and is dimensionally unmotivated.")

print("\n" + "=" * 100)
print("G. §3.1 'gravitational mass = entropy deficit (equivalence principle, Theorem 11)'")
print("=" * 100)
_DOCS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ALLG = "".join(era_paths.read(f) for f in
               ['A_axioms.md', 'B_foundation.md', 'C_geometry.md', 'D_electroweak.md',
                'E_electromagnetic.md', 'F_color.md', 'G_saturation.md'])
for w in ('Theorem 11', 'equivalence principle', 'N10', 'OP8', 'OP10', 'K-machine',
          'moment of inertia', 'rigid rotor', 'Regge', 'tumbling', 'magic number', 'shell model',
          'circumradius'):
    T(ALLG.count(w) == 0, f"corpus inventory: '{w}' count 0 -> no such tag/read")
# 'inertial' left the absent list with the A4/A6/A7 repair pass: L3(4) declares the single
# read m_i^2(q) := Delta S(q) (B Tier 2). The §3.1 adjudication itself stands: still no
# 'equivalence principle', no m_g^2 counterpart, no Theorem-11-style identification.
note("'inertial' is pinned PRESENT elsewhere (verify_H_gravmass §7): the L3(4) mass read,")
note("  declared by the repair pass; the equivalence-principle proposal remains refuted as above.")

print("\n" + "=" * 100)
print("H. OP10 'CPT algebra': what IS constructible from the two declared involutions")
print("=" * 100)
nv, DE = complete_graph(4)
U = undirected_from(nv, DE)
perms = automorphisms(nv, U)
rev = {(a, b): (b, a) for (a, b) in DE}
idx = {e: i for i, e in enumerate(DE)}
def mask(R): 
    b = 0
    for e in R: b |= 1 << idx[e]
    return b
# omega acts as R -> R^T on patterns [D2.6]; verify it is an involution and outside Aut
for bits in (0, 1, 3, 17, 129, 4095):
    R = frozenset(DE[i] for i in range(len(DE)) if (bits >> i) & 1)
    RT = frozenset(rev[e] for e in R)
    T(mask(frozenset(rev[e] for e in RT)) == bits, f"omega^2 = 1 on pattern {bits}")
nAnti = sum(1 for p in perms if all((p[a], p[b]) == (b, a) for (a, b) in DE))
T(nAnti == 0, f"no vertex permutation induces the global reversal (count {nAnti}) -> omega is NOT in Aut [FT.78(6)]")
T(all(mask(frozenset(rev[e] for e in frozenset(rev[e] for e in frozenset(DE[i] for i in range(len(DE)) if (b_ >> i) & 1)))) == b_
      for b_ in (0, 5, 129, 4095)), "omega^2 = 1 on whole patterns (reversal composed with itself)")
print("  Theta_L [D2.7] acts on the ledger order and G(e) -> G(e)* (sigma fixed, kappa -> -kappa);")
print("  omega [D2.6] acts on chain orientation (s<->t), charge -> -charge, chirality -> -chirality.")
print("  They act on DISJOINT data (edge set vs phase/ledger order) => they commute =>")
print("  <omega, Theta_L> = Z_2 x Z_2 on the skeleton registration data  [machine: omega^2 = 1 above].")
note("charge -> -charge under omega matches FT.40's omega-covariance of q_core (already derived)")

print("\n" + "=" * 100)
print(f"AUDIT TOTALS: {ok} checks passed, {fail} failed")
print("=" * 100)

assert fail == 0, f"{fail} audit failures"
print(f"\nverify_H_tumbling: {ok} checks green")
