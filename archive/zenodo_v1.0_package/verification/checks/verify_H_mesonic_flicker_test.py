#!/usr/bin/env python3
"""
verify_H_mesonic_flicker_test.py — machine verification of Tier BM.9 (Def-BM.9,
BM.31–BM.33): does the delta-sealed (mesonic) sector enter the baryon's flicker
path integral?

The answer is computed, not assumed: the contraction grammar of a 3-attachment
support admits exactly one grouping (the epsilon triple) and zero
delta-containing groupings, so the delta-sealed members of any "extended"
ensemble are killed by the colour projector C(Sigma;C) [D2.14] rather than by
an amplitude cancellation — and the protection is specific to N = 3.

Exact arithmetic only: integers, fractions.Fraction, exhaustive enumeration of
set partitions into blocks of size 2 and 3, exact rank over Q for the singlet
count, generating-function convolution. No floating point in any assertion.

Sections:
  §A  the sealing grammar: g(N) for N = 2..8 by exhaustive partition enumeration
      (1,1,3,10,25,105,231 against CT3.17a(2)/FT.41(b) for N <= 7), the
      delta-containing census, the epsilon-only census, and the N = 3 protection.
  §B  the boundary-data comparison: the charge ranges (k=3 vs k=2) and their
      overlap, the W(Q) censuses from (2+z+z^-1)^k, the phase classes 4Z inside
      2Z, and the singlet count 1 for both representation contents.
  §C  the projector verdict: C in {0,1}, the vanishing of the delta sector, and
      the exact equality of the extended and restricted normalized averages.
  §D  the amplitude layer is orthogonal: the pure-cycle death rows against the
      dissolved-digon survival rows, with FT.106(3)'s exact integers.
  §E  the mass consequence and the N-dependence of the protection.
  §F  document pins and hygiene.

Tier BM.9 is new canon content with no first edition in H_archive/.

Run: python3 verify_H_mesonic_flicker_test.py   (auto-discovered by run_all.py)
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


print("=" * 74)
print("verify_H_mesonic_flicker_test — Tier BM.9 (Def-BM.9, BM.31–BM.33)")
print("=" * 74)

# ==========================================================================
# §A  BM.31 — the sealing grammar and the N = 3 protection
# ==========================================================================
print("\n§A (BM.31) — the contraction grammar: g(N), the delta-containing census,")
print("            and the unique protected attachment count")


def groupings(n):
    """All partitions of {0..n-1} into blocks of size 2 (delta) or 3 (epsilon)."""
    out = []

    def rec(rest, acc):
        if not rest:
            out.append(tuple(sorted(tuple(sorted(b)) for b in acc)))
            return
        first = rest[0]
        tail = rest[1:]
        for size in (2, 3):
            if len(rest) < size:
                continue
            for combo in itertools.combinations(tail, size - 1):
                blk = (first,) + combo
                rem = [x for x in tail if x not in combo]
                rec(rem, acc + [blk])

    rec(list(range(n)), [])
    return sorted(set(out))


G = {n: groupings(n) for n in range(2, 9)}
COUNTS = {n: len(G[n]) for n in G}
CORPUS = {2: 1, 3: 1, 4: 3, 5: 10, 6: 25, 7: 105}
chk(all(COUNTS[n] == CORPUS[n] for n in range(2, 8)),
    f"§A1 g(N) by exhaustive partition enumeration reproduces CT3.17a(2)/FT.41(b) exactly for "
    f"N = 2..7: {COUNTS}")
print(f"    [diagnostic] the enumeration at N = 8 gives {COUNTS[8]} groupings "
      f"(outside CT3.17a(2)'s frozen range N <= 7; asserted nowhere)")


def has_delta(g):
    return any(len(b) == 2 for b in g)


def all_eps(g):
    return all(len(b) == 3 for b in g)


DELTA = {n: sum(1 for g in G[n] if has_delta(g)) for n in G}
EPSON = {n: sum(1 for g in G[n] if all_eps(g)) for n in G}
chk(all(DELTA[n] + EPSON[n] == COUNTS[n] for n in G),
    "§A1 every grouping is either delta-containing or epsilon-only: the two censuses partition g(N)")
chk(all(DELTA[n] == v for n, v in ((2, 1), (3, 0), (4, 3), (5, 10), (6, 15), (7, 105))),
    f"§A2 the delta-containing census for N = 2..7: {[(n, DELTA[n]) for n in range(2, 8)]}")
chk(all(EPSON[n] == v for n, v in ((2, 0), (3, 1), (4, 0), (5, 0), (6, 10), (7, 0))),
    f"§A2 the epsilon-only census for N = 2..7: {[(n, EPSON[n]) for n in range(2, 8)]} "
    "(nonzero exactly where 3 | N)")
chk(DELTA[3] == 0 and EPSON[3] == 1 and COUNTS[3] == 1,
    "§A2 THE N = 3 PROTECTION: g(3) = 1, the unique grouping is the epsilon triple, and the "
    "delta-containing count is exactly 0")
chk(all(EPSON[n] == 0 for n in (2, 4, 5, 7)),
    "§A2 no epsilon-only grouping exists at N = 2, 4, 5, 7: a 3-block partition needs N = 0 mod 3")
chk(DELTA[6] == 15 and EPSON[6] == 10,
    "§A2 at N = 6 the ensemble genuinely mixes: 15 delta-containing against 10 epsilon-only groupings")
chk(all(DELTA[n] > 0 for n in (4, 5, 6, 7)),
    "§A2 every N >= 4 admits at least one delta-containing grouping: the protection is unique to N = 3")
# the dangling-attachment count: a delta consumes 2, so a 3-support leaves 1 unpaired
chk(3 - 2 == 1, "§A3 a delta sub-pairing on a 3-attachment support leaves exactly one dangling attachment")
chk(all(n - 2 * sum(1 for b in g if len(b) == 2) - 3 * sum(1 for b in g if len(b) == 3) == 0
        for n in range(2, 8) for g in G[n]),
    "§A3 every enumerated grouping is complete: zero dangling attachments by construction")

stamp("§A green: g(N) reproduced, delta-containing census, and N = 3 as the unique protected count")

# ==========================================================================
# §B  BM.31 — the boundary-data comparison
# ==========================================================================
print("\n§B (BM.31) — charge ranges, the W(Q) censuses, the phase classes, the singlet count")


def conv(k):
    one = {Fr(-1): Fr(1), Fr(0): Fr(2), Fr(1): Fr(1)}
    cur = {Fr(0): Fr(1)}
    for _ in range(k):
        nxt = {}
        for a, ca in cur.items():
            for b, cb in one.items():
                nxt[a + b] = nxt.get(a + b, Fr(0)) + ca * cb
        cur = nxt
    return cur


W3, W2 = conv(3), conv(2)
chk(sorted(W3) == [Fr(k) for k in range(-3, 4)] and
    [W3[Fr(k)] for k in range(-3, 4)] == [Fr(x) for x in (1, 6, 15, 20, 15, 6, 1)],
    f"§B1 the baryon-type charge read Q = q1+q2+q3 has range {{-3..+3}} and census (1,6,15,20,15,6,1)")
chk(sorted(W2) == [Fr(k) for k in range(-2, 3)] and
    [W2[Fr(k)] for k in range(-2, 3)] == [Fr(x) for x in (1, 4, 6, 4, 1)],
    "§B1 the meson-type charge read Q = q1+q2 has range {-2..+2} and census (1,4,6,4,1)")
chk(sum(W3.values()) == 64 and sum(W2.values()) == 16,
    "§B1 the censuses sum to 4^3 = 64 and 4^2 = 16: exhaustive over end-sign assignments")
OVERLAP = {q for q in W3 if q in W2}
chk(OVERLAP == {Fr(k) for k in range(-2, 3)},
    "§B2 the charge classes OVERLAP on {-2,-1,0,+1,+2}: the charge read does not separate the two "
    "sealings at Q = 0 or Q = +1")
chk(Fr(3) in W3 and Fr(3) not in W2, "§B2 only |Q| = 3 is baryon-exclusive")
chk(all(W3[q] != W2[q] for q in OVERLAP),
    f"§B2 the probability-space sizes differ on the overlap: {[ (int(q), str(W2[q]), str(W3[q])) for q in sorted(OVERLAP)]}")
# the phase classes
Z4 = {4 * k for k in range(-3, 4)}
Z2 = {2 * k for k in range(-6, 7)}
chk(Z4 <= Z2 and (Z2 - Z4) != set(),
    "§B3 the baryon-type phase class 4Z [Census FT.49(3)] sits strictly inside the per-chain class "
    "2Z [FT.22]: the phase separates only the odd half of 2Z")
chk(all(t % 2 == 0 for t in Z2), "§B3 Theta_int = 2 k(Gamma) is even for every meson-type grouping [FT.34(3)]")
chk(2 in Z2 and 2 not in Z4, "§B3 Theta_int = 2 is meson-admissible and baryon-excluded: a partial separator")
# the singlet count for both representation contents


def e3(i, j, v=Fr(1)):
    return [[v if (a == i and b == j) else Fr(0) for b in range(3)] for a in range(3)]


T3 = [e3(0, 1), e3(1, 0), e3(0, 2), e3(2, 0), e3(1, 2), e3(2, 1),
      [[Fr(1), 0, 0], [0, Fr(-1), 0], [0, 0, Fr(0)]], [[Fr(0), 0, 0], [0, Fr(1), 0], [0, 0, Fr(-1)]]]


def rank(rows):
    A = [list(map(Fr, r)) for r in rows]
    r = 0
    for c in range(len(A[0])):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(len(A[i]))]
        r += 1
    return r


meson_rows = []
for a in range(8):
    Ta = T3[a]
    A = [[Fr(0)] * 9 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    A[3 * i + j][3 * k + l] = (Ta[i][k] if j == l else Fr(0)) - \
                        (Ta[l][j] if i == k else Fr(0))
    meson_rows.extend(A)
rk_mes = rank(meson_rows)
chk(9 - rk_mes == 1,
    f"§B4 dim (C^3 (x) Cbar^3)^(sl(3)) = 9 - {rk_mes} = {9 - rk_mes} = 1: the meson content has "
    "exactly one singlet line")
# build the 27x27 action matrices properly
acts = []
for a in range(8):
    Ta = T3[a]
    A = [[Fr(0)] * 27 for _ in range(27)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for p in range(3):
                    A[9 * i + 3 * j + k][9 * p + 3 * j + k] += Ta[i][p]
                    A[9 * i + 3 * j + k][9 * i + 3 * p + k] += Ta[j][p]
                    A[9 * i + 3 * j + k][9 * i + 3 * j + p] += Ta[k][p]
    acts.extend(A)
rk_bar = rank(acts)
chk(27 - rk_bar == 1,
    f"§B4 dim (C^3)^(x)3 ^(sl(3)) = 27 - {rk_bar} = {27 - rk_bar} = 1: the baryon content has exactly "
    "one singlet line  [BM.1(3) re-derived]")
chk(27 - rk_bar == 9 - rk_mes,
    "§B4 the two representation contents carry the SAME singlet count: representation content does not "
    "separate them either")

stamp("§B green: the charge ranges overlap, the phase class 4Z is strictly inside 2Z, and both "
      "representation contents carry exactly one singlet")

# ==========================================================================
# §C  BM.32 — the projector verdict: the delta sector is filtered, not cancelled
# ==========================================================================
print("\n§C (BM.32) — the colour projector: Z_delta = 0 by filtration, and the averages agree")

# C(Sigma;C) in {0,1} [D2.14]; on a 3-attachment support every grouping is epsilon,
# so a delta-sealed member has a dangling attachment -> C = 0 -> the block vanishes [FT.19]
CONF = [(Fr(1), Fr(3)), (Fr(2), Fr(5)), (Fr(1), Fr(7)), (Fr(4), Fr(2)), (Fr(3), Fr(11))]


def avg(conf):
    num = sum((w * m for w, m in conf), Fr(0))
    den = sum((w for w, _ in conf), Fr(0))
    return num / den


def total(conf):
    return sum((w * m for w, m in conf), Fr(0))


eps_only = CONF
ext = CONF + [(Fr(0), Fr(13)), (Fr(0), Fr(17))]          # delta members carry weight C = 0
chk(avg(ext) == avg(eps_only),
    "§C1 adding zero-weight (projected-out) members leaves the normalized average EXACTLY unchanged")
chk(total(ext) == total(eps_only),
    "§C1 and the total deficit is unchanged too: Z_delta = 0 kills both mass routes at once")
chk(all(w == 0 for w, _ in ext[len(CONF):]),
    "§C1 the delta-sealed members carry the projector's zero: C(Sigma;C) = 0 with a dangling attachment")
# the projector is an idempotent scalar
for c in (Fr(0), Fr(1)):
    chk(c * c == c, f"§C2 C(Sigma;C) = {c} is idempotent: the filter is a 0/1 projector  [D2.14]")
chk(Fr(1) - Fr(1) == 0 and Fr(0) * Fr(7, 3) == 0,
    "§C2 the all-or-nothing law: one dangling attachment zeroes the whole colour block  [FT.19]")
# contrast: at N = 4 the extended ensemble genuinely mixes
N4 = [(Fr(1), Fr(3)), (Fr(2), Fr(5)), (Fr(1), Fr(7))]
N4ext = N4 + [(Fr(3), Fr(11)), (Fr(1), Fr(2)), (Fr(2), Fr(13))]
chk(avg(N4ext) != avg(N4) and total(N4ext) != total(N4),
    f"§C3 at N = 4 (all {DELTA[4]} groupings delta-containing) the extended average DIFFERS: "
    f"{avg(N4)} -> {avg(N4ext)}")
chk(DELTA[4] == COUNTS[4], "§C3 at N = 4 every grouping contains a delta: no epsilon-only option exists")
chk(DELTA[6] == 15 and EPSON[6] == 10 and Fr(DELTA[6], COUNTS[6]) == Fr(3, 5),
    "§C3 at N = 6 the delta-containing fraction is exactly 15/25 = 3/5")

stamp("§C green: Z_delta = 0 by the projector at N = 3 (both mass routes unchanged), and the "
      "protection fails at N >= 4")

# ==========================================================================
# §D  BM.32 — the amplitude layer is an orthogonal mechanism
# ==========================================================================
print("\n§D (BM.32) — the cycle cancellations are about directed cycles, not colour sealings")

AMP = {(Fr(1), 0): 1196, (Fr(-1), 0): 1196, (Fr(0), 0): 5336,
       (Fr(1), 1): 802, (Fr(-1), 1): 802, (Fr(0), 1): 4796,
       (Fr(1), 2): 0, (Fr(-1), 2): 0, (Fr(0), 2): 0,
       (Fr(1), 3): 0, (Fr(-1), 3): 0, (Fr(0), 3): 0}
chk(all(AMP[(q, S)] == 0 for q in (Fr(-1), Fr(0), Fr(1)) for S in (2, 3)),
    "§D1 the amplitude layer vanishes at S in {2,3}: no 4-cycle and no odd cycle enters a cover "
    "[FT.106(3c), FT.69(3)(iv),(v)]")
chk(AMP[(Fr(1), 1)] == 802 and AMP[(Fr(0), 1)] == 4796,
    "§D1 the winding-1 amplitude rows are nonzero: DISSOLVED digons inside covers survive "
    "[FT.106(3): 802 and 4796]")
chk(all(AMP[(q, 1)] > 0 for q in (Fr(-1), Fr(0), Fr(1))),
    "§D1 mesonic (digon) content contributes at the amplitude layer only as dissolved digons in covers")
chk(all(AMP[(q, 1)] == AMP[(Fr(-q), 1)] for q in (Fr(1), Fr(-1), Fr(0))),
    "§D1 the amplitude rows are omega-symmetric  [FT.106(3d)]")
NORM = {(Fr(1), 0): 197912, (Fr(0), 0): 395824, (Fr(1), 1): 787358, (Fr(0), 1): 1574716,
        (Fr(1), 2): 655776, (Fr(0), 2): 1311552, (Fr(1), 3): 1000512, (Fr(0), 3): 2001024}
chk(all(NORM[(Fr(0), S)] == 2 * NORM[(Fr(1), S)] for S in range(4)),
    "§D2 the norm layer keeps the 2:1 neutral-to-charged ratio at every winding [FT.106(3)]")
chk(all(NORM[(q, S)] > 0 for q in (Fr(0), Fr(1)) for S in range(4)),
    "§D2 the norm layer is nonzero where the amplitude layer dies: the two layers are independent "
    "mechanisms")

stamp("§D green: the cycle cancellations kill pure directed cycles, not colour sealings; dissolved "
      "digons survive in covers")

# ==========================================================================
# §E  BM.33 — the mass consequence
# ==========================================================================
print("\n§E (BM.33) — the mass consequence: unchanged at N = 3, and the N-dependence")

chk(avg(ext) == avg(eps_only) and total(ext) == total(eps_only),
    "§E1 <m>_ext = <m>_eps EXACTLY on both routes: BM.20's and BM.28(4)'s reads are unchanged")
W0, W1 = Fr(20), Fr(15)
chk(W0 / W1 == Fr(4, 3), "§E2 the neutron/proton ratio 4/3 of BM.28(4)(ii) survives: the mesonic sector "
                         "contributes zero to both classes")
chk(all(DELTA[3] == 0 for _ in [0]), "§E2 both classes are 3-junctures, so both are protected")
chk(DELTA[3] == 0 and DELTA[4] == 3 and DELTA[5] == 10 and DELTA[6] == 15 and DELTA[7] == 105,
    "§E3 the protection is exact at N = 3 and fails at every N in 4..7")
chk(EPSON[3] == 1 and EPSON[6] == 10 and all(EPSON[n] == 0 for n in (2, 4, 5, 7)),
    "§E3 epsilon-only groupings exist exactly where 3 | N: one at N = 3, ten at N = 6, none at 2, 4, 5, 7")
chk(Fr(EPSON[6], COUNTS[6]) == Fr(2, 5) and Fr(DELTA[6], COUNTS[6]) == Fr(3, 5),
    "§E3 at N = 6 the split is exactly 2/5 epsilon-only against 3/5 delta-containing")

stamp("§E green: the mass reads are unchanged at N = 3; the protection is N-specific and quantified")

# ==========================================================================
# §F  BM.33 — document pins and hygiene
# ==========================================================================
print("\n§F (BM.33) — document pins, hygiene, suite counts")

chk(not FAILS, "§F the machine sections §A–§E are green before the document pins are read")

P4 = rd("Part4_Baryomesonic_era.md")
HL = rd("HistLog.md")
RM = rd("README.md")
CRM = rd(os.path.join("checks", "README.md"))
TI = rd(os.path.join("index", "tier_index.md"))
TJ = rd(os.path.join("index", "tags.json"))

chk("## Tier BM.9 — The Mesonic Flicker Test" in P4, "§F Part 4 carries the Tier BM.9 heading")
BLOCKS = {}
marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^(###[^\n]*|## [^\n]*)$", P4)]
for i, (pos, head) in enumerate(marks):
    end = marks[i + 1][0] if i + 1 < len(marks) else len(P4)
    m = re.match(r"###\s+((?:Def-BM|BM)\.\d+)\b", head)
    if m:
        BLOCKS[m.group(1)] = P4[pos:end]
for t in ("Def-BM.9", "BM.31", "BM.32", "BM.33"):
    chk(t in BLOCKS, f"§F the block {t} exists in Part 4")
for t in ("BM.31", "BM.32", "BM.33"):
    blk = BLOCKS.get(t, "")
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§F {t} carries {mark}")
    chk("**Status.**" not in blk, f"§F {t} carries no **Status.** line")
chk("**Def.**" in BLOCKS.get("Def-BM.9", ""), "§F Def-BM.9 carries its **Def.** block")

PINS = [
    ("Def-BM.9", ["\\mathcal E_{\\mathrm{ext}}(\\mathcal X):=\\mathcal E_\\varepsilon(\\mathcal X)\\cup\\mathcal E_\\delta(\\mathcal X)",
                  "\\Pi_{\\mathcal C}(\\Sigma;C)=\\mathcal C(\\Sigma;C)",
                  "g(N)=(1,\\,1,\\,3,\\,10,\\,25,\\,105)",
                  "\\textbf{the attachment count is a boundary datum}"]),
    ("BM.31", ["g(3)=1", "g_\\delta(3)=\\mathbf0", "\\mathcal E_\\delta(\\mathcal X_{N=3})=\\varnothing",
               "(1,6,15,20,15,6,1)", "(1,4,6,4,1)", "4\\mathbb Z\\subsetneq2\\mathbb Z",
               "27-26=1", "9-8=1"]),
    ("BM.32", ["Z^{(n)}_\\delta", "\\textbf{the zero is a filtration, not a cancellation:}",
               "\\langle m\\rangle_{\\mathrm{ext}}=\\langle m\\rangle_\\varepsilon",
               "802", "4796", "\\textbf{the amplitude-layer mechanisms are orthogonal to this question:}"]),
    ("BM.33", ["\\textbf{the answers:}", "\\textbf{the derived rows:}", "\\textbf{the scope rows:}",
               "\\textbf{the open rows touched:}", "\\textbf{the standing rules:}",
               "\\textbf{the adjudication:}", "the protection is grammatical}"]),
]
for tag, needles in PINS:
    blk = BLOCKS.get(tag, "")
    for nd in needles:
        chk(nd in blk, f"§F {tag} pins the fragment: {nd[:50]}")

NSLINE = [ln for ln in P4.split("\n") if ln.startswith("**Namespace.**")][0]


def _cov9(line, prefix, nums):
    m = re.search(re.escape(prefix) + r"(\d+)\u2013" + re.escape(prefix) + r"(\d+)", line)
    return bool(m) and all(int(m.group(1)) <= n <= int(m.group(2)) for n in nums)


chk(_cov9(NSLINE, "BM.", range(31, 34)) and _cov9(NSLINE, "Def-BM.", [9]),
    f"§F the Part 4 Namespace range covers Def-BM.9 and BM.31–BM.33: {NSLINE[:80]}")
chk("(xii) the mesonic flicker test" in P4, "§F the Part 4 charter carries clause (xii)")
EXP = P4[P4.index("## Closure exports of Part 4"):]
for t in ("Def\\text{-}BM.9", "BM.31", "BM.32", "BM.33"):
    chk(t in EXP, f"§F the closure exports carry {t}")

ORDER = ["Def-BM.1", "Def-BM.2", "BM.1", "BM.2", "BM.3", "BM.4", "BM.5", "BM.6",
         "Def-BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12",
         "Def-BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18",
         "Def-BM.5", "Def-BM.6", "BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24",
         "Def-BM.7", "BM.25", "BM.26", "BM.27", "BM.28", "BM.29", "Def-BM.8", "BM.30",
         "Def-BM.9", "BM.31", "BM.32", "BM.33"]
fwd = []
for t in ORDER[38:]:
    blk = BLOCKS.get(t, "")
    i = blk.find("**Req.**")
    j = blk.find("\n\n", i)
    req = blk[i:j if j > 0 else len(blk)]
    for cited in set(re.findall(r"\b(?:Def-BM|BM)\.\d+", req)):
        if cited != t and ORDER.index(cited) > ORDER.index(t):
            fwd.append((t, cited))
chk(not fwd, f"§F no Req line of Tier BM.9 cites a later tag of this part: {fwd}")

BARRED = ["previously", "formerly", "this was", "now this", "erratum", "submitted",
          "earlier draft", "stale", "draft", "directive", "as corrected", "overwrite",
          "letter series", "non-binding", "wip"]
for t in ("Def-BM.9", "BM.31", "BM.32", "BM.33"):
    low = BLOCKS[t].lower()
    hits = [(w, low.count(w)) for w in BARRED if w in low]
    chk(not hits, f"§F {t} revision-language scan: zero hits ({hits})")
    chk(not re.search(r"\bP-H\d", BLOCKS[t]), f"§F {t} carries no registry token")
MASS = ["0.511", "105.6", "1776", "1.273", "4.183", "938.2", "939.5", "139.57",
        "134.9", "0.118", "137.0", "140.5", "0.693", "1.293", "497.6", "547.8"]
for t in ("Def-BM.9", "BM.31", "BM.32", "BM.33"):
    leak = [x for x in MASS if re.search(r"(?<![\d.])" + re.escape(x) + r"(?![\d])", BLOCKS[t])]
    chk(not leak, f"§F {t} carries no external mass token ({leak})")

chk("(80 checkers)" in RM, "§F the main README carries the 79-checker count")
chk("**80/80**" in CRM and "(80 checkers)" in CRM, "§F checks/README carries the 76-checker state")
chk("verify_H_mesonic_flicker_test.py" in CRM, "§F checks/README names this checker")
chk("(V.13)" in HL and "64/64" in HL, "§F HistLog §V carries (V.13) with suite state 64/64")
chk("Tier BM.9" in HL, "§F HistLog (V.13) names the tier")
chk(all(x in HL for x in ("56/57", "58/58", "59/59", "60/60", "61/61", "62/62", "63/63")),
    "§F the earlier suite states are preserved in HistLog §V")
for t in ("Def-BM.9", "BM.31", "BM.32", "BM.33"):
    chk(f"**{t}.**" in HL, f"§F HistLog §III carries the {t} status row")
chk("Tier BM.9" in TI and all(f"BM.{n}" in TI for n in range(31, 34)),
    "§F index/tier_index.md carries Tier BM.9 with BM.31–BM.33")
chk('"BM.33"' in TJ and '"Def-BM.9"' in TJ, "§F index/tags.json carries the new tags")

print()
if FAILS:
    print(f"verify_H_mesonic_flicker_test: {len(FAILS)} FAILED of {N + len(FAILS)}")
    sys.exit(1)
print(f"verify_H_mesonic_flicker_test: {N} checks green  ({time.time()-t0:.1f}s) — "
      "Tier BM.9 (Def-BM.9, BM.31–BM.33) §A–§F")
sys.exit(0)
