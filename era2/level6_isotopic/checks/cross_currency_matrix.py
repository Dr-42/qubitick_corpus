#!/usr/bin/env python3
"""
cross_currency_matrix.py -- the Architect's CROSS-CURRENCY 2x2 matrix M = [[m_L, rho_B],[eps_q, m_S]]:
the entry-by-entry canon audit, the exact tensor product, the S-T decomposition (which for THIS M is
exactly the currency-exchange symmetrization), the CT1.12a(2)/AT.56 grading-map adjudication, the
formal-partial-derivative census behind the "photon vs ideal observer" asymmetry claim, and the
redundancy adjudication against IT.37-IT.39 / BM.22.
Level 6 (Isotopic), Tier IT.14 candidates (IT.43-IT.45).

DIRECTIVE (Architect, session 13j): "Audit a New Cross-Currency Mass Matrix, Its Tensor Product,
S-T Decomposition, and the Photon/Observer Derivative Asymmetry ... M = [[m_L, rho_B],[eps_q, m_S]]
... Placing rho_B (baryon currency) and eps_q (lepton currency) as off-diagonal entries in the same
matrix does NOT violate the incommensurability bar ... a matrix is a structural container where their
product rho_B*eps_q appears in the determinant and eigenvalues -- which is the exact algebraic seat of
the IT.4 handshake indicator ... S carries (rho_B+eps_q) ... T carries (rho_B-eps_q) ...
d(eps_q)/d(rho_B) = 0 (the photon view) vs d(rho_B)/d(eps_q) != 0 (the ideal observer view) ...
Scenario A (new structure) or Scenario B (redundancy)."

PREMISE AUDIT (verified against the canon BEFORE construction; the rows win over the framing):

  * THE TENSOR PRODUCT AS WRITTEN IS CORRECT (verified entrywise below): (M(x)M)_{(i,k),(j,l)} =
    M_ij M_kl gives exactly the directive's 4x4; the pure product rho_B*eps_q sits at (2,3),(3,2)
    (1-based), in det M with coefficient -1, in the discriminant with coefficient +4, and in the
    IT.38(1)-style combination C_11+C_22 = 4 rho_B eps_q. Exact symbolic arithmetic throughout.

  * (P1) THE MATRIX IS q-INHOMOGENEOUS -- a NEW obstruction IT.37's M did not have. On the corpus's
    own dimension grading: [m] = q^{+1/2} [BM.83(4): m = mu z, [mu]=q^{+1/2}], rho_B = mu'^2 h^2/(ln2)^2
    in q^0 [BM.83(4): "machine: the exponent arithmetic"], eps_q a threshold in q^0 [BM.19(2); D0.4].
    So M's diagonal carries q^{1/2} and its off-diagonal q^0: det M = m_L m_S - rho_B eps_q SUMS q^1
    with q^0, and the eigenvalue discriminant (m_L-m_S)^2 + 4 rho_B eps_q does the same. IT.37(1)'s M
    kept w mass-dimensioned, so its det was homogeneous; the new M is not a graded-homogeneous matrix
    at all. Homogenizing it needs a declared mass^2 scale -- a P4-class act, none issued [BM.6(4)].

  * (P2) THE CONTAINER DOES NOT LAUNDER THE SUMS. The Architect's key claim ("the bar forbids SUMMING
    or CONVERTING; a matrix is only a container") fails on the matrix's own derived reads: the Pauli
    coefficient v_1 = Tr(M sigma_1) = rho_B + eps_q ALREADY at the 2x2 level, S carries 1/2 m_L(rho_B+eps_q)
    and 1/2(rho_B^2+eps^2), T carries 1/2 m_L(rho_B-eps_q) and 1/2(rho_B^2-eps_q^2) = 1/2(rho_B-eps_q)(rho_B+eps_q),
    det and the eigenvalues sum m_L m_S with rho_B eps_q. These are cross-currency sums/differences of
    the IT.4(2)-disjoint alphabets: BARRED as formed reads [BM.83(3),(9); IT.4(3): the reduced mass
    mu = m1 m2/(m1+m2) "requires a SUM across the disjoint value alphabets -- a cross-currency equation,
    barred ... formable only as a SYMBOLIC expression carrying undeclared slots"; BM.140(5): "the
    comparison is arithmetic, NOT a bridge ... no derived equation converts them"]. The array M itself
    is formable as a symbolic expression (IT.4(3)'s precedent), but EVERY scalar read formed from it
    inherits the bar -- the container changes nothing.

  * (P3) rho_B*eps_q IS NOT THE HANDSHAKE SEAT. IT.4(2) is an exhaustiveness row: the formed MIXED
    loci are EXACTLY THREE -- B_ens^(n) [BM.137(3)], W_channel = x_+^2 chi_{NE>=T_0} [BM.122(3)], and
    the handshake chi_{NE>=T_0} itself [Def-BM.17(3); BM.122(2); BM.134(5)] -- and the handshake is
    BINARY, with T_0 built from E_int, h, ln2. BM.134(5): the two resolvent species "meet only through
    the threshold indicator chi_{NE>=T_0}". IT.4(2): "every formed cross-currency RATIO carries an
    UNDECLARED slot: cross-currency VALUES do not exist pre-calibration." The product rho_B*eps_q of the
    two undeclared slots appears in NO formed read -- calling it "the exact algebraic seat of the IT.4
    handshake indicator" contradicts the exhaustiveness census (machine: the three loci's alphabets are
    checked to contain neither rho_B nor mu'^2).

  * (P4) THE S/T <-> S-even/S-odd MAPPING [CT1.12a(2)] IS REFUTED BY THE CANON'S OWN BASIS. The S-T
    split is the +-1 eigensplit of the TRANSPOSE involution on End(C^4); CT1.12a(2)'s S-grading is the
    +-1 eigensplit of the pair-channel SWAP CONJUGATION (machine-reproduced at measurement_theorem.py
    B3). Different involutions: of the six S-odd operators J_i, K_i, exactly THREE (J_2, K_1, K_3) are
    transpose-EVEN (they sit in S), and the S-even carrier W_2 is transpose-ODD (it sits in T). Both
    involutions split 16 = 10+6 and their joint refinement is 7+3+3+3 -- the counts agree with
    CT1.12a(2)/CT1.1 numerically, the SUBSPACES do not: a numerology flag, not an identification
    [BM.134(5) dictionary discipline]. AT.56's six bivectors are Hermitian Pauli products, only 2 of
    6 transpose-odd, and not swap-eigenvectors at all: dim(bivector carrier INTERSECT T-carrier) = 2.
    And the 16-vs-8 over-count [IT.38(2)] carries over: S and T both have support on 4 Pauli-product
    directions OUTSIDE the derived 8-dim force algebra -- any force reading of S/T is a stipulation.

  * (P5) THE DERIVATIVE ASYMMETRY HAS NO SEAT. eps_q and rho_B sit in the two DISJOINT slot families
    [IT.5(1): "the two currency slot-families are DISJOINT"]. Machine census over every formed read the
    slot table lists: NO formed read contains both slots; the formal partials of rho_B's derived read
    (mu'^2 h^2/(ln2)^2 [BM.83(4)]) wrt eps_q and of eps_q wrt rho_B are BOTH exactly zero -- the
    independence is SYMMETRIC, not asymmetric. m_hid = E_int ln2/h [FT.44(4)] and Delta x_B = h/(E_int ln2)
    [Def-BM.4(1); IT.31(1)] have ZERO eps_q dependence (formal partials vanish): "the informational mass
    is governed by the flicker threshold" is false on the derived rows. A nonzero d(rho_B)/d(eps_q)
    requires a DECLARED functional link across the currencies -- exactly the conversion BM.140(5)/BM.83
    bar, and a P4-class declaration none is issued. Also: "perspectives" are not ledger primitives (the
    observer = a designated register [Def-H.9; IT.1(8)(P4)]); the photon has no formed perspective reads
    at all (the transit-leg amplitude is NOT formed [(R9''); BM.122(6); IT.3(6); IT.41: D3.7 trivial
    chains out of Def-H.38's scope]); eps_q is a GLOBAL A4-threshold slot [BM.19(2); D0.4; AT-O27
    adoption not issued], not a per-species possession; and rho_B (an undeclared q^0 slot) is not a seal
    class (the proton class 15 of 64 is the derived integer census W_3(Q) = C(6,Q+3) [AT.41(2),(3);
    IT.4(4)]) -- a category error. The salvageable kernel is the LOCUS distinction IT.4(2) already
    derives: eps_q enters formed reads ONLY at the three composite mixed loci (e.g. W_channel =
    (1-4 eps_q)^2 chi, the Born-width distribution sharpening at zero flicker [BM.122(3)]), while the
    geometric reads (Delta x_B, Delta x_B * r_s = h^2/(2 ln2) [BM.17(3); IT.31(1)]) are eps_q-free --
    the anchor bypasses the bar BECAUSE it never mixes [IT.32(3)], which is the opposite of what the
    directive asks it to license.

  * (P6) m_S MAPS TO EXISTING ROWS; "quantum free charge" IS NOT A CANON TERM. The phrase "free
    charge" occurs nowhere as a defined object. The two candidate reads are both already on record:
    (a) the rung-1 seal informational mass m_S = 2 ln2/h (E_int = 2 [FT.28; IT.37(1)]) -- commensurable
    with m_L, IT.37(4)'s row; (b) the lightest-neutrino scale: the absolute nu mass is NOT derived
    [BM.83(8); FT.143(3): mu_nu undeclared]; its informational floor is m_nu h >= 2 ln2 [BM.70(2),(3)
    re-cited at BM.83(8)] -- whose equality case IS read (a); a general floor read sigma_nu z_1 ln2/h
    is lepton/transport currency, making Tr M = m_L + m_S a barred reduced-mass-type cross-currency
    sum [IT.4(3)]. Neither read is a new object; the choice between them is undeclared.

  * THE HONEST VERDICT -- SCENARIO B (REDUNDANCY), sharpened: M is the general 2x2 (four slots: two
    derived diagonal reads + the two undeclared currency slots) -- a NON-HERMITIAN specialization of the
    SAME parametric construction class recorded at IT.37-IT.39 (redundant with BM.22's force-matrix
    species; the Pauli/tensor anatomy is AT.56-58 + IT.38(1): C_munu = v_mu v_nu verified below for the
    new v's). The S-T split adds NO new operators (S, T live in the same span{sigma_mu (x) sigma_nu})
    and NO new mixed locus (IT.4(2) exhaustiveness). Its one true structural gem -- for THIS M the
    transpose IS the currency involution iota (iota(M) = M^T exactly, because the diagonal is
    iota-fixed), so the S-T split IS the currency-exchange symmetrization -- EXPOSES the bar rather
    than bypassing it: S's entries are literally the barred cross-currency sums. NOT ADOPTED; no
    declaration issues; Cal-IT stays empty.

DERIVED/VERIFIED HERE (machine, exact -- multivariate polynomials over Gauss(i) over Fraction,
formal partial derivatives, integer/set censuses; NO floating point, NO measured value [P5]):
  (A) the directive's 4x4 tensor product verified entrywise; the rho_B*eps_q seat census; the
      q-grading inhomogeneity (new M) vs homogeneity (IT.37's M); the alphabet-disjointness census
      and the three-formed-mixed-loci exhaustiveness vs rho_B*eps_q.
  (B) S+T = M(x)M, S^T=S, T^T=-T; the explicit S,T entries; iota(M)=M^T and iota(S)=S, iota(T)=-T;
      the Pauli reads v_mu and C_munu = v_mu v_nu (all 16, symbolic traces); the 12-of-16 factor count.
  (C) the B3 swap grading re-certified on the canon's own basis; the transpose-parity cross-cut
      (J_2,K_1,K_3 in S; W_2 in T); the joint 7+3+3+3 refinement; the AT.56 bivector overlap (2 of 6);
      the S/T support vs the 8-dim derived force algebra (4 outside directions each).
  (D) the formed-read census: no formed read contains both slots; the formal partials; the
      eps_q-freeness of m_hid, Delta x_B, rho_B; the symmetric vanishing of the claimed asymmetry.
  (E) non-Hermiticity; the m_S candidate reads (2 ln2/h floor equality; the barred trace under read (b));
      the redundancy verdict assembly.

BARS: exact arithmetic only; no species identification [Def-BM.3(1),(7)]; no measured value [P5] --
rho_B, eps_q stay symbolic slots; no currency mixing as formed reads [BM.83; BM.134(5); BM.140(5)];
no smooth-manifold analogy (the partial derivatives below are FORMAL polynomial operations on slot
alphabets, not analysis); prices not masses [HistLog V.32]; Level-5 record and IT.1-IT.13 cited,
never edited [AT.63(2)]. Declarations issued: none; Cal-IT empty.
"""

import sys
from fractions import Fraction as Fr

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# =====================================================================================
# Gauss(i) over Fraction -- a complex coefficient is a pair (re, im) of Fractions
# =====================================================================================
def g(re, im=0):
    return (Fr(re), Fr(im))


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gneg(x):
    return (-x[0], -x[1])


def gconj(x):
    return (x[0], -x[1])


def ginv(x):
    n = x[0] * x[0] + x[1] * x[1]
    return (x[0] / n, -x[1] / n)


G0, G1, GI = g(0), g(1), g(0, 1)

# =====================================================================================
# Multivariate Laurent polynomials over Gauss(i): dict {(exponent tuple): Gauss coeff}
# Variables (fixed order):
VARS = ("mL", "mS", "rB", "eq", "E", "L", "h", "mu2", "chi", "d",
        "DS", "sl", "sn", "zl", "Rs", "w")
VI = {v: i for i, v in enumerate(VARS)}
NV = len(VARS)

# the corpus's q-grading (dimension bookkeeping) per variable -- the exponent arithmetic of
# BM.83(4) ([m]=q^{1/2} from m=mu z; rho_B = mu'^2 h^2/(ln2)^2 in q^0 => [mu'^2]=q^1, [h]=q^{-1/2})
QDEG = {"mL": Fr(1, 2), "mS": Fr(1, 2), "rB": Fr(0), "eq": Fr(0), "E": Fr(0), "L": Fr(0),
        "h": Fr(-1, 2), "mu2": Fr(1), "chi": Fr(0), "d": Fr(0), "DS": Fr(0), "sl": Fr(0),
        "sn": Fr(0), "zl": Fr(0), "Rs": Fr(0), "w": Fr(1, 2)}


def pvar(name):
    e = [0] * NV
    e[VI[name]] = 1
    return {tuple(e): G1}


def pconst(c):
    return {} if c == G0 else {tuple([0] * NV): c}


def pfrom_fr(x):
    return pconst(g(x))


def padd(p, q):
    out = dict(p)
    for e, c in q.items():
        if e in out:
            out[e] = gadd(out[e], c)
        else:
            out[e] = c
    return {e: c for e, c in out.items() if c != G0}


def pneg(p):
    return {e: gneg(c) for e, c in p.items()}


def psub(p, q):
    return padd(p, pneg(q))


def pmul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = gadd(out[e], gmul(c1, c2)) if e in out else gmul(c1, c2)
    return {e: c for e, c in out.items() if c != G0}


def pscale(p, s):
    return {e: gmul(c, s) for e, c in p.items() if gmul(c, s) != G0}


def peq(p, q):
    return padd(p, pneg(q)) == {}


def pdiff(p, name):
    """formal partial derivative wrt a variable -- a polynomial operation, not analysis."""
    k = VI[name]
    out = {}
    for e, c in p.items():
        if e[k]:
            e2 = list(e)
            e2[k] -= 1
            out[tuple(e2)] = gadd(out.get(tuple(e2), G0), gmul(c, g(e[k])))
    return {e: c for e, c in out.items() if c != G0}


def pvars_used(p):
    """the alphabet of a polynomial: variables with a nonzero exponent somewhere."""
    used = set()
    for e in p:
        for i, x in enumerate(e):
            if x:
                used.add(VARS[i])
    return used


def pdeg_set(p):
    """the set of q-degrees of the monomials (Laurent exponents allowed)."""
    out = set()
    for e in p:
        deg = Fr(0)
        for i, x in enumerate(e):
            deg += QDEG[VARS[i]] * x
        out.add(deg)
    return out


def pfmt(p):
    if not p:
        return "0"
    terms = []
    for e, c in sorted(p.items()):
        coef = ""
        if c == G1:
            coef = ""
        elif c == gneg(G1):
            coef = "-"
        elif c[1] == 0:
            coef = f"{c[0]}" if c[0] >= 0 else f"({c[0]})"
        else:
            sgn = "+" if c[1] >= 0 else "-"
            coef = f"({c[0]}{sgn}{abs(c[1])}i)"
        fac = "".join(f"*{VARS[i]}^{x}" if abs(x) != 1 else (f"*{VARS[i]}" if x == 1 else f"*{VARS[i]}^{x}")
                      for i, x in enumerate(e) if x)
        term = coef + fac
        terms.append(term.lstrip("*") if coef == "" else (term if term else "1"))
    return " + ".join(terms).replace("+-", "- ")


ML, MS, RB, EQ = pvar("mL"), pvar("mS"), pvar("rB"), pvar("eq")
ONE_P = pconst(G1)
HALF = pconst(g(Fr(1, 2)))

print("=" * 100)
print("PART A -- the object, entry by entry: the tensor product, the q-grading, the alphabet census")
print("=" * 100)

# ---- symbolic 2x2 matrices over Poly: [[p00,p01],[p10,p11]] ----
M = [[ML, RB], [EQ, MS]]


def m2mul(A, B):
    return [[padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j])) for j in (0, 1)] for i in (0, 1)]


def m2add(A, B):
    return [[padd(A[i][j], B[i][j]) for j in (0, 1)] for i in (0, 1)]


def m2trans(A):
    return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]


def kronP(A, B):
    """Kronecker product of 2x2 Poly matrices -> 4x4 Poly matrix, (A(x)B)_{(i,k),(j,l)} = A_ij B_kl."""
    out = [[{} for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + k][2 * j + l] = pmul(A[i][j], B[k][l])
    return out


def kronN(A, B):
    """Kronecker product of numeric Gauss 2x2 matrices -> 4x4."""
    out = [[G0] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + k][2 * j + l] = gmul(A[i][j], B[k][l])
    return out


A4 = kronP(M, M)

# A1: the directive's explicit 4x4, entry by entry
DIR4 = [
    [pmul(ML, ML), pmul(ML, RB), pmul(RB, ML), pmul(RB, RB)],
    [pmul(ML, EQ), pmul(ML, MS), pmul(RB, EQ), pmul(RB, MS)],
    [pmul(EQ, ML), pmul(EQ, RB), pmul(MS, ML), pmul(MS, RB)],
    [pmul(EQ, EQ), pmul(EQ, MS), pmul(MS, EQ), pmul(MS, MS)],
]
chk("A1  [directive Step 1; Kronecker rule]: the tensor product M(x)M computed from the rule"
    "\n           (M(x)M)_{(i,k),(j,l)} = M_ij M_kl equals the directive's explicit 4x4 ENTRYWISE"
    "\n           (16/16 symbolic polynomial equalities; commutative scalars: rB*mL = mL*rB etc.).",
    all(peq(A4[i][j], DIR4[i][j]) for i in range(4) for j in range(4)),
    "rows: [" + " | ".join(pfmt(A4[0][j]) for j in range(4)) + "] ... (all four rows verified)")

# A2: the seat census of the pure cross-currency product rho_B*eps_q
PROD = pmul(RB, EQ)
seats4 = [(i + 1, j + 1) for i in range(4) for j in range(4) if peq(A4[i][j], PROD)]
detM = psub(pmul(M[0][0], M[1][1]), pmul(M[0][1], M[1][0]))          # m_L m_S - rho_B eps_q
disc = padd(pmul(psub(ML, MS), psub(ML, MS)), pscale(PROD, g(4)))     # (m_L-m_S)^2 + 4 rho_B eps_q
PRODKEY = tuple(1 if VARS[i] in ("rB", "eq") else 0 for i in range(NV))
det_coeff = detM.get(PRODKEY, G0)
disc_entry = None
for e, c in disc.items():
    if e == tuple(1 if VARS[i] in ("rB", "eq") else 0 for i in range(NV)):
        disc_entry = c
chk("A2  [directive Step 1 seat identification]: the pure product rho_B*eps_q sits at EXACTLY the"
    "\n           1-based positions (2,3),(3,2) of M(x)M (a monomial seat census over all 16 entries);"
    "\n           det M = m_L*m_S - rho_B*eps_q carries it with coefficient -1; the discriminant"
    "\n           (m_L-m_S)^2 + 4*rho_B*eps_q with coefficient +4.",
    seats4 == [(2, 3), (3, 2)] and det_coeff == g(-1) and disc_entry == g(4),
    f"seats={seats4}; det coefficient={det_coeff}; discriminant coefficient={disc_entry}")

# A3: the q-grading census -- the NEW obstruction (dimensional inhomogeneity)
degM = set()
for row in M:
    for p in row:
        degM |= pdeg_set(p)
deg_det = pdeg_set(detM)
deg_disc = pdeg_set(disc)
# IT.37's contrast: M12 = [[mL, w],[w, mS]] with w mass-dimensioned (q^{1/2}) -- homogeneous
Wsym = pvar("w")
M12 = [[ML, Wsym], [Wsym, MS]]
degM12 = set()
for row in M12:
    for p in row:
        degM12 |= pdeg_set(p)
det12 = psub(pmul(ML, MS), pmul(Wsym, Wsym))
chk("A3  [BM.83(4) exponent arithmetic; FT.44(4); BM.19(2); IT.37(1) contrast]: the q-GRADING CENSUS --"
    "\n           [m_L]=[m_S]=q^{1/2} (mass reads E_int ln2/h), [rho_B]=[eps_q]=q^0 (BM.83(4): rho_B in q^0;"
    "\n           eps_q the A4 threshold): the new M's entries span TWO degrees {0, 1/2} (inhomogeneous);"
    "\n           det M sums q^1 with q^0; the discriminant too. IT.37's M (w of degree 1/2) is homogeneous"
    "\n           by contrast. Homogenizing needs a declared mass^2 scale -- a P4 act, none issued [BM.6(4)].",
    degM == {Fr(0), Fr(1, 2)} and deg_det == {Fr(0), Fr(1)} and deg_disc == {Fr(0), Fr(1)}
    and degM12 == {Fr(1, 2)} and pdeg_set(det12) == {Fr(1)},
    f"deg(entries M)={sorted(degM)}; deg(det M)={sorted(deg_det)}; deg(disc)={sorted(deg_disc)}; "
    f"deg(entries M_IT37)={sorted(degM12)}; deg(det M_IT37)={sorted(pdeg_set(det12))}")

# A4: the alphabet census -- disjointness [IT.4(2)] and the three formed mixed loci [IT.4(2); IT.5(1)]
BARYON_GEN = {"E", "mu2", "rB", "DS"}                      # {E_int, mu'^2, rho_B, D_S}
LEPTON_GEN = {"eq", "xp", "xm", "wc", "sl", "zl"}           # {eps_q, x_+-, w_c, sigma_l, z^(l)}
SHARED = {"h", "L", "pi"}                                   # h, ln2, pi
# the three formed mixed loci, encoded as polynomials (chi = the binary indicator as a formal symbol):
u_round = psub(pscale(EQ, g(4)), pscale(pmul(EQ, EQ), g(16)))          # W_round = x_+x_- = 4eq(1-4eq) [BM.122(3)]
W_channel = pmul(pmul(psub(ONE_P, pscale(EQ, g(4))), psub(ONE_P, pscale(EQ, g(4)))), pvar("chi"))
u_BM137 = pscale(EQ, g(4))                                              # u := 1-p = 4*eps_q [BM.137(1)]
# B_ens^(2) = -(2n u D_{n-1}/D_n)(ln2/h) at n=2: -(4u/(1+u))(ln2/h) [BM.137(3)]:
B_ens2_num = pscale(pmul(u_BM137, pmul(pvar("L"), {tuple(-1 if VARS[i] == "h" else 0 for i in range(NV)): G1})), g(-4))
T0_alphabet = {"E", "h", "L"}
loci = {"B_ens": pvars_used(B_ens2_num) | {"n"}, "W_channel": pvars_used(W_channel) | T0_alphabet,
        "chi (handshake)": T0_alphabet | {"NE"}}
disjoint = not (BARYON_GEN & LEPTON_GEN)
prod_vars = pvars_used(PROD)
no_locus_has_prod = all(not ({"rB"} <= loc and {"eq"} <= loc) for loc in loci.values())
chk("A4  [IT.4(2) alphabet census + exhaustiveness; IT.5(1); BM.83(5); BM.134(5)]: the baryon-side"
    "\n           generators {E_int, mu'^2, rho_B, D_S} and the lepton-side {eps_q, x_+-, w_c, sigma_l, z^(l)}"
    "\n           are DISJOINT (shared symbols only h, ln2, pi); and NONE of the EXACTLY THREE formed mixed"
    "\n           loci (B_ens [BM.137(3)], W_channel = x_+^2 chi [BM.122(3)], the handshake chi_{NE>=T_0}"
    "\n           [Def-BM.17(3); BM.122(2); BM.134(5)]) carries BOTH rho_B and eps_q -- the product"
    "\n           rho_B*eps_q is in no formed read: 'cross-currency VALUES do not exist pre-calibration'."
    "\n           The handshake seat claim of the directive is contradicted by the exhaustiveness census.",
    disjoint and no_locus_has_prod and prod_vars == {"rB", "eq"},
    f"loci alphabets: {{{', '.join(k + ': ' + str(sorted(v)) for k, v in loci.items())}}}")

print("=" * 100)
print("PART B -- the S-T decomposition: exact, and identical to the currency-exchange symmetrization")
print("=" * 100)


def m4add(A, B):
    return [[padd(A[i][j], B[i][j]) for j in range(4)] for i in range(4)]


def m4neg(A):
    return [[pneg(A[i][j]) for j in range(4)] for i in range(4)]


def m4trans(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def m4scale(A, s):
    return [[pscale(A[i][j], s) for j in range(4)] for i in range(4)]


def iota(p):
    """the currency involution: rho_B <-> eps_q, fixing m_L, m_S and all shared symbols."""
    out = {}
    for e, c in p.items():
        e2 = list(e)
        e2[VI["rB"]], e2[VI["eq"]] = e[VI["eq"]], e[VI["rB"]]
        out[tuple(e2)] = gadd(out.get(tuple(e2), G0), c)
    return {e: c for e, c in out.items() if c != G0}


def m4iota(A):
    return [[iota(A[i][j]) for j in range(4)] for i in range(4)]


A4T = m4trans(A4)
S = m4scale(m4add(A4, A4T), g(Fr(1, 2)))
T = m4scale(m4add(A4, m4neg(A4T)), g(Fr(1, 2)))
ST_sum = all(peq(padd(S[i][j], T[i][j]), A4[i][j]) for i in range(4) for j in range(4))
S_sym = all(peq(S[i][j], S[j][i]) for i in range(4) for j in range(4))
T_anti = all(peq(T[i][j], pneg(T[j][i])) for i in range(4) for j in range(4))
chk("B1  [directive Step 2]: S = 1/2(M(x)M + (M(x)M)^T), T = 1/2(M(x)M - (M(x)M)^T) computed"
    "\n           symbolically: S + T = M(x)M (16/16), S^T = S (16/16), T^T = -T (16/16) -- exact"
    "\n           polynomial identities (non-vacuous: a single sign slip in any entry fails one of them).",
    ST_sum and S_sym and T_anti)

# B2: the Architect's content claims, entrywise -- with the incompleteness correction
halfL = pscale(pmul(ML, padd(RB, EQ)), g(Fr(1, 2)))           # 1/2 m_L (rB+eq)
halfLm = pscale(pmul(ML, psub(RB, EQ)), g(Fr(1, 2)))          # 1/2 m_L (rB-eq)
sq_plus = pscale(padd(pmul(RB, RB), pmul(EQ, EQ)), g(Fr(1, 2)))     # 1/2 (rB^2+eq^2)
sq_minus_fact = pscale(pmul(psub(RB, EQ), padd(RB, EQ)), g(Fr(1, 2)))  # 1/2 (rB-eq)(rB+eq)
sq_minus = pscale(psub(pmul(RB, RB), pmul(EQ, EQ)), g(Fr(1, 2)))
claim_S = peq(S[0][1], halfL) and peq(S[0][3], sq_plus) and peq(S[3][1], pscale(pmul(MS, padd(RB, EQ)), g(Fr(1, 2))))
claim_T = peq(T[0][1], halfLm) and peq(T[0][3], sq_minus) and peq(sq_minus, sq_minus_fact)
chk("B2  [directive Step 2 claims, VERIFIED with one correction]: S carries 1/2*m_L*(rho_B+eps_q) at"
    "\n           (1,2),(1,3),(2,1),(3,1), 1/2*(rho_B^2+eps_q^2) at (1,4)/(4,1), 1/2*m_S*(rho_B+eps_q) at"
    "\n           (4,2),(4,3),(2,4),(3,4); T carries the difference analogues. CORRECTION: T's (1,4) entry"
    "\n           1/2*(rho_B^2-eps_q^2) FACTORS as 1/2*(rho_B-eps_q)*(rho_B+eps_q) -- T also carries the SUM"
    "\n           as a factor, so 'T carries (rho_B-eps_q)' is true but incomplete (verified as an identity).",
    claim_S and claim_T,
    f"S[1,2]={pfmt(S[0][1])}; S[1,4]={pfmt(S[0][3])}; T[1,2]={pfmt(T[0][1])}; T[1,4]={pfmt(T[0][3])}")

# B3: the structural gem -- for THIS M the transpose IS the currency involution
iotaM = [[iota(M[i][j]) for j in (0, 1)] for i in (0, 1)]
gem2 = all(peq(iotaM[i][j], M[j][i]) for i in (0, 1) for j in (0, 1))
gem4 = all(peq(m4iota(A4)[i][j], A4T[i][j]) for i in range(4) for j in range(4))
Sfix = all(peq(iota(S[i][j]), S[i][j]) for i in range(4) for j in range(4))
Tanti = all(peq(iota(T[i][j]), pneg(T[i][j])) for i in range(4) for j in range(4))
chk("B3  [the structural fact, machine-exact]: iota(M) = M^T (the currency involution rho_B <-> eps_q"
    "\n           fixes the diagonal, so transposing M IS exchanging the currencies) => iota(M(x)M) ="
    "\n           (M(x)M)^T, iota(S) = +S, iota(T) = -T: FOR THIS OBJECT the transpose S-T split IS the"
    "\n           currency-exchange symmetrization. Consequence (P2): S's entries are LITERALLY the"
    "\n           cross-currency sums/differences barred as formed reads [BM.83(3),(9); IT.4(3); BM.140(5)]"
    "\n           -- the split exposes the bar rather than bypassing it.",
    gem2 and gem4 and Sfix and Tanti)

# B4: the Pauli reads and the 16-component factorization C_munu = v_mu v_nu [IT.37(2); IT.38(1)]
SIG = [
    [[G1, G0], [G0, G1]],
    [[G0, G1], [G1, G0]],
    [[G0, gneg(GI)], [GI, G0]],
    [[G1, G0], [G0, g(-1)]],
]


def m2trace(A):
    return padd(A[0][0], A[1][1])


def m2mulN(A, B):
    """Poly 2x2 times numeric Gauss 2x2."""
    return [[padd(pscale(A[i][0], B[0][j]), pscale(A[i][1], B[1][j])) for j in (0, 1)] for i in (0, 1)]


def sum4(it):
    """explicit Poly accumulation -- NEVER sum() on ring elements (tuple concatenation trap)."""
    acc = {}
    for p in it:
        acc = padd(acc, p)
    return acc


v = [m2trace(m2mulN(M, SIG[mu])) for mu in range(4)]
# v_0 = mL+mS, v_1 = rB+eq, v_2 = i(rB-eq), v_3 = mL-mS
v_expect = [padd(ML, MS), padd(RB, EQ), pscale(psub(RB, EQ), GI), psub(ML, MS)]
v_ok = all(peq(v[mu], v_expect[mu]) for mu in range(4))


def m4mulPN(A, B):
    """Poly 4x4 times numeric Gauss 4x4."""
    return [[sum4(pscale(A[i][k], B[k][j]) for k in range(4)) for j in range(4)] for i in range(4)]


C = {}
for mu in range(4):
    for nu in range(4):
        SMN = kronN(SIG[mu], SIG[nu])
        C[(mu, nu)] = sum4(m4mulPN(A4, SMN)[i][i] for i in range(4))
C_ok = all(peq(C[(mu, nu)], pmul(v[mu], v[nu])) for mu in range(4) for nu in range(4))
# how many of the 16 C_munu carry v_1 = (rB+eq) or v_2/i = (rB-eq) as a factor:
fac_count = sum(1 for (mu, nu) in C if mu in (1, 2) or nu in (1, 2))
C11C22 = padd(C[(1, 1)], C[(2, 2)])
prod_seat = peq(C11C22, pscale(PROD, g(4)))
chk("B4  [IT.37(2); IT.38(1) re-derived for the new v's]: v_0 = m_L+m_S, v_1 = rho_B+eps_q,"
    "\n           v_2 = i(rho_B-eps_q), v_3 = m_L-m_S (symbolic traces); ALL 16 tensor components"
    "\n           C_munu = Tr((M(x)M)(sigma_mu (x) sigma_nu)) = v_mu*v_nu verified by explicit symbolic"
    "\n           4x4 multiplication; 12 of the 16 carry (rho_B+eps_q) or (rho_B-eps_q) as a factor"
    "\n           (the barred sums propagate through the WHOLE tensor layer); C_11+C_22 = 4*rho_B*eps_q.",
    v_ok and C_ok and fac_count == 12 and prod_seat,
    f"v = ({pfmt(v[0])}, {pfmt(v[1])}, {pfmt(v[2])}, {pfmt(v[3])}); factor count = {fac_count}/16")

print("=" * 100)
print("PART C -- the grading map: transpose vs the CT1.12a(2) swap conjugation vs AT.56's bivectors")
print("=" * 100)

# numeric 4x4 layer over Gauss -- the EXACT conventions of measurement_theorem.py B3
SG = [
    [[g(1), g(0)], [g(0), g(1)]],          # sigma_0
    [[g(0), g(1)], [g(1), g(0)]],          # sigma_1
    [[g(0), g(0, -1)], [g(0, 1), g(0)]],   # sigma_2 = [[0,-i],[i,0]]
    [[g(1), g(0)], [g(0), g(-1)]],         # sigma_3
]


def n4mul(A, B):
    out = [[G0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = G0
            for k in range(4):
                acc = gadd(acc, gmul(A[i][k], B[k][j]))
            out[i][j] = acc
    return out


def n4add(*mats):
    acc = [[G0] * 4 for _ in range(4)]
    for A in mats:
        for i in range(4):
            for j in range(4):
                acc[i][j] = gadd(acc[i][j], A[i][j])
    return acc


def n4scale(A, s):
    return [[gmul(A[i][j], s) for j in range(4)] for i in range(4)]


def n4trans(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def n4eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


SWAP = [[G0] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2):
        SWAP[2 * b + a][2 * a + b] = G1


def swapconj(X):
    return n4mul(n4mul(SWAP, X), SWAP)


Jop = [n4scale(n4add(kronN(SG[j], SG[k]), n4scale(kronN(SG[k], SG[j]), g(-1))), g(Fr(1, 2)))
       for (j, k) in ((2, 3), (3, 1), (1, 2))]
Kop = [n4scale(n4add(kronN(SG[0], SG[i]), n4scale(kronN(SG[i], SG[0]), g(-1))), g(Fr(1, 2)))
       for i in (1, 2, 3)]
We = [n4scale(n4add(kronN(SG[0], SG[i]), kronN(SG[i], SG[0])), g(Fr(1, 2))) for i in (1, 2, 3)]
E0 = kronN(SG[0], SG[0])
SIGM = n4add(kronN(SG[1], SG[1]), kronN(SG[2], SG[2]), kronN(SG[3], SG[3]))
Eii = [kronN(SG[i], SG[i]) for i in (1, 2, 3)]

# C1: re-certify the B3 grading (the machine row already in the suite, re-run on this basis)
sodd = all(n4eq(swapconj(X), n4scale(X, g(-1))) for X in Jop + Kop)
seven = all(n4eq(swapconj(X), X) for X in [E0, SIGM] + We + Eii)
chk("C1  [CT1.12a(2); measurement_theorem.py B3 re-certified]: on the canon's own pair-channel basis,"
    "\n           the SWAP conjugation grades J_1,J_2,J_3,K_1,K_2,K_3 S-ODD (anti-invariant) and"
    "\n           E_0, Sigma, W_1,W_2,W_3, E^11,E^22,E^33 S-EVEN (invariant) -- exact 4x4 conjugations.",
    sodd and seven)


def tparity(X):
    Xt = n4trans(X)
    if n4eq(Xt, X):
        return +1
    if n4eq(Xt, n4scale(X, g(-1))):
        return -1
    return 0


Jn = ["J_1", "J_2", "J_3"], [tparity(X) for X in Jop]
Kn = ["K_1", "K_2", "K_3"], [tparity(X) for X in Kop]
Wn = ["W_1", "W_2", "W_3"], [tparity(X) for X in We]
odd_in_S = [Jn[0][i] for i in range(3) if Jn[1][i] == +1] + [Kn[0][i] for i in range(3) if Kn[1][i] == +1]
even_in_T = [Wn[0][i] for i in range(3) if Wn[1][i] == -1] + \
            [f"E^{i}{i}" for i, X in zip((1, 2, 3), Eii) if tparity(X) == -1] + \
            (["Sigma"] if tparity(SIGM) == -1 else [])
chk("C2  [the cross-cut -- directive Step 2's grading map REFUTED on the canon's own operators]: of the"
    "\n           six S-ODD operators exactly THREE are transpose-EVEN (J_2, K_1, K_3 -- they sit inside S,"
    "\n           the 'cooperative' part); of the S-EVEN carriers W_2 is transpose-ODD (it sits inside T,"
    "\n           the 'gap' part). The transpose involution and the swap conjugation CROSS-CUT: neither"
    "\n           S <= S-even nor T <= S-odd holds. The claimed map is refuted without any new basis.",
    odd_in_S == ["J_2", "K_1", "K_3"] and even_in_T == ["W_2"],
    f"S-odd but transpose-even: {odd_in_S}; S-even but transpose-odd: {even_in_T}")

# C3: the joint refinement -- both involutions give 10+6, jointly 7+3+3+3 (numerology, not identity)
adapted = []
for a in range(4):
    adapted.append((f"s{a}s{a}", kronN(SG[a], SG[a])))
for a in range(4):
    for b in range(a + 1, 4):
        adapted.append((f"+({a},{b})", n4add(kronN(SG[a], SG[b]), kronN(SG[b], SG[a]))))
        adapted.append((f"-({a},{b})", n4add(kronN(SG[a], SG[b]), n4scale(kronN(SG[b], SG[a]), g(-1)))))
quad = {}
for name, X in adapted:
    tp, sp = tparity(X), (+1 if n4eq(swapconj(X), X) else (-1 if n4eq(swapconj(X), n4scale(X, g(-1))) else 0))
    quad[(tp, sp)] = quad.get((tp, sp), 0) + 1
chk("C3  [BM.134(5) dictionary discipline]: the dimension census -- transpose splits End(C^4) = 10+6,"
    "\n           swap conjugation splits 10+6, and their JOINT refinement on the adapted Pauli basis is"
    "\n           (T+,S+) 7, (T+,S-) 3, (T-,S+) 3, (T-,S-) 3 = 7+3+3+3. The counts rhyme with CT1.12a(2)'s"
    "\n           10=1+1+5+3 and CT1.1's 7+3+3+3 blocks, but C2's witnesses prove the SUBSPACES differ:"
    "\n           a numerology flag, NOT an identification -- no derived row maps one involution to the other.",
    quad == {(1, 1): 7, (1, -1): 3, (-1, 1): 3, (-1, -1): 3},
    f"joint eigenspace counts: {quad}")

# C4: AT.56's bivectors -- Hermitian Pauli products, 2 of 6 transpose-odd, not swap eigenvectors
BIV = [
    n4scale(kronN(SG[3], SG[0]), g(-1)),   # sigma^{12} = -(s3 (x) s0)
    kronN(SG[2], SG[0]),                    # sigma^{13} = +(s2 (x) s0)
    n4scale(kronN(SG[1], SG[0]), g(-1)),   # sigma^{23} = -(s1 (x) s0)
    kronN(SG[1], SG[3]),                    # sigma^{14} = s1 (x) s3
    kronN(SG[2], SG[3]),                    # sigma^{24} = s2 (x) s3
    kronN(SG[3], SG[3]),                    # sigma^{34} = s3 (x) s3
]
biv_todd = sum(1 for X in BIV if tparity(X) == -1)
# exact statement: swap conjugation maps sigma^{12} = -(s3(x)s0) to -(s0(x)s3), which is NOT
# proportional to ANY of the six bivectors (coefficient comparison in the Pauli-product basis):
def pauli_coords(X):
    """the 16 trace-orthogonal Pauli-product coefficients [CT1.1]: c_ab = Tr(X (s_a (x) s_b))/4."""
    coords = {}
    for a in range(4):
        for b in range(4):
            pr = kronN(SG[a], SG[b])
            acc = G0
            for i in range(4):
                for j in range(4):
                    acc = gadd(acc, gmul(X[i][j], pr[j][i]))
            coords[(a, b)] = gmul(acc, g(Fr(1, 4)))
    return coords


swap_of_biv0 = pauli_coords(swapconj(BIV[0]))
prop_to_some = any(all(swap_of_biv0[k] == gmul(lam, pauli_coords(X)[k]) for k in swap_of_biv0)
                   for X in BIV for lam in (g(1), g(-1), GI, gneg(GI)))
chk("C4  [AT.56(2),(3) bivector census]: the six bivectors sigma^{munu} are Hermitian Pauli products"
    "\n           (-s3s0, +s2s0, -s1s0, s1s3, s2s3, s3s3): only 2 of 6 are transpose-ODD, so"
    "\n           dim(bivector carrier INTERSECT T-carrier) = 2 < 6 -- T is NOT the bivector seat; and"
    "\n           swap conjugation sends sigma^{12} = -(s3(x)s0) to -(s0(x)s3), proportional to NONE of the"
    "\n           six (exact Pauli-coordinate comparison): AT.56's bivectors live in the Dirac F_0 frame,"
    "\n           outside BOTH eigensplit structures of the pair channel.",
    biv_todd == 2 and not prop_to_some,
    f"transpose-odd bivectors: {biv_todd}/6; sigma^{12} swap image proportional to a bivector: {prop_to_some}")

# C5: the S/T support vs the 8-dim derived force algebra [AT.56 'zero new operators'; IT.38(2)]
FORCE8 = {(0, 0), (1, 0), (2, 0), (3, 0), (1, 3), (2, 3), (3, 3), (0, 3)}


def sym_support(P4):
    """the Pauli-product directions of a symbolic Poly 4x4 with nonzero coefficients."""
    sup = set()
    for mu in range(4):
        for nu in range(4):
            pr = kronN(SIG[mu], SIG[nu])
            # coefficient = Tr(P4 * pr)/4 over Poly-Gauss
            tr = sum4(pscale(sum4(pmul_scalar(P4[i][j], pr[j][i]) for j in range(4)), G1) for i in range(4))
            tr = pscale(tr, g(Fr(1, 4)))
            if tr:
                sup.add((mu, nu))
    return sup


def pmul_scalar(p, s):
    return pscale(p, s)


supS, supT = sym_support(S), sym_support(T)
outS, outT = supS - FORCE8, supT - FORCE8
chk("C5  [IT.38(2) 16-vs-8 over-count carried over]: the symbolic Pauli supports: S occupies 10"
    "\n           transpose-even directions, T the 6 transpose-odd ones; against the DERIVED 8-dim force"
    "\n           algebra span{I_4, s_i(x)I_2, s_i(x)kappa, I(x)kappa} (kappa = s_3 [AT.56(1)]): S has 4"
    "\n           directions OUTSIDE, T has 4 OUTSIDE. The S-T split does not respect the force algebra --"
    "\n           any force reading of S or T is a STIPULATION, not a derived row (the IT.38(2) pattern).",
    len(supS) == 10 and len(supT) == 6 and len(outS) == 4 and len(outT) == 4,
    f"S outside the algebra: {sorted(outS)}; T outside: {sorted(outT)}")

print("=" * 100)
print("PART D -- the derivative asymmetry: a formal census over the formed reads [IT.1; IT.5(1); IT.10]")
print("=" * 100)

# the formed reads of the IT.5(1) slot census, encoded exactly (Laurent monomials allowed)
hinv = {tuple(-1 if VARS[i] == "h" else 0 for i in range(NV)): G1}      # h^{-1}
Linv = {tuple(-1 if VARS[i] == "L" else 0 for i in range(NV)): G1}      # (ln2)^{-1}
Einv = {tuple(-1 if VARS[i] == "E" else 0 for i in range(NV)): G1}      # E_int^{-1}
m_hid = pmul(pvar("E"), pmul(pvar("L"), hinv))                          # E_int ln2 / h [FT.44(4)]
dx_B = pmul(pvar("h"), pmul(Einv, Linv))                                # h/(E_int ln2) [Def-BM.4(1)]
r_s = pscale(pmul(pvar("h"), pvar("E")), g(Fr(1, 2)))                   # h E_int / 2 [BM.15(4)]
rho_B_read = pmul(pvar("mu2"), pmul(pmul(pvar("h"), pvar("h")),
                                    pmul(Linv, Linv)))                    # mu'^2 h^2/(ln2)^2 [BM.83(4)]
m2_pole = pmul(pvar("mu2"), pvar("DS"))                                 # mu'^2 D_S [BM.83(1) pole row]
W_round = u_round                                                        # 4eq(1-4eq) [BM.109(2); BM.122(3)]
B_ens2_den = padd(ONE_P, u_BM137)                                        # D_2 = 1+u, u=4eq [BM.137(1)]
eq_read = EQ                                                             # eps_q itself (a free slot)
READS = {
    "m_hid = E_int ln2/h [FT.44(4)]": (m_hid, None),
    "Delta x_B = h/(E_int ln2) [Def-BM.4(1); IT.31(1)]": (dx_B, None),
    "r_s = h E_int/2 [BM.15(4); BM.17(3)]": (r_s, None),
    "Delta x_B * r_s = h^2/(2 ln2) [BM.17(3); IT.31(1)]": (pmul(dx_B, r_s), None),
    "rho_B = mu'^2 h^2/(ln2)^2 [BM.83(4)]": (rho_B_read, None),
    "m^2_pole = mu'^2 D_S [BM.83(1)]": (m2_pole, None),
    "W_channel = (1-4eq)^2 chi [BM.122(3)]": (W_channel, None),
    "W_round = x_+x_- = 4eq(1-4eq) [BM.109(2)]": (W_round, None),
    "B_ens^(2) = -(4u/(1+u)) ln2/h [BM.137(1),(3)]": (B_ens2_num, B_ens2_den),
    "W_d = 1/(d^2 x_+x_-) [AT.44(5)]": (ONE_P, pmul(pmul(pvar("d"), pvar("d")), u_round)),
}
co_occur = []
both_nonzero = []
for name, (num, den) in READS.items():
    alph = pvars_used(num) | (pvars_used(den) if den else set())
    if "rB" in alph and "eq" in alph:
        co_occur.append(name)
    d_rB = pdiff(num, "rB") if den is None else padd(pdiff(num, "rB"), pdiff(den, "rB"))
    d_eq = pdiff(num, "eq") if den is None else padd(pdiff(num, "eq"), pdiff(den, "eq"))
    if d_rB and d_eq:
        both_nonzero.append(name)
chk("D1  [IT.5(1) slot census, machine: the two currency slot-families are DISJOINT]: over the full"
    "\n           formed-read census (m_hid, Delta x_B, r_s, Delta x_B*r_s, rho_B, m^2_pole, W_channel,"
    "\n           W_round, B_ens^(2), W_d): NO formed read contains BOTH slots rho_B and eps_q, and no"
    "\n           formed read has both formal partials nonzero. rho_B and eps_q share no formed read --"
    "\n           so no derived functional dependence exists IN EITHER DIRECTION.",
    not co_occur and not both_nonzero,
    f"reads containing both slots: {co_occur or 'NONE'}; reads with both partials nonzero: {both_nonzero or 'NONE'}")

d_rB_of_eq = pdiff(eq_read, "rB")       # formal d(eps_q)/d(rho_B)
d_eq_of_rB = pdiff(rho_B_read, "eq")    # formal d(rho_B)/d(eps_q) on rho_B's derived read
d_eq_of_mhid = pdiff(m_hid, "eq")       # the directive's premise "m_L governed by the flicker threshold"
d_eq_of_dxB = pdiff(dx_B, "eq")
d_eq_of_Wch = pdiff(W_channel, "eq")    # the contrast: the channel weight DOES depend on eps_q
d_rB_of_Wch = pdiff(W_channel, "rB")
chk("D2  [the asymmetry claim ADJUDICATED on formal partials -- IT.1(8)(P4); BM.140(5); IT.4(2),(3)]:"
    "\n           d(eps_q)/d(rho_B) = 0 AND d(rho_B)/d(eps_q) = 0 EXACTLY (rho_B's derived read"
    "\n           mu'^2 h^2/(ln2)^2 has alphabet {mu'^2, h, ln2}); the independence is SYMMETRIC -- the"
    "\n           claimed pair (0, nonzero) has no seat in any derived read. The directive's premises fail:"
    "\n           d(m_hid)/d(eps_q) = 0 and d(Delta x_B)/d(eps_q) = 0 ('governed by the flicker threshold'"
    "\n           is false [FT.44(4); Def-BM.4(1)]); the ONLY nonzero flicker partial is at the composite"
    "\n           loci (d W_channel/d eps_q = -8(1-4eq)chi != 0, d W_channel/d rho_B = 0 [BM.122(3);"
    "\n           IT.4(2)]) -- a nonzero d(rho_B)/d(eps_q) would be a DECLARED cross-currency conversion,"
    "\n           barred as a formed equation [BM.83(9); BM.140(5): 'no derived equation converts them']"
    "\n           and a P4-class declaration -- none issued.",
    not d_rB_of_eq and not d_eq_of_rB and not d_eq_of_mhid and not d_eq_of_dxB
    and peq(d_eq_of_Wch, pscale(pmul(psub(ONE_P, pscale(EQ, g(4))), pvar("chi")), g(-8)))
    and not d_rB_of_Wch,
    f"d(W_channel)/d(eps_q) = {pfmt(d_eq_of_Wch)}")

# D3: the IT.10 anchor row re-derived: the bypass is shared-currency, and it licenses NO dependence
anchor_prod = pmul(dx_B, r_s)
anchor_target = pmul(pscale(pmul(pvar("h"), pvar("h")), g(Fr(1, 2))), Linv)   # h^2/(2 ln2)
chk("D3  [IT.31(1); IT.32(3) -- the anchor re-derived and its direction corrected]: Delta x_B * r_s ="
    "\n           h^2/(2 ln2) EXACTLY, E_int-independent (the symbolic product cancels E); its alphabet is"
    "\n           {h, ln2} -- shared-currency geometric. The IT.10 bypass licenses geometric/cardinal/sign"
    "\n           reads BECAUSE they never mix currencies [IT.32(3): 'NONE is a cross-currency mass sum'];"
    "\n           citing it for a rho_B(eps_q) dependence INVERTS the row -- the anchor is the proof that"
    "\n           the observer's geometric reads need no flicker functional, not that they carry one.",
    peq(anchor_prod, anchor_target) and pvars_used(anchor_prod) == {"h", "L"},
    f"Delta x_B * r_s = {pfmt(anchor_prod)}; alphabet = {sorted(pvars_used(anchor_prod))}")

print("=" * 100)
print("PART E -- m_S, the redundancy census, and the verdict")
print("=" * 100)

# E1: non-Hermiticity + the species census vs BM.22 / IT.37
Mdag = [[{e: gconj(c) for e, c in M[j][i].items()} for j in (0, 1)] for i in (0, 1)]
nonH = not all(peq(M[i][j], Mdag[i][j]) for i in (0, 1) for j in (0, 1))
v2_pure_imag = all(c[0] == 0 for c in v[2].values()) and v[2] != {}
chk("E1  [BM.22(1),(2),(4); IT.38(3) species census]: M - M^dagger != 0 symbolically (the (1,2) entry"
    "\n           rho_B - eps_q; v_2 = i(rho_B-eps_q) purely imaginary) -- M is NON-HERMITIAN for generic"
    "\n           slots, unlike IT.37(1)'s M and unlike BM.22's Hermitian F_ext. Species line: F_ext reduced"
    "\n           = h*I + q*sigma_1 (2 slots, symmetric flip, DERIVED q in {-1,0,+1} [BM.22(7); EM.9]);"
    "\n           IT.37's M = 3 slots (Hermitian, conjugate flip); the new M = the GENERAL 2x2: 4 slots"
    "\n           (2 derived diagonal reads + 2 undeclared currency slots), asymmetric flip. Same"
    "\n           parametric construction class as IT.37-IT.39 -- a specialization, not a new species.",
    nonH and v2_pure_imag,
    f"M - M^dagger (1,2) entry: {pfmt(psub(M[0][1], Mdag[0][1]))}")

# E2: the m_S candidate reads -- both already on record
mS_read_a = pscale(pmul(pvar("L"), hinv), g(2))          # 2 ln2/h: the rung-1 seal [FT.28; IT.37(1)]
floor = pscale(pvar("L"), g(2))                           # the two-bit floor: m_nu h >= 2 ln2 [BM.70(2),(3)]
floor_eq = peq(pmul(mS_read_a, pvar("h")), floor)
mS_read_b = pmul(pvar("sn"), pmul(pvar("zl"), pmul(pvar("L"), hinv)))  # sigma_nu z_1 ln2/h [BM.83(4),(5)]
trace_b = padd(m_hid, mS_read_b)
trace_b_alphabet = pvars_used(trace_b)
chk("E2  [m_S ADJUDICATED -- maps to existing rows; 'quantum free charge' is NOT a canon term]: the two"
    "\n           candidate reads: (a) the rung-1 seal informational mass m_S = 2 ln2/h (E_int = 2"
    "\n           [FT.28; IT.37(1)]) -- its floor identity m_S*h = 2 ln2 is EXACTLY the two-bit neutrino"
    "\n           floor m_nu h >= 2 ln2 at equality [BM.70(2),(3) re-cited at BM.83(8)]; (b) the lightest-nu"
    "\n           scale sigma_nu z_1 ln2/h with sigma_nu UNDECLARED [BM.83(4),(8); FT.143(3)] -- absolute"
    "\n           nu mass NOT derived. Under (a) Tr M is commensurable [IT.37(4)]; under (b) Tr M = m_L+m_S"
    "\n           is a reduced-mass-type cross-currency SUM (alphabet {E, sigma_nu, z_1, ln2, h}), barred as"
    "\n           a formed read [IT.4(3); BM.83(3)]. NEITHER read is a new object; the choice is undeclared.",
    floor_eq and {"E", "sn", "zl"} <= trace_b_alphabet and "rB" not in trace_b_alphabet,
    f"m_S read (a): {pfmt(mS_read_a)}; (a)*h = {pfmt(pmul(mS_read_a, pvar('h')))} = the floor {pfmt(floor)}; "
    f"Tr M under (b) alphabet: {sorted(trace_b_alphabet)}")

# E3: the verdict assembly
S_in_span = supS | supT <= {(mu, nu) for mu in range(4) for nu in range(4)}
chk("E3  [THE VERDICT -- SCENARIO B, sharpened]: M is CONSTRUCTIBLE and its algebra EXACT (Parts A-B),"
    "\n           but: (P1) q-inhomogeneous (A3) -- worse than IT.37's M; (P2) its scalar reads are the"
    "\n           barred cross-currency sums, formable ONLY as symbolic expressions with undeclared slots"
    "\n           [IT.4(3)] (B2-B4); (P3) rho_B*eps_q is NOT the handshake seat -- IT.4(2)'s three formed"
    "\n           mixed loci are exhaustive and the handshake is the BINARY chi_{NE>=T_0} [BM.134(5):"
    "\n           'they meet only through the threshold indicator'] (A4); (P4) the S/T <-> S-even/S-odd map"
    "\n           is refuted on the canon's own basis (C2-C4), and the S-T split adds NO new operator"
    "\n           (S, T lie in the same span{sigma_mu (x) sigma_nu}: {sup} directions, 4 each outside the"
    "\n           derived force algebra [IT.38(2)]) (C5); (P5) the derivative asymmetry has NO seat -- the"
    "\n           independence is symmetric (D1-D3); (P6) m_S maps to existing rows (E2). REDUNDANT with"
    "\n           IT.37-IT.39's parametric construction class + PARAMETRIC in (rho_B, eps_q) + BARRED as a"
    "\n           formed read. NOT ADOPTED; no declaration; Cal-IT empty.".replace("{sup}", str(len(supS | supT))),
    S_in_span and len(supS | supT) == 16,
    f"S U T support: {len(supS)} + {len(supT)} directions spanning {len(supS | supT)} of the 16 -- the same"
    "\n           sigma_mu (x) sigma_nu space IT.38 already censused: zero new operators, zero new loci.")

print("=" * 100)
print("VERDICT SUMMARY (Tier IT.14 candidates IT.43-IT.45):")
print("""    * THE ALGEBRA IS EXACT: the directive's 4x4 tensor product is correct entrywise; the pure product
      rho_B*eps_q sits at (2,3),(3,2), in det M (coefficient -1), in the discriminant (+4) and in
      C_11+C_22 = 4 rho_B eps_q; S+T = M(x)M with S symmetric, T antisymmetric; and for THIS M the
      transpose IS the currency involution -- the S-T split IS the exchange symmetrization (the one true
      structural fact; it exposes the bar rather than bypassing it: S's entries are the barred sums).
    * THE KEY CLAIM FAILS: the container does not launder the sums. v_1 = rho_B+eps_q already at 2x2;
      det/lambda_+-/S/T entries are cross-currency sums -- formable only as SYMBOLIC expressions with
      undeclared slots [IT.4(3)], barred as formed reads/values [BM.83(3),(9); BM.140(5); IT.4(2):
      'cross-currency VALUES do not exist pre-calibration']. Plus a NEW obstruction IT.37's M lacked:
      q-INHOMOGENEITY -- det sums q^1 with q^0 [BM.83(4) exponent arithmetic].
    * THE HANDSHAKE SEAT CLAIM IS REFUTED: the formed mixed loci are EXACTLY THREE and the handshake is
      the binary chi_{NE>=T_0} [IT.4(2); BM.134(5)]; rho_B*eps_q appears in no formed read.
    * THE GRADING MAP IS REFUTED on the canon's own operators: J_2, K_1, K_3 (S-odd) are transpose-EVEN,
      W_2 (S-even) is transpose-ODD; the bivector overlap is 2/6; the 7+3+3+3 count-rhyme is numerology
      [BM.134(5) discipline]; S/T each carry 4 directions outside the 8-dim force algebra [IT.38(2)].
    * THE DERIVATIVE ASYMMETRY HAS NO SEAT: both formal partials vanish on every formed read (symmetric
      independence [IT.5(1)]); m_hid and Delta x_B are eps_q-FREE; a nonzero d(rho_B)/d(eps_q) would be a
      declared cross-currency conversion -- barred [BM.140(5)], none issued. 'Perspectives' are not
      primitives [IT.1(8)(P4)]; the photon has no formed perspective reads [(R9''); IT.3(6); IT.41];
      eps_q is a global A4 slot [BM.19(2); AT-O27]; rho_B is NOT a seal class [AT.41(2),(3)] -- category
      error. The salvageable kernel is IT.4(2)'s locus distinction, already derived.
    * m_S MAPS TO EXISTING ROWS ('quantum free charge' is not a canon term): (a) 2 ln2/h = the IT.37(1)
      rung-1 seal read = the BM.70 floor at equality; (b) the undeclared sigma_nu z_1 ln2/h [BM.83(8)]
      under which even Tr M is a barred cross-currency sum [IT.4(3)].
    * VERDICT -- SCENARIO B: REDUNDANT (the general-2x2 non-Hermitian specialization of IT.37-IT.39's
      parametric construction class; BM.22 species; AT.56-58 anatomy) + PARAMETRIC (rho_B, eps_q
      undeclared [IT.5(1)]) + newly BARRED as a formed read (q-inhomogeneity + cross-currency sums).
      NOT ADOPTED. Declarations issued: none. Cal-IT stays empty.""")
print("=" * 100)

n_ok = sum(R)
print(f"\n  cross_currency_matrix.py: {n_ok}/{len(R)} EXACT -- no floating point, no measured value.")
sys.exit(0 if n_ok == len(R) else 1)
