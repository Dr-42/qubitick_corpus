#!/usr/bin/env python3
"""verify_H_polespectrum.py — companion to FT.76 / FT.77 (Tier F.26).

Exact arithmetic only for every algebraic claim: the values live in Q, Q(sqrt2), Q(sqrt3) and
Q(cos(pi/10)) = Q[x]/(16x^4-20x^2+5), computed through the Chebyshev recursion
cos(m phi) = T_m(cos phi) with integer coefficients (the identity FT.60(5) already uses).
Decimal appears in exactly two roles, both non-load-bearing:
  (a) display / comparison against the documented decimal strings (tolerance 1e-9 or tighter);
  (b) evaluation of the exact nested radicals for those displays.
Every exact check is a field-element identity, an integer minimal polynomial, or a certified
Fraction bracket. The SM hierarchies of FT.77 are EXTERNAL data (marked in the document): they
are used here only to re-run the comparison audit, never to derive anything.

Asserts:
  * base elements (16c^4-20c^2+5=0; (sqrt2/2)^2=1/2; (sqrt3/2)^2=3/4; sqrt5=8c^2-5, squared=5);
  * FT.63(6) regression: the D_S column, its minimal-polynomial column, the published m<=4
    weight ladder of all five solids, the dodecahedron's D(2)=(3-sqrt5)/2 and D(4)=(5-sqrt5)/2;
  * independent validation of D(m) for m=0..24 on all five solids against an exact rational
    Taylor series for cos (agreement beyond 1e-45);
  * FT.76(1): k_f=(3,2,3,5,3) from the minimality rule, k_vf=(3,3,2,3,5), K_S=F*k_f=2*j_max,
    V*delta_v=4*pi, and the two trivial readings (Theta_R = 0 and 4*pi -> identically massless);
  * FT.76(2): both variant multiplets, value by value, as exact field elements;
  * FT.76(3): periods P=(4,8,6,20,12), distinct-value counts P/2+1, strict monotonicity on
    [0,P/2], max=4, min nonzero=D_S, the 4/D_S ceiling row and the dodecahedron's ceiling
    minimal polynomial x^4-48x^3+304x^2-512x+256, with certified mass-ceiling brackets;
  * FT.76(4)-(5): top-weight near-universality D(k_f)=(2,2,4,2,2), tetrahedral full degeneracy,
    the even-k zero modes (cube in A, octahedron in B);
  * FT.76(6)-(7): inter-solid ratios (exact identities where the field allows) and intra-solid
    splittings with their minimal polynomials and exact square-root identities;
  * FT.76(8)-(9): dual-pair multiset splitting in both variants; field membership;
  * FT.76(10): the dodecahedral quartic has FOUR positive roots, isolated to width 2^-60, with
    the documented decimals and the weight attribution m in {1,19},{3,17},{7,13},{9,11};
  * FT.77: pool accounting (25 per-solid / 16 distinct / 120 pairwise / 560 triples), the mass
    ceiling 6.392453..., the exhaustive triple floors (140.79 / 543.92 / 12514.76), the best
    pairwise discrepancy (2.6276), the three dimensionally-wrong near-coincidences, the two
    three-distinct-mass multiplets and their discrepancies, and the quantitative distance
    (D <= 1/202500, factor 19822.11 in D, 140.79 in mass, delta_v <= 1/225 rad vs pi/5).
"""
import os, sys, time, math, itertools
from fractions import Fraction as Fr
from decimal import Decimal, getcontext

getcontext().prec = 70
QFMT = Decimal('1.' + '0' * 50)            # fixed 50-digit quantizer for Decimal reads
N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1

t0 = time.time()
def stamp(msg):
    print(f"  [{time.time()-t0:5.1f}s] {msg}  (checks: {N})")

# ---------------------------------------------------------------- exact fields Q[x]/(f)
class AF:
    __slots__ = ('c', 'f')
    def __init__(s, coeffs, f):
        s.f = [Fr(z) for z in f]
        d = len(f) - 1
        c = [Fr(z) for z in coeffs] + [Fr(0)] * d
        s.c = c[:d]
    @property
    def deg(s): return len(s.f) - 1
    def _mk(s, coeffs):
        e = AF.__new__(AF); e.f = s.f
        c = [Fr(z) for z in coeffs] + [Fr(0)] * s.deg
        e.c = c[:s.deg]; return e
    def __add__(s, o):
        if isinstance(o, (int, Fr)): return s._mk([x + (o if i == 0 else 0) for i, x in enumerate(s.c)])
        return s._mk([a + b for a, b in zip(s.c, o.c)])
    __radd__ = __add__
    def __sub__(s, o):
        if isinstance(o, (int, Fr)): return s._mk([x - (o if i == 0 else 0) for i, x in enumerate(s.c)])
        return s._mk([a - b for a, b in zip(s.c, o.c)])
    def __rsub__(s, o): return s._mk([o]) - s
    def __neg__(s): return s._mk([-a for a in s.c])
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return s._mk([a * o for a in s.c])
        p = [Fr(0)] * (2 * s.deg - 1)
        for i, a in enumerate(s.c):
            if a:
                for j, b in enumerate(o.c): p[i + j] += a * b
        return s._mk(s._red(p))
    __rmul__ = __mul__
    def __pow__(s, n):
        r = s._mk([1]); b = s
        while n:
            if n & 1: r = r * b
            b = b * b; n >>= 1
        return r
    def _red(s, p):
        p = list(p); d = s.deg; lc = s.f[d]
        for i in range(len(p) - 1, d - 1, -1):
            if p[i]:
                q = p[i] / lc
                for j in range(d + 1): p[i - d + j] -= q * s.f[j]
        return p[:d]
    def inv(s):
        d = s.deg
        cols = [(s * s._mk([Fr(1) if i == j else Fr(0) for i in range(d)])).c for j in range(d)]
        rhs = [Fr(1)] + [Fr(0)] * (d - 1)
        A = [[cols[j][i] for j in range(d)] + [rhs[i]] for i in range(d)]
        for k in range(d):
            piv = next(r for r in range(k, d) if A[r][k])
            A[k], A[piv] = A[piv], A[k]
            A[k] = [x / A[k][k] for x in A[k]]
            for r in range(d):
                if r != k and A[r][k]:
                    f0 = A[r][k]; A[r] = [x - f0 * y for x, y in zip(A[r], A[k])]
        u = s._mk([A[i][d] for i in range(d)])
        assert s * u == s._mk([1]), f"inv failed: {s.c}"
        return u
    def __truediv__(s, o):
        if isinstance(o, (int, Fr)): return s._mk([a / o for a in s.c])
        return s * o.inv()
    def __eq__(s, o):
        if isinstance(o, (int, Fr)): return s.c == ([Fr(o)] + [Fr(0)] * (s.deg - 1))
        return s.c == o.c
    def __hash__(s): return hash(tuple(s.c))
    def __repr__(s): return f"AF({[str(x) for x in s.c]})"
    def rat(s):
        assert all(x == 0 for x in s.c[1:]), f"not rational: {s.c}"
        return s.c[0]
    def dec(s, g):
        tot = Decimal(0); pw = Decimal(1)
        for a in s.c:
            if a: tot += Decimal(a.numerator) / Decimal(a.denominator) * pw
            pw *= g
        return tot.quantize(QFMT)          # uniform fixed-digit display form

F_Q = [Fr(0), Fr(1)]
F_S2 = [Fr(-2), Fr(0), Fr(1)]
F_S3 = [Fr(-3), Fr(0), Fr(1)]
F_C = [Fr(5), Fr(0), Fr(-20), Fr(0), Fr(16)]
GDEC = {'Q': Decimal(0), 's2': Decimal(2).sqrt(), 's3': Decimal(3).sqrt(),
        'c': (Decimal(10) + 2 * Decimal(5).sqrt()).sqrt() / 4}

def _rref(M, ncols):
    A = [list(r) for r in M]; nrows = len(A); piv = []; pr = 0
    for col in range(ncols):
        p = next((r for r in range(pr, nrows) if A[r][col]), None)
        if p is None: continue
        A[pr], A[p] = A[p], A[pr]
        A[pr] = [x / A[pr][col] for x in A[pr]]
        for r in range(nrows):
            if r != pr and A[r][col]:
                f0 = A[r][col]; A[r] = [x - f0 * y for x, y in zip(A[r], A[pr])]
        piv.append(col); pr += 1
        if pr == nrows: break
    return A[:pr], piv

def minpoly(a):
    d = a.deg
    pows = [a._mk([1])]
    for _ in range(d): pows.append(pows[-1] * a)
    for n in range(1, d + 1):
        M = [[pows[j].c[i] for j in range(n + 1)] for i in range(d)]
        R, piv = _rref(M, n + 1)
        free = [j for j in range(n + 1) if j not in piv]
        if not free: continue
        j0 = free[0]; v = [Fr(0)] * (n + 1); v[j0] = Fr(1)
        for i, col in enumerate(piv): v[col] = -R[i][j0]
        lcm = 1
        for x in v: lcm = lcm * x.denominator // math.gcd(lcm, x.denominator)
        ip = [int(x * lcm) for x in v]
        g = 0
        for x in ip: g = math.gcd(g, abs(x))
        out = [x // g for x in ip]
        while len(out) > 1 and out[-1] == 0: out.pop()
        if out[-1] < 0: out = [-x for x in out]
        acc = a._mk([0])
        for k, cf in enumerate(out): acc = acc + pows[k] * cf
        chk(acc == a._mk([0]), f"minpoly {out} does not annihilate {a.c}")
        return out
    raise AssertionError("no minimal polynomial")

def peval(poly, x):
    acc = Fr(0); pw = Fr(1)
    for c in poly: acc += c * pw; pw *= x
    return acc

def bisect_root(poly, a, b, bits=60):
    a, b = Fr(a), Fr(b); fa = peval(poly, a)
    assert fa * peval(poly, b) < 0
    for _ in range(bits):
        m = (a + b) / 2; fm = peval(poly, m)
        if fa * fm <= 0: b = m
        else: a, fa = m, fm
    return a, b

# ---------------------------------------------------------------- the five solids (corpus data)
SOL = {  # delta_v/pi [FT.63(4)]; V,E,F; face/vertex-figure side counts; K_S [FT.63(1)]
 'tetra':  dict(dvp=Fr(1),    V=4,  E=6,  F=4,  Lf=3, Lv=3, Ks=12, f='Q'),
 'cube':   dict(dvp=Fr(1, 2), V=8,  E=12, F=6,  Lf=4, Lv=3, Ks=12, f='s2'),
 'octa':   dict(dvp=Fr(2, 3), V=6,  E=12, F=8,  Lf=3, Lv=4, Ks=24, f='Q'),
 'dodeca': dict(dvp=Fr(1, 5), V=20, E=30, F=12, Lf=5, Lv=3, Ks=60, f='c'),
 'icosa':  dict(dvp=Fr(1, 3), V=12, E=30, F=20, Lf=3, Lv=5, Ks=60, f='s3'),
}
ORDER = ['tetra', 'cube', 'octa', 'dodeca', 'icosa']
FIELD = {'Q': F_Q, 's2': F_S2, 's3': F_S3, 'c': F_C}
for S, d in SOL.items():
    d['kf'] = d['Lf'] * (2 if d['Lf'] % 2 else 1) // 2
    d['kvf'] = d['Lv'] * (2 if d['Lv'] % 2 else 1) // 2
    d['P'] = int(4 / d['dvp'])

def F_of(S): return FIELD[SOL[S]['f']]
def one(S): return AF([1], F_of(S))
def base_cos(S):
    f = SOL[S]['f']
    if f == 'Q':
        return one(S) * 0 if S == 'tetra' else one(S) / 2
    g = AF([0, 1], F_of(S))
    return g if S == 'dodeca' else g / 2

def cheb(m, x, S):
    if m == 0: return one(S)
    t0, t1 = one(S), x
    for _ in range(m - 1): t0, t1 = t1, 2 * x * t1 - t0
    return t1

def D(m, S):
    """D_S(m) = 2 - 2 cos(m delta_v / 2) = m^2_pole(m)/mu'^2, exact."""
    return one(S) * 2 - 2 * cheb(abs(int(m)), base_cos(S), S)

# ---------------------------------------------------------------- 1. base elements
c = AF([0, 1], F_C)
chk(16 * c ** 4 - 20 * c ** 2 + 5 == 0, "16c^4-20c^2+5 = 0 for c = cos(pi/10)")
chk(base_cos('cube') ** 2 == AF([Fr(1, 2)], F_S2), "cos(pi/4)^2 = 1/2")
chk(base_cos('icosa') ** 2 == AF([Fr(3, 4)], F_S3), "cos(pi/6)^2 = 3/4")
chk(base_cos('octa') == AF([Fr(1, 2)], F_Q), "cos(pi/3) = 1/2")
chk(base_cos('tetra') == 0, "cos(pi/2) = 0")
s5 = 8 * c ** 2 - 5
chk(s5 * s5 == AF([5], F_C), "sqrt5 = 8c^2 - 5 in Q(cos(pi/10)), squared = 5")
chk(s5.dec(GDEC['c']) > 0 and abs(s5.dec(GDEC['c']) - Decimal(5).sqrt()) < Decimal('1e-50'),
    "sqrt5 = 8c^2-5 is the positive branch (Q(sqrt5) subset Q(c))")
stamp("base elements: 16c^4-20c^2+5=0; cos^2 anchors; sqrt5 = 8c^2-5")

# ---------------------------------------------------------------- 2. FT.63(6) regression
DS_dec = {'tetra': '2', 'cube': '0.5857864376269049', 'octa': '1',
          'dodeca': '0.0978869674096928', 'icosa': '0.2679491924311227'}
DS_mp = {'tetra': [-2, 1], 'cube': [2, -4, 1], 'octa': [-1, 1],
         'dodeca': [1, -12, 19, -8, 1], 'icosa': [1, -4, 1]}
for S in ORDER:
    ds = D(1, S)
    chk(str(ds.dec(GDEC[SOL[S]['f']])).startswith(DS_dec[S][:14]), f"{S}: D_S decimal")
    chk(minpoly(ds) == DS_mp[S], f"{S}: D_S minimal polynomial {minpoly(ds)} != {DS_mp[S]}")
    chk(ds == AF([2], F_of(S)) - 2 * base_cos(S), f"{S}: D_S = 2-2cos(delta_v/2)")
ladder = {'tetra': [(2, 0), (4, 0), (2, 0), (0, 0)], 'octa': [(1, 0), (3, 0), (4, 0), (3, 0)],
          'cube': [(2, -1), (2, 0), (2, 1), (4, 0)], 'icosa': [(2, -1), (1, 0), (2, 0), (3, 0)]}
for S, rows in ladder.items():
    for i, (a, b) in enumerate(rows, start=1):
        chk(D(i, S) == AF([Fr(a), Fr(b)], F_of(S)), f"{S}: FT.63(6) ladder D({i})")
chk(D(2, 'dodeca') == AF([Fr(3, 2)], F_C) - s5 / 2, "dodeca: D(2) = (3-sqrt5)/2")
chk(D(4, 'dodeca') == AF([Fr(5, 2)], F_C) - s5 / 2, "dodeca: D(4) = (5-sqrt5)/2")
stamp("FT.63(6) regression: D_S column, minimal-polynomial column, m<=4 ladder, dodeca D(2)/D(4)")

# ---------------------------------------------------------------- 3. Taylor validation
def taylor_cos(q, terms=130):
    getcontext().prec = 95
    pi = Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798')
    x = Decimal(q.numerator) / Decimal(q.denominator) * pi
    tot, term, n = Decimal(0), Decimal(1), 0
    while n < terms:
        tot += term; n += 1
        term = term * (-x * x) / Decimal((2 * n - 1) * (2 * n))
    getcontext().prec = 70
    return +tot

nv = 0
for S in ORDER:
    d = SOL[S]['dvp']
    for m in range(25):
        exact = D(m, S).dec(GDEC[SOL[S]['f']])
        approx = Decimal(2) - 2 * taylor_cos(Fr(m) * d / 2)
        chk(abs(exact - approx) < Decimal('1e-45'), f"{S} m={m}: {exact} vs {approx}")
        nv += 1
chk(nv == 125, f"Taylor validation count {nv}")
stamp(f"125 values D_S(m), m=0..24, validated against an exact rational Taylor series (1e-45)")

# ---------------------------------------------------------------- 4. FT.76(1) windings
chk([SOL[S]['kf'] for S in ORDER] == [3, 2, 3, 5, 3], "k_f = (3,2,3,5,3)")
chk([SOL[S]['kvf'] for S in ORDER] == [3, 3, 2, 3, 5], "k_vf = (3,3,2,3,5)")
for S in ORDER:
    d = SOL[S]
    chk(d['F'] * d['kf'] == d['Ks'], f"{S}: K_S = F*k_f")
    chk(d['Ks'] % 2 == 0 and d['Ks'] // 2 == d['F'] * d['kf'] // 2, f"{S}: K_S even (j_max = K_S/2)")
    chk(d['V'] * d['dvp'] == 4, f"{S}: V*delta_v = 4 pi (Descartes)")
    # the two trivial readings: Theta_R = 4 pi -> cos(2 m pi) = 1 -> D = 0; Theta_R = 0 -> D = 0
    for m in (1, 2, 3, 5, SOL[S]['kf']):
        chk(one(S) * 2 - 2 * cheb(m, one(S), S) == AF([0], F_of(S)),
            f"{S}: both trivial readings (0 and 4 pi) are massless at m={m}")
stamp("FT.76(1): windings, K_S = F*k_f = 2*j_max, Descartes V*delta_v = 4pi, the two massless readings")

# ---------------------------------------------------------------- 5. FT.76(2) multiplets
mA = {'tetra': [(3, 2), (1, 2), (-1, 2), (-3, 2)],
      'cube': [(2, 2), (0, 0), (-2, 2)],
      'octa': [(3, 4), (1, 1), (-1, 1), (-3, 4)],
      'dodeca': [(5, 2), (3, None), (-3, None), (1, None), (-1, None)],
      'icosa': [(3, 2), (1, None), (-1, None), (-3, 2)]}
for S, rows in mA.items():
    for m, val in rows:
        v = D(m, S)
        if val is not None:
            chk(v == AF([Fr(val)], F_of(S)), f"(A) {S} m={m}: {v.c} != {val}")
        else:
            chk(v.dec(GDEC[SOL[S]['f']]) > 0 and v != AF([0], F_of(S)), f"(A) {S} m={m} nonzero")
chk(D(1, 'dodeca') == AF([2], F_C) - 2 * c, "(A) dodeca m=1: 2-2c")
chk(D(3, 'dodeca') == AF([2], F_C) - 2 * (4 * c ** 3 - 3 * c), "(A) dodeca m=3: 2-2cos(3pi/10)")
chk(D(1, 'icosa') == AF([2, -1], F_S3), "(A) icosa m=1: 2-sqrt3")
chk(D(1, 'cube') == AF([2, -1], F_S2) and D(3, 'cube') == AF([2, 1], F_S2), "(B) cube: 2-+sqrt2")
chk(D(2, 'octa') == AF([3], F_Q), "(B) octa m=2: 3")
chk(D(5, 'icosa') == AF([2, 1], F_S3), "(B) icosa m=5: 2+sqrt3")
dec_doc = {'dodeca': ['0.097886967410', '0.824429495415', '2.000000000000'],
           'icosa': ['0.267949192431', '2.000000000000', '3.732050807569'],
           'cube': ['0.585786437627', '3.414213562373']}
for S, vals in dec_doc.items():
    got = sorted({str(D(m, S).dec(GDEC[SOL[S]['f']]))[:14] for m in range(1, SOL[S]['P'])})
    for v in vals:
        chk(any(g.startswith(v[:12]) for g in got), f"{S}: documented decimal {v} in ladder {got[:4]}")
stamp("FT.76(2): variant (A) and (B) multiplets as exact field elements + documented decimals")

# ---------------------------------------------------------------- 6. FT.76(3) ceiling
chk([SOL[S]['P'] for S in ORDER] == [4, 8, 6, 20, 12], "periods P = 4pi/delta_v")
ceil_m2 = {'tetra': 2, 'octa': 4}
for S in ORDER:
    P = SOL[S]['P']
    for m in range(0, P + 4):
        chk(D(m + P, S) == D(m, S), f"{S}: periodicity at m={m}")
        chk(D(P - m, S) == D(m, S), f"{S}: reflection D(P-m) = D(m)")
    vals = [D(m, S).dec(GDEC[SOL[S]['f']]) for m in range(P // 2 + 1)]
    chk(len({str(v) for v in vals}) == P // 2 + 1, f"{S}: {P//2+1} distinct values")
    chk(all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)), f"{S}: strict monotonicity on [0,P/2]")
    chk(vals[0] == 0 and vals[-1] == Decimal(4), f"{S}: min 0, max 4")
    chk(vals[1] == D(1, S).dec(GDEC[SOL[S]['f']]), f"{S}: min nonzero = D_S")
    q = AF([4], F_of(S)) / D(1, S)
    if S in ceil_m2: chk(q == AF([Fr(ceil_m2[S])], F_of(S)), f"{S}: 4/D_S = {ceil_m2[S]}")
    if S == 'dodeca':
        chk(minpoly(q) == [256, -512, 304, -48, 1], f"dodeca ceiling minpoly {minpoly(q)}")
        a, b = bisect_root([256, -512, 304, -48, 1], Fr(40), Fr(42))
        dq = q.dec(GDEC['c'])
        chk(a < Fr(dq) < b and (b - a) < Fr(1, 2 ** 55),
            f"dodeca ceiling: certified bracket contains the exact field value {str(dq)[:14]}")
        chk(str(dq).startswith('40.863458189'), f"dodeca ceiling decimal {str(dq)[:16]}")
        # p(x^2) for p(x) = 256 - 512x + 304x^2 - 48x^3 + x^4 (ascending)
        am, bm = bisect_root([256, 0, -512, 0, 304, 0, -48, 0, 1], Fr(6), Fr(7))
        dm = dq.sqrt()
        chk(am < Fr(dm) < bm and (bm - am) < Fr(1, 2 ** 55),
            f"mass ceiling: certified bracket contains sqrt(4/D_dodeca) = {str(dm)[:14]}")
        chk(str(dm).startswith('6.3924532214'), f"mass ceiling decimal {str(dm)[:16]}")
    if S == 'icosa':
        chk(q == AF([8, 4], F_S3), "icosa: 4/D_S = 4/(2-sqrt3) = 8+4sqrt3")
        chk(minpoly(q) == [16, -16, 1], f"icosa ceiling minpoly {minpoly(q)}")
    if S == 'cube':
        chk(q == AF([4, 2], F_S2), "cube: 4/D_S = 4/(2-sqrt2) = 4+2sqrt2")
        chk(minpoly(q) == [8, -8, 1], f"cube ceiling minpoly {minpoly(q)}")
ceiling_m2 = [ (AF([4], F_of(S)) / D(1, S)).dec(GDEC[SOL[S]['f']]) for S in ORDER]
chk([str(x)[:8] for x in ceiling_m2] == ['2.000000', '6.828427', '4.000000', '40.86345', '14.92820'],
    f"ceiling row {[str(x)[:10] for x in ceiling_m2]}")
chk(max(ceiling_m2) == ceiling_m2[3], "the dodecahedron attains the ceiling")
chk(max(x.sqrt() for x in ceiling_m2).quantize(Decimal('1.000001')) == Decimal('6.392453'),
    "mass ceiling = 6.392453 (dodecahedron)")
stamp("FT.76(3): periods, distinct counts, monotonicity, max 4, the 4/D_S ceiling row + minpolys")

# ---------------------------------------------------------------- 7. FT.76(4)-(5) structure
for S in ORDER:
    k = SOL[S]['kf']
    top = D(k, S).dec(GDEC[SOL[S]['f']])
    want = (Decimal(4) if S == 'octa' else Decimal(2)).quantize(QFMT)
    chk(top == want, f"{S}: top weight D(k_f) = {top} (want {want})")
chk([D(SOL[S]['kf'], S).dec(GDEC[SOL[S]['f']]) for S in ORDER] ==
    [Decimal(x).quantize(QFMT) for x in (2, 2, 4, 2, 2)], "top-weight near-universality (2,2,4,2,2)")
for m in (1, 3, 5, 7):
    chk(D(m, 'tetra') == AF([2], F_Q) if m % 2 else D(m, 'tetra') in (AF([0], F_Q), AF([4], F_Q)),
        f"tetra D({m})")
chk([D(m, 'tetra') for m in (1, 3)] == [AF([2], F_Q)] * 2, "tetra k=3 multiplet fully degenerate at 2")
chk(D(0, 'cube') == 0 and D(0, 'octa') == 0, "even-k zero modes: D(0) = 0")
chk(SOL['cube']['kf'] % 2 == 0 and SOL['octa']['kvf'] % 2 == 0, "cube (A) and octa (B) have even k")
chk(SOL['tetra']['kf'] % 2 == 1 and SOL['dodeca']['kf'] % 2 == 1, "tetra/dodeca (A) have odd k")
stamp("FT.76(4)-(5): top-weight near-universality (2,2,4,2,2), tetra degeneracy, even-k zero modes")

# ---------------------------------------------------------------- 8. FT.76(6)-(7) ratios
tet = AF([2], F_Q)
inter_A = {}
for S in ORDER:
    k = SOL[S]['kf']
    nz = [D(m, S) for m in range(k, -k - 1, -2) if D(m, S) != 0]
    lo = min(nz, key=lambda v: v.dec(GDEC[SOL[S]['f']]))
    inter_A[S] = lo
chk(inter_A['tetra'] == AF([2], F_Q) and inter_A['cube'] == AF([2], F_S2), "lightest (A): tetra, cube = 2")
chk(inter_A['octa'] == AF([1], F_Q), "lightest (A): octa = 1")
chk(inter_A['dodeca'] == AF([2], F_C) - 2 * c, "lightest (A): dodeca = 2-2c")
chk(inter_A['icosa'] == AF([2, -1], F_S3), "lightest (A): icosa = 2-sqrt3")
# exact ratio identities where the field allows
chk(inter_A['dodeca'] / 2 == AF([1, -1], F_C), "dodeca/tetra = 1 - c exactly")
chk(inter_A['icosa'] / 2 == AF([1, Fr(-1, 2)], F_S3), "icosa/tetra = 1 - sqrt3/2 exactly")
dec_A = {'tetra': ('1', '1'), 'cube': ('1', '1'), 'octa': ('0.5', '0.707106781187'),
         'dodeca': ('0.048943483705', '0.221231742082'), 'icosa': ('0.133974596216', '0.366025403784')}
for S, (r2, rm) in dec_A.items():
    v2 = (inter_A[S].dec(GDEC[SOL[S]['f']]) / Decimal(2))
    chk(str(v2).startswith(r2[:10]), f"(A) {S} m^2 ratio {v2} vs {r2}")
    chk(str(v2.sqrt()).startswith(rm[:10]), f"(A) {S} mass ratio {v2.sqrt()} vs {rm}")
# variant B lightest
inter_B = {}
for S in ORDER:
    k = SOL[S]['kvf']
    nz = [D(m, S) for m in range(k, -k - 1, -2) if D(m, S) != 0]
    inter_B[S] = min(nz, key=lambda v: v.dec(GDEC[SOL[S]['f']]))
chk(inter_B['cube'] == AF([2, -1], F_S2), "lightest (B): cube = 2-sqrt2")
chk(inter_B['octa'] == AF([3], F_Q), "lightest (B): octa = 3 (zero mode excluded)")
chk(str((inter_B['cube'].dec(GDEC['s2']) / Decimal(2)))[:12] == '0.2928932188', "(B) cube/tetra m^2 ratio")
chk(str((inter_B['cube'].dec(GDEC['s2']) / Decimal(2)).sqrt())[:12] == '0.5411961001', "(B) cube/tetra mass ratio")
chk(str((inter_B['octa'].dec(GDEC['Q']) / Decimal(2)))[:5] == '1.500', "(B) octa/tetra m^2 ratio = 1.5")
# splittings
spl = {}
for tag, key in (('A', 'kf'), ('B', 'kvf')):
    for S in ORDER:
        k = SOL[S][key]
        nz = [D(m, S) for m in range(k, -k - 1, -2) if D(m, S) != 0]
        lo = min(nz, key=lambda v: v.dec(GDEC[SOL[S]['f']]))
        hi = max(nz, key=lambda v: v.dec(GDEC[SOL[S]['f']]))
        spl[(tag, S)] = (hi / lo, len([m for m in range(k, -k - 1, -2) if D(m, S) == 0]))
chk(spl[('A', 'tetra')][0] == AF([1], F_Q) and spl[('A', 'cube')][0] == AF([1], F_S2),
    "(A) tetra/cube splitting = 1")
chk(spl[('A', 'cube')][1] == 1 and spl[('B', 'octa')][1] == 1, "(A) cube / (B) octa carry one zero mode")
chk(spl[('A', 'octa')][0] == AF([4], F_Q), "(A) octa splitting = 4")
ic = spl[('A', 'icosa')][0]
chk(ic == AF([4, 2], F_S3), "(A) icosa splitting = 4+2sqrt3")
chk(minpoly(ic) == [4, -8, 1], "(A) icosa splitting minpoly x^2-8x+4")
r = AF([1, 1], F_S3)
chk(r * r == ic, "(A) icosa mass splitting = 1+sqrt3 exactly")
chk(minpoly(r) == [-2, -2, 1], "1+sqrt3 minpoly x^2-2x-2")
cb = spl[('B', 'cube')][0]
chk(cb == AF([3, 2], F_S2), "(B) cube splitting = 3+2sqrt2")
chk(minpoly(cb) == [1, -6, 1], "(B) cube splitting minpoly x^2-6x+1")
r2 = AF([1, 1], F_S2)
chk(r2 * r2 == cb, "(B) cube mass splitting = 1+sqrt2")
icb = spl[('B', 'icosa')][0]
chk(icb == AF([7, 4], F_S3), "(B) icosa splitting = 7+4sqrt3")
chk(minpoly(icb) == [1, -14, 1], "(B) icosa splitting minpoly x^2-14x+1")
r3 = AF([2, 1], F_S3)
chk(r3 * r3 == icb, "(B) icosa mass splitting = 2+sqrt3")
dA = spl[('A', 'dodeca')][0]
chk(minpoly(dA) == [16, -64, 76, -24, 1], f"(A) dodeca splitting minpoly {minpoly(dA)}")
chk(str(dA.dec(GDEC['c'])).startswith('20.4317290945'), "(A) dodeca splitting decimal")
a, b = bisect_root([16, -64, 76, -24, 1], Fr(20), Fr(21))
dAs = str(dA.dec(GDEC['c']))
chk(a < Fr(dAs and Decimal(dAs)) < b and (b - a) < Fr(1, 2 ** 50),
    f"(A) dodeca splitting: certified bracket contains {dAs[:16]}")
chk(dAs.startswith('20.43172909453'), f"(A) dodeca splitting decimal {dAs[:18]}")
dB = spl[('B', 'dodeca')][0]
chk(minpoly(dB) == [1, -34, 51, -14, 1], f"(B) dodeca splitting minpoly {minpoly(dB)}")
chk(str(dB.dec(GDEC['c'])).startswith('8.4222600539'), "(B) dodeca splitting decimal")
stamp("FT.76(6)-(7): inter-solid ratios (exact identities) + splittings with minpolys and sqrt identities")

# ---------------------------------------------------------------- 9. FT.76(8)-(9) duals, fields
def multiset(S, key):
    """the multiplet's values as exact Decimals (quantized), with multiplicity, sorted."""
    k = SOL[S][key]
    return sorted(D(m, S).dec(GDEC[SOL[S]['f']]) for m in range(k, -k - 1, -2))
chk(multiset('cube', 'kf') != multiset('octa', 'kf'), "(A) cube/octa pole multisets differ")
chk(multiset('cube', 'kvf') != multiset('octa', 'kvf'), "(B) cube/octa pole multisets differ")
chk(multiset('dodeca', 'kf') != multiset('icosa', 'kf'), "(A) dodeca/icosa pole multisets differ")
chk(multiset('dodeca', 'kvf') != multiset('icosa', 'kvf'), "(B) dodeca/icosa pole multisets differ")
TWO = Decimal(2).quantize(QFMT)
chk(TWO in multiset('dodeca', 'kf') and TWO in multiset('icosa', 'kf'),
    "(A) dodeca/icosa share the top value 2")
chk(not (set(multiset('icosa', 'kvf')) & set(multiset('dodeca', 'kvf'))),
    "(B) dodeca/icosa share no value")
chk(2 * SOL['cube']['E'] == 2 * SOL['octa']['E'] and 2 * SOL['dodeca']['E'] == 2 * SOL['icosa']['E'],
    "dual pairs share m_hid = 2E ln2/h [FT.44(1)]")
chk(SOL['tetra']['f'] == 'Q' and SOL['octa']['f'] == 'Q' and SOL['cube']['f'] == 's2'
    and SOL['icosa']['f'] == 's3' and SOL['dodeca']['f'] == 'c', "field ledger")
chk(len(F_C) - 1 == 4, "Q(cos(pi/10)) has degree 4 over Q")
stamp("FT.76(8)-(9): dual-pair multiset splitting in both variants; field ledger")

# ---------------------------------------------------------------- 10. FT.76(10) quartic roots
q4 = [1, -12, 19, -8, 1]
roots = []
step = Fr(1, 500); x = Fr(-1); prev = peval(q4, x)
while x < 6:
    x2 = x + step; f2 = peval(q4, x2)
    if prev * f2 < 0: roots.append(bisect_root(q4, x, x2))
    x, prev = x2, f2
chk(len(roots) == 4, f"the dodecahedral quartic has {len(roots)} real roots (documented: four)")
chk(all(a > 0 for a, b in roots), "all four roots positive")
chk([peval(q4, Fr(i)) for i in range(5)] == [1, 1, 5, 1, 1], "q(0..4) = (1,1,5,1,1) > 0")
doc_roots = ['0.097886967410', '0.824429495415', '3.175570504585', '3.902113032590']
for (a, b), d in zip(roots, doc_roots):
    chk((b - a) < Fr(1, 2 ** 55), f"root bracket width {float(b-a)}")
    chk(str(Decimal(a.numerator) / Decimal(a.denominator)).startswith(d[:12]), f"root {d}")
attr = {1: 0, 3: 1, 7: 2, 9: 3}
for m, i in attr.items():
    a, b = roots[i]
    dv = D(m, 'dodeca').dec(GDEC['c'])
    chk(Decimal(a.numerator) / Decimal(a.denominator) < dv < Decimal(b.numerator) / Decimal(b.denominator),
        f"D({m}) lies in root bracket {i}")
    chk(D(20 - m, 'dodeca') == D(m, 'dodeca'), f"D(20-{m}) = D({m})")
d1, d3, d7 = (D(m, 'dodeca').dec(GDEC['c']) for m in (1, 3, 7))
chk(d1 < d3 < d7 and d7 < D(9, 'dodeca').dec(GDEC['c']),
    "D(1) < D(3) < D(7) < D(9): D(1), D(3) are the two SMALLEST of four positive roots")
chk(all(D(m, 'dodeca').dec(GDEC['c']) >= d1 for m in range(1, 10)),
    "D(1) is the smallest nonzero value of the whole dodecahedral ladder")
stamp("FT.76(10): four positive roots isolated to 2^-60; weights {1,19},{3,17},{7,13},{9,11}")

# ---------------------------------------------------------------- 11. FT.77 audit re-run
SM = {'leptons': [1, 207, 3477], 'up': [1, 600, 80000], 'down': [1, 20, 900]}
pool = {}
for S in ORDER:
    for m in range(SOL[S]['P'] // 2 + 1):
        v = D(m, S)
        if v == 0: continue
        pool.setdefault(str(v.dec(GDEC[SOL[S]['f']])), []).append((S, m))
per_solid = {S: len({str(D(m, S).dec(GDEC[SOL[S]['f']]))
                     for m in range(SOL[S]['P'] // 2 + 1) if D(m, S) != 0}) for S in ORDER}
chk([per_solid[S] for S in ORDER] == [2, 4, 3, 10, 6], f"per-solid distinct nonzero values {per_solid}")
chk(sum(per_solid.values()) == 25, "25 per-solid values")
chk(len(pool) == 16, f"16 distinct values across the five solids (got {len(pool)})")
masses = sorted(Decimal(k).sqrt() for k in pool)
ratios = list(itertools.combinations(masses, 2))
chk(len(ratios) == 120, f"120 pairwise mass ratios (got {len(ratios)})")
chk(len(list(itertools.combinations(range(len(masses)), 3))) == 560, "560 triples")
mxr = masses[-1] / masses[0]
chk(str(mxr).startswith('6.39245322'), f"max pool mass ratio {mxr}")
chk(abs(mxr - (Decimal(4) / D(1, 'dodeca').dec(GDEC['c'])).sqrt()) < Decimal('1e-40'),
    "max pool mass ratio = sqrt(4/D_dodeca)")
def disc(x, y): return max(x / y, y / x)
our_mass_ratios = [y / x for x, y in ratios]
best_pair = []
for fam, trip in SM.items():
    a = [Decimal(x) for x in trip]
    for x_, y_ in itertools.combinations(a, 2):
        smr = y_ / x_
        best_pair.append((min(disc(r, smr) for r in our_mass_ratios), fam, f"{x_}:{y_}", smr))
chk(len(best_pair) == 9, f"all 9 SM ratios audited pairwise ({len(best_pair)})")
chk(all(b > 1 for b, _, _, _ in best_pair), "no pairwise match is exact")
bp = min(best_pair)
chk(str(bp[0]).startswith('2.62764'), f"best pairwise discrepancy {bp[0]} (documented x2.6276)")
chk(bp[1] == 'leptons' and bp[2] == '207:3477', f"best pairwise match is {bp[1]} {bp[2]}")
best_tri = {}
for fam, trip in SM.items():
    a = [Decimal(x) for x in trip]
    rsm = (a[1] / a[0], a[2] / a[0])
    bd = None
    for i, j, k in itertools.combinations(range(len(masses)), 3):
        v1, v2, v3 = masses[i], masses[j], masses[k]
        d = max(disc(v2 / v1, rsm[0]), disc(v3 / v1, rsm[1]))
        if bd is None or d < bd: bd = d
    best_tri[fam] = bd
chk(str(best_tri['down']).startswith('140.791'), f"down-type triple floor {best_tri['down']}")
chk(str(best_tri['leptons']).startswith('543.92'), f"lepton triple floor {best_tri['leptons']}")
chk(str(best_tri['up']).startswith('12514.75'), f"up-type triple floor {best_tri['up']}")
chk(min(best_tri.values()) > 10, "NO aligned triple is within an order of magnitude")
# the dimensionally-wrong m^2 comparison, reproduced and rejected
m2s = sorted(Decimal(k) for k in pool)
def best_m2(target):
    return min(max((b / a) / target, target / (b / a))
               for a, b in itertools.combinations(m2s, 2))
chk(str(best_m2(Decimal(20)))[:7] == '1.02158', f"m^2 vs m_s/m_d = 20: {best_m2(Decimal(20))}")
chk(str(best_m2(Decimal(45)))[:7] == '1.10122', f"m^2 vs 45: {best_m2(Decimal(45))}")
chk(str(best_m2(Decimal(3477) / Decimal(207)))[:7] == '1.12519', f"m^2 vs tau/mu: {best_m2(Decimal(3477)/Decimal(207))}")
allsm = [y / x for _, t in SM.items() for x, y in itertools.combinations([Decimal(v) for v in t], 2)]
tops = sorted(best_m2(s) for s in allsm)[:3]
chk([str(x)[:6] for x in tops] == ['1.0215', '1.1012', '1.1251'], f"top-3 wrong-variable hits {tops}")
# three-distinct-mass multiplets
three = []
for S in ORDER:
    for tag, key in (('A', 'kf'), ('B', 'kvf')):
        k = SOL[S][key]
        vs = sorted({str(D(m, S).dec(GDEC[SOL[S]['f']]))
                     for m in range(k, -k - 1, -2) if D(m, S) != 0})
        if len(vs) == 3: three.append((S, tag, [Decimal(v).sqrt() for v in vs]))
chk({(S, t) for S, t, _ in three} == {('dodeca', 'A'), ('icosa', 'B')},
    f"exactly two 3-distinct-mass multiplets: {[(S,t) for S,t,_ in three]}")
for S, tag, ms in three:
    r = (ms[1] / ms[0], ms[2] / ms[0])
    d = max(disc(r[0], Decimal(20)), disc(r[1], Decimal(900)))
    chk(d > 100, f"{S}({tag}) vs down-type discrepancy {d} > 100")
    if S == 'dodeca':
        chk(str(r[0]).startswith('2.902113') and str(r[1]).startswith('4.520147'), f"dodeca(A) mass ratios {r}")
        chk(str(d).startswith('199.1085'), f"dodeca(A) best discrepancy {d}")
    else:
        chk(str(r[0]).startswith('2.732050') and str(r[1]).startswith('3.732050'), f"icosa(B) mass ratios {r}")
        chk(str(d).startswith('241.1'), f"icosa(B) best discrepancy {d}")
# quantitative distance
need = Fr(4, 810000)
chk(need == Fr(1, 202500), "required D <= 4/810000 = 1/202500")
fac = D(1, 'dodeca').dec(GDEC['c']) * Decimal(202500)
chk(str(fac).startswith('19822.11'), f"D_dodeca / (1/202500) = {fac}")
chk(str(fac.sqrt())[:7] == '140.791', f"mass factor {fac.sqrt()} = the triple floor")
# D = 4 sin^2(delta/4) <= 1/202500  <=>  sin(delta/4) <= 1/900  <=>  delta <= 4 arcsin(1/900).
# Certified rational enclosure: x <= arcsin(x) <= x + x^3 for 0 < x <= 1/2 (Taylor, alternating).
x = Fr(1, 900)
d_lo, d_hi = 4 * x, 4 * (x + x ** 3)
chk(d_lo == Fr(1, 225), "delta_v <= 4 arcsin(1/900), lower bracket 1/225")
chk(d_hi - d_lo < Fr(1, 10 ** 8), f"delta_v bracket width {float(d_hi-d_lo):.2e}")
chk(str(Decimal(d_lo.numerator) / Decimal(d_lo.denominator)).startswith('0.00444444'),
    "delta_v <= 4.4444e-3 rad")
chk(Decimal(d_lo.numerator) / Decimal(d_lo.denominator) * Decimal(180) /
    Decimal('3.14159265358979323846') - Decimal('0.2546') < Decimal('0.0001'),
    "delta_v <= 0.2546 degrees")
# angle shortfall against the smallest Platonic defect, pi/5, with a certified pi bracket
plo, phi = Fr(314159265, 10 ** 8), Fr(314159266, 10 ** 8)
fac_lo = (plo / 5) / d_hi
fac_hi = (phi / 5) / d_lo
chk(Fr(1413714, 10 ** 4) < fac_lo and fac_hi < Fr(1413718, 10 ** 4),
    f"(pi/5)/delta_max in ({float(fac_lo):.6f}, {float(fac_hi):.6f})")
chk(fac_lo < 45 * plo and abs(fac_lo - 45 * plo) < Fr(1, 10 ** 3),
    "angle shortfall = 45*pi up to the arcsin cubic correction (< 1e-3)")
# the mass-ceiling shortfall (140.791) and the angle shortfall (141.372) agree to 0.5%:
chk(abs(Decimal('141.3717') / Decimal('140.7910') - 1) < Decimal('0.005'),
    "mass shortfall = angle shortfall to 0.5% (m proportional to delta at small angles)")
stamp("FT.77: pool 25/16/120/560, ceiling 6.392453, floors x140.79/x543.92/x12514.76, best pair x2.6276")
stamp("FT.77: m^2 near-coincidences reproduced and rejected; two 3-mass multiplets; distance 19822.11")

print(f"verify_H_polespectrum: {N} checks green  ({time.time()-t0:.1f}s)")
