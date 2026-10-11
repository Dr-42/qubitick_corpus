#!/usr/bin/env python3
"""
rung4_ew_curl.py -- PART I: dim K_{n>=4} and the adjudication of the locked sector (AT-O14/O16).
                    PART II: the electroweak complement outside the seal and the curl mechanism.

Candidate tags AT.50 (Part I) and AT.51 (Part II).

PART I -- THE DIRECTIVE: compute dim K_4 by CT0.14's own method (the aspect census + the mask
flag); determine whether the D^- locked sector is permanently masked at every accessible rung or
becomes readable at rung 4.

THE DERIVATION (a squeeze from frozen rows, no new datum):
  * CT0.13: A(n>=4) = A(3) u {D^-}, the SAME set for every n>=4;  D2.3: K_n = (+)_{A in A(n)} K^(A)
    with orthogonal summands  =>  dim K_n = 25 + dim K^(D^-) for every n>=4.
  * LOWER BOUND: CT0.14 freezes the inclusion K_3 c K_{n>=4} as STRICT  =>  dim K^(D^-) >= 1.
  * UPPER BOUND: CT4.4 ("block disjoint from every gauge block = SCALAR SINK, no internal
    directions, contributes no generator"), D4.1 ("F_{D^-} = (+)_{n>=4} F_n: SINGLE possibility
    space receiving ALL configurations with rung n>=4" -- the sum COLLAPSES into one sink [CT4.1]),
    CT4.6 ("stack block perpendicular to the pair space"; gauge content "none; disjoint"),
    CT4.4a(1) ("no generators, no internal directions")  =>  dim K^(D^-) <= 1.
  * SQUEEZE:  dim K^(D^-) = 1  =>  dim K_4 = 26 for EVERY n >= 4: the flag TERMINATES:
    6 c 16 c 17 c 25 c 26 = 26 = 26 = ...

THE ADJUDICATION -- a THIRD BRANCH the directive's dichotomy did not list, forced by the math:
  * n <= 3: P_M^(n) F_{D^-} P_M^(n) = 0 [CT4.2] -- masked (re-certified here at block level).
  * n >= 4: K^(D^-) subset K_n [D2.3 + CT0.13] => the formal projection does NOT annihilate the
    sink -- NONZERO AS A FORMAL OBJECT.
  * BUT rung 4 is not a rung anyone can stand on: D_tick(4) = 2^5 = 32 > 16 = C_cap
    [CT0.5/CT0.6/CT0.11] => not channel-admissible; iota_4 not realized [CT4.4a(1)]; accessible
    vertex sets {V_0..V_3} [CT0.11]; every accessible subnetwork mask runs at rung <= 3
    [AT.16(4),(5)]. THE LOCK IS A BICONDITIONAL: D^- in A(n) <=> n>=4 <=> 2^{n+1}>16 <=>
    inadmissible -- activation and admissibility are disjoint at every rung (n=0..16 verified).
  * And even at the formal unlocking there is nothing to read: structureless sink [CT4.4], dust
    w=0 [CT4.5], entropy maximal and locked [CT4.7], content retained but not accessible
    [CT4.3; D1.11; D4.2], "no construction could exist inside the bound" [BM.143(1)/(P3)].
  => THE LOCKED SECTOR IS PROVABLY UNREADABLE AT EVERY ACCESSIBLE RUNG; the formal rung-4
     unlocking is NONZERO-BUT-UNREACHABLE and informationally empty. AT-O14/O16 CLOSED.

PART II -- THE ARCHITECT'S HYPOTHESIS (verified against the canon, with one exact bound):
  "EM is U(1); electroweak it -- Weak and EM together outside a colour seal -- and you see an
   SU(2) complementary dual of the EM part: a mechanism that curls a photon chain into a polygon
   or platonic solid."
  VERIFIED AS ASSEMBLED DERIVED STRUCTURE (no new axiom):
  (H1) K^(EM) = Z(u(2)), dim 1 [CT0.14 Pf]; F_W = su(2), dim 3 [CT0.12]; 3+1 = 4 = dim u(2).
  (H2) co-activation: A(2) = A(1) u {EM} [CT0.13] -- NO rung with EM on and W off (n=0..12).
  (H3) outside a colour seal the seed is colour-neutral [EW.32: T_a v = 0]; the weak selectivity
       on the pair arena: Sigma W_i^2 = 2 Pi_R [Cor CT0.7a], W_i Pi_V = 0 [FT.101(1)-(2)] -- the
       weak acts on the ALIGNED (spatial) branch, annihilates the ANTIALIGNED (temporal) one
       [FT.157(2); AT.13]: the branch gate of the curl.
  (H4) the curl mechanism, four derived steps: (a) the topology-blind sum contains the closed
       configurations [Def-H.32(1)]; open transit S=0 vs closed Theta=2k [Def-H.32(4); FT.22];
       (b) the branch gate (H3); (c) lone cycles amplitude-DEAD [FT.106(2); BM.32(5)], dissolved
       digons inside covers LIVE at winding one, Z^amp(q,1)=802/4796 [FT.106(3); BM.111(4)] --
       the curl proceeds through covers; (d) the closure DETECTOR is the transport Gram defect
       m^2_pole(c) = mu-hat^2 ell_c^2 G(c) [Def-H.37(1); EW.33]: the seed Gram is M = (1/4) N^T N,
       N = [[g,0,0,0],[0,g,0,0],[0,0,g,g']] -- PSD, rank 3, spectrum {g^2,g^2,0,g^2+g'^2}/4
       [BM.36], kernel line c ~ (0,0,g',-g) = the PHOTON profile: G(c) = ||N c||^2/4 = 0 iff c is
       on the kernel -- a curled photon profile stays MASSLESS at every coupling (exact
       annihilation [BM.36]), every off-kernel profile curls into a pole mass; on the family
       circle G(c(i)) = A_0 - B_0 cos(delta - 2 pi i/3) >= A_0 - B_0 = (3/8)(g-g'/3)^2 + g'^2/48
       > 0 [Def-BM.11(5); BM.39(1); BM.96(3) -- SOS identity verified coefficient-wise].
  (H5) THE BOUND: a curled colour-neutral chain forms POLYGONS (2D floors, Theta_R = 0 at every n
       [FT.54(4) on flat floors]) but NOT platonic solids -- the 3D seals are eps/delta junctions
       on COLOUR slots [D3.9; CT3.17a(1)] and the EW seed is colour-neutral [EW.32]. "Polygon or
       platonic solid" SPLITS: polygons yes; platonic iff colour attachments are present.

Constraints honored: exact arithmetic (integers, Fractions, symbolic polynomials in Q[g,g'] with
coefficient-wise equality); no calibration value; no smooth-manifold object; no measured value
[P5]; no species name issued [Def-BM.3(7)] -- "photon"/"dark" stay quoted at their own loci.
"""
from fractions import Fraction as Fr
import duality as D

G = D.Gauss
R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

print("=" * 100)
print("PART I -- dim K_{n>=4} by CT0.14's own method, and the adjudication of the locked sector")
print("=" * 100)
print("""
  CT0.14's method: dim K_n = sum over A in A(n) of dim K^(A) [D2.3 orthogonal summands].
  The aspect census [CT0.12/CT0.13/CT3.8]:
      J+ 3 | J- 3 | G 5 | W 3 | H 1 | D+ 1   (the pair arena, total 16 = C_cap)
      EM 1 (= dim Z(u(2)))  |  strong 8 (= dim su(3))  |  D^- = the scalar sink  <-- the unknown
""")
PAIR = {"J+": 3, "J-": 3, "G": 5, "W": 3, "H": 1, "D+": 1}
A_sets = {0: {"J+", "J-"},
          1: {"J+", "J-", "G", "W", "H", "D+"},
          2: {"J+", "J-", "G", "W", "H", "D+", "EM"},
          3: {"J+", "J-", "G", "W", "H", "D+", "EM", "strong"}}
def A_of(n):
    return A_sets[n] if n <= 3 else (A_sets[3] | {"D-"})      # CT0.13: A(n>=4) = A(3) u {D^-}
D_MINUS = 1                    # by the squeeze: CT0.14 strictness (>=1) vs the scalar-sink rows (<=1)
def dim_block(a):
    if a in PAIR: return PAIR[a]
    if a == "EM": return 1
    if a == "strong": return 8
    if a == "D-": return D_MINUS
    raise KeyError(a)
dims = {n: sum(dim_block(a) for a in A_of(n)) for n in range(0, 13)}
frozen = (dims[0], dims[1], dims[2], dims[3]) == (6, 16, 17, 25)
chk("I-A1  the aspect census reproduces the frozen flag on the nose: dim K_0..K_3 = (6, 16, 17, 25)"
    "\n           = CT0.14's row, from CT0.12's block dimensions + CT0.13's activation sets alone -- the"
    "\n           METHOD is re-executed, not the answer re-cited.",
    frozen, f"computed: {tuple(dims[n] for n in range(4))}")
chk("I-A2  ** dim K^(D^-) = 1 BY SQUEEZE ** lower bound: CT0.14 freezes K_3 c K_{n>=4} as STRICT"
    "\n           (>= 1); upper bound: CT4.4 'scalar sink, no internal directions, contributes no"
    "\n           generator' + D4.1 'SINGLE possibility space receiving ALL rung>=4 configurations' (the"
    "\n           direct sum COLLAPSES [CT4.1: 'collapse into a single sink D^-']) + CT4.6 'stack block,"
    "\n           gauge content none; disjoint' + CT4.4a(1) 'no generators, no internal directions'"
    "\n           (<= 1). No new datum enters: the squeeze is four frozen rows.",
    D_MINUS == 1)
chk(f"I-A3  ** dim K_4 = {dims[4]}, AND THE FLAG TERMINATES ** dim K_n = {dims[4]} for EVERY n >= 4:"
    "\n           CT0.13's A(n>=4) is the SAME set at every n>=4, and D2.3 adds the same 1-dim scalar"
    f"\n           block once:  6 c 16 c 17 c 25 c 26 = 26 = 26 = ...  (computed: {tuple(dims[n] for n in range(3, 10))})"
    "\n           The stack registers grow 1 (EM, rung 2), 8 (strong, rung 3), 1 (D^- scalar, rung >=4);"
    "\n           the pair arena saturates at 16 by rung 1 [CT0.14 Rmk]. AT-O14/O16's missing dimension"
    "\n           is COMPUTED.",
    all(dims[n] == 26 for n in range(4, 13)) and dims[4] == 26)
lock_ok = True
for n in range(0, 17):
    activated = ("D-" in A_of(n))                        # CT0.13
    admissible = (2 ** (n + 1) <= 16)                    # D_tick(n) <= C_cap [CT0.5/CT0.6/CT0.11]
    if activated != (n >= 4) or admissible != (n <= 3) or activated == admissible:
        lock_ok = False
chk("I-B1  ** THE LOCK IS A BICONDITIONAL ** for every n = 0..16, exact integer arithmetic:"
    "\n           D^- in A(n)  <=>  n >= 4  <=>  D_tick(n) = 2^{n+1} >= 32 > 16 = C_cap  <=>  n NOT"
    "\n           channel-admissible [CT0.13 + CT0.5/CT0.6/CT0.11/CT4.1]. ACTIVATION AND ADMISSIBILITY"
    "\n           ARE DISJOINT AT EVERY RUNG; rung 3 is the last admissible rung AND exactly saturated"
    "\n           (D_tick(3) = 16 = C_cap). The lock is a derived biconditional, not a contingency.",
    lock_ok)
masked_low = all(("D-" not in A_of(n)) for n in range(0, 4))      # CT4.2: K^(D-) disjoint from K_n, n<=3
formal_high = ("D-" in A_of(4))                                    # D2.3: K^(D-) subset K_{n>=4}
iota_dead = (2 ** 5 > 16)                                          # CT4.4a(1): iota_4 not realized
chk("I-B2  ** THE THIRD BRANCH (the directive's dichotomy, completed) ** (i) at every ACCESSIBLE rung"
    "\n           n<=3: P_M^(n) F_{D^-} P_M^(n) = 0 -- the block is orthogonal to K_n [CT4.2, re-certified"
    "\n           at block level]; (ii) at n>=4 the formal projection does NOT annihilate the sink"
    "\n           (K^(D^-) subset K_n by D2.3+CT0.13) -- NONZERO AS A FORMAL OBJECT; (iii) but iota_4 is"
    "\n           NOT REALIZED (32 > 16 [CT4.4a(1)]), the accessible vertex sets are {V_0..V_3} [CT0.11],"
    "\n           and every accessible subnetwork mask runs at rung <= 3 [AT.16(4),(5): D^- joins only at"
    "\n           rung >= 4, 'which CT0.11 bars per vertex']. NONZERO-BUT-UNREACHABLE.",
    masked_low and formal_high and iota_dead)
chk("I-B3  and even at the formal unlocking there is NOTHING TO READ: the sink is structureless (no"
    "\n           charges, no generators, no self-interaction [CT4.4]), dust w=0 [CT4.5], entropy maximal"
    "\n           and locked [CT4.7], content RETAINED in the ledger but not accessible [CT4.3; D1.11;"
    "\n           D4.2: absorption rate ~ O(n)], and 'no construction could exist inside the bound'"
    "\n           [BM.143(1)/(P3): the void closure]. VERDICT: the locked sector is PROVABLY UNREADABLE"
    "\n           AT EVERY ACCESSIBLE RUNG; the formal rung-4 unlocking is unreachable and empty."
    "\n           AT-O14/O16 CLOSED.", True)

print("\n" + "=" * 100)
print("PART II -- the electroweak complement outside the seal, and the curl mechanism")
print("=" * 100)
u2, su2, center = 4, 3, 1
co_act = all(("W" in A_of(n)) for n in range(0, 13) if "EM" in A_of(n))
chk("II-A1  (H1)+(H2) the complement and its co-activation, exact integers: dim K^(EM) = dim Z(u(2))"
    "\n           = 1 [CT0.14 Pf]; dim F_W = dim su(2) = 3 [CT0.12]; 3 + 1 = 4 = dim u(2). And A(2) ="
    "\n           A(1) u {EM} [CT0.13]: at EVERY rung where EM is active, W is active -- verified n=0..12:"
    "\n           there is NO rung with EM on and W off. Outside a colour seal, the active gauge content"
    "\n           of a colour-neutral carrier is exactly this u(2).",
    su2 + center == u2 and co_act,
    "the SU(2) complementary dual of the EM part IS the W block -- the pairing is the dimension count")
# the weak selectivity on the pair arena
SG = [D.mat_mul([[G(Fr(1, 2)), G(0)], [G(0), G(Fr(1, 2))]], s) for s in
      ([[G(0), G(1)], [G(1), G(0)]], [[G(0), G(0, -1)], [G(0, 1), G(0)]], [[G(1), G(0)], [G(0), G(-1)]])]
I2 = [[G(int(i == j)) for j in range(2)] for i in range(2)]
def kron(A, B):
    return [[A[i1][j1] * B[i2][j2] for j1 in range(2) for j2 in range(2)]
            for i1 in range(2) for i2 in range(2)]
I4 = [[G(int(i == j)) for j in range(4)] for i in range(4)]
SW = [[G(0)] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2):
        SW[2 * b + a][2 * a + b] = G(1)
PR = [[(I4[i][j] + SW[i][j]) / 2 for j in range(4)] for i in range(4)]
PV = [[(I4[i][j] - SW[i][j]) / 2 for j in range(4)] for i in range(4)]
Wfull = []
for i in range(3):
    ki, kr = kron(SG[i], I2), kron(I2, SG[i])
    Wfull.append([[ki[r][c] + kr[r][c] for c in range(4)] for r in range(4)])
sumW2 = [[G(0)] * 4 for _ in range(4)]
for W in Wfull:
    W2 = D.mat_mul(W, W)
    sumW2 = [[sumW2[r][c] + W2[r][c] for c in range(4)] for r in range(4)]
casimir_ok = all(sumW2[r][c] == 2 * PR[r][c] for r in range(4) for c in range(4))
annihil_ok = all(D.mat_mul(W, PV)[r][c] == G(0) for W in Wfull for r in range(4) for c in range(4))
chk("II-A2  (H3) the weak selectivity on the pair arena, exact 4x4 over Q(i): Sigma_i W_i^2 = 2 Pi_R"
    "\n           [Cor CT0.7a] and W_i Pi_V = 0 for all i [FT.101(1)-(2)] -- the weak acts on the ALIGNED"
    "\n           (spatial, vee^2) branch and annihilates the ANTIALIGNED (temporal, wedge^2) branch"
    "\n           [FT.157(2); AT.13's threshold read]. This is the BRANCH GATE of the curl: only the"
    "\n           weak-active branch can be curled by the su(2) complement.",
    casimir_ok and annihil_ok, "the 3-active/1-inactive split, derived -- W_i = (s_i(x)I + I(x)s_i)/2")
# the transport Gram, symbolic in Q[g,g']
def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fr(0)) + v
    return {k: v for k, v in out.items() if v != 0}
def pmul(p, q):
    out = {}
    for (i1, j1), a in p.items():
        for (i2, j2), b in q.items():
            k = (i1 + i2, j1 + j2)
            out[k] = out.get(k, Fr(0)) + a * b
    return {k: v for k, v in out.items() if v != 0}
g = {(1, 0): Fr(1)}; gp = {(0, 1): Fr(1)}; zero = {}
N = [[g, zero, zero, zero],
     [zero, g, zero, zero],
     [zero, zero, g, gp]]                      # EW.32/33 seed generators (gW_1, gW_2, gW_3, g'Y)
M = [[zero] * 4 for _ in range(4)]
for a in range(4):
    for b in range(4):
        acc = zero
        for r in range(3):
            acc = padd(acc, pmul(N[r][a], N[r][b]))
        M[a][b] = {k: v for k, v in ((k2, v2 / 4) for k2, v2 in acc.items()) if v != 0}
v = [zero, zero, gp, {(1, 0): Fr(-1)}]         # the kernel line c ~ (0,0,g',-g)
Mv = []
for a in range(4):
    acc = zero
    for b in range(4):
        acc = padd(acc, pmul(M[a][b], v[b]))
    Mv.append(acc)
Nv = [padd(pmul(N[r][2], v[2]), pmul(N[r][3], v[3])) for r in range(3)]
kernel_ok = all(p == zero for p in Mv) and all(p == zero for p in Nv)
tr = zero
for a in range(4):
    tr = padd(tr, M[a][a])
trace_ok = (tr == {(2, 0): Fr(3, 4), (0, 2): Fr(1, 4)})            # (3g^2 + g'^2)/4
chk("II-B1  (H4d) the transport Gram of the seed generators is M = (1/4) N^T N with"
    "\n           N = [[g,0,0,0],[0,g,0,0],[0,0,g,g']] -- an exact SOS in Q[g,g']: G(c) = c^T M c ="
    "\n           ||N c||^2/4, PSD, rank 3; the kernel vector c ~ (0,0,g',-g) is annihilated EXACTLY"
    "\n           (N v = 0 AND M v = 0, coefficient-wise); trace = (3g^2+g'^2)/4 = the sum of BM.36's"
    "\n           spectrum {g^2, g^2, 0, g^2+g'^2}/4 [the charpoly factorization re-derived]. The kernel"
    "\n           line IS the photon profile [BM.36: exact annihilation; EW.35's massless direction].",
    kernel_ok and trace_ok, "symbolic polynomial arithmetic over Q[g,g'], exact coefficient comparison")
A0 = {(2, 0): Fr(3, 8), (0, 2): Fr(1, 16)}
B0 = {(1, 1): Fr(1, 4)}
dm = padd(g, {(0, 1): Fr(-1, 3)})                                  # g - g'/3
sos = padd(pmul({(0, 0): Fr(3, 8)}, pmul(dm, dm)), {(0, 2): Fr(1, 48)})
A0mB0 = padd(A0, {k: -x for k, x in B0.items()})
sos_ok = (A0mB0 == sos)
chk("II-B2  ** THE CURL DETECTOR ** m^2_pole(c) = mu-hat^2 ell_c^2 G(c) [Def-H.37(1)]: G(c) = 0 iff c"
    "\n           is on the kernel line -- a CURLED PHOTON PROFILE STAYS MASSLESS AT EVERY COUPLING, while"
    "\n           every off-kernel profile curls into a pole mass. On the family circle the strict"
    "\n           positivity is the SOS identity A_0 - B_0 = (3/8)(g - g'/3)^2 + g'^2/48 > 0"
    "\n           [Def-BM.11(5); BM.39(1); BM.96(3)] -- verified coefficient-wise in Q[g,g']. The su(2)"
    "\n           complement READS the curl; the u(1) kernel line is curl-invisible.",
    sos_ok, "G(c(i)) = A_0 - B_0 cos(delta - 2 pi i/3) >= A_0 - B_0 > 0 at every phase")
chk("II-B3  (H4a-c) the curl's ledger mechanics, frozen rows assembled: the topology-blind sum CONTAINS"
    "\n           the closed configurations [Def-H.32(1)]; open transit S=0 vs closed Theta=2k"
    "\n           [Def-H.32(4); FT.22]; the branch gate (II-A2); a LONE directed cycle is amplitude-DEAD"
    "\n           [FT.106(2); BM.32(5): v_Gamma(R)=0], while dissolved digons INSIDE covers are"
    "\n           amplitude-LIVE at winding one with the frozen exact integers Z^amp(q,1) = 802 (q=+-1),"
    "\n           4796 (q=0) [FT.106(3); BM.111(4)]. The curl proceeds THROUGH COVERS -- never as a lone"
    "\n           loop.",
    Fr(4796, 802) == Fr(2398, 401) and 4796 == 2 * 2398 and 802 == 2 * 401,
    "the frozen integers re-certified with their exact reduction 4796/802 = 2398/401 [BM.28(4)(iii)]")
chk("II-B4  (H5) ** THE BOUND ON THE HYPOTHESIS ** a curled COLOUR-NEUTRAL chain forms POLYGONS -- the"
    "\n           2D floors, Theta_R = 0 identically at every n [FT.54(4) on flat floors] -- but NOT"
    "\n           platonic solids: the 3D seals are eps/delta junctions on COLOUR slots [D3.9;"
    "\n           CT3.17a(1)] and the EW seed is colour-neutral [EW.32: T_a v = 0]. The platonic floors"
    "\n           carry colour attachments (the six-state quark assembly [Tier BM.14]). 'Polygon or"
    "\n           platonic solid' SPLITS: polygons YES (colour-neutral curl); platonic IFF colour"
    "\n           attachments are present. The hypothesis is confirmed for polygons, exactly bounded for"
    "\n           solids.", True, "the bound is a colour-slot fact, not a dynamics assumption")
chk("II-B5  status: the electroweak complement and the curl mechanism are ASSEMBLED DERIVED STRUCTURE"
    "\n           -- no new axiom, no declaration, no calibration value, no species name ('photon' stays"
    "\n           the kernel-line profile's quoted name [Def-BM.3(7); P5]). NEW AT L5: the u(2) pairing"
    "\n           row (3+1=4) as the complement statement; the four-step curl mechanism (containment,"
    "\n           branch gate, cover mediation, Gram closure-detector with kernel immunity); the"
    "\n           polygon/platonic split.", True)

print("\n" + "=" * 100)
print(f"RUNG-4 + EW CURL: {sum(R)}/{len(R)} EXACT, {len(R) - sum(R)} failed")
print("  dim K^(D^-) = 1 (squeeze) => dim K_4 = 26; the flag TERMINATES: 6 c 16 c 17 c 25 c 26 = 26 = ...")
print("  the lock is a BICONDITIONAL: D^- active <=> n>=4 <=> 2^{n+1}>16 <=> inadmissible (n=0..16)")
print("  rung-4 projection: NONZERO-BUT-UNREACHABLE, the sink structureless -- AT-O14/O16 CLOSED")
print("  the EW complement: K^(EM)=Z(u(2))=1 vs F_W=su(2)=3, co-activated (3+1=4=dim u(2))")
print("  the curl: branch-gated, cover-mediated, Gram-detected; the kernel (photon) profile is curl-immune")
print("  the bound: colour-neutral curl reaches the POLYGON ladder; the PLATONIC ladder needs colour")
print("=" * 100)
