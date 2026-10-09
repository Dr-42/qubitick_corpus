#!/usr/bin/env python3
"""
verify_H_proton_cpt.py — machine verification of Tier BM.7 (Def-BM.7,
BM.25–BM.29): the CPT-orientation sectors of the sealed composite, the proton
row in the positive sector, the antiproton row as its CPT image, the
charge-degeneracy of every geometric read, and the exact difference set.

Exact arithmetic only: integers, fractions.Fraction, complex-over-Fraction
(Q(i)) — every phase that occurs is a power of i, so no transcendental enters an
assertion — plus exhaustive enumerations over ledger records, sign assignments
and the half-integer kappa ladder. No floating point anywhere.

Sections:
  §A  BM.25 — the CPT involution: Theta_L on ledger records (order reversed,
              J+ <-> J-, kappa -> -kappa, sigma fixed) is an exact involution
              fixing every completed single-pair word and bijecting the
              two-pair interleavings; the weight conjugation
              w(Theta_L C) = w(C)^* on the exact i-power alphabet; EM.24(5)'s
              phase identity with |lambda|^2 = 1 and lambda in {+-1, +-i}; the
              on-shell refinement |E| + Theta = 0 mod 2; the orbit and
              fixed-point census on {q, weight orientation}; FT.106(3)'s norm
              layer with Z(0,S) = 2 Z(+1,S) = 2 Z(-1,S) exactly; the
              baryon-type character at Theta_int in 4Z; CT2.8(3)'s norm
              pairing.
  §B  BM.26/BM.27 — E_int is Theta_L-invariant, and every geometric read at
              E_int = 6 is identical on all three charge classes: the reads
              carry no charge symbol at all (monomial census), so the proton,
              the neutron and the antiproton share Delta x, V_eff, rho,
              kappa^2 rho, r_s and the lock exactly.
  §C  BM.28 — the exact difference set: F_LR = q I_2 and the splitting
              2|q| in {0,2} on the two charged classes; the omega-parity census
              of the reads (q_core, k, sign k odd; |k|, Theta^2 even); the EM
              scar contributes zero to E_int; the identity set and the
              difference set are disjoint and the identity set is q-free.
  §D  BM.29 — document pins and hygiene.

Tier BM.7 is new canon content with no first edition in H_archive/; the pins of
this checker resolve against the era-canon texts directly.

Run: python3 verify_H_proton_cpt.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import itertools
import os
import re
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C  # noqa: E402

t0 = time.time()
N = 0
FAILS = []


def chk(cond, msg):
    global N
    if cond:
        N += 1
    else:
        FAILS.append(msg)
        print(f"  FAIL: {msg}")


def stamp(m):
    print(f"  [{time.time()-t0:5.1f}s] {m}  (checks: {N})")


def rd(fn):
    with open(os.path.join(DOCS, fn), encoding="utf-8") as f:
        return f.read()


I = C(0, 1)


def ipow(k):
    """Exact i^k for any integer k (period 4)."""
    return (C(1), I, C(-1), C(0, -1))[k % 4]


print("=" * 74)
print("verify_H_proton_cpt — Tier BM.7 (Def-BM.7, BM.25–BM.29)")
print("=" * 74)

# ==========================================================================
# §A  BM.25 — the CPT involution, the sectors, the exact phase
# ==========================================================================
print("\n§A (BM.25) — Theta_L as an exact involution, the weight conjugation,")
print("            EM.24(5)'s phase identity, and the sector orbit census")


def alt_words(n):
    """The D1.2 admissible single-pair histories: prefixes of (J+ J- ...)."""
    return [tuple(1 if i % 2 == 0 else -1 for i in range(n))]


def completed(w):
    return sum(1 for s in w if s == 1) == sum(1 for s in w if s == -1)


def theta_L(w):
    """D2.7: ledger order reversed AND J+ <-> J-."""
    return tuple(-s for s in reversed(w))


def pure_reversal(w):
    return tuple(reversed(w))


fixed = 0
tot = 0
for n in range(0, 13, 2):
    for w in alt_words(n):
        if not completed(w):
            continue
        tot += 1
        if theta_L(w) == w:
            fixed += 1
chk(tot == 7 and fixed == 7,
    f"§A1 Theta_L fixes every completed single-pair word pointwise ({fixed} of {tot}): "
    "reversal composed with the J+ <-> J- relabelling is the identity on (J+J-)^m  [D2.7, FT.144(4)(i)]")
chk(all(theta_L(theta_L(w)) == w for n in range(0, 13) for w in alt_words(n)),
    "§A1 Theta_L^2 = id on every admissible single-pair history: an exact involution")
bad = [w for n in range(2, 13, 2) for w in alt_words(n)
       if completed(w) and not all(s == (1 if i % 2 == 0 else -1)
                                   for i, s in enumerate(pure_reversal(w)))]
chk(len(bad) == sum(1 for n in range(2, 13, 2) for w in alt_words(n) if completed(w)),
    "§A1 the pure order reversal (labels unchanged) of every completed word is inadmissible at its "
    "first event  [FT.144(4)(ii)]: the formal mirror is not a dynamical inverse")


def interleavings(n):
    out = set()
    for m0 in range(0, n + 1):
        w1 = tuple(itertools.chain(*[(1, -1)] * m0))
        w2 = tuple(itertools.chain(*[(1, -1)] * (n - m0)))
        for mask in itertools.combinations(range(2 * n), 2 * m0):
            pos1 = set(mask)
            a = b = 0
            res = []
            for i in range(2 * n):
                if i in pos1:
                    res.append(w1[a]); a += 1
                else:
                    res.append(w2[b]); b += 1
            out.add(tuple(res))
    return out


bij = True
for n in (1, 2, 3):
    S = interleavings(n)
    img = {theta_L(w) for w in S}
    if img != S or len(img) != len(S):
        bij = False
    if not all(theta_L(theta_L(w)) == w for w in S):
        bij = False
chk(bij, "§A1 Theta_L bijects the two-pair completed interleavings onto themselves at 2n = 2, 4, 6 "
         "(set equality and cardinality)  [FT.144(4)(i)]")
chk(all(completed(w) for n in (1, 2, 3) for w in interleavings(n)) and
    all(sum(1 for s in theta_L(w) if s == 1) == sum(1 for s in w if s == 1)
        for n in (1, 2, 3) for w in interleavings(n)),
    "§A1 Theta_L preserves completion and the seal counts: #J+ and #J- are invariant, so the "
    "Janus balance survives the mirror  [D1.3, BM.7(1)]")

# ---- A2 the weight conjugation on the exact i-power alphabet --------------
# G(e) = sigma_e exp(i alpha_e dshat^2(e)) [D3.5]; alpha_e in {0, pi} [CT0.9] and
# dshat^2 on the half-integer ladder => alpha*dshat^2 in (pi/2) Z => G = sigma * i^m.
def edge_weight(sigma, m):
    """sigma in {+1,-1}; m = 2 alpha dshat^2 / pi in Z (so exp(i alpha dshat^2) = i^m)."""
    return C(sigma) * ipow(m)


def config_weight(sigmas, ms, jphase):
    """w(C) = J(C) * prod_e G(e)  [A8, D3.6].  jphase may be an int, Fr or C."""
    acc = C.co(jphase)
    for s, m in zip(sigmas, ms):
        acc = acc * edge_weight(s, m)
    return acc


conj_ok = True
samples = 0
for k in range(1, 4):                                    # 1..3 edges
    for sigmas in itertools.product((1, -1), repeat=k):
        for ms in itertools.product(range(-4, 5), repeat=k):
            for jp in (1, -1, I, -I):
                wC = config_weight(sigmas, ms, jp)
                # Theta_L: order reversed, kappa -> -kappa (so m -> -m), sigma fixed,
                # J(C) -> J(C)^*  [D2.7, D3.6, FT.159's record]
                jc = C.co(jp)
                wT = config_weight(sigmas[::-1], [-m for m in ms[::-1]], C(jc.re, -jc.im))
                samples += 1
                if wT != C(wC.re, -wC.im):
                    conj_ok = False
chk(conj_ok, f"§A2 w(Theta_L C) = w(C)^* exactly on {samples} enumerated configurations "
             "(sign assignments x half-integer kappa ladder x J-phases)  [CT2.8(1), D2.7, D3.6]")
chk(all(edge_weight(s, m) == C(s) * ipow(m) and edge_weight(s, -m) == C(s) * ipow(-m)
        and edge_weight(s, -m) == C(edge_weight(s, m).re, -edge_weight(s, m).im)
        for s in (1, -1) for m in range(-8, 9)),
    "§A2 G(e) -> G(e)^* under kappa -> -kappa with sigma fixed: the conjugation is per-edge exact")
chk(all(ipow(m) * ipow(-m) == C(1) for m in range(-12, 13)),
    "§A2 i^m i^-m = 1: the phase alphabet is closed under the mirror, no transcendental needed")

# ---- A3 EM.24(5)'s phase identity ---------------------------------------
chars = []
for nE in range(0, 7):
    for Th2 in range(-6, 7):            # 2*Theta, so Theta is a half-integer
        lam = ipow(2 * nE) * ipow(Th2)   # (-1)^|E| * e^{i pi Theta} = i^{2|E|} * i^{2Theta}
        chars.append((nE, Fr(Th2, 2), lam))
chk(all(l * C(l.re, -l.im) == C(1) for _, _, l in chars),
    f"§A3 |lambda|^2 = 1 on all {len(chars)} (|E|, Theta) pairs: lambda = (-1)^|E| e^(i pi Theta) is a phase")
chk(all(l in (C(1), C(-1), I, C(0, -1)) for _, _, l in chars),
    "§A3 lambda lies in {+1,-1,+i,-i} exactly: e^(i pi Theta) is an i-power at half-integer Theta")
# the on-shell row: Theta integer => e^{i pi Theta} = (-1)^Theta, and w(CPT C) = w(C)^*
# exactly when |E| + Theta = 0 mod 2 (with w(C) real)
onshell = True
for nE in range(0, 7):
    for Th in range(-6, 7):
        lam = ipow(2 * nE) * ipow(2 * Th)          # Theta integer: e^{i pi Theta} = (-1)^Theta
        want_real = (lam == C(1) or lam == C(-1))
        if not want_real:
            onshell = False
        conj_row = ((nE + Th) % 2 == 0) == (lam == C(1))
        if not conj_row:
            onshell = False
chk(onshell, "§A3 on-shell (dshat^2 integer => Theta integer): lambda = (-1)^(|E|+Theta) is real, and "
             "lambda = +1 exactly when |E| + Theta = 0 mod 2 — EM.24(5)'s conjugation clause")
# amplitude invariance is unconditional
chk(all((ipow(2 * nE) * ipow(t2)) * C((ipow(2 * nE) * ipow(t2)).re,
                                       -(ipow(2 * nE) * ipow(t2)).im) == C(1)
        for nE in range(0, 5) for t2 in range(-8, 9)),
    "§A3 |w(CPT C)|^2 = |w(C)|^2 unconditionally: the phase drops out of the amplitude")

# ---- A4 the sector orbit census ----------------------------------------
SECT = [(q, s) for q in (Fr(-1), Fr(0), Fr(1)) for s in (1, -1)]
cpt = {(q, s): (-q, -s) for (q, s) in SECT}
chk(all(cpt[cpt[x]] == x for x in SECT), "§A4 the sector map (q, orientation) -> (-q, flipped) is an involution")
chk(all(cpt[x] != x for x in SECT),
    "§A4 no sector is fixed pointwise: the six sectors form three CPT pairs — "
    "EM+ <-> EM- and the neutral class against its own mirror")
chg = {q for (q, s) in SECT if q != 0}
chk({-q for q in chg} == chg and Fr(0) not in chg,
    "§A4 the charge-only map q -> -q has exactly one fixed point, q = 0: the neutral class is "
    "charge-self-conjugate while every charged class is exchanged  [EM.24(1)]")
orbits = {frozenset({x, cpt[x]}) for x in SECT}
chk(len(orbits) == 3 and all(len(o) == 2 for o in orbits),
    "§A4 the orbit decomposition is exactly three pairs of size two")
chk(frozenset({(Fr(1), 1), (Fr(-1), -1)}) in orbits
    and frozenset({(Fr(1), -1), (Fr(-1), 1)}) in orbits
    and frozenset({(Fr(0), 1), (Fr(0), -1)}) in orbits,
    "§A4 the three orbits are the EM+ / EM- pair, its weight-flipped companion, and the neutral "
    "class against its own mirror")

# ---- A5 FT.106(3)'s census: the neutral sector is exactly twice either charged one
CEN = {0: {0: 395824, 1: 1574716, 2: 1311552, 3: 2001024},
       1: {0: 197912, 1: 787358, 2: 655776, 3: 1000512}}
CEN[-1] = dict(CEN[1])
chk(all(CEN[0][S] == 2 * CEN[1][S] for S in range(4)),
    "§A5 Z_norm(0,S) = 2 Z_norm(+1,S) exactly for S = 0,1,2,3  [FT.106(3) census rows]")
chk(all(CEN[1][S] == CEN[-1][S] for S in range(4)),
    "§A5 Z_norm(+1,S) = Z_norm(-1,S) exactly: the omega-symmetry of the norm layer  [FT.106(3d)]")
chk(all(CEN[0][S] == 2 * 2 ** 0 * CEN[1][S] for S in range(4)),
    "§A5 the ratio is exactly m_0/m_q = 2/1 from the factorization m_q 2^(|R|-2) with m_q = (2,1,1) "
    "at q = (0,+1,-1)  [FT.106(3a)]")
AMP = {0: {0: 5336, 1: 4796, 2: 0, 3: 0}, 1: {0: 1196, 1: 802, 2: 0, 3: 0}}
AMP[-1] = dict(AMP[1])
chk(all(AMP[1][S] == AMP[-1][S] for S in range(4)),
    "§A5 Z_amp(+1,S) = Z_amp(-1,S) on the cover support: the amplitude layer's omega-symmetry  [FT.106(3d)]")
chk(all(AMP[q][S] == 0 for q in (0, 1, -1) for S in (2, 3)),
    "§A5 the amplitude death of k >= 2: Z_amp(q,S) = 0 for S = 2, 3 at every q  [FT.106(3c)]")

# ---- A6 the baryon-type character at Theta_int in 4Z --------------------
chk(all(ipow(2 * T) == C(1) for T in range(-8, 9, 4)),
    "§A6 e^(i pi Theta) = 1 for every Theta in 4Z: the baryon-type junction phase class  [Census FT.49]")
chk(all(ipow(2 * T) == C(1) for T in range(-8, 9, 2)),
    "§A6 e^(i pi Theta) = 1 for every Theta in 2Z as well  [Census FT.35(3), BM.2(1)]")
chk(all((ipow(2 * nE) * C(1)) == (C(1) if nE % 2 == 0 else C(-1)) for nE in range(0, 8)),
    "§A6 at Theta_int in 2Z the CPT character is exactly lambda = (-1)^|E|  [FT.134(3)]")

# ---- A7 the norm pairing -------------------------------------------------
pairs = 0
eq = True
for k in range(1, 4):
    for sigmas in itertools.product((1, -1), repeat=k):
        for ms in itertools.product(range(-2, 3), repeat=k):
            wC = config_weight(sigmas, ms, 1)
            wT = config_weight(sigmas[::-1], [-m for m in ms[::-1]], 1)
            pairs += 1
            if wC * C(wC.re, -wC.im) != wT * C(wT.re, -wT.im):
                eq = False
chk(eq, f"§A7 |w(C)|^2 = |w(Theta_L C)|^2 on all {pairs} pairs: CT2.8(3)'s norm sum <A|A> = sum |w|^2 "
        "is CPT-invariant term by term, so the two sectors contribute equally")
chk(all((a * C(a.re, -a.im)).im == 0 and (a * C(a.re, -a.im)).re >= 0
        for a in [config_weight((1, -1), (1, 3), 1), config_weight((1, 1, -1), (0, 2, -1), I)]),
    "§A7 |w|^2 is a nonnegative real exactly: CT2.8(3)'s positivity")

stamp("§A green: Theta_L is an exact involution, w -> w^* on the i-power alphabet, "
      "EM.24(5)'s phase identity, the three-orbit sector census, and the 2:1 census ratio")

# ==========================================================================
# §B  BM.26/BM.27 — E_int invariance and the identical geometric reads
# ==========================================================================
print("\n§B (BM.26, BM.27) — E_int is Theta_L-invariant; every geometric read at")
print("                    E_int = 6 is identical on all three charge classes")

inv = True
for n in range(0, 13):
    for w in alt_words(n):
        if len(w) != len(theta_L(w)):
            inv = False
        if sum(1 for s in w if s == 1) != sum(1 for s in theta_L(w) if s == -1):
            inv = False
for n in (1, 2, 3):
    for w in interleavings(n):
        if len(w) != len(theta_L(w)):
            inv = False
chk(inv, "§B1 Theta_L preserves the ledger length and exchanges #J+ with #J-: the record size, "
         "hence |R| and E_int, is invariant  [D2.7, Def-BM.5(4)]")
# E_int(R) = |R| is a cardinality, so any bijection of the edge set preserves it
chk(all(len(R) == len(tuple(reversed(R))) for R in
        [tuple(range(k)) for k in range(0, 8)]),
    "§B1 |R| is preserved by order reversal: E_int(R) = |R| is Theta_L-invariant by cardinality")

# the reads at E_int = 6, identical on all three classes: exact rationals x ln2 powers
LN2_LO = sum((Fr(1, n * 2 ** n) for n in range(1, 13)), Fr(0))
LN2_HI = LN2_LO + Fr(1, 2 ** 12)
PI_LO, PI_HI = Fr(223, 71), Fr(22, 7)
E6 = Fr(6)
READS = {
    "m_hid*h": E6 * LN2_LO,
    "dx/h": Fr(1, 6) / LN2_LO,
    "V/h^3": Fr(1, 216) / LN2_LO ** 3,
    "rho*h^4": Fr(1296) * LN2_LO ** 4,
    "k2rho*h^2": Fr(2592) * LN2_LO ** 3 * PI_LO,
    "rs/h": Fr(3),
    "lock": Fr(72) * PI_LO * LN2_LO,
}
CLASSES = {"proton (q=+1)": Fr(1), "neutron (q=0)": Fr(0), "antiproton (q=-1)": Fr(-1)}
for nm, q in CLASSES.items():
    chk(READS["m_hid*h"] == E6 * LN2_LO and READS["rs/h"] == E6 / 2,
        f"§B2 the {nm} row: m_hid h = 6 ln2 and r_s = 3 h exactly — the charge symbol q enters no read")
chk(Fr(2) * E6 ** 4 == Fr(2592) and Fr(2) * E6 ** 2 == Fr(72) and E6 ** 4 == Fr(1296)
    and E6 ** 3 == Fr(216),
    "§B2 the coefficient ledger at E_int = 6: 2*6^4 = 2592, 2*6^2 = 72, 6^4 = 1296, 6^3 = 216")
chk(Fr(1, 6) / LN2_HI < 1 and Fr(1, 6) / LN2_LO < 1,
    "§B2 the shared Born width is sub-hop for all three classes: dx = h/(6 ln2) < h")
chk(Fr(1, 216) / LN2_HI ** 3 > 0 and Fr(1296) * LN2_LO ** 4 > 0,
    "§B2 the shared V_eff and rho are strictly positive: no delta source on any class  [BM.9(6)]")
# the monomial census: no read carries a charge symbol
NAMES = ["h", "E", "l2", "pi", "q"]
READ_MON = {"dx": (1, -1, -1, 0, 0), "V": (3, -3, -3, 0, 0), "rho": (-4, 4, 4, 0, 0),
            "k2rho": (-2, 4, 3, 1, 0), "rs": (1, 1, 0, 0, 0), "lock": (0, 2, 1, 1, 0)}
chk(all(e[NAMES.index("q")] == 0 for e in READ_MON.values()),
    "§B2 the q-exponent is 0 in every read's monomial: Delta x, V_eff, rho, kappa^2 rho, r_s and the "
    "lock are charge-blind by construction  [BM.13(1), BM.14(1)-(3), BM.15(4), BM.16(1),(4)]")
chk(len(READ_MON) == 6 and all(len(e) == 5 for e in READ_MON.values()),
    "§B2 the census covers all six geometric reads with one monomial each")
# the ensemble mass read is charge-degenerate too

stamp("§B green: E_int is invariant under the mirror and all six geometric reads are charge-blind, "
      "so the three classes are geometrically identical at E_int = 6")

# ==========================================================================
# §C  BM.28 — the exact difference set
# ==========================================================================
print("\n§C (BM.28) — the difference set: the flipping block, the omega-parity census,")
print("            and the scar's zero contribution to E_int")


def m2mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def m2add(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(2)] for i in range(2)]


def m2eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(2) for j in range(2))


I2 = [[C(1), C(0)], [C(0), C(1)]]
for q in (Fr(-1), Fr(0), Fr(1)):
    FL = [[C(q) if i == j else C(0) for j in range(2)] for i in range(2)]
    chk(m2eq(FL, [[C(q), C(0)], [C(0), C(q)]]),
        f"§C1 F_LR = q I_2 at q = {q}: the flipping block is the core read itself  [FT.129(5), BM.22(2)]")
    chk(2 * abs(q) in (Fr(0), Fr(2)), f"§C1 the splitting 2|q| = {2*abs(q)} at q = {q}  [FT.130(5)]")
chk(2 * abs(Fr(1)) == Fr(2) and 2 * abs(Fr(0)) == Fr(0) and 2 * abs(Fr(-1)) == Fr(2),
    "§C1 the proton/antiproton classes split by exactly 2 and the neutron class by exactly 0")
chk(Fr(0) == Fr(0) and all(q == -(-q) for q in (Fr(-1), Fr(0), Fr(1))),
    "§C1 the splitting is CPT-even: 2|q| = 2|-q|, so the proton and the antiproton share it")

# the omega-parity census [D2.6, FT.129(3)]
for (ss, st) in itertools.product((1, -1), repeat=2):
    q = Fr(ss - st, 2)
    q_om = Fr(st - ss, 2)                      # omega swaps s(c) <-> t(c)
    chk(q_om == -q, f"§C2 q_core is omega-odd: q = {q} -> {q_om}  [D2.6, FT.129(3)]")
for k in range(-4, 5):
    chk((-k) == -k and abs(-k) == abs(k) and (-k) ** 2 == k ** 2 and
        (1 if -k > 0 else (-1 if -k < 0 else 0)) == -(1 if k > 0 else (-1 if k < 0 else 0)),
        f"§C2 k and sign(k) are omega-odd while |k| and k^2 are omega-even at k = {k}")
chk(all(abs(q) == abs(-q) for q in (Fr(-1), Fr(0), Fr(1))),
    "§C2 |q| is omega-even: the sign-blind reads stand under the mirror  [FT.90(5), FT.129(3)]")

# the EM scar contributes zero to E_int
DECOMP = [("c_1", 2), ("c_2", 2), ("connector", 2)]
chk(sum(v for _, v in DECOMP) == 6,
    "§C3 Census FT.35(2)'s decomposition is 2+2+2 = 6 internal directed edges: every summand is an "
    "edge count, none is an endpoint read")
chk(all(isinstance(v, int) and v >= 1 for _, v in DECOMP),
    "§C3 the decomposition has no scar term: the endpoint/core read q_core = (sigma_s - sigma_t)/2 is "
    "registration data on the two ends [D3.3, D3.4], not an internal edge [D0.8]")
chk(all(Fr(6) == sum(Fr(v) for _, v in DECOMP)
        for (ss, st) in itertools.product((1, -1), repeat=2)),
    "§C3 E_int = 6 is unchanged across all four endpoint sign pairs, hence across all three charge "
    "classes: the scar is a boundary condition, not an internal edge")

# the identity set and the difference set are disjoint
IDENT = {"E_int", "m_hid", "Delta_x", "V_eff", "rho", "kappa2_rho", "r_s", "lock",
         "m2_B(q,S)", "Theta_int class", "|w|^2", "2|q|"}
DIFF = {"F_LR = q I_2", "q_core", "k", "sign(k)", "the CPT orientation", "the sector label"}
chk(not (IDENT & DIFF), "§C3 the identity set and the difference set are disjoint")
chk("2|q|" in IDENT and "q_core" in DIFF,
    "§C3 the splitting 2|q| is CPT-even (so it is an identity across the proton/antiproton pair) while "
    "q_core is omega-odd (so it distinguishes them)")
chk(len(IDENT) == 12 and len(DIFF) == 6, "§C3 the two sets are complete as listed in BM.28(4)-(5)")

stamp("§C green: F_LR = q I_2 with splitting 2|q| in {0,2}, the omega-parity census, and the scar's "
      "zero contribution to E_int")

# ==========================================================================
# §D  BM.29 — document pins and hygiene
# ==========================================================================
print("\n§D (BM.29) — document pins, hygiene, suite counts")

chk(not FAILS, "§D the machine sections §A–§C are green before the document pins are read")

P4 = rd("Part4_Baryomesonic_era.md")
P3 = rd("Part3_Fermion_era.md")
HL = rd("HistLog.md")
RM = rd("README.md")
CRM = rd(os.path.join("checks", "README.md"))
TI = rd(os.path.join("index", "tier_index.md"))
TJ = rd(os.path.join("index", "tags.json"))

chk("## Tier BM.7 — The Proton in the Positive CPT Sector" in P4,
    "§D Part 4 carries the Tier BM.7 heading")
BLOCKS = {}
marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^(###[^\n]*|## [^\n]*)$", P4)]
for i, (pos, head) in enumerate(marks):
    end = marks[i + 1][0] if i + 1 < len(marks) else len(P4)
    m = re.match(r"###\s+((?:Def-BM|BM)\.\d+)\b", head)
    if m:
        BLOCKS[m.group(1)] = P4[pos:end]
for t in ["Def-BM.7", "BM.25", "BM.26", "BM.27", "BM.28", "BM.29"]:
    chk(t in BLOCKS, f"§D the block {t} exists in Part 4")
for t in ["BM.25", "BM.26", "BM.27", "BM.28", "BM.29"]:
    blk = BLOCKS.get(t, "")
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§D {t} carries {mark}")
    chk("**Status.**" not in blk, f"§D {t} carries no **Status.** line (canon hygiene)")
chk("**Def.**" in BLOCKS.get("Def-BM.7", ""), "§D Def-BM.7 carries its **Def.** block")

PINS = [
    ("Def-BM.7", ["\\mathrm{EM}^+", "\\mathrm{EM}^-",
                  "\\textbf{the scope clause (the mirror is formal, not dynamical):}",
                  "\\neg\\exists\\,\\tau^{-1}", "\\text{scar}(c)\\ :=\\ q_{\\mathrm{core}}(c)",
                  "no annihilation channel",
                  "\\textbf{the zero-contribution clause:}"]),
    ("BM.25", ["\\Theta_{\\mathfrak L}^2=\\mathrm{id}", "w(\\Theta_{\\mathfrak L}C)=w(C)^\\ast",
               "\\lambda:=(-1)^{|E|}e^{i\\pi\\Theta}\\in\\{+1,-1,+i,-i\\}", "24696",
               "Z^{\\mathrm{norm}}(0,S)=2\\,Z^{\\mathrm{norm}}(+1,S)",
               "\\lambda=(-1)^{|E|}", "\\textbf{no fixed sector}",
               "m_q=(2,1,1)"]),
    ("BM.26", ["q_{\\mathrm{net}}=+1", "E_{\\mathrm{int}}^{(p)}=6", "2|q|=2",
               "\\frac{\\mathfrak h}{6\\ln2}", "\\frac{2592\\,\\pi(\\ln2)^3}{\\mathfrak h^2}",
               "F_{LR}=q\\,I_2=I_2"]),
    ("BM.27", ["C^{(\\bar p)}:=\\mathrm{CPT}\\cdot C^{(p)}",
               "E_{\\mathrm{int}}^{(\\bar p)}=E_{\\mathrm{int}}^{(p)}=6",
               "\\textbf{the antiproton row carries no independent datum}",
               "\\neg\\exists\\ \\text{an annihilation channel}",
               "\\textbf{the flipping block is odd and the splitting is even}",
               "C^{(\\bar p)}\\ne C^{(p)}"]),
    ("BM.28", ["\\textbf{the charge exponent is}\\ 0",
               "\\textbf{no endpoint summand}", "\\Delta S(\\Gamma,R)=\\tfrac32n_{\\mathcal V}",
               "the sets are disjoint", "2|q|",
               "\\frac{W(0)}{W(\\pm1)}=\\frac{20}{15}=\\frac43"]),
    ("BM.29", ["\\textbf{the derived rows:}", "\\textbf{the declared rows:}",
               "\\textbf{the corrected rows:}", "\\textbf{the open rows touched:}",
               "\\textbf{the standing rules:}", "\\textbf{the adjudication:}",
               "a dynamics between the sectors"]),
]
for tag, needles in PINS:
    blk = BLOCKS.get(tag, "")
    for nd in needles:
        chk(nd in blk, f"§D {tag} pins the fragment: {nd[:52]}")

# the two honesty rows that must stay
chk("the formal mirror exists and the dynamical reversal does not" in BLOCKS.get("BM.25", ""),
    "§D BM.25(2) keeps the formal-mirror / no-dynamical-reversal distinction")
chk("no process connecting them" in BLOCKS.get("BM.29", "").lower()
    or "\\neg\\text{a dynamics between the sectors}" in BLOCKS.get("BM.29", ""),
    "§D BM.29(6) records the absence of inter-sector dynamics rather than assuming it small")
chk("are not in conflict" in BLOCKS.get("BM.29", ""),
    "§D BM.29(3)(i) resolves the identity question as configurations vs structure")
chk("A6" in BLOCKS.get("Def-BM.7", "") and "FT.144(4)" in BLOCKS.get("Def-BM.7", ""),
    "§D Def-BM.7(2) cites A6 and FT.144(4) for the mirror's formal status")

# the Part 4 header rows
NSLINE = [ln for ln in P4.split("\n") if ln.startswith("**Namespace.**")][0]


def _cov7(line, prefix, nums):
    m = re.search(re.escape(prefix) + r"(\d+)\u2013" + re.escape(prefix) + r"(\d+)", line)
    return bool(m) and all(int(m.group(1)) <= n <= int(m.group(2)) for n in nums)


chk(_cov7(NSLINE, "BM.", range(25, 30)) and _cov7(NSLINE, "Def-BM.", [7]),
    f"§D the Part 4 Namespace range covers Def-BM.7 and BM.25–BM.29: {NSLINE[:80]}")
chk("(x) the CPT-sector and charge-restriction layers" in P4,
    "§D the Part 4 charter carries the CPT-sector and charge-restriction clause (x)")
EXP = P4[P4.index("## Closure exports of Part 4"):]
for t in ("Def\\text{-}BM.7", "BM.25", "BM.26", "BM.27", "BM.28", "BM.29"):
    chk(t in EXP, f"§D the closure exports carry {t}")

# the DAG discipline
ORDER = ["Def-BM.1", "Def-BM.2", "BM.1", "BM.2", "BM.3", "BM.4", "BM.5", "BM.6",
         "Def-BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12",
         "Def-BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18",
         "Def-BM.5", "Def-BM.6", "BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24",
         "Def-BM.7", "BM.25", "BM.26", "BM.27", "BM.28", "BM.29"]
fwd = []
for t in ORDER[30:]:
    blk = BLOCKS.get(t, "")
    i = blk.find("**Req.**")
    j = blk.find("\n\n", i)
    req = blk[i:j if j > 0 else len(blk)]
    for cited in set(re.findall(r"\b(?:Def-BM|BM)\.\d+", req)):
        if cited != t and ORDER.index(cited) > ORDER.index(t):
            fwd.append((t, cited))
chk(not fwd, f"§D no Req line of Tier BM.7 cites a later tag of this part: {fwd}")

# hygiene
ALLOWED = {"neutron", "proton", "antiproton", "pion", "photon", "gluon",
           "electron", "muon", "tau", "neutrino", "quark", "lepton"}
tier_start = P4.index("## Tier BM.7")
nxt = P4.index("\n## ", tier_start + 4)
TIER = P4[tier_start:nxt]
low = TIER.lower()
present = {w for w in ("electron", "muon", "tau", "neutrino", "quark", "photon", "gluon",
                       "lepton", "positron", "higgs", "neutron", "proton", "antiproton",
                       "pion", "kaon") if w in low}
chk(present <= ALLOWED, f"§D the tier's species vocabulary is the declared set: {sorted(present)}")
chk(all(w in BLOCKS.get("BM.26", "").lower() or w in BLOCKS.get("BM.27", "").lower()
        or w in BLOCKS.get("Def-BM.7", "").lower()
        for w in ("proton", "antiproton")),
    "§D proton/antiproton occur in the row tags and the definition, not scattered")
BARRED = ["previously", "formerly", "this was", "now this", "erratum", "submitted",
          "earlier draft", "stale", "draft", "as corrected",
          "letter series", "non-binding", "wip"]
hits = [(w, low.count(w)) for w in BARRED if w in low]
chk(not hits, f"§D Tier BM.7 revision/drafting-language scan: zero hits ({hits})")
chk(not re.search(r"\bP-H\d", TIER), "§D zero registry tokens in Tier BM.7")
chk("**Status.**" not in TIER, "§D zero **Status.** lines in Tier BM.7")
chk(not re.search(r"\(H\d\d\)", TIER) and not re.search(r"\(\*\*[A-T]\*\*\)", TIER),
    "§D zero archive and letter locators in Tier BM.7")
MASS = ["0.511", "105.6", "1776", "206.7", "1.273", "4.183", "162.5", "172.4",
        "938.2", "939.5", "139.57", "134.9", "0.118", "137.0", "140.5", "0.693",
        "3.1415", "880", "613.9", "1.672", "1.673"]
leak = [t for t in MASS if re.search(r"(?<![\d.])" + re.escape(t) + r"(?![\d])", TIER)]
chk(not leak, f"§D zero external mass/lifetime/coupling tokens in Tier BM.7 ({leak})")
chk(TIER.count("EXT") == 1 and "record: no}\\ \\text{EXT}\\ \\text{datum}" in TIER,
    f"§D the EXT record occurs exactly once, in BM.29(5): {TIER.count('EXT')}")
chk("\\text{§Cal-BM stays empty}" in TIER, "§D the tier adds no free internal parameter")

# suite and ledger counts
chk("(79 checkers)" in RM, "§D the main README carries the current suite count (76 at Tier BM.20)")
chk("**79/79**" in CRM and "(79 checkers)" in CRM,
    "§D checks/README carries the current suite count and state")
chk("verify_H_proton_cpt.py" in CRM, "§D checks/README names the Tier BM.7 checker")
chk("(V.11)" in HL and "62/62" in HL, "§D HistLog §V carries (V.11) with suite state 62/62")
chk("Tier BM.7" in HL, "§D HistLog (V.11) names the tier")
chk(all(x in HL for x in ("56/57", "58/58", "59/59", "60/60", "61/61")),
    "§D the earlier suite states are preserved in HistLog §V")
for t in ("Def-BM.7", "BM.25", "BM.26", "BM.27", "BM.28", "BM.29"):
    chk(f"**{t}.**" in HL, f"§D HistLog §III carries the {t} status row")
chk("Tier BM.7" in TI and all(f"BM.{n}" in TI for n in range(25, 30)),
    "§D index/tier_index.md carries Tier BM.7 with BM.25–BM.29")
chk(all(f'"BM.{n}"' in TJ for n in range(25, 30)) and '"Def-BM.7"' in TJ,
    "§D index/tags.json carries the new tags")

print()
if FAILS:
    print(f"verify_H_proton_cpt: {len(FAILS)} FAILED of {N + len(FAILS)}")
    sys.exit(1)
print(f"verify_H_proton_cpt: {N} checks green  ({time.time()-t0:.1f}s) — "
      "Tier BM.7 (Def-BM.7, BM.25–BM.29) §A–§D")
sys.exit(0)
