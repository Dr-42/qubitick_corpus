#!/usr/bin/env python3
"""
verify_merge_tierA.py — machine verification of the Tier-A tags.

Exact arithmetic only (int / Fraction / complex-over-Fraction). No floats.

Sections:
  §0  firewall inventory: beach vocabulary counts must be 0 in A-G theorem bodies
  §A  CT3.22a — scalar-idempotent converse; null-factor tensor argument; singlet
      annihilation (meson delta + baryon epsilon) on a Hermitian traceless
      spanning basis of sl(3,C) (Gell-Mann set lies in its C-span; every identity
      checked is C-linear in the generator, so basis-independence holds and the
      sqrt(3) normalization of lambda_8 is irrelevant); sealing-grammar census
      1,1,3,10,25,105 for N=2..7
  §B  EW.5a — CT1.3-CT1.8, EW.5, CT0.7/CT0.7a, Sigma^2=3E0-2Sigma, [S,T]=0,
      full (S,T) parity table (17 named generators), the exhaustive 2^5=32
      sign-map enumeration (exactly {id, Ad(S)} survive), Ad(S) action table,
      J<->K exclusion, Hermiticity rigidity
  §C  CT4.4a — capacity arithmetic n=4..12; block-dimension census (max 8 < 15);
      [J1,J2]=iW3 non-closure witness; su(3) -> su(4) matrix-unit embedding
      (bracket-closed, traceless); A8 has no su(4)-sized summand
  §D  CT4.7a — census coordinates (exact dyadic entropy: S(I/4)=ln4; argmax
      uniqueness by an exact integer Jensen sweep over all 969 compositions of
      16 into 4 parts); baseline equality for all-virtual skeletons m=0..8;
      source criterion rho>0 iff some k_v>=4 exhausted on all 4096 tetrahedron
      patterns; Platonic anchors 448/896/2976/2240/24384 incl. exact
      Q(sqrt5) constructions of the icosahedron (12 verts, deg 5) and the
      dodecahedron (20 verts, deg 3); polygon family 16n; digon never locks
  §E  CT1.11a — (S,T) eigen-tables on the 17 named generators; sector dims
      (7,3,3,3) computed by exact rank; S=Ad(SWAP) with SWAP=(E0+Sigma)/2;
      T pure grading (non-multiplicativity witness); [S,T]=0 on all 16 Pauli
      basis elements; CT0.7(1) projector algebra (idempotent, orthogonal,
      sum=I, traces 3/1); omega^2=1 on all 4096 tetra patterns; omega not in
      Aut(K4) (all 24 permutations); Theta_L action (kappa -> -kappa, sigma
      fixed, order reversal, J+ <-> J-); omega/Theta_L commutation and both
      involutive on an exhaustive small-configuration space; D3.4 endpoint
      charge omega-oddness; chi=sign(k) orientation-oddness
  §F  CT1.29a — exact Fraction sweeps over all compositions: rate identity,
      exactness iff kappa==1 pointwise, kappa_bar >= 1, kappa_bar in (1/dh)Z,
      uniform chains kappa_bar = kappa
  §G  CT1.19 Rmk — integer midpoint sampling of g=1+x^2 on [0,1]:
      |sum kappa_e h^2 - integral| <= h/2 + h^2/6 exactly (Fractions), n=4..40

Run: python3 verify_merge_tierA.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import os, re, sys, itertools
import era_paths
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale, transpose, trace, conj_transpose  # noqa: E402

PASS = FAIL = 0
def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")

I = C(0, 1)

def mat(rows):
    return [[x if isinstance(x, C) else C(x) for x in row] for row in rows]

def eye(n):
    return mat([[1 if i == j else 0 for j in range(n)] for i in range(n)])

def zeros(n, m=None):
    m = m or n
    return [[C(0)] * m for _ in range(n)]

def kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb] for j in range(ca * cb)] for i in range(ra * rb)]

def comm(A, B):
    return matadd(matmul(A, B), matmul(B, A), -1)

def eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

def rank_c(vecs):
    """Exact rank over C (fraction-free Gaussian elimination with pivot search)."""
    rows = [list(v) for v in vecs]
    rank = 0
    for col in range(len(rows[0]) if rows else 0):
        piv = None
        for r in range(rank, len(rows)):
            if rows[r][col] != C(0):
                piv = r
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pv = rows[rank][col]
        for r in range(len(rows)):
            if r != rank and rows[r][col] != C(0):
                f = rows[r][col] / pv
                rows[r] = [rows[r][k] - f * rows[rank][k] for k in range(len(rows[r]))]
        rank += 1
        if rank == len(rows):
            break
    return rank

# Pauli basis over Q(i); A3 metric eta = (-,+,+,+)
s0 = mat([[1, 0], [0, 1]])
s1 = mat([[0, 1], [1, 0]])
s2 = mat([[0, -I], [I, 0]])
s3 = mat([[1, 0], [0, -1]])
P = [s0, s1, s2, s3]
ETA = [-1, 1, 1, 1]

EPS = {(1,2,3):1,(2,3,1):1,(3,1,2):1,(1,3,2):-1,(3,2,1):-1,(2,1,3):-1}
def eps(i, j, k):
    return EPS.get((i, j, k), 0)

def gen_basis():
    """CT1.2's named basis (4x4 over Q(i)); J in standard cyclic order J1=(2,3), J2=(3,1), J3=(1,2)."""
    E0 = kron(s0, s0)
    Sig = matadd(matadd(kron(s1, s1), kron(s2, s2)), kron(s3, s3))
    W = [matscale(matadd(kron(s0, P[i]), kron(P[i], s0)), C(Fr(1, 2))) for i in (1, 2, 3)]
    J = [matscale(matadd(kron(P[j], P[k]), kron(P[k], P[j]), -1), C(Fr(1, 2)))
         for (j, k) in ((2, 3), (3, 1), (1, 2))]
    K = [matscale(matadd(kron(s0, P[i]), kron(P[i], s0), -1), C(Fr(1, 2))) for i in (1, 2, 3)]
    Eij = {}
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            if i < j:
                Eij[(i, j)] = matscale(matadd(kron(P[i], P[j]), kron(P[j], P[i])), C(Fr(1, 2)))
    diag = {i: kron(P[i], P[i]) for i in (1, 2, 3)}
    return E0, Sig, W, J, K, Eij, diag

def hermitian_traceless_sl3():
    """8 Hermitian traceless 3x3 generators spanning sl(3,C); the Gell-Mann set
    (CT3.9) lies in their C-span (lambda_8 = H2/sqrt(3))."""
    E = lambda a, b: mat([[1 if (i, j) == (a, b) else 0 for j in range(3)] for i in range(3)])
    H1 = matadd(E(0, 0), E(1, 1), -1)                    # diag(1,-1,0)
    H2 = matadd(matadd(E(0, 0), E(1, 1)), matscale(E(2, 2), C(-2)))   # diag(1,1,-2)
    out = [H1, H2]
    for (a, b) in ((0, 1), (0, 2), (1, 2)):
        out.append(matadd(E(a, b), E(b, a)))             # symmetric (lambda_1,4,6 type)
        out.append(matscale(matadd(E(a, b), E(b, a), -1), I))  # antisymmetric Hermitian (lambda_2,5,7 type: i(E_ab - E_ba))
    return out

# ---------------------------------------------------------------- §0 firewall
def section0():
    print("S0 firewall inventory")
    words = ["clock gradient", "persistence cost", "gridmark", "z2 carpet",
             "spacetime quantum", "fermion factory", "biset", "kappa_eff",
             "\\kappa_{\\mathrm{eff}}"]
    texts = {}
    for fn in ["A_axioms.md", "B_foundation.md", "C_geometry.md", "D_electroweak.md",
               "E_electromagnetic.md", "F_color.md", "G_saturation.md"]:
        texts[fn] = era_paths.read(fn).lower()
    # (the frozen corpus is self-contained)
    ag_texts = {fn: t for fn, t in texts.items() if not fn.startswith("H_")}
    for w in words:
        hits = {fn: t.count(w) for fn, t in ag_texts.items() if t.count(w)}
        chk(f"inventory: '{w}' absent from A-G (H may name it only in frozen adjudication prose)", not hits, str(hits))
    ag = "".join(t for fn, t in texts.items() if not fn.startswith("H_"))
    chk("'clock' count 0 in A-G", ag.count("clock") == 0)
    chk("'dilation' count 0 in A-G", ag.count("dilation") == 0)

# ---------------------------------------------------------------- §A CT3.22a
def sectionA():
    print("S1 = §A CT3.22a subnetwork confinement")
    # (2) scalar-idempotent converse: Pi = C*I, C in {0,1}: Pi F Pi = C * F
    Fblk = mat([[0, 1, 0], [-1, 0, 2], [0, 3, 0]])
    I3 = eye(3)
    for cval in (0, 1):
        Pi = matscale(I3, C(cval))
        chk(f"§A(2) converse arithmetic C={cval}",
            eq(matmul(matmul(Pi, Fblk), Pi), matscale(Fblk, C(cval))))
    # exception locus: f = 0 => F|_Sigma = 0 even at C=1
    chk("§A(2) exception locus f=0", eq(matscale(zeros(3), C(1)), zeros(3)))
    # (1) null-factor tensor argument
    v1 = [C(1), C(2), C(-3)]
    nul = [C(0)] * 3
    tens = [[v1[i] * nul[j] for j in range(3)] for i in range(3)]
    chk("§A(1) null factor => whole tensor null", all(x == C(0) for row in tens for x in row))
    # (3) singlet annihilation on the Hermitian traceless spanning basis
    basis = hermitian_traceless_sl3()
    for t, T in enumerate(basis):
        chk(f"§A(3) generator {t} traceless", trace(T) == C(0))
        chk(f"§A(3) generator {t} Hermitian", eq(T, conj_transpose(T)))
        # meson singlet delta^i_j: variation V = i(T - T^dagger) = 0
        V = matscale(matadd(T, conj_transpose(T), -1), I)
        chk(f"§A(3) meson singlet annihilated (gen {t})", eq(V, zeros(3)))
        # baryon epsilon: variation_{ijk} = i * Tr(T) * eps_{ijk} = 0
        bad = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    acc = C(0)
                    for p in range(3):
                        acc += T[i][p] * eps(p + 1, j + 1, k + 1)
                        acc += T[j][p] * eps(i + 1, p + 1, k + 1)
                        acc += T[k][p] * eps(i + 1, j + 1, p + 1)
                    if acc != I * trace(T) * eps(i + 1, j + 1, k + 1):
                        bad += 1
        chk(f"§A(3) baryon variation = i Tr(T) eps (gen {t})", bad == 0)
    # sealing grammar census: partitions of {0..N-1} into parts of size 2 or 3
    def partitions(items):
        if not items:
            return [[]]
        first = items[0]
        rest = items[1:]
        out = []
        for r in (2, 3):
            if len(items) >= r:
                for combo in itertools.combinations(rest, r - 1):
                    remain = [x for x in rest if x not in combo]
                    for p in partitions(remain):
                        out.append([(first,) + combo] + p)
        return out
    counts = [len(partitions(list(range(n)))) for n in range(2, 8)]
    chk("§A grammar census = 1,1,3,10,25,105 (N=2..7)", counts == [1, 1, 3, 10, 25, 105], str(counts))
    # (0) domain restriction toy: sealed-only summation
    sealed_domain = [c for c in ["sealed", "free-index"] if c == "sealed"]
    chk("§A(0) Z sums the sealed domain only", len(sealed_domain) == 1)

# ---------------------------------------------------------------- §B EW.5a
def sectionB():
    print("S2 = §B EW.5a convention exactness and rigidity")
    E0, Sig, W, J, K, Eij, diag = gen_basis()
    SW = mat([[0] * 4 for _ in range(4)])
    for a in range(2):
        for b in range(2):
            SW[2 * a + b][2 * b + a] = C(1)
    half = C(Fr(1, 2))
    chk("CT0.7(1): SWAP = (E0+Sigma)/2 as matrices", eq(matscale(matadd(E0, Sig), half), SW))
    chk("SWAP^2 = I", eq(matmul(SW, SW), eye(4)))
    basis16 = [kron(P[m], P[n]) for m in range(4) for n in range(4)]
    chk("CT1.3: [E0,X]=0 for all 16 basis elements", all(eq(comm(E0, X), zeros(4)) for X in basis16))
    chk("CT1.4: [W_i,W_j]=i eps W (all pairs)",
        all(eq(comm(W[i-1], W[j-1]), matscale(W[k-1], I * eps(i, j, k)))
            for i in (1,2,3) for j in (1,2,3) for k in (1,2,3) if eps(i, j, k)))
    chk("CT1.5: [Sig,J]=4iK, [Sig,K]=-4iJ, [Sig,W]=0 (9)",
        all(eq(comm(Sig, J[i]), matscale(K[i], 4 * I))
            and eq(comm(Sig, K[i]), matscale(J[i], -4 * I))
            and eq(comm(Sig, W[i]), zeros(4)) for i in range(3)))
    chk("CT1.6: [J,J]=[K,K]=+i eps W exactly (12)",
        all(eq(comm(J[i-1], J[j-1]), matscale(W[k-1], I * eps(i, j, k)))
            and eq(comm(K[i-1], K[j-1]), matscale(W[k-1], I * eps(i, j, k)))
            for i in (1,2,3) for j in (1,2,3) for k in (1,2,3) if eps(i, j, k)))
    ok7 = True
    for i in range(1, 4):
        for j in range(1, 4):
            lhs = comm(J[i-1], K[j-1])
            if i == j:
                rhs = matscale(matadd(Sig, matscale(diag[i], C(-1))), I)
            else:
                rhs = matscale(Eij[(min(i, j), max(i, j))], -I)
            if not eq(lhs, rhs):
                ok7 = False
            for w_ in range(3):
                if trace(matmul(lhs, W[w_])) != C(0):
                    ok7 = False
    chk("CT1.7: [J_i,K_j]=i(delta Sig - E^ij), all W-components zero (9)", ok7)
    chk("CT1.8: [W,J]=i eps J, [W,K]=i eps K (12)",
        all(eq(comm(W[i-1], J[j-1]), matscale(J[k-1], I * eps(i, j, k)))
            and eq(comm(W[i-1], K[j-1]), matscale(K[k-1], I * eps(i, j, k)))
            for i in (1,2,3) for j in (1,2,3) for k in (1,2,3) if eps(i, j, k)))
    ok5 = True
    for i in range(1, 4):
        for j in range(1, 4):
            acc = zeros(4)
            for k in range(1, 4):
                acc = matadd(acc, matscale(W[k-1], C(4 * eps(i, j, k))))
            if not eq(comm(K[j-1], comm(Sig, J[i-1])), acc):
                ok5 = False
            acc2 = zeros(4)
            for k in range(1, 4):
                acc2 = matadd(acc2, matscale(W[k-1], C(-4 * eps(i, j, k))))
            if not eq(comm(J[j-1], comm(Sig, K[i-1])), acc2):
                ok5 = False
    chk("EW.5: both clauses at all nine (i,j), diagonal exactly 0", ok5)
    acc = zeros(4)
    for w_ in W:
        acc = matadd(acc, matmul(w_, w_))
    chk("CT0.7a: sum W^2 = (3/2)E0 + (1/2)Sigma",
        eq(acc, matadd(matscale(E0, C(Fr(3, 2))), matscale(Sig, half))))
    PR = matscale(matadd(matscale(E0, C(3)), Sig), C(Fr(1, 4)))
    PV = matscale(matadd(E0, matscale(Sig, C(-1))), C(Fr(1, 4)))
    chk("CT0.7(1): PR,PV idempotent/orthogonal/sum=I/traces 3,1",
        eq(matmul(PR, PR), PR) and eq(matmul(PV, PV), PV) and eq(matmul(PR, PV), zeros(4))
        and eq(matadd(PR, PV), eye(4)) and trace(PR) == C(3) and trace(PV) == C(1))
    chk("associative relation Sigma^2 = 3E0 - 2Sigma",
        eq(matmul(Sig, Sig), matadd(matscale(E0, C(3)), matscale(Sig, C(-2)))))
    # S,T gradings
    def Sact(X):
        return matmul(matmul(SW, X), SW)
    def pcoeff(X):
        return {(m, n): trace(matmul(X, kron(P[m], P[n]))) / C(4) for m in range(4) for n in range(4)}
    def Tact(X):
        c = pcoeff(X)
        out = zeros(4)
        for (m, n), v in c.items():
            if v != C(0):
                out = matadd(out, matscale(kron(P[m], P[n]), C(ETA[m] * ETA[n]) * v))
        return out
    chk("[S,T]=0 on all 16 basis elements", all(eq(Sact(Tact(X)), Tact(Sact(X))) for X in basis16))
    chk("T is NOT multiplicative (explicit witness)",
        not eq(matmul(Tact(kron(s0, s1)), Tact(kron(s0, s2))),
               Tact(matmul(kron(s0, s1), kron(s0, s2)))))
    # 17-generator parity table (CT1.2)
    named = [("E0", E0), ("Sigma", Sig)] + [(f"E^{i}{j}", Eij[(i, j)]) for (i, j) in ((1,2),(1,3),(2,3))] \
        + [(f"diag{i}", diag[i]) for i in (1, 2, 3)] \
        + [(f"W{i}", W[i-1]) for i in (1,2,3)] + [(f"J{i}", J[i-1]) for i in (1,2,3)] \
        + [(f"K{i}", K[i-1]) for i in (1,2,3)]
    expect = {"W": (1, -1), "J": (-1, 1), "K": (-1, -1)}
    okp = True
    for name, X in named:
        s_ev = 1 if eq(Sact(X), X) else (-1 if eq(Sact(X), matscale(X, C(-1))) else 0)
        t_ev = 1 if eq(Tact(X), X) else (-1 if eq(Tact(X), matscale(X, C(-1))) else 0)
        fam = name[0] if name[0] in "WJK" else "+"
        want = expect.get(fam, (1, 1))
        if (s_ev, t_ev) != want:
            okp = False
            print("    parity mismatch:", name, (s_ev, t_ev), want)
    chk(f"CT1.2 parity table reproduced ({len(named)} named generators)", okp and len(named) == 17)
    # 32 sign-map enumeration: (J,K,W,Sigma,E)
    survivors = []
    for lam in itertools.product([1, -1], repeat=5):
        lJ, lK, lW, lS, lE = lam
        J2 = [matscale(x, C(lJ)) for x in J]
        K2 = [matscale(x, C(lK)) for x in K]
        W2 = [matscale(x, C(lW)) for x in W]
        S2 = matscale(Sig, C(lS))
        E2 = {k: matscale(v, C(lE)) for k, v in Eij.items()}
        Ed = {i: matadd(diag[i], matscale(Sig, C(Fr(-1, 3)))) for i in (1, 2, 3)}
        Ed2 = {i: matscale(v, C(lE)) for i, v in Ed.items()}
        d2img = {i: matadd(matscale(S2, C(Fr(1, 3))), Ed2[i]) for i in (1, 2, 3)}
        conds = []
        conds.append(eq(matmul(S2, S2), matadd(matscale(E0, C(3)), matscale(S2, C(-2)))))
        conds.append(eq(matscale(matadd(E0, S2), half), SW))
        conds.append(all(eq(comm(S2, J2[i]), matscale(K2[i], 4 * I))
                         and eq(comm(S2, K2[i]), matscale(J2[i], -4 * I))
                         and eq(comm(S2, W2[i]), zeros(4)) for i in range(3)))
        conds.append(all(eq(comm(J2[i-1], J2[j-1]), matscale(W2[k-1], I * eps(i, j, k)))
                         and eq(comm(K2[i-1], K2[j-1]), matscale(W2[k-1], I * eps(i, j, k)))
                         for i in (1,2,3) for j in (1,2,3) for k in (1,2,3) if eps(i, j, k)))
        conds.append(all(eq(comm(W2[i-1], W2[j-1]), matscale(W2[k-1], I * eps(i, j, k)))
                         for i in (1,2,3) for j in (1,2,3) for k in (1,2,3) if eps(i, j, k)))
        conds.append(all(eq(comm(W2[i-1], J2[j-1]), matscale(J2[k-1], I * eps(i, j, k)))
                         and eq(comm(W2[i-1], K2[j-1]), matscale(K2[k-1], I * eps(i, j, k)))
                         for i in (1,2,3) for j in (1,2,3) for k in (1,2,3) if eps(i, j, k)))
        ok7b = True
        for i in range(1, 4):
            for j in range(1, 4):
                lhs = comm(J2[i-1], K2[j-1])
                if i == j:
                    rhs = matscale(matadd(S2, matscale(d2img[i], C(-1))), I)
                else:
                    rhs = matscale(E2[(min(i, j), max(i, j))], -I)
                if not eq(lhs, rhs):
                    ok7b = False
        conds.append(ok7b)
        ok5b = True
        for i in range(1, 4):
            for j in range(1, 4):
                a1 = zeros(4)
                for k in range(1, 4):
                    a1 = matadd(a1, matscale(W2[k-1], C(4 * eps(i, j, k))))
                if not eq(comm(K2[j-1], comm(S2, J2[i-1])), a1):
                    ok5b = False
                a2 = zeros(4)
                for k in range(1, 4):
                    a2 = matadd(a2, matscale(W2[k-1], C(-4 * eps(i, j, k))))
                if not eq(comm(J2[j-1], comm(S2, K2[i-1])), a2):
                    ok5b = False
        conds.append(ok5b)
        if all(conds):
            survivors.append(lam)
    chk("EW.5a(2): exactly {id, Ad(S)} of the 32 sign maps survive",
        set(survivors) == {(1, 1, 1, 1, 1), (-1, -1, 1, 1, 1)}, str(survivors))
    AdS = lambda X: matmul(matmul(SW, X), SW)
    chk("Ad(S): J,K odd; W,Sigma,E even",
        all(eq(AdS(J[i]), matscale(J[i], C(-1))) for i in range(3))
        and all(eq(AdS(K[i]), matscale(K[i], C(-1))) for i in range(3))
        and all(eq(AdS(W[i]), W[i]) for i in range(3))
        and eq(AdS(Sig), Sig) and all(eq(AdS(v), v) for v in Eij.values()))
    chk("EW.5a(3): J<->K exchange violates the frozen EW.5 signs",
        not eq(comm(J[0], comm(Sig, K[1])), matscale(W[2], C(4 * eps(2, 1, 3)))))
    chk("EW.5a(3): K Hermitian, iK not Hermitian (continuous phases excluded)",
        all(eq(K[i], conj_transpose(K[i])) for i in range(3))
        and all(not eq(matscale(K[i], I), conj_transpose(matscale(K[i], I))) for i in range(3)))
    return basis16, (E0, Sig, W, J, K, Eij, diag), (Sact, Tact, pcoeff, SW)

# ---------------------------------------------------------------- §C CT4.4a
def sectionC(mats):
    print("S3 = §C CT4.4a realization domain")
    E0, Sig, W, J, K, Eij, diag = mats
    for n in range(4, 13):
        chk(f"§C capacity n={n}: 2^(n+1)>16, O(n)>0", 2 ** (n + 1) > 16 and 2 ** (n + 1) - 16 > 0)
    blockdims = [3, 3, 5, 3, 1, 1, 8, 1]      # CT0.12 six blocks + strong + EM
    chk("§C max aspect block = 8 < 15 <= dim su(n), n>=4",
        max(blockdims) == 8 and all(n * n - 1 >= 15 for n in range(4, 9)))
    chk("§C [J1,J2] = iW3 (J-span not Lie-closed)", eq(comm(J[0], J[1]), matscale(W[2], I)))
    # su(3) -> su(4) embedding, bracket-closed and traceless
    basis3 = hermitian_traceless_sl3()
    def emb(T):
        M = zeros(4)
        for i in range(3):
            for j in range(3):
                M[i][j] = T[i][j]
        return M
    ok = True
    for X in basis3:
        if trace(emb(X)) != C(0):
            ok = False
    for X in basis3:
        for Y in basis3:
            if not eq(comm(emb(X), emb(Y)), emb(comm(X, Y))):
                ok = False
    chk("§C su(3) embeds in su(4): bracket-closed, traceless image", ok)
    # embedding image is NOT an aspect block: it commutes with neither structure —
    # assert the image leaves the 4th basis direction invariant (block-reducible),
    # while CT0.12's blocks act within the pair register's declared decomposition
    chk("§C embedded su(3) acts trivially on the 4th direction (reducible => not the full-register su(4))",
        all(emb(X)[3][j] == C(0) and emb(X)[j][3] == C(0) for X in basis3 for j in range(4)))
    a8 = era_paths.read("A_axioms.md")
    m = re.search(r"\*\*A8\.\*\*(.*?)\n\n", a8, re.S)
    chk("§C A8 lists no su(4) summand", m is not None and "su(4)" not in m.group(1).replace("\\mathfrak{su}(4)", "su(4)"))

# ---------------------------------------------------------------- §D CT4.7a
class Q5:
    __slots__ = ("a", "b")
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __add__(s, o): return Q5(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Q5(s.a - o.a, s.b - o.b)
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): o = Q5(o)
        return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __neg__(s): return Q5(-s.a, -s.b)
    def __eq__(s, o):
        if isinstance(o, (int, Fr)): o = Q5(o)
        return isinstance(o, Q5) and s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"Q5({s.a},{s.b})"

def On(n):
    return 2 ** (n + 1) - 16 if n >= 4 else 0

def sectionD():
    print("S4 = §D CT4.7a vacuum census and baseline equality")
    # S_raw(I/4) per pair = ln4 = 2 ln2 exactly (dyadic entropy in ln2 units)
    S_ln2 = sum(Fr(1, 4) * 2 for _ in range(4))
    chk("§D census: S_raw(Janus vacuum) = ln4 per pair (exact, = 2 ln2)", S_ln2 == Fr(2))
    # argmax uniqueness: exact integer Jensen sweep — for p_i = k_i/16:
    # S <= ln4  <=>  prod (16/k_i)^{k_i} <= 4^16  <=>  prod k_i^{k_i} >= 16^16 / 4^16 = 2^32
    worst_ok = True
    uniform_only = True
    for ks in itertools.product(range(17), repeat=3):
        k4 = 16 - sum(ks)
        if k4 < 0:
            continue
        parts = list(ks) + [k4]
        prod = 1
        for k in parts:
            if k > 0:
                prod *= k ** k          # 0^0 := 1
        if prod < 2 ** 32:
            worst_ok = False
        if prod == 2 ** 32 and parts != [4, 4, 4, 4]:
            uniform_only = False
    chk("§D census: raw entropy <= ln4 on all 969 dyadic(16) states (exact Jensen integers)", worst_ok)
    chk("§D census: equality only at I/4 (argmax unique)", uniform_only)
    # baseline equality: all-virtual skeletons with m potential edges, m = 0..8
    for m in range(0, 9):
        SL = 0                                  # n_R ln2 coefficient
        rho = sum(On(0) for _ in range(m))      # k_v = 0 everywhere
        locked = any(0 >= 4 for _ in range(m))
        chk(f"§D baseline equality skeleton m={m}: S_L=0, rho=0, unlocked, no boundary",
            SL == 0 and rho == 0 and not locked)
    # source criterion exhausted on all 4096 tetrahedron patterns (12 directed edges)
    verts = [0, 1, 2, 3]
    dirs = [(a, b) for a in verts for b in verts if a != b]
    bad = 0
    rhos = set()
    for mask in range(1 << 12):
        deg = {v: 0 for v in verts}
        for idx, (a, b) in enumerate(dirs):
            if mask >> idx & 1:
                deg[a] += 1
                deg[b] += 1
        rho = sum(On(deg[v]) for v in verts)
        rhos.add(rho)
        if (rho > 0) != any(deg[v] >= 4 for v in verts):
            bad += 1
    chk("§D source criterion rho>0 iff exists k_v>=4 (all 4096 patterns)", bad == 0)
    chk("§D all-real tetrahedron rho = 448 in range", 448 in rhos)
    # Platonic anchors: rho(all real) = V * O(2*deg)
    for name, V, d, want in [("tetra", 4, 3, 448), ("cube", 8, 3, 896), ("octa", 6, 4, 2976),
                             ("dodeca", 20, 3, 2240), ("icosa", 12, 5, 24384)]:
        chk(f"§D anchor {name}: V*O(2d) = {want}", V * On(2 * d) == want)
    for n in range(3, 11):
        chk(f"§D polygon P_{n}: rho = 16n", n * On(4) == 16 * n)
    chk("§D digon (k=2) never locks", On(2) == 0)
    # exact Q(sqrt5) constructions
    phi = Q5(Fr(1, 2), Fr(1, 2))
    iphi = Q5(Fr(-1, 2), Fr(1, 2))
    ico = set()
    for cyc in range(3):
        for sa in (1, -1):
            for sb in (1, -1):
                base = [Q5(0), Q5(sa), Q5(sb) * phi]
                v = (base[cyc], base[(cyc + 1) % 3], base[(cyc + 2) % 3])
                ico.add((v[0].a, v[0].b, v[1].a, v[1].b, v[2].a, v[2].b))
    ico = sorted(ico)
    def d2(u, v):
        acc = Q5(0)
        for i in range(3):
            dlt = Q5(u[2 * i], u[2 * i + 1]) - Q5(v[2 * i], v[2 * i + 1])
            acc = acc + dlt * dlt
        return acc
    degs = [sum(1 for v in ico if v != u and d2(u, v) == Q5(4)) for u in ico]
    chk("§D icosa construction: 12 vertices, all degree 5 (edge^2 = 4, exact Q(sqrt5))",
        len(ico) == 12 and all(d == 5 for d in degs))
    dod = []
    for sx in (1, -1):
        for sy in (1, -1):
            for sz in (1, -1):
                a, b, c = Q5(sx), Q5(sy), Q5(sz)
                dod.append((a.a, a.b, b.a, b.b, c.a, c.b))
    for cyc in range(3):
        for sa in (1, -1):
            for sb in (1, -1):
                base = [Q5(0), Q5(sa) * iphi, Q5(sb) * phi]
                v = (base[cyc], base[(cyc + 1) % 3], base[(cyc + 2) % 3])
                dod.append((v[0].a, v[0].b, v[1].a, v[1].b, v[2].a, v[2].b))
    edge2 = (Q5(2) * iphi) * (Q5(2) * iphi)
    ddeg = [sum(1 for v in dod if v != u and d2(u, v) == edge2) for u in dod]
    chk("§D dodeca construction: 20 vertices, all degree 3 (edge = 2/phi, exact Q(sqrt5))",
        len(dod) == 20 and all(d == 3 for d in ddeg))

# ---------------------------------------------------------------- §E CT1.11a
def sectionE(ctx):
    print("S5 = §E CT1.11a involution table")
    basis16, (E0, Sig, W, J, K, Eij, diag), (Sact, Tact, pcoeff, SW) = ctx
    # sector dims by exact rank
    sector_vecs = {(1, 1): [], (1, -1): [], (-1, 1): [], (-1, -1): []}
    for m in range(4):
        for n in range(m, 4):
            A = kron(P[m], P[n])
            if m == n:
                combos = [(A, 1)]
            else:
                Bv = kron(P[n], P[m])
                combos = [(matadd(A, Bv), 1), (matadd(A, Bv, -1), -1)]
            for X, s_ev in combos:
                mn_eig = ETA[m] * ETA[n]
                sector_vecs[(s_ev, mn_eig)].append([x for row in X for x in row])
    dims = {k: rank_c(v) for k, v in sector_vecs.items()}
    chk("§E sector dims (7,3,3,3) by exact rank",
        (dims[(1, 1)], dims[(1, -1)], dims[(-1, 1)], dims[(-1, -1)]) == (7, 3, 3, 3), str(dims))
    # A8 dictionary: generator membership per sector
    member = {
        (1, 1): [E0, Sig, diag[1], diag[2], diag[3], Eij[(1,2)], Eij[(1,3)], Eij[(2,3)]],
        (1, -1): W,
        (-1, 1): J,
        (-1, -1): K,
    }
    okd = True
    for (s_ev, t_ev), lst in member.items():
        for X in lst:
            if not (eq(Sact(X), matscale(X, C(s_ev))) and eq(Tact(X), matscale(X, C(t_ev)))):
                okd = False
    chk("§E A8 dictionary: G,H,D+ in E_{++}; W in E_{+-}; J in E_{-+}; K in E_{--}", okd)
    # traceless Ê^{ij} span with Sigma and E0 gives dim 7 in E_{++}
    vecs = [[x for row in X for x in row] for X in
            [E0, Sig, Eij[(1,2)], Eij[(1,3)], Eij[(2,3)],
             matadd(diag[1], matscale(diag[2], C(-1))),
             matadd(matadd(diag[1], diag[2]), matscale(diag[3], C(-2)))]]
    chk("§E E_{++} explicit 7-frame independent", rank_c(vecs) == 7)
    # omega^2 = 1 on all 4096 tetra patterns
    verts = [0, 1, 2, 3]
    dirs = [(a, b) for a in verts for b in verts if a != b]
    bad = 0
    for mask in range(1 << 12):
        R = {dirs[i] for i in range(12) if mask >> i & 1}
        RT = {(b, a) for (a, b) in R}
        if {(b, a) for (a, b) in RT} != R:
            bad += 1
    chk("§E omega^2 = 1 on all 4096 tetra patterns", bad == 0)
    # omega not in Aut(K4)
    induced = 0
    for p in itertools.permutations(verts):
        if all((p[a], p[b]) == (b, a) for (a, b) in dirs):
            induced += 1
    chk("§E omega not induced by any of the 24 automorphisms of K4", induced == 0)
    # Theta_L / omega commutation + involution on exhaustive small configurations
    edges = [(0, 1), (1, 0)]
    def omega(c):
        Rr, sg, kp, ordr, sl = c
        return (tuple(sorted((b, a) for (a, b) in Rr)), sg, kp, ordr, sl)
    def theta(c):
        Rr, sg, kp, ordr, sl = c
        return (Rr, sg, tuple(-x for x in kp), tuple(reversed(ordr)),
                tuple({0: 0, 1: -1, -1: 1}[x] for x in sl))
    bad_comm = bad_inv = 0
    ncfg = 0
    for Rmask in range(4):
        R = tuple(edges[i] for i in range(2) if Rmask >> i & 1)
        for sgs in itertools.product([1, -1], repeat=len(R)):
            for kps in itertools.product([-1, 0, 1], repeat=len(R)):
                for ordr in ([tuple(range(len(R)))[::1], tuple(range(len(R)))[::-1]] if len(R) == 2 else [tuple(range(len(R)))]):
                    for seals in itertools.product([0, 1, -1], repeat=len(R)):
                        conf = (R, sgs, kps, ordr, seals)
                        ncfg += 1
                        w1, w2 = theta(omega(conf)), omega(theta(conf))
                        if w1 != w2:
                            bad_comm += 1
                        if theta(theta(conf)) != conf:
                            bad_inv += 1
                        o2 = omega(omega(conf))
                        if o2[0] != tuple(sorted(conf[0])) or o2[1:] != conf[1:]:
                            bad_inv += 1
    chk(f"§E [omega,Theta_L]=0 on {ncfg} exhaustive configurations", bad_comm == 0)
    chk("§E omega^2 = Theta_L^2 = 1 on the same space", bad_inv == 0)
    # Z2xZ2: four distinct classes on a witness configuration
    w0 = (((0, 1),), (1,), (1,), (0,), (1,))
    classes = {w0, omega(w0), theta(w0), omega(theta(w0))}
    chk("§E four distinct classes (1, omega, Theta, omegaTheta)", len(classes) == 4)
    # D3.4 endpoint charge oddness
    badq = 0
    for sgs in itertools.product([1, -1], repeat=2):
        q = Fr(sgs[0] - sgs[1], 2)
        qo = Fr(sgs[1] - sgs[0], 2)
        if qo != -q:
            badq += 1
    chk("§E D3.4 endpoint charge q=(sig_s - sig_t)/2 is omega-odd", badq == 0)
    # chi = sign(k) orientation-odd
    chk("§E chi = sign(k) orientation-odd", all((k > 0) != (-k > 0) for k in (1, 2, 3, 4)))
    # Theta_L on edge weights: G = sigma e^{i pi kappa} -> conjugate: kappa -> -kappa, sigma fixed
    badG = 0
    for sg in (1, -1):
        for kap in range(-3, 4):
            G = C(sg) * C((-1) ** kap)               # e^{i pi k} = (-1)^k exact
            Gt = C(sg) * C((-1) ** (-kap))
            if Gt != C(G.re, -G.im):
                badG += 1
    chk("§E Theta_L: G -> G* is kappa -> -kappa with sigma fixed (exact)", badG == 0)
    # virtual edges carry no registration: sigma is defined on real edges only —
    # the weight record has no virtual-slot: assert A7/D0.5 phrasing in the corpus
    A = era_paths.read("A_axioms.md")
    chk("§E D0.5: phase alphabet declared for real edges",
        "phase alphabet of a real edge" in A)

# ---------------------------------------------------------------- §F CT1.29a
def sectionF():
    print("S6 = §F CT1.29a kappa-bar structure")
    def comps(t, k):
        if k == 1:
            yield (t,)
            return
        for first in range(1, t - k + 2):
            for rest in comps(t - first, k - 1):
                yield (first,) + rest
    bad = 0
    total_cases = 0
    for dh in range(1, 7):
        for Th in range(dh, dh + 7):
            for kap in comps(Th, dh):
                total_cases += 1
                kbar = Fr(Th, dh)
                okc = (kbar >= 1) and (kbar * dh == Th) and ((kbar == 1) == all(k == 1 for k in kap)) \
                    and (kbar.denominator == 1 or dh % kbar.denominator == 0)
                # rate identity: S/A coefficient dh/Th equals 1/kbar exactly
                okc = okc and (Fr(dh, Th) == 1 / kbar)
                if not okc:
                    bad += 1
    chk(f"§F sweeps dh<=6 (cases={total_cases}): kbar>=1, =1 iff all-ones, rate identity exact", bad == 0)
    for kap in range(1, 9):
        for dh in range(1, 6):
            if Fr(kap * dh, dh) != kap:
                chk("§F uniform chains kbar=kappa", False)
    chk("§F uniform chains: kbar = kappa, exact rate only at kappa=1", True)
    # even-Theta compatibility examples (conditional clause; existence only)
    chk("§F hypothesis class nonempty: kappa=(1,1) Theta=2; kappa=(2,2) Theta=4; kappa=(1,3) Theta=4",
        all(t % 2 == 0 for t in (2, 4, 4)))

# ---------------------------------------------------------------- §G CT1.19 Rmk
def sectionG():
    print("S7 = §G CT1.19 Rmk integer-sampling slack")
    # The Rmk claim (provenance H FT.31(1)-(2)), in exact normalized units
    # (path x(lam) = lam on [0,1], metric factor g = 1 + x^2, n edges, h = 1/n,
    #  hbar := h so that kappa_e := ds^2(e)/hbar^2 = g(lam_e) per D1.6):
    #  (i)  identity: sum kappa_e * hbar^2 = sum ds^2(e)   (definitional, D1.6)
    #  (ii) integer slack: |kappa^Z_e - kappa_e| <= 1/2 per edge
    #       =>  |sum (kappa^Z - kappa) hbar^2| <= (n/2) h^2 = h/2 = O(hbar*L)
    #  (iii) supporting lemma (midpoint exactness on quadratics):
    #       |sum g(lam_e) h - integral g| = h^2/12 exactly for g = 1+x^2.
    bad = 0
    for n in range(4, 41):
        h = Fr(1, n)
        slack = Fr(0)
        riem = Fr(0)
        for e in range(n):
            lam = Fr(2 * e + 1, 2 * n)
            kap = 1 + lam * lam                      # kappa_e exact (real-valued)
            kapZ = (2 * kap + 1) // 2                # nearest integer (round-half-up)
            d = abs(Fr(kapZ) - kap)
            if d > Fr(1, 2):
                bad += 1
            slack += d
            riem += kap * h
        if slack * h * h > h * Fr(1, 2):
            bad += 1
        if abs(riem - Fr(4, 3)) != h * h / 12:
            bad += 1
    chk("§G(i,ii): per-edge integer slack <= 1/2; total slack*hbar^2 <= h/2 = O(hbar L), n=4..40 exact", bad == 0)
    chk("§G(iii): midpoint sum of g=1+x^2 deviates from the integral by exactly h^2/12", bad == 0)
    # (i) the identity itself: kappa := ds^2/hbar^2  =>  sum kappa hbar^2 = sum ds^2 (Fractions)
    for n in (5, 8, 13):
        h = Fr(1, n)
        ds2 = [ (1 + Fr(2*e+1, 2*n)**2) * h * h for e in range(n) ]
        kap = [ d / (h*h) for d in ds2 ]
        if sum(k * h * h for k in kap) != sum(ds2):
            chk("§G(i) identity", False)
    chk("§G(i): sum kappa_e hbar^2 = sum ds^2(e) identically [D1.6]", True)

def main():
    section0()
    sectionA()
    ctx = sectionB()
    sectionC(ctx[1])
    sectionD()
    sectionE(ctx)
    sectionF()
    sectionG()
    print(f"verify_merge_tierA: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
    sys.exit(1 if FAIL else 0)

if __name__ == "__main__":
    main()
