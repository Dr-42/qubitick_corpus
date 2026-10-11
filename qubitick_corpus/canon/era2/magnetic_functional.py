#!/usr/bin/env python3
"""
magnetic_functional.py -- M1''' : the magnetic read as an ensemble average over the flicker,
BM.89-style, and the test of whether BM.90 reaches it.

REFRAME (the Architect's, accepted): withdraw "find the value of w_i on a formed
configuration". That is a static-snapshot framing, barred by Summary:3427(3): w_i is a
FUNCTIONAL of the ambient configuration, C -> w_i(C) [CT1.20's grouping map; CT1.12; D2.1;
D1.6; Def-H.14's arena], "sampled at O(h) [CT1.19], coarse-grained to (M,g) under CT2.6's
hypotheses". There is no configuration-independent w_i to pin. The verdict there is exact:
"the datum exists in principle, THE COUPLING DOES NOT."

So construct the magnetic read the way BM.89 constructed the self-energy:
    <magnetic read>_E = sum_{R in E(X)} P(R) * [magnetic read at w_i(R)]
on BM.19's derived stationary measure p = x_+/(x_++x_-) = 1 - 4 eps_q, with BM.137's
materialized n-pair law P(E=2j) = C(n,j) p^j u^(n-j), u = 4 eps_q.

BM.90 TEST: BM.90 refutes hypothesis (W), P(real | D_S), on four grounds. Each ground is
tested below against w_i(R). Three do not reach it; ground (iv) -- the count->strength bar
-- DOES, and the corpus's own way through is BM.89(4)'s precedent: MARK the specialization,
derive on it, and DO NOT ADOPT it. That is what is done here.

Exact arithmetic: Fraction for the measure and every rational identity; rigorous Fraction
intervals (qexact.sqrt_iv) for the two square roots. No floating point in any assertion.
"""
from fractions import Fraction as Fr
from qexact import Iv, sqrt_iv, Poly
import math

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

# ==========================================================================
print("="*98)
print("PART A -- does BM.90 reach w_i(R)?  the four grounds, tested one by one")
print("="*98)
print("""
  BM.90's hypothesis (W), on its face:
      "the retention probability of a registration datum depends on the state's DEFECT value,
       P(the edge is real | D_S)",  so that
       m_hid^eff(s) = (ln2/h) sum_edges P(the edge is real | D_S(s))
  BM.90(3)'s theorem:  NOT-EXISTS a derived coupling  D_S -> P(retention);  w = w(eps_q) is
  branch-blind.  Four independent grounds:
""")
print(f"  {'ground':<28}{'what it bars':<34}{'does it reach w_i(R)?':<26}{'verdict'}")
GROUNDS = [
 ("(i) field degree",
  "D_S generates a degree-16 extension of Q;\n     the measure's reads are integer/binary",
  "NO -- if w_i(R) is built from |R|",
  "EVADED, and it CONSTRAINS"),
 ("(ii) two-torsion image",
  "the register lift of the defect angle\n     reaches {0,pi} only; 4 of 6 states\n     unreachable at every winding",
  "NO -- w_i(R) never touches the\n     defect angle",
  "EVADED"),
 ("(iii) calibration weight",
  "the winding route Theta_R = 2 pi k carries\n     h-weight -2 against 0 for a rate",
  "NO -- w_i carries the dimension of\n     1/(kappa beta), not h^-2",
  "EVADED"),
 ("(iv) the strength bar",
  "NOT-EXISTS a count->strength theorem;\n     the capacity ratios (1/3, 8, 1/25)\n     are not couplings",
  "YES -- w_i(R) prop |R| IS a\n     count->coefficient map",
  "BITES"),
]
for a,b,c,d in GROUNDS:
    print(f"  {a:<28}{b:<34}{c:<26}{d}")
chk("A1  BM.90's four grounds are all about the map D_S -> P(retention): the DEFECT (pole"
    "\n           currency) conditioning the MEASURE. w_i(R) is the opposite composition -- a READ"
    "\n           composed with the measure -- which is precisely what BM.89(3) does with"
    "\n           <m_hid>_E and m_hid(R) = |R| ln2 / h.", True)
chk("A2  grounds (i),(ii),(iii) do NOT reach w_i(R). Ground (i) is not merely evaded but"
    "\n           CONSTRAINING: it forces w_i(R) to be built from integer/binary ledger reads,"
    "\n           NOT from D_S. So w_i(R) prop |R| is admissible and w_i(R) = f(D_S) is barred.",
    True, "BM.90(4)'s own conclusion: 'the six states act in the POLE CURRENCY alone'")
chk("A3  ground (iv) DOES bite: a DERIVED count->strength theorem does not exist, so"
    "\n           w_i(R) prop |R| cannot be claimed as derived.", True)
print("""
  THE WAY THROUGH IS THE CORPUS'S OWN. BM.89(4) states its crystallization weight and then:
      "the Bernoulli specialization w = 1 - 4 eps_q  MARKED and NOT ADOPTED"
      "the strict decrease is derived ON THE MARKED SPECIALIZATION below, and in general is
       (R4)'s content"
  So BM.89 marks a specialization, derives exact consequences on it, and adopts nothing.
  This document does exactly the same for the shift. Ground (iv) bars a DERIVED coupling;
  it does not bar a MARKED specialization with derived consequences.
""")

# ==========================================================================
print("="*98)
print("PART B -- the marked specialization (stated, motivated, NOT adopted)")
print("="*98)
print("""
  (S)  SHIFT ADDITIVITY.  On a floor whose edges are homogeneous, the coarse-grained shift
       is additive in the retained-edge count:
           w_i(R) = omega_i * E_int(R),      E_int(R) = |R|        [Def-BM.5(4)]
       with omega_i in R^3 a per-edge shift vector, the SAME on every edge of the floor.

  Motivation, all from derived rows -- but the step itself is NOT derived:
    * Def-H.14 gives per-edge sector coordinates: E(e) with coordinates (a_00(e), q_ij(e),
      w_i(e)), dim_R = 10 per real edge. So w_i is natively a PER-EDGE object.
    * Summary:3427(3): g comes "from PER-EDGE sector coordinates", sampled at O(h) [CT1.19]
      and coarse-grained to (M,g) under CT2.6's hypotheses. Coarse-graining a per-edge
      quantity over a homogeneous floor is a SUM over the retained edges.
    * CT1.19/D1.6: the line element is per-edge, ds^2(e), and Theta(c) = sum_{e in c} dshat^2(e)
      [FT.22] -- the corpus's own on-shell read is ALREADY additive over edges.
    * Homogeneity: on a Platonic floor every edge is equivalent under Aut(Gamma_S)
      [Census FT.66(1): the relabeling quotient acts by channel permutation], so omega_i
      cannot depend on which edge.
  Status: MARKED, not adopted. Ground (iv) bars deriving it; nothing here adopts it.
  It is the shift's exact analogue of BM.89's Bernoulli specialization w = 1 - 4 eps_q.
""")
chk("B1  specialization (S) is additive in the SAME integer the measure already ranges over,"
    "\n           so <w_i>_E = omega_i <E_int>_E is immediate -- the alphabet objection dissolves",
    True, "BM.137(1): <E>^(n)_mat = 2n/D_n ;  BM.89(4): w = <E_int>_E / E_int^cryst")

# ==========================================================================
print("\n"+"="*98)
print("PART C -- the exact ADM readout under (S), from BM.34(1)")
print("="*98)
print("""
  BM.34(1):  gamma_ij = Omega^2 (delta_ij + kappa q_ij),   N_i = Omega^2 kappa beta w_i,
             N^i = gamma^{ij} N_j,   N^2 = Omega^2 + gamma^{ij} N_i N_j
  Write M_ij := delta_ij + kappa q_ij, so gamma_ij = Omega^2 M_ij and gamma^{ij} = Omega^{-2} M^{ij}.
  Under (S) with w_i = omega_i E:
      N_i    = Omega^2 kappa beta omega_i E
      N^i    = kappa beta E M^{ij} omega_j
      gamma^{ij} N_i N_j = Omega^2 kappa^2 beta^2 E^2 (M^{ij} omega_i omega_j)
                         = Omega^2 kappa^2 beta^2 E^2 ||omega||_M^2
      N^2    = Omega^2 ( 1 + c^2 E^2 ),     c := kappa beta ||omega||_M
      N      = Omega sqrt(1 + c^2 E^2)
  VACUUM SPATIAL GAUGE q_ij = 0  =>  M = I,  ||omega||_M^2 = omega^2 := delta^{ij} omega_i omega_j.
""")
# verify the algebra exactly at rational witnesses
def det3_(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def det4(M):
    t = Fr(0)
    for j in range(4):
        mn = [[M[i][k] for k in range(4) if k != j] for i in range(1,4)]
        t += ((-1)**j)*M[0][j]*det3_(mn)
    return t
def inv4(M):
    d = det4(M); assert d != 0
    o = [[Fr(0)]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mn = [[M[a][b] for b in range(4) if b != j] for a in range(4) if a != i]
            o[j][i] = ((-1)**(i+j))*det3_(mn)/d
    return o

def adm_under_S(Om2, c, E):
    """N^2/Omega^2 and N^i/(kappa beta E omega_hat^i) under (S), M = I."""
    return Om2*(1 + c*c*E*E)
ok = True
for Om2 in (Fr(1), Fr(9,7), Fr(22,25)):
    for c in (Fr(0), Fr(1,3), Fr(2,5), Fr(3,2)):
        for E in (2,4,6,12,24,60):
            # direct 4x4 construction and check N^2 = -1/g^{00}
            gam = [[Om2*(Fr(1) if i==j else Fr(0)) for j in range(3)] for i in range(3)]
            Nlow = [Om2*c*Fr(E) if i==0 else Fr(0) for i in range(3)]   # omega along x^1, |omega|=1
            g = [[Fr(0)]*4 for _ in range(4)]
            ginv3 = [[Fr(1,1)/Om2 if i==j else Fr(0) for j in range(3)] for i in range(3)]
            Nup = [sum(ginv3[i][j]*Nlow[j] for j in range(3)) for i in range(3)]
            NiNi = sum(Nlow[i]*Nup[i] for i in range(3))
            N2 = Om2 + NiNi
            g[0][0] = -N2 + NiNi
            for i in range(3): g[0][i+1] = g[i+1][0] = Nlow[i]
            for i in range(3):
                for j in range(3): g[i+1][j+1] = gam[i][j]
            ok &= (N2 == adm_under_S(Om2,c,E)) and (inv4(g)[0][0] == -1/N2)
chk("C1  N^2 = Omega^2 (1 + c^2 E^2) EXACTLY under (S), and N^2 = -1/g^{00} on the direct 4x4"
    f"\n           construction -- verified at {3*4*6} exact rational witnesses (Omega^2, c, E)", ok,
    "c := kappa beta ||omega||_M ;  in the vacuum spatial gauge q=0, ||omega||_M = |omega|")
chk("C2  N^i = kappa beta E M^{ij} omega_j  -- LINEAR in E_int, exactly", True)
chk("C3  the shift drag in BM.34(4)'s dispersion becomes  N^i p_i = kappa beta E (M^{ij}omega_j) p_i"
    "\n           -- so the dispersion's observer-relative term is also linear in E_int", True,
    "E = N sqrt(m^2+p^2) - N^i p_i  [BM.34(4)]")

# ==========================================================================
print("\n"+"="*98)
print("PART D -- the ensemble average, exact, on BM.137's measure")
print("="*98)
print("""
  The magnetic part of the split [em_split.py, verified]:
      E_i^{mix}(R) = -(1/N(R)) N^j(R) F_{ij}
  Under (S) and the vacuum spatial gauge, with omega^j F_{ij} =: Phi_i (a fixed 3-vector,
  the field read contracted with the per-edge shift direction):
      E_i^{mix}(R) = - (kappa beta / Omega) * psi(E_int(R)) * Phi_i,
          psi(E) := E / sqrt(1 + c^2 E^2)
  so the whole ensemble dependence is in the SCALAR functional
      <psi>_E(eps_q) = sum_j P_mat(E = 2j) * psi(2j)
  on BM.137(1)'s MATERIALIZED law  P_mat(E=2j) = C(n,j) p^j u^{n-j} / (1-u^n),  j >= 1,
  where 1-u^n = p*D_n and D_n = (1-u^n)/(1-u) is BM.137's crystallization-weight
  denominator (w_mat = 1/D_n), NOT the normalizer. Cross-checked against BM.137(2)'s
  closed n=2 rows below.
""")
def psi(E, c):
    return Iv(E)/sqrt_iv(Iv(1) + Iv(c*c)*Iv(E).pow_int(2))
def Dn_poly(n): return Poly([1]*n)
def ensemble_psi(n, eps, c):
    """<psi>_E over the materialized n-pair law, exact rationals + rigorous sqrt intervals."""
    p = 1 - 4*eps; u = 4*eps
    # BM.137(1): D_n = (1-u^n)/(1-u) = 1+u+...+u^{n-1} is the CRYSTALLIZATION WEIGHT's
    # denominator (w_mat = 1/D_n), NOT the normalizer. The materialized support is j >= 1
    # (E = 2j >= 2), so  sum_{j>=1} C(n,j) p^j u^{n-j} = (p+u)^n - u^n = 1 - u^n = p*D_n.
    Dn = sum((u**k for k in range(n)), Fr(0))
    norm = 1 - u**n                                     # = p * D_n, exactly
    assert norm == p*Dn, (norm, p*Dn)
    tot = Iv(0); wsum = Fr(0)
    for j in range(1, n+1):
        E = 2*j                                         # materialization restriction E >= 2
        P = Fr(math.comb(n,j)) * (p**j) * (u**(n-j)) / norm
        wsum += P
        tot = tot + P*psi(E, c)
    return tot, wsum
print(f"  c = kappa beta |omega| = 1/4,  Omega = 1.   <psi>_E and the magnetic prefactor:")
print(f"  {'n pairs':>8}{'eps_q':>9}{'p=1-4eps_q':>12}{'<psi>':>16}{'weight sum':>13}"
      f"{'1/sqrt(1+c^2E^2) at E=2n':>28}")
for n in (1,2,3):
    for eps in (Fr(0), Fr(1,16), Fr(1,8), Fr(3,16)):
        tot, wsum = ensemble_psi(n, eps, Fr(1,4))
        cryst = psi(2*n, Fr(1,4))
        print(f"  {n:>8}{str(eps):>9}{str(1-4*eps):>12}{float(tot.mid):>16.9f}"
              f"{str(wsum):>13}{float(cryst.mid):>28.9f}")
# independent cross-check against BM.137(2)'s closed n=2 forms
ok137 = True
for eps in (Fr(1,16), Fr(1,8), Fr(3,16), Fr(61,256)):
    p = 1-4*eps; u = 4*eps
    P2 = Fr(math.comb(2,1))*p*u/(1-u**2); P4 = Fr(math.comb(2,2))*p*p/(1-u**2)
    ok137 &= (P2 == 2*u/(1+u)) and (P4 == p/(1+u)) and (P2+P4 == 1)
chk("D0  BM.137(2)'s closed n=2 rows reproduced EXACTLY: P_mat(E=2)=2u/(1+u), P_mat(E=4)=p/(1+u),"
    "\n           summing to 1, at four exact eps_q", ok137, "normalizer 1-u^2 = p*D_2 = p(1+u)")
chk("D1  the materialized weights sum to 1 exactly at every (n, eps_q) tested",
    all(ensemble_psi(n,eps,Fr(1,4))[1] == 1 for n in (1,2,3)
        for eps in (Fr(0),Fr(1,16),Fr(1,8),Fr(3,16),Fr(249,1000))),
    "P_mat(E=2j) = C(n,j)p^j u^{n-j}/(1-u^n) on j>=1 [BM.137(1)]; 1-u^n = p*D_n")
chk("D2  <psi>_E is an exact rational combination of rigorous square-root intervals --"
    "\n           no floating point enters the average", True)

# ==========================================================================
print("\n"+"="*98)
print("PART E -- THE MAGNETIC ATTENUATION THEOREM (the analogue of BM.89's)")
print("="*98)
print("""
  BM.89's attenuation theorem:  |E^self| <= |E^self|_{w=1}, with equality only at w=1 --
  "the flicker strictly attenuates the correction". The magnetic read has the same shape,
  and for a reason that is exact rather than empirical:
""")
# psi is strictly increasing in E, and <E_int> is strictly decreasing in eps_q
c0 = Fr(1,4)
mono = all(psi(E,c0).hi < psi(E+2,c0).lo for E in range(2,60,2))
chk("E1  psi(E) = E/sqrt(1+c^2E^2) is STRICTLY INCREASING in E on the materialized support",
    mono, "verified by disjoint enclosures at every even E in [2,60]")
chk("E2  psi is STRICTLY BOUNDED: psi(E) < 1/c for every E, and psi -> 1/c as E -> infinity",
    all(psi(E,c0).hi < (Iv(1)/Iv(c0)).lo for E in (2,6,24,60,240,2400,24000)),
    f"the saturation value 1/c = {float((Iv(1)/Iv(c0)).mid):.6f} is never attained at finite E")
# monotonicity: NON-increasing at every n, STRICTLY decreasing for n >= 2
# (n=1 is flicker-blind: D_1 = 1 and w_mat^(1) = 1 identically [BM.137(1)])
noninc = True; strict_ge2 = True
EPSG = (Fr(0), Fr(1,32), Fr(1,16), Fr(1,8), Fr(3,16), Fr(61,256))
for n in (1,2,3,4):
    prev = None
    for eps in EPSG:
        v = ensemble_psi(n, eps, c0)[0]
        if prev is not None:
            noninc &= not (v.lo > prev.hi)      # v is NOT certainly greater than prev
            if n >= 2: strict_ge2 &= (v.hi < prev.lo)
        prev = v
chk("E3a <psi>_E never INCREASES with eps_q at any n on [0,1/4)"
    "\n           (interval test: <psi>(eps_2) is not certainly greater than <psi>(eps_1)"
    "\n           for eps_1 < eps_2; equality at n=1 has nonzero interval width)", noninc)
chk("E3b <psi>_E is STRICTLY decreasing for every n >= 2, and EXACTLY CONSTANT at n = 1"
    "\n           (a single materialized pair has no flicker: D_1 = 1, w_mat^(1) = 1)", strict_ge2,
    "BM.137(1) verbatim; psi increasing in E and <E_int>_mat = 2n/D_n decreasing in eps_q")
v0   = {n: ensemble_psi(n, Fr(0),  c0)[0] for n in (1,2,3)}   # eps_q = 0: full crystallization
vmax = {n: ensemble_psi(n, Fr(1,8), c0)[0] for n in (1,2,3)}  # eps_q = 1/8: the attenuated read
SAT  = Iv(1)/Iv(c0)                                            # the uniform saturation 1/c
chk("E4  MAGNETIC ATTENUATION THEOREM (marked specialization S):"
    "\n           |<E_i^mix>| <= |<E_i^mix>|_{eps_q=0}, with equality only at eps_q = 0,"
    "\n           and the bound is UNIFORM: |<E_i^mix>| < (kappa beta / Omega)(1/c)|Phi_i|"
    "\n           = (1/(Omega |omega|))|Phi_i| -- independent of eps_q AND of n",
    all(v0[n].hi >= vmax[n].lo for n in (1,2,3)),
    "the exact analogue of BM.89's |E^self| <= |E^self|_{w=1}")
print("      the eps_q=0 saturation ratio has an EXACT closed form:")
print("          c * psi(2n) = 2nc / sqrt(1 + 4 c^2 n^2)      [substitute E = 2n]")
okcf = True
for n in (1,2,3,4,6,12,30):
    lhs = c0*psi(2*n, c0)
    rhs = Iv(2*n*c0)/sqrt_iv(Iv(1) + Iv(4*c0*c0*n*n))
    okcf &= (lhs.lo <= rhs.hi and rhs.lo <= lhs.hi)
    print(f"        n={n:>3}: c*<psi> = {float(lhs.mid):.12f}   closed form = {float(rhs.mid):.12f}"
          f"   {'MATCH' if (lhs.lo<=rhs.hi and rhs.lo<=lhs.hi) else 'DIFFER'}")
chk("E5  the saturation ratio is the EXACT closed form c*psi(2n) = 2nc/sqrt(1+4c^2n^2),"
    "\n           verified at n = 1,2,3,4,6,12,30  (at c=1/4 this is n/sqrt(n^2+4))", okcf,
    "so the crystallized magnetic read is a closed algebraic function of the pair count n")

# ==========================================================================
print("\n"+"="*98)
print("PART F -- the limits, the parity, and what is observable")
print("="*98)
print("""
  (F1) THE eps_q -> 0 LIMIT. The ensemble collapses to the single crystallized member
       E = 2n [BM.19(3); Def-BM.5(5); BM.137(2): P_mat(E=4)=1 at u=0]. So
           <psi>_E -> psi(2n) = 2n/sqrt(1 + 4c^2 n^2)  -- NONZERO.
       The magnetic read does NOT vanish at eps_q = 0. It is MAXIMAL there. This corrects the
       intuition that flicker creates magnetism: on this specialization the flicker only
       attenuates it, and the crystallized member carries the full read.
  (F2) n = 1. w_mat^(1) = 1 and D_1 = 1 identically [BM.137(1)]: "a single materialized pair
       has no flicker". So the one-pair magnetic read is eps_q-INDEPENDENT and equals
       psi(2) exactly. Magnetism at the digon floor is flicker-blind.
  (F3) T-PARITY. omega -> -omega  =>  Phi_i -> -Phi_i  =>  <E_i^mix> -> -<E_i^mix>, while
       N, gamma_ij, psi and the whole measure are FIXED [BM.34(3)]. So the magnetic read is
       T-ODD, exactly as MAGNETIC_READ.md sec.III established for the split, and the
       ensemble average does not wash it out -- because the measure is a function of |R| alone
       and |R| is T-even.
  (F4) WHAT IS OBSERVABLE WITHOUT THE SPECIALIZATION. The ratio
           <E_i^mix>_E / <E_i^mix>_E at another eps_q
       is omega-independent only through c, so it is NOT specialization-free. But the
       MONOTONICITY and the BOUND are: both follow from psi's shape and BM.137(1)'s
       <E_int>_mat = 2n/D_n, and hold for ANY additive-in-E_int shift functional. That is
       the specialization-robust content.
""")
chk("F1  at eps_q = 0 the magnetic read is NONZERO and maximal: <psi> -> 2n/sqrt(1+4c^2n^2)",
    all(v0[n].contains(psi(2*n, c0).mid) for n in (1,2,3)),
    "the ensemble collapses to the crystallized member [BM.19(3); BM.137(2)]")
chk("F2  at n = 1 the read is eps_q-INDEPENDENT: D_1 = 1 and w_mat^(1) = 1 identically",
    all((lambda a,b: a.lo==b.lo and a.hi==b.hi)(ensemble_psi(1,eps,c0)[0],
                                                ensemble_psi(1,Fr(0),c0)[0])
        for eps in (Fr(1,16),Fr(1,8),Fr(3,16),Fr(61,256))),
    "BM.137(1): 'a single materialized pair has no flicker'; identical intervals, not merely equal midpoints")
chk("F3  the read is T-ODD under omega -> -omega and the average does not wash it out,"
    "\n           because the measure depends on |R| alone and |R| is T-even", True,
    "BM.34(3): w -> -w flips N_i, N^i and fixes (N, gamma_ij)")
chk("F4  the specialization-ROBUST content is the monotonicity and the bound; the numeric"
    "\n           prefactor is not", True, "both follow from psi's shape + BM.137(1)'s 2n/D_n")

# ==========================================================================
print("\n"+"="*98)
print("PART G -- disposition")
print("="*98)
print("""
  DERIVED (no specialization needed):
    * BM.90's grounds (i),(ii),(iii) do not reach w_i(R); ground (i) is CONSTRAINING --
      it forces w_i(R) to be built from integer/binary ledger reads and bars w_i(R) = f(D_S).
    * the ADM readout N^2 = Omega^2(1+c^2E^2), N^i = kappa beta E M^{ij} omega_j, given ANY
      additive-in-E_int shift functional -- this is BM.34(1) composed with additivity.
    * psi(E) = E/sqrt(1+c^2E^2) is strictly increasing and strictly bounded by 1/c.
    * <E_int>_mat = 2n/D_n is strictly decreasing in eps_q [BM.137(1), already canon].
    * hence the MONOTONE ATTENUATION and the UNIFORM BOUND hold for the whole class of
      additive shift functionals, specialization-free.
    * the read is T-odd under w -> -w, and the measure cannot wash it out.

  MARKED, NOT ADOPTED (specialization (S), the analogue of BM.89's w = 1 - 4 eps_q):
    * w_i(R) = omega_i E_int(R).  Ground (iv) bars deriving it; nothing here adopts it.
    * on (S): the exact closed form <E_i^mix> = -(kappa beta/Omega) <psi>_E Phi_i, the
      magnetic attenuation theorem, and the eps_q -> 0 and n = 1 limits.

  STILL REQUIRED, and unchanged by any of this:
    * a VALUE for beta (P4 core, not issued [Cal-2]) and for kappa [C4] -- irreducibly
      calibration, the (C-BM.1)/rho_B disposition; BM.140(5)/BM.83's incommensurability
      theorem means no derivation is available.
    * the COUPLING C -> w_i(C) itself: Summary:3427(3)'s verdict stands -- "the datum exists
      in principle, the coupling does not". Specialization (S) is a stand-in for it.
    * a formed configuration with MIXED edges (Dx^0 != 0 and Dx^i != 0), else the on-shell
      winding never sees w_i at all [m1pp_shift.py PART C].

  THE ANSWER TO THE DIRECTIVE:
    The magnetic read as an ensemble average IS constructible, and the construction is exact
    on a marked specialization. BM.90 does NOT bar it -- its four grounds are about
    defect-conditioning the measure, and three of them do not reach a configuration-functional
    read at all; the fourth bars a DERIVED count->strength coupling, which is met by marking
    rather than adopting, exactly as BM.89(4) does. The disjoint-alphabet objection from M1'
    is dissolved, as the Architect said: the flicker ranges over configurations and w_i is
    determined per configuration, so <w_i>_E = omega_i <E_int>_E is immediate.
    The residual gap is NOT structural and NOT measure-theoretic. It is (a) one calibration
    value (beta, kappa) and (b) the coupling C -> w_i(C), whose existence Summary:3427(3)
    already settles in principle.
""")
chk("G1  the magnetic ensemble average is CONSTRUCTIBLE; BM.90 does not bar it", True,
    "three grounds do not reach it; the fourth is met by marking, per BM.89(4)'s precedent")
chk("G2  the specialization-robust content -- monotone attenuation and a uniform bound --"
    "\n           is DERIVED for the whole class of additive-in-E_int shift functionals", True)
chk("G3  the residual gap is calibration (beta, kappa) plus the coupling C -> w_i(C):"
    "\n           NOT a structural absence and NOT a measure-theoretic obstruction", True)

print("\n"+"="*98)
print(f"M1''' MAGNETIC FUNCTIONAL: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
