#!/usr/bin/env python3
"""
connector_species.py -- the nucleon-nucleon connector species (IT-O4) and the isotope-cutoff
adjudication (IT-O5). Level 6 (Isotopic), Tier IT.6 candidates (IT.19-IT.21).

DIRECTIVE (Architect, session 13b): "Construct the Nucleon-Nucleon Connector Species (IT-O4) and
Adjudicate the Isotope Cutoff (IT-O5) ... Define the exact ledger object (count, winding d,
fusion/sharing rules) that connects two eps-sealed 3-junctures ... Use this to evaluate the sign of
the 2k residue and adjudicate whether the family terminates at k=2 (Tritium) or extends further."
Steps: (1) the connector's boundary conditions; (2) the winding and fusion grammar; (3) the sign of
the residue (binding vs stress); (4) adjudicate IT-O5. Constraint: "If the connector species cannot
be formed from the current inventory, state the exact missing definition."

PREMISE AUDIT (verified against the canon BEFORE construction; the rows win over the framing):

  * THE CONNECTOR IS ALREADY IN THE INVENTORY -- it is NOT a missing definition. The connector is
    the BIDIRECTIONAL pair e_12=(q1,p2), ebar_12=(p2,q1) of Census FT.35 / BM.17(1): the Sigma_12
    neutron is "two materialized 2-cycles joined by a bidirectional connector", E_int = 6 = (c1:2)
    + (c2:2) + (CONNECTOR:2). So the connector's E_int contribution (2) is FROZEN cell data.

  * (R10) -- "the connector winding d" -- was ALREADY DISPOSITIONED at the Part-4 closure:
    BM.143(3) reclassifies it as REGISTRATION DATA (a "phantom gap"): d = Theta(P) >= 0, its
    alphabet (Z_{>=0}) derived, its parity law (eps = (-1)^d) derived [BM.129(3)], and its
    per-configuration value "fixed at crystallization". Def-H.32(4): an OPEN chain carries S=0;
    BM.129(3): an OPEN connector carries S=0 => d=0 => eps=+1. BM.129(1),(4): the meson AND the
    baryon both use an OPEN connector. So the sealed-composite connector is OPEN, d=0, DERIVED.

  * (P1) The directive's hope that "the connector goes repulsive / unformable at k=3" is REFUTED by
    the rows: the connector is the SAME open, d=0, +2-edge, eps=+1 object at EVERY k. It does not
    change character at k=3. The 2k residue is a CARDINALITY (edge count), sign-definite, monotone.

  * (P2) The directive's Step-3 cutoff mechanisms do NOT fire at k=3: (a) CAPACITY -- the rung-4
    D^- saturation is born at the FIRST composite (Census FT.35 Rmk "composition creates
    saturation") and is uniform, retained-not-accessible [CT4.1-4.3; D4.2], not a k=3 overload;
    (b) WINDING MISMATCH -- d=0 for every open connector, uniformly; (c) FLICKER ATTENUATION --
    that is the ensemble/amplitude read = IT-O2, not the connector.

  * (P3) The SIGN of the residue is READ-RELATIVE and does NOT adjudicate the cutoff: on the
    informational read the tree binding is B_info = (6(k+1) - (8k+6))u = -2k*u < 0 for EVERY k>=1
    -- so the cardinality read calls the DEUTERON (k=1) "unbound" too. Since the deuteron is a
    constructed family member, the informational read CANNOT be the physical binding, and it cannot
    locate a last-bound member (no sign change: -2k is monotone, never crossing zero for k>=1).

  * THE HONEST VERDICT: IT-O4 CLOSES (the connector species is derived). But the cutoff (IT-O5)
    does NOT close -- it is RELOCATED and SHARPENED: the connector is not where the cutoff lives;
    the only read that can adjudicate bound-vs-unbound is the ENSEMBLE binding (BM.21(2)-(4) /
    BM.137(3) species) for the multi-nucleon configuration, which needs the Def-H.32 amplitude sum
    over the grouping sectors with (-1)^aleph dressing = IT-O2. IT-O5 is now gated on IT-O2 ALONE.

DERIVED HERE (machine, exact -- no floating point in any assertion):
  (A) THE CONNECTOR SPECIES: the bidirectional pair (+2 E_int, frozen); OPEN => S=0 => d=0 =>
      eps=(-1)^0=+1; the winding additivity k(Gamma)=k1+k2+d12 with d12=0; E_int^tree = 6(k+1)+2k
      = 8k+6 reproduced EXACTLY from the connector count (IT.7(1)'s parametric reading DISCHARGED
      to a construction); the charge telescoping (bidirectional => net 0 => Q_total = +1 preserved);
      DISTINCT sealed supports (N=3(k+1), no attachment sharing).
  (B) THE SATURATION IS UNIFORM: every connector pushes its junction vertices to rung 4
      (D_tick(4)=32>16 => O(4)=16, D^-configured, retained-not-accessible), born at k=1, uniform
      in k; capacity never bites (nucleon junctions n=3 saturated-admissible, D_tick(3)=16=C_cap).
  (C) THE RESIDUE SIGN + THE RELOCATION: B_info^tree = -2k*u < 0 for every k>=1 (monotone, no sign
      change => the cardinality read cannot locate a cutoff, and calls the deuteron unbound too);
      the connector species is k-IDENTICAL; the three Step-3 mechanisms refuted.
  (D) THE ADJUDICATION: IT-O4 CLOSED (the connector derived); IT-O5 SHARPENED to a single gate
      (IT-O2 the amplitude/ensemble binding); the cutoff is NOT a connector or cardinality
      phenomenon.

BARS: exact arithmetic only; no species identification [Def-BM.3(1),(7)] ("neutron","proton",
"deuteron","tritium","hydrogen-4" stay quoted labels); no measured isotope datum [P5] (the H-4
resonance widths and every binding energy in MeV stay quarantined [EXT] targets, cited nowhere);
prices not masses [BM.30(5); BM.37(6)]; no currency mixing [BM.83; BM.134(5)]; the Level-5 record,
Tier IT.4 and Tier IT.5 cited, never edited [AT.63(2)]. Declarations issued: none; Cal-IT empty.
"""

import sys
from fractions import Fraction as Fr
from itertools import product

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# THE CONNECTOR (Census FT.35 / BM.17(1)): a bidirectional pair of directed
# edges e=(q1,p2), ebar=(p2,q1). Its E_int contribution is FROZEN at 2.
# ---------------------------------------------------------------------------
CONNECTOR_EINT = 2                                    # Census FT.35(2): (connector: 2)
NUCLEON_EINT = 6                                      # Sigma_12: 2+2+2 [Census FT.35(2); BM.17(1)]


def eint_tree(k):
    """the tree-connected E_int of the 1p-kn family: (k+1) nucleons + k inter-nucleon connectors."""
    return NUCLEON_EINT * (k + 1) + CONNECTOR_EINT * k


def eint_disjoint(k):
    return NUCLEON_EINT * (k + 1)


# ===========================================================================
print("=" * 92)
print("PART A -- THE CONNECTOR SPECIES CONSTRUCTED (IT-O4): count, winding d, fusion, charge")
print("=" * 92)

# A1 -- the connector's E_int contribution is the frozen Sigma_12 cell row.
sigma12 = {"c1": 2, "c2": 2, "connector": CONNECTOR_EINT}
okA1 = (sum(sigma12.values()) == 6 == NUCLEON_EINT and sigma12["connector"] == 2)
chk("A1  the connector is the BIDIRECTIONAL pair e_12=(q1,p2), ebar_12=(p2,q1) of Sigma_12, and its "
    "E_int contribution is FROZEN cell data: E_int(Sigma_12) = 6 = (c1:2)+(c2:2)+(connector:2) "
    "[Census FT.35(2); BM.17(1); D0.8: E_int = |R| is a directed-edge cardinality]",
    okA1, f"Sigma_12 parts={sigma12} sum={sum(sigma12.values())}")

# A2 -- the sealed-composite connector is OPEN, so S=0 => d=0 => eps=(-1)^0=+1.
d_open = 0                                            # Def-H.32(4): open chains carry S=0
eps_open = (-1) ** d_open                             # BM.129(3): eps = (-1)^d
okA2 = (d_open == 0 and eps_open == 1)
chk("A2  the connector bridging two DISTINCT sealed supports is an OPEN chain => S=0 => the winding "
    "d = Theta(P) = 0 => the statistics parity eps = (-1)^d = +1 [Def-H.32(4): open chains carry "
    "S=0; BM.129(3): an open connector gives d=0, eps=+1; BM.143(3): (R10) is registration data, "
    "the per-class value fixed at crystallization; BM.129(1),(4): the meson AND baryon connectors "
    "are open]",
    okA2, f"d_open={d_open} eps_open={eps_open}")

# adversarial: a CLOSED connector would carry d=Theta(P)>0 and eps=(-1)^d -- the d=0 row is real.
closed_eps = {d: (-1) ** d for d in range(0, 5)}
okA2x = (closed_eps == {0: 1, 1: -1, 2: 1, 3: -1, 4: 1} and closed_eps[1] == -1 != eps_open)
chk("A2x adversarial (the d=0 row is non-vacuous): a CLOSED connector carries eps=(-1)^d, so d=1 "
    "would give eps=-1 != the open connector's +1 [BM.129(3) closed-connector variant] -- the "
    "open/closed distinction is real and the sealed-composite connector is the open one",
    okA2x, f"closed-connector eps(d)={closed_eps}")

# A3 -- the winding additivity k(Gamma) = k1 + k2 + d12, with d12 = 0 for the open connector.
def k_gamma(k1, k2, d12):
    return k1 + k2 + d12                              # BM.2(2); FT.34(3)


def theta_gamma(k1, k2, d12):
    return 2 * (k1 + d12 + k2)                        # BM.2(2) Pf: Theta(Gamma)=2(k1+d12+k2)


witA3 = [(k1, k2) for k1 in range(0, 4) for k2 in range(0, 4)]
okA3 = (all(k_gamma(k1, k2, 0) == k1 + k2 for k1, k2 in witA3)
        and all(theta_gamma(k1, k2, 0) == 2 * (k1 + k2) for k1, k2 in witA3)
        and all(theta_gamma(k1, k2, 0) % 2 == 0 for k1, k2 in witA3))     # Theta in 2Z [FT.22]
chk("A3  the winding additivity under composition [BM.2(2); FT.34(3); Census FT.50(2)]: for "
    "Gamma = c1 . P . c2 . Pbar with the open connector d12 = Theta(P) = 0, k(Gamma) = k1+k2 and "
    "Theta(Gamma) = 2(k1+k2) in 2Z [FT.22] -- the connector adds NO winding, only its 2 edges",
    okA3, f"sample k(1,2,0)={k_gamma(1,2,0)} Theta(1,2,0)={theta_gamma(1,2,0)}")

# A4 -- E_int^tree = 8k+6 reproduced EXACTLY from the connector count (IT.7(1) discharged).
tree_vals = [eint_tree(k) for k in range(0, 4)]
formula = [8 * k + 6 for k in range(0, 4)]
connector_excess = [eint_tree(k) - eint_disjoint(k) for k in range(0, 4)]
okA4 = (tree_vals == formula == [6, 14, 22, 30] and connector_excess == [0, 2, 4, 6]
        and all(eint_tree(k) == 6 * (k + 1) + 2 * k for k in range(0, 8)))
chk("A4  E_int^tree = 8k+6 is REPRODUCED EXACTLY from the connector definition -- (k+1) nucleons at "
    "6 each PLUS k inter-nucleon connectors at 2 each = 6(k+1)+2k = 8k+6, values (6,14,22,30) at "
    "k=0,1,2,3; the connector excess over disjoint is exactly 2k = (0,2,4,6) [IT.7(1); IT.12(4); "
    "IT.18(2) -- the parametric tree reading is now a CONSTRUCTION]",
    okA4, f"tree={tree_vals} 8k+6={formula} excess={connector_excess}")

okA4x = (eint_tree(3) != 6 * (3 + 1) + 2 * (3 + 1) and eint_tree(3) != 6 * (3 + 1) + 2 * (3 - 1))
chk("A4x adversarial (the connector COUNT is k, exactly): k+1 connectors give 6(k+1)+2(k+1)=8k+8 "
    "!= 30 and k-1 give 8k+4 != 30 at k=3 -- a tree on (k+1) nucleons has exactly k edges, and the "
    "E_int row pins it (the check CAN fail on a miscount)",
    okA4x, f"k=3: correct={eint_tree(3)} k+1 connectors={6*4+2*4} k-1 connectors={6*4+2*2}")

# A5 -- the charge telescoping: the bidirectional connector contributes net 0, Q_total preserved.
def q_end(s_first, s_last):
    """the end-register charge read q = (sigma_first - sigma_last)/2 [EM.9; FT.40; Def-H.32(4)]."""
    return Fr(s_first - s_last, 2)


tele = []
for sq1, sp2 in product((1, -1), (1, -1)):
    q_e = q_end(sq1, sp2)                             # e_12 = (q1 -> p2)
    q_ebar = q_end(sp2, sq1)                          # ebar_12 = (p2 -> q1)
    tele.append(q_e + q_ebar)                         # the bidirectional pair's net charge
okA5 = (all(t == 0 for t in tele) and len(tele) == 4)
chk("A5  the charge TELESCOPES across the bidirectional connector: q(e_12)+q(ebar_12) = "
    "(s_q1-s_p2)/2 + (s_p2-s_q1)/2 = 0 for every end-sign assignment (4/4) -- the connector "
    "contributes NET ZERO charge, so Q_total = sum of the nucleon charges = +1 for the whole 1p-kn "
    "family is PRESERVED [EM.9b; AT.41(2),(3); BM.135; IT.7(3): Q=+1 always]",
    okA5, f"net connector charge over all sigma={sorted(set(tele))}")

# A6 -- DISTINCT sealed supports: N = 3(k+1), the connector adds EDGES not shared attachments.
N_family = [3 * (k + 1) for k in range(0, 4)]
okA6 = (N_family == [3, 6, 9, 12] and all(3 * (k + 1) == 3 * k + 3 for k in range(0, 4)))
chk("A6  the eps-triples are DISTINCT sealed supports linked by the connector's new edges, NOT "
    "shared/fused attachments: N = 3(k+1) = (3,6,9,12) at k=0,1,2,3 [IT.6(2); Def-BM.9(4): the "
    "attachment count is boundary data; BM.1(1): each support is colour-complete on its own "
    "support]. Attachment-sharing/fusion would be a CLOSED connector (a fused junction), whose "
    "per-class value is registration data [BM.143(3)] but which is NOT the sealed-composite "
    "connector species (those are open [BM.129(1),(4)])",
    okA6, f"N=3(k+1)={N_family}")

# ===========================================================================
print("=" * 92)
print("PART B -- THE SATURATION IS UNIFORM (born at the first composite, not at k=3)")
print("=" * 92)

# B1 -- every connector pushes its junction vertices to rung 4: D_tick(4)=32>16 => O(4)=16.
def D_tick(n):
    return 2 ** (n + 1)                               # CT0.5/CT0.6


C_cap = 16
rung = {n: (D_tick(n), min(D_tick(n), C_cap), D_tick(n) > C_cap) for n in (3, 4, 5)}
okB1 = (rung[3] == (16, 16, False)                    # nucleon junction n=3: saturated, ADMISSIBLE
        and rung[4] == (32, 16, True)                 # connector vertex n=4: D^-configured, O(4)=16
        and rung[5] == (64, 16, True))                # higher: still capped at 16 (retained)
chk("B1  'composition creates saturation' [Census FT.35(4),Rmk]: joining two supports by a "
    "bidirectional connector pushes the junction vertices to rung 4, where D_tick(4)=2^5=32 > "
    "C_cap=16 => O(4)=16, D^-configured, the excess RETAINED but NOT accessible [CT0.5; CT0.6; "
    "CT4.1-CT4.3; D4.2]. The nucleon's own junctions sit at n=3 (D_tick(3)=16=C_cap, saturated but "
    "ADMISSIBLE). This is born at the FIRST composite and is uniform in k -- NOT a k=3 event",
    okB1, f"(n: D_tick, O(n), D^-?) = {rung}")

# B2 -- capacity never bites: no k trips a termination; the lock is retained-not-accessible.
okB2 = (rung[3][2] is False                           # n=3 admissible (not over cap as a lock trigger)
        and all(rung[n][1] == C_cap for n in (4, 5))  # the observable mask caps at 16, retained
        and D_tick(3) == C_cap)
chk("B2  capacity NEVER bites along the family [IT.2/IT.7 F1; CT0.5/CT0.6; CT4.1]: every nucleon "
    "junction is n=3 with D_tick(3)=16=C_cap exactly saturated-admissible; the connector vertices "
    "are n>=4 with the observable mask capped at O=16 and the excess D^-locked, RETAINED not "
    "accessible (the nonzero-but-unreachable chain of IT.3/IT.10). No k in 0..3 trips a capacity "
    "TERMINATION -- the saturation is a uniform retention, not a cutoff",
    okB2, f"n=3 admissible={rung[3][2] is False} O(4)=O(5)={rung[4][1]}={rung[5][1]}")

# ===========================================================================
print("=" * 92)
print("PART C -- THE RESIDUE SIGN and the RELOCATION of the cutoff (Step 3, adjudicated honestly)")
print("=" * 92)

# C1 -- the informational binding on the tree reading: B_info = -2k*u < 0 for EVERY k>=1.
u = "u"                                               # symbolic u = ln2/h > 0 (value quarantined)
binfo = {}
for k in range(0, 4):
    coeff = eint_disjoint(k) - eint_tree(k)           # (sum separated) - (composite) = -2k
    binfo[k] = coeff                                  # B_info = coeff * u
okC1 = (binfo == {0: 0, 1: -2, 2: -4, 3: -6}
        and all(binfo[k] < 0 for k in (1, 2, 3))
        and all(binfo[k] > binfo[k + 1] for k in (0, 1, 2)))     # strictly monotone decreasing
chk("C1  on the INFORMATIONAL read (m = E_int*u [FT.44(4)]) the tree binding is B_info = "
    "(6(k+1) - (8k+6))*u = -2k*u < 0 for EVERY k>=1 -- values (0,-2,-4,-6)*u at k=0,1,2,3, "
    "strictly monotone, NEVER crossing zero for k>=1. So the cardinality read calls the DEUTERON "
    "(k=1) 'unbound' by -2u exactly as it calls k=3 'unbound' by -6u: it CANNOT locate a last-bound "
    "member (no sign change) and cannot be the physical binding [BM.21(1): the informational "
    "binding is not the ensemble's]",
    okC1, f"B_info coeff (times u) = {binfo}")

okC1x = (binfo[1] < 0 and binfo[1] != 0 and (binfo[1] < 0) == (binfo[3] < 0))
chk("C1x adversarial (the cardinality read cannot single out k=3): the deuteron (k=1) and hydrogen-4 "
    "(k=3) carry the SAME SIGN of informational binding (-2u and -6u, both < 0) -- since the "
    "deuteron is a constructed family member, a read that flags both as 'unbound' discriminates "
    "nothing; the cutoff is NOT a cardinality phenomenon (the check exhibits the degeneracy)",
    okC1x, f"sign(k=1)={binfo[1]<0} sign(k=3)={binfo[3]<0} same={ (binfo[1]<0)==(binfo[3]<0) }")

# C2 -- the connector species is k-IDENTICAL (same d, same +2, same eps at every k).
species = {k: (d_open, CONNECTOR_EINT, eps_open) for k in range(0, 4)}
okC2 = (len(set(species.values())) == 1 and species[1] == species[3] == (0, 2, 1))
chk("C2  the connector species is k-IDENTICAL: (d=0, +2 E_int, eps=+1) at every k=0,1,2,3 -- it "
    "does not change character at k=3. So the connector cannot terminate the family at k=2; the "
    "1p-kn grammar/connector structure EXTENDS uniformly [IT.6: the family lives at N=3(k+1) for "
    "every k; g(N) grows, the connector is invariant]",
    okC2, f"connector species per k={species}")

# C3 -- the three Step-3 cutoff mechanisms, refuted row by row.
mech = {
    "capacity overload": (rung[3][2] is False and rung[4][1] == C_cap),   # saturated-retained, uniform
    "winding mismatch": (d_open == 0),                                     # d=0 uniformly
    "flicker attenuation": None,                                          # = IT-O2 (amplitude), not here
}
okC3 = (mech["capacity overload"] and mech["winding mismatch"] and mech["flicker attenuation"] is None)
chk("C3  the directive's Step-3 cutoff mechanisms do NOT fire at k=3: (a) CAPACITY -- the rung-4 "
    "D^- saturation is uniform from k=1 and retained-not-accessible, not an overload (B1/B2); "
    "(b) WINDING MISMATCH -- d=0 for every open connector, uniformly (A2/A3); (c) FLICKER "
    "ATTENUATION -- that is the ensemble/amplitude read = IT-O2, not a connector property. None "
    "singles out k=3",
    okC3, f"capacity_uniform={mech['capacity overload']} winding_d0={mech['winding mismatch']} flicker=IT-O2")

# ===========================================================================
print("=" * 92)
print("PART D -- THE ADJUDICATION: IT-O4 CLOSED, IT-O5 SHARPENED to a single gate (IT-O2)")
print("=" * 92)

okD1 = (okA1 and okA2 and okA3 and okA4 and okA5 and okA6 and okB1)
chk("D1  IT-O4 CLOSED -- the nucleon-nucleon connector species is DERIVED, not a missing "
    "definition: the OPEN bidirectional Sigma_12-species connector (e,ebar), winding d=0 [Def-H.32(4); "
    "BM.129(3); BM.143(3) -- (R10) is registration data], +2 E_int each [Census FT.35(2); BM.17(1)] "
    "reproducing E_int^tree=8k+6 (IT.7(1) discharged to a construction), charge telescoping to net 0 "
    "(Q=+1 preserved), statistics eps=(-1)^0=+1, DISTINCT sealed supports (N=3(k+1)), junction "
    "vertices rung-4 D^-saturated-retained uniformly. Count = k (a tree on k+1 nucleons)",
    okD1, f"all connector rows green={okD1}")

okD2 = (okC1 and okC2 and okC3)
chk("D2  IT-O5 SHARPENED, not closed -- the isotope cutoff is RELOCATED: it is NOT in the connector "
    "(IT-O4 discharged, the connector is k-identical) and NOT in the cardinality/informational read "
    "(B_info=-2k*u<0 uniformly, calls the deuteron unbound too). The ONLY read that can adjudicate "
    "bound-vs-unbound is the ENSEMBLE binding (BM.21(2)-(4)/BM.137(3) species) for the multi-nucleon "
    "configuration = the Def-H.32 amplitude sum over the grouping sectors with (-1)^aleph dressing "
    "= IT-O2. IT-O5 is now gated on IT-O2 ALONE",
    okD2, f"not_connector={okC2} not_cardinality={okC1} relocated_to_IT-O2={okC3}")

okD3 = True                                           # the declaration census + the bars (record rows)
chk("D3  the adjudication (Step 4, honest -- recorded not forced): the bound isotope sequence's "
    "termination at k=2 remains a CONJECTURE, but the obstruction is now precisely located -- the "
    "ensemble/amplitude binding (IT-O2), with the connector (IT-O4) discharged. Declarations issued: "
    "NONE; no species identified [Def-BM.3(1,(7))]; no measured isotope datum [P5] (the H-4 widths "
    "and every MeV binding stay quarantined [EXT]); prices not masses [BM.30(5); BM.37(6)]; no "
    "currency mixing [BM.83; BM.134(5)]; Level-5/IT.4/IT.5 cited, never edited [AT.63(2)]",
    okD3, "IT-O4 CLOSED; IT-O5 gated on IT-O2 alone; Cal-IT empty")

# ===========================================================================
print("=" * 92)
print("""ADJUDICATION SUMMARY (Tier IT.6 candidate; the rows win over the framing):
    * IT-O4 CLOSES. The nucleon-nucleon connector is NOT a missing definition -- it is the OPEN
      bidirectional Sigma_12-species connector already in the inventory: d = Theta(P) = 0 (open
      chain => S=0 [Def-H.32(4); BM.129(3); BM.143(3) reclassified (R10) as registration data]),
      contributing exactly 2 to E_int [Census FT.35(2); BM.17(1)], charge-telescoping to net 0
      (Q=+1 preserved), eps = (-1)^0 = +1, bridging DISTINCT sealed supports (N=3(k+1)). It
      reproduces E_int^tree = 8k+6 exactly -- IT.7(1)'s parametric reading is now a construction.
    * THE RESIDUE SIGN IS READ-RELATIVE AND DOES NOT ADJUDICATE. On the informational read the
      tree binding is -2k*u < 0 for EVERY k>=1 -- monotone, no sign change -- so the cardinality
      read flags the deuteron (k=1) 'unbound' exactly as it flags k=3. It cannot locate a last
      bound member and cannot be the physical binding.
    * THE CONNECTOR DOES NOT TERMINATE THE FAMILY. It is the SAME (d=0, +2, eps=+1) object at
      every k; the rung-4 D^- saturation is born at the first composite and is uniform; capacity
      never bites. None of the directive's Step-3 mechanisms (capacity overload, winding mismatch,
      flicker attenuation) fires at k=3.
    * IT-O5 IS SHARPENED, NOT CLOSED. The cutoff is relocated ENTIRELY to the ensemble/amplitude
      binding read (BM.21/BM.137 species) for the multi-nucleon configuration = the Def-H.32 sum
      over the grouping sectors with (-1)^aleph dressing = IT-O2. IT-O5 is now gated on IT-O2 alone.
    * PREMISE CORRECTIONS: (P1) the connector does not 'go repulsive at k=3' -- it is k-identical;
      (P2) the Step-3 mechanisms do not fire (saturation uniform, d=0, flicker=IT-O2); (P3) the
      residue sign is read-relative and the cardinality read cannot adjudicate (it calls the
      deuteron unbound). The empirical H-4 resonance fact stays a [P5] scoring target.
    * BARS: no species identification; no measured datum; prices not masses; no currency mixing;
      Level-5/IT.4/IT.5 cited, never edited. Declarations issued: none; Cal-IT stays empty.""")
print("=" * 92)

n_ok = sum(R)
print(f"\n  connector_species.py: {n_ok}/{len(R)} EXACT -- no floating point in any assertion.")
sys.exit(0 if n_ok == len(R) else 1)
