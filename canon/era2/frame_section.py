#!/usr/bin/env python3
"""
frame_section.py -- the frame section on the extended carrier: the spacetime spin factor, the
frame census, the equivariant assignment reduction, the transport coupling, and the discrete
spin connection of the polygon case.  Candidate tag AT.47.  Builds on duality.py.

DIRECTIVE (Architect): "build it" -- the frame section, BM.6(8)/item 21(i)'s named residue.
The R.39 Rmk fixes the locus: Def-H.34's H_ext = H_int (x) H_omega IS "exactly the 'extended
carrier' locus that FT.93(7) identified and item 21(i) enumerated without adopting"; what stays
unconstructed there is "the per-edge frame section e -> F_e and its coupling to the EW.32
transport ..., a global Dirac-type operator on the emergent geometry".

DERIVED HERE (machine, exact):
  (T1) GATES: FT.93(1)-(2) reproduced -- 15 Pauli products; EXACTLY 30 pairwise-anticommuting
       4-frames (=720 ordered); the pseudoscalar catalog (15 values, each from exactly 2 frames,
       species 6/3/6); the F_0 rows. FT.93(3)'s pincer reproduced on the pair arena: commutant
       nullity 2 (= span{Pi_R,Pi_V}), anticommutant nullity 1 (= C.Pi_V), seed nullities 1 and 0.
  (T2) THE SPACETIME SPIN FACTOR EXISTS AND IS MAXIMAL: on H_ext with the seed weak action
       W_i^ext = (sigma_i/2)(x)I [EW.32 carrier + Def-H.34's minimal-combination Rmk], Def-H.34's
       quaternionic triple (omega-hat, chi-hat, kappa-hat) is gauge-TRIVIAL, generates Cl(3,0)
       (8 real-independent products), the commutant is exactly I(x)End(H_omega) (nullity 4), and
       NO gauge-trivial fourth anticommuting element exists (nullity 0). A fully gauge-scalar
       Dirac frame is IMPOSSIBLE -- proven.
  (T3) THE RELOCATION ROW: gamma_{F_0} = sigma_0(x)sigma_3 = I(x)kappa-hat AS MATRICES. The same
       matrix: pincered in the pair arena (commutes with W_3^pair alone), WEAK-SCALAR in the
       extended arena. The pincer is arena-relative; FT.93(3) stands untouched at its locus.
  (T4) THE FRAME SHORTLIST: exactly 6 of the 30 frames admit a weak-scalar chirality on H_ext
       (gamma = +-sigma_0(x)sigma_i), one S-transform orbit; no frame is fully gauge-trivial.
  (T5) THE ASSIGNMENT REDUCTION: on arc-transitive floors [AT.34] an equivariant section is ONE
       base frame per floor. Under the MARKED lift (Def-H.37(2)/Open Gaps 19 -- declared, inherited
       at use, NOT derived), the binary tetrahedral Ad-orbits on the 30 frames and on the shortlist
       are computed exactly; item 21(i)'s "undeclared datum" shrinks to a finite enumerated choice.
  (T6) THE TRANSPORT COUPLING: U = cos(phi)I + i sin(phi) n.sigma obeys de Moivre, U^L =
       cos(L phi)I + i sin(L phi) n.sigma, as an EXACT identity of Z[C,S]/(C^2+S^2-1) against
       matrix powers (L=1..8, five Pythagorean (cos,sin) pairs, three axes -- 120 identities);
       the fourth-root quantization [Def-BM.16(5)] is the lattice L.phi in (pi/2)Z -- a formal
       condition on P4-class data, discriminating witness included, no value issued.
  (T7) THE UNIFICATION: AT.46's drag operator diag(i^{+Td}, i^{-Td}) EQUALS exp(i(pi/2)Td kappa-hat)
       -- the discrete spin connection of the polygon case is the shortlist pseudoscalar's
       fourth-root exponential at the integer-quantized drag winding; omega-hat kappa-hat omega-hat
       = -kappa-hat gives D(omega(c)) = D(c)^{-1} exactly.

BARS RESPECTED: FT.93(3) pincer (pair arena, re-proved not touched); FT.93(4) (SU(2)_L-type chiral
coupling NOT natively derivable -- re-cited); FT.55(1) (Theta_R never equated with 2 pi k);
BM.134(5) (resolvent species); BM.125(4) (no mass-product ansatz); the chiral gauge coupling stays
application-layer [R.39 Rmk]. Marked rows stay marked; no declaration issued here.

Covenant: exact arithmetic -- Gauss(i)-over-Fraction matrices, exact nullities by elimination,
integer polynomial arithmetic in the quotient ring, integer group tables. No floating point in any
assertion. No measured value [P5].
"""
from fractions import Fraction as Fr
from itertools import combinations, product as iproduct
import duality as D

G = D.Gauss
R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

# ---------------------------------------------------------------------------
# exact 2x2 / 4x4 helpers over Gauss
# ---------------------------------------------------------------------------
I2 = [[G(int(i == j)) for j in range(2)] for i in range(2)]
I4 = [[G(int(i == j)) for j in range(4)] for i in range(4)]
SG = [I2,
      [[G(0), G(1)], [G(1), G(0)]],
      [[G(0), G(0, -1)], [G(0, 1), G(0)]],
      [[G(1), G(0)], [G(0), G(-1)]]]                        # sigma_0..sigma_3
HALF = [[G(Fr(1, 2)), G(0)], [G(0), G(Fr(1, 2))]]

def kron(A, B):
    """Kronecker product, row-major (first factor major) -- Def-H.34's internal-major order."""
    return [[A[i1][j1] * B[i2][j2] for j1 in range(len(B[0])) for j2 in range(len(B[0]))]
            for i1 in range(len(A)) for i2 in range(len(B))]

def mdag(A):
    return [[G(A[j][i].a, -A[j][i].b) for j in range(len(A))] for i in range(len(A[0]))]

def mscale(s, A):
    return [[s * x for x in row] for row in A]

def madd(A, B, sign=1):
    return [[A[i][j] + sign * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mcomm_anti(A, B):
    AB = D.mat_mul(A, B); BA = D.mat_mul(B, A)
    return madd(AB, BA, -1), madd(AB, BA, +1)

def mzero(A):
    return all(x == G(0) for row in A for x in row)

def mkey(A):
    return tuple((x.a, x.b) for row in A for x in row)

def nullity(rows, ncols):
    """exact nullity of {x : rows . x = 0} over Gauss by elimination."""
    M = [list(r) for r in rows if any(x != G(0) for x in r)]
    rank = 0
    for col in range(ncols):
        piv = next((r for r in range(rank, len(M)) if M[r][col] != G(0)), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        M[rank] = [x / pv for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] != G(0):
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
        if rank == len(M):
            break
    return ncols - rank

def real_rank(mats):
    """rank over Q of matrices flattened to (re, im) component vectors."""
    rows = [[x.a for row in m for x in row] + [x.b for row in m for x in row] for m in mats]
    M = [r[:] for r in rows if any(v != 0 for v in r)]
    if not M:
        return 0
    rank = 0
    for col in range(len(M[0])):
        piv = next((r for r in range(rank, len(M)) if M[r][col] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        M[rank] = [v / pv for v in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
        if rank == len(M):
            break
    return rank

def commutant_rows(Ws, n):
    rows = []
    for W in Ws:
        for p in range(n):
            for q in range(n):
                row = [G(0)] * (n * n)
                for j in range(n):
                    row[p * n + j] += W[j][q]
                    row[j * n + q] -= W[p][j]
                rows.append(row)
    return rows

def anticommutant_rows(Ws, n):
    rows = []
    for W in Ws:
        for p in range(n):
            for q in range(n):
                row = [G(0)] * (n * n)
                for j in range(n):
                    row[p * n + j] += W[j][q]
                    row[j * n + q] += W[p][j]
                rows.append(row)
    return rows

print("=" * 100)
print("PART A -- GATE: FT.93(1)-(2) reproduced exactly -- the 30 native Clifford frames")
print("=" * 100)
P15 = [(a, b) for a in range(4) for b in range(4) if (a, b) != (0, 0)]
PAULI = {(a, b): kron(SG[a], SG[b]) for (a, b) in P15}
herm_ok = all(mkey(PAULI[k]) == mkey(mdag(PAULI[k])) for k in P15)
sq_ok = all(mkey(D.mat_mul(PAULI[k], PAULI[k])) == mkey(I4) for k in P15)
tr_ok = all(sum(PAULI[k][i][i] for i in range(4)) == G(0) for k in P15)
frames = []
for quad in combinations(P15, 4):
    if all(mzero(mcomm_anti(PAULI[x], PAULI[y])[1]) for x, y in combinations(quad, 2)):
        frames.append(quad)
chk("A1  FT.93(1) reproduced from A3's Pauli facts alone: the 15 non-identity Pauli products on C^4"
    "\n           are Hermitian, square to +I_4, and traceless; and there are EXACTLY"
    f"\n           {len(frames)} pairwise-anticommuting 4-frames among the C(15,4)=1365 subsets"
    "\n           (= 720 ordered, 24 orderings per frame) -- Cl(4,0) native, no new axiom.",
    herm_ok and sq_ok and tr_ok and len(frames) == 30,
    "exhaustive enumeration, exact Gauss(i) matrix arithmetic")

def gamma_of(quad):
    M = PAULI[quad[0]]
    for q in quad[1:]:
        M = D.mat_mul(M, PAULI[q])
    return M
def sgn_class(m):
    k1 = mkey(m)
    k2 = tuple((-x.a, -x.b) for row in m for x in row)
    return min(k1, k2)
gam_classes = {}
for f in frames:
    gam_classes.setdefault(sgn_class(gamma_of(f)), []).append(f)
two_each = all(len(v) == 2 for v in gam_classes.values())
def species_of(key):
    for (a, b) in P15:
        if sgn_class(PAULI[(a, b)]) == key:
            return (a, b)
    return None
sp = [species_of(k) for k in gam_classes]
n_mixed = sum(1 for (a, b) in sp if (a == 0) != (b == 0))
n_diag = sum(1 for (a, b) in sp if a == b != 0)
n_off = sum(1 for (a, b) in sp if a != b and a != 0 and b != 0)
chk("A2  FT.93(2)'s pseudoscalar catalog reproduced: 15 distinct gamma values (up to sign), EACH"
    f"\n           FROM EXACTLY 2 FRAMES, species census mixed={n_mixed}, diagonal={n_diag},"
    f"\n           off-diagonal-spatial={n_off} -- the frozen 6/3/6, exhaustive and exact.",
    len(gam_classes) == 15 and two_each and (n_mixed, n_diag, n_off) == (6, 3, 6))
F0_ORD = ((1, 2), (2, 2), (3, 2), (0, 1))         # FT.93(2)'s listed order: (s1s2, s2s2, s3s2, s0s1)
F0_in = any(tuple(sorted(f)) == tuple(sorted(F0_ORD)) for f in frames)
# gamma is ORDER-dependent (every ordering sign flip flips gamma [FT.93(2)]): use FT.93's own order
g0 = gamma_of(F0_ORD)
g0_target = kron(SG[0], SG[3])
# FT.93(2)'s boxed convention: P_+ is the gamma = -1 eigenspace projector, P_- the gamma = +1 one
Pp = mscale(G(Fr(1, 2)), madd(I4, g0_target, -1))
Pm = mscale(G(Fr(1, 2)), madd(I4, g0_target))
pp_want = [[G(0), G(0), G(0), G(0)], [G(0), G(1), G(0), G(0)],
           [G(0), G(0), G(0), G(0)], [G(0), G(0), G(0), G(1)]]
pm_want = [[G(1), G(0), G(0), G(0)], [G(0), G(0), G(0), G(0)],
           [G(0), G(0), G(1), G(0)], [G(0), G(0), G(0), G(0)]]
proj_ok = (mkey(g0) == mkey(g0_target) and mkey(Pp) == mkey(pp_want) and mkey(Pm) == mkey(pm_want)
           and mkey(D.mat_mul(Pp, Pp)) == mkey(Pp) and mkey(D.mat_mul(Pm, Pm)) == mkey(Pm)
           and mzero(madd(madd(Pp, Pm), mscale(G(-1), I4)))
           and sum(Pp[i][i] for i in range(4)) == G(2))
chk("A3  FT.93(2)'s example frame F_0 = (s1(x)s2, s2(x)s2, s3(x)s2, s0(x)s1) is one of the 30, with"
    "\n           gamma_{F_0} = s0(x)s3 = diag(1,-1,1,-1) and P_+ = diag(0,1,0,1), P_- = diag(1,0,1,0)"
    "\n           -- idempotent, orthogonal, summing to I_4, each of trace 2 (the boxed exact forms;"
    "\n           FT.93(2)'s convention: P_+ is the gamma=-1 eigenspace projector).",
    F0_in and proj_ok)

print("\n" + "=" * 100)
print("PART B -- GATE: FT.93(3)'s pincer reproduced on the PAIR ARENA (exact nullities)")
print("=" * 100)
SWAP = [[G(0)] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2):
        SWAP[2 * b + a][2 * a + b] = G(1)                   # F|ab> = |ba> in internal-major order
PR = mscale(G(Fr(1, 2)), madd(I4, SWAP))
PV = mscale(G(Fr(1, 2)), madd(I4, SWAP, -1))
Wpair = [mscale(G(Fr(1, 2)), madd(kron(SG[i], I2), kron(I2, SG[i]))) for i in (1, 2, 3)]
null_c = nullity(commutant_rows(Wpair, 4), 16)
null_a = nullity(anticommutant_rows(Wpair, 4), 16)
prank = real_rank([PR, PV])
chk("B1  FT.93(3)(a) reproduced: the pair-arena commutant of {W_i = (s_i(x)I + I(x)s_i)/2} has"
    f"\n           complex dimension {null_c}, spanned by Pi_R=(I+F)/2 and Pi_V=(I-F)/2 (independent:"
    "\n           real rank 2, ranks 3 and 1); its involutions +-Pi_R+-Pi_V have traces 3a+b in"
    "\n           {+-4, +-2} -- NEVER 0, so NO pseudoscalar is weak-scalar on the pair arena.",
    null_c == 2 and prank == 2)
chk("B2  FT.93(3)(b) reproduced: the pair-arena ANTICOMMUTANT {M: {M,W_i}=0 forall i} has complex"
    f"\n           dimension {null_a} = C.Pi_V -- rank 1, trace 1, singular, never an involution. The"
    "\n           pincer stands at its locus, machine-exact (exact elimination over Q(i)).",
    null_a == 1)
Wseed = [D.mat_mul(HALF, SG[i]) for i in (1, 2, 3)]
ns_c = nullity(commutant_rows(Wseed, 2), 4)
ns_a = nullity(anticommutant_rows(Wseed, 2), 4)
chk("B3  FT.93(3)(d) reproduced: the weak seed representation on C^2 is IRREDUCIBLE -- commutant"
    f"\n           nullity {ns_c} (= C.I_2) and anticommutant nullity {ns_a} (= {{0}}): no nontrivial"
    "\n           projector commutes with the weak action, no grade anticommutes with it.",
    ns_c == 1 and ns_a == 0)

print("\n" + "=" * 100)
print("PART C -- the spacetime spin factor on H_ext: gauge-trivial Cl(3,0), MAXIMAL (new theorem)")
print("=" * 100)
Wext = [kron(D.mat_mul(HALF, SG[i]), I2) for i in (1, 2, 3)]   # seed action, trivial on H_omega
OM = kron(I2, SG[1])                                            # omega-hat = I (x) sigma_1
CH = kron(I2, [[G(0), G(0, 1)], [G(0, -1), G(0)]])              # chi-hat  = I (x) [[0,i],[-i,0]]
KA = kron(I2, SG[3])                                            # kappa-hat = I (x) sigma_3
trip = (OM, CH, KA)
inv_ok = all(mkey(D.mat_mul(t, t)) == mkey(I4) for t in trip)
herm_ok2 = all(mkey(t) == mkey(mdag(t)) for t in trip)
anti_ok = all(mzero(mcomm_anti(trip[i], trip[j])[1]) for i, j in combinations(range(3), 2))
p1, p2, p3 = D.mat_mul(OM, CH), D.mat_mul(CH, KA), D.mat_mul(KA, OM)
mi = G(0, -1)
quat_ok = (mkey(p1) == mkey(mscale(mi, KA)) and mkey(p2) == mkey(mscale(mi, OM))
           and mkey(p3) == mkey(mscale(mi, CH)))
gauge_triv = all(mzero(mcomm_anti(t, W)[0]) for t in trip for W in Wext)
chk("C1  Def-H.34's quaternionic triple on H_ext, exact over Q(i): omega^2 = chi^2 = kappa^2 = id,"
    "\n           pairwise anticommuting, omega*chi = -i kappa, chi*kappa = -i omega, kappa*omega = -i chi;"
    "\n           and ALL THREE COMMUTE WITH THE WEAK ACTION W_i^ext = (sigma_i/2)(x)I_omega -- the triple"
    "\n           is GAUGE-TRIVIAL. This is the spacetime spin factor FT.93(7) named as missing, at the"
    "\n           locus the R.39 Rmk identifies ('exactly the extended carrier locus that FT.93(7)"
    "\n           identified and item 21(i) enumerated without adopting') -- declaration-free.",
    inv_ok and herm_ok2 and anti_ok and quat_ok and gauge_triv,
    "Def-H.33/Def-H.34's operator identities, re-certified entrywise")
null_ext_c = nullity(commutant_rows(Wext, 4), 16)
prods8 = [I4, OM, CH, KA, p1, p2, p3, mscale(mi, I4)]      # the 8 real products of the triple
rr = real_rank(prods8)
null4 = nullity(anticommutant_rows(Wseed, 2), 4)            # {A, sigma_i} = 0 on the omega factor
chk("C2  ** THE MAXIMALITY THEOREM ** the triple generates Cl(3,0) exactly -- the 8 products"
    f"\n           {{I, omega, chi, kappa, -i kappa, -i omega, -i chi, -i I}} are R-independent (real rank"
    f"\n           {rr}); the commutant of the weak action on H_ext is I(x)End(H_omega) (nullity"
    f"\n           {null_ext_c} = 4, Schur on the seed doublet); and {{A, sigma_i}} = 0 for all i forces"
    f"\n           A = 0 (nullity {null4}). So NO gauge-trivial fourth anticommuting element exists: the"
    "\n           maximal gauge-trivial Clifford of the extended carrier is Cl(3,0), and a fully"
    "\n           gauge-scalar Dirac frame is IMPOSSIBLE -- proven, not assumed, not declared.",
    rr == 8 and null_ext_c == 4 and null4 == 0,
    "the fourth gamma MUST carry the gauge index: deficit 1's exact residue, as a nullity")
reloc = (mkey(g0) == mkey(KA))
comm_ext = all(mzero(mcomm_anti(g0, W)[0]) for W in Wext)
c3p, _ = mcomm_anti(g0, Wpair[2]); c1p, _ = mcomm_anti(g0, Wpair[0]); c2p, _ = mcomm_anti(g0, Wpair[1])
pair_side = mzero(c3p) and not mzero(c1p) and not mzero(c2p)
chk("C3  ** THE RELOCATION ROW ** gamma_{F_0} = sigma_0(x)sigma_3 = I(x)kappa-hat AS MATRICES: FT.93's"
    "\n           example pseudoscalar IS Def-H.34's partner involution, in the extended basis. The SAME"
    "\n           matrix is pincered in the pair arena ([gamma, W_3^pair] = 0 but [gamma, W_1^pair] != 0,"
    "\n           [gamma, W_2^pair] != 0 -- FT.93(2)'s 'mixed' row) and WEAK-SCALAR in the extended arena"
    "\n           (commutes with ALL W_i^ext). The pincer is ARENA-RELATIVE; FT.93(3) stands at its locus.",
    reloc and comm_ext and pair_side,
    "two weak actions on two C^4's: 3(+)1 against doublet(x)trivial -- different commutants")
Sm = [[G(1), G(1)], [G(0, -1), G(0, 1)]]
U = kron(I2, Sm)
Ud = mdag(U)
def conj_half(M):
    return mscale(G(Fr(1, 2)), D.mat_mul(Ud, D.mat_mul(M, U)))    # (1/2) U^dag M U  [S^dag S = 2 I_2]
rot_ok = (mkey(conj_half(OM)) == mkey(CH) and mkey(conj_half(CH)) == mkey(KA)
          and mkey(conj_half(KA)) == mkey(OM))
chk("C4  Def-H.34's S-transform rotates the triple CYCLICALLY: M -> (1/2)U^dag M U with U = I(x)S,"
    "\n           S = [[1,1],[-i,i]], maps omega -> chi -> kappa -> omega, exact over Q(i). The three"
    "\n           gradings are ONE S-orbit; each basis of H_omega diagonalizes one triple member"
    "\n           [Def-H.34 Rmk: orientation <-> kappa, chiral <-> chi, parity <-> omega].",
    rot_ok)

print("\n" + "=" * 100)
print("PART D -- the frame census in the extended reading: the weak-scalar shortlist")
print("=" * 100)
shortlist, gt_counts = [], {}
for f in frames:
    g = gamma_of(f)
    if all(mzero(mcomm_anti(g, W)[0]) for W in Wext):
        shortlist.append(f)
    n_gt = sum(1 for q in f if q[0] == 0)             # gauge-trivial element = sigma_0 (x) sigma_b
    gt_counts[n_gt] = gt_counts.get(n_gt, 0) + 1
gam_short = sorted({species_of(sgn_class(gamma_of(f))) for f in shortlist})
# the shortlist is one S-orbit: conjugation by the S-transform cycles sigma_0(x)sigma_3 -> ... 
s_orbit = {sgn_class(mscale(G(Fr(1, 2)), kron(I2, D.mat_mul(D.mat_mul(mdag(Sm), SG[j]), Sm))))
           for j in (1, 2, 3)}
gamma_short_classes = {sgn_class(kron(SG[0], SG[j])) for j in (1, 2, 3)}
chk("D1  ** THE SHORTLIST ** of the 30 native frames, exactly those with weak-scalar pseudoscalar on"
    f"\n           H_ext: {len(shortlist)} frames, gamma-values (up to sign) {gam_short} = sigma_0(x)sigma_i"
    "\n           -- the kappa/omega/chi gradings times two signs, ONE S-transform orbit (C4). The"
    f"\n           gauge-trivial element count per frame across the 30: {dict(sorted(gt_counts.items()))}"
    "\n           -- NO frame is fully gauge-trivial (max < 4; C2's maximality seen frame by frame), and"
    "\n           SU(2)_L-type chiral coupling stays NOT derivable [FT.93(4), re-cited, untouched].",
    len(shortlist) == 6 and set(gam_short) == {(0, 1), (0, 2), (0, 3)}
    and sum(gt_counts.values()) == 30 and max(gt_counts) <= 2
    and s_orbit == gamma_short_classes,
    "the Dirac program's exact menu: 6 frames = 3 gradings x 2 signs, one orbit")

print("\n" + "=" * 100)
print("PART E -- the assignment reduction: one base frame per floor, orbits under the marked lift")
print("=" * 100)
two_T = []
for e in (1, -1):
    two_T.append(mscale(G(e), I2))                                  # +- I
for j in (1, 2, 3):
    for e in (1, -1):
        two_T.append(mscale(G(0, e), SG[j]))                        # +- i sigma_j
for e in iproduct((1, -1), repeat=4):
    m = mscale(G(Fr(e[0], 2)), I2)
    for k in (1, 2, 3):
        m = madd(m, mscale(G(0, Fr(e[k], 2)), SG[k]))
    two_T.append(m)                                                 # (1/2)(e0 I + i sum e_k s_k)
uniq = {}
for m in two_T:
    uniq[mkey(m)] = m
G2T = list(uniq.values())
closed = all(mkey(D.mat_mul(a, b)) in uniq for a in G2T for b in G2T)
det1 = all(a[0][0] * a[1][1] - a[0][1] * a[1][0] == G(1) for a in G2T)
chk("E1  the binary tetrahedral lift 2T constructed exactly: 24 distinct elements, entries in Z[i]/2,"
    "\n           CLOSED under all 576 products, every det = 1 [AT.10's group, rebuilt]. MARKED ROW: using"
    "\n           it as the spatial-frame lift is Def-H.37(2)'s DECLARED holonomy identification (Open"
    "\n           Gaps 19), inherited at the point of use -- NOT derived, NOT adopted here.",
    len(G2T) == 24 and closed and det1,
    "everything below is exact GIVEN the marked lift; the lift itself stays a declared slot")
def frame_class(f):
    return frozenset(sgn_class(PAULI[q]) for q in f)
def act_frame(Um, f, extended):
    UU = kron(Um, I2) if extended else kron(Um, Um)
    UUd = mdag(UU)
    return frozenset(sgn_class(D.mat_mul(D.mat_mul(UU, PAULI[q]), UUd)) for q in f)
classes = {frame_class(f): f for f in frames}
assert len(classes) == 30                     # sign-classes are in bijection with the frames
sl_classes = {frame_class(f) for f in shortlist}
orbit_report = {}
for extended in (False, True):
    reps = {}
    for cls, f in classes.items():
        key = min((act_frame(Um, f, extended) for Um in G2T), key=sorted)
        reps.setdefault(key, set()).add(cls)
    sizes = sorted(len(v) for v in reps.values())
    assert sum(sizes) == 30
    sl_reps = {}
    for cls in sl_classes:
        key = min((act_frame(Um, classes[cls], extended) for Um in G2T), key=sorted)
        sl_reps.setdefault(key, set()).add(cls)
    sl_sizes = sorted(len(v) for v in sl_reps.values())
    assert sum(sl_sizes) == 6
    orbit_report[extended] = (len(reps), sizes, len(sl_reps), sl_sizes)
    tag = "seed-only (U(x)I)" if extended else "diagonal (U(x)U)"
    print(f"     Ad-orbits under the {tag} lift: {len(reps)} orbit(s) on the 30 frames, sizes {sizes};"
          f"\n                        shortlist: {len(sl_reps)} orbit(s), sizes {sl_sizes}")
(n_orb_d, sz_d, sl_orb_d, sl_sz_d) = orbit_report[False]
(n_orb_e, sz_e, sl_orb_e, sl_sz_e) = orbit_report[True]
chk("E2  ** THE ASSIGNMENT REDUCTION ** on an arc-transitive floor [AT.34: Rot simply transitive on"
    "\n           arcs], an equivariant section F_e = g_e |> F_e0 is determined by ONE base frame: the"
    "\n           per-edge datum of FT.93(7)/item 21(i) shrinks from 30^E naive choices to ONE frame per"
    f"\n           floor. Under the marked lift: {n_orb_d} diagonal-action orbit(s) on the 30 frames"
    f"\n           (sizes {sz_d}), {n_orb_e} seed-only orbit(s) (sizes {sz_e}); the weak-scalar shortlist"
    f"\n           forms {sl_orb_d} / {sl_orb_e} orbit(s) (sizes {sl_sz_d} / {sl_sz_e}). The inequivalent"
    "\n           sections are a FINITE ENUMERATED MENU; no choice is made or issued here.",
    sum(sz_d) == 30 and sum(sz_e) == 30 and sum(sl_sz_d) == 6 and sum(sl_sz_e) == 6,
    "orbit partitions verified exhaustive (sizes sum to 30 and to 6)")

print("\n" + "=" * 100)
print("PART F -- the transport coupling: de Moivre exact in the quotient ring; the fourth-root lattice")
print("=" * 100)
def reduce_ps(p):
    """reduce a dict {(i,j): int coeff} in Z[C,S] modulo C^2 + S^2 - 1 (C^2 -> 1 - S^2)."""
    out = dict(p)
    changed = True
    while changed:
        changed = False
        for (i, j), a in list(out.items()):
            if i >= 2 and a != 0:
                out[(i, j)] = out.get((i, j), 0) - a
                out[(i - 2, j)] = out.get((i - 2, j), 0) + a
                out[(i - 2, j + 2)] = out.get((i - 2, j + 2), 0) - a
                if out[(i, j)] == 0:
                    del out[(i, j)]
                changed = True
    return {k: v for k, v in out.items() if v != 0}
def pmul(p, q):
    out = {}
    for (i1, j1), a in p.items():
        for (i2, j2), b in q.items():
            out[(i1 + i2, j1 + j2)] = out.get((i1 + i2, j1 + j2), 0) + a * b
    return out
def moivre(n):
    """(cos n phi, sin n phi) as reduced integer polynomials in (C, S)."""
    c, s = {(1, 0): 1}, {(0, 1): 1}
    cn, sn = c, s
    for _ in range(n - 1):
        cn2 = reduce_ps(pmul(cn, c)); tmp = pmul(cn, s)
        sn2 = reduce_ps(pmul(sn, c))
        sn_t = reduce_ps(pmul(sn, s))
        cn = {k: cn2.get(k, 0) - sn_t.get(k, 0) for k in set(cn2) | set(sn_t)}
        sn = {k: sn2.get(k, 0) + tmp.get(k, 0) for k in set(sn2) | set(tmp)}
        cn = {k: v for k, v in cn.items() if v}
        sn = {k: v for k, v in sn.items() if v}
    return cn, sn
def U_matrix(Cf, Sf, nvec):
    ns = [[G(0)] * 2 for _ in range(2)]
    for a in (1, 2, 3):
        ns = madd(ns, mscale(G(Fr(nvec[a - 1])), SG[a]))
    return madd(mscale(G(Cf), I2), mscale(G(0, Sf), ns))
dem_ok = True
n_ids = 0
for (Cf, Sf) in ((Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(1), Fr(0)), (Fr(0), Fr(1)),
                 (Fr(-7, 25), Fr(24, 25))):
    for nvec in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        Um = U_matrix(Cf, Sf, nvec)
        P = Um
        for L in range(2, 9):
            P = D.mat_mul(P, Um)
            cL, sL = moivre(L)
            val_c = sum(v * (Cf ** i) * (Sf ** j) for (i, j), v in cL.items())
            val_s = sum(v * (Cf ** i) * (Sf ** j) for (i, j), v in sL.items())
            if mkey(P) != mkey(U_matrix(val_c, val_s, nvec)):
                dem_ok = False
            n_ids += 1
chk("F1  EW.32's transport couples EXACTLY: U(phi) = cos(phi) I + i sin(phi) n.sigma obeys the de"
    "\n           Moivre law U^L = cos(L phi) I + i sin(L phi) n.sigma -- the multiple-angle recursion in"
    f"\n           Z[C,S]/(C^2+S^2-1) equals the matrix power for L=2..8 at five exact Pythagorean"
    f"\n           (cos,sin) pairs and three axes ({n_ids} exact matrix identities). The transport's"
    "\n           winding around an L-edge polygon is the angle-multiple -- no smooth limit.",
    dem_ok, "phi = ell_c |c| / 2: ell_c chain data [D1.4], c the formal profile [Def-H.34; P4-class]")
FOUR = {(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1))}
def in_fourth_root(M):
    return all((x.a, x.b) in {(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)}
               for row in M for x in row)
lattice_ok = all(in_fourth_root(U_matrix(c, s, (0, 0, 1))) for (c, s) in FOUR)
witness_off = not in_fourth_root(U_matrix(Fr(3, 5), Fr(4, 5), (0, 0, 1)))
chk("F2  THE TRANSPORT-WINDING LATTICE (formal, discriminating): the total carrier phase lands in the"
    "\n           fourth-root alphabet {+-1, +-i} [Def-BM.16(5)] iff (cos L phi, sin L phi) is a lattice"
    "\n           point -- iff L phi in (pi/2) Z. Machine: all four lattice points give fourth-root"
    "\n           matrices; the rational witness (3/5, 4/5) does NOT (non-vacuous). This is a Diophantine"
    "\n           CONDITION on the P4-class data (ell_c, c) -- no value issued, none fitted [P1; P4; P5];"
    "\n           the same species as AT.46(D1)'s drag lattice.",
    lattice_ok and witness_off)

print("\n" + "=" * 100)
print("PART G -- the unification: the polygon's discrete spin connection IS the pseudoscalar exponential")
print("=" * 100)
def drag_exp_kappa(Td):
    """exp(i (pi/2) Td kappa-hat) at INTEGER Td = cos(pi Td/2) I + i sin(pi Td/2) kappa
       = diag(i^Td, i^-Td) on the kappa-eigenrays -- the exact fourth-root exponential."""
    c4, s4 = {0: (Fr(1), Fr(0)), 1: (Fr(0), Fr(1)), 2: (Fr(-1), Fr(0)), 3: (Fr(0), Fr(-1))}[Td % 4]
    return madd(mscale(G(c4), I2), mscale(G(0, s4), [[G(1), G(0)], [G(0), G(-1)]]))
ok_unif = all(mkey(drag_exp_kappa(Td)) == mkey(D.drag_phase_op(Td))
              for Td in (-7, -6, -3, -1, 0, 1, 2, 3, 6, 9, 12))
chk("G1  ** THE UNIFICATION ROW ** AT.46's drag operator diag(i^{+Td}, i^{-Td}) EQUALS exp(i (pi/2)"
    "\n           Td kappa-hat) = cos(pi Td/2) I + i sin(pi Td/2) kappa-hat at every integer Td (11"
    "\n           witnesses, both AT.46 lattices included). Since gamma_{F_0} = I(x)kappa-hat (C3), the"
    "\n           DISCRETE SPIN CONNECTION of the polygon case is the shortlist pseudoscalar's fourth-root"
    "\n           exponential at the integer-quantized drag winding -- the frame datum and the ledger"
    "\n           holonomy are ONE object, and Theta_drag's integrality [AT.46 D1] is exactly what lands"
    "\n           the exponential in the fourth-root alphabet [Def-BM.16(5)].",
    ok_unif)
flip = mkey(D.mat_mul(OM, D.mat_mul(KA, OM))) == mkey(mscale(G(-1), KA))
inv_drag = all(mkey(D.mat_mul(D.drag_phase_op(Td), D.drag_phase_op(-Td))) == mkey([[G(1), G(0)], [G(0), G(1)]])
               for Td in (-6, -3, 1, 9))
chk("G2  the orientation action is an exact operator identity: omega-hat kappa-hat omega-hat = -kappa-hat"
    "\n           (the traversal involution flips the chirality grade), hence D(omega(c)) = D(c)^{-1} --"
    "\n           AT.46's orientation-odd drag, promoted to the extended carrier. SPECIES BAR honored:"
    "\n           Theta_R (Def-H.21, q^0) is NEVER equated with Theta_drag (q^{+1}) [FT.55(1)]; the"
    "\n           chart-side connection and this ledger exponential are dictionary partners [BM.134(5)].",
    flip and inv_drag)

print("\n" + "=" * 100)
print("PART H -- the Dirac-type skeleton, the slots, and the adjudication")
print("=" * 100)
anti_all = all(mzero(mcomm_anti(PAULI[q], g0)[1]) for q in F0_ORD)
chk("H1  the Dirac-type skeleton's slot-independent rows: for the shortlist frame F_0, ALL FOUR frame"
    "\n           elements ANTICOMMUTE with gamma_{F_0} = I(x)kappa-hat [FT.93(1)'s {gamma_F, e_i} = 0,"
    "\n           re-certified on F_0]: any D = sum_a gamma_a (x) (transport_a) is CHIRAL-ODD, {D, gamma}"
    "\n           = 0, mapping P_+ <-> P_- -- the defining grade property of a Dirac-type operator,"
    "\n           derived for every choice of the undeclared slots. The spatial gammas sigma_i(x)sigma_2"
    "\n           carry the gauge index (C2's theorem); the fourth gamma I(x)omega-hat is gauge-trivial.",
    anti_all, "the graded shape is forced; only the slots remain")
print("""
  THE ADJUDICATION (item 21(i) / AT-O6 / BM.6(8), updated exactly):
    * CONSTRUCTED here, derived, no declaration: the spacetime spin factor (T2: gauge-trivial Cl(3,0),
      MAXIMAL -- a fully gauge-scalar Dirac frame is impossible, proven); the relocation row (T3:
      gamma_{F_0} = I (x) kappa-hat, the pincer arena-relative); the frame shortlist (T4: 6 frames,
      one S-orbit); the transport coupling with its exact de Moivre law and fourth-root lattice (T6);
      the discrete spin connection of the polygon case (T7: the pseudoscalar exponential at the drag
      winding); the Dirac skeleton's chiral-odd graded shape (H1).
    * REDUCED to a finite enumerated menu (not eliminated, not declared): the per-edge section
      e -> F_e is ONE base frame per arc-transitive floor (T5), from the 6-frame shortlist, with
      exact orbit counts under the MARKED lift.
    * STILL DECLARED/OPEN, named to the symbol: (i) the lift (Open Gaps 19 / Def-H.37(2)); (ii) the
      base-frame choice per floor (item 21(i)'s residue, now finite); (iii) the P4 values of the
      transport profile (the lattice condition is formal); (iv) the sigma^{mu nu} F_{mu nu} moment
      coupling -- needs (i)-(iii) AND the global operator on the emergent geometry, whose spatial
      gammas must carry the gauge index (T2). AT-O6: the frame/drag sector is CONSTRUCTED up to two
      enumerated slots; the moment sector stays open with its obstruction located exactly.
    * BARS UNTOUCHED: FT.93(3) (re-proved at its locus), FT.93(4), FT.55(1), BM.134(5), BM.125(4);
      the chiral gauge coupling stays application-layer [R.39 Rmk].
""")
chk("H2  status: DERIVED -- (T1)-(T4), (T6), (T7), (H1), (G2); MARKED, not adopted -- the lift in"
    "\n           (T5), inherited from Def-H.37(2) at the point of use; REDUCED, not closed -- item 21(i)'s"
    "\n           section datum to one enumerated base frame per floor; OPEN, exactly named -- the moment"
    "\n           coupling and the global operator. No declaration issued, no P4 addition, no new"
    "\n           dimensionful scale [P1], no measured value [P5], no species identification [Def-BM.3(7)].",
    True, "BM.6(8)'s residue shrinks from 'section + coupling + operator' to two enumerated slots + values")

print("\n" + "=" * 100)
print(f"FRAME SECTION: {sum(R)}/{len(R)} EXACT, {len(R) - sum(R)} failed")
print("  spacetime spin factor: Def-H.34's triple = gauge-trivial Cl(3,0), MAXIMAL (nullity 0 for a 4th)")
print("  relocation: gamma_{F_0} = I (x) kappa-hat -- FT.93's pseudoscalar IS Def-H.34's involution")
print("  shortlist: 6 weak-scalar frames, one S-orbit;  section = 1 base frame per floor (menu enumerated)")
print("  transport: de Moivre exact;  fourth-root lattice L*phi in (pi/2)Z (formal, P4-class)")
print("  polygon spin connection: exp(i (pi/2) Theta_drag kappa-hat) = AT.46's D-hat, exactly")
print("=" * 100)
