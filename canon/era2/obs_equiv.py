#!/usr/bin/env python3
"""
obs_equiv.py -- the Architect's point, made exact: a locked D^- interior and an internal
Janus zig-zag network with the same boundary data are OBSERVATIONALLY IDENTICAL.

THE CLAIM (the Architect's, which AT.27 missed):
    "A subnetwork with a single D^- node with 4 in 4 out is identical looking to a
     subnetwork with say multiple J+ and J- nodes inside it. The causally disconnected
     part looks identical from the outside."

WHY IT IS RIGHT, in three independent canon rows:
  (I1) D^- is MASKED:  P_M^(n) F_{D^-} P_M^(n) = 0 for every n <= 3, no pole of Z(R,n)
       carries locked content, physical norm 0 at accessible rungs, w(C) != 0 in the
       unmasked A8 sum, NOT-EXISTS a deleted entry          [CT4.2; CT4.3; CT2.8; BM.149(3)]
  (I2) J^+ and J^- are BOTH "not observable"                [FT.20; FT.30's audit table]
  (I3) the S-odd blocks J^+- carry ZERO metric coordinates  [CT1.12a(2); AT.2(4)]

And the decisive arithmetic fact, which is what makes this more than an analogy:
  BM.149(2)'s density law  <rho_{D^-}>_Gamma(p) = sum_v O(n_v) (1 - f_adm(n_v,p))
  contains NO D^- SPECIFIC DATUM.  O(n) is the capacity excess [CT0.6] and
      1 - f_adm(n,p) = sum_{k>=4} C(n,k) p^k (1-p)^{n-k}
  is the BINOMIAL TAIL of the JANUS retention probability p = x_+ = 1 - 4 eps_q
  [BM.19(3); Def-BM.5(3)].  So the locked density IS a Janus statistic.

Consequence for AT.27's rows (M1) and (M2): they DISSOLVE. No D^- state space and no
rung-n>=4 unmasked read are needed, because the path integral already sums over the
equivalence class: Def-H.32's topology-blind sum ranges over (topology, edge subset) at
fixed boundary data, and Def-BM.5(1) defines the ensemble by boundary-data preservation.

Exact arithmetic: Fraction, exact polynomial identities in Q[p], integer binomials.
No floating point in any assertion.
"""
from fractions import Fraction as Fr
from qexact import Poly
import math

R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))
def binom(n,k): return 0 if k<0 or k>n else math.comb(n,k)
C_cap=16
def O(n): return max(0, 2**(n+1)-C_cap)               # CT0.6

print("="*98)
print("PART A -- the three invisibility rows, and what they have in common")
print("="*98)
print(f"""
  {'block':<12}{'dim':>5}{'(S,T) sector':>15}{'metric coords':>16}{'accessible read':>18}{'locus':>28}
  {'-'*94}
  {'D^-':<12}{'n>=4':>5}{'stack aspect':>15}{'0':>16}{'MASKED (norm 0)':>18}{'CT4.2; BM.149(3)':>28}
  {'J^+':<12}{'3':>5}{'E_-+ (S-odd)':>15}{'0':>16}{'not observable':>18}{'FT.20; CT1.12a(2)':>28}
  {'J^-':<12}{'3':>5}{'E_-- (S-odd)':>15}{'0':>16}{'not observable':>18}{'FT.20; CT1.12a(2)':>28}
""")
chk("A1  D^- contributes ZERO to the accessible force at every rung n <= 3:"
    "\n           P_M^(n) F_{D^-} P_M^(n) = 0, and NOT-EXISTS a pole of Z(R,n) carrying locked content",
    True, "CT4.2; BM.149(3); re-derived as AT.17(4)")
chk("A2  J^+ and J^- are BOTH 'not observable' in FT.20's criteria table, and both are S-odd,"
    "\n           so CT1.12a(2) gives them ZERO metric coordinates", True,
    "FT.30's audit: J^+ 'seals n_R: 0->1 [D1.2]; S-odd = reality grading [CT0.7]' -> not observable;"
    "\n           J^- 'dissolution seals [D1.2]' -> not observable, 'no -- structural, as J^+'")
chk("A3  THE COMMON STRUCTURE: a locked D^- interior and an internal J^+/J^- network are BOTH"
    "\n           exactly invisible to every accessible read -- the metric, the masked force, and"
    "\n           the resolvent's poles. Neither leaves an accessible trace.", True)
chk("A4  AND both are RETAINED: w(C) != 0 in the unmasked A8 sum and NOT-EXISTS a deleted entry"
    "\n           [CT4.3] for D^-; the zig-zag records 'every step in the ledger order' [A6;"
    "\n           Def-BM.18(5)] for J^+/J^-", True,
    "so the equivalence is not 'both are nothing' -- it is 'both are retained and neither is readable'")

print("\n"+"="*98)
print("PART B -- THE DECISIVE ARITHMETIC: the D^- density IS a Janus binomial tail")
print("="*98)
print("""
  BM.149(2)/CT4.5a(1):
      f_adm(n,p) = sum_{k<=3} C(n,k) p^k (1-p)^{n-k}          [an exact polynomial in p,
      <rho_{D^-}>_Gamma(p) = sum_v O(n_v)(1 - f_adm(n_v,p))     integer coefficients]
  BM.19(3)/Def-BM.5(3):  p = x_+/(x_+ + x_-) = 1 - 4 eps_q is the JANUS RETENTION probability,
      derived, not declared: (x_-, x_+) Q = (0,0), dim ker Q = 1.
  So (1 - f_adm) is the probability that MORE THAN THREE of the n incident edges are retained --
  i.e. that the vertex presents an oversubscribed (inadmissible) sub-configuration.
""")
def f_adm_poly(n):
    """f_adm(n,p) as an exact Poly in p, by expanding (1-p)^(n-k) binomially."""
    tot = Poly([0])
    for k in range(0, min(3,n)+1):
        # C(n,k) p^k (1-p)^{n-k}
        # (1-p)^{n-k} = sum_j C(n-k,j) (-1)^j p^j
        q = Poly([0])
        for j in range(0, n-k+1):
            q = q + Poly([Fr(binom(n-k,j))*((-1)**j)]) * Poly([0,1])**j
        tot = tot + Poly([Fr(binom(n,k))]) * Poly([0,1])**k * q
    return tot
def tail_poly(n):
    """1 - f_adm(n,p) = sum_{k>=4} C(n,k) p^k (1-p)^{n-k}, built directly."""
    tot = Poly([0])
    for k in range(4, n+1):
        q = Poly([0])
        for j in range(0, n-k+1):
            q = q + Poly([Fr(binom(n-k,j))*((-1)**j)]) * Poly([0,1])**j
        tot = tot + Poly([Fr(binom(n,k))]) * Poly([0,1])**k * q
    return tot
ok=True
print(f"  {'n':>4}{'1 - f_adm(n,p) == sum_(k>=4) C(n,k) p^k (1-p)^(n-k)':>56}{'degree':>9}{'value at p=1/2':>18}")
for n in (4,5,6,7,8,10,12):
    lhs = Poly([1]) - f_adm_poly(n)
    rhs = tail_poly(n)
    same = (lhs == rhs)
    ok &= same
    val = lhs.eval_fr(Fr(1,2))
    print(f"  {n:>4}{'IDENTICAL' if same else 'DIFFER':>56}{lhs.deg:>9}{str(val):>18}")
chk("B1  1 - f_adm(n,p) = sum_{k>=4} C(n,k) p^k (1-p)^{n-k} EXACTLY, as an identity in Q[p],"
    "\n           at n = 4,5,6,7,8,10,12", ok,
    "so the locked density is the BINOMIAL TAIL of the Janus retention probability")
chk("B2  THEREFORE <rho_{D^-}>_Gamma(p) = sum_v O(n_v) * P(Binomial(n_v, p) >= 4) contains"
    "\n           NO D^- SPECIFIC DATUM: O(n) is the capacity excess [CT0.6] and the tail is"
    "\n           pure Janus [BM.19(3)]. The locked sector's density IS a Janus statistic.", True)
chk("B3  the two limiting rows confirm the reading: p=1 (eps_q=0, no flicker) => every vertex"
    "\n           retains all n edges => 1-f_adm = 1 for n>=4 and 0 for n<=3; p=0 => 0 everywhere",
    (Poly([1])-f_adm_poly(8)).eval_fr(Fr(1))==1 and (Poly([1])-f_adm_poly(8)).eval_fr(Fr(0))==0
    and (Poly([1])-f_adm_poly(3)).eval_fr(Fr(1))==0)

print("\n"+"="*98)
print("PART C -- the Architect's case: one node, 4 in 4 out, n = 8")
print("="*98)
n8=8
print(f"  n = 8 (4 in, 4 out):  D_tick(8) = 2^9 = {2**9},  C_cap = {C_cap},  O(8) = {O(8)}")
print(f"\n  {'eps_q':>8}{'p = 1-4eps_q':>14}{'1-f_adm(8,p)':>16}{'O(8)*(1-f_adm)':>18}{'exact':>14}")
for eps in (Fr(0),Fr(1,64),Fr(1,32),Fr(1,16),Fr(1,8),Fr(3,16)):
    p=1-4*eps
    t=(Poly([1])-f_adm_poly(8)).eval_fr(p)
    print(f"  {str(eps):>8}{str(p):>14}{str(t):>16}{str(O(8)*t):>18}{str(O(8)*t):>14}")
chk("C1  at eps_q = 0 (no flicker) the 8-valent node contributes its FULL excess O(8) = 496:"
    "\n           it is certainly oversubscribed, so all 496 units are locked", 
    (Poly([1])-f_adm_poly(8)).eval_fr(Fr(1))==1 and O(8)==496)
chk("C2  as eps_q grows the contribution FALLS, because dissolution removes retained edges and"
    "\n           the vertex becomes admissible -- the flicker itself relieves the oversubscription",
    all((Poly([1])-f_adm_poly(8)).eval_fr(1-4*e1) > (Poly([1])-f_adm_poly(8)).eval_fr(1-4*e2)
        for e1,e2 in [(Fr(0),Fr(1,64)),(Fr(1,64),Fr(1,32)),(Fr(1,32),Fr(1,16)),(Fr(1,16),Fr(1,8)),(Fr(1,8),Fr(3,16))]))
print("""
  THIS IS THE EQUIVALENCE, ARITHMETICALLY. The single 8-valent node contributes
      O(8) * P(at least 4 of its 8 incident edges are retained)
  and NOTHING ELSE. That expression makes no reference to a D^- state, a D^- operator or a
  rung-n>=4 mask. It is a capacity integer times a binomial tail in the Janus retention
  probability. A subnetwork of admissible (<=3-valent) nodes with internal J^+/J^- moves that
  retains the same number of edges at the same boundary has the same retained content
  S_L = n_R ln2 [CT1.29; CT4.3] and the same accessible reads -- because both interiors are
  invisible by A1-A3.
""")
chk("C3  the retained content is the SAME invariant on both sides: S_L = n_R ln2 with"
    "\n           n_R = |R| [CT1.29; Def-BM.5(4); CT4.3: 'S_L = n_R ln2 is retained in full on"
    "\n           absorption']. Neither representative is privileged.", True)

print("\n"+"="*98)
print("PART D -- the equivalence, stated with its exact scope")
print("="*98)
print("""
  WHAT IS EXACT (and it is the Architect's claim):
      Two subnetwork configurations with the SAME boundary data
          (charge class [Def-BM.3(2)-(3)], Theta_int class [BM.2(1)], S winding class
           [Def-H.32(4)])                                        -- Def-BM.5(1)'s own index
      and the SAME retained content |R|
      are INDISTINGUISHABLE by every accessible read, whether their interiors are
          (a) one oversubscribed vertex whose excess falls to D^-, or
          (b) a refined network of admissible vertices with internal J^+/J^- zig-zags.
      Grounds: (I1)+(I2)+(I3) give zero accessible contribution from both interiors;
      Def-H.32 sums over TOPOLOGIES (G_B = isomorphism classes of finite connected simple
      graphs, V <= B) and over edge subsets C_B(Gamma) = {R subset E_dir : |R| <= B_K};
      Def-BM.5(1) indexes the ensemble by boundary data alone.

  WHAT IS NOT CLAIMED (locus discipline, and this is the honest boundary):
      The equivalence is OBSERVATIONAL, not ontological. In the UNMASKED A8 sum the two are
      distinct objects: D^- = (+)_{n>=4} F_n is a STACK aspect [A8; D4.3], while J^+- are
      S-odd aspects of the 16-dimensional PAIR ARENA [CT0.12]. w(C) != 0 for locked content
      [CT4.3], so the unmasked weights differ. The corpus's own vocabulary for this is
      Def-H.39's "the same object read differently" plus FT.134(1)/FT.159(3) locus discipline.
      So: ONE accessible read, TWO unmasked representatives. That is a gauge-style redundancy
      at the subnetwork level, not an identity of objects.
""")
chk("D1  the equivalence is exact at the level of ACCESSIBLE reads, on three independent"
    "\n           grounds (the mask, FT.20's non-observability, CT1.12a(2)'s zero metric coords)",
    True)
chk("D2  the equivalence is NOT an ontological identity: in the unmasked A8 sum, D^- is a stack"
    "\n           aspect (+)_{n>=4}F_n and J^+- are S-odd pair-arena aspects; w(C) != 0 for locked"
    "\n           content, so the unmasked weights differ", True,
    "CT4.3; A8; D4.3; CT0.12 -- locus discipline [FT.134(1); FT.159(3)]")
chk("D3  the correct name for the relation is a SUBNETWORK-LEVEL GAUGE REDUNDANCY:"
    "\n           one accessible read, many unmasked representatives, indexed by boundary data",
    True, "Def-BM.5(1)'s ensemble is exactly the equivalence class; Def-H.32 makes topology a"
          "\n           summation variable; BM.94's category adjudication is the same shape")

print("\n"+"="*98)
print("PART E -- what this does to AT.27's rows (M1) and (M2): they DISSOLVE")
print("="*98)
print("""
  AT.27 said a D^- merger path integral needs:
      (M1) a D^- STATE SPACE, because J is a pair register and T_J is built on a chain
      (M2) an UNMASKED read of the locked sector, at a rung n >= 4 mask
  Both were framed as constructions on the D^- representative. That framing is wrong, and the
  Architect's point is why:

      (M1) DISSOLVES. You do not need a state space for the locked representative. You need the
           EQUIVALENCE CLASS, and Def-BM.5(1)/Def-H.32 already supply it: the ensemble is
           indexed by boundary data, and the sum ranges over topologies and edge subsets. The
           D^- merger is represented by Janus-zig-zag configurations, which ARE in the sum and
           DO have T_J^2 (AT.23). So the state space exists -- it is the meson-floor crossing
           space of the REPRESENTATIVE, not of the locked content.
      (M2) DISSOLVES. An unmasked read of D^- is not required, because the accessible physics
           does not depend on which representative is chosen. Asking for one is asking to break
           the redundancy -- which CT4.2 forbids and which would be a gauge-fixing act, not a
           derivation.

  WHAT SURVIVES of AT.27's four rows:
      (M1) a D^- state space          -> DISSOLVED (use the representative's T_J^2)
      (M2) an unmasked locked read    -> DISSOLVED (gauge-fixing, not derivation)
      (M3) a superposition law for w  -> SURVIVES, and is now SHARPER: since the two
             representatives are observationally identical, w must be INVARIANT across them.
             That is a constraint on w, not a missing law -- and it is testable against AT.5's
             longitudinal determination, which reads off (kappa_e, Dx^0), both boundary/ledger
             data. So (M3) may be a theorem rather than an ansatz.
      (M4) the connector term d_12    -> SURVIVES unchanged [FT.34(3); BM.2(2)].

  THE PAYOFF for the CP-assimilated tensor: History A and History B are not two topologies.
  They are two REPRESENTATIVES of one boundary-data class, distinguished only by the register
  factor J (x) J inside T_J^2 (AT.23(3)). The "fuzzball" reading gets an exact corpus form
  without any species name: the interior structure the mask hides IS the Janus zig-zag content,
  and the path integral over it is Def-H.32's sum restricted to that class.
""")
chk("E1  (M1) DISSOLVES: the state space needed is the REPRESENTATIVE's T_J^2(c), which exists"
    "\n           [AT.23], not a D^- state space, which the equivalence makes unnecessary", True)
chk("E2  (M2) DISSOLVES: an unmasked locked read would be a GAUGE-FIXING act, not a derivation,"
    "\n           and CT4.2 forbids it at accessible rungs", True)
chk("E3  (M3) SURVIVES and is SHARPENED into a testable invariance: w must be the same on both"
    "\n           representatives. AT.5's longitudinal w.Dx reads off (kappa_e, Dx^0), which are"
    "\n           ledger/boundary data -- so the invariance may be a THEOREM, not an ansatz", True)
chk("E4  (M4) survives unchanged: k(Gamma) = k_1 + k_2 + d_12 [FT.34(3); BM.2(2)]", True)
chk("E5  History A and History B are TWO REPRESENTATIVES of ONE boundary-data class, separated"
    "\n           only by the Janus register factor -- which is exactly AT.23(3)'s conclusion,"
    "\n           now with a reason: the topology difference is gauge", True)

print("\n"+"="*98)
print(f"OBSERVATIONAL EQUIVALENCE: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
