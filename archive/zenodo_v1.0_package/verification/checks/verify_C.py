
"""
verify_C.py — exact machine verification of the geometry claims of document C
(Qubitick_formal/C_geometry.md).

Method
------
All tensor identities below are pointwise algebraic (rational) identities in
the jet variables (gbar_{mu nu}, d_rho gbar, d d gbar, omega=Omega^2, d omega,
d d omega). The engine substitutes exact random rational jets; an identity
true on such a Zariski-dense set is true identically. Arithmetic is exact
(fractions.Fraction), so equality means bit-equality, zero tolerance.

Coverage
--------
  CT1.12  traceless split delta^ij hhat_ij = 0;
          Schur identity det(gbar) = det(gbar_ij) * (-1 - kap^2 N (gbar_ij)^-1 N);
          signature (-,+,+,+) by Sylvester sign pattern of leading minors;
          conformal rescaling omega>0 preserves the sign pattern.
  CT1.13  Gamma^l_{mu nu} - Gbar^l_{mu nu} = d^l_mu Ups_nu + d^l_nu Ups_mu - gbar_{mu nu} Ups^l
  CT1.14  R^r_{s mu nu} = Rbar^r_{s mu nu} + 2 nabla-bar_[mu C^r_{nu] s} + 2 C^r_{[mu|l|} C^l_{nu] s}
  CT1.15  Ricci_{mu nu} identity, general D (run for D = 3, 4, 5)
  CT1.16  R = omega^-1 [Rbar - 2(D-1) Box Ups - (D-1)(D-2) |d Ups|^2], general D
  CT1.17  Einstein_{mu nu} identity, D = 4
  CT1.18  linearized Einstein tensor: exact Series2 linearization of the full
          pipeline about gbar = eta + kap*hhat (hhat traceless), Omega = 1:
          O(kap^0) = 0 and O(kap^1) = L[hhat];
          gauge invariance of the FULL linearized tensor under the standard
          transformation h -> h + d_mu xi_nu + d_nu xi_mu (exact, incl. third
          derivatives of xi);
          documented shift of the traceless-PROJECTED variant
          (this corrects the erroneous invariance claim of the old codex CT1.18 step 6).
  CT2.1   dimensional bookkeeping as exact exponent arithmetic
  CT2.9   h^2 = 4 G_N ln2 <=> G_N = h^2/(4 ln2); kappa^2 = 8 pi G_N = 2 pi h^2 / ln2;
          S = A ln2 / h^2 = A/(4 G_N)
  CT2.10  Str(XY) = (-1)^{|X||Y|} Str(YX); Str[X,Y} = 0 (all parity combinations)
  CT1.29  S = n ln2; A = n h^2 => S = A ln2 / h^2

Run:  python3 verify_C.py
"""

import random
import sys
from fractions import Fraction

from qmath import (Series2, matmul, matadd, matscale, matinv, matdet,
                   zero, one, half, from_frac, is_unit)

FAILURES = []

def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILURES.append(name)

# --------------------------------------------------------------------------
# small tensor helpers (nested lists over Fraction or Series2)
# --------------------------------------------------------------------------

def tzeros(D, shape, proto):
    z = zero(proto)
    if shape == 1:
        return z
    return [tzeros(D, shape - 1, proto) for _ in range(D)]

def tsym2(D, rng, proto, lim=5, scale=(1, 3)):
    """random symmetric DxD matrix"""
    M = tzeros(D, 2, proto)
    for i in range(D):
        for j in range(i, D):
            v = from_frac(proto, Fraction(rng.randint(-lim, lim),
                                          rng.randint(scale[0], scale[1])))
            M[i][j] = v
            M[j][i] = v
    return M

def eta_D(D):
    return [[Fraction(-1 if i == j == 0 else (1 if i == j else 0))
             for j in range(D)] for i in range(D)]

def teq(A, B):
    """exact elementwise equality of nested lists"""
    if isinstance(A, list):
        return all(teq(a, b) for a, b in zip(A, B))
    return A == B

# --------------------------------------------------------------------------
# jet generator:  gbar = eta + small symmetric perturbation, omega = Omega^2 > 0
# --------------------------------------------------------------------------

def gen_jet(D, seed, proto_frac=True):
    rng = random.Random(seed)
    eta = eta_D(D)
    gbar = [[Fraction(eta[i][j]) for j in range(D)] for i in range(D)]
    for i in range(D):                       # small perturbation, keeps det != 0 generically
        for j in range(i, D):
            p = Fraction(rng.randint(-2, 2), rng.randint(5, 9))
            gbar[i][j] += p
            gbar[j][i] += p
    dg = [[[Fraction(0)] * D for _ in range(D)] for _ in range(D)]
    for r in range(D):
        for mu in range(D):
            for nu in range(mu, D):
                v = Fraction(rng.randint(-4, 4), rng.randint(1, 5))
                dg[r][mu][nu] = v
                dg[r][nu][mu] = v
    ddg = [[[[Fraction(0)] * D for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for r in range(D):
        for sg in range(r, D):
            for mu in range(D):
                for nu in range(mu, D):
                    v = Fraction(rng.randint(-4, 4), rng.randint(1, 5))
                    ddg[r][sg][mu][nu] = ddg[sg][r][mu][nu] = v
                    ddg[r][sg][nu][mu] = ddg[sg][r][nu][mu] = v
    om = Fraction(rng.randint(3, 9), rng.randint(2, 5))          # Omega^2 > 0
    dom = [Fraction(rng.randint(-4, 4), rng.randint(1, 4)) for _ in range(D)]
    ddom = [[Fraction(0)] * D for _ in range(D)]
    for mu in range(D):
        for nu in range(mu, D):
            v = Fraction(rng.randint(-4, 4), rng.randint(1, 4))
            ddom[mu][nu] = ddom[nu][mu] = v
    return dict(gbar=gbar, dg=dg, ddg=ddg, om=om, dom=dom, ddom=ddom)

# --------------------------------------------------------------------------
# ring-generic geometry engine from a single point's jet data
# --------------------------------------------------------------------------

def christoffel(ginv, dg, D, h):
    G = [[[h * sum(ginv[lam][rho] *
                   (dg[mu][nu][rho] + dg[nu][mu][rho] - dg[rho][mu][nu])
                   for rho in range(D))
           for nu in range(D)] for mu in range(D)] for lam in range(D)]
    return G

def dchristoffel(ginv, dginv, dg, ddg, D, h):
    dG = [[[[h * (sum(dginv[sig][lam][rho] *
                      (dg[mu][nu][rho] + dg[nu][mu][rho] - dg[rho][mu][nu])
                      for rho in range(D))
                  + sum(ginv[lam][rho] *
                        (ddg[sig][mu][nu][rho] + ddg[sig][nu][mu][rho]
                         - ddg[sig][rho][mu][nu])
                        for rho in range(D)))
            for nu in range(D)] for mu in range(D)] for lam in range(D)]
         for sig in range(D)]
    return dG

def riemann(dG, G, D):
    R = [[[[dG[mu][rho][nu][sig] - dG[nu][rho][mu][sig]
           + sum(G[rho][mu][lam] * G[lam][nu][sig]
                 - G[rho][nu][lam] * G[lam][mu][sig] for lam in range(D))
           for nu in range(D)] for mu in range(D)] for sig in range(D)]
      for rho in range(D)]
    return R

def engine(D, jb):
    """Compute every object needed by CT1.13–CT1.17 from jet data `jb`.
    Ring is inferred from jb entries (Fraction or Series2)."""
    gbar, dg, ddg = jb["gbar"], jb["dg"], jb["ddg"]
    om, dom, ddom = jb["om"], jb["dom"], jb["ddom"]
    proto = gbar[0][0]
    z, o, h = zero(proto), one(proto), half(proto)

    # Omega-potential derivatives:  Ups_mu = w_mu/(2w);  Ups_{,mu nu}
    omInv = o / om
    Ups = [dom[mu] * h * omInv for mu in range(D)]
    # Upsilon = ln Omega = (1/2) ln omega  =>  U_{,mu} = w_mu/(2w),
    # U_{,mu nu} = w_{mu nu}/(2w) - w_mu w_nu/(2w^2)
    Ups2 = [[h * (ddom[mu][nu] * omInv - dom[mu] * dom[nu] * omInv * omInv)
             for nu in range(D)] for mu in range(D)]

    # g = omega * gbar and its jet (product rule)
    g = [[om * gbar[mu][nu] for nu in range(D)] for mu in range(D)]
    dgG = [[[dom[r] * gbar[mu][nu] + om * dg[r][mu][nu]
             for nu in range(D)] for mu in range(D)] for r in range(D)]
    ddgG = [[[[ddom[r][s2] * gbar[mu][nu] + dom[r] * dg[s2][mu][nu]
               + dom[s2] * dg[r][mu][nu] + om * ddg[r][s2][mu][nu]
               for nu in range(D)] for mu in range(D)] for s2 in range(D)]
            for r in range(D)]

    gbar_inv = matinv(gbar)
    ginv = matinv(g)
    # CT1.13 step 1:  g^{mu nu} = Omega^{-2} gbar^{mu nu} = omega^{-1} gbar^{mu nu}
    ginv_consistent = teq(ginv, matscale(gbar_inv, omInv))

    dginvBar = [[[ -sum(gbar_inv[lam][a] * gbar_inv[rho][b] * dg[sig][a][b]
                   for a in range(D) for b in range(D))
                 for rho in range(D)] for lam in range(D)] for sig in range(D)]
    dginvG = [[[ -sum(ginv[lam][a] * ginv[rho][b] * dgG[sig][a][b]
                   for a in range(D) for b in range(D))
                 for rho in range(D)] for lam in range(D)] for sig in range(D)]

    GamBar = christoffel(gbar_inv, dg, D, h)
    Gam = christoffel(ginv, dgG, D, h)
    dGamBar = dchristoffel(gbar_inv, dginvBar, dg, ddg, D, h)
    dGam = dchristoffel(ginv, dginvG, dgG, ddgG, D, h)

    RiemBar = riemann(dGamBar, GamBar, D)
    Riem = riemann(dGam, Gam, D)

    RicciBar = [[sum(RiemBar[rho][sig][rho][nu] for rho in range(D))
                 for nu in range(D)] for sig in range(D)]
    Ricci = [[sum(Riem[rho][sig][rho][nu] for rho in range(D))
              for nu in range(D)] for sig in range(D)]
    ScalBar = sum(gbar_inv[mu][nu] * RicciBar[mu][nu]
                  for mu in range(D) for nu in range(D))
    Scal = sum(ginv[mu][nu] * Ricci[mu][nu] for mu in range(D) for nu in range(D))
    EinsBar = [[RicciBar[mu][nu] - h * gbar[mu][nu] * ScalBar
                for nu in range(D)] for mu in range(D)]
    Eins = [[Ricci[mu][nu] - h * g[mu][nu] * Scal
             for nu in range(D)] for mu in range(D)]

    # Upsilon-derived barred objects
    UpsUp = [sum(gbar_inv[rho][lam] * Ups[lam] for lam in range(D))
             for rho in range(D)]
    Hess = [[Ups2[mu][nu] - sum(GamBar[lam][mu][nu] * Ups[lam] for lam in range(D))
             for nu in range(D)] for mu in range(D)]
    BoxU = sum(gbar_inv[mu][nu] * Hess[mu][nu]
               for mu in range(D) for nu in range(D))
    Grad2 = sum(gbar_inv[mu][nu] * Ups[mu] * Ups[nu]
                for mu in range(D) for nu in range(D))

    # C^rho_{mu nu} and its barred-covariant derivative
    delta = lambda a, b: from_frac(proto, 1 if a == b else 0)
    Cdiff = [[[delta(rho, mu) * Ups[nu] + delta(rho, nu) * Ups[mu]
               - gbar[mu][nu] * UpsUp[rho]
               for nu in range(D)] for mu in range(D)] for rho in range(D)]
    dUpsUp = [[sum(dginvBar[a][rho][lam] * Ups[lam] for lam in range(D))
               + sum(gbar_inv[rho][lam] * Ups2[lam][a] for lam in range(D))
               for rho in range(D)] for a in range(D)]
    dC = [[[[delta(rho, mu) * Ups2[nu][a] + delta(rho, nu) * Ups2[mu][a]
             - dg[a][mu][nu] * UpsUp[rho] - gbar[mu][nu] * dUpsUp[a][rho]
             for nu in range(D)] for mu in range(D)] for rho in range(D)]
          for a in range(D)]
    nabC = [[[[dC[a][rho][mu][nu]
               + sum(GamBar[rho][a][lam] * Cdiff[lam][mu][nu] for lam in range(D))
               - sum(GamBar[lam][a][mu] * Cdiff[rho][lam][nu] for lam in range(D))
               - sum(GamBar[lam][a][nu] * Cdiff[rho][mu][lam] for lam in range(D))
               for nu in range(D)] for mu in range(D)] for rho in range(D)]
            for a in range(D)]

    return dict(ginv_consistent=ginv_consistent, Gam=Gam, GamBar=GamBar,
                Ups=Ups, UpsUp=UpsUp, gbar=gbar, Ricci=Ricci, RicciBar=RicciBar,
                Scal=Scal, ScalBar=ScalBar, Eins=Eins, EinsBar=EinsBar,
                Hess=Hess, BoxU=BoxU, Grad2=Grad2, Riem=Riem, RiemBar=RiemBar,
                Cdiff=Cdiff, nabC=nabC, omInv=omInv, D=D, proto=proto)

# --------------------------------------------------------------------------
# CT1.13 – CT1.17 : conformal identities, exact, general D
# --------------------------------------------------------------------------

def check_conformal_identities(D, seeds):
    delta_ok = True
    names = {13: "CT1.13", 14: "CT1.14", 15: "CT1.15", 16: "CT1.16", 17: "CT1.17"}
    results = {k: True for k in names}
    results_ginv = True
    for seed in seeds:
        jb = gen_jet(D, seed)
        try:
            t = engine(D, jb)
        except ZeroDivisionError:
            continue                     # degenerate draw; regenerate via other seed
        results_ginv &= t["ginv_consistent"]
        gbar, Ups, UpsUp = t["gbar"], t["Ups"], t["UpsUp"]
        Gam, GamBar = t["Gam"], t["GamBar"]
        Hess, BoxU, Grad2 = t["Hess"], t["BoxU"], t["Grad2"]
        o, h = one(t["proto"]), half(t["proto"])
        df = lambda k: from_frac(t["proto"], k)

        # CT1.13
        for lam in range(D):
            for mu in range(D):
                for nu in range(D):
                    lhs = Gam[lam][mu][nu] - GamBar[lam][mu][nu]
                    rhs = ((o if lam == mu else 0) * Ups[nu]
                           + (o if lam == nu else 0) * Ups[mu]
                           - gbar[mu][nu] * UpsUp[lam])
                    delta_ok &= (lhs == rhs)

        # CT1.14
        Cdiff, nabC = t["Cdiff"], t["nabC"]
        r14 = True
        for rho in range(D):
            for sig in range(D):
                for mu in range(D):
                    for nu in range(D):
                        lhs = t["Riem"][rho][sig][mu][nu]
                        rhs = (t["RiemBar"][rho][sig][mu][nu]
                               + nabC[mu][rho][nu][sig] - nabC[nu][rho][mu][sig]
                               + sum(Cdiff[rho][mu][lam2] * Cdiff[lam2][nu][sig]
                                     - Cdiff[rho][nu][lam2] * Cdiff[lam2][mu][sig]
                                     for lam2 in range(D)))
                        r14 &= (lhs == rhs)
        results[14] &= r14

        # CT1.15  (general D)
        r15 = True
        for mu in range(D):
            for nu in range(D):
                lhs = t["Ricci"][mu][nu]
                rhs = (t["RicciBar"][mu][nu]
                       - df(D - 2) * Hess[mu][nu]
                       - gbar[mu][nu] * BoxU
                       + df(D - 2) * (Ups[mu] * Ups[nu] - gbar[mu][nu] * Grad2))
                r15 &= (lhs == rhs)
        results[15] &= r15

        # CT1.16  (general D)
        rhs16 = t["omInv"] * (t["ScalBar"]
                              - df(2 * (D - 1)) * BoxU
                              - df((D - 1) * (D - 2)) * Grad2)
        results[16] &= (t["Scal"] == rhs16)

        # CT1.17  (D = 4 only)
        if D == 4:
            r17 = True
            for mu in range(D):
                for nu in range(D):
                    lhs = t["Eins"][mu][nu]
                    rhs = (t["EinsBar"][mu][nu]
                           - df(2) * Hess[mu][nu]
                           + df(2) * gbar[mu][nu] * BoxU
                           + df(2) * Ups[mu] * Ups[nu]
                           + gbar[mu][nu] * Grad2)
                    r17 &= (lhs == rhs)
            results[17] &= r17

    results[13] = delta_ok
    check(f"D={D}  g^{{mu nu}} = Omega^-2 gbar^{{mu nu}} (CT1.13 step 1)", results_ginv)
    for k in (13, 14, 15, 16) + ((17,) if D == 4 else ()):
        check(f"D={D}  {names[k]} exact conformal identity", results[k])

# --------------------------------------------------------------------------
# CT1.12 : Schur identity, signature, traceless split
# --------------------------------------------------------------------------

def check_ct1_12():
    rng = random.Random(12345)
    # traceless split
    q = [[Fraction(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(i, 3):
            v = Fraction(rng.randint(-3, 3), 2)
            q[i][j] = q[j][i] = v
    tr = sum(q[i][i] for i in range(3))
    hhat = [[q[i][j] - (Fraction(1, 3) if i == j else 0) * tr for j in range(3)]
            for i in range(3)]
    check("CT1.12  delta^ij hhat_ij = 0 (exact traceless split)",
          sum(hhat[i][i] for i in range(3)) == 0)

    # Schur determinant identity + signature, over many random draws
    kap = Fraction(1, 2)
    ok_schur = True
    ok_sig = True
    ok_conf = True
    for t in range(30):
        qq = [[Fraction(0)] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(i, 3):
                v = Fraction(rng.randint(-2, 2), rng.randint(4, 8))   # small => gbar_ij pos-def
                qq[i][j] = qq[j][i] = v
        gij = [[(Fraction(1) if i == j else Fraction(0)) + kap * qq[i][j]
                for j in range(3)] for i in range(3)]
        N = [Fraction(rng.randint(-3, 3), 2) for _ in range(3)]
        g4 = [[Fraction(0)] * 4 for _ in range(4)]
        g4[0][0] = Fraction(-1)
        for i in range(3):
            g4[0][i + 1] = kap * N[i]
            g4[i + 1][0] = kap * N[i]
        for i in range(3):
            for j in range(3):
                g4[i + 1][j + 1] = gij[i][j]
        gij_inv = matinv(gij)
        quad = sum(N[i] * gij_inv[i][j] * N[j] for i in range(3) for j in range(3))
        ok_schur &= (matdet(g4) == matdet(gij) * (Fraction(-1) - kap * kap * quad))
        # Sylvester: gij positive definite <=> all leading minors > 0
        for k in (1, 2, 3):
            ok_sig &= matdet([row[:k] for row in gij[:k]]) > 0
        # full gbar: signature (-,+,+,+) <=> leading minors D1..D4 all < 0
        # (sequence 1, D1, D2, D3, D4 has exactly one sign change)
        minors = [matdet([row[:k] for row in g4[:k]]) for k in (1, 2, 3, 4)]
        ok_sig &= all(m < 0 for m in minors)
        # conformal rescaling by omega > 0: D_k -> omega^k D_k, signs preserved
        om = Fraction(rng.randint(2, 7), rng.randint(1, 3))
        g4c = matscale(g4, om)
        minors_c = [matdet([row[:k] for row in g4c[:k]]) for k in (1, 2, 3, 4)]
        ok_conf &= all((mc < 0) == (m < 0) for mc, m in zip(minors_c, minors))
    check("CT1.12  Schur: det gbar = det(gbar_ij) * (-1 - kap^2 N gbar_ij^-1 N)", ok_schur)
    check("CT1.12  gbar_ij pos-def & sig(gbar) = (-,+,+,+) (Sylvester)", ok_sig)
    check("CT1.12  omega > 0 preserves signature signs", ok_conf)

# --------------------------------------------------------------------------
# CT1.18 : Series2 linearization about eta + kap*hhat, Omega = 1
# --------------------------------------------------------------------------

def gen_hhat_jet(seed):
    """(hhat, d hhat, dd hhat) over Fraction; hhat symmetric, eta-traceless."""
    rng = random.Random(seed)
    D = 4
    h = [[Fraction(0)] * D for _ in range(D)]
    for i in range(1, D):
        for j in range(i, D):
            v = Fraction(rng.randint(-3, 3), 2)
            h[i][j] = h[j][i] = v
    for i in range(1, D):
        v = Fraction(rng.randint(-3, 3), 2)
        h[0][i] = h[i][0] = v
    h[0][0] = sum(h[i][i] for i in range(1, D))     # -h00 + sum hii = 0
    dh = [[[Fraction(0)] * D for _ in range(D)] for _ in range(D)]
    for a in range(D):
        for mu in range(D):
            for nu in range(mu, D):
                v = Fraction(rng.randint(-3, 3), 3)
                dh[a][mu][nu] = dh[a][nu][mu] = v
    ddh = [[[[Fraction(0)] * D for _ in range(D)] for _ in range(D)]
           for _ in range(D)]
    # orbit fill: ddh[a][b][mu][nu] symmetric under a<->b, mu<->nu AND pair
    # exchange (a,b)<->(mu,nu)  (all true for jets of a smooth symmetric tensor)
    seen = set()
    for a in range(D):
        for b in range(D):
            for mu in range(D):
                for nu in range(D):
                    orbit = {(a, b, mu, nu), (b, a, mu, nu),
                             (a, b, nu, mu), (b, a, nu, mu),
                             (mu, nu, a, b), (mu, nu, b, a),
                             (nu, mu, a, b), (nu, mu, b, a)}
                    rep = min(orbit)
                    if rep in seen:
                        continue
                    seen |= orbit
                    v = Fraction(rng.randint(-3, 3), 3)
                    for (p, q, r, s2) in orbit:
                        ddh[p][q][r][s2] = v
    return h, dh, ddh

def L_linear(ddh, D=4):
    """L[hhat]_{mu nu} = 1/2(-Box h + d_mu d^l h_{nu l} + d_nu d^l h_{mu l}
                             - eta_{mu nu} d^l d^s h_{ls}),  traceless input."""
    sgn = [-1] + [1] * (D - 1)
    eta = eta_D(D)
    halfF = Fraction(1, 2)
    out = [[Fraction(0)] * D for _ in range(D)]
    for mu in range(D):
        for nu in range(D):
            box = sum(sgn[a] * ddh[a][a][mu][nu] for a in range(D))
            t3 = sum(sgn[l] * ddh[mu][l][nu][l] for l in range(D))
            t4 = sum(sgn[l] * ddh[nu][l][mu][l] for l in range(D))
            divdiv = sum(sgn[l] * sgn[s2] * ddh[l][s2][l][s2]
                         for l in range(D) for s2 in range(D))
            out[mu][nu] = halfF * (-box + t3 + t4 - eta[mu][nu] * divdiv)
    return out

def G1_full(ddh, D=4):
    """FULL linearized Einstein tensor as a function of dd-h only."""
    sgn = [-1] + [1] * (D - 1)
    eta = eta_D(D)
    halfF = Fraction(1, 2)
    out = [[Fraction(0)] * D for _ in range(D)]
    for mu in range(D):
        for nu in range(D):
            box = sum(sgn[a] * ddh[a][a][mu][nu] for a in range(D))
            dm_dnu_tr = sum(sgn[l] * ddh[mu][nu][l][l] for l in range(D))
            t3 = sum(sgn[l] * ddh[mu][l][nu][l] for l in range(D))
            t4 = sum(sgn[l] * ddh[nu][l][mu][l] for l in range(D))
            box_tr = sum(sgn[l] * sgn[a] * ddh[a][a][l][l]
                         for l in range(D) for a in range(D))
            divdiv = sum(sgn[l] * sgn[s2] * ddh[l][s2][l][s2]
                         for l in range(D) for s2 in range(D))
            out[mu][nu] = halfF * (-box - dm_dnu_tr + t3 + t4
                                   + eta[mu][nu] * (box_tr - divdiv))
    return out

def check_ct1_18():
    D = 4
    sgn = [-1, 1, 1, 1]
    eta = eta_D(D)
    ok_lin = True
    ok_a0 = True
    ok_gauge_std = True
    ok_proj_shift = True
    def constrain_ddh(ddh0):
        """Impose the jet-level consequence of eta^{mu nu} hhat_{mu nu}(x) = 0:
        sum_l s_l ddh[a][b][l][l] = 0 for every (a,b). Dependent components:
        second-pair (0,0) and first-pair (0,0); everything else stays free."""
        out = [[[[ddh0[a][b][mu][nu] for nu in range(D)] for mu in range(D)]
                for b in range(D)] for a in range(D)]
        for a in range(D):
            for b in range(D):
                if (a, b) != (0, 0):
                    out[a][b][0][0] = sum(out[a][b][l][l] for l in range(1, D))
        for mu in range(D):
            for nu in range(D):
                if (mu, nu) != (0, 0):
                    out[0][0][mu][nu] = sum(out[mu][nu][l][l] for l in range(1, D))
        out[0][0][0][0] = sum(out[0][0][l][l] for l in range(1, D))
        # verify constraints + symmetries exactly
        for a in range(D):
            for b in range(D):
                assert sum(sgn[l] * out[a][b][l][l] for l in range(D)) == 0
                for mu in range(D):
                    for nu in range(D):
                        assert out[a][b][mu][nu] == out[b][a][mu][nu]
                        assert out[a][b][mu][nu] == out[a][b][nu][mu]
                        assert out[a][b][mu][nu] == out[mu][nu][a][b]
        return out

    for seed in (11, 22, 33):
        h, dh, ddh_raw = gen_hhat_jet(seed)
        ddh = constrain_ddh(ddh_raw)
        # Series2 jets: gbar = eta + eps*h, omega = 1
        gbarS = [[Series2(eta[mu][nu], h[mu][nu], 0) for nu in range(D)]
                 for mu in range(D)]
        dgS = [[[Series2(0, dh[a][mu][nu], 0) for nu in range(D)]
                for mu in range(D)] for a in range(D)]
        ddgS = [[[[Series2(0, ddh[a][b][mu][nu], 0) for nu in range(D)]
                  for mu in range(D)] for b in range(D)] for a in range(D)]
        jbS = dict(gbar=gbarS, dg=dgS, ddg=ddgS,
                   om=Series2(1), dom=[Series2(0)] * D,
                   ddom=[[Series2(0)] * D for _ in range(D)])
        t = engine(D, jbS)
        Lexp = L_linear(ddh)
        for mu in range(D):
            for nu in range(D):
                e = t["Eins"][mu][nu]
                ok_a0 &= (e.a[0] == 0)
                ok_lin &= (e.a[1] == Lexp[mu][nu])
    check("CT1.18  Gbar_{mu nu}|_{O(kap^0)} = 0 (exact Series2 linearization)", ok_a0)
    check("CT1.18  Gbar_{mu nu}|_{O(kap^1)} = L[hhat] (wave-operator form)", ok_lin)

    # gauge invariance of the FULL linearized tensor under h -> h + d xi + d xi
    rng = random.Random(777)
    ddh = gen_hhat_jet(5)[2]

    def rand_d3():
        d3 = [[[[Fraction(0)] * D for _ in range(D)] for _ in range(D)]
              for _ in range(D)]
        for a in range(D):
            for b in range(a, D):
                for c in range(b, D):
                    for d in range(D):
                        v = Fraction(rng.randint(-3, 3), 2)
                        for p in ((a, b, c), (a, c, b), (b, a, c),
                                  (b, c, a), (c, a, b), (c, b, a)):
                            d3[p[0]][p[1]][p[2]][d] = v
        return d3

    def delta_std(d3):
        Dl = [[[[d3[a][b][mu][nu] + d3[a][b][nu][mu]
                 for nu in range(D)] for mu in range(D)] for b in range(D)]
              for a in range(D)]
        return Dl

    def delta_proj(d3):
        Dl = delta_std(d3)
        out = [[[[Dl[a][b][mu][nu]
                  - Fraction(1, 2) * eta[mu][nu]
                  * sum(sgn[r] * d3[a][b][r][r] for r in range(D))
                  for nu in range(D)] for mu in range(D)] for b in range(D)]
               for a in range(D)]
        return out

    def ddf(d3):
        """second partials of f = d.xi from d3: f_{,ab} = sum_r s_r d3[a][b][r][r]"""
        return [[sum(sgn[r] * d3[a][b][r][r] for r in range(D))
                 for b in range(D)] for a in range(D)]

    base = G1_full(ddh)
    for trial in range(6):
        d3 = rand_d3()
        dd_std = [[[[ddh[a][b][mu][nu] + delta_std(d3)[a][b][mu][nu]
                     for nu in range(D)] for mu in range(D)] for b in range(D)]
                  for a in range(D)]
        ok_gauge_std &= teq(G1_full(dd_std), base)
        dd_pr = [[[[ddh[a][b][mu][nu] + delta_proj(d3)[a][b][mu][nu]
                    for nu in range(D)] for mu in range(D)] for b in range(D)]
                  for a in range(D)]
        fp = ddf(d3)                                  # f_{,ab} = (d.xi)_{,ab}
        boxf = sum(sgn[a] * fp[a][a] for a in range(D))
        shift = G1_full(dd_pr)
        expected = [[base[mu][nu]
                     + Fraction(1, 2) * fp[mu][nu]
                     - Fraction(1, 2) * eta[mu][nu] * boxf
                     for nu in range(D)] for mu in range(D)]
        ok_proj_shift &= teq(shift, expected)
    check("CT1.18  G1[h + d_mu xi_nu + d_nu xi_mu] = G1[h] (standard gauge, exact)",
          ok_gauge_std)
    check("CT1.18  projected variant shifts by 1/2 (f_{,mu nu} - eta_{mu nu} Box f), "
          "f = d.xi  (old codex step-6 invariance claim FALSE; corrected)", ok_proj_shift)

# --------------------------------------------------------------------------
# CT2.10 : supertrace identities (exact Fractions)
# --------------------------------------------------------------------------

def check_ct2_10():
    rng = random.Random(4242)
    m, n = 2, 3                        # even-block sizes (distinct on purpose)
    def rmat(r, c):
        return [[Fraction(rng.randint(-4, 4), 3) for _ in range(c)]
                for _ in range(r)]
    def Str(M, m, n):
        return (sum(M[i][i] for i in range(m))
                - sum(M[m + j][m + j] for j in range(n)))
    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
                 for j in range(len(B[0]))] for i in range(len(A))]
    def graded(X, Y, ex, ey, m, n):
        out = [[Fraction(0)] * (m + n) for _ in range(m + n)]
        A, B = mm(X, Y), mm(Y, X)
        return Str(A, m, n) - ((-1) ** (ex * ey)) * Str(B, m, n)
    ok = True
    ok2 = True
    for _ in range(12):
        Be, Fe = rmat(m, m), rmat(n, n)
        Bo, Fo = rmat(m, m), rmat(n, n)
        Qx, Rx = rmat(m, n), rmat(n, m)
        Qy, Ry = rmat(m, n), rmat(n, m)
        def assemble(B, Q, R, F):
            M = [[Fraction(0)] * (m + n) for _ in range(m + n)]
            for i in range(m):
                for j in range(m): M[i][j] = B[i][j]
            for i in range(m):
                for j in range(n): M[i][m + j] = Q[i][j]
            for i in range(n):
                for j in range(m): M[m + i][j] = R[i][j]
            for i in range(n):
                for j in range(n): M[m + i][m + j] = F[i][j]
            return M
        X_even = assemble(Be, [[Fraction(0)] * n for _ in range(m)],
                          [[Fraction(0)] * m for _ in range(n)], Fe)
        Y_even = assemble(Bo, [[Fraction(0)] * n for _ in range(m)],
                          [[Fraction(0)] * m for _ in range(n)], Fo)
        X_odd = assemble([[Fraction(0)] * m for _ in range(m)], Qx, Rx,
                         [[Fraction(0)] * n for _ in range(n)])
        Y_odd = assemble([[Fraction(0)] * m for _ in range(m)], Qy, Ry,
                         [[Fraction(0)] * n for _ in range(n)])
        ok &= graded(X_even, Y_even, 0, 0, m, n) == 0
        ok &= graded(X_even, X_odd, 0, 1, m, n) == 0
        ok &= graded(X_odd, X_even, 1, 0, m, n) == 0
        ok &= graded(X_odd, Y_odd, 1, 1, m, n) == 0
        # Str[X,Y} = Str(XY) - (-1)^{XY} Str(YX) is exactly `graded` == 0 above
        # and additionally Str of a single graded commutator matrix:
        XY = mm(X_odd, Y_odd)
        YX = mm(Y_odd, X_odd)
        comm = [[XY[i][j] + YX[i][j] for j in range(m + n)]
                for i in range(m + n)]           # {X,Y} = XY + YX (|X||Y| = 1)
        ok2 &= Str(comm, m, n) == 0
    check("CT2.10  Str(XY) = (-1)^{|X||Y|} Str(YX), all parities (Str[X,Y} = 0)", ok)
    check("CT2.10  Str{X_odd,Y_odd} = 0", ok2)

# --------------------------------------------------------------------------
# CT2.1 / CT2.9 / CT1.29 : exact rational bookkeeping
# --------------------------------------------------------------------------

def check_units_and_calibration():
    # CT2.1: [q]-exponents as exact Fractions
    h = Fraction(-1, 2)              # [h] = q^{-1/2}
    length = h
    area = 2 * h
    energy = -length                 # hbar = c = 1
    volume = 3 * length
    T = energy - volume              # energy density
    curv = -area                     # inverse area
    kap2 = curv - T                  # [kappa^2] from kappa^2 T = G
    action = 4 * length + curv - kap2   # d^4x * R * kappa^{-2};  sqrt(-g) dimless
    ok = (T == 2 and curv == 1 and kap2 == -1 and action == 0
          and 2 * h == -1)
    check("CT2.1   [T]=q^+2, [G]=[Lambda]=q^+1, [kappa^2]=[G_N]=q^-1, [S]=q^0", ok)

    # CT2.9 / CT1.29: rational identities in the indeterminates (h2, ln2, pi, A, n)
    rng = random.Random(31337)
    ok9 = True
    ok29 = True
    for _ in range(20):
        h2 = Fraction(rng.randint(1, 50), rng.randint(1, 7))
        ln2 = Fraction(rng.randint(1, 9), rng.randint(1, 5))     # stands in for ln 2
        pi = Fraction(rng.randint(1, 9), rng.randint(1, 5))      # stands in for pi
        A = Fraction(rng.randint(1, 40), rng.randint(1, 3))
        GN = h2 / (4 * ln2)
        kap2v = 8 * pi * GN
        ok9 &= (kap2v == 2 * pi * h2 / ln2)
        S = A * ln2 / h2                                         # CT1.29
        ok9 &= (S == A / (4 * GN))                               # quarter-area form
        n = Fraction(rng.randint(0, 30), 1)
        S29 = n * ln2
        A29 = n * h2
        ok29 &= (S29 == A29 * ln2 / h2)
    check("CT2.9   h^2 = 4 G_N ln2 <=> S = A/(4 G_N); kappa^2 = 8 pi G_N = 2 pi h^2/ln2", ok9)
    check("CT1.29  S = n ln2 = (A/h^2) ln2 with A = n h^2", ok29)

# --------------------------------------------------------------------------

def main():
    print("verify_C: exact geometry checks (document C)")
    check_conformal_identities(3, seeds=(101, 202, 303, 404))
    check_conformal_identities(4, seeds=(1, 2, 3, 4, 5))
    check_conformal_identities(5, seeds=(11, 22, 33))
    check_ct1_12()
    check_ct1_18()
    check_ct2_10()
    check_units_and_calibration()
    print()
    if FAILURES:
        print(f"verify_C: {len(FAILURES)} FAILURE(S): {FAILURES}")
        return 1
    print("verify_C: ALL CHECKS PASS (exact arithmetic)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
