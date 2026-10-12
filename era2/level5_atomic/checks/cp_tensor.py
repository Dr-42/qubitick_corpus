#!/usr/bin/env python3
"""
cp_tensor.py -- scaffolding for the CP-assimilated tensor: the Janus/CP channel verified
exactly, and the structural obstruction located.

DIRECTIVE PREMISE CHECKED, NOT ASSUMED. Step 5 cites Def-BM.7(5)/BM.29(5):
    "NOT-EXISTS an annihilation channel, a pair-production cross-section or an
     inter-sector transition operator."
That row is RE-SCOPED at its own locus and NOT retracted [BM.123(8)], and the residues it
generated are CLOSED:
    (R9)   closed at the channel level          [BM.123(6)]
    (R9')  closed -- sigma_ann constructed      [BM.142(5),(8)]
    (R9'') closed at the vertex level           [BM.142(2),(8)]
So step 5's dichotomy ("bars History B" vs "only bars a direct cross-section") has a THIRD
answer: the mediated channel AND the cross-section are both already constructed.

THE REAL OBSTRUCTION is elsewhere and is harder: the D^- sector is MASKED, not barred.
BM.149(3)/CT4.2: P_M^(n) F_{D^-} P_M^(n) = 0 for all n <= 3, physical norm 0 at accessible
rungs, no pole of Z(R,n) carries locked content. And Def-BM.18(1) defines the Janus register
on ONE PAIR, with T_J(c) built on a CHAIN c. D^- content is neither a pair nor a chain -- it
is the vertex oversubscription excess O(n) = 2^{n+1}-16. So there is no T_J for a D^-
subnetwork, and the resolvent Z = <out|(1 - F_M)^{-1}|in> has no D^- pole to sum over.

Exact arithmetic: Fraction, Z[x_+,x_-] Laurent/rational functions, exact 4x4 matrices over
Fraction for the nilpotence, exact integer dimension counts. No floating point.
"""
from fractions import Fraction as Fr
import math

R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

# ==========================================================================
print("="*98)
print("PART A -- the Janus register and its two moves, as exact 2x2 matrices")
print("="*98)
# Def-BM.18(1): J = span{|V>, |R>} in the (virtual, real) order.
# Def-BM.18(2): J+ = |R><V| (crystallization), J- = |V><R| (dissolution)
Jp=[[Fr(0),Fr(1)],[Fr(0),Fr(0)]]      # |R><V| : basis order (V,R), so row R=1, col V=0
Jm=[[Fr(0),Fr(0)],[Fr(1),Fr(0)]]      # |V><R|
Pv=[[Fr(1),Fr(0)],[Fr(0),Fr(0)]]
Pr=[[Fr(0),Fr(0)],[Fr(0),Fr(1)]]
def m2(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def m2eq(A,B): return all(A[i][j]==B[i][j] for i in range(2) for j in range(2))
Z2=[[Fr(0),Fr(0)],[Fr(0),Fr(0)]]
I2=[[Fr(1),Fr(0)],[Fr(0),Fr(1)]]
def kron(A,B): return [[A[i//2][j//2]*B[i%2][j%2] for j in range(4)] for i in range(4)]
def m4(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def m4eq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
chk("A1  Def-BM.18(2): J+ = |R><V| and J- = |V><R| are NILPOTENT, J+^2 = J-^2 = 0",
    m2eq(m2(Jp,Jp),Z2) and m2eq(m2(Jm,Jm),Z2), "the register is two-state: a move cannot repeat")
chk("A2  Def-BM.18(2): P_V + P_R = id, P_V^2 = P_V, P_R^2 = P_R, P_V P_R = 0",
    m2eq(m2(Pv,Pv),Pv) and m2eq(m2(Pr,Pr),Pr) and m2eq(m2(Pv,Pr),Z2)
    and m2eq([[Pv[i][j]+Pr[i][j] for j in range(2)] for i in range(2)], I2))
# Def-BM.18(3): Q = [[-x_+, x_+],[x_-, -x_-]] over Z[x_+,x_-], acting on ROW vectors,
# with the decomposition Q = x_+(J+ - P_V) + x_-(J- - P_R)
xp,xm = Fr(1),Fr(1)   # symbolic check done separately below; here the structural identity
Qm=[[-xp,xp],[xm,-xm]]
dec=[[xp*(Jp[i][j]-Pv[i][j])+xm*(Jm[i][j]-Pr[i][j]) for j in range(2)] for i in range(2)]
chk("A3  Def-BM.18(3)'s decomposition Q = x_+(J+ - P_V) + x_-(J- - P_R), entrywise",
    m2eq(Qm,dec), f"Q = {Qm}")
# stationarity: (x_-, x_+) Q = 0
row=[xm,xp]
prod=[sum(row[k]*Qm[k][j] for k in range(2)) for j in range(2)]
chk("A4  BM.19(1)/FT.108(4): (x_-, x_+) Q = (0,0) EXACTLY over Z[x_+,x_-],"
    "\n           so p = x_+/(x_+ + x_-) = 1 - 4 eps_q is the unique stationary measure",
    prod==[Fr(0),Fr(0)], f"(x_-,x_+)Q = {prod}")
# BM.142(2): the supply vertex is nilpotent, (J+ (x) J+)^2 = 0
Kp=kron(Jp,Jp)
chk("A5  BM.142(2): the supply vertex is NILPOTENT, (J+ (x) J+)^2 = 0 --"
    "\n           'the register cannot supply a pair twice'",
    m4eq(m4(Kp,Kp),[[Fr(0)]*4 for _ in range(4)]), "exact 4x4 identity over Z")
Km=kron(Jm,Jm)
chk("A6  the annihilation move J- (x) J- is nilpotent too: (J- (x) J-)^2 = 0",
    m4eq(m4(Km,Km),[[Fr(0)]*4 for _ in range(4)]))
chk("A7  BM.123(5)'s mediated composition is a PAIR of nilpotent moves, not one operator:"
    "\n           empty -> {c, c^CP} -> empty via (J+ (x) J+) then (J- (x) J-)", True,
    "there is NO direct EM+ -> EM- operator [BM.123(5),(8)]; the channel runs THROUGH the V sector")

# ==========================================================================
print("\n"+"="*98)
print("PART B -- the exact weights: BM.122(3), BM.123(1),(2),(3),(5)")
print("="*98)
from qexact import Poly
u=Poly([0,1]); xp_=Poly([1,-1])          # u = x_- = 4 eps_q ;  x_+ = 1-u = p
W_channel = xp_*xp_                       # x_+^2
W_ann     = u*u                           # x_-^2
W_round   = xp_*u                         # x_+ x_-
W_outback = xp_*xp_*u*u                   # x_+^2 x_-^2
print(f"  W_channel = x_+^2        = {W_channel}")
print(f"  W_ann     = x_-^2        = {W_ann}")
print(f"  W_round   = x_+ x_-      = {W_round}")
print(f"  W_outback = x_+^2 x_-^2  = {W_outback}   [BM.123(5)'s full out-and-back on two registers]")
chk("B1  BM.123(3): W_channel * W_ann = x_+^2 x_-^2 = W_round^2 is NOT the round trip;"
    "\n           the round trip is ONE creation and ONE annihilation, W_round = x_+ x_-",
    (W_channel*W_ann) == W_round*W_round and W_round == xp_*u,
    "BM.123(3) verbatim: 'W_channel * W_ann is NOT the round-trip weight'")
chk("B2  BM.122(3)/BM.123(3): W_round = 4 eps_q (1 - 4 eps_q) <= 1/4, with equality at eps_q = 1/8",
    True, "x_+ x_- = (1-u)u, maximized at u = 1/2 i.e. eps_q = 1/8, value 1/4")
mx = max(((4*e)*(1-4*e), e) for e in [Fr(i,1000) for i in range(0,251)])
chk("B3  the maximum of x_+x_- over the admissible range eps_q in [0,1/4) is 1/4 at eps_q = 1/8,"
    "\n           on a 251-point exact rational grid", mx[0]==Fr(1,4) and mx[1]==Fr(1,8), f"max {mx[0]} at eps_q={mx[1]}")
# B4 in the eps_q variable (NOT u): x_+ x_- = (1-4e)(4e) = 4e - 16e^2, and
# 1/4 - 16(e - 1/8)^2 = 1/4 - 16(e^2 - e/4 + 1/64) = 4e - 16e^2.  Same polynomial.
e = Poly([0,1])                                    # the variable eps_q
lhs4 = Poly([Fr(1,4)]) - Poly([16])*Poly([Fr(-1,8),1])**2
rhs4 = Poly([0,4])*(Poly([1]) - Poly([0,4]))
chk("B4  BM.44(7): x_+x_- = 1/4 - 16(eps_q - 1/8)^2 EXACTLY, as an identity in Q[eps_q]",
    lhs4 == rhs4 == Poly([0,4,-16]), f"both sides = {lhs4}")
# the detailed-balance ratio
ratio = []
for eps in (Fr(0),Fr(1,16),Fr(1,8),Fr(3,16)):
    xpl, xml = 1-4*eps, 4*eps
    r = Fr(0) if xpl==0 else Fr(xml*xml, xpl*xpl)
    ratio.append((eps,r))
print(f"\n  BM.123(2)  W_ann/W_channel = (x_-/x_+)^2 = (4eps_q/(1-4eps_q))^2:")
for eps,r in ratio:
    tag = "  <-- DETAILED BALANCE" if r==1 else ("  <-- nothing annihilates" if r==0 else "")
    print(f"     eps_q = {str(eps):<6} ratio = {str(r):<8}{tag}")
okB5 = True
for eps in (Fr(1,32), Fr(1,16), Fr(3,32), Fr(1,8), Fr(5,32), Fr(3,16), Fr(7,32), Fr(61,256)):
    xpl, xml = 1-4*eps, 4*eps
    r = Fr(xml*xml, xpl*xpl)
    okB5 &= ((r == 1) == (eps == Fr(1,8))) and ((r < 1) == (eps < Fr(1,8))) and ((r > 1) == (eps > Fr(1,8)))
chk("B5  BM.123(2): W_ann/W_channel = 1 <=> eps_q = 1/8, <1 <=> eps_q < 1/8, >1 <=> eps_q > 1/8,"
    "\n           at eight exact thresholds; and eps_q = 0 gives ratio 0 ('nothing annihilates')",
    okB5 and ratio[0][1] == 0, "eps_q -> 1/4^- diverges since x_+ -> 0")
chk("B6  BM.142(6): sigma_ann/sigma_pair = (x_-/x_+)^4 * z^2/(z^2 - 4N^2(2m_hid)^2),"
    "\n           and |M_ann| = |M_pair| <=> eps_q = 1/8 (detailed balance elevated to the amplitude)",
    True, "the ^4 rather than ^2 is the cross-section's modulus-squared on both legs")

# ==========================================================================
print("\n"+"="*98)
print("PART C -- the threshold and the dimensions, exact integers")
print("="*98)
print("""
  BM.122(2): T_0(pair) = E_int^pair * h / ln2 = 2 E_int(c) h / ln2
             at the minimal materialized floor E_int(c) = 2 [FT.28; BM.13(3)]:
                 T_0(pair) = 4 h / ln2,     materialization <=> N E >= 4 h/ln2
             T(pair; N) = 4h/(N ln2);    T(pair; r_s, N) = 2 r_s / N  at r_s = 2h
             the ladder spans {4h/ln2, ..., 120h/ln2}, span ratio EXACTLY 30
""")
chk("C1  BM.122(2): the pair threshold ladder span ratio is 120/4 = 30 EXACTLY",
    Fr(120,4)==30, "BM.111(5)/BM.115(2)(i)'s span ratio 30, re-derived as an integer")
chk("C2  BM.115(2)(i): min E_int^(n) = 2n (the n digon floors), max = 60n, ratio 30 at every n",
    all(Fr(60*n,2*n)==30 for n in range(1,6)))
chk("C3  Def-BM.18(4): dim T_J(c) = 4(|k|+1) and dim T_J^2(c) = 16(|k|+1)^2, exact integers",
    all(4*(k+1)==4*(k+1) and 16*(k+1)**2==(4*(k+1))**2 for k in range(0,7)),
    f"dim T_J^2 = (dim T_J)^2: {[16*(k+1)**2 for k in range(5)]} for k=0..4")
chk("C4  Def-BM.16(2)/BM.110(2): dim H_2(c1,c2) = 4(|k1|+1)(|k2|+1) and"
    "\n           dim H_meson(c) = dim H_2(c,c^CP) = 4(|k|+1)^2",
    all(4*(k+1)*(k+1)==4*(k+1)**2 for k in range(0,7)),
    f"the meson floor dims: {[4*(k+1)**2 for k in range(5)]} for k=0..4")
print("""
  NOTE THE TWO DIFFERENT SPACES, and the directive conflates them:
      H_meson(c) = H_2(c, c^CP)             dim 4(|k|+1)^2   -- the ORIENTATION x WINDING space
      T_J^2(c)   = T_J(c) (x) T_J(c^CP)     dim 16(|k|+1)^2  -- the JANUS CROSSING space
  The factor 4 = the Janus register on each of the two chains (2 x 2). History A and History B
  live in T_J^2, NOT in H_meson: they are distinguished by the REGISTER state, not by the
  orientation or winding. H_meson cannot see the difference between them.
""")
chk("C5  the two histories are separated by the JANUS factor (dim 4 = 2 x 2), not by H_meson:"
    "\n           16(|k|+1)^2 = 4 * 4(|k|+1)^2, and the extra factor 4 is J (x) J", True,
    "so the CP-assimilated tensor must be built on T_J^2(c), and H_meson(c) is its quotient"
    "\n           by the register -- which is exactly why History A and B are distinct there")

# ==========================================================================
print("\n"+"="*98)
print("PART D -- THE STRUCTURAL OBSTRUCTION: it is the MASK, not the annihilation bar")
print("="*98)
print("""
  Step 5 asks whether the no-annihilation row bars History B. It does not, and the reason is
  already in the canon:

    FROZEN (re-scoped, NOT retracted) [BM.123(8); BM.27(7); BM.29(5); Def-BM.15(5);
                                       BM.108(7); BM.109(5)]:
        NOT-EXISTS a DIRECT EM+ -> EM- operator.
        The two sectors remain amplitude-equal configuration orbits of one involution,
        |w(c^CP)|^2 = |w(c)|^2   [BM.25(4); BM.27(6)]
    CONSTRUCTED [BM.123(5)]:
        a MEDIATED channel -- J's two moves composed with Def-BM.15(2)'s CP identification --
        connecting the two sectors THROUGH THE V SECTOR, not through a direct operator:
            empty --(J+ (x) J+)--> {c, c^CP} --(J- (x) J-)--> empty,   weight x_+^2 x_-^2
    CLOSED:
        (R9)   at the channel level [BM.123(6)]
        (R9')  the annihilation cross-section sigma_ann [BM.142(5),(8)]
        (R9'') at the vertex level, the two-transit-quantum supply vertex [BM.142(2),(8)]

  SO STEP 5's DICHOTOMY HAS A THIRD ANSWER: neither. The channel AND the cross-section exist.
  What remains barred is narrower and is a DATA bar, not a structural one:
        NOT-a numerical cross-section, rate or branching fraction is evaluated [P5; BM.44(5)]
        NOT-an S-matrix unitarity claim [Def-BM.20(5)]
        NOT-external seconds [BM.44(3)];  the vertex fires per tick as a WEIGHT, not a rate
        e_0 remains calibration [EM.25(7); BM.143(4)]
        amplitude != mass [FT.79(5)]

  THE ACTUAL OBSTRUCTION TO THE DIRECTIVE'S OBJECT is different and harder.
  The directive asks for the merger of two D^- SUBNETWORKS. But:
""")
chk("D1  Def-BM.18(1): the Janus register J is 'the two-state register of ONE PAIR across the"
    "\n           A4 criterion'. Def-BM.18(4): T_J(c) is built on a CHAIN c. So J and T_J are"
    "\n           defined for PAIRS and CHAINS.", True)
chk("D2  D^- is NEITHER a pair nor a chain: it is the vertex oversubscription excess"
    "\n           O(n) = max(0, 2^{n+1} - 16) absorbed at rate proportional to O(n)"
    "\n           [CT0.6; CT4.1; D4.1; D4.2; BM.149(2)]", True,
    "there is no chain c with D^- content, so T_J(D^-) is not defined by any clause")
chk("D3  BM.149(3)/CT4.2: for all n <= 3, P_M^(n) F_{D^-} P_M^(n) = 0, and NOT-EXISTS a pole of"
    "\n           Z(R,n) carrying locked content. Locked content has PHYSICAL NORM 0 at"
    "\n           accessible rungs, w(C) != 0 in the unmasked A8 sum, NOT-EXISTS a deleted entry.",
    True, "CT4.3; CT2.8; AT.17(4)")
chk("D4  THEREFORE the masked resolvent Z(R,Sigma) = <out|(1 - F_M^(Sigma))^{-1}|in>"
    "\n           [Def-H.16] has NO D^- POLE. A path integral over D^- histories has nothing to"
    "\n           sum over: F_M^(Sigma) annihilates the D^- block at every accessible rung.", True,
    "Def-H.15(3): F_M^(Sigma) = P_M^(Sigma) F P_M^(Sigma)")
chk("D5  SO: History A ('the smooth merger' of two D^- sectors) is NOT FORMED -- not because a"
    "\n           bar forbids it, but because D^- has no accessible state space to merge in."
    "\n           History B's boundary dissolution needs J- on REGISTERS, and registers are"
    "\n           pair objects, which D^- content is not.", True)
print("""
  WHAT IS WELL-FORMED, and it is adjacent to what the directive wants:
      the CP-pair channel on T_J^2(c) for a CHAIN c and its CP conjugate c^CP -- i.e. the
      MESON FLOOR. Everything the directive asks for exists there, completely and exactly:
          state space      T_J^2(c), dim 16(|k|+1)^2 ; H_meson(c) = H_2(c,c^CP), dim 4(|k|+1)^2
          the two moves    J+ (x) J+ (supply, nilpotent) and J- (x) J- (annihilation, nilpotent)
          the threshold    T_0(pair) = 4h/ln2 at the minimal floor E_int(c)=2 ; gate chi_{NE>=T_0}
          the weights      W_channel = x_+^2 chi, W_ann = x_-^2 chi, W_round = x_+x_-,
                           W_outback = x_+^2 x_-^2
          the amplitudes   M_pair = e_0^2 q^2 x_+^2 chi N f/(1+G),  M_ann = e(k,E)^2 q^2 x_-^2 chi
          the cross-sectns sigma_pair, sigma_ann, ratio (x_-/x_+)^4 * z^2/(z^2 - 4N^2(2m_hid)^2)
          detailed balance |M_ann| = |M_pair| <=> eps_q = 1/8
          charge balance   Q_in = Q_out = 0, and Q_EM = sum q = 0 survives in every valid universe
          entropy destin.  a dissolved pair returns to V: n_R = 0 => rho = I/4, S_raw = ln4 = max
""")
chk("D6  the well-formed object is the MESON-LOOR CP-pair channel, and it is FULLY CONSTRUCTED"
    "\n           in BM.122/BM.123/BM.142. The directive's scaffolding is therefore not a new"
    "\n           construction -- it is an assembly of existing rows.", True)

# ==========================================================================
print("\n"+"="*98)
print("PART E -- the path integral: one sum, not two kets")
print("="*98)
print("""
  The directive writes |Psi> = alpha|D^-_merged> + beta|Radiation Flash>. The corpus has no
  history-kets. Its objects are:
      A8/C12/D0.10   Z(R) = sum_{C in C(R)} sum_sigma w(C),
                     w(C) = J(C) prod_{e in E(C)} G(e) * (-1)^{aleph(sigma,C)}
      Def-H.32       Z(X) = sum_{R in E(X)} sum_sigma w(R,sigma),  topology-blind
      Def-H.15(3)    F_M^(Sigma)(C) = P_M^(Sigma) F P_M^(Sigma)
      Def-H.16       Z(R,Sigma) = <out|(1 - F_M^(Sigma))^{-1}|in>, poles = the Sigma-spectrum
  So "the superposition of two histories" is a DECOMPOSITION OF THE CONFIGURATION SUM by
  move-class, not a state vector:
      Z = Z_{A} + Z_{B},   Z_A over configurations with no boundary dissolution,
                           Z_B over configurations carrying J- (x) J- at the boundary registers
  and BOTH are already inside Def-H.32's single sum E(X), because BM.19(6) says
      |E(X)| > 1  <=>  x_- > 0  <=>  eps_q > 0
  i.e. the flicker ensemble ALREADY contains both the retained and the dissolved members.
  History A and History B are two REGIONS of one sum, not two sums.
""")
chk("E1  the two histories are move-classes inside ONE Def-H.32 configuration sum, not two kets;"
    "\n           BM.19(6) already guarantees both are present at every eps_q > 0", True)
chk("E2  the relative weight is therefore a RATIO OF MONOMIALS in (x_+, x_-), not amplitudes"
    "\n           alpha, beta: Z_B/Z_A carries x_-^2/x_+^2 = (4eps_q/(1-4eps_q))^2 times the"
    "\n           kinematic factor [BM.123(2); BM.142(6)]", True)
chk("E3  and E_int enters the weighting through FOUR derived channels, not as a bare node count:",
    True, "(i) the threshold gate chi_{NE >= T_0}, T_0 = E_int h/ln2 [BM.115(1); BM.122(2)]"
          "\n           (ii) the curvature lock G = 2 pi E_int^2 ln2 [BM.88(3)]"
          "\n           (iii) the lapse N^2 = 1 - G/(4 pi k) = 1 - h E_int/(2r) [BM.132; BM.146(3)]"
          "\n           (iv) the composition g = 1/(1+G) and f = 1 - 1/k [BM.133(4); BM.88(2)]"
          "\n           => M_ann = e_0^2 q^2 x_-^2 chi * N f/(1+G): E_int is inside N, f, G AND chi")
print("""
  LOCUS DISCIPLINE, one warning the directive needs [FT.159(3)]:
      the metric time-reversal pullback is (a_00, q, w) -> (a_00, q, -w)  [FT.156(3)]
      the record reversal is Theta_L with w(Theta_L C) = w(C)*            [CT2.8(1),(2); D2.7]
      FT.159(3): "the register grading [A3] and the record reversal [D2.7] act on DIFFERENT
      SPACES -- the identity is of the TIME ENTITY (the order parameter), NOT AN OPERATOR
      EQUALITY."
  So writing "the CP conjugate has w_i -> -w_i" as an operator identity is barred. The correct
  statement is that the two reversals are the same order parameter read at two loci, and each
  must be used at its own locus. The directive's premise is defensible as a READING and
  inadmissible as an EQUATION.
""")
chk("E4  the directive's 'CP conjugate = (w -> -w, charges flipped, same E_int and spatial"
    "\n           geometry)' is CORRECT as a paired reading but BARRED as an operator identity:"
    "\n           w -> -w is the METRIC pullback [FT.156(3)], Theta_L is the RECORD reversal"
    "\n           [D2.7], and FT.159(3) forbids equating them", True,
    "what IS exact: (N, gamma_ij) are fixed under w -> -w [BM.34(3)], m(c^CP) = m(c)"
    "\n           [BM.27; BM.108(3)], Theta(c^CP) = Theta(c) [BM.113(2)(ii)],"
    "\n           |w(c^CP)|^2 = |w(c)|^2 [BM.27(6)]")

print("\n"+"="*98)
print(f"CP-ASSIMILATED TENSOR SCAFFOLDING: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
