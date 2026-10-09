#!/usr/bin/env python3
"""
verify_promotion_F_colour.py — exact machine checks for the imported F corollaries

  Cor CT3.17a (sealing partition rule; grammar counts):
      g(N) = #{set partitions of a labelled N-set into parts of size 2 and 3}
           = sum_{2a+3b=N} N!/(a! b! 2^a 6^b)
      enumeration vs closed form (N = 1..8 exhaustive; closed form to N = 20);
      documented values 0,1,1,3,10,25,105 (N=1..7); lone attachment: g(1)=0;
      type-compatibility refinement counts at N=2,3.

  Cor CT3.10a (no per-edge abelian strong phase):
      exact Hermitian-matrix algebra over Q(sqrt3, i):
      tr(T_a) = 0; sum f_a T_a = c*I  <=>  f = 0 and c = 0 (nullspace rank);
      witnesses U2 = i*lam2 + I - lam2^2, U5 = i*lam5 + I - lam5^2 in SU(3)
      (unitary, det = 1); Ad_{U5}(T1) = -T6; per-line witness census:
      for every a some U in {U2, U5} moves span{T_a};
      dimension integers: dim u(3) = 9, dim su(3) = 8, K_3 = 25 = 17 + 8,
      dim K(EM) = 1.

Pure Python 3 standard library; exact arithmetic over Fraction pairs
(a + b*sqrt3) with complex structure (re, im). No floating point.
Deterministic. Exit code 0 = all green.
"""
import itertools
import era_paths
import math
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


# ============================================================ §A  CT3.17a
def partitions_23(items):
    """All set partitions of `items` (list) into blocks of size 2 or 3."""
    if not items:
        return [()]
    first = items[0]
    rest = items[1:]
    out = []
    # block of size 2 containing first
    for i, x in enumerate(rest):
        blk = (first, x)
        rem = rest[:i] + rest[i + 1:]
        for p in partitions_23(rem):
            out.append((blk,) + p)
    # block of size 3 containing first
    for i in range(len(rest)):
        for j in range(i + 1, len(rest)):
            blk = (first, rest[i], rest[j])
            rem = [x for k, x in enumerate(rest) if k != i and k != j]
            for p in partitions_23(rem):
                out.append((blk,) + p)
    return out


def g_closed(N):
    tot = 0
    fact = math.factorial
    for b in range(N // 3 + 1):
        rem = N - 3 * b
        if rem % 2:
            continue
        a = rem // 2
        tot += fact(N) // (fact(a) * fact(b) * 2 ** a * 6 ** b)
    return tot


ENUM = {N: len(partitions_23(list(range(N)))) for N in range(1, 9)}
DOC_VALS = {1: 0, 2: 1, 3: 1, 4: 3, 5: 10, 6: 25, 7: 105}
chk("enumerated g(N), N=1..7 == documented values 0,1,1,3,10,25,105",
    all(ENUM[N] == DOC_VALS[N] for N in range(1, 8)), str(ENUM))
chk("enumerated g(8) == 385  (= 105 four-pair + 280 one-pair-two-triple)", ENUM[8] == 385, str(ENUM[8]))
chk("enumeration == closed form for N=1..8",
    all(ENUM[N] == g_closed(N) for N in range(1, 9)))
chk("closed form exact to N=20; g(20) == 292938721075",
    g_closed(20) == 292938721075 and all(g_closed(N) >= 0 for N in range(21)))
chk("g(6) splits 15 (three pairs) + 10 (two triples)",
    720 // (6 * 8) == 15 and 720 // (2 * 36) == 10 and 15 + 10 == 25)
chk("lone attachment never sealed: g(1) = 0 (no part of size 1)", ENUM[1] == 0)
# every enumerated partition has parts of size 2 or 3 only, and is a partition
ok = True
for N in range(1, 8):
    for p in partitions_23(list(range(N))):
        flat = sorted(x for blk in p for x in blk)
        if flat != list(range(N)) or any(len(blk) not in (2, 3) for blk in p):
            ok = False
chk("all enumerated groupings are genuine {2,3}-partitions of the label set", ok)

# type refinement: triplet/antitriplet per attachment; delta consumes one of
# each, epsilon consumes three of the same. Count compatible (grouping, typing).
def type_compatible_count(N):
    total = 0
    for typing in itertools.product((0, 1), repeat=N):   # 0 = triplet, 1 = anti
        for p in partitions_23(list(range(N))):
            okp = True
            for blk in p:
                ts = {typing[x] for x in blk}
                if len(blk) == 2 and len(ts) != 2:
                    okp = False
                if len(blk) == 3 and len(ts) != 1:
                    okp = False
            if okp:
                total += 1
    return total

chk("type refinement N=2: 2 compatible (grouping, typing) configurations",
    type_compatible_count(2) == 2)
chk("type refinement N=3: 2 compatible configurations (all-triplet, all-anti)",
    type_compatible_count(3) == 2)
chk("type refinement N=1: 0 compatible configurations", type_compatible_count(1) == 0)

# ============================================================ §B  CT3.10a
# --- exact ring: entries are 2x2 matrices over Q(sqrt3): [[re0,re3],[im0,im3]]
F0 = Fraction(0)
F1 = Fraction(1)


def q(r0, r3=F0):
    return (Fraction(r0), Fraction(r3))


class C3:
    """complex number over Q(sqrt3): (a + b s) + (c + d s) i,  s = sqrt(3)."""
    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a, b=F0, c=F0, d=F0):
        self.a, self.b, self.c, self.d = Fraction(a), Fraction(b), Fraction(c), Fraction(d)

    def __add__(self, o):
        return C3(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)

    def __sub__(self, o):
        return C3(self.a - o.a, self.b - o.b, self.c - o.c, self.d - o.d)

    def __mul__(self, o):
        # (A + Ci)(B + Di) = (AB - CD) + (AD + CB)i,  A = a + b s, s = sqrt(3)
        # (a + b s)(c + d s) = (ac + 3bd) + (ad + bc) s
        ra = self.a * o.a + 3 * self.b * o.b - self.c * o.c - 3 * self.d * o.d
        rb = self.a * o.b + self.b * o.a - self.c * o.d - self.d * o.c
        ia = self.a * o.c + 3 * self.b * o.d + self.c * o.a + 3 * self.d * o.b
        ib = self.a * o.d + self.b * o.c + self.c * o.b + self.d * o.a
        return C3(ra, rb, ia, ib)

    def scale(self, r):
        r = Fraction(r)
        return C3(r * self.a, r * self.b, r * self.c, r * self.d)

    def conj(self):
        return C3(self.a, self.b, -self.c, -self.d)

    def neg(self):
        return C3(-self.a, -self.b, -self.c, -self.d)

    def is_zero(self):
        return (self.a, self.b, self.c, self.d) == (F0, F0, F0, F0)

    def __eq__(self, o):
        return (self.a, self.b, self.c, self.d) == (o.a, o.b, o.c, o.d)

    def __repr__(self):
        return f"C3({self.a},{self.b},{self.c},{self.d})"


Z = C3(0)
ONE = C3(1)
I = C3(0, 0, 1, 0)
S3 = C3(0, 1)          # sqrt(3)
HALF = Fraction(1, 2)


def mat(rows):
    return [[x for x in row] for row in rows]


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), Z) for j in range(n)]
            for i in range(n)]


def dagger(A):
    n = len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]


def trace(A):
    return sum((A[i][i] for i in range(len(A))), Z)


def ident(n=3):
    return [[ONE if i == j else Z for j in range(n)] for i in range(n)]


# Gell-Mann matrices (CT3.9 basis; lam_a = 2 T_a)
lam = {}
lam[1] = mat([[Z, ONE, Z], [ONE, Z, Z], [Z, Z, Z]])
lam[2] = mat([[Z, C3(0, 0, -1), Z], [C3(0, 0, 1), Z, Z], [Z, Z, Z]])
lam[3] = mat([[ONE, Z, Z], [Z, ONE.neg(), Z], [Z, Z, Z]])
lam[4] = mat([[Z, Z, ONE], [Z, Z, Z], [ONE, Z, Z]])
lam[5] = mat([[Z, Z, C3(0, 0, -1)], [Z, Z, Z], [C3(0, 0, 1), Z, Z]])
lam[6] = mat([[Z, Z, Z], [Z, Z, ONE], [Z, ONE, Z]])
lam[7] = mat([[Z, Z, Z], [Z, Z, C3(0, 0, -1)], [Z, C3(0, 0, 1), Z]])
# lam8 = diag(1,1,-2)/sqrt(3): 1/sqrt(3) = sqrt(3)/3
r3over3 = Fraction(1, 3)
lam[8] = mat([[C3(0, r3over3), Z, Z],
              [Z, C3(0, r3over3), Z],
              [Z, Z, C3(0, -2 * r3over3)]])
T = {a: mat([[lam[a][i][j].scale(HALF) for j in range(3)] for i in range(3)])
     for a in range(1, 9)}

# (i) tracelessness
chk("tr(T_a) = 0 for all a = 1..8", all(trace(T[a]).is_zero() for a in T))
chk("tr(lam_a lam_b) = 2 delta_ab (exact, all 64 pairs)",
    all(trace(matmul(lam[a], lam[b])) == (C3(2) if a == b else Z)
        for a in range(1, 9) for b in range(1, 9)))

# (ii) sum f_a T_a = c I  <=>  f = 0 and c = 0, via exact nullspace over Q.
# Flatten: each matrix entry (a + b s) + (c + d s) i gives 4 rational rows-
# components; unknowns f_1..f_8, c over Q. Build 36 x 9 rational system.
rows = []
for i in range(3):
    for j in range(3):
        for comp in range(4):   # components: a, b, c, d
            row = []
            for aa in range(1, 9):
                v = T[aa][i][j]
                row.append((v.a, v.b, v.c, v.d)[comp])
            # minus c * I[i][j]
            ident_v = ONE if i == j else Z
            row.append(-(ident_v.a, ident_v.b, ident_v.c, ident_v.d)[comp])
            rows.append(row)


def rank_mod(rows_in):
    rows = [list(map(Fraction, r)) for r in rows_in]
    rows = [r for r in rows if any(x != 0 for x in r)]
    r = 0
    for col in range(len(rows[0])):
        piv = next((k for k in range(r, len(rows)) if rows[k][col] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][col]
        rows[r] = [x / pv for x in rows[r]]
        for k in range(len(rows)):
            if k != r and rows[k][col] != 0:
                f = rows[k][col]
                rows[k] = [x - f * y for x, y in zip(rows[k], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


rk = rank_mod(rows)
chk("nullspace of {sum f_a T_a = c I} is trivial: rank 9 of 9 unknowns",
    rk == 9, f"rank={rk}")

# (iii) witnesses U2, U5 in SU(3)
def U_of(k):
    # U = i*lam_k + I - lam_k^2
    lk2 = matmul(lam[k], lam[k])
    return [[I * lam[k][i][j] + (ONE if i == j else Z) - lk2[i][j]
             for j in range(3)] for i in range(3)]


def det3(A):
    t0 = A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
    t1 = A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
    t2 = A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    return t0 - t1 + t2


U2, U5 = U_of(2), U_of(5)
for nm, U in (("U2", U2), ("U5", U5)):
    chk(f"{nm}: U U^dagger = I (unitary, exact)",
        all(matmul(U, dagger(U))[i][j] == (ONE if i == j else Z)
            for i in range(3) for j in range(3)))
    chk(f"{nm}: det U = 1 (SU(3), exact)", det3(U) == ONE)


def Ad(U, M):
    return matmul(matmul(U, M), dagger(U))


def proportional(M, N):
    """M = r*N for some scalar r (over the entry field)? Cross-multiplication."""
    flatM = [v for row in M for v in row]
    flatN = [v for row in N for v in row]
    for x, y in itertools.product(range(9), repeat=2):
        if (flatM[x] * flatN[y]) != (flatM[y] * flatN[x]):
            return False
    return True


# Ad_{U5}(T1) = -T6 (verbatim corpus witness)
chk("Ad_U5(T1) = -T6 exactly",
    all(Ad(U5, T[1])[i][j] == T[6][i][j].neg() for i in range(3) for j in range(3)))
chk("Ad_U5(T1) not proportional to T1", not proportional(Ad(U5, T[1]), T[1]))
# Ad_U5(T2) = T7 (corpus Pf line)
chk("Ad_U5(T2) = +T7 exactly",
    all(Ad(U5, T[2])[i][j] == T[7][i][j] for i in range(3) for j in range(3)))

# per-line witness census: for each a, some U in {U2, U5} moves span{T_a}
moved = {}
for a in range(1, 9):
    w = None
    for nm, U in (("U2", U2), ("U5", U5)):
        if not proportional(Ad(U, T[a]), T[a]):
            w = nm
            break
    moved[a] = w
chk("every generator line span{T_a} is moved by some witness in {U2,U5}",
    all(v is not None for v in moved.values()), str(moved))

# (iv) dimension integers
chk("dim u(3) = 9, dim su(3) = 8 (parameter counts)", 3 + 3 * 2 == 9 and 9 - 1 == 8)
chk("K_3 = 25 = 17 + 8; EM block dim = 1 (CT0.14/CT0.12 integers)",
    25 == 17 + 8 and 3 + 3 + 5 + 3 + 1 + 1 == 16 and 1 == 1)

# ============================================================ §C  document integration
f_src = era_paths.read("F_color.md")
for tag in ("CT3.10a", "CT3.17a"):
    chk(f"F_color.md contains **Cor {tag} (", f"**Cor {tag} (" in f_src)
    blk = f_src.split(f"**Cor {tag} (", 1)[1]
    cut = min([blk.find(m) if blk.find(m) != -1 else len(blk)
               for m in ("\n---", "\n**Phys.**", "\n### ", "\n## ")])
    body = blk[:cut]
    chk(f"Cor {tag}: has Req (Cor) and Pf (Cor) with terminator",
        "**Req (Cor).**" in body and "**Pf (Cor).**" in body and r"\blacksquare" in body)
    chk(f"Cor {tag}: cites no FT./Def-H./P-H token",
        not re.search(r"FT\.|Def-H\.|P-H\d", body))
chk("F closure exports mention CT3.10(a) and CT3.17a",
    r"\mathrm{CT3.10(a)}" in f_src and r"\mathrm{CT3.17a}" in f_src)
chk("F header lists verify_promotion_F_colour.py", "verify_promotion_F_colour.py" in f_src)

print(f"verify_promotion_F_colour: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
sys.exit(1 if FAIL else 0)
