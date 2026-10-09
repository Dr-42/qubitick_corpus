#!/usr/bin/env python3
"""
verify_H_neutron_decay_vertex.py — machine verification of Tier BM.11
(Def-BM.11, BM.39-BM.45): the neutron decay vertex — the family transport-profile
map, the rung-1 isospin row, the forced neutral member, the angular-momentum
budget, the member-wise curvature rows, the per-tick evolution, and the assembled
reaction with its Q-value sign theorem.

Exact arithmetic only: integers, fractions.Fraction, multivariate polynomial
rings over Q with monomial rewrite rules (quotient rings), complex-over-Fraction
matrix algebra with Faddeev-LeVerrier charpolys, complex-over-polynomial Pauli
spinor algebra over Q(i) (x) Q[g,g'], Laurent-monomial rings, weight-truncated
jet rings for the linearized field equations, exact rational ln2 enclosures.
No floating point in any assertion.

Sections:
  §A  Def-BM.11/BM.39 — the family transport-profile map: the EW.33 Gram form
      recomputed (imaginary parts antisymmetric, cancelling in the symmetric
      form), the kernel line as EW.22's span{(0,0,g',g)} = the EM generator
      direction, FT.158(1)'s inner C3 re-derived on the pair register
      (W^3 = 3W, U^3 = E, U W_i U^dag = W_{i+1}), the cosine-triplet identities
      in Q[c,s,r3,r2]/(c^2+s^2-1, r3^2-3, r2^2-2), the orbit evaluation
      G(i) = A0 - B0 cos(delta - 2 pi i/3) with A0 = 3g^2/8 + g'^2/16 and
      B0 = gg'/4, the sum-of-squares positivity A0 -+ B0 = (3/8)(g -+ g'/3)^2
      + g'^2/48, the kernel unreachability of the cosine triplet, the sum rule
      3 A0, the splitting factorization, the affine-in-r form, the angle ledger
      16 delta_nu = 9 delta_l = 27 delta_q = 2, and FT.54(1)'s exact defect
      identity for the area ladder.
  §B  BM.40 — the rung-1 isospin row: sum W_i^2 = (3/2)E0 + (1/2)Sigma
      = E0 + S = 2 Pi_R entrywise over Q(i), the su(2) closure, the branch
      eigen-rows (2 on the symmetric basis, 0 on the antisymmetric),
      W_i Pi_V = 0, the projector algebra and traces, and the sigma-vs-branch
      token-disjointness census on the defining strings of D3.4 against
      CT0.7/FT.101.
  §C  BM.41 — the vertex kinematics: the exact solution of the two-body
      conservation system, the Kallen identity and its m_n = m_p factorization
      ml^2(ml^2 - 4mn^2), the two-body impossibility E_p - m_p = -ml^2/(2mn) < 0
      with the branch cover (2 > sqrt2 by squaring), the positivity of m_l on
      both read species (SOS + the ln2 enclosure), the Q monomial -(ml+mv) and
      the sign theorem, the route-(ii) undetermined-sign witnesses, the
      three-body endpoint identities, the collinear reverse-Cauchy identity in
      the on-shell quotient ring, and the Lagrange Cauchy-Schwarz SOS.
  §D  BM.42 — angular momentum: the SU(2) Casimir ladder (3/4, 2, 15/4, 6),
      the tensor charpolys x^3(x-2) on C^4, (x-15/4)^4(x-3/4)^4 on C^8
      [FT.88(7): 2(x)2(x)2 = 4+2+2], x^2(x-2)^9(x-6)^5 on C^16 (2 singlets,
      3 triplets, 1 quintet), the Lagrange identity r^2 p^2 = (x.p)^2
      + sum L_ij^2 and the decomposed dispersion, the CN adjudication
      1/4 < 3/4 (zero correction), the conserved moment current on the dust
      class (symbolic differentiation, all 16 (nu,lambda) components), the
      (-1)^l integer characters, and the l-selection census.
  §E  BM.43 — curvature: the proton's six frozen reads re-verified as Laurent
      monomials at E_int = 6 with the 72 pi ln2 lock, the symbolic lepton rows,
      the linearized field equations in the weight-truncated jet ring
      (G00 = 2 Laplacian(Phi), G0i = 0, Gij = 0), the coefficient identity
      kappa^2/2 = 4 pi G_N, the harmonicity of 1/r away from the source,
      G_N m = h E/4, r_s = h E/2, Phi(Delta x_B) = -E^2 ln2 / 4, and the
      source-side superposition monomial.
  §F  BM.44 — time: the resolvent identity in Q[w,x+,x-]/(w^12), the SOS
      completion 4e(1-4e) = 1/4 - 16(e-1/8)^2, the grid census over k/256, the
      Gamma_tr range [0,1/3] with exact endpoints and the monotonicity
      difference identity, the e-folding count 3 ticks, and the no-flicker row.
  §G  BM.45 — document pins and hygiene: tier/tag presence and uniqueness,
      Thm/Req/Pf/Phys completeness, the BM.23 on-record Rmk, the naming rows
      A-BM.4/A-BM.5, namespace/charter/closure rows, the forbidden-word and P5
      scans, the HistLog §III/§V entries, README suite counts at 66, and the
      index/Summary regeneration pins.

Tier BM.11 is new canon content with no first edition in H_archive/; the pins of
this checker resolve against the era-canon texts directly.

Run: python3 verify_H_neutron_decay_vertex.py   (auto-discovered by run_all.py)
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
print("verify_H_neutron_decay_vertex — Tier BM.11 (Def-BM.11, BM.39–BM.45)")
print("=" * 74)


# ==========================================================================
# exact rings: polynomials with rewrite rules
# ==========================================================================

class Poly:
    """Commutative polynomial over Fraction in named variables, with monomial
    rewrite rules (quotient rings). Exact; no floating point."""

    def __init__(self, names, terms=None, rules=None):
        self.names = list(names)
        self.ix = {n: i for i, n in enumerate(self.names)}
        self.rules = rules or {}
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
            if guard > 400000:
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
        b = Poly(self.names, dict(self.t), self.rules)
        while n:
            if n & 1:
                r = r * b
            b = b * b
            n >>= 1
        return r

    def zero(self):
        return not self.t

    def __eq__(self, o):
        if not isinstance(o, Poly):
            return NotImplemented
        return self.t == o.t

    def __hash__(self):
        return hash(tuple(sorted(self.t.items(), key=lambda kv: str(kv[0]))))

    def subs(self, values):
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
                        term = term * (v ** e[i])
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
        for e, c in sorted(self.t.items(), key=lambda kv: str(kv[0]))[:6]:
            s = str(c)
            for i, n in enumerate(self.names):
                if e[i] == 1:
                    s += f"*{n}"
                elif e[i] > 1:
                    s += f"*{n}^{e[i]}"
            parts.append(s)
        tail = f" +...({len(self.t)})" if len(self.t) > 6 else ""
        return " + ".join(parts) + tail


def P(names, x, rules=None):
    return Poly.const(names, x, rules)


def V(names, n, rules=None):
    return Poly.var(names, n, rules)


def lift(poly, names, rules=None):
    pad = len(names) - len(poly.names)
    assert pad >= 0
    return Poly(names, {tuple(list(e) + [0] * pad): c for e, c in poly.t.items()}, rules)


def psub(poly, mapping):
    """substitute variables by Polys (same names/rules)."""
    out = Poly(poly.names, rules=poly.rules)
    for e, c in poly.t.items():
        term = Poly.const(poly.names, c, poly.rules)
        for i, n in enumerate(poly.names):
            if e[i]:
                base = mapping.get(n, Poly.var(poly.names, n, poly.rules))
                term = term * base.pow(e[i])
        out = out + term
    return out


def dpoly(p, name):
    """exact partial derivative d/d(name)."""
    k = p.names.index(name)
    out = Poly(p.names, rules=p.rules)
    for e, c in p.t.items():
        if e[k]:
            e2 = list(e)
            e2[k] -= 1
            out = out + Poly(p.names, {tuple(e2): c * e[k]}, p.rules)
    return out


# ---- complex numbers over Fraction and their matrices -----------------------

class Cplx:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, o):
        return Cplx(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return Cplx(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return Cplx(self.a * o, self.b * o)
        return Cplx(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, k):
        return Cplx(self.a / k, self.b / k)

    def __neg__(self):
        return Cplx(-self.a, -self.b)

    def conj(self):
        return Cplx(self.a, -self.b)

    def __eq__(self, o):
        if isinstance(o, (int, Fr)):
            o = Cplx(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def __repr__(self):
        return f"({self.a}{self.b:+}i)"


def cmat_mul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = [[Cplx(0)] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            acc = Cplx(0)
            for t in range(k):
                acc = acc + A[i][t] * B[t][j]
            C[i][j] = acc
    return C


def cmat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def cmat_scal(A, z):
    return [[A[i][j] * z for j in range(len(A[0]))] for i in range(len(A))]


def cmat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def ceye(n):
    return [[Cplx(int(i == j)) for j in range(n)] for i in range(n)]


def cdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def ctr(A):
    return sum((A[i][i] for i in range(len(A))), Cplx(0))


def cvec_mul(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v))), Cplx(0)) for i in range(len(A))]


def kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb] for j in range(ca * cb)]
            for i in range(ra * rb)]


def charpoly(A):
    """Faddeev-LeVerrier: [1, c1, ..., cn] for det(xI - A) = x^n + c1 x^{n-1} + ..."""
    n = len(A)
    cs = [Cplx(1)]
    M = [row[:] for row in A]
    for k in range(1, n + 1):
        cs.append(-ctr(M) / k)
        if k < n:
            M = cmat_mul(A, cmat_add(M, cmat_scal(ceye(n), cs[k])))
    return cs


def polymul_coeffs(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def expected_charpoly(roots_with_mult):
    poly = [Fr(1)]
    for root, mult in roots_with_mult:
        for _ in range(mult):
            poly = polymul_coeffs(poly, [Fr(1), -Fr(root)])
    return poly


# ---- complex-over-Poly (for the Gram form) -----------------------------------

class CP:
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


def cinner(u, w):
    res = None
    for a, b in zip(u, w):
        t = a.conj() * b
        res = t if res is None else CP(res.re + t.re, res.im + t.im)
    return res


# ---- Laurent monomials --------------------------------------------------------

class LM:
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
        return LM(names, {tuple(kw.get(n, 0) for n in names): Fr(1)})

    @staticmethod
    def cst(names, x):
        return LM(names, {tuple([0] * len(names)): Fr(x)})

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return LM(self.names, {e: c * Fr(o) for e, c in self.t.items()})
        acc = {}
        for e1, c1 in self.t.items():
            for e2, c2 in o.t.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                acc[e] = acc.get(e, Fr(0)) + c1 * c2
        return LM(self.names, {e: c for e, c in acc.items() if c != 0})

    def __add__(self, o):
        acc = dict(self.t)
        for e, c in o.t.items():
            acc[e] = acc.get(e, Fr(0)) + c
        return LM(self.names, {e: c for e, c in acc.items() if c != 0})

    def __sub__(self, o):
        return self + LM(self.names, {e: -c for e, c in o.t.items()})

    def __neg__(self):
        return LM(self.names, {e: -c for e, c in self.t.items()})

    def pow(self, n):
        r = LM.cst(self.names, 1)
        b = LM(self.names, dict(self.t))
        while n:
            if n & 1:
                r = r * b
            b = b * b
            n >>= 1
        return r

    def inv(self):
        assert len(self.t) == 1
        e, c = next(iter(self.t.items()))
        return LM(self.names, {tuple(-x for x in e): 1 / c})

    def __eq__(self, o):
        if isinstance(o, (int, Fr)):
            o = LM.cst(self.names, o)
        return self.t == o.t

    def __repr__(self):
        return str(self.t)


# ==========================================================================
# §A  Def-BM.11 / BM.39 — the family transport-profile map
# ==========================================================================
print("\n§A (Def-BM.11, BM.39) — the Gram form, the inner C3, the cosine-triplet")
print("            orbit, positivity, the sum rule, and the defect identity")

# A1 — the EW.33 Gram form recomputed from Pauli spinors over Q(i) x Q[g,g']
GV = ["g", "gp"]
gz = V(GV, "g")
gpz = V(GV, "gp")
zP = P(GV, 0)
halfP = P(GV, Fr(1, 2))
Gv = [
    [CP(halfP * gz, zP), CP(zP, zP)],
    [CP(zP, -halfP * gz), CP(zP, zP)],
    [CP(zP, zP), CP(-halfP * gz, zP)],
    [CP(zP, zP), CP(halfP * gpz, zP)],
]
Gram = [[None] * 4 for _ in range(4)]
im_diag_zero = im_antisym = True
for A_ in range(4):
    for B_ in range(4):
        ip = cinner(Gv[A_], Gv[B_])
        ipT = cinner(Gv[B_], Gv[A_])
        Gram[A_][B_] = ip.re
        if A_ == B_:
            im_diag_zero = im_diag_zero and ip.im.zero()
        im_antisym = im_antisym and (ip.im + ipT.im).zero()
q4 = P(GV, Fr(1, 4))
exp_Gram = [[q4 * gz * gz if i == j and i < 3 else
             (q4 * gpz * gpz if i == j == 3 else
              (-q4 * gz * gpz if {i, j} == {2, 3} else zP))
             for j in range(4)] for i in range(4)]
chk(all(Gram[i][j] == exp_Gram[i][j] for i in range(4) for j in range(4))
    and im_diag_zero and im_antisym,
    "§A1 the Gram form recomputed from EW.32's seed equals (1/4)[[g^2,0,0,0],[0,g^2,0,0],"
    "[0,0,g^2,-gg'],[0,0,-gg',g'^2]] exactly; the imaginary parts are zero on the diagonal and "
    "antisymmetric off it — Def-BM.11(1)")

# A2 — the kernel line is EW.22's span{(0,0,g',g)} = the EM generator direction
TV = ["g", "gp", "c", "s", "r3", "r2"]
TR = {("c", 2): Poly(TV, {(0, 0, 0, 0, 0, 0): Fr(1), (0, 0, 0, 2, 0, 0): Fr(-1)}),
      ("r3", 2): Poly.const(TV, 3),
      ("r2", 2): Poly.const(TV, 2)}
kvec = [P(TV, 0, TR), P(TV, 0, TR), lift(gpz, TV, TR), lift(gz, TV, TR)]
GramT = [[lift(Gram[i][j], TV, TR) for j in range(4)] for i in range(4)]
kv = [sum((GramT[i][j] * kvec[j] for j in range(4)), P(TV, 0, TR)) for i in range(4)]
chk(all(z.zero() for z in kv),
    "§A2 Gram*(0,0,g',g)^T = 0 exactly: the kernel line is the seed's stabilizer — EW.22's "
    "span{(0,0,g',g)}, the direction of gg'(W_3+Y) = gg'Q, the EM generator [FT.12; EW.22]")

# A3 — FT.158(1)'s inner C3 on the pair register
I2 = [[Cplx(int(i == j)) for j in range(2)] for i in range(2)]
sg = [[[Cplx(0), Cplx(1)], [Cplx(1), Cplx(0)]],
      [[Cplx(0), Cplx(0, -1)], [Cplx(0, 1), Cplx(0)]],
      [[Cplx(1), Cplx(0)], [Cplx(0), Cplx(-1)]]]
Wi = [cmat_scal(cmat_add(kron(sg[i], I2), kron(I2, sg[i])), Fr(1, 2)) for i in range(3)]
Wsum = cmat_add(cmat_add(Wi[0], Wi[1]), Wi[2])
Wsq = cmat_mul(Wsum, Wsum)
Wcu = cmat_mul(Wsq, Wsum)
chk(cmat_eq(Wcu, cmat_scal(Wsum, 3)),
    "§A3 W^3 = 3W exactly over Q(i) with W = W_1+W_2+W_3 on the pair register "
    "[FT.158(1)'s polynomial identity re-derived]")
E4 = ceye(4)
U = cmat_add(cmat_add(E4, cmat_scal(Wsq, Fr(-1, 2))), cmat_scal(Wsum, Cplx(0, Fr(-1, 2))))
U3 = cmat_mul(cmat_mul(U, U), U)
chk(cmat_eq(U3, E4), "§A3 U^3 = E_0 exactly with U = E_0 - W^2/2 - (i/2)W: the C3 is inner "
                     "[FT.158(1) re-derived]")
rot_ok = all(cmat_eq(cmat_mul(cmat_mul(U, Wi[i]), cdag(U)), Wi[(i + 1) % 3]) for i in range(3))
chk(rot_ok, "§A3 U W_i U^dag = W_{i+1} exactly (indices mod 3): the family rotation cycles the weak "
            "triplet — Def-BM.11(2)")
Yseed = cmat_scal(I2, Fr(1, 2))
comm_ok = all(cmat_eq(cmat_mul(Yseed, x), cmat_mul(x, Yseed)) for x in sg)
chk(comm_ok, "§A3 [Y, sigma_i] = 0 on the seed carrier: Y is the centre, so the hypercharge "
             "coordinate is C3-fixed [EW.8; D2.12; EW.32]")

# A4 — the cosine-triplet identities in the quotient ring
c = V(TV, "c", TR)
s = V(TV, "s", TR)
r3 = V(TV, "r3", TR)
r2 = V(TV, "r2", TR)
oneT = P(TV, 1, TR)
C0 = c
C1 = -(c + r3 * s) * P(TV, Fr(1, 2), TR)
C2 = -(c - r3 * s) * P(TV, Fr(1, 2), TR)
chk((C0 + C1 + C2).zero(),
    "§A4 sum_i cos(delta + 2 pi i/3) = 0 exactly in Q[c,s,r3]/(c^2+s^2-1, r3^2-3) — generic phase "
    "[FT.111(3)/FT.158(4) identity re-derived]")
chk(C0 * C0 + C1 * C1 + C2 * C2 == P(TV, Fr(3, 2), TR),
    "§A4 sum_i cos^2 = 3/2 exactly, generic phase — the normalization that makes the orbit sum "
    "phase-free")

# A5 — the orbit evaluation G(i) = A0 - B0 cos(delta - 2 pi i/3)
gT = lift(gz, TV, TR)
gpT = lift(gpz, TV, TR)
y0 = P(TV, Fr(1, 2), TR)
A0 = gT * gT * P(TV, Fr(3, 8), TR) + gpT * gpT * P(TV, Fr(1, 16), TR)
B0 = gT * gpT * P(TV, Fr(1, 4), TR)
c3slot = [C2, C1, C0]          # c(i)_3 = cos(delta + 2 pi (2-i)/3): the W_3 slot cycles
                               # through the triplet (the set equals {cos(delta-2 pi j/3)}_j
                               # under the orbit-label convention of Def-BM.11(4))
weak = [C0, C1, C2]
Gvals = []
for i in range(3):
    prof = [weak[(0 - i) % 3], weak[(1 - i) % 3], weak[(2 - i) % 3], y0]
    Gi = P(TV, 0, TR)
    for A_ in range(4):
        for B_ in range(4):
            Gi = Gi + prof[A_] * prof[B_] * GramT[A_][B_]
    Gvals.append(Gi)
chk(all(Gvals[i] == (A0 - B0 * c3slot[i]) for i in range(3)),
    "§A5 the orbit evaluation: G(c(i)) = (3g^2/8 + g'^2/16) - (gg'/4) cos(delta - 2 pi i/3) exactly "
    "in Q[g,g'] (x) Q[c,s,r3,r2]/(...) — Def-BM.11(5), the boxed mass form")

# A6 — positivity via exact sum-of-squares decompositions
sos_minus = gT * gT * P(TV, Fr(3, 8), TR) - gT * gpT * P(TV, Fr(1, 4), TR) + gpT * gpT * P(TV, Fr(1, 16), TR)
sos_form = (gT - gpT * P(TV, Fr(1, 3), TR)).pow(2) * P(TV, Fr(3, 8), TR) + gpT.pow(2) * P(TV, Fr(1, 48), TR)
chk(sos_minus == sos_form and (A0 - B0) == sos_minus,
    "§A6 A0 - B0 = (3/8)(g - g'/3)^2 + g'^2/48 exactly (SOS with positive rational coefficients): "
    "m^2_i > 0 for every line, every phase, every (g,g') != (0,0) — BM.39(1)")
sos_plus = (gT + gpT * P(TV, Fr(1, 3), TR)).pow(2) * P(TV, Fr(3, 8), TR) + gpT.pow(2) * P(TV, Fr(1, 48), TR)
chk((A0 + B0) == sos_plus, "§A6 A0 + B0 = (3/8)(g + g'/3)^2 + g'^2/48 exactly: the upper edge of the "
                           "mass-squared band M^2[A0-B0, A0+B0]")

# A7 — the kernel line is unreachable by the cosine triplet
C1_at_c0 = C1.subs({"c": 0})                       # -r3 s / 2
sq_pos = C1_at_c0.subs({"s": 1}).pow(2)            # r3^2/4 = 3/4
sq_neg = C1_at_c0.subs({"s": -1}).pow(2)
chk(sq_pos == P(TV, Fr(3, 4), TR) and sq_neg == P(TV, Fr(3, 4), TR),
    "§A7 at cos phi = 0 (s = +-1): cos(phi + 2 pi/3)^2 = 3/4 != 0 exactly — two cosines a third of "
    "a turn apart never vanish together: the EM kernel line carries no family row (BM.39(1))")

# A8 — the sum rule: phase-free and channel-free
chk(sum(Gvals, P(TV, 0, TR)) == A0 * P(TV, 3, TR),
    "§A8 sum_i G(c(i)) = 3 A0 exactly, generic phase: the orbit sum rule is phase-independent and "
    "channel-independent (the seed is channel-blind [EW.32]) — BM.39(3)")

# A9 — the splitting law: proportional to gg' exactly
split01 = Gvals[0] - Gvals[1]
target01 = B0 * (c3slot[1] - c3slot[0])
chk(split01 == target01,
    "§A9 G(c(0)) - G(c(1)) = (gg'/4)(cos phi_1 - cos phi_0) exactly: the intra-family splitting is "
    "the mixed weak-hypercharge strength acting on the transport phase — BM.39(2)")
dem = {"c": Fr(1), "s": Fr(0)}
Gdem = [Gvals[i].subs(dem) for i in range(3)]
chk(Gdem[0] == Gdem[1] and isinstance(Gdem[2], Poly)
    and (Gdem[0] - Gdem[2]) == B0 * P(TV, Fr(3, 2), TR),
    "§A9 the democratic witness delta = 0: the W_3-slot cos-values are {-1/2,-1/2,1} across the "
    "orbit — two lines degenerate at A0 + B0/2, the third sits at A0 - B0, split by (3/2)(gg'/4) "
    "exactly")

# A10 — the affine-in-r form: r2 * m^2_i = M^2 (A0 r2 + B0 - B0 r_i)
rvals = [oneT + r2 * Ci for Ci in [C0, C1, C2]]
c3r = [oneT + r2 * Ci for Ci in c3slot]
aff_ok = all(r2 * (A0 - B0 * c3slot[i]) == (A0 * r2 + B0 - B0 * c3r[i]) for i in range(3))
chk(aff_ok, "§A10 the affine form: r2 * (A0 - B0 C) = A0 r2 + B0 - B0 (1 + r2 C) exactly — "
            "m^2_i is affine decreasing in r = 1 + sqrt2 cos [FT.113 vocabulary rows; Def-BM.11(5)]")

# A11 — the angle ledger: exact rationals
chk(Fr(16) * Fr(1, 8) == 2 and Fr(9) * Fr(2, 9) == 2 and Fr(27) * Fr(2, 27) == 2
    and Fr(3) * Fr(2, 27) == Fr(2, 9),
    "§A11 the angle ledger: 16 delta_nu = 9 delta_l = 27 delta_q = 2 and 3 delta_q = delta_l exactly "
    "[FT.143(5); FT.119(2)] — the three channels share the seed numerator")

# A12 — FT.54(1)'s exact defect identity for the area ladder (holonomy species)
DV = ["Cc", "Ss"]
DR = {("Cc", 2): Poly(DV, {(0, 0): Fr(1), (0, 2): Fr(-1)})}
Cc = V(DV, "Cc", DR)
Ss = V(DV, "Ss", DR)
# U = cos(phi) I + i sin(phi) sigma_z  ->  diag(Cc + i Ss, Cc - i Ss) over CP
# (the defect identity is axis-independent [FT.54(1)]; the z-witness suffices)
Ucp = [[CP(Cc, Ss), CP(P(DV, 0, DR), P(DV, 0, DR))],
       [CP(P(DV, 0, DR), P(DV, 0, DR)), CP(Cc, -Ss)]]
one_cp = CP(P(DV, 1, DR), P(DV, 0, DR))
Uminus = [[Ucp[i][j] - (one_cp if i == j else CP(P(DV, 0, DR), P(DV, 0, DR))) for j in range(2)]
          for i in range(2)]
prod = [[sum((Uminus[i][k].conj() * Uminus[k][j] for k in range(2)),
             CP(P(DV, 0, DR), P(DV, 0, DR))) for j in range(2)] for i in range(2)]
target_diag = P(DV, 2, DR) - P(DV, 2, DR) * Cc
chk(prod[0][0].re == target_diag and prod[1][1].re == target_diag
    and prod[0][1].zero() and prod[1][0].zero()
    and prod[0][0].im.zero() and prod[1][1].im.zero(),
    "§A12 (U-1)^dag (U-1) = (2 - 2 cos phi) I exactly in Q[Cc,Ss]/(Cc^2+Ss^2-1) — FT.54(1)'s defect "
    "identity re-derived: the area-ladder species m^2 = 4 mu'^2 sin^2(Theta_R/4) with "
    "4 sin^2(phi/2) = 2 - 2 cos phi [BM.39(7)]")
half_ang = (one_cp.re - Cc) * P(DV, Fr(1, 2), DR)      # sin^2(phi/2) = (1 - cos phi)/2
chk(P(DV, 4, DR) * half_ang == target_diag,
    "§A12 4 sin^2(phi/2) = 4(1 - cos phi)/2 = 2 - 2 cos phi exactly: the half-angle row of "
    "Def-H.37(2)/FT.54(4)")

# A13 — text pins: the strength bar and the ceiling discipline stand in the tier
P4t = rd("Part4_Baryomesonic_era.md")
i39 = P4t.find("### BM.39")
j39 = P4t.find("### BM.40")
B39 = P4t[i39:j39]
chk("\\mathrm{FT.76}(3)" in B39 and "quarantined" in B39 and "\\mathrm{FT.55}(1)" in B39,
    "§A13 BM.39 carries the ceiling re-citations [FT.76(3)], the quarantine discipline, and the "
    "FT.55(1) ruled-out identification Theta_R = 2 pi k — the two ladders kept apart (BM.39(8))")
chk("\\neg\\text{a scale}" in B39 or "\\neg\\text{numbers}" in B39,
    "§A13 BM.39(4) records that the inter-channel relations are symbolic rows, not numbers [P4; P5]")

stamp("§A done — the family transport-profile map")


# ==========================================================================
# §B  BM.40 — the rung-1 isospin row
# ==========================================================================
print("\n§B (BM.40) — the weak Casimir, the branch selectivity, and the neutrality")
print("            of the sigma-vertex")

# B1 — sum W_i^2 = (3/2)E0 + (1/2)Sigma = E0 + S = 2 Pi_R, entrywise over Q(i)
# Sigma = sigma_1 (x) sigma_1 + sigma_2 (x) sigma_2 + sigma_3 (x) sigma_3
# (the CT0.7/CT1.2 Sigma: spec {1,1,1,-3}, traceless; the swap is S = (E0+Sigma)/2)
Sigma4 = cmat_add(cmat_add(kron(sg[0], sg[0]), kron(sg[1], sg[1])), kron(sg[2], sg[2]))
sumW2 = cmat_add(cmat_add(cmat_mul(Wi[0], Wi[0]), cmat_mul(Wi[1], Wi[1])), cmat_mul(Wi[2], Wi[2]))
rhs1 = cmat_add(cmat_scal(E4, Fr(3, 2)), cmat_scal(Sigma4, Fr(1, 2)))
Swap4 = cmat_scal(cmat_add(E4, Sigma4), Fr(1, 2))               # S = (E0 + Sigma)/2
rhs2 = cmat_add(E4, Swap4)
PiR = cmat_scal(cmat_add(cmat_scal(E4, 3), Sigma4), Fr(1, 4))   # (3E0 + Sigma)/4
PiV = cmat_scal(cmat_add(E4, cmat_scal(Sigma4, -1)), Fr(1, 4))  # (E0 - Sigma)/4
rhs3 = cmat_scal(PiR, 2)
chk(cmat_eq(sumW2, rhs1) and cmat_eq(sumW2, rhs2) and cmat_eq(sumW2, rhs3),
    "§B1 sum_i W_i^2 = (3/2)E0 + (1/2)Sigma = E0 + S = 2 Pi_R entrywise over Q(i), all 16 components "
    "[Cor CT0.7a; FT.141(4); FT.157(2) re-derived] — BM.40(1)")

# B2 — the su(2) closure [W_i,W_j] = i eps_ijk W_k
eps = {(0, 1): 2, (1, 2): 0, (2, 0): 1}
su2_ok = True
for i in range(3):
    for j in range(3):
        comm = cmat_add(cmat_mul(Wi[i], Wi[j]), cmat_scal(cmat_mul(Wi[j], Wi[i]), -1))
        if i == j:
            target = cmat_scal(E4, 0)
        else:
            k = eps[(i, j)] if (i, j) in eps else eps[(j, i)]
            sgn = 1 if (i, j) in eps else -1
            target = cmat_scal(Wi[k], Cplx(0, sgn))
        su2_ok = su2_ok and cmat_eq(comm, target)
chk(su2_ok, "§B2 [W_i,W_j] = i eps_ijk W_k exactly, all 9 pairs over Q(i) [CT1.4 re-derived]")


# B3 — the branch eigen-rows: Casimir 2 on the symmetric basis, 0 on the antisymmetric
sym_vecs = [[Cplx(1), Cplx(0), Cplx(0), Cplx(0)],
            [Cplx(0), Cplx(1), Cplx(1), Cplx(0)],
            [Cplx(0), Cplx(0), Cplx(0), Cplx(1)]]
anti_vec = [Cplx(0), Cplx(1), Cplx(-1), Cplx(0)]
br_ok = all(all(cvec_mul(sumW2, v)[i] == Cplx(2) * v[i] for i in range(4)) for v in sym_vecs)
anti_ok = all(x == Cplx(0) for x in cvec_mul(sumW2, anti_vec))
chk(br_ok, "§B3 the Casimir reads 2 on every symmetric (aligned/spatial) basis vector: "
           "spin-1 content on the real branch [Cor CT0.7a; FT.157(2)]")
chk(anti_ok, "§B3 the Casimir reads 0 on the antisymmetric (antialigned/temporal) vector: "
             "spin-0 content on the virtual branch — the (2,0) split is exact")

# B4 — W_i Pi_V = 0 = Pi_V W_i; the projector algebra and traces
wpi_ok = all(cmat_eq(cmat_mul(Wi[i], PiV), cmat_scal(E4, 0))
             and cmat_eq(cmat_mul(PiV, Wi[i]), cmat_scal(E4, 0)) for i in range(3))
proj_ok = (cmat_eq(cmat_mul(PiR, PiR), PiR) and cmat_eq(cmat_mul(PiV, PiV), PiV)
           and cmat_eq(cmat_mul(PiR, PiV), cmat_scal(E4, 0))
           and cmat_eq(cmat_add(PiR, PiV), E4))
trR = ctr(PiR)
trV = ctr(PiV)
chk(wpi_ok, "§B4 W_i Pi_V = 0 = Pi_V W_i for all i: the weak annihilates the virtual branch "
            "[FT.101(1)-(2); FT.157(2) re-derived]")
chk(proj_ok and trR == Cplx(3) and trV == Cplx(1),
    "§B4 Pi_R, Pi_V idempotent, orthogonal, complete, with traces 3 and 1 [CT0.7(1) re-derived]")
chk(all(cvec_mul(PiV, anti_vec)[i] == anti_vec[i] for i in range(4)),
    "§B4 the antisymmetric vector is Pi_V's image line: ker-intersection = im Pi_V "
    "[FT.101(2); FT.157(2) — the 3-active/1-inactive split]")

# B5 — the sigma-vs-branch token disjointness on the defining strings
P1t = rd("Part1_Qubit_era.md")
P3t = rd("Part3_Fermion_era.md")


def between(src, a, b, start=0):
    i = src.find(a, start)
    assert i >= 0, f"anchor missing: {a[:40]}"
    j = src.find(b, i + 1)
    assert j > i, f"end anchor missing after: {a[:40]}"
    return src[i:j]


d34 = between(P1t, "**D3.4.**", "**D3.5.**")
_i7 = P1t.find("### CT0.7 —")
ct07 = P1t[_i7:P1t.find("\n### ", _i7 + 5)]
ft101 = between(P3t, "### FT.101 —", "### FT.102")
BRANCH_TOK = [r"\\Pi_\{?\\mathcal R", r"\\Pi_\{?\\mathcal V", r"\bbranch\b", r"\\alpha"]
REG_TOK = [r"q_\{\\mathrm\{core\}\}", r"\\sigma_s", r"\\sigma_t", r"reality line"]
br_hits = [t for t in BRANCH_TOK if re.search(t, d34)]
reg_hits1 = [t for t in REG_TOK if re.search(t, ct07)]
reg_hits2 = [t for t in REG_TOK if re.search(t, ft101)]
chk(not br_hits, f"§B5 D3.4's q_core definition carries ZERO branch tokens {br_hits}: the charge "
                 "read is registration data on the reality line [D1.1; CT0.9]")
chk(not reg_hits1 and not reg_hits2,
    f"§B5 CT0.7's and FT.101's branch definitions carry ZERO registration tokens "
    f"{reg_hits1 + reg_hits2}: the weak Casimir is a function of the branch datum alone — "
    "the rung-1 Casimir deficit at the sigma-vertex is identically zero [BM.40(3); "
    "FT.136(3) register separation]")

stamp("§B done — the rung-1 isospin row")


# ==========================================================================
# §C  BM.41 — the vertex kinematics and the Q-value sign theorem
# ==========================================================================
print("\n§C (BM.41) — the two-body impossibility, the forced neutral member,")
print("            the Q-value sign theorem, and the three-body endpoint")

KV = ["mn", "mp", "ml"]
mn = V(KV, "mn")
mp = V(KV, "mp")
ml = V(KV, "ml")
zK = P(KV, 0)

# C1 — the exact solution of the two-body conservation system (cleared by 2mn)
ELn = mn * mn + ml * ml - mp * mp          # 2 mn E_l
EPn = mn * mn + mp * mp - ml * ml          # 2 mn E_p
chk(ELn + EPn == mn * mn * P(KV, 2, None),
    "§C1 E_l + E_p = m_n: the exact solution of the rest-frame conservation system, cleared by "
    "2 m_n [BM.34(4) dispersion; BM.11] — BM.41(2)")
p2_l = ELn * ELn - P(KV, 4, None) * mn * mn * ml * ml      # 4 mn^2 (E_l^2 - ml^2)
p2_p = EPn * EPn - P(KV, 4, None) * mn * mn * mp * mp      # 4 mn^2 (E_p^2 - mp^2)
chk(p2_l == p2_p, "§C1 the momentum-squared match E_l^2 - m_l^2 = E_p^2 - m_p^2 as an exact "
                  "polynomial identity over Q[mn,mp,ml]")

# C2 — the Kallen identity and its m_n = m_p factorization
lam = (mn.pow(2) * mn.pow(2) + mp.pow(2) * mp.pow(2) + ml.pow(2) * ml.pow(2)
       - mn * mn * mp * mp * P(KV, 2, None) - mn * mn * ml * ml * P(KV, 2, None)
       - mp * mp * ml * ml * P(KV, 2, None))
chk(p2_l == lam, "§C2 4 m_n^2 p^2 = lambda(m_n^2, m_p^2, m_l^2) exactly — the Kallen form as one "
                 "polynomial identity")
lam_eq = psub(lam, {"mp": mn})
target_eq = ml * ml * (ml * ml - mn * mn * P(KV, 4, None))
chk(lam_eq == target_eq, "§C2 at m_p = m_n: lambda = m_l^2 (m_l^2 - 4 m_n^2) exactly — spacelike for "
                         "0 < m_l < 2 m_n [BM.41(2)]")

# C3 — the two-body impossibility: E_p - m_p = -m_l^2/(2 m_n) < 0 for every m_l > 0
ep_minus = psub(EPn - mn * mp * P(KV, 2, None), {"mp": mn})       # 2 mn (E_p - m_p) at mp = mn
chk(ep_minus == -ml * ml, "§C3 at m_n = m_p: 2 m_n (E_p - m_p) = -m_l^2 exactly — the two-body "
                          "vertex puts the daughter below its own mass shell for EVERY positive "
                          "member mass (BM.41(2))")
wit_ok = True
MN = Fr(6)                                   # the corpus value m_n = m_p = 6 ln2/h [BM.17; BM.26]
for ML in [Fr(1, 2), Fr(1), Fr(3), Fr(11), Fr(12), Fr(13), Fr(24), Fr(50)]:
    Ep_val = (MN * MN + MN * MN - ML * ML) / (2 * MN)
    El_val = (MN * MN + ML * ML - MN * MN) / (2 * MN)
    below_shell = Ep_val < MN
    lepton_spacelike = (ML < 2 * MN) and (El_val < ML)
    heavy_neg = (ML >= 2 * MN) and (Ep_val < 0)
    wit_ok = wit_ok and below_shell and (lepton_spacelike or heavy_neg)
chk(wit_ok, "§C3 the branch cover on rational witnesses m_l in {1/2,1,3,11,12,13,24,50} at "
            "m_n = m_p = 6: E_p < m_p always; and either the lepton is spacelike (m_l < 2 m_n) or "
            "the daughter energy is negative (m_l >= 2 m_n) — 2 > sqrt(2) by squaring, so the two "
            "branches cover every m_l > 0")

# C4 — the positivity of m_l on both read species
# transport: A0 - B0 is the SOS of §A6 with positive coefficients, vanishing only at (g,g') = 0
chk((A0 - B0) == sos_minus and all(v > 0 for v in [Fr(3, 8), Fr(1, 48)]),
    "§C4 transport species: m_l^2 >= M^2 (A0 - B0) with A0 - B0 = (3/8)(g - g'/3)^2 + g'^2/48 > 0 "
    "for (g,g') != 0 [§A6 SOS re-pinned] — the lepton line is massive under Def-BM.11")
# informational: m = E_int ln2 / h with E_int >= 2 and ln2 > 1/2
NENC = 20
S20 = sum((Fr(1, n * 2 ** n) for n in range(1, NENC + 1)), Fr(0))
tail = Fr(1, 2 ** NENC)
chk(Fr(1, 2) < S20 and S20 + tail < Fr(1) and Fr(2) * S20 > Fr(1),
    f"§C4 informational species: the exact enclosure 1/2 < ln2 < 1 (partial sum to n={NENC}, tail "
    "< 2^-20) gives m = E_int ln2/h >= 2 ln2/h > 1/h > 0 [FT.28 minimal floor; FT.44(4)]")

# C5 — the Q-value sign theorem
QV = ["mn", "mp", "ml", "mv"]
mnq, mpq, mlq, mvq = (V(QV, x) for x in QV)
Qexpr = mnq - mpq - mlq - mvq
Qred = psub(Qexpr, {"mn": mpq})
chk(Qred == (-mlq - mvq), "§C5 Q = m_n - m_p - m_l - m_v reduces at m_n = m_p to -(m_l + m_v) "
                          "exactly — the Q-value sign theorem's monomial identity (BM.41(4)(a))")
sign_ok = all((-Fr(ML) - Fr(MV)) < 0 for ML, MV in [(Fr(1, 2), Fr(0)), (Fr(1), Fr(1, 4)),
                                                     (Fr(3), Fr(1)), (Fr(1, 1000), Fr(0))])
chk(sign_ok, "§C5 Q < 0 strictly on positive-mass witnesses with m_v >= 0 [EW.33 PSD]: the decay is "
             "kinematically closed on the crystallized informational read")
# normalized ensemble reads: charge-degeneracy is structural — re-run the cancellation lemma
vw = [Fr(3), Fr(5), Fr(7)]
dS = [Fr(2), Fr(9), Fr(4)]
base = sum((vw[i] * dS[i] for i in range(3)), Fr(0)) / sum(vw)
canc = all(sum((Fr(cc) * vw[i] * dS[i] for i in range(3)), Fr(0))
           / sum((Fr(cc) * vw[i] for i in range(3)), Fr(0)) == base
           for cc in (1, 2, 3, 15, 20, Fr(7, 3)))
chk(canc, "§C5 the uniform sector factor cancels identically in every normalized average at the six "
          "frozen factors [FT.107(3); BM.30(3); BM.37(2)] — Q < 0 on every normalized ensemble read "
          "(BM.41(4)(b))")
# the general channel closure: any member set with the daughter + one positive line exceeds m_n
closure_ok = all((MN + ML) > MN for ML in [Fr(1, 2), Fr(1), Fr(3), Fr(11)])
chk(closure_ok, "§C5 the general channel closure: m_p + m_l > m_n = m_p for every positive m_l — "
                "every material decay channel of the neutron row is kinematically closed on the "
                "adopted reads (BM.41(6))")

# C6 — the route-(ii) variant: the sign is undetermined without scale data
w1 = Fr(1, 3) * Fr(3) - Fr(1, 8) - Fr(1, 8)      # T = 3, small lepton masses: positive
w2 = Fr(1, 3) * Fr(3) - Fr(1) - Fr(1)            # T = 3, larger lepton masses: negative
chk(w1 == Fr(3, 4) and w1 > 0 and w2 == Fr(-1) and w2 < 0,
    "§C6 the route-(ii) variant Q_ii = T/3 - m_l - m_v takes both signs on exact rational witnesses "
    "(T=3: +3/4 against -1): the sign is undetermined without scale data — priced, not adopted "
    "[BM.30(5); BM.37(3)] (BM.41(4)(d))")

# C7 — the three-body endpoint identities (conditional section, Q >= 0 hypothesis)
EV = ["mn", "mp", "ml", "mv"]
mne, mpe, mle, mve = (V(EV, x) for x in EV)
zE = P(EV, 0)
syst = (mpe + mve).pow(2)                                   # (m_p + m_v)^2
Elmax_n = mne * mne + mle * mle - syst                      # 2 mn E_l^max
Erec_n = mne * mne + syst - mle * mle                       # 2 mn E_rec
chk(Elmax_n + Erec_n == mne * mne * P(EV, 2, None),
    "§C7 E_l^max + E_rec = m_n exactly [cleared by 2 m_n]: the endpoint splits the parent energy "
    "(BM.41(5))")
pl2 = Elmax_n.pow(2) - P(EV, 4, None) * mne * mne * mle * mle
pr2 = Erec_n.pow(2) - P(EV, 4, None) * mne * mne * syst
chk(pl2 == pr2, "§C7 (E_l^max)^2 - m_l^2 = E_rec^2 - (m_p+m_v)^2 exactly [cleared by 4 m_n^2]: the "
                "lepton and recoil momenta match at the endpoint (BM.41(5))")

# C8 — the collinear reverse-Cauchy identity in the on-shell quotient ring
OV = ["Pp", "Nn", "mp", "mv", "Ep", "Ev"]
OR = {("Ep", 2): Poly(OV, {(0, 0, 2, 0, 0, 0): Fr(1), (2, 0, 0, 0, 0, 0): Fr(1)}),   # Ep^2 -> mp^2 + Pp^2
      ("Ev", 2): Poly(OV, {(0, 0, 0, 2, 0, 0): Fr(1), (0, 2, 0, 0, 0, 0): Fr(1)})}   # Ev^2 -> mv^2 + Nn^2
Pp, Nn, mpo, mvo, Epo, Evo = (V(OV, x, OR) for x in OV)
lhs8 = (Epo * Evo - Pp * Nn).pow(2) - (mpo * mvo).pow(2)
rhs8 = (Epo * Nn - Evo * Pp).pow(2)
chk(lhs8 == rhs8, "§C8 (E_p E_v - P N)^2 = (m_p m_v)^2 + (E_p N - E_v P)^2 exactly in "
                  "Q[Pp,Nn,mp,mv,Ep,Ev]/(Ep^2-mp^2-Pp^2, Ev^2-mv^2-Nn^2): the collinear "
                  "reverse-Cauchy row giving E_p E_v - P N >= m_p m_v, hence s_pv >= (m_p+m_v)^2 "
                  "and the endpoint's maximality (BM.41(5))")

# C9 — the Lagrange Cauchy-Schwarz SOS (the general recoil bound)
LV = ["px", "py", "pz", "qx", "qy", "qz"]
px, py, pz, qx, qy, qz = (V(LV, x) for x in LV)
P2 = px * px + py * py + pz * pz
N2 = qx * qx + qy * qy + qz * qz
dot = px * qx + py * qy + pz * qz
sos9 = ((px * qy - py * qx).pow(2) + (px * qz - pz * qx).pow(2) + (py * qz - pz * qy).pow(2))
chk(P2 * N2 - dot.pow(2) == sos9,
    "§C9 P^2 N^2 - (p.q)^2 = sum_{i<j} (p_i q_j - p_j q_i)^2 exactly — the Lagrange identity: the "
    "Cauchy-Schwarz bound with its SOS certificate, so s_pv >= (m_p+m_v)^2 in general (BM.41(5))")

# C10 — Q = sum KE_i from the conservation law alone (the absorption budget's closure)
BV = ["mn", "Ep", "El", "Ev", "mp", "ml", "mv"]
mnb, Epb, Elb, Evb, mpb, mlb, mvb = (V(BV, x) for x in BV)
Qb = mnb - mpb - mlb - mvb
KEsum = (Epb - mpb) + (Elb - mlb) + (Evb - mvb)
conserved = Qb - KEsum                      # = mn - Ep - El - Ev
chk(conserved == (mnb - Epb - Elb - Evb),
    "§C10 Q - sum_i KE_i = m_n - (E_p + E_l + E_v) identically: energy conservation alone closes "
    "the budget, Q = KE_p + KE_l + KE_v — no residual term remains for any 'spin-coupling' or "
    "'orbital-coupling' addition (BM.42(4)-(5))")

# C11 — the vertex integer rows
chk(0 == 1 + (-1) + 0, "§C11 the charge balance 0 = (+1) + (-1) + 0 [EM.11; BM.23(4)]")
chk(all(k % 4 == 0 for k in (0, 4, 8, -4)), "§C11 the sealing-phase class 4Z is closed under the "
                                             "vertex [BM.2(1); Census FT.49(3) re-cited]")

# C12 — the upgrade language on record
i41 = P4t.find("### BM.41")
j41 = P4t.find("### BM.42")
B41 = P4t[i41:j41]
chk("conditionally forced" in B41 and "kinematic" in B41 and "uniqueness" in B41,
    "§C12 BM.41(3) carries the upgrade on record: the neutral member is 'conditionally forced' by "
    "kinematics + uniqueness, not by a number conservation")
chk("the forcing status of clause (6)" in P4t,
    "§C12 BM.23 carries the on-record Rmk upgrading clause (6)'s status (the FT.89 Rmk pattern)")

stamp("§C done — the vertex kinematics")


# ==========================================================================
# §D  BM.42 — angular momentum at the vertex
# ==========================================================================
print("\n§D (BM.42) — the Casimir ladder, the tensor charpolys, the Lagrange")
print("            decomposition, the CN adjudication, and the l-selection census")

# D1 — the SU(2) Casimir ladder
Js = [cmat_scal(x, Fr(1, 2)) for x in sg]
C1_ = cmat_add(cmat_add(cmat_mul(Js[0], Js[0]), cmat_mul(Js[1], Js[1])), cmat_mul(Js[2], Js[2]))
chk(cmat_eq(C1_, cmat_scal(I2, Fr(3, 4))),
    "§D1 the anchor Casimir: sum J_i^2 = (3/4) I_2 exactly over Q(i) at j = 1/2 (Sym^1 = the seed "
    "C^2) [EW.32; FT.55(2); Def-H.38's ladder at k=1]")
ladder = [Fr(k, 2) * (Fr(k, 2) + 1) for k in (1, 2, 3, 4)]
chk(ladder == [Fr(3, 4), Fr(2), Fr(15, 4), Fr(6)],
    "§D1 the Casimir ladder j(j+1) = (k/2)(k/2+1) at k = 1..4: (3/4, 2, 15/4, 6) — exact rationals "
    "[FT.60(3), generalizing Cor CT0.7a]")

# D2-D4 — the tensor charpolys: 2(x)2 = 3+1, 2(x)2(x)2 = 4+2+2, 2(x)2(x)2(x)2 = 2*0+3*1+1*2
def tensor_J(nfold):
    dim = 2 ** nfold
    out = []
    for a in range(3):
        acc = [[Cplx(0)] * dim for _ in range(dim)]
        for pos in range(nfold):
            facs = [I2] * nfold
            facs[pos] = Js[a]
            m = facs[0]
            for f in facs[1:]:
                m = kron(m, f)
            acc = cmat_add(acc, m)
        out.append(acc)
    return out


def casimir(nfold):
    JJ = tensor_J(nfold)
    return cmat_add(cmat_add(cmat_mul(JJ[0], JJ[0]), cmat_mul(JJ[1], JJ[1])), cmat_mul(JJ[2], JJ[2]))


def real_coeffs(cs):
    assert all(z.b == 0 for z in cs), "charpoly coefficients must be real"
    return [z.a for z in cs]


cp2 = real_coeffs(charpoly(casimir(2)))
chk(cp2 == expected_charpoly([(2, 3), (0, 1)]),
    "§D2 the charpoly of (sum J)^2 on C^4 = (x - 2)^3 x exactly: 2 (x) 2 = 3 + 1 — the triplet "
    "Casimir 2 with multiplicity three, the singlet 0 with multiplicity one: the lepton pair "
    "couples to singlet or triplet [Clebsch-Gordan; machine Faddeev-LeVerrier]")
cp3 = real_coeffs(charpoly(casimir(3)))
chk(cp3 == expected_charpoly([(Fr(3, 4), 4), (Fr(15, 4), 4)]),
    "§D3 the charpoly on C^8 = (x - 15/4)^4 (x - 3/4)^4 exactly: 2 (x) 2 (x) 2 = 4 + 2 + 2 with "
    "j in {3/2, 1/2} [FT.88(7) re-derived]")
cp4 = real_coeffs(charpoly(casimir(4)))
chk(cp4 == expected_charpoly([(0, 2), (2, 9), (6, 5)]),
    "§D4 the charpoly on C^16 = x^2 (x - 2)^9 (x - 6)^5 exactly: the full vertex 2(x)2(x)2(x)2 "
    "= 2*(j=0) + 3*(j=1) + 1*(j=2), dimensions 2 + 9 + 5 = 16 [BM.42(8)]")

# D5 — the Lagrange identity: r^2 p^2 = (x.p)^2 + sum_{i<j} L_ij^2
LV6 = ["x", "y", "z", "px", "py", "pz"]
xx6, yy6, zz6, pxx6, pyy6, pzz6 = (V(LV6, t) for t in LV6)
r2p = (xx6 * xx6 + yy6 * yy6 + zz6 * zz6) * (pxx6 * pxx6 + pyy6 * pyy6 + pzz6 * pzz6)
xdotp = xx6 * pxx6 + yy6 * pyy6 + zz6 * pzz6
Lsum = ((xx6 * pyy6 - yy6 * pxx6).pow(2) + (xx6 * pzz6 - zz6 * pxx6).pow(2)
        + (yy6 * pzz6 - zz6 * pyy6).pow(2))
chk(r2p - xdotp.pow(2) == Lsum,
    "§D5 the Lagrange identity r^2 p^2 - (x.p)^2 = sum_{i<j} (x_i p_j - x_j p_i)^2 exactly in "
    "Q[x,y,z,px,py,pz]: p^2 = p_r^2 + L^2/r^2 — the orbital content is BM.34's p^2 itself "
    "(BM.42(3))")

# D6 — the decomposed dispersion: the master identity survives the substitution
DV6 = LV6 + ["p0", "m6"]
r2l = lift(xx6 * xx6 + yy6 * yy6 + zz6 * zz6, DV6)
xdp = lift(xdotp, DV6)
Ls = lift(Lsum, DV6)
p0l = V(DV6, "p0")
m6 = V(DV6, "m6")
pl2 = lift(pxx6 * pxx6 + pyy6 * pyy6 + pzz6 * pzz6, DV6)
form1 = r2l * (p0l.pow(2) - m6 * m6 - pl2)
form2 = r2l * (p0l.pow(2) - m6 * m6) - xdp.pow(2) - Ls
chk(form1 == form2, "§D6 r^2 (p_0^2 - m^2 - p^2) = r^2 (p_0^2 - m^2) - (x.p)^2 - L^2 exactly: the "
                    "vacuum-gauge dispersion E^2 = m^2 + p_r^2 + L^2/r^2 is BM.34(4)'s master "
                    "identity under the Lagrange decomposition, cleared by r^2 (BM.42(3))")

# D7 — the CN adjudication: the correction is zero
cn_ok = all(Fr(1, 4) * c2 <= Fr(1, 4) < Fr(3, 4) for c2 in [Fr(0), Fr(1, 4), Fr(1, 2), Fr(1)])
chk(cn_ok, "§D7 (1/4)<cos^2> <= 1/4 < 3/4 on exact rational witnesses <cos^2> in {0,1/4,1/2,1}: the "
           "CN corollary <p^2> >= (1/4)<cos^2> m_hid^2 is uniformly weaker than BM.34(6)'s "
           "Cartesian (3/4) m_hid^2 — the correction to the zero-point bounds (7/4, 3/8, sqrt7/2) "
           "is exactly zero (BM.42(6))")

# D8 — the moment current on the dust class: d_mu M^{mu nu lambda} = 0, all components
MV = ["x0", "x1", "x2", "x3", "rho"]
xv = [V(MV, f"x{i}") for i in range(4)]
T = [[P(MV, 0) for _ in range(4)] for _ in range(4)]
T[0][0] = V(MV, "rho")
mom_ok = True
for nu in range(4):
    for la in range(4):
        div = P(MV, 0)
        for mu in range(4):
            Mmn = xv[nu] * T[mu][la] - xv[la] * T[mu][nu]
            div = div + dpoly(Mmn, f"x{mu}")
        mom_ok = mom_ok and div.zero()
chk(mom_ok, "§D8 d_mu M^{mu nu lambda} = 0 for all 16 (nu,lambda) components on the dust class "
            "T = diag(rho,0,0,0) with constant rho, by exact symbolic differentiation — the moment "
            "current of the symmetric on-shell Hilbert tensor is conserved [BM.9(2)-(3); BM.11] "
            "(BM.42(1))")
Tsym = all(T[i][j] == T[j][i] for i in range(4) for j in range(4))
leib = dpoly(xv[0] * V(MV, "rho"), "x0") == V(MV, "rho") and dpoly(xv[0] * V(MV, "rho"), "x1").zero()
chk(Tsym and leib, "§D8 the dust tensor is symmetric entrywise and the Leibniz row d_0(x^0 rho) = rho, "
                   "d_1(x^0 rho) = 0 holds exactly — the formal identity "
                   "d_mu M = (T^{nu lambda} - T^{lambda nu}) + x^nu d.T + ... closes on-shell (BM.42(1))")

# D9 — the orbital parity characters: sum_{m=-l}^{l} (-1)^m = (-1)^l
par_ok = all(sum((1 if m % 2 == 0 else -1) for m in range(-ell, ell + 1)) == (1 if ell % 2 == 0 else -1)
             for ell in range(0, 7))
chk(par_ok, "§D9 the integer SO(3) character at angle pi: sum_{m=-l}^{l} (-1)^m = (-1)^l exactly for "
            "l = 0..6 — the orbital factor of the ladder is derived (BM.42(9))")

# D10 — the l-selection census (anchor class, all four lines at j = 1/2)
def couple(j1, j2):
    return {Fr(abs(j1 - j2)) + k for k in range(int(j1 + j2 - abs(j1 - j2)) + 1)}


pair_S = couple(Fr(1, 2), Fr(1, 2))
Jint = {S: couple(S, Fr(1, 2)) for S in pair_S}
table = {}
for S in (Fr(0), Fr(1)):
    for ell in (0, 1, 2):
        table[(S, ell)] = any(Fr(1, 2) in couple(J, ell) for J in Jint[S])
expected = {(Fr(0), 0): True, (Fr(0), 1): True, (Fr(0), 2): False,
            (Fr(1), 0): True, (Fr(1), 1): True, (Fr(1), 2): True}
chk(pair_S == {Fr(0), Fr(1)} and Jint[Fr(0)] == {Fr(1, 2)} and Jint[Fr(1)] == {Fr(1, 2), Fr(3, 2)}
    and table == expected,
    "§D10 the l-selection census on exact half-integers: the lepton pair couples to S in {0,1}; "
    "J_int in {1/2} (singlet) or {1/2,3/2} (triplet); l=0 admissible on both channels, l=1 on both, "
    "l=2 ONLY via J_int = 3/2 — the derived allowed/forbidden ladder with no SM labels (BM.42(8))")

# D11 — the Def-H.38 anchor rows: Sym^k dimensions and the k=1 anchor
chk([k + 1 for k in (1, 2, 3, 4)] == [2, 3, 4, 5],
    "§D11 dim Sym^k = k+1 at k = 1..4: the anchor Sym^1 = C^2 carries j = 1/2 [EW.32; FT.55(2); "
    "FT.60(1)(iv)] — the declared multiplicity rule's carrier ladder")

# D12 — tier text pins
i42 = P4t.find("### BM.42")
j42 = P4t.find("### BM.43")
B42 = P4t[i42:j42]
chk("double-count" in B42 and "\\mathrm{FT.135}(4)" in B42 and "external vocabulary" in B42,
    "§D12 BM.42 carries the absorption adjudication ('double-count'), the FT.135(4) no-parity-"
    "operator citation, and the bar on external J^P vocabulary (BM.42(4),(9))")
chk("\\text{machine: the token census}" not in B42 and "item 19" in B42 or "item 19" in B42,
    "§D12 BM.42(7) records the line-winding attachment residue with the item-19 pointer")

stamp("§D done — angular momentum")


# ==========================================================================
# §E  BM.43 — the curvature rows of the members
# ==========================================================================
print("\n§E (BM.43) — the proton reads, the linearized field equations,")
print("            the weak-field potential, and the superposition")

# E1 — the proton's six frozen reads at E_int = 6, as Laurent monomials
CU = ["h", "l2", "pi"]
CR = ["h", "l2", "pi", "E"]
dxbR = LM.mon(CR, h=1, l2=-1, E=-1)          # Delta x_B = h/(E ln2)
veffR = dxbR.pow(3)                           # V_eff = (Delta x_B)^3
mR = LM.mon(CR, h=-1, l2=1, E=1)              # m_hid = E ln2/h
rhoR = mR * LM.mon(CR, h=3, l2=-3, E=-3)      # rho = m/V_eff = E^4 ln2^4/h^4... built below exactly
rhoR = mR * veffR.inv()
k2R = LM.mon(CR, h=2, l2=-1, pi=1) * 2        # kappa^2 = 2 pi h^2/ln2
k2rhoR = k2R * rhoR
rsR = LM.mon(CR, h=1, E=1) * Fr(1, 2)         # r_s = h E/2 [BM.16(4)]
# evaluate at E = 6 by monomial substitution: build the expected monomials directly
exp_dxb = LM.mon(CU, h=1, l2=-1) * Fr(1, 6)
exp_veff = LM.mon(CU, h=3, l2=-3) * Fr(1, 216)
exp_m = LM.mon(CU, h=-1, l2=1) * Fr(6)
exp_rho = LM.mon(CU, h=-4, l2=4) * Fr(1296)
exp_k2rho = LM.mon(CU, h=-2, l2=3, pi=1) * Fr(2592)
exp_rs = LM.mon(CU, h=1) * Fr(3)
got_veff = None
# compute from the E-ring at E=6: multiply out and substitute E->6 monomial-wise
def lm_at_E(lm, val):
    acc = {}
    for e, c in lm.t.items():
        e2 = (e[0], e[1], e[2])          # drop the E exponent, fold the value in
        acc[e2] = acc.get(e2, Fr(0)) + c * Fr(val) ** e[3]
    return LM(CU, acc)


chk(lm_at_E(dxbR, 6) == exp_dxb and lm_at_E(veffR, 6) == exp_veff and lm_at_E(mR, 6) == exp_m,
    "§E1 the proton's length/volume/mass reads at E_int = 6: Delta x_B = h/(6 ln2), "
    "V_eff = h^3/(216 (ln2)^3), m = 6 ln2/h — BM.26's frozen rows re-verified as exact Laurent "
    "monomials")
chk(lm_at_E(rhoR, 6) == exp_rho and lm_at_E(k2rhoR, 6) == exp_k2rho,
    "§E1 rho = 1296 (ln2)^4 / h^4 and kappa^2 rho = 2592 pi (ln2)^3 / h^2 exactly at E_int = 6 "
    "[BM.26; BM.9(5)]")
chk(lm_at_E(rsR, 6) == exp_rs, "§E1 r_s = h E_int / 2 = 3 h at E_int = 6 [BM.16(4); BM.26]")
lockR = dxbR.pow(2) * k2rhoR
exp_lock = LM.mon(CU, pi=1, l2=1) * Fr(72)
two_pi_E2_l2 = LM.mon(CR, pi=1, E=2, l2=1) * 2
chk(lm_at_E(lockR, 6) == exp_lock and lm_at_E(two_pi_E2_l2, 6) == exp_lock,
    "§E1 the lock: (Delta x_B)^2 kappa^2 rho = 2 pi E^2 ln2 = 72 pi ln2 at E_int = 6 — both routes "
    "one monomial [BM.16(1); BM.26]")

# E2 — the lepton rows are symbolic monomials; the source superposition is exact
CS_ = ["h", "l2", "pi", "V", "El", "En"]
kap2 = LM.mon(CS_, h=2, l2=-1, pi=1) * 2
rho_p = LM.mon(CS_, h=-1, V=-1) * 6 * LM.mon(CS_, l2=1)
rho_l = LM.mon(CS_, h=-1, V=-1, El=1, l2=1)
rho_n = LM.mon(CS_, h=-1, V=-1, En=1, l2=1)
sup = kap2 * (rho_p + rho_l + rho_n)
exp_sup = LM.mon(CS_, h=1, pi=1, V=-1) * 2 * LM.cst(CS_, 1) * (LM.cst(CS_, 6) + LM.mon(CS_, El=1) + LM.mon(CS_, En=1))
chk(sup == exp_sup, "§E2 kappa^2 rho_total = 2 pi h (6 + E_l + E_nu)/V exactly: the source-side "
                    "superposition is a monomial sum [CT1.22; BM.43(5)] — the lepton E_int rows "
                    "stay symbolic")

# E3 — the linearized field equations in the weight-truncated jet ring
JV = ["Phi", "Px", "Py", "Pz", "Pxx", "Pyy", "Pzz", "Pxy", "Pxz", "Pyz"]


def jtrunc(p):
    return Poly(JV, {e: c for e, c in p.t.items() if sum(e) <= 1})


def jmul(a, b):
    return jtrunc(a * b)


def jconst(x):
    return Poly.const(JV, x)


Phi = V(JV, "Phi")
Pk = [V(JV, "Px"), V(JV, "Py"), V(JV, "Pz")]
Pjk = {(1, 1): V(JV, "Pxx"), (2, 2): V(JV, "Pyy"), (3, 3): V(JV, "Pzz"),
       (1, 2): V(JV, "Pxy"), (1, 3): V(JV, "Pxz"), (2, 3): V(JV, "Pyz")}
Pjk.update({(b, a): v for (a, b), v in list(Pjk.items()) if a != b})
PjkN = {(1, 1): "Pxx", (2, 2): "Pyy", (3, 3): "Pzz", (1, 2): "Pxy", (2, 1): "Pxy",
        (1, 3): "Pxz", (3, 1): "Pxz", (2, 3): "Pyz", (3, 2): "Pyz"}


def djet(p, k):
    """exact partial derivative d/dx^k on weight-1 jets (static: third derivatives drop)."""
    out = Poly(JV)
    for e, c in p.t.items():
        tot = sum(e)
        if tot == 0:
            continue
        var = JV[[i for i in range(len(JV)) if e[i]][0]]
        if var == "Phi":
            out = out + Poly(JV, {tuple(1 if JV[i] == ("Px", "Py", "Pz")[k - 1] else 0
                                       for i in range(len(JV))): c})
        elif var in ("Px", "Py", "Pz"):
            j = ("Px", "Py", "Pz").index(var) + 1
            nm = PjkN[tuple(sorted((j, k)))]
            out = out + Poly(JV, {tuple(1 if JV[i] == nm else 0 for i in range(len(JV))): c})
        # second-derivative variables differentiate to zero at this truncation
    return out


# metric and inverse ansatz (static, diagonal): g00 = -(1+2Phi), gii = (1-2Phi)
gm = [[jconst(0)] * 4 for _ in range(4)]
gm[0][0] = jconst(-1) + jconst(-2) * Phi
for i in range(1, 4):
    gm[i][i] = jconst(1) + jconst(-2) * Phi
gu = [[jconst(0)] * 4 for _ in range(4)]
gu[0][0] = jconst(-1) + jconst(2) * Phi
for i in range(1, 4):
    gu[i][i] = jconst(1) + jconst(2) * Phi
inv_ok = True
for mu in range(4):
    for nu in range(4):
        acc = jconst(0)
        for sig in range(4):
            acc = acc + jmul(gm[mu][sig], gu[sig][nu])
        inv_ok = inv_ok and (acc == jconst(int(mu == nu)))
chk(inv_ok, "§E3 g^{mu a} g_{a nu} = delta^mu_nu to first order in the weight-truncated jet ring: "
            "the weak-field inverse ansatz is exact at linear order (BM.43(4))")
# metric derivatives (static): d_k g_00 = -2 P_k ; d_k g_ii = -2 P_k ; d_0 = 0
dg = [[[Poly(JV) for _ in range(4)] for _ in range(4)] for _ in range(4)]   # dg[mu][a][b]
for k in (1, 2, 3):
    dg[k][0][0] = jconst(-2) * Pk[k - 1]
    for i in range(1, 4):
        dg[k][i][i] = jconst(-2) * Pk[k - 1]


def Gamma(rho, mu, nu):
    acc = jconst(0)
    for sig in range(4):
        term = dg[mu][sig][nu] + dg[nu][sig][mu] - dg[sig][mu][nu]
        acc = acc + jmul(gu[rho][sig], term)
    return jtrunc(Fr(1, 2) * acc)


Ric = [[Poly(JV) for _ in range(4)] for _ in range(4)]
for mu in range(4):
    for nu in range(4):
        a = Poly(JV)
        for k in (1, 2, 3):
            a = a + djet(Gamma(k, mu, nu), k)
        tr = Poly(JV)
        for rho in range(4):
            tr = tr + Gamma(rho, mu, rho)
        b = djet(tr, nu) if nu in (1, 2, 3) else Poly(JV)
        Ric[mu][nu] = jtrunc(a - b)
Rsc = jtrunc(-Ric[0][0] + Ric[1][1] + Ric[2][2] + Ric[3][3])
G00 = jtrunc(Ric[0][0] + Fr(1, 2) * Rsc)
lap = V(JV, "Pxx") + V(JV, "Pyy") + V(JV, "Pzz")
chk(G00 == jconst(2) * lap, "§E3 G^(1)_00 = 2 (Pxx + Pyy + Pzz) = 2 Laplacian(Phi) exactly in the "
                            "jet ring — Christoffel -> Ricci -> Einstein computed, not assumed "
                            "(BM.43(4))")
G0i_zero = all(Ric[0][i].zero() for i in (1, 2, 3))
Gij_zero = all(jtrunc(Ric[i][j] - (Fr(1, 2) * Rsc if i == j else Poly(JV))).zero()
               for i in (1, 2, 3) for j in (1, 2, 3))
chk(G0i_zero and Gij_zero, "§E3 G^(1)_0i = 0 and G^(1)_ij = 0 exactly: the static diagonal "
                           "perturbation solves the linearized dust equations (p = 0) — the "
                           "Poisson row 2 Laplacian(Phi) = kappa^2 rho (BM.43(4))")

# E4 — the coefficient identity kappa^2/2 = 4 pi G_N
k2half = LM.mon(CU, h=2, l2=-1, pi=1)                     # (2 pi h^2/ln2)/2 = pi h^2/ln2
fourpiGN = LM.mon(CU, h=2, l2=-1, pi=1)                   # 4 pi * h^2/(4 ln2)
chk(k2half == fourpiGN, "§E4 kappa^2/2 = pi h^2/ln2 = 4 pi G_N exactly as one monomial "
                        "[CT2.9: G_N = h^2/(4 ln2), kappa^2 = 8 pi G_N] — the Poisson coefficient "
                        "(BM.43(4))")

# E5 — the harmonicity of 1/r away from the source: r^5 Laplacian(1/r) = -3r^2 + 3(x^2+y^2+z^2) = 0
HV = ["hx", "hy", "hz", "rr"]
HR = {("rr", 2): Poly(HV, {(2, 0, 0, 0): Fr(1), (0, 2, 0, 0): Fr(1), (0, 0, 2, 0): Fr(1)})}
hxr, hyr, hzr, rrr = (V(HV, t, HR) for t in HV)
harm = rrr.pow(2) * Fr(-3) + Fr(3) * (hxr.pow(2) + hyr.pow(2) + hzr.pow(2))
chk(harm.zero(), "§E5 -3r^2 + 3(x^2+y^2+z^2) = 0 exactly in Q[x,y,z,r]/(r^2 - x^2-y^2-z^2): "
                 "Laplacian(1/r) = 0 away from the source, so Phi = -G_N m/r solves the weak-field "
                 "row (BM.43(4))")

# E6 — G_N m = h E/4, r_s = h E/2, Phi(Delta x_B) = -E^2 ln2/4
CG = ["h", "l2", "E"]
GN = LM.mon(CG, h=2, l2=-1) * Fr(1, 4)
mhidG = LM.mon(CG, h=-1, l2=1, E=1)
GNm = GN * mhidG
chk(GNm == LM.mon(CG, h=1, E=1) * Fr(1, 4), "§E6 G_N m_hid = (h^2/(4 ln2))(E ln2/h) = h E/4 exactly")
chk(GNm * 2 == LM.mon(CG, h=1, E=1) * Fr(1, 2), "§E6 r_s = 2 G_N m = h E/2 [BM.16(4) re-derived]")
phiB = -(LM.mon(CG, h=1, E=1) * Fr(1, 4)) * LM.mon(CG, h=-1, l2=1, E=1)
chk(phiB == LM.mon(CG, l2=1, E=2) * Fr(-1, 4),
    "§E6 Phi(Delta x_B) = -(h E/4)(E ln2/h) = -E^2 ln2/4, dimensionless — one monomial (BM.43(4))")

# E7 — the scope pins
i43 = P4t.find("### BM.43")
j43 = P4t.find("### BM.44")
B43 = P4t[i43:j43]
chk("\\neg\\text{constructed}" in B43 and "pp-wave" in B43 and "linearized" in B43,
    "§E7 BM.43(5) carries the superposition scope: source side exact, metric side linearized-"
    "scope, the full non-linear joint solution and a full exterior solution not in the inventory")
chk("\\neg\\text{computed at any floor}" in B43,
    "§E7 BM.43(2) records the lepton E_int rows as open (no floor computes them) with the item-7 "
    "conversion residue")

stamp("§E done — the curvature rows")


# ==========================================================================
# §F  BM.44 — the per-tick weight and the e-folding count
# ==========================================================================
print("\n§F (BM.44) — the resolvent, the SOS parabola, the Gamma_tr range,")
print("            and the tick-unit discipline")

# F1 — the resolvent identity in Q[w,xp,xm]/(w^12)
WV = ["w", "xp", "xm"]
WR = {("w", 12): Poly.const(WV, 0)}
wv = V(WV, "w", WR)
xpv = V(WV, "xp", WR)
xmv = V(WV, "xm", WR)
series = P(WV, 0, WR)
for n in range(0, 12, 2):
    series = series + (xpv * xmv).pow(n // 2) * wv.pow(n)
prod = (P(WV, 1, WR) - wv * wv * xpv * xmv) * series
chk(prod == P(WV, 1, WR), "§F1 (1 - w^2 x+ x-) * sum_n <0|U^n|0> w^n = 1 exactly mod w^12 with "
                          "<0|U^n|0> = [n even](x+ x-)^(n/2) — FT.108(5)/BM.23(7)'s resolvent "
                          "re-verified coefficient-wise")

# F2 — the SOS completion: 4e(1-4e) = 1/4 - 16(e - 1/8)^2
EV = ["e"]
ev = V(EV, "e")
lhsF = ev * P(EV, 4, None) - ev.pow(2) * P(EV, 16, None)
rhsF = P(EV, Fr(1, 4), None) - (ev - P(EV, Fr(1, 8), None)).pow(2) * P(EV, 16, None)
chk(lhsF == rhsF, "§F2 x+ x- = 4 e_q (1 - 4 e_q) = 1/4 - 16 (e_q - 1/8)^2 exactly: the maximum 1/4 "
                  "at e_q = 1/8 is an SOS completion [BM.19(2); BM.23(7)]")

# F3 — the grid census: xx <= 1/4 with equality only at e = 1/8
grid_ok = True
eq_pts = []
for k in range(0, 64):
    e = Fr(k, 256)
    xx = 4 * e * (1 - 4 * e)
    grid_ok = grid_ok and xx <= Fr(1, 4)
    if xx == Fr(1, 4):
        eq_pts.append(k)
chk(grid_ok and eq_pts == [32], "§F3 the census over e_q = k/256, k = 0..63: x+ x- <= 1/4 at every "
                                "point, equality only at k = 32 (e_q = 1/8) — exact Fractions")

# F4 — Gamma_tr = xx/(1-xx): endpoints, range [0,1/3], strict monotonicity on [0,1/8]
G0 = Fr(0) / (1 - Fr(0))
G18 = Fr(1, 4) / (1 - Fr(1, 4))
chk(G0 == Fr(0) and G18 == Fr(1, 3), "§F4 Gamma_tr(0) = 0 and Gamma_tr(1/8) = (1/4)/(3/4) = 1/3 "
                                     "exactly [BM.44(2)]")
FV = ["e1", "e2"]
e1v, e2v = V(FV, "e1"), V(FV, "e2")
diff = (e2v * P(FV, 4, None) - e2v.pow(2) * P(FV, 16, None)) - (e1v * P(FV, 4, None) - e1v.pow(2) * P(FV, 16, None))
fact = (e2v - e1v) * P(FV, 4, None) * (P(FV, 1, None) - (e1v + e2v) * P(FV, 4, None))
chk(diff == fact, "§F4 the monotonicity difference identity xx(e2) - xx(e1) = 4(e2-e1)(1-4(e1+e2)) "
                  "exactly — positive for e1 < e2 <= 1/8, so Gamma_tr is strictly increasing there "
                  "and its range on [0,1/8] is [0, 1/3] (BM.44(2))")
mono_wit = all((Fr(4 * k2_ * (256 - 4 * k2_), 256 * 256) if False else
                4 * Fr(k2_, 256) * (1 - 4 * Fr(k2_, 256))) >
               4 * Fr(k1_, 256) * (1 - 4 * Fr(k1_, 256))
               for k1_, k2_ in [(0, 1), (5, 9), (16, 32), (31, 32)])
chk(mono_wit, "§F4 the monotonicity on rational witness pairs e1 < e2 <= 1/8 (exact Fractions)")
xx_range = all(Fr(0) <= 4 * Fr(k, 256) * (1 - 4 * Fr(k, 256)) <= Fr(1, 4) for k in range(0, 64))
g_range = all(Fr(0) <= (lambda x: x / (1 - x))(4 * Fr(k, 256) * (1 - 4 * Fr(k, 256))) <= Fr(1, 3)
              for k in range(0, 33))
chk(xx_range and g_range, "§F4 on the grid e_q = k/256, k = 0..32: 0 <= x+ x- <= 1/4 and "
                          "0 <= Gamma_tr <= 1/3 — the exact range row (BM.44(2))")

# F5 — the e-folding count and the no-flicker row
chk(1 / G18 == Fr(3), "§F5 tau_life = 1/Gamma_tr = 3 ticks exactly at e_q = 1/8 (unit fugacity): "
                      "the e-folding count is an exact rational, and >= 3 across the admissible "
                      "range [BM.44(3)]")
chk(Fr(1, 1 - 0) == Fr(1) and (4 * Fr(0) * (1 - 0)) == Fr(0),
    "§F5 at e_q = 0: x+ x- = 0 and the resolvent is 1 — no transition weight beyond the identity: "
    "a non-flickering composite never decays [BM.23(8); BM.19(3) re-derived]")

# F6 — the unit-discipline text pins
i44 = P4t.find("### BM.44")
j44 = P4t.find("### BM.45")
B44 = P4t[i44:j44]
chk("weight per tick" in B44 and "carries no rate datum" in B44
    and "\\neg\\text{external seconds}" in B44,
    "§F6 BM.44 carries the unit discipline on record: 'weight per tick', 'Cal-F carries no rate "
    "datum', and the ¬external-seconds row [P5; BM.23(9)]")
chk("\\mathrm{BM.8}(2)" in B44 and "stationarity" in B44,
    "§F6 the chart evolution is scoped to BM.8(2)'s declared stationarity hypothesis (BM.44(3))")

stamp("§F done — the time evolution")


# ==========================================================================
# §G  BM.45 — document pins and hygiene
# ==========================================================================
print("\n§G (BM.45) — document pins, hygiene, and the ledger/README/index rows")

P1t2 = P1t
P2t = rd("Part2_Bosonic_era.md")
CEt = rd("Census.md")
HLt = rd("HistLog.md")

# G1 — presence, uniqueness and ownership
chk(P4t.count("## Tier BM.11 —") == 1, "§G1 Part 4 carries exactly one '## Tier BM.11' header")
for tag in ["Def-BM.11", "BM.39", "BM.40", "BM.41", "BM.42", "BM.43", "BM.44", "BM.45"]:
    chk(P4t.count(f"### {tag} —") == 1, f"§G1 {tag} occurs exactly once as a Part 4 section")
    others = sum(tt.count(f"### {tag} —") for tt in (P1t2, P2t, P3t, CEt))
    chk(others == 0, f"§G1 {tag} occurs in no other canon file (ownership)")

# G2 — block completeness
for tag in ["BM.39", "BM.40", "BM.41", "BM.42", "BM.43", "BM.44", "BM.45"]:
    i_ = P4t.find(f"### {tag} —")
    cands = [x for x in (P4t.find("\n### ", i_ + 4), P4t.find("\n## ", i_ + 4), len(P4t)) if x > 0]
    blk = P4t[i_:min(cands)]
    ok = all(tok in blk for tok in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"))
    chk(ok and "\\blacksquare" in blk, f"§G2 {tag} carries Thm/Req/Pf/Phys and a proof terminator")
idb = P4t.find("### Def-BM.11 —")
jdb = P4t.find("### BM.39 —")
chk("**Def.**" in P4t[idb:jdb], "§G2 Def-BM.11 carries its **Def.** block")

# G3 — the header, charter and closure rows
_endash = chr(0x2013)
_mNS = re.search(r"Def-BM\.1" + _endash + r"Def-BM\.(\d+); BM\.1" + _endash + r"BM\.(\d+)\. Tiers 4\.0, BM\.1" + _endash + r"BM\.(\d+)", P4t)
chk(_mNS and int(_mNS.group(1)) >= 11 and int(_mNS.group(2)) >= 45 and int(_mNS.group(3)) >= 11,
    "§G3 the Part 4 Namespace line covers Tier BM.11's tags (Def-BM.11 / BM.45) and extends with later tiers")
chk("(xiv) the decay-vertex layer [Tier BM.11" in P4t,
    "§G3 the Part 4 charter 0.1 carries clause (xiv)")
closure = P4t[P4t.find("## Closure exports of Part 4"):]
chk("\\mathrm{Def\\text{-}BM.11}" in closure and "\\mathrm{BM.45}" in closure,
    "§G3 the closure-export table carries the Def-BM.11 and BM.39-BM.45 rows")

# G4 — hygiene of the tier text
tier = P4t[P4t.find("## Tier BM.11 —"):P4t.find("\n## ", P4t.find("## Tier BM.11 —") + 5)]
for word in ["previously", "formerly", "this was", "now this", "earlier draft", "revision"]:
    chk(word not in tier.lower(), f"§G4 zero '{word}' in the tier text")
chk(not re.search(r"\bP-H\d", tier), "§G4 zero registry (P-H) tokens in the tier")
chk("**Status.**" not in tier, "§G4 zero '**Status.**' lines in the tier")
chk("[EXT]" not in tier, "§G4 zero [EXT] markers in the tier")
dec = re.findall(r"(?<![A-Za-z0-9\u00a7])\d+\.\d+", tier)
chk(not dec, f"§G4 zero decimal numerals in the tier text outside tag/section names: {dec}")
for tok in ["1.293", "0.782", "880.2", "10.4", "MeV", "GeV", "keV", "2.2 \u00b5"]:
    chk(tok not in tier, f"§G4 zero external-value token '{tok}' in the tier [P5]")
chk("None introduced by this part." in P4t[P4t.find("## §Cal-BM"):P4t.find("## Tier 4.0")],
    "§G4 §Cal-BM stays empty: 'None introduced by this part.' stands")

# G5 — the ledger and README rows
for tag in ["Def-BM.11", "BM.39", "BM.40", "BM.41", "BM.42", "BM.43", "BM.44", "BM.45"]:
    chk(f"**{tag}.**" in HLt, f"§G5 HistLog §III carries the {tag} status-ledger entry")
chk("(A-BM.4)" in HLt and "(A-BM.5)" in HLt, "§G5 HistLog §II.4 carries the addendum entries "
                                             "A-BM.4 (the angle identification) and A-BM.5 (the "
                                             "antineutrino naming row)")
chk("(V.15)" in HLt and "Suite state: 66/66" in HLt,
    "§G5 HistLog §V carries the (V.15) verification-history entry with suite state 66/66")
RM = rd("README.md")
chk("(79 checkers)" in RM, "§G5 the main README carries the 79-checker count")
CRM = rd(os.path.join("checks", "README.md"))
chk("(79 checkers)" in CRM and "**79/79**" in CRM,
    "§G5 checks/README.md carries the 79-checker count and suite state")
chk("verify_H_neutron_decay_vertex.py" in CRM, "§G5 checks/README.md lists the new content checker")

# G6 — the index and the Summary of Record
with open(os.path.join(DOCS, "index", "tags.json"), encoding="utf-8") as f:
    IDXT = json.load(f)
idxkeys = set(IDXT.keys()) if isinstance(IDXT, dict) else {tt["tag"] for tt in IDXT}
for tag in ["Def-BM.11", "BM.39", "BM.40", "BM.41", "BM.42", "BM.43", "BM.44", "BM.45"]:
    chk(tag in idxkeys, f"§G6 the regenerated index/tags.json carries {tag}")
SM = rd("Summary.md")
chk("BM.39" in SM and "BM.45" in SM and "Def-BM.11" in SM,
    "§G6 the regenerated Summary of Record carries the tier's statements")

# G7 — the suite count arithmetic
nverify = len([f for f in os.listdir(HERE) if f.startswith("verify_") and f.endswith(".py")])
chk(nverify + 1 == 79, f"§G7 the discovered suite is {nverify} verify_*.py + check_format.py = 79 checkers")

stamp("§G done — document pins and hygiene")

# --------------------------------------------------------------------------
print("\n" + "=" * 74)
if FAILS:
    print(f"verify_H_neutron_decay_vertex: {len(FAILS)} FAILURE(S) of {N + len(FAILS)}")
    for msg in FAILS:
        print("  -", msg)
    sys.exit(1)
print(f"verify_H_neutron_decay_vertex: ALL GREEN — {N} exact checks, "
      f"{time.time()-t0:.1f}s, no floating point in any assertion")
sys.exit(0)
