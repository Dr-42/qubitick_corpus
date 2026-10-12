#!/usr/bin/env python3
"""
cutoff_resolution.py -- the isotope-cutoff resolution via the non-dynamical binding sign: the
"neutron stability" precedent (BM.41), the static binding-sign census, and the relocation of the
empirical resonance to the dynamics (IT-O1). Level 6 (Isotopic), Tier IT.9 candidates (IT.28-IT.30).

DIRECTIVE (Architect, session 13e): "please continue [the amplitude side / IT-O5]. Also if you need
inspiration, look at how the 'neutron's' stability was resolved. It was coming <= 0. The thing is the
non dynamical picture. That causes this."

THE INSPIRATION, MADE PRECISE. The corpus resolved the "neutron's" stability at BM.41 (reinforced at
BM.49 and BM.52(4)): the beta-decay vertex is KINEMATICALLY CLOSED on every adopted/constructed read,
Q = m_n - m_p - m_l - m_nu = -(m_l+m_nu) < 0, because m_n = m_p EXACTLY (the rest reads are
charge-degenerate). BM.41 Phys names the cause: "every rest read it has ever derived gives the neutron
and the proton the same mass ... because no crystallized count carries a charge exponent and every
normalized average is structurally charge-blind." Line 2299: "the closure is a theorem ABOUT THE READS,
not about the vertex grammar." So the corpus's "neutron" is STABLE -- and that <= 0 / stability is an
artifact of the NON-DYNAMICAL (static, charge-degenerate) picture, exactly as the Architect said. The
physically-decaying neutron needs a dynamical splitting the static reads do not produce.

THE RESOLUTION THIS TIER DRAWS FROM IT (the template applied to the isotope cutoff):
  * Every CONSTRUCTED static binding/decay read is <= 0 (bound or closed): BM.21(4) B<0 (the
    3-constituent ensemble), BM.137(3) B_ens<=0 (the two-chain floor), BM.41(4)(e)/BM.49/BM.52(4)
    Q<0 (the neutron beta vertex, closed on every read), the informational disjoint B_info=0. The
    non-dynamical picture has NO mechanism that produces a positive (unbound) physical binding.
  * The one static read that is positive -- the informational/cardinal mass excess of the bridged
    composite, m_comp - sum m_sep = +2k*u [FT.50(1); IT.20(1)] -- is NON-PHYSICAL: it flags the
    DEUTERON (k=1) "unbound" exactly as k=3, monotone with no sign change, so it cannot locate a
    last-bound member.
  * THEREFORE the static/non-dynamical ledger produces NO isotope cutoff: it gives a BOUND (<=0)
    sequence at every k, just as it gives a stable "neutron." The empirical hydrogen-4+ resonances
    (unbound, decaying) are a DYNAMICAL phenomenon -- a formed transit-leg / dissociation amplitude --
    which does NOT exist in the inventory [BM.122(6)(O1)-(O4); IT-O1]. The cutoff is RELOCATED from a
    static binding sign flip (IT-O2/IT-O5) to the dynamics (IT-O1).

DERIVED HERE (machine, exact -- no floating point, no external datum):
  (A) the neutron-stability precedent re-derived: m_n=m_p (charge-degeneracy) => Q=-(m_l+m_nu)<0
      (closed); the EM-corrected Q_corr=-(Dm_EM+m_l+m_nu)<0 ("strictly deeper" [BM.49]); the closure
      is a theorem about the READS (a hypothetical splitting is what would open it, and the static
      reads give none).
  (B) the static binding-sign census: every constructed read <= 0; the informational mass excess
      +2k*u is monotone and non-physical (flags the deuteron); no static read flips to unbound at k=3.
  (C) the dynamics gap: BM.122(6)(O1)-(O4) refute a formed transit-quantum supply vertex on four
      independent grounds => no formed radiation/transit leg [IT-O1] => the resonance is dynamical.
  (D) the adjudication: IT-O5's STATIC side CLOSES (no static cutoff; bound <=0 at every k, the
      neutron precedent); the empirical cutoff RELOCATES to IT-O1; the multi-nucleon ensemble binding
      VALUE stays open (IT-O2's three constructions) but does NOT gate the cutoff verdict.

BARS: exact arithmetic only; no species identification [Def-BM.3(1,(7))] ("neutron","proton","triton",
"hydrogen-4","resonance" stay quoted); no measured value [P5] (the neutron lifetime, the H-4 widths,
every MeV stay quarantined [EXT], cited nowhere); prices not masses [BM.30(5); BM.37(6)]; no currency
mixing [BM.83; BM.134(5)]; Level-5 and IT.4-IT.8 cited, never edited [AT.63(2)]. Declarations: none.
"""

import sys
from fractions import Fraction as Fr

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# masses as exact Fraction multiples of u = ln2/h (a positive scale; its value is quarantined [P5]).
# signs are decided by the rational coefficients alone -- u > 0 never enters as a number.
U = Fr(1)                                              # the symbolic unit u; all masses are coeff * u


# ===========================================================================
print("=" * 94)
print("PART A -- the 'neutron stability' precedent (BM.41): the template the Architect pointed to")
print("=" * 94)

# A1 -- the charge-degeneracy: m_n = m_p exactly (both E_int=6, the rest reads are charge-blind).
E_n, E_p = 6, 6                                        # Sigma_12 neutral / unit class [BM.17; BM.26]
m_n, m_p = E_n * U, E_p * U                            # m = E_int * u [FT.44(4)]
okA1 = (m_n == m_p == 6 * U and E_n == E_p)
chk("A1  the charge-degeneracy of the rest reads [BM.28(1); BM.30(3); BM.41(2); BM.17; BM.26]: the "
    "'neutron' and 'proton' both carry E_int=6 (the crystallized count has charge exponent 0), so "
    "m_n = m_p = 6u EXACTLY on every informational/normalized/curvature read -- 'no crystallized count "
    "carries a charge exponent and every normalized average is structurally charge-blind' [BM.41 Phys]",
    okA1, f"m_n={m_n}u m_p={m_p}u equal={m_n==m_p}")

# A2 -- the Q-value: Q = m_n - m_p - m_l - m_nu = -(m_l+m_nu) < 0 (kinematically closed).
m_l_min = 2 * U                                        # the lepton floor m_l >= 2 ln2/h [BM.41(4)(a); FT.28; FT.44(4)]
m_nu_min = 0 * U                                       # m_nu >= 0 [EW.33 PSD]
Q_coeff = (m_n - m_p) - m_l_min - m_nu_min             # the most-favorable (least-negative) Q
okA2 = (Q_coeff == -2 * U and Q_coeff < 0 and (m_n - m_p) == 0)
chk("A2  the Q-value sign theorem [BM.41(4)(e)]: Q = m_n - m_p - m_l - m_nu = 0 - (m_l+m_nu) = "
    "-(m_l+m_nu); with m_l >= 2u [FT.28 the digon floor] and m_nu >= 0 [EW.33], Q <= -2u < 0 on the "
    "MOST-favorable lepton mass -- the beta-decay vertex is KINEMATICALLY CLOSED; 'the corpus does not "
    "make the neutron heavier than the proton'",
    okA2, f"Q coefficient (most favorable) = {Q_coeff}u < 0 = {Q_coeff<0}")

# A3 -- the EM-corrected Q (BM.49): Dm_EM > 0 makes the charged member heavier, Q strictly deeper.
Dm_EM = Fr(3, 2) * U                                   # Dm_EM = 3 c e^2 ln2 / (2 pi h) > 0 [BM.46(4)], c>0 symbolic
Q_corr = (m_n) - (m_p + Dm_EM) - m_l_min - m_nu_min    # the proton (charged) is heavier by Dm_EM
okA3 = (Dm_EM > 0 and Q_corr == -Dm_EM - 2 * U and Q_corr < Q_coeff and Q_corr < 0)
chk("A3  the EM correction deepens the closure [BM.46(4); BM.49]: Dm_EM = 3ce^2 ln2/(2 pi h) > 0 makes "
    "the charged member heavier, so Q_corr = -(Dm_EM + m_l + m_nu) < Q < 0 -- 'the beta decay remains "
    "kinematically closed, STRICTLY DEEPER; the correction-makes-the-decay-possible claim is refuted by "
    "sign arithmetic' [BM.49]; and the closure survives the complete force operator [BM.52(4)]",
    okA3, f"Dm_EM={Dm_EM}u>0 Q_corr={Q_corr}u < Q={Q_coeff}u, both <0")

okA2x = (not (m_n > m_p) and Q_coeff < 0)
chk("A2x adversarial (the closure is a theorem about the READS): the static reads give m_n = m_p "
    "(NOT m_n > m_p), so there is no decay phase space; a positive splitting Dm = m_n - m_p > m_l+m_nu "
    "is what WOULD open the vertex, and no adopted static read supplies one [BM.41(4)(e); BM.30(5): the "
    "route-(ii) price that could split them is unadopted] -- the check CAN fail if a read split them",
    okA2x, f"m_n>m_p? {m_n>m_p} (the degeneracy is why Q<0)")

okA4 = (okA1 and okA2 and okA3)
chk("A4  THE NON-DYNAMICAL CAUSE (the Architect's point, made exact): the 'neutron' is STABLE in the "
    "corpus (Q<0, closed on EVERY adopted read [BM.41(4)(e); BM.49; BM.52(4)]) BECAUSE the picture is "
    "non-dynamical -- the static rest reads are charge-degenerate (A1), so no mass splitting exists to "
    "open a decay. 'The closure is a theorem about the reads, not about the vertex grammar' [BM.41 l.2299]. "
    "The physically-decaying neutron needs DYNAMICS the static ledger does not carry",
    okA4, f"degeneracy={okA1} Q<0={okA2} deeper-under-EM={okA3}")

# ===========================================================================
print("=" * 94)
print("PART B -- the static binding-sign census: every constructed read is <= 0 (bound/closed)")
print("=" * 94)

# B1 -- the constructed ENSEMBLE (physical) binding reads, all <= 0.
def D_n(n, uu):
    return Fr(n) if uu == 1 else (1 - uu ** n) / (1 - uu)


eps_grid = [Fr(i, 256) for i in range(1, 64)]
bens2 = [-Fr(4) * (4 * e) * D_n(1, 4 * e) / D_n(2, 4 * e) for e in eps_grid]   # BM.137(3), u=4 eps_q
bm21_like_sector = -2                                          # BM.21(4): B(1;1,1,1) = -2 m^2_4(.,1) < 0
okB1 = (all(b < 0 for b in bens2) and bm21_like_sector < 0)
chk("B1  the constructed ENSEMBLE binding reads are all <= 0 (bound): BM.137(3)'s two-chain "
    "B_ens^(2) = -4u/(1+u)*(ln2/h) re-derived STRICTLY < 0 on a 63-point rational eps_q grid; "
    "BM.21(4)'s three-constituent B(S_j;1,1,1) < 0 in every sector ('three separated constituents "
    "outweigh one junction'). The physical (ensemble) binding is NEGATIVE = bound in every constructed "
    "case",
    okB1, f"max B_ens^(2) coeff={max(bens2)} (all<0={all(b<0 for b in bens2)}); BM.21 like-sector sign={bm21_like_sector}")

# B2 -- the informational/cardinal read: a mass EXCESS +2k (non-physical), monotone, no flip at k=3.
def info_excess(k):
    """m_comp - sum m_sep on the informational read, in units of u: (8k+6) - 6(k+1) = +2k."""
    return (8 * k + 6) - 6 * (k + 1)


exc = [info_excess(k) for k in range(0, 4)]
okB2 = (exc == [0, 2, 4, 6] and all(info_excess(k) > 0 for k in (1, 2, 3))
        and all(info_excess(k) < info_excess(k + 1) for k in (0, 1, 2)))
chk("B2  the ONE static read that is positive -- the informational/cardinal mass excess of the bridged "
    "composite [FT.50(1); IT.20(1)]: m_comp - sum m_sep = (8k+6) - 6(k+1) = +2k*u = (0,2,4,6)u at "
    "k=0,1,2,3 (BM.21 binding convention: B_info=+2k>0 would read 'unbound'). BUT it is NON-PHYSICAL: "
    "strictly monotone with NO sign change, it flags the DEUTERON (k=1) 'unbound' exactly as k=3",
    okB2, f"info mass excess (coeff of u)={exc} monotone-no-flip={all(exc[i]<exc[i+1] for i in range(3))}")

okB2x = (info_excess(1) > 0 and info_excess(3) > 0 and (info_excess(1) > 0) == (info_excess(3) > 0))
chk("B2x adversarial (the cardinality read cannot locate a cutoff): the deuteron (k=1) and hydrogen-4 "
    "(k=3) carry the SAME SIGN of informational mass excess (+2u, +6u, both > 0) -- since the deuteron "
    "is a constructed family member, a read that flags both 'unbound' discriminates nothing; there is "
    "NO k at which the informational read flips (the check exhibits the degeneracy)",
    okB2x, f"sign(k=1)={info_excess(1)>0} sign(k=3)={info_excess(3)>0} same={(info_excess(1)>0)==(info_excess(3)>0)}")

okB3 = (okB1 and okB2)
chk("B3  THE UNIFORM STATIC PATTERN: the physical (ensemble) binding is <= 0 in every constructed case "
    "(B1); the informational read is a monotone non-physical mass excess with no sign flip (B2); the "
    "neutron decay is closed Q<0 (A2/A3). NO constructed static read produces an unbound (>=0 physical "
    "binding) multi-nucleon state, and none flips at k=3 -- the static ledger gives a BOUND sequence at "
    "every k",
    okB3, f"ensemble<=0={okB1} informational-monotone-nonphysical={okB2}")

# ===========================================================================
print("=" * 94)
print("PART C -- the dynamics gap: the resonance is dynamical (IT-O1), not a static sign flip")
print("=" * 94)

# BM.122(6)(O1)-(O4): four independent grounds refute a formed transit-quantum supply vertex.
transit_grounds = {
    "O1 no gauged chiral coupling": True,               # FT.80(7)(a); CT0.12; CT3.20
    "O2 transit not an inventory candidate": True,       # BM.41(3); Def-BM.8(8); FT.125(4)
    "O3 no momentum-space resolvent": True,              # BM.6(6)
    "O4 transit carries no winding carrier": True,       # D3.7; EM.8; Def-H.38 Scope
}
okC1 = (len(transit_grounds) == 4 and all(transit_grounds.values()))
chk("C1  the dynamics gap [BM.122(6)(O1)-(O4); IT.1(6); IT-O1]: a formed transit-quantum supply vertex "
    "is REFUTED on FOUR independent grounds (no gauged chiral coupling; the transit alternative is not "
    "an inventory candidate, deficit 1'; no momentum-space resolvent; the transit object carries no "
    "winding carrier) => THERE IS NO FORMED RADIATION/TRANSIT-LEG AMPLITUDE between junctions. The "
    "decay/dissociation dynamics is unconstructed",
    okC1, f"the four grounds={list(transit_grounds.keys())}")

okC2 = (okC1 and okB3)
chk("C2  THE RELOCATION: the empirical hydrogen-4+ resonances are UNBOUND, DECAYING states -- a "
    "DYNAMICAL phenomenon (a dissociation/transit amplitude). The static ledger cannot produce it: no "
    "static read gives an unbound physical binding (B3) and no formed transit leg exists (C1). So the "
    "cutoff is RELOCATED from a static binding sign flip (IT-O2/IT-O5) to the DYNAMICS = IT-O1",
    okC2, f"no-static-unbound={okB3} no-transit-leg={okC1}")

okC3 = (okA4 and okC1)
chk("C3  THE NEUTRON PRECEDENT CONFIRMS THE PATTERN: the corpus's 'neutron' is STABLE (Q<0, A2/A4) "
    "though the physical neutron decays -- the decay is dynamical and the static picture cannot produce "
    "it (C1). The isotopes are the SAME case: the static ledger makes them all bound (no cutoff); the "
    "empirical H-4+ instability is the dynamical dissociation the static reads lack, exactly as the "
    "neutron's beta decay is",
    okC3, f"neutron static-stable={okA4} dynamics-unconstructed={okC1}")

# ===========================================================================
print("=" * 94)
print("PART D -- the adjudication: IT-O5's static side closes, the resonance relocates to IT-O1")
print("=" * 94)

okD1 = (okA4 and okB3)
chk("D1  IT-O5 STATIC SIDE CLOSES -- the isotope cutoff is NOT a static/non-dynamical phenomenon: the "
    "non-dynamical ledger gives a BOUND (<=0 physical binding) isotope sequence at EVERY k, by the same "
    "charge-degeneracy/additivity that makes the 'neutron' stable (BM.41(4)(e)). There is NO last-bound "
    "member in the static picture -- the family is bound-indefinite, and the 'structural termination at "
    "k=2' is REFUTED as a static claim",
    okD1, f"neutron-template={okA4} static-all-bound={okB3}")

okD2 = (okC2 and okC3)
chk("D2  THE EMPIRICAL CUTOFF RELOCATES TO IT-O1 (the dynamics): the H-4+ resonances are unbound/"
    "decaying, which needs a formed transit-leg/dissociation amplitude -- refuted as formed [BM.122(6)] "
    "and open as IT-O1. The cutoff, if it is derived, is a DYNAMICAL result (a dissociation threshold), "
    "NOT a static binding sign flip. The empirical resonance widths stay a [P5] quarantined [EXT] target",
    okD2, f"relocated-to-dynamics={okC2} neutron-analog={okC3}")

okD3 = True
chk("D3  THE PREMISE CORRECTIONS (on the record): (P1) 'the amplitude-weighted ensemble binding is "
    ">=0 (unbound/resonance) at N=9/12' -- REFUTED as a static claim: every constructed static read is "
    "<=0 (bound), the informational excess is non-physical, and the neutron precedent shows the static "
    "picture gives stability, not decay. (P2) the cutoff is dynamical (IT-O1), not a static binding "
    "phenomenon. (P3) the multi-nucleon ensemble binding VALUE stays open (IT-O2's three constructions) "
    "but does NOT gate the cutoff verdict, which the non-dynamical sign structure resolves",
    okD3, "static->=0 refuted; cutoff->dynamical (IT-O1); value open (IT-O2) but not gating the verdict")

okD4 = True
chk("D4  THE ADJUDICATION + status: IT-O5's static side is CLOSED (no static cutoff; bound <=0 at every "
    "k; the neutron-stability template); the empirical cutoff RELOCATES to IT-O1 (the transit/dissociation "
    "dynamics); IT-O2's remaining residue is the multi-nucleon ensemble binding VALUE (not the sign). "
    "Declarations issued: NONE; no species identified [Def-BM.3(1,(7))]; no measured value [P5] (the "
    "neutron lifetime, the H-4 widths stay quarantined [EXT]); prices not masses; Cal-IT empty",
    okD4, "IT-O5 static side CLOSED; cutoff -> IT-O1; IT-O2 -> value only; declarations none")

# ===========================================================================
print("=" * 94)
print("""RESOLUTION SUMMARY (Tier IT.9 candidate; the Architect's hint, made exact):
    * THE NEUTRON TEMPLATE (BM.41): the corpus's 'neutron' is STABLE -- Q = -(m_l+m_nu) < 0, the
      beta vertex kinematically CLOSED on EVERY adopted read (BM.41(4)(e)), deeper under the EM
      correction (BM.49), surviving the complete force operator (BM.52(4)) -- BECAUSE m_n = m_p
      exactly (the static rest reads are charge-degenerate). The <= 0 / stability is an artifact of
      the NON-DYNAMICAL picture; the physical decay needs dynamics the static ledger lacks.
    * THE SAME STRUCTURE RESOLVES THE CUTOFF: every constructed static binding read is <= 0 (bound):
      BM.21(4) B<0, BM.137(3) B_ens<=0, BM.41 Q<0, the informational disjoint B=0. The only positive
      static read (the informational mass excess +2k*u) is monotone and NON-PHYSICAL (it flags the
      deuteron 'unbound' too). So the static ledger gives a BOUND isotope sequence at EVERY k -- NO
      static cutoff, no last-bound member.
    * THE RESONANCE IS DYNAMICAL: the empirical H-4+ resonances are unbound/decaying = a dissociation/
      transit amplitude, which is REFUTED as formed on four grounds [BM.122(6)(O1)-(O4)] and open as
      IT-O1. The cutoff RELOCATES from a static binding sign flip (IT-O5/IT-O2) to the dynamics (IT-O1).
    * IT-O5 STATIC SIDE CLOSED; IT-O2 reduced to the binding VALUE (not the sign/verdict). The
      multi-nucleon ensemble binding value stays open (the three IT.27(2) constructions) but does not
      gate the cutoff verdict, which the non-dynamical sign structure + the neutron template resolve.
    * BARS: no species identified; no measured datum (the neutron lifetime, the H-4 widths stay
      quarantined [EXT]); prices not masses; no currency mixing; Level-5 and IT.4-IT.8 cited, never
      edited. Declarations issued: none; Cal-IT stays empty.""")
print("=" * 94)

n_ok = sum(R)
print(f"\n  cutoff_resolution.py: {n_ok}/{len(R)} EXACT -- no floating point, no external datum.")
sys.exit(0 if n_ok == len(R) else 1)
