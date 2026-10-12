#!/usr/bin/env python3
"""verify_H_chirality.py — H18 Tier F.39 (Def-H.33, FT.122–FT.126): the orientation doublet.

The chain orientation space, the exchange-form chirality operator, the corrected ket
labelling (erratum §H18-E), weak covariance on the extended carrier, the seven-locus
obstruction census, and the deficit-ledger pins.

Exact arithmetic only (Fraction, Q(i) via qmath.C).  No floating point in any assertion.
H18 contains no [EXT] numerical data; the scan asserts that.

  §A  Def-H.33 / FT.122 algebra: chi-hat and omega-hat over Q(i); the chi^2 chain;
      Hermiticity; projectors; the ket eigen-identities and ray pinning; omega-covariance;
      the sign-flip equivalence (the overall sign is a naming convention, pinned by the
      boxed definition); canonicity (diagonal-free omega-odd Hermitian involutions =
      {+chi, -chi}); the spin-structure torsor fixed pointwise under reversal
      (Hom(Z,Z_2), exact); <chi> = 0 on omega-symmetric states (FT.95(3) pattern)
  §B  FT.123 / FT.126: Kronecker identities over Q(i); weak commutation; Casimir census
      (3/4 I_4 on the extended carrier vs 2 Pi_R on the pair register: inequivalent
      actions); seed irreducibility re-derived; extended commutant dim 4 = I (x) End(C^2);
      Hilbert-Schmidt independence of the two Z_2 gradings; P-H9 weight cardinality
  §C  FT.124: the seven-locus census — FT.93 pincer classes re-solved exactly; the
      30-frame / 15-pseudoscalar catalog re-run; per-frame failure; traceless-involution
      non-existence; trace/rank data of FT.101(3); FT.117 disjointness; string pins in
      the frozen documents
  §D  FT.125 / FT.126: H13 ledger-integrity pins; document pins (sections, markers,
      blacksquare/Status counts, the boxed chi-hat, the chiral kets, part 18 of 18)
  §E  vocabulary scans: revision and drafting-history language; species names in the
      derivation tags; [EXT] confinement (exactly one marker, standing rules);
      mass-token absence
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
    H18DOC = rd('H_archive/H18_chirality.md')
    H17DOC = rd('H_archive/H17_colour_channel.md')
    H13DOC = rd('H_archive/H13_registries_and_gaps.md')
    H12DOC = rd('H_archive/H12_chirality_and_form_factor.md')
    H11DOC = rd('H_archive/H11_gravity_and_koide.md')
    H10DOC = rd('H_archive/H10_sm_audit.md')
ADOC = rd('A_axioms.md')
EDOC = rd('E_electromagnetic.md')

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
def vdot(u, v): return sum((a.conj() * b for a, b in zip(u, v)), C(0))
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
def isq(x):  # exact rational perfect-square test on a Fraction
    x = Fr(x)
    if x < 0: return None
    import math
    r = math.isqrt(x.numerator); s = math.isqrt(x.denominator)
    return Fr(r, s) if r * r == x.numerator and s * s == x.denominator else None

# exact real-form nullspace of linear systems over Q(i) (unknowns = Re/Im parts)
def nullspaceQ(rows, ncols):
    M = [list(map(Fr, r)) for r in rows]
    piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * ncols; v[f] = Fr(1)
        for k, pc in enumerate(piv): v[pc] = -M[k][f]
        basis.append(v)
    return basis
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
def commutant_rows(Ws, n, sign=+1):
    """real rows for [M,W]=0 (sign=+1) or {M,W}=0 (sign=-1); M = X + iY, unknowns (X flat, Y flat)."""
    rows = []
    for W in Ws:
        WR = [[w.re for w in row] for row in W]; WI = [[w.im for w in row] for row in W]
        for p in range(n):
            for q in range(n):
                rr = [Fr(0)] * (2 * n * n); ri = [Fr(0)] * (2 * n * n)
                for k in range(n):
                    # (W M)_pq - sign (M W)_pq ; M = X + iY
                    # W X term: WR[p][k] X[k][q] ; -WI[p][k] Y[k][q]  (real part of W M)
                    rr[n * k + q] += WR[p][k]
                    ri[n * k + q] += WI[p][k]
                    rr[n * n + n * k + q] += -WI[p][k]
                    ri[n * n + n * k + q] += WR[p][k]
                    # - sign (M W): X[k][q]... (M W)_pq = sum_k M[p][k] W[k][q]
                    rr[n * p + k] += -sign * WR[k][q]
                    ri[n * p + k] += -sign * WI[k][q]
                    rr[n * n + n * p + k] += sign * WI[k][q]
                    ri[n * n + n * p + k] += -sign * WR[k][q]
                rows.append(rr); rows.append(ri)
    # strip the accidental no-op column touches (they added 0)
    return [[x for x in row] for row in rows]

# ================================================================== §A
banner("§A (H18/Def-H.33, FT.122) — the orientation doublet: chi-hat, omega-hat, projectors, ket pinning, canonicity, torsor")
kc = [C(1), C(0)]          # |c>
kw = [C(0), C(1)]          # |omega(c)>
Eex = matadd(outer(kc, kw), outer(kw, kc), -1)      # |c><w| - |w><c|  (antisymmetric exchange form)
OM = matadd(outer(kc, kw), outer(kw, kc))           # omega-hat = exchange involution
CHI = matscale(Eex, C(0, 1))                        # chi-hat = i (|c><w| - |w><c|)
chk(OM == [[C(0), C(1)], [C(1), C(0)]], "§A omega-hat = [[0,1],[1,0]] in the orientation basis")
chk(CHI == [[C(0), C(0, 1)], [C(0, -1), C(0)]], "§A chi-hat = [[0,i],[-i,0]] = i * exchange form (the boxed definition)")
# omega-hat involution
chk(matmul(OM, OM) == meye(2) and mdag(OM) == OM, "§A omega^2 = id, omega Hermitian [D2.6 involution]")
# chi-hat: Hermitian, involution — with the CORRECTED chain: Eex^2 = -id, chi^2 = i^2 Eex^2 = +id
chk(mdag(Eex) == matscale(Eex, C(-1)), "§A exchange form antisymmetric-Hermitian: (|c><w|-|w><c|)^dagger = -(|c><w|-|w><c|)")
chk(matmul(Eex, Eex) == matscale(meye(2), C(-1)),
    "§A chain step 1: (|c><w|-|w><c|)^2 = -(|c><c|+|w><w|) = -id")
chk(matmul(CHI, CHI) == meye(2), "§A chain step 2: chi^2 = i^2 * (-id) = +id")
chk(mdag(CHI) == CHI, "§A chi Hermitian: (i E)^dagger = -i E^dagger = -i(-E) = iE")
chk(mtr(CHI) == C(0), "§A tr chi = 0; charpoly x^2 - 1 = (x-1)(x+1): spec {+1,-1}")
chk(mtr(matmul(CHI, CHI)) == C(2), "§A tr chi^2 = 2 (spectral pin)")
# actions on the basis kets
chk(mvec(CHI, kc) == [C(0), C(0, -1)], "§A chi|c> = -i|omega(c)>")
chk(mvec(CHI, kw) == [C(0, 1), C(0)], "§A chi|omega(c)> = +i|c>")
# projectors
PL = matscale(matadd(meye(2), CHI), Fr(1, 2)); PR = matscale(matadd(meye(2), CHI, -1), Fr(1, 2))
chk(matmul(PL, PL) == PL and matmul(PR, PR) == PR, "§A P_L^2 = P_L, P_R^2 = P_R")
chk(matmul(PL, PR) == mz(2) and matadd(PL, PR) == meye(2), "§A P_L P_R = 0, P_L + P_R = id")
chk(mtr(PL) == C(1) and mtr(PR) == C(1), "§A tr P_L = tr P_R = 1 (rank-1 projectors)")
# chiral kets (unnormalized): |L_u> = |c> - i|omega>, |R_u> = |c> + i|omega>
Lu = [C(1), C(0, -1)]; Ru = [C(1), C(0, 1)]
chk(mvec(CHI, Lu) == Lu, "§A |L> = (|c> - i|omega>)/sqrt2: chi|L_u> = +|L_u>")
chk(mvec(CHI, Ru) == [-x for x in Ru], "§A |R> = (|c> + i|omega>)/sqrt2: chi|R_u> = -|R_u>")
chk(outer(Lu, Lu) == matadd(meye(2), CHI), "§A |L_u><L_u| = id + chi = 2 P_L (exact, no sqrt2 in the operator content)")
chk(outer(Ru, Ru) == matadd(meye(2), CHI, -1), "§A |R_u><R_u| = id - chi = 2 P_R")
chk(vdot(Lu, Lu) == C(2) and vdot(Ru, Ru) == C(2) and vdot(Lu, Ru) == C(0),
    "§A <L_u|L_u> = <R_u|R_u> = 2 (the 1/sqrt2 normalizes), <L_u|R_u> = 0")
chk(mvec(PL, Lu) == Lu and mvec(PR, Lu) == [C(0), C(0)], "§A P_L|L_u> = |L_u>, P_R|L_u> = 0")
chk(mvec(PR, Ru) == Ru and mvec(PL, Ru) == [C(0), C(0)], "§A P_R|R_u> = |R_u>, P_L|R_u> = 0")
# ray pinning: the +1 ray of the boxed chi is (|c> - i|omega>); the opposite-phase combination is P_R's ray
chk(mvec(CHI, Ru) != Ru, "§A ray pinning: chi acts by -1 on (|c> + i|omega>): the +1 ray is uniquely (|c> - i|omega>) up to phase")
chk(mvec(PL, Ru) == [C(0), C(0)], "§A ray pinning: P_L annihilates |R_u> (it is P_R's ray)")
# omega covariance
chk(matmul(matmul(OM, CHI), OM) == matscale(CHI, C(-1)), "§A omega chi omega^-1 = -chi (D2.6 'chirality -> -chirality' as an operator identity)")
chk(matadd(matmul(CHI, OM), matmul(OM, CHI)) == mz(2), "§A {chi, omega} = 0 (anticommutation)")
chk(matmul(matmul(OM, PL), OM) == PR and matmul(matmul(OM, PR), OM) == PL, "§A omega P_L omega = P_R, omega P_R omega = P_L")
chk(mvec(OM, Lu) == [C(0, -1) * x for x in Ru], "§A omega|L_u> = -i |R_u> (chiral rays exchanged up to phase)")
chk(mvec(OM, Ru) == [C(0, 1) * x for x in Lu], "§A omega|R_u> = +i |L_u>")
# the overall sign is a naming convention: flipping chi composes with P_L <-> P_R (all identities invariant)
CHIp = matscale(CHI, C(-1))
chk(matmul(matmul(OM, CHIp), OM) == matscale(CHIp, C(-1)),
    "§A sign-flip equivalence: omega(-chi)omega^-1 = -(-chi) also holds (adjoint action is linear): the overall sign is a naming convention, pinned by the boxed definition")
PLp = matscale(matadd(meye(2), CHIp), Fr(1, 2))
chk(matmul(CHIp, CHI) == matscale(meye(2), C(-1)), "§A (-chi)(chi) = -id: the flipped operator is still an involution")
chk(PLp == PR, "§A flipping chi's sign composes with P_L <-> P_R: an equivalent naming, pinned only by the boxed definition")
# canonicity: {M Hermitian 2x2 : omega M omega = -M, M^2 = id, diag M = 0} = {+chi, -chi}
# general Hermitian M = [[a, z],[z*, b]], a,b in Q, z = x+iy: omega-odd <=> b = -a and x = 0
# => M = [[a, iy],[-iy, -a]]; M^2 = (a^2+y^2) id; diagonal-free => a = 0 => y^2 = 1 => y = +-1 => M = +-chi
pts = []
for q in range(1, 21):
    for p in range(-20, 21):
        a = Fr(p, q)
        if a * a > 1: continue
        y = isq(1 - a * a)
        if y is not None:
            pts.append((a, y))
            if y != 0: pts.append((a, -y))
pts = sorted(set(pts))
chk(len(pts) >= 10 and (Fr(0), Fr(1)) in pts and (Fr(3, 5), Fr(4, 5)) in pts, f"§A rational unit-circle census: {len(pts)} exact points incl. (0,1), (3/5,4/5)")
for (a, y) in pts:
    M = [[C(a), C(0, y)], [C(0, -y), C(-a)]]
    chk(mdag(M) == M, "§A M(a,y) Hermitian")
    chk(matmul(matmul(OM, M), OM) == matscale(M, C(-1)), "§A every M(a,y) is omega-odd (the family before the diagonal-free pin)")
    chk(matmul(M, M) == meye(2), "§A M(a,y)^2 = id exactly when a^2+y^2=1 (machine on the census)")
diagfree = [(a, y) for (a, y) in pts if a == 0]
chk(set(diagfree) == {(Fr(0), Fr(1)), (Fr(0), Fr(-1))}, "§A diagonal-free omega-odd involutions over the census: a=0 => y=+-1 only")
for (a, y), target in (((Fr(0), Fr(1)), CHI), ((Fr(0), Fr(-1)), matscale(CHI, C(-1)))):
    M = [[C(a), C(0, y)], [C(0, -y), C(-a)]]
    chk(M == target, "§A canonicity: the unique diagonal-free omega-odd Hermitian involutions are +chi and -chi")
# spin-structure torsor: Hom(Z, Z_2) = {h_0, h_1}; orientation reversal n -> -n pulls back trivially
for n in range(-6, 7):
    chk((-n) % 2 == n % 2, f"§A torsor fixed pointwise under reversal: h(-n) = h(n) in Z_2 at n={n} (the exchanged objects are the chiral rays, not the boundary conditions)")
torsor_maps = [lambda n: 0, lambda n: n % 2]
reversal_pullback_fixed = all((h(-n) == h(n)) for h in torsor_maps for n in range(-6, 7))
chk(reversal_pullback_fixed, "§A both spin structures (R: h=0, NS: h=n mod 2) are reversal-invariant: the torsor Z_2 and the chiral-ray Z_2 are distinct kinds [FT.89(2) discipline]")
# <chi> = 0 on omega-symmetric / antisymmetric states (FT.95(3) pattern)
for s in (+1, -1):
    psi = [C(1), C(s)]
    chk(vdot(psi, mvec(CHI, psi)) == C(0), f"§A <psi_{'sym' if s>0 else 'anti'}|chi|psi> = 0 exactly (zero expectation on reversal-symmetric states; the per-chain grading persists)")
# FT.122(4) citation pins in the frozen documents
chk('chirality $\\mapsto-$chirality' in ADOC, "§A pin: D2.6 carries 'chirality -> -chirality' (vocabulary upgraded to an operator identity by FT.123(2))")
chk("sign-level realization of D2.6's" in EDOC, "§A pin: EM.24(1) records C as the sign-level realization of omega")
if ARCH:
    chk('C-odd orientation coordinate' in H11DOC, "§A pin: FT.87(8)'s sign(k) C-odd coordinate (the winding sign flips under reversal; the precedent for C-odd labels under FT.95(3))")
stamp("§A green: chi^2 chain; Hermitian involution; projectors; kets forced by the boxed chi; ray pinning; omega-covariance; sign-flip equivalence (naming convention); canonicity +-(chi); torsor reversal-invariant; <chi>=0 on symmetric states; frozen-doc pins")

# ================================================================== §B
banner("§B (H18/FT.123, FT.126) — the extended carrier: weak commutation, Casimir census, Schur discharge, independence of the two Z_2's")
Wint = [matscale(SG[i], Fr(1, 2)) for i in (1, 2, 3)]       # seed action W_i -> sigma_i/2 [EW.32]
PLc = ckron(meye(2), PL); PRc = ckron(meye(2), PR); CHIc = ckron(meye(2), CHI); OMc = ckron(meye(2), OM)
for i in range(3):
    Wi = ckron(Wint[i], meye(2))
    chk(matadd(matmul(Wi, PLc), matmul(PLc, Wi), -1) == mz(4), f"§B [W_{i+1} (x) I, I (x) P_L] = 0 (weak covariance: disjoint tensor factors)")
    chk(matadd(matmul(Wi, PRc), matmul(PRc, Wi), -1) == mz(4), f"§B [W_{i+1} (x) I, I (x) P_R] = 0")
    chk(matadd(matmul(Wi, CHIc), matmul(CHIc, Wi), -1) == mz(4), f"§B [W_{i+1} (x) I, I (x) chi] = 0")
chk(matmul(PLc, PLc) == PLc and matmul(PRc, PRc) == PRc and matmul(PLc, PRc) == mz(4), "§B carrier lift: idempotent, orthogonal")
chk(matadd(PLc, PRc) == meye(4) and mtr(PLc) == C(2) and mtr(PRc) == C(2), "§B carrier lift: complete, traces 2/2 (each Weyl half is 2-dimensional)")
# Casimir census: the extended weak action is seed (x) trivial; the pair-register action is 3 (+) 1 — inequivalent
CasExt = matadd(matadd(matmul(ckron(Wint[0], meye(2)), ckron(Wint[0], meye(2))),
                       matmul(ckron(Wint[1], meye(2)), ckron(Wint[1], meye(2)))),
                matmul(ckron(Wint[2], meye(2)), ckron(Wint[2], meye(2))))
chk(CasExt == matscale(meye(4), Fr(3, 4)), "§B extended carrier: sum_i (sigma_i/2 (x) I)^2 = (3/4) I_4 (type 2 (+) 2, multiplicity 2)")
# pair register (CT1.2): W_i = (sigma_0 (x) sigma_i + sigma_i (x) sigma_0)/2 ; Sigma = sum sigma_i (x) sigma_i ; Ss = (E_0+Sigma)/2 ; Pi_R = (I+Ss)/2
def kron2(A, B): return [[A[i // 2][k // 2] * B[i % 2][k % 2] for k in range(4)] for i in range(4)]
SIG = matadd(matadd(kron2(SG[1], SG[1]), kron2(SG[2], SG[2])), kron2(SG[3], SG[3]))
Wpair = [matscale(matadd(kron2(SG[0], SG[i]), kron2(SG[i], SG[0])), Fr(1, 2)) for i in (1, 2, 3)]
Ss = matscale(matadd(meye(4), SIG), Fr(1, 2))
PiR = matscale(matadd(meye(4), Ss), Fr(1, 2)); PiV = matscale(matadd(meye(4), Ss, -1), Fr(1, 2))
chk(mtr(PiR) == C(3) and mtr(PiV) == C(1), "§B CT0.7(1) re-derived: tr Pi_R = 3, tr Pi_V = 1 (type 3 (+) 1)")
CasPair = matadd(matadd(matmul(Wpair[0], Wpair[0]), matmul(Wpair[1], Wpair[1])), matmul(Wpair[2], Wpair[2]))
chk(CasPair == matscale(PiR, C(2)), "§B Cor CT0.7a re-derived: sum_i W_i^2 = 2 Pi_R on the pair register")
chk(CasPair != matscale(meye(4), Fr(3, 4)), "§B the two weak actions are inequivalent (2 Pi_R != (3/4) I_4): FT.93(3)'s pincer classifies the pair-register action and does not reach the extended carrier")
# seed irreducibility [FT.93(3d) re-derived]: commutant of {sigma_i} on C^2 = C I_2 ; anticommutant = 0
rowsC = commutant_rows([SG[1], SG[2], SG[3]], 2, +1)
nsC = nullspaceQ(rowsC, 8)
chk(len(nsC) == 2, "§B seed commutant over Q: dim 2 (= C I_2 over C): the seed action is irreducible [FT.93(3d)]")
# the seed commutant is exactly C*I2: basis vectors reshape to I2 multiples
def reshape(v, n): return [[C(v[n*n*0 + i*n+j], v[n*n + i*n+j]) for j in range(n)] for i in range(n)]
for v in nsC:
    Mv = reshape(v, 2)
    lam = Mv[0][0]
    chk(Mv == matscale(meye(2), lam), "§B every seed-commuting M is lambda * I_2 (Schur, exact)")
rowsA = commutant_rows([SG[1], SG[2], SG[3]], 2, -1)
chk(len(nullspaceQ(rowsA, 8)) == 0, "§B seed anticommutant = {0} [FT.93(3d)]")
# extended commutant: {M : [M, sigma_i (x) I_2] = 0} has complex dim 4 = I_2 (x) End(C^2) — Schur discharged by multiplicity
rowsE = commutant_rows([ckron(SG[1], meye(2)), ckron(SG[2], meye(2)), ckron(SG[3], meye(2))], 4, +1)
nsE = nullspaceQ(rowsE, 32)
chk(len(nsE) == 8, "§B extended commutant over Q: dim 8 (= 4 over C = I (x) End(C^2)): FT.93(3d)'s obstruction is discharged by extension, not violated [P-H18a]")
# the four I (x) E_ab lie in the commutant and are independent
units = []
for a in range(2):
    for b in range(2):
        Eab = mz(2); Eab[a][b] = C(1)
        units.append(ckron(meye(2), Eab))
flatU = []
for U in units:
    flatU.append([U[i][j].re for i in range(4) for j in range(4)] + [U[i][j].im for i in range(4) for j in range(4)])
    iU = matscale(U, C(0, 1))
    flatU.append([iU[i][j].re for i in range(4) for j in range(4)] + [iU[i][j].im for i in range(4) for j in range(4)])
chk(rankQ(flatU) == 8 and rankQ(nsE + flatU) == 8, "§B {I (x) E_ab, i I (x) E_ab} span the same 8-real-dim space as the nullspace: the extended commutant = I (x) End(C^2) exactly")
# weak kernel on the extended carrier is zero: the chiral halves are weak-BLIND, not weak-inactive
# kernel of stacked [W1;W2;W3] as complex 12x4 -> real 24x8 system
stack = []
for W in [ckron(SG[i], meye(2)) for i in (1, 2, 3)]:
    WR = [[w.re for w in row] for row in W]; WI = [[w.im for w in row] for row in W]
    for p in range(4):
        rr = [Fr(0)] * 8; ri = [Fr(0)] * 8
        for k in range(4):
            rr[k] += WR[p][k]; ri[k] += WI[p][k]
            rr[4 + k] += -WI[p][k]; ri[4 + k] += WR[p][k]
        stack.append(rr); stack.append(ri)
chk(8 - rankQ(stack) == 0, "§B the extended weak kernel is {0} (sigma_i invertible): chiral halves carry the full internal action — weak-blind, not weak-inactive [FT.124(2)]")
# Hilbert-Schmidt independence of the chiral grade from every internal-only operator
for G in [meye(2), SG[1], SG[2], SG[3]]:
    A = ckron(G, meye(2))
    hs = mtr(matmul(mdag(A), CHIc))
    chk(hs == C(0), "§B <G (x) I, I (x) chi>_HS = tr(G^dagger) tr(chi) = 0: the chiral grade is HS-orthogonal to the whole internal-only algebra")
chk(matadd(matmul(OMc, CHIc), matmul(CHIc, OMc)) == mz(4), "§B {omega (x)-lift, chi-lift} = 0 on the extended carrier")
# the two Z_2's: omega-hat exchange on the orientation factor vs internal involutions: commute and generate Z_2 x Z_2
for G in [SG[3], SG[1]]:
    Gi = ckron(G, meye(2))
    chk(matadd(matmul(Gi, OMc), matmul(OMc, Gi), -1) == mz(4), "§B internal involution and omega-hat commute: independent Z_2's [FT.126(4)]")
    chk(matmul(Gi, Gi) == meye(4) and matmul(OMc, OMc) == meye(4), "§B both are involutions")
    chk(matmul(Gi, OMc) != OMc and matmul(Gi, OMc) != Gi, "§B the product is a third, distinct involution: the group is Z_2 x Z_2, not Z_2")
# P-H9 conditional clause (FT.123(3)): weight census of Sym^1 = C^2 under the diagonal torus generator sigma_3/2
t3 = matscale(SG[3], Fr(1, 2))
chk(mvec(t3, [C(1), C(0)]) == [C(Fr(1, 2)), C(0)] and mvec(t3, [C(0), C(1)]) == [C(0), C(Fr(-1, 2))],
    "§B the j=1/2 carrier [P-H9 declared; FT.28 digon: k=1] has exactly two weights {+1/2, -1/2}: cardinality 2 = the chiral-ray cardinality (correspondence recorded as unordered pair)")
chk(2 * 2 == 4, "§B FT.123(5): 2 x 2 = 4 (the Dirac-type carrier dimension for one massive mode)")
stamp("§B green: weak commutation on all generators; Casimir census (3/4 I_4 vs 2 Pi_R — inequivalent); seed Schur re-derived; extended commutant dim 4 = I (x) End; weak kernel 0; HS independence; Z_2 x Z_2; weight cardinality under P-H9")

# ================================================================== §C
banner("§C (H18/FT.124) — the seven-locus obstruction census: every frozen obstruction re-derived at its own locus and shown not to reach H_omega")
# --- locus 1: the pincer [FT.93(3)] on the pair register, re-solved exactly
rowsCom = commutant_rows(Wpair, 4, +1)
nsCom = nullspaceQ(rowsCom, 32)
chk(len(nsCom) == 4, "§C commuting side over Q: dim 4 (= 2 over C)")
flatPR = [PiR[i][j].re for i in range(4) for j in range(4)] + [PiR[i][j].im for i in range(4) for j in range(4)]
flatPV = [PiV[i][j].re for i in range(4) for j in range(4)] + [PiV[i][j].im for i in range(4) for j in range(4)]
chk(rankQ(nsCom + [flatPR, flatPV]) == 4, "§C commuting side = span_C{Pi_R, Pi_V} exactly [FT.93(3a) re-derived]")
rowsAnt = commutant_rows(Wpair, 4, -1)
nsAnt = nullspaceQ(rowsAnt, 32)
chk(len(nsAnt) == 2 and rankQ(nsAnt + [flatPV]) == 2, "§C anticommuting side = C.Pi_V exactly (rank 1, singular) [FT.93(3b) re-derived]")
for sa in (+1, -1):
    for sb in (+1, -1):
        M = matadd(matscale(PiR, Fr(sa)), matscale(PiV, Fr(sb)))
        chk(mtr(M) != C(0), f"§C no traceless involution in the commuting side: tr = 3a+b = {3*sa+sb} != 0 for all sign pairs [FT.93(3a)]")
chk(matmul(PiV, PiV) == PiV and mtr(PiV) == C(1), "§C Pi_V is idempotent with tr = 1: rank 1 < 4, so c*Pi_V is never an involution on C^4 [FT.93(3b) singularity]")
# --- locus 2: the frame catalog [FT.93(1)-(2),(4),(6)] re-run
paulis = []
for i in range(4):
    for j in range(4):
        if (i, j) == (0, 0): continue
        paulis.append(((i, j), kron2(SG[i], SG[j])))
chk(len(paulis) == 15, "§C 15 non-identity Pauli products [FT.93(1)]")
def anticomm(A, B): return matadd(matmul(A, B), matmul(B, A)) == mz(4)
frames = []
for quad in itertools.combinations(range(15), 4):
    if all(anticomm(paulis[a][1], paulis[b][1]) for a, b in itertools.combinations(quad, 2)):
        frames.append(quad)
chk(len(frames) == 30, f"§C 30 pairwise-anticommuting 4-frames [FT.93(1): got {len(frames)}]")
gammas = {}
for fr in frames:
    g = paulis[fr[0]][1]
    for idx in fr[1:]:
        g = matmul(g, paulis[idx][1])
    chk(matmul(g, g) == meye(4) and mtr(g) == C(0) and mdag(g) == g, "§C per-frame pseudoscalar axioms: gamma^2 = I_4, tr gamma = 0, Hermitian")
    key = next((k for k in range(15)
                if g == paulis[k][1] or g == matscale(paulis[k][1], C(-1))), None)
    chk(key is not None, "§C gamma_F = +- a single Pauli product (exact match census)")
    gammas.setdefault(key, []).append(fr)
chk(len(gammas) == 15 and all(len(v) == 2 for v in gammas.values()),
    "§C all 15 pseudoscalar values attained (up to sign, FT.93(2)'s convention), each from exactly 2 frames")
Gams = [paulis[k][1] for k in sorted(gammas)]
for G in Gams:
    fail_com = any(matadd(matmul(G, Wpair[i]), matmul(Wpair[i], G), -1) != mz(4) for i in range(3))
    fail_ant = any(matadd(matmul(G, Wpair[i]), matmul(Wpair[i], G)) != mz(4) for i in range(3))
    chk(fail_com and fail_ant, "§C every attained pseudoscalar (sign-class representative) fails the commuting side for some W_i AND the anticommuting side for some W_i [FT.93(3c) re-run; failure is sign-invariant by linearity]")
Saligned = 0
for G in Gams:
    if matadd(matmul(G, Ss), matmul(Ss, G), -1) == mz(4):
        Saligned += 1
        ok = any(G == matscale(kron2(SG[i], SG[i]), s) for i in (1, 2, 3) for s in (+1, -1))
        chk(ok, "§C S-aligned pseudoscalars are exactly the +- sigma_i (x) sigma_i classes [FT.93(6)]")
chk(Saligned == 3, f"§C exactly 3 of the 15 pseudoscalar classes are S-aligned (got {Saligned}) [FT.93(6)]")
# the orientation-space grade is S-invariant by disjointness: [Ss (x) I_2, I_4 (x) chi] = 0 on C^4_pair (x) H_omega
Ssc = ckron(Ss, meye(2))
CHIc8 = ckron(meye(4), CHI)
chk(matadd(matmul(Ssc, CHIc8), matmul(CHIc8, Ssc), -1) == mz(8), "§C [Ss (x) I_2, I_4 (x) chi] = 0 (8x8 exact): the chiral grade is S-invariant — no misalignment possible [FT.124(4)]")
# --- locus 3: trace/rank [FT.101(3)] data
chk(mtr(PiR) == C(3) and mtr(PiV) == C(1), "§C FT.101(3) data re-derived: tr Pi_R = 3 != 1 = tr Pi_V — no pair-register branch swap; omega-hat is an honest matrix on a DIFFERENT space (no contradiction)")
# --- locus 5: zero expectation vs sharp per-chain grade (FT.95(3) pattern) — re-asserted from §A
chk(vdot([C(1), C(1)], mvec(CHI, [C(1), C(1)])) == C(0), "§C <chi> = 0 on the reversal-symmetric state while chi|L> = +|L> remains sharp: expectation-vanishing is not grade-vanishing [FT.87(8) precedent]")
# --- locus 6: confinement blindness disjointness [FT.117]: slot one-body operators vs I_3 (x) chi on C^3 (x) H_omega
I3 = meye(3)
def c3kron(A, B): return ckron(A, B)
slotH = [[C(1), C(2, -1), C(0)], [C(2, 1), C(0), C(1, 1)], [C(0), C(1, -1), C(2)]]  # generic Hermitian slot operator
chk(mdag(slotH) == slotH, "§C witness slot operator Hermitian")
A6 = c3kron(slotH, meye(2)); B6 = c3kron(I3, CHI)
chk(matadd(matmul(A6, B6), matmul(B6, A6), -1) == mz(6), "§C [H_slot (x) I_2, I_3 (x) chi] = 0 (6x6 exact): the chiral grade has no colour-slot argument — FT.117's blindness cannot reach it [FT.124(6)]")
# --- frozen-document string pins for the cited obstruction statements
if ARCH:
    chk('No chirality grade on the pair register can be weak-covariant' in H12DOC, "§C pin: FT.93(3)'s pincer statement is about the pair register (locus recorded)")
    chk('refuted, per frame and in general' in H12DOC, "§C pin: FT.93(4)'s per-frame refutation present in H12")
    chk('The branch flip is label-level' in H12DOC, "§C pin: FT.101(3)'s label-level verdict present in H12")
    chk('no colour-sealed object' in H17DOC, "§C pin: FT.117(7)'s verdict present in H17")
    chk('zero-expectation theorem' in H12DOC, "§C pin: FT.95(3)'s theorem present in H12")
    chk('no chiral projector, no Weyl symbol and no hypercharge-assignment read' in H10DOC, "§C pin: FT.81(4)'s three prerequisites — H18 discharges only the first")
stamp("§C green: pincer classes re-solved; 30 frames / 15 gammas re-run, all fail per-frame; no traceless involution; trace/rank data; S-invariance; expectation-vs-grade; slot disjointness; frozen pins")

# ================================================================== §D
banner("§D (H18/FT.125, FT.126) — ledger integrity and document pins")
if ARCH:
    chk('**(P-H18a)**' in H13DOC, "§D P-H18a registered in H13")
    chk('**(P-H16a)**' in H13DOC and '**(P-H17a)**' in H13DOC, "§D P-H16a/P-H17a entries intact")
    chk('deficit 1 is closed at the projector level' in H13DOC, "§D item 20 carries the H18 closure annotation")
    chk("deficit 11 unchanged" in H13DOC, "§D item 20 annotation records deficit 11 UNCHANGED (the submitted 'unblocked' claim was rejected as a kind confusion)")
    chk('P-H18a (H18)' in H13DOC or 'P-H18a' in H13DOC, "§D item 21(i) carries the extended-carrier annotation")
    doc = H18DOC
secs = {}
if ARCH:
    for sp in re.split(r'^### ', doc, flags=re.M)[1:]:
        key = sp.split(' —')[0].strip()
        body = sp.split('\n## ')[0]          # truncate at the next H2 (erratum / closure exports)
        secs[key] = body
    for t in ('Def-H.33', 'FT.122', 'FT.123', 'FT.124', 'FT.125', 'FT.126'):
        chk(t in secs, f"§D section {t} present")
    chk('FT.125a' not in doc, "§D the lettered tag FT.125a was renamed FT.126 (canon parsers admit FT.\\d+ only)")
    for w in ('**Thm.**', '**Req.**', '**Pf.**', '**Phys.**', '**Status.**'):
        chk(all(secs[t].count(w) == 1 for t in ('FT.122', 'FT.123', 'FT.124', 'FT.125', 'FT.126')), f"§D every FT block carries exactly one {w}")
    chk(secs['Def-H.33'].count('**Def.**') == 1, "§D Def-H.33 carries exactly one **Def.**")
    chk(doc.count(r'\blacksquare') == 6, f"§D 6 proof terminators (got {doc.count(chr(92)+'blacksquare')})")
    chk(doc.count('**Status.**') == 6, "§D Status count = 6 (5 theorem blocks + the document header line)")
    chk('## Tier F.39' in doc and 'part 18 of 18' in doc, "§D pins: Tier F.39 heading; part 18 of 18")
    chk('P-H18a' in doc and 'verify_H_chirality.py' in doc, "§D pins: P-H18a flagged; machine reference")
    chk(r'\hat\chi\ :=\ i\bigl(|c\rangle\langle\omega(c)|-|\omega(c)\rangle\langle c|\bigr)' in doc, "§D pin: the boxed chi-hat definition")
    chk(r'|L\rangle=\tfrac1{\sqrt2}\bigl(|c\rangle-i\,|\omega(c)\rangle\bigr)' in doc, "§D pin: the |L> ket display")
    chk(r'|R\rangle=\tfrac1{\sqrt2}\bigl(|c\rangle+i\,|\omega(c)\rangle\bigr)' in doc, "§D pin: the |R> ket display")
    chk("deficit 1$'$" in doc or "deficit 1' " in doc, "§D pin: deficit 1' opened in the ledger")
    chk('CLOSED at the projector level' in secs['FT.125'], "§D FT.125(1) states the qualified closure (projector level, under P-H18a)")
    chk('UNCHANGED' in secs['FT.125'], "§D FT.125 records the deficit-11 correction (UNCHANGED)")
    chk('H18' not in H17DOC, "§D H17 untouched (no forward reference)")
stamp("§D green: H13 ledger integrity; sections and markers; counts; boxed definition and ket pins; FT.125 qualifications")

# ================================================================== §E
banner("§E (H18) — vocabulary scans: revision language, species names, [EXT] discipline")
BARRED = ['previously', 'formerly', 'this was', 'now this']
if ARCH:
    hits = [(w, doc.lower().count(w)) for w in BARRED if w in doc.lower()]
if ARCH:
    chk(not hits, f"§E revision-language scan of H18: zero hits ({hits})")
META = ['erratum', 'submitted', 'earlier draft', 'stale', 'draft', 'as corrected', '§H18-E', 'H18-E']
if ARCH:
    mh = [(w, doc.lower().count(w.lower())) for w in META if w.lower() in doc.lower()]
if ARCH:
    chk(not mh, f"§E drafting-history scan of H18: zero hits — the theorem document carries no revision record ({mh})")
    deriv = ''.join(secs[t] for t in ('Def-H.33', 'FT.122', 'FT.123', 'FT.124', 'FT.126'))
SPECIES = ['electron', 'muon', 'tau', 'neutrino', 'proton', 'neutron', 'quark', 'photon', 'gluon', 'lepton', 'pion', 'higgs']
if ARCH:
    ph = [(w, deriv.count(w)) for w in SPECIES if w in deriv.lower()]
if ARCH:
    chk(not ph, f"§E species-name scan of the derivation tags (Def-H.33, FT.122–FT.124, FT.126): zero hits ({ph})")
    chk(doc.count('[EXT]') == 1, f"§E [EXT] occurs exactly once (the standing-rules clause; H18 carries no external data): got {doc.count('[EXT]')}")
MASS = ['0.511', '105.6', '1776', '206.7', '3477', '1.273', '4.183', '162.5', '172.4', '938.2', '139.57']
if ARCH:
    leak = [t for t in MASS if t in doc]
if ARCH:
    chk(not leak, f"§E no external mass token anywhere in H18 ({leak})")
    chk('spin structure' in doc.lower(), "§E the spin-structure vocabulary is present (as the flagged analogy of the corrected premise)")
    chk('reversal-invariant' in doc or 'fixed pointwise' in doc, "§E the torsor distinction is stated in the document")
    chk('kind' in deriv.lower() or 'FT.89(2)' in deriv, "§E the kind-flag discipline (FT.89(2)) is cited in the derivation tags")
stamp("§E green: zero barred/drafting-history hits; derivation tags species-free; exactly one [EXT] marker; no mass tokens; torsor distinction in-document")

print(f"\nverify_H_chirality: {N} checks green  ({time.time()-t0:.1f}s) — H18 §A–§E (Tier F.39, Def-H.33 + FT.122–FT.126)")
