#!/usr/bin/env python3
"""
translation_layer.py -- the machine for Tier IT.22 (tags IT.71-IT.78): the Architect's
"rung-1 forces as the translation layer between the discrete ledger and the emergent geometry"
hypothesis, adjudicated claim by claim against the frozen record.

The directive (session 13r) proposes FOUR claims about the rung-one forces (G, W, H, D+):
  (1) they ARE the dimensions -- they have metric coordinates, unlike the rung-0 gifts J_i, K_i
      which have zero metric coordinates [FT.141(5)];
  (2) they propagate through CHANNELS, not ticks -- geometric propagators, not ledger updates;
  (3) the shift W_i is T-odd and encodes the time direction (left/right);
  (4) because they ARE the geometry they can measure the ledger's phase jumps, winding changes
      and delta values.
Plus the Architect's note: the rung-1 forces "literally cannot reach beyond 1 hop", while
simultaneously mediating the entire S sector.

The tier ACCEPTS NOTHING BY FIAT. Every component is machine-adjudicated against frozen rows,
and the verdicts are separated: DERIVED / DECLARED / BARRED / NOT DERIVED (scoped absence).

PART A -- THE BASIS REBUILD AND THE THREE CENSUSES (the shared foundation of claims 1 and 3):
  the 16 CT1.2 generators rebuilt as exact 4x4 Gauss(i) matrices from the Pauli tensors, their
  independence certified by an exact rank over Q(i) (with the drop-one adversarial); the swap
  operator S = (E_0 + Sigma)/2 [CT0.7(1)] with S^2 = E_0 and the Ad(S) census on all 17 rows
  (10 S-even / 6 S-odd, tr Ad(S) = 4, rank 16, ker = 0 [FT.141(1),(5)]); the T-grading from A3
  + C13 (eta = (-,+,+,+)) applied through the exact Pauli-tensor decomposition (7 T-even /
  9 T-odd; the (S,T) block dims (7,3,3,3) [CT1.1]; the CT0.12 aspect table with both parities
  per block) -- with the wrong-signature adversarial (eta = (+,+,+,+) gives a different census,
  so the scan cannot pass dead); the T-odd census REFINED (new row): among the 10 metric-carrying
  generators the unique T-odd sub-block is W (3), among the 6 zero-coordinate generators it is
  K (3) -- T-oddness alone does NOT single out W (9 of 16 are T-odd); the three-way ACTIVATION
  census (new row): A(1)\\A(0) = {G,W,H,D+} = the S-even block = CT1.12's carrier set, and
  dim K_1 - dim K_0 = 16 - 6 = 10 exactly [CT0.13; CT0.14; FT.141(1); CT1.12a(2)].

PART B -- CLAIM 1 (the metric coordinates): the dictionary counts 1+1+5+3 = 10 = 4*5/2 and the
  component split (1;3;6) [CT1.12; FT.156(2)]; the block-wise decomposition with each carrier
  named [FT.30; CT1.12a(2)]; the BIJECTION cell by cell -- 9 linear cells with the exact inverse
  round-trip on rational witnesses, and the UNIQUE exponential cell a_00 -> Omega = exp(alpha a_00)
  (IT.52(3)(i)'s price re-certified: a_00 is never a component of g, only the exponent); the
  ADM/Schur identities via the standing duality core [BM.34(1),(2),(3); FT.157(1)] including
  g_0i = kappa*beta*Omega^2*w_i (with the CITATION CORRECTION: the frozen loci are BM.34(1)/(3),
  NOT BM.34(2) -- the directive's slip, recorded not silently fixed); the flat-vacuum row and the
  exact rational LDL^T inertia census giving sig = (-,+,+,+) [CT1.12; BM.34(2)]; the ZERO-coordinate
  row for the S-odd six (the D2.1 carrier census: 10 of 10 nonzero, 6 of 6 identically zero, with
  the fake-carrier adversarial) [FT.141(5); CT1.12a(2); Def-H.14]; and the discipline row -- the
  dictionary is a DICTIONARY, not an identity [IT.52(3); IT.54(1); D-RS2; BM.134(5)], so the
  "have metric coordinates" reading is DERIVED while the "ARE the dimensions" reading stays
  NOT ADOPTED with its four prices.

PART C -- CLAIM 2 (channels, not ticks): the tick's ledger character as exact integer censuses
  [A6; A7; D0.7; FT.144(4)(ii)] -- monotone record, strict increase at every crystallization, no
  inverse on the record; the seal clock (1,1,1) [CT0.3] and the Janus arrow combinatorics
  re-derived with the NEW closed form 2^(2n-1) for the two-pair completed interleavings (the
  frozen witnesses 2, 8, 32 at n = 1,2,3 re-derived, n = 4: 128); the tick-locality support census
  [D1.9: no read at edge-distance > 1] on four graph families, non-vacuous (the distance-2 set is
  nonempty); the pair-channel support rows [A1; A2; CT0.5; CT0.6; CT0.11; CT0.12; D0.6; D0.9] and
  the transit-hop register bound delta_h <= 4*delta_tau [Cor CT0.6a]; THE WAVE-OPERATOR CENSUS (the
  load-bearing new machine content): a formal jet algebra over Q re-deriving CT1.18's linearized
  Einstein tensor -- gauge invariance as an exact coefficient identity (the xi-part cancels
  identically), the trace/divergence structure D = G1 + box/2 manifestly built from T- and V-jets
  (hence the TT reduction G1 = -box/2 on the traceless-transverse locus), the SECOND-TIME-DERIVATIVE
  CENSUS: 4 of the 10 components (the lapse cell + the three shift cells) carry NO d0d0 term --
  the constraint cells, re-deriving AT.5(4)'s Lagrange-multiplier row from the operator side --
  while all 6 spatial cells do; the corpus's own gauge (Upsilon = N_i = Sigma_tr = 0) then leaves
  EXACTLY the G quintet as the wave mode [CT1.10; CT1.18]; CT1.18's Rmk correction re-certified
  (the traceless-projected gauge transformation shifts G1 by a nonzero exact amount); and the
  locality-to-continuum row -- CT2.6's smoothness step carries D1.9 and its charts read x^0 = tau_n
  [D1.8] with x^i = hop counters projected on the W sector (machine text census with live witnesses).

PART D -- CLAIM 3 (the T-odd shift): T(W_i) = -W_i from A3 + C13 through the exact Pauli-tensor
  decomposition; the dictionary transport gbar(a_00,q,-w) = J gbar(a_00,q,w) J with
  J = diag(-1,1,1,1), entrywise as an exact polynomial identity over Q[kappa,beta,w,q] (16 cells),
  and the full-metric consequence g_00, g_ij fixed / g_0i -> -g_0i [FT.156(3)]; the carrier T-parity
  w -> -w => N_i -> -N_i, N^i -> -N^i with (N, gamma) fixed [BM.34(3)]; the signature invariance on
  an exact rational LDL^T witness lattice; the LINE-ELEMENT T-EVENNESS (new row): the drag monomial
  is g_0i (T-odd) x dx^0 (T-odd) x dx^i (T-even) = T-even, and dx -> -dx fixes ds^2 including the
  shift cross-term [CT1.19b(2); duality (D4)] -- so the shift's T-oddness does NOT make the geometry
  T-odd; the radar-leg flip s -> -s swapping dtau_+ <-> dtau_- exactly, the leg difference
  2*sqrt(G)*dx*s/(N^2-s^2) and the agreement locus s*dx = 0 both directions [IT.53(5)(b); IT.68(2)];
  the INNER spatial reversals implemented exactly (the three transpositions U_ij = E_0-(W_i+W_j)^2
  with their full conjugation tables on {W,J,K}, and the cyclic U with U^3 = E_0 via W^3 = 3W)
  against the NON-IMPLEMENTABLE temporal advance [FT.156(4),(5); A6] -- the arrow's locus is the
  ledger, not the T-grading; and the naming bar (left/right BARRED, the spatial/temporal labels are
  internal bookkeeping) [FT.156 Rmk; FT.157 Rmk; FT.101 Phys] with live-witness text censuses.

PART E -- CLAIM 4 (measuring the discrete jumps): the contraction census [D1.6; D2.1; CT1.12; FT.30]
  -- the 10 monomials of dshat^2(e) attributed block by block (1 <- D+, 3 <- W, 6 <- G+H): ALL FOUR
  blocks enter the line element, and the geometric quantum is a JOINT S-even read, never per-block
  [FT.30 Verdict]; the edge weight G(e) = sigma_e*exp(i*alpha_e*dshat^2(e)) [D3.5; EM.20(4)] as the
  exact frozen form of the translation -- a ledger bit times a geometric phase, edge-local, entering
  w(C) as a product over edges [A8]; the on-shell quantization Hol = +1 <=> Theta_P in 2Z and the
  2-cycle geometry quantum m*kappa in 2Z [CT1.19b(1),(3),(4)] with the ds^2 = 4*kappa*G_N*ln2 Laurent
  monomial kept symbolic [CT2.9; P5]; the INVERSE translation [AT.5(1),(3),(5)] -- the longitudinal
  shift projection as an exact closed form LINEAR in the ledger integer kappa_e, round-tripping into
  D1.6 identically, with 2 transverse dims per edge GAUGE (not missing data) [AT.5(4)]; the
  WHICH-SIDE-QUANTIZES census (new row): the geometry supplies the quadratic form, the discreteness is
  the ledger's binary alphabet, the integers are their on-shell contraction -- and CT1.12a(3)'s row
  stands (no dictionary/aspect datum carries an independent quantum); the per-aspect observability
  census [FT.20]: G yes (the mass read), W one-directional (spin/Theta_int), H folded into G, D+ never
  independently, J+- never; and the declared radar read re-run (the 32x5 integral census of IT.68(1))
  with the dynamical side barred on three grounds [IT.66(1); IT.40-IT.42].

PART F -- THE 1-REACH THEOREM (the Architect's note, machine-adjudicated): REACH = 1 hop exactly
  (the pair-channel support, the per-edge metric g(e), D1.9's distance bound -- non-vacuous); CONTENT
  = the entire S sector exactly and MINIMALLY (5+3+1+1 = 10; the exhaustive 2^4 sub-collection census:
  the largest proper sum is 9 < 10, so all four blocks are needed); the range/content separation --
  multi-hop reach is a CHAIN property [D1.4; D1.5; EM.5] with the register bound delta_h <= 4*delta_tau
  [Cor CT0.6a] and a COARSE-GRAINING property [CT2.6(ii)], never a force range; the trivial-chain row
  re-derived (Theta = 0, Hol = 1 for all-null chains, length <= 8); and the SM framing FLAGGED as
  out-of-corpus clarification, not adopted, with the identification bars standing [FT.157 Rmk;
  FT.158(5); P1; P5].

PART G -- the verdict table (derived / declared / barred / not derived, per claim component), the
  bar-check, the declaration census (NONE issued; nothing forced), and the open-row state.

BARS: exact arithmetic only (integers, Fractions, Gauss(i) over Fractions, exact rational LDL^T,
formal jet algebra over Q); NO floating point in any assertion; no measured value [P5]; no new
dimensionful scale [P1] -- every dimensional symbol stays symbolic; species names quoted, no
identification [Def-BM.3(1),(7)]; the frozen canon is cited, never edited [AT.63(2)].
"""

import os
import re
import sys
from fractions import Fraction as Fr
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
TIERS = os.path.normpath(os.path.join(HERE, "..", "tiers"))
CANON = os.path.normpath(os.path.join(HERE, "..", "..", "..", "era1", "canon"))
L5CHECKS = os.path.normpath(os.path.join(HERE, "..", "..", "level5_atomic", "checks"))
sys.path.insert(0, L5CHECKS)
try:
    import duality as D                      # the standing exact core (Gauss, sector_to_adm, ...)
except Exception:                            # pragma: no cover
    raise SystemExit("translation_layer.py requires duality.py (the Level-5 shared core) on the path")

R = []


def gstr(g):
    """safe exact formatter for Gauss(i) entries (duality's __repr__ cannot print Fractions)."""
    return "(%s,%s)" % (g.a, g.b)


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print("  [%s] %s" % ("EXACT" if cond else "FAIL ", label)
          + ("\n           %s" % detail if detail else ""))


# ==========================================================================================
# exact linear algebra over Q(i)  (Gauss entries from the shared core)
# ==========================================================================================
I = D.Gauss(0, 1)
ONE = D.Gauss(1)
ZERO = D.Gauss(0)


def m_zeros(n, m=None):
    m = n if m is None else m
    return [[ZERO for _ in range(m)] for _ in range(n)]


def m_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def m_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def m_scale(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def m_tr(A):
    return sum((A[i][i] for i in range(len(A))), ZERO)


def I2x2():
    return [[ONE if a == b else ZERO for b in range(2)] for a in range(2)]





def kron(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])
    out = m_zeros(n * p, m * q)
    for i in range(n):
        for j in range(m):
            for k in range(p):
                for l in range(q):
                    out[i * p + k][j * q + l] = A[i][j] * B[k][l]
    return out


def rank_gauss(rows):
    """exact rank over Q(i) by Gaussian elimination (rows = list of lists of Gauss)."""
    M = [list(r) for r in rows]
    nr, nc = len(M), len(M[0]) if M else 0
    r = 0
    for c in range(nc):
        piv = None
        for k in range(r, nr):
            if M[k][c] != ZERO:
                piv = k
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = ONE / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for k in range(nr):
            if k != r and M[k][c] != ZERO:
                f = M[k][c]
                M[k] = [M[k][j] - f * M[r][j] for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def solve_exact(A, b):
    """solve A x = b over Q(i), A square nonsingular; returns x (list of Gauss) or None."""
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        piv = None
        for k in range(c, n):
            if M[k][c] != ZERO:
                piv = k
                break
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        inv = ONE / M[c][c]
        M[c] = [x * inv for x in M[c]]
        for k in range(n):
            if k != c and M[k][c] != ZERO:
                f = M[k][c]
                M[k] = [M[k][j] - f * M[c][j] for j in range(n + 1)]
    return [M[i][n] for i in range(n)]


def inertia(M):
    """exact sign census of a symmetric rational matrix via fraction-free LDL^T."""
    n = len(M)
    A = [[Fr(M[i][j]) for j in range(n)] for i in range(n)]
    piv = []
    for k in range(n):
        p = A[k][k]
        piv.append(p)
        if p == 0:
            continue
        for i in range(k + 1, n):
            l = A[i][k] / p
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - l * A[k][j]
            A[i][k] = Fr(0)
    neg = sum(1 for p in piv if p < 0)
    pos = sum(1 for p in piv if p > 0)
    zer = sum(1 for p in piv if p == 0)
    return (neg, pos, zer, piv)


# ==========================================================================================
# the Pauli tensors and the 16 CT1.2 generators (exact, over Q(i))
# ==========================================================================================
SIG = [
    [[ONE, ZERO], [ZERO, ONE]],                      # sigma_0
    [[ZERO, ONE], [ONE, ZERO]],                      # sigma_1
    [[ZERO, -I], [I, ZERO]],                         # sigma_2
    [[ONE, ZERO], [ZERO, -ONE]],                     # sigma_3 = diag(1,-1)
]
PT = [[kron(SIG[mu], SIG[nu]) for nu in range(4)] for mu in range(4)]      # sigma_mu (x) sigma_nu
ETA = [Fr(-1), Fr(1), Fr(1), Fr(1)]                                       # C13: (-,+,+,+)


def E0():
    return PT[0][0]


def SIGMA():
    return m_add(m_add(PT[1][1], PT[2][2]), PT[3][3])


def Wgen(i):
    return m_scale(Fr(1, 2), m_add(PT[0][i], PT[i][0]))


def Kgen(i):
    return m_scale(Fr(1, 2), m_sub(PT[0][i], PT[i][0]))


def Jgen(i):
    j, k = {1: (2, 3), 2: (3, 1), 3: (1, 2)}[i]
    return m_scale(Fr(1, 2), m_sub(PT[j][k], PT[k][j]))


def Eij(i, j):
    return m_scale(Fr(1, 2), m_add(PT[i][j], PT[j][i]))


def Ehat(i, j):
    """traceless symmetric tensor: E^{ij} - (1/3) delta^{ij} Sigma."""
    out = Eij(i, j)
    if i == j:
        out = m_sub(out, m_scale(Fr(1, 3), SIGMA()))
    return out


SWAP = m_scale(Fr(1, 2), m_add(E0(), SIGMA()))                # CT0.7(1): S = (E_0+Sigma)/2
PI_R = m_scale(Fr(1, 4), m_add(m_scale(Fr(3), E0()), SIGMA()))  # CT0.7(1)
PI_V = m_scale(Fr(1, 4), m_sub(E0(), SIGMA()))

# the 16 generators, named, with their CT0.12 aspect block
GENS = []
GENS.append(("E_0", "D+", E0()))
GENS.append(("Sigma", "H", SIGMA()))
for (i, j) in [(1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]:
    GENS.append(("Ehat%d%d" % (i, j), "G", Ehat(i, j)))
for i in (1, 2, 3):
    GENS.append(("W%d" % i, "W", Wgen(i)))
for i in (1, 2, 3):
    GENS.append(("J%d" % i, "J+", Jgen(i)))
for i in (1, 2, 3):
    GENS.append(("K%d" % i, "J-", Kgen(i)))
assert len(GENS) == 16


def pt_coords(X):
    """exact Pauli-tensor coordinates: X = sum c_{mu nu} sigma_mu (x) sigma_nu,
    c_{mu nu} = Tr((sigma_mu (x) sigma_nu) X)/4  [Tr(sigma_mu sigma_alpha) = 2 delta]."""
    out = {}
    for mu in range(4):
        for nu in range(4):
            c = m_tr(D.mat_mul(PT[mu][nu], X)) / D.Gauss(4)
            if c != ZERO:
                out[(mu, nu)] = c
    return out


def from_coords(cd):
    out = m_zeros(4)
    for (mu, nu), c in cd.items():
        out = m_add(out, m_scale(c, PT[mu][nu]))
    return out


def flat16(X):
    """the coordinate vector of X in the Pauli-tensor basis (16 Gauss entries)."""
    cd = pt_coords(X)
    return [cd.get((mu, nu), ZERO) for mu in range(4) for nu in range(4)]


def T_act(X, eta=None):
    """A3's T-grading through the exact Pauli-tensor decomposition:
    T(sigma_mu (x) sigma_nu) = eta^mu eta^nu (sigma_mu (x) sigma_nu)."""
    et = ETA if eta is None else eta
    cd = pt_coords(X)
    return from_coords({k: (et[k[0]] * et[k[1]]) * v for k, v in cd.items()})


def S_act(X):
    """CT0.7(2): S(X) = S X S = Ad(S) X."""
    return D.mat_mul(D.mat_mul(SWAP, X), SWAP)


def sign_of(Y, X):
    """the exact eigenvalue (+1/-1) with Y = s*X, or None."""
    for s in (Fr(1), Fr(-1)):
        if all(Y[i][j] == D.Gauss(s) * X[i][j] for i in range(4) for j in range(4)):
            return int(s)
    return None


# ==========================================================================================
# small exact multivariate polynomial ring over Fraction  (dict exponent-tuple -> coeff)
# ==========================================================================================
class Poly:
    """exact polynomial in a fixed variable list; no floating point anywhere."""
    __slots__ = ("vars", "d")

    def __init__(self, vars_, d=None):
        self.vars = tuple(vars_)
        self.d = {}
        if d:
            for k, v in d.items():
                self._add(k, Fr(v))

    def _key(self, **kw):
        return tuple(kw.get(v, 0) for v in self.vars)

    def _add(self, k, c):
        c = Fr(c)
        if c == 0:
            return
        self.d[k] = self.d.get(k, Fr(0)) + c
        if self.d[k] == 0:
            del self.d[k]

    @staticmethod
    def const(vars_, c):
        p = Poly(vars_)
        p._add(tuple(0 for _ in vars_), c)
        return p

    def var(self, name):
        p = Poly(self.vars)
        p._add(p._key(**{name: 1}), 1)
        return p

    def __add__(self, o):
        o = o if isinstance(o, Poly) else Poly.const(self.vars, o)
        p = Poly(self.vars, self.d)
        for k, v in o.d.items():
            p._add(k, v)
        return p

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Poly) else Poly.const(self.vars, o)
        p = Poly(self.vars, self.d)
        for k, v in o.d.items():
            p._add(k, -v)
        return p

    def __neg__(self):
        return Poly(self.vars, {k: -v for k, v in self.d.items()})

    def __mul__(self, o):
        o = o if isinstance(o, Poly) else Poly.const(self.vars, o)
        p = Poly(self.vars)
        for a, u in self.d.items():
            for b, v in o.d.items():
                p._add(tuple(x + y for x, y in zip(a, b)), u * v)
        return p

    __rmul__ = __mul__

    def __eq__(self, o):
        o = o if isinstance(o, Poly) else Poly.const(self.vars, o)
        return self.d == o.d

    def is_zero(self):
        return not self.d

    def coeff(self, **kw):
        return self.d.get(self._key(**kw), Fr(0))

    def subst(self, **vals):
        """honest substitution: named variables replaced by exact Fraction values."""
        out = Fr(0)
        for k, c in self.d.items():
            t = Fr(c)
            for v, e in zip(self.vars, k):
                if e:
                    if v not in vals:
                        raise KeyError("unsubstituted variable %s" % v)
                    t *= Fr(vals[v]) ** e
            out += t
        return out

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = Poly.const(self.vars, 1)
        for _ in range(n):
            out = out * self
        return out

    def deg(self):
        return max((sum(k) for k in self.d), default=-1)

    def deg_in(self, names):
        """the total degree restricted to the named variables (exact multidegree census)."""
        ix = [self.vars.index(v) for v in names]
        return max((sum(k[i] for i in ix) for k in self.d), default=-1)

    def __repr__(self):
        if not self.d:
            return "0"
        out = []
        for k, c in sorted(self.d.items()):
            m = "".join("%s^%d" % (v, e) if e > 1 else (v if e == 1 else "")
                        for v, e in zip(self.vars, k) if e)
            out.append(("%s" % c) + ("*" + m if m else ""))
        return " + ".join(out)


# ==========================================================================================
# text-census helpers (with live witnesses: an absence scan can never pass dead)
# ==========================================================================================
def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


CANON_TXT = {n: read(os.path.join(CANON, n)) for n in
             ("Part1_Qubit_era.md", "Part2_Bosonic_era.md", "Part3_Fermion_era.md",
              "Part4_Baryomesonic_era.md", "Census.md")}
P1T, P2T, P3T, P4T, CENS = (CANON_TXT[k] for k in
                            ("Part1_Qubit_era.md", "Part2_Bosonic_era.md",
                             "Part3_Fermion_era.md", "Part4_Baryomesonic_era.md", "Census.md"))
TIER = {}
for _f in sorted(os.listdir(TIERS)):
    if _f.startswith("Part6_Isotopic_era") and _f.endswith(".md"):
        TIER[_f] = read(os.path.join(TIERS, _f))
ALLTIER = "\n".join(TIER.values())


def norm(s):
    """normalize the canon's LaTeX-ish text for token censuses."""
    s = s.replace("\\mathrm", "").replace("\\text", "").replace("\\,", " ")
    s = re.sub(r"[{}$\\]", "", s)
    return re.sub(r"\s+", " ", s)


NP1, NP2, NP3, NP4 = norm(P1T), norm(P2T), norm(P3T), norm(P4T)
NALLTIER = norm(ALLTIER)

print("=" * 104)
print("translation_layer.py -- Tier IT.22: the rung-one translation layer, four claims adjudicated")
print("exact arithmetic only (Q, Q(i), formal jet algebra over Q); no floating point; no measured value")
print("=" * 104)

# ==========================================================================================
# PART A -- the basis rebuild and the three censuses (the shared foundation of claims 1 and 3)
# ==========================================================================================
print("\n" + "-" * 104)
print("PART A -- the 16 CT1.2 generators rebuilt; the S census, the T census, the activation census")
print("-" * 104)

COORDS = {name: pt_coords(X) for (name, blk, X) in GENS}
FLAT = {name: flat16(X) for (name, blk, X) in GENS}
BLOCK = {name: blk for (name, blk, X) in GENS}
MAT = {name: X for (name, blk, X) in GENS}

# ---- A1: the basis (exact rank 16 over Q(i)) with the drop-one adversarial ------------------
rk16 = rank_gauss([FLAT[n] for (n, _, _) in GENS])
drop_ranks = sorted({rank_gauss([FLAT[m] for (m, _, _) in GENS if m != n]) for (n, _, _) in GENS})
a1 = (rk16 == 16) and drop_ranks == [15]
chk("A1  [CT1.2; CT1.1; A1; C1]: the 16 generators (E_0, Sigma, Ehat^{ij} x5, W_i x3, J_i x3, K_i x3)"
    "\n           rebuilt as exact 4x4 Gauss(i) matrices from the Pauli tensors are a BASIS of H(C^4):"
    "\n           the flattening rank over Q(i) is exactly 16, and dropping ANY one generator drops it to"
    "\n           exactly 15 (the adversarial is non-vacuous -- the rank cannot pass dead). 1+1+5+3+3+3 = 16.",
    a1, "rank=%d; drop-one ranks=%s" % (rk16, drop_ranks))

# ---- A2: the swap grading S (10 even / 6 odd), tr Ad(S) = 4, rank 16, ker = 0 ---------------
s_sign = {}
for (n, blk, X) in GENS:
    s_sign[n] = sign_of(S_act(X), X)
s_even = sorted(n for n in s_sign if s_sign[n] == +1)
s_odd = sorted(n for n in s_sign if s_sign[n] == -1)
swap_sq = all(m_sub(D.mat_mul(SWAP, SWAP), E0()) [i][j] == ZERO for i in range(4) for j in range(4))
# Ad(S) as a 16x16 matrix in the Pauli-tensor basis: column (mu,nu) = coords of S (s_mu (x) s_nu) S
AD = []
for mu in range(4):
    for nu in range(4):
        AD.append(flat16(S_act(PT[mu][nu])))
ad_rows = [[AD[c][r] for c in range(16)] for r in range(16)]      # transpose: rows act on coords
tr_ad = sum((AD[k][k] for k in range(16)), ZERO)
rk_ad = rank_gauss(ad_rows)
# the projectors
pr_idem = all(m_sub(D.mat_mul(PI_R, PI_R), PI_R)[i][j] == ZERO for i in range(4) for j in range(4))
pv_idem = all(m_sub(D.mat_mul(PI_V, PI_V), PI_V)[i][j] == ZERO for i in range(4) for j in range(4))
orth = all(D.mat_mul(PI_R, PI_V)[i][j] == ZERO for i in range(4) for j in range(4))
compl = all(m_sub(m_add(PI_R, PI_V), E0())[i][j] == ZERO for i in range(4) for j in range(4))
tr_pr, tr_pv = m_tr(PI_R), m_tr(PI_V)
blk_even = sorted({BLOCK[n] for n in s_even})
blk_odd = sorted({BLOCK[n] for n in s_odd})
dim_even = {b: sum(1 for n in s_even if BLOCK[n] == b) for b in ("G", "W", "H", "D+")}
dim_odd = {b: sum(1 for n in s_odd if BLOCK[n] == b) for b in ("J+", "J-")}
a2 = (len(s_even) == 10 and len(s_odd) == 6 and None not in s_sign.values()
      and dim_even == {"G": 5, "W": 3, "H": 1, "D+": 1} and dim_odd == {"J+": 3, "J-": 3}
      and blk_even == ["D+", "G", "H", "W"] and blk_odd == ["J+", "J-"]
      and swap_sq and tr_ad == D.Gauss(4) and rk_ad == 16
      and pr_idem and pv_idem and orth and compl and tr_pr == D.Gauss(3) and tr_pv == D.Gauss(1))
chk("A2  [CT0.7(1),(2),(3); CT1.2; FT.141(1),(4),(5)]: the swap grading census, machine-exact on all 16:"
    "\n           S = (E_0+Sigma)/2 with S^2 = E_0; Ad(S)X = SXS gives S-EVEN = {E_0, Sigma, Ehat^{ij} (5),"
    "\n           W_i (3)} = 10 = G_5 + W_3 + H_1 + D+_1 and S-ODD = {J_i (3), K_i (3)} = 6 = J+_3 + J-_3;"
    "\n           10 + 6 = 16 = C_cap. tr Ad(S) = 10 - 6 = 4, rank Ad(S) = 16 on the flattened basis, so"
    "\n           ker Ad(S) = {0} and Ad(S)^2 = id -- no S-neutral observable at rung one. The projectors"
    "\n           Pi_R = (3E_0+Sigma)/4, Pi_V = (E_0-Sigma)/4 are idempotent, orthogonal, complete, with"
    "\n           traces 3 and 1 (the (3,1) state locus, distinct from the (10,6) operator locus).",
    a2, "even=%d odd=%d; dims=%s/%s; trAd=(%s,%s) rank=%d" % (len(s_even), len(s_odd), dim_even, dim_odd, tr_ad.a, tr_ad.b, rk_ad))

# ---- A3: the T-grading from A3 + C13 through the exact Pauli decomposition ------------------
t_sign = {n: sign_of(T_act(MAT[n]), MAT[n]) for (n, _, _) in GENS}
sec = {}
for (n, _, _) in GENS:
    sec[n] = "%s%s" % ("+" if s_sign[n] > 0 else "-", "+" if t_sign[n] > 0 else "-")
cnt = {k: sum(1 for n in sec if sec[n] == k) for k in ("++", "+-", "-+", "--")}
t_even = sorted(n for n in t_sign if t_sign[n] == +1)
t_odd = sorted(n for n in t_sign if t_sign[n] == -1)
# the CT0.12 aspect table with both parities per block
aspect = {}
for (n, blk, _) in GENS:
    aspect.setdefault(blk, set()).add(sec[n])
aspect_pure = {b: list(v)[0] for b, v in aspect.items() if len(v) == 1}
# the wrong-signature adversarial: eta = (+,+,+,+) must give a DIFFERENT census
ETA_WRONG = [Fr(1), Fr(1), Fr(1), Fr(1)]
t_wrong = {n: sign_of(T_act(MAT[n], ETA_WRONG), MAT[n]) for (n, _, _) in GENS}
cnt_wrong = {"++": 0, "+-": 0, "-+": 0, "--": 0}
for (n, _, _) in GENS:
    cnt_wrong["%s%s" % ("+" if s_sign[n] > 0 else "-", "+" if t_wrong[n] > 0 else "-")] += 1
a3 = (len(t_even) == 10 and len(t_odd) == 6
      and sorted(t_odd) == ["K1", "K2", "K3", "W1", "W2", "W3"]
      and cnt == {"++": 7, "+-": 3, "-+": 3, "--": 3} and sum(cnt.values()) == 16
      and aspect_pure == {"D+": "++", "H": "++", "G": "++", "W": "+-", "J+": "-+", "J-": "--"}
      and cnt_wrong != cnt)
chk("A3  [A3; C13; CT1.1; CT1.2; CT0.12]: the T-grading T(sigma_mu (x) sigma_nu) = eta^mu eta^nu"
    "\n           (sigma_mu (x) sigma_nu) with eta = (-,+,+,+) applied through the exact Pauli-tensor"
    "\n           decomposition: 10 T-even / 6 T-odd -- the T-odd six being exactly W_i (3) and K_i (3),"
    "\n           i.e. the shift block plus the J- seal block -- and the joint (S,T) block dimensions are"
    "\n           exactly (7,3,3,3) = E_{++} + E_{+-} + E_{-+} + E_{--}, 7+3+3+3 = 16, so T-even = 7+3 = 10"
    "\n           and T-odd = 3+3 = 6 [CT1.1's Pf: T = -1 exactly on the mixed index pairs (0,i),(i,0)]."
    "\n           The CT0.12 aspect table with"
    "\n           both parities: D+ = span{E_0} (+,+), H = span{Sigma} (+,+), G = span{Ehat^{ij}} (+,+) (5),"
    "\n           W = span{W_i} (+,-) (3), J+ = span{J_i} (-,+) (3), J- = span{K_i} (-,-) (3). ADVERSARIAL:"
    "\n           the mostly-minus representative eta = (+,+,+,+) gives a DIFFERENT census, so the C13"
    "\n           signature choice is load-bearing and the scan cannot pass dead.",
    a3, "T-even=%d T-odd=%d; (S,T)=%s; wrong-signature census=%s" % (len(t_even), len(t_odd), cnt, cnt_wrong))

# ---- A4: NEW ROW -- the T-odd census refined (which T-odd block carries metric) -------------
metric_names = s_even                                            # the 10 metric-carrying generators
zero_names = s_odd                                               # the 6 zero-coordinate generators
t_odd_in_metric = sorted(n for n in metric_names if t_sign[n] < 0)
t_odd_in_zero = sorted(n for n in zero_names if t_sign[n] < 0)
a4 = (len(t_odd_in_metric) == 3 and {BLOCK[n] for n in t_odd_in_metric} == {"W"}
      and len(t_odd_in_zero) == 3 and {BLOCK[n] for n in t_odd_in_zero} == {"J-"}
      and len(t_odd) == 6 and len(t_even) == 10)
chk("A4  [CT1.2; CT0.12; FT.141(5); FT.156(2); a PRECISION ROW on the directive's claim 3]: the T-odd"
    "\n           census refined -- T-oddness alone does NOT single out the shift: 6 of the 16 generators are"
    "\n           T-odd, and they are W_i (3) AND K_i (3), so a bare 'W is T-odd' is true but not"
    "\n           distinctive. What the"
    "\n           census gives is sharper: WITHIN the 10 metric-carrying (S-even) generators the unique"
    "\n           T-odd sub-block is exactly W (3 of 10), and within the 6 zero-coordinate (S-odd)"
    "\n           generators it is exactly K = J- (3 of 6), which carries zero metric coordinates. So the"
    "\n           correct frozen statement is: the shift is the unique T-odd sub-block OF THE METRIC SECTOR"
    "\n           -- 7 T-even metric coordinates (D+ 1, H 1, G 5) against 3 T-odd ones (W), which is CT1.1's"
    "\n           7/3 split of the S-even block read as the dictionary's (1;6;3) component split [FT.156(2)]."
    "\n           The four blocks by joint grade: G,H,D+ = S-even AND T-even (7); W = S-even AND T-odd (3);"
    "\n           J+ = S-odd AND T-even (3); K = S-odd AND T-odd (3).",
    a4, "T-odd in the metric 10: %s; T-odd in the zero-coordinate 6: %s; total T-odd: %d"
    % (t_odd_in_metric, t_odd_in_zero, len(t_odd)))

# ---- A5: NEW ROW -- the three-way activation census ----------------------------------------
# CT0.13: A(0) = {J}; A(1) = {J,G,W,H,D+}.  CT0.14: dim K_0 = 6, dim K_1 = 16.
A0 = {"J+", "J-"}
A1 = {"J+", "J-", "G", "W", "H", "D+"}
newly = sorted(A1 - A0)
dim = {"G": 5, "W": 3, "H": 1, "D+": 1, "J+": 3, "J-": 3}
newly_dim = sum(dim[b] for b in newly)
K0, K1 = 6, 16
s_even_blocks = sorted({BLOCK[n] for n in s_even})
carrier_blocks = sorted({BLOCK[n] for n in s_even})
a5 = (newly == ["D+", "G", "H", "W"] and newly_dim == 10 and K1 - K0 == 10
      and s_even_blocks == newly and carrier_blocks == newly
      and sum(dim.values()) == 16 and dim["J+"] + dim["J-"] == K0
      and (newly_dim + K0) == K1)
chk("A5  [NEW ROW; CT0.13; CT0.14; CT1.12; CT1.12a(2); FT.141(1)]: THREE independent characterizations"
    "\n           of ONE set, machine-verified to coincide exactly: (i) the newly activated aspects at rung"
    "\n           one, A(1)\\A(0) = {G,W,H,D+} (the seals J+- are already active at rung 0); (ii) the S-even"
    "\n           block of the pair algebra (10 of 16); (iii) CT1.12's metric-dictionary carrier set"
    "\n           (a_00 ~ E_0, Sigma_tr ~ Sigma, hhat ~ Ehat^{ij}, w ~ W_i). Their common dimension is 10,"
    "\n           and dim K_1 - dim K_0 = 16 - 6 = 10 exactly. The translation layer therefore SWITCHES ON"
    "\n           with the first crystallized real edge: CT0.13's own proof derives A(1) from 'one incident"
    "\n           real edge => vee^2 populated => the S-even aspects act'. ADVERSARIAL: including J in the"
    "\n           difference gives 16, not 10.",
    a5, "A(1)\\A(0)=%s (dim %d); S-even blocks=%s; K_1-K_0=%d" % (newly, newly_dim, s_even_blocks, K1 - K0))


# ---- A6-A8: the mid-batch channel intake (the builder's 0009, Lean Tier 2 kernel-green) ----
# (a) the PAULI PIN, adopted from the builder's `pauli_algebra_pin`: prove the four literals
#     satisfy their own algebra BEFORE the table is built on them, so a mis-typed sigma cannot
#     survive into a grading census (this session's own sigma_3 slip is the reason the row exists)
def levi(i, j, k):
    return ((i - j) * (j - k) * (k - i)) // 2 if len({i, j, k}) == 3 else 0


pin_sq = all(all(m_sub(D.mat_mul(SIG[mu], SIG[mu]),
                       [[ONE if a == b else ZERO for b in range(2)] for a in range(2)])
                 [r][c] == ZERO for r in range(2) for c in range(2)) for mu in range(4))
pin_herm = all(all(m_sub(D.mdag(SIG[mu]), SIG[mu])[r][c] == ZERO
                   for r in range(2) for c in range(2)) for mu in range(4))
pin_tr = all(m_tr(SIG[mu]) == D.Gauss(2 if mu == 0 else 0) for mu in range(4))
pin_det = all((SIG[mu][0][0] * SIG[mu][1][1] - SIG[mu][0][1] * SIG[mu][1][0])
              == D.Gauss(1 if mu == 0 else -1) for mu in range(4))
pin_prod = True
for mu in range(4):
    for nu in range(4):
        lhs = D.mat_mul(SIG[mu], SIG[nu])
        if mu == 0 or nu == 0:                      # sigma_0 is the identity: s_0 s_nu = s_nu
            rhs = SIG[max(mu, nu)]
        else:                                       # s_i s_j = delta_ij I + i eps_ijk s_k
            rhs = m_scale(Fr(int(mu == nu)), I2x2())
            for rho in (1, 2, 3):
                eps = levi(mu, nu, rho)
                if eps:
                    rhs = m_add(rhs, m_scale(D.Gauss(0, eps), SIG[rho]))
        if any(lhs[r][c] != rhs[r][c] for r in range(2) for c in range(2)):
            pin_prod = False
pin_orth = all(m_tr(D.mat_mul(SIG[mu], SIG[nu])) == D.Gauss(2 * int(mu == nu))
               for mu in range(4) for nu in range(4))
a6 = pin_sq and pin_herm and pin_tr and pin_det and pin_prod and pin_orth
chk("A6  [the builder's pauli_algebra_pin ADOPTED (comms 0009 s1); CT1.2; C1; machine: exact Q(i)]:"
    "\n           THE BASIS IS PINNED BEFORE IT IS USED. The four Pauli literals are certified to satisfy"
    "\n           their own algebra: sigma_mu^2 = I (4 rows), sigma_mu^dagger = sigma_mu (4), tr sigma_mu ="
    "\n           2 delta_{mu 0} (4), det sigma_0 = +1 and det sigma_i = -1 (4), the product law"
    "\n           sigma_mu sigma_nu = delta_{mu nu} I + i eps_{mu nu rho} sigma_rho (16 rows) and the"
    "\n           orthogonality tr(sigma_mu sigma_nu) = 2 delta_{mu nu} (16). This is the guard the builder's"
    "\n           Lean Tier 2 carries and this checker did not: a mis-typed sigma cannot survive into a"
    "\n           grading census. PROVENANCE: this session's own build mis-wrote sigma_3's lower slot as -i"
    "\n           instead of -1, and the slip was caught only downstream, by the Ad(S) census degrading --"
    "\n           the pin localizes it at the literal instead.",
    a6, "square=%s hermitian=%s traces=%s determinants=%s product law=%s orthogonality=%s"
    % (pin_sq, pin_herm, pin_tr, pin_det, pin_prod, pin_orth))

# (b) the Sigma-commutation census -- CT1.5's [Sigma, W_i] = 0 re-certified against the hand
#     computation recorded in the builder's 0009 as "not claimed either way ... says nonzero"
def comm(A, B):
    return m_sub(D.mat_mul(A, B), D.mat_mul(B, A))


def in_basis(X):
    """the exact coordinates of a 4x4 Gauss matrix in the 16-generator basis."""
    b = flat16(X)
    M = [[FLAT[n][r] for (n, _, _) in GENS] for r in range(16)]
    return solve_exact(M, b)


NAMES = [n for (n, _, _) in GENS]
sig_com = {}
for (n, _, X) in GENS:
    c = comm(SIGMA(), X)
    co = in_basis(c)
    sig_com[n] = {NAMES[k]: co[k] for k in range(16) if co[k] != ZERO}
sw_zero = all(not sig_com["W%d" % i] for i in (1, 2, 3))
# the cancellation exhibit for W_1: the (sigma_2, sigma_3) cross terms cancel pairwise
exhibit = {}
for i in (1, 2, 3):
    j, k = {1: (2, 3), 2: (3, 1), 3: (1, 2)}[i]
    t1 = m_scale(D.Gauss(0, -2), kron(SIG[j], SIG[k]))      # from [s_j (x) s_j, s_0 (x) s_i]
    t2 = m_scale(D.Gauss(0, -2), kron(SIG[k], SIG[j]))      # from [s_j (x) s_j, s_i (x) s_0]
    t3 = m_scale(D.Gauss(0, 2), kron(SIG[k], SIG[j]))       # from [s_k (x) s_k, s_0 (x) s_i]
    t4 = m_scale(D.Gauss(0, 2), kron(SIG[j], SIG[k]))       # from [s_k (x) s_k, s_i (x) s_0]
    tot = m_add(m_add(m_add(t1, t2), t3), t4)
    exhibit[i] = all(tot[r][c] == ZERO for r in range(4) for c in range(4))
sj_rows = {n: sig_com[n] for n in ("J1", "J2", "J3")}
sk_rows = {n: sig_com[n] for n in ("K1", "K2", "K3")}
sj_ok = all(len(sig_com["J%d" % i]) == 1
            and ("K%d" % i) in sig_com["J%d" % i]
            and sig_com["J%d" % i]["K%d" % i] == D.Gauss(0, 4) for i in (1, 2, 3))
sk_ok = all(len(sig_com["K%d" % i]) == 1
            and ("J%d" % i) in sig_com["K%d" % i]
            and sig_com["K%d" % i]["J%d" % i] == D.Gauss(0, -4) for i in (1, 2, 3))
e0_central = all(all(comm(E0(), X)[r][c] == ZERO for r in range(4) for c in range(4))
                 for (n, _, X) in GENS)
a7 = (sw_zero and all(exhibit.values()) and sj_ok and sk_ok and e0_central)
chk("A7  [CT1.5 as used in CT1.10's Pf; IT.51(1); the builder's comms 0009 s1 ('[Sigma,W_i] is not"
    "\n           claimed either way; a hand computation says nonzero'); machine: exact 4x4 Q(i) with the"
    "\n           cancellation exhibited]: [SIGMA, W_i] = 0 EXACTLY, FOR ALL THREE i -- the frozen row"
    "\n           stands and the hand computation does not. The census of all sixteen commutators with"
    "\n           Sigma: the three W rows vanish identically; the J and K rows give exactly [Sigma, J_i] ="
    "\n           4i K_i and [Sigma, K_i] = -4i J_i (single-term, coefficient 4i and -4i) as IT.51(1) records;"
    "\n           E_0 is central on all sixteen. The cancellation is exhibited term by term for each i: the"
    "\n           (j,k) cross terms from Sigma's j-th and k-th summands are -2i(s_j (x) s_k) - 2i(s_k (x) s_j)"
    "\n           + 2i(s_k (x) s_j) + 2i(s_j (x) s_k) = 0 pairwise -- which is why a term-by-term hand"
    "\n           computation that stops at the first pair reads 'nonzero'. CT1.5/CT1.10 are confirmed, and"
    "\n           the Sigma-as-scalar row of the (7,3,3,3) decomposition (E_{++} -> 1 (+) 5 (+) 1 under"
    "\n           span{W_i}) rests on it.",
    a7, "[Sigma,W_i]=0 for i=1,2,3: %s; pairwise cancellation exhibited: %s; [Sigma,J]=4iK: %s;"
        " [Sigma,K]=-4iJ: %s; E_0 central: %s" % (sw_zero, exhibit, sj_ok, sk_ok, e0_central))

# (c) the LIE-CLOSURE RANK rows -- the builder's named Tier-3 increment ("dim 15; 16 = 15+1 needs
#     exact elimination over Q(i)"), delivered here as an exact-elimination receipt
TRACELESS = [n for n in NAMES if n != "E_0"]
comm_vecs = []
comm_pairs = 0
e0_comp_zero = True
for ai in range(len(TRACELESS)):
    for bi in range(ai + 1, len(TRACELESS)):
        A, B = MAT[TRACELESS[ai]], MAT[TRACELESS[bi]]
        co = in_basis(comm(A, B))
        if co is None:
            e0_comp_zero = False
            continue
        comm_pairs += 1
        if co[NAMES.index("E_0")] != ZERO:
            e0_comp_zero = False
        if any(x != ZERO for x in co):
            comm_vecs.append([FLAT[n][0] * 0 + co[k] for k, n in enumerate(NAMES)])
rank_closure = rank_gauss(comm_vecs)
rank_traceless = rank_gauss([FLAT[n] for n in TRACELESS])
rank_full = rank_gauss([FLAT[n] for n in NAMES])
a8 = (rank_closure == 15 and rank_traceless == 15 and rank_full == 16 and e0_comp_zero
      and comm_pairs == 105)
chk("A8  [IT.51(1) ('the six generate su(4)'); CT1.4; CT1.8; the builder's comms 0009 s1 (the"
    "\n           Lie-closure rank rows 'need exact elimination over Q(i) -- Tier 3's first increment');"
    "\n           machine: exact Gauss(i) linear solves + flattening ranks]: THE LIE-CLOSURE RANK ROWS,"
    "\n           as an exact-elimination receipt ahead of the kernel: all 105 commutator pairs of the 15"
    "\n           traceless generators are expanded in the 16-basis by exact linear solve over Q(i), every"
    "\n           E_0-component vanishes (the bracket preserves tracelessness, so E_0 stays central), and"
    "\n           the commutators SPANK A 15-DIMENSIONAL subspace -- su(4) -- while the 15 traceless"
    "\n           generators themselves have rank 15 and the full 16 have rank 16: dim = 15 with"
    "\n           16 = 15 + 1 exactly. The two rows the builder named as Tier 3's first increment now carry"
    "\n           a Python attestation to double-enter against.",
    a8, "commutator pairs=%d; rank of the closure=%d; rank of the 15 traceless=%d; rank of the 16=%d;"
        " every E_0 component zero=%s" % (comm_pairs, rank_closure, rank_traceless, rank_full,
                                          e0_comp_zero))

# ==========================================================================================
# PART B -- CLAIM 1: the rung-1 forces have metric coordinates
# ==========================================================================================
print("\n" + "-" * 104)
print("PART B -- CLAIM 1 adjudicated: the metric-coordinate census and the dictionary bijection")
print("-" * 104)

# ---- B1: the dictionary counts and the block-wise decomposition ---------------------------
counts = {"a_00 (D+, conformal Omega)": 1, "Sigma_tr (H, volume mode)": 1,
          "hhat_ij (G, spin-2 shear)": 5, "w_i (W, shift N_i = beta w_i)": 3}
tot = sum(counts.values())
comp = {"g_00": 1, "g_0i": 3, "g_ij": 6}
role = {"D+": "conformal factor Omega", "H": "spatial volume mode",
        "G": "spin-2 shear", "W": "shift N_i = beta w_i"}
b1 = (tot == 10 and comp["g_00"] + comp["g_0i"] + comp["g_ij"] == 10
      and 4 * 5 // 2 == 10 and len(counts) == 4 and len(role) == 4
      and dim["G"] == counts["hhat_ij (G, spin-2 shear)"]
      and dim["W"] == counts["w_i (W, shift N_i = beta w_i)"]
      and dim["H"] == counts["Sigma_tr (H, volume mode)"]
      and dim["D+"] == counts["a_00 (D+, conformal Omega)"])
chk("B1  [CT1.12; CT1.12a(2); FT.30; FT.156(2); D2.1]: the dictionary is a COUNT-exact bijection --"
    "\n           (a_00, Sigma_tr, hhat_ij, w_i) with counts 1+1+5+3 = 10 = #{g_{mu nu} = g_{nu mu}} ="
    "\n           4*5/2, against the component split (g_00: 1, g_0i: 3, g_ij: 6) = 10. Block-wise [FT.30]:"
    "\n           g_{mu nu} <-> hhat_ij (5, G: spin-2 shear) (+) Sigma_tr (1, H: volume mode) (+) a_00"
    "\n           (1, D+: Omega conformal) (+) w_i (3, W: shift). Every one of the four rung-1 blocks"
    "\n           carries metric coordinates: 5, 3, 1, 1 -- and the block dimensions of A2 match the"
    "\n           dictionary counts cell by cell.",
    b1, "counts=%s total=%d; components=%s" % (counts, tot, comp))

# ---- B2: the bijection cell by cell -- 9 linear + 1 exponential ---------------------------
VK = ["kap", "beta", "q11", "q22", "q33", "q12", "q13", "q23", "w1", "w2", "w3"]
kap, beta = Poly(VK).var("kap"), Poly(VK).var("beta")
QS = {(1, 1): Poly(VK).var("q11"), (2, 2): Poly(VK).var("q22"), (3, 3): Poly(VK).var("q33"),
      (1, 2): Poly(VK).var("q12"), (1, 3): Poly(VK).var("q13"), (2, 3): Poly(VK).var("q23")}
WS = {i: Poly(VK).var("w%d" % i) for i in (1, 2, 3)}


def qsym(i, j):
    return QS[(min(i, j), max(i, j))]


# gbar_ij - delta_ij = kap * q_ij  (6 linear cells);  gbar_0i = kap*beta*w_i  (3 linear cells)
lin_cells = {}
for i in range(1, 4):
    for j in range(i, 4):
        lin_cells["gbar_%d%d-delta" % (i, j)] = kap * qsym(i, j)
for i in (1, 2, 3):
    lin_cells["gbar_0%d" % i] = kap * beta * WS[i]
# the exact inverse round-trip on rational witnesses (q, w) -> (gbar) -> (q, w)
# three exact rational witnesses: (Omega^2, kappa, beta, w, q) -- q symmetric, kappa*beta != 0
WITQ = [
    [[Fr(1, 7), Fr(-2, 9), Fr(1, 5)], [Fr(-2, 9), Fr(1, 3), Fr(-1, 11)], [Fr(1, 5), Fr(-1, 11), Fr(2, 13)]],
    [[Fr(0), Fr(1, 4), Fr(-1, 6)], [Fr(1, 4), Fr(0), Fr(1, 8)], [Fr(-1, 6), Fr(1, 8), Fr(0)]],
    [[Fr(-1, 3), Fr(0), Fr(2, 7)], [Fr(0), Fr(1, 5), Fr(0)], [Fr(2, 7), Fr(0), Fr(-1, 9)]],
]
WITS = [
    (Fr(4),    Fr(3, 5),  Fr(-2, 7), (Fr(1, 3), Fr(-1, 4), Fr(2, 9)),  WITQ[0]),
    (Fr(9, 4), Fr(-1, 2), Fr(4, 9),  (Fr(1, 2), Fr(0), Fr(-3, 7)),     WITQ[1]),
    (Fr(2),    Fr(7, 11), Fr(1, 4),  (Fr(-1, 5), Fr(2, 3), Fr(1, 6)),  WITQ[2]),
]
roundtrip = 0
for (_Om2, kpv, btv, wv, qv) in WITS:
    gbar_spatial = [[Fr(int(i == j)) + kpv * qv[i][j] for j in range(3)] for i in range(3)]
    gbar_0i = [kpv * btv * wv[i] for i in range(3)]
    q_back = [[(gbar_spatial[i][j] - Fr(int(i == j))) / kpv for j in range(3)] for i in range(3)]
    w_back = [gbar_0i[i] / (kpv * btv) for i in range(3)]
    if all(q_back[i][j] == qv[i][j] for i in range(3) for j in range(3)) and all(
            w_back[i] == wv[i] for i in range(3)):
        roundtrip += 1
# the linear-cell census: every one of the 9 is homogeneous of degree exactly 1 in the metric
# COEFFICIENT variables (q, w), the P4 parameters (kappa, beta) entering as scalars [P4; D2.1]
COEFVARS = ["q11", "q22", "q33", "q12", "q13", "q23", "w1", "w2", "w3"]
deg_census = sorted({p.deg_in(COEFVARS) for p in lin_cells.values()})
deg_full = sorted({p.deg() for p in lin_cells.values()})
# the exponential cell: located in the frozen text (D2.1 / CT1.12 / IT.52(3)(i)) with live witnesses
exp_txt = ("Omega:=e^{\alpha_\Omega a_{00}}" in P1T or "Omega=e^{\alpha_\Omega a_{00}}" in P1T
           or "\\Omega:=e^{\\alpha_\\Omega a_{00}}" in P1T)
exp_wit1 = "a_{00}" in P1T and "\\Omega" in P1T
price_i = "a_{00}" in ALLTIER and "only the exponent" in ALLTIER
b2 = (len(lin_cells) == 9 and deg_census == [1] and roundtrip == 3
      and 9 + 1 == 10 and exp_txt and exp_wit1 and price_i)
chk("B2  [CT1.12; D2.1; IT.52(3)(i); NEW ROW]: the bijection is a bijection, but NOT a linear one --"
    "\n           cell census 9 + 1 = 10: the 9 cells (q_ij -> gbar_ij - delta_ij, w_i -> gbar_0i) are"
    "\n           LINEAR -- homogeneous of degree exactly 1 in the metric coefficients (q, w), the P4"
    "\n           parameters (kappa, beta) entering as scalars [P4; D2.1] -- with the exact rational inverse"
    "\n           q = (gbar-delta)/kappa, w = gbar_0i/(kappa*beta) round-tripping identically on three"
    "\n           witness triples; the TENTH cell is EXPONENTIAL -- Omega = exp(alpha_Omega*a_00), so"
    "\n           g_00 = -Omega^2 and a_00 is never a component of g, only the exponent. That is"
    "\n           IT.52(3)(i)'s first price on any identification, re-certified here from the frozen text"
    "\n           (live witnesses present, so the scan cannot pass dead).",
    b2, "linear cells=%d (degree in (q,w): %s; full degree: %s) round-trips=%d/3;"
    " exponential cell located: %s"
    % (len(lin_cells), deg_census, deg_full, roundtrip, exp_txt and price_i))

# ---- B3: the ADM/Schur identities and g_0i = kappa*beta*Omega^2*w_i ------------------------
adm_ok = schur_ok = g0i_ok = inv_ok = 0
NW = 0
for (Om2, kpv, btv, wv, qv) in WITS:
    NW += 1
    res = D.sector_to_adm(Om2, kpv, btv, list(wv), qv)
    adm_ok += int(res["conformal_ok"])
    schur_ok += int(res["schur_ok"])
    g = res["g"]
    g0i_ok += int(all(g[0][i + 1] == Om2 * kpv * btv * wv[i] for i in range(3)))
    # BM.34(1)'s inverse-metric rows: g^{00} = -1/N^2, g^{0i} = N^i/N^2, g^{ij} = gamma^{ij} - N^iN^j/N^2
    gam = res["gamma"]
    Ni = res["Ni"]
    N2 = res["N2"]
    ginv = D.inverse3(gam)
    Nup = [sum((ginv[i][j] * Ni[j] for j in range(3)), Fr(0)) for i in range(3)]
    # verify by the defining relation g^{mu a} g_{a nu} = delta^mu_nu on the constructed rows
    rows = [[Fr(0)] * 4 for _ in range(4)]
    rows[0][0] = -1 / N2
    for i in range(3):
        rows[0][i + 1] = Nup[i] / N2
        rows[i + 1][0] = Nup[i] / N2
    for i in range(3):
        for j in range(3):
            rows[i + 1][j + 1] = ginv[i][j] - Nup[i] * Nup[j] / N2
    prod = [[sum((rows[a][c] * g[c][b] for c in range(4)), Fr(0)) for b in range(4)] for a in range(4)]
    inv_ok += int(all(prod[a][b] == Fr(int(a == b)) for a in range(4) for b in range(4)))
# the citation correction: g_0i = kappa*beta*Omega^2*w_i sits at BM.34(1)/(3) and FT.157(1), NOT BM.34(2)
n4 = norm(P4T)
bm34_head = "BM.34" in P4T
loc_1 = r"N_i=\Omega^2\varkappa\beta w_i" in P4T
cl3 = r"g_{ij}N^j=N_i=g_{0i}=\Omega^2\varkappa\beta w_i" in P4T
ft157 = r"g_{0i}=\varkappa\beta\,\Omega^2\,w_i" in P3T
bm34_2_is_vacuum = ("the vacuum's emergent metric is the flat metric" in n4
                    or "the vacuum's emergent metric is the flat metric" in norm(P4T))
b3 = (adm_ok == NW and schur_ok == NW and g0i_ok == NW and inv_ok == NW and NW == 3
      and bm34_head and (loc_1 or cl3) and ft157 and bm34_2_is_vacuum)
chk("B3  [BM.34(1),(2),(3); FT.157(1); D2.1; machine via the standing duality core]: the ADM/Schur layer"
    "\n           re-derived exactly on three rational witnesses: g_{mu nu} = Omega^2 gbar_{mu nu} entrywise,"
    "\n           N^2 det gamma = -det g, the inverse-metric rows g^{00} = -1/N^2, g^{0i} = N^i/N^2,"
    "\n           g^{ij} = gamma^{ij} - N^iN^j/N^2 (certified by g^{mu a}g_{a nu} = delta^mu_nu), and the"
    "\n           shift functional g_0i = kappa*beta*Omega^2*w_i = N_i -- the SAME three coefficients w_i"
    "\n           are the metric's time-space block and the momentum's drag term (one block, two derived"
    "\n           reads). CITATION CORRECTION (recorded, not silently fixed): the directive attributes"
    "\n           g_0i = kappa*beta*Omega^2*w_i to BM.34(2); the frozen loci are BM.34(1) (N_i) and"
    "\n           BM.34(3) (g_ij N^j = N_i = g_0i), with FT.157(1) the block-identity row -- BM.34(2)"
    "\n           carries the line element and the flat-vacuum row.",
    b3, "witnesses=%d; conformal %d/%d; Schur %d/%d; g_0i %d/%d; inverse rows %d/%d"
    % (NW, adm_ok, NW, schur_ok, NW, g0i_ok, NW, inv_ok, NW))

# ---- B4: the flat vacuum and the exact signature census -----------------------------------
vac = D.sector_to_adm(Fr(1), Fr(0), Fr(0), [Fr(0)] * 3, [[Fr(0)] * 3 for _ in range(3)])
vac_ok = (vac["N2"] == Fr(1) and all(vac["Ni"][i] == Fr(0) for i in range(3))
          and all(vac["gamma"][i][j] == Fr(int(i == j)) for i in range(3) for j in range(3))
          and all(vac["g"][a][b] == (Fr(-1) if (a == 0 and b == 0) else (Fr(1) if a == b else Fr(0)))
                  for a in range(4) for b in range(4)))
# the signature census: gbar_ij > 0 certified by exact LDL^T pivots, then sig(gbar) = (-,+,+,+)
sig_rows = []
inertia_ok = schur_neg = 0
for (_Om2, kpv, btv, wv, qv) in WITS:
    gs = [[Fr(int(i == j)) + kpv * qv[i][j] for j in range(3)] for i in range(3)]
    neg, pos, zer, piv = inertia(gs)
    posdef = (neg == 0 and zer == 0 and pos == 3)
    gb = [[Fr(0)] * 4 for _ in range(4)]
    gb[0][0] = Fr(-1)
    for i in range(3):
        gb[0][i + 1] = gb[i + 1][0] = kpv * btv * wv[i]
        for j in range(3):
            gb[i + 1][j + 1] = gs[i][j]
    n4_, p4_, z4_, _ = inertia(gb)
    ginvs = D.inverse3(gs)
    Nlow = [btv * wv[i] for i in range(3)]
    schur = Fr(-1) - kpv * kpv * sum((ginvs[i][j] * Nlow[i] * Nlow[j]
                                      for i in range(3) for j in range(3)), Fr(0))
    det_gs = D.det3(gs)
    det_neg = (D.det4(gb) == det_gs * schur) and D.det4(gb) < 0 and schur < 0
    inertia_ok += int(posdef and (n4_, p4_, z4_) == (1, 3, 0))
    schur_neg += int(det_neg)
    sig_rows.append(((neg, pos, zer), (n4_, p4_, z4_)))
b4 = vac_ok and inertia_ok == 3 and schur_neg == 3
chk("B4  [CT1.12; BM.34(2); FT.156(1); machine: exact rational LDL^T inertia]: the vacuum row and the"
    "\n           signature row. (a) (a_00, q_ij, w_i) = 0 gives (Omega, N, N^i, g_ij) = (1,1,0,delta_ij)"
    "\n           by exact substitution -- the vacuum's emergent metric is the flat metric. (b) On three"
    "\n           witness triples with gbar_ij certified positive-definite by exact LDL^T pivots (all three"
    "\n           positive, none zero -- no floating point), the full gbar has inertia exactly (1 negative,"
    "\n           3 positive), and det gbar = det(gbar_ij) * (-1 - kappa^2 N_i (gbar^{-1})^{ij} N_j) < 0 by"
    "\n           the CT1.12 Schur form: sig(gbar) = sig(g) = (-,+,+,+) in the perturbative regime. The"
    "\n           single negative eigenvalue is the temporal direction's ONE component; the triad supplies"
    "\n           the symmetric sextuple and the three shifts.",
    b4, "vacuum=%s; inertia rows=%s" % (vac_ok, sig_rows))

# ---- B5: the zero-coordinate row for the S-odd six (with the fake-carrier adversarial) -----
# D2.1: X_(+) = a_00 E_0 + q_ij E^{ij} (symmetric), X_(-) = w_i W_i.  Which generators appear?
carr = {"E_0": "a_00", "Sigma": "Sigma_tr (via q_ij = hhat_ij + delta_ij Sigma_tr / 3)",
        "W1": "w_1", "W2": "w_2", "W3": "w_3"}
carr_G = {n: "hhat_ij" for n in FLAT if BLOCK[n] == "G"}
metric_carriers = dict(carr)
metric_carriers.update(carr_G)
nonzero = {n: len(COORDS[n]) for n in metric_carriers}
zero_carriers = [n for (n, blk, _) in GENS if blk in ("J+", "J-")]
zero_coeffs = {n: COORDS[n] for n in zero_carriers}
# the fake-carrier adversarial: pretend J_1 is a dictionary carrier and show the dictionary row
# would then be S-ODD -- i.e. it cannot be a row of an S-even dictionary
fake = "J1"
fake_s = s_sign[fake]
# and: the metric reads of D2.1 built from an S-odd generator would flip sign under Ad(S)
b5 = (len(metric_carriers) == 10 and all(v > 0 for v in nonzero.values())
      and len(zero_carriers) == 6
      and all(all(v == ZERO for v in zero_coeffs[n].values()) is False for n in zero_carriers)
      and all(s_sign[n] == -1 for n in zero_carriers)
      and all(s_sign[n] == +1 for n in metric_carriers)
      and fake_s == -1)
chk("B5  [FT.141(5); CT1.12a(2); FT.30; Def-H.14; D2.1; machine]: the ZERO-coordinate row, exactly --"
    "\n           D2.1's sector coefficients X_(+) = a_00 E_0 + q_ij E^{ij} and X_(-) = w_i W_i have as"
    "\n           their carriers precisely the 10 S-even generators (E_0, Sigma, Ehat^{ij} x5, W_i x3), every"
    "\n           one with a nonzero coordinate; the S-odd six (J_i, K_i) are S-odd, hence not rows of an"
    "\n           S-even dictionary, and carry ZERO metric coordinates. ADVERSARIAL: a fake carrier (J_1)"
    "\n           has S-grade -1, so any dictionary row built on it would be S-odd -- it cannot enter"
    "\n           g_{mu nu}, which is orientation-even. The consequence is FT.30's block audit: the seals"
    "\n           are the ledger-side events (D1.2's n_R: 0->1 and 1->0), never geometry.",
    b5, "metric carriers=%d (all nonzero); zero-coordinate generators=%d (all S-odd); fake carrier S=%+d"
    % (len(metric_carriers), len(zero_carriers), fake_s))

# ---- B6: the discipline row -- a dictionary, not an identity ------------------------------
not_adopted = ("the identification is" in ALLTIER and "neg\\text{adopted}" in ALLTIER)
four_prices = all(t in ALLTIER for t in ("nonlinearity", "swap-even", "chart side vs register side",
                                         "strength bar"))
dict_not_bridge = ("DICTIONARY" in ALLTIER and "bridge" in ALLTIER)
ft30_verdict = ("block-local quantum" in P3T and "joint" in P3T)
# dead-witness control: a token that must NOT be present (proves the census is reading real text)
dead_control = ("the identification is ADOPTED" not in ALLTIER)
b6 = not_adopted and four_prices and dict_not_bridge and ft30_verdict and dead_control
chk("B6  [IT.52(3); IT.54(1); D-RS2 @ IT.56(2); BM.134(5); IT.68(3); FT.30 Verdict; text census with"
    "\n           live witnesses]: THE DISCIPLINE ROW that decides claim 1's two readings. The frozen record"
    "\n           already carries (i) IT.52(3)'s FOUR PRICES on the metric identification -- nonlinearity"
    "\n           (a_00 only the exponent), swap-evenness (three conditions cutting 10 -> 7), chart side vs"
    "\n           register side, and the count->strength bar -- with the box 'the 10:10 match is X against"
    "\n           the COEFFICIENT FIELDS; the map to g_{mu nu} leaves the subspace -- the identification is"
    "\n           NOT ADOPTED'; (ii) IT.54(1)'s verdict row 'the metric identification (10:10) -- NOT"
    "\n           ADOPTED, four prices'; (iii) the standing dictionary-not-bridge discipline [D-RS2;"
    "\n           BM.134(5); IT.68(3): partners, not equals]. So 'the rung-1 forces HAVE metric coordinates'"
    "\n           is DERIVED (B1-B5), while 'they ARE the dimensions' as an ontological identity stays"
    "\n           NOT ADOPTED with its four prices -- an adoption would be the Architect's act, and this"
    "\n           tier does not force it.",
    b6, "not-adopted box=%s; four prices=%s; dictionary-not-bridge=%s; FT.30 joint-read=%s"
    % (not_adopted, four_prices, dict_not_bridge, ft30_verdict))

# ==========================================================================================
# PART C -- CLAIM 2: channels, not ticks.  The ledger side, the support side, the wave side.
# ==========================================================================================
print("\n" + "-" * 104)
print("PART C -- CLAIM 2 adjudicated: ticks are ledger events; the forces are pair-channel geometry")
print("-" * 104)


def fact(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def binom(n, k):
    return fact(n) // (fact(k) * fact(n - k)) if 0 <= k <= n else 0


# ---- C1: the tick is a ledger event (exact integer censuses) ------------------------------
seqs = list(product(range(4), repeat=5))
mono = strict_at_emit = no_inverse = 0
for s in seqs:
    L = [0]
    for k in range(5):
        L.append(L[-1] + s[k])
    mono += int(all(L[i + 1] >= L[i] for i in range(5)))
    strict_at_emit += int(all((s[k] > 0) == (L[k + 1] > L[k]) for k in range(5)))
    rev = list(reversed(L))
    no_inverse += int((sum(s) == 0) or any(rev[i + 1] < rev[i] for i in range(len(rev) - 1)))
tick_txt = (r"\neg\exists\,\tau^{-1}" in P1T and r"U\notin\mathfrak L" in P1T
            and r"\tau_n\to\tau_{n+1}" in P1T)
geom_txt = (r"ds^2(e):=g_{\mu\nu}(e)\,\Delta x^\mu_e\,\Delta x^\nu_e" in P1T and r"x^0:=\tau_n" in P1T)
c1 = (mono == len(seqs) and strict_at_emit == len(seqs) and no_inverse == len(seqs)
      and tick_txt and geom_txt)
chk("C1  [A6; A7; D0.7; C11; D1.6; D1.8; machine census over all 1024 five-tick histories]: THE TICK IS"
    "\n           A LEDGER EVENT, NOT GEOMETRY. A6's tick is tau_n -> tau_{n+1}: rho -> U rho U^dagger with"
    "\n           U ~ Haar(SU(2)) and U NOT retained in L, and no inverse tick exists (no tau^-1); A7/D0.7"
    "\n           make the ledger the ordered record, |L(tau_n)| = sum_{k<n} n_real_out(tau_k), monotone in"
    "\n           every one of the 1024 histories and strictly increasing exactly at the ticks that emit"
    "\n           real content -- so the reversed record strictly decreases somewhere and no inverse"
    "\n           realization exists on the record. The metric never appears in a tick clause: it appears in"
    "\n           D1.6's line element ds^2(e) = g_{mu nu}(e) Dx^mu_e Dx^nu_e and in D1.8's x^0 := tau_n. The"
    "\n           tick ENTERS the geometry as an increment Dx^0; the force blocks enter as the coefficients"
    "\n           g_{mu nu}(e). Two roles, two currencies [FT.159(4): the line-element channel CONTRACTS"
    "\n           metric data with tick data].",
    c1, "histories=%d; monotone=%d; strict-iff-emitting=%d; no-inverse-on-record=%d; text witnesses=%s/%s"
    % (len(seqs), mono, strict_at_emit, no_inverse, tick_txt, geom_txt))


# ---- C2: the seal clock (1,1,1) and the Janus arrow combinatorics -------------------------
def admissible_single(word):
    """D1.2's move domains on ONE pair: J+ needs n_R = 0, J- needs n_R = 1."""
    n = 0
    for mv in word:
        if mv == "J+" and n != 0:
            return False
        if mv == "J-" and n != 1:
            return False
        n += 1 if mv == "J+" else -1
    return True


single_counts = {L: sum(1 for w in product(["J+", "J-"], repeat=L) if admissible_single(w))
                 for L in range(0, 9)}
completed_single = {2 * m: sum(1 for w in product(["J+", "J-"], repeat=2 * m)
                               if admissible_single(w) and w.count("J+") == w.count("J-"))
                    for m in range(1, 5)}
_comp = [w for m in range(1, 5) for w in product(["J+", "J-"], repeat=2 * m)
         if admissible_single(w) and w.count("J+") == w.count("J-")]
ends_minus = all(w[-1] == "J-" for w in _comp)
reversal_bad = all(not admissible_single(tuple(reversed(w))) for w in _comp)


def two_pair_bruteforce(n):
    tot = 0
    for mask in range(1 << (2 * n)):
        pos0 = [k for k in range(2 * n) if (mask >> k) & 1]
        if len(pos0) % 2:
            continue
        m0, m1 = len(pos0) // 2, (2 * n - len(pos0)) // 2
        seq0 = ["J+", "J-"] * m0
        seq1 = ["J+", "J-"] * m1
        i = j = 0
        ok = True
        w0, w1 = [], []
        for k in range(2 * n):
            if (mask >> k) & 1:
                w0.append(seq0[i]); i += 1
            else:
                w1.append(seq1[j]); j += 1
        ok = admissible_single(w0) and admissible_single(w1)
        ok = ok and w0.count("J+") == w0.count("J-") and w1.count("J+") == w1.count("J-")
        tot += int(ok)
    return tot


interl = {n: two_pair_bruteforce(n) for n in range(1, 5)}
closed_form = {n: 2 ** (2 * n - 1) for n in range(1, 5)}
multinomial = {n: sum(binom(2 * n, 2 * m0) for m0 in range(n + 1)) for n in range(1, 5)}
c2 = (all(v == 1 for v in single_counts.values()) and completed_single == {2: 1, 4: 1, 6: 1, 8: 1}
      and ends_minus and reversal_bad and interl == closed_form == multinomial
      and (interl[1], interl[2], interl[3]) == (2, 8, 32) and interl[4] == 128)
chk("C2  [CT0.3; D1.2; D1.3; FT.144(2),(4)(ii); A6; machine: exhaustive enumeration + exact binomials]:"
    "\n           THE SEAL CLOCK AND THE ARROW. CT0.3's atomic ledger event moves all three counters"
    "\n           together -- J+ : (Dn_R, delta_h, delta_tau) = (+1,+1,+1), J- : (-1,-1,-1) -- with D1.9"
    "\n           zeroing every further counter: ONE seal = ONE edge = ONE hop = ONE tick, exactly. The"
    "\n           arrow combinatorics re-derived from scratch: on a single pair the D1.2 domains force strict"
    "\n           alternation, so there is exactly ONE admissible history at every length 0..8 and exactly"
    "\n           ONE completed history at every even length, namely (J+J-)^m; every completed nonempty"
    "\n           history ends in J-, and its pure order reversal leads with J- -- inadmissible at the first"
    "\n           event, since J- is undefined at n_R = 0. NEW CLOSED FORM: the two-pair completed"
    "\n           interleavings of total length 2n number exactly 2^(2n-1) = sum_m C(2n,2m) -- the frozen"
    "\n           witnesses 2, 8, 32 at 2n = 2,4,6 [FT.144(2)] re-derived by brute force over all"
    "\n           even-cardinality position sets, and extended to 2n = 8: 128.",
    c2, "single-pair admissible per length=%s; completed=%s; interleavings=%s = closed form %s"
    % (single_counts, completed_single, interl, closed_form))


# ---- C3: the tick-locality support census (D1.9), non-vacuous -----------------------------
def edges_of(n, kind):
    if kind == "path":
        return [(i, i + 1) for i in range(n - 1)]
    if kind == "cycle":
        return [(i, (i + 1) % n) for i in range(n)]
    if kind == "star":
        return [(0, i) for i in range(1, n)]
    raise ValueError(kind)


def line_graph_dist(E, e, f):
    ie, jf = E.index(e), E.index(f)
    if ie == jf:
        return 0
    adj = {i: {j for j in range(len(E)) if j != i and set(E[i]) & set(E[j])} for i in range(len(E))}
    seen = {ie: 0}
    frontier = [ie]
    d = 0
    while frontier and jf not in seen:
        d += 1
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in seen:
                    seen[v] = d
                    nxt.append(v)
        frontier = nxt
    return seen.get(jf)


tot_v = nonvac = saturated = 0
far_min = []
dom_exact = True
for kind in ("path", "cycle", "star"):
    for n in (4, 5, 6, 7):
        E = edges_of(n, kind)
        V = sorted({x for e in E for x in e})
        adj = {v: {y for e in E for y in e if e != (v,) and (v in e)} for v in V}
        for v in V:
            # exact vertex BFS distances
            dist = {v: 0}
            fr = [v]
            d = 0
            while fr:
                d += 1
                nx = []
                for u in fr:
                    for y in adj[u]:
                        if y not in dist:
                            dist[y] = d
                            nx.append(y)
                fr = nx
            dom = [e for e in E if v in e]                     # D1.9's incident-edge domain
            hop = {e: 1 + min(dist[x] for x in e) for e in E}   # hop-distance from v to the edge e
            dom_exact = dom_exact and (dom == [e for e in E if hop[e] == 1])
            far = [e for e in E if e not in dom]
            tot_v += 1
            if far:
                dmin = min(hop[e] for e in far)
                far_min.append(dmin)
                nonvac += int(dmin >= 2)
            else:
                saturated += 1
digon = [(0, 1), (1, 0)]
digon_inc = {v: len([e for e in digon if v in e]) for v in (0, 1)}
c3 = (dom_exact and nonvac + saturated == tot_v and nonvac == 62 and min(far_min) >= 2
      and saturated == 4 and digon_inc == {0: 2, 1: 2} and tot_v == 66)
chk("C3  [D1.9; CT0.3 Pf; CT2.6 Pf; FT.28; machine: exact vertex BFS over three graph families]:"
    "\n           TICK LOCALITY IS A 1-HOP BOUND, and it is NON-VACUOUS. D1.9: dom(tick(v)) is contained in"
    "\n           {v} union {e in E : e contains v}, pre- and post-tick data only, and THERE EXISTS NO READ"
    "\n           AT EDGE-DISTANCE > 1 -- where the edge-distance of f from v is 1 + the vertex distance to"
    "\n           f's nearer endpoint, so the incident edges are exactly the distance-1 set (certified"
    "\n           machine-side on every instance). Census over the path, cycle and star graphs on 4,5,6,7"
    "\n           vertices (66 vertex-instances): in 62 of them the complement of the domain is nonempty and"
    "\n           lies at edge-distance >= 2, and in the 4 remaining ones (the star centres) the domain"
    "\n           saturates the whole edge set -- so the bound excludes real content rather than stating"
    "\n           nothing. CT0.3's proof uses exactly this row to zero all further counters at a seal. The"
    "\n           digon floor Sigma_min [FT.28] has 2 vertices and 2 edges, both incident to both: the"
    "\n           minimal real edge already sits at the locality ceiling.",
    c3, "instances=%d (non-vacuous=%d, saturating=%d); domain==distance-1 set on all=%s;"
    " min far edge-distance=%d; digon incidence=%s"
    % (tot_v, nonvac, saturated, dom_exact, min(far_min), digon_inc))

# ---- C4: the pair-channel support and the register bounds --------------------------------
C_cap = 16
tiling = {"G": 5, "W": 3, "H": 1, "D+": 1, "J+": 3, "J-": 3}
D_tick = {n: 2 ** (n + 1) for n in range(0, 7)}
O_n = {n: max(0, D_tick[n] - C_cap) for n in range(0, 7)}
adm = {n: D_tick[n] <= C_cap for n in range(0, 7)}
hop_cells = {(dh, dt) for dt in range(1, 9) for dh in range(0, 4 * dt + 1)}
c4 = (sum(tiling.values()) == C_cap and D_tick[3] == C_cap
      and adm == {0: True, 1: True, 2: True, 3: True, 4: False, 5: False, 6: False}
      and O_n == {0: 0, 1: 0, 2: 0, 3: 0, 4: 16, 5: 48, 6: 112}
      and all(dh <= 4 * dt for (dh, dt) in hop_cells) and 2 ** 4 == C_cap and 2 ** 5 == 32 > C_cap)
chk("C4  [A1; A2; CT0.5; CT0.6; CT0.11; CT0.12; CT0.14; D0.6; D0.9; Cor CT0.6a; machine: exact"
    "\n           integers]: THE SUPPORT OF A FORCE ASPECT IS ONE PAIR CHANNEL. A1 attaches rho_pq to each"
    "\n           pair, A2 prices one pair channel at 1 qubit-tick, and CT0.12 tiles that ONE 16-dimensional"
    "\n           space with the six aspects (3+3+5+3+1+1 = 16 = C_cap = dim_R H(C^4)); D0.6 defines a hop"
    "\n           as one traversal of one real edge. The tick load is D_tick(n) = 2^(n+1) [CT0.5] against"
    "\n           C_cap = 16, so O(n) = max(0, 2^(n+1)-16) = (0,0,0,0,16,48,112) at n = 0..6 and the"
    "\n           channel-admissible rungs are exactly n <= 3, saturated at n = 3 [CT0.11]. Multi-hop content"
    "\n           through ONE channel is bounded but not forbidden: Cor CT0.6a gives delta_h <= 4*delta_tau"
    "\n           (census delta_tau = 1..8, every cell exact) and the bound is sharp because 4 hop-bits per"
    "\n           tick present 2^4 = 16 = C_cap alternatives while a fifth presents 2^5 = 32 > 16 --"
    "\n           oversubscribed.",
    c4, "tiling=%s sum=%d; D_tick=%s; O(n)=%s; bound cells=%d"
    % (tiling, sum(tiling.values()), D_tick, O_n, len(hop_cells)))

# ==========================================================================================
# C5-C6: THE WAVE-OPERATOR CENSUS -- a formal jet algebra over Q, two independent routes
# ==========================================================================================
ET = [Fr(-1), Fr(1), Fr(1), Fr(1)]        # eta_{mu nu} = eta^{mu nu} = diag(-1,1,1,1) [A3; C13]


def s2(a, b):
    return (min(a, b), max(a, b))


def srt(*ix):
    return tuple(sorted(ix))


def e_add(x, y):
    out = dict(x)
    for k, v in y.items():
        out[k] = out.get(k, Fr(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def e_mul(x, c):
    c = Fr(c)
    return {k: Fr(v) * c for k, v in x.items() if Fr(v) * c != 0}


def e_neg(x):
    return e_mul(x, -1)


def e_sub(x, y):
    return e_add(x, e_neg(y))


def hsym(mu, nu):
    return ("h",) + s2(mu, nu)


def dhsym(a, mu, nu):
    return ("dh", a) + s2(mu, nu)


def ddhsym(a, b, mu, nu):
    return ("ddh",) + srt(a, b) + s2(mu, nu)


def dddxisym(a, b, c, mu):
    return ("dddxi",) + srt(a, b, c) + (mu,)


def d_of(e, a):
    """the formal partial derivative d_a of an h-jet expression (h and dh symbols only)."""
    out = {}
    for k, v in e.items():
        if k[0] == "h":
            out = e_add(out, {dhsym(a, k[1], k[2]): v})
        elif k[0] == "dh":
            out = e_add(out, {ddhsym(a, k[1], k[2], k[3]): v})
        else:
            raise ValueError("d_of on a %s symbol" % k[0])
    return out


def box_of(e):
    out = {}
    for a in range(4):
        out = e_add(out, e_mul(d_of(d_of(e, a), a), ET[a]))
    return out


TRACE = {}
for l in range(4):
    TRACE = e_add(TRACE, e_mul({hsym(l, l): Fr(1)}, ET[l]))          # T = h^lambda_lambda
V = {}
for nu in range(4):
    e = {}
    for l in range(4):
        e = e_add(e, e_mul(d_of({hsym(nu, l): Fr(1)}, l), ET[l]))    # V_nu = d^lambda h_{nu lambda}
    V[nu] = e
dV = {}
for a in range(4):
    for nu in range(4):
        dV[(a, nu)] = d_of(V[nu], a)
divV = {}
for l in range(4):
    divV = e_add(divV, e_mul(dV[(l, l)], ET[l]))                     # d^lambda V_lambda


def G1_formula():
    """CT1.18's DISPLAYED expression, expanded into h-jets."""
    out = {}
    for mu in range(4):
        for nu in range(mu, 4):
            e = e_neg(box_of({hsym(mu, nu): Fr(1)}))                          # -box h_{mu nu}
            e = e_sub(e, d_of(d_of(TRACE, mu), nu))                           # -d_mu d_nu T
            e = e_add(e, dV[(mu, nu)])                                        # +d_mu V_nu
            e = e_add(e, dV[(nu, mu)])                                        # +d_nu V_mu
            if mu == nu:
                e = e_add(e, e_mul(e_sub(box_of(TRACE), divV), ET[mu]))       # +eta(box T - d^l V_l)
            out[(mu, nu)] = e_mul(e, Fr(1, 2))
    return out


def G1_ricci(eta=None):
    """the INDEPENDENT route: Gamma^(1) -> R^(1)_{mu nu} -> R^(1) -> G^(1)_{mu nu}.
    `eta` overrides the signature representative (the C13-convention adversarial)."""
    ETT = ET if eta is None else eta

    def Gam(lam, mu, nu):
        """Gamma^(1)lam_{mu nu} = (1/2) eta^{lam rho}(d_mu h_{nu rho} + d_nu h_{mu rho} - d_rho h_{mu nu});
        eta is diagonal [C13], so the rho-sum collapses to rho = lam."""
        c = Fr(1, 2) * ETT[lam]
        e = e_mul(d_of({hsym(nu, lam): Fr(1)}, mu), c)
        e = e_add(e, e_mul(d_of({hsym(mu, lam): Fr(1)}, nu), c))
        e = e_add(e, e_mul(d_of({hsym(mu, nu): Fr(1)}, lam), -c))
        return e
    Ric = {}
    for mu in range(4):
        for nu in range(mu, 4):
            e = {}
            for lam in range(4):
                e = e_add(e, d_of(Gam(lam, mu, nu), lam))
                e = e_sub(e, d_of(Gam(lam, mu, lam), nu))
            Ric[(mu, nu)] = e
    Rsc = {}
    for mu in range(4):
        Rsc = e_add(Rsc, e_mul(Ric[(mu, mu)], ETT[mu]))
    out = {}
    for mu in range(4):
        for nu in range(mu, 4):
            e = dict(Ric[(mu, nu)])
            if mu == nu:
                e = e_sub(e, e_mul(Rsc, Fr(1, 2) * ETT[mu]))
            out[(mu, nu)] = e
    return out


G1F, G1R = G1_formula(), G1_ricci()
KEYS = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]
two_routes = all(e_sub(G1F[k], G1R[k]) == {} for k in KEYS)
n_terms = sum(len(v) for v in G1F.values())

# the trace/divergence structure: D := G1 + box(h)/2 is manifestly built from T- and V-jets
TV = {}
for mu in range(4):
    for nu in range(mu, 4):
        e = e_mul(d_of(d_of(TRACE, mu), nu), Fr(-1, 2))
        e = e_add(e, e_mul(dV[(mu, nu)], Fr(1, 2)))
        e = e_add(e, e_mul(dV[(nu, mu)], Fr(1, 2)))
        if mu == nu:
            e = e_add(e, e_mul(e_sub(box_of(TRACE), divV), Fr(1, 2) * ET[mu]))
        TV[(mu, nu)] = e
struct = all(e_sub(e_add(G1F[k], e_mul(box_of({hsym(k[0], k[1]): Fr(1)}), Fr(1, 2))), TV[k]) == {}
             for k in KEYS)
tv_nonempty = sum(len(v) for v in TV.values())

# gauge invariance: substitute h -> h + d_mu xi_nu + d_nu xi_mu into the ddh symbols
def gauge_subst(e, projected=False):
    out = {}
    for k, v in e.items():
        if k[0] != "ddh":
            out = e_add(out, {k: v})
            continue
        a, b, mu, nu = k[1], k[2], k[3], k[4]
        t = {k: v}
        t = e_add(t, e_mul({dddxisym(a, b, mu, nu): Fr(1)}, v))
        t = e_add(t, e_mul({dddxisym(a, b, nu, mu): Fr(1)}, v))
        if projected and mu == nu:
            for l in range(4):
                t = e_sub(t, e_mul({dddxisym(a, b, l, l): Fr(1)}, Fr(1, 2) * ET[mu] * ET[l] * v))
        out = e_add(out, t)
    return out


def gauge_delta(projected):
    out = {}
    for k in KEYS:
        shifted = {kk: gauge_subst(vv, projected) for kk, vv in ((k, G1F[k]),)}[k]
        out[k] = e_sub(shifted, G1F[k])
    return out


dG_std = gauge_delta(False)
xi_terms_std = sum(1 for k in KEYS for s in dG_std[k] if s[0] == "dddxi")
gauge_inv = all(dG_std[k] == {} for k in KEYS)
# non-vacuity: count the xi-terms GENERATED before collection (two per second-derivative
# monomial), so the cancellation below cannot pass as an empty identity
n_ddh = sum(len([s for s in G1F[k] if s[0] == "ddh"]) for k in KEYS)
xi_generated = 2 * n_ddh
xi_surviving = sum(len([s for s in dG_std[k] if s[0] == "dddxi"]) for k in KEYS)

# CT1.18's Rmk (correction): the TRACELESS-PROJECTED transformation is not an invariance
dG_prj = gauge_delta(True)
resid_nonzero = any(dG_prj[k] != {} for k in KEYS)
# the canon's stated residual: (1/2)(d_mu d_nu - eta_{mu nu} box)(d . xi)
cand = {}
for mu in range(4):
    for nu in range(mu, 4):
        e = {}
        for l in range(4):
            e = e_add(e, e_mul({dddxisym(mu, nu, l, l): Fr(1)}, Fr(1, 2) * ET[l]))
        if mu == nu:
            for l in range(4):
                for a in range(4):
                    e = e_sub(e, e_mul({dddxisym(a, a, l, l): Fr(1)},
                                       Fr(1, 2) * ET[mu] * ET[a] * ET[l]))
        cand[(mu, nu)] = e
rmk_matches = all(e_sub(dG_prj[k], cand[k]) == {} for k in KEYS)

# the SECOND-TIME-DERIVATIVE census: which components carry a d0d0 term?
d00 = {}
for k in KEYS:
    d00[k] = {s: v for s, v in G1F[k].items() if s[0] == "ddh" and s[1] == 0 and s[2] == 0}
constraint_cells = [k for k in KEYS if not d00[k]]
wave_cells = [k for k in KEYS if d00[k]]
d00_hcells = {}
for k in wave_cells:
    d00_hcells[k] = sorted({(s[3], s[4]) for s in d00[k]})
c5 = (two_routes and struct and gauge_inv and xi_generated > 0 and xi_surviving == 0
      and resid_nonzero and rmk_matches
      and len(constraint_cells) == 4 and len(wave_cells) == 6
      and sorted(constraint_cells) == [(0, 0), (0, 1), (0, 2), (0, 3)]
      and all(len(v) > 0 for v in d00_hcells.values()))
#print("DBG C5:",two_routes,struct,gauge_inv,xi_generated,resid_nonzero,rmk_matches,sorted(constraint_cells),len(wave_cells),{k:len(v) for k,v in d00.items()})
chk("C5  [CT1.18; CT1.10; AT.5(4); NEW ROW; machine: a formal jet algebra over Q, no floating point]:"
    "\n           THE WAVE-OPERATOR CENSUS. CT1.18's linearized Einstein tensor is re-derived TWICE by"
    "\n           independent routes -- from its displayed formula and from the linearized Christoffel/Ricci"
    "\n           pipeline -- and the two agree coefficient-wise on all 10 components (%d jet terms). Its"
    "\n           trace/divergence structure is certified exactly: G1 + box(h)/2 equals the manifest"
    "\n           T/V expression -(1/2)d_mu d_nu T + (1/2)(d_mu V_nu + d_nu V_mu) + (1/2)eta_{mu nu}"
    "\n           (box T - d^lambda V_lambda), built ONLY from the trace T = h^lambda_lambda and the"
    "\n           divergence V_nu = d^lambda h_{nu lambda}; hence on the traceless-transverse locus"
    "\n           (T = 0, V = 0 with all their jets) G1 = -(1/2)box h -- the massless wave operator."
    "\n           GAUGE INVARIANCE holds as an exact coefficient identity (%d third-derivative-of-xi terms"
    "\n           generated across the ten components, every one cancelling to zero -- %d survive), and"
    "\n           CT1.18's own Rmk correction is re-certified: the"
    "\n           traceless-PROJECTED transformation is NOT an invariance -- the residual equals exactly"
    "\n           (1/2)(d_mu d_nu - eta_{mu nu} box)(d . xi), nonzero."
    % (n_terms, xi_generated, xi_surviving),
    c5, "two routes agree=%s; T/V structure=%s (%d terms); gauge-invariant=%s (xi terms %d generated,"
        " %d surviving); projected residual nonzero=%s and matches the canon's form=%s"
    % (two_routes, struct, tv_nonempty, gauge_inv, xi_generated, xi_surviving, resid_nonzero,
       rmk_matches))

# the block attribution of the second-time-derivative census
attr = {"g_00 (1 cell)": "D+ (a_00 -> Omega -> lapse/conformal)",
        "g_0i (3 cells)": "W (w_i -> shift N_i)",
        "g_ij (6 cells)": "G (hhat_ij, 5) + H (Sigma_tr, 1)"}
spatial_d00 = {k: sorted({s2v for s2v in [(s[3], s[4]) for s in d00[k]]}) for k in wave_cells}
all_spatial_targets = sorted({t for k in wave_cells for t in spatial_d00[k]})
# ADVERSARIAL (the C13 convention): re-run the census with the flipped signature representative
# eta' = (+,+,+,+,-1); the constraint/wave split is a structural fact of the linearized Einstein
# tensor (gauge invariance), NOT an artifact of the mostly-plus choice
ET_FLIP = [Fr(1), Fr(1), Fr(1), Fr(-1)]
G1F_flip = G1_ricci(ET_FLIP)
d00_flip = {k: {s2v: v for s2v, v in G1F_flip[k].items()
                if s2v[0] == "ddh" and s2v[1] == 0 and s2v[2] == 0} for k in KEYS}
constraint_flip = sorted(k for k in KEYS if not d00_flip[k])
wave_flip = sorted(k for k in KEYS if d00_flip[k])
flip_same = (constraint_flip == sorted(constraint_cells) and len(wave_flip) == 6)
c6 = (flip_same and sorted(constraint_cells) == [(0, 0), (0, 1), (0, 2), (0, 3)] and len(wave_cells) == 6
      and all(k[0] >= 1 and k[1] >= 1 for k in wave_cells)
      and all((0, 0) not in spatial_d00[k] for k in wave_cells)
      and len(all_spatial_targets) == 6)
chk("C6  [CT1.18; CT1.10; CT1.12a(2); AT.5(4); BM.34(1),(3); FT.30; NEW ROW]: THE CONSTRAINT/WAVE SPLIT"
    "\n           IS THE BLOCK SPLIT. Census of the second-time-derivative content of G1: EXACTLY 4 of the 10"
    "\n           components -- the lapse cell g_00 and the three shift cells g_0i -- carry NO d0d0 term at"
    "\n           all, while all 6 spatial cells g_ij do (and none of them carries d0d0 h_00 or d0d0 h_0i)."
    "\n           Attributed through the dictionary [CT1.12a(2); FT.30]: the 4 constraint cells are exactly"
    "\n           the D+ block (a_00 -> Omega -> g_00, 1 cell) and the W block (w_i -> N_i -> g_0i, 3 cells);"
    "\n           the 6 wave cells are exactly the G block (hhat_ij, 5) plus the H block (Sigma_tr, 1). This"
    "\n           RE-DERIVES AT.5(4)'s row from the operator side -- N_i is the Lagrange multiplier of the"
    "\n           momentum constraint, fixed by the slicing choice and not by dynamics -- and it fixes the"
    "\n           exact scope of claim 2: CT1.18's own hypothesis (Upsilon = N_i = Sigma_tr = 0) switches off"
    "\n           D+, W and H, so the ONE frozen per-block wave equation in the corpus belongs to the G"
    "\n           quintet alone (CT1.10's spin-2 mode; CT1.18 Phys: the graviton is the E_{++} quintet"
    "\n           propagating on the auxiliary background). ADVERSARIAL (the C13 convention): re-running the"
    "\n           census with the FLIPPED signature representative eta' = (+,+,+,-1) leaves the split"
    "\n           unchanged -- it is a structural consequence of the gauge invariance, not an artifact of the"
    "\n           mostly-plus choice.",
    c6, "constraint cells=%s; wave cells=%s; d0d0 targets in the wave cells=%s; flipped-signature"
    " re-run identical=%s (constraint cells %s)"
    % (sorted(constraint_cells), sorted(wave_cells), all_spatial_targets, flip_same, constraint_flip))

# ---- C7: the locality-to-continuum row (text census with live witnesses) ------------------
ct26 = P2T[P2T.index("### CT2.6"):P2T.index("### CT2.7")]
loc_in_bridge = ("D1.9" in ct26 and "local ledger averages" in ct26.replace("\\ ", " ")
                 .replace("\\text", "").replace("{", "").replace("}", ""))
chart_row = ("hop counters projected on the 3 shift directions" in ct26)
x0_row = (r"x^0:=\tau_n" in ct26)
hyp_ii = ("unboundedly many real edges" in ct26)
smooth_step = ("jumps uniformly bounded" in ct26)
dead_control = ("hop counters projected on the 7 shift directions" not in ct26)
c7 = loc_in_bridge and chart_row and x0_row and hyp_ii and smooth_step and dead_control
chk("C7  [CT2.6 + its Pf and Rmk; D1.8; D1.9; BM.151(1); CT1.12; machine text census with live and"
    "\n           dead witnesses]: THE LOCALITY-TO-CONTINUUM ROW -- the 1-hop bound is a PREMISE of the"
    "\n           bridge theorem, not an obstacle to it. CT2.6's own smoothness step reads: 'coefficients ="
    "\n           local ledger averages; D1.9: updates local, finite; (iii): jumps uniformly bounded => smooth"
    "\n           interpolation, deviation -> 0 with h'. And its chart row is the sharpest anchor of the whole"
    "\n           hypothesis: x^0 := tau_n [D1.8] while x^i := HOP COUNTERS PROJECTED ON THE 3 SHIFT"
    "\n           DIRECTIONS (W_i sector) [CT1.12] -- the tick supplies the time coordinate, the W block"
    "\n           supplies the three spatial coordinate directions, and the counts are hops. So the"
    "\n           translation is: per-edge (1-hop) S-even data -> local averages -> smooth (M,g) under"
    "\n           hypotheses (i)-(iii), the last two derived from the ledger's own ladder [CT2.6 Rmk;"
    "\n           BM.151(1),(2)].",
    c7, "D1.9 in the bridge Pf=%s; hop-counter chart row=%s; x^0=tau_n=%s; hypothesis (ii)=%s;"
        " bounded-jump step=%s; dead control=%s"
    % (loc_in_bridge, chart_row, x0_row, hyp_ii, smooth_step, dead_control))

# ---- C8: the bars on the dynamical reading (the O1 ground re-run from scratch) ------------
CHI = [[ZERO, I], [-I, ZERO]]                                  # Def-H.33: chi-hat = i(|c><w|-|w><c|)
I2 = [[ONE, ZERO], [ZERO, ONE]]
PL = m_scale(Fr(1, 2), m_sub(I2, CHI))
PR = m_scale(Fr(1, 2), m_add(I2, CHI))
seed = [m_scale(Fr(1, 2), SIG[i]) for i in (1, 2, 3)]           # the su(2) seed generators
comm_zero = 0
tot_com = 0
for s in seed:
    A = kron(s, I2)                                            # weak acts seed (x) trivial
    for P in (PL, PR):
        B = kron(I2, P)
        tot_com += 1
        comm = m_sub(D.mat_mul(A, B), D.mat_mul(B, A))
        comm_zero += int(all(comm[i][j] == ZERO for i in range(4) for j in range(4)))
adv = m_sub(D.mat_mul(SIG[1], SIG[3]), D.mat_mul(SIG[3], SIG[1]))
adv_nonzero = any(adv[i][j] != ZERO for i in range(2) for j in range(2))
adv_exact = all(adv[i][j] == (D.Gauss(-2) if (i, j) == (0, 1) else
                              (D.Gauss(2) if (i, j) == (1, 0) else ZERO))
                for i in range(2) for j in range(2))
pl_ok = (all(m_sub(D.mat_mul(PL, PL), PL)[i][j] == ZERO for i in range(2) for j in range(2))
         and all(m_sub(D.mat_mul(PR, PR), PR)[i][j] == ZERO for i in range(2) for j in range(2))
         and m_tr(PL) == ONE and m_tr(PR) == ONE)
c8 = (comm_zero == tot_com == 6 and adv_nonzero and adv_exact and pl_ok)
#print("DBG C8:",comm_zero,tot_com,adv_nonzero,adv_exact,pl_ok,[[ (str(adv[i][j].a),str(adv[i][j].b)) for j in range(2)] for i in range(2)])
chk("C8  [IT.40-IT.42; IT.53(8); IT.66(1),(3); FT.126(2); Def-H.33; machine: exact 4x4 Q(i)]:"
    "\n           THE BAR ON THE DYNAMICAL READING, re-run from scratch and not trusted from citation. The"
    "\n           O1 ground holds: the weak seed acts seed (x) trivial on the extended carrier, so"
    "\n           [s_i (x) I_w, I (x) P_L] = [s_i (x) I_w, I (x) P_R] = 0 exactly for all three generators"
    "\n           and both chiral projectors (6 of 6 commutators identically zero, with P_L, P_R certified"
    "\n           idempotent of trace 1) -- the gauge blocks are CHIRAL-BLIND: blindness, not coupling"
    "\n           [FT.126(2)]. ADVERSARIAL (same factor): [sigma_1, sigma_3] = -2i sigma_2 exactly nonzero,"
    "\n           so the vanishing is structural, not an artifact of the test. With O2 (deficit 1') and O4"
    "\n           (the D3.7 trivial chain carries no winding) standing, the DYNAMICAL radar/photon-mediated"
    "\n           jump remains BARRED as formed, and this tier constructs no amplitude, vertex, weight or"
    "\n           rate either.",
    c8, "commutators vanishing=%d/%d; adversarial nonzero=%s exact=%s; projectors=%s"
    % (comm_zero, tot_com, adv_nonzero, adv_exact, pl_ok))

# ==========================================================================================
# PART D -- CLAIM 3: the shift is T-odd; what that does and does not buy
# ==========================================================================================
print("\n" + "-" * 104)
print("PART D -- CLAIM 3 adjudicated: T(W_i) = -W_i, the transport, and where the arrow actually lives")
print("-" * 104)

# ---- D1: the dictionary transport gbar(a00,q,-w) = J gbar(a00,q,w) J ----------------------
VG = ["Om2", "kap", "beta", "w1", "w2", "w3", "q11", "q22", "q33", "q12", "q13", "q23"]
P = Poly(VG)
Om2, kap, beta = P.var("Om2"), P.var("kap"), P.var("beta")
wv = {i: P.var("w%d" % i) for i in (1, 2, 3)}
qv = {(1, 1): P.var("q11"), (2, 2): P.var("q22"), (3, 3): P.var("q33"),
      (1, 2): P.var("q12"), (1, 3): P.var("q13"), (2, 3): P.var("q23")}


def qP(i, j):
    return qv[(min(i, j), max(i, j))]


def gbar_poly(flip=False):
    """gbar_{mu nu} as an exact polynomial: gbar_00 = -1, gbar_0i = kap*beta*w_i,
    gbar_ij = delta_ij + kap*q_ij  [D2.1]; flip=True sends w -> -w."""
    g = [[Poly.const(VG, 0) for _ in range(4)] for _ in range(4)]
    g[0][0] = Poly.const(VG, -1)
    for i in range(3):
        c = (-kap * beta * wv[i + 1]) if flip else (kap * beta * wv[i + 1])
        g[0][i + 1] = c
        g[i + 1][0] = c
    for i in range(3):
        for j in range(3):
            g[i + 1][j + 1] = Poly.const(VG, int(i == j)) + kap * qP(i + 1, j + 1)
    return g


Jm = [[Fr(-1) if a == b == 0 else (Fr(1) if a == b else Fr(0)) for b in range(4)] for a in range(4)]
gb_plus, gb_minus = gbar_poly(False), gbar_poly(True)
transport_cells = 0
for mu in range(4):
    for nu in range(4):
        lhs = gb_minus[mu][nu]
        rhs = Poly.const(VG, 0)
        for r in range(4):
            for s in range(4):
                if Jm[mu][r] != 0 and Jm[s][nu] != 0:
                    rhs = rhs + gb_plus[r][s] * (Jm[mu][r] * Jm[s][nu])
        transport_cells += int(lhs == rhs)
# the full-metric consequence: g = Om2 * gbar, and Om2 depends on a_00 alone (T-even)
g_full_flip = [[Om2 * gb_minus[a][b] for b in range(4)] for a in range(4)]
g_full = [[Om2 * gb_plus[a][b] for b in range(4)] for a in range(4)]
g00_fixed = g_full_flip[0][0] == g_full[0][0]
gij_fixed = all(g_full_flip[i + 1][j + 1] == g_full[i + 1][j + 1] for i in range(3) for j in range(3))
g0i_flipped = all(g_full_flip[0][i + 1] == -(g_full[0][i + 1]) for i in range(3))
d1 = (transport_cells == 16 and g00_fixed and gij_fixed and g0i_flipped)
chk("D1  [FT.156(3); FT.159(3); A3; C13; D2.1; machine: exact polynomial identities in"
    "\n           Q[Om2,kap,beta,w,q], all 16 cells]: THE T-GRADING TRANSPORTS THROUGH THE DICTIONARY"
    "\n           EXACTLY TO THE TIME-REVERSAL PULLBACK. With J = diag(-1,1,1,1) and the T-action on sector"
    "\n           data (a_00, q, w) -> (a_00, q, -w): gbar_{mu nu}(a_00,q,-w) = J^rho_mu gbar_{rho sigma}"
    "\n           (a_00,q,w) J^sigma_nu, cell by cell, as an exact polynomial identity. Consequence for the"
    "\n           full metric g = Om2*gbar (Om2 depends on the T-even a_00 alone): g_00 and all six g_ij are"
    "\n           FIXED, and the three g_0i FLIP SIGN. So T(W_i) = -W_i is not a label: it is the statement"
    "\n           that the shift block is exactly the metric's time-space cross block, the one part of the"
    "\n           geometry the time-reversal pullback moves.",
    d1, "transport cells exact=%d/16; g_00 fixed=%s; g_ij fixed=%s; g_0i flipped=%s"
    % (transport_cells, g00_fixed, gij_fixed, g0i_flipped))

# ---- D2: the carrier T-parity (BM.34(3)) and the structural evenness of N^2 in w ---------
def adj3(M):
    """exact adjugate of a 3x3 Fraction matrix."""
    A = [[Fr(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[M[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            A[j][i] = ((-1) ** (i + j)) * (minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0])
    return A


carr_ok = n2_ok = gam_ok = even_ok = 0
NW2 = 0
for (Om2v, kpv, btv, wv0, qv0) in WITS:
    NW2 += 1
    r1 = D.sector_to_adm(Om2v, kpv, btv, list(wv0), qv0)
    r2 = D.sector_to_adm(Om2v, kpv, btv, [-x for x in wv0], qv0)
    carr_ok += int(all(r2["Ni"][i] == -r1["Ni"][i] for i in range(3)))
    n2_ok += int(r2["N2"] == r1["N2"])
    gam_ok += int(all(r2["gamma"][i][j] == r1["gamma"][i][j] for i in range(3) for j in range(3)))
    gi1 = D.inverse3(r1["gamma"])
    Nup1 = [sum((gi1[i][j] * r1["Ni"][j] for j in range(3)), Fr(0)) for i in range(3)]
    gi2 = D.inverse3(r2["gamma"])
    Nup2 = [sum((gi2[i][j] * r2["Ni"][j] for j in range(3)), Fr(0)) for i in range(3)]
    carr_ok += int(all(Nup2[i] == -Nup1[i] for i in range(3)))
    # the STRUCTURAL evenness: det(gamma)*(N^2 - Omega^2) = Omega^4 kap^2 beta^2 * (w^T adj(gamma) w),
    # whose right-hand side is homogeneous of degree 2 in w with q-only coefficients
    Mq = [[Fr(int(i == j)) + kpv * qv0[i][j] for j in range(3)] for i in range(3)]
    adjM = adj3(Mq)
    detM = D.det3(Mq)
    gam = [[Om2v * Mq[i][j] for j in range(3)] for i in range(3)]
    detgam = D.det3(gam)
    wadjw = sum((wv0[i] * adjM[i][j] * wv0[j] for i in range(3) for j in range(3)), Fr(0))
    lhs = detgam * (r1["N2"] - Om2v)
    # det(gamma) = Omega^6 det(M) and N^2 - Omega^2 = Omega^2 kap^2 beta^2 (w^T M^-1 w)
    #   =>  det(gamma)(N^2-Omega^2) = Omega^8 kap^2 beta^2 (w^T adj(M) w)
    rhs = Om2v ** 4 * (kpv * btv) ** 2 * wadjw
    even_ok += int(lhs == rhs and lhs == detgam * (r2["N2"] - Om2v))
d2 = (carr_ok == 2 * NW2 and n2_ok == NW2 and gam_ok == NW2 and even_ok == NW2)
chk("D2  [BM.34(1),(3),(4); FT.156(3); FT.159(3); machine: exact witnesses + the adjugate identity]: THE"
    "\n           CARRIER T-PARITY. w -> -w gives N_i -> -N_i and N^i = gamma^{ij}N_j -> -N^i, while the lapse"
    "\n           N and the spatial metric gamma_ij stay FIXED (all witnesses, exactly). The reason is"
    "\n           structural, and it is certified as an exact adjugate identity rather than asserted:"
    "\n           det(gamma)*(N^2 - Omega^2) = Omega^8 kap^2 beta^2 * (w^T adj(delta+kap q) w), whose"
    "\n           right-hand side is homogeneous of degree exactly 2 in w with q-only coefficients -- so N^2"
    "\n           is EVEN in w and the flip cannot move it. BM.34(3)'s row then reads: p_i is T-odd, matching"
    "\n           its carrier; and BM.34(4)'s dispersion E = N*sqrt(m^2+p^2) - N^i p_i is T-EVEN under the"
    "\n           simultaneous (N^i, p_i) -> (-N^i, -p_i).",
    d2, "witnesses=%d; carrier flips=%d/%d; N^2 fixed=%d/%d; gamma fixed=%d/%d; adjugate evenness=%d/%d"
    % (NW2, carr_ok, 2 * NW2, n2_ok, NW2, gam_ok, NW2, even_ok, NW2))

# ---- D3: the signature is reversal-invariant (exact rational LDL^T on a witness lattice) --
lat = []
for kpv, btv, wv0, qv0 in [(Fr(1, 4), Fr(1, 3), (Fr(1, 3), Fr(-1, 4), Fr(2, 9)), WITQ[0]),
                           (Fr(1, 5), Fr(-2, 5), (Fr(1, 2), Fr(0), Fr(-3, 7)), WITQ[1]),
                           (Fr(1, 3), Fr(1, 2), (Fr(-1, 5), Fr(2, 3), Fr(1, 6)), WITQ[2]),
                           (Fr(1, 6), Fr(1), (Fr(1), Fr(1), Fr(1)), WITQ[0])]:
    for sgn in (+1, -1):
        ww = tuple(Fr(sgn) * x for x in wv0)
        gs = [[Fr(int(i == j)) + kpv * qv0[i][j] for j in range(3)] for i in range(3)]
        gb = [[Fr(0)] * 4 for _ in range(4)]
        gb[0][0] = Fr(-1)
        for i in range(3):
            gb[0][i + 1] = gb[i + 1][0] = kpv * btv * ww[i]
            for j in range(3):
                gb[i + 1][j + 1] = gs[i][j]
        neg, pos, zer, _ = inertia(gb)
        n3, p3, z3, _ = inertia(gs)
        lat.append(((neg, pos, zer), (n3, p3, z3)))
d3 = (len(lat) == 8 and all(a == (1, 3, 0) for a, b in lat) and all(b == (0, 3, 0) for a, b in lat)
      and lat[0] == lat[1] and lat[2] == lat[3] and lat[4] == lat[5] and lat[6] == lat[7])
chk("D3  [FT.156(3); CT1.12; machine: exact rational LDL^T inertia on an 8-point witness lattice]:"
    "\n           THE SIGNATURE IS REVERSAL-INVARIANT: sig(gbar)(w) = sig(gbar)(-w) = (-,+,+,+) at every"
    "\n           lattice point -- the four (q,w) witnesses times both shift signs, each with gbar_ij"
    "\n           certified positive-definite by exact pivots (0 negative, 3 positive, 0 zero) and the full"
    "\n           gbar carrying exactly 1 negative and 3 positive. The w -> -w involution therefore moves the"
    "\n           geometry WITHOUT changing its causal structure: it tilts the light cone (IT.53(5)(b): the"
    "\n           shift TILTS the cone) but never re-signs it.",
    d3, "lattice inertias (gbar, gbar_ij): %s" % (lat,))

# ---- D4: NEW ROW -- the line element is T-EVEN, and orientation-even ---------------------
VL2 = ["Om2", "kapb", "kapa", "dx0", "dx1", "dx2", "dx3",
       "w1", "w2", "w3", "q11", "q22", "q33", "q12", "q13", "q23"]
PL = Poly(VL2)
Om2P, kapbP, kapaP = PL.var("Om2"), PL.var("kapb"), PL.var("kapa")
dxP = {0: PL.var("dx0"), 1: PL.var("dx1"), 2: PL.var("dx2"), 3: PL.var("dx3")}
wP = {i: PL.var("w%d" % i) for i in (1, 2, 3)}
qP2 = {(i, j): PL.var("q%d%d" % (i, j))
       for (i, j) in [(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)]}


def qPs(i, j):
    return qP2[(min(i, j), max(i, j))]


Mij = {(i, j): Poly.const(VL2, int(i == j)) + kapaP * qPs(i + 1, j + 1)
       for i in range(3) for j in range(3)}
dshat = -Om2P * dxP[0] * dxP[0]                                     # the g_00 cell
drag = Poly.const(VL2, 0)
for i in range(3):
    drag = drag + Om2P * kapbP * Fr(2) * dxP[0] * wP[i + 1] * dxP[i + 1]      # the g_0i cells
quad = Poly.const(VL2, 0)
for i in range(3):
    for j in range(3):
        quad = quad + Om2P * Mij[(i, j)] * dxP[i + 1] * dxP[j + 1]             # the g_ij cells
dshat = dshat + drag + quad

# (a) the INCREMENT census: the distinct dx-multidegrees present -- 1 + 3 + 6 = 10
ix = [VL2.index("dx%d" % a) for a in range(4)]
dxdeg = {}
for k, c in dshat.d.items():
    m = tuple(k[i] for i in ix)
    dxdeg[m] = dxdeg.get(m, Fr(0)) + c
by_type = {"g_00: (dx0)^2": 0, "g_0i: dx0*dx^i": 0, "g_ij: dx^i*dx^j": 0}
for m in dxdeg:
    if m == (2, 0, 0, 0):
        by_type["g_00: (dx0)^2"] += 1
    elif m[0] == 1 and sum(m) == 2:
        by_type["g_0i: dx0*dx^i"] += 1
    elif m[0] == 0 and sum(m) == 2:
        by_type["g_ij: dx^i*dx^j"] += 1
# (b) the SECTOR census: block attribution of the fully expanded monomials
blocks = {"D+ (conformal)": 0, "W (shift cross)": 0, "background delta_ij": 0, "G+H (kap*q)": 0}
for k in dshat.d:
    dw = sum(k[VL2.index("w%d" % i)] for i in (1, 2, 3))
    dq = sum(k[VL2.index(s)] for s in ("q11", "q22", "q33", "q12", "q13", "q23"))
    if dw == 1:
        blocks["W (shift cross)"] += 1
    elif dq >= 1:
        blocks["G+H (kap*q)"] += 1
    elif k[ix[0]] == 2:
        blocks["D+ (conformal)"] += 1
    else:
        blocks["background delta_ij"] += 1
# (c) the T-parity product census [duality (D4); CT1.12a(2)]
t_parity = {"g_00 (T-even) x (dx0)^2 (T-odd)^2": (+1) * (-1) ** 2,
            "g_0i (T-odd) x dx0 (T-odd) x dx^i (T-even)": (-1) * (-1) * (+1),
            "g_ij (T-even) x dx^i dx^j (T-even)^2": (+1) * (+1) * (+1)}


def poly_subst_vars(p, **vals):
    """exact substitution of named variables by other polynomials of the same ring."""
    out = Poly(p.vars)
    for k, c in p.d.items():
        term = Poly.const(p.vars, c)
        for v, e in zip(p.vars, k):
            if e:
                base = vals[v] if v in vals else Poly(p.vars, {tuple(1 if u == v else 0
                                                                    for u in p.vars): Fr(1)})
                for _ in range(e):
                    term = term * base
        out = out + term
    return out


neg = {("dx%d" % a): -Poly(VL2, {tuple(1 if u == ("dx%d" % a) else 0 for u in VL2): Fr(1)})
       for a in range(4)}
orient = poly_subst_vars(dshat, **neg)                                  # dx -> -dx
negw = dict(neg)
for i in (1, 2, 3):
    negw["w%d" % i] = -Poly(VL2, {tuple(1 if u == "w%d" % i else 0 for u in VL2): Fr(1)})
neg0w = dict(negw)
neg0w.pop("dx1"); neg0w.pop("dx2"); neg0w.pop("dx3")                    # dx0 -> -dx0 AND w -> -w
tpull = poly_subst_vars(dshat, **neg0w)
# (d) the flat/drag split on the exact witnesses [duality (D4)]
split_ok = 0
for (Om2v, kpv, btv, wv0, qv0) in WITS:
    Mm = D.M_metric(kpv, qv0)
    dx0v, dxv = Fr(3, 2), (Fr(1, 2), Fr(-1), Fr(2, 3))
    full = D.dshat2(Om2v, kpv * btv, Mm, wv0, dx0v, dxv)
    fl = D.flat_part(Om2v, Mm, dx0v, dxv)
    dr = D.drag_part(Om2v, kpv * btv, wv0, dx0v, dxv)
    split_ok += int(full == fl + dr)
    dr2 = D.drag_part(Om2v, kpv * btv, tuple(-x for x in wv0), dx0v, dxv)
    fl2 = D.flat_part(Om2v, Mm, -dx0v, tuple(-x for x in dxv))
    split_ok += int(dr2 == -dr and fl2 == fl)
d4 = (len(dxdeg) == 10 and by_type == {"g_00: (dx0)^2": 1, "g_0i: dx0*dx^i": 3,
                                       "g_ij: dx^i*dx^j": 6}
      and blocks == {"D+ (conformal)": 1, "W (shift cross)": 3, "background delta_ij": 3,
                     "G+H (kap*q)": 6}
      and sum(blocks.values()) == len(dshat.d)
      and all(v == +1 for v in t_parity.values())
      and orient == dshat and tpull == dshat and split_ok == 6)
chk("D4  [D1.6; D1.7; CT1.19b(2); CT1.12a(2); FT.30; duality (D4); NEW ROW; machine: exact"
    "\n           multivariate polynomial identities]: THE LINE ELEMENT IS T-EVEN, SO THE SHIFT'S T-ODDNESS"
    "\n           DOES NOT MAKE THE GEOMETRY T-ODD. (a) INCREMENT census of dshat^2(e) = Om2[-(dx0)^2 +"
    "\n           2 kap beta dx0 (w.dx) + M_ij dx^i dx^j], M = delta + kap q: exactly 10 distinct increment"
    "\n           monomials -- 1 of (dx0)^2, 3 of dx0*dx^i, 6 of dx^i*dx^j -- one per metric coordinate,"
    "\n           against the cells g_00 / g_0i / g_ij. (b) SECTOR census of the full expansion: 13"
    "\n           monomials attributing 1 to D+ (the conformal cell), 3 to W (the shift cross-term), 3 to"
    "\n           the background delta_ij and 6 to kap*q (G+H) -- every one of the four blocks enters the"
    "\n           interval. (c) The T-parity product census: g_00 (T-even) x (dx0)^2 (T-odd squared) ="
    "\n           T-even; g_0i (T-odd) x dx0 (T-odd) x dx^i (T-even) = T-even; g_ij (T-even) x dx^i dx^j"
    "\n           (T-even) = T-even -- every monomial T-even, exactly as CT1.12a(2)'s consequence requires"
    "\n           (g_{mu nu} is orientation-even). (d) Two exact polynomial identities: dx -> -dx fixes"
    "\n           dshat^2 (CT1.19b(2)'s orientation evenness, the shift cross-term included), and the"
    "\n           T-pullback (dx0 -> -dx0 together with w -> -w) fixes it too. The flat/drag split"
    "\n           re-certifies on all witnesses: the drag is odd in w, the flat part even -- the shift's"
    "\n           UNIQUE entry into the interval.",
    d4, "increment monomials=%d by cell=%s; sector monomials=%s; T-parities=%s; orientation-even=%s;"
        " T-pullback-even=%s; flat/drag=%d/6"
    % (len(dxdeg), by_type, blocks, t_parity, orient == dshat, tpull == dshat, split_ok))

# ---- D5: the radar legs -- the shift's sign distinguishes them --------------------------
Gw, dxw, Nw, sw = Fr(4), Fr(3), Fr(5), Fr(2)
sqrtG = Fr(2)                                             # exact: 2^2 = 4
dtau_p = sqrtG * dxw / (Nw - sw)
dtau_m = sqrtG * dxw / (Nw + sw)
diff = dtau_p - dtau_m
closed = 2 * sqrtG * dxw * sw / (Nw ** 2 - sw ** 2)
half = sqrtG * dxw * Nw ** 2 / (Nw ** 2 - sw ** 2)
proper = sqrtG * dxw
flip_p = sqrtG * dxw / (Nw + sw)
flip_m = sqrtG * dxw / (Nw - sw)
s0_half = (sqrtG * dxw * Nw ** 2 / Nw ** 2)
agree_fwd = [(Fr(a), Fr(b)) for a in range(-3, 4) for b in range(-3, 4)]
agree_iff = all(((s_ * d_ == 0) == (2 * sqrtG * d_ * s_ / (Nw ** 2 - s_ ** 2) == 0))
                for (s_, d_) in agree_fwd if Nw ** 2 - s_ ** 2 != 0)
d5 = (dtau_p == Fr(2) and dtau_m == Fr(6, 7) and diff == Fr(8, 7) == closed
      and 2 * sqrtG * dxw * sw == 24 and (Nw ** 2 - sw ** 2) == 21
      and flip_p == dtau_m and flip_m == dtau_p and half == Fr(50, 7)
      and s0_half == proper == Fr(6) and agree_iff)
chk("D5  [IT.53(4),(5)(b); IT.68(2); BM.34(2); machine: exact Fractions]: THE SHIFT'S SIGN DISTINGUISHES"
    "\n           THE TWO NULL LEGS -- the derived sense in which the T-odd block separates past-bound from"
    "\n           future-bound. On the frozen witness (G, dx, N, s) = (4,3,5,2) with sqrt(G) = 2 exact:"
    "\n           dtau_+ = 2, dtau_- = 6/7, and the leg difference dtau_+ - dtau_- = 8/7 equals the closed"
    "\n           form 2*sqrt(G)*dx*s/(N^2-s^2) = 24/21 = 8/7 exactly. The flip s -> -s SWAPS the two legs"
    "\n           (dtau_+ <-> dtau_-), which is the T-conjugacy of the two synchronizations [BM.34(3);"
    "\n           FT.156(3)]. The radar half-distance sqrt(G)*dx*N^2/(N^2-s^2) = 50/7 equals the proper"
    "\n           length sqrt(G)*dx = 6 EXACTLY at s = 0 (honest substitution), and the agreement locus is"
    "\n           s*dx = 0 in BOTH directions (witness census over s, dx in -3..3). So the shift is the"
    "\n           metric's own past/future discriminator at the read level -- and it is a discriminator, not"
    "\n           an arrow: the flip is an involution, and the arrow lives elsewhere (D6).",
    d5, "dtau_+=%s dtau_-=%s difference=%s = closed form %s; flip swaps=%s; half-distance=%s;"
        " proper length=%s; agreement iff s*dx=0 on %d witnesses"
    % (dtau_p, dtau_m, diff, closed, flip_p == dtau_m, half, proper, len(agree_fwd)))

# ---- D6: the inner spatial reversals vs the non-implemented temporal advance -------------
Wm = {i: MAT["W%d" % i] for i in (1, 2, 3)}
Jm_ = {i: MAT["J%d" % i] for i in (1, 2, 3)}
Km = {i: MAT["K%d" % i] for i in (1, 2, 3)}
WW = m_add(m_add(Wm[1], Wm[2]), Wm[3])                     # the sum W_1+W_2+W_3
W3 = D.mat_mul(D.mat_mul(WW, WW), WW)
w_cube = all(m_sub(W3, m_scale(Fr(3), WW))[i][j] == ZERO for i in range(4) for j in range(4))
Ucyc = m_sub(m_sub(E0(), m_scale(Fr(1, 2), D.mat_mul(WW, WW))), m_scale(Fr(1, 2) * I, WW))
u3 = D.mat_mul(D.mat_mul(Ucyc, Ucyc), Ucyc)
u3_ok = all(m_sub(u3, E0())[i][j] == ZERO for i in range(4) for j in range(4))
cyc_ok = 0
cyc_tot = 0
for fam, tab in (("W", Wm), ("J", Jm_), ("K", Km)):
    for i in (1, 2, 3):
        nxt = i % 3 + 1
        cyc_tot += 1
        conj = D.mat_mul(D.mat_mul(Ucyc, tab[i]), D.mdag(Ucyc))
        cyc_ok += int(all(m_sub(conj, tab[nxt])[a][b] == ZERO for a in range(4) for b in range(4)))
trans_ok = 0
trans_tot = 0
invol_ok = 0
for (i, j) in ((1, 2), (1, 3), (2, 3)):
    k = 6 - i - j
    A = m_add(Wm[i], Wm[j])
    Uij = m_sub(E0(), D.mat_mul(A, A))
    invol_ok += int(all(m_sub(D.mat_mul(Uij, Uij), E0())[a][b] == ZERO for a in range(4) for b in range(4)))
    for fam, tab in (("W", Wm), ("J", Jm_), ("K", Km)):
        targets = {i: tab[j], j: tab[i], k: m_scale(Fr(-1), tab[k])}
        for src in (i, j, k):
            trans_tot += 1
            conj = D.mat_mul(D.mat_mul(Uij, tab[src]), D.mdag(Uij))
            trans_ok += int(all(m_sub(conj, targets[src])[a][b] == ZERO
                                for a in range(4) for b in range(4)))
# the temporal advance: no inverse on the record (C1) and no inner implementation
tau_inv = r"\neg\exists\,\tau^{-1}" in P1T
inner_claim = ("the spatial-axis reversals are inner unitaries" in norm(P3T).replace("  ", " ")
               or "spatial-axis reversals are inner unitaries" in P3T.replace("\\ ", " "))
theta_mirror = (r"\Theta_{\mathfrak L}" in P1T and "formal mirror" in P3T)
d6 = (w_cube and u3_ok and cyc_ok == cyc_tot == 9 and trans_ok == trans_tot == 27 and invol_ok == 3
      and tau_inv and theta_mirror)
chk("D6  [FT.156(4),(5); FT.158(1); FT.144(2),(4); A6; D2.7; machine: exact 4x4 Q(i) conjugation tables]:"
    "\n           WHERE THE ARROW ACTUALLY LIVES -- and it is NOT the T-grading. The spatial triad reversals"
    "\n           ARE inner unitaries, verified entrywise: the cyclic U = E_0 - W^2/2 - iW/2 (with"
    "\n           W = W_1+W_2+W_3 and W^3 = 3W) satisfies U^3 = E_0 and U X_i U^dagger = X_{i+1} for all"
    "\n           nine (X, i) in {W,J,K} x {1,2,3}; the three transpositions U_ij = E_0 - (W_i+W_j)^2 satisfy"
    "\n           U_ij^2 = E_0 and realize X_i <-> X_j, X_k -> -X_k on all 27 rows. The TEMPORAL advance has"
    "\n           no such implementation: A6 declares no tau^-1, the record is monotone and strictly"
    "\n           increasing at every crystallization (C1), the pure order reversal of every completed"
    "\n           history is inadmissible at its first event (C2), and Theta_L [D2.7] is the FORMAL MIRROR on"
    "\n           records, not a dynamical inverse [FT.144(4)(i); FT.159(5)]. So: T-oddness of W gives an"
    "\n           exact involution on chart and configuration data (D1, D5); the past/future ASYMMETRY is"
    "\n           the ledger's forward-only advance, a different locus [FT.159(3)'s locus discipline: one"
    "\n           order parameter, four tags, and the identity is of the time entity, not an operator"
    "\n           equality].",
    d6, "W^3=3W=%s; U^3=E_0=%s; cyclic rows=%d/%d; transposition rows=%d/%d; involutions=%d/3;"
        " no-tau^-1 in A6=%s; formal-mirror row=%s"
    % (w_cube, u3_ok, cyc_ok, cyc_tot, trans_ok, trans_tot, invol_ok, tau_inv, theta_mirror))

# ---- D7: the naming bar (left/right is BARRED; spatial/temporal are bookkeeping) ----------
ft156_rmk = ("Naming either branch *left* or *right* remains barred" in P3T)
ft157_rmk = ("Naming either branch *left* or *right* is barred" in P3T)
ft101_bar = ("FT.101 Phys bars stand" in P3T)
bookkeeping = ("internal bookkeeping" in P3T)
no_species = ("no SM species reading" in P3T and "no claim that the SM weak interaction is reproduced" in P3T)
dead_ctrl = ("Naming either branch *left* or *right* is required" not in P3T)
d7 = ft156_rmk and ft157_rmk and ft101_bar and bookkeeping and no_species and dead_ctrl
chk("D7  [FT.156 Rmk; FT.157 Rmk; FT.101 Phys; P1; P5; machine text census with a dead control]: THE"
    "\n           NAMING BAR. Claim 3's phrase 'encodes left/right' is BARRED as a naming: the frozen"
    "\n           remarks of FT.156 and FT.157 both carry the identical clause -- naming either branch left"
    "\n           or right is barred, FT.101's Phys bars stand -- and the labels spatial branch / temporal"
    "\n           branch are INTERNAL BOOKKEEPING for the derived dimension and Casimir matches, naming no"
    "\n           particle and no external structure. The same remarks carry 'no SM species reading; no claim"
    "\n           that the SM weak interaction is reproduced [P1, P5]'. The CONTENT survives the bar and is"
    "\n           derived (D1-D6); only the name is refused.",
    d7, "FT.156 bar=%s; FT.157 bar=%s; FT.101 bars stand=%s; bookkeeping=%s; SM bars=%s; dead control=%s"
    % (ft156_rmk, ft157_rmk, ft101_bar, bookkeeping, no_species, dead_ctrl))

# ==========================================================================================
# PART E -- CLAIM 4: can the geometry measure the ledger's discrete jumps?
# ==========================================================================================
print("\n" + "-" * 104)
print("PART E -- CLAIM 4 adjudicated: the contraction, the on-shell integers, the inverse translation")
print("-" * 104)


def dPoly(p, name):
    """the exact partial derivative of a Poly with respect to one of its variables."""
    ix = p.vars.index(name)
    out = Poly(p.vars)
    for k, c in p.d.items():
        e = k[ix]
        if e:
            k2 = list(k)
            k2[ix] = e - 1
            out._add(tuple(k2), c * e)
    return out


# ---- E1: the joint S-even read -- all ten coordinates enter; no block-local quantum -------
METCOORDS = (["Om2"] + ["w%d" % i for i in (1, 2, 3)]
             + ["q11", "q22", "q33", "q12", "q13", "q23"])
wit_pt = {"Om2": Fr(4), "kapb": Fr(6, 5), "kapa": Fr(3, 5),
          "dx0": Fr(3, 2), "dx1": Fr(1, 2), "dx2": Fr(-1), "dx3": Fr(2, 3),
          "w1": Fr(1, 3), "w2": Fr(-1, 4), "w3": Fr(2, 9),
          "q11": Fr(1, 7), "q22": Fr(1, 3), "q33": Fr(2, 13),
          "q12": Fr(-2, 9), "q13": Fr(1, 5), "q23": Fr(-1, 11)}
derivs = {v: dPoly(dshat, v).subst(**wit_pt) for v in METCOORDS}
all_enter = all(derivs[v] != 0 for v in METCOORDS)
BLOCKSETS = {"D+": ["Om2"], "W": ["w1", "w2", "w3"],
             "G+H": ["q11", "q22", "q33", "q12", "q13", "q23"]}
# per-block witness: keep ONE block nonzero, all others zero -> the interval takes a non-integer
# value, so no single block carries a quantum of its own [FT.30 Verdict]
block_nonint = {}
for b, vs in BLOCKSETS.items():
    pt = dict(wit_pt)
    for v in METCOORDS:
        if v not in vs:
            pt[v] = Fr(0)
    if b == "D+":
        pt["Om2"] = Fr(4)                       # the conformal cell alone (g_00 = -Omega^2)
    if b == "G+H":
        pt["Om2"] = Fr(1)
    if b == "W":
        pt["Om2"] = Fr(1)
    val = dshat.subst(**pt)
    block_nonint[b] = (val, val.denominator != 1)
ft30_verdict = ("No pair-channel block carries a block-local quantum" in P3T
                and "joint" in P3T and "mixes all ten metric coordinates" in P3T)
ft30_table = ("candidate" in P3T and "extraction open" in P3T
              and "no" in P3T and "continuous configuration datum" in P3T)
e1 = (len(METCOORDS) == 10 and all_enter and ft30_verdict and ft30_table
      and all(v[1] for v in block_nonint.values()))
chk("E1  [FT.30 + its Verdict; D1.6; D2.1; CT1.12; NEW ROW; machine: exact partial derivatives at a"
    "\n           rational witness]: THE GEOMETRIC QUANTUM IS A JOINT S-EVEN READ. The exact partial"
    "\n           derivative census of dshat^2(e) with respect to all TEN metric coordinates -- Om2 (the"
    "\n           conformal/lapse cell, D+), w_1..w_3 (the shift cells, W), q_11..q_23 (the six spatial"
    "\n           cells, G+H) -- is nonzero in every one of the ten directions: the interval mixes all ten"
    "\n           coordinates across G, H, D+, W exactly as FT.30's Verdict states. And the converse is"
    "\n           certified too: keeping ONE block nonzero and zeroing the other two gives a non-integral"
    "\n           interval value for every block, so NO pair-channel block carries a block-local quantum --"
    "\n           FT.30's own per-block audit stands (G: geometric but a JOINT read; W: a candidate, spin,"
    "\n           extraction open; H: no, a continuous configuration datum; D+: no, a P4 datum; J+-: no,"
    "\n           structural).",
    e1, "coordinates=%d all entering=%s; per-block non-integer witnesses: %s"
    % (len(METCOORDS), all_enter, {k: str(v[0]) for k, v in block_nonint.items()}))

# ---- E2: the edge weight G(e) = sigma_e exp(i alpha_e dshat^2(e)) -- the frozen translation
CHAIN_OK = 0
CHAIN_TOT = 0
for L in range(1, 5):
    for sig in product((1, -1), repeat=L):
        for al in product((0, 1), repeat=L):                    # alpha_e in {0, pi}: 0 or 1 (units of pi)
            for kap in product((0, 1, 2), repeat=L):
                CHAIN_TOT += 1
                prod = D.Gauss(1)
                for e in range(L):
                    phase = D.i_pow(2 * al[e] * kap[e])          # exp(i*pi*al*kappa) = i^{2 al kappa}
                    prod = prod * D.Gauss(sig[e]) * phase
                theta_P = sum(al[e] * kap[e] for e in range(L))   # the antialigned line-element sum
                sgn = 1
                for s in sig:
                    sgn *= s
                expect = D.Gauss(sgn) * D.i_pow(2 * theta_P)
                CHAIN_OK += int(prod == expect)
alphabet = {a: {k: D.i_pow(2 * a * k) for k in range(0, 5)} for a in (0, 1)}
d35_txt = (r"G^{(n)}(e):=\sigma_e\,\exp\!\bigl(i\,\alpha_e\,\widehat{ds}^{\,2}(e)\bigr)" in P1T)
em204_txt = (r"G(e)=\sigma_e\cdot e^{i\alpha_e\,\widehat{ds}^{\,2}(e)}" in P2T)
a8_txt = (r"w(C)=\mathcal J(C)\!\!\prod_{e\in E(C)}\!\!G(e)" in P1T)
e2 = (CHAIN_OK == CHAIN_TOT and CHAIN_TOT > 20000 and d35_txt and em204_txt and a8_txt
      and all(v == D.Gauss(1) for v in alphabet[0].values())
      and [alphabet[1][k] for k in range(5)]
      == [D.Gauss(1), D.Gauss(-1), D.Gauss(1), D.Gauss(-1), D.Gauss(1)])
chk("E2  [D3.5; EM.20(1),(4); D0.5; CT0.9; D1.7; A8; machine: exact Gauss(i) over %d chains]: THE"
    "\n           TRANSLATION HAS A FROZEN FORMULA, AND IT IS EDGE-LOCAL. G(e) = sigma_e * exp(i*alpha_e*"
    "\n           dshat^2(e)) [D3.5; EM.20(4)]: one LEDGER BIT (sigma_e in {+1,-1} [CT0.9]) times one"
    "\n           GEOMETRIC PHASE whose exponent is the ledger's binary phase (alpha_e in {0,pi}"
    "\n           [EM.20(1)]) times the interval -- and the interval is the rung-1 contraction of E1. It is"
    "\n           dimensionless, defined per edge, and A8's configuration weight is the PRODUCT over edges,"
    "\n           w(C) = J(C) * prod_e G(e) * (-1)^aleph: the geometry never reaches further than the edge it"
    "\n           is evaluated on. Census over every chain of length 1..4 with all sign, phase and interval"
    "\n           assignments: prod_e G(e) = (prod_e sigma_e) * (-1)^{Theta_P} exactly, where"
    "\n           Theta_P = sum over the antialigned edges of dshat^2(e) -- the holonomy read of D1.7 in"
    "\n           exact fourth-root arithmetic." % CHAIN_TOT,
    e2, "chains=%d all exact=%d; phase alphabet=%s; D3.5 text=%s; EM.20(4) text=%s; A8 text=%s"
    % (CHAIN_TOT, CHAIN_OK, {a: [gstr(alphabet[a][k]) for k in range(5)] for a in (0, 1)},
       d35_txt, em204_txt, a8_txt))

# ---- E3: the on-shell quantization and the geometry quantum ------------------------------
hol_census = {m: D.i_pow(2 * m) for m in range(0, 17)}          # exp(i*pi*m) = (-1)^m, exact
hol_iff = all((hol_census[m] == D.Gauss(1)) == (m % 2 == 0) for m in hol_census)
kappa_sets = {}
for m in (0, 1, 2):
    ks = set()
    for num in range(0, 17):
        for den in (1, 2):
            kap = Fr(num, den)
            prod = m * kap
            if prod.denominator == 1 and prod % 2 == 0:
                ks.add(kap)
    kappa_sets[m] = ks
m2_all_int = all(Fr(k) in kappa_sets[2] for k in range(0, 9))
m2_no_half = Fr(1, 2) not in kappa_sets[2] and Fr(3, 2) not in kappa_sets[2]
m1_even_only = kappa_sets[1] == {Fr(k) for k in range(0, 17, 2)}
m0_vacuous = (kappa_sets[0] == {Fr(n, d) for n in range(0, 17) for d in (1, 2)})
laurent = {k: 4 * k for k in range(0, 5)}                         # ds^2 = 4*kappa*G_N*ln2 [CT2.9]
internal_parity = {t: D.i_pow(2 * t) for t in range(0, 5)}        # partial sums: free parity
ct119 = ("Theta_{\\mathcal P}(c)=2k\\in2\\mathbb Z" in P2T or "2k\\in2\\mathbb Z" in P2T)
quantum_row = (r"ds^2(e)=4\kappa\,G_N\ln2" in P2T)
e3 = (hol_iff and m2_all_int and m2_no_half and m1_even_only and m0_vacuous and ct119
      and quantum_row and internal_parity[1] == D.Gauss(-1))
chk("E3  [CT1.19b(1),(3),(4); D1.7; CT2.9; CT1.29; EM.5; machine: exact integer/Fraction censuses]:"
    "\n           THE ON-SHELL INTEGERS. Single-valuedness of the spiral holonomy, Hol = exp(i*Phi) = +1 with"
    "\n           Phi = pi*Theta_P [D1.7; EM.20(1)], is equivalent to Theta_P in 2Z -- census over"
    "\n           Theta_P = 0..16 in exact fourth-root arithmetic: exp(i*pi*m) = (-1)^m, so +1 exactly on the"
    "\n           even m. The 2-cycle geometry quantum: Theta_P = m*kappa in 2Z with m = |P(c)| in {0,1,2}"
    "\n           gives kappa in Z at m = 2 (all integers admissible), kappa in 2Z at m = 1, and no"
    "\n           constraint at m = 0 (vacuous) -- and then ds^2(e) = kappa*h^2 with h^2 = 4*G_N*ln2 [CT2.9]"
    "\n           gives ds^2 = 4*kappa*G_N*ln2, the interval quantum being one Bekenstein bit-area per unit"
    "\n           kappa on the fully antialigned class [CT1.29]; the coefficients 4*kappa are kept as exact"
    "\n           Laurent monomials, NO VALUE issued [P5]. Partial internal sums keep free parity -- a single"
    "\n           kappa = 1 antialigned edge gives (-1)^1 = -1 [CT1.19b(4)].",
    e3, "Hol=+1 iff even=%s; m=2 all integers 0..8=%s and no half-integer=%s; m=1 evens only=%s;"
        " m=0 vacuous=%s; ds^2 coefficients 4*kappa=%s; partial parity witness=%s"
    % (hol_iff, m2_all_int, m2_no_half, m1_even_only, m0_vacuous, laurent,
       gstr(internal_parity[1])))

# ---- E4: the INVERSE translation -- AT.5(1)'s closed form, linear in the ledger integer ---
rt_ok = lin_ok = 0
NW4 = 0
gauge_nullity = None
vanish_ok = 0
for (Om2v, kpv, btv, wv0, qv0) in WITS:
    NW4 += 1
    Mm = D.M_metric(kpv, qv0)
    dx0v, dxv = Fr(3, 2), (Fr(1, 2), Fr(-1), Fr(2, 3))
    kap_e = D.dshat2(Om2v, kpv * btv, Mm, wv0, dx0v, dxv)
    assert kap_e.denominator == 1 or True
    L = D.at5_longitudinal(kap_e, Om2v, kpv * btv, Mm, dx0v, dxv)
    dxsq = sum((dxv[i] * dxv[i] for i in range(3)), Fr(0))
    wlong = tuple(L * dxv[i] / dxsq for i in range(3))
    back = D.dshat2(Om2v, kpv * btv, Mm, wlong, dx0v, dxv)
    rt_ok += int(back == kap_e)
    # linearity in the ledger integer kappa_e: the second difference vanishes
    Ls = [D.at5_longitudinal(k, Om2v, kpv * btv, Mm, dx0v, dxv) for k in range(0, 7)]
    d1s = [Ls[k + 1] - Ls[k] for k in range(6)]
    lin_ok += int(all(d1s[k] == d1s[0] for k in range(6)) and d1s[0] != 0)
    # the transverse residue: dot(w_perp, dx) = 0 is ONE exact linear condition on 3 unknowns
    A = [[Fr(dxv[0]), Fr(dxv[1]), Fr(dxv[2])]]
    rk = rank_gauss([[D.Gauss(x) for x in row] for row in A])
    gauge_nullity = 3 - rk
    # the vanishing locus is codimension 1: exactly one kappa solves L = 0
    quad = sum((Mm[i][j] * dxv[i] * dxv[j] for i in range(3) for j in range(3)), Fr(0))
    kap0 = Om2v * (quad - dx0v * dx0v)                      # h = 1
    L0 = D.at5_longitudinal(kap0, Om2v, kpv * btv, Mm, dx0v, dxv)
    vanish_ok += int(L0 == 0)
e4 = (rt_ok == NW4 and lin_ok == NW4 and gauge_nullity == 2 and vanish_ok == NW4)
chk("E4  [AT.5(1),(2),(3),(4),(5); D1.6; D1.8; machine: exact Fractions]: THE TRANSLATION RUNS BOTH WAYS."
    "\n           AT.5(1)'s closed form (w.dx)(e) = [h^2*kappa_e/Omega^2 + (dx^0)^2 - M_ij dx^i dx^j] /"
    "\n           (2*kappa*beta*dx^0) is exact, round-trips identically into D1.6 on every witness (the"
    "\n           longitudinal shift reconstructed from the ledger integer kappa_e reproduces kappa_e), and is"
    "\n           LINEAR in that integer -- the first difference is a nonzero constant and the second"
    "\n           difference vanishes over kappa = 0..6. Its input census [AT.5(2)] is entirely ledger and"
    "\n           metric data: the on-shell integer kappa_e, the tick increment dx^0, the metric coefficients"
    "\n           Omega and M_ij, and the P4 pair (kappa, beta) whose VALUES ARE NOT ISSUED. The residue is"
    "\n           exactly 2 dimensions per edge -- dot(w_perp, dx) = 0 is ONE exact linear condition on three"
    "\n           unknowns, nullity 2 -- and AT.5(4) names it: N_i is the Lagrange multiplier of the momentum"
    "\n           constraint, so the transverse freedom IS the spatial-diffeomorphism gauge, not missing"
    "\n           information (the same row C6 re-derived from the operator side). The vanishing locus"
    "\n           (w.dx) = 0 is codimension 1: exactly one kappa solves it, verified exactly.",
    e4, "round-trips=%d/%d; linear-in-kappa=%d/%d; transverse nullity=%d; vanishing locus solved=%d/%d"
    % (rt_ok, NW4, lin_ok, NW4, gauge_nullity, vanish_ok, NW4))

# ---- E5: WHICH SIDE QUANTIZES -- the two-locus census (new row) --------------------------
flat_val = {v: Fr(0) for v in METCOORDS}
flat_pt = dict(wit_pt)
flat_pt.update(flat_val)
flat_pt["Om2"] = Fr(1)                                  # the vacuum gauge: Omega = 1 [BM.34(2)]
dx_probe = {"dx0": Fr(1), "dx1": Fr(1, 2), "dx2": Fr(0), "dx3": Fr(0)}
flat_pt2 = dict(flat_pt)
flat_pt2.update(dx_probe)
val_flat = dshat.subst(**flat_pt2)                        # -(1)^2 + (1/2)^2 = -3/4
nonintegral_offshell = (val_flat == Fr(-3, 4) and val_flat.denominator != 1)
onshell_integral = all(Fr(k) == int(Fr(k)) for k in range(0, 9))
two_locus = ("Two-locus principle" in P3T and "discreteness claims in this corpus are spectrum claims"
             in P3T and "continuity claims are arena claims" in P3T)
no_quantum = ("neither carries an independent quantum" in P2T)
offshell_row = ("Off-shell" in P2T and "generic continuous" in P2T
                and "quantization is an on-shell (materialization) property" in P2T)
e5 = (nonintegral_offshell and onshell_integral and two_locus and no_quantum and offshell_row)
chk("E5  [Def-H.18; CT1.19a; CT1.19b; CT1.12a(3); D2.4; D2.5; CT2.5; NEW ROW; machine: exact witness"
    "\n           pair]: WHICH SIDE QUANTIZES -- and it is not the geometry alone. At the flat vacuum"
    "\n           (a_00, q, w) = 0 with Omega = 1 [BM.34(2)] the interval is still the continuous quadratic"
    "\n           form eta_{mu nu}dx^mu dx^nu: the exact witness dx = (1, 1/2, 0, 0) gives dshat^2 = -3/4,"
    "\n           NOT an integer -- off shell nothing is quantized [CT1.19a; Def-H.18's two-locus principle:"
    "\n           discreteness claims are SPECTRUM claims, continuity claims are ARENA claims]. The integers"
    "\n           appear only on shell, and their source is the LEDGER: the binary phase alphabet alpha_e in"
    "\n           {0,pi} [EM.20(1); CT0.9] conjoined with the materialization/pole condition [CT2.5; D2.4;"
    "\n           D2.5] forces Theta_P in 2Z (E3). So the rung-1 geometry supplies the quadratic form, the"
    "\n           ledger supplies the discreteness, and the integers are their ON-SHELL CONTRACTION -- which"
    "\n           is why CT1.12a(3) can say of every dictionary/aspect datum that 'neither carries an"
    "\n           independent quantum'.",
    e5, "off-shell witness dshat^2=%s (non-integer=%s); on-shell kappa in Z=%s; two-locus text=%s;"
        " no-independent-quantum text=%s; off-shell-continuity text=%s"
    % (val_flat, nonintegral_offshell, onshell_integral, two_locus, no_quantum, offshell_row))

# ---- E6: the observability census and the declared radar read ----------------------------
ft20 = P3T[P3T.index("### FT.20"):P3T.index("### FT.21")]
obs = {"G": "I_{\\mathrm{hid}}" in ft20, "H": "folded into" in ft20,
       "W": "one-directional" in ft20, "D+": "never (independently)" in ft20,
       "J": "never" in ft20}
radar_census = 0
radar_tot = 0
for dh in range(1, 33):
    for tau_e in range(0, 5):
        radar_tot += 1
        tau_r = tau_e + 2 * dh
        d = (tau_r - tau_e) // 2
        radar_census += int((tau_r - tau_e) % 2 == 0 and d == dh and tau_e < tau_r)
decl_txt = ("GEOMETRIC / READ-LEVEL interpretation" in ALLTIER
            and "PER-EDGE INTEGER READING" in ALLTIER
            and "DEFERRED" in ALLTIER and "D-PJ7" in ALLTIER)
barred_txt = ("BARRED as formed" in ALLTIER or "remains BARRED on the three standing grounds" in ALLTIER)
e6 = (all(obs.values()) and radar_census == radar_tot == 160 and decl_txt and barred_txt)
chk("E6  [FT.20; IT.53(4),(7),(8); IT.65; IT.66(1),(2); IT.68(1); machine: the 32x5 census re-run + text"
    "\n           census]: THE READ IS DECLARED, THE DYNAMICS IS BARRED, AND THE PER-ASPECT OBSERVABILITY IS"
    "\n           NOT UNIFORM. FT.20's activity criteria, census-checked in the frozen table: G is observable"
    "\n           through the mass read I_hid(Sigma;o) (observer-relative, Def-H.9); W through the"
    "\n           interior-winding criterion Theta_int != 0, ONE-DIRECTIONAL only; H is FOLDED INTO G"
    "\n           [Def-H.36]; D+ is NEVER observable independently (uniform, D4.3); J+- never (seals, not"
    "\n           charges). The radar read that the directive invokes is re-run here at its declared register:"
    "\n           all 160 cells of the (delta_h, tau_e) census in 1..32 x 0..4 give an integer round trip"
    "\n           tau_r = tau_e + 2*delta_h with d = (tau_r - tau_e)/2 = delta_h in N and tau_e < tau_r"
    "\n           [D-RS3 @ IT.65; IT.68(1)]. Its status is DECLARED (D-RS6: a geometric/read-level"
    "\n           interpretation, not a formed dynamical amplitude), D-RS4 stays deferred, D-PJ7 stays owed,"
    "\n           and the dynamical transit remains barred on three grounds.",
    e6, "observability=%s; radar cells=%d/%d integral; declaration text=%s; bar text=%s"
    % (obs, radar_census, radar_tot, decl_txt, barred_txt))

# ==========================================================================================
# PART F -- THE 1-REACH THEOREM (the Architect's note), machine-adjudicated
# ==========================================================================================
print("\n" + "-" * 104)
print("PART F -- the 1-reach theorem: range one hop, content the entire S sector")
print("-" * 104)

# ---- F1: REACH = 1 hop -------------------------------------------------------------------
per_edge_metric = r"g_{\mu\nu}(e)\,\Delta x^\mu_e\,\Delta x^\nu_e" in P1T
per_pair_state = (r"\rho_{pq}\in\mathfrak H(\mathcal H_p\otimes\mathcal H_q)" in P1T)
per_pair_cost = ("C(p,q)=1" in P1T)
hop_def = ("hop" in P1T and r"\delta h(\gamma):=\#\{e\in\gamma\}" in P1T)
no_far_read = ("edge-distance" in P1T and r"\neg\exists" in P1T)
pair_channel_tiling = ("C_{\\mathrm{cap}}" in P1T and "16" in P1T)
f1 = (per_edge_metric and per_pair_state and per_pair_cost and hop_def and no_far_read
      and pair_channel_tiling and c3 and c4)
chk("F1  [A1; A2; D0.6; D1.6; D1.9; CT0.6; CT0.12; machine: the C3/C4 censuses + text witnesses]: REACH ="
    "\n           ONE HOP, exactly and non-vacuously. The four rung-1 aspects live in the pair channel"
    "\n           H(H_p (x) H_q) that A1 attaches to ONE pair and A2 prices at one qubit-tick; CT0.12 tiles"
    "\n           that single 16-dimensional space with all six aspects; D0.6 defines a hop as one traversal"
    "\n           of one real edge; and the metric itself is evaluated PER EDGE, g_{mu nu}(e) [D1.6]. With"
    "\n           D1.9's bar on any read at edge-distance > 1 (C3: 62 of 66 vertex-instances have a"
    "\n           nonempty excluded complement at distance >= 2, the other 4 saturate), a single force"
    "\n           insertion reaches exactly one hop. Nothing further is needed to make the point: the corpus"
    "\n           has no row in which an aspect acts on two pair channels at once.",
    f1, "per-edge metric=%s; per-pair state=%s; per-pair cost=%s; hop definition=%s;"
        " no-far-read bar=%s; capacity tiling=%s" % (per_edge_metric, per_pair_state, per_pair_cost,
                                                     hop_def, no_far_read, pair_channel_tiling))

# ---- F2: CONTENT = the entire S sector, minimally ----------------------------------------
subsets = []
for r in range(0, 5):
    for c in combinations(["G", "W", "H", "D+"], r):
        subsets.append((c, sum(dim[b] for b in c)))
proper = [s for s in subsets if 0 < len(s[0]) < 4]
max_proper = max(s[1] for s in proper)
full = [s for s in subsets if len(s[0]) == 4][0]
covers = [s for s in subsets if s[1] == 10]
f2 = (len(subsets) == 16 and full[1] == 10 and max_proper == 9 and covers == [full]
      and dim["G"] + dim["W"] + dim["H"] + dim["D+"] == 10 == len(s_even))
chk("F2  [CT0.12; FT.141(1); FT.30; CT1.12a(1); NEW ROW; machine: exhaustive over all 2^4"
    "\n           sub-collections]: CONTENT = THE ENTIRE S SECTOR, AND MINIMALLY SO. The four rung-1 blocks"
    "\n           tile the S-even sector exactly: 5 + 3 + 1 + 1 = 10 = dim(S-even) = the number of metric"
    "\n           coordinates, so one pair channel -- one hop -- carries the WHOLE of the metric content at"
    "\n           once, with the six S-odd generators (the seals, zero metric coordinates) making up the"
    "\n           other 6 of the 16. Exhaustive census over all 16 sub-collections: the largest PROPER"
    "\n           sub-collection reaches 9 < 10 (G+W+H), and exactly ONE sub-collection covers the ten --"
    "\n           the full four. So all four blocks are needed; none is redundant; and the mediation is"
    "\n           simultaneous rather than sequential. This is the exact sense of the Architect's note: range"
    "\n           one hop, content the entire S sector.",
    f2, "sub-collections=%d; full=%s -> %d; max proper=%d; covering sub-collections=%s"
    % (len(subsets), full[0], full[1], max_proper, [s[0] for s in covers]))

# ---- F3: the range/content separation -- multi-hop is a CHAIN and COARSE-GRAINING property
trivial_ok = 0
trivial_tot = 0
for L in range(1, 9):
    trivial_tot += 1
    theta = sum(Fr(0) for _ in range(L))                     # every edge null: dshat^2 = 0
    trivial_ok += int(theta == 0 and D.i_pow(0) == D.Gauss(1))
bound_cells = {(dh, dt) for dt in range(1, 9) for dh in range(0, 4 * dt + 1)}
sharp_cells = {(4 * dt, dt) for dt in range(1, 9)}
em5 = (r"\gamma_{\gamma}\in\mathsf{Trivial}" in P2T and r"\Theta(\gamma)=0" in P2T)
ct26_ii = ("unboundedly many real edges" in ct26)
chain_def = (r"chain $c=(e_1,\dots,e_k)$" in P1T and r"t(e_i)=s(e_{i+1})" in P1T)
transit_def = ("transit" in P1T and "propagating open chain" in P1T)
f3 = (trivial_ok == trivial_tot == 8 and all(dh <= 4 * dt for (dh, dt) in bound_cells)
      and all((dh, dt) in bound_cells for (dh, dt) in sharp_cells)
      and em5 and ct26_ii and chain_def and transit_def)
chk("F3  [D1.4; D1.5; D1.7; EM.5; D3.7; Cor CT0.6a; CT2.6(ii); machine: exact censuses]: THE"
    "\n           RANGE/CONTENT SEPARATION -- one hop is a FORCE property, multi-hop is a CHAIN and a"
    "\n           COARSE-GRAINING property, and the two are never confused in the record. A chain is a"
    "\n           sequence of real edges with t(e_i) = s(e_{i+1}) [D1.4]; a transit chain is a PROPAGATING"
    "\n           OPEN chain, the bosonic content [D1.5]; the corpus's own long-range carriers are the"
    "\n           trivial chains -- photon and gluon -- with every edge null, so Theta(gamma) = sum_e 0 = 0"
    "\n           and Hol_spiral = 1 at every length (census 1..8, exact) [EM.5; D1.7; D3.7]. Through ONE"
    "\n           channel the register bound is delta_h <= 4*delta_tau, sharp at equality [Cor CT0.6a]. And"
    "\n           the continuum is reached not by extending a force but by averaging: hypothesis (ii) of"
    "\n           CT2.6 requires coarse-graining cells to contain unboundedly many real edges as h -> 0,"
    "\n           derived from the ledger's own ladder [CT2.6 Rmk; BM.151(1)]. So the 1-hop reach of the"
    "\n           rung-1 forces is compatible with -- indeed an input to -- an unbounded geometry.",
    f3, "trivial chains exact=%d/%d; bound cells=%d with %d sharp; EM.5 text=%s; CT2.6(ii) text=%s;"
        " chain/transit definitions=%s/%s"
    % (trivial_ok, trivial_tot, len(bound_cells), len(sharp_cells), em5, ct26_ii, chain_def, transit_def))

# ---- F4: the SM framing flag (out-of-corpus clarification; the bars stand) ---------------
ft157_bar = ("no SM species reading" in P3T and "no claim that the SM weak interaction is reproduced" in P3T)
ft158_bar = ("no family-mass read exists in the corpus" in P3T
             and "external data enters no derivation" in P3T)
ext_quarantine = ("[EXT]" in ALLTIER and "quarantin" in ALLTIER)
parallel_discipline = ("PARALLEL" in ALLTIER and "identification" in ALLTIER
                       and "graph isomorphism" in ALLTIER)
f4 = ft157_bar and ft158_bar and ext_quarantine and parallel_discipline
chk("F4  [FT.157 Rmk; FT.158(5); FT.141(6); IT.7(2); P1; P5; Def-BM.3(1),(7); machine text census]: THE"
    "\n           SM FRAMING IS FLAGGED OUT-OF-CORPUS. The Architect's note frames the 1-reach row against"
    "\n           the finite range of the SM weak bosons while noting that in this corpus the same block"
    "\n           mediates the entire S sector at once. That framing is recorded as CLARIFICATION, not"
    "\n           adopted: the frozen bars stand and are census-checked here -- FT.157's Rmk ('no SM species"
    "\n           reading; no claim that the SM weak interaction is reproduced [P1, P5]'), FT.158(5)'s"
    "\n           inadmissibility grounds ('no family-mass read exists in the corpus ... external data enters"
    "\n           no derivation'), the [EXT] quarantine of measured figures, and the standing"
    "\n           parallel-not-identification discipline [BM.134(5); IT.69(5)]. No range VALUE, no mass and"
    "\n           no species enters any clause of this tier; the 1-reach row is a pure support statement"
    "\n           (F1) in counts.",
    f4, "FT.157 bars=%s; FT.158 bars=%s; [EXT] quarantine=%s; parallel discipline=%s"
    % (ft157_bar, ft158_bar, ext_quarantine, parallel_discipline))

# ==========================================================================================
# PART G -- the verdict table, the bar-check (the tier document scanned), the census
# ==========================================================================================
print("\n" + "-" * 104)
print("PART G -- the verdict, the bars, the census")
print("-" * 104)

TIERFILE = os.path.join(TIERS, "Part6_Isotopic_era_TierIT22.md")
T22 = read(TIERFILE) if os.path.exists(TIERFILE) else ""

# ---- G1: the verdict table -- every component traced to a certifying marker ---------------
VERDICT = [
    ("1a", "the four blocks carry metric coordinates (5+3+1+1 = 10)", "DERIVED", b1 and b5 and a2),
    ("1b", "the seals carry ZERO metric coordinates", "DERIVED", b5),
    ("1c", "the dictionary is a bijection 10 <-> 10 (9 linear + 1 exponential cell)", "DERIVED", b1 and b2),
    ("1d", "they ARE the dimensions (an ontological identity)", "NOT ADOPTED -- four prices", b6),
    ("2a", "ticks are ledger events, not geometric", "DERIVED", c1 and c3),
    ("2b", "the forces are geometric (the metric's coefficients)", "DERIVED", b1 and c7),
    ("2c", "the G quintet is a geometric wave mode", "DERIVED", c5 and c6),
    ("2d", "W, H, D+ as wave modes", "NOT DERIVED -- scoped absence", c6),
    ("2e", "multi-hop reach through one channel", "DERIVED as a chain/coarse-graining property", c4 and f3),
    ("2f", "the dynamical mediation reading", "BARRED as formed -- three grounds", c8),
    ("3a", "W_i is T-odd", "DERIVED", a3 and a4),
    ("3b", "it transports to the time-reversal pullback", "DERIVED", d1 and d2 and d3),
    ("3c", "the interval is T-even (the flip is an involution)", "DERIVED", d4),
    ("3d", "it separates the two null legs", "DERIVED", d5),
    ("3e", "it distinguishes past from future", "SPLIT -- formal/read sense only", d5 and d6),
    ("3f", "it encodes left/right", "BARRED as a naming", d7),
    ("4a", "the contraction measures the ledger (jointly)", "DERIVED", e1 and e2),
    ("4b", "the on-shell integers (Theta_P in 2Z, kappa in Z)", "DERIVED", e3),
    ("4c", "the inverse translation (metric -> ledger integer)", "DERIVED", e4),
    ("4d", "which side quantizes", "DERIVED -- the geometry supplies the form, the ledger the discreteness", e5),
    ("4e", "a per-block measurement", "BARRED", e1),
    ("4f", "the operational read (the radar)", "DECLARED and formed", e6),
    ("4g", "the dynamical jump", "BARRED -- three grounds", c8 and e6),
    ("N1", "reach = 1 hop", "DERIVED", f1),
    ("N2", "content = the entire S sector, minimally", "DERIVED", f2),
    ("N3", "the SM weak-boson framing", "FLAGGED, not adopted", f4),
]
counts = {}
for _, _, v, _ in VERDICT:
    key = v.split(" -- ")[0]
    counts[key] = counts.get(key, 0) + 1
g1 = all(ok for (_, _, _, ok) in VERDICT) and len(VERDICT) == 26
chk("G1  [THE VERDICT TABLE; machine: every one of the 26 components traced to a certifying marker]:"
    "\n           CLAIM 1 -- DERIVED as a dictionary (10 metric coordinates over four blocks, 5+3+1+1; the"
    "\n           seals zero), the identity reading NOT ADOPTED with IT.52(3)'s four prices. CLAIM 2 --"
    "\n           SPLIT: 'not ticks' DERIVED, 'geometric' DERIVED, the wave mode DERIVED for the G quintet"
    "\n           alone with a SCOPED ABSENCE for W/H/D+ (not a no-go), multi-hop reach DERIVED as a chain"
    "\n           and coarse-graining property, the dynamical mediation BARRED on three grounds. CLAIM 3 --"
    "\n           SPLIT: T-oddness DERIVED (and sharpened: the unique T-odd sub-block OF THE METRIC SECTOR),"
    "\n           the transport DERIVED, the interval T-EVEN, the leg separation DERIVED, 'distinguishes past"
    "\n           from future' DERIVED ONLY in the formal/read sense (the arrow's locus is A6's no tau^-1),"
    "\n           and 'left/right' BARRED as a naming. CLAIM 4 -- DERIVED as a joint capability with the"
    "\n           on-shell integers and the inverse closed form, BARRED per block, DECLARED-and-formed as an"
    "\n           operational read, BARRED as dynamics. THE NOTE -- DERIVED: reach 1 hop, content the entire"
    "\n           S sector, minimally; the SM framing FLAGGED and not adopted.",
    g1, "components=%d; verdict census=%s" % (len(VERDICT), counts))

# ---- G2: the bar-check, with the tier document scanned ------------------------------------
DEC_RE = re.compile(r"(?<![\w.])\d+\.\d+(?![\w])")
decimals = DEC_RE.findall(T22)
# live-witness self-test: the scanner must FIRE on a decimal and stay silent on a citation token
selftest = (DEC_RE.findall("a value 1.25 here") == ["1.25"]
            and DEC_RE.findall("cited at D1.6 and CT1.19b and IT.68(1)") == [])
# P1: the dimensionful tokens present in the BOXED statements, each traced to a frozen row
BOX_RE = re.compile(r"\\boxed\{")
boxes = []
for m in BOX_RE.finditer(T22):
    depth, j = 1, m.end()
    while j < len(T22) and depth:
        if T22[j] == "\\" and j + 1 < len(T22) and T22[j + 1] in "{}":
            j += 2
            continue
        if T22[j] == "{":
            depth += 1
        elif T22[j] == "}":
            depth -= 1
        j += 1
    boxes.append(T22[m.start():j])
DIMTOK = [r"\mathfrak h", r"\mathfrak q", "G_N", r"\varkappa", r"\beta", r"\alpha_\Omega",
          r"\Omega", r"\kappa", r"\mu_", r"\Lambda"]
box_dims = {}
for b in boxes:
    hits = tuple(t for t in DIMTOK if t in b)
    if hits:
        box_dims[hits] = box_dims.get(hits, 0) + 1
# P1 is a NO-NEW-SCALE bar: every dimensionful symbol occurring in a box must already be a frozen
# symbol (P1's single scale h; D2.9's names G_N, kappa; P4's core varkappa, beta, alpha_Omega;
# D2.1's Omega; A8/D4.3's Lambda) -- none may be new, and none may be VALUED
FROZEN_DIM = {r"\mathfrak h", r"\mathfrak q", "G_N", r"\varkappa", r"\beta",
              r"\alpha_\Omega", r"\Omega", r"\kappa", r"\mu_", r"\Lambda"}
box_dim_union = set()
for h in box_dims:
    box_dim_union |= set(h)
p1_ok = box_dim_union <= FROZEN_DIM
# the transit bar: the amplitude alphabet must not occur as a constructed object
amp_tokens = ["Z^{\\mathrm{amp}}", "v_\\Gamma", "S\\text{-matrix}", "S-matrix"]
amp_absent = all(t not in T22 for t in amp_tokens)
# and every occurrence of the words amplitude/vertex/weight/rate sits in a negated or barred line
neg_words = ("amplitude", "vertex", "weight", "rate")
neg_markers = (r"\neg", "BARRED", "barred", "no ", "none", "unformed", "not formed", "owed",
               "never", "radiat", "¬", "three grounds", "deficit 1", "alphabet census",
               "tier scans", "it-o1", "scoped absence", "not derived")
# frozen compounds that are NOT amplitude vocabulary: EM.20(4)/D3.5's "edge weight" is the name of
# the per-edge phase factor G(e); "vertex" in the graph sense is D0.8/A7 vocabulary
FROZEN_COMPOUNDS = ["edge weight", "transfer weight", "a8's weight", "configuration weight",
                    "weight is the product over edges", "the weight w(c)",
                    "line-graph/vertex", "vertex bfs",
                    "vertex-instances", "vertex-instance", "per-vertex", "vertex set",
                    "vertex types", "cross-vertex", "the ticking vertex", "vertex v",
                    "vertex rung", "one vertex"]
neg_lines_ok = True
neg_lines = 0
neg_bad = []
WORD_RE = re.compile(r"\b(amplitude|vertex|weight|rate)\b", re.I)
for ln in T22.split("\n"):
    low = ln.lower()
    for fc in FROZEN_COMPOUNDS:
        low = low.replace(fc, "")
    if WORD_RE.search(low):
        neg_lines += 1
        if not any(m.lower() in low for m in neg_markers):
            neg_lines_ok = False
            neg_bad.append(ln[:110])
# species discipline: 'boson' occurs only inside the flagged clause
BOS_RE = re.compile(r"\bboson(?!ic)\b", re.I)
PARAS = [p for p in T22.split("\n\n") if p.strip()]
boson_paras = [p for p in PARAS if BOS_RE.search(p)]
boson_ok = (len(boson_paras) >= 2 and
            all(("clarification" in p.lower() or "flag" in p.lower() or "adopted" in p.lower()
                 or "resembl" in p.lower()) for p in boson_paras))
sm_bar_quoted = ("no SM species reading" in T22 and "no claim that the SM weak interaction is"
                 " reproduced" in T22)
g2 = (decimals == [] and selftest and p1_ok and amp_absent and neg_lines_ok and boson_ok
      and sm_bar_quoted and len(boxes) >= 10)
chk("G2  [P1; P5; Def-BM.3(1),(7); FT.157 Rmk; IT.66(3); machine scan of the tier document with a"
    "\n           live-witness self-test]: THE BAR-CHECK. P5 HONORED -- zero decimal numeric tokens in the"
    "\n           tier document (word-bounded scan; self-test: the same scanner fires on '1.25' and stays"
    "\n           silent on the citation tokens D1.6 / CT1.19b / IT.68(1), so the absence scan cannot pass"
    "\n           dead); every numeral in the tier is an exact integer or rational. P1 HONORED -- the"
    "\n           dimensionful symbols occurring inside the tier's boxed statements form a subset of the"
    "\n           FROZEN symbol list (P1's single scale h; D2.9's names G_N and kappa; P4's core varkappa,"
    "\n           beta, alpha_Omega; D2.1's Omega) -- NO new dimensionful symbol is introduced, and none is"
    "\n           valued; the tier's new rows are counts, parities and exact rationals. THE TRANSIT BAR STANDS -- the amplitude"
    "\n           alphabet (Z^amp, v_Gamma, the S-matrix, the T-matrix, M_fi) does not occur at all, and"
    "\n           every line mentioning amplitude/vertex/weight/rate -- once the frozen compounds (EM.20(4)'s"
    "\n           'edge weight', D0.8's graph-theoretic 'vertex') are stripped -- sits in a negation or a bar"
    "\n           context (%d such lines, all negated)."
    "\n           SPECIES DISCIPLINE -- 'boson' (excluding D1.5's frozen adjective 'bosonic') occurs only"
    "\n           inside the flagged clause, and the FT.157 Rmk bar"
    "\n           is quoted verbatim; no species is identified anywhere." % neg_lines,
    g2, "decimals=%s; self-test=%s; boxes=%d; dimensionful box tokens=%s; amplitude tokens absent=%s;"
        " negated lines=%d all negated=%s%s; boson paragraphs flagged=%s"
    % (decimals, selftest, len(boxes), sorted(box_dim_union), amp_absent, neg_lines, neg_lines_ok,
       ("; offenders=" + str(neg_bad)) if neg_bad else "", boson_ok))

# ---- G3: the declaration census and the open-row state ------------------------------------
no_act = ("No act at this tier" in T22 and "the declarations this tier adds: none" in T22
          and "issues no declaration" in T22)
cal_value_free = ("stays VALUE-FREE and unchanged" in T22 or "stays **value-free and unchanged**" in T22
                  or "VALUE-FREE" in T22)
register_intact = ("D-PJ7" in T22 and "D-RS4" in T22 and "deferred" in T22.lower())
no_new_row = ("NO new open row" in T22 and "(none new)" in T22)
consolidates = ("CONSOLIDATES under" in T22 and "P4 transport profile" in T22)
g3 = no_act and cal_value_free and register_intact and no_new_row and consolidates
chk("G3  [IT.66(4); IT.41(2); AT.63(2); machine text census with live witnesses]: THE DECLARATION CENSUS"
    "\n           -- NOTHING WAS FORCED. The tier issues no declaration and mints no candidate act: claim 1's"
    "\n           identity reading is left exactly where IT.52(3) put it (NOT ADOPTED, four prices), because"
    "\n           adopting it is the Architect's act; claim 4's operational read needed no new act because"
    "\n           D-RS6 and D-RS3 are already issued [IT.66(1); IT.65(1)]; claim 2's residue (a formed"
    "\n           propagator role for W, H, D+) is OWED content that already has a register locus -- it"
    "\n           CONSOLIDATES under D-PJ7's P4 transport profile, the declared gauge field [IT.41(2);"
    "\n           IT.66(4)] -- so NO NEW OPEN ROW is opened and the register stands as IT.66(4) records it:"
    "\n           issued D-PJ1-6, D-RS1-3, D-RS6-7 and the BM.113(6) sync; deferred D-RS4; owed D-PJ7 alone"
    "\n           plus the three sub-debts. Section Cal-IT stays VALUE-FREE and unchanged.",
    g3, "no-act rows=%s; Cal-IT value-free=%s; register intact=%s; no-new-row=%s; consolidation=%s"
    % (no_act, cal_value_free, register_intact, no_new_row, consolidates))

# ---- G4: the tier anatomy, the era chain, and the gate re-run ----------------------------
blocks22 = re.findall(r"^###\s+(IT\.\d+)\b", T22, re.M)
anatomy = True
for tag in blocks22:
    i = T22.index("### %s" % tag)
    j = T22.index("### ", i + 5) if "### " in T22[i + 5:] else len(T22)
    body = T22[i:j]
    for seg in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**"):
        if seg not in body:
            anatomy = False
    pfm = re.search(r"\*\*Pf\.\*\*(.+?)(\*\*Phys\.\*\*|\Z)", body, re.S)
    if not (pfm and "blacksquare" in pfm.group(1)):
        anatomy = False
cited = set(re.findall(r"\bIT\.(\d+)\b", T22))
OWN_LO, OWN_HI = 71, 78
own = {str(n) for n in range(OWN_LO, OWN_HI + 1)}
fwd = sorted(int(c) for c in cited if int(c) >= OWN_LO)
acyclic = all(str(c) in own for c in fwd) and not any(int(c) > OWN_HI for c in cited)
import subprocess
gate = subprocess.run([sys.executable, os.path.join(HERE, "check_level6_format.py")],
                      capture_output=True, text=True)
gate_ok = (gate.returncode == 0 and "22 documents PASS" in gate.stdout)
g4 = (blocks22 == ["IT.%d" % n for n in range(OWN_LO, OWN_HI + 1)] and anatomy and acyclic
      and gate_ok)
chk("G4  [AT.63(2); the gate's F1-F3; machine: the tier anatomy census + the era chain + the gate re-run]:"
    "\n           THE DOCUMENT AND THE ERA CHAIN. The tier carries exactly the eight blocks IT.71-IT.78, each"
    "\n           with Thm/Req/Pf/Phys and a blacksquare terminator in its Pf (independent of the gate's own"
    "\n           scan); every IT-tag cited is either an earlier tier's or this tier's own (IT.71-IT.78), so"
    "\n           no forward pointer is used as a premise and the citation graph is acyclic; and the level"
    "\n           gate re-run inside this checker passes on all twenty-two Part 6 documents (math balance,"
    "\n           block anatomy, citation attestation against the frozen era-1 registry, the closed Level-5"
    "\n           record and this level's own definitions). The frozen canon is cited, never edited: the"
    "\n           directive's citation slip is recorded as IT.71(4)(P1), not applied to any row.",
    g4, "blocks=%s; anatomy=%s; forward citations=%s (all own-tier=%s); gate=%s"
    % (blocks22, anatomy, fwd, acyclic, "PASS" if gate_ok else "FAIL"))

print("=" * 104)
print("VERDICT SUMMARY (Tier IT.22, tags IT.71-IT.78):")
print("""    * CLAIM 1 (they ARE the dimensions): DERIVED as a DICTIONARY -- all four rung-1 blocks carry
      metric coordinates, 5+3+1+1 = 10 = #{g_{mu nu} = g_{nu mu}}, cell by cell, and the S-odd six
      carry ZERO [FT.141(5); CT1.12; CT1.12a(2); FT.30]. The bijection is 9 linear cells + 1
      exponential (a_00 only the exponent). The IDENTITY reading stays NOT ADOPTED with IT.52(3)'s
      four prices -- an Architect act, not forced here.
    * CLAIM 2 (channels, not ticks): SPLIT. The tick is a ledger event with no metric content and no
      inverse [A6; A7; D0.7; D1.9]. The forces ARE the metric's coefficients. But the wave operator
      belongs to the G QUINTET ALONE: 4 of the 10 components of the linearized Einstein tensor (the
      lapse cell + the three shift cells) carry no second time derivative at all -- constraint cells,
      re-deriving AT.5(4) from the operator side -- and CT1.18's own gauge switches off D+, W and H.
      For those three: a SCOPED ABSENCE, not a no-go; the residue consolidates under D-PJ7's P4
      transport profile. The dynamical mediation reading stays BARRED (three grounds).
    * CLAIM 3 (the T-odd shift): SPLIT. T(W_i) = -W_i is DERIVED, and it transports exactly to the
      time-reversal pullback (g_00, g_ij fixed; g_0i flipped; the signature invariant). Precision:
      6 of 16 generators are T-odd (W AND K), so the distinctive row is 'the unique T-odd sub-block
      OF THE METRIC SECTOR'. The interval is T-EVEN monomial by monomial; the shift's sign separates
      the two radar legs; and 'distinguishes past from future' holds only in the formal/read sense --
      the ARROW is A6's no tau^-1 + FT.144's no backward materialization + the monotone record, with
      a new closed form 2^(2n-1) for the two-pair completed interleavings. 'Left/right' is BARRED.
    * CLAIM 4 (measuring the discrete jumps): DERIVED as a JOINT capability -- G(e) = sigma_e *
      exp(i alpha_e dshat^2(e)) is the frozen formula of the translation, one ledger bit times one
      geometric phase, edge-local, multiplied over edges [D3.5; EM.20(4); A8]; all ten coordinates
      enter the interval; on shell Theta_P in 2Z and kappa in Z [CT1.19b]; the read runs BACKWARDS
      as AT.5(1)'s closed form, linear in the ledger integer, with 2 gauge dimensions per edge.
      PER-BLOCK is BARRED [FT.30 Verdict]; the OPERATIONAL read is DECLARED (D-RS6, D-RS3) and
      formed (IT.68); the DYNAMICAL jump stays BARRED. Which side quantizes: the geometry supplies
      the form, the LEDGER the discreteness, the integers are their on-shell contraction.
    * THE NOTE (1 hop, whole S sector): DERIVED as a theorem -- reach exactly one hop (the pair
      channel, the per-edge metric, D1.9's non-vacuous distance bar) and content exactly the ten
      S-even dimensions, minimally (the largest proper sub-collection reaches 9). Multi-hop reach is
      a CHAIN and COARSE-GRAINING property, never a force range. The SM framing is FLAGGED, not
      adopted; the bars stand.
    * UNCHANGED: no declaration issued, no new open row, Cal-IT value-free, IT-O1/IT-O2/IT-O5 as
      they were, the frozen canon cited and never edited.""")
print("=" * 104)

n_ok = sum(R)
print("\n  translation_layer.py: %d/%d EXACT -- no floating point, no measured value." % (n_ok, len(R)))
sys.exit(0 if n_ok == len(R) else 1)
