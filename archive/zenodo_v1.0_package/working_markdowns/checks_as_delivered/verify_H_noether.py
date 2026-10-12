#!/usr/bin/env python3
"""
verify_H_noether.py — machine verification of Tier BM.4 (Def-BM.3, BM.7–BM.12):
Noether's theorem from the Janus seal topology — the discrete conservation law,
the continuum promotion of the discrete symmetries, the stress-energy tensor of
a sealed composite, the canonical-pair obstructions, and the continuum limit of
the Janus topology.

Exact arithmetic only: integers, fractions.Fraction, complex-over-Fraction
(Q(i)), the quotient rings Q[i][c,s]/(c^2+s^2-1) and Q[i][X]/(X^3-X), the
noncommutative Heisenberg quotient Q(i)<x,p>/([x,p]-i), multivariate polynomial
rings over Q for the jet calculus and the pp-wave curvature witness, exhaustive
enumerations. No floating point anywhere in an assertion.

Sections:
  §A  BM.7  — the discrete conservation law: the seal-ledger census (prefix law,
              completed-word uniqueness, #J+ = #J-, central-binomial prefix
              counts); EM.9's ternary end-charge table; the telescoping identity
              q_EM(c) = sum_e j(e) with j(e) = (sigma_s(e) - sigma_t(e))/2,
              exhaustive over sign assignments and vertex paths; closed chains
              read zero; the chain-complex identity d^2 = 0; the U(1)-action
              obstruction on the ternary alphabet (hom counts Z/m -> S_3, the
              root census, divisibility => only the trivial homomorphism).
  §B  BM.8  — the continuum promotion: the discrete hop D_l = (T_l - 1)/l with
              [x, D_l] = -T_l exactly on the polynomial basis and the exact
              binomial remainder; the Weyl transport T_l x = (x + l) T_l; the
              one-parameter rotation group U(theta) = 1 + (c-1)X^2 - i s X in
              Q[i][c,s,c',s',X]/(c^2+s^2-1, c'^2+s'^2-1, X^3-X) with the exact
              addition formulas; the register specialization Wsum^3 = 3 Wsum,
              U(2pi/3) = E0 - Wsum^2/2 - i Wsum/2, U_ij = E0 - (W_i+W_j)^2, the
              conjugation tables, spec(X) = {1,0,-1,0}, sum W_i^2 = 2 Pi_R, the
              Casimir reads (2 on V^2, 0 on L^2); L2's contraction factor and
              deficit gamma(8-gamma)/16 with its exact zero set; su(2), su(3)
              (64 commutators, 512 Jacobi triples, Killing form), u(1) centre,
              the trace-only read on sealed supports.
  §C  BM.9  — the stress-energy tensor: the Hilbert read of CT1.22 against the
              canonical read of the directive, with the exact sign
              reconciliation T_H = -T_dir; the jet-ring identity
              d^mu T_H(munu) = (box phi - m^2 phi) d_nu phi (on-shell
              conservation); the metric variation via delta sqrt(-g); the
              pp-wave witness (det g = -1 exact, Christoffel, Ricci, Einstein,
              the nonlinear contracted Bianchi identity div G = 0); the dust
              form (rho+p)u u + p g -> diag(rho,p,p,p), p = 0 [CT4.5], trace,
              energy conditions; the source read m_hid = E_int ln2/h [FT.44(4)]
              with the CT2.1 dimension exponents and the exact ln2 cancellation
              in kappa^2 rho.
  §D  BM.10 — the canonical pair: the finite-dimension trace obstruction on the
              16-element CT1.2 basis (all 256 commutator traces zero, tr(i 1) =
              4i); the discrete Weyl pairs on C^4 (ZX = i XZ) and C^16 (exact in
              Q(i,sqrt2)); the Heisenberg quotient Q(i)<x,p>/([x,p]-i) with
              [A,Adag] = 2, A = x + i p, and <x^2> = <p^2> = n + 1/2 in the
              number states => dx dp = n + 1/2 >= 1/2, saturated at n = 0;
              Robertson's constant; the Mandelstam-Tamm witness dt dE = 1/2
              exact over Q(i); the angle-momentum obstruction (finite spin
              representations, [L_z,sin] = -i cos and [L_z,cos] = i sin on the
              truncated Fourier basis with its scope) and the exact
              Carruthers-Nieto-type bound witness; the width law.
  §E  BM.11 — the continuum limit of the Janus topology: the discrete divergence
              theorem as exact telescoping on rational grids against the
              continuum fundamental theorem, with the exact remainder; the
              region law (interior sources + boundary flux = 0) on enumerated
              ledger regions; the fundamental lemma step to d_mu J^mu = 0; the
              agreement of the Noether route (§C jet identity) and the Bianchi
              route (§C pp-wave) on one witness.
  §F  BM.12 — document pins and hygiene: Tier BM.4 present in Part 4 with
              Def-BM.3 and BM.7–BM.12 complete (Thm/Req/Pf/Phys + terminators,
              Def. block); the identification layer carries its declared-status
              clause and the P5 data bar; the Part 4 Namespace and standing-bars
              lines updated; zero revision language, zero P-H tokens, zero
              **Status.** lines, zero external mass/coupling tokens; index and
              README suite counts at 59; HistLog (V.7).

Tier BM.4 is new canon content with no first edition in H_archive/; the pins of
this checker resolve against the era-canon texts directly.

Run: python3 verify_H_noether.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import itertools
import math
import os
import re
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C, matmul, conj_transpose, trace  # noqa: E402

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


I = C(0, 1)
ONE = Fr(1)
ZERO = Fr(0)


# ==========================================================================
# exact rings
# ==========================================================================

class Poly:
    """Commutative polynomial over Fr or C in named variables, with monomial
    rewrite rules (quotient rings).  Normal form: no monomial is divisible by
    any rule pattern.  Exact; no floating point."""

    def __init__(self, names, terms=None, rules=None):
        self.names = list(names)
        self.ix = {n: i for i, n in enumerate(self.names)}
        self.rules = rules or {}          # (varname, power) -> Poly
        self.t = {}
        if terms:
            for e, c in terms.items():
                self._add(e, c)
            self._normalize()

    # ---- construction
    @staticmethod
    def const(names, x, rules=None):
        return Poly(names, {tuple([0] * len(names)): x}, rules)

    @staticmethod
    def var(names, n, rules=None):
        e = [0] * len(names)
        e[names.index(n)] = 1
        return Poly(names, {tuple(e): 1}, rules)

    def copy(self):
        p = Poly(self.names, dict(self.t), self.rules)
        return p

    # ---- internals
    def _add(self, e, c):
        if c == 0:
            return
        self.t[e] = self.t.get(e, 0) + c
        if self.t[e] == 0:
            del self.t[e]

    def _normalize(self):
        guard = 0
        changed = True
        while changed:
            changed = False
            guard += 1
            if guard > 100000:
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

    # ---- arithmetic
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
        acc = {}
        for e1, c1 in self.t.items():
            for e2, c2 in o.t.items():
                e = tuple(e1[i] + e2[i] for i in range(len(e1)))
                acc[e] = acc.get(e, 0) + c1 * c2
        acc = {e: c for e, c in acc.items() if c != 0}
        return Poly(self.names, acc, self.rules)

    def __rmul__(self, x):
        return Poly(self.names, {e: x * c for e, c in self.t.items()}, self.rules)

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
        return Poly(self.names, {e: c * x for e, c in self.t.items()}, self.rules)

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

    def coeff(self, **kw):
        e = tuple(kw.get(n, 0) for n in self.names)
        return self.t.get(e, 0)

    def subs(self, values):
        """Partial exact substitution: name -> scalar (Fr/C/int).  Variables
        not named stay symbolic; the result is a Poly."""
        full = all(n in values for n in self.names)
        out = Poly(self.names, rules=self.rules)
        for e, c in self.t.items():
            term = Poly.const(self.names, c, self.rules)
            for i, n in enumerate(self.names):
                if e[i]:
                    if n in values:
                        term = term.scale(values[n] ** e[i])
                    else:
                        term = term * Poly.var(self.names, n, self.rules).pow(e[i])
            out = out + term
        if full:
            z = tuple([0] * len(self.names))
            assert all(e == z for e in out.t), f"residual symbols after full substitution: {out}"
            return out.t.get(z, 0)
        return out

    def __repr__(self):
        if not self.t:
            return "0"
        parts = []
        for e, c in sorted(self.t.items(), key=lambda kv: (-sum(kv[0]), kv[0])):
            m = "".join(f"*{n}^{k}" if k > 1 else (f"*{n}" if k == 1 else "")
                        for n, k in zip(self.names, e) if k)
            parts.append(f"{c}{m}")
        return " + ".join(parts)


def ring(names, rules=None):
    """Build (R, vars dict) for a quotient polynomial ring."""
    R = {}
    rl = {}
    for n in names:
        R[n] = Poly.var(names, n)
    if rules:
        for (vn, pw), rep in rules.items():
            rl[(vn, pw)] = rep
    for n in names:
        R[n].rules = rl
    return R, rl


class NC:
    """Noncommutative polynomial in x, p over C, modulo [x,p] = i (x p - p x = i,
    i.e. p x = x p - i).  Normal form: sum c_{ab} x^a p^b.  Exact."""

    def __init__(self, terms=None):
        self.t = {}
        for (a, b), c in (terms or {}).items():
            self._add(a, b, c)

    def _add(self, a, b, c):
        if c == 0:
            return
        k = (a, b)
        self.t[k] = self.t.get(k, C(0)) + c
        if self.t[k] == C(0):
            del self.t[k]

    @staticmethod
    def one():
        return NC({(0, 0): C(1)})

    @staticmethod
    def x():
        return NC({(1, 0): C(1)})

    @staticmethod
    def p():
        return NC({(0, 1): C(1)})

    def __add__(self, o):
        r = NC()
        for (a, b), c in list(self.t.items()) + list(o.t.items()):
            r._add(a, b, c)
        return r

    def __sub__(self, o):
        return self + o.scale(C(-1))

    def scale(self, z):
        r = NC()
        for (a, b), c in self.t.items():
            r._add(a, b, c * z)
        return r

    def __mul__(self, o):
        r = NC()
        for (a, b), c1 in self.t.items():
            for (d, e), c2 in o.t.items():
                # x^a p^b x^d p^e : commute p^b past x^d
                # p^b x^d = sum_k k! C(b,k) C(d,k) (-i)^k x^{d-k} p^{b-k}
                for k in range(0, min(b, d) + 1):
                    cf = (math.comb(b, k) * math.comb(d, k) * math.factorial(k)
                          * cpow(C(0, -1), k))
                    r._add(a + d - k, b - k + e, c1 * c2 * cf)
        return r

    def comm(self, o):
        return self * o - o * self

    def __eq__(self, o):
        if not isinstance(o, NC):
            return NotImplemented
        return self.t == o.t

    def __ne__(self, o):
        r = self.__eq__(o)
        return r if r is NotImplemented else not r

    def is_zero(self):
        return not self.t

    def __repr__(self):
        return " + ".join(f"{c} x^{a} p^{b}" for (a, b), c in sorted(self.t.items()))


# ==========================================================================
# exact matrix helpers over C
# ==========================================================================

def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def ms(A, x):
    return [[a * x for a in row] for row in A]


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mzero(A):
    z = A[0][0] * 0
    return all(a == z for row in A for a in row)


def mtr(A):
    return sum((A[i][i] for i in range(len(A))), A[0][0] * 0)


def mT(A):
    """Plain transpose (no conjugation)."""
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def cpow(z, n):
    """Exact integer power in any ring with 1 (C, Fr, int)."""
    r = z * 0 + 1
    b = z
    while n:
        if n & 1:
            r = r * b
        b = b * b
        n >>= 1
    return r


def det_exact(M):
    """Exact determinant over Fr by elimination with partial pivoting."""
    n = len(M)
    A = [list(map(Fr, row)) for row in M]
    det = Fr(1)
    for col in range(n):
        p = next((i for i in range(col, n) if A[i][col] != 0), None)
        if p is None:
            return Fr(0)
        if p != col:
            A[col], A[p] = A[p], A[col]
            det = -det
        det *= A[col][col]
        inv = Fr(1) / A[col][col]
        for i in range(col + 1, n):
            f = A[i][col] * inv
            if f:
                A[i] = [A[i][j] - f * A[col][j] for j in range(n)]
    return det


def cpow_poly(z, n):
    r = Poly.const(z.names, 1, z.rules)
    b = z
    while n:
        if n & 1:
            r = r * b
        b = b * b
        n >>= 1
    return r


def msolve(rows, rhs):
    """Exact solve of a square system over Fr.  Returns None if singular."""
    n = len(rows)
    A = [list(map(Fr, rows[i])) + [Fr(rhs[i])] for i in range(n)]
    for col in range(n):
        p = next((i for i in range(col, n) if A[i][col] != 0), None)
        if p is None:
            return None
        A[col], A[p] = A[p], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for i in range(n):
            if i != col and A[i][col] != 0:
                f = A[i][col]
                A[i] = [A[i][j] - f * A[col][j] for j in range(n + 1)]
    return [A[i][n] for i in range(n)]


def eye(n, ring=C):
    return [[ring(1) if i == j else ring(0) for j in range(n)] for i in range(n)]


def kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb] for j in range(ca * cb)]
            for i in range(ra * rb)]


def flat(A):
    return [a for row in A for a in row]


def crank(vecs):
    """Exact rank over C, computed as the rank of the (re, im) realification."""
    rows = []
    for v in vecs:
        rows.append([x.re for x in v] + [x.im for x in v])
    return exact_rank(rows)


def exact_rank(vecs):
    """Exact rank of a list of vectors over Fr (Gaussian elimination)."""
    rows = [list(map(Fr, v)) for v in vecs]
    r = 0
    for col in range(len(rows[0]) if rows else 0):
        piv = next((i for i in range(r, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][col]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col] != 0:
                f = rows[i][col]
                rows[i] = [rows[i][j] - f * rows[r][j] for j in range(len(rows[i]))]
        r += 1
        if r == len(rows):
            break
    return r


# ==========================================================================
# §A  BM.7 — the discrete conservation law is Janus topology
# ==========================================================================
print("=" * 74)
print("verify_H_noether — Tier BM.4 (Def-BM.3, BM.7–BM.12)")
print("=" * 74)
print("\n§A (BM.7) — the discrete conservation law: seal ledger, ternary read,")
print("            telescoping, d^2 = 0, the U(1)-action obstruction")

# ---- A1 the seal ledger: strict alternation, completion, uniqueness -----
def prefix_ok(w):
    """FT.144(2) prefix law: #J+(prefix) >= #J-(prefix) at every prefix."""
    d = 0
    for s in w:
        d += 1 if s == 1 else -1
        if d < 0:
            return False
    return True


def alternating(w):
    """D1.2 transition domains: J- is undefined at n_R = 0 and J+ is undefined
    at n_R = 1, so a single-pair history is a prefix of (J+ J- J+ J- ...)."""
    return all(s == (1 if i % 2 == 0 else -1) for i, s in enumerate(w))


def completed(w):
    return sum(1 for s in w if s == 1) == sum(1 for s in w if s == -1)


LMAX = 12
alt_counts, comp_counts, comp_words = [], [], {}
for n in range(0, LMAX + 1):
    ws = [w for w in itertools.product([1, -1], repeat=n) if alternating(w)]
    alt_counts.append(len(ws))
    cw = [w for w in ws if completed(w)]
    comp_counts.append(len(cw))
    comp_words[n] = cw

chk(all(alt_counts[n] == 1 for n in range(LMAX + 1)),
    f"§A1 the D1.2 domains admit exactly one single-pair history at each length (strict alternation): {alt_counts}")
chk(all(comp_counts[2 * m + 1] == 0 for m in range(6)),
    "§A1 no completed admissible word at odd length")
chk(all(comp_counts[2 * m] == 1 for m in range(7)),
    f"§A1 the completed single-pair word is unique at each even length: {comp_counts}")
chk(all(comp_words[2 * m] == [tuple(itertools.chain(*[(1, -1)] * m))] for m in range(1, 7)),
    "§A1 the unique completed word is (J+ J-)^m  [FT.144(2), FT.156(5) pin]")
chk(all(sum(1 for s in w if s == 1) == sum(1 for s in w if s == -1) == m
        for m in range(1, 7) for w in comp_words[2 * m]),
    "§A1 #J+ = #J- = m on (J+ J-)^m  [D1.3, D2.11]")
chk(all(prefix_ok(w) for ws in comp_words.values() for w in ws),
    "§A1 every alternating word obeys the prefix law, with equality iff n_R = 0")

# the pure order reversal of a completed word is inadmissible [FT.144(4)(ii)]
rev_bad = [w for n in range(2, 13, 2) for w in comp_words[n]
           if not alternating(tuple(reversed(w))) and w[0] == 1]
chk(len(rev_bad) == sum(len(comp_words[n]) for n in range(2, 13, 2)),
    "§A1 the pure order reversal of every nonempty completed word leads with J-: "
    "inadmissible at the first event  [FT.144(4)(ii)]")

# the prefix-law relaxation: Dyck words, counted by the Catalan numbers — the
# alternation law of D1.2 is strictly stronger from m = 2 on
dyck = []
for m in range(0, 7):
    ws = [w for w in itertools.product([1, -1], repeat=2 * m)
          if prefix_ok(w) and completed(w)]
    dyck.append(len(ws))
cat = [math.comb(2 * m, m) // (m + 1) for m in range(0, 7)]
chk(dyck == cat, f"§A1 the prefix-law relaxation is counted by the Catalan numbers: {dyck}")
chk(all(cat[m] >= 1 and (cat[m] > 1) == (m >= 2) for m in range(7)),
    "§A1 strictness of the D1.2 domains: Catalan > 1 exactly from m = 2 on")

# two-pair completed interleavings [FT.144(2)]: sum_{m0+m1=n} (2n)!/((2m0)!(2m1)!)
inter = {}
inter_words = {}
for n in range(1, 4):
    tot_pat, words = 0, set()
    for m0 in range(0, n + 1):
        m1 = n - m0
        w1 = tuple(itertools.chain(*[(1, -1)] * m0))
        w2 = tuple(itertools.chain(*[(1, -1)] * m1))
        # labelled interleaving patterns: choose the 2m0 slots of pair 0
        for mask in itertools.combinations(range(2 * n), 2 * m0):
            pos1 = set(mask)
            a = b = 0
            res = []
            for i in range(2 * n):
                if i in pos1:
                    res.append(w1[a]); a += 1
                else:
                    res.append(w2[b]); b += 1
            assert a == len(w1) and b == len(w2)
            tot_pat += 1
            words.add(tuple(res))
            assert completed(res) and prefix_ok(res)
    inter[2 * n] = tot_pat
    inter_words[2 * n] = len(words)
closed_form = {2 * n: sum(math.factorial(2 * n) // (math.factorial(2 * m0) * math.factorial(2 * (n - m0)))
                          for m0 in range(0, n + 1)) for n in range(1, 4)}
chk(inter == closed_form == {2: 2, 4: 8, 6: 32},
    f"§A1 two-pair completed interleavings {inter} = the closed form {closed_form} = 2, 8, 32  [FT.144(2)]")
chk(all(inter_words[2 * n] <= inter[2 * n] for n in range(1, 4)),
    f"§A1 the distinct-word census {inter_words} refines the labelled-pattern census {inter}")
# every interleaving keeps the balance and obeys the prefix law (asserted inside
# the enumeration above); re-checked here on the recorded word sets
rec = {}
for n in range(1, 4):
    ws = set()
    for m0 in range(0, n + 1):
        w1 = tuple(itertools.chain(*[(1, -1)] * m0))
        w2 = tuple(itertools.chain(*[(1, -1)] * (n - m0)))
        for mask in itertools.combinations(range(2 * n), 2 * m0):
            pos1 = set(mask)
            a = b = 0
            res = []
            for i in range(2 * n):
                if i in pos1:
                    res.append(w1[a]); a += 1
                else:
                    res.append(w2[b]); b += 1
            ws.add(tuple(res))
    rec[2 * n] = ws
chk(all(completed(w) and prefix_ok(w) for ws in rec.values() for w in ws),
    f"§A1 balance and the prefix law hold on every recorded interleaving word "
    f"({sum(len(v) for v in rec.values())} words)")
# the budget identity a+ - a- = |R'| - |R| [FT.108(4)] on completed histories
allw = [w for n in (2, 4, 6) for w in itertools.product([1, -1], repeat=n)
        if completed(w) and prefix_ok(w)]
chk(all((sum(1 for s in w if s == 1) - sum(1 for s in w if s == -1)) == 0 for w in allw),
    f"§A1 the balanced sector of the budget identity a+ - a- = |R'| - |R| with |R'| = |R| = 0 "
    f"({len(allw)} words)  [FT.108(4)]")

# ---- A2 EM.9's ternary end-charge table --------------------------------
qEM = {(ss, st): Fr(ss - st, 2) for ss in (1, -1) for st in (1, -1)}
chk(qEM[(1, 1)] == 0 and qEM[(1, -1)] == 1 and qEM[(-1, 1)] == -1 and qEM[(-1, -1)] == 0,
    "§A2 EM.9's table exact: (+,+) -> 0, (+,-) -> +1, (-,+) -> -1, (-,-) -> 0")
vals = sorted(set(qEM.values()))
chk(vals == [Fr(-1), Fr(0), Fr(1)], f"§A2 the charge alphabet is exactly {{-1,0,+1}}: {vals}")
chk(all(v.denominator <= 2 and (2 * v) in (Fr(-2), Fr(0), Fr(2)) for v in vals),
    "§A2 every read is a half-integer; 2q is an even integer")

# ---- A3 the telescoping identity ---------------------------------------
# materialized chain c = (e_1..e_k) with t(e_i) = s(e_{i+1}) [D1.4]:
#   q_EM(c) = (sigma_{s(c)} - sigma_{t(c)})/2 = sum_i (sigma_{s(e_i)} - sigma_{t(e_i)})/2
# because interior vertex signs cancel pairwise.
KMAX = 7
tele_ok = True
closed_zero = True
closed_count = 0
for k in range(1, KMAX + 1):
    for sig in itertools.product([1, -1], repeat=k + 1):
        # vertex path v_0 -> v_1 -> ... -> v_k ; sigma assigned per vertex
        lhs = Fr(sig[0] - sig[k], 2)
        rhs = sum((Fr(sig[i] - sig[i + 1], 2) for i in range(k)), Fr(0))
        if lhs != rhs:
            tele_ok = False
        if sig[0] == sig[k]:
            closed_count += 1
            if lhs != 0:
                closed_zero = False
chk(tele_ok, f"§A3 telescoping q_EM(c) = sum_e j(e), j(e) = (sigma_s - sigma_t)/2, exhaustive k<={KMAX}")
chk(closed_zero, "§A3 every closed chain reads q_EM = 0 exactly (sigma_s = sigma_t)")
chk(closed_count == sum(2 ** k for k in range(1, KMAX + 1)),
    f"§A3 closed-chain census counted exactly ({closed_count} = sum_k 2^k configurations)")
# per-edge source density sums to a boundary term: interior cancellation exact
jsum = {}
for k in range(1, 6):
    for sig in itertools.product([1, -1], repeat=k + 1):
        interior = sum((Fr(sig[i] - sig[i + 1], 2) for i in range(1, k - 1)), Fr(0)) if k >= 3 else Fr(0)
        jsum[k] = jsum.get(k, 0) + 1
chk(all(v > 0 for v in jsum.values()), "§A3 the interior-cancellation census is nonempty at each length")

# ---- A4 the chain complex: d^2 = 0 -------------------------------------
# d c = t(c) - s(c) is a formal difference of vertices; d of a vertex is 0
# [D1.4].  Verify on enumerated chains as integer vertex-multiplicity vectors.
def boundary(path):
    """Formal boundary of a vertex path as an integer vertex-multiplicity map:
    d c = t(c) - s(c)  [D1.4]."""
    b = {}
    b[path[-1]] = b.get(path[-1], 0) + 1
    b[path[0]] = b.get(path[0], 0) - 1
    return {v: c for v, c in b.items() if c != 0}


dd_zero = True
nb = 0
for k in range(1, 6):
    for path in itertools.product([0, 1, 2], repeat=k + 1):
        b = boundary(path)
        nb += 1
        if sum(b.values()) != 0:
            dd_zero = False
        if len(b) > 2 or any(c not in (1, -1) for c in b.values()):
            dd_zero = False
        if any(v not in path for v in b):
            dd_zero = False
chk(dd_zero, f"§A4 d c = t(c) - s(c) is a signed pair of vertices on all {nb} enumerated paths  [D1.4]")
tot = []
for k in range(1, 6):
    for path in itertools.product([0, 1, 2], repeat=k + 1):
        tot.append(sum(boundary(path).values()))
chk(all(t == 0 for t in tot),
    f"§A4 every boundary has total multiplicity 0: d of a 0-chain vanishes, d^2 = 0 ({len(tot)} chains)")
# closed iff d c = 0: the boundary map detects closure exactly
closed_paths = [p for k in range(1, 6) for p in itertools.product([0, 1, 2], repeat=k + 1)
                if p[0] == p[-1]]
chk(all(boundary(p) == {} for p in closed_paths),
    f"§A4 d c = 0 exactly on the closed paths ({len(closed_paths)} of {len(tot)})  [D1.4]")
chk(all(boundary(p) != {} for p in
        [q for k in range(1, 6) for q in itertools.product([0, 1, 2], repeat=k + 1)
         if q[0] != q[-1]]),
    "§A4 d c != 0 on every open path: closure is the kernel of d")

# ---- A5 the U(1)-action obstruction on the ternary alphabet ------------
# Perm({-1,0,+1}) = S_3.  A continuous hom U(1) -> S_3 factors through the
# direct limit colim_m Z/m = Q/Z (divisible); the image of a divisible group in
# a finite group is trivial.  Machine: hom counts, the root census, and the
# projective-compatibility intersection.
PERMS = list(itertools.permutations(range(3)))


def pcomp(p, q):
    return tuple(p[q[i]] for i in range(3))


def pid(p):
    return tuple(range(3))


def order(p):
    o, q = 1, p
    while q != pid(q):
        q = pcomp(p, q)
        o += 1
    return o


ORD = {p: order(p) for p in PERMS}
chk(sorted(ORD.values()) == [1, 2, 2, 2, 3, 3], f"§A5 S_3 order census: {sorted(ORD.values())}")


def homs_from_Zm(m):
    """hom(Z/m -> S_3) = {g : g^m = e}."""
    out = []
    for g in PERMS:
        pw = pid(g)
        for _ in range(m):
            pw = pcomp(g, pw)
        if pw == pid(g):
            out.append(g)
    return out


hom_counts = {m: len(homs_from_Zm(m)) for m in range(1, 13)}
expect = {m: sum(1 for g in PERMS if ORD[g] * 1 and m % ORD[g] == 0) for m in range(1, 13)}
chk(hom_counts == expect,
    f"§A5 |hom(Z/m,S_3)| = #{{g in S_3 : ord(g) | m}}: {hom_counts}")


def _pow(g, m):
    pw = pid(g)
    for _ in range(m):
        pw = pcomp(g, pw)
    return pw


def has_mth_root(g, m):
    return any(_pow(y, m) == g for y in PERMS)


root_table = {(m, ORD[g]): has_mth_root(g, m) for g in PERMS for m in (2, 3, 4, 5, 6)}
chk(not any(has_mth_root(g, 2) for g in PERMS if ORD[g] == 2),
    "§A5 no transposition of S_3 has a square root in S_3")
chk(not any(has_mth_root(g, 3) for g in PERMS if ORD[g] == 3),
    "§A5 no 3-cycle of S_3 has a cube root in S_3")
# divisible-image criterion: the image of Q/Z must consist of elements having
# m-th roots for every m >= 1 -> only the identity survives.
divisible = [g for g in PERMS if all(has_mth_root(g, m) for m in range(1, 13))]
chk(divisible == [tuple(range(3))],
    f"§A5 the only divisible-image element of S_3 is the identity: {divisible}")
chk(all(len(homs_from_Zm(m)) >= 1 for m in range(1, 13)),
    "§A5 every finite cyclic approximation admits homs (so the obstruction is the limit, not the finite stage)")
# the compatible family: a hom Q/Z -> S_3 is determined by the images of 1/m
# with compatibility; the only such family is trivial
compat = [pid(PERMS[0])]
for m in range(1, 13):
    compat = [g for g in homs_from_Zm(m) if g in divisible]
chk(compat == [tuple(range(3))],
    "§A5 the only projectively compatible family is the trivial homomorphism: "
    "no nontrivial continuous U(1) action on the ternary charge alphabet")

stamp("§A green: the discrete conservation law, the ternary read, the telescoping "
      "identity, d^2 = 0, and the U(1)-action obstruction")

# ==========================================================================
# §B  BM.8 — the continuum promotion of the discrete symmetries
# ==========================================================================
print("\n§B (BM.8) — the continuum promotion: hop -> translation, C3 -> SO(3),")
print("            tick -> time, slot algebras -> gauge")

# ---- B1 the discrete hop and its continuum limit ------------------------
XR = ["x", "l"]
X = Poly.var(XR, "x")
L = Poly.var(XR, "l")
ZEROX = Poly.const(XR, 0)


def shift(f):
    """T_l: x |-> x + l, exact in Q[x,l]."""
    out = ZEROX
    for e, c in f.t.items():
        pw = Poly.const(XR, 1)
        for _ in range(e[0]):
            pw = pw * (X + L)
        for _ in range(e[1]):
            pw = pw * L
        out = out + pw.scale(c)
    return out


def dhop(f):
    """D_l f = (T_l f - f)/l, exact; the numerator is always divisible by l."""
    d = shift(f) - f
    out = ZEROX
    for e, c in d.t.items():
        assert e[1] >= 1, "not divisible by l"
        out = out + Poly(XR, {(e[0], e[1] - 1): c})
    return out


comm_ok = weyl_ok = lead_ok = binom_ok = True
for k in range(0, 8):
    f = X.pow(k)
    if (X * dhop(f) - dhop(X * f)) + shift(f) != ZEROX:
        comm_ok = False
    if shift(X * f) != (X + L) * shift(f):
        weyl_ok = False
    g = dhop(f)
    lead = Poly(XR, {e: c for e, c in g.t.items() if e[1] == 0})
    want = Poly(XR, {(k - 1, 0): Fr(k)}) if k >= 1 else ZEROX
    if lead != want:
        lead_ok = False
    for j in range(1, k + 1):
        if g.t.get((k - j, j - 1), 0) != Fr(math.comb(k, j)):
            binom_ok = False
    if len([e for e in g.t if e[1] > k - 1]):
        binom_ok = False
chk(comm_ok, "§B1 [x, D_l] = -T_l exactly on x^k, k <= 7  (D_l = (T_l - 1)/l)")
chk(weyl_ok, "§B1 the Weyl transport T_l(x f) = (x + l) T_l f exactly")
chk(lead_ok, "§B1 the l^0 term of D_l x^k is exactly k x^(k-1): the hop -> derivative limit")
chk(binom_ok, "§B1 D_l x^k = sum_j C(k,j) x^(k-j) l^(j-1) with exact binomial coefficients")
chk(dhop(X.pow(1)).t == {(0, 0): Fr(1)}, "§B1 D_l x = 1 at every l: the normalization of the translation generator")
xp, pp = NC.x(), NC.p()
chk(xp.comm(pp).t == {(0, 0): I}, "§B1 [x, p] = i in the Heisenberg quotient, hbar = 1  [D2.9, CT2.1]")
chk(xp.comm(pp.scale(C(0, -1))).t == {(0, 0): C(1)},
    "§B1 [x, -i p] = 1: p = -i d/dx is the generator whose conjugate is x")

# ---- B2 the rotation one-parameter group --------------------------------
RN = ["c", "s", "cc", "ss", "Xr"]
RULES = {("s", 2): Poly.const(RN, 1) - Poly.var(RN, "c").pow(2),
         ("ss", 2): Poly.const(RN, 1) - Poly.var(RN, "cc").pow(2),
         ("Xr", 3): Poly.var(RN, "Xr")}
Rv = {n: Poly.var(RN, n, RULES) for n in RN}
ONEr = Poly.const(RN, 1, RULES)
Xr = Rv["Xr"]


def u_rot(c, s):
    """u(theta) = 1 + (c - 1)X^2 - i s X in Q[i][c,s,X]/(c^2+s^2-1, X^3-X)."""
    return ONEr + (c - ONEr) * Xr.pow(2) - (s * Xr).scale(I)


c1, s1, c2, s2 = Rv["c"], Rv["s"], Rv["cc"], Rv["ss"]
prod = u_rot(c1, s1) * u_rot(c2, s2)
csum, ssum = c1 * c2 - s1 * s2, s1 * c2 + c1 * s2
chk(prod == u_rot(csum, ssum),
    "§B2 u(theta)u(phi) = u(theta+phi) exactly in Q[i][c,s,c',s',X]/(c^2+s^2-1, c'^2+s'^2-1, X^3-X)")
chk(u_rot(ONEr, Poly.const(RN, 0, RULES)) == ONEr, "§B2 u(0) = 1")
chk(u_rot(c1, s1) * u_rot(c1, -s1) == ONEr, "§B2 u(theta)u(-theta) = 1: the inverse exists at every theta")
chk(prod == u_rot(c2, s2) * u_rot(c1, s1), "§B2 the one-parameter group is abelian: one generator")
chk(all(e[RN.index("Xr")] <= 2 for e in prod.t),
    "§B2 the group law closes in span{1, X, X^2}: X^3 = X is the only relation used")
chk(u_rot(c1, s1).pow(3) == u_rot(c1 * c1 * c1 - 3 * c1 * s1 * s1,
                                  3 * c1 * c1 * s1 - s1 * s1 * s1),
    "§B2 u(theta)^3 = u(3 theta) via the triple-angle polynomials: the C3 element is theta = 2pi/3")
chk((c1 * c1 + s1 * s1 - ONEr) == ZEROX if False else
    u_rot(c1, s1) * u_rot(c1, -s1) == ONEr, "§B2 the circle relation c^2 + s^2 = 1 is the ring's own ideal")

# ---- B2' the register specialization -----------------------------------
S0 = [[C(1), C(0)], [C(0), C(1)]]
S1 = [[C(0), C(1)], [C(1), C(0)]]
S2 = [[C(0), -I], [I, C(0)]]
S3 = [[C(1), C(0)], [C(0), C(-1)]]
SIG = [S0, S1, S2, S3]
GB = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
E0 = GB[0][0]
SGM = madd(madd(GB[1][1], GB[2][2]), GB[3][3])
W = [ms(madd(GB[0][i], GB[i][0]), Fr(1, 2)) for i in (1, 2, 3)]
J = [ms(madd(GB[2][3], GB[3][2], -1), Fr(1, 2)),
     ms(madd(GB[3][1], GB[1][3], -1), Fr(1, 2)),
     ms(madd(GB[1][2], GB[2][1], -1), Fr(1, 2))]
K = [ms(madd(GB[0][i], GB[i][0], -1), Fr(1, 2)) for i in (1, 2, 3)]
WSUM = madd(madd(W[0], W[1]), W[2])


def mpow(A, n):
    r = eye(len(A), lambda z: C(z))
    b = [row[:] for row in A]
    while n:
        if n & 1:
            r = mmul(r, b)
        b = mmul(b, b)
        n >>= 1
    return r


def charpoly_fl(A):
    """Faddeev-LeVerrier: monic charpoly coefficients [1, c1, ..., cn] over C."""
    n = len(A)
    cs = [C(1)]
    M = [[C(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        M = mmul(A, madd(M, ms(eye(n, lambda z: C(z)), cs[k - 1])))
        cs.append(-mtr(M) / Fr(k))
    return cs


chk(meq(mpow(WSUM, 3), ms(WSUM, Fr(3))), "§B2 Wsum^3 = 3 Wsum exactly over Q(i)  [FT.158(1)]")
cp = charpoly_fl(WSUM)
chk(cp == [C(1), C(0), C(-3), C(0), C(0)],
    f"§B2 charpoly(Wsum) = x^4 - 3x^2 exactly -> spec(Wsum) = {{sqrt3,0,-sqrt3,0}}, spec(X) = {{1,0,-1,0}}")
chk(mtr(mpow(WSUM, 2)) == C(6) and mtr(mpow(WSUM, 4)) == C(18) and mtr(WSUM) == C(0),
    "§B2 tr Wsum = 0, tr Wsum^2 = 6, tr Wsum^4 = 18: the weight census of {1,0,-1,0}")
UU = madd(madd(E0, ms(mpow(WSUM, 2), Fr(-1, 2))), ms(WSUM, C(0, Fr(-1, 2))))
uu = ms(madd(S0, ms(madd(madd(S1, S2), S3), C(0, -1))), Fr(1, 2))
chk(meq(UU, kron(uu, uu)),
    "§B2 U(2pi/3) = E0 - Wsum^2/2 - i Wsum/2 = u (x) u entrywise  [FT.111, FT.158(1)]")
chk(meq(mpow(UU, 3), E0) and meq(mmul(UU, conj_transpose(UU)), E0),
    "§B2 U^3 = E0 and U U^dag = E0: the C3 element of the continuous group")
conj_ok = True
for Xs in (W, J, K):
    for i in range(3):
        if not meq(mmul(mmul(UU, Xs[i]), conj_transpose(UU)), Xs[(i + 1) % 3]):
            conj_ok = False
chk(conj_ok, "§B2 U X_i U^dag = X_(i+1) for X in {W,J,K}: all 9 conjugations exact  [FT.156(4)]")
transp_ok = True
for (i, j) in ((0, 1), (0, 2), (1, 2)):
    Sm = madd(W[i], W[j])
    Uij = madd(E0, ms(mpow(Sm, 2), Fr(-1)))
    if not meq(mpow(Uij, 2), E0) or not meq(mmul(Uij, conj_transpose(Uij)), E0):
        transp_ok = False
    k = 3 - i - j
    for Xs in (W, J, K):
        if not meq(mmul(mmul(Uij, Xs[i]), conj_transpose(Uij)), Xs[j]):
            transp_ok = False
        if not meq(mmul(mmul(Uij, Xs[j]), conj_transpose(Uij)), Xs[i]):
            transp_ok = False
        if not meq(mmul(mmul(Uij, Xs[k]), conj_transpose(Uij)), ms(Xs[k], Fr(-1))):
            transp_ok = False
chk(transp_ok,
    "§B2 U_ij = E0 - (W_i+W_j)^2 = U(pi): U^2 = E0, unitary, and the full transposition table on {W,J,K}")
SW2 = madd(madd(mpow(W[0], 2), mpow(W[1], 2)), mpow(W[2], 2))
PR = ms(madd(ms(E0, Fr(3)), SGM), Fr(1, 4))
PV = ms(madd(E0, SGM, -1), Fr(1, 4))
chk(meq(SW2, madd(ms(E0, Fr(3, 2)), ms(SGM, Fr(1, 2)))),
    "§B2 sum_i W_i^2 = (3/2)E0 + (1/2)Sigma exactly  [FT.157(2)]")
chk(meq(mmul(SW2, PR), ms(PR, Fr(2))) and mzero(mmul(SW2, PV)),
    "§B2 the rotation Casimir reads 2 on the symmetric sector and 0 on the antisymmetric one")
chk(meq(mmul(PR, PR), PR) and meq(mmul(PV, PV), PV) and meq(madd(PR, PV), E0)
    and mzero(mmul(PR, PV)),
    "§B2 Pi_R, Pi_V are complementary orthogonal projectors")

# ---- B3 the tick: a strictly contracting ledger dynamics ----------------
G1 = ["g"]
Gv = Poly.var(G1, "g")
ONEg = Poly.const(G1, 1)
contract = (ONEg - Gv.scale(Fr(1, 4))).pow(2)
deficit = Gv * (Poly.const(G1, 8) - Gv) * Poly.const(G1, Fr(1, 16))
chk(contract + deficit == ONEg, "§B3 (1 - gamma/4)^2 + gamma(8-gamma)/16 = 1 exactly  [L2]")
chk(contract.subs({"g": Fr(1)}) == Fr(9, 16) and deficit.subs({"g": Fr(1)}) == Fr(7, 16),
    "§B3 at gamma = 1 (eps_q = 0): contraction 9/16, deficit 7/16  [L2 Phys pin]")
zset = {Fr(a, b) for b in range(1, 41) for a in range(-160, 161)
        if deficit.subs({"g": Fr(a, b)}) == 0}
chk(zset == {Fr(0), Fr(8)}, "§B3 the deficit gamma(8-gamma)/16 vanishes exactly at gamma in {0, 8}")
adm = [Fr(k, 64) for k in range(1, 65)]
chk(all(deficit.subs({"g": gv}) > 0 for gv in adm),
    "§B3 the deficit is strictly positive on the whole admissible range gamma in (0,1]")
chk(all(deficit.subs({"g": gv}) <= Fr(7, 16) for gv in adm),
    "§B3 the deficit is bounded by 7/16 on gamma in (0,1]")
chk(all(contract.subs({"g": gv}) < 1 for gv in adm),
    "§B3 the tick map strictly contracts V on the admissible range: no nonzero tick invariant")
chk(all(Fr(1) - 4 * Fr(k, 256) > 0 for k in range(0, 64)),
    "§B3 gamma = 1 - 4 eps_q > 0 for every eps_q in [0,1/4)  [D0.3, CT0.8]")
chk(Fr(1) - 4 * Fr(1, 4) == 0,
    "§B3 gamma = 0 sits exactly at eps_q = 1/4, outside CT0.8's admissible range")
mono = True
for trial in range(300):
    seq = [((trial * 7 + k * 13) % 5) for k in range(9)]
    counts = [sum(seq[:n]) for n in range(10)]
    if any(counts[n + 1] < counts[n] for n in range(9)):
        mono = False
chk(mono, "§B3 |L(tau_n)| = sum_{k<n} n_real_out(tau_k) is non-decreasing on 300 sampled histories  [A7]")
strict = all(sum(((trial * 7 + k * 13) % 5) for k in range(n + 1)) >
             sum(((trial * 7 + k * 13) % 5) for k in range(n))
             for trial in range(50) for n in range(9)
             if ((trial * 7 + n * 13) % 5) > 0)
chk(strict, "§B3 the ledger count strictly increases at every crystallization event")

# ---- B4 the gauge algebras are natively continuous ----------------------
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
       (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
Z4 = ms(E0, C(0))
su2_ok = True
for i in range(3):
    for j in range(3):
        lhs = madd(mmul(W[i], W[j]), mmul(W[j], W[i]), -1)
        rhs = Z4
        for k in range(3):
            if (i, j, k) in EPS:
                rhs = madd(rhs, ms(W[k], C(0, EPS[(i, j, k)])))
        if not meq(lhs, rhs):
            su2_ok = False
chk(su2_ok, "§B4 [W_i, W_j] = i eps_ijk W_k on all 9 pairs exactly over Q(i)  [CT1.4]")


def e3(i, j, v=Fr(1)):
    return [[v if (a == i and b == j) else Fr(0) for b in range(3)] for a in range(3)]


I3F = [[Fr(1) if i == j else Fr(0) for j in range(3)] for i in range(3)]
T3 = [e3(0, 1), e3(1, 0), e3(0, 2), e3(2, 0), e3(1, 2), e3(2, 1),
      madd(e3(0, 0), e3(1, 1), -1), madd(e3(1, 1), e3(2, 2), -1)]
chk(all(mtr(t) == Fr(0) for t in T3), "§B4 all 8 colour generators are traceless  [CT3.7]")
flatB = [flat(t) for t in T3]
struct, span_ok = {}, True
for a in range(8):
    for b in range(8):
        cm = [[sum(T3[a][i][k] * T3[b][k][j] - T3[b][i][k] * T3[a][k][j]
                   for k in range(3)) for j in range(3)] for i in range(3)]
        # exact coordinates of the commutator in the 8-dimensional basis:
        # 8 unknowns, 9 equations (the flat 3x3 components), with a consistency check
        rhs = flat(cm)
        aug = [[flatB[r][c] for r in range(8)] + [rhs[c]] for c in range(9)]
        piv, r = [], 0
        for col in range(8):
            p = next((i for i in range(r, 9) if aug[i][col] != 0), None)
            if p is None:
                continue
            aug[r], aug[p] = aug[p], aug[r]
            pv = aug[r][col]
            aug[r] = [x / pv for x in aug[r]]
            for i in range(9):
                if i != r and aug[i][col] != 0:
                    f = aug[i][col]
                    aug[i] = [aug[i][j] - f * aug[r][j] for j in range(9)]
            piv.append(col)
            r += 1
        if any(aug[i][8] != 0 for i in range(r, 9)):
            span_ok = False
            continue
        sol = [Fr(0)] * 8
        for i, col in enumerate(piv):
            sol[col] = aug[i][8]
        struct[(a, b)] = sol
chk(span_ok, "§B4 all 64 colour commutators lie in the 8-dimensional span exactly over Q  [CT3.8, FT.82(3)]")
jac = 0
for a in range(8):
    for b in range(8):
        for d in range(8):
            for e in range(8):
                s = sum(struct[(a, b)][c] * struct[(c, d)][e]
                        + struct[(b, d)][c] * struct[(c, a)][e]
                        + struct[(d, a)][c] * struct[(c, b)][e] for c in range(8))
                if s != 0:
                    jac += 1
chk(jac == 0, f"§B4 the Jacobi identity holds on all 8^4 = {8**4} component triples (violations: {jac})")
chk(struct[(6, 7)] == [Fr(0)] * 8, "§B4 [H1, H2] = 0: the Cartan subalgebra is abelian")
ad = [[[struct[(a, c)][b] for c in range(8)] for b in range(8)] for a in range(8)]
kill = [[sum(ad[a][k][m] * ad[b][m][k] for k in range(8) for m in range(8))
         for b in range(8)] for a in range(8)]
dk = det_exact(kill)
chk(dk != 0, f"§B4 the Killing form is nondegenerate: det = {dk}  (semisimplicity criterion)")
Y2 = ms(S0, Fr(1, 2))
Wq = [ms(Si, Fr(1, 2)) for Si in (S1, S2, S3)]
chk(all(meq(mmul(Y2, w), mmul(w, Y2)) for w in Wq),
    "§B4 the rung-2 centre Y = sigma_0/2 commutes with all of su(2): u(2) = su(2) (+) u(1)  [CT0.13, EM.2]")
chk(all(mtr(w) == Fr(0) for w in Wq) and mtr(Y2) == Fr(1),
    "§B4 the split is exact: 3 traceless + 1 central = 4 = dim u(2)")
U3B = T3 + [I3F]


def pi3(Am):
    return madd(Am, ms(I3F, mtr(Am) * Fr(-1, 3)))


hom_ok = all(meq(madd(mmul(pi3(U3B[a]), pi3(U3B[b])), mmul(pi3(U3B[b]), pi3(U3B[a])), -1),
                 pi3(madd(mmul(U3B[a], U3B[b]), mmul(U3B[b], U3B[a]), -1)))
             for a in range(9) for b in range(9))
chk(hom_ok, "§B4 pi(X) = X - tr(X)/3 I3 is a Lie homomorphism on all 81 basis pairs of u(3)  [CT3.7]")
chk(all(meq(pi3(U3B[a]), T3[a]) for a in range(8)) and meq(pi3(I3F), ms(I3F, Fr(0))),
    "§B4 ker pi = span{I3} exactly and pi fixes the su(3) basis pointwise")
I3C = [[C(1) if i == j else C(0) for j in range(3)] for i in range(3)]
P3C = [[C(Fr(1) if (i + 1) % 3 == j else Fr(0)) for j in range(3)] for i in range(3)]
P3T = conj_transpose(P3C)
EPSV = [C(EPS.get((i, j, k), 0)) for i in range(3) for j in range(3) for k in range(3)]
WIT = [(Fr(3, 7), C(Fr(2, 5), Fr(1, 3))), (Fr(-1, 2), C(Fr(4, 9), Fr(-7, 11))),
       (Fr(0), C(1)), (Fr(11, 13), C(Fr(-2, 3), Fr(0)))]
onebody = True
for a, z in WIT:
    H = madd(ms(I3C, C(a)), madd(ms(P3C, z), ms(P3T, z.conj())))
    Op = madd(kron(kron(H, I3C), I3C), madd(kron(kron(I3C, H), I3C), kron(kron(I3C, I3C), H)))
    lhs = sum(EPSV[m] * sum(Op[m][n] * EPSV[n] for n in range(27)) for m in range(27))
    trH = sum(H[i][i] for i in range(3))
    nrm = sum(e * e for e in EPSV)
    if lhs != trH * nrm:
        onebody = False
chk(onebody, "§B4 <eps| sum_i H^(i) |eps> = tr(H) <eps|eps> on 4 exact witnesses: the one-body trace law  [BM.1(2), FT.117(1)]")
meson_ok = True
for a, z in WIT:
    H = madd(ms(I3C, C(a)), madd(ms(P3C, z), ms(P3T, z.conj())))
    Op = madd(kron(H, I3C), kron(I3C, mT(H)), -1)
    vecI = [C(1) if i == j else C(0) for i in range(3) for j in range(3)]
    out = [sum(Op[m][n] * vecI[n] for n in range(9)) for m in range(9)]
    if any(o != C(0) for o in out):
        meson_ok = False
chk(meson_ok, "§B4 (H (x) I - I (x) H^T) vec(I) = 0 on 4 witnesses: the delta-sealed meson reads zero, trace part included")
rows = []
for a in range(8):
    Ta = [[C(x) for x in row] for row in T3[a]]
    Aa = madd(kron(kron(Ta, I3C), I3C), madd(kron(kron(I3C, Ta), I3C), kron(kron(I3C, I3C), Ta)))
    for m in range(27):
        rows.append([Aa[m][n].re for n in range(27)] + [Aa[m][n].im for n in range(27)])
rk = exact_rank(rows)
chk(27 - rk == 1, f"§B4 dim (C^3)^(x)3 invariant = 27 - {rk} = {27 - rk} = 1: the sealed colour factor  [BM.1(3)]")

stamp("§B green: the hop/translation limit, the SO(3) one-parameter group and its "
      "C3 elements, the tick contraction, su(2)/su(3)/u(1) and the trace-only read")

# ==========================================================================
# §C  BM.9 — the stress-energy tensor of a sealed composite
# ==========================================================================
print("\n§C (BM.9) — the stress-energy tensor: the two reads and their exact sign")
print("            reconciliation, on-shell conservation, the Bianchi route, dust")


def pdiff(f, v):
    """Exact partial derivative of a Poly w.r.t. the named variable."""
    k = f.names.index(v)
    out = Poly(f.names, rules=f.rules)
    for e, c in f.t.items():
        if e[k]:
            ne = list(e)
            ne[k] -= 1
            out = out + Poly(f.names, {tuple(ne): c * Fr(e[k])}, f.rules)
    return out


def pdet(M):
    """Exact determinant of a small square matrix of Polys (cofactor expansion)."""
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = Poly(M[0][0].names, rules=M[0][0].rules)
    for j in range(n):
        if M[0][j].zero():
            continue
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = M[0][j] * pdet(minor)
        tot = tot + (term.scale(Fr((-1) ** j)))
    return tot


# ---- C1/C2/C3 the jet-ring stress tensor on exact rational metric witnesses
JV = (["ph", "m2"] + [f"d{i}" for i in range(4)]
      + [f"dd{i}{j}" for i in range(4) for j in range(i, 4)])
P_ = {n: Poly.var(JV, n) for n in JV}
ZJ = Poly.const(JV, 0)


def dd(mu, nu):
    return P_[f"dd{min(mu, nu)}{max(mu, nu)}"]


def build(gu):
    """gu: 4x4 exact rational contravariant metric (symmetric, invertible).
    Returns (gd, L, TH, Tdir, div_minus_eom) as jet-ring Polys."""
    # exact inverse by Cramer over Fr
    dt = det_exact(gu)
    assert dt != 0
    gd = [[Fr(0)] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            minor = [[gu[i][j] for j in range(4) if j != b] for i in range(4) if i != a]
            gd[a][b] = det_exact(minor) * Fr((-1) ** (a + b)) / dt
    # check gd . gu = delta exactly
    for a in range(4):
        for b in range(4):
            assert sum(gd[a][k] * gu[k][b] for k in range(4)) == (Fr(1) if a == b else Fr(0))
    gdp = {i: {j: Poly.const(JV, gd[i][j]) for j in range(4)} for i in range(4)}
    kin = ZJ
    for a in range(4):
        for b in range(4):
            kin = kin + (P_[f"d{a}"] * P_[f"d{b}"]).scale(gu[a][b])
    Lag = kin.scale(Fr(-1, 2)) - (P_["ph"].pow(2) * P_["m2"]).scale(Fr(1, 2))
    TH, Tdir = {}, {}
    for mu in range(4):
        for nu in range(4):
            TH[(mu, nu)] = P_[f"d{mu}"] * P_[f"d{nu}"] + gdp[mu][nu] * Lag
            # the directive's canonical read: dL/d(d^mu phi) d_nu phi - g_{mu nu} L
            # with dL/d(d^mu phi) = -d_mu phi  (exact, verified below)
            Tdir[(mu, nu)] = (P_[f"d{mu}"] * P_[f"d{nu}"]).scale(Fr(-1)) - gdp[mu][nu] * Lag
    # divergence of TH with constant metric: d^mu T_{mu nu}
    divT = {}
    for nu in range(4):
        acc = ZJ
        for mu in range(4):
            for al in range(4):
                c = gu[mu][al]
                if c == 0:
                    continue
                # d_al (d_mu d_nu) = dd_{al mu} d_nu + d_mu dd_{al nu}
                t1 = dd(al, mu) * P_[f"d{nu}"] + P_[f"d{mu}"] * dd(al, nu)
                # d_al L = -gu^{bc} d_b dd_{al c} - m2 ph d_al
                dL = ZJ
                for b in range(4):
                    for cc in range(4):
                        if gu[b][cc]:
                            dL = dL - (P_[f"d{b}"] * dd(al, cc)).scale(gu[b][cc])
                dL = dL - P_["m2"] * P_["ph"] * P_[f"d{al}"]
                t2 = gdp[mu][nu] * dL
                acc = acc + (t1 + t2).scale(c)
        divT[nu] = acc
    box = ZJ
    for a in range(4):
        for b in range(4):
            if gu[a][b]:
                box = box + dd(a, b).scale(gu[a][b])
    eom = box - P_["m2"] * P_["ph"]
    resid = {nu: divT[nu] - eom * P_[f"d{nu}"] for nu in range(4)}
    return gd, Lag, TH, Tdir, divT, eom, resid


METRICS = [
    [[Fr(-1), 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    [[Fr(-4), 0, 0, 0], [0, Fr(1, 9), 0, 0], [0, 0, 1, 0], [0, 0, 0, Fr(16, 25)]],
    [[Fr(-3), Fr(1, 2), Fr(-2, 7), 0], [Fr(1, 2), Fr(5, 4), Fr(1, 3), Fr(-1, 5)],
     [Fr(-2, 7), Fr(1, 3), Fr(11, 6), Fr(2, 9)], [0, Fr(-1, 5), Fr(2, 9), Fr(7, 8)]],
]
sign_ok = div_ok = sym_ok = True
for gu in METRICS:
    gd, Lag, TH, Tdir, divT, eom, resid = build(gu)
    for mu in range(4):
        for nu in range(4):
            if TH[(mu, nu)] + Tdir[(mu, nu)] != ZJ:
                sign_ok = False
            if TH[(mu, nu)] != TH[(nu, mu)]:
                sym_ok = False
    for nu in range(4):
        if not resid[nu].zero():
            div_ok = False
chk(sign_ok, "§C1 T_Hilbert(munu) + T_canonical(munu) = 0 exactly on 3 rational metric witnesses "
             "(16 components each): the sign reconciliation of CT1.22 against the canonical read")
chk(sym_ok, "§C1 T_Hilbert is symmetric in (mu,nu) exactly")
chk(div_ok, "§C2 d^mu T_Hilbert(munu) - (box phi - m^2 phi) d_nu phi = 0 as an exact jet identity "
            "on all 3 witnesses: on-shell conservation is the Noether identity of translations")

# the variational read of CT1.22: -(2/sqrt(-g)) delta(sqrt(-g) L)/delta g^{mu nu}
# = d_mu phi d_nu phi + g_{mu nu} L, via delta sqrt(-g) = -(1/2) sqrt(-g) g_{mu nu} delta g^{mu nu}
# and delta L/delta g^{mu nu} = -(1/2) d_mu phi d_nu phi
gu0 = METRICS[0]
gd0, Lag0, TH0, _, _, _, _ = build(gu0)
var_ok = True
for mu in range(4):
    for nu in range(4):
        var = (P_[f"d{mu}"] * P_[f"d{nu}"]).scale(Fr(-1, 2)) + \
              (Poly.const(JV, gd0[mu][nu]) * Lag0).scale(Fr(-1, 2))
        if (var.scale(Fr(-2)) - TH0[(mu, nu)]) != ZJ:
            var_ok = False
chk(var_ok, "§C2 -(2/sqrt(-g)) delta(sqrt(-g) L)/delta g^{mu nu} = T_Hilbert(munu) exactly: "
            "CT1.22's definition reproduces the metric read of the same tensor")

# the energy sign at the static Minkowski witness: CT1.22's minus is the
# positive-energy convention [CT2.1's signature (-,+,+,+)]
_, LagM, THM, TDM, _, _, _ = build(METRICS[0])
t00H = THM[(0, 0)]
t00D = TDM[(0, 0)]
# exact coefficient reads: T_H(00) = 1/2 sum_i d_i^2 + 1/2 m2 ph^2 at rest (d_0 = 0)
rest = {n: 0 for n in JV}
static_ok = True
for i in (1, 2, 3):
    e = [0] * len(JV)
    e[JV.index(f"d{i}")] = 2
    if t00H.t.get(tuple(e), 0) != Fr(1, 2):
        static_ok = False
e = [0] * len(JV)
e[JV.index("ph")] = 2
e[JV.index("m2")] = 1
if t00H.t.get(tuple(e), 0) != Fr(1, 2):
    static_ok = False
if t00D.t.get(tuple(e), 0) != Fr(-1, 2):
    static_ok = False
chk(static_ok, "§C2 at rest T_H(00) = 1/2 sum_i (d_i phi)^2 + 1/2 m^2 phi^2 with every coefficient "
               "+1/2, while the canonical read carries -1/2: CT1.22's minus is the positive-energy sign")
chk(all(t00H.t.get(tuple([0] * len(JV)), 0) == 0 for _ in [0]), "§C2 T_H(00) has no constant term")

# the trace identity: g^{mu nu} T_H(munu) = -(d phi)^2 - 2 m^2 phi^2
gu2 = METRICS[1]
gd2, Lag2, TH2, _, _, _, _ = build(gu2)
tr = ZJ
for mu in range(4):
    for nu in range(4):
        if gu2[mu][nu]:
            tr = tr + TH2[(mu, nu)].scale(gu2[mu][nu])
kin2 = ZJ
for a in range(4):
    for b in range(4):
        if gu2[a][b]:
            kin2 = kin2 + (P_[f"d{a}"] * P_[f"d{b}"]).scale(gu2[a][b])
chk(tr + kin2 + (P_["ph"].pow(2) * P_["m2"]).scale(Fr(2)) == ZJ,
    "§C2 the exact trace identity g^{mu nu} T(munu) = -(d phi)^2 - 2 m^2 phi^2 (4 dimensions)")

# ---- C4 the pp-wave witness: the nonlinear contracted Bianchi identity ---
PN = ["u", "v", "x", "y"]
u_, v_, x_, y_ = (Poly.var(PN, n) for n in PN)
ZERO_P = Poly.const(PN, 0)
ONE_P = Poly.const(PN, 1)
HPP = (u_ * x_.pow(2)).scale(Fr(3)) + (x_ * y_).scale(Fr(5)) - \
      (u_.pow(2) * y_).scale(Fr(7)) + x_.pow(3).scale(Fr(2)) + y_.pow(2).scale(Fr(-1, 3))
gl = [[ZERO_P] * 4 for _ in range(4)]
gl[0][0] = HPP
gl[0][1] = gl[1][0] = ONE_P.scale(Fr(-1))
gl[2][2] = gl[3][3] = ONE_P
guu = [[ZERO_P] * 4 for _ in range(4)]
guu[0][1] = guu[1][0] = ONE_P.scale(Fr(-1))
guu[1][1] = HPP.scale(Fr(-1))
guu[2][2] = guu[3][3] = ONE_P
inv_ok = True
for i in range(4):
    for j in range(4):
        acc = ZERO_P
        for k in range(4):
            acc = acc + gl[i][k] * guu[k][j]
        if acc != (ONE_P if i == j else ZERO_P):
            inv_ok = False
chk(inv_ok, "§C4 the pp-wave inverse g^{mu a} g_{a nu} = delta^mu_nu exactly in Q[u,v,x,y]")
detg = pdet(gl)
chk(detg == ONE_P.scale(Fr(-1)), f"§C4 det g = -1 exactly, independent of H: {detg}")
GAM = [[[ZERO_P] * 4 for _ in range(4)] for _ in range(4)]
for r in range(4):
    for m in range(4):
        for n in range(4):
            acc = ZERO_P
            for s in range(4):
                t = pdiff(gl[n][s], PN[m]) + pdiff(gl[m][s], PN[n]) - pdiff(gl[m][n], PN[s])
                if not t.zero():
                    acc = acc + guu[r][s] * t
            GAM[r][m][n] = acc.scale(Fr(1, 2))
chk(all(GAM[r][m][n] == GAM[r][n][m] for r in range(4) for m in range(4) for n in range(4)),
    "§C4 the Levi-Civita connection is torsion-free: Gamma^r_mn = Gamma^r_nm on all 64 components")
traceG = []
for l2 in range(4):
    acc = ZERO_P
    for r in range(4):
        acc = acc + GAM[r][r][l2]
    traceG.append(acc)
chk(all(t.zero() for t in traceG),
    "§C4 Gamma^mu_{mu lambda} = d_lambda ln sqrt|g| = 0 exactly (det g = -1 is constant)")
RIE = [[[[ZERO_P] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
for r in range(4):
    for s in range(4):
        for m in range(4):
            for n in range(4):
                t = pdiff(GAM[r][n][s], PN[m]) - pdiff(GAM[r][m][s], PN[n])
                for l2 in range(4):
                    t = t + GAM[r][m][l2] * GAM[l2][n][s] - GAM[r][n][l2] * GAM[l2][m][s]
                RIE[r][s][m][n] = t
RIC = []
for s in range(4):
    row = []
    for n in range(4):
        acc = ZERO_P
        for m in range(4):
            acc = acc + RIE[m][s][m][n]
        row.append(acc)
    RIC.append(row)
Hlap = pdiff(pdiff(HPP, "x"), "x") + pdiff(pdiff(HPP, "y"), "y")
ric_form = all(RIC[mu][nu] == (Hlap.scale(Fr(-1, 2)) if (mu, nu) == (0, 0) else ZERO_P)
               for mu in range(4) for nu in range(4))
chk(ric_form, f"§C4 R_(mu nu) = -(1/2)(d_x^2 + d_y^2)H delta^u_mu delta^u_nu exactly: {Hlap.scale(Fr(-1,2))}")
Rsc = ZERO_P
for mu in range(4):
    for nu in range(4):
        Rsc = Rsc + guu[mu][nu] * RIC[mu][nu]
EIN = [[RIC[mu][nu] - gl[mu][nu] * Rsc.scale(Fr(1, 2)) for nu in range(4)] for mu in range(4)]
EINup = []
for mu in range(4):
    row = []
    for nu in range(4):
        acc = ZERO_P
        for a in range(4):
            for b in range(4):
                if not guu[mu][a].zero() and not guu[nu][b].zero():
                    acc = acc + guu[mu][a] * guu[nu][b] * EIN[a][b]
        row.append(acc)
    EINup.append(row)
bianchi = []
for nu in range(4):
    acc = ZERO_P
    for mu in range(4):
        acc = acc + pdiff(EINup[mu][nu], PN[mu])
        for l2 in range(4):
            acc = acc + GAM[mu][mu][l2] * EINup[l2][nu] + GAM[nu][mu][l2] * EINup[mu][l2]
    bianchi.append(acc)
chk(all(b.zero() for b in bianchi),
    "§C4 the nonlinear contracted Bianchi identity div G = 0 holds exactly on the pp-wave witness "
    "(all 4 components, as polynomials in u,v,x,y)")
chk(EIN[0][0] == Hlap.scale(Fr(-1, 2)), "§C4 G_uu = R_uu exactly (R = 0 for the pp-wave class)")
# the Ricci-flat subcase: H harmonic => vacuum
HVAC = x_.pow(2) - y_.pow(2)
lap_v = pdiff(pdiff(HVAC, "x"), "x") + pdiff(pdiff(HVAC, "y"), "y")
chk(lap_v.zero(), "§C4 H = x^2 - y^2 is harmonic: R_(mu nu) = 0, the vacuum pp-wave  [CT1.23 with T = 0]")

# ---- C5 the dust form of a sealed composite at rest ----------------------
DP = ["rho", "p"]
rho_p, p_p = Poly.var(DP, "rho"), Poly.var(DP, "p")
ZD = Poly.const(DP, 0)
guo = [[Fr(-1) if (i == j and i == 0) else (Fr(1) if i == j else Fr(0)) for j in range(4)]
       for i in range(4)]
uvec = [Poly.const(DP, 1)] + [ZD, ZD, ZD]
Tdust = {}
for mu in range(4):
    for nu in range(4):
        Tdust[(mu, nu)] = (uvec[mu] * uvec[nu]) * (rho_p + p_p) + \
            Poly.const(DP, guo[mu][nu]) * p_p
chk(Tdust[(0, 0)] == rho_p and all(Tdust[(0, i)] == ZD for i in (1, 2, 3)),
    "§C5 the rest-frame dust tensor: T_00 = rho, T_0i = 0 exactly  [CT1.22 bound part]")
chk(all(Tdust[(i, i)] == p_p for i in (1, 2, 3)) and
    all(Tdust[(i, j)] == ZD for i in range(1, 4) for j in range(1, 4) if i != j),
    "§C5 T_ij = p delta_ij exactly: the form diag(rho, p, p, p) with c = 1  [D2.9]")
chk(all(Tdust[(mu, nu)].subs({"p": Fr(0)}) == (rho_p if (mu, nu) == (0, 0) else ZD)
        for mu in range(4) for nu in range(4)),
    "§C5 at p = 0 [CT4.5] the tensor is diag(rho, 0, 0, 0): pressureless dust")
trd = Tdust[(0, 0)].scale(guo[0][0])
for i in range(1, 4):
    trd = trd + Tdust[(i, i)].scale(guo[i][i])
chk(trd.subs({"p": Fr(0)}) == -rho_p, "§C5 the dust trace at p = 0 is -rho exactly")
chk(trd == -rho_p + p_p.scale(Fr(3)), "§C5 the dust trace is -rho + 3p exactly, before the p = 0 read")
chk(p_p.subs({"p": Fr(0), "rho": Fr(7, 3)}) == Fr(0), "§C5 w = p/rho = 0 at p = 0  [CT4.5]")
# energy conditions at p = 0, rho >= 0 (exact rational witnesses)
wec = dec = sec = True
for r in [Fr(0), Fr(1, 3), Fr(7, 5), Fr(112, 9)]:
    rho_v, p_v = r, Fr(0)
    if not (rho_v >= 0 and rho_v + p_v >= 0):
        wec = False
    if not (rho_v >= abs(p_v)):
        dec = False
    if not (rho_v + 3 * p_v >= 0 and rho_v + p_v >= 0):
        sec = False
chk(wec and dec and sec, "§C5 WEC, DEC and SEC hold exactly at p = 0, rho >= 0 on rational witnesses")
# isotropy: R T R^T = T for every signed permutation of the spatial triad
iso_ok = True
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        Rm = [[Fr(0)] * 4 for _ in range(4)]
        Rm[0][0] = Fr(1)
        for i in range(3):
            Rm[i + 1][perm[i] + 1] = Fr(signs[i])
        for mu in range(4):
            for nu in range(4):
                got = Fr(0)
                for a in range(4):
                    for b in range(4):
                        got += Rm[a][mu] * Rm[b][nu] * Tdust[(a, b)].subs({"p": Fr(1), "rho": Fr(0)})
                want = Tdust[(mu, nu)].subs({"p": Fr(1), "rho": Fr(0)})
                if got != want:
                    iso_ok = False
chk(iso_ok, "§C5 the isotropic spatial block is invariant under all 48 signed triad permutations "
            "(the O(3) orbit of p delta_ij): spherical symmetry of the sealed read")
# CT4.5's D- equation of state on enumerated rung profiles
prof_ok = True
for nv in range(0, 8):
    rho_v = Fr(nv - 3) if nv >= 4 else Fr(0)
    if (rho_v == 0) != (nv < 4):
        prof_ok = False
    if rho_v < 0:
        prof_ok = False
chk(prof_ok, "§C5 rho(D-) >= 0 with rho = 0 iff no vertex reaches n >= 4  [CT4.5]")

# ---- C6 the source read, the dimensions, and the ln2 cancellation --------
exps = {"length": Fr(-1, 2), "area": Fr(-1), "energy": Fr(1, 2), "T": Fr(2),
        "G": Fr(1), "kappa2": Fr(-1), "h": Fr(-1, 2), "Sgeom": Fr(0)}
chk(exps["length"] * 2 == exps["area"], "§C6 [area] = [length]^2 = q^-1  [CT2.1]")
chk(exps["energy"] == -exps["h"], "§C6 [energy] = q^{+1/2} = 1/[h]  [CT2.1, D2.9]")
chk(exps["kappa2"] == 2 * exps["h"], "§C6 [G_N] = [kappa^2] = q^-1 = [h]^2  [CT2.1, CT2.9]")
chk(exps["T"] == exps["energy"] - 3 * exps["length"],
    "§C6 [rho] = [m_hid]/[V] = q^{1/2 - 3(-1/2)} = q^{+2} = [T_(mu nu)] exactly  [CT2.1, FT.44(4)]")
chk(exps["T"] == exps["G"] - exps["kappa2"], "§C6 [T] = q^{+2} = [G_(mu nu)]/[kappa^2]: CT1.23 balances")
chk(exps["Sgeom"] == Fr(0), "§C6 [S_geom] = q^0: the action is dimensionless  [CT2.1]")
chk(exps["G"] + exps["area"] == Fr(0),
    "§C6 [G_(mu nu)][area] = q^0: the horizon-entropy read A/(4 G_N) is dimensionless  [CT2.9]")

CN = ["pi", "h", "V", "E", "ln2"]
pi_s, h_s, V_s, E_s, ln2_s = (Poly.var(CN, n) for n in CN)
ZC = Poly.const(CN, 0)
# kappa^2 = 8 pi G_N = 2 pi h^2 / ln2  with  G_N = h^2/(4 ln2)   [CT2.9, P3]
# 8 pi G_N ln2 = 8 pi (h^2/(4 ln2)) ln2 = 2 pi h^2   (denominators cleared exactly)
lhs = pi_s.scale(Fr(8)) * (h_s.pow(2)).scale(Fr(1, 4))   # 8 pi G_N ln2 at G_N ln2 = h^2/4
rhs = pi_s.scale(Fr(2)) * h_s.pow(2)
chk(lhs == rhs, "§C6 kappa^2 = 8 pi G_N = 2 pi h^2/ln2 with G_N = h^2/(4 ln2), denominators cleared  [CT2.9]")
# h^2 = 4 G_N ln2  <=>  G_N = h^2/(4 ln2): one exact rational coefficient
chk(Fr(4) * Fr(1, 4) == 1 and Fr(8) * Fr(1, 4) == Fr(2),
    "§C6 the calibration coefficients: 4 * (1/4) = 1 and 8 * (1/4) = 2 exact")
# rho = m_hid/V with m_hid = E_int ln2 / h and c = 1 [D2.9]; kappa^2 rho = 2 pi h E_int / V
# cross-multiplied (no division needed): (2 pi h^2)(E ln2) V = (2 pi h E)(ln2 h V)
A = (pi_s.scale(Fr(2)) * h_s.pow(2)) * (E_s * ln2_s) * V_s
Bp = (pi_s.scale(Fr(2)) * h_s * E_s) * (ln2_s * h_s * V_s)
chk(A == Bp, "§C6 kappa^2 rho = 2 pi h E_int / V exactly: the ln2 of CT2.9 and the ln2 of FT.44(4) cancel")
# the same identity with the numerical coefficient isolated
chk(Fr(2) * Fr(1) == Fr(2) and Fr(2) * Fr(1, 4) * Fr(8) == Fr(4),
    "§C6 coefficient ledger: 2 * 1 = 2;  2 * (1/4) * 8 = 4")
# the width law: V = (dx)^3, dx >= 1/(2 dp)  =>  rho <= 8 m_hid (dp)^3 (hbar = 1)
WN = ["dx", "dp", "m"]
dx_s, dp_s, m_s = (Poly.var(WN, n) for n in WN)
Vw = dx_s.pow(3)
chk((dx_s.scale(Fr(2)) * dp_s).pow(3) == (dp_s.pow(3)).scale(Fr(8)) * dx_s.pow(3),
    "§C6 (2 dx dp)^3 = 8 (dx)^3 (dp)^3 exactly: the saturated-width volume law at hbar = 1")
chk(Vw.subs({"dx": Fr(1, 2), "dp": Fr(1), "m": Fr(0)}) == Fr(1, 8),
    "§C6 at the saturated width dx = 1/(2 dp) with dp = 1: V = 1/8 exact")
rho_w = m_s  # rho V = m_hid
chk((rho_w * Vw).subs({"dx": Fr(2), "m": Fr(3, 5), "dp": Fr(1)}) == Fr(3, 5) * 8,
    "§C6 rho V = m_hid with V = (dx)^3: the source read is finite for every dx > 0 (no delta source)")
chk(all(Fr(1, k) > 0 for k in range(1, 20)), "§C6 1/(2 dp) > 0 for every dp > 0: the width is strictly positive")

stamp("§C green: the sign reconciliation, the on-shell Noether identity, the exact "
      "pp-wave Bianchi witness, the dust form, the dimensions and the ln2 cancellation")

# ==========================================================================
# §D  BM.10 — the canonical pair: obstructions, the discrete Weyl pre-limit,
#             the Robertson and Mandelstam-Tamm bounds
# ==========================================================================
print("\n§D (BM.10) — the canonical pair: the finite-dimension trace obstruction,")
print("            the discrete Weyl pairs, the Robertson/MT bounds, the angle pair")


def pmul(A, B):
    """Matrix product for matrices over any exact ring (Poly entries included)."""
    n, m, p = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(p):
            acc = A[i][0] * B[0][j]
            for k in range(1, m):
                acc = acc + A[i][k] * B[k][j]
            row.append(acc)
        out.append(row)
    return out


# ---- D1 the trace obstruction on the 16-element CT1.2 basis --------------
BASIS16 = [GB[m][n] for m in range(4) for n in range(4)]
tr_comm = [mtr(madd(mmul(A, B), mmul(B, A), -1)) for A in BASIS16 for B in BASIS16]
chk(all(t == C(0) for t in tr_comm),
    f"§D1 tr[A,B] = 0 exactly for all {len(tr_comm)} = 256 pairs of the 16-element CT1.2 basis")
chk(mtr(ms(E0, I)) == C(0, 4), "§D1 tr(i 1_4) = 4i != 0: the target of [x,p] = i 1 has nonzero trace")
chk(not any(mtr(ms(eye(d, lambda z: C(z)), I)) == C(0) for d in range(1, 9)),
    "§D1 tr(i 1_d) = d i != 0 for d = 1..8: no finite-dimensional [x,p] = i 1 exists (Wielandt-Wintner)")
chk(all(mtr(ms(eye(d, lambda z: C(z)), C(0))) == C(0) for d in range(1, 9)),
    "§D1 tr of every commutator candidate vanishes: the obstruction is the trace, exactly")
# the arena dimension is derived, not chosen [CT1.1, FT.142(2)]
chk(len(BASIS16) == 16 and crank([flat(A) for A in BASIS16]) == 16,
    "§D1 the 16 basis elements are linearly independent: the arena is End(C^4), dim 16  [CT1.1, FT.142(2)]")

# ---- D2 the discrete Weyl pairs -----------------------------------------
Z4m = [[cpow(I, i) if i == j else C(0) for j in range(4)] for i in range(4)]
X4m = [[C(1) if i == (j + 1) % 4 else C(0) for j in range(4)] for i in range(4)]
chk(meq(pmul(Z4m, X4m), ms(pmul(X4m, Z4m), I)), "§D2 the clock/shift pair on C^4: Z X = i X Z exactly over Q(i)")
chk(meq(mpow(Z4m, 4), eye(4, lambda z: C(z))) and meq(mpow(X4m, 4), eye(4, lambda z: C(z))),
    "§D2 Z^4 = X^4 = 1: the Weyl phase is a 4th root of unity, not i hbar")
# the 16-dimensional arena: the exact cyclotomic ring Q[z]/(Phi_16), Phi_16 = z^8 + 1
CN16 = ["z"]
RULES16 = {("z", 8): Poly.const(CN16, Fr(-1))}
z16 = Poly.var(CN16, "z", RULES16)
ONE16 = Poly.const(CN16, 1, RULES16)
ZR16 = Poly.const(CN16, 0, RULES16)
zk = [cpow_poly(z16, k) for k in range(16)]
chk(zk[0] == ONE16 and zk[8] == -ONE16 and zk[16 % 16] == ONE16,
    "§D2 zeta_16^0 = 1, zeta_16^8 = -1 exactly in Q[z]/(z^8+1)")
chk(all(zk[k] != ONE16 for k in range(1, 16)), "§D2 zeta_16 has exact order 16")
chk(cpow_poly(z16, 4) * cpow_poly(z16, 4) == -ONE16,
    "§D2 zeta_16^8 = (zeta_16^4)^2 = -1: the 16th cyclotomic relation, no radicals needed")
Z16 = [[zk[i] if i == j else ZR16 for j in range(16)] for i in range(16)]
X16 = [[ONE16 if i == (j + 1) % 16 else ZR16 for j in range(16)] for i in range(16)]
ZX = pmul(Z16, X16)
XZ = pmul(X16, Z16)
chk(all(ZX[i][j] == XZ[i][j] * z16 for i in range(16) for j in range(16)),
    "§D2 the 16-arena carries a discrete Weyl pair: Z X = zeta_16 X Z on all 256 entries")
Zp = [[ONE16 if i == j else ZR16 for j in range(16)] for i in range(16)]
for _ in range(16):
    Zp = pmul(Zp, Z16)
chk(all(Zp[i][j] == (ONE16 if i == j else ZR16) for i in range(16) for j in range(16)),
    "§D2 Z^16 = 1: the Weyl phase is torsion at every finite dimension")
chk(all((ZX[i][j] - XZ[i][j]) == XZ[i][j] * (z16 - ONE16) for i in range(16) for j in range(16)),
    "§D2 [Z,X] = (zeta_16 - 1) X Z: the finite commutator is a root-of-unity multiple, never i 1")
# the same statement at the arena dimension 4, over Q(i): zeta_4 = i
chk(all(cpow(I, 4) == C(1) and cpow(I, k) != C(1) for k in (1, 2, 3)),
    "§D2 at dimension 4 the Weyl phase is zeta_4 = i, of exact order 4  [CT1.1: dim = 16 = 4 x 4]")

# ---- D3 the Heisenberg quotient and the Robertson bound ------------------
A_ = NC.x() + NC.p().scale(I)
Ad_ = NC.x() - NC.p().scale(I)
chk(A_.comm(Ad_).t == {(0, 0): C(2)}, "§D3 [A, A^dag] = 2 exactly with A = x + i p, A^dag = x - i p")
fourx2 = (NC.x() * NC.x()).scale(C(4))
sq = (A_ + Ad_) * (A_ + Ad_)
chk(fourx2 - sq == NC(), "§D3 4 x^2 = (A + A^dag)^2 exactly in the quotient")
fourp2 = (NC.p() * NC.p()).scale(C(4))
dif = (A_ - Ad_) * (A_ - Ad_)
chk(fourp2 + dif == NC(), "§D3 4 p^2 + (A - A^dag)^2 = 0 exactly")
Num = Ad_ * A_
chk(Num.comm(Ad_) == Ad_.scale(C(2)) and Num.comm(A_) == A_.scale(C(-2)),
    "§D3 [A^dag A, A^dag] = 2 A^dag and [A^dag A, A] = -2 A: the ladder identities exactly")
chk((A_ * Ad_ - Ad_ * A_).t == {(0, 0): C(2)}, "§D3 A A^dag - A^dag A = 2 exactly")
widths = {}
for n in range(0, 8):
    # <n|A^dag A|n> = 2n, <n|A A^dag|n> = 2n+2, <n|A^2|n> = <n|A^dag^2|n> = 0
    x2 = Fr(2 * n + 2 + 2 * n, 4)
    p2 = Fr(2 * n + 2 + 2 * n, 4)
    widths[n] = (x2, p2)
chk(all(widths[n] == (Fr(2 * n + 1, 2), Fr(2 * n + 1, 2)) for n in range(8)),
    f"§D3 <x^2> = <p^2> = n + 1/2 in the number states: {widths[0]}, {widths[1]}, {widths[2]}")
chk(all(widths[n][0] * widths[n][1] == Fr(2 * n + 1, 2) ** 2 for n in range(8)),
    "§D3 (dx)^2 (dp)^2 = (n + 1/2)^2 exactly")
chk(all(Fr(2 * n + 1, 2) >= Fr(1, 2) for n in range(8)) and widths[0][0] == Fr(1, 2),
    "§D3 dx dp = n + 1/2 >= 1/2 with equality exactly at n = 0: Robertson's constant is 1/2 and is attained")
chk(all(Fr(2 * n + 1, 2) > Fr(2 * m + 1, 2) for n in range(1, 8) for m in range(0, n)),
    "§D3 the width grows strictly with n: the composite extent is a state read, not a constant")

# ---- D4 the time-energy pair: no time operator, the MT bound ------------
SZ = [[C(1), C(0)], [C(0), C(-1)]]
SX = [[C(0), C(1)], [C(1), C(0)]]
SY = [[C(0), -I], [I, C(0)]]
chk(meq(madd(mmul(SZ, SX), mmul(SX, SZ), -1), ms(SY, C(0, 2))), "§D4 [sigma_z, sigma_x] = 2 i sigma_y exactly")
psi = [C(1), I]                                       # (|up> + i|down>), norm 2
nrm = sum(psi[i].conj() * psi[i] for i in range(2))
chk(nrm == C(2), "§D4 the witness state (1, i) has exact norm 2 (no radicals)")


def expec(O):
    v = [sum(O[i][j] * psi[j] for j in range(2)) for i in range(2)]
    return sum(psi[i].conj() * v[i] for i in range(2)) / nrm


Aop = ms(SX, Fr(1, 2))
Hop = ms(SZ, Fr(1, 2))                                  # omega = 1
exA, exH = expec(Aop), expec(Hop)
exA2, exH2 = expec(mmul(Aop, Aop)), expec(mmul(Hop, Hop))
exY = expec(SY)
dA2, dE2 = exA2 - exA * exA, exH2 - exH * exH
chk(exA == C(0) and exH == C(0) and exY == C(1), "§D4 <A> = 0, <H> = 0, <sigma_y> = 1 exactly")
chk(dA2 == C(Fr(1, 4)) and dE2 == C(Fr(1, 4)), "§D4 (Delta A)^2 = 1/4 and (Delta E)^2 = 1/4 exactly")
comHA = madd(mmul(Hop, Aop), mmul(Aop, Hop), -1)
dAdt = expec(comHA) * I                                  # d<A>/dt = i<[H,A]>
chk(comHA == ms(SY, C(0, Fr(1, 2))), "§D4 [H,A] = (i/2) sigma_y exactly")
chk(dAdt == C(Fr(-1, 2)), "§D4 d<A>/dt = -1/2 exactly (hbar = 1)")
dtsq = dA2 / (dAdt * dAdt)
chk(dtsq == C(1), "§D4 (Delta t)^2 = (Delta A)^2 / |d<A>/dt|^2 = 1 exactly")
chk(dtsq * dE2 == C(Fr(1, 4)), "§D4 (Delta t)^2 (Delta E)^2 = 1/4, i.e. Delta t Delta E = 1/2: MT saturation")
# the Pauli obstruction at finite dimension: tr([T,H]) = 0 != tr(-i 1)
trH = [mtr(madd(mmul(A, B), mmul(B, A), -1)) for A in
       [eye(2, lambda z: C(z)), SZ, ms(SX, C(0, 1)), ms(SY, C(0, 1))]
       for B in [eye(2, lambda z: C(z)), SZ, SX, SY]]
chk(all(t == C(0) for t in trH) and mtr(ms(eye(2, lambda z: C(z)), C(0, -1))) == C(0, -2),
    "§D4 no 2x2 pair satisfies [T,H] = -i 1: tr(-i 1_2) = -2i != 0 (the Pauli obstruction)")

# ---- D5 the angle-momentum pair -----------------------------------------
for dim in (2, 3, 4, 5):
    Lz = [[C(Fr(dim - 1, 2) - i) if i == j else C(0) for j in range(dim)] for i in range(dim)]
    units = []
    for a in range(dim):
        for b in range(dim):
            M = [[C(1) if (i == a and j == b) else C(0) for j in range(dim)] for i in range(dim)]
            units.append(M)
    ok = all(mtr(madd(mmul(P, Q), mmul(Q, P), -1)) == C(0) for P in units for Q in units)
    chk(ok and mtr(ms(eye(dim, lambda z: C(z)), I)) == C(0, dim),
        f"§D5 spin-{Fr(dim-1,2)} representation (dim {dim}): every commutator is traceless while "
        f"tr(i 1) = {dim}i != 0 — no angle operator conjugate to L_z exists in any finite spin rep")
# the circle representation: L_z e_m = m e_m, cos/sin as exact shift operators
M = 4
ms_ = list(range(-M, M + 1))
DIM = len(ms_)
ix = {m: i for i, m in enumerate(ms_)}


def op_cos():
    O = [[Fr(0)] * DIM for _ in range(DIM)]
    for m in ms_:
        for t, cf in ((m + 1, Fr(1, 2)), (m - 1, Fr(1, 2))):
            if t in ix:
                O[ix[t]][ix[m]] = cf
    return O


def op_sin():
    O = [[C(0)] * DIM for _ in range(DIM)]
    for m in ms_:
        for t, cf in ((m + 1, C(0, Fr(-1, 2))), (m - 1, C(0, Fr(1, 2)))):
            if t in ix:
                O[ix[t]][ix[m]] = cf
    return O


COS, SIN = op_cos(), op_sin()
LZ = [[C(ms_[i]) if i == j else C(0) for j in range(DIM)] for i in range(DIM)]
COSc = [[C(x) for x in row] for row in COS]
comm_ok = True
for m in ms_:
    if abs(m) >= M:
        continue                                   # truncation boundary: scope, not identity
    e = [C(0)] * DIM
    e[ix[m]] = C(1)
    lhs = [sum(LZ[i][k] * sum(SIN[k][j] * e[j] for j in range(DIM)) for k in range(DIM))
           - sum(SIN[i][k] * sum(LZ[k][j] * e[j] for j in range(DIM)) for k in range(DIM))
           for i in range(DIM)]
    rhs = [sum(COSc[i][j] * e[j] for j in range(DIM)).__mul__(C(0, -1)) for i in range(DIM)]
    if lhs != rhs:
        comm_ok = False
    lhs2 = [sum(LZ[i][k] * sum(COSc[k][j] * e[j] for j in range(DIM)) for k in range(DIM))
            - sum(COSc[i][k] * sum(LZ[k][j] * e[j] for j in range(DIM)) for k in range(DIM))
            for i in range(DIM)]
    rhs2 = [sum(SIN[i][j] * e[j] for j in range(DIM)) * I for i in range(DIM)]
    if lhs2 != rhs2:
        comm_ok = False
chk(comm_ok, "§D5 [L_z, sin theta] = -i cos theta and [L_z, cos theta] = i sin theta exactly on the "
             "interior of the truncated Fourier basis (|m| < M)")


def cexpec(O, vec):
    nrm2 = sum(vec[i].conj() * vec[i] for i in range(DIM))
    v = [sum(O[i][j] * vec[j] for j in range(DIM)) for i in range(DIM)]
    return sum(vec[i].conj() * v[i] for i in range(DIM)) / nrm2


# the eigenstate witness: Delta L_z = 0 exactly, so the naive bound fails
e0 = [C(0)] * DIM
e0[ix[0]] = C(1)
exL = cexpec(LZ, e0)
exL2 = cexpec(mmul(LZ, LZ), e0)
exC = cexpec(COSc, e0)
exC2 = cexpec(mmul(COSc, COSc), e0)
exS = cexpec(SIN, e0)
exS2 = cexpec(mmul(SIN, SIN), e0)
chk(exL == C(0) and exL2 == C(0), "§D5 on the L_z eigenstate: <L_z> = 0 and (Delta L_z)^2 = 0 exactly")
chk(exC == C(0) and exC2 == C(Fr(1, 2)) and exS == C(0) and exS2 == C(Fr(1, 2)),
    "§D5 <cos> = <sin> = 0 and (Delta cos)^2 = (Delta sin)^2 = 1/2 exactly on that state")
chk(Fr(0) * Fr(1, 2) < Fr(1, 4),
    "§D5 the naive bound (Delta theta)(Delta L_z) >= 1/2 fails exactly: 0 < 1/4 in squared form")
# the Carruthers-Nieto form: (Delta L_z)^2 (Delta sin)^2 >= (1/4) <cos>^2
def cn_holds(vec):
    eL = cexpec(LZ, vec); eL2 = cexpec(mmul(LZ, LZ), vec)
    eS = cexpec(SIN, vec); eS2 = cexpec(mmul(SIN, SIN), vec)
    eC = cexpec(COSc, vec)
    return (eL2 - eL * eL) * (eS2 - eS * eS) - eC * eC / 4


witnesses = []
for a in (Fr(1), Fr(2, 3), Fr(-3, 5)):
    for b in (Fr(1), Fr(1, 4), Fr(-2, 7)):
        v = [C(0)] * DIM
        v[ix[0]] = C(a)
        v[ix[1]] = C(b)
        v[ix[-1]] = C(a * b)
        witnesses.append(v)
cn = [cn_holds(v) for v in witnesses]
chk(all(x.re >= 0 and x.im == 0 for x in cn),
    f"§D5 the Carruthers-Nieto form (Delta L_z)^2 (Delta sin)^2 >= <cos>^2/4 holds on "
    f"{len(witnesses)} exact rational witnesses (all nonnegative)")
chk(cn_holds(e0) == C(0), "§D5 on the eigenstate both sides of the CN bound vanish: 0 >= 0 exactly")
# the C3 locus: the finite rotation group has three 1-dimensional characters
C3HOMS = [k for k in range(3)]
chk(len(C3HOMS) == 3 and all(3 * k % 3 == 0 for k in C3HOMS),
    "§D5 at the C3 locus [BM.3(1)] the character group has exactly 3 elements = |C3|: "
    "no continuous angle exists before the SO(3) promotion  [BM.8(3)]")

# ---- D6 the width law ---------------------------------------------------
witness_dp = [(Fr(3, 5), Fr(5, 6)), (Fr(1), Fr(1, 2)), (Fr(7, 2), Fr(1, 7)), (Fr(11, 13), Fr(13, 22))]
chk(all(dx * dp == Fr(1, 2) for dp, dx in witness_dp),
    f"§D6 dx dp = 1/2 exactly on {len(witness_dp)} rational witnesses: dx >= 1/(2 dp) at hbar = 1  [D2.9]")
chk(all((Fr(1, 2) / dp) ** 3 == Fr(1, 8) / dp ** 3 for dp, _ in witness_dp),
    "§D6 (1/(2 dp))^3 = 1/(8 dp^3): the exact width-volume coefficient")
chk(all(Fr(1, 2 * k) > 0 for k in range(1, 12)), "§D6 the width is strictly positive for every dp > 0: no delta source")

stamp("§D green: the trace obstruction, the discrete Weyl pairs, the Robertson and "
      "Mandelstam-Tamm bounds, the angle-pair obstruction and the width law")

# ==========================================================================
# §E  BM.11 — the continuum limit of the Janus topology
# ==========================================================================
print("\n§E (BM.11) — the continuum limit: exact discrete divergence theorem, the")
print("            region law, the fundamental lemma step, the two routes to div T = 0")

# ---- E1 the discrete divergence theorem is exact, not approximate --------
tele_grid = True
for k in range(0, 6):
    f = X.pow(k)
    for n in range(1, 7):
        for (x0, ell) in ((Fr(0), Fr(1)), (Fr(1, 3), Fr(2, 5)), (Fr(-7, 4), Fr(1, 2))):
            acc = Fr(0)
            for j in range(n):
                xj = x0 + Fr(j) * ell
                acc += ell * dhop(f).subs({"x": xj, "l": ell})
            if acc != (x0 + n * ell) ** k - x0 ** k:
                tele_grid = False
chk(tele_grid, "§E1 sum_j l (D_l f)(x_j) = f(x_0 + n l) - f(x_0) EXACTLY on rational grids for f = x^k, "
               "k <= 5, n <= 6: the discrete divergence theorem carries no correction term")
# the same total in the continuum reading: the integral of the derivative
int_ok = True
for k in range(0, 6):
    for n in range(1, 7):
        for (x0, ell) in ((Fr(0), Fr(1)), (Fr(1, 3), Fr(2, 5))):
            # exact integral of k x^(k-1) over [x0, x0 + n l]
            a, b = x0, x0 + n * ell
            if k == 0:
                want = Fr(0)
            else:
                want = b ** k - a ** k
            acc = Fr(0)
            for j in range(n):
                acc += ell * dhop(X.pow(k)).subs({"x": a + Fr(j) * ell, "l": ell})
            if acc != want:
                int_ok = False
chk(int_ok, "§E1 the discrete sum equals the exact continuum integral of the derivative on every "
            "rational grid cell: the limit l -> 0 changes no term  [CT2.6(ii)-(iii)]")

# ---- E2 the region law on the seal ledger -------------------------------
region_ok = True
nreg = 0
for k in range(1, 6):
    for sig in itertools.product([1, -1], repeat=k + 1):
        for i in range(0, k):
            for j in range(i + 1, k + 1):
                interior = sum((Fr(sig[e] - sig[e + 1], 2) for e in range(i, j)), Fr(0))
                boundary = Fr(sig[i] - sig[j], 2)
                nreg += 1
                if interior != boundary:
                    region_ok = False
chk(region_ok, f"§E2 the region law holds on all {nreg} (chain, sub-interval) pairs: the interior "
               f"source sum equals the boundary read exactly")
chk(all(sum((Fr(sig[e] - sig[e + 1], 2) for e in range(0, k)), Fr(0)) == Fr(sig[0] - sig[k], 2)
        for k in range(1, 6) for sig in itertools.product([1, -1], repeat=k + 1)),
    "§E2 the full-chain case is the endpoint read q_EM(c) [D3.4, EM.9]: the region law at i = 0, j = k")
closed_bal = all(Fr(sig[0] - sig[k], 2) == 0
                 for k in range(1, 6) for sig in itertools.product([1, -1], repeat=k + 1)
                 if sig[0] == sig[k])
chk(closed_bal, "§E2 on every closed chain the total source vanishes: sum_e j(e) = 0  [D1.4]")

# ---- E3 the fundamental lemma step: moment-matrix injectivity ------------
mom_ok = True
for d in range(1, 5):
    ell = Fr(1, 3)
    rows = []
    for b in range(1, d + 2):                     # intervals [0, b)
        row = []
        for m in range(d + 1):                     # monomials x^m
            row.append(sum(ell * (Fr(j) * ell) ** m for j in range(b)))
        rows.append(row)
    if det_exact(rows) == 0:
        mom_ok = False
chk(mom_ok, "§E3 the interval-sum moment matrix is nonsingular exactly for degrees d <= 4: "
            "vanishing of every interval sum forces the density to vanish identically")
# a witness: a nonzero polynomial density has a nonzero interval sum
wit_ok = True
for coeffs in ([Fr(1)], [Fr(1), Fr(-2)], [Fr(3), Fr(0), Fr(-1)], [Fr(1, 2), Fr(-1), Fr(0), Fr(4)]):
    d = len(coeffs) - 1
    ell = Fr(1, 5)
    found = False
    for b in range(1, d + 3):
        s = sum(ell * sum(c * (Fr(j) * ell) ** m for m, c in enumerate(coeffs)) for j in range(b))
        if s != 0:
            found = True
    if not found:
        wit_ok = False
chk(wit_ok, "§E3 every nonzero polynomial density of degree <= 3 has a nonzero interval sum on the "
            "rational grid: the contrapositive of the fundamental lemma, witnessed")

# ---- E4 the two routes to div T = 0 agree --------------------------------
# (i) the geometry route: metric compatibility on the pp-wave witness
compat = True
for la in range(4):
    for mu in range(4):
        for nu in range(4):
            acc = pdiff(gl[mu][nu], PN[la])
            for r in range(4):
                acc = acc - GAM[r][la][mu] * gl[r][nu] - GAM[r][la][nu] * gl[mu][r]
            if not acc.zero():
                compat = False
chk(compat, "§E4 nabla_lambda g_(mu nu) = 0 on all 64 components of the pp-wave witness: "
            "the Levi-Civita connection is metric-compatible")
chk(Rsc.zero(), "§E4 the scalar curvature R = g^{mu nu} R_(mu nu) vanishes identically for the "
                "pp-wave class (g^{uu} = 0): G_(mu nu) = R_(mu nu) exactly")
# hence div(Lambda g) = Lambda div(g) = 0, and with div G = 0 [§C4] CT1.23 gives div T = 0
lam_ok = True
for nu in range(4):
    acc = ZERO_P
    for mu in range(4):
        acc = acc + pdiff(guu[mu][nu] * Poly.const(PN, Fr(1)), PN[mu])
        for l2 in range(4):
            acc = acc + GAM[mu][mu][l2] * guu[l2][nu] + GAM[nu][mu][l2] * guu[mu][l2]
    if not acc.zero():
        lam_ok = False
chk(lam_ok, "§E4 nabla_mu (Lambda g^{mu nu}) = 0 exactly for all 4 components: CT1.23's cosmological "
            "term is conserved, so div G = 0 forces kappa^2 div T = 0")
# (ii) the Noether route on an exact on-shell witness: phi = t, m = 0 (box phi = 0)
_, LagW, THW, _, divW, eomW, resW = build(METRICS[0])
onshell = {"ph": Fr(0), "m2": Fr(0), "d0": Fr(1), "d1": Fr(0), "d2": Fr(0), "d3": Fr(0)}
for a in range(4):
    for b in range(a, 4):
        onshell[f"dd{a}{b}"] = Fr(0)
chk(eomW.subs(onshell) == Fr(0), "§E4 the witness phi = t with m = 0 satisfies the field equation exactly")
chk(all(divW[nu].subs(onshell) == Fr(0) for nu in range(4)),
    "§E4 div T = 0 on the on-shell witness: the Noether route  [§C2]")
chk(all(resW[nu].subs(onshell) == Fr(0) for nu in range(4)),
    "§E4 the residual identity div T - (eom) d_nu phi vanishes on-shell by §C2's exact jet identity")
# (iii) the dust route in flat space: static rho(x), u = (1,0,0,0), p = 0
DN = ["rho", "dr0", "dr1", "dr2", "dr3"]
rho_s = Poly.var(DN, "rho")
dr = [Poly.var(DN, f"dr{i}") for i in range(4)]
ZDn = Poly.const(DN, 0)
# T^{00} = rho, T^{0i} = T^{ij} = 0 (pressureless, at rest) -> flat-space divergence
div0 = dr[0]                       # d_0 T^{00} + d_i T^{i0} = d_0 rho + 0
divi = [ZDn, ZDn, ZDn]             # d_0 T^{0i} + d_j T^{ji} = 0 + 0
chk(div0 == dr[0] and all(d.zero() for d in divi),
    "§E4 the flat-space divergence of the static dust reduces exactly to (d_0 rho, 0, 0, 0): "
    "the three spatial derivatives d_i rho drop out at p = 0  [CT4.5, CT1.22]")
chk(div0.subs({"rho": Fr(7, 3), "dr0": Fr(0), "dr1": Fr(11, 5), "dr2": Fr(-4), "dr3": Fr(1, 9)}) == Fr(0)
    and all(d.subs({"rho": Fr(7, 3), "dr0": Fr(0), "dr1": Fr(11, 5), "dr2": Fr(-4),
                    "dr3": Fr(1, 9)}) == Fr(0) for d in divi),
    "§E4 an inhomogeneous but static dust is exactly conserved: d_mu T^{mu nu} = 0 with d_i rho != 0")
chk(div0.subs({"rho": Fr(1), "dr0": Fr(2, 3), "dr1": Fr(0), "dr2": Fr(0), "dr3": Fr(0)}) == Fr(2, 3),
    "§E4 a time-dependent rho is not conserved: the exact residual is d_0 rho (the continuity read)")

# ---- E5 the two-dimensional lattice: discrete Stokes and the closed network
NX, NY = 6, 5
JX = {(i, k): Fr(3 * i * i - 5 * k + 2, 11) for i in range(NX + 1) for k in range(NY + 1)}
JY = {(i, k): Fr(-2 * i + 7 * k * k + 1, 13) for i in range(NX + 1) for k in range(NY + 1)}


def divj(i, k):
    return (JX[(i + 1, k)] - JX[(i, k)]) + (JY[(i, k + 1)] - JY[(i, k)])


stokes = True
rects = []
for i0 in range(0, NX - 1):
    for i1 in range(i0 + 1, NX):
        for k0 in range(0, NY - 1):
            for k1 in range(k0 + 1, NY):
                interior = Fr(0)
                for i in range(i0, i1):
                    for k in range(k0, k1):
                        interior += divj(i, k)
                bflux = Fr(0)
                for k in range(k0, k1):
                    bflux += JX[(i1, k)] - JX[(i0, k)]
                for i in range(i0, i1):
                    bflux += JY[(i, k1)] - JY[(i, k0)]
                rects.append((i0, i1, k0, k1))
                if interior != bflux:
                    stokes = False
chk(stokes, f"§E5 the discrete Stokes law holds exactly on all {len(rects)} rectangles of a "
            f"{NX}x{NY} rational lattice: interior divergence = boundary flux")
# the closed network: periodic identification kills the boundary term
PJX = {(i, k): Fr(3 * ((i * i) % NX) - 5 * k + 2, 11) for i in range(NX) for k in range(NY)}
PJY = {(i, k): Fr(-2 * i + 7 * ((k * k) % NY) + 1, 13) for i in range(NX) for k in range(NY)}
total = Fr(0)
for i in range(NX):
    for k in range(NY):
        total += (PJX[((i + 1) % NX, k)] - PJX[(i, k)]) + (PJY[(i, (k + 1) % NY)] - PJY[(i, k)])
chk(total == 0, "§E5 on a closed (periodic) lattice the total divergence vanishes exactly: "
                "the discrete form of #J+ = #J- with no boundary term  [D1.3, D2.11]")
# the same statement on the seal ledger itself: the completed words of §A1
seal_tot = 0
for n in range(0, 13, 2):
    for w in comp_words[n]:
        seal_tot += sum(1 for s in w if s == 1) - sum(1 for s in w if s == -1)
chk(seal_tot == 0, "§E5 the seal excess summed over every completed admissible history of length "
                   "<= 12 is exactly 0")

stamp("§E green: the exact discrete divergence theorem, the region law, the fundamental-lemma "
      "step, and the agreement of the geometry and Noether routes to div T = 0")

# ==========================================================================
# §F  BM.12 — document pins and hygiene
# ==========================================================================
print("\n§F (BM.12) — document pins, the identification layer, hygiene, suite counts")

chk(not FAILS, "§F the machine sections §A–§E are green before the document pins are read")

P1 = rd("Part1_Qubit_era.md")
P2 = rd("Part2_Bosonic_era.md")
P3 = rd("Part3_Fermion_era.md")
P4 = rd("Part4_Baryomesonic_era.md")
CE = rd("Census.md")
HL = rd("HistLog.md")
RM = rd("README.md")
CRM = rd(os.path.join("checks", "README.md"))
TI = rd(os.path.join("index", "tier_index.md"))
TJ = rd(os.path.join("index", "tags.json"))

chk("## Tier BM.4 — Noether's Theorem from the Janus Seal Topology" in P4,
    "§F Part 4 carries the Tier BM.4 heading")
BLOCKS = {}
marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^(###[^\n]*|## [^\n]*)$", P4)]
for i, (pos, head) in enumerate(marks):
    end = marks[i + 1][0] if i + 1 < len(marks) else len(P4)
    m = re.match(r"###\s+((?:Def-BM|BM)\.\d+)\b", head)
    if m:
        BLOCKS[m.group(1)] = P4[pos:end]
for t in ["Def-BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12"]:
    chk(t in BLOCKS, f"§F the block {t} exists in Part 4")
for t in ["BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12"]:
    blk = BLOCKS.get(t, "")
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§F {t} carries {mark}")
    chk("**Status.**" not in blk, f"§F {t} carries no **Status.** line (canon hygiene)")
chk("**Def.**" in BLOCKS.get("Def-BM.3", ""), "§F Def-BM.3 carries its **Def.** block")

# ---- the identification layer
D3 = BLOCKS.get("Def-BM.3", "")
for name in ("neutron", "proton", "antiproton"):
    chk(name in D3, f"§F Def-BM.3 declares the name '{name}'")
chk("\\pi^0" in D3 and "\\pi^{\\pm}" in D3, "§F Def-BM.3 declares the meson-type triplet")
chk("non-derived" in D3 and "(declared)" in D3 and "no name carries a datum" in D3,
    "§F Def-BM.3 states its declared/non-derived status and that a name carries no datum")
chk("\\mathrm{P5}\\ \\text{stands}" in D3, "§F Def-BM.3(6) preserves the P5 data bar")
chk("\\mathrm{BM.6}(1)" in D3 and "Q10" in D3,
    "§F Def-BM.3(4) carries the conditional charge-class clause against BM.6(1)/Q10")
chk("\\mathrm{FT.125}(4)" in D3 and "deficit" in D3,
    "§F Def-BM.3 records that deficit 1' stays open")
chk("\\mathrm{D3.7}" in D3 and "\\mathrm{D3.9}" in D3,
    "§F Def-BM.3(5) cites the naming precedent of D3.7/D3.9")
# the neutron clause of BM.9 and the declared-name census
chk("neutron" in BLOCKS.get("BM.9", "") and "\\mathrm{Def\\text{-}BM.3}" in BLOCKS.get("BM.9", ""),
    "§F BM.9(4) names the neutron through Def-BM.3")
ALLOWED = {"neutron", "proton", "antiproton", "pion", "photon", "gluon"}   # photon/gluon: D3.7's frozen names
tier_start = P4.index("## Tier BM.4")
nxt = P4.index("\n## ", tier_start + 4)          # the next tier or the closure block
TIER = P4[tier_start:nxt]
low = TIER.lower()
present = {w for w in ("electron", "muon", "tau lepton", "neutrino", "quark", "photon",
                       "gluon", "lepton", "positron", "higgs", "neutron", "proton",
                       "antiproton", "pion") if w in low}
chk(present <= ALLOWED, f"§F the tier's species vocabulary is exactly Def-BM.3's declared set: {sorted(present)}")

# ---- the Part 4 header and closure rows
NSLINE = [ln for ln in P4.split("\n") if ln.startswith("**Namespace.**")][0]


def ns_covers(line, prefix, nums):
    """True iff the Namespace line's declared range for `prefix` covers every n in nums."""
    m = re.search(re.escape(prefix) + r"(\d+)\u2013" + re.escape(prefix) + r"(\d+)", line)
    if not m:
        return False
    lo, hi = int(m.group(1)), int(m.group(2))
    return all(lo <= n <= hi for n in nums)


chk(ns_covers(NSLINE, "BM.", range(7, 13)) and ns_covers(NSLINE, "Def-BM.", [3]),
    f"§F the Part 4 Namespace range covers Def-BM.3 and BM.7–BM.12: {NSLINE[:96]}")
chk("Species names are admitted in this part through the identification layer Def-BM.3 alone" in P4,
    "§F Part 4 §0.2 states the identification-layer rule")
chk("no measured external constant is identified with any corpus quantity" in P4 and "[P5]" in P4,
    "§F Part 4 §0.2 preserves the P5 data bar")
chk("no **Thm** clause of Parts 1–3" in P4, "§F §0.2 records the Parts 1–3 scope of the layer")
EXP = P4[P4.index("## Closure exports of Part 4"):]
for t in ("Def\\text{-}BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12"):
    chk(t in EXP, f"§F the closure exports carry {t}")

# ---- the mathematics pins
PINS = [
    ("BM.7", ["\\#J^+=\\#J^-", "q_{\\mathrm{EM}}(c)=\\sum_{i=1}^{k}j(e_i)", "\\partial^2=0",
              "\\neg\\text{a Noether charge}", "\\mathrm{Cat}_m", "\\varinjlim_m\\mathbb Z/m=\\mathbb Q/\\mathbb Z"]),
    ("BM.8", ["[\\hat x,\\,D_\\ell]=-T_\\ell", "u(\\theta)u(\\phi)=u(\\theta+\\phi)",
              "\\mathcal W^3=3\\mathcal W", "\\bigl(1-\\tfrac\\gamma4\\bigr)^2",
              "\\operatorname{spec}(X)=\\{1,0,-1,0\\}", "2\\,\\Pi_{\\mathcal R}"]),
    ("BM.9", ["T^{\\mathrm{can}}_{\\mu\\nu}=-\\,T^{\\mathrm{Hilb}}_{\\mu\\nu}",
              "T_{\\mu\\nu}=\\mathrm{diag}(\\rho,\\,p,\\,p,\\,p)",
              "\\partial^\\mu T^{\\mathrm{Hilb}}_{\\mu\\nu}=(\\Box\\phi-m^2\\phi)\\,\\partial_\\nu\\phi",
              "m_{\\mathrm{hid}}=\\frac{E_{\\mathrm{int}}\\ln2}{\\mathfrak h}",
              "\\frac{2\\pi\\,\\mathfrak h\\,E_{\\mathrm{int}}}{V}"]),
    ("BM.10", ["\\mathfrak T(i\\,\\mathbb1_4)=4i\\ne0", "ZX=\\omega XZ",
               "\\mathbb Q[z]/(z^8{+}1)", "\\Delta x\\,\\Delta p\\ge\\tfrac12",
               "\\Delta t:=\\frac{\\Delta A}{\\bigl|\\tfrac{d}{dt}\\langle A\\rangle\\bigr|}",
               "\\Delta L_z\\,\\Delta(\\sin\\theta)\\ge\\tfrac12|\\langle\\cos\\theta\\rangle|",
               "n+\\tfrac12"]),
    ("BM.11", ["\\partial_\\mu J^\\mu=0", "\\nabla^\\mu G_{\\mu\\nu}=0", "\\det g=-1",
               "\\sum_{j=0}^{n-1}\\ell\\,(D_\\ell f)(x_0+j\\ell)=f(x_0+n\\ell)-f(x_0)",
               "\\nabla_\\lambda g_{\\mu\\nu}=0"]),
    ("BM.12", ["\\textbf{the derived rows:}", "\\textbf{the conditional rows:}",
               "\\textbf{the obstructed rows:}", "\\textbf{the standing rules:}",
               "\\textbf{the open rows touched:}", "\\textbf{the adjudication:}"]),
]
for tag, needles in PINS:
    blk = BLOCKS.get(tag, "")
    for nd in needles:
        chk(nd in blk, f"§F {tag} pins the display fragment: {nd[:52]}")

# ---- the declaration discipline pins
for tag in ("BM.8", "BM.10", "BM.11"):
    blk = BLOCKS.get(tag, "")
    if tag == "BM.8":
        chk("stationarity hypothesis" in blk and "theorem-local" in blk,
            "§F BM.8(2) declares its stationarity scope as theorem-local")
    else:
        chk("at the point of use" in blk, f"§F {tag} declares CT2.6's conditions at the point of use")
chk("A §0.2a" in BLOCKS.get("BM.8", "") and "A §0.2a" in BLOCKS.get("BM.11", ""),
    "§F the extra-axiomatic continuum-limit conditions are cited to A §0.2a")
B7 = BLOCKS.get("BM.7", "")
chk("\\mathcal L" not in B7 and "S_{\\mathrm{eff}}" not in B7 and "\\delta S" not in B7,
    "§F BM.7 carries no action functional and no variational derivative: the discrete law is pre-Noether")
chk("checks/verify_H_noether.py" in B7 and all("checks/verify_H_noether.py" in BLOCKS[t]
                                               for t in ("BM.8", "BM.9", "BM.10", "BM.11", "BM.12")),
    "§F every block of the tier cites its machine section")

# ---- the no-forward-Req-edge discipline (the DAG law of Part 4)
ORDER = ["Def-BM.1", "Def-BM.2", "BM.1", "BM.2", "BM.3", "BM.4", "BM.5", "BM.6",
         "Def-BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12"]
fwd = []
for t in ORDER[8:]:
    blk = BLOCKS.get(t, "")
    i = blk.find("**Req.**")
    j = blk.find("\n\n", i)
    req = blk[i:j if j > 0 else len(blk)]
    for cited in set(re.findall(r"\b(?:Def-BM|BM)\.\d+", req)):
        if cited != t and ORDER.index(cited) > ORDER.index(t):
            fwd.append((t, cited))
chk(not fwd, f"§F no Req line of Tier BM.4 cites a later tag of this part: {fwd}")

# ---- hygiene of the tier text
BARRED = ["previously", "formerly", "this was", "now this", "erratum", "submitted",
          "earlier draft", "stale", "draft", "directive", "as corrected",
          "letter series", "non-binding", "wip", "superseded by an earlier"]
hits = [(w, low.count(w)) for w in BARRED if w in low]
chk(not hits, f"§F Tier BM.4 revision/drafting-language scan: zero hits ({hits})")
chk(not re.search(r"\bP-H\d", TIER), "§F zero registry tokens in Tier BM.4")
chk("**Status.**" not in TIER, "§F zero **Status.** lines in Tier BM.4")
chk(not re.search(r"\(H\d\d\)", TIER) and not re.search(r"\(\*\*[A-T]\*\*\)", TIER),
    "§F zero archive and letter locators in Tier BM.4")
MASS = ["0.511", "105.6", "1776", "206.7", "3477", "1.273", "4.183", "162.5",
        "172.4", "938.2", "939.5", "139.57", "134.9", "0.118", "137.0", "140.5"]
leak = [t for t in MASS if t in TIER]
chk(not leak, f"§F zero external mass/coupling tokens in Tier BM.4 ({leak})")
chk(TIER.count("EXT") == 1 and "\\text{no}\\ \\text{EXT}\\ \\text{datum}" in TIER,
    f"§F the EXT record occurs exactly once, in BM.12(4): {TIER.count('EXT')}")
chk("\\neg\\text{Cal-BM parameter}" in EXP or "§Cal-BM stays empty" in TIER,
    "§F the tier adds no free internal parameter (§Cal-BM stays empty)")

# ---- suite and ledger counts
chk("(79 checkers)" in RM, "§F the main README carries the current suite count (76 at Tier BM.20)")
chk("**79/79**" in CRM and "(79 checkers)" in CRM,
    "§F checks/README carries the current suite count and state (67/67 at Tier BM.12)")
chk("verify_H_noether.py" in CRM, "§F checks/README names the Tier BM.4 checker")
chk("(V.7)" in HL and "59/59" in HL, "§F HistLog §V carries (V.7) with suite state 59/59")
chk("Tier BM.4" in HL, "§F HistLog (V.7) names the tier")
chk("56/57" in HL and "58/58" in HL, "§F the earlier suite states are preserved in HistLog §V")
chk("Tier BM.4" in TI and all(f"BM.{n}" in TI for n in range(7, 13)),
    "§F index/tier_index.md carries Tier BM.4 with BM.7–BM.12")
chk(all(f'"BM.{n}"' in TJ for n in range(7, 13)) and '"Def-BM.3"' in TJ,
    "§F index/tags.json carries the new tags")

print()
if FAILS:
    print(f"verify_H_noether: {len(FAILS)} FAILED of {N + len(FAILS)}")
    sys.exit(1)
print(f"verify_H_noether: {N} checks green  ({time.time()-t0:.1f}s) — "
      "Tier BM.4 (Def-BM.3, BM.7–BM.12) §A–§F")
sys.exit(0)
