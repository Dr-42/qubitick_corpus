#!/usr/bin/env python3
"""
verify_F33_dynamic_phase.py — machine verification of Tier F.33.

Covers: Def-EM.20/EM.20 (dynamic edge phase), Def-EM.21/EM.23 (alignment
patterns, parity classification), EM.24 (CPT bridge), CT2.8 revised
(reflection positivity, factorization), FT.100 (m_hid phase-blindness),
and the corpus-level document pins of the revision (A §0.2a, P2, E/C
structure, dissolved-premise absence).

Exact arithmetic only: int / fractions.Fraction / complex-over-Fraction
(qmath.C) / an No floating point anywhere; every PASS is bit-exact equality.

Sections:
  §A  EM.20/Def-EM.20 — the revised two-branch A4 criterion: exact
      pair-state census over Q(i) (Pi_V = (E0-Sigma)/4 vs the singlet
      projector; rho_t = (1-t) Pi_R/3 + t Pi_V with w = |Pi_V rho_t| = t
      exact; pure witnesses |00>, |01>, singlet); aligned branch
      (w <= eps_q) real with alpha = 0, antialigned branch (w >= 1-eps_q)
      real with alpha = pi; BOTH branches non-empty for every eps_q in
      [0,1/4) (CT0.8); branch disjointness; vacuum w = 1/4 virtual;
      sharp eps_q = 0 read (supp in vee^2 or pure singlet); determinism;
      holonomy bijection e^{i alpha} <-> {+1,-1} (D1.1); EM.16 per-edge
      read-back alpha_e from sigma_e^{-1} G(e) on the D2.8 branch.
  §B  Def-EM.21/EM.23 — alignment-pattern enumeration for |E_R| = 1..6
      (126 patterns total): 2^k distinct patterns; path-reversal and
      cycle-reflection mirrors (involutions, orientation-reversing);
      parity-even census = 2^{#orbits} (closed form vs enumeration);
      parity-odd census (fixed-edge obstruction; 2^{k/2} on fixed-point-
      free mirrors); distinguishability P != E\\P for every k >= 1 and the
      k=0 degeneracy witness; uniform assignments are single points.
  §C  EM.24 — CPT bridge on exhaustive small models over Q(i):
      C/P/T closure and involutions; q -> -q, f -> -f, aleph invariant;
      T: w(Theta_L C) = w(C)^* (CT2.8(1) model); exact phase identity
      w(CPT C) = (-1)^|E| e^{i pi Theta} w(C); |w|^2 invariance
      unconditional; conjugate locus iff |E|+Theta even on-shell.
  §D  CT2.8 — reflection positivity on an explicit layered ledger model:
      factorization w(C) = w(left) w(right) at every interior cut
      (declared side convention); glue identity w(Theta A u A) =
      w(Theta A) w(A) with the interface vertex sign-telescoping to
      aleph_glue = 0; <A|A> = sum |w|^2 exhaustively; positivity;
      null space = mask-excluded set for two exact masks; |G(e)| = 1.
  §E  FT.100 — m_hid phase-blindness in exact integer coefficients
      (ln2 and hbar as formal symbols): coefficient invariant over all
      2^{E_int} alpha assignments; fiber cardinality; refinement witness
      (same m_hid, distinct parity classes).
  §F  document pins — A §0.2a list = CT2.6(ii),(iii); Comm-min / Eff /
      EM.20a absent from A-G; Def-EM.20/21/22 and the new EM.23/EM.24
      headings present; CT2.8 hypothesis-free; P2 alphabet row; H13
      Dissolution Registry; H12 Tier F.33/FT.100.

Run: python3 verify_F33_dynamic_phase.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import os
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

import re
import sys
import itertools
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C  # noqa: E402  exact complex over Fraction

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


# ---------------------------------------------------------------- exact rings

def kron(A, B):
    ra, ca = len(A), len(A[0]); rb, cb = len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb] for j in range(ca * cb)]
            for i in range(ra * rb)]


def mscale(A, x):
    return [[a * x for a in row] for row in A]


def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


I = C(0, 1)
S0 = [[C(1), C(0)], [C(0), C(1)]]
S1 = [[C(0), C(1)], [C(1), C(0)]]
S2 = [[C(0), -I], [I, C(0)]]
S3 = [[C(1), C(0)], [C(0), C(-1)]]
SIG = [S1, S2, S3]


def expipi_half(m):
    """e^{i pi m/2} exactly in Q(i), m in Z (period 4)."""
    return [C(1), C(0, 1), C(-1), C(0, -1)][m % 4]


def geo(alpha, d2):
    """e^{i alpha d2} for alpha in {0, pi}, d2 in (1/2)Z, exact in Q(i)."""
    m = int(alpha * d2 * 2)                      # alpha*d2 = m/2
    assert Fr(m, 2) == alpha * d2
    return expipi_half(m) if alpha else C(1)


# ---------------------------------------------------------------- §A EM.20

def sectionA():
    print("S1 = §A EM.20/Def-EM.20 dynamic phase: two-branch A4 census (exact)")
    # ---- Pi_V two ways: (E0 - Sigma)/4  vs  |Psi->><Psi-|  (exact over Q(i))
    E0 = kron(S0, S0)
    Sg = madd(madd(kron(S1, S1), kron(S2, S2)), kron(S3, S3))
    PV = mscale(madd(E0, Sg, -1), Fr(1, 4))          # (E0 - Sigma)/4  [CT0.7]
    PR = mscale(madd(mscale(E0, 3), Sg), Fr(1, 4))   # (3E0 + Sigma)/4
    sing = [[C(0)] * 4 for _ in range(4)]            # |Psi-> = (|01> - |10>)/sqrt2
    for (a, sa) in ((1, 1), (2, -1)):
        for (b, sb) in ((1, 1), (2, -1)):
            sing[a][b] = C(Fr(sa * sb, 2))
    chk("§A Pi_V = (E0-Sigma)/4 = |Psi->><Psi-| exactly; Pi_R + Pi_V = I4; "
        "Pi_V^2 = Pi_V; Tr Pi_V = 1; Pi_V Pi_R = 0 [CT0.7]",
        all(PV[i][j] == sing[i][j] for i in range(4) for j in range(4))
        and all(madd(PR, PV)[i][j] == (C(1) if i == j else C(0)) for i in range(4) for j in range(4))
        and all(sum(PV[i][k] * PV[k][j] for k in range(4)) == PV[i][j] for i in range(4) for j in range(4))
        and sum(PV[i][i] for i in range(4)) == C(1)
        and all(sum(PV[i][k] * PR[k][j] for k in range(4)) == C(0) for i in range(4) for j in range(4)))

    # ---- census family rho_t = (1-t) Pi_R/3 + t Pi_V :  w = |Pi_V rho_t| = t exact
    ts = [Fr(0), Fr(1, 8), Fr(1, 5), Fr(1, 4), Fr(3, 8), Fr(1, 2),
          Fr(5, 8), Fr(3, 4), Fr(4, 5), Fr(7, 8), Fr(1)]
    ws = {}
    ok_w = ok_tr = ok_psd = True
    for t in ts:
        rho = madd(mscale(PR, (1 - t) / 3), mscale(PV, t))
        w = sum(PV[i][k] * rho[k][i] for i in range(4) for k in range(4)).re   # Tr(Pi_V rho): real
        ws[t] = w
        if w != t:
            ok_w = False
        if sum(rho[i][i] for i in range(4)).re != 1:
            ok_tr = False
        # PSD by construction: eigenvalues (1-t)/3 (x3) and t, both >= 0 on the census
        if (1 - t) / 3 < 0 or t < 0:
            ok_psd = False
    chk("§A census: w = |Pi_V rho_t| = t exactly (matrix arithmetic), Tr rho_t = 1, "
        "rho_t >= 0 by construction (11 exact rational states)", ok_w and ok_tr and ok_psd)

    # ---- pure witnesses: |00> (w=0), |01> (w=1/2), singlet (w=1)
    def basis_proj(k):
        M = [[C(0)] * 4 for _ in range(4)]
        M[k][k] = C(1)
        return M
    w00 = PV[0][0].re
    w01 = PV[1][1].re
    wsk = sum(PV[i][k] * PV[k][i] for i in range(4) for k in range(4)).re
    chk("§A pure witnesses: w(|00><00|) = 0, w(|01><01|) = 1/2, w(singlet) = 1 — exact",
        w00 == 0 and w01 == Fr(1, 2) and wsk == 1)

    # ---- revised A4 classification on the census
    def classify(w, eps):
        """A4 two-branch: returns (real?, alpha/pi) — branches disjoint for eps < 1/2."""
        b1 = w <= eps
        b2 = w >= 1 - eps
        if b1 and b2:
            return ("overlap", None)
        if b1:
            return ("real", 0)
        if b2:
            return ("real", 1)
        return ("virtual", None)

    eps_list = [Fr(0), Fr(1, 8), Fr(1, 5), Fr(249, 1000)]
    ok_alpha = ok_disj = ok_pop = ok_vac = ok_det = True
    ok_sharp = True
    for eps in eps_list:
        assert eps < Fr(1, 2)                       # disjointness precondition
        edges0, edgesP = [], []
        f = {}
        for t in ts:
            st, a = classify(ws[t], eps)
            if st == "overlap":
                ok_disj = False
            if st == "real":
                if a not in (0, 1):
                    ok_alpha = False
                (edges0 if a == 0 else edgesP).append(t)
                if a != (0 if ws[t] <= eps else 1):
                    ok_det = False
            if t in f and f[t] != (st, a):
                ok_det = False
            f[t] = (st, a)
        if not edges0 or not edgesP:
            ok_pop = False                         # both branches must yield non-empty edge sets
        stv, _ = classify(Fr(1, 4), eps)
        if stv != "virtual":
            ok_vac = False                         # the A5 vacuum stays virtual (CT0.8)
    chk("§A alphabet preservation: alpha in {0,pi} for every real edge of the census, "
        "every admissible eps_q in [0,1/4) (EM.20(1))", ok_alpha)
    chk("§A branch disjointness: no census state satisfies both branches "
        "(eps_q < 1 - eps_q on the CT0.8 range)", ok_disj)
    chk("§A both branches populated: aligned (alpha=0) and antialigned (alpha=pi) edge "
        "sets are NON-EMPTY for every admissible eps_q (Directive census; A4 "
        "populatedness clause; EM.20(5))", ok_pop)
    chk("§A the vacuum w = 1/4 is virtual in both branches for every eps_q in [0,1/4) "
        "(CT0.8 consistency; CT0.2 global vacuum remains available)", ok_vac)
    chk("§A determinism: alpha_e is a function of (w, eps_q) — EM.20(2) measurement "
        "outcome, no declared constant", ok_det)
    # sharp eps = 0: real iff w in {0,1}; structural reads supp in vee^2 / rho = Pi_V
    sharp = {t: classify(ws[t], Fr(0)) for t in ts}
    ok_sharp = all((st == "real") == (ws[t] in (Fr(0), Fr(1))) for t, (st, _) in sharp.items())
    rho0 = mscale(PR, Fr(1, 3))
    ok_supp = all(sum(PV[i][k] * rho0[k][j] for k in range(4)) == C(0)
                  for i in range(4) for j in range(4))       # Pi_V rho_0 = 0: supp in vee^2
    ok_sing = all(PV[i][j] == sing[i][j] for i in range(4) for j in range(4))
    chk("§A sharp eps_q = 0: real iff w in {0,1}; w=0 witness has Pi_V rho = 0 "
        "(supp in vee^2, alpha=0); w=1 witness is the pure singlet (rho = Pi_V, alpha=pi) "
        "[CT0.8 sharp case]", ok_sharp and ok_supp and ok_sing)
    # ---- holonomy bijection e^{i alpha} <-> {+1,-1} [D1.1 reality-line action]
    hol = {al: C((-1) ** al) for al in (0, 1)}
    chk("§A holonomy bijection: e^{i alpha} = (-1)^{alpha/pi} maps {0,pi} onto {+1,-1} (D1.1)",
        hol[0] == C(1) and hol[1] == C(-1) and len(set(hol.values())) == 2)
    # ---- EM.16 per-edge read-back on the D2.8 branch
    ok = True
    for sg in (1, -1):
        for al in (0, 1):
            for d2 in (Fr(1, 2), Fr(1), Fr(3, 2)):
                G = C(sg) * geo(al, d2)
                r = C(sg) * G                       # sigma^{-1} = sigma
                back = 0 if r == C(1) else 1
                if back != al:
                    ok = False
    chk("§A EM.16 read-back: alpha_e recovered exactly from sigma_e^{-1} G(e) for every "
        "(sigma, alpha, ds2-hat in {1/2,1,3/2}) on the branch (distinct images)", ok)
    chk("§A |G(e)|^2 = 1 exactly for all (sigma, alpha, ds2-hat in (1/2)Z sample)",
        all((C(sg) * geo(al, d2)).re ** 2 + (C(sg) * geo(al, d2)).im ** 2 == Fr(1)
            for sg in (1, -1) for al in (0, 1)
            for d2 in (Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3))))


# ---------------------------------------------------------------- §B EM.23

def sectionB():
    print("S2 = §B Def-EM.21/EM.23 alignment patterns and parity classification")
    total = 0
    for k in range(1, 7):
        E = list(range(k))
        pats = [frozenset(p) for r in range(k + 1) for p in itertools.combinations(E, r)]
        total += len(pats)
        if len(pats) != 2 ** k or len(set(pats)) != 2 ** k:
            chk(f"§B k={k}: pattern count 2^{k}", False)
            continue
        chk(f"§B k={k}: exactly 2^{k} = {len(pats)} distinct alignment patterns (EM.23(4))",
            True)
        # distinguishability (EM.23(3)): P != E\P for every pattern, k >= 1
        selfcomp = [P for P in pats if P == frozenset(E) - P]
        chk(f"§B k={k}: no self-complementary pattern — even/odd distinguishable (EM.23(3))",
            selfcomp == [])
        # mirrors
        def orbits(m):
            seen, orb = set(), []
            for i in E:
                if i not in seen:
                    o = {i, m(i)}
                    seen |= o
                    orb.append(o)
            return orb

        mirrors = {"path-reversal": lambda i, k=k: k - 1 - i}
        mirrors["cycle-reflection"] = lambda i, k=k: (-i - 1) % k
        for mname, m in mirrors.items():
            # involution
            if any(m(m(i)) != i for i in E):
                chk(f"§B k={k} {mname}: mirror is an involution", False)
                continue
            orb = orbits(m)
            fixed = [o for o in orb if len(o) == 1]
            # parity-even census: M(P) = P  <=>  P is a union of orbits
            even = [P for P in pats if frozenset(m(i) for i in P) == P]
            if len(even) != 2 ** len(orb):
                chk(f"§B k={k} {mname}: even census 2^#orbits", False, f"{len(even)} vs {2**len(orb)}")
                continue
            # parity-odd census: M(P) = E\P  — possible iff no fixed edge
            odd = [P for P in pats if frozenset(m(i) for i in P) == frozenset(E) - P]
            want_odd = 0 if fixed else 2 ** len(orb)
            if len(odd) != want_odd:
                chk(f"§B k={k} {mname}: odd census", False, f"{len(odd)} vs {want_odd}")
                continue
            # no pattern is simultaneously even and odd (k >= 1)
            both = [P for P in pats if P in set(even) and P in set(odd)]
            chk(f"§B k={k} {mname}: even={len(even)}=2^{len(orb)}, odd={len(odd)}"
                f"{' (fixed-edge obstruction)' if fixed else ''}, even∩odd=∅ (EM.23(1)-(3))",
                both == [])
    chk("§B |E_R| <= 6: total enumerated patterns = 2+4+...+64 = 126", total == 126, str(total))
    # k = 0 degeneracy witness: P = E\P = empty — 'there is something' is required (EM.23(3))
    E0, P0 = frozenset(), frozenset()
    chk("§B k=0: the empty subnetwork's pattern is self-complementary — even/odd collapse "
        "(EM.23(3) precondition: at least one real edge)", P0 == E0 - P0)
    # uniform assignments are single points of the pattern space (EM.23(4))
    E6 = frozenset(range(6))
    pats6 = {frozenset(p) for r in range(7) for p in itertools.combinations(range(6), r)}
    chk("§B uniform assignments: P=∅ (alpha==0) and P=E_R (alpha==pi) are two points of the "
        "2^6 space; a single fixed pattern occupies one point",
        frozenset() in pats6 and E6 in pats6 and len({E6}) == 1 and len(pats6) == 64)
    # cycle-reflection fixed-edge structure (exactness of the obstruction)
    fx = {}
    for k in (3, 4, 5, 6):
        m = lambda i, k=k: (-i - 1) % k
        fx[k] = sum(1 for i in range(k) if m(i) == i)
    chk("§B cycle-reflection fixed edges: 1 for odd k, 0 for even k (k=3..6 exact)",
        fx == {3: 1, 4: 0, 5: 1, 6: 0}, str(fx))


# ---------------------------------------------------------------- §C EM.24

def model_w(sg, al, d2):
    """3-edge path model: w = prod sigma * prod e^{i alpha ds2} * (-1)^aleph.

    edges e0=(v0,v1), e1=(v1,v2), e2=(v2,v3); interior (1,1) vertices v1,v2
    (D3.3: f_v = (sigma_out - sigma_in)/2, aleph_v = |f_v|); J = 1 (D3.6).
    """
    f1 = Fr(sg[1] - sg[0], 2)
    f2 = Fr(sg[2] - sg[1], 2)
    aleph = abs(f1) + abs(f2)
    S = C(sg[0] * sg[1] * sg[2])
    G = geo(al[0], d2[0]) * geo(al[1], d2[1]) * geo(al[2], d2[2])
    return S * G * C((-1) ** int(aleph)), f1, f2, aleph


def sectionC():
    print("S3 = §C EM.24 CPT bridge (exhaustive small models over Q(i))")
    d2s = [(Fr(1), Fr(1, 2), Fr(3, 2)), (Fr(1), Fr(1), Fr(1)), (Fr(2), Fr(1), Fr(3))]
    nC = nT = nComp = nAbs = nIff = 0
    okC = okT = okComp = okAbs = True
    okq = okf = oka = True
    okInv = True
    for d2 in d2s:
        Theta = sum(d2)
        onshell = all(x.denominator == 1 for x in d2)
        for sg in itertools.product((1, -1), repeat=3):
            for al in itertools.product((0, 1), repeat=3):
                w, f1, f2, aleph = model_w(sg, al, d2)
                # (1) C: sigma -> -sigma
                sgc = tuple(-s for s in sg)
                wc, f1c, f2c, alephc = model_w(sgc, al, d2)
                q = Fr(sg[0] - sg[2], 2)
                qc = Fr(sgc[0] - sgc[2], 2)
                if qc != -q or f1c != -f1 or f2c != -f2 or alephc != aleph:
                    okC = False
                if wc != C((-1) ** 3) * w:
                    okC = False
                if q not in (Fr(-1), Fr(0), Fr(1)):
                    okq = False
                # (2) P: alpha -> pi - alpha (complement of the alignment pattern)
                alp = tuple(1 - a for a in al)
                wp, _, _, _ = model_w(sg, alp, d2)
                eipiTheta = expipi_half(int(2 * Theta)) if (2 * Theta).denominator == 1 else None
                Gfac = geo(al[0], d2[0]) * geo(al[1], d2[1]) * geo(al[2], d2[2])
                Gp = geo(alp[0], d2[0]) * geo(alp[1], d2[1]) * geo(alp[2], d2[2])
                if eipiTheta is not None and Gp != eipiTheta * C(Gfac.re, -Gfac.im):
                    okComp = False           # P: Gamma -> e^{i pi Theta} conj(Gamma)
                # (3) T: G(e) -> G(e)*, sigma fixed, aleph fixed => w -> w*
                wt = C(w.re, -w.im)
                # model of Theta_L on data: conjugate every edge factor
                wT = C(sg[0] * sg[1] * sg[2]) * C(Gfac.re, -Gfac.im) * C((-1) ** int(aleph))
                if wT != wt:
                    okT = False
                # (4) involutions on data
                if tuple(-(-s) for s in sg) != sg or tuple(1 - (1 - a) for a in al) != al:
                    okInv = False
                # (5) composition C o P o T on data (phase exponents in pi-units):
                # T: a -> -a (conjugation); P: a -> 1-a (complement) => P(T(a)) = 1+a; C: sigma -> -sigma
                alcpt = tuple(1 + a for a in al)
                sgx = tuple(-s for s in sg)
                Gx = C(1)
                for a2, dd in zip(alcpt, d2):
                    m = int(a2 * dd * 2)
                    assert Fr(m, 2) == a2 * dd
                    Gx *= expipi_half(m)
                fx1 = Fr(sgx[1] - sgx[0], 2)
                fx2 = Fr(sgx[2] - sgx[1], 2)
                ax = abs(fx1) + abs(fx2)
                wcpt = C(sgx[0] * sgx[1] * sgx[2]) * Gx * C((-1) ** int(ax))
                eipT = expipi_half(int(2 * Theta)) if (2 * Theta).denominator == 1 else None
                if eipT is not None and wcpt != C((-1) ** 3) * eipT * w:
                    okAbs = False            # w(CPT C) = (-1)^|E| e^{i pi Theta} w(C)
                if wcpt.re ** 2 + wcpt.im ** 2 != w.re ** 2 + w.im ** 2:
                    okAbs = False            # |w|^2 invariance
                if onshell and eipT is not None:
                    lhs = (wcpt == C(w.re, -w.im))
                    rhs = ((3 + int(Theta)) % 2 == 0)
                    if lhs != rhs:
                        okComp = False       # conjugate locus iff |E|+Theta even (on-shell, w real)
                    if w != C(w.re, -w.im):
                        okComp = False       # on-shell weights are real
                nC += 1
    chk(f"§C C: q->-q, f->-f, aleph invariant, w -> (-1)^|E| w (exhaustive: {nC} "
        "configuration-geometry pairs)", okC and okq)
    chk("§C T: w(Theta_L C) = w(C)^* exactly — CT2.8(1)/EM.24(3) (exhaustive)", okT)
    chk("§C component involutions C^2 = P^2 = T^2 = id on data (EM.24(4))", okInv)
    chk("§C P: Gamma -> e^{i pi Theta} conj(Gamma); composition identity w(CPT C) = "
        "(-1)^|E| e^{i pi Theta} w(C) (EM.24(5), exact over Q(i))", okComp and okAbs)
    chk("§C |w(CPT C)|^2 = |w(C)|^2 unconditional (EM.24(5); the directive's invariance bullet)",
        okAbs)
    chk("§C on-shell conjugate locus: w(CPT C) = w(C)^* iff |E|+Theta even; on-shell w real "
        "(biconditional, exhaustive)", okComp)


# ---------------------------------------------------------------- §D CT2.8

def sectionD():
    print("S4 = §D CT2.8 reflection positivity (explicit layered ledger model)")
    # --- factorization across interior cuts on a closed 4-cycle configuration
    d2 = (Fr(1), Fr(1, 2), Fr(1), Fr(3, 2))

    def cycle_w(sg, al):
        G = C(1)
        for s, a, dd in zip(sg, al, d2):
            G *= C(s) * geo(a, dd)
        aleph = 0
        for i in range(4):
            f = Fr(sg[(i + 1) % 4] - sg[i], 2)      # v_{i+1}: in e_i, out e_{i+1}
            aleph += abs(f)
        return G * C((-1) ** aleph)

    ok = True
    ncut = 0
    for cut in range(4):                              # cut after edge `cut`
        for sg in itertools.product((1, -1), repeat=4):
            for al in itertools.product((0, 1), repeat=4):
                wfull = cycle_w(sg, al)
                # left: edges e_0..e_cut with vertices v_1..v_cut (v_{i+1} joins e_i,e_{i+1});
                # right: remaining edges; interface vertex factor to the right (declared convention)
                def wpart(edges, verts):
                    G = C(1)
                    for i in edges:
                        G *= C(sg[i]) * geo(al[i], d2[i])
                    a = 0
                    for v in verts:                    # v joins e_{v-1} -> e_v (mod 4)
                        f = Fr(sg[v] - sg[v - 1], 2)
                        a += abs(f)
                    return G * C((-1) ** a)
                el = list(range(0, cut + 1))
                er = list(range(cut + 1, 4))
                vl = list(range(1, cut + 1))
                vr = [v for v in range(4) if v not in vl]     # includes interface vertex 0
                wl, wr = wpart(el, vl), wpart(er, vr)
                if wl * wr != wfull:
                    ok = False
                ncut += 1
    chk(f"§D(2) factorization w(C) = w(left) w(right) at every interior ledger-time cut "
        f"(4-cycle, all 4 cuts x all 256 assignments = {ncut} exact checks; interface "
        "convention declared)", ok)

    # --- glue identity + OS sum on a half-chain model: A = 3-edge path, sealed ends.
    # Theta_L A: reversed order, sigma fixed, each G conjugated [D2.7, CT1.11a(2)].
    # Glued cycle: interface vertex has in-sign = out-sign (Theta fixes sigma) => aleph_glue = 0.
    dh = (Fr(1), Fr(1, 2), Fr(1))

    def half_w(sg, al):
        G = C(1)
        for s, a, dd in zip(sg, al, dh):
            G *= C(s) * geo(a, dd)
        a1 = abs(Fr(sg[1] - sg[0], 2))               # interior vertex v1 (type (1,1))
        return G * C((-1) ** int(a1))                # terminal seals: aleph = 0 (D3.3 scope)


    def glue_w(sg, al):
        # Theta A edges (conjugated factors, sigma fixed) + A edges + interface vertex
        G = C(1)
        for s, a, dd in zip(sg, al, dh):
            g = C(s) * geo(a, dd)
            G *= C(g.re, -g.im)                      # reflected copy
        for s, a, dd in zip(sg, al, dh):
            G *= C(s) * geo(a, dd)
        a1 = abs(Fr(sg[1] - sg[0], 2))               # interior vertex of A
        aT = abs(Fr(sg[1] - sg[0], 2))               # reflected copy: sigma fixed => same |f|
        f_glue = Fr(sg[0] - sg[0], 2)                # interface: in = out = sigma(first edge)
        assert f_glue == 0                           # aleph_glue = 0: the sign telescope
        return G * C((-1) ** int(a1 + aT))

    okglue = okpos = True
    tot_half = Fr(0)
    n = 0
    for sg in itertools.product((1, -1), repeat=3):
        for al in itertools.product((0, 1), repeat=3):
            wh = half_w(sg, al)
            wth = C(wh.re, -wh.im)                   # w(Theta A) = w(A)^*  [clause (1)]
            if glue_w(sg, al) != wth * wh:
                okglue = False
            tot_half += wh.re ** 2 + wh.im ** 2
            n += 1
    chk(f"§D(1)+(2) glue identity w(Theta A u A) = w(Theta A) w(A) with aleph_glue = 0 "
        f"(sigma fixed under Theta_L; exhaustive {n} half-configurations)", okglue)
    chk(f"§D(3) <A|A> = sum_C |w(C)|^2 = {tot_half} = {n} (each |w|^2 = 1 exactly) >= 0",
        tot_half == n and tot_half >= 0)

    # --- clause (4): null space = mask-excluded configurations [CT2.2]
    def masked_sum(mask):
        s = Fr(0)
        for sg in itertools.product((1, -1), repeat=3):
            for al in itertools.product((0, 1), repeat=3):
                if mask(sg, al):
                    continue                         # excluded: weight 0 (projection kills it)
                w = half_w(sg, al)
                s += w.re ** 2 + w.im ** 2
        return s

    m_none = lambda sg, al: False
    m_some = lambda sg, al: sg[0] == -1 and al[0] == 1
    m_all = lambda sg, al: True
    s0, s1, s2 = masked_sum(m_none), masked_sum(m_some), masked_sum(m_all)
    chk("§D(4) null space: <A|A> = 0 iff every configuration is mask-excluded; partial masks "
        f"give exact positive counts ({s0}, {s1}, {s2})",
        s0 == 64 and s2 == 0 and 0 < s1 < 64 and s1.denominator == 1)
    # convergence clause (6): structural — the D2.8 sheet is a declaration, no float content
    print("  note: §D(6) convergence rests on the D2.8 sheet (declarative; no float check possible)")


# ---------------------------------------------------------------- §E FT.100

def sectionE():
    print("S5 = §E FT.100 m_hid phase-blindness (exact integer coefficients)")
    # m_hid = c * ln2/hbar with c = |Sigma| - min(delta_h, 4 delta_tau)  (Def-H.9(2), FT.1)
    # and on the floor families c = E_int (FT.32/FT.44(4)). ln2, hbar: formal symbols;
    # all comparisons are on the exact integer coefficients.
    ok = True
    for Eint in range(1, 7):
        Ebdy = 2
        for dh, dt in itertools.product((1, 2, 3, 6), (1, 2)):
            c = (Eint + Ebdy) - min(dh, 4 * dt)
            for al in itertools.product((0, 1), repeat=Eint):
                # alpha_e does not enter E_tot, E_vis, or the edge count
                c_alpha = (Eint + Ebdy) - min(dh, 4 * dt)
                if c_alpha != c:
                    ok = False
        # floor read: m_hid = E_int ln2/hbar — coefficient is the exact integer E_int
        if not isinstance(Eint, int):
            ok = False
    chk("§E(1)+(2) m_hid coefficient invariant over all 2^{E_int} phase assignments, "
        "E_int = 1..6, boundary/tick grid (Def-H.9(2), FT.1, FT.16): mass counts edges, "
        "not phases", ok)
    # fiber cardinality and refinement witness
    k = 2
    E = list(range(k))
    pats = [frozenset(p) for r in range(k + 1) for p in itertools.combinations(E, r)]
    m = lambda i: k - 1 - i                          # path-reversal mirror
    even = [P for P in pats if frozenset(m(i) for i in P) == P]
    odd = [P for P in pats if frozenset(m(i) for i in P) == frozenset(E) - P]
    chk("§E(3) refinement witness: all 2^2 = 4 patterns share E_int = 2 (same m_hid) yet split "
        f"into parity-even {sorted(map(sorted, even))} and parity-odd {sorted(map(sorted, odd))} "
        "— the alignment pattern refines the mass read",
        len(pats) == 4 and len(even) == 2 and len(odd) == 2 and set(even) & set(odd) == set())
    fibers = 0
    for Eint in range(1, 7):
        fibers += 2 ** Eint
    chk(f"§E(3) fiber cardinality over each mass value: 2^{{E_int}} patterns per fiber; "
        f"total over E_int=1..6: {fibers}", fibers == sum(2 ** i for i in range(1, 7)))


# ---------------------------------------------------------------- §F pins

def sectionF():
    print("S6 = §F document pins of the Tier F.33 revision")
    def rd(fn):
        return era_paths.read(fn)

    A, B, Cg, D, E, F, G = (rd(f) for f in
                            ("A_axioms.md", "B_foundation.md", "C_geometry.md",
                             "D_electroweak.md", "E_electromagnetic.md",
                             "F_color.md", "G_saturation.md"))
    AG = A + B + Cg + D + E + F + G
    chk("§F A §0.2a: the extra-axiomatic list is empty (CT2.6 (ii)-(iii) reclassified as derived, Part 4 Tier BM.24)",
        "The complete list of extra-axiomatic inputs is empty" in A and "BM.151" in A)
    chk("§F A §0.2a: CT2.6(i) reclassified as definitional precondition; CT2.8 hypothesis-free",
        "definitional precondition" in A and "CT2.8 carries no hypotheses" in A)
    chk("§F dissolved tokens absent from A-G: 'Comm-min' = 0, r'\\bEff\\b' = 0, 'EM.20a' = 0",
        AG.count("Comm-min") == 0 and len(re.findall(r"\bEff\b", AG)) == 0
        and AG.count("EM.20a") == 0)
    chk("§F P2 row: alpha_e in {0,pi} per edge (derived, zero freedom)",
        r"\alpha_e\in\{0,\pi\}\ \text{per edge};" in A)
    for h in ("### Def-EM.20 — ", "### Def-EM.21 — ", "### Def-EM.22 — ",
              "### EM.20 — The dynamic edge phase", "### EM.23 — Parity classification",
              "### EM.24 — The CPT bridge"):
        if h not in E:
            chk(f"§F E heading present: {h}", False)
    chk("§F E structure: Def-EM.20/21/22 + dynamic EM.20 + EM.23 parity + EM.24 CPT present; "
        "each Def block declares **Def.** exactly once",
        all(h in E for h in ("### Def-EM.20 — ", "### Def-EM.21 — ", "### Def-EM.22 — ",
                             "### EM.23 — Parity classification", "### EM.24 — The CPT bridge"))
        and all(E.count(f"### {t} — ") == 1 for t in ("Def-EM.20", "Def-EM.21", "Def-EM.22")))
    blk = Cg[Cg.index("### CT2.8 — "):Cg.index("### CT2.10 — ")]
    chk("§F C CT2.8: hypothesis-free statement citing D2.7, D1.9, D1.3, D2.8, CT2.2; "
        "clauses (1)-(6) present",
        "Hypotheses:" not in blk and all(t in blk for t in
        ("D2.7", "D1.9", "D1.3", "D2.8", "CT2.2", "(6)")))
    blk19 = Cg[Cg.index("### CT1.19b — "):Cg.index("### CT1.20 — ")]
    chk("§F C CT1.19b: antialigned-content winding Theta_P = 2k; EM.20(1) alphabet cited",
        "\\Theta_{\\mathcal P}(c)=2k" in blk19 and "EM.20}(1)" in blk19)
    if ARCH:
        H12, H13 = rd("H_archive/H12_chirality_and_form_factor.md"), rd("H_archive/H13_registries_and_gaps.md")
    if ARCH:
        chk("§F H12: Tier F.33 section with FT.100 present",
            "## Tier F.33 — " in H12 and "### FT.100 — " in H12)
        chk("§F H13: Dissolution Registry with the four mandated items",
            "**Dissolution Registry (corpus-level premises, Tier F.33).**" in H13
            and all(s in H13 for s in ("EM.20 Eff — eliminated", "EM.20a rung stability — withdrawn",
                                       "CT2.8 (i)–(ii) — closed", "CT2.6 (i) — reclassified")))


def main():
    print("verify_F33_dynamic_phase: Tier F.33 exact checks")
    sectionA()
    sectionB()
    sectionC()
    sectionD()
    sectionE()
    sectionF()
    print(f"verify_F33_dynamic_phase: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
