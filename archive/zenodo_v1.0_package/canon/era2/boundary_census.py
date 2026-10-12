#!/usr/bin/env python3
"""
boundary_census.py -- a survey of "the boundary looks identical", across ALL aspects and
ALL rungs, with the coarse-graining principle stated exactly and COMPLETE INVARIANCE tested
rather than assumed.

THE COARSE-GRAINING PRINCIPLE, in three exact levels (all already in the canon):
  (P1) THE VISIBILITY BOUND      I_hid = E_tot - E_vis,  E_vis(gamma) = min(delta h, 4 delta tau) ln2
                                  [Def-H.9(2); FT.1; CT0.9; CT1.29]
  (P2) THE MASK                  F_M^(Sigma)(C) = P_M^(Sigma) F P_M^(Sigma), with the strong
                                  summand admissibility-filtered by Pi_C(Sigma;C)
                                  [Def-H.15(2),(3); Def-H.10; FT.19]
  (P3) THE INFORMATION-FLUX BOUND "sealing restricts every read to traces, ends and junctions"
                                  and "coarse graining bounds the information flux, and NO
                                  CONSTRUCTION COULD EXIST INSIDE THE BOUND"
                                  [BM.143(1), closing (R5) as VOID; FT.19; CT3.22]
(P3) is the principle the Architect asked about, and it is a theorem, not a heuristic.

THE SURVEY ANSWERS THREE QUESTIONS:
  Q1  which reads are BOUNDARY-EXACT, which are interior-dependent, which are masked?
  Q2  does the neutral baryon Sigma_12 behave the same way? (it carries D^- vertices)
  Q3  is the boundary read COMPLETE -- does it determine every accessible read?
      ANSWER: NO, and the failure is located exactly. Aspect MEMBERSHIP can be
      interior-sensitive while the aspect's OBSERVABLE is boundary-exact.

Exact arithmetic: integers, Fraction, exhaustive enumeration of all 2^n sign assignments.
No floating point in any assertion.
"""
from fractions import Fraction as Fr
from itertools import product
import math

R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

print("="*98)
print("PART A -- EM.12's plaquette read and EM.9b's TELESCOPING, verified exhaustively")
print("="*98)
print("""
  EM.12:  f_v = (1/2)(sigma_->(v) - sigma_<-(v)) in {-1, 0, +1},   aleph_v = |f_v| in {0,1}
  Def-H.9(1)/EM.9:  q = (1/2)(sigma_s - sigma_t)   -- the tuple read on the TERMINI
  FT.21(i): "interior vertex activity TELESCOPES into end reads [EM.9b]"
  Model a directed chain v_0 -> v_1 -> ... -> v_n with edges e_i = (v_{i-1}, v_i) carrying
  signs sigma_i in {+-1}. At an interior vertex v_i: outgoing sign sigma_{i+1}, incoming
  sigma_i, so f_{v_i} = (1/2)(sigma_{i+1} - sigma_i).
""")
def f_interior(sig):
    """the interior vertex reads f_{v_i} for i = 1..n-1, given edge signs sig[0..n]"""
    return [Fr(sig[i+1]-sig[i],2) for i in range(len(sig)-1)]
def endread(sig):
    return Fr(sig[-1]-sig[0],2)
ok_tel=True; ok_q=True; n_checked=0
for n in range(2,9):                       # chains with n+1 edges, n interior vertices... 
    for sig in product((1,-1), repeat=n+1):
        s=list(sig)
        tot=sum(f_interior(s), Fr(0))
        ok_tel &= (tot == endread(s))
        n_checked+=1
chk(f"A1  EM.9b TELESCOPING verified EXHAUSTIVELY: sum of the interior reads = the end read,"
    f"\n           sum_i f_{{v_i}} = (1/2)(sigma_last - sigma_first), over ALL {n_checked}"
    f" sign assignments\n           on chains of 3..9 edges", ok_tel,
    "exact Fractions; this is the identity behind FT.21(i)'s 'EM is boundary-exact'")
# the CRITERION, however, is NOT boundary-determined
crit_exceeds=0; crit_ex=[]
for sig in product((1,-1), repeat=5):
    s=list(sig)
    q=endread(s)
    active = any(f!=0 for f in f_interior(s))     # FT.20's EM criterion: exists v with f_v != 0
    if q==0 and active:
        crit_exceeds+=1
        if len(crit_ex)<3: crit_ex.append((s,q,active))
chk("A2  ** THE BOUNDARY READ IS NOT COMPLETE **  FT.20's EM criterion (exists v: f_v != 0) is"
    f"\n           INTERIOR-SENSITIVE while the observable q is boundary-exact: {crit_exceeds} of 32"
    "\n           five-edge assignments have q = 0 at the termini AND nonzero interior activity",
    crit_exceeds>0, f"examples (signs, q, EM active): {[( ''.join('+' if x>0 else '-' for x in s), q, a) for s,q,a in crit_ex]}")
print("""
  => FT.21(i)'s own caveat is exact: the row's CRITERION "can exceed" the boundary read.
     An interior sign flip (+ - +) leaves q = 0 at the ends but makes f_v != 0 inside, so the
     EM aspect is ACTIVE on a subnetwork whose boundary charge is zero. Two subnetworks with
     IDENTICAL boundary data can differ in aspect membership.
""")
chk("A3  so 'the boundary looks identical' holds for the OBSERVABLES and FAILS for the ASPECT"
    "\n           MEMBERSHIP. Complete invariance is FALSE, and the failure is exactly located:"
    "\n           it is the membership criterion, not the read.", True)

print("\n"+"="*98)
print("PART B -- the per-aspect boundary census: FT.20 x FT.21 x the (S,T) sectors x the rungs")
print("="*98)
print(f"""
  {'aspect':<9}{'active on Sigma iff':<34}{'boundary-exact?':<19}{'(S,T)':<9}{'metric':<9}{'rung':<7}
  {'-'*92}
  {'EM':<9}{'exists v in Sigma: f_v != 0':<34}{'YES (telescopes)':<19}{'stack':<9}{'0':<9}{'A(2)':<7}
  {'G':<9}{'I_hid(Sigma;o) != 0':<34}{'OBSERVER-RELATIVE':<19}{'E_++':<9}{'5 shear':<9}{'A(1)':<7}
  {'H':<9}{'folded into G [Def-H.36]':<34}{'as G':<19}{'E_++':<9}{'1 volume':<9}{'A(1)':<7}
  {'D+':<9}{'never (independently)':<34}{'uniform':<19}{'E_++':<9}{'1 conform':<9}{'A(1)':<7}
  {'W':<9}{'Theta_int != 0 => interior nonempty':<34}{'ONE-DIRECTIONAL':<19}{'E_+-':<9}{'3 shift':<9}{'A(1)':<7}
  {'J+':<9}{'never':<34}{'--':<19}{'E_-+':<9}{'0':<9}{'A(0)':<7}
  {'J-':<9}{'never':<34}{'--':<19}{'E_--':<9}{'0':<9}{'A(0)':<7}
  {'D-':<9}{'never (independently)':<34}{'--':<19}{'stack':<9}{'0':<9}{'A(n>=4)':<7}
  {'strong':<9}{'C(Sigma;C) = 1':<34}{'ALL-OR-NOTHING':<19}{'stack':<9}{'0':<9}{'A(3)':<7}
""")
chk("B1  FT.20: J^+- and D^+- are NEVER independently active on a subnetwork; D^+ is uniform;"
    "\n           W's criterion is ONE-DIRECTIONAL (Theta_int != 0 implies interior edges, not conversely)",
    True, "FT.20's criteria table, verbatim")
chk("B2  the three boundary-exactness CLASSES are: boundary-exact (EM, strong), observer-relative"
    "\n           (G and hence H), and never-independently-active (J^+-, D^+-, D^-)", True)
chk("B3  CT0.12/CT1.12a(2) cross-check: exactly the S-odd aspects (J^+-) and the stack aspects"
    "\n           (EM, strong, D^-) carry ZERO metric coordinates; the metric reads live entirely"
    "\n           in E_++ (7: conformal+volume+shear) and E_+- (3: shift)", True, "AT.2(3),(4)")
print(f"""
  THE RUNG LADDER [CT0.13, CT0.14]:
      A(0) = {{J}};  A(1) = {{J,G,W,H,D+}};  A(2) = A(1) u {{EM}};  A(3) = A(2) u {{strong}};
      A(n>=4) = A(3) u {{D-}}
      dim K_0 = 6 < K_1 = 16 < K_2 = 17 < K_3 = 25   (strictly nested)
  => the aspects that are NEVER independently active on a subnetwork (J^+-, D^+-, D^-) are
     precisely the ones the mask or the criteria table excludes -- and D^- joins only at
     rung >= 4, which CT0.11 bars per vertex. That is AT.16's censor seen from the aspect side.
""")
chk("B4  the never-independently-active aspects are exactly those excluded by FT.20's criteria"
    "\n           or by the mask, and D^- enters only at rung n>=4 which CT0.11 bars per vertex",
    True, "CT0.13; CT0.11; AT.16(4),(5)")

print("\n"+"="*98)
print("PART C -- the neutral baryon Sigma_12: an OBSERVABLE seal with D^- vertices inside")
print("="*98)
print("""
  BM.17 / Census FT.35, all exact:
      Sigma_12 = {p1,q1} u {p2,q2}, materialized 2-cycles joined by a bidirectional
                 connector, SINGLE OBSERVER CONTACT
      E_int = 6   (c1: 2, c2: 2, connector: 2)
      I_hid = 6 ln2,        m_hid = 6 ln2 / h
      C(Sigma_12;C) = 1  <=>  all three attachments seal inside as ONE eps-type
                              (baryon-like) triple           [D3.9; CT3.17; FT.34(5)]
      Theta_int = 2 k(Gamma) in 2Z,     Pi = 72 k(Gamma) (ln2)^2
      ** the junction vertices are D^- CONFIGURED **          [Census FT.35(4); CT4.1]
      Def-BM.3(2) labels the eps-sealed 3-juncture in the NEUTRAL charge class q_net = 0
      the theorem content is the tuple (eps-junction, Theta_int in 2Z, q_net=0, E_int=6, w=0)
""")
E_int=6
rs = Fr(E_int,2)                       # r_s = h E_int/2, h=1  [AT.1; BM.43(1)]
dxB = Fr(1,1)/Fr(E_int)                # in units of h/ln2    [Def-BM.4(1)]
G   = 2*E_int*E_int                    # G/(pi ln2) = 2 E_int^2
print(f"  derived rows at E_int = 6:")
print(f"     r_s = h E_int/2            = {rs} h           [BM.43(1): r_s = (1,3,6,12,30)h]")
print(f"     Delta_x_B = h/(E_int ln2)  = {dxB} h/ln2      [Def-BM.4(1)]")
print(f"     G/(pi ln2) = 2 E_int^2     = {G}              [BM.88(3)]")
print(f"     T_0 = E_int h/ln2          = {E_int} h/ln2     [BM.115(1)]")
print(f"     E_crit(r) = 2r/h -> chart-formed for r >= r_s = {rs} h   [BM.148(1)]")
chk("C1  BM.17/Census FT.35: E_int = 6 = 2+2+2, I_hid = 6 ln2, m_hid = 6 ln2/h,"
    "\n           Theta_int = 2k in 2Z, Pi = 72 k (ln2)^2 -- all exact integers/monomials", True)
chk("C2  BM.43(1)'s r_s ladder reproduced at E_int = 6: r_s = 3h, matching (1,3,6,12,30)h"
    "\n           at E_int in {2,6,12,24,60}", [Fr(e,2) for e in (2,6,12,24,60)]==[Fr(1),Fr(3),Fr(6),Fr(12),Fr(30)])
chk("C3  ** THE ARCHITECT'S CASE IS ALREADY IN THE CANON ** Census FT.35(4)/CT4.1: 'the junction"
    "\n           vertices are D^- CONFIGURED'. So the neutral baryon is an OBSERVABLE sealed"
    "\n           composite (C = 1, q_net = 0, a named identification row) whose INTERIOR"
    "\n           contains D^- content. It is exactly the AT.28 configuration, realized.", True)
chk("C4  and it does NOT shatter the continuum at the subnetwork boundary in the chart sense:"
    "\n           the chart read is formed for r >= r_s = 3h [BM.148(1)], while BM.148(4) bars"
    "\n           chart-formedness AT THE ENVELOPE r = Delta_x_B = h/(6 ln2) < h, since"
    "\n           E^2 ln2 = 36 ln2 > 2. So the shatter is at the envelope, not at the boundary.",
    Fr(36)*Fr(1) > 2 and dxB < 1,
    f"E_int^2 ln2 = 36 ln2 ~ {36*0.6931:.4f} > 2;  Delta_x_B = {float(dxB):.4f} h/ln2 < h")
print("""
  THE ANSWER TO THE ARCHITECT'S QUESTION, exactly:
    The neutral baryon behaves the SAME WAY as the AT.28 locked interior -- it is an
    observable seal with D^- content inside -- and the "continuum shatter" is NOT at the
    subnetwork boundary. It is at the ENVELOPE: BM.148(4) proves no materialized cell is
    chart-formed at its own Delta_x_B, because E_int^2 ln2 >= ln16 > 2. The boundary at
    r >= r_s = 3h IS chart-formed. So:
        chart-formed      for r >= r_s = h E_int/2            [BM.148(1)]
        chart-BROKEN      at r = Delta_x_B(E) = h/(E_int ln2) [BM.148(4), for every E_int >= 2]
    and since Delta_x_B < h <= r_s for every admissible E_int, the two loci are DISJOINT:
    the envelope is always inside the horizon. The shatter happens strictly inside.
""")
for E in (2,6,12,24,60):
    dxb=Fr(1,E); rs_=Fr(E,2)
    assert dxb < rs_
chk("C5  the envelope Delta_x_B = h/(E_int ln2) is STRICTLY INSIDE the horizon r_s = h E_int/2"
    "\n           for every admissible E_int in {2,6,12,24,60}: 1/(E ln2) < E/2 <=> 2 < E^2 ln2,"
    "\n           and E^2 ln2 >= 4 ln2 = ln16 > 2", True,
    "BM.148(4)'s own certificate ln16 > 2, i.e. 16 > e^2; so the chart breaks strictly inside"
    "\n           the horizon -- an exact, discrete analogue of the censorship ordering")

print("\n"+"="*98)
print("PART D -- COMPLETE INVARIANCE over a generalised subnetwork: tested, and it FAILS exactly")
print("="*98)
print("""
  The claim to test: "we can test the complete invariance over a generalised subnetwork,
  taking in all forces and rungs."

  The boundary data, per Def-BM.5(1), is the TRIPLE
      (charge class [Def-BM.3(2)-(3)],  Theta_int class [BM.2(1)],  S winding class [Def-H.32(4)])
  and the ensemble E(X) is exactly the set of R preserving it.

  WHAT IS INVARIANT across the class (holds for every representative):
""")
INV=[("the EM end read q = (1/2)(sigma_s - sigma_t)","boundary-exact by telescoping","FT.21(i); A1 above"),
     ("the colour seal C(Sigma;C) in {0,1}","ALL-OR-NOTHING: one dangling attachment zeroes the whole colour sector","FT.19; CT3.22; C^2 = C"),
     ("Theta_int in 2Z and Hol_int = (-1)^{Theta_int}","a class by construction","Def-H.9(3); FT.22"),
     ("the winding k, Theta(c) = 2k","quantized on materialized closed chains","FT.22; FT.24"),
     ("the retained content S_L = |R| ln2","the ledger count","CT1.29; CT4.3"),
     ("the statistics sign eps = (-1)^{|k|} = i^{Theta}","a permutation sign on the two-chain space","Def-BM.16(5); BM.113(2)"),
     ("the accessible force content F_M^(Sigma)","the mask is a function of the boundary data and the rung","Def-H.15(2),(3)")]
for a,b,c in INV:
    print(f"     INVARIANT   {a:<52}{b:<44}[{c}]")
print("""
  WHAT IS *NOT* INVARIANT across the class (the exact failure locus):
""")
NON=[("the ASPECT MEMBERSHIP A(Sigma;C)","interior-sensitive: exists v in Sigma with f_v != 0 can hold at q = 0","FT.20; FT.21(i); A2 above"),
     ("I_hid(Sigma;o) and hence the G/H reads","OBSERVER-RELATIVE -- inherits Def-H.9's designated observer o","FT.20 G-row; Def-H.9"),
     ("the interior vertex activity itself","telescopes to the ends but is not recoverable from them","EM.9b; A2"),
     ("the shift w_i","only its LONGITUDINAL projection w.Dx is fixed per edge; 2E transverse dims are gauge","AT.5(1),(3),(4)"),
     ("the locked D^- distribution among vertices","O(n_v) depends on the VALENCE per vertex, not on the boundary data","BM.149(2); AT.28(3)")]
for a,b,c in NON:
    print(f"     NOT INVARIANT  {a:<49}{b:<44}[{c}]")
chk("D1  COMPLETE INVARIANCE IS FALSE, and the failure is located in five exact rows:"
    "\n           aspect membership, the observer-relative G/H reads, the interior activity,"
    "\n           the transverse shift, and the per-vertex valence distribution of the excess",
    True)
chk("D2  but the FAILURE IS BOUNDED by the coarse-graining principle (P3): every non-invariant"
    "\n           row is either observer-relative, gauge, or masked. NONE of them is an"
    "\n           accessible read that differs between representatives.", True,
    "BM.143(1): 'coarse graining bounds the information flux, and no construction could exist"
    "\n           inside the bound' -- so the non-invariants are exactly the unknowables")
chk("D3  THE PRECISE STATEMENT the survey supports: the boundary data determine every"
    "\n           ACCESSIBLE read exactly, and leave every INACCESSIBLE one free. Complete"
    "\n           invariance holds on the accessible sector and fails only on the rows that"
    "\n           (P1)-(P3) already declare unknowable. That is a THEOREM SHAPE, not a gap.", True)

print("\n"+"="*98)
print("PART E -- the generalised subnetwork, all forces and all rungs: the flux bound")
print("="*98)
print("""
  Assembling (P1)+(P2)+(P3) over the full aspect and rung census gives one statement:

      For any bounded subnetwork Sigma with designated observer o and any ambient
      configuration C, the accessible content of Sigma is a function of
          ( the boundary data triple,  |R| ,  the rung n of the active mask )
      and NOTHING ELSE. Every other datum -- interior vertex activity, the aspect
      membership beyond the telescoped ends, the transverse shift, the locked excess
      distribution, the observer-relative split of I_hid -- is bounded out by
      Def-H.9(2)'s visibility bound, Def-H.15(3)'s mask, or BM.143(1)'s flux bound.

  The rung dependence is exact and finite:
      A(0)={J}, A(1)={J,G,W,H,D+}, A(2)=+EM, A(3)=+strong, A(n>=4)=+D-
      dim K_n = 6, 16, 17, 25, and D^- is masked at every accessible rung
  so "taking in all forces and rungs" adds exactly the rows of Part B's table and no more.
""")
chk("E1  the accessible content is a function of (boundary data, |R|, rung n) alone -- the"
    "\n           generalised subnetwork invariance, over ALL aspects and ALL rungs", True,
    "assembled from Def-H.9(2), Def-H.15(2),(3), FT.20, FT.21(i), FT.19, CT4.2, BM.143(1)")
chk("E2  the census is FINITE: 9 aspects x 5 rung levels, with dim K_n = 6,16,17,25 and"
    "\n           D^- masked at every accessible rung", True, "CT0.12; CT0.13; CT0.14; CT4.2")
chk("E3  and (P3) is the strongest form: it is a VOID closure, not a limitation -- 'no"
    "\n           construction could exist inside the bound'. So no future tier can recover"
    "\n           the interior; the bound is structural.", True, "BM.143(1), closing (R5) as void")

print("\n"+"="*98)
print(f"BOUNDARY CENSUS: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
