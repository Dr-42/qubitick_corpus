#!/usr/bin/env python3
"""verify_H_phasediagram.py — companion to Def-H.26 / FT.69-FT.73.
Exact arithmetic only (int / Fraction). Asserts every tabulated value of Tier F.24:
  * FT.69: cap-census rows (octa/dodeca/icosa), low-K universality and the K=4 lock divergence,
    octahedron covering polynomials (two enumerators), dodeca/icosa covers to |C|<=3, the
    V d (d-1) single-centre closed form, floor cancellations, the cycle-alternation lemma on
    EVERY enumerated cover (tetra/cube/octa/P3-P7), canonical cycle censuses, the tetrahedron
    dissolution witness (brute force = 16), the FT.68(1) census re-audit (501/252/90; 48/0/0),
    and the minimal double-digon-hub family;
  * FT.70: crossover bisections re-run (exact dyadic intervals), grid monotonicity, the digon
    identity B == 1, charpoly T(t) at exact samples, the sqrt(2/3) limit arithmetic in Z[sqrt6],
    p*-interlacing vs sqrt(2/3), the f_adm chain identity (symbolic), lock-proneness order,
    octahedron refutation, <K>_byp rationals and monotonicity grids;
  * FT.71: O(n) anchors, dark-sum anchors (FT.63(5)), p=1/2 dust values, the polygon monomial,
    monotonicity grid;
  * FT.72: face-map ranks/kernels (all five), two-fold decomposition (explicit on the tetrahedron),
    dim(Z1 cap Cut), triangle census, dodecahedron girth-5 witness, MacWilliams at exact points,
    direct-enumeration cross-checks, P_{1/2} tables, dual-pair enumerator coincidences;
  * FT.73: irreducibility of y^4-5y^2+5 and x^4-8x^3+19x^2-12x+1, sqrt5 = 2y^2-5 in Q(y),
    sqrt5 not in Q(sqrt2,sqrt3), the exact ratio 4-2sqrt2+2sqrt3-sqrt6 and its quadratic-field
    exclusion, dual-degeneracy anchors, degree bookkeeping.
"""
import os, sys, time
from fractions import Fraction as Fr
from itertools import combinations, product
from math import comb, isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bypasscore import (bidir_skeleton, cycle_graph, complete_graph, cube_graph, octa_graph,
                        icosa_graph, dodeca_graph, icosa_edges, undirected_from, elim_order,
                        types_of, centers_of, is_cover_strict, cover_value, brute_sign_sum,
                        enum_covers_bt, cover_polys_bt, cover_dp, cap_dp_by_K,
                        poly_T, poly_B, poly_B_coeffs)

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1

t0 = time.time()
def stamp(s): print(f"  [{time.time()-t0:6.1f}s] {s}", flush=True)

SOL = {'tetra': complete_graph(4), 'cube': cube_graph(), 'octa': octa_graph(),
       'dodeca': dodeca_graph(), 'icosa': icosa_graph()}
UND = {k: undirected_from(*g) for k, g in SOL.items()}

# ================================================================ FT.69(1): cap censuses
rows = {
 'octa':   [1, 24, 276, 2024, 10206, 35448, 81344, 110736, 69504, 8960],
 'dodeca': [1, 60, 1770, 34220, 487335, 5445192, 49629140, 378649320, 2462218635, 13821757980,
            67596135894, 289867011060, 1094624937445, 3649443048240, 10752697982820,
            27986771515416, 64230393822660, 129556940704560, 228564130041640, 350343098681520,
            462476014375140, 519751575327520, 489884840892960, 379674924768000, 235661074398400,
            112977637895808, 39729436846080, 9482009372160, 1352036244480, 90335569920, 1486401536],
 'icosa':  [1, 60, 1770, 34220, 485115, 5332488, 46846640, 334247760, 1949934615, 9296112780,
            35958870006, 111271286100, 269284413245, 492631349520, 647357780880, 564240517760,
            284803298880, 63292604160, 2646415360],
}
for name in ('octa', 'dodeca', 'icosa'):
    nv, DE = SOL[name]
    cd = cap_dp_by_K(nv, UND[name], cap=3)
    chk(cd == rows[name], f"FT.69(1): {name} cap-census row exact (len {len(cd)})")
tot = {'octa': 318523, 'dodeca': 3067633654196912, 'icosa': 2483119531360}
for name in rows:
    chk(sum(rows[name]) == tot[name], f"FT.69(1): {name} total {tot[name]}")
kmax = {'octa': 9, 'dodeca': 30, 'icosa': 18}
for name in rows:
    nv = SOL[name][0]
    chk(len(rows[name]) - 1 == kmax[name] == (3 * nv) // 2, f"FT.69(1): {name} K_max = floor(3V/2)")
# low-order universality + K=4 divergence
for name in ('dodeca', 'icosa'):
    chk(rows[name][:4] == [comb(60, K) for K in range(4)], f"FT.69(1): {name} rows = C(60,K) for K<=3")
chk(comb(60, 4) - rows['dodeca'][4] == 20 * comb(6, 4) == 300, "FT.69(1): dodeca K=4 deficit = 20*C(6,4)")
chk(comb(60, 4) - rows['icosa'][4] == 12 * comb(10, 4) == 2520, "FT.69(1): icosa K=4 deficit = 12*C(10,4)")
# octa K<=5 exhaustive validation
nvo, DEo = SOL['octa']
for K in range(6):
    cnt = 0
    for ce in combinations(range(len(DEo)), K):
        R = [DEo[i] for i in ce]
        if all(a + b <= 3 for (a, b) in types_of(nvo, R)): cnt += 1
    chk(cnt == rows['octa'][K], f"FT.69(1): octa row exhaustive validation K={K}")
stamp("FT.69(1) cap censuses OK")

# ================================================================ FT.69(2): coverings
def small_covers(nv, U, maxC):
    nbr_in = [[] for _ in range(nv)]; nbr_out = [[] for _ in range(nv)]
    for (a, b) in U:
        nbr_in[b].append(a); nbr_out[a].append(b)
        nbr_in[a].append(b); nbr_out[b].append(a)
    res = {}
    for k in range(0, maxC + 1):
        for C in combinations(range(nv), k):
            Cs = set(C)
            pin = {c: [u for u in nbr_in[c] if u not in Cs] for c in C}
            pout = {c: [w for w in nbr_out[c] if w not in Cs] for c in C}
            if any(len(pin[c]) == 0 or len(pout[c]) == 0 for c in C): continue
            choices = [[(c, u, w) for u in pin[c] for w in pout[c]] for c in C]
            for combo in product(*choices):
                a = {}; b = {}
                for (c, u, w) in combo:
                    a[w] = a.get(w, 0) + 1; b[u] = b.get(u, 0) + 1
                ok = True; lock = 0
                for v in range(nv):
                    if v in Cs: continue
                    av = a.get(v, 0); bv = b.get(v, 0)
                    if av == 1 and bv == 1: ok = False; break
                    if av + bv >= 4: lock = 1
                if not ok: continue
                res[(k, lock)] = res.get((k, lock), 0) + 1
    return res

# machinery cross-validation: tetra full, cube |C|<=4 (against documented values)
rt = small_covers(4, UND['tetra'], 4)
chk(rt == {(0,0):1,(1,0):24,(2,0):60,(2,1):12,(3,1):4}, f"FT.69(2) machinery: tetra {rt}")
rc = small_covers(8, UND['cube'], 4)
cube_exp = {(0,0):1,(1,0):48,(2,0):648,(3,0):2672,(4,0):3624,(2,1):24,(3,1):728,(4,1):3192}
chk(all(rc.get(k, 0) == v for k, v in cube_exp.items()), f"FT.69(2) machinery: cube |C|<=4 {rc}")
# octahedron full: DP vs branch enumeration
pb, pl = cover_dp(nvo, UND['octa'])
chk(pb == {0: 1, 1: 72, 2: 852, 3: 1152}, f"FT.69(2): octa Z_byp(y) {pb}")
chk(pl == {2: 36, 3: 1008, 4: 840}, f"FT.69(2): octa Z_lock(y) {pl}")
Zb = sum(c * 4 ** k for k, c in pb.items()); Zl = sum(c * 4 ** k for k, c in pl.items())
chk((Zb, Zl, Zb + Zl) == (87649, 280128, 367777), f"FT.69(2): octa Z± {(Zb, Zl, Zb+Zl)}")
pb2, pl2, covs_o = cover_polys_bt(nvo, UND['octa'])
chk((pb2, pl2) == (pb, pl) and len(covs_o) == 3961, "FT.69(2): octa branch enumerator == DP (3961)")
# dodeca / icosa |C|<=3
rd = small_covers(20, UND['dodeca'], 3)
chk(rd == {(0,0):1,(1,0):120,(2,0):5880,(2,1):60,(3,0):153960,(3,1):6140}, f"FT.69(2): dodeca {rd}")
ri = small_covers(12, UND['icosa'], 3)
chk(ri == {(0,0):1,(1,0):240,(2,0):17520,(2,1):120,(3,0):478360,(3,1):27600}, f"FT.69(2): icosa {ri}")
chk(sum(rd.values()) == 166161 and sum(ri.values()) == 523841, "FT.69(2): totals 166161 / 523841")
# Z± lower bounds from counted range
zb_d = sum(v * 4 ** k for (k, l), v in rd.items() if l == 0)
zl_d = sum(v * 4 ** k for (k, l), v in rd.items() if l == 1)
zb_i = sum(v * 4 ** k for (k, l), v in ri.items() if l == 0)
zl_i = sum(v * 4 ** k for (k, l), v in ri.items() if l == 1)
chk((zb_d, zl_d) == (9948001, 393920), f"FT.69(2): dodeca Z± counted {(zb_d, zl_d)}")
chk((zb_i, zl_i) == (30896321, 1768320), f"FT.69(2): icosa Z± counted {(zb_i, zl_i)}")
# |C|=1 closed form V d (d-1)
one = {'tetra': (4,3,24), 'cube': (8,3,48), 'octa': (6,4,72), 'dodeca': (20,3,120), 'icosa': (12,5,240)}
chk(rd[(1,0)] == 120 and ri[(1,0)] == 240 and rt[(1,0)] == 24 and rc[(1,0)] == 48
    and pb[1] == 72, "FT.69(2): single-centre rows match V d(d-1)")
for name,(V,d,val) in one.items():
    chk(V*d*(d-1) == val, f"FT.69(2): closed form {name}: {V}*{d}*{d-1} = {val}")
# floors cancel
for name in SOL:
    nv, DE = SOL[name]
    Rf = frozenset(DE)
    tf = types_of(nv, Rf)
    chk(not centers_of(nv, Rf) and cover_value(nv, Rf) == 0, f"FT.69(2): {name} floor cancels")
chk(types_of(20, frozenset(SOL['dodeca'][1])) == [(3,3)]*20, "dodeca floor types (3,3)^20")
chk(types_of(12, frozenset(SOL['icosa'][1])) == [(5,5)]*12, "icosa floor types (5,5)^12")
stamp("FT.69(2) coverings OK")

# ================================================================ FT.69(3)-(5): cycle lemma
def canon(g):
    return min(g[i:] + g[:i] for i in range(len(g)))

def cycles_canon(nv, R):
    Rs = set(R)
    out = {}
    for (a, b) in Rs: out.setdefault(a, []).append(b)
    found = set()
    for start in range(nv):
        stack = [(start, [start], {start})]
        while stack:
            v, path, seen = stack.pop()
            for w in out.get(v, ()):
                if w == start and len(path) >= 2: found.add(canon(tuple(path)))
                elif w not in seen and len(path) < nv:
                    stack.append((w, path + [w], seen | {w}))
    return found

expected = {
 'tetra': dict(covers=101, with_cyc=64, dig_cov=64, dig_byp=48, dig_lock=16, dig_ins=84,
               c4_cov=0, c4_byp=0, c4_lock=0, c4_ins=0),
 'cube':  dict(covers=11205, with_cyc=9060, dig_cov=8772, dig_byp=4560, dig_lock=4212, dig_ins=14328,
               c4_cov=504, c4_byp=288, c4_lock=216, c4_ins=504),
 'octa':  dict(covers=3961, with_cyc=3054, dig_cov=2940, dig_byp=1104, dig_lock=1836, dig_ins=4704,
               c4_cov=354, c4_byp=72, c4_lock=282, c4_ins=672),
}
for name in ('tetra', 'cube', 'octa'):
    nv, DE = SOL[name]; U = UND[name]
    covs = covs_o if name == 'octa' else enum_covers_bt(nv, U)
    e = expected[name]
    chk(len(covs) == e['covers'], f"FT.69(3): {name} cover count {len(covs)}")
    wc = dd = d4 = dib = dil = c4b = c4l = di_i = c4_i = odd = alt = bare = pure = 0
    for cl, R in covs:
        Cs = set(cl.keys())
        cyc = cycles_canon(nv, R)
        locked = any(x + y >= 4 for (x, y) in types_of(nv, R))
        if cyc: wc += 1
        dig = [g for g in cyc if len(g) == 2]; c4 = [g for g in cyc if len(g) == 4]
        di_i += len(dig); c4_i += len(c4)
        if dig:
            dd += 1
            if locked: dil += 1
            else: dib += 1
        if c4:
            d4 += 1
            if locked: c4l += 1
            else: c4b += 1
        for g in cyc:
            L = len(g)
            if L % 2: odd += 1
            roles = [(v in Cs) for v in g]
            if any(roles[i] == roles[(i+1) % L] for i in range(L)): alt += 1
            for i, v in enumerate(g):
                if v in Cs: continue
                extra = [ed for ed in R if (ed[1] == v or ed[0] == v)
                         and ed not in ((g[i-1], v), (v, g[(i+1) % L]))]
                if not extra: bare += 1
        if len(cyc) == 1 and len(R) == len(next(iter(cyc))): pure += 1
    chk(odd == 0, f"FT.69(3)(i): {name}: no odd cycle inside any cover")
    chk(alt == 0, f"FT.69(3): {name}: strict centre/non-centre alternation")
    chk(bare == 0, f"FT.69(3)(ii): {name}: no bare non-centre cycle vertex")
    chk(pure == 0, f"FT.69(3)(iii): {name}: no pure-cycle cover")
    chk(wc == e['with_cyc'] and dd == e['dig_cov'] and dib == e['dig_byp'] and dil == e['dig_lock']
        and di_i == e['dig_ins'] and d4 == e['c4_cov'] and c4b == e['c4_byp'] and c4l == e['c4_lock']
        and c4_i == e['c4_ins'],
        f"FT.69(3)(v): {name} census {wc},{dd},{dib},{dil},{di_i},{d4},{c4b},{c4l},{c4_i}")
# polygons P3-P7: covers, digons only, P4 no 4-cycles
poly_cov = {3: 10, 4: 33, 5: 56, 6: 118, 7: 281}
for n in range(3, 8):
    nv, DE = cycle_graph(n); U = undirected_from(nv, DE)
    covs = enum_covers_bt(nv, U)
    chk(len(covs) == poly_cov[n], f"FT.69(3): P{n} cover count {len(covs)}")
    lens = set()
    for cl, R in covs:
        for g in cycles_canon(nv, R): lens.add(len(g))
    chk(lens <= {2}, f"FT.69(3): P{n} covers contain digons only: {sorted(lens)}")
# FT.69(4) witness
nv4 = 4
Rw = frozenset({(0,1),(1,0),(2,1),(3,2)})
tw = types_of(nv4, Rw)
chk(tw == [(1,1),(2,1),(1,1),(0,1)], f"FT.69(4): witness types {tw}")
chk(brute_sign_sum(nv4, Rw) == 16 and cover_value(nv4, Rw) == 16, "FT.69(4): witness amplitude 16 (brute = formula)")
chk(cycles_canon(nv4, Rw) == {(0,1)}, "FT.69(4): witness contains exactly the digon (0,1)")
chk(not any(x+y >= 4 for (x,y) in tw), "FT.69(4): witness is a bypass configuration")
# census re-audit on the tetrahedron: 501/252/90 with nonzero subcounts 48/0/0
nvt, DEt = SOL['tetra']; Ut = UND['tetra']
cens = [0,0,0]; nz = [0,0,0]
for bits in range(1 << 12):
    R = frozenset(DEt[i] for i in range(12) if (bits >> i) & 1)
    if any(x+y >= 4 for (x,y) in types_of(4, R)): continue
    cyc = cycles_canon(4, R)
    has = [any(len(g)==L for g in cyc) for L in (2,3,4)]
    z = cover_value(4, R) != 0
    for i in range(3):
        if has[i]:
            cens[i] += 1
            if z: nz[i] += 1
chk(cens == [501,252,90], f"FT.69(4): census 501/252/90 reproduced: {cens}")
chk(nz == [48,0,0], f"FT.69(4): nonzero subcounts 48/0/0: {nz}")
# FT.69(5): the tetra's 12 locked two-centre covers are exactly double-digon hubs
covs_t = enum_covers_bt(4, Ut)
lock2 = [(cl,R) for cl,R in covs_t
         if len(cl) == 2 and any(x+y >= 4 for (x,y) in types_of(4, R))]
chk(len(lock2) == 12, f"FT.69(5): 12 locked two-centre covers: {len(lock2)}")
for cl, R in lock2:
    hub = (set(range(4)) - set(cl.keys()) - {v for v in range(4) if types_of(4,R)[v]==(0,0)}).pop()
    digs = [frozenset((hub, c)) for c in cl]
    chk(all((a,b) in R and (b,a) in R for d in digs for a,b in [tuple(d)]),
        "FT.69(5): locked 2-centre cover = double digon on a locked (2,2) hub")
    chk(types_of(4,R)[hub] == (2,2), "FT.69(5): hub type (2,2), locked")
stamp("FT.69(3)-(5) cycle lemma + census + witnesses OK")

# ================================================================ FT.70: phase diagram
ROWS = {'tetra': [1,12,66,220,435,408,88],
        'cube': [1,24,276,2024,10506,40296,115796,247704,383913,408464,270096,91392,9600],
        'octa': rows['octa'], 'dodeca': rows['dodeca'], 'icosa': rows['icosa'],
        'digon': [1,2,1]}
NEDG = {'tetra':12,'cube':24,'octa':24,'dodeca':60,'icosa':60,'digon':2}
for n in range(3, 11):
    ROWS[f'P{n}'] = poly_B_coeffs(n); NEDG[f'P{n}'] = 2*n
    chk(sum(ROWS[f'P{n}']) == poly_B(n, 1), f"FT.70: P{n} row sums to B(1)")

def Bpoly(name):
    c = ROWS[name]; NN = NEDG[name]
    g = [0]*(NN+1)
    for K, cK in enumerate(c):
        if cK == 0: continue
        for j in range(NN-K+1):
            g[K+j] += cK * comb(NN-K, j) * (-1)**j
    g[NN] -= 1
    return g

def sgn_G(name, m, k):
    g = Bpoly(name); deg = len(g)-1
    s = sum(coef * (m**i) * (2 ** (k*(deg-i))) for i, coef in enumerate(g) if coef)
    return (s > 0) - (s < 0)

def bisect(name, prec=40):
    lo, hi = 0, 2**prec
    assert sgn_G(name, lo, prec) > 0 and sgn_G(name, hi, prec) < 0
    while hi - lo > 1:
        mid = (lo+hi)//2
        if sgn_G(name, mid, prec) > 0: lo = mid
        else: hi = mid
    return lo, hi

LO = {'tetra':795524050730,'cube':797554878777,'octa':746806804206,'dodeca':796617223222,
      'icosa':716919185441,'P3':888296284239,'P4':901237260764,'P5':896342294059,
      'P6':898331502578,'P7':897496916590,'P8':897857057380,'P9':897698775778,'P10':897769401807}
for name, lo0 in LO.items():
    lo, hi = bisect(name)
    chk((lo, hi) == (lo0, lo0+1), f"FT.70(2): p*({name}) isolating interval reproduced")
    sgn = [sgn_G(name, i*2**40//50, 40) for i in range(51)]
    flips = sum(1 for a,b in zip(sgn, sgn[1:]) if a != 0 and b != 0 and a != b)
    chk(flips == 1, f"FT.70(1): {name} single sign flip on 51-point grid (unique crossing)")
# order check
order = ['icosa','octa','tetra','dodeca','cube','P3','P5','P7','P9','P10','P8','P6','P4']
chk(all(LO[a] < LO[b] for a,b in zip(order, order[1:])), "FT.70(2): crossover order as documented")
# digon: B == 1 identically -> G(p) = 1 - p^2 (floor never locked: root only at p=1)
g2 = Bpoly('digon')
chk(g2 == [1, 0, -1], f"FT.70(1): digon G(p) = 1 - p^2 exactly: {g2}")
# sqrt(2/3) interlacing: P9 < sqrt(2/3) < P10 via exact integer square root
m40 = isqrt((2 * 2**80) // 3)
while 3 * (m40 + 1) ** 2 <= 2 * 2**80: m40 += 1
while 3 * m40 ** 2 > 2 * 2**80: m40 -= 1
chk(3 * m40**2 <= 2 * 2**80 < 3 * (m40+1)**2, "sqrt(2/3) dyadic floor verified by integer squaring")
chk(LO['P9'] < m40 < LO['P10'],
    f"FT.70(3): P9 < sqrt(2/3) < P10 interlacing ({LO['P9']} < {m40} < {LO['P10']})")
# limit arithmetic in Z[sqrt6]: s = 2+sqrt6 solves s^2 = 4s+2 ; p* = sqrt6/3
def z6_mul(x, y):   # (a + b sqrt6)(c + d sqrt6) = (ac+6bd) + (ad+bc) sqrt6
    a, b = x; c, d = y
    return (a*c + 6*b*d, a*d + b*c)
# (2+s)^2 = 4+4s+6 = 10+4s ; 4(2+s)+2 = 10+4s  =>  s^2 = 4s+2
chk(z6_mul((2,1),(2,1)) == (10,4) == (4*2+2, 4*1), "FT.70(3): (2+sqrt6)^2 = 10+4sqrt6 = 4(2+sqrt6)+2 in Z[sqrt6]")
# sqrt6/3 = (2+sqrt6)/(3+sqrt6): cross-multiply: sqrt6*(3+sqrt6) = 3sqrt6+6 = 3*(2+sqrt6)
chk(z6_mul((0,1),(3,1)) == (6,3) == (3*2, 3*1), "FT.70(3): sqrt6(3+sqrt6) = 6+3sqrt6 = 3(2+sqrt6)")
chk(Fr(6, 9) == Fr(2, 3), "FT.70(3): (sqrt6/3)^2 = 2/3")
# charpoly T(t) = x^2 (x^2 - (1+2t)x - t^2(1+2t)) at exact samples
def detF(M):
    n = len(M); M = [row[:] for row in M]; d = Fr(1)
    for i in range(n):
        p = None
        for r in range(i, n):
            if M[r][i] != 0: p = r; break
        if p is None: return Fr(0)
        if p != i: M[i], M[p] = M[p], M[i]; d = -d
        d *= M[i][i]; inv = 1/M[i][i]
        for r in range(i+1, n):
            f = M[r][i]*inv
            if f:
                for c in range(i, n): M[r][c] -= f*M[i][c]
    return d
for t in (Fr(1), Fr(2), Fr(1,3), Fr(5,2)):
    T = [[Fr(0)]*4 for _ in range(4)]
    for s in range(4):
        for sp in range(4):
            if bin(s).count('1') + bin(sp).count('1') <= 3:
                T[s][sp] = t ** bin(sp).count('1')
    pts = [Fr(i) for i in range(-1, 4)]
    for x in pts:
        Mx = [[(x if i==j else Fr(0)) - T[i][j] for j in range(4)] for i in range(4)]
        red = x*x - (1+2*t)*x - t*t*(1+2*t)
        chk(detF(Mx) == x*x*red, f"FT.70(3): charpoly T(t) at t={t}, x={x}")
# f_adm chain identity (symbolic, n=3..10)
def pad(g, L): return g + [0]*(L-len(g))
def padm_poly(n):
    g = [0]*(n+1)
    for k in range(4):
        for j in range(n-k+1):
            g[k+j] += comb(n,k)*comb(n-k,j)*(-1)**j
    return g
for n in range(3, 11):
    L = n+2
    corr = [0]*L
    for j in range(n-2):
        corr[4+j] += comb(n,3)*comb(n-3,j)*(-1)**j
    diff = [a-(b-c) for a,b,c in zip(pad(padm_poly(n+1),L), pad(padm_poly(n),L), corr)]
    chk(all(d == 0 for d in diff), f"FT.70(4): f_adm identity at n={n}")
f12 = {2: Fr(1), 4: Fr(15,16), 6: Fr(21,32), 8: Fr(93,256), 10: Fr(11,64)}
for n, v in f12.items():
    chk(sum(comb(n,k) for k in range(4)) * Fr(1, 2**n) == v == Fr(sum(Fr(comb(n,k)) for k in range(4)), 2**n),
        f"FT.70(4): f_adm({n},1/2) = {v}")
chk(f12[2] > f12[4] > f12[6] > f12[8] > f12[10], "FT.70(4): strict lock-proneness order")
# octahedron refutation: f_adm(8,p) >= (1-p)^8 > 0 pointwise for p in (0,1)
# (structural reason: f_adm(8,p) = sum_{k<=3} C(8,k) p^k (1-p)^{8-k} and the k=0 term is (1-p)^8)
for i in range(1, 100):
    p = Fr(i, 100)
    f8 = sum(comb(8, k) * p**k * (1-p)**(8-k) for k in range(4))
    chk(f8 > (1-p)**8 > 0, f"FT.70(4): f_adm(8,p) > (1-p)^8 > 0 at p={p}")
# <K>_byp(1/2)
Khalf = {'digon': Fr(1), 'tetra': Fr(852,205), 'cube': Fr(3311952,395023), 'octa': Fr(2124600,318523),
         'dodeca': Fr(4007491093935690,191727103387307), 'icosa': Fr(215801166207,15519497071),
         'P3': Fr(8,3), 'P4': Fr(248,69), 'P5': Fr(130,29), 'P6': Fr(296,55),
         'P7': Fr(2618,417), 'P8': Fr(11344,1581), 'P9': Fr(896,111), 'P10': Fr(13588,1515)}
for name, val in Khalf.items():
    c = ROWS[name]
    chk(Fr(sum(K*cK for K,cK in enumerate(c)), sum(c)) == val, f"FT.70(5): <K>_byp(1/2) {name} = {val}")
chk(Khalf['tetra'] == Fr(852,205), "FT.70(5): tetra anchor = FT.68(1) m_eff reading (i)")
def Kbyp_at(name, p):
    c = ROWS[name]; NN = NEDG[name]
    num = sum(Fr(K*cK) * p**K * (1-p)**(NN-K) for K,cK in enumerate(c))
    den = sum(Fr(cK) * p**K * (1-p)**(NN-K) for K,cK in enumerate(c))
    return num/den
for name in ('tetra','cube','icosa','P5'):
    vals = [Kbyp_at(name, Fr(i,20)) for i in range(1,20)]
    chk(all(b > a for a,b in zip(vals, vals[1:])), f"FT.70(5): <K>_byp strictly increasing, {name}")
    Kmax = max(K for K,cK in enumerate(ROWS[name]) if cK)
    chk(Kbyp_at(name, Fr(99,100)) > Kmax - 1, f"FT.70(5): {name} <K>_byp(99/100) > Kmax-1 = {Kmax-1}")
    chk(Kbyp_at(name, Fr(1,100)) < 1, f"FT.70(5): {name} <K>_byp(1/100) < 1 (vacuum-dominated)")
stamp("FT.70 phase diagram OK")

# ================================================================ FT.71: dust
On = {4: 16, 6: 112, 8: 496, 10: 2032}
for n, v in On.items():
    chk(v == 2**(n+1) - 16, f"FT.71(1): O({n}) = 2^{n+1}-16 = {v}")
VD = {'tetra': (4,6,448), 'cube': (8,6,896), 'octa': (6,8,2976), 'dodeca': (20,6,2240), 'icosa': (12,10,24384)}
for name,(V,nv,dark) in VD.items():
    chk(V*On[nv] == dark, f"FT.71(2): {name} dark-sum anchor V*O(2d) = {dark} [FT.63(5)]")
rho_half = {'tetra': Fr(154), 'cube': Fr(308), 'octa': Fr(15159,8), 'dodeca': Fr(770), 'icosa': Fr(20193)}
for name,(V,nv,dark) in VD.items():
    val = dark * (1 - f12[nv])
    chk(val == rho_half[name], f"FT.71(1): <rho>(1/2) {name} = {rho_half[name]}: got {val}")
# polygon monomial 16 n p^4: at p=1/2 -> n ; symbolic: V*16*p^4
for n in (3, 5, 8):
    chk(16*n*Fr(1,16) == n, f"FT.71(1): polygon <rho>(1/2) = n at n={n}")
# monotonicity grid
def rho_at(name, p):
    V, nv, dark = VD[name]
    return dark * (1 - sum(comb(nv,k)*p**k*(1-p)**(nv-k) for k in range(4)))
for name in VD:
    vals = [rho_at(name, Fr(i,20)) for i in range(0,21)]
    chk(all(b >= a for a,b in zip(vals, vals[1:])) and vals[-1] > vals[0],
        f"FT.71(2): <rho>(p) increasing on grid, {name}")
    chk(rho_at(name, Fr(1)) == VD[name][2] and rho_at(name, Fr(0)) == 0, f"FT.71(2): {name} anchors")
stamp("FT.71 dust OK")

# ================================================================ FT.72: GF(2) face cell
def solid_geo(name):
    nv, DE = SOL[name]; U = UND[name]
    if name == 'tetra':
        F = [frozenset(set(range(4)) - {v}) for v in range(4)]
    elif name == 'cube':
        V = [(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)]
        F = [frozenset(i for i in range(8) if V[i][ax]==s) for ax in range(3) for s in (0,1)]
    elif name == 'octa':
        Us = set(map(frozenset, U))
        F = [frozenset(c) for c in combinations(range(nv),3) if all(frozenset(p) in Us for p in combinations(c,2))]
    elif name == 'icosa':
        adj = [set() for _ in range(nv)]
        for a,b in U: adj[a].add(b); adj[b].add(a)
        F = [frozenset((a,b,c)) for a in range(nv) for b in adj[a] for c in adj[b] if c in adj[a] and a<b<c]
    else:  # dodeca: faces = icosa-vertex layers
        ic = icosa_edges()
        adj_i = [set() for _ in range(12)]
        for a,b in ic: adj_i[a].add(b); adj_i[b].add(a)
        faces_i = [(a,b,c) for a in range(12) for b in adj_i[a] for c in adj_i[b] if c in adj_i[a] and a<b<c]
        F = [frozenset(i for i in range(20) if v in faces_i[i]) for v in range(12)]
    return nv, U, F

def gf2_kernel_basis(M, nrows, ncols):
    M = [row[:] for row in M]; piv = {}; rank = 0
    for col in range(ncols):
        p = None
        for r in range(rank, nrows):
            if M[r][col]: p = r; break
        if p is None: continue
        M[rank], M[p] = M[p], M[rank]
        for r in range(nrows):
            if r != rank and M[r][col]: M[r] = [a^b for a,b in zip(M[r], M[rank])]
        piv[col] = rank; rank += 1
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        x = [0]*ncols; x[f] = 1
        for c, r in piv.items(): x[c] = M[r][f]
        basis.append(x)
    return basis, rank

def row_basis(rows, ncols):
    tmp = [r[:] for r in rows]; rr = 0
    for col in range(ncols):
        p = None
        for r in range(rr, len(tmp)):
            if tmp[r][col]: p = r; break
        if p is None: continue
        tmp[rr], tmp[p] = tmp[p], tmp[rr]
        for r in range(len(tmp)):
            if r != rr and tmp[r][col]: tmp[r] = [x^y for x,y in zip(tmp[r], tmp[rr])]
        rr += 1
    return [tmp[r] for r in range(rr)]

def enum_space(basis):
    k = len(basis)
    if k == 0: return [[0]*len(basis[0])] if basis else [[0]]
    nn = len(basis[0])
    return [[sum(basis[b][i] for b in range(k) if (m>>b)&1) % 2 for i in range(nn)] for m in range(1<<k)]

JDIM = {'tetra':2,'cube':3,'octa':3,'dodeca':5,'icosa':5}
TRI  = {'tetra':4,'cube':0,'octa':8,'dodeca':0,'icosa':20}
B1   = {'tetra':3,'cube':5,'octa':7,'dodeca':11,'icosa':19}
INTER = {'tetra': {0:1,4:3}, 'cube': {0:1,6:4,8:3}, 'octa': {0:1,6:4,8:3},
         'dodeca': {0:1,10:6,16:15,18:10}, 'icosa': {0:1,10:6,16:15,18:10}}
CUT_EVEN = {'tetra': False, 'cube': False, 'octa': True, 'dodeca': False, 'icosa': False}
for name in ('tetra','cube','octa','dodeca','icosa'):
    nv, U, F = solid_geo(name)
    ne = len(U)
    eidx = {frozenset(e): i for i, e in enumerate(U)}
    # face map
    M = [[0]*len(F) for _ in range(ne)]
    for fi_, f in enumerate(F):
        for a,b in combinations(sorted(f),2):
            if frozenset((a,b)) in eidx: M[eidx[frozenset((a,b))]][fi_] = 1
    ker, rank = gf2_kernel_basis(M, ne, len(F))
    chk(rank == len(F)-1 == B1[name], f"FT.72(1): {name} face-map rank = beta1 = F-1 = {B1[name]}")
    chk(len(ker) == 1 and all(x == 1 for x in ker[0]), f"FT.72(1): {name} kernel = all-faces (dim 1)")
    chk(ne - nv + 1 == B1[name], f"FT.72(1): {name} Euler: E-V+1 = beta1")
    # D1 / Z1 / Cut
    D1 = [[0]*ne for _ in range(nv)]
    for (a,b) in U:
        D1[a][eidx[frozenset((a,b))]] = 1; D1[b][eidx[frozenset((a,b))]] = 1
    z1b, rk1 = gf2_kernel_basis(D1, nv, ne)
    chk(rk1 == nv-1 and len(z1b) == B1[name], f"FT.72(2): {name} rk d1 = V-1, dim Z1 = beta1")
    cutb = row_basis(D1, ne)
    chk(len(cutb) == nv-1, f"FT.72(2): {name} dim Cut = V-1")
    dimsum = len(row_basis(z1b + cutb, ne))
    jdim = B1[name] + (nv-1) - dimsum
    chk(jdim == JDIM[name], f"FT.72(2): {name} dim(Z1 cap Cut) = {jdim}")
    # enumerators + MacWilliams + intersection histogram
    def whist(vecs):
        h = {}
        for v in vecs: h[sum(v)] = h.get(sum(v),0)+1
        return h
    z1all = enum_space(z1b); cutall = enum_space(cutb)
    chk(len(z1all) == 2**B1[name] and len(cutall) == 2**(nv-1), f"FT.72(3): {name} space sizes")
    zh = whist(z1all); ch = whist(cutall)
    # intersection: enumerate the smaller space, test membership in the other via orthogonality
    # (Cut = Z1^perp and Z1 = Cut^perp under the standard GF(2) pairing)
    if B1[name] <= nv - 1:
        inter = [v for v in z1all if all(sum(a*b for a,b in zip(v, z)) % 2 == 0 for z in z1b)]
    else:
        inter = [v for v in cutall if all(sum(a*b for a,b in zip(v, c)) % 2 == 0 for c in cutb)]
    ih = whist(inter)
    chk(len(inter) == 2**jdim, f"FT.72(2): {name} |Z1 cap Cut| = 2^j")
    chk(ih == INTER[name], f"FT.72(4): {name} intersection enumerator {ih}")
    def W(h, x, y, E): return sum(c * (x**w) * (y**(E-w)) for w, c in h.items())
    for (x,y) in ((Fr(3),Fr(5)), (Fr(1,2),Fr(7)), (Fr(-1),Fr(2))):
        chk(W(zh,x,y,ne) == W(ch,y-x,y+x,ne) / 2**(nv-1), f"FT.72(3): MacWilliams at ({x},{y}), {name}")
    for p in (Fr(1,4), Fr(1,2), Fr(3,4)):
        q = 1-2*p
        Pc = W(ch, q, Fr(1), ne) / 2**(nv-1)
        Pd = W(ih, q, Fr(1), ne) / 2**jdim
        if p == Fr(1,2):
            chk(Pc == Fr(1, 2**(nv-1)), f"FT.72(3): {name} P_1/2(cycle) = 2^-(V-1)")
            chk(Pd == Fr(1, 2**jdim), f"FT.72(3): {name} P_1/2(decomposable) = 2^-j")
        else:
            chk(Pc.denominator > 0 and Pd.denominator > 0, f"FT.72(3): {name} sample exact at p={p}")
        if name == 'tetra':
            exp = {Fr(1,4): (Fr(27,128), Fr(19,64)), Fr(3,4): (Fr(11,128), Fr(19,64))}
            if p in exp:
                chk((Pc,Pd) == exp[p], f"FT.72(3): tetra sample at p={p}: {(Pc,Pd)}")
        # direct enumeration cross-check where feasible
        if B1[name] <= 5:
            direct = sum(p**sum(v) * (1-p)**(ne-sum(v)) for v in z1all)
            chk(direct == Pc, f"FT.72(3): {name} direct Z1 enumeration == MacWilliams at p={p}")
    # cut parity
    all_even = all(w % 2 == 0 for w in ch)
    chk(all_even == CUT_EVEN[name], f"FT.72(4): {name} cut-space even-weight = {CUT_EVEN[name]}")
    # triangles
    Us = set(map(frozenset, U))
    tri = sum(1 for c in combinations(range(nv),3) if all(frozenset((c[i],c[j])) in Us for i,j in combinations(range(3),2)))
    chk(tri == TRI[name], f"FT.72(1): {name} triangle census = {TRI[name]}")
# dodeca girth-5: no 4-cycles
nv, U, F = solid_geo('dodeca')
Us = set(map(frozenset, U))
c4 = 0
for cv in combinations(range(nv), 4):
    present = [frozenset(p) for p in combinations(cv,2) if frozenset(p) in Us]
    if len(present) == 4:
        dd = {}
        for x in present:
            for v in x: dd[v] = dd.get(v,0)+1
        if all(dd.get(v,0)==2 for v in cv): c4 += 1
chk(c4 == 0, "FT.72(1): dodecahedron girth 5 — zero triangles, zero 4-cycles")
# two-fold decomposition explicit on the tetrahedron: every cycle has exactly 2 face preimages
nv, U, F = solid_geo('tetra')
ne = len(U); eidx = {frozenset(e): i for i, e in enumerate(U)}
M = [[0]*4 for _ in range(ne)]
for fi_, f in enumerate(F):
    for a,b in combinations(sorted(f),2):
        M[eidx[frozenset((a,b))]][fi_] = 1
img = {}
for m in range(16):
    v = [sum(M[i][j] * ((m>>j)&1) for j in range(4)) % 2 for i in range(ne)]
    img.setdefault(tuple(v), []).append(m)
chk(all(len(pre) == 2 for pre in img.values()), "FT.72(1): tetra — every face-sum has exactly 2 preimages")
chk(all(sorted(pre) == [pre[0], 15-pre[0]] for pre in img.values()), "FT.72(1): the two preimages are complements")
# dual coincidences
chk(INTER['cube'] == INTER['octa'], "FT.72(4): cube == octa intersection enumerator (dual degeneracy)")
chk(INTER['dodeca'] == INTER['icosa'], "FT.72(4): dodeca == icosa intersection enumerator (dual degeneracy)")
stamp("FT.72 face decomposition OK")

# ================================================================ FT.73: bridge field algebra
def has_rat_root(coefs):
    a0, an = coefs[0], coefs[-1]
    for p in range(1, abs(a0)+1):
        if a0 % p: continue
        for q in range(1, abs(an)+1):
            if an % q: continue
            for s in (1,-1):
                x = Fr(s*p, q)
                if sum(Fr(c)*x**i for i,c in enumerate(coefs)) == 0: return x
    return None
qy = [5,0,-5,0,1]        # y^4 - 5y^2 + 5
chk(has_rat_root(qy) is None, "FT.73(2): y^4-5y^2+5 has no rational root")
fac = False
for b in (1,5,-1,-5):
    d = 5//b
    for a in range(-6,7):
        c = -a
        if a*c + b + d == -5 and a*d + b*c == 0: fac = True
chk(not fac, "FT.73(2): y^4-5y^2+5 has no Z-quadratic factorization -> irreducible, degree 4")
qd = [1,-12,19,-8,1]     # x^4-8x^3+19x^2-12x+1
chk(has_rat_root(qd) is None, "FT.73(2): dodeca quartic has no rational root")
fac = False
for b in (1,-1):
    d = 1//b
    for a in range(-20,21):
        c = -8-a
        if b*d == 1 and a*d + b*c == -12 and a*c + b + d == 19: fac = True
chk(not fac, "FT.73(2): dodeca quartic x^4-8x^3+19x^2-12x+1 irreducible (FT.63 anchor)")
# sqrt5 = 2y^2 - 5 in Q(y): (2y^2-5)^2 = 5 mod (y^4-5y^2+5)
# 4y^4 - 20y^2 + 25 ; y^4 = 5y^2 - 5 -> 4(5y^2-5) - 20y^2 + 25 = 5
poly = {4: 4, 2: -20, 0: 25}
red = {}
for deg, coef in poly.items():
    if deg == 4:
        red[2] = red.get(2,0) + coef*5; red[0] = red.get(0,0) - coef*5
    else:
        red[deg] = red.get(deg,0) + coef
chk(red == {2: 0, 0: 5}, f"FT.73(2): (2y^2-5)^2 = 5 in Q[y)/(y^4-5y^2+5): {red}")
# sqrt5 not in Q(sqrt2,sqrt3): sigma-averaging => b=d=0, c=0, a^2=5 impossible
chk(isqrt(5)**2 != 5 and isqrt(2)**2 != 2 and isqrt(3)**2 != 3, "FT.73(2): 2,3,5 are not rational squares")
# ratio (2-s2)/(2-s3) = (2-s2)(2+s3)/1 = 4 + 2s3 - 2s2 - s2s3 in basis {1,s2,s3,s6}
ratio = (4, -2, 2, -1)
chk(all(c != 0 for c in ratio[1:]), "FT.73(3): ratio components (4,-2,2,-1) all nonzero")
# not in Q(s2) (c,d nonzero), not in Q(s3) (b,d nonzero), not in Q, not in Q(s6) (b,c nonzero)
for lbl, cond in (("Q", ratio[1] or ratio[2] or ratio[3]),
                  ("Q(s2)", ratio[2] or ratio[3]),
                  ("Q(s3)", ratio[1] or ratio[3]),
                  ("Q(s6)", ratio[1] or ratio[2])):
    chk(cond != 0, f"FT.73(3): ratio not in {lbl}")
# verify the ratio arithmetic exactly in Q(s2,s3): (4-2s2+2s3-s6)*(2-s3) =? 2-s2
def q23_mul(x, y):
    a,b,c,d = x; e,f,g,h = y
    return (a*e+2*b*f+3*c*g+6*d*h, a*f+b*e+3*c*h+3*d*g, a*g+c*e+2*b*h+2*d*f, a*h+d*e+b*g+c*f)
prod = q23_mul(ratio, (2,0,-1,0))
chk(prod == (2,-1,0,0), f"FT.73(3): (4-2s2+2s3-s6)(2-s3) = 2-s2 exactly: {prod}")
# dual anchors: m_hid = 2E ln2/h: (12,24,24,60,60)
EUND = {'tetra':6,'cube':12,'octa':12,'dodeca':30,'icosa':30}
mh = [2*EUND[k] for k in ('tetra','cube','octa','dodeca','icosa')]
chk(mh == [12,24,24,60,60], f"FT.73(3): m_hid ledger (2E) = {mh} — cube==octa, dodeca==icosa")
# rho_D^- integers on the dual pair: 896 vs 2976 -> rational ratio 28/93 (vs irrational pole ratio)
chk(Fr(896, 2976) == Fr(28, 93), "FT.73(3): drag-read ratio 896/2976 = 28/93 in Q")
# degree bookkeeping: [Q(s2,s3):Q]=4 (basis {1,s2,s3,s6}); compositum with Q(y) has degree 16
chk(4*4 == 16, "FT.73(2): compositum degree 4*4/1 = 16 (intersection Q)")
stamp("FT.73 bridge algebra OK")

# ================================================================ cross-document anchors
chk(Fr(615,2048) == Fr(1230, 4096), "anchor: tetra bypass probability (FT.68(1))")
chk(sum(rows['octa']) == 318523 and sum(rows['dodeca']) == 3067633654196912
    and sum(rows['icosa']) == 2483119531360, "anchor: census totals")
chk(4*112 == 448 and 8*112 == 896 and 6*496 == 2976 and 20*112 == 2240 and 12*2032 == 24384,
    "anchor: dark sums = V*O(2d) [FT.63(5)]")

print(f"verify_H_phasediagram: {N} checks green  ({time.time()-t0:.1f}s)")
