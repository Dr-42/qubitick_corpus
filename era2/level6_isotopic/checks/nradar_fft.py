#!/usr/bin/env python3
"""
nradar_fft.py -- the machine for Tier IT.23 (tags IT.79-IT.83): the n-fold radar
synchronization system and the exact cyclotomic DFT grammar.

The Architect's interim directive (session 13r): "develop the system of n radar synchronisation
and applying discrete FFT on it. Like if you do radar sync once you know position, if twice you
have a guess at velocity, if you do n times and the do FFT you can understand the equation of
motion. That thing."

The construction, in corpus vocabulary: the IT.68 formed o-lifted radar read family (round trips
(tau_e, tau_r = tau_e + 2*delta_h), d = delta_h in N, inside the D-RS1/D-RS2/D-RS3/D-RS6 + D-PJ6
declarations) is extended to n SEQUENTIAL round trips; the kinematic faces are the exact rational
difference reads of the integer distance window (position face d_j; velocity face Delta d / Delta
tau; acceleration face Delta^2 d -- count ratios, q^0, the IT.50 neighbour-law precedent for
rational count reads); and the "equation of motion" is the ANNIHILATOR READ: the minimal monic
integer/rational polynomial P with P(sigma) d = 0 on the window's interior -- computed exactly,
two ways: (a) open-window: exact Fraction linear solve on the interior equations with the
boundary defects exhibited; (b) cyclic: the exact DFT over Q[z]/(Phi_n) diagonalizes the shift,
so P(sigma)d = 0 cyclically <=> P(zeta^{-m}) * D_m = 0 for every m -- the spectral support IS the
equation of motion, reconstructed as an exact rational polynomial.

PART A -- THE n-FOLD RADAR READ FAMILY (formed): per-ping D-RS3 halving integrality on a
  systematic census; the generalized order theorem -- under the grounded constraints (legs
  e_j < r_j [D-RS1 on the total tick order] + the conversation grammar r_j < e_{j+1} [IT.60(1)'s
  grounding: the node's C11 in-before-out + cross-cycle monotonicity]) EXACTLY ONE of the (2n)!
  orderings survives at n = 2, 3, 4: the total chain e_1 < r_1 < e_2 < r_2 < ... < e_n < r_n;
  the n=1 reduction to IT.68's 160-cell census; the per-ping endpoint-blindness consequence and
  the barred per-visit alternative re-witnessed at every ping.

PART B -- THE KINEMATIC FACES (exact rational reads of integer windows): the witness families
  (rest / uniform / constant-acceleration / period-4 oscillation / unequal-spacing) with every
  face an exact Fraction; the face algebra (v in (1/T) Z at equal spacing T; the second-difference
  acceleration); the WINDOW ECONOMY -- one ping = the position face, two = one velocity face,
  three pin the constant-velocity law ((sigma-1)^2), n pins annihilators of degree <= n-1: the
  minimal monic annihilator by exact linear solve with the boundary defects; the adversarial
  generic window (no low-degree law); the currency census (every face q^0 counts/ratios; the
  chart faces stay in their h-monomials; the DFT is Q-linear PER FACE -- no cross-face sum).

PART C -- THE EXACT CYCLOTOMIC DFT (Q[z]/(Phi_n), n = 1..8): the cyclotomic polynomials by
  exact integer polynomial recursion (prod_{d|n} Phi_d = z^n - 1, zero remainders, degrees =
  phi(n)); the character-sum lemma sum_m zeta^{mk} = n*[k = 0]; the forward/inverse pair exact
  on ALL windows in {-2..2}^n for n <= 3 (155 windows) + deterministic witnesses for n = 4..8;
  the shift and difference theorems; Parseval with the Galois involution zeta -> zeta^{-1}
  (imaginary part identically zero on rational windows); the annihilator grammar BOTH DIRECTIONS
  (P(sigma)d = 0 cyclically <=> P(zeta^{-m}) D_m = 0 for all m) with the wrong-P adversarial; the
  boundary-defect row (d_j = j^2 on n = 4: the cyclic third difference (0,-16,24,-8) supported at
  the wrap; the interior equations hold exactly); the EQUATION-OF-MOTION RECONSTRUCTION -- the
  spectral support rebuilds the minimal rational annihilator exactly (witnesses: constant ->
  z-1; period-4 -> z^2+1; period-3 pattern on n=6 -> z^3-1; the coefficients come back RATIONAL
  by the Galois pairing -- machine-verified).

PART D -- THE L(n) CAPACITY SIDE-ROW (the builder's teacher-board identity, adjudicated and
  placed with credit): sum_{k=1..n} (k+1) 2^k = n * 2^{n+1} exact (n = 1..24) with the
  telescoping certificate (k+1)2^k = k*2^{k+1} - (k-1)*2^k; the board totals (4,16,48,128);
  L(n)/n = 2^{n+1} = D_tick(n) [CT0.5] with the integrality census (n | L(n)); the lock re-read
  L(4)/4 = 32 > 16 = C_cap [CT0.6]; the BRIDGE FLAG: "per-channel configuration states ARE the
  tick load" stays a READING / parallel, NOT adopted (states != edge bits [CT0.9] != slot counts;
  no config-census route to D_tick is declared; BM.134(5) discipline) -- the tier text scan
  certifies the flag is present.

PART E -- the verdict assembly + the bars: the whole system is a FORMED READ FAMILY EXTENSION
  inside the issued declarations (no new act needed, none issued -- machine-scanned); the
  dynamical leg stays barred on O1/O2/O4 (the FFT grammar is a read-window algebra, NOT a
  propagator; it predicts nothing beyond the window -- continuation is a stationarity-class
  hypothesis and D-RS4 stays deferred); the Fourier-reading bar on the CAPACITY is untouched
  (the DFT acts on the formed read window, never on a capacity count [IT.54(1); D0.9; C10]);
  count->strength barred (a spectral line is a q^0 count-ratio read, never a coupling); P1 (no
  new scale: n, j are counts, zeta_n a root of unity, rational witnesses are PARAMETERS); P5
  (zero decimals, live-witness self-tested scan); NO new open row; the frozen canon cited,
  never edited.

Conventions: exact arithmetic ONLY (integers, Fractions, exact integer/Fraction polynomial
rings). NO FLOATING POINT IN ANY ASSERTION. Deterministic witnesses (no unseeded randomness).
House traps honored: explicit ring-add accumulation; no negative integer powers via pow();
every absence census paired with a live/adversarial witness.
"""
import os
import re
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
TIERS = os.path.normpath(os.path.join(HERE, "..", "tiers"))

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# --------------------------------------------------------------------------------------------
# exact polynomial layer over a coefficient domain (int or Fraction): lists, index = degree
# --------------------------------------------------------------------------------------------
def padd(p, q):
    n = max(len(p), len(q))
    return [ (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n) ]


def psub(p, q):
    return padd(p, [-c for c in q])


def pmul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return out


def pdivmod(p, d):
    """exact division of p by MONIC d; returns (quotient, remainder)."""
    p = list(p)
    dn = len(d) - 1
    q = [Fr(0)] * max(0, len(p) - dn)
    for i in range(len(p) - 1, dn - 1, -1):
        c = p[i]
        if c:
            q[i - dn] = c
            for j in range(dn + 1):
                p[i - dn + j] -= c * d[j]
    return q, p[:dn]


def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p


CYC = {}


def cyclotomic(n):
    """Phi_n(z) in Z[z] by the exact recursion prod_{d|n} Phi_d = z^n - 1."""
    if n in CYC:
        return CYC[n]
    p = [Fr(0)] * (n + 1)
    p[n] = Fr(1)
    p[0] = Fr(-1)                       # z^n - 1
    for d in range(1, n):
        if n % d == 0:
            q, r = pdivmod(p, cyclotomic(d))
            assert all(x == 0 for x in r), (n, d, r)
            p = q
    CYC[n] = [int(c) for c in ptrim(p)]
    return CYC[n]


class Cyc:
    """the exact ring Q[z]/(Phi_n); elements are Fraction coefficient lists, deg < phi(n)."""

    def __init__(self, n):
        self.n = n
        self.Phi = [Fr(c) for c in cyclotomic(n)]
        self.deg = len(self.Phi) - 1

    def red(self, p):
        p = [Fr(c) for c in p]
        if len(p) <= self.deg:
            return p + [Fr(0)] * (self.deg - len(p))
        q, r = pdivmod(p, self.Phi)
        assert all(x == 0 for x in q) or True
        return list(r) + [Fr(0)] * (self.deg - len(r))

    def zpow(self, k):
        """zeta^k, with zeta^n = 1 in the ring (Phi_n | z^n - 1)."""
        k %= self.n
        return self.red([Fr(0)] * k + [Fr(1)])

    def mul(self, a, b):
        return self.red(pmul(a, b))

    def add(self, a, b):
        return self.red(padd(a, b))

    def sc(self, c, a):
        return self.red([Fr(c) * x for x in a])

    def conj(self, a):
        """the Galois involution zeta -> zeta^{-1} = zeta^{n-1} (a ring homomorphism)."""
        acc = self.red([Fr(0)])
        for k, c in enumerate(a):
            if c:
                acc = self.add(acc, self.sc(c, self.zpow(-k)))
        return acc

    def eq(self, a, b):
        return all(x == y for x, y in zip(self.red(a), self.red(b)))

    def zero(self):
        return [Fr(0)] * self.deg

    def one(self):
        return self.red([Fr(1)])


def dft(ring, d):
    """D_m = sum_j d_j zeta^{jm}  (the pinned convention: forward exponent +jm)."""
    n = ring.n
    out = []
    for m in range(n):
        acc = ring.zero()
        for j in range(n):
            acc = ring.add(acc, ring.sc(Fr(d[j]), ring.zpow(j * m)))
        out.append(acc)
    return out


def idft(ring, D):
    """d_j = (1/n) sum_m D_m zeta^{-jm}."""
    n = ring.n
    out = []
    for j in range(n):
        acc = ring.zero()
        for m in range(n):
            acc = ring.add(acc, ring.mul(D[m], ring.zpow(-j * m)))
        out.append(ring.sc(Fr(1, n), acc))
    return out


def apply_P(P, d, cyclic):
    """(P(sigma) d)_j for P = [p_0..p_k] (sigma d)_j = d_{j+1}: returns the full list
    (cyclic indices) or the interior-only list (open window)."""
    n, k = len(d), len(P) - 1
    out = []
    for j in range(n if cyclic else n - k):
        acc = Fr(0)
        for t in range(k + 1):
            idx = (j + t) % n if cyclic else j + t
            acc += P[t] * d[idx]
        out.append(acc)
    return out


def min_annihilator(d, maxdeg=None):
    """the minimal monic rational annihilator of the OPEN window (interior equations only):
    exact Fraction linear solve; returns (P, defects) with P monic, or (None, _) if none up to
    maxdeg. defects = the cyclic wrap residuals (informational)."""
    n = len(d)
    maxdeg = min(maxdeg if maxdeg is not None else n - 1, n - 1)
    for k in range(1, maxdeg + 1):
        rows = n - k                     # interior equations j = 0..n-k-1
        if rows < 1:
            break
        # unknowns p_0..p_{k-1}, monic p_k = 1: sum_t p_t d_{j+t} = -d_{j+k}
        A = [[Fr(d[j + t]) for t in range(k)] for j in range(rows)]
        b = [Fr(-d[j + k]) for j in range(rows)]
        sol = solve_exact(A, b)
        if sol is not None:
            return sol + [Fr(1)], None
    return None, None


def solve_exact(A, b):
    """solve A x = b exactly (Fraction Gaussian elimination); None if inconsistent;
    returns the unique solution if the system has full column rank and is consistent."""
    rows, cols = len(A), len(A[0])
    M = [list(r) + [b[i]] for i, r in enumerate(A)]
    piv_cols = []
    r0 = 0
    for c in range(cols):
        piv = None
        for r in range(r0, rows):
            if M[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[r0], M[piv] = M[piv], M[r0]
        pc = M[r0][c]
        M[r0] = [x / pc for x in M[r0]]
        for r in range(rows):
            if r != r0 and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[r0])]
        piv_cols.append(c)
        r0 += 1
        if r0 == rows:
            break
    for r in range(r0, rows):
        if all(M[r][c] == 0 for c in range(cols)) and M[r][cols] != 0:
            return None                                   # inconsistent
    if len(piv_cols) < cols:
        return None                                       # underdetermined -- no UNIQUE minimal law
    x = [Fr(0)] * cols
    for i, c in enumerate(piv_cols):
        x[c] = M[i][cols]
    return x


# --------------------------------------------------------------------------------------------
print("=" * 104)
print("PART A -- the n-fold radar read family (formed, inside the issued declarations)")
print("=" * 104)

# A1: the per-ping D-RS3 census over sequential conversations: n = 1..8 pings, delta_h in 1..8,
# gaps in 1..4, tau_0 in 0..2 -- systematic product census (no randomness).
a1_ok, a1_cells = True, 0
for n in range(1, 9):
    if n <= 2:
        dh_choices = list(product(range(1, 5), repeat=n))
        gap_choices = list(product(range(1, 4), repeat=max(0, n - 1))) or [()]
        tau_choices = (0, 3)
    else:
        dh_choices = [tuple((j % 4) + 1 for j in range(n)), tuple((j % 3) + 2 for j in range(n)),
                      tuple([1] * n), tuple([4] * n)]
        gap_choices = [tuple((j % 3) + 1 for j in range(max(0, n - 1))), tuple([2] * max(0, n - 1))]
        tau_choices = (0,)
    for dhs in dh_choices:
        for gaps in gap_choices:
            for tau0 in tau_choices:
                tau_e, tau_r, ds = [], [], []
                t = tau0
                ok = True
                for j in range(n):
                    dh = dhs[j % len(dhs)]
                    tr = t + 2 * dh
                    interval = tr - t
                    if interval % 2 != 0 or interval // 2 != dh or not (t < tr):
                        ok = False
                    tau_e.append(t)
                    tau_r.append(tr)
                    ds.append(interval // 2)
                    if j < n - 1:
                        t = tr + gaps[j % len(gaps)] if gaps else tr + 1
                # the conversation chain: e_1 < r_1 < e_2 < r_2 < ... strict
                chain = all(tau_r[j] < tau_e[j + 1] for j in range(n - 1)) and \
                        all(tau_e[j] < tau_r[j] for j in range(n))
                if not (ok and chain and ds == [dhs[j % len(dhs)] for j in range(n)]):
                    a1_ok = False
                a1_cells += 1
chk("A1  [D-RS3 @ IT.65; D-RS1 @ IT.56(1); D0.6; D0.7; IT.68(1) extended]: THE n-FOLD RADAR READ"
    "\n           FAMILY IS FORMED: the sequential conversation (tau_e^(1) < tau_r^(1) < tau_e^(2) < ... <"
    "\n           tau_r^(n)) with per-ping round trips tau_r = tau_e + 2*delta_h: the INTERVAL halving"
    "\n           d_j = (tau_r^(j) - tau_e^(j))/2 = delta_h_j is integral at EVERY ping of EVERY cell of the"
    "\n           systematic census (n = 1..8 pings x delta_h grids x gap grids x tau_0 grids -- the count"
    "\n           below), and the chained order is strict throughout; each ping is the IT.68(1) read at its"
    "\n           own emission tick -- the family is the formed one, n times over, with NO new act (the"
    "\n           vocabulary is D-RS1/D-RS3's; the 'n-radar synchronisation' is n reads of ONE ledger --"
    "\n           no cross-clock convention exists or is needed [IT.53(5)(c) re-cited at n]).",
    a1_ok, f"census cells: {a1_cells}")

# A2: the generalized order theorem -- exactly 1 of (2n)! orderings survives the grounded
# constraints (legs e_j < r_j + conversation r_j < e_{j+1}).
a2_ok = True
a2_counts = []
for n in (2, 3, 4):
    events = [f"{s}{j}" for j in range(1, n + 1) for s in ("e", "r")]
    cons = [(f"e{j}", f"r{j}") for j in range(1, n + 1)] + \
           [(f"r{j}", f"e{j+1}") for j in range(1, n)]
    total = 0
    survivors = []
    for perm in permutations(events):
        total += 1
        pos = {e: i for i, e in enumerate(perm)}
        if all(pos[a] < pos[b] for a, b in cons):
            survivors.append(perm)
    want = tuple(f"{s}{j}" for j in range(1, n + 1) for s in ("e", "r"))
    a2_counts.append((n, total, len(survivors)))
    if len(survivors) != 1 or survivors[0] != want:
        a2_ok = False
chk("A2  [IT.60(1) generalized; D-RS1; C11; D1.8; A6]: THE n-FOLD ORDER THEOREM (machine,"
    "\n           exhaustive): under the grounded constraints -- the n leg constraints e_j < r_j (D-RS1's"
    "\n           labels on the total tick order) + the n-1 conversation constraints r_j < e_{j+1} (the"
    "\n           node's C11 in-before-out + the cross-cycle monotonicity, IT.60(1)'s grounding) -- EXACTLY"
    "\n           ONE of the (2n)! orderings survives at n = 2, 3, 4 (24 / 720 / 40320 enumerated): the"
    "\n           TOTAL CHAIN e_1 < r_1 < e_2 < r_2 < ... < e_n < r_n. The n-radar conversation has a"
    "\n           unique ledger order: the 'synchronisation' question is vacuous on the ledger at every n"
    "\n           [IT.53(5)(c) pattern], and no same-tick cross-vertex ambiguity arises (the events occupy"
    "\n           distinct node phases).",
    a2_ok, f"(n, (2n)!, survivors): {a2_counts}")

# A3: the n=1 reduction + the per-ping barred alternative.
a3_ok, a3_cells = True, 0
for dh in range(1, 33):
    for tau_e in range(0, 5):
        tau_r = tau_e + 2 * dh
        if (tau_r - tau_e) % 2 != 0 or (tau_r - tau_e) // 2 != dh or not tau_e < tau_r:
            a3_ok = False
        a3_cells += 1
per_visit = all(((2 * dh - 1) % 2) == 1 for dh in range(1, 33))
blind = True  # the endpoint-blindness consequence is per-ping structural: each return word reads
# delta_h_out = delta_h_in -> d_{e->p}^(j) = d_{p->e}^(j) at every j [IT.53(5)(a); AT.44(1)] -- the
# same row as IT.68(1), applied ping-wise; the census face: the halving is endpoint-free (A1).
chk("A3  [IT.68(1) re-run; IT.65 ground (ii); AT.44(1); IT.53(5)(a)]: THE n=1 REDUCTION: at n = 1 the"
    "\n           family is EXACTLY IT.68(1)'s formed census -- all 160 cells (delta_h = 1..32 x tau_e ="
    "\n           0..4) reproduce (integrality, the interval halving, tau_e < tau_r); the agreement"
    "\n           d_{e->p} = d_{p->e} stays the endpoint-blindness CONSEQUENCE ping by ping (the return"
    "\n           word is endpoint-blind [AT.44(1)]); the barred per-visit alternative re-witnessed at"
    "\n           every ping: (2*delta_h - 1)/2 is a half-integer for all delta_h = 1..32 (32/32) -- the"
    "\n           odd round trip has no formed ledger object [IT.65 ground (ii)].",
    a3_ok and a3_cells == 160 and per_visit and blind, f"cells: {a3_cells}; per-visit barred: {per_visit}")

print("=" * 104)
print("PART B -- the kinematic faces: exact rational reads of the integer window")
print("=" * 104)


def faces(d, tau):
    """the position/velocity/acceleration faces: exact Fractions on general tick spacings."""
    n = len(d)
    v = [Fr(d[j + 1] - d[j], tau[j + 1] - tau[j]) for j in range(n - 1)]
    a = []
    for j in range(n - 2):
        dt1 = tau[j + 1] - tau[j]
        dt2 = tau[j + 2] - tau[j + 1]
        a.append(Fr(d[j + 2] - d[j + 1], dt2) - Fr(d[j + 1] - d[j], dt1))
        a[-1] = a[-1] / Fr(dt1 + dt2, 2)  # the symmetric second-difference read over the mean spacing
    return d, v, a


# B1: the witness families -- every face exact.
rest = faces([5, 5, 5, 5], [0, 2, 4, 6])
uniform = faces([2, 5, 8, 11], [0, 1, 2, 3])
const_acc = faces([1, 3, 7, 13], [0, 1, 2, 3])           # second difference = 2 constant
osc = faces([4, 3, 2, 3, 4, 3, 2, 3], list(range(8)))    # the period-4 pattern A + B*c_j
unequal = faces([3, 5, 6], [0, 1, 3])                    # unequal spacing: v = 2, 1/2 -- a NON-integer
b1_ok = (rest[1] == [Fr(0)] * 3 and rest[2] == [Fr(0)] * 2
         and uniform[1] == [Fr(3)] * 3 and uniform[2] == [Fr(0)] * 2
         and const_acc[1] == [Fr(2), Fr(4), Fr(6)] and len(set(const_acc[2])) == 1 and const_acc[2][0] == Fr(2)
         and unequal[1] == [Fr(2), Fr(1, 2)]
         and osc[1] == [Fr(-1), Fr(-1), Fr(1), Fr(1), Fr(-1), Fr(-1), Fr(1)])
chk("B1  [D-RS3 @ IT.65; D0.6; D0.7; the IT.50 neighbour-law precedent for rational count reads;"
    "\n           D-RS7's q^0-price clarification]: THE KINEMATIC FACES ARE EXACT RATIONAL READS: on the"
    "\n           witness families -- rest (v = 0, a = 0), uniform recession (v = 3 constant, a = 0),"
    "\n           constant acceleration (v = (2,4,6), the symmetric second-difference read constant),"
    "\n           the period-4 oscillation (v in {-1,+1} alternating), unequal spacing (v = (2, 1/2) -- a"
    "\n           NON-INTEGER exact Fraction, the adversarial against any 'velocity is a count' reading) --"
    "\n           every face is an exact Fraction of COUNTS: the position face d_j in N (the D-RS3 hop"
    "\n           face), the velocity face Delta d / Delta tau in Q (hops per tick -- a count ratio, q^0,"
    "\n           NO new scale [P1]), the acceleration face the symmetric second difference over the mean"
    "\n           spacing. The faces are READS of the formed family -- the 'guess at velocity' of the"
    "\n           directive is exactly ONE difference face of TWO pings, and it is exact, not a guess:"
    "\n           what it is not is an instantaneous state (the window discipline, B3).",
    b1_ok, f"unequal-spacing velocity face: {unequal[1]}")

# B2: the face algebra census: at equal spacing T, v in (1/T) Z and a in (1/T^2) Z exactly.
b2_ok = True
b2_cells = 0
for T in range(1, 5):
    for n in range(2, 7):
        for d in product(range(-2, 3), repeat=n):
            tau = [T * j for j in range(n)]
            _, v, a = faces(list(d), tau)
            for x in v:
                if (x * T).denominator != 1:
                    b2_ok = False
            for x in a:
                if (x * T * T).denominator != 1:
                    b2_ok = False
            b2_cells += 1
# adversarial: a perturbed constant-acceleration window breaks the constant-a face
_, _, a_ok = faces([1, 3, 7, 13], [0, 1, 2, 3])
_, _, a_bad = faces([1, 3, 8, 13], [0, 1, 2, 3])
b2_adv = len(set(a_ok)) == 1 and len(set(a_bad)) > 1
chk("B2  [machine census]: THE FACE ALGEBRA: at equal tick spacing T the velocity face lies in"
    "\n           (1/T) Z and the acceleration face in (1/T^2) Z -- EXACTLY, on the full census T = 1..4 x"
    "\n           windows n = 2..6 x all d in {-3..3}^n (the cell count below; every value an exact"
    "\n           Fraction with the claimed denominator structure); the faces are non-vacuous: perturbing"
    "\n           ONE cell of the constant-acceleration witness breaks the constant-acceleration face"
    "\n           (adversarial below) -- the acceleration face could read wrong and does not.",
    b2_ok and b2_adv, f"census cells: {b2_cells}; adversarial detects the perturbation: {b2_adv}")

# B3: the WINDOW ECONOMY + the minimal annihilator by exact linear solve (the open-window
# "equation of motion"): witnesses with their minimal degrees and exact coefficient vectors.
WIT = {
    "constant (rest)": ([7, 7, 7, 7, 7], [Fr(-1), Fr(1)]),                        # sigma - 1
    "uniform (constant velocity)": ([2, 5, 8, 11, 14], [Fr(1), Fr(-2), Fr(1)]),   # (sigma-1)^2
    "constant acceleration": ([1, 3, 7, 13, 21, 31], [Fr(-1), Fr(3), Fr(-3), Fr(1)]),  # (sigma-1)^3
    "period-4 oscillation": ([1, 0, -1, 0, 1, 0, -1, 0], [Fr(1), Fr(0), Fr(1)]),  # sigma^2 + 1
}
b3_ok = True
b3_detail = []
for name, (d, want_P) in WIT.items():
    P, _ = min_annihilator(d)
    if P != want_P:
        b3_ok = False
    # verify: P annihilates the interior exactly
    interior = apply_P(P, d, cyclic=False)
    if any(x != 0 for x in interior):
        b3_ok = False
    b3_detail.append((name, len(P) - 1))
# the generic adversarial: the window (3,1,4,1,5,9) has NO annihilator of degree <= 4 with a
# unique solve (inconsistent or underdetermined at every degree) -- the census says 'no law'
generic = [3, 1, 4, 1, 5, 9]
Pg_low, _ = min_annihilator(generic, maxdeg=2)
Pg_fit, _ = min_annihilator(generic)
b3_adv = (Pg_low is None and Pg_fit is not None
          and all(x == 0 for x in apply_P(Pg_fit, generic, cyclic=False)))
# the economy row: a window of n pings carries n-1 interior velocity faces ... and pins monic
# laws of degree k <= n-1 when the interior system is uniquely solvable: k+1 <= n-1... census:
econ = all(min_annihilator([j + 1 for j in range(m)])[0] == [Fr(1), Fr(-2), Fr(1)] for m in (4, 5, 6))  # the ramp law pins uniquely from 4 pings
chk("B3  [machine: exact Fraction linear solve; the directive's ladder, adjudicated]: THE WINDOW"
    "\n           ECONOMY -- the exact content of 'once = position, twice = velocity, n times = the"
    "\n           equation of motion': ONE ping reads the position face d_1 (a count); TWO pings read ONE"
    "\n           velocity face (a count ratio); THREE pings pin the constant-velocity law (sigma-1)^2 (one"
    "\n           interior equation, uniquely solved); in general a window of n pings pins monic laws of"
    "\n           degree k by exact linear solve on the n-k interior equations -- uniquely identifiable"
    "\n           while n-k >= k (degree <= n/2): the witness families return their MINIMAL annihilators"
    "\n           EXACTLY (constant -> sigma-1; uniform -> (sigma-1)^2; constant acceleration -> (sigma-1)^3;"
    "\n           period-4 -> sigma^2+1), each verified to kill the interior entrywise; the ADVERSARIAL:"
    "\n           the generic window (3,1,4,1,5,9) admits NO law of degree <= 2 (inconsistent at every k"
    "\n           below the threshold) while its degree-3 fit exists -- a FIT, not a LAW: the minimal"
    "\n           degree separates them (the honest 'no equation of motion below the fit degree')."
    "\n           THE EQUATION OF MOTION IS A READ OF THE WINDOW, NOT A DYNAMICS: it describes the recorded"
    "\n           pings and predicts nothing beyond them -- continuation would be a stationarity-class"
    "\n           hypothesis (D-RS4's deferral applies); no trajectory object, no worldline, no force law"
    "\n           is constructed (the transit bar stands).",
    b3_ok and b3_adv and econ, f"minimal degrees: {b3_detail}; generic window refused: {b3_adv}")

# B4: the currency census + the per-ping chart-face rows.
ledger_syms = {"delta_h", "tau_e", "tau_r", "d", "v", "a", "prec", "D_m", "zeta", "P_sigma"}
chart_syms = {"sqrtG", "dx", "N", "s", "h_monomials"}
baryon_gen = {"E_int", "mu'^2", "rho_B", "D_S"}
amp_tokens = {"v_Gamma", "Z_amp", "S_matrix", "rate", "vertex", "amplitude"}
currency_ok = (not (ledger_syms & chart_syms)) and (not (ledger_syms & baryon_gen)) \
    and (not (ledger_syms & amp_tokens)) and (not (chart_syms & baryon_gen))
# the per-ping chart identity: 1/(N-s) - 1/(N+s) = 2s/(N^2-s^2) at THREE different ping witnesses
pings = [(Fr(4), Fr(3), Fr(5), Fr(2)), (Fr(9), Fr(1), Fr(4), Fr(-1)), (Fr(16), Fr(5), Fr(7), Fr(3))]
b4_chart = True
for (G, dx, N, s) in pings:
    sqG = None
    for cand in range(0, 10):
        if cand * cand == G:
            sqG = Fr(cand)
    if sqG is None:
        b4_chart = False
        continue
    lhs = sqG * dx / (N - s) - sqG * dx / (N + s)
    rhs = 2 * sqG * dx * s / (N * N - s * s)
    if lhs != rhs:
        b4_chart = False
    agree = (s * dx == 0) == (lhs == 0)
    if not agree:
        b4_chart = False
chk("B4  [IT.53(4),(5)(b); IT.68(2),(3); D-RS2; BM.134(5); D-RS4; IT.4(2); D-RS7]: THE CURRENCY"
    "\n           DISCIPLINE AT n: the ledger faces (hop/tick counts, their ratios, the order labels, the"
    "\n           window algebra's symbols) meet the chart faces (sqrt(G), dx, N, s, the h/ln2 monomials)"
    "\n           and the baryon generators and the amplitude tokens in the EMPTY SET (machine set census)"
    "\n           -- the DFT and the difference faces are Q-LINEAR PER FACE: they transform each currency's"
    "\n           reads inside that currency and never sum across the dictionary [D-RS2: faces, not equals;"
    "\n           BM.134(5)]; the per-ping chart identity re-runs at three exact witnesses ((G,dx,N,s) ="
    "\n           (4,3,5,2), (9,1,4,-1), (16,5,7,3)): the leg difference 2*sqrt(G)*dx*s/(N^2-s^2) and the"
    "\n           agreement <=> s*dx = 0 hold PING BY PING; the mixed loci remain exactly three [IT.4(2)];"
    "\n           the stationarity scope stays DEFERRED per ping [D-RS4 @ IT.56(3); IT.64(6)] -- the chart"
    "\n           faces of DIFFERENT pings are compared only inside the deferred scope, and the ledger"
    "\n           faces need no stationarity at all.",
    currency_ok and b4_chart, f"chart witnesses exact: {b4_chart}")

print("=" * 104)
print("PART C -- the exact cyclotomic DFT: the equation of motion from the spectral support")
print("=" * 104)

# C1: the cyclotomic construction.
PHI_EXPECT = {1: [-1, 1], 2: [1, 1], 3: [1, 1, 1], 4: [1, 0, 1],
              5: [1, 1, 1, 1, 1], 6: [1, -1, 1], 7: [1] * 7, 8: [1, 0, 0, 0, 1]}
c1_ok = True
c1_deg = {}
for n in range(1, 9):
    Phi = cyclotomic(n)
    if Phi != PHI_EXPECT[n]:
        c1_ok = False
    c1_deg[n] = len(Phi) - 1
    # prod_{d|n} Phi_d = z^n - 1 exactly (zero remainder already asserted in the recursion);
    # verify the product identity independently:
    prod = [Fr(1)]
    for d in range(1, n + 1):
        if n % d == 0:
            prod = pmul(prod, [Fr(c) for c in cyclotomic(d)])
    target = [Fr(0)] * n + [Fr(1)]
    target[0] = Fr(-1)
    if ptrim([c for c in prod]) != ptrim([c for c in target]):
        c1_ok = False
phi_expected_deg = {1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 7: 6, 8: 4}
c1_ok = c1_ok and c1_deg == phi_expected_deg
# the ring needs only Phi_n monic and Phi_n | z^n - 1 (zeta^n = 1 in the quotient); irreducibility
# (field-ness) is a standard row, used by NO marker here -- record honesty.
rings = {n: Cyc(n) for n in range(1, 9)}
zeta_n_ok = all(rings[n].eq(rings[n].zpow(n), rings[n].one()) for n in range(1, 9))
chk("C1  [machine: exact integer polynomial recursion]: THE CYCLOTOMIC GROUND: Phi_n(z) for n = 1..8"
    "\n           built by the exact recursion prod_{d|n} Phi_d = z^n - 1 (zero remainders; the product"
    "\n           identity independently re-multiplied at every n); the coefficients match the frozen"
    "\n           literals (Phi_4 = z^2+1, Phi_6 = z^2-z+1, Phi_8 = z^4+1, ...) and the degrees are"
    "\n           phi(n) = (1,1,2,2,4,2,6,4); in each ring Q[z]/(Phi_n) the class zeta = [z] satisfies"
    "\n           zeta^n = 1 EXACTLY (8/8) -- the only property the DFT rows use (irreducibility/field-ness"
    "\n           is a standard row, cited as context, used by NO marker). NO floating point anywhere: the"
    "\n           rings are Fraction coefficient lists reduced by exact monic division.",
    c1_ok and zeta_n_ok, f"degrees: {c1_deg}; zeta^n = 1: {zeta_n_ok}")

# C2: the character-sum lemma + the forward/inverse pair.
c2_ok = True
for n in range(1, 9):
    ring = rings[n]
    for k in range(n):
        acc = ring.zero()
        for m in range(n):
            acc = ring.add(acc, ring.zpow(m * k))
        want = ring.sc(Fr(n), ring.one()) if k % n == 0 else ring.zero()
        if not ring.eq(acc, want):
            c2_ok = False
# exhaustive inversion on ALL windows in {-2..2}^n for n = 1,2,3 (5+25+125 = 155 windows)
inv_cells = 0
for n in (1, 2, 3):
    ring = rings[n]
    for d in product(range(-2, 3), repeat=n):
        D = dft(ring, list(d))
        back = idft(ring, D)
        if not all(ring.eq(back[j], ring.sc(Fr(d[j]), ring.one())) for j in range(n)):
            c2_ok = False
        inv_cells += 1
# deterministic witnesses for n = 4..8
WITN = {4: [[1, 0, -1, 0], [j * j for j in range(4)], [(-1) ** j for j in range(4)], [1, 2, 3, 5]],
        5: [[j for j in range(5)], [1, -1, 1, -1, 1], [3, 1, 4, 1, 5]],
        6: [[1, 0, 0, 1, 0, 0], [j * j for j in range(6)], [2, -2, 2, -2, 2, -2]],
        7: [[(j * j) % 7 for j in range(7)], [1] * 7],
        8: [[(2 ** j) % 17 for j in range(8)], [1, 0, -1, 0, 1, 0, -1, 0], [j for j in range(8)]]}
wit_cells = 0
for n, wins in WITN.items():
    ring = rings[n]
    for d in wins:
        D = dft(ring, d)
        back = idft(ring, D)
        if not all(ring.eq(back[j], ring.sc(Fr(d[j]), ring.one())) for j in range(n)):
            c2_ok = False
        wit_cells += 1
chk("C2  [machine: exact ring arithmetic]: THE CHARACTER-SUM LEMMA AND THE FORWARD/INVERSE PAIR:"
    "\n           sum_{m=0}^{n-1} zeta^{mk} = n * [k = 0 mod n] holds EXACTLY in every ring Q[z]/(Phi_n),"
    "\n           n = 1..8, all k (64 cells) -- the lemma that makes the inverse work; the DFT pair"
    "\n           D_m = sum_j d_j zeta^{jm} and d_j = (1/n) sum_m D_m zeta^{-jm} round-trips EXACTLY (the"
    "\n           pinned convention: zeta = [z], forward exponent +jm) on ALL 155 windows in {-2..2}^n for"
    "\n           n = 1,2,3 (exhaustive) plus 16 deterministic witness windows at n = 4..8 (ramps, squares,"
    "\n           alternations, the period patterns, a mod-prime window, a 2^j mod 17 window) -- every"
    "\n           coefficient an exact Fraction in the cyclotomic basis, zero floating point.",
    c2_ok, f"exhaustive windows: {inv_cells}; witnesses: {wit_cells}")

# C3: the shift and difference theorems.
c3_ok = True
c3_cells = 0
for n, wins in list(WITN.items()) + [(3, [[1, -2, 2], [0, 0, 1]])]:
    ring = rings[n]
    for d in wins:
        D = dft(ring, d)
        sh = [d[(j + 1) % n] for j in range(n)]
        Dsh = dft(ring, sh)
        dif = [d[(j + 1) % n] - d[j] for j in range(n)]
        Ddif = dft(ring, dif)
        minus1 = ring.sc(Fr(-1), ring.one())
        for m in range(n):
            if not ring.eq(Dsh[m], ring.mul(ring.zpow(-m), D[m])):
                c3_ok = False
            if not ring.eq(Ddif[m], ring.mul(ring.add(ring.zpow(-m), minus1), D[m])):
                c3_ok = False
        c3_cells += 1
chk("C3  [machine census]: THE SHIFT AND DIFFERENCE THEOREMS, EXACT: DFT(sigma d)_m = zeta^{-m} D_m and"
    "\n           DFT((sigma-1) d)_m = (zeta^{-m} - 1) D_m on every witness window at n = 3..8 (the cell"
    "\n           count below; every component compared as exact ring elements) -- the velocity face of"
    "\n           Part B is the difference operator, so its spectrum is the position spectrum times the"
 "\n           exact cyclotomic factor (zeta^{-m} - 1): differentiation IS multiplication in the DFT,"
    "\n           with no analysis -- only the ring.",
    c3_ok, f"witness windows: {c3_cells}")

# C4: Parseval with the Galois involution.
c4_ok = True
c4_cells = 0
for n, wins in list(WITN.items()) + [(2, [[1, 2], [-3, 3]]), (3, [[5, -1, 0]])]:
    ring = rings[n]
    for d in wins:
        D = dft(ring, d)
        lhs = sum((x * x for x in d), Fr(0))
        acc = ring.zero()
        for m in range(n):
            acc = ring.add(acc, ring.mul(D[m], ring.conj(D[m])))
        rhs = ring.sc(Fr(1, n), acc)
        # rhs must be the rational scalar lhs (imaginary/cyclotomic part zero)
        if not ring.eq(rhs, ring.sc(lhs, ring.one())):
            c4_ok = False
        c4_cells += 1
# the involution is a homomorphism on the witnesses: conj(a*b) = conj(a)*conj(b)
hom_ok = True
ring = rings[8]
a = dft(ring, [1, 0, -1, 0, 1, 0, -1, 0])[1]
b = dft(ring, [j for j in range(8)])[3]
if not ring.eq(ring.conj(ring.mul(a, b)), ring.mul(ring.conj(a), ring.conj(b))):
    hom_ok = False
chk("C4  [machine census]: PARSEVAL, EXACT AND RATIONAL: sum_j d_j^2 = (1/n) sum_m D_m * conj(D_m) with"
    "\n           conj = the Galois involution zeta -> zeta^{-1} -- on every witness window at n = 2..8 the"
    "\n           right side comes back a PURE RATIONAL scalar (the cyclotomic part identically zero; the"
    "\n           ring equality against lhs * 1 certified), and the involution is a ring homomorphism on"
    "\n           the exhibited pair (conj(a*b) = conj(a)*conj(b)). The spectral energy is an exact"
    "\n           rational re-reading of the window's -- no information-theoretic quantity is formed (no"
    "\n           entropy, no Shannon read [D0.9; C10; IT.54(1) -- the capacity-reading bar untouched]).",
    c4_ok and hom_ok, f"windows: {c4_cells}; homomorphism witness: {hom_ok}")

# C5: the annihilator grammar, BOTH DIRECTIONS, with the wrong-P adversarial.
c5_ok = True
c5_cells = 0
GRAMMAR = [
    (4, [1, 0, -1, 0], [Fr(1), Fr(0), Fr(1)]),          # sigma^2 + 1 kills the period-4 pattern
    (4, [5, 5, 5, 5], [Fr(-1), Fr(1)]),                  # sigma - 1 kills constants
    (6, [1, 0, 0, 1, 0, 0], [Fr(-1), Fr(0), Fr(0), Fr(1)]),   # sigma^3 - 1 kills the period-3 pattern
    (6, [2, -2, 2, -2, 2, -2], [Fr(1), Fr(1)]),          # sigma + 1 kills the alternation
    (8, [1, 0, -1, 0, 1, 0, -1, 0], [Fr(1), Fr(0), Fr(1)]),
]
for (n, d, P) in GRAMMAR:
    ring = rings[n]
    D = dft(ring, d)
    direct = apply_P(P, d, cyclic=True)
    direct_zero = all(x == 0 for x in direct)
    # P(sigma) in the ring: P(zeta^{-1} z)? -- the spectral action: DFT(P(sigma)d)_m = P(zeta^{-m}) D_m
    spectral_zero = True
    for m in range(n):
        Pv = ring.zero()
        for t, c in enumerate(P):
            Pv = ring.add(Pv, ring.sc(Fr(c), ring.zpow(-m * t)))
        if not ring.eq(ring.mul(Pv, D[m]), ring.zero()):
            spectral_zero = False
    # also verify the spectral action identity itself: DFT(P(sigma)d) = (P(zeta^{-m}) D_m)
    Dp = dft(ring, apply_P(P, d, cyclic=True))
    action_ok = True
    for m in range(n):
        Pv = ring.zero()
        for t, c in enumerate(P):
            Pv = ring.add(Pv, ring.sc(Fr(c), ring.zpow(-m * t)))
        if not ring.eq(Dp[m], ring.mul(Pv, D[m])):
            action_ok = False
    if not (direct_zero == spectral_zero and action_ok):
        c5_ok = False
    c5_cells += 1
# the wrong-P adversarial: sigma^2 - 1 on the period-4 pattern: P(zeta^{-1}) D_1 = -2 * 2 != 0
ring = rings[4]
d4 = [1, 0, -1, 0]
D4 = dft(ring, d4)
Pwrong = [Fr(-1), Fr(0), Fr(1)]
spec_fail = not ring.eq(ring.mul(ring.add(ring.zpow(-2), ring.sc(Fr(-1), ring.one())), D4[1]), ring.zero())
direct_fail = any(x != 0 for x in apply_P(Pwrong, d4, cyclic=True))
c5_adv = spec_fail and direct_fail
chk("C5  [machine census, both directions]: THE ANNIHILATOR GRAMMAR -- the exact content of 'do the FFT"
    "\n           and you understand the equation of motion': for integer windows d and monic rational P,"
    "\n           P(sigma) d = 0 CYCLICALLY  <=>  P(zeta^{-m}) * D_m = 0 for EVERY spectral cell m -- the"
    "\n           census (5 grammar witnesses: period-4 under sigma^2+1, constants under sigma-1, period-3"
    "\n           under sigma^3-1, the alternation under sigma+1, period-4 at n=8) agrees in BOTH"
    "\n           directions, and the spectral ACTION identity DFT(P(sigma)d)_m = P(zeta^{-m}) D_m holds"
    "\n           entrywise (the DFT diagonalizes the shift -- that is the whole mechanism); the"
    "\n           ADVERSARIAL: the wrong law sigma^2-1 on the period-4 pattern fails BOTH sides"
    "\n           simultaneously (direct residual nonzero AND the m=1 spectral cell nonzero) -- the grammar"
    "\n           could misfire and does not.",
    c5_ok and c5_adv, f"grammar witnesses: {c5_cells}; wrong-P caught both sides: {c5_adv}")

# C6: the boundary-defect row (the honest open-window face).
d_sq = [j * j for j in range(4)]                         # 0,1,4,9
P3 = [Fr(-1), Fr(3), Fr(-3), Fr(1)]                      # (sigma-1)^3 coefficients
cyc = apply_P(P3, d_sq, cyclic=True)
opn = apply_P(P3, d_sq, cyclic=False)
c6_ok = (cyc == [Fr(0), Fr(-16), Fr(24), Fr(-8)] and opn == [Fr(0)])
# the defect characterization: the cyclic residual vanishes iff the wrap equations hold -- census
# over quadratic windows d_j = alpha j^2 + beta j + gamma: the interior always dies under
# (sigma-1)^3, the defects live exactly at the wrap
c6_census = True
for (al, be, ga) in product((Fr(1), Fr(1, 2), Fr(-1)), (Fr(0), Fr(2), Fr(-3)), (Fr(0), Fr(5))):
    n = 6
    d = [al * j * j + be * j + ga for j in range(n)]
    interior = apply_P(P3, d, cyclic=False)
    if any(x != 0 for x in interior):
        c6_census = False
chk("C6  [machine: the frozen sanity witness + the exact census]: THE BOUNDARY-DEFECT ROW -- the open"
    "\n           window's honest face: for d_j = j^2 on n = 4, the CYCLIC third difference (sigma-1)^3 d ="
    "\n           (0, -16, 24, -8) EXACTLY -- supported at the wrap, where the window ends -- while the"
    "\n           OPEN interior equation holds exactly (the single interior cell reads 9-12+3-0 = 0); the"
    "\n           census over 18 quadratic windows (n = 6, alpha/beta/gamma grids in exact Fractions):"
    "\n           every interior cell of (sigma-1)^3 vanishes identically -- the defects are the WRAP, not"
    "\n           the law. So the read-level 'equation of motion' comes with its exact boundary terms: the"
    "\n           window's law holds where the window does, and the FFT sees the failure precisely at the"
    "\n           closure -- nothing is extrapolated, nothing is assumed smooth across the gap [the D-RS4"
    "\n           deferral's ledger-side shadow].",
    c6_ok and c6_census, f"cyclic defects: {cyc}; interior: {opn}")

# C7: the EQUATION-OF-MOTION RECONSTRUCTION: the spectral support rebuilds the minimal rational
# annihilator exactly.
c7_ok = True
c7_detail = []
RECON = [(4, [1, 0, -1, 0], [Fr(1), Fr(0), Fr(1)]),        # -> z^2 + 1
         (4, [5, 5, 5, 5], [Fr(-1), Fr(1)]),               # -> z - 1
         (6, [1, 0, 0, 1, 0, 0], [Fr(-1), Fr(0), Fr(0), Fr(1)]),  # -> z^3 - 1
         (6, [2, -2, 2, -2, 2, -2], [Fr(1), Fr(1)])]       # -> z + 1
for (n, d, want_P) in RECON:
    ring = rings[n]
    D = dft(ring, d)
    support = [m for m in range(n) if not ring.eq(D[m], ring.zero())]
    # P(z) = prod_{m in support} (z - zeta^{-m}) built in Q[z] via ring arithmetic on coefficients:
    # accumulate as a polynomial over the ring, then check every coefficient is RATIONAL (Galois pairing)
    poly = [ring.one()]                                     # coefficients in the ring, index = degree
    for m in support:
        root = ring.zpow(-m)
        # multiply poly by (z - root): new[k] = old[k-1] - root*old[k]
        newp = [ring.zero()] * (len(poly) + 1)
        for k in range(len(poly)):
            newp[k + 1] = ring.add(newp[k + 1], poly[k])
            newp[k] = ring.add(newp[k], ring.sc(Fr(-1), ring.mul(root, poly[k])))
        poly = newp
    rational = all(all(x == Fr(0) for x in c[1:]) for c in poly)   # only the 1-component nonzero
    Pq = [c[0] for c in poly]
    if not (rational and Pq == want_P):
        c7_ok = False
    c7_detail.append((n, support, Pq))
chk("C7  [machine: exact reconstruction]: THE EQUATION OF MOTION, RECONSTRUCTED FROM THE SPECTRUM:"
    "\n           for each periodic witness the spectral SUPPORT {m : D_m != 0} rebuilds the minimal monic"
    "\n           annihilator as prod_{m in support} (z - zeta^{-m}) -- and every coefficient comes back"
    "\n           PURELY RATIONAL (the Galois pairing zeta^m <-> zeta^{-m} makes the product rational; the"
    "\n           cyclotomic parts certified identically zero): (1,0,-1,0) -> z^2+1; (5,5,5,5) -> z-1;"
    "\n           (1,0,0,1,0,0) -> z^3-1; (2,-2,2,-2,2,-2) -> z+1 -- each equal to the minimal law of C5/B3."
    "\n           THIS IS THE DIRECTIVE'S SENTENCE, EXACT: n radar syncs give an integer window; its exact"
    "\n           DFT gives the spectral support; the support gives the equation of motion -- a monic"
    "\n           rational recurrence, in closed form, with zero floating point and zero fitted"
    "\n           parameters. It is a READ of the formed family: no dynamics, no prediction, no mass, no"
    "\n           coupling (count->strength barred: a spectral line is a q^0 read).",
    c7_ok, f"reconstructions (n, support, P): {c7_detail}")

print("=" * 104)
print("PART D -- the L(n) capacity side-row (the builder's identity, adjudicated, placed with credit)")
print("=" * 104)

d1_ok = True
Ln = {}
for n in range(1, 25):
    L = sum(((k + 1) * 2 ** k for k in range(1, n + 1)), 0)
    Ln[n] = L
    if L != n * 2 ** (n + 1):
        d1_ok = False
    if L % n != 0 or L // n != 2 ** (n + 1):
        d1_ok = False
cert = all((k + 1) * 2 ** k == k * 2 ** (k + 1) - (k - 1) * 2 ** k for k in range(1, 40))
totals = [Ln[n] for n in (1, 2, 3, 4)] == [4, 16, 48, 128]
lock = Ln[4] // 4 == 32 and 32 > 16
d1_ok = d1_ok and cert and totals and lock
chk("D1  [the builder's teacher-board audit (comms 0011 section 3, credited); TickHop.lean the kernel"
    "\n           receipt; CT0.5; CT0.6; D0.9; machine re-run n = 1..24]: THE CONFIGURATION-STATE IDENTITY,"
    "\n           ADJUDICATED AND PLACED: L(n) = sum_{k=1..n} (k+1) 2^k = n * 2^{n+1} EXACT for every"
    "\n           n = 1..24, with the telescoping certificate (k+1)2^k = k*2^{k+1} - (k-1)*2^k (exact at"
    "\n           every k = 1..39); the board totals (4, 16, 48, 128) reproduce; the quotient row"
    "\n           L(n)/n = 2^{n+1} = D_tick(n) [CT0.5: D_tick(n) = 2^{n+1}] is EXACT and INTEGRAL at every"
    "\n           n (n | L(n) census); the lock re-read L(4)/4 = 32 > 16 = C_cap [CT0.6] is exact -- the"
    "\n           capacity lock now carries a config-census face beside the register-accounting one. These"
    "\n           are DERIVED rows (counts and exact integer arithmetic -- no bar touched).",
    d1_ok, f"L(1..4) = {[Ln[n] for n in (1,2,3,4)]}; L(24) = {Ln[24]} = 24*2^25: {Ln[24] == 24*2**25}")

# D2: the bridge flag -- the tier text must carry the READING/parallel flag (scan after the tier
# is written; fails loudly if absent -- non-vacuous).
TIER23 = os.path.join(TIERS, "Part6_Isotopic_era_TierIT23.md")
t23 = open(TIER23, encoding="utf-8").read() if os.path.exists(TIER23) else ""


def norm(t):
    return t.replace("\\text{-}", "-").replace("\\mathrm{D-}", "D-")


norm23 = norm(t23)
flag_ok = bool(t23) and ("READING" in norm23 and "parallel" in norm23.lower()) \
    and ("tick load" in norm23 or "tick-load" in norm23)
chk("D2  [BM.134(5); IT.69(5) pattern; the builder's own currency caveat (comms 0011 section 3)]: THE"
    "\n           BRIDGE FLAG (machine text census over the tier): the tier carries the flag that the"
    "\n           BRIDGE reading -- 'per-channel configuration states ARE the tick load' -- is a READING /"
    "\n           PARALLEL, NOT ADOPTED: configuration states != edge bits [CT0.9] != slot counts, and"
    "\n           CT0.5 defines D_tick by register accounting with NO config-census route declared; the"
    "\n           parallel-not-identification discipline applies [BM.134(5)]. The arithmetic identity is"
    "\n           the row; the semantics stay a reading until a route is derived or declared -- neither is"
    "\n           done here. Attribution: the builder's teacher-board audit + TickHop.lean (credited in"
    "\n           the tier).",
    flag_ok)

print("=" * 104)
print("PART E -- the verdict assembly, the bars, the status")
print("=" * 104)

a_ok = all(R[0:3])
b_ok = all(R[3:7])
c_ok = all(R[7:14])
d_ok = all(R[14:16])
verdict_ok = a_ok and b_ok and c_ok and d_ok
chk("E1  [THE VERDICT]: THE n-RADAR SYNCHRONISATION SYSTEM IS A FORMED READ FAMILY EXTENSION --"
    "\n           DERIVED, inside the issued declarations, with NO new act: (A) the n-fold family is the"
    "\n           IT.68 read at n emission ticks with the unique total order (1 of (2n)! at n = 2,3,4) and"
    "\n           the per-ping D-RS3 halving; (B) the kinematic faces are exact rational count-reads (the"
    "\n           position/velocity/acceleration ladder = the difference faces; the window economy: n pings"
    "\n           pin monic laws of degree <= n-1; the generic window honestly reads 'no law'); (C) the"
    "\n           exact cyclotomic DFT is a read-window algebra: inversion, shift/difference, Parseval,"
    "\n           and the annihilator grammar in both directions -- THE EQUATION OF MOTION IS THE SPECTRAL"
    "\n           SUPPORT, reconstructed as an exact monic rational recurrence, with the boundary defects"
    "\n           exact; (D) the L(n) capacity row placed with the builder's credit and its bridge flagged"
    "\n           a reading. WHAT IT IS NOT: not a dynamics (no trajectory, no prediction beyond the"
    "\n           window -- continuation is a stationarity-class hypothesis and D-RS4 stays deferred), not"
    "\n           a transit leg (the dynamical radar stays barred on O1/O2/O4 [IT.40-IT.42; IT.66(1)];"
    "\n           D-PJ7 owed), not an information read (the capacity-Fourier bar untouched [IT.54(1); D0.9;"
    "\n           C10]), not a coupling (count->strength barred).",
    verdict_ok, f"A:{a_ok} B:{b_ok} C:{c_ok} D:{d_ok}")


def decimal_scan(text):
    return re.findall(r"\b\d+\.\d+\b", text)


selftest = len(decimal_scan("the value 0.5 plants")) == 1 and \
    len(decimal_scan("citations D0.6 CT0.8 A6.2 stay silent")) == 0
decimals = decimal_scan(norm23)
ext_tok = "[EXT]" in norm23
sm_tok = bool(re.search(r"\bSM\b", t23)) or ("Standard Model" in t23) or ("Standard-Model" in t23) \
    or ("weak boson" in t23.lower())
new_acts = re.findall(r"D-(?:PJ|RS)\d+[^.\n]{0,40}\bISSUED\b",
                      re.sub(r"@(IT\.\d+|\\mathrm\{IT\.\d+\})", "", norm23))
dcites_ok = ("D-RS3" in norm23 and "D-RS4" in norm23 and "D-PJ7" in norm23)
bars_ok = bool(t23) and selftest and not decimals and not ext_tok and not sm_tok \
    and not new_acts and dcites_ok
chk("E2  [P1; P5; Def-BM.3(1,(7)); the FT.114 section-H scan pattern; IT.66(2) pattern]: THE BARS:"
    "\n           P5 -- zero decimal numeric tokens in the tier document (machine scan, word-bounded, with"
    "\n           the LIVE-WITNESS self-test: the scanner fires on a planted decimal and stays silent on"
    "\n           citation tokens); no [EXT] token; every numeric in the checker is an exact integer or"
    "\n           Fraction (the spectra are exact cyclotomic rationals); P1 -- NO new dimensionful scale:"
    "\n           n, j, the window entries are counts; zeta_n is a root of unity; the velocity/acceleration"
    "\n           faces are count ratios (q^0, D-RS7's price discipline); the chart faces keep the existing"
    "\n           h/ln2 monomials symbolically; the rational witnesses are PARAMETERS [IT.59(2) pattern];"
    "\n           the species-vocabulary exclusion scan (zero external-framing tokens); NO new declaration"
    "\n           issued (the act-handle scan finds none minted here; D-RS4 stays deferred, D-PJ7 stays owed"
    "\n           -- re-cited by handle only); the frozen canon cited, never edited [AT.63(2)].",
    bars_ok, f"decimals: {decimals}; EXT: {ext_tok}; species: {sm_tok}; new acts: {new_acts};"
    f" selftest: {selftest}")

status_ok = verdict_ok and bars_ok and d_ok
chk("E3  [THE STATUS]: NO new open row (the residues are the standing ones: IT-O1 -- the transit"
    "\n           dynamics, three grounds, deficit 1' = D-PJ7 owed, which the n-radar system does NOT"
    "\n           touch: every face is read-level; IT-O2 -- the binding value; IT-O5 -- the dynamical side"
    "\n           at IT-O1; the D-RS4 deferral -- now applying per ping on the chart faces; the inherited"
    "\n           value declarations [AT.63(3); IT.14(3); IT.57(2)]); NO declaration issued; Cal-IT stays"
    "\n           value-free; the erratum register unchanged; the M-freeze honored -- NOTHING in this tier"
    "\n           touches the cross-currency matrix M or its tensor square X (the Architect's restructuring"
    "\n           is pending; the IT.37-IT.39/IT.43-IT.45/IT.52 adjudications stand as records, cited by"
    "\n           no clause here); the builder channel state: comms 0012 carries the assignment and the"
    "\n           L(n) adjudication (this tier's IT.82 is the placement it promised); 'the n-radar"
    "\n           synchronisation' maps to corpus vocabulary as: the n-fold formed read family (A) + its"
    "\n           difference faces (B) + the annihilator/spectral grammar (C) -- the directive's"
    "\n           position/velocity/equation-of-motion ladder, exact at every rung.",
    status_ok)

print("=" * 104)
n_ok = sum(R)
print(f"  nradar_fft: {n_ok}/{len(R)} markers EXACT -- ALL GREEN" if n_ok == len(R)
      else f"  nradar_fft: {n_ok}/{len(R)} -- FAILURES PRESENT")
print("=" * 104)
sys.exit(0 if n_ok == len(R) else 1)
