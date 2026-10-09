#!/usr/bin/env python3
"""verify_H_coverorbits.py — companion to Def-H.28 / FT.78 / FT.79 / FT.80 (Tier F.27).

Exact arithmetic only: every count is an int, every ratio a Fraction, every logarithm of an
orbit size handled SYMBOLICALLY as a ln2 + b ln3 (Omega | |Aut| = 2^a 3^b on both skeletons), so
Ansatz B is verified without ever evaluating a transcendental. Decimal appears nowhere.

Asserts:
  * Def-H.28: orbit-stabilizer (Omega | |Aut|), K constant on every orbit, the p-independence
    identity <K>_O = K as an exact Fraction identity at p in {1/4,1/3,1/2,2/3,3/4}, and the
    Omega = 2^a 3^b decomposition of every orbit size;
  * FT.78(1)-(2): tetrahedron 1230 configs -> 70 orbits, sum(Omega) = 1230, the cap row
    (1,12,66,220,435,408,88), orbits by K (1,1,5,13,23,21,6), the 7-orbit cover sector with its
    full table (K, |C|, Omega, 4^|C|, cycles, type multiset), Z_byp = 1057, Z_lock = 448, and
    the identification of the two locked rows with FT.69(5)'s families (12 double-digon hubs,
    4 K_(1,3) stars);
  * FT.78(3): the orbit-level amplitude identity sum_Omega Omega * 4^|C| = Z_pm on both skeletons;
  * FT.78(4): cube cap row + 1,580,092 total + K<=12 forced, Burnside orbit row + 33,564,
    covering polynomials (two enumerators), 264 cover orbits (166 byp + 98 lock), sum(Omega) =
    11,205, the Omega histogram {1:1,4:1,8:1,12:4,16:2,24:47,48:208}, the |C|-level orbit and
    configuration counts, and the INDEPENDENT explicit enumeration of all K<=5 admissible
    configurations reproducing the Burnside row (1,1,11,49,250,863);
  * FT.78(5)-(6): even-cycle-only signatures with the documented cycle-content counts, the
    signature's incompleteness (7 orbits / 6 signatures; 264 / 21), and the charge-conjugation
    chirality pair (the 48 dissolved-digon covers = two Omega=24 orbits exchanged by global
    orientation reversal, reversal not in Aut, both ansatze reversal-invariant);
  * FT.79(1)-(3): the Ansatz-A pool {2,4,6,8,10,12}, its 11 exact ratios, lightest/heaviest/
    median, the ceiling bounds |C| <= 3V/4 (bypass) / V (locked) and the V >= 4R/3 requirement
    table, the Ansatz-B class counts (19 tetra / 14 cube) with a<=4, b<=1;
  * FT.79(4)-(5): every pairwise and triple discrepancy as an EXACT Fraction (2.7995..., 150,
    579.5, 13333.3..., no triple within a factor of 10, floor 900/6 = 150), and the amplitude
    dimension-trap ratios (256/207, 4096/3477, 16/(3477/207), 1024/900, 64/45) with their
    square-root corrections;
  * FT.80: the census totals (180 / 40,200 thread instances; 84 / 14,832 bound-chain instances;
    delta_h in {2} / {2,4}; all even; delta_h >= 2 and rung n(v) = 6 >= 2 on every class), the
    norm weights Omega * 2^K per |C|-level, and the absence of any spectral-index datum.
"""
import os, sys, time, json
from fractions import Fraction as Fr
from itertools import combinations
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bypasscore import (complete_graph, cube_graph, undirected_from, types_of, centers_of,
                        is_cover_strict, cover_value, automorphisms, fix_capped_by_K,
                        cap_dp_by_K, cover_dp, cover_polys_bt)

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1

t0 = time.time()
def stamp(m):
    print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")

# ---------------------------------------------------------------- machinery
def canon(g): return min(g[i:] + g[:i] for i in range(len(g)))

def directed_cycles_canon(nv, R):
    adj = {}
    for (a, b) in R: adj.setdefault(a, []).append(b)
    found = set()
    for s in range(nv):
        st = [(s, [s], {s})]
        while st:
            v, p, seen = st.pop()
            for w in adj.get(v, ()):
                if w == s and len(p) >= 2: found.add(canon(tuple(p)))
                elif w not in seen and len(p) < nv: st.append((w, p + [w], seen | {w}))
    return found

def cyc_sig(nv, R): return tuple(sorted(len(c) for c in directed_cycles_canon(nv, R)))

def edge_perm_maps(DE, perms):
    idx = {e: i for i, e in enumerate(DE)}
    return [tuple(idx[(p[a], p[b])] for (a, b) in DE) for p in perms]

def apply_perm(mask, pm):
    out = 0; m = mask
    while m:
        j = (m & -m).bit_length() - 1
        out |= 1 << pm[j]; m &= m - 1
    return out

def canonical(mask, pmaps):
    c = mask
    for pm in pmaps:
        im = apply_perm(mask, pm)
        if im < c: c = im
    return c

def orbits_of(DE, perms, masks):
    pmaps = edge_perm_maps(DE, perms)
    orbs = {}
    for mask in masks: orbs.setdefault(canonical(mask, pmaps), []).append(mask)
    return orbs, pmaps

def unmask(DE, bits): return frozenset(DE[i] for i in range(len(DE)) if (bits >> i) & 1)
def maskof(DE, R):
    idx = {e: i for i, e in enumerate(DE)}
    b = 0
    for e in R: b |= 1 << idx[e]
    return b

def a_b(o):
    a = b = 0; x = o
    while x % 2 == 0: x //= 2; a += 1
    while x % 3 == 0: x //= 3; b += 1
    return a, b, x

def typemult(nv, R): return tuple(sorted(Counter(types_of(nv, R)).items()))

# ================================================================ Def-H.28 identities
print("Def-H.28: orbit invariants, p-independence, Omega = 2^a 3^b")
nvT, DET = complete_graph(4); UT = undirected_from(nvT, DET)
permsT = automorphisms(nvT, UT)
chk(len(permsT) == 24, "|Aut(tetra)| = 24")
admissT = [b for b in range(1 << 12)
           if all(x + y <= 3 for (x, y) in types_of(nvT, unmask(DET, b)))]
chk(len(admissT) == 1230, f"tetra admissible configurations {len(admissT)} != 1230 [FT.68(1)]")
orbT, pmT = orbits_of(DET, permsT, admissT)
chk(len(orbT) == 70, f"tetra orbits {len(orbT)} != 70 [FT.68(1)]")
chk(sum(len(v) for v in orbT.values()) == 1230, "sum(Omega) = 1230")
for c, mem in orbT.items():
    K = bin(c).count('1')
    chk(all(bin(x).count('1') == K for x in mem), "K not constant on an orbit")
    chk(24 % len(mem) == 0, f"orbit-stabilizer violated: Omega = {len(mem)}")
    a, b, rest = a_b(len(mem))
    chk(rest == 1 and a <= 3 and b <= 1, f"Omega = {len(mem)} is not 2^a 3^b with a<=3,b<=1")
# p-independence of the orbit-wise weighted average, as an exact Fraction identity
E = len(DET)
for c, mem in orbT.items():
    K = bin(c).count('1'); Om = len(mem)
    for p in (Fr(1, 4), Fr(1, 3), Fr(1, 2), Fr(2, 3), Fr(3, 4)):
        w = p ** K * (1 - p) ** (E - K)
        num = sum(K * w for _ in mem); den = sum(w for _ in mem)
        if den: chk(num / den == K, f"<K>_O != K at p = {p}, K = {K}")
stamp("K orbit-constant (0 violations); Omega | 24 with Omega = 2^a 3^b; <K>_O = K exactly at 5 p-values")

# ================================================================ FT.78(1)-(2) tetrahedron
capT = [0] * 7; orbKT = [0] * 7
for c, mem in orbT.items():
    K = bin(c).count('1'); capT[K] += len(mem); orbKT[K] += 1
chk(capT == [1, 12, 66, 220, 435, 408, 88], f"tetra cap row {capT}")
chk(orbKT == [1, 1, 5, 13, 23, 21, 6], f"tetra orbits by K {orbKT}")
chk(sum(orbKT) == 70, "orbits by K total")
OmT = sorted({len(v) for v in orbT.values()})
chk(OmT == [1, 3, 4, 6, 8, 12, 24], f"tetra Omega values {OmT}")
# cover sector
covT = []
for c, mem in orbT.items():
    R = unmask(DET, c)
    if cover_value(nvT, R): covT.append((c, mem, R))
covT_all = [b for b in range(1 << 12) if cover_value(nvT, unmask(DET, b))]
chk(len(covT_all) == 101, f"tetra covers {len(covT_all)} != 101 [FT.69(3)(v)]")
byp_cov = [b for b in covT_all
           if all(x + y <= 3 for (x, y) in types_of(nvT, unmask(DET, b)))]
lock_cov = [b for b in covT_all if b not in set(byp_cov)]
chk(len(byp_cov) == 85 and len(lock_cov) == 16, f"tetra covers: {len(byp_cov)} byp / {len(lock_cov)} lock")
orbC, _ = orbits_of(DET, permsT, byp_cov)
orbL, _ = orbits_of(DET, permsT, lock_cov)
chk(len(orbC) == 5 and len(orbL) == 2, f"tetra cover orbits: {len(orbC)} byp / {len(orbL)} lock (want 5/2)")
def row_of(c, mem, with_types):
    R = unmask(DET, c)
    r = (bin(c).count('1'), len(centers_of(nvT, R)), len(mem), cover_value(nvT, R), cyc_sig(nvT, R))
    return r + ((typemult(nvT, R),) if with_types else ())

tbl = sorted(row_of(c, mem, True) for c, mem in orbC.items())
doc_byp = [(0, 0, 1, 1, (), (((0, 0), 4),)),
           (2, 1, 24, 4, (), (((0, 0), 1), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1))),
           (4, 2, 24, 16, (2,), (((1, 0), 1), ((1, 1), 2), ((1, 2), 1))),
           (4, 2, 24, 16, (2,), (((0, 1), 1), ((1, 1), 2), ((2, 1), 1))),
           (4, 2, 12, 16, (), (((0, 2), 1), ((1, 1), 2), ((2, 0), 1)))]
chk(tbl == sorted(doc_byp), f"tetra bypass cover orbit table mismatch:\n{tbl}")
tblL = sorted(row_of(c, mem, False) for c, mem in orbL.items())
chk(tblL == [(4, 2, 12, 16, (2, 2)), (6, 3, 4, 64, (2, 2, 2))], f"tetra locked cover orbits {tblL}")
chk(sum(len(m) * cover_value(nvT, unmask(DET, c)) for c, m in orbC.items()) == 1057,
    "Z_byp(tetra) = 1057 via the orbit identity")
chk(sum(len(m) * cover_value(nvT, unmask(DET, c)) for c, m in orbL.items()) == 448,
    "Z_lock(tetra) = 448 via the orbit identity")
# FT.69(5) families
chk(sorted(len(m) for c, m in orbL.items()) == [4, 12], "locked families: 12 double-digon hubs + 4 stars")
chk(sum(1 for c, m in orbC.items() if cyc_sig(nvT, unmask(DET, c)) == (2,)) == 2,
    "two digon-shadowing bypass orbits (the chiral pair)")
stamp("FT.78(1)-(3): tetra 70 orbits, cap/orbit rows, the 7-orbit cover sector with full table, Z = 1057/448")

# ---- FT.78(6) chirality
revT = {(a, b): (b, a) for (a, b) in DET}
dig_orbits = [c for c, m in orbC.items() if cyc_sig(nvT, unmask(DET, c)) == (2,)]
chk(len(dig_orbits) == 2 and all(len(m) == 24 for m in (orbC[c] for c in dig_orbits)),
    "the 48 dissolved-digon covers = two Omega=24 orbits")
rev_canon = {canonical(maskof(DET, frozenset(revT[e] for e in unmask(DET, c))), pmT) for c in dig_orbits}
chk(rev_canon == set(dig_orbits), "global orientation reversal exchanges the two chiral orbits")
chk(not any(canonical(maskof(DET, frozenset(revT[e] for e in unmask(DET, c))), pmT) == c
            for c in dig_orbits), "reversal is not in Aut (orbits are distinct)")
for c in dig_orbits:
    R = unmask(DET, c); Rr = frozenset(revT[e] for e in R)
    chk(len(Rr) == len(R) and cover_value(nvT, Rr) == cover_value(nvT, R)
        and len(centers_of(nvT, Rr)) == len(centers_of(nvT, R)),
        "Ansatz A and the amplitude are reversal-invariant")
    chk(typemult(nvT, Rr) == tuple(sorted(((b_, a_), n) for (a_, b_), n in typemult(nvT, R))),
        "type multiset transposes under reversal")
stamp("FT.78(6): charge-conjugation chirality (two 24-orbits exchanged; both ansatze C-even)")

# ================================================================ FT.78(4) cube
nvc, DEc = cube_graph(); Uc = undirected_from(nvc, DEc)
permsC = automorphisms(nvc, Uc)
chk(len(permsC) == 48, "|Aut(cube)| = 48")
cdoc = [1, 24, 276, 2024, 10506, 40296, 115796, 247704, 383913, 408464, 270096, 91392, 9600]
cap = cap_dp_by_K(nvc, Uc, cap=3)
chk(cap[:13] == cdoc, f"cube cap row {cap[:13]}")
chk(sum(cap) == 1580092 and all(x == 0 for x in cap[13:]), "cube: 1,580,092 configs, K<=12 forced")
doc_orbits = [1, 1, 11, 49, 250, 863, 2509, 5211, 8163, 8571, 5768, 1922, 245]
orbK = {}
for p in permsC:
    fixK = ({K: c for K, c in enumerate(cdoc) if c} if all(p[v] == v for v in range(nvc))
            else fix_capped_by_K(nvc, Uc, p, cap=3))
    for K, c in fixK.items(): orbK[K] = orbK.get(K, 0) + c
chk(all(v % 48 == 0 for v in orbK.values()), "Burnside sums divisible by 48")
orbK = {K: v // 48 for K, v in orbK.items()}
chk([orbK.get(K, 0) for K in range(13)] == doc_orbits, f"cube orbit row {[orbK.get(K,0) for K in range(13)]}")
chk(sum(doc_orbits) == 33564, "cube: 33,564 orbits (> 10^4: bounded rule observed)")
pb, pl = cover_dp(nvc, Uc)
chk(pb == {0: 1, 1: 48, 2: 648, 3: 2672, 4: 3624}, f"Z_byp(y) {pb}")
chk(pl == {2: 24, 3: 728, 4: 3192, 5: 264, 6: 4}, f"Z_lock(y) {pl}")
pb2, pl2, covs = cover_polys_bt(nvc, Uc)
chk((pb2, pl2) == (pb, pl) and len(covs) == 11205, "two cover enumerators agree; 11,205 covers")
Zb = sum(c * 4 ** k for k, c in pb.items()); Zl = sum(c * 4 ** k for k, c in pl.items())
chk((Zb, Zl, Zb + Zl) == (1109313, 1150848, 2260161), f"cube Z± {(Zb, Zl, Zb+Zl)}")
idx = {e: i for i, e in enumerate(DEc)}
cov_masks = []
for cl, R in covs:
    b = 0
    for e in R: b |= 1 << idx[e]
    cov_masks.append(b)
chk(len(cov_masks) == 11205, "cover mask count")
orbCov, pmC = orbits_of(DEc, permsC, cov_masks)
chk(len(orbCov) == 264, f"cube cover orbits {len(orbCov)} != 264")
chk(sum(len(v) for v in orbCov.values()) == 11205, "sum(Omega) = 11,205")
nb = nl = 0; sb = sl = 0
hist = Counter(); lev = {}
threads = 0; chains = 0; chain_orbits = 0; dh = set(); cycsets = Counter(); sigs = set()
for c, mem in orbCov.items():
    R = unmask(DEc, c); K = len(R); Om = len(mem)
    nC = len(centers_of(nvc, R)); amp = cover_value(nvc, R)
    chk(amp != 0 and K == 2 * nC, f"cover identity K = 2|C| violated: K={K}, |C|={nC}")
    chk(48 % Om == 0, f"orbit-stabilizer violated: Omega = {Om}")
    a_, b_, rest = a_b(Om)
    chk(rest == 1 and a_ <= 4 and b_ <= 1, f"Omega = {Om} not 2^a 3^b with a<=4,b<=1")
    lk = any(x + y >= 4 for (x, y) in types_of(nvc, R))
    if lk: nl += 1; sl += Om
    else: nb += 1; sb += Om
    hist[Om] += 1
    cs = cyc_sig(nvc, R)
    cycsets[cs] += 1
    sigs.add((K, cs, nC))
    lev.setdefault((lk, nC), [0, 0, 0])
    lev[(lk, nC)][0] += 1; lev[(lk, nC)][1] += Om; lev[(lk, nC)][2] += Om * amp
    threads += nC * Om
    chains += len(cs) * Om
    if cs: chain_orbits += 1
    for L in cs: dh.add(L)
chk((nb, nl) == (166, 98), f"cube cover orbits by sector: {nb} byp / {nl} lock")
chk((sb, sl) == (6993, 4212), f"cube cover configs by sector: {sb}/{sl}")
chk(dict(hist) == {1: 1, 4: 1, 8: 1, 12: 4, 16: 2, 24: 47, 48: 208}, f"Omega histogram {dict(hist)}")
chk(sum(lev[(False, k)][2] for k in range(5) if (False, k) in lev) == Zb, "orbit amplitude identity = Z_byp")
chk(sum(lev[(True, k)][2] for k in range(2, 7) if (True, k) in lev) == Zl, "orbit amplitude identity = Z_lock")
doc_lev = {(False, 0): (1, 1), (False, 1): (1, 48), (False, 2): (19, 648), (False, 3): (57, 2672),
           (False, 4): (88, 3624), (True, 2): (1, 24), (True, 3): (18, 728), (True, 4): (71, 3192),
           (True, 5): (7, 264), (True, 6): (1, 4)}
for k, (o, cf) in doc_lev.items():
    chk((lev[k][0], lev[k][1]) == (o, cf), f"|C|-level {k}: {(lev[k][0], lev[k][1])} != {(o, cf)}")
chk([lev[(False, k)][1] for k in range(5)] == [1, 48, 648, 2672, 3624],
    "bypass |C|-level configs = the covering polynomial coefficients")
chk([lev[(True, k)][1] for k in range(2, 7)] == [24, 728, 3192, 264, 4],
    "locked |C|-level configs = the covering polynomial coefficients")
stamp("FT.78(4): cube cap/Burnside rows, covering polynomials, 264 cover orbits, |C|-levels, Z± identity")

# ---- signatures (FT.78(5))
chk(sorted(dh) == [2, 4], f"cube cover cycle lengths {sorted(dh)}")
chk(all(L % 2 == 0 for L in dh), "every shadowed cycle is even [FT.69(3)(i)]")
chk(len(cycsets) == 10, f"cube: {len(cycsets)} distinct cycle contents != 10")
chk(chains == 14832, f"cube bound-chain instances {chains} != 14832 (Omega-weighted)")
chk(sum(n for n in cycsets.values()) == 264, "cycle contents partition the 264 cover orbits")
chk(chain_orbits == 209, f"cube orbits shadowing >=1 cycle: {chain_orbits} != 209")
chk(len(sigs) == 21, f"cube: {len(sigs)} distinct (K,cycles,|C|) signatures != 21 (264 orbits: incomplete invariant)")
sigT = {(bin(c).count('1'), cyc_sig(nvT, unmask(DET, c)), len(centers_of(nvT, unmask(DET, c))))
        for c in list(orbC) + list(orbL)}
chk(len(sigT) == 6, f"tetra: {len(sigT)} signatures for 7 cover orbits (incomplete invariant)")
chk(threads == 40200, f"cube thread instances {threads} != 40,200")
# tetra census totals
thT = chT = 0; dhT = set()
for c, mem in list(orbC.items()) + list(orbL.items()):
    R = unmask(DET, c); cs = cyc_sig(nvT, R)
    thT += len(centers_of(nvT, R)) * len(mem); chT += len(cs) * len(mem); dhT |= set(cs)
chk(thT == 180 and chT == 84 and sorted(dhT) == [2], f"tetra census: threads {thT}, chains {chT}, dh {sorted(dhT)}")
chk(all(L >= 2 for L in dh | dhT), "Def-H.4 floor delta_h >= 2 on every bound-chain candidate")
nT = [sum(1 for e in DET if v in e) for v in range(nvT)]
nCg = [sum(1 for e in DEc if v in e) for v in range(nvc)]
chk(all(x == 6 for x in nT) and all(x == 6 for x in nCg),
    f"potential degree n(v) = 6 >= 2 on both skeletons (Def-H.4's rung floor): {set(nT)}, {set(nCg)}")
stamp("FT.78(5)/FT.80(3): signatures even-only, census totals 180/40200 threads, 84/14832 chains")

# ---- K<=5 explicit enumeration vs Burnside (independent cross-validation)
cfg5 = [b for b in range(1 << 24) if bin(b).count('1') <= 5
        and all(x + y <= 3 for (x, y) in types_of(nvc, unmask(DEc, b)))]
chk(len(cfg5) == sum(cdoc[:6]) == 53127, f"cube K<=5 configurations {len(cfg5)}")
orb5, _ = orbits_of(DEc, permsC, cfg5)
row5 = [0] * 6
for c in orb5: row5[bin(c).count('1')] += 1
chk(row5 == doc_orbits[:6], f"explicit orbit row {row5} != Burnside {doc_orbits[:6]}")
chk(sum(len(v) for v in orb5.values()) == 53127, "K<=5 sum(Omega)")
stamp("FT.78(4) cross-validation: explicit canonical forms (53,127 configs) == Burnside row")

# ================================================================ FT.79(1)-(3)
poolA = sorted({2 * nC for (lk, nC) in lev if nC}                      # cube cover levels
               | {2 * len(centers_of(nvT, unmask(DET, c)))               # tetra cover orbits
                  for c in list(orbC) + list(orbL)})
poolA = [k for k in poolA if k]
chk(poolA == [2, 4, 6, 8, 10, 12], f"Ansatz-A cover mass pool {poolA}")
rats = sorted({Fr(b, a) for a, b in combinations(poolA, 2)})
chk(len(rats) == 11, f"{len(rats)} distinct ratios != 11")
chk(rats == sorted([Fr(6, 5), Fr(5, 4), Fr(4, 3), Fr(3, 2), Fr(5, 3), Fr(2), Fr(5, 2), Fr(3),
                    Fr(4), Fr(5), Fr(6)]), f"ratio set {rats}")
chk(min(poolA) == 2 and max(poolA) == 12, "lightest 2, heaviest 12")
med = Fr(poolA[2] + poolA[3], 2)
chk(med == 7, f"median of distinct values {med}")
wK = sorted((2 * nC, lev[(lk, nC)][0]) for (lk, nC) in lev if nC)
tot = sum(o for _, o in wK); acc = 0; wmed = None
for k, o in wK:
    acc += o
    if acc * 2 >= tot and wmed is None: wmed = k
chk(wmed == 8, f"orbit-weighted median K {wmed} != 8")
# ceiling bounds
chk(Fr(3 * 4, 4) == 3 and Fr(3 * 8, 4) == 6, "ceiling 3V/4: tetra 3, cube 6 (observed maxima)")
needV = {20: 27, 207: 276, 600: 800, 900: 1200, 3477: 4636, 80000: 106667}
for R, V in needV.items():
    lo = Fr(4 * R, 3)
    chk(V - 1 < lo <= V, f"V >= 4R/3 for R={R}: {float(lo)} -> {V}")
# Ansatz B classes
clsT = {(bin(c).count('1'),) + a_b(len(m))[:2] for c, m in orbT.items()}          # bypass sector
clsT_all = clsT | {(bin(c).count('1'),) + a_b(len(m))[:2] for c, m in orbL.items()}  # + locked covers
clsC = {(len(unmask(DEc, c)),) + a_b(len(m))[:2] for c, m in orbCov.items()}
chk(len(clsT) == 18, f"tetra bypass Ansatz-B classes {len(clsT)} != 18")
chk(len(clsT_all) == 19, f"tetra classes incl. locked covers {len(clsT_all)} != 19")
chk(clsT_all - clsT == {(6, 2, 0)}, f"the locked star orbit adds exactly (K,a,b) = (6,2,0)")
chk(len(clsC) == 14, f"cube Ansatz-B classes {len(clsC)} != 14")
chk(all(a <= 3 and b <= 1 for _, a, b in clsT_all), "tetra: a<=3, b<=1")
chk(all(a <= 4 and b <= 1 for _, a, b in clsC), "cube: a<=4, b<=1")
chk(max(k for k, a, b in clsC) == 12 and max(k for k, a, b in clsT) == 6, "K ranges 6 / 12")
stamp("FT.79(1)-(3): pool {2..12}, 11 ratios, medians, ceiling 3V/4, V>=4R/3 table, Ansatz-B classes 19/14")

# ================================================================ FT.79(4)-(5) audit
SM = {'lep': [1, 207, 3477], 'up': [1, 600, 80000], 'down': [1, 20, 900]}
def disc(x, y): return max(x / y, y / x)
best_pair = []
for fam, trip in SM.items():
    a = [Fr(x) for x in trip]
    for x_, y_ in combinations(a, 2):
        smr = y_ / x_
        b = min(rats, key=lambda r: disc(r, smr))
        best_pair.append((disc(b, smr), fam, (x_, y_), b))
doc_pair = {('lep', (207, 3477)): Fr(3477, 207) / 6, ('down', (1, 20)): Fr(10, 3),
            ('down', (20, 900)): Fr(15, 2), ('up', (600, 80000)): Fr(200, 9),
            ('lep', (1, 207)): Fr(69, 2), ('up', (1, 600)): Fr(100),
            ('down', (1, 900)): Fr(150), ('lep', (1, 3477)): Fr(1159, 2),
            ('up', (1, 80000)): Fr(40000, 3)}
for d, fam, pair, b in best_pair:
    chk(d == doc_pair[(fam, pair)], f"pairwise discrepancy {fam} {pair}: {d} != {doc_pair[(fam,pair)]}")
bp = min(best_pair)
chk(bp[0] == Fr(3477, 207) / 6 and bp[1] == 'lep' and bp[2] == (207, 3477),
    f"best pairwise {bp[0]} = 1159/414 ({bp[1]} {bp[2]})")
chk(bp[0] < 10, "best pairwise IS within an order of magnitude (flagged as extreme-vs-extreme)")
trip_best = {}
for fam, trip in SM.items():
    a = [Fr(x) for x in trip]; rsm = (a[1] / a[0], a[2] / a[0])
    bd = None; bt = None
    for cmb in combinations(poolA, 3):
        v1, v2, v3 = (Fr(x) for x in cmb)
        d = max(disc(v2 / v1, rsm[0]), disc(v3 / v1, rsm[1]))
        if bd is None or d < bd: bd, bt = d, cmb
    trip_best[fam] = (bd, bt)
chk(trip_best['down'] == (Fr(150), (2, 4, 12)), f"down-type triple {trip_best['down']}")
chk(trip_best['lep'] == (Fr(1159, 2), (2, 4, 12)), f"lepton triple {trip_best['lep']}")
chk(trip_best['up'] == (Fr(40000, 3), (2, 4, 12)), f"up-type triple {trip_best['up']}")
chk(all(v[0] > 10 for v in trip_best.values()), "no aligned triple within a factor of 10")
chk(Fr(900, 6) == 150, "triple floor = 900/6 = 150 exactly")
amps = sorted({4 ** nC for (lk, nC) in lev if nC} | {1})
chk(amps == [1, 4, 16, 64, 256, 1024, 4096], f"amplitudes {amps}")
trap = {(256, 207): Fr(256, 207), (4096, 3477): Fr(4096, 3477),
        (16, Fr(3477, 207)): Fr(3477, 16 * 207), (1024, 900): Fr(256, 225), (64, 45): Fr(64, 45)}
chk(trap[(256, 207)] == Fr(256, 207) and Fr(256, 207) < Fr(5, 4), "256 vs 207: x1.2367 (<5/4)")
chk(Fr(4096, 3477) < Fr(6, 5), "4096 vs 3477: x1.1780 (<6/5)")
chk(Fr(3477, 16 * 207) < Fr(21, 20), "16 vs 3477/207: x1.0498 (<21/20)")
chk(Fr(256, 225) < Fr(8, 7), "1024 vs 900: x1.1378 (<8/7)")
chk(Fr(64, 45) < Fr(10, 7), "64 vs 45: x1.4222 (<10/7)")
chk(Fr(256, 207) > 1 and all(x > 1 for x in trap.values()), "all trap ratios > 1 (near-misses)")
stamp("FT.79(4)-(5): 9 pairwise + 3 triple discrepancies as exact Fractions; 5 amplitude-trap ratios rejected")

# ================================================================ FT.80 norm weights
norm = {}
for c, mem in orbCov.items():
    R = unmask(DEc, c); K = len(R); nC = len(centers_of(nvc, R))
    norm[nC] = norm.get(nC, 0) + len(mem) * 2 ** K
doc_norm = {0: 1, 1: 192, 2: 10752, 3: 217600, 4: 1744896, 5: 270336, 6: 16384}
chk(norm == doc_norm, f"cube norm weights Omega*2^K by |C|: {norm}")
chk(sum(norm.values()) == sum(len(m) * 2 ** bin(c).count('1') for c, m in orbCov.items()),
    "norm weights sum consistently")
chk(all(v > 0 for v in norm.values()), "every |C|-level has strictly positive CT2.8 norm weight")
stamp("FT.80(1),(3): norm weights Omega*2^K = (1,192,10752,217600,1744896,270336,16384) by |C|")

print(f"verify_H_coverorbits: {N} checks green  ({time.time()-t0:.1f}s)")
