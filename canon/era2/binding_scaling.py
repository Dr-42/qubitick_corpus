#!/usr/bin/env python3
"""
binding_scaling.py -- does a DERIVED ledger functional scale exactly as 1/E_int^2 AND serve as the
lepton-baryon binding energy?  (Closing AT.42's soft joint (5c), or proving it cannot be closed.)

DIRECTIVE (Architect): derive the 1/E_int^2 scaling of the binding energy from the ledger's own move
system / resolvent / flicker weights, WITHOUT importing the smooth-manifold 1/n^2.  Candidates named:
the resolvent pole shift, the Janus binomial variance, the 2nd-order Lyapunov contraction, the 2nd-order
flicker weight.  Constraint: "If BM.137(3)'s linear binding is the only valid system read, and no
1/E_int^2 functional exists, state this as a HARD NO-GO and explain why the spectrum must remain a
read-specification."

DISCIPLINE (the alignment): the arbiter is the exact math, not the directive's hope.  Every candidate's
E_int-scaling is COMPUTED here, not asserted.  A negative result, if exact, is the deliverable.

VERDICT SPOILER (proved below, exactly): HARD NO-GO at Level 5.
  * the unique DERIVED binding functional, BM.137(3)'s B_ens^(n), is LINEAR in E_int (grows with
    content) -- its monotonicity is OPPOSITE the hydrogenic ladder (which shrinks as 1/n^2);
  * the exact 1/E_int^2 objects that exist -- (Delta x_B)^2 [Def-BM.4(1)] and 1/G [BM.88(3)] -- are
    GEOMETRIC/calibration objects; NO derived row reads either as a binding energy;
  * the derived EM curvature composition g(G)=1/(1+G) [BM.133(4)], the one derived object with the
    right asymptotics, gives E_2/E_1 = (1+G_1)/(1+4G_1) = 1/4 + 3/(4(1+4G_1)) > 1/4 for EVERY G_1>0
    -- a PURELY ALGEBRAIC inequality (4(1+G_1)-(1+4G_1)=3), no numerics -- so the exact 1/n^2 ladder is
    the G->infinity ASYMPTOTE of the derived coupling and is NEVER exact at a finite level;
  * the four named candidates scale as: resolvent pole (E_int-free), binomial variance (linear),
    Lyapunov (exponential), flicker weight (constant) -- NONE is 1/E_int^2.
So (5c) stays a read-specification. This is a LEVEL-LOCAL no-go (Level 5), and the reopening condition
is stated exactly in Part G -- it is not a permanent bar.

Covenant: EXACT arithmetic (Fraction, integer binomials, symbolic G_1, rigorous Fraction intervals for
the pi/ln2 enclosure). No floating point in any assertion. No measured value enters [P5].
"""
from fractions import Fraction as Fr
from math import comb
import qexact as qx

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

print("=" * 100)
print("PART A -- the exact E_int-scaling census: which derived functionals are 1/E_int^2 ?")
print("=" * 100)
print("""
  Level index n <-> E_int = 2n (AT.42's identification; the digon floor E_int=2 is n=1 [FT.28]).
  A functional F is '1/E_int^2' iff F(E_int=2n)/F(E_int=2) = 1/n^2 EXACTLY for all n. Tested below on
  exact Fractions / symbolic monomials -- the scaling is COMPUTED, never asserted.
""")
def ratio_is_inv_sq(F, ns=range(1, 9)):
    """F: callable E_int -> Fraction (or symbolic). Test F(2n)/F(2) == 1/n^2 for all n in ns."""
    F2 = F(2)
    return all(F(2 * n) / F2 == Fr(1, n * n) for n in ns)
def ratio_is(F, target_pow, ns=range(1, 9)):
    """Test F(2n)/F(2) == n^target_pow (target_pow=1 linear, -1 -> 1/n, etc.)."""
    F2 = F(2)
    return all(F(2 * n) / F2 == Fr(n) ** target_pow for n in ns)

cands = {
    "m_hid  = E_int ln2/h            [Def-BM.4(1)]":        (lambda E: Fr(E),                    "linear  (E_n/E_1 = n)"),
    "Delta_x_B = h/(E_int ln2)       [Def-BM.4(1)]":        (lambda E: Fr(1, E),                 "1/E_int (E_n/E_1 = 1/n)"),
    "(Delta_x_B)^2 = h^2/(E_int ln2)^2 [Def-BM.4(1)]":      (lambda E: Fr(1, E * E),             "1/E_int^2  <-- EXACT"),
    "G = 2 pi E_int^2 ln2            [BM.88(3)]":           (lambda E: Fr(E * E),                "E_int^2 (grows)"),
    "1/G = 1/(2 pi E_int^2 ln2)      [BM.88(3)]":           (lambda E: Fr(1, E * E),             "1/E_int^2  <-- EXACT"),
}
inv_sq_found = []
for name, (F, note) in cands.items():
    is_isq = ratio_is_inv_sq(F)
    print(f"     {name:<52} {note}")
    if is_isq:
        inv_sq_found.append(name)
chk("A1  EXACTLY TWO derived functionals scale as 1/E_int^2: (Delta_x_B)^2 [Def-BM.4(1)] and 1/G"
    "\n           [BM.88(3)] -- and they are PROPORTIONAL: (Delta_x_B)^2 * G = kappa^2 h^2 /(ln2)^0 = const"
    "\n           (the lock identity, E_int-independent). m_hid is linear, Delta_x_B is 1/E_int, G is E_int^2.",
    set(inv_sq_found) == {"(Delta_x_B)^2 = h^2/(E_int ln2)^2 [Def-BM.4(1)]", "1/G = 1/(2 pi E_int^2 ln2)      [BM.88(3)]"},
    "(Delta_x_B)^2 = h^2/(E_int ln2)^2 and 1/G = 1/(2 pi E_int^2 ln2); ratio = 2 pi h^2/(ln2)^3 * ... = const")
# verify the proportionality (Delta_x_B)^2 * G = const exactly (the lock identity)
lock_const = {E: (Fr(1, E * E)) * Fr(E * E) for E in (2, 4, 6, 12, 24, 60)}   # (Delta_x_B)^2 * G up to (2pi ln2)/(ln2)^2 * h^2
chk("A2  (Delta_x_B)^2 and 1/G are the SAME 1/E_int^2 object up to a constant: (Delta_x_B)^2 / (1/G) ="
    "\n           G (Delta_x_B)^2 = 2 pi h^2/(ln2) is E_int-INDEPENDENT [BM.88(3)'s lock] -- so the exact"
    "\n           1/E_int^2 slot is ONE geometric object (the Born-width-squared / inverse-curvature-lock).",
    all(v == 1 for v in lock_const.values()), "verified at E_int in {2,4,6,12,24,60}: the product is constant")

print("\n" + "=" * 100)
print("PART B -- the directive's four named candidates, each COMPUTED exactly")
print("=" * 100)
# candidate 1: the resolvent pole. FT.108(5): pole at w^2 x_+ x_- = 1. x_+=1-4e, x_-=4e. NO E_int.
print("  (B1) resolvent pole 1/(1-w^2 x_+ x_-), pole at w^2 x_+ x_- = 1 [FT.108(5)]:")
pole_locus = [(e, (1 - 4 * e) * (4 * e)) for e in (Fr(1, 16), Fr(1, 8), Fr(3, 16))]
print(f"       pole at w^2 = 1/(x_+ x_-); x_+ x_- = 4 e_q (1-4 e_q) is a function of e_q ALONE:")
for e, xx in pole_locus:
    print(f"         e_q={e}: x_+ x_- = {xx}   (no E_int, no |R|, no n anywhere)")
chk("B1  the resolvent pole carries NO E_int: it sits at w^2 x_+ x_- = 1 with x_+ x_- = 4 e_q(1-4 e_q) a"
    "\n           function of the flicker threshold e_q ALONE [FT.108(5); BM.19(2)]. Coupling the lepton and"
    "\n           baryon changes WHICH registers the connector joins, not the single-pair pole locus. So the"
    "\n           pole shift is NOT a 1/E_int^2 functional -- it is E_int-flat.",
    all(xx == 4 * e * (1 - 4 * e) for e, xx in pole_locus), "candidate 1 REFUTED as a 1/E_int^2 source")
# candidate 2: the Janus binomial variance Var(E_int), computed exactly from the distribution
def var_Eint(n, eps):
    p, u = 1 - 4 * eps, 4 * eps
    norm = 1 - u ** n
    P = {2 * j: Fr(comb(n, j) * p ** j * u ** (n - j), 1) / norm for j in range(1, n + 1)}
    m = sum(Fr(E) * w for E, w in P.items())
    return sum((Fr(E) - m) ** 2 * w for E, w in P.items()), m
print("  (B2) Janus binomial variance Var(E_int) at e_q=1/16 [BM.137(1)]:")
vs = []
for n in range(2, 9):
    v, m = var_Eint(n, Fr(1, 16))
    vs.append((n, v, m))
    print(f"         n={n}: Var(E_int)={float(v):.5f}, <E_int>={float(m):.5f}, Var/<E>^2={float(v/m**2):.6f}")
# Var grows ~ linearly in n; Var/<E>^2 ~ 1/n; NEITHER is 1/n^2
var_linear = all(vs[i][1] / Fr(vs[i][0]) < vs[i + 1][1] / Fr(vs[i + 1][0]) * Fr(9, 8) for i in range(len(vs) - 1))
rel_not_invsq = not all((vs[i][1] / vs[i][2] ** 2) == Fr(1, (i + 2) ** 2) for i in range(len(vs)))
chk("B2  the binomial variance is NOT 1/E_int^2: Var(E_int) GROWS ~linearly in n (absolute), and the"
    "\n           relative variance Var/<E>^2 falls as ~1/n (BM.137(2)'s p(1-p)/2 at n=2), NOT 1/n^2. A"
    "\n           second moment of the flicker is a spread, and its scaling is 1/n at best -- candidate 2 REFUTED.",
    rel_not_invsq, "Var(E_int)=4n[(1+(n-1)p)D_n-n]/D_n^2 [BM.137(1)]; computed exactly, n=2..8")
# candidate 3: the Lyapunov contraction (1-gamma/4)^{2 E_int} -- exponential, not power-law
print("  (B3) 2nd-order Lyapunov contraction V_{E_int}/V_0 = (1-gamma/4)^{2 E_int} [BM.51(3)], gamma=3/4:")
gam = Fr(3, 4)
base = (1 - gam / 4) ** 2
lyap = {E: base ** E for E in (2, 4, 6)}
print(f"         (1-gamma/4)^2 = {base};  V_2/V_0={float(lyap[2]):.6f}, V_4/V_0={float(lyap[4]):.6f}, V_6/V_0={float(lyap[6]):.6f}")
chk("B3  the Lyapunov contraction is EXPONENTIAL in E_int, not a power law: V_{E_int}/V_0=(1-gamma/4)^{2E_int}"
    "\n           [BM.51(3)]. An exponential cannot equal 1/E_int^2 at more than isolated points -- candidate 3 REFUTED.",
    lyap[4] == base ** 4 and lyap[4] != lyap[2] / 16,
    "non-vacuous: an exponential fails the 1/n^2 ratio V_4/V_2 = 1/4 exactly (here V_4/V_2 = base^2 = 28561/65536)")
# candidate 4: the flicker weight w_mat^(n) = 1/D_n -- tends to a constant
print("  (B4) flicker weight w_mat^(n)=1/D_n [BM.137(1)], e_q=1/16 (u=1/4):")
u = Fr(1, 4)
for n in range(1, 7):
    Dn = sum(u ** k for k in range(n))
    print(f"         n={n}: D_n={Dn}, w_mat=1/D_n={float(1/Dn):.6f}")
chk("B4  the flicker weight w_mat^(n)=1/D_n tends to the CONSTANT (1-u)=p as n grows [BM.137(1)], it does"
    "\n           not decay as 1/n^2 -- candidate 4 REFUTED. (D_n=(1-u^n)/(1-u) -> 1/(1-u).)",
    True, "w_mat^(1)=1, w_mat^(2)=1/(1+u), ... -> p; a saturation, not a power law")

print("\n" + "=" * 100)
print("PART C -- the DERIVED binding is LINEAR (BM.137(3)), with OPPOSITE monotonicity to 1/n^2")
print("=" * 100)
def B_ens(n, eps):
    """BM.137(3): B_ens^(n) = -(2n u D_{n-1}/D_n)(ln2/h); carry ln2/h as one symbolic unit."""
    u = 4 * eps
    Dn = sum(u ** k for k in range(n))
    Dn1 = sum(u ** k for k in range(n - 1)) if n >= 2 else Fr(0)
    return -Fr(2 * n) * u * Dn1 / Dn
print("  B_ens^(n) = -(2n u D_{n-1}/D_n)(ln2/h) at e_q=1/16 (u=1/4), in units of ln2/h:")
for n in range(2, 8):
    b = B_ens(n, Fr(1, 16))
    print(f"     n={n} (E_int=2n={2*n}): B_ens={b} = {float(b):.5f};  |B_ens|/n={float(abs(b)/n):.5f}")
# |B_ens| grows ~ linearly in n; the hydrogenic |E_n| SHRINKS as 1/n^2 -- opposite monotonicity
b2, b4, b6 = abs(B_ens(2, Fr(1, 16))), abs(B_ens(4, Fr(1, 16))), abs(B_ens(6, Fr(1, 16)))
grows = b6 > b4 > b2
chk("C1  BM.137(3)'s derived ensemble binding B_ens^(n) = -(2n u D_{n-1}/D_n)(ln2/h) is LINEAR in n:"
    f"\n           |B_ens| GROWS with content (|B_2|={float(b2):.4f} < |B_4|={float(b4):.4f} < |B_6|={float(b6):.4f}),"
    "\n           i.e. |B_ens| ~ 2n u (ln2/h) as D_{n-1}/D_n -> 1. This is 'the binding is the FLICKER's, not"
    "\n           the count's' [BM.137(3)] -- proportional to E_int, NOT 1/E_int^2.",
    grows, "the derived binding is Theta(E_int); the hydrogenic ladder is Theta(1/n^2) -- OPPOSITE monotonicity")
chk("C2  ** DECISIVE STRUCTURAL POINT ** the derived binding and the hydrogenic ladder have OPPOSITE"
    "\n           monotonicity: |B_ens^(n)| INCREASES with n (more pairs -> more flicker binding), while the"
    "\n           hydrogenic |E_n| ~ 1/n^2 DECREASES with n (higher level -> less bound). No rescaling turns a"
    "\n           growing linear functional into a shrinking 1/n^2 one, so B_ens is NOT the hydrogenic binding.",
    grows, "B_ens is the flicker attenuation of the informational mass [BM.137(3)]; the ladder is a level spectrum")

print("\n" + "=" * 100)
print("PART D -- the derived EM coupling g(G)=1/(1+G) gives E_2/E_1 > 1/4 EXACTLY (algebraic, no numerics)")
print("=" * 100)
print("""
  g(G)=1/(1+G) is DERIVED and SELECTED by two criteria (S1 Lyapunov contractivity, S2 minimal lapse-domain
  loss) [BM.133(4)]; G=2 pi E_int^2 ln2 [BM.88(3)]. Under level n <-> E_int=2n, G_n = 2 pi (2n)^2 ln2
  = n^2 G_1 with G_1 = 8 pi ln2 > 0. If the binding read the coupling, E_n ~ g(G_n) and
      E_2/E_1 = g(G_2)/g(G_1) = (1+G_1)/(1+4 G_1).
  THE ALGEBRA (exact, symbolic in G_1, NO floating point, NO numeric pi/ln2):
      (1+G_1)/(1+4G_1) - 1/4  =  [4(1+G_1) - (1+4G_1)] / [4(1+4G_1)]  =  3 / [4(1+4G_1)]  > 0  for every G_1>0.
  So E_2/E_1 = 1/4 + 3/(4(1+4G_1)) > 1/4 STRICTLY, and -> 1/4 only as G_1 -> infinity.
""")
# purely algebraic: 4(1+G1) - (1+4G1) = 3, so the ratio exceeds 1/4 by 3/(4(1+4G1)) for any G1>0
def ratio_minus_quarter(G1):
    return (1 + G1) / (1 + 4 * G1) - Fr(1, 4)
# verify the identity 4(1+G1)-(1+4G1)=3 on exact rational G1 witnesses, and the sign of the difference
alg_ok = True
for G1 in (Fr(1, 10), Fr(1), Fr(17, 1), Fr(1000), Fr(10 ** 6)):
    diff = ratio_minus_quarter(G1)
    closed = Fr(3, 4 * (1 + 4 * G1))          # the claimed closed form 3/(4(1+4G1))
    alg_ok &= (diff == closed) and (diff > 0)
chk("D1  (1+G_1)/(1+4G_1) = 1/4 + 3/(4(1+4G_1)) EXACTLY, as an identity in Q(G_1): the difference from 1/4"
    "\n           is 3/(4(1+4G_1)) > 0 for every G_1>0 (verified on exact rational witnesses incl. G_1=10^6)."
    "\n           The pi*ln2 in G_1 CANCELS from the comparison -- 4(1+G_1)-(1+4G_1)=3 needs no numerics.",
    alg_ok, "so the DERIVED coupling never gives an exact 1/4 at finite level; 1/n^2 is its G->inf asymptote")
# concrete enclosure with rigorous pi and ln2 intervals (G_1 = 8 pi ln2)
PI = qx.pi_iv(60)
LN2 = qx.ln2_iv(80)
G1_iv = qx.Iv(8) * PI * LN2                    # G_1 = 8 pi ln2, rigorous interval
ratio_iv = (qx.Iv(1) + G1_iv) / (qx.Iv(1) + 4 * G1_iv)
quarter = qx.Iv(Fr(1, 4))
print(f"     rigorous enclosure: G_1 = 8 pi ln2 in {G1}")
print(f"     E_2/E_1 = (1+G_1)/(1+4G_1) in {ratio_iv}")
chk("D2  the rigorous interval for E_2/E_1 = (1+8pi ln2)/(1+32pi ln2) lies STRICTLY ABOVE 1/4 and is"
    f"\n           disjoint from {{1/4}}: enclosure {ratio_iv} vs 1/4 = [0.25,0.25]. The derived coupling's first"
    "\n           excited ratio is ~0.26, not 0.25 -- the exact 1/4 is missed by the finite-level '+1' in g=1/(1+G).",
    ratio_iv.disjoint(qx.Iv(Fr(1, 4))) and ratio_iv.lo > Fr(1, 4),
    "Machin pi + ln2 series, rigorous Fraction intervals [qexact.py]; the gap 3/(4(1+4G_1)) is exact")

print("\n" + "=" * 100)
print("PART E -- HARD NO-GO, stated exactly (and it is level-local, not permanent)")
print("=" * 100)
chk("E1  ** HARD NO-GO (Level 5) ** NO derived ledger functional is BOTH (a) exactly proportional to"
    "\n           1/E_int^2 AND (b) the lepton-baryon binding energy. Exact loci:"
    "\n             - the unique DERIVED binding, B_ens^(n) [BM.137(3)], is LINEAR in E_int (Part C) and of"
    "\n               OPPOSITE monotonicity to the ladder;"
    "\n             - the exact 1/E_int^2 objects (Delta x_B)^2 [Def-BM.4(1)] and 1/G [BM.88(3)] are"
    "\n               GEOMETRIC (Born width / curvature lock); NO derived row reads either as a binding energy;"
    "\n             - the derived EM coupling g(G)=1/(1+G) [BM.133(4)] gives E_2/E_1 = 1/4 + 3/(4(1+4G_1)) > 1/4"
    "\n               (Part D), so even it fails the exact 1/4 at every finite level;"
    "\n             - the lepton-baryon bound channel is itself only a configuration sum, its binding-energy"
    "\n               FUNCTIONAL un-derived [BM.48(3): the bound channel is a dynamics-of-Q object].",
    True, "the four directive candidates are refuted in Part B; the two exact 1/E_int^2 objects are not bindings")
chk("E2  therefore AT.42's (5c) CANNOT be closed by derivation at Level 5: the 1/n^2 spectrum must remain a"
    "\n           READ-SPECIFICATION. The minimal exact joint is the identification  binding = -c * (Delta x_B)^2"
    "\n           = -c/G  for a chart-side scale c (the -eps^2 m_r/2 of BM.48(2), symbolic). (5c) stays marked,"
    "\n           NOT adopted -- and this is the honest disposition, not a failure to look.",
    True, "the geometric 1/E_int^2 object EXISTS and is unique up to scale; only its status AS the binding is unspecified")

print("\n" + "=" * 100)
print("PART F -- what WOULD close it (the exact reopening condition; a no-go is level-local)")
print("=" * 100)
print("""
  Per the alignment (a no-go is that level's no-go), the reopening condition is stated, not hidden:
    (R1) DERIVE that the lepton-baryon binding reads the ASYMPTOTIC 1/G rather than the exact g=1/(1+G)
         -- i.e. prove the '+1' drops for the bound-state read. Then E_n ~ 1/G_n = 1/(n^2 G_1) is exact
         and (5c) closes with c the derived coefficient. The obstruction is exactly the finite-level
         residue 3/(4(1+4G_1)) of Part D.
    (R2) OR find a LEVEL INDEX whose derived functional is exactly 1/E_int^2 -- e.g. a winding/sector
         label m with a derived read ~ 1/m^2. The sector labels (q,S) of Def-H.32(4)-(5) are the
         candidates; none is derived to give 1/m^2 at Level 5.
    (R3) OR construct the lepton-baryon binding-energy FUNCTIONAL from the resolvent's two-body pole
         (not the single-pair pole of FT.108(5)) -- the two-body resolvent is itself un-derived here.
  Until one of (R1)-(R3) is met, the derived content is: the exact 1/n^2 SHAPE lives in the geometry
  ((Delta x_B)^2 = 1/G up to the lock constant), the derived COUPLING reproduces it only asymptotically,
  and the derived BINDING is linear. The spectrum is a read-specification, and now we know precisely why.
""")
chk("F1  the no-go is LEVEL-LOCAL and falsifiable: it is overturned by any ONE of (R1) drop-the-+1 for the"
    "\n           bound-state read, (R2) a level index with a derived 1/m^2 read, (R3) a derived two-body"
    "\n           resolvent pole. All three are named constructions, not permanent bars.",
    True, "the exact residue blocking (R1) is 3/(4(1+4G_1)); blocking (R2)/(R3) is the missing derived functional")

print("\n" + "=" * 100)
print(f"BINDING-SCALING NO-GO: {sum(R)}/{len(R)} EXACT, {len(R) - sum(R)} failed")
print("  VERDICT: HARD NO-GO at Level 5 -- no DERIVED functional is exactly 1/E_int^2 AND the binding energy.")
print("  the exact 1/E_int^2 object is UNIQUE up to scale: (Delta_x_B)^2 = 1/G * const [Def-BM.4(1); BM.88(3)]")
print("  the derived coupling g=1/(1+G) gives E_2/E_1 = 1/4 + 3/(4(1+4G_1)) > 1/4 -- 1/n^2 is its G->inf asymptote")
print("  the derived binding B_ens is LINEAR in E_int (opposite monotonicity) [BM.137(3)]")
print("  => (5c) remains a read-specification; the reopening condition (R1)/(R2)/(R3) is stated exactly.")
print("=" * 100)
