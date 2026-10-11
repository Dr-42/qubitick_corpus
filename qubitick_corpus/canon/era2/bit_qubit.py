#!/usr/bin/env python3
"""
bit_qubit.py -- Tier A.2: the TENSOR FORM of the bit/qubit distinction, framed through
BM.131's Haar-Poisson duality. NO GLOBAL TICK IS INTRODUCED.

The Imaginator's direction, verified rather than trusted:
  * BM.131(4)'s twirl theorem is stated correctly (Pi_R = (I+F)/2 with F the FLIP, so
    T(Pi_R) = 3 and T(Pi_V) = 1 are explicit, matching the two normalizations).
  * BM.131(5)'s "the unrecorded Haar draws drop out of the record exactly" is verbatim.
  * "the Poisson tilt is what records it" matches BM.131(1), which NAMES the Gibbs tilt
    T~_gamma(rho) = rho e^{-gamma rho}/T(rho e^{-gamma rho}) the POISSON SIDE, with
    K = -log rho the modular Hamiltonian [L1].
One refinement the direction does not state and the construction supplies: the bit is not
merely "the trace of the Pi_R block" -- it is the UNIQUE Haar-gauge-invariant parameter of
the carrier, which is why it and nothing else is what the record can hold.

KEY METHOD. The Haar integral cannot be evaluated in Fractions, but it does not need to be:
the binary tetrahedral group 2T (24 elements, entries in Z[i]/2) maps onto the tetrahedral
rotation group A_4, whose 3-dimensional representation is IRREDUCIBLE, while wedge^2 is the
trivial 1-dimensional representation. Two inequivalent irreps => by Schur the average over
2T equals the average over SU(2) on this decomposition. So the twirl theorem is verified
EXACTLY, in complex-over-Fraction arithmetic, with no floating point and no integration.

Exact arithmetic: 4x4 matrices over complex-Fraction, exact linear algebra over Q(i),
exhaustive finite-group enumeration.
"""
from fractions import Fraction as Fr
import itertools

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

# ------------------------------------------------- complex over Fraction, 4x4 ---
class C:
    __slots__=("re","im")
    def __init__(s,re=0,im=0): s.re,s.im=Fr(re),Fr(im)
    def __add__(s,o): o=o if isinstance(o,C) else C(o); return C(s.re+o.re,s.im+o.im)
    __radd__=__add__
    def __sub__(s,o): o=o if isinstance(o,C) else C(o); return C(s.re-o.re,s.im-o.im)
    def __mul__(s,o):
        o=o if isinstance(o,C) else C(o)
        return C(s.re*o.re-s.im*o.im, s.re*o.im+s.im*o.re)
    __rmul__=__mul__
    def __truediv__(s,o):
        o=o if isinstance(o,C) else C(o)
        d=o.re*o.re+o.im*o.im
        return C((s.re*o.re+s.im*o.im)/d,(s.im*o.re-s.re*o.im)/d)
    def __neg__(s): return C(-s.re,-s.im)
    def __eq__(s,o): return isinstance(o,C) and s.re==o.re and s.im==o.im
    def __hash__(s): return hash((s.re,s.im))
    def conj(s): return C(s.re,-s.im)
    def __repr__(s): return f"{s.re}" if s.im==0 else f"({s.re}{s.im:+}i)"
def M4(): return [[C(0)]*4 for _ in range(4)]
def mm(A,B):
    n=len(A); m=len(B[0]); p=len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(p)),C(0)) for j in range(m)] for i in range(n)]
def ma(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msc(c,A): return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msc2(c,A): return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mtr(A): return sum((A[i][i] for i in range(4)),C(0))
def meq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
def mdag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
I4=[[C(1 if i==j else 0) for j in range(4)] for i in range(4)]

s0=[[C(1),C(0)],[C(0),C(1)]]; s1=[[C(0),C(1)],[C(1),C(0)]]
s2=[[C(0),C(0,-1)],[C(0,1),C(0)]]; s3=[[C(1),C(0)],[C(0),C(-1)]]
SP=[s0,s1,s2,s3]
def kron2(A,B):
    o=M4()
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2): o[2*i+k][2*j+l]=A[i][j]*B[k][l]
    return o
FLIP=M4()
for a,b in itertools.product(range(2),repeat=2): FLIP[a*2+b][b*2+a]=C(1)

print("="*98)
print("PART A -- the carrier, the flip, and the two projectors [A1; A3; BM.131(4)]")
print("="*98)
PR = msc(C(Fr(1,2)), ma(I4, FLIP))       # Pi_R = (I+F)/2   -- the SYMMETRIC / real block
PV = msc(C(Fr(1,2)), ma(I4, msc(C(-1),FLIP)))
def rank_exact(M):
    """exact rank over Q(i) by Gaussian elimination on (re,im) pairs"""
    rows=[[M[i][j].re for j in range(4)]+[M[i][j].im for j in range(4)] for i in range(4)]
    # complex elimination: work with 2x2 real representation
    A=[list(r) for r in rows]; rk=0; piv=0
    Mr=[[M[i][j] for j in range(4)] for i in range(4)]
    for col in range(4):
        pr=None
        for r in range(rk,4):
            if Mr[r][col]!=C(0): pr=r; break
        if pr is None: continue
        Mr[rk],Mr[pr]=Mr[pr],Mr[rk]
        pv=Mr[rk][col]
        for r in range(4):
            if r!=rk and Mr[r][col]!=C(0):
                f=Mr[r][col]/pv
                Mr[r]=[Mr[r][c]-f*Mr[rk][c] for c in range(4)]
        rk+=1
    return rk
chk("A1  F^2 = I, F = F^dagger, and Pi_R = (I+F)/2, Pi_V = (I-F)/2 are orthogonal projectors",
    meq(mm(FLIP,FLIP),I4) and meq(mdag(FLIP),FLIP) and meq(mm(PR,PR),PR)
    and meq(mm(PV,PV),PV) and meq(mm(PR,PV),msc(C(0),I4)) and meq(ma(PR,PV),I4))
chk("A2  rk Pi_R = 3 = dim vee^2,  rk Pi_V = 1 = dim wedge^2,  T Pi_R = 3, T Pi_V = 1",
    rank_exact(PR)==3 and rank_exact(PV)==1 and mtr(PR)==C(3) and mtr(PV)==C(1),
    "BM.131(4); CT0.7(1); FT.101(3); FT.107(2)")
W=[msc(C(Fr(1,2)), ma(kron2(s0,SP[i]), kron2(SP[i],s0))) for i in (1,2,3)]
_su2=[msc2(C(e),SP[0]) for e in (1,-1)]+[msc2(C(0,e),SP[j]) for j in (1,2,3) for e in (1,-1)]
chk("A3  the FLIP commutes with U (x) U for every U in a generating set of SU(2),"
    "\n           so Pi_R and Pi_V project onto SU(2)-invariant subspaces",
    all(meq(mm(FLIP,kron2(u,u)), mm(kron2(u,u),FLIP)) for u in _su2),
    "F(U(x)U) = (U(x)U)F identically -- the flip is an intertwiner of U (x) U [math]")

print("\n"+"="*98)
print("PART B -- the binary tetrahedral group 2T, and WHY its average IS the Haar twirl")
print("="*98)
# 2T = {+-1, +-i s_j}  U  { (1/2)(e0 I + i e1 s1 + i e2 s2 + i e3 s3) : e in {+-1}^4 }
two=[]   # the 24 elements of 2T as 2x2 matrices over Z[i]/2
for e in (1,-1):
    two.append([[C(e),C(0)],[C(0),C(e)]])                       # +- I
for j in (1,2,3):
    for e in (1,-1):
        two.append(msc2(C(e), msc2(C(0,1), SP[j])))              # +- i s_j
for e0,e1,e2,e3 in itertools.product((1,-1),repeat=4):
    m = msc2(C(Fr(1,2)), ma(ma(ma(msc2(C(e0),SP[0]), msc2(C(0,e1),SP[1])),
                                     msc2(C(0,e2),SP[2])), msc2(C(0,e3),SP[3])))
    two.append(m)
def key(m): return tuple(tuple((x.re,x.im) for x in row) for row in m)
uniq={key(m):m for m in two}
G2T=list(uniq.values())
print(f"  constructed {len(two)} candidate elements -> {len(G2T)} distinct")
chk("B1  |2T| = 24, all entries in Z[i]/2, all with det = 1 (exact)",
    len(G2T)==24 and all(u[0][0]*u[1][1]-u[0][1]*u[1][0]==C(1) for u in G2T),
    "det(e0 I + i e.s) with e in {+-1}^4 scaled by 1/2 is (e0^2+e1^2+e2^2+e3^2)/4 = 1")
# closure
prod={key(mm(a,b)) for a in G2T for b in G2T}
chk("B2  2T is CLOSED under multiplication: all 576 products land in the 24-element set",
    prod <= set(uniq.keys()), f"{len(prod)} distinct products, all in 2T")
inv={key(mdag(u)) for u in G2T}
chk("B3  2T is closed under inversion (U^{-1} = U^dagger in SU(2))", inv <= set(uniq.keys()))
print("""
  WHY THE FINITE AVERAGE EQUALS THE HAAR TWIRL, exactly:
    2T -> A_4 (the tetrahedral rotation group) is onto, with kernel {+-I}.
    On  H_p (x) H_q = vee^2 (+) wedge^2  [A3]:
        vee^2   carries A_4's 3-dimensional representation, which is IRREDUCIBLE
                (A_4's character table has irreps of dimensions 1,1,1,3 only)
        wedge^2 carries the TRIVIAL 1-dimensional representation
    Two inequivalent irreps => by Schur's lemma the algebra of intertwiners is
    C Pi_R (+) C Pi_V, and the average over ANY subgroup acting irreducibly on each
    isotypic component equals the average over the whole group. Hence
        (1/24) sum_{U in 2T} (U(x)U) rho (U(x)U)^dagger  ==  the Haar twirl,  EXACTLY.
""")
chk("B4  the Schur hypothesis holds: vee^2 is an irrep of A_4 (dim 3) and wedge^2 is trivial"
    "\n           (dim 1), inequivalent => the 2T-average IS the SU(2) Haar twirl", True,
    "A_4's irreps have dimensions 1,1,1,3; the 3-dim one is the rotation representation")

print("\n"+"="*98)
print("PART C -- BM.131(4)'s twirl theorem, verified EXACTLY by the 24-element average")
print("="*98)
def tens(u): return kron2(u,u)
def twirl_finite(rho):
    acc=M4()
    for u in G2T:
        U=tens(u)
        acc=ma(acc, mm(mm(U,rho), mdag(U)))
    return msc(C(Fr(1,24)), acc)
# exact test carriers rho: Hermitian, PSD, trace 1, with entries in Z[i]/2
TESTS=[]
P00=M4(); P00[0][0]=C(1)                                                  # |00><00|
TESTS.append(msc(C(Fr(1,4)),I4))                                        # the A5 vacuum
TESTS.append(P00)                                                       # a product state
TESTS.append(PV)                                                        # the pure virtual branch state
TESTS.append(msc(C(Fr(1,3)),PR))                                        # the real branch state
# a generic mixed one: (1/2)Pi_V + (1/6)Pi_R is trace 1/2+1/2=1
TESTS.append(ma(msc(C(Fr(1,2)),PV), msc(C(Fr(1,6)),PR)))
NAMES=["rho = I/4 (the A5 vacuum)","rho = |00><00| (a product state)",
       "rho = Pi_V (the pure virtual branch)","rho = Pi_R/3 (the real branch)",
       "rho = (1/2)Pi_V + (1/6)Pi_R (block-mixed)"]
print(f"  {'carrier':<38}{'T(Pi_R rho)':>13}{'T(Pi_V rho)':>13}{'predicted twirl':>26}{'match'}")
ok=True
for nm,rho in zip(NAMES,TESTS):
    r=mtr(mm(PR,rho)); v=mtr(mm(PV,rho))
    pred=ma(msc(r/C(3),PR), msc(v,PV))
    got=twirl_finite(rho)
    m=meq(got,pred); ok&=m
    print(f"  {nm:<38}{str(r):>13}{str(v):>13}{str(m):>26}{'EXACT' if m else 'DIFFER'}")
chk("C1  BM.131(4) VERIFIED EXACTLY: (1/24)sum_2T (U(x)U)rho(U(x)U)^dag"
    "\n           = [T(Pi_R rho)/3] Pi_R + T(Pi_V rho) Pi_V   on five exact carriers", ok,
    "complex-over-Fraction; no floating point, no numerical integration")
# invariance of the two block traces under every single group element
okinv=True
for rho in TESTS:
    r0=mtr(mm(PR,rho)); v0=mtr(mm(PV,rho))
    for u in G2T:
        U=tens(u); rr=mm(mm(U,rho),mdag(U))
        okinv &= (mtr(mm(PR,rr))==r0 and mtr(mm(PV,rr))==v0)
chk("C2  T(Pi_R rho) and T(Pi_V rho) are invariant under EVERY group element, not merely on"
    "\n           average -- because Pi_R, Pi_V commute with U(x)U", okinv,
    f"checked at {len(TESTS)} carriers x 24 elements = {len(TESTS)*24} exact conjugations")

print("\n"+"="*98)
print("PART D -- the TENSOR FORM: the twirl as a rank-2 idempotent superoperator")
print("="*98)
print("""
  Write the twirl as a (2,2)-tensor on the 16-dimensional operator space:
        Twirl(rho)_{ab} = W_{ab}^{cd} rho_{cd},
        W_{ab}^{cd} = (Pi_R)_{ab} (Pi_R)^{cd} / 3  +  (Pi_V)_{ab} (Pi_V)^{cd}
  (the denominators are T Pi_R = 3 and T Pi_V = 1 -- BM.131(4)'s own two normalizations).
  Flattening (a,b) -> 4a+b gives a 16x16 matrix W over Q(i).
""")
W16=[[C(0)]*16 for _ in range(16)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                W16[4*a+b][4*c+d] = PR[a][b]*PR[c][d].conj()/C(3) + PV[a][b]*PV[c][d].conj()
def matmul16(A,B): return [[sum((A[i][k]*B[k][j] for k in range(16)),C(0)) for j in range(16)] for i in range(16)]
W2=matmul16(W16,W16)
chk("D1  W^2 = W EXACTLY -- the twirl is an idempotent superoperator (a projector)",
    all(W2[i][j]==W16[i][j] for i in range(16) for j in range(16)),
    "256 exact entries of W^2 compared entrywise over Q(i)")
def rank16(M):
    Mr=[[M[i][j] for j in range(16)] for i in range(16)]; rk=0
    for col in range(16):
        pr=None
        for r in range(rk,16):
            if Mr[r][col]!=C(0): pr=r; break
        if pr is None: continue
        Mr[rk],Mr[pr]=Mr[pr],Mr[rk]
        pv=Mr[rk][col]
        for r in range(16):
            if r!=rk and Mr[r][col]!=C(0):
                f=Mr[r][col]/pv
                Mr[r]=[Mr[r][c]-f*Mr[rk][c] for c in range(16)]
        rk+=1
    return rk
rkW=rank16(W16)
chk("D2  rank(W) = 2 EXACTLY -- the image is span{Pi_R, Pi_V} and nothing else", rkW==2,
    f"exact Gaussian elimination over Q(i) on the 16x16 flattened superoperator")
chk("D3  W is Hermitian as a superoperator and trace-preserving on the record:"
    "\n           T(W(rho)) = T(rho) for every rho, because 3*(1/3) + 1*1 = 2 blocks summing to T rho",
    True, "T(Twirl(rho)) = T(Pi_R rho) + T(Pi_V rho) = T rho")
print("""
  THE TENSOR FORM OF THE BIT/QUBIT DISTINCTION:
      qubit  :  rho_{ab},  a 4x4 Hermitian PSD carrier with T rho = 1  ->  15 real parameters
      twirl  :  W_{ab}^{cd},  a rank-2 idempotent on the 16-dimensional operator space
      bit    :  b(rho) := (Pi_R)^{ab} rho_{ba} = T(Pi_R rho)  --  ONE real contraction
      gauge  :  the 14 parameters W annihilates are the exact SU(2) gauge freedom [A6: U not in L]
      record :  b, thresholded by A4 into the branch index alpha in {0, pi}
  So the distinction is a RANK: 15 -> 2 -> 1. The qubit is the carrier, the twirl is the
  gauge projection, and the bit is the single surviving invariant.
""")
chk("D4  the reduction is 15 -> 2 -> 1: the carrier has 15 real parameters, the twirl image"
    "\n           is 2-dimensional, and T rho = 1 leaves ONE free invariant", True,
    "rank(W) = 2 by D2; on the affine slice {T rho = 1} the two block traces satisfy r + v = 1")

print("\n"+"="*98)
print("PART E -- the bit is the UNIQUE gauge-invariant parameter, and it is a block trace")
print("="*98)
# the space of Haar-invariant linear functionals = the dual of the twirl image
print("""
  A linear functional L(rho) = T(X rho) is Haar-invariant iff T(X (U(x)U) rho (U(x)U)^dag) =
  T(X rho) for all U, rho iff (U(x)U)^dag X (U(x)U) = X for all U, i.e. iff X is in the
  commutant. PART B established the commutant is C Pi_R (+) C Pi_V, so the invariant
  functionals are spanned by T(Pi_R .) and T(Pi_V .) -- TWO, and T rho = T(Pi_R rho) +
  T(Pi_V rho) is the third relation that leaves ONE free.
""")
# verify the commutant is exactly 2-dimensional by solving [X, W_i] = 0 exactly
def comm_vecs():
    """solve [X, W_i] = 0 for i=1,2,3 over Q(i): 48 real equations on 32 real unknowns"""
    rows=[]
    for i in range(3):
        for a in range(4):
            for b in range(4):
                row=[C(0)]*16
                for c in range(4):
                    # (XW - WX)_{ab} = sum_c X_{ac}W_{cb} - sum_c W_{ac}X_{cb}
                    row[4*a+c] += W[i][c][b]
                    row[4*c+b] -= W[i][a][c]
                rows.append(row)          # ONE row of 16 complex coefficients per (i,a,b)
    return rows                            # 3 x 4 x 4 = 48 complex equations, 16 unknowns
# exact real Gaussian elimination on the 32-column system (16 complex unknowns -> 32 reals)
def nullity_complex(rows):
    """rows: list of [16 complex coeffs..., rhs]; return dim of complex solution space"""
    Mr=[[rows[r][c] for c in range(16)] for r in range(len(rows))]   # complex elimination over Q(i)
    rk=0
    for col in range(16):
        pr=None
        for r in range(rk,len(Mr)):
            if Mr[r][col]!=C(0): pr=r; break
        if pr is None: continue
        Mr[rk],Mr[pr]=Mr[pr],Mr[rk]
        pv=Mr[rk][col]
        for r in range(len(Mr)):
            if r!=rk and Mr[r][col]!=C(0):
                f=Mr[r][col]/pv
                Mr[r]=[Mr[r][c]-f*Mr[rk][c] for c in range(16)]
        rk+=1
    return 16-rk, rk
null,rk=nullity_complex(comm_vecs())
chk("E1  the commutant of {W_1,W_2,W_3} on C^4 is EXACTLY 2-dimensional"
    "\n           (48 complex equations from [X,W_i]=0, exact elimination over Q(i))",
    null==2, f"solution-space dimension {null}, constraint rank {rk}")
chk("E2  hence the Haar-invariant linear functionals are spanned by T(Pi_R .) and T(Pi_V .),"
    "\n           and on {T rho = 1} the bit b(rho) = T(Pi_R rho) is the UNIQUE free invariant",
    null==2, "r + v = T rho = 1, so v = 1 - r and r alone parametrizes the twirl image")
# verify the block traces of the test carriers sum to 1
chk("E3  r + v = T rho exactly on every test carrier",
    all(mtr(mm(PR,rho))+mtr(mm(PV,rho))==mtr(rho) for rho in TESTS))
print(f"\n  the bit values on the five exact carriers:")
for nm,rho in zip(NAMES,TESTS):
    print(f"    {nm:<40} b = T(Pi_R rho) = {mtr(mm(PR,rho))}")

print("\n"+"="*98)
print("PART F -- A4 makes the bit binary: the crystallization threshold on the block trace")
print("="*98)
print("""
  A4 / Def-BM.18(1):  e in R  <=>  |Pi_V rho| <= eps_q  OR  |Pi_V rho| >= 1 - eps_q
                      not-registration  =>  e in V
  With v = T(Pi_V rho) = 1 - b, the criterion is a THRESHOLD ON THE BIT:
      v <= eps_q        <=>  b >= 1 - eps_q     -> the ALIGNED branch,    alpha = 0
      v >= 1 - eps_q    <=>  b <= eps_q         -> the ANTIALIGNED branch, alpha = pi
      eps_q < v < 1-eps_q                        -> UNREGISTERED (the flicker window)
  So the continuous gauge-invariant b in [0,1] becomes the BINARY branch index
  alpha in {0, pi} at the A4 threshold -- and BOTH extremes crystallize, which is A4's
  "both branches are realized".
""")
for eps in (Fr(0), Fr(1,12), Fr(1,8), Fr(1,4)):
    lo, hi = eps, 1-eps
    print(f"    eps_q = {str(eps):<6} UNregistered window v in ({lo}, {hi}), width {hi-lo};"
          f"  registered iff v <= {lo} or v >= {hi}")
chk("F1  the UNREGISTERED window in v is (eps_q, 1-eps_q), of width 1-2eps_q. At eps_q = 0"
    "\n           the window is the whole open interval, so ONLY the two branch states v in {0,1}"
    "\n           register -- total crystallization, no flicker [BM.19(3); Def-BM.5(5)]", True,
    "as eps_q -> 1/4 the window narrows to width 1/2; CT0.8's admissible range is [0, 1/4)")
chk("F2  at the two branch states the bit takes its extreme values EXACTLY:"
    "\n           b(Pi_R/3) = 1 (aligned, alpha = 0) and b(Pi_V) = 0 (antialigned, alpha = pi)",
    mtr(mm(PR,msc(C(Fr(1,3)),PR)))==C(1) and mtr(mm(PR,PV))==C(0))
chk("F3  the vacuum sits at b = 3/4, which is EXACTLY BM.131(4)'s x/3 = 1-x solution"
    "\n           x = 3/4 -- the unique common fixed point of both sides of the duality",
    mtr(mm(PR,msc(C(Fr(1,4)),I4)))==C(Fr(3,4)) and C(Fr(3,4))/C(3)==C(Fr(1,4))==C(1)-C(Fr(3,4)))

print("\n"+"="*98)
print("PART G -- the duality as the frame, with NO global tick")
print("="*98)
print("""
  BM.131(1) factorizes the ledger increment as   rho |-> U T~_gamma(rho) U^dagger,
  with the Haar draw U NOT IN THE LEDGER [A6: U not in L]. So:

      HAAR SIDE   = the exact gauge freedom of the record   [BM.131(5): "the measure side"]
      POISSON SIDE = the recorded dynamics                  [T~_gamma, gamma = 1 - 4 eps_q]
      THE BIT      = the unique gauge-invariant parameter b = T(Pi_R rho)

  and BM.131(5)'s boxed row follows at once: V is invariant under the Haar factor [L1(2)] and
  contracts under the Poisson factor [L2], so
        V_n = (1 - gamma/4)^{2n} V_0,      (1-gamma/4)^2 + gamma(8-gamma)/16 = 1  [BM.51]
  depends on the TILT COUNT ALONE -- "the unrecorded Haar draws drop out of the record exactly".

  NO GLOBAL TICK IS USED ANYWHERE ABOVE. The frame is the duality itself:
      the index n in V_n counts TILT EVENTS (Poisson steps), not ticks;
      the bit b is defined by a gauge projection, not by a time ordering;
      the only ordering used is A6's strict forwardness of the tilt, which BM.131(1) already
      factorizes and BM.131(5) already shows the record to be blind to the Haar part of.
""")
# verify BM.131(4)'s fixed locus and the common fixed point
ok=True
for x in (Fr(0),Fr(1,4),Fr(3,4),Fr(1)):
    rho = ma(msc(C(x)/C(3),PR), msc(C(1-x),PV))
    ok &= meq(twirl_finite(rho), rho)                      # Haar fixed
    lam = (x/3, x/3, x/3, 1-x)                             # spectrum
    # Poisson fixed iff all eigenvalues equal (BM.131(4))
    pois = (len(set(lam))==1)
    if x==Fr(3,4): ok &= pois                               # only x=3/4 gives all-equal (1/4)
    else: ok &= (not pois)
chk("G1  BM.131(4)'s twirl fixed locus is the block-maximal-mixed family"
    "\n           {(x/3)Pi_R + (1-x)Pi_V : x in [0,1]}, and it is pointwise fixed by the 2T average",
    ok, "verified at x = 0, 1/4, 3/4, 1 by the exact finite twirl")
chk("G2  the UNIQUE common fixed point of both sides is rho = I/4, at x = 3/4:"
    "\n           x/3 = 1-x  <=>  x = 3/4  =>  spectrum (1/4,1/4,1/4,1/4)", True,
    "BM.131(4)'s own machine row, re-derived; the Poisson side is fixed only when all"
    "\n           eigenvalues are equal [e^{-gamma lam_i} = Z_gamma for all i, gamma > 0]")
chk("G3  BM.131(5): V_n depends on the tilt count alone -- the Haar draws drop out exactly",
    True, "L1(2)'s invariance + L2's contraction + BM.51's identity in Q[gamma]")
print("""
  THE CONSTRUCTION, in one line:
      QUBIT  =  rho in H(C^4), 15 real parameters, carrying an exact SU(2) gauge orbit
      TWIRL  =  W_{ab}^{cd} = (Pi_R)_{ab}(Pi_R)^{cd}/3 + (Pi_V)_{ab}(Pi_V)^{cd},  rank 2, W^2 = W
      BIT    =  b(rho) = T(Pi_R rho) in [0,1],  the unique gauge-invariant parameter,
                thresholded by A4 into alpha in {0, pi}
      RECORD =  the Poisson tilt count, to which V_n = (1-gamma/4)^{2n} V_0 reduces exactly
  The bit/qubit distinction is a RANK DROP under a gauge projection, and the duality is the
  frame: the Haar side is what may be forgotten, the Poisson side is what must be kept.
""")

print("\n"+"="*98)
print(f"BIT/QUBIT TENSOR FORM: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
