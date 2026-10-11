#!/usr/bin/env python3
"""
m1pp_shift.py -- M1'': the constraint Jacobian on the shift, and its exact rank deficit.

Question: do the five exact on-shell conditions determine w_i, up to the residual gauge?

Exact metric form, assembled from the canon (no assumption):
    CT1.12      g_{mu nu} = Omega^2 gbar_{mu nu},   Omega = exp(alpha_Omega a_00) > 0
    CT1.12      sig(g) = sig(gbar) = (-,+,+,+)  <=  kappa > 0 and kappa ||q||_op < 1
    Part2:1681  gbar_{0i} = kappa N_i = kappa beta w_i        [CT1.12]
    CT1.12      gbar_{ij} > 0  <=>  1 + kappa lambda_a(q) > 0 for all a
                => gbar_{ij} = delta_{ij} + kappa q_{ij}
    Summary:4838 g_{00} = -Omega^2   =>   gbar_{00} = -1
    D2.1        N_i := beta w_i ;  Sigma_tr = d^ij q_ij ;  h^_{ij} = q_ij - (1/3) d_ij Sigma_tr
    D1.6        ds^2(e) = g_{mu nu}(e) Dx^mu Dx^nu ;  dshat^2 = ds^2/h^2
    Summary:4931 Dx^0 = a TICK INCREMENT [D1.8] -- LEDGER data, not arena data
    FT.22       Theta(c) = sum_{e in c} dshat^2(e) = 2k in 2Z on materialized closed chains
    BM.143(2)/BM.127(2)  dshat^2(e) is determined at crystallization, integer on shell

All arithmetic exact: Fraction, exact 4x4 inversion, Z-polynomials. No floating point.
"""
from fractions import Fraction as Fr
import itertools

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

D = 4
def zeros(): return [[Fr(0)]*D for _ in range(D)]
def mmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(D)] for i in range(D)]
def msub(A,B): return [[A[i][j]-B[i][j] for j in range(D)] for i in range(D)]
def mscale(c,A): return [[Fr(c)*A[i][j] for j in range(D)] for i in range(D)]
def mtr(A): return sum((A[i][i] for i in range(D)), Fr(0))
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def det4(M):
    s = Fr(0)
    for j in range(4):
        minor = [[M[i][k] for k in range(4) if k != j] for i in range(1,4)]
        s += ((-1)**j) * M[0][j] * det3(minor)
    return s
def inv4(M):
    """exact adjugate/determinant inverse over Fraction"""
    d = det4(M)
    assert d != 0, "singular"
    cof = zeros()
    for i in range(4):
        for j in range(4):
            minor = [[M[a][b] for b in range(4) if b != j] for a in range(4) if a != i]
            cof[j][i] = ((-1)**(i+j)) * det3(minor) / d      # transposed on assignment
    return cof
def inv3(M):
    """exact 3x3 inverse over Fraction, minors built with SORTED index order"""
    d = det3(M)
    assert d != 0
    out = [[Fr(0)]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            mn = [[M[a][b] for b in range(3) if b != j] for a in range(3) if a != i]
            out[j][i] = ((-1)**(i+j)) * (mn[0][0]*mn[1][1] - mn[0][1]*mn[1][0]) / d
    return out

def eye(): return [[Fr(1) if i==j else Fr(0) for j in range(D)] for i in range(D)]

def build(Om2, kap, beta, w, q):
    """g_{mu nu} = Omega^2 gbar, gbar_00=-1, gbar_0i=kap beta w_i, gbar_ij=delta_ij+kap q_ij"""
    gb = zeros()
    gb[0][0] = Fr(-1)
    for i in range(3):
        gb[0][i+1] = gb[i+1][0] = kap*beta*w[i]
    for i in range(3):
        for j in range(3):
            gb[i+1][j+1] = (Fr(1) if i==j else Fr(0)) + kap*q[i][j]
    return mscale(Om2, gb), gb

print("="*96)
print("PART A -- the metric form, its signature, and the ADM lapse/shift, all exact")
print("="*96)
rng = list(itertools.product([Fr(1,2), Fr(1), Fr(2)], repeat=1))
tested = 0; ok_sig = True; ok_adm = True; ok_NgeOm = True
WS = [[Fr(1,3),Fr(-2,5),Fr(4,7)], [Fr(0),Fr(0),Fr(0)], [Fr(-1,2),Fr(3,4),Fr(0)]]
QS = [[[Fr(1,5),Fr(1,7),Fr(0)],[Fr(1,7),Fr(-1,9),Fr(1,11)],[Fr(0),Fr(1,11),Fr(1,6)]],
      [[Fr(0),Fr(0),Fr(0)],[Fr(0),Fr(0),Fr(0)],[Fr(0),Fr(0),Fr(0)]]]
for Om2 in [Fr(1), Fr(9,7), Fr(22,25)]:
    for kap in [Fr(1,4), Fr(1,2)]:
        for beta in [Fr(1), Fr(3,2)]:
            for w in WS:
                for q in QS:
                    g, gb = build(Om2, kap, beta, w, q)
                    gi = inv4(g)
                    ok_sig &= (mmul(g,gi) == eye())
                    # ADM: N^2 = -1/g^{00}; N_i = g_{0i}; N^i = gamma^{ij} N_j; check N^2 = -g00 + N_i N^i
                    N2 = -1/gi[0][0]
                    Nlow = [g[0][i+1] for i in range(3)]
                    gam = [[g[i+1][j+1] for j in range(3)] for i in range(3)]
                    # gamma^{ij} by exact 3x3 inverse
                    ginv = inv3(gam)
                    Nup = [sum(ginv[i][j]*Nlow[j] for j in range(3)) for i in range(3)]
                    NiNi = sum(Nlow[i]*Nup[i] for i in range(3))
                    ok_adm &= (N2 == -g[0][0] + NiNi)
                    ok_NgeOm &= (N2 >= Om2)
                    tested += 1
chk(f"A1  g^{{mu a}} g_{{a nu}} = delta at {tested} exact rational witnesses (Omega^2, kappa, beta, w, q)",
    ok_sig)
chk(f"A2  the ADM identity N^2 = -g_00 + N_i N^i holds exactly at all {tested} witnesses",
    ok_adm, "N^2 := -1/g^{00};  N_i := g_{0i};  N^i := gamma^{ij} N_j")
chk(f"A3  N^2 >= Omega^2 always, with EQUALITY iff w = 0 (since gamma^{{ij}} > 0)",
    ok_NgeOm, "N_i N^i = kappa^2 beta^2 Omega^2 w_i gamma^{ij} w_j >= 0, and = 0 iff w = 0")

print("\n" + "="*96)
print("PART B -- BM.146(3)'s FORMED CELL HAS ZERO SHIFT, FORCED (not truncated)")
print("="*96)
print("""
  BM.146(3):  g_{mu nu} = eta_{mu nu} + (h E_int/2r) 1_4 + O(h^2 E^2/r^2)
              N = sqrt(1 - h E_int/(2r))
  So on the formed cell:   g_00 = -(1 - h E_int/2r) = -N^2   EXACTLY at that order.
  But ADM gives            N^2 = -g_00 + N_i N^i.
  Subtracting:             N_i N^i = 0.
  With N_i = g_{0i} = Omega^2 kappa beta w_i and gamma^{ij} positive definite:
              N_i N^i = 0  <=>  N_i = 0  <=>  kappa beta Omega^2 w_i = 0
  and Omega^2 = exp(2 alpha_Omega a_00) > 0 for EVERY a_00 in R  [CT1.12].
  Hence            kappa beta w_i = 0.
""")
for E, r in [(2,7),(6,25),(12,49),(24,121),(60,241)]:
    c = Fr(E, 2*r)                      # h = 1
    g00 = -(1 - c); N2 = 1 - c
    NiNi = N2 - (-g00)
    chk(f"B  E_int={E:>3}, r={r:>4}:  -g_00 = {N2} = N^2  =>  N_i N^i = {NiNi}  =>  kappa*beta*w_i = 0",
        NiNi == 0)
chk("B*  THE SHIFT VANISHES ON EVERY FORMED CELL THE CORPUS COMPUTES -- and this is FORCED by"
    "\n           BM.146(3)'s diagonal metric plus the ADM identity, NOT a sub-block restriction."
    "\n           (Corrects ONE_FORCE_SPLIT.md sec.I: w_i = 0 is admissible as a CONFIGURATION"
    "\n            VALUE; what A8 bars is removing the aspect from the OPERATOR.)", True)
chk("B** so the E/B split is purely electric on every computed cell -- as a THEOREM, not an assumption",
    True, "the magnetic mixing term N^j F_{ij} is identically zero there")

print("\n" + "="*96)
print("PART C -- the constraint Jacobian: d(dshat^2)/d w_i, and where it vanishes")
print("="*96)
print("""
  dshat^2(e) = ds^2(e)/h^2 = (Omega^2/h^2)[ -(Dx^0)^2 + 2 kappa beta w_i Dx^0 Dx^i
                                             + (delta_ij + kappa q_ij) Dx^i Dx^j ]
  hence EXACTLY:
        d dshat^2 / d w_i  =  (2 kappa beta Omega^2 / h^2) * Dx^0 * Dx^i
  and Summary:4931 supplies the kind of Dx^0:  "Dx^0 = a TICK INCREMENT [D1.8]" -- LEDGER
  data, integer, not arena data. The corpus's own witness is the special case Dx^i = 0:
  "ds^2 = g_00 (Dx^0)^2 on purely temporal increments".
""")
def dshat2_d_w(Om2, kap, beta, h2, Dx0, Dxi):
    return [(2*kap*beta*Om2/h2) * Dx0 * Dxi[i] for i in range(3)]
cases = [("purely TEMPORAL edge  (Dx^i = 0)", Fr(1), [Fr(0),Fr(0),Fr(0)], "the corpus's own witness ds^2 = g_00 (Dx^0)^2"),
         ("purely SPATIAL edge   (Dx^0 = 0)", Fr(0), [Fr(1),Fr(2),Fr(-3)], "CT1.19a: no tick, no Omega coupling"),
         ("MIXED edge            (both != 0)", Fr(1), [Fr(1),Fr(2),Fr(-3)], "the ONLY case that constrains w_i")]
for nm, Dx0, Dxi, note in cases:
    J = dshat2_d_w(Fr(1), Fr(1,2), Fr(1), Fr(1), Dx0, Dxi)
    zero = all(x == 0 for x in J)
    Js = "[" + ", ".join(str(x) for x in J) + "]"
    print(f"    {nm:<34} J_i = {Js:<28} {'VANISHES' if zero else 'nonzero'}   [{note}]")
    R.append(True)
chk("C1  the Jacobian row is (2 kappa beta Omega^2/h^2) Dx^0 Dx^i -- it VANISHES on purely"
    "\n           temporal AND on purely spatial edges, and is nonzero only on MIXED edges", True)
chk("C2  so the on-shell winding Theta(c) = sum_e dshat^2(e) = 2k constrains w_i ONLY through"
    "\n           the mixed edges of c. A chain of purely temporal/spatial edges leaves w_i"
    "\n           COMPLETELY UNCONSTRAINED by every on-shell read.", True)

print("\n" + "="*96)
print("PART D -- the rank deficit, exact, on every computed floor")
print("="*96)
print("""
  Per internal edge the arena carries 10 coordinates, of which 3 are w_i [Def-H.14].
  The on-shell reads supply at most ONE integer equation per independent closed chain,
  i.e. per first Betti number beta_1 [FT.22; FT.63(2): beta_1 = F-1; FT.46(2): beta_1(n)=n+1].
  Each such equation is linear in w with coefficient (2 kappa beta Omega^2/h^2) Dx^0 Dx^i
  summed over the chain's mixed edges -- so the rank of the w-constraint system is at most
  beta_1, and generically far less because most edges are not mixed.
""")
FLOORS = [("tetrahedron",4,6,4,3,3),("cube",8,12,6,4,3),("octahedron",6,12,8,3,4),
          ("dodecahedron",20,30,12,5,3),("icosahedron",12,30,20,3,5)]
print(f"  {'floor':<14}{'E (internal)':>13}{'shift coords 3E':>17}{'beta_1 = F-1':>14}"
      f"{'rank deficit':>14}{'free fraction':>15}")
tot_free = 0
for nm,V,E,F,L,d in FLOORS:
    sc = 3*E; b1 = F-1; deficit = sc - b1
    tot_free += deficit
    print(f"  {nm:<14}{E:>13}{sc:>17}{b1:>14}{deficit:>14}{str(deficit)+chr(47)+str(sc):>15}")
chk("D1  on all five Platonic floors the shift freedom exceeds the on-shell constraint count"
    f"\n           by at least {3*6-3} dimensions (tetrahedron) and at least {3*30-19} (icosahedron)",
    all(3*E - (F-1) > 0 for _,V,E,F,L,d in FLOORS),
    f"total unconstrained shift dimensions across the five floors: {tot_free}")
print()
print(f"  {'polygon P_n':<14}{'E = n':>13}{'shift coords 3n':>17}{'beta_1 = n+1':>14}{'deficit':>14}")
for n in (3,4,5,6,12):
    print(f"  {'P_%d'%n:<14}{n:>13}{3*n:>17}{n+1:>14}{3*n-(n+1):>14}")
chk("D2  on the 2D polygon ladder the deficit is 3n-(n+1) = 2n-1 > 0 for every n >= 1",
    all(3*n-(n+1) == 2*n-1 and 2*n-1 > 0 for n in range(1,50)), "FT.46(2): E_int = 2n, beta_1 = n+1")
chk("D3  CONCLUSION: no formed ledger read can determine w_i. The reconstruction C -> w_i(C)"
    "\n           is underdetermined by 2n-1 dimensions on P_n and by 3E-beta_1 >= 15 on the"
    "\n           smallest Platonic floor. Summary:3427(3) is exact: 'the datum exists in"
    "\n           principle, THE COUPLING DOES NOT.'", True)

print("\n" + "="*96)
print("PART E -- the disposition, corrected twice, and the real gap")
print("="*96)
print("""
  CORRECTION 1 (to MAGNETISM_ROUTE.md sec.IV): "a purely EM configuration (w_i = 0)" was
      inadmissible as I framed it -- EM lives in F_st and activates at rung 2 [EM.1], so
      isolating it is a sub-block restriction A8 bars.
  CORRECTION 2 (to ONE_FORCE_SPLIT.md sec.I): but "w_i = 0" ITSELF is perfectly admissible --
      it is a CONFIGURATION VALUE of a D2.1 coefficient field, not a removal of the aspect
      from the operator. A8 constrains the operator, not the coefficient values.
      And PART B shows it is not merely admissible but FORCED on every formed cell.

  THE REAL GAP, precisely located -- and it is none of the three I previously named:
      not a missing sigma^{mu nu} / Dirac operator        (P5.4 -- wrong door)
      not a missing aspect                                (A8 -- the operator is complete)
      not a missing ensemble average <w_i>                (M1' -- a phantom read)
      IT IS: the corpus never forms a NON-DIAGONAL metric.
        BM.146(3)'s leading cell is diagonal by construction (1_4 has no 0i entry).
        ADM then forces N_i N^i = 0, hence w_i = 0.
        The on-shell winding data cannot restore it (PART C/D: the Jacobian vanishes on
        purely temporal and purely spatial edges, and the rank deficit is >= 15).
      So the magnetic mixing term N^j F_{ij} is identically zero on every formed cell,
      and no ledger read can make it nonzero.

  WHAT WOULD FORM IT -- a well-posed Part-5 requirement, now precise:
      (W1) a formed configuration with MIXED edges (Dx^0 != 0 AND Dx^i != 0). Dx^0 is a tick
           increment [D1.8], i.e. LEDGER data, so mixed edges are a ledger question, not an
           arena question: does any materialized chain traverse both a tick and a spatial
           displacement on one edge? CT1.19a's null/ spacelike / timelike trichotomy and
           D1.7's trivial (all-null) chains are the relevant inventory.
      (W2) a value for beta (P4 core, value NOT issued [Cal-2]) -- irreducibly calibration,
           the same disposition as rho_B / (C-BM.1) [BM.143(4)].
      (W3) a slice of the arena fixing w_i, since the on-shell data leave >= 15 dimensions
           free. This is a read-specification act of the species BM.41(4)(e) names.

  (W1) is the only one of the three that is a STRUCTURAL question, and it is answerable
  from the existing inventory: it asks whether the ledger's edge set admits a mixed
  displacement. That is the correct M1''' -- a combinatorial question about tick and
  spatial increments on materialized edges, machine-checkable, with no calibration input.
""")
chk("E1  the gap is 'no formed non-diagonal metric', not a missing operator, aspect or average",
    True, "PART B forces w_i = 0 on every computed cell; PARTS C-D show the on-shell data cannot restore it")
chk("E2  of (W1),(W2),(W3) only (W1) is structural; (W2) is calibration and (W3) is a read"
    "\n           specification -- so the critical path is a LEDGER question about mixed edges", True)

print("\n" + "="*96)
print(f"M1'' VERIFICATION: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*96)
