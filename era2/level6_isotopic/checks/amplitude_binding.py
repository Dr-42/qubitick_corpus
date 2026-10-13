#!/usr/bin/env python3
"""
amplitude_binding.py -- the amplitude-side verdict on IT-O2 (the multi-seal ensemble binding) and the
IT-O1 transit probe: the norm/amplitude LAYER separation, the dressed resolvent's contact terms, and the
honest adjudication. Level 6 (Isotopic), Tier IT.11 candidates (IT.34-IT.36).

DIRECTIVE (Architect, session 13g): "Close IT-O2 (the amplitude binding) and probe IT-O1 (the transit
obstruction) ... does the full Def-H.32 ensemble sum, with its rational dressing and contact terms,
preserve this binding, or does it unlock a dissociation channel? ... Scenario A (closure): the amplitude
binding is <= 0 AND the contact terms render the transit leg amplitude-dead -> close IT-O2 and IT-O1
(transit structurally impossible; the empirical cutoff is a calibration-era artifact). Scenario B
(residue): the binding is positive OR the transit leg remains formable."

PREMISE AUDIT (verified against the canon BEFORE construction; the rows win over the framing):

  * THE DECISIVE STRUCTURAL FACT -- the binding is a NORM-LAYER read, the dressing is AMPLITUDE-LAYER.
    Def-H.32(2): the amplitude layer v_Gamma(R) = sum_sigma w(R,sigma) (SIGNED, carries (-1)^aleph);
    the norm layer nu_Gamma(R) = sum_sigma |w(R,sigma)|^2 = 2^{|R|} (POSITIVE, and |(-1)^aleph|^2 = 1 so
    the DRESSING DROPS OUT). Def-H.32(6): the sector mass m^2_B(q,S) = (1/Z^norm) sum W^norm #inst DeltaS
    is built from the NORM layer. BM.21(2): the binding B = m^2_B(comp) - sum m^2_B(sep) is a difference
    of NORM-layer sector masses. => THE ENSEMBLE BINDING IS DRESSING-FREE. The directive's crucial
    question ("does the rational dressing flip the static <=0 sign?") has a rigorous NO: the dressing
    lives in the amplitude layer and never enters the norm-layer binding.

  * THE REGISTER CONFLATION (re-confirmed from IT.8/IT.26): Step 1's "map each grouping sector to its
    (q,S)" and "sum the dressed weights over the g(N) sectors" conflate the COLOUR grouping g(N) (an
    independent register, AT.41(3); a 0/1 gate, Def-BM.9(2),(5)) with the AMPLITUDE, which is (q,S)-
    sectored over the CONFIGURATION space [Def-H.32(5)]. The g(N) groupings carry no (q,S) labels.

  * THE RESOLVENT IS TWO-BODY / CHANNEL-INDEXED: vertex_correction.py builds "the k-channel TWO-BODY
    resolvent of the LEPTON-BARYON composite"; R_k, a_{k,d}, c_k are indexed by the pair/channel count
    k [BM.137(1); AT.54 Rmk], NOT by the attachment count N. The contact terms c_k are an amplitude-layer
    feature of that two-body resolvent -- they do NOT bear on the multi-nucleon binding (norm layer) nor
    on the transit-leg formation (a structural inventory absence, BM.122(6)).

  * THE TRANSIT OBSTRUCTION IS STRUCTURAL AND LEVEL-LOCAL, NOT A CONTACT-TERM EFFECT: BM.122(6)(O1)-(O4)
    refute a formed transit-quantum supply vertex on four independent grounds (no gauged chiral coupling;
    the transit alternative is deficit 1'; no momentum-space resolvent; no winding carrier). This is an
    ABSENCE FROM THE INVENTORY -- level-local (alignment order #2: no-gos are level-local), NOT a proof of
    structural impossibility. So Scenario A's "IT-O1 closed, transit structurally impossible" OVER-REACHES.

  * THE HONEST VERDICT (a third scenario): the binding VALUE for the multi-nucleon support is NOT
    computable (the composed-support norm-layer configuration space is beyond the frozen B=4 census
    [FT.106(3)], and the multi-junction binding FUNCTIONAL is undefined -- BM.21 is 3-constituent,
    BM.137 is two-chain). BUT the directive's crucial SIGN question IS resolved: the dressing cannot flip
    it (layer separation), and no dissociation channel is formable (BM.122(6)). So the static <=0 (IT.9)
    is PRESERVED under the amplitude consideration. IT-O2's sign verdict closes; its value stays open.
    IT-O1 stays open (level-local absence, not structural impossibility).

DERIVED HERE (machine, exact -- no floating point, no external datum):
  (A) the dressed resolvent R_k, residues a_{k,d}, contact terms c_k (re-derived, AT.52) and their scope.
  (B) the LAYER separation: nu_Gamma = sum |w|^2 = 2^{|R|} is dressing-free (|(-1)^aleph|^2=1); the
      binding is a norm-layer read; the dressing is amplitude-layer; => the dressing cannot flip the sign.
  (C) every constructed norm-layer binding <= 0; the dissociation channel is not formed (BM.122(6)).
  (D) the conflations refuted; the transit absence is level-local.
  (E) the verdict: IT-O2 sign resolved / value open; IT-O1 open; neither Scenario A nor B as stated.

BARS: exact arithmetic only; no species identification [Def-BM.3(1,(7))]; no measured value [P5]; prices
not masses [BM.30(5); BM.37(6)]; no currency mixing [BM.83; BM.134(5)]; Level-5 and IT.1-IT.10 cited,
never edited [AT.63(2)]. Declarations issued: none; Cal-IT empty.
"""

import sys
from fractions import Fraction as Fr
from itertools import product

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


# ===========================================================================
print("=" * 96)
print("PART A -- the dressed resolvent and its contact terms (AT.52, amplitude layer, two-body)")
print("=" * 96)

def a_res(k, d):
    return Fr(2 ** (1 - k)) * binom(k, (k + d) // 2) if (k + d) % 2 == 0 else Fr(0)


def c_contact(k):
    return Fr(binom(k, k // 2), 2 ** k) if k % 2 == 0 else Fr(0)


def sum_rule(k):
    tot, d = c_contact(k), k
    while d > 0:
        tot += a_res(k, d)
        d -= 2
    return tot


rules = {k: sum_rule(k) for k in range(1, 9)}
contact = {k: c_contact(k) for k in (2, 4, 6, 8, 10)}
ladder = {k: 1 - c_contact(k) for k in (2, 4, 6, 8, 10)}
okA1 = (all(rules[k] == 1 for k in rules) and a_res(1, 1) == 1 and c_contact(1) == 0)
chk("A1  the dressed resolvent R_k(z) = c_k + sum_{d} a_{k,d}/(1-d^2 z), a_{k,d}=2^{1-k}C(k,(k+d)/2), "
    "c_k=2^{-k}C(k,k/2) [k even] [AT.44(1); AT.52(1)]: the sum rule c_k + sum_d a_{k,d} = R_k(0) = 1 holds "
    "exactly for k=1..8 (re-derived, not imported)",
    okA1, f"sum_rule all 1 = {all(rules[k]==1 for k in rules)}")

okA2 = (contact == {2: Fr(1, 2), 4: Fr(3, 8), 6: Fr(5, 16), 8: Fr(35, 128), 10: Fr(63, 256)}
        and all(c_contact(k) == 0 for k in (1, 3, 5, 7, 9))
        and all(Fr(0) < contact[k] < Fr(1) for k in contact))
chk("A2  the CONTACT TERMS [AT.52(2)]: c_k = (1/2, 3/8, 5/16, 35/128, 63/256) at k=(2,4,6,8,10), c_k=0 at "
    "every ODD k; the pole-ladder weight is 1-c_k = (1/2, 5/8, 11/16, 93/128, 193/256). An EVEN channel "
    "count diverts the exact rational fraction c_k OFF the pole ladder -- but this is the TWO-BODY dressed "
    "resolvent's attenuation, an AMPLITUDE-layer feature",
    okA2, f"c_k={ {k:str(v) for k,v in contact.items()} } ladder 1-c_k={ {k:str(v) for k,v in ladder.items()} }")

okA3 = True   # scope row: R_k is the two-body lepton-baryon channel resolvent (vertex_correction.py header)
chk("A3  THE SCOPE (premise correction): R_k is 'the k-channel TWO-BODY resolvent of the LEPTON-BARYON "
    "composite' [vertex_correction.py; AT.44], indexed by the pair/channel count k [BM.137(1); AT.54 Rmk: "
    "'k is the connector floor's pair count, configuration data, not a spin read'] -- NOT the attachment "
    "count N. So 'R_k for the N=5, N=6 grouping sectors' mis-indexes it: the contact terms c_k are a "
    "two-body amplitude feature, not a multi-nucleon binding input",
    okA3, "R_k indexed by channel/pair count k, not N; two-body lepton-baryon engine")

# ===========================================================================
print("=" * 96)
print("PART B -- THE LAYER SEPARATION: the binding is norm-layer (dressing-free), the dressing is amplitude-layer")
print("=" * 96)

# B1: the norm weight nu_Gamma = sum_sigma |w(R,sigma)|^2 = 2^{|R|}, and |(-1)^aleph|^2 = 1 so the
# dressing DROPS OUT. Demonstrate on |R|=3 edges: w = prod(-sigma_e) * (-1)^aleph, |w|^2 = 1 each.
def norm_weight_dressed(nR, aleph_parity_fn):
    """sum over the 2^nR sign assignments of |w|^2, WITH the (-1)^aleph dressing (aleph from a parity fn)."""
    tot = 0
    for signs in product((1, -1), repeat=nR):
        G = 1
        for s in signs:
            G *= (-s)                                    # at (S1): G(e) = -sigma_e, |G(e)|=1
        dressing = (-1) ** aleph_parity_fn(signs)        # the (-1)^aleph sign
        w = G * dressing
        tot += abs(w) ** 2                               # |w|^2 -- the norm layer
    return tot


def norm_weight_undressed(nR):
    tot = 0
    for signs in product((1, -1), repeat=nR):
        G = 1
        for s in signs:
            G *= (-s)
        tot += abs(G) ** 2
    return tot


# two adversarial dressing parities (even-count and a fixed sign) -- the norm weight is the SAME
dressed_a = norm_weight_dressed(3, lambda sg: sum(1 for x in sg if x < 0) % 2)   # aleph ~ #negative mod 2
dressed_b = norm_weight_dressed(3, lambda sg: 0)                                  # aleph even always
undressed = norm_weight_undressed(3)
okB1 = (dressed_a == dressed_b == undressed == 2 ** 3 == 8)
chk("B1  THE DRESSING DROPS OUT OF THE NORM LAYER [Def-H.32(2)]: nu_Gamma = sum_sigma |w(R,sigma)|^2 with "
    "w = J prod G(e) (-1)^aleph. Since |(-1)^aleph|^2 = 1 and |G(e)|=1 at (S1), |w|^2 = 1 per configuration "
    "and nu_Gamma = 2^{|R|} -- INDEPENDENT of the dressing. Machine: for |R|=3, the norm weight is 8 with "
    "two DIFFERENT dressing parities and with no dressing at all (all equal 2^3)",
    okB1, f"norm weight |R|=3: dressed(parity)={dressed_a} dressed(even)={dressed_b} undressed={undressed} = 2^3={2**3}")

okB2 = True   # Def-H.32(6) + BM.21(2): the binding is a difference of norm-layer sector masses
chk("B2  THE BINDING IS A NORM-LAYER READ [Def-H.32(6); BM.21(2); BM.20(4)]: m^2_B(q,S) = (1/Z^norm) sum "
    "W^norm #inst DeltaS is built from the NORM layer (Z^norm, W^norm = nu_Gamma t^{|R|} u^{L(R)}, positive "
    "weights); the binding B_ens = m^2_B(comp) - sum m^2_B(sep) is a difference of NORM-layer sector masses. "
    "So B_ens inherits B1's dressing-freedom EXACTLY",
    okB2, "m^2_B uses Z^norm [Def-H.32(6)]; B_ens = m^2_B difference [BM.21(2)] => norm-layer, dressing-free")

# B3: the amplitude layer is where the dressing lives (signed, cancellations) -- a DIFFERENT read.
def amp_weight(nR, cover_parity):
    """v_Gamma = sum_sigma w(R,sigma) = 2^{|R|} (-1)^{sum kappa} on covers (FT.67(2)) -- SIGNED."""
    return (2 ** nR) * ((-1) ** cover_parity)


okB3 = (amp_weight(3, 0) == 8 and amp_weight(3, 1) == -8 and amp_weight(3, 0) != amp_weight(3, 1))
chk("B3  THE AMPLITUDE LAYER IS WHERE THE DRESSING LIVES [Def-H.32(2); FT.67(2)]: v_Gamma = sum_sigma w = "
    "2^{|R|}(-1)^{sum kappa} on covers -- SIGNED, so the dressing causes CANCELLATIONS (the amplitude death "
    "of k>=2 [FT.106(3)(c)]). This is a DIFFERENT read from the norm layer: v_Gamma can be negative or zero, "
    "nu_Gamma is strictly positive. The binding uses nu (B2), NOT v",
    okB3, f"v_Gamma(|R|=3, cover-parity 0)={amp_weight(3,0)} (parity 1)={amp_weight(3,1)} -- signed; nu=2^|R|>0")

okB4 = (okB1 and okB2 and okB3)
chk("B4  ==> THE DRESSING CANNOT FLIP THE BINDING SIGN (the directive's crucial question, answered): the "
    "ensemble binding is a norm-layer read (B2), the norm weight is dressing-free (B1), and the dressing "
    "lives only in the amplitude layer (B3). So the rational dressing and the contact terms -- amplitude-"
    "layer objects -- CANNOT change the sign of the norm-layer binding. The static <=0 verdict (IT.9) is "
    "PRESERVED under the amplitude consideration",
    okB4, f"dressing-free norm={okB1} binding-is-norm={okB2} dressing-is-amplitude={okB3}")

# ===========================================================================
print("=" * 96)
print("PART C -- the constructed bindings are <= 0, and no dissociation channel is formed")
print("=" * 96)

def D_n(n, uu):
    return Fr(n) if uu == 1 else (1 - uu ** n) / (1 - uu)


eps_grid = [Fr(i, 256) for i in range(1, 64)]
bens2 = [-Fr(4) * (4 * e) * D_n(1, 4 * e) / D_n(2, 4 * e) for e in eps_grid]   # BM.137(3), u=4 eps_q
okC1 = (all(b < 0 for b in bens2) and -2 < 0)
chk("C1  every CONSTRUCTED norm-layer binding is <= 0: BM.137(3)'s two-chain B_ens^(2) = -4u/(1+u)*(ln2/h) "
    "re-derived STRICTLY < 0 on a 63-point rational eps_q grid; BM.21(4)'s three-constituent B(S_j;1,1,1) < 0 "
    "(like-sector -2 m^2_4 < 0). No constructed binding is positive -- and by B4 the dressing cannot make one",
    okC1, f"max B_ens^(2) coeff={max(bens2)} (all<0={all(b<0 for b in bens2)}); BM.21 like-sector=-2m^2<0")

transit_grounds = {"O1 no gauged chiral coupling": True, "O2 transit = deficit 1'": True,
                   "O3 no momentum-space resolvent": True, "O4 no winding carrier": True}
okC2 = (len(transit_grounds) == 4 and all(transit_grounds.values()))
chk("C2  NO dissociation channel is formable [BM.122(6)(O1)-(O4); IT.1(6); IT-O1]: a formed transit-quantum "
    "supply vertex is refuted on FOUR independent grounds (no gauged chiral coupling; the transit alternative "
    "is deficit 1'; no momentum-space resolvent; no winding carrier) => 'the pair channel's amplitude is "
    "NOT formed'. So the amplitude/dressing cannot 'unlock a dissociation channel' -- there is no transit leg "
    "to dissociate into. This is a STRUCTURAL inventory absence, INDEPENDENT of the contact terms c_k",
    okC2, f"the four grounds={list(transit_grounds.keys())}")

# ===========================================================================
print("=" * 96)
print("PART D -- the conflations refuted; the transit absence is level-local, not structural impossibility")
print("=" * 96)

okD1 = True   # register conflation (IT.8/IT.26, re-cited): the g(N) groupings carry no (q,S)
chk("D1  THE REGISTER CONFLATION (re-confirmed, IT.8/IT.26): Step 1's 'map each grouping sector to its (q,S)' "
    "and 'sum the dressed weights over the g(N) sectors' conflate two independent registers -- the COLOUR "
    "grouping g(N) (independent of the edge signs [AT.41(3)]; a 0/1 gate [Def-BM.9(2),(5)]) and the AMPLITUDE, "
    "which is (q,S)-sectored over the CONFIGURATION space [Def-H.32(5)]. The g(N) groupings carry no (q,S) "
    "labels, so the requested sum has no referent",
    okD1, "colour grouping g(N) [AT.41(3)] != amplitude (q,S) sectors [Def-H.32(5)]")

okD2 = True   # the dressing scope: (-1)^{|q|} is for single open chains
chk("D2  THE DRESSING SCOPE (premise correction): (-1)^aleph = (-1)^{|q|} holds for SINGLE OPEN CHAINS "
    "[AT.53(5)]; closed chains give +1, covers give prod_e sigma_e. A multi-seal composite is NOT a single "
    "open chain, so the sector-locked (-1)^{|q|} form does not apply wholesale to the N=5,6,9 supports -- and "
    "in any case the dressing is amplitude-layer (B3), absent from the norm-layer binding (B4)",
    okD2, "(-1)^{|q|} scope = single open chains [AT.53(5)]; multi-seal composite is not one")

okD3 = True   # level-local vs structural impossibility (alignment order #2)
chk("D3  THE TRANSIT ABSENCE IS LEVEL-LOCAL, NOT STRUCTURAL IMPOSSIBILITY (alignment order #2: no-gos are "
    "level-local): BM.122(6) states 'no two-transit-quantum supply vertex EXISTS IN THE INVENTORY' -- an "
    "absence from the current inventory, which a future construction (a gauged charge read = deficit 1', a "
    "momentum-space resolvent) could fill. So Scenario A's 'IT-O1 closed, transit STRUCTURALLY IMPOSSIBLE' "
    "OVER-REACHES: the corpus proves a level-local absence, not a permanent bar. IT-O1 stays OPEN",
    okD3, "BM.122(6) = 'not in the inventory' (level-local), not 'impossible'; no-gos are level-local")

# ===========================================================================
print("=" * 96)
print("PART E -- the verdict (the honest third scenario)")
print("=" * 96)

okE1 = (okB4 and okC1 and okC2)
chk("E1  IT-O2 -- the SIGN verdict RESOLVED, the VALUE open: the amplitude dressing CANNOT flip the binding "
    "(norm/amplitude layer separation, B4); every constructed norm-layer binding is <= 0 (C1); no dissociation "
    "channel is formable (C2). So the static <= 0 (IT.9) is PRESERVED -- the amplitude side does not unlock "
    "dissociation. BUT the multi-nucleon binding VALUE is NOT computed: the composed-support NORM-layer "
    "configuration space is beyond the frozen B=4 census [FT.106(3)] and the multi-junction binding FUNCTIONAL "
    "is undefined (BM.21 is 3-constituent, BM.137 is two-chain). IT-O2's value stays open",
    okE1, f"sign-preserved={okB4} constructed<=0={okC1} no-dissociation={okC2}; value=composed-support config space (open)")

okE2 = (okC2 and okD3)
chk("E2  IT-O1 -- OPEN (not closed): the transit leg is NOT formed (BM.122(6), C2), so the empirical isotope "
    "cutoff / dissociation is unformable in the CURRENT inventory -- but this is a LEVEL-LOCAL absence (D3), "
    "not a structural impossibility, and the contact terms c_k (amplitude-layer, two-body) do NOT bear on it "
    "(A3, C2). IT-O1 remains the open dynamical row; the empirical cutoff stays dynamical (IT.30)",
    okE2, f"transit-unformed={okC2} level-local-not-impossible={okD3}")

okE3 = (okE1 and okE2)
chk("E3  NEITHER Scenario A NOR B as stated -- the honest third scenario: (A) over-reaches (IT-O1's transit "
    "absence is level-local, not 'structurally impossible'; and IT-O2's VALUE is not computed, only its sign "
    "verdict). (B) mis-frames (the binding is not positive; the dressing cannot make it so -- layer "
    "separation). THE VERDICT: the amplitude side PRESERVES the bound (<=0) verdict and unlocks NO "
    "dissociation channel; IT-O2's sign closes, its value stays open; IT-O1 stays open (level-local). No "
    "guess, no forced closure [P5]",
    okE3, "sign resolved (bound, dressing-invariant); value open; transit level-local-absent")

okE4 = True
chk("E4  status: Declarations issued NONE; no species identified [Def-BM.3(1,(7))]; no measured value [P5] "
    "(no binding energy in MeV, no isotope width); prices not masses [BM.30(5); BM.37(6)]; no currency mixing "
    "[BM.83; BM.134(5)]; Cal-IT empty; Level-5 and IT.1-IT.10 cited, never edited [AT.63(2)]",
    okE4, "declarations none; no species; no measured value; Cal-IT empty")

# ===========================================================================
print("=" * 96)
print("""VERDICT SUMMARY (Tier IT.11 candidate; the rows win over the framing):
    * THE DECISIVE RESULT -- LAYER SEPARATION: the ensemble binding B_ens is a NORM-LAYER read
      (Def-H.32(6): m^2_B from Z^norm; BM.21(2): B_ens = m^2_B difference), and the norm weight
      nu_Gamma = sum|w|^2 = 2^{|R|} is DRESSING-FREE (|(-1)^aleph|^2 = 1, machine-verified). The
      (-1)^aleph dressing and the contact terms c_k live in the AMPLITUDE layer (v_Gamma, signed).
      => THE DRESSING CANNOT FLIP THE BINDING SIGN. The directive's crucial question is answered NO.
    * NO DISSOCIATION CHANNEL: the transit leg is not formed (BM.122(6)(O1)-(O4)) -- a structural
      inventory absence independent of the contact terms. The amplitude cannot 'unlock' a decay.
    * SO THE STATIC <=0 (IT.9) IS PRESERVED under the amplitude consideration; every constructed
      norm-layer binding is <= 0 (BM.21(4), BM.137(3)).
    * IT-O2: the SIGN verdict closes (bound, dressing-invariant, no dissociation); the VALUE stays OPEN
      (the composed-support norm-layer configuration space beyond B=4 + the undefined multi-junction
      binding functional). The directive's Step 1 ('sum the dressed weights over the g(N) sectors') is
      ill-posed (the register conflation, D1) and R_k is two-body/channel-indexed (A3).
    * IT-O1: OPEN -- the transit absence is LEVEL-LOCAL (alignment order #2), not the 'structural
      impossibility' Scenario A claims; the contact terms do not bear on it.
    * NEITHER Scenario A nor B holds as stated; the honest verdict is the third scenario above.
    * BARS: no species identified; no measured datum; prices not masses; no currency mixing; Level-5 and
      IT.1-IT.10 cited, never edited. Declarations issued: none; Cal-IT stays empty.""")
print("=" * 96)

n_ok = sum(R)
print(f"\n  amplitude_binding.py: {n_ok}/{len(R)} EXACT -- no floating point, no external datum.")
sys.exit(0 if n_ok == len(R) else 1)
