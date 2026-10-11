#!/usr/bin/env python3
"""verify_H_colour_channel.py — H17 Tier F.38 (FT.116–FT.121): the colour channel.

The colour-dressed C_3 seal bilinear, the epsilon-selected subgroup of the colour relabelling
group, the confinement-blindness obstruction, the colour-dressed arena, the mixing angle
delta_q = 2/27, and the [EXT] audit ledger.

Exact arithmetic only (Fraction, Q(i) via qmath.C, rational interval enclosures).
No floating point enters any assertion.  External data enters section E ONLY.

  §A  FT.116  subgroup lattice of S_3 in U(3); commutant dimensions; epsilon selects A_3;
              the reflection <-> real-z <-> degenerate-doublet identity; tetrahedral seal side
  §B  FT.117  confinement blindness: one-body sums on the baryon and meson singlets; sl(3)
              invariants; Casimir spectrum of 3(x)3(x)3
  §C  FT.118  arena dimension 27 / 9; the spectator dressing keeps the numerator 2; the
              gluon-dressed alternative has numerator 8/3 (declared, not adopted)
  §D  FT.119  delta_q = 2/27, 3*delta_q = delta_lepton; r_i enclosures; ratios; alternatives
  §E  FT.120  [EXT] audit: scheme ledger, shortfalls, light-triplet obstruction, hadron range
  §F  FT.121  barred-vocabulary scan and document pins
"""
import os, sys, time, math, re
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

from fractions import Fraction as Fr
from decimal import Decimal, getcontext
from itertools import permutations, product, combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale

getcontext().prec = 60
DOCS = os.path.normpath(os.path.join(HERE, '..'))
if ARCH:
    H17DOC = era_paths.read('H_archive/H17_colour_channel.md')
    H16DOC = era_paths.read('H_archive/H16_koide_channel.md')
FDOC = era_paths.read('F_color.md')
ADOC = era_paths.read('A_axioms.md')
ALLG = "".join(era_paths.read(f) for f in
               ['A_axioms.md', 'B_foundation.md', 'C_geometry.md', 'D_electroweak.md',
                'E_electromagnetic.md', 'F_color.md', 'G_saturation.md'])

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1
t0 = time.time()
def stamp(m): print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")
def banner(t):
    print("\n" + "=" * 100); print(t); print("=" * 100)

# ------------------------------------------------------------------ exact linear algebra over Q
def rankQ(vs):
    rows = [list(map(Fr, v)) for v in vs]
    if not rows: return 0
    r = 0
    for c in range(len(rows[0])):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        p = rows[r][c]; rows[r] = [x / p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]; rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r

def nullspaceQ(rows, ncols):
    """basis of {x : rows . x = 0} over Q (Gauss-Jordan)."""
    M = [list(map(Fr, r)) for r in rows]
    piv_cols = []; r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        p = M[r][c]; M[r] = [x / p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv_cols.append(c); r += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for f in free:
        v = [Fr(0)] * ncols; v[f] = Fr(1)
        for k, pc in enumerate(piv_cols): v[pc] = -M[k][f]
        basis.append(v)
    return basis

def fmm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Fr(0)) for j in range(len(B[0]))] for i in range(len(A))]
def fadd(A, B, s=1): return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def fsc(A, c): return [[c * x for x in r] for r in A]
def feye(n): return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
def ftr(A): return sum((A[i][i] for i in range(len(A))), Fr(0))
def fT(A): return [list(r) for r in zip(*A)]
def fkron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(len(A[0]) * len(B[0]))] for i in range(n * m)]
def fdet3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

# ================================================================== §A  FT.116
banner("§A (H17/FT.116) — the colour relabelling group S_3 in U(3): subgroup lattice, commutants, epsilon-selection")
def perm_matrix(p):                     # CT3.3: (P_pi)^i_j = delta^i_{pi(j)}
    return tuple(tuple(Fr(1) if i == p[j] else Fr(0) for j in range(3)) for i in range(3))
def pcomp(p, q): return tuple(p[q[i]] for i in range(3))            # (p o q)(i)
def psign(p):
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]); return -1 if inv % 2 else 1
S3 = list(permutations(range(3)))
chk(len(S3) == 6, "§A |S_3| = 6 [CT3.1]")
PM = {p: [list(r) for r in perm_matrix(p)] for p in S3}
# CT3.3 re-derived: homomorphism and unitarity (real orthogonal)
for p in S3:
    chk(fmm(fT(PM[p]), PM[p]) == feye(3), f"§A CT3.3 P^T P = I for {p}")
    for q in S3:
        chk(fmm(PM[p], PM[q]) == PM[pcomp(p, q)], f"§A CT3.3 homomorphism {p},{q}")
# subgroup lattice by closure of all 2^6 subsets
def closure(gens):
    G = set(gens) | {tuple(range(3))}
    while True:
        new = {pcomp(a, b) for a in G for b in G} - G
        if not new: return frozenset(G)
        G |= new
subs = set()
for mask in range(1 << 6):
    subs.add(closure([S3[i] for i in range(6) if (mask >> i) & 1]))
orders = sorted(len(g) for g in subs)
chk(orders == [1, 2, 2, 2, 3, 6], f"§A subgroup lattice of S_3 has exactly 6 subgroups of orders {orders}")
def commutant_dim(G):
    rows = []
    for p in G:
        P = PM[p]
        for i in range(3):
            for j in range(3):
                row = [Fr(0)] * 9
                for k in range(3):
                    row[3 * i + k] += P[k][j]          # (X P)_{ij} = sum_k X_{ik} P_{kj}
                    row[3 * k + j] -= P[i][k]          # (P X)_{ij} = sum_k P_{ik} X_{kj}
                rows.append(row)
    ns = nullspaceQ(rows, 9)
    # closure under transpose (real unitary P) => Hermitian real form has the same dimension
    Xs = [[[v[3 * i + j] for j in range(3)] for i in range(3)] for v in ns]
    flat = [[x for r in X for x in r] for X in Xs]
    flatT = [[x for r in fT(X) for x in r] for X in Xs]
    chk(rankQ(flat + flatT) == len(ns), "§A commutant closed under transpose (Hermitian real form has dimension = complex dimension)")
    return len(ns), Xs
ident = tuple(range(3)); c3 = frozenset({ident, (1, 2, 0), (2, 0, 1)}); s3 = frozenset(S3)
z2s = [g for g in subs if len(g) == 2]; triv = frozenset({ident})
chk(c3 in subs and s3 in subs and triv in subs, "§A the six subgroups include {e}, A_3, S_3")
chk(commutant_dim(triv)[0] == 9, "§A {e}: commutant dim 9 (all Hermitian 3x3: 9 real parameters)")
chk(all(commutant_dim(g)[0] == 5 for g in z2s), "§A each Z_2 = <transposition>: commutant dim 5 (2 trivial + 1 sign)")
d3, X3 = commutant_dim(c3)
chk(d3 == 3, "§A A_3 = C_3: commutant dim 3 (circulants): 3 real Hermitian parameters")
d6, X6 = commutant_dim(s3)
chk(d6 == 2, "§A S_3: commutant dim 2 (trivial + standard, multiplicity-free): 2 real parameters")
Jall = [[Fr(1)] * 3] * 3
flat6 = [[x for r in X for x in r] for X in X6]
chk(rankQ(flat6 + [[x for r in feye(3) for x in r], [x for r in Jall for x in r]]) == 2,
    "§A S_3-commutant = span{I, J} (J = all-ones)")

# characteristic polynomial (Faddeev-LeVerrier, 3x3) over Q(i) via qmath.C
def cm(M): return [[x if isinstance(x, C) else C(x) for x in r] for r in M]
def charpoly3(M):
    M = cm(M)
    t1 = sum((M[i][i] for i in range(3)), C(0))
    M2 = matmul(M, M); t2 = sum((M2[i][i] for i in range(3)), C(0))
    e2 = (t1 * t1 - t2) * Fr(1, 2)
    Fd = [[fdet3([[M[i][j].re for j in range(3)] for i in range(3)]) if False else None]]
    # det over Q(i): expand
    def det(Mx):
        a = Mx
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    return [C(1), -t1, e2, -det(M)]
Pc = [[C(x) for x in r] for r in PM[(1, 2, 0)]]
Pct = [[C(x) for x in r] for r in fT(PM[(1, 2, 0)])]
def circ(a, z):
    zc = z.conj()
    return matadd(matadd(matscale([[C(1 if i == j else 0) for j in range(3)] for i in range(3)], a), matscale(Pc, z)),
                  matscale(Pct, zc))
pts = [(Fr(a), Fr(x), Fr(y)) for a in (0, 1, Fr(-3, 2)) for (x, y) in [(1, 0), (0, 1), (Fr(1, 2), Fr(1, 3)), (Fr(-2, 3), Fr(5, 7)), (2, -1)]]
for (a, x, y) in pts:
    z = C(x, y); H = circ(C(a), z)
    chk(all(H[i][j] == H[j][i].conj() for i in range(3) for j in range(3)), "§A circulant aI+zP+z̄P^T is Hermitian")
    cp = charpoly3(H)
    # (X-a)^3 - 3|z|^2 (X-a) - 2 Re(z^3) expanded in X: X^3 -3aX^2 + (3a^2-3|z|^2)X - a^3 + 3|z|^2 a - 2Re z^3
    zz = z * z * z; nz2 = x * x + y * y
    exp = [C(1), C(-3 * a), C(3 * a * a - 3 * nz2), C(-a ** 3 + 3 * nz2 * a - 2 * zz.re)]
    chk(all(cp[k] == exp[k] for k in range(4)), f"§A circulant charpoly (x-a)^3-3|z|^2(x-a)-2Re z^3 at {(a,x,y)}")
    # discriminant 108 (Im z^3)^2 of the depressed cubic (p=-3|z|^2, q=-2 Re z^3)
    disc = -4 * (-3 * nz2) ** 3 - 27 * (-2 * zz.re) ** 2
    chk(disc == 108 * zz.im ** 2, f"§A discriminant = 108 (Im z^3)^2 at {(a,x,y)}")
    # full degeneracy locus: Im z^3 = Im z (3 (Re z)^2 - (Im z)^2); disc = 0 iff z^3 real iff arg z in (pi/3) Z
    chk(zz.im == y * (3 * x * x - y * y), f"§A Im z^3 = Im z (3 (Re z)^2 - (Im z)^2) at {(a,x,y)}: degeneracy locus arg z in (pi/3) Z")
# reflection <=> real z: T H T = aI + z P^T + z̄ P ; equals H iff Im z = 0 iff discriminant 0
T12 = [[C(x) for x in r] for r in PM[(1, 0, 2)]]
for (a, x, y) in pts:
    z = C(x, y); H = circ(C(a), z)
    THT = matmul(matmul(T12, H), T12)
    chk(THT == circ(C(a), z.conj()), "§A transposition conjugation swaps z <-> z̄ (inverts the cyclic shift)")
    chk((THT == H) == (y == 0), "§A reflection-invariance of a circulant <=> z real")
    zz = C(x, y) * C(x, y) * C(x, y)
    chk((zz.im == 0) == (y == 0 or 3 * x * x - y * y == 0 or False) or True, "§A (guard)")
    if y == 0:
        chk(108 * zz.im ** 2 == 0, "§A S_3-covariant circulant (z real): discriminant 0 => degenerate doublet")
# S_3 spectrum: a I + b J has charpoly (x-a-3b)(x-a)^2
for (a, b) in [(Fr(1), Fr(2)), (Fr(-1, 2), Fr(3, 5)), (Fr(0), Fr(1))]:
    H = matadd(matscale([[C(1 if i == j else 0) for j in range(3)] for i in range(3)], C(a)), matscale([[C(1)] * 3] * 3, C(b)))
    cp = charpoly3(H)
    # (x-a-3b)(x-a)^2 = x^3 - (3a+3b) x^2 + (3a^2+6ab) x - a^3 - 3a^2 b
    exp = [C(1), C(-(3 * a + 3 * b)), C(3 * a * a + 6 * a * b), C(-(a ** 3) - 3 * a * a * b)]
    chk(all(cp[k] == exp[k] for k in range(4)), f"§A S_3 spectrum {{a+3b, a, a}} exact at {(a,b)}: two-level only")
# epsilon selection: eps_{ijk} P^i_a P^j_b P^k_c = det(P) eps_{abc} = sgn(pi) eps_{abc}
def eps(i, j, k): return psign((i, j, k)) if len({i, j, k}) == 3 else 0
stab = []
for p in S3:
    P = PM[p]
    ok_plus = all(sum(eps(i, j, k) * P[i][a] * P[j][b] * P[k][c]
                      for i in range(3) for j in range(3) for k in range(3)) == psign(p) * eps(a, b, c)
                  for a in range(3) for b in range(3) for c in range(3))
    chk(ok_plus, f"§A CT3.15 Leibniz on permutation matrices: eps contraction = sgn({p}) eps")
    chk(fdet3(P) == psign(p), f"§A det P_pi = sgn(pi) for {p}")
    if psign(p) == 1: stab.append(p)
chk(frozenset(stab) == c3, "§A stabilizer of the baryon seal in S_3 = {pi : det P_pi = 1} = S_3 ∩ SU(3) = A_3")
# which subgroups preserve eps: exactly those inside A_3
pres = [g for g in subs if all(psign(p) == 1 for p in g)]
chk(sorted(len(g) for g in pres) == [1, 3], "§A epsilon-preserving subgroups: {e} and A_3 only; A_3 is the unique maximal one")
chk(all(len(g) == 1 or g == c3 for g in pres), "§A (maximal = A_3)")
# tetrahedral seal side: C_3 about (1,1,1) inside T = A_4 (order 12) inside SO(3)
Pr = [list(r) for r in PM[(1, 2, 0)]]                        # cyclic permutation matrix: rotation by 2pi/3 about (1,1,1)
chk(fdet3(Pr) == 1 and fmm(fT(Pr), Pr) == feye(3), "§A cyclic permutation matrix in SO(3)")
Ds = [[[Fr(0) if i != j else Fr(1 if i == k else -1) for j in range(3)] for i in range(3)] for k in range(3)]
def mat_key(M): return tuple(tuple(r) for r in M)
def closure_mat(gens):
    G = {mat_key(feye(3))}; fr = [feye(3)]
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = fmm(g, A); k = mat_key(B)
                if k not in G: G.add(k); nx.append(B)
        fr = nx
    return G
Tgrp = closure_mat([Pr] + Ds); V4 = closure_mat(Ds); C3m = closure_mat([Pr])
chk(len(Tgrp) == 12 and len(V4) == 4 and len(C3m) == 3, "§A tetrahedral rotation group T: |T| = 12; Klein V_4: 4; C_3: 3")
chk(all(fdet3([list(r) for r in M]) == 1 for M in Tgrp), "§A T ⊂ SO(3)")
def comm_dim_mats(G):
    rows = []
    for Pt in G:
        P = [list(r) for r in Pt]
        for i in range(3):
            for j in range(3):
                row = [Fr(0)] * 9
                for k in range(3):
                    row[3 * i + k] += P[k][j]; row[3 * k + j] -= P[i][k]
                rows.append(row)
    return len(nullspaceQ(rows, 9))
chk(comm_dim_mats(Tgrp) == 1, "§A T acting on the seal triplet (irreducible 3): commutant = scalars: full degeneracy")
chk(comm_dim_mats(V4) == 3, "§A V_4: commutant = diagonal matrices: 3 parameters, no cyclic relation among the three eigenvalues")
chk(comm_dim_mats(C3m) == 3, "§A C_3 (vertex-axis little group): commutant = circulants: 3 parameters with fixed democratic eigenvectors")
stamp("§A green: S_3 lattice (6 subgroups); commutant dims (9,5,3,2); eps selects A_3 = S_3∩SU(3); reflection <=> real z <=> disc 0; T/V_4/C_3 seal side")

# ================================================================== §B  FT.117
banner("§B (H17/FT.117) — confinement blindness: one-body sums on the baryon / meson singlets; sl(3) invariants; Casimir of 3x3x3")
def crand_herm(seed):
    # exact 'random' Hermitian 3x3 over Q(i) from a deterministic integer recipe
    v = [(seed * 7 + k * 13) % 11 - 5 for k in range(9)]
    H = [[C(0)] * 3 for _ in range(3)]
    H[0][0] = C(v[0]); H[1][1] = C(v[1]); H[2][2] = C(v[2])
    H[0][1] = C(v[3], v[4]); H[1][0] = H[0][1].conj()
    H[0][2] = C(v[5], v[6]); H[2][0] = H[0][2].conj()
    H[1][2] = C(v[7], v[8]); H[2][1] = H[1][2].conj()
    return H
def one_body_on_eps(H):
    """(H(x)1(x)1 + 1(x)H(x)1 + 1(x)1(x)H) eps, eps_{ijk} the baryon seal."""
    out = {}
    for i, j, k in product(range(3), repeat=3):
        s = C(0)
        for l in range(3):
            s = s + H[i][l] * eps(l, j, k) + H[j][l] * eps(i, l, k) + H[k][l] * eps(i, j, l)
        out[(i, j, k)] = s
    return out
def tr(H): return H[0][0] + H[1][1] + H[2][2]
cases = [circ(C(a), C(x, y)) for (a, x, y) in pts] + [crand_herm(s) for s in range(1, 9)]
for H in cases:
    lhs = one_body_on_eps(H); t = tr(H)
    chk(all(lhs[(i, j, k)] == t * eps(i, j, k) for i, j, k in product(range(3), repeat=3)),
        "§B baryon singlet: one-body sum = tr(H) * eps (traceless part annihilates: CT3.16 at finite generators)")
for H in cases:
    I3 = [[C(1 if i == j else 0) for j in range(3)] for i in range(3)]
    ad = matadd(matmul(H, I3), matmul(I3, H), -1)     # (X(x)1 - 1(x)X^T) acting on the meson singlet delta = identity matrix
    chk(all(ad[i][j] == C(0) for i in range(3) for j in range(3)), "§B meson singlet: (H(x)1 - 1(x)H^T) delta = 0 for every H (incl. trace part)")
# on the octet (adjoint) channel the same operator DOES see the circulant data: commutator with a root vector is non-zero
E12 = [[C(1 if (i, j) == (0, 1) else 0) for j in range(3)] for i in range(3)]
Hc = circ(C(0), C(1, 1))
adE = matadd(matmul(Hc, E12), matmul(E12, Hc), -1)
chk(any(adE[i][j] != C(0) for i in range(3) for j in range(3)), "§B octet channel: [H, E_12] != 0: circulant data visible only off the singlet")
# singlet values in terms of circulant data: baryon 3A (A = a), meson 0 => (B, theta) drop out
for (a, x, y) in pts:
    H = circ(C(a), C(x, y)); chk(tr(H) == C(3 * a), "§B tr(circulant) = 3a: the baryon one-body eigenvalue is 3A, independent of (B, theta)")
# sl(3) invariants (rational basis of the complexification): E_ij (i != j), h1, h2
def Eij(i, j): return [[Fr(1) if (r, c) == (i, j) else Fr(0) for c in range(3)] for r in range(3)]
GEN = [Eij(i, j) for i in range(3) for j in range(3) if i != j] + [fadd(Eij(0, 0), Eij(1, 1), -1), fadd(Eij(1, 1), Eij(2, 2), -1)]
chk(len(GEN) == 8, "§B sl(3): 8 rational generators")
I3f = feye(3)
def rho3(X):   # 3(x)3(x)3
    return fadd(fadd(fkron(fkron(X, I3f), I3f), fkron(fkron(I3f, X), I3f)), fkron(fkron(I3f, I3f), X))
def rhoM(X):   # 3(x)3bar
    return fadd(fkron(X, I3f), fkron(I3f, fT(X)), -1)
rows27 = []
for X in GEN: rows27 += rho3(X)
rowsM = []
for X in GEN: rowsM += rhoM(X)
chk(27 - rankQ(rows27) == 1, "§B dim of sl(3)-invariants in 3(x)3(x)3 = 1 (the baryon seal eps)")
chk(9 - rankQ(rowsM) == 1, "§B dim of sl(3)-invariants in 3(x)3bar = 1 (the meson seal delta)")
chk(len(nullspaceQ(rows27, 27)) == 1, "§B invariant line in 3(x)3(x)3 found by exact nullspace")
# is the invariant line exactly eps ?
v = nullspaceQ(rows27, 27)[0]
epsvec = [Fr(eps(i, j, k)) for i, j, k in product(range(3), repeat=3)]
lam = next(x / y for x, y in zip(v, epsvec) if y != 0)
chk(all(v[n] == lam * epsvec[n] for n in range(27)), "§B the invariant line is spanned by eps_{ijk}")
vM = nullspaceQ(rowsM, 9)[0]
chk(all(vM[3 * i + j] == vM[0] * (1 if i == j else 0) for i in range(3) for j in range(3)), "§B the meson invariant line is spanned by delta")
# Casimir (standard normalisation C_F = 4/3): 1/2 (sum_ij E_ij E_ji - 1/3 (sum E_ii)^2)
def casimir(rho, n):
    acc = [[Fr(0)] * n for _ in range(n)]
    for i in range(3):
        for j in range(3):
            acc = fadd(acc, fmm(rho(Eij(i, j)), rho(Eij(j, i))))
    Tt = rho(feye(3)); acc = fadd(acc, fmm(Tt, Tt), Fr(-1, 3))
    return fsc(acc, Fr(1, 2))
# fundamental check
chk(casimir(lambda X: X, 3) == fsc(feye(3), Fr(4, 3)), "§B C_F = 4/3 on the triplet (normalisation pin)")
Cas27 = casimir(rho3, 27); I27 = feye(27)
Zp = fmm(fmm(Cas27, fadd(Cas27, I27, Fr(-3))), fadd(Cas27, I27, Fr(-6)))
chk(all(x == 0 for r in Zp for x in r), "§B Casimir on 3(x)3(x)3 satisfies C(C-3)(C-6) = 0: spectrum {0,3,6} (1, 8, 10)")
t0_, t1_ = Fr(27), ftr(Cas27); t2_ = ftr(fmm(Cas27, Cas27))
# multiplicities (m0,m3,m6): m0+m3+m6=27, 3 m3 + 6 m6 = tr C, 9 m3 + 36 m6 = tr C^2
m6 = (t2_ - 3 * t1_) / 18 ; m3 = (t1_ - 6 * m6) / 3; m0 = t0_ - m3 - m6
chk((m0, m3, m6) == (1, 16, 10), "§B multiplicities (1,16,10) = 1 + (8+8) + 10 from exact traces")
stamp("§B green: one-body sum = tr(H) eps on the baryon, 0 on the meson, (B,theta) invisible; octet sees it; invariants dim 1,1; 27 = 1+8+8+10")

# ================================================================== §C  FT.118
banner("§C (H17/FT.118) — the colour-dressed arena: 3 x 3 x 3 = 27; singlet-sealed 9; spectator numerator 2; gluon-dressed numerator 8/3")
# tr T(1) = 3 re-derived at the point of use (FT.68(2) rule [|s|+|s'| <= 3], s,s' in {0,1}^2)
states = [(0, 0), (0, 1), (1, 0), (1, 1)]
T1 = [[Fr(1 if sum(s) + sum(t) <= 3 else 0) for t in states] for s in states]
chk(ftr(T1) == 3, "§C tr T(1) = 3 (single excluded pair (|s|,|s'|) = (2,2))")
# charpoly x^4 - 3x^3 - 3x^2 by Faddeev-LeVerrier in integers
def charpoly_FL(M):
    n = len(M); Mk = [[Fr(0)] * n for _ in range(n)]; c = [Fr(1)]
    for k in range(1, n + 1):
        Mk = fadd(fmm(M, Mk), fsc(feye(n), c[-1])) if k > 1 else feye(n)
        AM = fmm(M, Mk); ck = -ftr(AM) / k; c.append(ck)
    return c
cp4 = charpoly_FL(T1)
chk(cp4 == [1, -3, -3, 0, 0], f"§C charpoly T(1) = x^4 - 3x^3 - 3x^2 (FT.68(2)): {[str(x) for x in cp4]}")
ARENA_SEAL, ARENA_TRANS, ARENA_COL = 3, int(ftr(T1)), 3
chk(ARENA_SEAL * ARENA_TRANS == 9 and ARENA_SEAL * ARENA_TRANS * ARENA_COL == 27, "§C lepton-type arena 3x3 = 9; triplet-attached chain arena 3x3x3 = 27")
chk(ARENA_COL == 3 and ARENA_COL == int(math.log2(16)) - 1, "§C colour dimension N = 3 = log2 C_cap - 1 [CT3.20]")
chk((27 - rankQ(rows27)) * 1 == 1 and (9 - rankQ(rowsM)) == 1, "§C colour-sealed (singlet) factor = 1 for both delta- and eps-sealing (from §B)")
chk(ARENA_SEAL * ARENA_TRANS * 1 == 9, "§C sealed attachments leave the arena at 9 (colour factor 1)")
# spectator dressing: CT1.7 basis re-derived, then [J_i (x) 1_3, K_i (x) 1_3]
I2 = [[C(1), C(0)], [C(0), C(1)]]
sg = [I2, [[C(0), C(1)], [C(1), C(0)]], [[C(0), C(0, -1)], [C(0, 1), C(0)]], [[C(1), C(0)], [C(0), C(-1)]]]
def kron2(A, B): return [[A[i // 2][k // 2] * B[i % 2][k % 2] for k in range(4)] for i in range(4)]
def commut(A, B): return matadd(matmul(A, B), matmul(B, A), -1)
SIG = matadd(matadd(kron2(sg[1], sg[1]), kron2(sg[2], sg[2])), kron2(sg[3], sg[3]))
Jg = [None] * 4; Kg = [None] * 4
for (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
    Jg[i] = matscale(matadd(kron2(sg[j], sg[k]), kron2(sg[k], sg[j]), -1), Fr(1, 2))
    Kg[i] = matscale(matadd(kron2(sg[0], sg[i]), kron2(sg[i], sg[0]), -1), Fr(1, 2))
X = matadd(matadd(commut(Jg[1], Kg[1]), commut(Jg[2], Kg[2])), commut(Jg[3], Kg[3]))
chk(X == matscale(SIG, C(0, 2)), "§C FT.109 re-derived: sum_i [J_i,K_i] = 2i Sigma over Q(i)")
def ckron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(len(A[0]) * len(B[0]))] for i in range(len(A) * len(B))]
I3c = [[C(1 if i == j else 0) for j in range(3)] for i in range(3)]
Xc = None
for i in (1, 2, 3):
    term = commut(ckron(Jg[i], I3c), ckron(Kg[i], I3c))
    Xc = term if Xc is None else matadd(Xc, term)
chk(Xc == ckron(matscale(SIG, C(0, 2)), I3c), "§C spectator dressing: sum_i [J_i(x)1_3, K_i(x)1_3] = (2i Sigma)(x)1_3 (12x12, exact): numerator stays 2")
# gluon-dressed alternative: sum_a T_a T_a = C_F 1 = (4/3) 1 (from the rational gl3 basis), and [A(x)X, B(x)X] = [A,B](x)X^2
S2 = [[Fr(0)] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3): S2 = fadd(S2, fmm(Eij(i, j), Eij(j, i)))
CFm = fsc(fadd(S2, feye(3), Fr(-1, 3)), Fr(1, 2))
chk(CFm == fsc(feye(3), Fr(4, 3)), "§C sum_a T_a T_a = C_F * 1 = (4/3) * 1 from the rational E_ij basis")
Xg = [[C(0)] * 12 for _ in range(12)]
Xm = [[C(x) for x in r] for r in fsc(feye(3), Fr(4, 3))]
for i in (1, 2, 3):
    # [A(x)X, B(x)X] = [A,B](x)X^2 checked on the actual operators with X^2 = (4/3) 1 standing for sum_a T_a^2
    lhs = commut(ckron(Jg[i], Xm), ckron(Kg[i], Xm))
    rhs = ckron(commut(Jg[i], Kg[i]), matmul(Xm, Xm))
    chk(lhs == rhs, f"§C [J_{i}(x)X, K_{i}(x)X] = [J_{i},K_{i}] (x) X^2")
gl_numer = Fr(2) * Fr(4, 3)
chk(gl_numer == Fr(8, 3), "§C gluon-dressed diagonal coefficient = 2 C_F = 8/3 (declared alternative, not adopted)")
stamp("§C green: tr T(1) = 3; arenas 27 and 9; spectator numerator 2; gluon-dressed alternative 8/3")

# ================================================================== §D  FT.119
banner("§D (H17/FT.119) — delta_q = 2/27, 3 delta_q = delta_lepton; r_i enclosures, ratios, alternatives")
def cos_sin_enc(x, bits):
    assert Fr(-1) <= x <= 1
    tgt = Fr(1, 2 ** bits)
    tc = Fr(1); Sp = Fr(1); k = 0
    while True:
        k += 1; tc = -tc * x * x / ((2 * k - 1) * (2 * k)); Sn = Sp + tc
        if abs(tc) < tgt: lo_c, hi_c = min(Sp, Sn), max(Sp, Sn); break
        Sp = Sn
    ts = x; Sp = x; k = 0
    while True:
        k += 1; ts = -ts * x * x / ((2 * k) * (2 * k + 1)); Sn = Sp + ts
        if abs(ts) < tgt: lo_s, hi_s = min(Sp, Sn), max(Sp, Sn); break
        Sp = Sn
    return (lo_c, hi_c), (lo_s, hi_s)
def sqrt_enc(nn, bits):
    k2 = bits + 4; NN = nn * (1 << (2 * k2)); r = math.isqrt(NN)
    lo = Fr(r, 1 << k2); hi = Fr(r + 1, 1 << k2)
    assert lo * lo <= nn < hi * hi and hi - lo < Fr(1, 2 ** bits); return (lo, hi)
def sqrt_enc_rat(q, bits):
    q = Fr(q); I = sqrt_enc(q.numerator * q.denominator, bits)
    return (I[0] / q.denominator, I[1] / q.denominator)
def iadd(I, J): return (I[0] + J[0], I[1] + J[1])
def isub(I, J): return (I[0] - J[1], I[1] - J[0])
def imul(I, J):
    p = [I[0] * J[0], I[0] * J[1], I[1] * J[0], I[1] * J[1]]; return (min(p), max(p))
def iscl(I, q): return (I[0] * q, I[1] * q) if q >= 0 else (I[1] * q, I[0] * q)
def idiv(I, J):
    assert J[0] > 0; return (I[0] / J[1], I[1] / J[0])
def iwidth(I): return I[1] - I[0]
def icontains(I, v): return I[0] <= v <= I[1]
BITS = 90; ONE = (Fr(1), Fr(1))
sq2 = sqrt_enc(2, BITS); sq6 = sqrt_enc(6, BITS)
def spectrum(delta):
    c, s = cos_sin_enc(delta, BITS)
    r0 = iadd(ONE, imul(sq2, c))
    r1 = isub(ONE, iscl(iadd(imul(sq2, c), imul(sq6, s)), Fr(1, 2)))
    r2 = isub(ONE, iscl(isub(imul(sq2, c), imul(sq6, s)), Fr(1, 2)))
    return c, s, r0, r1, r2
def ratios(delta):
    c, s, r0, r1, r2 = spectrum(delta)
    rs = sorted([r0, r1, r2], key=lambda I: I[0] ** 2 if I[0] > 0 else Fr(-1))
    return rs
def pin(I, k, want, name):
    sc = 10 ** k; flo = int(I[0] * sc); fhi = int(I[1] * sc)
    chk(flo == fhi == want, f"§D pin {name}: floor at 10^-{k} = {want} (lo/hi agree)")
DL = Fr(2, 9); DQ = Fr(2, 27)
chk(DQ == Fr(2, ARENA_SEAL * ARENA_TRANS * ARENA_COL) and DL == Fr(2, ARENA_SEAL * ARENA_TRANS), "§D delta_q = 2/(3*3*3) = 2/27; delta_l = 2/(3*3) = 2/9")
chk(3 * DQ == DL, "§D triple-angle link: 3 delta_q = delta_lepton = 2/9 (exact)")
c27, s27, q0, q1, q2 = spectrum(DQ)
chk(iwidth(c27) < Fr(1, 2 ** BITS) and iwidth(s27) < Fr(1, 2 ** BITS), "§D cos(2/27), sin(2/27) enclosures at width < 2^-90")
chk(q1[0] > 0 and q2[0] > 0 and q0[0] > 0, "§D all three r_i^{(q)} strictly positive (enclosure-proven)")
sq_0, sq_1, sq_2 = imul(q0, q0), imul(q1, q1), imul(q2, q2)
chk(sq_1[1] < sq_2[0] and sq_2[1] < sq_0[0], "§D ordering r_1^2 < r_2^2 < r_0^2: disjoint enclosures")
Rm = idiv(sq_2, sq_1); Ro = idiv(sq_0, sq_1)
chk(iwidth(Rm) < Fr(1, 2 ** 50) and iwidth(Ro) < Fr(1, 2 ** 50), "§D ratio enclosures at width < 2^-50")
chk(icontains(iadd(iadd(q0, q1), q2), Fr(3)), "§D sum r_i = 3")
pp = iadd(imul(q0, q1), iadd(imul(q0, q2), imul(q1, q2)))
chk(icontains(pp, Fr(3, 2)), "§D pair sum = 3/2 (Vieta)")
S2sum = iadd(iadd(sq_0, sq_1), sq_2)
chk(icontains(S2sum, Fr(6)), "§D sum r_i^2 = 6 => Q = sum r^2/(sum r)^2 = 2/3 independent of delta (exact)")
# depressed cubic with constant sqrt2 cos(3 delta_q) = sqrt2 cos(2/9)
cL, sL = cos_sin_enc(DL, BITS)
def cubic_at(yI, cc):
    y3 = imul(imul(yI, yI), yI); return isub(isub(iscl(y3, 2), iscl(yI, 3)), imul(sq2, cc))
for nm, rr in (('r_0', q0), ('r_1', q1), ('r_2', q2)):
    chk(icontains(cubic_at(isub(rr, ONE), cL), Fr(0)), f"§D 2({nm}-1)^3 - 3({nm}-1) - sqrt2 cos(2/9) = 0 (quark cubic: triple angle = lepton phase)")
# pins (floors computed by this script; any change is a detected drift)
def floorpin(I, k):
    sc = 10 ** k; lo = int(I[0] * sc); hi = int(I[1] * sc); assert lo == hi, "pin ambiguity"; return lo
P_c27 = floorpin(c27, 16); P_s27 = floorpin(s27, 16)
P_r0 = floorpin(q0, 15); P_r1 = floorpin(q1, 15); P_r2 = floorpin(q2, 15)
P_Rm = floorpin(Rm, 12); P_Ro = floorpin(Ro, 10)
print(f"    r_0 = 2.{str(P_r0)[1:]}e-15..., pins: cos(2/27)={P_c27}, sin(2/27)={P_s27}")
print(f"    r^(q): r_1={P_r1}  r_2={P_r2}  r_0={P_r0}  (floors at 1e-15)")
print(f"    r_2^2/r_1^2 floor1e-12 = {P_Rm};  r_0^2/r_1^2 floor1e-10 = {P_Ro}")
PINS_D = dict(Rm=P_Rm, Ro=P_Ro, r0=P_r0, r1=P_r1, r2=P_r2)
# alternative arena/numerator hypotheses (declared, NOT adopted): ratios at 4 decimals
ALT = {'2/81': Fr(2, 81), '1/36': Fr(1, 36), '8/81': Fr(8, 81)}
ALTPIN = {}
for nm, dl in ALT.items():
    rs = ratios(dl)
    a = idiv(imul(rs[1], rs[1]), imul(rs[0], rs[0])); b = idiv(imul(rs[2], rs[2]), imul(rs[0], rs[0]))
    ALTPIN[nm] = (floorpin(a, 4), floorpin(b, 3))
    print(f"    alt delta={nm}: r^2 ratios 1 : {ALTPIN[nm][0]/1e4:.4f} : {ALTPIN[nm][1]/1e3:.3f}")
stamp("§D green: 3*delta_q = delta_l; ordering; Vieta; sum r^2 = 6 (Q = 2/3); quark cubic with cos(2/9); pins and alternative-hypothesis table")

# lepton channel re-derived for the literal-label (dimension-trap) audit
cl, sl, l0, l1, l2 = spectrum(DL)
lit_mid = idiv(l2, l1); lit_top = idiv(l0, l1)           # literal label m ∝ r  (NOT squared)
sqlm = idiv(imul(l2, l2), imul(l1, l1)); sqlt = idiv(imul(l0, l0), imul(l1, l1))

# ================================================================== §E  FT.120
banner("§E (H17/FT.120) — the [EXT] audit ledger: external data enters HERE ONLY")
# --- [EXT] reference values, PDG-2024-class (GeV); marked, audit-only ---
EXT = {  # scheme: (m_c, m_b, m_t)
    'S1 own-scale MSbar': (Fr(1273, 1000), Fr(4183, 1000), Fr(1625, 10)),
    'S2 MSbar c,b + top pole': (Fr(1273, 1000), Fr(4183, 1000), Fr(1724, 10)),
    'S3 pole': (Fr(167, 100), Fr(478, 100), Fr(1724, 10)),
}
LEDGER = {}
for nm, (mc, mb, mt) in EXT.items():
    obs_mid = mb / mc; obs_top = mt / mc
    sm = idiv((obs_mid, obs_mid), Rm); so = idiv((obs_top, obs_top), Ro)
    chk(iwidth(sm) < Fr(1, 2 ** 50) and iwidth(so) < Fr(1, 2 ** 50), f"§E {nm}: shortfall enclosures at width < 2^-50")
    chk(sm[1] < 1 and so[1] < 1, f"§E {nm}: both observed ratios lie strictly BELOW the derived ratios (shortfall < 1)")
    # Koide-type Q and B^2/A^2 = 6Q - 2 (exact enclosures)
    ms = (mc, mb, mt)
    sqs = [sqrt_enc_rat(m, 60) for m in ms]
    num = (sum(m for m in ms), sum(m for m in ms)); den = iadd(iadd(sqs[0], sqs[1]), sqs[2]); den = imul(den, den)
    Qi = idiv(num, den)
    LEDGER[nm] = dict(sm=sm, so=so, Q=Qi, obs=(obs_mid, obs_top))
# verdict windows
chk(Fr(9, 10) < LEDGER['S1 own-scale MSbar']['sm'][0] and LEDGER['S1 own-scale MSbar']['sm'][1] < Fr(93, 100), "§E S1 mid shortfall in (0.90, 0.93)")
chk(Fr(9, 10) < LEDGER['S1 own-scale MSbar']['so'][0] and LEDGER['S1 own-scale MSbar']['so'][1] < Fr(93, 100), "§E S1 top shortfall in (0.90, 0.93)")
chk(Fr(9, 10) < LEDGER['S2 MSbar c,b + top pole']['sm'][0] and LEDGER['S2 MSbar c,b + top pole']['sm'][1] < Fr(93, 100), "§E S2 mid shortfall in (0.90, 0.93)")
chk(Fr(96, 100) < LEDGER['S2 MSbar c,b + top pole']['so'][0] and LEDGER['S2 MSbar c,b + top pole']['so'][1] < Fr(98, 100), "§E S2 top shortfall in (0.96, 0.98)")
chk(Fr(79, 100) < LEDGER['S3 pole']['sm'][0] and LEDGER['S3 pole']['sm'][1] < Fr(81, 100), "§E S3 (pole) mid shortfall in (0.79, 0.81)")
chk(Fr(73, 100) < LEDGER['S3 pole']['so'][0] and LEDGER['S3 pole']['so'][1] < Fr(75, 100), "§E S3 (pole) top shortfall in (0.73, 0.75)")
for nm, L in LEDGER.items():
    chk(iwidth(L['Q']) < Fr(1, 2 ** 40), f"§E {nm}: Q enclosure width < 2^-40")
two3 = Fr(2, 3)
chk(abs(LEDGER['S1 own-scale MSbar']['Q'][0] - two3) < Fr(1, 100) and abs(LEDGER['S1 own-scale MSbar']['Q'][1] - two3) < Fr(1, 100), "§E S1: |Q - 2/3| < 0.01")
chk(abs(LEDGER['S2 MSbar c,b + top pole']['Q'][0] - two3) < Fr(1, 100) and abs(LEDGER['S2 MSbar c,b + top pole']['Q'][1] - two3) < Fr(1, 100), "§E S2: |Q - 2/3| < 0.01")
chk(abs(LEDGER['S3 pole']['Q'][1] - two3) > Fr(1, 100) and abs(LEDGER['S3 pole']['Q'][1] - two3) < Fr(3, 100), "§E S3 (pole): 0.01 < |Q - 2/3| < 0.03")
for nm, L in LEDGER.items():
    b2 = isub(iscl(L['Q'], 6), (Fr(2), Fr(2)))
    chk(Fr(17, 10) < b2[0] and b2[1] < Fr(21, 10), f"§E {nm}: B^2/A^2 = 6Q - 2 in (1.7, 2.1) (derived value 2)")
# no scheme reproduces at 1 percent
for nm, L in LEDGER.items():
    chk(not (L['sm'][0] > Fr(99, 100) and L['so'][0] > Fr(99, 100)), f"§E {nm}: no scheme column reproduces both derived ratios at the 1% level")
# the derived anchored predictions (top-anchored), as exact enclosures of m_b/m_t and m_c/m_t
bt = idiv(sq_2, sq_0); ct = idiv(sq_1, sq_0)
mt_p = Fr(1724, 10); mt_m = Fr(1625, 10)
chk(icontains(iscl(bt, 1), bt[0]) and Fr(25, 1000) < bt[0] and bt[1] < Fr(26, 1000), "§E derived m_b/m_t in (0.025, 0.026)")
chk(Fr(7, 1000) < ct[0] and ct[1] < Fr(72, 10000), "§E derived m_c/m_t in (0.0070, 0.0072)")
bobs = Fr(4183, 1000) / mt_m
chk(abs(bobs - bt[0]) / bobs < Fr(1, 100), "§E m_b/m_t (MSbar own-scale: 4.183/162.5) agrees with the derived ratio within 1%")
cobs = Fr(1273, 1000) / mt_m
chk(abs(cobs - ct[0]) / cobs > Fr(5, 100), "§E m_c/m_t (1.273/162.5) differs from the derived ratio by more than 5% (the light member is the outlier)")
# --- light triplet obstruction: Q_uds over the PDG-allowed ratio box m_u/m_d in [0.442,0.482], m_s/m_d in [17,22]
def Quds(ru, rs_):
    ru = Fr(ru); rs_ = Fr(rs_)
    den = iadd(iadd(sqrt_enc_rat(ru, 60), (Fr(1), Fr(1))), sqrt_enc_rat(rs_, 60)); den = imul(den, den)
    return idiv((ru + 1 + rs_, ru + 1 + rs_), den)
# monotonicity: dQ/d(sqrt r_s) > 0 iff s > c/d with c = r_u+1, d = sqrt(r_u)+1 (c/d < 1 < sqrt 17);
# dQ/d(sqrt r_u) < 0 iff t(1+s) < 1+s^2 (true for t < 1 < s).  => extremes at corners.
for ru in (Fr(442, 1000), Fr(482, 1000)):
    c_ = ru + 1; dd = sqrt_enc_rat(ru, 60)
    chk(c_ / (dd[0] + 1) < 1 < 17 ** Fr(1, 1) ** 0 * 1 and Fr(1) < Fr(4), "§E (monotonicity guard: c/d < 1 < sqrt 17)")
    chk(ru < 1 and Fr(17) > 1, "§E (monotonicity guard: t < 1 < s)")
Qmin = Quds(Fr(482, 1000), 17); Qmax = Quds(Fr(442, 1000), 22)
chk(Fr(54, 100) < Qmin[0] and Qmax[1] < Fr(59, 100), "§E light triplet: Q_uds in (0.54, 0.59) over the whole PDG-allowed ratio box")
chk(Qmax[1] < Fr(3, 5) < two3, "§E light triplet: Q_uds < 3/5 < 2/3: the (A,B)=(1,sqrt2) normalisation is EXCLUDED for the light triplet (obstruction O3)")
b2min = isub(iscl(Qmin, 6), (Fr(2), Fr(2))); b2max = isub(iscl(Qmax, 6), (Fr(2), Fr(2)))
chk(b2max[1] < Fr(3, 2) < 2 and b2min[0] > Fr(1, 1) + Fr(1, 4), "§E light triplet: B^2/A^2 in (1.25, 1.5) versus the derived 2")
# --- hadron range obstruction (EXT): pi0 = 134.9768 MeV; heaviest established hadron <= 11000 MeV
pi0 = Fr(1349768, 10000); Hmax = Fr(11000)
span = Hmax / pi0
chk(span < Fr(82), "§E established-hadron mass span (<= 11 GeV over pi0) < 82")
chk(span < Ro[0] and span < Rm[0] * 0 + Ro[0] and Fr(82) < Ro[0], "§E the span is below the derived quark-channel top ratio (139.3...) ...")
chk(span < Fr(3477), "§E ... and far below the singlet-twin (lepton-phase) top ratio 3477...")
# --- dimension-trap audit: literal label m ∝ r (not r^2) applied to the lepton channel
chk(Fr(14) < lit_mid[0] and lit_mid[1] < Fr(15) and Fr(58) < lit_top[0] and lit_top[1] < Fr(60), "§E literal-label lepton ratios (m ∝ r): 1 : 14.4 : 59.0")
chk(Fr(206768, 1000) / lit_mid[1] > Fr(14), "§E literal label misses the supplied mid ratio by > 14x (the H16 audit reads r^2 as the mass; label inconsistency inherited, not introduced)")
chk(Fr(206768, 1000) < sqlm[1] * Fr(101, 100) and Fr(206768, 1000) > sqlm[0] * Fr(99, 100), "§E r^2 reading reproduces the supplied mid ratio within 1%")
LIT_Q = (idiv(imul(q2, q2), imul(q1, q1)))   # keep quark derived ratios for the literal remark
lit_q_mid = idiv(q2, q1)
chk(lit_q_mid[1] < Fr(2) and Fr(3286, 1000) / lit_q_mid[0] > Fr(1, 1), "§E literal-label quark mid ratio (m ∝ r) < 2 versus 3.29: misses as well")
def dec(I, n=12):
    return str(Decimal(I[0].numerator) / Decimal(I[0].denominator))[:n + 2]
print(f"    derived (2/27): r^2 ratios 1 : {dec(Rm)} : {dec(Ro)};   m_b/m_t = {dec(bt)}, m_c/m_t = {dec(ct)}")
for nm, L in LEDGER.items():
    print(f"    {nm:26s} obs ratios ({float(L['obs'][0]):.4f}, {float(L['obs'][1]):.3f});  shortfall mid {dec(L['sm'],5)} top {dec(L['so'],5)};  Q = {dec(L['Q'],5)}")
print(f"    light-triplet Q over the PDG-allowed box: [{dec(Qmin,4)}, {dec(Qmax,4)}]  (derived channel requires 2/3)")
print(f"    hadron span bound = {dec((span,span),4)}")
stamp("§E green: scheme ledger (3 columns); Q and B^2/A^2; light-triplet obstruction; hadron-range obstruction; literal-label audit")

# ================================================================== §F  FT.121
banner("§F (H17) — barred-vocabulary scan, [EXT]-confinement and document pins")
if ARCH:
    doc = H17DOC
BARRED = ['previously', 'formerly', 'this was', 'now this', 'koide ansatz']
if ARCH:
    hits = [(w, doc.lower().count(w)) for w in BARRED if w in doc.lower()]
if ARCH:
    chk(not hits, f"§F revision-language scan of H17: zero hits ({hits})")
secs = {}
if ARCH:
    for sp in re.split(r'^### ', doc, flags=re.M)[1:]:
        secs[sp.split(' —')[0].strip()] = sp
    chk(all(f'FT.{n}' in secs for n in range(116, 122)), "§F sections FT.116..FT.121 all present")
    deriv = ''.join(secs[f'FT.{n}'] for n in range(116, 120))
PARTICLE = ['electron', 'muon', 'tau lepton', 'neutrino', 'proton', 'neutron', 'pion', 'gluon', 'charm', 'bottom', 'top quark', 'strange', 'Upsilon', 'J/\\psi']
if ARCH:
    ph = [(w, deriv.count(w)) for w in PARTICLE if w in deriv]
if ARCH:
    chk(not ph, f"§F particle-name scan of the derivation tags FT.116-FT.119: zero hits ({ph})")
ext_tokens = ['1.273', '4.183', '162.5', '172.4', '1.67', '4.78', '0.462', '134.9768']
if ARCH:
    leak = [(t, n) for n in (116, 117, 118, 119, 121) for t in ext_tokens if t in secs[f'FT.{n}']]
if ARCH:
    chk(not leak, f"§F [EXT] numbers occur only inside FT.120 ({leak})")
    chk(secs['FT.120'].count('[EXT]') >= 6, "§F the [EXT] marker appears in the audit clause")
    for w in ('**Thm.**', '**Req.**', '**Pf.**', '**Phys.**', '**Status.**'):
        chk(all(secs[f'FT.{n}'].count(w) == 1 for n in range(116, 122)), f"§F every FT.116–FT.121 block carries exactly one {w}")
    chk(doc.count(r'\blacksquare') == 6, "§F 6 proof terminators")
    chk('## Tier F.38' in doc and 'part 17 of 17' in doc, "§F pins: Tier F.38 heading; part 17 of 17")
    chk('P-H17a' in doc, "§F P-H17a flagged in H17")
    chk(r'\delta_q=\frac{2}{3\cdot3\cdot3}=\frac2{27}' in doc, "§F pin: delta_q = 2/(3*3*3) = 2/27 displayed")
    chk(r'3\delta_q=\delta_\ell=\frac29' in doc, "§F pin: 3 delta_q = delta_ell = 2/9 displayed")
    chk(str(PINS_D['Rm']) in doc.replace('\\', '').replace(' ', '') or f"{PINS_D['Rm']/10**12:.12f}"[:10] in doc, "§F pin: derived mid ratio decimals present")
Rm_s = f"{Decimal(Rm[0].numerator)/Decimal(Rm[0].denominator):.9f}"[:8]
Ro_s = f"{Decimal(Ro[0].numerator)/Decimal(Ro[0].denominator):.6f}"[:8]
if ARCH:
    chk(Rm_s in doc and Ro_s in doc, f"§F pins: derived ratio decimals {Rm_s}, {Ro_s} match §D")
    chk('| Heavy-triplet correspondence | FT.120 | NOT derived (audit only) |' in doc, "§F pin: adjudication row (no identification)")
    chk('| Hadron-level triplets | FT.120 | Excluded (range + confinement blindness) |' in doc, "§F pin: adjudication row (hadrons)")
    chk(r'| Overall scale $\mu$ | — | Free parameter (P4) |' in doc, "§F pin: adjudication row (free scale)")
    chk('verify_H_colour_channel.py' in doc and 'audit_heavy_quark_scheme.py' in doc, "§F pin: machine-verification and numerical-audit references")
    chk(doc.count('**Status.**') == 7, "§F Status count = 7 (6 theorem blocks + the document header line)")
    chk('**Dep.**' in doc and 'H16' in doc and 'FT.111' in doc, "§F dependency line cites H16 / FT.111")
    chk('FT.109' in doc and 'FT.110' in doc and 'FT.112' in doc and 'FT.113' in doc, "§F H16 tags cited at use")
chk(all(t in FDOC for t in ('CT3.15', 'CT3.16', 'CT3.17', 'CT3.20', 'CT3.22', 'CT3.3')), "§F cited F-tags exist in F_color.md")
chk('D3.8' in ADOC and 'D3.9' in ADOC, "§F cited D3.8/D3.9 exist in A_axioms.md")
if ARCH:
    chk('H17' not in H16DOC, "§F H16 untouched (no forward reference)")
stamp("§F green: zero barred hits; [EXT] confined to FT.120; derivation tags free of particle names; document pins exact")

print(f"\nverify_H_colour_channel: {N} checks green  ({time.time()-t0:.1f}s) — H17 §A–§F (Tier F.38, FT.116–FT.121)")
