
"""
verify_F.py — exact machine verification of the colour-sector claims of
document F (Qubitick_formal/F_color.md).

Exact arithmetic in the field Q(sqrt3, i):
  QS3  = a + b*sqrt3,  a,b in Fraction        (exact, since sqrt3 irrational)
  QS3C = x + i*y,      x,y in QS3             (exact complex extension)
All identities below are polynomial/rational with coefficients in this field,
so random-substitution testing is sound (Zariski density) and equality is
bit-exact.

Coverage:
  CT3.20  2^{n+1} <= 16 <=> n <= 3;  dim arithmetic 9 - 1 = 8
  CT3.1/3.3  S3 permutation matrices: 6 distinct, closed, P^T P = I,
          homomorphism P_pi P_rho = P_{pi o rho}, faithful
  CT3.4   exact unitaries (permutations x diagonal phases): L^dag L = I and
          inner-product preservation
  CT3.5/7 u(3) = su(3) + u(1): unique trace split; T[X,Y] = 0;
          pi([X,Y]) = [pi X, pi Y]; ker pi = span{I3}
  CT3.8/9 Gell-Mann basis: Hermitian, traceless, R-rank 8;
          T(l_a l_b) = 2 delta_ab ; T(T_a T_b) = 1/2 delta_ab
  CT3.21  f_abc = -2i T([T_a,T_b] T_c): exact standard list
          (f123=1; f147=f246=f257=f345=1/2; f156=f367=-1/2;
           f458=f678=sqrt3/2; else 0); total antisymmetry; Jacobi
  CT3.10  random F_strong = sum f_a T_a is traceless
  CT3.15  eps_ijk U^i_a U^j_b U^k_c = det(U) eps_abc (random exact U)
  CT3.16  trilinear characteristic identity for traceless X:
          det(I + X) = 1 - (1/2) T(X^2) + det X  (linear term absent <=> tr X = 0)
  CT3.17  U^{-1} U = I (delta invariance); eps identity applied to U^{-1}
          (dual invariance, det U^{-1} factor)

Run:  python3 verify_F.py
"""

import random
import sys
from fractions import Fraction

from qmath import matmul, matadd, matscale, matinv, matdet, trace, rank

FAILURES = []

def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILURES.append(name)

# --------------------------------------------------------------------------
# exact field  Q(sqrt3)
# --------------------------------------------------------------------------

class QS3:
    """a + b*sqrt(3), a,b in Fraction."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = a if isinstance(a, Fraction) else Fraction(a)
        self.b = b if isinstance(b, Fraction) else Fraction(b)

    @staticmethod
    def co(x):
        if isinstance(x, QS3):
            return x
        if isinstance(x, QS3C):
            raise TypeError("QS3.co: cannot coerce QS3C")
        return QS3(x)

    def __add__(self, o):
        o = QS3.co(o); return QS3(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __sub__(self, o):
        o = QS3.co(o); return QS3(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        o = QS3.co(o); return QS3(o.a - self.a, o.b - self.b)

    def __neg__(self):
        return QS3(-self.a, -self.b)

    def __mul__(self, o):
        o = QS3.co(o)
        return QS3(self.a * o.a + 3 * self.b * o.b,
                   self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 3 * self.b * self.b
        if n == 0:
            raise ZeroDivisionError("QS3.inv of zero")
        return QS3(self.a / n, -self.b / n)

    def __truediv__(self, o):
        return self * QS3.co(o).inv()

    def __rtruediv__(self, o):
        return QS3.co(o) * self.inv()

    def __eq__(self, o):
        o = QS3.co(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def __repr__(self):
        return f"({self.a}+{self.b}r3)"


# --------------------------------------------------------------------------
# exact field  Q(sqrt3, i)
# --------------------------------------------------------------------------

class QS3C:
    """x + i*y with x,y in QS3."""
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x if isinstance(x, QS3) else QS3(x)
        self.y = y if isinstance(y, QS3) else QS3(y)

    @staticmethod
    def co(x):
        if isinstance(x, QS3C):
            return x
        return QS3C(QS3.co(x))

    def __add__(self, o):
        o = QS3C.co(o); return QS3C(self.x + o.x, self.y + o.y)
    __radd__ = __add__

    def __sub__(self, o):
        o = QS3C.co(o); return QS3C(self.x - o.x, self.y - o.y)

    def __rsub__(self, o):
        o = QS3C.co(o); return QS3C(o.x - self.x, o.y - self.y)

    def __neg__(self):
        return QS3C(-self.x, -self.y)

    def __mul__(self, o):
        o = QS3C.co(o)
        return QS3C(self.x * o.x - self.y * o.y,
                    self.x * o.y + self.y * o.x)
    __rmul__ = __mul__

    def inv(self):
        n = self.x * self.x + self.y * self.y     # in QS3, nonzero iff self != 0
        ni = n.inv()
        return QS3C(self.x * ni, -self.y * ni)

    def __truediv__(self, o):
        return self * QS3C.co(o).inv()

    def __rtruediv__(self, o):
        return QS3C.co(o) * self.inv()

    def conj(self):
        return QS3C(self.x, -self.y)

    def __eq__(self, o):
        o = QS3C.co(o)
        return self.x == o.x and self.y == o.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}+i{self.y})"


R3 = QS3(0, 1)                # sqrt(3)
ONE = QS3C(1)
ZERO = QS3C(0)
I = QS3C(0, 1)                # imaginary unit
HALF = QS3C(Fraction(1, 2))

def q(x):
    return QS3C(Fraction(x))

def mat(A):
    return [[QS3C.co(A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]

def dag(M):
    return [[M[j][i].conj() for j in range(len(M))] for i in range(len(M[0]))]

def eqm(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

def I3():
    return [[ONE if i == j else ZERO for j in range(3)] for i in range(3)]

def flatten(M):
    """QS3C matrix -> rational vector (4 components per entry)."""
    v = []
    for row in M:
        for z in row:
            v += [z.x.a, z.x.b, z.y.a, z.y.b]
    return v

def rand_qs3(rng, lim=4):
    return QS3(Fraction(rng.randint(-lim, lim), rng.randint(1, 3)),
               Fraction(rng.randint(-lim, lim), rng.randint(1, 3)))

def rand_qs3c(rng, lim=4):
    return QS3C(rand_qs3(rng, lim), rand_qs3(rng, lim))

def rand_matrix(n, rng):
    return [[rand_qs3c(rng) for _ in range(n)] for _ in range(n)]

def rand_hermitian(n, rng):
    M = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = QS3C(rand_qs3(rng))            # real diagonal
        for j in range(i + 1, n):
            z = rand_qs3c(rng)
            M[i][j] = z
            M[j][i] = z.conj()
    return M

# --------------------------------------------------------------------------
# Gell-Mann basis (CT3.9)
# --------------------------------------------------------------------------

def gell_mann():
    z, o = ZERO, ONE
    L = []
    L.append([[z, o, z], [o, z, z], [z, z, z]])                      # l1
    L.append([[z, -I, z], [I, z, z], [z, z, z]])                     # l2
    L.append([[o, z, z], [z, -o, z], [z, z, z]])                     # l3
    L.append([[z, z, o], [z, z, z], [o, z, z]])                      # l4
    L.append([[z, z, -I], [z, z, z], [I, z, z]])                     # l5
    L.append([[z, z, z], [z, z, o], [z, o, z]])                      # l6
    L.append([[z, z, z], [z, z, -I], [z, I, z]])                     # l7
    r3over3 = QS3C(QS3(0, Fraction(1, 3)))                           # 1/sqrt3 = sqrt3/3
    L.append([[r3over3, z, z], [z, r3over3, z], [z, z, -2 * r3over3]])  # l8
    return L

# --------------------------------------------------------------------------

def eps3(i, j, k):
    return Fraction((i - j) * (j - k) * (k - i), 2) if len({i, j, k}) == 3 \
        else Fraction(0)

def main():
    print("verify_F: exact colour-sector checks (document F)")
    rng = random.Random(8888)
    L = gell_mann()
    T = [matscale(la, HALF) for la in L]

    # ---- CT3.20 ----------------------------------------------------------
    ok = all((2 ** (n + 1) <= 16) == (n <= 3) for n in range(0, 9))
    ok &= (3 + 6 == 9 and 9 - 1 == 8)
    check("CT3.20/CT3.8  2^{n+1} <= 16 <=> n <= 3 ;  dim u(3)=9, dim su(3)=8", ok)

    # ---- CT3.1 / CT3.3 : S3 permutation matrices --------------------------
    from itertools import permutations
    perms = list(permutations(range(3)))
    P = {}
    for pi in perms:
        M = [[q(1) if i == pi[j] else q(0) for j in range(3)] for i in range(3)]
        P[pi] = M
    keys = {tuple(map(tuple, [[str(c) for c in row] for row in M])): pi
            for pi, M in P.items()}
    distinct = len(keys) == 6
    closed = True
    homo = True
    unitary = True
    for pi in perms:
        for rho in perms:
            prod = matmul(P[pi], P[rho])
            comp = tuple(pi[rho[i]] for i in range(3))       # (pi o rho)(i)
            homo &= eqm(prod, P[comp])
            key = tuple(map(tuple, [[str(c) for c in row] for row in prod]))
            closed &= key in keys
        unitary &= eqm(matmul(dag(P[pi]), P[pi]), I3())
    check("CT3.1/CT3.3  S3 -> U(3): 6 distinct, closed, homomorphism, unitary (faithful)",
          distinct and closed and homo and unitary)

    # ---- CT3.4 : unitaries preserve inner products ------------------------
    phases = [q(1), q(-1), I, -I]
    ok = True
    for pi in perms[:3]:
        for d0 in phases[:2]:
            for d1 in phases[2:]:
                Dm = [[(d0 if i == 0 else (d1 if i == 1 else q(1))) if i == j
                       else q(0) for j in range(3)] for i in range(3)]
                Uu = matmul(P[pi], Dm)
                ok &= eqm(matmul(dag(Uu), Uu), I3())
                psi = [rand_qs3c(rng) for _ in range(3)]
                phi = [rand_qs3c(rng) for _ in range(3)]
                Lpsi = [sum(Uu[i][j] * psi[j] for j in range(3)) for i in range(3)]
                Lphi = [sum(Uu[i][j] * phi[j] for j in range(3)) for i in range(3)]
                ip1 = sum(Lpsi[i].conj() * Lphi[i] for i in range(3))
                ip0 = sum(psi[i].conj() * phi[i] for i in range(3))
                ok &= (ip1 == ip0)
    check("CT3.4  exact unitaries L: L^dag L = I and <Lpsi,Lphi> = <psi,phi>", ok)

    # ---- CT3.5 / CT3.7 : trace split, bracket tracelessness, pi homomorphism
    ok = True
    for _ in range(8):
        X = rand_hermitian(3, rng)
        Y = rand_hermitian(3, rng)
        trX = trace(X)
        X0 = matadd(X, matscale(I3(), -trX / 3))
        ok &= (trace(X0) == ZERO)
        ok &= eqm(matadd(X0, matscale(I3(), trX / 3)), X)
        comm = matadd(matmul(X, Y), matmul(Y, X), -1)
        ok &= (trace(comm) == ZERO)
        trY = trace(Y)
        Y0 = matadd(Y, matscale(I3(), -trY / 3))
        comm0 = matadd(matmul(X0, Y0), matmul(Y0, X0), -1)
        ok &= eqm(comm, comm0)                       # pi([X,Y]) = [piX,piY]
        cX = rand_qs3c(rng)
        Zc = matscale(I3(), cX)                      # central element c*I3
        Zc0 = matadd(Zc, matscale(I3(), -trace(Zc) / 3))
        ok &= eqm(Zc0, [[ZERO] * 3 for _ in range(3)])   # ker pi = span{I3}
    check("CT3.5/CT3.7  unique trace split; T[X,Y]=0; pi homomorphism; ker pi = span{I3}", ok)

    # ---- CT3.8 / CT3.9 : Gell-Mann basis ----------------------------------
    okH = all(eqm(dag(la), la) for la in L)
    okT = all(trace(la) == ZERO for la in L)
    r = rank([flatten(la) for la in L])
    okN = all(trace(matmul(L[a], L[b])) == (q(2) if a == b else ZERO)
              for a in range(8) for b in range(8))
    okTn = all(trace(matmul(T[a], T[b])) == (HALF if a == b else ZERO)
               for a in range(8) for b in range(8))
    check("CT3.9  lambda_a Hermitian and traceless", okH and okT)
    check("CT3.8/CT3.9  R-rank of the 8 generators = 8 (basis of su(3))", r == 8, f"rank={r}")
    check("CT3.9  T(l_a l_b) = 2 delta_ab ;  T(T_a T_b) = 1/2 delta_ab", okN and okTn)

    # ---- CT3.21 : structure constants --------------------------------------
    f = [[[ZERO] * 8 for _ in range(8)] for _ in range(8)]
    for a in range(8):
        for b in range(8):
            cab = matadd(matmul(T[a], T[b]), matmul(T[b], T[a]), -1)
            for c in range(8):
                f[a][b][c] = QS3C(QS3(0), QS3(-2)) * trace(matmul(cab, T[c]))
    expected = {
        (0, 1, 2): QS3C(1),                                   # f123 = 1
        (0, 3, 6): QS3C(Fraction(1, 2)),                      # f147 = 1/2
        (1, 3, 5): QS3C(Fraction(1, 2)),                      # f246 = 1/2
        (1, 4, 6): QS3C(Fraction(1, 2)),                      # f257 = 1/2
        (2, 3, 4): QS3C(Fraction(1, 2)),                      # f345 = 1/2
        (0, 4, 5): QS3C(Fraction(-1, 2)),                     # f156 = -1/2
        (2, 5, 6): QS3C(Fraction(-1, 2)),                     # f367 = -1/2
        (3, 4, 7): QS3C(QS3(0, Fraction(1, 2))),              # f458 = sqrt3/2
        (5, 6, 7): QS3C(QS3(0, Fraction(1, 2))),              # f678 = sqrt3/2
    }
    ok = True
    for a in range(8):
        for b in range(8):
            for c in range(8):
                val = ZERO
                key = None
                for (p, q2, r2), v in expected.items():
                    perm = sorted((a, b, c))
                    if perm == [p, q2, r2]:
                        # sign of permutation from (p,q2,r2) to (a,b,c)
                        sgn = eps3(a, b, c) / eps3(p, q2, r2) if (a, b, c) != (p, q2, r2) else Fraction(1)
                        val = QS3C(QS3(sgn)) * v if sgn != 1 else v
                        if len({a, b, c}) < 3:
                            val = ZERO
                        break
                ok &= (f[a][b][c] == val)
    check("CT3.21  f_abc = -2i T([T_a,T_b]T_c): exact standard list, totally antisymmetric", ok)

    okJ = True
    comm = lambda A, B: matadd(matmul(A, B), matmul(B, A), -1)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                tot = matadd(matadd(comm(comm(T[a], T[b]), T[c]),
                                    comm(comm(T[c], T[a]), T[b])),
                             comm(comm(T[b], T[c]), T[a]))
                okJ &= all(x == ZERO for row in tot for x in row)
    check("CT3.21  Jacobi identity [[T_a,T_b],T_c] + cyclic = 0 (all 512 triples)", okJ)

    # ---- CT3.10 : tracelessness of random F_strong --------------------------
    ok = True
    for _ in range(6):
        coeffs = [rand_qs3(rng) for _ in range(8)]
        Fs = [[ZERO] * 3 for _ in range(3)]
        for a in range(8):
            Fs = matadd(Fs, matscale(T[a], QS3C(coeffs[a])))
        ok &= (trace(Fs) == ZERO)
    check("CT3.10  T(F_strong) = 0 for random real coefficient combinations", ok)

    # ---- CT3.15 / CT3.17 : epsilon and delta invariance ---------------------
    ok = True
    ok17 = True
    for _ in range(6):
        U = rand_matrix(3, rng)
        if matdet(U) == ZERO:
            continue
        detU = matdet(U)
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    lhs = ZERO
                    for i in range(3):
                        for j in range(3):
                            for k in range(3):
                                e = eps3(i, j, k)
                                if e != 0:
                                    lhs = lhs + QS3C(e) * U[i][a] * U[j][b] * U[k][c]
                    rhs = detU * (QS3C(eps3(a, b, c)))
                    ok &= (lhs == rhs)
        Ui = matinv(U)
        ok17 &= eqm(matmul(Ui, U), I3())
        detUi = matdet(Ui)
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    lhs = ZERO
                    for i in range(3):
                        for j in range(3):
                            for k in range(3):
                                e = eps3(i, j, k)
                                if e != 0:
                                    lhs = lhs + QS3C(e) * Ui[i][a] * Ui[j][b] * Ui[k][c]
                    ok17 &= (lhs == detUi * QS3C(eps3(a, b, c)))
    check("CT3.15  eps_ijk U^i_a U^j_b U^k_c = det(U) eps_abc (exact random U)", ok)
    check("CT3.17  U^{-1}U = I (delta) and dual epsilon identity with det(U^{-1})", ok17)

    # ---- CT3.16 : characteristic identity for traceless X -------------------
    ok = True
    for _ in range(6):
        X = rand_matrix(3, rng)
        trX = trace(X)
        X0 = matadd(X, matscale(I3(), -trX / 3))          # traceless part
        IX = matadd(I3(), X0)
        lhs = matdet(IX)
        X2 = matmul(X0, X0)
        rhs = ONE - HALF * trace(X2) + matdet(X0)
        ok &= (lhs == rhs and trace(X0) == ZERO)
    check("CT3.16  det(I+X) = 1 - (1/2)T(X^2) + det X for traceless X (no linear term)", ok)

    print()
    if FAILURES:
        print(f"verify_F: {len(FAILURES)} FAILURE(S): {FAILURES}")
        return 1
    print("verify_F: ALL CHECKS PASS (exact arithmetic in Q(sqrt3, i))")
    return 0

if __name__ == "__main__":
    sys.exit(main())
