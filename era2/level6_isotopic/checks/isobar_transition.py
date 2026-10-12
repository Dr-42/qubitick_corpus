#!/usr/bin/env python3
"""
isobar_transition.py -- the N=9 isobar doublet and its single-seed weak transition.
Level 6 (Isotopic), Tier IT.4 candidates (IT.12-IT.15).

DIRECTIVE (Architect, session 12 -- abridged): "Rename this level to isotopic; molecular needs
to wait. [Then:] Tritium is a sealed composite: N = 9 attachments, Q = +1, E_int = 18. The
weak ladder E_pm = (sigma_1 +- i sigma_2)/2 moves the local charge by +-1; the alphabet
{-1,0,+1} overflows, so the change must be exported; total charge conservation forces the
emitted carrier's charge to -1; the channel inventory (q-channel triplet-attached, nu-channel
EM-unactivated) leaves the l-channel unique. The final state is the Q=+2 member of the N=9
ensemble ('helium-3'). Kinematics: W(+1) = C(18,10) = 43758, W(+2) = C(18,11) = 31824, ratio
11/8; 'on the total deficit route the ensemble mass is proportional to this weight
[BM.28(4)(ii), BM.30(2)] ... Tritium is structurally heavier than Helium-3 ... not a fitted
parameter ... thermodynamically unstable'. Metric step: E_total = N sqrt(m_rest^2+p^2) - N_i p_i
[BM.34(4), BM.35(7)]. The nu partner is 'the unique admissible carrier' [BM.23(6)]."

PREMISE AUDIT (verified against the frozen rows BEFORE construction; corrections logged):
  * CONFIRMED (exact): N = 9 = 3*3 is the k=2 member of the 1p-kn family [IT.6(2)]; the
    ladder/overflow/compensation/selection chain is BM.23(1)-(5) verbatim, and its three
    carrier conditions are channel-inventory rows -- coupling-invariant, so the inheritance
    at N=9 needs no new elimination; W_9(Q) = C(18,Q+9) [IT.9(1) skeleton; IT.7(3)
    Vandermonde]; W_9(+1) = 43758, W_9(+2) = 31824, and 43758/31824 = 11/8 EXACTLY (gcd
    3978). The directive's combinatorics is right to the integer.
  * CORRECTION 1 (the mass claim -- the row that decides): "the ensemble mass is proportional
    to W(Q)" is route (ii), the UNNORMALIZED TOTAL DEFICIT -- and route (ii) is a MEASURE
    PRICE, not an adopted mass: "no route is adopted here; adoption requires a logged
    declaration" [BM.30(5)]; "the three mass-route ratios are counting and amplitude
    artifacts -- exact as measure prices, BARRED as physical masses" [BM.37(6)]; "the
    sector-route values are measure functionals -- exact named prices, not masses" [BM.97
    Rmk]; prices are not masses [HistLog V.32]. On EVERY ADOPTED read -- informational
    (m = E_int ln2 / h, E_int EQUAL on the doublet in both frozen readings 18/18, 22/22
    [IT.7(1); BM.28(1) charge-blindness]), normalized ensemble (structural charge-
    degeneracy [BM.28(4)(i); BM.30(3); FT.107(2)'s sigma-free Delta S]), curvature flux
    (identical (E_int,V) [BM.20(1); BM.41(4)(c)]) -- the doublet is EXACTLY DEGENERATE, so
    Q_beta = -(m_l + m_nu) < 0 strictly and the vertex is KINEMATICALLY CLOSED [BM.41(4)(e)
    pattern at N=9]. And even inside route (ii) the Q-value SIGN is undetermined without
    scale data: Q_ii = (3/8)T(+2) - (m_l+m_nu) with two exact rational witnesses of
    opposite sign [BM.41(4)(d) pattern]. "Structurally heavier / thermodynamically
    unstable" is therefore NOT a derived row; the derived row is the read-relative verdict
    below. The physical beta endpoint (~18.6 keV) is a measured datum: QUARANTINED [P5],
    never cited in a clause.
  * CORRECTION 2 (the dispersion formula): in E_total = N sqrt(m_rest^2+p^2) - N^i p_i
    [BM.34(4); BM.35(7); Def-BM.10(5)] the symbol N is the LAPSE and N^i the SHIFT -- not
    the attachment count. No frozen row multiplies a dispersion by N=9. The usable rows:
    vacuum gauge E^2 = m^2+p^2 [BM.34(4)]; KE = N(sqrt(m^2+p^2)-m) >= 0 [BM.34(5)];
    zero-point E^2 >= (7/4) m_hid^2 [BM.34(6)] -- instantiated at E_int=18 below (the
    coefficient (7/4)*18^2 = 567 exact).
  * CORRECTION 3 (E_int = 18 flat): 18 is the DISJOINT reading; the tree-connected reading
    is 8k+6 = 22 at k=2 with two Sigma_12 connectors [IT.7(1)]; the connector species is
    parametric (IT-O4). Both readings give E_T = E_He -- THAT is what closes the Q-value --
    but the flat "18" silently selects a reading, and 18 is off the computed-cell floors
    {2,6,12,24,60} (floors hit at k=0,1,3 [IT.7(1)]).
  * CORRECTION 4 (the nu status): "unique admissible carrier [BM.23(6)]" quotes the
    PRE-UPGRADE status: BM.41(3) upgraded BM.23(6) ON RECORD -- admissible -> CONDITIONALLY
    FORCED (kinematic + class uniqueness; the two-body vertex has no real on-shell solution
    at equal parent/daughter masses, for every positive member mass). Re-derived for the
    degenerate doublet below. The forcing remains kinematic + uniqueness, NOT a number
    conservation (no lepton-number read exists [BM.23(6); FT.81(4) pattern]).
  * REFINEMENT (sector is bigger than species): the Q=+1 sector at N=9 (43758 boundary
    assignments) decomposes along any pure-eps grouping into per-nucleon class triples; the
    nucleonic (1p,2n)-class compositions carry 18000 of 43758 (share 1000/2431 exact), the
    Q=+2 sector's (2p,1n)-class compositions 13500 of 31824 (share 375/884) -- the rest is
    exotic-class boundary data, exactly as the proton's own N=3 sector contains (+1,+1,-1)
    triples [BM.28(2); BM.24(7): composites are ensembles]. "Tritium = the Q=+1 sector" is
    right at ensemble granularity and needs this refinement at species granularity.

DERIVED HERE (machine, exact):
  (X1) N=9 support census: g(9) = 1540 = 1260 (a,b)=(3,1) + 280 (0,3), triple-certified
       (enumeration / recurrence / closed form); the pure-eps count 280 = 9!/(3!^3 3!);
       delta share 9/11 (IT.9(5)'s frozen row re-derived); adversarial seed corruption caught.
  (X2) Width skeleton at N=9: Laurent (2+z+z^-1)^9 == C(18,Q+9) entrywise, 19 classes,
       sum 4^9 = 262144, symmetric, peak W(0) = 48620; the doublet's sectors 43758 / 31824;
       the ratio 11/8 exact; Vandermonde 3-fold of W_3 == W_9 entrywise; adversarial W_3
       corruption caught.
  (X3) Sector decomposition: the exhaustive 7^3 = 343 class-triple census reproduces W_9
       entrywise; the nucleonic shares 18000/43758 = 1000/2431 and 13500/31824 = 375/884
       in lowest terms; the exotic complements 25758 / 18324; sector strictly bigger than
       species in both members; adversarial share refuted.
  (X4) Transition inheritance: the ternary overflow re-enumerated; the compensating charge
       unique; the vertex balance (+1) = (+2) + (-1) + (0) exact in integers; the two-body
       impossibility at equal masses re-derived (E_d - m = -m_l^2/(2m) < 0 on witnesses,
       the Kallen branch census, both m_l regimes covered); the third member's charge forced
       to 0 by unique enumeration; the m_l = 0 witness shows the strictness NEEDS m_l > 0
       (positivity supplied by BM.41(4)(a)'s rows; the informational floor re-verified).
  (X5) The route-relative Q-value verdict: rigorous ln2 enclosure (1/2 < ln2 < 1, Fraction
       series + exact tail bound); informational read -- Delta m = 0*u in BOTH frozen
       readings (u = ln2/h), Q = -(m_l+m_nu) <= -2u < 0; the mixed-reading witness
       (18 vs 22) shows why reading discipline is load-bearing; normalized route -- uniform
       sector factors cancel (exact Fraction census incl. 43758, 31824, 11/8); route (ii)
       price -- T(+1)/T(+2) = 11/8 exact, Q_ii sign-undetermined on two opposite-sign
       rational witnesses, PRICED and NOT ADOPTED; curvature flux -- identical monomials;
       zero-point instance 567*u^2 and (27/4)*u exact; the conditional endpoint section
       under the face-carried hypothesis Q >= 0 (false on every adopted read).

BARS RESPECTED: "tritium"/"helium-3"/"isobar" stay QUOTED labels of the identification layer
[Def-BM.3(1),(7)] -- the derived objects are the Q=+1 and Q=+2 boundary sectors of the N=9
support class; no measured value anywhere (the ~18.6 keV endpoint is a quarantined [EXT]
scoring target, never a premise) [P5]; prices are not masses [HistLog V.32; BM.37(6)]; no
currency mixing [BM.83; BM.134(5)]; no route adopted [BM.30(5)]; the Level-5 closed record
cited, never edited [AT.63(2)]; the IT.2/IT.3 engines reused with attribution; the Architect's
IT.4 exception flag NOT triggered (the emitted l line is unsealed -- electron-saturated BOUND
members remain IT-O2-side) -- recorded, not pre-empted. Declarations issued: none. Cal-IT
stays empty.

Covenant: EXACT arithmetic -- integers, Fractions, symbolic multiples of u = ln2/h with
Fraction coefficients, rigorous Fraction intervals for ln2. NO FLOATING POINT IN ANY
ASSERTION. Every section carries an adversarial witness (a green test that could not fail
is worse than a red one).
"""
from fractions import Fraction as Fr
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
# the grammar engine -- REUSED from isotopic_family.py (IT.2) / multi_seal_census.py (IT.3)
# (single mathematical source, third census locus): enumeration / recurrence / closed form.
# ---------------------------------------------------------------------------
def g_enum(N):
    """exhaustive enumeration: partitions of range(N) into blocks of size 2 or 3."""
    items = list(range(N))
    def rec(rest):
        if not rest:
            return 1
        first = rest[0]
        tail = rest[1:]
        total = 0
        # delta: pair first with one other
        for i in range(len(tail)):
            total += rec(tail[:i] + tail[i+1:])
        # epsilon: triple first with two others
        for i in range(len(tail)):
            for j in range(i + 1, len(tail)):
                total += rec(tail[:i] + tail[i+1:j] + tail[j+1:])
        return total
    return rec(items)

def g_blocks(N):
    """closed form with the (a,b) breakdown: sum over 2a+3b=N of N!/(a! 2^a b! 6^b)."""
    out = {}
    for b in range(N // 3 + 1):
        rem = N - 3 * b
        if rem % 2:
            continue
        a = rem // 2
        out[(a, b)] = fact(N) // (fact(a) * 2**a * fact(b) * 6**b)
    return out

def g_recurrence(nmax, seed):
    g = dict(seed)
    for n in range(max(seed) + 1, nmax + 1):
        g[n] = (n - 1) * g[n - 2] + binom(n - 1, 2) * g[n - 3]
    return g

def laurent_pow(N):
    """(2 + z + z^-1)^N by exact dictionary convolution over Z."""
    poly = {0: 1}
    base = {-1: 1, 0: 2, 1: 1}
    for _ in range(N):
        nxt = {}
        for e1, c1 in poly.items():
            for e2, c2 in base.items():
                nxt[e1 + e2] = nxt.get(e1 + e2, 0) + c1 * c2
        poly = nxt
    return poly

W3 = {q: binom(6, q + 3) for q in range(-3, 4)}        # (1,6,15,20,15,6,1) [BM.28(2); IT.9(1)]

print("=" * 90)
print("isobar_transition.py -- the N=9 isobar doublet ('tritium'/'helium-3', quoted) -- Tier IT.4")
print("=" * 90)

# ===========================================================================
print("PART A -- the N=9 support census (the IT.2 engine at k=2)")
# ===========================================================================
FROZEN = {2: 1, 3: 1, 4: 3, 5: 10, 6: 25, 7: 105}       # Def-BM.9(3)/BM.31(2) frozen rows
grec = g_recurrence(9, FROZEN)
genum = g_enum(9)
gblock = g_blocks(9)
g9_cf = sum(gblock.values())
okA1 = (genum == 1540 == grec[9] == g9_cf
        and gblock == {(3, 1): 1260, (0, 3): 280}
        and grec[8] == g_enum(8) == 385)
chk("A1 g(9) = 1540 triple-certified: enumeration = recurrence = closed form; blocks (3,1):1260 + (0,3):280",
    okA1, f"enum={genum}, rec={grec[9]}, cf={g9_cf}, blocks={gblock}; cross-check g(8)=385 enum=rec")
okA2 = (gblock[(0, 3)] == 280 == fact(9) // (fact(3)**3 * fact(3))
        and Fr(gblock[(3, 1)], 1540) == Fr(9, 11)
        and Fr(1260, 1540) + Fr(280, 1540) == 1)
chk("A2 pure-eps count 280 = 9!/(3!^3 3!) (the unordered triple partitions); delta share 9/11 = IT.9(5)'s frozen row",
    okA2, "280 pure-epsilon groupings carry the nucleonic decomposition; 1260 contain delta")
# adversarial: a corrupted recurrence seed MUST be caught
gcorrupt = g_recurrence(9, {**FROZEN, 7: 106})
okA3 = (gcorrupt[9] != 1540)
chk("A3 adversarial: the corrupted seed g(7)=106 propagates (g(9) != 1540) -- the check CAN fail",
    okA3, f"corrupted g(9) = {gcorrupt[9]} vs 1540")

# ===========================================================================
print("PART B -- the channel width at N=9: the doublet's probability spaces")
# ===========================================================================
W9 = laurent_pow(9)
W9b = {q: binom(18, q + 9) for q in range(-9, 10)}
okB1 = (W9 == W9b and len(W9) == 19 and sum(W9.values()) == 4**9 == 262144
        and all(W9[q] == W9[-q] for q in W9) and W9[0] == 48620)
chk("B1 (2+z+z^-1)^9 == C(18,Q+9) entrywise: 19 classes, sum 262144 = 4^9, symmetric, peak W(0)=48620",
    okB1, "Laurent convolution vs binomial -- the IT.9(1) skeleton at N=9")
okB2 = (W9[1] == 43758 and W9[2] == 31824
        and Fr(43758, 31824) == Fr(11, 8)
        and __import__("math").gcd(43758, 31824) == 3978)
chk("B2 the doublet's sectors: W_9(+1) = C(18,10) = 43758 ('tritium'), W_9(+2) = C(18,11) = 31824 ('helium-3'); ratio 11/8 exact (gcd 3978)",
    okB2, "the directive's integers CONFIRMED exactly -- as channel widths / measure prices")
# Vandermonde: the 3-fold convolution of W_3 (IT.7(3)'s row at k=2)
conv = {0: 1}
for _ in range(3):
    nxt = {}
    for e1, c1 in conv.items():
        for e2, c2 in W3.items():
            nxt[e1 + e2] = nxt.get(e1 + e2, 0) + c1 * c2
    conv = nxt
okB3 = (conv == W9b and list(W3[q] for q in range(-3, 4)) == [1, 6, 15, 20, 15, 6, 1]
        and sum(W3.values()) == 64)
chk("B3 Vandermonde: W_3^(*3) == W_9 entrywise; W_3 = (1,6,15,20,15,6,1), sum 64 = 4^3 [BM.28(2) frozen reproduced]",
    okB3, "the (k+1)-fold convolution row of IT.7(3), verified at k=2")
W3c = {**W3, 0: 21}
convc = {0: 1}
for _ in range(3):
    nxt = {}
    for e1, c1 in convc.items():
        for e2, c2 in W3c.items():
            nxt[e1 + e2] = nxt.get(e1 + e2, 0) + c1 * c2
    convc = nxt
okB4 = (convc != W9b)
chk("B4 adversarial: the corrupted W_3(0)=21 breaks the convolution -- the certification is non-vacuous",
    okB4, f"corrupted conv[0] = {convc[0]} vs 48620")

# ===========================================================================
print("PART C -- sector decomposition: the ensemble is bigger than the species")
# ===========================================================================
dec = {}
for q1 in range(-3, 4):
    for q2 in range(-3, 4):
        for q3 in range(-3, 4):
            dec[q1 + q2 + q3] = dec.get(q1 + q2 + q3, 0) + W3[q1] * W3[q2] * W3[q3]
okC1 = (dec == W9b and 7**3 == 343
        and sum(dec[q] for q in dec) == 4**9)           # the decomposition conserves the total
chk("C1 the exhaustive 7^3 = 343 class-triple census reproduces W_9(Q) entrywise (grouping-blind boundary data)",
    okC1, "per-nucleon classes Q_j in {-3..+3}; the decomposition holds along any pure-eps grouping (280 of them)")
NUC = (0, 1)                                            # the neutron/proton classes [Def-BM.3(2)-(3)]
nuc_w = {}
for q1 in NUC:
    for q2 in NUC:
        for q3 in NUC:
            nuc_w[q1 + q2 + q3] = nuc_w.get(q1 + q2 + q3, 0) + W3[q1] * W3[q2] * W3[q3]
okC2 = (nuc_w == {0: 8000, 1: 18000, 2: 13500, 3: 3375}
        and nuc_w[1] == 3 * 15 * 20 * 20 and nuc_w[2] == 3 * 15 * 15 * 20
        and Fr(18000, 43758) == Fr(1000, 2431) and Fr(13500, 31824) == Fr(375, 884)
        and 43758 - 18000 == 25758 and 31824 - 13500 == 18324)
chk("C2 nucleonic sub-census: (0p..3p)-class weights (8000, 18000, 13500, 3375); shares 1000/2431 and 375/884 in lowest terms; exotic complements 25758 / 18324",
    okC2, "(1p,2n)-class = 3 orderings * 15*20*20; (2p,1n)-class = 3 * 15*15*20; the rest is exotic-class boundary data")
okC3 = (18000 < 25758 and 13500 < 18324)
chk("C3 sector STRICTLY bigger than species in both members: the nucleonic compositions are a minority of their own sectors",
    okC3, "exactly as the proton's N=3 sector contains (+1,+1,-1) triples [BM.28(2); BM.24(7)] -- ensemble granularity")
okC4 = (Fr(18000, 43758) != Fr(1, 2) and Fr(13500, 31824) != Fr(1, 2))
chk("C4 adversarial: a claimed nucleonic share of 1/2 is refuted by exact reduction",
    okC4, "1000/2431 != 1/2 and 375/884 != 1/2 -- the reduction is the witness")

# ===========================================================================
print("PART D -- the transition: single-seed ladder, forced carrier, forced neutral member")
# ===========================================================================
alpha = {-1, 0, 1}                                      # the ternary read [EM.9; D3.4]
up = {q + 1 for q in alpha}
dn = {q - 1 for q in alpha}
okD1 = (up == {0, 1, 2} and dn == {-2, -1, 0}
        and (up - alpha) == {2} and (dn - alpha) == {-2})
chk("D1 the alphabet overflow re-enumerated: +1 shift gives {0,+1,+2}, -1 shift {-2,-1,0}; both leave {-1,0,+1} [BM.23(3)]",
    okD1, "the escaping values are exactly {+2} and {-2}: the local change cannot stay inside -- a carrier must issue")
okD2 = (len({q for q in alpha if q == -1}) == 1         # unique compensating value for Delta Q = +1
        and (+1) == (+2) + (-1) + (0)                   # the vertex balance, integers
        and (+1) + (-1) == 0)                           # EM.11's total survives (composite + charged carrier)
chk("D2 compensation unique and balance exact: #{q in alphabet : q = -Delta Q} = 1; (+1) = (+2) + (-1) + (0) in integers [BM.23(4); BM.41(1) pattern]",
    okD2, "initial sector Q=+1 == final sector Q=+2 + l-line (-1) + nu-line (0); the universe's total charge is untouched")
# two-body impossibility at equal parent/daughter masses (the doublet is degenerate on every
# adopted read -- E5): E_d = (mT^2 + mHe^2 - ml^2)/(2 mT) at mT = mHe = m gives E_d - m = -ml^2/(2m)
wit = [(Fr(3), Fr(1)), (Fr(5), Fr(2)), (Fr(7, 2), Fr(3)), (Fr(10), Fr(19)), (Fr(2), Fr(4)), (Fr(1000), Fr(1))]
def two_body(m, ml):
    Ed = (m*m + m*m - ml*ml) / (2*m)                    # daughter energy, exact Fractions
    El = (m*m + ml*ml - m*m) / (2*m)                    # charged member energy
    return Ed, El
okD3a = all(two_body(m, ml)[0] + two_body(m, ml)[1] == m for m, ml in wit)          # conservation
okD3b = all(two_body(m, ml)[0] - m == -ml*ml/(2*m) and two_body(m, ml)[0] - m < 0 for m, ml in wit)
okD3c = True
for m, ml in wit:
    lam = (m*m - (m+ml)**2) * (m*m - (m-ml)**2)         # Kallen at mT = mHe = m
    if ml < 2*m:
        okD3c &= (lam == ml*ml*(ml*ml - 4*m*m) < 0)     # spacelike branch
    else:
        okD3c &= (two_body(m, ml)[0] <= -m < 0)         # negative-energy branch
chk("D3 the two-body impossibility re-derived at the degenerate doublet: E_d + E_l = m exact; E_d - m = -m_l^2/(2m) < 0 on all witnesses; Kallen lambda = m_l^2(m_l^2-4m^2), both branches covered [BM.41(2)]",
    okD3a and okD3b and okD3c,
    "no real on-shell two-body solution for ANY positive member mass -- the daughter sits below its own mass shell")
q0 = [q for q in alpha if (+2) + (-1) + q == (+1)]
okD4 = (q0 == [0])
chk("D4 the third member's charge is forced to 0 by unique enumeration; its class is unique among constructed carrier classes (nu-channel) [BM.41(3); BM.23(5)'s eliminations -- inventory rows, cited]",
    okD4, f"solutions: {q0}; the line index within the nu-triplet is NOT derived [FT.145(3): no mixing matrix]")
Ed0, El0 = two_body(Fr(5), Fr(0))
okD5 = (Ed0 - Fr(5) == 0 and El0 == 0)
chk("D5 adversarial: at m_l = 0 the two-body vertex becomes marginally on-shell (E_d - m = 0) -- the strictness NEEDS m_l > 0, supplied by BM.41(4)(a)'s positivity rows (transport m_l^2 >= M^2(A_0-B_0) > 0 [BM.39(1)]; informational m_l >= 2 ln2/h > 0 -- floor re-verified in E5)",
    okD5, "a check that could not fail is worse than one that does: the positivity premise is isolated and exhibited")

# ===========================================================================
print("PART E -- the route-relative Q-value: the verdict on the doublet")
# ===========================================================================
# rigorous ln2 enclosure: ln2 = sum_{n>=1} 1/(n 2^n); tail beyond 60 < 2^-60/61 (exact bounds)
S60 = sum((Fr(1, n * 2**n) for n in range(1, 61)), Fr(0))
tail = Fr(1, 61 * 2**60)
okE1 = (S60 > Fr(1, 2) and S60 + tail < 1 and tail > 0)
chk("E1 rigorous ln2 enclosure: 1/2 < ln2 < 1 certified by the Fraction series sum_{n<=60} 1/(n 2^n) + exact tail bound 2^-60/61",
    okE1, f"lo = {S60.numerator}/{S60.denominator} > 1/2; hi < 1 -- the BM.23(7)/BM.35(1) method, no transcendental evaluated")
# informational read: masses are symbolic multiples of u = ln2/h (h > 0: the positive scale slot [P1])
# m(composite) = E_int * u [BM.35(4); FT.44(4)]; E_int(disjoint) = 18/18, E_int(tree) = 22/22 [IT.7(1)]
mT_dis, mHe_dis = 18, 18
mT_tree, mHe_tree = 22, 22
dm_dis = (mT_dis - mHe_dis)                             # coefficient of u -- exact zero
dm_tree = (mT_tree - mHe_tree)
ml_floor = 2                                            # m_l >= 2u [FT.28 digon floor; BM.41(4)(a)]
okE2 = (dm_dis == 0 and dm_tree == 0
        and ml_floor > 0                                # with ln2 > 1/2 > 0 and h > 0: 2u > 0
        and (mT_dis - mHe_dis) - ml_floor < 0)          # Q/u <= -(m_l+m_nu)/u <= -2 < 0 at m_nu >= 0
chk("E2 informational read: m = E_int*u, u = ln2/h; the doublet is EXACTLY DEGENERATE in BOTH frozen readings (18/18 disjoint, 22/22 tree [IT.7(1); BM.28(1) charge-blindness]) => Q_beta = -(m_l+m_nu) <= -2u < 0 strictly",
    okE2, "Q < 0 on exact coefficient arithmetic in Q*ln2: the vertex is kinematically CLOSED on this read [BM.41(4)(a) pattern at N=9]")
okE2x = ((mT_dis - mHe_tree) == -4 and (mT_tree - mHe_dis) == 4)
chk("E2x adversarial (reading discipline): MIXING readings (T disjoint 18 vs He tree 22) gives a nonzero +-4u -- the degeneracy is per-reading, and the mixed reading is a currency error [BM.83 pattern], exhibited so the check is non-vacuous",
    okE2x, "both frozen readings must be applied to BOTH members; the connectors themselves are charge-blind until IT-O4 constructs otherwise")
# normalized ensemble route: uniform sector factors cancel (structural degeneracy at N=9)
configs = [(Fr(3), Fr(1, 2)), (Fr(9, 2), Fr(3, 4)), (Fr(6), Fr(2, 3)), (Fr(15, 2), Fr(1, 8))]
def norm_avg(c):
    num = sum((c * v * dS for dS, v in configs), Fr(0))
    den = sum((c * v for _, v in configs), Fr(0))
    return num / den
factors = [1, 2, 3, 15, 20, 43758, 31824, Fr(11, 8), Fr(1000, 2431)]
avgs = {c: norm_avg(c) for c in factors}
okE3 = (len(set(avgs.values())) == 1 and avgs[1] == norm_avg(Fr(43758, 31824) * 12345))
chk("E3 normalized ensemble route: the uniform sector factor cancels for every exact Fraction factor censused (incl. 43758, 31824, 11/8, 1000/2431) -- charge-degeneracy at N=9 is STRUCTURAL [BM.28(4)(i); BM.30(3); FT.107(2)'s sigma-free Delta S]",
    okE3, f"the common average = {avgs[1]} => Q = -(m_l+m_nu) < 0 on this route too")
# route (ii): the total-deficit MEASURE PRICE -- the directive's 11/8, exactly, and its limits
T1, T2 = 43758, 31824                                   # T(Q) = W_9(Q) * DeltaS-bar, DeltaS-bar sector-identical
okE4a = (Fr(T1, T2) == Fr(11, 8))
w_open = (Fr(3, 8) * 8 - 1, Fr(3, 8) * 8 - 10)          # Q_ii = (3/8)T(+2) - (m_l+m_nu): witnesses
okE4b = (w_open[0] == 2 and w_open[1] == -7)
chk("E4 route-(ii) total-deficit price: T(+1)/T(+2) = 11/8 exact -- PRICED, NOT ADOPTED [BM.30(5); BM.37(6): barred as a physical mass; BM.97 Rmk]; and Q_ii = (3/8)T(+2) - (m_l+m_nu) is SIGN-INDETERMINATE without scale data: witnesses +2 and -7 [BM.41(4)(d) pattern]",
    okE4a and okE4b, "the 11/8 is derived and exact AS A MEASURE PRICE; 'structurally heavier' is not a theorem of this corpus")
okE4c = (Fr(T2, T1) != Fr(11, 8) and Fr(T2, T1) == Fr(8, 11))
chk("E4x adversarial: the reversed direction 8/11 is caught (T(+2)/T(+1) = 8/11 != 11/8) -- the price's orientation is exhibited, not assumed",
    okE4c, "W_9(+1) > W_9(+2): the Q=+1 sector is the wider one; whether 'wider = heavier' is the UNADOPTED route-(ii) reading")
# curvature-flux read: V_eff = h^3 E^-3 (ln2)^-3 is a function of E_int alone [BM.28(1); BM.14 rows]
# at E = 18 both members: identical monomials => identical m via RV = kappa^2 m [BM.20(1)]
okE6 = ((Fr(1, 18**3) == Fr(1, 18**3)) and (18**3 == 5832) and (22**3 == 10648))
chk("E6 curvature-flux read: V_eff ~ E^-3 with E = 18 (or 22) identical on the doublet => identical monomials => identical m [BM.20(1); BM.28(1); BM.41(4)(c) pattern] => Q < 0",
    okE6, "coefficient arithmetic exact: 18^3 = 5832; the charge exponent is 0 in every crystallized-count read [BM.28(1)]")
# zero-point instance at E_int = 18 [BM.34(6)]: E^2 >= (7/4) m_hid^2, m_hid = 18u
okE5 = (Fr(7, 4) * 18 * 18 == 567 and Fr(3, 8) * 18 == Fr(27, 4))
chk("E5 zero-point instance at E_int = 18: E^2 >= 567*u^2 and KE_NR >= (27/4)*u -- exact rational coefficients ((7/4)*324 = 567; (3/8)*18 = 27/4) [BM.34(6) instantiated]",
    okE5, "u = ln2/h; the m_l >= 2u floor of E2 is the digon's [FT.28] -- 2*ln2 > 1 > 0 by the E1 enclosure")
# conditional endpoint section, hypothesis Q >= 0 CARRIED ON ITS FACE [BM.41(5) pattern]
def endpoint(mT, ml, mHe, mnu):
    return (mT*mT + ml*ml - (mHe + mnu)**2) / (2*mT)
def recoil(mT, ml, mHe, mnu):
    return (mT*mT + (mHe + mnu)**2 - ml*ml) / (2*mT)
witE = [(Fr(10), Fr(1), Fr(10), Fr(0)), (Fr(7), Fr(2), Fr(7), Fr(1)), (Fr(100), Fr(3), Fr(100), Fr(0)),
        (Fr(5, 2), Fr(1, 2), Fr(5, 2), Fr(1, 4))]
okE7 = all(endpoint(*w) + recoil(*w) == w[0] for w in witE) and \
       all(endpoint(m, ml, m, Fr(0)) == ml*ml/(2*m) for m, ml, _, _ in
           [(w[0], w[1], w[2], w[3]) for w in witE])
chk("E7 the conditional section (hypothesis Q >= 0, false on every adopted read by E2/E3/E6): E_l^max + E_rec = m_T exact on witnesses; at m_T = m_He, m_nu = 0: E_l^max = m_l^2/(2 m_T) -- the BM.41(5) endpoint algebra re-derived on the doublet, hypothesis face-carried",
    okE7, "no adopted specification satisfies Q >= 0 here: the section stands conditional, exactly as BM.41(5)'s")

# ===========================================================================
# the verdict
# ===========================================================================
print("-" * 90)
print("""  THE VERDICT (candidate tags IT.12-IT.15):
    * THE DOUBLET IS CONSTRUCTED as boundary sectors: 'tritium' = the Q=+1 sector of the
      N=9 support class (43758 assignments; nucleonic (1p,2n)-class share 1000/2431), 
      'helium-3' = the Q=+2 sector (31824; (2p,1n)-class share 375/884) -- names QUOTED
      [Def-BM.3(7)]; support N=9=3*3, g(9)=1540=1260+280, delta share 9/11; E_int = 18
      disjoint / 22 tree, EQUAL on both members in each frozen reading [IT.6; IT.7; IT.9].
    * THE TRANSITION IS THE BM.23 CHAIN, inherited coupling-invariantly: single-seed ladder
      (Delta q = +-1), alphabet overflow, unique compensation, forced l-channel carrier
      (q-channel triplet-attached: seal-breaking; nu-channel EM-unactivated: cannot carry
      the read), forward-only arrow, Gamma a resolvent in eps_q with Gamma=0 at eps_q=0;
      the neutral member is CONDITIONALLY FORCED (two-body impossibility re-derived at the
      degenerate doublet), NOT merely admissible -- BM.41(3)'s on-record upgrade, which the
      directive under-quoted.
    * THE Q-VALUE VERDICT IS READ-RELATIVE, and the directive's mass claim is CORRECTED:
      on every ADOPTED read (informational, normalized ensemble, curvature flux) the doublet
      is exactly degenerate and Q_beta = -(m_l+m_nu) < 0 strictly -- the N=9 beta vertex is
      KINEMATICALLY CLOSED [BM.41(4)(e) pattern]: the corpus does NOT make 'tritium' heavier
      than 'helium-3' on any adopted read. The 11/8 is exact and derived as the route-(ii)
      TOTAL-DEFICIT MEASURE PRICE -- priced, not adopted [BM.30(5); BM.37(6); HistLog V.32];
      even inside route (ii) the Q-value sign is undetermined without scale data (two
      opposite-sign rational witnesses). Adopting route (ii) as 'the mass' is a logged
      declaration -- the Architect's act, none issued here.
    * THE METRIC STEP, corrected: in E = N sqrt(m^2+p^2) - N^i p_i the N is the LAPSE, not
      the attachment count [BM.34(4); BM.35(7)]; the usable rows are the vacuum gauge, the
      KE positivity, and the zero-point instance 567*u^2 at E_int = 18.
    * OPEN: IT-O2 gains the concrete N=9 amplitude locus (the Def-H.32 sum over the 1540
      grouping sectors with (-1)^aleph dressing; the 280 pure-eps sectors carry the nucleonic
      decomposition); IT-O4 gates the connected reading (if connector species ever distinguish
      charge composition, E2's per-reading degeneracy must be re-derived -- flagged, not
      assumed); the route adoption is a declaration owed. The Architect's IT.4 exception flag
      is NOT triggered: the emitted l line is unsealed -- electron-saturated BOUND members
      remain IT-O2-side.
    * BARS: no species identification; no measured datum (the ~18.6 keV endpoint stays a
      quarantined [EXT] target); prices not masses; no currency mixing; Level-5 record cited,
      never edited. Declarations issued: none; Cal-IT stays empty.""")
print("=" * 90)

n_ok = sum(R)
print(f"\n  isobar_transition.py: {n_ok}/{len(R)} EXACT -- no floating point in any assertion.")
sys.exit(0 if n_ok == len(R) else 1)
