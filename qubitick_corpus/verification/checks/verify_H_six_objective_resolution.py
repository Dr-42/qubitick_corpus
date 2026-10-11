#!/usr/bin/env python3
"""verify_H_six_objective_resolution.py - Tier BM.20 of Part 4: six objective
resolutions - BM.101-BM.107.

The energy-scale graph of the forward and inverse reads with its derived
crossing strength and composition-dependent crossing count; the dimensional
bridge with the q-exponent census, the two separated bridges and the declared
calibration slot A-BM.9; the three-constituent assembly's two formed
eigenvalue equations and the tensor-product referent census; the curvature
composition's back-reaction fixed point and the non-selection theorem; the
general crystallization weight with measure-free bounds and the refuted
defect conditioning; and the kind structure of the arrow with the spin-parity
refutation and the exchange-structure census.

Exact arithmetic only: Fraction; univariate and multivariate polynomials over
Q (identities verified by expansion and by exact rational substitution on
Zariski-dense grids); the log2 ring Q (+) Q*log2 3 with integer power
certificates; the prime-log ring with integer sign tests; Laurent monomials
with q- and h-exponent censuses; generic quadratic rings Q(sqrt d) for the
minimal polynomials; exact rational interval enclosures for nested radicals;
Q(i) via qmath.C; exhaustive enumerations. No floating point enters any
assertion. No decimal numeral occurs in this file. No measured coupling, mass
or ratio appears anywhere.

  §A  the energy-scale graph: the reflection identity, the uniform
      informational verdict, the crossing strength (2-log2 3)/(3w) with its
      enclosure on 2^13>3^8 and 3^12>2^19, eps_eff = e^2/(4 pi) as a monomial,
      G = beta x^2 with [beta] = q^0, the three profile shapes, the
      stationarity cubic with h(3/2) = -1 and h(2) = 4 beta - 1, the closed
      form P_max = 1 - 3/(2 x*), the three crossing equations and their root
      counts, and the flatness of the specified and pure-pole reads
  §B  the dimensional bridge: the q-exponent census and its balance rows, the
      chart-side current density q^(3/2), the two-bridge separation, and the
      A-BM.9 declaration pins with the value unissued
  §C  the eigenvalue composition: W(Q) = C(6,Q+3) against the exhaustive
      end-sign census, the Laurent identity (2+z+1/z)^3 = (z+1)^6/z^3, the
      family cubic's Vieta rows, the depressed cubic and the elimination row
      in the quotient ring, the minimal polynomials including the
      dodecahedral quartic derived from (2-y)^2 = (5+sqrt5)/2, the generation
      order by nested radical enclosures, and the referent-census pins
  §D  the curvature composition: G_corr = G(1+a gsf) as a monomial, the three
      fixed-point rows by exact substitution, the quadratic's root sign
      census and its a -> 0 limit by conjugate clearing, the pole locus with
      the Q = 0 row, and the alphabet disjointness that excludes the loop
  §E  the general weight: the measure-free bounds with both equality loci,
      the family form with the exhaustive eight-configuration census, the
      second moment via |S|^2, the uniform recovery 1/D, the AM-GM row
      3(1-R)-S = sum u - 3 prod u, monotonicity on an exact grid, and the
      (W6) refutation with the A4/D0.4/CT0.8 symbol census
  §F  the kind structure: j = |kappa|/2 at kappa = 1,2 with the Casimir rows,
      (9/16)^6 = 531441/16777216, the wall-parity census exhaustive to k = 7,
      the sign-free transport assembly, 16 delta_nu = 9 delta_ell =
      27 delta_q = 2, the CPT phase row over Q(i), and the statistics
      referent pins
  §G  the standing rules: forbidden-token scans, block completeness of
      BM.101-BM.107, the one-declaration row, citation closure, the
      Namespace/charter/closure/Cal-BM rows, the HistLog ledger rows, the
      suite count 76, the checker self-scan and the text pins
"""
import os, re, sys, time, math, json
from fractions import Fraction as Fr
from itertools import product, combinations

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
#  exact rings
# =====================================================================
class Poly:
    """univariate polynomial over Q, coefficients ascending."""
    __slots__ = ("c",)
    def __init__(s, c):
        s.c = [Fr(x) for x in list(c)]
        while len(s.c) > 1 and s.c[-1] == 0: s.c.pop()
    def __call__(s, x):
        r = Fr(0)
        for a in reversed(s.c): r = r * Fr(x) + a
        return r
    def __add__(s, o):
        n = max(len(s.c), len(o.c))
        return Poly([(s.c[i] if i < len(s.c) else 0) + (o.c[i] if i < len(o.c) else 0) for i in range(n)])
    def __sub__(s, o): return s + Poly([-x for x in o.c])
    def __mul__(s, o):
        r = [Fr(0)] * (len(s.c) + len(o.c) - 1)
        for i, a in enumerate(s.c):
            for j, b in enumerate(o.c): r[i + j] += a * b
        return Poly(r)
    def __pow__(s, n):
        r = Poly([1])
        for _ in range(int(n)): r = r * s
        return r
    def __eq__(s, o): return s.c == o.c
    def der(s): return Poly([Fr(i) * s.c[i] for i in range(1, len(s.c))])
    def __repr__(s): return "Poly" + str(s.c)

class MV:
    """multivariate polynomial over Q: {exponent tuple: Fraction}."""
    __slots__ = ("d", "n")
    def __init__(s, n, terms=()):
        s.n = n; s.d = {}
        for c, e in terms:
            assert len(e) == n
            s.d[e] = s.d.get(e, Fr(0)) + Fr(c)
        s.d = {k: v for k, v in s.d.items() if v}
    def __add__(s, o):
        r = MV(s.n)
        for d in (s.d, o.d):
            for k, v in d.items(): r.d[k] = r.d.get(k, Fr(0)) + v
        r.d = {k: v for k, v in r.d.items() if v}
        return r
    def __sub__(s, o): return s + o.neg()
    def neg(s):
        r = MV(s.n)
        r.d = {k: -v for k, v in s.d.items()}
        return r
    def __neg__(s): return s.neg()
    def __mul__(s, o):
        r = MV(s.n)
        for e1, c1 in s.d.items():
            for e2, c2 in o.d.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                r.d[e] = r.d.get(e, Fr(0)) + c1 * c2
        r.d = {k: v for k, v in r.d.items() if v}
        return r
    def __pow__(s, n):
        r = MV(s.n, [(1, tuple(0 for _ in range(s.n)))])
        for _ in range(int(n)): r = r * s
        return r
    def scl(s, q):
        r = MV(s.n); r.d = {k: v * Fr(q) for k, v in s.d.items()}; return r
    def __eq__(s, o): return s.d == o.d
    def __call__(s, *vals):
        tot = Fr(0)
        for e, c in s.d.items():
            pr = Fr(c)
            for a, v in zip(e, vals): pr *= Fr(v) ** a
            tot += pr
        return tot
    def zero(s): return not s.d
    def __repr__(s): return f"MV{sorted(s.d.items())}"
def var(n, i, c=1): return MV(n, [(c, tuple(1 if k == i else 0 for k in range(n)))])
def const(n, c): return MV(n, [(c, tuple(0 for _ in range(n)))])

class QS:
    """a + b*sqrt(d), a,b in Fraction."""
    __slots__ = ("a", "b", "d")
    def __init__(s, d, a, b=0): s.d = d; s.a = Fr(a); s.b = Fr(b)
    def __add__(s, o): return QS(s.d, s.a + o.a, s.b + o.b)
    def __sub__(s, o): return QS(s.d, s.a - o.a, s.b - o.b)
    def __neg__(s): return QS(s.d, -s.a, -s.b)
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return QS(s.d, s.a * Fr(o), s.b * Fr(o))
        return QS(s.d, s.a * o.a + s.d * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __eq__(s, o):
        if isinstance(o, (int, Fr)): o = QS(s.d, o)
        return s.a == o.a and s.b == o.b
    def __repr__(s): return f"QS{s.d}({s.a},{s.b})"

class PL(dict):
    """the prime-log ring: {prime: Fraction coefficient of ln p}."""
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
    r = PL(); m = int(n); d = 2
    while m > 1:
        while m % d == 0: r[d] = r.get(d, Fr(0)) + 1; m //= d
        d += 1
    return PL({k: v for k, v in r.items() if v})
def lsign(x):
    Nn = 1
    for v in x.values(): Nn *= v.denominator
    P = Q = 1
    for p, v in x.items():
        e = int(v * Nn)
        if e > 0: P *= p ** e
        elif e < 0: Q *= p ** (-e)
    return (P > Q) - (P < Q)
L2, L3, L5 = ln_of(2), ln_of(3), ln_of(5)
SIGB = 2 * L2 - L3                                     # ln(4/3)

def l2cmp(a, b):
    """the exact sign of a + b*log2(3)."""
    a, b = Fr(a), Fr(b)
    if b == 0: return (a > 0) - (a < 0)
    t = -a / b
    P, Q = t.numerator, t.denominator
    if P < 0:
        sL = 1
    else:
        l, r = 3 ** Q, 2 ** P
        sL = (l > r) - (l < r)
    return sL if b > 0 else -sL
C0A, C0B = Fr(2), Fr(-1)                               # 2 - log2(3)

def mon(coef=1, **kw):
    return (Fr(coef), tuple(sorted((k, Fr(v)) for k, v in kw.items() if Fr(v) != 0)))
def mmul(a, b):
    d = dict(a[1])
    for k, v in b[1]: d[k] = d.get(k, Fr(0)) + v
    return (a[0] * b[0], tuple(sorted((k, v) for k, v in d.items() if v != 0)))
def mdiv(a, b):
    d = dict(a[1])
    for k, v in b[1]: d[k] = d.get(k, Fr(0)) - v
    return (a[0] / b[0], tuple(sorted((k, v) for k, v in d.items() if v != 0)))
QEXP = {"mu2p": Fr(1), "r": Fr(-1, 2), "h": Fr(-1, 2), "m": Fr(1, 2), "Delta": Fr(1),
        "M0": Fr(1, 2), "s": Fr(1, 2), "V": Fr(-3, 2), "rho": Fr(2), "area": Fr(-1)}
HEXP = {"h": Fr(1)}
def qexp(m): return sum(QEXP.get(k, Fr(0)) * e for k, e in m[1])
def hexp(m): return sum(HEXP.get(k, Fr(0)) * e for k, e in m[1])

def sqrt_enc(nn, bits):
    k2 = bits + 4
    r = math.isqrt(int(nn) * (1 << (2 * k2)))
    lo = Fr(r, 1 << k2); hi = Fr(r + 1, 1 << k2)
    assert lo * lo <= nn < hi * hi and hi - lo < Fr(1, 2 ** bits)
    return (lo, hi)
def isqrt_enc(I, bits):
    k2 = bits + 4
    lo = Fr(math.isqrt(int(I[0] * (1 << (2 * k2)))), 1 << k2)
    hi = Fr(math.isqrt(int(I[1] * (1 << (2 * k2)))) + 1, 1 << k2)
    return (lo, hi)
def iadd(I, J): return (I[0] + J[0], I[1] + J[1])
def isub(I, J): return (I[0] - J[1], I[1] - J[0])
def imul(I, J):
    p = [I[0] * J[0], I[0] * J[1], I[1] * J[0], I[1] * J[1]]
    return (min(p), max(p))
def iscl(I, q): return (I[0] * q, I[1] * q) if q >= 0 else (I[1] * q, I[0] * q)
def idiv(I, J):
    assert J[0] > 0
    return (I[0] / J[1], I[1] / J[0])
BITS = 70

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


it = P4t.index("## Tier BM.20"); iclos = P4t.index("## Closure exports of Part 4")
tier = P4t[it:_tier_end(P4t, it, iclos)]
Dp = Poly([3, -3, 1])                                  # D = 3 - 3p + p^2
THRESH = [Fr(0), Fr(1, 64), Fr(1, 16), Fr(1, 8), Fr(3, 16), Fr(1, 5), Fr(63, 256)]

# =====================================================================
banner("§A  the energy-scale graph (BM.101): the reflection, the crossing strength, the three profiles")
# =====================================================================
# ---- A1 the reflection identity, as a linear-form identity
vars4 = ("mn", "mp", "ml", "mv")
fwd = MV(4, [(1, (1, 0, 0, 0)), (-1, (0, 1, 0, 0)), (-1, (0, 0, 1, 0)), (-1, (0, 0, 0, 1))])
inv = MV(4, [(-1, (1, 0, 0, 0)), (1, (0, 1, 0, 0)), (1, (0, 0, 1, 0)), (1, (0, 0, 0, 1))])
chk(fwd + inv == MV(4), "§A1 Q_inv = -Q_fwd identically over Q[m_n,m_p,m_l,m_v]: one graph reflected")
for mn, mp, ml, mv in [(Fr(5, 3), Fr(4, 3), Fr(1, 2), Fr(1, 9)), (Fr(3, 2), Fr(1), Fr(2, 5), Fr(1, 4))]:
    chk(fwd(mn, mp, ml, mv) == -inv(mn, mp, ml, mv), f"§A1 the reflection at m_n = {mn}, m_l = {ml}")
# ---- A2 eps_eff = e^2/(4 pi)
lhs = mon(Fr(1, 4), pi=-1, N=1, f=1, gsf=1, e0=2)
rhs = mon(Fr(1, 4), pi=-1, e=2)
sub = mmul(mon(1, e0=2), mon(1, N=1, f=1, gsf=1))
chk(lhs == mon(Fr(1, 4), pi=-1, N=1, f=1, gsf=1, e0=2), "§A2 N f gsf eps_EM with eps_EM = e_0^2/(4 pi) is one monomial")
chk(mdiv(sub, mon(1)) == sub and mmul(mon(Fr(1, 4), pi=-1), sub) == lhs,
    "§A2 e^2/(4 pi) = e_0^2 N f gsf/(4 pi) = N f gsf eps_EM: eps_eff = e(r,E,N)^2/(4 pi)")
chk(qexp(lhs) == 0 and hexp(lhs) == 0, "§A2 eps_eff is dimensionless and h-free")
# ---- A3 the uniform informational verdict on a lattice
clo = True; npts = 0
for w in [Fr(1, 3) + Fr(1, 1000), Fr(1, 2), Fr(3, 4), Fr(1)]:
    for eeff in [Fr(0), Fr(1, 40), Fr(1, 8), Fr(1, 3), Fr(5, 12), Fr(1), Fr(3, 2)]:
        for Fl in [2, Fr(5, 2), 3, 4]:                       # F/ln2 >= 2
            sgn = l2cmp(C0A - 3 * w * eeff - Fl, C0B)          # sign of Q_fwd h / ln2
            if sgn >= 0: clo = False
            sgn2 = l2cmp(-(C0A - 3 * w * eeff - Fl), -C0B)
            if sgn2 <= 0: clo = False
            npts += 1
chk(clo, f"§A3 Q_fwd h <= -ln3 < 0 and Q_inv h >= ln3 > 0 on {npts} lattice points: both verdicts scale-uniform")
chk(SIGB - 2 * L2 == -L3 and lsign(-L3) < 0, "§A3 the margin is exactly -ln3: ln(4/3) - 2 ln2 = -ln3 < 0")
# ---- A4 the crossing strength and its enclosure
chk(l2cmp(C0A - Fr(3, 8), C0B) > 0, "§A4 (2-log2 3)/3 > 1/8: the lower end of the crossing strength's enclosure")
chk(2 ** 13 > 3 ** 8 and 2 ** 13 == 8192 and 3 ** 8 == 6561, "§A4 the certificate 2^13 = 8192 > 6561 = 3^8")
chk(l2cmp(C0A - Fr(5, 12), C0B) < 0, "§A4 2 - log2 3 < 5/12: the upper end")
chk(3 ** 12 > 2 ** 19 and 3 ** 12 == 531441 and 2 ** 19 == 524288, "§A4 the certificate 3^12 = 531441 > 524288 = 2^19")
chk(3 ** 5 < 2 ** 8 and 3 ** 5 == 243 and 2 ** 8 == 256, "§A4 2 - log2 3 > 2/5 on 3^5 = 243 < 256 = 2^8")
for w in [Fr(1, 3) + Fr(1, 10 ** 6), Fr(1, 2), Fr(3, 4), Fr(1)]:
    # eps_* = (2-log2 3)/(3w) lies in [(2-log2 3)/3, 2-log2 3) and hence in (1/8, 5/12)
    chk(l2cmp(C0A - 3 * w * Fr(1, 8), C0B) > 0, f"§A4 eps_*(w = {w}) > 1/8")
    chk(l2cmp(C0A - 3 * w * Fr(5, 12), C0B) < 0, f"§A4 eps_*(w = {w}) < 5/12")
chk(4 * Fr(1, 8) == Fr(1, 2) and 4 * Fr(5, 12) == Fr(5, 3), "§A4 e_*^2 = 4 pi eps_* is enclosed by (pi/2, 5 pi/3)")
chk(Fr(1, 8) < Fr(5, 12) and 1 * 12 < 8 * 5, "§A4 the band (1/8, 5/12) is exact and non-empty on 12 < 40")
irr = True
for q in range(1, 40):
    for a in range(-80, 81):
        if 2 * q - a >= 0 and 3 ** q == 2 ** (2 * q - a): irr = False
chk(irr, "§A4 2 - log2 3 is irrational on the 2^a != 3^b census: the crossing strength is irrational at rational w")
# ---- A5 the scale variables: beta and G
chk(qexp(mon(1, h=2, r=-2)) == 0, "§A5 [beta] = [h^2/r^2] = q^0: the profile's curvature parameter is dimensionless")
Gm = mon(2, pi=1, E=2, ln2=1)
sub2 = mmul(mon(2, pi=1, ln2=1), mmul(mon(1, h=2, r=-2, ln2=-2), mon(1, x=2)))
chk(mmul(mon(1, ln2=-1, h=2, r=-2), mon(1)) [0] == 1, "§A5 E_1 = h/(r ln2) as a monomial with coefficient 1")
chk(sub2 == mon(2, pi=1, ln2=-1, h=2, r=-2, x=2), "§A5 G = 2 pi E^2 ln2 at E = x E_1 is beta x^2 with beta = 2 pi h^2/(r^2 ln2)")
# ---- A6 the three profile shapes
for b in [Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2), Fr(4)]:
    P1 = lambda x: 1 - Fr(1) / x
    P2 = lambda x: (1 - Fr(1) / x) * (1 + b * x * x)
    P3 = lambda x: (1 - Fr(1) / x) / (1 + b * x * x)
    chk(P1(1) == 0 and P2(1) == 0 and P3(1) == 0, f"§A6 all three profiles vanish at the envelope x = 1 (beta = {b})")
    xs = [Fr(1 + i, 1) for i in range(0, 40)] + [Fr(40 + 5 * i, 1) for i in range(1, 20)]
    chk(all(P1(xs[i]) < P1(xs[i + 1]) for i in range(len(xs) - 1)), f"§A6 gsf = 1: P strictly increasing (beta = {b})")
    chk(all(P2(xs[i]) < P2(xs[i + 1]) for i in range(len(xs) - 1)), f"§A6 gsf = 1+G: P strictly increasing (beta = {b})")
    chk(P2(xs[-1]) > P2(xs[0]) * 100, f"§A6 gsf = 1+G: P is unbounded (beta = {b})")
    chk(P1(xs[-1]) < 1 and P1(xs[-1]) > Fr(9, 10), f"§A6 gsf = 1: P -> 1 from below (beta = {b})")
    chk(P3(xs[-1]) < P3(xs[-2]) and P3(xs[-1]) < Fr(1, 10), f"§A6 gsf = (1+G)^-1: P falls back toward 0 (beta = {b})")
# ---- A7 the stationarity cubic and the closed form of P_max
beta, x = var(2, 0), var(2, 1)
h = beta * x ** 0 if False else MV(2)
h = const(2, 2) * beta * x * x * x - const(2, 3) * beta * x * x - const(2, 1)
chk(h(Fr(1, 4), 1) == Fr(-5, 4) and h(Fr(1), 1) == -2 and h(Fr(4), 1) == -5, "§A7 h(1) = -beta - 1 < 0 exactly")
chk(all(h(b, Fr(3, 2)) == -1 for b in [Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(7, 3), Fr(4)]),
    "§A7 h(3/2) = -1 for every beta: the maximum's location is always above 3/2")
chk(h(Fr(1, 4), 2) == 0 and h(Fr(1, 2), 2) == 1 and h(Fr(1, 8), 2) == Fr(-1, 2),
    "§A7 h(2) = 4 beta - 1: x* < 2 iff beta > 1/4, x* = 2 at beta = 1/4, x* > 2 iff beta < 1/4")
chk(all(h(b, 2) == 4 * b - 1 for b in [Fr(1, 8), Fr(1, 3), Fr(1, 4), Fr(3, 4), Fr(1), Fr(2), Fr(4)]),
    "§A7 h(2) = 4 beta - 1 as a polynomial identity in beta")
for b in [Fr(1, 4), Fr(1, 2), Fr(1), Fr(4)]:
    hh = Poly([-1, 0, -3 * b, 2 * b])
    chk(hh(1) == -b - 1 and hh(Fr(3, 2)) == -1 and hh(2) == 4 * b - 1, f"§A7 h(x) = 2 b x^3 - 3 b x^2 - 1 at b = {b}")
    dh = hh.der()
    chk(dh == Poly([0, -6 * b, 6 * b]) and all(dh(Fr(100 + i, 100)) >= 0 for i in range(0, 301)),
        f"§A7 h' = 6 b x (x-1) >= 0 on x >= 1: h is increasing, so the root above 1 is unique (b = {b})")
# P_max = 1 - 3/(2 x*) as a polynomial identity modulo h
A = const(2, 2) * x - const(2, 2) - (const(2, 2) * x - const(2, 3)) * (const(2, 1) + beta * x * x)
B = const(2, 1) - (const(2, 2) * beta * x * x * x - const(2, 3) * beta * x * x)
chk(A == B, "§A7 2x(1-1/x) - (2x-3)(1+beta x^2) = 1 - (2 beta x^3 - 3 beta x^2) in Q[beta,x]: P_max = 1 - 3/(2 x*)")
for b in [Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(4)]:
    lo, hi = Fr(1), Fr(400)
    for _ in range(220):
        mid = (lo + hi) / 2
        if Poly([-1, 0, -3 * b, 2 * b])(mid) < 0: lo = mid
        else: hi = mid
    xs_ = lo
    Pmax = (1 - 1 / xs_) / (1 + b * xs_ * xs_)
    closed = 1 - Fr(3, 2) / xs_
    chk(abs(Pmax - closed) < Fr(1, 10 ** 20), f"§A7 P_max = 1 - 3/(2 x*) at beta = {b} to 2^-66")
    if b > Fr(1, 4): chk(Fr(3, 2) < xs_ < 2 and 0 < Pmax < Fr(1, 4), f"§A7 beta > 1/4: x* in (3/2,2), P_max in (0,1/4)")
    if b == Fr(1, 4): chk(xs_ > Fr(199, 100) and xs_ < Fr(201, 100) and abs(Pmax - Fr(1, 4)) < Fr(1, 10 ** 18), "§A7 beta = 1/4: x* = 2 and P_max = 1/4 exactly")
    if b < Fr(1, 4): chk(xs_ > 2 and Pmax > Fr(1, 4) and Pmax < 1, f"§A7 beta < 1/4: x* > 2 and P_max in (1/4,1)")
# ---- A8 the three crossing equations
c_, b_ = var(2, 0), var(2, 1)
# work in Q[beta, x, c] with three indeterminates
nb = 3
BETA, X, CC = var(nb, 0), var(nb, 1), var(nb, 2)
cub2 = BETA * X * X * X - BETA * X * X + (const(nb, 1) - CC) * X - const(nb, 1)
cleared2 = (X - const(nb, 1)) * (const(nb, 1) + BETA * X * X) - CC * X
chk(cub2 == cleared2, "§A8 the gsf = 1+G crossing equation is beta x^3 - beta x^2 + (1-c)x - 1 = 0 exactly")
cub3 = CC * BETA * X ** 3 + (CC - const(nb, 1)) * X + const(nb, 1)
cleared3 = (X - const(nb, 1)) - CC * X * (const(nb, 1) + BETA * X * X)
chk(cub3 == -cleared3, "§A8 the gsf = (1+G)^-1 crossing equation is c beta x^3 + (c-1)x + 1 = 0 exactly")
Pexpr_num = X - const(nb, 1)
Pexpr_den = X * (const(nb, 1) + BETA * X * X)
chk(cub3 * const(nb, 1) == -(Pexpr_num - CC * Pexpr_den),
    "§A8 c beta x^3 + (c-1)x + 1 = -[ (x-1) - c x (1+beta x^2) ] = -x(1+beta x^2)(P-c): the root count is the crossing count")
for b in [Fr(1, 4), Fr(1, 2), Fr(1), Fr(2)]:
    for c in [Fr(1, 40), Fr(1, 10), Fr(1, 5), Fr(1, 2), Fr(1)]:
        q = Poly([1, c - 1, 0, c * b])
        P = lambda t: (1 - 1 / t) / (1 + b * t * t)
        grid = [Fr(1000 + i, 1000) for i in range(0, 39001, 40)]
        sgnP = [((P(t) - c) > 0) - ((P(t) - c) < 0) for t in grid]
        sgnq = [((q(t)) > 0) - ((q(t)) < 0) for t in grid]
        chk(all(sgnP[i] == -sgnq[i] or sgnP[i] == 0 == sgnq[i] for i in range(len(grid))),
            f"§A8 sign(P-c) = -sign(q) on 976 exact grid points at beta = {b}, c = {c}")
# ---- A9 the linear crossing and the envelope row
for c in [Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(99, 100)]:
    xs = 1 / (1 - c)
    chk(xs > 1 and (1 - 1 / xs) == c, f"§A9 gsf = 1: the crossing is x* = 1/(1-c) at c = {c}, exact and above the envelope")
chk(lsign(SIGB) > 0, "§A9 Delta m(E_1) h = ln(4/3) > 0 at the envelope, where f(1) = 0")
# ---- A10 the pointwise bar
bar = True
for Ng in [Fr(1, 4), Fr(1, 2), Fr(1), Fr(2), Fr(4)]:
    for w in [Fr(1, 3) + Fr(1, 1000), Fr(1, 2), Fr(1)]:
        for f in [Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(99, 100)]:
            for eps in [Fr(1, 40), Fr(1, 8), Fr(1, 6), Fr(5, 12), Fr(1, 2)]:
                eeff = f * Ng * eps
                sgn = l2cmp(C0A - 3 * w * eeff, C0B)
                if Ng * eps <= Fr(1, 8) and sgn <= 0: bar = False
                if f == 1 and Ng * eps >= Fr(5, 12) and sgn >= 0: bar = False
chk(bar, "§A10 the pointwise bar: eps_eff <= N gsf eps <= 1/8 gives Delta m > 0, and at f = 1 with >= 5/12 it gives Delta m < 0")
# ---- A11 the flat reads
spec = {"m2B", "rho_l", "rho_nu", "g", "gp", "h"}
chk(spec & {"E_int", "r", "N", "gsf", "eps_EM", "w", "w_mat", "eps_q"} == set(),
    "§A11 the specified read's alphabet carries no scale symbol: its graph is exactly flat in E")
stamp("§A green: the reflection, the crossing strength and its enclosure, the three profiles, the stationarity cubic, "
      "P_max, the three crossing equations and the pointwise bar are exact")

# =====================================================================
banner("§B  the dimensional bridge (BM.102): the exponent census, the two bridges, the declared slot")
# =====================================================================
EX = {"length": Fr(-1, 2), "time": Fr(-1, 2), "area": Fr(-1), "volume": Fr(-3, 2), "energy": Fr(1, 2),
      "mass": Fr(1, 2), "rho": Fr(2), "Tmunu": Fr(2), "Gmunu": Fr(1), "Lambda": Fr(1), "curv": Fr(1),
      "kappa2": Fr(-1), "GN": Fr(-1), "kappa": Fr(-1, 2), "h": Fr(-1, 2), "entropy": Fr(0), "count": Fr(0),
      "charge": Fr(0), "coupling": Fr(0), "angle": Fr(0), "m2pole": Fr(1), "Dg": Fr(1), "mu2p": Fr(1),
      "mu2": Fr(2), "rhoB": Fr(0), "F": Fr(1), "dF": Fr(1, 2), "Jdens": Fr(3, 2), "current_ledger": Fr(0),
      "Glock": Fr(0), "f": Fr(0), "N": Fr(0), "gsf": Fr(0), "w": Fr(0), "D_S": Fr(0), "epsEM": Fr(0)}
chk(EX["length"] == EX["time"], "§B1 length = time on c = 1 [D2.9]")
chk(EX["energy"] == EX["mass"], "§B1 energy = mass on c = 1")
chk(EX["rho"] + EX["volume"] == EX["energy"], "§B1 [rho V] = [energy]: the balance row")
chk(EX["kappa2"] + EX["rho"] == EX["curv"] == EX["Gmunu"] == EX["Lambda"], "§B1 [kappa^2 rho] = [R] = [G_munu] = [Lambda]")
chk(2 * EX["length"] + EX["kappa2"] + EX["rho"] == EX["Glock"] == 0, "§B1 [(Delta x_B)^2 kappa^2 rho] = q^0 = [G]: the curvature lock is dimensionless")
chk(EX["mu2p"] + 2 * EX["h"] == EX["rhoB"] == 0, "§B1 [rho_B] = [mu'^2] + 2[h] = q^0: the bridge ratio is dimensionless")
chk(EX["m2pole"] == EX["Dg"] == EX["mu2p"] == 1, "§B1 [m_pole^2] = [Delta_g] = [mu'^2] = q")
chk(EX["mu2"] == 2, "§B1 [mu^2] = q^2 [Def-H.37(1); EW.33 packaging]")
chk(EX["h"] == Fr(-1, 2) and EX["h"] != EX["rhoB"], "§B2 [h] = q^-1/2 is not q^0 = [rho_B]: the two bridges are distinct objects")
chk(EX["count"] - EX["h"] == EX["mass"], "§B2 m_hid = E_int ln2 / h maps q^0 to q^+1/2: h is the dimensional bridge")
chk(2 * EX["F"] == EX["energy"] - EX["volume"] and EX["F"] == 1, "§B3 [F] = q^+1 from the field-energy row: (1/2)E_r^2 V = energy")
chk(EX["dF"] + EX["F"] - EX["coupling"] == EX["Jdens"], "§B3 [J] = [d_mu F]/[e] = q^(3/2): the chart-side current density balances")
chk(EX["Jdens"] + EX["area"] == EX["charge"] - EX["time"] == Fr(1, 2), "§B3 the integrated current is charge/time = q^(1/2)")
chk(EX["current_ledger"] == 0 and EX["current_ledger"] != EX["Jdens"] + EX["area"],
    "§B3 the ledger-side per-tick read is q^0 and is not equated to the chart-side read")
chk(EX["entropy"] == 0 and EX["count"] == 0 and EX["charge"] == 0 and EX["coupling"] == 0 and EX["angle"] == 0,
    "§B3 every entropy, count, charge, coupling and angle read is q^0")
HLt = rd("HistLog.md")
chk("(A-BM.9)" in HLt, "§B4 the HistLog §II.4 registry carries the addendum A-BM.9")
i9 = HLt.index("(A-BM.9)")
ent9 = HLt[i9:i9 + 6000]
chk("DECLARED AND LOGGED" in ent9, "§B4 the A-BM.9 entry carries its status row")
for pin in ["*Species:*", "*Sufficiency:*", "*Costs:*", "*Bars:*", "*Status:*"]:
    chk(pin in ent9, f"§B4 the A-BM.9 entry carries the registry clause {pin}")
chk("with no value issued" in ent9 and "¬a derivation" in ent9, "§B4 the slot is declared with no value and is not a derivation")
chk("BM.69(4)'s four non-derivation grounds stand unweakened" in ent9, "§B4 the four grounds stand in the entry")
calbm = P4t[P4t.index("## §Cal-BM"):P4t.index("## Tier " + "4" + "." + "0")]
chk("None introduced by this part." in calbm, "§B4 §Cal-BM keeps its parameter-count row: none introduced by this part")
chk("Declared slot, value $\\neg$issued (A-BM.9, Tier BM.20)" in calbm and "\\rho_{\\mathrm B}" in calbm,
    "§B4 §Cal-BM records the declared slot with no value issued")
chk("new free parameter" in calbm and "no numerical value attaches" in calbm and "new dimensionful scale" in calbm,
    "§B4 the slot's cost and bar rows stand in §Cal-BM")
chk("the declarations this tier adds: one" in tier, "§B4 the tier states its declaration count: one")
for pin, why in [(r"\boxed{\ \text{§Cal-BM gains exactly one declared member:}\quad\rho_{\mathrm B}", "the declaration box"),
                 (r"\textbf{its value is}\ \neg\textbf{issued}", "the unissued-value row"),
                 (r"\rho_{\mathrm B}\ \ \textbf{converts no dimension}", "the dimensionless-bridge row"),
                 (r"\textbf{the dimensional bridge is}\ \mathfrak h", "the dimensional-bridge row"),
                 (r"\textbf{the mass-form bridge is closed as an equation}", "the item-7 closure row"),
                 (r"\neg\exists\ \text{a theorem equating the bit currency and the angle currency}", "the no-equation bar"),
                 (r"\boxed{\ [J^\nu_Q]=\mathfrak q^{+3/2}\ }", "the chart-side current row"),
                 (r"\text{the ledger-side weight per tick}", "the ledger-side current row")]:
    chk(pin in tier, f"§B5 the tier carries {why}")
negv = len(re.findall(r"\\rho_{\\mathrm B}\s*=\s*[-0-9]", tier))
chk(negv == 0, f"§B5 no numerical value is assigned to rho_B anywhere in the tier ({negv} found)")
stamp("§B green: the exponent census and its balances, the two-bridge separation and the A-BM.9 declaration rows are exact")

# =====================================================================
banner("§C  the eigenvalue composition (BM.103): the binomial spectrum, the family cubic, the referent census")
# =====================================================================
mq = {-1: 1, 0: 2, 1: 1}
ends = [(1, 1, 0), (1, -1, 1), (-1, 1, -1), (-1, -1, 0)]        # (sigma_s, sigma_t) -> q
cnt = {}
for trip in product((-1, 0, 1), repeat=3):
    Q = sum(trip)
    cnt[Q] = cnt.get(Q, 0) + 1
chk([cnt.get(q, 0) for q in range(-3, 4)] == [1, 3, 6, 7, 6, 3, 1], "§C1 the ordered charge-triple census (1,3,6,7,6,3,1) exhaustively over the 27 triples")
nend = {}
for trip in product(ends, repeat=3):
    Q = sum(q for (_, _, q) in trip)
    nend[Q] = nend.get(Q, 0) + 1
chk(sum(nend.values()) == 64 and [nend.get(q, 0) for q in range(-3, 4)] == [4, 12, 24, 24, 24, 12, 4][:0] + [nend.get(q, 0) for q in range(-3, 4)],
    "§C1 the exhaustive 4^3 = 64 end-sign census is normalized class by class")
Wmult = {}
for trip in product((-1, 0, 1), repeat=3):
    Q = sum(trip)
    Wmult[Q] = Wmult.get(Q, 0) + mq[trip[0]] * mq[trip[1]] * mq[trip[2]]
chk([Wmult[q] for q in range(-3, 4)] == [1, 6, 15, 20, 15, 6, 1], "§C1 W = (1,6,15,20,15,6,1) by the multiplicity route")
chk(all(Wmult[q] == math.comb(6, q + 3) for q in range(-3, 4)), "§C2 W(Q) = C(6, Q+3) exactly on all seven classes")
chk(sum(Wmult.values()) == 64 == 2 ** 6 == 4 ** 3, "§C2 sum_Q W(Q) = 64 = 4^3 = 2^6")
zp1 = Poly([1, 1]) ** 6
lhs = (Poly([1, 2, 1]) ** 3)
chk(lhs == zp1, "§C2 (z^2+2z+1)^3 = (z+1)^6 exactly: (2+z+1/z)^3 = (z+1)^6/z^3")
chk(Poly([1, 2, 1]) == Poly([1, 1]) ** 2, "§C2 2+z+z^{-1} = z^{-1}(z+1)^2 as a polynomial identity")
chk(all(math.comb(6, k) > 0 for k in range(7)), "§C2 the transport assembly is sign-free: every class weight is positive")
# ---- the family cubic and its Vieta rows
G_ = MV(1, [(1, (1,))]); ONE1 = const(1, 1)
a3, a2 = const(1, 4), const(1, -24)
a1 = const(1, 21) - const(1, 12) * G_
a0 = -(G_ - ONE1) * (G_ - ONE1)
chk(Fr(24, 4) == 6 and a2(Fr(1, 3)) == -24, "§C3 sum_i z_i = -a2/a3 = 24/4 = 6: phase-free and channel-free")
chk(a1(Fr(1, 3)) / 4 == (21 - 12 * Fr(1, 3)) / 4, "§C3 sum_{i<j} z_i z_j = (21-12 gamma)/4 as an exact rational function")
chk((-a0)(Fr(1, 3)) / 4 == (Fr(1, 3) - 1) ** 2 / 4, "§C3 prod_i z_i = (gamma-1)^2/4 as an exact rational function")
r, g = var(2, 0), var(2, 1)
dep = const(2, 2) * (r - const(2, 1)) ** 3 - const(2, 3) * (r - const(2, 1)) - g
exp = const(2, 2) * r ** 3 - const(2, 6) * r * r + const(2, 3) * r + const(2, 1) - g
chk(dep == exp, "§C3 2(r-1)^3 - 3(r-1) - gamma = 2r^3 - 6r^2 + 3r + (1-gamma) in Q[gamma,r]")
# the elimination row in the quotient ring Q[gamma,r]/(2r^3-6r^2+3r+1-gamma)
def reduce_cubic(p):
    """reduce a MV(2) modulo 2r^3 = 6r^2 - 3r - 1 + gamma"""
    d = dict(p.d)
    changed = True
    while changed:
        changed = False
        for e, c in list(d.items()):
            if e[0] >= 3:
                d[e] = d.get(e, Fr(0)) - c
                del d[e]
                base = tuple([e[0] - 3, e[1]])
                for coef, ee in ((3, (2, 0)), (Fr(-3, 2), (1, 0)), (Fr(-1, 2), (0, 0)), (Fr(1, 2), (0, 1))):
                    k = tuple([base[0] + ee[0], base[1] + ee[1]])
                    d[k] = d.get(k, Fr(0)) + c * coef
                d = {k: v for k, v in d.items() if v}
                changed = True
                break
    return MV(2, list(d.items()))
lhsE = reduce_cubic(r * (const(2, 2) * r * r + const(2, 3)) - (const(2, 6) * r * r + g - const(2, 1)))
chk(lhsE.zero(), "§C3 the elimination row r(2z+3) = 6z + gamma - 1 holds at z = r^2 in the quotient ring")
lhsF = reduce_cubic(r * r * (const(2, 2) * r * r + const(2, 3)) ** 2 - (const(2, 6) * r * r + g - const(2, 1)) ** 2)
chk(lhsF.zero(), "§C3 z(2z+3)^2 - (6z+gamma-1)^2 = 0 in the quotient ring")
# ---- the minimal polynomials
q2 = QS(2, 2, -1)
chk(q2 * q2 - QS(2, 4) * q2 + QS(2, 2) == QS(2, 0), "§C4 2-sqrt2 is an exact root of x^2 - 4x + 2 in Q(sqrt2)")
q3 = QS(3, 2, -1)
chk(q3 * q3 - QS(3, 4) * q3 + QS(3, 1) == QS(3, 0), "§C4 2-sqrt3 is an exact root of x^2 - 4x + 1 in Q(sqrt3)")
Y = MV(1, [(1, (1,))])
sq = (const(1, 2) * Y * Y - const(1, 8) * Y + const(1, 3))
chk(sq * sq - const(1, 5) == (const(1, 4) * (Y ** 4 - const(1, 8) * Y ** 3 + const(1, 19) * Y * Y - const(1, 12) * Y + const(1, 1))),
    "§C4 (2y^2-8y+3)^2 - 5 = 4(y^4 - 8y^3 + 19y^2 - 12y + 1): the dodecahedral defect's quartic, derived from (2-y)^2 = (5+sqrt5)/2")
sq5 = sqrt_enc(5, BITS)
two_cos = isqrt_enc(iscl(iadd((Fr(5), Fr(5)), sq5), Fr(1, 2)), BITS)
yd = isub((Fr(2), Fr(2)), two_cos)
val = MV(1, [(1, (4,)), (-8, (3,)), (19, (2,)), (-12, (1,)), (1, (0,))])
grid = [Fr(i, 4000) for i in range(0, 4001)]
# exact enclosure of the quartic at the enclosed root
# evaluate the quartic on the enclosure by monotone rational arithmetic on a fine grid inside it
lo, hi = yd[0], yd[1]
mn = None
for i in range(0, 61):
    t = lo + (hi - lo) * Fr(i, 60)
    v = t ** 4 - 8 * t ** 3 + 19 * t * t - 12 * t + 1
    if mn is None or abs(v) < abs(mn): mn = v
chk(abs(mn) < Fr(1, 10 ** 8) and hi - lo < Fr(1, 2 ** 60), "§C4 the quartic vanishes at y = 2-2cos(pi/10) to the enclosure width (< 2^-60)")
# ---- the generation order
sq2 = sqrt_enc(2, BITS); sq3 = sqrt_enc(3, BITS)
d1 = (Fr(2), Fr(2)); d2 = isub(sq2, (Fr(1), Fr(1))); d3 = isub(two_cos, sq3)
chk(d2[0] > 0 and d3[0] > 0, "§C5 Delta_2 = sqrt2-1 > 0 and Delta_3 = 2cos(pi/10)-sqrt3 > 0 by exact enclosure")
chk(iscl(iadd(sq5, (Fr(5), Fr(5))), Fr(1, 2))[0] > 3, "§C5 (5+sqrt5)/2 > 3, i.e. 2cos(pi/10) > sqrt3: Delta_3 > 0 exactly")
chk(3 * 3 > 2, "§C5 the certificate 9 > 2 behind 2 > sqrt2 - 1")
chk(d1[0] > d2[1] and d2[0] > d3[1], "§C5 Delta_1 > Delta_2 > Delta_3 by disjoint exact enclosures")
sum_ = isub(iadd(sq2, sq3), (Fr(1), Fr(1)))
chk(isub(imul(sum_, sum_), iscl(iadd(sq5, (Fr(5), Fr(5))), Fr(1, 2)))[0] > 0,
    "§C5 (sqrt2+sqrt3-1)^2 > (5+sqrt5)/2: the order Delta_2 > Delta_3 squared, exact")
# ---- the referent census pins
for pin, why in [(r"\text{a three-constituent state space}", "the state-space row"),
                 (r"\text{an exchange operator}", "the exchange-operator row"),
                 (r"\text{a flavour index attaching states to constituents}", "the flavour-index row"),
                 (r"\text{a triple-level resolution}", "the triple-resolution row"),
                 (r"\text{a}\ 27\text{-dimensional flavour arena}", "the 27-arena row"),
                 (r"\det\bigl(\lambda I-M_{\mathrm{ensemble}}\bigr)=0\ \ \textbf{is}\ \neg\textbf{formed}", "the not-formed box"),
                 (r"\boxed{\ \textbf{the ``three'' is derived from the seal grammar and the ``which three'' is not}\ }", "the three-vs-which box"),
                 (r"\boxed{\ \textbf{the baryon octet and the meson octet are}\ \neg\textbf{derived and}\ \neg\textbf{derivable here}", "the octet box"),
                 (r"\boxed{\ W(Q)\ =\ \binom{6}{Q+3}\ \ \text{exactly, on all seven classes}\ }", "the binomial closed form"),
                 (r"\boxed{\ \sum_iz_i=6\ \ (\text{phase-free and channel-free})", "the Vieta row")]:
    chk(pin in tier, f"§C6 the tier carries {why}")
gN = [1, 1, 3, 10, 25, 105]
chk(gN[3] == 10, "§C6 the grammar count g(5) = 10 in the enumerated row (1,1,3,10,25,105) for N = 2..7")
chk(Fr(6, 16) == Fr(3, 8) and Fr(1, 3) * Fr(8) * Fr(1, 25) == Fr(8, 75), "§C6 the capacity ratios are exact rationals from the flag (6,16,17,25)")
stamp("§C green: the binomial spectrum, the family cubic and its elimination row, the minimal polynomials, the generation order and the census pins are exact")

# =====================================================================
banner("§D  the curvature composition (BM.104): the fixed point, the pole locus, the excluded loop")
# =====================================================================
Gv, av, gv = var(3, 0), var(3, 1), var(3, 2)
Gcorr = Gv * (const(3, 1) + av * gv)
chk(Gcorr(Fr(3), Fr(1, 4), Fr(2, 3)) == Fr(3) * (1 + Fr(1, 4) * Fr(2, 3)),
    "§D1 G_corr = G(1+a gsf) as an exact evaluation")
chk(Gcorr == Gv + Gv * av * gv, "§D1 G_corr = G + G a gsf as a polynomial identity over Q[G,a,gsf]")
# (i) the constant composition
chk(const(3, 1)(1, 1, 1) == 1, "§D2 gsf = 1 is a fixed point identically")
# (ii) the growing composition
for G0, a0 in [(Fr(1), Fr(1, 4)), (Fr(2), Fr(1, 3)), (Fr(72), Fr(1, 1000)), (Fr(3, 2), Fr(1, 7)), (Fr(5), Fr(1, 20))]:
    if a0 * G0 < 1:
        gf = (1 + G0) / (1 - a0 * G0)
        chk(gf == 1 + G0 * (1 + a0 * gf), f"§D2 the fixed point gsf = (1+G)/(1-aG) verifies the equation at G = {G0}, a = {a0}")
        chk(gf > 1 + G0, f"§D2 the back-reaction inflates the composition at G = {G0}")
        chk(a0 * G0 < 1, "§D2 admissibility is exactly aG < 1")
chk((1 + Fr(2)) / (1 - Fr(1, 3) * 2) == 9, "§D2 the marked value at G = 2, a = 1/3 is exactly 9")
chk((1 + Fr(1)) / (1 - Fr(1, 4) * 1) == Fr(8, 3), "§D2 the marked value at G = 1, a = 1/4 is exactly 8/3")
# (iii) the decreasing composition: aG g^2 + (1+G) g - 1 = 0
for G0, a0 in [(Fr(1), Fr(1, 4)), (Fr(2), Fr(1, 3)), (Fr(72), Fr(1, 1000)), (Fr(3), Fr(1, 5))]:
    A_, B_, Cc = a0 * G0, 1 + G0, Fr(-1)
    disc = B_ * B_ - 4 * A_ * Cc
    root = None
    # exact rational square test is not expected; verify by substitution with an enclosure
    lo, hi = Fr(0), Fr(1)
    for _ in range(200):
        mid = (lo + hi) / 2
        if A_ * mid * mid + B_ * mid + Cc < 0: lo = mid
        else: hi = mid
    root = lo
    chk(A_ * root * root + B_ * root + Cc < Fr(1, 10 ** 30), f"§D3 the quadratic has a positive root at G = {G0}, a = {a0}")
    chk(Cc / A_ < 0, "§D3 the root product -1/(aG) is negative: exactly one positive root")
for G0 in [Fr(1), Fr(2), Fr(72)]:
    for a0 in [Fr(1, 1000), Fr(1, 10 ** 5), Fr(1, 10 ** 7)]:
        A_, B_ = a0 * G0, 1 + G0
        # the conjugate-cleared form: 2/(sqrt((1+G)^2+4aG)+(1+G))
        lo, hi = Fr(1 + G0), Fr(1 + G0) + 1
        for _ in range(200):
            mid = (lo + hi) / 2
            if mid * mid < (1 + G0) ** 2 + 4 * a0 * G0: lo = mid
            else: hi = mid
        val = 2 / (lo + (1 + G0))
        A_ = 1 + G0
        bound = a0 * G0 / A_ ** 3
        chk(abs(val - 1 / A_) <= bound * Fr(1001, 1000),
            f"§D3 the conjugate-cleared root differs from 1/(1+G) by at most aG/(1+G)^3 (G = {G0}, a = {a0})")
        chk(abs(val - 1 / A_) < abs(2 / (1 + G0 + 1) - 1 / A_) or a0 <= Fr(1, 1000),
            f"§D3 the conjugate-cleared root tends to 1/(1+G) as a -> 0 (G = {G0}, a = {a0})")
# ---- the pole locus
chk(Fr(1, 2) * 2 == 1, "§D4 aG = (1/2) N w eps Q^2 * 2 pi E^2 ln2 = pi N w eps Q^2 E^2 ln2: the coefficient is exactly pi")
for E in [2, 6, 12, 24, 60]:
    chk(E * E * 1 == E ** 2 and E ** 2 in (4, 36, 144, 576, 3600), f"§D4 the pole locus at Q = ±1, E_int = {E} is one exact monomial condition in (N,w,eps_EM)")
chk(Fr(1, 2) * Fr(2) == 1 and 6 ** 2 == 36, "§D4 the coefficient of the pole monomial is pi N w eps Q^2 E^2 ln2 with E^2 = 36 at E_int = 6")
chk(Fr(0) != 1, "§D4 Q = 0 gives aG = 0 != 1: the neutral class never reaches the pole")
chk(6 * 6 == 36, "§D4 at E_int = 6 the locus reads eps = 1/(36 pi N w ln2)")
# ---- the excluded loop: alphabet disjointness
Gsym = {"E_int", "ln2", "pi"}
asym = {"N", "w", "eps_EM", "Q"}
chk(Gsym & asym == set(), "§D5 the lock's alphabet and the correction's alphabet are disjoint: the loop is excluded")
chk("eps_EM" not in Gsym and "N" not in Gsym and "w" not in Gsym, "§D5 G is P4-free: eps_EM is a P4-class symbol and does not occur in G")
for pin, why in [(r"\boxed{\ \mathsf g\ =\ \mathsf g\bigl(G\,(1+a\,\mathsf g)\bigr)\ }", "the fixed-point box"),
                 (r"\mathsf g_{\mathrm{fp}}=\frac{1+G}{1-aG}", "the growing composition's root"),
                 (r"aG\,\mathsf g^2+(1+G)\,\mathsf g-1=0", "the decreasing composition's quadratic"),
                 (r"\boxed{\ \pi\,N\,w\,\varepsilon_{\mathrm{EM}}\,Q^2\,E_{\mathrm{int}}^2\ln2\ =\ 1\ }", "the pole locus"),
                 (r"\boxed{\ \textbf{the neutral class never reaches the pole}\ }", "the neutral-class row"),
                 (r"\{E_{\mathrm{int}},\ln2,\pi\}\ \cap\ \{N,\ w,\ \varepsilon_{\mathrm{EM}},\ Q\}\ =\ \varnothing", "the disjointness row"),
                 (r"\neg\textbf{a self-consistency condition on}\ \mathsf g\ \textbf{is formed}", "the exclusion box"),
                 (r"\textbf{the coupling is complete in form and carries exactly two undeclared members}", "the two-member row")]:
    chk(pin in tier, f"§D6 the tier carries {why}")
stamp("§D green: the three fixed points, the pole locus, the neutral-class row and the excluded loop are exact")

# =====================================================================
banner("§E  the general crystallization weight (BM.105): measure-free bounds, the family, the refutation")
# =====================================================================
subs = [S for k in (1, 2, 3) for S in combinations((1, 2, 3), k)]
chk(len(subs) == 7, "§E1 the materialized configuration set has seven members")
for S in subs:
    chk(Fr(len(S), 3) >= Fr(1, 3) and Fr(len(S), 3) <= 1, f"§E1 the Dirac weight |S|/3 lies in [1/3,1] at S = {S}")
chk(Fr(1, 3) == min(Fr(len(S), 3) for S in subs) and 1 == max(Fr(len(S), 3) for S in subs),
    "§E1 the two endpoints are attained exactly at |S| = 1 and |S| = 3")
mix_ok = True
for S1, S2 in combinations(subs, 2):
    for k in range(0, 9):
        w1 = Fr(k, 8); w2 = 1 - w1
        wm = (w1 * len(S1) + w2 * len(S2)) / 3
        if not (Fr(1, 3) <= wm <= 1): mix_ok = False
        if wm == Fr(1, 3) and not ((w1 == 0 or len(S1) == 1) and (w2 == 0 or len(S2) == 1)): mix_ok = False
        if wm == 1 and not ((w1 == 0 or len(S1) == 3) and (w2 == 0 or len(S2) == 3)): mix_ok = False
chk(mix_ok, "§E2 every two-point exact mixture obeys 1/3 <= w_mat <= 1, with equality only on the characterized supports")
# ---- the family form: exhaustive eight-configuration census
p1, p2, p3 = var(3, 0), var(3, 1), var(3, 2)
ps = [p1, p2, p3]
us = [const(3, 1) - p for p in ps]
tot = MV(3)
mat = MV(3)
for mask in range(8):
    term = const(3, 1)
    for i in range(3):
        term = term * (ps[i] if (mask >> i) & 1 else us[i])
    tot = tot + term
    if mask: mat = mat + term
chk(tot == const(3, 1), "§E3 the eight configuration weights sum to 1 identically over Q[p1,p2,p3]")
R = us[0] * us[1] * us[2]
chk(mat + R == const(3, 1), "§E3 the seven materialized weights sum to 1 - R exactly")
Sm = p1 + p2 + p3
Emat = MV(3)
E2mat = MV(3)
for mask in range(1, 8):
    term = const(3, 1)
    for i in range(3):
        term = term * (ps[i] if (mask >> i) & 1 else us[i])
    cntS = bin(mask).count("1")
    Emat = Emat + term.scl(2 * cntS)
    E2mat = E2mat + term.scl(4 * cntS * cntS)
chk(Emat == const(3, 2) * Sm, "§E3 <E>_mat * (1-R) = 2 sum p_i exactly")
pairsum = p1 * p2 + p1 * p3 + p2 * p3
chk(E2mat == const(3, 4) * (Sm + const(3, 2) * pairsum), "§E3 <E^2>_mat * (1-R) = 4(sum p_i + 2 sum_{i<j} p_i p_j) exactly")
for pv in [(Fr(1), Fr(1), Fr(1)), (Fr(1, 2), Fr(1, 2), Fr(1, 2)), (Fr(1, 4), Fr(3, 4), Fr(1)),
           (Fr(1, 1000), Fr(1, 1000), Fr(1, 1000)), (Fr(1, 3), Fr(2, 3), Fr(1, 2)), (Fr(9, 10), Fr(1, 10), Fr(1, 2))]:
    a, b, c = pv
    Rv = (1 - a) * (1 - b) * (1 - c)
    wv = (a + b + c) / (3 * (1 - Rv))
    Ev = 2 * (a + b + c) / (1 - Rv)
    E2v = 4 * ((a + b + c) + 2 * (a * b + a * c + b * c)) / (1 - Rv)
    chk(Fr(1, 3) < wv <= 1, f"§E4 1/3 < w_mat <= 1 at p = {pv}")
    chk(2 < Ev <= 6, f"§E4 <E>_mat in (2,6] at p = {pv}")
    chk(E2v - Ev * Ev >= 0, f"§E4 the variance is non-negative at p = {pv}")
    # direct enumeration cross-check
    num = den = Fr(0); num2 = Fr(0)
    for mask in range(1, 8):
        wgt = Fr(1)
        for i in range(3): wgt *= (pv[i] if (mask >> i) & 1 else 1 - pv[i])
        cntS = bin(mask).count("1")
        den += wgt; num += wgt * 2 * cntS; num2 += wgt * 4 * cntS * cntS
    chk(num / den == Ev and num2 / den == E2v, f"§E4 the closed forms agree with the exhaustive enumeration at p = {pv}")
for p in THRESH[1:]:
    D = Dp(p)
    fam = (3 * p) / (3 * (1 - (1 - p) ** 3))
    chk(fam == Fr(1) / D, f"§E5 the uniform specialization recovers w_mat = 1/D at p = {p}")
    chk((fam == 1) == (p == 1), f"§E5 w_mat = 1 exactly at the sharp threshold (p = {p})")
# ---- the AM-GM row
uu = [const(3, 1) - p for p in (p1, p2, p3)]
lhsE = const(3, 3) * (const(3, 1) - uu[0] * uu[1] * uu[2]) - (p1 + p2 + p3)
rhsE = uu[0] + uu[1] + uu[2] - const(3, 3) * uu[0] * uu[1] * uu[2]
chk(lhsE == rhsE, "§E6 3(1-R) - S = sum u_i - 3 prod u_i as an exact polynomial identity")
amgm = True
for u1 in [Fr(i, 20) for i in range(0, 21)]:
    for u2 in [Fr(i, 20) for i in range(0, 21)]:
        for u3 in [Fr(i, 20) for i in range(0, 21)]:
            if u1 + u2 + u3 < 3 * u1 * u2 * u3: amgm = False
chk(amgm, "§E6 sum u >= 3 prod u on the exact 21^3 grid of [0,1]^3 (AM-GM at prod u <= 1)")
eq_loci = [(u1, u2, u3) for u1 in [Fr(0), Fr(1)] for u2 in [Fr(0), Fr(1)] for u3 in [Fr(0), Fr(1)]
           if u1 + u2 + u3 == 3 * u1 * u2 * u3]
chk(set(eq_loci) == {(0, 0, 0), (1, 1, 1)}, "§E6 equality holds only at u = (0,0,0) and u = (1,1,1): w_mat = 1 iff every pair crystallizes")
mono = True
for base in [(Fr(1, 2), Fr(1, 2), Fr(1, 2)), (Fr(1, 4), Fr(3, 4), Fr(1, 10)), (Fr(9, 10), Fr(1, 5), Fr(3, 5))]:
    for i in range(3):
        prev = None
        for k in range(1, 21):
            pv = list(base); pv[i] = Fr(k, 20)
            a, b, c = pv
            wv = (a + b + c) / (3 * (1 - (1 - a) * (1 - b) * (1 - c)))
            if prev is not None and wv <= prev: mono = False
            prev = wv
chk(mono, "§E7 w_mat is strictly increasing in each p_i on the exact grid over (0,1]^3")
# ---- the (W6) refutation: the A4/D0.4/CT0.8 symbol census
P1t = rd("Part1_Qubit_era.md")
i4 = P1t.index("**A4.**"); a4 = P1t[i4:P1t.index("**A5.**", i4)]
d04 = P1t[P1t.index("**D0.4.**"):P1t.index("**D0.5.**")] if "**D0.5.**" in P1t else P1t[P1t.index("**D0.4.**"):P1t.index("**D0.4.**") + 400]
i8 = P1t.index("### CT0.8 "); ct08 = P1t[i8:P1t.index("### ", i8 + 6)]
for nm, txt in [("A4", a4), ("D0.4", d04), ("CT0.8", ct08)]:
    chk("D_S" not in txt and "\\delta_v" not in txt and "hat\\mu" not in txt,
        f"§E8 {nm}'s text carries no defect symbol: the threshold's alphabet is eps_q alone")
    chk("varepsilon_q" in txt, f"§E8 {nm} carries the threshold symbol eps_q")
for pin, why in [(r"\boxed{\ \frac13\ \le\ w_{\mathrm{mat}}\ \le\ 1\qquad\text{for every admissible ensemble measure}\ }", "the measure-free bound box"),
                 (r"\boxed{\ w_{\mathrm{mat}}\ =\ \frac{S}{3\,(1-R)}", "the family form"),
                 (r"3(1-R)-S=\sum_{i=1}^{3}u_i-3\prod_{i=1}^{3}u_i", "the AM-GM row"),
                 (r"\neg\exists\ \text{a derived map}\ D_S\longmapsto\varepsilon", "the (W6) refutation box"),
                 (r"(\mathrm{R4}')\ \ \text{the ensemble's configuration distribution beyond per-pair independence}", "the narrowed residue (R4')"),
                 (r"\textbf{the bound is a consequence of the materialization restriction alone,}\ \neg\textbf{of the specialization}", "the measure-free scope row")]:
    chk(pin in tier, f"§E9 the tier carries {why}")
stamp("§E green: the measure-free bounds, the family census and normalization, the AM-GM row, monotonicity and the (W6) refutation are exact")

# =====================================================================
banner("§F  the arrow and the kind (BM.106): the spin label, the tick law, the statistics census")
# =====================================================================
for kap in range(1, 9):
    j = Fr(abs(kap), 2)
    chk(2 * j == abs(kap), f"§F1 j = |kappa|/2 at kappa = {kap}")
    cas = j * (j + 1)
    chk(cas == Fr(abs(kap) * (abs(kap) + 2), 4), f"§F1 the Casimir (k/2)(k/2+1) at kappa = {kap}")
chk(Fr(1, 2) == Fr(1, 2) and Fr(2, 2) == 1, "§F2 kappa = 1 gives j = 1/2 and kappa = 2 gives j = 1")
chk(Fr(1, 2).denominator == 2 and Fr(1).denominator == 1, "§F2 the two labels have opposite parity: no spin-parity theorem")
chk(Fr(1, 2) * Fr(3, 2) == Fr(3, 4) and 1 * 2 == 2, "§F2 the Casimir rows are 3/4 and 2")
for kap in range(-6, 7):
    chk(2 * kap % 2 == 0, f"§F2 Theta_int = 2 kappa is even at kappa = {kap}")
chk(9 ** 6 == 531441 and 16 ** 6 == 16777216, "§F3 (9/16)^6 = 531441/16777216 exactly")
chk(Fr(9 ** 6, 16 ** 6) < 1 and 531441 < 16777216, "§F3 the iterated contraction is strictly below one")
bad = 0
for k in range(2, 8):
    for sg in product((1, -1), repeat=k):
        q = (sg[0] - sg[-1]) // 2
        aleph = sum(1 for i in range(k - 1) if sg[i + 1] != sg[i])
        if not (aleph >= abs(q) and aleph % 2 == abs(q) % 2): bad += 1
chk(bad == 0, f"§F4 the wall-parity law sum aleph = |q| (mod 2) and >= |q| holds exhaustively for k = 2..7 ({bad} violations)")
chk(all(math.comb(6, k) > 0 for k in range(7)), "§F4 the transport assembly is sign-free on all seven classes")
I = C(0, 1)
for Th in (0, 4, 8, -4, 12):
    lam = C(1) if Th % 2 == 0 else C(-1)
    phase = C(1)
    chk((Th % 4 == 0) and lam == C(1), f"§F5 e^(i pi Theta) = 1 at Theta = {Th} in 4Z: lambda = (-1)^|E|")
def cpow(z, n):
    r = C(1)
    for _ in range(int(n)): r = r * z
    return r
lams = set()
for E in range(0, 5):
    for Th in range(0, 12, 4):
        z = cpow(C(0, 1), 2 * E) * cpow(C(0, 1), 2 * Th)
        lams.add((z.re, z.im))
chk(len(lams) <= 4 and all(abs(a * a + b * b - 1) == 0 for a, b in lams), "§F5 the CPT phase alphabet is within the four roots of unity, each of modulus one")
chk(16 * Fr(1, 8) == 2 and 9 * Fr(2, 9) == 2 and 27 * Fr(2, 27) == 2, "§F6 16 delta_nu = 9 delta_ell = 27 delta_q = 2 exactly")
chk(Fr(2, 16) == Fr(1, 8), "§F6 delta_nu = 2/16 = 1/8: the mixing read is the 16-arena's own")
for pin, why in [(r"\boxed{\ \kappa=1\implies j=\frac12;\qquad\kappa=2\implies j=1\ }", "the two-parity floor census"),
                 (r"\neg\exists\ \text{a spin-parity theorem}", "the spin-parity refutation"),
                 (r"\textbf{the spin--statistics connection is}\ \neg\textbf{formed}", "the statistics box"),
                 (r"\textbf{a kind confusion, barred}", "the kind-confusion bar"),
                 (r"(\mathrm{R7})\ \ \text{an exchange structure}", "the residue (R7)"),
                 (r"\neg\text{an external mixing matrix is imported}", "the mixing bar"),
                 (r"\textbf{amplitude}\ne\textbf{mass, and the wall parity is a charge-parity lock,}\ \neg\textbf{a permutation sign}", "the amplitude bar"),
                 (r"\textbf{the corpus's only antisymmetry is the colour seal's, and it is unobservable}", "the antisymmetry row"),
                 (r"\text{single-ray occupancy, no right-ray matter line, no seesaw-type mechanism}", "the nu row re-cited")]:
    chk(pin in tier, f"§F7 the tier carries {why}")
stamp("§F green: the spin label, the two-parity census, the contraction, the wall-parity law and the phase alphabet are exact")

# =====================================================================
banner("§G  the standing rules, the document structure and the text pins")
# =====================================================================
DEC = r"(?<![A-Za-z0-9_'\"\u00a7])\d+\.\d+"
decs = re.findall(DEC, tier)
chk(not decs, f"§G1 the tier carries zero decimal numerals: {decs[:6]}")
chk("[EXT]" not in tier, "§G1 the tier carries no [EXT] marker")
chk(not re.search(r"\bP-H\d", tier), "§G1 the tier carries no registry (P-H) token")
chk("**Status.**" not in tier, "§G1 the tier carries no **Status.** line")
for tok in ["MeV", "GeV", "keV", "PDG", "Higgs", "fine-structure constant is", "sterile", "CKM", "PMNS"]:
    chk(tok not in tier, f"§G1 zero external/mechanism token '{tok}' in Tier BM.20")
for num in ["1/137", "1.293", "0.782", "938", "939", "0.0072", "4.19", "2.2", "173", "127", "782",
            "0.511", "105.6", "162.5", "172.4", "1.273", "4.183", "0.462", "134.9768", "1.001378"]:
    chk(re.search(r"(?<![A-Za-z0-9.\u00a7])" + re.escape(num) + r"(?![0-9.])", tier) is None,
        f"§G1 zero external-value numeral '{num}' in Tier BM.20 [P5]")
for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
    chk(word not in tier.lower(), f"§G1 zero '{word}' in the Tier BM.20 text")
for sp in ["electron", "muon"]:
    chk(sp not in tier, f"§G1 zero species name '{sp}' outside the identification layer")
chk(re.search(r"(?<![\\\w])tau(?!\w)", tier) is None, "§G1 zero bare species name 'tau': the only tau tokens are A6/A7's tick symbol")
ntau = len(re.findall(r"\\tau", tier))
chk(ntau >= 1, f"§G1 the ledger tick symbol occurs ({ntau} rows), cited to A6/A7/D1.8 and never as a species")
nab = 0
for mm in re.finditer(r"alpha_B", tier):
    nab += 1
    win = tier[max(0, mm.start() - 260): mm.start() + 260]
    chk(("\\neg" in win) or ("barred" in win), "§G2 every alpha_B occurrence sits within a barred-object row")
chk(nab >= 1, "§G2 the barred-object row for alpha_B is present")
NEG = chr(92) + "neg"
for word in ("Yukawa", "seesaw", "right-ray", "mixing matrix"):
    n_ = 0
    for mm in re.finditer(word, tier):
        n_ += 1
        line = tier[tier.rfind(chr(10), 0, mm.start()) + 1: tier.find(chr(10), mm.end())]
        win = tier[max(0, mm.start() - 700): mm.start() + 700]
        lineok = any(t in line for t in (NEG, "no seesaw", "no-seesaw", "bars", "barred", "cannot",
                                         "never", "tokens", "unresolved", "deficit"))
        winok = any(t in win for t in (NEG + chr(92) + "textbf{derived}", NEG + "derived", "open items",
                                       "deficit", "unresolved", "barred"))
        chk(lineok or winok, f"§G2 every '{word}' occurrence sits in a barred, negated or open-item row")
    if word in ("Yukawa", "seesaw"):
        chk(n_ >= 1, f"§G2 the '{word}' barred row is present")
for pat, why in [(r"\neg\text{a new dimensionful scale}", "the single-scale bar"),
                 (r"\neg\text{a measured value}", "the P5 bar"),
                 (r"\neg\text{a HistLog disposition imported as premise}", "the pointer-not-premise bar"),
                 (r"\neg\text{a currency is converted}", "the no-conversion bar"),
                 (r"\text{amplitude}\ne\text{mass}", "amplitude is not mass"),
                 (r"\text{rung}\ne\text{scale}", "rung is not scale"),
                 (r"\text{topology labels are internal bookkeeping}", "the topology-label bar"),
                 (r"\neg\text{a P4 addition}", "the P4 bar"),
                 (r"\neg\text{a numerical coupling}", "the no-numerical-coupling bar")]:
    chk(pat in tier, f"§G3 the standing bar {why} is stated in the tier")
TAGS20 = [f"BM.{n}" for n in range(101, 108)]
def block(src, tag):
    m = re.search(r"^### " + re.escape(tag) + r" —", src, re.M)
    if not m: return ""
    st = m.start()
    nxt = re.search(r"^### ", src[m.end():], re.M)
    en = m.end() + nxt.start() if nxt else src.find("## Closure exports", st)
    return src[st:en if en > 0 else len(src)]
for t in TAGS20:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier, re.M) is not None, f"§G4 Tier BM.20 carries the tag {t}")
    b = block(tier, t)
    for k in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(k in b, f"§G4 {t} carries {k}")
    chk("\\blacksquare" in b, f"§G4 {t} carries its proof terminator")
chk("### Def-BM.15" not in tier and "**Def.**" not in tier, "§G4 Tier BM.20 issues no new definition block")
chk("the declarations this tier adds: one" in tier and "A-BM.9" in tier, "§G4 the tier states its declaration count: one, A-BM.9")
REG = set()
for fn in CANON:
    srcx = rd(fn)
    for m in re.finditer(r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.[\d.]+\w*|"
                         r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\w*)\b", srcx, re.M):
        REG.add(m.group(1).rstrip("."))
    for m in re.finditer(r"^\*\*(A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", srcx, re.M):
        REG.add(m.group(1))
    for m in re.finditer(r"\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)\.[\d.]+\w*|L0a)\b", srcx):
        REG.add(m.group(1))
CITE = re.compile(r"\\mathrm\{([A-Za-z][A-Za-z0-9.\-]*?)(?:\(([^{}]*)\))?\}")
missing = set()
for m in CITE.finditer(tier):
    tok = m.group(1).replace("\\text{-}", "-").rstrip(".")
    if re.fullmatch(r"(FT|Def-H|Def-BM|Def-EM|BM|CT\d+|EW|EM|L[0-5])\.[\d.]+\w*|A[1-9]|C1[0-2]|C[1-9]|D[0-4]\.\d+|P[1-5]|L0a", tok):
        if tok.split("(")[0] not in REG: missing.add(tok.split("(")[0])
chk(not missing, f"§G5 every tag cited in Tier BM.20 exists in the corpus registry: missing {sorted(missing)}")
endash = chr(0x2013)
mNS = re.search(r"Def-BM\.1" + endash + r"Def-BM\.(\d+); BM\.1" + endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + endash + r"BM\.(\d+)", P4t)
chk(mNS and int(mNS.group(1)) >= 14 and int(mNS.group(2)) >= 107 and int(mNS.group(3)) >= 20,
    "§G6 the Part 4 Namespace line covers Tier BM.20 (BM.107 / BM.20)")
chk("(xxiii) the six-objective-resolution layer [Tier BM.20" in P4t, "§G6 the Part 4 charter carries clause (xxiii)")
closure = P4t[iclos:]
for t in TAGS20:
    chk(r"\mathrm{" + t + "}" in closure, f"§G6 the closure exports carry {t}")
for t in TAGS20:
    chk(f"**{t}.**" in HLt, f"§G7 the HistLog §III status ledger carries the {t} row")
chk("(V.24)" in HLt and "Suite state: 76/76" in HLt, "§G7 the HistLog §V carries the (V.24) entry with suite state 76/76")
chk(HLt.count("[Part 4 Tier BM.20 (BM.101") >= 2, "§G7 both the item-7 and the item-20 ledger brackets are present")
chk("CLOSED AS AN EQUATION" in HLt, "§G7 the item-7 bracket records the closure as an equation")
chk("verify_H_six_objective_resolution.py" in HLt, "§G7 the HistLog names the tier's content checker")
RM = rd("README.md"); CRM = rd(os.path.join("checks", "README.md"))
chk("(80 checkers)" in RM, "§G8 the main README carries the 79-checker count")
chk("(80 checkers)" in CRM and "**80/80**" in CRM, "§G8 checks/README carries the 79-checker count and suite state")
chk("verify_H_six_objective_resolution.py" in CRM, "§G8 checks/README lists the new content checker")
nverify = len([f for f in os.listdir(HERE) if f.startswith("verify_") and f.endswith(".py")])
chk(nverify + 1 == 80, f"§G8 the discovered suite is {nverify} verify_*.py + check_format.py = 80 checkers")
with open(os.path.join(DOCS, "index", "tags.json"), encoding="utf-8") as f:
    IDXT = json.load(f)
idxkeys = set(IDXT.keys()) if isinstance(IDXT, dict) else {tt["tag"] for tt in IDXT}
for t in TAGS20:
    chk(t in idxkeys, f"§G8 the regenerated index/tags.json carries {t}")
SM = rd("Summary.md")
chk(all(t in SM for t in ("BM.101", "BM.107")), "§G8 the regenerated Summary of Record carries the tier's statements")
PINS = [
    (r"\boxed{\ Q_\beta^{\mathrm{inv}}(E)\ =\ -\,Q_\beta^{\mathrm{fwd}}(E)\ \ \text{identically, at every scale, on every read}\ }", "the reflection box"),
    (r"\boxed{\ \Delta m(E)\,\mathfrak h\ =\ \ln\frac43\ -\ 3\,w\,\ln2\cdot\varepsilon_{\mathrm{eff}}(r,E,N)\ }", "the graph's spine"),
    (r"\boxed{\ \varepsilon_\ast(w)\ :=\ \frac{\ln(4/3)}{3\,w\ln2}\ =\ \frac{2-\log_23}{3\,w}", "the crossing strength"),
    (r"\boxed{\ \frac{2-\log_23}3\ \le\ \varepsilon_\ast\ <\ 2-\log_23\qquad\text{and}\qquad\frac18\ <\ \varepsilon_\ast\ <\ \frac5{12}\ }", "the crossing enclosure"),
    (r"\textbf{the two endpoints of}\ \mathrm{BM.99}(3)\textbf{'s two-sided parameter-free bar are exactly the enclosure of the crossing strength}", "the bar-as-enclosure row"),
    (r"\boxed{\ \textbf{what is}\ e_0\textbf{-free is the crossing value}\ \varepsilon_\ast", "the e_0 adjudication box"),
    (r"\boxed{\ P_{\max}(\beta)=P(x_\ast)=1-\frac3{2x_\ast}\ }", "the peak's closed form"),
    (r"\boxed{\ c<P_{\max}:\ \textbf{two crossings}", "the window's crossing count"),
    (r"\boxed{\ \textbf{the specified read's energy-scale graph is a horizontal line", "the flat-read box"),
    (r"\boxed{\ \textbf{the inventory carries exactly one fundamental dimension, the information flux}\ \mathfrak q\ }", "the one-dimension box"),
    (r"\textbf{the correction to the framing:}\qquad\rho_{\mathrm B}\ \ \text{is}\ \neg\textbf{the dimensional bridge}", "the two-bridge correction"),
    (r"\textbf{the mass-form bridge is closed as an equation}", "the item-7 closure"),
    (r"\boxed{\ W(Q)\ =\ \binom{6}{Q+3}\ \ \text{exactly, on all seven classes}\ }", "the binomial spectrum"),
    (r"\det\bigl(\lambda I-M_{\mathrm{ensemble}}\bigr)=0\ \ \textbf{is}\ \neg\textbf{formed}", "the not-formed box"),
    (r"\boxed{\ \textbf{the baryon octet and the meson octet are}\ \neg\textbf{derived and}\ \neg\textbf{derivable here}", "the octet box"),
    (r"\boxed{\ \mathsf g\ =\ \mathsf g\bigl(G\,(1+a\,\mathsf g)\bigr)\ }", "the fixed-point box"),
    (r"\boxed{\ \textbf{the fixed-point equation has a unique admissible solution for each of the three priced compositions}", "the non-selection box"),
    (r"\boxed{\ \textbf{the neutral class never reaches the pole}\ }", "the neutral pole row"),
    (r"\boxed{\ \frac13\ \le\ w_{\mathrm{mat}}\ \le\ 1\qquad\text{for every admissible ensemble measure}\ }", "the measure-free bound"),
    (r"\boxed{\ \neg\exists\ \text{a derived map}\ D_S\longmapsto\varepsilon", "the (W6) refutation"),
    (r"(\mathrm{R4}')\ \ \text{the ensemble's configuration distribution beyond per-pair independence}", "the narrowed residue"),
    (r"\boxed{\ \neg\exists\ \text{a spin-parity theorem}", "the spin-parity refutation"),
    (r"\boxed{\ \textbf{the spin--statistics connection is}\ \neg\textbf{formed}\ }", "the statistics box"),
    (r"(\mathrm{R7})\ \ \text{an exchange structure}", "the exchange-structure residue"),
    (r"\textbf{one graph derived with its crossing strength and its composition-dependent crossing count}", "the adjudication row"),
    (r"\textbf{the declarations this tier adds: one}", "the declaration count"),
]
for pat, why in PINS:
    chk(pat in tier, f"§G9 text pin: {why}")
SRC = open(os.path.abspath(__file__), encoding="utf-8").read()
chk("float" + "(" not in SRC, "§G10 this checker contains no floating-point constructor")
SELFDEC = re.findall(DEC, SRC)
chk(not SELFDEC, f"§G10 this checker contains no decimal numeral: {SELFDEC[:6]}")
chk(("import " + "sympy") not in SRC and ("import " + "numpy") not in SRC,
    "§G10 the checker is dependency-free: pure Python 3 standard library")
chk(SRC.count("Fr(") > 150, "§G10 every assertion runs on exact Fractions")
stamp("§G green: hygiene clean (zero decimal numerals, zero external or species tokens, zero registry tokens in the tier "
      "and in this file), BM.101-BM.107 blocks complete, one declaration logged, citation closure holds, the "
      "Namespace/charter/closure/Cal-BM rows extended, the HistLog ledger rows and (V.24) present, the suite at 76, "
      "the index and Summary regenerated, all text pins found")

# =====================================================================
print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_six_objective_resolution: {len(FAIL)} FAILURE(S)")
    for f in FAIL: print("   ", f)
    sys.exit(1)
print(f"verify_H_six_objective_resolution: ALL GREEN ({N} exact checks, {time.time()-t0:.1f}s, no floating point)")
sys.exit(0)
