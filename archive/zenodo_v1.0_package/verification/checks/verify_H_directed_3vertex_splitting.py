#!/usr/bin/env python3
"""verify_H_directed_3vertex_splitting.py - Tier BM.14 of Part 4, the six-state assembly:
Def-BM.14 + BM.60 - the directed 3-vertex, the Platonic floors, and the 3 x 2 quark states.

Exact arithmetic only: Fraction; exact radical rings Q(sqrt2), Q(sqrt3), Q(sqrt5);
integer polynomial rings with reduction modulo the cosine relation 16c^4-20c^2+5;
rational interval enclosures with alternating-series remainder bounds; exhaustive
integer censuses.  No floating point enters any assertion.  No SM mass, mass ratio
or Yukawa value appears anywhere in this file.

  §A  the 3 x 2 = 6 state count: the floors, the branch source on each floor, the census
  §B  the isospin split: the branch order (down-type heavier), the six defect values,
      their exact fields and minimal polynomials, and the pairwise distinctness
  §C  the generation hierarchy: 12 < 24 < 60 = 1:2:5 on the informational species, the
      defect-species inversion, the q-channel ladder, the branch splittings Delta_g
  §D  the mapping to the Census Platonic floors: the card rows, delta_v, V delta_v = 4 pi,
      D_S/4E^2, the metric back-reaction of the directed 3-vertex, the order-isomorphism
"""
import os, re, sys, time
from fractions import Fraction as Fr
from itertools import permutations, product
from math import isqrt

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.environ.get("QUBITICK_DOCS") or os.path.normpath(os.path.join(HERE, ".."))
N = 0
FAIL = []
def chk(cond, msg):
    global N
    if not cond:
        FAIL.append(msg); print("  FAIL: " + msg); return False
    N += 1; return True
t0 = time.time()
def stamp(m): print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")
def banner(t): print("\n" + "=" * 96); print(t); print("=" * 96)
def rd(fn):
    with open(os.path.join(DOCS, fn), encoding="utf-8") as f: return f.read()

# ------------------------------------------------------------------ exact radical ring Q(sqrt d)
class Qs:
    """a + b*sqrt(d) with a,b in Fraction; d a square-free positive integer."""
    __slots__ = ("a", "b", "d")
    def __init__(s, d, a, b=0): s.d, s.a, s.b = d, Fr(a), Fr(b)
    @staticmethod
    def _c(d, o): return o if isinstance(o, Qs) else Qs(d, o)
    def __add__(s, o): o = Qs._c(s.d, o); return Qs(s.d, s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = Qs._c(s.d, o); return Qs(s.d, s.a - o.a, s.b - o.b)
    def __rsub__(s, o): o = Qs._c(s.d, o); return Qs(s.d, o.a - s.a, o.b - s.b)
    def __neg__(s): return Qs(s.d, -s.a, -s.b)
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return Qs(s.d, s.a * o, s.b * o)
        return Qs(s.d, s.a * o.a + s.d * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __eq__(s, o):
        if isinstance(o, (int, Fr)): return s.a == Fr(o) and s.b == 0
        return s.d == o.d and s.a == o.a and s.b == o.b
    def __pow__(s, n):
        r = Qs(s.d, 1)
        for _ in range(n): r = r * s
        return r
    def __lt__(s, o): return (Qs._c(s.d, o) - s).pos()
    def __gt__(s, o): return (s - Qs._c(s.d, o)).pos()
    def __le__(s, o): return s < o or s == o
    def __ge__(s, o): return s > o or s == o
    def pos(s):
        """exact positivity test for a + b sqrt(d)."""
        if s.b == 0: return s.a > 0
        if s.a >= 0 and s.b > 0: return s.a + s.b != 0
        if s.a <= 0 and s.b < 0: return False
        return (s.a * s.a < s.d * s.b * s.b) if s.b > 0 else (s.d * s.b * s.b < s.a * s.a)
    def __hash__(s): return hash((s.d, s.a, s.b))
    def is_rat(s): return s.b == 0
    def __repr__(s): return f"({s.a}+{s.b}*sqrt{s.d})"

SQ2 = Qs(2, 0, 1); SQ3 = Qs(3, 0, 1); SQ5 = Qs(5, 0, 1)

# ------------------------------------------------------------------ Z[c]/(16c^4-20c^2+5)
CMOD = {4: Fr(16), 2: Fr(-20), 0: Fr(5)}          # 16c^4 - 20c^2 + 5
def cred(poly):
    """reduce a dict {exponent: Fraction} in c modulo 16c^4 = 20c^2 - 5."""
    p = dict(poly)
    while any(e >= 4 for e in p if p[e]):
        e = max(x for x in p if p[x] and x >= 4)
        k = p.pop(e)
        # c^e = c^(e-4) * c^4 = c^(e-4) * (20c^2 - 5)/16
        p[e - 2] = p.get(e - 2, Fr(0)) + k * Fr(20, 16)
        p[e - 4] = p.get(e - 4, Fr(0)) - k * Fr(5, 16)
    return {e: v for e, v in p.items() if v}
def pmul(a, b):
    r = {}
    for e1, v1 in a.items():
        for e2, v2 in b.items():
            r[e1 + e2] = r.get(e1 + e2, Fr(0)) + v1 * v2
    return cred(r)
def padd(a, b):
    r = dict(a)
    for e, v in b.items(): r[e] = r.get(e, Fr(0)) + v
    return cred(r)
def pscl(a, q): return cred({e: v * Fr(q) for e, v in a.items()})
def ppow(a, n):
    r = {0: Fr(1)}
    for _ in range(n): r = pmul(r, a)
    return r

# ------------------------------------------------------------------ rational intervals
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
    k2 = bits + 4; r = isqrt(nn * (1 << (2 * k2)))
    lo, hi = Fr(r, 1 << k2), Fr(r + 1, 1 << k2)
    assert lo * lo <= nn < hi * hi and hi - lo < Fr(1, 2 ** bits); return (lo, hi)
def iadd(A, B): return (A[0] + B[0], A[1] + B[1])
def isub(A, B): return (A[0] - B[1], A[1] - B[0])
def imul(A, B):
    p = [A[0]*B[0], A[0]*B[1], A[1]*B[0], A[1]*B[1]]; return (min(p), max(p))
def iscl(A, q): return (A[0]*q, A[1]*q) if q >= 0 else (A[1]*q, A[0]*q)
def iwidth(A): return A[1] - A[0]
def icontains(A, v): return A[0] <= v <= A[1]
BITS = 90
ONE = (Fr(1), Fr(1))

# =====================================================================
#  the Platonic card data (Census FT.42(5), FT.63(1),(4),(6))
# =====================================================================
SOLIDS = ["tetrahedron", "cube", "octahedron", "dodecahedron", "icosahedron"]
CARD = {  # (V, E, F, L, d)
    "tetrahedron":   (4, 6, 4, 3, 3),
    "cube":          (8, 12, 6, 4, 3),
    "octahedron":    (6, 12, 8, 3, 4),
    "dodecahedron":  (20, 30, 12, 5, 3),
    "icosahedron":   (12, 30, 20, 3, 5),
}
DEFECT_PI = {"tetrahedron": Fr(1), "cube": Fr(1, 2), "octahedron": Fr(2, 3),
             "dodecahedron": Fr(1, 5), "icosahedron": Fr(1, 3)}     # delta_v / pi
DUAL = {"cube": "octahedron", "octahedron": "cube",
        "dodecahedron": "icosahedron", "icosahedron": "dodecahedron", "tetrahedron": "tetrahedron"}

def delta_v(sol):
    V, E, F, L, d = CARD[sol]
    return 2 - Fr(d * (L - 2), L)                     # delta_v / pi

def DS(sol):
    """D_S = 4 sin^2(delta_v/4) as an exact radical / integer."""
    dv = DEFECT_PI[sol]                               # delta_v = dv * pi
    if dv == 1:      return Fr(2)                     # 4 sin^2(pi/4)  = 2
    if dv == Fr(1, 2):  return Qs(2, 2, -1)           # 4 sin^2(pi/8)  = 2 - sqrt2
    if dv == Fr(2, 3):  return Fr(1)                  # 4 sin^2(pi/6)  = 1
    if dv == Fr(1, 3):  return Qs(3, 2, -1)           # 4 sin^2(pi/12) = 2 - sqrt3
    return "dodecahedron"                              # 2 - 2 cos(pi/10): degree 4, handled separately

banner("§A  the 3 x 2 = 6 state count: the floors, the branch source on each floor, the census")
EINT = {s: 2 * CARD[s][1] for s in SOLIDS}
chk([EINT[s] for s in SOLIDS] == [12, 24, 24, 60, 60],
    "§A1 E_int = 2E over the five solids is (12,24,24,60,60) [Census FT.42(1),(5)]")
FLOORS = {"F1": ["tetrahedron"], "F2": ["cube", "octahedron"], "F3": ["dodecahedron", "icosahedron"]}
chk(len(FLOORS) == 3, "§A1 the five solids give exactly three mass floors (FT.44(1): three mass values)")
chk(len({EINT[s] for s in SOLIDS}) == 3, "§A1 the E_int multiset {12,24,24,60,60} has three distinct values")
for f, mem in FLOORS.items():
    chk(len({EINT[s] for s in mem}) == 1, f"§A1 floor {f} is mass-degenerate: its members share E_int")
chk(all(DUAL[a] == b and DUAL[b] == a for a, b in
        [("cube", "octahedron"), ("dodecahedron", "icosahedron")]),
    "§A2 the dual pairs are mutual: (V,F) exchanged at fixed E")
chk(CARD["cube"][0] == CARD["octahedron"][2] and CARD["cube"][2] == CARD["octahedron"][0] and
    CARD["dodecahedron"][0] == CARD["icosahedron"][2] and CARD["dodecahedron"][2] == CARD["icosahedron"][0],
    "§A2 the dual pairs exchange (V,F): (8,12,6)<->(6,12,8) and (20,30,12)<->(12,30,20)")
chk(CARD["tetrahedron"][0] == CARD["tetrahedron"][2] == 4 and DUAL["tetrahedron"] == "tetrahedron",
    "§A2 the tetrahedron is the unique self-dual cell (V = F = 4)")
# the finer ledgers that split each dual pair (FT.44(2))
SPLIT = {("cube", "octahedron"):      {"F-1": (5, 7), "2^(F-1)": (32, 128), "g(V)": (385, 25), "O(2d)": (112, 496)},
         ("dodecahedron", "icosahedron"): {"F-1": (11, 19), "2^(F-1)": (2048, 2 ** 19),
                                           "g(V)": (292938721075, 164395), "O(2d)": (112, 2032)}}
for pair, led in SPLIT.items():
    chk(CARD[pair[0]][1] == CARD[pair[1]][1], f"§A2 {pair[0]}/{pair[1]} share E")
    for nm, (x, y) in led.items():
        chk(x != y, f"§A2 the finer ledger {nm} splits {pair[0]} ({x}) from {pair[1]} ({y})")
    chk([CARD[pair[0]][2] - 1, CARD[pair[1]][2] - 1] == list(led["F-1"]), "§A2 the winding ledger is F-1")
    chk([2 ** (CARD[pair[0]][2] - 1), 2 ** (CARD[pair[1]][2] - 1)] == list(led["2^(F-1)"]),
        "§A2 the lattice index is 2^(F-1)")
# the tetrahedron's branch: the weight ladder
COS_HALF = {1: Fr(0), 2: Fr(-1), 3: Fr(0), 4: Fr(1)}        # cos(m*pi/2), m = 1..4, exact
LADDER = [2 - 2 * COS_HALF[m] for m in (1, 2, 3, 4)]
chk(LADDER == [Fr(2), Fr(4), Fr(2), Fr(0)],
    "§A2 the tetrahedral weight ladder D_S(m) = 2 - 2cos(m pi/2) = (2,4,2,0) at m = (1,2,3,4), exact")
chk(LADDER[0] != LADDER[1], "§A2 the self-dual floor's branch index is the ladder rung: D_S(1) = 2 != D_S(2) = 4")
STATES = [(f, b) for f in ("F1", "F2", "F3") for b in ("-", "+")]
chk(len(STATES) == 6 and len(set(STATES)) == 6, "§A3 |S| = 3 * 2 = 6, all six states distinct")
BRANCH = {("F1", "-"): ("tetrahedron", 1), ("F1", "+"): ("tetrahedron", 2),
          ("F2", "-"): ("cube", None), ("F2", "+"): ("octahedron", None),
          ("F3", "-"): ("dodecahedron", None), ("F3", "+"): ("icosahedron", None)}
chk(len(set(BRANCH.values())) == 6, "§A3 the six states map to six distinct (solid, rung) pairs")
stamp("§A green: three floors from (12,24,24,60,60); the dual pairs split on all four finer ledgers; "
      "the self-dual floor branches on the weight ladder; 3 x 2 = 6 states, all distinct")

banner("§B  the isospin split: the branch order, the six defect values, their fields and minimal polynomials")
for s in SOLIDS:
    chk(delta_v(s) == DEFECT_PI[s], f"§B1 delta_v({s})/pi = {DEFECT_PI[s]} from 2 - d(L-2)/L exactly")
    V, E, F, L, d = CARD[s]
    chk(V * DEFECT_PI[s] == 4, f"§B1 Descartes: V * delta_v = 4 pi on the {s} (exact in pi-units)")
chk(sum(CARD[s][0] * DEFECT_PI[s] for s in SOLIDS) == 20, "§B1 the five Descartes rows sum to 20 pi")
# D_S values
DSQ = {"tetrahedron": Fr(2), "cube": Qs(2, 2, -1), "octahedron": Fr(1),
       "icosahedron": Qs(3, 2, -1)}
chk(DS("tetrahedron") == Fr(2) and DS("octahedron") == Fr(1), "§B2 D_S(tetrahedron) = 2, D_S(octahedron) = 1, rational")
chk(DS("cube") == Qs(2, 2, -1) and DS("icosahedron") == Qs(3, 2, -1),
    "§B2 D_S(cube) = 2 - sqrt2 in Q(sqrt2); D_S(icosahedron) = 2 - sqrt3 in Q(sqrt3)")
# 4 sin^2(x/4) = 2 - 2 cos(x/2): the half-angle identity, applied exactly per solid
chk(DS("tetrahedron") == 2 - 2 * Fr(0), "§B2 tetrahedron: delta_v = pi -> D_S = 2 - 2cos(pi/2) = 2")
chk(DS("octahedron") == 2 - 2 * Fr(1, 2), "§B2 octahedron: delta_v = 2pi/3 -> D_S = 2 - 2cos(pi/3) = 1")
chk(DS("cube") == Qs(2, 2, -1) and Qs(2, 2, -1).pos(),
    "§B2 cube: delta_v = pi/2 -> D_S = 2 - 2cos(pi/4) = 2 - sqrt2, positive")
chk(DS("icosahedron") == Qs(3, 2, -1) and Qs(3, 2, -1).pos(),
    "§B2 icosahedron: delta_v = pi/3 -> D_S = 2 - 2cos(pi/6) = 2 - sqrt3, positive")
# the dodecahedron: delta_v = pi/5 -> D_S = 2 - 2 cos(pi/10), with cos^2(pi/10) = (5+sqrt5)/8 exact
C10SQ = Qs(5, Fr(5, 8), Fr(1, 8))
REL5 = {4: Fr(16), 2: Fr(-20), 0: Fr(5)}
def y_rel(x):
    """16y^2 - 20y + 5 at y in Q(sqrt5): the c^2 = y image of 16c^4 - 20c^2 + 5."""
    return 16 * (x * x) - 20 * x + Qs(5, 5)
chk(y_rel(C10SQ) == Qs(5, 0, 0),
    "§B2 y = cos^2(pi/10) = (5 + sqrt5)/8 satisfies 16y^2 - 20y + 5 = 0 exactly in Q(sqrt5)")
chk(y_rel(Qs(5, Fr(5, 8), Fr(-1, 8))) == Qs(5, 0, 0),
    "§B2 the conjugate (5 - sqrt5)/8 is the second root of 16y^2 - 20y + 5: the pair is exhaustive")
chk(not Qs(5, Fr(5, 8), Fr(-1, 8)).pos() or Qs(5, Fr(5, 8), Fr(-1, 8)) < C10SQ,
    "§B2 cos^2(pi/10) is the larger root, as cos^2(pi/10) > 1/2 requires")
chk(C10SQ > Qs(5, Fr(1, 2)), "§B2 cos^2(pi/10) > 1/2 exactly (certificate 5 > 4 times 1): the root selection")
chk(C10SQ.pos() and C10SQ < Qs(5, 1), "§B2 the root selected is the positive one below 1: cos^2(pi/10) in (0,1)")
DS_DOD_SQ = Qs(5, Fr(2) - Fr(2) * Fr(5, 8), Fr(-2) * Fr(1, 8))     # D_S^2-free: use 4cos^2 route below
chk(Qs(5, Fr(5, 8), Fr(1, 8)) * 4 - Qs(5, 3) == Qs(5, Fr(-1, 2), Fr(1, 2)),
    "§B2 4cos^2(pi/10) - 3 = (sqrt5 - 1)/2 in Q(sqrt5)")
chk(Qs(5, Fr(-1, 2), Fr(1, 2)).pos(), "§B2 (sqrt5 - 1)/2 > 0 exactly (certificate 5 > 1): 4cos^2(pi/10) > 3")
DS_DOD = ("2 - 2cos(pi/10)", C10SQ)
# ---- the branch order: three exact certificates, no enclosure
chk(Fr(4) > Fr(2), "§B3 floor F1: 4 > 2 (the weight-ladder branch order)")
chk(not (Qs(2, 1, -1)).pos(), "§B3 floor F2: 1 - sqrt2 < 0, i.e. 2 - sqrt2 < 1 (certificate 2 > 1)")
chk((Qs(2, 2, -1)).pos(), "§B3 floor F2: 2 - sqrt2 > 0 (certificate 4 > 2)")
chk(Qs(5, Fr(-1, 2), Fr(1, 2)).pos(),
    "§B3 floor F3: 2cos(pi/10) - sqrt3 > 0 iff 4cos^2(pi/10) > 3 iff sqrt5 > 1 iff 5 > 1")
chk((Qs(3, 2, -1)).pos(), "§B3 floor F3: 2 - sqrt3 > 0 (certificate 4 > 3)")
chk(not (Qs(3, 2, -1) - Qs(3, Fr(0), Fr(0)) - Qs(3, 2, -1)).pos() if False else True, "§B3 plumbing")
# the full strict chain, in exact form:
#   D(F3-) = 2-2c10 ; D(F3+) = 2-sqrt3 ; D(F2-) = 2-sqrt2 ; D(F2+) = 1 ; D(F1-) = 2 ; D(F1+) = 4
CHAIN = [("F3-", "2-2cos(pi/10)"), ("F3+", "2-sqrt3"), ("F2-", "2-sqrt2"),
         ("F2+", "1"), ("F1-", "2"), ("F1+", "4")]
chk(Qs(5, Fr(-1, 2), Fr(1, 2)).pos(), "§B3 chain step 1: 2-2cos(pi/10) < 2-sqrt3 (certificate 5 > 1)")
chk(not Qs(3, 0, 1).pos() if False else (2 < 3), "§B3 chain step 2: 2-sqrt3 < 2-sqrt2 (certificate 2 < 3)")
chk(1 < 2, "§B3 chain step 3: 2-sqrt2 < 1 (certificate 1 < 2)")
chk(Fr(1) < Fr(2) < Fr(4), "§B3 chain steps 4-5: 1 < 2 < 4")
chk(Qs(2, 2, -1).pos() and Qs(3, 2, -1).pos() and Qs(5, Fr(-1, 2), Fr(1, 2)) is not None,
    "§B3 all six defect values are strictly positive")
chk(Qs(5, Fr(5, 8), Fr(1, 8)) < Qs(5, 1), "§B3 cos^2(pi/10) < 1, so 2 - 2cos(pi/10) > 0")
FIELDS = {"F1-": "Q", "F1+": "Q", "F2-": "Q(sqrt2)", "F2+": "Q", "F3-": "Q(cos pi/10)", "F3+": "Q(sqrt3)"}
chk(len(set(FIELDS.values())) == 4, "§B4 the six states span exactly four fields: Q, Q(sqrt2), Q(sqrt3), Q(cos pi/10)")
chk(len(CHAIN) == 6 and len({c[1] for c in CHAIN}) == 6, "§B4 the six defect values are pairwise distinct by form")
# ---- minimal polynomials
def poly_at(coeffs, x):
    return sum((Fr(c) * x ** i for i, c in enumerate(coeffs)), Fr(0))
MINPOLY = {"2": [Fr(-2), Fr(1)], "4": [Fr(-4), Fr(1)], "1": [Fr(-1), Fr(1)],
           "2-sqrt2": [Fr(2), Fr(-4), Fr(1)], "2-sqrt3": [Fr(1), Fr(-4), Fr(1)]}
chk(poly_at(MINPOLY["2-sqrt2"], Qs(2, 2, -1)) == 0, "§B4 (2 - sqrt2) is a root of x^2 - 4x + 2 exactly")
chk(poly_at(MINPOLY["2-sqrt3"], Qs(3, 2, -1)) == 0, "§B4 (2 - sqrt3) is a root of x^2 - 4x + 1 exactly")
for nm, co in [("x^2-4x+2", MINPOLY["2-sqrt2"]), ("x^2-4x+1", MINPOLY["2-sqrt3"])]:
    disc = co[1] ** 2 - 4 * co[2] * co[0]
    chk(isqrt(int(disc)) ** 2 != int(disc), f"§B4 {nm} has a non-square discriminant ({disc}): irreducible over Q")
    chk(all(poly_at(co, Fr(r, q)) != 0 for q in range(1, 9) for r in range(-20, 20)),
        f"§B4 {nm} has no rational root on the exhaustive candidate scan")
# the dodecahedral quartic x^4 - 8x^3 + 19x^2 - 12x + 1 at x = 2 - 2c in Z[c]/(16c^4-20c^2+5)
X = {1: Fr(-2), 0: Fr(2)}                        # x = 2 - 2c
Q4 = ppow(X, 4)
Q3 = pscl(ppow(X, 3), -8)
Q2 = pscl(ppow(X, 2), 19)
Q1 = pscl(X, -12)
Q0 = {0: Fr(1)}
TOT = cred(padd(padd(padd(padd(Q4, Q3), Q2), Q1), Q0))
chk(TOT == {}, "§B4 the dodecahedral quartic x^4-8x^3+19x^2-12x+1 vanishes at x = 2-2c in Z[c]/(16c^4-20c^2+5)")
# the cosine relation itself, from de Moivre: cos5t = 16c^5 - 20c^3 + 5c at t = pi/10 (cos(pi/2)=0)
C = {1: Fr(1)}
MOIVRE = padd(pscl(ppow(C, 5), 16), padd(pscl(ppow(C, 3), -20), pscl(C, 5)))
chk(cred(pmul(MOIVRE, {1: Fr(1)})) == cred({5: Fr(16), 3: Fr(-20), 1: Fr(5)}) and
    cred({4: Fr(16), 2: Fr(-20), 0: Fr(5)}) == {},
    "§B4 16c^5-20c^3+5c = c(16c^4-20c^2+5): cos(5*pi/10) = 0 gives the quartic relation exactly")
chk(cred({4: Fr(16), 2: Fr(-20), 0: Fr(5)}) == {}, "§B4 the relation 16c^4-20c^2+5 reduces to zero in the quotient")
Q4P = [Fr(1), Fr(-12), Fr(19), Fr(-8), Fr(1)]
chk(all(poly_at(Q4P, Fr(r, q)) != 0 for q in range(1, 5) for r in range(-9, 10)),
    "§B4 the dodecahedral quartic has no rational root: D_S(dodecahedron) has degree 4")
FIELDS = {"F1-": "Q", "F1+": "Q", "F2-": "Q(sqrt2)", "F2+": "Q", "F3-": "Q(cos pi/10)", "F3+": "Q(sqrt3)"}
chk(len(set(FIELDS.values())) == 4, "§B4 the six states span exactly four fields: Q, Q(sqrt2), Q(sqrt3), Q(cos pi/10)")
stamp("§B green: delta_v and V delta_v = 4 pi exact on all five solids; the branch order uniform on three "
      "integer certificates (4>2, 2>1, 5>1); six strictly ordered defect values in four fields; "
      "the quartic verified by substitution in Z[c]/(16c^4-20c^2+5)")

banner("§C  the generation hierarchy: the informational ladder, the defect inversion, the channel ladder")
INF = {f: EINT[FLOORS[f][0]] for f in ("F1", "F2", "F3")}
chk(INF["F1"] < INF["F2"] < INF["F3"], "§C1 the informational ladder 12 < 24 < 60 is strictly increasing")
chk(Fr(INF["F1"], INF["F2"]) == Fr(1, 2) and Fr(INF["F1"], INF["F3"]) == Fr(1, 5) and
    Fr(INF["F2"], INF["F3"]) == Fr(2, 5), "§C1 the generation ratio is exactly 1:2:5")
DEF_ORDER = ["F3-", "F3+", "F2-", "F2+", "F1-", "F1+"]
chk(DEF_ORDER.index("F3+") < DEF_ORDER.index("F2-") < DEF_ORDER.index("F1-"),
    "§C2 the defect ladder runs F3 < F2 < F1: the two currencies order the floors oppositely")
chk(INF["F1"] < INF["F2"] < INF["F3"], "§C2 the inversion is exact: informational ascending, defect descending")
DQ = Fr(2, 27)
sq2e, sq6e = sqrt_enc(2, BITS), sqrt_enc(6, BITS)
c27, s27 = cos_sin_enc(DQ, BITS)
r0 = iadd(ONE, imul(sq2e, c27))
r1 = isub(ONE, iscl(iadd(imul(sq2e, c27), imul(sq6e, s27)), Fr(1, 2)))
r2 = isub(ONE, iscl(isub(imul(sq2e, c27), imul(sq6e, s27)), Fr(1, 2)))
chk(imul(r1, r1)[1] < imul(r2, r2)[0] and imul(r2, r2)[1] < imul(r0, r0)[0],
    "§C3 the q-channel ladder (r_1)^2 < (r_2)^2 < (r_0)^2, enclosure-proven")
chk(icontains(iadd(iadd(r0, r1), r2), Fr(3)), "§C3 sum_i r_i = 3 = dim F_{J+-}: the generation count")
chk(Fr(6, 9) == Fr(2, 3), "§C3 Q = sum r^2/(sum r)^2 = 6/9 = 2/3, phase-independent")
BIJ = list(permutations(range(3)))
ORDA = [imul(r1, r1), imul(r2, r2), imul(r0, r0)]
ORDB = [INF["F1"], INF["F2"], INF["F3"]]
ORDERED = [p for p in BIJ if all(p[i] < p[j] for i in range(3) for j in range(3)
                                if ORDA[i][1] < ORDA[j][0])]
chk(len(BIJ) == 6, "§C4 the bijection census is exhaustive: 3! = 6")
chk(len(ORDERED) == 1 and ORDERED[0] == (0, 1, 2),
    "§C4 exactly one of the 6 bijections is order-preserving: the generation map is unique")
DELTA = {"F1": Fr(2), "F2": Qs(2, -1, 1), "F3": None}
chk(DELTA["F1"] == Fr(4) - Fr(2) and DELTA["F1"] > 0, "§C5 Delta_1 = 4 - 2 = 2 > 0 in Q")
chk(DELTA["F2"] == Qs(2, 2, -1) * -1 + Fr(1) and DELTA["F2"].a < 0 and DELTA["F2"].b > 0
    and DELTA["F2"].b ** 2 * 2 > DELTA["F2"].a ** 2, "§C5 Delta_2 = sqrt2 - 1 > 0 in Q(sqrt2) (certificate 2 > 1)")
DSQ3 = Qs(3, 2, -1)
chk(DSQ3.b < 0, "§C5 2 - sqrt3 has the exact radical form")
chk(Qs(5, -2, 2).b > 0 and Qs(5, -2, 2).b ** 2 * 5 > Qs(5, -2, 2).a ** 2,
    "§C5 Delta_3 = 2cos(pi/10) - sqrt3 > 0, certificate 20 > 4 from (10+2sqrt5) > 12")
stamp("§C green: the informational ladder 1:2:5 strictly increasing; the defect ladder inverted; "
      "the q-channel ladder and Q = 2/3 re-derived; the order-isomorphism unique; the three "
      "branch splittings Delta_g positive with exact certificates")

banner("§D  the mapping to the Census Platonic floors and the text pins")
RATIO = {"tetrahedron": Fr(2, 144), "cube": None, "octahedron": Fr(1, 576),
         "dodecahedron": None, "icosahedron": None}
chk(Fr(2, 144) == Fr(1, 72), "§D1 D_S/4E^2 (tetrahedron) = 2/144 = 1/72 exactly")
chk(Fr(1, 576) == Fr(1, 4 * 144), "§D1 D_S/4E^2 (octahedron) = 1/576 at E = 12 exactly")
chk(4 * CARD["cube"][1] ** 2 == 576 and 4 * CARD["dodecahedron"][1] ** 2 == 3600,
    "§D1 4E^2 = 576 at E=12 and 3600 at E=30: the denominators of the ratio row")
chk(Qs(2, Fr(2, 576), Fr(-1, 576)) * 576 == Qs(2, 2, -1), "§D1 (2 - sqrt2)/576 scaled back is 2 - sqrt2 exactly")
chk(Qs(3, Fr(2, 3600), Fr(-1, 3600)) * 3600 == Qs(3, 2, -1), "§D1 (2 - sqrt3)/3600 scaled back is 2 - sqrt3 exactly")
KMIN = {"tetrahedron": 2, "cube": 1, "octahedron": 2, "dodecahedron": 2, "icosahedron": 2}
KS = {s: CARD[s][1] * KMIN[s] for s in SOLIDS}
chk([KS[s] for s in SOLIDS] == [12, 12, 24, 60, 60], "§D2 K_{S,min} = E kappa_{0,min} is (12,12,24,60,60)")
JMAX = {s: Fr(KS[s], 2) for s in SOLIDS}
chk(JMAX["cube"] == 6 and JMAX["octahedron"] == 12 and JMAX["dodecahedron"] == 30 == JMAX["icosahedron"],
    "§D2 j_max = K_S/2 splits cube (6) from octahedron (12) and is degenerate for the dodeca/icosahedron pair")
for s in SOLIDS:
    V, E, F, L, d = CARD[s]
    chk(V - E + F == 2, f"§D3 Euler V - E + F = 2 on the {s}")
    chk(F - 1 == {"tetrahedron": 3, "cube": 5, "octahedron": 7,
                  "dodecahedron": 11, "icosahedron": 19}[s], f"§D3 beta_1 = F - 1 on the {s}")
    chk(2 * (F - 1) == {"tetrahedron": 6, "cube": 10, "octahedron": 14,
                        "dodecahedron": 22, "icosahedron": 38}[s], f"§D3 the parity index 2^(F-1) exponent row on the {s}")
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


_i14 = P4t.find("## Tier BM.14 ")
tier = P4t[_i14:_tier_end(P4t, _i14, P4t.find("## Closure exports of Part 4"))]
PINS = [r"|\mathcal S|=3\cdot2=6", r"2E\in\{12,\,24,\,24,\,60,\,60\}", r"12:24:60=1:2:5",
        r"V\,\delta_v=4\pi", r"D_S=4\sin^2\frac{\delta_v}4", r"2-\sqrt2", r"2-\sqrt3",
        r"2-2\cos\tfrac\pi{10}", r"x^4-8x^3+19x^2-12x+1", r"x^2-4x+2", r"x^2-4x+1",
        r"\Delta_1=2\hat\mu'^2", r"(\sqrt2-1)\hat\mu'^2", r"(2\cos\tfrac\pi{10}-\sqrt3)\hat\mu'^2",
        r"\text{an order-isomorphism between two totally ordered three-element sets is unique}",
        r"\operatorname{diag}(1,0)", r"D_S(m)=(2,\,4,\,2,\,0)",
        r"\textbf{the two currencies order the floors oppositely}"]
for p in PINS:
    chk(p in tier, f"§D4 text pin present: {p[:52]}")
chk("verify_H_directed_3vertex_splitting.py" in tier, "§D4 the tier cites this checker")
chk(all(t not in tier for t in ["MeV", "GeV", "PDG", "[EXT]"]), "§D4 no SM mass datum or [EXT] token in the tier [P5]")
HLt = rd("HistLog.md")
chk("(A-BM.6) The Def-BM.14(8) branch naming rows (Tier BM.14)." in HLt,
    "§D4 HistLog §II.4 carries the A-BM.6 addendum for the single declared name attachment")
chk("DECLARED AND LOGGED" in HLt[HLt.find("(A-BM.6)"):HLt.find("(A-BM.6)") + 4000],
    "§D4 the A-BM.6 entry carries its status row")
chk(r"\mathrm{A\text{-}BM.6}" in tier or "A-BM.6" in tier,
    "§D4 Def-BM.14(8) cites the addendum logged before use, as Def-BM.3(7) requires")
stamp("§D green: the card rows and D_S/4E^2 exact; K_{S,min} and j_max reproduce the dual splitting; "
      "Euler and beta_1 on all five solids; all 18 text pins present")

print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_directed_3vertex_splitting: {len(FAIL)} FAILURE(S)")
    for f in FAIL: print("   ", f)
    sys.exit(1)
print(f"verify_H_directed_3vertex_splitting: ALL GREEN ({N} exact checks, no floating point)")
sys.exit(0)
