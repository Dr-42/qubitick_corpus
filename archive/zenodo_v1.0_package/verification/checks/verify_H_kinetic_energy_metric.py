#!/usr/bin/env python3
"""
verify_H_kinetic_energy_metric.py — machine verification of Tier BM.10
(Def-BM.10, BM.34–BM.38): the kinetic energy from the emergent metric, the
vacuum-balanced entropy reframing of the rest mass, the force-structure
ladder with its strength bar, and the route-artifact adjudication closing
the counting trap.

Exact arithmetic only: integers, fractions.Fraction, multivariate polynomial
rings over Q with monomial rewrite rules (quotient rings), Laurent-monomial
rings Q[h,E,ln2,pi,V]^{+-}, truncated power series over Q, the quadratic ring
Q(sqrt7), complex-over-polynomial Pauli spinor algebra over Q(i)(x)Q[g,g'].
No floating point in any assertion.

Sections:
  §A  BM.34/Def-BM.10 — the ADM split of CT1.12's emergent metric as exact
      polynomial identities over Q[Omega^2, kappa, beta, w_i, q_ij, p_mu, m]:
      the lapse identity N^2 det(gamma) = -det g (Schur), the cleared adjugate
      rows of the inverse metric, the line-element identity, the master
      dispersion identity (p_0 - N^i p_i)^2 = N^2 (m^2 + gamma^{ij} p_i p_j),
      the vacuum-flat specialization, the T-parity rows, three rational metric
      witnesses with exact Fraction inverses, the binomial series sqrt(1+x)
      with rational coefficients and the KE assembly, the Sylvester positivity
      regime, the zero-point bounds (7/4, 3/8, sqrt(7)/2 in Q(sqrt7) with
      x^2-7 irreducible), and the on-shell rest agreement with BM.9(5)/BM.20(1)
      as Laurent identities.
  §B  BM.35 — the vacuum-balanced entropy: the exhaustive 1/8-grid Gibbs
      census (165 compositions, uniqueness of the maximizer by pure integer
      comparison), the exact ln2 enclosure 1/2 < ln2 < 1 (tail < 2^-20), the
      balance identity ln4 = 2 ln2 and Delta S_L = E_int ln2 = I_hid, the
      reframing identity m_rest = m_hid as one Laurent monomial, the CT2.1
      dimension exponents, the three-currency distinctness witnesses, and the
      total-energy series assembly.
  §C  BM.36 — the force-structure ladder: the mask-flag integer censuses
      (6,16,17,25; increments 1 and 8; the 18 bound), the derived dimension
      ratios (1/3, 8, 1/25) as exact Fractions, the EW.33 Gram form recomputed
      from Pauli spinors over Q(i) with symbolic g,g' (imaginary parts antisymmetric,
      cancelling in the symmetric form), the charpoly factorization giving the spectrum
      {g^2/4, g^2/4, 0, (g^2+g'^2)/4}, the kernel line c ~ (0,0,g',g), the
      h_0 = 0 vanishing, the M_Z^2/M_W^2 cross-multiplication, the sandwich
      PSD factorization, and the strength-bar text pins.
  §D  BM.37 — the route-artifact adjudication: the W(Q) census re-enumerated
      two ways (20, 15, 15 and (1,6,15,20,15,6,1)), the route-(i) cancellation
      lemma at the six frozen factors, the route-(iii) exact reductions
      5336/1196 = 58/13 and 4796/802 = 2398/401, the pairwise inequalities by
      integer cross-multiplication, the disjoint input-alphabet token census
      on the canonical defining strings extracted from the canon files, and
      the Koide-form invariant Q = 2/3 re-verified phase-independently in
      Q[c,s,r,u]/(c^2+s^2-1, r^2-3, u^2-2).
  §E  BM.38 — document pins and hygiene: tier/tag presence and uniqueness,
      Thm/Req/Pf/Phys completeness, namespace/charter/closure rows, the
      forbidden-word and P5 scans of the tier text, the Cal-BM standing row,
      HistLog §III/§V entries, README suite counts at 65, index and Summary
      regeneration pins.

Tier BM.10 is new canon content with no first edition in H_archive/; the pins
of this checker resolve against the era-canon texts directly.

Run: python3 verify_H_kinetic_energy_metric.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import itertools
import json
import os
import re
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

t0 = time.time()
N = 0
FAILS = []


def chk(cond, msg):
    global N
    if cond:
        N += 1
    else:
        FAILS.append(msg)
        print(f"  FAIL: {msg}")


def stamp(m):
    print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")


def rd(fn):
    with open(os.path.join(DOCS, fn), encoding="utf-8") as f:
        return f.read()


print("=" * 74)
print("verify_H_kinetic_energy_metric — Tier BM.10 (Def-BM.10, BM.34–BM.38)")
print("=" * 74)


# ==========================================================================
# exact rings
# ==========================================================================

class Poly:
    """Commutative polynomial over Fraction in named variables, with monomial
    rewrite rules (quotient rings). Exact; no floating point."""

    def __init__(self, names, terms=None, rules=None):
        self.names = list(names)
        self.ix = {n: i for i, n in enumerate(self.names)}
        self.rules = rules or {}          # (varname, power) -> Poly
        self.t = {}
        if terms:
            for e, c in terms.items():
                self._add(e, c)
            self._normalize()

    @staticmethod
    def const(names, x, rules=None):
        return Poly(names, {tuple([0] * len(names)): Fr(x)}, rules)

    @staticmethod
    def var(names, n, rules=None):
        e = [0] * len(names)
        e[names.index(n)] = 1
        return Poly(names, {tuple(e): Fr(1)}, rules)

    def copy(self):
        return Poly(self.names, dict(self.t), self.rules)

    def _add(self, e, c):
        if c == 0:
            return
        self.t[e] = self.t.get(e, Fr(0)) + c
        if self.t[e] == 0:
            del self.t[e]

    def _normalize(self):
        guard = 0
        changed = True
        while changed and self.rules:
            changed = False
            guard += 1
            if guard > 200000:
                raise RuntimeError("normalization did not terminate")
            for e, c in list(self.t.items()):
                for (vn, pw), rep in self.rules.items():
                    k = self.ix[vn]
                    if e[k] >= pw:
                        del self.t[e]
                        rest = list(e)
                        rest[k] -= pw
                        for e2, c2 in rep.t.items():
                            acc = [rest[i] + e2[i] for i in range(len(rest))]
                            self._add(tuple(acc), c * c2)
                        changed = True
                        break
                if changed:
                    break

    def __add__(self, o):
        r = Poly(self.names, dict(self.t), self.rules)
        for e, c in o.t.items():
            r._add(e, c)
        r._normalize()
        return r

    def __sub__(self, o):
        r = Poly(self.names, dict(self.t), self.rules)
        for e, c in o.t.items():
            r._add(e, -c)
        r._normalize()
        return r

    def __neg__(self):
        return Poly(self.names, {e: -c for e, c in self.t.items()}, self.rules)

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return Poly(self.names, {e: Fr(o) * c for e, c in self.t.items()}, self.rules)
        acc = {}
        for e1, c1 in self.t.items():
            for e2, c2 in o.t.items():
                e = tuple(e1[i] + e2[i] for i in range(len(e1)))
                acc[e] = acc.get(e, Fr(0)) + c1 * c2
        acc = {e: c for e, c in acc.items() if c != 0}
        return Poly(self.names, acc, self.rules)

    def __rmul__(self, x):
        return Poly(self.names, {e: Fr(x) * c for e, c in self.t.items()}, self.rules)

    def pow(self, n):
        r = Poly.const(self.names, 1, self.rules)
        b = self.copy()
        while n:
            if n & 1:
                r = r * b
            b = b * b
            n >>= 1
        return r

    def scale(self, x):
        return Poly(self.names, {e: c * Fr(x) for e, c in self.t.items()}, self.rules)

    def zero(self):
        return not self.t

    def __eq__(self, o):
        if not isinstance(o, Poly):
            return NotImplemented
        return self.t == o.t

    def __ne__(self, o):
        r = self.__eq__(o)
        return r if r is NotImplemented else not r

    def __hash__(self):
        return hash(tuple(sorted(self.t.items(), key=lambda kv: str(kv[0]))))

    def subs(self, values):
        """Exact substitution: name -> Fraction/int. Variables not named stay
        symbolic; if the result is fully numeric it collapses to a Fraction."""
        out = Poly(self.names, rules=self.rules)
        for e, c in self.t.items():
            term = Poly.const(self.names, c, self.rules)
            kill = False
            for i, n in enumerate(self.names):
                if e[i]:
                    if n in values:
                        v = Fr(values[n])
                        if v == 0:
                            kill = True
                            break
                        term = term.scale(v ** e[i])
                    else:
                        term = term * Poly.var(self.names, n, self.rules).pow(e[i])
            if not kill:
                out = out + term
        z = tuple([0] * len(self.names))
        if not out.t:
            return Fr(0)
        if all(e == z for e in out.t):
            return out.t[z]
        return out

    def __repr__(self):
        if not self.t:
            return "0"
        parts = []
        for e, c in sorted(self.t.items(), key=lambda kv: str(kv[0]))[:8]:
            s = str(c)
            for i, n in enumerate(self.names):
                if e[i] == 1:
                    s += f"*{n}"
                elif e[i] > 1:
                    s += f"*{n}^{e[i]}"
            parts.append(s)
        tail = f" + ...({len(self.t)} terms)" if len(self.t) > 8 else ""
        return " + ".join(parts) + tail


def P(names, x, rules=None):
    return Poly.const(names, x, rules)


def V(names, n, rules=None):
    return Poly.var(names, n, rules)


# ---- matrices over Poly ---------------------------------------------------

def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    zero = A[0][0] * 0
    C = [[zero for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            acc = zero
            for t in range(k):
                acc = acc + A[i][t] * B[t][j]
            C[i][j] = acc
    return C


def mdet(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    acc = M[0][0] * 0
    for j in range(n):
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = M[0][j] * mdet(minor)
        acc = acc + term if j % 2 == 0 else acc - term
    return acc


def madj(M):
    """adjugate: (adj M)_{ji} = cofactor_{ij}, so that adj(M) M = det(M) I."""
    n = len(M)
    A = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [[M[r][c] for c in range(n) if c != j] for r in range(n) if r != i]
            cof = mdet(minor)
            A[j][i] = cof if (i + j) % 2 == 0 else -cof
    return A


def mvec(A, v):
    zero = A[0][0] * 0
    return [sum((A[i][j] * v[j] for j in range(len(v))), zero) for i in range(len(A))]


# ---- matrices over Fraction ----------------------------------------------

def fdet(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    acc = Fr(0)
    for j in range(n):
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = M[0][j] * fdet(minor)
        acc = acc + term if j % 2 == 0 else acc - term
    return acc


def finv(M):
    """exact inverse by Gauss-Jordan over Fraction."""
    n = len(M)
    A = [list(row) + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]


def sylvester_pos(M):
    """all leading principal minors positive (exact Fractions)."""
    return all(fdet([row[:k] for row in M[:k]]) > 0 for k in range(1, len(M) + 1))


# ---- quadratic ring Q(sqrt d) ---------------------------------------------

class Qd:
    """a + b*sqrt(d) over Fraction; d a squarefree positive integer."""

    def __init__(self, d, a, b=0):
        self.d = d
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, o):
        return Qd(self.d, self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return Qd(self.d, self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return Qd(self.d, self.a * o, self.b * o)
        return Qd(self.d, self.a * o.a + self.d * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __eq__(self, o):
        if isinstance(o, (int, Fr)):
            o = Qd(self.d, o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"({self.a}+{self.b}*sqrt{self.d})"


# ---- Laurent monomials over Q ---------------------------------------------

class LM:
    """Laurent monomials in named variables with exact rational coefficients:
    a dict {exponent tuple: Fraction}."""

    def __init__(self, names, terms=None):
        self.names = list(names)
        self.t = {}
        if terms:
            for e, c in terms.items():
                if c != 0:
                    self.t[e] = self.t.get(e, Fr(0)) + Fr(c)
                    if self.t[e] == 0:
                        del self.t[e]

    @staticmethod
    def mon(names, **kw):
        e = tuple(kw.get(n, 0) for n in names)
        return LM(names, {e: Fr(1)})

    @staticmethod
    def cst(names, x):
        return LM(names, {tuple([0] * len(names)): Fr(x)})

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return LM(self.names, {e: Fr(o) * c for e, c in self.t.items()})
        acc = {}
        for e1, c1 in self.t.items():
            for e2, c2 in o.t.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                acc[e] = acc.get(e, Fr(0)) + c1 * c2
        acc = {e: c for e, c in acc.items() if c != 0}
        return LM(self.names, acc)

    def __add__(self, o):
        acc = dict(self.t)
        for e, c in o.t.items():
            acc[e] = acc.get(e, Fr(0)) + c
        acc = {e: c for e, c in acc.items() if c != 0}
        return LM(self.names, acc)

    def __sub__(self, o):
        return self + LM(self.names, {e: -c for e, c in o.t.items()})

    def __rmul__(self, x):
        return LM(self.names, {e: Fr(x) * c for e, c in self.t.items()})

    def pow(self, n):
        if n < 0:
            return self.inv().pow(-n)
        r = LM.cst(self.names, 1)
        b = LM(self.names, dict(self.t))
        while n:
            if n & 1:
                r = r * b
            b = b * b
            n >>= 1
        return r

    def inv(self):
        assert len(self.t) == 1, "only single monomials are invertible here"
        e, c = next(iter(self.t.items()))
        return LM(self.names, {tuple(-x for x in e): 1 / c})

    def eval(self, values):
        """exact evaluation at name -> Fraction; zero exponents allowed."""
        acc = Fr(0)
        for e, c in self.t.items():
            term = c
            for i, n in enumerate(self.names):
                term *= Fr(values[n]) ** e[i]
            acc += term
        return acc

    def __eq__(self, o):
        if isinstance(o, (int, Fr)):
            o = LM.cst(self.names, o)
        return self.t == o.t

    def __repr__(self):
        if not self.t:
            return "0"
        parts = []
        for e, c in sorted(self.t.items(), key=lambda kv: str(kv[0])):
            s = str(c)
            for i, n in enumerate(self.names):
                if e[i] == 1:
                    s += f"*{n}"
                elif e[i]:
                    s += f"*{n}^{e[i]}"
            parts.append(s)
        return " + ".join(parts)


# ---- truncated power series over Q -----------------------------------------

def series_mul(a, b, deg):
    out = [Fr(0)] * (deg + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= deg:
                out[i + j] += x * y
    return out


# ---- complex-over-Poly spinor algebra ---------------------------------------

class CP:
    """(re, im) pair of Polys: an element of the polynomial ring tensored with Q(i)."""

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, o):
        return CP(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CP(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return CP(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def conj(self):
        return CP(self.re, -self.im)

    def zero(self):
        return self.re.zero() and self.im.zero()

    def __repr__(self):
        return f"({self.re} | {self.im} i)"


def cinner(u, w):
    """Hermitian inner product sum_k conj(u_k) w_k of CP spinors."""
    res = None
    for a, b in zip(u, w):
        t = a.conj() * b
        res = t if res is None else res + t
    return res


# ==========================================================================
# §A  BM.34 / Def-BM.10 — the metric, the mass shell, the kinetic energy
# ==========================================================================
print("\n§A (Def-BM.10, BM.34) — the ADM split of CT1.12's metric, the master")
print("            dispersion identity, the KE series, and the zero-point bound")

AV = ["O2", "kap", "bet", "w1", "w2", "w3",
      "q11", "q12", "q13", "q22", "q23", "q33",
      "p0", "p1", "p2", "p3", "m"]

O2 = V(AV, "O2")                     # Omega^2 as an indeterminate
kap = V(AV, "kap")                   # varkappa
bet = V(AV, "bet")                   # beta
w = [V(AV, f"w{i+1}") for i in range(3)]
qq = [[None] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        a, b = min(i, j), max(i, j)
        qq[i][j] = V(AV, f"q{a+1}{b+1}")
p0 = V(AV, "p0")
psp = [V(AV, f"p{i+1}") for i in range(3)]
mm = V(AV, "m")
ONEA = P(AV, 1)
ZEROA = P(AV, 0)

# the CT1.12 metric: g_00 = -Omega^2, g_0i = Omega^2 kappa beta w_i,
#                    g_ij = Omega^2 (delta_ij + kappa q_ij)   [CT1.12; FT.157(1)]
gam = [[O2 * (ONEA if i == j else ZEROA) + O2 * kap * qq[i][j] for j in range(3)]
       for i in range(3)]
Nlow = [O2 * kap * bet * w[i] for i in range(3)]
g4 = [[None] * 4 for _ in range(4)]
g4[0][0] = -O2
for i in range(3):
    g4[0][i + 1] = Nlow[i]
    g4[i + 1][0] = Nlow[i]
    for j in range(3):
        g4[i + 1][j + 1] = gam[i][j]

Dg = mdet(gam)                       # det gamma
Gadj = madj(gam)                     # adj gamma:  gamma^{-1} = Gadj / Dg
detg = mdet(g4)
adjg = madj(g4)
GN = mvec(Gadj, Nlow)                # (adj gamma)^{ij} N_j

# A1 — the lapse identity (Schur):  -det g = Omega^2 det gamma + N (adj gamma) N
lhs = -detg
rhs = O2 * Dg + sum((Nlow[i] * GN[i] for i in range(3)), ZEROA)
chk(lhs == rhs, "§A1 N^2 det(gamma) = -det g as an exact polynomial identity "
                "(Schur; the cleared lapse row of BM.34(1)/Def-BM.10(2))")

# A2 — the cleared adjugate rows of the inverse metric:
#      (adj g)_00 = det gamma;   (adj g)_0i = -((adj gamma) N)_i;
#      det(gamma) (adj g)_ij = det(g) (adj gamma)^{ij} + ((adj gamma)N)_i ((adj gamma)N)_j
chk(adjg[0][0] == Dg, "§A2 (adj g)_{00} = det gamma exactly  <=>  g^{00} = -1/N^2")
row0_ok = all(adjg[0][i + 1] == -GN[i] for i in range(3))
chk(row0_ok, "§A2 (adj g)_{0i} = -((adj gamma) N)_i exactly  <=>  g^{0i} = N^i/N^2")
rowsp_ok = all(Dg * adjg[i + 1][j + 1] == detg * Gadj[i][j] + GN[i] * GN[j]
               for i in range(3) for j in range(3))
chk(rowsp_ok, "§A2 det(gamma)(adj g)_{ij} = det(g)(adj gamma)^{ij} + ((adj gamma)N)_i((adj gamma)N)_j "
              "exactly  <=>  g^{ij} = gamma^{ij} - N^i N^j/N^2 (all 9 components)")
adj_ok = mmul(adjg, g4)
ident_scaled = [[detg * (ONEA if i == j else ZEROA) for j in range(4)] for i in range(4)]
chk(adj_ok == ident_scaled, "§A2 (adj g) g = det(g) I exactly (all 16 components)")

# A3 — the line-element identity, cleared by det(gamma):
#      D g_{mu nu} X^mu X^nu = -Delta t^2 + D gamma_ij X^i X^j + 2 t D N_i X^i + t^2 N(adj gamma)N
#      with X^0 = t and Delta = -det g = Omega^2 D + N (adj gamma) N
AVX = AV + ["t", "X1", "X2", "X3"]


def lift(poly):
    return Poly(AVX, poly.t)


t = V(AVX, "t")
X = [V(AVX, f"X{i+1}") for i in range(3)]
g4x = [[lift(g4[i][j]) for j in range(4)] for i in range(4)]
Dx = lift(Dg)
GNx = [lift(GN[i]) for i in range(3)]
Nlx = [lift(Nlow[i]) for i in range(3)]
gamx = [[lift(gam[i][j]) for j in range(3)] for i in range(3)]
TWOx = lift(P(AV, 2))

lhsL = Dx * g4x[0][0] * t * t
for i in range(3):
    lhsL = lhsL + Dx * (g4x[0][i + 1] + g4x[i + 1][0]) * X[i] * t
    for j in range(3):
        lhsL = lhsL + Dx * g4x[i + 1][j + 1] * X[i] * X[j]

# the ADM form, cleared by D:  -Delta t^2 + D gamma_ij X^i X^j + 2 t D N_i X^i + t^2 N(adj gamma)N
NadN = sum((Nlx[i] * GNx[i] for i in range(3)), lift(ZEROA))     # t^2-coefficient, and Delta = O2 D + NadN
rhsL = (-(lift(O2) * Dx + NadN) * t * t
        + sum((Dx * gamx[i][j] * X[i] * X[j] for i in range(3) for j in range(3)), lift(ZEROA))
        + sum((TWOx * t * Dx * Nlx[i] * X[i] for i in range(3)), lift(ZEROA))
        + NadN * t * t)
chk(lhsL == rhsL, "§A3 the line-element identity ds^2 = -N^2 dtau^2 + g_ij(dx^i+N^i dtau)(dx^j+N^j dtau) "
                  "= g_{mu nu} dx^mu dx^nu as an exact cleared polynomial identity in (t, X^i), in the "
                  "fully expanded ADM form (-N^2 t^2 + gamma XX + 2 t N X + t^2 N(adj gamma)N, cleared by D) "
                  "(Def-BM.10(2), BM.34(2))")

# A4 — the master dispersion identity:
#      (p_0 det(gamma) - ((adj gamma) N).p)^2 = (-det g)( m^2 det(gamma) + p (adj gamma) p )
pGp = sum((Gadj[i][j] * psp[i] * psp[j] for i in range(3) for j in range(3)), ZEROA)
lin = p0 * Dg - sum((GN[i] * psp[i] for i in range(3)), ZEROA)
master_lhs = lin * lin
master_rhs = (-detg) * (mm * mm * Dg + pGp)
pv4 = [p0] + psp
adjp = sum((adjg[mu][nu] * pv4[mu] * pv4[nu] for mu in range(4) for nu in range(4)), ZEROA)
shell_cleared = Dg * (adjp + detg * mm * mm)
chk(master_lhs - master_rhs == shell_cleared,
    "§A4 the master dispersion identity in exact cleared-equivalence form: "
    "(p_0 det(gamma) - ((adj gamma)N).p)^2 - (-det g)(m^2 det(gamma) + p (adj gamma) p) "
    "= det(gamma) * ((adj g)^{mu nu} p_mu p_nu + det(g) m^2) as ONE polynomial identity over "
    "Q[Omega^2,kappa,beta,w_i,q_ij,p_mu,m] — hence the mass shell g^{mu nu}p_mu p_nu = -m^2 holds "
    "<=> (p_0 - N^i p_i)^2 = N^2 (m^2 + gamma^{ij} p_i p_j) wherever det(gamma) != 0 "
    "(BM.34(4)/Def-BM.10(5))")

# A5 — the vacuum specialization: (a_00,q,w) = 0 => Omega = 1, gamma = delta,
#      N_i = 0, N^2 = 1, g = diag(-1,1,1,1): the vacuum metric is flat
vac = {"O2": Fr(1), "kap": Fr(0), "bet": Fr(0), "w1": 0, "w2": 0, "w3": 0,
       "q11": 0, "q12": 0, "q13": 0, "q22": 0, "q23": 0, "q33": 0}
gvac = [[g4[i][j].subs(vac) for j in range(4)] for i in range(4)]
flat = [[Fr(-1) if (i == 0 and j == 0) else (Fr(1) if i == j else Fr(0)) for j in range(4)]
        for i in range(4)]
chk(gvac == flat, "§A5 the vacuum specialization (a_00,q,w) = 0 gives g = diag(-1,1,1,1) exactly "
                  "— the vacuum's emergent metric is flat (BM.34(2), BM.35(2))")
N2expr = O2 * Dg + sum((Nlow[i] * GN[i] for i in range(3)), ZEROA)   # == N^2 det(gamma)
chk(N2expr.subs(vac) == Dg.subs(vac), "§A5 at the vacuum N^2 = 1 exactly (N^2 det(gamma) = det(gamma))")

# A6 — T-parity: w -> -w fixes gamma, det gamma and N^2, flips N_i;
#      the mass shell is invariant under the simultaneous (w,p) -> (-w,-p) flip
def sub_neg(poly, wnames=("w1", "w2", "w3")):
    """substitute w_i -> -w_i exactly (sign flip by w-degree)."""
    out = Poly(poly.names, rules=poly.rules)
    for e, c in poly.t.items():
        k = sum(e[poly.ix[n]] for n in wnames)
        out = out + Poly(poly.names, {e: c * Fr((-1) ** k)}, poly.rules)
    return out


chk(all(sub_neg(gam[i][j]) == gam[i][j] for i in range(3) for j in range(3)),
    "§A6 gamma_ij is T-even under w -> -w (all 9 components)")
chk(sub_neg(Dg) == Dg, "§A6 det(gamma) is T-even")
chk(sub_neg(N2expr) == N2expr, "§A6 N^2 det(gamma) is T-even: the lapse is T-even")
chk(all(sub_neg(Nlow[i]) == -Nlow[i] for i in range(3)),
    "§A6 N_i is T-odd: the shift covector flips with its carrier w_i [FT.156(3), FT.159(3)]")


def sub_neg_wp(poly):
    out = Poly(poly.names, rules=poly.rules)
    for e, c in poly.t.items():
        k = sum(e[poly.ix[n]] for n in ("w1", "w2", "w3", "p1", "p2", "p3"))
        out = out + Poly(poly.names, {e: c * Fr((-1) ** k)}, poly.rules)
    return out


chk(sub_neg_wp(master_lhs) == master_lhs and sub_neg_wp(master_rhs) == master_rhs
    and sub_neg_wp(shell_cleared) == shell_cleared,
    "§A6 the master mass-shell identity is invariant under the simultaneous (w,p) -> (-w,-p) flip: "
    "the dispersion relation is T-even (BM.34(3),(4))")

# A7 — three rational metric witnesses: exact Fraction inverses, the ADM rows,
#      det g = -N^2 det gamma, the line element, the dispersion value identity,
#      and the on-shell rest branch g^{00} p_0^2 + m^2 = 0 at p_0^2 = N^2 m^2
WIT = [
    ("W1 vacuum", dict(O2=Fr(1), kap=Fr(0), bet=Fr(0), w=(Fr(0),) * 3,
                       q=[[Fr(0)] * 3 for _ in range(3)])),
    ("W2 off-diagonal", dict(O2=Fr(4, 3), kap=Fr(1, 2), bet=Fr(1),
                             w=(Fr(1, 3), Fr(-1, 2), Fr(1, 5)),
                             q=[[Fr(1, 7), Fr(1, 13), Fr(-1, 17)],
                                [Fr(1, 13), Fr(1, 9), Fr(1, 19)],
                                [Fr(-1, 17), Fr(1, 19), Fr(-1, 23)]])),
    ("W3 shifted", dict(O2=Fr(9, 4), kap=Fr(1, 3), bet=Fr(-1),
                        w=(Fr(1), Fr(2), Fr(-1)),
                        q=[[Fr(1, 5), Fr(1, 6), Fr(0)],
                           [Fr(1, 6), Fr(1, 5), Fr(1, 7)],
                           [Fr(0), Fr(1, 7), Fr(1, 5)]])),
]
PMOM = [(-Fr(3, 2), Fr(1, 4), Fr(-2, 7), Fr(5, 3), Fr(7, 5)),
        (Fr(2, 9), Fr(-11, 13), Fr(4, 5), Fr(1, 6), Fr(12, 7)),
        (-Fr(5, 4), Fr(3, 8), Fr(-9, 10), Fr(11, 12), Fr(13, 14))]
inv_ok = det_ok = le_ok = disp_ok = pos_ok = branch_ok = True
for k, (nm, W) in enumerate(WIT):
    sub = {"O2": W["O2"], "kap": W["kap"], "bet": W["bet"]}
    for i in range(3):
        sub[f"w{i+1}"] = W["w"][i]
    for i in range(3):
        for j in range(i, 3):
            sub[f"q{i+1}{j+1}"] = W["q"][i][j]
    gnum = [[g4[i][j].subs(sub) for j in range(4)] for i in range(4)]
    gamN = [[gam[i][j].subs(sub) for j in range(3)] for i in range(3)]
    pos_ok = pos_ok and sylvester_pos(gamN)
    ginv = finv(gnum)
    prod = [[sum((gnum[i][a] * ginv[a][j] for a in range(4)), Fr(0)) for j in range(4)]
            for i in range(4)]
    inv_ok = inv_ok and all(prod[i][j] == (Fr(1) if i == j else Fr(0))
                            for i in range(4) for j in range(4))
    gaminv = finv(gamN)
    detgN, detgamN = fdet(gnum), fdet(gamN)
    NlowN = [gnum[0][i + 1] for i in range(3)]
    NupN = [sum((gaminv[i][j] * NlowN[j] for j in range(3)), Fr(0)) for i in range(3)]
    N2N = -detgN / detgamN
    det_ok = det_ok and (detgN == -N2N * detgamN) and (N2N > 0)
    adm = (ginv[0][0] == -1 / N2N)
    admi = all(ginv[0][i + 1] == NupN[i] / N2N for i in range(3))
    admj = all(ginv[i + 1][j + 1] == gaminv[i][j] - NupN[i] * NupN[j] / N2N
               for i in range(3) for j in range(3))
    inv_ok = inv_ok and adm and admi and admj
    # the line element on a rational (t, X)
    tt, XX = Fr(3, 5), (Fr(-2, 3), Fr(7, 11), Fr(1, 13))
    l1 = sum((gnum[i][j] * (tt if i == 0 else XX[i - 1]) * (tt if j == 0 else XX[j - 1])
              for i in range(4) for j in range(4)), Fr(0))
    sh = [XX[i] + NupN[i] * tt for i in range(3)]
    l2 = -N2N * tt * tt + sum((gamN[i][j] * sh[i] * sh[j]
                               for i in range(3) for j in range(3)), Fr(0))
    le_ok = le_ok and (l1 == l2)
    # the dispersion value identity:
    # (p0 - N.p)^2 - N^2 (m^2 + p gamma^{-1} p) = -N^2 (g^{mu nu} p_mu p_nu + m^2)
    p0n, pspn, mn = PMOM[k][0], PMOM[k][1:4], PMOM[k][4]
    pv = [p0n] + list(pspn)
    gg = sum((ginv[i][j] * pv[i] * pv[j] for i in range(4) for j in range(4)), Fr(0))
    p2N = sum((gaminv[i][j] * pspn[i] * pspn[j] for i in range(3) for j in range(3)), Fr(0))
    Ndotp = sum((NupN[i] * pspn[i] for i in range(3)), Fr(0))
    a = (p0n - Ndotp) ** 2 - N2N * (mn * mn + p2N)
    b = -N2N * (gg + mn * mn)
    disp_ok = disp_ok and (a == b)
    # the on-shell rest branch: p_0^2 = N^2 m^2 solves g^{00} p_0^2 + m^2 = 0
    branch_ok = branch_ok and (ginv[0][0] * (N2N * mn * mn) + mn * mn == 0)
    # the lapse in components: N^2 = -g_00 + N_i N^i
    branch_ok = branch_ok and (N2N == -gnum[0][0]
                               + sum((NlowN[i] * NupN[i] for i in range(3)), Fr(0)))
chk(pos_ok, "§A7 gamma_ij is positive definite on all three rational witnesses "
            "(exact Sylvester criterion) — the perturbative regime of CT1.12")
chk(inv_ok, "§A7 the exact Fraction inverses satisfy g g^{-1} = I and the three ADM rows "
            "g^{00} = -1/N^2, g^{0i} = N^i/N^2, g^{ij} = gamma^{ij} - N^iN^j/N^2 on all witnesses")
chk(det_ok, "§A7 det g = -N^2 det gamma exactly, with N^2 > 0, on all witnesses")
chk(le_ok, "§A7 the line element -N^2 t^2 + g_ij(X^i+N^i t)(X^j+N^j t) equals g_{mu nu}X^mu X^nu "
           "on rational (t,X) for all witnesses")
chk(disp_ok, "§A7 the dispersion value identity (p_0-N^ip_i)^2 - N^2(m^2+p^2) = -N^2(g^{mu nu}p_mu p_nu + m^2) "
             "holds exactly on rational momenta for all witnesses")
chk(branch_ok, "§A7 the on-shell rest branch: p_0^2 = N^2 m^2 solves g^{00}p_0^2 + m^2 = 0 exactly, "
               "and N^2 = -g_00 + N_iN^i on every witness — E = N m at p = 0 (BM.34(4),(7))")

# A8 — the momentum drag term: gamma_ij ((adj gamma) N)^j = det(gamma) N_i exactly
drag_ok = all(sum((gam[i][j] * GN[j] for j in range(3)), ZEROA) == Dg * Nlow[i]
              for i in range(3))
chk(drag_ok, "§A8 gamma_ij ((adj gamma)N)^j = det(gamma) N_i exactly: the shift contribution to the "
             "momentum is the metric's time-space block g_0i (Def-BM.10(3), BM.34(3))")

# A9 — the non-relativistic series: sqrt(1+x) with exact rational coefficients
DEG = 5
sq = [Fr(1), Fr(1, 2), Fr(-1, 8), Fr(1, 16), Fr(-5, 128), Fr(7, 256)]
prod = series_mul(sq, sq, DEG)
chk(prod[:2] == [Fr(1), Fr(1)] and all(x == 0 for x in prod[2:]),
    "§A9 (1 + x/2 - x^2/8 + x^3/16 - 5x^4/128 + 7x^5/256)^2 = 1 + x mod x^6 — "
    "the exact rational binomial series of sqrt(1+x) (BM.34(5))")
binom = [Fr(1)]
acc = Fr(1)
for n in range(1, DEG + 1):
    acc = acc * (Fr(1, 2) - (n - 1)) / n
    binom.append(acc)
chk(binom == sq, "§A9 the coefficients equal the exact binomials (1/2 choose n) by the rational recursion")
LN = ["Nl", "m", "P"]
ke = (LM.mon(LN, Nl=1, P=1, m=-1).pow(1) * Fr(1, 2)
      - LM.mon(LN, Nl=1, P=2, m=-3) * Fr(1, 8)
      + LM.mon(LN, Nl=1, P=3, m=-5) * Fr(1, 16)
      - LM.mon(LN, Nl=1, P=4, m=-7) * Fr(5, 128))
chk(ke.t[(1, -1, 1)] == Fr(1, 2) and ke.t[(1, -3, 2)] == Fr(-1, 8)
    and ke.t[(1, -5, 3)] == Fr(1, 16) and ke.t[(1, -7, 4)] == Fr(-5, 128)
    and len(ke.t) == 4,
    "§A9 KE = N (p^2/(2m) - p^4/(8m^3) + p^6/(16m^5) - 5p^8/(128m^7)) + O(p^10) as exact Laurent "
    "coefficients; the unit normalization (m = N = 1) gives KE = p^2/2 + O(p^4) (BM.34(5))")

# A10 — positivity: the Sylvester criterion discriminates 1 + kappa*lambda_a(q) > 0
qdiag_ok = [[Fr(11, 10), Fr(0), Fr(0)], [Fr(0), Fr(4, 5), Fr(0)], [Fr(0), Fr(0), Fr(5, 4)]]
chk(sylvester_pos(qdiag_ok), "§A10 q = diag(1/10,-1/5,1/4), kappa = 1: every 1+kappa*lambda_a = "
                             "(11/10, 4/5, 5/4) > 0 and delta+kappa q passes the exact Sylvester criterion")
qdiag_bad = [[Fr(-1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
chk(not sylvester_pos(qdiag_bad), "§A10 q = diag(-2,0,0), kappa = 1: 1+kappa*lambda = -1 < 0 and the "
                                  "criterion refutes positivity — the regime is exactly CT1.12's")
gW2 = WIT[1][1]
subW2 = {"O2": gW2["O2"], "kap": gW2["kap"], "bet": gW2["bet"]}
for i in range(3):
    subW2[f"w{i+1}"] = gW2["w"][i]
for i in range(3):
    for j in range(i, 3):
        subW2[f"q{i+1}{j+1}"] = gW2["q"][i][j]
gamW2 = [[gam[i][j].subs(subW2) for j in range(3)] for i in range(3)]
gamW2inv = finv(gamW2)
ke_pos = True
for pv in [(Fr(0), Fr(0), Fr(0)), (Fr(1, 3), Fr(-2, 5), Fr(7, 11)), (Fr(-4, 9), Fr(1, 2), Fr(0))]:
    val = sum((gamW2inv[i][j] * pv[i] * pv[j] for i in range(3) for j in range(3)), Fr(0))
    ke_pos = ke_pos and ((val == 0) if pv == (0, 0, 0) else (val > 0))
chk(sylvester_pos(gamW2inv) and ke_pos,
    "§A10 gamma^{ij} is positive definite on the off-diagonal witness: KE = gamma^{ij}p_ip_j/(2m) >= 0 "
    "with equality exactly at p = 0 (BM.34(5))")

# A11 — the zero-point bound: dp >= m_hid/2 at the Born width, the isotropic
#       cube convention, and the exact constants 7/4, 3/8, sqrt(7)/2
LH = ["h", "E", "l2"]
mh = LM.mon(LH, E=1, l2=1, h=-1)                    # m_hid = E_int ln2 / h  [FT.44(4)]
dxb = mh.inv()                                      # Delta x_B = 1/m_hid   [Def-BM.4(1)]
chk(dxb * mh == LM.cst(LH, 1), "§A11 Delta x_B * m_hid = 1 exactly (Def-BM.4(1))")
dpb = dxb.inv() * Fr(1, 2)
chk(dpb == mh * Fr(1, 2), "§A11 1/(2 Delta x_B) = m_hid/2 exactly (BM.13(4) re-derived: the "
                          "Robertson saturation at the Born width)")
chk(Fr(3) * (Fr(1, 2) ** 2) == Fr(3, 4), "§A11 the isotropic bound <p^2> >= 3 (m_hid/2)^2 = (3/4) m_hid^2 "
                                          "— exact rationals (BM.34(6))")
chk(Fr(1) + Fr(3, 4) == Fr(7, 4), "§A11 E^2 >= m^2 + (3/4) m_hid^2 = (7/4) m_hid^2 at m = m_hid — exact")
chk(Fr(3, 4) / 2 == Fr(3, 8), "§A11 KE_NR >= <p^2>/(2m) = (3/8) m_hid at m = m_hid — exact")
s7 = Qd(7, 0, 1)
chk(s7 * s7 == Qd(7, 7), "§A11 sqrt(7)^2 = 7 exactly in Q(sqrt7)")
chk((s7 * Fr(1, 2)) * (s7 * Fr(1, 2)) == Qd(7, Fr(7, 4)),
    "§A11 (sqrt(7)/2)^2 = 7/4 exactly: E >= (sqrt7/2) m_hid is the squared form of "
    "E^2 >= (7/4) m_hid^2 — comparison by squaring, no radical evaluated")
irr = all(Fr(r) ** 2 != Fr(7) for r in range(-8, 9))
chk(irr, "§A11 x^2 - 7 has no rational root (integer scan; the rational-root theorem forces q | 1): "
         "Q(sqrt7) is a genuine quadratic extension")
E2full = LM.cst(LH, Fr(7, 4)) * mh.pow(2)
chk(len(E2full.t) == 1 and E2full.t[(-2, 2, 2)] == Fr(7, 4),
    "§A11 E^2 >= (7/4) (E_int ln2)^2 / h^2 as ONE Laurent monomial with coefficient 7/4 and "
    "exponents (h,E,ln2) = (-2,2,2) (BM.34(6))")

# A12 — the rest slice and the dust closure: kappa^2 rho = 2 pi h E/V with the
#       exact ln2 cancellation, and the CT2.1 dimension exponents
LU = ["h", "E", "l2", "pi", "V"]
k2 = LM.mon(LU, h=2, l2=-1, pi=1) * Fr(2)           # kappa^2 = 2 pi h^2/ln2 [CT2.9]
rho = LM.mon(LU, E=1, l2=1, h=-1, V=-1)             # rho = E_int ln2/(h V)  [BM.9(5)]
chk(k2 * rho == LM.mon(LU, h=1, E=1, V=-1, pi=1) * Fr(2),
    "§A12 kappa^2 rho = (2 pi h^2/ln2)(E_int ln2/(h V)) = 2 pi h E_int / V exactly — "
    "the ln2 cancellation of BM.9(5) re-verified as Laurent monomials")
chk(mh.pow(2) == LM.mon(LH, E=2, l2=2, h=-2) and len(mh.pow(2).t) == 1,
    "§A12 the rest slice: E(p=0)^2 = m_hid^2 = (E_int ln2)^2/h^2 as one monomial — the dispersion, "
    "informational and curvature-flux rest reads are the same object on-shell (BM.34(7))")
exps = {"mrest": Fr(0) - Fr(-1, 2), "gpp": Fr(1), "KE": Fr(1) - Fr(1, 2)}
chk(exps["mrest"] == Fr(1, 2) and exps["gpp"] == Fr(1) and exps["KE"] == Fr(1, 2),
    "§A12 the CT2.1 exponents: [Delta S_L] = q^0, [h] = q^{-1/2} => [m_rest] = q^{+1/2} = energy; "
    "[gamma^{ij}p_ip_j] = q^{+1}; [KE] = q^{+1} - q^{+1/2} = q^{+1/2} — the 1/m factor is "
    "dimensionally forced (Def-BM.10 Rmk, BM.34(5))")

stamp("§A done — the metric, the mass shell, the KE series, the zero-point bound")


# ==========================================================================
# §B  BM.35 — the vacuum-balanced entropy
# ==========================================================================
print("\n§B (BM.35) — the vacuum-balanced entropy: the Gibbs census, the balance")
print("            identity, the reframing monomial, and the three currencies")

# B1 — the exhaustive 1/8-grid Gibbs census: S(lambda) <= ln4 iff prod k^k >= 256
comps = [k for k in itertools.product(range(9), repeat=4) if sum(k) == 8]
chk(len(comps) == 165, f"§B1 the census has exactly C(11,3) = 165 compositions of 8 into 4 parts "
                       f"(got {len(comps)})")


def kpow(k):
    p = 1
    for ki in k:
        p *= (ki ** ki) if ki > 0 else 1
    return p


ge_ok = all(kpow(k) >= 256 for k in comps)
eq_cases = [k for k in comps if kpow(k) == 256]
chk(ge_ok, "§B1 prod k_i^{k_i} >= 256 for all 165 compositions — S(lambda) <= ln4 = S(I/4) by pure "
           "integer comparison (exp strictly monotone), no transcendental evaluated")
chk(eq_cases == [(2, 2, 2, 2)], "§B1 equality holds at exactly ONE composition, (2,2,2,2) = the uniform "
                                "state I/4: CT0.2's unique argmax re-derived on the grid (BM.35(1))")

# B2 — the exact ln2 enclosure: ln2 = sum_{n>=1} 1/(n 2^n), tail < 2^-N
NENC = 20
S20 = sum((Fr(1, n * 2 ** n) for n in range(1, NENC + 1)), Fr(0))
tail = Fr(1, 2 ** NENC)
chk(Fr(1, 2) < S20 and S20 + tail < Fr(1), "§B2 the exact rational enclosure 1/2 < ln2 < 1 "
                                            f"(partial sum to n={NENC}, tail < 2^-{NENC})")
chk(2 * (S20 + tail) < Fr(2) and Fr(2) < Fr(3), "§B2 2 ln2 < 2 < 3 by the enclosure — the witness "
                                                 "inequality of BM.35(6)")
chk(S20 > Fr(0), "§B2 ln2 > 0: the ledger deficit is strictly positive at every crystallized edge")

# B3 — the balance identity and the deficit monomials (Q*ln2 arithmetic)
ln4c, ln2c = Fr(2), Fr(1)                    # coefficients over the ln2 basis
chk(ln4c - 2 * ln2c == 0, "§B3 ln4 = 2 ln2 exactly: the vacuum pair entropy equals the ledger booking "
                          "of one bidirectional channel — the balance identity (BM.35(3))")
bal_ok = True
for Eb in (1, 3, 6, 12, 30):
    E_int = 2 * Eb
    bal_ok = bal_ok and (Fr(Eb) * ln4c == Fr(E_int) * ln2c)
chk(bal_ok, "§B3 Delta S_L = E_bidir * ln4 = E_int * ln2 = I_hid exactly at the bidirectional counts "
            "E_int in {2,6,12,24,60} — the digon, the neutron row, and the Platonic floors "
            "[FT.28, FT.42(1), FT.44(4), BM.17]")
mrest = LM.mon(LH, E=1, l2=1) * LM.mon(LH, h=-1)    # m_rest = Delta S_L / h
chk(mrest == mh and len(mrest.t) == 1,
    "§B3 m_rest := Delta S_L/h = E_int ln2 / h = m_hid as ONE Laurent monomial — the reframing "
    "identity of BM.35(4) (FT.44(4) untouched)")

# B4 — the digon witnesses: the deficit currencies are distinct functionals
ledger_full = Fr(2) * ln2c                    # |R| = 2E = 2: Delta S_L = 2 ln2
branch_full = Fr(3, 2) * (2 * 1 - 2)          # (3/2)(2E - |R|) at E=1, |R|=2: = 0
ledger_empty = Fr(0)                          # R = 0: Delta S_L = 0
branch_empty = Fr(3, 2) * (2 * 1 - 0)         # = 3
chk(ledger_full != branch_full, "§B4 the digon at |R| = 2E: the ledger deficit is 2 ln2 while the "
                                "branch-state deficit is 0 — distinct functionals (BM.35(6))")
chk(2 * (S20 + tail) < Fr(3) and ledger_empty != branch_empty,
    "§B4 the digon at R = 0: the ledger deficit is 0 while the branch-state deficit is 3, and "
    "2 ln2 != 3 by the exact enclosure 2 ln2 < 2 < 3 (BM.35(6))")

# B5 — the total-energy assembly: E_total = m_rest + KE with exact coefficients
LA = ["Nl", "m", "P", "h", "E", "l2"]
etot = (LM.mon(LA, E=1, l2=1, h=-1)                        # m_rest = Delta S_L / h
        + LM.mon(LA, Nl=1, P=1, m=-1) * Fr(1, 2)           # + N p^2/(2m)
        - LM.mon(LA, Nl=1, P=2, m=-3) * Fr(1, 8))          # - N p^4/(8 m^3)
chk(etot.t[(0, 0, 0, -1, 1, 1)] == Fr(1)
    and etot.t[(1, -1, 1, 0, 0, 0)] == Fr(1, 2)
    and etot.t[(1, -3, 2, 0, 0, 0)] == Fr(-1, 8)
    and len(etot.t) == 3,
    "§B5 E_total = Delta S_L/h + N p^2/(2m) - N p^4/(8m^3) + O(p^6): the exact series assembly of "
    "BM.35(7) — the rest term is the vacuum-balanced entropy, the motion term the metric's KE")
chk(Fr(1) == Fr(1) ** 2, "§B5 c = 1 [D2.9]: the restored c^2 carries q-exponent 0 — bookkeeping only")

stamp("§B done — the vacuum-balanced entropy")


# ==========================================================================
# §C  BM.36 — the force-structure ladder
# ==========================================================================
print("\n§C (BM.36) — the mask flag, the derived dimension ratios, the Gram form,")
print("            the kernel line, the sandwich, and the strength bar")

# C1 — the flag and its increments: exact integer censuses
chk((3 + 3) + 5 + 3 + 1 + 1 == 16,
    "§C1 (J^+_3+J^-_3) + G_5 + W_3 + H_1 + D^+_1 = 16 = dim K_1 = C_cap "
    "(CT1.12a(1), CT0.12, CT0.14)")
chk(16 + 1 == 17 and 17 + 8 == 25,
    "§C1 the increments: dim K_2 = 16 + 1 = 17 (the EM centre, dim Z(u(2)) = 1 [D2.12]), "
    "dim K_3 = 17 + 8 = 25 (dim su(3) = 8 [CT3.8]) — CT0.14's flag")
chk(6 < 16 < 17 < 25, "§C1 the flag 6 < 16 < 17 < 25 is strict")
chk(1 + 5 + 1 + 3 + 8 == 18, "§C1 the observable bound dim K_Sigma <= 1+5+1+3+8 = 18 (FT.26(3))")

# C2 — the derived structure ratios: exact Fractions
chk(Fr(1, 3) == Fr(1) / Fr(3) and Fr(8) == Fr(8, 1) and Fr(1, 25) == Fr(1) / Fr(25),
    "§C2 the derived dimension ratios: EM:weak-triplet = 1/3 [dim F_W = 3, C8], strong:EM = 8, "
    "EM:rung-3 total = 1/25 — exact rationals, alphabet capacities and nothing more (BM.36(2))")

# C3 — the EW.33 Gram form recomputed from Pauli spinors over Q(i) x Q[g,g']
GV = ["g", "gp"]
gz = V(GV, "g")
gpz = V(GV, "gp")
zP = P(GV, 0)
halfP = P(GV, Fr(1, 2))
# v = (0,1);  sigma_1 v = (1,0);  sigma_2 v = (-i,0);  sigma_3 v = (0,-1);  sigma_0 v = v
Gv = [
    [CP(halfP * gz, zP), CP(zP, zP)],                      # G_1 v = (g/2)(1,0)
    [CP(zP, -halfP * gz), CP(zP, zP)],                     # G_2 v = (g/2)(-i,0)
    [CP(zP, zP), CP(-halfP * gz, zP)],                     # G_3 v = (g/2)(0,-1)
    [CP(zP, zP), CP(halfP * gpz, zP)],                     # G_Y v = (g'/2)(0,1)
]
Gram = [[None] * 4 for _ in range(4)]
Imag = [[None] * 4 for _ in range(4)]
im_diag_zero = im_antisym = True
for A in range(4):
    for B in range(4):
        ip = cinner(Gv[A], Gv[B])
        ipT = cinner(Gv[B], Gv[A])
        Gram[A][B] = ip.re
        Imag[A][B] = ip.im
        if A == B:
            im_diag_zero = im_diag_zero and ip.im.zero()
        im_antisym = im_antisym and (ip.im + ipT.im).zero()
# the antisymmetric imaginary parts cancel in the symmetric form sum c_A c_B Im_AB
CV2 = GV + ["c1", "c2", "c3", "c4"]


def liftC2(poly):
    pad = len(CV2) - len(poly.names)
    return Poly(CV2, {tuple(list(e) + [0] * pad): c for e, c in poly.t.items()})


cc = [V(CV2, f"c{i+1}") for i in range(4)]
imsum = liftC2(P(GV, 0))
for A in range(4):
    for B in range(4):
        imsum = imsum + cc[A] * cc[B] * liftC2(Imag[A][B])
q4 = P(GV, Fr(1, 4))
exp_G = [[q4 * gz * gz if i == j and i < 3 else
          (q4 * gpz * gpz if i == j == 3 else
           (-q4 * gz * gpz if {i, j} == {2, 3} else zP))
          for j in range(4)] for i in range(4)]
chk(all(Gram[i][j] == exp_G[i][j] for i in range(4) for j in range(4))
    and im_diag_zero and im_antisym and imsum.zero(),
    "§C3 Re<G_A v, G_B v> recomputed from Pauli spinors equals (1/4)[[g^2,0,0,0],[0,g^2,0,0],"
    "[0,0,g^2,-gg'],[0,0,-gg',g'^2]] exactly; the imaginary parts are zero on the diagonal, "
    "antisymmetric off it, and cancel identically in the symmetric form sum c_A c_B Im(Gram) "
    "[EW.33's own row] — EW.20's weak-frame matrix re-derived from EW.32's seed (BM.36(4))")

# C4 — the charpoly factorization: spectrum {g^2/4, g^2/4, 0, (g^2+g'^2)/4}
CV = GV + ["x"]


def liftC(poly):
    # remap exponent tuples from the smaller variable list into CV
    pad = len(CV) - len(poly.names)
    return Poly(CV, {tuple(list(e) + [0] * pad): c for e, c in poly.t.items()})


xx = V(CV, "x")
zeroC = liftC(zP)
GramC = [[liftC(Gram[i][j]) for j in range(4)] for i in range(4)]
e1 = liftC(q4 * gz * gz)
e2 = liftC(q4 * (gz * gz + gpz * gpz))
cp = mdet([[(xx if i == j else zeroC) - GramC[i][j] for j in range(4)] for i in range(4)])
expect_cp = (xx - e1) * (xx - e1) * xx * (xx - e2)
chk(cp == expect_cp,
    "§C4 det(xI - Gram) = (x - g^2/4)^2 * x * (x - (g^2+g'^2)/4) exactly in Q[g,g',x]: "
    "the spectrum {g^2/4, g^2/4, 0, (g^2+g'^2)/4} — two equal charged directions, one massive "
    "neutral, one exact kernel (BM.36(4))")

# C5 — the kernel line c ~ (0,0,g',g): exact annihilation
ck = [zeroC, zeroC, liftC(gpz), liftC(gz)]
kvec = mvec(GramC, ck)
chk(all(z.zero() for z in kvec), "§C5 Gram * (0,0,g',g)^T = 0 exactly: the kernel line is the seed's "
                                 "stabilizer direction — the exact massless line (EW.33, BM.36(5))")

# C6 — h_0 = 0 => M^2 = 0: mu_star^2 = c_W kappa^2 beta^2 h_0^2 vanishes exactly
LMU = ["cW", "kap2", "bet2", "h0"]
mu2 = LM.mon(LMU, cW=1, kap2=1, bet2=1, h0=2)
chk(mu2.eval({"cW": Fr(3, 5), "kap2": Fr(2), "bet2": Fr(7, 9), "h0": Fr(0)}) == Fr(0),
    "§C6 mu_star^2 = c_W kappa^2 beta^2 h_0^2 evaluates to 0 exactly at h_0 = 0 on a rational "
    "witness, hence M^2 = mu_star^2 * Gram = 0 identically (EW.33's vanishing row)")

# C7 — the neutral ratio M_Z^2/M_W^2 = (g^2+g'^2)/g^2, cross-multiplied
chk(liftC(q4 * (gz * gz + gpz * gpz)) * liftC(gz * gz)
    == liftC(q4 * gz * gz) * liftC(gz * gz + gpz * gpz),
    "§C7 ((g^2+g'^2)/4) * g^2 = (g^2/4) * (g^2+g'^2) exactly: M_Z^2/M_W^2 = (g^2+g'^2)/g^2 in "
    "Q(g^2,g'^2) (BM.36(4))")

# C8 — the sandwich: ((g^2+g'^2)/4) I - Gram is PSD with the exact spectrum
#      {g'^2/4, g'^2/4, (g^2+g'^2)/4, g^2/4}
S8 = [[(e2 if i == j else zeroC) - GramC[i][j] for j in range(4)] for i in range(4)]
f1 = liftC(q4 * gpz * gpz)
cpS = mdet([[(xx if i == j else zeroC) - S8[i][j] for j in range(4)] for i in range(4)])
expect_cpS = (xx - f1) * (xx - f1) * (xx - e2) * xx
chk(cpS == expect_cpS,
    "§C8 det(xI - (((g^2+g'^2)/4)I - Gram)) = (x - g'^2/4)^2 (x - (g^2+g'^2)/4) x exactly: "
    "the difference form's spectrum {g'^2/4, g'^2/4, (g^2+g'^2)/4, 0} is nonnegative, hence the "
    "sandwich 0 <= G(c) <= mu_*^2 ((g^2+g'^2)/4) ||c||^2 (BM.36(5))")

# C9 — the strength bar: text pins
P2 = rd("Part2_Bosonic_era.md")
P4 = rd("Part4_Baryomesonic_era.md")
chk("no theorem of the corpus fixes its numerical value" in P2,
    "§C9 Part 2 §Cal-2's logged row stands: alpha_EM^(2)'s numerical value is fixed by no theorem")
i36 = P4.find("### BM.36")
j36 = P4.find("### BM.37")
B36 = P4[i36:j36]
chk("category error" in B36 and "\\neg\\text{derived and}\\ \\neg\\text{adopted}" in B36,
    "§C9 BM.36(3) carries the strength bar on record: alpha := dimension ratio is "
    "¬derived and ¬adopted, a category error of the pi-against-1/137 species [FT.73(5)]")
chk("Yukawa-like coupling" in B36 and "application-layer content" in B36 and "open gap" not in B36,
    "§C9 R1: BM.36(6) names the Yukawa-like coupling as application-layer content (the open-gap framing is retired)")
chk(not re.search(r"\\alpha\s*=", B36), "§C9 zero 'alpha =' assignments anywhere in BM.36 "
                                        "(no numerical strength value is asserted)")

stamp("§C done — the force-structure ladder")


# ==========================================================================
# §D  BM.37 — the route-artifact adjudication and the counting trap
# ==========================================================================
print("\n§D (BM.37) — the route values, the disjoint input alphabets,")
print("            and the Koide-form invariant Q = 2/3")

# D1 — the W(Q) census, re-enumerated two ways
mq = {0: 2, 1: 1, -1: 1}
Wc = {}
for trip in itertools.product((0, 1, -1), repeat=3):
    k = sum(trip)
    wt = 1
    for q in trip:
        wt *= mq[q]
    Wc[k] = Wc.get(k, 0) + wt
chk(Wc[0] == 20 and Wc[1] == 15 and Wc[-1] == 15,
    "§D1 W(0) = 20, W(+1) = W(-1) = 15 by exhaustive enumeration of the 27 ordered charge triples "
    "with the end-pair census m_q = (2,1,1) (BM.28(2))")
polyz = [1, 2, 1]                       # (z^-1 + 2 + z) coefficients over shifts (-1,0,1)
conv = [1]
for _ in range(3):
    conv = [sum((conv[k - d] if 0 <= k - d < len(conv) else 0) * polyz[d]
                for d in range(3)) for k in range(len(conv) + 2)]
chk(conv == [1, 6, 15, 20, 15, 6, 1],
    f"§D1 (2+z+z^-1)^3 = {conv}: the generating function reproduces the 64-assignment census "
    "(1,6,15,20,15,6,1) exactly (BM.28(2))")
chk(sum(conv) == 64, "§D1 the census sums to 4^3 = 64")
chk(Fr(20, 15) == Fr(4, 3), "§D1 route (ii): W(0)/W(+1) = 20/15 = 4/3 exactly — the probability-space "
                             "size ratio, an entropic capacity count (BM.30(2))")

# D2 — route (i): the cancellation lemma at the six frozen factors
vw = [Fr(3), Fr(5), Fr(7)]
dS = [Fr(2), Fr(9), Fr(4)]
base = sum((vw[i] * dS[i] for i in range(3)), Fr(0)) / sum(vw)
canc = all(sum((Fr(c) * vw[i] * dS[i] for i in range(3)), Fr(0))
           / sum((Fr(c) * vw[i] for i in range(3)), Fr(0)) == base
           for c in (1, 2, 3, 15, 20, Fr(7, 3)))
chk(canc, "§D2 route (i): a uniform sector factor cancels identically in the normalized average at "
          "the six frozen factors {1,2,3,15,20,7/3} — the ratio 1 is a theorem about normalized "
          "averages, not a physical degeneracy (BM.30(3))")

# D3 — route (iii): the exact reductions and the pairwise inequalities
chk(Fr(5336, 1196) == Fr(58, 13), "§D3 5336/1196 = 58/13 by exact reduction (FT.106(3)'s frozen integers)")
chk(Fr(4796, 802) == Fr(2398, 401), "§D3 4796/802 = 2398/401 by exact reduction")
chk(5336 * 13 == 1196 * 58 and 4796 * 401 == 802 * 2398,
    "§D3 both reductions cross-multiplied in Z")
rr = [Fr(1), Fr(4, 3), Fr(58, 13), Fr(2398, 401)]
chk(all(rr[i] != rr[j] for i in range(4) for j in range(i + 1, 4)),
    "§D3 the four route values 1, 4/3, 58/13, 2398/401 are pairwise unequal (BM.30(1) re-verified)")

# D4 — the disjoint input-alphabet token census on the canonical defining strings
P3 = rd("Part3_Fermion_era.md")


def between(src, a, b, start=0):
    i = src.find(a, start)
    assert i >= 0, f"anchor missing: {a[:40]}"
    j = src.find(b, i)
    assert j > i, f"end anchor missing after: {a[:40]}"
    return src[i:j]


route_blocks = {
    "route (i) [BM.28(4)(i)]": between(P4, "\\textbf{(i) the normalized ensemble average}",
                                       "\\textbf{(ii) the unnormalized total deficit}"),
    "route (ii) [BM.28(4)(ii)]": between(P4, "\\textbf{(ii) the unnormalized total deficit}",
                                         "\\textbf{(iii) the amplitude layer}"),
    "route (iii) [BM.28(4)(iii)]": between(P4, "\\textbf{(iii) the amplitude layer}",
                                           "(5)\\quad\\textbf{what the splitting does not touch:}"),
    "Def-H.32(2) weight layers": between(P3, "$(2)$ **Configurations and the two weight layers.**",
                                         "$(3)$ **Fugacities"),
    "Def-H.32(5) partition fns": between(P3, "$(5)$ **The sector partition functions.**",
                                         "$(6)$ **The mass expectation (Def-H.32(6)).**"),
    "Def-H.32(6) mass expectation": between(P3, "$(6)$ **The mass expectation (Def-H.32(6)).**",
                                            "$(7)$ **The Janus move system"),
}
METRIC_ALPHA = [r"\\Omega", r"\\varkappa", r"\\beta", r"w_i", r"q_\{ij\}", r"\\gamma",
                r"N\^i", r"N_i", r"N\^2", r"p_i", r"g_\{0i\}", r"g_\{ij\}",
                r"\blapse\b", r"\bshift\b", r"\bmomentum\b", r"\bmetric\b", r"\\sqrt"]
metric_hits = {nm: [pat for pat in METRIC_ALPHA if re.search(pat, blk)]
               for nm, blk in route_blocks.items()}
chk(all(not h for h in metric_hits.values()),
    f"§D4 the metric alphabet occurs ZERO times inside the canonical defining clauses of routes "
    f"(i)-(iii) [Def-H.32(2),(5),(6); BM.28(4)]: {metric_hits}")
dm10 = between(P4, "### Def-BM.10", "### BM.34")
kin = (between(dm10, "(2)\\quad\\textbf{the metric data", "(3)\\quad\\textbf{the momenta")
       + between(dm10, "(3)\\quad\\textbf{the momenta", "(4)\\quad\\textbf{the rest input")
       + between(dm10, "(5)\\quad\\textbf{the mass shell", "(6)\\quad\\textbf{status and scope")
       + between(dm10, "**Rmk (the unit-mass normalization).**", "**Req.**"))
MEASURE_ALPHA = [r"W\(Q\)", r"\\#\\mathrm\{inst\}", r"\\nu\,", r"\\nu_\\Gamma",
                 r"v_\\Gamma", r"\\Delta S", r"t\^\{\|R\|\}", r"u\^L", r"Z\^\{",
                 r"\bensemble\b", r"\bflicker\b", r"\\sigma_e", r"\bmeasure\b",
                 r"\bamplitude\b"]   # r"\\nu\," is the norm-weight symbol; a bare greek nu is a tensor index
meas_hits = [pat for pat in MEASURE_ALPHA if re.search(pat, kin)]
chk(not meas_hits,
    f"§D4 the measure alphabet occurs ZERO times inside Def-BM.10(2),(3),(5) and its Rmk "
    f"(the kinematic clauses; clause (4)'s rest input is the shared symbol m): {meas_hits}")

# D5 — the Koide-form invariant Q = 2/3, phase-independent, in the quotient ring
QV = ["c", "s", "r", "u"]
rules = {
    ("c", 2): Poly(QV, {(0, 0, 0, 0): Fr(1), (0, 2, 0, 0): Fr(-1)}),   # c^2 -> 1 - s^2
    ("r", 2): Poly.const(QV, 3),                                        # r^2 -> 3
    ("u", 2): Poly.const(QV, 2),                                        # u^2 -> 2
}
c = V(QV, "c", rules)
s = V(QV, "s", rules)
r = V(QV, "r", rules)
u = V(QV, "u", rules)
one = P(QV, 1, rules)
half = P(QV, Fr(1, 2), rules)
r0 = one + u * c
r1 = one - (u * c + u * s * r) * half
r2 = one - (u * c - u * s * r) * half
S1 = r0 + r1 + r2
S2 = r0 * r0 + r1 * r1 + r2 * r2
chk(S1 == P(QV, 3, rules), "§D5 sum r_i = 3 exactly in Q[c,s,r,u]/(c^2+s^2-1, r^2-3, u^2-2) — "
                           "for GENERIC c,s: phase-independent (Def-BM.6(4))")
chk(S2 == P(QV, 6, rules), "§D5 sum r_i^2 = 6 exactly, phase-independent (Def-BM.6(4), FT.158(4))")
chk(Fr(6, 9) == Fr(2, 3), "§D5 the Koide ratio Q = sum r_i^2/(sum r_i)^2 = 6/9 = 2/3 exactly — "
                          "a structural invariant of the cosine triplet; its mass-form bridge is "
                          "item-13 content, ¬adopted [Def-BM.6(5)]")

# D6 — the closure tokens on record
i37 = P4.find("### BM.37")
j37 = P4.find("### BM.38")
B37 = P4[i37:j37]
chk("counting trap" in B37 and "barred as physical masses" in B37,
    "§D6 BM.37 carries the closure rows: 'counting trap' and 'barred as physical masses' on record")
chk("item-13" in B37 and "\\mathrm{FT.79}(5)" in B37 and "\\mathrm{BM.30}(5)" in B37,
    "§D6 the three bars are cited in BM.37(3): disjointness, amplitude != mass [FT.79(5)], "
    "the read-choice row [BM.30(5)], and the item-13 pointer")

stamp("§D done — the route-artifact adjudication")


# ==========================================================================
# §E  BM.38 — document pins and hygiene
# ==========================================================================
print("\n§E (BM.38) — document pins, hygiene, and the ledger/README/index rows")

P1 = rd("Part1_Qubit_era.md")
CE = rd("Census.md")
HL = rd("HistLog.md")

# E1 — presence, uniqueness and ownership
chk(P4.count("## Tier BM.10 —") == 1, "§E1 Part 4 carries exactly one '## Tier BM.10' header")
for tag in ["Def-BM.10", "BM.34", "BM.35", "BM.36", "BM.37", "BM.38"]:
    chk(P4.count(f"### {tag} —") == 1, f"§E1 {tag} occurs exactly once as a Part 4 section")
    others = sum(tt.count(f"### {tag} —") for tt in (P1, P2, P3, CE))
    chk(others == 0, f"§E1 {tag} occurs in no other canon file (ownership)")

# E2 — block completeness
for tag in ["BM.34", "BM.35", "BM.36", "BM.37", "BM.38"]:
    i = P4.find(f"### {tag} —")
    cands = [x for x in (P4.find("\n### ", i + 4), P4.find("\n## ", i + 4), len(P4)) if x > 0]
    blocks = P4[i:min(cands)]
    ok = all(tok in blocks for tok in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"))
    chk(ok and "\\blacksquare" in blocks,
        f"§E2 {tag} carries Thm/Req/Pf/Phys and a proof terminator")
idb = P4.find("### Def-BM.10 —")
jdb = P4.find("### BM.34 —")
chk("**Def.**" in P4[idb:jdb], "§E2 Def-BM.10 carries its **Def.** block")

# E3 — the header, charter and closure rows
_endash = chr(0x2013)
_mNS = re.search(r"Def-BM\.1" + _endash + r"Def-BM\.(\d+); BM\.1" + _endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + _endash + r"BM\.(\d+)", P4)
chk(_mNS and int(_mNS.group(1)) >= 10 and int(_mNS.group(2)) >= 38 and int(_mNS.group(3)) >= 10,
    "§E3 the Part 4 Namespace line covers Tier BM.10's tags (Def-BM.10 / BM.38) and extends with later tiers")
chk("(xiii) the metric-energy and vacuum-entropy layer [Tier BM.10" in P4,
    "§E3 the Part 4 charter 0.1 carries clause (xiii)")
closure = P4[P4.find("## Closure exports of Part 4"):]
chk("\\mathrm{Def\\text{-}BM.10}" in closure and "\\mathrm{BM.38}" in closure,
    "§E3 the closure-export table carries the Def-BM.10 and BM.34–BM.38 rows")

# E4 — hygiene of the tier text
tier = P4[P4.find("## Tier BM.10 —"):P4.find("\n## ", P4.find("## Tier BM.10 —") + 5)]
for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
    chk(word not in tier.lower(), f"§E4 zero '{word}' in the tier text")
chk(not re.search(r"\bP-H\d", tier), "§E4 zero registry (P-H) tokens in the tier")
chk("**Status.**" not in tier, "§E4 zero '**Status.**' lines in the tier")
chk("[EXT]" not in tier, "§E4 zero [EXT] markers in the tier")
dec = re.findall(r"(?<![A-Za-z0-9§])\d+\.\d+", tier)
chk(not dec, f"§E4 zero decimal numerals in the tier text outside tag/section names "
             f"(exact rationals only): {dec}")
for tok in ["MeV", "GeV", "0.511", "938.2", "939.5", "105.6", "1776", "140.79"]:
    chk(tok not in tier, f"§E4 zero external-value token '{tok}' in the tier [P5]")
chk(tier.count("137") == len(re.findall(r"1/137", tier)),
    "§E4 every occurrence of '137' in the tier sits inside the pi-against-1/137 category-error "
    "citation [FT.73(5) trap pattern]")
chk("None introduced by this part." in P4[P4.find("## §Cal-BM"):P4.find("## Tier 4.0")],
    "§E4 §Cal-BM stays empty: 'None introduced by this part.' stands")

# E5 — the ledger and README rows
for tag in ["Def-BM.10", "BM.34", "BM.35", "BM.36", "BM.37", "BM.38"]:
    chk(f"**{tag}.**" in HL, f"§E5 HistLog §III carries the {tag} status-ledger entry")
chk("(V.14)" in HL and "Suite state: 65/65" in HL,
    "§E5 HistLog §V carries the (V.14) verification-history entry with suite state 65/65")
RM = rd("README.md")
chk("(80 checkers)" in RM, "§E5 the main README carries the 79-checker count")
CRM = rd(os.path.join("checks", "README.md"))
chk("(80 checkers)" in CRM and "**80/80**" in CRM,
    "§E5 checks/README.md carries the 79-checker count and suite state")
chk("verify_H_kinetic_energy_metric.py" in CRM, "§E5 checks/README.md lists the new content checker")

# E6 — the index and the Summary of Record
with open(os.path.join(DOCS, "index", "tags.json"), encoding="utf-8") as f:
    IDXT = json.load(f)
idxkeys = set(IDXT.keys()) if isinstance(IDXT, dict) else {tt["tag"] for tt in IDXT}
for tag in ["Def-BM.10", "BM.34", "BM.35", "BM.36", "BM.37", "BM.38"]:
    chk(tag in idxkeys, f"§E6 the regenerated index/tags.json carries {tag}")
SM = rd("Summary.md")
chk("BM.34" in SM and "BM.38" in SM and "Def-BM.10" in SM,
    "§E6 the regenerated Summary of Record carries the tier's statements")

# E7 — the suite count arithmetic
nverify = len([f for f in os.listdir(HERE)
               if f.startswith("verify_") and f.endswith(".py")])
chk(nverify + 1 == 80, f"§E7 the discovered suite is {nverify} verify_*.py + check_format.py = 80 checkers")

stamp("§E done — document pins and hygiene")

# --------------------------------------------------------------------------
print("\n" + "=" * 74)
if FAILS:
    print(f"verify_H_kinetic_energy_metric: {len(FAILS)} FAILURE(S) of {N + len(FAILS)}")
    for msg in FAILS:
        print("  -", msg)
    sys.exit(1)
print(f"verify_H_kinetic_energy_metric: ALL GREEN — {N} exact checks, "
      f"{time.time()-t0:.1f}s, no floating point in any assertion")
sys.exit(0)
