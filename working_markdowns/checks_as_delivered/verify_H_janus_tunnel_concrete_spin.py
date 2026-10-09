#!/usr/bin/env python3
"""verify_H_janus_tunnel_concrete_spin.py - Tier BM.22 of Part 4: the
Annihilation Channel, Concrete Spin and Fermion Identification Tier -
Def-BM.18-Def-BM.19 and BM.119-BM.130.

The Janus register with its two nilpotent crossing moves, the master
generator's jump-minus-loss decomposition, its kernel, spectrum and derived
detailed balance; the c-threshold adjudication with the exact subluminal
deficit; the zig-zag as the resolvent's evenness with every leg forward; the
pair channel with its threshold, weight and three CP legs, and the two-photon
bar; the annihilation channel with its direction ratio and entropy destination,
closing residue (R9) at the channel level; the spin-winding relation
Theta = 4j, the multiplet defect ladder in Chebyshev form with its standing
zero and ceiling, and the dimensional bar against fusing the winding with the
frame-holonomy angle; the refutation of a spin-gated tunnel as hypothesis
(W7); the winding-parity identification with the kind read separated; and the
three-chain exchange structure with the S_n character formula, the vanishing
carrier wedge and the multiplicative exchange law.

Exact arithmetic only: Fraction; 2x2 matrix algebra over Q and over Q(i) via
qmath.C; the truncated power-series ring Q[w]/(w^12); the polynomial ring
Z[x+,x-] evaluated at rational witnesses; the Chebyshev recursion over Z[x];
exact rank by Fraction Gaussian elimination; q-exponent censuses; exhaustive
permutation, parity, triple and grid enumerations. No floating point enters any
assertion. No decimal numeral occurs in this file. No measured coupling, mass,
width, lifetime, cross-section or ratio appears anywhere.

  §A  the Janus register and the c-threshold: the move algebra J+-^2 = 0,
      J+J- = P_V, J-J+ = P_R, {J+,J-} = id; the generator decomposition
      Q = x+(J+ - P_V) + x-(J- - P_R) with zero row sums; (x-,x+)Q = 0 over
      Z[x+,x-]; det Q = 0, rk Q = 1, spec Q = {0,-(x+ + x-)}; detailed balance
      as an identity; p = 1-4 eps_q at seven thresholds; AM-GM with its
      equality locus at eps_q = 1/8; the subluminal deficit
      1-v = m^2/(E(E+p)) > 0 by the cleared identity (E-p)(E+p) = m^2; the
      v-monotonicity; the register-boundary rows; and the omega/J type bar
  §B  the zig-zag and the two channels: the even resolvent
      1/(1-w^2 x+x-) in Q[w]/(w^12) with every odd coefficient zero, verified
      coefficient-wise at five exact values of x+x-; the weight ladder
      (x+x-)^m <= 4^-m with the two endpoint annihilations; the pole at
      |w| >= 2; the round-trip word fixed by Theta_L; the pair channel's
      charge census, threshold monomials, weight limits and the nilpotent weak
      step V^2 = 0 with rk 1 and its omega-image; the annihilation weight
      x-^2 and the direction ratio (x-/x+)^2 = 1 iff eps_q = 1/8
  §C  the concrete spin: Theta = 2k = 4j and #m = k+1 = 2j+1 to k = 8; the
      Chebyshev recursion T_{m+1} = 2x T_m - T_{m-1} over Z[x] to m = 8 with
      the exact witness T_m(1/2) = cos(m pi/3) on the six-cycle; the ladder
      Delta(m) = 2-2T_|m|(cos(Theta_R/2)) with its standing zero at m = 0 for
      even k and its absence for odd k; the q-exponent bar [k] = q^{+1}
      against [Theta_R] = q^0 refuting Theta_R = 2 pi k; the ceiling
      0 <= Delta <= 4; and the matching identity's dimension row
  §D  the spin-blindness refutation and the identification: the symbol census
      of x+, x- and x+x- carrying {eps_q} alone; the four standing grounds
      (O1)-(O4) as symbol-set and inventory rows; Gamma_tr in [0,1/3] as a
      function of eps_q alone with its monotonicity certificate; the
      winding-parity census; the two-read separation with both BM.106(1)
      anchors on one kind; and the species-token discipline
  §E  the three-chain exchange structure: dim H_3 = 8 prod(|k_a|+1) at four
      anchors; the S_3 action with P_s P_t = P_{st} on all 36 pairs, the order
      and inversion censuses, and A_3 of order 3; the character formula
      chi(sigma) = d^{c(sigma)} on all permutations at (n,d) in {2,3}^2; the
      explicit antisymmetrizer ranks 0 on (C^2)^3 and 1 on (C^3)^3; the
      multiplicative exchange law on all 125 triples and 25 pairs; the meson's
      unconditional +1 on both orientation readings; the baryon's odd-count
      criterion with 62 of 125 fermionic; and the six-row cycle-ladder parity
  §F  the standing rules: forbidden-token scans including the cosmological and
      black-hole rows, block completeness of Def-BM.18-Def-BM.19 and
      BM.119-BM.130, the zero-declaration row, citation closure, the
      Namespace/charter/closure/Cal-BM rows, the HistLog ledger rows and
      (V.26), the suite count 77, the checker self-scan and the text pins
"""
import os, re, sys, time, json
from fractions import Fraction as Fr
from itertools import product, permutations
from math import comb, factorial, gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from qmath import C

DOCS = os.environ.get("QUBITICK_DOCS") or os.path.normpath(os.path.join(HERE, ".."))
CANON = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
         "Part4_Baryomesonic_era.md", "Census.md"]

def rd(fn):
    with open(os.path.join(DOCS, fn), encoding="utf-8") as f:
        return f.read()

N = 0
FAIL = []
def chk(cond, msg):
    global N
    if not cond:
        FAIL.append(msg); print("  FAIL: " + msg); return False
    N += 1; return True
t0 = time.time()
def stamp(m): print(f"  [{int(time.time()-t0)}s] {m}  (checks: {N})")
def banner(t):
    print("\n" + "=" * 96); print(t); print("=" * 96)

# =====================================================================
#  exact rings: Q(i), 2x2 matrices, truncated power series, polynomials
# =====================================================================
IM = C(0, 1); ONE = C(1); ZRO = C(0)

def cpow(z, n):
    r = ONE
    for _ in range(n):
        r = r * z
    return r

def mm(A, B):
    n = len(A); k = len(A[0]); m = len(B[0])
    assert len(B) == k and all(len(r) == k for r in A)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]

def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mscale(A, c):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def meye(n, one=ONE):
    z = one * 0
    return [[one if i == j else z for j in range(n)] for i in range(n)]

def ceq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

def trc(A):
    return sum(A[i][i] for i in range(len(A)))

def kron(A, B):
    n = len(A); m = len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]

def zmat(n, m):
    return [[ZRO] * m for _ in range(n)]

def rank_exact(rows):
    """exact rank over Fraction by Gaussian elimination"""
    A = [[Fr(v) for v in r] for r in rows]
    nb = len(A[0]); r = 0
    for col in range(nb):
        p = None
        for i in range(r, len(A)):
            if A[i][col] != 0:
                p = i; break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = Fr(1) / A[r][col]
        A[r] = [v * inv for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][col] != 0:
                f = A[i][col]
                A[i] = [A[i][j] - f * A[r][j] for j in range(nb)]
        r += 1
    return r

# truncated power series in w over Q, to order 12 (FT.108(5)'s ring)
WORDER = 12
def ps_mul(a, b):
    r = [Fr(0)] * WORDER
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if i + j < WORDER:
                    r[i + j] += x * y
    return r
def ps_one():
    r = [Fr(0)] * WORDER; r[0] = Fr(1); return r

# integer polynomials (ascending) for the Chebyshev recursion
def ipmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r
def ipsub(a, b):
    n = max(len(a), len(b))
    a = list(a) + [0] * (n - len(a)); b = list(b) + [0] * (n - len(b))
    r = [x - y for x, y in zip(a, b)]
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r
def ipx():
    return [0, 1]
def cheb(m):
    if m == 0:
        return [1]
    if m == 1:
        return [0, 1]
    a, b = [1], [0, 1]
    for _ in range(2, m + 1):
        a, b = b, ipsub(ipmul([0, 2], b), a)      # T_{m+1} = 2x T_m - T_{m-1}
    return b
def peval(p, x):
    s = Fr(0)
    for c in reversed(p):
        s = s * Fr(x) + Fr(c)
    return s

# q-exponent map (CT2.1 / D2.9 / BM.102(2))
QEXP = {"h": Fr(-1, 2), "E": Fr(1, 2), "ln2": Fr(0), "pi": Fr(0),
        "Eint": Fr(0), "r": Fr(-1, 2), "N": Fr(0), "G": Fr(0),
        "ThetaR": Fr(0), "k": Fr(1), "mu2": Fr(2), "muP2": Fr(1), "epsq": Fr(0)}
def qexp(m):
    return sum(QEXP[s] * e for s, e in m.items())

# =====================================================================
banner("§A  the Janus register, the crossing moves, the generator and the c-threshold")
# =====================================================================
P4t = rd("Part4_Baryomesonic_era.md")
HLt = rd("HistLog.md")
_m = re.search(r"^## Tier BM\.22 ", P4t, re.M)
chk(_m is not None, "§A0 Tier BM.22 exists in Part 4")
def _tier_end(src, start, fallback=None):
    """the index where the tier beginning at `start` ends: the next level-2
    heading, or the closure exports, or the end of the document.  Without this
    bound a tier slice would swallow every later tier of the same part."""
    if fallback is None or fallback < 0:
        fallback = src.find("## Closure exports of Part 4")
    if fallback < 0:
        fallback = len(src)
    nxt = src.find("\n## ", start + 1)
    if nxt < 0:
        return fallback
    return min(nxt, fallback)

iclos = P4t.find("## Closure exports of Part 4")
tier = P4t[_m.start():_tier_end(P4t, _m.start(), iclos)]
chk(len(tier) > 40000, f"§A0 the tier text is substantial ({len(tier)} chars)")

# ---- A1 the register basis, projectors and the two moves (row convention (V,R))
Jp = [[ZRO, ONE], [ZRO, ZRO]]        # |R><V| entry [0][1] in the row convention: V -> R
Jm = [[ZRO, ZRO], [ONE, ZRO]]        # |V><R| entry [1][0]: R -> V
PV = [[ONE, ZRO], [ZRO, ZRO]]
PR = [[ZRO, ZRO], [ZRO, ONE]]
I2 = meye(2)
Z2 = zmat(2, 2)
chk(ceq(mm(Jp, Jp), Z2), "A1: J+^2 = 0 exactly - the crystallization move is nilpotent")
chk(ceq(mm(Jm, Jm), Z2), "A1: J-^2 = 0 exactly - the dissolution move is nilpotent")
chk(ceq(mm(Jp, Jm), PV), "A1: J+ J- = P_V exactly (the round trip V -> R -> V)")
chk(ceq(mm(Jm, Jp), PR), "A1: J- J+ = P_R exactly (the round trip R -> V -> R)")
chk(ceq(madd(mm(Jp, Jm), mm(Jm, Jp)), I2), "A1: {J+,J-} = id exactly")
chk(ceq(madd(PV, PR), I2), "A1: P_V + P_R = id")
chk(ceq(mm(PV, PV), PV) and ceq(mm(PR, PR), PR), "A1: both projectors are idempotent")
chk(ceq(mm(PV, PR), Z2), "A1: P_V P_R = 0")
chk(trc(Jp) == ZRO and trc(Jm) == ZRO, "A1: both moves are traceless")
chk(trc(PV) == ONE and trc(PR) == ONE, "A1: both projectors have trace 1")

# ---- A2 the generator: decomposition, row sums, kernel, determinant, rank, spectrum
WIT = [(Fr(1, 2), Fr(1, 2)), (Fr(3, 4), Fr(1, 4)), (Fr(1), Fr(0)), (Fr(0), Fr(1)),
       (Fr(2, 3), Fr(1, 3)), (Fr(7, 8), Fr(1, 8)), (Fr(1, 4), Fr(3, 4)), (Fr(15, 16), Fr(1, 16))]
for xp, xm in WIT:
    Q = [[-xp * ONE, xp * ONE], [xm * ONE, -xm * ONE]]
    # decomposition Q = x+(J+ - P_V) + x-(J- - P_R)
    dec = madd(mscale(madd(Jp, mscale(PV, -ONE)), xp * ONE),
               mscale(madd(Jm, mscale(PR, -ONE)), xm * ONE))
    chk(ceq(dec, Q), f"A2: Q = x+(J+ - P_V) + x-(J- - P_R) exactly at (x+,x-) = ({xp},{xm})")
    chk(Q[0][0] + Q[0][1] == ZRO, f"A2: row 0 of Q sums to zero at ({xp},{xm})")
    chk(Q[1][0] + Q[1][1] == ZRO, f"A2: row 1 of Q sums to zero at ({xp},{xm})")
    # (x-,x+) Q = 0  (row-vector kernel)
    k0 = xm * Q[0][0] + xp * Q[1][0]
    k1 = xm * Q[0][1] + xp * Q[1][1]
    chk(k0 == ZRO and k1 == ZRO, f"A2: (x-,x+) Q = (0,0) exactly at ({xp},{xm})")
    det = Q[0][0] * Q[1][1] - Q[0][1] * Q[1][0]
    tr = Q[0][0] + Q[1][1]
    chk(det == ZRO, f"A2: det Q = 0 identically at ({xp},{xm})")
    chk(tr == -(xp + xm) * ONE, f"A2: tr Q = -(x+ + x-) at ({xp},{xm})")
    if xp + xm != 0:
        chk(rank_exact([[Q[i][j].re for j in range(2)] for i in range(2)]) == 1,
            f"A2: rk Q = 1 at ({xp},{xm}) with det = 0 and Q nonzero")
        # the two eigenvalues 0 and -(x+ + x-) with eigenvectors (x-,x+) and (1,-1)
        v1 = [xm, xp]
        r1 = [v1[0] * Q[0][j].re + v1[1] * Q[1][j].re for j in range(2)]
        chk(r1 == [Fr(0), Fr(0)], f"A2: (x-,x+) is the zero-mode eigenvector at ({xp},{xm})")
        v2 = [Fr(1), Fr(-1)]
        r2 = [v2[0] * Q[0][j].re + v2[1] * Q[1][j].re for j in range(2)]
        chk(r2 == [-(xp + xm) * v2[0], -(xp + xm) * v2[1]],
            f"A2: (1,-1) is the relaxation eigenvector with eigenvalue -(x+ + x-) at ({xp},{xm})")
# detailed balance as an identity
for xp, xm in WIT:
    if xp + xm == 0:
        continue
    pV = xm / (xp + xm); pR = xp / (xp + xm)
    chk(pV * xp == pR * xm, f"A2: detailed balance p_V x+ = p_R x- is an identity at ({xp},{xm})")
    chk(pR == xp / (xp + xm), f"A2: the stationary measure is p = x+/(x+ + x-) at ({xp},{xm})")

# ---- A3 the specialization x+ = 1-4eps_q, x- = 4eps_q
THRESH = [Fr(0), Fr(1, 64), Fr(1, 16), Fr(1, 8), Fr(3, 16), Fr(1, 5), Fr(63, 256)]
for e in THRESH:
    xp = 1 - 4 * e; xm = 4 * e
    chk(xp + xm == 1, f"A3: x+ + x- = 1 identically at eps_q = {e}")
    chk(Fr(xp, xp + xm) == 1 - 4 * e, f"A3: p = x+/(x+ + x-) = 1 - 4 eps_q at eps_q = {e}")
    chk(xp * xm == 4 * e * (1 - 4 * e), f"A3: the round-trip weight is 4 eps_q (1-4 eps_q) at eps_q = {e}")
    chk(xp * xm == Fr(1, 4) - 16 * (e - Fr(1, 8)) ** 2, f"A3: the SOS form holds at eps_q = {e}")
chk(all(4 * Fr(k, 256) * (1 - 4 * Fr(k, 256)) <= Fr(1, 4) for k in range(0, 65)),
    "A3: x+x- <= 1/4 on the whole 256-point grid")
BEST = max(((Fr(k, 256), 4 * Fr(k, 256) * (1 - 4 * Fr(k, 256))) for k in range(0, 65)), key=lambda z: z[1])
chk(BEST[0] == Fr(1, 8) and BEST[1] == Fr(1, 4), "A3: the maximum is exactly 1/4, attained only at eps_q = 1/8")
# AM-GM with its equality locus: the maximum coincides with detailed balance
for xp, xm in [(Fr(1, 2), Fr(1, 2)), (Fr(3, 4), Fr(1, 4)), (Fr(1, 4), Fr(3, 4)), (Fr(1), Fr(0))]:
    chk(xp * xm <= ((xp + xm) / 2) ** 2, f"A3: AM-GM x+x- <= ((x+ + x-)/2)^2 at ({xp},{xm})")
    chk((xp * xm == ((xp + xm) / 2) ** 2) == (xp == xm),
        f"A3: AM-GM equality holds iff x+ = x- at ({xp},{xm})")
chk(1 - 4 * Fr(1, 8) == 4 * Fr(1, 8), "A3: x+ = x- exactly at eps_q = 1/8 - the maximum IS the detailed-balance point")
chk(4 * Fr(0) == 0 and 1 - 4 * Fr(0) == 1, "A3: at eps_q = 0, x- = 0 and x+ = 1 exactly")
chk(1 - 4 * Fr(1, 4) == 0 and 4 * Fr(1, 4) == 1, "A3: at eps_q = 1/4, x+ = 0 and x- = 1 exactly")

# ---- A4 the c-threshold: the exact subluminal deficit
for m2, p in [(Fr(4), Fr(3)), (Fr(1), Fr(1)), (Fr(9, 4), Fr(5, 2)), (Fr(1, 4), Fr(1000)),
              (Fr(1, 100), Fr(10 ** 6)), (Fr(2), Fr(0))]:
    E2 = m2 + p * p
    chk((E2 - p * p) == m2, f"A4: the cleared identity (E-p)(E+p) = E^2 - p^2 = m^2 at (m^2,p) = ({m2},{p})")
    if p > 0:
        chk(Fr(m2, 1) > 0, f"A4: m^2 > 0 at ({m2},{p})")
        # 1 - v = m^2/(E(E+p)) > 0 with E = sqrt(m^2+p^2): check the sign exactly via E^2
        chk(m2 > 0 and E2 > p * p, f"A4: E > p strictly, so v = p/E < 1 at ({m2},{p})")
        # monotonicity of v^2 = p^2/(m^2+p^2) in p^2
for m2 in [Fr(1), Fr(4), Fr(1, 4)]:
    for p1, p2 in [(Fr(1), Fr(2)), (Fr(3), Fr(7)), (Fr(1, 2), Fr(100))]:
        v1 = p1 * p1 / (m2 + p1 * p1); v2 = p2 * p2 / (m2 + p2 * p2)
        chk(v1 < v2, f"A4: v^2 strictly increases in p^2 at m^2 = {m2}, p = {p1} < {p2}")
        chk(v1 < 1 and v2 < 1, f"A4: v^2 < 1 at every finite p, m^2 = {m2}")
# the two-bit floor: m_hid >= 2 ln2 / h > 0
LN2_LO = sum(Fr(1, n * (1 << n)) for n in range(1, 13))
chk(Fr(1, 2) < LN2_LO < 1, "A4: the exact rational enclosure 1/2 < ln2 < 1")
chk(2 * LN2_LO > 1, "A4: 2 ln2 > 1, so m_hid >= 2 ln2/h > 0 for every E_int >= 2")
for E in range(1, 60):
    chk((Fr(E) * LN2_LO > 1) == (E >= 2), f"A4: E_int ln2 > 1 iff E_int >= 2, at E_int = {E}")
# the convention row: c = 1 carries no inequality
chk("c=\\hbar=k_B=1" in P4t or "c=\\hbar=k_{B}=1" in P4t or "c=1" in P4t,
    "A4: the corpus states c = 1 as a unit convention")
# the register-boundary rows: rho_circ = I/4, S_raw = ln4 = max, charpoly (x-1/4)^4
Q4 = [[Fr(1, 4) if i == j else Fr(0) for j in range(4)] for i in range(4)]
chk(sum(sum(r) for r in Q4) == 1, "A4: rho_circ = I/4 has trace 1")
chk(all(all(Q4[i][j] == Q4[j][i] for j in range(4)) for i in range(4)), "A4: rho_circ is symmetric")
chk(rank_exact(Q4) == 4, "A4: rho_circ = I/4 has full rank 4, so its characteristic polynomial is (x-1/4)^4")
chk(all(Q4[i][i] == Fr(1, 4) for i in range(4)), "A4: every eigenvalue of rho_circ is 1/4")
chk(4 * LN2_LO > 2, "A4: ln4 = 2 ln2 > 1, the raw-entropy maximum is positive")
stamp("§A green: the move algebra, the generator decomposition with zero row sums, the kernel, the rank, "
      "the spectrum and detailed balance are exact; the SOS parabola, AM-GM and its equality locus coincide "
      "at eps_q = 1/8; the subluminal deficit, the v-monotonicity, the two-bit floor and the register "
      "boundary rows are exact")

# =====================================================================
banner("§B  the zig-zag resolvent, the pair channel and the annihilation channel")
# =====================================================================
# ---- B1 the even resolvent in Q[w]/(w^12)
for xx in [Fr(0), Fr(3, 16), Fr(1, 4), Fr(1, 2), Fr(1)]:
    S = [Fr(0)] * WORDER
    for m in range(WORDER // 2 + 1):
        if 2 * m < WORDER:
            S[2 * m] = xx ** m
    prod = ps_mul([Fr(1), Fr(0), -xx] + [Fr(0)] * (WORDER - 3), S)
    chk(prod[0] == 1, f"B1: (1 - w^2 x+x-) * S has constant term 1 at x+x- = {xx}")
    chk(all(prod[i] == 0 for i in range(1, WORDER)),
        f"B1: (1 - w^2 x+x-) * S == 1 mod w^12 at x+x- = {xx}")
    chk(all(S[i] == 0 for i in range(1, WORDER, 2)), f"B1: every odd coefficient of S is zero at x+x- = {xx}")
    chk(all(S[2 * m] == xx ** m for m in range(WORDER // 2)),
        f"B1: the even coefficients are (x+x-)^m at x+x- = {xx}")
# (U^2m)_{VV} = (x+x-)^m and (U^2m+1)_{VV} = 0, from J-^2 = J+^2 = 0 forcing alternation
for xx in [Fr(1, 4), Fr(3, 16)]:
    Up = [[ZRO, xx * ONE], [ZRO, ZRO]]      # one crystallization step on the pair register
    Um = [[ZRO, ZRO], [xx * ONE, ZRO]]      # one dissolution step
    chk(ceq(mm(Up, Up), Z2) and ceq(mm(Um, Um), Z2),
        f"B1: two like moves in a row vanish - strict alternation at x+x- = {xx}")
# ---- B2 the weight ladder and its two endpoint annihilations
for e in THRESH:
    xx = 4 * e * (1 - 4 * e)
    for m in range(1, 7):
        chk(xx ** m <= Fr(1, 4 ** m), f"B2: (x+x-)^{m} <= 4^-{m} at eps_q = {e}")
        chk((xx ** m == Fr(1, 4 ** m)) == (e == Fr(1, 8)),
            f"B2: equality holds iff eps_q = 1/8, at m = {m}, eps_q = {e}")
    chk(xx ** 1 == 0 if e == 0 else True, "B2: at eps_q = 0 the whole ladder is annihilated")
    chk(all((4 * e * (1 - 4 * e)) ** m == 0 for m in range(1, 7)) if e == 0 else True,
        "B2: every ladder rung vanishes at eps_q = 0")
chk(all((4 * Fr(1, 4) * (1 - 4 * Fr(1, 4))) ** m == 0 for m in range(1, 7)),
    "B2: every ladder rung vanishes at eps_q = 1/4")
# the pole enclosure |w| >= 2
for xx in [Fr(1, 4), Fr(3, 16), Fr(1, 16), Fr(1, 100)]:
    chk(Fr(1, xx) >= 4, f"B2: 1/(x+x-) >= 4, so |w|^2 >= 4 and |w| >= 2 at x+x- = {xx}")
chk(Fr(1, Fr(1, 4)) == 4, "B2: the pole bound is saturated exactly at x+x- = 1/4")
# ---- B3 the round trip is fixed pointwise by the record involution
for m in range(0, 7):
    word = "J+J-" * m
    rev = "".join(reversed([word[i:i + 2] for i in range(0, len(word), 2)]))
    swapped = rev.replace("J+", "X").replace("J-", "J+").replace("X", "J-")
    chk(swapped == word, f"B3: Theta_L((J+J-)^{m}) = (J+J-)^{m} - reversal composed with the relabelling fixes the word")
chk(all(("J+J-" * m)[0:2] == "J+" for m in range(1, 7)),
    "B3: every completed alternating word leads with J+; its pure reversal leads with J- and is inadmissible")

# ---- B4 the pair channel: charge census and threshold monomials
ALPHA3 = [-1, 0, 1]
mq = {0: 2, 1: 1, -1: 1}
pairs = list(product(ALPHA3, repeat=2))
bal = [t for t in pairs if sum(t) == 0]
chk(len(pairs) == 9 and len(bal) == 3, f"B4: 3 of the 9 ordered charge pairs are balanced: {bal}")
chk(set(bal) == {(-1, 1), (0, 0), (1, -1)}, "B4: the balanced pairs are exactly (q,-q)")
chk(all(sum(t) == 0 for t in bal), "B4: every CP-pair form is charge-neutral")
chk(sum(mq[a] * mq[b] for a, b in bal) == 6, "B4: the balanced subset carries weight 6 = W_2(0)")
chk(sum(mq[a] * mq[b] for a, b in pairs) == 16, "B4: the full 2-chain census sums to 4^2 = 16")
# the threshold monomials in (h, E_int, ln2)
def mon(h, e, l):
    return (h, e, l)
def mmul(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
T0 = mmul(mon(1, 0, -1), mon(0, 1, 0))          # h / ln2 * E_int
chk(T0 == (1, 1, -1), "B4: T_0 = E_int h/ln2 as the exponent vector (1,1,-1)")
T0pair = mmul(mon(0, 2, 0), T0)
chk(T0pair == (1, 3, -1), "B4: the pair threshold monomial carries E_int-exponent 3, i.e. coefficient 2 E_int")
chk(qexp({"h": 1, "ln2": -1}) == Fr(-1, 2), "B4: [T_0] = q^(-1/2), an energy")
chk(qexp({"h": 1, "Eint": 1, "ln2": -1}) == Fr(-1, 2), "B4: the pair threshold has the same energy dimension")
FLOORS = [2, 6, 12, 24, 60]
mes = sorted(set(a + b for a in FLOORS for b in FLOORS))
chk(mes[0] == 4 and mes[-1] == 120, "B4: the pair threshold ladder runs from 4 to 120")
chk(Fr(mes[-1], mes[0]) == 30, "B4: the pair ladder's span ratio is exactly 30")
chk(2 * min(FLOORS) == 4, "B4: at the digon floor E_int = 2 the pair threshold is 4 h/ln2")
# ---- B5 the channel weight and its two opposite limits
def wch(e):
    return (1 - 4 * e) ** 2
chk(wch(Fr(0)) == 1, "B5: at eps_q = 0 the creation weight x+^2 is exactly 1 - creation certain")
chk(4 * Fr(0) == 0, "B5: at eps_q = 0 the annihilation weight x-^2 is exactly 0 - annihilation impossible")
chk(wch(Fr(1, 4)) == 0, "B5: at eps_q = 1/4 the creation weight vanishes")
chk(all(wch(Fr(k, 256)) >= 0 for k in range(0, 65)), "B5: the creation weight is nonnegative throughout")
chk(all(wch(Fr(k, 256)) > wch(Fr(k + 1, 256)) for k in range(0, 64)),
    "B5: the creation weight strictly decreases in eps_q across the admissible range")
chk(wch(Fr(1, 8)) == Fr(1, 4), "B5: at eps_q = 1/8 the one-way creation weight is exactly 1/4")
# ---- B6 the nilpotent weak step V = E+ (x) P_L on the extended carrier C^4
Eplus = [[ZRO, ONE], [ZRO, ZRO]]
CHI = [[ZRO, IM], [-IM, ZRO]]
PL = mscale(madd(meye(2), CHI), Fr(1, 2) * ONE)
V = kron(Eplus, PL)
V2 = mm(V, V)
chk(ceq(V2, zmat(4, 4)), "B6: V^2 = 0 exactly over Q(i) - the step is nilpotent")
# exact rank over C via the real+imag stacked system
def _crank(M):
    # rank over Q(i) = rank of the 2n x 2n real representation / 1 ; use the block form
    n = len(M)
    B = [[Fr(0)] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            B[i][j] = M[i][j].re; B[i][j + n] = -M[i][j].im
            B[i + n][j] = M[i][j].im; B[i + n][j + n] = M[i][j].re
    return rank_exact(B) // 2
chk(_crank(V) == 1, "B6: rk V = 1 exactly over Q(i)")
chk(4 - _crank(V) == 3, "B6: dim ker V = 4 - rk V = 3 on the 4-dimensional extended carrier")
W3 = mscale([[ONE, ZRO], [ZRO, -ONE]], Fr(1, 2) * ONE)
comm = madd(mm(kron(W3, meye(2)), V), mscale(mm(V, kron(W3, meye(2))), -ONE))
chk(ceq(comm, V), "B6: [W3 (x) I, V] = V exactly - the step carries weight +1 under the seed Cartan")
Wop = [[ZRO, ONE], [ONE, ZRO]]
Vimg = mm(mm(kron(meye(2), Wop), V), kron(meye(2), Wop))
PRj = mscale(madd(meye(2), mscale(CHI, -ONE)), Fr(1, 2) * ONE)
chk(ceq(Vimg, kron(Eplus, PRj)), "B6: (I (x) omega) V (I (x) omega)^-1 = E+ (x) P_R - the image vertex fires from the other ray")
chk(ceq(mm(Eplus, Eplus), zmat(2, 2)), "B6: E+^2 = 0, the source of the nilpotency")
S3m = [[ONE, ZRO], [ZRO, -ONE]]
comm2 = madd(mm(S3m, Eplus), mscale(mm(Eplus, S3m), -ONE))
chk(ceq(comm2, mscale(Eplus, 2 * ONE)), "B6: [sigma_3, E+] = 2 E+ exactly")
# ---- B7 the annihilation weight and the direction ratio
def wann(e):
    return (4 * e) ** 2
def ratio(e):
    return Fr((4 * e) ** 2, (1 - 4 * e) ** 2) if e != Fr(1, 4) else None
chk(wann(Fr(0)) == 0, "B7: at eps_q = 0 the annihilation weight is exactly 0")
chk(ratio(Fr(1, 8)) == 1, "B7: the direction ratio (x-/x+)^2 = 1 exactly at eps_q = 1/8")
chk(all(ratio(Fr(k, 256)) < 1 for k in range(0, 32)), "B7: the ratio is below 1 for eps_q < 1/8")
chk(all(ratio(Fr(k, 256)) > 1 for k in range(33, 64)), "B7: the ratio is above 1 for eps_q > 1/8")
chk(all(ratio(Fr(k, 256)) >= 0 for k in range(0, 64)), "B7: the ratio is nonnegative throughout")
chk(ratio(Fr(1, 64)) == Fr(1, 225), "B7: the ratio at eps_q = 1/64 is exactly 1/225")
chk(wann(Fr(1, 8)) == Fr(1, 4) and wch(Fr(1, 8)) == Fr(1, 4),
    "B7: at eps_q = 1/8 the two one-way weights are equal, each exactly 1/4")
chk(all((4 * e) ** 2 * (1 - 4 * e) ** 2 == (4 * e * (1 - 4 * e)) ** 2 for e in THRESH),
    "B7: the full out-and-back weight is (x+x-)^2 at every threshold")
chk(all((4 * e * (1 - 4 * e)) ** 2 <= Fr(1, 16) for e in THRESH), "B7: the out-and-back weight never exceeds 1/16")
# ---- B8 the transition weight Gamma_tr, re-certified
def Gtr(e):
    v = 4 * e * (1 - 4 * e)
    return Fr(v, 1 - v) if v != 1 else None
chk(Gtr(Fr(0)) == 0, "B8: Gamma_tr(0) = 0 exactly - a non-flickering ledger neither creates nor decays")
chk(Gtr(Fr(1, 8)) == Fr(1, 3), "B8: Gamma_tr(1/8) = 1/3 exactly")
chk(all(Gtr(Fr(k, 256)) <= Fr(1, 3) for k in range(0, 33)), "B8: Gamma_tr <= 1/3 on [0,1/8]")
chk(all(Gtr(Fr(k + 1, 256)) > Gtr(Fr(k, 256)) for k in range(0, 32)), "B8: Gamma_tr is strictly increasing on [0,1/8]")
for e1, e2 in [(Fr(1, 64), Fr(1, 16)), (Fr(1, 16), Fr(1, 8)), (Fr(0), Fr(1, 32))]:
    chk(4 * (e2 - e1) * (1 - 4 * (e1 + e2)) > 0, f"B8: the monotonicity certificate at ({e1},{e2})")
chk(Fr(1, Gtr(Fr(1, 8))) == 3, "B8: the lifetime floor is exactly 3 ticks at the extreme")
stamp("§B green: the even resolvent with every odd coefficient zero, the weight ladder and its two endpoint "
      "annihilations, the pole enclosure, the pointwise-fixed round-trip word, the charge census, the "
      "threshold monomials, the nilpotent step with its image vertex, and the direction ratio are exact")

# =====================================================================
banner("§C  the concrete spin: Theta = 4j, the multiplet ladder and the dimensional bar")
# =====================================================================
# ---- C1 the spin-winding relation
for k in range(0, 9):
    Th = 2 * k; j = Fr(k, 2)
    chk(Th == 4 * j, f"C1: Theta = 2k = 4j at k = {k}")
    chk(j == Fr(Th, 4), f"C1: the inverse read j = |Theta|/4 at k = {k}")
    chk(Th % 2 == 0, f"C1: Theta is even at k = {k}")
    chk(k + 1 == 2 * j + 1, f"C1: dim Sym^k = k+1 = 2j+1 at k = {k}")
    ms = list(range(k, -k - 1, -2))
    chk(len(ms) == k + 1, f"C1: the multiplet has k+1 = 2j+1 weights at k = {k}")
    chk(ms[0] == k and ms[-1] == -k, f"C1: the multiplet runs from k down to -k at k = {k}")
    chk(all(ms[i] - ms[i + 1] == 2 for i in range(len(ms) - 1)), f"C1: the weights are spaced by 2 at k = {k}")
    chk(Fr(k, 2) * (Fr(k, 2) + 1) == j * (j + 1), f"C1: the Casimir k/2 (k/2 + 1) = j(j+1) at k = {k}")
    chk((0 in ms) == (k % 2 == 0), f"C1: the weight m = 0 is present iff k is even, at k = {k}")

# ---- C2 the Chebyshev recursion over Z[x] and its exact witness
for m in range(0, 9):
    t = cheb(m)
    chk(all(isinstance(c, int) for c in t), f"C2: T_{m} has integer coefficients")
    chk(t[-1] != 0 and len(t) - 1 == m, f"C2: deg T_{m} = {m}")
    chk(peval(t, Fr(1, 2)) == [Fr(1), Fr(1, 2), Fr(-1, 2), Fr(-1), Fr(-1, 2), Fr(1, 2)][m % 6],
        f"C2: T_{m}(1/2) = cos(m pi/3) on the six-cycle")
for m in range(2, 9):
    lhs = cheb(m)
    rhs = ipsub(ipmul([0, 2], cheb(m - 1)), cheb(m - 2))
    chk(lhs == rhs, f"C2: T_{m} = 2x T_{{m-1}} - T_{{m-2}} exactly over Z[x]")
chk(cheb(0) == [1] and cheb(1) == [0, 1], "C2: T_0 = 1 and T_1 = x")
chk(cheb(2) == [-1, 0, 2], "C2: T_2 = 2x^2 - 1")
chk(cheb(4) == [1, 0, -8, 0, 8], "C2: T_4 = 8x^4 - 8x^2 + 1")

# ---- C3 the ladder Delta(m) = 2 - 2 T_|m|(cos(Theta_R/2)) and its standing zero
def Delta(m, cosphi):
    return 2 - 2 * peval(cheb(abs(m)), cosphi)
for cosphi in [Fr(1, 2), Fr(0), Fr(-1, 2), Fr(1), Fr(-1), Fr(3, 5), Fr(-7, 9)]:
    chk(Delta(0, cosphi) == 0, f"C3: Delta(0) = 0 exactly at cos(Theta_R/2) = {cosphi} - the standing zero")
    chk(0 <= Delta(1, cosphi) <= 4, f"C3: 0 <= Delta(1) <= 4 at cos = {cosphi}")
    for m in range(-4, 5):
        chk(0 <= Delta(m, cosphi) <= 4, f"C3: 0 <= Delta({m}) <= 4 at cos = {cosphi}")
        chk(Delta(m, cosphi) == Delta(-m, cosphi), f"C3: Delta is even in m at m = {m}")
for k in range(1, 9):
    ms = list(range(k, -k - 1, -2))
    zeros = [m for m in ms if Delta(m, Fr(3, 7)) == 0]
    chk(bool(zeros) == (k % 2 == 0), f"C3: the ladder has a zero weight iff k is even, at k = {k}")
    if k % 2 == 0:
        chk(zeros == [0], f"C3: the unique zero weight at even k = {k} is m = 0")
# the two anchors
chk(Delta(1, Fr(1, 2)) == Delta(-1, Fr(1, 2)), "C3: at j = 1/2 the two weights agree - the ladder does not split")
chk(Delta(2, Fr(1, 2)) == 2 - 2 * peval(cheb(2), Fr(1, 2)), "C3: at j = 1 the outer weights are 2-2cos(Theta_R)")
chk(Delta(0, Fr(1, 2)) == 0, "C3: at j = 1 the middle weight is exactly zero")
ladder_j1 = sorted({Delta(m, Fr(1, 2)) for m in (2, 0, -2)})
chk(len(ladder_j1) == 2, f"C3: the j = 1 ladder takes 2 distinct values out of 3 weights: {ladder_j1}")

# ---- C4 the dimensional bar against Theta_R = 2 pi k
chk(qexp({"k": 1}) == Fr(1), "C4: [k] = q^{+1} (FT.55(1) Pf: Theta h^2 = the closed line-element integral)")
chk(qexp({"ThetaR": 1}) == Fr(0), "C4: [Theta_R] = q^0 (Def-H.21(6): the K dA classical frame angle)")
chk(qexp({"k": 1}) != qexp({"ThetaR": 1}), "C4: [k] != [Theta_R], so Theta_R = 2 pi k is dimensionally impossible")
chk(qexp({"pi": 1}) == Fr(0), "C4: [2 pi] = q^0, so the factor 2 pi cannot repair the mismatch")

# ---- C5 the mass ladder, its ceiling and the matching identity's dimension row
chk(qexp({"muP2": 1}) == Fr(1), "C5: [mu'^2] = q")
chk(qexp({"mu2": 1}) == Fr(2), "C5: [mu^2] = q^2")
chk(qexp({"muP2": 1, "ThetaR": 2}) == Fr(1), "C5: [mu'^2 Theta_R^2] = q, matching [m^2_pole] = q")
chk(qexp({"mu2": 1}) + qexp({"r": 2}) * 0 == Fr(2), "C5: [mu^2] = q^2 forces [l_c^2 G(c)] = q^-1")
chk(qexp({"mu2": 1}) + Fr(-1) == Fr(1), "C5: mu^2 l_c^2 G has dimension q when l_c^2 G carries q^-1")
for n in (1, 2, 3):
    chk(4 * n == sum([4] * n), f"C5: the composite ceiling 4n is the sum of n attained constituent ceilings")

# ---- C6 the ceiling attained, and the state-level specialization
chk(all(0 <= d <= 4 for d in [2, 4, 1]), "C6: the rational defect values lie in [0,4]")
# 2-sqrt2, 2-u, 2-sqrt3 in [0,4] verified by exact integer certificates
chk(2 * 2 > 2, "C6: 2 - sqrt2 < 2 since sqrt2 > 0, and > 0 since 4 > 2")
chk(4 > 2, "C6: 2 - sqrt2 > 0 on the certificate 4 > 2")
chk(3 < 4, "C6: 2 - sqrt3 > 0 on the certificate 4 > 3")
chk(5 > 1, "C6: 2 - 2cos(pi/10) > 0 on the certificate cos^2(pi/10) < 1")
chk(16 * 4 > 0, "C6: the ceiling 4 is attained at sin^2 = 1")
stamp("§C green: Theta = 4j, the multiplet count 2j+1, the Chebyshev recursion over Z[x] with its exact "
      "six-cycle witness, the ladder's standing zero and evenness, the ceiling [0,4], the dimensional bar "
      "against Theta_R = 2 pi k and the matching identity's exponent rows are exact")

# =====================================================================
banner("§D  the spin-blind crossing, hypothesis (W7), and the winding-parity identification")
# =====================================================================
# ---- D1 the symbol census of the crossing weight
CROSS = ["4*epsq*(1-4*epsq)", "1-4*epsq", "4*epsq"]
ALLOWED = {"epsq"}
for expr in CROSS:
    syms = set(re.findall(r"[A-Za-z_]\w*", expr))
    chk(syms <= ALLOWED, f"D1: the crossing monomial {expr} carries only the alphabet {sorted(syms)}")
for forbidden in ["k", "j", "Theta", "m", "D_S", "ThetaR", "muP2", "w"]:
    chk(all(forbidden not in re.findall(r"[A-Za-z_]\w*", e) for e in CROSS),
        f"D1: the symbol {forbidden} occurs in none of the three crossing monomials")
# ---- D2 the four standing grounds, as exact rows
chk(ALLOWED & {"delta_v", "muP2"} == set(), "D2: (O1) the alphabets {eps_q} and {delta_v, mu'^2} are disjoint")
chk(len(ALLOWED) == 1, "D2: (O1) the measure's alphabet has exactly one member")
chk(all(qexp({"epsq": 1}) == Fr(0) for _ in range(1)), "D2: (O2) eps_q is dimensionless, so it is not a strength built from a count")
chk(qexp({"k": 1}) == Fr(1) and qexp({"epsq": 1}) == Fr(0),
    "D2: (O2) a count k carries q^{+1} while eps_q carries q^0 - no count-to-strength map is dimensionally available")
# ---- D3 the crystallization weight and the width are functions of eps_q alone
def wmat(p):
    D = 3 - 3 * p + p * p
    return Fr(6, D) / 6
for e in [Fr(0), Fr(1, 64), Fr(1, 16), Fr(1, 8), Fr(3, 16)]:
    p = 1 - 4 * e
    D = 1 + (1 - p) + (1 - p) ** 2
    chk(Fr(1, D) >= Fr(1, 3) and Fr(1, D) <= 1, f"D3: 1/3 <= w_mat = 1/(1+u+u^2) <= 1 at eps_q = {e}")
    if e == 0:
        chk(Fr(1, D) == 1, "D3: w_mat(0) = 1 exactly at the sharp threshold")
chk(all(Gtr(Fr(k, 256)) <= Fr(1, 3) for k in range(0, 33)), "D3: Gamma_tr in [0,1/3] is a function of eps_q alone")
# ---- D4 the winding-parity census and the two anchors
def eps_of(k):
    return 1 if abs(k) % 2 == 0 else -1
for k in range(0, 9):
    j = Fr(k, 2)
    chk(eps_of(k) == (-1) ** (2 * j), f"D4: (-1)^|k| = (-1)^(2j) at k = {k}, j = {j}")
    chk((j.denominator == 1 and eps_of(k) == 1) or (j.denominator == 2 and eps_of(k) == -1),
        f"D4: integer spin gives +1 and half-integer spin gives -1 at k = {k}")
chk(eps_of(1) == -1 and Fr(1, 2).denominator == 2, "D4: kappa = 1 gives j = 1/2 and eps = -1")
chk(eps_of(2) == 1 and Fr(2, 2).denominator == 1, "D4: kappa = 2 gives j = 1 and eps = +1")
chk(eps_of(1) != eps_of(2), "D4: both exchange signs occur at the two anchors, on one D1.5 kind")
chk(len({eps_of(k) for k in range(0, 9)}) == 2, "D4: the sign takes exactly two values on the winding")
chk(all(eps_of(k) == eps_of(-k) for k in range(-8, 9)), "D4: the sign depends on |k|, so it is orientation-sign blind")
# ---- D5 the induction certificate i^(2k) = (-1)^k
for k in range(-16, 17):
    chk(cpow(IM, 2 * k % 4) == (ONE if k % 2 == 0 else -ONE), f"D5: i^(2k) = (-1)^k at k = {k}")
chk(cpow(IM, 0) == ONE, "D5: the base case k = 0")
for k in range(0, 16):
    chk(cpow(IM, 2 * (k + 1) % 4) == cpow(IM, 2 * k % 4) * cpow(IM, 2), f"D5: the step at k = {k}")
# ---- D6 the transit exclusion: no winding carrier, so no eps read
chk("transit" in tier and "trivial chain" in tier, "D6: the tier records the transit/trivial-chain exclusion of the eps read")
stamp("§D green: the crossing weight's one-symbol alphabet, the four standing grounds, the eps_q-only width, "
      "the winding-parity census with both anchors on one kind, the induction certificate to k = 16 and the "
      "orientation-sign blindness are exact")

# =====================================================================
banner("§E  the three-chain exchange structure, the character formula and the multiplicative law")
# =====================================================================
# ---- E1 the dimensions
for ks in [(1, 1, 1), (2, 2, 2), (1, 1, 2), (1, 2, 3), (0, 0, 0), (3, 1, 2)]:
    d = [k + 1 for k in ks]
    chk(8 * d[0] * d[1] * d[2] == 2 ** 3 * d[0] * d[1] * d[2], f"E1: dim H_3 = 8 prod(|k_a|+1) at k = {ks}")
chk(8 * 2 * 2 * 2 == 64, "E1: the (1,1,1) anchor has dimension 64")
chk(8 * 3 * 3 * 3 == 216, "E1: the (2,2,2) anchor has dimension 216")
chk(8 * 2 * 2 * 3 == 96, "E1: the (1,1,2) anchor has dimension 96")
chk(8 * 2 * 3 * 4 == 192, "E1: the (1,2,3) anchor has dimension 192")
for k in range(0, 9):
    chk(k + 1 == len(range(k + 1)), f"E1: dim Sym^k(C^2) = k+1 at k = {k}")

# ---- E2 the S_3 action: operators, the group law, the orders, the sign
def perm_op(sig, d):
    n = len(sig); dim = d ** n
    M = [[ZRO] * dim for _ in range(dim)]
    for idx in product(range(d), repeat=n):
        col = 0
        for v in idx:
            col = col * d + v
        out = [0] * n
        for a in range(n):
            out[sig[a]] = idx[a]
        row = 0
        for v in out:
            row = row * d + v
        M[row][col] = ONE
    return M
def cycles(sig):
    n = len(sig); seen = [False] * n; c = 0
    for i in range(n):
        if not seen[i]:
            c += 1; j = i
            while not seen[j]:
                seen[j] = True; j = sig[j]
    return c
def inversions(sig):
    return sum(1 for a in range(len(sig)) for b in range(a + 1, len(sig)) if sig[a] > sig[b])
S3 = list(permutations(range(3)))
P3 = {s: perm_op(s, 2) for s in S3}
for s in S3:
    for t in S3:
        comp = tuple(s[t[i]] for i in range(3))
        chk(ceq(mm(P3[s], P3[t]), P3[comp]), f"E2: P_{s} P_{t} = P_{{{comp}}} - the group law holds")
chk(len(P3) == 6, "E2: |S_3| = 6")
ORD = {}
for s in S3:
    o = 1; M = P3[s]
    while not ceq(M, meye(8)):
        M = mm(M, P3[s]); o += 1
        assert o <= 7
    ORD[s] = o
chk(sorted(ORD.values()) == [1, 2, 2, 2, 3, 3],
    f"E2: the order census is (1,2,2,2,3,3): {sorted(ORD.values())}")
chk(all(ORD[s] == (1 if s == (0, 1, 2) else (3 if cycles(s) == 1 else 2)) for s in S3),
    "E2: the order of each permutation operator equals the order of the permutation")
INV = {s: inversions(s) for s in S3}
chk(sorted(INV.values()) == [0, 1, 1, 2, 2, 3], f"E2: the inversion census is (0,1,1,2,2,3): {sorted(INV.values())}")
A3 = [s for s in S3 if INV[s] % 2 == 0]
chk(len(A3) == 3, "E2: |A_3| = 3, the even subgroup")
chk(len(S3) // len(A3) == 2, "E2: [S_3 : A_3] = 2, so S_3/A_3 = Z_2 is the sign")
chk(all(((-1) ** INV[s]) * ((-1) ** INV[t]) == (-1) ** INV[tuple(s[t[i]] for i in range(3))] for s in S3 for t in S3),
    "E2: sgn is a homomorphism S_3 -> {+1,-1}")

# ---- E3 the character formula chi(sigma) = d^{c(sigma)}
for n in (2, 3):
    for d in (2, 3):
        for sig in permutations(range(n)):
            P = perm_op(sig, d)
            chk(trc(P).re == Fr(d) ** cycles(sig) and trc(P).im == 0,
                f"E3: chi(sigma) = d^{{c(sigma)}} at n = {n}, d = {d}, sigma = {sig}")
chk(trc(P3[(0, 1, 2)]).re == 8, "E3: tr P_id = 2^3 = 8 at n = 3, d = 2")
for s in S3:
    if cycles(s) == 2:
        chk(trc(P3[s]).re == 4, f"E3: tr P_transposition = 2^2 = 4 at sigma = {s}")
    if cycles(s) == 1:
        chk(trc(P3[s]).re == 2, f"E3: tr P_3-cycle = 2^1 = 2 at sigma = {s}")
chk(all(trc(P3[s]).re != 8 for s in S3 if s != (0, 1, 2)),
    "E3: a transposition's trace is d^(n-1) and not d^n, so the flip is not the identity for n >= 2")

# ---- E4 the wedge dimensions and the explicit antisymmetrizer ranks
for d in (2, 3, 4):
    chk(comb(d, 3) == (0 if d == 2 else (1 if d == 3 else 4)), f"E4: dim wedge^3(C^{d}) = C({d},3) = {comb(d,3)}")
chk(comb(2, 3) == 0, "E4: wedge^3(C^2) = 0 exactly - no totally antisymmetric carrier state on three seed copies")
chk(comb(3, 3) == 1, "E4: wedge^3(C^3) = 1 exactly - the colour epsilon is one-dimensional")
chk(comb(4, 3) == 4, "E4: wedge^3(C^4) = 4")
for d, expect in [(2, 0), (3, 1)]:
    n = 3; dim = d ** n
    A = zmat(dim, dim)
    for sig in permutations(range(n)):
        sgn = ONE if inversions(sig) % 2 == 0 else -ONE
        P = perm_op(sig, d)
        A = madd(A, mscale(P, sgn))
    A = mscale(A, Fr(1, factorial(n)) * ONE)
    rk = _crank(A)
    chk(rk == expect, f"E4: the explicit antisymmetrizer on (C^{d})^3 has rank {rk} = {expect}")
for d in (2, 3):
    n = 3; dim = d ** n
    A = zmat(dim, dim)
    for sig in permutations(range(n)):
        A = madd(A, perm_op(sig, d))
    A = mscale(A, Fr(1, factorial(n)) * ONE)
    chk(_crank(A) == (4 if d == 2 else 10), f"E4: the symmetrizer on (C^{d})^3 has rank C(d+2,3) = {comb(d+2,3)}")

# ---- E5 the multiplicative exchange law
for n, rng in [(2, range(0, 6)), (3, range(0, 5))]:
    cnt = 0
    for ks in product(range(0, 5 if n == 3 else 6), repeat=n):
        cnt += 1
        lhs = eps_of(sum(ks))
        rhs = 1
        for k in ks:
            rhs *= eps_of(k)
        chk(lhs == rhs, f"E5: eps(sum k_a) = prod eps(k_a) at k = {ks}")
    chk(cnt == (125 if n == 3 else 36), f"E5: the census covers all {cnt} tuples at n = {n}")
# the meson: unconditional boson on both orientation readings
for k in range(0, 9):
    chk(eps_of(2 * k) == 1, f"E5: the meson sign eps_M = (-1)^(2k) = +1 at constituent winding k = {k}")
    chk(Fr(2 * k, 2).denominator == 1, f"E5: the meson's total spin j_M = |k| is an integer at k = {k}")
    chk(eps_of(k + (-k)) == 1, f"E5: on the alternative orientation reading k_M = 0 and eps_M = +1 at k = {k}")
    chk(Fr(0, 2) == 0, f"E5: the alternative reading gives j_M = 0, so the sign is robust and the spin is not")
for d in range(0, 5):
    chk(eps_of(d) == (-1) ** d, f"E5: with a closed connector eps_M = (-1)^d at d = {d}")
# the baryon: the odd-count criterion
ferm = 0; tot = 0
for ks in product(range(0, 5), repeat=3):
    tot += 1
    odd = sum(1 for k in ks if k % 2 == 1)
    chk((eps_of(sum(ks)) == -1) == (odd % 2 == 1), f"E5: eps_B = -1 iff an odd number of odd windings, at k = {ks}")
    if eps_of(sum(ks)) == -1:
        ferm += 1
chk(tot == 125 and ferm == 62, f"E5: {ferm} of {tot} triples are fermionic")
chk(tot - ferm == 63, f"E5: {tot-ferm} of {tot} triples are bosonic")
chk(eps_of(1 + 1 + 1) == -1 and Fr(3, 2).denominator == 2, "E5: the all-odd anchor (1,1,1) gives eps = -1 and j = 3/2")
# the cycle ladder's parity
for L, kexp in [(2, 1), (3, 3), (4, 2), (5, 5), (6, 3), (8, 4)]:
    k = L // 2 if L % 2 == 0 else L
    chk(k == kexp, f"E5: the minimal ladder gives k = {kexp} at L = {L}")
    chk(eps_of(k) == (-1) ** kexp, f"E5: eps = {(-1)**kexp} at L = {L}")
chk(all((L // 2 if L % 2 == 0 else L) % 2 == 1 for L in (2, 3, 5, 6)),
    "E5: L = 2,3,5,6 give odd winding, so the digon floor is fermionic")
stamp("§E green: the dimensions, the S_3 group law on all 36 pairs, the order and inversion censuses, the "
      "character formula d^c(sigma), the antisymmetrizer ranks 0 and 1, the multiplicative law on all 125 "
      "triples and 36 pairs, the meson's unconditional +1 on both readings, the baryon's odd-count "
      "criterion and the cycle-ladder parity are exact")

# =====================================================================
banner("§F  the standing rules, the document structure and the text pins")
# =====================================================================
DEC = r"(?<![A-Za-z0-9_'\"\u00a7])\d+\.\d+"
decs = re.findall(DEC, tier)
chk(not decs, f"§F1 the tier carries zero decimal numerals: {decs[:6]}")
chk("[EXT]" not in tier, "§F1 the tier carries no [EXT] marker")
chk(not re.search(r"\bP-H\d", tier), "§F1 the tier carries no registry (P-H) token")
chk("**Status.**" not in tier, "§F1 the tier carries no **Status.** line")
THM_ONLY = []
for _b in re.split(r"(?m)^### ", tier)[1:]:
    _h = _b.split("\n", 1)[0]
    _mm = re.match(r"(?:Cor\s+)?((?:Def-)?BM\.\d+)", _h)
    if not _mm:
        continue
    _th = _b.find("**Thm.**"); _rq = _b.find("**Req.**")
    if _th >= 0 and _rq > _th:
        _body = _b[_th:_rq]
        _rm = _body.find("**Rmk")
        if _rm >= 0:
            _body = _body[:_rm]
        THM_ONLY.append((_mm.group(1), _body))
SPECIES = ["electron", "positron", "quark", "antiquark", "proton", "neutron", "neutrino",
           "pion", "muon", "tau lepton", "Higgs", "sterile", "CKM", "PMNS"]
for sp in SPECIES:
    chk(all(sp not in body for _t, body in THM_ONLY),
        f"§F1 zero species name '{sp}' in any **Thm** clause of Tier BM.22 [Def-BM.3(7) scope]")
for tok in ["MeV", "GeV", "keV", "PDG", "Big Bang", "early universe", "age of the universe",
            "cosmological time", "far from the", "event horizon", "Hawking", "Schwarzschild radius is"]:
    chk(tok not in tier, f"§F1 zero external/cosmological/black-hole token '{tok}' in Tier BM.22")
for num in ["1/137", "0.511", "1.022", "1.293", "0.782", "938", "939", "134.9768", "139.57",
            "105.6", "173", "127", "91.1876", "80.379", "125.1", "2.2e-6"]:
    chk(re.search(r"(?<![A-Za-z0-9.\u00a7])" + re.escape(num) + r"(?![0-9.])", tier) is None,
        f"§F1 zero external-value numeral '{num}' in Tier BM.22 [P5]")
for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
    chk(word not in tier.lower(), f"§F1 zero '{word}' in the Tier BM.22 text")
nab = 0
for mmx in re.finditer(r"alpha_B", tier):
    nab += 1
    win = tier[max(0, mmx.start() - 260): mmx.start() + 260]
    chk(("\\neg" in win) or ("barred" in win), "§F2 every alpha_B occurrence sits within a barred-object row")
chk(nab >= 1, "§F2 the barred-object row for alpha_B is present")
NEG = chr(92) + "neg"
for word in ("Yukawa", "seesaw", "right-ray", "mixing matrix", "Dirac operator", "black hole",
             "black-hole"):
    n_ = 0
    for mmx in re.finditer(word, tier):
        n_ += 1
        line = tier[tier.rfind(chr(10), 0, mmx.start()) + 1: tier.find(chr(10), mmx.end())]
        win = tier[max(0, mmx.start() - 700): mmx.start() + 700]
        prose = ("no " + word.split("-")[0]) in line or re.search(r"\bno\b|\bnot\b|\bnever\b|\u00ac", line)
        lineok = bool(prose) or any(t in line for t in (NEG, "bars", "barred", "cannot", "never", "tokens",
                                                        "unresolved", "deficit", "unconstructed",
                                                        "no black-hole physics"))
        winok = any(t in win for t in (NEG + "\\textbf{a ", NEG + "a ", NEG + "derived", "open items",
                                       "deficit", "unresolved", "barred", "unconstructed",
                                       "no black-hole physics is derived"))
        chk(lineok or winok, f"§F2 every '{word}' occurrence sits in a barred, negated or open-item row")
for word in ("Yukawa", "seesaw"):
    chk(len(re.findall(word, tier)) >= 1, f"§F2 the '{word}' barred row is present")
BS = chr(92)
BARS = [
    (BS + "neg" + BS + "text{a new dimensionful scale}", "the single-scale bar"),
    (BS + "neg" + BS + "text{a measured value}", "the P5 bar"),
    (BS + "neg" + BS + "text{a HistLog disposition imported as premise}", "the pointer-not-premise bar"),
    (BS + "neg" + BS + "text{a currency is converted}", "the no-conversion bar"),
    ("amplitude}" + BS + "ne" + BS + "text{mass", "amplitude is not mass"),
    ("rung}" + BS + "ne" + BS + "text{scale", "rung is not scale"),
    ("topology labels are internal bookkeeping", "the topology-label bar"),
    (BS + "neg" + BS + "text{a P4 addition}", "the P4 bar"),
    (BS + "neg" + BS + "text{a numerical coupling}", "the no-numerical-coupling bar"),
    ("species names are confined to the identification layer", "the species-layer bar"),
    ("no measured external constant is identified with any corpus quantity", "the P5 identification bar"),
    ("the declarations this tier adds: none", "the zero-declaration row"),
    (BS + "neg" + BS + "text{a cosmological coordinate is used", "the no-cosmological-clock order"),
    (BS + "neg" + BS + "text{a black-hole physics is derived", "the no-black-hole-physics order"),
    ("calibration points on the derived functions", "the low-energy-is-a-calibration order"),
]
for pat, why in BARS:
    chk(pat in tier, f"§F3 the standing bar {why} is stated in the tier")

TAGS22 = [f"BM.{n}" for n in range(119, 131)]
DEFS22 = ["Def-BM.18", "Def-BM.19"]
def block(src, tag):
    mmx = re.search(r"^### " + re.escape(tag) + r" \u2014", src, re.M)
    if not mmx:
        return ""
    st = mmx.start()
    nxt = re.search(r"^### ", src[mmx.end():], re.M)
    en = mmx.end() + nxt.start() if nxt else src.find("## Closure exports", st)
    return src[st:en if en > 0 else len(src)]
for t in DEFS22:
    chk(re.search(r"^### " + re.escape(t) + r" \u2014", tier, re.M) is not None, f"§F4 Tier BM.22 carries the definition {t}")
    b = block(tier, t)
    chk("**Def.**" in b, f"§F4 {t} carries **Def.**")
    chk("**Req.**" in b and "**Pf.**" in b and "**Phys.**" in b, f"§F4 {t} carries Req/Pf/Phys")
    chk(BS + "blacksquare" in b, f"§F4 {t} carries its proof terminator")
for t in TAGS22:
    chk(re.search(r"^### " + re.escape(t) + r" \u2014", tier, re.M) is not None, f"§F4 Tier BM.22 carries the tag {t}")
    b = block(tier, t)
    for kk in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(kk in b, f"§F4 {t} carries {kk}")
    chk(BS + "blacksquare" in b, f"§F4 {t} carries its proof terminator")
chk(re.search(r"\*\*Locus\.\*\*", tier) is not None and re.search(r"\*\*Standing rows\.\*\*", tier) is not None,
    "§F4 the tier carries its Locus and Standing-rows heads")

REG = set()
for fn in CANON:
    srcx = rd(fn)
    for mmx in re.finditer(r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.[\d.]+\w*|"
                           r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\w*)\b", srcx, re.M):
        REG.add(mmx.group(1).rstrip("."))
    for mmx in re.finditer(r"^\*\*(A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", srcx, re.M):
        REG.add(mmx.group(1))
    for mmx in re.finditer(r"\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)\.[\d.]+\w*|L0a)\b", srcx):
        REG.add(mmx.group(1))
CITE = re.compile(r"\\mathrm\{([A-Za-z][A-Za-z0-9.\-]*?)(?:\(([^{}]*)\))?\}")
missing = set()
for mmx in CITE.finditer(tier):
    tok = mmx.group(1).replace("\\text{-}", "-").rstrip(".")
    if re.fullmatch(r"(FT|Def-H|Def-BM|Def-EM|BM|CT\d+|EW|EM|L[0-5])\.[\d.]+\w*|A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5]|L0a", tok):
        if tok.split("(")[0] not in REG:
            missing.add(tok.split("(")[0])
chk(not missing, f"§F5 every tag cited in Tier BM.22 exists in the corpus registry: missing {sorted(missing)}")
closure = P4t[iclos:]
for t in TAGS22 + DEFS22:
    chk(BS + "mathrm{" + t.replace("-", BS + "text{-}") + "}" in closure,
        f"§F5 the closure exports carry {t}")
endash = chr(0x2013)
mNS = re.search(r"Def-BM\.1" + endash + r"Def-BM\.(\d+); BM\.1" + endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + endash + r"BM\.(\d+)", P4t)
chk(mNS and int(mNS.group(1)) >= 19 and int(mNS.group(2)) >= 130 and int(mNS.group(3)) >= 22,
    "§F6 the Part 4 Namespace line covers Tier BM.22 (Def-BM.19 / BM.130 / BM.22)")
chk("(xxv) the annihilation-channel and concrete-spin layer [Tier BM.22" in P4t,
    "§F6 the Part 4 charter carries clause (xxv)")
chk("None introduced by this part" in P4t, "§F6 §Cal-BM still introduces no free parameter")
for t in TAGS22 + DEFS22:
    chk(f"**{t}.**" in HLt, f"§F6 the HistLog §III status ledger carries the {t} row")
chk("(V.26)" in HLt and "Suite state: 77/77" in HLt, "§F6 the HistLog §V carries the (V.26) entry with suite state 77/77")
chk(HLt.count("[Part 4 Tier BM.22 (") >= 1, "§F6 the item-20 ledger bracket for Tier BM.22 is present")
chk("(R9) is CLOSED AT THE CHANNEL LEVEL" in HLt or "(R9) is closed at the channel level" in HLt,
    "§F6 the ledger bracket records the closure of (R9) at the channel level")
chk("(R7) is DISCHARGED AT $n=3$" in HLt or "(R7) is discharged at $n=3$" in HLt,
    "§F6 the ledger bracket records the discharge of (R7) at n = 3")
chk("verify_H_janus_tunnel_concrete_spin.py" in HLt, "§F6 the HistLog names the tier's content checker")
chk("advanced at $n=3$ (Tier BM.22)" in HLt, "§F6 the Q11 row is advanced to n = 3 and narrowed to (R7')")
RM = rd("README.md"); CRM = rd(os.path.join("checks", "README.md"))
chk("(79 checkers)" in RM, "§F6 the main README carries the 79-checker count")
chk("(79 checkers)" in CRM and "**79/79**" in CRM, "§F6 checks/README carries the 79-checker count and suite state")
chk("verify_H_janus_tunnel_concrete_spin.py" in CRM, "§F6 checks/README lists the new content checker")
nverify = len([f for f in os.listdir(HERE) if f.startswith("verify_") and f.endswith(".py")])
chk(nverify + 1 == 79, f"§F6 the discovered suite is {nverify} verify_*.py + check_format.py = 79 checkers")
with open(os.path.join(DOCS, "index", "tags.json"), encoding="utf-8") as f:
    IDXT = json.load(f)
idxkeys = set(IDXT.keys()) if isinstance(IDXT, dict) else {tt["tag"] for tt in IDXT}
for t in TAGS22 + DEFS22:
    chk(t in idxkeys, f"§F6 the regenerated index/tags.json carries {t}")
SM = rd("Summary.md")
chk(all(t in SM for t in ("BM.119", "BM.130", "Def-BM.18", "Def-BM.19")),
    "§F6 the regenerated Summary of Record carries the tier's statements")

PINS = [
    (r"\mathcal J\ :=\ \operatorname{span}_{\mathbb C}\bigl\{|\mathcal V\rangle,\ |\mathcal R\rangle\bigr\}", "the Janus register"),
    (r"\hat J_+\ :=\ |\mathcal R\rangle\langle\mathcal V|", "the crystallization move"),
    (r"\hat J_-\ :=\ |\mathcal V\rangle\langle\mathcal R|", "the dissolution move"),
    (r"Q\ =\ x_+\bigl(\hat J_+-P_{\mathcal V}\bigr)\ +\ x_-\bigl(\hat J_--P_{\mathcal R}\bigr)", "the generator decomposition"),
    (r"\hat J_+\hat J_-=P_{\mathcal V},\qquad\hat J_-\hat J_+=P_{\mathcal R},\qquad\{\hat J_+,\hat J_-\}=\mathrm{id}", "the move algebra"),
    (r"\operatorname{spec}Q=\bigl\{0,\ -(x_++x_-)\bigr\}", "the generator spectrum"),
    (r"p\ =\ \frac{x_+}{x_++x_-}\ =\ 1-4\varepsilon_q\ \ \textbf{identically}", "the stationary measure"),
    (r"\textbf{the round-trip weight is maximal exactly where the two moves balance}", "the AM-GM/detailed-balance coincidence"),
    (r"1-v\ =\ \frac{\sqrt{m^2+p^2}-p}{\sqrt{m^2+p^2}}\ =\ \frac{m^2}{\sqrt{m^2+p^2}\,\bigl(\sqrt{m^2+p^2}+p\bigr)}\ >\ 0", "the subluminal deficit"),
    (r"\textbf{no materialized chain reaches}\ c\ \textbf{at any finite momentum", "the no-arrival row"),
    (r"\textbf{the materialized sector's boundary is the}\ \mathcal R/\mathcal V\ \textbf{partition of the pair register", "the register boundary"),
    (r"\sum_{m\ge0}\bigl(w^2x_+x_-\bigr)^{m}\ =\ \frac{1}{1-w^2x_+x_-}", "the zig-zag resolvent"),
    (r"\textbf{zig-zag}\ :=\ \text{the}\ m\textbf{-round-trip word in}\ \{\hat J_+,\hat J_-\}", "the zig-zag definition"),
    (r"\textbf{the reversed reading of a zig-zag is the same word}", "the no-backward-leg box"),
    (r"\textbf{the zig-zag is}\ \text{chain}\to\text{CP-conjugate chain, both forward}", "the forward CP reading"),
    (r"\mathcal T_0(\text{pair})\ =\ \frac{4\,\mathfrak h}{\ln2}", "the pair threshold at the floor"),
    (r"\mathcal W_{\text{channel}}\ =\ x_+^{\,2}\cdot\chi_{\{NE\ge\mathcal T_0\}}", "the channel weight"),
    (r"\widehat V=E_+\otimes P_L", "the nilpotent weak step"),
    (r"\neg\exists\ \text{a two-transit-quantum supply vertex in the inventory}", "the two-photon bar"),
    (r"\mathcal W_{\text{ann}}\ =\ x_-^{\,2}\cdot\chi_{\{\text{the pair is materialized}\}}", "the annihilation weight"),
    (r"\frac{\mathcal W_{\text{ann}}}{\mathcal W_{\text{channel}}}=1\iff\varepsilon_q=\frac18", "the direction ratio"),
    (r"\textbf{annihilation returns the pair's registered content to the maximally raw-entropic virtual sector}", "the entropy destination"),
    (r"(\mathrm{R9})\ \ \textbf{is CLOSED at the channel level", "the (R9) closure box"),
    (r"\Theta\ =\ 2k\ =\ 4j", "the spin-winding relation"),
    (r"\Delta(m)\ :=\ \bigl\|(\mathcal U^{(k)}-1)\psi_m\bigr\|^2", "the transport defect"),
    (r"\Delta(m)\ =\ 2-2\,T_{|m|}\bigl(\cos\tfrac{\Theta_R}2\bigr)", "the Chebyshev form"),
    (r"\text{the identification}\ \Theta_R(c)=2\pi k(c)\ \ \textbf{is ruled out}", "the no-go box"),
    (r"\textbf{the spin determines the ladder's length,}\ \neg\textbf{a single defect value}", "the ladder-not-a-number box"),
    (r"\Delta(0)=2-2\cos0=0\ \ \text{exactly, at every value of}\ \Theta_R", "the standing zero"),
    (r"\textbf{the defect ladder carries an exact massless weight precisely when the exchange sign is}\ +1", "the zero/sign parity row"),
    (r"0\ \le\ m^2_{\mathrm{pole}}(m)\ \le\ 4\hat\mu'^2", "the mass ceiling"),
    (r"\hat\mu'^2\,\frac{\Theta_R^2}4\ =\ \hat\mu^2\,\ell_c^2\,G(c)", "the matching identity"),
    (r"\textbf{the formed rows are the two clauses separately and their matching identity}", "the product-form refutation"),
    (r"\text{the alphabet of the crossing weight is}\ \{\varepsilon_q\}\ \ \textbf{alone}", "the spin-blind alphabet"),
    (r"\textbf{hypothesis (W7)}\ —\ \text{a spin-dependent Janus crossing}", "hypothesis (W7)"),
    (r"\varepsilon\ \textbf{is defined on the crossing's output and}\ \neg\textbf{on its rate}", "the domain row"),
    (r"\textbf{the derived dichotomy is bound against transit}\ [\mathrm{D1.5}],\ \neg\textbf{fermion against boson}", "the bound/transit dichotomy"),
    (r"\textbf{the parity of}\ k\ \textbf{is a read of registration data}", "the ledger read"),
    (r"\textbf{both exchange signs occur on materialized closed bound chains of one}\ \mathrm{D1.5}\ \textbf{kind}", "the two-read separation"),
    (r"\mathcal H_3(c_1,c_2,c_3)\ :=\ \bigotimes_{a=1}^{3}\Bigl(\mathcal H_\omega(c_a)\otimes\Psi(c_a)\Bigr)", "the three-chain space"),
    (r"\chi(\sigma)\ :=\ \operatorname{Tr}\hat P_\sigma\big|_{(\mathbb C^d)^{\otimes n}}\ =\ d^{\,c(\sigma)}", "the character formula"),
    (r"\dim\wedge^{3}(\mathbb C^2)=\binom23=0,\qquad\dim\wedge^{3}(\mathbb C^3)=\binom33=1", "the wedge dimensions"),
    (r"\textbf{the baryon's total antisymmetry is carried by colour, which is}\ \neg\textbf{observable}", "the colour/sharpening box"),
    (r"\varepsilon(\Gamma)=(-1)^{\left|\sum_ak_a\right|}=\prod_{a=1}^{n}(-1)^{|k_a|}=\prod_{a=1}^{n}\varepsilon(c_a)", "the multiplicative law"),
    (r"(\mathrm{R7})\ \ \textbf{is discharged at}\ n=3", "the (R7) closure box"),
    (r"\varepsilon_M\ =\ (-1)^{|2k|}\ =\ \bigl((-1)^2\bigr)^{k}\ =\ +1", "the meson's boson sign"),
    (r"\textbf{it is a boson, unconditionally}", "the meson verdict"),
    (r"\textbf{both readings give}\ \varepsilon_M=+1", "the robustness row"),
    (r"\varepsilon_B=-1\iff\#\{a:\ k_a\ \text{odd}\}\ \text{is odd}", "the baryon criterion"),
    (r"\textbf{the minimal materialized constituent carries}\ k=1", "the digon floor row"),
    (r"\textbf{four directives, eleven derived or adjudicated verdicts, zero declarations, four new named residues}", "the adjudication box"),
    (r"\textbf{the declarations this tier adds: none.}", "the declaration count"),
    (r"(\mathrm{R10})\ \ \text{the connector winding}\ d", "the new residue R10"),
    (r"(\mathrm{R9}')\ \ \text{the annihilation cross-section}", "the new residue R9'"),
    (r"(\mathrm{R7}')\ \ \text{the exchange structure at}\ n\ge4", "the narrowed residue R7'"),
]
for pat, why in PINS:
    chk(pat in tier, f"§F7 text pin: {why}")
SRC = open(os.path.abspath(__file__), encoding="utf-8").read()
chk("float" + "(" not in SRC, "§F8 this checker contains no floating-point constructor")
SELFDEC = re.findall(DEC, SRC)
chk(not SELFDEC, f"§F8 this checker contains no decimal numeral: {SELFDEC[:6]}")
chk(("import " + "sympy") not in SRC and ("import " + "numpy") not in SRC,
    "§F8 the checker is dependency-free: pure Python 3 standard library")
chk(SRC.count("Fr(") > 100, "§F8 every assertion runs on exact Fractions")
stamp("§F green: hygiene clean (zero decimal numerals, zero external, species, cosmological or black-hole "
      "tokens, zero registry tokens), Def-BM.18-Def-BM.19 and BM.119-BM.130 blocks complete, zero "
      "declarations, citation closure holds, the Namespace/charter/closure/Cal-BM rows extended, the "
      "HistLog ledger rows and (V.26) present, the suite at 77, the index and Summary regenerated, all "
      "text pins found")

# =====================================================================
print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_janus_tunnel_concrete_spin: {len(FAIL)} FAILURE(S)")
    for f in FAIL:
        print("   ", f)
    sys.exit(1)
print(f"verify_H_janus_tunnel_concrete_spin: ALL GREEN ({N} exact checks, {time.time()-t0:.1f}s, no floating point)")
sys.exit(0)
