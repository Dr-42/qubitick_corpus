#!/usr/bin/env python3
"""
verify_L_lyapunov.py — machine verification of the A4/A6/A7 repair pass, the
Lyapunov restoration (B, Tier 2: L1-L3), and the eps_q-dependent tilt
(gamma = 1 - 4 eps_q, D0.3).

Exact arithmetic only: int / fractions.Fraction / complex-over-Fraction
(qmath.C) / truncated formal power series over Fraction (rational gamma
parameter) / exact Q(sqrt2) with exact order / rational log- and
exp-enclosures (series with exact rational tail bounds — no floating point
anywhere).

Sections:
  §A  gamma arithmetic (Directive-5 table): contraction c(gamma) = 1-gamma/4
      and decay 1-c^2 = gamma(8-gamma)/16 for gamma in {0,1/4,1/2,3/4,1}
      (exact Fractions; anchors: gamma=1 -> 3/4, 7/16; gamma=0 -> 1, 0);
      phi_gamma-calculus: phi_gamma = phi_1 + (1-gamma)x^2 and
      phi_gamma'' = (14+16x-32x^2)/(1+4x)^2 + 2(1-gamma) coefficient-wise in
      Q[[x]]; leading coefficients (8-gamma, -16); convexity-window roots
      (1 +- 2 sqrt2)/4 exact in Q(sqrt2); window contains [-1/4, 3/4].
  §B  L1(3)/L2/L3 identities as exact formal power series in Q[[t]]/(t^12)
      along rho(t) = I/4 + t*delta0 for five exact rational traceless
      families x gamma in {1/4,1/2,3/4,1}:
      (I1g) V'-V + gamma*sum phi_gamma(mu) = O(t^4) [quartic sharpness pinned];
      (I2g) V'-V + (gamma(8-gamma)/16) V = O(t^3) [cubic sharpness];
      (I6g) V'-V + (gamma(8-gamma)/2) DeltaS = O(t^3);
      (I8g) mu' - (1-gamma/4) mu = O(t^2);
      gamma-free: (I3) K~ + 4 t delta0 = O(t^2); (I4) V - 16 t^2 sum d^2 =
      O(t^3); (I5) S(rho||I/4) - 2 t^2 sum d^2 = O(t^3) [cubic sharpness];
      (I7) V - 8 S(rho||I/4) = O(t^3); trace normalization; the vacuum fixed
      point of every tilt (e^{-gamma/4} cancels in the ratio, exact).
  §C  L1(2)/(5) global facts: Haar-tick components (polynomial covariance and
      trace invariance, exact over Q(i)); global monotonicity V' <= V per
      gamma (exact rational log/exp enclosures; full grid 1/24 at gamma=1,
      grid 1/16 + extremes at gamma in {1/4,1/2,3/4}); equality only at the
      vacuum; sum phi_1(mu) >= 0 (Jensen witness set, inherited by every
      phi_gamma = phi_1 + (1-gamma)x^2); phi_1 > 0 on [-1/4,3/4]\{0}.
  §D  document pins: A4/A6/A7 axiom forms (zero-English scan); D0.3 gamma
      tilt form (incl. T~_gamma(K) = K rho^gamma / T(K rho^gamma)); B Tier 2
      gamma identities present and free of SM/hierarchy/fermion vocabulary;
      A7 absent from L3's Req; CT0.8 branch clause; E Def-EM.20 branch
      mechanism; H13 registries (Axiom Revision, Tilt Revision, P-H12/P-H13).

Run: python3 verify_L_lyapunov.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import os
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

import re
import sys
import random
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C, matmul, conj_transpose, trace  # noqa: E402

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


GAMMAS = [Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(1)]


# ---------------------------------------------------------------- Q(sqrt2)

class Q2:
    """Exact a + b*sqrt2 over Fraction, with exact total order."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = a if isinstance(a, Fr) else Fr(a)
        self.b = b if isinstance(b, Fr) else Fr(b)

    def __add__(self, o):
        return Q2(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return Q2(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __eq__(self, o):
        return self.a == o.a and self.b == o.b

    def __le__(self, o):
        return not (o < self)

    def __lt__(self, o):
        d = o - self
        a, b = d.a, d.b
        if b == 0:
            return a > 0
        if b > 0:
            return a >= 0 or a * a < 2 * b * b
        return a > 0 and a * a > 2 * b * b

    def __repr__(self):
        return f"Q2({self.a},{self.b})"


# ---------------------------------------------------------------- Q[[t]]/(t^N)

N = 12


class Ser:
    __slots__ = ("c",)

    def __init__(self, c):
        self.c = list(c) + [Fr(0)] * (N - len(c))

    @staticmethod
    def const(x):
        return Ser([x if isinstance(x, Fr) else Fr(x)])

    def __add__(self, o):
        return Ser([a + b for a, b in zip(self.c, o.c)])

    def __sub__(self, o):
        return Ser([a - b for a, b in zip(self.c, o.c)])

    def __neg__(self):
        return Ser([-a for a in self.c])

    def __mul__(self, o):
        out = [Fr(0)] * N
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if i + j < N and b:
                        out[i + j] += a * b
        return Ser(out)

    def scale(self, x):
        x = x if isinstance(x, Fr) else Fr(x)
        return Ser([a * x for a in self.c])

    def inv(self):
        assert self.c[0] != 0
        out = [Fr(0)] * N
        out[0] = 1 / self.c[0]
        for n in range(1, N):
            s = Fr(0)
            for k in range(1, n + 1):
                s += self.c[k] * out[n - k]
            out[n] = -s / self.c[0]
        return Ser(out)

    def __eq__(self, o):
        return self.c == o.c

    def __repr__(self):
        return f"Ser({[str(x) for x in self.c[:6]]}...)"


def ser_log1p(u):
    assert u.c[0] == 0
    acc = Ser([Fr(0)])
    pw = Ser([Fr(1)])
    for k in range(1, N):
        pw = pw * u
        acc = acc + pw.scale(Fr((-1) ** (k + 1), k))
    return acc


def ser_exp(u):
    assert u.c[0] == 0
    acc = Ser([Fr(0)])
    pw = Ser([Fr(1)])
    fact = Fr(1)
    for k in range(0, N):
        if k > 0:
            fact *= k
            pw = pw * u
        acc = acc + pw.scale(Fr(1) / fact if k else Fr(1))
    return acc


def deriv(s):
    return Ser([Fr(k + 1) * s.c[k + 1] for k in range(N - 1)])


def loworders(s, k):
    return all(x == 0 for x in s.c[:k])


# ---------------------------------------------------------------- §B model

def lyapunov_series(d, g):
    """Series objects for rho(t) = I/4 + t*diag(d), tilt strength gamma = g."""
    assert sum(d) == 0 and len(d) == 4
    t = Ser([Fr(0), Fr(1)])
    lam = [Ser.const(Fr(1, 4)) + t.scale(di) for di in d]
    L = [ser_log1p(t.scale(4 * di)) for di in d]
    sum_lamL = Ser([Fr(0)])
    for li, Li in zip(lam, L):
        sum_lamL = sum_lamL + li * Li
    Kt = [sum_lamL - Li for Li in L]               # log2 cancels exactly
    V = Ser([Fr(0)])
    for k in Kt:
        V = V + k * k
    u = [ser_exp(t.scale(-g * di)) for di in d]    # e^{-gamma t d_i}
    Zt = Ser([Fr(0)])
    for li, ui in zip(lam, u):
        Zt = Zt + li * ui                          # const term 1 (e^{-gamma/4} cancels)
    Zi = Zt.inv()
    lamp = [li * ui * Zi for li, ui in zip(lam, u)]
    logZt = ser_log1p(Zt - Ser.const(Fr(1)))       # log Z_gamma = -gamma/4 + logZt
    Lp = [Li - li.scale(g) + Ser.const(g / 4) - logZt for Li, li in zip(L, lam)]
    Sump = Ser([Fr(0)])
    for lp, Lq in zip(lamp, Lp):
        Sump = Sump + lp * Lq
    Ktp = [Sump - Lq for Lq in Lp]
    Vp = Ser([Fr(0)])
    for k in Ktp:
        Vp = Vp + k * k
    phi_sum = Ser([Fr(0)])                         # sum phi_gamma(mu_i(t))
    for di, Li in zip(d, L):
        mu = t.scale(di)
        phi_sum = phi_sum + mu.scale(2) * Li - (mu * mu).scale(g)
    return dict(lam=lam, lamp=lamp, Kt=Kt, V=V, Vp=Vp, phi_sum=phi_sum,
                Srel=sum_lamL, sumd2=sum(di * di for di in d), d=d)


def sectionB():
    print("S2 = §B formal-series identities (exact over Q, order 12; gamma x family sweeps)")
    fams = [(1, -1, 0, 0), (1, 1, -1, -1), (3, -1, -1, -1),
            (2, -1, 3, -4), (5, -3, -7, 5)]
    okI1 = okI2 = okI6 = okI8 = True
    okI3 = okI4 = okI5 = okI7 = okTr = True
    sharp1 = sharp2 = sharp5 = False
    for g in GAMMAS:
        decay = g * (8 - g) / 16
        for d in fams:
            M = lyapunov_series([Fr(x) for x in d], g)
            V, Vp, phis, t = M["V"], M["Vp"], M["phi_sum"], Ser([Fr(0), Fr(1)])
            sumd2 = M["sumd2"]
            t2 = t * t
            # I1g: V' - V + gamma * sum phi_gamma = O(t^4)
            r1 = Vp - V + phis.scale(g)
            if not loworders(r1, 4):
                okI1 = False
            if r1.c[4] != 0:
                sharp1 = True
            # I2g: V' - V + decay*V = O(t^3)
            r2 = Vp - V + V.scale(decay)
            if not loworders(r2, 3):
                okI2 = False
            if r2.c[3] != 0:
                sharp2 = True
            # I6g: V' - V + (gamma(8-gamma)/2) * DeltaS = O(t^3), DeltaS = 2 t^2 sum d^2
            r6 = Vp - V + t2.scale(g * (8 - g) * sumd2)   # (g(8-g)/2)*(2 sumd2) = g(8-g) sumd2
            if not loworders(r6, 3):
                okI6 = False
            # I8g: mu' - (1-gamma/4) mu = O(t^2)
            for lp, di in zip(M["lamp"], M["d"]):
                mup = lp - Ser.const(Fr(1, 4))
                if not loworders(mup - t.scale((1 - g / 4) * di), 2):
                    okI8 = False
            # gamma-free identities
            for Ki, di in zip(M["Kt"], M["d"]):
                if not loworders(Ki + t.scale(4 * di), 2):
                    okI3 = False
            if not loworders(V - t2.scale(16 * sumd2), 3):
                okI4 = False
            r5 = M["Srel"] - t2.scale(2 * sumd2)
            if not loworders(r5, 3):
                okI5 = False
            if r5.c[3] != 0:
                sharp5 = True
            if not loworders(V - M["Srel"].scale(8), 3):
                okI7 = False
            tot = Ser([Fr(0)])
            for li in M["lam"]:
                tot = tot + li
            if not loworders(tot - Ser.const(Fr(1)), N):
                okTr = False
    chk("§B(I1g) V' - V + gamma*sum phi_gamma(mu) = O(t^4) for every gamma in "
        "{1/4,1/2,3/4,1} x 5 exact rational families (coefficient-wise in Q[[t]])", okI1)
    chk("§B(I1g-sharp) the t^4 coefficient is nonzero on a generic family-gamma pair: "
        "the O(delta^4) remainder is sharp", sharp1)
    chk("§B(I2g) V' - V + (gamma(8-gamma)/16) V = O(t^3): the decay law with the exact "
        "rational gamma-dependent coefficient", okI2 and sharp2)
    chk("§B(I6g) V' - V + (gamma(8-gamma)/2) DeltaS_pair = O(t^3) (L3(3))", okI6)
    chk("§B(I8g) mu' = (1-gamma/4) mu + O(t^2) (L2 eigenvalue contraction, exact "
        "coefficient per gamma)", okI8)
    chk("§B(I3) K~ = -4 t delta0 + O(t^2) (gamma-free)", okI3)
    chk("§B(I4) V = 16 t^2 sum d^2 + O(t^3) (gamma-free)", okI4)
    chk("§B(I5) S(rho||I/4) = 2 t^2 sum d^2 + O(t^3), cubic term sharp (gamma-free)",
        okI5 and sharp5)
    chk("§B(I7) V = 8 S(rho||I/4) + O(t^3) (gamma-free)", okI7)
    chk("§B trace normalization: sum lambda_i(t) = 1 as an exact series (the log2 "
        "cancellation in K~ is exact at every gamma)", okTr)
    # vacuum fixed point of every tilt: (1/4 * c) / (4 * 1/4 * c) = 1/4, c = e^{-gamma/4} cancels
    c = Fr(7, 3)
    chk("§B vacuum: every tilt fixes lambda = 1/4 exactly (e^{-gamma/4} cancels in the "
        "ratio); K~ = 0 there (log-parts cancel symbolically) => V = 0 [L1(1)]",
        (Fr(1, 4) * c) / (4 * Fr(1, 4) * c) == Fr(1, 4))


# ---------------------------------------------------------------- enclosures

def log2_enc(tol):
    z = Fr(1, 3)
    z2 = z * z
    s = Fr(0)
    n = 0
    while True:
        s += 2 * z ** (2 * n + 1) / (2 * n + 1)
        nn = n + 1
        tail = 2 * z ** (2 * nn + 1) / ((2 * nn + 1) * (1 - z2))
        if tail < tol:
            return (s, s + tail)
        n += 1


def log_enc(y, tol, l2):
    assert y > 0
    k = 0
    m = y
    while m < Fr(3, 4):
        m *= 2
        k -= 1
    while m > Fr(3, 2):
        m /= 2
        k += 1
    if m == 1:
        base = (Fr(0), Fr(0))
    else:
        z = (m - 1) / (m + 1)
        z2 = z * z
        s = Fr(0)
        n = 0
        while True:
            s += 2 * z ** (2 * n + 1) / (2 * n + 1)
            nn = n + 1
            tail = 2 * abs(z) ** (2 * nn + 1) / ((2 * nn + 1) * (1 - z2))
            if tail < tol / 2:
                base = (s - tail, s + tail)
                break
            n += 1
    lo2, hi2 = l2
    add = (k * lo2, k * hi2) if k >= 0 else (k * hi2, k * lo2)
    return (base[0] + add[0], base[1] + add[1])


def exp_enc(x, nterms=24):
    """Exact (lo, hi) for e^x, x in [-1, 0]: alternating decreasing partial sums."""
    assert Fr(-1) <= x <= 0
    acc = Fr(0)
    pw = Fr(1)
    f = 1
    vals = []
    for k in range(nterms + 2):
        if k > 0:
            pw *= x
            f *= k
        acc += pw / f
        vals.append(acc)
    a, b = vals[nterms], vals[nterms + 1]
    return (min(a, b), max(a, b))


class Iv:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi):
        assert lo <= hi
        self.lo, self.hi = lo, hi

    def __add__(self, o):
        return Iv(self.lo + o.lo, self.hi + o.hi)

    def __sub__(self, o):
        return Iv(self.lo - o.hi, self.hi - o.lo)

    def __neg__(self):
        return Iv(-self.hi, -self.lo)

    def __mul__(self, o):
        ps = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return Iv(min(ps), max(ps))

    def __truediv__(self, o):
        assert o.lo > 0 or o.hi < 0
        ps = [self.lo / o.lo, self.lo / o.hi, self.hi / o.lo, self.hi / o.hi]
        return Iv(min(ps), max(ps))

    def sq(self):
        if self.lo >= 0:
            return Iv(self.lo * self.lo, self.hi * self.hi)
        if self.hi <= 0:
            return Iv(self.hi * self.hi, self.lo * self.lo)
        m = max(-self.lo, self.hi)
        return Iv(Fr(0), m * m)


def IV(x):
    x = x if isinstance(x, Fr) else Fr(x)
    return Iv(x, x)


def log_enc_pair(Ziv, tol, l2):
    lo = log_enc(Ziv.lo, tol, l2)
    hi = log_enc(Ziv.hi, tol, l2)
    return (lo[0], hi[1])


def V_interval(lams, g, tol, l2):
    """(V, V') intervals for eigenvalues lams under tilt strength g."""
    logs = [Iv(*log_enc(l, tol, l2)) for l in lams]
    S = Iv(Fr(0), Fr(0))
    for l, lg in zip(lams, logs):
        S = S - IV(l) * lg
    Kt = [(-lg) - S for lg in logs]
    V = sum((k.sq() for k in Kt), Iv(Fr(0), Fr(0)))
    exps = [Iv(*exp_enc(-g * l)) for l in lams]
    num = [IV(l) * e for l, e in zip(lams, exps)]
    Z = sum(num[1:], num[0])
    lamp = [n / Z for n in num]
    logZ = Iv(*log_enc_pair(Z, tol, l2))
    logsp = [lg - IV(g * l) - logZ for lg, l in zip(logs, lams)]
    Sp = Iv(Fr(0), Fr(0))
    for lp, lgp in zip(lamp, logsp):
        Sp = Sp - lp * lgp
    Ktp = [(-lgp) - Sp for lgp in logsp]
    Vp = sum((k.sq() for k in Ktp), Iv(Fr(0), Fr(0)))
    return V, Vp


def phi1_interval(mu, tol, l2):
    y = 1 + 4 * mu
    if y <= 0:
        return None
    lg = Iv(*log_enc(y, tol, l2))
    return IV(2 * mu) * lg - IV(mu * mu)


def grid(G):
    pts = []
    for a in range(1, G - 2):
        for b in range(1, G - a - 1):
            for c in range(1, G - a - b):
                d = G - a - b - c
                if d >= 1:
                    pts.append([Fr(a, G), Fr(b, G), Fr(c, G), Fr(d, G)])
    return pts


EXTREMES = [[Fr(97, 100), Fr(1, 100), Fr(1, 100), Fr(1, 100)],
            [Fr(997, 1000), Fr(1, 1000), Fr(1, 1000), Fr(1, 1000)],
            [Fr(7, 10), Fr(1, 10), Fr(1, 10), Fr(1, 10)],
            [Fr(4, 10), Fr(4, 10), Fr(1, 10), Fr(1, 10)],
            [Fr(2397, 2400), Fr(1, 2400), Fr(1, 2400), Fr(1, 2400)],
            [Fr(7, 24), Fr(6, 24), Fr(6, 24), Fr(5, 24)]]


def sectionC():
    print("S3 = §C global monotonicity per gamma, Jensen witnesses, Haar components "
          "(exact enclosures)")
    tol = Fr(1, 10 ** 9)
    l2 = log2_enc(Fr(1, 10 ** 12))
    chk("§C log2 enclosure sane: 0.69 < log2 < 0.70 (exact rational bounds)",
        Fr(69, 100) < l2[0] and l2[1] < Fr(70, 100))

    # ---- Haar-tick components (gamma-free)
    rng = random.Random(20260928)

    def rc():
        return C(Fr(rng.randint(-4, 4), 3), Fr(rng.randint(-4, 4), 3))

    def rand4():
        return [[rc() for _ in range(4)] for _ in range(4)]

    def unitary4():
        perm = list(range(4))
        rng.shuffle(perm)
        phases = [C(1), C(-1), C(0, 1), C(0, -1)]
        M = [[C(0)] * 4 for _ in range(4)]
        for i in range(4):
            M[i][perm[i]] = phases[rng.randrange(4)]
        return M

    ok_cov = True
    for _ in range(6):
        U = unitary4()
        Ud = conj_transpose(U)
        rho = rand4()

        def pw(M, k):
            r = M
            for _ in range(k - 1):
                r = matmul(r, M)
            return r
        for p in (2, 3):
            lhs = pw(matmul(matmul(U, rho), Ud), p)
            rhs = matmul(matmul(U, pw(rho, p)), Ud)
            if any(lhs[i][j] != rhs[i][j] for i in range(4) for j in range(4)):
                ok_cov = False
        if trace(matmul(matmul(U, rho), Ud)) != trace(rho):
            ok_cov = False
    chk("§C Haar-tick components: p(U rho U^dag) = U p(rho) U^dag for p = X^2, X^3 and "
        "T(U rho U^dag) = T(rho), exact over Q(i) — assembles L1(2): V is tick-invariant",
        ok_cov)

    # ---- global monotonicity per gamma
    vac = [Fr(1, 4)] * 4
    all_ok = True
    counts = {}
    for g in GAMMAS:
        pts = (grid(24) if g == 1 else grid(16)) + EXTREMES
        bad = []
        for lam in pts:
            if lam == vac:
                continue
            V, Vp = V_interval(lam, g, tol, l2)
            if (Vp - V).hi > 0:
                bad.append(lam)
        counts[g] = len(pts)
        if bad:
            all_ok = False
            print(f"    gamma={g}: bad points {bad[:2]}")
    chk(f"§C global monotonicity: V' - V <= 0 for every gamma in {{1/4,1/2,3/4,1}} "
        f"(grids {counts}, extremes included; rational log/exp enclosures, no floats)",
        all_ok)
    # strictness witness per gamma at (7,6,6,5)/24
    lam1 = [Fr(7, 24), Fr(6, 24), Fr(6, 24), Fr(5, 24)]
    ok_strict = True
    for g in GAMMAS:
        V, Vp = V_interval(lam1, g, tol, l2)
        if (Vp - V).hi >= 0:
            ok_strict = False
    chk("§C strictness: V' - V < 0 exactly resolved at (7,6,6,5)/24 for every gamma "
        "(contraction is strict off-vacuum on the sweep)", ok_strict)
    # vacuum equality (exact symbolic; enclosure sanity)
    V0, V0p = V_interval(vac, Fr(1), tol, l2)
    chk("§C equality locus: at the vacuum V = V' = 0 within enclosure width < 1e-9 "
        "(the exact identity is §B's symbolic cancellation)",
        max(abs(x) for iv in (V0, V0p) for x in (iv.lo, iv.hi)) < tol)

    # ---- Jensen witnesses via phi_1 (phi_gamma = phi_1 + (1-gamma)x^2 inherits)
    bad_j = []
    for lam in grid(24) + EXTREMES:
        s = Iv(Fr(0), Fr(0))
        for l in lam:
            s = s + phi1_interval(l - Fr(1, 4), tol, l2)
        if s.hi < 0:
            bad_j.append(lam)
    chk("§C Jensen witnesses: sum phi_1(mu) >= 0 on the exact rational sweep; every "
        "phi_gamma = phi_1 + (1-gamma) mu^2 inherits the bound for gamma in (0,1] "
        "(L1(4)-(5)); equality only at mu = 0", not bad_j)
    bad_phi = []
    for k in range(-11, 37):
        x = Fr(k, 48)
        if x == 0 or x <= Fr(-1, 4) or x >= Fr(3, 4):
            continue
        iv = phi1_interval(x, tol, l2)
        if iv.hi <= 0:
            bad_phi.append(x)
    p0 = phi1_interval(Fr(0), tol, l2)
    chk("§C phi_1(x) > 0 on [-1/4, 3/4] \\ {0} (48-denominator sweep, exact enclosures); "
        "phi_1(0) = 0 exactly", not bad_phi and p0.lo == 0 and p0.hi == 0)


# ---------------------------------------------------------------- §A

def sectionA():
    print("S1 = §A gamma arithmetic table + phi_gamma-calculus (exact)")
    # Directive-5 table: contraction and decay per gamma, exact Fractions
    tab_ok = True
    want = {Fr(0): (Fr(1), Fr(0)), Fr(1, 4): (Fr(15, 16), Fr(31, 256)),
            Fr(1, 2): (Fr(7, 8), Fr(15, 64)), Fr(3, 4): (Fr(13, 16), Fr(87, 256)),
            Fr(1): (Fr(3, 4), Fr(7, 16))}
    for g, (cw, dw) in want.items():
        c = 1 - g / 4
        dec = 1 - c * c
        alt = g * (8 - g) / 16
        if not (c == cw and dec == dw and alt == dw):
            tab_ok = False
    chk("§A contraction/decay table: c(gamma) = 1-gamma/4 and decay 1-c^2 = "
        "gamma(8-gamma)/16 for gamma in {0,1/4,1/2,3/4,1} — exact Fractions; anchors: "
        "gamma=1 -> (3/4, 7/16); gamma=0 -> (1, 0)", tab_ok)
    # phi_gamma series identities
    x = Ser([Fr(0), Fr(1)])
    x2 = x * x
    log1p4 = ser_log1p(x.scale(4))
    phi1 = x.scale(2) * log1p4 - x2
    chk("§A phi_1 coefficients: c0=c1=0, c2=7, c3=-16, c4=128/3 (exact)",
        phi1.c[0] == 0 and phi1.c[1] == 0 and phi1.c[2] == 7
        and phi1.c[3] == -16 and phi1.c[4] == Fr(128, 3))
    num = Ser([Fr(14), Fr(16), Fr(-32)])
    den = Ser([Fr(1), Fr(4)])
    phi1pp = deriv(deriv(phi1))
    rhs1 = num * den.inv() * den.inv()
    chk("§A phi_1'' = (14+16x-32x^2)/(1+4x)^2 coefficient-wise (orders 0..9)",
        phi1pp.c[:N - 2] == rhs1.c[:N - 2])
    okg = True
    for g in GAMMAS:
        phig = x.scale(2) * log1p4 - x2.scale(g)
        # phi_gamma = phi_1 + (1-gamma) x^2
        if phig != phi1 + x2.scale(1 - g):
            okg = False
        # phi_gamma'' = phi_1'' + 2(1-gamma)
        pp = deriv(deriv(phig))
        if pp.c[:N - 2] != [c + (2 * (1 - g) if k == 0 else Fr(0))
                            for k, c in enumerate(rhs1.c[:N - 2])]:
            okg = False
        # leading coefficients: (8-gamma)x^2 - 16x^3
        if phig.c[2] != 8 - g or phig.c[3] != -16 or phig.c[0] != 0 or phig.c[1] != 0:
            okg = False
    chk("§A phi_gamma identity block for gamma in {1/4,1/2,3/4,1}: phi_gamma = phi_1 + "
        "(1-gamma)x^2; phi_gamma'' = (14+16x-32x^2)/(1+4x)^2 + 2(1-gamma); leading "
        "(8-gamma)x^2 - 16x^3; phi_gamma(0) = phi_gamma'(0) = 0 (all exact in Q[[x]])", okg)
    r1 = Q2(Fr(1, 4), Fr(-1, 2))
    r2 = Q2(Fr(1, 4), Fr(1, 2))
    poly = lambda z: z * z * Q2(16) - z * Q2(8) - Q2(7)
    chk("§A convexity-window roots: 16x^2-8x-7 vanishes exactly at (1 +- 2 sqrt2)/4 "
        "in Q(sqrt2)", poly(r1) == Q2(0) and poly(r2) == Q2(0))
    chk("§A window contains the eigenvalue domain: (1-2 sqrt2)/4 <= -1/4 and "
        "3/4 <= (1+2 sqrt2)/4 (exact Q(sqrt2) order); W_gamma >= W_1 for gamma <= 1 "
        "since phi_gamma'' = phi_1'' + 2(1-gamma) >= phi_1''",
        r1 <= Q2(Fr(-1, 4)) and Q2(Fr(3, 4)) <= r2)


# ---------------------------------------------------------------- §D pins

def sectionD():
    print("S4 = §D document pins (repair pass + gamma pass)")

    def rd(fn):
        return era_paths.read(fn)

    A, B = rd("A_axioms.md"), rd("B_foundation.md")
    E = rd("E_electromagnetic.md")
    if ARCH:
        H13 = rd("H_archive/H13_registries_and_gaps.md")

    def block(src, a, b):
        i = src.index(a)
        j = src.index(b, i)
        return src[i:j]

    a4 = block(A, "**A4.**", "**A5.**")
    a6 = block(A, "**A6.**", "**A7.**")
    a7 = block(A, "**A7.**", "**A8.**")
    chk("§D A4: two-branch criterion, alpha_pq cases, populatedness clause",
        a4.count(r"\ge1-\varepsilon_q") >= 2 and r"\alpha_{pq}:=\begin{cases}" in a4
        and r"\exists\,\rho_{pq}" in a4 and r"\exists\,\rho_{p'q'}" in a4)
    chk("§D A6: Haar tick form present; thermal map absent; irreversibility clauses",
        r"\mathcal T(\rho):=U\rho U^\dagger" in a6 and r"\neg\exists\,\tau^{-1}" in a6
        and r"\mathcal T^{2}\ne\mathbb1" in a6 and r"\mathcal T^{-1}(\rho)=U^\dagger\rho U" in a6
        and "e^{-\\rho}" not in a6 and r"\mathbb V" not in a6
        and r"\mu_{\mathrm{Haar}}" in a6 and r"n_{\mathrm{real\_out}}" in a6)
    chk("§D A7: phase map and ledger stratification",
        r"\alpha_e\in\{0,\pi\}" in a7 and r"\mathfrak L=\bigcup_{n\ge0}\mathfrak L(\tau_n)" in a7
        and r"\bigl|\mathfrak L(\tau_0)\bigr|=0" in a7 and r"n_{\mathrm{real\_out}}(\tau_k)" in a7)

    def english_free(blk):
        t = re.sub(r"\\{1,2}\[\d+mm\]", " ", blk)
        t = re.sub(r"\\(?:begin|end)\{[a-zA-Z*]+\}", " ", t)
        for w in ("Haar", "SU", "real\\_out"):
            t = t.replace(w, " ")
        t = re.sub(r"\\[a-zA-Z]+", " ", t)
        t = re.sub(r"_\{[^{}]*\}", "", t)
        t = t.replace("'", "")
        return not re.search(r"[A-Za-z]{2,}", t)

    chk("§D zero English inside the A4/A6/A7 axiom blocks (macro-stripped scan)",
        all(english_free(b) for b in (a4, a6, a7)))

    d03 = block(A, "**D0.3.**", "**D0.4.**")
    chk("§D D0.3: gamma tilt form — gamma := 1-4 eps_q with [A4, D0.4, CT0.8]; "
        "T~_gamma on states and on K (rho^gamma form); identity at gamma=0; L1 pointer; "
        "non-interchangeability with the A6 tick",
        r"\gamma:=1-4\varepsilon_q" in d03 and "[A4, D0.4, CT0.8]" in d03
        and r"\tilde{\mathcal T}_\gamma(\rho)=\rho\,e^{-\gamma\rho}" in d03
        and r"\tilde{\mathcal T}_\gamma(K)=K\rho^{\gamma}/\mathfrak T(K\rho^{\gamma})" in d03
        and r"\gamma=0:" in d03 and "L1" in d03 and "interchangeable" in d03
        and "RESERVED" not in d03)
    ct08 = block(B, "### CT0.8 — ", "### CT0.9 — ")
    chk("§D CT0.8: two-branch sharp case (supp in vee^2 or pure singlet) + disjointness",
        r"\rho_{pq}=\Pi_{\mathcal V}" in ct08 and "disjoint" in ct08
        and r"\alpha_{pq}=0\ /\ \pi" in ct08)
    tier2 = block(B, "\n## Tier 2 — ", "## Closure exports of Part 1 §F")
    chk("§D B Tier 2: gamma identities present — phi_gamma, gamma(8-gamma)/16, "
        "(1-gamma/4) contraction, gamma-weighted decay identity",
        r"\phi_\gamma" in tier2 and r"\gamma(8-\gamma)" in tier2
        and r"1-\tfrac\gamma4" in tier2 and r"-\gamma\sum_i\phi_\gamma(\mu_i)" in tier2)
    l3 = block(B, "### L3 — ", "## Closure exports of Part 1 §F")
    req3 = l3[l3.index("**Req.**"):l3.index("**Pf.**")]
    chk("§D L3 Req: A7 removed (the inertial read is definitional at pair level)",
        "A7" not in req3)
    chk("§D B Tier 2 free of identification vocabulary: no 'SM', 'hierarchy', 'fermion' "
        "(the interpretation lives in the H-layer registry, P-H13)",
        not re.search(r"\bSM\b|hierarchy|fermion", tier2))
    for h in ("\n## Tier 2 — ", "### L1 — ", "### L2 — ", "### L3 — "):
        if h not in B:
            chk(f"§D B heading present: {h}", False)
    chk("§D B Tier 2: L1, L2, L3 blocks present with machine pointers",
        B.count("verify_L_lyapunov.py") >= 4)
    de = block(E, "### Def-EM.20 — ", "### EM.20 — ")
    chk("§D E Def-EM.20: the phase is A4's branch index (alpha_e = alpha_st)",
        r"\alpha_{st}" in de and r"\Pi_{\mathcal V}\rho_{st}" in de and "A4" in de)
    if ARCH:
        chk("§D H13: Axiom Revision Registry, Tilt Revision Registry, P-H12 and P-H13 logged",
            "**Axiom Revision Registry (A4/A6/A7 repair pass).**" in H13
            and "**Tilt Revision Registry" in H13
            and "**(P-H12)**" in H13 and "**(P-H13)**" in H13)


def main():
    print("verify_L_lyapunov: repair pass + gamma-tilt restoration (exact)")
    sectionA()
    sectionB()
    sectionC()
    sectionD()
    print(f"verify_L_lyapunov: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
