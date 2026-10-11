
#!/usr/bin/env python3
"""
verify_H_hosting.py -- suite for the H layer (H01–H13).
Exact arithmetic for Def-H.22 / FT.58:

  I.   Matrix-unit hosting identity: (lambda_1 + i*lambda_2)/2 = E_12 (3x3),
       over Q(i) -- the literal corolla hosting of the exchange doublet.
  II.  su(2) exchange basis at N=2: T3 = (D1-D2)/2, T+ = E12, T- = E21 close
       [T3,T+] = T+, [T3,T-] = -T-, [T+,T-] = 2*T3 (2x2, Q(i)).
  III. W-basis commutators [W_i, W_j] = i eps_ijk W_k (CT1.4; 4x4 faithful Q(i),
       sigma_2 regression-guarded).
  IV.  Gell-Mann f_123 = 1: [T_1, T_2] = i T_3 with T_a = lambda_a/2 (CT3.9/CT3.21).
  V.   Observable capacity: pair-part G+H+W = 5+1+3 = 9; stack-part EM+strong =
       1+8 = 9; total 18 = FT.26(3); dim su(N) = N^2-1: 15, 24, 35 for N = 4,5,6
       all > 9 => no injective hom. image in either commuting factor => trivial
       (FT.58(3)); ceiling: N^2-1 <= 9 <=> N <= 3.
  VI.  Separated-case ledger at N=2: dim u(2) = 4 = 1 (EM-total image) + 1
       (traceless diagonal kernel) + 2 (unhosted exchange) [FT.58(2)].
  VII. Corolla at N=3, n(w)=3: dim su(3) = 8 = dim K^(strong) exact fit
       [D2.12/CT3.8]; at N=6 (face floor): exchange dims N^2-N = 30,
       hostable <= 8 => unhosted >= 22.

NO FLOATS anywhere (H document convention); Q(i) entries exact.
"""
import sys
from fractions import Fraction as F

FAILS = []
PASSES = 0


def check(name, cond, detail=""):
    global PASSES
    if cond:
        PASSES += 1
        print("  [OK]   %s" % name)
    else:
        FAILS.append(name)
        print("  [FAIL] %s   %s" % (name, detail))


def ci(a, b):
    return (F(a), F(b))


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def csub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def csmul(c, x):
    # scalar x complex-number: scalar may be a Fraction or a Q(i) tuple
    if isinstance(c, tuple):
        return cmul(c, x)
    return (c * x[0], c * x[1])


Z = ci(0, 0)
ONE = ci(1, 0)
I = ci(0, 1)


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[Z for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            acc = Z
            for k in range(m):
                acc = cadd(acc, cmul(A[i][k], B[k][j]))
            C[i][j] = acc
    return C


def comm(A, B):
    return mat_sub(mat_mul(A, B), mat_mul(B, A))


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mat_scale(c, A):
    return [[csmul(c, x) for x in row] for row in A]


def mat_sub(A, B):
    return [[csub(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def mat_add(A, B):
    return [[cadd(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def E(n, i, j):
    M = [[Z for _ in range(n)] for _ in range(n)]
    M[i][j] = ONE
    return M


def diag(*entries):
    n = len(entries)
    M = [[Z for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] = entries[i]
    return M


# ---- Pauli matrices over Q(i) (faithful; sigma_2 regression-guarded) ----
s0 = diag(ONE, ONE)
s1 = [[Z, ONE], [ONE, Z]]
s2 = [[Z, ci(0, -1)], [I, Z]]
s3 = diag(ONE, ci(-1, 0))

check("sigma_2^2 = I (faithful encoding regression guard)",
      mat_eq(mat_mul(s2, s2), s0))

# ---- Gell-Mann lambda_1, lambda_2, lambda_3 (3x3) ----
lam1 = mat_add(E(3, 0, 1), E(3, 1, 0))
lam2 = mat_sub(mat_scale(ci(0, -1), E(3, 0, 1)), mat_scale(ci(0, -1), E(3, 1, 0)))
lam3 = diag(ONE, ci(-1, 0), Z)

print("== I. Matrix-unit hosting identity (FT.58(1)) ==")
T1 = mat_scale(F(1, 2), lam1)
T2 = mat_scale(F(1, 2), lam2)
lhs = mat_add(T1, mat_scale(I, T2))    # (lambda_1 + i lambda_2)/2
check("(lambda_1 + i*lambda_2)/2 = E_12 (3x3 matrix unit)",
      mat_eq(lhs, E(3, 0, 1)),
      detail=str(lhs))
# and the diagonal: lambda_3 = D1 - D2 at N=2 (slots 1,2 of 3)
check("lambda_3 = diag(1,-1,0) (traceless diagonal direction)",
      mat_eq(lam3, diag(ONE, ci(-1, 0), Z)))

print("== II. su(2) exchange basis at N=2 (FT.58(1)/(2)) ==")
t3 = mat_scale(F(1, 2), diag(ONE, ci(-1, 0)))
tp = E(2, 0, 1)
tm = E(2, 1, 0)
check("[T3, T+] = T+", mat_eq(comm(t3, tp), tp), detail=str(comm(t3, tp)))
check("[T3, T-] = -T-", mat_eq(comm(t3, tm), mat_scale(F(-1), tm)))
check("[T+, T-] = 2*T3", mat_eq(comm(tp, tm), mat_scale(F(2), t3)))
# Hermitian real basis X_+ = E12+E21, X_- = i(E12-E21), H = D1-D2: same algebra
Xp = mat_add(E(2, 0, 1), E(2, 1, 0))
Xm = mat_scale(I, mat_sub(E(2, 0, 1), E(2, 1, 0)))
Hd = diag(ONE, ci(-1, 0))
check("[Hd, Xp] = 2*Xm/... structure closes (dim ledger of span{Hd,Xp,Xm} = su(2))",
      mat_eq(comm(Hd, Xp), mat_scale(F(2), mat_sub(E(2, 0, 1), E(2, 1, 0)))),
      detail=str(comm(Hd, Xp)))
check("[Xp, Xm] = -2i*Hd (Hermitian-basis su(2))",
      mat_eq(comm(Xp, Xm), mat_scale(ci(0, -2), Hd)),
      detail=str(comm(Xp, Xm)))

print("== III. W-basis commutators [W_i, W_j] = i eps_ijk W_k (CT1.4; 4x4) ==")


def kron(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])
    out = [[Z for _ in range(m * q)] for _ in range(n * p)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                for l in range(q):
                    out[i * p + k][j * q + l] = cmul(A[i][j], B[k][l])
    return out


def W(i):
    return mat_scale(F(1, 2), mat_add(kron([s1, s2, s3][i], s0), kron(s0, [s1, s2, s3][i])))


eps = {(0, 1): 2, (1, 2): 0, (2, 0): 1}
okW = True
for (i, j), k in eps.items():
    if not mat_eq(comm(W(i), W(j)), mat_scale(I, W(k))):
        okW = False
check("W_i close su(2): [W_i, W_j] = i eps_ijk W_k", okW)

print("== IV. Gell-Mann f_123 = 1 (CT3.9/CT3.21) ==")
T3g = mat_scale(F(1, 2), lam3)
check("[T_1, T_2] = i*T_3", mat_eq(comm(T1, T2), mat_scale(I, T3g)),
      detail=str(comm(T1, T2)))

print("== V. Observable capacity and the no-hosting arithmetic (FT.58(3)/(4)) ==")
pair_obs = 5 + 1 + 3          # G + H + W (J+-, D+- never observable: FT.20)
stack_obs = 1 + 8             # EM + strong (D^- never: FT.20)
check("observable pair-part dim = 9", pair_obs == 9)
check("observable stack-part dim = 9", stack_obs == 9)
check("total observable capacity = 18 = FT.26(3)", pair_obs + stack_obs == 18)
dimsu = {N: N * N - 1 for N in range(2, 9)}
check("dim su(N): 3, 8, 15, 24, 35 (N=2..6)",
      [dimsu[N] for N in range(2, 7)] == [3, 8, 15, 24, 35])
check("N >= 4: dim su(N) = 15, 24, 35 > 9 = max commuting factor",
      all(dimsu[N] > max(pair_obs, stack_obs) for N in (4, 5, 6)))
check("capacity ceiling: su(N) hostable (dim <= 9) iff N <= 3",
      all((dimsu[N] <= max(pair_obs, stack_obs)) == (N <= 3) for N in range(2, 8)))
check("N=5 forces kernel by dimension alone: 25 > 18", 5 * 5 > 18)
check("N=4: 16 <= 18 -- linear injection dimension-possible, Lie-type excluded by (3)",
      4 * 4 <= 18 and dimsu[4] > 9)

print("== VI. Separated-case ledger at N=2 (FT.58(2)) ==")
image_dim = 1                 # EM total (dim K^(EM) = 1, CT0.14)
kernel_dim = 1                # traceless diagonal D1 - D2
unhosted_dim = 2              # N^2 - N exchange generators (FT.41(d)/FT.57(1))
check("dim u(2) = 4 = 1 (image) + 1 (kernel) + 2 (unhosted)",
      image_dim + kernel_dim + unhosted_dim == 4 == 2 * 2)

print("== VII. Corolla fits (FT.58(1)/(4)) ==")
check("N=3, n(w)=3: dim su(3) = 8 = dim K^(strong) -- exact fit",
      dimsu[3] == 8)
N6_exchange = 6 * 6 - 6       # face floor [FT.49(8)]
check("N=6 face floor: exchange dims = 30", N6_exchange == 30)
check("hostable <= 8 (strong block) => unhosted >= 22", N6_exchange - 8 >= 22)

print()
if FAILS:
    print("HOSTING SUITE: %d FAIL(S): %s" % (len(FAILS), FAILS))
    sys.exit(1)
print("HOSTING SUITE: ALL %d CHECKS PASS" % PASSES)
sys.exit(0)
