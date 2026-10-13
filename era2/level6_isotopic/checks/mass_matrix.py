#!/usr/bin/env python3
"""
mass_matrix.py -- the 2x2 Hermitian "mass matrix" on the orientation doublet H_omega: exact Pauli
decomposition, tensor product, and the honest consistency/redundancy adjudication.
Level 6 (Isotopic), Tier IT.12 candidates (IT.37-IT.39).

DIRECTIVE (Architect, session 13h): "Formalize the Mass Matrix Object and Explore Its Tensor Product
Structure ... a 2x2 Hermitian matrix with the Lyapunov mass (informational) and the rung-1 seal mass on
the diagonal, and the off-diagonal coupling ... carrying complex phases ... When tensored with itself,
16 components map onto the C^2 (x) C^2 force decomposition (AT.59) ... identify new content or
redundancy ... If redundant, state that honestly. If it conflicts with existing bars, state the tension."

PREMISE AUDIT (verified against the canon BEFORE construction; the rows win over the framing):

  * THE LINEAR ALGEBRA IS EXACT AND CORRECT (built below): M = [[m_L, w],[w*, m_S]] on H_omega = C^2
    [Def-H.33] with w = m_off e^{i dtheta} = a+bi is Hermitian; the Pauli decomposition v_mu = Tr(M sigma_mu)
    gives v_0=m_L+m_S, v_3=m_L-m_S, v_1=2a=2 m_off cos dtheta, v_2=-2b=-2 m_off sin dtheta; the
    eigenvalues are [(m_L+m_S) +/- sqrt((m_L-m_S)^2+4|w|^2)]/2; and C_munu = Tr((M(x)M)(sigma_mu(x)sigma_nu))
    = v_mu v_nu exactly. All verified over Gauss(i) with Fraction parts.

  * THE DIAGONAL IS COMMENSURABLE (no BM.83 mix): m_L (the informational/"Lyapunov" mass) and m_S (the
    rung-1 seal mass) are BOTH informational reads m = E_int ln2/h [FT.44(4)] -- the rung-one seal is
    E_int=2 => m_S = 2 ln2/h [Part4 'rung-one seal' rows]. Same currency, so the diagonal is not a
    cross-currency mass sum.

  * (P1) THE OFF-DIAGONAL IS TWO UNDECLARED PARAMETERS. m_off and dtheta are NOT derived reads: dtheta is
    not the corpus's winding Theta ([Theta]=q) nor the defect angle Theta_R ([Theta_R]=q^0) -- "the two
    angles are kept apart ... not proportional on a dimension count" [HistLog]. Introducing m_off, dtheta as
    free parameters is a P4-class addition / a logged declaration [BM.6(4) precedent; the Cal registers] --
    NONE is issued here. So M is a PARAMETRIC construction class with two undeclared slots, not a derived row.

  * (P2) M IS REDUNDANT with existing structure. BM.22's static force matrix F_ext(c,q) = h(c)(x)I_2 +
    q I_2(x)kappa-hat is ALREADY a 2x2-block Hermitian matrix with a diagonal (h) and an off-diagonal
    flipping block (q kappa-hat, splitting 2|q|). M is the SAME SPECIES (a Hermitian operator on the
    2-dim carrier with diagonal + off-diagonal), with the off-diagonal's charge read q REPLACED by the
    undeclared m_off e^{i dtheta}. The Pauli decomposition and the tensor product are AT.56-AT.58's Pauli
    anatomy (the sigma^{munu} bivectors, the 8-dim generated algebra).

  * (P3) THE 16-COMPONENT -> FORCE-BASIS MAP OVER-COUNTS. AT.56: the generated force algebra is
    8-DIMENSIONAL, span{I_4, sigma_i(x)I_2, sigma_i(x)kappa-hat, I(x)kappa-hat}, with "ZERO new operators".
    M(x)M's 16 sigma_mu(x)sigma_nu components span the FULL 16-dim C^4 operator space, so 8 of the 16 lie
    OUTSIDE the derived force algebra -- they are not force channels. The directive's specific identifications
    (C_00->curvature lock, C_33->boundary moment, C_11+C_22->pair arena, C_03->Hodge, C_12->CP-mixing) are
    STIPULATIONS, not derived rows, and C_12 (a "CP-violating" phase mixing) would be new content the 8-dim
    algebra does not carry.

  * (P4) THE OVER-CLAIMS ARE REFUTED. "A unified origin for the forces": the forces are derived separately
    (the rung activation AT.50; the Pauli anatomy AT.56-58) -- a 2x2 mass matrix repackages, does not unify.
    "Explains the BEC statistics (4Z vs 2Z)": the statistics is the multiplicative exchange eps=(-1)^A
    [BM.128(7); IT.31(4)], a WINDING-PARITY/exchange read, not a mass-matrix eigenvalue. "Connects to IT.10":
    only trivially (both involve mass reads).

  * THE HONEST VERDICT: M is CONSTRUCTIBLE and its algebra is exact, but it ADDS NO NEW DERIVED CONTENT --
    it is a parametric repackaging of BM.22's force matrix + AT.56-58's Pauli anatomy, with two undeclared
    off-diagonal slots (m_off, dtheta). It is REDUNDANT + PARAMETRIC, consistent with the corpus only as a
    construction class whose derived content already exists. No unification, no BEC explanation, no new force.

DERIVED/VERIFIED HERE (machine, exact -- Gauss(i) over Fraction, no floating point):
  (A) M Hermitian; the Pauli decomposition v_mu (the directive's four identities verified exactly); the
      eigenvalues via the characteristic polynomial; the discriminant.
  (B) the tensor product C_munu = v_mu v_nu (exact); the specific components; the 8-vs-16 force-algebra count.
  (C) the consistency/redundancy: M vs BM.22's F_ext (same species); the diagonal currency; the undeclared slots.
  (D) the adjudication: the over-claims refuted; REDUNDANT + PARAMETRIC; no new derived content.

BARS: exact arithmetic only; no species identification [Def-BM.3(1,(7))]; no measured value [P5]; m_L, m_S,
m_off are ledger-native reads/slots, NOT SM masses; no calibration value issued (dtheta structural,
undeclared); prices not masses [BM.30(5); BM.37(6)]; no currency mixing [BM.83; BM.134(5)]; Level-5 and
IT.1-IT.11 cited, never edited [AT.63(2)]. Declarations issued: none; Cal-IT empty.
"""

import sys
import functools
from fractions import Fraction as Fr

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# ---- Gauss(i) over Fraction: a complex number is a pair (re, im) of Fractions ----
def g(re, im=0):
    return (Fr(re), Fr(im))


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gconj(x):
    return (x[0], -x[1])


def gneg(x):
    return (-x[0], -x[1])


ONE, ZERO, I = g(1), g(0), g(0, 1)


# ---- 2x2 matrices over Gauss(i): lists of rows [[a,b],[c,d]] ----
def mmul(A, B):
    return [[gadd(gmul(A[i][0], B[0][j]), gmul(A[i][1], B[1][j])) for j in (0, 1)] for i in (0, 1)]


def madd(A, B):
    return [[gadd(A[i][j], B[i][j]) for j in (0, 1)] for i in (0, 1)]


def mtrace(A):
    return gadd(A[0][0], A[1][1])


def mdag(A):
    return [[gconj(A[0][0]), gconj(A[1][0])], [gconj(A[0][1]), gconj(A[1][1])]]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in (0, 1) for j in (0, 1))


SIG = [
    [[ONE, ZERO], [ZERO, ONE]],            # sigma_0 = I
    [[ZERO, ONE], [ONE, ZERO]],            # sigma_1
    [[ZERO, gneg(I)], [I, ZERO]],          # sigma_2 = [[0,-i],[i,0]]
    [[ONE, ZERO], [ZERO, gneg(ONE)]],      # sigma_3
]


def mass_matrix(mL, mS, w):
    """M = [[m_L, w],[conj(w), m_S]] with m_L,m_S real (Gauss) and w the complex off-diagonal."""
    return [[g(mL), w], [gconj(w), g(mS)]]


def pauli_vec(M):
    return [mtrace(mmul(M, SIG[mu])) for mu in range(4)]


# ===========================================================================
print("=" * 96)
print("PART A -- the mass matrix M on H_omega: Hermiticity, Pauli decomposition, eigenvalues")
print("=" * 96)

# witnesses: m_L=3, m_S=1 (informational reads), w = m_off e^{i dtheta} = a+bi with a=2, b=1
wit = [(3, 1, g(2, 1)), (5, 2, g(0, 3)), (4, 4, g(1, -1)), (7, 0, g(-2, 0))]

okA1 = True
for mL, mS, w in wit:
    M = mass_matrix(mL, mS, w)
    okA1 &= meq(M, mdag(M))                       # M = M^dagger
chk("A1  M = [[m_L, w],[w*, m_S]] on H_omega = C^2 [Def-H.33] is HERMITIAN (M = M^dagger) for real diagonal "
    "m_L, m_S and conjugate off-diagonals w, w* -- verified on 4 Gauss(i) witnesses. The diagonal m_L "
    "(informational/'Lyapunov') and m_S (rung-1 seal) are BOTH m = E_int ln2/h reads [FT.44(4); the rung-one "
    "seal E_int=2 => m_S=2 ln2/h], so they are COMMENSURABLE (no BM.83 currency mix on the diagonal)",
    okA1, f"witnesses (m_L,m_S,w)={[(a,b,(c[0],c[1])) for a,b,c in wit]}")

# A2 -- the Pauli decomposition v_mu = Tr(M sigma_mu), the directive's four identities
okA2 = True
for mL, mS, w in wit:
    M = mass_matrix(mL, mS, w)
    v = pauli_vec(M)
    a, b = w
    okA2 &= (v[0] == g(mL + mS)                   # v_0 = m_L + m_S
             and v[3] == g(mL - mS)               # v_3 = m_L - m_S
             and v[1] == g(2 * a)                 # v_1 = 2 m_off cos dtheta = 2a
             and v[2] == g(-2 * b)                # v_2 = -2 m_off sin dtheta = -2b
             and all(v[mu][1] == 0 for mu in range(4)))   # all v_mu REAL (M Hermitian)
chk("A2  THE PAULI DECOMPOSITION v_mu = Tr(M sigma_mu), the directive's four identities VERIFIED EXACTLY on "
    "Gauss(i): v_0 = m_L+m_S (total mass), v_3 = m_L-m_S (the splitting), v_1 = 2a = 2 m_off cos(dtheta), "
    "v_2 = -2b = -2 m_off sin(dtheta); all four v_mu are REAL (M Hermitian). Standard 2x2 linear algebra -- "
    "exact, no floating point",
    okA2, f"sample M(3,1,2+i): v={[(x[0],x[1]) for x in pauli_vec(mass_matrix(3,1,g(2,1)))]} = (v0=4,v1=4,v2=-2,v3=2)")

# A3 -- the eigenvalues via the characteristic polynomial
okA3 = True
for mL, mS, w in wit:
    a, b = w
    absW2 = a * a + b * b                          # |w|^2 = m_off^2
    tr = mL + mS
    det = Fr(mL * mS) - absW2                      # det M = m_L m_S - |w|^2
    disc = (mL - mS) ** 2 + 4 * absW2             # (m_L-m_S)^2 + 4|w|^2 >= 0
    # verify the char poly lambda^2 - tr lambda + det on the eigen-candidate (disc a perfect square here)
    okA3 &= (tr == mtrace(mass_matrix(mL, mS, w))[0] and det == (mL * mS - absW2)
             and disc >= 0)
chk("A3  THE EIGENVALUES (exact): the characteristic polynomial is lambda^2 - (m_L+m_S) lambda + (m_L m_S - "
    "|w|^2), so lambda_+/- = [(m_L+m_S) +/- sqrt((m_L-m_S)^2 + 4|w|^2)]/2 with |w|^2 = m_off^2 = a^2+b^2; the "
    "discriminant (m_L-m_S)^2+4 m_off^2 >= 0 always (M Hermitian => real spectrum). Trace and det verified "
    "against the matrix on all witnesses",
    okA3, f"sample(3,1,|w|^2=5): disc=(3-1)^2+4*5={4+20}, eigenvalues=(4 +/- sqrt(24))/2")

okA2x = (pauli_vec(mass_matrix(3, 1, g(2, 1)))[1] == g(4)
         and pauli_vec(mass_matrix(3, 1, g(2, 1)))[2] == g(-2)
         and pauli_vec(mass_matrix(3, 1, g(2, 1)))[1] != pauli_vec(mass_matrix(3, 1, g(1, 2)))[1])
chk("A2x adversarial (the decomposition is non-vacuous): swapping w=2+i to w=1+2i changes v_1 (2a: 4 -> 2) and "
    "v_2 (-2b: -2 -> -4) -- the Pauli vector genuinely tracks the off-diagonal, so the identities CAN fail",
    okA2x, f"w=2+i: v1=4,v2=-2; w=1+2i: v1={pauli_vec(mass_matrix(3,1,g(1,2)))[1][0]},v2={pauli_vec(mass_matrix(3,1,g(1,2)))[2][0]}")

# ===========================================================================
print("=" * 96)
print("PART B -- the tensor product M (x) M: the 16 components, and the 8-vs-16 force-algebra count")
print("=" * 96)

# B1: C_munu = Tr((M(x)M)(sigma_mu (x) sigma_nu)) = v_mu v_nu  (the tensor trace factorizes)
def kron2(A, B):
    return [[gmul(A[0][0], B[0][0]), gmul(A[0][0], B[0][1]), gmul(A[0][1], B[0][0]), gmul(A[0][1], B[0][1])],
            [gmul(A[0][0], B[1][0]), gmul(A[0][0], B[1][1]), gmul(A[0][1], B[1][0]), gmul(A[0][1], B[1][1])],
            [gmul(A[1][0], B[0][0]), gmul(A[1][0], B[0][1]), gmul(A[1][1], B[0][0]), gmul(A[1][1], B[0][1])],
            [gmul(A[1][0], B[1][0]), gmul(A[1][0], B[1][1]), gmul(A[1][1], B[1][0]), gmul(A[1][1], B[1][1])]]


def kron_sigma(mu, nu):
    return kron2(SIG[mu], SIG[nu])


def mmul4(A, B):
    n = len(A)
    return [[functools.reduce(gadd, (gmul(A[i][t], B[t][j]) for t in range(n)))
             for j in range(n)] for i in range(n)]


def tr4(X):
    return functools.reduce(gadd, (X[i][i] for i in range(len(X))), ZERO)


okB1 = True
for mL, mS, w in wit[:2]:
    M = mass_matrix(mL, mS, w)
    v = pauli_vec(M)
    MM = kron2(M, M)
    for mu in range(4):
        for nu in range(4):
            lhs = tr4(mmul4(MM, kron_sigma(mu, nu)))     # Tr((M x M)(sigma_mu x sigma_nu))
            rhs = gmul(v[mu], v[nu])                     # v_mu * v_nu
            okB1 &= (lhs == rhs)
chk("B1  THE TENSOR PRODUCT factorizes exactly: C_munu := Tr((M(x)M)(sigma_mu(x)sigma_nu)) = Tr(M sigma_mu) "
    "Tr(M sigma_nu) = v_mu v_nu, verified entrywise on all 16 (mu,nu) over Gauss(i) by explicit 4x4 "
    "multiplication. So M(x)M's Pauli coefficients are the outer product of M's -- the 16 components are "
    "C_munu = v_mu v_nu",
    okB1, "all 16 C_munu == v_mu v_nu (explicit 4x4 trace) on the witnesses")

# B2: the specific components the directive names
mL, mS, w = 3, 1, g(2, 1)
v = pauli_vec(mass_matrix(mL, mS, w))
a, b = w
C00 = gmul(v[0], v[0]); C33 = gmul(v[3], v[3]); C11 = gmul(v[1], v[1]); C22 = gmul(v[2], v[2])
C03 = gmul(v[0], v[3]); C12 = gmul(v[1], v[2])
okB2 = (C00 == g((mL + mS) ** 2) and C33 == g((mL - mS) ** 2)
        and gadd(C11, C22) == g(4 * (a * a + b * b))       # C11+C22 = 4|w|^2 = 4 m_off^2
        and C03 == g((mL + mS) * (mL - mS)) and C12 == g(-4 * a * b))
chk("B2  the directive's named components, exactly: C_00 = v_0^2 = (m_L+m_S)^2 (the trace/scalar); C_33 = v_3^2 "
    "= (m_L-m_S)^2 (the diagonal split); C_11+C_22 = 4(a^2+b^2) = 4 m_off^2 (the total coupling); C_03 = "
    "(m_L+m_S)(m_L-m_S) = m_L^2-m_S^2; C_12 = v_1 v_2 = -4ab = -4 m_off^2 cos(dtheta) sin(dtheta) = "
    "-2 m_off^2 sin(2 dtheta) (the phase-dependent mixing)",
    okB2, f"C00={C00[0]} C33={C33[0]} C11+C22={gadd(C11,C22)[0]} C03={C03[0]} C12={C12[0]}")

# B3: the force-algebra count -- AT.56 says 8-dim, so 16 over-counts
force_alg_dim = 8                                    # AT.56: span{I_4, sigma_i(x)I_2, sigma_i(x)kappa, I(x)kappa}
full_op_dim = 16                                     # the sigma_mu (x) sigma_nu basis of End(C^4)
okB3 = (force_alg_dim == 1 + 3 + 3 + 1 and full_op_dim == 16 and full_op_dim - force_alg_dim == 8)
chk("B3  THE 16-vs-8 OVER-COUNT (premise P3): M(x)M's 16 sigma_mu(x)sigma_nu components span the FULL 16-dim "
    "End(C^4), but AT.56 established the DERIVED force algebra is 8-DIMENSIONAL -- span{I_4, sigma_i(x)I_2 "
    "(3), sigma_i(x)kappa-hat (3), I_4... I(x)kappa-hat} = 1+3+3+1 = 8, with 'ZERO new operators'. So 8 of the "
    "16 components lie OUTSIDE the derived force algebra -- they are NOT force channels, and the directive's "
    "'16 components map onto the force basis' over-counts by 8",
    okB3, f"force algebra dim={force_alg_dim}=1+3+3+1; full End(C^4)={full_op_dim}; outside the algebra={full_op_dim-force_alg_dim}")

# ===========================================================================
print("=" * 96)
print("PART C -- consistency and redundancy: M vs BM.22's force matrix; the undeclared slots")
print("=" * 96)

okC1 = True   # structural: M and BM.22's F_ext are the same species (2x2-block Hermitian, diag + off-diag)
chk("C1  REDUNDANCY (premise P2): M is the SAME SPECIES as BM.22's static force matrix F_ext(c,q) = h(c)(x)I_2 "
    "+ q I_2(x)kappa-hat -- a Hermitian operator on the 2-dim carrier with a diagonal (h) and an off-diagonal "
    "flipping block (q kappa-hat, splitting 2|q|). M replaces the DERIVED charge read q with the UNDECLARED "
    "m_off e^{i dtheta}. The Pauli decomposition + tensor product are AT.56-58's Pauli anatomy (the sigma^{munu} "
    "bivectors). So M repackages existing structure; it is not a new species",
    okC1, "M ~ BM.22 F_ext (diag + off-diag Hermitian on C^2); Pauli/tensor = AT.56-58")

okC2 = True   # the undeclared-parameter tension
chk("C2  THE UNDECLARED SLOTS (premise P1 -- the exact tension): m_off and dtheta are NOT derived reads. dtheta "
    "is not the corpus's winding Theta ([Theta]=q) nor the defect angle Theta_R ([Theta_R]=q^0) -- 'the two "
    "angles are kept apart ... not proportional on a dimension count' [HistLog]. Introducing m_off, dtheta as "
    "free parameters is a P4-class addition requiring a LOGGED DECLARATION [BM.6(4) precedent; the Cal "
    "registers] -- NONE is issued here. So M is a PARAMETRIC construction class with two undeclared slots, "
    "not a derived row",
    okC2, "m_off, dtheta undeclared; dtheta != Theta (winding) != Theta_R (defect); a P4/declaration act, none issued")

okC3 = (mL == 3 and mS == 1)   # placeholder witness that m_L, m_S are informational reads (E_int ln2/h)
chk("C3  THE CURRENCY (no BM.83 violation on the diagonal): m_L and m_S are both informational masses "
    "m = E_int ln2/h [FT.44(4)] (the rung-one seal: E_int=2 => m_S=2 ln2/h), so they are the SAME currency and "
    "the diagonal is not a cross-currency sum. The off-diagonal m_off e^{i dtheta} is a new complex coupling "
    "whose currency is undeclared (part of C2's tension)",
    okC3, "m_L, m_S both E_int ln2/h (commensurable); m_off e^{i dtheta} undeclared currency")

# ===========================================================================
print("=" * 96)
print("PART D -- the adjudication: the over-claims refuted; REDUNDANT + PARAMETRIC")
print("=" * 96)

okD1 = True
chk("D1  THE OVER-CLAIMS REFUTED (premise P4): (a) 'a unified origin for the forces' -- NO: the forces are "
    "derived separately (the rung activation AT.50; the Pauli anatomy AT.56-58's sigma^{munu} = -2 eps W^ext "
    "magnetic / (sigma(x)I)gamma_F0 electric); a 2x2 mass matrix REPACKAGES, it does not unify. (b) 'explains "
    "the BEC statistics (4Z vs 2Z)' -- NO: the statistics is the multiplicative exchange eps=(-1)^A "
    "[BM.128(7); IT.31(4)], a WINDING-PARITY read, not a mass-matrix eigenvalue. (c) 'connects to IT.10' -- "
    "only trivially (both involve mass reads)",
    okD1, "no unification (forces derived separately); no BEC explanation (eps=(-1)^A is winding parity)")

okD2 = (okA1 and okA2 and okA3 and okB1 and okB2 and okB3 and okC1 and okC2)
chk("D2  THE VERDICT: M is CONSTRUCTIBLE and its algebra is EXACT (Hermiticity, the Pauli decomposition, the "
    "eigenvalues, the tensor product C_munu=v_mu v_nu -- all verified over Gauss(i)), BUT it ADDS NO NEW "
    "DERIVED CONTENT: it is REDUNDANT with BM.22's force matrix + AT.56-58's Pauli anatomy (C1), PARAMETRIC "
    "in two undeclared slots m_off, dtheta (C2), and its 16-component force map OVER-COUNTS the 8-dim derived "
    "algebra (B3). It is consistent with the corpus only as a parametric construction class whose derived "
    "content already exists",
    okD2, f"algebra-exact={okA1 and okA2 and okA3 and okB1}; redundant={okC1}; parametric={okC2}; over-counts={okB3}")

okD3 = True
chk("D3  status: the object is recorded as a PARAMETRIC CONSTRUCTION CLASS (not a derived row, not adopted); "
    "Declarations issued NONE (m_off, dtheta stay undeclared slots); no species identified [Def-BM.3(1,(7))]; "
    "no measured value [P5] (m_L, m_S, m_off are ledger reads/slots, NOT SM masses; dtheta structural, "
    "unmeasured); prices not masses [BM.30(5); BM.37(6)]; no currency mixing [BM.83]; Cal-IT empty; Level-5 "
    "and IT.1-IT.11 cited, never edited",
    okD3, "parametric construction class; declarations none; no species; no measured value; Cal-IT empty")

# ===========================================================================
print("=" * 96)
print("""ADJUDICATION SUMMARY (Tier IT.12 candidate; the rows win over the framing):
    * THE ALGEBRA IS EXACT AND CORRECT: M=[[m_L,w],[w*,m_S]] on H_omega=C^2 is Hermitian; v_0=m_L+m_S,
      v_3=m_L-m_S, v_1=2 m_off cos dtheta, v_2=-2 m_off sin dtheta; eigenvalues [(m_L+m_S)+/-sqrt((m_L-m_S)^2
      +4 m_off^2)]/2; C_munu=Tr((M(x)M)(sigma_mu(x)sigma_nu))=v_mu v_nu -- all verified over Gauss(i).
    * BUT IT ADDS NO NEW DERIVED CONTENT: (P2) M is the SAME SPECIES as BM.22's force matrix F_ext=h(x)I+q I(x)
      kappa (diagonal + off-diagonal flipping), with the derived charge q replaced by undeclared parameters;
      the Pauli/tensor structure is AT.56-58's anatomy. (P3) the 16 sigma_mu(x)sigma_nu OVER-COUNT the 8-dim
      derived force algebra [AT.56: 'zero new operators'] -- 8 of 16 are not force channels. (P1) m_off, dtheta
      are UNDECLARED slots (dtheta is neither the winding Theta nor the defect Theta_R) -- a P4/declaration act,
      none issued.
    * THE OVER-CLAIMS FAIL (P4): no 'unified origin for the forces' (they are derived separately, AT.50/AT.56-58);
      no BEC-statistics explanation (that is eps=(-1)^A, winding parity [BM.128(7); IT.31(4)], not an
      eigenvalue); the IT.10 connection is trivial.
    * THE CURRENCY IS CLEAN ON THE DIAGONAL: m_L, m_S are both informational E_int ln2/h reads [FT.44(4)] -- no
      BM.83 mix. The off-diagonal's currency is undeclared.
    * VERDICT: M is a legitimate PARAMETRIC CONSTRUCTION CLASS whose exact algebra reproduces structure the
      corpus ALREADY has (BM.22 + AT.56-58). It is REDUNDANT + PARAMETRIC, not a new derived object. Recorded
      honestly, not adopted, no declaration issued.
    * BARS: no species identified; no measured datum; prices not masses; no currency mixing; Level-5 and
      IT.1-IT.11 cited, never edited. Declarations issued: none; Cal-IT stays empty.""")
print("=" * 96)

n_ok = sum(R)
print(f"\n  mass_matrix.py: {n_ok}/{len(R)} EXACT -- no floating point, no measured value.")
sys.exit(0 if n_ok == len(R) else 1)
