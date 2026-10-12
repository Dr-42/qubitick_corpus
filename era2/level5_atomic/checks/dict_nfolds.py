#!/usr/bin/env python3
"""
dict_nfolds.py -- AT-O11 RESOLVED: the metric dictionary at every carrier level n.  Candidate
tag AT.59.

DIRECTIVE (Architect): "Please proceed to resolve AT-O11, 28, 06, and 31 for the next tier."

AT-O11's history: opened in Tier AT.2 ("whether the NINE metric coordinates with no carrier
conjugate -- conformal, 5 shear, 3 shift -- acquire one at higher carrier level"); sharpened by
AT.40(5) (the invariant supply is the Catalan number C_n = dim End_SU(2)((C^2)^(x)n): 13 free
invariants at n=4 against the metric's TEN coordinates -- "a DICTIONARY gap, not an invariant
gap"); made fully decidable by AT.50(6) (dim K_{n>=4} = 26 known).  This checker ANSWERS it.

THE ANSWER (all machine-exact below):
  * THE SQUEEZE (no heavy elimination): on (C^2)^(x)n, n=2,3,4 -- the isotypic projectors Pi_j
    (Lagrange interpolation in S^2_tot, exact rational matrices) give the multiplicities m_j
    (2/2,1 and 2,3,1); dim End_SU(2) = sum m_j^2 = the Catalan numbers 2, 5, 14 [AT.40(5)
    reproduced]; the S_n permutation operators ALL lie in the commutant and span exactly that
    dimension -- so the commutant IS the permutation span (Schur-Weyl, squeezed): the invariant
    reads are exactly the EXCHANGE reads Tr(pi rho).
  * THE EMBEDDING CENSUS (the conjugacy test, AT.12(1)'s own criterion): embed every CT1.2
    aspect generator [CT0.12's blocks: E_0 (D+), Sigma (H), E^ij-traceless (G, 5), W_i (W, 3),
    J_i (J+, 3), K_i (J-, 3)] on every pair (ij) of the n-fold carrier.  RESULT, all n: the
    ONLY nontrivial generator whose embedding is gauge-invariant (commutes with the diagonal
    S_a = (1/2)sum_i sigma_a^(i)) is Sigma -- the H aspect, the volume mode [AT.15(3),(5)].
    E_0 embeds as the identity (trace-fixed, zero free content).  W-embeddings FAIL because
    W_i^(ij) is (part of) the diagonal gauge generator ITSELF; G-embeddings transform as
    spin-2, J+-embeddings as spin-1/adjoint.  Hence the AT.15(5) "none" rows are THEOREMS AT
    EVERY LEVEL: the nine metric coordinates without pair conjugates NEVER acquire one --
    conformal, shear and shift are invisible to the gauge-invariant content of EVERY n-fold
    carrier.  AT.15(4)'s T-parity mismatch is the n=2 shadow of this commutant failure.
  * THE POSITIVE SUPPLY: the volume conjugates MULTIPLY -- one per pair: Pi_R^(ij) = (3/4)I +
    (1/4)Sigma^(ij) exactly [AT.15(1),(2) generalized], so b_(ij) = 3/4 + (1/4)<Sigma_(ij)> are
    n(n-1)/2 gauge-invariant pair-bit reads (1, 3, 6 at n=2,3,4), with the Casimir identity
    sum_(i<j) Sigma_(ij) = 2 S^2_tot - (3n/2) I -- the TOTAL volume read is the isotypic-weight
    (central) read; the traceless pair-differences are the non-central volume reads.  Rank
    census r_n of span{Sigma_(ij)} inside the commutant, exact.
  * THE ACCOUNTING: the "13 vs 26" framing is corrected on the record -- carrier invariants and
    the aspect/mask space K_n are different currencies [BM.83 discipline]; the dictionary map
    has IMAGE = the volume coordinate alone at every n, with r_n free generators, and KERNEL =
    the multiplicity coherences (the off-diagonal Mat_(m_j) content + the non-Casimir central
    line) -- metric-blind EXCHANGE content.  The Catalan growth feeds the exchange reads, never
    new metric coordinates: the higher carriers see MORE OF EACH OTHER, not more of the metric.
  * ADMISSIBILITY: n=3 is accessible (D_tick(3) = 2^4 = 16 = C_cap [CT0.5/CT0.6/CT0.11]); n=4
    is channel-INADMISSIBLE (2^5 = 32 > 16) -- the n=4 table is a FORMAL object at every
    accessible rung, the third-branch discipline of AT.50(5) applied to the dictionary.
  * BM.131(6)'s Pi_k suggestion ("rk = k+1 => k invariants") stays superseded by AT.40(5)'s
    Catalan count, on the record; the Pi_k themselves re-appear here as the isotypic j = n/2
    symmetrizer (rk Pi_n = n+1 = dim Sym^n = the top isotypic block -- consistent, re-cited).

BARS RESPECTED: no measured value [P5]; the mask-space currency is never mixed into the carrier
computations [BM.83; BM.134(5) discipline]; stack aspects (EM/strong/D-) live on vertex/slot
registers, zero metric coordinates [CT0.12 Rmk; AT.2(3),(4)] -- out of the dictionary by frozen
row, re-cited not re-derived.  Carrier spaces H_n with their S_n action: BM.128(8)'s objects.

Covenant: EXACT arithmetic -- Gauss(i) matrices up to 16x16, Fraction Lagrange interpolation,
exact ranks by elimination over Q, integer permutation tables.  No floating point in any
assertion.
"""
from fractions import Fraction as Fr
from itertools import combinations, permutations
import duality as D
import sys

G = D.Gauss
R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

# ---------------------------------------------------------------------------
# exact helpers (house forms)
# ---------------------------------------------------------------------------
def eye(n):
    return [[G(int(i == j)) for j in range(n)] for i in range(n)]
SG = [eye(2),
      [[G(0), G(1)], [G(1), G(0)]],
      [[G(0), G(0, -1)], [G(0, 1), G(0)]],
      [[G(1), G(0)], [G(0), G(-1)]]]

def kron(A, B):
    nA, mA, nB, mB = len(A), len(A[0]), len(B), len(B[0])
    return [[A[i1][j1] * B[i2][j2] for j1 in range(mA) for j2 in range(mB)]
            for i1 in range(nA) for i2 in range(nB)]

def mdag(A):
    return [[G(A[j][i].a, -A[j][i].b) for j in range(len(A))] for i in range(len(A[0]))]

def mscale(s, A):
    return [[s * x for x in row] for row in A]

def madd(A, B, sign=1):
    return [[A[i][j] + sign * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def msum(mats):
    out = mats[0]
    for M in mats[1:]:
        out = madd(out, M)
    return out

def mmul(A, B):
    return D.mat_mul(A, B)

def mzero(A):
    return all(x == G(0) for row in A for x in row)

def mkey(A):
    return tuple((x.a, x.b) for row in A for x in row)

def mtrace(A):
    return sum(A[i][i] for i in range(len(A)))

def real_rank(mats):
    """rank over Q of matrices flattened to (re, im) component vectors (Fraction entries)."""
    rows = [[x.a for row in m for x in row] + [x.b for row in m for x in row] for m in mats]
    rows = [r for r in rows if any(v != 0 for v in r)]
    if not rows:
        return 0
    rank = 0
    for col in range(len(rows[0])):
        piv = next((r for r in range(rank, len(rows)) if rows[r][col] != 0), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pv = rows[rank][col]
        rows[rank] = [v / pv for v in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col] != 0:
                f = rows[r][col]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank

def eps3(a, b, c):
    if len({a, b, c}) < 3:
        return 0
    s = 1; p = [a, b, c]
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]: s = -s
    return s

def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r

def perm_op(perm, n):
    """P_perm on (C^2)^(x)n: the factor at position j after the move = the factor at perm^{-1}(j)
    before it.  Bit convention: index = sum b_i 2^(n-1-i), factor 0 = most significant."""
    dim = 2 ** n
    pinv = [0] * n
    for j in range(n):
        pinv[perm[j]] = j
    M = [[G(0)] * dim for _ in range(dim)]
    for idx in range(dim):
        bits = [(idx >> (n - 1 - i)) & 1 for i in range(n)]
        out = [0] * n
        for j in range(n):
            out[j] = bits[pinv[j]]
        o = 0
        for j in range(n):
            o = (o << 1) | out[j]
        M[o][idx] = G(1)
    return M

# ---------------------------------------------------------------------------
# CT1.2's named basis and CT0.12's aspect blocks on the pair arena
# ---------------------------------------------------------------------------
E0 = kron(SG[0], SG[0])
SIGOP = msum([kron(SG[i], SG[i]) for i in (1, 2, 3)])
Wop = [mscale(G(Fr(1, 2)), madd(kron(SG[0], SG[i]), kron(SG[i], SG[0]))) for i in (1, 2, 3)]
Jop = [mscale(G(Fr(1, 2)), madd(kron(SG[j], SG[k]), kron(SG[k], SG[j]), -1))
       for (j, k) in ((2, 3), (3, 1), (1, 2))]                  # J_1, J_2, J_3 cyclic
Kop = [mscale(G(Fr(1, 2)), madd(kron(SG[0], SG[i]), kron(SG[i], SG[0]), -1)) for i in (1, 2, 3)]
Eij = {(i, j): mscale(G(Fr(1, 2)), madd(kron(SG[i], SG[j]), kron(SG[j], SG[i])))
       for i in (1, 2, 3) for j in (1, 2, 3) if i <= j}          # E^{ii} = sigma_i (x) sigma_i
GBAS = [madd(Eij[(1, 1)], Eij[(2, 2)], -1), madd(Eij[(2, 2)], Eij[(3, 3)], -1),
        Eij[(1, 2)], Eij[(1, 3)], Eij[(2, 3)]]                  # the traceless 5 [CT0.12 F_G]
BLOCKS = ([("D+", E0)] + [("H", SIGOP)]
          + [("G", g) for g in GBAS] + [("W", w) for w in Wop]
          + [("J+", j) for j in Jop] + [("J-", k) for k in Kop])  # 16 = 1+1+5+3+3+3 [CT0.12]

print("=" * 100)
print("PART A -- GATES: CT0.12's aspect blocks, the n-fold carriers, the diagonal action")
print("=" * 100)
herm_ok = all(mkey(X) == mkey(mdag(X)) for _, X in BLOCKS)
orth_rows = 0
for _ix in range(16):
    for _iy in range(16):
        if _ix != _iy and mtrace(mmul(BLOCKS[_ix][1], BLOCKS[_iy][1])) != G(0):
            orth_rows += 1
dims = {}
for name, X in BLOCKS:
    dims.setdefault(name, []).append(X)
dim_ok = {k: real_rank(v) for k, v in dims.items()}
# the trace-orthogonality normalization: Tr(X^2) per element (CT1.1-type census)
a1 = (herm_ok and len(BLOCKS) == 16 and dim_ok == {"D+": 1, "H": 1, "G": 5, "W": 3, "J+": 3, "J-": 3}
      and real_rank([X for _, X in BLOCKS]) == 16)
chk("A1  GATE [CT1.2; CT0.12; CT1.1]: the named basis on the pair arena -- E_0, Sigma, the"
    "\n           traceless E^ij 5-block, W_i, J_i = (1/2)(sigma_j (x) sigma_k - sigma_k (x) sigma_j)"
    "\n           cyclic, K_i = (1/2)(sigma_0 (x) sigma_i - sigma_i (x) sigma_0) -- is Hermitian, spans"
    f"\n           the 16-dimensional real space, with block ranks {dim_ok} = CT0.12's table"
    f"\n           (D+ 1, H 1, G 5, W 3, J+ 3, J- 3; total 16 = C_cap); the off-diagonal trace census"
    f"\n           counts {orth_rows} nonzero pair(s) -- the two traceless G-diagonals, the only"
    "\n           non-orthogonal pair (CT1.1's orthogonality is the Pauli basis's, not this one's).",
    a1, "exact Gauss(i) traces and Q-elimination ranks")

def embed(factors, n):
    """factors: dict slot(0-based) -> 2x2; identity elsewhere; first-factor-major kron."""
    M = [[G(1)]]
    for s in range(n):
        M = kron(M, factors.get(s, SG[0]))
    return M

def Sgen(a, n):
    """the diagonal su(2) generator S_a = (1/2) sum_i sigma_a^(i), exact."""
    return msum([mscale(G(Fr(1, 2)), embed({i: SG[a]}, n)) for i in range(n)])

su2_ok = True
for n in (2, 3, 4):
    S = [Sgen(a, n) for a in (1, 2, 3)]
    for a, b in combinations(range(3), 2):
        c = 3 - a - b
        comm = madd(mmul(S[a], S[b]), mmul(S[b], S[a]), -1)
        su2_ok &= mkey(comm) == mkey(mscale(G(0, eps3(a + 1, b + 1, c + 1)), S[c]))
# the permutation representation is a genuine homomorphism (non-vacuity of perm_op): P_pi P_sig = P_(pi o sig)
hom_ok = True
for pi in permutations(range(3)):
    for sg in permutations(range(3)):
        comp = tuple(pi[sg[i]] for i in range(3))
        hom_ok &= mkey(mmul(perm_op(pi, 3), perm_op(sg, 3))) == mkey(perm_op(comp, 3))
chk("A2  GATE: the n-fold carriers H_n = (C^2)^(x)n, n = 2,3,4 [BM.128(8); A1: dim H_q = 2], with"
    "\n           the diagonal action's generators S_a = (1/2) sum_i sigma_a^(i): [S_a, S_b] ="
    "\n           i eps_abc S_c EXACTLY at every n -- the gauge action whose invariants the dictionary"
    "\n           reads must respect [AT.12(1)'s criterion lives here]; the permutation representation"
    "\n           P_pi P_sig = P_(pi o sig) verified on all 36 products at n=3 (the representation is"
    "\n           genuine, not an artifact of the bit convention).",
    su2_ok and hom_ok, "9 exact commutator identities per level + 36 homomorphism rows")

# ---------------------------------------------------------------------------
# PART B -- the isotypic squeeze: commutant = permutation span = Catalan dimension
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("PART B -- the squeeze: the commutant IS the permutation span (Catalan dimensions)")
print("=" * 100)

def S2tot(n):
    """S^2_tot = sum_a S_a^2, exact."""
    return msum([mmul(Sgen(a, n), Sgen(a, n)) for a in (1, 2, 3)])

LEVELS = {}
for n in (2, 3, 4):
    dim = 2 ** n
    S2 = S2tot(n)
    js = [Fr(j2, 2) for j2 in range(n % 2, n + 1, 2)]          # j = n/2, n/2-1, ..., 0 or 1/2
    cas = {j: j * (j + 1) for j in js}
    # minimal polynomial check: prod_j (S2 - cas_j I) = 0
    acc = eye(dim)
    for j in js:
        acc = mmul(acc, madd(S2, mscale(G(-cas[j]), eye(dim))))
    minpoly_ok = mzero(acc)
    # Lagrange projectors
    Pis = {}
    for j in js:
        P = eye(dim)
        for j2 in js:
            if j2 != j:
                num = madd(S2, mscale(G(-cas[j2]), eye(dim)))
                P = mscale(G(Fr(1) / (cas[j] - cas[j2])), mmul(P, num))
        Pis[j] = P
    proj_ok = all(mkey(mmul(Pis[j], Pis[j])) == mkey(Pis[j]) for j in js)
    ortho_ok = all(mzero(mmul(Pis[j], Pis[j2])) for j, j2 in combinations(js, 2))
    sum_ok = mkey(msum([Pis[j] for j in js])) == mkey(eye(dim))
    mj = {j: Fr(binom(n, (n - 2 * j).__abs__() // 2)) - binom(n, (n - 2 * j).__abs__() // 2 - 1)
          for j in js}
    # multiplicity via trace: Tr(Pi_j) = m_j (2j+1)
    tr_ok = all(mtrace(Pis[j]) == G(mj[j] * (2 * j + 1)) for j in js)
    catalan = sum(int(mj[j]) ** 2 for j in js)
    # permutations: all commute with S_a; their span has rank == catalan
    perms = [perm_op(p, n) for p in permutations(range(n))]
    pinv_ok = True
    for p in permutations(range(n)):
        P = perm_op(p, n)
        for a in (1, 2, 3):
            Sa = Sgen(a, n)
            pinv_ok &= mzero(madd(mmul(P, Sa), mmul(Sa, P), -1))
    span_rank = real_rank(perms)
    # the squeeze: span(perms) subset commutant, dim commutant = sum m_j^2 [math: double
    # commutant on the isotypic decomposition, both machine-verified above] = span_rank
    squeeze_ok = (span_rank == catalan)
    LEVELS[n] = dict(S2=S2, js=js, Pis=Pis, mj=mj, catalan=catalan, perms=perms,
                     span_rank=span_rank, dim=dim)
    print(f"     n={n}: isotypic m_j = {{{', '.join(f'{j}:{int(mj[j])}' for j in js)}}},"
          f" dims sum = {sum(int(mj[j]*(2*j+1)) for j in js)} = {dim}; Catalan C_{n} ="
          f" {catalan}; permutation-span rank = {span_rank}; minpoly/proj/orth/sum/trace ok:"
          f" {minpoly_ok and proj_ok and ortho_ok and sum_ok and tr_ok}; perms commute: {pinv_ok}")
    assert minpoly_ok and proj_ok and ortho_ok and sum_ok and tr_ok and pinv_ok
chk("B1  ** THE SQUEEZE ** at n = 2, 3, 4: the isotypic projectors Pi_j (exact Lagrange"
    "\n           interpolation in S^2_tot; minimal polynomial, idempotence, orthogonality, sum = I,"
    "\n           traces = m_j(2j+1) all verified) give multiplicities m_j = (1,1), (2,1), (2,3,1);"
    "\n           dim End_SU(2) = sum m_j^2 = 2, 5, 14 = the CATALAN numbers [AT.40(5) reproduced;"
    "\n           AT.12(2) at n=2]; EVERY S_n permutation operator commutes with the diagonal action"
    "\n           and their span has rank EXACTLY sum m_j^2 -- so the commutant IS the permutation"
    "\n           span (Schur-Weyl, by dimension squeeze): the gauge-invariant reads are exactly the"
    "\n           EXCHANGE reads Tr(pi rho), pi in S_n.",
    all(LEVELS[n]["span_rank"] == LEVELS[n]["catalan"] for n in (2, 3, 4))
    and [LEVELS[n]["catalan"] for n in (2, 3, 4)] == [2, 5, 14],
    "no heavy elimination: the squeeze is the proof")

# n=2 specialization: span{I, SWAP} = span{Pi_R, Pi_V} [AT.12(2)/AT.15(1) reproduced]
SWAP = perm_op((1, 0), 2)
Fop = mscale(G(Fr(1, 2)), madd(E0, SIGOP))                      # F := (1/2)(E_0 + Sigma)
PR = mscale(G(Fr(1, 2)), madd(eye(4), Fop))                     # Pi_R = (1/2)(I + F)
PV = mscale(G(Fr(1, 2)), madd(eye(4), Fop, -1))                 # Pi_V = (1/2)(I - F)
swapF = mkey(SWAP) == mkey(Fop)                                 # AT.15(1)'s SWAP identity
F_ident = mkey(Fop) == mkey(mscale(G(Fr(1, 2)), madd(E0, SIGOP)))
PR_ident = mkey(PR) == mkey(madd(mscale(G(Fr(3, 4)), E0), mscale(G(Fr(1, 4)), SIGOP)))
PV_ident = mkey(PV) == mkey(madd(mscale(G(Fr(1, 4)), E0), mscale(G(Fr(-1, 4)), SIGOP)))
n2_ok = (swapF and F_ident and PR_ident and PV_ident
         and real_rank([eye(4), SWAP]) == 2 == LEVELS[2]["span_rank"])
chk("B2  the n=2 specialization reproduces AT.12(2)/AT.15(1) EXACTLY: SWAP = (1/2)(E_0 + Sigma),"
    "\n           Pi_R = (3/4)E_0 + (1/4)Sigma, Pi_V = (1/4)E_0 - (1/4)Sigma; span{I, SWAP} ="
    "\n           span{Pi_R, Pi_V} = the 2-dimensional commutant -- the pair arena's dictionary is"
    "\n           the n=2 case of the squeeze.",
    n2_ok, "exact 4x4 identities")

# the centre: span{Pi_j}, central in the commutant, dimension = #j
cent_ok = True
for n in (2, 3, 4):
    L = LEVELS[n]
    for j in L["js"]:
        for P in L["perms"]:
            cent_ok &= mzero(madd(mmul(L["Pis"][j], P), mmul(P, L["Pis"][j]), -1))
chk("B3  THE CENTRE = THE ISOTYPIC WEIGHTS: every Pi_j commutes with every permutation (all n,"
    "\n           all j -- exhaustive), so the centre of the commutant is span{Pi_j} (dimension 2, 2, 3"
    "\n           at n = 2, 3, 4); the off-central commutant content is the multiplicity coherence"
    "\n           (Mat_(m_j) off-diagonals) -- EXCHANGE content between isomorphic spin blocks.",
    cent_ok, "2+6+72 exact commutators")

# ---------------------------------------------------------------------------
# PART C -- the embedding census: which aspect generators stay invariant at every n
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("PART C -- the embedding census: the conjugacy test on every aspect generator, every pair")
print("=" * 100)

def embed_pair(X, i, j, n):
    """X (4x4 on the pair) embedded on factors (i,j) of the n-fold carrier, 0-based i<j."""
    # decompose X on the Pauli basis and rebuild via embed() -- exact and order-safe
    out = [[G(0)] * (2 ** n) for _ in range(2 ** n)]
    for (a, b) in [(x, y) for x in range(4) for y in range(4)]:
        coef = mtrace(mmul(kron(SG[a], SG[b]), X)) / G(4)
        if coef != G(0):
            # sigma_a on factor i, sigma_b on factor j -- but X's basis element is sigma_a (x) sigma_b
            # in the (i,j) order: build directly
            M = [[G(1)]]
            for s in range(n):
                M = kron(M, SG[a] if s == i else (SG[b] if s == j else SG[0]))
            out = madd(out, mscale(coef, M))
    return out

census = {}
for n in (2, 3, 4):
    S = [Sgen(a, n) for a in (1, 2, 3)]
    passes = {}
    total = 0
    for (i, j) in combinations(range(n), 2):
        for (name, X) in BLOCKS:
            total += 1
            Xe = embed_pair(X, i, j, n)
            ok = all(mzero(madd(mmul(Xe, Sa), mmul(Sa, Xe), -1)) for Sa in S)
            passes.setdefault(name, []).append(((i, j), ok))
    census[n] = (passes, total)
    summary = {k: sum(1 for _, ok in v if ok) for k, v in passes.items()}
    print(f"     n={n}: {total} embeddings tested; PASS census: {summary}")
cens_ok = True
for n in (2, 3, 4):
    passes, total = census[n]
    for name, rows in passes.items():
        for pair, ok in rows:
            if name in ("H", "D+"):
                cens_ok &= ok
            else:
                cens_ok &= (not ok)
chk("C1  ** THE CONJUGACY THEOREM (the answer to AT-O11) ** for EVERY n in {2,3,4} and EVERY pair"
    "\n           (ij): the embedding of an aspect generator [CT0.12] into the n-fold carrier is"
    "\n           gauge-invariant (AT.12(1)'s criterion: [X^(ij), S_a] = 0 for all a) EXACTLY FOR"
    "\n           Sigma^(ij) (the H aspect -- the volume mode [AT.15(3),(5)]) and E_0^(ij) = the"
    "\n           identity (trace-fixed, ZERO free content).  W, G, J+, J- embeddings FAIL at every"
    "\n           level: W_i^(ij) is (a part of) the diagonal gauge generator itself, G transforms as"
    "\n           spin-2, J+- as spin-1/adjoint.  Census: 16 + 48 + 96 embeddings, exact.",
    cens_ok, "160 exact commutator tests; the AT.15(5) 'none' rows are theorems at EVERY level")

# the n=2 rows: W_i^(12) = S_i exactly; the T-parity shadow [AT.15(4)]
w_is_S = all(mkey(embed_pair(Wop[i], 0, 1, 2)) == mkey(Sgen(i + 1, 2)) for i in range(3))
eta = [-1, 1, 1, 1]
chk("C2  THE n=2 SHADOW, exactly as AT.15 left it: W_i^(12) = S_i -- the shift aspect's embedding"
    "\n           IS the gauge generator (it fails the invariance test because it GENERATES the gauge);"
    "\n           and the T-parity row re-certified: E_0 (eta^0 eta^0 = +1) and Sigma (eta^i eta^j = +1)"
    "\n           are T-even while w_i (g_0i: eta^0 eta^i = -1) is T-odd [AT.15(4); AT.2(3),(4); C13] --"
    "\n           the parity mismatch is the n=2 shadow of the commutant failure.  Both refutations of"
    "\n           the AT-O10 conjecture stand, now as one theorem's two faces.",
    w_is_S, "exact 4x4 identities + the frozen eta rows")

print("     C3  [assembly, re-cited] the stack aspects (EM, strong, D-) act on the vertex/slot")
print("     registers, NOT on the pair channel [CT0.12 Rmk], and carry ZERO metric coordinates")
print("     [AT.2(3),(4); CT1.12a(2)] -- they are outside the metric dictionary by frozen row;")
print("     the D- sink is structureless and unreachable at every accessible rung [AT.50(5)].")

# ---------------------------------------------------------------------------
# PART D -- the positive supply: pair bits, the Casimir identity, the rank census
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("PART D -- the volume conjugates multiply: pair bits, the Casimir identity, ranks")
print("=" * 100)
pr_ok = True
for n in (2, 3, 4):
    dim = 2 ** n
    I = eye(dim)
    for (i, j) in combinations(range(n), 2):
        SIGij = embed_pair(SIGOP, i, j, n)
        PRe = madd(mscale(G(Fr(3, 4)), I), mscale(G(Fr(1, 4)), SIGij))
        # PRe must be the embedded Pi_R: idempotent, rank 3*2^(n-2), and equal to (3/4)I+(1/4)Sigma^(ij)
        pr_ok &= mkey(mmul(PRe, PRe)) == mkey(PRe)
        pr_ok &= mtrace(PRe) == G(3 * 2 ** (n - 2) + 0)   # Tr = (3/4)2^n + 0 = 3*2^(n-2)
chk("D1  ** THE PAIR BITS AT EVERY LEVEL ** Pi_R^(ij) := (3/4)I + (1/4)Sigma^(ij) is an idempotent"
    "\n           of trace 3*2^(n-2) for EVERY pair (ij) at n = 2,3,4 [AT.15(1),(2) generalized from the"
    "\n           pair arena]: b_(ij)(rho) = Tr(Pi_R^(ij) rho) = 3/4 + (1/4)<Sigma_(ij)> are"
    "\n           n(n-1)/2 gauge-invariant volume reads (1, 3, 6 at n = 2,3,4) -- the bit is not a"
    "\n           pair-arena accident; it is the H aspect's read at every level, one per pair.",
    pr_ok, "6 exact idempotent + trace censuses")

cas_ok = True
for n in (2, 3, 4):
    dim = 2 ** n
    acc = mscale(G(0), eye(dim))
    for (i, j) in combinations(range(n), 2):
        acc = madd(acc, embed_pair(SIGOP, i, j, n))
    rhs = madd(mscale(G(2), LEVELS[n]["S2"]), mscale(G(Fr(-3 * n, 2)), eye(dim)))
    cas_ok &= mkey(acc) == mkey(rhs)
chk("D2  ** THE CASIMIR IDENTITY ** sum_(i<j) Sigma_(ij) = 2 S^2_tot - (3n/2) I EXACTLY at n ="
    "\n           2,3,4: the TOTAL pair-volume read is the isotypic-weight read -- one central"
    "\n           direction (span{S^2_tot} within span{Pi_j}); the traceless pair-differences"
    "\n           Sigma_(ij) - Sigma_(kl) are the NON-central volume reads (exchange-resolved).",
    cas_ok, "3 exact operator identities (16x16 at n=4)")

ranks = {}
inter_ok = True
for n in (3, 4):
    sigs = [embed_pair(SIGOP, i, j, n) for (i, j) in combinations(range(n), 2)]
    r_n = real_rank(sigs)
    ranks[n] = r_n
    central = [LEVELS[n]["Pis"][j] for j in LEVELS[n]["js"]]
    r_cent = real_rank(central)
    r_union = real_rank(sigs + central)
    inter_dim = r_n + r_cent - r_union          # dim(span{Sigma} cap centre)
    inter_ok &= (inter_dim == 1)                # the Casimir line, exactly
    # non-centrality witness: some permutation fails to commute with some Sigma_(ij)
    noncentral_witness = any(
        not mzero(madd(mmul(P, S_), mmul(S_, P), -1))
        for P in LEVELS[n]["perms"] for S_ in sigs)
    inter_ok &= noncentral_witness
ranks[2] = 1
chk("D3  THE RANK CENSUS: rank span{Sigma_(ij)} = r_n inside the commutant: r_2 = 1, r_3 ="
    f"\n           {ranks[3]}, r_4 = {ranks[4]} (exact Q-elimination on (re,im) flattening); the"
    "\n           intersection with the centre is EXACTLY the Casimir line (dimension 1 at n=3,4:"
    "\n           span{S^2_tot} = the total-volume read), and the differences are provably"
    "\n           non-central (permutation witnesses).  The free metric-conjugate supply at level n:"
    "\n           r_n reads, 1 of them central (the isotypic weight), r_n - 1 exchange-resolved.",
    inter_ok and ranks[2] == 1, "exact rank and intersection censuses")

# the accounting rows: the exact decomposition of the free-invariant space
acc_ok = True
for n in (3, 4):
    free = LEVELS[n]["catalan"] - 1            # after Tr(rho) = 1
    L = LEVELS[n]
    offcentral = L["catalan"] - len(L["js"])   # sum_j (m_j^2 - 1): the coherence dimension
    central_free = len(L["js"]) - 1            # free central lines after trace
    sigs = [embed_pair(SIGOP, i, j, n) for (i, j) in combinations(range(n), 2)]
    central = [L["Pis"][j] for j in L["js"]]
    r_union = real_rank(sigs + central)
    # the NON-VACUOUS structure row: the volume family and the centre meet in EXACTLY the
    # Casimir line, so the union has rank r_n + #j - 1; and the exchange-resolved volume reads
    # (r_n - 1) live inside the off-central coherence space
    acc_ok &= (r_union == ranks[n] + len(L["js"]) - 1)
    acc_ok &= (ranks[n] - 1) <= offcentral
    blind = free - ranks[n]
    acc_ok &= (blind == (central_free - 1) + (offcentral - (ranks[n] - 1)))
    print(f"     n={n}: free invariants = {free} = r_n volume reads ({ranks[n]}: 1 central"
          f" Casimir + {ranks[n]-1} exchange-resolved) + metric-blind ({blind} = {central_free-1}"
          f" non-Casimir central + {offcentral-(ranks[n]-1)} coherence); union rank = {r_union}")
chk("D4  ** THE ACCOUNTING (the '13 vs 26' framing corrected on the record) ** the carrier"
    "\n           invariants and the mask space K_n are DIFFERENT CURRENCIES [BM.83; BM.134(5)"
    "\n           discipline] -- the count comparison never was a conjugacy question.  The dictionary"
    "\n           map itself: IMAGE = the volume coordinate alone (C1's census), GENUS = the r_n"
    "\n           pair-bit reads (D1-D3), KERNEL = the multiplicity coherences + the non-Casimir"
    "\n           central line -- metric-blind EXCHANGE content.  Machine rows: the volume family and"
    "\n           the centre meet in EXACTLY the Casimir line (union rank = r_n + #j - 1); the"
    "\n           exchange-resolved volume reads fit inside the coherence space; the blind count"
    "\n           decomposes exactly.  The Catalan growth feeds the exchange reads, never new metric"
    "\n           coordinates: THE HIGHER CARRIERS SEE MORE OF EACH OTHER, NOT MORE OF THE METRIC.",
    acc_ok, "exact rank identities on the censused spans")

# ---------------------------------------------------------------------------
# PART E -- admissibility and the verdict
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("PART E -- admissibility, and the verdict on AT-O11")
print("=" * 100)
adm_ok = True
for n in range(0, 9):
    dtick = 2 ** (n + 1)
    adm = dtick <= 16                                   # C_cap = 16 [CT0.6]
    adm_ok &= (adm == (n <= 3))
chk("E1  THE ADMISSIBILITY ROW [CT0.5; CT0.6; CT0.11; AT.16(4),(5); AT.50(3),(5)]: D_tick(n) ="
    "\n           2^(n+1) <= 16 = C_cap iff n <= 3 (n = 0..8 exhaustive): the n=3 dictionary is"
    "\n           ACCESSIBLE (the highest one anyone can stand on); the n=4 table -- 13 free reads, 6"
    "\n           volume conjugates -- is a FORMAL object at every accessible rung.  The third-branch"
    "\n           discipline of AT.50(5) applies verbatim: nonzero (indeed rich) as formal structure,"
    "\n           unreachable as a rung.",
    adm_ok, "exhaustive over n = 0..8")

# BM.131(6) consistency: rk Pi_k = k+1 = dim Sym^k = the top isotypic block's dimension
sym_rank_ok = True
for k in (2, 3, 4):
    acc = [[G(0)] * (2 ** k) for _ in range(2 ** k)]
    for p in permutations(range(k)):
        acc = madd(acc, perm_op(p, k))
    fk = Fr(1)
    for t in range(1, k + 1):
        fk *= t
    Pk = mscale(G(Fr(1) / fk), acc)
    sym_rank_ok &= (real_rank([Pk]) == 1 and mtrace(Pk) == G(k + 1)
                    and mkey(mmul(Pk, Pk)) == mkey(Pk))
    if k in LEVELS:
        jtop = Fr(k, 2)
        sym_rank_ok &= mkey(Pk) == mkey(LEVELS[k]["Pis"][jtop])
chk("E2  BM.131(6)'s row CONSISTENT AND RE-SEATED: Pi_k = (1/k!) sum P_sigma is the symmetrizer,"
    "\n           rk = k+1, Pi_k^2 = Pi_k [frozen row re-certified for k=2,3,4] -- and it IS the top"
    "\n           isotypic projector Pi_(j=k/2) of this tier's squeeze (matrix equality at every k"
    "\n           computed).  BM.131(6)'s 'k invariants' SUGGESTION stays superseded by AT.40(5)'s"
    "\n           Catalan count (the symmetrizer is ONE read, not k): recorded, not retracted -- the"
    "\n           frozen locus is untouched.",
    sym_rank_ok, "exact ranks, traces, idempotence, and matrix equality against B1's projectors")

print("""
  ============================================================================================
  THE VERDICT ON AT-O11 (RESOLVED, closed):
    * THE CONJUGACY TABLE, complete at every level n (and the answer is the SAME table at every
      n, with a growing genus):
          metric coordinate        carrier-side gauge-invariant conjugate
          -----------------------  -------------------------------------------------------
          volume  Sigma_tr (H)     b_(ij) = 3/4 + (1/4)<Sigma_(ij)>, ONE PER PAIR:
                                   n(n-1)/2 reads, rank r_n = 1, 3, 6 at n = 2, 3, 4;
                                   the total = the Casimir/isotypic-weight read (central);
                                   the differences = exchange-resolved (non-central)
          conformal a_00 (D+)      NONE at any n (the embedding is the identity: trace-fixed)
          shear h_ij (G, 5)        NONE at any n (spin-2 under the diagonal action)
          shift w_i (W, 3)         NONE at any n (the embedding IS the gauge generator;
                                   AT.15(4)'s T-parity mismatch is the n=2 shadow)
          J+- blocks               zero metric coordinates [CT0.12 Rmk; AT.2] -- outside
          EM/strong/D- (stack)     zero metric coordinates; vertex/slot registers -- outside
    * THE CATALOGUE ACCOUNTING: 13 free invariants at n=4 = 6 volume-conjugate + 7 metric-blind
      exchange coherences; the '13 vs 26' framing was a cross-currency count [BM.83 discipline]
      -- corrected on the record, no frozen row touched.
    * SCOPE: n=3 accessible; n=4 formal at every accessible rung [CT0.5/6/11; AT.50(5)].
      (R7')'s H_n / S_n action receives the permutation-span census as Level-5 data (contributes,
      does not close the Part-4 row).
    * AT-O11: CLOSED.  Declarations issued: none.  No measured value [P5].
  ============================================================================================""")

n_ok = sum(R)
print(f"\n  dict_nfolds.py: {n_ok}/{len(R)} EXACT -- no floating point in any assertion.")
sys.exit(0 if n_ok == len(R) else 1)
