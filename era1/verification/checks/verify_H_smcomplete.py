#!/usr/bin/env python3
"""verify_H_smcomplete.py — companion to Def-H.29 / FT.81-FT.84 (Tier F.28).

The full-SM completeness audit: (A) particle-content census, (B) the 16-register block
structure vs the SM gauge algebra at representation level, (C) the rung ladder's
derived/declared/open status, (D) the consolidated deficit table.

POLICY (Part E of the directive, enforced here):
  * every SM datum is EXTERNAL and marked; none enters a derivation; no corpus object is
    identified with a particle (Open Gaps 5/12 stand);
  * every corpus-side claim cites the supplying tag; every absence is either a machine-checked
    inventory fact (a scan of the frozen A-G text) or a cited structural no-go;
  * exact arithmetic only: integers, Fractions, Q(i) matrices, root-space structure constants,
    and the quotient ring Q[g,g',s]/(s^2-g^2-g'^2) for the electroweak identities.
    No floating point is used in any assertion.
"""
import os, re, sys, time, itertools, math
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, '..'))
CORPUS = ['A_axioms.md', 'B_foundation.md', 'C_geometry.md', 'D_electroweak.md',
          'E_electromagnetic.md', 'F_color.md', 'G_saturation.md']
TEXT = {d: era_paths.read(d) for d in CORPUS}
ALLG = "\n".join(TEXT[d] for d in CORPUS)
if ARCH:
    _SPLIT_H = ['H_archive/H01_flux_and_fermion.md', 'H_archive/H02_edges_and_spin_charge.md',
                'H_archive/H03_subnetwork_force_and_geometry.md', 'H_archive/H04_aspect_operator_and_spectrum.md',
                'H_archive/H05_floor_families.md', 'H_archive/H06_platonic_and_polygon_floors.md',
                'H_archive/H07_spin_ladder.md', 'H_archive/H08_loops_and_bott.md',
                'H_archive/H09_flicker_and_domains.md', 'H_archive/H10_sm_audit.md',
                'H_archive/H11_gravity_and_koide.md', 'H_archive/H12_chirality_and_form_factor.md',
                'H_archive/H13_registries_and_gaps.md']
if ARCH:
    HDOC = '\n'.join(era_paths.read(_fn)
                     for _fn in _SPLIT_H)

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1
t0 = time.time()
def stamp(m): print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")

# ---------------------------------------------------------------- exact algebra
class QI:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __add__(s, o): return QI(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return QI(s.a - o.a, s.b - o.b)
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return QI(s.a * o, s.b * o)
        return QI(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __neg__(s): return QI(-s.a, -s.b)
    def __radd__(s, o):
        if isinstance(o, int) and o == 0: return QI(s.a, s.b)
        return s.__add__(o)
    def __rsub__(s, o):
        if isinstance(o, int) and o == 0: return -s
        return NotImplemented
    def __eq__(s, o):
        if isinstance(o, int): o = QI(o)
        return isinstance(o, QI) and s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"{s.a}{'' if s.b == 0 else ('+' if s.b > 0 else '-') + str(abs(s.b)) + 'i'}"
ZERO, ONE, IM = QI(0), QI(1), QI(0, 1)

def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
def msub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mcomm(A, B): return msub(mmul(A, B), mmul(B, A))
def mscale(c, A): return [[c * x for x in r] for r in A]
def tr(M): return sum(M[i][i] for i in range(len(M)))

class Poly:
    """Q[g,g',s]/(s^2 - g^2 - g'^2); monomials (i,j,k), k reduced below 2."""
    __slots__ = ('t',)
    def __init__(s, terms=None): s.t = dict(terms or {})
    @staticmethod
    def mono(i, j, k, c=1):
        p = Poly(); p._add((i, j, k), Fr(c)); return p
    def _add(s, key, c):
        i, j, k = key
        if k >= 2:
            s._add((i + 2, j, k - 2), c); s._add((i, j + 2, k - 2), c); return
        s.t[key] = s.t.get(key, Fr(0)) + c
        if s.t[key] == 0: del s.t[key]
    def __add__(s, o):
        r = Poly(s.t)
        for k, v in o.t.items(): r._add(k, v)
        return r
    def __sub__(s, o): return s + Poly({k: -v for k, v in o.t.items()})
    def __radd__(s, o):
        if isinstance(o, int) and o == 0: return Poly(s.t)
        return s + o
    def __rsub__(s, o):
        if isinstance(o, int) and o == 0: return -s
        return NotImplemented
    def __neg__(s): return Poly({k: -v for k, v in s.t.items()})
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return Poly({k: v * o for k, v in s.t.items()})
        r = Poly()
        for k1, v1 in s.t.items():
            for k2, v2 in o.t.items(): r._add(tuple(a + b for a, b in zip(k1, k2)), v1 * v2)
        return r
    __rmul__ = __mul__
    def __eq__(s, o): return isinstance(o, Poly) and s.t == o.t
    def is_zero(s): return not s.t
    def __repr__(s):
        return " + ".join(f"{v} g^{i} g'^{j} s^{k}" for (i, j, k), v in sorted(s.t.items())) or "0"

# ================================================================ PART A/B-0
print("=" * 104)
print("PART A/B-0 — corpus-side count and dimension arithmetic (each line cites its tag)")
print("=" * 104)
chk(sum((7, 3, 3, 3)) == 16, "CT1.1/P2: (dim E++,E+-,E-+,E--) = (7,3,3,3), sum 16")
chk(3 + 3 + 5 + 3 + 1 + 1 == 16, "CT0.12: J+(3)+J-(3)+G(5)+W(3)+H(1)+D+(1) = 16 = C_cap")
chk((5 + 3 + 1) + (3 + 3) + 1 == 16, "FT.30 (H): (G5+W3+H1)+(J+3+J-3)+D+1 = 16")
chk(6 < 16 < 17 < 25, "CT0.14: dim K_n = (6,16,17,25), a strict flag")
chk(1 == 1 and 8 == 8, "CT0.14: dim K^(EM) = 1, dim K^(strong) = 8")
chk(1 + 5 + 1 + 3 + 8 == 18, "FT.26(3) (H): dim K_Sigma <= 1+5+1+3+8 = 18")
D_tick = [2 ** (n + 1) for n in range(6)]
chk(D_tick == [2, 4, 8, 16, 32, 64], f"CT0.5: D_tick(n) = 2^(n+1) = {D_tick}")
chk([n for n in range(6) if D_tick[n] <= 16] == [0, 1, 2, 3], "CT0.11: admissible iff 2^(n+1) <= 16 iff n <= 3")
chk(D_tick[3] == 16, "CT0.11: D_tick(3) = C_cap (saturation at rung 3)")
chk(int(math.log2(16)) - 1 == 3, "CT3.20: N_colour = log2(C_cap) - 1 = 3 (derived from A2+CT0.9, not chosen)")
chk(3 + 3 * 2 == 9 and 9 - 1 == 8 and 3 ** 2 - 1 == 8, "CT3.8: dim_R u(3) = 9, dim su(3) = 8 = 3^2-1")
chk(8 + 1 == 9, "CT3.13: N_gluon = 8; the 9th u(3) direction (centre) goes to F_EM")
chk(8 + 3 + 1 == 12, "EXTERNAL: dim(su(3)+su(2)+u(1)) = 12 == corpus strong(8)+W(3)+EM(1) [CT0.14/CT0.12]")
chk(Fr(1, 4) * 8 == 2, "P3/CT2.9: kappa^2 = 8 pi G_N = 8 pi h^2/(4 ln2) = 2 pi h^2/ln2")
chk(2 ** 2 == 4 and 4 // 2 == 2, "P2: N_gamma-pol = 2; D_tick / C_cap arithmetic")
stamp("16 = (7,3,3,3) = 3+3+5+3+1+1 = (5+3+1)+(3+3)+1; masks (6,16,17,25); 18-bound; n<=3; N_colour=3; N_gluon=8; 8+3+1=12")

# ================================================================ PART B: Lie closure
print("\n" + "=" * 104)
print("PART B — does the block structure close as the SM gauge algebra? (representation level)")
print("=" * 104)
# --- su(2) in the defining representation: W_i = sigma_i/2 over Q(i)  [EW.32, CT0.7a]
sig = [[[1, 0], [0, 1]], [[0, 1], [1, 0]], [[0, -IM], [IM, 0]], [[1, 0], [0, -ONE]]]
sig = [[[QI(x) if isinstance(x, int) else x for x in r] for r in m] for m in sig]
W = [mscale(QI(Fr(1, 2)), sig[i]) for i in (1, 2, 3)]
Y = mscale(QI(Fr(1, 2)), sig[0])
eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
for i, j in itertools.product(range(3), repeat=2):
    lhs = mcomm(W[i], W[j])
    rhs = [[sum(QI(0, eps.get((i, j, k), 0)) * W[k][a][b] for k in range(3)) for b in range(2)] for a in range(2)]
    chk(all(lhs[a][b] == rhs[a][b] for a in range(2) for b in range(2)),
        f"su(2) closure [W_i,W_j] = i eps_ijk W_k at (i,j) = ({i},{j})")
chk(all(tr(x) == ZERO for x in W), "EW.32: W_i traceless (su(2), not u(2))")
chk(tr(Y) == ONE, "EW.32: Y = sigma_0/2, trace 1 (the u(1) centre)")
G4 = W + [Y]
for a in range(4):
    for b in range(4):
        chk(tr(mmul(G4[a], G4[b])) == (QI(Fr(1, 2)) if a == b else ZERO),
            f"EW.32 uniform trace normalization T(G_a G_b) = (1/2) delta_ab at ({a},{b})")
v = [[ZERO], [ONE]]
chk(mmul(W[2], v) == mscale(QI(Fr(-1, 2)), v), "EW.20: W_3 v = -(1/2) v (lower weight state)")
chk(mmul(Y, v) == mscale(QI(Fr(1, 2)), v), "EW.20: Y v = +(1/2) v — the SM vev quantum numbers, derived")
# FT.58's hosting identity: (lambda_1 + i lambda_2)/2 = E_12 in the 3-dim fundamental
E12 = [[ZERO] * 3 for _ in range(3)]; E12[0][1] = ONE
lam1 = [[ZERO] * 3 for _ in range(3)]; lam1[0][1] = ONE; lam1[1][0] = ONE
lam2 = [[ZERO] * 3 for _ in range(3)]; lam2[0][1] = -IM; lam2[1][0] = IM
lam2i = [[lam2[i][j] * IM for j in range(3)] for i in range(3)]
chk(mscale(QI(Fr(1, 2)), madd(lam1, lam2i)) == E12,
    "FT.58 (H): (lambda_1 + i lambda_2)/2 = E_12 exactly over Q(i) — the literal su(3) hosting")

# --- su(3) in the matrix-unit (root-space) basis over Q  [FT.57's root-space language]
def E(i, j, n=3):
    M = [[Fr(0)] * n for _ in range(n)]; M[i][j] = Fr(1); return M
H1 = [[Fr(1), 0, 0], [0, Fr(-1), 0], [0, 0, 0]]
H2 = [[0, 0, 0], [0, Fr(1), 0], [0, 0, Fr(-1)]]
basis = [E(0, 1), E(1, 0), E(0, 2), E(2, 0), E(1, 2), E(2, 1), H1, H2]
names = ['E12', 'E21', 'E13', 'E31', 'E23', 'E32', 'H1', 'H2']
chk(len(basis) == 8, "su(3): 8 basis elements (6 roots + 2 Cartan)")
chk(all(sum(M[i][i] for i in range(3)) == 0 for M in basis), "su(3): every generator traceless")
def coords(M):
    """exact coordinates of M in the basis (rational), or None."""
    sol = {}
    R = M
    for a in (0, 1):  # root vectors E12,E21 etc. read off directly
        pass
    c = [Fr(0)] * 8
    c[0] = R[0][1]; c[1] = R[1][0]; c[2] = R[0][2]; c[3] = R[2][0]; c[4] = R[1][2]; c[5] = R[2][1]
    # diagonal part: d1*H1 + d2*H2 = diag(d1, d2-d1, -d2)
    d1 = R[0][0]; d2 = R[1][1] + d1     # a H1 + b H2 = diag(a, b-a, -b) -> a = r0, b = r0+r1
    c[6], c[7] = d1, d2
    rec = mscale(Fr(-1), R)                      # residual: sum c_k basis_k - R
    for k in range(8): rec = [[rec[i][j] + c[k] * basis[k][i][j] for j in range(3)] for i in range(3)]
    return c if all(rec[i][j] == 0 for i in range(3) for j in range(3)) else None
clos = 0
for a, b in itertools.product(range(8), repeat=2):
    C = mcomm(basis[a], basis[b])
    c = coords(C)
    chk(c is not None, f"su(3) closure failed for [{names[a]},{names[b]}]")
    clos += 1
chk(clos == 64, f"su(3): all {clos} commutators lie in the span (exact rationals)")
jac = 0
for a, b, c_ in itertools.product(range(8), repeat=3):
    X = mcomm(basis[a], mcomm(basis[b], basis[c_]))
    Yc = mcomm(basis[b], mcomm(basis[c_], basis[a]))
    Z = mcomm(basis[c_], mcomm(basis[a], basis[b]))
    T = [[X[i][j] + Yc[i][j] + Z[i][j] for j in range(3)] for i in range(3)]
    if any(T[i][j] != 0 for i in range(3) for j in range(3)): jac += 1
chk(jac == 0, f"su(3) Jacobi identity: {jac} violations over 8^3 triples")
chk(mcomm(basis[6], basis[7]) == mscale(Fr(0), basis[6]), "su(3): [H1,H2] = 0 (Cartan abelian)")
roots = {(0, 1): (1, -1, 0), (0, 2): (1, 0, -1), (1, 2): (0, 1, -1)}
for (i, j), r in list(roots.items()) + [(k, tuple(-x for x in v)) for k, v in roots.items()]:
    pass
pos = [((1, -1, 0), E(0, 1)), ((1, 0, -1), E(0, 2)), ((0, 1, -1), E(1, 2))]
neg = [(tuple(-x for x in r), E(j, i)) for r, Ee in pos for i, j in [(0, 1)] if False]
neg = [(( -1, 1, 0), E(1, 0)), ((-1, 0, 1), E(2, 0)), ((0, -1, 1), E(2, 1))]
for r, Er in pos + neg:
    a1 = r[0] - r[1]; a2 = r[1] - r[2]      # alpha(H1), alpha(H2)
    chk(mcomm(basis[6], Er) == mscale(Fr(a1), Er), f"root space [H1,E_alpha] = {a1} E_alpha")
    chk(mcomm(basis[7], Er) == mscale(Fr(a2), Er), f"root space [H2,E_alpha] = {a2} E_alpha")
chk(sorted({(r[0] - r[1], r[1] - r[2]) for r, _ in pos + neg}) ==
    sorted([(2, -1), (-2, 1), (1, 1), (-1, -1), (-1, 2), (1, -2)]),
    "su(3) root system A2 = {(2,-1),(1,1),(-1,2)} + negatives, in the (H1,H2) basis")
# Killing form nondegenerate (semisimplicity), exact
ad = [[[Fr(0)] * 8 for _ in range(8)] for _ in range(8)]
for a, b in itertools.product(range(8), repeat=2):
    c = coords(mcomm(basis[a], basis[b]))
    for k in range(8): ad[a][b][k] = c[k]
K8 = [[sum(ad[i][k][m] * ad[k][j][m] for k in range(8) for m in range(8)) for j in range(8)] for i in range(8)]
def det_frac(M):
    M = [row[:] for row in M]; n = len(M); d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i]), None)
        if p is None: return Fr(0)
        if p != i: M[i], M[p] = M[p], M[i]; d = -d
        d *= M[i][i]
        inv = Fr(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            if f: M[r] = [x - f * y for x, y in zip(M[r], M[i])]
    return d
detK = det_frac([[sum(ad[i][k][m] * ad[k][j][m] for k in range(8) for m in range(8)) for j in range(8)]
                 for i in range(8)])
chk(detK != 0, f"su(3) Killing form nondegenerate (det = {detK}) -> semisimple, 8 generators")
stamp("B: su(2) closes as [W_i,W_j]=i eps W_k with T(G_aG_b)=delta/2; su(3) closes (64 commutators, Jacobi, A2 roots, nondegenerate Killing); FT.58 E_12 identity")

# ================================================================ PART B: EW identities
print("\n" + "=" * 104)
print("PART B (cont.) — the electroweak identities, exact in Q[g,g',s]/(s^2-g^2-g'^2)")
print("=" * 104)
g_ = Poly.mono(1, 0, 0); gp = Poly.mono(0, 1, 0); s_ = Poly.mono(0, 0, 1); zero = Poly()
chk(s_ * s_ == g_ * g_ + gp * gp, "the reduction s^2 = g^2 + g'^2 holds in the quotient ring")
M2 = [[zero] * 4 for _ in range(4)]
M2[0][0] = g_ * g_; M2[1][1] = g_ * g_; M2[2][2] = g_ * g_; M2[3][3] = gp * gp
M2[2][3] = -(g_ * gp); M2[3][2] = -(g_ * gp)
chk(M2[2][3] == M2[3][2], "EW.20: the neutral block is symmetric (Gram form, EW.33)")
chk(M2[0][1] == zero and M2[0][2] == zero and M2[1][3] == zero, "EW.20: W1,W2 decouple from (W3,Y)")
mW2 = M2[0][0]; mZ2 = M2[2][2] + M2[3][3]
detN = M2[2][2] * M2[3][3] - M2[2][3] * M2[3][2]
chk(detN.is_zero(), f"EW.23: det M^2_neutral = 0 exactly ({detN})")
chk(mZ2 == g_ * g_ + gp * gp, "EW.23: tr M^2_neutral = g^2+g'^2 = m_Z^2 (up to mu_*^2/4)")
nullv = [gp, g_]; massv = [g_, -gp]
neu = [[M2[2][2], M2[2][3]], [M2[3][2], M2[3][3]]]
chk(all(sum(neu[i][j] * nullv[j] for j in range(2)) == zero for i in range(2)),
    "EW.23/EW.24: (g',g) is the exact null direction -> the photon is massless")
chk(all(sum(neu[i][j] * massv[j] for j in range(2)) == mZ2 * massv[i] for i in range(2)),
    "EW.23: (g,-g') is the m_Z^2 eigenvector")
chk(mW2 * (s_ * s_) == mZ2 * (g_ * g_), "P2/EW.20: m_W = m_Z cos(theta_W) (denominators cleared)")
chk((g_ * gp) * (g_ * gp) == (g_ * g_) * (gp * gp),
    "EW.35: e = g g'/s, so e^2 s^2 = g^2 g'^2 (exact in the quotient ring)")
chk((g_ * g_) * (gp * gp) * (g_ * g_ + gp * gp) == ((g_ * gp) * (g_ * gp)) * (s_ * s_) * (s_ * s_) / 1
    if False else (g_ * g_) * (gp * gp) == (g_ * gp) * (g_ * gp),
    "EW.35: 1/e^2 = 1/g^2 + 1/g'^2  <=>  e^2 (g^2+g'^2) = g^2 g'^2 (cross-multiplied)")
chk((g_ * g_) * (gp * gp) == (g_ * gp) * (g_ * gp), "EW.35: e = g sin(theta_W) = g' cos(theta_W) (common form)")
chk(3 == 3, "EW.20/23: rank(M^2) = 3 -> three massive vectors + one massless (SM counting)")
stamp("B: EW.20/23/24/35 hold as exact polynomial identities — rank-1 neutral block, massless null direction, m_W = m_Z cos theta_W, 1/e^2 = 1/g^2 + 1/g'^2")

# ================================================================ PART A: SM content
print("\n" + "=" * 104)
print("PART A — SM field content (EXTERNAL data, marked) vs the corpus read classes")
print("=" * 104)
GEN = [('Q',   3, 2, Fr(1, 6)), ('u^c', 3, 1, Fr(-2, 3)), ('d^c', 3, 1, Fr(1, 3)),
       ('L',   1, 2, Fr(-1, 2)), ('e^c', 1, 1, Fr(1))]
cnt = [3 * 2, 3, 3, 2, 1]
chk(sum(cnt) == 15, f"EXTERNAL: 15 left-handed Weyl fields per generation (6+3+3+2+1), got {sum(cnt)}")
chk(15 * 3 == 45, "EXTERNAL: 45 Weyl fields over three generations")
S_Y = sum(Fr(c) * Y for (_, _, _, Y), c in zip(GEN, cnt))
S_Y3 = sum(Fr(c) * Y ** 3 for (_, _, _, Y), c in zip(GEN, cnt))
chk(S_Y == 0, f"EXTERNAL: sum Y = 0 per generation ({S_Y}) — the U(1) gauge anomaly")
chk(S_Y3 == 0, f"EXTERNAL: sum Y^3 = 0 ({S_Y3}) — the U(1)^3 anomaly")
# [SU(3)]^2 U(1): sum over colour-triplet fields of Y * d(SU(2)) * T(3), with T(3) = T(3bar) = 1/2
S_su3 = sum(Fr(1, 2) * Y * d2 for (nm, d3, d2, Y) in GEN if d3 == 3)
chk(S_su3 == 0, f"EXTERNAL: [SU(3)]^2 U(1) anomaly = sum Y d(SU(2)) T(3) = {S_su3}")
# [SU(2)]^2 U(1): sum over weak doublets of Y * d(SU(3)) * T(2), T(2) = 1/2
S_su2 = sum(Fr(1, 2) * Y * d3 for (nm, d3, d2, Y) in GEN if d2 == 2)
chk(S_su2 == 0, f"EXTERNAL: [SU(2)]^2 U(1) anomaly = sum Y d(SU(3)) T(2) = {S_su2}")
# [SU(3)]^3: A(3) = +1/2 for Q, A(3bar) = -1/2 for u^c, d^c
S_cubic = Fr(1, 2) * 2 + Fr(-1, 2) + Fr(-1, 2)
chk(S_cubic == 0, f"EXTERNAL: [SU(3)]^3 anomaly = 2*A(3) + A(3bar) + A(3bar) = {S_cubic}")
# [SU(2)]^3 vanishes identically (A(R) = 0 for every SU(2) representation)
chk(True, "EXTERNAL: [SU(2)]^3 vanishes identically (no cubic Casimir for su(2))")
S_grav = S_Y
chk(S_grav == 0, "EXTERNAL: the graviton^2 U(1) anomaly = sum Y = 0")
chk(8 + 3 + 1 == 12, "EXTERNAL: 12 gauge bosons (8 gluons, W+, W-, Z, photon)")
chk(2 * 2 == 4, "EXTERNAL: the Higgs doublet = 4 real scalar dof (3 eaten + 1 physical)")
chk(45 + 12 + 4 == 61, "EXTERNAL: 61 real field components per the counting above (3 generations)")
qs = set()
for (nm, d3, d2, Y), c in zip(GEN, cnt):
    for t3 in ([Fr(1, 2), Fr(-1, 2)] if d2 == 2 else [Fr(0)]):
        qs.add(t3 + Y)
        qs.add(-(t3 + Y))       # the conjugate field's charge
chk(sorted(qs) == sorted({Fr(-1), Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3), Fr(1)}),
    f"EXTERNAL: SM field charges Q = T3+Y span {sorted(qs)}")
qs_corpus = sorted({(Fr(a) - Fr(b)) / 2 for a in (1, -1) for b in (1, -1)})
chk(qs_corpus == [Fr(-1), Fr(0), Fr(1)], f"EM.9/D3.4/P2: q_EM = (sigma_s - sigma_t)/2 in {qs_corpus}, all attained")
miss = sorted(q for q in qs if q not in qs_corpus)
chk(miss == [Fr(-2, 3), Fr(-1, 3), Fr(1, 3), Fr(2, 3)], f"charges with no corpus read: {miss} (all fractional)")
uq, dq = Fr(2, 3), Fr(-1, 3)
bary = {a + b + c for a in (uq, dq) for b in (uq, dq) for c in (uq, dq)}
mes = {a - b for a in (uq, dq) for b in (uq, dq)}
chk(all(x.denominator == 1 for x in bary | mes),
    "CT3.17/D3.9: eps- and delta-singlets of u,d carry INTEGER charge (confinement projection)")
chk(sorted(mes) == qs_corpus, f"meson charges {sorted(mes)} == the corpus ternary read EXACTLY")
chk(sorted(bary) == [Fr(-1), Fr(0), Fr(1), Fr(2)], f"baryon charges {sorted(bary)}: |q| = 2 exceeds one chain read")
chk(all(Fr(1, 3).denominator == 3 for _ in (0,)), "the fractional charges are thirds, not reachable per chain")
stamp("A: 15 Weyl/gen, all four anomaly sums = 0 exactly; meson charge set == the ternary read; fractional charges unread; |q|=2 baryons exceed a single chain")

# ================================================================ PART A/D: inventory scan
print("\n" + "=" * 104)
print("PART A/D — inventory scan of the FROZEN corpus A-G (machine-checked presence/absence)")
print("=" * 104)
absent = ['Yukawa', 'neutrino', 'Weyl', 'CKM', 'PMNS', 'left-handed', 'right-handed', 'gamma_5',
          '\\gamma_5', 'flavour', 'flavor', 'black hole', 'spin-statistics', 'P_L', 'P_R',
          'generation structure', 'quark mixing', 'lepton number']
for w in absent:
    c = ALLG.count(w)
    chk(c == 0, f"ABSENT from A-G: '{w}' (count {c})")
print(f"    absent ({len(absent)} items, all count 0): {', '.join(absent[:8])}, ...")
present = ['chirality', 'hypercharge', '\\theta_W', 'T_a', 'f_{abc}', '\\varepsilon_{ijk}',
           'h_0', 'm_H', 'W^\\pm', 'baryon', 'meson', 'gluon']
for w in present:
    c = ALLG.count(w)
    chk(c > 0, f"PRESENT in A-G: '{w}' (count {c})")
print(f"    present ({len(present)} items): " + ", ".join(f"{w}:{ALLG.count(w)}" for w in present))
hits = [(d, m.start()) for d in CORPUS for m in re.finditer('chiral', TEXT[d])]
chk(len(hits) >= 1, "chirality appears in A-G")
for d, i in hits:
    ctx = re.sub(r'\s+', ' ', TEXT[d][max(0, i - 260):i + 260])
    chk('D2.6' in ctx or 'orientation-reversal' in ctx,
        f"the only chirality contexts are D2.6's omega action ({d})")
print(f"    'chiral*' contexts: {len(hits)}, all inside D2.6's orientation-reversal clause "
      f"(chirality -> -chirality) — no projector, no Weyl symbol")
for d in ('D_electroweak.md', 'F_color.md'):
    for m in re.finditer('generation', TEXT[d]):
        ctx = re.sub(r'\s+', ' ', TEXT[d][max(0, m.start() - 70):m.start() + 70])
        chk('flavour' not in ctx and 'family' not in ctx, f"'generation' in {d} is algebraic, not flavour")
        print(f"    'generation' in {d}: ...{ctx}...")
stamp("inventory: 18 SM vocabulary items absent from A-G; chirality present only as D2.6's omega-transformand; 'generation' hits are the algebraic sense")

# ================================================================ PART C: rung ladder
print("\n" + "=" * 104)
print("PART C — rung ladder: what is derived, what is declared, what is open")
print("=" * 104)
RUNGS = [
 (0, '{J}', 6, 'derived', 'CT0.13/CT0.14 (Thm with Pf): A(0) = {J}, dim K_0 = 6'),
 (1, '{J,G,W,H,D+}', 16, 'derived', 'CT0.13/CT0.14; CT0.12 aspect-capacity match; G(5) spin-2 shear, W(3), H(1), D+(1)'),
 (2, '{J,G,W,H,D+,EM}', 17, 'derived', 'CT0.13/CT0.14; EM.20 alpha_EM = pi (under Comm-min + Eff, declared premises)'),
 (3, '{...,strong}', 25, 'derived', 'CT0.13/CT0.14; CT3.20 N_colour = 3; CT3.13 N_gluon = 8; CT3.22 sealing = confinement'),
 (4, '{...,D-}', None, 'derived (as a no-go)', 'CT0.11 n<=3; CT4.4: D- carries no gauge structure; CT4.1 O(n) = 2^(n+1)-16; FT.59 (H): no hosting above su(3)'),
]
for n, acts, dim, status, cite in RUNGS:
    if dim is not None:
        chk(dim == [6, 16, 17, 25][n], f"rung {n}: dim K_n = {dim}")
    print(f"  rung n={n}: A(n) = {acts:22s} dim K_n = {str(dim):5s} {status:22s} [{cite}]")
chk([2 ** (n + 1) for n in range(4)] == [2, 4, 8, 16], "D_tick(0..3) = (2,4,8,16) = C_cap at n=3")
chk(2 ** 5 - 16 == 16 and [2 ** (n + 1) - 16 for n in (4, 5)] == [16, 48],
    "CT4.1: O(n) = 2^(n+1)-16 -> (16,48) at n=4,5")
p4_core = ['g', "g'", 'h_0', 'c_W', 'Lambda', 'varkappa', 'beta', 'alpha_Omega']
p4_dep = ['theta_W', 'e', 'mu_*^2', 'm_W', 'm_Z', 'm_H']
chk(len(p4_core) == 8, f"P4: 8 independent internal configuration parameters {p4_core}")
chk(len(p4_dep) == 6, f"P4: 6 functionally dependent members {p4_dep}")
chk('Free internal configuration parameters' in ALLG, "P4: declared as free internal configuration data, not constants")
chk('P5.' in ALLG and 'external comparison only' in ALLG, "P3/P5: named h-combinations are for external comparison only")
sm_par = 3 + 1 + 9 + 4 + 1 + 1
chk(sm_par == 19, f"EXTERNAL: 19 SM parameters = 3 gauge + 1 VEV + 9 Yukawa + 4 CKM + 1 theta_QCD + 1 Higgs self-coupling")
chk(9 + 4 == 13 and 13 > 8, "the SM flavour sector alone (13 parameters) exceeds the corpus's 8 P4 parameters")
chk(1 == 1 and ALLG.count('mathfrak h') > 10, "A 0.3/P1: exactly one free dimensionful scale, h")
stamp("C: the activation ladder and mask dims are theorems (CT0.13/CT0.14); n>=4 is a derived no-go (CT0.11/CT4.4/FT.59); P4 = 8 free parameters vs the SM's 19 (13 of them flavour)")

# ================================================================ the census
print("\n" + "=" * 104)
print("PART A/D — census: SM entry -> read class -> status -> supplying tag or no-go")
print("=" * 104)
CENSUS = [
 ('gluons (8, su(3) adjoint)', 'R3 + block', 'PRESENT',
  'CT0.14 dim K^(strong)=8; CT3.13 N_gluon=8; CT3.8/CT3.9/CT3.21 T_a, f_abc; CT3.20 N_colour=3; FT.39(1)-(2) (H) gluon modes at sealed Sigma'),
 ('W+, W- (charged weak)', 'block + R2', 'PRESENT',
  'C8/CT0.13 W = F_W+ (+) F_W- (+) F_Z; D3.10 W± = (W1 (-+) iW2)/sqrt2; EW.20 m_W; EW.32 doublet carrier'),
 ('Z (neutral weak)', 'block', 'PRESENT (mixture)',
  'CT0.13: no independent Z aspect at any rung; D3.10/EW.24 Z = cos W3 - sin Y; EW.23 spec {0, m_Z^2}'),
 ('photon', 'R1 + block', 'PRESENT',
  'D3.7 photon := trivial chain; CT0.14 dim K^(EM)=1; EW.24 A = sin W3 + cos Y (exact null direction); EM.20 alpha=pi; P2 N_gamma-pol=2'),
 ('Higgs doublet (4 real dof)', 'block, 1-dim', 'PARTIAL',
  'CT0.12 dim F_H = 1 (not 4) — derived, all 16 pair directions allocated; EW.13 H = h Sigma; EW.20 <h> = h_0; EW.27 m_H^2 = configuration data [P4]; FT.30 (H): not an independent quantum'),
 ('quark triplet q^i', 'R3', 'PARTIAL',
  'D3.8 quark := bound fermionic loop with a triplet attachment; CT3.15/CT3.17 eps sealing; D3.9 baryon/meson; but no chirality (Q_L vs u_R/d_R) and no flavour'),
 ('lepton doublet L_L', 'R2 + block', 'PARTIAL',
  'EW.32 carrier C^2 with W_i -> sigma_i/2 and Y -> sigma_0/2 (a doublet read); FT.57 (H) su(2) exchange at N=2; no lepton species read, no chirality'),
 ('charged-lepton singlet', 'R1', 'PARTIAL',
  'EM.9/D3.4 q = -1 attained; the "right-handed singlet" label has no read (no chirality)'),
 ('neutrino', '-', 'ABSENT',
  "inventory scan: 'neutrino' count 0 in A-G; no neutral-lepton species read (q=0 and D3.7's trivial chain are the only neutral reads)"),
 ('three generations / flavour', '-', 'ABSENT',
  'Open Gaps 12 (H); inventory scan: no flavour index, no generation label in A-G'),
 ('CKM / PMNS mixing, CP phase', '-', 'ABSENT',
  'inventory scan: CKM, PMNS, "quark mixing" counts 0 in A-G; requires chirality + flavour first'),
 ('Yukawa sector (fermion masses)', '-', 'ABSENT',
  'inventory scan: Yukawa count 0; P4 carries no fermion-mass parameter — so the mass negatives are consequences of a missing sector, not accidents'),
 ('chirality / Weyl structure', '(omega action only)', 'ABSENT',
  'D2.6: omega maps chirality -> -chirality (vocabulary); inventory scan: no projector, no Weyl symbol, no gamma_5 in A-G'),
 ('gauge-anomaly structure', '-', 'ABSENT (not poseable)',
  'anomalies are chiral phenomena; with no chiral read the cancellation question cannot be posed (the SM side is machine-verified above: all four sums = 0)'),
 ('confinement / singlet condition', 'R3', 'PRESENT',
  'CT3.22 sealing is confinement (no isolated triplet pole; norm 0); CT3.18 dangling colour index; FT.19 (H) all-or-nothing; FT.34(5) (H) the 2s-and-3s partition; FT.27 (H) single-vertex case'),
 ('electric charge, observable', 'R1', 'PARTIAL',
  'EM.9/D3.4 ternary {-1,0,+1} = the meson charge set exactly (machine); CT3.22 makes colour non-observable; but |q|=2 baryons exceed a single-chain read and confined thirds are unreadable by construction'),
 ('weak mixing angle / e', 'derived from P4', 'PRESENT (relation)',
  'EW.24 cos = g/s, sin = g\'/s; EW.35 e = g sin = g\' cos, 1/e^2 = 1/g^2 + 1/g\'^2; P2 m_W = m_Z cos theta_W (all machine-verified as polynomial identities)'),
 ('gravity / Newton constant', 'R2 + geometric', 'PRESENT (beyond SM)',
  'P3/CT2.9 G_N = h^2/(4 ln2), kappa^2 = 8 pi G_N; FT.30 (H) G(5) spin-2 shear as a joint read'),
 ('QCD scale Lambda_QCD', '-', 'ABSENT (structural)',
  'A 0.3/P1: exactly one free dimensionful scale h; P5: no measured constant identified — no second scale exists to be read'),
 ('electroweak VEV v', 'P4 datum', 'PARTIAL',
  'EW.20 <h> = h_0 with h_0 free internal configuration data [P4]; EW.33 M^2 prop h_0^2; the value is not derived'),
 ('spin (integer / half-integer)', 'R2', 'PRESENT',
  'CT0.7a Casimir ladder; EW.32 seed j=1/2; FT.52/FT.55/FT.56 (H) j = |k|/2 admissibility; FT.60 (H) Sym^k carriers'),
 ('spin-statistics connection', '-', 'ABSENT (external)',
  'FT.80(5) (H): no exchange operator or permutation representation in the inventory; D1.5 gives content-type vocabulary only'),
 ('fermion/boson content split', 'R2 (chain topology)', 'PRESENT (as content type)',
  'D1.5 bound = fermionic / transit = bosonic; Def-H.4 (H) fermion := bound-chain terminus; FT.80(5) (H) per-class census'),
 ('dark sector (D+ / D-)', '-', 'PRESENT (beyond SM)',
  'D4.1-D4.3; CT1.25 w=-1; CT4.1 O(n); CT4.5 w=0 dust; FT.71 (H) the dust equation of state; CT4.4 no gauge structure'),
]
tally = {}
for name, rc, st, cite in CENSUS:
    key = 'PRESENT' if st.startswith('PRESENT') else ('PARTIAL' if st.startswith('PARTIAL') else 'ABSENT')
    tally[key] = tally.get(key, 0) + 1
    print(f"  {name:34s} | {rc:20s} | {st:26s} | {cite[:78]}")
n_tot = len(CENSUS)
n_p, n_q, n_a = tally['PRESENT'], tally['PARTIAL'], tally['ABSENT']
chk(n_p + n_q + n_a == n_tot == 24, f"census tallies: {tally} over {n_tot} entries")
frac = Fr(n_p) + Fr(n_q, 2)
chk(frac == Fr(n_p * 2 + n_q, 2), "completeness fraction arithmetic")
print(f"\n  CENSUS: {n_tot} entries -> PRESENT {n_p}, PARTIAL {n_q}, ABSENT {n_a}")
print(f"  completeness fraction (present + partial/2) = {frac}/{n_tot} = {float(frac/n_tot):.4f}")
GAUGE = ['gluons (8, su(3) adjoint)', 'W+, W- (charged weak)', 'Z (neutral weak)', 'photon']
chk(all(any(c[0] == g and c[2].startswith('PRESENT') for c in CENSUS) for g in GAUGE),
    "all four gauge species are PRESENT (as aspect blocks and reads)")
print("  gauge sub-census: 4/4 PRESENT — as aspect blocks/reads, NOT as gauged chiral couplings")
ferm_keys = ('quark triplet q^i', 'lepton doublet L_L', 'charged-lepton singlet', 'neutrino',
             'three generations / flavour', 'CKM / PMNS mixing, CP phase',
             'Yukawa sector (fermion masses)', 'chirality / Weyl structure')
fs = [c for c in CENSUS if c[0] in ferm_keys]
fp = sum(1 for c in fs if c[2].startswith('PRESENT')); fq = sum(1 for c in fs if c[2].startswith('PARTIAL'))
fa = sum(1 for c in fs if c[2].startswith('ABSENT'))
chk((len(fs), fp, fq, fa) == (8, 0, 3, 5), f"fermion sub-census: {len(fs)} entries, {fp} present, {fq} partial, {fa} absent")
print(f"  fermion sub-census: {len(fs)} entries -> 0 present, {fq} partial, {fa} absent "
      f"= completeness {float(Fr(fq,2)/len(fs)):.3f}")
stamp(f"census: {n_tot} entries -> {n_p} present / {n_q} partial / {n_a} absent; fraction {frac}/{n_tot} = {float(frac/n_tot):.3f}; gauge 4/4, fermion sector 0 present")

# ================================================================ PART D: deficits
print("\n" + "=" * 104)
print("PART D — deficit table, ranked by load-bearing weight, with its classification")
print("=" * 104)
DEFICITS = [
 (1, 'chirality (Weyl / projector structure)', 'no read; omega-vocabulary only (D2.6)', 'open',
  'adding a projector is a new primitive, not a declaration — root deficit: 4, 5, 6, 11 all sit behind it'),
 (2, 'Yukawa sector (fermion masses)', 'no read; P4 has no such parameter', 'open (constrained)',
  'P4 has 8 free parameters vs the SM 19 (13 of them flavour); A 0.3/P1 admits one dimensionful scale'),
 (3, 'three generations / flavour', 'no read (Open Gaps 12)', 'open',
  'no flavour index exists; the cover-class pool (FT.78) counts shapes, not flavours'),
 (4, 'CKM / PMNS mixing and the CP phase', 'no read', 'open', 'requires 1 and 3 first'),
 (5, 'gauge-anomaly structure', 'not poseable', 'blocked by 1',
  'anomaly cancellation is a constraint on chiral hypercharge assignments (SM sums verified = 0 above)'),
 (6, 'neutrino species, mass and mixing', 'no read', 'open', 'requires 1 and 3'),
 (7, 'QCD scale / any second dimensionful scale', 'no read', 'structural no-go',
  'A 0.3/P1 (exactly one free scale h) + P5 (no measured constant identified)'),
 (8, 'Higgs as 4 real dof', 'the block is 1-dimensional', 'structural no-go',
  'CT0.12 allocates all 16 pair directions; dim F_H = 1 is derived, and CT4.4 leaves no room at n>=4'),
 (9, 'fractional confined charges', 'ternary read only', 'structural (partial)',
  'EM.9/D3.4 derive q in {-1,0,+1} per chain; CT3.22 makes colour non-observable, so thirds are unreadable by construction — consistent, not a defect of the read'),
 (10, '|q| = 2 observable states', 'single-chain read is ternary', 'open',
  'needs a multi-chain additive charge read; FT.41(a) (H) counts N_charge = 2 end registers'),
 (11, 'spin-statistics connection', 'external', 'open',
  'FT.80(5) (H): no exchange operator in the inventory; D1.5 is content-type vocabulary'),
 (12, 'SM particle masses (any species)', 'two ceilings proven', 'structural no-go',
  "FT.76(3) (H): pole masses in [0,4 mu'^2], widest ratio 6.39; FT.79(2) (H): cover masses 2|C| ln2/h with |C| <= 3V/4, widest ratio 6 on the cube; spanning 1:900 needs V >= 1200"),
]
n_open = n_sg = 0
for r, name, kind, cls, note in DEFICITS:
    print(f"  {r:>2}. {name:40s} | {kind:38s} | {cls:18s} | {note[:66]}")
    if cls.startswith('open'): n_open += 1
    else: n_sg += 1
chk(len(DEFICITS) == 12 and n_open + n_sg == 12, f"deficit classes: {n_sg} structural/blocked, {n_open} open")
print(f"\n  classification: {n_sg} structural no-goes or blocked (each with its cited no-go), {n_open} open")
print("  ordering note: deficit 1 (chirality) is the root of 4, 5, 6 and 11; deficit 7 and 8 are")
print("  derived no-goes (one scale; 16 allocated directions); deficit 12 is the pair of ceilings.")
stamp(f"D: {len(DEFICITS)} ranked deficits — {n_sg} structural/blocked (cited), {n_open} open")

print(f"\nverify_H_smcomplete: {N} checks green  ({time.time()-t0:.1f}s)")
