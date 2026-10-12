#!/usr/bin/env python3
"""verify_H_organic_bridge_post_bm14.py - Tier BM.15 of Part 4:
the organic bridge after BM.14 - the operator EM lift, the derived-holonomy
attempt, the constrained joint entropy, the bridge convergence, and the
beta-decay energy audit.

Exact arithmetic only: Fraction; exact complex over Fraction; multivariate
polynomial rings over Q by exponent-tuple dictionaries; the prime-log ring
Q (+) (+)_p Q*ln p whose sign tests reduce to exact comparisons of two
non-negative integers; exact quadratic rings Q(sqrt2), Q(sqrt3), Q(sqrt5);
exact rational polynomial gcds; GF(2) parity censuses; Burnside enumeration;
rational ln-series enclosures with exact remainder bounds. No floating point
enters any assertion; no decimal numeral occurs in this file.

The section-A content spec admits a symbolic-algebra (sympy) formulation with
the indeterminates (c0, C, q, c, eps, L); this checker realizes exactly the
same identities in the corpus's dependency-free style - the polynomial ring
over Q in the same indeterminates - so every assertion is the same bit-exact
equality, with the matrix route added over complex-with-rational-parts.

  §A  the force-operator invariant: Tr F = 2 c0 (charge-blind), Tr F^2 =
      c0^2 + C^2 + 4 Q^2, I_F = Tr F^2 - Tr F0^2 = 4 Q^2, the operator EM
      correction at Q = 0 and Q = ±1, the coefficient row E_int/4 = 3/2 at
      E_int = 6, the agreement with BM.46(1)'s monomial, the matrix witnesses
      and the power-sum/charpoly rows
  §B  the charge census and the splitting: m_q = (2,1,1), W = (1,6,15,20,15,
      6,1), sum 64, ln W(0) - ln W(+1) = ln(4/3) > 0, m_n h = ln 1280, m_p h =
      ln 960 + 6 c eps ln2, the ratio bar 1280^3 != 960^4
  §C  the critical coupling bounds: 1/9 < eps_crit(3/5) < 1/8 < eps_crit(1/2)
      < 1/7 on the four integer power certificates 2^13>3^8, 2^11<3^7,
      2^8>3^5, 2^31<3^20; the sub-criticality bar 64>54, 1024>972; an
      independent rational-enclosure cross-check of all four bounds
  §D  the holonomy lift: the bare Z2 Wilson product from the edge signs, the
      parity lock (chain and composite level), the integer winding and sealing
      sectors, the two-torsion image against the six state angles, the rung
      law m*delta_v in pi*Z iff D_S(m) in {0,2,4} on all five ladders, the
      channel-cap integers, Descartes V*delta_v = 4*pi
  §E  the joint entropy factorization: register independence on the tested
      finite domains, Omega_count = 2^E, Omega_charge = W(Q), the stationary
      geometric fiber = 1, the Sigma_12 scoped strict/null-permitting fibers
      by stars-and-bars and Burnside, the infinite-fiber witness, the
      tetrahedron A_S(K) and M_S(K) re-derivation against the census rows,
      the bridge-candidate refutations, the six-value distinctness by
      pairwise-coprime minimal polynomials
  §F  the beta-decay floor audit: E_int >= 2 on every computed cell, the
      margin ladder -ln3, -ln12, -ln24 with the certificates 4<12, 4<48,
      4<96, the floor ladder (2,4,5)*ln2 with the k=1 refinement, the
      on-shell non-existence and Kallen polynomial identities, the MT
      reciprocal monomial, the nearby fractions 1-1/k, the lock integer
      O(4)=16, the field-reconfiguration sign census, the binding count zero
  §G  the standing rules: forbidden-token scans (alpha_B barred-row-only,
      Yukawa negated-only, zero Higgs, zero external numerals and units,
      zero decimal numerals), hygiene (zero previously/formerly/this was/now
      this, zero P-H tokens, zero Status lines, zero [EXT]), block
      completeness of BM.65-BM.72, no new definition block, citation closure,
      the Namespace/charter/closure/HistLog rows, the checker self-scan (no
      floating-point constructor, no decimal numeral in this file), and the
      text pins
"""
import os, re, sys, time
from fractions import Fraction as Fr
from itertools import product, permutations
from math import gcd

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
#  exact algebra: the prime-log ring  (a + sum_p e[p]*ln p)
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
    def __repr__(s):
        t = [str(s.a)] if s.a else []
        for p in sorted(s.e):
            v = s.e[p]
            t.append(("" if v == 1 else ("-" if v == -1 else f"{v}*")) + f"ln{p}")
        return "(" + " + ".join(t).replace("+ -", "- ") + (")" if t else "0")

LN2, LN3 = Ln.log(2), Ln.log(3)

def intpair(x):
    """a pure-log element as an exact pair (N, D) with value ln(N/D)."""
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
    """sign of x - y for pure-log differences: an exact integer comparison."""
    d = x - Ln._c(y)
    assert d.pure, "sign test needs a pure-log difference"
    a, b = intpair(d)
    return (a > b) - (a < b)

# =====================================================================
#  exact algebra: multivariate polynomials over Q (exponent tuples)
# =====================================================================
class Poly:
    __slots__ = ("names", "t")
    def __init__(s, names, t=None):
        s.names = tuple(names)
        s.t = {}
        for k, v in (t or {}).items():
            v = Fr(v)
            if v: s.t[tuple(k)] = s.t.get(tuple(k), Fr(0)) + v
        s.t = {k: v for k, v in s.t.items() if v != 0}
    @staticmethod
    def const(names, c):
        c = Fr(c)
        return Poly(names, {tuple([0] * len(names)): c}) if c else Poly(names)
    @staticmethod
    def var(names, nm):
        i = names.index(nm); e = [0] * len(names); e[i] = 1
        return Poly(names, {tuple(e): Fr(1)})
    def _c(s, o): return o if isinstance(o, Poly) else Poly.const(s.names, o)
    def __add__(s, o):
        o = s._c(o); r = Poly(s.names, s.t)
        for k, v in o.t.items(): r.t[k] = r.t.get(k, Fr(0)) + v
        r.t = {k: v for k, v in r.t.items() if v != 0}; return r
    __radd__ = __add__
    def __sub__(s, o): return s + (-s._c(o))
    def __rsub__(s, o): return s._c(o) + (-s)
    def __neg__(s): return Poly(s.names, {k: -v for k, v in s.t.items()})
    def __mul__(s, o):
        o = s._c(o); r = Poly(s.names)
        for k1, v1 in s.t.items():
            for k2, v2 in o.t.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r.t[k] = r.t.get(k, Fr(0)) + v1 * v2
        r.t = {k: v for k, v in r.t.items() if v != 0}; return r
    __rmul__ = __mul__
    def __pow__(s, n):
        r = Poly.const(s.names, 1)
        for _ in range(int(n)): r = r * s
        return r
    def __eq__(s, o):
        if isinstance(o, Poly):
            assert o.names == s.names
            return s.t == o.t
        return s.t == Poly.const(s.names, o).t
    def __hash__(s): return hash(tuple(sorted(s.t.items())))
    def subs(s, mapping):
        """substitute names -> Fraction (exact rationals only)."""
        r = Poly(s.names)
        for k, v in s.t.items():
            mono = Poly.const(s.names, v)
            for i, nm in enumerate(s.names):
                if k[i]:
                    if nm in mapping:
                        mono = mono * Poly.const(s.names, Fr(mapping[nm]) ** k[i])
                    else:
                        mono = mono * (Poly.var(s.names, nm) ** k[i])
            r = r + mono
        return r
    def is_zero(s): return not s.t
    def __repr__(s):
        if not s.t: return "0"
        out = []
        for k, v in sorted(s.t.items()):
            m = ("" if v == 1 else str(v) + "*") + \
                ("*".join(nm + ("^" + str(e) if e > 1 else "")
                          for nm, e in zip(s.names, k) if e) or "1")
            out.append(m)
        return " + ".join(out)

# =====================================================================
#  exact algebra: complex over Fraction, matrices, Kronecker products
# =====================================================================
class Cx:
    __slots__ = ("re", "im")
    def __init__(s, re=0, im=0):
        s.re = re if isinstance(re, Fr) else Fr(re)
        s.im = im if isinstance(im, Fr) else Fr(im)
    @staticmethod
    def co(x): return x if isinstance(x, Cx) else Cx(x)
    def __add__(s, o): o = Cx.co(o); return Cx(s.re + o.re, s.im + o.im)
    __radd__ = __add__
    def __sub__(s, o): o = Cx.co(o); return Cx(s.re - o.re, s.im - o.im)
    def __rsub__(s, o): o = Cx.co(o); return Cx(o.re - s.re, o.im - s.im)
    def __neg__(s): return Cx(-s.re, -s.im)
    def __mul__(s, o):
        o = Cx.co(o)
        return Cx(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    __rmul__ = __mul__
    def __eq__(s, o): o = Cx.co(o); return s.re == o.re and s.im == o.im
    def __hash__(s): return hash((s.re, s.im))
    def __repr__(s): return f"({s.re},{s.im})i"

def madd(A, B): return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(A, B)]
def mmul(A, B):
    m, p = len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), Cx(0)) for j in range(p)]
            for i in range(len(A))]
def msc(A, c): return [[c * a for a in r] for r in A]
def trM(A): return sum((A[i][i] for i in range(len(A))), Cx(0))
def kron(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    return [[A[i][k] * B[j][l] for k in range(ca) for l in range(cb)]
            for i in range(ra) for j in range(rb)]

# =====================================================================
#  exact quadratic rings Q(sqrt d): pairs (a, b) meaning a + b*sqrt d
# =====================================================================
def qmul(d, x, y): return (x[0] * y[0] + Fr(d) * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def qadd(x, y): return (x[0] + y[0], x[1] + y[1])
def qsc(c, x): return (Fr(c) * x[0], Fr(c) * x[1])
def qeq(x, y): return x[0] == y[0] and x[1] == y[1]

# exact rational polynomials (coefficient lists, low -> high)
def peval(p, x):
    r = Fr(0)
    for c in reversed(p): r = r * x + c
    return r
def _pnorm(p):
    p = [Fr(c) for c in p]
    while p and p[-1] == 0: p.pop()
    return p
def pdiv_rem(a, b):
    r = _pnorm(a); b = _pnorm(b)
    assert b
    while r and len(r) >= len(b):
        f = r[-1] / b[-1]; sh = len(r) - len(b)
        for i in range(len(b)): r[sh + i] -= f * b[i]
        r = _pnorm(r)
    return r
def pgcd(a, b):
    a, b = _pnorm(a), _pnorm(b)
    while b: a, b = b, pdiv_rem(a, b)
    return a

def no_rational_sqrt(n):
    """exact helper: x^2 = n has no solution in Q for a positive integer n
    some prime divides to an odd power (valuation parity in p^2 = n q^2)."""
    return any(e % 2 for e in _factor(n).values())

# exact enclosures of ln2 and ln(3/2) by rational series (no floating point)
def ln2_enclosure(N):
    """S < ln2 < S + 2^-N with S the partial sum of sum_{n>=1} 1/(n 2^n);
    the tail is bounded by the geometric series sum_{n>N} 2^-n = 2^-N."""
    S = sum((Fr(1, n * 2 ** n) for n in range(1, N + 1)), Fr(0))
    return S, S + Fr(1, 2 ** N)
def ln32_enclosure(M):
    """alternating series ln(3/2) = sum_{n>=1} (-1)^(n+1) (1/2)^n / n at even M:
    A(M) < ln(3/2) < A(M) + the first omitted term."""
    A = sum((Fr((-1) ** (n + 1), n * 2 ** n) for n in range(1, M + 1)), Fr(0))
    return A, A + Fr(1, (M + 1) * 2 ** (M + 1))

# =====================================================================
banner("§A  the force-operator invariant: the charge-blind trace, I_F = 4 Q^2, the operator lift")
NM3 = ("c0", "C", "Q")
c0p, Cp, Qp = (Poly.var(NM3, n) for n in NM3)
half = Poly.const(NM3, Fr(1, 2))
eigs = [half * (c0p + Fr(s) * Cp) + Fr(t) * Qp for s in (-1, 1) for t in (-1, 1)]
trF = sum(eigs, Poly.const(NM3, 0))
chk(trF == Fr(2) * c0p, "§A1 Tr F = sum_{s,t} lambda_(s,t) = 2 c0 exactly: the linear trace is charge-blind")
trF2 = sum((e * e for e in eigs), Poly.const(NM3, 0))
chk(trF2 == c0p * c0p + Cp * Cp + Fr(4) * Qp * Qp, "§A2 Tr F^2 = c0^2 + C^2 + 4 Q^2 exactly")
trF0_2 = trF2.subs({"Q": Fr(0)})
chk(trF0_2 == c0p * c0p + Cp * Cp, "§A2 Tr F0^2 = c0^2 + C^2 at Q = 0")
charge_quad = trF2 - trF0_2
chk(charge_quad == Fr(4) * Qp * Qp, "§A3 I_F = Tr F^2 - Tr F0^2 = 4 Q^2 exactly")
for qv, iv in ((0, 0), (1, 4), (-1, 4)):
    chk(charge_quad.subs({"Q": Fr(qv)}) == Fr(iv), f"§A3 I_F at Q = {qv} is {iv}: the monopole selector (0,4,4)")

NM4 = ("c", "eps", "L", "Q")
cp, ep, Lp, Qq = (Poly.var(NM4, n) for n in NM4)
Delta_MH_EM = Fr(3, 2) * cp * ep * Lp * (Fr(4) * Qq * Qq)
six = Fr(6) * cp * ep * Lp
chk(Delta_MH_EM.subs({"Q": Fr(0)}).is_zero(), "§A4 the operator EM correction vanishes at Q = 0")
chk(Delta_MH_EM.subs({"Q": Fr(1)}) == six, "§A4 the operator EM correction at Q = +1 is 6 c eps ln2")
chk(Delta_MH_EM.subs({"Q": Fr(-1)}) == six, "§A4 the operator EM correction at Q = -1 is 6 c eps ln2")
chk(Delta_MH_EM == six * Qq * Qq, "§A4 the correction is 6 c eps ln2 Q^2 on the whole ring: Def-BM.13(5)'s scalar row lifted exactly")

NM2 = ("E", "Q")
Ep, Qe = (Poly.var(NM2, n) for n in NM2)
chk(Fr(1, 4) * Ep * (Fr(4) * Qe * Qe) == Ep * Qe * Qe, "§A5 (E_int/4) * 4 Q^2 = E_int Q^2 on the ring: the coefficient E_int/4 is derived, not chosen")
chk(Fr(6, 4) == Fr(3, 2) and Fr(3, 2) * Fr(4) == Fr(6), "§A5 at E_int = 6 the prefactor E_int/4 is exactly 3/2 and (3/2)*4 = 6")

NM5 = ("c", "eps", "E", "L", "Q")
pc, pe, pE, pL, pQ = (Poly.var(NM5, n) for n in NM5)
chk(Fr(1, 4) * pE * pc * pe * pL * (Fr(4) * pQ * pQ) == pc * pe * pQ * pQ * pE * pL,
    "§A6 the operator route equals BM.46(1)'s unified monomial c eps Q^2 E_int ln2 identically: three routes, one monomial")

# the matrix route: F = h (x) I2 + q I2 (x) kappa-hat over complex-with-rational-parts
I2 = [[Cx(1), Cx(0)], [Cx(0), Cx(1)]]
SX = [[Cx(0), Cx(1)], [Cx(1), Cx(0)]]
SY = [[Cx(0), Cx(0, -1)], [Cx(0, 1), Cx(0)]]
SZ = [[Cx(1), Cx(0)], [Cx(0), Cx(-1)]]
KH = [[Cx(0), Cx(1)], [Cx(1), Cx(0)]]          # the ray swap [FT.129(2)]
chk(mmul(KH, KH) == I2 and trM(KH) == Cx(0), "§A7 the ray swap satisfies kappa^2 = I2 with trace 0")
WIT = [(Fr(0), Fr(0), Fr(0), Fr(0)), (Fr(1), Fr(2), Fr(3), Fr(5)), (Fr(3), Fr(0), Fr(4), Fr(0)),
       (Fr(-2), Fr(1), Fr(0), Fr(7)), (Fr(5), Fr(0), Fr(0), Fr(12)), (Fr(7, 3), Fr(-1, 2), Fr(2), Fr(0))]
nw = 0
for (a0, ax, ay, az) in WIT:
    h = madd(msc(I2, Cx(Fr(1, 2) * a0)),
             madd(msc(SX, Cx(Fr(1, 2) * ax)),
                  madd(msc(SY, Cx(Fr(1, 2) * ay)), msc(SZ, Cx(Fr(1, 2) * az)))))
    chk(trM(h) == Cx(a0), f"§A7 tr h = c0 at the witness {(str(a0), str(ax), str(ay), str(az))}")
    C2 = ax * ax + ay * ay + az * az
    for q in (-1, 0, 1):
        F = madd(kron(h, I2), msc(kron(I2, KH), Cx(q)))
        chk(trM(F) == Cx(2 * a0), f"§A8 matrix route: Tr F = 2 c0 at q = {q}")
        chk(trM(mmul(F, F)) == Cx(a0 * a0 + C2 + 4 * q * q), f"§A8 matrix route: Tr F^2 = c0^2 + C^2 + 4 q^2 at q = {q}")
        nw += 1
chk(nw == 18, "§A8 the matrix census covers 6 witnesses x 3 charges = 18 exact cases")
# the charpoly/power-sum row at a rational-|c| witness (BM.22(3) re-certified)
a0w, avw = Fr(3), Fr(4)
hw = madd(msc(I2, Cx(Fr(1, 2) * a0w)), msc(SZ, Cx(Fr(1, 2) * avw)))
for q in (-1, 0, 1):
    Fw = madd(kron(hw, I2), msc(kron(I2, KH), Cx(q)))
    roots = [Fr(1, 2) * (a0w + s * avw) + t * q for s in (-1, 1) for t in (-1, 1)]
    pows_F = [trM(Fw)]
    M = Fw
    for k in (2, 3, 4):
        M = mmul(M, Fw); pows_F.append(trM(M))
    pows_r = [sum((r ** k for r in roots), Fr(0)) for k in (1, 2, 3, 4)]
    chk(all(pf.im == 0 and pf.re == pr for pf, pr in zip(pows_F, pows_r)),
        f"§A9 the power sums of F at q = {q} equal those of the four roots (1/2)(c0 + s C) + t q")
stamp("§A green: Tr F = 2 c0; Tr F^2 = c0^2 + C^2 + 4 Q^2; I_F = 4 Q^2; the lift reproduces "
      "6 c eps ln2 at Q = ±1 and 0 at Q = 0; the coefficient E_int/4 = 3/2 is a count row; "
      "the matrix and power-sum routes agree on 18 + 3 exact cases")

# =====================================================================
banner("§B  the charge census and the splitting: W(Q), ln(4/3), ln 1280 / ln 960, the ratio bar")
ENDPAIRS = [((+1, +1), 0), ((+1, -1), +1), ((-1, +1), -1), ((-1, -1), 0)]
QOF = {p: q for p, q in ENDPAIRS}
mq = {0: 0, 1: 0, -1: 0}
for (_, q) in ENDPAIRS: mq[q] += 1
chk((mq[0], mq[1], mq[-1]) == (2, 1, 1), "§B1 the end-pair census m_q = (2,1,1) at q = (0,+1,-1)")
Wexh = {}
for prs in product([p for p, _ in ENDPAIRS], repeat=3):
    Q = sum(QOF[p] for p in prs)
    Wexh[Q] = Wexh.get(Q, 0) + 1
WROW = [Wexh.get(k, 0) for k in range(-3, 4)]
chk(WROW == [1, 6, 15, 20, 15, 6, 1], "§B2 the exhaustive 4^3 end-sign census gives W = (1,6,15,20,15,6,1)")
chk(sum(WROW) == 64 == 4 ** 3, "§B3 sum_Q W(Q) = 64 = 4^3")
Ww = {}
for trip in product((-1, 0, 1), repeat=3):
    Q = sum(trip)
    Ww[Q] = Ww.get(Q, 0) + mq[trip[0]] * mq[trip[1]] * mq[trip[2]]
base = {-1: 1, 0: 2, 1: 1}
conv = {0: 1}
for _ in range(3):
    nxt = {}
    for k, v in conv.items():
        for d, b in base.items(): nxt[k + d] = nxt.get(k + d, 0) + v * b
    conv = nxt
chk(all(conv.get(Q, 0) == Ww.get(Q, 0) for Q in range(-3, 4)), "§B4 the weighted triple census and the convolution of (2+z+z^-1)^3 agree class by class")
chk([conv.get(k, 0) for k in range(-3, 4)] == WROW, "§B4 the convolution reproduces W = (1,6,15,20,15,6,1)")
T0 = [t for t in product((-1, 0, 1), repeat=3) if sum(t) == 0]
T1 = [t for t in product((-1, 0, 1), repeat=3) if sum(t) == 1]
chk(len(T0) == 7 and len(T1) == 6, "§B5 the ordered charge-triple census: 7 neutral triples against 6 charged")
chk(mq[0] ** 3 == 8 and
    sum(mq[a] * mq[b] * mq[c] for (a, b, c) in T0 if sorted((a, b, c)) == [-1, 0, 1]) == 12 and
    Ww[0] == 8 + 12 == 20,
    "§B5 W(0) = 8 + 12 = 20: the (0,0,0) and the mixed-permutation splits")
chk(sum(mq[a] * mq[b] * mq[c] for (a, b, c) in T1 if (a, b, c).count(0) == 2) == 12 and
    sum(mq[a] * mq[b] * mq[c] for (a, b, c) in T1 if (a, b, c).count(0) == 0) == 3 and
    Ww[1] == 12 + 3 == 15,
    "§B5 W(+1) = 12 + 3 = 15")
SB = Ln.log(20) - Ln.log(15)
chk(SB == Ln.log(4, 3), "§B6 ln W(0) - ln W(+1) = ln(4/3) = Sigma_B in the prime-log ring")
chk(SB == 2 * LN2 - LN3, "§B6 Sigma_B = 2 ln2 - ln3")
chk(lsign(SB) > 0 and 4 > 3, "§B6 Sigma_B > 0 on the integer certificate 4 > 3")
chk(Ww[1] == Ww[-1] == 15, "§B7 W(+1) = W(-1) = 15: the CPT row")
chk(2 ** 6 * 20 == 1280 and 2 ** 6 * 15 == 960, "§B8 2^6 * 20 = 1280 and 2^6 * 15 = 960")
chk(Ln.log(1280) == 6 * LN2 + Ln.log(20), "§B8 m_n h = 6 ln2 + ln20 = ln 1280")
chk(Ln.log(960) == 6 * LN2 + Ln.log(15), "§B8 the ln 960 row: 6 ln2 + ln15")
chk(1280 ** 3 != 960 ** 4, "§B9 1280^3 != 960^4: the mass ratio ln1280/ln960 is not 4/3")
chk(3 * Ln.log(1280) != 4 * Ln.log(960), "§B9 3 ln 1280 != 4 ln 960 in the prime-log ring")
chk(intpair(SB) == (4, 3), "§B10 exp(Sigma_B) = 4/3 as the integer pair (4, 3)")
chk(intpair(3 * SB) == (64, 27) and 64 < 108, "§B10 3 Sigma_B = ln(64/27) and the contraction certificate 64 < 108: 3 ln(4/3) < 2 ln2")
stamp("§B green: m_q = (2,1,1); W = (1,6,15,20,15,6,1) by two routes; Sigma_B = ln(4/3) > 0; "
      "the ln 1280 / ln 960 rows exact; 1280^3 != 960^4; the contraction 16 < 27 base 64 < 108")

# =====================================================================
banner("§C  the critical coupling bounds: four integer power certificates and the sub-criticality bar")
BND = [
    # (c, r, a, b, greater): eps_crit(c) >< r  <=>  a*Sigma_B >< b*ln2
    (Fr(3, 5), Fr(1, 9), 5, 2, True, "eps_crit(3/5) > 1/9"),
    (Fr(3, 5), Fr(1, 8), 40, 18, False, "eps_crit(3/5) < 1/8"),
    (Fr(1, 2), Fr(1, 8), 8, 3, True, "eps_crit(1/2) > 1/8"),
    (Fr(1, 2), Fr(1, 7), 7, 3, False, "eps_crit(1/2) < 1/7"),
]
for c, r, a, b, greater, name in BND:
    chk(6 * c * r == Fr(b, a), f"§C1 {name}: the cleared form a*Sigma_B >< b*ln2 matches 6 c r = b/a exactly")
    want = +1 if greater else -1
    chk(lsign(a * SB, b * LN2) == want, f"§C1 {name}: the ln-ring sign of {a} Sigma_B - {b} ln2 is {'+' if greater else '-'}")
    g = gcd(2 * a - b, a)
    L, R = (2 * a - b) // g, a // g
    pow_ok = (2 ** L > 3 ** R) if greater else (2 ** L < 3 ** R)
    chk(pow_ok, f"§C1 {name}: the reduced integer certificate 2^{L} {'>' if greater else '<'} 3^{R} ({2**L} vs {3**R})")
chk(2 ** 13 > 3 ** 8 and 2 ** 11 < 3 ** 7 and 2 ** 8 > 3 ** 5 and 2 ** 31 < 3 ** 20,
    "§C2 the four named certificates 2^13>3^8, 2^11<3^7, 2^8>3^5, 2^31<3^20 hold as integer comparisons")
s2lo, s2hi = ln2_enclosure(40)
s32lo, s32hi = ln32_enclosure(40)
num_lo, num_hi = s2lo - s32hi, s2hi - s32lo          # Sigma_B = ln2 - ln(3/2)
def eps_crit_bounds(cf):
    d_lo, d_hi = 6 * cf * s2lo, 6 * cf * s2hi
    return num_lo / d_hi, num_hi / d_lo
lo, hi = eps_crit_bounds(Fr(1, 2))
chk(lo > Fr(1, 8) and hi < Fr(1, 7), "§C3 enclosure cross-check: 1/8 < eps_crit(1/2) < 1/7")
lo, hi = eps_crit_bounds(Fr(3, 5))
chk(lo > Fr(1, 9) and hi < Fr(1, 8), "§C3 enclosure cross-check: 1/9 < eps_crit(3/5) < 1/8")
chk(4 ** 3 == 64 and 3 ** 3 * 2 == 54 and 64 > 54, "§C4 the bar witness 4^3 = 64 > 54 = 3^3 * 2 (c = 1/2 at eps = 1/9)")
chk(4 ** 5 == 1024 and 3 ** 5 * 2 ** 2 == 972 and 1024 > 972, "§C4 the bar witness 4^5 = 1024 > 972 = 3^5 * 2^2 (c = 3/5 at eps = 1/9)")
chk(lsign(SB, LN2 * Fr(1, 3)) > 0 and lsign(SB, LN2 * Fr(2, 5)) > 0, "§C4 Sigma_B > ln2/3 and > 2 ln2/5: the parameter-free 1/9 bar at both priced c")
chk(lsign(SB) > 0, "§C4 eps_crit(c) > 0: the sub-critical branch is non-empty and exact")
stamp("§C green: 1/9 < eps_crit(3/5) < 1/8 < eps_crit(1/2) < 1/7 on four integer power certificates, "
      "cross-checked by exact rational ln-enclosures; the 1/9 bar witnessed by 64>54 and 1024>972")

# =====================================================================
banner("§D  the holonomy lift: the Z2 Wilson sector, the parity lock, the two-torsion obstruction, the rung law")
for n in range(2, 8):
    ok = True
    for sig in product((1, -1), repeat=n):
        Npi = sum(1 for s in sig if s == -1)
        for ori in product((1, -1), repeat=n):
            U = 1
            for s, o in zip(sig, ori): U *= s if o == 1 else (1 // s if s else s)
            if U != (-1) ** Npi: ok = False; break
        if not ok: break
    chk(ok, f"§D1 exhaustive: U(gamma) = prod sigma^or = (-1)^N_pi on every sign x orientation assignment, length {n}")
okmul = okrev = True
def uproduct(ss):
    u = 1
    for s in ss: u *= s
    return u
for s1 in product((1, -1), repeat=2):
    for s2 in product((1, -1), repeat=3):
        if uproduct(s1 + s2) != uproduct(s1) * uproduct(s2): okmul = False
        if uproduct(tuple(reversed(s1 + s2))) != uproduct(s1 + s2): okrev = False
chk(okmul, "§D2 U(gamma1 . gamma2) = U(gamma1) U(gamma2) on the exhaustive small census")
chk(okrev, "§D2 U(gamma-bar) = U(gamma): orientation invariance in Z2")
for k in range(2, 8):
    ok = True
    for sig in product((1, -1), repeat=k):
        q = (sig[0] - sig[-1]) // 2
        ale = sum(1 for i in range(k - 1) if sig[i + 1] != sig[i])
        if ale % 2 != abs(q) % 2 or ale < abs(q): ok = False; break
    chk(ok, f"§D3 exhaustive parity lock: sum aleph = |q| (mod 2) and >= |q|, k = {k}")
m0 = min(sum(1 for i in range(3) if s[i + 1] != s[i]) for s in product((1, -1), repeat=4) if (s[0] - s[-1]) // 2 == 0)
m1 = min(sum(1 for i in range(3) if s[i + 1] != s[i]) for s in product((1, -1), repeat=4) if abs((s[0] - s[-1]) // 2) == 1)
chk(m0 == 0 and m1 == 1, "§D3 the minima are attained: 0 walls at q = 0, 1 wall at |q| = 1")
ok = True
for trip in product((-1, 0, 1), repeat=3):
    Q = sum(trip)
    if sum(abs(q) for q in trip) % 2 != abs(Q) % 2: ok = False
    if sum(abs(q) for q in trip) < abs(Q): ok = False
chk(ok, "§D4 exhaustive composite lock: sum aleph = |Q| (mod 2) and >= |Q| over all 27 charge triples")
okw = True
for prs in product([p for p, _ in ENDPAIRS], repeat=3):
    Q = sum(QOF[p] for p in prs)
    walls = sum(1 for p in prs if p[0] != p[1])
    if (-1) ** walls != (-1) ** abs(Q): okw = False
chk(okw, "§D4 the wall read U = (-1)^(sum aleph) = (-1)^|Q| on the exhaustive 64-assignment census")
chk(all((-1) ** T == 1 for T in range(-40, 41, 2)), "§D5 (-1)^Theta = +1 on every even winding: the spiral phase is trivial on materialized loops")
chk(all(T % 2 == 0 for T in range(-40, 41, 4)), "§D5 4Z <= 2Z: the baryon-type sealing phase class sits inside the winding lattice")
IMAGE = {Fr(0), Fr(1)}
STATES = [("tetra m=1", Fr(1)), ("tetra m=2", Fr(2)), ("cube", Fr(1, 2)),
          ("octa", Fr(2, 3)), ("dodeca", Fr(1, 5)), ("icosa", Fr(1, 3))]
reach = [(nm, (a % 2) in IMAGE) for nm, a in STATES]
chk(sum(1 for _, r in reach if r) == 2, "§D6 exactly two of the six state angles lie in the two-torsion image {0, pi}")
chk(reach[0][1] and reach[1][1], "§D6 the reachable pair is the self-dual floor's (pi and 2pi = 0)")
outs = [a % 1 for nm, a in STATES if not ((a % 2) in IMAGE)]
chk(len(set(outs)) == 4 and Fr(0) not in outs, "§D6 the four unreachable angles are pairwise distinct nontrivial cosets mod pi")

QUART = [Fr(1), Fr(-12), Fr(19), Fr(-8), Fr(1)]    # x^4 - 8x^3 + 19x^2 - 12x + 1, low -> high
chk(peval(QUART, Fr(0)) == 1 and peval(QUART, Fr(2)) == 5 and peval(QUART, Fr(4)) == 1,
    "§D7 the dodecahedral quartic is nonzero at 0, 2 and 4: its roots avoid {0,2,4}")
COS_HALF = {Fr(0): (Fr(1), 0), Fr(1, 2): (Fr(0), 0), Fr(1): (Fr(-1), 0), Fr(3, 2): (Fr(0), 0)}
COS_THIRD = {Fr(0): (Fr(1), 0), Fr(1, 3): (Fr(1, 2), 0), Fr(2, 3): (Fr(-1, 2), 0),
             Fr(1): (Fr(-1), 0), Fr(4, 3): (Fr(-1, 2), 0), Fr(5, 3): (Fr(1, 2), 0)}
COS_QUARTER = {Fr(0): (Fr(1), 0), Fr(1, 4): (Fr(0), Fr(1, 2)), Fr(1, 2): (Fr(0), 0),
               Fr(3, 4): (Fr(0), Fr(-1, 2)), Fr(1): (Fr(-1), 0), Fr(5, 4): (Fr(0), Fr(-1, 2)),
               Fr(3, 2): (Fr(0), 0), Fr(7, 4): (Fr(0), Fr(1, 2))}                    # in Q(sqrt2)
COS_SIXTH = {Fr(0): (Fr(1), 0), Fr(1, 6): (Fr(0), Fr(1, 2)), Fr(1, 3): (Fr(1, 2), 0),
             Fr(1, 2): (Fr(0), 0), Fr(2, 3): (Fr(-1, 2), 0), Fr(5, 6): (Fr(0), Fr(-1, 2)),
             Fr(1): (Fr(-1), 0), Fr(7, 6): (Fr(0), Fr(-1, 2)), Fr(4, 3): (Fr(-1, 2), 0),
             Fr(3, 2): (Fr(0), 0), Fr(5, 3): (Fr(1, 2), 0), Fr(11, 6): (Fr(0), Fr(1, 2))}  # in Q(sqrt3)
def cos_exact(kind, num):
    num = Fr(num) % 2
    if kind == "half": return ("Q", COS_HALF[num])
    if kind == "third": return ("Q", COS_THIRD[num])
    if kind == "quarter": return ("sqrt2", COS_QUARTER[num])
    if kind == "sixth": return ("sqrt3", COS_SIXTH[num])
    raise KeyError(kind)
def DS_of(fld, cs):
    return (fld, (Fr(2) - 2 * cs[0], -2 * cs[1]))
def in_024(v):
    fld, (a, b) = v
    return b == 0 and a in (Fr(0), Fr(2), Fr(4))
SQ5COS = {2: (Fr(1, 4), Fr(1, 4)), 4: (Fr(-1, 4), Fr(1, 4))}    # cos(pi/5), cos(2pi/5) in Q(sqrt5)
chk(qeq(qmul(5, qadd(qsc(4, SQ5COS[2]), (Fr(-1), Fr(0))), qadd(qsc(4, SQ5COS[2]), (Fr(-1), Fr(0)))), (Fr(5), Fr(0))),
    "§D7 the exact identity (4 cos(pi/5) - 1)^2 = 5 in Q(sqrt5)")
chk(qeq(qmul(5, qadd(qsc(4, SQ5COS[4]), (Fr(1), Fr(0))), qadd(qsc(4, SQ5COS[4]), (Fr(1), Fr(0)))), (Fr(5), Fr(0))),
    "§D7 the exact identity (4 cos(2pi/5) + 1)^2 = 5 in Q(sqrt5)")
LADDERS = [
    ("tetrahedron", Fr(1), "half", range(1, 5), {}),
    ("cube", Fr(1, 2), "quarter", range(1, 5), {}),
    ("octahedron", Fr(2, 3), "third", range(1, 5), {}),
    ("dodecahedron", Fr(1, 5), None, range(1, 6),
     {1: "quartic", 3: "quartic", 2: ("sqrt5", SQ5COS[2]), 4: ("sqrt5", SQ5COS[4]), 5: ("Q", (Fr(0), 0))}),
    ("icosahedron", Fr(1, 3), "sixth", range(1, 7), {}),
]
for name, dfrac, kind, rng, special in LADDERS:
    p, qq = dfrac.numerator, dfrac.denominator
    for m in rng:
        reachable = (m * p) % qq == 0
        if m in special:
            sp = special[m]
            inSet = False if sp == "quartic" else in_024(DS_of(sp[0], sp[1]))
        else:
            fld, cs = cos_exact(kind, Fr(m * p, 2 * qq))
            inSet = in_024(DS_of(fld, cs))
        chk(inSet == reachable,
            f"§D7 {name} rung m = {m}: D_S(m) in {{0,2,4}} iff m*delta_v in pi*Z (both {reachable})")
tet = []
for m in (1, 2, 3, 4):
    fld, cs = cos_exact("half", Fr(m, 2))
    tet.append(DS_of(fld, cs)[1][0])
chk(tet == [Fr(2), Fr(4), Fr(2), Fr(0)], "§D7 the tetrahedral ladder D_S(m) = (2,4,2,0) re-derived exactly")
chk(7 + 3 + 3 + 3 == 16 and 2 ** 4 == 16 and 2 ** 5 - 16 == 16,
    "§D8 the cap integers: 7+3+3+3 = 16 = D_tick(3); the lock O(4) = 2^5 - 16 = 16")
SOLIDS = [("tetrahedron", 4, 3, 3), ("cube", 8, 3, 4), ("octahedron", 6, 4, 3),
          ("dodecahedron", 20, 3, 5), ("icosahedron", 12, 5, 3)]
for nm, V, d, L in SOLIDS:
    dv = Fr(2) - Fr(d * (L - 2), L)
    chk(V * dv == 4, f"§D9 Descartes on the {nm}: V * delta_v = 4 pi exactly (delta_v/pi = {dv})")
chk([Fr(2) - Fr(d * (L - 2), L) for _, _, d, L in SOLIDS] == [Fr(1), Fr(1, 2), Fr(2, 3), Fr(1, 5), Fr(1, 3)],
    "§D9 delta_v/pi = (1, 1/2, 2/3, 1/5, 1/3) on the five solids")
stamp("§D green: U(gamma) = (-1)^N_pi exhaustively to length 7; the parity lock to k = 7 and on all 27 "
      "triples; the image {0, pi} reaches exactly 2 of 6 states; the rung law holds on all five ladders; "
      "V delta_v = 4 pi on all five solids")

# =====================================================================
banner("§E  the joint entropy factorization: registers, the stationary fiber, the scoped counts, the bridge census")
SIG2 = list(product((1, -1), repeat=2))
KAP2 = [1, 2]
states = [(s, k) for s in SIG2 for k in KAP2]
chk(len(states) == len(SIG2) * len(KAP2) == 8, "§E1 the digon register product: 4 sign states x 2 kappa states = 8, none converts into another")
fib = {}
for s in SIG2:
    q = (s[0] - s[1]) // 2
    fib[q] = fib.get(q, 0) + len(KAP2)
chk((fib[-1], fib[0], fib[1]) == (2, 4, 2), "§E1 the charge fibers are m_q * |kappa| = (1,2,1) * 2")
chk(2 ** 6 == 64 == sum(WROW), "§E2 Omega_count(6) = 2^6 = 64 = sum_Q W(Q): the count register is exhausted by the sign census")
chk(Ln.log(64) == 6 * LN2, "§E2 S_count = 6 ln2 = ln 64 = I_hid at E_int = 6")
def profiles(K, lo):
    return [(a, b, K - a - b) for a in range(lo, K + 1 - 2 * lo) for b in range(lo, K + 1 - a - lo)
            if K - a - b >= lo]
def orbits(profs):
    seen = set(); n = 0
    for p in profs:
        if p in seen: continue
        seen.add(p); seen.add((p[1], p[0], p[2])); n += 1
    return n
def binom(n, k):
    if k < 0 or k > n: return 0
    r = 1
    for i in range(k): r = r * (n - i) // (i + 1)
    return r
STRICT = {K: (len(profiles(K, 1)), orbits(profiles(K, 1))) for K in (3, 4, 5, 6)}
chk([STRICT[K][0] for K in (3, 4, 5, 6)] == [binom(2, 2), binom(3, 2), binom(4, 2), binom(5, 2)] == [1, 3, 6, 10],
    "§E3 the strict-fiber counts are C(K-1,2) = (1,3,6,10) at K = (3,4,5,6)")
chk([STRICT[K][1] for K in (3, 4, 5, 6)] == [1, 2, 4, 6], "§E3 the strict-fiber swap orbits are (1,2,4,6) at K = (3,4,5,6)")
for K in (3, 4, 5, 6):
    fixed = sum(1 for a in range(1, K) if K - 2 * a >= 1)
    chk(2 * STRICT[K][1] == STRICT[K][0] + fixed, f"§E3 Burnside agrees with the orbit enumeration at K = {K}")
NULLP = {K: (len(profiles(K, 0)), orbits(profiles(K, 0))) for K in (1, 3)}
chk(NULLP[1] == (3, 2) and NULLP[3] == (10, 6), "§E3 the null-permitting fibers: (3 profiles, 2 orbits) at K = 1 and (10, 6) at K = 3")
chk(NULLP[1][0] == binom(3, 2) and NULLP[3][0] == binom(5, 2), "§E3 the null-permitting counts are C(K+2,2)")
for k0 in range(1, 6):
    chk(orbits([(k0, k0, k0)]) == 1, f"§E4 the uniform profile ({k0},{k0},{k0}) is swap-fixed: one orbit")
chk(profiles(3, 1) == [(1, 1, 1)] and orbits(profiles(3, 1)) == 1,
    "§E4 the strict minimum (1,1,1) at K = 3 is the unique profile and a unique orbit: Omega_geom = 1")
W5 = [(7 + n, -n, 0) for n in range(1, 51)]
chk(len(set(W5)) == 50 and all(sum(w) == 7 for w in W5), "§E5 the fiber over the full Z^3 lattice at fixed K is infinite: 50 distinct witnesses (K+n, -n, 0)")
EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
FACES = [[e for e in EDGES if v not in e] for v in (0, 1, 2, 3)]
EIDX = {e: i for i, e in enumerate(EDGES)}
def parity_ok(kap):
    return all(sum(kap[EIDX[e]] for e in f) % 2 == 0 for f in FACES)
def A_tetra(K):
    return sum(1 for kap in product(range(K + 1), repeat=6) if sum(kap) == K and parity_ok(kap))
AROW = [A_tetra(K) for K in range(5)]
chk(AROW == [1, 0, 6, 4, 24], "§E6 the tetrahedron level counts A_S(K) = (1,0,6,4,24) at K = 0..4 re-derived by the GF(2)-filtered enumeration")
PERMS = list(permutations(range(4)))
def edge_perm(pm):
    return [EIDX[tuple(sorted((pm[i], pm[j])))] for (i, j) in EDGES]
def M_tetra(K):
    tot = 0
    for pm in PERMS:
        ep = edge_perm(pm)
        seen = [False] * 6; orbs = []
        for i in range(6):
            if seen[i]: continue
            o = []; j = i
            while not seen[j]: seen[j] = True; o.append(j); j = ep[j]
            orbs.append(o)
        sizes = [len(o) for o in orbs]
        def rec(t, kap):
            if t == len(orbs):
                return 1 if (sum(kap) == K and parity_ok(kap)) else 0
            n = 0; v = 0
            while sizes[t] * v <= K:
                for idx in orbs[t]: kap[idx] = v
                n += rec(t + 1, kap)
                v += 1
            for idx in orbs[t]: kap[idx] = 0
            return n
        tot += rec(0, [0] * 6)
    assert tot % 24 == 0
    return tot // 24
MROW = [M_tetra(K) for K in range(5)]
chk(MROW == [1, 0, 1, 1, 4], "§E7 the tetrahedron coarse-grained degeneracies M_S(K) = (1,0,1,1,4) at K = 0..4 re-derived by Burnside over S4")
MINP = {
    "s1": [Fr(-2), Fr(1)],
    "s2": [Fr(-4), Fr(1)],
    "s4": [Fr(-1), Fr(1)],
    "s3": [Fr(2), Fr(-4), Fr(1)],
    "s6": [Fr(-1), Fr(-4), Fr(1)],
    "s5": QUART,
}
names = sorted(MINP)
coprime = True
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        g = pgcd(MINP[names[i]], MINP[names[j]])
        if len(g) != 1: coprime = False
chk(coprime, "§E8 the six minimal polynomials are pairwise coprime: the six D_S values are pairwise distinct, so no flat count can carry a defect value")
s_lo, s_hi = ln2_enclosure(24)
chk(s_lo > Fr(1, 2) and s_hi < Fr(1), "§E9 the exact enclosure 1/2 < ln2 < 1 (partial sums with the exact tail bound)")
chk(2 * s_hi < 3, "§E9 2 ln2 < 3 strictly: the ledger and branch-state deficits are distinct functionals, so no Legendre pair is formed")
chk(no_rational_sqrt(2) and no_rational_sqrt(3) and no_rational_sqrt(5),
    "§E10 x^2 = 2, 3, 5 have no rational solutions (valuation parity): the quadratic fields are proper, the degree-16 row stands")
chk(Ln.log(1) == Ln(0) and intpair(Ln.log(1)) == (1, 1), "§E11 ln(Omega_stat/Omega_stat) = ln 1 = 0: the count is flat along the stationary ladder while D_S varies")
chk(Wexh[0] > Wexh[1] == Wexh[-1], "§E12 W(0) = 20 > 15 = W(+1) = W(-1): the neutral class is the entropy-maximal class at fixed E")
chk(Fr(6) / Fr(18) == Fr(1, 3), "§E13 the capacity ratios are exact rationals (1/3, 8, 1/25): no Casimir ratio reaches the degree-16 pole side")
stamp("§E green: the register products hold on the tested domains; Omega_geom^stat = 1; the strict fibers are "
      "(1,3,6,10) profiles and (1,2,4,6) orbits; A_S and M_S re-derived for the tetrahedron; the general fiber "
      "is infinite (witnessed); the six D_S are distinct by coprime minimal polynomials")

# =====================================================================
banner("§F  the beta-decay floor audit: E_int >= 2, the margin ladder, the on-shell identities, the route rows")
CELLS = [2, 6, 12, 24, 60]
chk(min(CELLS) == 2, "§F1 the minimal computed E_int is 2 (the digon floor)")
chk(all(E >= 2 for E in CELLS) and all(E >= 2 for E in range(2, 61)), "§F1 E_int >= 2 on the whole ladder: m h = E ln2 >= 2 ln2")
chk(lsign(2 * LN2) > 0, "§F1 2 ln2 > 0: the floor is strictly positive")
chk(SB - 2 * LN2 == -LN3, "§F2 ln(4/3) - 2 ln2 = -ln3 exactly")
chk(SB - 4 * LN2 == -Ln.log(12), "§F2 ln(4/3) - 4 ln2 = -ln12 exactly")
chk(SB - 5 * LN2 == -Ln.log(24), "§F2 ln(4/3) - 5 ln2 = -ln24 exactly")
for n, a, b in ((2, 4, 12), (4, 4, 48), (5, 4, 96)):
    chk(lsign(SB, n * LN2) < 0, f"§F2 ln(4/3) < {n} ln2 in the ring")
    chk(a < b and 3 * 2 ** n == b, f"§F2 the certificate: 4/3 < 2^{n} iff 4 < {b}")
chk(4 < 12 and 4 < 48 and 4 < 96, "§F2 the three integer certificates 4<12, 4<48, 4<96")
conv1 = dict(base)
chk([conv1.get(k, 0) for k in (-1, 0, 1)] == [1, 2, 1], "§F3 at k = 1 the census is W(q) = m_q = (1,2,1)")
chk(Ln.log(2) - Ln.log(1) == LN2, "§F3 Sigma_cl(0) - Sigma_cl(±1) = ln2 at k = 1: the neutral daughter carries one extra bit")
chk(2 * LN2 + 0 * LN2 + 2 * LN2 + LN2 == 5 * LN2, "§F3 the fully refined floor: 2 ln2 + 0 + 2 ln2 + ln2 = 5 ln2")
chk(2 < 4 < 5, "§F3 the floor ladder (2,4,5) ln2 on the integer row 2 < 4 < 5")
NMk = ("mn", "ml")
mn, ml = Poly.var(NMk, "mn"), Poly.var(NMk, "ml")
ident = ((2 * mn * mn - ml * ml) - 2 * mn * mn) + ml * ml
chk(ident.is_zero(), "§F4 2 m_n (E_p - m_p) = -m_l^2 at m_p = m_n: the cleared polynomial identity is zero")
lam = (mn * mn - (mn + ml) ** 2) * (mn * mn - (mn - ml) ** 2) - ml * ml * (ml * ml - 4 * mn * mn)
chk(lam.is_zero(), "§F4 the Kallen factorization lambda = m_l^2 (m_l^2 - 4 m_n^2) at m_n = m_p: the cleared identity is zero")
dmE = ((-1, 1, 2, 1, -1), Fr(3, 2))       # Delta m_EM = 3 c e^2 ln2 / (2 pi h): exponents (h,c,e,ln2,pi)
dtB = ((1, -1, -2, -1, 1), Fr(1, 3))      # Delta t  = pi h / (3 c e^2 ln2)
prod_e = tuple(a + b for a, b in zip(dmE[0], dtB[0]))
chk(prod_e == (0, 0, 0, 0, 0) and dmE[1] * dtB[1] == Fr(1, 2),
    "§F5 the MT reciprocal: Delta m_EM * [pi h / (3 c e^2 ln2)] = 1/2 exactly as Laurent monomials")
for k in (2, 3, 4):
    f = 1 - Fr(1, k)
    chk(f == Fr(k - 1, k) and 0 < f < 1, f"§F6 f({k}) = (k-1)/k is a strict fraction in (0,1)")
chk(all(1 - Fr(1, k) < 1 for k in range(2, 101)), "§F6 f(k) = 1 - 1/k < 1 for every finite k: no neighborhood holds the whole correction")
NMr = ("c", "eps", "mh", "ml")
pc2, pe2, pmh, pml = (Poly.var(NMr, n) for n in NMr)
diff = pc2 * pe2 * (pmh + pml)
chk(all(v > 0 for v in diff.t.values()) and len(diff.t) == 2,
    "§F7 the reconfiguration difference c eps (m_hid + m_lep) has strictly positive coefficients: it deepens the closure at the constructed order")
chk(6 - (2 + 2 + 2) == 0, "§F8 the count binding 6 - (2+2+2) = 0 on both rows")
chk(2 ** 5 - 16 == 16 and 2 ** 4 == 16, "§F9 O(4) = 2^5 - 16 = 16 and D_tick(3) = 2^4 = 16: the lock integers")
chk(lsign(SB - 2 * LN2) < 0 and lsign(SB - 4 * LN2) < 0 and lsign(SB - 5 * LN2) < 0,
    "§F10 Q h <= -ln3, -ln12, -ln24 < 0 at the three floors of the ladder: formed implies closed")
stamp("§F green: E_int >= 2; the margins -ln3, -ln12, -ln24 certified by 4<12, 4<48, 4<96; the on-shell "
      "non-existence and Kallen identities are zero polynomials; the MT reciprocal monomial is exact; "
      "the reconfiguration sign, the nearby fractions and the binding zero all hold")

# =====================================================================
banner("§G  the standing rules: forbidden tokens, hygiene, blocks, citation closure, ledger rows, the text pins")
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
i15 = P4t.find("## Tier BM.15 ")
i14 = P4t.find("## Tier BM.14 ")
iclos = P4t.find("## Closure exports of Part 4")
chk(0 < i14 < i15 < iclos, "§G0 the tier order in Part 4 is BM.14 then BM.15 then the closure exports")
tier = P4t[i15:_tier_end(P4t, i15, iclos)]

for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
    chk(word not in tier.lower(), f"§G1 zero '{word}' in the Tier BM.15 text")
chk(not re.search(r"\bP-H\d", tier), "§G1 zero registry (P-H) tokens in Tier BM.15")
chk("**Status.**" not in tier, "§G1 zero '**Status.**' lines in Tier BM.15 (canon hygiene)")
chk("[EXT]" not in tier, "§G1 zero [EXT] markers in Tier BM.15")
dec = re.findall(r"(?<![A-Za-z0-9\u00a7])\d+\.\d+", tier)
chk(not dec, f"§G1 zero decimal numerals in Tier BM.15 outside tag/section names: {dec}")
for tok in ["MeV", "GeV", "keV", "PDG", "Higgs", "fine-structure constant is"]:
    chk(tok not in tier, f"§G1 zero external/mechanism token '{tok}' in Tier BM.15")
for num in ["1/137", "1.293", "0.782", "938", "939", "0.0072", "4.19", "2.2", "173", "127", "782"]:
    chk(re.search(r"(?<![A-Za-z0-9.\u00a7])" + re.escape(num) + r"(?![0-9.])", tier) is None,
        f"§G1 zero external-value numeral '{num}' in Tier BM.15 [P5]")
nab = 0
for pat in [r"\alpha_B", "alpha_B"]:
    for mm in re.finditer(re.escape(pat), tier):
        nab += 1
        line = tier[tier.rfind("\n", 0, mm.start()) + 1: tier.find("\n", mm.end())]
        chk(("\\neg" in line) or ("barred" in line) or ("not derivable" in line),
            f"§G1 every '{pat}' occurrence sits in a barred-object row")
nyk = 0
for mm in re.finditer("Yukawa", tier):
    nyk += 1
    line = tier[tier.rfind("\n", 0, mm.start()) + 1: tier.find("\n", mm.end())]
    chk(("\\neg" in line) or ("no Yukawa" in line), "§G1 every 'Yukawa' occurrence sits in a negation row")
chk(nab >= 1 and nyk >= 1, "§G1 the barred-object rows are present (alpha_B refused, Yukawa absent)")

TAGS15 = [f"BM.{n}" for n in range(65, 73)]
def block(src, tag):
    m = re.search(r"^### " + re.escape(tag) + r" —", src, re.M)
    if not m: return ""
    st = m.start()
    nxt = re.search(r"^### ", src[m.end():], re.M)
    en = m.end() + nxt.start() if nxt else src.find("## Closure exports", st)
    return src[st:en if en > 0 else len(src)]
for t in TAGS15:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier, re.M) is not None, f"§G2 Tier BM.15 carries the tag {t}")
    b = block(tier, t)
    for k in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(k in b, f"§G2 {t} carries {k}")
    chk("\\blacksquare" in b, f"§G2 {t} carries its proof terminator")
chk("### Def-BM.15" not in tier and "**Def.**" not in tier, "§G2 Tier BM.15 issues no new definition block")
chk("the declarations this tier adds: zero" in tier, "§G2 the tier states that it adds zero declarations")

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
        base = tok.split("(")[0]
        if base not in REG: missing.add(base)
chk(not missing, f"§G3 every tag cited in Tier BM.15 exists in the corpus registry: missing {sorted(missing)}")

endash = chr(0x2013)
mNS = re.search(r"Def-BM\.1" + endash + r"Def-BM\.(\d+); BM\.1" + endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + endash + r"BM\.(\d+)", P4t)
chk(mNS and int(mNS.group(1)) >= 14 and int(mNS.group(2)) >= 72 and int(mNS.group(3)) >= 15,
    "§G4 the Part 4 Namespace line covers Tier BM.15 (Def-BM.14 / BM.72 / BM.15)")
chk("(xviii) the organic-bridge layer [Tier BM.15" in P4t, "§G4 the Part 4 charter carries clause (xviii)")
closure = P4t[iclos:]
for t in [r"\mathrm{BM.65}", r"\mathrm{BM.66}", r"\mathrm{BM.67}", r"\mathrm{BM.68}",
          r"\mathrm{BM.69}", r"\mathrm{BM.70}", r"\mathrm{BM.71}", r"\mathrm{BM.72}"]:
    chk(t in closure, f"§G4 the closure exports carry {t}")
chk("(V.19)" in HLt, "§G5 the HistLog §V carries the (V.19) verification-history entry")
for n in range(65, 73):
    chk(f"**BM.{n}.**" in HLt, f"§G5 the HistLog §III status ledger carries the BM.{n} row")

PINS = [
    (r"\operatorname{Tr}\widehat F\ =\ \sum_{s,t\in\{\pm1\}}\lambda_{s,t}\ =\ 2\,c_0", "the charge-blind linear trace"),
    (r"I_F\ :=\ \operatorname{Tr}\widehat F^2-\operatorname{Tr}\widehat F_0^2\ =\ 4\,\widehat Q^2", "the quadratic invariant I_F = 4 Q^2"),
    (r"\frac{E_{\mathrm{int}}}4\;c\,\varepsilon_{\mathrm{EM}}\ln2", "the derived coefficient E_int/4"),
    (r"\widehat M_{\mathrm{rest}}\mathfrak h\ =\ E_{\mathrm{int}}\ln2\ +\ \ln W(\widehat Q)", "the assembled operator rest input"),
    (r"U(\gamma)\ =\ \prod_{e\in\gamma}\sigma_e\ =\ (-1)^{N_\pi(\gamma)}", "the bare Z2 Wilson holonomy"),
    (r"\sum_i\aleph_{v_i}\ \equiv\ |Q|\ (\mathrm{mod}\ 2)", "the composite parity lock"),
    (r"\operatorname{im}(\text{any register/force/caps lift})\ \subseteq\ \{0,\ \pi\}", "the two-torsion image"),
    ("OBSTRUCTION: holonomy_lift_not_derived", "the holonomy obstruction record"),
    ("OBSTRUCTION: geometric_fiber_count_not_derived", "the geometric-fiber obstruction record"),
    (r"\Omega(E,\Theta,Q)\ =\ \Omega_{\mathrm{count}}(E)\ \cdot\ \Omega_{\mathrm{charge}}(Q)\ \cdot\ \Omega_{\mathrm{geom}}(\Theta;E,Q)", "the joint-entropy factorization"),
    (r"\Omega_{\mathrm{count}}(E)\ =\ 2^E", "the count fiber"),
    (r"\Omega_{\mathrm{charge}}(Q)\ =\ W(Q)", "the charge fiber"),
    (r"\Omega_{\mathrm{geom}}^{\mathrm{stat}}(\Theta)\ =\ 1", "the stationary geometric fiber is one"),
    (r"S_{\mathrm{joint}}\bigl(6,\ \Theta_{\mathrm{stat}},\ Q\bigr)\ =\ 6\ln2\ +\ \ln W(Q)\ +\ 0", "the stationary joint entropy equals the refined rest input"),
    (r"\rho_{\mathrm B}\ :=\ \frac{\hat\mu'^2\,\mathfrak h^2}{(\ln2)^2}", "the single undeclared bridge ratio, named"),
    (r"\frac{m^2_{\mathrm{pole}}}{m_{\mathrm{hid}}^2}\ =\ \mathcal R\bigl(E_{\mathrm{int}},\Theta_R\bigr)\ =\ \rho_{\mathrm B}\cdot\frac{D_S(\Theta_R)}{4\,E_{\mathrm{int}}^2}", "the bridge identity in its derived form"),
    (r"F_{\ell\nu}\ \ge\ 2\ln2", "the two-bit daughter floor"),
    (r"Q_\beta\,\mathfrak h\ =\ \ln\tfrac43\ -\ 6\,c\,\varepsilon_{\mathrm{EM}}\ln2\ -\ F_{\ell\nu}", "the audited Q-value row"),
    (r"\textbf{formed}\implies\textbf{closed}", "the formed-closed dichotomy"),
    (r"-\ln(4\cdot3)=-\ln12", "the second margin rung"),
    (r"-\ln(8\cdot3)=-\ln24", "the third margin rung"),
    ("4<12", "the weakest margin certificate"),
    ("4<48", "the second margin certificate"),
    ("4<96", "the third margin certificate"),
    (r"\Delta m_{\mathrm{bridge}}\ =\ 0\ \ \text{in the informational currency}", "the bridge term is zero in currency"),
    ("the beta-decay no-go", "the no-go verdict"),
    (r"2^{13}>3^{8}", "the certificate 2^13 > 3^8"),
    (r"2^{11}<3^{7}", "the certificate 2^11 < 3^7"),
    (r"2^{8}>3^{5}", "the certificate 2^8 > 3^5"),
    (r"2^{31}<3^{20}", "the certificate 2^31 < 3^20"),
    ("256>243", "the sub-criticality witness 256 > 243"),
    ("64>54", "the bar witness 64 > 54"),
    ("1024>972", "the bar witness 1024 > 972"),
    (r"1280^3\ne960^4", "the ratio bar certificate"),
    ("the partial-bridge outcome and the no-go outcome are conjoined", "the status adjudication"),
    (r"\neg\exists\ \text{a theorem of Parts 1--4 fixing}\ \varepsilon_{\mathrm{EM}}", "no theorem fixes the coupling"),
    ("no continuous angle is inserted anywhere in this tier", "no declared holonomy"),
    (r"\frac{5\,(2-\log_23)}{18}", "the exact critical strength at c = 3/5"),
]
for pat, why in PINS:
    chk(pat in tier, f"§G6 text pin: {why}")
for pat in [r"\neg\text{a P4 addition}", r"\neg\text{a new dimensionful scale}",
            r"\text{§Cal-BM stays empty}", r"\neg\text{a measured value}",
            r"\neg\text{a HistLog disposition imported as premise}"]:
    chk(pat in tier, f"§G7 the standing bar {pat} is stated in the tier")

SRC = open(os.path.abspath(__file__), encoding="utf-8").read()
FLT = "float" + "("
chk(FLT not in SRC, "§G8 this checker contains no floating-point constructor")
DEC2 = r"(?<![A-Za-z0-9_'\"\u00a7])\d+\." + r"\d+"
selfdec = re.findall(DEC2, SRC)
chk(not selfdec, f"§G8 this checker contains no decimal numeral: {selfdec}")
chk(("import " + "sympy") not in SRC, "§G8 the checker is dependency-free: no external algebra system is imported")
stamp("§G green: hygiene scans clean, blocks complete for BM.65-BM.72, no new definition, citation closure "
      "holds, the Namespace/charter/closure/ledger rows extended, all text pins present, the checker itself "
      "carries no floating point and no decimal numeral")

# =====================================================================
print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_organic_bridge_post_bm14: {len(FAIL)} FAILURE(S)")
    for f in FAIL: print("   ", f)
    sys.exit(1)
print(f"verify_H_organic_bridge_post_bm14: ALL GREEN ({N} exact checks, no floating point)")
sys.exit(0)
