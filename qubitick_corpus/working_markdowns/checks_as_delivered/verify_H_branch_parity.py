#!/usr/bin/env python3
"""
verify_H_branch_parity.py — machine verification of FT.101 (H12, Tier F.34):
the weak branch grading of the two-branch crystallization.

Exact arithmetic only (complex over Fraction = Q(i); integers; exhaustive
enumeration). No floating point anywhere.

Sections:
  §A  pair-register identities: Pi_R/Pi_V projectors (idempotent, orthogonal,
      sum I4, traces 3/1, ranks 3/1); Pi_V = |Psi-><Psi-|; [S, W_i] = 0;
      W_i Pi_V = 0 = Pi_V W_i (all i, entrywise); W_i = Pi_R W_i Pi_R with
      nonzero witnesses; sum_i W_i^2 = (3/2)E_0 + (1/2)Sigma = 2 Pi_R;
      Casimir reads 2 on all three triplet basis vectors, 0 on the singlet;
      joint kernel of (W1;W2;W3) = im Pi_V (rank 3, dimension count).
  §B  the branch flip: Aut(Phi) = Z2 exhaustive on {0,pi}; iota(alpha) = pi - alpha;
      alignment-pattern complement census — membership flip equals alpha-flip on
      every edge, exhaustive for |E_R| = 1..5 (all 2^n patterns); uniform
      patterns exchange (empty <-> E_R); pattern count 2^|E_R| [EM.23(4)].
  §C  no Hilbert-space branch swap: trace and rank are conjugation invariants;
      Tr Pi_R = 3 != 1 = Tr Pi_V; rk 3 != 1 (exact elimination); hence no
      invertible M with M Pi_R M^-1 = Pi_V, and no linear bijection vee^2 -> wedge^2.
  §D  sharp-branch witnesses (CT0.8 at eps_q = 0): branch-0 state Pi_R/3 has
      |Pi_V rho| = 0 and W_3 rho != 0; branch-pi state Pi_V has |Pi_V rho| = 1
      and W_i rho = 0 for all i; the weak-activity predicate is flip-asymmetric.
  §E  document pins: H12 Tier F.34 + FT.101 structure (Thm/Req/Pf/Phys/Status,
      blacksquare, Req content); H12 header Order + Machine lines; H13 item 20
      carries the [FT.101] addition and the Legacy dynamics import registry
      carries FT.101; the four frozen adjudication phrases still occur exactly
      8 times across H (2 each); barred identifications absent from FT.101.

Run: python3 verify_H_branch_parity.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import os
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

import re
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from qmath import C, matmul, conj_transpose, trace  # noqa: E402

PASS = FAIL = 0


def chk(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {name} {detail}")


I = C(0, 1)

# ---------------------------------------------------------------- Pauli data
S0 = [[C(1), C(0)], [C(0), C(1)]]
S1 = [[C(0), C(1)], [C(1), C(0)]]
S2 = [[C(0), -I], [I, C(0)]]
S3 = [[C(1), C(0)], [C(0), C(-1)]]
SIG = [S0, S1, S2, S3]


def kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb] for j in range(ca * cb)]
            for i in range(ra * rb)]


def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(4)] for i in range(4)]


def mscale(A, x):
    return [[a * x for a in row] for row in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


def mzero(A):
    return all(A[i][j] == C(0) for i in range(4) for j in range(4))


GB = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
E0 = GB[0][0]
SGM = madd(madd(GB[1][1], GB[2][2]), GB[3][3])                 # Sigma
W = [mscale(madd(GB[0][i], GB[i][0]), Fr(1, 2)) for i in (1, 2, 3)]
SWAP = mscale(madd(E0, SGM), Fr(1, 2))                          # S = (E0+Sigma)/2
PR = mscale(madd(mscale(E0, 3), SGM), Fr(1, 4))                 # (3E0+Sigma)/4
PV = mscale(madd(E0, SGM, -1), Fr(1, 4))                        # (E0-Sigma)/4
I4 = [[C(1 if i == j else 0) for j in range(4)] for i in range(4)]


def rank(M):
    """exact rowspace rank over Q(i) (Gaussian elimination)."""
    M = [row[:] for row in M]
    r = 0
    for cidx in range(len(M[0])):
        piv = None
        for rr in range(r, len(M)):
            if M[rr][cidx] != C(0):
                piv = rr
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cidx]
        M[r] = [x / pv for x in M[r]]
        for rr in range(len(M)):
            if rr != r and M[rr][cidx] != C(0):
                f = M[rr][cidx]
                M[rr] = [x - f * y for x, y in zip(M[rr], M[r])]
        r += 1
    return r


def mvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(4)) for i in range(4)]


# ---------------------------------------------------------------- §A
def sectionA():
    print("S1 = §A pair-register identities (exact over Q(i))")
    chk("§A Pi_R + Pi_V = I4; both idempotent; Pi_R Pi_V = 0; Tr = 3 / 1 [CT0.7(1)]",
        meq(madd(PR, PV), I4)
        and meq(matmul(PR, PR), PR) and meq(matmul(PV, PV), PV)
        and mzero(matmul(PR, PV))
        and trace(PR) == C(3) and trace(PV) == C(1))
    sing = [[C(0)] * 4 for _ in range(4)]
    for (a, sa) in ((1, 1), (2, -1)):
        for (b, sb) in ((1, 1), (2, -1)):
            sing[a][b] = C(Fr(sa * sb, 2))
    chk("§A Pi_V = |Psi-><Psi-| exactly (the singlet line is wedge^2)", meq(PV, sing))
    chk("§A [S, W_i] = 0 for all i (S W_i S = W_i)",
        all(meq(matmul(matmul(SWAP, Wi), SWAP), Wi) for Wi in W))
    chk("§A W_i Pi_V = 0 = Pi_V W_i for all i, entrywise [FT.93(5)]",
        all(mzero(matmul(Wi, PV)) and mzero(matmul(PV, Wi)) for Wi in W))
    chk("§A W_i = Pi_R W_i = W_i Pi_R = Pi_R W_i Pi_R for all i, with nonzero witnesses",
        all(meq(matmul(Wi, PR), Wi) and meq(matmul(PR, Wi), Wi)
            and meq(matmul(matmul(PR, Wi), PR), Wi) and not mzero(Wi) for Wi in W))
    cas = madd(madd(matmul(W[0], W[0]), matmul(W[1], W[1])), matmul(W[2], W[2]))
    chk("§A sum_i W_i^2 = (3/2)E_0 + (1/2)Sigma = 2 Pi_R [CT0.7a]",
        meq(cas, madd(mscale(E0, Fr(3, 2)), mscale(SGM, Fr(1, 2))))
        and meq(cas, mscale(PR, 2)))
    trips = [[C(1), C(0), C(0), C(0)],                       # |00>
             [C(0), C(Fr(1, 2)), C(Fr(1, 2)), C(0)],         # (|01>+|10>)/2 (eigenvector, unnormalized)
             [C(0), C(0), C(0), C(1)]]                       # |11>
    v_sing = [C(0), C(Fr(1, 2)), C(Fr(-1, 2)), C(0)]         # (|01>-|10>)/2
    chk("§A Casimir read: sum W^2 v = 2v on all three triplet basis vectors; = 0 on the singlet",
        all(meq_vec(mvec(cas, v), mscale_vec(v, 2)) for v in trips)
        and mzero_vec(mvec(cas, v_sing)))
    blk = []
    for Wi in W:
        blk += Wi
    chk("§A joint kernel: rank (W1;W2;W3) stacked = 3 => dim ker = 1 = dim im Pi_V; "
        "with W_i Pi_V = 0 this pins ker = im Pi_V exactly",
        rank(blk) == 3 and rank(PV) == 1)


def mscale_vec(v, x):
    return [a * x for a in v]


def meq_vec(a, b):
    return all(x == y for x, y in zip(a, b))


def mzero_vec(v):
    return all(x == C(0) for x in v)


# ---------------------------------------------------------------- §B
def sectionB():
    print("S2 = §B the branch flip (label level, exhaustive)")
    # Aut(Phi): maps {0,1} -> {0,1} (1 = pi); automorphisms = bijections
    maps = []
    for f0 in (0, 1):
        for f1 in (0, 1):
            if len({f0, f1}) == 2:
                maps.append((f0, f1))
    chk("§B |Aut(Phi)| = 2 for Phi = {0, pi}: identity and iota(alpha) = pi - alpha; "
        "iota^2 = id, iota != id (exhaustive)",
        len(maps) == 2 and (0, 1) in maps and (1, 0) in maps)
    # pattern-complement census: membership flip == alpha flip, every edge, all patterns
    ok = True
    counts = {}
    for nE in range(1, 6):
        pats = set()
        for pat in range(2 ** nE):
            alpha = [0 if (pat >> e) & 1 == 0 else 1 for e in range(nE)]
            flip = [1 - a for a in alpha]
            P = frozenset(e for e in range(nE) if alpha[e] == 1)
            Pc = frozenset(range(nE)) - P
            Pflip = frozenset(e for e in range(nE) if flip[e] == 1)
            if Pflip != Pc:
                ok = False
            pats.add(P)
        counts[nE] = len(pats)
    chk("§B alignment-pattern complement = per-edge alpha-flip: exhaustive for |E_R| = 1..5 "
        "(all 2^n patterns); uniform patterns exchange (P = empty <-> P = E_R)",
        ok and all(counts[n] == 2 ** n for n in counts))


# ---------------------------------------------------------------- §C
def sectionC():
    print("S3 = §C no Hilbert-space branch swap (invariant obstruction)")
    chk("§C Tr and rank are conjugation invariants; Tr Pi_R = 3 != 1 = Tr Pi_V; rk 3 != 1: "
        "no invertible M in End(C^4) with M Pi_R M^-1 = Pi_V, and no linear bijection "
        "vee^2 -> wedge^2 (dimensions 3 vs 1)",
        trace(PR) == C(3) and trace(PV) == C(1) and rank(PR) == 3 and rank(PV) == 1)


# ---------------------------------------------------------------- §D
def sectionD():
    print("S4 = §D sharp-branch witnesses (CT0.8 at eps_q = 0)")
    rho0 = mscale(PR, Fr(1, 3))            # branch-0 witness: faithful on vee^2, trace 1
    w0 = trace(matmul(PV, rho0))           # |Pi_V rho| = Tr(Pi_V rho) [D0.2]
    chk("§D branch alpha=0 witness rho = Pi_R/3: Tr rho = 1, |Pi_V rho| = 0 <= eps_q = 0; "
        "W_3 rho != 0 (weak-active, entrywise)",
        trace(rho0) == C(1) and w0 == C(0) and not mzero(matmul(W[2], rho0)))
    chk("§D branch alpha=pi witness rho = Pi_V: Tr rho = 1, |Pi_V rho| = 1 >= 1 - eps_q; "
        "W_i rho = 0 for all i (weak-blind)",
        trace(PV) == C(1) and trace(matmul(PV, PV)) == C(1)
        and all(mzero(matmul(Wi, PV)) for Wi in W))
    act0 = any(not mzero(matmul(Wi, rho0)) for Wi in W)
    actp = any(not mzero(matmul(Wi, PV)) for Wi in W)
    chk("§D flip-asymmetry of the weak-activity predicate: act(alpha=0) = True, "
        "act(alpha=pi) = False — the branch exchange does not preserve the weak support",
        act0 and not actp)


# ---------------------------------------------------------------- §E pins
def sectionE():
    print("S5 = §E document pins of the branch-grading pass")

    def rd(fn):
        return era_paths.read(fn)

    if ARCH:
        H12 = rd("H_archive/H12_chirality_and_form_factor.md")
        H13 = rd("H_archive/H13_registries_and_gaps.md")
        chk("§E H12 carries Tier F.34 and FT.101",
            "## Tier F.34 — " in H12 and "### FT.101 — " in H12)
        blk = H12[H12.index("### FT.101 — "):]
    if ARCH:
        blk = blk[:blk.index("\n---\n")] if "\n---\n" in blk else blk
        chk("§E FT.101 block complete: Thm/Req/Pf/Phys/Status + blacksquare",
            all(p in blk for p in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "**Status.**"))
            and "\\blacksquare" in blk)
        chk("§E FT.101 Req cites A3, A4, D0.5, CT0.7, CT0.7a, CT0.8, CT0.9, CT1.1, CT1.2, "
            "CT1.11a, Def-EM.21, EM.23, EM.24, FT.13, FT.93",
            all(t in blk for t in ("A3", "A4", "D0.5", "CT0.7", "CT0.7a", "CT0.8", "CT0.9",
                                   "CT1.1", "CT1.2", "CT1.11a", "Def-EM.21", "EM.23", "EM.24",
                                   "FT.13", "FT.93")))
        chk("§E FT.101 carries the scope clause: deficit 1 untouched, pincer stands",
            "deficit 1 of item 20 is untouched" in blk and "FT.93(3)" in blk and "FT.93(7)" in blk)
        chk("§E FT.101 free of barred identifications: no 'left-handed', 'right-handed', "
            "'SU(2)_L', 'neutrino', 'Weyl' in the block",
            not re.search(r"left-handed|right-handed|SU\(2\)_L|neutrino|Weyl", blk))
        chk("§E H12 header: Order line carries Tier F.34 (FT.101); Machine line carries "
            "verify_H_branch_parity.py; DAG line H02 (4 tags)",
            "Tier F.34 (FT.101)" in H12 and "verify_H_branch_parity.py" in H12
            and "H02 (4 tags)" in H12)
        chk("§E H13: item 20 carries the [FT.101] addition; Legacy dynamics import registry "
            "carries FT.101 as item (5)",
            "[FT.101]" in H13 and "FT.101 — the weak branch grading" in H13)
    # frozen adjudication phrases: exactly 8 occurrences across H (2 per phrase)
    phrases = ["S-parity fracture", "automatic chiral selectivity", "Janus-mediated",
               "Higgs pathway"]
    total = 0
    if ARCH:
        ARCHD = os.path.join(DOCS, "H_archive")
    if ARCH:
        for fn in os.listdir(ARCHD):
            if re.match(r"^H\d\d_.*\.md$", fn):
                total += sum(era_paths.read(fn).count(p) for p in phrases)
        chk("§E the four frozen adjudication phrases still occur exactly 8 times across H "
            "(FT.101 text adds none)", total == 8, str(total))


def main():
    print("verify_H_branch_parity: FT.101 weak branch grading (exact)")
    sectionA()
    sectionB()
    sectionC()
    sectionD()
    sectionE()
    print(f"verify_H_branch_parity: {PASS} checks green" + (f", {FAIL} FAILED" if FAIL else ""))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
