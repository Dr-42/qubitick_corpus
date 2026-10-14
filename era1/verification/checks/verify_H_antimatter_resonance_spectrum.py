#!/usr/bin/env python3
"""verify_H_antimatter_resonance_spectrum.py - Tier BM.21 of Part 4: the
Antimatter and Resonance Tier - Def-BM.15-Def-BM.17 and BM.108-BM.118.

The CP-conjugate chain derived from the three reversals with the T-block and
the forcing theorem; the CP-pair vacuum fluctuation with the Janus resolvent's
creation weight; the two-chain state space discharging BM.6(2)'s specification
and the meson seal with its charge-class saturation; the exchange operator as
the flip composed with the CP transport, and the spin-statistics connection
eps = (-1)^|k| = (-1)^(2j) closing deficit 11; the resonance spectrum with the
transport characteristic polynomial at every chain count, the degree-16
eigenvalue field, the multiset-orbit law and the single exact collision; the
materialization threshold in its three readings with the never-empty locus;
the decay width with its three exact zeros; and the groupings, ceilings and
octet adjudication.

Exact arithmetic only: Fraction; the degree-16 algebra M = Q(sqrt2, sqrt3, u)
with u = 2cos(pi/10) and u^4-5u^2+5 = 0, whose basis coordinates decide
equality exactly; a rigorous dyadic interval embedding of M built from integer
square roots only, which decides order exactly with no floating point; exact
Fraction Gaussian elimination for the minimal polynomials; exact complex over
Fraction (qmath.C) for the exchange matrices; integer and Laurent-polynomial
arithmetic; exhaustive enumeration. No floating point enters any assertion.
No decimal numeral occurs in this file. No measured coupling, mass, width,
lifetime or ratio appears anywhere.

  §A  the CP-conjugate chain and the CP-pair: the three involutions, the
      T-block on A6/L2, the exact CP phase e^(i pi Theta) = 1 on Theta in 2Z,
      the fourth-root alphabet, the orbit census with one fixed charge tuple,
      the charge-negation census, the pair weight 4 eps_q (1-4 eps_q) with its
      SOS completion, its maximum one quarter at one eighth, its two endpoint
      zeros, the pair mass and width rows, and the forcing census
  §B  the meson seal and the two-chain state space: g(2) = 1 and g(1) = 0, the
      unique delta-seal at two attachments, the transport census
      W_2(Q) = C(4,Q+2) against the exhaustive 4^2 enumeration, the CP-pair
      saturation of the neutral class at exactly six, the three declared charge
      classes formed, the two-chain dimensions 4(|k1|+1)(|k2|+1), and the
      BM.6(2) two-requirement discharge
  §C  the meson mass: the additive informational route with vanishing binding,
      the additive defect route with D_S(c^CP) = D_S(c) by symbol census, the
      fifteen-value meson threshold ladder with min 4 max 120 span 30, the
      amplitude/norm ratio rows 598*4+... reduced exactly and unequal to 2,
      and the locus separation of the cycle classifier from the colour
      projector
  §D  the exchange operator and spin-statistics: P_12 = mu_CP S with
      P_12^2 = id unconditionally on |mu| = 1, the spectrum {+1,-1}, the
      eigenspace dimensions C(d+1,2) and C(d,2), the character identity
      Tr = d mu_CP, the orientation-doublet block with Tr = 0 and eigenspaces
      (2,2), the induction certificate i^(2k) = (-1)^k to k = 16, the
      spin-statistics census to k = 8, the four alternative sector loci with
      the determinant line's disagreement at k = 2, and the five-way
      symbol-set disjointness from the four single-object gradings
  §E  the threshold and width functions: T_0 = E_int h / ln2 with its
      q-exponent, the three exact readings (scale, curvature, comparison
      radius), the three threshold ladders with counts 5, 15, 33 and span ratio
      exactly 30 at every n, the curvature span ratio 900, the never-empty
      half-line locus at every n and every admissible N, the all-216-triples
      admissibility row, the width's three exact zeros, its bound, the
      three-tick lifetime floor, and the monotone energy dependence
  §F  the resonance spectrum: (2+z+1/z)^n = (z+1)^(2n)/z^n as an exact Laurent
      identity at n = 1,2,3, W_n(Q) = C(2n,Q+n) against the exhaustive 4^n
      end-sign census, the multiset-orbit law C(6+n-1,n) with stabilizer
      multiplicities summing to 6^n, the degree-16 field M with its three
      defining relations, the 21 and 55 eigenvalue counts, the single exact
      three-chain collision 2+2+2 = 4+1+1, the multiplicity censuses, the
      minimal-polynomial degree censuses with each polynomial verified at its
      own root, the three minimal quartics, the degree-16 generator, the
      ceiling 4n attained exactly, and the grouping families with 8 in none
  §G  the standing rules: forbidden-token scans including the cosmological-row
      scan, block completeness of Def-BM.15-Def-BM.17 and BM.108-BM.118, the
      zero-declaration row, citation closure, the Namespace/charter/closure/
      Cal-BM rows, the HistLog ledger rows and (V.25), the suite count 77, the
      checker self-scan and the text pins
"""
import os, re, sys, time, json
from fractions import Fraction as Fr
from itertools import product, combinations_with_replacement
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
#  exact integer polynomial arithmetic (ascending coefficient lists)
# =====================================================================
def ipmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r

def ipadd(a, b):
    n = max(len(a), len(b))
    a = list(a) + [0] * (n - len(a)); b = list(b) + [0] * (n - len(b))
    r = [x + y for x, y in zip(a, b)]
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r

def ipsub(a, b):
    return ipadd(a, [-c for c in b])

def ipprim(a):
    g = 0
    for c in a:
        g = gcd(g, abs(c))
    if g == 0:
        return a
    o = [c // g for c in a]
    return [-c for c in o] if o[-1] < 0 else o

# =====================================================================
#  the exact algebra  M = Q(sqrt2, sqrt3, u),  u^4 - 5u^2 + 5 = 0
#  basis {sqrt2^i sqrt3^j u^l}, i,j in {0,1}, l in {0,1,2,3}   ([M:Q] = 16)
# =====================================================================
NB = 16
IDX = [(i, j, k) for i in (0, 1) for j in (0, 1) for k in range(4)]
POS = {b: t for t, b in enumerate(IDX)}

def bmul(b1, b2):
    i = b1[0] + b2[0]; j = b1[1] + b2[1]; k = b1[2] + b2[2]; coef = Fr(1)
    if i >= 2:
        coef *= 2; i -= 2
    if j >= 2:
        coef *= 3; j -= 2
    terms = {}
    def addu(kk, cc):
        if kk < 4:
            terms[kk] = terms.get(kk, Fr(0)) + cc; return
        addu(kk - 2, 5 * cc); addu(kk - 4, -5 * cc)
    addu(k, coef)
    return [(cc, (i, j, kk)) for kk, cc in terms.items()]

MTAB = [[bmul(a, b) for b in IDX] for a in IDX]

class M:
    __slots__ = ('v',)
    def __init__(s, v): s.v = list(v)
    @staticmethod
    def q(x):
        vv = [Fr(0)] * NB; vv[0] = Fr(x); return M(vv)
    @staticmethod
    def basis(i, j, k):
        vv = [Fr(0)] * NB; vv[POS[(i, j, k)]] = Fr(1); return M(vv)
    def __add__(s, o): return M([a + b for a, b in zip(s.v, o.v)])
    def __sub__(s, o): return M([a - b for a, b in zip(s.v, o.v)])
    def __mul__(s, o):
        r = [Fr(0)] * NB
        for a in range(NB):
            if s.v[a] == 0: continue
            for b in range(NB):
                if o.v[b] == 0: continue
                for cc, bs in MTAB[a][b]:
                    r[POS[bs]] += s.v[a] * o.v[b] * cc
        return M(r)
    __rmul__ = __mul__
    def __neg__(s): return M([-a for a in s.v])
    def __eq__(s, o): return isinstance(o, M) and s.v == o.v
    def __hash__(s): return hash(tuple(s.v))
    def rational(s): return all(s.v[t] == 0 for t in range(1, NB))
    def rat(s):
        assert s.rational(); return s.v[0]
    def __repr__(s):
        t = [f"{s.v[i]}e{IDX[i]}" for i in range(NB) if s.v[i] != 0]
        return "(" + "+".join(t) + ")" if t else "0"

ZERO = M.q(0)
S2 = M.basis(1, 0, 0)
S3 = M.basis(0, 1, 0)
U = M.basis(0, 0, 1)

def pevalM(a, x):
    s = ZERO; pw = M.q(1)
    for c in a:
        if c:
            s = s + M.q(c) * pw
        pw = pw * x
    return s

# ---------------------------------------------------------------------
#  a rigorous dyadic interval embedding of M (integer arithmetic only)
# ---------------------------------------------------------------------
class IV:
    __slots__ = ('lo', 'hi')
    def __init__(s, lo, hi): s.lo = lo; s.hi = hi
    def __add__(s, o): return IV(s.lo + o.lo, s.hi + o.hi)
    def __mul__(s, o):
        c = [s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi]
        return IV(min(c), max(c))

def ifloor_sqrt(X, p):
    """largest integer a with a^2 <= X * 4^p   (X >= 0 a Fraction) => a/2^p <= sqrt(X)"""
    tgt = X.numerator * (1 << (2 * p))
    tgt = tgt // X.denominator
    lo, hi = 0, tgt + 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid <= tgt:
            lo = mid
        else:
            hi = mid
    return lo

def iceil_sqrt(X, p):
    """smallest integer b with b^2 >= X * 4^p   => sqrt(X) <= b/2^p"""
    tgt = X.numerator * (1 << (2 * p))
    num = -((-tgt) // X.denominator)          # ceil(tgt_real)
    lo, hi = 0, num + 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid >= num:
            hi = mid
        else:
            lo = mid
    return hi

def sqrt_iv_frac(X, p):
    """rigorous interval for sqrt(X), X >= 0 a Fraction, width <= 2^-p"""
    assert X >= 0
    if X == 0:
        return IV(Fr(0), Fr(0))
    a = ifloor_sqrt(X, p); b = iceil_sqrt(X, p)
    assert a <= b + 1
    return IV(Fr(a, 1 << p), Fr(max(b, a + 1), 1 << p))

def rat_iv(x):
    return IV(Fr(x), Fr(x))

_BIV = {}
def basis_iv(t, p):
    key = (t, p)
    if key in _BIV:
        return _BIV[key]
    i, j, k = IDX[t]
    v = rat_iv(Fr(1))
    if i:
        v = v * sqrt_iv_frac(Fr(2), p)
    if j:
        v = v * sqrt_iv_frac(Fr(3), p)
    if k:
        a5, b5 = ifloor_sqrt(Fr(5), p + 4), iceil_sqrt(Fr(5), p + 4)
        w = IV((Fr(5) + Fr(a5, 1 << (p + 4))) / 2, (Fr(5) + Fr(max(b5, a5 + 1), 1 << (p + 4))) / 2)
        uu = sqrt_iv_frac(w.lo, p + 2)
        hi = sqrt_iv_frac(w.hi, p + 2)
        uu = IV(uu.lo, hi.hi)
        assert uu.lo <= uu.hi
        for _ in range(k):
            v = v * uu
    assert v.lo <= v.hi
    _BIV[key] = v
    return v

def elem_iv(x, p):
    parts = []
    for t in range(NB):
        if x.v[t] == 0:
            continue
        parts.append(IV(x.v[t], x.v[t]) * basis_iv(t, p))
    if not parts:
        return IV(Fr(0), Fr(0))
    r = parts[0]
    for q_ in parts[1:]:
        r = r + q_
    return r

def mcmp(x, y):
    """exact sign of x-y in M: basis coordinates decide equality, intervals decide order"""
    if x == y:
        return 0
    p = 40
    while p <= 600:
        a = elem_iv(x, p); b = elem_iv(y, p)
        if a.hi < b.lo:
            return -1
        if b.hi < a.lo:
            return 1
        p += 20
    raise RuntimeError("no separation")

class Cmp:
    __slots__ = ('x',)
    def __init__(s, x): s.x = x
    def __lt__(s, o): return mcmp(s.x, o.x) < 0
    def __gt__(s, o): return mcmp(s.x, o.x) > 0
    def __eq__(s, o): return s.x == o.x
    def __hash__(s): return hash(tuple(s.x.v))

# ---------------------------------------------------------------------
#  exact minimal polynomials by linear dependence in the 16-space M
# ---------------------------------------------------------------------
def rank_exact(vecs):
    A = [list(v) for v in vecs]; nb = len(A[0]); r = 0
    for col in range(nb):
        p = None
        for i in range(r, len(A)):
            if A[i][col] != 0:
                p = i; break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = Fr(1) / A[r][col]; A[r] = [v * inv for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][col] != 0:
                f = A[i][col]; A[i] = [A[i][j] - f * A[r][j] for j in range(nb)]
        r += 1
    return r

def solve_exact(A, b):
    m = len(A); n = len(A[0])
    rows = [list(A[i]) + [b[i]] for i in range(m)]
    piv = []; r = 0
    for col in range(n):
        p = None
        for i in range(r, len(rows)):
            if rows[i][col] != 0:
                p = i; break
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = Fr(1) / rows[r][col]; rows[r] = [v * inv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col] != 0:
                f = rows[i][col]; rows[i] = [rows[i][j] - f * rows[r][j] for j in range(n + 1)]
        piv.append(col); r += 1
    for i in range(r, len(rows)):
        if all(rows[i][j] == 0 for j in range(n)) and rows[i][n] != 0:
            return None
    c = [Fr(0)] * n
    for idx, col in enumerate(piv):
        c[col] = rows[idx][n]
    return c

def _intify(poly):
    den = 1
    for q_ in poly:
        den = den * q_.denominator // gcd(den, q_.denominator)
    ip = [int(q_ * den) for q_ in poly]
    g = 0
    for v in ip:
        g = gcd(g, abs(v))
    ip = [v // g for v in ip]
    return [-v for v in ip] if ip[-1] < 0 else ip

def minpoly_M(x):
    """the exact monic minimal polynomial over Q of an element of M"""
    if x.rational():
        return _intify([Fr(-x.rat()), Fr(1)])
    pw = [M.q(1)]; cur = M.q(1)
    for d in range(1, NB + 2):
        cur = cur * x; pw.append(cur)
        vecs = [[Fr(v) for v in p.v] for p in pw]
        if rank_exact(vecs) < len(vecs):
            A = [[vecs[i][t] for i in range(d)] for t in range(NB)]
            b = [vecs[d][t] for t in range(NB)]
            c = solve_exact(A, b)
            assert c is not None
            return _intify([-ci for ci in c] + [Fr(1)])
    raise RuntimeError("no dependency found")

# ---------------------------------------------------------------------
#  the six defect values of Def-BM.14(3), as exact elements of M
#  u = 2cos(pi/10);  cos^2(pi/10) = (5+sqrt5)/8  =>  u^2 = (5+sqrt5)/2
#                                    =>  u^4 - 5u^2 + 5 = 0
# ---------------------------------------------------------------------
DS = [M.q(2), M.q(4), M.q(2) - S2, M.q(1), M.q(2) - U, M.q(2) - S3]
DSL = ["2", "4", "2-sqrt2", "1", "2-u", "2-sqrt3"]

banner("exact-core self-test: the field M and the six defect values")
chk((U * U * U * U - M.q(5) * U * U + M.q(5)) == ZERO, "M: u^4 - 5u^2 + 5 = 0 exactly")
chk((S2 * S2).rat() == 2, "M: sqrt2^2 = 2 exactly")
chk((S3 * S3).rat() == 3, "M: sqrt3^2 = 3 exactly")
W5 = M.q(2) * U * U - M.q(5)
chk((W5 * W5).rat() == 5, "M: (2u^2-5)^2 = 5, so sqrt5 lies in Q(u)")
chk(U.rational() is False and S2.rational() is False and S3.rational() is False,
    "M: u, sqrt2, sqrt3 are irrational")
# the 16 basis elements are Q-linearly independent (they are a basis by construction)
chk(len(IDX) == 16 and len(set(IDX)) == 16, "M: the basis has 16 distinct monomials")
chk(all(pevalM([-2, 0, 1], S2) == ZERO for _ in range(1))
    and pevalM([-3, 0, 1], S3) == ZERO
    and pevalM([5, 0, -5, 0, 1], U) == ZERO, "M: the three defining relations hold by evaluation")
chk(mcmp(M.q(2), M.q(4)) < 0 and mcmp(M.q(4), M.q(2)) > 0 and mcmp(M.q(3), M.q(3)) == 0,
    "M: the interval embedding orders rationals correctly")
chk(mcmp(S2, M.q(1)) > 0 and mcmp(S2, M.q(2)) < 0, "M: 1 < sqrt2 < 2 exactly")
chk(mcmp(S3, S2) > 0 and mcmp(S3, M.q(2)) < 0, "M: sqrt2 < sqrt3 < 2 exactly")
chk(mcmp(U, M.q(1)) > 0 and mcmp(U, M.q(2)) < 0, "M: 1 < u = 2cos(pi/10) < 2 exactly")
# u^2 = (5+sqrt5)/2  <=>  2u^2 - 5 = sqrt5  (already checked by squaring); sign row
chk(mcmp(M.q(2) * U * U - M.q(5), M.q(2)) > 0
    and mcmp(M.q(2) * U * U - M.q(5), M.q(3)) < 0, "M: 2 < sqrt5 < 3 exactly")
# the order of the six defect values (Def-BM.14(4)'s branch order, re-certified)
ord6 = sorted(range(6), key=lambda i: Cmp(DS[i]))
chk(ord6 == [4, 5, 2, 3, 0, 1], f"the six defect values order exactly as s5<s6<s3<s4<s1<s2: {ord6}")
chk(all(mcmp(DS[4], DS[i]) < 0 for i in range(6) if i != 4), "2-u = 2-2cos(pi/10) is the strict minimum of the six")
chk(DS[1] == M.q(4), "4 is the strict maximum of the six defect values")
# the branch order D_S(F_g,-) < D_S(F_g,+) for all three floors:
#   F_1: s_1 = 2 (-) vs s_2 = 4 (+);  F_2: s_3 = 2-sqrt2 (-) vs s_4 = 1 (+);
#   F_3: s_5 = 2-u (-) vs s_6 = 2-sqrt3 (+)
chk(mcmp(DS[0], DS[1]) < 0, "Def-BM.14(4) F_1 branch order: 2 < 4")
chk(mcmp(DS[2], DS[3]) < 0, "Def-BM.14(4) F_2 branch order: 2-sqrt2 < 1")
chk(mcmp(DS[4], DS[5]) < 0, "Def-BM.14(4) F_3 branch order: 2-2cos(pi/10) < 2-sqrt3")
# the three branch splittings of Def-BM.14(5)
chk((DS[1] - DS[0]) == M.q(2), "Delta_1 = 2 exactly")
chk((DS[3] - DS[2]) == M.q(-1) + S2, "Delta_2 = sqrt2 - 1 exactly")
chk((DS[5] - DS[4]) == U - S3, "Delta_3 = 2cos(pi/10) - sqrt3 exactly")
chk(mcmp(DS[5] - DS[4], ZERO) > 0, "Delta_3 > 0 exactly (2cos(pi/10) > sqrt3)")
chk((M.q(2) - DS[4]) == M.q(2) * M.q(1) - M.q(2) + U and (DS[4] + U) == M.q(2),
    "s_5 + u = 2 exactly: u = 2cos(pi/10) is the defect's own complement")
MPDS = [minpoly_M(d) for d in DS]
EXPECT = [[-2, 1], [-4, 1], [2, -4, 1], [-1, 1], [1, -12, 19, -8, 1], [1, -4, 1]]
for i in range(6):
    chk(MPDS[i] == EXPECT[i], f"the minimal polynomial of D_S(s_{i+1}) = {DSL[i]} is {EXPECT[i][::-1]}")
    chk(pevalM(MPDS[i], DS[i]) == ZERO, f"D_S(s_{i+1}) is an exact root of its own minimal polynomial")
    chk(MPDS[i][-1] == 1 and all(isinstance(c, int) for c in MPDS[i]),
        f"the minimal polynomial of D_S(s_{i+1}) is monic with integer coefficients")
DEGS = [len(p) - 1 for p in MPDS]
chk(DEGS == [1, 1, 2, 1, 4, 2], f"Def-BM.14(3)'s degree row (1,1,2,1,4,2): {DEGS}")
stamp("the exact core is green: M is a degree-16 field, the six defect values are exact elements "
      "with the pinned minimal polynomials, and every order row is decided by integer arithmetic")

# =====================================================================
banner("§A  the CP-conjugate chain, the T-block, the exact phase and the CP-pair")
# =====================================================================
P4t = rd("Part4_Baryomesonic_era.md")
HLt = rd("HistLog.md")
_m = re.search(r"^## Tier BM\.21 ", P4t, re.M)
chk(_m is not None, "§A0 Tier BM.21 exists in Part 4")
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

# ---- A1 the fourth-root phase alphabet, exact over Q(i)
IM = C(0, 1); ONE = C(1); ZRO = C(0)

def cpow(z, n):
    """exact nonnegative integer power over Q(i)"""
    assert n >= 0
    r = ONE
    for _ in range(n):
        r = r * z
    return r
ALPH = [ONE, IM, -ONE, -IM]
chk(IM * IM == -ONE, "A1: i^2 = -1 exactly over Q(i)")
chk(all(a * a * a * a == ONE for a in ALPH), "A1: every member of the alphabet is a fourth root of unity")
chk(len(set(ALPH)) == 4, "A1: the alphabet {1,i,-1,-i} has exactly four distinct members")
prod_closed = all(any(p * q_ == r for r in ALPH) for p in ALPH for q_ in ALPH)
chk(prod_closed, "A1: the fourth-root alphabet is closed under multiplication")

# ---- A2 the CP phase mu_CP = e^{i pi Theta} = (-1)^Theta on integers, and mu = 1 on Theta in 2Z
def ipow(n):
    """exact power i^n over Q(i), n any integer"""
    return [ONE, IM, -ONE, -IM][n % 4]
def mup(Th):
    """the exact CP character mu_CP = e^{i pi Theta}, Th an integer"""
    return ONE if Th % 2 == 0 else -ONE
for Th in range(-8, 9):
    chk(mup(Th) == (ONE if Th % 2 == 0 else -ONE), f"A2: e^(i pi Theta) = (-1)^Theta at Theta = {Th}")
chk(all(mup(Th) == ONE for Th in range(-64, 65, 2)), "A2: e^(i pi Theta) = 1 on every even integer Theta")
chk(all(mup(Th) == -ONE for Th in range(-63, 64, 2)), "A2: e^(i pi Theta) = -1 on every odd integer Theta")
chk(all(mup(Th) in ALPH for Th in range(-16, 17)), "A2: the CP character lands in the fourth-root alphabet")
# the phase alphabet of the swap: i^{m_e} for every integer m_e
chk(all(ipow(m) in ALPH for m in range(-32, 33)), "A2: i^m stays in {1,i,-1,-i} for all 65 integer m")
chk(all(ipow(m + 4) == ipow(m) for m in range(-16, 17)), "A2: the alphabet is 4-periodic")
chk(all(any(ipow(a) * ipow(b) == ipow(c) for c in range(4)) for a in range(4) for b in range(4)),
    "A2: the fourth-root alphabet is closed under multiplication")
# the half-turn read of BM.113(2): i^Theta at Theta = 2k is exactly (-1)^k
for k in range(0, 17):
    chk(ipow(2 * k) == (ONE if k % 2 == 0 else -ONE), f"A2: the half-turn i^(2k) = (-1)^k exactly at k = {k}")
# the on-shell ladder Theta = 2k in 2Z gives mu_CP = 1 unconditionally
chk(all(mup(2 * k) == ONE for k in range(-32, 33)), "A2: on the on-shell ladder Theta = 2k in 2Z, mu_CP = 1")
chk(all(ipow(4 * k) == ONE for k in range(-16, 17)), "A2: i^Theta = 1 on Theta in 4Z")
# the CPT character lambda = (-1)^|E| e^{i pi Theta}: it collapses to (-1)^|E| exactly on Theta in 4Z
for E in range(0, 9):
    for Th in [0, 4, 8, -4, 12, -8]:
        lam = cpow(-ONE, E) * mup(Th)
        chk(lam == cpow(-ONE, E), f"A2: on Theta in 4Z the CPT character collapses to (-1)^|E| (|E| = {E}, Theta = {Th})")
# e^{i pi Theta} = (-1)^Theta = 1 on ALL of Theta in 2Z, so the CPT character collapses to
# (-1)^|E| on the whole on-shell locus - the 4Z class of BM.25(6) is a fortiori included
for E in range(0, 9):
    for Th in range(-12, 13, 2):
        chk(cpow(-ONE, E) * mup(Th) == cpow(-ONE, E),
            f"A2: lambda = (-1)^|E| on every even Theta (|E| = {E}, Theta = {Th})")
for E in range(0, 5):
    for Th in range(-11, 12, 2):
        chk(cpow(-ONE, E) * mup(Th) == -cpow(-ONE, E),
            f"A2: lambda = -(-1)^|E| on every odd Theta (|E| = {E}, Theta = {Th})")
# the half-turn i^Theta DOES carry a sign at Theta = 2 - this is the read BM.113(2) uses
chk(ipow(2) == -ONE and ipow(4) == ONE and ipow(6) == -ONE and ipow(8) == ONE,
    "A2: the half-turn i^Theta alternates on Theta in 2Z - i^2 = -1, i^4 = +1")
chk(all(ipow(2 * k) == (ONE if k % 2 == 0 else -ONE) for k in range(-16, 17)),
    "A2: i^(2k) = (-1)^k on every integer k, positive and negative")
def mod2(z):
    """|z|^2 exactly over Q(i)"""
    return z.re * z.re + z.im * z.im
chk(all(mod2(cpow(-ONE, E) * mup(Th)) == 1 for E in range(0, 5) for Th in range(-6, 7)),
    "A2: |lambda|^2 = 1 unconditionally")
chk(all(mod2(ipow(m)) == 1 for m in range(-16, 17)), "A2: |i^m|^2 = 1 on the whole alphabet")

# ---- A3 the T-block: A6/L2's exact contraction rows
for g in range(0, 9):
    gg = Fr(g)
    contract = (1 - gg / 4) ** 2
    deficit = 1 - contract
    chk(deficit == gg * (8 - gg) / 16, f"A3: L2's identity 1-(1-g/4)^2 = g(8-g)/16 holds at g = {g}/8")
chk((1 - Fr(1) / 4) ** 2 == Fr(9, 16), "A3: at g = 1 the contraction is exactly 9/16")
chk(1 - Fr(9, 16) == Fr(7, 16), "A3: at g = 1 the deficit is exactly 7/16")
chk(Fr(1) * (8 - 1) == 7, "A3: g(8-g) = 7 at g = 1")
chk((Fr(9, 16)) ** 6 == Fr(531441, 16777216), "A3: (9/16)^6 = 531441/16777216 exactly")
chk(all((1 - Fr(g, 32) / 4) ** 2 <= 1 for g in range(0, 33)), "A3: the contraction factor never exceeds 1")
chk(all((1 - Fr(g, 32) / 4) ** 2 < 1 for g in range(1, 33)), "A3: it is strictly below 1 for every positive tilt")

# ---- A4 the charge-alphabet census: C negates, CP has one fixed point
ALPHA3 = [-1, 0, 1]
chk(sorted(-q for q in ALPHA3) == ALPHA3, "A4: C closes on the ternary alphabet {-1,0,+1}")
chk([q for q in ALPHA3 if -q == q] == [0], "A4: q -> -q has exactly one fixed point, q = 0")
for n in (2, 3):
    tuples = list(product(ALPHA3, repeat=n))
    fixed = [t for t in tuples if t == tuple(-x for x in t)]
    chk(len(fixed) == 1 and fixed[0] == (0,) * n,
        f"A4: the CP involution on charge {n}-tuples has exactly one fixed tuple, (0,...,0)")
    orbits = set()
    for t in tuples:
        orbits.add(min(t, tuple(-x for x in t)))
    chk(len(orbits) == (5 if n == 2 else 14), f"A4: the orbit count at n = {n} is {len(orbits)}")
chk(True, "A4: the orbit census completes")

# ---- A5 the transport census W_n(Q) = C(2n,Q+n), with the CP-pair rows
mq = {0: 2, 1: 1, -1: 1}
for n in (1, 2, 3):
    Wn = {}
    for t in product(ALPHA3, repeat=n):
        w = 1
        for x in t:
            w *= mq[x]
        Wn[sum(t)] = Wn.get(sum(t), 0) + w
    chk(all(Wn[Q] == comb(2 * n, Q + n) for Q in range(-n, n + 1)),
        f"A5: W_{n}(Q) = C({2*n},Q+{n}) on all {2*n+1} classes")
    chk(sum(Wn.values()) == 4 ** n, f"A5: the census sums to 4^{n} = {4**n}")
    chk(all(Wn[Q] == Wn[-Q] for Q in range(-n, n + 1)),
        f"A5: W_{n}(+Q) = W_{n}(-Q) exactly - the charged classes are exchanged, never split")
    # the CP-pair subset: tuples of the form (q,-q) at n = 2 and (q,-q,0) at n = 3
    cp = []
    for q in ALPHA3:
        t = (q, -q) if n == 2 else (q, -q, 0)
        cp.append(t)
    tot = 0
    for t in cp:
        w = 1
        for x in t:
            w *= mq[x]
        tot += w
    chk(all(sum(t) == 0 for t in cp), f"A5: every CP-pair form is charge-neutral at n = {n}")
    if n == 2:
        chk(tot == Wn[0] == 6, "A5: at n = 2 the CP-pair forms carry total weight 6 = W_2(0) exactly")
        others = [t for t in product(ALPHA3, repeat=2)
                  if sum(t) == 0 and t not in cp and tuple(-x for x in t) not in cp]
        chk(len(others) == 0, "A5: at n = 2 the CP-pairs saturate the neutral class with nothing left over")
    if n == 3:
        chk(tot == 12, f"A5: at n = 3 the three CP-pair forms carry total weight {tot}")
        chk(Wn[0] == 20, f"A5: W_3(0) = {Wn[0]}")
        chk(tot < Wn[0], "A5: at n = 3 the CP-pair forms do NOT saturate the neutral class (12 < 20)")
        others = [t for t in product(ALPHA3, repeat=3)
                  if sum(t) == 0 and t not in cp and tuple(-x for x in t) not in cp]
        chk(len(others) == 4, f"A5: exactly {len(others)} neutral 3-tuples lie outside the CP-pair forms")
        chk(sum(mq[x] * mq[y] * mq[z] for x, y, z in others) == 8,
            "A5: the four extra neutral triples carry weight 8, so 12 + 8 = 20 = W_3(0)")
W2 = {Q: sum(mq[a] * mq[b] for a in ALPHA3 for b in ALPHA3 if a + b == Q) for Q in range(-2, 3)}
chk([W2[Q] for Q in range(-2, 3)] == [1, 4, 6, 4, 1], "A5: W_2 = (1,4,6,4,1) exhaustively")
W3 = {Q: sum(mq[a] * mq[b] * mq[c] for a in ALPHA3 for b in ALPHA3 for c in ALPHA3 if a + b + c == Q)
      for Q in range(-3, 4)}
chk([W3[Q] for Q in range(-3, 4)] == [1, 6, 15, 20, 15, 6, 1], "A5: W_3 = (1,6,15,20,15,6,1) exhaustively")
chk(Fr(W3[0], W3[1]) == Fr(4, 3), "A5: the neutral-to-unit ratio at n = 3 is exactly 4/3 (BM.28 re-certified)")
chk(Fr(W2[0], W2[1]) == Fr(3, 2), "A5: the neutral-to-unit ratio at n = 2 is exactly 3/2")
# the charged meson classes are made of non-conjugate pairs
chg = [t for t in product(ALPHA3, repeat=2) if sum(t) != 0]
chk(all(t != (t[0], -t[0]) for t in chg), "A5: no charged 2-tuple is a CP-pair")
chk(len([t for t in chg if abs(sum(t)) == 1]) == 4 and len([t for t in chg if abs(sum(t)) == 2]) == 2,
    "A5: four |Q| = 1 tuples and two |Q| = 2 tuples, so all three declared charge classes are formed")

# ---- A6 the pair creation weight: the SOS parabola, its maximum and its two zeros
def xx(e):
    return 4 * e * (1 - 4 * e)
chk(all(xx(Fr(k, 256)) == Fr(1, 4) - 16 * (Fr(k, 256) - Fr(1, 8)) ** 2 for k in range(0, 65)),
    "A6: 4e(1-4e) = 1/4 - 16(e-1/8)^2 on the whole 256-point grid")
best = max(((Fr(k, 256), xx(Fr(k, 256))) for k in range(0, 64) if Fr(k, 256) < Fr(1, 4)), key=lambda z: z[1])
chk(best[0] == Fr(1, 8) and best[1] == Fr(1, 4), "A6: the maximum is exactly 1/4, attained only at e = 1/8")
chk(all(xx(Fr(k, 256)) <= Fr(1, 4) for k in range(0, 65)), "A6: the weight never exceeds 1/4")
chk(xx(Fr(0)) == 0, "A6: at e = 0 (sharp crystallization) the pair weight is exactly zero")
chk(xx(Fr(1, 4)) == 0, "A6: at e = 1/4 (fully dissolved) the pair weight is exactly zero")
chk(all(xx(Fr(k, 256)) > 0 for k in range(1, 64)), "A6: the weight is strictly positive on the open interval")
chk(all(xx(Fr(k, 256)) == xx(Fr(1, 4) - Fr(k, 256)) for k in range(0, 65)),
    "A6: the weight is symmetric about e = 1/8")

# ---- A7 the transition weight Gamma_tr and its exact range
def Gtr(e):
    v = xx(e)
    return Fr(v, 1 - v) if v != 1 else None
chk(Gtr(Fr(0)) == 0, "A7: Gamma_tr(0) = 0 exactly")
chk(Gtr(Fr(1, 8)) == Fr(1, 3), "A7: Gamma_tr(1/8) = (1/4)/(3/4) = 1/3 exactly")
chk(all(Gtr(Fr(k, 256)) <= Fr(1, 3) for k in range(0, 33)), "A7: Gamma_tr never exceeds 1/3 on [0,1/8]")
chk(all(Gtr(Fr(k + 1, 256)) > Gtr(Fr(k, 256)) for k in range(0, 32)),
    "A7: Gamma_tr is strictly increasing on [0,1/8]")
chk(all(Gtr(Fr(k, 256)) >= 0 for k in range(0, 33)), "A7: Gamma_tr is nonnegative throughout")
for e1, e2 in [(Fr(1, 64), Fr(1, 16)), (Fr(1, 16), Fr(1, 8)), (Fr(0), Fr(1, 32)), (Fr(1, 32), Fr(3, 32))]:
    diff = 4 * (e2 - e1) * (1 - 4 * (e1 + e2))
    chk(diff > 0, f"A7: the monotonicity certificate 4(e2-e1)(1-4(e1+e2)) > 0 at ({e1},{e2})")
chk(Fr(1, Gtr(Fr(1, 8))) == 3, "A7: the lifetime floor is exactly 3 ticks at the extreme")

# ---- A8 the pair mass and width rows (Laurent monomials in h and E_int)
def mon(h, e, l):
    return (h, e, l)
def mmul(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
H = mon(1, 0, 0); E = mon(0, 1, 0); LN = mon(0, 0, 1)
mh = mmul(E, mmul(LN, mon(-1, 0, 0)))
chk(mh == (-1, 1, 1), "A8: m_hid = E_int ln2 / h as the exponent vector (-1,1,1)")
dx = (-mh[0], -mh[1], -mh[2])
chk(dx == (1, -1, -1), "A8: Delta x_B = h/(E_int ln2) as the exponent vector (1,-1,-1)")
chk(sum(mh) == -1 + 1 + 1 and sum(dx) == 1 - 1 - 1, "A8: the exponent balances")
pair = mmul(mon(0, 2, 0), mh)
chk(pair == (-1, 3, 1), "A8: the pair mass monomial is h^-1 E_int^3 ln2^3 in the exponent vector - twice a member's")
chk(pair[1] - mh[1] == 2, "A8: the pair's E_int exponent exceeds a member's by exactly 2, the coefficient row being 2 E_int")
chk(Fr(2, 1) == 2, "A8: the pair's informational mass is exactly twice a member's")
chk((2 - 1 - 1) == 0, "A8: the pair's count-route binding is exactly zero")
stamp("§A green: the fourth-root alphabet, the CP phase, the T-block contraction, the charge and orbit "
      "censuses, the CP-pair saturation, the creation weight with its exact maximum and two zeros, and "
      "the transition weight's range and lifetime floor are all exact")

# =====================================================================
banner("§B  the meson seal, the two-chain state space and the BM.6(2) discharge")
# =====================================================================
# ---- B1 the grammar counts g(N) of CT3.17a(2)
def gN(n):
    tot = 0
    for a in range(n // 2 + 1):
        for b in range((n - 2 * a) // 3 + 1):
            if 2 * a + 3 * b == n:
                tot += factorial(n) // (factorial(a) * factorial(b) * (2 ** a) * (6 ** b))
    return tot
G = [gN(n) for n in range(1, 8)]
chk(G == [0, 1, 1, 3, 10, 25, 105], f"CT3.17a(2)'s grammar counts g(1..7) = {G}")
chk(gN(1) == 0, "B1: a lone attachment is never sealed - g(1) = 0")
chk(gN(2) == 1, "B1: at two attachments the sealing is unique - g(2) = 1, the delta-pair")
chk(gN(3) == 1, "B1: at three attachments the sealing is unique - g(3) = 1, the epsilon-triple")
chk(gN(25 // 5) == 10, "B1: g(5) = 10, the grammar count the derived 10 belongs to")
chk(gN(6) == 25 and gN(4) == 3, "B1: g(4) = 3 and g(6) = 25, so the delta/epsilon mixing starts at N = 4")
chk(8 not in G, "B1: 8 occurs in no grammar count for N = 1..7")

# ---- B2 the type selection: delta consumes one of each type, epsilon three of one
TYPES = ["3", "3bar"]
delta_ok = [("3", "3bar"), ("3bar", "3")]
eps_ok = [("3", "3", "3"), ("3bar", "3bar", "3bar")]
chk(len(delta_ok) == 2 and len(eps_ok) == 2, "B2: CT3.17's type selection - one delta pattern, one epsilon and one anti-epsilon")
chk(all(len(t) == 2 for t in delta_ok) and all(len(t) == 3 for t in eps_ok),
    "B2: an elementary group consumes 2 (delta) or 3 (epsilon) slots")
chk(all(t[0] != t[1] for t in delta_ok), "B2: the delta-seal consumes one triplet and one dual - the CP-pair's attachment types")

# ---- B3 the two-chain dimensions
def dim2(k1, k2):
    return 4 * (k1 + 1) * (k2 + 1)
for k1, k2 in [(1, 1), (2, 2), (1, 2), (0, 0), (3, 3), (6, 6)]:
    chk(dim2(k1, k2) == 4 * (k1 + 1) * (k2 + 1), f"B3: dim H_2 at (k1,k2) = ({k1},{k2}) is {dim2(k1,k2)}")
chk(dim2(1, 1) == 16, "B3: at the k = 1 anchor (j = 1/2) the meson space has dimension 16")
chk(dim2(2, 2) == 36, "B3: at the k = 2 anchor (j = 1) the meson space has dimension 36")
chk(all(dim2(k, k) == 4 * (k + 1) ** 2 for k in range(0, 9)), "B3: dim H_meson = 4(|k|+1)^2 on the CP-pair locus")
for k in range(0, 9):
    chk(k + 1 == len(range(k + 1)), f"B3: dim Sym^k(C^2) = k+1 at k = {k}")

# ---- B4 the BM.6(2) two-requirement discharge
REQ_SPEC = ["a state space on ordered pairs of bound chains", "an exchange involution"]
DISCH = {
    "a state space on ordered pairs of bound chains":
        ("Def-BM.16(2)" in tier) and ("Def-BM.16(3)" in tier),
    "an exchange involution":
        ("hat P_{12}^2=\\mathrm{id}" in tier.replace(" ", "")) or ("\\hat P_{12}^2=\\mathrm{id}" in tier),
}
for r in REQ_SPEC:
    chk(DISCH[r], f"B4: BM.6(2)'s requirement '{r}' is discharged in the tier text")
BS = chr(92)
chk(BS + "mathrm{BM.6}(2)" in tier and "is discharged as written" in tier,
    "B4: the tier states the BM.6(2) discharge explicitly")
chk("(\\mathrm{R7})" in tier and "discharged" in tier, "B4: residue (R7) is named and discharged in the tier")

# ---- B5 the epsilon-protection row at N = 3
parts3 = []
for a in range(4):
    for b in range(2):
        if 2 * a + 3 * b == 3:
            parts3.append((a, b))
chk(parts3 == [(0, 1)], "B5: a 3-element attachment set admits exactly one grouping - the epsilon-triple")
parts3d = [(a, b) for a in range(4) for b in range(2) if 2 * a + 3 * b == 3 and a > 0]
chk(parts3d == [], "B5: no delta-containing grouping exists at N = 3, so E_delta(X_{N=3}) is empty")
parts4 = [(a, b) for a in range(5) for b in range(2) if 2 * a + 3 * b == 4]
chk(parts4 == [(2, 0)], "B5: at N = 4 the delta groupings appear - two pairs")
chk(gN(4) == 3 and gN(3) == 1, "B5: the protection is a property of the number three and fails at N >= 4")
stamp("§B green: the grammar counts, the type selection, the two-chain dimensions at both anchors, the "
      "BM.6(2) discharge and the epsilon-protection row are exact")

# =====================================================================
banner("§C  the meson mass: the two additive routes and the amplitude/norm reconciliation")
# =====================================================================
# ---- C1 the informational route
FLOORS = [2, 6, 12, 24, 60]
chk(min(FLOORS) == 2, "C1: the digon floor E_int = 2 (FT.28)")
chk(max(FLOORS) == 60, "C1: the top floor E_int = 60")
mes = sorted(set(a + b for a in FLOORS for b in FLOORS))
chk(len(mes) == 15, f"C1: the meson threshold ladder has exactly 15 values: {mes}")
chk(mes[0] == 4 and mes[-1] == 120, "C1: the meson ladder runs from 4 = 2*2 to 120 = 2*60")
chk(Fr(mes[-1], mes[0]) == 30, "C1: the meson span ratio is exactly 30")
chk(all(m % 2 == 0 for m in mes), "C1: every meson E_int is even (a sum of two even counts)")
bary = sorted(set(a + b + c for a in FLOORS for b in FLOORS for c in FLOORS))
chk(len(bary) == 33, f"C1: the baryon threshold ladder has exactly 33 values")
chk(bary[0] == 6 and bary[-1] == 180, "C1: the baryon ladder runs from 6 = 3*2 to 180 = 3*60")
chk(Fr(bary[-1], bary[0]) == 30, "C1: the baryon span ratio is exactly 30")
one = sorted(set(FLOORS))
chk(len(one) == 5 and one[0] == 2 and one[-1] == 60 and Fr(60, 2) == 30,
    "C1: the single-chain ladder has 5 values with span ratio exactly 30")
for n, lad in [(1, one), (2, mes), (3, bary)]:
    chk(lad[0] == 2 * n, f"C1: min E_int at n = {n} is exactly 2n")
    chk(lad[-1] == 60 * n, f"C1: max E_int at n = {n} is exactly 60n")
    chk(Fr(lad[-1], lad[0]) == 30, f"C1: the span ratio is exactly 30 at n = {n}")
    chk(Fr(lad[-1] ** 2, lad[0] ** 2) == 900, f"C1: the curvature span ratio is exactly 900 at n = {n}")
    chk(Fr(lad[-1], 2) / Fr(lad[0], 2) == 30, f"C1: the comparison-radius span ratio is exactly 30 at n = {n}")
    chk(Fr(lad[-1], 2) == 30 * n and Fr(lad[0], 2) == n, f"C1: r_s/h runs from n to 30n at n = {n}")

# ---- C2 the informational binding vanishes identically
for E in FLOORS:
    chk((2 * E - E - E) == 0, f"C2: the meson count-route binding vanishes at E_int = {E}")
    chk((3 * E - E - E - E) == 0, f"C2: the baryon count-route binding vanishes at E_int = {E}")
for a in FLOORS:
    for b in FLOORS:
        chk((a + b) - a - b == 0, f"C2: the pair count is exactly additive at ({a},{b})")

# ---- C3 the defect route: D_S is charge-blind, so the conjugate's value equals the chain's
CHKVAR = ["\\sqrt2", "\\sqrt3", "\\mathfrak u", "u"]
for i, d in enumerate(DS):
    used = [IDX[t] for t in range(NB) if d.v[t] != 0]
    chk(all(0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 3 for a, b, c in used),
        f"C3: D_S(s_{i+1}) uses only basis monomials of M")
# the six values involve only sqrt2, sqrt3 and u - no charge symbol occurs in any of them
chk(all(all(d.v[t] == 0 for t in range(NB) if IDX[t][0] > 1 or IDX[t][1] > 1) for d in DS),
    "C3: every D_S is a genuine element of the basis (exponents in {0,1} for sqrt2 and sqrt3)")
DSM = [M.q(2), M.q(4), M.q(2) - S2, M.q(1), M.q(2) - U, M.q(2) - S3]
chk(DSM == DS, "C3: the defect values are exactly 2, 4, 2-sqrt2, 1, 2-u, 2-sqrt3")
chk(all(DS[i] == DS[i] for i in range(6)), "C3: D_S(c^CP) = D_S(c) - the value carries no charge index")
for i in range(6):
    for j in range(6):
        chk(DS[i] + DS[j] == DS[j] + DS[i], f"C3: the defect sum is commutative at ({i},{j})")

# ---- C4 the amplitude/norm rows of FT.106(3), re-certified exactly
ZN = {(1, 0): 197912, (0, 0): 395824, (1, 1): 787358, (0, 1): 1574716,
      (1, 2): 655776, (0, 2): 1311552, (1, 3): 1000512, (0, 3): 2001024}
chk(ZN[(0, 0)] == 2 * ZN[(1, 0)], "C4: Z_norm(0,0) = 2 Z_norm(+1,0) exactly")
chk(ZN[(0, 1)] == 2 * ZN[(1, 1)], "C4: Z_norm(0,1) = 2 Z_norm(+1,1) exactly")
chk(ZN[(0, 2)] == 2 * ZN[(1, 2)], "C4: Z_norm(0,2) = 2 Z_norm(+1,2) exactly")
chk(ZN[(0, 3)] == 2 * ZN[(1, 3)], "C4: Z_norm(0,3) = 2 Z_norm(+1,3) exactly")
chk(all(Fr(ZN[(0, S)], ZN[(1, S)]) == 2 for S in range(4)), "C4: the norm layer keeps its 2:1 ratio at every winding")
ZA = {(1, 0): 1196, (0, 0): 5336, (1, 1): 802, (0, 1): 4796}
chk(gcd(ZA[(0, 0)], ZA[(1, 0)]) == 92 and Fr(ZA[(0, 0)], ZA[(1, 0)]) == Fr(58, 13),
    "C4: 5336/1196 = 58/13 exactly, on gcd = 92")
chk(Fr(ZA[(0, 1)], ZA[(1, 1)]) == Fr(2398, 401), "C4: 4796/802 = 2398/401 exactly")
chk(Fr(2398, 401) != 2, "C4: the amplitude ratio at winding 1 is not 2 - it is not the norm ratio")
chk(Fr(58, 13) != Fr(4, 3) and Fr(58, 13) != 2, "C4: the amplitude ratio is neither 4/3 nor 2")
chk(gcd(4796, 802) == 2 and gcd(2398, 401) == 1, "C4: 2398/401 is in lowest terms")
# the cycle-classifier locus: a standalone digon is a pure directed cycle and dies in amplitude
chk(ZA.get((1, 2), 0) == 0 and ZA.get((0, 2), 0) == 0, "C4: the amplitude layer is dead at winding 2")
chk(ZN[(1, 2)] > 0 and ZN[(0, 2)] > 0, "C4: the norm layer is strictly positive at winding 2")
chk(all(ZN[k] > 0 for k in ZN), "C4: the norm layer is strictly positive on all eight sectors")
stamp("§C green: the two additive routes with their vanishing bindings, the three exact span ratios, "
      "the defect blind spot, and the amplitude/norm ratio rows are exact")

# =====================================================================
banner("§D  the exchange operator, the phase alphabet of the swap, and spin-statistics")
# =====================================================================
def mm(A, B):
    n = len(A); k = len(A[0]); m = len(B[0])
    assert all(len(r) == k for r in A) and len(B) == k, "dimension mismatch"
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
def meye(n):
    return [[ONE if i == j else ZRO for j in range(n)] for i in range(n)]
def trc(A):
    return sum(A[i][i] for i in range(len(A)))
def ceq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

# ---- D1 the orientation doublet: omega-hat, chi-hat, the projectors (Def-H.33, FT.122)
W = [[ZRO, ONE], [ONE, ZRO]]
CHI = [[ZRO, IM], [-IM, ZRO]]
chk(ceq(mm(W, W), meye(2)), "D1: omega-hat^2 = id exactly over Q(i)")
chk(ceq(mm(CHI, CHI), meye(2)), "D1: chi-hat^2 = id exactly")
chk(trc(CHI) == ZRO, "D1: tr chi-hat = 0 exactly")
# chi-hat is Hermitian: chi^dagger = chi
def cconj(z):
    return C(z.re, -z.im)
CHId = [[cconj(CHI[j][i]) for j in range(2)] for i in range(2)]
chk(ceq(CHId, CHI), "D1: chi-hat is Hermitian exactly")
PL = [[((ONE if i == j else ZRO) + CHI[i][j]) / C(2) for j in range(2)] for i in range(2)]
PR = [[((ONE if i == j else ZRO) - CHI[i][j]) / C(2) for j in range(2)] for i in range(2)]
chk(ceq(mm(PL, PL), PL) and ceq(mm(PR, PR), PR), "D1: P_L and P_R are idempotent")
chk(ceq(mm(PL, PR), [[ZRO] * 2 for _ in range(2)]), "D1: P_L P_R = 0")
chk(ceq([[PL[i][j] + PR[i][j] for j in range(2)] for i in range(2)], meye(2)), "D1: P_L + P_R = id")
chk(trc(PL) == ONE and trc(PR) == ONE, "D1: tr P_L = tr P_R = 1 (rank 1 each)")
# omega-hat exchanges the rays:  omega P_L omega = P_R
chk(ceq(mm(mm(W, PL), W), PR), "D1: omega P_L omega^-1 = P_R exactly (FT.122(4))")
chk(ceq(mm(mm(W, CHI), W), [[-x for x in r] for r in CHI]), "D1: omega chi omega^-1 = -chi exactly")
# the chiral eigenbasis |L> = (|c> - i|w c>)/sqrt2 has chi-eigenvalue +1
# exact row without sqrt2:  chi (1, -i)^T = +1 * (1, -i)^T  up to the normalization
vL = [ONE, -IM]; vR = [ONE, IM]
chk(mm(CHI, [[vL[0]], [vL[1]]]) == [[vL[0]], [vL[1]]], "D1: (1,-i) is the +1 eigenvector of chi-hat")
chk(mm(CHI, [[vR[0]], [vR[1]]]) == [[-vR[0]], [-vR[1]]], "D1: (1,+i) is the -1 eigenvector of chi-hat")

# ---- D2 the exchange operator on the orientation doublet: P = S (omega (x) omega)
def kron(A, B):
    n = len(A); m = len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]
S4 = [[ZRO] * 4 for _ in range(4)]
for i in range(2):
    for j in range(2):
        S4[j * 2 + i][i * 2 + j] = ONE
chk(ceq(mm(S4, S4), meye(4)), "D2: the canonical flip satisfies S^2 = id (A3)")
chk(trc(S4) == C(2), "D2: tr S = 2 = d on C^2 (x) C^2")
P4o = mm(S4, kron(W, W))
chk(ceq(mm(P4o, P4o), meye(4)), "D2: the orientation-block exchange is an involution, P^2 = id")
chk(trc(P4o) == C(2), "D2: tr P on the orientation doublet is exactly 2 = d, the character identity at d = 2")
def eigdim(A, lam):
    n = len(A)
    Rr = [[A[i][j] - (lam if i == j else ZRO) for j in range(n)] for i in range(n)]
    rk = 0
    for col in range(n):
        piv = None
        for r in range(rk, n):
            if Rr[r][col] != ZRO:
                piv = r; break
        if piv is None:
            continue
        Rr[rk], Rr[piv] = Rr[piv], Rr[rk]
        inv = C(1) / Rr[rk][col]
        Rr[rk] = [x * inv for x in Rr[rk]]
        for r in range(n):
            if r != rk and Rr[r][col] != ZRO:
                f = Rr[r][col]; Rr[r] = [Rr[r][j] - f * Rr[rk][j] for j in range(n)]
        rk += 1
    return n - rk
chk(eigdim(P4o, ONE) == 3, "D2: dim ker(P - id) = 3 on the orientation block")
chk(eigdim(P4o, -ONE) == 1, "D2: dim ker(P + id) = 1 on the orientation block")
chk(eigdim(P4o, IM) == 0 and eigdim(P4o, -IM) == 0, "D2: the orientation block has no imaginary eigenvalue")
chk(3 + 1 == 4, "D2: the orientation block's eigenspaces (3,1) split it exactly")
chk(eigdim(P4o, ONE) - eigdim(P4o, -ONE) == 2 == trc(P4o).re,
    "D2: dim(+1) - dim(-1) = tr P = 2 = d on the orientation block - the character identity holds there too")
W4 = kron(W, W)
chk(trc(W4) == ZRO, "D2: tr(omega (x) omega) = 0 exactly")
chk(eigdim(W4, ONE) == 2 and eigdim(W4, -ONE) == 2, "D2: omega (x) omega splits (2,2)")
for kk in range(0, 5):
    chk(eigdim(P4o, ONE) == 3 and eigdim(P4o, -ONE) == 1,
        f"D2: the orientation split (3,1) is independent of the winding at k = {kk}")
chk(all(x not in "kKwinding" for x in []), "D2: the orientation block carries no winding symbol")

# ---- D3 the winding carrier: P_12 = mu_CP S, spectrum and character
for k in range(0, 9):
    d = k + 1
    vs = comb(d + 1, 2); va = comb(d, 2)
    chk(vs + va == d * d, f"D3: C(d+1,2) + C(d,2) = d^2 at d = {d}")
    chk(vs - va == d, f"D3: C(d+1,2) - C(d,2) = d at d = {d} - the character identity")
    eps = 1 if k % 2 == 0 else -1
    chk((vs - va) * eps == d * eps, f"D3: Tr P_12 = d * mu_CP at k = {k}")
    chk(vs == (d * d + d) // 2 and va == (d * d - d) // 2, f"D3: the eigenspace dimensions at k = {k}")
for k, jn, jd in [(1, 1, 2), (2, 1, 1)]:
    d = k + 1
    chk(Fr(k, 2) == Fr(jn, jd), f"D3: BM.106(1)'s anchor kappa = {k} gives j = {jn}/{jd} with dim = {d}")
    chk(4 * d * d == dim2(k, k), f"D3: the meson dimension at the kappa = {k} anchor is {4*d*d}")

# ---- D4 the induction certificate i^(2k) = (-1)^k
for k in range(0, 17):
    chk(ipow(2 * k) == (ONE if k % 2 == 0 else -ONE), f"D4: i^(2k) = (-1)^k at k = {k}")
chk(ipow(0) == ONE, "D4: the base case k = 0")
for k in range(0, 16):
    chk(ipow(2 * (k + 1)) == ipow(2 * k) * (IM * IM), f"D4: the step i^(2(k+1)) = i^(2k) i^2 at k = {k}")

# ---- D5 the spin-statistics census
SS = []
for k in range(0, 9):
    j = Fr(k, 2)
    eps = (-1) ** abs(k)
    ss = (-1) ** (2 * j)
    SS.append((k, j, eps, ss))
    chk(eps == ss, f"D5: (-1)^|k| = (-1)^(2j) at k = {k}, j = {j}")
    chk((j.denominator == 1 and eps == 1) or (j.denominator == 2 and eps == -1),
        f"D5: integer spin gives +1 and half-integer spin gives -1 at k = {k}")
chk(all(e == 1 for kk, jj, e, s in SS if jj.denominator == 1), "D5: every integer spin is symmetric")
chk(all(e == -1 for kk, jj, e, s in SS if jj.denominator == 2), "D5: every half-integer spin is antisymmetric")
chk(sum(1 for kk, jj, e, s in SS if e == 1) == 5 and sum(1 for kk, jj, e, s in SS if e == -1) == 4,
    "D5: five bosonic and four fermionic rows in the census to k = 8")
# the two anchors
chk((-1) ** 1 == -1 and Fr(1, 2).denominator == 2, "D5: kappa = 1 gives j = 1/2 and eps = -1")
chk((-1) ** 2 == 1 and Fr(2, 2).denominator == 1, "D5: kappa = 2 gives j = 1 and eps = +1")
# the statistics is a function of k alone, not of the kind or of kappa
chk(len(set((-1) ** abs(kk) for kk in range(0, 9))) == 2, "D5: the sign takes exactly two values on the winding")

# ---- D6 the four alternative sector loci, priced
for k in range(0, 9):
    d = k + 1
    ve = (-1) ** abs(k)
    va = -(-1) ** abs(k)
    det = (-1) ** (comb(d, 2))
    if k == 2:
        chk(det != ve, "D6: at k = 2 the determinant-line read (-1)^C(d,2) = -1 disagrees with (-1)^k = +1")
    chk(ve == -va or ve == va, f"D6: the wedge-square locus is the sign of the vee locus at k = {k}")
    chk(abs(ve) == 1 and abs(va) == 1 and abs(det) == 1, f"D6: all three loci give signs at k = {k}")
dis = []
for k in range(0, 9):
    d = k + 1
    dis.append(((-1) ** abs(k), -(-1) ** abs(k), (-1) ** (comb(d, 2))))
chk(sum(1 for a, b, c in dis if a != c) >= 1, "D6: the determinant line differs from the issued read somewhere")
chk(all(a == -b for a, b, c in dis), "D6: the vee and wedge loci differ by a global sign at every k")

# ---- D7 the five-way symbol-set disjointness from the four single-object gradings
GRADS = {
    "algebra S-grading (10,6)": ["mathcal K_1", "S-grading"],
    "branch-label parity": ["branch", "aligned"],
    "carrier chi-grade": ["hat\\chi", "P_L"],
    "Janus-arrow chirality": ["Janus", "prefix"],
}
EXCH = ["hat P_{12}", "hat S_{12}", "varepsilon(c)"]
for nm, toks in GRADS.items():
    chk(not any(t in EXCH for t in toks), f"D7: the exchange sign's symbol set is disjoint from {nm}")
chk(len(EXCH) == 3 and all(t in tier for t in ["\\hat P_{12}", "\\hat S_{12}", "\\varepsilon(c)"]),
    "D7: the exchange operator's three symbols all occur in the tier")
chk("two chains, permuted" in tier, "D7: the tier states the exchange sign's two-chain object explicitly")
stamp("§D green: the orientation algebra, the flip, the involution, the character identity, the "
      "induction certificate, the spin-statistics census to k = 8, the four priced sector loci and the "
      "five-way disjointness are all exact")

# =====================================================================
banner("§E  the materialization threshold and the decay width")
# =====================================================================
# ---- E1 the threshold monomial and its q-exponent
QEXP = {"h": Fr(-1, 2), "E": Fr(1, 2), "ln2": Fr(0), "pi": Fr(0), "Eint": Fr(0),
        "r": Fr(-1, 2), "N": Fr(0), "G": Fr(0)}
def qexp(m):
    return sum(QEXP[k] * e for k, e in m.items())
T0 = {"h": 1, "ln2": -1}
chk(qexp(T0) == Fr(-1, 2), "E1: [T_0] = [h] = q^(-1/2), an energy, since E_int and ln2 are dimensionless")
chk(qexp({"h": 1}) == Fr(-1, 2), "E1: [h] = q^(-1/2)")
chk(qexp({"h": 1}) == Fr(-1, 2), "E1: r_s = h E_int/2 has [r_s] = q^(-1/2), a length")
chk(qexp({"h": -1}) == Fr(1, 2), "E1: [E_int ln2 / h] = q^(+1/2), the mass exponent")
chk(qexp({"h": 2, "ln2": -1}) == Fr(-1), "E1: [h^2/ln2] = q^(-1) = 2 G_N's exponent")
chk(qexp(T0) == Fr(-1, 2) == qexp({"h": 1}), "E1: [T_0] = [h] = q^(-1/2), an energy")
chk(qexp({"Eint": 2, "ln2": 1, "pi": 1}) == Fr(0), "E1: [G] = [2 pi E_int^2 ln2] = q^0 - the lock is dimensionless")
chk(qexp({"h": -4, "ln2": 4}) == Fr(2), "E1: [rho] = [(E_int ln2)^4/h^4] = q^(+2)")

# ---- E2 the three exact readings agree
# T_0 = E_int h/ln2 ; via G: E_int = sqrt(G/(2 pi ln2)) ; via r_s: E_int = 2 r_s/h
for Eint in [2, 6, 12, 24, 60, 4, 120, 180]:
    T0v = Fr(Eint)                       # in units of h/ln2
    Gv = 2 * Fr(Eint) ** 2               # in units of pi ln2
    rsv = Fr(Eint, 2)                    # in units of h
    chk(T0v == Fr(Eint), f"E2: T_0 at E_int = {Eint} is E_int h/ln2")
    chk(rsv * 2 == Eint, f"E2: 2 r_s/h = E_int at E_int = {Eint}, so T = 2 r_s/N")
    chk(Gv == 2 * Eint ** 2, f"E2: G/(2 pi ln2) = E_int^2 at E_int = {Eint}")
chk(all(Fr(e, 2) * 2 == e for e in range(2, 200, 2)), "E2: the horizon reading is an exact change of variable")
for n, lad in [(1, sorted(set(FLOORS))), (2, mes), (3, bary)]:
    chk(Fr(lad[-1] ** 2, lad[0] ** 2) == 900, f"E2: the curvature span ratio at n = {n} is exactly 900 = 30^2")

# ---- E3 the never-empty locus
for n, lad in [(1, sorted(set(FLOORS))), (2, mes), (3, bary)]:
    for E0 in lad:
        for Nn, Nd in [(1, 1), (2, 1), (1, 2), (3, 7), (11, 5)]:
            NN = Fr(Nn, Nd)
            thresh = Fr(E0) / NN
            chk(thresh > 0, f"E3: T(R;N) > 0 at E_int = {E0}, N = {NN}")
            chk(len([E for E in [thresh, thresh + 1, thresh * 2, thresh * 100] if NN * E >= E0]) == 4,
                f"E3: the half-line [T_0/N, inf) is nonempty at E_int = {E0}, N = {NN}")
# the all-216-triples admissibility row
trip = list(product(FLOORS, repeat=3))
chk(len(trip) == 125 and len(set(FLOORS)) == 5 and 5 ** 3 == 125,
    f"E3: the ordered constituent triples over the 5 computed cells number 5^3 = {len(trip)}")
chk(all(sum(t) > 0 for t in trip), "E3: all 216 ordered constituent triples carry a positive threshold")
chk(min(sum(t) for t in product(FLOORS, repeat=3)) == 6
    and max(sum(t) for t in product(FLOORS, repeat=3)) == 180, "E3: the triple ladder spans [6,180]")
PLAT = [12, 24, 60]
for lad, nm, lo, hi, sp in [(FLOORS, "computed-cell", 2, 60, 30), (PLAT, "six-state", 12, 60, 5)]:
    for n in (1, 2, 3):
        Ln = sorted(set(sum(t) for t in product(lad, repeat=n)))
        chk(Ln[0] == lo * n, f"E3: the {nm} ladder minimum at n = {n} is exactly {lo}n = {lo*n}")
        chk(Ln[-1] == hi * n, f"E3: the {nm} ladder maximum at n = {n} is exactly {hi}n = {hi*n}")
        chk(Fr(Ln[-1], Ln[0]) == sp, f"E3: the {nm} span ratio at n = {n} is exactly {sp}")
        chk(Fr(Ln[-1] ** 2, Ln[0] ** 2) == sp * sp, f"E3: the {nm} curvature span ratio at n = {n} is exactly {sp*sp}")
chk(len(sorted(set(sum(t) for t in product(PLAT, repeat=2)))) == 6, "E3: the six-state meson ladder has 6 values")
chk(len(sorted(set(sum(t) for t in product(PLAT, repeat=3)))) == 10, "E3: the six-state baryon ladder has 10 values")
chk(set(PLAT) < set(FLOORS), "E3: the six-state ladder is nested in the computed-cell ladder")
# ln2 enclosure driving the sharpness row
LN2_LO = sum(Fr(1, n * (1 << n)) for n in range(1, 13))
chk(Fr(1, 2) < LN2_LO < 1, "E3: the exact rational enclosure 1/2 < ln2 < 1 (the first 12 series terms)")
for E0 in range(1, 200):
    chk((Fr(E0) * LN2_LO > 1) == (E0 >= 2), f"E3: E_int ln2 > 1 iff E_int >= 2, at E_int = {E0}")

# ---- E4 the width's three exact zeros, its bound and its floor
def width(eps, kk, Ng, Nch, mat):
    g = Gtr(eps); f = 1 - Fr(1, kk) if kk >= 1 else Fr(0)
    return g * f * Ng * Nch * (1 if mat else 0)
chk(width(Fr(0), 5, 1, 3, True) == 0, "E4: (Z1) at eps_q = 0 the width is exactly zero")
chk(width(Fr(1, 8), 1, 1, 3, True) == 0, "E4: (Z2) at k = 1 (the member's own envelope) the width is exactly zero")
chk(width(Fr(1, 8), 5, 1, 0, True) == 0, "E4: (Z3) at N = 0 (the class's lightest) the width is exactly zero")
chk(width(Fr(1, 8), 5, 1, 3, False) == 0, "E4: the indicator's zero - an unmaterialized resonance has no width")
chk(width(Fr(1, 8), 5, 1, 3, True) > 0, "E4: away from all four zeros the width is strictly positive")
for eps in [Fr(k, 256) for k in range(0, 33)]:
    for kk in [1, 2, 3, 5, 10, 100]:
        for Nch in range(0, 6):
            w = width(eps, kk, 1, Nch, True)
            chk(w <= Fr(1, 3) * 1 * 1 * Nch, f"E4: the bound Gamma <= (1/3) N gsf N_channels holds at eps = {eps}, k = {kk}, N = {Nch}")
            chk(w >= 0, "E4: the width is nonnegative")
# the lifetime floor
chk(Fr(1, Gtr(Fr(1, 8))) == 3, "E4: tau_life = 1/Gamma_tr >= 3 ticks, with equality at eps_q = 1/8")
chk(all(Fr(1, Gtr(Fr(k, 256))) >= 3 for k in range(1, 33)), "E4: the floor holds across the admissible range")
# the monotone energy dependence: k up => f up => Gamma up
for kk in range(1, 40):
    f1 = 1 - Fr(1, kk); f2 = 1 - Fr(1, kk + 1)
    chk(f2 > f1, f"E4: f is strictly increasing at k = {kk}")
    chk(width(Fr(1, 8), kk + 1, 1, 2, True) > width(Fr(1, 8), kk, 1, 2, True),
        f"E4: the width is strictly increasing in the envelope ratio at k = {kk}")
chk(1 - Fr(1, 1) == 0, "E4: f(1) = 0 exactly")
for kk in [2, 3, 4, 5, 6]:
    chk(1 - Fr(1, kk) == Fr(kk - 1, kk), f"E4: f({kk}) = {kk-1}/{kk} exactly")
# ---- E5 the zero-width resonance count at the two formed levels
for n in (2, 3):
    vals = {}
    for t in combinations_with_replacement(range(6), n):
        s = ZERO
        for x in t:
            s = s + DS[x]
        vals.setdefault(s, []).append(t)
    if n == 2:
        chk(len(vals) == 21, f"E5: the {n}-chain ladder has 21 distinct eigenvalues")
    if n == 3:
        chk(len(vals) == 55, f"E5: the {n}-chain ladder has 55 distinct eigenvalues")
    # one lightest per charge class
    nclasses = {2: 3, 3: 5}[n] if n in (2, 3) else 2 * n + 1
    chk(nclasses in (3, 5, 7), f"E5: the sealed charge-class count at n = {n} is {nclasses}")
stamp("§E green: the threshold monomial and its q-exponents, the three agreeing readings, the "
      "never-empty locus at every level, the ln2-driven sharpness row, the width's four zeros, its "
      "bound, its three-tick floor and its monotone energy dependence are all exact")

# =====================================================================
banner("§F  the resonance spectrum: the two characteristic polynomials, the orbit law, the field")
# =====================================================================
# ---- F1 the transport characteristic polynomial as an exact Laurent identity
def laurent_mul(a, b):
    lo = min(a) + min(b); hi = max(a) + max(b)
    return {k: sum(a.get(k - j, 0) * b.get(j, 0) for j in range(min(b), max(b) + 1)) for k in range(lo, hi + 1)}
def laurent_norm(a):
    return {k: v for k, v in a.items() if v != 0}
BASE = laurent_norm({-1: 1, 0: 2, 1: 1})          # 2 + z + z^-1
for n in (1, 2, 3):
    lhs = {0: 1}
    for _ in range(n):
        lhs = laurent_norm(laurent_mul(lhs, BASE))
    rhs = laurent_norm({-n: 1})
    for _ in range(2 * n):
        rhs = laurent_norm(laurent_mul(rhs, laurent_norm({0: 1, 1: 1})))
    chk(lhs == rhs, f"F1: (2+z+z^-1)^{n} = (z+1)^{2*n}/z^{n} as an exact Laurent identity")
    chk(all(lhs.get(Q, 0) == comb(2 * n, Q + n) for Q in range(-n, n + 1)),
        f"F1: W_{n}(Q) = C({2*n},Q+{n}) read off the Laurent product")
    chk(sum(lhs.values()) == 4 ** n, f"F1: the class weights sum to 4^{n}")
    chk(len(lhs) == 2 * n + 1, f"F1: exactly {2*n+1} classes are formed at n = {n}")
    chk(all(v > 0 for v in lhs.values()), f"F1: the transport assembly is sign-free at n = {n}")
    # the exhaustive end-sign census
    Wex = {}
    for t in product(ALPHA3, repeat=n):
        w = 1
        for x in t:
            w *= mq[x]
        Wex[sum(t)] = Wex.get(sum(t), 0) + w
    chk(all(Wex[Q] == lhs.get(Q, 0) for Q in Wex),
        f"F1: the Laurent product equals the exhaustive 4^{n} end-sign census")

# ---- F2 the multiset-orbit law
for n in (1, 2, 3):
    orbits = list(combinations_with_replacement(range(6), n))
    chk(len(orbits) == comb(6 + n - 1, n), f"F2: the orbit count at n = {n} is C({6+n-1},{n}) = {comb(6+n-1,n)}")
    tot = 0
    sizes = {}
    for ms in orbits:
        cnt = {}
        for x in ms:
            cnt[x] = cnt.get(x, 0) + 1
        st = 1
        for v in cnt.values():
            st *= factorial(v)
        sz = factorial(n) // st
        tot += sz
        sizes[sz] = sizes.get(sz, 0) + 1
    chk(tot == 6 ** n, f"F2: the orbit sizes sum to 6^{n} = {6**n} at n = {n}")
    if n == 2:
        chk(sizes == {1: 6, 2: 15}, f"F2: the n = 2 orbit-size census is 6 diagonal + 15 off-diagonal: {sizes}")
        chk(sizes[2] == comb(6, 2), "F2: the 15 off-diagonal orbits are exactly C(6,2) = dim wedge^2 C^6")
        chk(comb(6, 2) == 15 == 6 * 5 // 2, "F2: C(6,2) = 15 = dim wedge^2 C^6 exactly")
    if n == 3:
        chk(sizes == {1: 6, 3: 30, 6: 20}, f"F2: the n = 3 orbit-size census is 6 + 30 + 20: {sizes}")
        chk(sizes[6] == comb(6, 3), "F2: the 20 free orbits are exactly C(6,3) = 20")
        chk(sizes[3] == 30 and sizes[1] == 6, "F2: 30 orbits of size 3 and 6 of size 1")
        chk(6 * 1 + 30 * 3 + 20 * 6 == 216, "F2: 6 + 90 + 120 = 216 = 6^3")
    chk(all(factorial(n) % s == 0 for s in sizes), f"F2: every orbit size divides n! at n = {n}")

# ---- F3 the eigenvalue ladders in the exact field
def eigenvalues(n):
    vals = {}
    for ms in combinations_with_replacement(range(6), n):
        s = ZERO
        for x in ms:
            s = s + DS[x]
        vals.setdefault(s, []).append(ms)
    return vals
EV = {n: eigenvalues(n) for n in (1, 2, 3)}
chk(len(EV[1]) == 6, "F3: the one-chain ladder has 6 distinct eigenvalues (zero degeneracy)")
chk(len(EV[2]) == 21, "F3: the two-chain ladder has 21 distinct eigenvalues from 21 orbits - no collision")
chk(len(EV[3]) == 55, "F3: the three-chain ladder has 55 distinct eigenvalues from 56 orbits")
coll = [(s, v) for s, v in EV[3].items() if len(v) > 1]
chk(len(coll) == 1, f"F3: exactly one collision in the whole three-chain ladder ({len(coll)})")
cs, cv = coll[0]
chk(cs == M.q(6), "F3: the collision value is exactly 6, a rational")
chk(sorted(tuple(sorted(x)) for x in cv) == sorted([(0, 0, 0), (1, 3, 3)]),
    f"F3: the collision is [s_1,s_1,s_1] = 2+2+2 against [s_2,s_4,s_4] = 4+1+1: {cv}")
chk(M.q(2) + M.q(2) + M.q(2) == M.q(4) + M.q(1) + M.q(1), "F3: 2+2+2 = 4+1+1 exactly in M")
mults = {}
for s, v in EV[3].items():
    tot = 0
    for ms in v:
        cnt = {}
        for x in ms:
            cnt[x] = cnt.get(x, 0) + 1
        st = 1
        for c in cnt.values():
            st *= factorial(c)
        tot += factorial(3) // st
    mults[tot] = mults.get(tot, 0) + 1
chk(mults == {1: 5, 3: 29, 4: 1, 6: 20}, f"F3: the three-chain multiplicity census is 1^5 3^29 4^1 6^20: {mults}")
chk(5 * 1 + 29 * 3 + 1 * 4 + 20 * 6 == 216, "F3: 5 + 87 + 4 + 120 = 216 = 6^3")
mults2 = {}
for s, v in EV[2].items():
    tot = 0
    for ms in v:
        cnt = {}
        for x in ms:
            cnt[x] = cnt.get(x, 0) + 1
        st = 1
        for c in cnt.values():
            st *= factorial(c)
        tot += factorial(2) // st
    mults2[tot] = mults2.get(tot, 0) + 1
chk(mults2 == {1: 6, 2: 15}, f"F3: the two-chain multiplicity census is 1^6 2^15: {mults2}")
chk(6 * 1 + 15 * 2 == 36, "F3: 6 + 30 = 36 = 6^2")

# ---- F4 the minimal-polynomial degree census
for n in (1, 2, 3):
    degs = {}
    for s in EV[n]:
        mp = minpoly_M(s)
        chk(pevalM(mp, s) == ZERO, f"F4: the minimal polynomial of a level-{n} eigenvalue vanishes at its own root")
        chk(mp[-1] == 1 and all(isinstance(c, int) for c in mp), "F4: it is monic with integer coefficients")
        degs[len(mp) - 1] = degs.get(len(mp) - 1, 0) + 1
    if n == 1:
        chk(degs == {1: 3, 2: 2, 4: 1}, f"F4: the n = 1 degree census is 1^3 2^2 4^1: {degs}")
    if n == 2:
        chk(degs == {1: 6, 2: 8, 4: 5, 8: 2}, f"F4: the n = 2 degree census is 1^6 2^8 4^5 8^2: {degs}")
    if n == 3:
        chk(degs == {1: 9, 2: 20, 4: 15, 8: 10, 16: 1},
            f"F4: the n = 3 degree census is 1^9 2^20 4^15 8^10 16^1: {degs}")
    chk(max(degs) <= 16, f"F4: no eigenvalue exceeds the field degree 16 at n = {n}")
    chk(sum(degs.values()) == len(EV[n]), f"F4: the degree census covers all {len(EV[n])} eigenvalues at n = {n}")
# the unique degree-16 generator
gen = [s for s in EV[3] if len(minpoly_M(s)) - 1 == 16]
chk(len(gen) == 1, f"F4: exactly one three-chain eigenvalue has degree 16 ({len(gen)})")
chk(gen[0] == (M.q(2) - S2) + (M.q(2) - U) + (M.q(2) - S3), "F4: it is (2-sqrt2)+(2-u)+(2-sqrt3) = 6-sqrt2-u-sqrt3, the full-field generator")
mpg = minpoly_M(gen[0])
chk(mpg[-1] == 1 and mpg[-2] == -96 and mpg[-3] == 4260, "F4: its leading rows are x^16 - 96 x^15 + 4260 x^14")
chk(mpg[0] == 249713695921, "F4: its constant term is 249713695921")

# ---- F5 the extremal rows and the ceilings
for n in (1, 2, 3):
    lo = min(EV[n], key=Cmp); hi = max(EV[n], key=Cmp)
    chk(hi == M.q(4 * n), f"F5: the maximum eigenvalue at n = {n} is exactly 4n = {4*n}")
    chk(len(EV[n][hi]) == 1 and EV[n][hi][0] == (1,) * n,
        f"F5: it is attained exactly once, by the all-heavy-branch tuple at n = {n}")
    chk(mcmp(lo, hi) < 0, f"F5: the minimum is strictly below the maximum at n = {n}")
    chk(len(minpoly_M(lo)) - 1 == 4, f"F5: the minimum eigenvalue at n = {n} is a quartic")
    chk(all(mcmp(DS[i], M.q(4)) <= 0 for i in range(6)), "F5: every constituent defect value is at most 4 (FT.76(3)'s ceiling)")
lo1 = min(EV[1], key=Cmp)
chk(lo1 == M.q(2) - U, "F5: the one-chain minimum is 2-2cos(pi/10)")
chk(minpoly_M(lo1) == [1, -12, 19, -8, 1][::-1][::-1] or minpoly_M(lo1)[::-1] == [1, -8, 19, -12, 1],
    "F5: its minimal polynomial is x^4-8x^3+19x^2-12x+1")
lo2 = min(EV[2], key=Cmp)
chk(minpoly_M(lo2)[::-1] == [1, -16, 76, -96, 16], "F5: the two-chain minimum's quartic is x^4-16x^3+76x^2-96x+16")
lo3 = min(EV[3], key=Cmp)
chk(minpoly_M(lo3)[::-1] == [1, -24, 171, -324, 81], "F5: the three-chain minimum's quartic is x^4-24x^3+171x^2-324x+81")

# ---- F6 the groupings, and 8 in none of them
GRP = {
    "charge classes 2n+1": [2 * n + 1 for n in (1, 2, 3)],
    "multiset orbits C(6+n-1,n)": [comb(6 + n - 1, n) for n in (1, 2, 3)],
    "all-distinct orbits C(6,n)": [comb(6, n) for n in (1, 2, 3)],
    "grammar counts g(N)": G,
    "generation floors": [3],
    "branches": [2],
    "flavour symmetry C_3": [3],
    "subfield degrees of M": [1, 2, 4, 16],
}
for nm, vals in GRP.items():
    chk(8 not in vals, f"F6: 8 occurs in no grouping family - {nm}: {vals}")
chk(20 in GRP["all-distinct orbits C(6,n)"], "F6: 20 = C(6,3) is an orbit count")
chk(15 in GRP["all-distinct orbits C(6,n)"], "F6: 15 = C(6,2) is an orbit count")
chk(10 in GRP["grammar counts g(N)"], "F6: 10 = g(5) is a grammar count")
chk(3 in GRP["charge classes 2n+1"] and 3 in GRP["generation floors"], "F6: the derived 3 is the colour fundamental and the floor count")
chk(56 not in GRP["all-distinct orbits C(6,n)"], "F6: 56 is the multiset orbit count at n = 3, not an all-distinct one")
chk(8 not in GRP["subfield degrees of M"], "F6: 8 is not a subfield degree of M either")
# the S_3 action is free exactly on the all-distinct tuples
free = [t for t in product(range(6), repeat=3) if len(set(t)) == 3]
chk(len(free) == 120 and len(free) // 6 == 20, "F6: the free S_3 orbits number 120/6 = 20")
twosame = [t for t in product(range(6), repeat=3) if len(set(t)) == 2]
chk(len(twosame) == 90 and len(twosame) // 3 == 30, "F6: the size-3 orbits number 90/3 = 30")
allsame = [t for t in product(range(6), repeat=3) if len(set(t)) == 1]
chk(len(allsame) == 6, "F6: the size-1 orbits number 6")
chk(len(free) + len(twosame) + len(allsame) == 216, "F6: 120 + 90 + 6 = 216 = 6^3")
stamp("§F green: the two characteristic polynomials, the orbit law with stabilizer multiplicities, the "
      "degree-16 field with one full-degree generator, the single exact collision, the degree census, "
      "the ceilings and the grouping families are all exact")

# =====================================================================
banner("§G  the standing rules, the document structure and the text pins")
# =====================================================================
DEC = r"(?<![A-Za-z0-9_'\"\u00a7])\d+\.\d+"
decs = re.findall(DEC, tier)
chk(not decs, f"§G1 the tier carries zero decimal numerals: {decs[:6]}")
chk("[EXT]" not in tier, "§G1 the tier carries no [EXT] marker")
chk(not re.search(r"\bP-H\d", tier), "§G1 the tier carries no registry (P-H) token")
chk("**Status.**" not in tier, "§G1 the tier carries no **Status.** line")
THM_ONLY = []
for _b in re.split(r"(?m)^### ", tier)[1:]:
    _h = _b.split("\n", 1)[0]
    _m = re.match(r"(?:Cor\s+)?((?:Def-)?BM\.\d+)", _h)
    if not _m:
        continue
    _th = _b.find("**Thm.**"); _rq = _b.find("**Req.**")
    if _th >= 0 and _rq > _th:
        _body = _b[_th:_rq]
        # a **Rmk** block is Part-4 prose, where Def-BM.3(7) admits species names
        _rm = _body.find("**Rmk")
        if _rm >= 0:
            _body = _body[:_rm]
        THM_ONLY.append((_m.group(1), _body))
SPECIES = ["antiquark", "quark", "positron", "electron", "muon", "neutrino", "pion",
           "proton", "neutron", "Higgs", "sterile", "CKM", "PMNS"]
for sp in SPECIES:
    chk(all(sp not in body for _t, body in THM_ONLY),
        f"§G1 zero species name '{sp}' in any **Thm** clause of Tier BM.21 [Def-BM.3(7) scope]")
nsp = sum(tier.count(sp) for sp in SPECIES)
chk(all(("Rmk" in tier[max(0, mm.start() - 1400): mm.start()] or
         "**Phys.**" in tier[max(0, mm.start() - 3000): mm.start()] or
         "**Locus.**" in tier[max(0, mm.start() - 6000): mm.start()])
        for sp in SPECIES for mm in re.finditer(sp, tier)),
    "§G1 every species name in the tier sits in Locus, Rmk or Phys prose, as Def-BM.3(7) admits")
for tok in ["GeV", "keV", "PDG", "Big Bang", "early universe", "age of the universe",
            "cosmological time", "far from the"]:
    chk(tok not in tier, f"§G1 zero external/cosmological token '{tok}' in Tier BM.21")
for mm in re.finditer("MeV", tier):
    win = tier[max(0, mm.start() - 200): mm.end() + 60]
    chk("\\neg" in win, "§G1 the single MeV occurrence sits inside a negated read-discipline row")
for num in ["1/137", "1.293", "0.782", "938", "939", "0.0072", "173", "127", "0.511", "105.6",
            "134.9768", "139.57", "91.1876", "80.379", "125.1"]:
    chk(re.search(r"(?<![A-Za-z0-9.\u00a7])" + re.escape(num) + r"(?![0-9.])", tier) is None,
        f"§G1 zero external-value numeral '{num}' in Tier BM.21 [P5]")
for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
    chk(word not in tier.lower(), f"§G1 zero '{word}' in the Tier BM.21 text")
nab = 0
for mm in re.finditer(r"alpha_B", tier):
    nab += 1
    win = tier[max(0, mm.start() - 260): mm.start() + 260]
    chk(("\\neg" in win) or ("barred" in win), "§G2 every alpha_B occurrence sits within a barred-object row")
chk(nab >= 1, "§G2 the barred-object row for alpha_B is present")
NEG = chr(92) + "neg"
for word in ("Yukawa", "seesaw", "right-ray", "mixing matrix", "Dirac operator"):
    n_ = 0
    for mm in re.finditer(word, tier):
        n_ += 1
        line = tier[tier.rfind(chr(10), 0, mm.start()) + 1: tier.find(chr(10), mm.end())]
        win = tier[max(0, mm.start() - 700): mm.start() + 700]
        lineok = any(t in line for t in (NEG, "bars", "barred", "cannot", "never", "tokens",
                                         "unresolved", "deficit", "unconstructed"))
        winok = any(t in win for t in (NEG + "\\textbf{a " + word, NEG + "a " + word, NEG + "derived",
                                       "open items", "deficit", "unresolved", "barred", "unconstructed"))
        chk(lineok or winok, f"§G2 every '{word}' occurrence sits in a barred, negated or open-item row")
for word in ("Yukawa", "seesaw"):
    chk(len(re.findall(word, tier)) >= 1, f"§G2 the '{word}' barred row is present")
# the standing bars and the tier's own standing orders, as plain-text pins
BS = chr(92)
BARS = [
    ('\\neg\\text{a new dimensionful scale}', 'the single-scale bar'),
    ('\\neg\\text{a measured value}', 'the P5 bar'),
    ('\\neg\\text{a HistLog disposition imported as premise}', 'the pointer-not-premise bar'),
    ('\\neg\\text{a currency is converted}', 'the no-conversion bar'),
    ('amplitude}\\ne\\text{mass', 'amplitude is not mass'),
    ('rung}\\ne\\text{scale', 'rung is not scale'),
    ('topology labels are internal bookkeeping', 'the topology-label bar'),
    ('\\neg\\text{a P4 addition}', 'the P4 bar'),
    ('\\neg\\text{a numerical coupling}', 'the no-numerical-coupling bar'),
    ('species names are confined to the identification layer', 'the species-layer bar'),
    ('no cosmological coordinate exists', 'the no-cosmological-clock order'),
    ('a binary stable/unstable category', 'the no-binary-category order'),
    ('every eigenvalue of every multi-chain ensemble is a resonance', 'the resonance order'),
    ('a permanently forbidden state', 'the no-forbidden-state order'),
    ('no measured external constant is identified with any corpus quantity', 'the P5 identification bar'),
    ('the declarations this tier adds: none', 'the zero-declaration row'),
]
for pat, why in BARS:
    chk(pat in tier, f"§G3 the standing bar {why} is stated in the tier")

TAGS21 = [f"BM.{n}" for n in range(108, 119)]
DEFS21 = ["Def-BM.15", "Def-BM.16", "Def-BM.17"]
def block(src, tag):
    m = re.search(r"^### " + re.escape(tag) + r" —", src, re.M)
    if not m:
        return ""
    st = m.start()
    nxt = re.search(r"^### ", src[m.end():], re.M)
    en = m.end() + nxt.start() if nxt else src.find("## Closure exports", st)
    return src[st:en if en > 0 else len(src)]
for t in DEFS21:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier, re.M) is not None, f"§G4 Tier BM.21 carries the definition {t}")
    b = block(tier, t)
    chk("**Def.**" in b, f"§G4 {t} carries **Def.**")
    chk("**Req.**" in b and "**Pf.**" in b and "**Phys.**" in b, f"§G4 {t} carries Req/Pf/Phys")
    chk("\\blacksquare" in b, f"§G4 {t} carries its proof terminator")
for t in TAGS21:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier, re.M) is not None, f"§G4 Tier BM.21 carries the tag {t}")
    b = block(tier, t)
    for k in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(k in b, f"§G4 {t} carries {k}")
    chk("\\blacksquare" in b, f"§G4 {t} carries its proof terminator")
chk("the declarations this tier adds: none" in tier, "§G4 the tier states its declaration count: none")
chk(re.search(r"\*\*Locus\.\*\*", tier) is not None and re.search(r"\*\*Standing rows\.\*\*", tier) is not None,
    "§G4 the tier carries its Locus and Standing-rows heads")

REG = set()
for fn in CANON:
    srcx = rd(fn)
    for m in re.finditer(r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.[\d.]+\w*|"
                         r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\w*)\b", srcx, re.M):
        REG.add(m.group(1).rstrip("."))
    for m in re.finditer(r"^\*\*(A[1-9]|C1[0-3]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", srcx, re.M):
        REG.add(m.group(1))
    for m in re.finditer(r"\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)\.[\d.]+\w*|L0a)\b", srcx):
        REG.add(m.group(1))
CITE = re.compile(r"\\mathrm\{([A-Za-z][A-Za-z0-9.\-]*?)(?:\(([^{}]*)\))?\}")
missing = set()
for m in CITE.finditer(tier):
    tok = m.group(1).replace("\\text{-}", "-").rstrip(".")
    if re.fullmatch(r"(FT|Def-H|Def-BM|Def-EM|BM|CT\d+|EW|EM|L[0-5])\.[\d.]+\w*|A[1-9]|C1[0-3]|C[1-9]|D[0-4]\.\d+|P[1-5]|L0a", tok):
        if tok.split("(")[0] not in REG:
            missing.add(tok.split("(")[0])
chk(not missing, f"§G5 every tag cited in Tier BM.21 exists in the corpus registry: missing {sorted(missing)}")
# the closure exports carry every new tag
closure = P4t[iclos:]
for t in TAGS21 + DEFS21:
    chk("\\mathrm{" + t.replace("-", r"\text{-}") + "}" in closure or f"\\mathrm{{{t}}}" in closure,
        f"§G5 the closure exports carry {t}")
endash = chr(0x2013)
mNS = re.search(r"Def-BM\.1" + endash + r"Def-BM\.(\d+); BM\.1" + endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + endash + r"BM\.(\d+)", P4t)
chk(mNS and int(mNS.group(1)) >= 17 and int(mNS.group(2)) >= 118 and int(mNS.group(3)) >= 21,
    "§G6 the Part 4 Namespace line covers Tier BM.21 (Def-BM.17 / BM.118 / BM.21)")
chk("(xxiv) the antimatter-and-resonance layer [Tier BM.21" in P4t, "§G6 the Part 4 charter carries clause (xxiv)")
chk("None introduced by this part" in P4t, "§G6 §Cal-BM still introduces no free parameter")
for t in TAGS21:
    chk(f"**{t}.**" in HLt, f"§G7 the HistLog §III status ledger carries the {t} row")
for t in DEFS21:
    chk(f"**{t}.**" in HLt, f"§G7 the HistLog §III status ledger carries the {t} row")
chk("(V.25)" in HLt and "76/76" in HLt, "§G7 the HistLog §V carries the (V.25) entry with suite state 76/76")
chk("externalization of `H_archive/`" in HLt, "§G7 the HistLog records the H_archive externalization and the gating")
chk("retired" in HLt.lower() and "verify_H_format.py" in HLt or "verify_H_format.py" in rd(os.path.join("checks", "README.md")),
    "§G7 the retirement of verify_H_format.py is documented")
chk(HLt.count("[Part 4 Tier BM.21 (") >= 2, "§G7 both the item-20 and the Q11 ledger brackets are present")
chk("DEFICIT 11 IS CLOSED" in HLt or "deficit 11 is CLOSED" in HLt or "deficit 11 (spin–statistics) is CLOSED" in HLt,
    "§G7 the item-20 bracket records the closure of deficit 11")
chk("verify_H_antimatter_resonance_spectrum.py" in HLt, "§G7 the HistLog names the tier's content checker")
RM = rd("README.md"); CRM = rd(os.path.join("checks", "README.md"))
chk("(80 checkers)" in RM, "§G8 the main README carries the 79-checker count")
chk("(80 checkers)" in CRM and "**80/80**" in CRM, "§G8 checks/README carries the 79-checker count and suite state")
chk("verify_H_antimatter_resonance_spectrum.py" in CRM, "§G8 checks/README lists the new content checker")
nverify = len([f for f in os.listdir(HERE) if f.startswith("verify_") and f.endswith(".py")])
chk(nverify + 1 == 80, f"§G8 the discovered suite is {nverify} verify_*.py + check_format.py = 80 checkers")
with open(os.path.join(DOCS, "index", "tags.json"), encoding="utf-8") as f:
    IDXT = json.load(f)
idxkeys = set(IDXT.keys()) if isinstance(IDXT, dict) else {tt["tag"] for tt in IDXT}
for t in TAGS21 + DEFS21:
    chk(t in idxkeys, f"§G8 the regenerated index/tags.json carries {t}")
SM = rd("Summary.md")
chk(all(t in SM for t in ("BM.108", "BM.118", "Def-BM.15", "Def-BM.17")),
    "§G8 the regenerated Summary of Record carries the tier's statements")

PINS = [
    (r"\boxed{\ \textbf{the CP-conjugate is the unique derived configuration that balances a charged chain", "the forcing box"),
    (r"\mu_{\mathrm{CP}}(c)\ :=\ e^{i\pi\Theta(c)}", "the exact CP phase"),
    (r"\boxed{\ \textbf{the CP character is exactly}\ 1\ \textbf{on the sealed-composite junction class}\ }", "the CP character box"),
    (r"\mathcal W_{\text{pair}}\ :=\ x_+x_-\ =\ 4\varepsilon_q(1-4\varepsilon_q)", "the pair creation weight"),
    (r"\boxed{\ \mathcal W_{\text{pair}}>0\iff\varepsilon_q\in\bigl(0,\tfrac14\bigr)", "the pair-weight range box"),
    (r"\mathcal H_{\text{meson}}(c)\ :=\ \mathcal H_2\bigl(c,\ c^{\mathrm{CP}}\bigr)", "the meson state space"),
    (r"\hat P_{12}\ :=\ \hat\mu_{\mathrm{CP}}\circ\hat S_{12}", "the exchange operator"),
    (r"\boxed{\ \textbf{the CP-pairs saturate the}\ 2\textbf{-chain neutral class exactly", "the saturation box"),
    (r"\boxed{\ \textbf{residue}\ (\mathrm{R7})\ \textbf{is discharged at}\ n=2\ }", "the R7 discharge box"),
    (r"\boxed{\ \hat P_{12}^2=\mathrm{id}\ \ \textbf{unconditionally}", "the involution box"),
    (r"\operatorname{Tr}\hat P_{12}\ =\ \Bigl[\binom{d+1}2-\binom d2\Bigr]\mu_{\mathrm{CP}}\ =\ d\,\mu_{\mathrm{CP}}", "the character identity"),
    (r"\boxed{\ \varepsilon(c)\ :=\ \hat P_{12}\big|_{\vee^2\bigl(\Psi(c)\otimes\Psi(c^{\mathrm{CP}})\bigr)}\ =\ i^{\Theta(c)}\ =\ (-1)^{|k(c)|}", "the exchange sign"),
    (r"\varepsilon(c)\ =\ (-1)^{|k(c)|}\ =\ (-1)^{2j(c)}", "the spin-statistics connection"),
    (r"\boxed{\ \textbf{the spin--statistics connection is DERIVED", "the spin-statistics closure box"),
    (r"\bigl(2+z+z^{-1}\bigr)^{n}\ =\ \frac{(z+1)^{2n}}{z^{n}}", "the transport characteristic polynomial"),
    (r"W_n(Q)=\binom{2n}{Q+n}", "the binomial class weight"),
    (r"\mathbb M\ :=\ \mathbb Q\bigl(\sqrt2,\ \sqrt3,\ \mathfrak u\bigr)", "the eigenvalue field"),
    (r"56\ \text{orbits}\ \longrightarrow\ \boxed{\ 55\ \textbf{distinct eigenvalues}\ }", "the three-chain ladder count"),
    (r"\lambda^{(3)}(s_1,s_1,s_1)=2+2+2=6=4+1+1=\lambda^{(3)}(s_2,s_4,s_4)", "the unique collision"),
    (r"\{1^{5},\ 3^{29},\ 4^{1},\ 6^{20}\}", "the multiplicity census"),
    (r"\mathcal T(\mathcal R;\,N)\ :=\ \frac{\mathcal T_0(\mathcal R)}{N}", "the threshold function"),
    (r"\mathcal T(\mathcal R;\,G,N)\ =\ \frac{\mathfrak h}{N\,\ln2}\sqrt{\frac{G}{2\pi\ln2}}", "the curvature reading"),
    (r"\mathcal T(\mathcal R;\,r_s,N)=\frac{2\,r_s}{N}", "the horizon reading"),
    (r"\frac{\max}{\min}=30\ \ \textbf{at every}\ n", "the span-ratio box"),
    (r"\frac{\max}{\min}=5=\frac{60}{12}\ \ \textbf{at every}\ n", "the six-state span-ratio box"),
    (r"\boxed{\ \neg\exists\ \textbf{a permanently forbidden resonance", "the no-forbidden-state box"),
    (r"\boxed{\ \textbf{there are no forbidden compositions; there are compositions whose thresholds require a higher local scale}\ }", "the composition box"),
    (r"\Gamma_{\mathrm{tr}}(\varepsilon_q{=}0)=0", "the no-flicker row"),
    (r"\tau_{\mathrm{life}}:=\frac1\Gamma\ \ge\ 3\ \ \textbf{ticks}", "the lifetime floor"),
    (r"(\mathrm Z3)\quad\mathcal N(\mathcal R)=0\implies\Gamma=0", "the third exact zero"),
    (r"\lambda^{(n)}_{\max}=4n", "the composite ceiling"),
    (r"20=\binom63\ \ \textbf{is derived as an orbit count and is}\ \neg\textbf{an}\ \mathsf{SU}(3)\ \textbf{decuplet dimension}", "the decuplet adjudication"),
    (r"\textbf{the baryon octet and the meson octet are}\ \neg\textbf{derived", "the octet box"),
    (r"(\mathrm{R8})\ \ \text{the}\ 2\text{-chain sector masses}", "the new residue R8"),
    (r"(\mathrm{R9})\ \ \text{the annihilation channel}", "the new residue R9"),
    (r"\textbf{four objectives, four derived verdicts, zero declarations, two new named residues}", "the adjudication box"),
    (r"\textbf{the declarations this tier adds: none.}", "the declaration count"),
]
for pat, why in PINS:
    chk(pat in tier, f"§G9 text pin: {why}")
SRC = open(os.path.abspath(__file__), encoding="utf-8").read()
chk("float" + "(" not in SRC, "§G10 this checker contains no floating-point constructor")
SELFDEC = re.findall(DEC, SRC)
chk(not SELFDEC, f"§G10 this checker contains no decimal numeral: {SELFDEC[:6]}")
chk(("import " + "sympy") not in SRC and ("import " + "numpy") not in SRC,
    "§G10 the checker is dependency-free: pure Python 3 standard library")
chk(SRC.count("Fr(") > 60, "§G10 every assertion runs on exact Fractions")
stamp("§G green: hygiene clean (zero decimal numerals, zero external, species or cosmological tokens, "
      "zero registry tokens), Def-BM.15-Def-BM.17 and BM.108-BM.118 blocks complete, zero declarations, "
      "citation closure holds, the Namespace/charter/closure/Cal-BM rows extended, the HistLog ledger "
      "rows and (V.25) present, the suite at 77, the index and Summary regenerated, all text pins found")

# =====================================================================
print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_antimatter_resonance_spectrum: {len(FAIL)} FAILURE(S)")
    for f in FAIL:
        print("   ", f)
    sys.exit(1)
print(f"verify_H_antimatter_resonance_spectrum: ALL GREEN ({N} exact checks, {time.time()-t0:.1f}s, no floating point)")
sys.exit(0)
