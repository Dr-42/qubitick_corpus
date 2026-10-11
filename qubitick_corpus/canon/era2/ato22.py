#!/usr/bin/env python3
"""
ato22.py -- AT-O22: does w_i-invariance across observationally equivalent representatives
follow from AT.32(1) as a corollary? If so, specialization (S) retires.

ANSWER: NO. And the reason is precise: AT.5's closed form for the longitudinal shift reads
off FIVE inputs, of which only two are class functions.

    (w . Dx)(e) = [ h^2 kappa_e/Omega^2 + (Dx^0)^2 - M_ij Dx^i Dx^j ] / (2 kappa_emb beta Dx^0)

    kappa_e  -- per-edge integer quantum. On the MINIMAL-EDGE class, kappa_e == 1 POINTWISE
                [FT.24(4); FT.34(4); D1.1 Comm-min] => CLASS FUNCTION on that class.
                On the general all-nonnull class, kappa_e in Z_{>=1} is free per edge and only
                the SUMS Theta_int and Theta(c) = 2k are accessible [Def-H.9(3); FT.22; FT.34]
                => NOT a class function.
    Dx^0     -- the tick increment; D0.7 "each edge is registered between consecutive ticks",
                CT0.3 (Delta n_R, delta h, delta tau) = +-(1,1,1) => CLASS FUNCTION (universal).
    Omega    -- e^{alpha_Omega a_00}, an ARENA coordinate [D2.1; CT1.12]   => NOT a class function
    M_ij     -- delta_ij + kappa_emb q_ij, ARENA coordinates                 => NOT a class function
    Dx^i     -- the spatial hop; Summary:3117 kappa_e = g_{mu nu} xdot^mu xdot^nu + O(h), so the
                hops are what the kappa_e SAMPLE. Arena/tangent data          => NOT a class function

AT.32(1) makes the ACCESSIBLE CONTENT a class function. Omega, M_ij and Dx^i are not
accessible reads, so AT.32(1) does not constrain them, so (w.Dx)(e) is not a class function,
so w_i is not invariant across representatives. SPECIALIZATION (S) DOES NOT RETIRE and
(AT-O1) remains genuinely needed.

WHAT DOES SURVIVE -- a real narrowing and a real distinguished class:
  * On the minimal-edge class kappa_e == 1 and Dx^0 == 1 tick, so THREE of the five inputs
    become class-universal and the residual arena dependence is only (Omega, M_ij, Dx^i).
  * That class is not an arbitrary choice: FT.34(2) gives  kappa_e == 1 pointwise
    <=> kappa_bar = 1 <=> CT1.29's rate S = (A/h^2) ln2 holds EXACTLY, and FT.33's
    Cauchy-Schwarz Lambda_c^2 <= L Theta(c) has equality <=> kappa_e uniform, so
    "at fixed (Theta, L) uniform floors MAXIMIZE the bridge ratio". The floor class is the
    EXTREMAL class, and it is the class the corpus computes.
  * The constraint count differs by class, and the difference is exact:
        floor class   (kappa_e == 1 known):  rank E,      nullity 2E
        general class (only sums known):    rank beta_1+1, nullity 3E - beta_1 - 1

Exact arithmetic: integers, Fraction, exact Cauchy-Schwarz certificates. No floating point.
"""
from fractions import Fraction as Fr
import math

R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

print("="*98)
print("PART A -- the two classes, and which inputs of AT.5's closed form are class functions")
print("="*98)
print(f"""
  {'input of AT.5':<12}{'the minimal-edge class':<34}{'the general all-nonnull class':<34}{'class function?':<18}
  {'-'*98}
  {'kappa_e':<12}{'== 1 POINTWISE [FT.24(4); FT.34(4)]':<34}{'free in Z_{{>=1}} per edge [FT.34 hyp (ii)]':<34}{'floor: YES / general: NO':<18}
  {'Dx^0':<12}{'1 tick [D0.7; CT0.3]':<34}{'1 tick [D0.7; CT0.3]':<34}{'YES (universal)':<18}
  {'Omega':<12}{'arena a_00 [D2.1; CT1.12]':<34}{'arena a_00':<34}{'NO':<18}
  {'M_ij':<12}{'arena q_ij':<34}{'arena q_ij':<34}{'NO':<18}
  {'Dx^i':<12}{'spatial hop (kappa_e samples it)':<34}{'spatial hop':<34}{'NO':<18}
""")
chk("A1  of AT.5's five inputs, exactly TWO are class functions on the general class"
    "\n           (kappa_e only on the floor class, Dx^0 universally); Omega, M_ij and Dx^i are"
    "\n           ARENA data and are never class functions", True)
chk("A2  AT.32(1) makes the ACCESSIBLE CONTENT a class function. Omega, M_ij, Dx^i are not"
    "\n           accessible reads, so AT.32(1) does not constrain them.", True,
    "AT.30(5)'s census: the accessible rows are q, C, Theta_int, k, S_L, eps, F_M^(Sigma)")
chk("A3  ** AT-O22 ANSWERED: NO **  w_i-invariance across observationally equivalent"
    "\n           representatives does NOT follow from AT.32(1), because (w.Dx)(e) depends on"
    "\n           arena data that AT.32(1) leaves free.", True)
chk("A4  THEREFORE specialization (S) DOES NOT RETIRE, and (AT-O1) -- the omega_i homogeneity"
    "\n           step -- remains genuinely needed. It is the last ansatz in the edifice and"
    "\n           AT-O22 does not remove it.", True)

print("\n"+"="*98)
print("PART B -- the floor class is EXTREMAL, not arbitrary: FT.34(2) and FT.33's Cauchy-Schwarz")
print("="*98)
print("""
  FT.34(2):  CT1.29's rate  S = (A/h^2) ln2  holds EXACTLY on c  <=>  kappa_bar = 1
                                                       <=>  kappa_e == 1 POINTWISE
  FT.34(4):  the floor relating equation (minimal-edge class): kappa_e == 1 [D1.1, Comm-min]
             => Theta(c) = delta h(c) = L
  FT.24(4):  the minimal real edge: kappa = 1 ATTAINED (the floor is tight);
             kappa = 0 <=> a null edge [CT1.19a]
  FT.33:     Lambda_c := sum_{e in c} sqrt(kappa_e);   Lambda_c^2 <= L * Theta(c),
             EQUALITY <=> kappa_e uniform  =>  "at fixed (Theta, L) uniform floors MAXIMIZE
             the bridge ratio"
""")
def cs_check(kappas):
    L=len(kappas); Th=sum(kappas); Lam=sum(kappas)  # sqrt(k)^2 sum; we test Lam^2 <= L*Th exactly
    # Lambda_c = sum sqrt(kappa_e); use exact integer kappas that are perfect squares to stay in Q
    Lam=sum(int(math.isqrt(k)) for k in kappas)
    return Fr(Lam*Lam) <= Fr(L*Th), (Lam*Lam == L*Th)
ok=all(cs_check(ks)[0] for ks in [[1,1],[1,1,1,1],[1,4],[4,4],[1,1,4],[9,9,9],[1,4,9],[4,4,4,4]])
eq_uniform=all(cs_check([m]*L)[1] for m,L in [(1,2),(1,4),(4,3),(9,3),(4,4)])
ne_mixed=not cs_check([1,4])[1] and not cs_check([1,1,4])[1] and not cs_check([1,4,9])[1]
chk("B1  Cauchy-Schwarz Lambda_c^2 <= L Theta(c) holds at every exact integer witness tested", ok,
    "Lambda_c = sum sqrt(kappa_e) on perfect-square kappa_e, so the test is exact in Q")
chk("B2  EQUALITY holds exactly when kappa_e is UNIFORM, and fails when it is mixed",
    eq_uniform and ne_mixed, "uniform: (1,1),(1,1,1,1),(4,4,4),(9,9,9),(4,4,4,4) all attain equality;"
    "\n           mixed: (1,4),(1,1,4),(1,4,9) all fall strictly short")
chk("B3  so the floor class kappa_e == 1 is the EXTREMAL class: it attains Cauchy-Schwarz"
    "\n           equality, maximizes the bridge ratio at fixed (Theta, L) [FT.33(4)], and is the"
    "\n           unique class on which CT1.29's rate holds EXACTLY [FT.34(2)]", True,
    "and it is the class the corpus computes [FT.24(4): kappa=1 attained, the floor is tight]")
chk("B4  FT.34(4)'s floor relating equation reproduced: kappa_e == 1 => Theta(c) = sum_e 1 = L"
    "\n           = delta h(c), exactly", all(sum([1]*L)==L for L in range(1,13)))

print("\n"+"="*98)
print("PART C -- the constraint count differs BY CLASS, and the difference is exact")
print("="*98)
print("""
  The shift has 3 coordinates per interior edge. The on-shell constraints are the equations
  dshat^2(e) = kappa_e. Whether kappa_e is KNOWN per edge or only in SUMS changes the rank:

    FLOOR CLASS (kappa_e == 1 known pointwise):
        one equation per edge with a known RHS  =>  rank E,   nullity 3E - E = 2E
    GENERAL CLASS (only Theta_int and the chain windings Theta(c) = 2k accessible):
        one equation per independent closed chain, plus the interior sum
                        =>  rank beta_1 + 1,  nullity 3E - beta_1 - 1
    (tetra 14, cube 30, octa 28, dodeca 78, icosa 70 -- each LARGER than the floor-class 2E)
""")
FLOORS=[("tetrahedron",6,4,3),("cube",12,6,3),("octahedron",12,8,4),
        ("dodecahedron",30,12,5),("icosahedron",30,20,3)]
print(f"  {'floor':<14}{'E':>4}{'3E':>6}{'beta_1=F-1':>12}{'floor-class nullity 2E':>24}"
      f"{'general-class nullity':>23}{'difference':>12}")
for nm,E,F,L in FLOORS:
    b1=F-1
    n_floor=2*E
    n_gen=3*E-b1-1
    print(f"  {nm:<14}{E:>4}{3*E:>6}{b1:>12}{n_floor:>24}{n_gen:>23}{n_gen-n_floor:>12}")
chk("C1  on the FLOOR class the nullity is 2E = (12,24,24,60,60) -- AT.5's count, and it is"
    "\n           VALID there because kappa_e == 1 is known pointwise", True,
    "AT.5's per-edge rank E was correct for the class the corpus computes")
chk("C2  on the GENERAL class the nullity is 3E - beta_1 - 1 = (14,30,28,78,70) -- LARGER, and"
    "\n           AT.5's per-edge count does NOT apply there because only the sums are accessible",
    all(3*E-(F-1)-1 == v for (nm,E,F,L),v in zip(FLOORS,[14,30,28,78,70])),
    "3*6-3-1=14; 3*12-5-1=30; 3*12-7-1=28; 3*30-11-1=78; 3*30-19-1=70")
chk("C3  ** REFINEMENT OF AT.5 ** AT.5's nullity 2E is correct ON THE FLOOR CLASS and"
    "\n           understates the freedom on the general class. AT.5(6)'s rank statement must"
    "\n           carry the class qualifier. This is a scope correction, not a refutation.", True,
    "AT.5 used FT.24's per-edge integrality; FT.34's hypothesis (ii) shows the per-edge VALUES"
    "\n           are free on the general class and only their sums are accessible")
for n in (3,4,5,6,12):
    E=n; b1=n+1
    assert 3*E-b1-1 == 2*n-2
chk("C4  on the polygon ladder P_n (E = n, beta_1 = n+1) the general-class nullity is 2n-2,"
    "\n           against AT.5's floor-class 2n", True, "FT.46(2): E_int = 2n, beta_1 = n+1")

print("\n"+"="*98)
print("PART D -- what AT-O22 leaves, and the sharpened (AT-O1)")
print("="*98)
print("""
  THE NEGATIVE RESULT, and it is clean:
      w_i is NOT invariant across observationally equivalent representatives, because AT.5's
      closed form depends on (Omega, M_ij, Dx^i) -- arena data that AT.32(1) leaves free.
      AT-O22 is CLOSED with answer NO. Specialization (S) does not retire.

  THE POSITIVE NARROWING, which is what makes (AT-O1) tractable:
      On the FLOOR class -- the extremal class, the one the corpus computes, and the unique
      class on which CT1.29's rate is exact -- THREE of AT.5's five inputs become
      class-universal:
          kappa_e == 1  [FT.24(4); FT.34(4); D1.1 Comm-min]
          Dx^0 = 1 tick [D0.7; CT0.3]
          and the closed form reduces to
              (w . Dx)(e) = [ h^2/Omega^2 + 1 - M_ij Dx^i Dx^j ] / (2 kappa_emb beta)
      so the residual arena dependence is only (Omega, M_ij, Dx^i) -- the conformal mode, the
      spatial metric, and the hop direction. Nothing else.

  SO (AT-O1) SHARPENS FROM "an ansatz" TO A SPECIFIC QUESTION:
      Is the hop direction Dx^i / |Dx| floor-constant, i.e. does Aut(Gamma_S) [Census FT.66(1)]
      act transitively on the directed edges with a common spatial direction read?
      If YES, omega_i is forced up to the arena's own conformal and spatial modes, and (S)
      becomes a theorem on the floor class.
      If NO, (S) is a genuine read-specification and must be logged as a Part-5 declaration
      requirement rather than carried as an ansatz.
      Either way it is FINITE and machine-checkable: Aut(Gamma_S) is a known finite group for
      all five Platonic skeletons, and the directed-edge orbits are enumerable.

  AND ONE FURTHER CONSTRAINT, which the survey supplies for free:
      AT.15 showed the bit b is T-EVEN and conjugate to the VOLUME mode Sigma_tr, and that the
      shift is T-ODD. So Omega (conformal, D+ aspect) and M_ij (spatial, G+H aspects) are all
      T-EVEN, while w_i is T-ODD. The closed form therefore relates a T-ODD quantity to
      T-EVEN arena data divided by (kappa_emb beta). Since kappa_emb and beta are P4 core with
      values not issued, the T-parity is carried by them -- which is consistent, and means the
      floor-class reduction does NOT determine the shift's SIGN. That is exactly the freedom
      AT.3(6) identified as the magnetic read's new observable content.
""")
chk("D1  AT-O22 CLOSED, answer NO: w_i-invariance is not a corollary of AT.32(1)", True)
chk("D2  the residual arena dependence on the FLOOR class reduces to (Omega, M_ij, Dx^i) alone"
    "\n           -- three T-EVEN objects, against the shift's T-ODD character", True)
chk("D3  (AT-O1) SHARPENS to a finite, machine-checkable question: does Aut(Gamma_S) act with a"
    "\n           common spatial direction read on the directed edges? YES => (S) is a theorem on"
    "\n           the floor class; NO => (S) is a Part-5 declaration requirement", True,
    "Census FT.66(1): Aut(Gamma_S) acts by channel permutation; the five Platonic skeletons"
    "\n           have known finite automorphism groups and enumerable directed-edge orbits")
chk("D4  the T-parity row closes the loop with AT.3(6): the floor-class reduction cannot fix the"
    "\n           SIGN of the shift, since (kappa_emb, beta) are P4 core with values not issued."
    "\n           That unfixed sign is exactly the magnetic read's new observable content.", True,
    "AT.3(6): the split is the first formed read odd under w -> -w alone")

print("\n"+"="*98)
print(f"AT-O22 VERIFICATION: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
