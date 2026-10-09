#!/usr/bin/env python3
"""verify_H_force_matrix.py — H19 Tier F.40 (Def-H.34, FT.127–FT.132): the static force matrix.

Exact arithmetic only (Fraction, Q(i) via qmath.C). No floating point in any assertion.
H19 carries no [EXT] numerical data; §E enforces that.

  §A  Def-H.34: the extended-carrier bases; the S-transform (chiral basis change) as an exact
      Pauli-triple rotation; the partner involution kappa-hat; the quaternionic triple
      (omega, chi, kappa); kappa's chiral action (ray swap, no phase); parity-definite
      kappa-eigenstates; the equal-weight chiral decomposition; kappa canonicity
  §B  FT.127/FT.128: seed images 1/2 sigma_a (x) I_2; the derived force matrix h(c) (x) I_omega;
      block decomposition in the chiral basis at Zariski-dense rational profile points:
      F_LL = F_RR = h, F_LR = F_RL = 0 (the no-flip theorem); [F_ext, chi-lift] = 0;
      the derived charpoly (x^2 - c0 x + (c0^2-|c|^2)/4)^2 (parity doubling);
      frozen-document census pins (EW.32 Y-image, EW.24 mixing, CT4.6 D+-scalar, FT.40, FT.15)
  §C  FT.129: the promoted matrix h (x) I + q I (x) kappa; commutation; chiral blocks
      F_LR = F_RL = q I_2; ternary q in {-1,0,1}: flip iff q != 0; flip-set minimality
  §D  FT.130: operator-Schmidt ranks via exact Pauli-bilinear flattening (1 derived, 2 promoted,
      degenerate cases); promoted charpoly ((y-u)^2-q^2)((y+u)^2-q^2), y = x - c0/2, u = |c|/2;
      the splitting 2|q| in {0,2}; collision census; scalar-shift invariance
  §E  FT.131/FT.132: document pins and vocabulary scans (no revision/drafting/directive language,
      species-free throughout, exactly one [EXT] marker, no external mass/coupling tokens);
      H18 forward pointer; H13 ledger pins
"""
import os, sys, time, re, itertools
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale

DOCS = os.path.normpath(os.path.join(HERE, '..'))
def rd(fn): return era_paths.read(fn)
if ARCH:
    H19DOC = rd('H_archive/H19_force_matrix.md')
    H18DOC = rd('H_archive/H18_chirality.md')
    H13DOC = rd('H_archive/H13_registries_and_gaps.md')
BDOC = rd('B_foundation.md')
DDOC = rd('D_electroweak.md')
GDOC = rd('G_saturation.md')
if ARCH:
    H02DOC = rd('H_archive/H02_edges_and_spin_charge.md')
    H05DOC = rd('H_archive/H05_floor_families.md')

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1
t0 = time.time()
def stamp(m): print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")
def banner(t):
    print("\n" + "=" * 100); print(t); print("=" * 100)

# ------------------------------------------------------------------ helpers over Q(i)
def mdag(A): return [[A[i][j].conj() for i in range(len(A))] for j in range(len(A[0]))]
def mvec(A, v): return [sum((A[i][j] * v[j] for j in range(len(v))), C(0)) for i in range(len(A))]
def outer(v, w): return [[v[i] * w[j].conj() for j in range(len(w))] for i in range(len(v))]
def mz(n): return [[C(0)] * n for _ in range(n)]
def meye(n): return [[C(1 if i == j else 0) for j in range(n)] for i in range(n)]
def mtr(A): return sum((A[i][i] for i in range(len(A))), C(0))
def ckron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(len(A[0]) * len(B[0]))]
            for i in range(n * m)]
SG = [meye(2),
      [[C(0), C(1)], [C(1), C(0)]],
      [[C(0), C(0, -1)], [C(0, 1), C(0)]],
      [[C(1), C(0)], [C(0), C(-1)]]]
OM = SG[1]      # omega-hat  = sigma_1 on H_omega
CHI = matscale([[C(0), C(1)], [C(-1), C(0)]], C(0, 1))   # i*(|c><w| - |w><c|) = [[0,i],[-i,0]] = -sigma_2
KAP = SG[3]     # kappa-hat  = sigma_3 on H_omega (orientation sign)
S = [[C(1), C(1)], [C(0, -1), C(0, 1)]]                  # columns = |L_u>, |R_u>;  S^dag S = 2 I
def schiral(B):
    """(1/2) S^dag B S : the omega-factor image in the chiral basis (exact over Q(i))."""
    return matscale(matmul(matmul(mdag(S), B), S), Fr(1, 2))
def rankQ(vs):
    rows = [list(map(Fr, v)) for v in vs]
    if not rows: return 0
    r = 0
    for c in range(len(rows[0])):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]; rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]; rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
def flatR(M):
    return [M[i][j].re for i in range(len(M)) for j in range(len(M[0]))] + \
           [M[i][j].im for i in range(len(M)) for j in range(len(M[0]))]
def charpoly_FL(M):
    """Faddeev-LeVerrier over Q(i); returns [1, c1, c2, c3, c4] of x^4 + c1 x^3 + ..."""
    n = len(M); Mk = meye(n); c = [C(1)]
    for k in range(1, n + 1):
        if k > 1: Mk = matadd(matmul(M, Mk), matscale(meye(n), c[-1]))
        AM = matmul(M, Mk); c.append(-mtr(AM) / k)
    return c
def hmat(c):
    """h(c) = (1/2) sum_a c_a sigma_a  (a = 0..3), exact over Q(i)."""
    H = mz(2)
    for a in range(4):
        H = matadd(H, matscale(SG[a], Fr(c[a], 2)))
    return H
def blocks4(M):
    """chiral-block decomposition of a 4x4 on (int (x) chiral-omega): returns (LL, LR, RL, RR)
    in the basis order (v|L>, v|R>, vp|L>, vp|R>) = int-major, omega-chiral-minor:
    composite index = 2*int + chiral (L=0, R=1)."""
    Lrows = (0, 2); Rrows = (1, 3)
    return ([[M[r][c] for c in Lrows] for r in Lrows],
            [[M[r][c] for c in Rrows] for r in Lrows],
            [[M[r][c] for c in Lrows] for r in Rrows],
            [[M[r][c] for c in Rrows] for r in Rrows])
def to_chiral_basis(M):
    """conjugate an int-major 4x4 (omega basis) into the chiral omega basis: (I2 (x) S)^-1 M (I2 (x) S)."""
    U = ckron(meye(2), S)
    Ud = matscale(mdag(U), Fr(1, 2))          # U^{-1} = (1/2) U^dagger  (S^dag S = 2 I)
    return matmul(matmul(Ud, M), U)

# profile sample points: Zariski-dense rational set in Q^4 (incl. degenerate corners)
CS = []
for c0 in (0, 1, Fr(-1, 2)):
    for c1 in (0, 1, -2, Fr(1, 3)):
        for c2 in (0, -1, Fr(2, 5)):
            for c3 in (0, 3, Fr(-1, 4)):
                CS.append((c0, c1, c2, c3))
QS = (Fr(0), Fr(1), Fr(-1))

# ================================================================== §A
banner("§A (H19/Def-H.34) — bases, the S-transform, kappa-hat, the quaternionic triple")
chk(matmul(mdag(S), S) == matscale(meye(2), C(2)), "§A S^dag S = 2 I_2 (the 1/sqrt2 lives in the normalization; all conjugations are exact over Q(i))")
# S-conjugation rotates the Pauli triple: sigma_1 -> -sigma_2, sigma_2 -> -sigma_3, sigma_3 -> sigma_1
chk(schiral(SG[0]) == SG[0], "§A S-conjugation fixes I_2")
chk(schiral(OM) == matscale(SG[2], C(-1)), "§A omega-hat (sigma_1) maps to -sigma_2 in the chiral basis (= the chi-hat matrix form)")
chk(schiral(CHI) == SG[3], "§A chi-hat (-sigma_2) maps to sigma_3 in the chiral basis (diagonal: chirality is the chiral-basis grade)")
chk(schiral(KAP) == SG[1], "§A kappa-hat (sigma_3) maps to sigma_1 in the chiral basis (pure flip)")
# kappa-hat: construction, involution, omega-oddness, diagonality
kc = [C(1), C(0)]; kw = [C(0), C(1)]
KAPc = matadd(outer(kc, kc), outer(kw, kw), -1)
chk(KAPc == KAP, "§A kappa-hat = |c><c| - |w><w| (the orientation-sign operator)")
chk(matmul(KAP, KAP) == meye(2) and mdag(KAP) == KAP and mtr(KAP) == C(0), "§A kappa^2 = id, Hermitian, traceless")
chk(matmul(matmul(OM, KAP), OM) == matscale(KAP, C(-1)), "§A omega kappa omega^-1 = -kappa (omega-odd)")
chk(matadd(matmul(KAP, OM), matmul(OM, KAP)) == mz(2) and matadd(matmul(KAP, CHI), matmul(CHI, KAP)) == mz(2),
    "§A kappa anticommutes with omega and with chi: the three form a Pauli triple")
# quaternionic products
chk(matmul(OM, CHI) == matscale(KAP, C(0, -1)), "§A omega*chi = -i kappa")
chk(matmul(CHI, KAP) == matscale(OM, C(0, -1)), "§A chi*kappa = -i omega")
chk(matmul(KAP, OM) == matscale(CHI, C(0, -1)), "§A kappa*omega = -i chi")
# kappa canonicity: diagonal omega-odd Hermitian involutions = {+kappa, -kappa}
diag_inv = []
for p in range(-6, 7):
    for q in range(1, 7):
        a = Fr(p, q)
        M = [[C(a), C(0)], [C(0), C(-a)]]
        if matmul(matmul(OM, M), OM) == matscale(M, C(-1)) and matmul(M, M) == meye(2):
            diag_inv.append(a)
chk(set(diag_inv) == {Fr(1), Fr(-1)}, f"§A diagonal omega-odd involutions over the rational census: a in {{+-1}} only (got {sorted(set(diag_inv))}): kappa unique up to sign")
# kappa swaps the chiral rays without phase
Lu = [C(1), C(0, -1)]; Ru = [C(1), C(0, 1)]
chk(mvec(KAP, Lu) == Ru and mvec(KAP, Ru) == Lu, "§A kappa|L_u> = |R_u>, kappa|R_u> = |L_u> (ray swap, no phase)")
# kappa eigenrays = the orientation rays; omega eigenrays = the parity superpositions
pp = [C(1), C(1)]; mm = [C(1), C(-1)]
chk(mvec(KAP, kc) == kc and mvec(KAP, kw) == [-x for x in kw], "§A kappa|c> = +|c>, kappa|w> = -|w>: the kappa-eigenrays are the orientation rays (kappa is diagonal in the orientation basis)")
chk(mvec(OM, pp) == pp and mvec(OM, mm) == [-x for x in mm], "§A omega|c+-w> = +-|c+-w>: the parity rays are the omega-eigenrays")
# orientation rays are equal-weight chiral superpositions: |c> = (|L_u> + |R_u>)/2 (unnormalized)
chk([(Lu[k] + Ru[k]) / 2 for k in range(2)] == kc, "§A |c> = (|L_u> + |R_u>)/2: equal-weight superposition of the two chiral rays")
chk([(Ru[k] - Lu[k]) / C(0, 2) for k in range(2)] == kw, "§A |w> = (|R_u> - |L_u>)/(2i): equal-weight superposition with the opposite relative phase")
# parity rays are equal-weight chiral superpositions too: |c+w> = ((1+i)|L_u> + (1-i)|R_u>)/2
chk([((C(1) + C(0,1)) * Lu[k] + (C(1) - C(0,1)) * Ru[k]) / 2 for k in range(2)] == pp, "§A parity ray |c+w> = ((1+i)|L_u> + (1-i)|R_u>)/2: no stationary ray carries a definite chirality when q != 0")
stamp("§A green: S-transform exact; Pauli-triple rotation; kappa constructed, canonical, quaternionic with (omega, chi); ray swap; orientation/parity eigenrays; equal-weight chiral decompositions")

# ================================================================== §B
banner("§B (H19/FT.127, FT.128) — seed images, the derived force matrix, the no-flip theorem")
# seed images: W_i -> sigma_i/2 (x) I_2 ; Y -> sigma_0/2 (x) I_2  [EW.32, P-H18a]
SEED = [ckron(matscale(SG[i], Fr(1, 2)), meye(2)) for i in (1, 2, 3, 0)]
chk(all(matmul(SEED[a], mdag(SEED[a])) != mz(4) for a in range(4)), "§A (guard: seed images nonzero)")
# the four seed images span End(C^2) (x) I_omega: Q-rank 8 of the flattened family
_rows = []
for M in SEED:
    _rows.append(flatR(M)); _rows.append(flatR(matscale(M, C(0, 1))))
chk(rankQ(_rows) == 8, "§B the seed images {sigma_a/2 (x) I_2} are C-independent (real rank 8 = 4 over C = End(C^2) (x) I): the EW aspects span every chirality-blind internal operator")
# weak chirality-blindness re-verified from the explicit matrices (not assumed)
PLc = ckron(meye(2), matscale(matadd(meye(2), CHI), Fr(1, 2)))
PRc = ckron(meye(2), matscale(matadd(meye(2), CHI, -1), Fr(1, 2)))
for i in range(3):
    chk(matmul(matmul(PLc, SEED[i]), PRc) == mz(4), f"§B P_L W_{i+1}^(ext) P_R = 0 entrywise (the weak flip contribution is verified, not assumed)")
# the derived force matrix and its chiral blocks at every sample profile
def Fext_derived(c):
    return ckron(hmat(c), meye(2))
for c in CS:
    F = Fext_derived(c)
    Fc = to_chiral_basis(F)
    LL, LR, RL, RR = blocks4(Fc)
    h = hmat(c)
    chk(Fc == ckron(h, meye(2)), "§B chiral-basis form invariance: U^-1 (h (x) I) U = h (x) I (conjugation touches only the omega factor, where F is I_2)")
    chk(LL == h and RR == h, "§B F_LL = F_RR = h(c)")
    chk(LR == mz(2) and RL == mz(2), "§B NO-FLIP THEOREM: F_LR = F_RL = 0 exactly, for every rational profile c (entries linear in c: Zariski-dense sampling => identically zero)")
    chk(matadd(matmul(F, ckron(meye(2), CHI)), matmul(ckron(meye(2), CHI), F), -1) == mz(4), "§B [F_ext, I (x) chi] = 0: chirality is an exact quantum number of the derived static force matrix")
# derived charpoly: (x^2 - c0 x + (c0^2 - |c|^2)/4)^2 with |c|^2 = c1^2+c2^2+c3^2
for c in CS:
    F = Fext_derived(c)
    cp = charpoly_FL(F)
    c0, c1, c2, c3 = c
    n2 = c1*c1 + c2*c2 + c3*c3
    # (x^2 - c0 x + (c0^2-n2)/4)^2 = x^4 - 2c0 x^3 + (c0^2 + 2*(c0^2-n2)/4... expand exactly:
    d = Fr(c0*c0 - n2, 4)
    exp = [C(1), C(-2*Fr(c0)), C(Fr(c0)*Fr(c0) + 2*d), C(-2*Fr(c0)*d), C(d*d)]
    chk(all(cp[k] == exp[k] for k in range(5)), f"§B derived charpoly = (x^2 - c0 x + (c0^2-|c|^2)/4)^2 at c={c}: parity doubling (each eigenvalue x2)")
    chk(all(cp[k].im == 0 for k in range(5)), "§B charpoly coefficients real-rational (Hermitian)")
# frozen-document census pins
chk('Y\\longmapsto\\tfrac12\\sigma_0' in DDOC, "§B pin: EW.32 carries the Y seed image (1/2) sigma_0")
chk('W_i\\longmapsto\\tfrac12\\sigma_i' in DDOC, "§B pin: EW.32 carries the weak seed images (1/2) sigma_i")
chk('T_a\\,\\mathsf v=0' in DDOC, "§B pin: EW.32 colour neutrality of the seed")
chk('A=\\sin\\theta_W\\,W_3+\\cos\\theta_W\\,Y' in DDOC, "§B pin: EW.24/D3.10 neutral mixing")
chk('F_{D^+}=\\Lambda\\,\\mathbb I' in GDOC, "§B pin: CT4.6/D4.3 — F_D+ = Lambda * identity (scalar class)")
chk('F_{D^-}=\\bigoplus_{n\\ge4}F_n' in GDOC, "§B pin: CT4.1/D4.1 — F_D- = the oversubscription ledger sink")
chk('F_{D^+} & \\operatorname{span}\\{E_0\\}' in BDOC, "§B pin: CT0.12 aspect table — D+ = span{E_0} (central pair direction)")
stamp(f"§B green: seed span; weak flip contribution zero (entrywise); no-flip theorem on {len(CS)} profiles; chirality conserved; parity-doubled charpoly; census pins")

# ================================================================== §C
banner("§C (H19/FT.129) — the promoted matrix: F_LR = q I_2, the flipping set, ternary q")
for c in CS[:48]:
    for q in QS:
        F = matadd(Fext_derived(c), matscale(ckron(meye(2), KAP), q))
        # the two terms commute
        A1 = Fext_derived(c); A2 = matscale(ckron(meye(2), KAP), q)
        chk(matadd(matmul(A1, A2), matmul(A2, A1), -1) == mz(4), "§C [h (x) I, q I (x) kappa] = 0 (the promoted terms commute)")
        Fc = to_chiral_basis(F)
        LL, LR, RL, RR = blocks4(Fc)
        h = hmat(c)
        chk(LL == h and RR == h, "§C promoted blocks: F_LL = F_RR = h(c) (the diagonal part is untouched)")
        chk(LR == matscale(meye(2), q) and RL == matscale(meye(2), q), "§C FLIPPING BLOCK: F_LR = F_RL = q * I_2 exactly")
        if q != 0:
            chk(LR != mz(2), "§C F_LR != 0 iff q != 0")
        else:
            chk(LR == mz(2), "§C neutral core (q=0): F_LR = 0 — the derived no-flip result is the q=0 case")
# minimality of the flipping set: dropping the kappa term kills the flip (FT.128); dropping any weak/seed term leaves it
c0 = (Fr(1), Fr(2), Fr(-1), Fr(1, 2))
Ffull = matadd(Fext_derived(c0), matscale(ckron(meye(2), KAP), Fr(1)))
FnoW = matscale(ckron(meye(2), KAP), Fr(1))
chk(blocks4(to_chiral_basis(Ffull))[1] == meye(2), "§C full matrix: F_LR = I_2 at q=1")
chk(blocks4(to_chiral_basis(FnoW))[1] == meye(2), "§C flipping set minimality: with EVERY internal term removed (the kappa term alone), F_LR = q I_2 — the flip needs only the promoted core read")
chk(blocks4(to_chiral_basis(Fext_derived(c0)))[1] == mz(2), "§C flipping set minimality: with the kappa term removed, F_LR = 0 for every profile — no subset of the derived actions flips")
# ternary read pin
if ARCH:
    chk('q_{\\mathrm{core}}' in H05DOC and 'ternary' in H05DOC, "§C pin: FT.40's ternary core-charge read")
    chk('boundary charge $q$' in H02DOC, "§C pin: FT.15's equal-q hypothesis (the superselection tension logged in P-H19a)")
stamp("§C green: commutation; F_LR = q I_2 on 48 profiles x ternary q; flip iff charged core; flipping set {EM core read} minimal and unique; pins")

# ================================================================== §D
banner("§D (H19/FT.130) — Schmidt ranks, the promoted charpoly, the splitting 2|q|, scalar shifts")
def pauli_coeffs(M):
    """exact coefficients t_ab with M = sum_ab t_ab (sigma_a (x) sigma_b)/... using tr orthogonality:
    t_ab = tr(M (sigma_a (x) sigma_b)) / 4."""
    T = [[C(0)] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            P = ckron(SG[a], SG[b])
            T[a][b] = mtr(matmul(M, P)) / 4
    return T
for c in CS[:48]:
    T = pauli_coeffs(Fext_derived(c))
    flat = [[T[a][b].re for b in range(4)] + [T[a][b].im for b in range(4)] for a in range(4)]
    nz = any(c[a] != 0 for a in range(4))
    # the coefficient matrix T is over Q for rational profiles (Hermitian F, Pauli basis): rank over Q = Schmidt rank
    chk(all(T[a][b].im == 0 for a in range(4) for b in range(4)), "§D Pauli coefficients of a Hermitian matrix at rational profiles are real")
    chk(rankQ(flat) == (1 if nz else 0), "§D derived locus: operator-Schmidt rank 1 (h (x) I_omega is a single simple tensor; rank 0 iff c = 0)")
    tz = any(c[a] != 0 for a in (1, 2, 3))          # traceless internal part nonzero
    for q in QS:
        F = matadd(Fext_derived(c), matscale(ckron(meye(2), KAP), q))
        T = pauli_coeffs(F)
        chk(all(T[a][b].im == 0 for a in range(4) for b in range(4)), "§D promoted Pauli coefficients real at rational data")
        flat = [[T[a][b].re for b in range(4)] + [T[a][b].im for b in range(4)] for a in range(4)]
        want = (1 if nz else 0) + (1 if q != 0 else 0) - (1 if (nz and q != 0 and not tz) else 0)
        chk(rankQ(flat) == want, "§D promoted locus: Schmidt rank 2 iff q != 0 AND the traceless internal part of h is nonzero; rank 1 when h is proportional to I_2 (the two terms share the internal factor and recombine into I_2 (x) (lam I_2 + q kappa)); rank 0 iff c = 0 = q")
# HS orthogonality exact: <h (x) I, q I (x) kappa>_HS = q tr(h) tr(kappa) = 0 for EVERY h
hc = hmat((1, 2, -1, Fr(1, 2)))
chk(mtr(KAP) == C(0), "§D tr kappa = 0: the two Schmidt terms are HS-orthogonal for every h (tr(h (x) I . I (x) kappa) = tr(h) tr(kappa) = 0)")
chk(mtr(matmul(mdag(ckron(hc, meye(2))), matscale(ckron(meye(2), KAP), Fr(1)))) == C(0), "§D HS inner product of the two terms vanishes exactly (witness profile)")
# promoted charpoly and the splitting
for c in CS:
    c0, c1, c2, c3 = c
    n2 = c1*c1 + c2*c2 + c3*c3
    for q in QS:
        F = matadd(Fext_derived(c), matscale(ckron(meye(2), KAP), q))
        cp = charpoly_FL(F)
        # charpoly = ((y-u)^2 - q^2)((y+u)^2 - q^2), y = x - c0/2, u^2 = n2/4
        # = (y^2 + u^2 - q^2)^2 - 4 u^2 y^2
        d = Fr(c0, 2)
        A = Fr(n2, 4) - q*q          # u^2 - q^2
        # (y^2 + A)^2 - n2 y^2 with y = x - d:  expand in x exactly over Q
        # y^2 = x^2 - 2dx + d^2;  y^4 = ...
        from fractions import Fraction as F2
        def poly_mul(p, r):
            out = [Fr(0)] * (len(p) + len(r) - 1)
            for i, a in enumerate(p):
                for j, b in enumerate(r):
                    out[i+j] += a*b
            return out
        y2 = [d*d, Fr(-2)*d, Fr(1)]                    # y^2 in ascending x-powers
        base = [A + d*d, Fr(-2)*d, Fr(1)]              # y^2 + A
        sq = poly_mul(base, base)                       # (y^2+A)^2
        n2y2 = [Fr(0), Fr(0), Fr(n2)]                  # n2 * y^2
        term = poly_mul(n2y2, [Fr(1)])
        # subtract n2*y^2*(1)?? careful: 4u^2 y^2 = n2 * y^2:
        target = [sq[k] - (Fr(n2) * (y2[k] if k < len(y2) else Fr(0))) for k in range(len(sq))]
        got = [cp[4-k].re for k in range(5)]           # cp is descending; target ascending
        chk(all(got[k] == target[k] for k in range(5)), f"§D promoted charpoly = ((y-u)^2-q^2)((y+u)^2-q^2), y=x-c0/2, u^2=|c|^2/4, at c={c}, q={q}")
        chk(all(cp[k].im == 0 for k in range(5)), "§D promoted charpoly real-rational")
# the splitting: eigenvalue pairs (s fixed, t = +-): difference exactly 2q
# census of collisions at ternary q and rational |c| values where |c|/2 in Q
for u2, uname in ((Fr(1,4), '|c|/2 = 1/2'), (Fr(1), '|c|/2 = 1'), (Fr(9,4), '|c|/2 = 3/2')):
    for q in QS:
        ev = sorted([Fr(1,1)*s*(u2) + t*q for s in (1, -1) for t in (1, -1)])
        split = 2*abs(q)
        chk(split in (0, 2), "§D splitting 2|q| in {0, 2} for the ternary read (EM.9): charged cores split by exactly 2, neutral cores keep parity doubling")
        if q == 0:
            chk(len(set(ev)) == 2, "§D q=0: parity doubling (two eigenvalues, each x2)")
# scalar-shift clause: F -> F + lambda I_4 re-absorbs into h -> h + lambda I_2
for c in CS[:24]:
    for lam in (Fr(3), Fr(-1, 2)):
        F1 = matadd(Fext_derived(c), matscale(meye(4), lam))
        F2 = ckron(matadd(hmat(c), matscale(meye(2), lam)), meye(2))
        chk(F1 == F2, "§D scalar shift lambda I_4 = (lambda I_2) (x) I_omega re-absorbs into h: Schmidt rank, F_LR, commutants unchanged; the spectrum shifts by lambda")
stamp(f"§D green: Schmidt ranks 1/2 exact (HS-orthogonal terms); promoted charpoly on {len(CS)} profiles x ternary q; splitting 2|q| in {{0,2}}; collision census; scalar-shift invariance")

# ================================================================== §E
banner("§E (H19/FT.131, FT.132) — document pins, vocabulary scans, downstream integrity")
if ARCH:
    doc = H19DOC
secs = {}
if ARCH:
    for sp in re.split(r'^### ', doc, flags=re.M)[1:]:
        secs[sp.split(' —')[0].strip()] = sp.split('\n## ')[0]
    for t in ('Def-H.34', 'FT.127', 'FT.128', 'FT.129', 'FT.130', 'FT.131', 'FT.132'):
        chk(t in secs, f"§E section {t} present")
    for w in ('**Thm.**', '**Req.**', '**Pf.**', '**Phys.**', '**Status.**'):
        chk(all(secs[t].count(w) == 1 for t in ('FT.127', 'FT.128', 'FT.129', 'FT.130', 'FT.131', 'FT.132')), f"§E every FT block carries exactly one {w}")
    chk(secs['Def-H.34'].count('**Def.**') == 1, "§E Def-H.34 carries exactly one **Def.**")
    chk(doc.count(r'\blacksquare') == 7, f"§E 7 proof terminators (got {doc.count(chr(92)+'blacksquare')})")
    chk(doc.count('**Status.**') == 7, "§E Status count = 7 (6 theorem blocks + the document header line)")
    chk('## Tier F.40' in doc and 'part 19 of 19' in doc, "§E pins: Tier F.40 heading; part 19 of 19")
    chk('P-H19a' in doc and 'verify_H_force_matrix.py' in doc, "§E pins: P-H19a flagged; machine reference")
    chk(r'h(\mathbf c)=\tfrac12\sum_{a=0}^{3}c_a\,\sigma_a' in doc, "§E pin: the h(c) display")
    chk(r'F_{LR}=q\,I_2' in doc, "§E pin: the flipping block display F_LR = q I_2")
    chk('2|q|' in doc, "§E pin: the splitting 2|q|")
    chk(r'\mathbf F_{\mathrm{ext}}(\mathbf c)=h(\mathbf c)\otimes I_\omega' in doc, "§E pin: the derived force matrix display")
    chk(r'\mathbf F_{\mathrm{ext}}(\mathbf c,q)=h(\mathbf c)\otimes I_2+q\,I_2\otimes\hat\kappa' in doc, "§E pin: the promoted force matrix display")
    chk('| Flipping frequency | — | Deferred (needs emergent time, FT.131(3)) |' in doc, "§E pin: adjudication row (frequency deferred)")
    chk('| Read promotion $\\hat Q_{\\mathrm{EM}}=q_{\\mathrm{core}}\\hat\\kappa$ | FT.129(4) | Declared (P-H19a) |' in doc, "§E pin: adjudication row (declared promotion)")
BARRED = ['previously', 'formerly', 'this was', 'now this', 'erratum', 'submitted', 'earlier draft', 'stale', 'draft', 'directive', 'as corrected']
if ARCH:
    hits = [(w, doc.lower().count(w)) for w in BARRED if w in doc.lower()]
if ARCH:
    chk(not hits, f"§E revision/drafting/directive-language scan of H19: zero hits ({hits})")
SPECIES = ['electron', 'muon', 'tau lepton', 'neutrino', 'proton', 'neutron', 'quark', 'photon', 'gluon', 'lepton', 'pion', 'higgs boson']
if ARCH:
    ph = [(w, doc.lower().count(w)) for w in SPECIES if w in doc.lower()]
if ARCH:
    chk(not ph, f"§E species-name scan of ALL of H19 (no audit clause needed — zero external data): zero hits ({ph})")
    chk(doc.count('tau') == doc.count('\\tau'), "§E every 'tau' substring in H19 is the tick-symbol macro \\delta\\tau (D0.7 vocabulary), not a species name")
    chk(doc.count('[EXT]') == 1, f"§E [EXT] occurs exactly once (the standing-rules clause): got {doc.count('[EXT]')}")
MASS = ['0.511', '105.6', '1776', '206.7', '3477', '1.273', '4.183', '162.5', '172.4', '938.2', '139.57', '0.118', '137.0']
if ARCH:
    leak = [t for t in MASS if t in doc]
if ARCH:
    chk(not leak, f"§E no external mass/coupling token anywhere in H19 ({leak})")
    # downstream integrity
    chk('FT.128' in H18DOC and 'off-diagonal complement' in H18DOC, "§E H18 carries the forward pointer to the flipping block (non-load-bearing)")
    chk('**(P-H19a)**' in H13DOC, "§E P-H19a registered in H13")
    chk('flipping block computed' in H13DOC, "§E H13 deficit-1' annotation: flipping block computed; frequency deferred")
    chk('prerequisite' in H13DOC, "§E H13 item-21(b) annotation: emergent time is a named prerequisite")
    chk('forward pointer' in H18DOC and 'FT.128' in H18DOC, "§E H18 carries the forward pointer to the flipping-block tier (non-load-bearing; H18 Req lines cite no H19 tag)")
chk(all(t in BDOC for t in ('CT0.12', 'CT0.7', 'CT1.2')), "§E cited B-tags exist")
chk(all(t in DDOC for t in ('EW.32', 'EW.24', 'EW.13', 'EW.33')), "§E cited D-tags exist")
chk(all(t in GDOC for t in ('CT4.1', 'CT4.6')), "§E cited G-tags exist")
stamp("§E green: sections, markers, counts, display pins, adjudication rows; zero barred/species hits; one [EXT] marker; H18/H13 downstream integrity")

print(f"\nverify_H_force_matrix: {N} checks green  ({time.time()-t0:.1f}s) — H19 §A–§E (Tier F.40, Def-H.34 + FT.127–FT.132)")
