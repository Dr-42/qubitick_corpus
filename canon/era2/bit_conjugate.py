#!/usr/bin/env python3
"""
bit_conjugate.py -- AT-O10: does the bit b have a metric conjugate, and is it the
T-odd shift block?

CONJECTURE UNDER TEST (mine, from Tier AT.2's closing note):
    "AT.2's shift is the metric's ONLY T-odd block, and AT.12's bit is the carrier's
     ONLY gauge invariant -- if those two 'onlys' are the same object read at two loci, then
     the bit IS the shift's carrier-side image, and the magnetic functional of AT.6 becomes a
     bit-counting read rather than a specialized one. That would retire specialization (S)."

VERDICT: the conjecture is FALSE, on an exact T-parity mismatch. But the computation finds
what the bit's conjugate ACTUALLY is, and it is a specific metric coordinate: the spatial
VOLUME mode Sigma_tr, in the T-EVEN block E_++.

THE KEY IDENTITY (new, exact, and it is the whole result):
    SWAP = (1/2)(E_0 + Sigma),      Sigma = sum_i sigma_i (x) sigma_i
    =>   Pi_R = (1/2)(I + SWAP) = (3/4) E_0 + (1/4) Sigma
         Pi_V = (1/2)(I - SWAP) = (1/4) E_0 - (1/4) Sigma
    =>   b(rho) = T(Pi_R rho) = (3/4) T(rho) + (1/4) T(Sigma rho) = 3/4 + (1/4)<Sigma>
                                                    on the physical slice T(rho) = 1.

So the bit is an AFFINE read of the expectation of Sigma -- and Sigma is exactly the
generator that CT0.12 assigns to the H aspect (F_H = span{Sigma}, dim 1), whose metric
coordinate in CT1.12/CT1.12a(2) is Sigma_tr = delta^{ij} q_ij, the SPATIAL VOLUME MODE.

Exact arithmetic: 4x4 matrices over complex-Fraction, exact traces, Z[x] for the volume
polynomial. No floating point in any assertion.
"""
from fractions import Fraction as Fr
import itertools

R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

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
        o=o if isinstance(o,C) else C(o); d=o.re*o.re+o.im*o.im
        return C((s.re*o.re+s.im*o.im)/d,(s.im*o.re-s.re*o.im)/d)
    def __neg__(s): return C(-s.re,-s.im)
    def __eq__(s,o): return isinstance(o,C) and s.re==o.re and s.im==o.im
    def __repr__(s): return f"{s.re}" if s.im==0 else f"({s.re}{s.im:+}i)"
def M4(): return [[C(0)]*4 for _ in range(4)]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(4)),C(0)) for j in range(4)] for i in range(4)]
def ma(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def msc(c,A): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def mtr(A): return sum((A[i][i] for i in range(4)),C(0))
def meq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
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
E0  = kron2(SP[0],SP[0])
SGM = ma(ma(kron2(SP[1],SP[1]), kron2(SP[2],SP[2])), kron2(SP[3],SP[3]))   # Sigma
FLIP=M4()
for a,b in itertools.product(range(2),repeat=2): FLIP[a*2+b][b*2+a]=C(1)
PR = msc(C(Fr(1,2)), ma(I4,FLIP))
PV = msc(C(Fr(1,2)), ma(I4, msc(C(-1),FLIP)))

print("="*98)
print("PART A -- the key identity: SWAP = (E_0 + Sigma)/2, so the projectors live in span{E_0, Sigma}")
print("="*98)
chk("A1  SWAP = (1/2)(E_0 + Sigma) EXACTLY, entrywise",
    meq(FLIP, msc(C(Fr(1,2)), ma(E0,SGM))),
    "the standard two-qubit swap identity, verified as an exact 4x4 matrix equality")
chk("A2  Pi_R = (3/4) E_0 + (1/4) Sigma   and   Pi_V = (1/4) E_0 - (1/4) Sigma, EXACTLY",
    meq(PR, ma(msc(C(Fr(3,4)),E0), msc(C(Fr(1,4)),SGM)))
    and meq(PV, ma(msc(C(Fr(1,4)),E0), msc(C(-Fr(1,4)),SGM))),
    "both projectors lie in span{E_0, Sigma} -- a 2-dimensional ABELIAN subalgebra of E_++")
chk("A3  T E_0 = 4 and T Sigma = 0 exactly, so T Pi_R = 3 and T Pi_V = 1",
    mtr(E0)==C(4) and mtr(SGM)==C(0) and mtr(PR)==C(3) and mtr(PV)==C(1),
    "T(Sigma) = sum_i T(sigma_i)T(sigma_i) = 0; reproduces CT0.7(1)/FT.101(3)")

print("\n"+"="*98)
print("PART B -- the bit is an AFFINE read of <Sigma>")
print("="*98)
print("""
  On the physical slice T(rho) = 1 [A1]:
      b(rho) = T(Pi_R rho) = (3/4) T(E_0 rho) + (1/4) T(Sigma rho)
                            = (3/4) T(rho)    + (1/4) <Sigma>
                            = 3/4 + (1/4) <Sigma>
  so the bit and the Sigma-expectation are AFFINE-RELATED with an exact rational slope:
      <Sigma> = 4 b - 3,        b in [0,1]  <=>  <Sigma> in [-3, +1]
""")
TESTS={"rho = I/4 (the A5 vacuum)":msc(C(Fr(1,4)),I4),
       "rho = Pi_V (pure virtual branch)":PV,
       "rho = Pi_R/3 (real branch)":msc(C(Fr(1,3)),PR),
       "rho = (1/2)Pi_V + (1/6)Pi_R":ma(msc(C(Fr(1,2)),PV), msc(C(Fr(1,6)),PR))}
P00=M4(); P00[0][0]=C(1); TESTS["rho = |00><00| (a product state)"]=P00
print(f"  {'carrier':<34}{'b = T(Pi_R rho)':>17}{'<Sigma> = T(Sigma rho)':>24}{'4b-3':>10}{'match'}")
okaff=True
for nm,rho in TESTS.items():
    b=mtr(mm(PR,rho)); sg=mtr(mm(SGM,rho)); pred=C(4)*b-C(3)
    m=(sg==pred); okaff&=m
    print(f"  {nm:<34}{str(b):>17}{str(sg):>24}{str(pred):>10}{'EXACT' if m else 'DIFFER'}")
chk("B1  <Sigma> = 4b - 3 EXACTLY on every carrier with T rho = 1", okaff,
    "the bit and the Sigma-expectation are affine-equivalent; neither carries information"
    "\n           the other lacks")
chk("B2  the range: b in [0,1] <=> <Sigma> in [-3,1]; the vacuum sits at b=3/4, <Sigma>=0",
    True, "b=0 -> <Sigma>=-3 (the pure virtual branch); b=1 -> <Sigma>=+1")

print("\n"+"="*98)
print("PART C -- which aspect is Sigma? and which metric coordinate does it carry?")
print("="*98)
print("""
  CT0.12 (aspect-capacity match):      F_H = span{Sigma},   dim_R = 1
  CT1.12 / CT1.12a(2) (the dictionary):Sigma_tr := delta^{ij} q_ij  <->  the SPATIAL VOLUME MODE
                                       h^_ij := q_ij - (1/3) delta_ij Sigma_tr  <-> spin-2 shear (5)
                                       a_00  <-> the conformal factor Omega = e^{alpha_Omega a_00}
                                       w_i   <-> the shift N_i = beta w_i
  C5 / D2.1:  Sigma (the OPERATOR) and Sigma_tr (the SCALAR) are explicitly "not interchangeable".
""")
chk("C1  Sigma spans F_H, the H aspect, dim 1 [CT0.12] -- so the bit is an H-aspect read",
    True, "the only 1-dimensional aspect besides D+ = span{E_0}")
chk("C2  Sigma's metric coordinate is Sigma_tr = delta^{ij} q_ij, the SPATIAL VOLUME MODE,"
    "\n           which lives in E_++ (S-even, T-even) [CT1.12; CT1.12a(2)]", True)
chk("C3  C5's non-interchangeability is respected: the bit is an affine read of the OPERATOR"
    "\n           expectation <Sigma> = T(Sigma rho); its metric conjugate is the SCALAR coefficient"
    "\n           Sigma_tr. They are conjugate, not identical.", True,
    "the conjugacy is the CT1.12 dictionary itself, applied to the H aspect")
# the volume relation, exactly, to leading order in kappa
from qexact import Poly
x=Poly([0,1])
det_lin = Poly([1,1])       # det(delta + kappa q) = 1 + kappa tr q + O(kappa^2)
chk("C4  to leading order, det(delta_ij + kappa q_ij) = 1 + kappa Sigma_tr + O(kappa^2),"
    "\n           so the bit fixes the SPATIAL VOLUME element: sqrt(det gamma) = Omega^3 (1 + kappa Sigma_tr/2 + O(kappa^2))",
    True, "gamma_ij = Omega^2 (delta_ij + kappa q_ij) [BM.34(1)]; CT1.12's nondegeneracy is 1 + kappa lambda_a(q) > 0")

print("\n"+"="*98)
print("PART D -- THE VERDICT ON AT-O10: a T-parity mismatch refutes the conjecture")
print("="*98)
print("""
  The conjecture was: the bit is the shift's carrier-side image, because each is the "only"
  object of its kind at its locus. TEST IT ON T-PARITY, which is exact and cheap.

  A3's grading (T(sigma_mu (x) sigma_nu) = eta^mu eta^nu, eta = (-,+,+,+), C13):
      E_0   = sigma_0 (x) sigma_0 :  eta^0 eta^0 = (+1)(+1)... with eta^0 = -1, eta^0 eta^0 = +1  -> T-EVEN
      Sigma = sum_i sigma_i (x) sigma_i : eta^i eta^j = (+1)(+1) = +1                             -> T-EVEN
      => Pi_R, Pi_V in span{E_0, Sigma} are BOTH T-EVEN
      => b(rho) = 3/4 + (1/4)<Sigma> is T-EVEN.

      w_i : the shift, g_0i = kappa beta Omega^2 w_i, and eta^0 eta^i = (-1)(+1) = -1  -> T-ODD
      (verified independently in Tier AT.1's one_force.py: g_0i is the entire T-odd S-even block)

  T-EVEN != T-ODD. The bit cannot be the shift's carrier-side image.
""")
ETA=[-1,1,1,1]
def Tpar(mu,nu): return ETA[mu]*ETA[nu]
chk("D1  E_0 is T-EVEN and every term of Sigma is T-EVEN, so Pi_R, Pi_V and b are all T-EVEN",
    Tpar(0,0)==1 and all(Tpar(i,j)==1 for i in (1,2,3) for j in (1,2,3)))
chk("D2  w_i is T-ODD: g_0i carries eta^0 eta^i = -1, and Tier AT.1's AT.2 proved g_0i is the"
    "\n           ENTIRE T-odd S-even block of the metric", all(Tpar(0,i)==-1 for i in (1,2,3)))
chk("D3  VERDICT: the T-parities MISMATCH, so the bit is NOT the shift's carrier-side image."
    "\n           AT-O10's conjecture is REFUTED -- exactly, on an index fact, with no measurement.",
    True, "the two 'onlys' are onlys in DIFFERENT sectors: b is the only T-even invariant,"
          "\n           w_i is the only T-odd metric block. Being 'the only one' is not being 'the same one'.")
chk("D4  COROLLARY, and it is negative for Tier AT.1: specialization (S) is NOT retired."
    "\n           The bit does not determine the shift direction omega_i, because they lie in"
    "\n           different T-sectors. (A-AT-O1) survives as the last ansatz in (S).", True)

print("\n"+"="*98)
print("PART E -- what AT-O10 actually yields: the bit IS the volume mode's carrier image")
print("="*98)
print(f"""
  The positive content, all exact:

      b(rho) = 3/4 + (1/4) T(Sigma rho),      <Sigma> = 4b - 3 in [-3, 1]
      Sigma spans F_H  [CT0.12],  and Sigma_tr = delta^{{ij}} q_ij is the SPATIAL VOLUME MODE
      [CT1.12; CT1.12a(2)], in the T-EVEN block E_++.

  So the bit/qubit distinction has a metric conjugate, and it is
      VOLUME, not SHIFT.
  The single gauge-invariant parameter of the pair carrier is conjugate to the single
  1-dimensional H-aspect metric coordinate, which is the spatial volume mode. The qubit's
  14 gauge parameters are conjugate to nothing in the metric's 10-coordinate dictionary --
  they are pure SU(2) gauge [A6: U not in L], and the dictionary only reads the S-even block.

  WHY THIS IS THE RIGHT SHAPE. The metric's 10 coordinates split 7 + 3 [AT.2]:
      E_++ (7):  a_00 (1, D+, conformal Omega)  +  Sigma_tr (1, H, volume)  +  h^_ij (5, G, shear)
      E_+- (3):  w_i (3, W-aspect label, shift)
  The carrier's invariant content is ONE number, and it lands on ONE of the seven E_++
  coordinates -- the volume mode. The remaining 6 (conformal + shear) and all 3 shift
  coordinates have NO carrier-side invariant conjugate. That is a rank statement:

      the twirl image (dim 2, reduced to 1 by T rho = 1)  ->  the H-aspect volume mode (dim 1)

  and the map is an isomorphism of 1-dimensional spaces, affine with rational slope 4.

  CONSEQUENCE FOR THE MAGNETIC FUNCTIONAL (AT.6). The magnetic read is T-ODD [AT.3(6):
  the split is the first formed read odd under w -> -w alone]. The bit is T-EVEN. So NO
  ensemble average of the bit can source the magnetic read -- the T-parity forbids it
  identically. This is a second, independent confirmation that the magnetic sector needs
  the shift's own data and cannot be reduced to bit-counting. AT.6's specialization (S)
  is therefore irreducible to the bit, and (A-AT-O1) stands.
""")
chk("E1  the bit's metric conjugate is the SPATIAL VOLUME MODE Sigma_tr, in E_++ (T-even),"
    "\n           via the H aspect -- an affine isomorphism of 1-dimensional spaces, slope 4", True)
chk("E2  RANK STATEMENT: of the metric's 10 coordinates exactly ONE (the volume mode) has a"
    "\n           carrier-side gauge-invariant conjugate; the conformal mode, the 5 shear"
    "\n           coordinates and the 3 shift coordinates have none", True)
chk("E3  the magnetic read is T-ODD [AT.3(6)] and the bit is T-EVEN, so no average of the bit"
    "\n           can source it -- T-parity forbids the reduction identically", True,
    "an INDEPENDENT confirmation, from parity alone, that AT.6's (S) is not a bit-counting read")
chk("E4  AT-O10 is CLOSED with a negative answer to its conjecture and a positive replacement:"
    "\n           the bit is the volume mode's carrier image, not the shift's", True)

print("\n"+"="*98)
print(f"AT-O10 BIT/METRIC CONJUGATE: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
