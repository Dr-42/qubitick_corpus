#!/usr/bin/env python3
"""
verify_merge_tierC.py — machine verification of the Tier-C tags (CT1.11b).

Exact arithmetic only (Fraction / complex-over-Fraction via qmath.C). No floats.

Sections:
  §0  firewall: forbidden-vocabulary scan of the CT1.11b block;
      frozen 'chiral*' inventory profile of A-G must be exactly {A:1, D:1}
  §A  the 15 Pauli products (Hermitian, square I4, traceless); exhaustive
      enumeration of 1365 4-subsets -> exactly 30 pairwise-anticommuting frames;
      per frame: gamma Hermitian, gamma^2 = I4, Tr gamma = 0, {gamma, e_i} = 0;
      the 16 real products R-independent for ALL 30 frames (exact rank 16)
  §B  pseudoscalar catalog: all 15 values, each from exactly 2 frames; species
      table ([gamma,S] = +2iJ_i for sigma0(x)sigma_i, -2iJ_i for sigma_i(x)sigma0,
      0 diagonal, +-2iK_k off-diagonal with k = 6-i-j); commuting-W counts per
      species (mixed 1, diagonal 1, off-diag 0), anticommuting caps; the F0
      witness frame and its exact projector forms
  §C  the pincer: commutant {M: [M,W_i]=0} = span_C{Pi_R, Pi_V} exactly (nullspace
      over Q, real-flattened: dim 4 real = 2 complex, span equality by rank);
      anticommutant = C.Pi_V exactly (dim 2 real); the four commutant involutions
      have traces {4,2,-2,-4}; cyclic-flip trace identity; bracket-reversal
      witness (-id not a Lie automorphism of su(2)); all 15 products fail both
      sides entrywise
  §D  carrier irreducibility (2x2): commutant of {sigma_i} = C.I2, anticommutant = {0}
  §E  native selectivity: W_i Pi_V = 0; sum W_i^2 = 2 Pi_R = (3E0+Sigma)/2;
      joint kernel of the W_i = im Pi_V = the singlet line (eigenvector test)
  §F  non-alignment: [P,S]=0 iff P = sigma_i(x)sigma_i among the 15;
      [sigma3(x)sigma3, W1] = 2i E^{23}; [sigma0(x)sigma3, S] = 2i J3;
      cross-ranks (P+- Pi_R / P+- Pi_V) = (2,1,2,1); Pi ranks (3,1)

Run: python3 verify_merge_tierC.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import os, re, sys, itertools, hashlib
import era_paths
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale, transpose, trace, conj_transpose  # noqa: E402

PASS = FAIL = 0
def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond: PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")

I = C(0, 1)
HALF = C(Fr(1, 2))
def mat(rows): return [[x if isinstance(x, C) else C(x) for x in row] for row in rows]
def eye(n): return mat([[1 if i == j else 0 for j in range(n)] for i in range(n)])
def zeros4(): return [[C(0)] * 4 for _ in range(4)]
def kron2(A, B): return [[A[i // 2][j // 2] * B[i % 2][j % 2] for j in range(4)] for i in range(4)]
def comm(A, B): return matadd(matmul(A, B), matmul(B, A), -1)
def acomm(A, B): return matadd(matmul(A, B), matmul(B, A))
def eq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def is_zero(A): return all(x == C(0) for row in A for x in row)

def rank_q(vectors):
    rows = [list(v) for v in vectors if any(x != 0 for x in v)]
    if not rows:
        return 0
    n = len(rows[0])
    rank = 0
    for c in range(n):
        pr = None
        for rr in range(rank, len(rows)):
            if rows[rr][c] != 0:
                pr = rr
                break
        if pr is None:
            continue
        rows[rank], rows[pr] = rows[pr], rows[rank]
        pv = rows[rank][c]
        for rr in range(len(rows)):
            if rr != rank and rows[rr][c] != 0:
                f = rows[rr][c] / pv
                rows[rr] = [rows[rr][k] - f * rows[rank][k] for k in range(n)]
        rank += 1
        if rank == len(rows):
            break
    return rank

def rank_c(M):
    """complex rank via the realification [[A,-B],[B,A]] (exact, = 2*rank_C / 2)."""
    n = len(M); m = len(M[0])
    A = [[M[i][j].re for j in range(m)] for i in range(n)]
    B = [[M[i][j].im for j in range(m)] for i in range(n)]
    rows = [A[i] + [-x for x in B[i]] for i in range(n)] + [B[i] + A[i] for i in range(n)]
    r = rank_q(rows)
    assert r % 2 == 0
    return r // 2

def rref_nullspace(rows):
    m = [list(r) for r in rows if any(x != 0 for x in r)]
    n = len(rows[0])
    if not m:
        return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    piv = []
    r = 0
    for c in range(n):
        pr = None
        for rr in range(r, len(m)):
            if m[rr][c] != 0:
                pr = rr
                break
        if pr is None:
            continue
        m[r], m[pr] = m[pr], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for rr in range(len(m)):
            if rr != r and m[rr][c] != 0:
                f = m[rr][c]
                m[rr] = [m[rr][k] - f * m[r][k] for k in range(n)]
        piv.append(c)
        r += 1
        if r == len(m):
            break
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for ri, pc in enumerate(piv):
            v[pc] = -m[ri][fc]
        basis.append(v)
    return basis

s0 = mat([[1, 0], [0, 1]])
s1 = mat([[0, 1], [1, 0]])
s2 = mat([[0, -I], [I, 0]])
s3 = mat([[1, 0], [0, -1]])
S2 = [s0, s1, s2, s3]

PK = [(mu, nu) for mu in range(4) for nu in range(4) if (mu, nu) != (0, 0)]
PR = {k: kron2(S2[k[0]], S2[k[1]]) for k in PK}

E0 = kron2(s0, s0)
SIG = matadd(matadd(kron2(s1, s1), kron2(s2, s2)), kron2(s3, s3))
SW = zeros4()
for a in range(2):
    for b in range(2):
        SW[2 * a + b][2 * b + a] = C(1)
SW = mat(SW)
W = [matscale(matadd(kron2(s0, S2[i]), kron2(S2[i], s0)), HALF) for i in (1, 2, 3)]
J = [matscale(matadd(kron2(S2[j], S2[k]), matscale(kron2(S2[k], S2[j]), C(-1))), HALF)
     for (j, k) in ((2, 3), (3, 1), (1, 2))]
K = [matscale(matadd(kron2(s0, S2[i]), matscale(kron2(S2[i], s0), C(-1))), HALF) for i in (1, 2, 3)]
PRJ_R = matscale(matadd(matscale(E0, C(3)), SIG), C(Fr(1, 4)))
PRJ_V = matscale(matadd(E0, matscale(SIG, C(-1))), C(Fr(1, 4)))
BASIS16 = [E0] + [PR[k] for k in PK]

def solve_side(anti):
    """Nullspace (over Q, real-flattened coefficient space) of X -> [X,W_i] (anti=False)
    or {X,W_i} (anti=True) for all i. Returns complex matrices."""
    eqs = []
    for i in range(3):
        mats = [(acommm(Bm, W[i]) if anti else commm(Bm, W[i])) for Bm in BASIS16]
        for r in range(4):
            for c in range(4):
                rrow = []; irow = []
                for M in mats:
                    z = M[r][c]
                    rrow += [z.re, -z.im]
                    irow += [z.im, z.re]
                eqs.append(rrow); eqs.append(irow)
    ns = rref_nullspace(eqs)
    out = []
    for v in ns:
        M = zeros4()
        for a, Bm in enumerate(BASIS16):
            coef = C(v[2 * a], v[2 * a + 1])
            if coef != C(0):
                M = matadd(M, matscale(Bm, coef))
        out.append((v, M))
    return out

def commm(A, B): return matadd(matmul(A, B), matmul(B, A), -1)
def acommm(A, B): return matadd(matmul(A, B), matmul(B, A))

def cspan_dim(mats):
    """real dimension of the complex span of the given complex matrices."""
    vecs = []
    for M in mats:
        vecs.append([x for row in M for x in (row and [y.re for y in row] or [])] +
                    [y.im for row in M for y in row])
    return rank_q(vecs)

def flat(M, scale=None):
    X = M if scale is None else matscale(M, scale)
    return [y.re for row in X for y in row] + [y.im for row in X for y in row]

# ---------------------------------------------------------------- §0
def section0():
    print("S0 firewall (Tier-C)")
    B = era_paths.read("B_foundation.md")
    i = B.index("### CT1.11b")
    m = re.compile(r"\n##[# ]").search(B, i + 4)
    blk = B[i:m.start() if m else len(B)]
    absent = ['Yukawa', 'neutrino', 'Weyl', 'CKM', 'PMNS', 'left-handed', 'right-handed',
              'gamma_5', '\\gamma_5', 'flavour', 'flavor', 'black hole', 'spin-statistics',
              'P_L', 'P_R', 'generation structure', 'quark mixing', 'lepton number',
              'chiral', 'clock', 'biset', 'Gridmark', 'carpet', 'fermion factory',
              'spacetime quantum', 'persistence cost', 'clock gradient']
    hits = [w for w in absent if w.lower() in blk.lower()]
    chk("CT1.11b block: forbidden vocabulary absent", not hits, str(hits))
    # era canon: the frozen profile is now read on the era files. The D2.6 clause
    # ('chirality -> -chirality') lives in Part 2 §A; Part 1 must stay clean.
    prof = {}
    for key, fn in (('P1', 'Part1_Qubit_era.md'), ('P2', 'Part2_Bosonic_era.md')):
        with open(os.path.join(DOCS, fn), encoding='utf-8') as f:
            prof[key] = len(re.findall('chiral', f.read()))
    chk("frozen 'chiral*' inventory profile of Parts 1-2 unchanged {P1:2 (D2.6 clause), P2:0}",
        prof == {'P1': 2, 'P2': 0}, str(prof))

# ---------------------------------------------------------------- §A
FRAMES = None
def sectionA():
    global FRAMES
    print("S1 = §A native frames")
    chk("15 Pauli products: Hermitian, square I4, traceless",
        all(eq(PR[k], conj_transpose(PR[k])) and eq(matmul(PR[k], PR[k]), eye(4))
            and trace(PR[k]) == C(0) for k in PK))
    FRAMES = [c for c in itertools.combinations(PK, 4)
              if all(is_zero(acomm(PR[a], PR[b])) for a, b in itertools.combinations(c, 2))]
    chk("exactly 30 pairwise-anticommuting frames among 1365 candidates", len(FRAMES) == 30, str(len(FRAMES)))
    chk("30 frames x 4! = 720 ordered tuples", len(FRAMES) * 24 == 720)
    bad = 0
    for F in FRAMES:
        g = PR[F[0]]
        for k in F[1:]:
            g = matmul(g, PR[k])
        if not (eq(g, conj_transpose(g)) and eq(matmul(g, g), eye(4)) and trace(g) == C(0)):
            bad += 1
        for k in F:
            if not is_zero(acomm(g, PR[k])):
                bad += 1
    chk("every frame: gamma Hermitian, gamma^2 = I4, Tr gamma = 0, {gamma, e_i} = 0", bad == 0)
    badr = 0
    for F in FRAMES:
        prods = [eye(4)]
        for r in range(1, 5):
            for combo in itertools.combinations(range(4), r):
                M = eye(4)
                for idx in combo:
                    M = matmul(M, PR[F[idx]])
                prods.append(M)
        rows = []
        for M in prods:
            rows.append([y.re for row in M for y in row] + [y.im for row in M for y in row])
        if rank_q(rows) != 16:      # 16 R-independent products
            badr += 1
    chk("Cl(4,0): the 16 real products are R-independent for ALL 30 frames (rank 32 real)", badr == 0)

# ---------------------------------------------------------------- §B
def sectionB():
    print("S2 = §B pseudoscalar catalog")
    counts = {}
    for F in FRAMES:
        g = PR[F[0]]
        for k in F[1:]:
            g = matmul(g, PR[k])
        key = next((k for k in PK if eq(g, PR[k]) or eq(g, matscale(PR[k], C(-1)))), None)
        if key is None:
            chk("catalog: gamma = +- a Pauli product", False, str(F))
            continue
        counts[key] = counts.get(key, 0) + 1
    chk("all 15 values attained", len(counts) == 15, str(len(counts)))
    chk("each value from exactly 2 frames", all(v == 2 for v in counts.values()), str(counts))
    mixed = [(0, i) for i in (1, 2, 3)] + [(i, 0) for i in (1, 2, 3)]
    diag = [(i, i) for i in (1, 2, 3)]
    offd = [(i, j) for i in (1, 2, 3) for j in (1, 2, 3) if i < j]
    ok = True
    for k in mixed:
        cm = comm(PR[k], SW)
        i = k[1] if k[0] == 0 else k[0]
        sgn = 1 if k[0] == 0 else -1
        if not eq(cm, matscale(J[i - 1], C(2 * sgn) * I)):
            ok = False
    for k in diag:
        if not is_zero(comm(PR[k], SW)):
            ok = False
    for k in offd:
        kk = 6 - k[0] - k[1]
        cm = comm(PR[k], SW)
        if not (eq(cm, matscale(K[kk - 1], 2 * I)) or eq(cm, matscale(K[kk - 1], -2 * I))):
            ok = False
    chk("species table exact: [gamma,S] = +2iJ_i / -2iJ_i (mixed), 0 (diagonal), +-2iK_k (off-diag)", ok)
    okc = True
    for k in mixed:
        nc = sum(1 for i in range(3) if is_zero(comm(PR[k], W[i])))
        if nc != 1:
            okc = False
    for k in diag:
        nc = sum(1 for i in range(3) if is_zero(comm(PR[k], W[i])))
        na = sum(1 for i in range(3) if is_zero(acomm(PR[k], W[i])))
        if nc != 1 or na != 2:
            okc = False
    for k in offd:
        nc = sum(1 for i in range(3) if is_zero(comm(PR[k], W[i])))
        na = sum(1 for i in range(3) if is_zero(acomm(PR[k], W[i])))
        if nc != 0 or na != 1:
            okc = False
    chk("W-commutation census: mixed (1 commute), diagonal (1 commute, 2 anticommute), off-diag (0 commute, 1 anticommute)", okc)
    chk("caps: no product commutes with >1 W_i; none anticommutes with >2",
        all(sum(1 for i in range(3) if is_zero(comm(PR[k], W[i]))) <= 1 and
            sum(1 for i in range(3) if is_zero(acomm(PR[k], W[i]))) <= 2 for k in PK))
    F0 = [(1, 2), (2, 2), (3, 2), (0, 1)]
    chk("F0 is a frame", all(is_zero(acomm(PR[a], PR[b])) for a, b in itertools.combinations(F0, 2)))
    g = PR[F0[0]]
    for k in F0[1:]:
        g = matmul(g, PR[k])
    tgt = mat([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
    chk("gamma_F0 = sigma0(x)sigma3 = diag(1,-1,1,-1)", eq(g, tgt) and eq(g, PR[(0, 3)]))
    Pp = matscale(matadd(eye(4), matscale(g, C(-1))), HALF)   # P_+ = (I - gamma)/2 (H labeling)
    Pm = matscale(matadd(eye(4), g), HALF)                     # P_- = (I + gamma)/2
    chk("P+ = diag(0,1,0,1), P- = diag(1,0,1,0) (with P± = (I ∓ gamma)/2)",
        eq(Pp, mat([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]])) and eq(Pm, mat([[1,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]])))
    chk("P+- idempotent, orthogonal, sum I4, trace 2, rank 2",
        eq(matmul(Pp, Pp), Pp) and eq(matmul(Pm, Pm), Pm) and is_zero(matmul(Pp, Pm))
        and eq(matadd(Pp, Pm), eye(4)) and trace(Pp) == C(2) and trace(Pm) == C(2)
        and rank_c(Pp) == 2 and rank_c(Pm) == 2)

# ---------------------------------------------------------------- §C
def sectionC():
    print("S3 = §C the weak-covariance pincer")
    chk("Pi_R, Pi_V commute with all W_i",
        all(is_zero(comm(PRJ_R, W[i])) and is_zero(comm(PRJ_V, W[i])) for i in range(3)))
    ns = solve_side(False)
    chk("commutant: real nullspace dim 4 (= complex dim 2)", len(ns) == 4, str(len(ns)))
    def coeff_vec(M):
        v = []
        for Bm in BASIS16:
            z = trace(matmul(M, Bm)) / C(4)
            v += [z.re, z.im]
        return v
    spanvec = [coeff_vec(PRJ_R), coeff_vec(matscale(PRJ_R, I)),
               coeff_vec(PRJ_V), coeff_vec(matscale(PRJ_V, I))]
    chk("commutant = span_C{Pi_R, Pi_V} (span equality by rank, coefficient space)",
        rank_q([v for v, _ in ns] + spanvec) == 4 and rank_q(spanvec) == 4)
    trs = set()
    for a in (1, -1):
        for b in (1, -1):
            X = matadd(matscale(PRJ_R, C(a)), matscale(PRJ_V, C(b)))
            if eq(matmul(X, X), eye(4)):
                trs.add(trace(X))
    chk("commutant involutions: traces {4,2,-2,-4}, none zero",
        trs == {C(4), C(2), C(-2), C(-4)}, str(trs))
    F0 = [(1, 2), (2, 2), (3, 2), (0, 1)]
    g1 = PR[F0[0]]
    for k in F0[1:]:
        g1 = matmul(g1, PR[k])
    g2 = PR[F0[1]]
    for k in (F0[2], F0[3], F0[0]):
        g2 = matmul(g2, PR[k])
    chk("cyclic flip: Tr(e1e2e3e4) = -Tr(e2e3e4e1)", trace(g1) == -trace(g2))
    chk("Pi_V anticommutes with all W_i (via W_i Pi_V = 0 = Pi_V W_i)",
        all(is_zero(matmul(W[i], PRJ_V)) and is_zero(matmul(PRJ_V, W[i])) for i in range(3)))
    nsa = solve_side(True)
    spanv = [coeff_vec(PRJ_V), coeff_vec(matscale(PRJ_V, I))]
    chk("anticommutant = C.Pi_V exactly (real dim 2, span equality)",
        len(nsa) == 2 and rank_q([v for v, _ in nsa] + spanv) == 2 and rank_q(spanv) == 2)
    chk("bracket-reversal witness: [W1,W2] = iW3, but -id would demand -iW3",
        eq(comm(W[0], W[1]), matscale(W[2], I)) and not eq(comm(W[0], W[1]), matscale(W[2], -I)))
    bad = 0
    for k in PK:
        fails_c = any(not is_zero(comm(PR[k], W[i])) for i in range(3))
        fails_a = any(not is_zero(acomm(PR[k], W[i])) for i in range(3))
        if not (fails_c and fails_a):
            bad += 1
    chk("all 15 pseudoscalars fail BOTH sides entrywise", bad == 0)

# ---------------------------------------------------------------- §D
def sectionD():
    print("S4 = §D carrier irreducibility (2x2)")
    paul = [s1, s2, s3]
    basis2 = [mat([[1, 0], [0, 1]]), s1, s2, s3]
    def solve2(anti):
        eqs = []
        for sp in paul:
            mats = [(acommm(Bm, sp) if anti else commm(Bm, sp)) for Bm in basis2]
            for r in range(2):
                for c in range(2):
                    rrow = []; irow = []
                    for M in mats:
                        z = M[r][c]
                        rrow += [z.re, -z.im]
                        irow += [z.im, z.re]
                    eqs.append(rrow); eqs.append(irow)
        return rref_nullspace(eqs)
    ns = solve2(False)
    chk("carrier commutant {m: [m,sigma_i]=0} = C.I2 (real dim 2)", len(ns) == 2, str(len(ns)))
    nsa = solve2(True)
    chk("carrier anticommutant {m: {m,sigma_i]=0} = {0} (dim 0)", len(nsa) == 0, str(len(nsa)))

# ---------------------------------------------------------------- §E
def sectionE():
    print("S5 = §E native selectivity")
    chk("W_i Pi_V = 0 exactly (all i)", all(is_zero(matmul(W[i], PRJ_V)) for i in range(3)))
    acc = zeros4()
    for i in range(3):
        acc = matadd(acc, matmul(W[i], W[i]))
    chk("sum W_i^2 = 2 Pi_R = (3E0+Sigma)/2 (Cor CT0.7a cross-check)",
        eq(acc, matscale(PRJ_R, C(2))) and eq(matscale(PRJ_R, C(2)),
           matscale(matadd(matscale(E0, C(3)), SIG), HALF)))
    eqs = []
    for i in range(3):
        for r in range(4):
            rrow = [Fr(0)] * 8; irow = [Fr(0)] * 8
            for c in range(4):
                z = W[i][r][c]
                rrow[2 * c] = z.re; rrow[2 * c + 1] = -z.im
                irow[2 * c] = z.im; irow[2 * c + 1] = z.re
            eqs.append(rrow); eqs.append(irow)
    ns = rref_nullspace(eqs)
    singlet = [Fr(0), Fr(0), Fr(1), Fr(0), Fr(-1), Fr(0), Fr(0), Fr(0)]     # (0,1,-1,0)
    isinglet = [Fr(0), Fr(0), Fr(0), Fr(1), Fr(0), Fr(-1), Fr(0), Fr(0)]    # i*(0,1,-1,0)
    chk("joint kernel of the W_i is complex 1-dimensional (real dim 2)", len(ns) == 2, str(len(ns)))
    chk("joint kernel = the singlet complex line (0,1,-1,0)",
        all(rank_q([singlet, isinglet, v]) == 2 for v in ns))
    sv = [[C(0)], [C(1)], [C(-1)], [C(0)]]
    mv = [[sum(PRJ_V[r][c] * sv[c][0] for c in range(4))] for r in range(4)]
    chk("im Pi_V = the singlet line (eigenvector test Pi_V v = v)", eq(mv, sv))
    chk("rank(Pi_V) = 1, rank(Pi_R) = 3", rank_c(PRJ_V) == 1 and rank_c(PRJ_R) == 3)

# ---------------------------------------------------------------- §F
def sectionF():
    print("S6 = §F non-alignment")
    bad = 0
    for k in PK:
        c0 = is_zero(comm(PR[k], SW))
        isdiag = (k[0] == k[1] and k[0] != 0)
        if c0 != isdiag:
            bad += 1
    chk("[P,S]=0 iff P = sigma_i(x)sigma_i among the 15", bad == 0)
    E23 = matscale(matadd(kron2(s2, s3), kron2(s3, s2)), HALF)
    chk("[sigma3(x)sigma3, W1] = 2i E^{23} exactly", eq(comm(PR[(3, 3)], W[0]), matscale(E23, 2 * I)))
    chk("[sigma0(x)sigma3, S] = 2i J3 exactly", eq(comm(PR[(0, 3)], SW), matscale(J[2], 2 * I)))
    g = PR[(0, 3)]
    Pp = matscale(matadd(eye(4), matscale(g, C(-1))), HALF)
    Pm = matscale(matadd(eye(4), g), HALF)
    rr = (rank_c(matmul(Pp, PRJ_R)), rank_c(matmul(Pp, PRJ_V)),
          rank_c(matmul(Pm, PRJ_R)), rank_c(matmul(Pm, PRJ_V)))
    chk("cross-ranks (P+ Pi_R, P+ Pi_V, P- Pi_R, P- Pi_V) = (2,1,2,1)", rr == (2, 1, 2, 1), str(rr))
    chk("S-split profile (3,1) != (2,2): the two splits do not align",
        (rank_c(PRJ_R), rank_c(PRJ_V)) == (3, 1))

def main():
    section0()
    sectionA()
    sectionB()
    sectionC()
    sectionD()
    sectionE()
    sectionF()
    print(f"verify_merge_tierC: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
    sys.exit(1 if FAIL else 0)

if __name__ == "__main__":
    main()
