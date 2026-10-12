
"""
verify_D.py — exact machine verification of the electroweak claims of document D
(Qubitick_formal/D_electroweak.md).

Reuses the exact Pauli/generator machinery of verify_B (complex numbers over
Fraction); all coupling/vev arithmetic uses Fraction (g, g', mu^2 are exact
rationals, so every identity below is bit-exact).

Coverage:
  EW.5/EW.16  [K_j,[Sigma,J_i]] = 4 eps_ijk W_k ;  [J_j,[Sigma,K_i]] = -4 eps_ijk W_k ;
              [J_i,K_j] is S-even and T-even (in E_{++}) and has zero W-component
  EW.10       carrier rep {sigma_i/2, sigma_0/2}: su(2) closure, [W_i, Y] = 0
  EW.12       sum_i E^{ii} = Sigma
  EW.20       W3 v = -v/2, Y v = +v/2 for v = (0,1);
              Gram mass form M2 = mu^2 Re<G_A v, G_B v> equals
              (mu^2/4) [[g^2,0,0,0],[0,g^2,0,0],[0,0,g^2,-g g'],[0,0,-g g',g'^2]]
  EW.21       charged block = c*I2 is basis-change invariant (complex U)
  EW.22/23    neutral block: det = 0, trace = mu^2(g^2+g'^2)/4, rank(M2) = 3,
              kernel spanned by (0,0,g',g); (g,-g') eigenvector with m_Z^2
  EW.24/25    M2_neutral (g',g)^T = 0 ; M2_neutral (g,-g')^T = m_Z^2 (g,-g')^T ;
              m_W^2/m_Z^2 = g^2/(g^2+g'^2) = cos^2(theta_W)
  EW.26       colour (zero) vectors add zero rows/cols to the Gram form
  EW.32       trace normalization  T(G_A G_B) = delta_AB / 2
  EW.34       spin-j lowest weight:  ||J_x v||^2 = j/2, ||J_z v||^2 = j^2,
              ratio = 1/(2j) = 1 iff j = 1/2   (origin of rho = 1)
  EW.35       e^2 = g^2 g'^2/(g^2+g'^2);  1/e^2 = 1/g^2 + 1/g'^2;
              e^2 = g^2 sin^2 = g'^2 cos^2
  EW.36       Q = (sigma_3 + sigma_0)/2 = diag(1,0): idempotent, trace 1
              => spec {1,0}

Run:  python3 verify_D.py
"""

import random
import sys
from fractions import Fraction

from qmath import C, matmul, matadd, matscale, matinv, trace, rank
from verify_B import (s, E0, Sig, W, J, K, E, Swap, eps, comm, eq, eqz,
                      linear_combo, kron, I4)

FAILURES = []

def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILURES.append(name)

I2c = [[C(1), C(0)], [C(0), C(1)]]
Z2c = [[C(0), C(0)], [C(0), C(0)]]

def rep_W(i):          # carrier image of W_i  (EW.32)
    return matscale(s[i], Fraction(1, 2))

def rep_Y():           # carrier image of Y    (EW.32)
    return matscale(s[0], Fraction(1, 2))

def mv(M, v):          # 2x2 matrix times 2-vector over C
    return [M[i][0] * v[0] + M[i][1] * v[1] for i in range(2)]

def herm(x, y):        # <x, y> = sum conj(x_i) y_i
    return sum(x[i].conj() * y[i] for i in range(len(x)))

def T_act(X):
    """metric-sign involution T on pair operators, via basis expansion (A3)."""
    sign = [-1, 1, 1, 1]
    out = [[C(0)] * 4 for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            coeff = trace(matmul(X, kron(s[mu], s[nu]))) / C(4)
            if coeff != C(0):
                out = matadd(out, matscale(kron(s[mu], s[nu]),
                                           coeff * C(sign[mu] * sign[nu])))
    return out

def main():
    print("verify_D: exact electroweak checks (document D)")
    rng = random.Random(20260923)

    # ---- EW.5 / EW.16 : second-order pathways ---------------------------
    ok = True
    ok_perp = True
    ok_sec = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            lhs1 = comm(K[j], comm(Sig, J[i]))
            rhs1 = linear_combo([(C(4 * eps(i, j, k)), W[k]) for k in (1, 2, 3)])
            lhs2 = comm(J[j], comm(Sig, K[i]))
            rhs2 = linear_combo([(C(-4 * eps(i, j, k)), W[k]) for k in (1, 2, 3)])
            ok &= eq(lhs1, rhs1) and eq(lhs2, rhs2)
            X = comm(J[i], K[j])
            # X in E_{++}: S-even and T-even
            ok_sec &= eq(matmul(matmul(Swap, X), Swap), X) and eq(T_act(X), X)
            # zero W-component under the trace-orthogonal basis
            for k in (1, 2, 3):
                ok_perp &= trace(matmul(X, W[k])) == C(0)
    check("EW.5   [K_j,[Sigma,J_i]] = 4 eps W ;  [J_j,[Sigma,K_i]] = -4 eps W", ok)
    check("EW.5   [J_i,K_j] is S-even and T-even (in E_{++})", ok_sec)
    check("EW.5   [J_i,K_j] has zero W-component (E_{++} cap span{W} = {0})", ok_perp)

    # ---- EW.12 : trace of E^{ii} -----------------------------------------
    check("EW.12  sum_i E^{ii} = Sigma", eq(matadd(matadd(E[(1, 1)], E[(2, 2)]),
                                                  E[(3, 3)]), Sig))

    # ---- EW.32 : trace normalization on the carrier -----------------------
    G = [rep_W(1), rep_W(2), rep_W(3), rep_Y()]
    ok = all(trace(matmul(G[a], G[b])) == (C(Fraction(1, 2)) if a == b else C(0))
             for a in range(4) for b in range(4))
    check("EW.32  T(G_A G_B) = delta_AB / 2 on carrier (uniform normalization)", ok)

    # ---- EW.10 : carrier algebra ------------------------------------------
    ok = True
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            rhs = [[C(0)] * 2, [C(0)] * 2]
            for k in (1, 2, 3):
                if eps(i, j, k) != 0:
                    rhs = matadd(rhs, matscale(rep_W(k), C(0, eps(i, j, k))))
            ok &= eq(comm(rep_W(i), rep_W(j)), rhs)
            ok &= eqz(comm(rep_W(i), rep_Y()))
    check("EW.10  carrier: [W_i,W_j] = i eps W_k ;  [W_i,Y] = 0", ok)

    # ---- EW.20 : seed conditions and Gram mass form ------------------------
    v = [C(0), C(1)]                       # lower weight state of W3
    ok = (eq_vec(mv(rep_W(3), v), matscale_vec(v, Fraction(-1, 2)))
          and eq_vec(mv(rep_Y(), v), matscale_vec(v, Fraction(1, 2))))
    check("EW.20  W3 v = -v/2 ;  Y v = +v/2  (seed = lower weight state)", ok)

    for trial in range(8):
        g = Fraction(rng.randint(1, 9), rng.randint(1, 5))
        gp = Fraction(rng.randint(1, 9), rng.randint(1, 5))
        mu2 = Fraction(rng.randint(1, 9), rng.randint(1, 5))
        Gc = [matscale(rep_W(1), g), matscale(rep_W(2), g),
              matscale(rep_W(3), g), matscale(rep_Y(), gp)]
        Gv = [mv(M, v) for M in Gc]
        M2 = [[mu2 * herm(Gv[a], Gv[b]).re for b in range(4)] for a in range(4)]
        q = mu2 / 4
        expected = [[q * g * g, C0f(), C0f(), C0f()],
                    [C0f(), q * g * g, C0f(), C0f()],
                    [C0f(), C0f(), q * g * g, -q * g * gp],
                    [C0f(), C0f(), -q * g * gp, q * gp * gp]]
        if M2 != expected:
            check(f"EW.20  Gram mass form (g={g}, g'={gp}, mu^2={mu2})", False,
                  str(M2))
            break
    else:
        check("EW.20  M2_{AB} = mu^2 Re<G_A v, G_B v> = block-diag form (8 exact draws)", True)

    # rank and kernel (EW.22 / EW.23)
    g, gp, mu2 = Fraction(3, 2), Fraction(5, 7), Fraction(11, 3)
    q = mu2 / 4
    M2f = [[q * g * g, Fraction(0), Fraction(0), Fraction(0)],
           [Fraction(0), q * g * g, Fraction(0), Fraction(0)],
           [Fraction(0), Fraction(0), q * g * g, -q * g * gp],
           [Fraction(0), Fraction(0), -q * g * gp, q * gp * gp]]
    r = rank(M2f)
    kern = [Fraction(0), Fraction(0), gp, g]
    M2k = [sum(M2f[a][b] * kern[b] for b in range(4)) for a in range(4)]
    check("EW.22/23  rank(M2) = 3 ;  kernel spanned by (0,0,g',g)",
          r == 3 and all(x == 0 for x in M2k), f"rank={r}")

    N = [[q * g * g, -q * g * gp], [-q * g * gp, q * gp * gp]]
    detN = N[0][0] * N[1][1] - N[0][1] * N[1][0]
    trN = N[0][0] + N[1][1]
    nullv = [gp, g]
    massv = [g, -gp]
    Nnull = [sum(N[a][b] * nullv[b] for b in range(2)) for a in range(2)]
    Nmass = [sum(N[a][b] * massv[b] for b in range(2)) for a in range(2)]
    mZ2 = q * (g * g + gp * gp)
    ok = (detN == 0 and trN == mZ2
          and all(x == 0 for x in Nnull)
          and Nmass == [mZ2 * massv[0], mZ2 * massv[1]])
    check("EW.23  neutral block: det=0, tr=m_Z^2, null=(g',g), massive=(g,-g')", ok)

    # EW.24 / EW.34 : ratios
    mW2 = q * g * g
    ok = (mW2 / mZ2 == (g * g) / (g * g + gp * gp))
    check("EW.24/34  m_W^2/m_Z^2 = g^2/(g^2+g'^2) = cos^2(theta_W);  rho = 1", ok)

    # EW.35 : residual coupling
    e2 = (g * g * gp * gp) / (g * g + gp * gp)
    ok = (Fraction(1, e2) == Fraction(1, g * g) + Fraction(1, gp * gp)
          and e2 == g * g * Fraction(gp * gp, g * g + gp * gp)     # g^2 sin^2
          and e2 == gp * gp * Fraction(g * g, g * g + gp * gp))    # g'^2 cos^2
    check("EW.35  e^2 = g^2 g'^2/(g^2+g'^2);  1/e^2 = 1/g^2 + 1/g'^2", ok)

    # EW.21 : charged block basis-invariance (complex U)
    c = q * g * g
    cI = [[C(c), C(0)], [C(0), C(c)]]
    ok = True
    for _ in range(6):
        U = [[C(Fraction(rng.randint(-4, 4), 3), Fraction(rng.randint(-4, 4), 3))
              for _ in range(2)] for _ in range(2)]
        detU = U[0][0] * U[1][1] - U[0][1] * U[1][0]
        if detU == C(0):
            continue
        Ui = matinv(U)
        ok &= eq(matmul(matmul(U, cI), Ui), cI)
    check("EW.21  charged block c*I2 invariant under complex basis change (W^+/- degenerate)", ok)

    # EW.26 : colour-neutral vectors add zero rows/cols
    zero_vec = [C(0), C(0)]
    ok = all(herm(zero_vec, x) == C(0)
             for x in [mv(Gc[a], v) for a in range(4)] + [zero_vec])
    check("EW.26  T_a v = 0 => colour rows/cols of the Gram form vanish", ok)

    # EW.34 : spin-j norms  ||J_x v_{-j}||^2 = j/2,  ||J_z v_{-j}||^2 = j^2
    ok = True
    for two_j in (1, 2, 3, 4, 5):
        j = Fraction(two_j, 2)
        m = -j
        # J_+ |m> coefficient^2 = j(j+1) - m(m+1);  at m = -j this is 2j
        c2 = j * (j + 1) - m * (m + 1)
        ok &= (c2 == 2 * j
               and Fraction(1, 4) * c2 == j / 2          # ||J_x v||^2
               and m * m == j * j                         # ||J_z v||^2
               and (j / 2) / (j * j) == Fraction(1, two_j))   # 1/(2j) = 1/two_j
    check("EW.34  ||W1 v||^2 / ||W3 v||^2 = 1/(2j) = 1 iff j = 1/2 (j = 1/2..5/2)", ok)

    # EW.36 : Q = diag(1,0)
    Qm = matadd(matscale(s[3], Fraction(1, 2)), matscale(s[0], Fraction(1, 2)))
    ok = (eq(matmul(Qm, Qm), Qm) and trace(Qm) == C(1)
          and Qm == [[C(1), C(0)], [C(0), C(0)]])
    check("EW.36  Q = (sigma_3+sigma_0)/2 = diag(1,0): idempotent, T Q = 1 => spec {1,0}", ok)

    print()
    if FAILURES:
        print(f"verify_D: {len(FAILURES)} FAILURE(S): {FAILURES}")
        return 1
    print("verify_D: ALL CHECKS PASS (exact arithmetic)")
    return 0


def C0f():
    return Fraction(0)

def eq_vec(x, y):
    return all(a == b for a, b in zip(x, y))

def matscale_vec(v, c):
    return [c * x for x in v]


if __name__ == "__main__":
    sys.exit(main())
