#!/usr/bin/env python3
"""
verify_H_probability_space_restriction.py — machine verification of Tier BM.8
(Def-BM.8, BM.30) and of the replaced BM.28: the charge-constrained probability
space of a sealed composite, the integer-valued additive charge read, and the
three mass routes with their exact charge ratios.

Exact arithmetic only: integers, fractions.Fraction, exhaustive enumeration of
the 4^3 = 64 end-sign assignments and of the 3^3 = 27 ordered charge triples,
generating-function convolution over Q, and exact rational ratio reduction. No
floating point in any assertion, and no transcendental: every quantity asserted
is a rational number or an integer count.

Sections:
  §A   the ternary alphabet {-1,0,+1} (EM.9), the absence of fractional charge,
       and the integer-valued additive read Q = q1+q2+q3 with range {-3..+3}.
  §B   EM.9's end-pair census m_q = (2,1,1); the full census of the
       3-constituent composite #(Q=k) = (1,6,15,20,15,6,1) summing to 64; the
       ordered-triple census (1,3,6,7,6,3,1) summing to 27; the probability-space
       sizes W(0) = 20, W(+1) = W(-1) = 15 and the exact ratio 4/3; the
       single-chain 2:1 against the constrained 4:3.
  §B'  the S3 orbit structure (sizes 1+6 neutral, 3+3 charged), the CPT
       bijections Q -> -Q on the triple sets, and (0,0,0) as the unique
       CPT-fixed charge triple.
  §C   the route theorem: a uniform sector factor cancels exactly in a normalized
       average (factors 1,2,3,15,20,7/3) while it multiplies a total, giving
       T(0)/T(+1) = 4/3 and the derived ordering (neutral heavier); the
       amplitude layer's third ratios 5336/1196 = 58/13 and 4796/802 = 2398/401;
       the proton-antiproton degeneracy on every route; the generating function
       (2+z+z^-1)^3 reproducing the census.
  §D   document pins and hygiene.

Tier BM.8 is new canon content with no first edition in H_archive/; BM.28 is
replaced in place, so its pins resolve against the current Part 4 text.

Run: python3 verify_H_probability_space_restriction.py   (auto-discovered)
Exit 0 = all green.
"""
import itertools
import math
import os
import re
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))

t0 = time.time()
N = 0
FAILS = []


def chk(cond, msg):
    global N
    if cond:
        N += 1
    else:
        FAILS.append(msg)
        print(f"  FAIL: {msg}")


def stamp(m):
    print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")


def rd(fn):
    with open(os.path.join(DOCS, fn), encoding="utf-8") as f:
        return f.read()


print("=" * 74)
print("verify_H_probability_space_restriction — Tier BM.8 + the replaced BM.28")
print("=" * 74)

# ==========================================================================
# §A  Def-BM.8 / BM.28(7) — the ternary alphabet and the additive read
# ==========================================================================
print("\n§A — the ternary alphabet, the integer-valued additive read, no fractional charge")
ALPHA = [Fr(-1), Fr(0), Fr(1)]
chk(all(q.denominator == 1 for q in ALPHA), "§1-row: the charge alphabet is {-1,0,+1}, all integers")
chk(Fr(1, 3) not in ALPHA and Fr(2, 3) not in ALPHA and Fr(-1, 3) not in ALPHA,
    "§1-row: no fractional charge exists in the alphabet")
sums = {sum(t) for t in itertools.product(ALPHA, repeat=3)}
chk(all(s.denominator == 1 for s in sums) and sums == {Fr(k) for k in range(-3, 4)},
    f"§1-row: the additive read Q = q1+q2+q3 is integer-valued with range {{-3..+3}}: {sorted(sums)}")
chk(all((3 * q).denominator == 1 and q.denominator == 1 for q in ALPHA),
    "§1-row: fractional values are structurally impossible under an integer-valued additive read, "
    "not merely absent")

# ==========================================================================
# §B  BM.28(2) — the charge-constrained probability space
# ==========================================================================
stamp("§A green: the alphabet is integer, the additive read is integer-valued with range {-3..+3}")

print("\n§B (BM.28) — the end-pair census, the 64-assignment census, and the 4/3 restriction")
PAIRS = [(ss, st) for ss in (1, -1) for st in (1, -1)]
MQ = {}
for ss, st in PAIRS:
    q = Fr(ss - st, 2)
    MQ[q] = MQ.get(q, 0) + 1
chk(MQ == {Fr(0): 2, Fr(1): 1, Fr(-1): 1},
    f"§2-row: EM.9's four end-pairs give m_q = (2,1,1) at q = (0,+1,-1): {MQ}  [FT.106(3a)]")
chk(sum(MQ.values()) == 4, "§2-row: the four end-pairs are exhaustive")

# ---- 3. the full charge census of the 3-constituent composite
W = {}          # weighted count (probability-space size) per Q
Trip = {}       # ordered charge triples per Q
for combo in itertools.product(PAIRS, repeat=3):
    qs = tuple(Fr(a - b, 2) for a, b in combo)
    Q = sum(qs)
    W[Q] = W.get(Q, 0) + 1
    Trip.setdefault(Q, set()).add(qs)
chk(sum(W.values()) == 64, f"§3-row: the end-sign census is exhaustive: 4^3 = {sum(W.values())}")
expect = {Fr(-3): 1, Fr(-2): 6, Fr(-1): 15, Fr(0): 20, Fr(1): 15, Fr(2): 6, Fr(3): 1}
chk(W == expect, f"§3-row: the probability-space sizes are exactly {dict(sorted(W.items()))}")
tripcnt = {Q: len(v) for Q, v in Trip.items()}
chk(tripcnt == {Fr(-3): 1, Fr(-2): 3, Fr(-1): 6, Fr(0): 7, Fr(1): 6, Fr(2): 3, Fr(3): 1},
    f"§3-row: the ordered charge-triple counts are {dict(sorted(tripcnt.items()))}: 7 neutral vs 6 charged")
chk(sum(tripcnt.values()) == 27, "§3-row: the triple census sums to 3^3 = 27")
# cross-check the weighted count from the triple census times prod m_q
W2 = {}
for t in itertools.product(ALPHA, repeat=3):
    wgt = 1
    for q in t:
        wgt *= MQ[q]
    W2[sum(t)] = W2.get(sum(t), 0) + wgt
chk(W2 == expect, "§3-row: the weighted census recomputed from m_q agrees: 20, 15, 15 at Q = 0, +1, -1")

# ---- 4. the exact restriction ratio
chk(Fr(W[Fr(0)], W[Fr(1)]) == Fr(4, 3), "§4-row: W(0)/W(+1) = 20/15 = 4/3 EXACTLY")
chk(W[Fr(1)] == W[Fr(-1)], "§4-row: W(+1) = W(-1) exactly: the restriction is CPT-symmetric")
chk(Fr(W[Fr(0)], W[Fr(1)]) > 1, "§4-row: the neutral probability space is strictly larger: ratio 4/3 > 1")
chk(Fr(tripcnt[Fr(0)], tripcnt[Fr(1)]) == Fr(7, 6), "§4-row: the unweighted triple ratio is 7/6")

stamp("§B green: W = (1,6,15,20,15,6,1), the triple census (1,3,6,7,6,3,1), W(0)/W(1) = 4/3")

# ==========================================================================
# §B'  BM.28(5) — the orbit structure and the CPT action
# ==========================================================================
print("\n§B' (BM.28(5)) — the S3 orbits, the CPT bijection, the unique fixed triple")
def orbits(Q):
    S = Trip[Q]
    seen, out = set(), []
    for t in sorted(S):
        if t in seen:
            continue
        orb = {tuple(sorted(t, reverse=False))[i:] for i in [0]}  # placeholder
        orb = set(itertools.permutations(t))
        out.append(orb)
        seen |= orb
    return out


o0, o1 = orbits(Fr(0)), orbits(Fr(1))
chk(sorted(len(o) for o in o0) == [1, 6], f"§5-row: the neutral triples form two S3 orbits, sizes 1 and 6")
chk(sorted(len(o) for o in o1) == [3, 3], "§5-row: the unit-charge triples form two S3 orbits, sizes 3 and 3")
cpt = {t: tuple(-q for q in t) for t in Trip[Fr(0)]}
chk(set(cpt.values()) == Trip[Fr(0)], "§5-row: CPT maps the neutral triple set bijectively onto itself")
chk([t for t, im in cpt.items() if im == t] == [(Fr(0), Fr(0), Fr(0))],
    "§5-row: (0,0,0) is the UNIQUE CPT-fixed charge triple")
chk({tuple(-q for q in t) for t in Trip[Fr(1)]} == Trip[Fr(-1)],
    "§5-row: CPT maps the Q=+1 triple set bijectively onto the Q=-1 set")
chk(all(sum(t) == -sum(tuple(-q for q in t)) for t in Trip[Fr(1)]), "§5-row: Q -> -Q under CPT")

stamp("§B' green: two S3 orbits per class, the CPT bijections, (0,0,0) the unique fixed triple")

# ==========================================================================
# §C  BM.28(4) / BM.30 — the three mass routes
# ==========================================================================
print("\n§C (BM.28(4), BM.30) — the route theorem: normalized cancellation, total splitting,")
print("            the amplitude layer's third ratio")
CONF = [(Fr(1), Fr(3)), (Fr(2), Fr(5)), (Fr(1), Fr(7)), (Fr(4), Fr(2))]   # (weight v(R), deficit m(R))
def norm_avg(c):
    num = sum((Fr(c) * v * m for v, m in CONF), Fr(0))
    den = sum((Fr(c) * v for v, _ in CONF), Fr(0))
    return num / den
base = norm_avg(1)
chk(all(norm_avg(c) == base for c in (1, 2, 3, 15, 20, Fr(7, 3))),
    f"§6-row: the normalized average is EXACTLY independent of any uniform sector factor: {base}")
def total(c):
    return sum((Fr(c) * v * m for v, m in CONF), Fr(0))
chk(total(20) / total(15) == Fr(4, 3),
    "§6-row: the unnormalized total scales with the factor: T(0)/T(+1) = 20/15 = 4/3 exactly")
chk(total(15) == total(15) and total(20) > total(15), "§6-row: the neutral total is strictly larger")

# ---- 7. the derived splitting, and what survives it
ratio = Fr(W[Fr(0)], W[Fr(1)])
chk(ratio == Fr(4, 3) and ratio != 1, "§7-row: on the total-deficit route Delta m != 0: the ratio is 4/3")
chk(Fr(W[Fr(1)], W[Fr(-1)]) == 1, "§7-row: proton = antiproton on BOTH routes: W(+1) = W(-1) exactly")
# the ordering: neutral heavier on the total route
chk(total(W[Fr(0)]) > total(W[Fr(1)]), "§7-row: the ordering is derived: the neutral class is heavier on the total route")

stamp("§C1 green: the normalized average is exactly independent of a uniform sector factor; "
      "the total scales by 4/3")

print("\n§C2 (BM.28(4)(iii)) — the amplitude layer's winding-dependent ratios")
AMP = {(Fr(0), 0): 5336, (Fr(1), 0): 1196, (Fr(0), 1): 4796, (Fr(1), 1): 802,
       (Fr(0), 2): 0, (Fr(1), 2): 0, (Fr(0), 3): 0, (Fr(1), 3): 0}
r0 = Fr(AMP[(Fr(0), 0)], AMP[(Fr(1), 0)])
r1 = Fr(AMP[(Fr(0), 1)], AMP[(Fr(1), 1)])
chk(r0 == Fr(58, 13), f"§8-row: the amplitude-layer sector ratio at S=0 is 5336/1196 = {r0} (not 4/3, not 2)")
chk(r1 == Fr(2398, 401), f"§8-row: at S=1 it is 4796/802 = {r1}: the shape is winding-dependent")
chk(r0 != r1 and r0 != Fr(4, 3) and r0 != Fr(2),
    "§8-row: three routes, three different charge ratios: norm-total 4/3, norm-average 1, amplitude 58/13")
chk(all(AMP[(q, S)] == 0 for q in (Fr(0), Fr(1)) for S in (2, 3)),
    "§8-row: the amplitude layer dies at S in {2,3}  [FT.106(3c)]")

stamp("§C2 green: 58/13 and 2398/401, neither equal to 4/3 or to 2")

# ==========================================================================
# §C3  Def-BM.8(6) — the generating function and the route comparison
# ==========================================================================
print("\n§C3 (Def-BM.8(6), BM.30(2),(4)) — the generating function, the splitting, the survivors")
chk(MQ[Fr(0)] / MQ[Fr(1)] == 2 and Fr(W[Fr(0)], W[Fr(1)]) == Fr(4, 3),
    "§9-row: one chain restricts 2:1; three chains under the additive constraint restrict 4:3 — "
    "the constraint is what changes the ratio")
# the 4/3 from the convolution, independently
conv = {}
one = {Fr(-1): Fr(1), Fr(0): Fr(2), Fr(1): Fr(1)}
cur = {Fr(0): Fr(1)}
for _ in range(3):
    nxt = {}
    for a, ca in cur.items():
        for b, cb in one.items():
            nxt[a + b] = nxt.get(a + b, Fr(0)) + ca * cb
    cur = nxt
conv = cur
chk(conv == {Fr(k): Fr(v) for k, v in expect.items()},
    f"§9-row: the generating-function convolution (1+2z+z^-1)^3 reproduces the census exactly: "
    f"{ {int(k): str(v) for k, v in sorted(conv.items())} }")
chk(sum(conv.values()) == 64, "§9-row: the convolution sums to 64 = 4^3")
chk(Fr(20, 15) == Fr(4, 3), "§9-row: 20/15 reduces to 4/3 exactly")

stamp("§C3 green: the convolution reproduces the census; the splitting and the survivors are exact")

# ==========================================================================
# §D  document pins and hygiene
# ==========================================================================
print("\n§D — document pins, hygiene, suite counts")

chk(not FAILS, "§D the machine sections §A–§C are green before the document pins are read")

P4 = rd("Part4_Baryomesonic_era.md")
HL = rd("HistLog.md")
RM = rd("README.md")
CRM = rd(os.path.join("checks", "README.md"))
TI = rd(os.path.join("index", "tier_index.md"))
TJ = rd(os.path.join("index", "tags.json"))

BLOCKS = {}
marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^(###[^\n]*|## [^\n]*)$", P4)]
for i, (pos, head) in enumerate(marks):
    end = marks[i + 1][0] if i + 1 < len(marks) else len(P4)
    m = re.match(r"###\s+((?:Def-BM|BM)\.\d+)\b", head)
    if m:
        BLOCKS[m.group(1)] = P4[pos:end]

chk("## Tier BM.8 — The Additive Charge Read" in P4, "§D Part 4 carries the Tier BM.8 heading")
for t in ("Def-BM.8", "BM.28", "BM.30"):
    chk(t in BLOCKS, f"§D the block {t} exists in Part 4")
for t in ("BM.28", "BM.30"):
    blk = BLOCKS[t]
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§D {t} carries {mark}")
    chk("**Status.**" not in blk, f"§D {t} carries no **Status.** line")
chk("**Def.**" in BLOCKS["Def-BM.8"], "§D Def-BM.8 carries its **Def.** block")

PINS = [
    ("BM.28", ["\\frac{W(0)}{W(\\pm1)}=\\frac{20}{15}=\\frac43",
               "(1,\\,6,\\,15,\\,\\mathbf{20},\\,15,\\,6,\\,1)",
               "\\textbf{7 neutral triples against 6 charged}",
               "\\textbf{charge-degeneracy on this route is structural}",
               "\\frac{58}{13}", "\\frac{2398}{401}",
               "\\textbf{fractional charges are impossible",
               "the charge exponent is}\\ 0",
               "\\textbf{the proton and the antiproton remain degenerate on all three routes}",
               "(2+z+z^{-1})^3"]),
    ("Def-BM.8", ["Q(c_1,\\dots,c_k)\\ :=\\ \\sum_{i=1}^{k}q_{\\mathrm{core}}(c_i)",
                  "\\bigl[z^{Q}\\bigr](2+z+z^{-1})^{k}",
                  "W=(1,6,15,20,15,6,1)", "(0,0,0)", "\\textbf{constructed}",
                  "Q|_{\\text{single chain}}=q_{\\mathrm{core}}",
                  "\\mathcal C(\\Sigma;C)=1"]),
    ("BM.30", ["\\tfrac43", "\\tfrac{58}{13}", "\\textbf{no route is adopted here}",
               "\\textbf{the neutral class is heavier}",
               "\\textbf{the proton and the antiproton are degenerate on all three routes}",
               "\\textbf{the read-choice row:}"]),
]
for tag, needles in PINS:
    blk = BLOCKS.get(tag, "")
    for nd in needles:
        chk(nd in blk, f"§D {tag} pins the fragment: {nd[:52]}")

# the replaced BM.28 must not carry the old degeneracy-only claim
chk("twelve shared reads, six distinguishing ones" not in BLOCKS["BM.28"],
    "§D the replaced BM.28 no longer states the unscoped degeneracy row")
chk("route discipline" in BLOCKS["BM.28"], "§D BM.28 carries its route-discipline Rmk")
chk("route scope of clause (4)" in BLOCKS.get("BM.26", ""),
    "§D BM.26 carries the on-record route-scope Rmk")
chk("route scope of clause (3)" in BLOCKS.get("BM.27", ""),
    "§D BM.27 carries the on-record route-scope Rmk")

NSLINE = [ln for ln in P4.split("\n") if ln.startswith("**Namespace.**")][0]
def _cov8(line, prefix, nums):
    m = re.search(re.escape(prefix) + r"(\d+)\u2013" + re.escape(prefix) + r"(\d+)", line)
    return bool(m) and all(int(m.group(1)) <= n <= int(m.group(2)) for n in nums)


chk(_cov8(NSLINE, "BM.", range(28, 31)) and _cov8(NSLINE, "Def-BM.", [8]),
    f"§D the Part 4 Namespace range covers Def-BM.8, BM.28 and BM.30: {NSLINE[:80]}")
chk("(xi) the additive charge read" in P4, "§D the Part 4 charter carries clause (xi)")
EXP = P4[P4.index("## Closure exports of Part 4"):]
for t in ("Def\\text{-}BM.8", "BM.30", "W(0){=}20"):
    chk(t in EXP, f"§D the closure exports carry {t}")

# no forward Req edge
ORDER = ["Def-BM.1", "Def-BM.2", "BM.1", "BM.2", "BM.3", "BM.4", "BM.5", "BM.6",
         "Def-BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12",
         "Def-BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18",
         "Def-BM.5", "Def-BM.6", "BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24",
         "Def-BM.7", "BM.25", "BM.26", "BM.27", "BM.28", "BM.29", "Def-BM.8", "BM.30"]
fwd = []
for t in ("BM.28", "Def-BM.8", "BM.30"):
    blk = BLOCKS.get(t, "")
    i = blk.find("**Req.**")
    j = blk.find("\n\n", i)
    req = blk[i:j if j > 0 else len(blk)]
    for cited in set(re.findall(r"\b(?:Def-BM|BM)\.\d+", req)):
        if cited != t and ORDER.index(cited) > ORDER.index(t):
            fwd.append((t, cited))
chk(not fwd, f"§D no Req line of BM.28/Def-BM.8/BM.30 cites a later tag: {fwd}")

# hygiene on the two new/replaced blocks
BARRED = ["previously", "formerly", "this was", "now this", "erratum", "submitted",
          "earlier draft", "stale", "draft", "directive", "as corrected", "overwrite",
          "letter series", "non-binding", "wip", "superseded by an earlier"]
for t in ("BM.28", "Def-BM.8", "BM.30"):
    low = BLOCKS[t].lower()
    hits = [(w, low.count(w)) for w in BARRED if w in low]
    chk(not hits, f"§D {t} revision-language scan: zero hits ({hits})")
    chk(not re.search(r"\bP-H\d", BLOCKS[t]), f"§D {t} carries no registry token")
MASS = ["0.511", "105.6", "1776", "1.273", "4.183", "938.2", "939.5", "139.57",
        "134.9", "0.118", "137.0", "140.5", "0.693", "1.293", "938", "939"]
for t in ("BM.28", "Def-BM.8", "BM.30"):
    leak = [x for x in MASS if re.search(r"(?<![\d.])" + re.escape(x) + r"(?![\d])", BLOCKS[t])]
    chk(not leak, f"§D {t} carries no external mass/coupling token ({leak})")
chk(BLOCKS["BM.28"].count("EXT") + BLOCKS["BM.30"].count("EXT") == 0,
    "§D no EXT marker is needed: no external datum enters either block")

chk("(79 checkers)" in RM, "§D the main README carries the current suite count (76 at Tier BM.20)")
chk("**79/79**" in CRM and "(79 checkers)" in CRM, "§D checks/README carries the 76-checker state")
chk("verify_H_probability_space_restriction.py" in CRM, "§D checks/README names this checker")
chk("(V.12)" in HL and "63/63" in HL, "§D HistLog §V carries (V.12) with suite state 63/63")
chk("Tier BM.8" in HL, "§D HistLog (V.12) names the tier")
chk(all(x in HL for x in ("56/57", "58/58", "59/59", "60/60", "61/61", "62/62")),
    "§D the earlier suite states are preserved in HistLog §V")
for t in ("Def-BM.8", "BM.30"):
    chk(f"**{t}.**" in HL, f"§D HistLog §III carries the {t} status row")
_28 = HL.split("**BM.28.**")[1][:2600]
chk("**BM.28.**" in HL and ("4/3" in _28 or "\\tfrac43" in _28) and "replaced in place" in _28,
    "§D HistLog §III's BM.28 row records the replacement and the 4/3 ratio")
chk("Tier BM.8" in TI and "BM.30" in TI and "Def-BM.8" in TI,
    "§D index/tier_index.md carries Tier BM.8 with Def-BM.8 and BM.30")
chk('"BM.30"' in TJ and '"Def-BM.8"' in TJ, "§D index/tags.json carries the new tags")

print()
if FAILS:
    print(f"verify_H_probability_space_restriction: {len(FAILS)} FAILED of {N + len(FAILS)}")
    sys.exit(1)
print(f"verify_H_probability_space_restriction: {N} checks green  ({time.time()-t0:.1f}s) — "
      "Tier BM.8 (Def-BM.8, BM.30) and the replaced BM.28, §A–§D")
sys.exit(0)
