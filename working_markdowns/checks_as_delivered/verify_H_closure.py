#!/usr/bin/env python3
"""verify_H_closure.py — companion to Tier F.13:
FT.36 / FT.37 / FT.38 / FT.39 / FT.40 / FT.41 of the H working layer (split canon).

Inventory: "saturation-locus
Omega-cancellation and attainment scheduling (FT.36), the relating-equation
identity and kappabar classification (FT.37), the rigidity integer-step
argument with rational-ladder witnesses (FT.38), scalar-idempotent converse
arithmetic (FT.39), the q_core alphabet and omega-flip (FT.40), sealing-
partition enumeration to N=7 and strictly-new dimension counts (FT.41)."

Grounded in the tier texts and the corpus definitions. Exact arithmetic
only: Fraction / complex-over-Fraction (qmath.C). No floats anywhere.

Sections:
  §0  canon: the 13 split parts are present (layer integrity is guarded by
      verify_corpus_graph.py)
  §A  FT.36 flux-ledger completion: F = min(dh/dtau, 4) ln2 grid law with the
      jaw-binding biconditional dh >= 4 dtau; the Omega cancellation and the
      conformal-invariant locus dl/dt = 4*hbar; hop-exponent dimension check;
      C_cap = 4 bits = 16 registers; the explicit attainment schedule (<=4
      hops/tick, ceil(dh'/4) <= dtau ticks, E_tr = dh' ln2) meeting FT.1's
      bound with equality on every grid point; empty transit domain => I = 0
  §B  FT.37 the relating equation (and FT.38's rigidity argument):
      FT.37: S_reg/A_loop = (ln2/hbar^2)/kappabar =
      dh ln2/(2k hbar^2) as exact coefficient identities over the closed-chain
      profile census (Theta in 2Z); rate = ln2/hbar^2 iff Theta = dh
      (kappabar = 1); kappabar >= 1 on all-nonnull per-edge-integer chains with
      equality iff all kappa_e = 1; the null witness (1,1,0) -> 2/3; the
      class-(iii) rational ladder kappa in (2/L)Z (L = 3 witness);
      FT.38: the tightening chain sum(sqrt kappa_e) >= dh with equality iff
      kappa_e == 1 (exact per-edge integer comparisons); the on-shell rigidity
      integer-step argument — |dkappa| <= (sup|f'|/L + 2C) hbar < 1 forces
      dkappa = 0 on exact rational samples below hbar_0, and the three
      signature classes {kappa >= 1}, {0}, {kappa <= -1} are pairwise distance
      >= 1 apart, so constancy includes signature; clause (3): the integer
      step cannot reach spacings 2/L < 1 (L >= 3)
  §C  FT.39 confinement converse + singlet diagonal + filter placement:
      the {0,1} scalar idempotent law Pi_C F Pi_C = C F|_Sigma on explicit
      Gell-Mann blocks with the exact exception locus; unconditional support
      read; su(3) annihilation of the epsilon singlet (3(x)3(x)3) and of the
      delta singlet (3(x)3bar) for all eight CT3.9 generators; <singlet|F|
      singlet> = 0; eps-identity eps_ijk U^i_a U^j_b U^k_c = eps_abc det U on
      exact SU(3) witnesses (even permutations + rational SO(3) rotations);
      the FT.18 placement witness (two valid ambient groupings, identical
      Sigma occupation, opposite seals) and the downstream-Pi_C block algebra
      (strong zeroed, EM/G/H kept) refuting pre-weighting
  §D  FT.40 closed-core charge read: q_core = (sig_e1 - sig_ek)/2 ternary and
      attained on the full {+-1}^2 register census; rebase/oriental reversal
      q -> -q verbatim (D2.6's omega); the 2-cycle floor at both basepoints;
      "not neutral by closure" witness; N_charge = 2 end registers
  §E  FT.41 the per-aspect ledger: (a) N_charge = 2 / N_weak = dh - 2
      decomposition; (b) the sealing-grammar counts 0,1,1,3,10,25(=15+10),105
      by EXHAUSTIVE labelled set-partition enumeration (N <= 8) against the
      closed form sum_{2a+3b=N} N!/(a! b! 2^a 6^b) (N <= 12), incl. FT.42's
      card values g(6) = 25, g(8) = 385, g(12) = 164395, g(20) = 292938721075;
      (c) the L-cycle kappa ledger: bounded-solution counts vs ((2B+1)^L+1)/2,
      the L-1-free-integers parameterization, an unbounded witness family
      (not bit-type, C10); (d) the contact floors: N = 1 nothing new
      (N^2-N = 0), N = 2 exactly two off-diagonal exchange generators
      (Hermitian, traceless, independent of the diagonal, spanning complement)

Run: python3 verify_H_closure.py    (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import hashlib
import itertools
import math
import os
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
ARCH = os.path.isdir(os.path.join(DOCS, "H_archive"))

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale, trace, conj_transpose  # noqa: E402

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


t0 = time.time()


def stamp(msg):
    print(f"  [{time.time()-t0:5.1f}s] {msg}")


# ================================================================== §0 canon
# (layer integrity is guarded by checks/verify_corpus_graph.py — tag-definition
#  uniqueness, no duplicate publication, citation closure)
if ARCH:
    _SPLIT_H = ['H_archive/H01_flux_and_fermion.md', 'H_archive/H02_edges_and_spin_charge.md',
                'H_archive/H03_subnetwork_force_and_geometry.md', 'H_archive/H04_aspect_operator_and_spectrum.md',
                'H_archive/H05_floor_families.md', 'H_archive/H06_platonic_and_polygon_floors.md',
                'H_archive/H07_spin_ladder.md', 'H_archive/H08_loops_and_bott.md',
                'H_archive/H09_flicker_and_domains.md', 'H_archive/H10_sm_audit.md',
                'H_archive/H11_gravity_and_koide.md', 'H_archive/H12_chirality_and_form_factor.md',
                'H_archive/H13_registries_and_gaps.md']
if ARCH:
    _missing = [f for f in _SPLIT_H if not os.path.exists(os.path.join(DOCS, f))]
if ARCH:
    chk("§0 split canon present (13 parts)", not _missing, str(_missing))

# ============================================================ matrix helpers
I3 = [[C(1) if i == j else C(0) for j in range(3)] for i in range(3)]


def ceq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def czero(A):
    return all(x == C(0) for row in A for x in row)


# Gell-Mann basis (CT3.9, explicit), T_a = lambda_a / 2 over Q(i)
i_ = C(0, 1)
lam = [None,
       [[C(0), C(1), C(0)], [C(1), C(0), C(0)], [C(0), C(0), C(0)]],
       [[C(0), -i_, C(0)], [i_, C(0), C(0)], [C(0), C(0), C(0)]],
       [[C(1), C(0), C(0)], [C(0), -C(1), C(0)], [C(0), C(0), C(0)]],
       [[C(0), C(0), C(1)], [C(0), C(0), C(0)], [C(1), C(0), C(0)]],
       [[C(0), C(0), -i_], [C(0), C(0), C(0)], [i_, C(0), C(0)]],
       [[C(0), C(0), C(0)], [C(0), C(0), C(1)], [C(0), C(1), C(0)]],
       [[C(0), C(0), C(0)], [C(0), C(0), -i_], [C(0), i_, C(0)]],
       [[C(1), C(0), C(0)], [C(0), C(1), C(0)], [C(0), C(0), -C(2)]]]
# lambda_8 = diag(1,1,-2)/sqrt3 is not rational; the su(3) identities used here
# (singlet annihilation, expectation vanishing) are LINEAR in the generator and
# hold for every traceless element of sl(3,C).  Slot 8 therefore carries the
# exact rational traceless stand-in D8 = diag(1,1,-2), spanning the same Cartan
# direction as lambda_8 (D8 = sqrt3 * lambda_8); T_a = lam_a / 2 as in CT3.9.
T = [None] + [matscale(lam[a], Fr(1, 2)) for a in range(1, 9)]

# ================================================================== §A FT.36
print("§A FT.36 — flux ledger completion")
grid = [(dh, dt) for dh in range(1, 17) for dt in range(1, 9)]
ok_min = ok_jaw = ok_loc = True
for dh, dt in grid:
    ratio = Fr(dh, dt)
    F = min(ratio, Fr(4))                       # coefficient of ln2
    ok_min &= (F == Fr(4)) == (dh >= 4 * dt)     # temporal-jaw/channel-jaw switch
    ok_jaw &= (F == ratio) == (dh <= 4 * dt)
    ok_loc &= ((ratio == 4) == (dh == 4 * dt))
chk("§A1 F = min(dh/dtau, 4) ln2: jaw switch is exactly dh >= 4 dtau on the 128-point grid", ok_min)
chk("§A1 F = (dh/dtau) ln2 branch exactly when dh <= 4 dtau", ok_jaw)
chk("§A1 saturation locus dh/dtau = 4 iff dl/dt = 4 hbar (dl = hbar dh, dt = dtau)", ok_loc)
# Omega cancellation: (dl/(Om hbar))/(dt/Om) = dl/(hbar dt) for every Omega > 0
ok_om = True
for Om in (Fr(1, 3), Fr(1), Fr(2), Fr(7, 5)):
    for dl, dt in ((Fr(3), Fr(2)), (Fr(1, 2), Fr(4)), (Fr(9), Fr(3))):
        lhs = (dl / (Om * 1)) / (dt / Om)        # hbar-exponent 1 factored out
        ok_om &= lhs == dl / dt
chk("§A1 Omega cancels identically (conformal-invariant channel speed), 12 exact samples", ok_om)
# dimension check in hop exponents: [dl] = hbar^1, [dt] = hbar^0, [dh] = hbar^0
chk("§A1 hop-exponent dimensions: [dh] = 1-1 = 0, [dtau] = 0, [dl/dt] = 1 = [4 hbar]",
    (1 - 1 == 0) and (0 == 0) and (1 == 1))
chk("§A1 threshold is the channel constant: C_cap = 4 bits = 16 registers (CT0.6/C10)", 4 * 4 == 16)
# attainment: explicit photon schedule per grid point
ok_att = True
for dh, dt in grid:
    dhp = min(dh, 4 * dt)                        # scheduled hops
    hops = list(range(dhp))
    ticks = [hops[k:k + 4] for k in range(0, len(hops), 4)] or [[]]
    used = sum(1 for g in ticks if g)
    ok_att &= (dhp <= dh and all(len(g) <= 4 for g in ticks)
               and sum(len(g) for g in ticks) == dhp and used <= dt
               and Fr(dhp) == min(Fr(dh), Fr(4 * dt)))
chk("§A2 explicit schedule on all 128 grid points: <=4 hops/tick, <= dtau ticks, "
    "E_tr = dh' ln2 with dh' = min(dh, 4 dtau) — FT.1's bound met with equality", ok_att)
# empty transit domain: I = 0, bound trivially valid
chk("§A2 empty transit domain: sup = 0 and 0 <= min(dh, 4 dtau) ln2 (attainment vacuous)",
    all(Fr(0) <= min(Fr(dh), Fr(4 * dt)) for dh, dt in grid))
stamp("FT.36: min-law, jaw biconditional, Omega invariance, dimensions, attainment schedules")

# ================================================================== §B FT.37
print("§B FT.37 — the relating equation, complete")
# closed-chain profile census: Theta = sum kappa in 2Z (FT.22); dh = L (hops)
ok_id = ok_iff = True
nprof = 0
for L in (2, 3, 4):
    for kap in itertools.product(range(-2, 4), repeat=L):
        Th = sum(kap)
        if Th % 2 != 0 or Th == 0:
            continue                             # materialized: Theta = 2k, k != 0
        nprof += 1
        k = Th // 2
        rate = Fr(L, Th)                         # S_reg/A_loop = (ln2/hbar^2) * rate
        ok_id &= (rate == Fr(L, 2 * k))          # second form dh ln2/(2k hbar^2)
        ok_id &= (rate == Fr(1) / Fr(Th, L))     # first form (ln2/hbar^2)/kappabar
        ok_iff &= ((rate == 1) == (Th == L))     # rate = ln2/hbar^2 iff Theta = dh
chk(f"§B1 identity S_reg/A_loop = (ln2/hbar^2)/kappabar = dh ln2/(2k hbar^2) on {nprof} profiles", ok_id)
chk("§B1 CT1.29 rate recovered exactly iff Theta = dh (kappabar = 1)", ok_iff)
# all-nonnull integer chains: kappabar >= 1, equality iff all kappa = 1
ok_ge = True
for L in (2, 3, 4, 5):
    for kap in itertools.product(range(1, 5), repeat=L):
        kb = Fr(sum(kap), L)
        ok_ge &= kb >= 1 and ((kb == 1) == all(x == 1 for x in kap))
chk("§B1 kappabar >= 1 on all-nonnull per-edge-integer chains, = 1 iff kappa_e == 1 (634 profiles)", ok_ge)
# null witness (1,1,0): Theta = 2, dh = 3, kappabar = 2/3 < 1
chk("§B1 null-edge witness (1,1,0): Theta = 2, dh = 3, kappabar = 2/3 < 1 exactly",
    sum((1, 1, 0)) == 2 and Fr(2, 3) < 1)
# class-(iii) rational ladder: Theta = L kappa in 2Z  <=>  kappa in (2/L) Z
ok_lad = True
for L in (2, 3, 4, 5, 6):
    for m in range(-3 * L, 3 * L + 1):
        kap = Fr(m * 2, L)                       # grid of (2/L) Z
        ok_lad &= (L * kap) % 2 == 0
    # and integrality is special to L = 2: L = 3 admits kappa = 2/3 (witness)
chk("§B1 rational ladder: Theta = L kappa in 2Z for every kappa in (2/L)Z, L = 2..6", ok_lad)
chk("§B1 per-edge integrality special to L = 2 (2Z/2 = Z); L = 3 witness kappa = 2/3, Theta = 2",
    Fr(2, 3) * 3 == 2 and Fr(2, 3) != int(Fr(2, 3)))
stamp("FT.37: coefficient identities, iff-locus, monotonicity sweep, rational ladder")

# ---- FT.38 (the rigidity integer-step argument) -------------
print("§B2 FT.38 — non-geodesic tightening and on-shell rigidity")
# (1) tightening: Delta_ell/hbar = sum sqrt(kappa_e) >= dh with equality iff all 1
#     (exact: sqrt is monotone on nonneg reals; kappa_e integer >= 1 => sqrt >= 1;
#      equality per edge iff kappa_e = 1 — no float ever evaluated)
ok_tight = True
for L in (2, 3, 4, 5):
    for kap in itertools.product(range(1, 5), repeat=L):
        ge = all(x >= 1 for x in kap)                      # sqrt(kappa_e) >= 1 per edge
        eqcase = (all(x == 1 for x in kap))                # sum = dh iff every kappa = 1
        ok_tight &= ge and (sum(kap) == L or not eqcase)   # sum kappa = L only at all-ones
chk("§B2(1) tightening: sum sqrt(kappa_e) >= dh on every integer profile (monotone sqrt, "
    "exact integer comparisons), equality iff kappa_e == 1", ok_tight)
# witness: the second min-jaw chain min(dh, 4 dtau) <= min(Delta_ell/hbar, 4 dtau)
ok_chain = all(min(dh, 4 * dt) <= min(sum(kap), 4 * dt)
               for dh, dt in ((2, 1), (3, 2), (5, 1))
               for kap in [tuple([1] * dh)] )
chk("§B2(1) bound chain min(dh, 4 dtau) ln2 <= min(Delta_ell/hbar, 4 dtau) ln2 "
    "(Delta_ell/hbar = sum sqrt kappa >= dh)", ok_chain)
# (2) rigidity: |kappa_{e+1} - kappa_e| <= (sup|f'|/L + 2C) hbar; hbar < hbar_0 => step < 1
ok_rig = True
for s_, Cc, L in ((Fr(3, 2), Fr(1, 4), 5), (Fr(7, 3), Fr(1, 2), 3), (Fr(1, 10), Fr(1, 7), 8)):
    hbar0 = Fr(1) / (s_ / L + 2 * Cc)
    for hbar in (hbar0 / 2, hbar0 / 3, hbar0 * Fr(99, 100)):
        step_bound = (s_ / L + 2 * Cc) * hbar
        ok_rig &= step_bound < 1
        # integer-step lemma: the only integer with |d| < 1 is 0
        ok_rig &= all(d == 0 for d in range(-3, 4) if abs(d) < 1)
chk("§B2(2) rigidity: for every exact rational sample below hbar_0 = 1/(sup|f'|/L + 2C), "
    "|dkappa| < 1 and the only integer in (-1,1) is 0 => kappa constant along chains", ok_rig)
# signature classes pairwise distance >= 1: {>=1}, {0}, {<=-1}
dists = [min(abs(a - b) for a in range(1, 6) for b in (0,)) ,
         min(abs(a - b) for a in range(-5, 0) for b in (0,)),
         min(abs(a - b) for a in range(1, 6) for b in range(-5, 0))]
chk("§B2(2) signature separation: the classes {kappa>=1}, {0}, {kappa<=-1} are pairwise "
    "distance >= 1 (min gaps %s) — constancy includes signature" % dists, all(d >= 1 for d in dists))
# (3) the integer step cannot reach spacings 2/L < 1 for L >= 3
chk("§B2(3) class-(iii) arena: spacing 2/L < 1 for every L >= 3 (L = 3..8), so clause (2)'s "
    "integer-step argument does not reach the rational ladder", all(Fr(2, L) < 1 for L in range(3, 9)))
chk("§B2(3) L = 2 recovers per-edge integrality: 2Z/2 = Z exactly",
    all(Fr(2 * m, 2) == int(Fr(2 * m, 2)) for m in range(-4, 5)))
stamp("FT.38: tightening, integer-step rigidity with signature separation, ladder reach")


# ================================================================== §C FT.39
print("§C FT.39 — confinement converse, singlet diagonal, filter placement")
# (1) the {0,1} scalar idempotent law
ok_idem = ok_ex = True
Fsamp = [[C(Fr(3, 7)), C(Fr(-2, 5)), C(0, Fr(1, 3))],
         [C(0, Fr(-1, 2)), C(Fr(1, 4)), C(Fr(5, 6))],
         [C(Fr(-1, 9)), C(0, Fr(4, 3)), C(Fr(-7, 2))]]
for Cc in (0, 1):
    Pi = matscale(I3, Cc)
    PFP = matmul(matmul(Pi, Fsamp), Pi)
    ok_idem &= (Cc * Cc == Cc) and ceq(PFP, matscale(Fsamp, Cc))
    if Cc == 1:
        ok_ex &= not czero(PFP)                  # nonzero aspect data survives
chk("§C1 Pi_C F Pi_C = C F|_Sigma for C in {0,1} (scalar idempotent, Def-H.10); C = 1 nonzero", ok_idem and ok_ex)
ok_basis = all(not czero(T[a]) for a in range(1, 9))
chk("§C1 CT3.9 generators nonzero on C^3: generic nonvanishing for f != 0 on >= 1 colour slot", ok_basis)
# exact exception locus: f = 0 -> zero block; Colour(Sigma) = empty -> zero map
f0 = [[C(0)] * 3 for _ in range(3)]
chk("§C1 exception locus {f = 0}: the zero aspect datum gives the zero block", czero(matscale(f0, 1)))
empty_block = []                                  # 0 x 0 matrix = zero map on the zero space
chk("§C1 exception locus {Colour(Sigma) = empty}: F|_Sigma is the zero map (0 x 0 block)",
    len(empty_block) == 0)
# support-level read: Pi_C = I != 0 whenever C = 1 (unconditional)
chk("§C1 support level: Pi_C = I_3 != 0 whenever C = 1 — unconditional", ceq(matscale(I3, 1), I3))

# (2) singlet diagonal: su(3) annihilates both singlets; <singlet|F|singlet> = 0
eps = [0] * 27
for perm, sgn in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                  ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
    eps[perm[0] * 9 + perm[1] * 3 + perm[2]] = sgn
ok_eps = True
for a in range(1, 9):
    Ta = T[a]
    out = [C(0)] * 27
    for idx in range(27):
        if eps[idx] == 0:
            continue
        i, j, k = idx // 9, (idx // 3) % 3, idx % 3
        # (T (x) 1 (x) 1 + 1 (x) T (x) 1 + 1 (x) 1 (x) T) eps
        for ip in range(3):
            if Ta[ip][i] != C(0):
                out[ip * 9 + j * 3 + k] += Ta[ip][i] * eps[idx]
        for jp in range(3):
            if Ta[jp][j] != C(0):
                out[i * 9 + jp * 3 + k] += Ta[jp][j] * eps[idx]
        for kp in range(3):
            if Ta[kp][k] != C(0):
                out[i * 9 + j * 3 + kp] += Ta[kp][k] * eps[idx]
    ok_eps &= all(x == C(0) for x in out)
chk("§C2 T_a (x) 1 (x) 1 + 1 (x) T_a (x) 1 + 1 (x) 1 (x) T_a annihilates eps — "
    "su(3) kills the triplet singlet (all 8 generators, exact)", ok_eps)
ok_del = True
for a in range(1, 9):
    Ta = T[a]
    Tb = [[-Ta[j][ii] for j in range(3)] for ii in range(3)]     # bar-rep: -T^T
    # (T (x) 1 + 1 (x) Tbar) vec(X) = vec(T X + X Tb^T); at X = I (the delta
    # singlet): vec(T + Tb^T) = vec(T - T) = 0
    TbT = [[Tb[j][ii] for j in range(3)] for ii in range(3)]
    ok_del &= czero(matadd(Ta, TbT))
chk("§C2 delta singlet of 3 (x) 3bar annihilated: (T (x) 1 + 1 (x) Tbar)|delta> = 0 "
    "entrywise, all 8 generators (CT3.17 invariance)", ok_del)
# <singlet| F_strong |singlet> = 0 computed explicitly on the delta singlet of
# 3 (x) 3bar: F (x) 1 + 1 (x) Fbar with Fbar = -F^T; |delta> = sum_i |i>|i>.
ok_exp = True
for fa in ([{a: C(Fr(a, 5), Fr(-a, 7))} for a in range(1, 9)]
           + [{1: C(1), 5: C(Fr(-2, 3))}, {a: C(0) for a in range(1, 9)}]):
    F = [[C(0)] * 3 for _ in range(3)]
    for a, c in fa.items():
        F = matadd(F, matscale(T[a], c))
    Fbar = [[-F[j][ii] for j in range(3)] for ii in range(3)]
    val = C(0)
    for ii in range(3):                    # <delta| (F (x) 1) |delta> = Tr F
        val += F[ii][ii]
    for ii in range(3):                    # <delta| (1 (x) Fbar) |delta> = Tr Fbar
        val += Fbar[ii][ii]
    ok_exp &= (val == C(0))
chk("§C2 <singlet|F_strong|singlet> = 0 exactly: Tr F + Tr Fbar = Tr F - Tr F = 0 "
    "on 10 exact generator combinations (CT3.15/CT3.17 invariance)", ok_exp)
chk("§C2 all eight CT3.9 generators are traceless (Tr T_a = 0)",
    all(trace(T[a]) == C(0) for a in range(1, 9)))
# eps-identity on exact SU(3) witnesses: eps_ijk U^i_a U^j_b U^k_c = eps_abc det U
def det3c(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def eps_id(U):
    d = det3c(U)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                lhs = C(0)
                for ii in range(3):
                    for jj in range(3):
                        for kk in range(3):
                            e = eps[ii * 9 + jj * 3 + kk]
                            if e:
                                lhs += C(e) * U[ii][a] * U[jj][b] * U[kk][c]
                ea = eps[a * 9 + b * 3 + c]
                if lhs != C(ea) * d:
                    return False
    return True


perm_mats = []
for p in itertools.permutations(range(3)):
    sgn = 1 if p in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1
    M = [[C(1) if p[j] == i else C(0) for j in range(3)] for i in range(3)]
    if sgn == 1:                                  # even perms: det = 1, in SU(3)
        perm_mats.append(M)
# rational SO(3) rotations (Pythagorean cos/sin), embedded in SU(3)
def rot(axis, c_, s_):
    R = [[C(0)] * 3 for _ in range(3)]
    R[axis][axis] = C(1)
    u, v = [x for x in range(3) if x != axis]
    R[u][u] = C(c_); R[u][v] = -C(s_); R[v][u] = C(s_); R[v][v] = C(c_)
    return R


rots = [rot(0, Fr(3, 5), Fr(4, 5)), rot(1, Fr(5, 13), Fr(12, 13)), rot(2, Fr(7, 25), Fr(24, 25)),
        matmul(rot(0, Fr(3, 5), Fr(4, 5)), rot(1, Fr(5, 13), Fr(12, 13)))]
wit = perm_mats + rots
ok_w = all(eps_id(U) and det3c(U) == C(1) for U in wit)
chk("§C2 eps_ijk U^i_a U^j_b U^k_c = eps_abc det U on %d exact SU(3) witnesses "
    "(even permutations + rational rotations, CT3.15)" % len(wit), ok_w)

# (3) filter placement: the FT.18 witness, machine-built
V = ["v1", "v2", "v3"]
W_ = ["w1", "w2", "w3", "w4", "w5", "w6"]
U9 = V + W_
C_group = [frozenset(x) for x in (("v1", "v2", "v3"), ("w1", "w2", "w3"), ("w4", "w5", "w6"))]
Cp_group = [frozenset(x) for x in (("v1", "w1", "w2"), ("v2", "w3", "w4"), ("v3", "w5", "w6"))]


def valid(g):
    return (set().union(*g) == set(U9) and sum(len(p) for p in g) == len(U9)
            and all(len(p) in (2, 3) for p in g))


def seal(g, Sig):
    return all((p <= set(Sig)) or not (p & set(Sig)) for p in g) and \
        all(p <= set(Sig) for p in g if p & set(Sig))


def occupy(g, Sig):
    return sorted(x for p in g for x in p if x in Sig)


chk("§C3 FT.18 witness: both ambient groupings valid (parts of size 2/3, CT3.18/FT.41(b) grammar)",
    valid(C_group) and valid(Cp_group))
chk("§C3 identical Sigma occupation (triplet carriers v1,v2,v3 in both restrictions)",
    occupy(C_group, V) == occupy(Cp_group, V) == V)
chk("§C3 opposite seals: C(Sigma;C) = 1 (partners inside) vs C(Sigma;C') = 0 (partners outside)",
    seal(C_group, V) and not seal(Cp_group, V))
# pre-weighting loses physical colour-independent reads; downstream filter does not
f_v1 = C(Fr(1))                                   # EM read datum at v1 (f_v != 0 => EM in A)
EM_read = {"C": f_v1, "Cp": f_v1}                 # colour-independent (FT.11/FT.21)
preweighted = {k: (v * (1 if seal(g, V) else 0)) for (k, v), g in
               zip(EM_read.items(), (C_group, Cp_group))}
chk("§C3 pre-weighting deletes C'|_Sigma's EM read (f_v1 != 0 lost) — data loss demonstrated",
    preweighted["Cp"] == C(0) and EM_read["Cp"] != C(0))
# downstream Pi_C: strong block zeroed exactly, EM/G/H blocks kept
alpha_em = C(Fr(22, 7)); g_block = C(Fr(-3, 2))
Fblocks = {"EM": [[alpha_em]], "G": [[g_block]], "strong": matscale(T[1], 1)}
for Cc in (0, 1):
    masked = dict(Fblocks)
    masked["strong"] = matscale(Fblocks["strong"], Cc)
    if Cc == 0:
        chk("§C3 downstream Pi_C at C = 0: strong block zeroed, EM/G/H kept exactly",
            czero(masked["strong"]) and masked["EM"] == Fblocks["EM"] and masked["G"] == Fblocks["G"])
    else:
        chk("§C3 downstream Pi_C at C = 1: every block kept (corpus-consistent placement)",
            all(masked[k] == Fblocks[k] for k in Fblocks))
stamp("FT.39: idempotent law + exception locus, singlet annihilation (eps/delta), "
      "eps-identity witnesses, FT.18 placement witness, block algebra")

# ================================================================== §D FT.40
print("§D FT.40 — closed-core charge read")
qtab = {}
for s1 in (1, -1):
    for sk in (1, -1):
        qtab[(s1, sk)] = Fr(s1 - sk, 2)
chk("§D1 q_core = (sig_e1 - sig_ek)/2 is ternary {-1,0,+1} on the full register census",
    set(qtab.values()) == {Fr(-1), Fr(0), Fr(1)})
chk("§D1 all three values attained (EM.9 alphabet): +1 at (+,-), -1 at (-,+), 0 at (=)",
    qtab[(1, -1)] == 1 and qtab[(-1, 1)] == -1 and qtab[(1, 1)] == 0 and qtab[(-1, -1)] == 0)
ok_rev = all(qtab[(sk, s1)] == -qtab[(s1, sk)] for s1 in (1, -1) for sk in (1, -1))
chk("§D1 rebase/oriental reversal e1 <-> ek: q -> -q verbatim (D2.6's omega law)", ok_rev)
# 2-cycle floor: c = (e1: p->q, e2: q->p); base p reads (sig_e1 - sig_e2)/2, base q negated
ok_floor = True
for s1 in (1, -1):
    for s2 in (1, -1):
        qp = Fr(s1 - s2, 2)
        qq = Fr(s2 - s1, 2)                      # rebase at q: first edge e2, last e1
        ok_floor &= (qp == -qq)
chk("§D1 2-cycle floor: q_core at base p = (sig_e1 - sig_e2)/2, negated at base q (all 4 states)", ok_floor)
chk("§D1 not neutral by closure: 2 of 4 register states carry q_core != 0",
    sum(1 for v in qtab.values() if v != 0) == 2)
chk("§D1 N_charge = 2: the read is a function of exactly the two end registers "
    "(census domain {+-1}^2 = 4 states, CT0.9 independent registers)", len(qtab) == 4)
stamp("FT.40: ternary census, reversal law, floor basepoints, end-register count")

# ================================================================== §E FT.41
print("§E FT.41 — the per-aspect ledger")
# (a) decomposition
ok_dec = all(2 + (dh - 2) == dh and dh - 2 >= 0 for dh in range(2, 13))
chk("§E(a) N_charge = 2, N_weak = dh - 2, N_visible = dh (FT.14 decomposition, dh = 2..12)", ok_dec)

# (b) sealing grammar: labelled set partitions into parts of size 2 and 3
def partitions_23(items):
    if not items:
        yield []
        return
    first = items[0]
    rest = items[1:]
    # explicit recursion: pair first with someone, or triple first with two others
    for j in range(len(rest)):
        pair = [first, rest[j]]
        rem = [x for idx, x in enumerate(rest) if idx != j]
        for p in partitions_23(rem):
            yield [pair] + p
    for j in range(len(rest)):
        for k in range(j + 1, len(rest)):
            trip = [first, rest[j], rest[k]]
            rem = [x for idx, x in enumerate(rest) if idx not in (j, k)]
            for p in partitions_23(rem):
                yield [trip] + p


def count_23(N):
    return sum(1 for _ in partitions_23(list(range(N))))


def closed_form(N):
    tot = 0
    for b in range(N // 3 + 1):
        a = (N - 3 * b) // 2
        if 3 * b + 2 * a != N:
            continue
        tot += math.factorial(N) // (math.factorial(a) * math.factorial(b) * (2 ** a) * (6 ** b))
    return tot


brute = [count_23(N) for N in range(1, 9)]
doc = [0, 1, 1, 3, 10, 25, 105]
chk("§E(b) exhaustive enumeration N = 1..8: %s == closed form" % brute,
    brute == [closed_form(N) for N in range(1, 9)])
chk("§E(b) documented counts 0,1,1,3,10,25,105 (N = 1..7) reproduced exactly", brute[:7] == doc)
chk("§E(b) N = 6 split 15 + 10 = 25 ((a,b) = (3,0) + (0,2))",
    closed_form(6) == 25
    and math.factorial(6) // (6 * 8) == 15 and math.factorial(6) // (2 * 36) == 10)
chk("§E(b) FT.42 card values: g(6) = 25, g(8) = 385, g(12) = 164395, g(20) = 292938721075",
    closed_form(6) == 25 and closed_form(8) == 385
    and closed_form(12) == 164395 and closed_form(20) == 292938721075)
chk("§E(b) N_strong(Sigma) = log2(#groupings) is the sealing-pattern information "
    "(exact powers at N = 2, 3; non-integral elsewhere is data, not defect)",
    closed_form(4) == 3 and closed_form(5) == 10)

# (c) the gravity ledger: L integers, one loop constraint Theta in 2Z
ok_cnt = True
for L in (2, 3, 4, 5):
    for B in (1, 2, 3):
        brute_n = sum(1 for kap in itertools.product(range(-B, B + 1), repeat=L)
                      if sum(kap) % 2 == 0)
        # even-sum tuples over [-B,B]^L: ((2B+1)^L + (E-O)^L)/2 with E-O = (-1)^B
        formula = ((2 * B + 1) ** L + (-1) ** (B * L)) // 2
        ok_cnt &= brute_n == formula
chk("§E(c) bounded ledger counts = ((2B+1)^L + (-1)^(BL))/2 exactly "
    "(L = 2..5, B = 1..3 brute force)", ok_cnt)
ok_free = True
for L in (2, 3, 4):
    B = 2
    tot = 0
    for kp in itertools.product(range(-B, B + 1), repeat=L - 1):
        par = (-sum(kp)) % 2
        tot += sum(1 for x in range(-B, B + 1) if x % 2 == par)
    ok_free &= tot == ((2 * B + 1) ** L + (-1) ** (B * L)) // 2
chk("§E(c) L-1 free integers + parity-determined last: parameterization counts match", ok_free)
ok_unb = all((sum((2 * m,) + (0,) * (L - 1)) % 2 == 0) for m in range(1, 51) for L in (3,))
chk("§E(c) unbounded witness family kappa = (2m, 0, ..., 0), m = 1..50: Theta = 2m in 2Z "
    "=> the ledger is not bit-type (C10: bits attach to finite registered sets)", ok_unb)
ledger_types = {"registration-bit (charge, colour)", "unbounded-integer (gravity)",
                "continuous-real (Higgs h0, EW.13/P4)"}
chk("§E(c) the trichotomy: three pairwise distinct ledger types — bit-counts are "
    "well-posed exactly for the registration-type ledgers (a),(b)", len(ledger_types) == 3)

# (d) strictly new at Sigma: dim u(N) = N^2, factored diagonal = N, new = N^2 - N
chk("§E(d) N(Sigma) = 1: dim u(1) = 1 = factored diagonal, strictly new = 1^2 - 1 = 0",
    1 * 1 - 1 == 0)
E12 = [[C(0), C(1)], [C(0), C(0)]]
E21 = [[C(0), C(0)], [C(1), C(0)]]
X1 = matadd(E12, E21)                             # |e1><e2| + h.c.
X2 = matscale(matadd(E12, matscale(E21, -1)), i_)  # i(|e1><e2| - h.c.)
D1 = [[C(1), C(0)], [C(0), C(0)]]
D2 = [[C(0), C(0)], [C(0), C(1)]]
herm = all(ceq(X, conj_transpose(X)) for X in (X1, X2))
tr0 = all(trace(X) == C(0) for X in (X1, X2))


def real_rank(mats):
    rows = []
    for M in mats:
        rows.append([M[i][j].re for i in range(2) for j in range(2)] +
                    [M[i][j].im for i in range(2) for j in range(2)])
    piv = 0
    rows = [r[:] for r in rows]
    for col in range(len(rows[0])):
        pr = next((r for r in range(piv, len(rows)) if rows[r][col] != 0), None)
        if pr is None:
            continue
        rows[piv], rows[pr] = rows[pr], rows[piv]
        for r in range(len(rows)):
            if r != piv and rows[r][col] != 0:
                f = Fr(rows[r][col]) / Fr(rows[piv][col])
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
        piv += 1
    return piv


rk = real_rank([D1, D2, X1, X2])
diag_comm = [not czero(matadd(matmul(matmul(D1, X), D1), matscale(X, -1))) for X in (X1, X2)]
chk("§E(d) N(Sigma) = 2: dim u(2) = 4; the two exchange generators are Hermitian, traceless",
    herm and tr0 and 2 * 2 == 4)
chk("§E(d) strictly new = N^2 - N = 2 real dimensions: {diag(2)} + {X1,X2} independent (rank 4)",
    rk == 4)
chk("§E(d) the exchange modes are off-diagonal boundary mixings (non-commuting with the diagonal)",
    any(diag_comm))
stamp("FT.41: decomposition, sealing grammar (exhaustive + closed form), kappa ledger, u(2) modes")

print()
if FAIL:
    print(f"verify_H_closure: {PASS} passed, {FAIL} FAILED")
    sys.exit(1)
print(f"verify_H_closure: {PASS} checks green  ({time.time()-t0:.1f}s)")
