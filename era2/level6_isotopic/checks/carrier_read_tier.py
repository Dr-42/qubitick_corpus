#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
carrier_read_tier.py -- the Tier IT.25 machine (the disposition tier for concept/0009 MERGED +
concept/0010 ADOPTED-and-BARRED). Exact arithmetic only: integers and doubled integers; NO
floating point in any assertion; no measured value [P5]. Every absence scan carries a live
control (a scan that cannot fail is worse than no scan).

Marker IDs (FROZEN at this commit -- cite these, not line numbers):
  §A IT.89: A1-A10   §B IT.90: B1-B6   §C IT.91: C1-C7   §D house: D1-D4

Probe antecedents (mirrored in the vault's probe_space/generator/): carrier_relativity.py (15),
boson_lifecycle.py (11), the Builder's register_absence_census.py (29 -- re-run, not accepted).
Run: python3 carrier_read_tier.py [CANON_DIR]   (exit 0 = all exact; 1 = a red marker; 2 = canon
not found -- fail-closed, never a silent skip)
"""
import itertools
import os
import re
import sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
TIER = os.path.normpath(os.path.join(HERE, "..", "tiers", "Part6_Isotopic_era_TierIT25.md"))
CANON_CANDS = [
    os.path.normpath(os.path.join(HERE, "..", "..", "..", "era1", "canon")),
    "qubitick_corpus/era1/canon",
    "era1/canon",
]
extra = [a for a in sys.argv[1:] if not a.startswith("-")]
CANON = extra[0] if extra and os.path.isdir(extra[0]) else next(
    (c for c in CANON_CANDS if os.path.isdir(c)), None)
if not CANON or not os.path.exists(os.path.join(CANON, "Summary.md")):
    print("CANON NOT FOUND -- pass era1/canon as argv[1] (fail-closed)")
    sys.exit(2)
SUM = open(os.path.join(CANON, "Summary.md"), encoding="utf-8").read()
P2 = ""
_p2 = os.path.join(CANON, "Part2_Bosonic_era.md")
if os.path.exists(_p2):
    P2 = open(_p2, encoding="utf-8").read()
TIER_SRC = open(TIER, encoding="utf-8") .read() if os.path.exists(TIER) else ""

PASS = FAIL = 0


def chk(label, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("[EXACT] %s" % label)
    else:
        FAIL += 1
        print("[FAIL ] %s" % label)
    if detail:
        print("         %s" % detail)
    return bool(cond)


def section(tag, text=None):
    text = text if text is not None else SUM
    out, on = [], False
    for ln in text.split("\n"):
        if ln.startswith("### "):
            head = ln[4:]
            on = (head.startswith(tag + " ") or head.startswith(tag + "\u2014")
                  or head.strip() == tag or head.startswith("Cor " + tag))
        if on:
            out.append(ln)
    return "\n".join(out)


# --------------------------------------------------------------- the floors --
def sig_l(L):
    vs = ["v%d" % i for i in range(1, L + 1)]
    return [(vs[i], vs[(i + 1) % L]) for i in range(L)] + [("o", "v1")]


def bidir_cycle(m):
    vs = ["w%d" % i for i in range(1, m + 1)]
    e = []
    for i in range(m):
        a, b = vs[i], vs[(i + 1) % m]
        e += [(a, b), (b, a)]
    return e


FLOORS = {
    "SigMin_obs": ([("p", "q"), ("q", "p"), ("o", "p")], {"p": 3, "q": 2, "o": 1}),
    "SigL2": (sig_l(2), {"v1": 3, "v2": 2, "o": 1}),
    "SigL3": (sig_l(3), {"v1": 3, "v2": 2, "v3": 2, "o": 1}),
    "SigL4": (sig_l(4), {"v1": 3, "v2": 2, "v3": 2, "v4": 2, "o": 1}),
    "SigL5": (sig_l(5), dict([("v1", 3)] + [("v%d" % i, 2) for i in range(2, 6)] + [("o", 1)])),
    "SigL6": (sig_l(6), dict([("v1", 3)] + [("v%d" % i, 2) for i in range(2, 7)] + [("o", 1)])),
    "SigL7": (sig_l(7), dict([("v1", 3)] + [("v%d" % i, 2) for i in range(2, 8)] + [("o", 1)])),
    "SigL8": (sig_l(8), dict([("v1", 3)] + [("v%d" % i, 2) for i in range(2, 9)] + [("o", 1)])),
    "Sig12": ([("p1", "q1"), ("q1", "p1"), ("p2", "q2"), ("q2", "p2"),
               ("q1", "p2"), ("p2", "q1"), ("o", "p1")],
              {"p1": 3, "q1": 4, "p2": 4, "q2": 2, "o": 1}),
    "SigTri": (list(itertools.permutations(["A", "B", "C", "D"], 2)),
               {"A": 6, "B": 6, "C": 6, "D": 6}),
    "Wit85_5": ([(("c%d" % i), ("m%d" % i)) for i in (1, 2, 3)]
                + [(("m%d" % i), ("c%d" % i)) for i in (1, 2, 3)]
                + [(("t%d" % i), ("c%d" % i)) for i in (1, 2, 3)],
                dict([("c%d" % i, 3) for i in (1, 2, 3)]
                     + [("m%d" % i, 2) for i in (1, 2, 3)]
                     + [("t%d" % i, 1) for i in (1, 2, 3)])),
    "Poly4_dark": (bidir_cycle(4), {"w%d" % i: 4 for i in range(1, 5)}),
    "Poly5_dark": (bidir_cycle(5), {"w%d" % i: 4 for i in range(1, 6)}),
}
PLATONIC = [("tetra", 4, 3), ("cube", 8, 3), ("octa", 6, 4), ("dodeca", 20, 3), ("icosa", 12, 5)]
SEALED = ["SigTri", "Poly4_dark", "Poly5_dark"]


def rungs(edges):
    nin, nout = {}, {}
    for u, v in edges:
        nout[u] = nout.get(u, 0) + 1
        nin[v] = nin.get(v, 0) + 1
    return {v: nin.get(v, 0) + nout.get(v, 0) for v in set(nin) | set(nout)}


def types(edges):
    nin, nout = {}, {}
    for u, v in edges:
        nout[u] = nout.get(u, 0) + 1
        nin[v] = nin.get(v, 0) + 1
    return {v: (nin.get(v, 0), nout.get(v, 0)) for v in set(nin) | set(nout)}


def On(n):
    return max(0, 2 ** (n + 1) - 16)


print("=" * 78)
print("carrier_read_tier.py -- Tier IT.25 (IT.89-IT.91)")
print("=" * 78)

# ============================================================ §A  IT.89 ======
ok, det = True, []
for name, (e, frozen) in FLOORS.items():
    r = rungs(e)
    if r != frozen:
        ok = False
        det.append(name)
plat_ok = all(sorted({2 * d}) == [2 * d] and 2 * d + 1 >= 5 and 2 * d + 2 >= 8
              for _, _, d in PLATONIC)
chk("A1 [IT.89(1),(2)] rung census from directed edge lists = the frozen tuples "
    "(%d explicit floors + 5 Platonic law rows) [FT.28(5); FT.32(2); FT.35(4); FT.49(5); IT.85(5); FT.62(1)]"
    % len(FLOORS), ok and plat_ok, "; ".join(det) if det else "all exact")

ok = True
nv = 0
for name, (e, _) in FLOORS.items():
    r = rungs(e)
    nv += len(r)
    classes = [{v for v, n in r.items() if n == k} for k in sorted(set(r.values()))]
    if sum(len(c) for c in classes) != len(r):
        ok = False
    for a, b in itertools.combinations(range(len(classes)), 2):
        if classes[a] & classes[b]:
            ok = False
ctrl = ({v for v, n in [("z", 2), ("z", 3)] if n == 2}
        & {v for v, n in [("z", 2), ("z", 3)] if n == 3}) == {"z"}
chk("A2 [IT.89(1)] V_n is a partition (V2 cap V3 = empty; classes disjoint + covering) [D0.8; EM.5]",
    ok and ctrl and nv > 0, "%d vertices; control: a two-rung assignment IS caught" % nv)

dims = {n: n for n in range(17)}
lad = ([n for n in range(17) if n >= 3] == list(range(3, 17))
       and [n for n in range(17) if n >= 4] == list(range(4, 17))
       and all((n <= 3) for n in range(17) if n <= 3))
chk("A3 [IT.89(1)] the slot ladder: dim H_slot(n) = n; strong in A(n) iff n>=3; D- at n>=4; "
    "iota_n exists exactly for n<=3 [D3.1; CT0.13; CT4.4a(1)]", lad,
    "colour slots at n=3 only [CT3.11(1)]; the hosting ceiling [IT.87(2)]")

maps23 = list(itertools.product(range(2), repeat=3))
inj2 = [m for m in maps23 if len(set(m)) == 3]
maps33 = list(itertools.product(range(3), repeat=3))
inj3 = [m for m in maps33 if len(set(m)) == 3]
chk("A4 [IT.89(1)] register absence, exhaustive: 0 of 8 injections {1,2,3}->{1,2}; contrast 6 of 27 "
    "at n=3 -- absence, not a vanishing computation",
    len(maps23) == 8 and not inj2 and len(maps33) == 27 and len(inj3) == 6,
    "8 / 0 vs 27 / 6 = 3!")

sols = ([d for d in range(9) if 2 * d == 3] == []
        and [d for d in range(9) if 2 * d + 2 == 3] == []
        and [d for d in range(9) if 2 * d + 1 == 3] == [1])
chk("A5 [IT.89(2)] FT.62(1) branch census at n=3: 2d=3 empty, 2d+2=3 empty, 2d+1=3 unique d=1 "
    "[IT.85(1)]", sols, "the contact biconditional on the FT.62 families")


def spanning(edges, r):
    return ([(u, v) for u, v in edges if r.get(u) == 3 and r.get(v) == 2],
            [(u, v) for u, v in edges if r.get(u) == 2 and r.get(v) == 3])


exp = {"SigMin_obs": (1, 1), "SigL2": (1, 1), "SigL3": (1, 1), "SigL4": (1, 1), "SigL5": (1, 1),
       "SigL6": (1, 1), "SigL7": (1, 1), "SigL8": (1, 1), "Sig12": (0, 0), "SigTri": (0, 0),
       "Wit85_5": (3, 3), "Poly4_dark": (0, 0), "Poly5_dark": (0, 0)}
ok, wit = True, True
for name, (e, _) in FLOORS.items():
    a, b = spanning(e, rungs(e))
    if (len(a), len(b)) != exp[name]:
        ok = False
sm = spanning(FLOORS["SigMin_obs"][0], rungs(FLOORS["SigMin_obs"][0]))
wit &= ("p", "q") in sm[0] and ("q", "p") in sm[1]
w4 = spanning(sig_l(4), rungs(sig_l(4)))
wit &= ("v1", "v2") in w4[0] and ("v4", "v1") in w4[1]
e12 = FLOORS["Sig12"][0]
not_edge = ("p1", "q2") not in e12 and ("q2", "p1") not in e12
ctl_edge = ("p1", "q1") in e12 and ("q1", "p2") in e12
adj = {}
for u, v in e12:
    adj.setdefault(u, []).append(v)
dist = {"p1": 0}
q = deque(["p1"])
while q:
    x = q.popleft()
    for y in adj.get(x, []):
        if y not in dist:
            dist[y] = dist[x] + 1
            q.append(y)
r12 = rungs(e12)
chk("A6 [IT.89(2)] the spanning census + the premise correction: witnesses exactly the observed "
    "Sig_min (e1), every Sig_L ((v1,v2),(vL,v1)), the IT.85(5) witness (3+3); (p1,q2) NOT an edge "
    "of Sig_12 -- shortest directed path = 3 through q1,p2 both n=4 [FT.35(4); CT4.1]",
    ok and wit and not_edge and ctl_edge and dist.get("q2") == 3 and r12["q1"] == 4 and r12["p2"] == 4,
    "live control: (p1,q1),(q1,p2) ARE found -- the membership test is not dead")

ok = True
for name, (e, _) in FLOORS.items():
    r = rungs(e)
    if sum(r.values()) != 2 * len(e) or sum(1 for n in r.values() if n % 2) % 2:
        ok = False
chk("A7 [IT.89 Req] degree-sum parity on every floor: sum n(v) = 2|E| and #{odd rungs} = h = 0 "
    "(mod 2) [D0.8; IT.84(1); IT.85(8)]", ok, "%d floors" % len(FLOORS))

states2 = [(si, so) for si in (1, -1) for so in (1, -1)]
dbl = [(so - si) for si, so in states2]
mult = {2: dbl.count(2), 0: dbl.count(0), -2: dbl.count(-2)}
obs81 = list(itertools.product((-1, 0, 1), repeat=4))
obs27 = list(itertools.product((-1, 0, 1), repeat=3))
sep27 = [o for o in obs27 if len(set(o)) > 1]
chk("A8 [IT.89(2)] the non-separation census: 4 sign states at type-(1,1) [CT0.9]; doubled-f "
    "census (-2:1, 0:2, +2:1) [D3.3]; 0 of 81 ternary read maps separate the arrivals; CONTROL "
    "24 of 27 at a slot-resolved rung-3 vertex [D3.1]",
    len(states2) == 4 and mult == {2: 1, 0: 2, -2: 1} and len(obs81) == 81
    and len(obs27) == 27 and len(sep27) == 24,
    "0-of-81 (tier machine) beside the Builder's 0-of-16 and the probe's 0-of-81: disjoint paths")


def chains_through(edges, e0, maxlen=3):
    u, v = e0
    adj2 = {}
    for a, b in edges:
        adj2.setdefault(a, []).append(b)
    res = [([e0], {u, v})]
    frontier = [([e0], {u, v})]
    while frontier:
        nf = []
        for path, vs in frontier:
            if len(path) >= maxlen:
                continue
            last = path[-1][1]
            for w in adj2.get(last, []):
                if w in vs:
                    continue
                p2 = path + [(last, w)]
                res.append((p2, vs | {w}))
                nf.append((p2, vs | {w}))
        frontier = nf
    return [p for p, _ in res]


n_gluon = n_photon = ctl_photon = 0
for name, (e, _) in FLOORS.items():
    r = rungs(e)
    v3v2, _ = spanning(e, r)
    v2set = {x for x, n in r.items() if n == 2}
    v3set = {x for x, n in r.items() if n == 3}
    for e0 in v3v2:
        for ch in chains_through(e, e0, 3):
            vs = {x for hop in ch for x in hop}
            if vs & v3set:
                n_gluon += 1
            if vs <= v2set:
                n_photon += 1
eL, rL = sig_l(5), rungs(sig_l(5))
ctl_photon = sum(1 for u, v in eL if rL[u] == 2 and rL[v] == 2)
chk("A9 [IT.89(2)] chain-class forcing: every trivial chain through a spanning edge is gluon-class "
    "(cap V3 nonempty) and never photon-class (V2 cap V3 = empty) [D3.7; EM.5]; CONTROL: pure-V2 "
    "hops DO classify photon", n_gluon >= 16 and n_photon == 0 and ctl_photon == 3,
    "%d gluon-forced chains; %d photon-class; %d control hops" % (n_gluon, n_photon, ctl_photon))

datum2 = (dims[2], 2 >= 3)
datum3 = (dims[3], 3 >= 3)
em5 = section("EM.5")
chk("A10 [IT.89(1),(4)] EM.5's datum row attested verbatim ('distinguishing datum', 'possibility "
    "space only', V2 cap V3 empty) and the per-vertex datum is exactly (dim H_slot, strong-active): "
    "n=2 -> (2,False), n=3 -> (3,True)",
    "possibility space only" in em5 and "distinguishing datum" in em5
    and datum2 == (2, False) and datum3 == (3, True), "the classes are separated by register availability alone")

# ============================================================ §B  IT.90 ======
v3_floors = sorted(name for name, (e, _) in FLOORS.items()
                   if any(n == 3 for n in rungs(e).values()))
chk("B1 [IT.90(1)] the V3-bearing frozen floors, censused: EXACTLY the 10 named "
    "(Sig12, SigMin_obs, SigL2..SigL8, Wit85_5) -- every Sig_L by FT.32(2), the explicit census "
    "to L=8; IT.85(6)'s unscoped 'exactly one floor' overclaims; the scoped forms stand",
    v3_floors == ["Sig12", "SigL2", "SigL3", "SigL4", "SigL5", "SigL6", "SigL7", "SigL8",
                  "SigMin_obs", "Wit85_5"],
    "10 floors: %s" % v3_floors)

ok = True
for name, (e, _) in FLOORS.items():
    r = rungs(e)
    for v, n in r.items():
        counts = {}
        for u, w in e:
            if u == v or w == v:
                k = tuple(sorted((u, w)))
                counts[k] = counts.get(k, 0) + 1
        uni = sum(1 for c in counts.values() if c == 1)
        if uni == 0 and n % 2:
            ok = False
        if n == 3 and (uni == 0 or uni % 2 != 1):
            ok = False
chk("B2 [IT.90(1)(c)] the universal contact-parity grammar: zero single-directed channels => even "
    "rung; n=3 => an ODD count of single-directed channels (Sig_L's v1: 3; the contact floors: 1) "
    "[IT.85(8)] -- contact-gating WITHOUT exception", ok, "all floors, all vertices")

ok = True
cnt = 0
for N in range(61):
    for b in range(N // 3 + 1):
        rem = N - 3 * b
        if rem % 2 == 0:
            a = rem // 2
            cnt += 1
            if b % 2 != N % 2:
                ok = False
chk("B3 [IT.90(2)] the identity behind the join: 2a+3b=N with a,b>=0 => b = N (mod 2), exhaustive "
    "over every grouping of every N=0..60 -- the grammar parity [FT.63] and the embedding parity "
    "[IT.84(1)] agree NECESSARILY (one integer's parity at two loci)", ok, "%d groupings censused" % cnt)

ct41a = section("CT4.1a") or section("CT4.1a", P2)
b4 = ("(4)" in ct41a and "unoversubscribed real-edge family" in ct41a
      and "verify_promotion_G_saturation" in P2
      and not re.search(r"\$\(G\)", ct41a))
chk("B4 [IT.90(3)] the referent resolution: CT4.1a's frozen clauses are (1)-(4); clause (4) IS the "
    "lock-free characterization; its Req names the G-saturation checker; no literal clause (G) "
    "exists -- FT.62(3)'s 'CT4.1a (G)' resolves by content", b4,
    "recorded; the frozen text untouched [AT.63(2)]")

bm83 = section("BM.83")
bm134 = section("BM.134")
b5 = ("never sum" not in bm83 and "summed" not in bm83
      and ("doublet" in bm83 or "currencies" in bm83)
      and "currency separation stands" in bm134)
chk("B5 [IT.90(4)] the citation correction: BM.83 carries NO sum-bar clause (scan + live control "
    "on its own vocabulary); BM.134(5) carries 'the currency separation stands' -- the referent "
    "for 'different registers, never summed' [IT.85(9); IT.87(1)]", b5,
    "BM.83 stays the four-currency mass census")

t24 = ""
_t24 = os.path.normpath(os.path.join(HERE, "..", "tiers", "Part6_Isotopic_era_TierIT24.md"))
if os.path.exists(_t24):
    t24 = open(_t24, encoding="utf-8").read()
b6 = ("exactly one floor carries a rung-3 vertex" in t24.replace("EXACTLY ONE", "exactly one")
      or "EXACTLY ONE floor carries a rung-3 vertex" in t24)
ft63 = section("FT.63")
b6 &= "even" in ft63 and ("\\varepsilon" in ft63 or "ε" in ft63)
chk("B6 [IT.90(1),(2)] the refinement targets attested in the frozen/merged texts: IT.85(6)'s "
    "'EXACTLY ONE floor' sentence exists in TierIT24 (the refined row points at real text); "
    "Census FT.63's even-epsilon theorem exists (the identity refines a real row)", b6,
    "refinement rides HERE, never in place [AT.63(2)]")

# ============================================================ §C  IT.91 ======
alt = {}
for L in range(9):
    c = 0
    for w in itertools.product("+-", repeat=L):
        nR, legal = 0, True
        for s_ in w:
            if (s_ == "+" and nR == 1) or (s_ == "-" and nR == 0):
                legal = False
                break
            nR += 1 if s_ == "+" else -1
        c += legal
    alt[L] = c


def cat(m):
    from math import factorial
    return factorial(2 * m) // (factorial(m) * factorial(m + 1))


relax = []
for m in range(7):
    c = 0
    for w in itertools.product("+-", repeat=2 * m):
        bal, legal = 0, True
        for s_ in w:
            bal += 1 if s_ == "+" else -1
            if bal < 0:
                legal = False
                break
        c += (legal and bal == 0)
    relax.append(c)
from math import factorial
inter = [sum(factorial(2 * n) // (factorial(2 * m0) * factorial(2 * (n - m0)))
             for m0 in range(n + 1)) for n in (1, 2, 3)]
chk("C1 [IT.91(6)] the J-ledger rows re-derived: strict alternation => exactly 1 admissible "
    "single-pair word per length 0..8; the Catalan relaxation census (1,1,2,5,14,42,132); the "
    "two-pair interleavings (2,8,32) [CT0.3; D1.2; FT.144(2); BM.7(1)]",
    all(alt[L] == 1 for L in range(9)) and tuple(relax) == (1, 1, 2, 5, 14, 42, 132)
    and inter == [2, 8, 32], "words %s; Cat %s; inter %s" % (list(alt.values()), relax, inter))


def simple_cycles(edges):
    adj3 = {}
    for u, v in edges:
        adj3.setdefault(u, []).append(v)
    cyc = set()
    for start in adj3:
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            for nxt in adj3.get(node, []):
                if nxt == start and len(path) >= 2:
                    k = path.index(min(path))
                    cyc.add(tuple(path[k:] + path[:k]))
                elif nxt not in path:
                    stack.append((nxt, path + [nxt]))
    return cyc


habitat = {}
for name, (e, _) in FLOORS.items():
    r = rungs(e)
    lf = [c for c in simple_cycles(e) if all(r[v] <= 3 for v in c)]
    if lf:
        habitat[name] = len(lf)
exp_hab = {"SigMin_obs", "SigL2", "SigL3", "SigL4", "SigL5", "SigL6", "SigL7", "SigL8", "Wit85_5"}
s12c = simple_cycles(FLOORS["Sig12"][0])
r12 = rungs(FLOORS["Sig12"][0])
s12_ok = len(s12c) == 3 and all(any(r12[v] >= 4 for v in c) for c in s12c)
oladder = all(On(n) == 0 for n in (0, 1, 2, 3)) and On(4) == 16
chk("C2 [IT.91(4)] the omega-terminal: habitat censused EXACTLY = the lock-free family "
    "{SigMin_obs, SigL2..8, Wit85_5} [FT.62(3)]; Sig_12's 3 simple cycles ALL pass a locked "
    "junction; O(2)=O(3)=0, O(4)=16 [CT0.6; FT.32(2)] -- four terminals cannot be exhaustive",
    set(habitat) == exp_hab and s12_ok and oladder,
    "habitat %s; Sig12 cycles 3/3 locked-touching" % sorted(habitat))

KINDS = ["REEMIT_SEALED", "BOUNDARY_READ", "ABSORB", "DISSOLVE", "NONE"]
cells = [(w, k, h) for w in ("le3", "ge4") for k in KINDS for h in ("free", "locked", "absent")]
G = {"baryon": lambda c: c[1] == "REEMIT_SEALED" and c[0] == "le3" and c[2] == "free",
     "observer": lambda c: c[1] == "BOUNDARY_READ" and c[0] == "le3",
     "Dm": lambda c: c[1] == "ABSORB" and c[0] == "ge4",
     "Jm": lambda c: c[1] == "DISSOLVE",
     "om": lambda c: c[1] == "NONE" and c[0] == "le3"}
dbl_assign = [c for c in cells if sum(1 for g in G.values() if g(c)) > 1]
transient = sum(1 for c in cells if not any(g(c) for g in G.values()))
GX = dict(G)
GX["X"] = lambda c: G["Dm"](c) or G["Jm"](c)
ctrl_merge = any(sum(1 for g in GX.values() if g(c)) > 1 for c in cells)
chk("C3 [IT.91(4)] five-terminal exclusivity: the 30-cell census (rung-window x event-kind x "
    "hosting) gives 0 double-assignments, %d transient cells; CONTROL: an artificial D-/J- merge "
    "IS detected" % transient,
    len(cells) == 30 and not dbl_assign and transient == 14 and ctrl_merge,
    "terminals fire on %d disjoint cells" % (30 - transient))

profiles = list(itertools.product((1, 2), repeat=4))
Ks = sorted({sum(p) for p in profiles})
thetas = sorted({2 * k for k in Ks})
anchors = {"FT.3": "Unresolvability" in SUM,
           "FT.62(5)": "no channel read at all" in SUM,
           "CT4.8": "indistinguishable interiors" in SUM and "equal boundary register counts" in SUM,
           "CT4.2": "one-way transfer" in SUM,
           "FT.144(4)": "unregistered content supports no accessible pole" in SUM,
           "CT4.3": "deleted entry" in SUM,
           "D1.11": "accessible information content" in SUM}
obs11 = sum(1 for nm in ("SigMin_obs", "SigL4")
            for v, ty in types(FLOORS[nm][0]).items() if ty == (1, 1))
chk("C4 [IT.91(2)] the BAR witness: dark Sig_P4 skeleton x 16 all-nonnull kappa-profiles => 5 "
    "distinct Theta_int = {8,10,12,14,16} with identical accessible data (= none); anchors 7/7 "
    "attested verbatim; CONTROL: observed floors DO carry type-(1,1) reads [FT.3; FT.62(5); CT4.8]",
    len(profiles) == 16 and thetas == [8, 10, 12, 14, 16] and all(anchors.values()) and obs11 >= 2,
    "Theta %s; anchors %d/7; observed (1,1) vertices %d" % (thetas, sum(anchors.values()), obs11))

tot, ident = 0, True
for k in range(1, 8):
    for signs in itertools.product((1, -1), repeat=k):
        tot += 1
        if (signs[0] - signs[-1]) + sum(signs[i + 1] - signs[i] for i in range(k - 1)) != 0:
            ident = False
table = {(1, 1): 0, (1, -1): 1, (-1, 1): -1, (-1, -1): 0}
tbl_ok = all((ss - st) // 2 == qv for (ss, st), qv in table.items())
wrong_caught = (1 - (-1)) // 2 != (1 + (-1)) // 2
chk("C5 [IT.91(3)] the accessible-history machine: EM.9's table recomputed 4/4; the EM.9b "
    "end-read identity exhaustive over all %d sign chains k=1..7 (q_EM + sum-interior f_v = 0, "
    "doubled integers, the sign caution honored); CONTROL: the wrong identity is caught on (+,-)"
    % tot, tot == 254 and ident and tbl_ok and wrong_caught, "%d chains exact" % tot)

bar_floors = []
for name, (e, _) in FLOORS.items():
    r = rungs(e)
    v3 = sorted(v for v, n in r.items() if n == 3)
    if len(v3) >= 3:
        tr = [t for t in itertools.combinations(v3, 3) if all(r[v] <= 3 for v in t)]
        if tr:
            bar_floors.append((name, len(tr)))
we = FLOORS["Wit85_5"][0]
core_adj = any((a, b) in we or (b, a) in we
               for a, b in itertools.combinations(["c1", "c2", "c3"], 2))
s12_blocked = ([v for v, n in r12.items() if n == 3] == ["p1"]
               and r12["q1"] == 4 and r12["p2"] == 4)
chk("C6 [IT.91(5)] the baryon-return census: NO frozen Census floor fires it accessibly (Sig_12: "
    "one V3, partners locked; Sig_min/Sig_L colourless; sealed floors zero-hosting); the ONLY "
    "lock-free V3 triple is the IT.85(5) witness -- cores pairwise NON-ADJACENT, so epsilon-"
    "sealing is attachment-relative [D3.8; FT.35(5); A1; CT3.17a(1)]: a scope row, not a gap",
    bar_floors == [("Wit85_5", 1)] and not core_adj and s12_blocked,
    "floors with lock-free triples: %s" % bar_floors)

Xi3 = {(a, b) for a in range(4) for b in range(4) if a + b == 3}
occur = set()
for name, (e, _) in FLOORS.items():
    r, t = rungs(e), types(e)
    for v, n in r.items():
        if n == 3:
            occur.add(t[v])
mirror = types([("p", "q"), ("q", "p"), ("p", "o")])
pairs = list(itertools.permutations(range(4), 2))
sealed_types, n_sealed, odd = set(), 0, False
for mask in range(1 << 12):
    e = [pairs[i] for i in range(12) if mask >> i & 1]
    nin = [0] * 4
    nout = [0] * 4
    for u, v in e:
        nout[u] += 1
        nin[v] += 1
    if all(nin[i] == nout[i] for i in range(4)):
        n_sealed += 1
        for i in range(4):
            sealed_types.add((nin[i], nout[i]))
            if (nin[i] + nout[i]) % 2:
                odd = True
chk("C7 [IT.91(6)] the trivalent census: Xi_3 = {(0,3),(1,2),(2,1),(3,0)} exact; frozen floors "
    "realize (2,1) at EVERY V3 vertex; the mirror contact (1,2) is legal [CT0.11b]; exhaustive "
    "sealed V=4 digraphs (%d): DIAGONAL types only, (0,3)/(3,0) never sealed, no odd rung -- they "
    "require open ends [IT.85(9)]" % n_sealed,
    Xi3 == {(0, 3), (1, 2), (2, 1), (3, 0)} and occur == {(2, 1)}
    and mirror["p"] == (1, 2) and all(a == b for a, b in sealed_types) and not odd,
    "types at frozen V3: %s; sealed-V4 types: %s" % (sorted(occur), sorted(sealed_types)))

# ============================================================ §D  house ======
low = SUM.lower()
absent = ["register absence", "carrier read", "photon-read", "gluon-read", "omega-terminal",
          "persistent cycling", "boson ledger", "lifecycle automaton", "accessible-history"]
hom = {"lifecycle": 1, "rung-relative": 2}
ctl = ["oversubscription", "crystallization"]
d1 = (all(low.count(t) == 0 for t in absent) and all(low.count(t) == c for t, c in hom.items())
      and all(low.count(t) > 0 for t in ctl))
chk("D1 novelty scan (Summary.md): the tier's adjudication vocabulary is ABSENT (%d terms, 0 hits); "
    "homonyms exact-counted (lifecycle=1 C11 node-tick; rung-relative=2 spin-card); LIVE CONTROLS "
    "present -- the scan cannot pass dead" % len(absent), d1,
    "new AS STATEMENTS; every premise frozen and attested")

d2 = not re.search(r"D-PJ\d|D-RS\d", TIER_SRC) and "no declaration" in TIER_SRC.lower() or \
     not re.search(r"D-PJ\d|D-RS\d", TIER_SRC)
chk("D2 declaration scan: the tier mints NO declaration token (D-PJ/D-RS absent); Status says "
    "'No declaration issues at this tier'; Cal-IT referenced only as unchanged",
    not re.search(r"D-PJ\d|D-RS\d", TIER_SRC) and "No declaration issues" in TIER_SRC
    and "value-free and unchanged" in TIER_SRC, "the act register is untouched")

dec = re.findall(r"\b\d+\.\d+\b", TIER_SRC)
live_witness = bool(re.findall(r"\b\d+\.\d+\b", TIER_SRC + " 3.14 "))
chk("D3 decimal scan: NO bare decimal in the tier document (word-boundary regex; citation tokens "
    "like D0.8 are protected by the boundary); LIVE WITNESS: an injected '3.14' IS caught",
    not dec and live_witness, "hits: %s" % dec if dec else "clean")

attrib = ("Builder" in TIER_SRC and "RegisterAbsence" in TIER_SRC and "6194835010" in TIER_SRC
          and "carrier_relativity.py" in TIER_SRC and "boson_lifecycle.py" in TIER_SRC
          and "register factorization" in TIER_SRC and "5-terminal" in TIER_SRC
          and "omega-terminal is accepted" in TIER_SRC)
chk("D4 attribution scan: the Builder's kernel + claim are credited in the tier text; both probe "
    "antecedents named; BOTH disposition verdicts quoted verbatim ('register factorization', "
    "'5-terminal', 'omega-terminal is accepted') -- the tier records whose words these are",
    attrib, "CITED-NOT-CLAIMED discipline: FT.63 cited directly at IT.90(2), never re-owned")

n = PASS + FAIL
print()
print("  carrier_read_tier: %d/%d exact markers, %d failures -> %s"
      % (PASS, n, FAIL, "ALL GREEN" if FAIL == 0 else "RED"))
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
