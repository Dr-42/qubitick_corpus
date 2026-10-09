#!/usr/bin/env python3
"""verify_H_koide_channel.py — companion to FT.89 / FT.90 / FT.91 (Tier F.30).

Exact arithmetic only: Fractions for the bisections and thresholds, Z[sqrt6] for the asymptotic
phase boundary, Decimal for display. The Koide constant is EXTERNAL data [EXT] and is used for no
derivation; no particle is identified.

Asserts:
  * FT.89(1): p*_Gamma(n) for n = 3..10 by rational bisection (width 2^-44) reproducing the
    documented decimals; (p*_n)^2 interlacing 2/3 with the four documented deviations;
    p*_inf = sqrt6/3 exactly in Z[sqrt6] (s^2-4s-2 = 0; s/(1+s) = sqrt6/3; (sqrt6/3)^2 = 2/3);
  * FT.89(2d): CAP SENSITIVITY -- cap 2 gives (p*_inf)^2 -> 0.508004 (P_6/P_8/P_10), cap 4 gives
    B == 1 and hence no interior boundary [FT.70(1)]: 2/3 is the cap-3 value, not a universal;
  * FT.89(4a): charpoly x^2(x^2-3x-3) has exactly one positive root;
  * FT.90(2)-(3): the resolution ladder (budget = delta_h at the saturating schedule; 2^4 = C_cap
    = 16) and the exact thresholds ceil(log2 N) = (11, 7, 3, 21, 16, 9) with merge factors 615/8
    and 395023/4; C10's register-vs-Shannon distinction;
  * FT.90(5): the sign-blindness audit -- FT.15's hypothesis includes equal q (so it never merges
    different-q states), FT.40's q_core -> -q_core under omega, j = |k|/2 and m_hid sign-blind;
  * FT.90(6): ceil(log2 3) = 2 and the Compton-like length's dimension;
  * FT.91(3)-(4): the colour-free minimality clauses are present in H as cited, and the vertex
    support is Aut-covariant (so Sigma(O) is well-defined on a class);
  * inventory: 'Koide' counts 0 in the frozen A-G (the constant is external, never imported).

H16 sections (Tier F.37, FT.109-FT.115 — the Koide channel: the C3-covariant seal bilinear
and the bound-chain mixing angle), appended below the Tier F.30 pass:
  * §A: FT.109 — CT1.7 re-derived on all 9 pairs; sum_i [J_i,K_i] = 2i Sigma entrywise exact
    over Q(i); unique component read on the 16-element CT1.2 basis (exact linear solve:
    coefficient 2i on Sigma, zero on the other 15); E_{++} landing (S,T parity); not in span{W_k};
  * §B: FT.109(2) — E^{ii} = sigma_i (x) sigma_i; sum_i E^{ii} = Sigma; sum_i Ehat^{ii} = 0;
  * §C: FT.110(2) — T(1) rebuilt from FT.68(2)'s transfer rule; charpoly x^2(x^2-3x-3) by exact
    permutation expansion; tr T(1) = 3 (Vieta); Newton row (3,15,54,207) = FT.68(2)'s counts;
  * §D: FT.111 — the inner C3 rotation U = u (x) u, u = (I - i(s1+s2+s3))/2 exact over Q(i)
    (U^3 = I; J,K cyclic; Sigma fixed; Ehat cycles; bilinear equivariance on all 9 pairs);
    the doublet witness (P^3 = I; minimal polynomial x^2+x+1 on the zero-sum plane; irreducible
    over Q); comm(P) = span{I,P,P^2} (exact nullity 3); the Hermitian-circulant charpoly identity
    (x-a)^3 - 3|z|^2(x-a) - 2Re(z^3) at 24 exact rational points (Zariski-dense); the symbolic
    ring Q(sqrt3)[A,B,x,c,s]/(c^2+s^2-1): sum cos = 0, sum cos^2 = 3/2 for arbitrary theta, the
    triple-angle identity, the depressed-cubic product identity, the shift covariance witness;
    the normalization A = 1, B^2 = 2 with (sqrt2)^2 = 2 exact in Q(sqrt2);
  * §E: FT.112 — delta = 2/(3*3) = 2/9 exact; dim F_{J+-} = 3 by exact rank; the three 2/3
    cross-checks exact (Z[sqrt6]; 2 - d(L-2)/L at d=4,L=3; 2/3 = N_charge/N_visible);
  * §F: FT.113 — rational Taylor enclosures of cos(2/9), sin(2/9), cos(2/3) (width < 2^-90),
    integer Newton certificates for sqrt2/sqrt6, monotone Fraction interval arithmetic:
    r_1^2 < r_2^2 < r_0^2 disjoint; sum r = 3; pair sum = 3/2; the depressed cubic
    2y^3 - 3y - sqrt2 cos(2/3) contains 0 at each root; ratio widths < 2^-50; decimal pins;
  * §G: FT.114 — the [EXT] audit (external data enters here only): shortfalls
    206.768/(r_2^2/r_1^2) and 3477.2/(r_0^2/r_1^2) by exact rational interval division
    (widths < 2^-50); both < 1 and > 1 - 2*10^-4; the stated-precision mismatch exact;
  * §H: barred-vocabulary scan of the H16 document (zero particle-name and revision-language
    hits); [EXT] numbers and family vocabulary confined to FT.114/FT.115; document pins.
"""
import os, sys, time, math, re
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

from fractions import Fraction as Fr
from decimal import Decimal, getcontext

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bypasscore import cycle_graph, complete_graph, cube_graph, undirected_from, cap_dp_by_K, automorphisms

getcontext().prec = 60
HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, '..'))
if ARCH:
    _SPLIT_H = ['H_archive/H01_flux_and_fermion.md', 'H_archive/H02_edges_and_spin_charge.md',
                'H_archive/H03_subnetwork_force_and_geometry.md', 'H_archive/H04_aspect_operator_and_spectrum.md',
                'H_archive/H05_floor_families.md', 'H_archive/H06_platonic_and_polygon_floors.md',
                'H_archive/H07_spin_ladder.md', 'H_archive/H08_loops_and_bott.md',
                'H_archive/H09_flicker_and_domains.md', 'H_archive/H10_sm_audit.md',
                'H_archive/H11_gravity_and_koide.md', 'H_archive/H12_chirality_and_form_factor.md',
                'H_archive/H13_registries_and_gaps.md']
if ARCH:
    HDOC = '\n'.join(era_paths.read(_fn)
                     for _fn in _SPLIT_H)
ALLG = "".join(era_paths.read(f) for f in
               ['A_axioms.md', 'B_foundation.md', 'C_geometry.md', 'D_electroweak.md',
                'E_electromagnetic.md', 'F_color.md', 'G_saturation.md'])

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1
t0 = time.time()
def stamp(m): print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")

# ---------------------------------------------------------------- exact Z[sqrt d]
class QD:
    __slots__ = ('a', 'b', 'd')
    def __init__(s, a, b, d): s.a = Fr(a); s.b = Fr(b); s.d = d
    def __add__(s, o): return QD(s.a + o.a, s.b + o.b, s.d)
    def __sub__(s, o): return QD(s.a - o.a, s.b - o.b, s.d)
    def __mul__(s, o):
        if isinstance(o, (int, Fr)): return QD(s.a * o, s.b * o, s.d)
        return QD(s.a * o.a + s.d * s.b * o.b, s.a * o.b + s.b * o.a, s.d)
    __rmul__ = __mul__
    def __eq__(s, o):
        if isinstance(o, (int, Fr)): return s.a == o and s.b == 0
        return s.a == o.a and s.b == o.b and s.d == o.d
    def __repr__(s): return f"{s.a}+{s.b}*sqrt({s.d})"

def Bminus(cap, E2):
    def f(p):
        tot = Fr(0)
        for K, c in enumerate(cap):
            if c: tot += Fr(c) * p ** K * (1 - p) ** (E2 - K)
        return tot - p ** E2
    return f

def pstar(cap, E2, bits=44):
    f = Bminus(cap, E2)
    lo, hi = Fr(0), Fr(1)
    assert f(lo) > 0 and f(hi) < 0, "FT.70(1): B(0)-F(0) = 1 > 0 > B(1)-F(1) = -1"
    for _ in range(bits):
        mid = (lo + hi) / 2
        if f(mid) > 0: lo = mid
        else: hi = mid
    return lo, hi

def caprow(n, c):
    nv, DE = cycle_graph(n)
    return cap_dp_by_K(nv, undirected_from(nv, DE), cap=c), 2 * n

# ---------------------------------------------------------------- FT.89(1)
print("=" * 100)
print("FT.89(1) — the phase boundary, recomputed exactly")
print("=" * 100)
DOC = {3: '0.807901', 4: '0.819671', 5: '0.815219', 6: '0.817028', 7: '0.816269',
       8: '0.816596', 9: '0.816452', 10: '0.816517'}
devs = {}
for n in range(3, 11):
    cap, E2 = caprow(n, 3)
    chk(max(K for K, c in enumerate(cap) if c) <= 3 * n // 2, f"P_{n}: K <= 3V/2 (cap census)")
    lo, hi = pstar(cap, E2)
    chk(hi - lo < Fr(1, 2 ** 40), f"P_{n}: bisection width {float(hi-lo):.2e} < 2^-40")
    d = Decimal(lo.numerator) / Decimal(lo.denominator)
    chk(str(d).startswith(DOC[n][:6]), f"P_{n}: p* = {str(d)[:12]} reproduces FT.70(2)'s {DOC[n]}")
    sq = lo * lo
    devs[n] = Fr(2, 3) - sq
    chk(abs(devs[n]) < Fr(2, 100), f"P_{n}: (p*)^2 within 0.02 of 2/3")
sgn = [(devs[n] > 0) for n in range(3, 11)]
chk(sgn == [True, False] * 4, f"interlacing: odd n below 2/3, even above {sgn} [FT.70(3)]")
chk(abs(devs[3]) > abs(devs[5]) > abs(devs[7]) > abs(devs[9]), "deviations shrink monotonically")
for n, want in ((3, Fr(14, 1000)), (5, Fr(21, 10000)), (7, Fr(4, 10000)), (9, Fr(8, 100000))):
    chk(abs(devs[n] - want) < Fr(1, 10 ** 4), f"P_{n}: deviation {float(devs[n]):.3e} ~ {float(want):.3e}")
# exact asymptote in Z[sqrt6]
s6 = QD(0, 1, 6); s = QD(2, 1, 6)
chk(s * s - 4 * s - QD(2, 0, 6) == QD(0, 0, 6), "s = 2+sqrt6 satisfies s^2-4s-2 = 0 exactly")
num = s * QD(3, -1, 6); den = QD(3, 1, 6) * QD(3, -1, 6)
chk(den == QD(3, 0, 6) and num == QD(0, 1, 6), f"s/(1+s) rationalizes to sqrt6/3: {num}/{den}")
pinf = QD(0, Fr(1, 3), 6)
chk(pinf * pinf == QD(Fr(2, 3), 0, 6), "(sqrt6/3)^2 = 2/3 EXACTLY in Z[sqrt6]")
chk(str(Decimal(6).sqrt() / 3).startswith('0.8164965809277260327324280249'),
    f"sqrt(2/3) = {str(Decimal(6).sqrt()/3)[:34]}...")
stamp("p*_n reproduced for n=3..10 (width 2^-44); interlacing + shrinking deviations; (p*_inf)^2 = 2/3 exact in Z[sqrt6]")

# ---------------------------------------------------------------- FT.89(2d) cap sensitivity
print("\n" + "=" * 100)
print("FT.89(2d) — cap sensitivity: 2/3 is the cap-3 value")
print("=" * 100)
c2 = {}
for n in (6, 8, 10):
    cap, E2 = caprow(n, 2)
    lo, hi = pstar(cap, E2)
    d = Decimal(lo.numerator) / Decimal(lo.denominator)
    c2[n] = d * d
    print(f"    cap 2, P_{n}: p* = {str(d)[:12]}, (p*)^2 = {str(d*d)[:12]}")
    chk(d * d < Decimal('0.5082') and d * d > Decimal('0.5079'), f"cap 2 P_{n}: (p*)^2 ~ 0.508")
chk(max(c2.values()) - min(c2.values()) < Decimal('0.0003'), "cap-2 values converge (P_6 -> P_10)")
chk(abs(c2[10] - Decimal(2) / Decimal(3)) > Decimal('0.15'), "cap-2 limit ~0.508004 != 2/3")
cap4, E2 = caprow(6, 4)
chk(sum(cap4) == 2 ** E2, f"cap 4: every pattern admissible ({sum(cap4)} = 2^{E2}) -> B == 1")
f4 = Bminus(cap4, E2)
# cap 4: every pattern admissible -> B(p) == 1 identically, so B - F = 1 - p^(2E) > 0 on (0,1)
chk(all(f4(Fr(i, 10)) == 1 - Fr(i, 10) ** E2 for i in range(1, 10)), "cap 4: B(p) == 1 identically")
chk(all(f4(Fr(i, 10)) > 0 for i in range(1, 10)),
    "cap 4: B - F = 1 - p^(2E) > 0 on (0,1) -> NO interior boundary [FT.70(1)]")
chk(ALLG.count('C_{\\mathrm{cap}}') >= 3, "C_cap is corpus data [CT0.6]")
stamp("cap 2 -> (p*_inf)^2 ~ 0.508004; cap 4 -> B == 1, no boundary: 2/3 is cap-3 combinatorics, not universal")

# ---------------------------------------------------------------- FT.89(4a)
print("\n" + "=" * 100)
print("FT.89(4a) — the transfer charpoly supplies one positive number, not three")
print("=" * 100)
r1 = (Decimal(3) + Decimal(21).sqrt()) / 2; r2 = (Decimal(3) - Decimal(21).sqrt()) / 2
chk(r1 > 0 and r2 < 0, f"x^2-3x-3 roots: {str(r1)[:10]} (positive), {str(r2)[:11]} (negative)")
chk(abs(r1 + r2 - 3) < Decimal('1e-30') and abs(r1 * r2 + 3) < Decimal('1e-30'), "sum = 3, product = -3")
chk(str(r1)[:10] == '3.79128784', f"lambda_max = (3+sqrt21)/2 = {str(r1)[:12]} [FT.68(2)]")
stamp("charpoly x^2(x^2-3x-3): exactly one positive root -> no three-component mass vector")

# ---------------------------------------------------------------- FT.90(2)-(3) ladder
print("\n" + "=" * 100)
print("FT.90(2)-(3) — the resolution ladder and exact thresholds")
print("=" * 100)
for dh in range(1, 13):
    dtau = -(-dh // 4)
    chk(min(dh, 4 * dtau) == dh, f"saturating schedule: budget(delta_h={dh}) = {dh} bits")
chk([2 ** b for b in range(1, 6)] == [2, 4, 8, 16, 32], "ladder 2,4,8,16,32 alternatives")
chk(2 ** 4 == 16, "at delta_h = 4 the bit budget equals C_cap = 16 registers [CT0.6]")
chk('register cost' in ALLG and '\\log_2|X|' in ALLG, "C10: register cost |X| vs Shannon log2|X| are distinct")
THRESH = [('tetra configs', 1230, 11), ('tetra classes', 70, 7), ('tetra covers', 7, 3),
          ('cube configs', 1580092, 21), ('cube classes', 33564, 16), ('cube covers', 264, 9),
          ('P_8 configs', 42687, 16)]
for name, cnt, want in THRESH:
    got = 0
    while 2 ** got < cnt: got += 1
    chk(got == want == math.ceil(math.log2(cnt)), f"{name}: {cnt} classes need delta_h >= {got}")
chk(Fr(1230, 16) == Fr(615, 8), "tetra merge factor at delta_h=4 is 615/8")
chk(Fr(1580092, 16) == Fr(395023, 4), "cube merge factor at delta_h=4 is 395023/4")
cap8, _ = caprow(8, 3)
chk(sum(cap8) == 42687, f"P_8 admissible configurations = {sum(cap8)}")
stamp("ladder verified; thresholds (11,7,3,21,16,9,16); merge factors 615/8 and 395023/4; C10 distinction present")

# ---------------------------------------------------------------- FT.90(5)-(6)
print("\n" + "=" * 100)
print("FT.90(5)-(6) — sign-blindness audit and the generation-cost question")
print("=" * 100)
if ARCH:
    chk('sharing boundary signature $(\\delta h,\\delta\\tau)$, boundary charge $q$, and $\\Theta_{\\mathrm{int}}$' in HDOC,
        "FT.15's hypothesis INCLUDES equal q -> it never merges different-q states")
    chk('q_{\\mathrm{core}}\\mapsto-q_{\\mathrm{core}}' in HDOC, "FT.40: q_core is omega-odd (sign-sensitive)")
    chk('j=|k|/2' in HDOC, "the spin read is j = |k|/2 (sign-blind)")
    chk('m_{\\mathrm{hid}}=E_{\\mathrm{int}}\\ln2/\\mathfrak h' in HDOC, "m_hid counts edges (sign-blind)")
chk(-(-3 // 1) == 3 and 2 ** 2 >= 3, "three classes are resolvable at delta_h >= 2")
chk(math.ceil(math.log2(3)) == 2, "ceil(log2 3) = 2")
if ARCH:
    chk('4^{|\\mathcal C|}' in HDOC and 'Z-weight' in HDOC or 'not a mass' in HDOC,
        "the amplitude-vs-mass trap flag is in the document")
    chk(HDOC.count('1056') >= 1 and HDOC.count('1109312') >= 1, "FT.87(9)'s refutation of (8,1056,1109312) is on record")
stamp("FT.15 includes equal q; q_core omega-odd; S and m_hid sign-blind -> the chiral merger is NOT forced")

# ---------------------------------------------------------------- FT.91(3)-(4)
print("\n" + "=" * 100)
print("FT.91 — colour-free minimality and the Aut-covariance of the vertex support")
print("=" * 100)
if ARCH:
    chk('\\mathrm{Colour}(\\Sigma)\\ne\\varnothing\\ \\wedge\\ \\mathcal C(\\Sigma;C)=1' in HDOC,
        "FT.20's strong criterion requires Colour(Sigma) nonempty")
    chk('the strong summand $\\equiv0$ whenever $\\mathcal C(\\Sigma;C)=0$' in HDOC,
        "FT.26(2): the strong summand vanishes identically when C = 0")
    chk('Covers contain no *materialized* closed chain' in HDOC,
        "FT.80(6): covers carry no materialized closed chain")
nv, DE = complete_graph(4)
U = undirected_from(nv, DE)
perms = automorphisms(nv, U)
idx = {e: i for i, e in enumerate(DE)}
def supp(mask): return {v for e in DE if (mask >> idx[e]) & 1 for v in e}
tests = [0b1, 0b11, 0b1111, 0b101010101010, (1 << 12) - 1]
for mask in tests:
    for p in perms:
        img = 0
        for i, e in enumerate(DE):
            if (mask >> i) & 1: img |= 1 << idx[(p[e[0]], p[e[1]])]
        chk(supp(img) == {p[v] for v in supp(mask)}, "supp(g R) = g supp(R) (Aut-covariance)")
        chk(len(supp(img)) == len(supp(mask)), "support cardinality is an orbit invariant")
chk(ALLG.count('Koide') == 0, "'Koide' counts 0 in the frozen A-G: the constant was never imported")
if ARCH:
    chk(HDOC.count('[EXT]') >= 1 or 'external' in HDOC, "the document marks external data")
stamp("colour-free minimality clauses present; supp(gR) = g supp(R) verified on 5 patterns x 24 automorphisms; 'Koide' absent from A-G")


# ============================================================================
# H16 (Tier F.37) — THE KOIDE CHANNEL: FT.109–FT.115
# Sections §A–§H below. Exact arithmetic only: C = Q(i) matrices (qmath),
# Fractions, integer charpolys by permutation expansion, the symbolic ring
# Q(sqrt3)[A,B,x,c,s]/(c^2+s^2-1), QD(d) quadratic rings, and rational
# Taylor/Newton enclosures. No floating point in any assertion.
# [EXT] data (FT.114) enters §G only — the audit clause. No particle names.
# ============================================================================
from qmath import C, matmul, matadd, matscale, conj_transpose
from itertools import permutations as _perms

if ARCH:
    H16DOC = era_paths.read('H_archive/H16_koide_channel.md')
    H13DOC = era_paths.read('H_archive/H13_registries_and_gaps.md')

def eqm(A, B):
    return len(A) == len(B) and all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

# ---------------------------------------------------------------- Pauli layer over Q(i)
I2 = [[C(1), C(0)], [C(0), C(1)]]
sg = [I2,
      [[C(0), C(1)], [C(1), C(0)]],
      [[C(0), C(0, -1)], [C(0, 1), C(0)]],
      [[C(1), C(0)], [C(0), C(-1)]]]

def kron2(A, B):
    return [[A[i // 2][k // 2] * B[i % 2][k % 2] for k in range(4)] for i in range(4)]

def commut(A, B):
    return matadd(matmul(A, B), matmul(B, A), -1)

SIG0 = kron2(sg[0], sg[0])
SIG = matadd(matadd(kron2(sg[1], sg[1]), kron2(sg[2], sg[2])), kron2(sg[3], sg[3]))
Wg = [None] + [matscale(matadd(kron2(sg[0], sg[i]), kron2(sg[i], sg[0])), Fr(1, 2)) for i in (1, 2, 3)]
Jg = [None] * 4; Kg = [None] * 4
for (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
    Jg[i] = matscale(matadd(kron2(sg[j], sg[k]), kron2(sg[k], sg[j]), -1), Fr(1, 2))
    Kg[i] = matscale(matadd(kron2(sg[0], sg[i]), kron2(sg[i], sg[0]), -1), Fr(1, 2))
Eij = {(i, j): matscale(matadd(kron2(sg[i], sg[j]), kron2(sg[j], sg[i])), Fr(1, 2))
       for i in (1, 2, 3) for j in (1, 2, 3) if i <= j}
Ehat = {}
for (i, j), M in Eij.items():
    Ehat[(i, j)] = matadd(M, matscale(SIG, Fr(-1, 3))) if i == j else M
BASIS16 = ([('E0', SIG0), ('Sig', SIG)]
           + [(f'Eh{i}{j}', Ehat[(i, j)]) for (i, j) in [(1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]]
           + [(f'W{i}', Wg[i]) for i in (1, 2, 3)]
           + [(f'J{i}', Jg[i]) for i in (1, 2, 3)]
           + [(f'K{i}', Kg[i]) for i in (1, 2, 3)])
# note: Ehat^{33} = -Ehat^{11}-Ehat^{22} (zero-sum diagonal triple, §B) — the CT1.2 basis takes 5 independent traceless elements
sigb = {(mu, nu): kron2(sg[mu], sg[nu]) for mu in range(4) for nu in range(4)}   # trace-orthogonal sigma basis (CT1.1)

# ---------------------------------------------------------------- §A  FT.109: the diagonal contraction
print("\n" + "=" * 100)
print("§A (H16/FT.109) — CT1.7 diagonal contraction: sum_i [J_i,K_i] = 2i Sigma, exact over Q(i)")
print("=" * 100)
# CT1.7 re-derived at the point of use, all nine pairs: [J_i,K_j] = i*(delta_ij Sigma - E^{ij})
for i in (1, 2, 3):
    for j in (1, 2, 3):
        E = Eij[(min(i, j), max(i, j))]
        rhs = matscale(matadd(matscale(SIG, 1 if i == j else 0), E, -1), C(0, 1))
        chk(eqm(commut(Jg[i], Kg[j]), rhs), f"§A CT1.7 re-derived: [J{i},K{j}] = i(delta_{i}{j} Sigma - E^{i}{j})")
X = matadd(matadd(commut(Jg[1], Kg[1]), commut(Jg[2], Kg[2])), commut(Jg[3], Kg[3]))
two_i_Sig = matscale(SIG, C(0, 2))
chk(eqm(X, two_i_Sig), "§A H16.1: sum_i [J_i,K_i] = 2i Sigma entrywise exact over Q(i)")
# 16-element basis: independence + unique component read of X
def flatten(M):
    v = []
    for row in M:
        for z in row:
            v += [z.re, z.im]
    return v
def rankQ(vs):
    rows = [list(map(Fr, v)) for v in vs]
    r = 0
    for c in range(len(rows[0])):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        p = rows[r][c]
        rows[r] = [x / p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
chk(rankQ([flatten(M) for _, M in BASIS16]) == 16, "§A the 16 CT1.2 elements are independent (rank 16 over Q)")
chk(len(BASIS16) == 16, "§A basis count = 16 (E0, Sigma, 5 Ehat, 3 W, 3 J, 3 K)")
# sigma (x) sigma read (trace-orthogonal basis, CT1.1 pattern): X = 2i(S11+S22+S33)
dX = {}
for key, Bm in sigb.items():
    t = sum((Bm[i][j] * X[j][i] for i in range(4) for j in range(4)), C(0))
    if t != C(0):
        dX[key] = t / 4
chk(dX == {(1, 1): C(0, 2), (2, 2): C(0, 2), (3, 3): C(0, 2)},
    "§A sigma-basis read of X: exactly 2i on (1,1),(2,2),(3,3), zero elsewhere")
# named 16-element CT1.2 basis: unique component solve (exact Gauss over Q on re/im parts)
def solve_exact(Amat, bvec):
    n = len(bvec); m = len(Amat[0])
    Mx = [list(Amat[r]) + [bvec[r]] for r in range(n)]
    piv_cols = []; r = 0
    for c in range(m):
        pv = next((i for i in range(r, n) if Mx[i][c] != 0), None)
        if pv is None:
            continue
        Mx[r], Mx[pv] = Mx[pv], Mx[r]
        p0 = Mx[r][c]
        Mx[r] = [x / p0 for x in Mx[r]]
        for i in range(n):
            if i != r and Mx[i][c] != 0:
                f = Mx[i][c]
                Mx[i] = [a - f * b for a, b in zip(Mx[i], Mx[r])]
        piv_cols.append(c); r += 1
        if r == n:
            break
    if r < n and any(Mx[i][m] != 0 and all(Mx[i][c] == 0 for c in range(m)) for i in range(r, n)):
        raise ValueError("inconsistent")
    if len(piv_cols) < m:
        raise ValueError("underdetermined")
    sol = [Fr(0)] * m
    for i, c in enumerate(piv_cols):
        sol[c] = Mx[i][m]
    return sol
Arows = [[] for _ in range(32)]
bvec = []
for i in range(4):
    for j in range(4):
        # real and imaginary part equations of X = sum_B c_B B, c_B in Q(i)
        row_re = []; row_im = []
        for nm, B in BASIS16:
            row_re += [B[i][j].re, -B[i][j].im]
            row_im += [B[i][j].im, B[i][j].re]
        Arows[2 * (4 * i + j)] = row_re
        Arows[2 * (4 * i + j) + 1] = row_im
        bvec += [X[i][j].re, X[i][j].im]
sol = solve_exact(Arows, bvec)
coeffs = {}
for bidx, (nm, B) in enumerate(BASIS16):
    coeffs[nm] = C(sol[2 * bidx], sol[2 * bidx + 1])
chk(coeffs['Sig'] == C(0, 2), "§A H16.1(3): the Sigma coefficient is exactly 2i (scalar coefficient 2)")
chk(all(coeffs[nm] == C(0) for nm, _ in BASIS16 if nm != 'Sig'),
    "§A H16.1(3): all 15 other basis coefficients are exactly 0 (unique solve on the rank-16 basis)")
recon = matscale(SIG0, C(0))
for nm, B in BASIS16:
    recon = matadd(recon, matscale(B, coeffs[nm]))
chk(eqm(recon, X), "§A component read reconstructs X exactly (uniqueness of the basis read)")
# S/T parity: X in E_{++}; W_k have opposite T-parity; X not in span{W_k}
# swap matrix on C^2 (x) C^2: S|ab> = |ba>
SWAP = [[C(0)] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2):
        SWAP[b * 2 + a][a * 2 + b] = C(1)
chk(eqm(matmul(matmul(SWAP, SWAP), [[C(1 if i == j else 0) for j in range(4)] for i in range(4)]),
        [[C(1 if i == j else 0) for j in range(4)] for i in range(4)]), "§A swap^2 = I")
chk(eqm(matmul(matmul(SWAP, X), SWAP), X), "§A H16.1(4): S(X) = X (swap-even)")
chk(eqm(matmul(matmul(SWAP, SIG), SWAP), SIG), "§A S(Sigma) = Sigma")
for i in (1, 2, 3):
    chk(eqm(matmul(matmul(SWAP, Wg[i]), SWAP), Wg[i]), f"§A S(W{i}) = W{i}")
# T grading on the sigma (x) sigma basis: T(s_mu (x) s_nu) = eta^mu eta^nu s_mu (x) s_nu, eta = (-,+,+,+)
eta = [-1, 1, 1, 1]
def decomp(M):
    d = {}
    for key, Bm in sigb.items():
        t = sum((Bm[i][j] * M[j][i] for i in range(4) for j in range(4)), C(0))
        if t != C(0):
            d[key] = t / 4
    return d
def Tact(M):
    out = matscale(SIG0, C(0))
    for (mu, nu), a in decomp(M).items():
        out = matadd(out, matscale(sigb[(mu, nu)], a * eta[mu] * eta[nu]))
    return out
def Sact(M):
    out = matscale(SIG0, C(0))
    for (mu, nu), a in decomp(M).items():
        out = matadd(out, matscale(sigb[(nu, mu)], a))
    return out
chk(all(eqm(sigb[(nu, mu)], matmul(matmul(SWAP, sigb[(mu, nu)]), SWAP))
        for mu in range(4) for nu in range(4)), "§A S-action = swap conjugation on all 16 sigma basis elements")
chk(eqm(Tact(X), X), "§A H16.1(4): T(X) = X  =>  X in E_{++} (Higgs/gravity block)")
for i in (1, 2, 3):
    chk(eqm(Tact(Wg[i]), matscale(Wg[i], -1)), f"§A T(W{i}) = -W{i}: span{{W_k}} lies in E_{{+-}}")
chk(all(coeffs[f'W{i}'] == C(0) for i in (1, 2, 3)) and X != matscale(SIG0, C(0)),
    "§A H16.1(4): zero W-components and X != 0  =>  X not in span{W_k} (direct-sum sectors)")
stamp("§A green: CT1.7 on all 9 pairs; sum = 2iSigma exact; unique basis read (coeff 2i, 15 zeros); E_{++} landing; not in span{W_k}")

# ---------------------------------------------------------------- §B  sum_i E^{ii} = Sigma
print("\n" + "=" * 100)
print("§B (H16/FT.109(2)) — sum_i E^{ii} = sum_i sigma_i (x) sigma_i = Sigma, exact")
print("=" * 100)
acc = matscale(SIG0, C(0))
for i in (1, 2, 3):
    chk(eqm(Eij[(i, i)], kron2(sg[i], sg[i])), f"§B E^{i}{i} = sigma_{i} (x) sigma_{i}")
    acc = matadd(acc, kron2(sg[i], sg[i]))
chk(eqm(acc, SIG), "§B H16.1(2): sum_i E^{ii} = Sigma entrywise exact")
accE = matscale(SIG0, C(0))
for i in (1, 2, 3):
    accE = matadd(accE, Ehat[(i, i)])
chk(eqm(accE, matscale(SIG0, C(0))), "§B sum_i Ehat^{ii} = 0 (the diagonal traceless triple is zero-sum: the doublet plane)")
stamp("§B green: E^{ii} = sigma_i (x) sigma_i; sum = Sigma; sum Ehat^{ii} = 0")

# ---------------------------------------------------------------- §C  tr T(1) = 3 from the charpoly
print("\n" + "=" * 100)
print("§C (H16/FT.110) — tr T(1) = 3 from charpoly T(1) = x^2(x^2-3x-3), exact integers")
print("=" * 100)
states = [(0, 0), (0, 1), (1, 0), (1, 1)]
T1 = [[Fr(1 if sum(sa) + sum(sb) <= 3 else 0) for sb in states] for sa in states]
chk(sum(T1[i][i] for i in range(4)) == Fr(3), "§C tr T(1) = 3 directly from the FT.68(2) transfer rule (only (2,2) excluded)")
def pmul_i(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i2, x in enumerate(a):
        if x:
            for j2, y in enumerate(b):
                if y:
                    out[i2 + j2] += x * y
    return out
def perm_sign(p):
    sgn = 1
    seen = [False] * len(p)
    for i2 in range(len(p)):
        if not seen[i2]:
            j2 = i2; ln = 0
            while not seen[j2]:
                seen[j2] = True; j2 = p[j2]; ln += 1
            if ln % 2 == 0:
                sgn = -sgn
    return sgn
def charpoly_int(M):
    n = len(M)
    xI_T = [[([Fr(-M[i2][j2])] if i2 != j2 else [Fr(-M[i2][j2]), Fr(1)]) for j2 in range(n)] for i2 in range(n)]
    tot = [Fr(0)]
    for p in _perms(range(n)):
        prod = [Fr(perm_sign(p))]
        for i2 in range(n):
            prod = pmul_i(prod, [Fr(c) for c in xI_T[i2][p[i2]]])
        nn = max(len(tot), len(prod))
        tot = [a + b for a, b in zip(tot + [Fr(0)] * (nn - len(tot)), prod + [Fr(0)] * (nn - len(prod)))]
    return tot
ch = charpoly_int(T1)
chk([Fr(c) for c in ch] == [Fr(0), Fr(0), Fr(-3), Fr(-3), Fr(1)],
    "§C charpoly T(1) = x^4 - 3x^3 - 3x^2 by exact permutation expansion")
fact = pmul_i(pmul_i([Fr(0), Fr(1)], [Fr(0), Fr(1)]), [Fr(-3), Fr(-3), Fr(1)])
chk([Fr(c) for c in fact] == [Fr(c) for c in ch], "§C x^2(x^2-3x-3) = x^4-3x^3-3x^2 exactly [FT.68(2)]")
chk(-ch[3] == Fr(3) == sum(T1[i][i] for i in range(4)), "§C H16.2(2): tr T(1) = -[x^3]charpoly = 3 (Vieta, exact)")
def Tpow(n):
    R = [[Fr(1 if i2 == j2 else 0) for j2 in range(4)] for i2 in range(4)]
    for _ in range(n):
        R = [[sum(R[i2][k2] * T1[k2][j2] for k2 in range(4)) for j2 in range(4)] for i2 in range(4)]
    return R
tr_n = [sum(Tpow(n)[i2][i2] for i2 in range(4)) for n in range(1, 5)]
chk(tr_n == [Fr(3), Fr(15), Fr(54), Fr(207)], "§C Newton recursion tr_n = 3tr_{n-1}+3tr_{n-2}: (3,15,54,207) matches FT.68(2)'s P_3,P_4 counts")
chk(3 * tr_n[2] + 3 * tr_n[1] == tr_n[3] and 3 * tr_n[1] + 3 * tr_n[0] == tr_n[2], "§C recursion holds exactly at n=3,4")
stamp("§C green: T(1) rebuilt from the transfer rule; charpoly x^2(x^2-3x-3) exact; tr = 3; Newton row (3,15,54,207)")

# ---------------------------------------------------------------- §D  C3 representation theory
print("\n" + "=" * 100)
print("§D (H16/FT.111) — the C3 action, singlet+doublet, the circulant charpoly, trig normalization")
print("=" * 100)
# (i) the inner C3 rotation: u = (I2 - i(s1+s2+s3))/2, U = u (x) u, exact over Q(i)
u = matscale(matadd(I2, matscale(matadd(matadd(sg[1], sg[2]), sg[3]), C(0, -1))), Fr(1, 2))
chk(u[0][0] * u[1][1] - u[0][1] * u[1][0] == C(1), "§D det u = 1 exact")
U = kron2(u, u); Ud = conj_transpose(U)
I4 = kron2(I2, I2)
chk(eqm(matmul(U, Ud), I4), "§D U unitary exact")
chk(eqm(matmul(matmul(U, U), U), I4), "§D U^3 = I4: the C3 generator, exact over Q(i)")
okJ = all(eqm(matmul(matmul(U, Jg[i]), Ud), Jg[i % 3 + 1]) for i in (1, 2, 3))
okK = all(eqm(matmul(matmul(U, Kg[i]), Ud), Kg[i % 3 + 1]) for i in (1, 2, 3))
chk(okJ, "§D U J_i U^dag = J_{i+1} (CT1.8 exponentiated: the cyclic C3 in SO(3))")
chk(okK, "§D U K_i U^dag = K_{i+1}")
chk(eqm(matmul(matmul(U, SIG), Ud), SIG), "§D U Sigma U^dag = Sigma: the singlet is C3-invariant")
chk(all(eqm(matmul(matmul(U, Eij[(i, i)]), Ud), Eij[(i % 3 + 1, i % 3 + 1)]) for i in (1, 2, 3)),
    "§D U E^{ii} U^dag = E^{i+1,i+1}: cyclic permutation")
chk(all(eqm(matmul(matmul(U, Ehat[(i, i)]), Ud), Ehat[(i % 3 + 1, i % 3 + 1)]) for i in (1, 2, 3)),
    "§D U Ehat^{ii} U^dag = Ehat^{i+1,i+1}")
chk(eqm(matmul(matmul(U, Ehat[(1, 2)]), Ud), Ehat[(2, 3)])
    and eqm(matmul(matmul(U, Ehat[(2, 3)]), Ud), Ehat[(1, 3)])
    and eqm(matmul(matmul(U, Ehat[(1, 3)]), Ud), Ehat[(1, 2)]),
    "§D off-diagonal Ehat cycle: 12 -> 23 -> 13 -> 12")
chk(all(eqm(matmul(matmul(U, commut(Jg[i], Kg[j])), Ud), commut(Jg[i % 3 + 1], Kg[j % 3 + 1]))
        for i in (1, 2, 3) for j in (1, 2, 3)),
    "§D bilinear equivariance: U[J_i,K_j]U^dag = [J_{i+1},K_{j+1}], all 9 pairs")
# (ii) the doublet witness: shift on the zero-sum plane, minimal polynomial x^2+x+1
P3 = [[Fr(0)] * 3 for _ in range(3)]
for k in range(3):
    P3[(k + 1) % 3][k] = Fr(1)          # P e_k = e_{k+1}
def m3mul(A, B):
    return [[sum(A[i2][k2] * B[k2][j2] for k2 in range(3)) for j2 in range(3)] for i2 in range(3)]
I3 = [[Fr(1 if i2 == j2 else 0) for j2 in range(3)] for i2 in range(3)]
chk(eqm(m3mul(m3mul(P3, P3), P3), I3) and sum(P3[i2][i2] for i2 in range(3)) == Fr(0), "§D P^3 = I, tr P = 0")
v1 = [Fr(1), Fr(-1), Fr(0)]; v2 = [Fr(0), Fr(1), Fr(-1)]
def mv(A, v):
    return [sum(A[i2][k2] * v[k2] for k2 in range(3)) for i2 in range(3)]
Pv1 = mv(P3, v1); Pv2 = mv(P3, v2)
# plane matrix in basis (v1,v2): P v1 = v2; P v2 = -v1 - v2
def combo_coeffs(v):
    a = v[0]
    b = -v[2]
    chk([a * v1[t] + b * v2[t] for t in range(3)] == list(v), "§D plane vector expands in (v1,v2)")
    return a, b
a1, b1 = combo_coeffs(Pv1); a2, b2 = combo_coeffs(Pv2)
Mpl = [[a1, a2], [b1, b2]]
chk(Mpl == [[Fr(0), Fr(-1)], [Fr(1), Fr(-1)]], f"§D P|plane in basis (v1,v2) = {Mpl}")
Mpl2 = [[sum(Mpl[i2][k2] * Mpl[k2][j2] for k2 in range(2)) for j2 in range(2)] for i2 in range(2)]
chk([[Mpl2[i2][j2] + Mpl[i2][j2] + I3[i2][j2] for j2 in range(2)] for i2 in range(2)] == [[Fr(0)] * 2 for _ in range(2)],
    "§D (P|plane)^2 + P|plane + I = 0: minimal polynomial x^2+x+1 (P|plane != I)")
chk(all(q * q + q + 1 != 0 for q in (Fr(-1), Fr(0), Fr(1))) and 1 * 1 + 1 + 1 == 3 != 0 and (-1) ** 2 + (-1) + 1 == 1 != 0,
    "§D x^2+x+1 has no rational root (values at +-1 are 3, 1): irreducible over Q => the plane is the doublet")
chk(mv(P3, [Fr(1), Fr(1), Fr(1)]) == [Fr(1), Fr(1), Fr(1)], "§D the (1,1,1) direction is the singlet of P")
# (iii) commutant of P = span{I, P, P^2} (dimension 3, exact Q elimination)
P3sq = m3mul(P3, P3)
# build the 9x9 system (X P - P X = 0) over the entries of X
rows = []
for i2 in range(3):
    for j2 in range(3):
        row = [Fr(0)] * 9
        for k2 in range(3):
            row[i2 * 3 + k2] += P3[k2][j2]      # X_{ik} P_{kj}
            row[k2 * 3 + j2] -= P3[i2][k2]      # P_{ik} X_{kj}
        rows.append(row)
chk(9 - rankQ(rows) == 3, "§D dim_Q comm(P) = 3 (exact nullity of XP-PX)")
chk(all(eqm(m3mul(Bm, P3), m3mul(P3, Bm)) for Bm in (I3, P3, P3sq)), "§D I, P, P^2 commute with P")
chk(rankQ([[c for cell in Bm for c in cell] for Bm in (I3, P3, P3sq)]) == 3, "§D I, P, P^2 independent => basis of comm(P)")
# (iv) Hermitian circulants: charpoly(aI + zP + zbar P^T) = (x-a)^3 - 3|z|^2(x-a) - 2Re(z^3), 24 rational points
pts = [(Fr(0), Fr(0), Fr(0)), (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(1)),
       (Fr(1), Fr(1), Fr(0)), (Fr(1), Fr(0), Fr(1)), (Fr(-2), Fr(1), Fr(-1)), (Fr(Fr(5, 3)), Fr(-1), Fr(2)),
       (Fr(0), Fr(1, 2), Fr(-3, 7)), (Fr(2), Fr(-4, 5), Fr(2, 3)), (Fr(-1), Fr(3, 2), Fr(3, 2)),
       (Fr(7), Fr(-2, 3), Fr(1, 5)), (Fr(0), Fr(-1), Fr(-1)), (Fr(3), Fr(2), Fr(-5)),
       (Fr(Fr(1, 3)), Fr(4, 3), Fr(-1, 7)), (Fr(-5), Fr(0), Fr(3, 4)), (Fr(2), Fr(1, 10), Fr(-9, 10)),
       (Fr(0), Fr(5), Fr(12)), (Fr(1), Fr(-7, 3), Fr(2, 9)), (Fr(-3), Fr(1, 4), Fr(1, 4)),
       (Fr(4), Fr(-1), Fr(-2)), (Fr(Fr(1, 2)), Fr(1, 3), Fr(1, 6)), (Fr(0), Fr(2), Fr(0)), (Fr(-1), Fr(0), Fr(5))]
for (a2, p2, q2) in pts:
    z = C(p2, q2); zb = C(p2, -q2)
    I3c = [[C(Fr(I3[i2][j2])) for j2 in range(3)] for i2 in range(3)]
    P3c = [[C(Fr(P3[i2][j2])) for j2 in range(3)] for i2 in range(3)]
    P3Tc = [[C(Fr(P3[j2][i2])) for j2 in range(3)] for i2 in range(3)]
    H = matadd(matadd(matscale(I3c, a2), matscale(P3c, z)), matscale(P3Tc, zb))
    def tr3(M):
        return sum((M[i2][i2] for i2 in range(3)), C(0))
    def mm3(A, B):
        return [[sum(A[i2][k2] * B[k2][j2] for k2 in range(3)) for j2 in range(3)] for i2 in range(3)]
    H2 = mm3(H, H); H3 = mm3(H2, H)
    p1 = tr3(H); p2t = tr3(H2); p3t = tr3(H3)
    chk(p1.im == 0 and p2t.im == 0 and p3t.im == 0, "§D Hermitian circulant power traces real")
    e1 = p1.re; e2 = (p1.re * p1.re - p2t.re) / 2; e3 = (p1.re ** 3 - 3 * p1.re * p2t.re + 2 * p3t.re) / 6
    zz = p2 * p2 + q2 * q2
    chk(e1 == 3 * a2, f"§D e1 = 3a at (a,p,q)=({a2},{p2},{q2})")
    chk(e2 == 3 * a2 * a2 - 3 * zz, f"§D e2 = 3a^2-3|z|^2 at ({a2},{p2},{q2})")
    chk(e3 == a2 ** 3 - 3 * a2 * zz + 2 * (p2 ** 3 - 3 * p2 * q2 * q2), f"§D e3 = a^3-3a|z|^2+2Re(z^3) at ({a2},{p2},{q2})")
stamp("§D(i-iv) green: inner C3 exact over Q(i); doublet minimal polynomial; comm(P) = span{I,P,P^2}; circulant charpoly identity at 24 exact rational points (Zariski-dense)")


# ---------------------------------------------------------------- §D(v) symbolic trig ring
# R = Q(sqrt3)[A,B,x,c,s]/(c^2+s^2-1). Element = (Rc, Sc) with Rc,Sc c-elements (P0,P1):
# value = (P0 + P1 c) + sqrt3 (Q0 + Q1 c); P* are polys in (A,B,x,s) over Q (dict: exps -> Fr).
def pzero(): return {}
def pconst(q): return {} if q == 0 else {(0, 0, 0, 0): Fr(q)}
def pvar(ix):  # ix: 0=A,1=B,2=x,3=s
    e = [0, 0, 0, 0]; e[ix] = 1
    return {tuple(e): Fr(1)}
def padd(p, q, s=1):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fr(0)) + s * v
        if out[k] == 0: del out[k]
    return out
def pmulq(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            out[k] = out.get(k, Fr(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}
def cmul(e, f):   # c-elements: (P0,P1)*(Q0,Q1) with c^2 = 1 - s^2
    s2 = {(0, 0, 0, 2): Fr(1)}
    e1f1 = pmulq(e[1], f[1])
    p0 = padd(pmulq(e[0], f[0]), e1f1)
    p0 = padd(p0, pmulq(e1f1, s2), -1)          # subtract e1 f1 s^2
    p1 = padd(pmulq(e[0], f[1]), pmulq(e[1], f[0]))
    return (p0, p1)
def cadd(e, f, s=1):
    return (padd(e[0], f[0], s), padd(e[1], f[1], s))
def cconst(q): return (pconst(q), pzero())
CE = (pzero(), pconst(1))                          # the element c
SE = (pvar(3), pzero())                            # the element s
XE = (pvar(2), pzero()); AE = (pvar(0), pzero()); BE = (pvar(1), pzero())
def cscale(e, q): return (pmulq(e[0], pconst(q)), pmulq(e[1], pconst(q)))
def rwrap(e): return (e, (pzero(), pzero()))       # sqrt3-layer: rational part only
def rboth(e1, e3): return (e1, e3)                 # e1 + sqrt3*e3
def radd(z1, z2, s=1): return (cadd(z1[0], z2[0], s), cadd(z1[1], z2[1], s))
def rmul(z1, z2):
    return (cadd(cmul(z1[0], z2[0]), cmul(z1[1], z2[1]), 3),
            cadd(cmul(z1[0], z2[1]), cmul(z1[1], z2[0])))
def rscale(z1, q): return (cscale(z1[0], q), cscale(z1[1], q))
def rzero(): return ((pzero(), pzero()), (pzero(), pzero()))
def rz(z1): return z1 == rzero()
SQ3 = rboth((pzero(), pzero()), (pconst(1), pzero()))
gam = [Fr(1), Fr(-1, 2), Fr(-1, 2)]
tau = [Fr(0), Fr(1, 2), Fr(-1, 2)]
ckel = [radd(rwrap(cscale(CE, g)), rmul(SQ3, rwrap(cscale(SE, -t)))) for g, t in zip(gam, tau)]
# c_k = gamma_k c - sqrt3 tau_k s   == cos(theta + 2 pi k / 3)
s0 = rzero()
for k in range(3):
    s0 = radd(s0, ckel[k])
chk(rz(s0), "§D(v) sum_k cos(theta+2pi k/3) = 0 for arbitrary theta — exact in Q(sqrt3)[c,s]/(c^2+s^2-1)")
s2acc = rzero()
for k in range(3):
    s2acc = radd(s2acc, rmul(ckel[k], ckel[k]))
chk(s2acc == rwrap(cconst(Fr(3, 2))), "§D(v) sum_k cos^2(theta+2pi k/3) = 3/2 for arbitrary theta — exact ring identity")
# triple angle: cos3theta = c*cos2theta - s*sin2theta = 4c^3-3c
cos2 = cadd(cmul(CE, CE), cmul(SE, SE), -1)                 # c^2 - s^2
sin2 = cscale(cmul(CE, SE), 2)                              # 2 s c
cos3a = cadd(cmul(CE, cos2), cmul(SE, sin2), -1)            # c cos2 - s sin2
c3poly = cadd(cscale(cmul(CE, cmul(CE, CE)), 4), cscale(CE, -3))   # 4c^3 - 3c
chk(rz(radd(rwrap(cos3a), rwrap(c3poly), -1)), "§D(v) cos3theta = 4c^3-3c (double-angle steps, exact)")
# product identity: prod_k (x - A - B c_k) = (x-A)^3 - (3B^2/4)(x-A) - (B^3/4) cos3theta
XA = cadd(XE, AE, -1)
lhs = rwrap((pconst(1), pzero()))
for k in range(3):
    fac = radd(rwrap(XA), rmul(rwrap(BE), ckel[k]), -1)
    lhs = rmul(lhs, fac)
XA3 = rmul(rwrap(XA), rmul(rwrap(XA), rwrap(XA)))
term2 = rmul(rscale(rmul(rwrap(BE), rwrap(BE)), Fr(-3, 4)), rwrap(XA))   # -(3B^2/4)(x-A)
term3 = rmul(rmul(rmul(rwrap(BE), rwrap(BE)), rwrap(BE)), rwrap(cos3a))
rhs = radd(radd(XA3, term2), rscale(term3, Fr(-1, 4)))
chk(rz(radd(lhs, rhs, -1)), "§D(v) prod_k (x-A-B cos(theta+2pi k/3)) = (x-A)^3-(3B^2/4)(x-A)-(B^3/4)cos3theta — exact")
# covariance witness: c_k(theta') = c_{k+1}(theta) at theta' = theta + 2pi/3
cp = ckel[1]                                                   # cos(theta+2pi/3)
sp = radd(rwrap(cscale(SE, Fr(-1, 2))), rmul(SQ3, rwrap(cscale(CE, Fr(1, 2)))))   # sin(theta+2pi/3) = -s/2 + (sqrt3/2)c
for k in range(3):
    lhs_k = radd(rscale(cp, gam[k]), rmul(SQ3, rscale(sp, -tau[k])))
    chk(rz(radd(lhs_k, ckel[(k + 1) % 3], -1)), f"§D(v) covariance: cos(theta'+2pi {k}/3) = cos(theta+2pi {k+1}/3) exact")
# ---------------------------------------------------------------- §D(vi) normalization A=1, B=sqrt2
chk(3 * Fr(1) == Fr(3), "§D(vi) trace normalization: sum lambda = 3A = 3 at A = 1 = dim F_J± [CT0.12]")
chk(Fr(3) / Fr(3, 2) == Fr(2), "§D(vi) variance normalization: B^2 = 3/(3/2) = 2 exactly")
q2 = QD(0, 1, 2)
chk(q2 * q2 == QD(2, 0, 2), "§D(vi) (sqrt2)^2 = 2 exact in Q(sqrt2): B = sqrt2")
stamp("§D green (i–vi): inner C3 over Q(i); doublet x^2+x+1; comm(P)=span{I,P,P^2}; circulant charpoly at 24 points; trig identities and A=1, B=sqrt2 exact")

# ---------------------------------------------------------------- §E  FT.112: delta = 2/9
print("\n" + "=" * 100)
print("§E (H16/FT.112) — the mixing angle delta = 2/(3*3) = 2/9, exact rationals")
print("=" * 100)
num_coeff = coeffs['Sig']
chk(num_coeff == C(0, 2) and num_coeff.im == Fr(2), "§E numerator: the Sigma coefficient of sum_i[J_i,K_i] is 2i — scalar 2 exact [FT.109]")
def flatC(M):
    v = []
    for row in M:
        for z in row:
            v += [z.re, z.im]
    return v
dimJ = rankQ([flatC(Jg[i]) for i in (1, 2, 3)])
dimK = rankQ([flatC(Kg[i]) for i in (1, 2, 3)])
chk(dimJ == 3 and dimK == 3, "§E dim F_{J+} = dim F_{J-} = 3 by exact rank [CT0.12 re-derived]")
trT1 = sum(T1[i][i] for i in range(4))
chk(trT1 == Fr(3), "§E tr T(1) = 3 [§C]")
delta = Fr(2) / (Fr(dimJ) * trT1)
chk(delta == Fr(2, 9), "§E H16.4: delta = 2/(3*3) = 2/9 exact")
# cross-check rationals (recorded, not derived equal)
pinf6 = QD(0, Fr(1, 3), 6)
chk(pinf6 * pinf6 == QD(Fr(2, 3), 0, 6), "§E cross-check: (sqrt6/3)^2 = 2/3 exact in Z[sqrt6] [FT.70(3)]")
chk(Fr(2) - Fr(4 * (3 - 2), 3) == Fr(2, 3), "§E cross-check: delta_v/pi = 2 - d(L-2)/L = 2/3 at d=4, L=3 (octahedron) [FT.63(4)]")
chk(Fr(2, 3) == Fr(2) / Fr(3), "§E cross-check: f_charge(delta h=3) = N_charge/N_visible = 2/3 [FT.14]")
chk(Fr(2, 3) / 3 == Fr(2, 9) == delta, "§E delta = (2/3)/3 = 2/9: the cross-check rational over the seal dimension")
stamp("§E green: delta = 2/9 from (FT.109 coefficient 2)/(CT0.12 dim 3 x FT.68(2) trace 3); three 2/3 cross-checks exact")

# ---------------------------------------------------------------- §F  FT.113: exact enclosures
print("\n" + "=" * 100)
print("§F (H16/FT.113) — r_i = 1+sqrt2 cos(2/9+2pi i/3): rational trigonometric enclosures, width 2^-50")
print("=" * 100)
def cos_sin_enc(x, bits):
    """exact (lo,hi) for (cos x, sin x), x rational, |x| <= 1: consecutive alternating
    partial sums bracket; term monotonicity asserted (no floating point)."""
    assert Fr(-1) <= x <= 1
    tgt = Fr(1, 2 ** bits)
    # cos: consecutive alternating partial sums bracket the value (terms decrease for |x| <= 1)
    tc = Fr(1); Sc_prev = Fr(1); k = 0
    while True:
        k += 1
        tc = -tc * x * x / ((2 * k - 1) * (2 * k))
        Sc_new = Sc_prev + tc
        if abs(tc) < tgt:
            lo_c, hi_c = min(Sc_prev, Sc_new), max(Sc_prev, Sc_new)
            break
        Sc_prev = Sc_new
    ts = x; Ss_prev = x; k = 0
    while True:
        k += 1
        ts = -ts * x * x / ((2 * k) * (2 * k + 1))
        Ss_new = Ss_prev + ts
        if abs(ts) < tgt:
            lo_s, hi_s = min(Ss_prev, Ss_new), max(Ss_prev, Ss_new)
            break
        Ss_prev = Ss_new
    return (lo_c, hi_c), (lo_s, hi_s)

def sqrt_enc(nn, bits):
    """exact (lo,hi) for sqrt(nn), nn a positive integer: scaled isqrt with certificates."""
    k2 = bits + 4
    N = nn * (1 << (2 * k2))
    r = math.isqrt(N)
    lo = Fr(r, 1 << k2); hi = Fr(r + 1, 1 << k2)
    assert lo * lo <= nn < hi * hi and hi - lo < Fr(1, 2 ** bits)
    return (lo, hi)

def iadd(I, J): return (I[0] + J[0], I[1] + J[1])
def isub(I, J): return (I[0] - J[1], I[1] - J[0])
def imul(I, J):
    prods = [I[0] * J[0], I[0] * J[1], I[1] * J[0], I[1] * J[1]]
    return (min(prods), max(prods))
def iscl(I, q):
    return (I[0] * q, I[1] * q) if q >= 0 else (I[1] * q, I[0] * q)
def idiv(I, J):
    assert J[0] > 0, "positive denominator interval"
    return (I[0] / J[1], I[1] / J[0])
def iwidth(I): return I[1] - I[0]
def icontains(I, v): return I[0] <= v <= I[1]

BITS = 90
ONE = (Fr(1), Fr(1))
cE, sE = cos_sin_enc(Fr(2, 9), BITS)
sq2 = sqrt_enc(2, BITS)
sq6 = sqrt_enc(6, BITS)
cos23 = cos_sin_enc(Fr(2, 3), BITS)[0]
chk(iwidth(cE) < Fr(1, 2 ** BITS) and iwidth(sE) < Fr(1, 2 ** BITS), "§F cos(2/9), sin(2/9) enclosures at width < 2^-90")
rr0 = iadd(ONE, imul(sq2, cE))                                    # 1 + sqrt2 c
rr1 = isub(ONE, iscl(iadd(imul(sq2, cE), imul(sq6, sE)), Fr(1, 2)))   # 1 - (sqrt2 c + sqrt6 s)/2
rr2 = isub(ONE, iscl(isub(imul(sq2, cE), imul(sq6, sE)), Fr(1, 2)))   # 1 - (sqrt2 c - sqrt6 s)/2
chk(rr1[0] > 0 and rr2[0] > 0, "§F r_1, r_2 strictly positive (enclosure-proven)")
sq0 = imul(rr0, rr0); sq1 = imul(rr1, rr1); sq2i = imul(rr2, rr2)
chk(sq1[1] < sq2i[0] and sq2i[1] < sq0[0], "§F H16.5 ordering r_1^2 < r_2^2 < r_0^2: disjoint enclosures, exact")
qm = idiv(sq2i, sq1); qo = idiv(sq0, sq1)
chk(iwidth(qm) < Fr(1, 2 ** 50) and iwidth(qo) < Fr(1, 2 ** 50), "§F ratio enclosures at width < 2^-50")
rsum = iadd(iadd(rr0, rr1), rr2)
chk(icontains(rsum, Fr(3)), "§F sum r_i = 3 (enclosure contains 3 exactly; FT.111(3) sum identity)")
pp = iadd(imul(rr0, rr1), iadd(imul(rr0, rr2), imul(rr1, rr2)))
chk(icontains(pp, Fr(3, 2)), "§F pair sum r_i r_j = 3/2 (Vieta of the depressed cubic)")
def cubic_at(yI):
    y3 = imul(imul(yI, yI), yI)
    return isub(isub(iscl(y3, 2), iscl(yI, 3)), imul(sq2, cos23))
for nm, rr in (('r_0', rr0), ('r_1', rr1), ('r_2', rr2)):
    pI = cubic_at(isub(rr, ONE))
    chk(icontains(pI, Fr(0)), f"§F 2({nm}-1)^3 - 3({nm}-1) - sqrt2 cos(2/3) = 0: enclosure contains 0")
def pin(I, k, want, name):
    sc = 10 ** k
    flo = int(I[0] * sc); fhi = int(I[1] * sc)
    chk(flo == fhi == want, f"§F pin {name}: floor at 10^-{k} = {want} (lo/hi agree)")
pin(cE, 16, 9754100853894475, "cos(2/9)")
pin(sE, 16, 2203977434561222, "sin(2/9)")
pin(rr0, 15, 2379438171633255, "r_0")
pin(rr1, 15, 40349908219207, "r_1")
pin(rr2, 15, 580211920147537, "r_2")
pin(qm, 12, 206770315972729, "r_2^2/r_1^2")
pin(qo, 9, 3477472837104, "r_0^2/r_1^2")
d10 = Decimal
print(f"    r_0 = {str(d10(rr0[0].numerator)/d10(rr0[0].denominator))[:22]}..., r_1 = {str(d10(rr1[0].numerator)/d10(rr1[0].denominator))[:22]}..., r_2 = {str(d10(rr2[0].numerator)/d10(rr2[0].denominator))[:22]}...")
print(f"    r_2^2/r_1^2 = {str(d10(qm[0].numerator)/d10(qm[0].denominator))[:22]}..., r_0^2/r_1^2 = {str(d10(qo[0].numerator)/d10(qo[0].denominator))[:22]}...")
stamp("§F green: ordering, sum/Vieta, depressed-cubic containment, pins — all exact rational enclosures, width < 2^-50")

# ---------------------------------------------------------------- §G  FT.114: [EXT] audit
print("\n" + "=" * 100)
print("§G (H16/FT.114) — the [EXT] audit: exact shortfall factors (external data enters HERE ONLY)")
print("=" * 100)
EXTm = Fr(206768, 1000); EXTo = Fr(34772, 10)
chk(EXTm == Fr(25846, 125) and EXTo == Fr(17386, 5), "§G [EXT] values in lowest terms: 25846/125, 17386/5")
shm = idiv((EXTm, EXTm), qm); sho = idiv((EXTo, EXTo), qo)
chk(iwidth(shm) < Fr(1, 2 ** 50) and iwidth(sho) < Fr(1, 2 ** 50), "§G shortfall enclosures at width < 2^-50")
chk(shm[1] < 1 and sho[1] < 1, "§G H16.6(2): both shortfalls strictly below 1 (derived ratios exceed [EXT])")
chk(shm[0] > 1 - Fr(2, 10 ** 4) and sho[0] > 1 - Fr(2, 10 ** 4), "§G H16.6(2): both above 1 - 2*10^-4")
om = isub(ONE, shm); oo = isub(ONE, sho)
chk(om[0] > Fr(1, 10 ** 5) and om[1] < Fr(2, 10 ** 5), "§G 1 - shortfall_mid in (10^-5, 2*10^-5) exact")
chk(oo[0] > Fr(7, 10 ** 5) and oo[1] < Fr(9, 10 ** 5), "§G 1 - shortfall_out in (7*10^-5, 9*10^-5) exact")
chk(qm[0] - EXTm > Fr(1, 1000), "§G H16.6(1): r_2^2/r_1^2 - 206.768 > 1/1000: NO match at [EXT]'s stated 6-digit precision")
chk(qo[0] - EXTo > Fr(1, 10), "§G H16.6(1): r_0^2/r_1^2 - 3477.2 > 1/10: NO match at [EXT]'s stated 5-digit precision")
chk(EXTm < qm[0] and EXTo < qo[0], "§G [EXT] values lie strictly below the derived enclosures (disjoint)")
pin(shm, 15, 999988799297817, "shortfall_mid")
pin(sho, 15, 999921541556935, "shortfall_out")
print(f"    shortfall_mid = {str(d10(shm[0].numerator)/d10(shm[0].denominator))[:22]}..., shortfall_out = {str(d10(sho[0].numerator)/d10(sho[0].denominator))[:22]}...")
stamp("§G green: exact rational shortfalls; no match at stated precision; both within 2*10^-4 of 1; audit verdicts (1)-(2) exact")

# ---------------------------------------------------------------- §H  document scan + pins
print("\n" + "=" * 100)
print("§H (H16) — barred-vocabulary scan and document pins")
print("=" * 100)
if ARCH:
    doc = H16DOC
BARRED16 = ['previously', 'formerly', 'this was', 'now this',
            'electron', 'muon', 'tau ', 'quark', 'neutrino',
            'proton', 'neutron', 'pion', 'positron', 'photon', 'gluon']
if ARCH:
    hits = [(w, doc.lower().count(w)) for w in BARRED16 if w.lower() in doc.lower()]
if ARCH:
    chk(not hits, f"§H barred-vocabulary scan of H16: zero hits on particle names and revision language ({hits})")
# section-resolved confinement scans
secs = {}
if ARCH:
    parts = re.split(r'^### ', doc, flags=re.M)[1:]
if ARCH:
    for sp in parts:
        head = sp.split(' —')[0].strip()
        secs[head] = sp
    chk(all(f'FT.{n}' in secs for n in range(109, 116)), "§H sections FT.109..FT.115 all present")
    deriv = ''.join(secs[f'FT.{n}'] for n in range(109, 114))
if ARCH:
    chk('lepton' not in deriv.lower(), "§H family vocabulary confined to the audit clause and the adjudication (absent from FT.109-FT.113)")
    chk('206.768' not in ''.join(secs[f'FT.{n}'] for n in list(range(109, 114)) + [115]),
        "§H [EXT] number 206.768 occurs only inside FT.114")
    chk('3477.2' not in ''.join(secs[f'FT.{n}'] for n in list(range(109, 114)) + [115]),
        "§H [EXT] number 3477.2 occurs only inside FT.114")
    chk(secs['FT.114'].count('[EXT]') >= 4, "§H the [EXT] marker appears in the audit clause")
    chk('lepton' in secs['FT.114'].lower() and 'lepton' in secs['FT.115'].lower(), "§H the audit + adjudication carry the family descriptor")
    for w in ('**Thm.**', '**Req.**', '**Pf.**', '**Phys.**', '**Status.**'):
        chk(all(secs[f'FT.{n}'].count(w) == 1 for n in range(109, 116)), f"§H every FT.109–FT.115 block carries exactly one {w}")
    chk(doc.count('**Status.**') == 8, "§H Status count = 8 (7 theorem blocks + the document header line)")
    chk(doc.count(r'\blacksquare') == 7, "§H 7 proof terminators")
    chk('## Tier F.37' in doc and 'part 16 of 16' in doc, "§H pins: Tier F.37 heading; part 16 of 16")
    chk('P-H16a' in doc and '**(P-H16a)**' in H13DOC, "§H P-H16a flagged in H16 and registered in H13")
    chk(r'=\frac{2}{3\cdot3}=\frac29' in doc, "§H pin: delta = 2/(3*3) = 2/9 displayed")
    chk('206.770315972729' in doc and '3477.472837104' in doc, "§H pins: the derived ratio decimals match §F's floors")
    chk('0.999988799297817' in doc and '0.999921541556935' in doc, "§H pins: the shortfall decimals match §G's floors")
    chk('| Identification with lepton masses | FT.114 | NOT derived (audit only) |' in doc, "§H pin: adjudication row (no identification)")
    chk(r'| Overall scale $\mu$ | — | Free parameter (P4) |' in doc, "§H pin: adjudication row (free scale)")
    chk('verify_H_koide_channel.py' in doc, "§H pin: machine-verification reference")
# split so the era-canon half stays live when H_archive/ is externalized
chk(ALLG.count('Koide') == 0, "§H 'Koide' absent from the frozen A-G era canon")
if ARCH:
    chk(doc.count('Koide') >= 1, "§H the channel name lives in H16")
stamp("§H green: zero barred hits; [EXT] and family vocabulary confined to the audit clause; document pins exact")

print(f"\nverify_H_koide_channel: {N} checks green  ({time.time()-t0:.1f}s) — Tier F.30 (FT.89–FT.91) + H16 §A–§H (Tier F.37, FT.109–FT.115)")

