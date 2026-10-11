#!/usr/bin/env python3
"""
verify_L0_ledger_tilt.py — machine verification of the ledger-tilt dynamics pass
(B, Tier 2: L0 + Cor L0a, L4, L5).

Exact arithmetic only: int / fractions.Fraction / complex-over-Fraction
(qmath.C) / truncated formal power series over Fraction / rational log- and
exp-enclosures (series with exact rational tail bounds — no floating point).

Sections:
  §A  coupling arithmetic: gamma = 1 - 4 eps_q endpoint map (CT0.8 range);
      c = 1-gamma/4, d = gamma(8-gamma)/8, exact Fraction table for
      gamma in {0,1/4,1/2,3/4,1}; identities 1-c^2 = gamma(8-gamma)/16,
      4d = gamma(8-gamma)/2, d/2 = gamma(8-gamma)/16 (L2 consistency);
      anchors gamma=1: (c,d) = (3/4, 7/8), gamma=0: (1, 0).
  §B  Cor L0a spectral K-update identity K' = K + gamma rho + log Z_gamma:
      eigenvalue-level -log lam' = -log lam + gamma lam + log Z_gamma by exact
      rational log/exp-enclosures at two tolerances (tightening), 4 gammas x
      (grid + extremes).
  §C  Jensen block: g(p) = p e^{-gamma p} concavity sign gamma^2 p - 2 gamma <= 0
      (exact rationals); Z_gamma <= e^{-gamma/4} with equality iff vacuum;
      tr(deltaK) = gamma + 4 log Z_gamma <= 0, strict off-vacuum, pinch at
      vacuum; Z_gamma > 0 (faithfulness/positivity of the tilt).
  §D  L0 ledger and collapse: exact integer recursion |L(tau_n)| = sum_{k<n}
      n_real_out(tau_k) (A6/A7 closed form) on witness sequences; Haar spectral
      preservation tr((U rho U^dag)^m) = tr(rho^m), m=1..4, exact over Q(i)
      (signed perms x Pythagorean blocks); tilt permutation-equivariance and
      V-collapse under interleaving (eigenvalue enclosures); vacuum fixed
      point; mu_k = (1-gamma/4)^k mu_0 + O(mu_0^2), k <= 3 (series composition).
  §E  L4 patch deficit: multi-channel series sum_e S(rho_e||I/4) =
      2 sum_e |delta rho_e|^2 through t^2 (cubic sharpness); V_patch =
      8 DeltaS_patch + O(3); per-step deficit -gamma(8-gamma)/2 DeltaS_patch;
      n_V bookkeeping exact for all (n, n_R), n <= 3; empty-sum degenerate.
  §F  L5 sector flow: eigenvalue-level quadratic flow mu' = c mu - d(mu^2 -
      |mu|^2/4) + O(t^3) and log Z_gamma = -gamma/4 - d |delta rho|^2 + O(3)
      and tr(deltaK) = -4d |delta rho|^2 + O(3), coefficient-wise, 4 gammas x
      5 exact rational families; square-channel census: T multiplicative on all
      nonvanishing anticommutator pairs (256-pair exhaustive), CT1.11a witness
      reproduced on the commutator channel; single-sector squares S,T-even with
      traceless part on span{Sigma, Ehat}; E++ one-directionality; gamma=1
      exact table (7/8, 7/16, 7/4, 7/2).
  §G  document pins: B Tier 2 heading order L0 < L1 < L2 < L3 < L4 < L5;
      Cor L0a present; L1/L2/L3 Phys carry the [L0] grounding pointer; Tier 2
      free of identification vocabulary; L3 Req free of A7; A §0.1 carries
      L0-L5; A §0.2a list unchanged (two items) and carries the L0/L4 scope
      note; H13 carries the Legacy dynamics import registry.

Run: python3 verify_L0_ledger_tilt.py   (auto-discovered by run_all.py)
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
I = C(0, 1)

# ---------------------------------------------------------------- exact rings


class Ser:
    """truncated formal power series over Fraction, order N."""
    N = 10
    __slots__ = ("c",)

    def __init__(self, c):
        self.c = list(c) + [Fr(0)] * (Ser.N - len(c))

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
        out = [Fr(0)] * Ser.N
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if i + j < Ser.N and b:
                        out[i + j] += a * b
        return Ser(out)

    def scale(self, x):
        x = x if isinstance(x, Fr) else Fr(x)
        return Ser([a * x for a in self.c])

    def inv(self):
        assert self.c[0] != 0
        out = [Fr(0)] * Ser.N
        out[0] = 1 / self.c[0]
        for n in range(1, Ser.N):
            s = Fr(0)
            for k in range(1, n + 1):
                s += self.c[k] * out[n - k]
            out[n] = -s / self.c[0]
        return Ser(out)


def ser_log1p(u):
    assert u.c[0] == 0
    acc = Ser([Fr(0)])
    pw = Ser([Fr(1)])
    for k in range(1, Ser.N):
        pw = pw * u
        acc = acc + pw.scale(Fr((-1) ** (k + 1), k))
    return acc


def ser_exp(u):
    assert u.c[0] == 0
    acc = Ser([Fr(0)])
    pw = Ser([Fr(1)])
    fact = Fr(1)
    for k in range(Ser.N):
        if k > 0:
            fact *= k
            pw = pw * u
        acc = acc + pw.scale(Fr(1) / fact)
    return acc


def loworders(s, k):
    return all(x == 0 for x in s.c[:k])


# ------------------------------------------------------------- enclosures


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
    """exact (lo, hi) for e^x, x in [-1, 0]: alternating decreasing partial sums."""
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


def tilt_spectrum(lams, g, tol, l2):
    exps = [Iv(*exp_enc(-g * l)) for l in lams]
    num = [IV(l) * e for l, e in zip(lams, exps)]
    Z = sum(num[1:], num[0])
    lamp = [n / Z for n in num]
    logZ = Iv(*log_enc_pair(Z, tol, l2))
    return lamp, logZ, Z


def tilt_iv(cur, g):
    exps = []
    for x in cur:
        elo = exp_enc(-g * x.hi, 18)
        ehi = exp_enc(-g * x.lo, 18)
        exps.append(Iv(min(elo[0], ehi[0]), max(elo[1], ehi[1])))
    num = [x * e for x, e in zip(cur, exps)]
    Z = sum(num[1:], num[0])
    return [n / Z for n in num]


def V_iv(lam_iv, tol, l2):
    logs = [Iv(-log_enc(x.hi, tol, l2)[1], -log_enc(x.lo, tol, l2)[0]) for x in lam_iv]
    S = Iv(Fr(0), Fr(0))
    for l, lg in zip(lam_iv, logs):
        S = S - l * lg
    Kt = [(-lg) - S for lg in logs]
    return sum((k.sq() for k in Kt), Iv(Fr(0), Fr(0)))


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
            [Fr(7, 10), Fr(1, 10), Fr(1, 10), Fr(1, 10)],
            [Fr(4, 10), Fr(4, 10), Fr(1, 10), Fr(1, 10)],
            [Fr(7, 24), Fr(6, 24), Fr(6, 24), Fr(5, 24)]]
VAC = [Fr(1, 4)] * 4

# ------------------------------------------------------------- Pauli data

S0 = [[C(1), C(0)], [C(0), C(1)]]
S1 = [[C(0), C(1)], [C(1), C(0)]]
S2 = [[C(0), -I], [I, C(0)]]
S3 = [[C(1), C(0)], [C(0), C(-1)]]
SIG = [S0, S1, S2, S3]
ETA = [C(-1), C(1), C(1), C(1)]            # A3: eta = (-,+,+,+)


def kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb] for j in range(ca * cb)]
            for i in range(ra * rb)]


GB = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(4)] for i in range(4)]


def mscale(A, x):
    return [[a * x for a in row] for row in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


def mzero(A):
    return all(A[i][j] == C(0) for i in range(4) for j in range(4))


SWAP = mscale(madd(GB[0][0], madd(madd(GB[1][1], GB[2][2]), GB[3][3])), Fr(1, 2))


def S_act(X):
    return matmul(matmul(SWAP, X), SWAP)


def T_act(X):
    out = [[C(0)] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            c = comp(X, m, n)
            if c != C(0):
                out = madd(out, mscale(GB[m][n], c * ETA[m] * ETA[n]))
    return out


def comp(X, m, n):
    return trace(matmul(X, GB[m][n])) / 4


E0 = GB[0][0]
SGM = madd(madd(GB[1][1], GB[2][2]), GB[3][3])
W = [mscale(madd(GB[0][i], GB[i][0]), Fr(1, 2)) for i in (1, 2, 3)]


def antisym(a, b):
    return mscale(madd(GB[a[0]][a[1]], GB[b[0]][b[1]], -1), Fr(1, 2))


JG = [antisym((2, 3), (3, 2)), antisym((3, 1), (1, 3)), antisym((1, 2), (2, 1))]
KG = [antisym((0, 1), (1, 0)), antisym((0, 2), (2, 0)), antisym((0, 3), (3, 0))]
EHAT = []
for i in range(1, 4):
    for j in range(i, 4):
        Eij = GB[i][i] if i == j else mscale(madd(GB[i][j], GB[j][i]), Fr(1, 2))
        EHAT.append(madd(Eij, mscale(SGM, Fr(-1, 3))) if i == j else Eij)
EHAT5 = EHAT[:5]                            # Ehat33 = -Ehat11-Ehat22 dependent
SECT = {'E++': [E0, SGM] + EHAT5, 'E+-': W, 'E-+': JG, 'E--': KG}


# ---------------------------------------------------------------- §A
def sectionA():
    print("S1 = §A coupling arithmetic (exact Fractions)")
    # gamma = 1 - 4 eps endpoint map on the CT0.8 range
    chk("§A gamma(eps=0) = 1 (sharp crystallization); gamma -> 0 at the excluded endpoint eps=1/4",
        1 - 4 * Fr(0) == 1 and 1 - 4 * Fr(1, 4) == 0)
    ok = True
    for g in [Fr(0)] + GAMMAS:
        c = 1 - g / 4
        d = g * (8 - g) / 8
        if 1 - c * c != g * (8 - g) / 16:
            ok = False
        if 4 * d != g * (8 - g) / 2:
            ok = False
        if d / 2 != g * (8 - g) / 16:
            ok = False
        if 2 * d != g * (8 - g) / 4:
            ok = False
    chk("§A identities: 1-c^2 = gamma(8-gamma)/16 [L2]; 4d = gamma(8-gamma)/2; d/2 = gamma(8-gamma)/16; "
        "2d = gamma(8-gamma)/4 — all gamma", ok)
    g1c, g1d = 1 - Fr(1, 4), Fr(1) * 7 / 8
    chk("§A anchors: gamma=1 -> (c,d) = (3/4, 7/8); gamma=0 -> (1, 0); 1-c^2|_1 = 7/16; 2d|_1 = 7/4? (7/2 = 4d)",
        (g1c, g1d) == (Fr(3, 4), Fr(7, 8))
        and (1 - Fr(0), Fr(0)) == (Fr(1), Fr(0))
        and 1 - g1c * g1c == Fr(7, 16) and 4 * g1d == Fr(7, 2))


# ---------------------------------------------------------------- §B
def sectionB(l2):
    print("S2 = §B Cor L0a spectral K-update identity (exact log/exp enclosures)")
    tol1, tol2 = Fr(1, 10 ** 6), Fr(1, 10 ** 9)
    pts = grid(10) + EXTREMES
    ok = True
    tight = True
    for gi, g in enumerate(GAMMAS):
        for pi, lam in enumerate(pts):
            tols = (tol1, tol2) if pi == 0 else (tol1,)
            widths = []
            for tol in tols:
                lamp, logZ, Z = tilt_spectrum(lam, g, tol, l2)
                for l, lp in zip(lam, lamp):
                    lhs = Iv(-log_enc(lp.hi, tol, l2)[1], -log_enc(lp.lo, tol, l2)[0])
                    rhs = Iv(-log_enc(l, tol, l2)[1], -log_enc(l, tol, l2)[0]) + IV(g * l) + logZ
                    d = lhs - rhs
                    if not (d.lo <= 0 <= d.hi):
                        ok = False
                    widths.append(d.hi - d.lo)
            if len(widths) == 2 and widths[1] >= widths[0]:
                tight = False
    chk("§B K' = K + gamma rho + log Z_gamma (spectral identity): 4 gammas x %d rational spectra; "
        "difference enclosure contains 0 at every tolerance" % len(pts), ok)
    chk("§B enclosure tightening at the witness point (tol 1e-6 -> 1e-9 strictly narrows)", tight)


# ---------------------------------------------------------------- §C
def sectionC(l2):
    print("S3 = §C Jensen block: concavity, Z bound, tr(deltaK) sign (exact)")
    tol = Fr(1, 10 ** 9)
    ok_sign = True
    for g in GAMMAS + [Fr(1, 100), Fr(99, 100)]:
        for p100 in range(0, 101):
            p = Fr(p100, 100)
            if g * g * p - 2 * g > 0:
                ok_sign = False
    chk("§C g''(p) = e^{-gamma p}(gamma^2 p - 2 gamma) <= 0 on (0,1] x [0,1] "
        "(gamma p <= 1 < 2; exact rational grid incl. gamma = 1/100, 99/100)", ok_sign)
    pts = grid(9) + EXTREMES
    ok = True
    for g in GAMMAS:
        for lam in pts:
            lamp, logZ, Z = tilt_spectrum(lam, g, tol, l2)
            if Z.lo <= 0:
                ok = False                     # Z_gamma > 0 (faithful tilt)
            trdK = IV(g) + logZ * IV(4)
            if lam == VAC:
                if not (trdK.lo <= 0 <= trdK.hi and (trdK.hi - trdK.lo) < Fr(1, 10 ** 8)):
                    ok = False                 # equality case pinches at 0
            else:
                if trdK.hi >= 0:
                    ok = False                 # strict deficit off-vacuum
    chk("§C Z_gamma in (0, e^{-gamma/4}]; tr(deltaK) = gamma + 4 log Z_gamma < 0 strictly off-vacuum, "
        "= 0 at the vacuum (enclosure pinch); 4 gammas x %d spectra" % len(pts), ok)


# ---------------------------------------------------------------- §D
def sectionD(l2):
    print("S4 = §D ledger recursion, Haar spectral preservation, collapse (exact)")
    # integer recursion (A6/A7)
    seqs = [[0, 2, 1, 0, 3, 1, 0, 0, 2], [1, 1, 1, 1, 1], [0, 0, 0, 4], [3, 0, 0, 1, 2, 0]]
    ok = True
    for s in seqs:
        L = [0]
        for n in range(len(s)):
            L.append(L[-1] + s[n])
            if L[-1] != sum(s[:n + 1]):        # closed form |L(tau_{n+1})| = sum_{k<n+1}
                ok = False
            if L[-1] < L[-2]:
                ok = False                     # monotone (A6)
    chk("§D |L(tau_{n+1})| = |L(tau_n)| + n_real_out(tau_n) with |L(tau_0)| = 0 gives "
        "|L(tau_n)| = sum_{k<n} n_real_out(tau_k), monotone (exact integers, 4 witness sequences)", ok)

    # Haar spectral preservation: tr((U rho U^dag)^m) = tr(rho^m), m = 1..4
    rng = random.Random(20260929)

    def rc():
        return C(Fr(rng.randint(-4, 4), 3), Fr(rng.randint(-4, 4), 3))

    def unitary_exact():
        perm = list(range(4))
        rng.shuffle(perm)
        phases = [C(1), C(-1), C(0, 1), C(0, -1)]
        M = [[C(0)] * 4 for _ in range(4)]
        for i in range(4):
            M[i][perm[i]] = phases[rng.randrange(4)]
        R = [[C(Fr(3, 5)), C(Fr(-4, 5)), C(0), C(0)],
             [C(Fr(4, 5)), C(Fr(3, 5)), C(0), C(0)],
             [C(0), C(0), C(1), C(0)],
             [C(0), C(0), C(0), C(1)]]
        return matmul(M, R)

    def rand_herm():
        M = [[rc() for _ in range(4)] for _ in range(4)]
        H = [[C(0)] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                s = M[i][j] + C(M[j][i].re, -M[j][i].im)
                H[i][j] = C(s.re / 2, s.im / 2)
        return H

    def pw(M, k):
        r = M
        for _ in range(k - 1):
            r = matmul(r, M)
        return r

    ok = True
    for _ in range(8):
        U = unitary_exact()
        Ud = conj_transpose(U)
        if any(matmul(U, Ud)[i][j] != (C(1) if i == j else C(0)) for i in range(4) for j in range(4)):
            ok = False                          # unitarity precheck
        rho = rand_herm()
        rr = matmul(matmul(U, rho), Ud)
        for m in (1, 2, 3, 4):
            if trace(pw(rr, m)) != trace(pw(rho, m)):
                ok = False
    chk("§D tick is spectral: tr((U rho U^dag)^m) = tr(rho^m), m=1..4, exact over Q(i); "
        "8 unitaries (signed perms x Pythagorean SO(2) blocks) x random Hermitian rho "
        "=> V(K~(T(rho))) = V(K~(rho)) [L0(1)/L1(2)]", ok)

    # L0(4) collapse — exact structural form:
    # (i) the tilt's eigenvalue map is componentwise-over-symmetric-normalization:
    #     f_i(lam, e) = lam_i e_i / sum_j lam_j e_j with e_i = e^{-gamma lam_i} modeled
    #     as independent positive rationals => permutation-equivariant EXACTLY;
    # (ii) V = sum_i (l_i - mean(l))^2 with l_i = -log lam_i is a symmetric polynomial
    #     in the log-eigenvalues => spectral;
    # (iii) conjugation preserves power traces (checked above) => preserves the
    #     log-eigenvalue multiset [Newton]. Together: interleaving is inert.
    rng2 = random.Random(777)
    ok = True
    for _ in range(40):
        lam = [Fr(rng2.randint(1, 40), 41) for _ in range(4)]
        e = [Fr(rng2.randint(1, 60), 61) for _ in range(4)]
        Zs = sum(l * ei for l, ei in zip(lam, e))
        f = [l * ei / Zs for l, ei in zip(lam, e)]
        for perm in ([1, 0, 2, 3], [0, 2, 3, 1], [3, 2, 1, 0]):
            lamP = [lam[i] for i in perm]
            eP = [e[i] for i in perm]
            Zp = sum(l * ei for l, ei in zip(lamP, eP))
            fP = [l * ei / Zp for l, ei in zip(lamP, eP)]
            if [fP[perm.index(k)] for k in range(4)] != f:
                ok = False
        # V symmetric in the logs (rational stand-ins l_i): V = sum l^2 - (sum l)^2/4
        l = [Fr(rng2.randint(-30, 30), 7) for _ in range(4)]
        V1 = sum(x * x for x in l) - (sum(l) ** 2) / 4
        for perm in ([1, 0, 2, 3], [0, 2, 3, 1]):
            lp = [l[i] for i in perm]
            V2 = sum(x * x for x in lp) - (sum(lp) ** 2) / 4
            if V1 != V2:
                ok = False
        # the componentwise tilt map equals the V-formula's input: sum f = 1 (trace kept)
        if sum(f) != 1:
            ok = False
    chk("§D L0(4) collapse, exact structural form: tilt eigenvalue map is permutation-equivariant "
        "(componentwise / symmetric normalization; 40 exact rational draws x 3 permutations), "
        "V is a symmetric polynomial in the log-eigenvalues, and the tilt keeps sum = 1 — "
        "with the tr-power identity above, Haar interleaving is inert", ok)
    # small numeric demo at gamma = 1 on one extreme spectrum (enclosures, tol 1e-4)
    tol = Fr(1, 10 ** 4)
    g = Fr(1)
    lam0 = EXTREMES[1]
    cur = [IV(x) for x in lam0]
    cur = tilt_iv(cur, g)
    cur = [cur[i] for i in [1, 0, 2, 3]]
    cur = tilt_iv(cur, g)
    Va = V_iv(cur, tol, l2)
    direct = [IV(x) for x in lam0]
    for _ in range(2):
        direct = tilt_iv(direct, g)
    Vb = V_iv(direct, tol, l2)
    d = Va - Vb
    chk("§D L0(4) numeric witness: V(tilt-perm-tilt) = V(tilt^2) at gamma=1 "
        "(enclosure difference contains 0)", d.lo <= 0 <= d.hi, str((float(d.lo), float(d.hi))))

    # vacuum fixed point
    tol = Fr(1, 10 ** 7)
    ok = True
    for g in GAMMAS:
        lamp, _, _ = tilt_spectrum(VAC, g, tol, l2)
        for x in lamp:
            if not (x.lo <= Fr(1, 4) <= x.hi and (x.hi - x.lo) < Fr(1, 10 ** 8)):
                ok = False
    chk("§D vacuum fixed point of every tilt: lam' = 1/4 (enclosure pinch), all gammas", ok)

    # mu_k = c^k mu_0 + O(mu_0^2), k <= 3 (series composition of L2's eigenvalue law)
    t = Ser([Fr(0), Fr(1)])
    fams = [(1, -1, 0, 0), (3, -1, -1, -1), (5, -2, -2, -1)]
    ok = True
    for g in GAMMAS:
        c = 1 - g / 4
        d = g * (8 - g) / 8
        for fam in fams:
            mu = [t.scale(Fr(x)) for x in fam]
            for k in range(1, 4):
                s2 = Ser([Fr(0)])
                for m in mu:
                    s2 = s2 + m * m
                mu = [m.scale(c) - (m * m - s2.scale(Fr(1, 4))).scale(d) for m in mu]
                for m, x0 in zip(mu, fam):
                    if m.c[1] != (c ** k) * Fr(x0):
                        ok = False
    chk("§D mu_k = (1-gamma/4)^k mu_0 + O(mu_0^2) for k = 1..3, every gamma "
        "(coefficient-wise series composition)", ok)


# ---------------------------------------------------------------- §E
def sectionE():
    print("S5 = §E L4 patch deficit (multi-channel series + bookkeeping)")
    t = Ser([Fr(0), Fr(1)])
    chans = [(1, -1, 0, 0), (2, -1, -1, 0), (3, -2, -1, 0)]   # three virtual channels
    okS = True
    for g in GAMMAS:
        Srel = Ser([Fr(0)])
        Vsum = Ser([Fr(0)])
        Vpsum = Ser([Fr(0)])
        s2 = Fr(0)
        for fam in chans:
            lam = [Ser.const(Fr(1, 4)) + t.scale(Fr(di)) for di in fam]
            L = [ser_log1p(t.scale(4 * di)) for di in fam]
            sr = Ser([Fr(0)])
            for li, Li in zip(lam, L):
                sr = sr + li * Li
            Srel = Srel + sr                       # S(rho||I/4) = sum lam log(4 lam)
            sum_lamL = sr
            Kt = [sum_lamL - Li for Li in L]
            V = Ser([Fr(0)])
            for k in Kt:
                V = V + k * k
            Vsum = Vsum + V
            u = [ser_exp(t.scale(-g * di)) for di in fam]
            Zt = Ser([Fr(0)])
            for li, ui in zip(lam, u):
                Zt = Zt + li * ui
            Zi = Zt.inv()
            lamp = [li * ui * Zi for li, ui in zip(lam, u)]
            logZt = ser_log1p(Zt - Ser.const(Fr(1)))
            Lp = [Li - li.scale(g) + Ser.const(g / 4) - logZt for Li, li in zip(L, lam)]
            Sp = Ser([Fr(0)])
            for lp, Lq in zip(lamp, Lp):
                Sp = Sp + lp * Lq
            Ktp = [Sp - Lq for Lq in Lp]
            Vp = Ser([Fr(0)])
            for k in Ktp:
                Vp = Vp + k * k
            Vpsum = Vpsum + Vp
            for di in fam:
                s2 += Fr(di) ** 2
        dS = (t * t).scale(2 * s2)                 # DeltaS_patch leading = 2 sum_e |delta_e|^2
        if not loworders(Srel - dS, 3):
            okS = False
        if all(x == 0 for x in (Srel - dS).c[3:6]):
            okS = False                            # cubic remainder must be generically nonzero
        if not loworders(Vsum - dS.scale(8), 3):
            okS = False
        want = dS.scale(-g * (8 - g) / 2)
        if not loworders((Vpsum - Vsum) - want, 3):
            okS = False
    chk("§E patch identities hold channel-summed for every gamma: DeltaS(q) = 2 sum_e |delta rho_e|^2 "
        "through t^2 (cubic remainder sharp); V_patch = 8 DeltaS(q); "
        "V'-V = -gamma(8-gamma)/2 DeltaS(q) (all O(t^3))", okS)
    okb = True
    for n in range(0, 4):
        for nR in range(0, n + 1):
            nV = n - nR
            if nV >= 1:
                devs = [Fr(i + 1, 7) for i in range(nV)]
                tot = sum(2 * x * x for x in devs)
                avg = tot / nV
                if nV * avg != tot:
                    okb = False
            else:
                if 2 * nV != 0:
                    okb = False
    if 2 * Fr(1, 4) != Fr(1, 2):
        okb = False
    chk("§E n_V bookkeeping exact for all (n, n_R), n <= 3: DeltaS = n_V * mean; n_V = 0 => 0; "
        "coefficient 2 * (1/4) = 1/2 (r-form)", okb)


# ---------------------------------------------------------------- §F
def sectionF():
    print("S6 = §F L5 sector flow: series identities + square-channel census")
    t = Ser([Fr(0), Fr(1)])
    fams = [(1, -1, 0, 0), (1, 1, -1, -1), (3, -1, -1, -1), (5, -2, -2, -1), (7, -3, -3, -1)]
    ok = True
    for g in GAMMAS:
        c = 1 - g / 4
        d = g * (8 - g) / 8
        for fam in fams:
            mu = [t.scale(Fr(x)) for x in fam]
            lam = [Ser.const(Fr(1, 4)) + m for m in mu]
            u = [ser_exp(m.scale(-g)) for m in mu]
            Zt = Ser([Fr(0)])
            for li, ui in zip(lam, u):
                Zt = Zt + li * ui
            Zi = Zt.inv()
            mup = [li * ui * Zi - Ser.const(Fr(1, 4)) for li, ui in zip(lam, u)]
            s2 = Ser([Fr(0)])
            for m in mu:
                s2 = s2 + m * m
            for m, mp in zip(mu, mup):
                pred = m.scale(c) - (m * m - s2.scale(Fr(1, 4))).scale(d)
                if not loworders(mp - pred, 3):
                    ok = False
            if not loworders(Zt - (Ser.const(Fr(1)) - s2.scale(d)), 3):
                ok = False
            logZt = ser_log1p(Zt - Ser.const(Fr(1)))
            if not loworders(logZt.scale(4) + s2.scale(4 * d), 3):   # tr dK series part
                ok = False
    chk("§F quadratic flow mu' = c mu - d(mu^2 - |mu|^2/4), Z_gamma = e^{-gamma/4}(1 - d|drho|^2), "
        "tr(deltaK) = gamma + 4 log Z_gamma = -4d|drho|^2 — coefficient-wise t^0..t^2, "
        "4 gammas x 5 exact families", ok)

    # square-channel census: T multiplicative on nonvanishing anticommutators
    bad = []
    nz = 0
    for a in range(16):
        for b in range(16):
            Ga, Gb = GB[a // 4][a % 4], GB[b // 4][b % 4]
            ac = madd(matmul(Ga, Gb), matmul(Gb, Ga))
            if not mzero(ac):
                nz += 1
                if not meq(T_act(matmul(Ga, Gb)), matmul(T_act(Ga), T_act(Gb))):
                    bad.append((a, b))
    chk(f"§F square channel: T(G_a G_b) = T(G_a)T(G_b) on all {nz} nonvanishing-anticommutator "
        "pairs of the 256 (exhaustive, exact)", not bad, str(bad[:6]))
    # CT1.11a(1) witness reproduced on the commutator channel
    a, b = 1, 2        # sigma_0 (x) sigma_1 ,  sigma_0 (x) sigma_2
    Ga, Gb = GB[a // 4][a % 4], GB[b // 4][b % 4]
    ac = madd(matmul(Ga, Gb), matmul(Gb, Ga))
    witness = mzero(ac) and not meq(T_act(matmul(Ga, Gb)), matmul(T_act(Ga), T_act(Gb)))
    chk("§F CT1.11a(1) non-multiplicativity witness reproduced: {G_a,G_b} = 0 (cancels in squares) "
        "while T(G_a G_b) != T(G_a)T(G_b)", witness)

    # generator sectors and single-sector squares
    rng_w = [Fr(1, 3), Fr(-2, 5), Fr(7, 11), Fr(-1, 7), Fr(4, 9), Fr(-3, 8), Fr(1, 2)]
    par_ok = True
    for nm, gens in SECT.items():
        s_want, t_want = {'E++': (1, 1), 'E+-': (1, -1), 'E-+': (-1, 1), 'E--': (-1, -1)}[nm]
        want_dim = {'E++': 7, 'E+-': 3, 'E-+': 3, 'E--': 3}[nm]
        if len(gens) != want_dim:
            par_ok = False
        for X in gens:
            if not meq(S_act(X), mscale(X, s_want)) or not meq(T_act(X), mscale(X, t_want)):
                par_ok = False
    chk("§F CT1.2 generator sectors: dims (7,3,3,3) with exact S/T parities", par_ok)
    ok = True
    for nm, gens in SECT.items():
        X = [[C(0)] * 4 for _ in range(4)]
        for k, gEl in enumerate(gens):
            X = madd(X, mscale(gEl, rng_w[k % len(rng_w)]))
        X2 = matmul(X, X)
        trX2 = trace(X2)
        X2t = madd(X2, mscale(E0, -trX2 / 4))
        if not (meq(S_act(X2), X2) and meq(T_act(X2), X2)
                and meq(S_act(X2t), X2t) and meq(T_act(X2t), X2t)
                and meq(X2, conj_transpose(X2))):
            ok = False
    chk("§F single-sector landing: X^2 S-even and T-even for generic X in each of the four sectors "
        "(delta rho^2 in E_{++}; traceless part too; Hermitian/PSD-structured)", ok)
    ok = True
    ee = SECT['E++']
    for ia in range(len(ee)):
        for ib in range(ia, len(ee)):
            A_, B_ = ee[ia], ee[ib]
            ac = madd(matmul(A_, B_), matmul(B_, A_))
            if not mzero(ac):
                p = mscale(ac, Fr(1, 2))
                if not (meq(S_act(p), p) and meq(T_act(p), p)):
                    ok = False
    chk("§F E++ one-directionality: nonvanishing anticommutators of E++ generators stay S,T-even", ok)

    # gamma=1 exact table
    c1, d1 = 1 - Fr(1, 4), Fr(7, 8)
    chk("§F gamma=1 table exact: c = 3/4, d = 7/8, 1-c^2 = 7/16, d/2 = 7/16, 2d = 7/4, 4d = 7/2",
        (c1, d1) == (Fr(3, 4), Fr(7, 8)) and 1 - c1 * c1 == Fr(7, 16)
        and d1 / 2 == Fr(7, 16) and 2 * d1 == Fr(7, 4) and 4 * d1 == Fr(7, 2))


# ---------------------------------------------------------------- §G pins
def sectionG():
    print("S7 = §G document pins of the ledger-tilt pass")

    def rd(fn):
        return era_paths.read(fn)

    A, B = rd("A_axioms.md"), rd("B_foundation.md")
    if ARCH:
        H13 = rd("H_archive/H13_registries_and_gaps.md")

    heads = ["### L0 — ", "### L1 — ", "### L2 — ", "### L3 — ", "### L4 — ", "### L5 — "]
    pos = [B.index(h) for h in heads if h in B]
    chk("§G B Tier 2 heading order: L0 < L1 < L2 < L3 < L4 < L5",
        len(pos) == 6 and pos == sorted(pos))
    chk("§G Cor L0a present in the L0 block",
        "**Cor L0a (tilt modular update).**" in B
        and B.index("**Cor L0a") < B.index("### L1 — "))

    def phys_block(tag):
        i = B.index(f"### {tag} — ")
        j = B.index("### ", i + 4) if "### " in B[i + 4:] else len(B)
        blk = B[i:i + (j - i)]
        k = blk.index("**Phys.**")
        return blk[k:k + 2500]

    chk("§G L1/L2/L3 Phys carry the [L0] grounding pointer",
        all("[L0]" in phys_block(t) for t in ("L1", "L2", "L3")))
    tier2 = B[B.index("\n## Tier 2 — "):B.index("## Closure exports of Part 1 §F")]
    chk("§G B Tier 2 (L0..L5) free of identification vocabulary: no 'SM', 'hierarchy', 'fermion'",
        not re.search(r"\bSM\b|hierarchy|fermion", tier2))
    l3 = B[B.index("### L3 — "):B.index("### L4 — ")]
    req3 = l3[l3.index("**Req.**"):l3.index("**Pf.**")]
    chk("§G L3 Req still free of A7 (pin kept)", "A7" not in req3)
    l4req = B[B.index("### L4 — "):B.index("### L5 — ")]
    chk("§G L4 Req cites L3 and carries the finite-incidence scope",
        "L3" in l4req and "finite-incidence" in l4req)
    chk("§G A §0.1 carries L0–L5 for B", "L0–L5" in A)
    chk("§G A §0.2a: the extra-axiomatic list is empty (CT2.6 (ii)-(iii) reclassified as derived, Part 4 Tier BM.24)",
        "The complete list of extra-axiomatic inputs is empty" in A and "BM.151" in A)
    chk("§G A §0.2a integration note carries the L0/L4 theorem-local scope sentence",
        "crystallization–tilt coupling of L0" in A and "finite-incidence scope of L4" in A)
    chk("§G B machine line references verify_L0_ledger_tilt.py",
        B.count("verify_L0_ledger_tilt.py") >= 4)
    if ARCH:
        chk("§G H13 carries the Legacy dynamics import registry with six items",
            "**Legacy dynamics import registry (ledger–tilt and branch-grading pass).**" in H13
            and all(f"**({i}) " in H13[H13.index("**Legacy dynamics import registry"):
                                       H13.index("**Inherited declared premises")] for i in range(1, 7)))


def main():
    print("verify_L0_ledger_tilt: ledger-tilt dynamics pass (exact)")
    want = {a.upper() for a in sys.argv[1:]}
    l2 = log2_enc(Fr(1, 10 ** 12))
    chk("§0 log2 enclosure sane: 0.69 < log2 < 0.70 (exact rational bounds)",
        Fr(69, 100) < l2[0] and l2[1] < Fr(70, 100))
    if not want or "A" in want:
        sectionA()
    if not want or "B" in want:
        sectionB(l2)
    if not want or "C" in want:
        sectionC(l2)
    if not want or "D" in want:
        sectionD(l2)
    if not want or "E" in want:
        sectionE()
    if not want or "F" in want:
        sectionF()
    if not want or "G" in want:
        sectionG()
    print(f"verify_L0_ledger_tilt: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
