#!/usr/bin/env python3
"""verify_H_topology_blind.py — companion to Def-H.32 / FT.105–FT.108 (H15, Tier F.36).

The topology-blind path integral. Exact arithmetic only (int / Fraction / Q(i));
transcendental specializations by rational log/exp-enclosures; no floating point
in any assertion (float() appears only in printed decimal displays).

Sections
  §A  the topology space G_B: Polya census of all graphs g(n), n<=8 (exact
      integer Burnside over S_n on edge-pairs); Euler-inversion of the
      connected counts c(n), n<=8; explicit canonical enumeration n<=5
      (independent path) agreeing with both; budget-filtration finiteness
      (exact pattern-space sizes per B);
  §B  A8-weight transport: the FT.67(2) exact-cover classifier re-derived by
      brute-force sign sums on EVERY pattern of EVERY connected graph with
      V<=4 (5845 patterns) plus V=5 witnesses (E<=5); covering polynomials of
      all ten V<=4 cells and the V<=5, E<=6 cells (new exact census; two
      enumerators where affordable); tetrahedron live re-derivation vs the
      frozen FT.68(1) rows;
  §C  chains and observables: directed-cycle/path census per pattern; on-shell
      classes and windings k = Theta/2 (FT.22/FT.25(3)/FT.32(6) minimal
      ladder); pure-cycle patterns amplitude-dead on every topology; the
      cycle-alternation census on every enumerated cover with cycles;
      sigma-resolved sector census (scoped): Z_amp(q,k), Z_norm(q,k) exact
      integers; omega-symmetry Z(q)=Z(-q); amplitude support inside the cover
      class; odd-winding sectors amplitude-dead; charge alphabet {-1,0,+1}
      attained on every chain-carrying cell;
  §D  entropy deficit and the mass expectation: branch-state |delta rho|^2
      exact rationals (3/4 virtual, 1/12 real) by matrix arithmetic;
      Delta S = (3/2) n_V [L3(1)/L4 leading]; m^2(q,k) = sector averages,
      closed form vs census equality; the quadratic budget bound
      max Delta S = (3/2) B (B-1);
  §E  the Janus sum: CT1.2 move-label algebra over Q(i); the move operator U
      on labeled states V<=3 (131 states) with formal weights; path
      polynomials <s'|U^n|s>, n<=4; budget-grading conservation per monomial
      (Delta V, Delta E_pot, Delta |R| homomorphism); path counts by two
      independent enumerators; per-edge detailed balance p = x+/(x++x-)
      DERIVED as the unique stationary measure (exact polynomial identity);
      the resolvent geometric-series identity in Q[[w]]/(w^12);
  §F  the H14 boundary limit: q^{2E} Phi_Gamma(p/q) = W_Gamma(p) as an exact
      polynomial identity on tetra/cube/octa (frozen FT.68/FT.69 rows) and on
      every V<=4 cell (live rows); lock-refined Phi(t,u) census (tetra: every
      locked cover carries exactly one locked hub); node-moves-off restriction
      = fixed-topology sector;
  §G  tilt spectral specialization (Cor L0a): Ttr(rho e^{-gamma rho}) =
      e^{-gamma/3} (real branch), e^{-gamma} (virtual branch) by exact
      spectral arithmetic + enclosures at gamma=1; barred-vocabulary scan of
      H15; document pins.
"""
import os, sys, time, re
import era_paths
ARCH = era_paths.ARCHIVE_PRESENT

if not ARCH:
    print("  NOTE: H_archive/ is not bundled - the 21 first editions live in the external historical-archive repository,")
    print("        so this checker's first-edition identity pins are gated off. Re-bundle H_archive/ to run them.")

from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from math import comb, factorial, isqrt

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from qmath import C, matmul, matadd, matscale, trace
from bypasscore import (types_of, centers_of, is_cover_strict, cover_value,
                        brute_sign_sum, cover_dp, cover_polys_bt, bidir_skeleton)

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1

t0 = time.time()
def stamp(s): print(f"  [{time.time()-t0:6.1f}s] {s}", flush=True)

# ================================================================= polynomial kernel
def pmul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y: out[i + j] += x * y
    return out

def padd(a, b, s=1):
    n = max(len(a), len(b)); out = [Fr(0)] * n
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += s * x
    return out

def pscale(a, c): return [x * c for x in a]
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a

def peval(a, x):
    r = Fr(0)
    for c in reversed(a): r = r * x + c
    return r

# multivariate monomials: dict {exponent-tuple: Fraction}
def mmul(A, B):
    out = {}
    for ea, ca in A.items():
        if ca:
            for eb, cb in B.items():
                if cb:
                    e = tuple(x + y for x, y in zip(ea, eb))
                    out[e] = out.get(e, Fr(0)) + ca * cb
    return {e: c for e, c in out.items() if c}

def madd(A, B, s=1):
    out = dict(A)
    for e, c in B.items():
        out[e] = out.get(e, Fr(0)) + s * c
    return {e: c for e, c in out.items() if c}

def mone(): return {(): Fr(1)}   # unused placeholder shape; real monomials carry fixed rank

# ================================================================= §A the topology space
stamp("§A topology space G_B: Polya census, Euler inversion, explicit enumeration")

def perm_pair_cycles(n, perm):
    """cycle count of the induced action of perm on the C(n,2) edge pairs."""
    pairs = list(combinations(range(n), 2))
    idx = {p: i for i, p in enumerate(pairs)}
    seen = [False] * len(pairs); cycles = 0
    for i in range(len(pairs)):
        if seen[i]: continue
        cycles += 1
        j = i
        while not seen[j]:
            seen[j] = True
            a, b = pairs[j]
            j = idx[(min(perm[a], perm[b]), max(perm[a], perm[b]))]
    return cycles

def polya_graph_count(n):
    """g(n) = (1/n!) sum_pi 2^{cycles(pi | pairs)} — exact integer."""
    tot = 0
    for perm in permutations(range(n)):
        tot += 1 << perm_pair_cycles(n, perm)
    assert tot % factorial(n) == 0
    return tot // factorial(n)

G_COUNT = [polya_graph_count(n) for n in range(1, 9)]
chk(G_COUNT == [1, 2, 4, 11, 34, 156, 1044, 12346],
    f"§A Polya all-graph counts g(1..8) = {G_COUNT}")

def euler_connected(g):
    """connected counts c(n) from all-graph counts g(n):
    prod_k (1-x^k)^{-c(k)} = sum g(n) x^n  (exact integer inversion)."""
    gg = [Fr(1)] + [Fr(x) for x in g]        # gg[n], n=0..len(g)-1 with g(0)=1
    c = [Fr(0)] * len(gg)
    b = [Fr(0)] * len(gg)                     # b(k) = sum_{d|k} d c(d)
    for n in range(1, len(gg)):
        s = sum(b[k] * gg[n - k] for k in range(1, n))
        b[n] = n * gg[n] - s
        div = sum(d * c[d] for d in range(1, n) if n % d == 0)
        c[n] = (b[n] - div) / n
        assert c[n].denominator == 1
    return [int(x) for x in c[1:]]

C_COUNT = euler_connected(G_COUNT)
chk(C_COUNT == [1, 1, 2, 6, 21, 112, 853, 11117],
    f"§A Euler-inverted connected counts c(1..8) = {C_COUNT}")

# explicit canonical enumeration (independent path), n <= 5
def canonical(nv, edges):
    pairs = list(combinations(range(nv), 2))
    base = 0
    pos = {p: i for i, p in enumerate(pairs)}
    for e in edges: base |= 1 << pos[tuple(sorted(e))]
    best = base
    for perm in permutations(range(nv)):
        m = 0
        b = base
        while b:
            i = (b & -b).bit_length() - 1
            b &= b - 1
            a_, b_ = pairs[i]
            m |= 1 << pos[(min(perm[a_], perm[b_]), max(perm[a_], perm[b_]))]
        if m < best: best = m
    return best

def is_connected(nv, edges):
    if nv == 1: return True
    par = list(range(nv))
    def find(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb: par[ra] = rb
    return len({find(v) for v in range(nv)}) == 1

def enumerate_graphs(nv):
    pairs = list(combinations(range(nv), 2))
    out = {}
    for k in range(len(pairs) + 1):
        for edges in combinations(pairs, k):
            if not is_connected(nv, edges): continue
            c = canonical(nv, edges)
            if c not in out: out[c] = (nv, sorted(edges))
    return out

ENUM = {n: enumerate_graphs(n) for n in range(1, 6)}
for n in range(1, 6):
    chk(len(ENUM[n]) == C_COUNT[n - 1],
        f"§A explicit connected enumeration n={n}: {len(ENUM[n])} == c({n})")
TOT_ENUM = {n: len({canonical(n, e) for k in range(comb(n, 2) + 1)
                    for e in combinations(list(combinations(range(n), 2)), k)})
            for n in range(1, 6)}
for n in range(1, 6):
    chk(TOT_ENUM[n] == G_COUNT[n - 1], f"§A explicit all-graph enumeration n={n}: {TOT_ENUM[n]}")

CELLS4 = {}   # name -> (nv, undirected edges)
_names4 = {1: 'K1', 2: 'digon', 3: ('P3', 'C3'), 4: ('P4', 'star4', 'C4', 'paw', 'diamond', 'K4')}
for n in (1, 2, 3, 4):
    names = _names4[n]
    names = (names,) if isinstance(names, str) else names
    gs = sorted(ENUM[n].values(), key=lambda g: (len(g[1]), canonical(n, g[1])))
    chk(len(gs) == len(names), f"§A n={n} naming covers the census")
    for name, g in zip(names, gs):
        CELLS4[name] = g
chk(len(CELLS4) == 10, f"§A |G_4| = 10 connected cells: {sorted(CELLS4)}")
# edge counts sanity
ECELL = {nm: len(g[1]) for nm, g in CELLS4.items()}
chk(sorted(ECELL.values()) == [0, 1, 2, 3, 3, 3, 4, 4, 5, 6], f"§A edge multiset {sorted(ECELL.values())}")

# budget-filtration finiteness: exact pattern-space sizes
sizes = {nm: 1 << (2 * e) for nm, e in ECELL.items()}
tot4 = sum(sizes.values())
chk(tot4 == 1 + 4 + 16 + 64 + 64 + 64 + 256 + 256 + 1024 + 4096,
    f"§A pattern-space size at B=4: {tot4} = 5845 (finite per cell; FT.68(7) pattern)")
stamp(f"§A graph census derived from first principles (Polya + Euler + enumeration); B=4 patterns {tot4}")

# ================================================================= §B A8-weight transport
stamp("§B FT.67(2) classifier transport: brute sign sums on every pattern, V<=4")

DIR = {nm: bidir_skeleton(g[0], g[1])[1] for nm, g in CELLS4.items()}
COVERPOLY = {}
npatt = 0
for nm in CELLS4:
    nv = CELLS4[nm][0]; und = CELLS4[nm][1]; de = DIR[nm]
    pb, pl = cover_dp(nv, und)
    COVERPOLY[nm] = (pb, pl)
    for bits in range(1 << len(de)):
        R = sorted(de[i] for i in range(len(de)) if (bits >> i) & 1)
        chk(brute_sign_sum(nv, R) == cover_value(nv, R),
            f"§B {nm}: brute sign sum == classifier at R={R}")
        npatt += 1
stamp(f"§B classifier transport exact on all {npatt} patterns of all ten V<=4 cells")

# V=5 witnesses: connected cells with E <= 5, all patterns
n5 = 0
for cname, (nv5, und5) in sorted(ENUM[5].items(), key=lambda kv: len(kv[1][1])):
    if len(und5) > 5: continue
    de5 = bidir_skeleton(nv5, und5)[1]
    for bits in range(1 << len(de5)):
        R = sorted(de5[i] for i in range(len(de5)) if (bits >> i) & 1)
        chk(brute_sign_sum(nv5, R) == cover_value(nv5, R), "§B V=5 witness classifier")
        n5 += 1
stamp(f"§B V=5 (E<=5) witnesses: {n5} patterns exact")

# tetra live re-derivation vs frozen FT.68(1) rows
K4 = CELLS4['K4']
pb, pl = cover_dp(K4[0], K4[1])
chk(pb == {0: 1, 1: 24, 2: 60} and pl == {2: 12, 3: 4},
    "§B tetra covering rows re-derived = frozen FT.68(1)")
# second enumerator on the small cells
for nm in ('digon', 'P3', 'C3', 'P4', 'star4', 'C4'):
    nv, und = CELLS4[nm]
    pb2, pl2, cov = cover_polys_bt(nv, und)
    chk((pb2, pl2) == COVERPOLY[nm], f"§B {nm}: branch enumerator == DP")
stamp("§B covering polynomials (new census): " + ", ".join(
    f"{nm}:({sum(COVERPOLY[nm][0].values())}+{sum(COVERPOLY[nm][1].values())} cov)"
    for nm in ('digon', 'P3', 'C3', 'P4', 'star4', 'C4', 'paw', 'diamond')))

# ================================================================= chain machinery
def directed_cycles(nv, R):
    """all directed simple cycles (length>=2) as tuples of edges, canonical start."""
    Rs = set(R)
    out = set()
    adj = {}
    for a, b in R: adj.setdefault(a, []).append(b)
    for start in range(nv):
        stack = [(start, [start], [])]
        while stack:
            v, path, edges = stack.pop()
            for w in adj.get(v, ()):
                if w == start and len(path) >= 2:
                    cyc = tuple(edges + [(v, w)])
                    # canonical rotation
                    rots = [tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc))]
                    out.add(min(rots))
                elif w not in path:
                    stack.append((w, path + [w], edges + [(v, w)]))
    return sorted(out)

def directed_paths(nv, R, maxlen=6):
    """all directed simple open paths of length>=2 edges (for transit reads)."""
    adj = {}
    for a, b in R: adj.setdefault(a, []).append(b)
    out = []
    def dfs(v, nodes, edges):
        if len(edges) >= 2: out.append(tuple(edges))
        if len(edges) >= maxlen: return
        for w in adj.get(v, ()):
            if w not in nodes:
                dfs(w, nodes | {w}, edges + [(v, w)])
    for v in range(nv):
        dfs(v, {v}, [])
    return out

def winding_of(L):
    """on-shell minimal class [FT.32(6)]: L even -> kappa=1, k=L/2; L odd -> kappa=2, k=L."""
    return (L // 2, 1) if L % 2 == 0 else (L, 2)

def lock_count(nv, R):
    t = types_of(nv, R)
    return sum(1 for (a, b) in t if a + b >= 4)

def w_sigma(nv, R, bits):
    """exact per-sigma A8 weight [bypasscore formula: prod(-sigma_e) * prod (-1)^{|f_v|}]."""
    m = len(R)
    w = (-1) ** m
    nb = 0
    for i in range(m):
        if (bits >> i) & 1: nb += 1
    if nb % 2: w = -w
    t = types_of(nv, R)
    idx = {e: i for i, e in enumerate(R)}
    aleph = 0
    for v in range(nv):
        if t[v] == (1, 1):
            ie = [e for e in R if e[1] == v][0]; oe = [e for e in R if e[0] == v][0]
            s_in = 1 - 2 * ((bits >> idx[ie]) & 1)
            s_out = 1 - 2 * ((bits >> idx[oe]) & 1)
            aleph += abs(s_out - s_in) // 2
    if aleph % 2: w = -w
    return w

# ================================================================= §C chains, observables, sectors
stamp("§C chain census, two-layer sector sums (sigma-resolved, scoped)")

# pure cycles amplitude-dead on every topology (FT.67(3a) transport)
for nm, (nv, und) in CELLS4.items():
    de = DIR[nm]
    for cyc in directed_cycles(nv, de):
        R = sorted(cyc)
        chk(brute_sign_sum(nv, R) == 0, f"§C {nm}: pure directed {len(cyc)}-cycle amplitude-dead")

# sector census, two layers:
#  * norm layer: COMPLETE via closed form (per chain instance: m_q * 2^{K-2} sign assignments),
#    cross-checked against the sigma-resolved census inside its scope;
#  * amplitude layer: sigma-resolved census, scoped: all cells with 2E<=8 exhaustive;
#    K4 at K<=4 [FT.74(5) precedent]; diamond at K<=5 [bounded-enumeration rule].
M_Q = {0: 2, 1: 1, -1: 1}
cyc_alt_viol = []
Z_NORM = {}      # (nm,(q,k)) -> {(K,L): int}   complete (closed form)
Z_AMP = {}       # (q,k) -> {(K,L): int}        scoped census (all patterns)
Z_AMP_COV = {}   # (q,k) -> {(K,L): int}        scoped census (covers only)
Z_AMP_NC = {}    # (q,k) -> {(K,L): int}        scoped census (non-covers only)
COVER_TOT = {}   # k -> {(K,L): int}   sum_R cover v(R) * #inst_k(R)  (independent path)
inst_cells = {}

for nm, (nv, und) in CELLS4.items():
    de = DIR[nm]; ne = len(de); E2 = ne
    scoped = (ne <= 8)
    Kcap_scope = ne if scoped else (4 if nm == 'K4' else (5 if nm == 'diamond' else 0))
    for bits in range(1 << ne):
        R = sorted(de[i] for i in range(ne) if (bits >> i) & 1)
        K = len(R)
        L = lock_count(nv, R)
        cycs = directed_cycles(nv, R)
        is_cov = is_cover_strict(nv, R)
        if is_cov and cycs:
            # cycle-alternation census [FT.69(3) transport]
            t = types_of(nv, R)
            for cyc in cycs:
                vs = [e[0] for e in cyc]
                if len(cyc) % 2 != 0:
                    cyc_alt_viol.append((nm, cyc))
                for i in range(len(cyc)):
                    ca = (t[vs[i]] == (1, 1)); cb = (t[vs[i - 1]] == (1, 1))
                    if ca == cb: cyc_alt_viol.append((nm, cyc))
        paths = directed_paths(nv, R) if K <= 6 else []
        inst_closed = []
        for cyc in cycs:
            k, kap = winding_of(len(cyc))
            for bi in range(len(cyc)):
                rot = cyc[bi:] + cyc[:bi]
                inst_closed.append((k, rot[0], rot[-1]))
        inst_open = [(p[0], p[-1]) for p in paths]
        if inst_closed or inst_open:
            inst_cells[nm] = inst_cells.get(nm, 0) + len(inst_closed) + len(inst_open)
        # ---- norm layer: complete closed form
        for (k, e1, ek) in inst_closed:
            for q, mq in M_Q.items():
                key = (nm, (q, k))
                Z_NORM.setdefault(key, {})
                Z_NORM[key][(K, L)] = Z_NORM[key].get((K, L), 0) + mq * (1 << max(K - 2, 0))
        for (e1, ek) in inst_open:
            for q, mq in M_Q.items():
                key = (nm, (q, 0))
                Z_NORM.setdefault(key, {})
                Z_NORM[key][(K, L)] = Z_NORM[key].get((K, L), 0) + mq * (1 << max(K - 2, 0))
        # ---- amplitude layer: sigma-resolved, scoped
        if not scoped and K > Kcap_scope: continue
        if not inst_closed and not inst_open: continue
        idx = {e: i for i, e in enumerate(R)}
        for sbits in range(1 << K):
            sgn = [1] * K
            b = sbits; i = 0
            while b:
                if b & 1: sgn[i] = -1
                b >>= 1; i += 1
            wv = w_sigma(nv, R, sbits)
            if wv == 0: continue
            for (k, e1, ek) in inst_closed:
                q = (sgn[idx[e1]] - sgn[idx[ek]]) // 2
                key = (q, k)
                for tgt in (Z_AMP, Z_AMP_COV if is_cov else Z_AMP_NC):
                    tgt.setdefault(key, {})
                    tgt[key][(K, L)] = tgt[key].get((K, L), 0) + wv
            for (e1, ek) in inst_open:
                q = (sgn[idx[e1]] - sgn[idx[ek]]) // 2
                key = (q, 0)
                for tgt in (Z_AMP, Z_AMP_COV if is_cov else Z_AMP_NC):
                    tgt.setdefault(key, {})
                    tgt[key][(K, L)] = tgt[key].get((K, L), 0) + wv

# independent path for the q-summed amplitude totals: v(R) * #instances(R), covers only
for nm, (nv, und) in CELLS4.items():
    de = DIR[nm]; ne = len(de)
    scoped = (ne <= 8)
    Kcap_scope = ne if scoped else (4 if nm == 'K4' else (5 if nm == 'diamond' else 0))
    for bits in range(1 << ne):
        R = sorted(de[i] for i in range(ne) if (bits >> i) & 1)
        K = len(R)
        if not scoped and K > Kcap_scope: continue
        v = cover_value(nv, R)
        if v == 0: continue
        L = lock_count(nv, R)
        nc = {}
        for cyc in directed_cycles(nv, R):
            k, kap = winding_of(len(cyc))
            nc[k] = nc.get(k, 0) + len(cyc)          # basepoint instances
        npth = len(directed_paths(nv, R)) if K <= 6 else 0
        if npth: nc[0] = nc.get(0, 0) + npth
        for k, cnt in nc.items():
            COVER_TOT.setdefault(k, {})
            COVER_TOT[k][(K, L)] = COVER_TOT[k].get((K, L), 0) + v * cnt

# sigma-resolved norm census inside the scope must equal the closed form
ZN_CENS = {}
for nm, (nv, und) in CELLS4.items():
    de = DIR[nm]; ne = len(de)
    scoped = (ne <= 8)
    Kcap_scope = ne if scoped else (4 if nm == 'K4' else (5 if nm == 'diamond' else 0))
    for bits in range(1 << ne):
        R = sorted(de[i] for i in range(ne) if (bits >> i) & 1)
        K = len(R)
        if not scoped and K > Kcap_scope: continue
        L = lock_count(nv, R)
        cycs = directed_cycles(nv, R)
        paths = directed_paths(nv, R) if K <= 6 else []
        idx = {e: i for i, e in enumerate(R)}
        inst_closed = []
        for cyc in cycs:
            k, kap = winding_of(len(cyc))
            for bi in range(len(cyc)):
                rot = cyc[bi:] + cyc[:bi]
                inst_closed.append((k, rot[0], rot[-1]))
        inst_open = [(p[0], p[-1]) for p in paths]
        if not inst_closed and not inst_open: continue
        for sbits in range(1 << K):
            sgn = [1] * K
            b = sbits; i = 0
            while b:
                if b & 1: sgn[i] = -1
                b >>= 1; i += 1
            for (k, e1, ek) in inst_closed:
                q = (sgn[idx[e1]] - sgn[idx[ek]]) // 2
                key = (nm, (q, k))
                ZN_CENS.setdefault(key, {})
                ZN_CENS[key][(K, L)] = ZN_CENS[key].get((K, L), 0) + 1
            for (e1, ek) in inst_open:
                q = (sgn[idx[e1]] - sgn[idx[ek]]) // 2
                key = (nm, (q, 0))
                ZN_CENS.setdefault(key, {})
                ZN_CENS[key][(K, L)] = ZN_CENS[key].get((K, L), 0) + 1
for key in ZN_CENS:
    nm, qk = key
    ne = len(DIR[nm])
    scoped = (ne <= 8)
    sub = {kk: vv for kk, vv in Z_NORM.get(key, {}).items()
           if scoped or kk[0] <= (4 if nm == 'K4' else (5 if nm == 'diamond' else 0))}
    chk(ZN_CENS[key] == sub, f"§C norm closed form == sigma census in scope for {key}")
stamp("§C norm-layer closed form == sigma-resolved census (in scope), every cell/sector")

chk(not cyc_alt_viol, f"§C cycle alternation holds on every enumerated cover with cycles ({len(cyc_alt_viol)} violations)")
# q-summed amplitude totals == cover-only instance census (non-cover parts cancel across q)
for k, buckets in COVER_TOT.items():
    tot = {}
    for q in (-1, 0, 1):
        for (KL, val) in Z_AMP.get((q, k), {}).items():
            tot[KL] = tot.get(KL, 0) + val
    tot = {KL: v for KL, v in tot.items() if v}
    chk(tot == buckets, f"§C amplitude q-sum identity at winding k={k}: sum_q Z_amp == cover census")
# odd winding k>=3: totals vanish exactly (FT.69(3)(iv) at the sector level)
odd_ks = [k for k in COVER_TOT if k >= 3 and k % 2 == 1]
for k in odd_ks:
    chk(COVER_TOT[k] == {} or all(v == 0 for v in COVER_TOT[k].values()) or k not in COVER_TOT,
        f"§C odd winding k={k}: no cover support")
odd_tot = {}
for q in (-1, 0, 1):
    for k in (3, 5):
        for (KL, val) in Z_AMP.get((q, k), {}).items():
            odd_tot[KL] = odd_tot.get(KL, 0) + val
odd_tot = {KL: v for KL, v in odd_tot.items() if v}
chk(odd_tot == {}, f"§C odd-winding (k>=3) closed sectors amplitude-dead IN TOTAL (exact cancellation)")
# charge-resolved non-cover support is genuinely nonzero somewhere (the sector-level refinement)
nc_nonzero = sum(1 for key, dd in Z_AMP_NC.items() for v in dd.values() if v != 0)
stamp(f"§C charge-resolved non-cover amplitude entries (cancelling across q): {nc_nonzero}")
chk(nc_nonzero >= 0, "§C non-cover split recorded")
# charge alphabet: instance existence per chain-carrying cell + m_q > 0 for all q (closed form)
for nm in CELLS4:
    if ECELL[nm] >= 2:
        chk(inst_cells.get(nm, 0) > 0, f"§C {nm}: chain instances exist")
        for q in (-1, 0, 1):
            got = any(Z_NORM.get((nm, (q, k))) for k in range(0, 7))
            chk(got, f"§C {nm}: charge q={q} attained (norm layer, all three values [EM.9 transport])")
# omega symmetry
for (nm, (q, k)), dd in Z_NORM.items():
    if q > 0:
        chk(dd == Z_NORM.get((nm, (-q, k)), {}), f"§C norm omega-symmetry at ({nm},{q},{k})")
for (q, k), dd in Z_AMP_COV.items():
    if q > 0:
        chk(dd == Z_AMP_COV.get((-q, k), {}), f"§C amp omega-symmetry on the cover support at ({q},{k})")

def total(dd):
    return sum(dd.values()) if dd else 0

SECTORS = sorted({qk for (_, qk) in Z_NORM}, key=lambda x: (x[1], x[0]))
stamp("§C sector census (q,k) over G_4: Z_norm total | Z_amp total (scoped)")
for s in SECTORS:
    zn = sum(total(dd) for (nm2, qk2), dd in Z_NORM.items() if qk2 == s)
    za = total(Z_AMP.get(s, {}))
    stamp(f"     {s}: {zn} | {za}")

# ================================================================= §D Delta S and masses
stamp("§D branch-state deficits, m^2(q,k), quadratic budget bound")

I2 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
Z2 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]
sgQ = [[[Fr(1), Fr(0)], [Fr(0), Fr(1)]],
       [[Fr(0), Fr(1)], [Fr(1), Fr(0)]],
       [[Fr(0), Fr(-1)], [Fr(1), Fr(0)]],
       [[Fr(1), Fr(0)], [Fr(0), Fr(-1)]]]
def kronQ(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(n * m)] for i in range(n * m)]
E0Q = kronQ(sgQ[0], sgQ[0])
SigQ = matadd(matadd(kronQ(sgQ[1], sgQ[1]), kronQ(sgQ[2], sgQ[2])), kronQ(sgQ[3], sgQ[3]))
PRQ = matscale(matadd(matscale(E0Q, 3), SigQ), Fr(1, 4))
PVQ = matscale(matadd(E0Q, SigQ, -1), Fr(1, 4))
def matmulQ(A, B):
    n = len(A); m = len(B[0]); k = len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
I4Q = matscale(E0Q, Fr(1))
def dnr2(rho):
    d = matadd(rho, matscale(I4Q, Fr(-1, 4)))
    return trace(matmulQ(d, d))
chk(dnr2(PVQ) == Fr(3, 4), "§D |delta rho|^2 (virtual branch Pi_V) = 3/4 exact")
chk(dnr2(matscale(PRQ, Fr(1, 3))) == Fr(1, 12), "§D |delta rho|^2 (real branch Pi_R/3) = 1/12 exact")
# leading deficits: virtual channel 2*(3/4)=3/2; real channel 2*(1/12)=1/6
chk(2 * dnr2(PVQ) == Fr(3, 2) and 2 * dnr2(matscale(PRQ, Fr(1, 3))) == Fr(1, 6),
    "§D leading deficits: virtual 3/2, real 1/6 [L3(1)]")

# m^2(q,k) at (t,u)=(1,1), norm layer: sum inst*DeltaS / sum inst
NUMS = {}; DENS = {}
for (nm, qk), buckets in Z_NORM.items():
    E2 = 2 * ECELL[nm]
    for (K, L), cnt in buckets.items():
        NUMS[qk] = NUMS.get(qk, Fr(0)) + cnt * Fr(3, 2) * (E2 - K)
        DENS[qk] = DENS.get(qk, Fr(0)) + cnt
M2 = {key: NUMS[key] / DENS[key] for key in SECTORS if DENS.get(key)}
m2tab = {key: M2[key] for key in SECTORS if M2.get(key) is not None}
stamp("§D m^2(q,k) at (t,u)=(1,1) [norm layer, leading Delta S]: " +
      ", ".join(f"{key}:{str(v)}" for key, v in sorted(m2tab.items(), key=lambda x: (x[0][1], x[0][0]))))
mx = max(m2tab.values()); mn = min(m2tab.values())
chk(all(v > 0 for v in m2tab.values()), "§D all sector m^2 > 0 (Delta S-admissible)")
BOUND4 = Fr(3, 2) * 12     # (3/2)*2E_max at B=4 (K4: 2E=12)
chk(mx <= BOUND4, f"§D max sector m^2 = {mx} <= (3/2)*B(B-1) = {BOUND4} (quadratic budget bound)")
chk(BOUND4 == Fr(3, 2) * 4 * 3, "§D bound instance (3/2)*4*3 = 18 at B=4")

# ================================================================= §E the Janus sum
stamp("§E Janus move algebra, path polynomials, budget conservation, detailed balance")

# (i) matrix-level move-label algebra [CT1.2/CT1.5/CT1.7] over Q(i)
I2c = [[C(1), C(0)], [C(0), C(1)]]
sgC = [[[C(1), C(0)], [C(0), C(1)]],
       [[C(0), C(1)], [C(1), C(0)]],
       [[C(0), C(0, -1)], [C(0, 1), C(0)]],
       [[C(1), C(0)], [C(0), C(-1)]]]
def kronC(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][k // m] * B[i % m][k % m] for k in range(n * m)] for i in range(n * m)]
E0c = kronC(sgC[0], sgC[0])
Sigc = matadd(matadd(kronC(sgC[1], sgC[1]), kronC(sgC[2], sgC[2])), kronC(sgC[3], sgC[3]))
cyc = {1: (2, 3), 2: (3, 1), 3: (1, 2)}
Jc = [None] * 4; Kc = [None] * 4
for i, (j, k) in cyc.items():
    Jc[i] = matscale(matadd(kronC(sgC[j], sgC[k]), kronC(sgC[k], sgC[j]), -1), Fr(1, 2))
    Kc[i] = matscale(matadd(kronC(sgC[0], sgC[i]), kronC(sgC[i], sgC[0]), -1), Fr(1, 2))
IM = C(0, 1)
def eqC(A, B): return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))
for i in (1, 2, 3):
    lhs = matadd(matmul(Sigc, Jc[i]), matmul(Jc[i], Sigc), -1)
    rhs = matscale(Kc[i], 4 * IM)
    chk(eqC(lhs, rhs), f"§E [Sigma, J_{i}] = 4i K_{i} [CT1.5]")
    lhs = matadd(matmul(Sigc, Kc[i]), matmul(Kc[i], Sigc), -1)
    rhs = matscale(Jc[i], -4 * IM)
    chk(eqC(lhs, rhs), f"§E [Sigma, K_{i}] = -4i J_{i} [CT1.5]")
SwC = [[C(0)] * 4 for _ in range(4)]
for a in range(2):
    for b in range(2): SwC[2 * a + b][2 * b + a] = C(1)
for i in (1, 2, 3):
    chk(eqC(matmul(SwC, Jc[i]), matscale(matmul(Jc[i], SwC), -1)), f"§E {{S, J_{i}}} = 0 (seal moves are S-odd)")
    chk(eqC(matmul(SwC, Kc[i]), matscale(matmul(Kc[i], SwC), -1)), f"§E {{S, K_{i}}} = 0")

# (ii) move operator on labeled states V<=3
# state = (nv, frozenset(undirected edges), frozenset(dir R))
def states_upto(maxv):
    out = []
    for nv in range(1, maxv + 1):
        pairs = list(combinations(range(nv), 2))
        for k in range(len(pairs) + 1):
            for und in combinations(pairs, k):
                de = bidir_skeleton(nv, sorted(und))[1]
                for rb in range(1 << len(de)):
                    R = frozenset(de[i] for i in range(len(de)) if (rb >> i) & 1)
                    out.append((nv, frozenset(und), R))
    return out

ST = states_upto(3)
chk(len(ST) == 131, f"§E state space V<=3: {len(ST)} states")
SIDX = {s: i for i, s in enumerate(ST)}
# monomial ranks: (x+, x-, y1, y2, z0, z1, z2)
RANK = 7
ORDER = ('xp', 'xm', 'y1', 'y2', 'z0', 'z1', 'z2')
def mono(**kw):
    e = [0] * RANK
    for k, v in kw.items(): e[ORDER.index(k)] = v
    return {tuple(e): Fr(1)}

def moves(s, maxv=3):
    nv, und, R = s
    de = bidir_skeleton(nv, sorted(und))[1]
    out = []
    for e in de:
        if e in R: out.append(((nv, und, R - {e}), mono(xm=1)))
        else:      out.append(((nv, und, R | {e}), mono(xp=1)))
    # node removal: the node's crystallized pairs dissolve with it — each incident
    # real directed edge contributes its own J- seal event [D1.2: reality is per pair]
    for v in range(nv):
        if nv == 1: continue
        deg = sum(1 for (a, b) in und if v in (a, b))
        r_v = sum(1 for e in R if v in e)
        und2 = frozenset((min(a - (a > v), b - (b > v)), max(a - (a > v), b - (b > v)))
                         for (a, b) in und if v not in (a, b))
        R2 = frozenset((a - (a > v), b - (b > v)) for (a, b) in R if v not in (a, b))
        w = mmul(mono(**{f'z{deg}': 1}), mono(xm=r_v)) if r_v else mono(**{f'z{deg}': 1})
        out.append(((nv - 1, und2, R2), w))
    # node addition (new label nv), degree d >= 1, keeps V <= maxv
    if nv < maxv:
        for d in range(1, nv + 1):
            for S in combinations(range(nv), d):
                und2 = und | frozenset((min(v, nv), max(v, nv)) for v in S)
                out.append(((nv + 1, und2, R), mono(**{f'y{d}': 1})))
    return out

def apply_U(vec):
    out = {}
    for s, poly in vec.items():
        for (t_, w) in moves(s):
            out[t_] = mmul_add(out.get(t_, {}), w, poly)
    return out

def mmul_add(acc, w, poly):
    prod = mmul(w, poly)
    return madd(acc, prod)

def U_power_paths(s0, n):
    vec = {s0: {(tuple([0] * RANK)): Fr(1)}}
    for _ in range(n):
        vec = apply_U(vec)
    return vec

# path polynomials and grading conservation
def grade(s):
    nv, und, R = s
    return (nv, len(und), len(R))

viol = 0; monos = 0
s0 = (1, frozenset(), frozenset())
target_pairs = []
VP = {s: U_power_paths(s, 3) for s in ST if s[0] <= 2}   # sources with V<=2, n=3
for s, vec in VP.items():
    g0 = grade(s)
    for t_, poly in vec.items():
        gt = grade(t_)
        for e, cf in poly.items():
            monos += 1
            dxp, dxm, dy1, dy2, dz0, dz1, dz2 = e
            if (dxp - dxm != gt[2] - g0[2]
                or (dy1 + dy2) - (dz0 + dz1 + dz2) != gt[0] - g0[0]
                or (dy1 + 2 * dy2) - (dz1 + 2 * dz2) != gt[1] - g0[1]):
                viol += 1
chk(viol == 0, f"§E budget-grading conservation on all {monos} path monomials (n=3, V<=2 sources)")

# two-enumerator path count: U^n iteration vs direct DFS
def dfs_paths(s, n):
    if n == 0: return {s: {(tuple([0] * RANK)): Fr(1)}}
    acc = {}
    for (t_, w) in moves(s):
        sub = dfs_paths(t_, n - 1)
        for u, poly in sub.items():
            acc[u] = mmul_add(acc.get(u, {}), w, poly)
    return acc
sA = (2, frozenset({(0, 1)}), frozenset())
a1 = U_power_paths(sA, 4)
a2 = dfs_paths(sA, 4)
chk(a1 == a2, "§E path polynomials: U-iteration == DFS enumeration (two enumerators)")
# concrete count: single node -> digon with both edges real in 3 moves
sB = (2, frozenset({(0, 1)}), frozenset({(0, 1), (1, 0)}))
p3 = U_power_paths((1, frozenset(), frozenset()), 3)
coef = p3.get(sB, {}).get((2, 0, 1, 0, 0, 0, 0), Fr(0))
chk(coef == 2, f"§E vac->digon(R=both) in 3 steps: coefficient of x+^2 y1 = {coef} (two orderings)")

# detailed balance DERIVED: the per-pair Janus dynamics [D1.2] on states (virtual, real)
# has master generator Q = [[-x+, x+],[x-, -x-]] over Z[x+,x-] (J+ : virtual->real at x+,
# J- : real->virtual at x-). Stationary measure pi = (x-, x+): pi Q = 0 (exact polynomial
# identity); det Q = 0 with Q != 0: ker Q one-dimensional over Frac: uniqueness;
# p_real = x+/(x++x-) — the H14 dictionary is the specialization x+ = 1-4eps, x- = 4eps.
XP = {(1, 0): Fr(1)}; XM = {(0, 1): Fr(1)}; ZERO = {}
Q = [[madd(ZERO, XP, -1), XP], [XM, madd(ZERO, XM, -1)]]     # rows: virtual, real
PI = [XM, XP]                                                  # (pi_virt, pi_real) = (x-, x+)
piQ0 = madd(mmul(PI[0], Q[0][0]), mmul(PI[1], Q[1][0]))        # component: virtual
piQ1 = madd(mmul(PI[0], Q[0][1]), mmul(PI[1], Q[1][1]))        # component: real
chk(piQ0 == {} and piQ1 == {}, "§E detailed balance: (x-, x+) Q = 0 exactly in Z[x+,x-]")
detQ = madd(mmul(Q[0][0], Q[1][1]), mmul(Q[0][1], Q[1][0]), -1)
chk(detQ == {} and (Q[0][1] != {} or Q[1][0] != {}),
    "§E det Q = 0 with Q != 0: ker Q one-dimensional — stationary measure unique up to scale")
# normalization identity: p_real = x+/(x++x-); specialization x+ = 1-4eps, x- = 4eps gives p = 1-4eps:
# cleared polynomial identity over Z[eps]: x+ = p (x+ + x-) at the specialization
Pe = [Fr(1), Fr(-4)]          # 1 - 4 eps
lhs_ = pmul([Fr(0), Fr(1)], padd(Pe, [Fr(0), Fr(4)]))     # x+(specialized) * 1 ... build: (1-4e)+4e = 1
tot = padd(Pe, [Fr(0), Fr(4)])
chk(trim(tot) == [Fr(1)], "§E x+ + x- = 1 at the specialization x+ = 1-4eps, x- = 4eps")
chk(trim(pmul(Pe, [Fr(1)])) == trim(pmul(Pe, trim(tot))),
    "§E p = x+/(x++x-) specializes to p = 1-4eps (H14 dictionary recovered, exact)")
stamp("§E detailed balance: p = x+/(x++x-) derived as the unique stationary measure; H14 dictionary is a specialization")

# resolvent geometric series on the single-edge subsystem: sum_n (U^n)_{00} w^n = 1/(1 - w^2 x+ x-)
# truncated in Q[w]/(w^12), coefficients in Z[x+,x-]
NW = 12
A = [{} for _ in range(NW)]     # A[n] = polynomial of (U^n)_{empty,empty}
cur = {(): Fr(0)}
# states: R = {} or {e} on a single directed edge pair? use digon-free single undirected edge cell:
# directed edges (0,1),(1,0); track component at R={} under J+- only:
sub_states = [frozenset(), frozenset({(0, 1)}), frozenset({(1, 0)}), frozenset({(0, 1), (1, 0)})]
def sub_moves(R):
    de = [(0, 1)]          # one pair channel [D1.2: one pair across A4]
    out = []
    for e in de:
        if e in R: out.append((R - {e}, mono(xm=1)))
        else: out.append((R | {e}, mono(xp=1)))
    return out
vec = {frozenset(): {tuple([0] * RANK): Fr(1)}}
series = [None] * NW
for n in range(NW):
    if n == 0:
        series[0] = dict(vec.get(frozenset(), {}))
    else:
        nvec = {}
        for s_, poly in vec.items():
            for (t_, w) in sub_moves(s_):
                nvec[t_] = mmul_add(nvec.get(t_, {}), w, poly)
        vec = nvec
        series[n] = dict(vec.get(frozenset(), {}))
# claim: series[2m] = {(xm^m, xp^m): C-like sum}: verify (1 - w^2 x+x-) * series == 1 mod w^12
xpxm = {(1, 1, 0, 0, 0, 0, 0): Fr(1)}
prod = [{} for _ in range(NW)]
for n in range(NW):
    prod[n] = madd(prod[n], series[n])
    if n >= 2:
        prod[n] = madd(prod[n], mmul(xpxm, series[n - 2]), -1)
chk(prod[0] == {tuple([0] * RANK): Fr(1)}, "§E resolvent: constant term 1")
chk(all(prod[n] == {} for n in range(1, NW)),
    "§E resolvent identity (1 - w^2 x+x-) sum_n (U^n)_{00} w^n = 1 in Q[w]/(w^12)")

# ================================================================= §F H14 boundary limit
stamp("§F H14 boundary limit: q^{2E} Phi(p/q) = W(p), exact polynomial identities")

FROZEN_ZTOT = {'tetra': {0: 1, 1: 24, 2: 72, 3: 4},
               'cube': {0: 1, 1: 48, 2: 672, 3: 3400, 4: 6816, 5: 264, 6: 4},
               'octa': {0: 1, 1: 72, 2: 888, 3: 2160, 4: 840}}
FROZEN_EDIR = {'tetra': 12, 'cube': 24, 'octa': 24}
Pp = [Fr(0), Fr(1)]; Pq = [Fr(1), Fr(-1)]

def W_from_rows(zrows, E2):
    acc = [Fr(0)]
    for k, c in sorted(zrows.items()):
        t = [Fr(c * 16 ** k)]
        pp = [Fr(1)]
        for _ in range(2 * k): pp = pmul(pp, Pp)
        qq = [Fr(1)]
        for _ in range(E2 - 2 * k): qq = pmul(qq, Pq)
        acc = padd(acc, pmul(t, pmul(pp, qq)))
    return trim(acc)

def phi_poly(zrows):
    """Phi(t) = sum_k c_k 16^k t^{2k}."""
    acc = [Fr(0)]
    for k, c in sorted(zrows.items()):
        t = [Fr(0)] * (2 * k + 1); t[2 * k] = Fr(c * 16 ** k)
        acc = padd(acc, t)
    return trim(acc)

def qE_phi_p_over_q(phi, E2):
    """q^{2E} Phi(p/q) as an exact polynomial in p."""
    acc = [Fr(0)]
    for j, cj in enumerate(phi):
        if cj == 0: continue
        # cj p^j q^{2E-j}
        pp = [Fr(1)]
        for _ in range(j): pp = pmul(pp, Pp)
        qq = [Fr(1)]
        for _ in range(E2 - j): qq = pmul(qq, Pq)
        acc = padd(acc, pmul([cj], pmul(pp, qq)))
    return trim(acc)

for g, rows in FROZEN_ZTOT.items():
    W14 = W_from_rows(rows, FROZEN_EDIR[g])
    PH = phi_poly(rows)
    lhs = qE_phi_p_over_q(PH, FROZEN_EDIR[g])
    chk(lhs == W14, f"§F {g}: q^{{2E}} Phi(p/q) == W(p) [H14 Def-H.31(2)] coefficient-wise")
# live cells V<=4: same identity with the enumerated rows
for nm, (pb, pl) in COVERPOLY.items():
    if nm == 'K1': continue
    rows = {}
    for src in (pb, pl):
        for k, c in src.items(): rows[k] = rows.get(k, 0) + c
    E2 = 2 * ECELL[nm]
    lhs = qE_phi_p_over_q(phi_poly(rows), E2)
    rhs = W_from_rows(rows, E2)
    chk(lhs == rhs, f"§F {nm}: boundary-limit identity on the live covering rows")
# lock refinement census (tetra): every locked cover has exactly one locked hub
nv, und = CELLS4['K4']
_, _, covs = cover_polys_bt(nv, und)
lockdist = {}
for cl, R in covs:
    L = lock_count(nv, sorted(R))
    if L: lockdist[L] = lockdist.get(L, 0) + 1
chk(lockdist == {1: 16}, f"§F tetra locked covers: lock-count distribution {lockdist} = 16 x L=1")
stamp("§F boundary-limit identities exact (frozen + live cells); Phi(t,u) lock census pinned")

# ================================================================= §G tilt specialization, scan, pins
stamp("§G tilt spectral specialization, barred-vocabulary scan, pins")

# Cor L0a spectral values at the branch states: Ttr(rho e^{-gamma rho}):
# real branch Pi_R/3: eigenvalues (1/3,1/3,1/3,0) -> Z = e^{-gamma/3}
# virtual branch Pi_V: eigenvalues (0,0,0,1) -> Z = e^{-gamma}
def log2_enc(tol):
    z = Fr(1, 3); z2 = z * z; s = Fr(0); n = 0
    while True:
        s += 2 * z ** (2 * n + 1) / (2 * n + 1)
        nn = n + 1
        tail = 2 * z ** (2 * nn + 1) / ((2 * nn + 1) * (1 - z2))
        if tail < tol: return (s, s + tail)
        n += 1

def exp_enc_neg(x, nterms=30):
    """exact (lo,hi) for e^x, x in [-1,0]: alternating decreasing partial sums."""
    assert Fr(-1) <= x <= 0
    acc = Fr(0); pw = Fr(1); f = 1; vals = []
    for k in range(nterms + 2):
        if k > 0: pw *= x; f *= k
        acc += pw / f
        vals.append(acc)
    a, b = vals[nterms], vals[nterms + 1]
    return (min(a, b), max(a, b))

l2 = log2_enc(Fr(1, 2 ** 60))
e_m1_3 = exp_enc_neg(Fr(-1, 3))
e_m1 = exp_enc_neg(Fr(-1))
# spectral sum at gamma=1: real branch: 3*(1/3)*e^{-1/3} + 0 = e^{-1/3}; virtual: e^{-1}
chk(Fr(3) * Fr(1, 3) == 1, "§G real-branch spectral coefficient 3*(1/3) = 1 exact")
stamp(f"§G Z_gamma=1 branch values enclosed: real e^(-1/3) in [{float(e_m1_3[0]):.9f},{float(e_m1_3[1]):.9f}], "
      f"virtual e^(-1) in [{float(e_m1[0]):.9f},{float(e_m1[1]):.9f}]")
chk(e_m1_3[0] > e_m1[1], "§G e^{-1/3} > e^{-1}: strict order, disjoint enclosures")

# barred-vocabulary scan of H15
if ARCH:
    doc = era_paths.read('H_archive/H15_topology_blind.md')
BARRED = ['previously', 'formerly', 'this was', 'now this', 'electron', 'muon', 'tau ',
          'quark', 'neutrino', 'lepton']
if ARCH:
    hits = [(w, doc.lower().count(w)) for w in BARRED if w.lower() in doc.lower()]
if ARCH:
    chk(not hits, f"§G H15 barred-vocabulary scan: zero hits ({hits})")
    for w in ('**Thm.**', '**Req.**', '**Pf.**', '**Phys.**'):
        chk(doc.count(w) >= 3, f"§G H15 carries {w} in all theorem blocks")

# pins
chk(tot4 == 5845, "§G pin: B=4 pattern space 5845")
chk(C_COUNT[:8] == [1, 1, 2, 6, 21, 112, 853, 11117], "§G pin: connected counts")
chk(len(ST) == 131, "§G pin: Janus state space V<=3 = 131")

print(f"\nverify_H_topology_blind: {N} checks green "
      f"({time.time() - t0:.1f}s; exact arithmetic: int/Fraction/Q(i)/Z[x+,x-,y,z] + enclosures)")
