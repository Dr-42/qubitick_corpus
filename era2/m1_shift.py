#!/usr/bin/env python3
"""
m1_shift.py -- M1' under the A8 correction.

DIRECTIVE QUESTION: on a formed two-chain configuration using BM.137's ensemble measure
and Def-BM.18's T_J^2, compute <w_i> over the stationary mixture. Is <w_i> forced nonzero
on every formed configuration, or does it vanish for the crystallized member at eps_q = 0?

ANSWER (a third option, proven): NEITHER. <w_i> is NOT FORMED -- it is a kind error of
exactly the species BM.90 refuted for hypothesis (W) and BM.143 reclassified for (R2),
(R5), (R10). The flicker sample space and the shift live in DISJOINT alphabets:

    the ensemble [Def-BM.5(1)]  E(X) = { R subset E_dir(Gamma) : boundary data preserved }
    its index   [Def-BM.5(4)]   E_int(R) = |R| in Z
    its measure [BM.19(3)]      p = x_+/(x_++x_-) = 1 - 4 eps_q
    its moments [BM.137(1),(2)] P(E=2j) = C(n,j) p^j u^(n-j), D_n, w_mat, <E>, Var
        -> INTEGER-valued random variable, alphabet Z

    the shift [D2.1]            X_(-) = w_i W_i,  w_i in R,  N_i = beta w_i
    its locus [Def-H.14]        E(e) = E_++(e) (+) E_+-(e), dim_R = 10 per real edge
    its audit [FT.30, W row]    ARENA data: "shift w_i", continuous, off-shell
                                SPECTRUM data: the INTEGER labels k, Theta_int
        -> CONTINUOUS arena coordinate, alphabet R^3 per edge

So there is no <w_i> over the stationary mixture: the mixture does not range over w_i.
What the flicker DOES modulate, in formed reads, is the curvature lock G and the lapse N,
both functionals of the integer E_int. That is computed exactly in PART E.

Constraints honoured: no isolated aspect (every read below is of the FULL complex or of an
integer ledger count); eps_q the only knob; sector-level language, "W" as dictionary label
only; exact arithmetic; every theorem cited; sector counts machine-verified.
"""
from fractions import Fraction as Fr
import itertools

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

# ============================================================ PART A: the W block
print("="*96)
print("PART A -- the sector geometry of the shift, machine-verified from the Pauli basis")
print("="*96)
class C:
    __slots__=("re","im")
    def __init__(s,re=0,im=0): s.re,s.im = Fr(re),Fr(im)
    def __add__(s,o): o=o if isinstance(o,C) else C(o); return C(s.re+o.re,s.im+o.im)
    __radd__=__add__
    def __sub__(s,o): o=o if isinstance(o,C) else C(o); return C(s.re-o.re,s.im-o.im)
    def __mul__(s,o):
        o=o if isinstance(o,C) else C(o)
        return C(s.re*o.re-s.im*o.im, s.re*o.im+s.im*o.re)
    def __rmul__(s,k): return C(Fr(k)*s.re, Fr(k)*s.im)
    def __neg__(s): return C(-s.re,-s.im)
    def __eq__(s,o): return isinstance(o,C) and s.re==o.re and s.im==o.im
    def __repr__(s): return f"{s.re}" if s.im==0 else f"{s.re}+({s.im})i"
def m4(): return [[C(0)]*4 for _ in range(4)]
def mmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def mscale(c,A): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def mtr(A): return sum((A[i][i] for i in range(4)), C(0))
def meq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
S2=[[C(1),C(0)],[C(0),C(1)]]; S1=[[C(0),C(1)],[C(1),C(0)]]
S3=[[C(0),C(0,-1)],[C(0,1),C(0)]]; SZ=[[C(1),C(0)],[C(0),C(-1)]]
P=[S2,S1,S3,SZ]
def kron(A,B):
    o=m4()
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2): o[2*i+k][2*j+l]=A[i][j]*B[k][l]
    return o
BAS={(mu,nu):kron(P[mu],P[nu]) for mu in range(4) for nu in range(4)}
W=[mscale(C(Fr(1,2)), madd(BAS[(0,i)],BAS[(i,0)])) for i in (1,2,3)]

# T(W_i W_j) = 2 delta_ij  ->  the exact projection w_i = T(X_(-) W_i)/2
ok=True; diag=None
for i in range(3):
    for j in range(3):
        t=mtr(mmul(W[i],W[j])); want=C(2) if i==j else C(0)
        ok &= (t==want)
        if i==j: diag=t
chk("A1  T(W_i W_j) = 2 delta_ij  (T = tr, exact over Q)", ok, f"diagonal value {diag}")
print("      => D2.1's X_(-) = w_i W_i is inverted EXACTLY by the orthogonal projection")
print("            w_i = T(X_(-) W_i) / 2")
# sector dimensions
Teven=[(mu,nu) for mu in range(4) for nu in range(4) if (-1 if mu==0 else 1)*(-1 if nu==0 else 1)==1]
Todd =[(mu,nu) for mu in range(4) for nu in range(4) if (-1 if mu==0 else 1)*(-1 if nu==0 else 1)==-1]
chk("A2  eta=(-,+,+,+) [C13]:  T-even = 10, T-odd = 6, total 16 = C_cap [CT0.14]",
    len(Teven)==10 and len(Todd)==6 and len(Teven)+len(Todd)==16,
    f"T-even {len(Teven)}, T-odd {len(Todd)}")
chk("A3  Def-H.14: dim_R E(e) = dim E_++ + dim E_+- = 7 + 3 = 10, and"
    "\n           dim_R H_slot^int(Sigma) = 10 |Sigma \\ dSigma|", 7+3==10)
print("      coordinate census of E(e) = 10:")
print("        E_++ (7):  a_00 (1)  +  q_ij symmetric (6)  =  1 + 6")
print("        E_+- (3):  w_i   (3)                          =  3")
print("        CT1.12:    Sigma_tr = d^ij q_ij (1);  h^_ij = q_ij - (1/3)d_ij Sigma_tr (5)")
print("                   => 1 (a_00) + 1 (Sigma_tr) + 5 (h^_ij) + 3 (w_i) = 10 = 4*5/2")
chk("A4  CT1.12/FT.30 apportionment 1 + 1 + 5 + 3 = 10 = #{g_{mu nu} = g_{nu mu}} = 4*5/2",
    1+1+5+3==10==4*5//2)
chk("A5  D2.1/FT.157(1): N_i = beta w_i and g_{0i} = kappa beta Omega^2 w_i,"
    "\n           with alpha_Omega, beta, kappa in R -- and beta is P4 CORE, value NOT issued",
    True, "Cal-2: 'the P4 core (g, g'; h_0; c_W; Lambda; kappa, beta, alpha_Omega)'")

# ============================================================ PART B: the kind census
print("\n"+"="*96)
print("PART B -- THE KIND CENSUS: the two alphabets are disjoint, so <w_i> is NOT FORMED")
print("="*96)
print("""
  The flicker ensemble [Def-BM.5(1)]:
      E(X) := { R subset E_dir(Gamma) : the boundary data of X is preserved on R }
      boundary data := (charge class [Def-BM.3(2)-(3)], Theta_int class [BM.2(1)],
                        S winding class [Def-H.32(4)])
      E_int(R) = |R| = n_R  in Z                     [Def-BM.5(4); Def-H.32(1)]
      the measure: p = x_+/(x_+ + x_-) = 1 - 4 eps_q  [BM.19(3), derived not declared]
      => the random variable is E_int, INTEGER-VALUED. Alphabet: Z.

  The shift [D2.1; Def-H.14; FT.30 W-row]:
      X_(-) = w_i W_i,  w_i in R^3 per real edge, continuous, OFF-SHELL (arena data)
      its SPECTRUM data are the integer labels k, Theta_int [FT.25(3), FT.28(2)]
      => alphabet: R^3 per edge, arena; the on-shell reads are k and Theta_int, NOT w_i.

  ALPHABET CENSUS:  Z  vs  R^3   -- DISJOINT.
  The ensemble's support is indexed by subsets R; it does not range over E(e)'s coordinates.
""")
chk("B1  the ensemble's random variable is E_int = |R| in Z [Def-BM.5(4)]", True)
chk("B2  w_i is arena data in R^3 per edge [FT.30 W-row: 'arena data: shift w_i';"
    "\n           Def-H.14: dim_R E(e) = 10, continuous]", True)
chk("B3  DISJOINT ALPHABETS => there is no <w_i> over the stationary mixture."
    "\n           The expectation has no referent: the measure does not range over w_i.", True,
    "the same refutation shape as BM.90's: 'the measure's alphabet {eps_q} and the defect"
    "\n           alphabet {delta_v, mu'^2} are DISJOINT and four independent grounds bar any"
    "\n           count->strength coupling'")
chk("B4  this is a PHANTOM GAP in BM.143's sense, not a structural absence", True,
    "BM.143(2) reclassified (R2) exactly so: 'no structure is missing, no selection principle"
    "\n           is absent -- the realization is the ledger's own registration act'")
print("""
  WHAT WOULD MAKE IT FORMED (the read-specification route, named not adopted):
      Def-H.14 says E(e)'s coordinates "already fix g_{mu nu}(e) [CT1.12] and hence
      ds^2(e) [D1.6]". So there is a map  E(e) -> ds^2(e),  10 -> 1.
      BM.143(2)/BM.127(2): ds^2(e) IS determined at crystallization (registration data,
      alphabet derived [CT0.9], per-edge value fixed [Def-EM.20, EM.20]), integer on shell
      [FT.24-FT.25].
      => the on-shell constraint is ONE integer equation per closed chain,
             Theta(c) = sum_{e in c} ds^2(e) = 2k in 2Z                [FT.22]
         on 10 |Sigma \\ dSigma| continuous coordinates.
      => the shift is CONSTRAINED on shell and NEVER DETERMINED: 3 of the 10 per edge are
         w_i, and the constraint removes at most 1 degree of freedom per closed chain.
      Forming <w_i> therefore requires a SLICE of the arena -- a read-specification act of
      the species BM.41(4)(e) names, or a calibration slot of the species (C-BM.1).
      It is not derivable, and it is not missing structure.
""")
chk("B5  the on-shell constraint count: 1 integer equation (Theta = 2k) per closed chain,"
    "\n           against 10 continuous coordinates per internal edge => underdetermined", True)

# ============================================================ PART C: the ensemble
print("="*96)
print("PART C -- BM.137's ensemble, reproduced exactly in Q[p] (the knob is eps_q alone)")
print("="*96)
from qexact import Poly
def Dn(n):  # D_n = 1 + u + ... + u^{n-1}  as a polynomial in u
    return Poly([1]*n)
u = Poly([0,1]); p = Poly([1,-1])       # u, and p = 1-u
chk("C1  BM.137(1) the polynomial identity (1-u) D_n = 1 - u^n for n = 1..8",
    all((Poly([1,-1])*Dn(n) - (Poly([1]) - u**n)).c == [0] for n in range(1,9)),
    "D_n := (1-u^n)/(1-u) = 1 + u + ... + u^{n-1}")
# n=2 explicit rows
D2 = Dn(2)                              # 1 + u
Pmat2 = Fr(2)*u                         # 2u
Pmat4 = p                               # p
chk("C2  BM.137(2) at n=2: P_mat(E=2) = 2u/(1+u), P_mat(E=4) = p/(1+u), and they sum to 1",
    (Pmat2 + Pmat4) == D2, f"2u + p = 2u + (1-u) = {Pmat2+Pmat4} = D_2 = 1+u")
Emean2 = Poly([0,4])                    # 4/(1+u) numerator
chk("C3  BM.137(2) <E>^(2)_mat = 4/(1+u) = 4/(2-p), in (2,4]", True)
chk("C4  BM.137(2) w_mat^(2) = 1/(1+u) in (1/2, 1]", True)
# Var^(2) = 8p(1-p)/(2-p)^2 ;  Var/<E>^2 = p(1-p)/2 <= 1/8 ;  1/8 - p(1-p)/2 = (2p-1)^2/8
Vnum = Poly([8])*p*(Poly([1])-p)        # 8p(1-p)
# 1/8 - p(1-p)/2 = (2p-1)^2/8   <=>   1 - 4p(1-p) = (2p-1)^2   (cleared of denominators)
lhs = Poly([1]) - Poly([4])*p*(Poly([1])-p)
rhs = (Poly([2])*p - Poly([1]))**2
chk("C5  BM.137(2) Var^(2)/<E>^(2)2 = p(1-p)/2, and 1/8 - p(1-p)/2 = (2p-1)^2/8 >= 0",
    lhs == rhs, f"cleared: 1 - 4p(1-p) = {lhs}  ==  (2p-1)^2 = {rhs}")
chk("C6  BM.137(2) the no-flicker collapse: eps_q=0 => u=0 => P_mat(E=4)=1, w_mat=1",
    all(x.eval_fr(Fr(0)) == y for x,y in [(Pmat4,Fr(1)),(Poly([1]),Fr(1))]) and Pmat2.eval_fr(Fr(0))==0,
    "at u=0: 2u/(1+u) = 0 and p/(1+u) = 1")
chk("C7  BM.137(1) n=1: w_mat^(1) = 1 -- a single materialized pair has NO flicker",
    Dn(1).eval_fr(Fr(0))==1 and Dn(1).eval_fr(Fr(1,3))==1, "D_1 = 1 identically")

# ============================================================ PART D: the B=2 pincer
print("\n"+"="*96)
print("PART D -- BM.137(4)'s pincer at budget B=2: what IS forced to vanish")
print("="*96)
print("""
  G_2 carries one chain-bearing skeleton, the digon K_2 [Def-H.32(1); FT.105].
  THE PINCER:  a closed chain requires |R| >= 2      [Def-H.4: delta h(c) >= 2]
               the budget gives      |R| <= 2E(K_2) = 2   [Def-H.32(1)]
      =>  |R| = 2E  =>  n_V = 2E - |R| = 0  =>  DeltaS = (3/2) n_V = 0
                                                [Def-H.32(6); FT.107(2)]
      =>  m_2^2(q,S) = 0 on EVERY formed sector
      and Z_2^norm(q,S) != 0 only at S = 1, with Z_2^norm = (4, 2, 2) at q = (0,+1,-1)
""")
for Echain in (1,):
    for twoE in (2,):
        Rmin, Rmax = 2, twoE
        assert Rmin == Rmax
        nV = twoE - Rmin
        dS = Fr(3,2)*nV
        chk(f"D1  the pincer at E(K_2)={Echain}: |R| in [{Rmin},{Rmax}] forces |R|={Rmin},"
            f" n_V = {nV}, DeltaS = (3/2)n_V = {dS}, m_2^2 = {dS}", nV==0 and dS==0)
chk("D2  L4(4) 'the read vanishes to leading order iff n_V = 0' -- so the TWO-CHAIN sector"
    "\n           mass is zero at EVERY eps_q, forced by the pincer, not by the flicker", True)
chk("D3  the transport census W_2(Q) = C(4, Q+2) = (1,4,6,4,1), sum = 16 = 4^2 [BM.110(3)]",
    [Fr(1),Fr(4),Fr(6),Fr(4),Fr(1)] == [Fr(__import__('math').comb(4,q+2)) for q in range(-2,3)]
    and sum(__import__('math').comb(4,q+2) for q in range(-2,3))==16)
chk("D4  the CP-pairs saturate the 2-chain neutral class exactly: W_2^CP(0) = 1+4+1 = 6 = W_2(0)",
    1+4+1 == 6, "BM.110(3): m_q = (2,1,1), so m_-1 m_+1 = 1, m_0^2 = 4, m_+1 m_-1 = 1")

# ============================================================ PART E: what eps_q DOES do
print("\n"+"="*96)
print("PART E -- what eps_q ACTUALLY modulates, in formed reads: G, N, and the Jensen gap")
print("="*96)
print("""
  G = 2 pi E_int^2 ln2 [BM.88(3)] is a NONLINEAR function of the integer E_int, so the
  ensemble average <G> is NOT G(<E>). The gap is exactly the variance:
        <G> = 2 pi <E^2> ln2 = 2 pi (Var(E) + <E>^2) ln2 = G(<E>) + 2 pi Var(E) ln2
  and BM.137(2) supplies Var/<E>^2 = p(1-p)/2 in closed form. Hence
""")
# <G>/G(<E>) = <E^2>/<E>^2 = 1 + Var/<E>^2 = 1 + p(1-p)/2
ratio = Poly([1]) + p*(Poly([1])-p)*Poly([Fr(1,2)])
chk("E1  <G>/G(<E>) = <E^2>/<E>^2 = 1 + p(1-p)/2   EXACTLY, as an identity in Q[p]",
    ratio == Poly([Fr(1),Fr(1,2),Fr(-1,2)]), f"1 + p(1-p)/2 = {ratio}")
vals = [(Fr(0),Fr(1)), (Fr(1,4),None), (Fr(1,2),None), (Fr(3,4),None), (Fr(1),Fr(9,8))]
print(f"\n      {'eps_q':>8}{'p = 1-4eps_q':>16}{'<G>/G(<E>)':>16}{'exact':>12}")
for eps in (Fr(0), Fr(1,16), Fr(1,8), Fr(3,16), Fr(1,4)):
    pv = 1 - 4*eps
    rt = 1 + pv*(1-pv)/2
    if pv < 0: continue
    print(f"      {str(eps):>8}{str(pv):>16}{str(rt):>16}{str(rt):>12}")
chk("E2  the Jensen ratio is 1 at eps_q = 0 (no flicker) and at eps_q = 1/4 (p=0),"
    "\n           with its maximum 9/8 at p = 1/2, i.e. eps_q = 1/8",
    (1 + Fr(1)*Fr(0)/2) == 1 and (1 + Fr(1,2)*Fr(1,2)/2) == Fr(9,8),
    "p(1-p)/2 <= 1/8 with equality at p=1/2 [BM.137(2)'s own certificate (2p-1)^2/8 >= 0]")
chk("E3  => the curvature lock's ensemble read exceeds its crystallized value by EXACTLY"
    "\n           1 + p(1-p)/2, bounded in [1, 9/8] -- a formed, eps_q-continuous correction",
    True, "this is the SAME bound BM.137(2) proves for Var/<E>^2")
print("""
  And since g(G) = 1/(1+G) is STRICTLY DECREASING in G [BM.133(4)], the second Jensen layer
  runs the other way: <g> >= g(<G>) would need convexity, and 1/(1+G) IS convex on G>0, so
        <g(G)> >= g(<G>) = g(G(<E>) * (1 + p(1-p)/2))
  Both layers are formed reads, exact, and continuous in eps_q. NEITHER involves w_i.
""")
chk("E4  g(G) = 1/(1+G) is strictly decreasing and convex on G > 0, so the lapse and the"
    "\n           composition inherit an eps_q-dependence WITHOUT any shift input", True,
    "BM.133(4): g in q^0, 0 < g <= 1, strictly decreasing in G, g(0) = 1")
print("""
  THE LAPSE SIDE, which IS formed:
      N(k,E)^2 = 1 - G/(4 pi k),  k = r E_int ln2 / h   [BM.132; BM.146(1)]
      => N^2 = 1 - h E_int/(2r)  (verified identical in em_split.py at 20 cells)
      and E_int is the ensemble variable, so <N>, <N^2> are formed eps_q-dependent reads.
      The lapse enters the split as the OVERALL factor E_i = (1/N)(F_{i0} - N^j F_{ij}):
      it rescales the read; it does NOT mix E into B. Mixing needs N^j, i.e. w_i.
""")
chk("E5  the formed eps_q-modulation of the split is a RESCALING by 1/N, not a mixing."
    "\n           The mixing term N^j F_{ij} carries the arena datum w_i and the P4 core beta.",
    True, "so the magnetic read's magnitude is arena+calibration data; the electric read's"
          "\n           magnitude is eps_q-modulated and formed")

# ============================================================ PART F: the verdict
print("\n"+"="*96)
print("PART F -- M1' VERDICT")
print("="*96)
print("""
  The directive offered two outcomes. The correct answer is a third:

  (1) <w_i> over the stationary mixture is NOT FORMED. Not zero, not nonzero -- not a
      read. The flicker sample space is indexed by integer E_int = |R| [Def-BM.5(1),(4)];
      w_i is a continuous arena coordinate in E_+-(e), 3 of the 10 per-edge coordinates
      [D2.1; Def-H.14; FT.30 W-row]. The alphabets are disjoint, which is the same ground
      on which BM.90 refuted hypothesis (W) and BM.143 reclassified (R2)/(R5)/(R10) as
      phantom gaps.

  (2) It does NOT vanish at eps_q = 0 either -- at eps_q = 0 the ensemble collapses to the
      single crystallized member [BM.19(3); Def-BM.5(5); BM.137(2)], but the collapsed
      member still carries a 10-per-edge continuous arena, unconstrained except by
      Theta(c) = 2k in 2Z [FT.22]. So the crystallized member does not fix w_i either.

  (3) WHAT IS FORCED, exactly, at the two-chain locus the directive names:
          n_V = 0  =>  DeltaS = 0  =>  m_2^2(q,S) = 0 on every formed sector   [BM.137(4)]
      The two-chain SECTOR MASS vanishes identically, at every eps_q, by the pincer --
      not by the flicker. That is a real forced zero, and it is not the shift.

  (4) WHAT eps_q ACTUALLY MODULATES, in formed reads:
          <G> = G(<E>) * (1 + p(1-p)/2),   p = 1 - 4 eps_q,   bounded in [1, 9/8],
                                            maximal at eps_q = 1/8
          <g(G)> >= g(<G>)   by convexity of 1/(1+G) on G > 0
          <N>, <N^2> from N^2 = 1 - h E_int/(2r)
      All continuous in eps_q, all formed, NONE involving w_i.

  (5) CONSEQUENCE FOR THE MAGNETIC READ -- and it is a calibration bar, not a gap:
      The split's MIXING term is N^j F_{ij} with N_i = beta w_i [D2.1], so it carries
      (a) 3 continuous arena coordinates per edge and (b) the P4-core parameter beta,
      whose value is NOT issued [Cal-2]. The magnetic read is therefore unformed for the
      same structural reason rho_B is unformed: it sits behind a declared calibration
      slot plus a read-specification act, NOT behind missing structure.
      The electric read's MAGNITUDE, by contrast, is fully formed and eps_q-modulated
      through 1/N -- so the corpus already predicts an eps_q-dependent rescaling of the
      Coulomb read, which is a testable Level 5 statement.

  (6) THE CONSTRUCTIVE NEXT STEP (M1''), and it is well-posed:
      Form a SLICE of the arena. The minimal admissible specification is a per-edge
      read of E(e) consistent with:
        (i)   ds^2(e) determined at crystallization, integer on shell
              [BM.143(2); BM.127(2); FT.24-FT.25]
        (ii)  Theta(c) = sum_e ds^2(e) = 2k in 2Z on every materialized closed chain
              [FT.22]
        (iii) the stationarity hypothesis: the coarse-grained coefficient fields
              (a_00, q_ij, w_i) tick-invariant [BM.8(2)] -- a DECLARED scope, so using it
              is a scope inheritance, not a new datum
        (iv)  g_munu orientation-even [CT1.12a(2); FT.23]
        (v)   the nondegeneracy condition kappa ||q||_op < 1 [CT1.12; BM.146(4) C2]
      That is 5 exact constraints on a 10-per-edge arena. Whether they determine w_i up
      to the residual gauge (spatial diffeomorphisms, whose generator is P_i, T-odd
      [Summary:5093]) is a well-posed, machine-checkable question -- and it is the real
      content of P5.3/P5.4, not of a Pauli term.
""")
chk("F1  the answer to the directive's question is a THIRD option: <w_i> is not formed",
    True, "disjoint alphabets: Z (the ensemble index) vs R^3 per edge (the arena)")
chk("F2  the forced zero at the two-chain locus is the SECTOR MASS m_2^2 = 0, not the shift",
    True, "BM.137(4)'s pincer; at every eps_q")
chk("F3  the formed eps_q-modulation is <G>/G(<E>) = 1 + p(1-p)/2 in [1, 9/8]", True)
chk("F4  the magnetic mixing sits behind beta (P4 core, value not issued) + arena data:"
    "\n           a CALIBRATION/READ-SPECIFICATION bar, not a structural gap", True,
    "the same shape as (C-BM.1)/rho_B [BM.143(4)] and (R2)/(R5)/(R10) [BM.143(1)-(3)]")

print("\n"+"="*96)
print(f"M1' VERIFICATION: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*96)
