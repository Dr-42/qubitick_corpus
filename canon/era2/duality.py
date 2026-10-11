#!/usr/bin/env python3
"""
duality.py -- REUSABLE exact core for the View1/View2 duality (chart <-> ledger), Level 5.

Logged as a standing tool (MEMORY.md §6): the base transformation between
  VIEW 2 (ledger): per-edge on-shell integers kappa_e = dshat^2(e) [FT.24-25], tick increments
         Delta x^0 [D1.8: x^0 := tau_n, forward-only A6], arc-dependent spatial hops Delta x^i,
         signs sigma_e, Janus weights x_+-, winding Theta(c) = sum_e dshat^2(e) = 2k [FT.22],
         orientation doublet H_omega with omega-hat, chi-hat [Def-H.33], phases i^Theta [Def-BM.16(5)];
  VIEW 1 (chart):  the emergent metric g_{mu nu} = Omega^2 gbar_{mu nu} with
         gbar_00 = -1, gbar_0i = kappa beta w_i, gbar_ij = delta_ij + kappa q_ij [CT1.12],
         identically BM.34(1)'s ADM data (gamma_ij = Omega^2(delta+kappa q), N_i = Omega^2 kappa beta w_i,
         N^2 = Omega^2 + gamma^{ij} N_i N_j, N^2 det gamma = -det g [Schur]), g_0i = kappa beta Omega^2 w_i
         [FT.157(1)], lapse N(k,E) = sqrt(1 - G/(4 pi k)) [BM.132].

THE DICTIONARY (the transformation rules this module implements exactly):
  (D1) sector -> ADM/conformal:  sector_to_adm()  [CT1.12 == BM.34(1), machine identity];
  (D2) ledger -> chart, per edge: the AT.5(1) closed form
         (w.Dx)(e) = [h^2 kappa_e/Omega^2 + (Dx^0)^2 - M_ij Dx^i Dx^j] / (2 kappa beta Dx^0),
         M = delta + kappa q; longitudinal DERIVED, transverse 2 dims per edge GAUGE [AT.5(3),(4)];
  (D3) chart -> ledger, per edge: dshat^2(e) = (Omega^2/h^2)[-(Dx^0)^2 + 2 kappa beta Dx^0 (w.Dx)
         + M Dx Dx] must be the integer kappa_e on shell [FT.24-25], and sum_e kappa_e = 2k in 2Z
         [FT.22] -- the quantization that turns the drag into a Diophantine condition;
  (D4) the flat/drag decomposition: kappa_e = flat_e + drag_e with
         drag_e = (Omega^2/h^2) 2 kappa beta Dx^0 (w.Dx)(e) -- the shift's UNIQUE entry (index
         structure: g_0i T-odd x Dx^0 T-odd x Dx^i T-even = T-even, as the metric must be);
  (D5) holonomy reads: Hol_w(c) = sum_e (w.Dx)(e); weighted Hol~ = sum_e Dx^0(e)(w.Dx)(e);
         Theta_drag = (Omega^2/h^2) 2 kappa beta Hol~; ORIENTATION-ODD (Dx^0 forward, Dx arc-odd);
         constant shift telescopes: Hol_w = w . (sum_e Dx(e)) = 0 on every closed chain;
  (D6) doublet reads: on H_omega (basis |c>,|omega(c)>): omega-hat = [[0,1],[1,0]],
         chi-hat = i(|c><omega| - |omega><c|) = [[0,i],[-i,0]], |L> = |c> - i|omega(c)>,
         |R> = |c> + i|omega(c)> [Def-H.33]; the drag phase operator diag(i^{+Td}, i^{-Td})
         for INTEGER Td; statistics eps = i^Theta [Def-BM.16(5)].
  HANDSHAKE / SPECIES DISCIPLINE: the ledger resolvent 1/(1 - wf^2 x_+ x_-) [FT.108(5); wf the
  move fugacity -- NOT the shift w_i] and the chart resolvent R(z;p) [Def-BM.20] are NEG-identified;
  they meet only through the threshold indicator chi_{NE >= T_0} [BM.134(5)]. Frame angle Theta_R
  (q^0, Def-H.21) is NEVER equated with 2 pi k (q^{+1}) [FT.55(1)]. This module forms dictionaries
  and decompositions; it forms no cross-species identification.

Units: h = 1 throughout (the single scale factors out of every identity here); Omega^2 is carried as
an exact positive Fraction; kappa*beta is carried symbolically as one Fraction parameter (P4 core,
values neg-issued -- every output is a polynomial/rational function of it, never a number for it).

Arithmetic: Fraction; Quad(d) = a + b sqrt(d) exact (regular polygons); Gauss = a + b i exact
(the fourth-root phase alphabet). No floating point anywhere.
"""
from fractions import Fraction as Fr

# --------------------------------------------------------------------------
# exact number systems
# --------------------------------------------------------------------------
class Quad:
    """a + b*sqrt(d) over Fraction; d a fixed squarefree positive int."""
    __slots__ = ("a", "b", "d")
    def __init__(self, a, b=0, d=3):
        self.a, self.b, self.d = Fr(a), Fr(b), d
    def __add__(s, o):
        o = o if isinstance(o, Quad) else Quad(o, 0, s.d)
        assert o.d == s.d
        return Quad(s.a + o.a, s.b + o.b, s.d)
    __radd__ = lambda s, o: s + o
    def __sub__(s, o):
        o = o if isinstance(o, Quad) else Quad(o, 0, s.d)
        return Quad(s.a - o.a, s.b - o.b, s.d)
    def __rsub__(s, o): return (-s) + o
    def __neg__(s): return Quad(-s.a, -s.b, s.d)
    def __mul__(s, o):
        if isinstance(o, Quad):
            assert o.d == s.d
            return Quad(s.a * o.a + s.b * o.b * s.d, s.a * o.b + s.b * o.a, s.d)
        return Quad(s.a * o, s.b * o, s.d)
    __rmul__ = __mul__
    def conj(s): return Quad(s.a, -s.b, s.d)
    def norm2(s): return s.a * s.a + s.b * s.b * s.d      # exact, in Q
    def __eq__(s, o):
        o = o if isinstance(o, Quad) else Quad(o, 0, s.d)
        return s.d == o.d and s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b, s.d))
    def __repr__(s):
        return f"({s.a}+{s.b}*r{s.d})" if s.b else f"({s.a})"

class Gauss:
    """a + b*i over Fraction -- the fourth-root phase alphabet, exact."""
    __slots__ = ("a", "b")
    def __init__(self, a, b=0): self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, Gauss) else Gauss(o); return Gauss(s.a + o.a, s.b + o.b)
    __radd__ = lambda s, o: s + o
    def __sub__(s, o): return s + (-o if isinstance(o, Gauss) else Gauss(-o))
    def __neg__(s): return Gauss(-s.a, -s.b)
    def __mul__(s, o):
        o = o if isinstance(o, Gauss) else Gauss(o)
        return Gauss(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = o if isinstance(o, Gauss) else Gauss(o)
        n = o.a * o.a + o.b * o.b
        assert n != 0, "division by zero Gauss"
        return Gauss((s.a * o.a + s.b * o.b) / n, (s.b * o.a - s.a * o.b) / n)
    def __pow__(s, n):
        assert isinstance(n, int) and n >= 0
        r = Gauss(1)
        b = s
        while n:
            if n & 1:
                r = r * b
            b, n = b * b, n >> 1
        return r
    def __eq__(s, o): o = o if isinstance(o, Gauss) else Gauss(o); return (s.a, s.b) == (o.a, o.b)
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"{s.a}{s.b:+g}i"

def i_pow(n):
    """i^n exactly, n an integer (the fourth-root alphabet); accepts int or integral Fraction."""
    n = Fr(n)
    assert n.denominator == 1, f"i^n needs an integer exponent, got {n}"
    t = int(n) % 4
    return (Gauss(1), Gauss(0, 1), Gauss(-1), Gauss(0, -1))[t]

# --------------------------------------------------------------------------
# small exact matrix/vector helpers (any ring with +,-,*)
# --------------------------------------------------------------------------
def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def mat_vec(A, v):
    return [sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A))]

def mat_T(A):
    return [list(r) for r in zip(*A)]

def mdag(A):
    """conjugate transpose over Gauss entries (no-op on Fraction entries)."""
    out = []
    for j in range(len(A[0])):
        row = []
        for i in range(len(A)):
            x = A[i][j]
            row.append(Gauss(x.a, -x.b) if isinstance(x, Gauss) else x)
        out.append(row)
    return out

def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))

def inverse3(M):
    """exact 3x3 inverse over Fraction (Fraction entries required)."""
    d = det3(M)
    assert d != 0
    C = [[Fr(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[M[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            m2 = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            C[j][i] = ((-1) ** (i + j)) * m2 / d
    return C

# --------------------------------------------------------------------------
# (D1) the dictionary: sector data -> ADM / conformal metric
# --------------------------------------------------------------------------
def sector_to_adm(Omega2, kappa, beta, w, q):
    """w, q: w = (w1,w2,w3) Fractions; q = 3x3 symmetric Fractions.
    Returns dict with gamma, Ni, N2, g (4x4), gbar (4x4), and the exact identity flags."""
    I3 = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
    gamma = [[Omega2 * (I3[i][j] + kappa * q[i][j]) for j in range(3)] for i in range(3)]
    ginv = inverse3([[I3[i][j] + kappa * q[i][j] for j in range(3)] for i in range(3)])  # M^{-1}
    Ni = [Omega2 * kappa * beta * w[i] for i in range(3)]                # FT.157(1)/BM.34(1)
    # gamma^{ij} = Omega^{-2} M^{ij}  =>  gamma^{ij} N_i N_j = Omega^{-2} sum M^{ij} Ni Nj
    gam_inv_NiNj = sum(ginv[i][j] * Ni[i] * Ni[j] for i in range(3) for j in range(3)) / Omega2
    N2 = Omega2 + gam_inv_NiNj                                            # BM.34(1)
    # g_{mu nu}: g00 = -N2 + N_i N^i = -N2 + gam_inv_NiNj... careful: N_iN^i = gamma^{ij}N_iN_j
    g = [[Fr(0)] * 4 for _ in range(4)]
    g[0][0] = -N2 + gam_inv_NiNj
    for i in range(3):
        g[0][i + 1] = Ni[i]
        g[i + 1][0] = Ni[i]
        for j in range(3):
            g[i + 1][j + 1] = gamma[i][j]
    # CT1.12 conformal form: gbar_00=-1, gbar_0i=kappa beta w_i, gbar_ij=delta+kappa q
    gbar = [[Fr(0)] * 4 for _ in range(4)]
    gbar[0][0] = Fr(-1)
    for i in range(3):
        gbar[0][i + 1] = kappa * beta * w[i]
        gbar[i + 1][0] = kappa * beta * w[i]
        for j in range(3):
            gbar[i + 1][j + 1] = I3[i][j] + kappa * q[i][j]
    conformal_ok = all(g[a][b] == Omega2 * gbar[a][b] for a in range(4) for b in range(4))
    # Schur identity N^2 det gamma = -det g
    det_gam = det3(gamma)
    g4det = det4(g)
    schur_ok = (N2 * det_gam == -g4det)
    return dict(gamma=gamma, Ni=Ni, N2=N2, g=g, gbar=gbar,
                conformal_ok=conformal_ok, schur_ok=schur_ok)

def det4(M):
    tot = Fr(0)
    for j in range(4):
        minor = [[M[r][c] for c in range(4) if c != j] for r in range(1, 4)]
        tot += ((-1) ** j) * M[0][j] * det3(minor)
    return tot

# --------------------------------------------------------------------------
# (D2)-(D4) the per-edge dictionary: line element, AT.5 closed form, flat/drag split
# --------------------------------------------------------------------------
def M_metric(kappa, q, dim=3):
    I = [[Fr(int(i == j)) for j in range(dim)] for i in range(dim)]
    return [[I[i][j] + kappa * q[i][j] for j in range(dim)] for i in range(dim)]

def dshat2(Omega2, kapb, Mmat, w_e, dx0, dx):
    """dshat^2(e) at h=1: Omega2*[ -(dx0)^2 + 2*kapb*dx0*(w.dx) + dx.M.dx ]; kapb = kappa*beta."""
    quad = sum(Mmat[i][j] * dx[i] * dx[j] for i in range(len(dx)) for j in range(len(dx)))
    return Omega2 * (-dx0 * dx0 + 2 * kapb * dx0 * dot(w_e, dx) + quad)

def drag_part(Omega2, kapb, w_e, dx0, dx):
    return Omega2 * 2 * kapb * dx0 * dot(w_e, dx)

def flat_part(Omega2, Mmat, dx0, dx):
    quad = sum(Mmat[i][j] * dx[i] * dx[j] for i in range(len(dx)) for j in range(len(dx)))
    return Omega2 * (-dx0 * dx0 + quad)

def at5_longitudinal(kappa_e, Omega2, kapb, Mmat, dx0, dx):
    """AT.5(1): (w.Dx)(e) = [kappa_e/Omega2 + dx0^2 - M Dx Dx] / (2 kapb dx0), at h=1."""
    quad = sum(Mmat[i][j] * dx[i] * dx[j] for i in range(len(dx)) for j in range(len(dx)))
    return (Fr(kappa_e) / Omega2 + dx0 * dx0 - quad) / (2 * kapb * dx0)

# --------------------------------------------------------------------------
# (D5) holonomy reads on chains; polygons with exact coordinates
# --------------------------------------------------------------------------
def holonomy(arcs, w_field):
    """arcs: list of (dx0, dx); w_field: list of per-arc shift vectors. Hol = sum (w.dx)."""
    return sum((dot(w, dx) for (_, dx), w in zip(arcs, w_field)), 0 * arcs[0][1][0])

def weighted_holonomy(arcs, w_field):
    return sum((dx0 * dot(w, dx) for (dx0, dx), w in zip(arcs, w_field)), 0 * arcs[0][1][0])

def reverse_chain(arcs):
    """omega(c): the opposite traversal. Forward-only ledger [A6; D1.8]: the tick increment
    stays the edge's registered positive Delta x^0; the SPATIAL hop is arc-odd (source->target)."""
    out = []
    for (dx0, dx) in reversed(arcs):
        out.append((dx0, [-c for c in dx]))
    return out

def digon(t=1, ell=1):
    v0, v1 = (Fr(0),), (Fr(ell),)
    return [(Fr(t), (Fr(ell),)), (Fr(t), (Fr(-ell),))]

def square(t=1, ell=1):
    L = Fr(ell)
    return [(Fr(t), (L, Fr(0))), (Fr(t), (Fr(0), L)), (Fr(t), (-L, Fr(0))), (Fr(t), (Fr(0), -L))]

def triangle(t=1, ell=1, d=3):
    """regular triangle, exact in Quad(d=3): vertices 0, ell, ell*(1/2 + sqrt3/2 i)-style plane coords."""
    L = Fr(ell)
    h = Quad(Fr(1, 2), Fr(1, 2), d)          # (1+sqrt3)/2 placeholder -> use proper height sqrt(d)/2
    hh = Quad(Fr(0), Fr(1, 2), d)             # sqrt(3)/2
    e1 = (L, Quad(0, 0, d))
    e2 = (Quad(Fr(-1, 2)) * L, hh * L)
    e3 = (Quad(Fr(-1, 2)) * L, -hh * L)
    return [(Fr(t), e1), (Fr(t), e2), (Fr(t), e3)]

def hexagon(t=1, d=3):
    """regular hexagon, unit edge: edge vectors at angles 0,60,...,300 deg, exact in Quad(3)."""
    hh = Quad(Fr(0), Fr(1, 2), d)             # sqrt3/2
    dirs = [(Quad(1), Quad(0)), (Quad(Fr(1, 2)), hh), (Quad(Fr(-1, 2)), hh),
            (Quad(-1), Quad(0)), (Quad(Fr(-1, 2)), -hh), (Quad(Fr(1, 2)), -hh)]
    return [(Fr(t), (a, b)) for a, b in dirs]

# --------------------------------------------------------------------------
# the tetrahedral floor: integer rotation group, simply transitive on the 12 arcs [AT.34]
# --------------------------------------------------------------------------
TET_V = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]

def tet_arcs():
    return [(a, b) for a in range(4) for b in range(4) if a != b]

def _signed_perms():
    from itertools import permutations, product as iproduct
    out = []
    for perm in permutations(range(3)):
        for signs in iproduct((1, -1), repeat=3):
            M = [[Fr(0)] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = Fr(signs[i])
            out.append(M)
    return out

def _preserves_tet(M):
    return all(apply_rot(M, v) in TET_V for v in TET_V)

def tet_automorphisms():
    """Aut of the tetrahedral skeleton: the 24 signed permutations preserving the vertex set
    (product of signs = +1); |Aut| = 2|Rot| [AT.34(1),(4)]."""
    return [M for M in _signed_perms() if _preserves_tet(M)]

def tet_rotations():
    """the 12 orientation-preserving tetrahedral rotations (det +1 AND vertex-set preserving),
    exact integer entries; |Rot| = 2E = 12 and Rot is simply transitive on the 12 arcs [AT.34(1)-(3)]."""
    return [M for M in tet_automorphisms() if det3(M) == 1]

def arc_vector(arc):
    a, b = arc
    va, vb = TET_V[a], TET_V[b]
    return tuple(Fr(vb[i] - va[i]) for i in range(3))

def apply_rot(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))

# --------------------------------------------------------------------------
# (D6) the orientation doublet H_omega [Def-H.33], exact 2x2 over Gauss
# --------------------------------------------------------------------------
OMEGA_HAT = [[Gauss(0), Gauss(1)], [Gauss(1), Gauss(0)]]        # |c> <-> |omega(c)>
CHI_HAT   = [[Gauss(0), Gauss(0, 1)], [Gauss(0, -1), Gauss(0)]]  # i(|c><w| - |w><c|)
KET_C     = [Gauss(1), Gauss(0)]
KET_W     = [Gauss(0), Gauss(1)]
KET_L     = [Gauss(1), Gauss(0, -1)]     # |c> - i|omega(c)>  (chi = +1)
KET_R     = [Gauss(1), Gauss(0, 1)]      # |c> + i|omega(c)>  (chi = -1)

def drag_phase_op(Td):
    """the diagonal fourth-root drag operator diag(i^{+Td}, i^{-Td}) on the traversal basis,
    Td an INTEGER (forced by FT.22 quantization on materialized polygons)."""
    assert Td.denominator == 1
    return [[i_pow(Td), Gauss(0)], [Gauss(0), i_pow(-Td)]]
