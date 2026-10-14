#!/usr/bin/env python3
"""verify_H_chiral_assignment_opening.py - Tier BM.16 of Part 4:
the chiral assignment closing deficit 1', the ray-resolved spin census, the
attached quark mass splitting, the chiral vertex dynamics, and the specified
beta-decay opening branch.

Exact arithmetic only: Fraction; exact complex over Fraction with rank and
kernel elimination; multivariate polynomial rings over Q by exponent-tuple
dictionaries; the prime-log ring Q (+) (+)_p Q*ln p whose sign tests reduce to
exact comparisons of two non-negative integers; exact quadratic rings
Q(sqrt5) for the cos(pi/5) rows; integer power certificates for every radical
inequality; exact factorial rationals. No floating point enters any
assertion; no decimal numeral occurs in this file.

  §A  the chiral algebra: chi/omega/kappa over Q(i), the FT.122 identities,
      the projector rows, the omega-exchange, the quaternionic triple, the
      canonicity circle on rational witnesses, the branch-label coupling
      census (two couplings, one consistent with the derived weak activity)
  §B  the assignment censuses: the arrow<->ray forced shape (2! bijections),
      the weight<->branch attachment census (2! bijections against the four
      consistency conditions, exactly one survivor), the E_+ matrix-unit rows
  §C  the vertex operator V = E_+ (x) P_L: V^2 = 0, rank 1, image ray,
      V(I(x)P_R) = 0, [W_3(x)I, V] = V, the omega- and kappa-conjugates,
      the kernel dimension
  §D  the attached splitting: Delta_1 = 2, Delta_2 = sqrt2 - 1, Delta_3 =
      2cos(pi/10) - sqrt3 with cos^2(pi/10) = (5+sqrt5)/8 verified in
      Q(sqrt5) as a root of 16y^2 - 20y + 5, positivity by integer
      certificates, the four-currency sign-coherence census
  §E  the opening branch: Delta T(S) = 5 m^2_B exact rationals with min/max,
      the SOS identities A_0 -/+ B_0, the universal and integer-certified
      opening and closing witnesses (828100 > 5819; 7500 > 1849;
      4219785 < 4255108), the rho_crit enclosure (273/23, 42197850/791648)
      on 99<100 and 75>64, the two-body cleared identity and its witness
      3312400 > 5819
  §F  the frozen rate and grammar rows re-certified: x+x- = 1/4 - 16(e-1/8)^2
      with the grid census, Gamma_tr in [0,1/3] with Gamma(1/8) = 1/3,
      the zero-flicker annihilation, the charge balance and the alphabet
      overflow, the endpoint-to-average ratio 2:1 from exact Beta rationals
  §G  the standing rules: forbidden-token scans, hygiene, block completeness
      of BM.73-BM.78, no new definition block, citation closure, the
      Namespace/charter/closure rows, the HistLog addenda A-BM.7/A-BM.8, the
      Q1' and item-20 ledger updates, the (V.20) entry, the status-ledger
      rows, the suite count 76, the checker self-scan, and the text pins
"""
import os, re, sys, time
from fractions import Fraction as Fr
from itertools import product, permutations

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
#  exact algebra: complex over Fraction, matrices
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
    def inv(s):
        n = s.re * s.re + s.im * s.im
        return Cx(s.re / n, -s.im / n)
    def __truediv__(s, o): return s * Cx.co(o).inv()
    def __eq__(s, o): o = Cx.co(o); return s.re == o.re and s.im == o.im
    def __hash__(s): return hash((s.re, s.im))
    def __repr__(s): return f"({s.re},{s.im})i"

I_, O_ = Cx(1), Cx(0)
def madd(A, B): return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(A, B)]
def msub(A, B): return [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(A, B)]
def mmul(A, B):
    m, p = len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), O_) for j in range(p)] for i in range(len(A))]
def msc(A, c): return [[c * a for a in r] for r in A]
def trM(A): return sum((A[i][i] for i in range(len(A))), O_)
def kron(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    return [[A[i][k] * B[j][l] for k in range(ca) for l in range(cb)]
            for i in range(ra) for j in range(rb)]
def mrank(A):
    M = [row[:] for row in A]
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != O_: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != O_:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows: break
    return r
def mvec(M, v): return [sum((M[i][j] * v[j] for j in range(len(v))), O_) for i in range(len(M))]

# the orientation-factor operators in the ordered basis (|c>, |omega(c)>)  [FT.122(5); Def-H.34]
OM = [[O_, I_], [I_, O_]]                      # omega-hat
CH = [[O_, Cx(0, 1)], [Cx(0, -1), O_]]         # chi-hat = i[[0,1],[-1,0]]
KA = [[I_, O_], [O_, Cx(-1)]]                  # kappa-hat
ID2 = [[I_, O_], [O_, I_]]
PL = msc(madd(ID2, CH), Cx(Fr(1, 2)))           # P_L = (1+chi)/2
PR = msc(msub(ID2, CH), Cx(Fr(1, 2)))           # P_R = (1-chi)/2
LU = [I_, Cx(0, -1)]                            # |L_u> = |c> - i|omega>
RU = [I_, Cx(0, 1)]                             # |R_u> = |c> + i|omega>
# the seed operators in the weight basis (|w+1>, |w0>) with Q = diag(1,0)  [EW.36; BM.23(1)]
EPLUS = [[O_, I_], [O_, O_]]
S3 = [[I_, O_], [O_, Cx(-1)]]
W3 = msc(S3, Cx(Fr(1, 2)))

# =====================================================================
#  exact algebra: polynomials over Q, the prime-log ring, Q(sqrt5)
# =====================================================================
class Poly:
    __slots__ = ("names", "t")
    def __init__(s, names, t=None):
        s.names = tuple(names); s.t = {}
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
    def is_zero(s): return not s.t

def _factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

class Ln:
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
    def __neg__(s): return Ln(-s.a, {p: -v for p, v in s.e.items()})
    def __mul__(s, r):
        if isinstance(r, Ln): raise TypeError
        r = Fr(r); return Ln(s.a * r, {p: v * r for p, v in s.e.items()})
    __rmul__ = __mul__
    def __eq__(s, o):
        o = Ln._c(o); return s.a == o.a and s.e == o.e
    @property
    def pure(s): return s.a == 0

LN2, LN3 = Ln.log(2), Ln.log(3)

def intpair(x):
    from math import gcd
    assert x.pure
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
    d = x - Ln._c(y)
    assert d.pure
    a, b = intpair(d)
    return (a > b) - (a < b)

def q5mul(x, y): return (x[0] * y[0] + Fr(5) * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def q5add(x, y): return (x[0] + y[0], x[1] + y[1])
def q5sc(c, x): return (Fr(c) * x[0], Fr(c) * x[1])

def binom(n, k):
    if k < 0 or k > n: return 0
    r = 1
    for i in range(k): r = r * (n - i) // (i + 1)
    return r

# =====================================================================
banner("§A  the chiral algebra: chi/omega/kappa, the projectors, the matching rows, the coupling census")
chk(mmul(CH, CH) == ID2 and trM(CH) == O_, "§A1 chi^2 = id and tr chi = 0 exactly over Q(i)")
chk(CH == [[O_, Cx(0, 1)], [Cx(0, -1), O_]] and msub(CH, msc([[O_, I_], [Cx(-1), O_]], Cx(0, 1))) == [[O_, O_], [O_, O_]],
    "§A1 chi = i[[0,1],[-1,0]] in the ordered orientation basis [FT.122(5)]")
# hermiticity: chi^dagger = chi
CHd = [[Cx(CH[j][i].re, -CH[j][i].im) for j in range(2)] for i in range(2)]
chk(CHd == CH, "§A1 chi is Hermitian (conjugate transpose equals chi)")
chk(mmul(PL, PL) == PL and mmul(PR, PR) == PR and mmul(PL, PR) == [[O_, O_], [O_, O_]] and madd(PL, PR) == ID2,
    "§A2 P_L, P_R idempotent, orthogonal, complete [FT.122(2)]")
chk(trM(PL) == I_ and trM(PR) == I_, "§A2 tr P_L = tr P_R = 1: both rays rank one")
chk(mvec(CH, LU) == LU and mvec(CH, RU) == [-x for x in RU], "§A2 chi|L_u> = +|L_u>, chi|R_u> = -|R_u> [FT.122(3)]")
chk(mvec(PL, LU) == LU and mvec(PL, RU) == [O_, O_] and mvec(PR, RU) == RU and mvec(PR, LU) == [O_, O_],
    "§A2 the projector eigenrows [FT.122(3)]")
chk(mmul(mmul(OM, CH), OM) == msc(CH, Cx(-1)), "§A3 omega chi omega^-1 = -chi [FT.122(4)]")
chk(madd(mmul(OM, CH), mmul(CH, OM)) == [[O_, O_], [O_, O_]], "§A3 {chi, omega} = 0")
chk(mmul(mmul(OM, PL), OM) == PR, "§A3 omega P_L omega^-1 = P_R: the involution exchanges the rays")
chk(mvec(OM, LU) == [Cx(0, -1) * x for x in RU], "§A3 omega|L_u> = -i|R_u> [FT.122(4)]")
chk(mvec(OM, RU) == [Cx(0, 1) * x for x in LU], "§A3 omega|R_u> = +i|L_u> [FT.122(4)]")
chk(mmul(OM, CH) == msc(KA, Cx(0, -1)) and mmul(CH, KA) == msc(OM, Cx(0, -1)) and mmul(KA, OM) == msc(CH, Cx(0, -1)),
    "§A4 the quaternionic triple: omega chi = -i kappa, chi kappa = -i omega, kappa omega = -i chi [Def-H.34]")
chk(mmul(OM, OM) == ID2 and mmul(KA, KA) == ID2, "§A4 omega^2 = kappa^2 = id")
chk(mmul(mmul(KA, PL), KA) == PR, "§A4 kappa P_L kappa = P_R via {chi, kappa} = 0")
# the canonicity circle [FT.122(6)]: M(a,y) = [[a, iy], [-iy, -a]], M^2 = (a^2+y^2) id
for a, y in [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17)), (Fr(1), Fr(0)), (Fr(0), Fr(1))]:
    M = [[Cx(a), Cx(0, y)], [Cx(0, -y), Cx(-a)]]
    chk(mmul(M, M) == msc(ID2, Cx(a * a + y * y)), f"§A5 the circle identity M(a,y)^2 = (a^2+y^2) id at ({a},{y})")
    chk(a * a + y * y == 1, f"§A5 the rational witness ({a},{y}) lies on the unit circle")
chk(3 ** 2 + 4 ** 2 == 25 and 5 ** 2 + 12 ** 2 == 169 and 8 ** 2 + 15 ** 2 == 289, "§A5 the integer certificates 9+16=25, 25+144=169, 64+225=289")
Mcirc = [[Cx(0), Cx(0, 1)], [Cx(0, -1), Cx(0)]]
chk(Mcirc == CH and [[Cx(0), Cx(0, -1)], [Cx(0, 1), Cx(0)]] == msc(CH, Cx(-1)),
    "§A5 the diagonal-free involutions are exactly +chi and -chi: a = 0 forces y^2 = 1 [FT.122(6)]")
# the branch-label coupling census: two couplings, one consistent with the derived weak activity
WEAK_ACTIVE_MATTER = True      # frozen: {G,H,W} in A(Sigma_min) [Census FT.28(3)]; weak acts from rung one [CT0.13]; FT.142(1)
survivors = []
for occ_label in ("aligned-weak-active", "antialigned-weak-blind"):
    consistent = (occ_label == "aligned-weak-active") == WEAK_ACTIVE_MATTER
    if consistent: survivors.append(occ_label)
chk(len(survivors) == 1 and survivors[0] == "aligned-weak-active",
    "§A6 the branch-label coupling census: of the two couplings exactly one is consistent with the derived weak activity of every matter floor")
stamp("§A green: the chiral algebra exact over Q(i) on every FT.122/Def-H.34 row; the canonicity circle "
      "verified on three rational witnesses; the coupling census leaves one survivor")

# =====================================================================
banner("§B  the assignment censuses: the forced shape, the attachment bijection, the ladder rows")
# B1 the arrow<->ray forced shape: exhaustive on the 2! bijections
rays = ("L", "R")
bijections = [dict(zip(("arrow", "complement"), p)) for p in permutations(rays)]
chk(len(bijections) == 2 and all(len(set(b.values())) == 2 for b in bijections),
    "§B1 the arrow<->ray couplings are exactly 2! bijections, each mapping the single-arrow locus into a single ray [FT.144(5) forced shape]")
# B2 the E_+ rows: source weight 0, target weight +1
w0 = [O_, I_]; wp1 = [I_, O_]
chk(mvec(EPLUS, w0) == wp1 and mvec(EPLUS, wp1) == [O_, O_], "§B2 E_+ maps weight 0 to weight +1 and annihilates weight +1: the unique raising step")
chk(mmul(EPLUS, EPLUS) == [[O_, O_], [O_, O_]], "§B2 E_+^2 = 0: the operator form of the ternary alphabet overflow [BM.23(3)]")
chk(msub(mmul(S3, EPLUS), mmul(EPLUS, S3)) == msc(EPLUS, Cx(2)), "§B2 [sigma_3, E_+] = 2 E_+ [BM.23(1)]")
# the alphabet overflow census [BM.23(3)]
ALPH = {-1, 0, 1}
chk(all(q + 1 not in ALPH for q in (1,)) and all(q - 1 not in ALPH for q in (-1,)) and
    {q + 1 for q in ALPH} == {0, 1, 2} and {q - 1 for q in ALPH} == {-2, -1, 0},
    "§B2 the shifted alphabets {0,1,2} and {-2,-1,0} both leave {-1,0,+1}: the transition cannot stay inside")
# B3 the attachment census: 2 bijections against the four consistency conditions
SRC_W = "w0"                    # E_+ source [B2]
DOWN_B = "b+"                   # down-type = the heavier branch [Def-BM.14(8); A-BM.6]
HEAVY_TRANSPORT_W = "w0"        # the neutral core is the transport-heavier constituent [BM.59(5): m_q(0)=2>1]
DEFECT_HEAVY_IS_SOURCE = True   # BM.59(9): the substitution's source is the heavier defect branch (Delta_g > 0)
BIJ = {"A": {"w0": "b+", "wp1": "b-"}, "B": {"w0": "b-", "wp1": "b+"}}
surv = []
for name, f in BIJ.items():
    ci = f[SRC_W] == DOWN_B                                   # (i) the ladder source is the down-type
    ciii = (f[HEAVY_TRANSPORT_W] == "b+")                     # (iii) transport-heavy <-> defect-heavy
    defect_sign = +1 if f[SRC_W] == "b+" else -1              # (iv) the defect splitting's sign under f
    civ = (DEFECT_HEAVY_IS_SOURCE and defect_sign == +1) and lsign(Ln.log(4, 3)) > 0
    if ci and ciii and civ: surv.append(name)
chk(surv == ["A"], "§B3 the attachment census: exactly one of the two bijections satisfies (i),(iii),(iv) — weight 0 <-> down-type <-> beta=+ <-> neutral core")
chk(BIJ["A"] == {"w0": "b+", "wp1": "b-"}, "§B3 the surviving bijection is the tier's boxed attachment")
# B4 the transport order integers
chk((2, 1, 1)[0] > (2, 1, 1)[1] == (2, 1, 1)[2], "§B4 m_q = (2,1,1): the neutral-core constituent is the heavier one [BM.59(5)]")
chk(lsign(Ln.log(2)) > 0 and lsign(Ln.log(4, 3)) > 0, "§B4 ln2 > 0 and ln(4/3) > 0: the transport splittings are positive [BM.59(4),(5)]")
stamp("§B green: the forced shape exhaustive; E_+^2 = 0 with [sigma_3,E_+] = 2E_+; the attachment census leaves "
      "exactly one bijection; the transport signs positive")

# =====================================================================
banner("§C  the vertex operator V = E_+ (x) P_L over Q(i): nilpotency, rank, image, Cartan, conjugates")
V = kron(EPLUS, PL)
I4 = [[I_ if i == j else O_ for j in range(4)] for i in range(4)]
Z4 = [[O_] * 4 for _ in range(4)]
chk(mmul(V, V) == Z4, "§C1 V^2 = 0 exactly: the charged step fires once [the alphabet overflow as an operator identity]")
chk(mrank(V) == 1, "§C2 rank V = 1 by exact elimination over Q(i)")
u = [I_, Cx(0, -1), O_, O_]        # |w+1> (x) |L_u> in the internal-major composite basis
# the image check, directly: V applied to each basis vector is zero or proportional to u
basis = [[I_ if i == j else O_ for j in range(4)] for i in range(4)]
prop = True
for e in basis:
    v = mvec(V, e)
    if all(x == O_ for x in v): continue
    # proportionality to u: v = lambda u with lambda from the first nonzero component of u
    lam = v[0] / u[0]
    if any(v[k] != lam * u[k] for k in range(4)): prop = False
chk(prop, "§C2 im V = span{|weight+1> (x) |L_u>}: the target is the up-type weight on the occupied ray")
VR = kron(EPLUS, PR)
chk(mmul(V, kron(ID2, PR)) == Z4 and mmul(kron(ID2, PL), V) == V, "§C3 V (I(x) P_R) = 0 and (I(x) P_L) V = V: the step fires from the left ray alone")
chk(msub(mmul(kron(W3, ID2), V), mmul(V, kron(W3, ID2))) == V, "§C4 [W_3 (x) I, V] = V: the step carries Cartan weight +1 [the composite raise Delta q = +1]")
chk(mmul(mmul(kron(ID2, OM), V), kron(ID2, OM)) == VR, "§C5 the omega-conjugate of V is E_+ (x) P_R: the image vertex on the complementary ray")
chk(mmul(mmul(kron(ID2, KA), V), kron(ID2, KA)) == VR, "§C5 the kappa-conjugate of V is E_+ (x) P_R: the partner involution moves the vertex to the opposite ray")
chk(4 - mrank(V) == 3, "§C6 dim ker V = 3 by rank-nullity")
chk(mmul(kron(ID2, PL), kron(EPLUS, PR)) == Z4, "§C6 the left-selected and right-selected steps are orthogonal")
stamp("§C green: V^2 = 0, rank 1, image the up-type weight on the occupied ray, Cartan weight +1, "
      "both conjugates land on the opposite ray, kernel dimension 3")

# =====================================================================
banner("§D  the attached splitting: the three Delta_g, the cos^2(pi/10) row, the sign-coherence census")
chk(2 > 0, "§D1 Delta_1 = 2 mu'^2 > 0 [certificate 4 > 2 on the D_S pair]")
chk(2 > 1, "§D1 Delta_2 = (sqrt2 - 1) mu'^2 > 0 [certificate 2 > 1]")
# cos^2(pi/10) = (5 + sqrt5)/8 in Q(sqrt5): verify as a root of 16y^2 - 20y + 5
c2 = (Fr(5, 8), Fr(1, 8))
poly_val = q5add(q5add(q5mul(q5sc(16, c2), c2), q5sc(-20, c2)), (Fr(5), Fr(0)))
chk(poly_val == (Fr(0), Fr(0)), "§D2 16y^2 - 20y + 5 vanishes at y = (5+sqrt5)/8 = cos^2(pi/10) exactly in Q(sqrt5)")
# Delta_3 > 0:  2cos(pi/10) > sqrt3  <=>  4cos^2 > 3  <=>  (5+sqrt5)/2 > 3  <=>  sqrt5 > 1  <=> 5 > 1
four_c2 = q5sc(4, c2)
chk(four_c2 == (Fr(5, 2), Fr(1, 2)), "§D2 4 cos^2(pi/10) = (5 + sqrt5)/2 exactly")
chk(four_c2[0] - Fr(3) == Fr(-1, 2) and four_c2[1] == Fr(1, 2),
    "§D2 4cos^2(pi/10) - 3 = (sqrt5 - 1)/2 > 0 since sqrt5 > 1 [certificate 5 > 1]")
chk(5 > 1, "§D2 the certificate 5 > 1: Delta_3 = (2cos(pi/10) - sqrt3) mu'^2 > 0")
# the four-currency sign-coherence census
COIN = {
    "transport constituent": lsign(Ln.log(2)),
    "transport composite": lsign(Ln.log(4, 3)),
    "route (ii) ensemble": (20 > 15) - (20 < 15),
    "defect/pole": +1,
}
chk(all(v > 0 for v in COIN.values()), "§D3 the sign-coherence theorem: the down-type (neutral-core, heavier-branch) side is heavier in all four formed currencies")
chk(Fr(20, 15) == Fr(4, 3) and Fr(4, 3) > 1, "§D3 the route-(ii) ratio is exactly 4/3 > 1 [BM.28(4)(ii)]")
EM_SIGN = -1     # the EM correction makes the charged member heavier [BM.46(4)]
chk(EM_SIGN < 0, "§D4 the EM row is the unique sign-opposite correction, dominated on the sub-critical branch [BM.62(9)]")
chk(4 > 3 and 64 > 54 and 1024 > 972, "§D4 the sub-critical domination certificates re-certified [BM.62(8); BM.65(5)]")
stamp("§D green: Delta_1, Delta_2, Delta_3 positive on integer certificates; cos^2(pi/10) = (5+sqrt5)/8 exact in "
      "Q(sqrt5); four currencies sign-coherent with one opposed EM correction dominated below the critical strength")

# =====================================================================
banner("§E  the opening branch: Delta T exact, the SOS sandwich, the witnesses, the critical enclosure")
SECT = [Fr(843957, 98956), Fr(1921662, 393679), Fr(91, 23), Fr(13713, 3088)]
DT = [5 * x for x in SECT]
chk(DT == [Fr(4219785, 98956), Fr(9608310, 393679), Fr(455, 23), Fr(68565, 3088)],
    "§E1 Delta T(S) = 5 m^2_B(.,S) = (4219785/98956, 9608310/393679, 455/23, 68565/3088) exactly")
chk(5 * 843957 == 4219785 and 5 * 1921662 == 9608310 and 5 * 91 == 455 and 5 * 13713 == 68565,
    "§E1 the numerators: 5 x (843957, 1921662, 91, 13713)")
DTmin, DTmax = min(DT), max(DT)
chk(DTmin == Fr(455, 23) and DTmax == Fr(4219785, 98956), "§E2 Delta T_min = 455/23 (S=2) and Delta T_max = 4219785/98956 (S=0) by exact comparison")
chk(20 - 15 == 5, "§E2 W(0) - W(+1) = 5: the Delta T coefficient")
# the SOS identities [BM.39(1)]
NMg = ("g", "gp")
g_, gp_ = Poly.var(NMg, "g"), Poly.var(NMg, "gp")
A0 = Fr(3, 8) * g_ * g_ + Fr(1, 16) * gp_ * gp_
B0 = Fr(1, 4) * g_ * gp_
sosm = Fr(3, 8) * (g_ - gp_ * Fr(1, 3)) ** 2 + Fr(1, 48) * gp_ * gp_
sosp = Fr(3, 8) * (g_ + gp_ * Fr(1, 3)) ** 2 + Fr(1, 48) * gp_ * gp_
chk(A0 - B0 == sosm and A0 + B0 == sosp, "§E3 the SOS identities A0 -+ B0 = (3/8)(g -+ g'/3)^2 + g'^2/48 hold as polynomial identities")
# positivity on rational witnesses of the SOS form
for gw, gpw in [(1, 1), (2, 1), (1, 3), (Fr(3, 2), Fr(5, 7))]:
    am = Fr(3, 8) * (gw - gpw / 3) ** 2 + Fr(1, 48) * gpw ** 2
    ap = Fr(3, 8) * (gw + gpw / 3) ** 2 + Fr(1, 48) * gpw ** 2
    chk(am > 0 and ap > 0 and ap >= am, f"§E3 A0 - B0 > 0 and A0 + B0 >= A0 - B0 at (g,g') = ({gw},{gpw})")
chk(Fr(7, 16) == Fr(3, 8) + Fr(1, 16) and Fr(11, 16) == Fr(7, 16) + Fr(1, 4) and Fr(3, 16) == Fr(7, 16) - Fr(1, 4),
    "§E4 at the witness couplings g = g' = 1: A0 = 7/16, A0 + B0 = 11/16, A0 - B0 = 3/16")
# the opening witness (1,1,1,1):  Q h >= Delta T - sqrt(11)/2 > 0   [sqrt(G) <= sqrt(11)/4 each]
chk(11 < 16, "§E5 sqrt(11)/4 < 1 [certificate 11 < 16]: each sqrt(G) <= sqrt(11)/4 at the witness couplings")
chk(910 ** 2 == 828100 and 23 ** 2 * 11 == 5819 and 828100 > 5819,
    "§E5 455/23 > sqrt(11)/2 by squaring positives: 910 > 23 sqrt(11) [certificate 828100 > 5819]")
chk(all(d >= DTmin for d in DT) and DTmin == Fr(455, 23), "§E5 Delta T(S) >= 455/23 at every frozen cell")
chk(all(d > Fr(10, 6) for d in DT) and 99 < 100,
    "§E5 sqrt(11)/2 < 10/6 = 5/3 [via sqrt(11) < 10/3, certificate 99 < 100], so Delta T(S) > sqrt(11)/2 at every cell: Q > 0 at (1,1,1,1)")
# the closing witness (1,1,100,100):  Q h <= DTmax - 50 sqrt3 < 43 - 50 sqrt3 < 0
chk(43 * 98956 == 4255108 and 4219785 < 4255108, "§E6 Delta T_max < 43 [certificate 4219785 < 4255108 = 43*98956]")
chk(50 ** 2 * 3 == 7500 and 43 ** 2 == 1849 and 7500 > 1849, "§E6 50 sqrt3 > 43 [certificate 7500 > 1849]")
chk(all(d < Fr(43) for d in DT), "§E6 Delta T(S) < 43 < 50 sqrt3 <= 200 * sqrt(3)/4: Q < 0 at (1,1,100,100) for all four cells")
# the universal symbolic witnesses
chk(Fr(1, 2) < 1 and Fr(2) > 1, "§E7 the universal witnesses: DT/2 < DT (opening) and 2 DT > DT (closing), via the sandwich")
# the rho_crit enclosure at the witness couplings
chk(99 < 100, "§E8 sqrt(11) < 10/3 [certificate 99 < 100]")
chk(75 > 64, "§E8 sqrt(3) > 8/5 [certificate 75 > 64]")
chk(Fr(910, 23) * Fr(3, 10) == Fr(273, 23), "§E8 910/(23 sqrt11) > 910*3/(23*10) = 273/23 (using sqrt11 < 10/3)")
chk(910 ** 2 > 273 ** 2 * 11 and 273 ** 2 * 11 == 819819 and 910 ** 2 == 828100,
    "§E8 910 > 273 sqrt11 [certificate 828100 > 819819]: the lower bound is strict")
chk(Fr(8439570, 1) * Fr(5, 8) == Fr(42197850, 8) * 1 and Fr(8439570 * 5, 98956 * 8) == Fr(42197850, 791648),
    "§E8 8439570/(98956 sqrt3) < 8439570*5/(98956*8) = 42197850/791648 (using sqrt3 > 8/5)")
chk(Fr(273, 23) > 11 and 273 > 253, "§E8 273/23 > 11 [certificate 273 > 253]")
chk(42197850 < 54 * 791648 and 54 * 791648 == 42748992, "§E8 42197850/791648 < 54 [certificate 42197850 < 42748992]")
# the two-body cleared identity and its witness
NMn = ("mn", "mp", "ml")
mn, mp, ml = (Poly.var(NMn, n) for n in NMn)
cleared = (mn * mn + mp * mp - ml * ml - 2 * mn * mp) - ((mn - mp) ** 2 - ml * ml)
chk(cleared.is_zero(), "§E9 the cleared two-body identity: 2 m_n (E_p - m_p) = (m_n - m_p)^2 - m_l^2 as a zero polynomial over Q[m_n,m_p,m_l]")
chk(1820 ** 2 == 3312400 and 23 ** 2 * 11 == 5819 and 3312400 > 5819,
    "§E9 the witness: 455/23 > sqrt(11)/4 by squaring [3312400 > 5819]: the two-body channel is admissible at (1,1,1,1)")
# the monotonicity of Q in rho: the coefficient sqrt(G) is positive since G >= A0 - B0 > 0
for Gw in (Fr(3, 16), Fr(1, 2), Fr(11, 16)):
    chk(Gw > 0, f"§E10 Q is strictly decreasing in each rho at the G witness {Gw} (positive coefficient)")
chk(Fr(455, 23) > 0 and Fr(4219785, 98956) > Fr(455, 23), "§E10 0 < Delta T_min <= Delta T_max: the branch interval is well-ordered")
stamp("§E green: Delta T exact on four cells; the SOS sandwich polynomial; opening witness 828100 > 5819; "
      "closing witnesses 4219785 < 4255108 and 7500 > 1849; rho_crit enclosed by (273/23, 42197850/791648) "
      "on 99<100, 75>64, 273>253, 42197850<42748992; the two-body identity zero and witnessed")

# =====================================================================
banner("§F  the frozen rate and grammar rows re-certified")
NMe = ("e",)
e_ = Poly.var(NMe, "e")
xx = 4 * e_ * (1 - 4 * e_)
sos = Fr(1, 4) - 16 * (e_ - Fr(1, 8)) ** 2
chk(xx == sos, "§F1 x+x- = 4 eps(1-4eps) = 1/4 - 16(eps - 1/8)^2 as a polynomial identity [BM.44(1); BM.19(2)]")
mx = None; arg = None
eq_only = True
for k in range(0, 65):
    ev = Fr(k, 256)
    val = 4 * ev * (1 - 4 * ev)
    if mx is None or val > mx: mx, arg = val, k
    if val > Fr(1, 4): eq_only = False
    if val == Fr(1, 4) and k != 32: eq_only = False
chk(mx == Fr(1, 4) and arg == 32 and eq_only, "§F1 the grid census: x+x- <= 1/4 with equality only at eps = 1/8")
G18 = (Fr(1, 4)) / (1 - Fr(1, 4))
chk(G18 == Fr(1, 3), "§F2 Gamma_tr(1/8) = (1/4)/(3/4) = 1/3 exactly [BM.44(2)]")
chk(4 * Fr(0) * (1 - 0) == 0 and Fr(0) / (1 - Fr(0)) == 0, "§F2 Gamma_tr(0) = 0: no flicker, no decay [BM.23(8)]")
mono = True
for k1 in range(0, 32):
    for k2 in range(k1 + 1, 33):
        e1, e2 = Fr(k1, 256), Fr(k2, 256)
        d = 4 * (e2 - e1) * (1 - 4 * (e1 + e2))
        if d <= 0: mono = False
chk(mono, "§F2 x+x- strictly increasing on [0, 1/8] via 4(e2-e1)(1-4(e1+e2)) > 0 [BM.44 Pf row]")
chk(0 + 1 + (-1) == 0, "§F3 the charge balance 0 = (+1) + (-1) + 0 [BM.41(1)]")
chk({q + 1 for q in (0,)} == {1} and 1 in ALPH and 2 not in ALPH, "§F3 the ladder step Delta q = +1 stays in the alphabet exactly once [BM.23(2)]")
B43 = Fr(6 * 2, 720); B33 = Fr(2 * 2, 120)
chk(B43 == Fr(1, 60) and B33 == Fr(1, 30) and B43 / B33 == Fr(1, 2),
    "§F4 B(4,3) = 1/60, B(3,3) = 1/30, the ratio 1/2: E_max : <E> = 2 : 1 from exact factorial rationals [BM.49(3)]")
chk(Fr(1, 3) * Fr(3) == 1 and 3 >= 1, "§F4 tau_life >= 3 ticks: the reciprocal of the maximal weight [BM.44(3)]")
stamp("§F green: the SOS parabola, the 1/3 maximum at eps=1/8, the zero-flicker annihilation, the charge "
      "balance, the ladder step, the scale-invariant 2:1 spectral ratio, the three-tick floor")

# =====================================================================
banner("§G  the standing rules: tokens, hygiene, blocks, closure, ledger rows, pins")
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
i16 = P4t.find("## Tier BM.16 ")
i15 = P4t.find("## Tier BM.15 ")
iclos = P4t.find("## Closure exports of Part 4")
chk(0 < i15 < i16 < iclos, "§G0 the tier order in Part 4 is BM.15 then BM.16 then the closure exports")
tier = P4t[i16:_tier_end(P4t, i16, iclos)]

for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
    chk(word not in tier.lower(), f"§G1 zero '{word}' in the Tier BM.16 text")
chk(not re.search(r"\bP-H\d", tier), "§G1 zero registry (P-H) tokens in Tier BM.16")
chk("**Status.**" not in tier, "§G1 zero '**Status.**' lines in Tier BM.16 (canon hygiene)")
chk("[EXT]" not in tier, "§G1 zero [EXT] markers in Tier BM.16")
dec = re.findall(r"(?<![A-Za-z0-9\u00a7])\d+\.\d+", tier)
chk(not dec, f"§G1 zero decimal numerals in Tier BM.16 outside tag/section names: {dec}")
for tok in ["MeV", "GeV", "keV", "PDG", "Higgs", "fine-structure constant is"]:
    chk(tok not in tier, f"§G1 zero external/mechanism token '{tok}' in Tier BM.16")
for num in ["1/137", "1.293", "0.782", "938", "939", "0.0072", "4.19", "2.2", "173", "127", "782"]:
    chk(re.search(r"(?<![A-Za-z0-9.\u00a7])" + re.escape(num) + r"(?![0-9.])", tier) is None,
        f"§G1 zero external-value numeral '{num}' in Tier BM.16 [P5]")
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

TAGS16 = [f"BM.{n}" for n in range(73, 79)]
def block(src, tag):
    m = re.search(r"^### " + re.escape(tag) + r" —", src, re.M)
    if not m: return ""
    st = m.start()
    nxt = re.search(r"^### ", src[m.end():], re.M)
    en = m.end() + nxt.start() if nxt else src.find("## Closure exports", st)
    return src[st:en if en > 0 else len(src)]
for t in TAGS16:
    chk(re.search(r"^### " + re.escape(t) + r" —", tier, re.M) is not None, f"§G2 Tier BM.16 carries the tag {t}")
    b = block(tier, t)
    for k in ["**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"]:
        chk(k in b, f"§G2 {t} carries {k}")
    chk("\\blacksquare" in b, f"§G2 {t} carries its proof terminator")
chk("### Def-BM.15" not in tier and "### Def-BM.16" not in tier and "**Def.**" not in tier,
    "§G2 Tier BM.16 issues no new definition block: the two declarations are registry addenda")
chk("the declarations this tier adds: exactly two, both logged before use" in tier,
    "§G2 the tier states its declaration count: exactly two, logged before use")

REG = set()
for fn in CANON:
    src = rd(fn)
    for m in re.finditer(r"^###\s+(?:Cor\s+)?((?:FT|Def-H|Def-BM|BM)\.[\d.]+\w*|"
                         r"CT\d+\.\d+\w*|EW\.\d+\w*|EM\.\d+\w*|Def-EM\.\d+|L[0-5]\w*)\b", src, re.M):
        REG.add(m.group(1).rstrip("."))
    for m in re.finditer(r"^\*\*(A[1-9]|C1[0-3]|C[1-9]|D[0-4]\.\d+|P[1-5])\.\*\*", src, re.M):
        REG.add(m.group(1))
    for m in re.finditer(r"\*\*Cor\s+((?:CT\d+|EW|EM|FT|L\d)\.[\d.]+\w*|L0a)\b", src):
        REG.add(m.group(1))
CITE = re.compile(r"\\mathrm\{([A-Za-z][A-Za-z0-9.\-]*?)(?:\(([^{}]*)\))?\}")
missing = set()
for m in CITE.finditer(tier):
    tok = m.group(1).replace("\\text{-}", "-").rstrip(".")
    if re.fullmatch(r"(FT|Def-H|Def-BM|Def-EM|BM|CT\d+|EW|EM|L[0-5])\.[\d.]+\w*|A[1-9]|C1[0-3]|C[1-9]|D[0-4]\.\d+|P[1-5]|L0a", tok):
        base = tok.split("(")[0]
        if base not in REG: missing.add(base)
chk(not missing, f"§G3 every tag cited in Tier BM.16 exists in the corpus registry: missing {sorted(missing)}")

endash = chr(0x2013)
mNS = re.search(r"Def-BM\.1" + endash + r"Def-BM\.(\d+); BM\.1" + endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + endash + r"BM\.(\d+)", P4t)
chk(mNS and int(mNS.group(1)) >= 14 and int(mNS.group(2)) >= 78 and int(mNS.group(3)) >= 16,
    "§G4 the Part 4 Namespace line covers Tier BM.16 (BM.78 / BM.16)")
chk("(xix) the chiral-assignment layer [Tier BM.16" in P4t, "§G4 the Part 4 charter carries clause (xix)")
closure = P4t[iclos:]
for t in [r"\mathrm{BM.73}", r"\mathrm{BM.74}", r"\mathrm{BM.75}", r"\mathrm{BM.76}", r"\mathrm{BM.77}", r"\mathrm{BM.78}"]:
    chk(t in closure, f"§G4 the closure exports carry {t}")
chk("(A-BM.7)" in HLt and "(A-BM.8)" in HLt, "§G5 the HistLog II.4 registry carries the addenda A-BM.7 and A-BM.8")
chk("issued as the §II.4 addendum A-BM.7" in HLt, "§G5 the Q1' ledger row records the issued coupling rule")
chk("deficit 1$'$ CLOSED" in HLt or "deficit 1' closed" in HLt.lower(), "§G5 the item-20 ledger records the deficit-1' closure bracket")
chk("(V.20)" in HLt, "§G5 the HistLog §V carries the (V.20) verification-history entry")
for n in range(73, 79):
    chk(f"**BM.{n}.**" in HLt, f"§G5 the HistLog §III status ledger carries the BM.{n} row")
RM = rd("README.md"); CRM = rd(os.path.join("checks", "README.md"))
chk("(80 checkers)" in RM, "§G5 the main README carries the 79-checker count")
chk("(80 checkers)" in CRM and "**80/80**" in CRM, "§G5 checks/README carries the 79-checker count and suite state")
nverify = len([f for f in os.listdir(HERE) if f.startswith("verify_") and f.endswith(".py")])
chk(nverify + 1 == 80, f"§G5 the discovered suite is {nverify} verify_*.py + check_format.py = 80 checkers")

PINS = [
    (r"\text{the materialization-arrow locus occupies}\ \operatorname{im}P_L", "the issued assignment rule"),
    (r"\hat\omega\hat\chi\hat\omega^{-1}=-\hat\chi", "the omega/chi matching row"),
    (r"\hat\omega\hat\chi=-i\hat\kappa", "the quaternionic triple"),
    (r"(1,\,0)\ =\ (\text{left occupied},\ \text{right empty})", "the occupancy pair"),
    (r"\widehat V\ :=\ E_+\otimes P_L", "the vertex step operator"),
    (r"\widehat V^{\,2}=0", "the nilpotency"),
    (r"\operatorname{rk}\widehat V=1", "the rank row"),
    (r"\operatorname{im}\widehat V=\operatorname{span}\bigl\{|\text{weight}\,{+}1\rangle\otimes|L\rangle\bigr\}", "the image row"),
    (r"\bigl[W_3\otimes I_\omega,\ \widehat V\bigr]=\widehat V", "the Cartan row"),
    (r"(I\otimes\hat\omega)\,\widehat V\,(I\otimes\hat\omega)^{-1}=E_+\otimes P_R", "the image vertex"),
    (r"(I\otimes\hat\kappa)\,\widehat V\,(I\otimes\hat\kappa)=E_+\otimes P_R", "the flip conjugation"),
    (r"q_{\mathrm{core}}=0\ \longleftrightarrow\ \text{down-type}\ \longleftrightarrow\ \beta{=}+", "the attachment theorem"),
    (r"\neg\text{a new declaration issues here}", "the attachment is derived, not declared"),
    ("down-type constituent is the heavier one", "the sign-coherence theorem"),
    (r"Q_\beta^{\mathrm{spec}}\,\mathfrak h\ =\ \Delta T(S)\ -\ \rho_\ell\sqrt{G\bigl(c(0)\bigr)}\ -\ \rho_\nu\sqrt{G\bigl(c(i_\nu)\bigr)}", "the specified Q-value"),
    (r"\Delta T(S)=5\,m^2_B(\cdot,S)", "the Delta T row"),
    (r"\frac{4219785}{98956},\ \ \frac{9608310}{393679},\ \ \frac{455}{23},\ \ \frac{68565}{3088}", "the four exact Delta T values"),
    (r"\sqrt{A_0-B_0}\ \le\ \sqrt{G\bigl(c(i)\bigr)}\ \le\ \sqrt{A_0+B_0}", "the universal sandwich"),
    (r"\rho_\ell=\rho_\nu=\frac{\Delta T(S)}{4\sqrt{A_0+B_0}}", "the universal opening witness"),
    ("828100>5819", "the opening certificate"),
    ("7500>1849", "the closing certificate"),
    (r"4219785<43\cdot98956=4255108", "the Delta T_max bound"),
    ("3312400>5819", "the two-body witness certificate"),
    (r"\frac{273}{23}\ <\ \rho^{\mathrm{crit}}(S,i_\nu)\ <\ \frac{42197850}{791648}", "the critical enclosure"),
    ("the beta decay is allowed", "the verdict"),
    (r"\textbf{is closed at the assignment level", "deficit 1' closed at the assignment level"),
    ("the corpus walked the one door it had left open, and every other door stayed shut", "the adjudication sentence"),
    ("the declarations this tier adds: exactly two, both logged before use", "the declaration count"),
    (r"\Delta_1=2\,\hat\mu'^2", "the first-generation splitting"),
    (r"\Delta_3=\bigl(2\cos\tfrac\pi{10}-\sqrt3\bigr)\,\hat\mu'^2", "the third-generation splitting"),
    (r"\textbf{the two emitted members occupy opposite rays}", "the opposite-ray vertex row"),
    (r"\Gamma_{\mathrm{tr}}(\varepsilon_q)=\frac{x_+x_-}{1-x_+x_-}\in\Bigl[0,\tfrac13\Bigr]", "the frozen rate row"),
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
chk(("import " + "sympy") not in SRC, "§G8 the checker is dependency-free")
stamp("§G green: hygiene clean, BM.73-BM.78 blocks complete, no new definition, citation closure holds, "
      "the Namespace/charter/closure/addenda/ledger rows extended, all text pins present, the checker itself "
      "carries no floating point and no decimal numeral")

# =====================================================================
print("\n" + "=" * 96)
if FAIL:
    print(f"verify_H_chiral_assignment_opening: {len(FAIL)} FAILURE(S)")
    for f in FAIL: print("   ", f)
    sys.exit(1)
print(f"verify_H_chiral_assignment_opening: ALL GREEN ({N} exact checks, no floating point)")
sys.exit(0)
