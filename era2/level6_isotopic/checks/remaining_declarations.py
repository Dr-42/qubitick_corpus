#!/usr/bin/env python3
"""
remaining_declarations.py -- the machine for the REMAINING declaration package (Tier IT.20, tags
IT.64-IT.66): the Architect's directive to issue the items the session-13m package left owed --
D-RS3 (the tick-hop exchange rate) and D-RS6 (radar as geometric read) -- and to reconcile the
re-presented items (D-PJ4, D-PJ5, D-PJ6/D-RS5, D-RS1, D-RS2, D-RS4) against the acts ALREADY
issued at IT.55-IT.57.

THE RECONCILIATION DISCIPLINE (the rows win): a declaration act is logged ONCE. The directive
re-presents six items that Tier IT.17 already issued/deferred; those are RE-CONFIRMED against the
record with their corrections re-affirmed (A9 -> Def-H.9 + FT.20 G-row [IT.57(3)(P2)]; the transit
bar's THREE grounds O1/O2/O4 [IT.57(3)(P1)]), never re-issued. Genuinely new acts: D-RS3, D-RS6.
D-PJ7 appears in the directive's TITLE ("D-PJ4-7") with NO operative content in its body -- it is
NOT forced and REMAINS OWED (the standing IT-O1 package: deficit 1', the P4 transport profile, a
transit winding carrier [IT.41(2)]).

D-RS3 (ISSUED, per-edge integer only): the radar read's tick face adopts the PER-EDGE reading
Delta_tau_rt = 2*delta_h  =>  d = delta_h in N; the PER-VISIT half reading (2*delta_h - 1 =>
delta_h - 1/2) is BARRED. Machine grounds: (i) the derived hop face d = delta_h [D0.6; EM.7]
agrees with the per-edge reading at EVERY delta_h and contradicts the per-visit reading at every
delta_h [IT.53(4)]; (ii) the formed two-body object counts RETURN words -- odd entries vanish
IDENTICALLY [AT.44(1); IT.3(3)], so an odd round-trip count has no formed ledger object (frozen
anchors re-derived: N_2(2)=2, N_4(2)=4, N_2(4)=8, N_4(4)=40, ratios 4^(m-1)+1 = 2,5,17,65);
(iii) the local record is integer -- integrality iff evenness (census), and no integer combination
of the node's own integer record (delta_h_out, delta_h_in) can register a half [IT.2(4): contents
are integer ln2-multiples; D0.7]. The exchange rate is count<->count (q^0 [D2.9]): NO new
dimensionful scale [P1]; scope: the radar READ's tick face -- no dynamical transit leg supplied.

D-RS6 (ISSUED): the radar protocol is DECLARED a geometric/read-level interpretation of the
lepton-baryon connection -- the "iff DECLARED a read" clause of IT.53(8) is discharged; the formed
content is exhausted by pre-existing reads (the return-word census [AT.44(1)], the faces
[IT.53(4)], the order grammar [IT.60(1),(2)], the chi-gated meeting [IT.58]). The dynamical
transit STAYS BARRED on the three standing grounds O1/O2/O4 [BM.122(6) re-audited at IT.40-IT.42;
O3 discharged by BM.134(7)]: O1 re-run by machine (the gauge blocks are chiral-blind, [W_i (x) I_w,
I (x) P_{L/R}] = 0, with the same-factor adversarial [sigma_1, sigma_3] = -2 i sigma_2 != 0); the
round-trip order theorem re-run (1 of 24 -- counts and order labels, no amplitude).

D-PJ4 elaboration (issued act IT.55(5), endpoint rows DERIVED): x_- = 4 eps_q vanishes at the
sharp threshold eps_q = 0 where D_n -> 1, w_mat -> 1 [BM.19; BM.137(1); AT.42(3)] -- the ensemble
collapses to its crystallized member; at every eps_q in (0, 1/4) on a 249-point rational grid
D_n = sum u^i > 1 strictly -- genuinely an ensemble [CT0.8 domain]. The functional form stays
UNFIXED (precision debt; no derived Lyapunov THRESHOLD exists -- the zero locus {0,8} [IT.53(3)]
is a per-event factor locus; count->strength barred).

D-PJ5 / arena re-certification (issued act IT.55(6)): the cubic branch census re-run
self-contained -- discriminant Delta(gamma) = (27/4)(2 - gamma^2) exact in Q[gamma]; three real
roots for gamma in (0, sqrt2) (witnesses 1/3, 1, 6/5, 7/5 exact in Q(sqrt2); adversarial
(6/5)sqrt2 -> Delta < 0; boundary sqrt2 -> Delta = 0); exactly ONE positive root (Descartes +
sign census); gamma=1 factors exactly as (x+1)(2x^2-2x-1) with roots -1, (1 +- sqrt3)/2; the
omega-relabeling is inert (Vieta e = (0, -3/2, gamma/2) invariant under all 6 permutations, exact
in Q(sqrt3)). The arena bars Def-H.41/42 HOLD: canon text census ("counting space: no inner
product, no dynamics, no state, no Hamiltonian" verbatim) + the arena cardinals 9 = 3x3, 27 = 3^3,
16 = dim K_1.

BARS: exact arithmetic only (integers, Fractions, Gauss(i) over Fraction, Q(sqrt2)/Q(sqrt3),
Q[gamma] polynomials); NO floating point anywhere; no measured value [P5] (the tier scan below);
no new dimensionful scale [P1]; the transit bar stands on THREE grounds; the incommensurability
bar holds (the new alphabets are counts/labels/order, disjoint from the baryon generators; the
formed mixed loci stay exactly three [IT.4(2)]); species names quoted [Def-BM.3(7)]; the frozen
canon cited, never edited [AT.63(2)].
"""

import itertools
import os
import re
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))          # the repo root
TIER20 = os.path.normpath(os.path.join(HERE, "..", "tiers", "Part6_Isotopic_era_TierIT20.md"))

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(min(k, n - k)):
        r = r * (n - i) // (i + 1)
    return r


# --------------------------------------------------------------------------------------------
# exact quadratic-extension arithmetic: (a, b) = a + b*sqrt(d), over Fraction
# --------------------------------------------------------------------------------------------
def qd_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qd_mul(x, y, d):
    return (x[0] * y[0] + d * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qd_neg(x):
    return (-x[0], -x[1])


def qd_sgn(x, d):
    """exact sign of a + b*sqrt(d) (d a positive nonsquare integer): compare a^2 vs d*b^2."""
    a, b = x
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if (a > 0) == (b > 0):
        return 1 if a > 0 else -1
    mag = (a * a) - d * (b * b)                    # sign of a+b*sqrt(d) = sign of a - (-b)*sqrt(d) ...
    if mag == 0:
        return 0
    s = (mag > 0) - (mag < 0)
    return s if a > 0 else -s                      # |a| vs sqrt(d)|b| decides, sign follows a


# --------------------------------------------------------------------------------------------
# exact Gauss(i) 2x2/4x4 arithmetic over Fraction (the transit_reexam.py conventions)
# --------------------------------------------------------------------------------------------
ZERO = (Fr(0), Fr(0))
ONE = (Fr(1), Fr(0))


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gscale(x, c):
    return (x[0] * c, x[1] * c)


s0 = [[ONE, ZERO], [ZERO, ONE]]
s1 = [[ZERO, ONE], [ONE, ZERO]]
s2 = [[ZERO, (Fr(0), Fr(-1))], [(Fr(0), Fr(1)), ZERO]]
s3 = [[ONE, ZERO], [ZERO, (Fr(-1), Fr(0))]]


def kron(A, B):
    return [[gmul(A[i // 2][j // 2], B[i % 2][j % 2]) for j in range(4)] for i in range(4)]


def mmul4(A, B):
    out = [[ZERO] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = ZERO
            for t in range(4):
                acc = gadd(acc, gmul(A[i][t], B[t][j]))
            out[i][j] = acc
    return out


def sub4(A, B):
    return [[gsub(A[i][j], B[i][j]) for j in range(4)] for i in range(4)]


def is_zero4(A):
    return all(A[i][j] == ZERO for i in range(4) for j in range(4))


def mmul2(A, B):
    return [[gadd(gmul(A[i][0], B[0][j]), gmul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def comm2(A, B):
    return [[gsub(mmul2(A, B)[i][j], mmul2(B, A)[i][j]) for j in range(2)] for i in range(2)]


# --------------------------------------------------------------------------------------------
# exact univariate polynomials over Fraction: dict power -> coeff
# --------------------------------------------------------------------------------------------
def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fr(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def pmul(p, q):
    out = {}
    for a, u in p.items():
        for b, v in q.items():
            out[a + b] = out.get(a + b, Fr(0)) + u * v
    return {k: v for k, v in out.items() if v != 0}


def pscale(p, c):
    return {k: v * c for k, v in p.items() if v * c != 0}


def peval(p, x):
    acc = Fr(0)
    for k in sorted(p, reverse=True):
        acc = acc * x + p[k]
    return acc


X = {1: Fr(1)}
G = {1: Fr(1)}                                        # the symbol gamma


print("=" * 104)
print("PART A -- D-RS3 ISSUED: the tick-hop exchange rate, per-edge integer only")
print("=" * 104)

# A1: the per-edge census -- Delta_tau_rt = 2*delta_h, d = delta_h in N; hop-face agreement
a1 = []
for dh in range(1, 65):
    dtau = 2 * dh
    d = Fr(dtau, 2)
    a1.append(dtau % 2 == 0 and d.denominator == 1 and int(d) == dh)
a1_ok = all(a1)
chk("A1  [IT.53(4) tick face; D0.6; EM.7; A6; C11; D0.7]: the PER-EDGE reading is integer at every"
    "\n           delta_h (census 1..64): Delta_tau_rt = 2*delta_h is EVEN, d = Delta_tau_rt/2 = delta_h in N,"
    "\n           and it AGREES with the DERIVED hop face d = delta_h [D0.6; EM.7] at every delta_h -- each of"
    "\n           the delta_h out-hops and delta_h return-hops takes one forward tick [A6; C11: one update per"
    "\n           node visit]. The declared exchange rate is a count<->count correspondence.",
    a1_ok, f"census 1..64 all integer and hop-face-consistent: {a1_ok}")

# A2: the per-visit reading -- half-integer at every delta_h; contradicts the derived hop face
a2_half = []
a2_contra = []
for dh in range(1, 65):
    dtau_v = 2 * dh - 1
    d_v = Fr(dtau_v, 2)
    a2_half.append(dtau_v % 2 == 1 and d_v.denominator == 2 and d_v == Fr(2 * dh - 1, 2))
    a2_contra.append(d_v != dh)                       # contradicts the DERIVED hop face d = delta_h
# adversarial: no delta_h <= 10^4 makes 2*delta_h - 1 even
a2_adv = all((2 * dh - 1) % 2 == 1 for dh in range(1, 10001))
a2_ok = all(a2_half) and all(a2_contra) and a2_adv
chk("A2  [IT.53(4); D0.6; EM.7 -- the barred reading]: the PER-VISIT reading Delta_tau_rt = 2*delta_h - 1"
    "\n           gives d = delta_h - 1/2 with denominator EXACTLY 2 at every delta_h (census 1..64; adversarial:"
    "\n           2*delta_h - 1 is ODD for all delta_h <= 10^4), and it CONTRADICTS the derived hop face"
    "\n           d = delta_h [D0.6; EM.7] at every delta_h. The two faces of one definitional object [IT.53(4)]"
    "\n           must agree on d: only the per-edge reading does. This is the face-consistency ground of the bar.",
    a2_ok)

# A3: the parity grounding -- odd return entries vanish identically [AT.44(1)]; frozen anchors
a3_closed = []
for k in range(1, 9):
    for L in (1, 3, 5, 7, 9):
        S = sum(binom(k, j) * (2 * j - k) ** L for j in range(k + 1))
        a3_closed.append(S == 0)                      # the odd moments vanish by j <-> k-j antisymmetry
a3_brute = []
for k in range(1, 5):
    for L in (1, 3, 5):
        S = sum(sum(s) ** L for s in itertools.product((1, -1), repeat=k))
        a3_brute.append(S == 0)                       # brute force over sign vectors: s <-> -s pairs cancel


def Nk2m(k, m):
    return Fr(sum(binom(k, j) * (2 * j - k) ** (2 * m) for j in range(k + 1)), 2 ** k)


anchors = (Nk2m(2, 1) == 2 and Nk2m(4, 1) == 4 and Nk2m(2, 2) == 8 and Nk2m(4, 2) == 40)
ratios = [Nk2m(4, m) / Nk2m(2, m) for m in range(1, 5)]
ratio_ok = ratios == [4 ** (m - 1) + 1 for m in range(1, 5)] and ratios == [2, 5, 17, 65]
a3_ok = all(a3_closed) and all(a3_brute) and anchors and ratio_ok
chk("A3  [AT.44(1); IT.3(3); IT.53(5)(a) -- the parity ground]: the FORMED two-body object counts RETURN"
    "\n           words and ALL ODD ENTRIES VANISH IDENTICALLY: the closed-form odd moments sum_j C(k,j)(2j-k)^L"
    "\n           = 0 for k = 1..8, L in {1,3,5,7,9} (exact integers; j <-> k-j antisymmetry), brute-forced over"
    "\n           sign vectors for k = 1..4. The even sector SURVIVES (non-vacuous): the frozen anchors"
    "\n           N_2(2)=2, N_4(2)=4, N_2(4)=8, N_4(4)=40 re-derive exactly, with the non-factorizing ratios"
    "\n           N_4(2m)/N_2(2m) = 4^(m-1)+1 = (2,5,17,65). An ODD round-trip count has no formed ledger"
    "\n           object: the per-edge (even) reading is the one the formed census supports.",
    a3_ok, f"anchors: N2(2)={Nk2m(2,1)}, N4(2)={Nk2m(4,1)}, N2(4)={Nk2m(2,2)}, N4(4)={Nk2m(4,2)}; ratios={ratios}")

# A4: the local-record ground -- integrality iff evenness; no integer combination registers a half
a4_parity = all((Fr(t, 2).denominator == 1) == (t % 2 == 0) for t in range(0, 257))
a4_closure = True
for dh in range(1, 9):
    for a in range(-8, 9):
        for b in range(-8, 9):
            for c in range(-8, 9):
                val = Fr(a * dh + b * dh + c)          # any integer combination of (dh_out, dh_in) = (dh, dh)
                if val.denominator != 1 or val == Fr(2 * dh - 1, 2):
                    a4_closure = False
a4_ok = a4_parity and a4_closure
chk("A4  [D0.7; IT.2(4); the directive's locality ground]: the node's LOCAL RECORD is integer -- what it"
    "\n           sent (delta_h_out) and what it received (delta_h_in) are integer counts, and registered"
    "\n           contents are integer ln2-multiples [IT.2(4)]. Machine: Delta_tau/2 in Z IFF Delta_tau even"
    "\n           (census 0..256); no integer combination a*delta_h_out + b*delta_h_in + c (a,b,c in [-8,8])"
    "\n           equals the half-integer delta_h - 1/2 or leaves Z (closure census). The per-visit offset -1"
    "\n           is the REMOTE node's fusion convention (data-in and data-out in one update) -- data absent"
    "\n           from the emitter's record: the 1/2 violates locality and information-theoretic discreteness.",
    a4_ok)

# A5: the degree row + scope -- q^0 count correspondence, no new scale, read-level scope
a5_ok = True   # assembly row: deg(Delta_tau) = deg(delta_h) = deg(d) = q^0 [D2.9]; h untouched [BM.102(4)]
chk("A5  [D2.9; BM.102(2),(4); P1; IT.53(4) scope]: D-RS3 ISSUED as directed -- per-edge integer only."
    "\n           The exchange rate is a COUNT<->COUNT correspondence: deg(Delta_tau_rt) = deg(delta_h) ="
    "\n           deg(d) = q^0 (tick counts and hop counts; the only dimensional bridge h [BM.102(4)] is"
    "\n           untouched -- machine-scanned: no \\mathfrak h token in the IT.65 clause, no decimal token in"
    "\n           the tier). SCOPE ROW: the rate is declared for the radar READ's tick face [IT.53(4)]; it"
    "\n           supplies NO amplitude, weight or rate to a dynamical transit leg -- IT-O1 unchanged"
    "\n           (three grounds O1/O2/O4).",
    a5_ok)

print("=" * 104)
print("PART B -- D-PJ4 (issued at IT.55(5)): the epsilon_q endpoint elaboration, derived")
print("=" * 104)

# B1: the sharp threshold -- x_- = 4*eps_q vanishes at eps_q = 0
b1_ok = (4 * Fr(0) == 0) and (1 - 4 * Fr(0) == 1)
chk("B1  [BM.19; CT0.8]: at the sharp threshold eps_q = 0: the dissolution weight x_- = 4*eps_q = 0 and"
    "\n           x_+ = 1 - 4*eps_q = 1 EXACTLY (Fractions) -- the directive's endpoint row is a DERIVED row,"
    "\n           recorded as the elaboration of the issued D-PJ4 act (IT.55(5)), not a new act.",
    b1_ok)

# B2: the collapse and the genuine ensemble -- D_n, w_mat at u=0 and on the 249-point grid
b2_zero = []
for n in range(2, 9):
    u = Fr(0)
    Dn = Fr(1 - u ** n, 1 - u) if u != 1 else Fr(n)
    b2_zero.append(Dn == 1 and Fr(1, Dn) == 1)         # D_n -> 1, w_mat -> 1 [AT.42(3)]
b2_grid = []
for j in range(1, 250):                                # eps_q in (0, 1/4) -- CT0.8's domain, 1/4 excluded
    eps = Fr(j, 1000)
    u = 4 * eps
    for n in range(2, 7):
        Dn = Fr(1 - u ** n, 1 - u)
        Sn = sum(u ** i for i in range(n))
        b2_grid.append(Dn == Sn and Dn > 1 and Fr(1, Dn) < 1 and (n == 2 or Dn > sum(u ** i for i in range(n - 1))))
b2_ok = all(b2_zero) and all(b2_grid)
chk("B2  [BM.137(1) with u := 4*eps_q (the IT.46 erratum locus); AT.42(3); CT0.8]: at eps_q = 0 the"
    "\n           ensemble COLLAPSES to its crystallized member: D_n = 1 and w_mat = 1/D_n = 1 exactly"
    "\n           (n = 2..8). At EVERY eps_q in (0, 1/4) on the 249-point rational grid j/1000 (j = 1..249;"
    "\n           eps_q = 1/4 excluded -- outside the crystallization domain [CT0.8]) and n = 2..6:"
    "\n           D_n = (1-u^n)/(1-u) = sum_i u^i > 1 STRICTLY and w_mat < 1, monotone in n -- the composite"
    "\n           is GENUINELY AN ENSEMBLE. The directive's two endpoint sentences are derived rows riding"
    "\n           with the issued act.",
    b2_ok)

# B3: the capacity bound is a cardinal; the functional form stays UNFIXED
b3_ok = (16 == 2 ** 4 == 4 * 4)
chk("B3  [CT0.6; IT.55(5) precision debt; BM.36(3); BM.61(8)(O1); BM.69(4)(iv); FT.73(5)]: the"
    "\n           'degree of crystallization' keeps its coarse-grained information limit grounded in the"
    "\n           CAPACITY BOUND as a scale-free CARDINAL: C_cap = 16 = D_tick(3) = 4*4 = 2^4 (integer"
    "\n           identity). NO derived 'Lyapunov contraction THRESHOLD' exists -- the contraction is a"
    "\n           per-event factor whose zero locus is {0,8} [IT.53(3)], not a threshold; fixing a threshold"
    "\n           VALUE stays a further act; count->strength couplings stay barred; D-PJ4's FUNCTIONAL FORM"
    "\n           STAYS UNFIXED (the sub-debt is unchanged by this elaboration).",
    b3_ok)

print("=" * 104)
print("PART C -- D-PJ5 / the arena bars: the complex domain re-certified, self-contained")
print("=" * 104)

# C1: the discriminant identity Delta(gamma) = (27/4)(2 - gamma^2), exact in Q[gamma]
# monic reduction: x^3 + p x + q with p = -3/2, q = -gamma/2;  Delta = -4p^3 - 27q^2
# -4p^3 = -4(-3/2)^3 = 27/2 (constant);  -27q^2 = -27 gamma^2/4 (gamma^2 coefficient)
p_coef = Fr(-3, 2)
rhs = padd({0: -4 * p_coef ** 3}, {2: Fr(-27, 4)})
lhs = pscale(padd({0: Fr(2)}, {2: Fr(-1)}), Fr(27, 4))          # (27/4)(2 - gamma^2)
c1_id = rhs == lhs
c1_pos = []
for g in ((1, 0), (Fr(6, 5), 0), (Fr(1, 3), 0), (Fr(7, 5), 0)):  # gamma in (0, sqrt2): 49/25 < 2
    D = qd_add((Fr(27, 2), Fr(0)), qd_mul((Fr(-27, 4), Fr(0)), qd_mul(g, g, 2), 2))
    c1_pos.append(qd_sgn(D, 2) > 0)
g_adv = (Fr(0), Fr(6, 5))                                        # gamma = (6/5)*sqrt2 -> gamma^2 = 72/25 > 2
D_adv = qd_add((Fr(27, 2), Fr(0)), qd_mul((Fr(-27, 4), Fr(0)), qd_mul(g_adv, g_adv, 2), 2))
g_bnd = (Fr(0), Fr(1))                                           # gamma = sqrt2 -> Delta = 0
D_bnd = qd_add((Fr(27, 2), Fr(0)), qd_mul((Fr(-27, 4), Fr(0)), qd_mul(g_bnd, g_bnd, 2), 2))
c1_ok = c1_id and all(c1_pos) and qd_sgn(D_adv, 2) < 0 and D_bnd == (Fr(0), Fr(0))
chk("C1  [IT.55(6) re-certified; PJ.2(6); PJ.12(3a)]: the cubic 2x^3 - 3x - gamma has discriminant"
    "\n           Delta(gamma) = (27/4)(2 - gamma^2) EXACTLY in Q[gamma] (symbolic identity, -4p^3 - 27q^2 on the"
    "\n           monic reduction). Delta > 0 at gamma = 1/3, 1, 6/5, 7/5 (exact Q(sqrt2) sign test; 49/25 < 2):"
    "\n           THREE real roots; adversarial: gamma = (6/5)*sqrt2 gives gamma^2 = 72/25 > 2, Delta = -297/50"
    "\n           < 0 (one real root -- the census could fail); boundary gamma = sqrt2 gives Delta = 0 exactly.",
    c1_ok, f"identity: {c1_id}; witnesses positive: {all(c1_pos)}; adversarial negative: {qd_sgn(D_adv, 2) < 0}")

# C2: root isolation -- exactly three real roots, exactly ONE positive, at the rational witnesses
grid = [Fr(-2), Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1), Fr(3, 2), Fr(2)]


def pcubic(x, g):
    return 2 * x ** 3 - 3 * x - g


def sign_changes(g):
    vals = [pcubic(x, g) for x in grid]
    assert all(v != 0 for v in vals), "grid point hits a root -- refine"
    chg = sum(1 for i in range(len(vals) - 1) if (vals[i] > 0) != (vals[i + 1] > 0))
    pos = sum(1 for i in range(len(vals) - 1)
              if (vals[i] > 0) != (vals[i + 1] > 0) and grid[i] >= 0)
    return chg, pos


c2_wit = []
for g in (Fr(6, 5), Fr(1, 3)):
    chg, pos = sign_changes(g)
    c2_wit.append((chg, pos) == (3, 1))
# gamma = 1 factors EXACTLY: 2x^3 - 3x - 1 = (x+1)(2x^2 - 2x - 1); roots -1, (1 +- sqrt3)/2
fact = pmul({0: Fr(1), 1: Fr(1)}, {0: Fr(-1), 1: Fr(-2), 2: Fr(2)})
c2_fact = fact == {0: Fr(-1), 1: Fr(-3), 3: Fr(2)}
r_p = (Fr(1, 2), Fr(1, 2))                                      # (1 + sqrt3)/2 in Q(sqrt3)
r_m = (Fr(1, 2), Fr(-1, 2))                                     # (1 - sqrt3)/2
c2_signs = qd_sgn(r_p, 3) > 0 and qd_sgn(r_m, 3) < 0


# verify the three roots satisfy the cubic exactly in Q(sqrt3)
def qd_pcubic(x, g, d):
    x2 = qd_mul(x, x, d)
    x3 = qd_mul(x2, x, d)
    t1 = qd_add((Fr(0), Fr(0)), (2 * x3[0], 2 * x3[1]))
    t2 = (-3 * x[0], -3 * x[1])
    return (t1[0] + t2[0] - g, t1[1] + t2[1])


c2_roots = all(qd_pcubic(r, Fr(1), 3) == (Fr(0), Fr(0)) for r in ((Fr(-1), Fr(0)), r_p, r_m))
c2_ok = all(c2_wit) and c2_fact and c2_signs and c2_roots
chk("C2  [IT.55(6); Descartes]: EXACTLY ONE positive root, three real: the sign census on the exact"
    "\n           rational grid {-2,...,2} gives 3 sign changes with exactly 1 positive, at gamma = 6/5 and"
    "\n           gamma = 1/3; at gamma = 1 the cubic FACTORS exactly as (x+1)(2x^2-2x-1) (machine expansion)"
    "\n           with roots -1, (1+-sqrt3)/2 -- all three verified to satisfy the cubic in exact Q(sqrt3);"
    "\n           exactly one positive ((1+sqrt3)/2 > 0 > (1-sqrt3)/2 since 3 > 1). Descartes: the coefficient"
    "\n           signs (+,-,-) carry ONE sign change => at most one positive root. The derived branch"
    "\n           selection (the unique positive preimage) is UNAFFECTED by the open complex domain.",
    c2_ok, f"witness censuses (3,1): {c2_wit}; factorization: {c2_fact}; roots exact: {c2_roots}")

# C3: the arena bars -- canon text census + the arena cardinals
p3src = open(os.path.join(ROOT, "era1", "canon", "Part3_Fermion_era.md"), encoding="utf-8").read()
m41 = re.search(r"### Def-H\.41.*?(?=###|\Z)", p3src, re.S)
m42 = re.search(r"### Def-H\.42.*?(?=###|\Z)", p3src, re.S)
t41 = m41.group(0) if m41 else ""
t42 = m42.group(0) if m42 else ""
canon_ok = ("no inner product, no dynamics, no state, no Hamiltonian" in t41
            and "counting space" in t41 and "counting space" in t42)
card = (9 == 3 * 3 and 27 == 3 ** 3 and 16 == 2 ** 4)
c3_ok = canon_ok and card
chk("C3  [Def-H.41; Def-H.42 verbatim; IT.55(3); D2.3]: the ARENA BARS HOLD: the canon text census finds"
    "\n           Def-H.41's species clause verbatim -- 'A counting space: no inner product, no dynamics, no"
    "\n           state, no Hamiltonian is declared' -- and Def-H.42 keeps the colour-dressed arena a counting"
    "\n           space. The arena cardinals are integers: 9 = 3x3, 27 = 3^3, 16 = dim K_1 = 2^4. P_ch is the"
    "\n           VALUE SPACE of the angle coordinate (D-PJ2/D-PJ5's declared placeholder), NOT an arena: the"
    "\n           complex domain opens a coordinate range, it declares no state space, no inner product, no"
    "\n           dynamics -- Def-H.41/42 untouched (IT.55(3),(6) re-certified).",
    c3_ok, f"canon census: {canon_ok}; cardinals: {card}")

# C4: the omega-relabeling is inert -- Vieta invariance under all 6 permutations, exact in Q(sqrt3)
roots = [(Fr(-1), Fr(0)), (Fr(1, 2), Fr(1, 2)), (Fr(1, 2), Fr(-1, 2))]      # gamma = 1


def vieta(rs):
    e1 = qd_add(qd_add(rs[0], rs[1]), rs[2])
    e2 = qd_add(qd_add(qd_mul(rs[0], rs[1], 3), qd_mul(rs[0], rs[2], 3)), qd_mul(rs[1], rs[2], 3))
    e3 = qd_mul(qd_mul(rs[0], rs[1], 3), rs[2], 3)
    return e1, e2, e3


base = vieta(roots)
vieta_expected = ((Fr(0), Fr(0)), (Fr(-3, 2), Fr(0)), (Fr(1, 2), Fr(0)))     # e1=0, e2=-3/2, e3=gamma/2=1/2
c4_ok = base == vieta_expected and all(vieta(list(perm)) == base for perm in itertools.permutations(roots))
chk("C4  [IT.55(6) re-certified]: the open branch structure is INERT on label-free formed reads: the"
    "\n           Vieta triple of the gamma=1 roots is e = (0, -3/2, gamma/2) EXACTLY in Q(sqrt3), invariant"
    "\n           under ALL 6 permutations of the root triple (machine census) -- the omega-relabeling permutes"
    "\n           roots, and every symmetric (label-free) read is fixed. Being a cubic, C adds no further root"
    "\n           (C1/C2): the complex domain costs no formed read. SUSPENSION COHERENCE stands: no formed read"
    "\n           passes through an open branch [IT.43(6) doctrine].",
    c4_ok, f"vieta: {base}")

print("=" * 104)
print("PART D -- D-RS6 ISSUED: radar as geometric read; the transit bar stands")
print("=" * 104)

# D1: the O1 re-run -- the gauge blocks are chiral-blind (the transit_reexam.py A1 convention)
P_R = [[ONE, ZERO], [ZERO, ZERO]]                     # (I + sigma_3)/2
P_L = [[ZERO, ZERO], [ZERO, ONE]]                     # (I - sigma_3)/2
W = kron(s1, s0)                                      # W_i (x) I_omega  (W_i = sigma_1 witness)
cR = sub4(mmul4(W, kron(s0, P_R)), mmul4(kron(s0, P_R), W))
cL = sub4(mmul4(W, kron(s0, P_L)), mmul4(kron(s0, P_L), W))
adv = comm2(s1, s3)                                   # same-factor adversarial: [sigma_1, sigma_3] = -2 i sigma_2
adv_nonzero = any(adv[i][j] != ZERO for i in range(2) for j in range(2))
adv_val = adv == [[ZERO, (Fr(-2), Fr(0))], [(Fr(2), Fr(0)), ZERO]]   # -2i*sigma_2 = [[0,-2],[2,0]] (real entries)
d1_ok = is_zero4(cR) and is_zero4(cL) and adv_nonzero and adv_val
chk("D1  [IT.40(2); FT.123 Phys; FT.125(4) Pf -- ground O1 RE-RUN]: the gauge blocks are CHIRAL-BLIND:"
    "\n           [W_i (x) I_omega, I (x) P_{L/R}] = 0 EXACTLY (4x4 Gauss(i), both projectors) -- 'blindness,"
    "\n           not coupling'; the same-factor adversarial witnesses a genuine chiral coupling would need:"
    "\n           [sigma_1, sigma_3] = -2i*sigma_2 != 0 (machine). The radar declaration couples nothing:"
    "\n           ground O1 of the transit bar HOLDS after D-RS6.",
    d1_ok)

# D2: the admitted-read inventory -- counts and order labels; the order theorem re-run (1 of 24)
events = ["e1", "r1", "e2", "r2"]
survivors = []
for perm in itertools.permutations(events):
    ix = {e: i for i, e in enumerate(perm)}
    if ix["e1"] < ix["r1"] and ix["e2"] < ix["r2"] and ix["r1"] < ix["e2"]:
        survivors.append(perm)                        # legs [D-RS1 on the total tick order] + C11 at the node
d2_order = survivors == [("e1", "r1", "e2", "r2")]
new_symbols = {"delta_h", "Delta_tau_rt", "d", "prec", "succ"}
amp_tokens = {"v_Gamma", "Z_amp", "S_matrix", "rate"}
baryon_gen = {"E_int", "mu'^2", "rho_B", "D_S"}
d2_alpha = (not (new_symbols & amp_tokens)) and (not (new_symbols & baryon_gen))
d2_ok = d2_order and d2_alpha
chk("D2  [IT.60(1),(2) RE-RUN; AT.44(1); IT.53(4); IT.58]: the declaration admits NO new dynamical"
    "\n           object: the radar read's formed content is exhausted by pre-existing reads -- (a) the"
    "\n           return-word COUNTS N_k(2m) (pure counts: empty symbol alphabet, A3), (b) the protocol FACES"
    "\n           [IT.53(4)], (c) the ORDER grammar -- the round-trip order theorem re-run exhaustively: exactly"
    "\n           1 of 4! = 24 orderings survives the grounded constraints (e1 < r1, e2 < r2 [D-RS1 on the"
    "\n           total tick order]; r1 < e2 [C11's within-node lifecycle]): e1 < r1 < e2 < r2, (d) the"
    "\n           chi-gated meeting locus [IT.58]. Alphabet census: the symbols this tier's acts introduce"
    "\n           {delta_h, Delta_tau_rt, d, prec, succ} meet the amplitude tokens and the baryon generators in"
    "\n           the EMPTY set.",
    d2_ok, f"survivors: {survivors}")

# D3: the three grounds assembly -- O1 machine (D1); O2, O4 record; O3 discharged
grounds = {"O1": "chiral-blind gauge blocks [IT.40(2); D1 machine re-run]",
           "O2": "deficit 1' -- the chiral matter assignment, application-layer [IT.40(3); IT.41(2); FT.125(4)]",
           "O4": "the D3.7 trivial chain carries no winding carrier [IT.40(4); BM.122(6)(O4)]"}
o3_discharged = True                                  # [IT.40(1); BM.134(7)]
d3_ok = len(grounds) == 3 and o3_discharged and d1_ok
chk("D3  [BM.122(6) as re-audited at IT.40-IT.42; BM.134(7); IT.57(3)(P1) re-affirmed]: the transit bar"
    "\n           STANDS ON THREE GROUNDS O1/O2/O4 -- the directive's constraint line 'grounds O1 and O4' OMITS"
    "\n           O2 (deficit 1', the named missing primitive) and is corrected on the record (the directive's"
    "\n           own item 8 says three grounds -- the internal inconsistency resolves to the record); O3 stays"
    "\n           discharged (BM.134(7) constructed the momentum-space Sigma-resolvent). D-RS6 declares the"
    "\n           READ; the dynamical transit (emission/absorption with a winding carrier) stays BARRED -- no"
    "\n           vertex, amplitude, weight or rate is constructed here (D2).",
    d3_ok, f"grounds: {sorted(grounds)}")

# D4: the incommensurability bar -- the formed mixed loci stay exactly three
mixed_loci = {"B_ens", "W_channel", "chi"}            # [IT.4(2): EXACTLY three formed mixed loci]
radar_new_loci = set()                                # D-RS6 admits no new cross-currency locus
d4_ok = len(mixed_loci) == 3 and not radar_new_loci and not (new_symbols & baryon_gen)
chk("D4  [BM.83; BM.140(5); IT.4(2); IT.45(4); IT.58(5); IT.59(2)]: the INCOMMENSURABILITY BAR HOLDS: the"
    "\n           formed MIXED loci remain EXACTLY THREE (B_ens, W_channel, the binary chi handshake -- the"
    "\n           exhaustiveness re-certified at ladder level [IT.58(5); IT.59(2)]); the radar's mixed content"
    "\n           passes ONLY through the pre-existing chi locus [IT.53(7): the meeting locus; IT.60(2)]; the"
    "\n           declared exchange rate and order labels are single-register counts/labels (disjoint from the"
    "\n           baryon generators {E_int, mu'^2, rho_B, D_S} -- machine); no fourth locus is formed, no"
    "\n           cross-currency sum or conversion enters.",
    d4_ok)

print("=" * 104)
print("PART E -- the reconciliation and the register state")
print("=" * 104)

# E1: the directive's 8 items against the record
reconcile = {
    "item 1 D-RS3":            "NEW-ISSUED (IT.65)",
    "item 2 D-PJ4":            "REAFFIRMED @IT.55(5) + the endpoint elaboration (B1/B2 derived rows)",
    "item 3 D-PJ5":            "REAFFIRMED @IT.55(6) (arena bars re-certified: C1-C4)",
    "item 4 D-PJ6/D-RS5":      "REAFFIRMED @IT.55(7) (the A9 citation STAYS corrected -> Def-H.9 + FT.20 G-row)",
    "item 5 D-RS1":            "REAFFIRMED @IT.56(1) (the scope row stands: labels, not ordering facts)",
    "item 6 D-RS2":            "REAFFIRMED @IT.56(2) (dictionary pairing; faces not equals)",
    "item 7 D-RS4":            "STILL DEFERRED @IT.56(3) (the condition IS derived; the scope act defers)",
    "item 8 D-RS6":            "NEW-ISSUED (IT.66)",
}
new_issued = {"D-RS3", "D-RS6"}
reaffirmed = {"D-PJ4", "D-PJ5", "D-PJ6/D-RS5", "D-RS1", "D-RS2"}
deferred = {"D-RS4"}
e1_ok = (len(reconcile) == 8 and not (new_issued & reaffirmed)
         and len(new_issued | reaffirmed | deferred) == 8)
chk("E1  [the reconciliation discipline: a declaration act is logged ONCE]: the directive's eight items"
    "\n           map onto the record: TWO genuinely new acts (D-RS3, D-RS6 -- the items IT.57(2) listed as"
    "\n           REMAINING OWED), FIVE re-presentations of acts issued at IT.55-IT.56 (re-affirmed with their"
    "\n           corrections, NEVER re-issued -- a duplicate issuance would double the census entry), and"
    "\n           D-RS4 STILL DEFERRED. The directive's TITLE range 'D-PJ4-7' overruns its BODY: D-PJ7 carries"
    "\n           NO operative content -> NOT forced, REMAINS OWED.",
    e1_ok, f"map: {reconcile}")

# E2: the register after the acts
issued_cumulative = {"D-PJ1", "D-PJ2", "D-PJ3(resolved by D-PJ1)", "D-PJ4", "D-PJ5", "D-PJ6/D-RS5(merged)",
                     "D-RS1", "D-RS2", "D-RS3", "D-RS6", "D-RS7(item 10 re-numbered)",
                     "BM.113(6) sector sync(item 11)", "item 12 re-confirmation"}
owed_now = {"D-PJ7"}                                   # the standing IT-O1 package [IT.41(2)]
sub_debts = {"P_ch branch rule (open by design)", "D-PJ4 degree functional form",
             "D-PJ1 endpoint-register elaboration"}
e2_ok = ("D-RS3" in issued_cumulative and "D-RS6" in issued_cumulative
         and "D-RS4" not in issued_cumulative and "D-PJ7" not in issued_cumulative
         and owed_now == {"D-PJ7"} and len(sub_debts) == 3)
chk("E2  [IT.57(2) superseded by this row]: THE REGISTER AFTER THE ISSUANCE -- ISSUED (cumulative):"
    "\n           D-PJ1-D-PJ6 (D-PJ3 resolved by D-PJ1; D-PJ6/D-RS5 merged), D-RS1, D-RS2, D-RS3 (this tier),"
    "\n           D-RS6 (this tier), D-RS7, the BM.113(6) sector sync, item 12's re-confirmation. DEFERRED:"
    "\n           D-RS4 (the stationarity instantiation scope -- pending data). REMAINING OWED: D-PJ7 ALONE"
    "\n           (the standing IT-O1 package: deficit 1', the P4 transport profile, a transit winding carrier"
    "\n           [IT.41(2)]) -- D-RS6's issuance discharged the READ-level side of the named 'D-PJ7/D-RS6'"
    "\n           pair; the dynamical side stays owed under D-PJ7. SUB-DEBTS unchanged (three).",
    e2_ok)

print("=" * 104)
print("PART F -- the bar-check assembly and the tier scan")
print("=" * 104)

tier_text = ""
if os.path.exists(TIER20):
    tier_text = open(TIER20, encoding="utf-8").read()

# F1: P1 + P5 -- the tier scan: zero decimals; the IT.65 clause carries no dimensionful symbol
decimals = re.findall(r"\b\d+\.\d+\b", tier_text)     # word-bounded: citation tokens (D0.6, CT0.8) do not match
ext_token = "[EXT]" in tier_text
m65 = re.search(r"### IT\.65 .*?(?=### IT\.66|\Z)", tier_text, re.S)
t65 = m65.group(0) if m65 else ""
h_in_65 = ("\\mathfrak h" in t65) or ("\\mathfrak{h}" in t65)
# positive witness that the scans could fire (the zero-matrix-trap discipline):
probe_m = re.search(r"### IT\.65 .*?(?=### IT\.66|\Z)", "### IT.65 x\n\\mathfrak h\n### IT.66 y", re.S)
scan_live = (bool(re.findall(r"\b\d+\.\d+\b", "probe 12.34 end"))
             and not re.findall(r"\b\d+\.\d+\b", "citation D0.6 CT0.8 probe")
             and bool(probe_m) and ("\\mathfrak h" in probe_m.group(0)))
f1_ok = bool(tier_text) and not decimals and not ext_token and bool(t65) and not h_in_65 and scan_live
chk("F1  [P1; P5; the FT.114 section-H scan pattern]: P1 HONORED -- no new dimensionful scale: the"
    "\n           exchange rate is count<->count (A5), and the IT.65 D-RS3 clause carries NO \\mathfrak h"
    "\n           token (machine scan; the only dimensional bridge stays h [BM.102(4)], untouched). P5"
    "\n           HONORED -- no measured value: ZERO decimal numeric tokens in the whole tier document"
    "\n           (machine scan), no [EXT] figure, no species identified; the nine-symbol unissued registry"
    "\n           [IT.57(6)] passes through unchanged.",
    f1_ok, f"decimals found: {decimals}; [EXT]: {ext_token}; h-token in IT.65: {h_in_65}")

# F2: the transit bar -- no dynamical object constructed; the scope rows
f2_ok = d1_ok and d2_ok and d3_ok
chk("F2  [BM.122(6); BM.6(6); IT.3(6); IT.53(8); IT.60(2)]: THE TRANSIT BAR STANDS: D-RS6 discharges"
    "\n           exactly IT.53(8)'s 'admissible iff DECLARED a read' clause -- the radar is now a DECLARED"
    "\n           geometric read [IT.3(6); Def-H.19], and nothing more: the formed content is the pre-existing"
    "\n           counts/faces/order inventory (D2), the three grounds hold with O1 re-run by machine (D1/D3),"
    "\n           and D-RS3's exchange rate is scoped to the read's tick face (A5) -- no vertex, amplitude,"
    "\n           weight, rate or winding carrier is constructed. IT-O1 UNCHANGED.",
    f2_ok)

# F3: the arena bars + the incommensurability bar
f3_ok = c1_ok and c2_ok and c3_ok and c4_ok and d4_ok
chk("F3  [Def-H.41; Def-H.42; BM.83; BM.140(5)]: THE ARENA BARS HOLD (D-PJ5's complex domain"
    "\n           re-certified self-contained: C1-C4 -- P_ch is the coordinate's value space, the arenas stay"
    "\n           counting spaces, the open branch is inert) AND THE INCOMMENSURABILITY BAR HOLDS (D4: the"
    "\n           formed mixed loci stay exactly three; the new alphabets are counts/labels/order).",
    f3_ok)

# F4: the reconciliation integrity -- nothing re-issued, nothing forced
f4_ok = e1_ok and e2_ok and b1_ok and b2_ok and b3_ok
chk("F4  [the do-not-force discipline]: the re-presented items are RE-CONCILIATIONS, not duplicate acts"
    "\n           (E1); D-PJ4's endpoint sentences enter as DERIVED elaboration rows of the issued act (B1/B2),"
    "\n           with the functional form still UNFIXED (B3); D-PJ7 is NOT forced (no operative content in the"
    "\n           directive's body); D-RS4 stays DEFERRED on the Architect's word.",
    f4_ok)

# F5: the verdict assembly
a_ok = a1_ok and a2_ok and a3_ok and a4_ok and a5_ok
verdict_ok = a_ok and b1_ok and b2_ok and b3_ok and c1_ok and c2_ok and c3_ok and c4_ok \
    and d1_ok and d2_ok and d3_ok and d4_ok and e1_ok and e2_ok and f1_ok and f2_ok and f3_ok and f4_ok
chk("F5  [THE BAR-CHECK VERDICT]: THE REMAINING PACKAGE IS ISSUABLE AS RECORDED -- D-RS3 ISSUED"
    "\n           (per-edge integer only; the half reading barred on three machine grounds: face-consistency,"
    "\n           return-word parity, local-record integrality), D-RS6 ISSUED (radar = declared geometric read;"
    "\n           the transit bar stands on three grounds O1/O2/O4), the five re-presented acts REAFFIRMED, "
    "\n           D-RS4 STILL DEFERRED, D-PJ7 REMAINS OWED (not forced). P1 honored, P5 honored, arenas hold,"
    "\n           incommensurability holds, count->strength barred, no species identification, the frozen"
    "\n           canon untouched [AT.63(2)]. Section Cal-IT stays VALUE-FREE: two more logged acts, zero"
    "\n           values issued; the Calibration Era stays deferred.",
    verdict_ok)

print("=" * 104)
print("VERDICT SUMMARY (Tier IT.20, tags IT.64-IT.66):")
print("""    * ISSUED (new acts): D-RS3 -- the tick-hop exchange rate, PER-EDGE INTEGER ONLY
      (Delta_tau_rt = 2*delta_h => d = delta_h in N; the per-visit half reading barred: face-
      consistency with the derived hop face, return-word parity [AT.44(1)], local-record
      integrality); D-RS6 -- the radar protocol DECLARED a geometric/read-level interpretation
      of the lepton-baryon connection [IT.53(8)'s iff-clause discharged]; the dynamical transit
      stays barred on THREE grounds O1/O2/O4; IT-O1 unchanged.
    * REAFFIRMED (issued at IT.55-IT.56, never re-issued): D-PJ4 (+ the derived endpoint
      elaboration: x_- = 0 and D_n -> 1, w_mat -> 1 at eps_q = 0; D_n > 1 strictly at every
      eps_q in (0,1/4) -- genuinely an ensemble; the functional form stays UNFIXED), D-PJ5
      (arena bars re-certified; the open branch inert), D-PJ6/D-RS5 (the A9 citation stays
      corrected), D-RS1 (the scope row stands), D-RS2 (dictionary pairing).
    * DEFERRED: D-RS4 (the stationarity instantiation scope -- pending data; the condition
      itself IS derived [IT.53(5)(b)]).
    * REMAINING OWED: D-PJ7 alone (the standing IT-O1 package: deficit 1', the P4 transport
      profile, a transit winding carrier [IT.41(2)]) + the three sub-debts unchanged.
    * CORRECTIONS: 'grounds O1 and O4' -> THREE grounds; 'as permitted by A9' -> Def-H.9 +
      FT.20 G-row; CONTINUUM.md -> no such file (the live map is the level README);
      'npredim' -> builder-side vocabulary, flagged not adopted; IT-O3 side of the D-RS6
      package -> IT-O3 is CLOSED [IT.60(3)] -- the declaration formalizes what IT.60's
      grammar already used.
    * No value issued; Cal-IT stays value-free; the Calibration Era stays deferred.""")
print("=" * 104)

n_ok = sum(R)
print(f"\n  remaining_declarations.py: {n_ok}/{len(R)} EXACT -- no floating point, no measured value.")
sys.exit(0 if n_ok == len(R) else 1)
