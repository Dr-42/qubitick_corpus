#!/usr/bin/env python3
"""
verify_promotion_B_rung.py — exact machine checks for the imported B corollaries

  Cor CT0.6a  (transit-hop register bound):
      registered content vs single-channel supply over a tick window:
      delta_h <= 4*delta_tau;  entropy bound min(delta_h, 4*delta_tau)*ln2;
      sharpness by groups of <= 4 hops at exact capacity (2^4 = 16 = C_cap).

  Cor CT0.11b (directed rung of bidirectional skeletons):
      n(v) = indeg + outdeg = 2*d on exhaustive bidirectional skeletons;
      n(v) >= 2*d in general; d >= 2 => n >= 4 => D_tick >= 32 > 16 => O > 0;
      unoversubscribed <=> n <= 3; mixed skeletons n = 2*b + u.

Pure Python 3 standard library. Exact integer arithmetic only (no floating
point). Deterministic. Exit code 0 = all green; any discrepancy fails loudly.

Graph witnesses are built as explicit edge lists (K4, cube, octahedron,
Petersen, cycles, paths, stars, circulants) — all integer combinatorics.
"""
import itertools
import era_paths
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


# ---------------------------------------------------------------- constants
C_CAP = 16          # CT0.6: dim_R H(C^4) = 16 register directions per crossing
BITS_PER_TICK = 4   # log2(C_CAP), exact: 2**4 == C_CAP


def D_tick(n):      # CT0.5
    return 2 ** (n + 1)


def O_of(n):        # CT0.6
    return max(0, 2 ** (n + 1) - C_CAP)


# ---------------------------------------------------------------- graphs
def cycle(m):
    return [(i, (i + 1) % m) for i in range(m)]


def path(m):        # m vertices
    return [(i, i + 1) for i in range(m - 1)]


def complete(m):
    return [(i, j) for i in range(m) for j in range(i + 1, m)]


def star(leaves):
    return [(0, i) for i in range(1, leaves + 1)]


def cube():
    return [(v, v ^ (1 << b)) for v in range(8) for b in range(3) if v < (v ^ (1 << b))]


def octahedron():   # K_{2,2,2}: 6 vertices in 3 antipodal pairs; all non-antipodal edges
    verts = range(6)
    return [(u, v) for u in verts for v in verts
            if u < v and (u // 2) != (v // 2)]


def petersen():
    # standard construction: outer cycle 0-4, inner star 5-9 (i+5 <-> ((i+2)%5)+5), spokes
    e = [(i, (i + 1) % 5) for i in range(5)]
    e += [(i, i + 5) for i in range(5)]
    e += [(5 + i, 5 + ((i + 2) % 5)) for i in range(5)]
    return sorted({(min(a, b), max(a, b)) for a, b in e})


def circulant(m, offsets):
    e = set()
    for v in range(m):
        for k in offsets:
            w = (v + k) % m
            if w != v:
                e.add((min(v, w), max(v, w)))
    return sorted(e)


def degrees(edges, verts=None):
    if verts is None:
        verts = sorted({v for e in edges for v in e})
    return {v: sum(1 for e in edges if v in e) for v in verts}


def directed_from_bidir(edges):
    d = []
    for (u, v) in edges:
        d.append((u, v))   # out at u, in at v
        d.append((v, u))   # out at v, in at u
    return d


def rung_of(directed, v):
    inn = sum(1 for (a, b) in directed if b == v)
    out = sum(1 for (a, b) in directed if a == v)
    return inn, out, inn + out


# ---------------------------------------------------- §A  CT0.11b: n = 2d
GRAPH_WITNESSES = [
    ("K2", complete(2), 1),
    ("P3", path(3), None),
    ("P4", path(4), None),
    ("C3", cycle(3), 2),
    ("C4", cycle(4), 2),
    ("C5", cycle(5), 2),
    ("C6", cycle(6), 2),
    ("star K1,4", star(4), None),
    ("K4", complete(4), 3),
    ("cube Q3", cube(), 3),
    ("octahedron K2,2,2", octahedron(), 4),
    ("Petersen", petersen(), 3),
    ("circulant C12(1,2,6)", circulant(12, [1, 2, 6]), 5),
    ("K7", complete(7), 6),
]

for name, edges, reg in GRAPH_WITNESSES:
    degs = degrees(edges)
    if reg is not None:
        chk(f"{name}: {reg}-regular", all(d == reg for d in degs.values()), str(degs))
    dir_e = directed_from_bidir(edges)
    ok_n, ok_sat = True, True
    for v in sorted(degs):
        inn, out, n = rung_of(dir_e, v)
        d = degs[v]
        if (inn, out, n) != (d, d, 2 * d):
            ok_n = False
        if d >= 2 and not (n >= 4 and D_tick(n) >= 32 > C_CAP and O_of(n) > 0):
            ok_sat = False
        if d <= 1 and O_of(n) != 0:
            ok_sat = False
    chk(f"{name}: n(v) = indeg+outdeg = 2*d(v) on bidirectional skeleton", ok_n)
    chk(f"{name}: d>=2 <=> saturated (O>0, D_tick>16); d<=1 <=> O=0", ok_sat)

# specific O-values of the graded ladder (CT4.1a(3) arithmetic, derived here)
for d, expected in [(2, 16), (3, 112), (4, 496), (5, 2032), (6, 8176)]:
    chk(f"O(2d) at d={d}: O({2*d}) = 2^{2*d+1}-16 = {expected}", O_of(2 * d) == expected)

# O(n) = 0 exactly on the lock-free family n <= 3
chk("lock-free family: O(n)=0 <=> n<=3 (n=0..16)",
    all((O_of(n) == 0) == (n <= 3) for n in range(17)))
chk("D_tick(n) <= C_cap <=> n <= 3 (n=0..16)",
    all((D_tick(n) <= C_CAP) == (n <= 3) for n in range(17)))

# 2-regular bidirectional cycles: uniform minimal saturation n=4, O(4)=16=C_cap
for m in range(3, 11):
    dir_e = directed_from_bidir(cycle(m))
    ns = {rung_of(dir_e, v)[2] for v in range(m)}
    chk(f"bidirectional cycle C{m}: uniform n=4, O=16=C_cap",
        ns == {4} and O_of(4) == C_CAP)

# mixed skeletons: n = 2*b + u  (b bidirectional channels, u unidirectional edges)
for b in range(4):
    for u in range(4):
        n = 2 * b + u
        # explicit construction: center vertex v with b bidirectional channels
        # to leaves w1..wb plus u unidirectional edges v -> z1..zu
        dir_e = []
        for i in range(b):
            w = ("w", i)
            dir_e.append((("v",), w))
            dir_e.append((w, ("v",)))
        for j in range(u):
            dir_e.append((("v",), ("z", j)))
        inn, out, nn = rung_of(dir_e, ("v",))
        chk(f"mixed skeleton b={b}, u={u}: n = 2b+u = {n}", nn == n)
        chk(f"mixed skeleton b={b}, u={u}: O=0 <=> n<=3", (O_of(nn) == 0) == (n <= 3))

# non-exhaustive inequality: n(v) >= 2*d_S(v) with strict excess possible
k4 = complete(4)
extra = directed_from_bidir(k4) + [(0, 99)]           # one unidirectional dangling edge
inn, out, n0 = rung_of(extra, 0)
chk("non-exhaustive S: n(v) >= 2*d_S(v), strict with dangling edge (n=7, d_S=3)",
    n0 == 7 and n0 > 2 * 3 and O_of(7) == 240)

# ---------------------------------------------------- §B  CT0.6a: delta_h <= 4 delta_tau
chk("capacity identity: 2^4 = 16 = C_cap; 2^5 = 32 > C_cap",
    2 ** BITS_PER_TICK == C_CAP and 2 ** 5 > C_CAP)

ok = True
for dtau in range(1, 9):
    for dh in range(0, 41):
        admissible = dh <= BITS_PER_TICK * dtau
        # equivalence with the alternatives-vs-supply form: 2^dh <= 16^dtau
        if admissible != (2 ** dh <= C_CAP ** dtau):
            ok = False
        # entropy bound in integer (bit) units: E_bits = dh <= min(dh, 4 dtau)
        if min(dh, BITS_PER_TICK * dtau) != (dh if admissible else BITS_PER_TICK * dtau):
            ok = False
        if admissible and min(dh, BITS_PER_TICK * dtau) != dh:
            ok = False
chk("delta_h <= 4*delta_tau  <=>  2^delta_h <= 16^delta_tau  (grid 1..8 x 0..40)", ok)

# sharpness: schedule of groups of <= 4 hops, group count <= delta_tau,
# alternatives per group 2^|group| <= 16 (at capacity when |group| = 4)
ok = True
for dtau in range(1, 7):
    for dh in range(0, 4 * dtau + 1):
        groups = [min(4, dh - 4 * i) for i in range((dh + 3) // 4)]
        if len(groups) > dtau or sum(groups) != dh:
            ok = False
        if any(2 ** gsz > C_CAP for gsz in groups):
            ok = False
        if dh == 4 * dtau and any(gsz != 4 for gsz in groups):
            ok = False   # at the bound every group is exactly at capacity
chk("sharpness: groups of <=4 hops fit delta_tau ticks at <= C_cap alternatives", ok)

# oversubscribed payload: 5 hop-bits in one tick exceeds supply
chk("5 bits/tick: 2^5 = 32 > 16 = C_cap (oversubscribed); 4 bits: exactly at capacity",
    2 ** 5 == 32 > C_CAP and 2 ** 4 == C_CAP)

# ---------------------------------------------------- §C  document integration
b_src = era_paths.read("B_foundation.md")
for tag in ("CT0.6a", "CT0.11b"):
    chk(f"B_foundation.md contains **Cor {tag} (", f"**Cor {tag} (" in b_src)
    blk = b_src.split(f"**Cor {tag} (", 1)[1]
    cut = min([blk.find(m) if blk.find(m) != -1 else len(blk)
               for m in ("\n---", "\n**Phys.**", "\n### ", "\n## ", "\n**Note")])
    body = blk[:cut]
    chk(f"Cor {tag}: has Req (Cor) and Pf (Cor) with terminator",
        "**Req (Cor).**" in body and "**Pf (Cor).**" in body and r"\blacksquare" in body)
    chk(f"Cor {tag}: cites no FT./Def-H. token",
        not re.search(r"FT\.|Def-H\.|P-H\d", body))
chk("B closure exports mention CT0.6(a) and CT0.11b",
    r"\mathrm{CT0.6(a)}" in b_src and r"\mathrm{CT0.11b}" in b_src)

print(f"verify_promotion_B_rung: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
sys.exit(1 if FAIL else 0)
