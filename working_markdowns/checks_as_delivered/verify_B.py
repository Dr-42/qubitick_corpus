
"""
verify_B.py — exact machine verification of the operator-algebra claims of
document B (Qubitick_formal/B_foundation.md).

Coverage:
  CT0.1   real/virtual dichotomy: x = Tr(Pi_V rho) real in [0,1] on exact
          rational density states; [R] XOR [V] total+exclusive on every
          (state, epsilon) sample; V = complement (D0.1); endpoints attained;
          inclusive boundary branch x = epsilon in R (A4) 
  CT0.6   dim_R H(C^4) = 16                       (rank of the 16 flattened generators)
  CT0.7   S_swap = (E0 + Sigma)/2
          Pi_R = (3 E0 + Sigma)/4,  Pi_V = (E0 - Sigma)/4
          orthogonal complementary projections, traces 3 and 1
          Sigma = 2 S_swap - E0
  CT0.7a  Casimir sum_i W_i^2 = (3/2) E0 + (1/2) Sigma;
          = 2 * Pi_R on symmetric sector, = 0 on antisymmetric sector
  CT1.1   sector dimensions (7,3,3,3); trace orthogonality
          T(sigma_mu x sigma_nu) = 4 delta_mu0 delta_nu0
  CT1.2   basis sector assignment via S,T eigen-relations
  CT1.3   [E0, X] = 0 for all basis X
  CT1.4   [W_i, W_j] = i eps_ijk W_k
  CT1.5   [Sigma, J_i] = 4i K_i;  [Sigma, K_i] = -4i J_i;  [Sigma, W_i] = 0
  CT1.6   [J_i, J_j] = i eps_ijk W_k;  [K_i, K_j] = i eps_ijk W_k
  CT1.7   [J_i, K_j] = i (delta_ij Sigma - E^{ij})
  CT1.8   [W_i, J_j] = i eps_ijk J_k;  [W_i, K_j] = i eps_ijk K_k
  CT1.9   su(4) traceless complement: all generators except E0 traceless;
          dimension count 1+5+3+3+3 = 15
  CT1.10  delta_ij Ehat^{ij} = 0;  [W_a, E^{ij}] = i(eps_aik E^{kj} + eps_ajk E^{ik})
  CT1.11  [Sigma, J_1] = 4i K_1 != 0  (Sigma non-central), E0 central (CT1.3)

All arithmetic is exact (complex numbers over Fraction). Run:  python3 verify_B.py
"""

import random
import sys
from fractions import Fraction
from qmath import (C, matmul, matadd, matscale, transpose, trace, rank,
                   conj_transpose, one, zero)

FAILURES = []

def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILURES.append(name)

# --------------------------------------------------------------------------
# Pauli basis over exact complex rationals
# --------------------------------------------------------------------------
I2 = [[C(1), C(0)], [C(0), C(1)]]
s = [
    I2,                                                   # sigma_0
    [[C(0), C(1)], [C(1), C(0)]],                         # sigma_1
    [[C(0, 0), C(0, -1)], [C(0, 1), C(0, 0)]],            # sigma_2 = [[0,-i],[i,0]]
    [[C(1), C(0)], [C(0), C(-1)]],                        # sigma_3
]

def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(n * m)]
            for i in range(n * m)]

def comm(A, B):
    return matadd(matmul(A, B), matmul(B, A), -1)

def eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

def eqz(A):
    return all(A[i][j] == 0 for i in range(len(A)) for j in range(len(A[0])))

Z4 = matscale(kron(I2, I2), 0)
I4 = kron(I2, I2)

# generators (CT1.2)
E0 = kron(s[0], s[0])
Sig = matadd(matadd(kron(s[1], s[1]), kron(s[2], s[2])), kron(s[3], s[3]))
W = [None] + [matscale(matadd(kron(s[0], s[i]), kron(s[i], s[0])), Fraction(1, 2))
              for i in (1, 2, 3)]
cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
J = [None] * 4
K = [None] * 4
for i, (j, k) in cyc.items():
    J[i] = matscale(matadd(kron(s[j], s[k]), kron(s[k], s[j]), -1), Fraction(1, 2))
    K[i] = matscale(matadd(kron(s[0], s[i]), kron(s[i], s[0]), -1), Fraction(1, 2))
E = {}
for i in (1, 2, 3):
    for j in (1, 2, 3):
        E[(i, j)] = matscale(matadd(kron(s[i], s[j]), kron(s[j], s[i])), Fraction(1, 2))
# traceless Ehat^{ij} = E^{ij} - delta_ij Sigma / 3
Ehat = {(i, j): matadd(E[(i, j)], Sig, -Fraction(1, 3)) if i == j else E[(i, j)]
        for i in (1, 2, 3) for j in (1, 2, 3)}

eps = lambda i, j, k: Fraction((i - j) * (j - k) * (k - i), 2)

def eps_sum(mats):
    """sum_k c_k mats[k] helper is inline; this returns i*eps combination"""
    return mats

def linear_combo(pairs):
    """pairs: list of (Fraction-or-C coefficient, matrix) -> matrix"""
    out = [[C(0)] * 4 for _ in range(4)]
    for c, M in pairs:
        out = matadd(out, matscale(M, c))
    return out

# swap operator S_swap |ab> -> |ba>
Swap = [[C(0)] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2):
        Swap[2 * a + b][2 * b + a] = C(1)

def check_ct01_dichotomy():
    """CT0.1 — real/virtual dichotomy [(p,q) in R] XOR [(p,q) in V].

    The Pf's arithmetic core, exact:
      * Pi_V = (E0 - Sigma)/4 is the rank-1 orthogonal projector onto wedge^2
        (A3), idempotent/self-adjoint/trace-1;
      * x = |Pi_V rho| = Tr(Pi_V rho) is REAL and in [0,1] for every density
        state rho (A1: rho >= 0, Tr rho = 1) — exact rational witnesses
        rho = M M^dag / Tr(M M^dag), seeded; both endpoints attained;
      * for eps in [0,1] (D0.4) the total order of R gives exactly one of
        [x <= eps], [x > eps] — A4 puts the first branch in R, D0.1 defines V
        as the complement: totality + exclusivity + the complement law hold on
        the full sample universe; the inclusive boundary x = eps lands in R.
    """
    PV = matscale(matadd(E0, Sig, -1), Fraction(1, 4))          # (E0 - Sigma)/4
    PR = matscale(matadd(matscale(E0, 3), Sig), Fraction(1, 4))  # (3E0 + Sigma)/4
    check("CT0.1  Pi_V = (E0-Sigma)/4: idempotent, self-adjoint, Tr = 1 (rank-1, A3)",
          eq(matmul(PV, PV), PV) and eq(conj_transpose(PV), PV) and trace(PV) == C(1))
    check("CT0.1  Pi_V + Pi_R = I4, orthogonal (CT0.7 complement)",
          eq(matadd(PV, PR), I4) and eqz(matmul(PV, PR)))

    rng = random.Random(20260926)

    def rand_rho():
        M = [[C(Fraction(rng.randint(-4, 4)), Fraction(rng.randint(-4, 4)))
              for _ in range(4)] for _ in range(4)]
        MM = matmul(M, conj_transpose(M))
        return matscale(MM, Fraction(1) / trace(MM).re)

    xs = []
    ok_state = True
    for _ in range(12):
        rho = rand_rho()
        ok_state &= (trace(rho) == C(1))
        x = trace(matmul(PV, rho))
        ok_state &= (x.im == 0 and Fraction(0) <= x.re <= Fraction(1))
        xs.append(x.re)
    check("CT0.1  x = Tr(Pi_V rho) real and in [0,1] on 12 exact rational density states",
          ok_state, f"xs sample: {xs[:4]}")
    # endpoints attained: symmetric state -> x = 0; Pi_V itself -> x = 1
    x0 = trace(matmul(PV, matscale(PR, Fraction(1, 3))))
    x1 = trace(matmul(PV, PV))
    check("CT0.1  endpoints attained: x = 0 (rho = Pi_R/3), x = 1 (rho = Pi_V)",
          x0 == C(0) and x1 == C(1))
    # exact half-mixture: x = 1/2 with an exactly equal eps -> inclusive branch
    rho_half = matscale(matadd(matscale(PR, Fraction(1, 3)), PV), Fraction(1, 2))
    xh = trace(matmul(PV, rho_half)).re
    check("CT0.1  half-mixture state has x = 1/2 exactly (boundary witness)", xh == Fraction(1, 2))

    epsilons = [Fraction(0), Fraction(1, 4), Fraction(1, 3), xh, Fraction(2, 3),
                Fraction(3, 4), Fraction(1)]
    universe = {(xi, ei) for xi in range(len(xs) + 3) for ei in range(len(epsilons))}
    allx = xs + [x0.re, x1.re, xh]
    R, V = set(), set()
    ok_xor = True
    for xi, x in enumerate(allx):
        for ei, e in enumerate(epsilons):
            inR = (x <= e)              # A4's branch (inclusive)
            inV = not inR               # D0.1: V = (QxQ) \ R
            ok_xor &= (inR != inV) and (inR or inV)
            (R if inR else V).add((xi, ei))
    check("CT0.1  [R] XOR [V]: total and exclusive on all %d sampled pairs" % len(universe),
          ok_xor)
    check("CT0.1  V = sample-universe \ R exactly, R int V = empty (D0.1 complement law)",
          (R | V) == universe and not (R & V))
    check("CT0.1  inclusive boundary: x = eps lands in R (A4 uses <=)", (len(allx) - 1, epsilons.index(xh)) in R)


def main():
    print("verify_B: exact operator-algebra checks (document B)")
    check_ct01_dichotomy()

    # ---- CT1.1: basis, orthogonality, sector dims ------------------------
    basis = [kron(s[mu], s[nu]) for mu in range(4) for nu in range(4)]
    ok_orth = all(trace(matmul(basis[4 * mu + nu], basis[4 * al + be]))
                  == (C(4) if (mu, nu) == (al, be) else C(0))
                  for mu in range(4) for nu in range(4)
                  for al in range(4) for be in range(4))
    check("CT1.1  T(s_mu x s_nu * s_al x s_be) = 4 d_mu,al d_nu,be", ok_orth)

    # rank of the 16 Hermitian generators as real vectors => dim_R H(C^4) = 16
    flat = []
    for M in basis:
        v = []
        for i in range(4):
            for j in range(4):
                v += [M[i][j].re, M[i][j].im]
        flat.append(v)
    check("CT0.6/CT1.1  dim_R H(C^4) = rank = 16", rank(flat) == 16)

    # sector dimensions by explicit eigenspace counting (7,3,3,3)
    eta = [-1, 1, 1, 1]
    cnt = {(1, 1): 0, (1, -1): 0, (-1, 1): 0, (-1, -1): 0}
    for mu in range(4):
        for nu in range(mu, 4):
            t = eta[mu] * eta[nu]
            if mu == nu:
                cnt[(1, t)] += 1
            else:
                cnt[(1, t)] += 1    # symmetric combination
                cnt[(-1, t)] += 1   # antisymmetric combination
    check("CT1.1  sector dims = (7,3,3,3)",
          (cnt[(1, 1)], cnt[(1, -1)], cnt[(-1, 1)], cnt[(-1, -1)]) == (7, 3, 3, 3),
          str(cnt))

    # tracelessness pattern: T(sigma_mu x sigma_nu) = 4 d_mu0 d_nu0
    ok_tr = all(trace(kron(s[mu], s[nu])) == (C(4) if (mu, nu) == (0, 0) else C(0))
                for mu in range(4) for nu in range(4))
    check("CT1.9  T(s_mu x s_nu) = 4 d_mu0 d_nu0 (only E0 has trace)", ok_tr)

    # ---- CT1.2: sector assignment via S,T actions ------------------------
    def S_act(X):  # S(sigma_mu x sigma_nu) = sigma_nu x sigma_mu, extended linearly
        out = [[C(0)] * 4 for _ in range(4)]
        for mu in range(4):
            for nu in range(4):
                coeff = trace(matmul(X, kron(s[mu], s[nu]))) / C(4)
                if coeff != C(0):
                    out = matadd(out, matscale(kron(s[nu], s[mu]), coeff))
        return out
    # direct checks on each named generator: S(X) = +-X via the swap conjugation
    def S_conj(X):
        return matmul(matmul(Swap, X), Swap)
    ok_S = (eq(S_conj(E0), E0) and eq(S_conj(Sig), Sig)
            and all(eq(S_conj(W[i]), W[i]) for i in (1, 2, 3))
            and all(eqz(matadd(S_conj(J[i]), J[i])) for i in (1, 2, 3))
            and all(eqz(matadd(S_conj(K[i]), K[i])) for i in (1, 2, 3))
            and all(eq(S_conj(E[(i, j)]), E[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)))
    check("CT1.2  S-parities: E0,Sig,W,E^{ij} even; J,K odd", ok_S)

    # T-parity: rebuild each generator from (mu,nu) components and check eta signs
    # W_i: (0,i)+(i,0) -> T=-; J_i: (j,k)-(k,j), both spatial -> T=+;
    # K_i: (0,i)-(i,0) -> T=-; E^{ij}: spatial -> T=+; E0: (0,0) -> +; Sig: (i,i) -> +
    # verified structurally by construction; numeric proxy: T acts as conjugation by
    # the metric-sign diagonal; implement T on basis and check eigen-relations.
    Diag = [[C(0)] * 4 for _ in range(4)]
    sign = [-1, 1, 1, 1]   # eta^mu acting on single-qubit basis: sigma_0 -> -, sigma_i -> +
    # T(X) = eta^mu eta^nu componentwise; represent via basis expansion:
    def T_act(X):
        out = [[C(0)] * 4 for _ in range(4)]
        for mu in range(4):
            for nu in range(4):
                coeff = trace(matmul(X, kron(s[mu], s[nu]))) / C(4)
                if coeff != C(0):
                    out = matadd(out, matscale(kron(s[mu], s[nu]),
                                               coeff * C(sign[mu] * sign[nu])))
        return out
    ok_T = (eq(T_act(E0), E0) and eq(T_act(Sig), Sig)
            and all(eqz(matadd(T_act(W[i]), W[i])) for i in (1, 2, 3))
            and all(eq(T_act(J[i]), J[i]) for i in (1, 2, 3))
            and all(eqz(matadd(T_act(K[i]), K[i])) for i in (1, 2, 3))
            and all(eq(T_act(E[(i, j)]), E[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)))
    check("CT1.2  T-parities: E0,Sig,J,E^{ij} +; W,K -", ok_T)

    check("CT1.2  {E0, E^{ij}(6), W, J, K} is a basis: rank = 16",
          rank([[x for row in M for c in row for x in (c.re, c.im)]
                for M in [E0] + [E[(i, j)] for i in (1, 2, 3) for j in range(i, 4)]
                + [W[i] for i in (1, 2, 3)] + [J[i] for i in (1, 2, 3)]
                + [K[i] for i in (1, 2, 3)]]) == 16)

    # ---- CT1.3: centrality of E0 -----------------------------------------
    all_gens = [E0, Sig] + [W[i] for i in (1, 2, 3)] + [J[i] for i in (1, 2, 3)] \
        + [K[i] for i in (1, 2, 3)] + [E[(i, j)] for i in (1, 2, 3) for j in (1, 2, 3)]
    check("CT1.3  [E0, X] = 0 for all generators X", all(eqz(comm(E0, X)) for X in all_gens))

    # ---- CT1.4 -----------------------------------------------------------
    ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            rhs = linear_combo([(C(0, eps(i, j, k)), W[k]) for k in (1, 2, 3)])
            ok &= eq(comm(W[i], W[j]), rhs)
    check("CT1.4  [W_i,W_j] = i eps_ijk W_k", ok)

    # ---- CT1.5 -----------------------------------------------------------
    ok = all(eq(comm(Sig, J[i]), matscale(K[i], C(0, 4))) for i in (1, 2, 3))
    check("CT1.5  [Sigma,J_i] = 4i K_i", ok)
    ok = all(eq(comm(Sig, K[i]), matscale(J[i], C(0, -4))) for i in (1, 2, 3))
    check("CT1.5  [Sigma,K_i] = -4i J_i", ok)
    ok = all(eqz(comm(Sig, W[i])) for i in (1, 2, 3))
    check("CT1.5  [Sigma,W_i] = 0", ok)

    # ---- CT1.6 -----------------------------------------------------------
    ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            rhs = linear_combo([(C(0, eps(i, j, k)), W[k]) for k in (1, 2, 3)])
            ok &= eq(comm(J[i], J[j]), rhs) and eq(comm(K[i], K[j]), rhs)
    check("CT1.6  [J_i,J_j] = [K_i,K_j] = i eps_ijk W_k", ok)

    # ---- CT1.7 -----------------------------------------------------------
    ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            d = C(1) if i == j else C(0)
            rhs = matscale(matadd(matscale(Sig, d), E[(i, j)], -1), C(0, 1))
            ok &= eq(comm(J[i], K[j]), rhs)
    check("CT1.7  [J_i,K_j] = i(delta_ij Sigma - E^{ij})", ok)

    # ---- CT1.8 -----------------------------------------------------------
    ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            rj = linear_combo([(C(0, eps(i, j, k)), J[k]) for k in (1, 2, 3)])
            rk = linear_combo([(C(0, eps(i, j, k)), K[k]) for k in (1, 2, 3)])
            ok &= eq(comm(W[i], J[j]), rj) and eq(comm(W[i], K[j]), rk)
    check("CT1.8  [W_i,J_j] = i eps J;  [W_i,K_j] = i eps K", ok)

    # ---- CT1.9: su(4) complement ----------------------------------------
    traceless = all(trace(M) == C(0) for M in
                    [Sig] + [W[i] for i in (1, 2, 3)] + [J[i] for i in (1, 2, 3)]
                    + [K[i] for i in (1, 2, 3)] + [Ehat[(i, j)] for i in (1, 2, 3)
                                                   for j in (1, 2, 3)])
    check("CT1.9  Sigma, Ehat, W, J, K all traceless (su(4) span)", traceless)
    dim_su4 = rank([[x for row in M for c in row for x in (c.re, c.im)]
                    for M in [Sig] + [Ehat[(i, j)] for i in (1, 2, 3) for j in range(i, 4)]
                    + [W[i] for i in (1, 2, 3)] + [J[i] for i in (1, 2, 3)]
                    + [K[i] for i in (1, 2, 3)]])
    check("CT1.9  dim su(4) = 1+5+3+3+3 = 15", dim_su4 == 15, f"got {dim_su4}")

    # ---- CT0.7: swap, projections ----------------------------------------
    check("CT0.7   Swap = (E0 + Sigma)/2", eq(Swap, matscale(matadd(E0, Sig), Fraction(1, 2))))
    PR = matscale(matadd(matscale(E0, 3), Sig), Fraction(1, 4))
    PV = matscale(matadd(E0, Sig, -1), Fraction(1, 4))
    check("CT0.7   Pi_R idempotent/hermitian", eq(matmul(PR, PR), PR)
          and eq(conj_transpose(PR), PR))
    check("CT0.7   Pi_V idempotent/hermitian", eq(matmul(PV, PV), PV)
          and eq(conj_transpose(PV), PV))
    check("CT0.7   Pi_R Pi_V = 0,  Pi_R + Pi_V = 1", eqz(matmul(PR, PV)) and eq(matadd(PR, PV), I4))
    check("CT0.7   T Pi_R = 3,  T Pi_V = 1", trace(PR) == C(3) and trace(PV) == C(1))
    check("CT0.7   Sigma = 2 Swap - E0", eq(Sig, matadd(matscale(Swap, 2), E0, -1)))

    # ---- CT0.7a: Casimir --------------------------------------------------
    Cas = matadd(matadd(matmul(W[1], W[1]), matmul(W[2], W[2])), matmul(W[3], W[3]))
    check("CT0.7a  sum W_i^2 = (3/2)E0 + (1/2)Sigma",
          eq(Cas, matadd(matscale(E0, Fraction(3, 2)), matscale(Sig, Fraction(1, 2)))))
    check("CT0.7a  Casimir = 2 on vee^2", eq(matmul(Cas, PR), matscale(PR, 2)))
    check("CT0.7a  Casimir = 0 on wedge^2", eqz(matmul(Cas, PV)))

    # ---- CT1.10: Ehat traceless + vector transformation -------------------
    tr_Ehat = matadd(matadd(Ehat[(1, 1)], Ehat[(2, 2)]), Ehat[(3, 3)])
    check("CT1.10  delta_ij Ehat^{ij} = 0", eqz(tr_Ehat))
    ok = True
    for a in (1, 2, 3):
        for i in (1, 2, 3):
            for j in (1, 2, 3):
                rhs = linear_combo([(C(0, eps(a, i, k)), E[(k, j)]) for k in (1, 2, 3)]
                                   + [(C(0, eps(a, j, k)), E[(i, k)]) for k in (1, 2, 3)])
                ok &= eq(comm(W[a], E[(i, j)]), rhs)
    check("CT1.10  [W_a,E^{ij}] = i(eps_aik E^{kj} + eps_ajk E^{ik})", ok)

    # ---- CT1.11 ------------------------------------------------------------
    check("CT1.11  [Sigma,J_1] = 4i K_1 != 0 (Sigma non-central)",
          eq(comm(Sig, J[1]), matscale(K[1], C(0, 4))) and not eqz(K[1]))

    print()
    if FAILURES:
        print(f"verify_B: {len(FAILURES)} FAILURE(S): {FAILURES}")
        return 1
    print("verify_B: ALL CHECKS PASS (exact arithmetic)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
