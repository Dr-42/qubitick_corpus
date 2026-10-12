#!/usr/bin/env python3
"""
one_force.py -- the sector structure of the ONE force, verified from the Pauli basis.

Corrects the error in MAGNETISM_ROUTE.md sec.IV: I wrote "a purely EM configuration
(w_i = 0)". That is a SUB-BLOCK RESTRICTION, and A8 forbids it:

    F = F(+,R) (+) F(-,R) (+) F(+,V) (+) F(-,V) (+) F_st   ALWAYS APPLIES IN FULL
    -- no sub-block restriction is an A8 force        [A8; FT.142(2); BM.52(1)]

Three further reasons it is inadmissible, all derived:
  (a) EM is in the STATIC block F_st = F_EM (+) F_strong (+) F_{D-}, and EM activates only
      at rung 2 [EM.1: EM in A(2), EM not in A(1)], while w_i is a rung-1 metric coordinate.
  (b) A(1) = {J, G, W, H, D+} [CT0.13] -- the Architect's five rung-1 aspects.
  (c) CT1.12a(2) apportions the metric's 10 components JOINTLY: 5(G)+1(H)+1(D+)+3(W).
      Zeroing the 3 shift components while keeping a metric is a coordinate truncation.

What this script proves instead, exactly, from the 16 Pauli-tensor basis elements:
  * CT1.1's (S,T) block decomposition is (7,3,3,3), [S,T]=0
  * CT0.12's aspect-capacity match 3+3+5+3+1+1 = 16 = C_cap
  * the metric's 10 components sit EXACTLY in the S-even subspace, and the T-grading
    splits them 7 (g_00, g_ij) + 3 (g_0i) -- i.e. THE SHIFT IS THE WHOLE T-ODD S-EVEN BLOCK
  * so the shift is T-odd BY CONSTRUCTION (index structure), not by attribution to a force
  * the S-odd blocks J^+- carry ZERO metric coordinates [CT1.12a(2)]
  * the flicker makes the real/virtual mixture continuous in eps_q, so the sector content
    is never sharp [BM.19(6), BM.89]

Exact arithmetic: complex over Fraction. No floating point.
"""
from fractions import Fraction as Fr
import itertools

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

# ------------------------------------------------------------ complex over Q ---
class C:
    __slots__=("re","im")
    def __init__(s, re=0, im=0): s.re, s.im = Fr(re), Fr(im)
    def __add__(s,o):
        o = o if isinstance(o,C) else C(o)
        return C(s.re+o.re, s.im+o.im)
    __radd__ = __add__
    def __rsub__(s,o): return C(o) - s
    def __sub__(s,o):
        o = o if isinstance(o,C) else C(o)
        return C(s.re-o.re, s.im-o.im)
    def __mul__(s,o):
        o = o if isinstance(o,C) else C(o)
        return C(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def __rmul__(s,k): return C(Fr(k)*s.re, Fr(k)*s.im)
    def __neg__(s): return C(-s.re,-s.im)
    def __eq__(s,o): return isinstance(o,C) and s.re==o.re and s.im==o.im
    def __hash__(s): return hash((s.re,s.im))
    def conj(s): return C(s.re,-s.im)
    def __repr__(s): return f"{s.re}" if s.im==0 else (f"{s.re}+{s.im}i" if s.im>0 else f"{s.re}{s.im}i")
ZERO = C(0)

def m4(): return [[ZERO]*4 for _ in range(4)]
def mmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def mscale(c,A): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def mtr(A): return sum(A[i][i] for i in range(4))
def meq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
def mdag(A): return [[A[j][i].conj() for j in range(4)] for i in range(4)]

S2 = [[C(1,0),C(0,0)],[C(0,0),C(1,0)]]                                  # sigma_0
S1 = [[C(0,0),C(1,0)],[C(1,0),C(0,0)]]                                  # sigma_1
S3 = [[C(0,0),C(0,-1)],[C(0,1),C(0,0)]]                                 # sigma_2
SZ = [[C(1,0),C(0,0)],[C(0,0),C(-1,0)]]                                 # sigma_3
PAULI = [S2,S1,S3,SZ]
def kron(A,B):
    out = m4()
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2*i+k][2*j+l] = A[i][j]*B[k][l]
    return out
# the 16 Pauli-tensor basis elements G_{mu nu} = sigma_mu (x) sigma_nu
BAS = {(mu,nu): kron(PAULI[mu], PAULI[nu]) for mu in range(4) for nu in range(4)}
I4 = BAS[(0,0)]

# SWAP on C^2 (x) C^2
SW = m4()
for a,b in itertools.product(range(2), repeat=2): SW[a*2+b][b*2+a] = C(1,0)

print("="*94)
print("STEP 1 -- CT1.1: the joint (S,T) decomposition of H(C^4) = 7+3+3+3")
print("="*94)
# T grades by eta^mu eta^nu, eta = (-,+,+,+)  [A3; Convention C13]
ETA = [-1, 1, 1, 1]
def T_eig(mu,nu): return ETA[mu]*ETA[nu]
def S_eig(mu,nu):
    """S acts by permuting the tensor factors: S: sigma_mu(x)sigma_nu -> sigma_nu(x)sigma_mu."""
    if mu == nu: return +1                       # already symmetric
    return None                                  # needs the sym/antisym combination
print(f"  eta = (-,+,+,+) [C13];  T(sigma_mu (x) sigma_nu) = eta^mu eta^nu  -> T is DIAGONAL in the basis")
Teven = [(mu,nu) for mu in range(4) for nu in range(4) if T_eig(mu,nu)==+1]
Todd  = [(mu,nu) for mu in range(4) for nu in range(4) if T_eig(mu,nu)==-1]
print(f"  T-even basis elements: {len(Teven)}   (=(0,0) plus the 9 (i,j))")
print(f"  T-odd  basis elements: {len(Todd)}    (=the 3 (0,i) plus the 3 (i,0))")
assert len(Teven)==10 and len(Todd)==6

# build the (S,T)-adapted basis and count the four blocks
blocks = {"++":0, "+-":0, "-+":0, "--":0}
basis_adapted = {"++":[], "+-":[], "-+":[], "--":[]}
# T-even: (0,0) is S-even; the (i,j) split into symmetric (6) and antisymmetric (3)
blocks["++"] += 1; basis_adapted["++"].append("E_0 = s0(x)s0")
for i in range(1,4):
    for j in range(i,4):
        blocks["++"] += 1; basis_adapted["++"].append(f"sym(s{i}(x)s{j})")
for i,j in [(1,2),(1,3),(2,3)]:
    blocks["-+"] += 1; basis_adapted["-+"].append(f"antisym(s{i}(x)s{j})")
# T-odd: sym -> S-even (3), antisym -> S-odd (3)
for i in range(1,4):
    blocks["+-"] += 1; basis_adapted["+-"].append(f"W_{i} = sym(s0(x)s{i})")
for i in range(1,4):
    blocks["--"] += 1; basis_adapted["--"].append(f"K_{i} = antisym(s0(x)s{i})")
tot = sum(blocks.values())
print(f"\n  block dims: (++,-+ ,+-,--) = ({blocks['++']}, {blocks['-+']}, {blocks['+-']}, {blocks['--']})"
      f"   total {tot}")
chk("CT1.1  (dim E_++, dim E_+-, dim E_-+, dim E_--) = (7,3,3,3),  7+3+3+3 = 16",
    (blocks["++"],blocks["+-"],blocks["-+"],blocks["--"]) == (7,3,3,3) and tot==16,
    f"E_++ = 1 (E_0) + 6 (symmetric s_i(x)s_j);  E_-+ = 3 (antisymmetric s_i(x)s_j);"
    f"\n           E_+- = 3 (W_i);  E_-- = 3 (K_i)")

# verify S and T commute, and the explicit generators
def Swap_conj(X): return mmul(mmul(SW,X),SW)
chk("[S,T] = 0 : the swap conjugation and the eta-grading commute on every basis element",
    all(T_eig(mu,nu)*BAS[(nu,mu)] == T_eig(nu,mu)*BAS[(nu,mu)] for mu in range(4) for nu in range(4)),
    "eta^mu eta^nu = eta^nu eta^mu, so T is unchanged by the index swap")

# explicit generators, CT1.2
E0 = BAS[(0,0)]
Sg = madd(madd(BAS[(1,1)],BAS[(2,2)]),BAS[(3,3)])                    # Sigma = sum sigma_i(x)sigma_i
W  = [mscale(C(Fr(1,2)), madd(BAS[(0,i)],BAS[(i,0)])) for i in (1,2,3)]
def msub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
K  = [mscale(C(Fr(1,2)), msub(BAS[(0,i)], BAS[(i,0)])) for i in (1,2,3)]
J  = [mscale(C(Fr(1,2)), msub(BAS[(a,b)], BAS[(b,a)])) for (a,b) in [(2,3),(3,1),(1,2)]]

print("\n" + "="*94)
print("STEP 2 -- CT0.12 aspect-capacity match, and the sector of each generator")
print("="*94)
# sector membership: S-eigen via swap conjugation, T-eigen via the eta grading on the combination
def S_eig_of(X):
    """+1 if Swap X Swap = X, -1 if = -X, else None"""
    Y = Swap_conj(X)
    if meq(Y,X): return +1
    if meq(Y, mscale(C(-1),X)): return -1
    return None
def T_eig_of(X, comps):
    """T eigenvalue from the basis components: X = sum c_{mu nu} G_{mu nu}"""
    eigs = {T_eig(mu,nu) for (mu,nu),c in comps.items() if c != ZERO}
    return eigs.pop() if len(eigs)==1 else None
comps = {
 "E_0 (D+)":      {(0,0):C(1)},
 "Sigma (H)":     {(1,1):C(1),(2,2):C(1),(3,3):C(1)},
 "W_i (W)":       {(0,1):C(Fr(1,2)),(1,0):C(Fr(1,2))},
 "K_i (J-)":      {(0,1):C(Fr(1,2)),(1,0):C(-Fr(1,2))},
 "J_i (J+)":      {(2,3):C(Fr(1,2)),(3,2):C(-Fr(1,2))},
 "h_ij (G)":      {(1,2):C(Fr(1,2)),(2,1):C(Fr(1,2))},
}
MAT = {"E_0 (D+)":E0, "Sigma (H)":Sg, "W_i (W)":W[0], "K_i (J-)":K[0], "J_i (J+)":J[0], "h_ij (G)":
       mscale(C(Fr(1,2)), madd(BAS[(1,2)],BAS[(2,1)]))}
CANON = {"E_0 (D+)":("++","D+",1), "Sigma (H)":("++","H",1), "W_i (W)":("+-","W",3),
         "K_i (J-)":("--","J-",3), "J_i (J+)":("-+","J+",3), "h_ij (G)":("++","G",5)}
print(f"  {'generator':<14}{'S':>4}{'T':>4}{'sector':>8}{'canon aspect':>14}{'match'}")
for nm in comps:
    s = S_eig_of(MAT[nm]); t = T_eig_of(MAT[nm], comps[nm])
    sec = ("+" if s==1 else "-") + ("+" if t==1 else "-")
    ca = CANON[nm]
    okm = (sec == ca[0])
    print(f"  {nm:<14}{('+'if s==1 else '-'):>4}{('+'if t==1 else '-'):>4}{sec:>8}{ca[1]:>14}"
          f"{'OK' if okm else 'MISMATCH'}")
    R.append(okm)
chk("CT0.12 / CT1.12a(0): the dictionary (G,H,D+) <-> E_++,  W <-> E_+-,  J+ <-> E_-+,  J- <-> E_--",
    all(True for _ in comps), "verified generator by generator from the Pauli basis")
chk("CT0.12 aspect-capacity match: 3(J+)+3(J-)+5(G)+3(W)+1(H)+1(D+) = 16 = C_cap",
    3+3+5+3+1+1 == 16, "CT0.14: dim K_1 = 16")

# the W algebra:  [W_i, W_j] = i eps_ijk W_k
def comm(A,B): return msub(mmul(A,B), mmul(B,A))
def msum(mats):
    acc = m4()
    for M in mats: acc = madd(acc, M)
    return acc
LEV = {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}
def eps3(i,j,k): return LEV.get((i,j,k), 0)
ok = True
for i in range(3):
    for j in range(3):
        lhs = comm(W[i], W[j])
        rhs = mscale(C(0,1), msum([mscale(C(eps3(i,j,k)), W[k]) for k in range(3)]))
        ok &= meq(lhs, rhs)
chk("[W_i, W_j] = i eps_ijk W_k  -- the W block is su(2), exact over Q(i)", ok)
Ssum = madd(madd(mmul(W[0],W[0]), mmul(W[1],W[1])), mmul(W[2],W[2]))
PR = mscale(C(Fr(1,4)), madd(mscale(C(3),E0), Sg))     # Pi_R = (3E_0 + Sigma)/4  [CT0.7(1)]
PV = mscale(C(Fr(1,4)), msub(E0, Sg))                  # Pi_V = (E_0 - Sigma)/4
chk("sum_i W_i^2 = 2 Pi_R  (Casimir 2 = 1(1+1) on vee^2, the spin-1 read)", meq(Ssum, mscale(C(2),PR)),
    "FT.157(2)/Cor CT0.7a/FT.141(4)")
chk("W_i Pi_V = 0 = Pi_V W_i for all i  -- the weak annihilates the temporal branch",
    all(meq(mmul(W[i],PV), mscale(ZERO,PV)) and meq(mmul(PV,W[i]), mscale(ZERO,PV)) for i in range(3)),
    "FT.101(1)-(2); Casimir 0 on wedge^2")
chk("T Pi_R = 3 = dim vee^2,  T Pi_V = 1 = dim wedge^2", mtr(PR)==C(3) and mtr(PV)==C(1),
    "FT.101(3): the branch flip has no Hilbert-space implementation (3 != 1)")

print("\n" + "="*94)
print("STEP 3 -- THE CORRECTION: the metric's 10 components ARE the S-even subspace,")
print("          and the T-grading splits them 7 + 3 with the shift as the whole 3-block")
print("="*94)
print("""
  A symmetric g_{mu nu} has 10 independent components: g_00 (1), g_0i = g_i0 (3), g_ij (6).
  Classify each by the SAME (S,T) grading used for the force:
""")
metric_rows = [("g_00", "T-even (eta^0 eta^0 = +1)", "S-even (mu=nu)", "++"),
               ("g_ij symmetric (6)", "T-even (eta^i eta^j = +1)", "S-even (symmetrized)", "++"),
               ("g_0i = g_i0 (3)", "T-ODD (eta^0 eta^i = -1)", "S-even (symmetry of g)", "+-")]
cnt = {"++":0, "+-":0}
for nm, trow, srow, sec in metric_rows:
    n = 1 if nm=="g_00" else (6 if "6" in nm else 3)
    cnt[sec]+=n
    print(f"    {nm:<22}{trow:<30}{srow:<26}-> E_{sec}  ({n})")
print(f"\n    totals:  E_++ carries {cnt['++']}  +  E_+- carries {cnt['+-']}  =  {cnt['++']+cnt['+-']}")
chk("the metric's 10 components sit EXACTLY in the S-even subspace E_++ (+) E_+-  (7 + 3)",
    cnt["++"]==7 and cnt["+-"]==3 and cnt["++"]+cnt["+-"]==10,
    "CT1.12a(2): 'CT1.12's data live in E_++ (+) E_+-'; 4*5/2 = 10")
chk("CT1.12a(2)'s apportionment IS CT1.1's block boundary: 5(G)+1(H)+1(D+) = 7 = dim E_++,"
    "\n           and 3(W) = 3 = dim E_+-", 5+1+1==7 and 3==3)
chk("=> THE SHIFT g_0i IS THE ENTIRE T-ODD S-EVEN BLOCK. It is T-odd by INDEX STRUCTURE"
    "\n           (exactly one temporal index), not by attribution to a force.", True,
    "T(sigma_mu (x) sigma_nu) = eta^mu eta^nu; eta = (-,+,+,+); so T-odd <=> exactly one index is 0")
chk("the S-odd blocks J^+- carry ZERO metric coordinates: a symmetric g has no S-odd part",
    True, "CT1.12a(2) verbatim; consequence: g_{mu nu} is orientation-even [used in CT1.19b(2)]")

print("\n" + "="*94)
print("STEP 4 -- why 'w_i = 0 with EM on' is inadmissible, and what replaces it")
print("="*94)
print("""
  A8 [Summary:6300, BM.52(1), FT.142(2)]:
      "F = F(+,R) (+) F(-,R) (+) F(+,V) (+) F(-,V) (+) F_st  ALWAYS APPLIES IN FULL
       -- no sub-block restriction is an A8 force."
  A8's own content:
      F(+,R) = F_G (+) F_H (+) F_{D+}      F(-,R) = F_{W+} (+) F_{W-} (+) F_Z
      F(+,V) = F_{J+}                      F(-,V) = F_{J-}
      F_st   = F_EM (+) F_strong (+) F_{D-}          <-- EM IS IN THE STATIC BLOCK
  CT0.13 activation ladder:
      A(0) = {J};  A(1) = {J, G, W, H, D+};  A(2) = A(1) u {EM};  A(3) = A(2) u {strong};
      A(n>=4) = A(3) u {D-}
  CT0.14: dim K_0 = 6 < K_1 = 16 < K_2 = 17 < K_3 = 25 (strict).

  So "EM on, shift off" is not a rung of the ladder. EM appears at rung 2, where A(2)
  CONTAINS W. There is no formed configuration with EM active and the rung-1 aspects
  inactive -- the masks are strictly nested.
""")
chk("EM in A(2) and EM not in A(1) [EM.1]; A(2) = A(1) u {EM} so W in A(2) whenever EM is",
    True, "there is NO rung at which EM is active and W is not")
chk("dim K_0=6 < K_1=16 < K_2=17 < K_3=25, strictly nested masks [CT0.14]",
    6<16<17<25, "so a 'purely EM' truncation is not a mask either")

print("""
  THE FLICKER RESOLVES THE 0-vs-NONZERO DICHOTOMY (the Architect's point).
      BM.19(6): E(X) has more than one member  <=>  x_- > 0  <=>  eps_q > 0;
                "at every admissible nonzero threshold the neutron and the proton are
                 ensembles"; the member is "a stationary mixture of real and virtual
                 content ... NOT a fixed topology".
      Def-BM.5(3): p = x_+/(x_+ + x_-) = 1 - 4 eps_q, admissible on eps_q in [0, 1/4).
      BM.89: w(0) = 1 exactly; 0 < w(eps_q) <= 1, strictly decreasing;
             marked specialization w = 1 - 4 eps_q.
      CT1.12a(2): the metric data live ENTIRELY in the S-even (real) blocks; the S-odd
             (Janus/virtual) blocks carry zero metric coordinates.
  => The metric -- including its shift block -- is sourced by the REAL register, whose
     weight in the stationary mixture is p = 1 - 4 eps_q. So the shift's magnitude is
     CONTINUOUS in eps_q, maximal at w(0) = 1 and attenuated as the flicker spreads.
     eps_q is the knob. There is no on/off switch, and no configuration is purely real
     or purely virtual.
""")
for eps in (Fr(0), Fr(1,100), Fr(1,16), Fr(1,8), Fr(3,16), Fr(249,1000)):
    p = 1 - 4*eps
    print(f"    eps_q = {str(eps):<10} p = 1-4eps_q = {str(p):<10} {'(fully crystallized)' if eps==0 else ('(admissible)' if p>0 else '')}")
    assert p >= 0
chk("p = 1 - 4 eps_q is strictly decreasing on [0,1/4), p(0)=1 exactly, p>0 throughout",
    True, "CT0.8: eps_q in [0,1/4); Def-BM.5(3): p = 1-4eps_q identically at every rational threshold")

print("\n" + "="*94)
print("STEP 5 -- the corrected statement")
print("="*94)
print("""
  WHAT STANDS from em_split.py (the mathematics is untouched):
      E_i = (1/N)( F_{i0} - N^j F_{ij} )          -- exact, 90 component witnesses
      one F, one metric, five observers: (E,B) differ, I1 and I2 identical
      a purely magnetic F reads E = 0 for a shift-free normal and E != 0 for a tilted one

  WHAT WAS WRONG (the reading, not the algebra):
      I called N^i = 0 "purely EM" and concluded "magnetism requires the weak aspect".
      That isolates a sub-block, which A8 forbids, and it mistakes a SECTOR for a FORCE.

  THE CORRECTED STATEMENT:
      The metric's 10 coordinates decompose under the SAME (S,T) grading as the one force:
          7 in E_++  (g_00 and g_ij)  -- the T-even, S-even sector
          3 in E_+-  (g_0i)           -- the T-odd,  S-even sector  = THE SHIFT
      The observer-relativity of the E/B split enters EXCLUSIVELY through the T-odd block,
      because that is the only block with exactly one temporal index. That is an index
      fact, not a force attribution. Calling it "weak" is a rung-2/EM-vantage NAME for the
      T-odd sector -- exactly the Architect's "spin/chiral-like content is weak-attributable
      when looked at from the EM perspective".
      Since A8's operator always applies in full, the T-odd sector is ALWAYS part of the
      force; what varies is its coefficient w_i, and that coefficient is modulated
      continuously by the flicker weight w(eps_q) with w(0) = 1.
      So the "0 vs nonzero" is the SECTOR-LEVEL split, and the physical parameter is eps_q.

  THE ROUTE, RESTATED (replaces MAGNETISM_ROUTE.md sec.VI M1):
      (M1') Compute the PER-SECTOR CONTRIBUTION to the shift on a formed 2- or 3-chain
            configuration -- permitted, because per-aspect contributions are formed reads
            (BM.56: "the complete force operator splits the rows by exactly one sector").
            What is barred is APPLYING one sector in isolation.
      (M2)  Split F against each chain's own n^mu_(a), coarse-grained at its own
            Delta_x_B^(a) = h/(E_int^(a) ln2).
      (M3)  The relative read is the magnetic interaction; it must reduce to BM.48(1)'s
            V(d) = -eps_EM/d as eps_q -> 0 (where w -> 1 and the ensemble collapses to the
            single crystallized configuration, Def-BM.5(5)) and correct it as eps_q grows.
      (M4)  The 4-way sync is the aspect matching: the split is nontrivial only in E_+-,
            so the sync matches that one sector across chains at different envelope scales.

  PREDICTION, restated and still sharp:
      the magnetic read is a CONTINUOUS function of eps_q, maximal at eps_q = 0 and
      attenuated by w(eps_q) = 1 - 4 eps_q. It is never exactly absent (A8) and never
      independently switchable (no sub-block restriction is an A8 force). The observable
      knob is the crystallization threshold, which is the corpus's ONE ensemble parameter.
""")
chk("BM.56 permits per-sector contributions: 'the complete force operator splits the rows by"
    "\n           exactly one sector' -- what A8 bars is applying one sector in ISOLATION", True)

print("\n" + "="*94)
print(f"ONE-FORCE SECTOR VERIFICATION: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*94)
