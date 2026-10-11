
"""
qmath.py — pure-stdlib math core for the Qubitick corpus checks.

No dependencies beyond the Python 3 standard library.

Rings used (all exact, no floating point anywhere):

  fractions.Fraction   exact rationals          — jet calculus (CT1.12–CT1.17), dimensions, combinatorics
  C                    exact complex a+b*i,     — Pauli / pair-operator algebra (document B)
                         a,b in Fraction
  Series2              truncated series         — linearization to O(eps^2) (CT1.18)
                         a0 + a1*e + a2*e^2,
                         coefficients Fraction

Matrices are nested lists [[...],[...]] over any of these rings. The matrix
routines below are ring-generic: they require +, -, *, unary -, exact
comparison with zero, and 1/x for units. `is_unit` dispatches:
  Fraction/C   : x != 0
  Series2      : constant coefficient != 0  (formal-power-series invertibility)

Method note (why numeric substitution proves identities): every checked
tensor identity is an algebraic (rational) identity in the jet variables.
If it holds on random rational data with invertible metric — a Zariski-dense
set — it holds identically. All arithmetic is exact, so "holds" means bit-
exact equality, not tolerance.
"""

from fractions import Fraction

# --------------------------------------------------------------------------
# Ring: exact complex numbers over Fraction
# --------------------------------------------------------------------------

class C:
    """Exact complex number re + im*i with re, im in Fraction."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = re if isinstance(re, Fraction) else Fraction(re)
        self.im = im if isinstance(im, Fraction) else Fraction(im)

    @staticmethod
    def co(x):
        return x if isinstance(x, C) else C(x)

    def __add__(self, o):
        o = C.co(o); return C(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, o):
        o = C.co(o); return C(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        o = C.co(o); return C(o.re - self.re, o.im - self.im)

    def __neg__(self):
        return C(-self.re, -self.im)

    def __mul__(self, o):
        o = C.co(o)
        return C(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def inv(self):
        n = self.re * self.re + self.im * self.im
        if n == 0:
            raise ZeroDivisionError("C.inv of zero")
        return C(self.re / n, -self.im / n)

    def __truediv__(self, o):
        return self * C.co(o).inv()

    def __rtruediv__(self, o):
        return C.co(o) * self.inv()

    def conj(self):
        return C(self.re, -self.im)

    def __eq__(self, o):
        o = C.co(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"C({self.re},{self.im})"


# --------------------------------------------------------------------------
# Ring: truncated power series a0 + a1*e + a2*e^2  (e^3 = 0), over Fraction
# --------------------------------------------------------------------------

class Series2:
    __slots__ = ("a",)

    def __init__(self, a0=0, a1=0, a2=0):
        self.a = (Fraction(a0), Fraction(a1), Fraction(a2))

    @staticmethod
    def co(x):
        return x if isinstance(x, Series2) else Series2(x)

    def __add__(self, o):
        o = Series2.co(o)
        return Series2(*[p + q for p, q in zip(self.a, o.a)])
    __radd__ = __add__

    def __sub__(self, o):
        o = Series2.co(o)
        return Series2(*[p - q for p, q in zip(self.a, o.a)])

    def __rsub__(self, o):
        o = Series2.co(o)
        return Series2(*[q - p for p, q in zip(self.a, o.a)])

    def __neg__(self):
        return Series2(*[-p for p in self.a])

    def __mul__(self, o):
        o = Series2.co(o)
        a, b = self.a, o.a
        return Series2(a[0] * b[0],
                       a[0] * b[1] + a[1] * b[0],
                       a[0] * b[2] + a[1] * b[1] + a[2] * b[0])
    __rmul__ = __mul__

    def inv(self):
        a0, a1, a2 = self.a
        if a0 == 0:
            raise ZeroDivisionError("Series2.inv: constant term is zero")
        return Series2(1 / a0, -a1 / (a0 * a0), a1 * a1 / (a0 ** 3) - a2 / (a0 * a0))

    def __truediv__(self, o):
        return self * Series2.co(o).inv()

    def __rtruediv__(self, o):
        return Series2.co(o) * self.inv()

    def __eq__(self, o):
        o = Series2.co(o)
        return self.a == o.a

    def __hash__(self):
        return hash(self.a)

    def __repr__(self):
        return f"S2({self.a[0]},{self.a[1]},{self.a[2]})"


# --------------------------------------------------------------------------
# Ring-generic helpers
# --------------------------------------------------------------------------

def zero(proto):
    if isinstance(proto, Series2): return Series2(0)
    if isinstance(proto, C):       return C(0)
    return Fraction(0)

def one(proto):
    if isinstance(proto, Series2): return Series2(1)
    if isinstance(proto, C):       return C(1)
    return Fraction(1)

def half(proto):
    if isinstance(proto, Series2): return Series2(Fraction(1, 2))
    if isinstance(proto, C):       return C(Fraction(1, 2))
    return Fraction(1, 2)

def from_frac(proto, f):
    f = Fraction(f)
    if isinstance(proto, Series2): return Series2(f)
    if isinstance(proto, C):       return C(f)
    return f

def is_unit(x):
    if isinstance(x, Series2): return x.a[0] != 0
    return x != 0


# --------------------------------------------------------------------------
# Generic matrix routines (nested lists over any supported ring)
# --------------------------------------------------------------------------

def matmul(A, B):
    n, p, m = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)]
            for i in range(n)]

def matadd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def matscale(A, c):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def transpose(A):
    return [list(col) for col in zip(*A)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def matinv(M):
    """Gauss–Jordan inverse over Fraction / C / Series2."""
    n = len(M)
    proto = M[0][0]
    o, z = one(proto), zero(proto)
    A = [list(M[i]) + [o if i == j else z for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if is_unit(A[r][col])), None)
        if piv is None:
            raise ZeroDivisionError("matinv: singular or non-unit pivot")
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
        p = A[col][col]
        A[col] = [x / p for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != z:
                f = A[r][col]
                A[r] = [A[r][j] - f * A[col][j] for j in range(2 * n)]
    return [row[n:] for row in A]

def matdet(M):
    """Exact determinant by Gauss elimination with row swaps."""
    n = len(M)
    proto = M[0][0]
    o, z = one(proto), zero(proto)
    A = [list(row) for row in M]
    det, swaps = o, 0
    for col in range(n):
        piv = next((r for r in range(col, n) if is_unit(A[r][col])), None)
        if piv is None:
            return z
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            swaps += 1
        p = A[col][col]
        det = det * p
        A[col] = [x / p for x in A[col]]
        for r in range(col + 1, n):
            if A[r][col] != z:
                f = A[r][col]
                A[r] = [A[r][j] - f * A[col][j] for j in range(n)]
    return -det if swaps % 2 else det

def rank(vecs):
    """Rank of a list of Fraction vectors (exact Gaussian elimination)."""
    rows = [list(map(Fraction, v)) for v in vecs]
    if not rows:
        return 0
    ncol = len(rows[0])
    r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        p = rows[r][c]
        rows[r] = [x / p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [rows[i][j] - f * rows[r][j] for j in range(ncol)]
        r += 1
        if r == len(rows):
            break
    return r

def conj_transpose(A):
    return [[A[j][i].conj() if isinstance(A[j][i], C) else A[j][i]
             for j in range(len(A))] for i in range(len(A[0]))]
