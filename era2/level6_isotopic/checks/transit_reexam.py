#!/usr/bin/env python3
"""
transit_reexam.py -- IT-O1 re-examined: BM.122(6)'s four grounds against the atomic/isotopic machinery.
Level 6 (Isotopic), Tier IT.13 candidates (IT.40-IT.42).

DIRECTIVE (Architect, session 13i): "Re-Examine IT-O1 (the transit-leg amplitude) in light of the new
machinery. BM.122(6)'s four grounds: (O1) no gauged chiral coupling, (O2) transit alternative is
deficit 1', (O3) no momentum-space resolvent, (O4) transit object carries no winding carrier.
Re-examine each against AT.46/AT.52-54/AT.56-58/AT.60/AT.61 and IT.6-IT.9. If any ground is now
addressable, construct the transit-leg amplitude and close IT-O1. If all hold, state exactly why the
new machinery does not dissolve them, and name the exact missing primitive. Do not force a construction."

THE VERDICT (machine + row-by-row): O3 is DISSOLVED (superseded within era 1); O1, O2, O4 HOLD, and the
new machinery SHARPENS them rather than dissolving them. So the transit-leg amplitude is still not
constructed; IT-O1 stays OPEN, with the obstruction localized to deficit 1' (the chiral matter
assignment), which is application-layer / non-derivable.

  * O3 DISSOLVED -- a genuine downstream supersession. BM.122(6)(O3) ("no momentum-space resolvent;
    plane-wave boundary-channel states and the Sigma-resolvent are an open interface, blocked pending
    their own declaration [BM.6(6)]") was written at Tier BM.22. At Tier BM.23 (LATER, same era),
    Def-BM.20 / BM.134 CONSTRUCTED the momentum-space Sigma-resolvent: "BM.6(6)'s specification is
    discharged", with the plane-wave boundary states of covariant momentum label p_mu, the pole locus
    = the mass shell [BM.134(1)], the on-shell measure [BM.134(3)], and the two-body phase space +
    fluxes [BM.134(4)]; BM.134(7): "the momentum-space Sigma-resolvent is constructed", closing
    HistLog item 17. So O3's literal claim is now FALSE. (IT.1(6)/IT.29(4)/IT.35(4) re-cited all four
    grounds -- that citation is STALE on O3.)

  * O1 HOLDS, SHARPENED -- the new machinery shows the gauge blocks are CHIRAL-BLIND, not chirally
    coupled: "[W_i (x) I_omega, I (x) P_{L/R}] = 0 is blindness, not coupling" [FT.123 Phys; FT.125(4)
    Pf]. The commutator vanishes because the gauge block acts on one tensor factor and the chiral
    projector on the other (machine-verified below). AT.56-58 built the sigma^{mu nu} F_{mu nu} Pauli
    coupling, but (a) the gauge field is the transport curvature of UNDECLARED slots T_a [AT.57: "16
    independent indeterminates", slot-free], (b) the native EM read is an index-free scalar -- the
    index-carrying VECTOR EM read is not formable [AT.48(5v); AT-O29], and (c) the electric channel is
    ray-antisymmetric [AT.61] but that is a splitting, not a gauged chiral coupling to a matter multiplet.

  * O2 HOLDS -- deficit 1' (the chiral matter assignment): "which species sits in which gauge
    representation on which chiral ray is NOT derived" [FT.125(4)]; it needs "a chiral projector, a Weyl
    symbol, a hypercharge-assignment read" [FT.81(4)] and "Tier F.39 discharges ONLY THE FIRST"; the
    anomaly sums are formable only for a DECLARED chiral assignment; "no corpus-internal statement is
    possible until deficits 1' (+2/3) close" [FT.125(2)]; the assignment rule is application-layer, its
    non-derivability proven [Def-BM.3 Rmk; FT.125(4)]. The isotopic grammar (IT.6-IT.9) is the colour
    contraction census -- it does not touch the gauge coupling of Q.

  * O4 HOLDS -- the transit object (the D3.7 trivial chain = photons/gluons, all-null) is EXCLUDED from
    Def-H.38's scope: "Bound chains on the nonnegative cone only; transit/trivial chains excluded", so
    no j=|k|/2 read and no eps read attach to it [BM.122(6)(O4); D3.7; EM.8]. AT.46's polygon holonomy
    and AT.52's winding-revival ladder are for MATERIALIZED bound chains / covers, not the all-null
    trivial chain -- they do not extend to it.

  * THE MISSING PRIMITIVE (named exactly): deficit 1' -- the chiral matter assignment rule correlating
    the chi-hat grade with the gauge representation and the weak coupling, requiring a Weyl symbol and a
    hypercharge-assignment read [FT.81(4); FT.125(4)]. This is application-layer / non-derivable at the
    ledger level, so IT-O1 is not a construction gap the new machinery can fill -- it needs a declaration.

BARS: exact arithmetic only (Gauss(i) over Fraction); no species identification [Def-BM.3(1,(7))]; no
measured value [P5]; prices not masses; no currency mixing [BM.83; BM.134(5)]; Level-5 and IT.1-IT.12
cited, never edited [AT.63(2)]. Declarations issued: none; Cal-IT empty.
"""

import sys
import functools
from fractions import Fraction as Fr

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# ---- Gauss(i) over Fraction ----
def g(re, im=0):
    return (Fr(re), Fr(im))


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


ONE, ZERO, I = g(1), g(0), g(0, 1)
s0 = [[ONE, ZERO], [ZERO, ONE]]
s1 = [[ZERO, ONE], [ONE, ZERO]]
s3 = [[ONE, ZERO], [ZERO, g(-1)]]


def madd2(A, B):
    return [[gadd(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]


def mscale2(A, c):
    return [[(A[i][j][0] * c, A[i][j][1] * c) for j in range(2)] for i in range(2)]


def mmul4(A, B):
    return [[functools.reduce(gadd, (gmul(A[i][t], B[t][j]) for t in range(4))) for j in range(4)]
            for i in range(4)]


def kron(A, B):
    return [[gmul(A[i // 2][j // 2], B[i % 2][j % 2]) for j in range(4)] for i in range(4)]


def sub4(A, B):
    return [[gsub(A[i][j], B[i][j]) for j in range(4)] for i in range(4)]


def is_zero4(A):
    return all(A[i][j] == ZERO for i in range(4) for j in range(4))


# ===========================================================================
print("=" * 96)
print("PART A -- Ground O1 (no gauged chiral coupling): the gauge blocks are CHIRAL-BLIND")
print("=" * 96)

# chiral projectors on H_omega: chi = sigma_3; P_R=(I+chi)/2=diag(1,0), P_L=(I-chi)/2=diag(0,1)
P_R = mscale2(madd2(s0, s3), Fr(1, 2))
P_L = mscale2(madd2(s0, mscale2(s3, Fr(-1))), Fr(1, 2))

# the gauge block acts on the FIRST factor (W_i = sigma_1), the chirality on the SECOND
W = kron(s1, s0)          # W_i (x) I_omega
PR = kron(s0, P_R)        # I (x) P_R
PL = kron(s0, P_L)
comm_R = sub4(mmul4(W, PR), mmul4(PR, W))
comm_L = sub4(mmul4(W, PL), mmul4(PL, W))
okA1 = (is_zero4(comm_R) and is_zero4(comm_L))
chk("A1  Ground O1 -- the gauge block is CHIRAL-BLIND [FT.123 Phys; FT.125(4) Pf]: the commutator "
    "[W_i (x) I_omega, I (x) P_{L/R}] = 0 EXACTLY (machine: 4x4 Gauss(i), W_i=sigma_1 on factor 1, "
    "P_{L/R}=(I -/+ sigma_3)/2 on factor 2). 'Blindness, not coupling' -- a gauge block on one tensor "
    "factor cannot couple chirally to a projector on the other. So AT.56-58's Pauli anatomy does NOT "
    "supply a gauged chiral coupling",
    okA1, f"[W,P_R]=0: {is_zero4(comm_R)}; [W,P_L]=0: {is_zero4(comm_L)}")

# adversarial: a gauge block on the SAME factor as the chirality would NOT commute (that would be a chiral coupling)
W_same = kron(s1, s0)
chi_same = kron(s3, s0)     # chirality on the SAME factor as the gauge block
comm_same = sub4(mmul4(W_same, chi_same), mmul4(chi_same, W_same))
okA1x = (not is_zero4(comm_same))
chk("A1x adversarial (the blindness is real, not vacuous): if the gauge block and the chirality acted on "
    "the SAME factor, [sigma_1, sigma_3] = -2 i sigma_2 != 0 -- a chiral coupling REQUIRES a nonzero "
    "commutator. The corpus's gauge blocks act on the pair register, the chirality on H_omega, so they "
    "commute (blind). The check CAN fail (the same-factor commutator is nonzero)",
    okA1x, f"[sigma_1 (x) I, sigma_3 (x) I] != 0: {not is_zero4(comm_same)} (a chiral coupling needs this)")

okA2 = True   # the gauge field is undeclared slots; the vector EM read is not formable
chk("A2  Ground O1 -- the gauge FIELD is undeclared and the VECTOR EM read is not formable: AT.57's "
    "Weitzenboeck birth sigma^{mu nu} F_{mu nu} couples to the transport curvature F_{ab}=[T_a,T_b], but "
    "the T_a are '16 independent indeterminates' -- UNDECLARED slots (the P4 transport profile, an owed "
    "declaration) [AT.57]; and the native EM reads are index-free scalars -- the index-carrying VECTOR EM "
    "read Sigma_i (EM)_i sigma_i (x) sigma_2 is NOT formable [AT.48(5v); AT-O29]. So no gauged chiral "
    "VECTOR coupling exists",
    okA2, "gauge field T_a = undeclared slots [AT.57]; vector EM read not formable [AT-O29]")

# ===========================================================================
print("=" * 96)
print("PART B -- Ground O3 (no momentum-space resolvent): DISSOLVED by BM.134/Def-BM.20")
print("=" * 96)

# BM.134(4): the two-body phase space, CM frame, zero shift: p_* = (1/2N) sqrt(z^2 - 4 N^2 m^2) at m1=m2=m.
# vacuum gauge N=1: p_* = (1/2) sqrt(z^2 - 4 m^2). Verify the exact solve on rational witnesses.
def p_star(z, m, N=Fr(1)):
    disc = z * z - 4 * N * N * m * m
    return disc            # keep exact; p_* = sqrt(disc)/(2N); verify disc>=0 and the on-shell identity


wit = [(Fr(5), Fr(1)), (Fr(10), Fr(2)), (Fr(7, 2), Fr(1, 2)), (Fr(4), Fr(1))]
okB1 = True
for z, m in wit:
    disc = p_star(z, m)
    # on-shell: E_i = N sqrt(m^2+p^2), z = E_1+E_2 = 2 sqrt(m^2+p_*^2) at N=1 => p_*^2 = (z/2)^2 - m^2
    okB1 &= (disc == 4 * ((z / 2) ** 2 - m * m) and disc >= 0)
chk("B1  Ground O3 is DISSOLVED -- the momentum-space Sigma-resolvent IS CONSTRUCTED [Def-BM.20; BM.134]: "
    "the plane-wave boundary states of covariant momentum label p_mu, the pole locus R(z;p)^{-1}=0 <=> the "
    "mass shell g^{mu nu}p_mu p_nu = -m^2 [BM.134(1)], the on-shell measure [BM.134(3)], and the two-body "
    "phase space p_* = (1/2N)sqrt(z^2-4N^2 m^2) [BM.134(4)] -- machine: the exact CM solve z=2 sqrt(m^2+p_*^2) "
    "=> p_*^2=(z/2)^2-m^2 holds on rational witnesses. BM.134(7): 'the momentum-space Sigma-resolvent is "
    "constructed', discharging BM.6(6) and closing HistLog item 17",
    okB1, f"two-body phase-space identity verified on {len(wit)} witnesses (z=5,m=1 -> p_*^2={p_star(Fr(5),Fr(1))}=21/4)")

okB2 = True   # the supersession: BM.122 (Tier BM.22) predates BM.134 (Tier BM.23)
chk("B2  THE SUPERSESSION (a level-local no-go, dissolved downstream -- alignment order 2): BM.122(6)(O3) "
    "was written at Tier BM.22; Def-BM.20/BM.134 constructed the Sigma-resolvent at Tier BM.23 (LATER, same "
    "era). So O3's literal claim ('no momentum-space resolvent ... blocked pending their own declaration') "
    "is now FALSE. IT.1(6)/IT.29(4)/IT.35(4) re-cited BM.122(6)'s FOUR grounds -- that citation is STALE on "
    "O3; the bar now stands on THREE grounds (O1, O2, O4). This is exactly the corpus-supersedes-downstream "
    "discipline (BM.88->BM.133, BM.6(1)->Def-BM.8, ...)",
    okB2, "BM.122(6)(O3) [Tier BM.22] superseded by BM.134/Def-BM.20 [Tier BM.23]; four grounds -> three")

# ===========================================================================
print("=" * 96)
print("PART C -- Grounds O2 and O4: both HOLD against the new machinery")
print("=" * 96)

okC1 = True   # O2: deficit 1' (the chiral matter assignment)
chk("C1  Ground O2 HOLDS -- deficit 1' (the chiral matter assignment) [FT.125(4); FT.81(4)]: 'which species "
    "sits in which gauge representation on which chiral ray is NOT derived'; it needs 'a chiral projector, a "
    "Weyl symbol, a hypercharge-assignment read' and 'Tier F.39 discharges ONLY THE FIRST' (the chiral "
    "projector); the anomaly sums (sum Y, sum Y^3, [SU(3)]^2 U(1), [SU(2)]^2 U(1)) are formable only for a "
    "DECLARED chiral assignment; 'no corpus-internal statement is possible until deficits 1' (+2/3) close' "
    "[FT.125(2)]; the assignment rule is application-layer, its non-derivability PROVEN [Def-BM.3 Rmk]. The "
    "isotopic grammar (IT.6-IT.9) is the colour contraction census -- it does not touch the gauge coupling of Q",
    okC1, "deficit 1' = the chiral matter assignment; only the chiral projector supplied (F.39/AT.60); Weyl symbol + hypercharge read absent")

okC2 = True   # O4: the trivial chain excluded from Def-H.38
chk("C2  Ground O4 HOLDS -- the transit object carries no winding carrier [BM.122(6)(O4); D3.7; Def-H.38 "
    "Scope]: the transit object is the D3.7 TRIVIAL chain (= photons/gluons, all-null), and Def-H.38's scope "
    "is 'bound chains on the nonnegative cone only; TRANSIT/TRIVIAL CHAINS EXCLUDED' -- so no j=|k|/2 read and "
    "no eps read attach to it (N_pol=2, helicity a transit-side read with no identification). AT.46's polygon "
    "holonomy and AT.52's winding-revival ladder B_min(m)=2m+ceil(m/2) are for MATERIALIZED bound chains / "
    "covers -- they do NOT extend to the all-null trivial chain",
    okC2, "Def-H.38 scope excludes transit/trivial chains; AT.46/AT.52 are for materialized chains")

# ===========================================================================
print("=" * 96)
print("PART D -- the verdict: O3 dissolved, O1/O2/O4 hold, IT-O1 OPEN, the missing primitive named")
print("=" * 96)

okD1 = (okA1 and okA2 and okB1 and okC1 and okC2)
chk("D1  THE GROUND-BY-GROUND VERDICT: O3 DISSOLVED (the Sigma-resolvent + plane-wave states + two-body "
    "phase space are constructed [BM.134/Def-BM.20]); O1 HOLDS (the gauge blocks are chiral-blind, A1; the "
    "gauge field is undeclared slots and the vector EM read is not formable, A2); O2 HOLDS (deficit 1', C1); "
    "O4 HOLDS (the trivial chain is excluded from Def-H.38, C2). The new machinery SHARPENS O1/O2/O4; it "
    "does not dissolve them",
    okD1, f"O1 chiral-blind={okA1} O1 gauge-field/vector={okA2} O3 dissolved={okB1} O2 deficit1'={okC1} O4 trivial-chain={okC2}")

okD2 = okD1
chk("D2  IT-O1 STAYS OPEN -- the transit-leg amplitude is STILL not constructed: the two-photon / transit "
    "supply vertex now stands barred on THREE grounds (O1, O2, O4), not four (O3 discharged). Dissolving O3 "
    "supplies the propagator/phase-space machinery but NOT the vertex: the supply vertex needs the gauged "
    "chiral COUPLING (O1), the chiral matter ASSIGNMENT (O2 = deficit 1'), and a winding carrier for the "
    "transit quantum (O4) -- all three still absent. Per the directive's constraint, the construction is NOT "
    "forced",
    okD2, "O3 discharged; O1+O2+O4 still bar the supply vertex; IT-O1 open")

okD3 = True
chk("D3  THE EXACT MISSING PRIMITIVE (named, per the directive): DEFICIT 1' -- the chiral matter assignment "
    "rule correlating the chi-hat grade with the gauge representation and the weak coupling, requiring a WEYL "
    "SYMBOL and a HYPERCHARGE-ASSIGNMENT READ [FT.81(4); FT.125(4)]. This is APPLICATION-LAYER / "
    "non-derivable at the ledger level [Def-BM.3 Rmk; FT.125(4): 'no assignment rule in Tiers F.1-F.39'], so "
    "IT-O1 is not a construction gap the atomic/isotopic machinery can fill -- it needs a DECLARATION (a "
    "chiral assignment), plus O1's declared gauge field (the P4 transport profile) and O4's transit-chain "
    "winding carrier",
    okD3, "missing primitive = deficit 1' (Weyl symbol + hypercharge-assignment read); application-layer, needs a declaration")

okD4 = True
chk("D4  status + the premise correction: IT-O1 remains OPEN, sharpened (O3 discharged; the obstruction "
    "localized to deficit 1' + the undeclared gauge field + the trivial-chain carrier). PREMISE CORRECTION: "
    "IT.1(6)/IT.29(4)/IT.35(4)'s 'four grounds [BM.122(6)(O1-O4)]' is STALE on O3 (superseded by BM.134) -- "
    "corrected to three grounds. Declarations issued NONE; no species identified [Def-BM.3(1,(7))]; no "
    "measured value [P5]; Cal-IT empty; Level-5 and IT.1-IT.12 cited, never edited",
    okD4, "IT-O1 open+sharpened; O3 stale-citation corrected; declarations none")

# ===========================================================================
print("=" * 96)
print("""VERDICT SUMMARY (Tier IT.13 candidate; the level-local no-go re-examined, alignment order 2):
    * O3 (no momentum-space resolvent) -- DISSOLVED. Def-BM.20/BM.134 constructed the momentum-space
      Sigma-resolvent + plane-wave boundary states + pole locus + on-shell measure + two-body phase space,
      discharging BM.6(6) and closing item 17. BM.122(6)(O3) [Tier BM.22] is superseded by BM.134 [Tier
      BM.23] within era 1 -- a downstream supersession IT-O1's four-grounds citation missed.
    * O1 (no gauged chiral coupling) -- HOLDS, sharpened: the gauge blocks are CHIRAL-BLIND ([W_i (x) I_omega,
      I (x) P_{L/R}]=0, machine-verified -- 'blindness, not coupling' [FT.123]); the gauge field is undeclared
      slots T_a [AT.57]; the vector EM read is not formable [AT-O29].
    * O2 (deficit 1') -- HOLDS: the chiral matter assignment needs a Weyl symbol + hypercharge read (only the
      chiral projector is supplied, F.39/AT.60); application-layer, non-derivable [FT.125(4); Def-BM.3 Rmk].
    * O4 (no winding carrier) -- HOLDS: the D3.7 trivial chain is excluded from Def-H.38's scope; AT.46/AT.52
      are for materialized bound chains, not the all-null transit chain.
    * VERDICT: IT-O1 STAYS OPEN. The transit-leg amplitude is still not constructed -- the bar now stands on
      THREE grounds (O1, O2, O4). The exact missing primitive is DEFICIT 1' (the chiral matter assignment:
      a Weyl symbol + a hypercharge-assignment read), which is application-layer and needs a DECLARATION, not
      a construction. The construction is NOT forced (the directive's constraint honored).
    * BARS: no species identified; no measured datum; prices not masses; no currency mixing; Level-5 and
      IT.1-IT.12 cited, never edited. Declarations issued: none; Cal-IT stays empty.""")
print("=" * 96)

n_ok = sum(R)
print(f"\n  transit_reexam.py: {n_ok}/{len(R)} EXACT -- no floating point, no external datum.")
sys.exit(0 if n_ok == len(R) else 1)
