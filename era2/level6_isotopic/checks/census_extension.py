#!/usr/bin/env python3
"""
census_extension.py -- Tier IT.19's machine (tags IT.61-IT.63): the level-ladder arithmetic, the
delta-glue scope census behind the new open row IT-O6, and the builder-channel census rows
re-verified by TRIPLE certification (recurrence ^ dynamic program ^ closed form) before adoption.

PROVENANCE: the k=4,5 family cells, the (a,b) block splits, the transparency census and the m=4
weight-convention fork were surfaced by the BUILDER's instruments (vault comms/0001, pinned at era2
978e27d) and are re-derived here FROM SCRATCH against the corpus's own grammar [BM.31(1),(2);
Def-BM.9(3)] -- the corpus is the single source of truth (vault PROTOCOL rule 4); the builder's
numbers are the second attestation, not the first. The g(15)/g(18) cells also lie inside
isotopic_family.py F2's range (k=0..5), so the suite already certified them; this checker makes the
cells, the block splits, the shares and the transparency census explicit rows.

EXACT ARITHMETIC ONLY: integers and Fractions; no floating point; no measured value [P5]; the
species names ("proton", "neutron") stay quoted [Def-BM.3(7)]; counts and prices only.
"""

import sys
from fractions import Fraction as Fr

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


# ---- route 1: the recurrence  g(N) = (N-1) g(N-2) + C(N-1,2) g(N-3),  g(0)=1, g(1)=0, g(2)=1
def g_rec(N):
    g = {0: 1, 1: 0, 2: 1}
    for n in range(3, N + 1):
        g[n] = (n - 1) * g[n - 2] + binom(n - 1, 2) * g[n - 3]
    return g[N]


# ---- route 2: the memoized block recursion (independent code path from the iterative recurrence)
def g_dp(N):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def f(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return 0
        return (n - 1) * f(n - 2) + binom(n - 1, 2) * f(n - 3)

    return f(N)


# ---- route 3: the closed form  sum over 2a+3b=N of N!/(a! 2^a b! 6^b), with the block split
def g_closed(N):
    tot = 0
    blocks = {}
    for b in range(N // 3 + 1):
        rem = N - 3 * b
        if rem % 2:
            continue
        a = rem // 2
        t = fact(N) // (fact(a) * 2 ** a * fact(b) * 6 ** b)
        blocks[(a, b)] = t
        tot += t
    return tot, blocks


print("=" * 104)
print("PART A -- the family cells at k=4,5: triple certification + the block splits + the shares")
print("=" * 104)

# the builder-published cells (vault comms/0001 §3.1), verified against all three routes:
CLAIM = {
    15: (27152125, {(0, 5): 1401400, (3, 3): 21021000, (6, 1): 4729725}),
    18: (6443061625, {(0, 6): 190590400, (3, 4): 4288284000, (6, 2): 1929727800, (9, 0): 34459425}),
}
triple_ok = True
for N, (gv, blocks) in CLAIM.items():
    triple_ok &= (g_rec(N) == gv) and (g_dp(N) == gv)
    tot, bl = g_closed(N)
    triple_ok &= (tot == gv) and (bl == blocks)
# the frozen anchors re-hit on the same engines (the chain to the record):
anchors_ok = (g_rec(3) == 1 and g_rec(4) == 3 and g_rec(5) == 10 and g_rec(6) == 25
              and g_rec(8) == 385 and g_rec(9) == 1540 and g_rec(12) == 164395)
chk("A1  [BM.31(1),(2); Def-BM.9(3); IT.6(5),(6); IT.31(5); vault 0001 §3.1 -- TRIPLE-certified]: the"
    "\n           family cells at k=4,5 (the '(computed)' placeholders of ISOTOPIC_FAMILY.md §III):"
    "\n           g(15) = 27152125 with blocks (0,5):1401400, (3,3):21021000, (6,1):4729725; g(18) ="
    "\n           6443061625 with blocks (0,6):190590400, (3,4):4288284000, (6,2):1929727800,"
    "\n           (9,0):34459425 -- recurrence ^ DP ^ closed form all agree, and the frozen anchors"
    "\n           g(3)=1, g(4)=3, g(5)=10, g(6)=25, g(8)=385, g(9)=1540, g(12)=164395 re-hit on the same"
    "\n           engines. The builder's independent instruments are the SECOND attestation.",
    triple_ok and anchors_ok, f"g(15)={g_rec(15)}; g(18)={g_rec(18)}")

ge15, ge18 = CLAIM[15][1][(0, 5)], CLAIM[18][1][(0, 6)]
gd15, gd18 = CLAIM[15][0] - ge15, CLAIM[18][0] - ge18
# g_eps closed form: the pure-triple term N!/(b! 6^b) at b=N/3 (nonzero iff 3|N [IT.6(5)])
ge_ok = (ge15 == fact(15) // (fact(5) * 6 ** 5)) and (ge18 == fact(18) // (fact(6) * 6 ** 6))
shares = [Fr(0), Fr(3, 5), Fr(9, 11), Fr(387, 427), Fr(gd15, CLAIM[15][0]), Fr(gd18, CLAIM[18][0])]
A2_ok = (ge_ok and gd15 == 25750725 and gd18 == 6252471225
         and shares[4] == Fr(147, 155) and shares[5] == Fr(14697, 15145)
         and Fr(gd15, ge15) == Fr(147, 8) and Fr(gd18, ge18) == Fr(14697, 448)
         and all(shares[i] < shares[i + 1] for i in range(5))
         and all(s < 1 for s in shares))
chk("A2  [IT.6(6); IT.9(5); IT.18; IT.31(5)]: the epsilon/delta split at k=4,5: g_eps = the pure-triple"
    "\n           closed form N!/(b! 6^b) (15: 1401400; 18: 190590400 -- machine); g_delta = (25750725,"
    "\n           6252471225); the delta-share sequence 0, 3/5, 9/11, 387/427, 147/155, 14697/15145 is"
    "\n           STRICTLY INCREASING and stays below 1 -- IT.17(2)'s monotonicity continues past the frozen"
    "\n           range and 'delta-dominance is a degree, not a kind-change' [IT.18(4)] holds at k=5; the"
    "\n           pure-epsilon backbone never vanishes on the family (3|N [IT.6(5)]).",
    A2_ok, f"shares: {[str(s) for s in shares]}")

print("=" * 104)
print("PART B -- the transparency census: the curtain is transparent at exactly one support class")
print("=" * 104)


def nucleonic(m, Q):
    """the nucleonic weight binom(m,Q) 15^Q 20^(m-Q): 15 = W_3(+1) proton-class, 20 = W_3(0)
    neutron-class [BM.17(1); Census FT.35(5); D3.9; BM.135(2); exotic_states.py C2 convention]."""
    return binom(m, Q) * 15 ** Q * 20 ** (m - Q)


def residues(N):
    """exotic residue per nucleonic charge Q = 0..m: W_N(Q) - nucleonic(m,Q), W_N(Q)=C(2N, N+Q)."""
    m = N // 3
    return [binom(2 * N, N + Q) - nucleonic(m, Q) for Q in range(0, m + 1)]


res_table = {3 * m: residues(3 * m) for m in range(1, 7)}
transparent = [N for N, rs in res_table.items() if all(x == 0 for x in rs)]
opaque = [N for N, rs in res_table.items() if all(x > 0 for x in rs)]
n3_full = [binom(6, Q + 3) - (nucleonic(1, Q) if Q in (0, 1) else 0) for Q in range(-3, 4)]
B1_ok = (transparent == [3] and opaque == [6, 9, 12, 15, 18]
         and res_table[6] == [524, 192, 270]
         and res_table[9] == [40620, 25758, 18324, 15189]
         and res_table[12] == [2544156, 2016144, 1421256, 1037504, 684846]
         and res_table[15] == [151917520, 133422675, 101759850, 72993225, 49564800, 29285640]
         and res_table[18] == [9011135300, 8309496600, 6767872110, 5027902560, 3492547200,
                               2219664600, 1240287075]
         and n3_full == [1, 6, 15, 0, 0, 6, 1])
chk("B1  [IT.22; IT.23(2); exotic_states.py engines; vault 0001 §3.2 -- re-derived from scratch]: the"
    "\n           transparency census over the nucleonic range 0 <= Q <= m: the exotic residue"
    "\n           W_N(Q) - binom(m,Q) 15^Q 20^(m-Q) vanishes for BOTH nucleonic classes at N=3 (m=1)"
    "\n           -- the UNIQUE transparent support class -- and is strictly positive at every nucleonic"
    "\n           Q for m=2..6 (N=6..18; every builder row reproduced exactly, incl. the N=9 row"
    "\n           40620/25758/18324/15189 whose middle entries are IT.12(1)'s frozen complements"
    "\n           25758/18324). The N=3 row over ALL SEVEN charge classes is (1,6,15,0,0,6,1): zero"
    "\n           across both nucleonic classes, positive on all four exotic ones.",
    B1_ok, f"transparent: {transparent}; residues(6) = {res_table[6]}; residues(9) = {res_table[9]}")

B2_ok = (binom(6, 3) == 20 == nucleonic(1, 0)) and (binom(6, 4) == 15 == nucleonic(1, 1)) \
    and all(binom(12, 6 + Q) > nucleonic(2, Q) for Q in (0, 1, 2))
chk("B2  [the exact reason; IT.22(1); BM.31(1) mirror-flag]: with ONE sealed epsilon-triple the"
    "\n           nucleonic restriction exhausts the sector (W_3(0)=20=nucleonic(0), W_3(1)=15="
    "\n           nucleonic(1) -- equalities, machine); from m=2 on, mixed nucleon charges leave"
    "\n           positive residue (strict inequalities machine-verified). MIRROR FLAG: this width-side"
    "\n           transparency at N=3 mirrors the grammar-side protection g(3)=1, g_delta(3)=0"
    "\n           [BM.31(1); IT.6(5)] -- two currencies turning at the same N; recorded as a PARALLEL,"
    "\n           NOT an identification [BM.134(5) discipline; IT.44(3) numerology pattern].",
    B2_ok)

print("=" * 104)
print("PART C -- the sub-sum witness, the m=4 convention fork, the glue census, the ladder")
print("=" * 104)

# C1: the nucleonic sub-sum is 35^m, a genuine sub-sum of 4^N = 64^m
sub_ok = all(sum(nucleonic(m, Q) for Q in range(m + 1)) == 35 ** m for m in range(1, 7))
ratios = [Fr(35 ** m, 64 ** m) for m in range(1, 5)]
C1_ok = sub_ok and ratios == [Fr(35, 64), Fr(1225, 4096), Fr(42875, 262144), Fr(1500625, 16777216)]
chk("C1  [vault 0001 §3.3 -- re-derived]: the nucleonic census summed over Q equals 35^m (the"
    "\n           sub-alphabet 20+15 per nucleon), a genuine SUB-sum of 4^N = 64^m (binomial theorem,"
    "\n           m=1..6 machine); the builder's ratio row (35/64, 1225/4096, 42875/262144,"
    "\n           1500625/16777216) reproduced exactly.",
    C1_ok)

# C2: the m=4 weight-convention fork (the curtain's guard, stated as a row)
conv_A = [binom(4, Q) * 15 ** Q * 20 ** (4 - Q) for Q in range(5)]
conv_B = [binom(4, Q) * 20 ** Q * 15 ** (4 - Q) for Q in range(5)]
agree = [Q for Q in range(5) if conv_A[Q] == conv_B[Q]]
C2_ok = (conv_A == [160000, 480000, 540000, 270000, 50625]
         and conv_B == [50625, 270000, 540000, 480000, 160000]
         and agree == [2])
chk("C2  [vault 0001 §1 residue -- the m=4 convention fork, recorded as a guard row]: the two"
    "\n           candidate nucleonic weight conventions (15 on proton-class vs reversed) COINCIDE at"
    "\n           m=3 (IT.12(3)'s frozen display) and DIVERGE at m=4, agreeing only at Q=2: the two"
    "\n           tables (160000, 480000, 540000, 270000, 50625) vs (50625, 270000, 540000, 480000,"
    "\n           160000) -- machine. Any N=12 curtain extension must take the convention from the"
    "\n           ALPHABET derivation [exotic_states.py C2: 15 = W_3(+1) on proton-class nucleons],"
    "\n           never transcribed from the m=3 display.",
    C2_ok, f"agreement locus: Q = {agree}")

# C3: the glue census at N=5,6 -- the block shapes and the derived/underived stamps
t5, b5 = g_closed(5)
t6, b6 = g_closed(6)
glue_table = {(5, (1, 1)): b5[(1, 1)], (6, (0, 2)): b6[(0, 2)], (6, (3, 0)): b6[(3, 0)]}
shapes = {(1, 1): (2, 3), (0, 2): (3, 3), (3, 0): (2, 2)}
stamps = {(3, 3): "DERIVED (Sigma_12 [IT.19])", (2, 3): "UNDERIVED", (2, 2): "UNDERIVED"}
C3_ok = (t5 == 10 and b5 == {(1, 1): 10} and t6 == 25 and b6 == {(0, 2): 10, (3, 0): 15}
         and glue_table == {(5, (1, 1)): 10, (6, (0, 2)): 10, (6, (3, 0)): 15})
chk("C3  [IT.9(2); IT.19-IT.21; IT.25; vault 0001 §4 -- the block census re-derived]: the multi-seal"
    "\n           block shapes at N=5,6: g(5)=10 ALL-(1,1) (shape 2+3, distinct pair (2,3)); g(6)=25 ="
    "\n           (3,0):15 [shape 2+2+2, pair (2,2)] + (0,2):10 [shape 3+3, pair (3,3)] (machine: the"
    "\n           closed-form block splits). The glue stamps: (3,3) = the DERIVED Sigma_12 connector"
    "\n           [IT.19: the frozen open bidirectional pair, d=0, +2 E_int, charge-telescoping, eps=+1,"
    "\n           DISTINCT SEALED SUPPORTS at N=3(k+1) -- epsilon-sealed 3-junctures]; (2,3) and (2,2)"
    "\n           involve delta-sealed digon supports [BM.110(1): the unique sealed 2-juncture] and are"
    "\n           UNDERIVED -- no row of IT.19-IT.21 constructs a glue species for a delta support (an"
    "\n           absence claim, level-local). The derived glue covers ONE of the three block shapes.",
    C3_ok, f"glue census: {glue_table}; stamps: {stamps}")

# C4: the ladder arithmetic -- the insertion and the target shift
ladder = {5: "Atomic", 6: "Isotopic", 7: "Molecular", 8: "Anthropic", 9: "Stellar",
          10: "Black holes", 11: "Galactic", 12: "Galactic clusters", 13: "Laniakea-like",
          14: "Universe"}
old_target, new_target = 13, 14
C4_ok = (len(ladder) == 10 and ladder[7] == "Molecular" and ladder[8] == "Anthropic"
         and ladder[14] == "Universe" and new_target == old_target + 1)
chk("C4  [the Architect's level-map act, recorded at IT.61; vault 0002]: the declared ladder --"
    "\n           Molecular at 7 (between Isotopic and Anthropic: IT.15(3)'s reserved act EXERCISED),"
    "\n           Anthropic moved to 8, the named rungs 9-13 (Stellar, Black holes, Galactic, Galactic"
    "\n           clusters, Laniakea-like), and the target Universe at 14: the insertion of Isotopic"
    "\n           shifts the target 13 -> 14 by exactly one level (integer arithmetic). The prefix"
    "\n           recommendation MO.n for Level 7 is RECORDED, not minted (ML is retired-ambiguous --"
    "\n           Level 6's original prefix before the IT.15(3) retag); minting happens at opening.",
    C4_ok, f"ladder: {ladder}")

print("=" * 104)
n_ok = sum(R)
print(f"\n  census_extension.py: {n_ok}/{len(R)} EXACT -- no floating point, no measured value.")
sys.exit(0 if n_ok == len(R) else 1)
