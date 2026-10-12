#!/usr/bin/env python3
"""verify_CT10_signature.py — machine verification of CT1.0 (Part 1, Tier 1A),
C13 (Part 1 §B) and the revised A3 (the signature de-axiomatization).

Sections:
  §A  document pins: the revised A3 sign-structure display, C13, the CT1.0
      block (Thm/Req/Pf/Phys/Rmk, proof terminator), the CT1.1/CT1.2 Req and
      Pf representative lines, the §D symbol rows, and the absence of the
      former axiomatic literal eta = (-,+,+,+)
  §B  clause (1): the admissible sign vectors are exactly the eight
      +/- eta^(o), o unique, sign unique (exhaustive over {+/-1}^4)
  §C  clause (2): T[eta] = T[-eta] on all 16 index pairs; T = D_zeta (x) D_zeta
      via zeta_mu zeta_nu = eta^mu eta^nu (exact integers)
  §D  clause (3): [S,T] = 0 and the sector census (7,3,3,3) for every o
  §E  clause (4): o=0 gives D_zeta = sf (spin flip); o=k reflects Bloch axis k;
      T^(1)~T^(2)~T^(3) via the exact rational unitary U_c = (1 - i(S1+S2+S3))/2
      (Ad_{U_c}: s1->s2->s3->s1, verified over Q(i)); T^(0) is conjugate to
      none: the traceless-block char polys (x+1)^3 vs (x-1)^2(x+1) differ
  §F  clause (5): (<=) as POLYNOMIAL IDENTITIES over Q(i)[a,b,c,d] for the
      generic U = [[alpha, beta], [-conj(beta), conj(alpha)]],
      alpha = a+bi, beta = c+di:  sigma2 U^T sigma2 = U^dagger,
      sigma2 conj(U) sigma2 = U, and sf(U s_mu U^dagger) = U sf(s_mu) U^dagger
      for all four Pauli matrices (the tensor lift to sf(x)sf gives (<=) on
      the 16-basis; exhibited additionally at the exact rational point
      a=3/5, b=4/5, c=d=0).  (=>) via U_c: [T, Ad_{U_c (x) U_c}] = 0 on the
      16-basis  <=>  eta^1 = eta^2 = eta^3  <=>  o = 0 (all eight eta).
  §G  the Rmk census: CT1.2's 17-generator sector table re-evaluated at all
      four o; at o=1 exactly W2,W3 move to E_++, J2,J3 to E_--, K2,K3 to
      E_-+, E^12,E^13 to E_+-, and only W1,J1,K1 stay; symmetric at o=2,3.

Arithmetic: integers, fractions.Fraction, complex-over-Fraction (hcommon.QI),
and an exact polynomial ring over QI in four real variables. No floating
point in any assertion.
"""
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import era_paths
from hcommon import QI

FAILS = []


def chk(cond, msg):
    if cond:
        print(f"  PASS  {msg}")
    else:
        FAILS.append(msg)
        print(f"  FAIL  {msg}")
    return cond


# ---------------------------------------------------------------- matrices
def mat(rows):
    return [list(r) for r in rows]


def m_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def m_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def m_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), ZERO) for j in range(p)]
            for i in range(n)]


def m_T(A):
    return [list(r) for r in zip(*A)]


def m_dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def m_scale(c, A):
    cc = c if isinstance(c, QI) else QI(c)
    return [[cc * x for x in row] for row in A]


def m_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def kron(A, B):
    return [[A[i // 2][k // 2] * B[i % 2][k % 2] for k in range(4)] for i in range(4)]


ONE = QI(1)
ZERO = QI(0)
IM = QI(0, 1)
SIG = [
    mat([[ONE, ZERO], [ZERO, ONE]]),
    mat([[ZERO, ONE], [ONE, ZERO]]),
    mat([[ZERO, -IM], [IM, ZERO]]),
    mat([[ONE, ZERO], [ZERO, -ONE]]),
]
SIG2 = SIG[2]


def sf(X):
    return m_mul(SIG2, m_mul(m_T(X), SIG2))


# ---------------------------------------------------------------- polynomials over QI
class Poly:
    """exact polynomial in (a,b,c,d) with QI coefficients"""
    __slots__ = ("t",)

    def __init__(self, terms=None):
        self.t = {}
        if terms:
            for k, v in terms.items():
                if v != ZERO:
                    self.t[k] = self.t.get(k, ZERO) + v

    @staticmethod
    def const(z):
        zz = z if isinstance(z, QI) else QI(z)
        return Poly({(0, 0, 0, 0): zz}) if zz != ZERO else Poly()

    @staticmethod
    def var(i, z=1):
        e = [0, 0, 0, 0]
        e[i] = 1
        return Poly({tuple(e): QI(z, 0) if isinstance(z, int) and z == 1 else QI(z)})

    def __add__(self, o):
        if isinstance(o, int):
            o = Poly() if o == 0 else Poly.const(QI(o))
        r = Poly(self.t)
        for k, v in o.t.items():
            nv = r.t.get(k, ZERO) + v
            if nv == ZERO:
                r.t.pop(k, None)
            else:
                r.t[k] = nv
        return r

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        r = Poly()
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                k = tuple(x + y for x, y in zip(k1, k2))
                nv = r.t.get(k, ZERO) + v1 * v2
                if nv == ZERO:
                    r.t.pop(k, None)
                else:
                    r.t[k] = nv
        return r

    def conj(self):
        return Poly({k: v.conj() for k, v in self.t.items()})

    def is_zero(self):
        return not self.t


def pm(rows):
    return [list(r) for r in rows]


def pm_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j]) for k in range(m)) for j in range(p)] for i in range(n)]


def pm_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def pm_T(A):
    return [list(r) for r in zip(*A)]


def pm_conj(A):
    return [[x.conj() for x in row] for row in A]


def pm_dag(A):
    return pm_conj(pm_T(A))


def pm_zero(A):
    return all(x.is_zero() for row in A for x in row)


# ---------------------------------------------------------------- §A document pins
def section_A():
    print("§A — document pins (Part 1: revised A3, C13, CT1.0, CT1.1/CT1.2 edits)")
    P1 = era_paths.read("B_foundation.md")
    chk("\\eta\\in\\{\\pm1\\}^4" in P1, "§A A3 carries the sign-vector condition eta in {+/-1}^4")
    chk("\\exists!\\,\\mathfrak o\\in\\{0,1,2,3\\}" in P1, "§A A3 carries the unique-odd-slot condition")
    chk("\\eta=(-,+,+,+),\\quad T^2=\\mathbb1" not in P1, "§A the former axiomatic literal eta=(-,+,+,+) is gone from A3")
    chk("**C13.** Signature convention." in P1, "§A C13 is declared (signature convention)")
    chk("The corpus takes $\\mathfrak o:=0$" in P1 and "$\\eta^{0}:=-1$" in P1, "§A C13 fixes o:=0 and eta^0:=-1 (mostly-plus)")
    chk("### CT1.0 — Signature classification of the $T$-grading" in P1, "§A CT1.0 block present")
    i0 = P1.index("### CT1.0")
    i1 = P1.index("### CT1.1", i0)
    blk = P1[i0:i1]
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§A CT1.0 carries {mark}")
    chk("**Req.** A3; C1;" in blk, "§A CT1.0 Req = A3; C1; [math] (no prior theorem)")
    chk("checks/verify_CT10_signature.py" in blk, "§A the CT1.0 Rmk cites this checker")
    chk("**Req.** A3, C13; C3; CT1.0; Pauli basis facts:" in P1, "§A CT1.1 Req cites A3, C13 and CT1.0")
    chk("\\eta:=(-,+,+,+)\\ [\\mathrm{C13}]:" in P1, "§A CT1.1 Pf names the representative under C13")
    chk("**Req.** A3, C1, C3, C13; CT1.0, CT1.1." in P1, "§A CT1.2 Req cites A3, C1, C3, C13; CT1.0, CT1.1")
    for j in ("\\eta^i\\eta^j=+1\\ [\\mathrm{C13}]", "\\eta^0\\eta^i=-1\\ [\\mathrm{C13}]"):
        chk(j in P1, f"§A CT1.2 Pf justification carries [C13]: {j[:34]}...")
    chk("| $\\mathfrak o$, $\\eta^{(\\mathfrak o)}$ |" in P1, "§A §D symbol row for o / eta^(o)")
    chk("| $\\zeta_i$, $\\mathsf D_\\zeta$, $\\mathrm{sf}$ |" in P1, "§A §D symbol row for zeta / D_zeta / sf")
    chk("sign-grading involution ($T=\\mathsf D_\\zeta\\otimes\\mathsf D_\\zeta$; metric-sign reading: C13)" in P1, "§A §D row S,T updated")
    chk("the representative $\\eta=(-,+,+,+)$ [C13] of A3's sign vector" in P1, "§A CT1.11b native-frames clause updated")
    chk("\\vartheta_a\\vartheta_b" in P1 and "\\eta_a\\eta_b" not in P1, "§A L5 uses vartheta_a vartheta_b (renamed off the slot vector eta)")
    chk(P1.count("**C13.**") == 1, "§A C13 declared exactly once")


# ---------------------------------------------------------------- §B clause (1)
def eta_vectors():
    out = []
    for bits in range(16):
        eta = [1 - 2 * ((bits >> m) & 1) for m in range(4)]   # +1 / -1
        out.append(tuple(eta))
    return out


def odd_slots(eta):
    return [o for o in range(4) if all(eta[o] == -eta[m] for m in range(4) if m != o)]


def eta_of(o, sign):
    return tuple(sign * (-1 if m == o else 1) for m in range(4))


def section_B():
    print("§B — clause (1): the admissible sign vectors are exactly +/- eta^(o)")
    adm = [e for e in eta_vectors() if len(odd_slots(e)) == 1]
    chk(len(adm) == 8, "§B exactly 8 of the 16 sign vectors satisfy A3's unique-odd-slot condition")
    for e in adm:
        o = odd_slots(e)[0]
        sign = 1 if e[o] == -1 else -1
        reps = [(oo, s) for oo in range(4) for s in (1, -1) if eta_of(oo, s) == e]
        chk(reps == [(o, sign)],
            f"§B eta={e}: eta = {'+' if sign == 1 else '-'}eta^({o}) with (o,sign) unique")
    for e in eta_vectors():
        if e not in adm:
            chk(len(odd_slots(e)) != 1, f"§B eta={e} is inadmissible (odd-slot count {len(odd_slots(e))} != 1)")


# ---------------------------------------------------------------- §C clause (2)
def zeta_of(eta):
    return tuple([1] + [eta[0] * eta[i] for i in (1, 2, 3)])


def section_C():
    print("§C — clause (2): T[eta] = T[-eta]; T = D_zeta (x) D_zeta")
    for eta in [eta_of(o, -1) for o in range(4)]:
        neg = tuple(-x for x in eta)
        z = zeta_of(eta)
        ok_t = all(eta[m] * eta[n] == neg[m] * neg[n] for m in range(4) for n in range(4))
        ok_z = all(z[m] * z[n] == eta[m] * eta[n] for m in range(4) for n in range(4))
        chk(ok_t, f"§C eta^( {odd_slots(eta)[0]} ): the 16 products eta^mu eta^nu are sign-blind")
        chk(ok_z, f"§C eta^({odd_slots(eta)[0]}): zeta_mu zeta_nu = eta^mu eta^nu on all 16 pairs (zeta_0=1, zeta_i=eta^0 eta^i)")
    # D_zeta as a matrix map equals sf at o=0 (used again in §E)
    z0 = zeta_of(eta_of(0, -1))
    chk(z0 == (1, -1, -1, -1), "§C zeta at o=0 is (1,-1,-1,-1)")


# ---------------------------------------------------------------- §D clause (3)
def sector_census(z):
    # 16-basis (mu,nu): S=+ on symmetric (mu=nu or symmetrized mu<nu), S=- antisym
    pp = pm_ = mp = mm = 0
    for m in range(4):
        t = z[m] * z[m]
        pp += 1 if t == 1 else 0            # diagonal: S=+
    for m in range(4):
        for n in range(m + 1, 4):
            t = z[m] * z[n]
            if t == 1:
                pp += 1                     # sym
                mp += 1                     # antisym
            else:
                pm_ += 1                    # sym
                mm += 1                     # antisym
    return (pp, pm_, mp, mm)


def section_D():
    print("§D — clause (3): [S,T]=0 and (7,3,3,3) for every o")
    for o in range(4):
        eta = eta_of(o, -1)
        z = zeta_of(eta)
        cen = sector_census(z)
        chk(cen == (7, 3, 3, 3), f"§D o={o}: sector census (E_++,E_+-,E_-+,E_--) = {cen}")
        # [S,T]=0: S permutes (mu,nu); the T sign z_mu z_nu is symmetric in mu<->nu
        chk(all(z[m] * z[n] == z[n] * z[m] for m in range(4) for n in range(4)),
            f"§D o={o}: the T-grading is S-invariant on every basis pair ([S,T]=0)")


# ---------------------------------------------------------------- §E clause (4)
def Uc():
    s = m_add(m_add(SIG[1], SIG[2]), SIG[3])
    return m_add(m_scale(Fr(1, 2), SIG[0]), m_scale(QI(0, -1), m_scale(Fr(1, 2), s)))


def T_map(eta):
    """4x4-basis action: T(sigma_mu (x) sigma_nu) = eta^mu eta^nu (same basis el.)"""
    z = [(eta[m] * eta[n]) for m in range(4) for n in range(4)]
    return z


def section_E():
    print("§E — clause (4): sf at o=0; axis reflections at o>=1; conjugacy classes")
    # sf on the Pauli basis
    chk(m_eq(sf(SIG[0]), SIG[0]), "§E sf(sigma_0) = sigma_0")
    for i in (1, 2, 3):
        chk(m_eq(sf(SIG[i]), m_scale(-1, SIG[i])), f"§E sf(sigma_{i}) = -sigma_{i}")
    # o=0: D_zeta = sf on the basis
    z0 = zeta_of(eta_of(0, -1))
    chk(all(m_eq(m_scale(z0[mu], SIG[mu]), sf(SIG[mu])) for mu in range(4)),
        "§E o=0: D_zeta = sf on the Pauli basis (T = sf (x) sf: both-Bloch inversion)")
    # o=k: reflection of axis k
    for k in (1, 2, 3):
        z = zeta_of(eta_of(k, -1))
        chk(z[k] == -1 and all(z[i] == 1 for i in range(4) if i != k and i != 0) and z[0] == 1,
            f"§E o={k}: D_zeta reflects Bloch axis {k} only")
    # U_c exact: unitary and cyclic
    U = Uc()
    chk(m_eq(m_mul(U, m_dag(U)), mat([[ONE if i == j else ZERO for j in range(2)] for i in range(2)])),
        "§E U_c = (1 - i(s1+s2+s3))/2 is unitary over Q(i)")
    cyc = {1: 2, 2: 3, 3: 1}
    for i in (1, 2, 3):
        Ad = m_mul(U, m_mul(SIG[i], m_dag(U)))
        chk(m_eq(Ad, SIG[cyc[i]]), f"§E Ad_(U_c): sigma_{i} -> sigma_{cyc[i]} (exact over Q(i))")
    # T^(k) conjugacy under U_c (x) U_c: Ad T^(k) Ad^-1 = T^(pi(k))
    U4 = kron(U, U)
    basis = [kron(SIG[m], SIG[n]) for m in range(4) for n in range(4)]
    pi = {0: 0, 1: 2, 2: 3, 3: 1}
    for k in (1, 2, 3):
        tk = T_map(eta_of(k, -1))
        tp = T_map(eta_of(pi[k], -1))
        ok = True
        for idx, b in enumerate(basis):
            mu, nu = divmod(idx, 4)
            idx2 = pi[mu] * 4 + pi[nu]
            Ad_b = m_mul(U4, m_mul(b, m_dag(U4)))
            if not m_eq(Ad_b, basis[idx2]):       # Ad permutes the basis by pi
                ok = False
                break
            if tk[idx] != tp[idx2]:               # eigenvalue transport
                ok = False
                break
        chk(ok, f"§E Ad_(U_c (x) U_c) T^({k}) Ad^-1 = T^({pi[k]}) on all 16 basis elements")
    # T^(0) conjugate to none: char polys of the traceless block differ
    def charpoly3(M):
        # monic char poly coefficients (x^3 + c2 x^2 + c1 x + c0) exact Fractions
        tr = sum(M[i][i] for i in range(3))
        minors = (M[0][0] * M[1][1] - M[0][1] * M[1][0]
                   + M[0][0] * M[2][2] - M[0][2] * M[2][0]
                   + M[1][1] * M[2][2] - M[1][2] * M[2][1])
        det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
               - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
               + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        return (-tr, minors, -det)
    M0 = [[Fr(z0[i + 1] if i == j else 0) for j in range(3)] for i in range(3)]
    c0 = charpoly3(M0)
    chk(c0 == (Fr(3), Fr(3), Fr(1)), "§E o=0 traceless block char poly = (x+1)^3")
    for k in (1, 2, 3):
        z = zeta_of(eta_of(k, -1))
        Mk = [[Fr(z[i + 1] if i == j else 0) for j in range(3)] for i in range(3)]
        ck = charpoly3(Mk)
        chk(ck == (Fr(-1), Fr(-1), Fr(1)), f"§E o={k} traceless block char poly = (x-1)^2(x+1)")
        chk(ck != c0, f"§E o={k}: spectrum differs from o=0 => T^(0) not conjugate to T^({k}) under any similarity")


# ---------------------------------------------------------------- §F clause (5)
def generic_U():
    a, b, c, d = Poly.var(0), Poly.var(1), Poly.var(2), Poly.var(3)
    al = a + Poly.const(IM) * b
    be = c + Poly.const(IM) * d
    return pm([[al, be], [-be.conj(), al.conj()]]), al, be


def section_F():
    print("§F — clause (5): covariance iff o=0 (polynomial identities + U_c census)")
    U, al, be = generic_U()
    S2p = pm([[Poly.const(ZERO), Poly.const(-IM)], [Poly.const(IM), Poly.const(ZERO)]])
    # (i) sigma2 U^T sigma2 = U^dagger
    lhs = pm_mul(S2p, pm_mul(pm_T(U), S2p))
    rhs = pm_dag(U)
    chk(pm_zero(pm_sub(lhs, rhs)), "§F (i) sigma2 U^T sigma2 = U^dagger as a polynomial identity over Q(i)[a,b,c,d]")
    # (ii) sigma2 conj(U) sigma2 = U
    lhs2 = pm_mul(S2p, pm_mul(pm_conj(U), S2p))
    chk(pm_zero(pm_sub(lhs2, U)), "§F (ii) sigma2 conj(U) sigma2 = U as a polynomial identity")
    # (iii) sf(U s_mu U^dag) = U sf(s_mu) U^dag for the four Paulis (generic U)
    SIGp = [
        pm([[Poly.const(ONE), Poly.const(ZERO)], [Poly.const(ZERO), Poly.const(ONE)]]),
        pm([[Poly.const(ZERO), Poly.const(ONE)], [Poly.const(ONE), Poly.const(ZERO)]]),
        pm([[Poly.const(ZERO), Poly.const(-IM)], [Poly.const(IM), Poly.const(ZERO)]]),
        pm([[Poly.const(ONE), Poly.const(ZERO)], [Poly.const(ZERO), Poly.const(-ONE)]]),
    ]
    Ud = pm_dag(U)
    for mu in range(4):
        inner = pm_mul(U, pm_mul(SIGp[mu], Ud))
        l = pm_mul(S2p, pm_mul(pm_T(inner), S2p))
        r = pm_mul(U, pm_mul(pm_mul(S2p, pm_mul(pm_T(SIGp[mu]), S2p)), Ud))
        chk(pm_zero(pm_sub(l, r)), f"§F (iii) sf(U sigma_{mu} U^dagger) = U sf(sigma_{mu}) U^dagger (polynomial identity)")
    # witness point a=3/5, b=4/5, c=d=0: T^(0) = SF (.)^T SF with SF = s2 (x) s2,
    # and T^(0) Ad_(U(x)U) = Ad_(U(x)U) T^(0) on the 16-basis
    aa, bb, cc, dd = Fr(3, 5), Fr(4, 5), Fr(0), Fr(0)
    Uw = [[QI(aa, bb), QI(cc, dd)], [QI(-cc, dd), QI(aa, -bb)]]
    chk(m_eq(m_mul(Uw, m_dag(Uw)), mat([[ONE if i == j else ZERO for j in range(2)] for i in range(2)])),
        "§F witness U(3/5,4/5,0,0) is unitary over Q(i)")
    eta0 = eta_of(0, -1)
    t0 = T_map(eta0)
    SF4 = kron(SIG2, SIG2)
    basis = [kron(SIG[m], SIG[n]) for m in range(4) for n in range(4)]
    chk(all(m_eq(m_mul(SF4, m_mul(m_T(b), SF4)), m_scale(t0[i], b)) for i, b in enumerate(basis)),
        "§F witness: T^(0)(X) = SF X^T SF on the 16-basis (T^(0) = sf (x) sf)")
    U4 = kron(Uw, Uw)
    ok = True
    for idx, b in enumerate(basis):
        Ad_b = m_mul(U4, m_mul(b, m_dag(U4)))
        lhs = m_mul(SF4, m_mul(m_T(Ad_b), SF4))                # T^(0)(Ad(b))
        rhs = m_mul(U4, m_mul(m_scale(t0[idx], b), m_dag(U4)))  # Ad(T^(0)(b))
        if not m_eq(lhs, rhs):
            ok = False
            break
    chk(ok, "§F witness: T^(0) Ad_(U(x)U) = Ad_(U(x)U) T^(0) on all 16 basis elements at (3/5,4/5,0,0)")
    # (=>) via U_c: commutation on the 16-basis forces eta^1=eta^2=eta^3
    Uc4 = kron(Uc(), Uc())
    pi = {0: 0, 1: 2, 2: 3, 3: 1}
    for bits in range(16):
        eta = tuple(1 - 2 * ((bits >> m) & 1) for m in range(4))
        if len(odd_slots(eta)) != 1:
            continue
        # [T, Ad] = 0 on the 16-basis  <=>  zeta is pi-invariant
        z = zeta_of(eta)
        zinvar = all(z[pi[m]] == z[m] for m in range(4))
        o = odd_slots(eta)[0]
        chk(zinvar == (o == 0), f"§F (=>) eta with o={o}: [T, Ad_(U_c (x) U_c)]=0 on the 16-basis iff o=0 (zeta pi-invariance: {zinvar})")
    # explicit operator-level commutation at o=0 vs failure at o=1
    for o, expect in ((0, True), (1, False)):
        eta = eta_of(o, -1)
        t = T_map(eta)
        comm = True
        for idx, bs in enumerate(basis):
            mu, nu = divmod(idx, 4)
            Ad_b = m_mul(Uc4, m_mul(bs, m_dag(Uc4)))
            lhs = m_scale(t[pi[mu] * 4 + pi[nu]], Ad_b)   # T(Ad(b))
            rhs = m_mul(Uc4, m_mul(m_scale(t[idx], bs), m_dag(Uc4)))   # Ad(T(b))
            if not m_eq(lhs, rhs):
                comm = False
                break
        chk(comm == expect, f"§F operator-level: [T^(o={o}), Ad_(U_c (x) U_c)] = 0 is {expect}")


# ---------------------------------------------------------------- §G the Rmk census
def section_G():
    print("§G — the Rmk census: CT1.2's generator sectors at all four o")
    # generator T-eigenvalues in terms of zeta: (name, S, T(zeta))
    def sectors(z):
        out = {}
        out["E_0"] = ("+", "+")
        out["Sigma"] = ("+", "+")
        for i in range(1, 4):
            for j in range(i + 1, 4):
                out[f"E^{i}{j}"] = ("+", "+" if z[i] * z[j] == 1 else "-")
        # traceless diagonal E^ii combos: T = z_i^2 = + always
        out["E_diag"] = ("+", "+")
        for i in range(1, 4):
            out[f"W{i}"] = ("+", "+" if z[0] * z[i] == 1 else "-")
            out[f"K{i}"] = ("-", "+" if z[0] * z[i] == 1 else "-")
        cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
        for i in range(1, 4):
            j, k = cyc[i]
            out[f"J{i}"] = ("-", "+" if z[j] * z[k] == 1 else "-")
        return out
    base = sectors(zeta_of(eta_of(0, -1)))
    chk(base["W1"] == ("+", "-") and base["W2"] == ("+", "-") and base["W3"] == ("+", "-"),
        "§G o=0 reproduces CT1.2's table: W_i in E_+-")
    chk(base["J1"] == ("-", "+"), "§G o=0: J_i in E_-+ (sample J1)")
    chk(base["K1"] == ("-", "-"), "§G o=0: K_i in E_-- (sample K1)")
    chk(base["E^12"] == ("+", "+") and base["E^13"] == ("+", "+") and base["E^23"] == ("+", "+"),
        "§G o=0: E^ij in E_++ (all three pairs)")
    s1 = sectors(zeta_of(eta_of(1, -1)))
    chk(s1["W2"] == ("+", "+") and s1["W3"] == ("+", "+"), "§G o=1: W2,W3 move to E_++ (not E_+-)")
    chk(s1["W1"] == ("+", "-"), "§G o=1: only W1 stays in E_+-")
    chk(s1["J2"] == ("-", "-") and s1["J3"] == ("-", "-"), "§G o=1: J2,J3 move to E_--")
    chk(s1["K2"] == ("-", "+") and s1["K3"] == ("-", "+"), "§G o=1: K2,K3 move to E_-+ (swapped with J)")
    chk(s1["J1"] == ("-", "+") and s1["K1"] == ("-", "-"), "§G o=1: J1,K1 stay where CT1.2 puts them")
    chk(s1["E^12"] == ("+", "-") and s1["E^13"] == ("+", "-"), "§G o=1: E^12,E^13 move to E_+- (not E_++)")
    chk(s1["E^23"] == ("+", "+"), "§G o=1: E^23 stays in E_++")
    for o in (2, 3):
        so = sectors(zeta_of(eta_of(o, -1)))
        movedW = [i for i in (1, 2, 3) if i != o and so[f"W{i}"] == ("+", "+")]
        stayedW = [i for i in (1, 2, 3) if so[f"W{i}"] == ("+", "-")]
        chk(sorted(movedW) == sorted(i for i in (1, 2, 3) if i != o) and stayedW == [o],
            f"§G o={o}: symmetric statement — only W{o} stays in E_+-, the other two move to E_++")


def main():
    for s in (section_A, section_B, section_C, section_D, section_E, section_F, section_G):
        s()
    note = era_paths.archive_note("verify_CT10_signature")
    if note:
        print(note)
    print()
    if FAILS:
        print(f"verify_CT10_signature: {len(FAILS)} FAILURES")
        for m in FAILS:
            print("  -", m)
        return 1
    print("verify_CT10_signature: ALL CHECKS PASS (exact arithmetic; no floating point)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
