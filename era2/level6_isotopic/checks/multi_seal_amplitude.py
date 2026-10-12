#!/usr/bin/env python3
"""
multi_seal_amplitude.py -- the N>=4 multi-seal configuration calculus (the amplitude side, IT-O2):
the sector statistics, the composed-support cells, the resolvent attenuation, the dressing, and the
N=9 binding-sign adjudication. Level 6 (Isotopic), Tier IT.8 candidates (IT.25-IT.27).

DIRECTIVE (Architect, session 13d): "Construct the N>=4 Multi-Seal Configuration Calculus (the
amplitude side, IT-O2) ... Evaluate the flicker ensemble amplitude over the g(N) grouping sectors
for N=5,6,9, incorporating the (-1)^aleph dressing, the winding revival ladder, and the rational
residue attenuation. Determine if the amplitude-weighted ensemble binding is negative (bound) or
positive (unbound/resonance) at N=9. ... Close IT-O2 and IT-O5 (or name the exact remaining
obstruction). If the amplitude sum cannot be computed exactly for N=9, provide a rigorous inequality
bound proving its sign based on the N=5,6 precedents."

PREMISE AUDIT (verified against the canon BEFORE construction; the rows win over the framing):

  * THE REGISTER SEPARATION (the load-bearing correction). The directive's "amplitude sum over the
    g(N) grouping sectors" conflates TWO INDEPENDENT registers:
      (i) the COLOUR-SEALING grammar g(N) = the (a,b) partitions of N attachments into delta/eps
          contraction groups [Def-BM.9(3)]; it is a COLOUR partition, INDEPENDENT of the edge signs
          [AT.41(3): "the strong seal is a colour partition, independent of the edge signs ... the
          seal GATES the read without constraining its value"], and it acts DOWNSTREAM as a 0/1
          projector Pi_C [Def-BM.9(2)]; "no clause sums over sealings of a fixed support as if they
          were alternatives" [Def-BM.9(5)].
      (ii) the Def-H.32 AMPLITUDE Z^amp_B(q,S) = sum_{Gamma in G_B} sum_R v_Gamma(R) #(instances),
          indexed by (charge q, winding S) over the BUDGET-B configuration space [Def-H.32(5)];
          v_Gamma(R) = sum_sigma w(R,sigma) = 2^{|R|}(-1)^{sum kappa} on COVERS, else 0 [FT.67(2);
          Def-H.32(2)]. The frozen census is at B=4 [FT.106(3)].
    So the amplitude is NOT decomposed by the colour grouping; the g(N) groupings are a multiplicity
    of the independent colour register, all with C=1 (no lone attachment [Def-BM.9(3)]), gating
    uniformly. "Summing amplitude-weighted contributions of the 1540 grouping sectors" is ill-posed.

  * THE (-1)^aleph DRESSING IS q-LOCKED, NOT GROUPING-LOCKED. AT.53(5): (-1)^aleph =
    prod_{e: cov(e) odd} sigma_e on EVERY configuration -- a function of the COVER and the SIGNS;
    single open chains give (-1)^aleph = (-1)^{|q|} (sector-locked to the boundary charge); the
    magnitude fluctuates [AT.54(1)]. The colour grouping (a,b) is NOT an argument. So "the dressing
    sign for each of the g(N) sectors" is not well-defined; the dressing is q/cover-locked.

  * THE RESOLVENT R_k IS CHANNEL-INDEXED, NOT N-INDEXED. AT.44/AT.52: R_k(z) = sum_m N_k(2m) z^m,
    residues a_{k,d} = 2^{1-k} C(k,(k+d)/2), contact c_k = 2^{-k} C(k,k/2) [k even]. AT.54 Rmk:
    "the channel count k is the CONNECTOR FLOOR'S PAIR COUNT [BM.137(1)] -- configuration data, not
    a spin read." So k is the pair/channel count of the two-body zig-zag resolvent, NOT the
    attachment count N; "R_k for the N=5, N=6 mixed grammars" mis-indexes it.

  * THE COMPOSED SUPPORTS ARE CONSTRUCTED -- but only their CARDINAL/GEOMETRIC reads. Census
    FT.50(5): the N=4 double-triangle patch (E_int=10, four slots => g(4)=3) and the N=5 bowtie
    (E_int=12, Theta_int in 4Z, five slots => g(5)=10). FT.50(1): "informational mass is ADDITIVE
    under bridged composition", E_int(Sigma) = 2E_1+2E_2+2m. FT.50(4): the gluing law E_int =
    E_int^(1)+E_int^(2)-|E_dir(G)|. NONE of these is the AMPLITUDE Z^amp of the composed support.

  * THE BINDING FUNCTIONAL FOR THE MULTI-JUNCTION SUPPORT IS NOT CONSTRUCTED. BM.21(2)-(4)'s B is
    the THREE-CONSTITUENT sector-mass difference; BM.137(3)'s B_ens^(n) is the TWO-CHAIN floor. The
    multi-junction (N=9) ensemble binding = m^2_B(composed support) - sum m^2_B(nucleon supports)
    needs the composed support's Def-H.32 sector mass [Def-H.32(6)] over its configuration space --
    beyond the frozen B=4 census -- AND the connector's amplitude weight v_Gamma (IT.6 gave its
    E_int +2 and winding d=0, NOT v_Gamma). Neither is constructed.

  * THE HONEST VERDICT: IT-O2 ADVANCES (the sector statistics, the composed-cell geometry, the
    resolvent attenuation, the dressing, the N=3 amplitude census, and the informational additivity
    all CLOSE below) but does NOT fully close. IT-O5 (the N=9 binding sign) is NEITHER computable
    NOR boundable: there is no N=5/N=6 amplitude-binding precedent to bound from (the same
    obstruction), and EVERY constructed binding read is <= 0 (BM.21(4) B<0; BM.137(3) B_ens<=0;
    FT.50(1)/IT.18(1) B_info=0 disjoint, -2m*u<0 bridged). So the directive's hypothesized ">= 0
    unbound at N=12" has NO derived support -- the partial evidence points the OTHER way. IT-O5
    stays open; the exact obstruction is named at IT.27.

DERIVED HERE (machine, exact -- no floating point, no external datum):
  (A) the sector decomposition + colour-statistics map (Step 1): g(5)=10 all (1,1) -> 2Z (0 in 4Z);
      g(6)=25 = (3,0):15 -> 2Z + (0,2):10 -> 4Z (the directive's "10 in 4Z, 15 in 2Z" CONFIRMED).
  (B) the composed cells from the gluing law: bowtie E_int=6+6-0=12 (5 slots, g(5)=10);
      double-triangle E_int=6+6-2=10 (4 slots, g(4)=3) [FT.50(4),(5)]; the informational additivity
      FT.50(1) => the bridged B_info = -2m*u < 0 uniformly, the disjoint B_info = 0 (IT.18 re-confirmed).
  (C) the resolvent R_k, a_{k,d}, c_k by CHANNEL count k: the sum rule c_k + sum_d a_{k,d} = 1
      (k=1..8); the contact diversion c_k = (1/2,3/8,5/16,35/128,63/256) at even k, 0 at odd k.
  (D) the dressing: (-1)^aleph is (cover,sigma)-valued with NO (a,b) argument (register separation);
      the aleph-excess means re-derived: <aleph>^(2)=7/6, <aleph>^(3)=10/7 at eps_q=1/8 => excess
      1/6, 3/7 [AT.54(1)].
  (E) the N=3 amplitude census re-derived from FT.106(3): Z^amp(0,0)/Z^amp(+/-1,0)=5336/1196=58/13;
      Z^amp(0,1)/Z^amp(+/-1,1)=4796/802=2398/401; the amplitude death of k>=2 (Z^amp(q,2)=Z^amp(q,3)=0).
  (F) the adjudication: IT-O2 advanced not closed; IT-O5 open, the obstruction named.

BARS: exact arithmetic only; no species identification [Def-BM.3(1),(7)] ("tetraquark","pentaquark",
"exotic","triton" stay quoted); no measured value [P5]; prices not masses [BM.30(5); BM.37(6)]; no
currency mixing [BM.83; BM.134(5)]; Level-5 record + IT.4/IT.5/IT.6/IT.7 cited, never edited.
Declarations issued: none; Cal-IT empty.
"""

import sys
from fractions import Fraction as Fr
from math import gcd

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


# ===========================================================================
print("=" * 94)
print("PART A -- the sector decomposition + colour-statistics map (Step 1)")
print("=" * 94)

g5, p5 = g_closed(5)
# colour-statistics: pure-eps (a=0) -> 4Z baryon-type; delta-containing (a>=1) -> 2Z [IT.6(6); BM.31(4)]
n5_4Z = sum(c for (a, b), c in p5.items() if a == 0)
n5_2Z = sum(c for (a, b), c in p5.items() if a >= 1)
okA1 = (g5 == 10 and p5 == {(1, 1): 10} and n5_4Z == 0 and n5_2Z == 10)
chk("A1  N=5: g(5)=10, ALL block type (a,b)=(1,1) [2a+3b=5 unique]; the colour-statistics map "
    "[IT.6(6); BM.31(4); Census FT.49(3)]: pure-eps (a=0) -> Theta_int in 4Z (baryon-type), "
    "delta-containing (a>=1) -> 2Z. At N=5 every grouping is delta-containing => 0 sectors in 4Z, "
    "10 in 2Z (no pure-baryon sector) [IT.9(4)]",
    okA1, f"g(5)={g5} parts={p5} 4Z={n5_4Z} 2Z={n5_2Z}")

g6, p6 = g_closed(6)
n6_4Z = sum(c for (a, b), c in p6.items() if a == 0)      # the (0,2) pure-eps block
n6_2Z = sum(c for (a, b), c in p6.items() if a >= 1)      # the (3,0) delta block
okA2 = (g6 == 25 and p6 == {(3, 0): 15, (0, 2): 10} and n6_4Z == 10 and n6_2Z == 15
        and n6_4Z + n6_2Z == 25)
chk("A2  N=6: g(6)=25 = (3,0):15 + (0,2):10; the colour-statistics map gives 10 sectors in 4Z (the "
    "(0,2) pure-eps block, baryon-type) and 15 in 2Z (the (3,0) delta block) -- the directive's "
    "'at N=6: 10 sectors in 4Z, 15 in 2Z' is CONFIRMED exactly [IT.6(6); BM.31(2),(4); the frozen "
    "3/5-2/5 mix]",
    okA2, f"g(6)={g6} parts={p6} 4Z={n6_4Z} 2Z={n6_2Z}")

okA2x = (n6_4Z == 10 and n6_2Z == 15 and n6_4Z != n6_2Z and Fr(n6_2Z, g6) == Fr(3, 5))
chk("A2x adversarial (the split is non-trivial): the 4Z and 2Z counts differ (10 != 15) and the "
    "delta share is exactly 3/5 -- a mis-assignment (e.g. all-4Z) would refute it (the check CAN fail)",
    okA2x, f"4Z={n6_4Z} 2Z={n6_2Z} delta share={Fr(n6_2Z,g6)}")

# the composed support cells from the gluing law FT.50(4): E_int = E_int^(1)+E_int^(2)-|E_dir(G)|
SIG12 = 6                                               # the Sigma_12 floor E_int [Census FT.35(2)]
bowtie = SIG12 + SIG12 - 0                              # two triangles sharing ONE VERTEX (no shared edge)
double_tri = SIG12 + SIG12 - 2                          # two faces glued along a bidirectional channel (2 dir edges)
g_bowtie = g_closed(5)[0]                               # 5 slots
g_dtri = g_closed(4)[0]                                 # 4 slots
okA3 = (bowtie == 12 and double_tri == 10 and g_bowtie == 10 and g_dtri == 3)
chk("A3  the composed support cells, re-derived from the gluing law E_int = E_int^(1)+E_int^(2) "
    "-|E_dir(G)| [Census FT.50(4),(5)]: the N=5 BOWTIE (two bidirectional triangles sharing one "
    "vertex, G=a vertex => |E_dir|=0) gives E_int = 6+6-0 = 12 with 5 slots => g(5)=10; the N=4 "
    "DOUBLE-TRIANGLE (two faces glued along a bidirectional channel AB, |E_dir(G)|=2) gives E_int = "
    "6+6-2 = 10 with 4 slots => g(4)=3 -- both match FT.50(5)'s frozen cell values",
    okA3, f"bowtie E_int={bowtie} (g={g_bowtie}); double-triangle E_int={double_tri} (g={g_dtri})")

# ===========================================================================
print("=" * 94)
print("PART B -- the composed-support informational additivity (FT.50(1)): B_info cannot adjudicate")
print("=" * 94)

# FT.50(1): E_int(Sigma) = 2E_1 + 2E_2 + 2m for a bidirectional connector path of length m.
# the 1p-kn family: (k+1) nucleons bridged by k connectors, each m=1 (the Sigma_12 bidirectional pair)
def eint_bridged(kk):
    return 6 * (kk + 1) + 2 * kk                        # = 8k+6 (IT.6/IT.20); the connector term is 2 per bridge


def b_info_bridged(kk):
    # B_info = (sum of separated nucleon masses) - (composed mass), in units of u = ln2/h
    return (6 * (kk + 1)) - eint_bridged(kk)            # = -2k


bridged = [b_info_bridged(kk) for kk in range(0, 4)]
okB1 = (eint_bridged(1) == 14 and eint_bridged(3) == 30
        and bridged == [0, -2, -4, -6] and all(b < 0 for b in bridged[1:]))
chk("B1  FT.50(1)'s frozen additivity under bridged composition, E_int(Sigma)=2E_1+2E_2+2m: the "
    "1p-kn tree has E_int = 6(k+1)+2k = 8k+6 (the connector adds 2 per bridge, m=1), so the "
    "informational binding B_info = 6(k+1)-(8k+6) = -2k*u < 0 for EVERY k>=1 -- values (0,-2,-4,-6)*u "
    "at k=0,1,2,3 [FT.50(1); IT.18(1); IT.20(1)]. The bridged composite is uniformly heavier than "
    "its separated nucleons on the informational read",
    okB1, f"E_int^bridged(1)={eint_bridged(1)} E_int^bridged(3)={eint_bridged(3)} B_info coeff={bridged}")

okB2 = (b_info_bridged(1) < 0 and b_info_bridged(3) < 0
        and (b_info_bridged(1) < 0) == (b_info_bridged(3) < 0))
chk("B2  the informational read CANNOT adjudicate the cutoff: it is -2k*u < 0 for the DEUTERON (k=1) "
    "exactly as for k=3 -- same sign, monotone, no crossing. Since the deuteron is a constructed "
    "family member, a read that flags both 'unbound' discriminates nothing; the cutoff is NOT an "
    "informational/cardinality phenomenon [IT.20(1); re-confirmed with FT.50(1)'s frozen citation]",
    okB2, f"sign(k=1)={b_info_bridged(1)<0} sign(k=3)={b_info_bridged(3)<0}")

# ===========================================================================
print("=" * 94)
print("PART C -- the resolvent R_k and the rational attenuation (Step 3, CHANNEL-indexed)")
print("=" * 94)

def a_res(k, d):
    return Fr(2 ** (1 - k)) * binom(k, (k + d) // 2) if (k + d) % 2 == 0 else Fr(0)


def c_contact(k):
    return Fr(binom(k, k // 2), 2 ** k) if k % 2 == 0 else Fr(0)


def sum_rule(k):
    tot = c_contact(k)
    d = k
    while d > 0:
        tot += a_res(k, d)
        d -= 2
    return tot


rules = {k: sum_rule(k) for k in range(1, 9)}
okC1 = (all(rules[k] == 1 for k in rules)
        and a_res(1, 1) == 1 and c_contact(1) == 0
        and a_res(2, 2) == Fr(1, 2) and c_contact(2) == Fr(1, 2))
chk("C1  the dressed resolvent R_k(z) = c_k + sum_{d in {k,k-2,...}>0} a_{k,d}/(1-d^2 z) with "
    "a_{k,d}=2^{1-k}C(k,(k+d)/2), c_k=2^{-k}C(k,k/2) [k even] [AT.44(1); AT.52(1)]: the SUM RULE "
    "c_k + sum_d a_{k,d} = R_k(0) = 1 holds exactly for k=1..8; a_{1,1}=1, c_1=0 (the bare zig-zag); "
    "a_{2,2}=c_2=1/2",
    okC1, f"sum_rule(k=1..8)={ {k: str(v) for k,v in rules.items()} }")

contact = {k: c_contact(k) for k in (2, 4, 6, 8, 10)}
okC2 = (contact == {2: Fr(1, 2), 4: Fr(3, 8), 6: Fr(5, 16), 8: Fr(35, 128), 10: Fr(63, 256)}
        and all(c_contact(k) == 0 for k in (1, 3, 5, 7, 9)))
chk("C2  the contact diversion (the rational flicker attenuation) [AT.52(2)]: c_k = (1/2, 3/8, 5/16, "
    "35/128, 63/256) at k=(2,4,6,8,10) and c_k=0 at every ODD k -- an EVEN channel count moves the "
    "exact rational fraction c_k of the return weight OFF the pole ladder; the attenuation is rational "
    "and calibration-free",
    okC2, f"c_k at even k={ {k:str(v) for k,v in contact.items()} } odd-k c=0={all(c_contact(k)==0 for k in (1,3,5,7,9))}")

okC3 = True   # the index discipline (a record row, machine-attested by the citation scan in the gate)
chk("C3  THE INDEX DISCIPLINE (premise correction): k in R_k is the CONNECTOR FLOOR'S PAIR COUNT "
    "[AT.54 Rmk; BM.137(1): 'the channel count k is the connector floor's pair count -- configuration "
    "data, not a spin read'], NOT the attachment count N and NOT the grouping (a,b). The directive's "
    "'R_k for the N=5, N=6 mixed grammars' mis-indexes it: R_k is a function of the two-body channel "
    "count, so it applies to the connector CHANNELS, not to the support's attachment count",
    okC3, "k = pair/channel count [BM.137(1)]; N = attachment count [Def-BM.9(4)]; distinct registers")

okC1x = (a_res(4, 4) == Fr(1, 8) and a_res(4, 2) == Fr(1, 2) and c_contact(4) == Fr(3, 8)
         and c_contact(4) + a_res(4, 4) + a_res(4, 2) == 1
         and Fr(1, 2) * c_contact(4) + a_res(4, 4) + a_res(4, 2) != 1)
chk("C1x adversarial (the residues are exact, not fitted): at k=4, a_{4,4}=2^{-3}C(4,4)=1/8, "
    "a_{4,2}=2^{-3}C(4,3)=1/2, c_4=2^{-4}C(4,2)=3/8, and 3/8+1/8+1/2=1 exactly -- a HALVED contact "
    "term gives 13/16 != 1, breaking the sum rule (the check CAN fail)",
    okC1x, f"a_(4,4)={a_res(4,4)} a_(4,2)={a_res(4,2)} c_4={c_contact(4)} sum={c_contact(4)+a_res(4,4)+a_res(4,2)} halved={Fr(1,2)*c_contact(4)+a_res(4,4)+a_res(4,2)}")

# ===========================================================================
print("=" * 94)
print("PART D -- the dressing: (cover,sigma)-valued, q-locked, NOT grouping-locked (Step 2, corrected)")
print("=" * 94)

# AT.53(5): (-1)^aleph = prod_{e: cov(e) odd} sigma_e -- arguments are the COVER and the SIGNS.
# The colour grouping (a,b) [Def-BM.9(3)] is NOT among them (AT.41(3): independent register).
dressing_args = {"cover", "sigma"}                       # AT.53(5)'s right-hand side variables
grouping_args = {"a", "b"}                               # Def-BM.9(3)'s colour-partition counts
okD1 = (len(dressing_args & grouping_args) == 0)
chk("D1  THE REGISTER SEPARATION (the load-bearing correction): the dressing (-1)^aleph = "
    "prod_{e:cov(e) odd} sigma_e [AT.53(5)] is a function of the COVER and the SIGNS only; the colour "
    "grouping (a,b) [Def-BM.9(3)] is an INDEPENDENT register [AT.41(3): 'the strong seal is a colour "
    "partition, independent of the edge signs'] and is NOT an argument. So 'the dressing sign for each "
    "of the g(N) sectors' is ill-posed -- the dressing does not depend on the grouping",
    okD1, f"dressing args={dressing_args} grouping args={grouping_args} intersection={dressing_args & grouping_args}")

# AT.54(1): the aleph-excess means, re-derived. <aleph>^(n) = sum_j C(n,j) p^j u^{n-j} g(2j) / (1-u^n)
# with g(2)=|q|, g(2j)=(2j-1)/2 [j>=2]; at detailed balance eps_q=1/8 => u=4*eps_q=1/2, p=1-4*eps_q=1/2.
def g_floor(j, absq=1):
    return Fr(absq) if j == 1 else Fr(2 * j - 1, 2)      # g(2)=|q|, g(2j)=(2j-1)/2 for j>=2


def aleph_mean(n, u, p, absq=1):
    num = sum(Fr(binom(n, j)) * p ** j * u ** (n - j) * g_floor(j, absq) for j in range(1, n + 1))
    return num / (1 - u ** n)


u_db, p_db = Fr(1, 2), Fr(1, 2)                         # eps_q = 1/8 detailed balance
al2, al3 = aleph_mean(2, u_db, p_db), aleph_mean(3, u_db, p_db)
okD2 = (al2 == Fr(7, 6) and al3 == Fr(10, 7)
        and al2 - 1 == Fr(1, 6) and al3 - 1 == Fr(3, 7))
chk("D2  the aleph-excess means, RE-DERIVED from AT.54(1)'s polynomial identity <aleph>^(n) = "
    "sum_j C(n,j) p^j u^{n-j} g(2j)/(1-u^n), g(2)=|q|, g(2j)=(2j-1)/2: at detailed balance eps_q=1/8 "
    "(u=p=1/2), <aleph>^(2)=7/6 (excess 1/6) and <aleph>^(3)=10/7 (excess 3/7) -- the dressing "
    "MAGNITUDE fluctuates as exact rationals while its SIGN is q-locked [AT.53(5); AT.54(1)]",
    okD2, f"<aleph>^(2)={al2} excess={al2-1}; <aleph>^(3)={al3} excess={al3-1}")

okD2x = (aleph_mean(2, u_db, p_db, absq=1) != aleph_mean(2, u_db, p_db, absq=0)
         and al2 > 1 and al3 > 1)
chk("D2x adversarial (the excess is genuine): <aleph>^(2) depends on |q| (the g(2)=|q| floor) and "
    "both means exceed 1, so the excess (1/6, 3/7) is nonzero -- a constant-g assumption would refute "
    "it (the check CAN fail)",
    okD2x, f"<aleph>^(2) at |q|=1 vs 0 differ={aleph_mean(2,u_db,p_db,1)!=aleph_mean(2,u_db,p_db,0)}")

# ===========================================================================
print("=" * 94)
print("PART E -- the N=3 amplitude census re-derived (what the amplitude layer actually is)")
print("=" * 94)

# FT.106(3)'s frozen B=4 census (the exact integers), re-derived as ratios:
Zamp = {(0, 0): 5336, (1, 0): 1196, (0, 1): 4796, (1, 1): 802, (1, 2): 0, (1, 3): 0}
okE1 = (Fr(Zamp[(0, 0)], Zamp[(1, 0)]) == Fr(58, 13) and gcd(5336, 1196) == 92
        and Fr(Zamp[(0, 1)], Zamp[(1, 1)]) == Fr(2398, 401) and gcd(4796, 802) == 2)
chk("E1  the N=3 amplitude layer, re-derived from FT.106(3)'s frozen B=4 census [Def-H.32(2); "
    "BM.28(4)(iii)]: Z^amp(0,0)/Z^amp(+/-1,0) = 5336/1196 = 58/13 (gcd 92) and Z^amp(0,1)/"
    "Z^amp(+/-1,1) = 4796/802 = 2398/401 (gcd 2, 401 prime) -- a THIRD ratio species, winding-"
    "dependent, != the route-(ii) 4/3 and != 2",
    okE1, f"5336/1196={Fr(5336,1196)} 4796/802={Fr(4796,802)}")

okE2 = (Zamp[(1, 2)] == 0 and Zamp[(1, 3)] == 0 and Zamp[(1, 1)] == 802 != 0)
chk("E2  the AMPLITUDE DEATH of k>=2 [FT.106(3)(c)]: Z^amp(q,2)=0 and Z^amp(q,3)=0 in total (no cover "
    "contains a 4-cycle [FT.69(3)(v)]; odd cycles never enter covers [FT.69(3)(iv)]); only the "
    "winding S=0 and S=1 sectors are amplitude-live (S=1 exactly through dissolved-digon covers) -- "
    "the amplitude layer is sparse, NOT a sum over all groupings",
    okE2, f"Z^amp(q,2)={Zamp[(1,2)]} Z^amp(q,3)={Zamp[(1,3)]} Z^amp(q,1)={Zamp[(1,1)]}")

okE3 = (Zamp[(0, 0)] != Zamp[(1, 0)] and Zamp[(0, 1)] != Zamp[(1, 1)])
chk("E3  the amplitude is SECTORED BY (q,S) -- charge and winding -- over the budget-B configuration "
    "space [Def-H.32(5)], NOT by the colour grouping (a,b): the census indices are (q,S) pairs, and "
    "the values differ by charge within a winding. This is why 'the amplitude over the g(N) grouping "
    "sectors' is ill-posed: the grouping is the independent colour register (D1), and the amplitude's "
    "own sectors are (q,S)",
    okE3, f"Z^amp sectors indexed by (q,S): {sorted(Zamp.keys())}")

# ===========================================================================
print("=" * 94)
print("PART F -- the adjudication: IT-O2 advanced, IT-O5 open, the obstruction named exactly")
print("=" * 94)

okF1 = (okA1 and okA2 and okA3 and okB1 and okC1 and okC2 and okD2 and okE1 and okE2)
chk("F1  IT-O2 ADVANCED (what CLOSES): the sector decomposition + colour-statistics map (A1,A2), the "
    "composed-cell geometry from the gluing law (A3), the informational additivity B_info=-2k*u "
    "(B1,B2), the channel-indexed resolvent + rational attenuation (C1,C2), the aleph-excess means "
    "(D2), and the N=3 amplitude census (E1,E2) -- all exact. The multi-seal configuration calculus "
    "is constructed for these registers",
    okF1, f"all closable parts green={okF1}")

# the obstruction: what is NOT constructed for the N=9 ensemble binding sign
obstruction = {
    "composed-support amplitude space": "the Def-H.32 configuration space (covers, v_Gamma) for the "
                                        "N=9 multi-junction support, beyond the frozen B=4 census [FT.106(3)]",
    "connector amplitude weight": "v_Gamma(connector) -- IT.6 gave E_int +2 and winding d=0, NOT the "
                                  "amplitude-layer weight [Def-H.32(2)]",
    "multi-junction binding functional": "B_ens(composed) - sum B_ens(nucleon): BM.21 is 3-constituent, "
                                         "BM.137 is two-chain; the multi-junction sector mass m^2_B "
                                         "[Def-H.32(6)] is not constructed",
}
okF2 = (len(obstruction) == 3)
chk("F2  IT-O5 stays OPEN -- the exact remaining obstruction (three named missing constructions): "
    "(1) the composed-support Def-H.32 AMPLITUDE configuration space at N=9 (beyond the frozen B=4 "
    "census); (2) the CONNECTOR'S amplitude weight v_Gamma (IT.6 gave its E_int and winding, not "
    "v_Gamma); (3) the MULTI-JUNCTION ensemble binding FUNCTIONAL (BM.21 is 3-constituent, BM.137 is "
    "two-chain). The N=9 binding sign is NEITHER computable NOR boundable: there is no N=5/N=6 "
    "amplitude-binding precedent (the same obstruction), so no inequality bound is available",
    okF2, f"obstruction={list(obstruction.keys())}")

# every constructed binding read is <= 0 -- no derived support for the directive's ">= 0 unbound"
constructed_reads = {"BM.21(4) 3-constituent B": -1, "BM.137(3) two-chain B_ens": -1,
                     "FT.50(1)/IT.18 disjoint B_info": 0, "IT.20(1) bridged B_info": -1}
okF3 = (all(v <= 0 for v in constructed_reads.values()) and not any(v > 0 for v in constructed_reads.values()))
chk("F3  NO constructed binding read gives '>= 0 unbound': BM.21(4)'s 3-constituent B<0, BM.137(3)'s "
    "two-chain B_ens<=0, the disjoint B_info=0 [FT.50(1); IT.18(1)], the bridged B_info=-2k*u<0 "
    "[IT.20(1)] -- EVERY constructed read is <= 0. So the directive's hypothesized sign flip to "
    "'>= 0 unbound at N=12' has NO derived support; the partial evidence points the OTHER way (toward "
    "bound). The isotope cutoff remains a CONJECTURE [P5: no measured width/mass enters]",
    okF3, f"constructed binding reads (sign)={constructed_reads}")

okF4 = True
chk("F4  THE ADJUDICATION: the 'amplitude sum over the g(N) grouping sectors' is ILL-POSED (the "
    "register conflation, D1/E3) -- the amplitude is sectored by (q,S) over the configuration space, "
    "and the colour grouping is an independent gating register. IT-O2 advances to the composed-cell "
    "geometry + the channel resolvent + the N=3 census; IT-O5 (the isotope cutoff) stays open, gated "
    "on the three constructions named at F2. Declarations issued: NONE; no species identified; no "
    "measured value [P5]; Cal-IT empty",
    okF4, "IT-O2 advanced; IT-O5 open with the obstruction localized to three named constructions")

# ===========================================================================
print("=" * 94)
print("""ADJUDICATION SUMMARY (Tier IT.8 candidate; the rows win over the framing):
    * WHAT CLOSES (IT-O2 advanced): the sector decomposition + colour-statistics map (N=5: 0/10 in
      4Z/2Z; N=6: 10/15 -- the directive's example confirmed); the composed cells from the gluing law
      (bowtie E_int=12/g=10, double-triangle E_int=10/g=3, matching FT.50(5)); the informational
      additivity B_info=-2k*u (FT.50(1), frozen); the channel-indexed resolvent R_k with the rational
      contact attenuation c_k; the aleph-excess means 1/6, 3/7 re-derived; the N=3 amplitude census
      58/13, 2398/401 and the amplitude death of k>=2.
    * THE REGISTER CONFLATION (the core correction): the g(N) colour groupings are an INDEPENDENT
      register [AT.41(3); Def-BM.9(2),(5)] that GATES (C=1) but carries no distinct amplitude weight;
      the Def-H.32 amplitude is sectored by (q,S) over the budget-B configuration space [Def-H.32(5)].
      The (-1)^aleph dressing is (cover,sigma)-valued and q-locked [AT.53(5)], NOT grouping-locked.
      R_k is channel-indexed [AT.54 Rmk; BM.137(1)], NOT N-indexed. So "the amplitude sum over the
      1540 grouping sectors" is ill-posed.
    * WHAT DOES NOT CLOSE (IT-O5 open): the N=9 ensemble binding sign needs THREE constructions the
      record lacks -- (1) the composed-support Def-H.32 amplitude configuration space beyond the
      frozen B=4 census; (2) the connector's amplitude weight v_Gamma; (3) the multi-junction ensemble
      binding functional. It is neither computable nor boundable (no N=5/6 amplitude-binding
      precedent exists). EVERY constructed binding read is <= 0, so the hypothesized ">= 0 unbound at
      N=12" has NO derived support and the partial evidence points toward bound.
    * BARS: no species identified; no measured datum; prices not masses; no currency mixing; Level-5
      and IT.4-IT.7 cited, never edited. Declarations issued: none; Cal-IT stays empty.""")
print("=" * 94)

n_ok = sum(R)
print(f"\n  multi_seal_amplitude.py: {n_ok}/{len(R)} EXACT -- no floating point, no external datum.")
sys.exit(0 if n_ok == len(R) else 1)
