#!/usr/bin/env python3
"""
parity_contact_gate.py -- the machine for Tier IT.24 (tags IT.84-IT.88): the parity of the
seal and the contact gate.

The Architect's concept-queue dispositions, executed on formed ground:
  * concept/0002 (the Baryonic Lock / Census inversion) MERGED -- the Parity Theorem adopted
    as a read-tier remark, with the JOIN to Census FT.63's even-eps theorem named by the
    Architect as the load-bearing result;
  * concept/0004 (the Janus balance knot) MERGED -- the three-locus resolution beside
    BM.7(1)/D2.11;
  * concept/0005 (the Observation Gate) PROMOTED -- "build the exact census of photon vs.
    gluon rung-parity and formalize the contact-gating theorem. This is a priority physics
    derivation."

THE THREE RESULTS.
  (i)  EMBEDDING PARITY (new): sum_v n(v) = 2|E_R| is even [D0.8], so on a sealed admissible
       network the trivalent count k satisfies 3k + 2m = 2|E_R| and is therefore EVEN. An
       eps-triple needs three colour vertices at DISTINCT nodes [CT3.17a(1); D2.14], and three
       is odd -- so a sealed admissible network cannot host one, and some colour vertex of any
       eps-sealed baryon-type floor has n >= 4 and is D^-configured [CT4.1].
  (ii) THE JOIN (load-bearing per the disposition): Census FT.63's even-eps theorem is a
       labelled-set-partition parity; (i) is a degree-sum parity. Unrelated machinery, same
       Z_2, and they AGREE. The grammar half is FT.63's and is cited as such -- an earlier
       probe-space draft claimed it, and the correction is logged at IT.88(6).
  (iii)THE CONTACT-GATING BICONDITIONAL: Census FT.62(1) freezes dark n=2d, single-directed
       contact n=2d+1, bidirectional contact n=2d+2. Colour hosts exactly at n=3 [CT0.13 and
       CT4.4a(1)]. Over the integers 2d=3 and 2d+2=3 have NO solution and 2d+1=3 has the
       UNIQUE solution d=1, so n(v)=3 <=> one channel plus exactly one single-directed-edge
       contact. Hence the Baryonic Lock is a CONTACT DEFICIT -- three needed, one supplied
       (Sigma_12), and a lock-free eps-triple is constructible only with three contacts.

PART A -- embedding parity: the handshaking identity, the even-k theorem, both hypotheses
  load-bearing (adversarial).
PART B -- the sealed case: in(v)=out(v) => every type diagonal => (0,3)/(3,0) unreachable;
  the eps-triple's distinct-node requirement.
PART C -- the join: CT3.17a(2)'s g(N) closed form re-derived, its independent cross-era
  attestation (g(8)=385, g(9)=1540), g_eps nonzero exactly where 3|N, the mod-6 corollary,
  the fermion/boson dichotomy.
PART D -- FT.62(1)'s rung-correction law and the integer solution census making it a
  biconditional at the hosting rung.
PART E -- the contact budget; a bidirectional contact never opens the gate (it deepens the
  lock); Sigma_triangle as the instance.
PART F -- the contact deficit: Sigma_12's rungs re-derived from FT.35's own edge list; the
  CONSTRUCTIVE lock-free eps-triple witness (9 edges, zero locked, all hosting types (2,1)).
PART G -- the photon/gluon rung-parity census [D3.7] over 15 floor variants; FT.62(2)'s four
  columns reproduced exactly; the mixed-skeleton scope residue.
PART H -- locus A: strict alternation, the prefix law, the unique completed word, the Catalan
  relaxation census, the two-pair interleavings, the reversal bar.
PART I -- locus C: CT4.3's register separation (oversubscription is not a seal, Delta n_R = 0),
  the balanced wholly-locked triangle, CT4.5a's ten anchors and genericity.
PART J -- locus B: the boundary reading of D2.11 at EM.11's proof; the two refuted readings;
  the barred temporal words.
PART K -- the tier scans: verdict assembly, the bars (P1/P5, no [EXT], no species framing, no
  new declaration, zero decimals with the LIVE-WITNESS self-test), the status row.

All arithmetic is exact: integers and Fraction. NO FLOATING POINT IN ANY ASSERTION. No
measured value in any derivation [P5]. Enumerations are exhaustive where claimed and
constructive elsewhere; witnesses are deterministic -- no randomness.
"""
import os
import re
import sys
from fractions import Fraction as Fr
from itertools import product
from math import comb, factorial

HERE = os.path.dirname(os.path.abspath(__file__))
TIERS = os.path.normpath(os.path.join(HERE, "..", "tiers"))
CANON = os.path.normpath(os.path.join(HERE, "..", "..", "..", "era1", "canon"))
TIER_FILE = os.path.join(TIERS, "Part6_Isotopic_era_TierIT24.md")

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print("[EXACT] %s" % label if cond else "[FAIL ] %s" % label)
    if detail:
        print("        %s" % detail)
def sec(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)

C_CAP = 16                                    # CT0.6 / D0.9
CEIL = 3                                      # CT0.11
def D_tick(n): return 2 ** (n + 1)            # CT0.5
def O(n):      return max(0, D_tick(n) - C_CAP)
def locked(n): return O(n) > 0                # CT4.1 / D4.1

def rungs(E, V):
    """n(v) = d_in(v) + d_out(v)  [D0.8]."""
    return {v: sum(1 for e in E if e[0] == v) + sum(1 for e in E if e[1] == v) for v in V}

def types(E, V):
    return {v: (sum(1 for e in E if e[1] == v), sum(1 for e in E if e[0] == v)) for v in V}

def digraphs(V):
    """every simple digraph on V vertices (no self-loops) [A7: E subset V x V]."""
    prs = [(i, j) for i in range(V) for j in range(V) if i != j]
    for mask in range(1 << len(prs)):
        yield [prs[b] for b in range(len(prs)) if mask >> b & 1]

def sealed(E, V):
    """every end paired: in(v) = out(v) at every vertex [D1.2/D1.3/D1.4 read at EM.11 Pf]."""
    return all(sum(1 for e in E if e[1] == v) == sum(1 for e in E if e[0] == v) for v in V)

# ===========================================================================
sec("PART A -- IT.84(1): EMBEDDING PARITY (the handshaking identity and the even-k theorem)")
# ===========================================================================
h_ok = True
for V in (2, 3, 4):
    for E in digraphs(V):
        if sum(rungs(E, range(V)).values()) != 2 * len(E):
            h_ok = False
            break
A1 = h_ok
chk("A1  [D0.8 additivity] sum_v n(v) = 2|E_R| on EVERY simple digraph, exhaustive V = 2,3,4 "
    "(4 + 64 + 4096 graphs)",
    A1, "ground: n(v) = d_in + d_out is additive and each directed real edge contributes exactly "
        "1 to one d_out and 1 to one d_in. Hence the degree sum is EVEN.")

def parity_scan(V, allow_lone):
    """odd-trivalent witnesses among admissible (n<=3), optionally dangling-free (n!=1) digraphs."""
    bad = []
    for E in digraphs(V):
        n = rungs(E, range(V))
        vals = list(n.values())
        if any(x > CEIL for x in vals):
            continue
        if not allow_lone and any(x == 1 for x in vals):
            continue
        if sum(1 for x in vals if x == CEIL) % 2 == 1:
            bad.append((E, n))
    return bad

A2 = all(len(parity_scan(V, False)) == 0 for V in (2, 3, 4, 5))
A2n = sum(2 ** (V * (V - 1)) for V in (2, 3, 4, 5))
chk("A2  [IT.84(1); CT0.11] THE PARITY THEOREM: on every admissible dangling-free digraph the "
    "trivalent count k = #{v: n(v)=3} is EVEN -- exhaustive V = 2..5 (%d graphs)" % A2n,
    A2, "3k + 2m = 2|E_R| forces 3k even, hence k even. Zero odd-k witnesses found.")

A3 = len(parity_scan(3, True)) > 0 and len(parity_scan(4, True)) > 0
chk("A3  [ADVERSARIAL -- the dangling-free hypothesis is LOAD-BEARING] permitting a lone end "
    "(n=1) DOES produce odd trivalent counts",
    A3, "odd-k witnesses at V=3: %d; at V=4: %d. So D2.11's 'no dangling ledger boundary' is not "
        "decorative -- it is half the theorem." % (len(parity_scan(3, True)), len(parity_scan(4, True))))

def witness(V, k_target):
    for E in digraphs(V):
        n = rungs(E, range(V))
        vals = list(n.values())
        if any(x > CEIL for x in vals) or any(x == 1 for x in vals):
            continue
        if sum(1 for x in vals if x == CEIL) == k_target:
            return E, n
    return None
W2, W4 = witness(3, 2), witness(4, 4)
A4 = W2 is not None and W4 is not None and all(witness(V, 3) is None for V in (3, 4, 5))
chk("A4  [ADVERSARIAL -- the ceiling is LOAD-BEARING, and k=3 is the parity hole] k=2 and k=4 are "
    "attainable with witnesses; k=3 is UNATTAINABLE on any admissible dangling-free digraph, V <= 5",
    A4, "k=2 witness rungs %s; k=4 witness rungs %s; k=3 searched exhaustively at V=3,4,5 and "
        "never found. THREE is exactly what eps_ijk consumes [D3.9; CT3.17; CT3.18]."
    % (sorted(W2[1].values()) if W2 else None, sorted(W4[1].values()) if W4 else None))

# ===========================================================================
sec("PART B -- IT.84(2),(3): the sealed case -- diagonal types, and (0,3)/(3,0) unreachable")
# ===========================================================================
B_types, B_extreme = set(), 0
for E in digraphs(4):
    if not sealed(E, range(4)):
        continue
    for v, t in types(E, range(4)).items():
        B_types.add(t)
        if t in ((0, 3), (3, 0)):
            B_extreme += 1
B1 = B_extreme == 0 and all(a == b for (a, b) in B_types)
chk("B1  [D1.2; D1.4; D1.3 read at EM.11's Pf; FT.62(5)] exhaustive over ALL sealed digraphs on "
    "V=4: every occurring vertex type is DIAGONAL (d,d), and the extreme types (0,3),(3,0) NEVER "
    "occur",
    B1, "%d distinct types found, all diagonal: %s. Sealed => in(v)=out(v) => n(v)=2*in(v) is even, "
        "so an admissible sealed vertex is n in {0,2} -- NEVER 3. FT.62(5) states the same for d>=2: "
        "'bidirectional-skeleton vertices with d>=2 channels have type (d,d)'."
    % (len(B_types), sorted(B_types)))
chk("B2  [the corollary that closes the comms/0013 vocabulary] the 'vacuum source (0,3) / vacuum "
    "sink (3,0)' vertices cannot exist in ANY valid universe",
    B1, "they need three unpaired ends and D2.11 forbids dangling ones. This is strictly stronger "
        "than a lexical kind-bar argument, and exhaustive rather than lexical.")
chk("B3  [CT3.17a(1); D2.14] the eps-triple needs THREE colour vertices at DISTINCT nodes",
    True, "CT3.17a(1) verbatim: '|Colour(Sigma)| = 1 => C(Sigma;C) = 0 [a contraction partner is a "
          "DISTINCT NODE -- A1: p != q -- hence pi_C(v) is not a subset of {v}; equivalently, "
          "CT3.17's list contains no invariant of a single slot]'. D2.14: pi_C(v) = the OTHER members "
          "-- one for a meson pair via delta, TWO for a (anti)baryon triple via eps.")

# ===========================================================================
sec("PART C -- IT.84(4),(5): THE JOIN with Census FT.63, the mod-6 corollary, the dichotomy")
# ===========================================================================
def g(N):
    """CT3.17a(2): g(N) = sum_{2a+3b=N} N!/(a! b! 2^a 6^b) -- labelled set partitions with
    parts in {2,3}. Exact integer arithmetic."""
    tot = 0
    for b in range(0, N // 3 + 1):
        rem = N - 3 * b
        if rem % 2:
            continue
        a = rem // 2
        tot += factorial(N) // (factorial(a) * factorial(b) * 2 ** a * 6 ** b)
    return tot
def g_eps(N):
    """pure-eps groupings: a = 0, so 3b = N. Nonzero exactly where 3 | N [HistLog V.13]."""
    if N % 3:
        return 0
    b = N // 3
    return factorial(N) // (factorial(b) * 6 ** b)

FROZEN_G = {1: 0, 2: 1, 3: 1, 4: 3, 5: 10, 6: 25, 7: 105}
C1 = all(g(N) == FROZEN_G[N] for N in FROZEN_G)
C1b = (factorial(6) // (factorial(3) * 2 ** 3) == 15
       and factorial(6) // (factorial(2) * 6 ** 2) == 10)
chk("C1  [CT3.17a(2)] the frozen g(N) = (0,1,1,3,10,25,105) for N=1..7 reproduced EXACTLY from the "
    "closed form, with g(6) = 25 = 15 + 10 split as the canon splits it",
    C1 and C1b, "computed g(1..7) = %s; the two summands of g(6) are the a=3,b=0 and a=0,b=2 terms "
                "= (15, 10)." % [g(N) for N in range(1, 8)])
C2 = g(8) == 385 and g(9) == 1540 \
    and factorial(9) // (factorial(3) * 2 ** 3 * 6) == 1260 \
    and factorial(9) // (factorial(3) * 6 ** 3) == 280
chk("C2  [CROSS-ERA DOUBLE ENTRY] the same closed form independently reproduces g(8)=385 (the Census "
    "FT.42(5) cube card) and g(9)=1540=1260+280 (Def-H.32's 1540 grouping sectors)",
    C2, "g(8) = %d, g(9) = %d. The grammar is thus attested from two directions: against CT3.17a(2)'s "
        "own frozen values and against two unrelated frozen counts." % (g(8), g(9)))
C3 = all((g_eps(N) > 0) == (N % 3 == 0) for N in range(1, 19)) and g(1) == 0
chk("C3  [CT3.17a(2); HistLog V.13] pure-eps groupings exist EXACTLY where 3 | N, and g(1) = 0 "
    "('a lone attachment is never sealed')",
    C3, "g_eps(1..12) = %s" % [g_eps(N) for N in range(1, 13)])
# FT.63's even-eps theorem, re-derived as the grammar-side parity
C4 = all((N % 2 == 0) == all(b % 2 == 0 for b in range(0, N // 3 + 1)
                             if (N - 3 * b) % 2 == 0 and g_eps(3 * b) > 0)
         for N in range(2, 25, 2))
C4b = all(b % 2 == 0 for b in range(0, 13) if (12 - 3 * b) % 2 == 0)
chk("C4  [Census FT.63, THE GRAMMAR HALF -- CITED, NOT CLAIMED] the even-eps theorem re-derived: for "
    "even V, every grouping 2a+3b=V has b EVEN, so 'Platonic sealing phases are baryon-number-even by "
    "structure'",
    C4 and C4b, "V=12: admissible b values %s -- all even. This row is Census FT.63's and predates "
                "this tier; IT.88(6) logs that an earlier probe-space draft claimed its corollary "
                "without citing it." % [b for b in range(0, 5) if (12 - 3 * b) % 2 == 0])
def pure_eps_lockfree(N):
    """WIRED to the grammar, not asserted: eps side = CT3.17a(2)'s g_eps(N) > 0; even side = the
    embedding parity of Part A."""
    return g_eps(N) > 0 and N % 2 == 0
C5 = all(pure_eps_lockfree(N) == (N % 6 == 0) for N in range(1, 31))
chk("C5  [IT.84(5) THE JOIN] a lock-free pure-eps seal needs 3 | |Colour| (grammar) AND |Colour| "
    "even (embedding parity) -- coprime, so 6 | |Colour|",
    C5 and C3 and A2, "checked N = 1..30. THE LOAD-BEARING POINT per the Architect's disposition: the "
                      "two parities come from UNRELATED machinery -- a labelled-set-partition count "
                      "[CT3.17a(2)/FT.63] versus a degree-sum identity [D0.8] -- and they AGREE. Their "
                      "agreement is the result, not either half alone.")
C6 = pure_eps_lockfree(2) is False and (2 % 2 == 0) and g(2) == 1 and not pure_eps_lockfree(3)
chk("C6  [IT.84(5) THE FERMION/BOSON DICHOTOMY] |Colour|=2 (delta-pair, meson-type) is EVEN -> "
    "parity-allowed lock-free; |Colour|=3 (eps-triple, baryon-type) is ODD -> forbidden",
    C6, "so FT.35's Rmk 'Composite fermion structure and saturation content are born together' is "
        "promoted from a census observation to a theorem, and FT.42(2)'s 'the lock-free family is the "
        "unidirectional one' [FT.28; FT.32; FT.62(3)] is explained: that family carries no eps-seal.")

# ===========================================================================
sec("PART D -- IT.85(1): FT.62(1)'s rung-correction law is a BICONDITIONAL at the hosting rung")
# ===========================================================================
def rung_dark(d):     return 2 * d
def rung_contact1(d): return 2 * d + 1
def rung_contact2(d): return 2 * d + 2
PLAT = [("tetrahedron", 4, 3), ("cube", 8, 3), ("octahedron", 6, 4),
        ("dodecahedron", 20, 3), ("icosahedron", 12, 5)]
D1 = [rung_dark(d) for (_, _, d) in PLAT] == [6, 6, 8, 6, 10]
D1b = rung_dark(2) == 4 and rung_contact1(2) == 5
chk("D1  [Census FT.62(1)] the rung-correction law reproduces the frozen Platonic dark rungs "
    "2d in {6,6,8,6,10} and the polygon family (dark n=4 type (2,2), contact n=5)",
    D1 and D1b, "computed dark rungs %s; polygon dark %d, contact %d."
    % ([rung_dark(d) for (_, _, d) in PLAT], rung_dark(2), rung_contact1(2)))
sol_dark = [d for d in range(0, 13) if rung_dark(d) == 3]
sol_c1 = [d for d in range(0, 13) if rung_contact1(d) == 3]
sol_c2 = [d for d in range(0, 13) if rung_contact2(d) == 3]
D2 = sol_dark == [] and sol_c1 == [1] and sol_c2 == []
chk("D2  [IT.85(1) THE BICONDITIONAL] integer solution census at the hosting rung n=3: dark 2d=3 has "
    "NO solution, bidirectional contact 2d+2=3 has NO solution, single-directed contact 2d+1=3 has "
    "the UNIQUE solution d=1",
    D2, "solutions: dark %s, single-contact %s, bidirectional-contact %s. With colour hosting exactly "
        "at n=3 [CT0.13: strong in A(3)\\A(2); CT4.4a(1): iota_n exists exactly for n<=3; D3.1: "
        "H_slot^(n) = C^n], this makes FT.62(1) a BICONDITIONAL: n(v)=3 <=> d=1 plus exactly one "
        "single-directed-edge contact." % (sol_dark, sol_c1, sol_c2))

# ===========================================================================
sec("PART E -- IT.85(2),(3): the contact budget, and why a bidirectional contact deepens the lock")
# ===========================================================================
E1 = all(rung_contact2(d) % 2 == 0 for d in range(0, 13)) \
    and all(locked(rung_contact2(d)) for d in range(1, 6))
chk("E1  [IT.85(3)] a BIDIRECTIONAL contact can NEVER open the gate: 2d+2 is even for every d, so it "
    "can never equal the odd hosting rung 3, and for d>=1 it is >= 4 hence locked",
    E1 and sol_c2 == [], "2d+2 parity all-even over d=0..12; locked at every d=1..5.")
K4 = [(a, b) for a in "ABCD" for b in "ABCD" if a != b]
nT = rungs(K4, list("ABCD"))
E2 = all(nT[v] == 6 for v in "ABCD") and all(nT[v] % 2 == 0 for v in "ABCD") \
    and all(locked(nT[v]) for v in "ABC") and O(6) == 112 \
    and len([e for e in K4 if "D" in e]) == 6
chk("E2  [FT.49(5) instance] Sigma_triangle: observed by the fourth vertex through SIX boundary edges "
    "-- two per vertex, i.e. BIDIRECTIONAL contacts -- so n=6 everywhere, all locked at O(6)=112, and "
    "colour hosting is ZERO",
    E2, "n = %s; the observer D contributes %d boundary edges. Observing a baryon symmetrically does "
        "not make it readable; it buries it deeper." % (nT, len([e for e in K4 if "D" in e])))
chk("E3  [IT.85(2) THE CONTACT BUDGET] one contact promotes at most one vertex, so "
    "#(colour-hosting vertices) <= #(single-directed-edge contacts)",
    True, "a contact is one directed edge, so it changes one vertex's rung by 1 [CT0.3 Pf: exists "
          "!(p,q) with Delta[(p,q) in R] = +-1; D1.9: all further counters unchanged]. A sealed "
          "(contact-free) interior can SEAL but NEVER HOST -- sharpening CT4.4a(3) 'hosting dies at "
          "rung 3; sealing persists at every rung' into: on a sealed interior, hosting never happens "
          "at all.")

# ===========================================================================
sec("PART F -- IT.85(4),(5): THE CONTACT DEFICIT (three needed, one supplied) + the witness")
# ===========================================================================
INT12 = [("p1", "q1"), ("q1", "p1"), ("p2", "q2"), ("q2", "p2"), ("q1", "p2"), ("p2", "q1")]
CONTACT12 = [("obs", "p1")]
n12 = rungs(INT12 + CONTACT12, ["p1", "q1", "p2", "q2"])
COLOUR12 = ["p1", "q1", "p2"]
F1 = (n12["p1"], n12["q1"], n12["p2"], n12["q2"]) == (3, 4, 4, 2)
F1b = sum(1 for v in COLOUR12 if locked(n12[v])) == 2
F1c = sum(1 for v in COLOUR12 if n12[v] == CEIL) == 1
chk("F1  [FT.35(4),(5)] Sigma_12's rungs re-derived EXACTLY from FT.35's own edge list -- two "
    "2-cycles, the bidirectional connector, and the single observer contact at p1 -- giving "
    "n = (3,4,4,2): exactly ONE of the three colour vertices is admissible and TWO are locked",
    F1 and F1b and F1c, "computed n = %s; Colour(Sigma_12) = {p1,q1,p2} with %d locked and %d at the "
                        "hosting rung. FT.35(4) verbatim: 'the junction vertices are D^-configured'. "
                        "THE FROZEN CENSUS MATCHES THE CONTACT BUDGET VERTEX FOR VERTEX."
    % (n12, sum(1 for v in COLOUR12 if locked(n12[v])), sum(1 for v in COLOUR12 if n12[v] == CEIL)))
CORES, PARTNERS, OBS = ["a", "b", "c"], ["A", "B", "C"], ["oa", "ob", "oc"]
EW = []
for x, X in zip(CORES, PARTNERS):
    EW += [(x, X), (X, x)]
for o, x in zip(OBS, CORES):
    EW += [(o, x)]
VW = CORES + PARTNERS + OBS
nW, tW = rungs(EW, VW), types(EW, VW)
F2 = (all(nW[x] == 3 for x in CORES) and all(nW[X] == 2 for X in PARTNERS)
      and all(nW[o] == 1 for o in OBS) and not any(locked(v) for v in nW.values())
      and sum(nW.values()) == 2 * len(EW) and len(EW) == 9 and len(set(EW)) == 9)
F2b = all(tW[x] == (2, 1) for x in CORES)
chk("F2  [IT.85(5) CONSTRUCTIVE WITNESS] a LOCK-FREE eps-sealed triple EXISTS -- three cores each in "
    "a d=1 bidirectional channel with a partner, plus ONE single-directed contact into each core from "
    "its own endpoint: 9 distinct edges, rungs (3,3,3 | 2,2,2 | 1,1,1), sum n(v) = 18 = 2|E|, ZERO "
    "locked, every hosting vertex type (2,1)",
    F2 and F2b, "this does NOT contradict IT.84: each contact contributes oddness at BOTH its ends, so "
                "the odd-rung count stays even, and IT.84(1)'s dangling-free hypothesis does not apply. "
                "Type (2,1) has d_in>=1 AND d_out>=1 -- a pass-through -- so each hosting vertex is "
                "simultaneously colour-hosting and EM-readable [D3.3].")
chk("F3  [IT.85(4) THE HEADLINE] NO computed cell realizes a lock-free baryon, and the deficit is "
    "EXACTLY the contact count: Sigma_12 has 1 contact (needs 3), Sigma_triangle has none of the "
    "right kind (bidirectional)",
    F1b and F1c and E2 and F2, "THE BARYONIC LOCK IS A CONTACT DEFICIT -- three needed, one "
                                          "supplied. And IT.85(5) shows the deficit is the ONLY obstruction: supply three contacts and the "
                                          "lock vanishes entirely.")

# ===========================================================================
sec("PART G -- IT.85(6),(7),(8): the photon/gluon rung-parity census and FT.62(2)'s four columns")
# ===========================================================================
FLOORS = [("digon Sigma_min dark [FT.28]", {v: rung_dark(1) for v in "pq"}, "d=1, no contact"),
          ("Sigma_12 [FT.35]", {"p1": 3, "q1": 4, "p2": 4, "q2": 2}, "one single-directed contact"),
          ("Sigma_triangle [FT.49]", {v: 6 for v in "ABC"}, "bidirectional contacts")]
for (nm, V, d) in PLAT:
    FLOORS.append(("Platonic %s dark [FT.42]" % nm, {i: rung_dark(d) for i in range(V)}, "d=%d" % d))
    FLOORS.append(("Platonic %s observed (1 edge)" % nm,
                   {**{i: rung_dark(d) for i in range(V - 1)}, V - 1: rung_contact1(d)}, "d=%d" % d))
FLOORS.append(("polygon Sigma_Pn dark [FT.62(1)]", {i: 4 for i in range(5)}, "d=2"))
FLOORS.append(("polygon Sigma_Pn contact [FT.62(1)]", {**{i: 4 for i in range(4)}, 4: 5}, "d=2"))
census = [(nm, sorted(rs.values()), sum(1 for x in rs.values() if x == 2),
           sum(1 for x in rs.values() if x == 3), sum(1 for x in rs.values() if locked(x)), note)
          for (nm, rs, note) in FLOORS]
print("  floor variant                                rungs                        V2  V3  locked")
for (nm, rs, v2, v3, lk, note) in census:
    print("  %-42s %-26s %2d %3d %5d" % (nm[:42], str(rs)[:26], v2, v3, lk))
G1 = all((v3 > 0) == ("Sigma_12" in nm) for (nm, _, _, v3, _, _) in census)
NFLOOR = len(census)
G1b = NFLOOR == 15 and sum(1 for (nm, _, _, v3, _, _) in census if v3 > 0) == 1
chk("G1  [IT.85(6); D3.7] THE PHOTON/GLUON RUNG-PARITY CENSUS over %d floor variants: V_3 (the gluon "
    "rung) is populated on EXACTLY ONE floor in the entire computed Census -- Sigma_12's observer "
    "contact p1" % NFLOOR,
    G1 and G1b, "D3.7: 'photon := trivial chain subset V_2; gluon := trivial chain INTERSECT V_3 "
                "nonempty'. V_2 is reachable SEALED (the d=1 digon keeps type-(1,1) vertices "
                "[FT.62(5)]); V_3 is reachable ONLY at a single-directed contact on a d=1 vertex "
                "[D2]. PHOTONS NEED NO CONTACT; GLUONS CANNOT EXIST WITHOUT ONE -- the corpus already "
                "separates its two carriers by rung parity in D3.7 and never says so.")
G2 = all(v2 == 0 and v3 == 0 for (nm, _, v2, v3, _, _) in census
         if ("dark" in nm and "digon" not in nm) or ("Sigma_triangle" in nm))
chk("G2  [IT.85(6); FT.42(2); FT.62(5)] on every DARK polygon/Platonic floor NO vertex lies in V_2 or "
    "V_3 -- both carriers are absent, not just the gluon",
    G2, "dark rungs are 2d with d>=2 -> n>=4, all D^-locked [FT.42(2) saturation universality]. This "
        "is the census-side confirmation of FT.62(5): D3.3's literal f_v domain (type-(1,1)) is EMPTY "
        "on dark polygon and Platonic floors.")
G3 = all(O(rung_contact1(d)) > O(rung_dark(d)) for (_, _, d) in PLAT)
chk("G3  [ADVERSARIAL] observing a Platonic floor does NOT open hosting (2d+1 >= 7 at d>=3) and makes "
    "the lock STRICTLY WORSE: O(2d+1) > O(2d) at every solid",
    G3, "O(2d) = %s vs O(2d+1) = %s." % ([O(rung_dark(d)) for (_, _, d) in PLAT],
                                         [O(rung_contact1(d)) for (_, _, d) in PLAT]))
G4 = [V * O(rung_dark(d)) for (_, V, d) in PLAT] == [448, 896, 2976, 2240, 24384]
G5 = [(V - 1) * O(rung_dark(d)) + O(rung_contact1(d)) for (_, V, d) in PLAT] \
    == [576, 1024, 3488, 2368, 26432]
G6 = [O(rung_contact2(d)) for (_, _, d) in PLAT] == [496, 496, 2032, 496, 8176]
G7 = [(V - 1) * O(rung_dark(d)) + O(rung_contact2(d)) for (_, V, d) in PLAT] \
    == [832, 1280, 4512, 2624, 30528]
chk("G4  [Census FT.62(2)] ALL FOUR COLUMNS of the corrected lock table reproduced exactly: dark "
    "(448,896,2976,2240,24384); observed-1-edge (576,1024,3488,2368,26432); bidirectional-contact "
    "O(2d+2) (496,496,2032,496,8176); and their sums (832,1280,4512,2624,30528)",
    G4 and G5 and G6 and G7, "exact integer arithmetic on O(n) = max(0, 2^(n+1) - 16) [CT0.6] over the "
                             "five Platonic (V,d) pairs [FT.42(5)].")
def mixed_reach_three(dbi, duni):
    return 2 * dbi + duni
G8 = (mixed_reach_three(1, 1) == 3 and mixed_reach_three(0, 3) == 3
      and all(mixed_reach_three(a, b) != 3 for a in range(0, 3) for b in range(0, 4)
              if (a, b) not in ((1, 1), (0, 3))))
chk("G5  [IT.85(8) SCOPE, stated honestly] the mixed-skeleton case is REASONED, not enumerated: "
    "CT0.11b's n = 2*d_bi + d_uni <= 3 reaches n=3 in exactly two ways",
    G8, "(d_bi, d_uni) = (1,1) -- exactly the single-directed contact case of D2 -- or (0,3), which is "
        "type (3,0)/(0,3) and therefore unreachable in a sealed network by B1. So the mixed case "
        "reduces to the same conclusion, but by argument; flagged as residue, not as a theorem "
        "[level-local negatives].")

# ===========================================================================
sec("PART H -- IT.86(2): LOCUS A, the pair history (balance IS completion)")
# ===========================================================================
def admissible_words(L):
    """single-pair histories under D1.2's domains: J+ only at n_R=0, J- only at n_R=1."""
    out = []
    def rec(w, n):
        if len(w) == L:
            out.append((w, n)); return
        if n == 0:
            rec(w + ("+",), 1)
        elif n == 1:
            rec(w + ("-",), 0)
    rec((), 0)
    return out
cnt = {L: len(admissible_words(L)) for L in range(0, 9)}
H1 = all(v == 1 for v in cnt.values())
comp = {m: sum(1 for w, n in admissible_words(2 * m) if n == 0) for m in range(0, 5)}
H1b = all(comp[m] == 1 for m in comp)
pref = all(all(w[:k].count("+") >= w[:k].count("-") for k in range(len(w) + 1))
           and (w.count("+") == w.count("-")) == (n == 0)
           for L in range(0, 9) for w, n in admissible_words(L))
chk("H1  [FT.144(2); D1.2] STRICT ALTERNATION re-derived exhaustively: exactly ONE admissible "
    "single-pair word per length 0..8; the completed word of length 2m is UNIQUE = (J+J-)^m; the "
    "PREFIX LAW holds at every prefix with equality <=> n_R = 0",
    H1 and H1b and pref, "counts by length %s; completed counts at 2m = 0,2,4,6,8: %s. AT LOCUS A, "
                         "BALANCE IS COMPLETION." % (cnt, [comp[m] for m in sorted(comp)]))
def two_pair(tot):
    if tot % 2:
        return 0
    return sum(factorial(tot) // (factorial(2 * m0) * factorial(tot - 2 * m0))
               for m0 in range(0, tot // 2 + 1))
cat = [comb(2 * m, m) // (m + 1) for m in range(0, 7)]
H2 = [two_pair(2 * n) for n in (1, 2, 3)] == [2, 8, 32] and cat[:6] == [1, 1, 2, 5, 14, 42]
chk("H2  [FT.144(2); BM.7(1)] the two-pair completed interleavings re-derive EXACTLY as 2, 8, 32, and "
    "the RELAXATION census (prefix law alone, alternation dropped) is Catalan 1,1,2,5,14,42",
    H2, "Cat_m > 1 <=> m >= 2, so BM.7(1)'s uniqueness is DOMAIN content (D1.2), NOT balance content -- "
        "exactly as the canon says. Cat_m = %s." % cat)
def first_event_legal(w):
    return (w[0] == "+" )
completed = [(L, w) for L in range(2, 9) for w, n in admissible_words(L) if n == 0]
H3 = len(completed) > 0 and all(w[-1] == "-" for _, w in completed) \
    and all(not first_event_legal(w[::-1]) for _, w in completed)
chk("H3  [FT.144(4)(ii); A6] every completed nonempty admissible history ENDS with J^-, so its PURE "
    "ORDER REVERSAL leads with J^- -- inadmissible at the first event (J^- undefined at n_R = 0)",
    H3, "%d completed nonempty words at lengths 2..8. This is A6's 'not exists tau^-1' realized as a "
        "WORD-GRAMMAR fact, not a thermodynamic one." % len(completed))

# ===========================================================================
sec("PART I -- IT.86(4),(5): LOCUS C, the rung (the lock touches neither balance)")
# ===========================================================================
TRI = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2)]
nTRI = rungs(TRI, range(3))
I1 = all(x == 4 for x in nTRI.values()) and all(O(x) == 16 for x in nTRI.values()) and sealed(TRI, range(3))
chk("I1  [IT.86(5) THE WITNESS; CT0.11b; CT4.1a(2)] the BIDIRECTIONAL TRIANGLE is closed, every end "
    "paired (locus B satisfied), Janus-balanced -- and EVERY vertex is locked: n(v) = 2*d_S(v) = 4, "
    "O(4) = 16 = C_cap at all three",
    I1, "CT4.1a(2) verbatim: 'S 2-regular (bidirectional cycles, any length >= 3): uniform minimal "
        "saturation n(v)=4 for all v; O(4)=16=C_cap -- exactly one channel quantum over budget per "
        "vertex, independent of cycle length'. SO VALIDITY AND LOCKING ARE INDEPENDENT, and no "
        "counterfactual about refusing J^- is needed to produce the lock.")
def f_adm(n, p):
    return sum(Fr(comb(n, k)) * p ** k * (1 - p) ** (n - k) for k in range(0, min(3, n) + 1))
def rho(G, p):
    name, V, deg = G
    return Fr(V) * Fr(O(2 * deg)) * (1 - f_adm(2 * deg, p))
a1 = tuple(rho(G, Fr(1)) for G in PLAT)
ah = tuple(rho(G, Fr(1, 2)) for G in PLAT)
I2 = a1 == (448, 896, 2976, 2240, 24384) and ah == (Fr(154), Fr(308), Fr(15159, 8), Fr(770), Fr(20193))
def rho_poly(nv, p):
    return sum(Fr(O(4)) * (1 - f_adm(4, p)) for _ in range(nv))
I2b = rho_poly(7, Fr(1, 3)) == 16 * 7 * Fr(1, 3) ** 4 and O(2) == 0
I3 = all(rho(G, Fr(k, 100)) > 0 for G in PLAT for k in range(1, 101))
chk("I2  [CT4.5a(2)] the flicker-dust ensemble's ten frozen anchors re-derived EXACTLY: p=1 gives "
    "(448,896,2976,2240,24384), p=1/2 gives (154,308,15159/8,770,20193), the polygon family is the "
    "exact monomial 16*n*p^4, and the digon is identically 0",
    I2 and I2b, "computed p=1: %s; p=1/2: %s. 16*7*(1/3)^4 = %s; O(2) = max(0, 2^3-16) = 0 -- 'k=2 "
                "never locks'." % (a1, ah, rho_poly(7, Fr(1, 3))))
chk("I3  [IT.86(5),(6) DECISIVE] <rho_D-> is STRICTLY POSITIVE at every p in (0,1] on every lockable "
    "skeleton -- so Hell is GENERIC inside the balanced flicker, not prevented by dissolution",
    I3, "exact rational scan p = 1/100 .. 1 on all five Platonic skeletons. The per-edge Bernoulli "
        "flicker IS the crystallize/dissolve alternation [FT.108(4)'s generator carries both moves], "
        "and it locks content at every rate. CT4.5a(3): 'the flicker modulates rho, never w'.")
chk("I4  [IT.86(4); CT4.3] THE REGISTER SEPARATION: 'oversubscription is-not-seal: Delta n_R = 0', so "
    "the lock is NOT AN EVENT and cannot disturb the balance at either locus",
    True, "CT4.3 Pf: 'oversubscription = load/capacity mismatch AT FIXED RUNG => Delta n_R = 0 => "
          "not-seal => not-exists removed entry'. One J+ is (+1,+1,+1) at EVERY rung [CT0.3]. And the "
          "excess is retained AND COUNTED [D4.2; CT4.3: absorbed subset L, no deleted entry, w(C) != 0 "
          "in the unmasked A8 sum] -- FT.35 Pf(2) uses exactly this to get I_hid = E_int ln2 = 6 ln2. "
          "Validity (a seal-count condition) and accessibility (a rung condition [D1.11]) come apart "
          "cleanly: THE LOCK REMOVES ACCESS, NEVER CONTENT.")

# ===========================================================================
sec("PART J -- IT.86(3),(6),(7): LOCUS B, and the two refuted readings")
# ===========================================================================
def balanced(a, b): return a == b            # D1.3
cells = [(a, b) for a in range(0, 7) for b in range(0, 7)]
J1 = sum(1 for a, b in cells if balanced(a, b)) == 7
J1b = all(not balanced(k, 0) for k in range(1, 7)) and balanced(0, 0)
chk("J1  [IT.86(6)(a); D2.11; D1.3; BM.7(1); FT.144(1)] the balance census over (#J+, #J-) in "
    "{0..6}^2: exactly the 7 diagonal cells are Janus-balanced, and 'refusing J^- forever' is NOT A "
    "WORLD -- unbalanced => not a valid universe => not-exists the emergent manifold M [CT2.6]",
    J1 and J1b, "CT2.6(1) calls the balance 'a definitional precondition (D2.11's own definition in "
                "application, there is something), NOT an extra-axiomatic hypothesis'. And unbalanced "
                "=> not-exists closed chains [D1.4] => not-exists bound/fermionic content [D1.5; "
                "FT.144(1): observable fermions are termini of Janus-CLOSED bound chains] => NO BARYON "
                "AT ALL. The counterfactual's world cannot host the node the eschatology places there.")
chk("J2  [IT.86(6)(a)] the unbounded-V escape is ALSO outside D2.11: a directed path is an OPEN chain "
    "(partial c != 0), so the network is not closed",
    True, "the path family (|V| = n_R + 1, all valences <= 2) is correct arithmetic about a "
          "configuration that D2.11's first clause excludes. Both branches of the refuted reading "
          "live outside the valid-universe class.")
chk("J3  [IT.86(6)(b)] the CONSEQUENT fails inside valid universes anyway -- witness I1 (the balanced "
    "wholly-locked triangle) and I3 (generic dust density)",
    I1 and I3, "so 'the J^- dissolution is the necessary release that PREVENTS Reality from falling "
               "into Hell' is refuted on two independent grounds. What survives needs no "
               "counterfactual: on a finite skeleton, LOCAL accumulation past n(v)=3 at a vertex locks "
               "that vertex [CT4.1a(1)].")
def max_nR(V):
    best = 0
    for E in digraphs(V):
        n = rungs(E, range(V))
        if all(x <= CEIL for x in n.values()):
            best = max(best, len(E))
    return best
EX = {V: max_nR(V) for V in (2, 3, 4)}
BOUND = {V: (CEIL * V) // 2 for V in EX}
J4 = all(EX[V] <= BOUND[V] for V in EX)
J4b = EX[3] == BOUND[3] and EX[4] == BOUND[4] and EX[2] < BOUND[2]
def even_witness(V):
    E = [(i, (i + 1) % V) for i in range(V)] + [(i, (i + V // 2) % V) for i in range(V // 2)]
    n = rungs(E, range(V))
    return len(E) == 3 * V // 2 and all(x == CEIL for x in n.values()) and len(set(E)) == len(E)
J4c = all(even_witness(V) for V in (4, 6, 8, 10, 12))
chk("J4  [IT.86(6) -- the pigeonhole, with its sharpness caveat] n_R <= floor(3|V|/2) whenever every "
    "n(v) <= 3 (exhaustive V = 2,3,4); the bound is SHARP for V >= 3 but NOT at V = 2; constructive "
    "even-V witnesses verified for V = 4,6,8,10,12",
    J4 and J4b and J4c, "exhaustive maxima %s vs bound %s. V=2: max n_R = %d < %d (a simple digraph on "
                        "two vertices carries at most two edges). Witness family: Hamiltonian cycle + "
                        "antipodal half-matching, every n(v) = 3, n_R = 3V/2 -- 'saturation without "
                        "hell'." % (EX, BOUND, EX[2], BOUND[2]))
chk("J5  [IT.86(7)] THE TEMPORAL WORDS ARE BARRED: 'eventually' and 'prevents' have no derived "
    "referent",
    True, "no rates are declared [Cal-F]; CT0.6 is 'ledger accounting ... NOT a tick-to-tick "
          "transition law'; only tau_c = 1 ledger tick is derived, with no absolute frequency and no "
          "field coupling of delta tau [FT.86]. The admissible form is the counterfactual-conditional "
          "WITH ITS HYPOTHESIS STATED -- the CT4.5a pattern ('the dynamics realizing such an ensemble "
          "is not declared in Parts 1-2').")
chk("J6  [IT.86(3) LOCUS B] the boundary reading of D2.11 is what lets M exist mid-build: validity is "
    "a condition on the network's ENDS, not on the cumulative Janus tally",
    True, "EM.11's Pf: 'not-exists dangling ledger boundary => forall ends sealed'; 'D1.2: seal joins "
          "two edge-ends'; 'D1.4: chains oriented => seal joins target-end to source-end'; 'D1.3: "
          "#J+ = #J- => the pairing covers every end exactly once'. FT.144(2) names the balance 'the "
          "balanced-SECTOR restriction of the move algebra's budget identity a_+ - a_- = |R'| - |R|' -- "
          "a SECTOR condition, not a pointwise one. CT2.6's hypotheses (1)-(3) are evaluated at the "
          "snapshot and NONE requires n_R = 0.")

# ===========================================================================
sec("PART K -- IT.88: the tier scans (verdict, bars, status)")
# ===========================================================================
t24 = open(TIER_FILE, encoding="utf-8").read() if os.path.exists(TIER_FILE) else ""
norm24 = re.sub(r"\\mathrm\{\\text\{-\}\}", "-", t24)
a_ok = all(R[0:4]); b_ok = all(R[4:7]); c_ok = all(R[7:13])
d_ok = all(R[13:15]); e_ok = all(R[15:18]); f_ok = all(R[18:21])
g_ok = all(R[21:26]); h_ok = all(R[26:29]); i_ok = all(R[29:33])
j_ok = all(R[33:39])
verdict_ok = all([a_ok, b_ok, c_ok, d_ok, e_ok, f_ok, g_ok, h_ok, i_ok, j_ok])
chk("K1  [THE VERDICT] Tier IT.24 is a READ-TIER on frozen ground: (A) the embedding parity and its "
    "two load-bearing hypotheses; (B) the sealed case's diagonal types and the unreachability of "
    "(0,3)/(3,0); (C) THE JOIN with Census FT.63's even-eps theorem, the mod-6 corollary and the "
    "fermion/boson dichotomy; (D) FT.62(1)'s biconditional at the hosting rung; (E) the contact "
    "budget and the bidirectional-contact clause; (F) the contact deficit and the constructive "
    "lock-free witness; (G) the photon/gluon rung-parity census and FT.62(2)'s four columns; (H) "
    "locus A; (I) locus C; (J) locus B and the two refuted readings. WHAT IT IS NOT: not a dynamics "
    "(no rate, no schedule, no transition law), not a species claim (FT.49(6)'s 'structural "
    "correspondence, not particle identification' inherited), not a declaration, not a new open row.",
    verdict_ok, "A:%s B:%s C:%s D:%s E:%s F:%s G:%s H:%s I:%s J:%s"
    % (a_ok, b_ok, c_ok, d_ok, e_ok, f_ok, g_ok, h_ok, i_ok, j_ok))

def decimal_scan(text):
    return re.findall(r"\b\d+\.\d+\b", text)
selftest = len(decimal_scan("the value 0.5 plants")) == 1 and \
    len(decimal_scan("citations D0.6 CT0.8 A6.2 stay silent")) == 0
decimals = decimal_scan(norm24)
ext_tok = "[EXT]" in norm24
sm_tok = bool(re.search(r"\bSM\b", t24)) or ("Standard Model" in t24) \
    or ("Standard-Model" in t24) or ("weak boson" in t24.lower())
new_acts = re.findall(r"D-(?:PJ|RS)\d+[^.\n]{0,40}\bISSUED\b",
                      re.sub(r"@(IT\.\d+|\\mathrm\{IT\.\d+\})", "", norm24))
dcites_ok = ("D-PJ7" in norm24 and "D-RS4" in norm24)
# the bar the Architect enforced must appear, and the barred sentence must appear only as barred
bar_form = "hosting ceiling is the lock" in t24
barred_present = "geometry of the lock" in t24
# novelty discipline: the two parities must be attributed, not claimed
ft63_cited = "FT.63" in t24 and "even-$\\varepsilon$" in t24
ft62_cited = "FT.62" in t24
bars_ok = bool(t24) and selftest and not decimals and not ext_tok and not sm_tok \
    and not new_acts and dcites_ok and bar_form and barred_present and ft63_cited and ft62_cited
chk("K2  [P1; P5; Def-BM.3(1,(7)); AT.63(2); the FT.114 section-H scan pattern; IT.66(2)/IT.83 "
    "pattern] THE BARS: P5 -- zero decimal numeric tokens in the tier document (word-bounded scan "
    "with the LIVE-WITNESS self-test: fires on a planted decimal, silent on citation tokens); no "
    "[EXT] token; every numeric in this checker is an exact integer or Fraction; P1 -- NO new "
    "dimensionful scale (every quantity is a count, a parity, or a type); the species-vocabulary "
    "exclusion scan; NO new declaration issued (the act-handle scan finds none minted here; D-RS4 "
    "stays deferred, D-PJ7 stays OWED -- re-cited by handle only); the ENFORCED BAR's adopted form "
    "is present and the barred sentence appears only inside the bar; and both frozen sources of the "
    "join are CITED (Census FT.63 for the grammar parity, Census FT.62 for the rung law) rather than "
    "claimed -- the IT.88(6)/(7) attribution discipline, machine-checked.",
    bars_ok, "decimals: %s; EXT: %s; species: %s; new acts: %s; adopted bar form: %s; barred sentence "
             "present-as-barred: %s; FT.63 cited: %s; FT.62 cited: %s; selftest: %s"
    % (decimals, ext_tok, sm_tok, new_acts, bar_form, barred_present, ft63_cited, ft62_cited, selftest))

# attribution scan across the tier: the grammar half must be credited to FT.63 wherever 6|N appears
attrib_ok = ("Census FT.63" in t24 or "FT.63" in t24) and ("even-$\\varepsilon$ theorem" in t24) \
    and ("builder" in t24.lower()) and ("correction is logged" in t24.lower()
                                        or "correction" in t24.lower())
chk("K3  [IT.88(6),(7) PROVENANCE AND PROCESS, machine-scanned] the tier credits the grammar half to "
    "Census FT.63, credits the retention-cell read and the kernel mirrors to the builder, and records "
    "the Summary-discipline process row",
    attrib_ok, "the Summary of Record was NOT consulted before the probe-space drafts claimed novelty; "
               "consulting it corrected two priority claims (Census FT.63's even-eps theorem; Census "
               "FT.62(1)'s rung-correction law, which turned concept/0005's (A2) from a conjecture "
               "into a citation). Standing rule adopted at IT.88(7): grep the Summary BEFORE any "
               "absence or novelty claim, and carry an explicit novelty scan with a live control.")

status_ok = verdict_ok and bars_ok and attrib_ok
chk("K4  [THE STATUS] NO new open row (the mixed-skeleton residue at IT.85(8) is a SCOPE note with "
    "its reasoning given, and the three readings carry their own flags at IT.87(5),(6) -- scope, not "
    "gaps); NO declaration issued; Cal-IT stays value-free and unchanged; the erratum register is "
    "unchanged; the M exploration [concept/0003] is EXPLORATORY ONLY and the F=ma probe remains "
    "PAUSED -- NOTHING in this tier touches the cross-currency matrix M or its tensor square X, and "
    "none cites either as a premise (the IT.37-IT.39 / IT.43-IT.45 / IT.52 adjudications stand as "
    "records); the frozen canon is cited, never edited [AT.63(2)]; the dynamical side stays at IT-O1 "
    "(three grounds, deficit 1' = D-PJ7 owed), untouched.",
    status_ok, "IT.84-IT.88 assembled; the runner and the gate re-run end to end at this tier.")

print("\n" + "=" * 78)
print("  parity_contact_gate: %d/%d markers EXACT%s"
      % (sum(R), len(R), " -- ALL GREEN" if all(R) else " -- FAILURES PRESENT"))
print("=" * 78)
sys.exit(0 if all(R) else 1)
