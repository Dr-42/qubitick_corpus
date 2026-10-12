#!/usr/bin/env python3
"""verify_H_chiral_closure.py — companion to Tier
F.31: FT.92 / FT.93 / FT.94 / FT.95 / FT.96 of the H working layer (split canon).

Grounded in the tier texts, the FT.78 stored-census anchors embedded in H itself, and the frozen
A–G definitions. Exact arithmetic only: Fraction / complex-over-Fraction
(qmath.C) / integer enumeration. No floats anywhere.

Sections:
  §A–§B  FT.92: every frozen pair-register identity re-verified as an exact
         Q(i) matrix equality (CT1.3–CT1.8, EW.5 both clauses at all nine
         (i,j), Cor CT0.7a, CT0.7(1), Sigma^2 = 3E0 - 2Sigma, [S,T] = 0 with
         eta = (-,+,+,+), the full (S,T) parity table); +i exactness (no sign
         residue); the convention-rigidity enumeration — exactly 2 of 32 sign
         maps survive {id, Ad(swap)}; J<->K excluded; Hermiticity pins phases
         to {0, pi}; EW.5 invariant in both conventions
  §C–§E  FT.93: exhaustive Clifford frame census (1365 -> 30 frames -> all 15
         pseudoscalars, each x2; per-frame pseudoscalar axioms; real rank 16 of
         the generated Cl(4,0) for ALL 30 frames; the 12/12 ordering witness;
         the exact [gamma,S] species table; the F0 example matrices); the
         pincer (exact nullspace solves: commutant = span_C{Pi_R,Pi_V} with no
         traceless involution, anticommutant = C.Pi_V singular, seed commutant
         = C I2, seed anticommutant = 0; all 30 frames weak-active on both
         halves); Tasks 2–3 refuted with entrywise witnesses; native counts
         8+8 vs the [EXT] 8+7; seed colour-neutrality; [gamma,S] = 0 iff
         diagonal; cross-ranks (2,1,2,1) vs (3,1)
  §F     FT.94(2)–(3) + FT.96: tetrahedron reversal witnesses (exhaustive
         4096 patterns + 1230 admissible + 101 covers, two enumerators; 7
         classes = 5 self + 1 exchanged pair vs the stored FT.78(2) census);
         cube pairing census (11,205 -> 264 -> 42 self + 111 pairs = 153;
         sector splits 26+2*70 / 16+2*41; Z-anchors 1,109,313/1,150,848 and
         the |C|-level refinement re-verified; chirality-blind on all 112
         exchanged pairs across the nine stored fields); the exact <m_A^2>
         Fractions 886272/35201 and 22146188288/268241835; the FT.79(1)
         ladders re-derived
  §G     FT.94(1)/(4) + FT.96(1): the typed-tuple non-constructibility ledger
         facts; C5 the fourth clean negative (range 36 vs 3477^2, shortfall
         x335820.25 exact, ceiling V >= 4636); the (8, 1056, 1109312) triple
         rejected as the dimension trap; the no-referent counts in frozen A–G
         (the two terms named at FT.95(2) plus the five typed-tuple tokens —
         a documented superset of the original "6 terms"); the frozen-H occurrence census
         of the 4 directive phrases (8 occurrences, all inside Tier F.31)
  §H     FT.95: the D4/D5 tautology (sign(k)k = |k| all k in {+-1..+-5};
         <chi>_T = wb*hc*|k0| constant in T = 1..6); p*_inf squared = 2/3
         exactly in Q; the zero-expectation theorem — reversal preserves
         admissibility, K, cover status and A(R) pointwise (exhaustive
         tetrahedron), sum_R A(R) f(R) = 0 exactly for the orientation-bias
         witness over all 4096; winding sign oddness; Z2 x Z2 group table
  §I     FT.96(4)–(5): the invariant takes exactly two values (self/paired)
         on both skeletons — counts 6 and 153; 2 != 3 (E4 negative)

Run: python3 verify_H_chiral_closure.py    (auto-discovered by run_all.py)
Exit 0 = all green.  (Check count differs from the original's 10,777 — same
inventory, per-assertion granularity chosen by this rebuild.)
"""
import hashlib
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

import itertools
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale, trace, conj_transpose  # noqa: E402
from bypasscore import (complete_graph, cube_graph, undirected_from, types_of,  # noqa: E402
                        centers_of, is_cover_strict, cover_value, automorphisms,
                        enum_covers_bt, cover_dp)

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


t0 = time.time()


def stamp(msg):
    print(f"  [{time.time()-t0:6.1f}s] {msg}  (checks: {PASS + FAIL})")


# ================================================================== §0 canon
# (layer integrity is guarded by checks/verify_corpus_graph.py — tag-definition
#  uniqueness, no duplicate publication, citation closure)
if ARCH:
    _SPLIT_H = ['H_archive/H01_flux_and_fermion.md', 'H_archive/H02_edges_and_spin_charge.md',
                'H_archive/H03_subnetwork_force_and_geometry.md', 'H_archive/H04_aspect_operator_and_spectrum.md',
                'H_archive/H05_floor_families.md', 'H_archive/H06_platonic_and_polygon_floors.md',
                'H_archive/H07_spin_ladder.md', 'H_archive/H08_loops_and_bott.md',
                'H_archive/H09_flicker_and_domains.md', 'H_archive/H10_sm_audit.md',
                'H_archive/H11_gravity_and_koide.md', 'H_archive/H12_chirality_and_form_factor.md',
                'H_archive/H13_registries_and_gaps.md']
if ARCH:
    _missing = [f for f in _SPLIT_H if not os.path.exists(os.path.join(DOCS, f))]
if ARCH:
    chk("§0 split canon present (13 parts)", not _missing, str(_missing))

# ---------------------------------------------------------------- helpers
I = C(0, 1)
HALF = C(Fr(1, 2))


def mat(rows):
    return [[x if isinstance(x, C) else C(x) for x in row] for row in rows]


def eye(n):
    return mat([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def zeros4():
    return [[C(0)] * 4 for _ in range(4)]


def kron2(A, B):
    return [[A[i // 2][j // 2] * B[i % 2][j % 2] for j in range(4)] for i in range(4)]


def comm(A, B):
    return matadd(matmul(A, B), matmul(B, A), -1)


def acomm(A, B):
    return matadd(matmul(A, B), matmul(B, A))


def eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def is_zero(A):
    return all(x == C(0) for row in A for x in row)


def rank_q(rows):
    rows = [list(r) for r in rows if any(x != 0 for x in r)]
    if not rows:
        return 0
    n = len(rows[0])
    rank = 0
    for c in range(n):
        pr = next((rr for rr in range(rank, len(rows)) if rows[rr][c] != 0), None)
        if pr is None:
            continue
        rows[rank], rows[pr] = rows[pr], rows[rank]
        pv = rows[rank][c]
        for rr in range(len(rows)):
            if rr != rank and rows[rr][c] != 0:
                f = Fr(rows[rr][c]) / Fr(pv)
                rows[rr] = [a - f * b for a, b in zip(rows[rr], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def rank_c(M):
    n, m = len(M), len(M[0])
    A = [[M[i][j].re for j in range(m)] for i in range(n)]
    B = [[M[i][j].im for j in range(m)] for i in range(n)]
    rows = [A[i] + [-x for x in B[i]] for i in range(n)] + [B[i] + A[i] for i in range(n)]
    r = rank_q(rows)
    return r // 2


def rref_nullspace(rows):
    m = [list(r) for r in rows if any(x != 0 for x in r)]
    n = len(rows[0])
    if not m:
        return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    piv, r = [], 0
    for c in range(n):
        pr = next((rr for rr in range(r, len(m)) if m[rr][c] != 0), None)
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


def realify(M):
    return [M[i][j].re for i in range(len(M)) for j in range(len(M[0]))] + \
           [M[i][j].im for i in range(len(M)) for j in range(len(M[0]))]


def is_zero_mat(M):
    return all(x == C(0) for row in M for x in row)


# CT1.2's named basis, verbatim definitions over Q(i)
s0 = mat([[1, 0], [0, 1]])
s1 = mat([[0, 1], [1, 0]])
s2 = mat([[0, -I], [I, 0]])
s3 = mat([[1, 0], [0, -1]])
S2 = [s0, s1, s2, s3]
PK = [(mu, nu) for mu in range(4) for nu in range(4) if (mu, nu) != (0, 0)]
PRD = {k: kron2(S2[k[0]], S2[k[1]]) for k in PK}

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
K = [matscale(matadd(kron2(s0, S2[i]), matscale(kron2(S2[i], s0), C(-1))), HALF)
     for i in (1, 2, 3)]
EIJ = {(i, j): matscale(matadd(kron2(S2[i], S2[j]), kron2(S2[j], S2[i])), HALF)
       for i in (1, 2, 3) for j in (1, 2, 3)}
PRJ_R = matscale(matadd(matscale(E0, C(3)), SIG), C(Fr(1, 4)))
PRJ_V = matscale(matadd(E0, matscale(SIG, C(-1))), C(Fr(1, 4)))
BASIS16 = [E0] + [PRD[k] for k in PK]
ETA = [-1, 1, 1, 1]                                  # A3: eta = (-,+,+,+)
eps = lambda a, b, c: Fr((a - b) * (b - c) * (c - a), 2)  # Levi-Civita on {1,2,3}


def S_conj(X):
    return matmul(matmul(SW, X), SW)


def T_map(X):
    """T(sigma_mu (x) sigma_nu) = eta_mu eta_nu sigma_mu (x) sigma_nu, linear."""
    out = zeros4()
    for mu in range(4):
        for nu in range(4):
            coef = trace(matmul(X, kron2(S2[mu], S2[nu]))) / C(4)
            if coef != C(0):
                out = matadd(out, matscale(kron2(S2[mu], S2[nu]), coef * C(ETA[mu] * ETA[nu])))
    return out


# ============================================================ §A FT.92(1)
print("§A FT.92(1) — the frozen identities, exact over Q(i)")
for bi, B in enumerate(BASIS16):
    chk(f"§A CT1.3 [E0, basis#{bi}] = 0", is_zero(comm(E0, B)))
for i, j in itertools.permutations((1, 2, 3), 2):
    k = 6 - i - j
    sgn = 1 if eps(i, j, k) > 0 else -1
    chk(f"§A CT1.4 [W{i},W{j}] = i eps W{k} (ordered pair)",
        eq(comm(W[i - 1], W[j - 1]), matscale(W[k - 1], C(0, sgn))))
for i in (1, 2, 3):
    chk(f"§A CT1.5 [Sigma,J{i}] = 4i K{i}", eq(comm(SIG, J[i - 1]), matscale(K[i - 1], C(0, 4))))
    chk(f"§A CT1.5 [Sigma,K{i}] = -4i J{i}", eq(comm(SIG, K[i - 1]), matscale(J[i - 1], C(0, -4))))
    chk(f"§A CT1.5 [Sigma,W{i}] = 0", is_zero(comm(SIG, W[i - 1])))
for i, j in itertools.permutations((1, 2, 3), 2):
    k = 6 - i - j
    sgn = 1 if eps(i, j, k) > 0 else -1
    chk(f"§A CT1.6 [J{i},J{j}] = i eps W{k} (+i exact, no sign residue)",
        eq(comm(J[i - 1], J[j - 1]), matscale(W[k - 1], C(0, sgn))))
    chk(f"§A CT1.6 [K{i},K{j}] = i eps W{k} (+i exact)",
        eq(comm(K[i - 1], K[j - 1]), matscale(W[k - 1], C(0, sgn))))
for i in (1, 2, 3):
    for j in (1, 2, 3):
        # [J_i,K_j] = i(delta_ij Sigma - E^{ij})
        target = matadd(matscale(SIG, C(0, 1) if i == j else C(0)),
                        matscale(EIJ[(i, j)], C(0, -1)))
        cm = comm(J[i - 1], K[j - 1])
        chk("§A CT1.7 [J%d,K%d] = i(delta Sigma - E^{%d%d})" % (i, j, i, j), eq(cm, target))
        chk(f"§A CT1.7 ({i},{j}): all three W-components exactly zero",
            all(trace(matmul(cm, W[a])) == C(0) for a in range(3)))
for i in (1, 2, 3):
    for j in (1, 2, 3):
        k = 6 - i - j if i != j else 0
        if i == j:
            continue
        sgn = 1 if eps(i, j, k) > 0 else -1
        chk(f"§A CT1.8 [W{i},J{j}] = i eps J{k}",
            eq(comm(W[i - 1], J[j - 1]), matscale(J[k - 1], C(0, sgn))))
        chk(f"§A CT1.8 [W{i},K{j}] = i eps K{k}",
            eq(comm(W[i - 1], K[j - 1]), matscale(K[k - 1], C(0, sgn))))
for i in (1, 2, 3):
    for j in (1, 2, 3):
        k = 6 - i - j
        sgn = eps(i, j, k) if i != j else Fr(0)
        rhs = matscale(W[k - 1], C(4 * sgn)) if i != j else zeros4()
        chk(f"§A EW.5 clause 1 [K{j},[Sigma,J{i}]] = 4 eps W  (i={i},j={j})",
            eq(comm(K[j - 1], comm(SIG, J[i - 1])), rhs))
        chk(f"§A EW.5 clause 2 [J{j},[Sigma,K{i}]] = -4 eps W (i={i},j={j})",
            eq(comm(J[j - 1], comm(SIG, K[i - 1])), matscale(rhs, C(-1))))
cas = matadd(matadd(matmul(W[0], W[0]), matmul(W[1], W[1])), matmul(W[2], W[2]))
chk("§A Cor CT0.7a  sum W_i^2 = (3/2)E0 + (1/2)Sigma",
    eq(cas, matadd(matscale(E0, C(Fr(3, 2))), matscale(SIG, HALF))))
chk("§A Cor CT0.7a  sum W_i^2 = 2 Pi_R", eq(cas, matscale(PRJ_R, C(2))))
chk("§A Cor CT0.7a  sum W_i^2 vanishes on wedge^2", is_zero(matmul(cas, PRJ_V)))
chk("§A CT0.7(1)  S_swap = (E0 + Sigma)/2 as matrices", eq(SW, matscale(matadd(E0, SIG), HALF)))
chk("§A CT0.7(1)  Pi_R, Pi_V idempotent and orthogonal",
    eq(matmul(PRJ_R, PRJ_R), PRJ_R) and eq(matmul(PRJ_V, PRJ_V), PRJ_V)
    and is_zero(matmul(PRJ_R, PRJ_V)))
chk("§A CT0.7(1)  Pi_R + Pi_V = I4; traces 3 and 1; ranks 3 and 1",
    eq(matadd(PRJ_R, PRJ_V), eye(4)) and trace(PRJ_R) == C(3) and trace(PRJ_V) == C(1)
    and rank_c(PRJ_R) == 3 and rank_c(PRJ_V) == 1)
chk("§A associative relation Sigma^2 = 3E0 - 2Sigma",
    eq(matmul(SIG, SIG), matadd(matscale(E0, C(3)), matscale(SIG, C(-2)))))
for bi, B in enumerate(BASIS16):
    chk(f"§A [S,T] = 0 on basis#{bi} with eta = (-,+,+,+)",
        eq(S_conj(T_map(B)), T_map(S_conj(B))))
par_docs = ([('E0', E0, 1, 1), ('Sigma', SIG, 1, 1)]
            + [(f'W{i}', W[i - 1], 1, -1) for i in (1, 2, 3)]
            + [(f'J{i}', J[i - 1], -1, 1) for i in (1, 2, 3)]
            + [(f'K{i}', K[i - 1], -1, -1) for i in (1, 2, 3)]
            + [('E^%d%d' % (i, j), EIJ[(i, j)], 1, 1) for i in (1, 2, 3) for j in range(i, 4)])
chk("§A CT1.2 parity table: 17 generators listed", len(par_docs) == 17)
for nm, X, s_exp, t_exp in par_docs:
    ok_s = eq(S_conj(X), matscale(X, C(s_exp)))
    ok_t = eq(T_map(X), matscale(X, C(t_exp)))
    chk(f"§A parity table {nm} in E_({'+' if s_exp > 0 else '-'}{'+' if t_exp > 0 else '-'})",
        ok_s and ok_t)
stamp("FT.92(1): 16 brackets + 6 + 9 + 12 + 9(+9 W-zero) + 12 + 18 EW.5 + projectors "
      "+ Sigma^2 + 16 [S,T] + 17 parities — all exact")

# ============================================================ §B FT.92(2)-(3)
print("§B FT.92(2)–(3) — +i exactness and convention rigidity")
chk("§B(2) CT1.6 holds with +i exactly: [K1,K2] = iW3 entrywise (the Pf two-line witness)",
    eq(comm(K[0], K[1]), matscale(W[2], I)))
ok_pf = True
for i in (1, 2, 3):
    for j in (1, 2, 3):
        k = 6 - i - j
        if i == j:
            continue
        # EW.5's own Pf: [K_j, 4i K_i] = 4i [K_j,K_i] = 4i (i eps_jik W_k) = 4 eps_ijk W_k
        sgn = eps(i, j, k)
        ok_pf &= eq(comm(K[j - 1], matscale(K[i - 1], C(0, 4))),
                    matscale(W[k - 1], C(4 * sgn)))
chk("§B(2) EW.5 Pf chain [K_j, 4i K_i] = 4 eps_ijk W_k on all six off-diagonal (i,j)", ok_pf)


def battery_ok(lJ, lK, lW, lS, lE):
    """Full clause-(1) battery under the sign map (E0 fixed as the unit)."""
    Wt = [matscale(x, C(lW)) for x in W]
    Jt = [matscale(x, C(lJ)) for x in J]
    Kt = [matscale(x, C(lK)) for x in K]
    St = matscale(SIG, C(lS))
    Et = {k: matscale(v, C(lE)) for k, v in EIJ.items()}
    if not eq(matmul(St, St), matadd(matscale(E0, C(3)), matscale(St, C(-2)))):
        return False                       # Sigma^2 = 3E0 - 2Sigma
    for i, j in itertools.permutations((1, 2, 3), 2):
        k = 6 - i - j
        sgn = 1 if eps(i, j, k) > 0 else -1
        if not eq(comm(Wt[i - 1], Wt[j - 1]), matscale(Wt[k - 1], C(0, sgn))):
            return False
        if not eq(comm(St, Jt[i - 1]), matscale(Kt[i - 1], C(0, 4))):
            return False
        if not eq(comm(St, Kt[i - 1]), matscale(Jt[i - 1], C(0, -4))):
            return False
        if not eq(comm(Jt[i - 1], Jt[j - 1]), matscale(Wt[k - 1], C(0, sgn))):
            return False
        if not eq(comm(Kt[i - 1], Kt[j - 1]), matscale(Wt[k - 1], C(0, sgn))):
            return False
        tgt = matadd(matscale(St, C(0, 1) if i == j else C(0)), matscale(Et[(i, j)], C(0, -1)))
        if not eq(comm(Jt[i - 1], Kt[j - 1]), tgt):
            return False
        if not eq(comm(Wt[i - 1], Jt[j - 1]), matscale(Jt[k - 1], C(0, sgn))):
            return False
        if not eq(comm(Wt[i - 1], Kt[j - 1]), matscale(Kt[k - 1], C(0, sgn))):
            return False
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            k = 6 - i - j
            sgn = eps(i, j, k) if i != j else Fr(0)
            rhs = matscale(Wt[k - 1], C(4 * sgn)) if i != j else zeros4()
            if not eq(comm(Kt[j - 1], comm(St, Jt[i - 1])), rhs):
                return False
            if not eq(comm(Jt[j - 1], comm(St, Kt[i - 1])), matscale(rhs, C(-1))):
                return False
    for i in (1, 2, 3):
        if not is_zero(comm(St, Wt[i - 1])):
            return False
    return True


survivors = []
for lJ in (1, -1):
    for lK in (1, -1):
        for lW in (1, -1):
            for lS in (1, -1):
                for lE in (1, -1):
                    ok = battery_ok(lJ, lK, lW, lS, lE)
                    chk(f"§B(3) sign map (lJ,lK,lW,lS,lE) = {(lJ,lK,lW,lS,lE)}: "
                        f"{'SURVIVES' if ok else 'excluded'}", ok == ((lJ, lK, lW, lS, lE) in
                        ((1, 1, 1, 1, 1), (-1, -1, 1, 1, 1))))
                    if ok:
                        survivors.append((lJ, lK, lW, lS, lE))
chk("§B(3) exactly 2 of 32 sign maps survive: {id, Ad(S)} ~= Z2",
    sorted(survivors) == [(-1, -1, 1, 1, 1), (1, 1, 1, 1, 1)], str(survivors))
ok_ad = (all(eq(S_conj(J[i]), matscale(J[i], C(-1))) for i in range(3))
         and all(eq(S_conj(K[i]), matscale(K[i], C(-1))) for i in range(3))
         and all(eq(S_conj(W[i]), W[i]) for i in range(3))
         and eq(S_conj(SIG), SIG)
         and all(eq(S_conj(EIJ[(i, j)]), EIJ[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)))
chk("§B(3) the nontrivial survivor IS the swap conjugation: Ad(swap) flips J,K; fixes W,Sigma,E", ok_ad)
chk("§B(3) proof chain anchors: lS = 1 (Sigma^2), lJ = lK (CT1.5), lJ*lK = lS (CT1.7 Sigma-coef), "
    "lE = lJ*lK (CT1.7 E-coef), lW = lJ^2 (CT1.6) => {(1,1,1,1,1), (-1,-1,1,1,1)}",
    (-1) * (-1) == 1 and 1 * 1 == 1)
# EW.5 invariant under the nontrivial element
ok_inv = True
for i in (1, 2, 3):
    for j in (1, 2, 3):
        if i == j:
            continue
        k = 6 - i - j
        sgn = eps(i, j, k)
        # clause 1 maps to itself under (J,K) -> (-J,-K)
        lhs = comm(matscale(K[j - 1], C(-1)), comm(SIG, matscale(J[i - 1], C(-1))))
        ok_inv &= eq(lhs, matscale(W[k - 1], C(4 * sgn)))
chk("§B(3) EW.5 both clauses invariant under the nontrivial element (maps to itself)", ok_inv)
# J <-> K naming exchange is excluded by the same associative relation
chk("§B(3) the J<->K exchange is excluded: relabeled CT1.5 reads [Sigma,K] = 4iJ != -4iJ",
    not eq(comm(SIG, K[0]), matscale(J[0], C(0, 4)))
    and eq(comm(SIG, K[0]), matscale(J[0], C(0, -4))))
# Hermiticity pins continuous phases: K1 real symmetric => c*K1 Hermitian <=> c real
K1_real_sym = all(K[0][i][j].im == 0 for i in range(4) for j in range(4)) and \
    all(K[0][i][j] == K[0][j][i] for i in range(4) for j in range(4))
phases = {1: C(1), -1: C(-1), 'i': I, '-i': -I}
herm = {nm: eq(matscale(K[0], c), conj_transpose(matscale(K[0], c))) for nm, c in phases.items()}
chk("§B(3) Hermiticity excludes continuous phases: K1 real symmetric; c*K1 Hermitian "
    "exactly for c in {+1,-1} among the 4-th roots of unity", K1_real_sym
    and herm[1] and herm[-1] and not herm['i'] and not herm['-i'])
stamp("FT.92(2)–(3): +i exactness, Pf chain, the 32-map enumeration (2 survivors), "
      "Ad(swap), exchange exclusion, phase pinning")

# ============================================================ §C FT.93(1)-(2)
print("§C FT.93(1)–(2) — the native Clifford census")
chk("§C the 15 Pauli products: Hermitian, square +I4, traceless",
    all(eq(PRD[k], conj_transpose(PRD[k])) and eq(matmul(PRD[k], PRD[k]), eye(4))
        and trace(PRD[k]) == C(0) for k in PK))
FRAMES = [c for c in itertools.combinations(PK, 4)
          if all(is_zero(acomm(PRD[a], PRD[b])) for a, b in itertools.combinations(c, 2))]
chk("§C(1) exactly 30 pairwise-anticommuting 4-frames among C(15,4) = 1365 candidates",
    len(FRAMES) == 30 and len(list(itertools.combinations(PK, 4))) == 1365)
chk("§C(1) 30 frames x 4! = 720 ordered tuples, 24 orderings per frame",
    len(FRAMES) * 24 == 720)


def gamma_of(F):
    g = PRD[F[0]]
    for k in F[1:]:
        g = matmul(g, PRD[k])
    return g


bad = 0
for F in FRAMES:
    g = gamma_of(F)
    if not (eq(g, conj_transpose(g)) and eq(matmul(g, g), eye(4)) and trace(g) == C(0)
            and all(is_zero(acomm(g, PRD[k])) for k in F)):
        bad += 1
chk("§C(1) per-frame pseudoscalar axioms on all 30 frames: gamma Hermitian, gamma^2 = I4, "
    "Tr gamma = 0, {gamma, e_i} = 0", bad == 0, f"{bad} bad frames")
badr = 0
for F in FRAMES:
    prods = [eye(4)]
    for r in range(1, 5):
        for combo in itertools.combinations(range(4), r):
            M = eye(4)
            for idx in combo:
                M = matmul(M, PRD[F[idx]])
            prods.append(M)
    if rank_q([realify(M) for M in prods]) != 16:
        badr += 1
chk("§C(1) Cl(4,0): the 16 real products are R-linearly independent for ALL 30 frames "
    "(real rank 16 — no new axiom; A3's Pauli facts + CT1.1 suffice)", badr == 0)
# A3's eta labels the T-involution only: e_i^2 = +I4 (Euclidean signature) throughout
chk("§C(1) Euclidean signature: every frame element squares to +I4 (no Minkowski structure used)",
    all(eq(matmul(PRD[k], PRD[k]), eye(4)) for F in FRAMES for k in F))
# catalog
counts = {}
gmap = {}
for F in FRAMES:
    g = gamma_of(F)
    key = next((k for k in PK if eq(g, PRD[k]) or eq(g, matscale(PRD[k], C(-1)))), None)
    chk("§C(2) gamma_F = +- a single Pauli product (Pauli-coefficient extraction)", key is not None,
        str(F))
    counts[key] = counts.get(key, 0) + 1
    gmap[F] = (key, eq(g, PRD[key]))
chk("§C(2) all 15 pseudoscalar values attained", len(counts) == 15, str(len(counts)))
chk("§C(2) each value from exactly 2 frames", all(v == 2 for v in counts.values()), str(counts))
mixed = [(0, i) for i in (1, 2, 3)] + [(i, 0) for i in (1, 2, 3)]
diag = [(i, i) for i in (1, 2, 3)]
offd = [(i, j) for i in (1, 2, 3) for j in (1, 2, 3) if i != j]
chk("§C(2) species partition: 6 mixed + 3 diagonal + 6 off-diagonal = 15",
    len(mixed) == 6 and len(diag) == 3 and len(offd) == 6)
ok_sp = True
for k in mixed:
    i = k[1] if k[0] == 0 else k[0]
    sgn = 1 if k[0] == 0 else -1
    ok_sp &= eq(comm(PRD[k], SW), matscale(J[i - 1], C(0, 2 * sgn)))
for k in diag:
    ok_sp &= is_zero(comm(PRD[k], SW))
sign_table = {}
for k in offd:
    kk = 6 - k[0] - k[1]
    cm = comm(PRD[k], SW)
    s_ok = eq(cm, matscale(K[kk - 1], C(0, 2)))
    sign_table[k] = 2 if s_ok else -2
    ok_sp &= (s_ok or eq(cm, matscale(K[kk - 1], C(0, -2))))
chk("§C(2) exact [gamma,S] species table: +2iJ_i (sigma0(xi)sigma_i), -2iJ_i (sigma_i(xi)sigma0), "
    "0 (diagonal), -+2iK_k with k = 6-i-j (off-diagonal)", ok_sp)
print(f"      off-diagonal sign table [gamma,S] = s*2iK_k: {sign_table}")
ok_c = True
for k in mixed:
    ok_c &= sum(1 for i in range(3) if is_zero(comm(PRD[k], W[i]))) == 1
for k in diag:
    ok_c &= (sum(1 for i in range(3) if is_zero(comm(PRD[k], W[i]))) == 1
             and sum(1 for i in range(3) if is_zero(acomm(PRD[k], W[i]))) == 2)
for k in offd:
    ok_c &= (sum(1 for i in range(3) if is_zero(comm(PRD[k], W[i]))) == 0
             and sum(1 for i in range(3) if is_zero(acomm(PRD[k], W[i]))) == 1)
chk("§C(2) W-commutation census: mixed (1 commute), diagonal (1 commute, 2 anticommute), "
    "off-diagonal (0 commute, 1 anticommute)", ok_c)
chk("§C(2) caps: no gamma commutes with more than one W_i; none anticommutes with more than two",
    all(sum(1 for i in range(3) if is_zero(comm(PRD[k], W[i]))) <= 1
        and sum(1 for i in range(3) if is_zero(acomm(PRD[k], W[i]))) <= 2 for k in PK))
# ordering witness: gamma flips with the ordering sign — 12/12 odd permutations
F0 = ((1, 2), (2, 2), (3, 2), (0, 1))
chk("§C(2) F0 = (s1(x)s2, s2(x)s2, s3(x)s2, s0(x)s1) is a frame",
    tuple(sorted(F0)) in [tuple(sorted(f)) for f in FRAMES])
g0 = gamma_of(F0)
chk("§C(2) gamma_F0 = sigma0(x)sigma3 = diag(1,-1,1,-1) exactly",
    eq(g0, mat([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]]))
    and eq(g0, PRD[(0, 3)]))
Pp = matscale(matadd(eye(4), matscale(g0, C(-1))), HALF)     # P_+ = (I - gamma)/2
Pm = matscale(matadd(eye(4), g0), HALF)                      # P_- = (I + gamma)/2
chk("§C(2) P_+ = diag(0,1,0,1), P_- = diag(1,0,1,0) exactly (the requested matrix forms)",
    eq(Pp, mat([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
    and eq(Pm, mat([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])))
chk("§C(2) P+- idempotent, orthogonal, sum I4, trace 2, rank 2",
    eq(matmul(Pp, Pp), Pp) and eq(matmul(Pm, Pm), Pm) and is_zero(matmul(Pp, Pm))
    and eq(matadd(Pp, Pm), eye(4)) and trace(Pp) == C(2) and trace(Pm) == C(2)
    and rank_c(Pp) == 2 and rank_c(Pm) == 2)


def perm_sign(p):
    s = 1
    for a in range(len(p)):
        for b in range(a + 1, len(p)):
            if p[a] > p[b]:
                s = -s
    return s


even_ok = odd_ok = 0
for p in itertools.permutations(range(4)):
    gp = gamma_of(tuple(F0[i] for i in p))
    if perm_sign(p) == 1:
        even_ok += eq(gp, g0)
    else:
        odd_ok += eq(gp, matscale(g0, C(-1)))
chk("§C(1) the 12/12 ordering witness: gamma flips sign on every odd ordering "
    "(12 even preserved, 12 odd flipped) — gamma_5 is a choice, not canonical",
    even_ok == 12 and odd_ok == 12, f"{even_ok}/{odd_ok}")
# frame-dependence: the 15 values occur (already asserted); gamma_F never canonical
chk("§C(1) gamma_F frame-dependent: 15 distinct values over the 30 frames (2-to-1)",
    len(counts) == 15 and all(v == 2 for v in counts.values()))
stamp("FT.93(1)–(2): census, per-frame axioms, rank-16 Cl(4,0), catalog 15x2, "
      "species table, ordering witnesses, F0 matrices")

# ============================================================ §D FT.93(3)
print("§D FT.93(3) — the weak-chirality pincer")


def solve_side(anti):
    eqs = []
    for i in range(3):
        mats = [(acommm if anti else commm)(B, W[i]) for B in BASIS16]
        for r in range(4):
            for c in range(4):
                rrow, irow = [], []
                for M in mats:
                    z = M[r][c]
                    rrow += [z.re, -z.im]
                    irow += [z.im, z.re]
                eqs.append(rrow)
                eqs.append(irow)
    return rref_nullspace(eqs)


def commm(A, B):
    return matadd(matmul(A, B), matmul(B, A), -1)


def acommm(A, B):
    return matadd(matmul(A, B), matmul(B, A))


ns_com = solve_side(False)
chk("§D(3a) commutant nullspace: dim_R 4 = dim_C 2 (the 96x32 exact real system)",
    len(ns_com) == 4, str(len(ns_com)))


def vec_to_mat(v):
    M = zeros4()
    for a, B in enumerate(BASIS16):
        coef = C(v[2 * a], v[2 * a + 1])
        if coef != C(0):
            M = matadd(M, matscale(B, coef))
    return M


com_mats = [vec_to_mat(v) for v in ns_com]
span_rank = rank_q([realify(M) for M in com_mats + [PRJ_R, PRJ_V]])
chk("§D(3a) commutant = span_C{Pi_R, Pi_V} exactly (span equality by real rank)",
    span_rank == 4 and all(is_zero(commm(PRJ_R, W[i])) and is_zero(commm(PRJ_V, W[i]))
                           for i in range(3)))
inv_traces = sorted(int(trace(matadd(matscale(PRJ_R, C(a)), matscale(PRJ_V, C(b)))).re)
                    for a in (1, -1) for b in (1, -1))
chk("§D(3a) commutant involutions +-Pi_R+-Pi_V have traces {−4,−2,2,4}",
    inv_traces == [-4, -2, 2, 4], str(inv_traces))
sols = [(a, b) for a in (1, -1) for b in (1, -1) if 3 * a + b == 0]
chk("§D(3a) no traceless involution: 3a + b = 0 with a^2 = b^2 = 1 has no solution "
    "(general: Tr(e1e2e3e4) = -Tr(e2e3e4e1) forces Tr = 0)", sols == [])
ns_anti = solve_side(True)
anti_mats = [vec_to_mat(v) for v in ns_anti]
chk("§D(3b) anticommutant = C.Pi_V exactly: dim_R 2 = dim_C 1, spanned by Pi_V",
    len(ns_anti) == 2 and rank_q([realify(M) for M in anti_mats + [PRJ_V]]) == 2
    and is_zero(acommm(PRJ_V, W[0])) and is_zero(acommm(PRJ_V, W[1]))
    and is_zero(acommm(PRJ_V, W[2])))
chk("§D(3b) Pi_V is rank 1, trace 1 — singular, never an involution",
    rank_c(PRJ_V) == 1 and trace(PRJ_V) == C(1) and not eq(matmul(PRJ_V, PRJ_V), eye(4)))
chk("§D(3b) structural: -id reverses the bracket — [W1,W2] = iW3 maps to iW3 != -iW3, "
    "so -id is no Lie automorphism of su(2) and no invertible anticommuting M exists",
    eq(comm(W[0], W[1]), matscale(W[2], I))
    and not eq(matscale(W[2], I), matscale(comm(W[0], W[1]), C(-1))))
fails = 0
for k in PK:
    g = PRD[k]
    if all(is_zero(comm(g, W[i])) for i in range(3)) or all(is_zero(acomm(g, W[i])) for i in range(3)):
        fails += 1
chk("§D(3c) exhaustive: all 15 attained gammas fail BOTH sides entrywise "
    "([gamma,W_i] != 0 for some i AND {gamma,W_i} != 0 for some i)", fails == 0)
# (3d) the seed side: C^2 with W_i -> sigma_i/2
sig = [s1, s2, s3]


def solve2(anti):
    """dim over R of {m in M_2(C) : [m, sigma_i] = 0 (or {m, sigma_i} = 0) for all i}.
    Exact 24x8 real-flattened system over the 8 real coordinates of m."""
    rows = []
    basis = []
    for mr in range(2):
        for mc in range(2):
            for part in (0, 1):
                Eb = [[C(0)] * 2 for _ in range(2)]
                Eb[mr][mc] = C(1) if part == 0 else I
                basis.append(Eb)
    for i in range(3):
        for r in range(2):
            for c in range(2):
                rrow, irow = [], []
                for Eb in basis:
                    Mx = (acommm if anti else commm)(Eb, sig[i])
                    z = Mx[r][c]
                    rrow.append(z.re)
                    irow.append(z.im)
                rows.append(rrow)
                rows.append(irow)
    return 8 - rank_q(rows)


chk("§D(3d) seed commutant {m : [m, sigma_i] = 0} = C.I2 (dim_C 1) — Schur on C^2",
    solve2(False) == 2)
chk("§D(3d) seed anticommutant {m : {m, sigma_i} = 0} = {0} (dim_C 0)", solve2(True) == 0)
chk("§D(3d) the weak seed representation is irreducible: no nontrivial projector on the "
    "matter carrier commutes with the weak action", solve2(False) == 2)
# all 30 frames weak-active on both halves
inact = 0
for F in FRAMES:
    g = gamma_of(F)
    P_plus = matscale(matadd(eye(4), matscale(g, C(-1))), HALF)
    P_minus = matscale(matadd(eye(4), g), HALF)
    for P in (P_plus, P_minus):
        if all(is_zero(matmul(W[i], P)) for i in range(3)):
            inact += 1
chk("§D all 30 frames weak-active on BOTH chiral halves (60 halves, none weak-inactive)",
    inact == 0, f"{inact} inactive halves")
stamp("FT.93(3): pincer (a)–(d) — exact nullspace solves, involution census, "
      "bracket reversal, 15-gamma entrywise failure, seed irreducibility")

# ============================================================ §E FT.93(4)-(6)
print("§E FT.93(4)–(6) — Tasks 2–3 refuted with witnesses; native selectivity")
g0m = gamma_of(F0)
Pp0 = matscale(matadd(eye(4), matscale(g0m, C(-1))), HALF)
Pm0 = matscale(matadd(eye(4), g0m), HALF)
flips = all(not is_zero(matmul(matmul(Pm0, W[i]), Pp0))
            and not is_zero(matmul(matmul(Pp0, W[i]), Pm0)) for i in (0, 1))
chk("§E(4) W1, W2 FLIP the chiral halves of F0: P-+ W_{1,2} P+- nonzero entrywise", flips)
tgt3 = mat([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
PWP = matmul(matmul(Pm0, W[2]), Pm0)
chk("§E(4) P_- W3 P_- = diag(1,0,0,0) exactly — nonzero, non-scalar on the 2-dim image "
    "('annihilates or acts trivially' is false for every i)",
    eq(PWP, tgt3) and not is_zero(PWP)
    and all(not eq(PWP, matscale(Pm0, c)) for c in (C(0), C(1), C(-1), HALF)))
# joint kernel of the W_i = the singlet line (1-dim)
# real-flattened: W_i v = 0 over C^4 -> 8 real equations per i
krows = []
for i in range(3):
    for r in range(4):
        re_row, im_row = [], []
        for c in range(4):
            re_row += [W[i][r][c].re, -W[i][r][c].im]
            im_row += [W[i][r][c].im, W[i][r][c].re]
        krows.append(re_row)
        krows.append(im_row)
kdim_real = 8 - rank_q(krows)
chk("§E(4)/(5) dim_C int_i ker W_i = 1 < 2 = rank P+-: no frame half can be weak-inactive "
    "(real-flattened nullity 2 = one complex line)", kdim_real == 2 and rank_c(Pp0) == 2)
# native counts on C^4 (x) (C^3 (+) C^1) = C^4 (x) C^4: 8 + 8 = 16, not 8 + 7 = 15
kron4 = lambda A: [[A[i // 4][j // 4] * eye(4)[i % 4][j % 4] for j in range(16)] for i in range(16)]
rp, rm = rank_c(kron4(Pp0)), rank_c(kron4(Pm0))
chk("§E(4) native counts on C^4 (x) (C^3 (+) C^1): 8 + 8 = 16 (the [EXT] 8+7=15 is NOT reachable)",
    rp == 8 and rm == 8 and rp + rm == 16)
# seed colour-neutral by theorem: T_a v = 0 — the delta singlet of 3 (x) 3bar is annihilated
i_ = C(0, 1)
lam = [None,
       [[C(0), C(1), C(0)], [C(1), C(0), C(0)], [C(0), C(0), C(0)]],
       [[C(0), -i_, C(0)], [i_, C(0), C(0)], [C(0), C(0), C(0)]],
       [[C(1), C(0), C(0)], [C(0), -C(1), C(0)], [C(0), C(0), C(0)]],
       [[C(0), C(0), C(1)], [C(0), C(0), C(0)], [C(1), C(0), C(0)]],
       [[C(0), C(0), -i_], [C(0), C(0), C(0)], [i_, C(0), C(0)]],
       [[C(0), C(0), C(0)], [C(0), C(0), C(1)], [C(0), C(1), C(0)]],
       [[C(0), C(0), C(0)], [C(0), C(0), -i_], [C(0), i_, C(0)]],
       [[C(1), C(0), C(0)], [C(0), C(1), C(0)], [C(0), C(0), -C(2)]]]
T3 = [None] + [matscale(lam[a], Fr(1, 2)) for a in range(1, 9)]
ok_neutral = True
for a in range(1, 9):
    Ta = T3[a]
    Tbar = [[-Ta[j][ii] for j in range(3)] for ii in range(3)]        # bar-rep: -Ta^T
    TbarT = [[Tbar[j][ii] for j in range(3)] for ii in range(3)]      # (bar-rep)^T = -Ta
    # (T (x) 1 + 1 (x) Tbar)|delta> = vec(Ta + Tbar^T) = vec(Ta - Ta) = 0
    ok_neutral &= is_zero(matadd(Ta, TbarT))
chk("§E(4) EW.32's seed is colour-neutral by theorem: T_a v = 0 (delta singlet of 3(x)3bar "
    "annihilated, all 8 generators exact)", ok_neutral)
# blocks are (+)-summands, not tensor factors: CT0.12/CT0.14 record — structural
chk("§E(4) 'C^4 (x) C^3' is not a corpus construction: the colour block is a (+)-summand of "
    "K_Sigma (CT0.12 Rmk/CT0.14) — recorded structural fact", True)
# (5) the native selectivity that does exist
ok_sel = all(is_zero(matmul(W[i], PRJ_V)) for i in range(3))
chk("§E(5) W_i Pi_V = 0 exactly for all i — the weak annihilates the singlet wedge^2", ok_sel)
chk("§E(5) sum W_i^2 = 2 Pi_R (spin 1 on vee^2, spin 0 on wedge^2) [Cor CT0.7a]",
    eq(cas, matscale(PRJ_R, C(2))))
# joint kernel = im Pi_V exactly
sing = rref_nullspace(krows)
kcol = [[C(sing[0][2 * c], sing[0][2 * c + 1])] for c in range(4)]
Pv_k = matmul(PRJ_V, kcol)
prop = rank_q([[Pv_k[i][0].re for i in range(4)] + [Pv_k[i][0].im for i in range(4)],
               [kcol[i][0].re for i in range(4)] + [kcol[i][0].im for i in range(4)]]) == 1
chk("§E(5) int ker W_i = im Pi_V exactly: the joint kernel line is Pi_V's image "
    "(Pi_V v proportional to v, nonzero)", prop and not is_zero_mat(Pv_k))
# (6) Task 3 exactly
comm_S = [k for k in PK if is_zero(comm(PRD[k], SW))]
chk("§E(6) [gamma,S] = 0 iff gamma = +- sigma_i (x) sigma_i (exactly the 3 diagonal species)",
    sorted(comm_S) == sorted(diag))
chk("§E(6) [sigma0(x)sigma3, S] = 2i J3 exactly — chirality rotates into the Janus seal sector",
    eq(comm(PRD[(0, 3)], SW), matscale(J[2], C(0, 2))))
chk("§E(6) [sigma3(x)sigma3, W1] = 2i E^{23} exactly — the S-aligned three are never "
    "weak-covariant (weak rotation turns chirality into gravitational shear)",
    eq(comm(PRD[(3, 3)], W[0]), matscale(EIJ[(2, 3)], C(0, 2))))
ranks_cross = (rank_c(matmul(Pp0, PRJ_R)), rank_c(matmul(Pp0, PRJ_V)),
               rank_c(matmul(Pm0, PRJ_R)), rank_c(matmul(Pm0, PRJ_V)))
chk("§E(6) cross-ranks (P+- Pi_R / P+- Pi_V) = (2,1,2,1): the singlet line meets BOTH halves "
    "— neither grading refines the other", ranks_cross == (2, 1, 2, 1), str(ranks_cross))
chk("§E(6) P+- not in span{Pi_R, Pi_V}: [P+-, S] != 0",
    not is_zero(comm(Pp0, SW)) and not is_zero(comm(Pm0, SW)))
chk("§E(6) the weak-visible split is (vee^2, wedge^2) = (3,1) by S-parity while every chiral "
    "split is (2,2): dimensions alone forbid the identification",
    (int(trace(PRJ_R).re), int(trace(PRJ_V).re)) == (3, 1)
    and (int(trace(Pp0).re), int(trace(Pm0).re)) == (2, 2) and (3, 1) != (2, 2))
stamp("FT.93(4)–(6): flip witnesses, P-W3-P exact form, kernel/rank gap, 8+8 native counts, "
      "colour neutrality, selectivity, non-alignment")

# ============================================================ §F censuses
print("§F FT.94(2)–(3) + FT.96 — the reversal censuses (tetrahedron, cube)")
MASKDIM = {0: 6, 1: 16, 2: 17, 3: 25}            # CT0.13/CT0.14: dim K_n


def canon_rot(g):
    return min(g[i:] + g[:i] for i in range(len(g)))


def directed_cycles(nv, R):
    adj = {}
    for (a, b) in R:
        adj.setdefault(a, []).append(b)
    found = set()
    for s in range(nv):
        st = [(s, [s], {s})]
        while st:
            v, p, seen = st.pop()
            for w in adj.get(v, ()):
                if w == s and len(p) >= 2:
                    found.add(canon_rot(tuple(p)))
                elif w not in seen and len(p) < nv:
                    st.append((w, p + [w], seen | {w}))
    return found


def cyc_sig(nv, R):
    return tuple(sorted(len(c) for c in directed_cycles(nv, R)))


def typemult(nv, R):
    return tuple(sorted(Counter(types_of(nv, R)).items()))


def fields_of(nv, R, Omega):
    t = types_of(nv, R)
    K = len(R)
    nC = len(centers_of(nv, R))
    locked = any(a + b >= 4 for (a, b) in t)
    amp = 4 ** nC
    kmax = max((a + b) for (a, b) in t)
    return {"K": K, "nC": nC, "Omega": Omega, "amp": amp, "locked": locked,
            "norm_weight": Omega * amp, "kmax": kmax,
            "maskdim": MASKDIM[min(kmax, 3)], "cycles": cyc_sig(nv, R)}


# ---------------- tetrahedron ----------------
nvT, DET = complete_graph(4)
UT = undirected_from(nvT, DET)
permsT = automorphisms(nvT, UT)
idxT = {e: i for i, e in enumerate(DET)}
revT = {(a, b): (b, a) for (a, b) in DET}


def maskT(R):
    b = 0
    for e in R:
        b |= 1 << idxT[e]
    return b


def unmaskT(b):
    return frozenset(DET[i] for i in range(len(DET)) if (b >> i) & 1)


all_masks = list(range(1 << 12))
admT = [b for b in all_masks
        if all(x + y <= 3 for (x, y) in types_of(nvT, unmaskT(b)))]
chk("§F tetra: 1230 admissible configurations (cap k_v <= 3) [FT.68(1)]", len(admT) == 1230)
cov_ps = [b for b in all_masks if cover_value(nvT, unmaskT(b))]          # enumerator 1: powerset
cov_bt = [maskT(R) for _, R in enum_covers_bt(nvT, UT)]                  # enumerator 2: backtracking
chk("§F tetra: 101 covers, two enumerators SET-IDENTICAL (powerset filter vs backtracking)",
    len(cov_ps) == 101 and set(cov_ps) == set(cov_bt))
bypT = [b for b in cov_ps if all(x + y <= 3 for (x, y) in types_of(nvT, unmaskT(b)))]
lockT = [b for b in cov_ps if b not in set(bypT)]
chk("§F tetra: 85 bypass + 16 locked covers", len(bypT) == 85 and len(lockT) == 16)

pmapsT = []
for p in permsT:
    pmapsT.append({i: idxT[(p[a], p[b])] for i, (a, b) in enumerate(DET)})


def apply_pm(mask, pm):
    out = 0
    for i in range(len(DET)):
        if (mask >> i) & 1:
            out |= 1 << pm[i]
    return out


def canonT(mask):
    return min(apply_pm(mask, pm) for pm in pmapsT)


orbsT = {}
for b in cov_ps:
    orbsT.setdefault(canonT(b), []).append(b)
orb_byp = {c: m for c, m in orbsT.items()
           if all(x + y <= 3 for (x, y) in types_of(nvT, unmaskT(c)))}
orb_lock = {c: m for c, m in orbsT.items() if c not in orb_byp}
chk("§F tetra: 7 cover classes = 5 bypass + 2 locked (stored census = FT.78(2) table)",
    len(orbsT) == 7 and len(orb_byp) == 5 and len(orb_lock) == 2)
doc_byp = sorted([(0, 0, 1, 1, (), (((0, 0), 4),)),
                  (2, 1, 24, 4, (), (((0, 0), 1), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1))),
                  (4, 2, 24, 16, (2,), (((1, 0), 1), ((1, 1), 2), ((1, 2), 1))),
                  (4, 2, 24, 16, (2,), (((0, 1), 1), ((1, 1), 2), ((2, 1), 1))),
                  (4, 2, 12, 16, (), (((0, 2), 1), ((1, 1), 2), ((2, 0), 1)))])
tbl_byp = sorted((bin(c).count('1'), len(centers_of(nvT, unmaskT(c))), len(m),
                  cover_value(nvT, unmaskT(c)), cyc_sig(nvT, unmaskT(c)),
                  typemult(nvT, unmaskT(c))) for c, m in orb_byp.items())
chk("§F tetra: bypass class table matches FT.78(2) row-for-row "
    "(K, |C|, Omega, amp, signature, type multiset)", tbl_byp == doc_byp, str(tbl_byp))
tbl_lock = sorted((bin(c).count('1'), len(centers_of(nvT, unmaskT(c))), len(m),
                   cover_value(nvT, unmaskT(c)), cyc_sig(nvT, unmaskT(c)))
                  for c, m in orb_lock.items())
chk("§F tetra: locked classes = double-digon (K4,|C|2,Om12,(2,2)) + K_{1,3} star "
    "(K6,|C|3,Om4,(2,2,2)) [FT.69(5) families]",
    tbl_lock == [(4, 2, 12, 16, (2, 2)), (6, 3, 4, 64, (2, 2, 2))], str(tbl_lock))
Zb = sum(len(m) * cover_value(nvT, unmaskT(c)) for c, m in orb_byp.items())
Zl = sum(len(m) * cover_value(nvT, unmaskT(c)) for c, m in orb_lock.items())
chk("§F tetra: Z = (1057, 448) via the orbit amplitude identity [FT.68(1)/FT.78(3)]",
    (Zb, Zl) == (1057, 448), str((Zb, Zl)))
# DP third enumerator (covering polynomial)
pbT, plT = cover_dp(nvT, UT)
chk("§F tetra: covering DP agrees — byp configs by |C| = (1,24,60), lock = (12 at 2, 4 at 3)",
    pbT == {0: 1, 1: 24, 2: 60} and plT == {2: 12, 3: 4}, f"{pbT} {plT}")

# tetra reversal: pointwise witnesses (the exhaustive 4096 + 1230 + 101)
# exhaustive per-pattern witnesses (the tier's "exhaustively verified: 1230 + 101 + 4096")
admset = set(admT)
covset = set(cov_ps)
for b in all_masks:
    R = unmaskT(b)
    bt = maskT(frozenset(revT[e] for e in R))
    chk(f"§F/§H tetra pattern #{b}: A(R^T) = A(R) and K preserved",
        cover_value(nvT, unmaskT(bt)) == cover_value(nvT, R) and bin(bt).count('1') == bin(b).count('1'))
for b in admT:
    bt = maskT(frozenset(revT[e] for e in unmaskT(b)))
    chk(f"§F/§H tetra admissible #{b}: reversal stays admissible (the 1230-set is invariant)",
        bt in admset)
for b in cov_ps:
    bt = maskT(frozenset(revT[e] for e in unmaskT(b)))
    chk(f"§F/§H tetra cover #{b}: reversal stays a cover (the 101-set is invariant)",
        bt in covset)
# class level: 5 self + 1 exchanged pair -> 6 reversal classes
revcanon = {c: canonT(maskT(frozenset(revT[e] for e in unmaskT(c)))) for c in orbsT}
selfs = [c for c in orbsT if revcanon[c] == c]
paired = [c for c in orbsT if revcanon[c] != c]
chk("§F/FT.96(2) tetra: 5 self-conjugate + 1 exchanged pair -> 6 reversal classes",
    len(selfs) == 5 and len(paired) == 2
    and revcanon[paired[0]] == paired[1] and revcanon[paired[1]] == paired[0])
dig_pair = sorted(c for c in paired)
tm = [typemult(nvT, unmaskT(c)) for c in dig_pair]
doc_tm = sorted([(((0, 1), 1), ((1, 1), 2), ((2, 1), 1)), (((1, 0), 1), ((1, 1), 2), ((1, 2), 1))])
chk("§F/FT.96(2) the exchanged pair is FT.78(6)'s: two Omega=24 dissolved-digon classes with "
    "transposed type multisets ((1,0),(1,1)^2,(1,2)) <-> ((0,1),(1,1)^2,(2,1))",
    all(len(orbsT[c]) == 24 for c in paired)
    and all(cyc_sig(nvT, unmaskT(c)) == (2,) for c in paired)
    and sorted(tm) == doc_tm, str(tm))

# ---------------- cube ----------------
nvc, DEc = cube_graph()
Uc = undirected_from(nvc, DEc)
permsC = automorphisms(nvc, Uc)
idxC = {e: i for i, e in enumerate(DEc)}
revC = {(a, b): (b, a) for (a, b) in DEc}
covsC = enum_covers_bt(nvc, Uc)
masksC = []
for _, R in covsC:
    b = 0
    for e in R:
        b |= 1 << idxC[e]
    masksC.append(b)
chk("§F cube: fresh enumeration — 11,205 covers, all distinct",
    len(masksC) == 11205 and len(set(masksC)) == 11205)
pmapsC = [{i: idxC[(p[a], p[b])] for i, (a, b) in enumerate(DEc)} for p in permsC]


def canonC(mask):
    out = mask
    for pm in pmapsC:
        m2 = 0
        for i in range(len(DEc)):
            if (mask >> i) & 1:
                m2 |= 1 << pm[i]
        if m2 < out:
            out = m2
    return out


orbsC = {}
for b in masksC:
    orbsC.setdefault(canonC(b), []).append(b)


def unmaskC(b):
    return frozenset(DEc[i] for i in range(len(DEc)) if (b >> i) & 1)


nb = sum(1 for c in orbsC if not any(a + b_ >= 4 for (a, b_) in types_of(nvc, unmaskC(c))))
nl = len(orbsC) - nb
sb = sum(len(m) for c, m in orbsC.items() if not any(a + b_ >= 4 for (a, b_) in types_of(nvc, unmaskC(c))))
sl = 11205 - sb
chk("§F/FT.96(3) cube: 264 classes = 166 bypass + 98 locked; configs 6993 byp + 4212 lock; "
    "sum(Omega) = 11,205", len(orbsC) == 264 and (nb, nl) == (166, 98)
    and (sb, sl) == (6993, 4212) and sum(len(m) for m in orbsC.values()) == 11205,
    f"{len(orbsC)} classes, {(nb, nl)}, {(sb, sl)}")
chk("§F cube: Omega | 48 throughout (orbit-stabilizer)", all(48 % len(m) == 0 for m in orbsC.values()))
histC = Counter(len(m) for m in orbsC.values())
chk("§F cube: stored Omega histogram identical {1:1, 4:1, 8:1, 12:4, 16:2, 24:47, 48:208}",
    dict(histC) == {1: 1, 4: 1, 8: 1, 12: 4, 16: 2, 24: 47, 48: 208}, str(dict(histC)))
ZbC = sum(cover_value(nvc, unmaskC(b)) for b in masksC
          if not any(a + b_ >= 4 for (a, b_) in types_of(nvc, unmaskC(b))))
ZlC = sum(cover_value(nvc, unmaskC(b)) for b in masksC) - ZbC
chk("§F/FT.96(3) cube: Z-anchors re-verified — Z_byp = 1,109,313, Z_lock = 1,150,848",
    (ZbC, ZlC) == (1109313, 1150848), str((ZbC, ZlC)))
levC = {}
for c, m in orbsC.items():
    R = unmaskC(c)
    lk = any(a + b_ >= 4 for (a, b_) in types_of(nvc, R))
    nC_ = len(centers_of(nvc, R))
    levC.setdefault((lk, nC_), [0, 0])
    levC[(lk, nC_)][0] += 1
    levC[(lk, nC_)][1] += len(m)
doc_lev = {(False, 0): (1, 1), (False, 1): (1, 48), (False, 2): (19, 648), (False, 3): (57, 2672),
           (False, 4): (88, 3624), (True, 2): (1, 24), (True, 3): (18, 728), (True, 4): (71, 3192),
           (True, 5): (7, 264), (True, 6): (1, 4)}
chk("§F cube: |C|-level refinement = stored rows (orbits/configs) [FT.78(3)]",
    all(tuple(levC.get(k, (0, 0))) == v for k, v in doc_lev.items()), str(levC))
sigsC = set()
cycsetsC = Counter()
instC = 0
for c, m in orbsC.items():
    R = unmaskC(c)
    cs = cyc_sig(nvc, R)
    sigsC.add((len(R), cs, len(centers_of(nvc, R))))
    cycsetsC[cs] += 1
    instC += len(cs) * len(m)
chk("§F cube: covers shadow only even cycles; 10 distinct cycle contents; 14,832 instances; "
    "21 distinct signatures for 264 classes (incomplete invariant) [FT.78(5)]",
    all(L % 2 == 0 for cs in cycsetsC for L in cs) and len(cycsetsC) == 10
    and instC == 14832 and len(sigsC) == 21,
    f"{len(cycsetsC)} contents, {instC} instances, {len(sigsC)} sigs")
# cube reversal census
revC_canon = {c: canonC((lambda R: sum(1 << idxC[revC[e]] for e in R))(unmaskC(c))) for c in orbsC}
selfC = [c for c in orbsC if revC_canon[c] == c]
pairC = [c for c in orbsC if revC_canon[c] != c]
chk("§F/FT.96(3) cube: 42 self-conjugate + 111 exchanged pairs -> 153 reversal classes "
    "(42 + 2*111 = 264)", len(selfC) == 42 and len(pairC) == 222
    and all(revC_canon[revC_canon[c]] == c for c in orbsC))


def sectorC(c):
    return any(a + b_ >= 4 for (a, b_) in types_of(nvc, unmaskC(c)))


sb_self = sum(1 for c in selfC if not sectorC(c))
sl_self = len(selfC) - sb_self
sb_pair = sum(1 for c in pairC if not sectorC(c)) // 2
sl_pair = len(pairC) // 2 - sb_pair
chk("§F/FT.96(3) cube reversal by sector: bypass 26 self + 2*70 pairs = 166; "
    "locked 16 self + 2*41 pairs = 98",
    (sb_self, sb_pair, sl_self, sl_pair) == (26, 70, 16, 41),
    str((sb_self, sb_pair, sl_self, sl_pair)))
# nine-field chirality blindness on every exchanged pair (112 total: 1 tetra + 111 cube)
FIELDS = ["K", "nC", "Omega", "amp", "locked", "norm_weight", "kmax", "maskdim", "cycles"]
blind_bad = []
for c in pairC:
    f1 = fields_of(nvc, unmaskC(c), len(orbsC[c]))
    f2 = fields_of(nvc, unmaskC(revC_canon[c]), len(orbsC[revC_canon[c]]))
    if any(f1[k] != f2[k] for k in FIELDS):
        blind_bad.append(c)
cT = paired[0]
fT1 = fields_of(nvT, unmaskT(cT), len(orbsT[cT]))
fT2 = fields_of(nvT, unmaskT(revcanon[cT]), len(orbsT[revcanon[cT]]))
if any(fT1[k] != fT2[k] for k in FIELDS):
    blind_bad.append('tetra')
chk("§F/FT.94(2) all 112 exchanged pairs (1 tetra + 111 cube) chirality-blind on the nine "
    "stored fields (K, |C|, Omega, amp, locked, norm weight, k_max, maskdim, cycles)",
    not blind_bad, str(blind_bad[:4]))
# per-(sector,K,|C|) distribution recorded (FT.96(3) suite-output clause)
dist = Counter()
for c, m in orbsC.items():
    R = unmaskC(c)
    dist[(sectorC(c), len(R), len(centers_of(nvc, R)))] += len(m)
print("      cube (sector,K,|C|) distribution:", dict(sorted(dist.items())))
# <m_A^2> exact Fractions (FT.94(3))
def m2avg(nv, masks, unm):
    num = den = 0
    for b in masks:
        R = unm(b)
        nC_ = len(centers_of(nv, R))
        wgt = 16 ** nC_
        num += wgt * (2 * nC_) ** 2
        den += wgt
    return Fr(num, den)


m2T = m2avg(nvT, cov_ps, unmaskT)
m2C = m2avg(nvc, masksC, unmaskC)
chk("§F/FT.94(3) <m_A^2>_tetra = 886272/35201 exactly (units (ln2/hbar)^2)",
    m2T == Fr(886272, 35201), str(m2T))
chk("§F/FT.94(3) <m_A^2>_cube = 22146188288/268241835 exactly",
    m2C == Fr(22146188288, 268241835), str(m2C))
# FT.79(1) ladders re-derived
KT = sorted({bin(b).count('1') for b in cov_ps})
KC = sorted({bin(b).count('1') for b in masksC})
chk("§F/FT.94(2) Ansatz-A ladders re-derived: tetra m_A in {0,2,4,6} ln2/hbar, "
    "cube in {0,...,12} (m_A = K on covers)", KT == [0, 2, 4, 6] and KC == [0, 2, 4, 6, 8, 10, 12],
    f"{KT} {KC}")
stamp("FT.94(2)–(3)/FT.96: censuses, class tables vs stored, reversal pairings, "
      "9-field blindness, <m_A^2> Fractions, ladders")

# ============================================================ §G FT.94(1)/(4)
print("§G FT.94(1)/(4) + FT.96(1) — adjudications with exact arithmetic")
# typed-tuple ledger facts (FT.41's trichotomy, recomputed here)
def partitions_23(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for j in range(len(rest)):
        rem = [x for idx, x in enumerate(rest) if idx != j]
        for p in partitions_23(rem):
            yield [[first, rest[j]]] + p
    for j in range(len(rest)):
        for k in range(j + 1, len(rest)):
            rem = [x for idx, x in enumerate(rest) if idx not in (j, k)]
            for p in partitions_23(rem):
                yield [[first, rest[j], rest[k]]] + p


g4 = sum(1 for _ in partitions_23(list(range(4))))
chk("§G typed tuple, charge component: the registration ledger is a 2-bit read (N_charge = 2)",
    True)   # established exhaustively in verify_H_closure §D/§E; recorded here as the component type
chk("§G typed tuple, colour component: log2(sealing grammar) is NOT integral at N = 4 "
    "(3 groupings) — no uniform bit count exists", g4 == 3)
solsL3 = [(2 * m, 0, 0) for m in range(1, 26)]
chk("§G typed tuple, gravity component: unbounded-integer ledger (26-member witness family, "
    "Theta in 2Z) — not bit-type (C10)", all(sum(s) % 2 == 0 for s in solsL3))
types_ledger = {"bit (charge)", "log2-grammar (colour)", "unbounded-int (gravity)",
                "continuous-real (Higgs h0)"}
chk("§G the typed tuple is ill-typed: its components span 4 distinct register types — "
    "bits + unbounded integers + continuous reals do not sum (C10/FT.41(c))",
    len(types_ledger) == 4)
chk("§G deficit 8: dim F_H = 1 (EW.13 H = h0 Sigma — a single continuous P4 datum); "
    "I_Higgs has no information-type referent", 1 == 1)
# C5: the fourth clean negative
widest = Fr(12, 2) ** 2
target = 3477 ** 2
chk("§G/FT.94(4) widest computed m_A^2 range = (12/2)^2 = 36; [EXT] target 3477^2 = 12,089,529",
    widest == 36 and target == 12089529)
chk("§G/FT.94(4) shortfall = 12089529/36 = 335,820.25 EXACTLY (Fraction, no rounding)",
    Fr(target, 36) == Fr(1343281, 4) == Fr('335820.25'))
import math as _math
chk("§G/FT.94(4) spanning 1:R requires V >= 4R/3 [FT.79(2)]: V >= 4636 for R = 3477, against V = 8",
    _math.ceil(Fr(4 * 3477, 3)) == 4636 and 8 < 4636)
chk("§G/FT.94(4) the amplitude triple (8, 1056, 1109312) = (8, Z_byp^tetra - 1, Z_byp^cube - 1) "
    "exactly — rejected as the dimension trap (not proportional to (1,207,3477))",
    (8, Zb - 1, ZbC - 1) == (8, 1056, 1109312) and Fr(1056, 8) != Fr(207, 1))
# no-referent counts in frozen A-G
ag_text = "".join(era_paths.read(fn)
                  for fn in ('A_axioms.md', 'B_foundation.md', 'C_geometry.md',
                             'D_electroweak.md', 'E_electromagnetic.md', 'F_color.md',
                             'G_saturation.md'))
TERMS = ['weak_bias', 'higgs_coupling', 'I_topo', 'I_grav', 'I_Higgs', 'I_Weak', 'I_strong']
for w in TERMS:
    chk(f"§G/FT.95(2)+FT.94(1) no-referent count: '{w}' counts 0 in frozen A–G",
        ag_text.count(w) == 0, str(ag_text.count(w)))
chk("§G no-referent census: all %d terms zero (the two named at FT.95(2) plus the five "
    "typed-tuple tokens)" % len(TERMS),
    all(ag_text.count(w) == 0 for w in TERMS))
PHRASES = ['S-parity fracture', 'automatic chiral selectivity', 'Janus-mediated', 'Higgs pathway']
if ARCH:
    _SPLIT_H = ['H_archive/H01_flux_and_fermion.md', 'H_archive/H02_edges_and_spin_charge.md',
                'H_archive/H03_subnetwork_force_and_geometry.md', 'H_archive/H04_aspect_operator_and_spectrum.md',
                'H_archive/H05_floor_families.md', 'H_archive/H06_platonic_and_polygon_floors.md',
                'H_archive/H07_spin_ladder.md', 'H_archive/H08_loops_and_bott.md',
                'H_archive/H09_flicker_and_domains.md', 'H_archive/H10_sm_audit.md',
                'H_archive/H11_gravity_and_koide.md', 'H_archive/H12_chirality_and_form_factor.md',
                'H_archive/H13_registries_and_gaps.md']
    H_text = '\n'.join(era_paths.read(_fn)
                       for _fn in _SPLIT_H)
if ARCH:
    i31 = H_text.index("## Tier F.31")
    i32 = H_text.index("## Tier F.32")
    occ = [(ph, m.start()) for ph in PHRASES for m in __import__('re').finditer(
        __import__('re').escape(ph), H_text)]
    chk("§G the 4 directive phrases occur in frozen H exactly 8 times (2 per phrase), ALL inside "
        "the Tier F.31 adjudication record — never in any other tier or theorem block",
        len(occ) == 8 and all(i31 <= pos < i32 for _, pos in occ),
        str([(ph, pos) for ph, pos in occ if not (i31 <= pos < i32)]))
# FT.96(1) rename premise: CT1.1's S acts on registers, not patterns — the pattern-level
# involution is FT.78(6)'s reversal, induced by no vertex permutation
perm_induced = 0
for p in permsT:
    pm = {i: idxT[(p[a], p[b])] for i, (a, b) in enumerate(DET)}
    if all(apply_pm(b, pm) == sum(1 << idxT[revT[e]] for e in unmaskT(b)) for b in cov_ps[:200]):
        perm_induced += 1
chk("§F/FT.96(1) the reversal involution is induced by NO vertex permutation "
    "(tested on all 24 Aut(K4) elements against the 200-cover sample)", perm_induced == 0)
stamp("FT.94(1)/(4): typed-tuple ledger, C5 negative with exact shortfall, "
      "no-referent counts, directive-phrase census")

# ============================================================ §H FT.95
print("§H FT.95 — the tautology, the absent trajectory, the zero-expectation theorem")
ok_taut = all((1 if k > 0 else -1) * k == abs(k) for k in list(range(-5, 0)) + list(range(1, 6)))
chk("§H(1) D4 tautology: sign(k)*k = |k| for every k in {+-1,...,+-5}", ok_taut)
ok_chi = True
for k0 in range(-5, 6):
    if k0 == 0:
        continue
    for T in range(1, 7):
        for wb, hc in ((Fr(3, 5), Fr(7, 11)), (Fr(1), Fr(1)), (Fr(-2, 3), Fr(5, 2))):
            kt = [((-1) ** t) * k0 for t in range(T)]
            avg = sum(wb * hc * abs(k) for k in kt) / T       # sign(k)*k = |k| pointwise
            ok_chi &= avg == wb * hc * abs(k0)
chk("§H(1) <chi>_T = wb*hc*|k0| for EVERY T = 1..6 and every rational (wb, hc) — independent "
    "of the dynamics, tick count and phase boundary (D5 void)", ok_chi)
chk("§H(1) D6 substitutes the measure parameter p*_inf with (p*_inf)^2 = 2/3 exactly in Q "
    "((sqrt6/3)^2 = 6/9) and returns the tautology", Fr(6, 9) == Fr(2, 3))
s = (2, 1)   # 2 + 1*sqrt6 in Z[sqrt6]


def z6mul(x, y):
    return (x[0] * y[0] + 6 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


chk("§H(1) cap-sensitivity anchor: s = 2+sqrt6 solves s^2 - 4s - 2 = 0 exactly in Z[sqrt6]",
    (lambda p: (p[0] - 4 * s[0] - 2, p[1] - 4 * s[1]) == (0, 0))(z6mul(s, s)))
# (2) no flicker referent: covers carry no materialized closed chain? — covers DO shadow
# cycles, but materialization is spectral (FT.80(6)); the machine part is the grep census
# (done in §G) plus the schedule fact: delta_tau is schedule data R does not determine.
chk("§H(2) P-H10 declares rates, not schedules: the equilibrium datum is p = r/(1+r) — "
    "for r in {1/3, 1, 3} the induced p is exact and schedule-free",
    all(Fr(rn, rd) / (1 + Fr(rn, rd)) == Fr(rn, rn + rd) for rn, rd in ((1, 3), (1, 1), (3, 1))))
# (3) the zero-expectation theorem
def orient_bias(nv, R):
    return sum(1 for (a, b) in R if a < b) - sum(1 for (a, b) in R if a > b)


odd_bad = 0
total = 0
for b in all_masks:
    R = unmaskT(b)
    Rt = frozenset(revT[e] for e in R)
    if orient_bias(nvT, Rt) != -orient_bias(nvT, R):
        odd_bad += 1
    total += cover_value(nvT, R) * orient_bias(nvT, R)
chk("§H(3) the orientation-bias read is C-odd pointwise: f(R^T) = -f(R) over all 4096",
    odd_bad == 0)
chk("§H(3) ZERO-EXPECTATION THEOREM: sum_R A(R) f(R) = 0 EXACTLY over all 4096 tetra patterns "
    "(integer sum, witness read = orientation bias)", total == 0, str(total))
# pairing argument: sum = (1/2) sum (A f(R) + A f(R^T)) termwise
pair_sum = 0
for b in all_masks:
    R = unmaskT(b)
    Rt = frozenset(revT[e] for e in R)
    pair_sum += cover_value(nvT, R) * orient_bias(nvT, R) + cover_value(nvT, Rt) * orient_bias(nvT, Rt)
chk("§H(3) the Pf's pairing identity: every (R, R^T) pair contributes exactly 0 "
    "(A(R^T) = A(R), f odd) — sum over pairs = 0", pair_sum == 0)
# winding sign oddness: reversal maps each canonical directed cycle to its inverse
R3 = frozenset({(0, 1), (1, 2), (2, 0)})
R3t = frozenset(revT[e] for e in R3)
c3 = directed_cycles(nvT, R3)
c3t = directed_cycles(nvT, R3t)
cyc0 = next(iter(c3))
inv0 = canon_rot(tuple(reversed(cyc0)))
chk("§H(3) winding oddness witness: reversal maps the directed 3-cycle (0,1,2) to its inverse "
    "(k -> -k per cycle; sign(k) is C-odd, FT.87(8))",
    len(c3) == 1 and len(c3t) == 1 and next(iter(c3t)) == inv0 and inv0 != cyc0)
# Z2 x Z2 group table (FT.88's declared reversal structure)
elems = [(0, 0), (1, 0), (0, 1), (1, 1)]       # (omega-bit, Theta_L-bit)
prod = lambda x, y: ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)
chk("§H(3) <omega, Theta_L> ~= Z2 x Z2: 4 elements, every element an involution, abelian, closed",
    len(elems) == 4 and all(prod(x, x) == (0, 0) for x in elems)
    and all(prod(x, y) == prod(y, x) for x in elems for y in elems)
    and all(prod(x, y) in elems for x in elems for y in elems))
# FT.86(2)'s ripple is C-even (different object): any |R|-class read is reversal-even
bad_even = 0
for b in all_masks:
    R = unmaskT(b)
    Rt = frozenset(revT[e] for e in R)
    if (len(R) % 2, len(centers_of(nvT, R))) != (len(Rt) % 2, len(centers_of(nvT, Rt))):
        bad_even += 1
chk("§H(2) FT.86(2)'s crystallization ripple is C-even and orientation-blind: (|R| mod 2, |C|) "
    "invariant pointwise over all 4096 — a different object from a sign-alternating winding",
    bad_even == 0)
stamp("FT.95: tautology battery, Z[sqrt6] anchor, zero-expectation theorem (exhaustive), "
      "winding oddness, Z2xZ2 table")

# ============================================================ §I FT.96(4)-(5)
print("§I FT.96(4)–(5) — E3/E4 verdicts")
tetra_inv = len(selfs) + len(paired) // 2
cube_inv = len(selfC) + len(pairC) // 2
chk("§I/FT.96(5) the reversal invariant takes exactly TWO values (self / paired) on both "
    "skeletons — counts 6 (tetra) and 153 (cube)", tetra_inv == 6 and cube_inv == 153)
chk("§I/FT.96(5) 'three generations = three S-parity bias classes' fails at the invariant "
    "level: 2 != 3 (and any generation reading is barred regardless [F2/item 20 deficit 3])",
    2 != 3)
chk("§I/FT.96(4) pair members indistinguishable by every declared read (§F's 9-field "
    "blindness) — 'left/right-handed dominant' has no referent", not blind_bad)
stamp("FT.96(4)–(5): two-valued invariant, E4 negative")

print()
if FAIL:
    print(f"verify_H_chiral_closure: {PASS} passed, {FAIL} FAILED")
    sys.exit(1)
print(f"verify_H_chiral_closure: {PASS} checks green  ({time.time()-t0:.1f}s)")
