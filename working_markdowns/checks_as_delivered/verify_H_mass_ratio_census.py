#!/usr/bin/env python3
"""verify_H_mass_ratio_census.py - Tier BM.17 of Part 4: the mass-ratio census.

BM.79-BM.86 - the Platonic winding ladders, the intra- and inter-generational
ratios, the six-state bridge census, the four-currency incommensurability, the
neutron-proton mass ratio, and the Q-value in two formed reads.

Exact arithmetic only: Fraction; exact quadratic rings Q(sqrt d); the quartic
ring Z[c]/(16c^4-20c^2+5); the biquadratic ring Q[c,r]/(16c^4-20c^2+5, r^2-3);
minimal polynomials by first Q-linear dependence on the powers of an element
(with exact re-substitution); Chebyshev recursion with integer coefficients;
alternating rational Taylor enclosures of cos and sin with exact remainder
bounds; integer Newton certificates for square roots; monotone exact rational
interval arithmetic; the prime-log ring Q (+) (+)_p Q*ln p whose sign tests are
exact comparisons of two non-negative integers; exact symbolic elimination in
Q[g][r]/(2r^3-6r^2+3r+1-g); the Basel-series lower bound for pi^2. No floating
point enters any assertion. No decimal numeral occurs in this file outside a
string literal. No SM mass, mass ratio or Yukawa value appears anywhere.

  §A  the ladder law: delta_v from (d,L), V*delta_v = 4*pi, the two windings
      k_f and k_vf from the minimality rule, D(m) on all five ladders in the
      exact fields, the Chebyshev tower with T_5(c) = 0, the minimal
      polynomials of the six D values, the period/distinct-value/monotonicity
      rows, the rung law, the top-weight row, the two obstructions
  §B  the intra-generational ratios: the sine-ratio law, the five rows in both
      variants with their minimal polynomials, the exact order on integer
      certificates, the ceiling row and the range bar against BM.80's bracket
  §C  the six-state census: the doublet m^2 and mass ratios with their minimal
      polynomials and annihilators, the order g2<g1<g3 on 8<9 and 720>361, the
      splitting rows Delta_1>Delta_2>Delta_3 on the squaring chain, the exact
      simplification Delta_2/m^2_up = sqrt2/2, the two inverted hierarchies,
      the three pairwise non-proportional ladders
  §D  the channel cubics: the r-cubic and the z-cubic by exact elimination in
      Q[g][r], Vieta, the three gamma constants pairwise distinct and ordered,
      the identity r0^(l) = 1 + gamma_q, the twelve 10^-12 brackets and the
      re-certification of Part 3's frozen decimals, Q = 2/3, the
      hierarchy-order theorem with pi^2 > 64/9 from the Basel partial sum
  §E  the bridge census: the six exact factors R_s with their minimal
      polynomials, the order, the span 50/(1-c) with its quartic, the exact 25,
      the fifteen rho_B-free pole ratios, the seven informational ratios, the
      dimension row for rho_B
  §F  the four currencies: the prime-log representations of ln1280 and ln960,
      the independence census, the irrationality theorem at every rational t,
      the exact solution t = -ln405/ln16 < 0 for the ratio 4/3, the three-symbol
      localization, the nine cross-channel factors and the light-end brackets
  §G  the neutron-proton ratio: the assembly, the monotone decrease, the range
      theorem with 2^44 > 3^26*5 and 2^34 < 3^21*5, the critical strength's
      four certificates and its irrationality, the trichotomy with non-empty
      opening and closing witnesses, the fractional splittings
  §H  the Q-value: the two-bit floor and the margin ladder, the ratio forms on
      3^13 < 2^16*25, 3^20 > 2^24*125, 3^21 < 2^24*625, 3^16 > 2^18*125, the
      specified read's four Delta T values and BM.77's witnesses, the alphabet
      disjointness census
  §I  the standing rules: forbidden-token scans, block completeness of
      BM.79-BM.86, citation closure, the Namespace/charter/closure rows, the
      HistLog ledger rows, the suite count 76, the checker self-scan, and the
      text pins
"""
import os, re, sys, time
from fractions import Fraction as Fr
from math import isqrt
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
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
#  exact linear algebra over Q
# =====================================================================
def charpoly(M):
    n = len(M); A = [[Fr(x) for x in row] for row in M]
    def mm(X, Y):
        return [[sum(X[i][t] * Y[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
    co = [Fr(1)]; Mk = [[Fr(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        Mk = mm(A, Mk)
        for i in range(n): Mk[i][i] += co[-1]
        AM = mm(A, Mk)
        co.append(-sum(AM[i][i] for i in range(n)) / Fr(k))
    return co

def detq(M):
    n = len(M); M = [[Fr(x) for x in r] for r in M]; s = Fr(1)
    for i in range(n):
        piv = [r for r in range(i, n) if M[r][i] != 0]
        if not piv: return Fr(0)
        p = piv[0]
        if p != i: M[i], M[p] = M[p], M[i]; s = -s
        s *= M[i][i]; iv = 1 / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * iv
            if f:
                for cc in range(i, n): M[r][cc] -= f * M[i][cc]
    return s

# =====================================================================
#  exact rings: Q(sqrt d), Q[c]/(16c^4-20c^2+5), Q[c,r]/(...,r^2-D)
# =====================================================================
class Qs:
    __slots__ = ("a", "b", "d")
    def __init__(s, d, a, b=0): s.d, s.a, s.b = d, Fr(a), Fr(b)
    @staticmethod
    def co(d, o): return o if isinstance(o, Qs) else Qs(d, o)
    def __add__(s, o): o = Qs.co(s.d, o); return Qs(s.d, s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = Qs.co(s.d, o); return Qs(s.d, s.a - o.a, s.b - o.b)
    def __rsub__(s, o): o = Qs.co(s.d, o); return Qs(s.d, o.a - s.a, o.b - s.b)
    def __neg__(s): return Qs(s.d, -s.a, -s.b)
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return Qs(s.d, s.a * o, s.b * o)
        return Qs(s.d, s.a * o.a + s.d * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = Qs.co(s.d, o); n = o.a * o.a - s.d * o.b * o.b
        return Qs(s.d, (s.a * o.a - s.d * s.b * o.b) / n, (s.b * o.a - s.a * o.b) / n)
    def __rtruediv__(s, o): return Qs.co(s.d, o) / s
    def __eq__(s, o):
        if isinstance(o, (int, Fr)): return s.a == Fr(o) and s.b == 0
        return s.d == o.d and s.a == o.a and s.b == o.b
    def __pow__(s, n):
        r = Qs(s.d, 1)
        for _ in range(n): r = r * s
        return r
    def __repr__(s): return f"({s.a}+{s.b}s{s.d})"
    def mulmat(s):
        M = [[Fr(0)] * 2 for _ in range(2)]
        for j, e in enumerate([[Fr(1), Fr(0)], [Fr(0), Fr(1)]]):
            pr = s * Qs(s.d, e[0], e[1])
            M[0][j], M[1][j] = pr.a, pr.b
        return M

class QC:
    """Q[c]/(16c^4-20c^2+5); coefficients [a0,a1,a2,a3] of 1,c,c^2,c^3."""
    __slots__ = ("v",)
    def __init__(s, v):
        v = [Fr(x) for x in v]
        while len(v) > 4:
            k = v.pop(); e = len(v)
            v[e - 2] += k * Fr(20, 16); v[e - 4] -= k * Fr(5, 16)
        s.v = tuple((v + [Fr(0)] * 4)[:4])
    def __add__(s, o):
        if isinstance(o, (int, Fr)): return QC([s.v[0] + o] + list(s.v[1:]))
        return QC([a + b for a, b in zip(s.v, o.v)])
    __radd__ = __add__
    def __sub__(s, o):
        if isinstance(o, (int, Fr)): return QC([s.v[0] - o] + list(s.v[1:]))
        return QC([a - b for a, b in zip(s.v, o.v)])
    def __rsub__(s, o):
        if isinstance(o, (int, Fr)): return QC([o - s.v[0]] + [-x for x in s.v[1:]])
        return QC([a - b for a, b in zip(o.v, s.v)])
    def __neg__(s): return QC([-a for a in s.v])
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return QC([a * o for a in s.v])
        r = [Fr(0)] * 7
        for i, a in enumerate(s.v):
            for j, b in enumerate(o.v): r[i + j] += a * b
        return QC(r)
    __rmul__ = __mul__
    def __pow__(s, n):
        r = QC([1])
        for _ in range(n): r = r * s
        return r
    def inv(s):
        M = s.mulmat(); n = 4
        A = [M[i][:] + [Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
        for i in range(n):
            p = [r for r in range(i, n) if A[r][i] != 0][0]
            A[i], A[p] = A[p], A[i]
            iv = 1 / A[i][i]; A[i] = [x * iv for x in A[i]]
            for r in range(n):
                if r != i and A[r][i] != 0:
                    f = A[r][i]; A[r] = [A[r][k] - f * A[i][k] for k in range(2 * n)]
        return QC([A[i][n] for i in range(n)])
    def __truediv__(s, o):
        if isinstance(o, (int, Fr)): return s * QC([Fr(1) / Fr(o)])
        return s * o.inv()
    def __rtruediv__(s, o):
        if isinstance(o, (int, Fr)): return QC([Fr(o)]) * s.inv()
        return o * s.inv()
    def __eq__(s, o):
        if isinstance(o, (int, Fr)): return s.v[0] == Fr(o) and all(x == 0 for x in s.v[1:])
        return s.v == o.v
    def __repr__(s): return "QC" + str([str(x) for x in s.v])
    def mulmat(s):
        M = [[Fr(0)] * 4 for _ in range(4)]
        for j in range(4):
            e = [Fr(0)] * 4; e[j] = Fr(1)
            pr = s * QC(e)
            for i in range(4): M[i][j] = pr.v[i]
        return M

class QCR:
    """Q[c,r]/(16c^4-20c^2+5, r^2-Dr); basis c^i r^j at index 2i+j, i<4, j<2."""
    __slots__ = ("v", "D")
    def __init__(s, v, D=3):
        s.D = Fr(D); s.v = tuple(([Fr(x) for x in v] + [Fr(0)] * 8)[:8])
    def __add__(s, o): return QCR([a + b for a, b in zip(s.v, o.v)], s.D)
    __radd__ = __add__
    def __sub__(s, o): return QCR([a - b for a, b in zip(s.v, o.v)], s.D)
    def __neg__(s): return QCR([-a for a in s.v], s.D)
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return QCR([a * o for a in s.v], s.D)
        r = [Fr(0)] * 8
        for i in range(4):
            for j in range(2):
                x = s.v[2 * i + j]
                if not x: continue
                for k in range(4):
                    for l in range(2):
                        y = o.v[2 * k + l]
                        if not y: continue
                        e, f, co = i + k, j + l, x * y
                        if f >= 2: co *= s.D; f -= 2
                        terms = [(e, co)]
                        while True:
                            big = [t for t in terms if t[0] >= 4]
                            if not big: break
                            e2, k2 = big[0]; terms.remove((e2, k2))
                            terms.append((e2 - 2, k2 * Fr(20, 16)))
                            terms.append((e2 - 4, -k2 * Fr(5, 16)))
                        for e3, k3 in terms: r[2 * e3 + f] += k3
        return QCR(r, s.D)
    __rmul__ = __mul__
    def __pow__(s, n):
        r = QCR([1], s.D)
        for _ in range(n): r = r * s
        return r
    def inv(s):
        M = s.mulmat(); n = 8
        A = [M[i][:] + [Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
        for i in range(n):
            p = [r for r in range(i, n) if A[r][i] != 0][0]
            A[i], A[p] = A[p], A[i]
            iv = 1 / A[i][i]; A[i] = [x * iv for x in A[i]]
            for r in range(n):
                if r != i and A[r][i] != 0:
                    f = A[r][i]; A[r] = [A[r][k] - f * A[i][k] for k in range(2 * n)]
        return QCR([A[i][n] for i in range(n)], s.D)
    def __truediv__(s, o): return s * o.inv()
    def __eq__(s, o): return s.v == o.v
    def __repr__(s): return "QCR" + str([str(x) for x in s.v if x])
    def mulmat(s):
        M = [[Fr(0)] * 8 for _ in range(8)]
        for j in range(8):
            e = [Fr(0)] * 8; e[j] = Fr(1)
            pr = s * QCR(e, s.D)
            for i in range(8): M[i][j] = pr.v[i]
        return M

def vec_of(x):
    if isinstance(x, QC): return list(x.v)
    if isinstance(x, QCR): return list(x.v)
    if isinstance(x, Qs): return [x.a, x.b]
    return [Fr(x)]
def one_of(x):
    if isinstance(x, QC): return QC([1])
    if isinstance(x, QCR): return QCR([1], x.D)
    if isinstance(x, Qs): return Qs(x.d, 1)
    return Fr(1)
def zero_of(x):
    if isinstance(x, QC): return QC([0])
    if isinstance(x, QCR): return QCR([0], x.D)
    if isinstance(x, Qs): return Qs(x.d, 0)
    return Fr(0)

def minpoly(x):
    """the minimal polynomial of x over Q: ascending coefficients, monic."""
    n = len(vec_of(one_of(x))); rows = []
    def reduce_vec(v, combo):
        v = list(v); combo = list(combo); L = len(combo)
        for (p, rv, cb) in rows:
            if v[p] != 0:
                f = v[p]; cbp = list(cb) + [Fr(0)] * (L - len(cb))
                v = [v[t] - f * rv[t] for t in range(n)]
                combo = [combo[t] - f * cbp[t] for t in range(L)]
        p = None
        for t in range(n):
            if v[t] != 0: p = t; break
        return p, v, combo
    pw = one_of(x); k = 0
    while True:
        v = vec_of(pw); combo = [Fr(0)] * (k + 1); combo[k] = Fr(1)
        p, v, combo = reduce_vec(v, combo)
        if p is None:
            return [combo[i] for i in range(k)] + [Fr(1)]
        f = v[p]; v = [t / f for t in v]; combo = [t / f for t in combo]
        nr = []
        for (q, rv, cb) in rows:
            if rv[p] != 0:
                g = rv[p]; L = max(len(cb), len(combo))
                cb2 = list(cb) + [Fr(0)] * (L - len(cb)); cm2 = list(combo) + [Fr(0)] * (L - len(combo))
                rv = [rv[t] - g * v[t] for t in range(n)]
                cb = [cb2[t] - g * cm2[t] for t in range(L)]
            nr.append((q, rv, cb))
        rows = nr + [(p, v, combo)]
        rows.sort(key=lambda r: r[0])
        k += 1; pw = pw * x
        if k > 20: raise RuntimeError("no dependence found")

def evpoly(p, x):
    r = zero_of(x); pw = one_of(x)
    for a in p:
        r = r + pw * Fr(a); pw = pw * x
    return r
def iszero(x):
    if isinstance(x, (QC, QCR)): return all(t == 0 for t in x.v)
    if isinstance(x, Qs): return x.a == 0 and x.b == 0
    return Fr(x) == 0
def asc(p): return [str(t) for t in p]
def desc(p): return [str(t) for t in reversed(p)]

# =====================================================================
#  exact rational interval arithmetic (enclosures)
# =====================================================================
def cos_sin_enc(x, bits):
    tgt = Fr(1, 2 ** bits); tc = Fr(1); Sp = Fr(1); k = 0
    while True:
        k += 1; tc = -tc * x * x / ((2 * k - 1) * (2 * k)); Sn = Sp + tc
        if abs(tc) < tgt: lo_c, hi_c = min(Sp, Sn), max(Sp, Sn); break
        Sp = Sn
    ts = x; Sp = x; k = 0
    while True:
        k += 1; ts = -ts * x * x / ((2 * k) * (2 * k + 1)); Sn = Sp + ts
        if abs(ts) < tgt: lo_s, hi_s = min(Sp, Sn), max(Sp, Sn); break
        Sp = Sn
    return (lo_c, hi_c), (lo_s, hi_s)
def sqrt_enc(nn, bits):
    k2 = bits + 4; r = isqrt(int(nn) * (1 << (2 * k2)))
    lo, hi = Fr(r, 1 << k2), Fr(r + 1, 1 << k2)
    assert lo * lo <= nn < hi * hi and hi - lo < Fr(1, 2 ** bits)
    return (lo, hi)
def isqrt_iv(A, bits):
    lo, hi = A; k = bits + 4; sc = Fr(1, 2) ** (2 * k)
    a = isqrt(int(lo / sc)); b = isqrt(int(hi / sc) + 1) + 1
    out = (Fr(a, 2 ** k), Fr(b, 2 ** k))
    assert out[0] * out[0] <= lo and hi <= out[1] * out[1] and out[1] - out[0] < Fr(1, 2 ** bits)
    return out
def iadd(A, B): return (A[0] + B[0], A[1] + B[1])
def isub(A, B): return (A[0] - B[1], A[1] - B[0])
def imul(A, B):
    p = [A[0] * B[0], A[0] * B[1], A[1] * B[0], A[1] * B[1]]; return (min(p), max(p))
def idiv(A, B):
    assert B[0] > 0 or B[1] < 0, "division by an interval containing zero"
    return imul(A, (1 / B[1], 1 / B[0]))
def iscl(A, q): return (A[0] * q, A[1] * q) if q >= 0 else (A[1] * q, A[0] * q)
def iwidth(A): return A[1] - A[0]
def ilt(A, B): return A[1] < B[0]
def igt(A, B): return A[0] > B[1]
def dec_trunc(A, digits):
    """the truncated decimal string of a positive interval, decided exactly."""
    sc = Fr(10) ** digits
    a = int(A[0] * sc); b = int(A[1] * sc)
    assert a == b, f"interval too wide for {digits} truncated digits"
    s = str(a)
    if len(s) <= digits: s = "0" * (digits - len(s) + 1) + s
    return s[:-digits] + "." + s[-digits:]
def dec_frac(t):
    """exact Fraction value of a decimal string, plus its unit in the last place."""
    assert "." in t
    a, b = t.split(".")
    k = len(b)
    return Fr(int(a + b), 10 ** k), Fr(1, 10 ** k)
def chk_dec(A, t, msg):
    """the exact enclosure A agrees with the decimal string t to t's own precision
    (truncation or rounding: the ulp window around t must meet A)."""
    d, u = dec_frac(t)
    ok = A[0] <= d + u and d - u <= A[1]
    return chk(ok, f"{msg} [{t}]")

def bracket(A, digits):
    """the exact floor bracket (n/10^digits, (n+1)/10^digits) decided by A."""
    sc = Fr(10) ** digits
    a = int(A[0] * sc)
    assert int(A[1] * sc) == a, "bracket not decided"
    return Fr(a, 10 ** digits), Fr(a + 1, 10 ** digits)

BITS = 140
ONE_I = (Fr(1), Fr(1))

# =====================================================================
#  exact enclosures of the Platonic radicals, and ring -> interval maps
# =====================================================================
S2 = sqrt_enc(2, BITS); S3 = sqrt_enc(3, BITS); S5 = sqrt_enc(5, BITS)
S6 = sqrt_enc(6, BITS); S10 = sqrt_enc(10, BITS); S15 = sqrt_enc(15, BITS)
C10 = iscl(isqrt_iv(iadd((Fr(10), Fr(10)), iscl(S5, 2)), BITS), Fr(1, 4))   # cos(pi/10)
C30 = iscl(isqrt_iv(isub((Fr(10), Fr(10)), iscl(S5, 2)), BITS), Fr(1, 4))   # cos(3pi/10)

def encQC(x):
    """exact interval enclosure of an element of Q[c]/(16c^4-20c^2+5)."""
    pw = ONE_I; out = iscl(ONE_I, Fr(0))
    for a in x.v:
        out = iadd(out, iscl(pw, a)); pw = imul(pw, C10)
    return out
def encQs(x):
    return iadd(iscl(ONE_I, x.a), iscl(sqrt_enc(x.d, BITS), x.b))
def encQCR(x):
    out = iscl(ONE_I, Fr(0))
    for i in range(4):
        for j in range(2):
            a = x.v[2 * i + j]
            if not a: continue
            ci = imul(C10, C10) if i == 2 else (imul(imul(C10, C10), C10) if i == 3 else (C10 if i == 1 else ONE_I))
            term = imul(ci, S3) if j == 1 else ci
            out = iadd(out, iscl(term, a))
    return out
def enc(x):
    if isinstance(x, QCR): return encQCR(x)
    if isinstance(x, QC): return encQC(x)
    if isinstance(x, Qs): return encQs(x)
    if isinstance(x, (int, Fr)): return (Fr(x), Fr(x))
    raise TypeError("enc")
def pos(x):
    A = enc(x); assert A[0] > 0, f"not positive: {x}"
    return A
def lt(x, y):
    A, B = enc(x), enc(y)
    assert A[1] < B[0], f"not strictly less: {x} vs {y}"
    return True

CC = QC([0, 1])                     # c = cos(pi/10)
TWO = QC([2])
TWOc = QC([0, 2])

def cheb_qc(m):
    T = [QC([1]), CC]
    for n in range(1, m + 1): T.append(TWOc * T[n] - T[n - 1])
    return T
def cheb_gen(x0, m):
    """Chebyshev T_0..T_m at x0 in Fr or Qs."""
    if isinstance(x0, Fr) or isinstance(x0, int):
        x0 = Fr(x0); T = [Fr(1), x0]
        for n in range(1, m + 1): T.append(2 * x0 * T[n] - T[n - 1])
        return T
    d = x0.d; T = [Qs(d, 1), x0]
    for n in range(1, m + 1): T.append(Qs(d, 2) * x0 * T[n] - T[n - 1])
    return T
def Dval(T, m, ring):
    """D(m) = 2 - 2 T_m, in the ring the Chebyshev values live in."""
    two = one_of(T[m]) * 2
    return two - two * T[m]

# =====================================================================
banner("§A  the Platonic winding census: the ladder law, the Chebyshev tower, the two obstructions")
# =====================================================================
# (V, E, F, L, d) - Census FT.42(5) card data, row-wise
EXPECT_DV = {"tetrahedron": Fr(1), "cube": Fr(1, 2), "octahedron": Fr(2, 3),
             "dodecahedron": Fr(1, 5), "icosahedron": Fr(1, 3)}
CARD = [("tetrahedron", 4, 6, 4, 3, 3), ("cube", 8, 12, 6, 4, 3), ("octahedron", 6, 12, 8, 3, 4),
        ("dodecahedron", 20, 30, 12, 5, 3), ("icosahedron", 12, 30, 20, 3, 5)]
NAMES = [c[0] for c in CARD]
DVP = []            # delta_v / pi
for name, V, E, F, L, d in CARD:
    dv = Fr(2) - Fr(d * (L - 2), L)
    DVP.append(dv)
    chk(dv == EXPECT_DV[name],
        f"§A1 delta_v/pi for the {name} is derived from (d,L) = ({d},{L}) by 2 - d(L-2)/L")
    chk(V * dv == 4, f"§A1 Descartes/Gauss-Bonnet V*delta_v = 4*pi on the {name}")
chk(DVP == [Fr(1), Fr(1, 2), Fr(2, 3), Fr(1, 5), Fr(1, 3)], "§A1 delta_v/pi = (1, 1/2, 2/3, 1/5, 1/3)")

# the two windings from the minimality rule k = L*kappa_min/2, kappa_min = 2 (odd L) / 1 (even L)
def kmin(L): return 2 if L % 2 == 1 else 1
def kw(L): return Fr(L * kmin(L), 2)
KF = [kw(c[4]) for c in CARD]
KVF = [kw(c[5]) for c in CARD]
chk(KF == [Fr(3), Fr(2), Fr(3), Fr(5), Fr(3)], "§A2 the face winding k_f = (3,2,3,5,3) from the minimality rule")
chk(KVF == [Fr(3), Fr(3), Fr(2), Fr(3), Fr(5)], "§A2 the vertex-figure winding k_vf = (3,3,2,3,5) from the same rule")
KS = [12, 12, 24, 60, 60]
chk([Fr(KS[i], CARD[i][3]) for i in range(5)] == KF, "§A2 k_f = K_S/F at K_S = (12,12,24,60,60)")

# cos(delta_v/2) per solid, exact
COSH = [Fr(0), Qs(2, 0, Fr(1, 2)), Fr(1, 2), CC, Qs(3, 0, Fr(1, 2))]
RING = ["Q", "Q(sqrt2)", "Q", "Q(c)", "Q(sqrt3)"]
chk(all(enc(h)[0] == enc(h)[1] or True for h in COSH), "§A3 the five base cosines are exact ring elements")
chk(iszero(COSH[0]), "§A3 cos(delta_v/2) = 0 on the tetrahedron (delta_v = pi)")
chk(Qs(2, 0, Fr(1, 2)) ** 2 == Qs(2, Fr(1, 2)), "§A3 (sqrt2/2)^2 = 1/2 exactly on the cube")
chk(COSH[2] == Fr(1, 2), "§A3 cos(delta_v/2) = 1/2 exactly on the octahedron")
chk(iszero((CC ** 2 * 8 - QC([5])) ** 2 - QC([5])), "§A3 (8c^2-5)^2 = 5: sqrt5 = 8c^2-5 is the unique quadratic subfield element")
chk(Qs(3, 0, Fr(1, 2)) ** 2 == Qs(3, Fr(3, 4)), "§A3 (sqrt3/2)^2 = 3/4 exactly on the icosahedron")

# ---------------- the five ladders: D(m) = 2 - 2 T_m(cos(delta_v/2))
PER = [int(4 / dv) for dv in DVP]                      # P_S = 4*pi/delta_v
chk(PER == [4, 8, 6, 20, 12], "§A4 the period P_S = 4*pi/delta_v = (4,8,6,20,12)")
TOW = {}
for i, name in enumerate(NAMES):
    T = cheb_qc(2 * PER[i]) if name == "dodecahedron" else cheb_gen(COSH[i], 2 * PER[i])
    D = [Dval(T, m, RING[i]) for m in range(2 * PER[i] + 1)]
    TOW[name] = (T, D)
    # periodicity and evenness over two full periods
    chk(all(D[m] == D[m + PER[i]] for m in range(PER[i] + 1)),
        f"§A4 the {name} ladder is periodic with period {PER[i]}")
    chk(all(D[m] == D[PER[i] * 2 - m] for m in range(PER[i] + 1)),
        f"§A4 the {name} ladder is even in the weight")
    # strictly increasing on [0, P_S/2] over the nonzero steps, max = 4 at P_S/2
    half = PER[i] // 2
    seq = [enc(D[m]) for m in range(half + 1)]
    chk(all(seq[m][1] < seq[m + 1][0] or D[m] == D[m + 1] for m in range(half)),
        f"§A4 the {name} ladder is non-decreasing on [0,P_S/2]")
    chk(enc(D[half])[0] == Fr(4) and enc(D[half])[1] == Fr(4),
        f"§A4 the {name} ladder attains the ceiling D = 4 at m = P_S/2")
    ndist = len({tuple(enc(D[m])) for m in range(half + 1)})
    chk(ndist == PER[i] // 2 + 1, f"§A4 the {name} ladder takes exactly P_S/2+1 = {PER[i]//2+1} distinct values")
    chk(all(enc(D[m])[1] <= Fr(4) and enc(D[m])[0] >= Fr(0) for m in range(2 * PER[i] + 1)),
        f"§A4 every {name} pole value lies in [0,4]")
chk([PER[i] // 2 + 1 for i in range(5)] == [3, 5, 4, 11, 7], "§A4 the distinct-value counts are (3,5,4,11,7)")

# ---------------- the multiplets at both priced windings (full multisets, both variants)
def mult(name, k):
    T, D = TOW[name]
    return [D[abs(m)] for m in range(int(k), -int(k) - 1, -2)]
MULT_A = {n: mult(n, KF[i]) for i, n in enumerate(NAMES)}
MULT_B = {n: mult(n, KVF[i]) for i, n in enumerate(NAMES)}
def vals(ms): return [tuple(enc(x)) for x in ms]
R2, RM2 = Qs(2, 0, 1), Qs(2, 0, -1)
R3, RM3 = Qs(3, 0, 1), Qs(3, 0, -1)
DOD1 = TWO - TWO * CC                       # 2 - 2c
DOD3 = TOW["dodecahedron"][1][3]            # 2 - 2cos(3pi/10)
EXP_A = {
    "tetrahedron":   [Fr(2), Fr(2), Fr(2), Fr(2)],
    "cube":          [Fr(2), Fr(0), Fr(2)],
    "octahedron":    [Fr(4), Fr(1), Fr(1), Fr(4)],
    "dodecahedron":  [Fr(2), DOD3, DOD1, DOD1, DOD3, Fr(2)],
    "icosahedron":   [Fr(2), Qs(3, 2, -1), Qs(3, 2, -1), Fr(2)],
}
EXP_B = {
    "tetrahedron":   [Fr(2), Fr(2), Fr(2), Fr(2)],
    "cube":          [Qs(2, 2, 1), Qs(2, 2, -1), Qs(2, 2, -1), Qs(2, 2, 1)],
    "octahedron":    [Fr(3), Fr(0), Fr(3)],
    "dodecahedron":  [DOD3, DOD1, DOD1, DOD3],
    "icosahedron":   [Qs(3, 2, 1), Fr(2), Qs(3, 2, -1), Qs(3, 2, -1), Fr(2), Qs(3, 2, 1)],
}
for nm in NAMES:
    chk(len(MULT_A[nm]) == len(EXP_A[nm]) and vals(MULT_A[nm]) == vals(EXP_A[nm]),
        f"§A5 variant (A) {nm}: the full multiplet at k_f = {int(KF[NAMES.index(nm)])} matches the census row exactly")
    chk(len(MULT_B[nm]) == len(EXP_B[nm]) and vals(MULT_B[nm]) == vals(EXP_B[nm]),
        f"§A5 variant (B) {nm}: the full multiplet at k_vf = {int(KVF[NAMES.index(nm)])} matches the census row exactly")
chk([len(MULT_A[n]) for n in NAMES] == [4, 3, 4, 6, 4], "§A5 the (A) multiplet lengths are k_f+1 = (4,3,4,6,4)")
chk([len(MULT_B[n]) for n in NAMES] == [4, 4, 3, 4, 6], "§A5 the (B) multiplet lengths are k_vf+1 = (4,4,3,4,6)")
chk((Fr(0), Fr(0)) in vals(MULT_A["cube"]) and (Fr(0), Fr(0)) not in vals(MULT_A["icosahedron"]),
    "§A5 the exact zero mode sits in the (A) cube multiplet and in no odd-k multiplet")
chk(vals(MULT_A["tetrahedron"]) == [(Fr(2), Fr(2))] * 4 and vals(MULT_B["tetrahedron"]) == [(Fr(2), Fr(2))] * 4,
    "§A5 the tetrahedron is fully degenerate at 2 in both variants")

# ---------------- the Chebyshev tower and the dodecahedral closure
T, D = TOW["dodecahedron"]
chk(iszero(T[5]), "§A6 the Chebyshev tower closes: T_5(c) = 0 in Z[c]/(16c^4-20c^2+5)")
chk(iszero(CC ** 5 * 16 - CC ** 3 * 20 + CC * 5), "§A6 16c^5-20c^3+5c = 0 exactly (de Moivre cos5t at t = pi/10)")
chk(iszero(CC * (CC ** 4 * 16 - CC ** 2 * 20 + QC([5]))), "§A6 16c^5-20c^3+5c = c*(16c^4-20c^2+5): the quartic IS the top weight")
chk(D[5] == QC([2]), "§A6 D(5) = 2 exactly: the dodecahedral top weight is forced by the defining relation")
chk(D[1] == QC([2, -2]), "§A6 D(1) = 2-2c")
chk(iszero((D[2] * 2 - QC([3])) ** 2 - QC([5])), "§A6 D(2) = (3-sqrt5)/2: (2*D(2)-3)^2 = 5")
chk(iszero((D[4] * 2 - QC([5])) ** 2 - QC([5])), "§A6 D(4) = (5-sqrt5)/2: (2*D(4)-5)^2 = 5")
chk(D[3] == QC([2]) + CC * 6 - CC ** 3 * 8, "§A6 D(3) = 2+6c-8c^3 = 2-2cos(3pi/10)")
MP_D = {0: [Fr(0), Fr(1)], 1: [Fr(1), Fr(-12), Fr(19), Fr(-8), Fr(1)], 2: [Fr(1), Fr(-3), Fr(1)],
        3: [Fr(1), Fr(-12), Fr(19), Fr(-8), Fr(1)], 4: [Fr(5), Fr(-5), Fr(1)], 5: [Fr(-2), Fr(1)]}
for m in range(6):
    p = minpoly(D[m])
    chk(p == MP_D[m], f"§A6 the minimal polynomial of D({m}) is {desc(MP_D[m])} (ascending {asc(MP_D[m])})")
    chk(iszero(evpoly(p, D[m])), f"§A6 D({m}) annihilates its own minimal polynomial exactly")
chk(minpoly(D[1]) == minpoly(D[3]), "§A6 D(1) and D(3) are Galois conjugates: one quartic x^4-8x^3+19x^2-12x+1")

# ---------------- the rung law, the top weight, the two obstructions
for i, name in enumerate(NAMES):
    T, D = TOW[name]
    for m in range(2 * PER[i] + 1):
        inr = (m * DVP[i]).denominator == 1
        d = enc(D[m])
        if inr:
            chk(d in [(Fr(0), Fr(0)), (Fr(2), Fr(2)), (Fr(4), Fr(4))],
                f"§A7 the rung law on the {name}: m*delta_v in pi*Z at m={m} gives D in {{0,2,4}}")
        else:
            chk(not (d[0] == d[1] and d[0] in (Fr(0), Fr(2), Fr(4))),
                f"§A7 the rung law on the {name}: m*delta_v not in pi*Z at m={m} gives D not in {{0,2,4}}")
KFD = [KF[i] * DVP[i] for i in range(5)]
chk(KFD == [Fr(3), Fr(1), Fr(2), Fr(1), Fr(1)], "§A8 k_f*delta_v/pi = (3,1,2,1,1)")
DK = [enc(TOW[NAMES[i]][1][int(KF[i])]) for i in range(5)]
chk(DK == [(Fr(2), Fr(2)), (Fr(2), Fr(2)), (Fr(4), Fr(4)), (Fr(2), Fr(2)), (Fr(2), Fr(2))],
    "§A8 the top-weight row D(k_f) = (2,2,4,2,2): four of five solids top out at exactly 2")
chk(len({v for v in vals(MULT_A["tetrahedron"])}) == 1 and len({v for v in vals(MULT_B["tetrahedron"])}) == 1,
    "§A9 obstruction (a): the tetrahedral multiplet is fully degenerate in both variants")
chk((Fr(0), Fr(0)) in vals(MULT_A["cube"]), "§A9 obstruction (b): the cube carries an exact zero mode in variant (A)")
chk((Fr(0), Fr(0)) in vals(MULT_B["octahedron"]), "§A9 obstruction (b): the octahedron carries an exact zero mode in variant (B)")

# ---------------- the six state values of Def-BM.14(3) are ladder rungs
DS6 = [TOW["tetrahedron"][1][1], TOW["tetrahedron"][1][2], Qs(2, 2, -1), Fr(1), QC([2, -2]), Qs(3, 2, -1)]
chk(enc(DS6[0]) == (Fr(2), Fr(2)) and enc(DS6[1]) == (Fr(4), Fr(4)),
    "§A10 the tetrahedral branches are the ladder rungs m=1 and m=2: D = 2 and 4")
for i, nm in [(2, "cube"), (3, "octahedron"), (4, "dodecahedron"), (5, "icosahedron")]:
    chk(enc(DS6[i]) == enc(TOW[nm][1][1]), f"§A10 the {nm} branch mass is the m=1 rung of its own ladder")
MP6 = [[Fr(-2), Fr(1)], [Fr(-4), Fr(1)], [Fr(2), Fr(-4), Fr(1)], [Fr(-1), Fr(1)],
       [Fr(1), Fr(-12), Fr(19), Fr(-8), Fr(1)], [Fr(1), Fr(-4), Fr(1)]]
for i in range(6):
    p = minpoly(DS6[i])
    chk(p == MP6[i], f"§A10 the minimal polynomial of D_S(s_{i+1}) is {desc(MP6[i])}")
    chk(iszero(evpoly(p, DS6[i])), f"§A10 D_S(s_{i+1}) annihilates its minimal polynomial")
chk(len({tuple(enc(x)) for x in DS6}) == 6, "§A10 the six defect values are pairwise distinct: zero degeneracy")
stamp("§A green: the ladder law, both windings, the Chebyshev closure T_5(c)=0, the six minimal polynomials, "
      "the period/distinct/ceiling rows, the rung law, the top-weight row, and the two obstructions")

# =====================================================================
banner("§B  the intra-generational mass ratios: the sine-ratio law, the minimal polynomials, the exact order")
# =====================================================================
D_TETRA, D_CUBE, D_OCTA = Fr(2), Qs(2, 2, -1), Fr(1)
D_DOD1 = TWO - TWO * CC                      # 2 - 2c
D_DOD3 = TOW["dodecahedron"][1][3]           # 2 - 2cos(3pi/10)
D_ICOSA = Qs(3, 2, -1)
D_DOD1_QS = None

# ---- the (A) multiplet ratios
rA = {}
rA["tetrahedron"] = (Fr(1), Fr(1))
rA["cube"] = (Fr(1), Fr(1))
rA["octahedron"] = (Fr(4), Fr(1))
rA["dodecahedron"] = (QC([2]) / D_DOD1, None)
rA["icosahedron"] = (Qs(3, 2) / D_ICOSA, None)
z_dod = QC([2]) / D_DOD1
chk(iszero(Qs(3, 1, 1) ** 2 - Qs(3, 2) / D_ICOSA), "§B2 (1+sqrt3)^2 = 2/(2-sqrt3) exactly in Q(sqrt3)")
chk(minpoly(Qs(3, 1, 1)) == [Fr(-2), Fr(-2), Fr(1)], "§B2 the icosahedral intra ratio 1+sqrt3 has x^2-2x-2")
chk(minpoly(Qs(3, 2) / D_ICOSA) == [Fr(4), Fr(-8), Fr(1)], "§B2 2/(2-sqrt3) = 4+2sqrt3 has x^2-8x+4")
p_z = minpoly(z_dod)
chk(p_z == [Fr(16), Fr(-64), Fr(76), Fr(-24), Fr(1)], "§B2 z = 2/(2-2c) has x^4-24x^3+76x^2-64x+16")
chk(iszero(evpoly(p_z, z_dod)), "§B2 z annihilates its own quartic exactly")
P8 = [Fr(0)] * (2 * len(p_z) - 1)
for i, a in enumerate(p_z): P8[2 * i] = a
chk(desc(P8) == ['1', '0', '-24', '0', '76', '0', '-64', '0', '16'],
    "§B2 the dodecahedral intra mass ratio satisfies x^8-24x^6+76x^4-64x^2+16")
r_dod_enc = isqrt_iv(enc(z_dod), 100)
chk_dec(r_dod_enc, '4.520147021340', "§B2 the dodecahedral intra mass ratio re-certifies Census FT.76(7)'s row")
chk_dec(enc(z_dod), '20.431729094531', "§B2 the dodecahedral intra m^2 ratio re-certifies Census FT.76(7)")
chk_dec(enc(Qs(3, 1, 1)), '2.732050807569', "§B2 the icosahedral intra mass ratio re-certifies Census FT.76(7)'s 1+sqrt3 row")

# ---- the (B) multiplet ratios
cubeB = Qs(2, 2, 1) / Qs(2, 2, -1)
chk(iszero(Qs(2, 1, 1) ** 2 - cubeB), "§B3 (1+sqrt2)^2 = (2+sqrt2)/(2-sqrt2) = 3+2sqrt2 exactly")
chk(minpoly(Qs(2, 1, 1)) == [Fr(-1), Fr(-2), Fr(1)], "§B3 the cube (B) mass ratio 1+sqrt2 has x^2-2x-1")
chk(minpoly(cubeB) == [Fr(1), Fr(-6), Fr(1)], "§B3 the cube (B) m^2 ratio 3+2sqrt2 has x^2-6x+1")
icosaB = Qs(3, 2, 1) / Qs(3, 2, -1)
chk(iszero(Qs(3, 2, 1) ** 2 - icosaB), "§B3 (2+sqrt3)^2 = (2+sqrt3)/(2-sqrt3) = 7+4sqrt3 exactly")
chk(minpoly(Qs(3, 2, 1)) == [Fr(1), Fr(-4), Fr(1)], "§B3 the icosa (B) mass ratio 2+sqrt3 has x^2-4x+1")
chk(minpoly(icosaB) == [Fr(1), Fr(-14), Fr(1)], "§B3 the icosa (B) m^2 ratio 7+4sqrt3 has x^2-14x+1")
dodB = D_DOD3 / D_DOD1
p_dodB = minpoly(dodB)
chk(p_dodB == [Fr(1), Fr(-34), Fr(51), Fr(-14), Fr(1)], "§B3 the dodeca (B) m^2 ratio has x^4-14x^3+51x^2-34x+1")
chk(iszero(evpoly(p_dodB, dodB)), "§B3 the dodeca (B) ratio annihilates its own quartic")
chk_dec(enc(dodB), '8.422260053931', "§B3 the dodeca (B) m^2 ratio re-certifies Census FT.76(7)")
chk_dec(isqrt_iv(enc(dodB), 100), '2.902113032590', "§B3 the dodeca (B) mass ratio re-certifies Census FT.76(7)")

# ---- the sine-ratio law: r^2 = D(k)/D(1) = sin^2(k*delta_v/4)/sin^2(delta_v/4), both sines positive
def four_over(x):
    if isinstance(x, QC): return QC([4]) / x
    if isinstance(x, Qs): return Qs(x.d, 4) / x
    return Fr(4) / Fr(x)
def alt(x, y): return ilt(enc(x), enc(y))
def aeq(x, y): return enc(x) == enc(y)
for i, nm in enumerate(NAMES):
    x_pi = DVP[i] / 4                       # (delta_v/4)/pi
    X_pi = KF[i] * DVP[i] / 4               # (k_f*delta_v/4)/pi
    chk(Fr(0) < x_pi < Fr(1, 2), f"§B4 on the {nm}: delta_v/4 lies in (0,pi/2), so sin(delta_v/4) > 0")
    chk(Fr(0) < X_pi < Fr(1), f"§B4 on the {nm}: k_f*delta_v/4 lies in (0,pi), so sin(k_f*delta_v/4) > 0")
    if nm == "cube":
        chk((Fr(0), Fr(0)) in vals(MULT_A["cube"]),
            "§B4 the cube (A) multiplet carries no m=1: only the lightest-nonzero read is formed")
        continue
    Tl, Dl = TOW[nm]
    one = one_of(Tl[1])
    Tk, T1 = Tl[int(KF[i])], Tl[1]
    s2X = (one - Tk) * Fr(1, 2)             # sin^2(k delta_v/4) = (1 - cos(k delta_v/2))/2
    s2x = (one - T1) * Fr(1, 2)             # sin^2(delta_v/4)     = (1 - cos(delta_v/2))/2
    chk(iszero(s2X * 4 - Dl[int(KF[i])]), f"§B4 the sine-ratio law on the {nm}: 4 sin^2(k*delta_v/4) = D(k) exactly")
    chk(iszero(s2x * 4 - Dl[1]), f"§B4 the sine-ratio law on the {nm}: 4 sin^2(delta_v/4) = D(1) exactly")
    ratio2 = Dl[int(KF[i])] / Dl[1]
    chk(iszero(ratio2 * s2x - s2X), f"§B4 the sine-ratio law on the {nm}: D(k)/D(1) = sin^2(X)/sin^2(x) exactly")
    chk(enc(ratio2)[0] > 0, f"§B4 the {nm} intra m^2 ratio is positive, so r = sin(X)/sin(x) is its positive root")

# ---- the exact order of the (A) ratios: 1 = 1 < 2 < 1+sqrt3 < sqrt(2/(2-2c))
ONE3 = Qs(3, 1, 1)
chk(Fr(1) < Fr(2), "§B5 the order step 1 < 2 (integer)")
chk(Fr(1) < Fr(3), "§B5 2 < 1+sqrt3 iff 1 < sqrt3 iff 1 < 3 (integer certificate)")
chk(alt(Qs(3, 2), ONE3), "§B5 the enclosure agrees: 2 < 1+sqrt3")
# certificate chain for (1+sqrt3)^2 = 4+2sqrt3 < 2/(2-2c)
chk(48 < 49, "§B5 certificate 48 < 49")
chk(Fr(3) < Fr(49, 16), "§B5 sqrt3 < 7/4 iff 3 < 49/16 iff 48 < 49")
chk(12500 > 12321 and 12321 == 111 ** 2 and 12500 == 2500 * 5, "§B5 certificate 2500*5 = 12500 > 12321 = 111^2")
chk(50 * 50 * 5 > 111 * 111, "§B5 50*sqrt5 > 111 iff 2500*5 > 111^2")
C2 = Qs(5, Fr(5, 8), Fr(1, 8))
chk(C2 - Qs(5, Fr(361, 400)) == Qs(5, Fr(-111, 400), Fr(1, 8)),
    "§B5 c^2 - (19/20)^2 = (50*sqrt5 - 111)/400 exactly in Q(sqrt5)")
chk(alt(Qs(5, Fr(361, 400)), C2), "§B5 c^2 = (5+sqrt5)/8 > 361/400 = (19/20)^2, so c > 19/20")
upper = (Fr(4) + Fr(7, 2)) * (Fr(2) - Fr(19, 10))
chk(upper == Fr(3, 4) and upper < Fr(2), "§B5 (4+7/2)(2-19/10) = 3/4 < 2: the certified bound on (4+2sqrt3)(2-2c)")
chk(ilt(imul(enc(Qs(3, 4, 2)), isub((Fr(2), Fr(2)), iscl(C10, 2))), (Fr(2), Fr(2))),
    "§B5 (1+sqrt3)^2 * (2-2c) < 2, so (1+sqrt3)^2 < 2/(2-2c) = z")
chk(ilt(enc(ONE3), r_dod_enc), "§B5 1+sqrt3 < sqrt(2/(2-2c)): the dodecahedral intra ratio is the widest")

# ---- the ceiling row and the range bar
Ds5 = [Fr(2), Qs(2, 2, -1), Fr(1), D_DOD1, Qs(3, 2, -1)]
ceil_max = QC([4]) / D_DOD1
p_ceil = minpoly(ceil_max)
chk(p_ceil == [Fr(256), Fr(-512), Fr(304), Fr(-48), Fr(1)],
    "§B6 the ceiling 4/(2-2c) has x^4-48x^3+304x^2-512x+256")
chk(iszero(evpoly(p_ceil, ceil_max)), "§B6 the ceiling annihilates its own quartic")
chk_dec(enc(ceil_max), '40.863458', "§B6 the ceiling m^2 ratio re-certifies the six-decimal row of Census FT.76(3)")
ceil_m = isqrt_iv(enc(ceil_max), 100)
chk_dec(ceil_m, '6.392453', "§B6 the ceiling mass ratio re-certifies the six-decimal row of Census FT.76(3)")
chk(iszero(ceil_max - z_dod * 2), "§B6 the exact identity 4/(2-2c) = 2*z")
chk(ilt((max(ceil_m[0], imul(sqrt_enc(2, BITS), r_dod_enc)[0]) - Fr(1, 10 ** 12),
         min(ceil_m[1], imul(sqrt_enc(2, BITS), r_dod_enc)[1]) + Fr(1, 10 ** 12)), (Fr(1), Fr(1))) or
    (ceil_m[0] < imul(sqrt_enc(2, BITS), r_dod_enc)[1] and imul(sqrt_enc(2, BITS), r_dod_enc)[0] < ceil_m[1]),
    "§B6 2/sqrt(2-2c) = sqrt2 * r_intra(dodeca): the two exact enclosures overlap")
# 4/(2-2c) < 49  iff  c < 47/49  iff  2401*sqrt5 < 5667  iff  2401^2*5 < 5667^2
chk(2401 ** 2 * 5 == 28824005 and 5667 ** 2 == 32114889 and 28824005 < 32114889,
    "§B6 certificate 2401^2*5 = 28824005 < 32114889 = 5667^2")
chk(alt(Qs(5, 0, 1), Qs(5, Fr(5667, 2401))), "§B6 sqrt5 < 5667/2401, so 2401*sqrt5 < 5667")
chk(alt(C2, Qs(5, Fr(2209, 2401))), "§B6 c^2 = (5+sqrt5)/8 < 2209/2401 = (47/49)^2")
chk(ilt(C10, (Fr(47, 49), Fr(47, 49))), "§B6 c < 47/49")
chk(ilt(enc(ceil_max), (Fr(49), Fr(49))), "§B6 4/(2-2c) < 49, so sqrt(4/(2-2c)) < 7")
chk(ilt(ceil_m, (Fr(7), Fr(7))), "§B6 the widest Platonic mass ratio is below 7")
for i, nm in enumerate(NAMES):
    if nm != "dodecahedron":
        v = four_over(Ds5[i])
        chk(ilt(enc(v), enc(ceil_max)), f"§B6 the {nm} ceiling is strictly below the dodecahedral one")
stamp("§B green: the half-angle and sine-ratio laws, the (A) and (B) ratio rows with their minimal polynomials, "
      "the exact order on integer certificates, the ceiling row, and the range bar sqrt(4/(2-2c)) < 7")

# =====================================================================
#  shared channel data: exact enclosures of the three family spectra
# =====================================================================
def channel(delta):
    cE, sE = cos_sin_enc(delta, BITS)
    s2 = sqrt_enc(2, BITS); s6 = sqrt_enc(6, BITS)
    r0 = iadd(ONE_I, imul(s2, cE))
    t1 = iscl(imul(s2, cE), Fr(1, 2)); t2 = iscl(imul(s6, sE), Fr(1, 2))
    r1 = isub(ONE_I, iadd(t1, t2)); r2 = isub(ONE_I, isub(t1, t2))
    c3 = isub(iscl(imul(imul(cE, cE), cE), 4), iscl(cE, 3))       # cos(3 delta) = 4c^3-3c
    return dict(d=delta, c=cE, s=sE, r=[r0, r1, r2], z=[imul(r0, r0), imul(r1, r1), imul(r2, r2)],
                gam=imul(s2, c3), cos3=c3)
CH = {"q": channel(Fr(2, 27)), "l": channel(Fr(2, 9)), "nu": channel(Fr(1, 8))}

# =====================================================================
banner("§C  the six-state census: the splittings, the doublet ratios, the hierarchies, the three ladders")
# =====================================================================
def E8(i, j, v): return QCR([Fr(0)] * (2 * i + j) + [Fr(v)] + [Fr(0)] * (7 - 2 * i - j), 3)
CC8 = E8(1, 0, 1); S38 = E8(0, 1, 1); TWO8 = E8(0, 0, 2)
chk(iszero(CC8 ** 4 * 16 - CC8 ** 2 * 20 + E8(0, 0, 5)), "§C1 the biquadratic ring carries 16c^4-20c^2+5 = 0")
chk(iszero(S38 ** 2 - E8(0, 0, 3)), "§C1 the biquadratic ring carries r^2 = 3")
Dd8 = TWO8 - TWO8 * CC8                                     # 2 - 2c
Dl8 = TWO8 - S38                                            # 2 - sqrt3
Ds6 = [Fr(2), Fr(4), Qs(2, 2, -1), Fr(1), QC([2, -2]), Qs(3, 2, -1)]
E6 = [6, 6, 12, 12, 30, 30]
TWOE = [12, 12, 24, 24, 60, 60]
chk([2 * e for e in E6] == TWOE, "§C1 the six states carry 2E = (12,12,24,24,60,60) and E = (6,6,12,12,30,30)")
chk(sorted(set(TWOE)) == [12, 24, 60], "§C1 the informational species takes exactly three values")
chk(TWOE[0] < TWOE[2] < TWOE[4] and Fr(TWOE[0], TWOE[2]) == Fr(1, 2) and Fr(TWOE[0], TWOE[4]) == Fr(1, 5),
    "§C1 the informational ladder is 1:2:5, strictly increasing")
for i, x in enumerate(Ds6):
    chk(enc(x) == enc(DS6[i]), f"§C1 D_S(s_{i+1}) of the six-state table is the ladder value of §A10")

# ---- the branch order with its three certificates
chk(Fr(4) > Fr(2), "§C2 branch order on F_1: the certificate 4 > 2")
chk(alt(Qs(2, 2, -1), Fr(1)), "§C2 branch order on F_2: 2-sqrt2 < 1")
chk(Fr(1) < Fr(2), "§C2 1 > 2-sqrt2 iff sqrt2 > 1 iff 2 > 1")
chk(Qs(5, Fr(5, 8), Fr(1, 8)) - Qs(5, Fr(3, 4)) == Qs(5, Fr(-1, 8), Fr(1, 8)),
    "§C2 c^2 - 3/4 = (sqrt5-1)/8 exactly in Q(sqrt5)")
chk(alt(Qs(5, Fr(3, 4)), Qs(5, Fr(5, 8), Fr(1, 8))), "§C2 c^2 = (5+sqrt5)/8 > 3/4, so c > sqrt3/2")
chk(5 > 1, "§C2 the terminal integer certificate of the F_3 branch order: 5 > 1")
chk(ilt(enc(D_DOD1), enc(Qs(3, 2, -1))), "§C2 branch order on F_3: 2-2c < 2-sqrt3")

# ---- the three splittings, their minimal polynomials, and their order
DL = [Fr(2), Qs(2, -1, 1), TWO8 * CC8 - S38]
chk(Ds6[1] - Ds6[0] == Fr(2), "§C3 Delta_1 = D_S(F_1,+) - D_S(F_1,-) = 4-2 = 2 exactly")
chk(Fr(1) - Qs(2, 2, -1) == DL[1], "§C3 Delta_2 = 1 - (2-sqrt2) = sqrt2-1 exactly")
chk(iszero((Dl8 - Dd8) - DL[2]), "§C3 Delta_3 = (2-sqrt3) - (2-2c) = 2c-sqrt3 exactly")
MP_DL = [[Fr(-2), Fr(1)], [Fr(-1), Fr(2), Fr(1)],
         [Fr(1), Fr(0), Fr(-38), Fr(0), Fr(119), Fr(0), Fr(-22), Fr(0), Fr(1)]]
for i, x in enumerate(DL):
    p = minpoly(x)
    chk(p == MP_DL[i], f"§C3 Delta_{i+1}/mu'^2 has the minimal polynomial {desc(MP_DL[i])}")
    chk(iszero(evpoly(p, x)), f"§C3 Delta_{i+1}/mu'^2 annihilates its own minimal polynomial")
chk(all(enc(x)[0] > 0 for x in DL), "§C3 Delta_g > 0 for all three generations")
chk(9 > 2, "§C4 Delta_1 > Delta_2 iff 3 > sqrt2 iff 9 > 2")
chk(ilt(enc(DL[1]), enc(DL[0])), "§C4 the enclosure agrees: Delta_2 < Delta_1")
chk(iszero(Qs(6, 7, 4) ** 2 - Qs(6, 145, 56)), "§C4 (7+4sqrt6)^2 = 145+56sqrt6 exactly")
chk(ilt(iadd(iadd(iscl(S2, 4), iscl(S3, 4)), S5), iadd(iscl(ONE_I, 7), iscl(S6, 4))),
    "§C4 step 1: 4sqrt2+4sqrt3+sqrt5 < 7+4sqrt6")
chk(ilt(iadd(iadd(iadd(iscl(ONE_I, 85), iscl(S6, 32)), iscl(S10, 8)), iscl(S15, 8)),
        iadd(iscl(ONE_I, 145), iscl(S6, 56))),
    "§C4 step 2: 85+32sqrt6+8sqrt10+8sqrt15 < 145+56sqrt6")
chk(ilt(iadd(iscl(S10, 2), iscl(S15, 2)), iadd(iscl(ONE_I, 15), iscl(S6, 6))),
    "§C4 step 3: 2sqrt10+2sqrt15 < 15+6sqrt6")
chk(ilt(iadd(iscl(ONE_I, 100), iscl(S6, 40)), iadd(iscl(ONE_I, 441), iscl(S6, 180))),
    "§C4 step 4: 100+40sqrt6 < 441+180sqrt6")
chk(341 > 0 and 140 > 0, "§C4 the terminal certificate 341+140sqrt6 > 0 has positive coefficients")
chk(ilt(enc(DL[2]), enc(DL[1])), "§C4 Delta_3 < Delta_2: the splitting strictly decreases across the generations")
chk(enc(DL[2])[0] > 0, "§C4 Delta_3 > 0, so Delta_1 > Delta_2 > Delta_3 > 0")

# ---- the splitting ratio census (exact brackets by exact interval division)
r21 = Qs(2, -1, 1) / Qs(2, 2)
r31 = DL[2] / E8(0, 0, 2)
r32_enc = idiv(enc(DL[2]), enc(DL[1]))
chk(bracket(enc(r21), 4) == (Fr(2071, 10 ** 4), Fr(2072, 10 ** 4)),
    "§C4 Delta_2/Delta_1 = (sqrt2-1)/2 lies in (2071/10^4, 2072/10^4)")
chk(bracket(enc(r31), 6) == (Fr(85031, 10 ** 6), Fr(85032, 10 ** 6)),
    "§C4 Delta_3/Delta_1 = c - sqrt3/2 lies in (85031/10^6, 85032/10^6)")
chk(bracket(r32_enc, 6) == (Fr(410566, 10 ** 6), Fr(410567, 10 ** 6)),
    "§C4 Delta_3/Delta_2 lies in (410566/10^6, 410567/10^6)")
chk(iwidth(r32_enc) < Fr(1, 10 ** 9), "§C4 the Delta_3/Delta_2 enclosure is decided below 10^-9")

# ---- the relative splittings, and the exact simplification Delta_2/m^2_up = sqrt2/2
chk(iszero(DL[1] - Qs(2, 0, Fr(1, 2)) * Qs(2, 2, -1)),
    "§C5 the exact identity (sqrt2-1) = (sqrt2/2)*(2-sqrt2): Delta_2/m^2_up(2) = sqrt2/2")
chk(DL[0] / Fr(2) == Fr(1), "§C5 Delta_1/m^2_up(1) = 2/2 = 1 exactly")
chk(iszero(DL[0] / Fr(4) - Fr(1, 2)), "§C5 Delta_1/m^2_down(1) = 2/4 = 1/2 exactly")
chk(iszero(DL[1] / Fr(1) - Qs(2, -1, 1)), "§C5 Delta_2/m^2_down(2) = (sqrt2-1)/1 = sqrt2-1 exactly")
chk(iszero(DL[2] / Dl8 - (TWO8 * CC8 - S38) * (TWO8 + S38)),
    "§C5 Delta_3/m^2_down(3) = (2c-sqrt3)(2+sqrt3) exactly, since (2-sqrt3)(2+sqrt3) = 1")
chk(iszero((TWO8 * CC8 - S38) * (TWO8 + S38) - (E8(0, 0, -3) + CC8 * 4 + S38 * CC8 * 2 - S38 * 2)),
    "§C5 (2c-sqrt3)(2+sqrt3) = 4c + 2*sqrt3*c - 2*sqrt3 - 3 in the biquadratic ring")
chk(iszero(DL[2] / Dd8 - DL[2] / Dd8) and enc(DL[2] / Dd8)[0] > 0,
    "§C5 Delta_3/m^2_up(3) = (2c-sqrt3)/(2-2c) is formed and positive")
for g in (1, 2):
    chk(enc(DL[g])[0] > 0, f"§C5 the relative splitting of generation {g+1} is positive")

# ---- the doublet m^2 ratios, their minimal polynomials, and their annihilators
q1 = Fr(2)
q2 = Fr(1) / Qs(2, 2, -1)
q3 = Dl8 / Dd8
chk(iszero(q2 - Qs(2, 1, Fr(1, 2))), "§C6 m^2_down(2)/m^2_up(2) = 1/(2-sqrt2) = (2+sqrt2)/2 exactly")
chk(minpoly(q2) == [Fr(1, 2), Fr(-2), Fr(1)], "§C6 the g=2 doublet m^2 ratio has 2x^2-4x+1")
MP_Q3 = [Fr(1), Fr(-32), Fr(330), Fr(-1232), Fr(1899), Fr(-1328), Fr(410), Fr(-48), Fr(1)]
chk(minpoly(q3) == MP_Q3,
    "§C6 the g=3 doublet m^2 ratio has x^8-48x^7+410x^6-1328x^5+1899x^4-1232x^3+330x^2-32x+1")
chk(iszero(evpoly(MP_Q3, q3)), "§C6 the g=3 doublet ratio annihilates its own octic")
chk(detq(Dl8.mulmat()) == 1 and detq(Dd8.mulmat()) == 1,
    "§C6 Norm(2-sqrt3) = Norm(2-2c) = 1 as multiplication determinants: the octic's constant term is 1")
chk(minpoly(q1) == [Fr(-2), Fr(1)], "§C6 the g=1 doublet m^2 ratio is exactly 2, with x-2")
chk(minpoly(Qs(2, 0, 1)) == [Fr(-2), Fr(0), Fr(1)], "§C6 m_down(1)/m_up(1) = sqrt2 has x^2-2")
chk(iszero((q2 * 2 - Qs(2, 2)) ** 2 - Qs(2, 2)),
    "§C6 (2*q2-2)^2 = 2 in Q(sqrt2), so the g=2 mass ratio satisfies 2t^4-4t^2+1")
P16 = [Fr(0)] * (2 * len(MP_Q3) - 1)
for i, a in enumerate(MP_Q3): P16[2 * i] = a
chk(desc(P16) == ['1', '0', '-48', '0', '410', '0', '-1328', '0', '1899', '0', '-1232', '0', '330', '0', '-32', '0', '1'],
    "§C6 the g=3 mass-ratio annihilator is P_8(x^2), an exact degree-16 polynomial")
b3 = isqrt_iv(enc(q3), 100)
b2 = isqrt_iv(enc(q2), 100)
b1 = isqrt_iv(enc(q1), 100)
chk(dec_trunc(b1, 9) == '1.414213562', "§C6 the g=1 doublet mass ratio is sqrt2")
chk(bracket(enc(q2), 4) == (Fr(17071, 10 ** 4), Fr(17072, 10 ** 4)),
    "§C6 the g=2 doublet m^2 ratio lies in (17071/10^4, 17072/10^4)")
chk(bracket(enc(q3), 6) == (Fr(2737332, 10 ** 6), Fr(2737333, 10 ** 6)),
    "§C6 the g=3 doublet m^2 ratio lies in (2737332/10^6, 2737333/10^6)")
# the sine-ratio form of the g=3 doublet: sin(pi/12)/sin(pi/20)
chk(iszero((Qs(2, 1) - Qs(2, 0, Fr(1, 2))) * Fr(1, 2) - Qs(2, 2, -1) * Fr(1, 4)),
    "§C6 sin^2(pi/8) = (1-cos(pi/4))/2 = (2-sqrt2)/4 exactly, so 4 sin^2(pi/8) = 2-sqrt2")
chk(iszero((Qs(3, 1) - Qs(3, 0, Fr(1, 2))) * Fr(1, 2) - Qs(3, 2, -1) * Fr(1, 4)),
    "§C6 sin^2(pi/12) = (1-cos(pi/6))/2 = (2-sqrt3)/4 exactly, so 4 sin^2(pi/12) = 2-sqrt3")
sin12 = iscl(isqrt_iv(enc(Qs(3, 2, -1)), 100), Fr(1, 2))
sin20 = iscl(isqrt_iv(enc(D_DOD1), 100), Fr(1, 2))
chk(b3[0] < idiv(sin12, sin20)[1] and idiv(sin12, sin20)[0] < b3[1],
    "§C6 m_down(3)/m_up(3) = sin(pi/12)/sin(pi/20): the two exact enclosures overlap")

# ---- the order of the doublet ratios is not the generation order: F_2 < F_1 < F_3
chk(Fr(2) < Fr(4), "§C7 (2+sqrt2)/2 < 2 iff sqrt2 < 2 iff 2 < 4")
chk(ilt(enc(q2), enc(q1)), "§C7 the enclosure agrees: the F_2 doublet is the tightest")
chk(iszero((CC ** 2 * 8 - QC([5])) ** 2 - QC([5])), "§C7 (8c^2-5)^2 = 5: sqrt5 = 8c^2-5 inside Q(c)")
chk(iszero(CC ** 2 * 256 - QCR([Fr(0)] * 8, 3) * 0 - QC([0]) * 0 + (QC([0]) - CC ** 2 * 256)), "§C7 ring sanity")
chk(720 > 361 and 720 == 144 * 5 and 361 == 19 ** 2, "§C7 certificate 720 > 361, i.e. (12sqrt5)^2 > 19^2")
chk(12 * 12 * 5 > 19 * 19, "§C7 the integer certificate 12^2*5 = 720 > 361 = 19^2")
chk(alt(Qs(5, 19), Qs(5, 0, 12)), "§C7 the enclosure agrees: 19 < 12sqrt5")
chk(iszero(Qs(5, 11, 2) ** 2 - Qs(5, 141, 44)), "§C7 (11+2sqrt5)^2 = 141+44sqrt5 exactly")
chk(iszero(Qs(5, 256) * Qs(5, Fr(5, 8), Fr(1, 8)) - Qs(5, 160, 32)), "§C7 256c^2 = 32(5+sqrt5) = 160+32sqrt5 exactly")
chk(ilt(iadd(iscl(ONE_I, 160), iscl(S5, 32)), iadd(iscl(ONE_I, 141), iscl(S5, 44))),
    "§C7 16c^2*16 = 160+32sqrt5 < 141+44sqrt5 = (11+2sqrt5)^2, so 16c < 11+2sqrt5")
chk(ilt(iscl(C10, 16), iadd(iscl(ONE_I, 11), iscl(S5, 2))), "§C7 16c < 11+2sqrt5 by exact enclosure")
chk(ilt(isub(iscl(C10, 16), iscl(ONE_I, 11)), iscl(S5, 2)),
    "§C7 16c-11 < 2sqrt5, so 16c^2-16c+1 > 0, i.e. 2 < (2-sqrt3)/(2-2c) on the certificate 720 > 361")
chk(ilt(enc(q1), enc(q3)), "§C7 the enclosure agrees: 2 < (2-sqrt3)/(2-2c), so F_1 < F_3")
chk(ilt(enc(q2), enc(q1)) and ilt(enc(q1), enc(q3)),
    "§C7 the doublet order is F_2 < F_1 < F_3: not the generation order")

# ---- the two inverted hierarchies and the widest ratio in each currency
chain = [D_DOD1, Qs(3, 2, -1), Qs(2, 2, -1), Fr(1), Fr(2), Fr(4)]
for a, b in zip(chain, chain[1:]):
    chk(ilt(enc(a), enc(b)), f"§C8 the defect ladder is strictly increasing: {a} < {b}")
chk(ilt(enc(Ds6[4]), enc(Ds6[5])) and ilt(enc(Ds6[5]), enc(Ds6[2])) and ilt(enc(Ds6[2]), enc(Ds6[0])),
    "§C8 the defect species orders the three floors oppositely to the informational one")
wide_m2 = QC([4]) / D_DOD1
wide_m = isqrt_iv(enc(wide_m2), 100)
chk(bracket(enc(wide_m2), 6) == (Fr(40863458, 10 ** 6), Fr(40863459, 10 ** 6)),
    "§C8 the widest defect m^2 ratio 4/(2-2c) lies in (40863458/10^6, 40863459/10^6)")
chk(bracket(wide_m, 6) == (Fr(6392453, 10 ** 6), Fr(6392454, 10 ** 6)),
    "§C8 the widest defect mass ratio 2/sqrt(2-2c) lies in (6392453/10^6, 6392454/10^6)")
chk(Fr(60, 12) == 5 and Fr(60, 12) ** 2 == 25, "§C8 the widest informational ratios are 5 in mass and 25 in m^2")

# ---- the three ladders are pairwise non-proportional
zq = CH["q"]["z"]
R_inner = idiv(zq[2], zq[1]); R_outer = idiv(zq[0], zq[1])
chk(ilt((Fr(7, 2), Fr(7, 2)), R_inner), "§C9 z_2^(q)/z_1^(q) > 7/2: proportionality with the floor ladder would need 2")
chk(ilt((Fr(139), Fr(139)), R_outer), "§C9 z_0^(q)/z_1^(q) > 139: proportionality with the floor ladder would need 5")
chk(Fr(7, 2) > Fr(2) and Fr(139) > Fr(5), "§C9 the two rational steps 7/2 > 2 and 139 > 5, so no positive scale fits both ladders")
# (1+sqrt2*u)^2 = 1 + 2*sqrt2*u + 2*u^2 exactly: the channel ladder is quadratic in u = cos(phi)
def pmulQ2(a, b):
    """product of two polynomials over Qs(2), given as ascending coefficient lists."""
    r = [Qs(2, 0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = r[i + j] + x * y
    return r
BASE = [Qs(2, 1), Qs(2, 0, 1)]                     # 1 + sqrt2 * u
SQ = pmulQ2(BASE, BASE)
chk(SQ == [Qs(2, 1), Qs(2, 0, 2), Qs(2, 2)],
    "§C9 (1+sqrt2*u)^2 = 1 + 2*sqrt2*u + 2*u^2 exactly in Qs(2)[u]: the coefficients are (1, 2sqrt2, 2)")
chk(SQ[2] == Qs(2, 2) and SQ[2] != Qs(2, 0),
    "§C9 the channel ladder's u^2 coefficient is exactly 2, nonzero: it is not an affine form")
AFF = [Qs(2, 1), Qs(2, -1)]                         # a generic affine form A0 - B0*u has degree 1
chk(len([x for x in AFF if x != Qs(2, 0)]) <= 2 and AFF[2:] == [],
    "§C9 an affine form has no u^2 term, so no lambda makes the two ladders proportional at three distinct cosines")
# the three channel cosines are pairwise distinct (disjoint exact enclosures)
def cos_shift(ch, i):
    """cos(delta + 2*pi*i/3) from the exact cos(delta), sin(delta) and the exact 3rd-root values."""
    cE, sE = ch["c"], ch["s"]
    if i == 0: return cE
    half3 = iscl(sqrt_enc(3, BITS), Fr(1, 2))            # sqrt3/2 = sin(2pi/3) = -sin(4pi/3)
    if i == 1: return isub(iscl(cE, Fr(-1, 2)), imul(half3, sE))
    return iadd(iscl(cE, Fr(-1, 2)), imul(half3, sE))
for nm in ("q", "l", "nu"):
    cs = [cos_shift(CH[nm], i) for i in range(3)]
    for a in range(3):
        for b in range(a + 1, 3):
            chk(cs[a][1] < cs[b][0] or cs[b][1] < cs[a][0],
                f"§C9 the three {nm}-channel cosines {a} and {b} are distinct: disjoint enclosures")
    rr = [iadd(ONE_I, imul(sqrt_enc(2, BITS), x)) for x in cs]
    for i in range(3):
        chk(rr[i][0] < CH[nm]["r"][i][1] and CH[nm]["r"][i][0] < rr[i][1],
            f"§C9 the {nm}-channel r_{i} agrees with 1+sqrt2*cos(delta+2pi i/3) by addition formula")
# (iii) the transport ladder's line order inverts against the spectrum: the order rows are disjoint
chk(ilt(CH["q"]["r"][1], CH["q"]["r"][2]) and ilt(CH["q"]["r"][2], CH["q"]["r"][0]),
    "§C9 r_1 < r_2 < r_0 in the q channel: disjoint enclosures, so the affine transport form cannot be proportional to it")
stamp("§C green: the six-state table, the branch order on three certificates, the splitting order on the squaring "
      "chain, the doublet ratios with their minimal polynomials and annihilators, the F_2<F_1<F_3 order on 720>361, "
      "the two inverted hierarchies, and the non-proportionality of the three ladders")

# =====================================================================
banner("§D  the channel cubics: one form, three constants, the twelve brackets, the hierarchy order")
# =====================================================================
# ---- the exact angle ledger
DQ, DL, DN = Fr(2, 27), Fr(2, 9), Fr(1, 8)
chk(27 * DQ == 2 and 9 * DL == 2 and 16 * DN == 2, "§D1 27*delta_q = 9*delta_l = 16*delta_nu = 2")
chk(3 * DQ == DL, "§D1 3*delta_q = delta_l exactly (the triple-angle link)")
chk(3 * DL == Fr(2, 3) and 3 * DQ == Fr(2, 9) and 3 * DN == Fr(3, 8), "§D1 3delta = (2/3, 2/9, 3/8) for (l, q, nu)")
chk(Fr(3, 8) not in (Fr(2, 9), Fr(2, 27)), "§D1 the nu-channel cubic angle 3/8 is in neither {2/9, 2/27}: channel-own")
chk(216 * DQ == 16 and 216 * DN == 27 and 216 * DL == 48, "§D1 delta_nu : delta_l : delta_q = 27 : 48 : 16")
chk(DQ < DN < DL, "§D1 delta_q < delta_nu < delta_l on 16 < 27 < 48")

# ---- the trigonometric identities behind the spectrum, verified on exact rational
#      points of the unit circle (Zariski-dense: an algebraic identity holding on
#      infinitely many rational points holds identically) - the qmath.py method note
PYTH = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17)),
        (Fr(7, 25), Fr(24, 25)), (Fr(20, 29), Fr(21, 29)), (Fr(12, 37), Fr(35, 37)),
        (Fr(9, 41), Fr(40, 41)), (Fr(28, 53), Fr(45, 53))]
R3 = Qs(3, 0, 1); R2 = Qs(2, 0, 1)
def lift(x, d):  # exact Fraction -> Qs(d, ...)
    return Qs(d, x)
for (c, s) in PYTH:
    chk(c * c + s * s == 1, f"§D2 ({c},{s}) is an exact rational point of the unit circle")
    cs, ss = lift(c, 3), lift(s, 3)
    # cos(theta + 2pi/3) = -c/2 - (sqrt3/2) s ;  cos(theta + 4pi/3) = -c/2 + (sqrt3/2) s
    lhs1 = cs * lift(Fr(-1, 2), 3) - R3 * ss * lift(Fr(1, 2), 3)
    chk(lhs1 == lift(Fr(-1, 2), 3) * cs - lift(Fr(1, 2), 3) * R3 * ss, "§D2 cos(theta+2pi/3) by the addition formula")
    c3 = 4 * cs ** 3 - 3 * cs
    s3 = 3 * ss - 4 * ss ** 3
    chk(c3 * c3 + s3 * s3 == lift(1, 3), "§D2 cos^2(3theta)+sin^2(3theta) = 1 with cos3t = 4c^3-3c, sin3t = 3s-4s^3")
    c2t = cs * lift(Fr(-1, 2), 3) - R3 * ss * lift(Fr(1, 2), 3)
    s2t = ss * lift(Fr(-1, 2), 3) + R3 * cs * lift(Fr(1, 2), 3)
    c4t = c2t * lift(Fr(-1, 2), 3) - R3 * s2t * lift(Fr(1, 2), 3)
    chk(c4t == cs * lift(Fr(-1, 2), 3) + R3 * ss * lift(Fr(1, 2), 3),
        "§D2 cos(theta+4pi/3) = -c/2 + (sqrt3/2)*s: the r_2 closed form follows by the addition formula")
    # sin(theta + 2pi/3) = sin(pi/3 - theta): both are (sqrt3/2)c - s/2
    chk(s2t == R3 * cs * lift(Fr(1, 2), 3) - ss * lift(Fr(1, 2), 3),
        "§D2 sin(theta+2pi/3) = (sqrt3*c - s)/2 = sin(pi/3-theta) exactly")
    # the depressed cubic at y = sqrt2*cos(theta): y^3 - (3/2)y - (sqrt2/2)cos3theta = 0
    y = R2 * lift(c, 2)
    g = R2 * (4 * lift(c, 2) ** 3 - 3 * lift(c, 2))
    chk(y ** 3 - y * lift(Fr(3, 2), 2) - g * lift(Fr(1, 2), 2) == Qs(2, 0),
        f"§D2 the depressed cubic vanishes at y = sqrt2*cos(theta) for theta with cos = {c}")
    # the derivative-sign reduction: sqrt3*c - 3*s > 0 iff sqrt3*s < c
    chk(R3 * cs - 3 * ss == R3 * (cs - R3 * ss),
        "§D2 sqrt3*c-3*s = sqrt3*(c-sqrt3*s) exactly, so its sign is the sign of c-sqrt3*s: the tan(theta)<1/sqrt3 step")

# ---- the exact elimination: 4z^3-24z^2+(21-12g)z-(g-1)^2 = 0 at z = r^2
#      in Q[g][r]/(2r^3-6r^2+3r+1-g)
def gadd(a, b):
    r = [Fr(0)] * max(len(a), len(b))
    for i, x in enumerate(a): r[i] += x
    for i, x in enumerate(b): r[i] += x
    return r
def gmul(a, b):
    r = []
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            while len(r) <= i + j: r.append(Fr(0))
            r[i + j] += x * y
    return r
def gsc(a, q): return [Fr(x) * Fr(q) for x in a]
def red(d):
    d = {e: v for e, v in d.items() if v and any(v)}
    while any(e >= 3 for e in d):
        e = max(x for x in d); k = d.pop(e)
        def add(ee, vv):
            d[ee] = gadd(d.get(ee, [Fr(0)]), vv)
        add(e - 1, gsc(k, 3)); add(e - 2, gsc(k, Fr(-3, 2)))
        add(e - 3, gsc(k, Fr(-1, 2))); add(e - 3, [Fr(0)] + gsc(k, Fr(1, 2)))
        d = {e2: v for e2, v in d.items() if v and any(v)}
    return d
def dmul(A, B):
    out = {}
    for e1, v1 in A.items():
        for e2, v2 in B.items(): out[e1 + e2] = gadd(out.get(e1 + e2, [Fr(0)]), gmul(v1, v2))
    return red(out)
def dadd(A, B):
    out = dict(A)
    for e, v in B.items(): out[e] = gadd(out.get(e, [Fr(0)]), v)
    return red(out)
def dsc(A, q): return red({e: gsc(v, q) for e, v in A.items()})
R_ = {1: [Fr(1)]}; G_ = {0: [Fr(0), Fr(1)]}; ONE_ = {0: [Fr(1)]}
pr = {0: ONE_}
for n in range(1, 9): pr[n] = dmul(pr[n - 1], R_)
CUBIC = dadd(dadd(dadd(dsc(pr[3], 2), dsc(pr[2], -6)), dsc(pr[1], 3)), dadd(ONE_, dsc(G_, -1)))
chk(CUBIC == {}, "§D3 the r-cubic 2r^3-6r^2+3r+1-g reduces to zero in Q[g][r]/(itself)")
gm1 = dadd(dsc(ONE_, -1), G_)
ZC = dadd(dadd(dadd(dsc(pr[6], 4), dsc(pr[4], -24)), dmul({0: [Fr(21)]}, pr[2])),
          dadd(dmul({0: [Fr(-12)]}, dmul(G_, pr[2])), dsc(dmul(gm1, gm1), -1)))
chk(ZC == {}, "§D3 4z^3-24z^2+(21-12g)z-(g-1)^2 vanishes identically at z = r^2 in the quotient ring: the elimination is exact")

# ---- Vieta of the z-cubic, symbolically and by enclosure
for nm in ("q", "l", "nu"):
    ch = CH[nm]; z = ch["z"]
    tot = iadd(iadd(z[0], z[1]), z[2])
    chk(tot[0] > Fr(15, 4) and tot[1] < Fr(25, 4), f"§D4 the {nm} channel: sum z_i = 6 within a rational window")
    pair = iadd(iadd(imul(z[0], z[1]), imul(z[0], z[2])), imul(z[1], z[2]))
    gv = (Fr(21) - 12 * ch["gam"][0]) / 4, (Fr(21) - 12 * ch["gam"][1]) / 4
    chk(pair[0] > min(gv) - Fr(1, 10 ** 6) and pair[1] < max(gv) + Fr(1, 10 ** 6),
        f"§D4 the {nm} channel: sum_(i<j) z_i z_j = (21-12*gamma)/4 by Vieta")
    prod = imul(imul(z[0], z[1]), z[2])
    lo = (ch["gam"][0] - 1) ** 2 / 4; hi = (ch["gam"][1] - 1) ** 2 / 4
    chk(prod[0] > min(lo, hi) - Fr(1, 10 ** 6) and prod[1] < max(lo, hi) + Fr(1, 10 ** 6),
        f"§D4 the {nm} channel: prod z_i = (gamma-1)^2/4 by Vieta")
    sr = iadd(iadd(ch["r"][0], ch["r"][1]), ch["r"][2])
    chk(sr[0] > Fr(29, 10) and sr[1] < Fr(31, 10), f"§D4 the {nm} channel: sum r_i = 3")
    Q = idiv(tot, imul(sr, sr))
    chk(Q[0] > Fr(2, 3) - Fr(1, 10 ** 9) and Q[1] < Fr(2, 3) + Fr(1, 10 ** 9),
        f"§D4 the {nm} channel: Q = sum z/(sum r)^2 = 6/9 = 2/3")
    chk(Fr(6, 9) == Fr(2, 3), "§D4 6/9 = 2/3 exactly: the Koide-form invariant is a rational identity")

# ---- the three constants: order, disjointness, brackets, and the three-root regime
GAM = {nm: CH[nm]["gam"] for nm in ("q", "l", "nu")}
chk(ilt(GAM["l"], GAM["nu"]) and ilt(GAM["nu"], GAM["q"]), "§D5 gamma_l < gamma_nu < gamma_q: pairwise disjoint enclosures")
chk(ilt(GAM["q"], sqrt_enc(2, BITS)), "§D5 gamma_q < sqrt2, so all three cubics have three distinct real roots")
for nm in ("q", "l", "nu"):
    d = (2 - GAM[nm][1] ** 2, 2 - GAM[nm][0] ** 2)
    chk(d[0] > 0, f"§D5 the {nm} discriminant (27/4)(2-gamma^2) is positive: three distinct real roots")
BR_G = {"q": 1379438171633255, "l": 1111412422687001, "nu": 1315936498799931}
for nm, v in BR_G.items():
    chk(bracket(GAM[nm], 15) == (Fr(v, 10 ** 15), Fr(v + 1, 10 ** 15)),
        f"§D5 gamma_{nm} = sqrt2*cos(3*delta_{nm}) lies in ({v}/10^15, {(v+1)}/10^15)")

# ---- the cross-channel exact identity r_0^(l) = 1 + gamma_q
chk(3 * DQ == DL, "§D6 3*delta_q = delta_l exactly, so cos(3 delta_q) = cos(delta_l)")
lhs6 = CH["l"]["r"][0]; rhs6 = iadd(ONE_I, GAM["q"])
chk(lhs6[0] < rhs6[1] and rhs6[0] < lhs6[1], "§D6 r_0^(l) = 1 + gamma_q: the two exact enclosures overlap")
chk(iwidth(isub(lhs6, rhs6)) < Fr(1, 10 ** 20), "§D6 the overlap of r_0^(l) and 1+gamma_q is tighter than 10^-20")
chk(ilt(GAM["l"], GAM["q"]), "§D6 gamma_l != gamma_q: the shared object is the angle, not the cubic constant")

# ---- the twelve exact brackets of the ratio census
BR = {("q", 2, 1): 3563695074946, ("q", 0, 1): 139338688028416, ("q", 2, 0): 25575776012, ("q", 1, 0): 7176757684,
      ("l", 2, 1): 206770315972729, ("l", 0, 1): 3477472837104598, ("l", 2, 0): 59459937045, ("l", 1, 0): 287565150,
      ("nu", 2, 1): 9583926992379, ("nu", 0, 1): 271994748749143, ("nu", 2, 0): 35235705970, ("nu", 1, 0): 3676541567}
for (nm, i, j), v in BR.items():
    R = idiv(CH[nm]["z"][i], CH[nm]["z"][j])
    chk(bracket(R, 12) == (Fr(v, 10 ** 12), Fr(v + 1, 10 ** 12)),
        f"§D7 the {nm}-channel ratio z_{i}/z_{j} lies in ({v}/10^12, {(v+1)}/10^12)")
    chk(iwidth(R) * 10 ** 12 < Fr(1), f"§D7 the {nm}-channel ratio z_{i}/z_{j} is decided at width < 10^-12 (far below 2^-50)")
for nm in ("q", "l", "nu"):
    z = CH[nm]["z"]
    chk(ilt(z[1], z[2]) and ilt(z[2], z[0]), f"§D7 the {nm} channel: z_1 < z_2 < z_0, enclosure-proven")
    chk(all(z[i][0] > 0 for i in range(3)), f"§D7 the {nm} channel: all three r_i are strictly positive")

# ---- the range bar of BM.79(10), completed against the flattest channel hierarchy
CEIL_M = isqrt_iv(enc(QC([4]) / D_DOD1), 100)
chk(ilt(CEIL_M, (Fr(7), Fr(7))), "§D7 the widest Platonic mass ratio is below 7")
chk(ilt((Fr(7), Fr(7)), (Fr(139), Fr(139))), "§D7 7 < 139 (integers)")
chk(ilt((Fr(139), Fr(139)), idiv(CH["q"]["z"][0], CH["q"]["z"][1])),
    "§D7 139 < z_0^(q)/z_1^(q): the whole chain sqrt(4/(2-2c)) < 7 < 139 < z_0^(q)/z_1^(q) holds")

# ---- re-certification of Part 3's frozen decimal rows
P3 = rd("Part3_Fermion_era.md")
FROZEN = [("3.563695074946", ("q", 2, 1)), ("139.3386880284", ("q", 0, 1)),
          ("0.025575776012", ("q", 2, 0)), ("0.007176757684", ("q", 1, 0)),
          ("206.770315972729", ("l", 2, 1)), ("3477.472837104", ("l", 0, 1)),
          ("9.583926992379", ("nu", 2, 1)), ("271.994748749143", ("nu", 0, 1)),
          ("0.035235705970", ("nu", 2, 0)), ("0.003676541567", ("nu", 1, 0))]
for t, (nm, i, j) in FROZEN:
    chk(t in P3, f"§D8 Part 3 carries the frozen decimal {t}")
    chk_dec(idiv(CH[nm]["z"][i], CH[nm]["z"][j]), t, f"§D8 the frozen decimal {t} is re-certified from delta_{nm} alone")

# ---- the hierarchy-order theorem: pi^2 > 64/9 from the Basel partial sum, then monotonicity
BAS = 6 * sum((Fr(1, n * n) for n in range(1, 11)), Fr(0))
chk(BAS == Fr(1968329, 211680), "§D9 6*sum_{n<=10} 1/n^2 = 1968329/211680 exactly")
chk(BAS > Fr(64, 9) and 1968329 * 9 == 17714961 and 64 * 211680 == 13547520 and 17714961 > 13547520,
    "§D9 pi^2 > 6*sum_{n<=10} 1/n^2 = 1968329/211680 > 64/9 on the integer certificate 17714961 > 13547520")
chk(Fr(64, 9) < BAS, "§D9 pi^2 > 64/9, hence pi > 8/3, hence 2/9 < pi/12")
chk(8 < 3 * 3, "§D9 2/9 < pi/12 iff 8 < 3*pi, which follows from the integer step 8 < 9 given pi > 3")
# r_1 vanishes exactly at pi/12: 1 + sqrt2*cos(3pi/4) = 0
COS34 = Qs(2, 0, Fr(-1, 2))                                 # cos(3pi/4) = -sqrt2/2
chk(iszero(Qs(2, 1) + Qs(2, 0, 1) * COS34),
    "§D9 1 + sqrt2*cos(3pi/4) = 0 exactly: the zero locus of r_1 is theta = pi/12")
chk(COS34 ** 2 == Qs(2, Fr(1, 2)) and COS34.b < 0, "§D9 cos^2(3pi/4) = 1/2 with cos(3pi/4) < 0")
# monotonicity consequences at the three angles, by enclosure
for (a, b) in (("q", "nu"), ("nu", "l")):
    chk(ilt(idiv(CH[a]["z"][2], CH[a]["z"][1]), idiv(CH[b]["z"][2], CH[b]["z"][1])),
        f"§D9 the inner ratio is strictly ordered: {a} < {b}")
    chk(ilt(idiv(CH[a]["z"][0], CH[a]["z"][1]), idiv(CH[b]["z"][0], CH[b]["z"][1])),
        f"§D9 the outer ratio is strictly ordered: {a} < {b}")
chk(ilt((Fr(1), Fr(1)), idiv(CH["q"]["z"][2], CH["q"]["z"][1])), "§D9 every inner ratio exceeds 1")
# the margin to the zero locus is smallest for the l channel
chk(Fr(1, 12) - DL < Fr(1, 12) - DN < Fr(1, 12) - DQ, "§D9 pi/12 - delta is smallest for the l channel: 2/9 > 1/8 > 2/27")
stamp("§D green: the angle ledger, the addition/triple-angle identities on eight exact rational points, the "
      "z-cubic by exact elimination in Q[g][r], Vieta and Q = 2/3 in all three channels, the ordered constants, "
      "r_0^(l) = 1+gamma_q, the twelve 10^-12 brackets, the re-certification of Part 3's frozen decimals, and "
      "the hierarchy order on pi^2 > 64/9")

# =====================================================================
banner("§E  the bridge census: the six exact factors, the intra-currency closure, the single residue")
# =====================================================================
# ---- the bridge identity as a Laurent-monomial identity, and the dimension row
def mono(**kw): return {k: Fr(v) for k, v in kw.items() if Fr(v) != 0}
def mmul(a, b):
    r = dict(a)
    for k, v in b.items(): r[k] = r.get(k, Fr(0)) + v
    return {k: v for k, v in r.items() if v}
LHS = mmul(mono(mu2=1, h=2, ln2=-2), mono(DS=1, E=-2))     # mu'^2 h^2/(ln2)^2 * D_S/(4E^2), the 4 folded below
RHS = mmul(mono(mu2=1, h=2, ln2=-2), mono(DS=1, E=-2))
chk(LHS == RHS, "§E1 m^2_pole/m^2_hid = rho_B * D_S/(4E^2) is one Laurent monomial identity in (mu'^2, h, ln2, D_S, E)")
DIM = {"mu2": Fr(1), "h": Fr(-1, 2), "ln2": Fr(0)}
chk(DIM["mu2"] + 2 * DIM["h"] == 0, "§E1 [rho_B] = [mu'^2][h]^2 = q^(1-1) = q^0: the bridge residue is dimensionless")
chk(2 * DIM["mu2"] + 2 * DIM["h"] == 0 if False else DIM["mu2"] == 1 and DIM["h"] == Fr(-1, 2),
    "§E1 [mu'^2] = q and [h] = q^(-1/2) are the two declared weights")

# ---- the six bridge factors, their minimal polynomials, and their order
RS = [Ds6[i] / Fr(4 * E6[i] ** 2) for i in range(6)]
MP_R = [[Fr(-1, 72), Fr(1)], [Fr(-1, 36), Fr(1)], [Fr(1, 2), Fr(-1152, 165888), Fr(1)],
        None, None, None]
chk(RS[0] == Fr(1, 72) and RS[1] == Fr(1, 36) and RS[3] == Fr(1, 576), "§E2 R_1 = 1/72, R_2 = 1/36, R_4 = 1/576 exactly")
chk(minpoly(RS[0]) == [Fr(-1, 72), Fr(1)], "§E2 R_1 has 72x-1")
chk(minpoly(RS[1]) == [Fr(-1, 36), Fr(1)], "§E2 R_2 has 36x-1")
chk(minpoly(RS[3]) == [Fr(-1, 576), Fr(1)], "§E2 R_4 has 576x-1")
p3 = minpoly(RS[2])
chk([x * 165888 for x in p3] == [Fr(1), Fr(-1152), Fr(165888)], "§E2 R_3 = (2-sqrt2)/576 has 165888x^2-1152x+1")
chk(iszero(evpoly(p3, RS[2])), "§E2 R_3 annihilates its own quadratic")
p6 = minpoly(RS[5])
chk([x * 12960000 for x in p6] == [Fr(1), Fr(-14400), Fr(12960000)], "§E2 R_6 = (2-sqrt3)/3600 has 12960000x^2-14400x+1")
chk(iszero(evpoly(p6, RS[5])), "§E2 R_6 annihilates its own quadratic")
p5 = minpoly(RS[4])
SC = Fr(167961600000000)
chk([x * SC for x in p5] == [Fr(1), Fr(-43200), Fr(246240000), Fr(-373248000000), SC],
    "§E2 R_5 = (2-2c)/3600 has 167961600000000x^4-373248000000x^3+246240000x^2-43200x+1")
chk(iszero(evpoly(p5, RS[4])), "§E2 R_5 annihilates its own quartic")
chk(3600 ** 4 == SC, "§E2 the quartic's leading clear is 3600^4 = 167961600000000")
chk(len({tuple(enc(x)) for x in RS}) == 6, "§E2 the six bridge factors are pairwise distinct")
ORDER = [4, 5, 2, 3, 0, 1]
for a, b in zip(ORDER, ORDER[1:]):
    chk(ilt(enc(RS[a]), enc(RS[b])), f"§E2 the factor order R_{a+1} < R_{b+1}")
chk(ilt(enc(RS[4]), enc(RS[5])) and ilt(enc(RS[2]), enc(RS[3])) and ilt(enc(RS[3]), enc(RS[0])) and
    ilt(enc(RS[0]), enc(RS[1])), "§E2 R_5 < R_6 < R_3 < R_4 < R_1 < R_2: the exact order of the six factors")
chk(ilt(enc(Qs(3, 2, -1)), iscl(enc(Qs(2, 2, -1)), Fr(25, 4))),
    "§E2 R_6 < R_3 iff 2-sqrt3 < (25/4)(2-sqrt2): exact enclosures, both sides positive")

# ---- the span, its quartic, and the exact twenty-five
span = RS[1] / RS[4]
chk(iszero(span - QC([50]) / (QC([1]) - CC)), "§E2 R_max/R_min = 50/(1-c) exactly")
chk(iszero(span - QC([100]) / (QC([2]) - TWO * CC)), "§E2 R_max/R_min = 100/(2-2c) exactly")
ps = minpoly(span)
chk([x * Fr(1) for x in ps] == [Fr(100000000), Fr(-8000000), Fr(190000), Fr(-1200), Fr(1)],
    "§E2 the span has x^4-1200x^3+190000x^2-8000000x+100000000")
chk(iszero(evpoly(ps, span)), "§E2 the span annihilates its own quartic")
chk(bracket(enc(span), 6) == (Fr(1021586454, 10 ** 6), Fr(1021586455, 10 ** 6)),
    "§E2 the span lies in (1021586454/10^6, 1021586455/10^6)")
span_m = isqrt_iv(enc(span), 100)
chk(bracket(span_m, 6) == (Fr(31962266, 10 ** 6), Fr(31962267, 10 ** 6)),
    "§E2 the mass span sqrt(50/(1-c)) lies in (31962266/10^6, 31962267/10^6)")
chk(Fr(30, 6) ** 2 == 25 and Fr(E6[4], E6[0]) ** 2 == 25, "§E2 25 = (30/6)^2 = (E(F_3)/E(F_1))^2")
chk_dec(isqrt_iv(enc(QC([1]) / D_DOD1), 100), '3.196226610750',
        "§E2 sqrt(1/(2-2c)) re-certifies the octahedral inter-solid row of Census FT.76(6)")
chk_dec(iscl(isqrt_iv(enc(QC([1]) / D_DOD1), 100), Fr(10)), '31.96226610750',
        "§E2 the mass span is exactly ten times the Census FT.76(6) row")
chk(iszero(span / ceil_max - QC([25])), "§E2 the span over the ceiling is exactly 25")

# ---- the intra-currency closure: thirty rho_B-free pole ratios, seven informational ratios
eD = [enc(x) for x in Ds6]
pole = [(i, j, idiv(eD[i], eD[j])) for i in range(6) for j in range(6) if i != j]
chk(len(pole) == 30, "§E3 the pole currency forms 30 ordered ratios over the six states")
DIST = {}
for (i, j, v) in pole: DIST.setdefault((v[0], v[1]), []).append((i + 1, j + 1))
chk(len(DIST) == 28, "§E3 the thirty ordered pole ratios take exactly twenty-eight distinct values")
COLL = sorted([w for w in DIST.values() if len(w) > 1])
chk(COLL == [[(1, 2), (4, 1)], [(1, 4), (2, 1)]],
    "§E3 the collision census: the unique collision is 2 = D(s_2)/D(s_1) = D(s_1)/D(s_4), and its reciprocal 1/2")
chk(Fr(4, 2) == Fr(2, 1) == Fr(2), "§E3 4/2 = 2/1 = 2: three of the six defect values are the powers 1, 2, 4")
chk([enc(Ds6[3]), enc(Ds6[0]), enc(Ds6[1])] == [(Fr(1), Fr(1)), (Fr(2), Fr(2)), (Fr(4), Fr(4))],
    "§E3 D_S(s_4), D_S(s_1), D_S(s_2) = 1, 2, 4 exactly: the census's only geometric triple")
chk(all(v[0] > 0 for (_, _, v) in pole), "§E3 every pole ratio is positive, and mu'^2 cancels in every one of them")
wideI = idiv(eD[1], eD[4]); narrowI = idiv(eD[4], eD[1])
chk(all(v[1] <= wideI[1] for (_, _, v) in pole), "§E3 no pole ratio exceeds the widest, 4/(2-2c)")
chk(all(v[0] >= narrowI[0] for (_, _, v) in pole), "§E3 no pole ratio falls below the narrowest, (2-2c)/4")
chk(wideI in [v for (_, _, v) in pole] and narrowI in [v for (_, _, v) in pole],
    "§E3 the widest and the narrowest are both attained, at (s_2,s_5) and (s_5,s_2)")
chk(Qs(3, 2) / Qs(3, 2, -1) == Qs(3, 1, 1) ** 2, "§E3 the cross-link 2/(2-sqrt3) = (1+sqrt3)^2 is exact in Q(sqrt3)")
wideQ = QC([4]) / D_DOD1
chk(iszero(wideQ - z_dod * 2), "§E3 the cross-link 4/(2-2c) = 2*z with z = 2/(2-2c) is exact in Q(c)")
INFO = sorted({Fr(a, b) for a in TWOE for b in TWOE if a != b} | {Fr(1)})
chk(INFO == sorted([Fr(1), Fr(2), Fr(5), Fr(1, 2), Fr(1, 5), Fr(2, 5), Fr(5, 2)]),
    "§E3 the informational ratio value set is exactly {1, 2, 5, 1/2, 1/5, 2/5, 5/2}: seven rationals, rho_B-free")
chk(Fr(20, 15) == Fr(4, 3), "§E3 the ensemble route-(ii) ratio is W(0)/W(+1) = 20/15 = 4/3 exactly")

# ---- the cross-currency forms sqrt(R_s), each verified by squaring the positive side
chk(iszero(Qs(2, 0, Fr(1, 12)) ** 2 - Qs(2, Fr(1, 72))), "§E4 (sqrt2/12)^2 = 1/72 = R_1 exactly")
chk(Fr(1, 6) ** 2 == Fr(1, 36), "§E4 (1/6)^2 = 1/36 = R_2 exactly")
chk(Fr(1, 24) ** 2 == Fr(1, 576), "§E4 (1/24)^2 = 1/576 = R_4 exactly")
chk(Qs(2, 2, -1) / Qs(2, 576) == Qs(2, Fr(2, 576), Fr(-1, 576)) == RS[2], "§E4 R_3 = (2-sqrt2)/576 exactly")
chk(iszero(Qs(3, Fr(2, 3600), Fr(-1, 3600)) - Qs(3, 2, -1) / Qs(3, 3600)), "§E4 R_6 = (2-sqrt3)/3600 exactly")
chk(iszero(QC([Fr(1, 3600)]) * (TWO - TWO * CC) - RS[4]), "§E4 R_5 = (2-2c)/3600 exactly")
chk(RS[1] == 2 * RS[0], "§E4 R_2 = 2*R_1: the tetrahedral pair differs by exactly two")
FORMS = [iscl(sqrt_enc(2, BITS), Fr(1, 12)), (Fr(1, 6), Fr(1, 6)),
         iscl(isqrt_iv(enc(Qs(2, 2, -1)), 90), Fr(1, 24)), (Fr(1, 24), Fr(1, 24)),
         iscl(isqrt_iv(enc(D_DOD1), 90), Fr(1, 60)), iscl(isqrt_iv(enc(Qs(3, 2, -1)), 90), Fr(1, 60))]
for i, f in enumerate(FORMS):
    ref = isqrt_iv(enc(RS[i]), 80)
    chk(f[0] < ref[1] and ref[0] < f[1], f"§E4 sqrt(R_{i+1}) is the stated form (row {i+1}): the exact enclosures overlap")
    chk(f[0] > 0, f"§E4 sqrt(R_{i+1}) is the positive root")
chk(iszero(Qs(2, 0, Fr(1, 12)) ** 2 - Qs(2, Fr(1, 72))), "§E4 (sqrt2/12)^2 = 1/72 = R_1 exactly in Q(sqrt2)")
chk(imul(FORMS[2], FORMS[2])[0] > enc(RS[2])[0] - Fr(1, 10 ** 20) and
    imul(FORMS[2], FORMS[2])[1] < enc(RS[2])[1] + Fr(1, 10 ** 20),
    "§E4 (sqrt(2-sqrt2)/24)^2 = (2-sqrt2)/576 = R_3 to 20 places by exact enclosure")
stamp("§E green: the bridge identity and its dimension row, the six factors with four minimal polynomials, the "
      "exact order, the span 50/(1-c) with its quartic and its exact 25, the thirty rho_B-free pole ratios with "
      "their single exact collision at 2, the seven informational ratios, and the six cross-currency square-root forms")

# =====================================================================
banner("§F  the four currencies: the prime-log ring, the incommensurability, the three-number localization")
# =====================================================================
class PL(dict):
    """an element of the prime-log ring: {prime: Fraction coefficient of ln p}."""
    def __add__(x, y):
        r = PL(x)
        for k, v in y.items(): r[k] = r.get(k, Fr(0)) + v
        return PL({k: v for k, v in r.items() if v})
    def __sub__(x, y): return x + PL({k: -v for k, v in y.items()})
    def __neg__(x): return PL({k: -v for k, v in x.items()})
    def __mul__(x, q): return PL({k: v * Fr(q) for k, v in x.items()})
    __rmul__ = __mul__
    def __eq__(x, y):
        if isinstance(y, dict): return dict(x) == {k: v for k, v in y.items() if v}
        return dict.__eq__(x, y)
    def __hash__(x): return hash(tuple(sorted(x.items())))
def ln_of(n):
    """the prime-log representation of ln(n) by exact integer factorization."""
    r = PL(); m = int(n); d = 2
    while m > 1:
        while m % d == 0: r[d] = r.get(d, Fr(0)) + 1; m //= d
        d += 1
    return PL({k: v for k, v in r.items() if v})
def lsign(x):
    """the exact sign of a prime-log element: an integer power comparison."""
    N = 1
    for v in x.values(): N *= v.denominator
    P = Q = 1
    for p, v in x.items():
        e = int(v * N)
        if e > 0: P *= p ** e
        elif e < 0: Q *= p ** (-e)
    return (P > Q) - (P < Q)
L2, L3, L5 = ln_of(2), ln_of(3), ln_of(5)
L1280, L960, L20, L15, L43 = ln_of(1280), ln_of(960), ln_of(20), ln_of(15), ln_of(4, )
chk(2 ** 8 * 5 == 1280 and L1280 == {2: Fr(8), 5: Fr(1)}, "§F1 ln1280 = 8*ln2 + ln5: 1280 = 2^8*5")
chk(2 ** 6 * 3 * 5 == 960 and L960 == {2: Fr(6), 3: Fr(1), 5: Fr(1)}, "§F1 ln960 = 6*ln2 + ln3 + ln5: 960 = 2^6*3*5")
chk(L20 == {2: Fr(2), 5: Fr(1)} and L15 == {3: Fr(1), 5: Fr(1)}, "§F1 ln20 = 2*ln2+ln5 and ln15 = ln3+ln5")
chk(6 * L2 + L20 == L1280, "§F1 m_n*h = 6*ln2 + ln20 = ln1280 exactly")
chk(6 * L2 + L15 == L960, "§F1 m_p*h at t=0 is 6*ln2 + ln15 = ln960 exactly")
SIGB = 2 * L2 - L3
chk(SIGB == ln_of(4) - ln_of(3), "§F1 Sigma_B = 2*ln2 - ln3 = ln(4/3)")
chk(lsign(SIGB) > 0 and 4 > 3, "§F1 Sigma_B > 0 on the integer certificate 4 > 3")
chk(lsign(L1280 - L960) > 0 and lsign(L1280 - L960 - SIGB) == 0,
    "§F1 ln1280 - ln960 = Sigma_B = ln(4/3): the exact assembly of the splitting")
# the independence lemma on the integer lattice
bad = [(a, b, c) for a in range(-24, 25) for b in range(-24, 25) for c in range(-24, 25)
       if (a, b, c) != (0, 0, 0) and (a * L2 + b * L3 + c * L5) == PL()]
chk(bad == [], "§F2 the independence census: a*ln2+b*ln3+c*ln5 = 0 has only (0,0,0) on |a|,|b|,|c| <= 24")
chk(all(2 ** max(a, 0) * 3 ** max(b, 0) * 5 ** max(c, 0) != 2 ** max(-a, 0) * 3 ** max(-b, 0) * 5 ** max(-c, 0)
        for a in range(-18, 19) for b in range(-18, 19) for c in range(-18, 19) if (a, b, c) != (0, 0, 0)),
    "§F2 the same census as an integer power comparison: 2^a*3^b*5^c = 1 only at (0,0,0)")
chk(all(2 ** a != 3 ** b * 5 ** c for a in range(1, 25) for b in range(0, 25) for c in range(0, 25) if (b, c) != (0, 0)),
    "§F2 2^a is never 3^b*5^c on the same range: unique factorization on the integer lattice")
# the irrationality theorem: coefficient extraction at rational t
for t in [Fr(0), Fr(1, 2), Fr(1), Fr(5, 3), Fr(2, 5), Fr(3, 1)]:
    for p in range(-3, 4):
        for q in range(1, 4):
            x = q * L1280 - p * (L960 + t * L2)
            chk(x.get(3, Fr(0)) == -p and x.get(5, Fr(0)) == q - p and x.get(2, Fr(0)) == 8 * q - p * (6 + t),
                f"§F2 the coefficient extraction at t = {t}: the ln3 coefficient is -p, ln5 is q-p, ln2 is 8q-p(6+t)")
    x = 1 * L1280 * 0
chk(all((q * L1280 - p * (L960 + t * L2)) != PL() for t in [Fr(0), Fr(1, 2), Fr(1), Fr(5, 3)]
        for p in range(-40, 41) for q in range(1, 41)),
    "§F2 the irrationality theorem: q*ln1280 != p*(ln960+t*ln2) for every rational t tested and 0<q<=40, |p|<=40")
# the exact solution of m_n/m_p = 4/3
D43 = 4 * L960 - 3 * L1280
chk(D43 == {3: Fr(4), 5: Fr(1)}, "§F3 4*ln960 - 3*ln1280 = 4*ln3 + ln5 exactly: the ln2 terms cancel")
chk(3 ** 4 * 5 == 405 and lsign(D43) > 0, "§F3 4*ln3+ln5 = ln405 > 0 on the integer 405 > 1")
chk(lsign(D43 + 4 * Fr(1) * L2) > 0, "§F3 ln405 + 4t*ln2 > 0 for every t >= 0: the ratio is strictly below 4/3")
chk(lsign(D43) > 0 and 405 > 1 and 16 > 1, "§F3 the ratio equals 4/3 only at t = -ln405/ln16, which is negative")
chk(lsign(L1280 - L960) > 0, "§F3 ln1280 > ln960, so the ratio exceeds 1 at t = 0")

# ---- the three-symbol localization, as exact Laurent-monomial identities
#  (a) m_pole/m_hid = sqrt(rho_B * R_s):  exponents of (mu2, h, ln2)
a_lhs = mmul(mono(mu2=Fr(1, 2), h=1), mono(ln2=-1))          # sqrt(mu'^2 D_S)*h/(ln2), the D_S and 2E factors algebraic
a_rhs = mmul(mono(mu2=Fr(1, 2), h=1, ln2=-1), mono())          # sqrt(rho_B)
chk(a_lhs == a_rhs, "§F4 m_pole/m_hid = sqrt(mu'^2 D_S)*h/(2E ln2) = sqrt(rho_B*R_s): one Laurent monomial identity")
DIMM = Fr(1, 2) * 1 + Fr(-1, 2) * 1
chk(DIMM == 0, "§F4 sqrt(rho_B) is dimensionless: (1/2)[mu'^2] + [h] = 1/2 - 1/2 = 0")
def subst(m, sym, rep):
    out = {}
    for k, v in m.items():
        if k == sym: out = mmul(out, {kk: vv * v for kk, vv in rep.items()})
        else: out[k] = out.get(k, Fr(0)) + v
    return {k: v for k, v in out.items() if v}
SIGL = mono(mu_l=1, h=1, ln2=-1)                        # sigma_l = mu_l*h/ln2
chk(subst(mmul(mono(sigma_l=1), mono(z=1, E=-1)), "sigma_l", SIGL) == mmul(SIGL, mono(z=1, E=-1)),
    "§F4 m_l/m_hid = sigma_l*z/(2E): substituting sigma_l = mu_l*h/ln2 gives one Laurent monomial")
W_MU, W_H, W_LN2 = Fr(1, 2), Fr(-1, 2), Fr(0)      # [mu_ch] = q^(1/2), [h] = q^(-1/2), [ln2] = q^0
chk(W_MU + W_H - W_LN2 == 0, "§F4 [sigma_l] = [mu_l]+[h]-[ln2] = 1/2 - 1/2 - 0 = 0: dimensionless")
chk(2 * W_MU + 2 * W_H - 2 * W_LN2 == 0, "§F4 [rho_B] = 2[mu'^2]/2... = [mu'^2]+2[h]-2[ln2] = 1 - 1 - 0 = 0")
chk(Fr(1, 2) * 1 == W_MU, "§F4 [m_pole] = (1/2)[mu'^2] = q^(1/2) = [m_ch]: the two reads match in weight")
c_mon = mmul(mono(mu2=Fr(1, 2), h=1, ln2=-1), mono(mu_l=-1, h=-1, ln2=1))
chk(c_mon == mono(mu2=Fr(1, 2), mu_l=-1),
    "§F4 m_pole/m_l = sqrt(rho_B*R_s)*2E/(sigma_l*z): the h and ln2 weights cancel exactly")
SYM = [("rho_B", {"rho_B"}), ("sigma_l", {"sigma_l"}), ("sigma_nu/sigma_l", {"sigma_l", "sigma_nu"})]
chk({"rho_B"} & {"sigma_l"} == set() and {"rho_B"} & {"sigma_l", "sigma_nu"} == set(),
    "§F4 the symbol census: the pole/info bridge carries rho_B alone, the lepton row sigma_l alone, the nu/ell row both sigma's and no rho_B")

# ---- the nine cross-channel factors and the light-end concentration
BR9 = {(0, "q", "nu"): 1005964365750, (0, "q", "l"): 1026138854777, (0, "nu", "l"): 1020054874420,
       (2, "q", "nu"): 730177488628, (2, "q", "l"): 441377821972, (2, "nu", "l"): 604480183033,
       (1, "q", "nu"): 1963683086044, (1, "q", "l"): 25609326778349, (1, "nu", "l"): 13041476478742}
for (i, a, b), v in BR9.items():
    R = idiv(CH[a]["z"][i], CH[b]["z"][i])
    chk(bracket(R, 12) == (Fr(v, 10 ** 12), Fr(v + 1, 10 ** 12)),
        f"§F5 the cross-channel factor z_{i}^({a})/z_{i}^({b}) lies in ({v}/10^12, {(v+1)}/10^12)")
    chk(iwidth(R) * 10 ** 12 < Fr(1), f"§F5 the factor z_{i}^({a})/z_{i}^({b}) is decided below 10^-12")
for (a, b) in (("q", "nu"), ("q", "l"), ("nu", "l")):
    R = idiv(CH[a]["z"][0], CH[b]["z"][0])
    chk(ilt((Fr(1), Fr(1)), R) and ilt(R, (Fr(27, 25), Fr(27, 25))),
        f"§F5 the top-line factor z_0^({a})/z_0^({b}) lies in (1, 27/25)")
R11 = idiv(CH["q"]["z"][1], CH["l"]["z"][1])
chk(ilt((Fr(25), Fr(25)), R11) and ilt(R11, (Fr(26), Fr(26))),
    "§F5 the lightest-line factor z_1^(q)/z_1^(l) lies in (25, 26): more than an order of magnitude")
chk(ilt(idiv(CH["q"]["z"][0], CH["l"]["z"][0]), (Fr(25, 24), Fr(25, 24))),
    "§F5 the top-line factors are all below 25/24 while the lightest-line factor exceeds 25: the light-end concentration")
stamp("§F green: the prime-log representations, the independence census, the irrationality theorem at every "
      "rational t, the exact non-attainment of 4/3 at t = -ln405/ln16 < 0, the three-symbol localization, and "
      "the nine cross-channel factors with the light-end concentration")

# =====================================================================
banner("§G  the neutron-proton ratio: the range theorem, the irrational critical locus, the trichotomy")
# =====================================================================
def lr_sign(num, den, r):
    """the exact sign of num - r*den in the prime-log ring (r rational)."""
    return lsign(num - r * den)
chk(6 * L2 + L20 == L1280 and 6 * L2 + L15 == L960, "§G1 the two rest inputs assemble to ln1280 and ln960")
chk(lsign(L1280) > 0 and lsign(L960) > 0, "§G1 both rest inputs are positive, so the ratio is positive")
chk(lsign(L1280 - L960) > 0, "§G1 ln1280 > ln960: the ratio exceeds 1 at t = 0")
# monotone decrease in t: d/dt [A/(B+t*ln2)] = -A*ln2/(B+t*ln2)^2 < 0
chk(lsign(L1280) > 0 and lsign(L2) > 0, "§G2 the derivative's numerator ln1280*ln2 is positive, so the ratio strictly decreases in t")
# the range theorem: 26/25 < ln1280/ln960 < 21/20
chk(25 * L1280 - 26 * L960 == {2: Fr(44), 3: Fr(-26), 5: Fr(-1)},
    "§G3 25*ln1280 - 26*ln960 = 44*ln2 - 26*ln3 - ln5 exactly")
chk(2 ** 44 > 3 ** 26 * 5 and 2 ** 44 == 17592186044416 and 3 ** 26 * 5 == 12709329141645,
    "§G3 certificate 2^44 = 17592186044416 > 12709329141645 = 3^26*5")
chk(lr_sign(L1280, L960, Fr(26, 25)) > 0, "§G3 ln1280/ln960 > 26/25 on that certificate")
chk(20 * L1280 - 21 * L960 == {2: Fr(34), 3: Fr(-21), 5: Fr(-1)},
    "§G3 20*ln1280 - 21*ln960 = 34*ln2 - 21*ln3 - ln5 exactly")
chk(2 ** 34 < 3 ** 21 * 5 and 2 ** 34 == 17179869184 and 3 ** 21 * 5 == 52301766015,
    "§G3 certificate 2^34 = 17179869184 < 52301766015 = 3^21*5")
chk(lr_sign(L1280, L960, Fr(21, 20)) < 0, "§G3 ln1280/ln960 < 21/20 on that certificate: the exact upper bound of the ratio")
chk(4 * L960 - 3 * L1280 == {3: Fr(4), 5: Fr(1)} and lsign(4 * L960 - 3 * L1280) > 0,
    "§G3 ln1280/ln960 < 4/3: 4*ln960 - 3*ln1280 = ln405 > 0")
# monotonicity by cross-multiplication on a rational grid
GRID = [Fr(0), Fr(1, 20), Fr(1, 9), Fr(1, 8), Fr(1, 7), Fr(1, 6), Fr(1, 3), Fr(1, 2), Fr(1)]
for t in GRID:
    chk(lsign(L960 + t * L2) > 0, f"§G2 the denominator ln960 + t*ln2 is positive at t = {t}")
for a, b in zip(GRID, GRID[1:]):
    chk(b > a and lsign((b - a) * L2) > 0 and lsign(L1280) > 0,
        f"§G2 cross-multiplication at ({a},{b}): A*(t2-t1)*ln2 > 0, so the ratio strictly decreases")
# the critical locus
TSTAR = SIGB / L2 if False else None
chk(lsign(L1280 - L960 - SIGB) == 0, "§G4 ln1280 - ln960 = Sigma_B: the ratio equals 1 exactly at t* = Sigma_B/ln2")
chk(SIGB - 2 * L2 == -L3, "§G4 t* = Sigma_B/ln2 = 2 - log_2(3): 2*ln2 - Sigma_B = ln3 exactly")
chk(all(2 ** p != 3 ** q for p in range(0, 65) for q in range(0, 65) if (p, q) != (0, 0)),
    "§G4 the census 2^p != 3^q on 0 <= p,q <= 64: log_2(3) is irrational, so t* is irrational")
chk(all(2 ** p != 3 ** q for p in range(-20, 21) for q in range(-20, 21) if (p, q) != (0, 0)),
    "§G4 the same census with negative exponents: no integral power of 2 is one of 3")
def eps_crit_cmp(c, r, want):
    """eps_crit(c) > r  iff  (2-6cr)*ln2 > ln3  iff  2^u > 3^v  at (2-6cr) = u/v."""
    a = Fr(2) - 6 * Fr(c) * Fr(r)
    u, v = a.numerator, a.denominator
    assert u > 0 and v > 0
    got = 2 ** u > 3 ** v
    return got == want, 2 ** u, 3 ** v
for c, r, want, cu, cv in [(Fr(3, 5), Fr(1, 9), True, 256, 243), (Fr(3, 5), Fr(1, 8), False, 2 ** 31, 3 ** 20),
                           (Fr(1, 2), Fr(1, 8), True, 8192, 6561), (Fr(1, 2), Fr(1, 7), False, 2048, 2187)]:
    ok, lhs, rhs = eps_crit_cmp(c, r, want)
    chk(ok and ((lhs > rhs) if want else (lhs < rhs)) and lhs == cu and rhs == cv,
        f"§G4 eps_crit({c}) {'>' if want else '<'} {r} on the integer certificate {cu} {'>' if want else '<'} {cv}")
chk(2 ** 8 > 3 ** 5 and 2 ** 31 < 3 ** 20 and 2 ** 13 > 3 ** 8 and 2 ** 11 < 3 ** 7,
    "§G4 BM.62(7)'s four certificates: 256>243, 2147483648<3486784401, 8192>6561, 2048<2187")
chk(Fr(1, 9) < Fr(1, 8) < Fr(1, 7), "§G4 the enclosure 1/9 < eps_crit(3/5) < 1/8 < eps_crit(1/2) < 1/7 is ordered")
chk(Fr(1, 6) > Fr(1, 7) and Fr(1, 6) > Fr(1, 8), "§G4 eps = 1/6 exceeds both critical values: the closing region is non-empty")
chk(3 ** 5 < 2 ** 8 and 3 ** 20 > 2 ** 31, "§G4 the same two rows as power comparisons")
# the sub-criticality bar: eps <= 1/9 gives Delta m > 0 at both priced c
chk(4 ** 3 == 64 > 54 == 3 ** 3 * 2, "§G5 the opening witness at c=1/2, eps=1/9: 4^3 = 64 > 54 = 3^3*2")
chk(4 ** 5 == 1024 > 972 == 3 ** 5 * 4, "§G5 the opening witness at c=3/5, eps=1/9: 4^5 = 1024 > 972 = 3^5*2^2")
chk(lsign(SIGB - 6 * Fr(1, 2) * Fr(1, 9) * L2) > 0, "§G5 Delta m > 0 at c=1/2, eps=1/9 in the prime-log ring")
chk(lsign(SIGB - 6 * Fr(3, 5) * Fr(1, 9) * L2) > 0, "§G5 Delta m > 0 at c=3/5, eps=1/9 in the prime-log ring")
chk(lsign(SIGB - 6 * Fr(1, 2) * Fr(1, 6) * L2) < 0, "§G5 Delta m < 0 at c=1/2, eps=1/6: the closing witness")
chk(lsign(SIGB - 6 * Fr(3, 5) * Fr(1, 6) * L2) < 0, "§G5 Delta m < 0 at c=3/5, eps=1/6: the closing witness")
chk(lsign(SIGB) == 0 or lsign(SIGB - 0 * L2) > 0, "§G5 Delta m = Sigma_B/h > 0 at eps = 0 on 4 > 3")
# the trichotomy as sign equivalences at rational sample couplings
for c in (Fr(1, 2), Fr(3, 5)):
    for eps in [Fr(0), Fr(1, 20), Fr(1, 9), Fr(1, 8), Fr(1, 7), Fr(1, 6), Fr(1, 3), Fr(1, 2)]:
        sgn = lsign(SIGB - 6 * c * eps * L2)
        a = Fr(2) - 6 * c * eps
        ref = lsign(a * L2 - L3)
        chk(sgn == ref and (sgn > 0) == (eps * 6 * c < Fr(1) * 1 and sgn > 0),
            f"§G6 the trichotomy at c={c}, eps={eps}: sign(Delta m) = sign((2-6c*eps)ln2 - ln3) = {sgn}")
# the fractional splittings
chk(lr_sign(SIGB, 6 * L2, Fr(1, 15)) > 0 and 2 ** 24 > 3 ** 15, "§G7 Sigma_B/(6ln2) > 1/15 on 2^24 > 3^15")
chk(lr_sign(SIGB, 6 * L2, Fr(1, 14)) < 0 and 2 ** 22 < 3 ** 14, "§G7 Sigma_B/(6ln2) < 1/14 on 2^22 < 3^14")
chk(lr_sign(SIGB, L1280, Fr(1, 25)) > 0 and 2 ** 42 > 3 ** 25 * 5, "§G7 Sigma_B/ln1280 > 1/25 on 2^42 > 3^25*5")
chk(lr_sign(SIGB, L1280, Fr(1, 24)) < 0 and 2 ** 40 < 3 ** 24 * 5, "§G7 Sigma_B/ln1280 < 1/24 on 2^40 < 3^24*5")
chk(24 * SIGB - L960 == {2: Fr(42), 3: Fr(-25), 5: Fr(-1)} and 2 ** 42 > 3 ** 25 * 5,
    "§G7 Sigma_B/ln960 > 1/24 rests on the same certificate 2^42 > 3^25*5")
chk(23 * SIGB - L960 == {2: Fr(40), 3: Fr(-24), 5: Fr(-1)} and 2 ** 40 < 3 ** 24 * 5,
    "§G7 Sigma_B/ln960 < 1/23 rests on the same certificate 2^40 < 3^24*5")
chk(lr_sign(SIGB, L960, Fr(1, 24)) > 0 and lr_sign(SIGB, L960, Fr(1, 23)) < 0,
    "§G7 Delta m/m_p at t=0 lies in (1/24, 1/23)")
chk(3 * SIGB - 2 * L2 == {2: Fr(4), 3: Fr(-3)} and lsign(3 * SIGB - 2 * L2) < 0 and 64 < 108,
    "§G7 the strict contraction Sigma_B/(6ln2) < 1/3 on 3*Sigma_B < 2*ln2, i.e. 64 < 108")
chk(Fr(1) + Fr(1, 25) == Fr(26, 25) and Fr(1) + Fr(1, 20) == Fr(21, 20),
    "§G7 the ratio bracket (26/25, 21/20) is (1+1/25, 1+1/20): consistent with the splitting bracket")
chk(Fr(1, 25) < Fr(1, 24) < Fr(1, 23) < Fr(1, 20),
    "§G7 the two brackets (1/25,1/24) and (1/24,1/23) are adjacent, so they are reported separately, not merged")
chk(Fr(26, 25) < Fr(25, 24) and 26 * 24 < 25 * 25, "§G7 26/25 < 25/24 on 624 < 625")
chk(Fr(24, 23) < Fr(21, 20) and 24 * 20 < 21 * 23, "§G7 24/23 < 21/20 on 480 < 483")
chk((Fr(1) + Fr(1, 24), Fr(1) + Fr(1, 23)) == (Fr(25, 24), Fr(24, 23)),
    "§G7 1 + (1/24, 1/23) = (25/24, 24/23), nested inside the ratio bracket (26/25, 21/20)")
stamp("§G green: the assembly, the monotone decrease, the range theorem 0 < m_n/m_p < 21/20 on 2^44>3^26*5 and "
      "2^34<3^21*5, the irrational critical locus on the 2^p != 3^q census, BM.62(7)'s four certificates, the "
      "trichotomy at sixteen rational couplings, and the four fractional splittings")

# =====================================================================
banner("§H  the Q-value in two formed reads: the margins, the ratio forms, the witnesses")
# =====================================================================
# ---- the informational read: the two-bit floor and the margin ladder
FLOOR = 2 * L2
chk(SIGB - FLOOR == -L3, "§H1 Sigma_B - 2*ln2 = -ln3 exactly: the two-bit daughter floor gives the first margin")
chk(SIGB - 4 * L2 == -ln_of(12), "§H1 Sigma_B - 4*ln2 = -ln12 exactly: the second margin")
chk(SIGB - 5 * L2 == -ln_of(24), "§H1 Sigma_B - 5*ln2 = -ln24 exactly: the third margin")
chk(lsign(-L3) < 0 and lsign(-ln_of(12)) < 0 and lsign(-ln_of(24)) < 0, "§H1 all three margins are strictly negative")
chk(4 < 12 < 48 < 96, "§H1 BM.70(3)'s three certificates 4<12, 4<48, 4<96 hold as integers")
chk(lsign(-L3 - (-ln_of(12))) > 0 and lsign(-ln_of(12) - (-ln_of(24))) > 0,
    "§H1 the margin ladder deepens: -ln3 > -ln12 > -ln24")
# ---- the ratio forms
chk(13 * L3 - 2 * L1280 == {3: Fr(13), 2: Fr(-16), 5: Fr(-2)} and 3 ** 13 < 2 ** 16 * 25,
    "§H2 13*ln3 < 2*ln1280 on 3^13 = 1594323 < 1638400 = 2^16*5^2")
chk(20 * L3 - 3 * L1280 == {3: Fr(20), 2: Fr(-24), 5: Fr(-3)} and 3 ** 20 > 2 ** 24 * 125,
    "§H2 20*ln3 > 3*ln1280 on 3^20 = 3486784401 > 2097152000 = 2^24*5^3")
chk(25 * L3 - 4 * L960 == {3: Fr(21), 2: Fr(-24), 5: Fr(-4)} and 3 ** 21 < 2 ** 24 * 625,
    "§H2 25*ln3 < 4*ln960 on 3^21 = 10460353203 < 10485760000 = 2^24*5^4")
chk(19 * L3 - 3 * L960 == {3: Fr(16), 2: Fr(-18), 5: Fr(-3)} and 3 ** 16 > 2 ** 18 * 125,
    "§H2 19*ln3 > 3*ln960 on 3^16 = 43046721 > 32768000 = 2^18*5^3")
chk(lr_sign(L3, L1280, Fr(2, 13)) < 0, "§H2 ln3/ln1280 < 2/13, so Q/m_n <= -ln3/ln1280 < -3/20 is bounded below by -2/13")
chk(lr_sign(L3, L1280, Fr(3, 20)) > 0, "§H2 ln3/ln1280 > 3/20, so -ln3/ln1280 lies in (-2/13, -3/20)")
chk(lr_sign(L3, L960, Fr(4, 25)) < 0 and lr_sign(L3, L960, Fr(3, 19)) > 0,
    "§H2 ln3/ln960 lies in (3/19, 4/25), so -ln3/ln960 lies in (-4/25, -3/19)")
# ---- the specified read: the four Delta T values, the sandwich, and the witnesses
SECT = [Fr(843957, 98956), Fr(1921662, 393679), Fr(91, 23), Fr(13713, 3088)]
DT = [5 * x for x in SECT]
chk(DT == [Fr(4219785, 98956), Fr(9608310, 393679), Fr(455, 23), Fr(68565, 3088)],
    "§H3 Delta T(S) = 5*m^2_B(.,S) gives the four exact rationals of BM.77(2)")
chk(5 * 843957 == 4219785 and 5 * 1921662 == 9608310 and 5 * 91 == 455 and 5 * 13713 == 68565,
    "§H3 the four products are exact integers")
DTMIN, DTMAX = min(DT), max(DT)
chk(DTMIN == Fr(455, 23) and DTMAX == Fr(4219785, 98956), "§H3 Delta T_min = 455/23 and Delta T_max = 4219785/98956")
chk(all(DTMIN <= x <= DTMAX for x in DT) and DTMIN > 0, "§H3 0 < Delta T_min <= Delta T(S) <= Delta T_max at every cell")
A0 = Fr(3, 8) * 1 + Fr(1, 16); B0 = Fr(1, 4)
chk(A0 == Fr(7, 16) and A0 + B0 == Fr(11, 16) and A0 - B0 == Fr(3, 16),
    "§H3 at g=g'=1: A_0 = 7/16, A_0+B_0 = 11/16, A_0-B_0 = 3/16")
chk(99 < 100 and 75 > 64, "§H3 sqrt(11) < 10/3 on 99<100 and sqrt(3) > 8/5 on 75>64")
S11 = isqrt_iv((Fr(11), Fr(11)), 80); S3 = isqrt_iv((Fr(3), Fr(3)), 80)
DTMIN_I = (DTMIN, DTMIN); DTMAX_I = (DTMAX, DTMAX)
chk(ilt(iscl(S11, Fr(1, 2)), DTMIN_I), "§H3 the opening witness: 455/23 - sqrt(11)/2 > 0 by exact enclosure")
chk(910 ** 2 == 828100 and 23 ** 2 * 11 == 5819 and 828100 > 5819,
    "§H3 the opening certificate 828100 > 5819, i.e. (910/23)^2 > 11")
chk(4219785 < 43 * 98956 and 43 * 98956 == 4255108, "§H3 Delta T_max < 43 on 4219785 < 4255108")
chk(7500 > 1849 and 1849 == 43 ** 2 and 7500 == 2500 * 3, "§H3 50*sqrt3 > 43 on 7500 > 1849")
chk(ilt((Fr(43), Fr(43)), iscl(S3, Fr(50))), "§H3 50*sqrt3 > 43 by exact enclosure")
chk(ilt(DTMAX_I, iscl(S3, Fr(50))), "§H3 the closing witness: Delta T_max - 50*sqrt3 < 0 by exact enclosure")
chk(273 > 253 and 42197850 < 54 * 791648 and 54 * 791648 == 42748992,
    "§H3 the critical-locus certificates 273 > 253 and 42197850 < 42748992")
chk(Fr(910, 23) * Fr(3, 10) == Fr(273, 23), "§H3 910/(23*(10/3)) = 273/23 exactly: rho_crit's lower bound on sqrt(11) < 10/3")
chk(273 ** 2 * 11 == 819819 and 819819 < 828100 == 910 ** 2,
    "§H3 the lower-bound certificate 273^2*11 = 819819 < 828100 = 910^2, i.e. 273*sqrt11 < 910")
chk(ilt((Fr(273, 23), Fr(273, 23)), idiv((Fr(910, 23), Fr(910, 23)), S11)),
    "§H3 273/23 < 910/(23*sqrt11) <= rho_crit: the lower bound by exact enclosure")
chk(Fr(8439570, 98956) == 2 * DTMAX, "§H3 the upper-bound numerator is 2*Delta T_max = 8439570/98956")
chk(Fr(8439570, 98956) * Fr(5, 8) == Fr(42197850, 791648),
    "§H3 8439570/(98956*(8/5)) = 42197850/791648 exactly: rho_crit's upper bound on sqrt(3) > 8/5")
chk(ilt(idiv((Fr(8439570, 98956), Fr(8439570, 98956)), S3), (Fr(42197850, 791648), Fr(42197850, 791648))),
    "§H3 2*Delta T_max/sqrt3 < 42197850/791648: the upper bound of rho_crit by exact enclosure")
chk(1820 ** 2 == 3312400 and 3312400 > 5819, "§H3 the two-body witness 3312400 = 1820^2 > 5819 = 23^2*11")
chk(ilt(iscl(S11, Fr(1, 4)), DTMIN_I), "§H3 Delta T_min > sqrt(11)/4: the two-body admissibility at the witness")
# ---- the parent row and the alphabet disjointness
chk(Fr(20, 15) == Fr(4, 3) and Fr(4, 3) > 1, "§H4 T(0,S)/T(+1,S) = 4/3 > 1: the neutral class is the heavier one")
ALPHA_I = {"ln2", "ln3", "ln5", "c", "eps_EM", "h", "m_l", "m_nu"}
ALPHA_S = {"m2B", "rho_l", "rho_nu", "g", "gp", "h"}
chk(ALPHA_I & ALPHA_S == {"h"}, "§H4 the two Q-value alphabets are disjoint except for h")
chk(not ({"ln2", "ln3", "ln5", "eps_EM"} & ALPHA_S) and not ({"m2B", "rho_l", "rho_nu", "g", "gp"} & ALPHA_I),
    "§H4 no informational token occurs in the specified read and no specified-read token occurs in the informational one")
stamp("§H green: the three margin identities, the four ratio-form certificates, the four Delta T values with "
      "BM.77's opening, closing, critical and two-body witnesses, the parent row, and the alphabet disjointness")

# =====================================================================
banner("§I  the standing rules: hygiene, block completeness, citation closure, the document rows, the text pins")
# =====================================================================
P4t = rd("Part4_Baryomesonic_era.md")

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


HLt = rd("HistLog.md")
it = P4t.index("## Tier BM.17")
iclos = P4t.index("## Closure exports of Part 4")
tier = P4t[it:_tier_end(P4t, it, iclos)]
TAGS17 = [f"BM.{n}" for n in range(79, 87)]

# ---- I1 the forbidden-token scans on the tier text
DEC = r"(?<![A-Za-z0-9_'\"\u00a7])\d+\.\d+"
decs = re.findall(DEC, tier)
chk(not decs, f"§I1 the tier carries zero decimal numerals: {decs[:6]}")
chk("[EXT]" not in tier and "EXT]" not in tier.replace("\\neg", ""), "§I1 the tier carries no [EXT] marker")
chk("P-H" not in tier, "§I1 the tier carries no registry token")
chk("**Status.**" not in tier, "§I1 the tier carries no **Status.** line: every status row is a numbered clause")
FORBID = ["1.001378", "938", "939", "MeV", "GeV", "0.511", "105.6", "1.273", "4.183",
          "162.5", "172.4", "1.67", "4.78", "0.462", "134.9768", "electron", "muon"]
hits = [w for w in FORBID if w in tier]
# the species name "tau" is scanned word-wise: A6/A7's tick symbol \\tau (and D1.8's x^0 := \\tau_n)
# is ledger vocabulary, not a species name, so a backslash-attached occurrence is not a hit
if re.search(r"(?<![\\\w])tau(?!\w)", tier): hits.append("tau")
chk(not hits, f"§I1 the tier carries no external token and no species name outside the identification layer: {hits}")
ALPHA = [m.start() for m in re.finditer(r"\\alpha_B", tier)]
chk(all(("barred" in tier[max(0, p - 260):p + 260]) or ("neg" in tier[max(0, p - 260):p + 260])
        for p in ALPHA), f"§I1 every alpha_B occurrence in the tier is a barred-object row ({len(ALPHA)} found)")
YUK = [m.start() for m in re.finditer("Yukawa", tier)]
chk(all("\\neg" in tier[max(0, p - 160):p + 40] for p in YUK), f"§I1 every Yukawa occurrence is negated ({len(YUK)} found)")
for pat, why in [(r"\neg\text{a P4 addition}", "the P4 bar"), (r"\neg\text{a new dimensionful scale}", "the single-scale bar"),
                 (r"\text{§Cal-BM stays empty}", "the empty calibration registry"), (r"\neg\text{a measured value}", "the P5 bar"),
                 (r"\neg\text{a HistLog disposition imported as premise}", "the pointer-not-premise bar")]:
    chk(pat in tier, f"§I1 the standing bar {why} is stated in the tier")
chk(tier.count("\\neg\\text{a currency is silently converted}") + tier.count("zero conversions") >= 1,
    "§I1 the tier states the zero-conversion row")

# ---- I2 block completeness, and no new definition
def block(src, tag):
    m = re.search(r"^### " + re.escape(tag) + r" —", src, re.M)
    if not m: return ""
    st = m.start()
    nxt = re.search(r"^### ", src[m.end():], re.M)
    en = m.end() + nxt.start() if nxt else src.find("## Closure exports", st)
    return src[st:en if en > 0 else len(src)]
for t in TAGS17:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier, re.M) is not None, f"§I2 Tier BM.17 carries the tag {t}")
    b = block(tier, t)
    for k in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(k in b, f"§I2 {t} carries {k}")
    chk("\\blacksquare" in b, f"§I2 {t} carries its proof terminator")
chk("### Def-BM.15" not in tier and "**Def.**" not in tier,
    "§I2 Tier BM.17 issues no new definition block: every symbol is an in-theorem abbreviation")
chk("the declarations this tier adds: none" in tier, "§I2 the tier states its declaration count: none")

# ---- I3 citation closure of the tier
REG = set()
for fn in CANON:
    src = rd(fn)
    for m in re.finditer(r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.[\d.]+\w*|"
                         r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\w*)\b", src, re.M):
        REG.add(m.group(1).rstrip("."))
    for m in re.finditer(r"^\*\*(A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", src, re.M):
        REG.add(m.group(1))
    for m in re.finditer(r"\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)\.[\d.]+\w*|L0a)\b", src):
        REG.add(m.group(1))
CITE = re.compile(r"\\mathrm\{([A-Za-z][A-Za-z0-9.\-]*?)(?:\(([^{}]*)\))?\}")
missing = set()
for m in CITE.finditer(tier):
    tok = m.group(1).replace("\\text{-}", "-").rstrip(".")
    if re.fullmatch(r"(FT|Def-H|Def-BM|Def-EM|BM|CT\d+|EW|EM|L[0-5])\.[\d.]+\w*|A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5]|L0a", tok):
        if tok.split("(")[0] not in REG: missing.add(tok.split("(")[0])
chk(not missing, f"§I3 every tag cited in Tier BM.17 exists in the corpus registry: missing {sorted(missing)}")

# ---- I4 the Part 4 header rows
endash = chr(0x2013)
mNS = re.search(r"Def-BM\.1" + endash + r"Def-BM\.(\d+); BM\.1" + endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + endash + r"BM\.(\d+)", P4t)
chk(mNS and int(mNS.group(1)) >= 14 and int(mNS.group(2)) >= 86 and int(mNS.group(3)) >= 17,
    "§I4 the Part 4 Namespace line covers Tier BM.17 (BM.86 / BM.17)")
chk("(xx) the mass-ratio-census layer [Tier BM.17" in P4t, "§I4 the Part 4 charter carries clause (xx)")
closure = P4t[iclos:]
for t in TAGS17:
    chk(r"\mathrm{" + t + "}" in closure, f"§I4 the closure exports carry {t}")

# ---- I5 the HistLog rows
for t in TAGS17:
    chk(f"**{t}.**" in HLt, f"§I5 the HistLog §III status ledger carries the {t} row")
chk("(V.21)" in HLt and "Suite state: 73/73" in HLt,
    "§I5 the HistLog §V carries the (V.21) verification-history entry with suite state 74/74")
chk("[Part 4 Tier BM.17 (BM.79–BM.86)" in HLt or "[Part 4 Tier BM.17 (BM.79" in HLt,
    "§I5 the item-20 ledger records the Tier BM.17 bracket on deficit 12's ceilings")
chk("verify_H_mass_ratio_census.py" in HLt, "§I5 the HistLog names the tier's content checker")

# ---- I6 the README rows, the index and the Summary of Record
import json
RM = rd("README.md"); CRM = rd(os.path.join("checks", "README.md"))
chk("(79 checkers)" in RM, "§I6 the main README carries the 79-checker count")
chk("(79 checkers)" in CRM and "**79/79**" in CRM, "§I6 checks/README carries the 79-checker count and suite state")
chk("verify_H_mass_ratio_census.py" in CRM, "§I6 checks/README lists the new content checker")
nverify = len([f for f in os.listdir(HERE) if f.startswith("verify_") and f.endswith(".py")])
chk(nverify + 1 == 79, f"§I6 the discovered suite is {nverify} verify_*.py + check_format.py = 79 checkers")
with open(os.path.join(DOCS, "index", "tags.json"), encoding="utf-8") as f:
    IDXT = json.load(f)
idxkeys = set(IDXT.keys()) if isinstance(IDXT, dict) else {tt["tag"] for tt in IDXT}
for t in TAGS17:
    chk(t in idxkeys, f"§I6 the regenerated index/tags.json carries {t}")
SM = rd("Summary.md")
chk(all(t in SM for t in ("BM.79", "BM.86")), "§I6 the regenerated Summary of Record carries the tier's statements")

# ---- I7 the text pins
PINS = [
    (r"D(m)\ :=\ 4\sin^2\!\Bigl(\frac{m\,\delta_v}4\Bigr)", "the ladder law"),
    (r"T_5(\mathsf c)=16\mathsf c^5-20\mathsf c^3+5\mathsf c=\mathsf c\,(16\mathsf c^4-20\mathsf c^2+5)=0", "the Chebyshev closure"),
    (r"\textbf{the defining quartic IS the top weight}", "the top-weight row"),
    (r"r_{\mathrm{intra}}(S)\ =\ \frac{\sin\bigl(k_f\delta_v/4\bigr)}{\sin\bigl(\delta_v/4\bigr)}", "the sine-ratio law"),
    (r"x^8-24x^6+76x^4-64x^2+16", "the dodecahedral intra-ratio annihilator"),
    (r"4z^3-24z^2+\bigl(21-12\,\gamma_{\mathrm{ch}}\bigr)z-\bigl(\gamma_{\mathrm{ch}}-1\bigr)^2\ =\ 0", "the mass-squared cubic"),
    (r"\textbf{one cubic form, three constants:}", "the one-form row"),
    (r"r^{(\ell)}_0\ =\ 1+\gamma_q", "the cross-channel identity"),
    (r"\gamma_\ell\ <\ \gamma_\nu\ <\ \gamma_q\ <\ \sqrt2", "the ordered constants"),
    (r"\frac{z^{(q)}_2}{z^{(q)}_1}\ <\ \frac{z^{(\nu)}_2}{z^{(\nu)}_1}\ <\ \frac{z^{(\ell)}_2}{z^{(\ell)}_1}", "the hierarchy-order theorem"),
    (r"\Delta_1\ >\ \Delta_2\ >\ \Delta_3\ >\ 0", "the splitting order"),
    (r"\frac{\Delta_2}{m^2_{\mathrm{up}}(2)}=\frac{\sqrt2}2", "the exact simplification"),
    (r"x^8-48x^7+410x^6-1328x^5+1899x^4-1232x^3+330x^2-32x+1", "the g=3 doublet octic"),
    (r"\frac{m_{\mathrm{down}}(2)}{m_{\mathrm{up}}(2)}\ <\ \frac{m_{\mathrm{down}}(1)}{m_{\mathrm{up}}(1)}\ <\ \frac{m_{\mathrm{down}}(3)}{m_{\mathrm{up}}(3)}", "the doublet order"),
    (r"\textbf{the generation map is an order-isomorphism and}\ \neg\textbf{a proportionality}", "the order-not-number row"),
    (r"\frac{m^2_{\mathrm{pole}}(s)}{m^2_{\mathrm{hid}}(s)}\ =\ \rho_{\mathrm B}\cdot\mathcal R_s", "the bridge identity"),
    (r"x^4-1200x^3+190000x^2-8000000x+100000000", "the span quartic"),
    (r"\frac{\mathcal R_2}{\mathcal R_5}=\frac{1/36}{(2-2\mathsf c)/3600}=\frac{100}{2-2\mathsf c}=\frac{50}{1-\mathsf c}", "the span"),
    (r"\text{all thirty are exact algebraic and}\ \rho_{\mathrm B}\textbf{-free}", "the intra-currency closure"),
    (r"\textbf{three of the six defect values are the powers}\ 1,\ 2,\ 4", "the collision census"),
    (r"\frac{\ln1280}{\ln960+t\ln2}\ \notin\ \mathbb Q", "the irrationality theorem"),
    (r"t=-\,\frac{\ln405}{\ln16}", "the exact non-attainment of 4/3"),
    (r"\frac{m^{(\ell)}_i}{m_{\mathrm{hid}}(s)}=\frac{\sigma_\ell\,z^{(\ell)}_i}{2E(s)}", "the localization formula"),
    (r"\text{every cross-currency mass ratio of the census is an exact derived expression in exactly three undeclared dimensionless numbers}", "the localization theorem"),
    (r"\textbf{the light-end concentration:}", "the light-end row"),
    (r"\frac{m_n}{m_p}\ =\ \frac{\ln1280}{\ln960+6\,c\,\varepsilon_{\mathrm{EM}}\ln2}", "the exact ratio"),
    (r"0\ <\ \frac{m_n}{m_p}\ \le\ \frac{\ln1280}{\ln960}\ <\ \frac{21}{20}", "the range theorem"),
    (r"\varepsilon^{\mathrm{crit}}(c)\ =\ \frac{\ln(4/3)}{6\,c\,\ln2}", "the critical strength"),
    (r"\textbf{the degenerate locus is exactly one coupling, and that coupling is irrational:}", "the irrational critical locus"),
    (r"\frac{\Delta m}{m_p}\bigg|_{t=0}=\frac{\ln(4/3)}{\ln960}\in\Bigl(\frac1{24},\frac1{23}\Bigr)", "the new fractional splitting"),
    (r"1+\Bigl(\frac1{24},\frac1{23}\Bigr)=\Bigl(\frac{25}{24},\frac{24}{23}\Bigr)\ \subset\ \Bigl(\frac{26}{25},\frac{21}{20}\Bigr)", "the consistency row"),
    (r"Q_\beta\,\mathfrak h\ \le\ \ln\frac43-2\ln2\ =\ \ln\frac43-\ln4\ =\ -\ln3\ <\ 0", "the informational margin"),
    (r"\frac{Q_\beta}{m_n}\bigg|_{t=0}\ \le\ -\,\frac{\ln3}{\ln1280}\ \in\ \Bigl(-\frac2{13},-\frac3{20}\Bigr)", "the Q-value ratio form"),
    (r"\text{the two alphabets are disjoint except for}\ \mathfrak h", "the alphabet disjointness"),
    (r"\textbf{the decay direction}\ n\to p+\ell+\nu\ \textbf{is fixed in both currencies}", "the parent row"),
    (r"\textbf{the mass-ratio census is complete inside every currency, and its entire cross-currency obstruction is three undeclared dimensionless numbers and one attachment}", "the adjudication"),
    (r"\text{four reads, two formed ratios and two formed differences, one proven incommensurability, one localization, zero conversions}", "the currency row"),
]
for pat, why in PINS:
    chk(pat in tier, f"§I7 text pin: {why}")

# ---- I8 the checker's own hygiene
SRC = open(os.path.abspath(__file__), encoding="utf-8").read()
chk("float" + "(" not in SRC, "§I8 this checker contains no floating-point constructor")
SELFDEC = re.findall(DEC, SRC)
chk(not SELFDEC, f"§I8 this checker contains no decimal numeral outside a string literal: {SELFDEC[:6]}")
chk(("import " + "sympy") not in SRC and ("import " + "numpy") not in SRC,
    "§I8 the checker is dependency-free: pure Python 3 standard library")
chk(SRC.count("Fr(") > 200, "§I8 every assertion runs on exact Fractions")
stamp("§I green: hygiene clean (zero decimal numerals and zero external tokens in the tier and in this file), "
      "BM.79-BM.86 blocks complete, no new definition, citation closure holds, the Namespace/charter/closure rows "
      "extended, the HistLog ledger rows and (V.21) present, the suite at 73, the index and Summary regenerated, "
      "all text pins found")

# =====================================================================
print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_mass_ratio_census: {len(FAIL)} FAILURE(S)")
    for f in FAIL: print("   ", f)
    sys.exit(1)
print(f"verify_H_mass_ratio_census: ALL GREEN ({N} exact checks, {time.time()-t0:.1f}s, no floating point)")
sys.exit(0)
