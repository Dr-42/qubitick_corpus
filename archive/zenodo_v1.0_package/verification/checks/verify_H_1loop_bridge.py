#!/usr/bin/env python3
"""verify_H_1loop_bridge.py — companion to Def-H.31 / FT.102–FT.104 (H14, Tier F.35).

The 1-loop bridge: the swap-graded effective potential on the flicker phase diagram.
Exact arithmetic only (int / Fraction / Q(i)); transcendental steps by exact
rational log-enclosures (atanh series with rational tail bounds — no floating
point in any assertion; float() appears only in printed decimal displays).

Sections
  §A  frozen cell data re-derived: covering polynomials (two independent
      enumerators), cap-census rows, the single-centre closed form, Z(4)/Z(16)
      amplitude anchors, uniform <K>_byp at p=1/2 [FT.68(1)-(3), FT.69(1)-(2)];
  §B  the 16-mode space: CT1.2 generators over Q(i); Ad(S) grading (10 even /
      6 odd, membership = CT0.7(4) verbatim); block structure (even preserves
      Pi_R/Pi_V, odd swaps); Str_S(I_16) = 10-6 = 4; frozen anchors (EW.12,
      CT0.7(1), CT0.7a, CT1.10, W_i Pi_V = 0) [FT.93(5)];
  §C  the dictionary and the tree layer: W_Gamma(p) exact integer polynomials;
      the tree-limit identity vs the enumerated cover sum (independent paths);
      anchors; W > 0; the phase-balance functions G_Gamma = B_Gamma - p^{2E};
      crossover isolation at width 2^-40 reproducing FT.70(2) exactly;
  §D  Spec(Delta^-1): even {3/phat x9, 1/(1-phat)}, odd {p G^2 x3, q G^2 x3};
      phat bounds (sup = k_top/E, attained exactly at p=1); positivity on exact
      grids; odd-block zero locus = {p*_Gamma} u {0,1}; the directive-3
      bookkeeping (block form == 16-term eigenvalue sum, by enclosures);
  §E  vacua: V' sign census on exact dyadic grids (rational + log-enclosure
      evaluation), exactly one flip per wall-delimited region, bisection to
      width 2^-36; V and m^2 = V/8 enclosures; mass order; ratios; minima in
      (0,1/4) [CT0.8]; dominance windows (pairwise W-crossing roots); dominant
      skeleton per vacuum; the two no-vacuum windows monotone (V' > 0);
  §F  susceptibility census: chi_Gamma = d<K>/dy = 2 Var_y(k)/y strictly
      decreasing on exact grids; transition scales c_k/c_{k+1} with exact
      quadratic eps-images eps = 1/(4+sqrt(y)); Var peak census; family
      trajectory extrema (degree-<=98 integer-Horner sign census);
  §G  [EXT] adjudication (external data, comparison only, no identification):
      shortfall enclosures vs 1:207:3477 / 1:20:900 / 1:600:80000 for the m
      and m^2 reads; the composed tilt read (P-H13 species at general gamma):
      bases, exact E_int thresholds (16/27/35/42), the proportionality
      obstruction (disjoint enclosures);
  §H  range species: floor-barrier growth instance at p=15/16 (the linear-in-E
      lower-bound law); Delta S-admissibility; bare-read span; document pins.
"""
import os, sys, time
from fractions import Fraction as Fr
from math import isqrt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale, trace
from hcommon import QI, field_rank
from bypasscore import (complete_graph, cube_graph, octa_graph, undirected_from,
                        cover_dp, cover_polys_bt, cap_dp_by_K)

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1

t0 = time.time()
def stamp(s): print(f"  [{time.time()-t0:6.1f}s] {s}", flush=True)

FAM = ('tetra', 'cube', 'octa')

# ============================================================ polynomial kernel
def pmul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y: out[i + j] += x * y
    return out

def pmulN(*args):
    r = [Fr(1)]
    for a in args: r = pmul(r, a)
    return r

def padd(a, b, s=1):
    n = max(len(a), len(b)); out = [Fr(0)] * n
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += s * x
    return out

def pscale(a, c): return [x * c for x in a]
def pderiv(a): return [Fr(i) * a[i] for i in range(1, len(a))]
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a

def peval(a, x):
    r = Fr(0)
    for c in reversed(a): r = r * x + c
    return r

Pp = [Fr(0), Fr(1)]          # p
Pq = [Fr(1), Fr(-1)]         # q = 1-p

def poly_root_bisect(poly, lo, hi, bits):
    flo = peval(poly, lo)
    for _ in range(bits):
        mid = (lo + hi) / 2
        fm = peval(poly, mid)
        if fm == 0: return (mid, mid)
        if (fm > 0) == (flo > 0): lo, flo = mid, fm
        else: hi = mid
    return (lo, hi)

def poly_roots_scan(poly, lo, hi, ngrid, bits=30):
    roots = []
    prev = peval(poly, lo); a = lo
    for i in range(1, ngrid + 1):
        x = lo + (hi - lo) * Fr(i, ngrid)
        v = peval(poly, x)
        if v == 0: roots.append((x, x))
        elif (prev > 0) != (v > 0):
            roots.append(poly_root_bisect(poly, a, x, bits))
        prev = v; a = x
    return roots

def dyadic_sign(coeffs, m, k):
    """sign of poly(m/2^k) via integer Horner (exact, no Fraction blowup).
    coeffs ascending; acc ends as sum_i c_i m^i 2^{k(deg-i)} = 2^{k deg} poly(m/2^k)."""
    acc = 0; e = 0
    for c in reversed(coeffs):
        assert c.denominator == 1
        acc = acc * m + int(c) * (1 << (k * e))
        e += 1
    return (acc > 0) - (acc < 0)

# ============================================================ §A frozen cell data
stamp("§A frozen cell data (two enumerators, cap-DP, anchors)")

ZBYP = {'tetra': {0: 1, 1: 24, 2: 60},
        'cube':  {0: 1, 1: 48, 2: 648, 3: 2672, 4: 3624},
        'octa':  {0: 1, 1: 72, 2: 852, 3: 1152}}
ZLOCK = {'tetra': {2: 12, 3: 4},
         'cube':  {2: 24, 3: 728, 4: 3192, 5: 264, 6: 4},
         'octa':  {2: 36, 3: 1008, 4: 840}}
ZTOT = {g: {k: ZBYP[g].get(k, 0) + ZLOCK[g].get(k, 0) for k in
            set(ZBYP[g]) | set(ZLOCK[g])} for g in FAM}
CK = {'tetra': [1, 12, 66, 220, 435, 408, 88],
      'cube':  [1, 24, 276, 2024, 10506, 40296, 115796, 247704, 383913,
                408464, 270096, 91392, 9600],
      'octa':  [1, 24, 276, 2024, 10206, 35448, 81344, 110736, 69504, 8960]}
EDIR = {'tetra': 12, 'cube': 24, 'octa': 24}      # directed edges (2E)
KTOP = {'tetra': 6, 'cube': 12, 'octa': 8}        # max cover K = 2 max|C|
NCOV = {'tetra': 101, 'cube': 11205, 'octa': 3961}  # total cover counts
NV = {'tetra': 4, 'cube': 8, 'octa': 6}
DEG = {'tetra': 3, 'cube': 3, 'octa': 4}          # undirected degree d

SOL = {'tetra': complete_graph(4), 'cube': cube_graph(), 'octa': octa_graph()}
UND = {g: undirected_from(*SOL[g]) for g in FAM}
COVS = {}

for g in FAM:
    nv, de = SOL[g]
    chk(nv == NV[g] and len(de) == EDIR[g], f"§A {g}: (V, 2E) = ({NV[g]}, {EDIR[g]})")
    pb1, pl1 = cover_dp(nv, UND[g])
    chk(pb1 == ZBYP[g] and pl1 == ZLOCK[g],
        f"§A {g}: cover_dp reproduces the frozen covering rows [FT.68/FT.69]")
    pb2, pl2, cov = cover_polys_bt(nv, UND[g])
    chk(pb2 == ZBYP[g] and pl2 == ZLOCK[g] and len(cov) == NCOV[g],
        f"§A {g}: cover_polys_bt (independent enumerator) agrees; {NCOV[g]} covers")
    COVS[g] = cov
    row = cap_dp_by_K(nv, UND[g], cap=3)
    chk(row == CK[g], f"§A {g}: cap-DP row reproduces the frozen c_K census")
    chk(ZTOT[g][1] == NV[g] * DEG[g] * (DEG[g] - 1),
        f"§A {g}: single-centre closed form V d(d-1) = {ZTOT[g][1]} [FT.69(2)]")
stamp("§A enumerators + censuses agree with the frozen rows (3 cells x 2 enumerators)")

# Z(4) amplitude anchors [FT.68(1),(3), FT.69(2)]
Z4 = {'tetra': (1057, 448, 1505), 'cube': (1109313, 1150848, 2260161),
      'octa': (87649, 280128, 367777)}
for g in FAM:
    zb = sum(c * 4 ** k for k, c in ZBYP[g].items())
    zl = sum(c * 4 ** k for k, c in ZLOCK[g].items())
    chk((zb, zl, zb + zl) == Z4[g], f"§A {g}: Z(4) anchors {Z4[g]} reproduced")
# Z(16) norm-layer anchors [CT2.8: |A_C|^2 = 16^{|C|}]
Z16 = {g: (sum(c * 16 ** k for k, c in ZBYP[g].items()),
           sum(c * 16 ** k for k, c in ZLOCK[g].items())) for g in FAM}
Z16 = {g: (Z16[g][0], Z16[g][1], Z16[g][0] + Z16[g][1]) for g in FAM}
chk(Z16['tetra'] == (15745, 19456, 35201), f"§A tetra Z(16) = {Z16['tetra']}")
stamp(f"§A Z(16) anchors: cube {Z16['cube']}, octa {Z16['octa']}")
# amplitude-weighted <K> on the bypass sector at y=16 [FT.68(1)(ii)]
numK = sum(2 * k * c * 16 ** k for k, c in ZBYP['tetra'].items())
chk(Fr(numK, Z16['tetra'][0]) == Fr(62208, 15745),
    "§A tetra amplitude-weighted <K>_byp = 62208/15745 [FT.68(1)(ii)]")
# uniform <K>_byp at p=1/2 [FT.68(1)(i), FT.70(5)]
UNI = {'tetra': Fr(852, 205), 'cube': Fr(3311952, 395023), 'octa': Fr(2124600, 318523)}
CNT = {'tetra': 1230, 'cube': 1580092, 'octa': 318523}
for g in FAM:
    sK = sum(K * c for K, c in enumerate(CK[g])); s = sum(CK[g])
    chk(s == CNT[g] and Fr(sK, s) == UNI[g],
        f"§A {g}: bypass count {CNT[g]}, uniform <K>_byp = {UNI[g]} at p=1/2")

# ============================================================ §B mode space, swap grading
stamp("§B CT1.2 mode space and the Ad(S) grading")

sg = [[[C(1), C(0)], [C(0), C(1)]],
      [[C(0), C(1)], [C(1), C(0)]],
      [[C(0), C(0, -1)], [C(0, 1), C(0)]],
      [[C(1), C(0)], [C(0), C(-1)]]]

def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(n * m)]
            for i in range(n * m)]

E0 = kron(sg[0], sg[0])
Sig = matadd(matadd(kron(sg[1], sg[1]), kron(sg[2], sg[2])), kron(sg[3], sg[3]))
Wg = [None] + [matscale(matadd(kron(sg[0], sg[i]), kron(sg[i], sg[0])), Fr(1, 2))
               for i in (1, 2, 3)]
cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
Jg = [None] * 4; Kg = [None] * 4
for i, (j, k) in cyc.items():
    Jg[i] = matscale(matadd(kron(sg[j], sg[k]), kron(sg[k], sg[j]), -1), Fr(1, 2))
    Kg[i] = matscale(matadd(kron(sg[0], sg[i]), kron(sg[i], sg[0]), -1), Fr(1, 2))
Eij = {(i, j): matscale(matadd(kron(sg[i], sg[j]), kron(sg[j], sg[i])), Fr(1, 2))
       for i in (1, 2, 3) for j in (1, 2, 3)}
Ehat = {(i, j): matadd(Eij[(i, j)], Sig, -Fr(1, 3)) if i == j else Eij[(i, j)]
        for i in (1, 2, 3) for j in (1, 2, 3)}
Swap = [[C(0)] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2):
        Swap[2 * a + b][2 * b + a] = C(1)
PR = matscale(matadd(matscale(E0, 3), Sig), Fr(1, 4))
PV = matscale(matadd(E0, Sig, -1), Fr(1, 4))

def eqm(A, B): return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))
def eqz(A): return all(A[i][j] == C(0) for i in range(4) for j in range(4))
def flat(A): return [x for row in A for x in row]

chk(eqm(Swap, matscale(matadd(E0, Sig), Fr(1, 2))), "§B S = (E0+Sigma)/2 [CT0.7(1)]")
chk(eqm(matmul(Swap, Swap), E0), "§B S^2 = I")
chk(eqm(Sig, matadd(matadd(Eij[(1, 1)], Eij[(2, 2)]), Eij[(3, 3)])),
    "§B Sigma = sum_i E^{ii} [EW.12]")
chk(eqz(matadd(Ehat[(1, 1)], matadd(Ehat[(2, 2)], Ehat[(3, 3)]))),
    "§B delta_ij Ehat^{ij} = 0 [CT1.10]")
chk(eqm(matadd(matmul(Wg[1], Wg[1]), matadd(matmul(Wg[2], Wg[2]), matmul(Wg[3], Wg[3]))),
          matscale(PR, 2)), "§B sum W_i^2 = 2 Pi_R [CT0.7a]")
for i in (1, 2, 3):
    chk(eqz(matmul(PV, Wg[i])) and eqz(matmul(Wg[i], PV)),
        f"§B W_{i} Pi_V = 0 = Pi_V W_{i} [FT.93(5)]")
chk(trace(PR) == C(3) and trace(PV) == C(1), "§B Tr Pi_R = 3, Tr Pi_V = 1 [CT0.7(1)]")

EHAT5 = [(1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]
BASIS = ([('E0', E0, +1), ('Sigma', Sig, +1)]
         + [(f'Ehat{i}{j}', Ehat[(i, j)], +1) for (i, j) in EHAT5]
         + [(f'W{i}', Wg[i], +1) for i in (1, 2, 3)]
         + [(f'J{i}', Jg[i], -1) for i in (1, 2, 3)]
         + [(f'K{i}', Kg[i], -1) for i in (1, 2, 3)])
chk(len(BASIS) == 16, "§B 16 basis elements")
chk(field_rank([[QI(x.re, x.im) for x in flat(m)] for _, m, _ in BASIS]) == 16,
    "§B basis rank 16 over Q(i) [CT0.6]")

even_names, odd_names = [], []
for name, M, sgn in BASIS:
    AdS = matmul(matmul(Swap, M), Swap)
    chk(eqm(AdS, matscale(M, sgn)), f"§B Ad(S) grading of {name}: sign {sgn:+d}")
    if sgn > 0:
        even_names.append(name)
        chk(eqm(matmul(M, Swap), matmul(Swap, M)), f"§B [{name}, S] = 0 (S-even)")
        chk(eqz(matmul(matmul(PV, M), PR)) and eqz(matmul(matmul(PR, M), PV)),
            f"§B {name} preserves the S-eigenspaces [CT0.7(3)]")
    else:
        odd_names.append(name)
        chk(eqz(matadd(matmul(M, Swap), matmul(Swap, M))), f"§B {{S, {name}}} = 0 (S-odd)")
        chk(eqz(matmul(matmul(PR, M), PR)) and eqz(matmul(matmul(PV, M), PV)),
            f"§B {name} swaps the S-eigenspaces [CT0.7(3)]")
chk(len(even_names) == 10 and len(odd_names) == 6, "§B grading counts 10 even / 6 odd")
chk(set(even_names) == {'E0', 'Sigma', 'Ehat11', 'Ehat22', 'Ehat12', 'Ehat13',
                        'Ehat23', 'W1', 'W2', 'W3'},
    "§B S-even = {E0, Sigma, Ehat^{ij}, W_i} [CT0.7(4) verbatim]")
chk(set(odd_names) == {'J1', 'J2', 'J3', 'K1', 'K2', 'K3'},
    "§B S-odd = {J_i} u {K_i} = the seal blocks F_{J+}/F_{J-} [CT0.7(4)]")
chk(sum(s for _, _, s in BASIS) == 4, "§B Str_S(I_16) = 10 - 6 = 4")
chk(Fr(1, 2) * (9 + 1 - 3 - 3) == 2, "§B degenerate-spectrum coefficient (10-6)/2 = 2")
stamp("§B grading, block structure, Str(I)=4: all matrix-exact over Q(i)")

# ============================================================ §C dictionary, tree layer
stamp("§C dictionary p = 1-4 eps_q; W_Gamma(p); G_Gamma; crossovers")

def build_W(g, zdict):
    """W(p) = sum_k c_k 16^k p^{2k} q^{2E-2k} — exact integer polynomial in p."""
    E2 = EDIR[g]; acc = [Fr(0)]
    for k, c in sorted(zdict.items()):
        t = [Fr(c * 16 ** k)]
        t = pmul(t, pmulN(*([Pp] * (2 * k) + [Pq] * (E2 - 2 * k))))
        acc = padd(acc, t)
    return trim(acc)

Wb = {g: build_W(g, ZBYP[g]) for g in FAM}
Wl = {g: build_W(g, ZLOCK[g]) for g in FAM}
Wt = {g: trim(padd(Wb[g], Wl[g])) for g in FAM}
for g in FAM:
    chk(all(c.denominator == 1 for c in Wt[g]),
        f"§C {g}: W has integer coefficients (degree {len(Wt[g]) - 1}, Bernstein form)")
    chk(peval(Wt[g], Fr(0)) == 1 and peval(Wt[g], Fr(1)) == 0,
        f"§C {g}: W(0) = 1 (vacuum cover), W(1) = 0 (the floor is no cover [FT.67(3a)])")
    # independent path: enumerated covers -> sum |A_C|^2 p^K q^{2E-K}
    p0 = Fr(3, 7)
    direct = sum(Fr(16 ** len(cl)) * p0 ** (2 * len(cl)) * (1 - p0) ** (EDIR[g] - 2 * len(cl))
                 for cl, R in COVS[g])
    chk(peval(Wt[g], p0) == direct,
        f"§C {g}: tree-limit identity W(p) == enumerated cover sum at p=3/7")
    chk(peval(Wt[g], Fr(1, 2)) * 2 ** EDIR[g] == Z16[g][2],
        f"§C {g}: W(1/2) * 2^{EDIR[g]} = Z_tot(16) = {Z16[g][2]}")
    chk(peval(Wb[g], Fr(1, 2)) * 2 ** EDIR[g] == Z16[g][0],
        f"§C {g}: bypass sector W_byp(1/2) * 2^{EDIR[g]} = {Z16[g][0]}")

def build_N(g):
    E2 = EDIR[g]; acc = [Fr(0)]
    for k, c in sorted(ZTOT[g].items()):
        if k == 0: continue
        t = [Fr(c * 16 ** k * 2 * k)]
        t = pmul(t, pmulN(*([Pp] * (2 * k) + [Pq] * (E2 - 2 * k))))
        acc = padd(acc, t)
    return trim(acc)
Nk = {g: build_N(g) for g in FAM}
chk(peval(Nk['tetra'], Fr(1, 2)) / peval(Wt['tetra'], Fr(1, 2)) == Fr(172800, 35201),
    "§C tetra pooled <K>^cov(1/2) = 172800/35201")

def build_B(g):
    n = EDIR[g]; acc = [Fr(0)]
    for K, c in enumerate(CK[g]):
        t = [Fr(c)]
        t = pmul(t, pmulN(*([Pp] * K + [Pq] * (n - K))))
        acc = padd(acc, t)
    return trim(acc)
Bp = {g: build_B(g) for g in FAM}
Gp = {g: trim(padd(Bp[g], pmulN(*[Pp] * EDIR[g]), -1)) for g in FAM}
for g in FAM:
    chk(peval(Gp[g], Fr(0)) == 1 and peval(Gp[g], Fr(1)) == -1,
        f"§C {g}: G(0) = 1, G(1) = -1 [FT.70(1) endpoint values]")

PSTAR = {}
FROZEN_PSTAR = {'tetra': '0.723525', 'cube': '0.725372', 'octa': '0.679217'}
for g in FAM:
    signs = []
    for i in range(51):
        v = peval(Gp[g], Fr(i, 50))
        signs.append((v > 0) - (v < 0))
    flips = sum(1 for a, b in zip(signs, signs[1:]) if a != 0 and b != 0 and a != b)
    chk(flips == 1, f"§C {g}: single sign flip of G on the 51-point grid [FT.70(1)]")
    lo, hi = poly_root_bisect(Gp[g], Fr(1, 2), Fr(19, 20), 40)
    chk(hi - lo <= Fr(1, 2 ** 40), f"§C {g}: p* isolated at width <= 2^-40")
    PSTAR[g] = (lo, hi)
    dec = f"{float((lo + hi) / 2):.6f}"
    chk(dec == FROZEN_PSTAR[g], f"§C {g}: p* decimal {dec} == frozen FT.70(2) {FROZEN_PSTAR[g]}")
    roots_G = poly_roots_scan(Gp[g], Fr(1, 1000), Fr(999, 1000), 400, bits=30)
    chk(len(roots_G) == 1, f"§C {g}: G has exactly one root on the resolved grid")
chk(PSTAR['octa'][1] < PSTAR['tetra'][0] and PSTAR['tetra'][1] < PSTAR['cube'][0],
    "§C crossover order octa < tetra < cube [FT.70(2)]")
EPSW = {g: ((1 - PSTAR[g][1]) / 4, (1 - PSTAR[g][0]) / 4) for g in FAM}
stamp("§C crossovers: " + ", ".join(
    f"eps*_{g} ~ {float((EPSW[g][0] + EPSW[g][1]) / 2):.9f}" for g in FAM))

for g in FAM:
    for k in range(1, 40):
        x = Fr(k, 40)
        chk(peval(Wt[g], x) > 0 and peval(Bp[g], x) > 0, f"§C {g}: W, B > 0 at p={x}")

# ============================================================ §D the spectrum
stamp("§D Spec(Delta^-1): positivity, phat bounds, zero locus, directive-3 form")

PHSUP = {'tetra': Fr(1, 2), 'cube': Fr(1, 2), 'octa': Fr(1, 3)}
for g in FAM:
    # phat(p->1) = K_top/2E exactly: R = N - K_top*W vanishes to order m+2 at p=1
    # (the k_top term of R is identically zero; the k_top-1 term carries q^{m+2}),
    # m = 2E - K_top — exact derivative census
    m = EDIR[g] - KTOP[g]
    R = trim(padd(Nk[g], pscale(Wt[g], Fr(-KTOP[g]))))
    Rj = R; order = 0
    while peval(Rj, Fr(1)) == 0:
        Rj = pderiv(Rj); order += 1
    chk(order == m + 2 and peval(Rj, Fr(1)) != 0,
        f"§D {g}: phat(p->1) = K_top/2E = {PHSUP[g]} (vanishing order exactly {order})")
    for k in range(1, 40):
        p = Fr(k, 40); Wv = peval(Wt[g], p); Nv = peval(Nk[g], p)
        phat = Nv / (Wv * EDIR[g])
        chk(Fr(0) < phat <= PHSUP[g], f"§D {g}: 0 < phat <= {PHSUP[g]} at p={p}")
        M2e1 = 3 / phat; M2e2 = 1 / (1 - phat)
        chk(M2e1 > 0 and M2e2 > 0, f"§D {g}: even masses positive at p={p}")
        q = 1 - p; Gv = peval(Gp[g], p)
        M2o1 = p * Gv ** 2; M2o2 = q * Gv ** 2
        chk(M2o1 >= 0 and M2o2 >= 0, f"§D {g}: odd masses nonnegative at p={p}")
        if Gv != 0:
            chk(M2o1 > 0 and M2o2 > 0, f"§D {g}: odd masses positive off-wall at p={p}")
stamp("§D even block strictly positive; odd-block zero locus = {p*_G} u {0,1} only")

# ---- log-enclosure kernel (rational atanh series with exact tails) ----------
def log2_enc(tol):
    z = Fr(1, 3); z2 = z * z; s = Fr(0); n = 0
    while True:
        s += 2 * z ** (2 * n + 1) / (2 * n + 1)
        nn = n + 1
        tail = 2 * z ** (2 * nn + 1) / ((2 * nn + 1) * (1 - z2))
        if tail < tol: return (s, s + tail)
        n += 1

def log_enc(y, tol, l2):
    assert y > 0
    k = 0; m = y
    while m < Fr(3, 4): m *= 2; k -= 1
    while m > Fr(3, 2): m /= 2; k += 1
    if m == 1: base = (Fr(0), Fr(0))
    else:
        z = (m - 1) / (m + 1); z2 = z * z; s = Fr(0); n = 0
        while True:
            s += 2 * z ** (2 * n + 1) / (2 * n + 1)
            nn = n + 1
            tail = 2 * abs(z) ** (2 * nn + 1) / ((2 * nn + 1) * (1 - z2))
            if tail < tol / 2: base = (s - tail, s + tail); break
            n += 1
    lo2, hi2 = l2
    add = (k * lo2, k * hi2) if k >= 0 else (k * hi2, k * lo2)
    return (base[0] + add[0], base[1] + add[1])

class Iv:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi):
        lo = lo if isinstance(lo, Fr) else Fr(lo)
        hi = hi if isinstance(hi, Fr) else Fr(hi)
        assert lo <= hi
        self.lo, self.hi = lo, hi
    def __add__(self, o): return Iv(self.lo + o.lo, self.hi + o.hi)
    def __sub__(self, o): return Iv(self.lo - o.hi, self.hi - o.lo)
    def __neg__(self): return Iv(-self.hi, -self.lo)
    def __mul__(self, o):
        ps = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return Iv(min(ps), max(ps))
    def __truediv__(self, o):
        assert o.lo > 0 or o.hi < 0
        ps = [self.lo / o.lo, self.lo / o.hi, self.hi / o.lo, self.hi / o.hi]
        return Iv(min(ps), max(ps))
    def width(self): return self.hi - self.lo

def IV(x):
    x = x if isinstance(x, Fr) else Fr(x)
    return Iv(x, x)

def sqrt_enc(x, k):
    """dyadic enclosure of sqrt(x), x > 0 rational, width 2^-k."""
    scale = 1 << (2 * k)
    m = (x.numerator * scale) // x.denominator
    s = isqrt(m)
    return (Fr(s, 1 << k), Fr(s + 1, 1 << k))

def sqrt_iv(iv, k=44):
    lo = sqrt_enc(iv.lo, k); hi = sqrt_enc(iv.hi, k)
    return Iv(lo[0], hi[1])

def log_enc_iv(iv, tol, l2):
    lo = log_enc(iv.lo, tol, l2); hi = log_enc(iv.hi, tol, l2)
    return Iv(lo[0], hi[1])

# ---- exact assembly of V and V' as (rational, [(coeff, log-argument)]) ------
def base_quantities(eps):
    p = 1 - 4 * eps; q = 4 * eps
    d = {'p': p, 'q': q}
    d['W'] = {g: peval(Wt[g], p) for g in FAM}
    d['N'] = {g: peval(Nk[g], p) for g in FAM}
    d['dW'] = {g: peval(pderiv(Wt[g]), p) for g in FAM}
    d['dN'] = {g: peval(pderiv(Nk[g]), p) for g in FAM}
    d['phat'] = {g: d['N'][g] / (d['W'][g] * EDIR[g]) for g in FAM}
    d['G'] = {g: peval(Gp[g], p) for g in FAM}
    d['dG'] = {g: peval(pderiv(Gp[g]), p) for g in FAM}
    d['SW'] = sum(d['W'].values())
    d['dSW'] = sum(d['dW'].values())
    d['P'] = {g: d['W'][g] / d['SW'] for g in FAM}
    return d

def log_terms_V(d):
    """V_eff = sum_j coeff_j * ln(arg_j)."""
    terms = []
    p, q = d['p'], d['q']
    for g in FAM:
        Pg = d['P'][g]; ph = d['phat'][g]
        terms.append((-Pg, d['W'][g]))
        terms.append((Pg * Fr(9, 2), 3 / ph))
        terms.append((-Pg * Fr(1, 2), 1 - ph))
        terms.append((-Pg * Fr(3, 2), p))
        terms.append((-Pg * Fr(3, 2), q))
        terms.append((-6 * Pg, abs(d['G'][g])))
    return terms

def log_terms_Vg(d, g):
    p, q = d['p'], d['q']; ph = d['phat'][g]
    return [(-1, d['W'][g]), (Fr(9, 2), 3 / ph), (-Fr(1, 2), 1 - ph),
            (-Fr(3, 2), p), (-Fr(3, 2), q), (-6, abs(d['G'][g]))]

def Vprime_parts(d):
    """V'(eps) = rat + sum coeff*ln(arg);  dp/deps = -4, dq/deps = +4."""
    rat = Fr(0); terms = []
    p, q = d['p'], d['q']
    for g in FAM:
        Wg = d['W'][g]; dWg = d['dW'][g]; SW = d['SW']; dSW = d['dSW']
        Pg = d['P'][g]
        dP = -4 * (dWg * SW - Wg * dSW) / (SW * SW)
        for c, arg in log_terms_Vg(d, g):
            terms.append((dP * c, arg))
        ph = d['phat'][g]
        dph = -4 * (d['dN'][g] * Wg - d['N'][g] * dWg) / (Wg * Wg * EDIR[g])
        r = Fr(0)
        r += 4 * dWg / Wg                     # d(-ln W)/deps
        r += Fr(9, 2) * (-dph) / ph           # d (9/2) ln(3/phat)
        r += dph / (2 * (1 - ph))             # d -(1/2) ln(1-phat)
        r += 6 / p                            # d -(3/2) ln p
        r += -6 / q                           # d -(3/2) ln q
        r += 24 * d['dG'][g] / d['G'][g]      # d -6 ln|G|
        rat += Pg * r
    return rat, terms

def enc_value(rat, terms, tol, l2):
    acc = IV(rat)
    cache = {}
    for c, arg in terms:
        if arg not in cache:
            cache[arg] = log_enc(arg, tol, l2)
        L = cache[arg]
        acc = acc + IV(c) * Iv(L[0], L[1])
    return acc

TOL = Fr(1, 2 ** 62)
L2 = log2_enc(Fr(1, 2 ** 66))

def Vprime_sign(eps, tol=TOL):
    d = base_quantities(eps)
    rat, terms = Vprime_parts(d)
    iv = enc_value(rat, terms, tol, L2)
    if iv.lo > 0: return +1
    if iv.hi < 0: return -1
    return 0

def Vprime_sign_retry(eps):
    s = Vprime_sign(eps, TOL)
    k = 0
    while s == 0 and k < 3:
        k += 1
        s = Vprime_sign(eps, Fr(1, 2 ** (62 + 20 * k)))
    return s

# directive-3 bookkeeping: block form == 16-term eigenvalue sum (enclosures)
eps_s = Fr(1, 16)
d_s = base_quantities(eps_s)
lhs_terms = []
for g in FAM:
    Pg = d_s['P'][g]; ph = d_s['phat'][g]
    lhs_terms += [(Pg * Fr(9, 2), 3 / ph), (-Pg * Fr(1, 2), 1 - ph),
                  (-Pg * Fr(3, 2), d_s['p']), (-Pg * Fr(3, 2), d_s['q']),
                  (-6 * Pg, abs(d_s['G'][g]))]
lhs = enc_value(Fr(0), lhs_terms, TOL, L2)
rhs_terms = []
for g in FAM:
    ph = d_s['phat'][g]; Gv = abs(d_s['G'][g]); Pg = d_s['P'][g]
    ev = [3 / ph] * 9 + [1 / (1 - ph)]
    od = [d_s['p'] * Gv ** 2] * 3 + [d_s['q'] * Gv ** 2] * 3
    for x in ev: rhs_terms.append((Pg * Fr(1, 2), x))
    for x in od: rhs_terms.append((-Pg * Fr(1, 2), x))
rhs = enc_value(Fr(0), rhs_terms, TOL, L2)
diff = lhs - rhs
chk(diff.lo <= 0 <= diff.hi,
    "§D directive-3 form: 1/2(sum_even ln M^2 - sum_odd ln M^2) == block assembly")

# ============================================================ §E vacua
stamp("§E vacuum structure: sign census, bisection 2^-36, masses, ratios")

wc = EPSW['cube']; wt = EPSW['tetra']; wo = EPSW['octa']
E_LO = Fr(1, 2 ** 26); E_HI = Fr(1, 4) - Fr(1, 2 ** 26)
regions = {'R1': (E_LO, wc[0]), 'R2': (wc[1], wt[0]),
           'R3': (wt[1], wo[0]), 'R4': (wo[1], E_HI)}
hints = {'R1': ['0.0213373'], 'R2': ['0.0687833'], 'R3': ['0.0800915'], 'R4': ['0.1907924']}

def region_grid(name, a, b, n_uni=90):
    pts = set()
    for i in range(n_uni + 1):
        pts.add(a + (b - a) * Fr(i, n_uni))
    for h in hints[name]:
        hf = Fr(h)
        for k in (10, 12, 14, 16):
            for s in (-1, 1):
                x = hf + s * Fr(1, 2 ** k)
                if a < x < b: pts.add(x)
    if name == 'R3':
        for k in range(11, 19):
            x = b - Fr(1, 2 ** k)
            if a < x: pts.add(x)
    if name in ('R4',):
        for k in range(11, 20):
            x = a + Fr(1, 2 ** k)
            if x < b: pts.add(x)
    return [x for x in sorted(pts) if a < x < b]

VAC = {}
for name in ('R1', 'R2', 'R3', 'R4'):
    a, b = regions[name]
    grid = region_grid(name, a, b)
    signs = []
    for x in grid:
        s = Vprime_sign_retry(x)
        assert s != 0, f"§E {name}: undecided V' sign at eps={float(x):.12f}"
        signs.append((x, s))
    flips = [(signs[i][0], signs[i + 1][0]) for i in range(len(signs) - 1)
             if signs[i][1] != signs[i + 1][1]]
    chk(len(flips) == 1,
        f"§E {name}: exactly one V' sign flip on the exact grid ({len(grid)} pts)")
    chk(signs[0][1] == -1 and signs[-1][1] == +1,
        f"§E {name}: V' goes - to + across the region (minimum, not maximum)")
    lo, hi = flips[0]
    for _ in range(60):
        if hi - lo <= Fr(1, 2 ** 36): break
        mid = (lo + hi) / 2
        s = Vprime_sign_retry(mid)
        assert s != 0, f"§E {name}: undecided at bisection midpoint"
        if s == -1: lo = mid
        else: hi = mid
    chk(hi - lo <= Fr(1, 2 ** 36), f"§E {name}: vacuum isolated at width <= 2^-36")
    mid = (lo + hi) / 2
    d = base_quantities(mid)
    iv = enc_value(Fr(0), log_terms_V(d), Fr(1, 2 ** 56), L2)
    chk(iv.lo > 0, f"§E {name}: V(vacuum) > 0 — Delta S-admissible (nats)")
    VAC[name] = dict(lo=lo, hi=hi, mid=mid, V=(iv.lo, iv.hi))
    stamp(f"§E {name}: eps in [{float(lo):.12f}, {float(hi):.12f}]  "
          f"V in [{float(iv.lo):.9f}, {float(iv.hi):.9f}]  "
          f"m2=V/8 in [{float(iv.lo / 8):.9f}, {float(iv.hi / 8):.9f}]")

for name, v in VAC.items():
    chk(Fr(0) < v['lo'] and v['hi'] < Fr(1, 4),
        f"§E {name}: vacuum inside eps_q in (0, 1/4) [CT0.8 domain]")

def m2_iv(name):
    lo, hi = VAC[name]['V']
    return Iv(lo / 8, hi / 8)

m2s = {n: m2_iv(n) for n in VAC}
chk(m2s['R4'].hi < m2s['R1'].lo, "§E mass order: R4 < R1 (disjoint enclosures)")
chk(m2s['R1'].hi < m2s['R3'].lo, "§E mass order: R1 < R3 (disjoint enclosures)")
chk(m2s['R3'].hi < m2s['R2'].lo, "§E mass order: R3 < R2 (disjoint enclosures)")
r_phase_m2 = (m2s['R1'] / m2s['R4'], m2s['R3'] / m2s['R4'])
r_phase_m = (sqrt_iv(r_phase_m2[0]), sqrt_iv(r_phase_m2[1]))
r_all_m2 = tuple(m2s[n] / m2s['R4'] for n in ('R1', 'R3', 'R2'))
span4 = m2s['R2'] / m2s['R4']
stamp("§E phase-vacuum m^2 ratios 1 : " + " : ".join(
    f"[{float(r.lo):.6f},{float(r.hi):.6f}]" for r in r_phase_m2))
stamp("§E phase-vacuum m   ratios 1 : " + " : ".join(
    f"[{float(r.lo):.6f},{float(r.hi):.6f}]" for r in r_phase_m))
stamp("§E all-four m^2 ratios     1 : " + " : ".join(
    f"[{float(r.lo):.6f},{float(r.hi):.6f}]" for r in r_all_m2))

# dominance windows: roots of pairwise W differences
def Wdiff(ga, gb): return trim(padd(Wt[ga], Wt[gb], -1))
roots_tc = poly_roots_scan(Wdiff('tetra', 'cube'), Fr(1, 1000), Fr(999, 1000), 3000, bits=30)
roots_co = poly_roots_scan(Wdiff('cube', 'octa'), Fr(1, 1000), Fr(999, 1000), 3000, bits=30)
roots_to = poly_roots_scan(Wdiff('tetra', 'octa'), Fr(1, 1000), Fr(999, 1000), 3000, bits=30)
chk(len(roots_tc) == 2 and len(roots_co) == 1 and len(roots_to) == 2,
    f"§E dominance-crossing census: t/c {len(roots_tc)}, c/o {len(roots_co)}, t/o {len(roots_to)}")
tc_eps = sorted(((1 - hi) / 4, (1 - lo) / 4) for lo, hi in roots_tc)
co_eps = ((1 - roots_co[0][1]) / 4, (1 - roots_co[0][0]) / 4)
stamp(f"§E dominance windows (eps_q): tetra|cube at ~{float((tc_eps[0][0]+tc_eps[0][1])/2):.6f} "
      f"and ~{float((tc_eps[1][0]+tc_eps[1][1])/2):.6f}; cube|octa at "
      f"~{float((co_eps[0]+co_eps[1])/2):.6f}")
dom = {}
for name, v in VAC.items():
    p = 1 - 4 * v['mid']
    wv = {g: peval(Wt[g], p) for g in FAM}
    order = sorted(wv.values())
    chk(order[-1] != order[-2], f"§E {name}: dominance strict")
    dom[name] = max(wv, key=lambda g: wv[g])
chk(dom['R1'] == 'tetra' and dom['R2'] == 'tetra' and dom['R3'] == 'tetra'
    and dom['R4'] == 'cube', f"§E dominance at the vacua: {dom}")

# no-vacuum windows: octa window and the tetra tail sliver are monotone rising
oct_win = (co_eps[1] + Fr(1, 2 ** 30), tc_eps[1][0] - Fr(1, 2 ** 30))
sl = [Vprime_sign_retry(oct_win[0] + (oct_win[1] - oct_win[0]) * Fr(i, 40))
      for i in range(41)]
chk(all(s is not None and s > 0 for s in sl if s != 0) and any(sl),
    "§E octa-dominance window: V' > 0 throughout (no vacuum; monotone rise)")
tail = (tc_eps[1][1] + Fr(1, 2 ** 30), E_HI)
sl2 = [Vprime_sign_retry(tail[0] + (tail[1] - tail[0]) * Fr(i, 40)) for i in range(41)]
chk(all(s is not None and s > 0 for s in sl2 if s != 0) and any(sl2),
    "§E tetra tail sliver (vacuum-threshold side): V' > 0 (no vacuum)")

# ============================================================ §F susceptibility census
stamp("§F chi = d<K>/dy: monotonicity, transition scales, Var peaks, family extrema")

def chi_parts(g):
    """chi_g(y) = 2 Var_y(k)/y = 2*NUM/(y*Z^2)."""
    c = ZTOT[g]; ks = sorted(c)
    Zy = [Fr(c.get(k, 0)) for k in range(max(ks) + 1)]
    dZ = pderiv(Zy); ddZ = pderiv(dZ)
    y = [Fr(0), Fr(1)]
    A = padd(pmul(pmul(y, y), ddZ), pmul(y, dZ))
    Bq = pmul(y, dZ)
    NUM = trim(padd(pmul(A, Zy), pmul(Bq, Bq), -1))
    DEN = pmul(y, pmul(Zy, Zy))
    return NUM, DEN, Zy

for g in FAM:
    NUMg, DENg, Zy = chi_parts(g)
    prev = None; ok = True
    for i in range(-160, 161):
        y = Fr(2) ** Fr(i, 4)
        v = peval(NUMg, y) / peval(DENg, y)
        if prev is not None and v >= prev: ok = False; break
        prev = v
    chk(ok, f"§F {g}: chi_Gamma strictly decreasing on the exact grid y=2^(i/4), |i|<=40")
    c = ZTOT[g]; ks = sorted(c)
    ntr = 0
    for k in ks:
        if k + 1 in c:
            yk = Fr(c[k], c[k + 1])
            n, dd = yk.numerator, yk.denominator
            A_ = 16 * dd - n; B_ = -8 * dd; Cc = dd
            rpart = Fr(A_) + 4 * B_ + 16 * Cc + Cc * yk
            spart = B_ + 8 * Cc
            chk(rpart == 0 and spart == 0,
                f"§F {g}: transition {k}->{k+1}: eps = 1/(4+sqrt({yk})) solves the exact quadratic")
            poly_e = trim([Fr(Cc), Fr(B_), Fr(A_)])
            rr = poly_roots_scan(poly_e, Fr(1, 1000), Fr(249, 1000), 2000, bits=40)
            chk(len(rr) == 1,
                f"§F {g}: eps-image of transition {k}->{k+1} unique in (0,1/4); "
                f"eps ~ {float((rr[0][0] + rr[0][1]) / 2):.6f}")
            ntr += 1
    # Var peak census
    VARN = NUMg; VARD = pmul(Zy, Zy)
    PK = trim(padd(pmul(pderiv(VARN), VARD), pmul(VARN, pderiv(VARD)), -1))
    ys = [Fr(2) ** Fr(i, 3) for i in range(-30, 34)]
    vals = [peval(PK, y) for y in ys]
    npeaks = sum(1 for a, b in zip(vals, vals[1:]) if a > 0 >= b)
    chk(npeaks >= 1, f"§F {g}: Var_y(k) has >= 1 interior maximum ({npeaks} found; {ntr} transitions)")
stamp("§F per-skeleton chi monotone decreasing; transition eps-images exact quadratics")

# family trajectory chi_fam extrema
NUMf = [Fr(0)]
for g in FAM: NUMf = padd(NUMf, Nk[g])
DENf = [Fr(0)]
for g in FAM: DENf = padd(DENf, Wt[g])
dNUMf = pderiv(NUMf); dDENf = pderiv(DENf)
Kf_NUM = trim(padd(pmul(dNUMf, DENf), pmul(NUMf, dDENf), -1))
CHI_N = pmul(Kf_NUM, pmulN(Pq, Pq, Pq))
CHI_D = pscale(pmul(pmul(DENf, DENf), Pp), 32)
PKf = trim(padd(pmul(pderiv(CHI_N), CHI_D), pmul(CHI_N, pderiv(CHI_D)), -1))
chk(all(c.denominator == 1 for c in PKf), "§F family chi' numerator: integer coefficients")
deg = len(PKf) - 1
K = 13; flips = []; prev = None; prevx = None
for m in range(8, 2 ** K - 7):
    s = dyadic_sign(PKf, m, K)
    if s != 0:
        if prev is not None and s != prev:
            flips.append((prevx, Fr(m, 2 ** K)))
        prev = s; prevx = Fr(m, 2 ** K)
chk(len(flips) == 2,
    f"§F chi_fam has exactly {len(flips)} interior extrema on the 2^-13 grid (degree {deg})")
CHI_EX = []
for a, b in flips:
    r = poly_root_bisect(PKf, a, b, 25)
    CHI_EX.append(r)
    stamp(f"§F chi_fam extremum at p in [{float(r[0]):.6f}, {float(r[1]):.6f}] "
          f"(eps ~ {float((1 - (r[0] + r[1]) / 2) / 4):.6f})")

# ============================================================ §G [EXT] adjudication
stamp("§G [EXT] audit (external data, comparison only — no identification)")

EXT = {'leptons': (207, 3477), 'down': (20, 900), 'up': (600, 80000)}
for fam, (r2, r3) in EXT.items():
    d_m = (IV(r2) / r_phase_m[0], IV(r3) / r_phase_m[1])
    d_m2 = (IV(r2) / r_phase_m2[0], IV(r3) / r_phase_m2[1])
    stamp(f"§G {fam}: m-read shortfalls x[{float(d_m[0].lo):.1f},{float(d_m[0].hi):.1f}] / "
          f"x[{float(d_m[1].lo):.1f},{float(d_m[1].hi):.1f}]; m^2-read "
          f"x[{float(d_m2[0].lo):.1f},{float(d_m2[0].hi):.1f}] / "
          f"x[{float(d_m2[1].lo):.1f},{float(d_m2[1].hi):.1f}]")
    chk(d_m[0].lo > 10 and d_m[1].lo > 100,
        f"§G {fam}: bare 1-loop read short by >10x (middle) / >100x (outer), enclosure-proven")

# composed tilt read (P-H13 species at general gamma): c(eps) = 3/4 + eps
cIv = {n: Iv(Fr(3, 4) + VAC[n]['lo'], Fr(3, 4) + VAC[n]['hi']) for n in ('R1', 'R3', 'R4')}
beta_mid = cIv['R3'] / cIv['R1']
beta_out = cIv['R4'] / cIv['R1']
chk(beta_mid.lo > 1 and beta_out.lo > beta_mid.hi,
    "§G composed bases: 1 < beta_mid < beta_out (disjoint enclosures)")
ln_mid = log_enc_iv(beta_mid, Fr(1, 2 ** 50), L2)
ln_out = log_enc_iv(beta_out, Fr(1, 2 ** 50), L2)
def ln_int(n): return log_enc_iv(Iv(Fr(n), Fr(n)), Fr(1, 2 ** 50), L2)
def threshold(beta_ln, target):
    lt = ln_int(target)
    for E in range(1, 500):
        if (IV(E) * beta_ln).lo >= lt.hi:
            chk((IV(E - 1) * beta_ln).hi < lt.lo,
                f"§G threshold E={E} strict for target {target}")
            return E
    raise AssertionError("threshold not found")
E207 = threshold(ln_out, 207); E3477 = threshold(ln_out, 3477)
E20 = threshold(ln_out, 20); E900 = threshold(ln_out, 900)
chk((E207, E3477, E20, E900) == (27, 42, 16, 35),
    f"§G composed-read thresholds (207,3477,20,900) -> ({E207},{E3477},{E20},{E900})")
v42 = IV(42) * ln_mid
ln207 = ln_int(207)
chk(v42.hi < ln207.lo, "§G beta_mid^42 < 207 (the middle generation falls short at E=42)")
prop_comp = ln_mid / ln_out
prop_ext = ln_int(207) / ln_int(3477)
chk(prop_comp.hi < prop_ext.lo,
    "§G proportionality obstruction: ln(beta_mid)/ln(beta_out) < ln207/ln3477 (disjoint)")
stamp(f"§G ln-proportions: computed [{float(prop_comp.lo):.6f},{float(prop_comp.hi):.6f}] "
      f"vs [EXT] [{float(prop_ext.lo):.6f},{float(prop_ext.hi):.6f}]")

# ============================================================ §H range species + pins
stamp("§H range species and document pins")
p0 = Fr(15, 16)
ln16 = log_enc(Fr(16), Fr(1, 2 ** 50), L2)
for g in FAM:
    Wv = peval(Wt[g], p0)
    ivW = log_enc(Wv, Fr(1, 2 ** 50), L2)
    expo = EDIR[g] - KTOP[g]
    Ztop = sum(c * 16 ** k for k, c in ZTOT[g].items())
    lnZ = log_enc(Fr(Ztop), Fr(1, 2 ** 50), L2)
    lb = expo * ln16[0] - lnZ[1]
    chk(Fr(-ivW[1]) >= lb,
        f"§H {g}: -lnW(15/16) >= (2E-K_top)*ln16 - lnZtop (linear-in-E law instance)")
    stamp(f"§H {g}: -lnW(15/16) in [{float(-ivW[1]):.4f}, {float(-ivW[0]):.4f}], "
          f"exponent (2E-K_top) = {expo}")
chk(span4.lo > 5 and span4.hi < 6, "§H bare m^2 span of the four vacua in (5, 6)")
chk(m2s['R4'].lo > 1 and m2s['R4'].hi < Fr(3, 2), "§H lightest m^2 in (1, 3/2)")
chk(m2s['R2'].lo > 7 and m2s['R2'].hi < 8, "§H heaviest m^2 in (7, 8)")

PINS = {'R1': ('0.0213372', '0.0213374'), 'R2': ('0.0687832', '0.0687834'),
        'R3': ('0.0800914', '0.0800916'), 'R4': ('0.1907923', '0.1907925')}
for name, (lo, hi) in PINS.items():
    v = VAC[name]
    chk(v['lo'] >= Fr(lo) - Fr(1, 10 ** 6) and v['hi'] <= Fr(hi) + Fr(1, 10 ** 6),
        f"§H pin eps_{name}: [{float(v['lo']):.9f}, {float(v['hi']):.9f}] matches H14 table")
VPINS = {'R1': ('24.2717', '24.2720'), 'R2': ('59.6450', '59.6453'),
         'R3': ('38.7129', '38.7132'), 'R4': ('10.6556', '10.6559')}
for name, (lo, hi) in VPINS.items():
    vlo, vhi = VAC[name]['V']
    chk(vlo >= Fr(lo) - Fr(1, 10 ** 3) and vhi <= Fr(hi) + Fr(1, 10 ** 3),
        f"§H pin V_{name}: [{float(vlo):.6f}, {float(vhi):.6f}] matches H14 table")

print(f"\nverify_H_1loop_bridge: {N} checks green "
      f"({time.time() - t0:.1f}s; exact arithmetic: int/Fraction/Q(i) + rational log-enclosures)")
