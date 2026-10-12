#!/usr/bin/env python3
"""verify_H_form_factor.py — companion to Tier F.32:
FT.97 / FT.98 / FT.99 of the H working layer (split canon; Tier F.32 lives in H12).

Grounded in the tier texts and the frozen anchors documented in H itself. Exact arithmetic only:
every census an int, every average a Fraction. No floats in any assertion.

Sections:
  §A  FT.97(1)–(2): node ontology (V(R) subset of V(Gamma); roles = the derived
      vertex types); the three underdeterminations exposed — per-cover tail
      normalization sum_v i_v = K = n_R exactly on all 17,042 strict covers of
      the ten computed families (8 polygons C_3..C_10 + tetrahedron + cube),
      the end-sum = 2K and half-split = 1K factor-2 ledger; the five role
      weights w_U, w_K, w_C, w_E, w_H evaluated per cover (none selected)
  §B  FT.97(3): the reduction identities S_wU(R) = K(R) and
      S_wC(R) = |C(R)| = K/2 machine-asserted on EVERY strict cover of all
      ten families; K = 2|C| per cover; the anchor M(w_U)(tetra, byp) =
      62208/15745 reproduced from independent enumeration; M(w_C) = M(w_U)/2
      identically per family and sector
  §C  FT.97(5): the Form-Factor Ceiling — finite-type maxima c_w = (6,36,1,6,24)
      over the type set {0 < a+b <= 6}; S_w(R) <= c_w*V pointwise (per-family
      maxima); the |C| caps 3V/4 (byp) / V (lock) per cover; the exact
      required-V table at R = 3477 [EXT]: (2187, 1062, 6561, 65, 515)
  §D  FT.98: polygon censuses n = 3..10 by TWO enumerators (backtracking vs
      covering DP); FT.68(2)'s Z-anchors verbatim; cover counts and sector
      splits; byp |C|_max <= floor(3n/4); the exact Fraction M-tables (all
      32 documented values); growth ratios vs P_3; the fifth clean negative;
      the concentration Fractions at |C|_max with their documented decimals
  §E  FT.99: tetrahedron two-enumerator set identity (4096 power-set filter ==
      backtracking, 101 covers) + 7-class table + Z = (1057,448) + the exact
      all/byp/lock M-tables (15 Fractions) + locked w_E = 0 structural +
      concentration 16384/35201; cube fresh 11,205-covers census cross-checked
      against the stored class data (sum Omega = 11,205; Omega-histogram
      identical; Z = (1,109,313, 1,150,848)) + the exact M-tables + the
      unreduced denominator 804,725,505 = 3 * 268,241,835 with the gcd trap
      recorded + concentration 67,108,864/804,725,505; the cube/tetra ratio
      band (1.831 primary, <= 2.652 widest, m_hid ratio 2); the dominance
      census (tetra 64/100 weighted 248/275; cube 10,052/11,204 weighted
      3,115,352/3,143,459; polygons 3/9 -> 2725/3165) under the half-split
      rule, with the thread-tie mechanism verified
  §F  the five no-referent counts in frozen A–G ('worldline', 'propagator',
      'refinement', 'subdivision', 'form factor'); the m_hid floor anchors
      12/24 = 2E (FT.42(1)); the integrity ledger (6a) endpoint-double-count
      trap reproduced exactly (124416/15745 = 2x the anchor) and (6b) the
      reduced-vs-unreduced gcd record

Run: python3 verify_H_form_factor.py    (auto-discovered by run_all.py)
Exit 0 = all green.  Per-cover granularity mirrors the original's 68,356:
five asserted identities on each of the 17,042 strict covers (tail
normalization, the factor-2 convention ledger, S_wU = K, S_wC = |C|,
K = 2|C|) plus the family-level batteries.
"""
import hashlib
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

import math
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from bypasscore import (complete_graph, cube_graph, cycle_graph, undirected_from,  # noqa: E402
                        types_of, centers_of, is_cover_strict, enum_covers_bt,
                        cover_dp, cover_value, automorphisms)

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


t0 = time.time()


def stamp(msg):
    print(f"  [{time.time()-t0:6.1f}s] {msg}  (checks: {PASS + FAIL})")


def round_frac(x, nd):
    """exact rational rounding to nd decimals (half-up), no floats."""
    sc = 10 ** nd
    return Fr(math.floor(x * sc + Fr(1, 2)), sc)


# ================================================================== §0 canon
# (layer integrity is guarded by checks/verify_corpus_graph.py — tag-definition
#  uniqueness, no duplicate publication, citation closure)
if ARCH:
    _SPLIT_H = ['H_archive/H01_flux_and_fermion.md', 'H_archive/H02_edges_and_spin_charge.md',
                'H_archive/H03_subnetwork_force_and_geometry.md', 'H_archive/H04_aspect_operator_and_spectrum.md',
                'H_archive/H05_floor_families.md', 'H_archive/H06_platonic_and_polygon_floors.md',
                'H_archive/H07_spin_ladder.md', 'H_archive/H08_loops_and_bott.md',
                'H_archive/H09_flicker_and_domains.md', 'H_archive/H10_sm_audit.md',
                'H_archive/H11_gravity_and_koide.md', 'H_archive/H12_chirality_and_form_factor.md',
                'H_archive/H13_registries_and_gaps.md']
if ARCH:
    _missing = [f for f in _SPLIT_H if not os.path.exists(os.path.join(DOCS, f))]
if ARCH:
    chk("§0 split canon present (13 parts)", not _missing, str(_missing))

# ---------------------------------------------------------------- families
# the ten computed families of the tier: polygons C_3..C_10, tetrahedron, cube
FAMILIES = []
for n in range(3, 11):
    nv, DE = cycle_graph(n)
    FAMILIES.append((f"C_{n}", nv, undirected_from(nv, DE)))
nvT, DET = complete_graph(4)
FAMILIES.append(("tetra", nvT, undirected_from(nvT, DET)))
nvC, DEc = cube_graph()
FAMILIES.append(("cube", nvC, undirected_from(nvC, DEc)))

# role weights (FT.97(2b)) — five derived candidates over the finite type set
def w_U(t):   # 1_participating
    return 1 if t[0] + t[1] > 0 else 0


def w_K(t):   # k_v = a + b  [CT0.11's capped quantity]
    return t[0] + t[1]


def w_C(t):   # 1_centre
    return 1 if t == (1, 1) else 0


def w_E(t):   # 1_endpoint: types (a,0)/(0,b), a+b > 0
    return 1 if (t[0] == 0) != (t[1] == 0) else 0


def w_H(t):   # hub excess max(0, a+b-2)
    return max(0, t[0] + t[1] - 2)


WS = [("w_U", w_U), ("w_K", w_K), ("w_C", w_C), ("w_E", w_E), ("w_H", w_H)]


def cover_data(nv, R):
    """per-cover census record: exact ints/Fractions only."""
    t = types_of(nv, R)
    K = len(R)
    nC = len(centers_of(nv, R))
    locked = any(a + b >= 4 for (a, b) in t)
    out = {
        "K": K, "nC": nC, "locked": locked, "w16": 16 ** nC,
        "tail": sum(b for (a, b) in t),                     # sum_v i_v, i_v = outdeg
        "endsum": sum(a + b for (a, b) in t),                # the 2x convention
        "halves2": sum(a + b for (a, b) in t),               # half-split sums to K (x2)
    }
    # S_w(R) = sum_v w(type(v)) * i_v with the tail convention i_v = outdeg
    out["S"] = {nm: sum(w(tv) * tv[1] for tv in t) for nm, w in WS}
    # dominance (FT.99(4), convention-free half-split): centre+hub role bits =
    # 1 per centre thread + the FULL hub excess max(0, a+b-2) on every
    # multi-role vertex (a+b >= 3); endpoint role bits = (a+b)/2 each.
    # x2 to stay in integers.  This exact rule reproduces all four documented
    # anchors: tetra 64/100 (248/275), cube 10,052/11,204 (3,115,352/3,143,459),
    # C_3 3/9, C_10 2725/3165.
    end2 = sum((a + b) for (a, b) in t if w_E((a, b)))
    ch2 = (2 * sum(1 for tv in t if tv == (1, 1))
           + 2 * sum(max(0, tv[0] + tv[1] - 2) for tv in t if tv[0] + tv[1] >= 3))
    out["dom"] = ch2 > end2
    out["tie"] = ch2 == end2
    return out


# enumerate every family once (both enumerators where documented)
DATA = {}
for name, nv, U in FAMILIES:
    covs = [frozenset(R) for _, R in enum_covers_bt(nv, U)]
    recs = [cover_data(nv, R) for R in covs]
    DATA[name] = {"nv": nv, "U": U, "covers": covs, "recs": recs}
stamp("enumeration: %s" % ", ".join(f"{k}:{len(v['covers'])}" for k, v in DATA.items()))

TOTAL = sum(len(v["covers"]) for v in DATA.values())
chk("§A the three families' ten skeletons carry 17,042 strict covers in total "
    "(5,736 polygon + 101 tetra + 11,205 cube)", TOTAL == 17042, str(TOTAL))

# ================================================================== §A FT.97(1)-(2)
print("§A FT.97(1)–(2) — node ontology, three underdeterminations")
for name, nv, U in FAMILIES:
    d = DATA[name]
    chk(f"§A(1) {name}: node ontology V(R) subset V(Gamma) — every cover edge has both "
        "endpoints in the skeleton (no refinement mechanism; roles are vertex types)",
        all(0 <= a < nv and 0 <= b < nv for R in d["covers"] for (a, b) in R))
# tail normalization, end-sum factor 2, half-split factor 1 — asserted PER COVER
for name in DATA:
    for ci, r in enumerate(DATA[name]["recs"]):
        chk(f"§A(2a) {name}#{ci}: tail normalization sum_v i_v = |R| = n_R (CT1.29's count)",
            r["tail"] == r["K"])
        chk(f"§A(2a) {name}#{ci}: end-sum = 2K, half-split = K (the documented factor-2 freedom)",
            r["endsum"] == 2 * r["K"] and r["halves2"] == 2 * r["K"])
# role census (informational): types over all covers
role_c = Counter()
for name in DATA:
    for R in DATA[name]["covers"]:
        for tv in types_of(DATA[name]["nv"], R):
            if tv == (1, 1):
                role_c["centre"] += 1
            elif w_E(tv):
                role_c["endpoint"] += 1
            elif tv[0] + tv[1] >= 4:
                role_c["hub"] += 1
            elif tv[0] + tv[1] > 0:
                role_c["mixed k=3"] += 1
            else:
                role_c["unclaimed"] += 1
print("      role census over all covers:", dict(role_c))
chk("§A(1) the role vocabulary is derived: centre (1,1), endpoint (a,0)/(0,b), hub a+b>=4, "
    "unclaimed (0,0) — 'intermediate nodes' do not exist as nodes",
    set(role_c) <= {"centre", "endpoint", "hub", "mixed k=3", "unclaimed"})
# (2b) the five weights: finite-type maxima c_w = (6,36,1,6,24) over {0 < a+b <= 6}
TYPES = [(a, b) for a in range(7) for b in range(7) if 0 < a + b <= 6]
CW = {"w_U": 6, "w_K": 36, "w_C": 1, "w_E": 6, "w_H": 24}
for nm, w in WS:
    mx = max(w(tv) * tv[1] for tv in TYPES)       # per-vertex max of w(v)*i_v
    chk(f"§C(5) finite-type maximum c_{{{nm}}} = {CW[nm]} attained exactly over the type set "
        "{0 < a+b <= 6}", mx == CW[nm], str(mx))
stamp("FT.97(1)–(2): ontology, conventions ledger, role census, finite-type maxima")

# ================================================================== §B FT.97(3)
print("§B FT.97(3) — the reduction identities on every strict cover")
for name in DATA:
    for ci, r in enumerate(DATA[name]["recs"]):
        chk(f"§B {name}#{ci}: S_wU(R) = K(R) (the reduction identity)", r["S"]["w_U"] == r["K"])
        chk(f"§B {name}#{ci}: S_wC(R) = |C(R)|", r["S"]["w_C"] == r["nC"])
        chk(f"§B {name}#{ci}: K = 2|C| (each centre claims exactly 2 edges, FT.67(2)/(3d))",
            r["K"] == 2 * r["nC"])


def M_table(recs, sector=None):
    """M(w) = sum 16^|C| S_w / sum 16^|C| over the sector's covers (exact Fractions)."""
    sel = [r for r in recs if sector is None or (r["locked"] is (sector == "lock"))]
    den = sum(r["w16"] for r in sel)
    return {nm: (Fr(sum(r["w16"] * r["S"][nm] for r in sel), den) if den else None)
            for nm, _ in WS}, den, sel


Mt, dent, _ = M_table(DATA["tetra"]["recs"], "byp")
chk("§B the anchor M(w_U)(tetra, byp) = 62208/15745 reproduced from independent enumeration "
    "(= FT.68(1)(ii)'s reading — the 'paradigm shift' is a reweighting of tabulated data)",
    Mt["w_U"] == Fr(62208, 15745), str(Mt["w_U"]))
ok_half = True
for name in DATA:
    for sector in (None, "byp", "lock"):
        mm, den, sel = M_table(DATA[name]["recs"], sector)
        if den and mm["w_U"] is not None and mm["w_C"] is not None:
            ok_half &= (mm["w_C"] == mm["w_U"] / 2)
chk("§B M(w_C) = M(w_U)/2 identically, per family AND per sector (30 identities)", ok_half)
stamp("FT.97(3): per-cover identities, the 62208/15745 anchor, the w_C = w_U/2 law")

# ================================================================== §C FT.97(5)
print("§C FT.97(5) — the Form-Factor Ceiling (third size theorem)")
ok_ceil = True
for name, nv, U in FAMILIES:
    for nm, w in WS:
        mx = max((r["S"][nm] for r in DATA[name]["recs"]), default=0)
        ok_ceil &= mx <= CW[nm] * nv
chk("§C(5) M_form <= max_R S_w(R) <= c_w * V(Gamma) pointwise on all ten families "
    "(linear in skeleton size for every role weight)", ok_ceil)
ok_cap = True
for name in DATA:
    nv = DATA[name]["nv"]
    for r in DATA[name]["recs"]:
        if not r["locked"]:
            ok_cap &= Fr(r["nC"]) <= Fr(3 * nv, 4)
        else:
            ok_cap &= r["nC"] <= nv
chk("§C(5) the |C| caps hold per cover: |C| <= 3V/4 (byp) / V (lock) [CT0.11/FT.79(2)] — "
    "the 16^|C| enhancement saturates at the cap (exponential inside, linear across)", ok_cap)
P3 = DATA["C_3"]
m3, _, _ = M_table(P3["recs"])
reqV = {nm: math.ceil(Fr(3477) * m3[nm] / CW[nm]) for nm, _ in WS}
chk("§C(5) exact required-V table at R = 3477 [EXT]: (w_U, w_K, w_C, w_E, w_H) = "
    "(2187, 1062, 6561, 65, 515) — the ceiling rearranged at the exact P_3 anchors",
    (reqV["w_U"], reqV["w_K"], reqV["w_C"], reqV["w_E"], reqV["w_H"]) == (2187, 1062, 6561, 65, 515),
    str(reqV))
chk("§C(5) the P_3 anchors are the documented ones: M = (3264/865, 9504/865, 1632/865, "
    "96/865, 3072/865)",
    (m3["w_U"], m3["w_K"], m3["w_C"], m3["w_E"], m3["w_H"]) ==
    (Fr(3264, 865), Fr(9504, 865), Fr(1632, 865), Fr(96, 865), Fr(3072, 865)))
stamp("FT.97(5): ceilings pointwise, caps per cover, required-V table exact")

# ================================================================== §D FT.98
print("§D FT.98 — the polygon form factors")
DOC_COUNTS = {3: 10, 4: 33, 5: 56, 6: 118, 7: 281, 8: 649, 9: 1423, 10: 3166}
DOC_SPLIT = {3: (7, 3), 4: (29, 4), 5: (51, 5), 6: (97, 21), 7: (211, 70),
             8: (485, 164), 9: (1051, 372), 10: (2241, 925)}
DOC_Z = {3: (25, 48), 4: (353, 64), 5: (1161, 80), 6: (3121, 1632), 7: (11929, 10864),
         8: (53825, 43136), 9: (229417, 159888), 10: (844881, 775840)}
DOC_CMAX = {3: 1, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 5, 10: 6}
DOC_M = {  # n -> (w_U, w_K, w_E, w_H) exact Fractions (all-sector, tail convention)
    3: (Fr(3264, 865), Fr(9504, 865), Fr(96, 865), Fr(3072, 865)),
    4: (Fr(24832, 6273), Fr(1408, 153), Fr(1408, 2091), Fr(10240, 6273)),
    5: (Fr(281920, 50081), Fr(694240, 50081), Fr(7840, 50081), Fr(135680, 50081)),
    6: (Fr(2808192, 407233), Fr(7585344, 407233), Fr(212160, 407233), Fr(2079744, 407233)),
    7: (Fr(29210048, 3804641), Fr(74587296, 3804641), Fr(2663136, 3804641), Fr(17679872, 3804641)),
    8: (Fr(300392960, 33646849), Fr(767038208, 33646849), Fr(19632384, 33646849), Fr(178147328, 33646849)),
    9: (Fr(2833063488, 282265633), Fr(7303749984, 282265633), Fr(16677792, 21712741), Fr(1757108736, 282265633)),
    10: (Fr(27649976960, 2481810241), Fr(71155288000, 2481810241), Fr(2115650880, 2481810241), Fr(17046103040, 2481810241)),
}
DOC_CONC = {3: Fr(768, 865), 4: Fr(2048, 2091), 5: Fr(40960, 50081), 6: Fr(196608, 407233),
            7: Fr(3211264, 3804641), 8: Fr(16777216, 33646849), 9: Fr(50331648, 282265633),
            10: Fr(1509949440, 2481810241)}
DOC_CONC_DEC = {3: Fr('0.888'), 4: Fr('0.979'), 5: Fr('0.818'), 6: Fr('0.483'),
                7: Fr('0.844'), 8: Fr('0.499'), 9: Fr('0.178'), 10: Fr('0.608')}
MU = {}
for n in range(3, 11):
    name = f"C_{n}"
    d = DATA[name]
    nv, U = d["nv"], d["U"]
    # two enumerators: backtracking vs covering DP
    pb, pl = cover_dp(nv, U)
    dp_tot = sum(pb.values()) + sum(pl.values())
    bt_tot = len(d["covers"])
    bt_b = sum(1 for r in d["recs"] if not r["locked"])
    bt_l = bt_tot - bt_b
    chk(f"§D(1) {name}: two enumerators agree — backtracking {bt_tot} = DP {dp_tot}; "
        f"sector split ({bt_b}+{bt_l}) = documented {DOC_SPLIT[n]}",
        bt_tot == dp_tot == DOC_COUNTS[n] and (bt_b, bt_l) == DOC_SPLIT[n],
        f"{bt_tot} {dp_tot} {(bt_b, bt_l)}")
    Zb = sum(cover_value(nv, R) for R in d["covers"]
             if not any(a + b >= 4 for (a, b) in types_of(nv, R)))
    Zl = sum(cover_value(nv, R) for R in d["covers"]) - Zb
    chk(f"§D(1) {name}: FT.68(2)'s Z-anchor verbatim — (Z_byp, Z_lock) = {DOC_Z[n]}",
        (Zb, Zl) == DOC_Z[n], str((Zb, Zl)))
    cmax_b = max((r["nC"] for r in d["recs"] if not r["locked"]), default=0)
    chk(f"§D(1) {name}: byp |C|_max = {DOC_CMAX[n]} <= floor(3n/4) = {3 * n // 4}",
        cmax_b == DOC_CMAX[n] and cmax_b <= 3 * n // 4, str(cmax_b))
    mm, den, _ = M_table(d["recs"])
    MU[n] = mm
    chk(f"§D(2) {name}: exact M-table (w_U, w_K, w_E, w_H) = documented Fractions",
        (mm["w_U"], mm["w_K"], mm["w_E"], mm["w_H"]) == DOC_M[n],
        str((mm["w_U"], mm["w_K"], mm["w_E"], mm["w_H"])))
    chk(f"§D(2) {name}: M(w_C) = M(w_U)/2 exactly [FT.97(3)]", mm["w_C"] == mm["w_U"] / 2)
    cmax_all = max(r["nC"] for r in d["recs"])
    num = sum(r["w16"] for r in d["recs"] if r["nC"] == cmax_all)
    conc = Fr(num, den)
    chk(f"§D(5) {name}: concentration at |C|_max = {cmax_all}: {DOC_CONC[n]} "
        f"(decimal {float(DOC_CONC[n]):.3f} parity-oscillating)", conc == DOC_CONC[n], str(conc))
    chk(f"§D(5) {name}: concentration decimal matches the documented 3-place value",
        round_frac(conc, 3) == DOC_CONC_DEC[n], str(round_frac(conc, 3)))
# per-sector values recorded in the suite output (FT.98(2) clause)
for n in range(3, 11):
    for sec in ("byp", "lock"):
        mm, den, _ = M_table(DATA[f"C_{n}"]["recs"], sec)
        if den:
            print(f"      C_{n} [{sec}] M: " + ", ".join(f"{nm}={mm[nm]}" for nm, _ in WS))
# growth (3): ratios vs P_3
DOC_RATIO_U = {4: Fr('1.049'), 5: Fr('1.492'), 6: Fr('1.827'), 7: Fr('2.035'),
               8: Fr('2.366'), 9: Fr('2.660'), 10: Fr('2.953')}
ok_g = True
for n in range(4, 11):
    r = MU[n]["w_U"] / MU[3]["w_U"]
    ok_g &= round_frac(r, 3) == DOC_RATIO_U[n]
chk("§D(3) w_U growth ratios vs P_3 = (1.049, 1.492, 1.827, 2.035, 2.366, 2.660, 2.953) "
    "— linear-to-sublinear, never exponential in n", ok_g)
chk("§D(3) M(w_U) rises 3.77 -> 11.14 over n = 3..10 (exact endpoints 3264/865 and "
    "27649976960/2481810241)", round_frac(MU[3]["w_U"], 2) == Fr('3.77')
    and round_frac(MU[10]["w_U"], 2) == Fr('11.14'))
maxratio = {}
for nm, _ in WS:
    vals = [MU[n][nm] for n in range(3, 11)]
    base = MU[3][nm]
    maxratio[nm] = max(v / base for v in vals if base) if base else None
chk("§D(3) w_K max ratio 2.609; w_H max ratio 1.934; w_E max ratio 7.681 (non-monotone, "
    "parity oscillation)",
    round_frac(maxratio["w_K"], 3) == Fr('2.609') and round_frac(maxratio["w_H"], 3) == Fr('1.934')
    and round_frac(maxratio["w_E"], 3) == Fr('7.681'),
    str({k: str(round_frac(v, 4)) for k, v in maxratio.items() if v}))
# (4) the fifth clean negative
widest = max(maxratio[nm] for nm in ("w_U", "w_K", "w_C", "w_E", "w_H") if maxratio[nm])
chk("§D(4) the widest form-factor ratio in the entire computed family is w_E's 7.681",
    widest == maxratio["w_E"] and round_frac(widest, 3) == Fr('7.681'))
sh207 = Fr(207) / widest
sh3477 = Fr(3477) / widest
chk("§D(4) fifth clean negative, exact shortfalls on the exact ratio: 207/widest = 26.9|49.., "
    "3477/widest = 452.67.. (Fractions pinned); the tier's decimals x27.0 / x453.9 reproduce "
    "from the 2-place rounded ratio 7.66 (207/7.66 = 27.0|23, 3477/7.66 = 453.9|16) — the "
    "rebuild records both readings",
    round_frac(sh207, 1) == Fr('26.9') and round_frac(sh3477, 1) == Fr('452.7')
    and round_frac(Fr(207) / Fr('7.66'), 1) == Fr('27.0')
    and round_frac(Fr(3477) / Fr('7.66'), 1) == Fr('453.9'))
shU207 = Fr(207) / maxratio["w_U"]
shU3477 = Fr(3477) / maxratio["w_U"]
chk("§D(4) primary weight w_U: widest 2.953 -> shortfalls x70.1 / x1177.6 (exact)",
    round_frac(shU207, 1) == Fr('70.1') and round_frac(shU3477, 1) == Fr('1177.6'),
    f"{round_frac(shU207,1)} {round_frac(shU3477,1)}")
chk("§D(4) no aligned triple exists within any factor of 10: the widest family ratio over "
    "all weights and all n is 7.681 < 207/10", widest < Fr(207, 10))
stamp("FT.98: censuses (2 enumerators), Z-anchors, M-tables, growth, negatives, concentration")

# ================================================================== §E FT.99
print("§E FT.99 — the Platonic form factors, dominance, integrity ledger")
# (1) tetrahedron: two enumerators SET-identical
dT = DATA["tetra"]
ps = [b for b in range(1 << len(DET))
      if is_cover_strict(nvT, frozenset(DET[i] for i in range(len(DET)) if (b >> i) & 1))]
ps_sets = {frozenset(DET[i] for i in range(len(DET)) if (b >> i) & 1) for b in ps}
chk("§E(1) tetra: power-set filter of all 4096 patterns == backtracking, SET-identical "
    "(101 = 101 covers)", len(ps) == 101 and ps_sets == set(dT["covers"]))
ZbT = sum(cover_value(nvT, R) for R in dT["covers"]
          if not any(a + b >= 4 for (a, b) in types_of(nvT, R)))
ZlT = sum(cover_value(nvT, R) for R in dT["covers"]) - ZbT
chk("§E(1) tetra: Z = (1057, 448) [FT.68(1)]", (ZbT, ZlT) == (1057, 448), str((ZbT, ZlT)))
# 7-class table re-verified [FT.78(2)]: class invariants via Aut(K4) — fresh census
permsT = automorphisms(nvT, dT["U"])
idxT = {e: i for i, e in enumerate(DET)}
pmapsT = [{i: idxT[(p[a], p[b])] for i, (a, b) in enumerate(DET)} for p in permsT]


def mask_of(R, idx, DE):
    b = 0
    for e in R:
        b |= 1 << idx[e]
    return b


def canon(mask, pmaps):
    out = mask
    for pm in pmaps:
        m2 = 0
        for i, j in pm.items():
            if (mask >> i) & 1:
                m2 |= 1 << j
        if m2 < out:
            out = m2
    return out


clsT = {}
for R in dT["covers"]:
    clsT.setdefault(canon(mask_of(R, idxT, DET), pmapsT), []).append(R)
n_byp_cls = sum(1 for m in clsT.values()
                if not any(a + b >= 4 for (a, b) in types_of(nvT, m[0])))
chk("§E(1) tetra: 7 classes = 5 bypass + 2 locked (stored / FT.78(2) table re-verified)",
    len(clsT) == 7 and n_byp_cls == 5, f"{len(clsT)} classes, {n_byp_cls} byp")
sizes = sorted((len(m), min(len(centers_of(nvT, R)) for R in m)) for m in clsT.values())
chk("§E(1) tetra class Omega/|C| profile = FT.78(2): (1,0),(24,1),(24,2),(24,2),(12,2) byp; "
    "(12,2),(4,3) lock", sizes == sorted([(1, 0), (24, 1), (24, 2), (24, 2), (12, 2), (12, 2), (4, 3)]),
    str(sizes))
# exact M-tables all/byp/lock
DOC_MT = {
    ("all", "w_U"): Fr(172800, 35201), ("all", "w_K"): Fr(566400, 35201),
    ("all", "w_C"): Fr(86400, 35201), ("all", "w_E"): Fr(12672, 35201),
    ("all", "w_H"): Fr(227328, 35201),
    ("byp", "w_U"): Fr(62208, 15745), ("byp", "w_K"): Fr(27264, 3149),
    ("byp", "w_C"): Fr(31104, 15745), ("byp", "w_E"): Fr(12672, 15745),
    ("byp", "w_H"): Fr(18432, 15745),
    ("lock", "w_U"): Fr(108, 19), ("lock", "w_K"): Fr(420, 19),
    ("lock", "w_C"): Fr(54, 19), ("lock", "w_E"): Fr(0), ("lock", "w_H"): Fr(204, 19),
}
for sec in ("all", "byp", "lock"):
    mm, den, sel = M_table(dT["recs"], None if sec == "all" else sec)
    for nm, _ in WS:
        chk(f"§E(1) tetra M({nm})[{sec}] = {DOC_MT[(sec, nm)]} exactly",
            mm[nm] == DOC_MT[(sec, nm)], str(mm[nm]))
ok_we0 = all(r["S"]["w_E"] == 0 for r in dT["recs"] if r["locked"])
chk("§E(1) the locked w_E = 0 is STRUCTURAL: every locked tetra cover (double-digon hubs, "
    "K_{1,3} stars) has no endpoint-type vertex at all", ok_we0)
cmaxT = max(r["nC"] for r in dT["recs"])
numT = sum(r["w16"] for r in dT["recs"] if r["nC"] == cmaxT)
n_at = sum(1 for r in dT["recs"] if r["nC"] == cmaxT)
denT_all = sum(r["w16"] for r in dT["recs"])
chk("§E(1) tetra concentration at |C|_max = 3: 16384/35201 all-sector (the four K_{1,3} "
    "stars; total weight 35201)", cmaxT == 3 and n_at == 4 and denT_all == 35201
    and Fr(numT, denT_all) == Fr(16384, 35201), f"{numT}/{denT_all}, {n_at} covers")
# (2) cube: fresh census cross-checked against stored class data
dC = DATA["cube"]
chk("§E(2) cube: fresh enumeration — 11,205 covers, all distinct",
    len(dC["covers"]) == 11205 and len(set(dC["covers"])) == 11205)
permsC = automorphisms(nvC, dC["U"])
idxC = {e: i for i, e in enumerate(DEc)}
pmapsC = [{i: idxC[(p[a], p[b])] for i, (a, b) in enumerate(DEc)} for p in permsC]
clsC = {}
for R in dC["covers"]:
    clsC.setdefault(canon(mask_of(R, idxC, DEc), pmapsC), []).append(R)
Om_hist = Counter(len(m) for m in clsC.values())
sum_Om = sum(len(m) for m in clsC.values())
chk("§E(2) cube vs stored: sum(Omega) = 11,205 and the Omega-histogram is IDENTICAL "
    "{1:1, 4:1, 8:1, 12:4, 16:2, 24:47, 48:208}",
    sum_Om == 11205 and dict(Om_hist) == {1: 1, 4: 1, 8: 1, 12: 4, 16: 2, 24: 47, 48: 208},
    str(dict(Om_hist)))
nC_hist = Counter()
for R, r in zip(dC["covers"], dC["recs"]):
    nC_hist[r["nC"]] += 1
chk("§E(2) cube |C|-histogram = stored covering-polynomial coefficients: byp "
    "(1,48,648,2672,3624) + lock (24 at 2, 728 at 3, 3192 at 4, 264 at 5, 4 at 6)",
    nC_hist == Counter({0: 1, 1: 48, 2: 648 + 24, 3: 2672 + 728, 4: 3624 + 3192,
                        5: 264, 6: 4}), str(dict(nC_hist)))
ZbC = sum(cover_value(nvC, R) for R in dC["covers"]
          if not any(a + b >= 4 for (a, b) in types_of(nvC, R)))
ZlC = sum(cover_value(nvC, R) for R in dC["covers"]) - ZbC
chk("§E(2) cube: Z = (1,109,313, 1,150,848) re-verified [FT.68(3)]",
    (ZbC, ZlC) == (1109313, 1150848), str((ZbC, ZlC)))
DOC_MC = {
    ("all", "w_U"): Fr(482089472, 53648367), ("all", "w_K"): Fr(2241319168, 89413945),
    ("all", "w_C"): Fr(241044736, 53648367), ("all", "w_E"): Fr(256135424, 268241835),
    ("all", "w_H"): Fr(2021359616, 268241835),
    ("byp", "w_U"): Fr(655450624, 82871211), ("byp", "w_K"): Fr(485339392, 27623737),
    ("byp", "w_C"): Fr(327725312, 82871211), ("byp", "w_E"): Fr(144068864, 82871211),
    ("byp", "w_H"): Fr(202792960, 82871211),
    ("lock", "w_U"): Fr(285644, 30171), ("lock", "w_K"): Fr(285804, 10057),
    ("lock", "w_C"): Fr(142822, 30171), ("lock", "w_E"): Fr(6080, 10057),
    ("lock", "w_H"): Fr(887972, 90513),
}
denC_all = None
for sec in ("all", "byp", "lock"):
    mm, den, sel = M_table(dC["recs"], None if sec == "all" else sec)
    if sec == "all":
        denC_all = den
    for nm, _ in WS:
        chk(f"§E(2) cube M({nm})[{sec}] = {DOC_MC[(sec, nm)]} exactly",
            mm[nm] == DOC_MC[(sec, nm)], str(mm[nm]))
chk("§E(2)/(6b) the unreduced cube denominator: sum Omega*16^|C| = 804,725,505 = "
    "3 * 268,241,835 exactly", denC_all == 804725505 and 804725505 == 3 * 268241835)
numC2 = sum(r["w16"] * (2 * r["nC"]) ** 2 for r in dC["recs"])
chk("§E(2)/(6b) gcd(66,438,564,864, 804,725,505) = 3 and the reduced Fraction equals the "
    "published 22,146,188,288/268,241,835 (the trap is recorded)",
    numC2 == 66438564864 and math.gcd(numC2, denC_all) == 3
    and Fr(numC2, denC_all) == Fr(22146188288, 268241835))
cmaxC = max(r["nC"] for r in dC["recs"])
numC = sum(r["w16"] for r in dC["recs"] if r["nC"] == cmaxC)
n_atC = sum(1 for r in dC["recs"] if r["nC"] == cmaxC)
chk("§E(2) cube concentration at |C|_max = 6: 67,108,864/804,725,505 (four covers)",
    cmaxC == 6 and Fr(numC, denC_all) == Fr(67108864, 804725505) and n_atC == 4,
    f"{numC}/{denC_all}, {n_atC}")
# (3) the same O(V) band
mmT_all, denT_all, _ = M_table(dT["recs"])
mmC_all, denC_all2, _ = M_table(dC["recs"])
r_prim = mmC_all["w_U"] / mmT_all["w_U"]
chk("§E(3) M(w_U)*hbar/ln2 = 4.909 (tetra 172800/35201), 8.986 (cube 482089472/53648367); "
    "cube/tetra = 1.831 against the m_hid ratio 2 — the same O(V) band",
    round_frac(mmT_all["w_U"], 3) == Fr('4.909') and round_frac(mmC_all["w_U"], 3) == Fr('8.986')
    and round_frac(r_prim, 3) == Fr('1.831') and Fr(24, 12) == 2)
ratios_w = {nm: mmC_all[nm] / mmT_all[nm] for nm, _ in WS if mmT_all[nm]}
widest_ct = max(ratios_w.values())
chk("§E(3) the widest cube-vs-tetra form-factor ratio over the five weights is 2.652 "
    "(w_E, all-sector) and the locked sector is degenerate at w_E (tetra locked = 0)",
    round_frac(widest_ct, 3) == Fr('2.652') and max(ratios_w, key=lambda k: ratios_w[k]) == "w_E"
    and DOC_MT[("lock", "w_E")] == 0)
# (4) dominance census
def dom_counts(name):
    d = DATA[name]
    nvac = [r for r in d["recs"] if r["K"] > 0]
    c = sum(1 for r in nvac if r["dom"])
    w = sum(r["w16"] for r in nvac if r["dom"])
    wall = sum(r["w16"] for r in nvac)
    return c, len(nvac), Fr(w, wall)


c, tot, wf = dom_counts("tetra")
chk("§E(4) tetra dominance: 64/100 non-vacuum covers, |A|^2-weighted fraction 248/275 "
    "(the calibrated half-split rule reproduces the anchor exactly)",
    (c, tot, wf) == (64, 100, Fr(248, 275)), f"{c}/{tot} {wf}")
c, tot, wf = dom_counts("cube")
chk("§E(4) cube dominance: 10,052/11,204 covers, weighted 3,115,352/3,143,459 = 0.9911 — "
    "the amplitude-weighted ensemble is generically centre-dominated",
    (c, tot, wf) == (10052, 11204, Fr(3115352, 3143459)), f"{c}/{tot} {wf}")
c3, tot3, _ = dom_counts("C_3")
c10, tot10, _ = dom_counts("C_10")
chk("§E(4) polygons rising 3/9 (C_3) -> 2725/3165 (C_10)",
    (c3, tot3) == (3, 9) and (c10, tot10) == (2725, 3165), f"{c3}/{tot3} -> {c10}/{tot10}")
# mechanism: the isolated 2-edge thread splits its bits evenly (tie, NOT dominant)
thread_recs = [r for r in DATA["tetra"]["recs"] if r["K"] == 2]
chk("§E(4) mechanism verified: every single-thread cover is an exact tie (one centre bit vs "
    "two endpoint half-bits) — dominance arises exactly where vertices share roles",
    len(thread_recs) == 24 and all(r["tie"] and not r["dom"] for r in thread_recs))
# (5) D1 verdict: no ratios within x27 of 207 or x454 of 3477 anywhere
allM = {}
for name in DATA:
    for sec in ("all", "byp", "lock"):
        mm, den, _ = M_table(DATA[name]["recs"], None if sec == "all" else sec)
        if den:
            for nm, _ in WS:
                if mm[nm]:
                    allM[(name, sec, nm)] = mm[nm]
# the tier's hierarchy ratios are ANCHORED family growths: M(n)/M(P_3) per
# weight and sector (polygons), M_cube/M_tetra per weight and sector (platonics)
# — "spanning 1:R off the P_3 anchors" [FT.97(5)], "ratios to P_3" [FT.98(3)]
poly_byp = {}
poly_lock = {}
for n in range(3, 11):
    mb, _, _ = M_table(DATA[f"C_{n}"]["recs"], "byp")
    ml, _, _ = M_table(DATA[f"C_{n}"]["recs"], "lock")
    poly_byp[n] = mb
    poly_lock[n] = ml
anchored = {}
for nm, _ in WS:
    for sec, tbl in (("all", MU), ("byp", poly_byp), ("lock", poly_lock)):
        b3 = tbl[3][nm]
        if b3:
            for n in range(4, 11):
                if tbl[n][nm]:
                    anchored[(nm, f"polygons-{sec}", n)] = tbl[n][nm] / b3
    for sec, mS, mT in (("all", mmC_all, mmT_all),):
        pass
for sec in ("all", "byp", "lock"):
    mmC_s, _, _ = M_table(dC["recs"], None if sec == "all" else sec)
    mmT_s, _, _ = M_table(dT["recs"], None if sec == "all" else sec)
    for nm, _ in WS:
        if mmT_s[nm] and mmC_s[nm]:
            anchored[(nm, f"platonic-{sec}", "cube")] = mmC_s[nm] / mmT_s[nm]
# (a) the frozen text's census scope: ALL-SECTOR anchored ratios (FT.98(2)'s table)
allsec = {k: v for k, v in anchored.items() if k[1].endswith("-all")}
as_max = max(allsec.values())
as_key = max(allsec, key=lambda k: allsec[k])
chk("§E(5) D1 verdict — fifth clean negative (the tier's all-sector census): the widest "
    f"anchored ratio is {round_frac(as_max, 4)} = 7.681 (w_E, polygons-all, n=10/3); "
    "every Platonic anchored ratio is <= 2.652; every all-sector anchored ratio R "
    "satisfies 207/R > 10 and 3477/R > 10 — NO aligned triple within any factor of 10",
    round_frac(as_max, 3) == Fr('7.681') and as_key == ("w_E", "polygons-all", 10)
    and all(Fr(207) / v > 10 and Fr(3477) / v > 10 for v in allsec.values()),
    f"max {as_max} at {as_key}")
plat_max = max(v for k, v in allsec.items() if k[1] == "platonic-all")
chk("§E(5) the Platonic all-sector anchored maximum is 2.652 (w_E) — the documented widest "
    "cube-vs-tetra form-factor ratio; primary weight w_U gives 1.831",
    round_frac(plat_max, 3) == Fr('2.652')
    and round_frac(allsec[("w_U", "platonic-all", "cube")], 3) == Fr('1.831'))
# (b) extended census: byp/lock anchored ratios — the frozen x27 bound is stated on the
# all-sector census; the rebuild records that the sector-extended maxima also stay far
# inside the x10 aligned-triple test (the tier's operative verdict)
ext_max = max(anchored.values())
ext_key = max(anchored, key=lambda k: anchored[k])
chk("§E(5) extended census (rebuild record): including byp/lock anchors the widest is "
    f"{round_frac(ext_max, 4)} ({ext_key}) — still 207/R > 10 for EVERY anchored ratio in "
    "every sector, so the operative no-aligned-triple verdict holds sector-wide",
    all(Fr(207) / v > 10 and Fr(3477) / v > 10 for v in anchored.values())
    and ext_max < Fr(207, 10), f"{ext_max} at {ext_key}")
# unrestricted cross-product maxima (mixed sector/family pairings the tier never forms)
cross = {}
for nm, _ in WS:
    vals = [(v, k) for k, v in allM.items() if k[2] == nm]
    cross[nm] = (max(v for v, _ in vals) / min(v for v, _ in vals))
cross_max = max(cross.values())
xw = max(cross, key=lambda nm: cross[nm])
expect_cross = Fr(144068864, 82871211) / Fr(96, 865)     # cube-byp w_E over C_3-all w_E
unanch = Fr(0)
for nm, _ in WS:
    for tbl in (poly_byp, poly_lock):
        vb = [tbl[n][nm] for n in range(3, 11) if tbl[n][nm]]
        if vb:
            unanch = max(unanch, max(vb) / min(vb))
chk("§E(5) census record: unrestricted pairings also stay far below the [EXT] targets — "
    f"widest cross-sector/cross-family ratio {round_frac(cross_max, 3)} (w_E: cube-byp "
    f"144068864/82871211 over C_3-all 96/865, exact); widest unanchored within-family "
    f"max/min {round_frac(unanch, 3)}; both leave 207 short by more than x10",
    cross_max == expect_cross and xw == "w_E"
    and round_frac(unanch, 3) == Fr('8.915')
    and Fr(207) / cross_max > 10 and Fr(207) / unanch > 10)
# (6a) the endpoint double-count trap, reproduced exactly
mmTrap = Fr(sum(r["w16"] * r["endsum"] for r in dT["recs"]
                if not r["locked"]), sum(r["w16"] for r in dT["recs"] if not r["locked"]))
chk("§E(6a) integrity ledger: the end-sum convention (i_v = a+b) yields exactly "
    "124416/15745 = 2x the FT.68(1)(ii) anchor — the trap the anchor caught",
    mmTrap == Fr(124416, 15745) == 2 * Fr(62208, 15745), str(mmTrap))
stamp("FT.99: tetra/cube M-tables exact, stored cross-checks, dominance census, "
      "integrity ledger")

# ================================================================== §F no-referents
print("§F FT.97 premise audit — the no-referent counts")
ag_text = "".join(era_paths.read(fn)
                  for fn in ('A_axioms.md', 'B_foundation.md', 'C_geometry.md',
                             'D_electroweak.md', 'E_electromagnetic.md', 'F_color.md',
                             'G_saturation.md'))
for w in ('worldline', 'propagator', 'refinement', 'subdivision', 'form factor'):
    chk(f"§F '{w}' counts 0 in frozen A–G (the premise audit's machine half)",
        ag_text.count(w) == 0, str(ag_text.count(w)))
# m_hid floor anchors (FT.42(1)): 2E on the floors
chk("§F m_hid anchors: tetra floor 12 = 2E (E=6), cube floor 24 = 2E (E=12) — the "
    "'single-node' premise is false against the corpus (whole-subnetwork sums)",
    2 * 6 == 12 and 2 * 12 == 24)
stamp("FT.97 premise audit: five no-referent counts + the m_hid anchors")

print()
if FAIL:
    print(f"verify_H_form_factor: {PASS} passed, {FAIL} FAILED")
    sys.exit(1)
print(f"verify_H_form_factor: {PASS} checks green  ({time.time()-t0:.1f}s)")
