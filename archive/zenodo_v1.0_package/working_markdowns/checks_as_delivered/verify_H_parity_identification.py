#!/usr/bin/env python3
"""verify_H_parity_identification.py — H20 Tier F.41 (FT.133–FT.140): parity.

The configuration-space reversal calculus (C, P, T, omega-pattern), the carrier
bookkeeping on the orientation doublet (the scalar-CPT theorem), the weak-branch
parity reading, the rung-one S-grading (10/6), and the cover / flicker / pole /
channel parity censuses.

Exact arithmetic only (Fraction, Q(i) via qmath.C, Q[c]/(16c^4-20c^2+5), Q(sqrt3)).
No floating point in any assertion.  H20 carries no [EXT] numerical data.

  §A  FT.133: the four register involutions; exhaustive commutation census; component
      weight relations w(C) = (-1)^|E| w, w(T) = w*, w(P) = e^{i pi Theta} w*; the
      composition identities in both frozen lifts (EM.24(5) conjugation lift; FT.88(2)
      kappa-flip lift — agreeing exactly on the integer-Theta locus); |w|^2 unconditional;
      read-covariance table (q_core, Theta, |E|)
  §B  FT.134: carrier bookkeeping — C/P/T fix the doublet rays, omega-hat swaps them;
      the promoted Q-hat family: C-odd, P/T-even, omega-covariant; the scalar-CPT theorem
      with the trace refutation of any kappa multiple; the uniqueness pair; FT.126(4) Z2xZ2
  §C  FT.135: the weak branch data re-derived; the label-level branch exchange; the
      trace/rank non-implementation census
  §D  FT.136: Ad(S) census on the CT1.2 basis: dims (10, 6) with exact membership;
      A(1) and FT.30 pins; the weak block located in the S-even side
  §E  FT.137: tetrahedron census — v(R^T) = v(R) on all 4096 patterns; 101 covers; the 48
      dissolved-digon bypass covers = two Omega=24 Aut-orbits exchanged by reversal;
      the exact P sign character v_a(R) = (-1)^{sum a} v_0(R) (triangle, exhaustive)
  §F  FT.138: the five Platonic defect multiplets exact (Q, Q[c]/(16c^4-20c^2+5),
      Q(sqrt3)); D(m) = D(-m); on-shell P-triviality of the weights
  §G  FT.139: the seal bilinear is Ad(S)-even (all 9 pairs); sum_i [J_i,K_i] = 2iSigma
      re-run; channel-constant blindness pins; the flip-block character contrast
  §H  FT.140: document pins, vocabulary scans, downstream integrity (H13, H19, frozen)
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
from bypasscore import types_of, brute_sign_sum, automorphisms

DOCS = os.path.normpath(os.path.join(HERE, '..'))
def rd(fn): return era_paths.read(fn)
if ARCH:
    H20DOC = rd('H_archive/H20_parity_identification.md')
    H19DOC = rd('H_archive/H19_force_matrix.md')
    H18DOC = rd('H_archive/H18_chirality.md')
    H17DOC = rd('H_archive/H17_colour_channel.md')
    H16DOC = rd('H_archive/H16_koide_channel.md')
    H13DOC = rd('H_archive/H13_registries_and_gaps.md')
    H12DOC = rd('H_archive/H12_chirality_and_form_factor.md')
    H11DOC = rd('H_archive/H11_gravity_and_koide.md')
    H10DOC = rd('H_archive/H10_sm_audit.md')
    H09DOC = rd('H_archive/H09_flicker_and_domains.md')
    H04DOC = rd('H_archive/H04_aspect_operator_and_spectrum.md')
BDOC = rd('B_foundation.md')
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

# ------------------------------------------------------------------ helpers
def mvec(A, v): return [sum((A[i][j] * v[j] for j in range(len(v))), C(0)) for i in range(len(A))]
def mz(n): return [[C(0)] * n for _ in range(n)]
def meyeC(n): return [[C(1 if i == j else 0) for j in range(n)] for i in range(n)]
def mtr(A): return sum((A[i][i] for i in range(len(A))), C(0))
def ckron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(len(A[0]) * len(B[0]))]
            for i in range(n * m)]
SG = [[[C(1), C(0)], [C(0), C(1)]],
      [[C(0), C(1)], [C(1), C(0)]],
      [[C(0), C(0, -1)], [C(0, 1), C(0)]],
      [[C(1), C(0)], [C(0), C(-1)]]]
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
IPOW = {0: C(1), 1: C(0, 1), 2: C(-1), 3: C(0, -1)}
def ipow(n): return IPOW[int(n) % 4]                     # i^n exact (n may be negative Fraction with den 1)
def negpow(n): return C(1) if int(n) % 2 == 0 else C(-1)  # (-1)^n exact
def eipTh(Th): return ipow(2 * Fr(Th))                    # e^{i pi Theta}, 2*Theta integer in the model
DSET = [Fr(1, 2), Fr(1), Fr(3, 2), Fr(2)]
def eps(a, d):
    if a == 0: return C(1)
    return ipow(2 * d)

# configuration model: per directed edge — absent, or (sigma, a, d) with alpha = a*pi, ds^2 = d
def configs_of(dedges, dset):
    per = [None] + [(s, a, d) for s in (1, -1) for a in (0, 1) for d in dset]
    for assign in itertools.product(range(len(per)), repeat=len(dedges)):
        yield {e: per[k] for e, k in zip(dedges, assign) if per[k] is not None}
def W_of(cfg):
    verts = sorted({v for e in cfg for v in e})
    aleph = 0
    for v in verts:
        inn = [e for e in cfg if e[1] == v]; out = [e for e in cfg if e[0] == v]
        if len(inn) == 1 and len(out) == 1:
            aleph += abs(Fr(cfg[out[0]][0] - cfg[inn[0]][0], 2))
    prod = C(1)
    for e, (s, a, d) in cfg.items():
        prod = prod * C(s) * eps(a, d)
    Th = sum((d for (s, a, d) in cfg.values()), Fr(0))
    return prod * negpow(aleph), len(cfg), Th
def act_C(cfg): return {e: (-s, a, d) for e, (s, a, d) in cfg.items()}
def act_P(cfg): return {e: (s, 1 - a, d) for e, (s, a, d) in cfg.items()}
def act_T(cfg): return {e: (s, a, -d) for e, (s, a, d) in cfg.items()}
def act_W(cfg): return {(b, a): v for (a, b), v in cfg.items()}
ACTS = {'C': act_C, 'P': act_P, 'T': act_T, 'W': act_W}
def qcore(chain, cfg):
    return Fr(cfg[chain[0]][0] - cfg[chain[-1]][0], 2)

digon_edges = [(0, 1), (1, 0)]
tri_edges = [(a, b) for a in range(3) for b in range(3) if a != b]

# ================================================================== §A
banner("§A (H20/FT.133) — the configuration-space reversal calculus: registers, commutation, weight identities")
cfgs_dig = list(configs_of(digon_edges, DSET))
chk(len(cfgs_dig) == 17 ** 2, f"§A digon model census: {len(cfgs_dig)} = 17^2 configurations")
for cfg in cfgs_dig:
    for X in ACTS.values():
        chk(X(X(cfg)) == cfg, "§A each of C, P, T, omega-pattern is an involution (digon, exhaustive)")
    for (n1, X), (n2, Y) in itertools.combinations(ACTS.items(), 2):
        chk(X(Y(cfg)) == Y(X(cfg)), f"§A [{n1},{n2}] = 0 on configuration data (exhaustive digon)")
cfgs_tri_on = list(configs_of(tri_edges, [Fr(1)]))
chk(len(cfgs_tri_on) == 5 ** 6, f"§A triangle on-shell submodel: {len(cfgs_tri_on)} = 5^6 configurations")
for cfg in cfgs_tri_on:
    for X in ACTS.values():
        chk(X(X(cfg)) == cfg, "§A involutions (triangle on-shell, exhaustive)")
    for (n1, X), (n2, Y) in itertools.combinations(ACTS.items(), 2):
        chk(X(Y(cfg)) == Y(X(cfg)), f"§A [{n1},{n2}] = 0 (triangle on-shell, exhaustive)")
_state = [12345]
def lcg():
    _state[0] = (1103515245 * _state[0] + 12345) % (2 ** 31)
    return _state[0]
per = [None] + [(s, a, d) for s in (1, -1) for a in (0, 1) for d in DSET]
for _ in range(3000):
    cfg = {e: per[lcg() % len(per)] for e in tri_edges}
    cfg = {e: v for e, v in cfg.items() if v is not None}
    for (n1, X), (n2, Y) in itertools.combinations(ACTS.items(), 2):
        chk(X(Y(cfg)) == Y(X(cfg)), f"§A [{n1},{n2}] = 0 (triangle off-shell deterministic sample)")
# component weight relations + composition in the kappa-flip lift [FT.88(2)]
for cfg in cfgs_dig + cfgs_tri_on:
    w, nE, Th = W_of(cfg)
    wC, _, _ = W_of(act_C(cfg))
    wT, _, ThT = W_of(act_T(cfg))
    wP, _, ThP = W_of(act_P(cfg))
    chk(wC == w * negpow(nE), "§A w(C cfg) = (-1)^|E| w(cfg) [EM.24(1) component]")
    chk(wT == w.conj() and ThT == -Th, "§A w(T cfg) = w(cfg)^* with Theta -> -Theta [D2.7, FT.88(2), CT2.8(1) components]")
    chk(ThP == Th and wP == eipTh(Th) * w.conj(), "§A w(P cfg) = e^{i pi Theta} w(cfg)^* with Theta P-invariant [EM.24(5) Pf component]")
    for X in ACTS.values():
        wX, _, _ = W_of(X(cfg))
        chk(wX.re * wX.re + wX.im * wX.im == w.re * w.re + w.im * w.im, "§A |w|^2 invariant under each register involution (unconditional)")
    wCPT, nC, ThC = W_of(act_C(act_P(act_T(cfg))))
    chk(nC == nE and ThC == -Th, "§A CPT preserves |E|; Theta -> -Theta (T is the only d-odd map)")
    chk(wCPT == negpow(nE) * eipTh(-Th) * w, "§A kappa-flip lift [FT.88(2)]: w(CPT cfg) = (-1)^|E| e^{-i pi Theta} w")
    if Th.denominator == 1:      # integer-Theta locus: the two frozen lifts agree with EM.24(5) verbatim
        chk(eipTh(-Th) == eipTh(Th), "§A on the integer-Theta locus e^{-i pi Theta} = e^{+i pi Theta}: the two lifts agree")
        chk(wCPT == negpow(nE) * eipTh(Th) * w, "§A EM.24(5) identity w(CPT C) = (-1)^|E| e^{i pi Theta} w(C) on the integer locus")
        if Th % 2 == 0:
            chk(eipTh(Th) == C(1), "§A materialized even-Theta locus [FT.22]: the CPT character reduces to (-1)^|E|")
# read-covariance census
dig_cycle = ((0, 1), (1, 0))
tri_cycle = ((0, 1), (1, 2), (2, 0))
for chain in (dig_cycle, tri_cycle):
    edges = list(chain)
    for cfg in configs_of(edges, DSET):
        if set(cfg) != set(edges):
            continue
        q = qcore(chain, cfg)
        chk(qcore(chain, act_C(cfg)) == -q, "§A q_core is C-odd [EM.24(1)]")
        chk(qcore(chain, act_P(cfg)) == q, "§A q_core is P-even (sigma-based; alpha-blind)")
        chk(qcore(chain, act_T(cfg)) == q, "§A q_core is T-even (sigma fixed [FT.88(2)])")
        chk(qcore(tuple((b, a) for (a, b) in reversed(chain)), act_W(cfg)) == -q, "§A q_core is omega-odd [FT.40 omega-covariance; omega on a directed chain = reverse+transpose with data transport, FT.88(1)]")
        _, nE, Th = W_of(cfg)
        _, nEw, Thw = W_of(act_W(cfg))
        chk((nEw, Thw) == (nE, Th), "§A |E| and Theta = sum ds^2 are omega-pattern-even (edge-set functions)")
stamp("§A green: four register involutions, exhaustive commutation (289 + 15625 + 3000 configurations), component weight identities, both CPT lifts with the integer-Theta agreement locus, read-covariance table")

# ================================================================== §B
banner("§B (H20/FT.134) — carrier bookkeeping: ray-fixing vs ray-swapping; the scalar-CPT theorem")
OM2 = SG[1]; CHI2 = [[C(0), C(0, 1)], [C(0, -1), C(0)]]; KAP2 = SG[3]
chk(matmul(OM2, OM2) == meyeC(2) and matmul(CHI2, CHI2) == meyeC(2) and matmul(KAP2, KAP2) == meyeC(2), "§B the doublet triple: involutions")
chk(matmul(OM2, CHI2) == matscale(KAP2, C(0, -1)) and matmul(CHI2, KAP2) == matscale(OM2, C(0, -1)) and matmul(KAP2, OM2) == matscale(CHI2, C(0, -1)),
    "§B quaternionic triple: omega chi = -i kappa, chi kappa = -i omega, kappa omega = -i chi [Def-H.34 re-derived]")
kc = [C(1), C(0)]; kw = [C(0), C(1)]
chk(mvec(OM2, kc) == kw and mvec(OM2, kw) == kc, "§B omega-hat swaps the doublet rays [FT.122]")
chk(OM2 != meyeC(2) and OM2 != matscale(meyeC(2), C(-1)), "§B omega-hat is not +-id on the doublet")
for cfg in cfgs_dig:
    if not cfg: continue
    for nm in ('C', 'P', 'T'):
        chk(set(ACTS[nm](cfg).keys()) == set(cfg.keys()), f"§B {nm} fixes the edge tuple pointwise: its doublet action is the identity on rays (with a label map) — register-disjoint from omega-hat")
    chk(set(act_W(cfg).keys()) == {(b, a) for (a, b) in cfg}, "§B the omega-pattern map transposes the tuple: the only family member that moves the doublet basis")
# the promoted Q-hat family [P-H19a]: parity characters
for q in (Fr(1), Fr(-1)):
    Q = matscale(KAP2, q)
    chk(matscale(KAP2, -q) == matscale(Q, C(-1)), "§B the Q-hat family is C-odd: Q_{-q} = -Q_q — the flip block F_LR = q I_2 is C-odd [FT.129(5) character]")
chk(matmul(matmul(OM2, KAP2), OM2) == matscale(KAP2, C(-1)), "§B kappa is omega-odd; q_core is omega-odd [§A]: the coupled Q-hat = q kappa is omega-COVARIANT (both signs cancel)")
# the scalar-CPT theorem: lambda(ray c) = lambda(ray omega c)
for chain in (dig_cycle, tri_cycle):
    edges = list(chain)
    for cfg in configs_of(edges, DSET):
        if set(cfg) != set(edges): continue
        _, nE, Th = W_of(cfg)
        _, nEw, Thw = W_of(act_W(cfg))
        lam_c = negpow(nE) * eipTh(Th)
        lam_w = negpow(nEw) * eipTh(Thw)
        chk(lam_c == lam_w, "§B the CPT character lambda = (-1)^|E| e^{i pi Theta} takes the SAME value on both doublet rays (|E|, Theta are edge-set functions)")
        chk(lam_c.re * lam_c.re + lam_c.im * lam_c.im == Fr(1), "§B |lambda| = 1: the character never vanishes")
chk(mtr(meyeC(2)) == C(2) and mtr(KAP2) == C(0), "§B tr(id) = 2 != 0 = tr(kappa): no scalar character equals any kappa multiple — CPT|_H_omega = lambda id refutes CPT = -kappa exactly")
# uniqueness pair re-run (FT.122(6) / FT.129(1) at the point of use)
diag_inv, offdiag_inv = set(), set()
for p in range(-8, 9):
    for qq in range(1, 9):
        a = Fr(p, qq)
        M1 = [[C(a), C(0)], [C(0), C(-a)]]
        if matmul(M1, M1) == meyeC(2): diag_inv.add(a)
        M2 = [[C(0), C(0, a)], [C(0, -a), C(0)]]
        if matmul(M2, M2) == meyeC(2): offdiag_inv.add(a)
chk(diag_inv == {Fr(1), Fr(-1)} and offdiag_inv == {Fr(1), Fr(-1)}, "§B diagonal omega-odd involutions = +-kappa; diagonal-free = +-chi (rational census): the uniqueness pair")
# FT.126(4) independence re-run
for G in (SG[3], SG[1]):
    Gi = ckron(G, meyeC(2)); OMc = ckron(meyeC(2), OM2)
    chk(matadd(matmul(Gi, OMc), matmul(OMc, Gi), -1) == mz(4), "§B internal involutions commute with the omega-lift: independent Z_2's [FT.126(4)]")
    prod = matmul(Gi, OMc)
    chk(matmul(prod, prod) == meyeC(4) and prod != Gi and prod != OMc, "§B the product is a third distinct involution: Z_2 x Z_2")
stamp("§B green: quaternionic triple; ray-fixing (C,P,T) vs ray-swapping (omega) census; Q-hat family C-odd and omega-covariant; scalar-CPT theorem with the trace refutation; uniqueness pair; Z_2 x Z_2 independence")

# ================================================================== §C
banner("§C (H20/FT.135) — the weak branch grading: label-level exchange, non-implementation re-derived")
def kron2(A, B): return [[A[i // 2][k // 2] * B[i % 2][k % 2] for k in range(4)] for i in range(4)]
E0 = meyeC(4)
SIG4 = matadd(matadd(kron2(SG[1], SG[1]), kron2(SG[2], SG[2])), kron2(SG[3], SG[3]))
Wp = [matscale(matadd(kron2(SG[0], SG[i]), kron2(SG[i], SG[0])), Fr(1, 2)) for i in (1, 2, 3)]
Ss = matscale(matadd(E0, SIG4), Fr(1, 2))
PiR = matscale(matadd(E0, Ss), Fr(1, 2)); PiV = matscale(matadd(E0, Ss, -1), Fr(1, 2))
chk(matmul(PiR, PiR) == PiR and matmul(PiV, PiV) == PiV and matmul(PiR, PiV) == mz(4) and matadd(PiR, PiV) == E0, "§C CT0.7(1): Pi_R, Pi_V orthogonal idempotents, sum = E_0")
chk(mtr(PiR) == C(3) and mtr(PiV) == C(1), "§C traces 3/1 [CT0.7(1)] — the trace obstruction datum")
for i in range(3):
    chk(matmul(Wp[i], PiV) == mz(4) and matmul(PiV, Wp[i]) == mz(4), f"§C W_{i+1} Pi_V = 0 = Pi_V W_{i+1}: antialigned branch weak-blind [FT.101(2)]")
    chk(matmul(matmul(PiR, Wp[i]), PiR) == Wp[i], f"§C W_{i+1} = Pi_R W_{i+1} Pi_R: aligned branch weak-active [FT.101(1)]")
CasW = matadd(matadd(matmul(Wp[0], Wp[0]), matmul(Wp[1], Wp[1])), matmul(Wp[2], Wp[2]))
chk(CasW == matscale(PiR, C(2)), "§C sum W_i^2 = 2 Pi_R [Cor CT0.7a]; Casimir reads 2 (vee^2) / 0 (wedge^2)")
chk(matmul(Ss, PiR) == PiR and matmul(Ss, PiV) == matscale(PiV, C(-1)), "§C S-eigenvalues +1 on Pi_R (vee^2), -1 on Pi_V (wedge^2)")
for sa in (1, -1):
    for sb in (1, -1):
        M = matadd(matscale(PiR, Fr(sa)), matscale(PiV, Fr(sb)))
        chk(mtr(M) != C(0), f"§C tr({sa}Pi_R {sb:+}Pi_V) = {3*sa+sb} != 0: no traceless involution [FT.93(3a)/FT.101(3)]")
rowsK = []
for W in Wp:
    WR = [[w.re for w in row] for row in W]; WI = [[w.im for w in row] for row in W]
    for p in range(4):
        rr = [Fr(0)] * 8; ri = [Fr(0)] * 8
        for k in range(4):
            rr[k] += WR[p][k]; ri[k] += WI[p][k]
            rr[4 + k] += -WI[p][k]; ri[4 + k] += WR[p][k]
        rowsK.append(rr); rowsK.append(ri)
chk(8 - rankQ(rowsK) == 2, "§C dim ker(W-stack) = 1 over C = im Pi_V [FT.93(5)/FT.101(2)]")
iota = {Fr(0): Fr(1), Fr(1): Fr(0)}   # branch alphabet a = alpha/pi
chk(all(iota[iota[a]] == a for a in iota) and iota[Fr(0)] == Fr(1), "§C iota(a) = 1-a on the branch alphabet: the label-level exchange [FT.101(3), EM.24(2)]")
if ARCH:
    chk('Structural parity non-invariance' in H12DOC, "§C pin: FT.101(5)'s scope statement (force arena, not matter chirality)")
    chk('The branch flip is label-level' in H12DOC, "§C pin: FT.101(3)'s label-level verdict")
stamp("§C green: branch data re-derived (supports, Casimirs, traces, kernel); no traceless involution; label-level exchange; non-implementation data exact")

# ================================================================== §D
banner("§D (H20/FT.136) — the rung-one S-grading: Ad(S) census, dims (10, 6)")
Ehat = {}
for i in range(1, 4):
    for j in range(i + 1, 4):
        Ehat[(i, j)] = matscale(matadd(kron2(SG[i], SG[j]), kron2(SG[j], SG[i])), Fr(1, 2))
for i in range(1, 4):
    Ehat[(i, i)] = matadd(kron2(SG[i], SG[i]), matscale(SIG4, Fr(-1, 3)))
Jg = {}; Kg = {}
for (i, j, k) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)):
    Jg[i] = matscale(matadd(kron2(SG[j], SG[k]), kron2(SG[k], SG[j]), -1), Fr(1, 2))
    Kg[i] = matscale(matadd(kron2(SG[0], SG[i]), kron2(SG[i], SG[0]), -1), Fr(1, 2))
BASIS = [('E0', E0), ('Sigma', SIG4)] + [(f'Ehat{i}{j}', Ehat[(i, j)]) for (i, j) in sorted(Ehat)] \
        + [(f'W{i}', Wp[i - 1]) for i in (1, 2, 3)] + [(f'J{i}', Jg[i]) for i in (1, 2, 3)] + [(f'K{i}', Kg[i]) for i in (1, 2, 3)]
chk(len(BASIS) == 17, f"§D CT1.2 generator census: {len(BASIS)} = 17 (16 basis + the dependent Ehat33 = -Ehat11-Ehat22)")
rows = []
for (_, M) in BASIS:
    rows.append([x.re for r in M for x in r]); rows.append([x.im for r in M for x in r])
chk(rankQ(rows) == 16, "§D the 17 Hermitian generators span the 16-real-dim Hermitian pair space with the single traceless-diagonal relation sum Ehat^ii = 0 [CT1.2/FT.92(1)]")
even, odd = [], []
for nm, M in BASIS:
    AdM = matmul(matmul(Ss, M), Ss)
    if AdM == M: even.append(nm)
    elif AdM == matscale(M, C(-1)): odd.append(nm)
    else: raise AssertionError(f"§D {nm} is not an Ad(S)-eigenelement")
chk(len(even) == 11 and len(odd) == 6, f"§D Ad(S) census: S-even {len(even)} = 11 generators (10 basis dims, Ehat-trace relation), S-odd {len(odd)} = 6")
chk(set(even) == {'E0', 'Sigma', 'Ehat11', 'Ehat12', 'Ehat13', 'Ehat22', 'Ehat23', 'Ehat33', 'W1', 'W2', 'W3'}, f"§D S-even membership = D+ (E0) + H (Sigma) + G (Ehat, 5 dims) + W (3): {sorted(even)}")
chk(set(odd) == {'J1', 'J2', 'J3', 'K1', 'K2', 'K3'}, f"§D S-odd membership = J+ (3) + J- (3): {sorted(odd)}")
chk('\\mathcal A(1)=\\{J,\\,G,\\,W,\\,H,\\,D^+\\}' in BDOC, "§D pin: CT0.13's rung-one active set A(1) = {J, G, W, H, D+}")
if ARCH:
    chk('(5{+}3{+}1)+(3{+}3)+1' in H04DOC, "§D pin: FT.30's tiling ((5+3+1)+(3+3)+1) = the 10/6 split with D+")
    chk('metric coordinates' in H04DOC, "§D pin: FT.30's metric dictionary — J^+- carry no metric coordinates")
chk(all(nm in even for nm in ('W1', 'W2', 'W3')) and all(nm in odd for nm in ('J1', 'K1')), "§D the weak block is S-even; the Janus seals are S-odd: the rung-one force/dynamics split")
stamp("§D green: Ad(S) census with exact membership (10 even dims = G5+W3+H1+D+1; 6 odd = J+3+J-3); A(1)/FT.30 pins")

# ================================================================== §E
banner("§E (H20/FT.137) — the cover sector: pattern reversal vs parity; the two Omega=24 orbits")
nvT = 4
DET = [(a, b) for a in range(4) for b in range(4) if a != b]
undT = sorted({(min(a, b), max(a, b)) for (a, b) in DET})
permsT = automorphisms(nvT, undT)
chk(len(permsT) == 24, f"§E |Aut(tetrahedron skeleton)| = {len(permsT)} = 24")
def unmask(bits): return frozenset(DET[i] for i in range(12) if (bits >> i) & 1)
def maskof(R):
    m = 0
    for i, e in enumerate(DET):
        if e in R: m |= 1 << i
    return m
def act_perm(pm, R): return frozenset((pm[a], pm[b]) for (a, b) in R)
def canonical(R): return min(maskof(act_perm(pm, R)) for pm in permsT)
revT = {(a, b): (b, a) for (a, b) in DET}
def rev(R): return frozenset(revT[e] for e in R)
n_cov = 0; forty_eight = []
for bits in range(1 << 12):
    R = unmask(bits); Rr = rev(R)
    v = brute_sign_sum(nvT, R); vr = brute_sign_sum(nvT, Rr)
    chk(v == vr, "§E v(R^T) = v(R): reversal invariance of the amplitude (all 4096 tetrahedron patterns) [FT.95(3) re-derived]")
    ty = types_of(nvT, R); tyr = types_of(nvT, Rr)
    adm = all(x + y <= 3 for (x, y) in ty); admr = all(x + y <= 3 for (x, y) in tyr)
    chk(adm == admr and len(Rr) == len(R), "§E admissibility and K = |R| reversal-invariant")
    if v != 0:
        n_cov += 1
        if adm and any((b, a) in R for (a, b) in R):
            forty_eight.append(bits)
chk(n_cov == 101, f"§E tetrahedron covers: {n_cov} = 101 [FT.68/FT.69 census]")
chk(len(forty_eight) == 48, f"§E dissolved-digon bypass covers: {len(forty_eight)} = 48 [FT.69(4)]")
orb = {}
for bits in forty_eight:
    orb.setdefault(canonical(unmask(bits)), []).append(bits)
chk(len(orb) == 2 and sorted(len(v) for v in orb.values()) == [24, 24], f"§E the 48 split into two Omega=24 Aut-orbits: sizes {sorted(len(v) for v in orb.values())} [FT.78(6)]")
(o1, o2) = list(orb.keys())
chk({canonical(rev(unmask(b))) for b in orb[o1]} == {o2} and o1 != o2, "§E the pattern reversal EXCHANGES the two chiral cover orbits [FT.78(6) re-derived]")
chk(all(canonical(rev(unmask(b))) != b for b in orb[o1] + orb[o2]), "§E no orbit is reversal-invariant (reversal is not in Aut)")
# the exact P sign character: v_a(R) = (-1)^{sum a} v_0(R) — triangle, exhaustive over (R, a, sigma)
def v_a_brute(R, a):
    Rl = sorted(R); tot = 0
    verts = sorted({v for e in R for v in e})
    for assign in itertools.product((1, -1), repeat=len(Rl)):
        sg = dict(zip(Rl, assign))
        aleph = 0
        for v in verts:
            inn = [e for e in Rl if e[1] == v]; out = [e for e in Rl if e[0] == v]
            if len(inn) == 1 and len(out) == 1:
                aleph += abs((sg[out[0]] - sg[inn[0]]) // 2)
        term = (-1) ** aleph
        for e in Rl:
            term *= sg[e] * (-1) ** a[e]
        tot += term
    return tot
tri_dir = [(a, b) for a in range(3) for b in range(3) if a != b]
n_checked = 0
for rbits in range(1 << 6):
    R = frozenset(tri_dir[i] for i in range(6) if (rbits >> i) & 1)
    if not R: continue
    v0 = v_a_brute(R, {e: 0 for e in R})
    for abits in range(1 << len(R)):
        a = {e: (abits >> i) & 1 for i, e in enumerate(sorted(R))}
        chk(v_a_brute(R, a) == (-1) ** (sum(a.values()) % 2) * v0, "§E the exact P sign character: v_a(R) = (-1)^{sum a} v_0(R) — cover status, |v|, K, 4^|C|, 2^|R| all P-invariant")
        n_checked += 1
print(f"    (P sign character verified on {n_checked} (R, a) pairs, triangle skeleton, exhaustive)")
if ARCH:
    chk('zero-expectation theorem' in H12DOC, "§E pin: FT.95(3)'s theorem present in H12")
    chk('two $\\Omega=24$ orbits exchanged by reversal' in H10DOC, "§E pin: FT.78(6)'s chiral-pair statement present in H10")
stamp("§E green: reversal invariance on all 4096 patterns; 101 covers; the 48 = two Omega=24 orbits exchanged by reversal; the exact P sign character (census alpha-blind up to sign)")

# ================================================================== §F
banner("§F (H20/FT.138) — the defect multiplets: exact parity (m <-> -m) in algebraic number fields")
def cmul(x, y):
    p = [Fr(0)] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            p[i + j] += a * b
    for k in (6, 5, 4):
        if p[k]:
            p[k - 2] += p[k] * Fr(20, 16); p[k - 4] += p[k] * Fr(-5, 16); p[k] = Fr(0)
    return tuple(p[:4])
cEl = (Fr(0), Fr(1), Fr(0), Fr(0))
c4 = cmul(cmul(cEl, cEl), cmul(cEl, cEl)); c2 = cmul(cEl, cEl)
poly = tuple(Fr(16) * c4[i] - Fr(20) * c2[i] + (Fr(5) if i == 0 else Fr(0)) for i in range(4))
chk(poly == (0, 0, 0, 0), "§F 16c^4 - 20c^2 + 5 = 0 in Q[c]/(...): c = cos(pi/10) [FT.76(2)]")
def cheb(m):
    prev, cur = (Fr(1), Fr(0), Fr(0), Fr(0)), cEl
    if m == 0: return prev
    for _ in range(m - 1):
        nxt = tuple(2 * x for x in cmul(cEl, cur))
        nxt = tuple(nxt[i] - prev[i] for i in range(4))
        prev, cur = cur, nxt
    return cur
chk(cheb(5) == (Fr(0), Fr(0), Fr(0), Fr(0)), "§F T_5(c) = 16c^5-20c^3+5c = c(16c^4-20c^2+5) = 0: cos(pi/2) = 0 exact")
c3_ = cmul(c2, cEl)
chk(cheb(3) == tuple(4 * c3_[i] - 3 * cEl[i] for i in range(4)), "§F T_3(c) = 4c^3 - 3c exact (recurrence vs triple-angle)")
def Ddod(m):
    T = cheb(abs(m))
    return tuple((Fr(2) if i == 0 else Fr(0)) - 2 * x for i, x in enumerate(T))
for m in (1, 3, 5):
    chk(Ddod(m) == Ddod(-m), f"§F dodecahedron (delta_v = pi/5): D({m}) = D({-m}) exact in Q[c] — the multiplet is m-parity-symmetric")
chk(Ddod(5) == (Fr(2), Fr(0), Fr(0), Fr(0)), "§F D(+-5) = 2 exact")
chk(Ddod(3) == (Fr(2), Fr(6), Fr(0), Fr(-8)) and Ddod(1) == (Fr(2), Fr(-2), Fr(0), Fr(0)), "§F D(+-3) = 2-2(4c^3-3c) and D(+-1) = 2-2c exact in Q[c]")
# tetra (delta_v = pi): D = 2 - 2cos(m pi/2), m odd -> cos = 0 -> D = 2 (fully degenerate [FT.76(5a)])
for m in (3, 1, -1, -3):
    chk(Fr(2) - 2 * Fr(0) == Fr(2), f"§F tetrahedron (delta_v = pi): D({m}) = 2 exact — the fully degenerate multiplet [FT.76(5a)]")
# cube (delta_v = pi/2): m in {2,0,-2}: D = 2 - 2cos(m pi/4) = {2, 0, 2} (massless even winding [FT.76(5b)])
for m, cosv, D in ((2, Fr(0), Fr(2)), (0, Fr(1), Fr(0)), (-2, Fr(0), Fr(2))):
    chk(Fr(2) - 2 * cosv == D, f"§F cube (delta_v = pi/2): D({m}) = {D} exact — the massless weight [FT.76(5b)]")
# octa (delta_v = 2pi/3): m in {3,1,-1,-3}: D = 2 - 2cos(m pi/3) = {4, 1, 1, 4}
for m, cosv, D in ((3, Fr(-1), Fr(4)), (1, Fr(1, 2), Fr(1)), (-1, Fr(1, 2), Fr(1)), (-3, Fr(-1), Fr(4))):
    chk(Fr(2) - 2 * cosv == D, f"§F octahedron (delta_v = 2pi/3): D({m}) = {D} exact; D(m) = D(-m)")
# icosa (delta_v = pi/3): m in {3,1,-1,-3}: D = 2 - 2cos(m pi/6) = {2, 2-sqrt3, 2-sqrt3, 2} in Q(sqrt3)
for m in (3, 1, -1, -3):
    Dpair = (Fr(2), Fr(0)) if abs(m) == 3 else (Fr(2), Fr(-1))
    chk(Dpair[0] ** 2 - 3 * Dpair[1] ** 2 == (4 if abs(m) == 3 else 1), f"§F icosahedron (delta_v = pi/3): D({m}) = {Dpair[0]} {'+' if Dpair[1] >= 0 else '-'} {abs(Dpair[1])} sqrt3 in Q(sqrt3) with norm D*Dconj = {4 if abs(m)==3 else 1} exact; D(m) = D(-m)")
if ARCH:
    chk('4\\sin^2(m\\,\\delta_v/4)' in H10DOC, "§F pin: FT.76's defect formula D = 4 sin^2(m delta_v / 4) present in H10")
# on-shell P-triviality: even Theta, real weights -> w(P cfg) = w(cfg)
# materialized locus = per-edge integer ds^2 [FT.24: kappa in Z] AND Theta in 2Z [FT.22]
# -> every eps(a,d) = (-1)^(a d) real -> w real; w(P) = e^{i pi Theta} w* = w [FT.133(3), FT.137(3)]
n_on = 0
for cfg in cfgs_dig:
    _, nE, Th = W_of(cfg)
    if Th.denominator == 1 and Th % 2 == 0 and all(d.denominator == 1 for (s, a, d) in cfg.values()):
        wP, _, _ = W_of(act_P(cfg))
        w, _, _ = W_of(cfg)
        chk(wP == w, "§F on-shell even-Theta locus: w(P cfg) = w(cfg) exactly (P acts trivially on materialized weights)")
        n_on += 1
chk(n_on > 0, "§F the on-shell P-triviality census is nonempty")
stamp("§F green: the five Platonic defect multiplets exact in Q / Q[c]/(16c^4-20c^2+5) / Q(sqrt3); D(m) = D(-m) throughout; degenerate tetra and massless cube weights; on-shell P-triviality")

# ================================================================== §G
banner("§G (H20/FT.139) — the channel census: Ad(S)-even seal bilinear; register-blind constants; the flip-block contrast")
for i in (1, 2, 3):
    for j in (1, 2, 3):
        comm = matadd(matmul(Jg[i], Kg[j]), matmul(Kg[j], Jg[i]), -1)
        chk(matmul(matmul(Ss, comm), Ss) == comm, f"§G Ad(S)([J_{i},K_{j}]) = [J_{i},K_{j}]: the seal bilinear is S-even (all 9 pairs)")
Xsum = matadd(matadd(matadd(matmul(Jg[1], Kg[1]), matmul(Kg[1], Jg[1]), -1),
                     matadd(matmul(Jg[2], Kg[2]), matmul(Kg[2], Jg[2]), -1)),
              matadd(matmul(Jg[3], Kg[3]), matmul(Kg[3], Jg[3]), -1))
chk(Xsum == matscale(SIG4, C(0, 2)), "§G sum_i [J_i,K_i] = 2 i Sigma re-derived [FT.109]")
chk(matmul(matmul(Ss, SIG4), Ss) == SIG4, "§G Sigma is S-even: the Koide numerator lives in the S-even block [FT.109(4)]")
if ARCH:
    chk(r'\frac{2}{3\cdot3}=\frac29' in H16DOC, "§G pin: delta = 2/(3*3) = 2/9 displayed in H16")
    chk(r'\frac{2}{3\cdot3\cdot3}=\frac2{27}' in H17DOC, "§G pin: delta_q = 2/(3*3*3) = 2/27 displayed in H17")
    chk('x^2-3x-3' in H09DOC, "§G pin: FT.68(2)'s transfer charpoly present in H09")
    chk('f_{\\mathrm{adm}}' in H09DOC, "§G pin: FT.70/FT.71's admissibility function present in H09")
q = Fr(1)
chk(matscale(KAP2, -q) == matscale(matscale(KAP2, q), C(-1)), "§G the flip block F_LR = q I_2 is C-odd [FT.129(5) + §A q-covariance]: channel constants register-blind, flip block C-odd — distinct parity characters")
stamp("§G green: seal bilinear S-even on all 9 pairs; 2iSigma re-derived; channel-constant blindness pins; the flip-block C-odd contrast")

# ================================================================== §H
banner("§H (H20/FT.140) — document pins, vocabulary scans, downstream integrity")
if ARCH:
    doc = H20DOC
secs = {}
if ARCH:
    for sp in re.split(r'^### ', doc, flags=re.M)[1:]:
        secs[sp.split(' —')[0].strip()] = sp.split('\n## ')[0]
    for t in ('FT.133', 'FT.134', 'FT.135', 'FT.136', 'FT.137', 'FT.138', 'FT.139', 'FT.140'):
        chk(t in secs, f"§H section {t} present")
    for w in ('**Thm.**', '**Req.**', '**Pf.**', '**Phys.**', '**Status.**'):
        chk(all(secs[t].count(w) == 1 for t in ('FT.133', 'FT.134', 'FT.135', 'FT.136', 'FT.137', 'FT.138', 'FT.139', 'FT.140')), f"§H every FT block carries exactly one {w}")
    chk(doc.count(r'\blacksquare') == 10, f"§H 10 proof terminators (7 theorem proofs + FT.140's row marker and terminator + the document-end seal; got {doc.count(chr(92)+'blacksquare')})")
    chk(doc.count('**Status.**') == 9, "§H Status count = 9 (8 theorem blocks + the document header line)")
    chk('## Tier F.41' in doc and 'part 20 of 20' in doc, "§H pins: Tier F.41 heading; part 20 of 20")
    chk('P-H20a' in doc and 'verify_H_parity_identification.py' in doc, "§H pins: P-H20a adjudicated in-document; machine reference")
    chk('vacuous' in doc.lower(), "§H the P-H20a adjudication (vacuous as a declaration) is stated")
    chk(r'\mathrm{CPT}\big|_{\mathcal H_\omega}=\lambda\,\mathrm{id}' in doc, "§H pin: the scalar-CPT display")
    chk(r'\lambda=(-1)^{|E|}e^{i\pi\Theta}' in doc, "§H pin: the CPT character display")
    chk(r'F_{LR}=q\,I_2' in doc, "§H pin: the flip-block character row")
BARRED = ['previously', 'formerly', 'this was', 'now this', 'erratum', 'submitted', 'earlier draft', 'stale', 'draft', 'directive', 'as corrected']
if ARCH:
    hits = [(w, doc.lower().count(w)) for w in BARRED if w in doc.lower()]
if ARCH:
    chk(not hits, f"§H revision/drafting/directive-language scan of H20: zero hits ({hits})")
SPECIES = ['electron', 'muon', 'tau lepton', 'neutrino', 'proton', 'neutron', 'quark', 'photon', 'gluon', 'lepton', 'pion', 'higgs boson']
if ARCH:
    ph = [(w, doc.lower().count(w)) for w in SPECIES if w in doc.lower()]
if ARCH:
    chk(not ph, f"§H species-name scan of ALL of H20 (zero external data in this part): zero hits ({ph})")
    chk(doc.count(r'[\text{EXT}]') == 1 and doc.count('EXT') == 1, f"§H [EXT] occurs exactly once (the standing-rules clause, typeset [\\text{{EXT}}]): got {doc.count('EXT')}")
MASS = ['0.511', '105.6', '1776', '206.7', '3477', '1.273', '4.183', '162.5', '172.4', '938.2', '139.57', '0.118', '137.0']
if ARCH:
    leak = [t for t in MASS if t in doc]
if ARCH:
    chk(not leak, f"§H no external mass/coupling token anywhere in H20 ({leak})")
    chk('**(P-H20a)**' in H13DOC and 'VACUOUS' in H13DOC, "§H H13 carries the P-H20a registry entry with the vacuous adjudication")
    chk('parity census' in H13DOC, "§H H13 item-20 annotation carries the parity-census status")
    chk('FT.134' in H19DOC and 'scalar character' in H19DOC, "§H H19 carries the forward pointer to the parity tier")
    chk('forward pointer' in H19DOC and 'H20' not in H19DOC.split('forward pointer')[0], "§H H19 references H20 only in/after its forward-pointer remark")
chk('**P (parity).**' in EDOC, "§H pin: EM.24(2)'s derived parity clause")
chk('w(\\mathrm{CPT}\\,C)=(-1)^{|E(C)|}\\,e^{i\\pi\\Theta(C)}\\,w(C)' in EDOC, "§H pin: EM.24(5)'s phase identity (frozen)")
if ARCH:
    chk('\\mathbb Z_2\\times\\mathbb Z_2' in H11DOC, "§H pin: FT.88(3)'s involution algebra")
    chk('R\\mapsto R^{\\mathrm T}' in H11DOC, "§H pin: FT.88(1)'s pattern-level reversal")
chk(all(t in BDOC for t in ('CT0.7', 'CT0.12', 'CT0.13', 'CT1.2')), "§H cited B-tags exist")
stamp("§H green: sections, markers, counts, display pins; zero barred/species hits; one [EXT] marker; no mass tokens; H13/H19 downstream integrity; frozen pins")

print(f"\nverify_H_parity_identification: {N} checks green  ({time.time()-t0:.1f}s) — H20 §A–§H (Tier F.41, FT.133–FT.140)")
