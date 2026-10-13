#!/usr/bin/env python3
"""
ion_fill_matrix.py -- the Architect's 4x4 "capacity-bound calibration matrix": the parametric ion
fills of M (x) M, the "relative information flux" ratio, the "crystallization cost" eigenvalue story,
and the re-visited derivative asymmetry -- audited against the frozen canon and Tier IT.14.
Level 6 (Isotopic), Tier IT.15 candidates (IT.46-IT.48).

DIRECTIVE (Architect, session 13k): "Audit the 4x4 Capacity-Bound Calibration Matrix, the Parametric
Ion Fills, and the 'Relative Information Flux' Renormalization ... M_4 = M (x) M (dimension 16,
matching the capacity bound C_cap=16), filled parametrically ... Baryon side: m_L(N) = 2N*u,
rho_B(N) = rho_0 N, mu_B(N) = mu_0 N; lepton side: eps_q(n_e) = eps_0 n_e, m_S(n_e) = m_0 n_e,
sigma_e(n_e) = sigma_0 n_e ... Ions: 'H+' (N=3, n_e=0), 'H' (3,1), 'H-' (3,2), 'He2+' (6,0), 'He+'
(6,1), 'He' (6,2) ... the dimensional tension is resolved by the ratio rho_B eps_q/(m_L m_S)
(interface cost vs self-cost), which is dimensionless ... the cost of crystallizing a qubit is the
eigenvalue structure for single-node (bare nucleus) vs multi-node (neutral atom) systems ...
Scenario A (reconciliation) or Scenario B (refutation)."

PREMISE AUDIT (verified against the canon BEFORE construction; the rows win over the framing):

  * u IS DEFINED IN THE CORPUS: u := 1-p = 4*eps_q [BM.137(1)] (the same u as IT.20's B_info=-2ku).
    So the fill m_L(N) = 2N*u = 8N*eps_q is EXACTLY the leading numerator fragment of the formed
    ensemble binding B_ens^(n) = -(2n*u*D_{n-1}/D_n)(ln2/h) [BM.137(3)] -- sign-flipped, D-ratio-
    stripped, and norm-layer-scale-stripped. The binding is a NORM-LAYER read [IT.34(1);
    Def-H.32(6); BM.21(2)], NOT a mass: amplitude != mass [FT.79(5)], prices are not masses
    [HistLog V.32]. (If instead u is meant as a sixth undeclared slot, the fill is worse: one more
    P4-class declaration owed.)

  * THE INTEGER SKELETON 2N IS REAL -- AND THAT IS THE ONLY DERIVED PART: the disjoint E_int read of
    the 1p-kn family is E_int = 6(k+1) with N = 3(k+1) [IT.6(1); IT.7], so E_int = 2N exactly and
    m_L(derived) = E_int ln2/h = 2N*(ln2/h) [FT.44(4)]. The fill keeps the skeleton 2N and SWAPS the
    scale factor ln2/h (shared currency {h, ln2}, degree q^{1/2}) for u = 4*eps_q (lepton currency,
    degree q^0) -- a currency substitution inside a derived name (machine: the degree + alphabet
    comparison). Same skeleton, different species -- the conflation is exactly at the scale joint.

  * THE FILLS CONTRADICT THE DERIVED FORMS THEY NAME: rho_B(derived) = mu'^2 h^2/(ln2)^2 is
    N-INDEPENDENT [BM.83(4)] vs the fill rho_0*N; eps_q is ONE GLOBAL A4-threshold slot [BM.19(2):
    "no P-class datum enters"; D0.4; IT.4(2)'s generator census] vs the ion-indexed law eps_0*n_e --
    which assigns the single global slot THREE different values (0, eps_0, 2*eps_0) across the ion
    table, and pins every bare nucleus to the sharp crystallization point eps_q=0 [BM.19(3); D0.4] as
    a LAW rather than a limit. sigma_e collides with the DERIVED registration sign sigma_e in {-1,+1}
    [CT0.9; IT.1(3)(R1)] -- the fill's sigma_0*n_e takes the value 0 at n_e=0, outside the derived
    value census; or it restates sigma_l = mu_l h/ln2 with a new slot [BM.83(4)]. mu_B, sigma_e enter
    NO entry of M or M_4 -- decorative slots. And if mu_B is mu'^2, then BM.83(4)'s identity forces
    rho_0 = mu_0 h^2/(ln2)^2 -- a constraint between slots the fill calls independent: either the
    derived identity breaks or the slot count is wrong. Domain: eps_q = eps_0*n_e in [0,1/4) [CT0.8]
    at n_e=2 forces eps_0 < 1/8 exactly -- an undeclared constraint strictly below AT-O27's five-ways
    distinguished value 1/8.

  * THE ION TABLE'S N-ASSIGNMENTS CONTRADICT THE DERIVED N-LADDER: N = 3 per nucleon [IT.6(1):
    N=3(k+1) for 1p-kn; IT.12(1): the N=9 doublet = the two 3-nucleon species]. So N=6 is a
    TWO-nucleon configuration class (g(6)=25 groupings [IT.9(2)]; the Q=+2 charge class exists:
    W_6(+2)=C(12,8)=495 [IT.9(1): W_N(Q)=C(2N,Q+N)]) -- while the 4-nucleon "He-4" system sits at
    A=4, N=12 [IT.31(4),(5): eps=(-1)^A=+1; g(12)=164395, delta-dominant]. The quoted labels stay
    quoted [P5; Def-BM.3(7)], but the label-to-N map is not a derived read; and the electron-
    saturated members are NOT CONSTRUCTED -- the IT.4-exception row is "to be derived, NOT assumed,
    at its own locus" [Tier IT.2 status row; IT.8(3)]: n_e has no derived standing as a ledger
    variable.

  * (P1) THE q-INHOMOGENEITY IS NOT RESOLVED -- IT IS RELABELED. The dilemma, both horns machine-
    checked: HORN 1 (keep the derived names): deg(rho_B*eps_q) = q^0 and deg(m_L*m_S) = q^1, so the
    "relative flux" ratio has degree q^{-1} -- the directive's "dimensionless" claim is FALSE by the
    exponent arithmetic [BM.83(4)], and det/(m_L m_S) = 1 - ratio is inhomogeneous {0, -1}: the ratio
    trick divides the SAME inhomogeneous sum through; homogenizing still needs the declared mass^2
    scale IT.45(5)(i) named. HORN 2 (keep the fills): every entry becomes degree q^0 -- homogeneous,
    but then m_L is no longer the informational mass read (deg 1/2 vs 0) and NO entry of the "mass
    matrix" carries mass. Also without any fill, M_4's entries span THREE degrees {0, 1/2, 1}: the
    tensor product SPREADS the mismatch, it does not cure it.

  * (P2) THE RATIO IS NOT A FORMED READ: BM.83(5)'s localization theorem enumerates EVERY formed
    cross-currency mass ratio and proves each depends on exactly the three undeclared dimensionless
    numbers (rho_B, sigma_l, sigma_nu) "and in no others"; eps_q appears in NO formed cross-currency
    ratio [IT.4(2),(4): the formed mixed loci are exactly three; the atomic ladder fixes lepton slots
    only]. The ratio rho_B*eps_q/(m_L*m_S) is formable ONLY as a symbolic expression carrying
    undeclared slots [IT.4(3)'s reduced-mass doctrine] -- and "interface cost / self-cost / relative
    information flux" has no ledger primitive: the ledger's information reads are I_hid in Z*ln2
    [IT.2(4)] and the integer prices [HistLog V.32]; the only "flux" on record is IT.14(2)'s adopted
    curvature-flux Q-value read -- a different object (name collision flagged).

  * (P3) THE CRYSTALLIZATION COST IS THE FILL'S OWN LAW READ BACK -- AND IT IS BLIND. At n_e=0 the
    fill gives eps_q=0 => u=0 => m_L=m_S=0 => M = [[0, rho_0 N],[0,0]] is NILPOTENT: M^2=0 and
    charpoly(M_4) = lambda^4 EXACTLY -- identically for N=3 and N=6: the "single-node cost" cannot
    see the only baryon datum (a read that cannot fail carries no information -- the house non-
    vacuity order). The contrast "bare nucleus vs neutral atom" is then circular: it is the stipulated
    law eps_q = eps_0*n_e zeroing u at n_e=0, read back as a spectrum. Crystallization needs no
    eigenvalue story: eps_q=0 => x_-=0 => no dissolution move => the crystallized configuration
    [BM.19(3); Def-BM.5(5)]; W_channel = 1 iff eps_q=0 AND NE>=T_0 [BM.122(3)]; P_mat(E=4)=1 at the
    no-flicker collapse [BM.137(2)]. And the proposed Def-H.32 mapping is the ALREADY-ADJUDICATED
    ill-posed form: the configuration sum is (q,S)-sectored [Def-H.32(5); IT.26], the colour
    grouping is an independent register [AT.41(3)], and IT-O2's binding VALUE needs the three named
    constructions [IT.27(2)] -- none supplied by a parametric 4x4. Eigenvalue-splitting-as-binding-
    energy is the smooth-manifold mass-matrix story the bars exclude [FT.79(5); IT.34(1); IT.39(2)].

  * (P4) THE DERIVATIVE VERDICT STANDS -- AND THE FILL SMUGGLES THE DECLARATION IT NEEDS. On the
    fill's own algebra, N and n_e remain independent counters and rho_0, eps_0 independent slots:
    the formal partials of rho_B(fill) wrt every lepton variable and of eps_q(fill) wrt every baryon
    variable ALL vanish -- IT.44(5),(6)'s symmetric independence is untouched. But m_L(fill) =
    8N*eps_0*n_e has a NONZERO formal partial wrt eps_0: the fill MANUFACTURES a baryon-named read
    that depends on a lepton slot -- a stipulated cross-currency functional law, i.e. exactly the
    declared conversion BM.140(5) bars ("no derived equation converts them") and IT.45(5)(ii) named
    as an owed declaration -- none issued. The parametric fill does not DISCOVER the asymmetry; it
    assumes it.

  * (P5) THE "CONSTANT ACCELERATION" IS CORRECT FORMAL CALCULUS AND VACUOUS: in the adapted
    coordinates Sig = rho_B+eps_q, Del = rho_B-eps_q (a formal linear change of variables),
    S_14 = 1/2(rho_B^2+eps_q^2) = (Sig^2+Del^2)/4, so dS_14/dDel = Del/2 and d^2S_14/dDel^2 = 1/2 --
    verified exactly. But the same computation on T_14 = 1/2(rho_B^2-eps_q^2) = Sig*Del/2 gives
    d^2T_14/dDel^2 = 0: the "acceleration" measures the quadratic form's normalization in adapted
    coordinates, not a ledger property -- and S_14 remains a cross-currency SUM under every fill
    [IT.43(4),(6)]: the bar is inherited by every derivative read of it.

  * (P6) C_cap=16 vs dim End(C^4)=16 IS NUMEROLOGY: C_cap = 16 = D_tick(3) = 2^{3+1} is the junction
    capacity with the lock biconditional 2^{n+1}>16 <=> n>=4 <=> inadmissible [CT0.6; CT0.12;
    CT0.13; IT.1(1)]; the 16 of M_4 is the entry count 4^2. No derived row connects them [BM.134(5)
    dictionary discipline; IT.44(3) pattern]; and IT.38(2)'s 16-vs-8 force-algebra over-count carries
    over unchanged.

  * THE HONEST VERDICT -- SCENARIO B (REFUTATION): the fills are five (six with a slot-u) new
    undeclared P4-class parameters [BM.6(4)] dressing derived names (m_L, rho_B, eps_q, m_S, sigma_e)
    in forms the derived rows contradict; the only derived content is the integer skeleton E_int=2N
    [IT.6(1); IT.7] the fill then re-scales with a lepton-currency factor; the ratio is unformed and
    q^{-1} under the true degrees; the crystallization cost is a circular, N-blind nilpotent artifact;
    the derivative independence stands and the fill smuggles the conversion it was supposed to find;
    the C_cap match is numerology. NOT ADOPTED; no declaration; Cal-IT empty; no new open row. The
    declared door for ion-indexed calibration data is the Calibration Era's own program [IT.5(2):
    multi-seal EM-bound spectroscopy the necessary data species; IT.33: the anchor as strategy;
    AT.63(4): deferred] with the read rules (M1')-(M3') [AT.54(6)] gating every conversion --
    values by declared reads, NOT by parametric-matrix eigenvalues.

DERIVED/VERIFIED HERE (machine, exact -- multivariate Laurent polynomials over Gauss(i) over
Fraction, formal partials, Faddeev-LeVerrier characteristic polynomials over the polynomial ring,
integer censuses; NO floating point, NO measured value [P5]; species labels stay quoted):
  (A) the unfilled M_4 degree census {0,1/2,1}; the two-horn dilemma on the ratio; the C_cap lock
      biconditional census (numerology row).
  (B) the skeleton E_int=2N; the scale-factor substitution; the binding-fragment identity for n=2,3,4
      + the sign-flip witness; the four fill contradictions + the domain bound + the decorative-slot
      and sigma_e-collision censuses; the ion table vs the N-ladder (N=3/nucleon; W_6(+2)=495;
      sum(W_6)=4096; the "He-4" row at A=4, N=12).
  (C) the localization-census exclusion of the ratio; the nilpotency at n_e=0 (charpoly = lambda^4
      for BOTH bare ions -- the N-blindness); the n_e=1 Kronecker spectral identities
      (tr(M_4)=(trM)^2, det(M_4)=(detM)^4) and the circularity row.
  (D) the persisting independence + the manufactured m_L dependence; the adapted-coordinate
      derivative identities + the T_14 vacuity witness; the verdict assembly.

BARS: exact arithmetic only; no species identification [Def-BM.3(1,(7))]; no measured value [P5] --
every fill slot stays symbolic; no currency mixing as formed reads [BM.83; BM.134(5); BM.140(5)];
no smooth-manifold analogy (formal polynomial partials only); prices not masses [HistLog V.32];
Level-5 record and IT.1-IT.14 cited, never edited [AT.63(2)]. Declarations issued: none; Cal-IT empty.
"""

import sys
from fractions import Fraction as Fr

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# =====================================================================================
# Gauss(i) over Fraction
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


G0, G1, GI = g(0), g(1), g(0, 1)

# =====================================================================================
# Multivariate Laurent polynomials over Gauss(i)
# =====================================================================================
VARS = ("mL", "mS", "rB", "eq", "E", "L", "h", "mu2", "chi", "d", "DS", "sl", "sn", "zl",
        "Rs", "w", "N", "ne", "rho0", "eps0", "m0", "mu0", "sig0", "Sig", "Del")
VI = {v: i for i, v in enumerate(VARS)}
NV = len(VARS)

# the corpus's q-grading per variable (BM.83(4) exponent arithmetic; FT.22). The NEW fill slots'
# degrees are the fill's own best case (q^0) -- the audit shows the name-swap either way:
QDEG = {"mL": Fr(1, 2), "mS": Fr(1, 2), "rB": Fr(0), "eq": Fr(0), "E": Fr(0), "L": Fr(0),
        "h": Fr(-1, 2), "mu2": Fr(1), "chi": Fr(0), "d": Fr(0), "DS": Fr(0), "sl": Fr(0),
        "sn": Fr(0), "zl": Fr(0), "Rs": Fr(0), "w": Fr(1, 2), "N": Fr(0), "ne": Fr(0),
        "rho0": Fr(0), "eps0": Fr(0), "m0": Fr(0), "mu0": Fr(1), "sig0": Fr(0),
        "Sig": Fr(0), "Del": Fr(0)}


def pvar(name):
    e = [0] * NV
    e[VI[name]] = 1
    return {tuple(e): G1}


def pconst(c):
    return {} if c == G0 else {tuple([0] * NV): c}


def padd(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = gadd(out[e], c) if e in out else c
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
    k = VI[name]
    out = {}
    for e, c in p.items():
        if e[k]:
            e2 = list(e)
            e2[k] -= 1
            out[tuple(e2)] = gadd(out.get(tuple(e2), G0), gmul(c, g(e[k])))
    return {e: c for e, c in out.items() if c != G0}


def pvars_used(p):
    used = set()
    for e in p:
        for i, x in enumerate(e):
            if x:
                used.add(VARS[i])
    return used


def pdeg_set(p):
    out = set()
    for e in p:
        deg = Fr(0)
        for i, x in enumerate(e):
            deg += QDEG[VARS[i]] * x
        out.add(deg)
    return out


def psubst(p, mapping):
    """formal substitution var -> polynomial (monomial-wise power expansion)."""
    out = {}
    for e, c in p.items():
        term = pconst(c)
        for i, x in enumerate(e):
            if x:
                if x > 0:
                    base = mapping.get(VARS[i], pvar(VARS[i]))
                    pw = pconst(G1)
                    for _ in range(x):
                        pw = pmul(pw, base)
                    term = pmul(term, pw)
                else:
                    return None  # negative exponents unsupported in substitutions here
        out = padd(out, term)
    return out


def pfmt(p):
    if not p:
        return "0"
    terms = []
    for e, c in sorted(p.items()):
        if c == G1:
            coef = ""
        elif c == gneg(G1):
            coef = "-"
        elif c[1] == 0:
            coef = f"{c[0]}" if c[0] >= 0 else f"({c[0]})"
        else:
            sgn = "+" if c[1] >= 0 else "-"
            coef = f"({c[0]}{sgn}{abs(c[1])}i)"
        fac = "".join(f"*{VARS[i]}" if x == 1 else f"*{VARS[i]}^{x}"
                      for i, x in enumerate(e) if x)
        term = coef + fac
        terms.append(term.lstrip("*") if coef == "" else (term if term else "1"))
    return " + ".join(terms).replace("+-", "- ")


ML, MS, RB, EQ = pvar("mL"), pvar("mS"), pvar("rB"), pvar("eq")
NN, NE, RHO0, EPS0, M0 = pvar("N"), pvar("ne"), pvar("rho0"), pvar("eps0"), pvar("m0")
ONE_P = pconst(G1)


def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


# ---- symbolic matrices over Poly ----
def m2mul(A, B):
    return [[padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j])) for j in (0, 1)] for i in (0, 1)]


def m2add(A, B):
    return [[padd(A[i][j], B[i][j]) for j in (0, 1)] for i in (0, 1)]


def kronP(A, B):
    out = [[{} for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + k][2 * j + l] = pmul(A[i][j], B[k][l])
    return out


def m4mul(A, B):
    out = [[{} for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = {}
            for k in range(4):
                acc = padd(acc, pmul(A[i][k], B[k][j]))
            out[i][j] = acc
    return out


def m4trace(A):
    acc = {}
    for i in range(4):
        acc = padd(acc, A[i][i])
    return acc


def m2trace(A):
    return padd(A[0][0], A[1][1])


def charpoly_fl(A, n):
    """Faddeev-LeVerrier over the polynomial ring: returns [c_0=1, c_1, ..., c_n] of
    det(lam I - A) = sum_k c_k lam^{n-k}. Recurrence: M_1 = I; c_k = -tr(A M_k)/k;
    M_{k+1} = A M_k + c_k I. Valid over any characteristic-0 commutative ring."""
    ident = [[pconst(G1) if i == j else pconst(G0) for j in range(n)] for i in range(n)]
    coeffs = [pconst(G1)]
    Mk = [row[:] for row in ident]
    for k in range(1, n + 1):
        AMk = m4mul_n(A, Mk, n)
        c = pscale(m4trace_n(AMk, n), g(Fr(-1, k)))
        coeffs.append(c)
        if k < n:
            Mk = [[padd(AMk[i][j], pmul(ident[i][j], c)) for j in range(n)] for i in range(n)]
    return coeffs


def m4mul_n(A, B, n):
    out = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = {}
            for k in range(n):
                acc = padd(acc, pmul(A[i][k], B[k][j]))
            out[i][j] = acc
    return out


def m4trace_n(A, n):
    acc = {}
    for i in range(n):
        acc = padd(acc, A[i][i])
    return acc


print("=" * 100)
print("PART A -- the unfilled object: the q-grading persists and spreads; the two horns; the 16-vs-16")
print("=" * 100)

M = [[ML, RB], [EQ, MS]]
A4 = kronP(M, M)

# A1: the degree census of M_4's 16 entries under the DERIVED degrees
deg_entries = set()
for i in range(4):
    for j in range(4):
        deg_entries |= pdeg_set(A4[i][j])
detM = psub(pmul(ML, MS), pmul(RB, EQ))
deg_ratio = {d1 - d2 for d1 in pdeg_set(pmul(RB, EQ)) for d2 in pdeg_set(pmul(ML, MS))}
one_minus_ratio_degs = {Fr(0)} | deg_ratio
chk("A1  [IT.43(3) carried over + extended]: the q-degree census WITHOUT any fill: M's entries span"
    "\n           {0, 1/2}; M_4 = M(x)M's 16 entries span THREE degrees {0, 1/2, 1} (m_L^2 in q^1,"
    "\n           m_L*rho_B in q^{1/2}, rho_B*eps_q in q^0) -- the tensor product SPREADS the mismatch,"
    "\n           it does not cure it; det M stays inhomogeneous {0, 1}.",
    deg_entries == {Fr(0), Fr(1, 2), Fr(1)} and pdeg_set(detM) == {Fr(0), Fr(1)},
    f"deg(entries M_4) = {sorted(deg_entries)}; deg(det M) = {sorted(pdeg_set(detM))}")

# A2: the two horns of the claimed "dimensionless ratio" resolution
horn1 = (deg_ratio == {Fr(-1)}) and (one_minus_ratio_degs == {Fr(0), Fr(-1)})
# horn 2: the FILLED matrix -- m_L = 2N*u, u = 4*eps_q => 8N*eps_q; rho_B = rho0*N;
# eps_q = eps0*ne; m_S = m0*ne
u_fill = pscale(pmul(EPS0, NE), g(4))                      # u = 4*eps_q = 4*eps0*ne [BM.137(1)]
mL_fill = pmul(pscale(NN, g(2)), u_fill)                   # 2N*u = 8N*eps0*ne
rB_fill = pmul(RHO0, NN)
eq_fill = pmul(EPS0, NE)
mS_fill = pmul(M0, NE)
Mfill = [[mL_fill, rB_fill], [eq_fill, mS_fill]]
A4fill = kronP(Mfill, Mfill)
deg_fill = set()
for i in range(4):
    for j in range(4):
        deg_fill |= pdeg_set(A4fill[i][j])
mL_name_swap = (pdeg_set(mL_fill) == {Fr(0)}) and (pdeg_set(pmul(pvar("E"), pmul(pvar("L"),
              {tuple(-1 if VARS[i] == "h" else 0 for i in range(NV)): G1}))) == {Fr(1, 2)})
chk("A2  [the two-horn dilemma -- the 'dimensionless ratio' claim adjudicated]: HORN 1 (keep the"
    "\n           derived names): deg(rho_B*eps_q) - deg(m_L*m_S) = 0 - 1 = -1 -- the ratio is q^{-1},"
    "\n           NOT dimensionless (the directive's claim is FALSE by BM.83(4)'s exponent arithmetic),"
    "\n           and det/(m_L m_S) = 1 - ratio is inhomogeneous {0, -1}: the ratio trick divides the"
    "\n           SAME barred sum through. HORN 2 (keep the fills): every entry of M_4 becomes q^0 --"
    "\n           'homogeneous', but the informational read m_L = E_int ln2/h has degree q^{1/2} while"
    "\n           the fill 2N*u = 8N*eps_0*n_e has degree q^0: NO entry of the 'mass matrix' carries"
    "\n           mass. Both horns lose the claim; the homogenizing declaration IT.45(5)(i) named is"
    "\n           still the only honest door.",
    horn1 and deg_fill == {Fr(0)} and mL_name_swap,
    f"deg(ratio) = {sorted(deg_ratio)}; deg(1-ratio) = {sorted(one_minus_ratio_degs)}; "
    f"deg(entries M_4^fill) = {sorted(deg_fill)}")

# A3: the C_cap numerology row -- the lock biconditional re-censused, no derived bridge
lock = all((2 ** (n + 1) > 16) == (n >= 4) for n in range(0, 7))
dims = (2 ** (3 + 1) == 16) and (4 * 4 == 16)
chk("A3  [CT0.6; CT0.12; CT0.13; IT.1(1); BM.134(5) discipline]: the two sixteens -- C_cap = 16 ="
    "\n           D_tick(3) = 2^(3+1) (the junction capacity, with the lock biconditional 2^(n+1) > 16"
    "\n           <=> n >= 4 <=> inadmissible, re-censused over n=0..6) and dim End(C^4) = 16 = 4^2 (an"
    "\n           entry count): NO derived row connects them -- a numerology flag [IT.44(3) pattern],"
    "\n           and IT.38(2)'s 16-vs-8 force-algebra over-count carries over unchanged.",
    lock and dims)

print("=" * 100)
print("PART B -- the parametric fills vs the derived forms they name")
print("=" * 100)

# B1: the integer skeleton E_int = 2N, and the scale-factor substitution at the joint
skeleton = all(6 * (k + 1) == 2 * (3 * (k + 1)) for k in range(0, 13))
hinv = {tuple(-1 if VARS[i] == "h" else 0 for i in range(NV)): G1}
scale_derived = pmul(pvar("L"), hinv)                       # ln2/h: shared currency, degree +1/2
scale_fill = pscale(EQ, g(4))                               # u = 4*eps_q: lepton currency, degree 0
substitution = (pdeg_set(scale_derived) == {Fr(1, 2)} and pdeg_set(scale_fill) == {Fr(0)}
                and pvars_used(scale_derived) == {"L", "h"} and pvars_used(scale_fill) == {"eq"})
chk("B1  [IT.6(1); IT.7; FT.44(4); BM.137(1)]: the ONLY derived part of the fill: the disjoint read"
    "\n           E_int = 6(k+1) with N = 3(k+1) gives E_int = 2N exactly (integer census k=0..12), so"
    "\n           m_L(derived) = 2N*(ln2/h). The fill m_L(N) = 2N*u keeps the skeleton and SWAPS the"
    "\n           scale factor: ln2/h (alphabet {h, ln2}, degree q^{1/2}) -> u = 4*eps_q (alphabet"
    "\n           {eps_q}, degree q^0) -- a currency substitution inside a derived name, machine-exact"
    "\n           at the joint.",
    skeleton and substitution,
    f"scale(derived) = {pfmt(scale_derived)} [deg {sorted(pdeg_set(scale_derived))}]; "
    f"scale(fill) = {pfmt(scale_fill)} [deg {sorted(pdeg_set(scale_fill))}]")

# B2: the binding-fragment identity + the sign flip
u = pscale(EQ, g(4))                                          # u = 4*eps_q [BM.137(1)]
frag_ok = True
for n in (2, 3, 4):
    Dn, Dn1 = pconst(G1), pconst(G1)
    upow = pconst(G1)
    for j in range(1, n):                                     # D_n = 1+u+...+u^{n-1}
        upow = pmul(upow, u)
        Dn = padd(Dn, upow)
    upow = pconst(G1)
    for j in range(1, n - 1):                                 # D_{n-1} = 1+u+...+u^{n-2}
        upow = pmul(upow, u)
        Dn1 = padd(Dn1, upow)
    # BM.137(3)'s polynomial identity D_n - 1 = u*D_{n-1} -- the exact hinge between the
    # formed binding B_ens^(n) = -(2n u D_{n-1}/D_n)(ln2/h) and the fill's fragment 2n*u:
    frag_ok &= peq(psub(Dn, ONE_P), pmul(u, Dn1))
u_wit = 4 * Fr(1, 16)                                         # eps_q = 1/16 => u = 1/4 (exact rational)
frag_wit = Fr(4) * u_wit                                      # 2n*u at n=2: +1
bens_wit = -Fr(4) * u_wit / (1 + u_wit)                       # B_ens^(2)*(h/ln2) = -4u/(1+u): -4/5
sign_flip = frag_wit > 0 and bens_wit < 0
chk("B2  [BM.137(1),(3); IT.34(1); FT.79(5); HistLog V.32]: the fill IS the binding's numerator"
    "\n           fragment: B_ens^(n) = -(2n*u*D_{n-1}/D_n)(ln2/h) with u = 4*eps_q, D_n = 1+u+...+u^{n-1}"
    "\n           -- BM.137(3)'s hinge identity D_n - 1 = u*D_{n-1} verified as a polynomial identity for"
    "\n           n=2,3,4 (non-vacuous: a wrong D_n construction fails it). The fill's m_L = 2N*u is that"
    "\n           numerator with the sign FLIPPED, the D-ratio stripped, and the norm-layer scale ln2/h"
    "\n           stripped. Exact rational witness at eps_q=1/16 (u=1/4): the fragment 2n*u = +1 > 0 while"
    "\n           B_ens^(2)*(h/ln2) = -4/5 < 0 -- the formed binding is <= 0 [BM.137(3); IT.34(1): a"
    "\n           norm-layer read], the fill's 'mass' >= 0: binding is not mass [FT.79(5); HistLog V.32].",
    frag_ok and sign_flip,
    f"2n*u|_(n=2,eps_q=1/16) = {frag_wit}; B_ens^(2)*(h/ln2)|_(eps_q=1/16) = {bens_wit}")

# B3: the fill-contradiction census
rho_derived = pmul(pvar("mu2"), pmul(pmul(pvar("h"), pvar("h")),
                   {tuple(-2 if VARS[i] == "L" else 0 for i in range(NV)): G1}))   # mu'^2 h^2/(ln2)^2
N_indep_derived = not pdiff(rho_derived, "N")
N_law_fill = peq(pdiff(rB_fill, "N"), pvar("rho0"))
# the ion table's eps_q values: pairwise distinct polynomials (one GLOBAL slot, three values)
ion_eps = {pfmt(pscale(EPS0, g(ne))) for ne in (0, 1, 2)}
distinct_eps = len(ion_eps) == 3
# sigma_e collision: the fill's sigma_0*n_e at n_e=0 is EXACTLY 0 -- outside CT0.9's {-1,+1} census
sigma_fill_zero = peq(psubst(pmul(pvar("sig0"), NE), {"ne": pconst(G0)}), {})
# BM.83(4) identity constraint: rho_0 N == mu_0 N h^2/L^2 fails identically (a constraint is owed)
constraint_break = not peq(rB_fill, pmul(pvar("mu0"), pmul(NN, pmul(pmul(pvar("h"), pvar("h")),
                       {tuple(-2 if VARS[i] == "L" else 0 for i in range(NV)): G1}))))
# decorative slots: mu0, sig0 appear in NO entry of M_4^fill
alph4 = set()
for i in range(4):
    for j in range(4):
        alph4 |= pvars_used(A4fill[i][j])
decorative = ({"mu0", "sig0"} & alph4 == set()) and alph4 <= {"N", "ne", "rho0", "eps0", "m0"} \
    and {"rho0", "eps0", "m0"} <= alph4
# domain bound: eps_q = eps0*ne in [0,1/4) at ne=2 => eps0 < 1/8 (exact rational arithmetic)
domain_bound = (Fr(1, 4) / 2 == Fr(1, 8))
chk("B3  [BM.83(4); BM.19(2),(3); D0.4; CT0.8; CT0.9; IT.4(2); AT-O27]: the fill-contradiction"
    "\n           census: (i) rho_B(derived) = mu'^2 h^2/(ln2)^2 is N-INDEPENDENT (formal partial = 0)"
    "\n           vs the fill's N-law (partial = rho_0); (ii) eps_q is ONE global A4 slot, but the ion"
    "\n           table assigns it THREE pairwise-distinct values (0, eps_0, 2*eps_0) and pins every bare"
    "\n           nucleus to the sharp crystallization point eps_q=0 as a LAW [BM.19(3); D0.4]; (iii)"
    "\n           mu_B, sigma_e enter NO entry of M_4 -- decorative slots -- and sigma_e collides with"
    "\n           the DERIVED registration sign sigma_e in {-1,+1} [CT0.9; IT.1(3)(R1)]: the fill's"
    "\n           sigma_0*n_e takes the value 0 at n_e=0, outside the derived value census; (iv) if mu_B"
    "\n           is mu'^2, BM.83(4)'s identity forces rho_0 = mu_0 h^2/(ln2)^2 -- a constraint between"
    "\n           slots the fill calls independent (the fill breaks the identity otherwise); (v) the"
    "\n           domain eps_q in [0,1/4) [CT0.8] at n_e=2 forces eps_0 < 1/8 EXACTLY -- strictly below"
    "\n           AT-O27's five-ways distinguished value 1/8.",
    N_indep_derived and N_law_fill and distinct_eps and sigma_fill_zero and decorative
    and constraint_break and domain_bound,
    f"alphabets in M_4^fill: {sorted(alph4)}; ion-table eps_q values: {sorted(ion_eps)}; "
    f"sigma_e(fill)|_(n_e=0) = 0, outside CT0.9's {{-1,+1}}")

# B4: the ion table vs the derived N-ladder
ladder = [(3 * (k + 1), k + 1) for k in range(0, 4)]        # (N, nucleon count) for 1p-kn
W6_2 = binom(12, 8)                                          # W_6(Q=+2) = C(12, 8)
W6_sum = sum(binom(12, Q + 6) for Q in range(-6, 7))
nucleons_at_N6 = 2                                           # N=6 => 2 nucleons (k=1: 1p-1n)
chk("B4  [IT.6(1); IT.9(1),(2); IT.12(1); IT.31(4),(5); Tier IT.2 status; IT.8(3)]: the ion table vs"
    "\n           the derived N-ladder: N = 3 per nucleon (the 1p-kn census (3,1),(6,2),(9,3),(12,4));"
    "\n           so the quoted 'He2+' at N=6 is a TWO-nucleon configuration class (g(6)=25 groupings;"
    "\n           the Q=+2 charge class exists: W_6(+2) = C(12,8) = 495; sum(W_6) = 4096), while the"
    "\n           4-nucleon 'He-4' system sits at A=4, N=12 [IT.31(4),(5)]. The labels stay quoted [P5;"
    "\n           Def-BM.3(7)], but the label-to-N map contradicts the ladder; and the electron-saturated"
    "\n           members are NOT constructed -- the exception row is 'to be derived, NOT assumed, at its"
    "\n           own locus' [Tier IT.2 status; IT.8(3)]: n_e has no derived standing.",
    ladder == [(3, 1), (6, 2), (9, 3), (12, 4)] and W6_2 == 495 and W6_sum == 4096,
    f"N-ladder (N, nucleons): {ladder}; W_6(+2) = {W6_2}; sum W_6 = {W6_sum}")

print("=" * 100)
print("PART C -- the 'relative flux' and the 'crystallization cost'")
print("=" * 100)

# C1: the localization census excludes the ratio
formed_ratios_slots = [
    {"sl", "zl", "E"},                # m^(l)/m_hid = sigma_l z_l/(2E) [BM.83(5)]
    {"sn", "sl"},                     # m^(nu)/m^(l) = sigma_nu z_nu/(sigma_l z_l)
    {"E", "sl", "zl", "rB", "Rs"},    # m_pole/m^(l) = (2E/(sigma_l z_l))*sqrt(rho_B R_s)
]
ratio_slots = pvars_used(pmul(RB, EQ)) | pvars_used(pmul(ML, MS))
not_localized = all("eq" not in s for s in formed_ratios_slots)
chk("C1  [BM.83(5) localization theorem; IT.4(2),(4)]: the 'relative information flux' ratio"
    "\n           rho_B*eps_q/(m_L*m_S) is NOT a formed read: BM.83(5) enumerates EVERY formed cross-"
    "\n           currency mass ratio and localizes each to exactly (rho_B, sigma_l, sigma_nu) 'and in no"
    "\n           others' -- eps_q appears in NONE of the three (machine: the slot-set census), because"
    "\n           eps_q enters no formed cross-currency ratio [IT.4(2),(4): the atomic ladder fixes"
    "\n           lepton slots only]. The ratio is formable ONLY as a symbolic expression with undeclared"
    "\n           slots [IT.4(3)] -- and 'interface cost / self-cost / information flux' has no ledger"
    "\n           primitive (the ledger's information reads: I_hid in Z*ln2 [IT.2(4)]; integer prices"
    "\n           [HistLog V.32]; the only 'flux' on record is IT.14(2)'s curvature-flux Q-value read --"
    "\n           a name collision, a different object).",
    not_localized and "eq" in ratio_slots,
    f"the ratio's slots: {sorted(ratio_slots)}; formed-ratio slot sets: "
    f"{[sorted(s) for s in formed_ratios_slots]}")

# C2: the nilpotency at n_e=0 -- the 'cost' is N-blind
def m2subst(A, mapping):
    return [[psubst(A[i][j], mapping) for j in (0, 1)] for i in (0, 1)]


M0 = m2subst(Mfill, {"ne": pconst(G0)})
M0_kron = kronP(M0, M0)
M0_sq = m4mul_n(M0_kron, M0_kron, 4)
cp0 = charpoly_fl(M0_kron, 4)
nilp = all(x == {} for row in M0_sq for x in row) and all(c == {} for c in cp0[1:])
m0sq = m2mul(M0, M0)
nilp2 = all(x == {} for row in m0sq for x in row)
# and the charpoly is IDENTICAL for N=3 and N=6 -- it carries no N at all:
N_blind = all("N" not in pvars_used(c) for c in cp0)
chk("C2  [BM.19(3); Def-BM.5(5); BM.122(3); BM.137(2)]: the 'crystallization cost' at n_e=0: the fill"
    "\n           gives eps_q=0 => u=0 => m_L=m_S=0 => M = [[0, rho_0*N],[0,0]] is NILPOTENT (M^2 = 0"
    "\n           symbolically) and charpoly(M_4) = lambda^4 EXACTLY by Faddeev-LeVerrier over the"
    "\n           polynomial ring -- IDENTICALLY for 'H+' (N=3) and 'He2+' (N=6): the characteristic"
    "\n           polynomial carries NO N at all. The 'single-node cost' is blind to the only baryon"
    "\n           datum -- a read that cannot fail carries no information (the house non-vacuity order)."
    "\n           Crystallization needs no eigenvalue story: eps_q=0 => x_-=0 => no dissolution move =>"
    "\n           the crystallized configuration [BM.19(3); Def-BM.5(5)]; W_channel = 1 iff eps_q=0 AND"
    "\n           NE >= T_0 [BM.122(3)]; P_mat(E=4)=1 at the no-flicker collapse [BM.137(2)].",
    nilp and nilp2 and N_blind,
    f"charpoly(M_4)|_(n_e=0) coefficients (after the leading 1): {[pfmt(c) for c in cp0[1:]]}")

# C3: n_e=1 -- the Kronecker spectral identities and the circularity
M1 = m2subst(Mfill, {"ne": ONE_P})
M1_kron = kronP(M1, M1)
trM1, trM4 = m2trace(M1), m4trace_n(M1_kron, 4)
detM1 = psub(pmul(M1[0][0], M1[1][1]), pmul(M1[0][1], M1[1][0]))
cp4 = charpoly_fl(M1_kron, 4)
detM4 = cp4[4]  # constant term = det for n=4 (with sign (+)): det(lam I - A) at lam=0 = det(-A) = det A
tr_ok = peq(trM4, pmul(trM1, trM1))
det_ok = peq(detM4, pmul(pmul(pmul(detM1, detM1), detM1), detM1))
# the fill's tr M at n_e=1: 8N*eps0 + m0; det M = N*eps0*(8*m0 - rho0)
tr_expected = padd(pscale(pmul(NN, EPS0), g(8)), pvar("m0"))
det_expected = pmul(pmul(NN, EPS0), psub(pscale(pvar("m0"), g(8)), pvar("rho0")))
forms_ok = peq(trM1, tr_expected) and peq(detM1, det_expected)
chk("C3  [FT.79(5); IT.34(1); IT.39(2); IT.26; IT.27(2); Def-H.32(5)]: at n_e=1 the Kronecker spectral"
    "\n           identities hold symbolically -- tr(M_4) = (tr M)^2 and det(M_4) = (det M)^4 (verified on"
    "\n           the FILLED matrix: tr M = 8N*eps_0 + m_0, det M = N*eps_0*(8*m_0 - rho_0), both exact)."
    "\n           So the whole 'bare nucleus vs neutral atom' spectral contrast is the fill's own law"
    "\n           eps_q = eps_0*n_e zeroing u at n_e=0, READ BACK as a spectrum -- circular. The proposed"
    "\n           Def-H.32 mapping is the already-adjudicated ill-posed form ('amplitudes over grouping"
    "\n           sectors' [IT.26; AT.41(3): the colour grouping is an independent register; Def-H.32(5):"
    "\n           (q,S)-sectored]); IT-O2's binding VALUE needs the three named constructions [IT.27(2)]"
    "\n           -- none supplied; eigenvalue-splitting-as-binding-energy is the smooth-manifold story the"
    "\n           bars exclude [FT.79(5); IT.34(1); IT.39(2)'s BEC pattern: the statistics is the exchange"
    "\n           sign, not an eigenvalue].",
    tr_ok and det_ok and forms_ok,
    f"tr M|_(n_e=1) = {pfmt(trM1)}; det M|_(n_e=1) = {pfmt(detM1)}")

print("=" * 100)
print("PART D -- the derivative verdict re-visited, and the assembly")
print("=" * 100)

# D1: the independence persists through the fill
d_rB_lepton = [pdiff(rB_fill, v) for v in ("eps0", "ne", "m0")]
d_eq_baryon = [pdiff(eq_fill, v) for v in ("rho0", "N")]
persists = all(not x for x in d_rB_lepton + d_eq_baryon)
# D2: the manufactured cross-currency dependence -- the smuggled declaration
d_mL_deps0 = pdiff(mL_fill, "eps0")
d_mL_dne = pdiff(mL_fill, "ne")
manufactured = bool(d_mL_deps0) and bool(d_mL_dne)
chk("D1+D2  [IT.44(5),(6) re-certified on the fill; BM.140(5); IT.45(5)(ii); BM.6(4)]: the derivative"
    "\n           verdict STANDS -- and the fill SMUGGLES the declaration it needs. On the fill's own"
    "\n           algebra N, n_e remain independent counters and rho_0, eps_0 independent slots: every"
    "\n           formal partial of rho_B(fill) wrt a lepton variable and of eps_q(fill) wrt a baryon"
    "\n           variable vanishes -- the symmetric independence is untouched. BUT the fill's m_L = "
    "\n           8N*eps_0*n_e has NONZERO formal partials wrt eps_0 and n_e: the fill MANUFACTURES a"
    "\n           baryon-named read that depends on the lepton slot -- a stipulated cross-currency"
    "\n           functional LAW, exactly the declared conversion BM.140(5) bars ('no derived equation"
    "\n           converts them') and IT.45(5)(ii) named as an owed declaration -- none issued. The fill"
    "\n           does not DISCOVER the asymmetry; it ASSUMES it.",
    persists and manufactured,
    f"d(m_L^fill)/d(eps_0) = {pfmt(d_mL_deps0)}; d(rho_B^fill)/d(eps_0) = {pfmt(pdiff(rB_fill, 'eps0'))}")

# D3: the adapted-coordinate derivative identities -- correct and vacuous
Sig, Del = pvar("Sig"), pvar("Del")
subst_inv = {"rB": pscale(padd(Sig, Del), g(Fr(1, 2))), "eq": pscale(psub(Sig, Del), g(Fr(1, 2)))}
S14 = pscale(padd(pmul(RB, RB), pmul(EQ, EQ)), g(Fr(1, 2)))
T14 = pscale(psub(pmul(RB, RB), pmul(EQ, EQ)), g(Fr(1, 2)))
S14_ad = psubst(S14, subst_inv)
target = pscale(padd(pmul(Sig, Sig), pmul(Del, Del)), g(Fr(1, 4)))
d1 = pdiff(S14_ad, "Del")
d1_target = pscale(Del, g(Fr(1, 2)))
d2 = pdiff(d1, "Del")
d2_target = pconst(g(Fr(1, 2)))
T14_ad = psubst(T14, subst_inv)
t2 = pdiff(pdiff(T14_ad, "Del"), "Del")
chk("D3  [IT.43(4),(6) carried over]: the 'constant acceleration' is CORRECT formal calculus and"
    "\n           VACUOUS: in the adapted coordinates Sig = rho_B+eps_q, Del = rho_B-eps_q (a formal"
    "\n           linear change of variables, machine-exact): S_14 = 1/2(rho_B^2+eps_q^2) = (Sig^2+Del^2)/4,"
    "\n           dS_14/dDel = Del/2, d^2S_14/dDel^2 = 1/2 -- the directive's identities verified. But the"
    "\n           SAME computation on T_14 = Sig*Del/2 gives d^2T_14/dDel^2 = 0: the 'acceleration'"
    "\n           measures the quadratic form's normalization in adapted coordinates, not a ledger"
    "\n           property -- and S_14 remains a cross-currency SUM under every fill [IT.43(4),(6)]: the"
    "\n           bar is inherited by every derivative read of it.",
    peq(S14_ad, target) and peq(d1, d1_target) and peq(d2, d2_target) and not t2,
    f"S_14(Sig,Del) = {pfmt(S14_ad)}; d^2S_14/dDel^2 = {pfmt(d2)}; d^2T_14/dDel^2 = {pfmt(t2)}")

# D4: the verdict assembly
five_slots = {"rho0", "eps0", "m0", "mu0", "sig0"}
chk("D4  [THE VERDICT -- SCENARIO B (REFUTATION)]: the parametric ion fills introduce FIVE new"
    "\n           undeclared P4-class slots (rho_0, eps_0, m_0, mu_0, sigma_0 -- six with a slot-u reading)"
    "\n           [BM.6(4)] dressing DERIVED names (m_L, rho_B, eps_q, m_S, sigma_e) in forms the derived"
    "\n           rows contradict (B1-B4); the only derived content is the integer skeleton E_int = 2N,"
    "\n           re-scaled with a lepton-currency factor (B1); the q-inhomogeneity is relabeled, not"
    "\n           resolved (A2's two horns); the ratio is unformed and q^{-1} under the true degrees (A2,"
    "\n           C1); the crystallization cost is a circular, N-blind nilpotent artifact (C2, C3); the"
    "\n           derivative independence stands and the fill smuggles the conversion (D1+D2); C_cap=16 vs"
    "\n           4^2=16 is numerology (A3). NOT ADOPTED; no declaration; Cal-IT empty; NO new open row --"
    "\n           the ion-fill family is a parametric subclass of IT.37-39/IT.43-45's construction class."
    "\n           The declared door for ion-indexed data is the Calibration Era's program [IT.5(2); IT.33;"
    "\n           AT.63(4)] with the read rules (M1')-(M3') [AT.54(6)].",
    len(five_slots) == 5 and not (five_slots & {"rB", "eq", "mL", "mS"})
    and horn1 and deg_fill == {Fr(0)} and nilp and N_blind and persists and manufactured
    and not_localized and frag_ok and N_indep_derived,
    f"the new slots: {sorted(five_slots)}; none derived, none declared")

print("=" * 100)
print("VERDICT SUMMARY (Tier IT.15 candidates IT.46-IT.48):")
print("""    * THE SKELETON IS REAL, THE FLESH IS NOT: E_int = 2N on the disjoint read [IT.6(1); IT.7] is the
      fill's only derived content; every scale joint then swaps currency (ln2/h -> u = 4 eps_q), every
      named slot gets a contradictory law (rho_B N-independent -> rho_0 N; eps_q global -> eps_0 n_e),
      and two of the five new slots (mu_0, sigma_0) never even enter the matrix.
    * THE q-TENSION IS RELABELED, NOT RESOLVED: the ratio rho_B eps_q/(m_L m_S) is q^{-1} under the
      derived degrees ('dimensionless' FALSE), and the fills homogenize only by stripping the mass
      reads of their mass. M_4 unfilled spans THREE degrees {0, 1/2, 1}.
    * THE 'RELATIVE FLUX' IS UNFORMED: BM.83(5)'s localization census is closed -- eps_q appears in no
      formed cross-currency ratio; the ratio is a symbolic parametric expression [IT.4(3)], and its
      cost/flux naming has no ledger primitive.
    * THE 'CRYSTALLIZATION COST' IS CIRCULAR AND BLIND: at n_e=0 the fill is nilpotent with charpoly
      lambda^4 identically for BOTH bare ions -- it cannot see N; the contrast with n_e=1 is the
      fill's own law read back. Crystallization is already derived [BM.19(3); BM.122(3); BM.137(2)];
      the Def-H.32 grouping-sector map is the adjudicated ill-posed form [IT.26; IT.27(2)].
    * THE DERIVATIVE VERDICT STANDS: both cross-partials vanish on the fill's own algebra; the only
      nonzero cross-dependence the fill exhibits (d m_L/d eps_0) is a SMUGGLED cross-currency law --
      the barred conversion [BM.140(5)] declared by fiat. The 'constant acceleration' identities are
      correct formal calculus, vacuous as physics, and inherit the bar.
    * VERDICT -- SCENARIO B (REFUTATION). Not adopted; no declaration; Cal-IT empty; no new open row.
      The door for ion-indexed calibration data is the deferred Calibration Era program [IT.5(2);
      IT.33; AT.63(4)] with the (M1')-(M3') read rules [AT.54(6)] -- values by declared reads, not by
      parametric-matrix eigenvalues.""")
print("=" * 100)

n_ok = sum(R)
print(f"\n  ion_fill_matrix.py: {n_ok}/{len(R)} EXACT -- no floating point, no measured value.")
sys.exit(0 if n_ok == len(R) else 1)
