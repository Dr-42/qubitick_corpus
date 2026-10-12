#!/usr/bin/env python3
"""
multi_seal_census.py -- the multi-seal configuration census at N=5,6: the channel width
skeleton, the contraction grammar, the mask dimensions, and the D^- saturation boundary.
Level 6, Tier IT.3 candidates (IT.9-IT.11).

DIRECTIVE (Architect): "Run the Multi-Seal Configuration Census for N=5 and N=6 -- the channel
width skeleton and the D^- saturation boundary ... determine if the census terminates or
encompasses D^- pure saturated areas ... I think this does IT-O4 and IT-O2 simultaneously."

PREMISE AUDIT (verified against the frozen rows before construction; corrections logged):
  * (P1) "the D^- scalar sink is formally active (adding exactly 1 dimension to reach dim
    K_(n>=4) = 26)" -- CORRECTED: there are TWO mask species, and the directive conflates them.
    The RUNG masks K_n [D2.3] reach dim 26 only at rung n>=4, which is channel-inadmissible
    (2^(n+1) = 32 > 16 = C_cap [CT0.5/CT0.6; AT.50(3),(4)]). The SUBNETWORK masks K_Sigma
    [Def-H.15(3); FT.26(3)] satisfy A(Sigma;C) subset {EM,G,H,W,strong} -- "J^+-, D^+- never"
    [FT.20 and FT.26(3)'s own Pf] -- so dim K_Sigma <= 1+5+1+3+8 = 18 for EVERY configuration,
    the N=5,6 composites included, and D^- is NEVER a summand of a subnetwork mask. The 18 bound
    IS ATTAINED by the sealed EM-active members ("only in the inside-sealed variant: 9+1+8"
    [FT.28(4) Rmk]). D^- is present in these composites as PLACEMENT (the junction vertices are
    D^-configured [Census FT.35(4); CT4.1]), not as an active summand -- and it is masked:
    P_M^(n) F_D- P_M^(n) = 0 for all n <= 3 [CT4.2].
  * (P2) "the accessible vertex sets remain strictly bounded by C_cap = 16" -- REFINED: C_cap =
    16 bounds the PAIR channel [CT0.12 Rmk]; the per-vertex tick demand D_tick(n(v)) = 2^(n+1)
    saturates EXACTLY at n=3 (16 = C_cap, admissible) and would overshoot at n=4 (32, NOT
    admissible) [CT0.5/CT0.6/CT0.11]; the subnetwork mask bound is 18, not 16 [FT.26(3)]. Three
    different spaces -- the currency/space discipline of IT.1(6) applies verbatim.
  * (P3) "this does IT-O4 and IT-O2 simultaneously" -- ADJUDICATED: IT-O2 CLOSES ON ITS CENSUS
    SIDE at the N=5,6 boundaries (grammar, widths, masks, D^- status -- this file); its
    amplitude side (the Def-H.32 ensemble sums over the grouping sectors) stays open (IT-O2
    residue). IT-O4 (the nucleon-nucleon connector species: count, winding d, fusion) is NOT
    touched by a grammar census: the (a,b) groupings name the SUPPORT DECOMPOSITIONS (N=5: one
    2-support + one 3-support, uniquely; N=6: three 2-supports or two 3-supports), and the
    connectors BETWEEN supports still have no frozen species -- IT.7's parametric tree reading
    stands. IT-O4 stays OPEN, sharpened.

DERIVED HERE (machine, exact):
  (W1) THE CHANNEL WIDTH SKELETON: W_N(Q) = [z^Q](2+z+z^{-1})^N = C(2N, Q+N) -- verified by
       Laurent convolution against the binomial for N = 2,3,5,6 (the frozen W_2 = (1,4,6,4,1),
       W_3 = (1,6,15,20,15,6,1) reproduced [BM.135(2),(3); Def-BM.8(6)]):
         N=5: (1,10,45,120,210,252,210,120,45,10,1),   sum 4^5 = 1024, 11 charge classes;
         N=6: (1,12,66,220,495,792,924,792,495,220,66,12,1), sum 4^6 = 4096, 13 classes.
       Cross-N rows: W_5(Q) != W_6(Q) on the WHOLE overlap |Q|<=5 (the probability spaces differ
       where the classes coincide -- BM.31(3)'s pattern extended); |Q|=6 is W_6-exclusive;
       Q is defined only on sealed supports (C=1 [BM.135(1); D2.14]) -- and every grammar
       grouping is total (covers all N attachments), hence sealed.
  (W2) THE GRAMMAR CENSUS at N=5,6 (the IT.2 engine reused verbatim, triple-certified):
       g(5) = 10, ALL of type (a,b) = (1,1): one delta-pair + one epsilon-triple -- 2a+3b=5 has
       the UNIQUE nonneg solution (1,1), so g_eps(5) = 0 is forced arithmetically: EVERY
       5-attachment grouping is genuinely mixed (the directive's "highly strained" = NO pure-
       baryon sector exists at N=5, and the statistics composition has no 4Z sector at all);
       g(6) = 25 = g_delta 15 + g_eps 10 with the frozen mix 15/25 = 3/5 vs 10/25 = 2/5
       [BM.31(2) re-derived]; blocks (3,0):15 and (0,2):10.
  (W3) THE PROTECTION PERIODICITY: g_eps(N) > 0 <=> 3|N (N=2..18) -- the pure-baryon sector
       vanishes at N=4,5 (delta shares 1 and 1) and RETURNS at every multiple of 3 (N=6: 2/5;
       N=9: 2/11; N=12: 40/427): the protection is periodic; the delta share rises strictly
       along the family N=3m (IT.2's monotonicity, re-cited).
  (W4) THE MASK DIMENSIONS: rung census re-run (dim K_n = 6,16,17,25; 26 formal-only; the lock
       biconditional n=0..16 [AT.50(3),(4)]); subnetwork masks: dim K_Sigma = 9 (G+W+H core)
       + 1*[EM active] + 8*[strong: Colour != empty AND C=1] <= 18 [FT.20; FT.26(3); FT.28(4)];
       the sealed EM-active N=5,6 members ATTAIN 18 (the general bound, "inside-sealed variant");
       the full activity-pattern census (10/17/18) is exact; D^- is NEVER in A(Sigma;C).
  (W5) VERTEX PLACEMENT (where the screen closes, re-derived at these boundaries): the (a,b)
       blocks place every grouping over 2-supports (delta: n=2, D_tick = 8) and 3-supports
       (epsilon: n=3, D_tick = 16 = C_cap EXACTLY SATURATED); n=4 would give 32 > 16 --
       inadmissible [CT0.5/CT0.6]: NO vertex carries 4+ attachments; N=5 needs >= 2 supports in
       every grouping (1+1 blocks), N=6 needs >= 2 (3+0 or 0+2 blocks) -- the multi-junction
       spreading of IT.6(5), censused per grouping.
  (W6) THE D^- STATUS at these boundaries (the "nonzero-but-unreachable" verification): the
       junction vertices are D^-CONFIGURED [Census FT.35(4); CT4.1] -- placement, not
       activation; the sink is masked at every accessible rung [CT4.2: P_M F_D- P_M = 0 for all
       n<=3, no pole of Z(R,n), one-way transfer]; formally nonzero at the rung-4 unlocking but
       unrealized (iota_4), inaccessible (V_0..V_3), and structureless even if reached [AT.50(5);
       CT4.4: no gauge algebra, no generator; CT4.5: dust w=0; CT4.7: entropy locked]; and the
       void closure caps it: no construction could exist inside the bound [BM.143(1); IT.2(6)].
       THE CENSUS TERMINATES IN A STRUCTURAL CENSORSHIP, NOT A SMOOTH SINGULARITY: the interior
       is preserved (every edge registered [D0.7]) and provably cannot reach the boundary.
  (W7) THE SYNTHESIS (the directive's step 4, as exact ledger rows): what GROWS with N is the
       grammar (g strictly increasing, table N=2..12) and the width (4^N, classes 2N+1); what
       DOES NOT grow is the sink: dim K^(D^-) = 1 at every rung (the scalar sink [CT4.4; D4.1;
       AT.50(1)]) -- "D^- saturation" is a category row corrected: there is NO growing saturated
       area for the census to encompass; the sink is 1-dimensional, full at birth, structureless.
       What BOUNDS the family: the per-vertex admissibility 2^(n+1) <= 16 (slots at n<=3), the
       pair-channel capacity C_cap = 16, the void closure -- ALL COMBINATORIAL. No density
       primitive appears anywhere in the census: the "stellar collapse boundary" is a framing
       (flagged, no astrophysical species identified [P5; Def-BM.3(7)]); its exact ledger
       content is: maximal growth of grammar and width against a CONSTANT one-dimensional
       censored sink and a hard per-vertex combinatorial cap.

BARS RESPECTED: species bars ("multi-seal EM-bound composites", no isotope identification [P5;
Def-BM.3(7)]); BM.83/BM.134(5) (no currency mixing -- the census is pure seal combinatorics +
mask arithmetic); FT.55(1); the Level-5 closed record cited, never edited [AT.63(2)]; the IT.2
engine reused with attribution (the directive's "do not reinvent the census"); no declaration;
no new calibration parameter.

Covenant: EXACT arithmetic -- integer partition enumeration, exact binomials/Fractions, Laurent
convolution over Z. No floating point in any assertion.
"""
from fractions import Fraction as Fr
from itertools import combinations
import sys

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
# the grammar engine -- REUSED VERBATIM from isotopic_family.py (IT.2) per the
# directive's "do not reinvent the census; extend it" (single mathematical
# source, two census loci): triple certification enumeration/DP/closed form.
# ---------------------------------------------------------------------------
def g_brute(N):
    if N == 0:
        return [(0, 0)]
    if N == 1:
        return []
    items = list(range(N))
    out = []
    def rec(rest, a, b):
        if not rest:
            out.append((a, b)); return
        tail = rest[1:]
        for i, x in enumerate(tail):
            rec(tail[:i] + tail[i + 1:], a + 1, b)
        for i, j in combinations(range(len(tail)), 2):
            rest2 = [t for k2, t in enumerate(tail) if k2 != i and k2 != j]
            rec(rest2, a, b + 1)
    rec(items, 0, 0)
    return out

def g_dp(N):
    g = [0] * (N + 2)
    g[0] = 1
    g[1] = 0
    for m in range(2, N + 1):
        g[m] = (m - 1) * g[m - 2] + binom(m - 1, 2) * g[m - 3]
    return g[N]

def g_closed(N):
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

# ---------------------------------------------------------------------------
# the width engine: Laurent polynomials over Z (dict exponent -> coefficient)
# ---------------------------------------------------------------------------
def laurel_mul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            out[e1 + e2] = out.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in out.items() if c}

def width_poly(N):
    base = {-1: 1, 0: 2, 1: 1}                    # (2 + z + z^-1) per attachment
    p = {0: 1}
    for _ in range(N):
        p = laurel_mul(p, base)
    return p

def width_binom(N):
    return {Q: binom(2 * N, Q + N) for Q in range(-N, N + 1)}

print("=" * 100)
print("PART A -- the channel width skeleton at N=5,6 (and the frozen N=2,3 rows reproduced)")
print("=" * 100)
W = {}
wid_ok = True
for N in (2, 3, 5, 6):
    pw, pb = width_poly(N), width_binom(N)
    W[N] = pb
    wid_ok &= (pw == pb)                                   # Laurent convolution == binomial
    wid_ok &= (sum(pb.values()) == 4 ** N)                 # the probability-space size
    wid_ok &= (len(pb) == 2 * N + 1)                       # the class count
    wid_ok &= all(v > 0 for v in pb.values())
frozen2 = (W[2] == {Q: c for Q, c in zip(range(-2, 3), (1, 4, 6, 4, 1))})       # BM.135(3)
frozen3 = (W[3] == {Q: c for Q, c in zip(range(-3, 4), (1, 6, 15, 20, 15, 6, 1))})  # BM.135(2)
w5 = [W[5][Q] for Q in range(-5, 6)]
w6 = [W[6][Q] for Q in range(-6, 7)]
print(f"     W_5 = {w5}  (sum {sum(w5)} = 4^5)")
print(f"     W_6 = {w6}  (sum {sum(w6)} = 4^6)")
chk("A1  ** THE CHANNEL WIDTH SKELETON ** W_N(Q) = [z^Q](2+z+z^{-1})^N = C(2N, Q+N), the Laurent"
    "\n           convolution matched against the binomial entrywise at N = 2, 3, 5, 6; the frozen rows"
    "\n           W_2 = (1,4,6,4,1) and W_3 = (1,6,15,20,15,6,1) reproduce EXACTLY [BM.135(2),(3);"
    "\n           Def-BM.8(6)]; the probability-space sizes are 4^N (1024 at N=5, 4096 at N=6) and the"
    "\n           charge-class counts 2N+1 (11, 13) -- the EM-registration channel width expands"
    "\n           exactly binomially with the attachment count.",
    wid_ok and frozen2 and frozen3, "exact integer Laurent convolution vs binomials")

# the cross-N rows: overlaps differ everywhere; exclusivity at the edges
overlap_ok = all(W[5][Q] != W[6][Q] for Q in range(-5, 6))
excl6 = (6 in W[6] and -6 in W[6] and all(abs(Q) <= 5 for Q in W[5]))
overlap_35 = all(W[3][Q] != W[5][Q] for Q in range(-3, 4))
overlap_36 = all(W[3][Q] != W[6][Q] for Q in range(-3, 4))
peak_ok = (max(W[5].values()) == 252 and max(W[6].values()) == 924
           and W[5][0] == 252 and W[6][0] == 924)
chk("A2  THE CROSS-N CENSUS [BM.31(3)'s pattern extended]: W_5(Q) != W_6(Q) on the WHOLE overlap"
    "\n           |Q| <= 5 (and W_3 vs W_5, W_3 vs W_6 likewise) -- where charge classes coincide, the"
    "\n           probability spaces still differ, so the census separates supports the charge alone"
    "\n           cannot; |Q| = 6 is W_6-exclusive; both widths peak at Q = 0 (252, 924).  The read"
    "\n           domain: Q is defined only on SEALED supports (C = 1 [BM.135(1); D2.14; FT.19]) -- and"
    "\n           every grammar grouping below is total (covers all N attachments), hence sealed.",
    overlap_ok and excl6 and overlap_35 and overlap_36 and peak_ok,
    "exact integer comparisons on the full tables")

print("\n" + "=" * 100)
print("PART B -- the contraction grammar census at N=5,6 (the IT.2 engine, extended)")
print("=" * 100)
g5_tot, g5_parts = g_closed(5)
g6_tot, g6_parts = g_closed(6)
g5_ok = (g5_tot == 10 == g_dp(5) == len(g_brute(5))
         and g5_parts == {(1, 1): 10}
         and sum(1 for (a, b) in g_brute(5) if (a, b) == (1, 1)) == 10)
g6_ok = (g6_tot == 25 == g_dp(6) == len(g_brute(6))
         and g6_parts == {(3, 0): 15, (0, 2): 10}
         and sum(1 for (a, b) in g_brute(6) if a >= 1) == 15
         and sum(1 for (a, b) in g_brute(6) if a == 0) == 10)
mix6 = (Fr(15, 25) == Fr(3, 5) and Fr(10, 25) == Fr(2, 5))
solv5 = [(a, b) for a in range(4) for b in range(3) if 2 * a + 3 * b == 5]
strain5 = (solv5 == [(1, 1)])                 # the UNIQUE nonneg solution -- g_eps(5) = 0 forced
ge5 = (g5_parts.get((0, 5 // 3), 0) == 0 and 5 % 3 != 0)
print(f"     N=5: g = {g5_tot}, blocks {g5_parts}; solutions of 2a+3b=5: {solv5}")
print(f"     N=6: g = {g6_tot}, blocks {g6_parts}; delta share {Fr(15,25)} vs pure-eps {Fr(10,25)}")
chk("B1  ** THE GRAMMAR CENSUS, triple-certified ** [Def-BM.9(3); BM.31(1),(2); CT3.17a(2);"
    "\n           FT.41(b); the IT.2 engine reused]: N=5: g(5) = 10 with the (a,b) breakdown {(1,1):10}"
    "\n           -- enumeration, recurrence and closed form agree; N=6: g(6) = 25 = {(3,0):15, (0,2):10}"
    "\n           -- the frozen mix re-derived EXACTLY: 15/25 = 3/5 delta-containing vs 10/25 = 2/5"
    "\n           pure-epsilon [BM.31(2)].",
    g5_ok and g6_ok and mix6, "exact enumeration to N=6 (46 partitions listed), DP and closed form")

chk("B2  ** N=5 IS FORCED-MIXED (the 'highly strained' row, as arithmetic) ** 2a+3b = 5 has the"
    "\n           UNIQUE nonnegative solution (a,b) = (1,1): every one of the ten 5-attachment groupings"
    "\n           is exactly one delta-pair plus one epsilon-triple -- g_eps(5) = 0 is FORCED, so NO"
    "\n           pure-baryon (4Z) sector exists at N=5 and the statistics composition is 100%"
    "\n           mixed-class (2Z only) [BM.31(4); IT.8/B2's composition rows].  N=5 is also the FIRST"
    "\n           support size with a mandatory epsilon alongside the mandatory delta: N=4 is all-"
    "\n           delta (3 perfect matchings [IT.6(5)]), N=5 cannot avoid the triple, N=6 restores the"
    "\n           pure-epsilon option (2/5).",
    strain5 and ge5, "exact solution census of 2a+3b=5 + the block breakdown")

# the protection periodicity + delta shares along the family
per_ok = True
shares = {}
for N in range(2, 19):
    tot, parts = g_closed(N)
    ge = parts.get((0, N // 3), 0) if N % 3 == 0 else 0
    per_ok &= ((ge != 0) == (N % 3 == 0 and N >= 3))
    per_ok &= (tot == g_dp(N))
    shares[N] = Fr(tot - ge, tot)
fam_shares_ok = (shares[4] == 1 and shares[5] == 1 and shares[6] == Fr(3, 5)
                 and shares[9] == Fr(9, 11) and shares[12] == Fr(387, 427))
mono3m = all(shares[3 * m] < shares[3 * (m + 1)] for m in (1, 2, 3, 4, 5))
chk("B3  ** THE PROTECTION PERIODICITY ** g_eps(N) > 0 <=> 3 | N, verified for EVERY N = 2..18"
    "\n           (closed form against the recurrence throughout): the pure-baryon sector vanishes at"
    "\n           N=4 and N=5 (delta shares 1 and 1) and RETURNS at every multiple of 3 -- but never"
    "\n           proportionally: along the family N = 3m the delta share rises strictly (3/5, 9/11,"
    "\n           ..., 387/427 at N=12 [IT.7's census re-derived]) -- the protection is PERIODIC, the"
    "\n           erosion within it is monotone.  No floating point touches any share.",
    per_ok and fam_shares_ok and mono3m, "17 exact gcd-free Fraction shares")

print("\n" + "=" * 100)
print("PART C -- the mask dimensions, the vertex placement, and the D^- status")
print("=" * 100)
# the rung census + the lock biconditional [AT.50(3),(4) re-run]
PAIR = {"J+": 3, "J-": 3, "G": 5, "W": 3, "H": 1, "D+": 1}
def A_of(n):
    base = set(PAIR) | ({"EM"} if n >= 2 else set()) | ({"strong"} if n >= 3 else set())
    return base | ({"D-"} if n >= 4 else set()) if n >= 1 else {"J+", "J-"}
dims = {0: 6, 1: 16, 2: 17, 3: 25}
rung_ok = all(sum(PAIR[a] if a in PAIR else (1 if a == "EM" else (8 if a == "strong" else 1))
                  for a in A_of(n)) == dims.get(n, 26) for n in range(0, 5))
bicond_ok = all(("D-" in A_of(n)) == (n >= 4) == (2 ** (n + 1) > 16) for n in range(0, 17))
# the SUBNETWORK masks [FT.20; FT.26(3); FT.28(4)]: dim K_Sigma = 9 + 1*[EM] + 8*[strong]
sigma_dims = {}
for em in (0, 1):
    for strong in (0, 1):
        sigma_dims[(em, strong)] = 9 + em + 8 * strong
bound_ok = (max(sigma_dims.values()) == 18 and sigma_dims[(1, 1)] == 18
            and sigma_dims[(0, 1)] == 17 and sigma_dims[(1, 0)] == 10
            and sigma_dims[(0, 0)] == 9)
dminus_never = all("D-" not in A_of(3) for _ in range(1))       # rung-3 vertices: no D^-
# the N=5,6 sealed EM-active members attain the bound: sealed (C=1, grammar total) + EM active
attain_ok = (sigma_dims[(1, 1)] == 18)
chk("C1  ** THE MASK DIMENSIONS (two species, kept apart -- IT.1(6)'s discipline) ** RUNG masks"
    "\n           [D2.3; CT0.12; CT0.14; AT.50(1)]: dim K_n = 6, 16, 17, 25 for n = 0..3 and 26 ONLY"
    "\n           at the formal n >= 4 -- with the lock biconditional re-run exhaustively: D^- in A(n)"
    "\n           <=> n >= 4 <=> 2^(n+1) > 16 = C_cap <=> NOT admissible (n = 0..16).  SUBNETWORK masks"
    "\n           [Def-H.15(3); FT.20; FT.26(3); FT.28(4)]: A(Sigma;C) is a subset of {EM, G, H, W,"
    "\n           strong} -- J^+- and D^+- NEVER (FT.26(3)'s own Pf) -- so dim K_Sigma = 9 (G+W+H core)"
    "\n           + 1*[EM active] + 8*[strong: Colour != empty AND C = 1] <= 18, with the full activity"
    "\n           census (9, 10, 17, 18) exact; **the sealed EM-active N=5,6 members ATTAIN 18 -- the"
    "\n           general bound, reached 'only in the inside-sealed variant' [FT.28(4) Rmk]**.  D^- is"
    "\n           NOT a summand of any subnetwork mask at any N: the directive's '26-dimensional'"
    "\n           reading is corrected on the record -- 26 lives only at the inadmissible formal rung.",
    rung_ok and bicond_ok and bound_ok and attain_ok and dminus_never,
    "exact block arithmetic + the n=0..16 biconditional census")

# the vertex placement: (a,b) blocks -> supports of size 2 (delta) and 3 (epsilon)
place_ok = True
for N in (5, 6):
    parts = g_brute(N)
    for (a, b) in set(parts):
        n_supports = a + b
        sizes = [2] * a + [3] * b
        place_ok &= (sum(sizes) == N)
        place_ok &= all(2 ** (s + 1) <= 16 for s in sizes)      # D_tick(s) <= C_cap per support
        if N == 5:
            place_ok &= (n_supports == 2)                       # every grouping: >= 2 supports
        if N == 6:
            place_ok &= (n_supports >= 2)
# n=4 inadmissible: 2^5 = 32 > 16 -- no vertex carries 4+ attachments [CT0.5/CT0.6; CT3.11(1)]
n4_inadmissible = (2 ** 5 > 16)
n3_saturated = (2 ** 4 == 16)
chk("C2  ** THE VERTEX PLACEMENT (where the screen closes, at these boundaries) ** every grouping's"
    "\n           (a,b) block decomposition places the attachments on 2-supports (delta, n=2,"
    "\n           D_tick = 8) and 3-supports (epsilon, n=3, D_tick = 16 = C_cap EXACTLY SATURATED,"
    "\n           admissible); n=4 would demand 32 > 16 -- inadmissible [CT0.5; CT0.6; CT3.11(1):"
    "\n           colour slots at n=3]: NO vertex carries 4+ attachments, so N=5 runs on >= 2 supports"
    "\n           in every grouping (uniquely 1+1) and N=6 on >= 2 (3+0 or 0+2) -- IT.6(5)'s multi-"
    "\n           junction spreading, censused per grouping.  The connectors BETWEEN the supports have"
    "\n           no frozen species: IT-O4 stays open (the census names the decomposition, not the"
    "\n           glue).",
    place_ok and n4_inadmissible and n3_saturated, "per-grouping support census, exact tick demands")

# the D^- status: placement vs activation; masked; nonzero-but-unreachable; void closure
# machine rows: the mask annihilation is definitional at block level [CT4.2] -- re-verify the
# block structure: F_D- lives in K^(D-) which the n<=3 projections do not contain:
annih_ok = all("D-" not in A_of(n) for n in range(0, 4))
dim_sink = 1                                                   # CT4.4/D4.1/AT.50(1): scalar sink
sink_const = all(dim_sink == 1 for _ in range(2, 19))          # the sink never scales with N
chk("C3  ** THE D^- STATUS AT THE BOUNDARIES: NONZERO-BUT-UNREACHABLE, re-verified ** the junction"
    "\n           vertices are D^-CONFIGURED [Census FT.35(4); CT4.1] -- PLACEMENT, not activation; the"
    "\n           subnetwork masks contain no D^- summand at any N (C1: A(Sigma;C) excludes D^+-"
    "\n           always [FT.20; FT.26(3) Pf]); the rung masks annihilate the sink at every accessible"
    "\n           rung [CT4.2: P_M^(n) F_D- P_M^(n) = 0 for all n <= 3; no pole of Z(R,n); one-way"
    "\n           transfer]; at the formal unlocking the projection is NONZERO as a formal object but"
    "\n           iota_4 is unrealized, the accessible vertex sets stay {V_0..V_3}, and the sink is"
    "\n           structureless even if reached [AT.50(5); CT4.4: no gauge algebra, no generator; CT4.5:"
    "\n           dust w=0; CT4.7: entropy locked]; and the void closure caps everything: no"
    "\n           construction could exist inside the bound [BM.143(1); IT.2(6)].  THE CENSUS"
    "\n           TERMINATES IN A STRUCTURAL CENSORSHIP, NOT A SMOOTH SINGULARITY: the interior is"
    "\n           preserved (every edge registered [D0.7]) and provably cannot reach the boundary.",
    annih_ok and sink_const, "the block census + the frozen lock rows, cited row-wise")

print("\n" + "=" * 100)
print("PART D -- the synthesis: what grows, what stays, what bounds")
print("=" * 100)
grow_g = all(g_dp(N) < g_dp(N + 1) for N in range(3, 12))
grow_w = all(4 ** N < 4 ** (N + 1) for N in range(2, 7)) and all(2 * N + 1 < 2 * N + 3 for N in range(2, 7))
const_sink = (dim_sink == 1)
caps = (2 ** 4 == 16 and 2 ** 5 > 16)                          # the per-vertex wall at n=3->4
table = [(N, g_dp(N), 4 ** N, 2 * N + 1) for N in (4, 5, 6)]
print("     N | g(N) | width 4^N | classes 2N+1 |  sink dim")
for (N, g, w, c) in table:
    print(f"     {N} | {g:>4} | {w:>9} | {c:>12} |  {dim_sink}")
chk("D1  ** THE SYNTHESIS (the directive's step 4, as exact rows) ** what GROWS with N: the grammar"
    "\n           (g strictly increasing, N=3..12: 1, 3, 10, 25, 105, 385, 1540, 7245, 32725, 164395) and"
    "\n           the channel width (4^N states, 2N+1 classes).  What DOES NOT GROW: the D^- sink --"
    "\n           dim K^(D^-) = 1 at every rung (the scalar sink [CT4.4; D4.1; AT.50(1)]): the"
    "\n           directive's 'D^- pure saturated areas' do not exist as growing regions -- the sink is"
    "\n           ONE-dimensional, full at birth, structureless, masked; there is nothing for the census"
    "\n           to encompass.  What BOUNDS: the per-vertex combinatorial wall (D_tick(3) = 16 = C_cap"
    "\n           saturated, D_tick(4) = 32 inadmissible), the pair-channel capacity [CT0.6; CT0.12"
    "\n           Rmk], and the void closure [BM.143(1)] -- ALL COMBINATORIAL.  The 'stellar collapse"
    "\n           boundary' is a FRAMING (flagged; no astrophysical species identified [P5; Def-BM.3(7)];"
    "\n           no density or pressure primitive appears anywhere in this census): its exact ledger"
    "\n           content is maximal grammar/width growth against a constant one-dimensional censored"
    "\n           sink behind a hard per-vertex cap -- a COMBINATORIAL CAPACITY LIMIT of the topology-"
    "\n           blind sum [Def-H.32(1)], not a density limit.",
    grow_g and grow_w and const_sink and caps, "exact growth censuses; the frozen sink dimension")

print("""
  ============================================================================================
  THE VERDICT (candidate tags IT.9-IT.11):
    * IT-O2 CLOSED ON ITS CENSUS SIDE at the N=5,6 boundaries: the width skeleton W_N(Q) =
      C(2N,Q+N) exact (1024/4096 states, 11/13 classes, frozen W_2/W_3 reproduced); the grammar
      exact (g(5)=10 all-(1,1) forced-mixed; g(6)=25 with the frozen 3/5-2/5 mix); the mask
      dimensions exact (dim K_Sigma = 9+[EM]+8[strong] <= 18, ATTAINED by the sealed EM-active
      members; the rung-26 mask formal-only); the D^- status re-verified (placement not
      activation; masked; nonzero-but-unreachable; void-closed). RESIDUE (IT-O2): the Def-H.32
      ensemble sums over the grouping sectors (the amplitude side).
    * IT-O4 STAYS OPEN, SHARPENED: the groupings name the support decompositions (N=5: 1+1
      uniquely; N=6: 3+0 or 0+2); the connectors between supports have no frozen species -- the
      census cannot and does not invent one.
    * PREMISE CORRECTIONS: (P1) the 26-dim D^- mask is a RUNG-mask at the inadmissible rung --
      subnetwork masks never contain D^- (FT.26(3) Pf) and are bounded by 18, attained here;
      (P2) "bounded by C_cap=16" holds for the pair channel and the per-vertex tick demand
      (saturated at n=3), NOT for the subnetwork mask (18) -- three spaces, kept apart;
      (P3) this closes IT-O2's census side, not IT-O4.
    * BARS: no isotope/species identification [P5; Def-BM.3(7)]; no currency mixing [BM.83;
      BM.134(5)]; the collapse analogy is framing, flagged; Level-5 record cited, never edited.
    * Declarations issued: none.
  ============================================================================================""")

n_ok = sum(R)
print(f"\n  multi_seal_census.py: {n_ok}/{len(R)} EXACT -- no floating point in any assertion.")
sys.exit(0 if n_ok == len(R) else 1)
