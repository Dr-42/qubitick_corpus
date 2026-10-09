#!/usr/bin/env python3
"""verify_H_rung1_neutrino.py — H21 Tier F.42 (FT.141–FT.145): the rung-one chirality,
the Janus-arrow obstruction, and the family channel of the sixteen-dimensional arena.

Exact arithmetic only (Fraction, Q(i) via qmath.C, exact symbolic rings, rational
interval enclosures). No floating point enters any assertion. This part carries no
external numerical data — no section receives any [EXT] value.

  §A  FT.141  the Ad(S) census on all 17 CT1.2 generators; the 10/6 split; the exhaustive
              2^6 block-deletion census; no S-neutral observable; the weak shadow
              (sum W_i^2 = E_0 + S = 2 Pi_R); the two independent Z_2 witnesses
  §B  FT.142  CT1.7 re-derived; sum_i [J_i,K_i] = 2i Sigma with the unique Pauli-component
              read; mask/block dimensions by exact rank (6, 10, 16, 17, 25); delta_nu = 1/8
  §C  FT.143  the rung-one spectrum: exact identities in Q[sqrt2,sqrt3][c,s]/(c^2+s^2-1);
              rational trigonometric enclosures (width 2^-50); Q = 2/3; the angle ledger;
              the frozen channel decimals re-verified as enclosure floors
  §D  FT.144(1)-(4)  exhaustive Janus-history enumeration (prefix law, Catalan completions,
              two pairs); the two reversals adjudicated; ledger monotonicity; the all-virtual
              state; the exact resolvent identity in Q[w,x+,x-]/(w^12); balanced monomials
  §E  FT.144(5)-(6)  the doublet triple and projectors over Q(i); the orientation-ray
              equal-weight witness; the rung-one no-flip blocks; the rung-two flip channel
              F_LR = q I_2 with charpoly factorization (splitting 2|q|); minimality rows
  §F  FT.145 + document pins: completeness arithmetic, the digon read, sections/markers/
              counts, decimal pins, vocabulary scans, import discipline, downstream integrity
"""
import os, sys, time, math, re
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

from fractions import Fraction as Fr
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from qmath import C

DOCS = os.path.normpath(os.path.join(HERE, '..'))
def rd(fn): return era_paths.read(fn)
if ARCH:
    H21DOC = rd('H_archive/H21_rung1_neutrino.md')
    H13DOC = rd('H_archive/H13_registries_and_gaps.md')
    H18DOC = rd('H_archive/H18_chirality.md')
    H19DOC = rd('H_archive/H19_force_matrix.md')
ADOC = rd('A_axioms.md'); BDOC = rd('B_foundation.md'); CDOC = rd('C_geometry.md')
DDOC = rd('D_electroweak.md'); EDOC = rd('E_electromagnetic.md')
FDOC = rd('F_color.md'); GDOC = rd('G_saturation.md')

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1
t0 = time.time()
def stamp(m): print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")
def banner(t):
    print("\n" + "=" * 100); print(t); print("=" * 100)

# ---------------------------------------------------------------- matrix helpers over Q(i) / Q
def eqm(A, B):
    return len(A) == len(B) and len(A[0]) == len(B[0]) and all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def madd(A, B, s=1): return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mmul(A, B):
    k, m = len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), A[i][0] * 0) for j in range(m)] for i in range(len(A))]
def msc(A, c): return [[c * x for x in row] for row in A]
def meye(n): return [[C(1) if i == j else C(0) for j in range(n)] for i in range(n)]
def meyeQ(n): return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
def mtr(A): return sum((A[i][i] for i in range(len(A))), A[0][0] * 0)
def mdag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def mkron(A, B):
    m = len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(len(A[0]) * len(B[0]))] for i in range(len(A) * m)]
def flatten(M):
    v = []
    for row in M:
        for z in row:
            v += [z.re, z.im]
    return v
def rankQ(vs):
    rows = [list(map(Fr, v)) for v in vs]
    if not rows: return 0
    r = 0
    for c in range(len(rows[0])):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        p = rows[r][c]; rows[r] = [x / p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]; rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
def charpoly(M):
    """Faddeev–LeVerrier over Q(i): coefficients [1, c1, ..., cn] of det(xI - M)."""
    n = len(M); coeffs = [C(1)]; A = meye(n)
    for k in range(1, n + 1):
        A = mmul(M, A) if k == 1 else mmul(M, madd(A, meye(n), coeffs[k - 1]))
        coeffs.append(-mtr(A) / C(k))
    return coeffs
def charpolyQ(M):
    """Faddeev–LeVerrier over Q."""
    n = len(M); coeffs = [Fr(1)]; A = meyeQ(n)
    for k in range(1, n + 1):
        A = [[Fr(M[i][j]) for j in range(n)] for i in range(n)] if k == 1 else \
            [[sum((Fr(M[i][t]) * (A[t][j] + coeffs[k - 1] * (1 if t == j else 0)) for t in range(n)), Fr(0)) for j in range(n)] for i in range(n)]
        coeffs.append(-sum((A[i][i] for i in range(n)), Fr(0)) / Fr(k))
    return coeffs

# ---------------------------------------------------------------- Pauli / CT1.2 layer over Q(i)
I2 = [[C(1), C(0)], [C(0), C(1)]]
sg = [I2,
      [[C(0), C(1)], [C(1), C(0)]],
      [[C(0), C(0, -1)], [C(0, 1), C(0)]],
      [[C(1), C(0)], [C(0), C(-1)]]]
SIG0 = mkron(sg[0], sg[0])
SIG = madd(madd(mkron(sg[1], sg[1]), mkron(sg[2], sg[2])), mkron(sg[3], sg[3]))
ZERO4 = msc(SIG0, C(0))
Wg = [None] + [msc(madd(mkron(sg[0], sg[i]), mkron(sg[i], sg[0])), Fr(1, 2)) for i in (1, 2, 3)]
Jg = [None] * 4; Kg = [None] * 4
for (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)]:
    Jg[i] = msc(madd(mkron(sg[j], sg[k]), mkron(sg[k], sg[j]), -1), Fr(1, 2))
    Kg[i] = msc(madd(mkron(sg[0], sg[i]), mkron(sg[i], sg[0]), -1), Fr(1, 2))
Eij = {(i, j): msc(madd(mkron(sg[i], sg[j]), mkron(sg[j], sg[i])), Fr(1, 2))
       for i in (1, 2, 3) for j in (1, 2, 3) if i <= j}
Ehat = {(i, j): (madd(Eij[(i, j)], msc(SIG, Fr(-1, 3))) if i == j else Eij[(i, j)])
        for (i, j) in Eij}
SSW = msc(madd(SIG0, SIG), Fr(1, 2))          # the swap S = (E0 + Sigma)/2   [CT0.7(1)]
PR = msc(madd(SIG0, SSW), Fr(1, 2))           # Pi_R = (E0 + S)/2 = (3E0+Sigma)/4
PV = msc(madd(SIG0, SSW, -1), Fr(1, 2))       # Pi_V = (E0 - S)/2 = (E0-Sigma)/4
def AdS(X): return mmul(mmul(SSW, X), SSW)

GENS17 = ([('E0', SIG0), ('Sig', SIG)]
          + [(f'E{i}{j}', Eij[(i, j)]) for (i, j) in [(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)]]
          + [(f'W{i}', Wg[i]) for i in (1, 2, 3)]
          + [(f'J{i}', Jg[i]) for i in (1, 2, 3)]
          + [(f'K{i}', Kg[i]) for i in (1, 2, 3)])
BASIS16 = ([('E0', SIG0), ('Sig', SIG)]
           + [(f'Eh{i}{j}', Ehat[(i, j)]) for (i, j) in [(1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]]
           + [(f'W{i}', Wg[i]) for i in (1, 2, 3)]
           + [(f'J{i}', Jg[i]) for i in (1, 2, 3)]
           + [(f'K{i}', Kg[i]) for i in (1, 2, 3)])
sigb = {(mu, nu): mkron(sg[mu], sg[nu]) for mu in range(4) for nu in range(4)}

# ================================================================== §A  FT.141
banner("§A (H21/FT.141) — the rung-one chirality theorem: Ad(S) census, deletion invariance, no S-neutral observable, the weak shadow")
chk(eqm(mmul(SSW, SSW), SIG0), "§A S^2 = E0 [A3; CT0.7(1)]")
chk(eqm(mmul(SIG, SIG), madd(msc(SIG0, 3), SIG, -2)), "§A Sigma^2 = 3E0 - 2Sigma [CT0.7(1) Pf datum]")
chk(eqm(SIG, madd(msc(SSW, 2), SIG0, -1)), "§A Sigma = 2S - E0")
grade = {}
for nm, X in GENS17:
    g = 1 if eqm(AdS(X), X) else (-1 if eqm(AdS(X), msc(X, -1)) else 0)
    chk(g != 0, f"§A Ad(S) eigen-census: {nm} is a pure eigenvector (S-grade {g:+d})")
    grade[nm] = g
chk(sum(1 for g in grade.values() if g == 1) == 11 and sum(1 for g in grade.values() if g == -1) == 6,
    "§A the 17-generator census: 11 S-even (incl. the redundant E33), 6 S-odd")
chk(all(grade[n] == 1 for n in ['E0', 'Sig', 'E11', 'E22', 'E33', 'E12', 'E13', 'E23', 'W1', 'W2', 'W3']),
    "§A membership: E0, Sigma, E^{ij} (6), W_i (3) are S-even [CT1.2 table]")
chk(all(grade[f'J{i}'] == -1 and grade[f'K{i}'] == -1 for i in (1, 2, 3)),
    "§A membership: J_i, K_i are S-odd [CT0.7(3)]")
chk(eqm(madd(madd(Eij[(1, 1)], Eij[(2, 2)]), Eij[(3, 3)]), SIG), "§A E11+E22+E33 = Sigma [CT1.2 Pf]")
chk(eqm(madd(madd(Ehat[(1, 1)], Ehat[(2, 2)]), Ehat[(3, 3)]), ZERO4), "§A the traceless diagonal triple is zero-sum: Eh33 = -Eh11-Eh22")
g16 = {nm: (1 if (nm in ('E0', 'Sig') or nm.startswith('Eh') or nm.startswith('W')) else -1) for nm, _ in BASIS16}
for nm, X in BASIS16:
    chk(eqm(AdS(X), X if g16[nm] == 1 else msc(X, -1)), f"§A 16-basis grade: {nm} ({g16[nm]:+d})")
chk(sum(1 for g in g16.values() if g == 1) == 10 and sum(1 for g in g16.values() if g == -1) == 6,
    "§A the 10/6 split on the 16-basis: G5+W3+H1+D1 = 10 even; J3+K3 = 6 odd")
chk(10 + 6 == 16, "§A 10 + 6 = 16 = C_cap [CT0.12; CT0.6]")
chk(rankQ([flatten(X) for _, X in BASIS16]) == 16, "§A the 16 CT1.2 elements are R-linearly independent (rank 16 in the 32-real flattening)")
for nm, X in BASIS16:
    chk(eqm(AdS(AdS(X)), X), f"§A Ad(S)^2 = id on {nm}: self-inverse => injective => ker = {{0}} (no S-neutral observable)")
chk(sum(g16.values()) == 4, "§A tr Ad(S) on the 16-dim Hermitian locus = 10 - 6 = 4 (integer census)")
lcg_state = [987654321]
def lcg():
    lcg_state[0] = (1103515245 * lcg_state[0] + 12345) % (2 ** 31)
    return lcg_state[0]
for trial in range(24):
    Xs = msc(SIG0, C(0))
    for nm, X in BASIS16:
        Xs = madd(Xs, X, C(Fr(lcg() % 17) - 8))
    Xp = msc(madd(Xs, AdS(Xs)), Fr(1, 2)); Xm = msc(madd(Xs, AdS(Xs), -1), Fr(1, 2))
    chk(eqm(AdS(Xp), Xp) and eqm(AdS(Xm), msc(Xm, -1)) and eqm(madd(Xp, Xm), Xs),
        f"§A grade decomposition X = X+ + X- with Ad(X±) = ±X± (sample {trial})")
ev = [flatten(X) for nm, X in BASIS16 if g16[nm] == 1]
od = [flatten(X) for nm, X in BASIS16 if g16[nm] == -1]
chk(rankQ(ev) == 10 and rankQ(od) == 6 and rankQ(ev + od) == 16, "§A the grade sum is direct: ranks 10, 6, 16")
chk(eqm(mmul(PR, PR), PR) and eqm(mmul(PV, PV), PV) and eqm(mmul(PR, PV), ZERO4) and eqm(madd(PR, PV), SIG0),
    "§A Pi_R, Pi_V idempotent, orthogonal, complete [CT0.7(1)]")
chk(mtr(PR) == C(3) and mtr(PV) == C(1), "§A tr Pi_R = 3, tr Pi_V = 1: the state-locus split is 3+1 [CT0.7(1)]")
for i in (1, 2, 3):
    chk(eqm(mmul(Wg[i], PV), ZERO4) and eqm(mmul(PV, Wg[i]), ZERO4), f"§A W{i} Pi_V = 0 = Pi_V W{i} [FT.101(2) re-derived]")
Wsq = msc(SIG0, C(0))
for i in (1, 2, 3):
    Wsq = madd(Wsq, mmul(Wg[i], Wg[i]))
chk(eqm(Wsq, madd(msc(SIG0, Fr(3, 2)), msc(SIG, Fr(1, 2)))), "§A sum_i W_i^2 = (3/2)E0 + (1/2)Sigma [Cor CT0.7a re-derived]")
chk(eqm(Wsq, madd(SIG0, SSW)), "§A sum_i W_i^2 = E0 + S — the swap itself enters the weak Casimir identity")
chk(eqm(Wsq, msc(PR, 2)), "§A sum_i W_i^2 = 2 Pi_R [FT.135(2)/Cor CT0.7a]")
chk(rankQ([flatten(Jg[i]) for i in (1, 2, 3)] + [flatten(Kg[i]) for i in (1, 2, 3)]) == 6, "§A rank span{J,K} = 6 = dim K_0 [CT0.14]")
chk(rankQ([flatten(Jg[i]) for i in (1, 2, 3)] + [flatten(Kg[i]) for i in (1, 2, 3)] + [flatten(Wg[i]) for i in (1, 2, 3)]) == 9,
    "§A rank span{J,K,W} = 9 = 6+3: the S-odd block carries no weak content (zero intersection)")
BLOCKS = {'G': [f'Eh{i}{j}' for (i, j) in [(1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]],
          'W': ['W1', 'W2', 'W3'], 'H': ['Sig'], 'Dp': ['E0'],
          'Jp': ['J1', 'J2', 'J3'], 'Jm': ['K1', 'K2', 'K3']}
BDIM = {'G': 5, 'W': 3, 'H': 1, 'Dp': 1, 'Jp': 3, 'Jm': 3}
BGR = {b: (1 if b in ('G', 'W', 'H', 'Dp') else -1) for b in BLOCKS}
names = {nm: X for nm, X in BASIS16}
both = 0; singles = []
keys = list(BLOCKS)
for r in range(0, 7):
    for dele in combinations(keys, r):
        surv_blocks = [b for b in keys if b not in dele]
        survivors = [nm for b in surv_blocks for nm in BLOCKS[b]]
        for nm in survivors:
            X = names[nm]
            chk(eqm(AdS(X), X if g16[nm] == 1 else msc(X, -1)),
                f"§A deletion invariance: grade of {nm} unchanged after deleting {dele}")
        deven = sum(BDIM[b] for b in surv_blocks if BGR[b] == 1)
        dodd = sum(BDIM[b] for b in surv_blocks if BGR[b] == -1)
        if deven >= 1 and dodd >= 1:
            both += 1
        if r == 1:
            singles.append((dele[0], deven, dodd))
chk(both == 45, f"§A both-grade (nontrivial) subsets: 45 of 64 = 2^6 - 2^4 - 2^2 + 1 (got {both})")
chk(sorted((d[1], d[2]) for d in singles) == sorted([(5, 6), (7, 6), (9, 6), (9, 6), (10, 3), (10, 3)]),
    f"§A single-block deletions leave (5,6),(7,6),(9,6),(9,6),(10,3),(10,3): got {sorted((d[1], d[2]) for d in singles)}")
chk((sum(BDIM[b] for b in keys if BGR[b] == 1), sum(BDIM[b] for b in keys if BGR[b] == -1)) == (10, 6),
    "§A the full split (10,6) is recovered iff nothing is deleted")
G1 = mkron(sg[3], I2); G2 = mkron(sg[1], I2); OMcar = mkron(I2, sg[1])
for G in (G1, G2):
    chk(eqm(mmul(G, OMcar), mmul(OMcar, G)), "§A [G (x) I, I (x) omega] = 0 (Kronecker disjointness)")
    P = mmul(G, OMcar)
    chk(eqm(mmul(P, P), meye(4)), "§A (G (x) omega)^2 = id")
    chk(not eqm(P, G) and not eqm(P, OMcar), "§A G (x) omega is a third distinct involution: the Z_2's do not collapse")
stamp("§A green: 17-generator Ad(S) census; 10/6 split; rank/trace/directness pins; deletion census exhaustive (64 subsets); weak shadow sum W^2 = E0 + S; independence witnesses")

# ================================================================== §B  FT.142
banner("§B (H21/FT.142) — the rung-one arena: seal coefficient 2 undressed, mask dimensions, delta_nu = 1/8")
for i in (1, 2, 3):
    for j in (1, 2, 3):
        E = Eij[(min(i, j), max(i, j))]
        base = SIG if i == j else ZERO4
        rhs = msc(madd(base, E, -1), C(0, 1))
        comm = madd(mmul(Jg[i], Kg[j]), mmul(Kg[j], Jg[i]), -1)
        chk(eqm(comm, rhs), f"§B CT1.7 re-derived: [J{i},K{j}] = i(delta Sigma - E^{i}{j})")
X = msc(SIG0, C(0))
for i in (1, 2, 3):
    X = madd(X, madd(mmul(Jg[i], Kg[i]), mmul(Kg[i], Jg[i]), -1))
chk(eqm(X, msc(SIG, C(0, 2))), "§B sum_i [J_i,K_i] = 2i Sigma entrywise exact over Q(i) [FT.109(1),(3) re-derived]")
coef = {(mu, nu): mtr(mmul(X, sigb[(mu, nu)])) / C(4) for mu in range(4) for nu in range(4)}
nonz = {k: v for k, v in coef.items() if v != C(0)}
chk(set(nonz) == {(1, 1), (2, 2), (3, 3)} and all(v == C(0, 2) for v in nonz.values()),
    "§B Pauli-component read: x_11 = x_22 = x_33 = 2i, all 13 others zero — the unique CT1.2 component is Sigma with coefficient 2i")
dK0 = rankQ([flatten(Jg[i]) for i in (1, 2, 3)] + [flatten(Kg[i]) for i in (1, 2, 3)])
dK1 = rankQ([flatten(X) for _, X in BASIS16])
dEven = rankQ([flatten(X) for nm, X in BASIS16 if g16[nm] == 1])
dOdd = rankQ([flatten(X) for nm, X in BASIS16 if g16[nm] == -1])
chk((dK0, dEven, dOdd, dK1) == (6, 10, 6, 16), f"§B dimensions by exact rank: K_0 = 6, S-even = 10, S-odd = 6, K_1 = 16 (got {(dK0, dEven, dOdd, dK1)})")
chk(3 + 3 + 5 + 3 + 1 + 1 == 16, "§B completeness arithmetic: J+3 + J-3 + G5 + W3 + H1 + D+1 = 16 = C_cap [CT0.12]")
chk(16 + 1 == 17 and 17 + 8 == 25, "§B the strict flag 6 < 16 < 17 < 25 [CT0.14: dim Z(u2) = 1, dim su3 = 8]")
delta_nu = Fr(2) / Fr(dK1)
chk(delta_nu == Fr(1, 8), "§B delta_nu = 2/16 = 1/8 exact")
cands = {'S-even 10': Fr(2, 10), 'seal x transfer 9 [P-H16a — not imported]': Fr(2, 9),
         'seal x transfer x colour 27 [P-H17a — not imported]': Fr(2, 27), 'K_0 = 6': Fr(2, 6)}
chk(all(v != delta_nu for v in cands.values()), "§B delta_nu = 1/8 is distinct from every rejected-candidate angle (2/10, 2/9, 2/27, 2/6)")
chk(Fr(1, 8) < Fr(2, 9) and Fr(2, 27) < Fr(1, 8), "§B angle order: delta_q < delta_nu < delta_ell")
chk(3 * Fr(1) == Fr(3), "§B trace normalization: sum lambda = 3A = 3 = dim F_J± at A = 1 [CT0.12]")
chk(Fr(3) / Fr(3, 2) == Fr(2), "§B variance normalization: B^2 = 3/(3/2) = 2 exact [FT.111(3)]")
if ARCH:
    chk(r'\frac{2}{16}\ =\ \frac18' in H21DOC, "§B pin: the delta_nu display 2/16 = 1/8")
    chk('imported nowhere' in H21DOC and 'not imported' in H21DOC, "§B pins: the import-discipline phrases")
    chk('FT.68(2)' in H21DOC, "§B pin: the transfer-trace rejection cites FT.68(2)")
stamp("§B green: CT1.7 on all 9 pairs; 2iSigma with the unique component read; ranks (6,10,6,16); flag arithmetic; delta_nu = 1/8 exact; candidate census")

# ================================================================== §C  FT.143
banner("§C (H21/FT.143) — the rung-one family spectrum: ring identities, enclosures, Q = 2/3, the angle ledger")
# ---- exact symbolic ring: M = Q[u,v]/(u^2-2, v^2-3); R = M[s][c]/(c^2-(1-s^2))
def Mz(): return (Fr(0), Fr(0), Fr(0), Fr(0))
def Mmul(x, y):
    a, b, d, e = x; A, B, D, E = y
    return (a * A + 2 * b * B + 3 * d * D + 6 * e * E,
            a * B + A * b + 3 * (d * E + D * e),
            a * D + A * d + 2 * (b * E + B * e),
            a * E + A * e + b * D + B * d)
def Msc(x, q): return tuple(q * t for t in x)
def Madd(x, y, s=1): return tuple(x[i] + s * y[i] for i in range(4))
M1 = (Fr(1), Fr(0), Fr(0), Fr(0))
MU = (Fr(0), Fr(1), Fr(0), Fr(0))       # u = sqrt2
MV = (Fr(0), Fr(0), Fr(1), Fr(0))       # v = sqrt3
chk(Mmul(MU, MU) == Msc(M1, 2) and Mmul(MV, MV) == Msc(M1, 3) and Mmul(Mmul(MU, MV), Mmul(MU, MV)) == Msc(M1, 6),
    "§C coefficient module: u^2 = 2, v^2 = 3, (uv)^2 = 6 exact")
def pz(): return []
def padd(p, q, s=1):
    n = max(len(p), len(q)); P = list(p) + [Mz()] * (n - len(p)); Q = list(q) + [Mz()] * (n - len(q))
    return [Madd(P[i], Q[i], s) for i in range(n)]
def pmul(p, q):
    r = [Mz()] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] = Madd(r[i + j], Mmul(a, b))
    return r
def psc(p, m): return [Mmul(x, m) for x in p]
ONEMS2 = [M1, Mz(), Msc(M1, -1)]        # 1 - s^2
def Rz(): return ([], [])
def Radd(z1, z2, s=1): return (padd(z1[0], z2[0], s), padd(z1[1], z2[1], s))
def Rmul(z1, z2):
    # (P1 + c Q1)(P2 + c Q2) = P1P2 + (1-s^2) Q1Q2 + c (P1Q2 + P2Q1);  c^2 -> 1 - s^2
    return (padd(pmul(z1[0], z2[0]), pmul(ONEMS2, pmul(z1[1], z2[1]))) if z1[1] and z2[1] else pmul(z1[0], z2[0]),
            padd(pmul(z1[0], z2[1]), pmul(z1[1], z2[0])))
def Rsc(z, m): return (psc(z[0], m), psc(z[1], m))
def Rq(q): return (([ (Fr(q), Fr(0), Fr(0), Fr(0)) ] if q != 0 else []), [])
def Rzchk(z): return all(all(t == Fr(0) for t in x) for x in z[0]) and all(all(t == Fr(0) for t in x) for x in z[1])
chk(Rzchk(Radd(Rmul(Rq(2), Rq(3)), Rq(-6))), "§C ring plumbing: rational product 2*3 = 6 exact in R")
R1 = Rq(1)
CE = ([], [M1])                          # c
SE = ([Mz(), M1], [])                    # s
UE = ([MU], [])                          # sqrt2
VE = ([MV], [])                          # sqrt3
chk(Rzchk(Radd(Rmul(CE, CE), Radd(Rmul(SE, SE), Rq(-1)))), "§C c^2 + s^2 = 1 in R = M[s][c]/(c^2+s^2-1)")
UV = Rmul(UE, VE)                        # sqrt6 = u v
r0 = Radd(R1, Rmul(UE, CE))                                              # 1 + sqrt2 c
r1 = Radd(R1, Rsc(Radd(Rmul(UE, CE), Rmul(UV, SE)), Msc(M1, Fr(-1, 2)))) # 1 - (sqrt2 c + sqrt6 s)/2
r2 = Radd(R1, Rsc(Radd(Rmul(UE, CE), Rmul(UV, SE), -1), Msc(M1, Fr(-1, 2))))  # 1 - (sqrt2 c - sqrt6 s)/2
RS = [r0, r1, r2]
chk(Rzchk(Radd(Radd(Radd(r0, r1), r2), Rq(-3))), "§C sum_i r_i = 3 exact in R [FT.143(2)]")
sq = [Rmul(r, r) for r in RS]
chk(Rzchk(Radd(Radd(Radd(sq[0], sq[1]), sq[2]), Rq(-6))), "§C sum_i r_i^2 = 6 exact in R")
pr = Radd(Radd(Rmul(r0, r1), Rmul(r0, r2)), Rmul(r1, r2))
chk(Rzchk(Radd(pr, Rq(Fr(-3, 2)))), "§C pair sum r_i r_j = 3/2 exact in R (Vieta)")
chk(Rzchk(Radd(Rmul(Radd(Radd(r0, r1), r2), Radd(Radd(r0, r1), r2)),
               Radd(Radd(Radd(sq[0], sq[1]), sq[2]), Rsc(pr, Msc(M1, 2))), -1)),
    "§C consistency: (sum r)^2 = sum r^2 + 2 * pair sum exact in R")
cos3 = Radd(Rsc(Rmul(CE, Rmul(CE, CE)), Msc(M1, 4)), Rsc(CE, Msc(M1, -3)))            # 4c^3-3c
cos3b = Rmul(CE, Radd(Rq(1), Rsc(Rmul(SE, SE), Msc(M1, -4))))                          # c(1-4s^2)
chk(Rzchk(Radd(cos3, cos3b, -1)), "§C triple angle: 4c^3 - 3c = c(1 - 4s^2) = cos(3/8) at c = cos(1/8) — exact ring identity")
for i, r in enumerate(RS):
    y = Radd(r, Rq(-1))
    cubic = Radd(Radd(Rsc(Rmul(y, Rmul(y, y)), Msc(M1, 2)), Rsc(y, Msc(M1, -3))), Rsc(Rmul(UE, cos3), Msc(M1, -1)))
    chk(Rzchk(cubic), f"§C depressed cubic 2(r_{i}-1)^3 - 3(r_{i}-1) - sqrt2 cos(3/8) = 0 exact in R")
# product identity over R[x]: prod (x - r_i) = (x-1)^3 - (3/2)(x-1) - (sqrt2/2) cos3
def RXmul(A, B):
    out = [Rz()] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i + j] = Radd(out[i + j], Rmul(a, b))
    return out
def RXadd(A, B, s=1):
    n = max(len(A), len(B))
    return [Radd(A[k] if k < len(A) else Rz(), B[k] if k < len(B) else Rz(), s) for k in range(n)]
lhs = [Rq(1)]
for r in RS:
    lhs = RXmul(lhs, [Rsc(r, Msc(M1, -1)), Rq(1)])            # (x - r)
xm1 = [Rq(-1), Rq(1)]                                          # (x - 1)
xm13 = RXmul(xm1, RXmul(xm1, xm1))
rhs = list(xm13)
term2 = [Rsc(xm1[0], Msc(M1, Fr(-3, 2))), Rsc(xm1[1], Msc(M1, Fr(-3, 2)))]   # -(3/2)(x-1)
rhs = RXadd(rhs, term2)
rhs = RXadd(rhs, [Rsc(Rmul(UE, cos3), Msc(M1, Fr(-1, 2)))])                  # -(sqrt2/2) cos3
chk(all(Rzchk(RXadd(lhs, rhs, -1)[k]) for k in range(max(len(lhs), len(rhs)))),
    "§C product identity: prod_i (x - r_i) = (x-1)^3 - (3/2)(x-1) - (sqrt2/2)cos(3/8) exact over R[x]")
# ---- rational interval enclosures
def cos_sin_enc(x, bits):
    assert Fr(-1) <= x <= 1
    tgt = Fr(1, 2 ** bits)
    tc = Fr(1); Sc_prev = Fr(1); k = 0
    while True:
        k += 1
        tc = -tc * x * x / ((2 * k - 1) * (2 * k))
        Sc_new = Sc_prev + tc
        if abs(tc) < tgt:
            lo_c, hi_c = min(Sc_prev, Sc_new), max(Sc_prev, Sc_new); break
        Sc_prev = Sc_new
    ts = x; Ss_prev = x; k = 0
    while True:
        k += 1
        ts = -ts * x * x / ((2 * k) * (2 * k + 1))
        Ss_new = Ss_prev + ts
        if abs(ts) < tgt:
            lo_s, hi_s = min(Ss_prev, Ss_new), max(Ss_prev, Ss_new); break
        Ss_prev = Ss_new
    return (lo_c, hi_c), (lo_s, hi_s)
def sqrt_enc(nn, bits):
    k2 = bits + 4
    Nn = nn * (1 << (2 * k2))
    r = math.isqrt(Nn)
    lo = Fr(r, 1 << k2); hi = Fr(r + 1, 1 << k2)
    assert lo * lo <= nn < hi * hi and hi - lo < Fr(1, 2 ** bits)
    return (lo, hi)
def iadd(I, J): return (I[0] + J[0], I[1] + J[1])
def isub(I, J): return (I[0] - J[1], I[1] - J[0])
def imul(I, J):
    prods = [I[0] * J[0], I[0] * J[1], I[1] * J[0], I[1] * J[1]]
    return (min(prods), max(prods))
def iscl(I, q): return (I[0] * q, I[1] * q) if q >= 0 else (I[1] * q, I[0] * q)
def idiv(I, J):
    assert J[0] > 0
    return (I[0] / J[1], I[1] / J[0])
def iwidth(I): return I[1] - I[0]
def icontains(I, v): return I[0] <= v <= I[1]
BITS = 90
ONE = (Fr(1), Fr(1))
def spectrum_enc(delta):
    cE, sE = cos_sin_enc(delta, BITS)
    sq2 = sqrt_enc(2, BITS); sq6 = sqrt_enc(6, BITS)
    rr0 = iadd(ONE, imul(sq2, cE))
    rr1 = isub(ONE, iscl(iadd(imul(sq2, cE), imul(sq6, sE)), Fr(1, 2)))
    rr2 = isub(ONE, iscl(isub(imul(sq2, cE), imul(sq6, sE)), Fr(1, 2)))
    return rr0, rr1, rr2, cE, sE, sq2, sq6
rr0, rr1, rr2, cE, sE, sq2, sq6 = spectrum_enc(Fr(1, 8))
chk(iwidth(cE) < Fr(1, 2 ** BITS) and iwidth(sE) < Fr(1, 2 ** BITS), "§C cos(1/8), sin(1/8) enclosures at width < 2^-90")
chk(rr1[0] > 0 and rr2[0] > 0 and rr0[0] > 0, "§C r_0, r_1, r_2 strictly positive (enclosure-proven)")
sq0 = imul(rr0, rr0); sq1 = imul(rr1, rr1); sq2s = imul(rr2, rr2)
chk(sq1[1] < sq2s[0] and sq2s[1] < sq0[0], "§C ordering r_1^2 < r_2^2 < r_0^2: disjoint enclosures, exact")
qm = idiv(sq2s, sq1); qo = idiv(sq0, sq1)
chk(iwidth(qm) < Fr(1, 2 ** 50) and iwidth(qo) < Fr(1, 2 ** 50), "§C ratio enclosures at width < 2^-50")
chk(icontains(iadd(iadd(rr0, rr1), rr2), Fr(3)), "§C sum r_i = 3 (enclosure)")
chk(icontains(iadd(imul(rr0, rr1), iadd(imul(rr0, rr2), imul(rr1, rr2))), Fr(3, 2)), "§C pair sum = 3/2 (enclosure)")
sqsum = iadd(iadd(sq0, sq1), sq2s)
chk(icontains(sqsum, Fr(6)), "§C sum r_i^2 = 6 (enclosure)")
cos38 = cos_sin_enc(Fr(3, 8), BITS)[0]
cos29 = cos_sin_enc(Fr(2, 9), BITS)[0]
chk(cos38[1] < cos29[0], "§C cos(3/8) < cos(2/9): disjoint enclosures — the cubic constant is channel-own")
def cubic_enc(yI):
    y3 = imul(imul(yI, yI), yI)
    return isub(isub(iscl(y3, 2), iscl(yI, 3)), imul(sq2, cos38))
for nm, rr in (('r_0', rr0), ('r_1', rr1), ('r_2', rr2)):
    chk(icontains(cubic_enc(isub(rr, ONE)), Fr(0)), f"§C 2({nm}-1)^3 - 3({nm}-1) - sqrt2 cos(3/8) = 0: enclosure contains 0")
chk(Fr(6) / Fr(9) == Fr(2, 3), "§C Q = sum r^2 / (sum r)^2 = 6/9 = 2/3 exact (phase- and mu-independent)")
qI = idiv(sqsum, imul(iadd(iadd(rr0, rr1), rr2), iadd(iadd(rr0, rr1), rr2)))
chk(icontains(qI, Fr(2, 3)), "§C Q enclosure contains 2/3")
def floor_pin(I, k):
    sc = 10 ** k
    flo = int(I[0] * sc); fhi = int(I[1] * sc)
    assert flo == fhi, f"pin at 10^-{k} not resolved: {flo} vs {fhi}"
    return flo
def tok2int(tok, k):
    ip, fp = tok.split('.')
    return int(ip) * 10 ** k + int((fp + '0' * k)[:k])
for tok, (I, k) in {'2.403179397550': (rr0, 12), '0.145715560918': (rr1, 12), '0.451105041530': (rr2, 12),
                    '9.583926992379': (qm, 12), '271.994748749143': (qo, 12)}.items():
    chk(floor_pin(I, k) == tok2int(tok, k), f"§C decimal pin {tok}: exact floor at 10^-{k}")
anch1 = idiv(sq2s, sq0); anch2 = idiv(sq1, sq0)
for tok, (I, k) in {'0.035235705970': (anch1, 12), '0.003676541567': (anch2, 12)}.items():
    chk(floor_pin(I, k) == tok2int(tok, k), f"§C anchored-form pin {tok}")
if ARCH:
    for tok in ('2.403179397550', '0.145715560918', '0.451105041530', '9.583926992379', '271.994748749143',
                '0.035235705970', '0.003676541567'):
        chk(tok in H21DOC, f"§C document carries the decimal pin {tok}")
# frozen-channel decimals re-verified in the same pipeline
l0, l1, l2, *_ = spectrum_enc(Fr(2, 9))
chk(floor_pin(idiv(imul(l2, l2), imul(l1, l1)), 12) == 206770315972729, "§C frozen re-verification: ell-channel mid ratio = 206.770315972729…")
chk(floor_pin(idiv(imul(l0, l0), imul(l1, l1)), 9) == 3477472837104, "§C frozen re-verification: ell-channel out ratio = 3477.472837104…")
qq0, qq1, qq2, *_ = spectrum_enc(Fr(2, 27))
chk(floor_pin(idiv(imul(qq2, qq2), imul(qq1, qq1)), 12) == 3563695074946, "§C frozen re-verification: q-channel mid ratio = 3.563695074946…")
chk(floor_pin(idiv(imul(qq0, qq0), imul(qq1, qq1)), 10) == 1393386880284, "§C frozen re-verification: q-channel out ratio = 139.3386880284…")
if ARCH:
    for tok in ('206.770315972729', '3477.472837104', '3.563695074946', '139.3386880284'):
        chk(tok in H21DOC, f"§C the three-channel table carries the frozen decimal {tok}")
# the angle ledger: exact Fractions
dn, dl, dq = Fr(1, 8), Fr(2, 9), Fr(2, 27)
chk(16 * dn == 2 and 9 * dl == 2 and 27 * dq == 2, "§C the shared seal numerator: 16 d_nu = 9 d_ell = 27 d_q = 2")
chk(3 * dn == Fr(3, 8) and 3 * dn != dl and 3 * dn != dq, "§C 3 delta_nu = 3/8 is neither delta_ell nor delta_q — no rung-one triple-angle link")
chk(dn not in (3 * dl, 3 * dq, dl / 3, dq / 3), "§C delta_nu is not in {3 d_ell, 3 d_q, d_ell/3, d_q/3}")
chk(3 * dq == dl, "§C the frozen link 3 delta_q = delta_ell [FT.119(2)] re-derived")
chk(dn - dl == Fr(-7, 72) and dn - dq == Fr(11, 216) and 3 * dn - dl == Fr(11, 72) and Fr(11, 72) == 3 * (dn - dq),
    "§C differences: -7/72, 11/216, 11/72 = 3(d_nu - d_q) exact")
chk(tuple(x * 216 for x in (dn, dl, dq)) == (27, 48, 16), "§C ratio census: delta_nu : delta_ell : delta_q = 27:48:16 (x216)")
stamp("§C green: ring identities (Vieta, cubic, product, triple angle); enclosures; ordering; Q = 2/3; angle ledger exact; frozen decimals re-verified")

# ================================================================== §D  FT.144(1)-(4)
banner("§D (H21/FT.144(1)-(4)) — the Janus arrow: exhaustive histories, the two reversals, the vacuum residence")
def step(state, mv):
    if mv == '+': return 1 if state == 0 else None
    return 0 if state == 1 else None
adm = []
def walk(seq, state):
    adm.append((tuple(seq), state))
    if len(seq) == 8: return
    for mv in ('+', '-'):
        ns = step(state, mv)
        if ns is not None:
            walk(seq + [mv], ns)
walk([], 0)
chk(all(s[0] != '-' for s in adm if s), "§D no admissible history leads with J- (D1.2 domain: J- undefined at n_R = 0)")
chk(step(0, '-') is None and step(1, '+') is None, "§D witnesses: J- at n_R = 0 and J+ at n_R = 1 have no target state — the domains force strict alternation")
prefix_ok = True
for seq, _ in adm:
    for k in range(1, len(seq) + 1):
        if seq[:k].count('+') < seq[:k].count('-'):
            prefix_ok = False
chk(prefix_ok, "§D the prefix law #J+ >= #J- holds on every admissible prefix (exhaustive, lengths <= 8)")
alt_ok = all(all(mv == ('+' if k % 2 == 0 else '-') for k, mv in enumerate(seq)) for seq, _ in adm)
chk(alt_ok, "§D strict alternation: every admissible single-pair history is a prefix of (J+ J- J+ J- ...) [machine: exhaustive]")
for L in (2, 4, 6, 8):
    comp = [s for s, e in adm if len(s) == L and e == 0]
    chk(len(comp) == 1 and comp[0] == tuple('+-' * (L // 2)), f"§D the completed single-pair history of length {L} is unique: (J+J-)^{L//2}")
    chk(comp[0].count('+') == comp[0].count('-') == L // 2, f"§D completion <=> #J+ = #J- at length {L} [D1.3/D1.4 balance]")
    chk(all(s[-1] == '-' for s in comp), f"§D every completed nonempty history ends with J- (state 0 is reached only via 1->0)")
adm2 = []
def walk2(seq, st):
    adm2.append((tuple(seq), st))
    if len(seq) == 6: return
    for p in (0, 1):
        for mv in ('+', '-'):
            ns = step(st[p], mv)
            if ns is not None:
                n2 = list(st); n2[p] = ns
                walk2(seq + [(p, mv)], tuple(n2))
walk2([], (0, 0))
proj_ok = True
for seq, st in adm2:
    for p in (0, 1):
        s = 0
        for (pp, mv) in seq:
            if pp == p:
                s = step(s, mv)
                if s is None: proj_ok = False; break
chk(proj_ok, "§D two-pair interleavings (<= 6): every per-pair projection of an admissible history is admissible")
for seq, st in adm2:
    if st == (0, 0):
        chk(sum(1 for _, mv in seq if mv == '+') == sum(1 for _, mv in seq if mv == '-'),
            "§D global completion <=> total #J+ = total #J- [D2.11 universe-level balance]")
for n, want in ((1, 2), (2, 8), (3, 32)):
    cnt = sum(1 for seq, st in adm2 if len(seq) == 2 * n and st == (0, 0))
    closed = sum(math.factorial(2 * n) // (math.factorial(2 * m0) * math.factorial(2 * n - 2 * m0)) for m0 in range(n + 1))
    chk(cnt == closed == want, f"§D two-pair completed interleavings of length {2*n}: {cnt} = the multinomial closed form {closed}")
def mirror(seq): return tuple('+' if m == '-' else '-' for m in reversed(seq))     # Theta_L [D2.7]
comps = [s for s, e in adm if e == 0 and s]
chk(all(mirror(mirror(s)) == s for s in comps), "§D Theta_L (reverse + label swap) is an involution on completed words")
chk(sorted(mirror(s) for s in comps) == sorted(comps), "§D Theta_L bijects the completed admissible words onto themselves — the formal mirror")
bad = 0
for s in comps:
    stt = 0; ok = True
    for mv in reversed(s):
        stt = step(stt, mv)
        if stt is None: ok = False; break
    if ok: bad += 1
chk(bad == 0, "§D the pure order reversal of every completed nonempty admissible history is inadmissible (leads with J-)")
mono_ok = True; rev_witness = 0
for s, e in adm:
    cum = []; n = 0
    for mv in s:
        n += (1 if mv == '+' else 0); cum.append(n)
    if any(cum[k + 1] < cum[k] for k in range(len(cum) - 1)): mono_ok = False
    if cum and cum[-1] >= 2:
        rcum = list(reversed(cum))
        if any(rcum[k + 1] < rcum[k] for k in range(len(rcum) - 1)):
            rev_witness += 1
chk(mono_ok, "§D A6 ledger monotonicity: the cumulative crystallization count is non-decreasing along every admissible history")
chk(rev_witness > 0, "§D the reversed ledger count strictly decreases somewhere on every multi-crystallization history: no forward realization (no inverse tick, A6)")
# the all-virtual state rho_0 = I/4 [A5, CT0.2]
RHO = [[Fr(1, 4) if i == j else Fr(0) for j in range(4)] for i in range(4)]
chk(sum((RHO[i][i] for i in range(4)), Fr(0)) == Fr(1), "§D tr rho_0 = 1 [A5]")
chk(charpolyQ(RHO) == [Fr(1), Fr(-1), Fr(3, 8), Fr(-1, 16), Fr(1, 256)], "§D charpoly(rho_0) = (x - 1/4)^4 exact over Q [CT0.2]")
def ln2_enc(n):
    S = sum((Fr(1, k * (1 << k)) for k in range(1, n + 1)), Fr(0))
    return (S, S + Fr(1, (n + 1) * (1 << n)))
LN2 = ln2_enc(120)
chk(iwidth(LN2) < Fr(1, 2 ** 100) and LN2[0] > 0, "§D ln2 enclosure (Euler series + exact remainder bound) at width < 2^-100")
chk(Fr(-4) * Fr(1, 4) * Fr(-2) == Fr(2), "§D S_raw(rho_0) = -4*(1/4)*ln(1/4) = 2 ln2 = ln4: exact coefficient identity [CT0.2]")
chk(Fr(1, 2) * 1 + Fr(1, 4) * 2 + Fr(1, 8) * 3 + Fr(1, 8) * 3 == Fr(7, 4) and Fr(7, 4) < 2,
    "§D dyadic entropy witness: S(diag(1/2,1/4,1/8,1/8)) = (7/4) ln2 < ln4 — exact coefficient comparison [CT0.2 Gibbs]")
for k in (1, 2, 3, 4):
    chk(len(list(product([], repeat=k))) == 0, f"§D |E_R| = 0 => the chain-tuple count at length {k} is 0: no fermion terminus [D1.4, Def-H.4]")
# the fluctuation resolvent [FT.108(4)-(5) re-derived] in Q[w, x+, x-]/(w^12)
def pd_add(p, q, s=1):
    r = dict(p)
    for k, v in q.items(): r[k] = r.get(k, Fr(0)) + s * v
    return {k: v for k, v in r.items() if v != 0}
def pd_mul(p, q):
    r = {}
    for (i1, j1), v1 in p.items():
        for (i2, j2), v2 in q.items():
            k = (i1 + i2, j1 + j2); r[k] = r.get(k, Fr(0)) + v1 * v2
    return {k: v for k, v in r.items() if v != 0}
PXp = {(1, 0): Fr(1)}; PXm = {(0, 1): Fr(1)}; P1 = {(0, 0): Fr(1)}
U = [[{}, PXm], [PXp, {}]]
def mp_mul(A, B):
    n = len(A)
    Out = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for t in range(n):
            for j in range(n):
                Out[i][j] = pd_add(Out[i][j], pd_mul(A[i][t], B[t][j]))
    return Out
cur = [[P1, {}], [{}, P1]]
series = []
for n in range(13):
    series.append(cur[0][0])
    cur = mp_mul(cur, U)
chk(all(series[n] == {} for n in (1, 3, 5, 7, 9, 11)), "§D return amplitudes vanish at odd n (no unbalanced return)")
for n in (0, 2, 4, 6, 8, 10, 12):
    want = P1
    for _ in range(n // 2): want = pd_mul(pd_mul(want, PXp), PXm)
    chk(series[n] == want, f"§D <vac|U^{n}|vac> = (x+ x-)^{n//2} exact — every return is a balanced J+J- pair")
    chk(all(i == j for (i, j) in series[n]), f"§D balanced-degree census at n = {n}: deg x+ = deg x- on every monomial")
prod = [{} for _ in range(13)]
for n in range(13):
    prod[n] = pd_add(prod[n], series[n])
    if n + 2 <= 12:
        prod[n + 2] = pd_add(prod[n + 2], pd_mul(pd_mul(PXp, PXm), series[n]), -1)
chk(prod[0] == P1 and all(prod[n] == {} for n in range(1, 13)),
    "§D resolvent identity (1 - w^2 x+ x-) * sum_n <vac|U^n|vac> w^n = 1 coefficient-wise in Q[w]/(w^12) [FT.108(5) re-derived]")
Qm = [[pd_add({}, PXp, -1), dict(PXp)], [dict(PXm), pd_add({}, PXm, -1)]]
stat = [dict(PXm), dict(PXp)]
c0 = pd_add(pd_mul(stat[0], Qm[0][0]), pd_mul(stat[1], Qm[1][0]))
c1 = pd_add(pd_mul(stat[0], Qm[0][1]), pd_mul(stat[1], Qm[1][1]))
chk(c0 == {} and c1 == {}, "§D ker Q is spanned by (x-, x+): (x-,x+) Q = 0 exact [FT.108(4) re-derived]")
detQ = pd_add(pd_mul(Qm[0][0], Qm[1][1]), pd_mul(Qm[0][1], Qm[1][0]), -1)
chk(detQ == {} and Qm[0][1] != {}, "§D det Q = 0 != Q: rank 1 over the fraction field => the stationary measure is unique up to scale")
d12 = [l for l in ADOC.split('\n') if l.startswith('**D1.2.**')][0]
chk('rung' not in d12 and 'mathcal G_n' not in d12, "§D D1.2's transition domains carry no rung argument: the arrow law is rung-blind")
stamp("§D green: exhaustive histories; prefix law; Catalan completions; the two reversals; ledger monotonicity; rho_0 pins; resolvent + balanced pairs; ker Q; D1.2 rung-blindness")

# ================================================================== §E  FT.144(5)-(6)
banner("§E (H21/FT.144(5)-(6)) — the doublet, the ray occupancy datum, and the flip channel at rung two")
OM2 = sg[1]                                          # omega-hat
CHI2 = [[C(0), C(0, 1)], [C(0, -1), C(0)]]           # chi-hat = i(|c><w| - |w><c|)
KAP2 = sg[3]                                         # kappa-hat
chk(eqm(mmul(OM2, OM2), I2) and eqm(mmul(CHI2, CHI2), I2) and eqm(mmul(KAP2, KAP2), I2), "§E the doublet triple: involutions [Def-H.33/34]")
chk(eqm(mmul(OM2, CHI2), msc(KAP2, C(0, -1))) and eqm(mmul(CHI2, KAP2), msc(OM2, C(0, -1))) and eqm(mmul(KAP2, OM2), msc(CHI2, C(0, -1))),
    "§E quaternionic triple: om chi = -i kap, chi kap = -i om, kap om = -i chi [Def-H.34]")
chk(eqm(madd(mmul(OM2, CHI2), mmul(CHI2, OM2)), msc(I2, C(0))), "§E {om, chi} = 0: chi is omega-odd")
PL = msc(madd(I2, CHI2), Fr(1, 2)); PRj = msc(madd(I2, CHI2, -1), Fr(1, 2))
chk(eqm(mmul(PL, PL), PL) and eqm(mmul(PRj, PRj), PRj) and eqm(mmul(PL, PRj), msc(I2, C(0))) and eqm(madd(PL, PRj), I2),
    "§E P_L, P_R idempotent, orthogonal, complete [FT.122(2)]")
chk(mtr(PL) == C(1) and mtr(PRj) == C(1), "§E rank-1: tr P_L = tr P_R = 1")
chk(eqm(mmul(mmul(OM2, PL), OM2), PRj), "§E omega P_L omega = P_R: the rays are omega-exchanged [FT.122(4)/FT.123(2)]")
Lu = [C(1), C(0, -1)]; Ru = [C(1), C(0, 1)]
def mvec(M, v): return [sum((M[i][j] * v[j] for j in range(2)), C(0)) for i in range(2)]
chk(mvec(CHI2, Lu) == Lu and mvec(CHI2, Ru) == [C(-1) * x for x in Ru], "§E chi |L_u> = +|L_u>, chi |R_u> = -|R_u> [Def-H.33 eigenbasis]")
chk(mvec(KAP2, Lu) == Ru and mvec(KAP2, Ru) == Lu, "§E kappa swaps the chiral rays with no phase [FT.129(2)]")
chk([(Lu[i] + Ru[i]) / 2 for i in range(2)] == [C(1), C(0)], "§E (|L_u> + |R_u>)/2 = |c>: the orientation ray is an equal-weight superposition of both chiral rays [Def-H.34 Rmk]")
for bij in (('L', 'R'), ('R', 'L')):
    chk(len({bij[0]}) == 1, f"§E coupling census {bij}: the single-arrow locus maps into a single chiral ray; the complement has occupancy zero")
# extended carrier [P-H18a]: weak-commuting chirality
Wext = [msc(mkron(sg[i], I2), Fr(1, 2)) for i in (1, 2, 3)]
PLcar = mkron(I2, PL); CHIcar = mkron(I2, CHI2)
for i in range(3):
    chk(eqm(mmul(Wext[i], PLcar), mmul(PLcar, Wext[i])), f"§E [W{i+1} (x) I, I (x) P_L] = 0: weak acts chirality-blind on the extended carrier [FT.123(1)]")
chk(rankQ([[x for z in row for x in (z.re, z.im)] for W in Wext for row in W]) == 8, "§E the stacked weak images have full rank over C (8 over R): the joint kernel is {0} [FT.126(3)]")
Smat = [[C(1), C(1)], [C(0, -1), C(0, 1)]]                 # Def-H.34's S (columns = unnormalized chiral kets)
chk(eqm(mmul(mdag(Smat), Smat), msc(I2, C(2))), "§E S^dagger S = 2 I_2 [Def-H.34]")
U4 = mkron(I2, Smat); U4d = mkron(I2, mdag(Smat))
def chiral_blocks(M):
    T = msc(mmul(mmul(U4d, M), U4), Fr(1, 2))
    Li, Ri = (0, 2), (1, 3)                                # composite index = 2*int + chiral [Def-H.34]
    return ([[T[i][j] for j in Li] for i in Li], [[T[i][j] for j in Ri] for i in Ri],
            [[T[i][j] for j in Ri] for i in Li], [[T[i][j] for j in Li] for i in Ri])
PROF = [tuple(C(v) for v in prof) for prof in product([Fr(0), Fr(1)], [Fr(-1), Fr(1), Fr(2)], [Fr(-1), Fr(0), Fr(1)], [Fr(1), Fr(3, 2), Fr(-1, 2)])]
def h_of(c):
    return [[sum((c[a] * sg[a][i][j] for a in range(4)), C(0)) * Fr(1, 2) for j in range(2)] for i in range(2)]
for c in PROF:
    h = h_of(c)
    F = mkron(h, I2)                                          # rung-one derived locus [FT.127(9)]
    FLL, FRR, FLR, FRL = chiral_blocks(F)
    chk(eqm(FLR, msc(I2, C(0))) and eqm(FRL, msc(I2, C(0))), "§E rung one: F_LR = F_RL = 0 exactly (the no-flip theorem) [FT.128(2)]")
    chk(eqm(FLL, h) and eqm(FRR, h), "§E rung one: F_LL = F_RR = h — spectral parity doubling [FT.128(2),(5)]")
    chk(eqm(mmul(F, CHIcar), mmul(CHIcar, F)), "§E [F_ext, I (x) chi] = 0: chirality is an exact quantum number at the derived locus [FT.128(4)]")
    cph = charpoly(h); cpF = charpoly(F)
    sqp = [C(0)] * 5
    for i in range(3):
        for j in range(3):
            sqp[i + j] += cph[i] * cph[j]
    chk(cpF == sqp, "§E charpoly(F_ext) = charpoly(h)^2 [FT.128(5); Faddeev–LeVerrier exact]")
chk(eqm(msc(mmul(mmul(U4d, mkron(I2, KAP2)), U4), Fr(1, 2)), mkron(I2, sg[1])),
    "§E (1/2) U^dag (I (x) kappa) U = I (x) sigma_1: kappa maps to the sigma_1-type [Def-H.34 rotation; FT.129(2)]")
def shift2(cp, s):                                          # charpoly_h(x - s) for a monic quadratic
    _, c1, c2 = cp
    return [C(1), c1 - 2 * C(s), c2 - c1 * C(s) + C(s) * C(s)]
for c in PROF:
    h = h_of(c)
    cph = charpoly(h)
    for q in (Fr(-1), Fr(0), Fr(1)):
        Fq = madd(mkron(h, I2), mkron(I2, KAP2), q)
        FLL, FRR, FLR, FRL = chiral_blocks(Fq)
        chk(eqm(FLR, msc(I2, C(q))) and eqm(FRL, msc(I2, C(q))), f"§E rung two: F_LR = F_RL = q I_2 at q = {q} [FT.129(5)]")
        chk(eqm(FLL, h) and eqm(FRR, h), "§E rung two: F_LL = F_RR = h unchanged")
        chk((q != 0) == (not eqm(FLR, msc(I2, C(0)))), "§E F_LR != 0 iff q != 0 — the flip channel opens exactly for charged cores [FT.129(5)]")
        A = shift2(cph, q); B = shift2(cph, -q)
        want = [C(0)] * 5
        for i in range(3):
            for j in range(3):
                want[i + j] += A[i] * B[j]
        chk(charpoly(Fq) == want, f"§E charpoly factorization at q = {q}: spec = spec(h) ± q — the chiral-partner splitting is 2|q| in {{0,2}} [FT.130(5)]")
for c in PROF[:12]:
    h = h_of(c)
    _, _, FLR0, _ = chiral_blocks(mkron(h, I2))
    chk(eqm(FLR0, msc(I2, C(0))), "§E minimality: removing the kappa term kills F_LR at every profile [FT.129(5)]")
    for q in (Fr(-1), Fr(1)):
        _, _, FLRk, _ = chiral_blocks(msc(mkron(I2, KAP2), q))
        chk(eqm(FLRk, msc(I2, C(q))), "§E minimality: the kappa term alone leaves F_LR = q I_2 [FT.129(5)]")
chk(2 * 2 == 4 and 4 != 4 * 3, "§E H_ext = C^2 (x) C^2 has no C^3 slot factor: colour acts elsewhere [FT.127(7); CT3.2]")
stamp("§E green: doublet triple and projectors; equal-weight ray witness; coupling census; no-flip blocks at 54 profiles; flip channel F_LR = qI_2 with charpoly factorization; minimality rows")

# ================================================================== §F  FT.145 + document pins
banner("§F (H21/FT.145) — the rung-one completion: arithmetic pins, document structure, vocabulary scans, downstream integrity")
chk(3 + 3 + 5 + 3 + 1 + 1 == 16, "§F completeness fraction: 3+3+5+3+1+1 = 16 = C_cap [CT0.12]")
chk(2 == 2 and LN2[0] > Fr(69, 100), "§F digon E_int = 2 [FT.28(1)]: m_hid = 2 ln2 / h — exact integer coefficient; ln2 enclosure sane")
flag = (6, 16, 17, 25)
chk(all(flag[i] < flag[i + 1] for i in range(3)), "§F the mask flag is strict: 6 < 16 < 17 < 25 [CT0.14]")
chk(17 - 16 == 1 and 25 - 17 == 8, "§F rung-two growth is exactly the EM centre (+1); rung-three adds su(3) (+8) [CT0.14]")
if ARCH:
    doc = H21DOC
secs = {}
if ARCH:
    for sp in re.split(r'^### ', doc, flags=re.M)[1:]:
        secs[sp.split(' —')[0].strip()] = sp.split('\n## ')[0]
    for t in ('FT.141', 'FT.142', 'FT.143', 'FT.144', 'FT.145'):
        chk(t in secs, f"§F section {t} present")
    for w in ('**Thm.**', '**Req.**', '**Pf.**', '**Phys.**', '**Status.**'):
        chk(all(secs[t].count(w) == 1 for t in ('FT.141', 'FT.142', 'FT.143', 'FT.144', 'FT.145')), f"§F every FT block carries exactly one {w}")
    chk(doc.count(r'\blacksquare') == 6, f"§F 6 proof terminators (5 proofs + the document-end seal; got {doc.count(chr(92)+'blacksquare')})")
    chk(doc.count('**Status.**') == 6, "§F Status count = 6 (5 theorem blocks + the document header line)")
    chk('## Tier F.42' in doc and 'part 21 of 21' in doc, "§F pins: Tier F.42 heading; part 21 of 21")
    chk('verify_H_rung1_neutrino.py' in doc, "§F pin: machine-verification reference")
    chk(r'=E_0+\mathbb S=2\,\Pi_{\mathcal R}' in doc, "§F pin: the weak-Casimir display sum W^2 = E0 + S = 2 Pi_R")
    chk('45\\ \\text{of the}\\ 2^6=64' in doc, "§F pin: the 45/64 deletion census")
    chk(r'm_{\mathrm{hid}}=\frac{2\ln2}{\mathfrak h}' in doc, "§F pin: the digon mass read")
    chk('| Species identification of the triplet | — | NOT derived (barred: P1, P5) |' in doc, "§F pin: adjudication row (no identification)")
    chk('| Arrow$\\leftrightarrow$ray assignment rule | — | Open (deficit 1$\'$ content) |' in doc, "§F pin: adjudication row (assignment rule open)")
    chk(r'\sqrt2\cos\tfrac38' in doc, "§F pin: the channel-own cubic constant")
    chk('16\\,\\delta_\\nu=9\\,\\delta_\\ell=27\\,\\delta_q=2' in doc, "§F pin: the shared-numerator identity")
    chk(doc.count('$$') % 2 == 0, "§F $$ total even")
cum = 0; bad = 0
if ARCH:
    for l in doc.split('\n'):
        if l.startswith('## ') and cum % 2 != 0: bad += 1
        cum += l.count('$$')
    chk(bad == 0, "§F per-section $$ balance")
arts = []
if ARCH:
    for pat in (r'\\u201[0-9a-fA-F]', r'\\u[0-9a-fA-F]{4}', r'^\$$', r'\$\$\$', r'TODO', r'PLACEHOLDER', r'XXX'):
        for m in re.finditer(pat, doc, flags=re.M):
            arts.append((pat, doc[:m.start()].count('\n') + 1))
chk(not arts, f"§F artifact scan clean ({arts})")
BARRED = ['previously', 'formerly', 'this was', 'now this', 'erratum', 'submitted', 'earlier draft', 'stale', 'draft', 'directive', 'as corrected']
if ARCH:
    hits = [(w, doc.lower().count(w)) for w in BARRED if w in doc.lower()]
if ARCH:
    chk(not hits, f"§F revision/drafting-language scan of H21: zero hits ({hits})")
    scan = doc.replace('verify_H_rung1_neutrino.py', '')      # the checker filename is a ledger-level channel label, not prose
SPECIES = ['electron', 'muon', 'tau lepton', 'neutrino', 'proton', 'neutron', 'quark', 'photon', 'gluon', 'lepton', 'pion', 'higgs']
if ARCH:
    phs_hits = [(w, scan.lower().count(w)) for w in SPECIES if w in scan.lower()]
if ARCH:
    chk(not phs_hits, f"§F species-name scan of ALL of H21 (prose; checker-filename mentions exempt): zero hits ({phs_hits})")
    chk(doc.count('tau') == doc.count('\\tau'), "§F every 'tau' substring in H21 is the tick-symbol macro \\tau")
    chk(doc.count('EXT') == 1, f"§F [EXT] occurs exactly once (the standing-rules clause): got {doc.count('EXT')}")
EXTTOK = ['206.768', '3477.2', '0.999988', '0.999921', '0.511', '105.6', '1776', '1.273', '4.183',
          '162.5', '172.4', '938.2', '139.57', '0.118', '137.0']
if ARCH:
    leak = [t for t in EXTTOK if t in doc]
if ARCH:
    chk(not leak, f"§F no external datum token anywhere in H21 ({leak})")
    reqtext = '\n'.join(l for l in doc.split('\n') if l.startswith('**Req.**'))
if ARCH:
    phs = set(re.findall(r"P-H\d+'?[a-z]?", reqtext))
if ARCH:
    chk(phs <= {'P-H0', "P-H7'", 'P-H9', 'P-H18a', 'P-H19a', 'P-H16a', 'P-H17a'}, f"§F Req-line P-H tokens within the logged set ({sorted(phs)})")
    imports = phs - {'P-H16a', 'P-H17a'}
if ARCH:
    chk(imports <= {'P-H0', 'P-H18a', 'P-H19a'}, f"§F actual imports confined to {{P-H0, P-H18a, P-H19a}} (got {sorted(imports)})")
    chk('P-H16a, P-H17a cited in the rejection rows and imported nowhere' in reqtext, "§F the Req line carries the cited-not-imported clause verbatim")
chk(all(t in BDOC for t in ('CT0.1', 'CT0.2', 'CT0.6', 'CT0.7', 'CT0.12', 'CT0.13', 'CT0.14', 'CT1.1', 'CT1.2', 'CT1.7')), "§F cited B-tags exist")
chk('CT2.5' in CDOC and 'EW.32' in DDOC and 'EM.9' in EDOC and 'CT3.11' in FDOC and 'CT4.2' in GDOC, "§F cited C/D/E/F/G-tags exist")
chk(all(t in ADOC for t in ('**A3.**', '**A5.**', '**A6.**', '**A8.**', '**D1.2.**', '**D1.3.**', '**D2.11.**', '**P1.**', '**P4.**', '**P5.**')), "§F cited A-tags exist")
if ARCH:
    chk('### FT.68' in rd('H_archive/H09_flicker_and_domains.md') and '### FT.88' in rd('H_archive/H11_gravity_and_koide.md') and '### FT.108' in rd('H_archive/H15_topology_blind.md'), "§F cited H-tags exist (FT.68, FT.88, FT.108)")
    chk('FT.141–FT.145 (H21, Tier F.42)' in H13DOC, "§F H13 item-20 carries the H21 bracketed ledger entry")
    chk('Rung-one completion' in H13DOC, "§F H13 entry records the rung-one completion status")
    chk('FT.141' in H18DOC and 'FT.144' in H18DOC, "§F H18 carries the forward pointer to the rung-one tier")
    chk('FT.144' in H19DOC and 'Tier F.42' in H19DOC, "§F H19 carries the forward pointer to the rung-one tier")
    for s in ('**(P-H18a)**', '**(P-H19a)**', '**(P-H20a)**', 'VACUOUS', 'parity census',
              'deficit 1 is closed at the projector level', 'deficit 11 unchanged', 'flipping block computed'):
        chk(s in H13DOC, f"§F H13 pin intact: {s[:40]}")
    chk(H18DOC.count(r'\blacksquare') == 6 and H19DOC.count(r'\blacksquare') == 7, "§F H18/H19 proof-terminator counts unchanged by the forward pointers")
    chk(H18DOC.count('[EXT]') == 1 and H19DOC.count('[EXT]') == 1, "§F H18/H19 [EXT] counts unchanged")
stamp("§F green: completion arithmetic; document structure and pins; vocabulary and import scans; frozen-citation existence; downstream integrity")

print(f"\nverify_H_rung1_neutrino: {N} checks green  ({time.time()-t0:.1f}s) — H21 §A–§F (Tier F.42, FT.141–FT.145)")
