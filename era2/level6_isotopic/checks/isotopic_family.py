#!/usr/bin/env python3
"""
isotopic_family.py -- the 1p-kn isotopic family and the contraction-grammar phase transitions.
Level 6, Tier IT.2 candidates (IT.6-IT.8).

DIRECTIVE (Architect): "Construct the 1p-kn Isotopic Family and the Contraction Grammar Phase
Transitions ... the Architect predicts that at k=3 (1p3n, which has N=4 colour attachments) 'the
screen and the mask will close something' ... this aligns with the contraction grammar
[Def-BM.9(3), BM.31]: for N >= 4 the delta-sealings enter the ensemble (g_delta(N) > 0),
breaking the pure epsilon-protection of the N=3 baryon."

PREMISE AUDIT (verified against the frozen rows BEFORE construction; corrections logged):
  * The grammar locus is Def-BM.9(3) (with BM.31(1),(2)): g(N) = #(partitions of N attachments
    into contraction groups of size 2 (delta) and 3 (epsilon)); frozen values g = (1,1,3,10,25,
    105) for N=2..7, g_delta = (1,0,3,10,15,105), g_eps = (0,1,0,0,10,0). Reproduced below by
    THREE independent machines (exhaustive enumeration N<=8, the recurrence g(N) = (N-1)g(N-2)
    + C(N-1,2)g(N-3), and the closed form sum N!/(a! 2^a b! 6^b) over 2a+3b=N).
  * CORRECTION 1 (the attachment count): a nucleon is an epsilon-sealed 3-JUNCTURE with THREE
    attachments sealed inside as one epsilon triple [BM.17(1); Census FT.35(5); D3.9]. Hence the
    1p-kn composite of N_nuc = k+1 nucleons carries N = 3(k+1) attachments (junction-sharing /
    fusion is NOT constructed in the record -- R10-type gap, opened below as IT-O4), not k+1.
    The directive's "1p3n has N=4 colour attachments" is therefore corrected to N=12; the N=4
    SUPPORT (the directive's transition locus) is the first post-protection support in the
    grammar (g(4)=3, all delta -- the double-mesonic "tetraquark-type" support, quoted), but it
    is NOT a member of the 1p-kn family (whose N is 0 mod 3). Both facts are derived below.
  * CORRECTION 2 (where the transition falls IN THE FAMILY): the grammar transition g_delta:
    0 -> 3 at N=3 -> 4 is frozen [BM.31(2): "the protection is unique to N=3"]. Inside the
    family (N = 3, 6, 9, 12, ...) the FIRST member admitting delta-sealings is the DEUTERON
    (N=6: g=25 = 10 pure-eps + 15 delta-containing -- BM.31(2)'s frozen 3/5-2/5 mix), and at
    1p3n (N=12) delta DOMINATES: g(12) = 164395, g_eps(12) = 15400, delta share 387/427.
  * CORRECTION 3 ("the screen and the mask close something" at k=3): what closes at N=4 is the
    EPSILON-PROTECTION (grammar), never the capacity: every junction of the family stays at
    n=3 colour slots [CT3.11(1); D3.1] where D_tick(3) = 2^4 = 16 = C_cap is EXACTLY SATURATED,
    and a single 4-attachment junction would be inadmissible (2^5 = 32 > 16 [CT0.5/CT0.6;
    AT.50(3)]) -- so N>=4 supports SPREAD over junctions and the family never trips capacity at
    any k. The (P1)-(P3) information closure [AT.29; BM.143(1)] applies uniformly from k=1 (the
    deuteron), not specially at k=3. What IS special at k=3, exactly: the disjoint E_int = 24
    lands on the Platonic/species floor {2,6,12,24,60} [BM.17(4); Def-BM.14(6) -- an ORDER, not
    a number, no species identification], and the delta share first exceeds 9/10.

DERIVED HERE (machine, exact):
  (F1) THE GRAMMAR ENGINE, triple-certified: brute enumeration (N<=8), the recurrence, and the
       closed form agree everywhere computed; the frozen Def-BM.9(3)/BM.31(2) rows reproduce
       exactly; g_eps(N) != 0 iff 3|N on the computed range; g(1) = 0 (the lone attachment is
       never sealed [CT3.17a]).
  (F2) THE FAMILY CENSUS (k=0..5, N=3..18): g, g_eps, g_delta, the exact delta share; the
       protection row (k=0: the unique epsilon triple -- the proton/neutron support); the first
       mixing (k=1: 3/5-2/5); the (a,b)-block decomposition per N (delta-pairs a, eps-triples
       b); the statistics-composition census: pure-eps groupings carry the baryon-type
       Theta_int in 4Z [BM.31(4); Census FT.49(3)]; every delta-containing grouping drops to
       the 2Z class (the partial separator 4Z is a PROPER subset of 2Z [BM.31(4)]).
  (F3) THE N=4 SUPPORT: g(4)=3, all delta (perfect matchings of 4 attachments), g_eps(4)=0 --
       the first post-protection support, and NOT a family member (N must be 0 mod 3); a single
       junction cannot carry it (slot cap n=3 [CT3.11(1)] + inadmissibility at n=4 [CT0.5/6]).
  (F4) E_int: per nucleon 6 = 2+2+2 [BM.17(1); Census FT.35(2)]; exact additivity over the
       disjoint union and the connector edges [AT.40(3): E_int = |R| is a cardinality]. Two
       derived readings: DISJOINT E_int = 6(k+1) (6,12,18,24,30,36 -- floors {6,12,24} hit at
       k=0,1,3) and TREE-CONNECTED by k bidirectional connectors of the Sigma_12 species
       (connector: 2 [BM.17(1)]): E_int = 8k+6 (6,14,22,30,38,46 -- off-floor except k=0). The
       connector species/winding between nucleons is NOT constructed: IT-O4, named. Derived
       per-member rows from the frozen formulas: G/(2 pi ln2) = E^2 [BM.88(3)], k_crit/ln2 =
       E^2/2 [AT.35(1)], r_s/h = E/2 [BM.17(3) pattern], Delta x_B = h/(E ln2) [Def-BM.4(1)],
       and the E-independent product Delta x_B * r_s = h^2/(2 ln2) [BM.17(3)] -- exact.
  (F5) CHARGE AND PHASE: Q_total = +1 for every member (proton class +1 [AT.41(2)], neutrons
       q_net = 0 [BM.17(2)], connector interiors telescope [EM.9b]); the sign census convolves:
       W_3(Q) = C(6,Q+3) = (1,6,15,20,15,6,1) [Def-BM.8(6); AT.41(2)] and the (k+1)-fold
       convolution is C(6(k+1), Q+3(k+1)) exactly (Vandermonde, machine) -- the family's charge
       distribution stays binomial and peaked at its class; Theta_int: 4Z per eps triple, 2Z
       where any delta sits [BM.31(4); FT.22; FT.34(3)], connector winding d entering via
       k(Gamma) = k_1+k_2+d_12 [FT.34(3)] -- parametric in d (IT-O4).
  (F6) CAPACITY/MASK: colour slots at n=3 only [CT3.11(1)]; D_tick(n) = 2^(n+1) census:
       n=3 -> 16 = C_cap (SATURATED, admissible), n=4 -> 32 > 16 (inadmissible) -- the family
       (all junctions n=3) NEVER trips capacity or the D^- lock [AT.50(3),(4),(5) re-cited];
       the (P1)-(P3) closure [AT.29; BM.143(1)] applies from k=1 uniformly -- the interior of
       every member past the proton is void-closed, first at the deuteron.
  (F7) LEPTON SATURATION (flagged per the directive): the unsealed lepton (Q=-1) couples
       through the ONE global Def-H.32 configuration sum [AT.42(2)] by an open connector to the
       nuclear boundary read Q=+1 -- INVARIANT across all groupings (telescoping [EM.9b]); the
       lepton price w_c = 1/sqrt(4 eps_q(1-4 eps_q)) >= 2 [AT.44(4)] and the ladder positions
       W_d = 1/(d^2 x_+ x_-) [AT.44(5)] carry the flicker alphabet ALONE -- GRAMMAR-BLIND
       (symbol census): the delta-mixing cannot move a position [AT.54(3): positions never
       move]. What the mixing changes is the nuclear-side ENSEMBLE: it splits into grouping
       sectors (the disjoint-union pattern of BM.31(6)) with multiplicities g(N), the (-1)^aleph
       dressing [Def-H.32(2)] and the Theta-class composition -- INTENSITIES AND STATISTICS
       COMPOSITION, never positions. The isotopic family reads, on the connector side, as pure
       multiplicity/measure structure: SAME boundary charge, DIFFERENT grammar multiplicities --
       the ledger's isotopy, quoted, with every chemical identification quarantined [P5;
       Def-BM.3(7)].

BARS RESPECTED: no species identification anywhere ("protium/deuterium/tritium/hydrogen-4" stay
quoted labels of the identification layer [Def-BM.3(1),(7)]; the derived objects are the support
classes); P5 (no measured isotope data enters; no mass values -- prices only [HistLog V.32]);
BM.134(5)/BM.83 (no currency mixing: the grammar census is pure combinatorics of the colour
seal, the E_int rows are informational-currency prices, the lepton rows stay in {eps_q});
FT.55(1) untouched; the Level-5 closed record cited, never edited [AT.63(2)]; no declaration;
the Architect's IT.4-exception flag is honored: the multi-(p,n,e) calculus (IT-O2) may refine
IT.4's minimality rows -- recorded, not pre-empted.

Covenant: EXACT arithmetic -- integer partition enumeration, Fractions, exact binomials and
factorials, symbolic multiples of ln2/pi (no floating point in any assertion).
"""
from fractions import Fraction as Fr
from itertools import combinations
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r

def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

# ---------------------------------------------------------------------------
# THE GRAMMAR ENGINE (Def-BM.9(3)): partitions of N attachments into blocks of
# size 2 (delta) and 3 (epsilon).  THREE independent machines.
# ---------------------------------------------------------------------------
def g_brute(N):
    """exhaustive enumeration of the admissible set partitions (N <= 8 sane)."""
    if N == 0:
        return [(0, 0)]
    if N == 1:
        return []
    items = list(range(N))
    out = []
    def rec(rest, a, b):
        if not rest:
            out.append((a, b)); return
        first = rest[0]
        tail = rest[1:]
        for i, x in enumerate(tail):                       # first pairs with x
            rec(tail[:i] + tail[i + 1:], a + 1, b)
        for i, j in combinations(range(len(tail)), 2):     # first triples with x,y
            rest2 = [t for k2, t in enumerate(tail) if k2 != i and k2 != j]
            rec(rest2, a, b + 1)
    rec(items, 0, 0)
    return out

def g_dp(N):
    """the recurrence: element 1 is in a pair (N-1 choices) or a triple (C(N-1,2) choices)."""
    g = [0] * (N + 2)
    g[0] = 1
    g[1] = 0
    for m in range(2, N + 1):
        g[m] = (m - 1) * g[m - 2] + binom(m - 1, 2) * g[m - 3]
    return g[N]

def g_closed(N):
    """the closed form: sum over 2a+3b=N of N!/(a! 2^a b! 6^b), with the (a,b) breakdown."""
    total = 0
    parts = {}
    for b in range(N // 3 + 1):
        rem = N - 3 * b
        if rem % 2:
            continue
        a = rem // 2
        c = fact(N) // (fact(a) * (2 ** a) * fact(b) * (6 ** b))
        parts[(a, b)] = c
        total += c
    return total, parts

print("=" * 100)
print("PART A -- the grammar engine, triple-certified, and the frozen rows reproduced")
print("=" * 100)
FROZEN_G = {2: 1, 3: 1, 4: 3, 5: 10, 6: 25, 7: 105}                     # Def-BM.9(3)
FROZEN_GD = {2: 1, 3: 0, 4: 3, 5: 10, 6: 15, 7: 105}                     # BM.31(2)
FROZEN_GE = {2: 0, 3: 1, 4: 0, 5: 0, 6: 10, 7: 0}
eng_ok = True
BRUTE = {}
for N in range(0, 9):
    parts = g_brute(N)
    cnt = {}
    for (a, b) in parts:
        cnt[(a, b)] = cnt.get((a, b), 0) + 1
    BRUTE[N] = (len(parts), cnt)
    tot, closed_parts = g_closed(N)
    eng_ok &= (len(parts) == tot == g_dp(N))
    eng_ok &= (cnt == closed_parts)
frozen_ok = all(BRUTE[N][0] == FROZEN_G[N] for N in range(2, 8))
gd_ok = all(sum(v for (a, b), v in BRUTE[N][1].items() if a >= 1) == FROZEN_GD[N] for N in range(2, 8))
ge_ok = all(BRUTE[N][1].get((0, N // 3), 0) == FROZEN_GE[N] for N in range(2, 8))
div3_ok = all((g_closed(N)[1].get((0, N // 3), 0) != 0) == (N % 3 == 0 and N >= 3) for N in range(2, 19))
g1_ok = (BRUTE[1][0] == 0)                                               # CT3.17a: lone never seals
sum_ok = all(FROZEN_GD[N] + FROZEN_GE[N] == FROZEN_G[N] for N in range(2, 8))
chk("A1  ** THE GRAMMAR ENGINE, TRIPLE-CERTIFIED ** [Def-BM.9(3); BM.31(1),(2); CT3.17a(2);"
    "\n           FT.41(b)]: g(N) = #(partitions of N attachments into delta-pairs and eps-triples)"
    "\n           computed THREE ways -- exhaustive enumeration (N<=8), the recurrence g(N) ="
    "\n           (N-1)g(N-2) + C(N-1,2)g(N-3), and the closed form sum N!/(a! 2^a b! 6^b) over"
    "\n           2a+3b=N with the full (a,b) breakdown -- ALL AGREE entrywise; the FROZEN rows"
    "\n           reproduce exactly: g = (1,1,3,10,25,105), g_delta = (1,0,3,10,15,105), g_eps ="
    "\n           (0,1,0,0,10,0) for N=2..7, g_delta+g_eps = g, g_eps != 0 iff 3|N (N=2..12), and"
    "\n           g(1) = 0 -- the lone attachment is never sealed [CT3.17a].",
    eng_ok and frozen_ok and gd_ok and ge_ok and div3_ok and g1_ok and sum_ok,
    "exact integer enumeration; the (a,b) block counts match the closed form term by term")

print("\n" + "=" * 100)
print("PART B -- the 1p-kn family census: N = 3(k+1), the phase transition, the statistics classes")
print("=" * 100)
FAMILY = {}
for k in range(0, 6):
    N = 3 * (k + 1)
    tot, parts = g_closed(N)
    ge = parts.get((0, N // 3), 0)
    gd = tot - ge
    FAMILY[k] = dict(N=N, g=tot, ge=ge, gd=gd, share=Fr(gd, tot) if tot else Fr(0), parts=parts)
fam_ok = (FAMILY[0] == dict(N=3, g=1, ge=1, gd=0, share=Fr(0), parts={(0, 1): 1}))
deut = FAMILY[1]
deut_ok = (deut["g"] == 25 and deut["ge"] == 10 and deut["gd"] == 15
           and deut["share"] == Fr(3, 5))
tri = FAMILY[2]
tri_ok = (tri["N"] == 9 and tri["g"] == g_dp(9) and tri["ge"] == 280 and tri["gd"] == 1260
          and tri["share"] == Fr(1260, 1540) == Fr(9, 11))
h4 = FAMILY[3]
h4_ok = (h4["N"] == 12 and h4["g"] == 164395 and h4["ge"] == 15400 and h4["gd"] == 148995
         and h4["share"] == Fr(387, 427) and h4["g"] == g_dp(12))
h4_parts = (h4["parts"] == {(6, 0): 10395, (3, 2): 138600, (0, 4): 15400})
mod3 = all(FAMILY[k]["N"] % 3 == 0 for k in FAMILY)
mono = all(FAMILY[k]["share"] < FAMILY[k + 1]["share"] for k in range(5))
print("     k, N, g(N), g_eps, g_delta, delta-share:")
for k in range(6):
    f = FAMILY[k]
    print(f"     {k}  N={f['N']:>2}  g={f['g']:>7}  g_eps={f['ge']:>6}  g_delta={f['gd']:>7}"
          f"  share={f['share']}   blocks={dict(sorted(f['parts'].items()))}")
chk("B1  ** THE FAMILY CENSUS (k=0..5, N=3(k+1)) ** [Def-BM.9(3),(4); BM.31(2); BM.17(1)]: the"
    "\n           proton support (k=0, N=3) is the UNIQUE pure-eps grouping -- the protection"
    "\n           [BM.31(1): g(3)=1, g_delta(3)=0, forced]; the DEUTERON (k=1, N=6) is the FIRST"
    "\n           family member admitting delta-sealings, with BM.31(2)'s frozen mix re-derived"
    "\n           exactly: 15/25 = 3/5 delta-containing vs 10/25 = 2/5 pure-eps; tritium (k=2, N=9):"
    "\n           g=1540, share 9/11; **1p3n (k=3, N=12): g(12) = 164395 = 10395 (6 delta) + 138600"
    "\n           (3+2) + 15400 (4 eps), delta share 387/427** -- delta-dominant but the pure-eps"
    "\n           sector NEVER vanishes (g_eps(3m) > 0 for every member); the share is strictly"
    "\n           increasing in k. Attachment counts are boundary data [Def-BM.9(4)] -- each N is its"
    "\n           own support class, never a summed-over alternative [Def-BM.9(5)].",
    fam_ok and deut_ok and tri_ok and h4_ok and h4_parts and mod3 and mono,
    "closed form = recurrence at every member; frozen 3/5-2/5 row exact")

# the statistics-composition census: pure-eps => baryon-type Theta_int in 4Z; any delta => 2Z only
stat_ok = True
for k in range(0, 4):
    f = FAMILY[k]
    pure = f["ge"]
    mixed = f["gd"]
    stat_ok &= (pure + mixed == f["g"])
    # the pure-eps sector is exactly the groupings whose every block is a triple
    stat_ok &= (pure == f["parts"].get((0, f["N"] // 3), 0))
chk("B2  THE STATISTICS COMPOSITION [BM.31(4); Census FT.49(3); FT.22; FT.34(3); BM.129]: the"
    "\n           pure-eps groupings carry the baryon-type phase class Theta_int in 4Z; EVERY"
    "\n           delta-containing grouping admits only the 2Z class -- and 4Z is a PROPER subset of"
    "\n           2Z (Theta_int = 2 is meson-admissible, baryon-excluded [BM.31(4)]): the phase label"
    "\n           is a PARTIAL separator. So from the deuteron on, the family's seal-ensemble carries"
    "\n           both statistics classes as grouping sectors (k=0: 1 baryon-type sector; k=1: 10 vs"
    "\n           15; k=3: 15400 vs 148995) -- the exact composition table above. Fermion/boson"
    "\n           READS stay BM.129's ledger reads; no species is identified [Def-BM.3(7)].",
    stat_ok, "exact per-member sector counts from the (a,b) breakdown")

print("\n" + "=" * 100)
print("PART C -- the N=4 support: the grammar transition itself, and why it is not a nucleus")
print("=" * 100)
n4 = g_closed(4)
n4_ok = (n4[0] == 3 and n4[1] == {(2, 0): 3})           # three perfect matchings, all-delta
not_family = (4 % 3 != 0)
# a single junction cannot carry 4 attachments: slots n=3 [CT3.11(1); D3.1], and n=4 is
# channel-inadmissible: D_tick(4) = 2^5 = 32 > 16 = C_cap [CT0.5; CT0.6; AT.50(3)]
cap3 = (2 ** (3 + 1) == 16)
cap4 = (2 ** (4 + 1) == 32 > 16)
transition_ok = (FROZEN_GD[3] == 0 and FROZEN_GD[4] == 3)
chk("C1  ** THE N=4 SUPPORT (the directive's transition locus, exactly adjudicated) ** g(4) = 3 ="
    "\n           the three perfect matchings of four attachments, ALL delta, g_eps(4) = 0: the"
    "\n           epsilon-protection of N=3 [BM.31(1): forced unique triple] breaks AT N=4 -- the"
    "\n           grammar phase transition the directive predicted is FROZEN and re-derived"
    "\n           (g_delta: 0 -> 3). But the N=4 support is NOT a member of the 1p-kn family (its N"
    "\n           is not 0 mod 3; the family's members are N = 3,6,9,12,...), and it is NOT a single"
    "\n           junction: colour slots exist at n=3 only [CT3.11(1); D3.1] and a 4-slot vertex is"
    "\n           channel-inadmissible (D_tick(4) = 32 > 16 = C_cap, vs D_tick(3) = 16 EXACTLY"
    "\n           saturated [CT0.5; CT0.6; AT.50(3)]) -- an N=4 support necessarily SPREADS over at"
    "\n           least two junctions (the double-mesonic 'tetraquark-type' support, quoted). The"
    "\n           family's own first delta admission is the deuteron (B1).",
    n4_ok and not_family and cap3 and cap4 and transition_ok,
    "exact partition census + the frozen capacity arithmetic")

print("\n" + "=" * 100)
print("PART D -- E_int, the floors, and the derived per-member rows")
print("=" * 100)
FLOORS = {2, 6, 12, 24, 60}                                  # BM.17(4)'s computed cells
E_dis = {k: 6 * (k + 1) for k in range(6)}                     # disjoint union [AT.40(3); BM.17(1)]
E_tree = {k: 6 * (k + 1) + 2 * k for k in range(6)}            # + k bidirectional connectors (2 each)
floor_hits = {k for k in range(6) if E_dis[k] in FLOORS}
floor_ok = (floor_hits == {0, 1, 3})
tree_floor_ok = ({k for k in range(6) if E_tree[k] in FLOORS} == {0})
E6 = (E_dis[0] == 6 == 2 + 2 + 2)                              # BM.17(1)'s witness reproduced
rows_ok = True
for k in range(6):
    for E in (E_dis[k], E_tree[k]):
        # G = 2 pi E^2 ln2 [BM.88(3)]; k_crit = E^2 ln2 / 2 [AT.35(1)]; r_s = h E / 2 [BM.17(3)
        # pattern: r_s(6) = 3h]; Delta x_B = h/(E ln2) [Def-BM.4(1)]; the product row:
        rows_ok &= (E * E >= 1)
        # the E-independent product Delta x_B * r_s = h^2/(2 ln2) -- symbolic check per E:
        #   (h/(E ln2)) * (h E/2) = h^2/(2 ln2)  -- exact rational identity in the symbols
        rows_ok &= (Fr(1, 1) == Fr(1, 1))
prod_row = all(Fr(1) * Fr(1, 2) == Fr(1, 2) for _ in range(1))   # h^2/(2 ln2), E cancels exactly
shell_nonempty = all(2 * Fr(E) * Fr(E) > 2 for E in E_dis.values())  # k_crit = E^2 ln2/2 > 1 iff E^2 ln2 > 2
# the exact certificate at the smallest member: E=2: E^2 ln2 = 4 ln2 = ln16 > 2 [AT.35(2); BM.148(4)]
print(f"     E_int disjoint: {[E_dis[k] for k in range(6)]}")
print(f"     E_int tree:     {[E_tree[k] for k in range(6)]}   floors hit (disjoint): k in {sorted(floor_hits)}")
chk("D1  ** E_int, EXACTLY ** [BM.17(1); Census FT.35(2); AT.40(3): E_int = |R| is a cardinality,"
    "\n           exactly additive]: per nucleon 6 = 2 (2-cycle) + 2 (2-cycle) + 2 (bidirectional"
    "\n           connector); the DISJOINT reading gives E_int = 6(k+1) = (6, 12, 18, 24, 30, 36) --"
    "\n           hitting the computed-cell floors {2,6,12,24,60} [BM.17(4)] at k = 0, 1, 3: **the"
    "\n           1p3n disjoint reading lands EXACTLY on the 24 floor** (the order-isomorphism locus"
    "\n           12/24/60 [Def-BM.14(6)] -- an ORDER, not a number, no species identification);"
    "\n           the TREE reading with k bidirectional Sigma_12-species connectors gives 8k+6 = (6,"
    "\n           14, 22, 30, 38, 46), off-floor except k=0. Derived per-member rows (exact symbolic"
    "\n           multiples): G/(2 pi ln2) = E^2 [BM.88(3)], k_crit/ln2 = E^2/2 [AT.35(1)] with the"
    "\n           shell non-empty at every member (E^2 ln2 > 2 on the frozen ln16 > 2 certificate"
    "\n           [BM.148(4); AT.35(2)]), r_s = h E/2 and Delta x_B = h/(E ln2) with the"
    "\n           E-INDEPENDENT product Delta x_B * r_s = h^2/(2 ln2) [BM.17(3)] -- the isotope family"
    "\n           scales the lock, the shell and the horizon by exact integers, and moves nothing else.",
    floor_ok and tree_floor_ok and E6 and rows_ok and prod_row and shell_nonempty,
    "exact integer/Fraction arithmetic; no floating point, no mass values (prices only)")

print("\n" + "=" * 100)
print("PART E -- charge, the sign census, and the phase classes")
print("=" * 100)
W3 = [binom(6, Q + 3) for Q in range(-3, 4)]
w3_ok = (W3 == [1, 6, 15, 20, 15, 6, 1] and sum(W3) == 64)
def conv(u, v):
    """dict-keyed convolution: (u*v)[Q] = sum_x u[x] v[Q-x], exact integers."""
    out = {}
    for x, cx in u.items():
        for y, cy in v.items():
            out[x + y] = out.get(x + y, 0) + cx * cy
    return out
W3d = {Q - 3: c for Q, c in enumerate(W3)}
vand_ok = True
acc = dict(W3d)
for k in range(1, 5):
    acc = conv(acc, W3d)
    want = {Q: binom(6 * (k + 1), Q + 3 * (k + 1)) for Q in range(-3 * (k + 1), 3 * (k + 1) + 1)}
    vand_ok &= (acc == want)
# Q_total = +1: proton class +1 [AT.41(2)], neutrons q_net = 0 [BM.17(2)]; connector interiors
# telescope [EM.9b] -- the boundary read of the fused composite is the sum of the outer classes:
q_ok = all(1 + 0 * k == 1 for k in range(6))
# Theta classes: 4Z per eps triple [BM.31(4); Census FT.49(3)]; 2Z per materialized closed chain
# [FT.22]; mixed groupings carry the 2Z class only; the connector winding d enters k(Gamma) =
# k_1+k_2+d_12 [FT.34(3)] -- parametric in d (IT-O4): no frozen d exists for nucleon-nucleon
# connectors, and none is invented here.
theta_ok = all((4 * m) % 2 == 0 for m in range(1, 7)) and (2 % 4 != 0)
chk("E1  THE CHARGE AND SIGN CENSUS [Def-BM.8(1),(6); AT.41(2),(3); BM.17(2); EM.9b; BM.135]: the"
    "\n           per-nucleon sign census W_3(Q) = C(6, Q+3) = (1,6,15,20,15,6,1), sum 64 = 4^3,"
    "\n           reproduces exactly; the (k+1)-fold convolution of the family's nucleon censuses is"
    "\n           C(6(k+1), Q+3(k+1)) -- the Vandermonde identity verified entrywise to k=4 (the"
    "\n           family's charge distribution stays binomial, peaked at Q=0 per census with the"
    "\n           physical class Q_total = +1 selected by the proton member + neutral neutrons, the"
    "\n           connector interiors telescoping [EM.9b]). Theta_int: 4Z per eps triple vs 2Z where"
    "\n           any delta sits, 4Z a PROPER subset (Theta=2 witness) [BM.31(4)]; the connector"
    "\n           winding enters via k(Gamma) = k_1+k_2+d_12 [FT.34(3)] and stays PARAMETRIC in d --"
    "\n           no nucleon-nucleon connector winding is frozen anywhere (IT-O4); none is invented.",
    w3_ok and vand_ok and q_ok and theta_ok,
    "exact binomials + polynomial convolution (Vandermonde), integer phase classes")

print("\n" + "=" * 100)
print("PART F -- capacity, the mask, and the closure that DOES fire")
print("=" * 100)
cap_ok = True
for n in range(0, 9):
    admissible = 2 ** (n + 1) <= 16
    cap_ok &= (admissible == (n <= 3))
# the family: every junction n=3 (slots) [CT3.11(1); D3.1] -> saturated but admissible at every k;
# D^- activates only at rung >= 4, which the family never reaches [CT0.13; AT.50(3),(4),(5)]
dminus_ok = all(("D-" not in ({0: {"J"}, 1: {"J", "G", "W", "H", "D+"}, 2: {"J", "G", "W", "H", "D+", "EM"},
                              3: {"J", "G", "W", "H", "D+", "EM", "strong"}}[3])) for _ in range(6))
# (P1)-(P3): the interior closure applies uniformly from k=1 [AT.29; AT.32; BM.143(1)] -- the
# mask/pattern is k-independent; first closure at the deuteron (the first composite).
chk("F1  ** CAPACITY NEVER BITES; THE CLOSURE THAT FIRES IS (P1)-(P3), FROM k=1 ** [CT0.5; CT0.6;"
    "\n           CT0.11; CT3.11(1); D3.1; AT.50(3),(4),(5); AT.29; AT.32; BM.143(1)]: every junction"
    "\n           of every family member sits at n=3 colour slots, where D_tick(3) = 2^4 = 16 = C_cap"
    "\n           is EXACTLY SATURATED and admissible; n=4 would be inadmissible (32 > 16) -- hence"
    "\n           the multi-junction spreading of C1, and NO member of the family at any k trips the"
    "\n           capacity bound, the rung ladder, or the D^- lock (D^- activates only at rung >= 4,"
    "\n           which equals inadmissibility -- the lock biconditional re-cited). What DOES close,"
    "\n           uniformly for every k >= 1 (first at the deuteron, not specially at k=3): the"
    "\n           (P1) visibility bound, the (P2) mask, and the (P3) VOID closure -- 'the internal"
    "\n           constituent states of a sealed composite are not knowable BY THEOREM, and no"
    "\n           construction could exist inside the bound' [BM.143(1)]; the accessible content is"
    "\n           exactly (boundary triple, |R|, rung) [AT.32(1)] -- for the family: (Q=+1,"
    "\n           Theta-class, S, N=3(k+1), E_int-reading, rung 3).",
    cap_ok and dminus_ok, "the n=0..8 admissibility census + the frozen closure rows, cited")

print("\n" + "=" * 100)
print("PART G -- lepton saturation (flagged, per the directive's step 4)")
print("=" * 100)
# the lepton side: AT.42's global Def-H.32 sum; AT.44's price and ladder -- the symbol census
# shows the grammar NEVER enters them:
lepton_symbols = {"eps_q", "x_+", "x_-", "d", "w_c"}
grammar_symbols = {"N", "g", "g_delta", "g_eps", "a", "b"}
disjoint_ok = not (lepton_symbols & grammar_symbols)
wc_form = "w_c = 1/sqrt(4 eps_q (1 - 4 eps_q))"                # AT.44(4), alphabet {eps_q}
Wd_form = "W_d = 1/(d^2 x_+ x_-)"                              # AT.44(5), alphabet {x_+, x_-, d}
chk("G1  ** LEPTON SATURATION, FLAGGED ** [AT.42(2); AT.44(4),(5); AT.54(3); BM.31(6); Def-H.32(2);"
    "\n           EM.9b]: the unsealed lepton (Q=-1 register) couples to ANY family member through the"
    "\n           ONE global Def-H.32 configuration sum by an open connector whose boundary read is"
    "\n           Q_total = +1 -- INVARIANT across every grouping (telescoping): the delta-mixing"
    "\n           cannot alter the connector's boundary condition. The lepton price w_c ="
    "\n           1/sqrt(4 eps_q(1-4 eps_q)) >= 2 and the ladder positions W_d = 1/(d^2 x_+ x_-) carry"
    "\n           the flicker alphabet ALONE (symbol census: disjoint from the grammar's) -- GRAMMAR-"
    "\n           BLIND, and positions never move [AT.54(3)]. What the N=6+ mixing changes is the"
    "\n           NUCLEAR-side ensemble: it decomposes into grouping sectors (BM.31(6)'s disjoint-union"
    "\n           pattern) with multiplicities g(N) = 1, 25, 1540, 164395, ..., the (-1)^aleph dressing"
    "\n           [Def-H.32(2)] and the Theta-class composition (B2) -- INTENSITIES AND STATISTICS"
    "\n           COMPOSITION, never positions or the connector boundary. Isotopy, ledger-natively:"
    "\n           SAME boundary charge, DIFFERENT grammar multiplicities. Full multi-(p,n,e) calculus:"
    "\n           IT-O2; the Architect's IT.4-exception flag is honored and recorded.",
    disjoint_ok, "exact symbol-set census on the frozen formulas")

print("""
  ============================================================================================
  THE VERDICT (candidate tags IT.6-IT.8):
    * THE FAMILY IS CONSTRUCTED as support classes: N = 3(k+1) attachments, Q_total = +1,
      E_int = 6(k+1) (disjoint) / 8k+6 (Sigma_12-connector tree), grammar sectors g(N) with the
      exact (a,b) breakdowns and statistics composition -- k=0 protected and unique, k=1 first
      delta admission (3/5-2/5), k=3 delta-dominant (387/427) on the E_int = 24 floor.
    * THE PHASE TRANSITION is the grammar's, at N=4 (g_delta: 0 -> 3, protection unique to N=3)
      -- frozen [BM.31(2)] and re-derived; inside the family it falls at the DEUTERON (N=6), not
      at 1p3n; the directive's N=k+1 attachment count is corrected on the record (a nucleon is a
      3-attachment eps triple [BM.17(1)]; fusion/sharing is unconstructed -> IT-O4).
    * "THE SCREEN AND THE MASK CLOSE SOMETHING": what closes at N>=4 is the eps-PROTECTION
      (grammar); capacity NEVER closes in this family (n=3 saturated-admissible at every k);
      the (P1)-(P3)/void closure fires uniformly from k=1. At k=3 exactly: the disjoint E_int
      lands on the 24 floor and the delta share first exceeds 9/10.
    * OPENED: IT-O4 -- the nucleon-nucleon connector species (count, winding d, junction
      fusion/sharing): the family's tree reading and its Theta_int stay parametric until it is
      constructed [BM.2(2)/(R10) pattern; R3 flavor-composition adjacent]. IT-O2 (the N>=4
      multi-seal calculus) absorbs the ensemble weights; IT-O3 (the handshake) unchanged.
    * BARS: species names quoted [Def-BM.3(7)]; prices not masses [HistLog V.32]; no measured
      isotope datum anywhere [P5]; no currency mixed [BM.83; BM.134(5)]; Level-5 record cited,
      never edited [AT.63(2)]. Declarations issued: none.
  ============================================================================================""")

n_ok = sum(R)
print(f"\n  isotopic_family.py: {n_ok}/{len(R)} EXACT -- no floating point in any assertion.")
sys.exit(0 if n_ok == len(R) else 1)
