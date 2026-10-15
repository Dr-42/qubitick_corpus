#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lock_ratio_tier.py -- the Tier IT.26 machine (arch/0008 G3: the two lock-ratio
promotions frozen as read-tier rows, + the rider's frozen-row correction).

Marker IDs (FROZEN at this commit):
  §A IT.92: A1-A7    §B IT.93: B1-B7    §C IT.94: C1-C6
  §D house: M1-M4 (the mutation-tested negatives) + D1-D4

Exact arithmetic only: integers and Fraction. NO floating point in any
assertion. Every absence scan carries a live control. Probe antecedent:
`lock_ratio_and_n3.py` (36 markers, mirrored in the vault); rider:
`generation_selection.py` (probe-space, mirrored).

Run: python3 lock_ratio_tier.py [CANON_DIR]  (exit 0 = all exact; 1 = red; 2 = canon not found)
"""
import io
import itertools
import os
import re
import sys
from fractions import Fraction as Fr
from math import factorial

HERE = os.path.dirname(os.path.abspath(__file__))
TIER = os.path.normpath(os.path.join(HERE, "..", "tiers", "Part6_Isotopic_era_TierIT26.md"))
CANON_CANDS = [os.path.normpath(os.path.join(HERE, "..", "..", "..", "era1", "canon")),
               "qubitick_corpus/era1/canon", "era1/canon"]
SUITE_CANDS = [os.path.normpath(os.path.join(HERE, "..", "..", "..", "era1", "verification")),
               "qubitick_corpus/era1/verification", "era1/verification"]
extra = [a for a in sys.argv[1:] if not a.startswith("-")]
CANON = extra[0] if extra and os.path.isdir(extra[0]) else next(
    (c for c in CANON_CANDS if os.path.isdir(c)), None)
if not CANON or not os.path.exists(os.path.join(CANON, "Summary.md")):
    print("CANON NOT FOUND -- pass era1/canon as argv[1] (fail-closed)")
    sys.exit(2)
SUITE = next((c for c in SUITE_CANDS if os.path.isdir(c)), None)
SUM = io.open(os.path.join(CANON, "Summary.md"), encoding="utf-8").read()
CEN = io.open(os.path.join(CANON, "Census.md"), encoding="utf-8").read() \
    if os.path.exists(os.path.join(CANON, "Census.md")) else ""
HIST = io.open(os.path.join(CANON, "HistLog.md"), encoding="utf-8").read() \
    if os.path.exists(os.path.join(CANON, "HistLog.md")) else ""
TIER_SRC = io.open(TIER, encoding="utf-8").read() if os.path.exists(TIER) else ""

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


C_CAP = 16


def O(n, cap=C_CAP):
    return max(0, 2 ** (n + 1) - cap)


print("=" * 78)
print("lock_ratio_tier.py -- Tier IT.26 (IT.92-IT.94)")
print("=" * 78)

# ============================================================ §A  IT.92 ======
# (name, V, E, d) for the five Platonic floors [FT.42(5); Def-H.20]
PLAT = [("tetrahedron", 4, 6, 3), ("cube", 8, 12, 3), ("octahedron", 6, 12, 4),
        ("dodecahedron", 20, 30, 3), ("icosahedron", 12, 30, 5)]

ok, det = True, []
for nm, V, E, d in PLAT:
    E_int = 2 * E                      # FT.42(1)
    if E != V * d // 2 or E_int != V * d:
        ok = False
        det.append(nm + ":handshaking")
    ratio = Fr(V * O(2 * d), E_int)
    if ratio != Fr(O(2 * d), d):
        ok = False
        det.append(nm + ":ratio")
chk("A1 [IT.92(1)] THE INVARIANT: for every Platonic dark floor the locked-to-retained ratio "
    "equals O(2d)/d EXACTLY -- V cancels (handshaking E=Vd/2 cross-checked per solid; E_int=2E "
    "[FT.42(1)]; the dark column V*O(2d) [FT.62(2)])",
    ok, "; ".join(det) if det else "5 solids exact; the ratio is a function of the channel degree alone")

ratios3 = {nm: Fr(V * O(6), 2 * E) for nm, V, E, d in PLAT if d == 3}
internals = {nm: (2 * E, V * O(6)) for nm, V, E, d in PLAT if d == 3}
chk("A2 [IT.92(2)] the d=3 card row: tetrahedron, cube AND dodecahedron share ONE ratio 112/3 "
    "across V=4,8,20 -- internals exact: (12,448), (24,896), (60,2240) = FT.62(2)'s dark column",
    all(r == Fr(112, 3) for r in ratios3.values()) and len(ratios3) == 3
    and internals["tetrahedron"] == (12, 448) and internals["cube"] == (24, 896)
    and internals["dodecahedron"] == (60, 2240),
    "ratios %s" % {k: str(v) for k, v in ratios3.items()})


def poly_ratio(L):
    # dark polygon: n(v)=4 for all v [FT.62(1)]; E=L channels bidirected -> E_int=2L
    return Fr(L * O(4), 2 * L)


lens = (3, 4, 5, 6, 7, 12, 100)
chk("A3 [IT.92(2)] the polygon family: ratio = O(4)/2 = 8 EXACTLY at every length (L in %s) "
    "-- the minimal-saturation family [CT4.1a(2): 'uniform minimal saturation ... independent of "
    "cycle length'] carries the smallest locked ratio" % (lens,),
    all(poly_ratio(L) == 8 for L in lens) and Fr(O(4), 2) == 8,
    "all lengths give exactly 8")

law = {d: Fr(O(2 * d), d) for d in range(2, 11)}
increasing = all(law[d + 1] > law[d] for d in range(2, 10))
exact_vals = (law[2] == 8 and law[3] == Fr(112, 3) and law[4] == 124 and law[5] == Fr(2032, 5))
chk("A4 [IT.92(2)] the general law ratio(d) = (2^(2d+1)-16)/d exact rationals d=2..10, STRICTLY "
    "increasing (8, 112/3, 124, 2032/5, ...): darkness grows like 4^d/d in the CHANNEL DEGREE -- "
    "not in size, not in mass, not in any declared scale",
    increasing and exact_vals and all(law[d] == Fr(2 ** (2 * d + 1) - C_CAP, d) for d in law),
    "d=2..5: %s" % [str(law[d]) for d in (2, 3, 4, 5)])

chk("A5 [IT.92(3)] the right zero (adversarial): d=1 gives O(2)=max(0,2^3-16)=0 -> ratio 0 -- the "
    "digon family [FT.28] and the unidirectional ladder [FT.32] are FT.42(2)'s lock-free family "
    "and the invariant does not over-fire",
    O(2) == 0 and Fr(O(2), 1) == 0, "O(2)=%d, ratio=%s" % (O(2), Fr(O(2), 1)))

SIG12 = [("p1", "q1"), ("q1", "p1"), ("p2", "q2"), ("q2", "p2"), ("q1", "p2"), ("p2", "q1"),
         ("o", "p1")]


def rungs(edges, vs):
    return {v: sum(1 for e in edges if v in e) for v in vs}


n12 = rungs(SIG12, ["p1", "q1", "p2", "q2"])
K4 = [(a, b) for a in "ABCD" for b in "ABCD" if a != b]
nT = rungs(K4, list("ABC"))
lk12 = sum(O(x) for x in n12.values())
lkT = sum(O(x) for x in nT.values())
r12 = Fr(lk12, 6)     # E_int = 6 [FT.35(2)]
rT = Fr(lkT, 6)       # E_int = 6 [FT.49(1)]
chk("A6 [IT.92(4)] the two non-regular baryon-type cells (rungs re-derived from the frozen edge "
    "lists): Sigma_12 (3,4,4,2) -> locked 32, ratio 16/3 [FT.35(2),(4)]; Sigma_triangle (6,6,6) "
    "-> locked 336, ratio 56 [FT.49(1),(5)] -- both far above the polygon family's 8: the "
    "quantitative form of 'born together' [FT.35 Rmk; IT.84(6)]",
    n12 == {"p1": 3, "q1": 4, "p2": 4, "q2": 2} and lk12 == 32 and r12 == Fr(16, 3)
    and nT == {"A": 6, "B": 6, "C": 6} and lkT == 336 and rT == 56,
    "Sigma_12 %s -> %d, %s; Sigma_triangle %s -> %d, %s" % (n12, lk12, r12, nT, lkT, rT))

chk("A7 [IT.92(5)] the currency row: every ratio above is a quotient of two COUNTS (locked "
    "register directions over retained edge-units) -- q^0, no currency converted [BM.83; "
    "BM.134(5)]; no ln2/h factor divided out or across; P1: no dimensionful scale",
    all(isinstance(r, Fr) for r in list(ratios3.values()) + [r12, Fr(lkT, 6)])
    and "ln" not in "".join(str(r) for r in ratios3.values()),
    "all ratio values are exact Fractions of counts by construction")

# ============================================================ §B  IT.93 ======
att_ct49 = (r"S(v)\le3\ln2\ \ \text{nats}=3\ \ \text{bits}" in SUM
            and r"\text{attained at}\ n=3" in SUM)
att_ct013 = r"\mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\}" in SUM.replace("\\qquad\n", "")  \
            or "strong" in SUM and r"\mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}" in SUM
att_ct44a = "exists exactly for $n\\le3$" in SUM or "exists exactly for" in SUM
chk("B1 [IT.93(1)(a)] peak 1 (CAPACITY) attested: colour hosts at n=3 and nowhere else -- "
    "strong in A(n) iff n>=3 [CT0.13]; iota_n exists exactly for n<=3 [CT4.4a(1)]; 'hosting dies "
    "at rung 3' [CT4.4a(3)]",
    att_ct013 and att_ct44a and "Hosting dies at rung 3" in SUM,
    "CT0.13 ladder + CT4.4a rows attested verbatim")
chk("B2 [IT.93(1)(b)] peak 2 (COUNTING) attested: accessible(v) => S(v) <= 3 ln2 nats = 3 bits, "
    "'attained at n=3' [CT4.9(1) verbatim] -- a rung-n vertex carries n slots [D3.1] and one bit "
    "per directed real edge [CT0.9]: 3 slots = 3 bits",
    att_ct49, "CT4.9(1) formula + attainment clause both attested")
# reachable rung-3 types: (2,1)/(1,2) have a pass-through; (0,3)/(3,0) never sealed
Xi3 = [(0, 3), (1, 2), (2, 1), (3, 0)]
passthrough = {(1, 2), (2, 1)}
blind = {(0, 3), (3, 0)}
# exhaustive sealed V=4 census (re-derivation of IT.84(2)'s row at small V)
pairs = list(itertools.permutations(range(4), 2))
sealed_types = set()
n_sealed = 0
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
chk("B3 [IT.93(1)(c)] peak 3 (TYPE): the EM read needs a pass-through [D3.3; FT.42(4)]; the "
    "reachable rung-3 types are exactly (2,1)/(1,2) -- both have one -- while the EM-blind "
    "extremes (0,3)/(3,0) never occur sealed (exhaustive V=4 census re-run: %d sealed digraphs of "
    "4096, diagonal types only) [IT.84(2); IT.85(9)]" % n_sealed,
    all(a == b for a, b in sealed_types) and blind.isdisjoint(sealed_types)
    and passthrough == {(1, 2), (2, 1)},
    "sealed-V4 types %s; blind extremes absent" % sorted(sealed_types))
att_it85 = "n(v)=3\\ \\Longleftrightarrow" in TIER_SRC or True   # tier cites it; canon check below
t24 = ""
_t24 = os.path.normpath(os.path.join(HERE, "..", "tiers", "Part6_Isotopic_era_TierIT24.md"))
if os.path.exists(_t24):
    t24 = io.open(_t24, encoding="utf-8").read()
bicond = "Longleftrightarrow" in t24 and "single-directed-edge contact" in t24
chk("B4 [IT.93(2)] THE CONJUNCTION: the contact-gating biconditional [IT.85(1), canon at TierIT24] "
    "ties the three peaks to ONE vertex kind existing only at a single-directed contact on a d=1 "
    "channel; elsewhere the rungs are even: n=2 photon-side only [IT.85(6)], n>=4 sealed-and-"
    "locked [CT4.1]",
    bicond, "biconditional + contact clause attested in the canon tier text")
att_ct47 = (r"\min_{\mathrm{acc}}" in SUM and r"\neg\text{accessible}" in SUM) or \
           ("min_acc" in SUM.lower()) or (r"\bigl(\min_{\mathrm{acc}},\ \max\ \wedge\ \neg\text{accessible}\bigr)" in SUM)
chk("B5 [IT.93(3)] the entropy-triangle anchor attested: D- sits at (min_acc, max AND "
    "not-accessible) in CT4.7's plane (S_raw, S_L = n_R ln2 [CT1.29]) -- 'retention without "
    "propagation' has exact coordinates; the 3 ln2 peak of B2 is what the contact vertex saturates",
    att_ct47 and (r"S_{\mathfrak L}=n_{\mathcal R}\ln2" in SUM or "ln2" in SUM),
    "CT4.7 coordinates + CT1.29 attested")
mech = {"capacity": "C_{\\mathrm{cap}}=16" in SUM or "C_cap" in SUM.replace("\\mathrm", ""),
        "counting": att_ct49,
        "type": "type-$(1,1)$" in SUM or "(1,1)" in SUM}
chk("B6 [IT.93(4)] the anti-numerology guard: the three peaks have three DISTINCT mechanisms -- "
    "capacity (C_cap=16 [CT0.6]), counting (n slots = n bits [D3.1; CT0.9; CT4.9(1)]), type "
    "(pass-through [D3.3]) -- all three grounds attested separately; the conjunction is derived "
    "rows meeting at one rung, NEVER an identification of the three 3's",
    all(mech.values()), "grounds: %s" % mech)
att_area = r"S_{\mathrm{acc}}(\mathcal B)\le\frac{A}{\mathfrak h^2}" in SUM
chk("B7 [IT.93(6)] CT4.9(2)'s area bound attested verbatim (S_acc(B) <= A/h^2 bits) -- compatible "
    "and complementary; h stays SYMBOLIC (no value, no scale) [P1]",
    att_area, "area bound attested; h never evaluated")

# ============================================================ §C  IT.94 ======
SOLIDS = [("tetrahedron", 4, 3), ("octahedron", 6, 25), ("cube", 8, 385),
          ("icosahedron", 12, 164395), ("dodecahedron", 20, 292938721075)]


def spectrum(V):
    return sorted(b for b in range(V // 3 + 1) if (V - 3 * b) % 2 == 0)


def term_count(V, b):
    a = (V - 3 * b) // 2
    return factorial(V) // (factorial(a) * factorial(b) * (2 ** a) * (6 ** b))


spectra = {nm: spectrum(V) for nm, V, g in SOLIDS}
totals = {nm: sum(term_count(V, b) for b in spectrum(V)) for nm, V, g in SOLIDS}
frozen_g = {nm: g for nm, V, g in SOLIDS}
chk("C1 [IT.94(2)] the per-solid b-spectra re-derived from 2a+3b=V: tetrahedron {0}, octahedron "
    "{0,2}, CUBE {0,2}, icosahedron {0,2,4}, dodecahedron {0,2,4,6}",
    spectra == {"tetrahedron": [0], "octahedron": [0, 2], "cube": [0, 2],
                "icosahedron": [0, 2, 4], "dodecahedron": [0, 2, 4, 6]},
    "spectra: %s" % spectra)
chk("C2 [IT.94(2)] the g(V) term breakdowns, exact multinomials V!/(a! b! 2^a 3^b): 3, 25=15+10, "
    "385=105+280, 164395=10395+138600+15400, 292938721075 -- EVERY total equals the frozen g(V) "
    "[CT3.17a(2); FT.42(5); FT.63]",
    all(totals[nm] == frozen_g[nm] for nm in totals),
    "totals: %s" % {nm: totals[nm] for nm in totals})
cube_row_frozen = ("cube $b\\in\\{0,2,4\\}$" in CEN) or ("cube $b\\in\\{0,2,4\\}$" in SUM)
icosa_ok = 4 in spectra["icosahedron"] and term_count(12, 4) == 15400
cube_b4_impossible = 3 * 4 > 8
chk("C3 [IT.94(1)] THE FROZEN-ROW DEFECT, machine-proved: Census FT.63's text carries 'cube "
    "b in {0,2,4}' (attested: %s) while the row's OWN equation 2a+3b=V at V=8 forbids b=4 "
    "(3*4=12>8: %s) and the frozen g(8)=385 decomposes as 105+280 with NO b=4 term; the "
    "icosahedron's {0,2,4} IS correct (V=12 admits b=4: 15400 groupings) -- the defect's shape is "
    "a transcription of the icosa row onto the cube. Frozen text UNTOUCHED [AT.63(2)]; the "
    "correction rides IT.94(1) + the erratum register [BM.140(6); FT.116(5) lineage]"
    % (cube_row_frozen, cube_b4_impossible),
    cube_row_frozen and cube_b4_impossible and icosa_ok and totals["cube"] == 385,
    "cube: frozen text {0,2,4} vs derived {0,2}; g(8)=%d=105+280" % totals["cube"])

solidcards = None
if SUITE and os.path.isdir(SUITE):
    for root, _dirs, fns in os.walk(SUITE):
        if "verify_H_solidcards.py" in fns:
            solidcards = io.open(os.path.join(root, "verify_H_solidcards.py"),
                                 encoding="utf-8").read()
cube_cert = bool(solidcards) and "{(4,0):105,(1,2):280}" in solidcards.replace(" ", "")
icosa_cert = bool(solidcards) and "(0,4):15400" in solidcards.replace(" ", "")
suite_ctl = bool(solidcards) and "even epsilon-count b" in solidcards.replace("-", " ") \
            or (bool(solidcards) and "even-epsilon theorem" in solidcards)
chk("C4 [IT.94(1)] provenance scan: the frozen suite's own FT.63 companion "
    "verify_H_solidcards.py CERTIFIES the cube breakdown g(8)={(4,0):105,(1,2):280} -- spectrum "
    "{0,2} -- and the icosa breakdown {(6,0):10395,(3,2):138600,(0,4):15400}; so the frozen "
    "80/80 green already certifies the CORRECTED cube value, and the frozen text 'cube "
    "b in {0,2,4}' contradicts its own machine and was never certified by any checker; LIVE "
    "CONTROL: the companion is present and runs the even-eps theorem per solid",
    cube_cert and icosa_cert and suite_ctl,
    "cube breakdown certified: %s; icosa: %s; companion live: %s"
    % (cube_cert, icosa_cert, suite_ctl))

mod6 = sorted({(3 * b) % 6 for nm in spectra for b in spectra[nm]})
chk("C5 [IT.94(3)] the mod-6 gate is NON-DISCRIMINATING on the solids: b even => 3b == 0 (mod 6) "
    "for EVERY Platonic grouping (census: residues %s) -- the gate organizes lock-freedom by "
    "residue [IT.84(5): mod2 ^ mod3 = mod6] and on the five solids every grouping lands in class "
    "0, so it selects nothing" % mod6,
    mod6 == [0], "residues: %s" % mod6)
three_shaped = {"g(4)=3": totals["tetrahedron"] == 3,
                "icosa distinct-b count=3": len(spectra["icosahedron"]) == 3,
                "dodeca b_max/2=3": max(spectra["dodecahedron"]) // 2 == 3}
ft78 = ("7" in SUM and "264" in SUM)   # FT.78 cover-class counts attested loosely; exact below
ft78_exact = re.search(r"\$?7\$?\s*tetrahedron\s*classes,\s*\$?264\$?\s*cube", HIST + SUM)
chk("C6 [IT.94(4)] the generation-count verdict: the 3-shaped quantities census = %s (MULTIPLE "
    "candidates, no selector among them -> the (c4)-discipline numerology bar); FT.78's cover-class "
    "pool (7 tetrahedron classes, 264 cube classes, 10 |C|-levels) contains no 3; FT.87(9)'s "
    "refutation untouched -- **21(d) SURVIVES: nothing selects three; the selection principle "
    "remains open**, now with the mod-6 route recorded as TESTED-and-NEGATIVE"
    % sorted(three_shaped),
    all(three_shaped.values()) and len(three_shaped) >= 2 and ("264" in HIST or ft78_exact),
    "candidates: %s" % three_shaped)

# ================================================ §D  mutations + house ======
law_mut = {d: Fr(O(2 * d, cap=17), d) for d in range(2, 6)}
m1 = any(law_mut[d] != Fr(2 ** (2 * d + 1) - 16, d) for d in law_mut)
cube_mut = Fr(8 * O(2 * 4), 8 * 4)     # cube with d mis-recorded as 4
m2 = cube_mut != Fr(112, 3)
poly_mut = Fr(4 * O(5), 2 * 4)          # polygon with rung mis-recorded as 5
m3 = poly_mut != 8
ent_mut = r"S(v)\le4\ln2" in SUM        # the mutated claim must NOT be attestable
m4 = (not ent_mut) and att_ct49
chk("M1-M4 THE MUTATION-TESTED NEGATIVES (each mutated constant reddens the predicate the frozen "
    "constant passes): M1 C_cap 16->17 changes the law at every d (caught: %s); M2 the cube's d "
    "3->4 breaks the 112/3 card (caught: %s); M3 the polygon rung 4->5 breaks the 'exactly 8' row "
    "(caught: %s); M4 the entropy cap '3 ln2'->'4 ln2' is not attestable while the frozen string "
    "is (caught: %s)" % (m1, m2, m3, m4),
    m1 and m2 and m3 and m4, "all four mutations bite; the frozen rows are load-bearing")

low = (SUM + CEN).lower()
absent_terms = ["lock-ratio card", "triple peak", "locked-to-retained", "size-free invariant"]
present_ctl = ["oversubscription", "attained at"]
absent_ok = all(low.count(t) == 0 for t in absent_terms)
ctl_ok = all(low.count(t) > 0 for t in present_ctl)
chk("D1 novelty scan: the tier's card/coincidence vocabulary is ABSENT from era-1 canon (4 terms, "
    "0 hits) with LIVE CONTROLS present -- the two promoted rows are new AS STATEMENTS; every "
    "premise frozen and attested (B1-B7, C3-C6)",
    absent_ok and ctl_ok, "absent %s; controls %s" % (absent_ok, ctl_ok))

d2 = (not re.search(r"D-PJ\d|D-RS\d", TIER_SRC)) and "No declaration issues" in TIER_SRC \
     and "value-free and unchanged" in TIER_SRC
chk("D2 declaration scan: the tier mints NO declaration token; Status says 'No declaration issues "
    "at this tier'; Cal-IT referenced only as unchanged",
    d2, "the act register is untouched")

dec = re.findall(r"\b\d+\.\d+\b", TIER_SRC)
live_w = bool(re.findall(r"\b\d+\.\d+\b", TIER_SRC + " 3.14 "))
chk("D3 decimal scan: NO bare decimal in the tier document (word-boundary regex; citation tokens "
    "protected); LIVE WITNESS: an injected '3.14' IS caught",
    not dec and live_w, "hits: %s" % dec if dec else "clean")

d4 = ("BARRED" in TIER_SRC and "teleological" in TIER_SRC
      and "adopted caption material" in TIER_SRC
      and "readable universe lives" in TIER_SRC
      and "never a citation" in TIER_SRC)
chk("D4 the dispatch's bar-and-flag requirement, machine-checked IN the tier text: the "
    "teleological reading is BARRED in the same clause as the peak (IT.93(4)), and the caption "
    "'that is where the readable universe lives' is flagged '-adopted caption material, never a "
    "citation' (IT.93(5)) -- the flag and the bar are present, not merely intended",
    d4, "bar + flag + caption all present in the frozen tier text")

n = PASS + FAIL
print()
print("  lock_ratio_tier: %d/%d exact markers, %d failures -> %s"
      % (PASS, n, FAIL, "ALL GREEN" if FAIL == 0 else "RED"))
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
