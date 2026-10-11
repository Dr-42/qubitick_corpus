#!/usr/bin/env python3
"""
verify_promotion_G_saturation.py — exact machine checks for the imported G
corollary.

  Cor CT4.1a (universal saturation of bidirectional real-edge subgraphs):
      (1) d >= 2  =>  n = 2d >= 4  =>  O(n) > 0  (falls to the dark sector);
      (2) 2-regular bidirectional skeletons: uniform n = 4, O(4) = 16 = C_cap
          (exactly one channel quantum over budget, independent of length);
      (3) d-regular: graded oversubscription O(2d) = 2^(2d+1) - 16 with the
          documented values 16, 112, 496, 2032, 8176 at d = 2..6;
      (4) unoversubscribed family exactly n <= 3; mixed skeletons n = 2b + u.

Pure Python 3 standard library. Exact integer arithmetic only (no floating
point). Deterministic. Exit code 0 = all green.
"""
import os
import era_paths
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


C_CAP = 16


def O_of(n):        # CT0.6
    return max(0, 2 ** (n + 1) - C_CAP)


def D_tick(n):      # CT0.5
    return 2 ** (n + 1)


def cycle(m):
    return [(i, (i + 1) % m) for i in range(m)]


def circulant(m, offs):
    e = set()
    for v in range(m):
        for k in offs:
            w = (v + k) % m
            if w != v:
                e.add((min(v, w), max(v, w)))
    return sorted(e)


def degrees(edges):
    vs = sorted({v for e in edges for v in e})
    return {v: sum(1 for e in edges if v in e) for v in vs}


def directed(edges):
    d = []
    for (u, v) in edges:
        d += [(u, v), (v, u)]
    return d


def rung(directed_edges, v):
    return (sum(1 for (a, b) in directed_edges if b == v)
            + sum(1 for (a, b) in directed_edges if a == v))


# ------------------------------------------- (2) uniform minimal saturation
for m in range(3, 13):
    de = directed(cycle(m))
    ns = sorted({rung(de, v) for v in range(m)})
    chk(f"bidirectional cycle C{m}: every vertex n=4 (type (2,2)), O(4)=16=C_cap",
        ns == [4] and O_of(4) == 16 == C_CAP)

# ------------------------------------------- (3) graded ladder O(2d)
LADDER = {2: 16, 3: 112, 4: 496, 5: 2032, 6: 8176}
for d, val in LADDER.items():
    chk(f"graded ladder: O(2*{d}) = 2^{2*d+1}-16 = {val}", O_of(2 * d) == val)
# d-regular witnesses for each grade
REG_WITNESSES = [
    (2, cycle(5)),
    (3, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),               # K4
    (4, circulant(6, [1, 2])),                                            # octahedron K2,2,2
    (5, circulant(12, [1, 2, 6])),                                        # 5-regular
    (6, [(i, j) for i in range(7) for j in range(i + 1, 7)]),             # K7
]
for d, edges in REG_WITNESSES:
    degs = degrees(edges)
    de = directed(edges)
    ok = all(dg == d for dg in degs.values())
    ok = ok and all(rung(de, v) == 2 * d and O_of(2 * d) == LADDER[d] for v in degs)
    chk(f"{d}-regular witness: n = 2d = {2*d}, O = {LADDER[d]} at every vertex", ok)

# ------------------------------------------- (1) universality
chk("d>=2 => n>=4 => D_tick>=32>16 => O>0 (d = 2..10)",
    all(2 * d >= 4 and D_tick(2 * d) >= 32 > C_CAP and O_of(2 * d) > 0
        for d in range(2, 11)))
chk("O strictly increasing on the saturated ladder n >= 4 (n = 4..20)",
    all(O_of(n + 1) > O_of(n) for n in range(4, 20)))

# ------------------------------------------- (4) lock-free family n <= 3
chk("unoversubscribed <=> n <= 3 <=> D_tick <= C_cap (n = 0..16)",
    all((O_of(n) == 0) == (n <= 3) == (D_tick(n) <= C_CAP) for n in range(17)))
# mixed skeletons: b bidirectional channels + u unidirectional edges
ok = True
for b in range(4):
    for u in range(4):
        n = 2 * b + u
        if (O_of(n) == 0) != (n <= 3):
            ok = False
        if b >= 2 and O_of(n) == 0:
            ok = False   # any vertex with >= 2 bidirectional channels saturates
chk("mixed skeletons: n = 2b+u; O=0 <=> n<=3; b>=2 always saturated", ok)
# bidirectional-only lock-free cases: n in {0, 2}
chk("bidirectional-only unoversubscribed rungs: {0, 2} (b=0,1)",
    O_of(0) == 0 and O_of(2) == 0 and O_of(4) > 0)

# ------------------------------------------- document integration
g_src = era_paths.read("G_saturation.md")
tag = "CT4.1a"
chk("G_saturation.md contains **Cor CT4.1a (", "**Cor CT4.1a (" in g_src)
blk = g_src.split("**Cor CT4.1a (", 1)[1]
cut = min([blk.find(m) if blk.find(m) != -1 else len(blk)
           for m in ("\n---", "\n**Phys.**", "\n### ", "\n## ")])
body = blk[:cut]
chk("Cor CT4.1a: has Req (Cor) and Pf (Cor) with terminator",
    "**Req (Cor).**" in body and "**Pf (Cor).**" in body and r"\blacksquare" in body)
chk("Cor CT4.1a: cites CT0.11b (B) and no FT./Def-H./P-H token",
    "CT0.11b" in body and not re.search(r"FT\.|Def-H\.|P-H\d", body))
chk("G header Order line lists +CT4.1a", "+CT4.1a" in g_src)
chk("G closure exports mention CT4.1(a)", r"\mathrm{CT4.1(a)}" in g_src)
chk("G header lists verify_promotion_G_saturation.py",
    "verify_promotion_G_saturation.py" in g_src)

print(f"verify_promotion_G_saturation: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
sys.exit(1 if FAIL else 0)
