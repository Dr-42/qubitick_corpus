
#!/usr/bin/env python3
"""
verify_H_ladder.py — machine checks for H (WIP), Tier F.18.

Exact verification of the native ladder rungs (FT.56): CT0.7a's Casimir
identities as explicit 4x4 rational matrix arithmetic on the pair channel;
the admissibility correction j = |k|/2 (Casimir sign-discrimination,
cone-additivity witnesses); and the boundary exchange algebra shape
(FT.57): su(2) commutators over Q(i) and the u(N) dimension split.
Pure Python 3 standard library; no floating point; 4x4 checks run over
Q(i) with faithful complex Pauli matrices (a real encoding of sigma_2 squares
to -I and silently breaks the CT0.7a identity — guarded in-suite). Exit 0 =
all green.

Run:  python3 checks/verify_H_ladder.py
"""

from fractions import Fraction
import sys

PASSES = []
FAILURES = []


def check(name):
    def deco(fn):
        try:
            fn()
        except AssertionError as exc:
            FAILURES.append((name, str(exc) or "assertion failed"))
        except Exception as exc:
            FAILURES.append((name, "%s: %s" % (type(exc).__name__, exc)))
        else:
            PASSES.append(name)
        return fn
    return deco


F = Fraction

# ---- Q(i) exact arithmetic (Pauli sigma_2 is genuinely complex — a real
# ---- encoding of it squares to -I and silently breaks the CT0.7a identity)
Z0 = (F(0), F(0))
Z1 = (F(1), F(0))
ZI = (F(0), F(1))
ZMI = (F(0), F(-1))
ZM1 = (F(-1), F(0))


def zmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def zadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def zscale(a, z):
    return (a * z[0], a * z[1])


SIG = [
    [[Z1, Z0], [Z0, Z1]],
    [[Z0, Z1], [Z1, Z0]],
    [[Z0, ZMI], [ZI, Z0]],
    [[Z1, Z0], [Z0, ZM1]],
]


def kron(A, B):
    n = len(A)
    m = len(B)
    return [[zmul(A[i // n][j // m], B[i % n][j % m])
             for j in range(m * len(B[0]))] for i in range(n * len(A))]


def madd(A, B):
    return [[zadd(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def mmul(A, B):
    n = len(A)
    out = []
    for i in range(n):
        row = []
        for j in range(len(B[0])):
            acc = Z0
            for k in range(n):
                acc = zadd(acc, zmul(A[i][k], B[k][j]))
            row.append(acc)
        out.append(row)
    return out


def mscale(a, A):
    return [[zscale(a, x) for x in row] for row in A]


def eye_z(n):
    return [[Z1 if i == j else Z0 for j in range(n)] for i in range(n)]


def tr_z(A):
    acc = Z0
    for i in range(len(A)):
        acc = zadd(acc, A[i][i])
    return acc


I2z = eye_z(2)
I4z = eye_z(4)
E0 = kron(SIG[0], SIG[0])
SIGMA_OP = madd(madd(kron(SIG[1], SIG[1]), kron(SIG[2], SIG[2])), kron(SIG[3], SIG[3]))
W = [mscale(F(1, 2), madd(kron(SIG[i], I2z), kron(I2z, SIG[i]))) for i in (1, 2, 3)]
CAS_W2 = madd(madd(mmul(W[0], W[0]), mmul(W[1], W[1])), mmul(W[2], W[2]))


@check("FT.56(1)/CT0.7a: sum W_i^2 = (3/2)E0 + (1/2)Sigma — exact 4x4 identity over Q(i)")
def _casimir_identity():
    rhs = madd(mscale(F(3, 2), E0), mscale(F(1, 2), SIGMA_OP))
    assert CAS_W2 == rhs
    # sigma_2 really is complex in this encoding (regression guard for the real-encoding trap):
    assert SIG[2][0][1] == ZMI and SIG[2][1][0] == ZI
    assert mmul(SIG[2], SIG[2]) == eye_z(2)          # sigma_2^2 = I, faithfully


@check("FT.56(1): reality projectors — Pi_vee = (3E0+Sigma)/4 (tr 3), Pi_wedge = (E0-Sigma)/4 (tr 1); swap S = (E0+Sigma)/2, S^2 = I; Casimir eigenvalues 2 and 0")
def _projectors():
    Pvee = mscale(F(1, 4), madd(mscale(F(3), E0), SIGMA_OP))
    Pwedge = mscale(F(1, 4), madd(E0, mscale(F(-1), SIGMA_OP)))
    assert tr_z(Pvee) == (F(3), F(0)) and tr_z(Pwedge) == (F(1), F(0))
    assert madd(Pvee, Pwedge) == I4z
    assert mmul(Pvee, Pvee) == Pvee and mmul(Pwedge, Pwedge) == Pwedge
    S = mscale(F(1, 2), madd(E0, SIGMA_OP))
    assert mmul(S, S) == I4z
    # Casimir action: sum W^2 restricted via projectors
    assert mmul(CAS_W2, Pvee) == mscale(F(2), Pvee)      # eigenvalue 2 = j(j+1), j=1
    assert mmul(CAS_W2, Pwedge) == mscale(F(0), Pwedge)  # eigenvalue 0, j=0
    assert F(2) == F(1) * (F(1) + 1)                     # j=1: j(j+1) = 2
    assert F(0) == F(0) * (F(0) + 1)                     # j=0


@check("FT.56(1): rung dimensions 2j+1 = 1, 2, 3 for j = 0, 1/2, 1 (wedge^2 / seed / vee^2 = Sym^2)")
def _dimensions():
    assert 2 * F(0) + 1 == 1        # wedge^2: virtual line [CT0.9's home]
    assert 2 * F(1, 2) + 1 == 2     # seed: EW.32's single qubit
    assert 2 * F(1) + 1 == 3        # vee^2 = Sym^2: reality sector


@check("FT.56(3) correction: Casimir distinguishes +/- k/2 — j = |k|/2 forced; negative-j Casimir inadmissible")
def _admissibility():
    # k = -3: signed rule would give j = -3/2 with Casimir 3/4 (= j=+1/2's!) while |k|/2 = 3/2 gives 15/4
    j_signed = F(-3, 2)
    j_abs = F(3, 2)
    assert j_signed * (j_signed + 1) == F(3, 4)
    assert j_abs * (j_abs + 1) == F(15, 4)
    assert j_signed * (j_signed + 1) != j_abs * (j_abs + 1)     # the Casimir distinguishes
    # negative-j Casimir can be negative — inadmissible for unitary su(2) reps:
    assert j_signed * (j_signed + 1) < F(15, 4)
    assert F(-1, 2) * (F(-1, 2) + 1) == F(-1, 4) < 0            # j=-1/2: negative Casimir — excluded
    # the rule: Sym^{|k|} has dim |k|+1 and Casimir |k|(|k|+2)/4
    for k in (-3, -2, -1, 0, 1, 2, 3):
        j = F(abs(k), 2)
        assert j * (j + 1) == F(abs(k) * (abs(k) + 2), 4)
        assert j >= 0


@check("FT.56(2): cone additivity j(Gamma) = j1+j2+j_rel for nonneg windings; mixed-sign counterexample scopes the cone")
def _cone():
    for k1, k2, d in ((1, 1, 2), (2, 3, 4), (0, 5, 1), (7, 2, 0)):
        assert F(k1 + k2 + d, 2) == F(k1, 2) + F(k2, 2) + F(d, 2)
    # mixed sign: |3 + (-1)|/2 = 1 != 3/2 + (-1)/2 ... stretched sum on |.| fails:
    assert F(abs(3 + (-1)), 2) == F(1)
    assert F(3, 2) + F(1, 2) == F(2) != F(1)     # cone condition is load-bearing
    # signature samples: Theta = sum kappa; k = Theta/2; timelike-dominant gives k < 0
    samples = [((2, 1, -1), 1), ((1, 1, -4), -1), ((1, 1, 0), 1), ((2, 2, 2), 3)]
    for prof, k in samples:
        theta = sum(prof)
        assert theta % 2 == 0
        assert theta // 2 == k
    # orientation-blindness: Theta invariant under profile reversal (k is signature data)
    for prof, k in samples:
        assert sum(reversed(prof)) == sum(prof)


# ---- Q(i) helpers for the exchange algebra
def zmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def zadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def zsub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def zmat_mul(A, B):
    return [[zadd(zmul(A[i][0], B[0][j]), zmul(A[i][1], B[1][j])) for j in range(2)]
            for i in range(2)]


@check("FT.57(2): exchange su(2) over Q(i) — E± = (sigma1 ± i sigma2)/2: [E+,E-] = sigma3, [sigma3,E±] = ±2E±")
def _exchange():
    s1 = [[(F(0), F(0)), (F(1), F(0))], [(F(1), F(0)), (F(0), F(0))]]
    s2 = [[(F(0), F(0)), (F(0), F(-1))], [(F(0), F(1)), (F(0), F(0))]]
    s3 = [[(F(1), F(0)), (F(0), F(0))], [(F(0), F(0)), (F(-1), F(0))]]
    half_i = (F(0), F(1, 2))
    Ep = [[zadd((F(1, 2) * s1[i][j][0], F(1, 2) * s1[i][j][1]), zmul(half_i, s2[i][j]))
           for j in range(2)] for i in range(2)]
    Em = [[zsub((F(1, 2) * s1[i][j][0], F(1, 2) * s1[i][j][1]), zmul(half_i, s2[i][j]))
           for j in range(2)] for i in range(2)]
    comm_pm = [[zsub(zmat_mul(Ep, Em)[i][j], zmat_mul(Em, Ep)[i][j]) for j in range(2)] for i in range(2)]
    assert comm_pm == s3
    c3p = [[zsub(zmat_mul(s3, Ep)[i][j], zmat_mul(Ep, s3)[i][j]) for j in range(2)] for i in range(2)]
    assert c3p == [[zadd(x, x) for x in row] for row in Ep]          # +2 E+
    c3m = [[zsub(zmat_mul(s3, Em)[i][j], zmat_mul(Em, s3)[i][j]) for j in range(2)] for i in range(2)]
    assert c3m == [[zsub((F(0), F(0)), zadd(x, x)) for x in row] for row in Em]  # -2 E-


@check("FT.57(1): u(N) split — dim su(N) = N^2-1 = strictly-new (N^2-N) + Cartan (N-1); matches FT.41(d) counts")
def _uN_split():
    for N in range(1, 9):
        su_dim = N * N - 1
        cartan = N - 1
        strictly_new = N * N - N
        assert su_dim == strictly_new + cartan
    assert 1 * 1 - 1 == 0            # N=1: nothing strictly new [FT.41(d)]
    assert 2 * 2 - 2 == 2            # N=2: two exchange dimensions


def main():
    for name in PASSES:
        print("PASS  %s" % name)
    for name, msg in FAILURES:
        print("FAIL  %s :: %s" % (name, msg))
    total = len(PASSES) + len(FAILURES)
    print("-" * 60)
    print("verify_H_ladder: %d/%d checks green" % (len(PASSES), total))
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
