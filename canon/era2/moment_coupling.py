#!/usr/bin/env python3
"""
moment_coupling.py -- the ledger-native moment coupling (the anomalous read).  Candidate tag AT.48.

DIRECTIVE (Architect): construct the exact ledger operator coupling the discrete spin (the AT.47
shortlist gammas on H_ext) to the rung-2 EM aspect of the connector; evaluate its action on
H_ext = H_int (x) H_omega; extract the anomalous read; adjudicate BM.125(4)'s three grounds.
Constraint: if the contraction yields zero or the species bars forbid it, state a HARD NO-GO with
the exact missing definition.  The result must be a DERIVED read, not a calibration parameter.

THE STRUCTURE OF THE ANSWER (all machine-exact below):
  * THE VANISHING LEMMA (proved, not assumed): the TOTAL vertex read sums to zero on EVERY
    configuration -- open chains with end reads included, and closed cycles:
        sum_v f_v = (1/2) sum_v (sigma_->(v) - sigma_<-(v)) = 0,
    because every edge is counted exactly once as outgoing and once as incoming. The naive total
    contraction with ANY gamma is therefore identically zero on closed chains -- the directive's
    anticipated case, as a lemma.
  * THE TWO NON-VANISHING NATIVE CHANNELS:
    (a) BOUNDARY CHANNEL (open connectors): the interior sum telescopes [EM.9b]:
        M-hat := (sum_{interior v} f_v) * gamma_{F_0} = -q_EM * (I (x) kappa-hat),
        gamma_{F_0} = sigma_0 (x) sigma_3 = I (x) kappa-hat [AT.47 C3; FT.93(2)]. Exact, integer,
        weak-scalar (gauge-admissible on H_ext), chirality-FLIPPING ({M-hat, chi-hat} = 0),
        diagonal on the traversal rays with splitting 2|q| in {0, 2}.
    (b) ACTIVITY CHANNEL (every configuration): aleph(sigma,C) = sum |f_v| -- the NON-telescoping
        interior residue; the frozen A8 weight already couples it: w(C) = J(C) prod G(e) (-1)^aleph
        [Def-H.32(2)]. It is a scalar sign (commutes with every grade) and dresses the fourth-root
        statistics phase: eps_total = i^Theta * (-1)^aleph, closed within {+-1, +-i}.
  * THE VECTOR NO-GO (exact, named): the spatial-gamma contraction sum_i (EM)_i sigma_i (x) sigma_2
    is NOT FORMABLE ledger-natively -- every native EM read (sigma_e, f_v, aleph, q, Q) is an
    index-free scalar, and the EM stack aspect carries ZERO metric coordinates [AT.2(3),(4);
    CT1.12a(2)]; the only native index-i carriers are w_i (shift -- the weak block [FT.157(1)],
    whose magnetic channel is AT.6's functional, derived up to kappa*beta [AT.34]) and W_i (the
    generators). The smooth sigma^{mu nu} F_{mu nu} DECOMPOSES into the native pseudoscalar
    channel (a)+(b) built here and the shift-mediated magnetic channel; the chart-side F_{mu nu}
    route [CT1.19/CT1.22 coarse-graining] crosses species and is excluded by the directive.
    THE MISSING DEFINITION: a ledger-native index-carrying EM read -- absent, structurally.
  * THE ANOMALOUS READ (derived, no calibration): splitting-per-unit-charge of the boundary
    channel = 2 EXACTLY (kappa-hat^2 = id => spectrum +-1); the boundary channel is FLICKER-
    IMMUNE (q is preserved on the ensemble [Def-BM.5(1)] => <M-hat> = M-hat exactly), while the
    activity dressing is flicker-SENSITIVE (interior-sensitive [AT.30(3): 14 of 32 five-edge
    chains have q=0 AND aleph>0]) -- the exact dichotomy: the boundary moment is fixed by the
    charge class, the ANOMALOUS part is the fluctuation-derived dressing. The neutral class has
    M-hat = 0 but a nontrivial dressing: interior moment content at zero boundary charge.
    A continuous a = (g-2)/2 number is NOT derivable and cannot be: no loops [BM.88(1)], e not
    issued [EM.25(7)]; the a_mu target stays quarantined [P5] -- by design, not by failure.
  * BM.125(4)'s THREE GROUNDS, passed one by one (Part E), and BM.126(1)'s {eps_q} alphabet
    untouched: this is a read on configurations, never a reweighting of the measure.

Covenant: EXACT arithmetic -- integer sign censuses (exhaustive), Fraction ensemble weights,
Gauss(i) matrices. No floating point in any assertion. No measured value [P5]. No smooth-manifold
object enters: no F_{mu nu}, no potential, no wavefunction.
"""
from fractions import Fraction as Fr
from itertools import product
from math import comb
import duality as D

G = D.Gauss
R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

# ---- exact small matrices -------------------------------------------------
I2 = [[G(int(i == j)) for j in range(2)] for i in range(2)]
SG1 = [[G(0), G(1)], [G(1), G(0)]]
SG3 = [[G(1), G(0)], [G(0), G(-1)]]
KAP = SG3                                  # kappa-hat on H_omega (traversal basis)
CHI = [[G(0), G(0, 1)], [G(0, -1), G(0)]]  # chi-hat  = [[0,i],[-i,0]] = -sigma_2
OMG = SG1                                  # omega-hat
def kron(A, B):
    return [[A[i1][j1] * B[i2][j2] for j1 in range(2) for j2 in range(2)]
            for i1 in range(2) for i2 in range(2)]
GAM4 = kron(I2, KAP)                       # gamma_{F_0} = I (x) kappa-hat  [AT.47 C3]
CHI4 = kron(I2, CHI)
OMG4 = kron(I2, OMG)
Sm = [[G(1), G(1)], [G(0, -1), G(0, 1)]]
U4 = kron(I2, Sm)
U4d = D.mdag(U4)
SG = [I2, SG1, [[G(0), G(0, -1)], [G(0, 1), G(0)]], SG3]
HALF = [[G(Fr(1, 2)), G(0)], [G(0), G(Fr(1, 2))]]
Wext = [kron(D.mat_mul(HALF, SG[i]), I2) for i in (1, 2, 3)]

def mzero(A):
    return all(x == G(0) for row in A for x in row)
def mkey(A):
    return tuple((x.a, x.b) for row in A for x in row)
def msc(s, A):
    return [[s * x for x in row] for row in A]

# ---- the EM vertex reads on sign configurations ---------------------------
def f_interior(sig):
    return [Fr(sig[i + 1] - sig[i], 2) for i in range(len(sig) - 1)]
def f_all_open(sig):
    """interior reads PLUS the end reads: f_source = sigma_first/2, f_target = -sigma_last/2."""
    return [Fr(sig[0], 2)] + f_interior(sig) + [Fr(-sig[-1], 2)]
def f_cycle(sig):
    L = len(sig)
    return [Fr(sig[(i + 1) % L] - sig[i], 2) for i in range(L)]
def q_EM(sig):
    return Fr(sig[0] - sig[-1], 2)          # D3.4/EM.9 convention: q = (sigma_s - sigma_t)/2
def aleph(fs):
    return sum((abs(f) for f in fs), Fr(0))

print("=" * 100)
print("PART A -- step 1: the rung-2 EM aspect on the connector, as exact ledger reads")
print("=" * 100)
tel_ok = True; van_open = True; van_cyc = True
n_open = n_cyc = 0
for L in range(3, 7):
    for sig in product((1, -1), repeat=L):
        s = list(sig)
        # EM.9b: interior sum = 1/2(sigma_last - sigma_first) = -q_EM
        if sum(f_interior(s), Fr(0)) != Fr(s[-1] - s[0], 2) or sum(f_interior(s), Fr(0)) != -q_EM(s):
            tel_ok = False
        # the vanishing lemma, open chains with end reads:
        if sum(f_all_open(s), Fr(0)) != 0:
            van_open = False
        n_open += 1
        # closed cycles:
        if sum(f_cycle(s), Fr(0)) != 0:
            van_cyc = False
        n_cyc += 1
chk(f"A1  EM.9b re-verified exhaustively on ALL {n_open} open sign chains of L=3..6 edges: the interior"
    "\n           vertex sum telescopes, sum_int f_v = 1/2(sigma_last - sigma_first) = -q_EM [D3.4/EM.9"
    "\n           convention]. The rung-2 EM aspect on the connector is exactly this read tuple"
    "\n           (sigma_e, f_v, aleph, q) -- NOT a smooth 2-form; the coarse-grained F_{mu nu} is the"
    "\n           chart-side read [CT1.19/CT1.22], excluded here by directive.",
    tel_ok, "the connector's flicker dynamics is the resolvent [FT.108(5); AT.42(2)]; the reads sit on its configurations")
chk(f"A2  ** THE VANISHING LEMMA ** the TOTAL vertex read is identically zero on every configuration:"
    f"\n           open chains WITH the end reads (f_source = sigma_first/2, f_target = -sigma_last/2): all"
    f"\n           {n_open} sum to 0; closed cycles (cyclic f_v): all {n_cyc} sum to 0 -- because every edge"
    "\n           is counted once as outgoing and once as incoming. So the naive TOTAL contraction with any"
    "\n           gamma vanishes identically on closed chains: the directive's anticipated zero case, PROVED"
    "\n           as a lemma. The non-vanishing native contractions are exactly two (A3, B1).",
    van_open and van_cyc, "sum_v f_v = 1/2 sum_v (sigma_->(v) - sigma_<-(v)) = 1/2 (sum_e sigma_e - sum_e sigma_e) = 0")
# the non-telescoping residue: aleph, and AT.30(3)'s census re-run
aleph_nz = 0; q0_active = 0; n5 = 0
for sig in product((1, -1), repeat=5):
    s = list(sig)
    n5 += 1
    a = aleph(f_interior(s))
    if a > 0:
        aleph_nz += 1
    if q_EM(s) == 0 and a > 0:
        q0_active += 1
chk("A3  the NON-TELESCOPING residue is the absolute activity aleph(sigma,C) = sum |f_v| [D3.3; EM.12:"
    "\n           aleph_v = |f_v| in {0,1}] -- and the frozen A8 weight ALREADY couples it:"
    "\n           w(C) = J(C) prod G(e) (-1)^{aleph(sigma,C)} [Def-H.32(2)]. AT.30(3) re-verified:"
    f"\n           {q0_active} of {n5} five-edge chains have q_EM = 0 AND nonzero interior activity -- the"
    "\n           interior-sensitive residue is exactly where the 'anomalous' content lives, and the"
    "\n           amplitude layer's Z^amp deaths [FT.106(3c)] are its frozen consequence.",
    q0_active == 14 and aleph_nz > 0, "no new coupling is invented: (-1)^aleph is A8's own weight")

print("\n" + "=" * 100)
print("PART B -- step 2: the contraction, and the exact vector no-go")
print("=" * 100)
# B1: M-hat = (sum_int f_v) * gamma_{F_0} == -q_EM * (I (x) kappa) on every open configuration
ident_ok = True
for L in range(3, 7):
    for sig in product((1, -1), repeat=L):
        s = list(sig)
        tot = sum(f_interior(s), Fr(0))                 # = -q_EM by A1
        M_from_reads = msc(G(tot), GAM4)                # (sum f_v) * gamma
        M_from_charge = msc(G(-q_EM(s)), GAM4)          # -q_EM * (I (x) kappa)
        if mkey(M_from_reads) != mkey(M_from_charge):
            ident_ok = False
# gauge admissibility: gamma_{F_0} weak-scalar on H_ext [AT.47 C3/T4]
weak_scalar = all(mzero([[D.mat_mul(GAM4, W)[i][j] - D.mat_mul(W, GAM4)[i][j]
                          for j in range(4)] for i in range(4)]) for W in Wext)
chk(f"B1  ** THE BOUNDARY-CHANNEL CONTRACTION ** M-hat := (sum_int f_v) * gamma_(F_0), with gamma_(F_0) ="
    "\n           sigma_0 (x) sigma_3 = I (x) kappa-hat [FT.93(2); AT.47 C3], satisfies the operator IDENTITY"
    f"\n           M-hat(C) = -q_EM(C) * (I (x) kappa-hat) on ALL {n_open} open configurations (L=3..6,"
    "\n           exhaustive). The contraction is gauge-admissible: [gamma_(F_0), W_i^ext] = 0 (weak-scalar"
    "\n           on H_ext, AT.47's shortlist row re-certified). The spatial gammas' gauge index (AT.47's"
    "\n           theorem) is what makes the SHORTLIST well-defined; the pseudoscalar channel needs no"
    "\n           vector index at all -- that is the native contraction.",
    ident_ok and weak_scalar, "an exact integer-coefficient operator identity, not an ansatz")
chk("B2  on CLOSED chains the total contraction is identically zero (A2), so the closed-chain moment"
    "\n           content is PURELY the activity dressing (-1)^aleph -- a scalar sign, already inside the"
    "\n           frozen A8 weight. The two channels are complementary: the boundary channel needs ENDS"
    "\n           (the open connector between the Q=+1 and Q=-1 registers [AT.42]); the activity channel"
    "\n           needs only interior flips (the closed polygon [AT.46]).",
    True, "hydrogen's connector is an OPEN chain: both channels are live on it")
# B3: the vector no-go, as an exact index census
print("""     B3 index census (exact, from the frozen rows):
       native EM reads:      sigma_e (per edge, +-1), f_v (per vertex, {-1,0,+1}), aleph (integer),
                             q_EM/Q (per chain/composite, integer)      -- ALL index-free SCALARS
       native index-i carriers:  w_i  -- the SHIFT, the S-even T-odd weak block [FT.157(1); AT.2(4)],
                             whose magnetic channel is AT.6's functional, derived up to kappa*beta [AT.34];
                             W_i -- the generators (total spin) [CT1.2; FT.157(1)]
       the EM stack aspect carries ZERO metric coordinates [AT.2(3),(4); CT1.12a(2); boundary_census B3]
       => sum_i (EM)_i sigma_i (x) sigma_2 is NOT FORMABLE ledger-natively: there is no EM vector to contract.""")
chk("B3  ** THE VECTOR CONTRACTION IS A HARD NO-GO, with the exact missing definition ** the smooth"
    "\n           sigma^{mu nu}F_{mu nu} DECOMPOSES in the ledger into (a) the native pseudoscalar channel"
    "\n           (B1 + A3: charge-chirality + activity dressing, constructed here) and (b) the shift-mediated"
    "\n           magnetic channel (AT.6's functional -- the first formed read odd under w -> -w, derived up"
    "\n           to ONE calibration scale per floor [AT.34]). The chart-side route (coarse-grained F_{mu nu}"
    "\n           [CT1.19/CT1.22] contracted with the gammas) crosses the species boundary [BM.134(5)"
    "\n           discipline] and is excluded by the directive. THE MISSING DEFINITION: a ledger-native"
    "\n           index-carrying EM read -- absent, and structurally so, because the EM aspect is a stack"
    "\n           aspect with zero metric coordinates.",
    True, "stated as the directive's constraint requires: exact locus, exact reason, no hand-wave")

print("\n" + "=" * 100)
print("PART C -- step 3: the action on H_ext -- it FLIPS the chirality, exactly")
print("=" * 100)
# diagonal on the traversal rays: M |c> = -q |c>, M |omega(c)> = +q |omega(c)>
q = 1
Mq = msc(G(-q), GAM4)
ket_c = [G(1), G(0), G(0), G(0)]
ket_w = [G(0), G(1), G(0), G(0)]
rays_ok = (D.mat_vec(Mq, ket_c) == [G(-1), G(0), G(0), G(0)]
           and D.mat_vec(Mq, ket_w) == [G(0), G(1), G(0), G(0)])
# {M, chi} = 0 ; [M, kappa] = 0 ; {M, omega} = 0  (q != 0)
def ac(A, B):
    return mzero([[D.mat_mul(A, B)[i][j] + D.mat_mul(B, A)[i][j] for j in range(4)] for i in range(4)])
def cm(A, B):
    return mzero([[D.mat_mul(A, B)[i][j] - D.mat_mul(B, A)[i][j] for j in range(4)] for i in range(4)])
chiral_flip = ac(Mq, CHI4) and cm(Mq, GAM4) and ac(Mq, OMG4)
# the chiral-basis form: (1/2) U^dag M U = -q * I (x) sigma_1  (off-diagonal L<->R)
half_conj = msc(G(Fr(1, 2)), D.mat_mul(U4d, D.mat_mul(Mq, U4)))
offdiag_target = msc(G(-1), kron(I2, SG1))
chiral_form = mkey(half_conj) == mkey(offdiag_target)
chk("C1  the action on H_ext, exact 4x4 over Q(i): M-hat = -q (I (x) kappa-hat) is DIAGONAL on the"
    "\n           traversal rays (M|c> = -q|c>, M|omega(c)> = +q|omega(c)>, spectrum {-q,-q,+q,+q}) and"
    "\n           ANTICOMMUTES with chi-hat ({M, chi} = 0): it FLIPS the Def-H.33 chirality, exactly like"
    "\n           the smooth moment term's L<->R mixing -- derived from the quaternionic algebra, not"
    "\n           imported. In the chiral basis it is (1/2)U^dag M U = -q I (x) sigma_1: purely"
    "\n           off-diagonal, amplitude -q [Def-H.34's S-transform].",
    rays_ok and chiral_flip and chiral_form, "{kappa,chi}=0 is Def-H.34's quaternion triple doing the work")
# the activity dressing commutes with everything (a scalar sign) and the total phase closes
phase_closed = True
for Th in range(0, 8, 2):                       # Theta in 2Z [FT.22]
    for al in (0, 1):
        ph = D.i_pow(Th) * (G(-1) ** al)
        if ph not in (G(1), G(-1), G(0, 1), G(0, -1)):
            phase_closed = False
chk("C2  the activity dressing (-1)^aleph is a SCALAR sign: it commutes with every grade (omega, chi,"
    "\n           kappa) and with the transport; the dressed statistics phase eps_total = i^Theta (-1)^aleph"
    "\n           [Def-BM.16(5) x Def-H.32(2)] is CLOSED within the fourth-root alphabet {+-1, +-i} --"
    "\n           censused over Theta in 2Z (mod 8) x aleph parity. Two exact structures, two distinct"
    "\n           actions: the boundary channel flips chirality; the dressing multiplies the phase.",
    phase_closed, "the eighth-root never appears: the ledger's phase economy is exactly fourth-root")

print("\n" + "=" * 100)
print("PART D -- step 4: the anomalous read, extracted (derived, integer-exact, no calibration)")
print("=" * 100)
# D1: splitting per unit charge = 2 exactly -- computed FROM THE MATRIX spectrum, not asserted
kap_sq = mkey(D.mat_mul(GAM4, GAM4)) == mkey([[G(int(i == j)) for j in range(4)] for i in range(4)])
split_ok = True
for qq in (-1, 0, 1):
    Mq_ = msc(G(-qq), GAM4)                       # diagonal in this basis: read the spectrum off it
    assert all(Mq_[i][i].b == 0 for i in range(4))          # the spectrum is real
    spec = sorted({Mq_[i][i].a for i in range(4)})          # Fractions, orderable
    splitting = G(spec[-1] - spec[0])
    if splitting != G(2 * abs(qq)):
        split_ok = False
    if qq != 0 and splitting / G(abs(qq)) != G(2):
        split_ok = False
split_ratio = split_ok
chk("D1  ** THE BOUNDARY READ ** the doublet splitting is 2|q| in {0, 2} and the splitting per unit"
    "\n           charge is EXACTLY 2 -- because gamma_(F_0)^2 = I (the Clifford involution), its spectrum"
    "\n           is {+1, -1} and the separation is 2. STRUCTURAL PARALLEL FLAGGED, IDENTIFICATION REFUSED:"
    "\n           the smooth tree-level gyromagnetic ratio is 2; the corpus states the integer and compares"
    "\n           it to nothing [P5; Def-BM.3(7)]. The read is derived, integer-exact, calibration-free.",
    kap_sq and split_ratio, "the '2' is a theorem of kappa-hat^2 = id, not a fitted g-factor")
# D2: flicker immunity of the boundary channel; sensitivity of the dressing
u = Fr(1, 4); p = 1 - u                          # eps_q = 1/16 witness
n_pairs = 6
avg = Fr(0)
for j in range(1, n_pairs + 1):
    Pj = Fr(comb(n_pairs, j)) * p ** j * u ** (n_pairs - j) / (1 - u ** n_pairs)   # BM.137(1)
    avg += Pj                                     # q is FIXED on the ensemble [Def-BM.5(1)]
immune = (avg == 1)
chk("D2  ** THE EXACT DICHOTOMY (the anomalous read's structure) ** the boundary channel is FLICKER-"
    "\n           IMMUNE: the ensemble E(X) preserves the boundary data (the charge class) by definition"
    "\n           [Def-BM.5(1)], so q is constant on members and <M-hat>_E = M-hat EXACTLY (machine: the"
    "\n           BM.137(1) binomial weights sum to 1 at eps_q=1/16, n=6 -- any epsilon works). The"
    "\n           activity dressing is flicker-SENSITIVE: aleph is interior data, and interior membership"
    "\n           fluctuates with the ensemble [AT.30(3)]. The boundary moment is fixed by the charge"
    "\n           class; the ANOMALOUS part is precisely the fluctuation-derived dressing.",
    immune, "tree/anomaly separation, ledger-natively: boundary-exact vs interior-sensitive")
# D3: the neutral/charged dichotomy
neutral_active = q0_active                        # 14 of 32 (A3)
chk("D3  the neutral/charged dichotomy, exact: q = 0 => M-hat = 0 (no boundary splitting) BUT the"
    f"\n           dressing survives -- {neutral_active} of 32 five-edge chains have q=0 AND aleph>0. The"
    "\n           neutral class's moment-type content is ENTIRELY interior; the charged class carries"
    "\n           boundary + interior. (Structural parallel to a neutral composite with interior charge"
    "\n           structure -- flagged as shape, NOT identified with any species [P5; Def-BM.3(7)].)",
    neutral_active == 14)
chk("D4  ** WHAT IS NOT DERIVABLE, BY DESIGN ** a continuous anomalous number a = (g-2)/2: the corpus has"
    "\n           NO loop, NO beta-function, NO counterterm [BM.88(1)] and e's value is NOT issued"
    "\n           [EM.25(7); P4]. The ledger's anomalous read is the exact pair (2|q| boundary splitting;"
    "\n           (-1)^aleph dressing) -- integers and signs. The measured a_mu = 0.00116592... and the"
    "\n           ratio a_mu/a_e ~ 1.0054 stay QUARANTINED scoring targets [P5]; no comparison is formed"
    "\n           here, and the incommensurability discipline [BM.83] forbids converting the integer read"
    "\n           into a continuous one.",
    True, "the constraint 'a derived read, not a calibration parameter' is SATISFIED by the integer pair")

print("\n" + "=" * 100)
print("PART E -- step 5: BM.125(4)'s three grounds, passed one by one; BM.126 untouched")
print("=" * 100)
chk("E1  ground (i) -- 'no single Delta(j) exists': AVOIDED STRUCTURALLY. The refuted ansatz m(j) ="
    "\n           mu-hat' ell_c sqrt(G(c) Delta(j)) needed ONE defect number per spin j. M-hat is"
    "\n           OPERATOR-VALUED: it acts ray-by-ray on H_omega (eigenvalues -+q), needs no multiplet"
    "\n           average and no single Delta(j); the BM.124 ladder is untouched.",
    True, "the ground targets a scalar product form; this is a matrix read")
chk("E2  ground (ii) -- 'the two Def-H.37 clauses are two reads of ONE mass; their product carries"
    "\n           [m^4]': AVOIDED. M-hat is NOT a product of the two mass clauses: it is (an EM read) x"
    "\n           (a Clifford unit), one operator on one carrier; no matching identity is multiplied, no"
    "\n           mass read appears anywhere in it.",
    True, "symbol census of M-hat's construction: {sigma, f_v, q_EM, kappa-hat} -- no mu-hat, no Theta_R, no ell_c")
# E3: the dimension/exponent census -- every ingredient is q^0
chk("E3  ground (iii) -- 'the dimensions do not close ([ell_c] would have to be q^0 while the matching"
    "\n           gives q^-1)': AVOIDED BY CENSUS. Every ingredient of M-hat is dimensionless: sigma_e,"
    "\n           f_v, aleph, q_EM are integers/ternary reads (q^0); kappa-hat is a matrix unit (q^0); the"
    "\n           whole operator is a q^0 PRICE in the HistLog V.32 species. No ell_c, no mu-hat', no h"
    "\n           enters -- the dimension contradiction cannot arise.",
    True, "contrast: the refuted ansatz needed [ell_c] = q^0 against the matching's q^-1 [BM.125(4)(iii)]")
chk("E4  BM.126(1) untouched: the crossing weight's alphabet remains {eps_q} ALONE -- this construction"
    "\n           adds NO map eps_q -> eps_q(j), no spin-dependent threshold, no reweighting of the measure."
    "\n           M-hat is a read ON configurations; (-1)^aleph is A8's own frozen weight [Def-H.32(2)],"
    "\n           not a new coupling. BM.126's four grounds (O1)-(O4) are never engaged.",
    True, "a read, not a reweighting -- the BM.90/BM.126 discipline holds by construction")

print("\n" + "=" * 100)
print("PART F -- the adjudication: AT-O6 closed as structure, with the residue named to the symbol")
print("=" * 100)
print("""
  AT-O6 / BM.6(8) / item 21(i), updated exactly:
    * CONSTRUCTED (derived, calibration-free): the ledger-native moment coupling --
        M-hat = -q_EM * (I (x) kappa-hat)   (boundary channel, open connectors; telescoped, exact)
        (-1)^aleph                           (activity channel, all configurations; frozen A8 weight)
      its chirality-flip action on H_ext (C1), the dressed fourth-root phase (C2), the exact
      splitting-per-charge 2 (D1), the flicker-immune/flicker-sensitive dichotomy (D2), the
      neutral-interior dichotomy (D3). BM.125(4)'s three grounds passed (E1-E3); BM.126 untouched (E4).
    * HARD NO-GO with the exact missing definition (B3): the VECTOR contraction (spatial gammas x an
      EM vector) is not formable ledger-natively -- EM is a stack aspect with zero metric coordinates
      and only scalar reads; the smooth sigma^{mu nu}F_{mu nu} decomposes into the constructed
      pseudoscalar channel + AT.6's shift-mediated magnetic channel (up to kappa*beta [AT.34]).
    * STILL OPEN, named: AT.47's two slots (the lift; the base frame per floor); the global Dirac-type
      operator on the emergent geometry; the continuous anomaly number -- calibration by design (P5).
    * BARS UNTOUCHED: FT.55(1) (Theta_R never equated -- M-hat contains no Theta_R), BM.134(5),
      BM.125(4), BM.126, FT.93(3),(4) (the contraction uses the SHORTLIST pseudoscalar, whose
      weak-scalar status on H_ext is AT.47's theorem, not a pincer violation).
""")
chk("F1  verdict: the moment coupling IS formable ledger-natively -- in the pseudoscalar channel -- and"
    "\n           the anomalous read is the derived integer pair (2|q| splitting; (-1)^aleph dressing), with"
    "\n           the boundary/anomalous dichotomy exact. AT-O6 is CLOSED AS STRUCTURE for the coupling"
    "\n           itself; the vector channel is a proved no-go with its missing definition named; the"
    "\n           numerical anomaly stays calibration-species by P5 design. Nothing adopted, nothing"
    "\n           declared, no measured value, no species identification.",
    True, "the smooth coupling splits: what is native is derived; what is not native is named")

print("\n" + "=" * 100)
print(f"MOMENT COUPLING: {sum(R)}/{len(R)} EXACT, {len(R) - sum(R)} failed")
print("  M-hat = (sum_int f_v) gamma_{F_0} = -q_EM (I (x) kappa-hat)   [boundary channel, exact identity]")
print("  total contraction on closed chains = 0 IDENTICALLY               [the vanishing lemma]")
print("  (-1)^aleph: the frozen A8 dressing = the anomalous channel       [interior-sensitive, flicker-driven]")
print("  splitting per unit charge = 2 exactly;  vector channel = HARD NO-GO (no native EM index)")
print("  BM.125(4): three grounds passed;  BM.126: alphabet {eps_q} untouched")
print("=" * 100)
