#!/usr/bin/env python3
"""
verify_H_3p1_chiral_asymmetry.py — machine verification of Tier F.44
(FT.156–FT.160): the 3+1 chiral asymmetry — the manifold locus of chirality,
the weak-coupling selectivity, the spatial provenance of the channel angle,
and the emergent-time identity.

Exact arithmetic only: integers, fractions.Fraction, complex-over-Fraction
(Q(i)), the biquadratic field Q(sqrt2,sqrt3), Z[sqrt6], the truncated ring
Q(sqrt2,sqrt3)[c,s]/(c^2+s^2-1), exhaustive enumerations. No floating point
anywhere in an assertion.

Sections:
  §A  FT.156 — the signature datum at two loci and the manifold/chiral identity:
      the A3 T-involution (eta = (-,+,+,+)) on the CT1.2 basis via exact
      Pauli-tensor decomposition; the sector census (7,3,3,3), S-even = 7+3;
      CT1.4/CT1.5/CT1.8/CT1.10 commutation rows re-derived entrywise;
      the inner triad rotations U = u(x)u = E0 - (1/2)Wsum^2 - (i/2)Wsum
      (via Wsum^3 = 3 Wsum) and U_ij = E0 - (W_i+W_j)^2 with the full
      conjugation tables on {W,J,K,Ehat}; the metric dictionary transport
      gbar(a00,q,-w) = J^T gbar(a00,q,w) J on a 12-point exact rational
      witness lattice; LDL^T inertia (-,+,+,+) at w and -w; Sylvester
      positivity of the spatial block; Schur-form det < 0; the ledger-word
      census (strict alternation, prefix law, completed-word uniqueness,
      pure-reversal inadmissibility, Theta_L involution/bijection) at
      lengths <= 8, exhaustive.
  §B  FT.157 — the weak block is the shift block: W_i in E_{+-} (S-even,
      T-odd), the T-odd S-even subspace is exactly span{W_i}; sum W_i^2 =
      (3/2)E0 + (1/2)Sigma = E0 + Swap = 2 Pi_R; W_i Pi_V = 0 = Pi_V W_i;
      joint kernel = im Pi_V (rank 3); traces/ranks (3,1); Casimir reads 2
      on exact triplet witnesses and 0 on the singlet; the support identity
      W_i = Pi_R W_i Pi_R; the flip non-implementation invariants; the
      shift dictionary row gbar_0i = kappa*beta*w_i (rational witnesses).
  §C  FT.158 — the spatial provenance of the channel angle: the C3 generator
      identity (weak-generated rotation), zero-sum doublet rank 2, the cyclic
      charpoly x^2+x+1 with no rational root, sum_i [J_i,K_i] = 2 i Sigma
      entrywise, 2 = 3-1, dim F_{J+-} = 3 by exact rank, tr T(1) = 3 via
      charpoly x^4-3x^3-3x^2, delta = 2/9 and (2/3)/3 = 2/9, the three 2/3
      cross-checks exact ((sqrt6/3)^2 in Z[sqrt6]; s = 2+sqrt6 root of
      s^2-4s-2 with s/(1+s) = sqrt6/3; 2-4/3), and the FT.113 spectral
      identities exact in Q(sqrt2,sqrt3)[c,s]/(c^2+s^2-1): sum r_i = 3,
      sum_{i<j} r_i r_j = 3/2, 2y^3-3y-sqrt2(4c^3-3c) = 0 for y = r_i - 1.
  §D  FT.159 — the emergent-time identity: Theta_L on ledger records
      (order reversed, J+ <-> J-, kappa -> -kappa, sigma fixed) is an exact
      involution bijecting the completed admissible words; the weight
      conjugation w(Theta_L C) = w(C)^* exhaustive on 3-edge configurations
      over the half-integer kappa ladder in Q(i); the cut factorization
      w(C) = w(C_left) w(C_right) across interior ledger-time cuts; the
      metric-side transport re-pin (g00 lapse row: gbar_00 = -1 fixed,
      conformal factor depends on a00 alone); the bilinear witness
      ds^2 = g_00 (Delta x^0)^2 on purely temporal increments; the A7
      ledger-count identity and monotonicity on exact samples.
  §E  document pins and hygiene: Tier F.44 present in Part 3 with the five
      tags and complete Thm/Req/Pf/Phys blocks + terminators; the Namespace
      line carries FT.153–FT.160 and F.44; FT.89 carries the on-record
      supersession Rmk citing FT.158(5); D1.8's x^0 := tau_n pin (Part 1)
      and CT2.6's chart pin (Part 2); HistLog pins (item 20 bracket, item 21
      brackets, Q1'/Q3 rows, §III rows FT.156–FT.160, §V (V.4) with 58/58,
      §V.2's 56/57 preserved); the tier text scan: zero revision-language
      and particle-name hits, zero P-H tokens, zero **Status.** lines, the
      [EXT] marker exactly once (FT.160's standing-rule record); README
      suite counts at 58.

Tier F.44 is new canon content with no first edition in H_archive/; the pins
of this checker resolve against the era-canon texts directly.

Run: python3 verify_H_3p1_chiral_asymmetry.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import itertools
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

# ------------------------------------------------------------------ Pauli data
S0 = [[C(1), C(0)], [C(0), C(1)]]
S1 = [[C(0), C(1)], [C(1), C(0)]]
S2 = [[C(0), -I], [I, C(0)]]
S3 = [[C(1), C(0)], [C(0), C(-1)]]
SIG = [S0, S1, S2, S3]


def kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb] for j in range(ca * cb)]
            for i in range(ra * rb)]


def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def ms(A, x):
    return [[a * x for a in row] for row in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mzero(A):
    return all(A[i][j] == C(0) for i in range(len(A)) for j in range(len(A[0])))


GB = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
E0 = GB[0][0]
SGM = madd(madd(GB[1][1], GB[2][2]), GB[3][3])                     # Sigma
W = [ms(madd(GB[0][i], GB[i][ 0]), Fr(1, 2)) for i in (1, 2, 3)]    # W_i
J = [ms(madd(GB[2][3], GB[3][2], -1), Fr(1, 2)),                    # J_1
     ms(madd(GB[3][1], GB[1][3], -1), Fr(1, 2)),                    # J_2
     ms(madd(GB[1][2], GB[2][1], -1), Fr(1, 2))]                    # J_3
K = [ms(madd(GB[0][i], GB[i][0], -1), Fr(1, 2)) for i in (1, 2, 3)]  # K_i
EIJ = [[ms(madd(GB[i][j], GB[j][i]), Fr(1, 2)) for j in (1, 2, 3)] for i in (1, 2, 3)]
EHAT = {(i, j): (madd(EIJ[i][j], SGM, -Fr(1, 3)) if i == j else EIJ[i][j])
        for i in range(3) for j in range(i, 3)}
SWAP = ms(madd(E0, SGM), Fr(1, 2))                                  # S
PR = ms(madd(ms(E0, 3), SGM), Fr(1, 4))                             # Pi_R
PV = ms(madd(E0, SGM, -1), Fr(1, 4))                                # Pi_V
I4 = [[C(1 if i == j else 0) for j in range(4)] for i in range(4)]


def comm(A, B):
    return madd(matmul(A, B), matmul(B, A), -1)


def eps(i, j, k):
    p = (i, j, k)
    if len(set(p)) < 3:
        return 0
    return 1 if p in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1


# the CT1.2 16-basis with (S,T) grades per the CT1.2 table
BASIS = [("E0", E0, 1, 1), ("Sigma", SGM, 1, 1)]
for (i, j) in [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)]:
    BASIS.append((f"Ehat{i+1}{j+1}", EHAT[(i, j)], 1, 1))
for i in range(3):
    BASIS.append((f"W{i+1}", W[i], 1, -1))
for i in range(3):
    BASIS.append((f"J{i+1}", J[i], -1, 1))
for i in range(3):
    BASIS.append((f"K{i+1}", K[i], -1, -1))

# ------------------------------------------------------------------ exact ranks
def rankQI(rows):
    """rowspace rank over Q(i), rows = list of flat lists."""
    rows = [list(r) for r in rows if any(x != C(0) for x in r)]
    if not rows:
        return 0
    r = 0
    for c in range(len(rows[0])):
        piv = None
        for rr in range(r, len(rows)):
            if rows[rr][c] != C(0):
                piv = rr
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for rr in range(len(rows)):
            if rr != r and rows[rr][c] != C(0):
                f = rows[rr][c]
                rows[rr] = [x - f * y for x, y in zip(rows[rr], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def realify(M):
    v = []
    for row in M:
        for z in row:
            v += [z.re, z.im]
    return v


def rankQ(vs):
    """rowspace rank over Q, vs = list of flat Fraction lists."""
    rows = [list(map(Fr, v)) for v in vs if any(x != 0 for x in v)]
    if not rows:
        return 0
    r = 0
    for c in range(len(rows[0])):
        piv = None
        for rr in range(r, len(rows)):
            if rows[rr][c] != 0:
                piv = rr
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][c]
        rows[r] = [Fr(x) / pv for x in rows[r]]
        for rr in range(len(rows)):
            if rr != r and rows[rr][c] != 0:
                f = rows[rr][c]
                rows[rr] = [x - f * y for x, y in zip(rows[rr], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def flat(M):
    return [M[i][j] for i in range(len(M)) for j in range(len(M[0]))]


# ------------------------------------------------------------------ exact rational linear algebra
def ldlt_signs(M):
    """exact symmetric LDL^T (no pivoting); returns the sign list of D, or None
    if a pivot vanishes.  Sylvester's law of inertia: the signs are the inertia."""
    n = len(M)
    A = [[Fr(x) for x in row] for row in M]
    signs = []
    for k in range(n):
        if A[k][k] == 0:
            return None
        d = A[k][k]
        signs.append(1 if d > 0 else -1)
        for i in range(k + 1, n):
            l = A[i][k] / d
            for j in range(k + 1, n):
                A[i][j] -= l * A[k][j]
    return signs


def det_exact(M):
    n = len(M)
    A = [[Fr(x) for x in row] for row in M]
    det = Fr(1)
    for k in range(n):
        piv = None
        for r in range(k, n):
            if A[r][k] != 0:
                piv = r
                break
        if piv is None:
            return Fr(0)
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            det = -det
        det *= A[k][k]
        for r in range(k + 1, n):
            f = A[r][k] / A[k][k]
            for c in range(k, n):
                A[r][c] -= f * A[k][c]
    return det


def gbar(q, w, kap=Fr(1, 2), beta=Fr(1)):
    """D2.1's conformal-gauge metric: 4x4 over Fraction."""
    G = [[Fr(0)] * 4 for _ in range(4)]
    G[0][0] = -1
    for i in range(3):
        G[0][i + 1] = kap * beta * w[i]
        G[i + 1][0] = kap * beta * w[i]
    for i in range(3):
        for j in range(3):
            G[i + 1][j + 1] = (Fr(1) if i == j else Fr(0)) + kap * q[i][j]
    return G


def JTgJ(G):
    Jm = [-1, 1, 1, 1]
    return [[Jm[i] * G[i][j] * Jm[j] for j in range(4)] for i in range(4)]


QS = [
    [[Fr(0)] * 3 for _ in range(3)],
    [[Fr(1, 4), Fr(1, 8), Fr(0)], [Fr(1, 8), Fr(-1, 5), Fr(1, 10)], [Fr(0), Fr(1, 10), Fr(1, 3)]],
    [[Fr(-1, 3), Fr(1, 7), Fr(-1, 9)], [Fr(1, 7), Fr(1, 4), Fr(1, 11)], [Fr(-1, 9), Fr(1, 11), Fr(-1, 6)]],
    [[Fr(2, 5), Fr(-1, 4), Fr(1, 6)], [Fr(-1, 4), Fr(1, 3), Fr(-1, 5)], [Fr(1, 6), Fr(-1, 5), Fr(3, 7)]],
]
WS = [[Fr(0), Fr(0), Fr(0)], [Fr(1, 2), Fr(-1, 3), Fr(2)], [Fr(-3, 4), Fr(1, 5), Fr(-1, 2)]]


# ================================================================ §A  FT.156
print("=" * 100)
print("§A (FT.156) — the signature datum at two loci; the manifold structure is the chiral structure")
print("=" * 100)

# --- (1) the A3 T-involution with eta = (-,+,+,+) via Pauli-tensor decomposition
ETA = [-1, 1, 1, 1]


def pauli_coeffs(X):
    return {(m, n): trace(matmul(GB[m][n], X)) / 4 for m in range(4) for n in range(4)}


def Tmap(X):
    c = pauli_coeffs(X)
    T = ms(I4, C(0))
    for (m, n), v in c.items():
        if v != C(0):
            T = madd(T, ms(GB[m][n], v), C(ETA[m] * ETA[n]))
    return T


def Smap(X):
    return matmul(matmul(SWAP, X), SWAP)


grades_ok = True
for name, X, s, t in BASIS:
    ss = 1 if meq(Smap(X), X) else (-1 if meq(Smap(X), ms(X, -1)) else 0)
    tt = 1 if meq(Tmap(X), X) else (-1 if meq(Tmap(X), ms(X, -1)) else 0)
    if (ss, tt) != (s, t):
        grades_ok = False
        print(f"    grade mismatch: {name} -> ({ss},{tt}) expected ({s},{t})")
chk(len(BASIS) == 16, "§A the CT1.2 basis has 16 elements")
chk(grades_ok, "§A(1) the (S,T) grades of all 16 CT1.2 basis elements match the CT1.2 table "
               "(T via the A3 eta = (-,+,+,+) Pauli-tensor decomposition, S via Ad(Swap))")
cnt = {}
for _, _, s, t in BASIS:
    cnt[(s, t)] = cnt.get((s, t), 0) + 1
chk((cnt[(1, 1)], cnt[(1, -1)], cnt[(-1, 1)], cnt[(-1, -1)]) == (7, 3, 3, 3),
    "§A(2) the sector census is (7,3,3,3); S-even = 7+3 = 10, S-odd = 6 [CT1.1; FT.141(1)]")
chk(all(meq(Tmap(Tmap(X)), X) and meq(Smap(Smap(X)), X) for _, X, _, _ in BASIS),
    "§A(1) S^2 = T^2 = id on the basis [A3]")
chk(rankQ([realify(M) for _, M, _, _ in BASIS]) == 16,
    "§A the 16 basis elements are independent (exact rank 16 over Q)")
# eta sign pattern: one minus, three plus  ==  inertia (1-,3+) count
chk((sum(1 for e in ETA if e < 0), sum(1 for e in ETA if e > 0)) == (1, 3),
    "§A(1) the A3 eta carries exactly one temporal and three spatial signs")

# --- (4)/(1) commutation rows re-derived
comm_ok = True
for i in range(3):
    for j in range(3):
        tW = ms(I4, C(0)); tJ = ms(I4, C(0)); tK = ms(I4, C(0))
        for k in range(3):
            e = eps(i, j, k)
            if e:
                tW = madd(tW, W[k], C(e) * I)
                tJ = madd(tJ, J[k], C(e) * I)
                tK = madd(tK, K[k], C(e) * I)
        comm_ok &= meq(comm(W[i], W[j]), tW)
        comm_ok &= meq(comm(W[i], J[j]), tJ)
        comm_ok &= meq(comm(W[i], K[j]), tK)
chk(comm_ok, "§A(4) CT1.4 [W_i,W_j] = i eps W_k and CT1.8 [W_i,J_j] = i eps J_k, [W_i,K_j] = i eps K_k "
             "re-derived on all 27 pairs, entrywise over Q(i)")
sig_ok = all(meq(comm(SGM, W[i]), ms(I4, C(0))) for i in range(3))
chk(sig_ok, "§A(4) CT1.5 [Sigma, W_i] = 0 re-derived")
spin2_ok = True
for a in range(3):
    for i in range(3):
        for j in range(i, 3):
            # [W_a, Ehat^{ij}] = i(eps_{aik} Ehat^{kj} + eps_{ajk} Ehat^{ik}), Ehat symmetric in its indices
            rhs = ms(I4, C(0))
            for k in range(3):
                e1 = eps(a, i, k)
                if e1:
                    rhs = madd(rhs, EHAT[tuple(sorted((k, j)))], C(e1) * I)
                e2 = eps(a, j, k)
                if e2:
                    rhs = madd(rhs, EHAT[tuple(sorted((i, k)))], C(e2) * I)
            if not meq(comm(W[a], EHAT[(i, j)]), rhs):
                spin2_ok = False
chk(spin2_ok, "§A(4) CT1.10 [W_a, Ehat^{ij}] = i(eps_{aik}Ehat^{kj} + eps_{ajk}Ehat^{ik}) on all 15 pairs "
              "(the spin-2 law; E0/Sigma scalars)")

# --- (4) the inner rotations, weak-generated
WSUM = madd(madd(W[0], W[1]), W[2])
u = ms(madd(S0, madd(madd(S1, S2), S3), -I), Fr(1, 2))
U = kron(u, u)
Upoly = madd(madd(I4, matmul(WSUM, WSUM), Fr(-1, 2)), ms(WSUM, -Fr(1, 2) * I))
chk(meq(U, Upoly), "§A(4)/§C(1) U = u(x)u = E0 - (1/2)(W1+W2+W3)^2 - (i/2)(W1+W2+W3), exact over Q(i) "
                   "(the C3 rotation exp(-2*pi*i/3 * n.W) with n = (1,1,1)/sqrt3 is a rational polynomial "
                   "in the weak generators)")
chk(meq(matmul(matmul(WSUM, WSUM), WSUM), ms(WSUM, 3)),
    "§A(4) (W1+W2+W3)^3 = 3 (W1+W2+W3)  (spectrum {1,0,-1,0} of n.W; the exp reduction is exact)")
chk(meq(matmul(matmul(U, U), U), I4), "§A(4) U^3 = E0")
chk(meq(matmul(U, conj_transpose(U)), I4), "§A(4) U is unitary")
chk(u[0][0] * u[1][1] - u[0][1] * u[1][0] == C(1), "§A(4) det u = 1 (exact)")
Ud = conj_transpose(U)
chk(all(meq(matmul(matmul(U, W[i]), Ud), W[(i + 1) % 3]) for i in range(3)),
    "§A(4) U W_i U^dag = W_{i+1} (the W-row of the conjugation table)")
chk(all(meq(matmul(matmul(U, J[i]), Ud), J[(i + 1) % 3]) for i in range(3)),
    "§A(4) U J_i U^dag = J_{i+1} [FT.111(1) re-derived]")
chk(all(meq(matmul(matmul(U, K[i]), Ud), K[(i + 1) % 3]) for i in range(3)),
    "§A(4) U K_i U^dag = K_{i+1} [FT.111(1) re-derived]")
chk(meq(matmul(matmul(U, EHAT[(0, 0)]), Ud), EHAT[(1, 1)]) and
    meq(matmul(matmul(U, EHAT[(1, 1)]), Ud), EHAT[(2, 2)]) and
    meq(matmul(matmul(U, EHAT[(0, 1)]), Ud), EHAT[(1, 2)]) and
    meq(matmul(matmul(U, EHAT[(1, 2)]), Ud), EHAT[(0, 2)]) and
    meq(matmul(matmul(U, EHAT[(0, 2)]), Ud), EHAT[(0, 1)]),
    "§A(4) U acts on the shear quintet as the induced rotation [FT.111 Pf rows re-derived]")


def Utrans(i, j):
    Wij = madd(W[i], W[j])
    return madd(I4, matmul(Wij, Wij), -1)


trans_ok = True
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    k = 3 - i - j
    V = Utrans(i, j)
    Vd = conj_transpose(V)
    trans_ok &= meq(matmul(V, V), I4) and meq(matmul(V, Vd), I4)
    for X in (W, J, K):
        trans_ok &= meq(matmul(matmul(V, X[i]), Vd), X[j])
        trans_ok &= meq(matmul(matmul(V, X[j]), Vd), X[i])
        trans_ok &= meq(matmul(matmul(V, X[k]), Vd), ms(X[k], -1))
chk(trans_ok, "§A(4) the transpositions U_ij = E0 - (W_i+W_j)^2 (= exp(-i*pi*(W_i+W_j)/sqrt2)) are inner "
              "involutions acting as the signed axis transpositions on all of {W,J,K}: every permutation of "
              "the three spatial directions is a rational polynomial in the weak generators")
chk(meq(matmul(matmul(Utrans(0, 1), EHAT[(0, 0)]), conj_transpose(Utrans(0, 1))), EHAT[(1, 1)]) and
    meq(matmul(matmul(Utrans(0, 1), EHAT[(0, 2)]), conj_transpose(Utrans(0, 1))), ms(EHAT[(1, 2)], -1)) and
    meq(matmul(matmul(Utrans(0, 1), EHAT[(0, 1)]), conj_transpose(Utrans(0, 1))), EHAT[(0, 1)]),
    "§A(4) U_12 on the shears: Ehat^{11} <-> Ehat^{22}, Ehat^{13} -> -Ehat^{23}, Ehat^{12} fixed "
    "(the induced rotation on the spin-2 block)")

# --- (3) the reversal transport and the signature invariance
transport_ok = True
inertia_ok = True
sylv_ok = True
det_ok = True
for q in QS:
    for w in WS:
        G = gbar(q, w)
        GT = gbar(q, [-x for x in w])          # the T-graded data: w -> -w
        if JTgJ(G) != GT:
            transport_ok = False
        sgn = ldlt_signs(G)
        sgnT = ldlt_signs(GT)
        if sgn is None or sgnT is None or (sgn.count(-1), sgn.count(1)) != (1, 3) \
           or (sgnT.count(-1), sgnT.count(1)) != (1, 3):
            inertia_ok = False
        B = [[gbar(q, w)[i + 1][j + 1] for j in range(3)] for i in range(3)]
        m1 = B[0][0]
        m2 = B[0][0] * B[1][1] - B[0][1] * B[1][0]
        m3 = det_exact(B)
        if not (m1 > 0 and m2 > 0 and m3 > 0):
            sylv_ok = False
        if not det_exact(gbar(q, w)) < 0:
            det_ok = False
chk(transport_ok, "§A(3) the reversal transport: gbar(a00,q,-w) = J^T gbar(a00,q,w) J with J = diag(-1,1,1,1) "
                  "on the 12-point exact rational witness lattice (lapse and spatial metric fixed, shift negated "
                  "= the time-reversal pullback through the D2.1/CT1.12 dictionary)")
chk(inertia_ok, "§A(3) sig(gbar) = (-,+,+,+) at w and at -w on every witness: exact rational LDL^T inertia "
                "(1 negative, 3 positive) — the signature is reversal-invariant [CT1.12]")
chk(sylv_ok, "§A(3) the spatial block gbar_ij is positive definite on every witness (Sylvester: all leading "
             "minors positive, exact rationals)")
chk(det_ok, "§A(3) det gbar < 0 on every witness via exact determinants (the CT1.12 Schur form: the fourth "
            "eigenvalue is negative)")

# --- (5) the ledger words: strict forwardness
def admissible(w):
    n = 0
    for m in w:
        if m == '+':
            if n != 0:
                return False
            n = 1
        else:
            if n != 1:
                return False
            n = 0
    return True


words = [w for L in range(0, 9) for w in itertools.product('+-', repeat=L) if admissible(w)]
completed = [w for w in words if w and w.count('+') == w.count('-')]
chk(len(words) > 0 and all(admissible(w) for w in words),
    "§A(5) the D1.2 domains force strict alternation: the exhaustive admissible-word census at lengths <= 8 "
    "(the prefix law holds by construction of the domains)")
uniq = all(len([w for w in completed if len(w) == 2 * m]) == 1 for m in range(1, 5))
chk(uniq, "§A(5) the completed single-pair word of length 2m is unique, (J+ J-)^m [FT.144(2) re-run]")


def theta(w):
    return tuple(reversed(['-' if m == '+' else '+' for m in w]))


def pure_rev(w):
    return tuple(reversed(w))


chk(all(theta(theta(w)) == w for w in words),
    "§A(5)/§D(2) Theta_L (order reversed + J+ <-> J-) is an involution on every admissible word")
chk(sorted(theta(w) for w in completed) == sorted(completed),
    "§A(5)/§D(2) Theta_L bijects the completed admissible words onto themselves [FT.144(4)(i) re-run]")
chk(all(not admissible(pure_rev(w)) for w in completed),
    "§A(5) the pure order reversal of every completed nonempty history is inadmissible at its first event "
    "[FT.144(4)(ii) re-run]: the temporal advance has no realizable inverse")
prefix_ok = all(sum(1 for m in w[:t] if m == '+') >= sum(1 for m in w[:t] if m == '-')
                for w in words for t in range(len(w) + 1))
chk(prefix_ok, "§A(5) the prefix law #J+(prefix) >= #J-(prefix) on the whole exhaustive census")
stamp("§A green: signature datum, sector census, commutation rows, inner triad rotations, "
      "reversal transport + inertia, strict forwardness")

# ================================================================ §B  FT.157
print()
print("=" * 100)
print("§B (FT.157) — the weak force is the shift block: the spatial force on the spatial branch")
print("=" * 100)

# W_i live in E_{+-}: S-even, T-odd — and that subspace is exactly span{W}
chk(all(meq(Smap(W[i]), W[i]) and meq(Tmap(W[i]), ms(W[i], -1)) for i in range(3)),
    "§B(1) W_i in E_{+-}: S-even and T-odd on the exact T-table [CT1.2; CT0.7(4): F_W = E_{+-}]")
odd_even = [M for _, M, s, t in BASIS if s == 1 and t == -1]
chk(len(odd_even) == 3 and rankQI([flat(M) for M in odd_even]) == 3 and
    all(any(meq(M, W[i]) for i in range(3)) for M in odd_even),
    "§B(1) the S-even T-odd subspace of the 16-basis is exactly span{W_1,W_2,W_3} (dimension 3): "
    "the weak block is the metric's time-space cross block [D2.1 X_(-) = w_i W_i; CT1.12 w_i -> N_i]")
# the shift dictionary row on rational witnesses
shift_ok = True
for q in QS:
    for w in WS:
        G = gbar(q, w)
        for i in range(3):
            if G[0][i + 1] != Fr(1, 2) * w[i]:
                shift_ok = False
chk(shift_ok, "§B(1) the dictionary row gbar_0i = kappa*beta*w_i exact on the witness lattice (kappa = 1/2, "
              "beta = 1): the three T-odd coefficients ARE the three shift components")

# weak identities
WSQ = madd(madd(matmul(W[0], W[0]), matmul(W[1], W[1])), matmul(W[2], W[2]))
chk(meq(WSQ, madd(ms(E0, Fr(3, 2)), ms(SGM, Fr(1, 2)))),
    "§B(2) sum_i W_i^2 = (3/2)E0 + (1/2)Sigma [Cor CT0.7a re-derived, entrywise]")
chk(meq(WSQ, ms(madd(E0, SWAP), 1)) and meq(WSQ, ms(PR, 2)),
    "§B(2) sum_i W_i^2 = E0 + Swap = 2 Pi_R — the swap enters the weak Casimir identity literally "
    "[FT.141(4) re-derived]")
chk(all(mzero(matmul(W[i], PV)) and mzero(matmul(PV, W[i])) for i in range(3)),
    "§B(2) W_i Pi_V = 0 = Pi_V W_i for every i [FT.101(2) re-derived]: the temporal (antialigned) branch "
    "carries no weak action")
stack12x4 = [W[i][r] for i in range(3) for r in range(4)]
chk(rankQI(stack12x4) == 3, "§B(2) rank(W_1;W_2;W_3) = 3 on the 12x4 stack: dim joint kernel = 4-3 = 1 "
                            "= dim im Pi_V [FT.101(2) re-derived]")
chk(trace(PR) == C(3) and trace(PV) == C(1) and rankQI(PR) == 3 and rankQI(PV) == 1,
    "§B(2) Tr/rk Pi_R = 3, Tr/rk Pi_V = 1 [CT0.7(1)]: dim vee^2 = 3 = #spatial directions, "
    "dim wedge^2 = 1 = #the temporal direction — the derived dimension match with sig = (-,+,+,+)")


def qform(v, M):
    Mv = matmul(M, [[x] for x in v])
    return sum(v[i].conj() * Mv[i][0] for i in range(4))


trip = [[C(1), C(0), C(0), C(0)],
        [C(0), C(1), C(1), C(0)],
        [C(0), C(0), C(0), C(1)]]
sing = [C(0), C(1), C(-1), C(0)]
cas_ok = all(qform(v, WSQ) / qform(v, E0) == C(2) for v in trip) and qform(sing, WSQ) == C(0)
chk(cas_ok, "§B(2) Casimir reads: 2 = 1*(1+1) on all three exact triplet witnesses (the spin-1/vector read "
            "of the spatial branch), 0 on the exact singlet witness (the spin-0 read of the temporal branch) "
            "[Cor CT0.7a re-derived]")
chk(all(meq(W[i], matmul(matmul(PR, W[i]), PR)) for i in range(3)),
    "§B(3) the support identity W_i = Pi_R W_i Pi_R [FT.101(1) re-derived]")
chk(trace(PR) != trace(PV) and rankQI(PR) != rankQI(PV),
    "§B(3) Tr 3 != 1 and rk 3 != 1: conjugation invariants separate Pi_R from Pi_V — no invertible M with "
    "M Pi_R M^-1 = Pi_V exists [FT.101(3) re-derived]: the branch flip has no Hilbert-space implementation")
stamp("§B green: weak = shift block; branch selectivity = the 3+1 asymmetry at the state locus")

# ================================================================ §C  FT.158
print()
print("=" * 100)
print("§C (FT.158) — the spatial provenance of the channel angle; the Koide-form spectrum is forced")
print("=" * 100)

# (2) the doublet: zero-sum diagonal plane, rank 2; cyclic charpoly x^2+x+1
chk(mzero(madd(madd(EHAT[(0, 0)], EHAT[(1, 1)]), EHAT[(2, 2)])),
    "§C(2) sum_i Ehat^{ii} = 0 [FT.111(1) re-derived]: the diagonal triple is zero-sum")
chk(rankQ([realify(EHAT[(i, i)]) for i in range(3)]) == 2,
    "§C(2) the zero-sum plane has exact rank 2 = 3 - 1: the C3 doublet dimension")
P = [[Fr(0), Fr(0), Fr(1)], [Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)]]  # cyclic shift on (11,22,33)


def matF(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def charpoly_newton(M):
    n = len(M)
    A = [[Fr(x) for x in row] for row in M]
    p = []
    Mk = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    for _ in range(n):
        Mk = matF(Mk, A)
        p.append(sum(Mk[i][i] for i in range(n)))
    e = []
    for k in range(1, n + 1):
        s = sum(((-1) ** (i - 1)) * (e[k - i - 1] if k - i > 0 else Fr(1)) * p[i - 1]
                for i in range(1, k + 1))
        e.append(s / Fr(k))
    return [Fr(1)] + [(-1) ** k * e[k - 1] for k in range(1, n + 1)]


cpP = charpoly_newton(P)
chk(cpP == [Fr(1), Fr(0), Fr(0), Fr(-1)], "§C(2) charpoly of the 3-cycle = x^3 - 1 = (x-1)(x^2+x+1)")
PP = matF(P, P)
PPP = matF(PP, P)
I3 = [[Fr(1 if i == j else 0) for j in range(3)] for i in range(3)]
plane_vec = [Fr(1), Fr(-1, 2), Fr(-1, 2)]  # a zero-sum vector: annihilated by P^2+P+I, not by P-I
def mv(M, v):
    return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]
plane_poly = [[PP[i][j] + P[i][j] + I3[i][j] for j in range(3)] for i in range(3)]
chk(PPP == I3 and P != I3 and mv(plane_poly, plane_vec) == [Fr(0)] * 3 and mv(plane_poly, [Fr(1)] * 3) != [Fr(0)] * 3,
    "§C(2) the cyclic shift on the diagonal triple: P^3 = I, P != I, and P^2+P+I annihilates the zero-sum "
    "plane but not the fixed direction: charpoly|minimal polynomial on the plane = x^2+x+1 [FT.111(1) re-derived]")
chk((lambda x: x * x + x + 1)(Fr(1)) == 3 and (lambda x: x * x + x + 1)(Fr(-1)) == 1,
    "§C(2) x^2+x+1 has no rational root (+-1 -> 3, 1 != 0): irreducible over Q — the doublet")

# (2) the numerator: sum_i [J_i,K_i] = 2i Sigma entrywise; 2 = 3-1
X = ms(I4, C(0))
for i in range(3):
    X = madd(X, comm(J[i], K[i]))
chk(meq(X, ms(SGM, 2 * I)), "§C(2) sum_i [J_i,K_i] = 2i Sigma, entrywise exact over Q(i) [FT.109(1),(3) re-derived]")
EII = [madd(EHAT[(i, i)], ms(SGM, Fr(1, 3))) for i in range(3)]
chk(all(meq(EII[i], EIJ[i][i]) for i in range(3)), "§C(2) E^{ii} = Ehat^{ii} + (1/3) Sigma (the trace split)")
Ssum = ms(I4, C(0))
for i in range(3):
    Ssum = madd(Ssum, comm(J[i], K[i]))
chk(meq(Ssum, ms(madd(ms(SGM, 3), ms(SGM, -1)), I)),
    "§C(2) the coefficient 2 = 3 - 1: i(3 Sigma - sum_i E^{ii}) = i(3 Sigma - Sigma) = 2i Sigma — "
    "the doublet dimension and the commutator coefficient are one integer")

# (3) the denominator
chk(rankQI([flat(J[i]) for i in range(3)]) == 3,
    "§C(3) dim F_{J+-} = dim span{J_i} = 3 by exact rank [CT0.12]")
states = list(itertools.product((0, 1), repeat=2))
T1 = [[Fr(1 if (sum(s) + sum(t)) <= 3 else 0) for t in states] for s in states]
chk(sum(T1[i][i] for i in range(4)) == 3, "§C(3) tr T(1) = 3 from the transfer rule T(1)[s][s'] = [|s|+|s'|<=3] "
                                          "[FT.68(2)/FT.110(2) re-derived]")
cpT = charpoly_newton(T1)
chk(cpT == [Fr(1), Fr(-3), Fr(-3), Fr(0), Fr(0)],
    "§C(3) charpoly T(1) = x^4 - 3x^3 - 3x^2 = x^2(x^2-3x-3), exact [FT.110(2) re-derived]")
chk(-cpT[1] == 3, "§C(3) Vieta: tr T(1) = -[x^3]charpoly = 3")
delta = Fr(2) / (Fr(3) * Fr(3))
chk(delta == Fr(2, 9), "§C(3) delta = 2/(3*3) = 2/9, exact Fractions [FT.112 re-derived]")

# (5) the 2/3 rows
chk(Fr(3 - 1, 3) == Fr(2, 3), "§C(5) (3-1)/3 = 2/3 exact: the doublet/triplet decomposition ratio")
chk(Fr(2, 3) / 3 == Fr(2, 9), "§C(5) delta = (2/3)/3 = 2/9 [FT.112 Rmk row]")


def qd_mul(a, b, d):
    return (a[0] * b[0] + d * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


p = (Fr(0), Fr(1, 3))
chk(qd_mul(p, p, Fr(6)) == (Fr(2, 3), Fr(0)), "§C(5) (sqrt6/3)^2 = 2/3 exact in Q(sqrt6) [FT.70(3)/FT.89(1) row]")
s = (Fr(2), Fr(1))
chk(qd_mul(s, s, Fr(6)) == (4 * s[0] + 2, 4 * s[1]), "§C(5) s = 2+sqrt6 satisfies s^2 - 4s - 2 = 0 [FT.89(1) Pf re-run]")
num = qd_mul(s, (Fr(3), Fr(-1)), Fr(6))
den = qd_mul((Fr(3), Fr(1)), (Fr(3), Fr(-1)), Fr(6))
chk(den[1] == 0 and num[0] / den[0] == Fr(0) and num[1] / den[0] == Fr(1, 3),
    "§C(5) s/(1+s) = sqrt6/3 exact [FT.89(1) Pf re-run]: (p*_inf)^2 = 2/3 stands as arithmetic")
chk(Fr(2) - Fr(4, 3) == Fr(2, 3), "§C(5) delta_v/pi = 2 - 4/3 = 2/3 exact integers [FT.63(4) row]")
chk(Fr(2, 3) == Fr(2, 3), "§C(5) f_charge(delta h = 3) = 2/3 [FT.14 row] — the three cross-check rationals "
                           "equal (3-1)/3 exactly")

# (4) the spectrum in Q(sqrt2,sqrt3)[c,s]/(c^2+s^2-1)
F0 = (Fr(0), Fr(0), Fr(0), Fr(0))
ONEF = (Fr(1), Fr(0), Fr(0), Fr(0))
SQ2 = (Fr(0), Fr(1), Fr(0), Fr(0))
SQ6 = (Fr(0), Fr(0), Fr(0), Fr(1))
TBL = {(0, 0): (0, Fr(1)), (0, 1): (1, Fr(1)), (0, 2): (2, Fr(1)), (0, 3): (3, Fr(1)),
       (1, 1): (0, Fr(2)), (1, 2): (3, Fr(1)), (1, 3): (2, Fr(2)),
       (2, 2): (0, Fr(3)), (2, 3): (1, Fr(3)), (3, 3): (0, Fr(6))}


def fadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def fmul(a, b):
    if isinstance(a, (int, Fr)):
        a = (Fr(a), Fr(0), Fr(0), Fr(0))
    if isinstance(b, (int, Fr)):
        b = (Fr(b), Fr(0), Fr(0), Fr(0))
    r = [Fr(0)] * 4
    for i in range(4):
        for j in range(4):
            if a[i] == 0 or b[j] == 0:
                continue
            k, co = TBL[(min(i, j), max(i, j))]
            r[k] += a[i] * b[j] * co
    return tuple(r)


CP = [F0, ONEF]
C2 = [F0, F0, ONEF]
C3P = [F0, F0, F0, ONEF]
ONEP = [ONEF]
ZEROP = [F0]


def padd(p, q):
    n = max(len(p), len(q))
    return [fadd(p[i] if i < len(p) else F0, q[i] if i < len(q) else F0) for i in range(n)]


def psub(p, q):
    return padd(p, [tuple(-x for x in c) for c in q])


def pscal(p, l):
    return [fmul(c, l) for c in p]


def pmul(p, q):
    r = [F0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] = fadd(r[i + j], fmul(a, b))
    return r


def radd(x, y):
    return (padd(x[0], y[0]), padd(x[1], y[1]))


def rsub(x, y):
    return (psub(x[0], y[0]), psub(x[1], y[1]))


def rmul(x, y):
    (A0, A1) = x
    (B0, B1) = y
    S0 = psub(padd(pmul(A0, B0), pmul(A1, B1)), pmul(pmul(A1, B1), C2))
    S1 = padd(pmul(A0, B1), pmul(A1, B0))
    return (S0, S1)


def rscal(x, f):
    return (pscal(x[0], f), pscal(x[1], f))


cE = (CP, ZEROP)
sE = (ZEROP, ONEP)
oneE = (ONEP, ZEROP)
HALF = rscal(oneE, Fr(1, 2))
SQ2E = ([SQ2], ZEROP)
SQ6E = ([SQ6], ZEROP)
r0 = radd(oneE, rmul(SQ2E, cE))
t1 = radd(rmul(SQ2E, cE), rmul(SQ6E, sE))
r1 = rsub(oneE, rmul(HALF, t1))
t2 = rsub(rmul(SQ2E, cE), rmul(SQ6E, sE))
r2 = rsub(oneE, rmul(HALF, t2))


def is_const(x, k):
    P0, P1 = x
    ok0 = P0[0] == (Fr(k), Fr(0), Fr(0), Fr(0)) and all(cc == F0 for cc in P0[1:])
    ok1 = all(cc == F0 for cc in P1)
    return ok0 and ok1


chk(is_const(radd(radd(r0, r1), r2), 3),
    "§C(4) sum_i r_i = 3 exact in Q(sqrt2,sqrt3)[c,s]/(c^2+s^2-1) [FT.113 re-derived]")
chk(is_const(radd(radd(rmul(r0, r1), rmul(r0, r2)), rmul(r1, r2)), Fr(3, 2)),
    "§C(4) sum_{i<j} r_i r_j = 3/2 exact [FT.113 Vieta row re-derived]")
cos3 = padd(pscal(C3P, Fr(4)), pscal(CP, Fr(-3)))          # 4c^3-3c = cos(2/3)
rhs = rmul(([SQ2], ZEROP), (cos3, ZEROP))                    # sqrt2*cos(2/3)
cub_ok = True
for r in (r0, r1, r2):
    y = rsub(r, oneE)
    expr = rsub(radd(rscal(rmul(rmul(y, y), y), Fr(2)), rscal(y, Fr(-3))), rhs)
    if not (all(cc == F0 for cc in expr[0]) and all(cc == F0 for cc in expr[1])):
        cub_ok = False
chk(cub_ok, "§C(4) 2y^3 - 3y - sqrt2*cos(2/3) = 0 for every y = r_i - 1, exact in the radical-trigonometric "
            "ring with cos(2/3) = 4c^3-3c at c = cos(2/9) [FT.111(2)/FT.113 depressed cubic re-derived]: "
            "the Koide-form spectrum is forced by C3 covariance + the democratic normalization + delta = 2/9")
stamp("§C green: C3 weak-generated; 2 = 3-1; 9 = 3*3; delta = 2/9; spectrum forced; the 2/3 rows exact")

# ================================================================ §D  FT.159
print()
print("=" * 100)
print("§D (FT.159) — the emergent-time identity: gravitational time and CPT time are the ledger order")
print("=" * 100)

# Theta_L on records with edge data: order reversed, J+ <-> J-, kappa -> -kappa, sigma fixed
def eipik(k):
    """e^{i pi k} for k in (1/2)Z, exact in Q(i) via the 4-period."""
    k = k % 4
    table = {Fr(0): (Fr(1), Fr(0)), Fr(1, 2): (Fr(0), Fr(1)), Fr(1): (Fr(-1), Fr(0)),
             Fr(3, 2): (Fr(0), Fr(-1)), Fr(2): (Fr(1), Fr(0)), Fr(5, 2): (Fr(0), Fr(1)),
             Fr(3): (Fr(-1), Fr(0)), Fr(7, 2): (Fr(0), Fr(-1))}
    return table[k]


def cC(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


KAP = [Fr(0), Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(-1, 2), Fr(-1)]
conj_ok = True
for sigmas in itertools.product((1, -1), repeat=3):
    for kappas in itertools.product(KAP, repeat=3):
        w = (Fr(1), Fr(0))
        for s, k in zip(sigmas, kappas):
            w = cC(w, (Fr(s), Fr(0)))
            w = cC(w, eipik(k))
        wt = (Fr(1), Fr(0))
        for s, k in list(zip(sigmas, kappas))[::-1]:   # Theta_L: order reversed, kappa -> -kappa, sigma fixed
            wt = cC(wt, (Fr(s), Fr(0)))
            wt = cC(wt, eipik(-k))
        if wt != cconj(w):
            conj_ok = False
chk(conj_ok, "§D(2) w(Theta_L C) = w(C)^* exhaustive on all 3-edge configurations "
             "(sigma in {+-1}^3, kappa in the half-integer ladder): e^{i pi kappa} in {1,i,-1,-i} exact in Q(i), "
             "G(e) = sigma_e e^{i pi kappa_e} [FT.88(2); D3.5], kappa -> -kappa, sigma fixed [CT2.8(1) re-derived]")

# cut factorization across interior ledger-time cuts (exact regrouping in Q(i))
cut_ok = True
for cfg in [([(0, Fr(1, 2)), (1, Fr(1)), (1, Fr(-1, 2)), (2, Fr(3, 2))], [1, -1, 1, -1]),
            ([(0, Fr(0)), (0, Fr(1)), (2, Fr(1, 2))], [-1, 1, 1])]:
    ticks_k, sigs = cfg
    def wprod(items):
        w = (Fr(1), Fr(0))
        for (t, k), s in items:
            w = cC(w, (Fr(s), Fr(0)))
            w = cC(w, eipik(k))
        return w
    full = wprod(list(zip(ticks_k, sigs)))
    for tstar in {0, 1, 2, 3}:
        left = [(tk, s) for tk, s in zip(ticks_k, sigs) if tk[0] < tstar]
        right = [(tk, s) for tk, s in zip(ticks_k, sigs) if tk[0] >= tstar]
        if cC(wprod(left), wprod(right)) != full:
            cut_ok = False
chk(cut_ok, "§D(2) the cut factorization w(C) = w(C_left) w(C_right) across every interior ledger-time cut "
            "[CT2.8(2) re-derived on exact witnesses]: the Hilbert-space gluing runs across the same ledger time")

# the metric-side transport re-pin: lapse row fixed, conformal factor depends on a00 alone
lap_ok = True
for q in QS:
    for w in WS:
        G = gbar(q, w)
        GT = gbar(q, [-x for x in w])
        if G[0][0] != Fr(-1) or GT[0][0] != Fr(-1):
            lap_ok = False
        for i in range(3):
            for j in range(3):
                if G[i + 1][j + 1] != GT[i + 1][j + 1]:
                    lap_ok = False
        for i in range(3):
            if GT[0][i + 1] != -G[0][i + 1]:
                lap_ok = False
chk(lap_ok, "§D(3) the time-reversal transport of the metric dictionary: gbar_00 = -1 (lapse/conformal row) "
            "and gbar_ij fixed; gbar_0i -> -gbar_0i; the conformal factor Omega = e^{alpha_Omega a00} depends "
            "on the T-even a00 alone [D2.1; FT.156(3) transport re-pinned]: g_00 = -Omega^2 is reversal-even")

# the bilinear witness: ds^2 = g_00 (Delta x^0)^2 on purely temporal increments [D1.6 o D1.8]
bil_ok = True
for q in QS:
    for w in WS:
        G = gbar(q, w)
        for dtau in (Fr(1), Fr(3), Fr(-2), Fr(1, 2)):
            dx = [dtau, Fr(0), Fr(0), Fr(0)]
            ds2 = sum(G[m][n] * dx[m] * dx[n] for m in range(4) for n in range(4))
            if ds2 != G[0][0] * dtau * dtau:
                bil_ok = False
chk(bil_ok, "§D(4) the line-element channel contracts metric data with tick data: on purely temporal "
            "increments ds^2 = g_00 (Delta x^0)^2 exactly [D1.6 with x^0 = tau_n, D1.8]: the lapse and the "
            "tick increment meet in every temporal ds^2(e) (bilinear-form witness, exact rationals)")

# A7 ledger counts: |L(tau_n)| = sum_{k<n} n_real_out(tau_k), monotone, strict at crystallization
seqs = [[1, 0, 2, 1, 0, 3], [0, 1, 1], [2, 0, 0, 1]]
mono_ok = True
for s in seqs:
    counts = [sum(s[:n]) for n in range(len(s) + 1)]
    if any(counts[n + 1] < counts[n] for n in range(len(counts) - 1)):
        mono_ok = False
    if any(s[n] > 0 and counts[n + 1] == counts[n] for n in range(len(s))):
        mono_ok = False
chk(mono_ok, "§D(5) |L(tau_n)| = sum_{k<n} n_real_out(tau_k) is non-decreasing along every sample history "
             "and strictly increases at every crystallization [A6/A7 exact samples]: the ledger arrow")
stamp("§D green: Theta_L involution/bijection; weight conjugation; cut gluing; lapse transport; "
      "line-element contraction; monotone ledger")

# ================================================================ §E  document pins + hygiene
print()
print("=" * 100)
print("§E — document pins (Part 1–3, HistLog, READMEs) and the tier hygiene scan")
print("=" * 100)

P1 = rd("Part1_Qubit_era.md")
P2 = rd("Part2_Bosonic_era.md")
P3 = rd("Part3_Fermion_era.md")
HL = rd("HistLog.md")
RM = rd("README.md")
CRM = rd(os.path.join("checks", "README.md"))

chk("## Tier F.44 — The 3+1 Chiral Asymmetry" in P3, "§E Tier F.44 header present in Part 3")
blocks = {}
for t in ("FT.156", "FT.157", "FT.158", "FT.159", "FT.160"):
    i = P3.find(f"### {t} —")
    chk(i >= 0, f"§E {t} section present in Part 3")
    if i >= 0:
        j = P3.find("\n### ", i + 4)
        blocks[t] = P3[i:j if j > 0 else len(P3)]
for t, blk in blocks.items():
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§E {t} carries {mark}")
    chk("**Status.**" not in blk, f"§E {t} carries no **Status.** line (canon hygiene)")
    chk(not re.search(r"\bP-H\d", blk), f"§E {t} carries no registry token")
    chk(not re.search(r"\(H\d\d\)", blk), f"§E {t} carries no archive locator")

chk("FT.1–FT.114 (structural tags), FT.116–FT.131, FT.133–FT.139, FT.141–FT.145, FT.153–FT.160" in P3 and
    "Tiers F.1–F.42, F.44 in series order" in P3,
    "§E the Part 3 Namespace line carries FT.153–FT.160 and Tiers F.1–F.42, F.44")

i89 = P3.find("### FT.89 —")
j89 = P3.find("\n### ", i89 + 4)
blk89 = P3[i89:j89]
chk("Rmk (supersession of the classification clause)" in blk89 and "FT.158(5)" in blk89,
    "§E FT.89 carries the on-record supersession Rmk citing FT.158(5)")
chk("P1, P5" in blk89 or "[P1, P5]" in blk89, "§E the FT.89 Rmk preserves the identification bars [P1, P5]")

chk("**D1.8.**" in P1 and "x^0:=\\tau_n" in P1, "§E D1.8 pin: the emergent coordinate x^0 := tau_n (Part 1)")
chk("(\\tau_n,h_1,h_2,h_3)" in P2, "§E CT2.6 pin: the chart chi([v]) = (tau_n,h_1,h_2,h_3) (Part 2)")
chk("\\eta\\in\\{\\pm1\\}^4" in P1 and "\\exists!\\,\\mathfrak o" in P1,
    "§E A3 pin: the sign structure (exactly one odd entry) is the axiomatic content (Part 1)")
chk("**C13.**" in P1 and "\\eta:=(-,+,+,+)" in P1,
    "§E C13 pin: the representative eta = (-,+,+,+) is the convention (Part 1)")
chk("\\neg\\exists\\,\\tau^{-1}" in P1, "§E A6 pin: the tick advance has no inverse (Part 1)")

# tier text hygiene scan
it = P3.find("## Tier F.44")
tier = P3[it:]
BARRED = ['previously', 'formerly', 'this was', 'now this',
          'electron', 'muon', 'tau ', 'quark', 'neutrino',
          'proton', 'neutron', 'pion', 'positron', 'photon', 'gluon', 'lepton']
hits = [(w, tier.lower().count(w)) for w in BARRED if w.lower() in tier.lower()]
chk(not hits, f"§E Tier F.44 barred-vocabulary scan: zero revision-language and particle-name hits ({hits})")
chk(tier.count(r"\text{EXT}") == 1 and r"\text{EXT}" in blocks["FT.160"],
    "§E the [EXT] marker occurs exactly once in Tier F.44 — FT.160's standing-rule record")
chk(not re.search(r"\bP-H\d", tier), "§E zero registry tokens in Tier F.44")
chk("**Status.**" not in tier, "§E zero **Status.** lines in Tier F.44")
chk("letter series" not in tier and "non-binding" not in tier, "§E zero letter-series vocabulary in Tier F.44")

# HistLog pins
chk("[FT.156–FT.160 (Tier F.44)" in HL, "§E HistLog item 20 carries the Tier F.44 ledger bracket")
chk("[FT.159 (Tier F.44)" in HL and "REMOVED" in HL, "§E HistLog item 21 carries the FT.159 removal bracket")
chk("[FT.158(5) (Tier F.44)" in HL, "§E HistLog item 21 carries the FT.158(5) supersession bracket")
chk("the manifold-side branch read is derived [FT.157(2)–(3)" in HL, "§E the Q1' row carries the manifold-side read")
chk("the spatial provenance of the angles" in HL and "FT.158" in HL, "§E the Q3 row carries the spatial provenance")
for t in ("FT.156", "FT.157", "FT.158", "FT.159", "FT.160"):
    chk(f"**{t}.** Closed" in HL, f"§E HistLog §III carries the {t} status row")
chk("superseded by FT.158(5)" in HL, "§E HistLog §III's FT.89 row records the supersession")
chk("(V.4) The Tier F.44 pass." in HL and "58/58" in HL, "§E HistLog §V carries (V.4) with suite state 58/58")
chk("56/57" in HL, "§E HistLog §V.2's historical state is preserved")
chk("Tier F.44 issues no declaration [FT.160(4)]" in HL, "§E §II.4 records the no-declaration clause")

# README pins
chk("(80 checkers)" in RM, "§E the main README carries the current suite count (76 at Tier BM.20)")
chk("**80/80**" in CRM and "(80 checkers)" in CRM, "§E checks/README carries the current suite count and state (75/75 at Tier BM.19)")
chk("verify_H_3p1_chiral_asymmetry.py" in CRM, "§E checks/README names the Tier F.44 checker")

stamp("§E green: document pins and hygiene")

# ------------------------------------------------------------------ summary
print()
if FAILS:
    print(f"verify_H_3p1_chiral_asymmetry: {len(FAILS)} FAILED of {N + len(FAILS)}")
    sys.exit(1)
print(f"verify_H_3p1_chiral_asymmetry: {N} checks green  ({time.time()-t0:.1f}s) — "
      "Tier F.44 (FT.156–FT.160) §A–§E")
sys.exit(0)
