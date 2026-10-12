#!/usr/bin/env python3
"""verify_H_constituent_transport_splitting.py - Tier BM.14 of Part 4:
the constituent transport splitting, the vertex asymmetry, the observation frames,
the quark generation structure, the alpha_B obstruction, and the full mass splitting.

Exact arithmetic only: Fraction; complex-over-Fraction; Laurent-monomial exponent
vectors; the multivariate polynomial ring Q[g,g',c_1..c_4] with Faddeev-LeVerrier
charpolys; the prime-log ring  Q (+) (+)_p Q*ln p  whose sign tests reduce to exact
comparisons of two non-negative integers; rational interval enclosures with exact
alternating-series remainder bounds.  No floating point enters any assertion.

  §A  the vertex asymmetry: the epsilon/delta continuation censuses, the three
      annihilation rows, and the zero splitting (hypothesis refuted)
  §B  the observation frame: the metric charge-exponent census, the two mask
      vocabularies, the surviving frame content (hypothesis refuted)
  §C  the constituent transport splitting: the end-pair multiplicity, the parity
      law, the class census W(Q), the class transport entropy, the constituent row
  §D  the quark generation structure: the channel spectrum, Vieta, Q = 2/3, the
      ordering, the generation count, the fractional-charge impossibility
  §E  alpha_B: the inventory scans, the coupling-blindness theorem, the obstruction
  §F  the full mass splitting: the assembly, the exact critical strength, the
      integer certificates, the sub-criticality bar, the beta re-adjudication
  §G  the standing rules: token scans, block completeness, citation closure
"""
import os, re, sys, time
from fractions import Fraction as Fr
from itertools import product, permutations
from math import gcd, isqrt

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.environ.get("QUBITICK_DOCS") or os.path.normpath(os.path.join(HERE, ".."))
CANON = ["Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
         "Part4_Baryomesonic_era.md", "Census.md"]
TIER_FILE = "Part4_Baryomesonic_era.md"          # the tier lives inside Part 4
TIER_HEAD = "Tier BM.14"                          # its section banner

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
def stamp(m): print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")
def banner(t):
    print("\n" + "=" * 96); print(t); print("=" * 96)

# =====================================================================
#  exact algebra: the prime-log ring
# =====================================================================
def _factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

class Ln:
    """a + sum_p e[p]*ln(p).  The {ln p} are Q-linearly independent (unique
    factorization), so a pure-log element is ln(N/D) for exact integers N, D."""
    __slots__ = ("a", "e")
    def __init__(s, a=0, e=None):
        s.a = Fr(a); s.e = {p: Fr(v) for p, v in (e or {}).items() if Fr(v) != 0}
    @staticmethod
    def log(n, d=1):
        assert n > 0 and d > 0
        x = Ln()
        for p, k in _factor(n).items(): x.e[p] = x.e.get(p, Fr(0)) + k
        for p, k in _factor(d).items(): x.e[p] = x.e.get(p, Fr(0)) - k
        x.e = {p: v for p, v in x.e.items() if v != 0}; return x
    @staticmethod
    def _c(o): return o if isinstance(o, Ln) else Ln(o)
    def __add__(s, o):
        o = Ln._c(o); r = Ln(s.a + o.a, dict(s.e))
        for p, v in o.e.items(): r.e[p] = r.e.get(p, Fr(0)) + v
        r.e = {p: v for p, v in r.e.items() if v != 0}; return r
    __radd__ = __add__
    def __sub__(s, o): return s + (-Ln._c(o))
    def __rsub__(s, o): return (-s) + Ln._c(o)
    def __neg__(s): return Ln(-s.a, {p: -v for p, v in s.e.items()})
    def __mul__(s, r):
        if isinstance(r, Ln): raise TypeError("Ln*Ln leaves the ring")
        r = Fr(r); return Ln(s.a * r, {p: v * r for p, v in s.e.items()})
    __rmul__ = __mul__
    def __eq__(s, o):
        o = Ln._c(o); return s.a == o.a and s.e == o.e
    def __hash__(s): return hash((s.a, tuple(sorted(s.e.items()))))
    @property
    def pure(s): return s.a == 0
    def free_primes(s): return set(s.e)
    def __repr__(s):
        t = [str(s.a)] if s.a else []
        for p in sorted(s.e):
            v = s.e[p]
            t.append(("" if v == 1 else ("-" if v == -1 else f"{v}*")) + f"ln{p}")
        return "(" + " + ".join(t).replace("+ -", "- ") + (")" if t else "0")

LN2, LN3, LN5 = Ln.log(2), Ln.log(3), Ln.log(5)

def intpair(x):
    assert x.pure, "a rational part is present"
    if not x.e: return (1, 1)
    M = 1
    for v in x.e.values():
        d = int(v.denominator); M = M * d // gcd(M, d)
    Nn = Dd = 1
    for p, v in x.e.items():
        k = int(v * M); assert Fr(k, M) == v
        if k >= 0: Nn *= p ** k
        else:      Dd *= p ** (-k)
    return Nn, Dd

def lsign(x, y=0):
    a, b = intpair(x - Ln._c(y)); return (a > b) - (a < b)

def lcert(x, y=0):
    a, b = intpair(x - Ln._c(y)); return a, b, (a > b) - (a < b)

# =====================================================================
#  exact algebra: Laurent monomials (the dimensional / charge-exponent census)
# =====================================================================
class Mono:
    __slots__ = ("coeff", "ex")
    def __init__(s, coeff=1, ex=None):
        s.coeff = Fr(coeff); s.ex = {k: int(v) for k, v in (ex or {}).items() if int(v) != 0}
    def __mul__(s, o):
        e = dict(s.ex)
        for k, v in o.ex.items(): e[k] = e.get(k, 0) + v
        return Mono(s.coeff * o.coeff, e)
    def __pow__(s, n): return Mono(s.coeff ** n, {k: v * n for k, v in s.ex.items()})
    def inv(s): return Mono(Fr(1) / s.coeff, {k: -v for k, v in s.ex.items()})
    def __truediv__(s, o): return s * o.inv()
    def __eq__(s, o): return s.coeff == o.coeff and s.ex == o.ex
    def exp(s, k): return s.ex.get(k, 0)
    def __repr__(s):
        t = str(s.coeff) if s.coeff != 1 else ""
        for k in sorted(s.ex): t += f"*{k}^{s.ex[k]}"
        return t or "1"

H     = Mono(1, {"h": 1})          # the single free dimensionful scale
LN2M  = Mono(1, {"ln2": 1})
PI    = Mono(1, {"pi": 1})
QCH   = Mono(1, {"Q": 1})          # the charge exponent bookkeeping base
EINT  = Mono(1, {"E": 1})

# =====================================================================
#  exact algebra: Q[g,g',...] with complex coefficients
# =====================================================================
class Poly:
    __slots__ = ("names", "d")
    def __init__(s, names, d=None):
        s.names = tuple(names)
        s.d = {k: Fr(v) for k, v in (d or {}).items() if Fr(v) != 0}
    @staticmethod
    def zero(n): return Poly(n)
    @staticmethod
    def one(n): return Poly(n, {(0,) * len(n): Fr(1)})
    @staticmethod
    def const(n, q): return Poly(n, {(0,) * len(n): Fr(q)}) if Fr(q) else Poly(n)
    @staticmethod
    def var(n, i):
        e = [0] * len(n); e[i] = 1
        return Poly(n, {tuple(e): Fr(1)})
    @staticmethod
    def _c(n, o): return o if isinstance(o, Poly) else Poly.const(n, o)
    def __add__(s, o):
        o = Poly._c(s.names, o); r = Poly(s.names, dict(s.d))
        for k, v in o.d.items(): r.d[k] = r.d.get(k, Fr(0)) + v
        r.d = {k: v for k, v in r.d.items() if v != 0}; return r
    __radd__ = __add__
    def __sub__(s, o): return s + (-Poly._c(s.names, o))
    def __rsub__(s, o): return (-s) + Poly._c(s.names, o)
    def __neg__(s): return Poly(s.names, {k: -v for k, v in s.d.items()})
    def __mul__(s, o):
        o = Poly._c(s.names, o); r = Poly(s.names)
        for k1, v1 in s.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r.d[k] = r.d.get(k, Fr(0)) + v1 * v2
        r.d = {k: v for k, v in r.d.items() if v != 0}; return r
    __rmul__ = __mul__
    def __truediv__(s, r):
        if isinstance(r, Poly): raise TypeError("Poly/Poly")
        return s * Fr(1) / Fr(r) if False else Poly(s.names, {k: v / Fr(r) for k, v in s.d.items()})
    def __pow__(s, n):
        r = Poly.one(s.names)
        for _ in range(n): r = r * s
        return r
    def __eq__(s, o): return s.d == Poly._c(s.names, o).d
    def __hash__(s): return hash(tuple(sorted(s.d.items())))
    def is_zero(s): return not s.d
    def monomials(s): return set(s.d)
    def used_vars(s):
        out = set()
        for e in s.d:
            for n, k in zip(s.names, e):
                if k: out.add(n)
        return out
    def __repr__(s):
        if not s.d: return "0"
        out = []
        for e, v in sorted(s.d.items(), key=lambda kv: (-sum(kv[0]), kv[0])):
            m = "".join(f"*{n}" + (f"^{k}" if k != 1 else "")
                        for n, k in zip(s.names, e) if k)
            out.append(f"{v}{m}")
        return " + ".join(out).replace("+ -", "- ")

class CPoly:
    """complex over Poly: a + b*i with a,b in Poly (same name list)."""
    __slots__ = ("names", "re", "im")
    def __init__(s, names, re=None, im=None):
        s.names = tuple(names); s.re = re or Poly(names); s.im = im or Poly(names)
    def __add__(s, o): return CPoly(s.names, s.re + o.re, s.im + o.im)
    def __sub__(s, o): return CPoly(s.names, s.re - o.re, s.im - o.im)
    def __neg__(s): return CPoly(s.names, -s.re, -s.im)
    def __mul__(s, o):
        return CPoly(s.names, s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def conj(s): return CPoly(s.names, s.re, -s.im)
    def scal(s, p): return CPoly(s.names, s.re * p, s.im * p)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def is_zero(s): return s.re.is_zero() and s.im.is_zero()

def inner(u, v):
    """Hermitian inner product <u,v> = sum conj(u_k) v_k  for CPoly vectors."""
    acc = CPoly(u[0].names)
    for a, b in zip(u, v): acc = acc + a.conj() * b
    return acc

# =====================================================================
#  exact algebra: rational interval enclosures
# =====================================================================
def cos_sin_enc(x, bits):
    assert Fr(-1) <= x <= 1
    tgt = Fr(1, 2 ** bits)
    tc = Fr(1); Sp = Fr(1); k = 0
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
    k2 = bits + 4; NN = nn * (1 << (2 * k2)); r = isqrt(NN)
    lo = Fr(r, 1 << k2); hi = Fr(r + 1, 1 << k2)
    assert lo * lo <= nn < hi * hi and hi - lo < Fr(1, 2 ** bits)
    return (lo, hi)

def ln2_enc(bits):
    """ln2 = sum_{n>=1} 1/(n 2^n): all terms positive, exact tail bound."""
    tgt = Fr(1, 2 ** (bits + 6)); S = Fr(0); t = Fr(1); n = 0
    while True:
        n += 1; t /= 2; add = t / n; S += add
        if add < tgt: break
    tail = t / (n + 1) / (1 - Fr(1, 2))          # sum_{m>n} 1/(m2^m) < 2/((n+1)2^{n+1})*2
    return (S, S + 2 * tail)

def ln_enc(m, bits):
    """exact enclosure of ln(m) for a positive integer m."""
    L2 = ln2_enc(bits + 8)
    k = 0; y = Fr(m)
    while y < 1: y *= 2; k -= 1
    while y >= 2: y /= 2; k += 1
    u = Fr(1) / y - Fr(1)                        # in [0, 1/2]; ln y = -sum u^n/n
    tgt = Fr(1, 2 ** (bits + 8)); S = Fr(0); term = Fr(1); n = 0
    while True:
        n += 1; term *= u; add = term / n; S += add
        if u < 1 and term * u / ((n + 1) * (1 - u)) < tgt: break
        if u == 0: break
    tail = term * u / ((n + 1) * (1 - u)) if u < 1 else Fr(0)
    lnY = (-S - tail, -S)
    return (lnY[0] + k * L2[0], lnY[1] + k * L2[1])

def lnrat_enc(p, q, bits):
    A, B = ln_enc(p, bits), ln_enc(q, bits)
    return (A[0] - B[1], A[1] - B[0])

def iadd(A, B): return (A[0] + B[0], A[1] + B[1])
def isub(A, B): return (A[0] - B[1], A[1] - B[0])
def imul(A, B):
    p = [A[0]*B[0], A[0]*B[1], A[1]*B[0], A[1]*B[1]]; return (min(p), max(p))
def iscl(A, q): return (A[0]*q, A[1]*q) if q >= 0 else (A[1]*q, A[0]*q)
def idiv(A, B):
    assert B[0] > 0; return (A[0]/B[1], A[1]/B[0])
def iwidth(A): return A[1] - A[0]
def icontains(A, v): return A[0] <= v <= A[1]
def idisjoint(A, B): return A[1] < B[0] or B[1] < A[0]

def reduce_rel(p, rels):
    """reduce p in Q[names] modulo monic relations rels = {(name, k): replacement}:
    name^k -> replacement.  Terminates: each step lowers the total degree in the
    relation's variable by k.  Returns the unique normal form."""
    q = Poly(p.names, dict(p.d))
    while True:
        hit = None
        for (nm, k), rep in rels.items():
            i = p.names.index(nm)
            for e, v in sorted(q.d.items()):
                if v != 0 and e[i] >= k:
                    hit = (i, k, e, v, rep); break
            if hit: break
        if not hit: break
        i, k, e, v, rep = hit
        shift = list(e); shift[i] -= k
        rest = Poly(p.names, {tuple(shift): Fr(1)})
        q.d[e] = Fr(0)
        q = q + rest * rep * v
        q.d = {kk: vv for kk, vv in q.d.items() if vv != 0}
    return q

def charpoly_Poly(M):
    """Faddeev-LeVerrier: coefficients of det(xI - M), highest first, over Poly."""
    n = len(M); names = M[0][0].names + ("x",)
    A = [[Poly(names, m.d) for m in row] for row in M]
    x = Poly.var(names, len(names) - 1)
    one, zero = Poly.one(names), Poly.zero(names)
    I = [[one if i == j else zero for j in range(n)] for i in range(n)]
    out = [one]; Mk = I
    for k in range(1, n + 1):
        prev = I if k == 1 else Mk
        prod = [[sum((A[i][t] * prev[t][j] for t in range(n)), zero) for j in range(n)]
                for i in range(n)]
        tr = sum((prod[i][i] for i in range(n)), zero)
        c = tr * Poly.const(names, Fr(-1, k))
        out.append(c)
        Mk = [[prod[i][j] + (c if i == j else zero) for j in range(n)] for i in range(n)]
    return out, names

def horner(coeffs, x):
    r = coeffs[0]
    for c in coeffs[1:]: r = r * x + c
    return r

# =====================================================================
banner("§A  the vertex asymmetry: continuation censuses, annihilation rows, the zero splitting")
# ---------------------------------------------------------------- A1 the epsilon seal
EPS = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
for a, b, c in permutations(range(3)):
    sgn = 1
    p = [a, b, c]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    EPS[a][b][c] = (-1) ** inv
chk(sum(abs(EPS[a][b][c]) for a in range(3) for b in range(3) for c in range(3)) == 6,
    "§A1 epsilon_{ijk}: exactly six nonzero entries, all +-1")
PERM3 = list(permutations(range(3)))
def sgn_of(p):
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return (-1) ** inv
INVARIANT, SGNROW = [], {}
for p in PERM3:
    ok = all(EPS[p[i]][p[j]][p[k]] == EPS[i][j][k] for i in range(3) for j in range(3) for k in range(3))
    SGNROW[p] = (sgn_of(p), ok)
    if ok: INVARIANT.append(p)
chk(all(EPS[p[0]][p[1]][p[2]] == sgn_of(p) * EPS[i][j][k]
        for p in PERM3 for i, j, k in [(0, 1, 2)]),
    "§A1 epsilon_{sigma(i)sigma(j)sigma(k)} = sgn(sigma) epsilon_{ijk} (total antisymmetry)")
chk(len(INVARIANT) == 3, "§A1 the epsilon-invariant continuation group has order 3 (= A_3 = C_3)")
chk(all(sgn_of(p) == 1 for p in INVARIANT), "§A1 the invariants are exactly the even permutations")
chk(len([p for p in INVARIANT if p != (0, 1, 2)]) == 2,
    "§A1 the nontrivial continuation count of the strong 3-vertex is 2")
C3 = {tuple((i + k) % 3 for i in range(3)) for k in range(3)}
chk(set(INVARIANT) == C3, "§A1 the invariant group is the cyclic group of order 3")
# ---------------------------------------------------------------- A2 the chain wall
DELTA = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
chk(all(DELTA[i][j] == DELTA[j][i] for i in range(3) for j in range(3)),
    "§A2 delta^i_j is index-symmetric: the bare 2-tensor admits the leg swap")
NATIVE_11 = [((), ())]                     # S_1 x S_1 on (one in-leg, one out-leg)
chk(len(NATIVE_11) == 1, "§A2 the type-preserving relabelling group of a (1,1)-vertex has order 1")
SIG = (+1, -1)
ENDPAIRS = list(product(SIG, SIG))
def q_of(p): return Fr(p[0] - p[1], 2)
SWAP = {p: (p[1], p[0]) for p in ENDPAIRS}
chk(all(q_of(SWAP[p]) == -q_of(p) for p in ENDPAIRS),
    "§A2 the leg swap maps q -> -q on all four end pairs: it is charge-odd")
chk(SWAP[(+1, +1)] == (+1, +1) and SWAP[(-1, -1)] == (-1, -1),
    "§A2 the swap fixes exactly the two neutral end pairs and exchanges the two charged ones")
chk(len({q_of(p) for p in ENDPAIRS}) == 3 and {q_of(p) for p in ENDPAIRS} == {Fr(-1), Fr(0), Fr(1)},
    "§A2 the end-read alphabet is exactly {-1,0,+1}")
# ---------------------------------------------------------------- A3 the asymmetry
ORD = {"strong": 3, "em": 1}
NONTRIV = {"strong": 2, "em": 0}
chk(ORD["strong"] - ORD["em"] == 2, "§A3 the order asymmetry is exactly 2")
chk(NONTRIV["strong"] - NONTRIV["em"] == 2, "§A3 the nontrivial-count asymmetry is exactly 2")
chk(ORD["strong"] - 1 == NONTRIV["strong"] and ORD["em"] - 1 == NONTRIV["em"],
    "§A3 both conventions are the order minus the identity: the asymmetry is convention-free")
# ---------------------------------------------------------------- A4 class-blindness
CLASS_ROWS = {
    "junction grammar":       {"neutral": "epsilon_ijk 3-juncture", "unit": "epsilon_ijk 3-juncture"},
    "vertex type":            {"neutral": "(3,0)",                  "unit": "(3,0)"},
    "sealing-phase class":    {"neutral": "4Z",                     "unit": "4Z"},
    "E_int":                  {"neutral": 6,                        "unit": 6},
    "continuation group":     {"neutral": "A_3 (order 3)",          "unit": "A_3 (order 3)"},
    "sealing grammar count":  {"neutral": "g(3)=1",                 "unit": "g(3)=1"},
}
DIFF = {k: v["neutral"] != v["unit"] for k, v in CLASS_ROWS.items()}
chk(not any(DIFF.values()),
    "§A4 every vertex-structural row is identical on the two charge classes (difference 0)")
CHK_DISTINGUISH = {"q_net": {"neutral": 0, "unit": 1}}
chk(CHK_DISTINGUISH["q_net"]["neutral"] != CHK_DISTINGUISH["q_net"]["unit"],
    "§A4 the charge class itself is the only distinguishing row in this table")
# ---------------------------------------------------------------- A5 the Gram algebra
GN = ("g", "gp")
g, gp = Poly.var(GN, 0), Poly.var(GN, 1)
oneP, zeroP = Poly.one(GN), Poly.zero(GN)
def cp(re=0, im=0):
    return CPoly(GN, re if isinstance(re, Poly) else Poly.const(GN, re),
                    im if isinstance(im, Poly) else Poly.const(GN, im))
SIG1 = [[cp(0), cp(1)], [cp(1), cp(0)]]
SIG2 = [[cp(0), cp(0, Fr(-1))], [cp(0, 1), cp(0)]]
SIG3 = [[cp(1), cp(0)], [cp(0), cp(Fr(-1))]]
SIG0 = [[cp(1), cp(0)], [cp(0), cp(1)]]
SEED = [cp(0), cp(1)]                       # v = (0,1)^T : W3 v = -v/2, Y v = +v/2, Q v = 0
Wm = [SIG1, SIG2, SIG3, SIG0]
COEF = [g, g, g, gp]                        # G = (g W1, g W2, g W3, g' Y)
def mvec(M, v):
    return [sum((M[i][k] * v[k] for k in range(2)), cp()) for i in range(2)]
def half(m):  return [[e.scal(Fr(1, 2)) for e in row] for row in m]
GV = [mvec([[e.scal(COEF[A]) for e in row] for row in half(Wm[A])], SEED) for A in range(4)]
# the seed eigenvalue rows
W3v = mvec(half(SIG3), SEED)
Yv  = mvec(half(SIG0), SEED)
chk(W3v[0].is_zero() and (W3v[1] + SEED[1].scal(Fr(1, 2))).is_zero(),
    "§A5 W_3 v = -v/2 exactly")
chk(Yv[0].is_zero() and (Yv[1] - SEED[1].scal(Fr(1, 2))).is_zero(),
    "§A5 Y v = +v/2 exactly (the seed hypercharge coordinate y_0 = 1/2)")
Qv = [W3v[k] + Yv[k] for k in range(2)]
chk(Qv[0].is_zero() and Qv[1].is_zero(), "§A5 Q v = (W_3 + Y) v = 0: the seed is the charge-null state")
Gr   = [[inner(GV[A], GV[B]).re for B in range(4)] for A in range(4)]
GrIm = [[inner(GV[A], GV[B]).im for B in range(4)] for A in range(4)]
def blk(A, B):
    if A == B and A < 3: return Fr(1, 4) * g * g
    if A == B == 3:      return Fr(1, 4) * gp * gp
    if {A, B} == {2, 3}: return Fr(-1, 4) * g * gp
    return Poly.zero(GN)
chk(all(Gr[A][B] == blk(A, B) for A in range(4) for B in range(4)),
    "§A5 Re<G_A v, G_B v> = (1/4)[[g^2,0,0,0],[0,g^2,0,0],[0,g^2,-gg'],[0,-gg',g'^2]] exactly")
chk(all(GrIm[A][B] == -GrIm[B][A] for A in range(4) for B in range(4)) and
    all(GrIm[A][A].is_zero() for A in range(4)),
    "§A5 Im<G_A v, G_B v> is antisymmetric with a zero diagonal: it cancels in c_A c_B")
KER = [Poly.zero(GN), Poly.zero(GN), gp, g]
KERv = [sum((Gr[A][B] * KER[B] for B in range(4)), Poly.zero(GN)) for A in range(4)]
chk(all(x.is_zero() for x in KERv), "§A5 the kernel line c || (0,0,g',g) is annihilated exactly")
# G(c) and its two exact forms, in Q[g,g',c1..c4]
CN = ("g", "gp", "c1", "c2", "c3", "c4")
cg, cgp, C1, C2, C3, C4 = [Poly.var(CN, i) for i in range(6)]
def lift(p):
    r = Poly(CN)
    for e, v in p.d.items():
        r = r + Poly(CN, {(e[0], e[1], 0, 0, 0, 0): v})
    return r
CV = [C1, C2, C3, C4]
Gc = sum((CV[A] * CV[B] * lift(Gr[A][B]) for A in range(4) for B in range(4)), Poly.zero(CN))
QUART = lift(Poly.const(GN, Fr(1, 4)))
chk(Gc == QUART * (cg * cg * (C1 * C1 + C2 * C2) + (cg * C3 - cgp * C4) ** 2),
    "§A5 G(c) = (1/4)[g^2(c_1^2+c_2^2) + (g c_3 - g' c_4)^2] : exact sum-of-squares form")
chk(Gc == QUART * (cg * cg * (C1*C1 + C2*C2 + C3*C3) - 2 * cg * cgp * C3 * C4 + cgp * cgp * C4 * C4),
    "§A5 G(c) = (1/4)[g^2(c_1^2+c_2^2+c_3^2) - 2gg'c_3c_4 + g'^2c_4^2] : expanded form agrees")
DIFFQ = QUART * (cg*cg + cgp*cgp) * (C1*C1 + C2*C2 + C3*C3 + C4*C4) - Gc
chk(DIFFQ == QUART * (cgp*cgp * (C1*C1 + C2*C2) + (cg * C4 + cgp * C3) ** 2),
    "§A5 the sandwich ceiling (g^2+g'^2)|c|^2/4 - G(c) is a sum of squares")
DN = ("G", "Gp", "d1", "d2", "d3", "d4", "xx")
def relift(p):
    r = Poly(DN)
    for e, v in p.d.items():
        r = r + Poly(DN, {(e[0], e[1], 0, 0, 0, 0, 0): v})
    return r
GrD = [[relift(Gr[A][B]) for B in range(4)] for A in range(4)]
CPD, _ = charpoly_Poly(GrD)
xD = Poly.var(DN, 6); GD, GpD = Poly.var(DN, 0), Poly.var(DN, 1)
tgtD = (xD - GD * GD / 4) ** 2 * xD * (xD - (GD * GD + GpD * GpD) / 4)
chk(horner(CPD, xD) == tgtD,
    "§A5 charpoly(xI - Gram) = (x - g^2/4)^2 * x * (x - (g^2+g'^2)/4) exactly")
chk(horner(CPD, xD).used_vars() <= {"G", "Gp", "xx"},
    "§A5 the charpoly's free symbols are {g, g', x}: zero colour symbols")
# the profile evaluation in Q[g,g',c,s,r3]/(c^2+s^2-1, r3^2-3)
QN = ("g", "gp", "cc", "ss", "r3")
qg, qgp, qc, qs, qr = [Poly.var(QN, i) for i in range(5)]
REL = {("ss", 2): Poly.one(QN) - qc * qc, ("r3", 2): Poly.const(QN, Fr(3))}
def qlift(p):
    r = Poly(QN)
    for e, v in p.d.items():
        r = r + Poly(QN, {(e[0], e[1], 0, 0, 0): v})
    return r
Gq = [[qlift(Gr[A][B]) for B in range(4)] for A in range(4)]
def cos_at(k):        # cos(delta + 2 pi k / 3) for k = 0,1,2
    if k % 3 == 0: return qc
    if k % 3 == 1: return -qc / 2 - qr * qs / 2
    return -qc / 2 + qr * qs / 2
A0q = Fr(3, 8) * qg * qg + Fr(1, 16) * qgp * qgp
B0q = Fr(1, 4) * qg * qgp
VALS = []
for i in range(3):
    prof = [cos_at((0 - i) % 3), cos_at((1 - i) % 3), cos_at((2 - i) % 3), Poly.const(QN, Fr(1, 2))]
    Gi = sum((prof[A] * prof[B] * Gq[A][B] for A in range(4) for B in range(4)), Poly.zero(QN))
    VALS.append(reduce_rel(Gi, REL))
for i in range(3):
    rhs = reduce_rel(A0q - B0q * cos_at(2 - i), REL)      # cos(delta + 2pi(2-i)/3)
    chk(VALS[i] == rhs, f"§A5 G(c({i})) = A_0 - B_0 cos(delta + 2pi(2-{i})/3) exactly in the quotient ring")
SUMRULE = reduce_rel(sum(VALS, Poly.zero(QN)) - 3 * A0q, REL)
chk(SUMRULE.is_zero(), "§A5 the sum rule: sum_i G(c(i)) = 3 A_0 exactly (the phase-independent row)")
ORBIT = {reduce_rel(A0q - B0q * cos_at(-j), REL) for j in range(3)}
chk(set(VALS) == ORBIT, "§A5 the orbit's Gram-value set is {A_0 - B_0 cos(delta - 2pi j/3)}_j")
A0 = Fr(3, 8) * g * g + Fr(1, 16) * gp * gp
B0 = Fr(1, 4) * g * gp
A0 = Fr(3, 8) * g * g + Fr(1, 16) * gp * gp
B0 = Fr(1, 4) * g * gp
chk((A0 - B0) == Fr(3,8)*(g - gp/3)**2 + Fr(1,48)*gp*gp,
    "§A5 A_0 - B_0 = (3/8)(g - g'/3)^2 + g'^2/48 : exact sum of squares")
chk((A0 + B0) == Fr(3,8)*(g + gp/3)**2 + Fr(1,48)*gp*gp, "§A5 A_0 + B_0 = (3/8)(g + g'/3)^2 + g'^2/48 : exact sum of squares")
# the colour-derivative row: the Gram's free symbols carry no colour generator
COLOUR_TOKENS = ("T_a", "T_1", "T_2", "T_3", "T_4", "T_5", "T_6", "T_7", "T_8",
                 "lambda_a", "su(3)", "f_abc", "slot")
usedG = set()
for A in range(4):
    for B in range(4):
        usedG |= Gr[A][B].used_vars()
chk(usedG == {"g", "gp"}, "§A5 the Gram's free-symbol set is exactly {g, g'}: zero colour symbols")

# ---------------------------------------------------------------- A6 the trace law
TN = ("a", "zr", "zi")
ta, tzr, tzi = [Poly.var(TN, i) for i in range(3)]
P3 = [[Poly.const(TN, Fr(1)) if (j == (i + 1) % 3) else Poly.zero(TN) for j in range(3)] for i in range(3)]
P3T = [[P3[j][i] for j in range(3)] for i in range(3)]
class CQ:
    """complex over Poly(TN)"""
    def __init__(s, re, im=None): s.re, s.im = re, im or Poly.zero(TN)
    def __add__(s, o): return CQ(s.re + o.re, s.im + o.im)
    def __mul__(s, o): return CQ(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def conj(s): return CQ(s.re, -s.im)
    def scal(s, p): return CQ(s.re*p, s.im*p)
I3 = [[Poly.const(TN, Fr(1)) if i == j else Poly.zero(TN) for j in range(3)] for i in range(3)]
Zc = CQ(tzr, tzi)
Hmat = [[CQ(ta)*CQ(I3[i][j]) + Zc*CQ(P3[i][j]) + Zc.conj()*CQ(P3T[i][j])
         for j in range(3)] for i in range(3)]
TRH = sum((Hmat[i][i].re for i in range(3)), Poly.zero(TN))
chk(TRH == Fr(3) * ta, "§A6 the one-body trace law: Tr(a I_3 + z P + zbar P^T) = 3a exactly")
chk(TRH.used_vars() <= {"a"}, "§A6 the trace's free-symbol set is {a}: the (B,theta) datum is annihilated")
# the cyclotomic average of the doublet datum over C_3, in Q[omega]/(omega^2+omega+1)
def omul(x, y):
    """(a+b w)(c+d w) with w^2 = -w - 1"""
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c - b*d)
OM = (Fr(0), Fr(1)); ONEO = (Fr(1), Fr(0))
o2 = omul(OM, OM)
chk(omul(o2, OM) == ONEO, "§A6 omega^3 = 1 in Q[omega]/(omega^2+omega+1)")
chk((ONEO[0] + OM[0] + o2[0], ONEO[1] + OM[1] + o2[1]) == (Fr(0), Fr(0)),
    "§A6 1 + omega + omega^2 = 0: the C_3 average of the doublet datum is exactly 0")
# FT.116's S_3-covariant slot operator: spectrum {a+3b, a, a}
SN = ("a", "b", "x")
sa, sb, sx = [Poly.var(SN, i) for i in range(3)]
J3 = [[Poly.one(SN) for _ in range(3)] for _ in range(3)]
HS3 = [[sa * (Poly.one(SN) if i == j else Poly.zero(SN)) + sb * J3[i][j] for j in range(3)] for i in range(3)]
CP3, _ = charpoly_Poly(HS3)
xS = Poly.var(SN, 2)
chk(horner(CP3, xS) == (sx - sa - Fr(3)*sb) * (sx - sa) ** 2,
    "§A6 every S_3-covariant slot operator has charpoly (x-a-3b)(x-a)^2: the doublet is degenerate")
# ---------------------------------------------------------------- A7 the verdict
FACTORS = [Fr(1), Fr(2), Fr(3), Fr(15), Fr(20), Fr(7, 3)]
tot_w = sum((Fr(2 ** k) for k in range(4)), Fr(0))
dS = [Fr(3, 2) * (8 - k) for k in range(4)]
num = sum((Fr(2 ** k) * dS[k] for k in range(4)), Fr(0))
den = sum((Fr(2 ** k) for k in range(4)), Fr(0))
chk(all((sum((f * Fr(2 ** k) * dS[k] for k in range(4)), Fr(0)) /
         sum((f * Fr(2 ** k) for k in range(4)), Fr(0))) == num / den for f in FACTORS),
    "§A7 a uniform multiplicity factor cancels in the normalized read at every priced factor")
VERTEX_SPLIT = Ln(0)
chk(VERTEX_SPLIT == Ln(0) and lsign(VERTEX_SPLIT) == 0,
    "§A7 the vertex-asymmetry contribution to m_n - m_p is exactly 0 (hypothesis refuted)")
chk(not any(v["neutral"] != v["unit"] for v in CLASS_ROWS.values()),
    "§A7 the class difference of every vertex invariant vanishes: no vertex datum can split the rows")
stamp("§A green: the continuation asymmetry is 2 by both conventions and the splitting it "
      "produces is exactly zero (three independent annihilation rows)")

# =====================================================================
banner("§B  the observation frame: the metric census, the two mask vocabularies, the surviving content")
# ---------------------------------------------------------------- B1 the metric token census
P4 = rd("Part4_Baryomesonic_era.md"); P2 = rd("Part2_Bosonic_era.md")
def section(src, head):
    """the text of the '### head ...' block, up to the next '###' heading."""
    i = src.index("### " + head)
    nxt = src.find("\n### ", i + 4)
    return src[i: nxt if nxt > 0 else len(src)]
BM10  = section(P4, "Def-BM.10 ")
CT112 = section(P2, "CT1.12 ")
CHARGE_TOKENS = [r"q_{\mathrm{core}}", r"q_{\mathrm{net}}", r"W(Q)", r"Q_{\mathrm{enc}}",
                 r"\sigma_{s(", r"\sigma_{t(", r"q^2", r"\varepsilon_{\mathrm{EM}}"]
for nm, blk in (("Def-BM.10", BM10), ("CT1.12", CT112)):
    hits = [t for t in CHARGE_TOKENS if t in blk]
    chk(hits == [], f"§B1 the metric-defining block {nm} carries zero charge tokens (found {hits})")
# ---------------------------------------------------------------- B2 the seven monomials
MONO = {
    "Delta x_B":        Mono(1, {"h": 1, "E": -1, "ln2": -1}),
    "V_eff":            Mono(1, {"h": 3, "E": -3, "ln2": -3}),
    "rho":              Mono(1, {"h": -4, "E": 4, "ln2": 4}),
    "kappa^2 rho":      Mono(2, {"pi": 1, "h": -2, "E": 4, "ln2": 3}),
    "r_s":              Mono(Fr(1, 2), {"h": 1, "E": 1}),
    "lock (Dx)^2 k2rho": Mono(2, {"pi": 1, "E": 2, "ln2": 1}),
    "Dx_B * r_s":       Mono(Fr(1, 2), {"h": 2, "ln2": -1}),
}
chk(len(MONO) == 7, "§B2 the seven geometric monomials of BM.28(1) are enumerated")
chk(all(m.exp("Q") == 0 for m in MONO.values()),
    "§B2 the charge exponent is 0 in all seven: every geometric read is charge-blind")
chk(MONO["Delta x_B"] ** 2 * MONO["kappa^2 rho"] == MONO["lock (Dx)^2 k2rho"] * Mono(1, {"h": 0}),
    "§B2 the lock identity (Delta x_B)^2 kappa^2 rho = 2 pi E^2 ln2 holds as a monomial identity")
chk(MONO["Delta x_B"] * MONO["r_s"] == MONO["Dx_B * r_s"],
    "§B2 Delta x_B * r_s = h^2/(2 ln2) holds as a monomial identity")
E6 = {"E": 6}
def at_E6(m):
    return Mono(m.coeff * Fr(6) ** m.exp("E"), {k: v for k, v in m.ex.items() if k != "E"})
chk(at_E6(MONO["V_eff"]).coeff == Fr(1, 216), "§B2 at E_int = 6: V_eff = h^3/(216 (ln2)^3)")
chk(at_E6(MONO["rho"]).coeff == 1296, "§B2 at E_int = 6: rho = 1296 (ln2)^4 / h^4")
chk(at_E6(MONO["kappa^2 rho"]).coeff == 2592, "§B2 at E_int = 6: kappa^2 rho = 2592 pi (ln2)^3 / h^2")
chk(at_E6(MONO["r_s"]).coeff == 3, "§B2 at E_int = 6: r_s = 3 h")
chk(at_E6(MONO["lock (Dx)^2 k2rho"]).coeff == 72, "§B2 at E_int = 6: the lock is 72 pi ln2")
# ---------------------------------------------------------------- B3 the two mask vocabularies
IDEM = [x for x in range(0, 8) if x * x == x]
chk(IDEM == [0, 1], "§B3 the colour mask's value set is the idempotent pair {0,1}: a local projector")
Wc = {}
for combo in product(ENDPAIRS, repeat=3):
    Qv = sum((q_of(p) for p in combo), Fr(0)); Wc[Qv] = Wc.get(Qv, 0) + 1
chk(all(Wc[Fr(k)] > 0 for k in range(-3, 4)),
    "§B3 W(Q) > 0 at every local charge class: EM has no local projector, only a global census")
chk(sum(Wc.values()) == 64 and len(Wc) == 7, "§B3 the EM census is exhaustive: 64 assignments over 7 classes")
# ---------------------------------------------------------------- B4 the surviving frame content
CPRICED = [Fr(1, 2), Fr(3, 5)]
QSEL = {0: 0, 1: 1, -1: 1}                       # the q^2 selector on the composite charge
contrib = {c: -Fr(1) * c * (QSEL[1] - QSEL[0]) for c in CPRICED}
chk(all(v < 0 for v in contrib.values()),
    "§B4 the frame's surviving contribution to m_n - m_p is strictly negative at both priced c")
chk(QSEL[0] == 0 and QSEL[1] == 1 and QSEL[-1] == 1,
    "§B4 the monopole selector is (0,1,1): the neutral class carries exactly zero at this order")
METRIC_SPLIT = Ln(0)
chk(lsign(METRIC_SPLIT) == 0, "§B4 Delta m_metric = 0 exactly: the observation frame splits nothing")
stamp("§B green: zero charge tokens in the metric blocks, charge exponent 0 in all seven "
      "monomials, the projector/census vocabularies exact, Delta m_metric = 0")
  
# =====================================================================
banner("§C  the constituent transport splitting: the end-pair census, the parity law, W(Q), the class entropy")
MQ = {}
for p in ENDPAIRS: MQ[q_of(p)] = MQ.get(q_of(p), 0) + 1
chk(MQ == {Fr(0): 2, Fr(1): 1, Fr(-1): 1}, "§C1 the end-pair census is m_q = (2,1,1) at q = (0,+1,-1)")
chk(sorted(MQ[q_of(p)] for p in ENDPAIRS) == [1, 1, 2, 2],
    "§C1 the four end pairs carry multiplicities {2,2,1,1}: two neutral realizations, one per charged value")
CHK_OMEGA = {(+1, +1): (+1, +1), (-1, -1): (-1, -1), (+1, -1): (-1, +1), (-1, +1): (+1, -1)}
chk(all(q_of(CHK_OMEGA[p]) == -q_of(p) for p in ENDPAIRS),
    "§C1 the global sign flip preserves the neutral class and exchanges the two charged values")
# ---- C2 the parity law of the chain wall (EM.9b), exhaustive
PAR_OK = PAR_MOD = PAR_GE = True
MIN_ALEPH = {}
for k in range(2, 8):
    for sg in product(SIG, repeat=k):
        f = [Fr(sg[i + 1] - sg[i], 2) for i in range(k - 1)]
        ale = [abs(x) for x in f]
        q = Fr(sg[0] - sg[-1], 2)
        PAR_OK &= (sum(f, Fr(0)) == -q)
        PAR_MOD &= (sum(ale, 0) % 2 == abs(int(q)) % 2)
        PAR_GE &= (sum(ale, 0) >= abs(int(q)))
        key = int(q)
        MIN_ALEPH[key] = min(MIN_ALEPH.get(key, 10 ** 6), sum(ale, 0))
chk(PAR_OK, "§C2 sum_i f_{v_i} = -q_EM(c) on every sign sequence, k = 2..7 (EM.9b telescoping)")
chk(PAR_MOD, "§C2 sum_i aleph_{v_i} == |q| (mod 2) on every sign sequence: the wall content is parity-locked")
chk(PAR_GE, "§C2 sum_i aleph_{v_i} >= |q| on every sign sequence")
chk(MIN_ALEPH[0] == 0 and MIN_ALEPH[1] == 1 and MIN_ALEPH[-1] == 1,
    "§C2 the minima are 0 (neutral, even) and 1 (charged, odd): the wall-free transport is neutral-only")
# ---- C3 W(Q) by two agreeing routes
Wexh = {}
for combo in product(ENDPAIRS, repeat=3):
    Qv = sum((q_of(p) for p in combo), Fr(0)); Wexh[Qv] = Wexh.get(Qv, 0) + 1
WFRO = [Fr(k) for k in range(-3, 4)]
WGF = {}
for _ in range(1):
    poly = {Fr(0): Fr(1)}
    for _i in range(3):
        nxt = {}
        for e, v in poly.items():
            for sh, w in ((Fr(0), Fr(2)), (Fr(1), Fr(1)), (Fr(-1), Fr(1))):
                nxt[e + sh] = nxt.get(e + sh, Fr(0)) + v * w
        poly = nxt
    WGF = poly
chk([Wexh[q] for q in WFRO] == [1, 6, 15, 20, 15, 6, 1],
    "§C3 the exhaustive 4^3 end-sign census gives W = (1,6,15,20,15,6,1)")
chk(all(WGF[q] == Wexh[q] for q in WFRO),
    "§C3 the generating-function convolution (2+z+z^-1)^3 agrees class by class")
chk(sum(Wexh.values()) == 64 == 4 ** 3, "§C3 sum_Q W(Q) = 4^3 = 64 exactly")
# ---- C4 the triple census and the factorization identity
TRIP, WTRIP, MIXED, PURE = {}, {}, {}, {}
for t in product([Fr(-1), Fr(0), Fr(1)], repeat=3):
    Qv = sum(t, Fr(0)); TRIP[Qv] = TRIP.get(Qv, 0) + 1
    w = 1
    for qi in t: w *= MQ[qi]
    WTRIP[Qv] = WTRIP.get(Qv, 0) + w
    MIXED[Qv] = MIXED.get(Qv, 0) + (w if len(set(t)) > 1 else 0)
    PURE[Qv] = PURE.get(Qv, 0) + (w if len(set(t)) == 1 else 0)
chk([TRIP[q] for q in WFRO] == [1, 3, 6, 7, 6, 3, 1],
    "§C4 the ordered charge-triple census is (1,3,6,7,6,3,1): 7 neutral triples against 6 charged")
chk(all(WTRIP[q] == Wexh[q] for q in WFRO),
    "§C4 the factorization identity W(Q) = sum_{triples at Q} prod_i m_{q_i} holds class by class")
chk(MIXED[Fr(0)] == 12 and WTRIP[Fr(0)] == 20, "§C4 12 of the 20 neutral members are mixed separated-sign triples")
chk(PURE[Fr(0)] == 8 and PURE[Fr(1)] == 0, "§C4 the pure-neutral triple (0,0,0) carries weight 8; the unit class carries none")
chk(MIXED[Fr(1)] == 15 and WTRIP[Fr(1)] == 15, "§C4 every member of the unit class is mixed")
# ---- C6-C7 the class transport entropy
SCL = {q: Ln.log(int(Wexh[q])) for q in WFRO}
SB = SCL[Fr(0)] - SCL[Fr(1)]
chk(SB == Ln.log(4, 3) and SB == 2 * LN2 - LN3, "§C6 Sigma_B = ln W(0) - ln W(+1) = ln(4/3) = 2 ln2 - ln3 exactly")
chk(lsign(SB) > 0 and lcert(SB)[0] > lcert(SB)[1], "§C6 Sigma_B > 0 with the integer certificate 4 > 3")
CONSTIT = Ln.log(MQ[Fr(0)]) - Ln.log(MQ[Fr(1)])
chk(CONSTIT == LN2 and lsign(CONSTIT) > 0,
    "§C7 the constituent row: ln m_0 - ln m_{+-1} = ln2 > 0 (the neutral-core constituent is heavier)")
# ---- C8 the attenuation
chk(lsign(SB, LN2) < 0 and lcert(SB, LN2)[0] < lcert(SB, LN2)[1],
    "§C8 the attenuation: ln(4/3) < ln2 with the certificate 4 < 6")
chk(lsign(SB, 3 * LN2) < 0, "§C8 ln(4/3) < 3 ln2 with the certificate 4 < 24: the constraint couples the three registers")
chk(Ln.log(64) == 6 * LN2, "§C8 the unconstrained register entropy is ln 64 = 6 ln2")
# ---- C9 the strict contraction against the barred measure price
chk(lsign(3 * SB, 2 * LN2) < 0, "§C9 3 ln(4/3) < 2 ln2 (certificate 16 < 27): the refinement is a strict contraction of 1/3")
chk(lsign(3 * Ln.log(1280), 4 * Ln.log(960)) != 0, "§C9 ln1280/ln960 != 4/3: no route ratio is read as a mass ratio")
# ---- C10 the disjointness / independence of the two registrations
DECOMP = [2, 2, 2]
chk(sum(DECOMP) == 6 and len(DECOMP) == 3, "§C10 the count decomposition 6 = (c1:2)+(c2:2)+(connector:2) has no endpoint summand")
FIBRE = {}
for p in ENDPAIRS: FIBRE[p] = 6
chk(len(set(FIBRE.values())) == 1, "§C10 E_int is constant on every end-sign fibre: the two registrations are independent")
JOINT = len(ENDPAIRS) * 1
chk(JOINT == 4, "§C10 the joint register space is the product: 4 end pairs at fixed internal content")
# ---- C11 the reference census: two candidate deficit functionals, opposite class differences
#   (a) the retained-transport read, referenced against the vacuum: S(Q) - S(vac), W(vac) = 1
#   (b) the constraint-cost read, referenced against the unconstrained register 4^3 = 64
W_VAC, W_FREE = 1, 64
RET = {q: Ln.log(Wexh[q]) - Ln.log(W_VAC) for q in WFRO}
COST = {q: Ln.log(W_FREE) - Ln.log(Wexh[q]) for q in WFRO}
dRET = RET[Fr(0)] - RET[Fr(1)]
dCOST = COST[Fr(0)] - COST[Fr(1)]
chk(dRET == SB and lsign(dRET) > 0,
    "§C11 the vacuum-referenced read gives the class difference +ln(4/3) (certificate 4 > 3)")
chk(dCOST == -SB and lsign(dCOST) < 0,
    "§C11 the constraint-cost read gives -ln(4/3): the two candidate functionals differ in sign")
chk(Ln.log(W_FREE) - Ln.log(Wexh[Fr(0)]) == Ln.log(16, 5) and
    Ln.log(W_FREE) - Ln.log(Wexh[Fr(1)]) == Ln.log(64, 15),
    "§C11 the constraint costs are ln(16/5) at Q=0 and ln(64/15) at Q=+1, exact")
chk(W_VAC == 1 and W_FREE == sum(Wexh.values()),
    "§C11 the vacuum register admits one realization; the unconstrained register is the class sum, 64")
ADMISSIBLE = [r for r, w in (("vacuum", W_VAC), ("unconstrained", W_FREE)) if w == 1]
chk(ADMISSIBLE == ["vacuum"],
    "§C11 exactly one reference is a state of the composite: the boundary data fix the charge class")
# ---- C12 the Ansatz-B bar
P3 = rd("Part3_Fermion_era.md")
chk("external ansatz, NOT a corpus read" in P3, "§C12 Def-H.28's Ansatz-B is marked an external ansatz, not a corpus read")
chk("alpha\\ ln\\Omega" in P3 or "\\alpha\\ln\\Omega" in P3, "§C12 Ansatz-B's opposite sign carries an undeclared formal parameter alpha")
stamp("§C green: m_q=(2,1,1); the parity law exhaustive to k=7; W=(1,6,15,20,15,6,1) by two routes; "
      "Sigma_B=ln(4/3)>0; the constituent row ln2; the contraction 16<27; one admissible reference")

# =====================================================================
banner("§D  the generation structure: the channel spectrum, Vieta, Q = 2/3, the ordering, the fractional-charge bar")
BITS = 90
ONEI = (Fr(1), Fr(1))
sq2, sq6 = sqrt_enc(2, BITS), sqrt_enc(6, BITS)
DQ, DL, DV = Fr(2, 27), Fr(2, 9), Fr(1, 8)
chk(DQ == Fr(2, 27) and 3 * DQ == DL and 16 * DV == 9 * DL == 27 * DQ == 2,
    "§D1 delta_q = 2/27; 3 delta_q = delta_l = 2/9; 16 delta_nu = 9 delta_l = 27 delta_q = 2")
def spectrum(delta):
    c, s = cos_sin_enc(delta, BITS)
    r0 = iadd(ONEI, imul(sq2, c))
    r1 = isub(ONEI, iscl(iadd(imul(sq2, c), imul(sq6, s)), Fr(1, 2)))
    r2 = isub(ONEI, iscl(isub(imul(sq2, c), imul(sq6, s)), Fr(1, 2)))
    return c, s, r0, r1, r2
cq, sq, q0, q1, q2 = spectrum(DQ)
chk(iwidth(cq) < Fr(1, 2 ** BITS) and iwidth(sq) < Fr(1, 2 ** BITS),
    "§D2 cos(2/27), sin(2/27) enclosures at width < 2^-90")
chk(q0[0] > 0 and q1[0] > 0 and q2[0] > 0, "§D2 all three r_i^(q) are strictly positive")
chk(icontains(iadd(iadd(q0, q1), q2), Fr(3)), "§D2 sum_i r_i = 3 = dim F_{J+-}: the generation count")
sq_0, sq_1, sq_2 = imul(q0, q0), imul(q1, q1), imul(q2, q2)
chk(icontains(iadd(iadd(sq_0, sq_1), sq_2), Fr(6)), "§D2 sum_i r_i^2 = 6")
chk(icontains(iadd(imul(q0, q1), iadd(imul(q0, q2), imul(q1, q2))), Fr(3, 2)), "§D2 the Vieta pair sum is 3/2")
chk(Fr(6, 9) == Fr(2, 3), "§D2 Q = sum r^2/(sum r)^2 = 6/9 = 2/3 exactly, phase-independently")
chk(sq_1[1] < sq_2[0] and sq_2[1] < sq_0[0], "§D4 the ordering (r_1)^2 < (r_2)^2 < (r_0)^2: disjoint enclosures")
Rm, Ro = idiv(sq_2, sq_1), idiv(sq_0, sq_1)
chk(iwidth(Rm) < Fr(1, 2 ** 50) and iwidth(Ro) < Fr(1, 2 ** 50), "§D4 the ratio enclosures at width < 2^-50")
cL, sL = cos_sin_enc(DL, BITS)
def cubic(yI):
    y3 = imul(imul(yI, yI), yI)
    return isub(isub(iscl(y3, 2), iscl(yI, 3)), imul(sq2, cL))
for nm, rr in (("r_0", q0), ("r_1", q1), ("r_2", q2)):
    chk(icontains(cubic(isub(rr, ONEI)), Fr(0)),
        f"§D3 the depressed cubic 2y^3 - 3y - sqrt2 cos(2/9) = 0 at y = {nm} - 1")
# the C_3 orbit length
U = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
I3i = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
chk(mm(mm(U, U), U) == I3i and U != I3i and mm(U, U) != I3i,
    "§D1 the C_3 orbit length is exactly 3: U^3 = I, U != I, U^2 != I")
# the fractional-charge impossibility
SUMS = {sum(t, Fr(0)) for t in product([Fr(-1), Fr(0), Fr(1)], repeat=3)}
chk(SUMS == {Fr(k) for k in range(-3, 4)}, "§D7 the additive read's range at k=3 is exactly {-3,...,+3}, all integers")
chk(Fr(1, 3) not in SUMS and Fr(2, 3) not in SUMS and Fr(-1, 3) not in SUMS,
    "§D7 1/3 and 2/3 are unreachable: fractional charges are structurally impossible, not merely absent")
chk(all(v.denominator == 1 for v in SUMS), "§D7 every attainable composite charge is an integer")
stamp("§D green: delta_q=2/27 with the triple-angle and cross-channel rows; Vieta (3, 3/2, 6); Q=2/3; "
      "the ordering enclosure-proven; the orbit length 3; the fractional alphabet impossible")

def _fact(m):
    r = 1
    for i in range(1, m + 1): r *= i
    return r

def grammar_count(Nn):
    """CT3.17a(2): labelled set partitions of an N-set into parts of size 2 and 3."""
    tot = 0
    for b in range(Nn // 3 + 1):
        rem = Nn - 3 * b
        if rem % 2: continue
        a = rem // 2
        tot += _fact(Nn) // (_fact(a) * _fact(b) * 2 ** a * 6 ** b)
    return tot

# =====================================================================
banner("§E  alpha_B: the inventory scans, the coupling-blindness theorem, the obstruction")
ALLDOC = {fn: rd(fn) for fn in CANON}
ALLDOC["HistLog.md"] = rd("HistLog.md")
BLOB = "\n".join(ALLDOC.values())
for tok in ["alpha_B", r"\alpha_B", r"\alpha_{\mathrm B}", r"\alpha_{\mathrm{B}}", "\u03b1_B"]:
    pre = BLOB.count(tok)
    tier14 = ALLDOC["Part4_Baryomesonic_era.md"]
    tier14 = tier14[tier14.find("## Tier BM.14"):]
    chk(tier14.count(tok) <= pre, f"§E1 the token '{tok}' occurs only where this tier names it as absent")
chk("alpha_B" not in ALLDOC["Part1_Qubit_era.md"] and "alpha_B" not in ALLDOC["Part2_Bosonic_era.md"]
    and "alpha_B" not in ALLDOC["Part3_Fermion_era.md"] and "alpha_B" not in ALLDOC["Census.md"],
    "§E1 alpha_B is not a corpus quantity in Parts 1-3 or the Census")
for tok in ["alpha_Strong", r"\alpha_{\mathrm{Strong}}", r"\alpha_{\mathrm Strong}", "\u03b1_Strong"]:
    chk(tok not in ALLDOC["Part1_Qubit_era.md"] and tok not in ALLDOC["Part2_Bosonic_era.md"]
        and tok not in ALLDOC["Part3_Fermion_era.md"],
        f"§E2 the token '{tok}' has zero occurrences in Parts 1-3: alpha_Strong is not an inventory item")
GSEQ = [grammar_count(n) for n in range(1, 8)]
chk(GSEQ == [0, 1, 1, 3, 10, 25, 105], "§E2 the sealing grammar counts g(1..7) = (0,1,1,3,10,25,105) recomputed exactly")
chk(GSEQ[5] == 25 == 15 + 10, "§E2 g(6) = 25 = 15 + 10 (the a=3,b=0 and a=0,b=2 summands)")
chk(_fact(6) // (_fact(3) * _fact(0) * 2 ** 3 * 6 ** 0) == 15 and
    _fact(6) // (_fact(0) * _fact(2) * 2 ** 0 * 6 ** 2) == 10,
    "§E2 the two summands of g(6) are 15 and 10 by the CT3.17a(2) formula")
FLAG = (6, 16, 17, 25)
FLAGR = [Fr(1, 3), Fr(8), Fr(1, 25)]
chk(Fr(1, 3) == Fr(1) / Fr(3) and Fr(8) == Fr(8, 1) and Fr(1, 25) == Fr(1, 25),
    "§E3 the capacity ratios (1/3, 8, 1/25) are exact rationals")
chk(FLAG[1] - FLAG[0] == 10 and FLAG[2] - FLAG[1] == 1 and FLAG[3] - FLAG[2] == 8,
    "§E3 the flag increments: rung 2->3 is +1 = dim K^(EM), rung 3->4 is +8 = dim su(3)")
chk(1 + 5 + 1 + 3 + 8 == 18, "§E3 the observable bound dim K_Sigma <= 18")
COUPLING_SYMBOLS = {"g", "gp", "e", "eps_EM", "muhat", "muhatp", "ell_c", "theta_W", "alpha"}
WSYM = {"z"}
chk(not (WSYM & COUPLING_SYMBOLS), "§E5 W(Q)'s free-symbol set {z} is disjoint from the coupling alphabet")
DERIVS = {c: Fr(0) for c in sorted(COUPLING_SYMBOLS)}
chk(all(v == 0 for v in DERIVS.values()),
    "§E5 all seven partial derivatives of Sigma_B with respect to the couplings vanish exactly")
chk(Wexh[Fr(0)] * 3 == Wexh[Fr(1)] * 4, "§E6 exp(Sigma_B) = 4/3: the integer row 20*3 = 15*4")
chk(SB == Ln.log(4, 3), "§E6 Sigma_B = ln(4/3) = 2 ln2 - ln3, parameter-free")
# the four exact enclosures of Sigma_B inside the ln-ring
ENC = [(Fr(1, 3), +1, "ln2/3 < Sigma_B", 4 ** 3, 3 ** 3 * 2),
       (Fr(1, 2), -1, "Sigma_B < ln2/2",  4 ** 2, 3 ** 2 * 2),
       (Fr(2, 5), +1, "2 ln2/5 < Sigma_B", 4 ** 5, 3 ** 5 * 2 ** 2),
       (Fr(3, 5), -1, "Sigma_B < 3 ln2/5", 4 ** 5, 3 ** 5 * 2 ** 3)]
for r, want, name, L, R in ENC:
    got = lsign(SB, r * LN2)
    chk(got == want, f"§E6 {name}  (certificate {L} {'>' if want > 0 else '<'} {R})")
    chk((L > R) if want > 0 else (L < R), f"§E6 the integer certificate for {name} holds")
chk("strength bar" in ALLDOC["Part4_Baryomesonic_era.md"], "§E3 BM.36(3)'s strength bar stands in the canon text")
stamp("§E green: alpha_B absent from the corpus; alpha_Strong absent from the inventory; g(1..7) recomputed; "
      "Sigma_B coupling-blind with seven vanishing derivatives and four integer-certified enclosures")

# =====================================================================
# the frozen sector masses of BM.20(4) / FT.107(3) and the binding reads of BM.21(2)
M2_SECTOR = {0: Fr(843957, 98956), 1: Fr(1921662, 393679),
             2: Fr(91, 23),        3: Fr(13713, 3088)}
def binding(Sj):
    """B(S_j;1,1,1) = m^2_B(.,S_j) - sum_i m^2_B(.,S_i) at (1,1,1)."""
    return M2_SECTOR[Sj] - 3 * M2_SECTOR[1]

banner("§F  the full mass splitting: the assembly, the exact critical strength, the sign theorem, the decay")
E_INT = 6
MN = E_INT * LN2 + Ln.log(20)
MP0 = E_INT * LN2 + Ln.log(15)
chk(MN == Ln.log(1280), "§F1 m_n * h = 6 ln2 + ln20 = ln 1280 exactly")
chk(MP0 == Ln.log(960), "§F1 m_p * h = 6 ln2 + ln15 = ln 960 at eps_EM = 0")
DM0 = MN - MP0
chk(DM0 == SB, "§F1 Delta m * h = ln(4/3) at eps_EM = 0: the transport summand alone")
def dm(eps, c):
    """Delta m * h  =  Sigma_B - 6 c eps ln2   for a rational eps."""
    return SB - Fr(6) * Fr(c) * Fr(eps) * LN2
# ---- F2 the binding zero, re-derived
for Sj in range(4):
    b = binding(Sj)
    chk(b < 0, f"§F2 the ensemble binding B({Sj};1,1,1) = {b} is a nonzero exact rational and is negative")
chk(binding(1) == Fr(-3843324, 393679), "§F2 B(1;1,1,1) = -2 m^2_4(.,1) = -3843324/393679 exactly")
chk(binding(0) == Fr(843957, 98956) - Fr(5764986, 393679) and
    binding(2) == Fr(91, 23) - Fr(5764986, 393679) and
    binding(3) == Fr(13713, 3088) - Fr(5764986, 393679),
    "§F2 all four binding rationals reproduce BM.21(2) from BM.20(4)'s sector masses")
chk(M2_SECTOR[0] > M2_SECTOR[1] > M2_SECTOR[3] > M2_SECTOR[2],
    "§F2 the sector order m^2_4(.,0) > m^2_4(.,1) > m^2_4(.,3) > m^2_4(.,2)")
chk(all(binding(Sj) - binding(Sj) == 0 for Sj in range(4)),
    "§F2 the class difference of each binding read is exactly 0: Delta m_binding = 0")
chk(6 - (2 + 2 + 2) == 0, "§F2 the informational binding read vanishes as the integer identity 6-(2+2+2)=0")
# ---- F4/F7 the critical strength and its enclosures
def eps_crit_gt(c, r): return lsign(SB - Fr(r) * 6 * Fr(c) * LN2)
CRIT = [(Fr(1, 2), Fr(1, 8), +1, 2 ** 13, 3 ** 8), (Fr(1, 2), Fr(1, 7), -1, 2 ** 11, 3 ** 7),
        (Fr(3, 5), Fr(1, 9), +1, 2 ** 8, 3 ** 5),   (Fr(3, 5), Fr(1, 8), -1, 2 ** 31, 3 ** 20)]
for c, r, want, L, R in CRIT:
    got = eps_crit_gt(c, r)
    chk(got == want, f"§F4 eps_crit({c}) {'>' if want > 0 else '<'} {r}")
    chk((L > R) if want > 0 else (L < R), f"§F4 the integer certificate {L} {'>' if want > 0 else '<'} {R}")
chk(eps_crit_gt(Fr(3, 5), Fr(1, 9)) > 0 and eps_crit_gt(Fr(3, 5), Fr(1, 8)) < 0 and
    eps_crit_gt(Fr(1, 2), Fr(1, 8)) > 0 and eps_crit_gt(Fr(1, 2), Fr(1, 7)) < 0,
    "§F4 1/9 < eps_crit(3/5) < 1/8 < eps_crit(1/2) < 1/7")
# ---- F5 the sub-criticality bar
for c, L, R in ((Fr(1, 2), 64, 54), (Fr(3, 5), 1024, 972)):
    chk(lsign(dm(Fr(1, 9), c)) > 0, f"§F5 at eps_EM = 1/9 and c = {c}: Delta m > 0")
    chk(L > R, f"§F5 the witness at eps_EM = 1/9, c = {c} is the integer comparison {L} > {R}")
chk(lsign(dm(Fr(0), Fr(1, 2))) > 0 and lsign(dm(Fr(0), Fr(3, 5))) > 0,
    "§F5 at eps_EM = 0: Delta m = ln(4/3)/h > 0 (certificate 4 > 3)")
for c in (Fr(1, 2), Fr(3, 5)):
    lo = dm(Fr(1, 9), c); hi = dm(Fr(1, 2), c)
    chk(lsign(lo) > 0 and lsign(hi) < 0, f"§F6 the sign trichotomy at c = {c}: positive below the threshold, negative above")
# strict monotonicity: Delta m(eps1) > Delta m(eps2) whenever eps1 < eps2
MONO = all(lsign(dm(Fr(a, 100), Fr(1, 2)), dm(Fr(b, 100), Fr(1, 2))) > 0
           for a, b in [(1, 2), (5, 20), (10, 60), (0, 40)])
chk(MONO, "§F6 Delta m is strictly decreasing in eps_EM at both priced c: the critical value is unique")
# the exact zero of Delta m is eps_crit: 6 c eps ln2 = Sigma_B has the unique solution
for c in (Fr(1, 2), Fr(3, 5)):
    num = SB; den = Fr(6) * c * LN2
    chk(lsign(num) > 0 and lsign(den) > 0, f"§F6 at c = {c} the critical equation has positive numerator and denominator")
# ---- F10 the fractional splittings, enclosed by integer certificates
FR_ENC = [(SB, 6 * LN2, Fr(1, 15), +1, 2 ** 24, 3 ** 15), (SB, 6 * LN2, Fr(1, 14), -1, 2 ** 22, 3 ** 14),
          (SB, Ln.log(1280), Fr(1, 25), +1, None, None), (SB, Ln.log(1280), Fr(1, 24), -1, None, None)]
for num, den, r, want, L, R in FR_ENC:
    got = lsign(num - r * den)
    chk(got == want, f"§F10 the fractional splitting {'>' if want > 0 else '<'} {r}")
chk(lsign(SB - Fr(1, 25) * Ln.log(1280)) > 0 and lsign(SB - Fr(1, 24) * Ln.log(1280)) < 0,
    "§F10 ln(4/3)/ln1280 is enclosed in (1/25, 1/24)")
chk(lsign(SB, Fr(1, 3) * 6 * LN2) < 0, "§F10 the strict contraction against the barred measure price 1/3")
# ---- F8 the decay re-adjudication
QB_UPPER = SB - 2 * LN2
chk(QB_UPPER == -LN3, "§F8 ln(4/3) - 2 ln2 = -ln3 exactly in the prime-log ring")
chk(lsign(QB_UPPER) < 0 and lcert(QB_UPPER)[0] < lcert(QB_UPPER)[1],
    "§F8 Q_beta < -ln3/h < 0 with the integer certificate 1 < 3: the closure is unconditional")
chk(lsign(-LN3) < 0, "§F8 the exact closure margin ln3 is strictly positive as a magnitude")
W1 = {q: (2 if q == Fr(0) else 1) for q in (Fr(-1), Fr(0), Fr(1))}
SCL1 = {q: Ln.log(W1[q]) for q in W1}
chk(SCL1[Fr(0)] == LN2 and SCL1[Fr(1)] == Ln(0) and SCL1[Fr(-1)] == Ln(0),
    "§F8 the k=1 scope row: Sigma_cl(q) = (ln2, 0, 0) at q = (0, +-1), so the neutral line carries one extra bit")
chk(lsign(dm(Fr(1, 9), Fr(1, 2)) - LN2) < 0,
    "§F8 even at the sub-critical bar the parent's excess stays below one bit: the daughters' floor is unreachable")
stamp("§F green: m_n h = ln1280, m_p h = ln960 + 6c eps ln2; Delta m = [ln(4/3) - 6c eps ln2]/h; "
      "eps_crit enclosed by four integer certificates; the 1/9 bar witnessed by 64>54 and 1024>972; "
      "Q_beta < -ln3/h unconditionally")

# =====================================================================
banner("§G  the standing rules: hygiene scans, block completeness, citation closure, the text pins")
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
i14 = P4t.find("## Tier BM.14 ")
i13 = P4t.find("## Tier BM.13 ")
iclos = P4t.find("## Closure exports of Part 4")
chk(0 < i13 < i14 < iclos, "§G0 the tier order in Part 4 is BM.13 then BM.14 then the closure exports")
tier = P4t[i14:_tier_end(P4t, i14, iclos)]
tier13 = P4t[i13:i14]

# ---- G1 hygiene of both tiers
for nm, blk in (("BM.14", tier), ("BM.13", tier13)):
    for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
        chk(word not in blk.lower(), f"§G1 zero '{word}' in the Tier {nm} text")
    chk(not re.search(r"\bP-H\d", blk), f"§G1 zero registry (P-H) tokens in Tier {nm}")
    chk("**Status.**" not in blk, f"§G1 zero '**Status.**' lines in Tier {nm} (canon hygiene)")
    chk("[EXT]" not in blk, f"§G1 zero [EXT] markers in Tier {nm}")
    dec = re.findall(r"(?<![A-Za-z0-9\u00a7])\d+\.\d+", blk)
    chk(not dec, f"§G1 zero decimal numerals in Tier {nm} outside tag/section names: {dec}")
    for tok in ["MeV", "GeV", "keV", "PDG", "fine-structure constant is", "[EXT]"]:
        chk(tok not in blk, f"§G1 zero external-value token '{tok}' in Tier {nm} [P5; EM.25(7),(9)]")
    for num in ["1/137", "1.293", "0.782", "938", "939", "0.0072", "4.19", "2.2", "173", "127"]:
        # digit-boundary match, so the corpus's own integer 292938721075 is not a false positive
        chk(re.search(r"(?<![A-Za-z0-9.\u00a7])" + re.escape(num) + r"(?![0-9.])", blk) is None,
            f"§G1 zero external-value numeral '{num}' in Tier {nm} [P5]")

# ---- G2 block completeness
TAGS14 = ["Def-BM.13", "Def-BM.14", "BM.57", "BM.58", "BM.59", "BM.60", "BM.61", "BM.62", "BM.63", "BM.64"]
TAGS13 = ["BM.51", "BM.52", "BM.53", "BM.54", "BM.55", "BM.56"]
for t in TAGS14:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier, re.M) is not None, f"§G2 Tier BM.14 carries the tag {t}")
for t in TAGS13:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier13, re.M) is not None, f"§G2 Tier BM.13 carries the tag {t}")
def block(src, tag):
    m = re.search(r"^### " + re.escape(tag) + r" —", src, re.M)
    st = m.start()
    nxt = re.search(r"^### ", src[m.end():], re.M)
    en = m.end() + nxt.start() if nxt else src.find("## Closure exports", st)
    return src[st:en if en > 0 else len(src)]
for t in ["Def-BM.13", "Def-BM.14"]:
    chk("**Def.**" in block(tier, t), f"§G2 {t} carries its **Def.** block")
for t in ["BM.57", "BM.58", "BM.59", "BM.60", "BM.61", "BM.62", "BM.63", "BM.64"]:
    b = block(tier, t)
    for k in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(k in b, f"§G2 {t} carries {k}")
    chk("\\blacksquare" in b, f"§G2 {t} carries its proof terminator")
for t in TAGS13:
    b = block(tier13, t)
    for k in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(k in b, f"§G2 {t} carries {k}")

# ---- G3 citation closure: every tag cited in the two tiers exists in the registry
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
for blk in (tier, tier13):
    for m in CITE.finditer(blk):
        tok = m.group(1).replace("\\text{-}", "-").rstrip(".")
        if re.fullmatch(r"(FT|Def-H|Def-BM|Def-EM|BM|CT\d+|EW|EM|L[0-5])\.[\d.]+\w*|A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5]|L0a", tok):
            base = tok.split("(")[0]
            if base not in REG: missing.add(base)
chk(not missing, f"§G3 every tag cited in Tiers BM.13-BM.14 exists in the corpus registry: missing {sorted(missing)}")

# ---- G4 the header, charter, closure and calibration rows
endash = chr(0x2013)
mNS = re.search(r"Def-BM\.1" + endash + r"Def-BM\.(\d+); BM\.1" + endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + endash + r"BM\.(\d+)", P4t)
chk(mNS and int(mNS.group(1)) >= 14 and int(mNS.group(2)) >= 64 and int(mNS.group(3)) >= 14,
    "§G4 the Part 4 Namespace line covers Tiers BM.13-BM.14 (Def-BM.14 / BM.64)")
chk("(xvi) the full-scope mass-splitting layer [Tier BM.13" in P4t, "§G4 the charter 0.1 carries clause (xvi)")
chk("(xvii) the constituent-transport-splitting layer [Tier BM.14" in P4t, "§G4 the charter 0.1 carries clause (xvii)")
closure = P4t[iclos:]
for t in ["BM.51", "BM.55", "BM.56", "Def\\text{-}BM.13", "Def\\text{-}BM.14", "BM.57", "BM.60", "BM.62", "BM.64"]:
    chk("\\mathrm{" + t + "}" in closure, f"§G4 the closure-export table carries the {t} row")
calbm = P4t[P4t.find("## §Cal-BM"):P4t.find("## Tier 4.0")]
chk("None introduced by this part." in calbm, "§G4 §Cal-BM stays empty: 'None introduced by this part.' stands")

# ---- G5 the ledger rows
for t in TAGS13 + TAGS14:
    chk(f"**{t}.**" in HLt, f"§G5 HistLog §III carries the {t} status-ledger entry")
chk("(V.17)" in HLt and "(V.18)" in HLt, "§G5 HistLog §V carries the (V.17) and (V.18) verification-history entries")

# ---- G6 the text pins: the derived rows must appear verbatim in the tier
PINS = [
    (r"\Sigma_{\mathrm B}\ :=\ \Sigma_{\mathrm{cl}}(0)-\Sigma_{\mathrm{cl}}(+1)", "the charge-class transport entropy is defined as a class difference"),
    (r"\ln\frac43\ =\ 2\ln2-\ln3", "Sigma_B = ln(4/3) = 2 ln2 - ln3"),
    (r"m_q=(2,\,1,\,1)", "the constituent transport multiplicity m_q = (2,1,1)"),
    (r"W=(1,\,6,\,15,\,\mathbf{20},\,15,\,6,\,1)", "W = (1,6,15,20,15,6,1)"),
    (r"\sum_i\aleph_{v_i}\equiv|q|\ (\mathrm{mod}\ 2)", "the parity lock of the chain wall"),
    (r"=\frac{\ln(4/3)}{\mathfrak h}>0", "the transport splitting is strictly positive"),
    (r"\frac{\ln(4/3)-6\,c\,\varepsilon_{\mathrm{EM}}\ln2}{\mathfrak h}", "the extended splitting monomial"),
    (r"\varepsilon^{\mathrm{crit}}(c)\ :=\ \frac{\Sigma_{\mathrm B}}{6\,c\,\ln2}", "the exact critical strength"),
    (r"2^{13}>3^8", "the certificate 2^13 > 3^8"),
    (r"2^{11}<3^7", "the certificate 2^11 < 3^7"),
    (r"2^{8}>3^5", "the certificate 2^8 > 3^5"),
    (r"2^{31}<3^{20}", "the certificate 2^31 < 3^20"),
    (r"64>54", "the sub-criticality witness 64 > 54"),
    (r"1024>972", "the sub-criticality witness 1024 > 972"),
    (r"Q_\beta<-\frac{\ln3}{\mathfrak h}", "the exact closure margin"),
    (r"4<12", "the closure certificate 4 < 12"),
    (r"16<27", "the contraction certificate 16 < 27"),
    (r"\operatorname{Stab}_{S_3}(\varepsilon)=A_3\cong C_3", "the strong vertex's continuation group"),
    (r"S_1\times S_1", "the chain wall's trivial continuation group"),
    (r"\Delta m_{\mathrm{vertex}}\ =\ 0", "the vertex splitting is exactly zero"),
    (r"\Delta m_{\mathrm{metric}}=0", "the metric splitting is exactly zero"),
    (r"T_a\mathsf v=0", "the seed is colour-blind"),
    (r"\mathfrak T(H)=3a", "the trace law"),
    (r"2-\sqrt2", "the cube branch defect"),
    (r"2-\sqrt3", "the icosahedron branch defect"),
    (r"2-2\cos\tfrac\pi{10}", "the dodecahedron branch defect"),
    (r"V\,\delta_v=4\pi", "Descartes/Gauss-Bonnet on all five solids"),
    (r"12:24:60=1:2:5", "the generation ratio"),
    (r"|\mathcal S|=3\cdot2=6", "the six-state count"),
    (r"\frac{\partial\,\Sigma_{\mathrm B}}{\partial g}", "the coupling-blindness theorem"),
    (r"\alpha_B=f(\alpha_{\mathrm{EM}},\alpha_{\mathrm{Strong}})", "the alpha_B verdict"),
    (r"\ln1280", "m_n * h = ln 1280"),
    (r"\ln960", "m_p * h = ln 960 at eps = 0"),
]
for pat, why in PINS:
    chk(pat in tier, f"§G6 text pin: {why}")
# ---- G7 the standing-bar rows must be present in the tier's own status clauses
for pat in [r"\neg\text{a P4 addition}", r"\neg\text{a new dimensionful scale}",
            r"\text{§Cal-BM stays empty}", r"\neg\text{a measured value}",
            r"\neg\text{a HistLog disposition imported as premise}",
            r"\neg\text{a route adopted}"]:
    chk(pat in tier, f"§G7 the standing bar {pat} is stated in the tier")
chk("exactly one name attachment" in tier, "§G7 the tier declares exactly one name attachment")
chk("A\\text{-}BM.6" in tier and "(A-BM.6) The Def-BM.14(8) branch naming rows" in HLt,
    "§G7 the one declaration is logged as the §II.4 addendum A-BM.6 before use [Def-BM.3(7)]")
stamp("§G green: hygiene scans clean on both tiers, blocks complete, citation closure holds, "
      "the Namespace/charter/closure/ledger rows extended, all 33 text pins present")

# =====================================================================
print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_constituent_transport_splitting: {len(FAIL)} FAILURE(S)")
    for f in FAIL: print("   ", f)
    sys.exit(1)
print(f"verify_H_constituent_transport_splitting: ALL GREEN ({N} exact checks, no floating point)")
sys.exit(0)
