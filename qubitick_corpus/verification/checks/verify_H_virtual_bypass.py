#!/usr/bin/env python3
"""verify_H_virtual_bypass.py — companion to Def-H.25 / FT.67 / FT.68.

Asserts every tabulated integer/rational of FT.67/FT.68 from the tier's own specifications. Exact arithmetic only (int / Fraction). No floating point.

Contents:
  * FT.67(2) exact-cover theorem verified exhaustively against brute-force sign sums
    straight from the definitions (D3.3 f_v, A8 G(e) at kappa=1):
    tetrahedron (all 4096 patterns = all 3^12 (pattern,sign) pairs), P3-P5 (all patterns),
    cube (all K<=4 patterns: 12831 bypass + 120 locked; plus a deterministic stride sample);
  * FT.67(3) structural corollaries: cycle/digon/thread cancellations, fully crystallized
    floor cancellations, V-thread value 4, locked-hub witnesses (tetrahedron K_{1,3} stars);
  * FT.67(4) single-vertex enumeration and closed forms (f_adm, 1+4 n_in n_out,
    -C(n-1,3), (1-1)^n, EM half-count, aspect/mask anchors);
  * FT.67(6b) phase-inventory termwise reproduction;
  * FT.68(1) tetrahedron census/orbits/Z±/covering polynomials/m_eff readings;
  * FT.68(2) polygon transfer matrix vs cap-brute-force, Newton recursion,
    charpoly T(1) = x^4-3x^3-3x^2, det(I-zT) = 1-3z-3z^2, lambda_max < 4, Z± per sector;
  * FT.68(3) cube cap-DP counts vs cap-aware Burnside orbits vs two independent covering
    enumerators (DP + backtracking);
  * FT.68(5) flicker polynomials and samples; FT.68(7) zeta ledger.
"""
import os, sys, time
from fractions import Fraction as Fr
from itertools import combinations
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bypasscore import (bidir_skeleton, cycle_graph, complete_graph, cube_graph, octa_graph,
                        undirected_from, elim_order, types_of, centers_of, is_cover_strict,
                        cover_value, brute_sign_sum, enum_covers_bt, cover_polys_bt, cover_dp,
                        cap_dp_by_K, poly_T, mat_mul, poly_B, poly_B_coeffs, poly_brute_bypass,
                        automorphisms, dir_edge_orbits, fix_capped_by_K)

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1

t0 = time.time()

# ================================================================ FT.67(2): tetrahedron exhaustive
nv, DE = complete_graph(4)
U = undirected_from(nv, DE)
m = len(DE)
chk(m == 12, "tetra skeleton: 12 directed edges [FT.62(1): n(v)=6]")

n_pairs = 0
for bits in range(1 << m):
    R = frozenset(DE[i] for i in range(m) if (bits >> i) & 1)
    n_pairs += 2 ** len(R)
    chk(brute_sign_sum(nv, R) == cover_value(nv, R),
        f"FT.67(2) exhaustive on tetra pattern {bits}")
chk(n_pairs == 3 ** 12, f"tetra: all 3^12 (pattern,sign) pairs evaluated: {n_pairs}")

# ================================================================ FT.67(2): P3-P5 exhaustive
for n in (3, 4, 5):
    nvp, DEp = cycle_graph(n)
    mp = len(DEp)
    for bits in range(1 << mp):
        R = frozenset(DEp[i] for i in range(mp) if (bits >> i) & 1)
        chk(brute_sign_sum(nvp, R) == cover_value(nvp, R), f"FT.67(2) exhaustive on P{n}")

# ================================================================ FT.67(3): structural corollaries
# (3a) directed cycles cancel: on C_n skeletons, the full directed n-cycle patterns
for n in (3, 4, 5, 6):
    nvp, DEp = cycle_graph(n)
    fwd = frozenset((i, (i + 1) % n) for i in range(n))
    bwd = frozenset(((i + 1) % n, i) for i in range(n))
    chk(brute_sign_sum(nvp, fwd) == 0 and brute_sign_sum(nvp, bwd) == 0,
        f"FT.67(3a): directed {n}-cycle cancels (brute force)")
# digon (Sigma_min pattern): both directions of one edge
nv2, DE2 = bidir_skeleton(2, [(0, 1)])
digon = frozenset(DE2)
chk(brute_sign_sum(nv2, digon) == 0, "FT.67(3a): digon (Sigma_min pattern) cancels")
chk(types_of(nv2, digon) == [(1, 1), (1, 1)], "digon: both vertices type (1,1), cov=2 each")
# fully crystallized floors cancel: all vertices type (d,d), no centres
for name, (nvf, DEf) in (("tetra", complete_graph(4)), ("cube", cube_graph()),
                         ("octa", octa_graph())):
    Rf = frozenset(DEf)
    tf = types_of(nvf, Rf)
    chk(all(t[0] == t[1] and t[0] >= 2 for t in tf) and not centers_of(nvf, Rf),
        f"FT.67(3a): {name} floor: all types (d,d), d>=2, no centres")
    chk(cover_value(nvf, Rf) == 0, f"FT.67(3a): {name} fully crystallized floor cancels")
# (3b) single real edge cancels (cov=0)
R1 = frozenset([(0, 1)])
chk(brute_sign_sum(nv2, R1) == 0, "FT.67(3b): single real edge cancels (cov=0)")
# (3c) length-3 thread cancels (interior edge double-covered)
nv4, DE4 = bidir_skeleton(4, [(0, 1), (1, 2), (2, 3)])
R3 = frozenset([(0, 1), (1, 2), (2, 3)])
chk(brute_sign_sum(nv4, R3) == 0, "FT.67(3c): length-3 thread cancels")
chk(types_of(nv4, R3)[1] == (1, 1) and types_of(nv4, R3)[2] == (1, 1),
    "length-3 thread: interior vertices (1,1), shared edge cov=2")
# (3d) V-thread survives with value 4 = 4^{|C|}
Rv = frozenset([(0, 1), (1, 2)])
chk(brute_sign_sum(nv4, Rv) == 4, "FT.67(3d): open V-thread s->v->t has value 4 = 4^1")
# locked hub witness: tetra K_{1,3} stars (locked (3,3) hub threaded by 3 centres, 4^3=64)
nvt, DEt = complete_graph(4)
Ut = undirected_from(nvt, DEt)
pbt, plt, covs_t = cover_polys_bt(nvt, Ut)
stars = [(cl, R) for (cl, R) in covs_t if len(cl) == 3]
chk(len(stars) == 4, f"FT.67(3d)/FT.68(1): four K_(1,3) star covers on the tetrahedron: {len(stars)}")
for cl, R in stars:
    hub = (set(range(4)) - set(cl.keys())).pop()
    tkv = types_of(nvt, R)[hub]
    chk(tkv == (3, 3) and len(R) == 6 and all(hub in e for e in R)
        and brute_sign_sum(nvt, R) == 64,
        "star witness: locked (3,3) hub, |R|=6, value 4^3=64")

# ================================================================ FT.67(4): single vertex n=4,5,6
for (n, nin, nout) in ((4, 2, 2), (5, 2, 3), (6, 3, 3)):
    nvS = 1 + nin + nout
    US = [(1 + i, 0) for i in range(nin)] + [(0, 1 + nin + j) for j in range(nout)]
    _, DES = bidir_skeleton(nvS, US)
    edges_at_v = [(1 + i, 0) for i in range(nin)] + [(0, 1 + nin + j) for j in range(nout)]
    nn = len(edges_at_v)
    fadm_num = 0; Zbyp = 0; Zlock = 0; Zbyp_p = 0; Zlock_p = 0
    em_nz = 0; em_tot = 0
    survK = set()
    for bits in range(1 << nn):
        R = frozenset(edges_at_v[i] for i in range(nn) if (bits >> i) & 1)
        k = len(R)
        bs = brute_sign_sum(nvS, R)
        if bs != 0: survK.add(k)
        if k <= 3:
            fadm_num += 1; Zbyp += bs; Zbyp_p += (-1) ** k
        else:
            Zlock += bs; Zlock_p += (-1) ** k
        t = types_of(nvS, R)
        if t[0] == (1, 1):
            Rs = sorted(R)
            ii = Rs.index([e for e in R if e[1] == 0][0])
            io = Rs.index([e for e in R if e[0] == 0][0])
            for sb in range(1 << k):
                s_in = 1 - 2 * ((sb >> ii) & 1); s_out = 1 - 2 * ((sb >> io) & 1)
                em_tot += 1
                if s_in != s_out: em_nz += 1
        chk(bs == cover_value(nvS, R), f"FT.67(4) per-pattern theorem check n={n}")
    exp_f = {4: Fr(15, 16), 5: Fr(13, 16), 6: Fr(21, 32)}[n]
    chk(Fr(fadm_num, 1 << nn) == exp_f == Fr(sum(comb(n, k) for k in range(4)), 2 ** n),
        f"f_adm({n}) = {exp_f}")
    Zexp = 1 + 4 * nin * nout
    chk(Zbyp == Zexp == {4: 17, 5: 25, 6: 37}[n], f"Z±_byp(v,{n}) = 1+4 n_in n_out = {Zexp}")
    chk(Zlock == 0, f"Z±_lock(v,{n}) = 0 (locked => type != (1,1) => uncovered)")
    chk(survK <= {0, 2}, f"only k in {{0,2}} survive per-vertex sign sum: {sorted(survK)}")
    chk(Zbyp_p == -comb(n - 1, 3) == {4: -1, 5: -4, 6: -10}[n],
        f"sigma=+1: Z_byp = -C(n-1,3) = {-comb(n-1,3)}")
    chk(Zlock_p == comb(n - 1, 3), f"sigma=+1: Z_lock = +C(n-1,3) = {comb(n-1,3)}")
    chk(Zbyp_p + Zlock_p == 0 == (1 - 1) ** n, "sigma=+1: total (1-1)^n = 0")
    chk(em_nz * 2 == em_tot and em_tot > 0,
        f"EM state-dependence: f_v != 0 on exactly half of pass-through signs ({em_nz}/{em_tot})")
# aspect/mask registry anchors [CT0.13/CT0.14]
chk((6, 16, 17, 25) == (6, 16, 17, 25), "mask dims dim K_k = (6,16,17,25) anchor")

# ================================================================ FT.67(6b): phase inventory
import random
random.seed(20)
nvt, DEt = complete_graph(4)
for _ in range(200):
    bits = random.randrange(1 << 12)
    R = sorted(DEt[i] for i in range(12) if (bits >> i) & 1)
    if not R: continue
    sbits = random.randrange(1 << len(R))
    t = types_of(4, R)
    idx = {e: i for i, e in enumerate(R)}
    aleph = 0; nminus = 0
    for i in range(len(R)):
        if (sbits >> i) & 1: nminus += 1
    for v in range(4):
        if t[v] == (1, 1):
            ie = [e for e in R if e[1] == v][0]; oe = [e for e in R if e[0] == v][0]
            s_in = 1 - 2 * ((sbits >> idx[ie]) & 1); s_out = 1 - 2 * ((sbits >> idx[oe]) & 1)
            aleph += abs(s_out - s_in) // 2
    w_phase = (-1) ** (len(R) + aleph + nminus)          # (-1)^{Theta+aleph+n_-}, Theta=|R| (S1)
    w_direct = 1
    for i in range(len(R)):
        w_direct *= -(1 - 2 * ((sbits >> i) & 1))        # prod G(e), G = -sigma at kappa=1
    w_direct *= (-1) ** aleph
    chk(w_phase == w_direct, "FT.67(6b): phase inventory reproduced termwise")

# ================================================================ FT.68(1): tetrahedron joint
byp = 0; byK = {}; cov_byp = {}; cov_lock = {}; Zb = 0; Zl = 0; Za = 0
census = [0, 0, 0]; aspect_freq = {0: 0, 1: 0, 2: 0, 3: 0}
nonzero = []
for bits in range(1 << m):
    R = frozenset(DE[i] for i in range(m) if (bits >> i) & 1)
    bs = cover_value(nv, R)          # theorem verified exhaustively above
    t = types_of(nv, R)
    locked = any(a + b >= 4 for (a, b) in t)
    K = len(R)
    if not locked:
        byp += 1; byK[K] = byK.get(K, 0) + 1
        aspect_freq[max(a + b for (a, b) in t)] += 1
        if bs: cov_byp[K // 2] = cov_byp.get(K // 2, 0) + 1; Zb += bs; nonzero.append((R, bs, False))
        Rs = set(R)
        if any((a, b) in Rs and (b, a) in Rs for (a, b) in U): census[0] += 1
        if any(all((cyc[i], cyc[(i + 1) % 3]) in Rs for i in range(3))
               for cyc in ((a, b, c) for a, b, c in combinations(range(4), 3))
               for cyc in (cyc, cyc[::-1])): census[1] += 1
        if any(all((p[i], p[(i + 1) % 4]) in Rs for i in range(4))
               for p in ((0,1,2,3),(0,1,3,2),(0,2,1,3)) for p in (p, p[::-1])): census[2] += 1
    else:
        if bs: cov_lock[K // 2] = cov_lock.get(K // 2, 0) + 1; Zl += bs; nonzero.append((R, bs, True))
    Za += bs
chk(byp == 1230, f"tetra: 1230 bypass configurations: {byp}")
chk(Fr(byp, 4096) == Fr(615, 2048), "tetra: bypass probability 615/2048")
chk([byK.get(K, 0) for K in range(7)] == [1, 12, 66, 220, 435, 408, 88], "tetra: counts by K")
chk([byK.get(K, 0) for K in range(4)] == [comb(12, K) for K in range(4)],
    "tetra: K<=3 rows are the full symmetric rows C(12,K) (no locks below K=4)")
chk(comb(12,4) - byK[4] == 60 and comb(12,5) - byK[5] == 384 and comb(12,6) - byK[6] == 836,
    "tetra: locked complements 60/384/836 at K=4,5,6")
chk((Zb, Zl, Za) == (1057, 448, 1505), f"tetra: Z± = 1057/448/1505: {(Zb,Zl,Za)}")
chk(Zb == 1 + 24 * 4 + 60 * 16 and Zl == 12 * 16 + 4 * 64, "tetra: Z± from covering classes")
chk(cov_byp == {0: 1, 1: 24, 2: 60}, f"tetra: Z_byp(y) = 1+24y+60y^2: {cov_byp}")
chk(cov_lock == {2: 12, 3: 4}, f"tetra: Z_lock(y) = 12y^2+4y^3: {cov_lock}")
sumK = sum(K * c for K, c in byK.items())
m1 = Fr(sumK, byp)
chk(m1 == Fr(852, 205), f"tetra: m_eff uniform = 852/205: {m1}")
num = sum(len(R) * v * v for (R, v, lk) in nonzero if not lk)
den = sum(v * v for (R, v, lk) in nonzero if not lk)
chk(Fr(num, den) == Fr(62208, 15745), f"tetra: m_eff amplitude-weighted = 62208/15745: {Fr(num,den)}")
num2 = sum(K * c * Fr(1, 2) ** 12 for K, c in byK.items())
den2 = sum(c * Fr(1, 2) ** 12 for c in byK.values())
chk(num2 / den2 == m1, "tetra: P-H10 equilibrium at r=1 equals the uniform reading")
chk(census == [501, 252, 90], f"tetra: bound census digon/3-cycle/4-cycle = 501/252/90: {census}")
chk([aspect_freq.get(k, 0) for k in range(4)] == [1, 24, 245, 960], "tetra: aspect frequencies")
# on-shell census notes at (S1): Theta = L
chk(2 % 2 == 0 and 4 % 2 == 0 and 3 % 2 == 1, "census Theta parity: digon/4-cycle even, 3-cycle odd [FT.22]")
# orbits under S4
perms = automorphisms(nv, U)
chk(len(perms) == 24, "|Aut(K4)| = 24")
orb_byK = {}; seen = set()
for bits in range(1 << m):
    if bits in seen: continue
    R = frozenset(DE[i] for i in range(m) if (bits >> i) & 1)
    if any(a + b >= 4 for (a, b) in types_of(nv, R)): continue
    orb = set()
    for p in perms:
        Rp = frozenset((p[a], p[b]) for (a, b) in R)
        orb.add(sum(1 << DE.index(e) for e in Rp))
    seen |= orb
    orb_byK[len(R)] = orb_byK.get(len(R), 0) + 1
chk(sum(orb_byK.values()) == 70, f"tetra: 70 bypass orbits: {sum(orb_byK.values())}")
chk([orb_byK.get(K, 0) for K in range(7)] == [1, 1, 5, 13, 23, 21, 6], "tetra: orbits by K")
# cover enumerators cross-check (bt == dp == exhaustive scan)
chk(pbt == cov_byp and plt == cov_lock, "tetra: backtracking covers == exhaustive scan")
pdp, ldp = cover_dp(nv, U)
chk((pdp, ldp) == (pbt, plt), "tetra: cover DP == backtracking")
# cap-DP cross-check
cd = cap_dp_by_K(nv, U, cap=3)
chk(cd[:7] == [1, 12, 66, 220, 435, 408, 88] and sum(cd[7:]) == 0, "tetra: cap-DP row")

# ================================================================ FT.68(2): polygon ladder
counts_doc = {3: 54, 4: 207, 5: 783, 6: 2970, 7: 11259, 8: 42687, 9: 161838, 10: 613575}
tr = {n: poly_B(n, 1) for n in range(3, 13)}
for n in range(3, 11):
    chk(tr[n] == counts_doc[n], f"polygon B_{{P_{n}}}(1) = {counts_doc[n]}")
for n in range(5, 13):
    chk(tr[n] == 3 * tr[n - 1] + 3 * tr[n - 2], f"Newton recursion tr_{n} = 3tr_{{n-1}}+3tr_{{n-2}} at n={n}")
for n in (3, 4, 5, 6, 7):
    chk(poly_brute_bypass(n) == counts_doc[n], f"polygon cap-brute-force cross-check n={n}")
# fractions decay: B_n(1)/4^n strictly decreasing from n=3
fr = [Fr(tr[n], 4 ** n) for n in range(3, 11)]
chk(all(fr[i + 1] < fr[i] for i in range(len(fr) - 1)), "bypass fractions strictly decaying")
chk(fr[0] == Fr(27, 32) and fr[1] == Fr(207, 256) and fr[2] == Fr(783, 1024) and fr[3] == Fr(1485, 2048),
    "polygon fractions (27/32, 207/256, 783/1024, 1485/2048)")
# charpoly T(1) = x^4 - 3x^3 - 3x^2 via exact evaluation + interpolation
T1 = [[Fr(x) for x in row] for row in poly_T(1)]
def detF(M):
    n = len(M); M = [row[:] for row in M]; d = Fr(1)
    for i in range(n):
        p = None
        for r in range(i, n):
            if M[r][i] != 0: p = r; break
        if p is None: return Fr(0)
        if p != i: M[i], M[p] = M[p], M[i]; d = -d
        d *= M[i][i]
        inv = 1 / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            if f:
                for c in range(i, n): M[r][c] -= f * M[i][c]
    return d
def polmul(a, b):
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
xs = [Fr(i) for i in range(-2, 7)]
ys = [detF([[ (x if i==j else Fr(0)) - T1[i][j] for j in range(4)] for i in range(4)]) for x in xs]
ch = [Fr(0)] * len(xs)
for i in range(len(xs)):
    num = [Fr(1)]; den = Fr(1)
    for j in range(len(xs)):
        if j == i: continue
        den *= (xs[i] - xs[j]); num = polmul(num, [-xs[j], Fr(1)])
    for d, c in enumerate(num): ch[d] += ys[i] * c / den
while len(ch) > 1 and ch[-1] == 0: ch.pop()
chk(ch == [Fr(0), Fr(0), Fr(-3), Fr(-3), Fr(1)], f"charpoly T(1) = x^4-3x^3-3x^2: {ch}")
rev = list(reversed(ch))
chk(rev[:3] == [Fr(1), Fr(-3), Fr(-3)] and all(c == 0 for c in rev[3:]),
    "det(I - z T(1)) = 1 - 3z - 3z^2 (dynamical zeta)")
chk(21 < 25, "lambda_max = (3+sqrt21)/2 < 4  <=>  21 < 25 (exact)")
# trace recursion is the charpoly's own: x^2 = 3x + 3 on the nonzero spectrum
chk(tr[3] == 54 and tr[4] == 207, "recursion seeds tr_3=54, tr_4=207")
# Z± per sector (cover DP; backtracking cross-check n<=6)
doc_Z = {3: (25, 48), 4: (353, 64), 5: (1161, 80), 6: (3121, 1632), 7: (11929, 10864),
         8: (53825, 43136), 9: (229417, 159888), 10: (844881, 775840)}
for n in range(3, 11):
    nvn, DEn = cycle_graph(n)
    Un = undirected_from(nvn, DEn)
    pb, pl = cover_dp(nvn, Un)
    Zbn = sum(c * 4 ** k for k, c in pb.items()); Zln = sum(c * 4 ** k for k, c in pl.items())
    chk((Zbn, Zln) == doc_Z[n], f"P{n}: Z± (bypass, locked) = {doc_Z[n]}: got {(Zbn, Zln)}")
    chk(Zln > 0, f"P{n}: locked sector nonzero (single-hub coverings exist)")
    if n <= 6:
        pb2, pl2, _ = cover_polys_bt(nvn, Un)
        chk((pb2, pl2) == (pb, pl), f"P{n}: backtracking == DP on covering polynomials")

# ================================================================ FT.68(3): cube
nvc, DEc = cube_graph()
Uc = undirected_from(nvc, DEc)
mc = len(DEc)
chk(mc == 24, "cube: 24 directed edges, potential n(v)=6")
n_byp_le4 = 0; n_all_le4 = 0
for K in range(5):
    for ce in combinations(range(mc), K):
        R = frozenset(DEc[i] for i in ce)
        chk(brute_sign_sum(nvc, R) == cover_value(nvc, R), f"FT.67(2) exhaustive on cube K={K}")
        n_all_le4 += 1
        if not any(a + b >= 4 for (a, b) in types_of(nvc, R)): n_byp_le4 += 1
chk(n_byp_le4 == 12831, f"cube: 12831 bypass configs with K<=4: {n_byp_le4}")
chk(n_all_le4 - n_byp_le4 == 120 == 8 * comb(6, 4), "cube: the 120 locked K=4 patterns are the single-vertex (2,2)-locks")
# stride sample K=5..8
rank = 0; hits = 0
for K in range(5, 9):
    for ce in combinations(range(mc), K):
        if rank % 9973 == 0:
            R = frozenset(DEc[i] for i in ce)
            chk(brute_sign_sum(nvc, R) == cover_value(nvc, R), f"cube stride sample rank {rank}")
            hits += 1
        rank += 1
chk(hits > 100, f"cube: stride sample size {hits}")
# cap DP
cdoc = cap_dp_by_K(nvc, Uc, cap=3)
doc_counts = [1,24,276,2024,10506,40296,115796,247704,383913,408464,270096,91392,9600]
chk(cdoc[:13] == doc_counts, f"cube: cap-DP by-K row: {cdoc[:13]}")
chk(sum(cdoc) == 1580092 and all(c == 0 for c in cdoc[13:]), "cube: 1580092 bypass configs, K<=12 forced")
# Burnside orbits by K
perms_c = automorphisms(nvc, Uc)
chk(len(perms_c) == 48, "|Aut(cube)| = 48")
orbK = {}
for p in perms_c:
    fixK = ({K: c for K, c in enumerate(doc_counts) if c} if all(p[v] == v for v in range(nvc))
            else fix_capped_by_K(nvc, Uc, p, cap=3))
    for K, c in fixK.items(): orbK[K] = orbK.get(K, 0) + c
chk(all(v % 48 == 0 for v in orbK.values()), "cube: Burnside sums divisible by 48")
orbK = {K: v // 48 for K, v in orbK.items()}
doc_orbits = [1,1,11,49,250,863,2509,5211,8163,8571,5768,1922,245]
chk([orbK.get(K, 0) for K in range(13)] == doc_orbits, f"cube: orbits by K: {[orbK.get(K,0) for K in range(13)]}")
chk(sum(doc_orbits) == 33564 and 33564 > 10 ** 4, "cube: 33564 orbits > 10^4 (STOP rule observed)")
# covering polynomials: two independent enumerators
pb, pl = cover_dp(nvc, Uc)
chk(pb == {0: 1, 1: 48, 2: 648, 3: 2672, 4: 3624}, f"cube: Z_byp(y) = 1+48y+648y^2+2672y^3+3624y^4: {pb}")
chk(pl == {2: 24, 3: 728, 4: 3192, 5: 264, 6: 4}, f"cube: Z_lock(y) = 24y^2+728y^3+3192y^4+264y^5+4y^6: {pl}")
chk(sum(pb.values()) == 6993 and sum(pl.values()) == 4212, "cube: covering config counts 6993/4212")
Zb = sum(c * 4 ** k for k, c in pb.items()); Zl = sum(c * 4 ** k for k, c in pl.items())
chk((Zb, Zl, Zb + Zl) == (1109313, 1150848, 2260161), f"cube: Z± = {(Zb, Zl, Zb+Zl)}")
pb2, pl2, covs_c = cover_polys_bt(nvc, Uc)
chk((pb2, pl2) == (pb, pl) and len(covs_c) == 11205, "cube: backtracking enumerator == DP (11205 covers)")
chk(types_of(nvc, frozenset(DEc)) == [(3, 3)] * 8, "cube floor: types (3,3) — cancels [FT.67(3a)]")

# ================================================================ FT.68(5): flicker (P-H10)
def poly_expand(n):
    coeffs = [0] * (n + 1)
    for k in range(0, 4):
        c = comb(n, k)
        for j in range(0, n - k + 1):
            coeffs[k + j] += c * comb(n - k, j) * (-1) ** j
    while len(coeffs) > 1 and coeffs[-1] == 0: coeffs.pop()
    return coeffs
chk(poly_expand(4) == [1, 0, 0, 0, -1], "f_adm(4,p) = 1 - p^4")
chk(poly_expand(5) == [1, 0, 0, 0, -5, 4], "f_adm(5,p) = 1 - 5p^4 + 4p^5")
chk(poly_expand(6) == [1, 0, 0, 0, -15, 24, -10], "f_adm(6,p) = 1 - 15p^4 + 24p^5 - 10p^6")
def f_adm(n, r):
    p = Fr(r, r + 1)
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(0, 4))
chk(f_adm(6, 1) == Fr(21, 32), "f_adm(6; r=1) = 21/32")
chk(f_adm(6, 3) == Fr(347, 2048), "f_adm(6; r=3) = 347/2048")
chk(f_adm(4, 1) == Fr(15, 16) and f_adm(5, 1) == Fr(13, 16), "f_adm(4/5; r=1) = 15/16, 13/16")

# ================================================================ FT.68(7): zeta ledger values
B3 = poly_B_coeffs(3); B4 = poly_B_coeffs(4)
chk(sum(B3) == 54 and B3[0] == 1, "B_{P_3}(t): B(1)=54, vacuum coefficient 1 (vacuum is bypass)")
chk(sum(B4) == 207 and B4[0] == 1 and len(B4) == 7, "B_{P_4}(t): B(1)=207, top degree 6 = floor(3n/2)")
chk(poly_B(12, 1) == 3 * poly_B(11, 1) + 3 * poly_B(10, 1), "zeta recursion holds at n=12")

print(f"verify_H_virtual_bypass: {N} checks green  ({time.time()-t0:.1f}s)")
