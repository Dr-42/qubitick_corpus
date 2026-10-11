#!/usr/bin/env python3
"""verify_H_extdomains.py — companion to Def-H.27 / FT.74 / FT.75.
Exact arithmetic only (int). Asserts every tabulated value of Tier F.25:
  * Def-H.27 semantics implemented twice — brute force (explicit enumeration of all walk
    partitions D for E1, all partial-matching systems M with orbit-wrap closure for E2) and
    the closed classifiers N_E1/N_E2 of FT.74(1)-(2) — and cross-verified on EVERY pattern
    of seven families (the battery of FT.74(5): 2460 pattern-domain checks);
  * FT.74(2) display convention: the corrected monomial w = (-1)^{sum kappa} prod_{cov even} sigma_e
    re-derived from scratch and asserted on every tetrahedron pattern;
  * FT.74(3): pointwise order N_E2 <= N_E1 and even support (exhaustive families), the six-row
    witness table in all three domains (classifier = brute force), digon death in all three;
  * FT.74(4): the equality locus E2 == E1 on patterns without type-(1,1) vertices;
  * FT.75(1): single-vertex star closed forms (bypass domain-invariant 1+4 n_in n_out; locked
    literal 0, E2 = E1 = sum_{a>=2} C(n_in,a) C(n_out,a) a! 4^a), the locked digon-hub
    derangement family (literal 4^a, E2 0, E1 !a 4^a; a = 2..5, brute force a <= 3), and the
    tetrahedron's 12 + 4 locked digon-cover instances;
  * FT.75(2): floor thread counts (tetra 32 / cube 2304 / octa 72384) with exact values, the
    even-L parity theorem for bidirectional polygon floors (L = 3..10), the pure-orientation
    and #FF = #BB = L/2 witness, and literal-domain floor death;
  * FT.75(3): the directed-cycle family L = 3..10 in all three domains;
  * FT.75(4): the tetrahedron triangle census (2397 carriers; 0/833/1025; bypass-only 0/40/88),
    the exhibited witness, the FT.68(1)/FT.69(4) census anchors (501/252/90; 48/0/0), and the
    digon-cover split (48 bypass killed by both extensions; 16 locked killed by E2, kept by E1);
  * FT.75(5): skeleton totals for the tetrahedron and bidirectional P_3..P_6 (bypass/locked
    sums and nonzero counts in all three domains), the literal column reproducing the earlier record;
  * FT.75(6): |w| = 1 on every (R, D, sigma) of the bidirectional triangle, and the exact
    pattern-sign configuration count 3^{|E_dir|};
  * FT.75(8)/regression: the counting side (cap census, admissibility) untouched by the domain
    choice; literal anchors (tetra Z = 1057/448/1505; single vertex 17/25/37).
"""
import os, sys, time
from itertools import combinations, product
from math import comb, factorial

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bypasscore import (bidir_skeleton, cycle_graph, complete_graph, cube_graph, octa_graph,
                        types_of, centers_of, cover_value, brute_sign_sum, poly_brute_bypass)

N = 0
def chk(cond, msg):
    global N
    assert cond, "FAIL: " + msg
    N += 1

t0 = time.time()
def stamp(msg):
    print(f"  [{time.time()-t0:6.1f}s] {msg}  (checks so far: {N})")

# ================================================================ Def-H.27 machinery
def walk_partitions(edges):
    """All partitions of a directed edge set into walks (edge sequences, t(e_i) = s(e_{i+1}))."""
    Eall = sorted(edges)
    gidx = {e: i for i, e in enumerate(Eall)}
    if not Eall:
        yield []
        return
    def rec(unassigned, acc):
        if not unassigned:
            yield acc
            return
        E = sorted(unassigned, key=lambda e: gidx[e])
        idx = {e: i for i, e in enumerate(E)}
        def ext_forward(walk, used):
            yield walk
            head = walk[-1][1]
            for e in E:
                if idx[e] in used: continue
                if e[0] == head:
                    yield from ext_forward(walk + [e], used | {idx[e]})
        def ext_backward(walk, used):
            yield walk
            tail = walk[0][0]
            for e in E:
                if idx[e] in used: continue
                if e[1] == tail:
                    yield from ext_backward([e] + walk, used | {idx[e]})
        e0 = E[0]
        for fw in ext_forward([e0], {idx[e0]}):
            usedfw = {idx[e] for e in fw}
            for full in ext_backward(fw, usedfw):
                usedfull = {idx[e] for e in full}
                rest = [e for e in E if idx[e] not in usedfull]
                for part in rec(rest, acc + [tuple(full)]):
                    yield part
    yield from rec(list(Eall), [])

def readings_of(walk):
    """[(v, e_in, e_out)] reads of one walk: open -> interior vertices; closed -> all, cyclic
    (the Def-H.27(b) wrap read at the start vertex)."""
    k = len(walk)
    start, end = walk[0][0], walk[-1][1]
    out = []
    if start != end:
        for i in range(1, k):
            out.append((walk[i][0], walk[i - 1], walk[i]))
    else:
        for i in range(k):
            out.append((walk[i][0], walk[i - 1], walk[i]))
    return out

def all_partial_matchings(inedges, outedges):
    res = []
    def rec(i, cur, used_out):
        if i == len(inedges):
            res.append(tuple(cur)); return
        rec(i + 1, cur, used_out)
        e = inedges[i]
        for j, f in enumerate(outedges):
            if j in used_out: continue
            cur.append((e, f))
            rec(i + 1, cur, used_out | {j})
            cur.pop()
    rec(0, [], frozenset())
    return res

def parity_eval(R, readings):
    """sum_sigma w at (S1) via the exponent parity (the FT.67(2) involution mechanism)."""
    m = len(R)
    idx = {e: i for i, e in enumerate(sorted(R))}
    expo = [1] * m
    for (a, b) in readings:
        expo[idx[a]] += 1
        expo[idx[b]] += 1
    if any(x % 2 for x in expo):
        return 0
    return ((-1) ** m) * (2 ** m)

def brute_domain_sum(nv, R, domain, explicit_max=8):
    """Ground truth for Z^dom(R): explicit enumeration of D (E1) / M (E2), explicit sign sums
    for |R| <= explicit_max, exponent-parity evaluation above that (itself exhaustively
    validated in the literal domain by verify_H_virtual_bypass.py)."""
    R = sorted(R)
    m = len(R)
    t = types_of(nv, R)
    explicit = m <= explicit_max
    idx = {e: i for i, e in enumerate(R)}
    def sigma_sum(readings):
        if not explicit:
            return parity_eval(R, readings)
        P = [(idx[a], idx[b]) for (a, b) in readings]
        tot = 0
        for bits in range(1 << m):
            w = (-1) ** m
            if bin(bits).count('1') % 2: w = -w
            for (ia, ib) in P:
                sa = 1 - 2 * ((bits >> ia) & 1)
                sb = 1 - 2 * ((bits >> ib) & 1)
                if sa * sb < 0: w = -w
            tot += w
        return tot
    total = 0
    if domain == 'E1':
        for D in walk_partitions(R):
            readings = []
            for walk in D:
                readings.extend((a, b) for (v, a, b) in readings_of(walk))
            total += sigma_sum(readings)
    else:
        literal, higher = [], []
        for v in range(nv):
            if t[v] == (1, 1):
                literal.append(([e for e in R if e[1] == v][0], [e for e in R if e[0] == v][0]))
            else:
                higher.append(v)
        matchings = []
        for v in higher:
            matchings.append(all_partial_matchings([e for e in R if e[1] == v],
                                                   [e for e in R if e[0] == v]))
        for combo in (product(*matchings) if matchings else [()]):
            pairs = set(literal)
            for mm in combo:
                pairs |= set(mm)
            succ = {a: b for (a, b) in pairs}
            pred = {b: a for (a, b) in pairs}
            readings = set(pairs)
            touched = {e for pr in pairs for e in pr}
            for e1 in [e for e in touched if e not in pred]:
                walk = [e1]
                while walk[-1] in succ:
                    walk.append(succ[walk[-1]])
                ek = walk[-1]
                if ek not in succ and e1[0] == ek[1]:
                    readings.add((ek, e1))          # orbit returns to its start: wrap read
            total += sigma_sum(sorted(readings))
    return total

def count_thread_partitions(nv, edges, junction_ok=None):
    """# partitions of `edges` into open directed 2-threads (s->v->t, s != t)."""
    E = sorted(edges)
    if len(E) % 2: return 0
    out_at, in_at = {}, {}
    for e in E:
        out_at.setdefault(e[0], []).append(e)
        in_at.setdefault(e[1], []).append(e)
    used = set()
    def rec(i):
        while i < len(E) and E[i] in used: i += 1
        if i == len(E): return 1
        e = E[i]; a, b = e
        total = 0
        if junction_ok is None or junction_ok(b):
            for f in out_at.get(b, ()):
                if f in used or f[1] == a: continue
                used.add(e); used.add(f); total += rec(i + 1); used.discard(e); used.discard(f)
        if junction_ok is None or junction_ok(a):
            for g in in_at.get(a, ()):
                if g in used or g == e or g[0] == b: continue
                used.add(e); used.add(g); total += rec(i + 1); used.discard(e); used.discard(g)
        return total
    return rec(0)

def N_E1(nv, R):
    return count_thread_partitions(nv, R)

def N_E2(nv, R):
    t = types_of(nv, R)
    for (a, b) in R:                                    # condition (2a)
        if t[a] == (1, 1) and t[b] == (1, 1):
            return 0
    for v in range(nv):                                 # condition (2b)
        if t[v] != (1, 1): continue
        ie = [e for e in R if e[1] == v][0]
        oe = [e for e in R if e[0] == v][0]
        if ie[0] == oe[1]: return 0
    rest = [(a, b) for (a, b) in R if t[a] != (1, 1) and t[b] != (1, 1)]
    return count_thread_partitions(nv, rest, junction_ok=lambda v: t[v] != (1, 1))

def eps(R):
    return ((-1) ** len(R)) * (2 ** len(R))

def dom_values(nv, R):
    """(literal, E2, E1) exact amplitudes at (S1)."""
    return cover_value(nv, R), N_E2(nv, R) * eps(R), N_E1(nv, R) * eps(R)

def all_patterns(DE):
    m = len(DE)
    for bits in range(1 << m):
        yield frozenset(DE[i] for i in range(m) if (bits >> i) & 1)

def patterns_upto(DE, K):
    m = len(DE)
    for k in range(K + 1):
        for ce in combinations(range(m), k):
            yield frozenset(DE[i] for i in ce)

def locked(nv, R):
    return any(a + b >= 4 for (a, b) in types_of(nv, R))

def canon(g):
    return min(g[i:] + g[:i] for i in range(len(g)))

def directed_cycles_canon(nv, R):
    adj = {}
    for (a, b) in R: adj.setdefault(a, []).append(b)
    found = set()
    for s in range(nv):
        st = [(s, [s], {s})]
        while st:
            v, p, seen = st.pop()
            for w in adj.get(v, ()):
                if w == s and len(p) >= 2: found.add(canon(tuple(p)))
                elif w not in seen and len(p) < nv: st.append((w, p + [w], seen | {w}))
    return found

def derange(a):
    return sum((-1) ** k * factorial(a) // factorial(k) for k in range(a + 1))

# ================================================================ A. FT.74(5) battery
stamp("FT.74(5): brute force vs classifiers")
families = []
nv, DE = bidir_skeleton(2, [(0, 1)]);            families.append(("digon", nv, sorted(DE), None))
nv, DE = cycle_graph(3);                          families.append(("bidir triangle", nv, sorted(DE), None))
nv, DE = cycle_graph(4);                          families.append(("bidir P_4", nv, sorted(DE), None))
for (nn, nin, nout) in ((4, 2, 2), (5, 2, 3), (6, 3, 3)):
    nvS = 1 + nin + nout
    US = [(1 + i, 0) for i in range(nin)] + [(0, 1 + nin + j) for j in range(nout)]
    bidir_skeleton(nvS, US)
    ev = sorted([(1 + i, 0) for i in range(nin)] + [(0, 1 + nin + j) for j in range(nout)])
    families.append((f"single vertex n={nn}", nvS, ev, None))
nv, DE = complete_graph(4);                       families.append(("tetra K<=4", nv, sorted(DE), 4))

battery = 0
for (label, nvv, edges, maxK) in families:
    pats = patterns_upto(edges, maxK) if maxK is not None else all_patterns(edges)
    for R in pats:
        for dom, clf in (('E1', N_E1), ('E2', N_E2)):
            bf = brute_domain_sum(nvv, R, dom)
            pred = clf(nvv, R) * eps(R)
            chk(bf == pred, f"{label} {dom} R={sorted(R)}: brute {bf} != classifier {pred}")
            battery += 1
chk(battery == 2460, f"FT.74(5): battery size {battery} (documented 2460)")
stamp(f"battery: {battery} pattern-domain checks, zero mismatches")

# ================================================== B. FT.67(2)/Def-H.27 monomial
# w(R,sigma) = (-1)^{sum kappa} prod_{e: cov(e) even} sigma_e  -- re-derived from scratch here.
nv, DE = complete_graph(4)
mono_ok = 0
for R in all_patterns(sorted(DE)):
    m = len(R)
    if m == 0 or m > 6: continue
    t = types_of(nv, R)
    Rs = sorted(R)
    idx = {e: i for i, e in enumerate(Rs)}
    cov = {e: 0 for e in Rs}
    for v in range(nv):
        if t[v] == (1, 1):
            cov[[e for e in Rs if e[1] == v][0]] += 1
            cov[[e for e in Rs if e[0] == v][0]] += 1
    for bits in range(1 << m):
        sg = {e: (1 - 2 * ((bits >> idx[e]) & 1)) for e in Rs}
        w_def = ((-1) ** m)
        for e in Rs: w_def *= sg[e]
        aleph = 0
        for v in range(nv):
            if t[v] == (1, 1):
                ie = [e for e in Rs if e[1] == v][0]; oe = [e for e in Rs if e[0] == v][0]
                aleph += abs(sg[oe] - sg[ie]) // 2
        w_def *= (-1) ** aleph
        w_mono = (-1) ** m
        for e in Rs:
            if cov[e] % 2 == 0: w_mono *= sg[e]
        chk(w_def == w_mono, f"monomial form mismatch on R={Rs}, sigma bits={bits}")
        mono_ok += 1
chk(mono_ok > 1000, f"monomial re-derivation sample size {mono_ok}")
stamp(f"FT.67(2) corrected monomial (cov even) re-derived on {mono_ok} (pattern,sign) pairs")

# ================================================================ C. FT.74(3) order/witnesses
order_pats = 0; viol = 0; odd_supp = 0
for (nvv, DEv) in ((complete_graph(4)[0], complete_graph(4)[1]),
                   (cycle_graph(4)[0], cycle_graph(4)[1]),
                   (cycle_graph(5)[0], cycle_graph(5)[1]),
                   (cycle_graph(6)[0], cycle_graph(6)[1])):
    for R in all_patterns(sorted(DEv)):
        n1, n2 = N_E1(nvv, R), N_E2(nvv, R)
        order_pats += 1
        if n2 > n1: viol += 1
        if (n1 and len(R) % 2) or (n2 and len(R) % 2): odd_supp += 1
chk(order_pats == 9472, f"order-assertion family size {order_pats} (documented 9472)")
chk(viol == 0, f"FT.74(3): N_E2 <= N_E1 violations {viol}")
chk(odd_supp == 0, f"FT.74(3): odd |R| on classifier support {odd_supp}")
stamp(f"pointwise order N_E2 <= N_E1 and even support on {order_pats} patterns")

wit = {}
nv2, DE2 = bidir_skeleton(2, [(0, 1)])
wit['digon'] = (nv2, frozenset(DE2))
nv3, DE3 = cycle_graph(3)
wit['dir 3-cycle'] = (nv3, frozenset((i, (i + 1) % 3) for i in range(3)))
nv4, DE4 = cycle_graph(4)
wit['dir 4-cycle'] = (nv4, frozenset((i, (i + 1) % 4) for i in range(4)))
wit['double-thread hub'] = (5, frozenset({(0, 2), (1, 2), (2, 3), (2, 4)}))
wit['digon-pair hub'] = (nv3, frozenset({(0, 1), (1, 0), (0, 2), (2, 0)}))
wit['bidir P_4 floor'] = (nv4, frozenset(DE4))
expected = {'digon': (0, 0, 0), 'dir 3-cycle': (0, 0, 0), 'dir 4-cycle': (0, 0, 32),
            'double-thread hub': (0, 32, 32), 'digon-pair hub': (16, 0, 16),
            'bidir P_4 floor': (0, 1024, 1024)}
for k, (nvv, R) in wit.items():
    v = dom_values(nvv, R)
    chk(v == expected[k], f"FT.74(3) witness {k}: {v} != {expected[k]}")
    chk(brute_sign_sum(nvv, R) == v[0], f"FT.74(3) witness {k}: literal brute force")
    chk(brute_domain_sum(nvv, R, 'E2') == v[1], f"FT.74(3) witness {k}: E2 brute force")
    chk(brute_domain_sum(nvv, R, 'E1') == v[2], f"FT.74(3) witness {k}: E1 brute force")
    chk(N_E2(nvv, R) <= N_E1(nvv, R), f"FT.74(3) witness {k}: order")
stamp("FT.74(3): witness table (6 rows x 3 domains, classifier = brute force)")
# digon-pair hub types as documented
t = types_of(nv3, wit['digon-pair hub'][1])
chk(t[0] == (2, 2) and t[1] == (1, 1) and t[2] == (1, 1), f"digon-pair hub types {t}")
# the E1 revival threading of the digon-pair hub exists (two open threads)
chk(N_E1(nv3, wit['digon-pair hub'][1]) == 1, "digon-pair hub: unique E1 threading")

# ================================================================ D. FT.74(4) equality locus
eq = 0
for (nvv, DEv) in ((complete_graph(4)[0], complete_graph(4)[1]), (cycle_graph(4)[0], cycle_graph(4)[1])):
    for R in all_patterns(sorted(DEv)):
        t = types_of(nvv, R)
        if any(x == (1, 1) for x in t): continue
        chk(N_E2(nvv, R) == N_E1(nvv, R), f"FT.74(4): E2 != E1 on a type-(1,1)-free pattern {sorted(R)}")
        eq += 1
chk(eq > 500, f"equality-locus sample {eq}")
stamp(f"FT.74(4): E2 == E1 on {eq} patterns with no type-(1,1) vertex")

# ================================================================ E. FT.75(1) single vertex
for (nn, nin, nout) in ((4, 2, 2), (5, 2, 3), (6, 3, 3)):
    nvS = 1 + nin + nout
    US = [(1 + i, 0) for i in range(nin)] + [(0, 1 + nin + j) for j in range(nout)]
    _, DES = bidir_skeleton(nvS, US)
    ev = sorted([(1 + i, 0) for i in range(nin)] + [(0, 1 + nin + j) for j in range(nout)])
    tot = [0, 0, 0]; tot_lock = [0, 0, 0]
    for bits in range(1 << nn):
        R = frozenset(ev[i] for i in range(nn) if (bits >> i) & 1)
        v = dom_values(nvS, R)
        for i in range(3):
            tot[i] += v[i]
            if len(R) >= 4: tot_lock[i] += v[i]
    byp_cf = 1 + 4 * nin * nout
    lock_cf = sum(comb(nin, a) * comb(nout, a) * factorial(a) * 4 ** a
                  for a in range(2, min(nin, nout) + 1))
    chk(tot == [byp_cf, byp_cf + lock_cf, byp_cf + lock_cf], f"FT.75(1) n={nn} totals {tot}")
    chk(tot_lock == [0, lock_cf, lock_cf], f"FT.75(1) n={nn} locked sector {tot_lock}")
    chk(byp_cf == {4: 17, 5: 25, 6: 37}[nn], f"FT.75(1) n={nn} bypass closed form {byp_cf}")
    chk(lock_cf == {4: 32, 5: 96, 6: 672}[nn], f"FT.75(1) n={nn} locked closed form {lock_cf}")
    chk(tot[1] == {4: 49, 5: 121, 6: 709}[nn], f"FT.75(1) n={nn} grand total {tot[1]}")
stamp("FT.75(1): single-vertex closed forms (bypass invariant; locked revived) n=4,5,6")

# locked digon-hub derangement family
for a in (2, 3, 4, 5):
    nvv = 1 + a
    _, DEH = bidir_skeleton(nvv, [(0, 1 + i) for i in range(a)])
    RH = frozenset(DEH)
    t = types_of(nvv, RH)
    chk(t[0] == (a, a) and all(t[i] == (1, 1) for i in range(1, a + 1)), f"hub a={a} types {t}")
    chk(cover_value(nvv, RH) == 4 ** a, f"hub a={a}: literal {cover_value(nvv,RH)} != 4^{a}")
    chk(N_E2(nvv, RH) == 0, f"hub a={a}: E2 nonzero")
    chk(N_E1(nvv, RH) == derange(a), f"hub a={a}: N_E1 {N_E1(nvv,RH)} != !{a}={derange(a)}")
    chk(N_E1(nvv, RH) * eps(RH) == derange(a) * 4 ** a, f"hub a={a}: E1 value")
    if a <= 3:
        chk(brute_domain_sum(nvv, RH, 'E1') == derange(a) * 4 ** a, f"hub a={a}: E1 brute force")
        chk(brute_domain_sum(nvv, RH, 'E2') == 0, f"hub a={a}: E2 brute force")
chk([derange(a) * 4 ** a for a in (2, 3, 4, 5)] == [16, 128, 2304, 45056], "derangement values")
chk([4 ** a for a in (2, 3, 4, 5)] == [16, 64, 256, 1024], "literal hub values")
stamp("FT.75(1): locked digon-hub family 4^a / 0 / !a 4^a (a=2..5, brute force a<=3)")

# tetrahedron: the 16 locked digon-covers are the a=2 (12) and a=3 (4) instances
nv, DE = complete_graph(4)
lock_dig = []; byp_dig = []
for R in all_patterns(sorted(DE)):
    if cover_value(nv, R) == 0: continue
    if not any(len(c) == 2 for c in directed_cycles_canon(nv, R)): continue
    (lock_dig if locked(nv, R) else byp_dig).append(R)
chk(len(byp_dig) == 48 and len(lock_dig) == 16, f"digon-covers: {len(byp_dig)} byp / {len(lock_dig)} lock")
chk(all(N_E1(nv, R) == 0 and N_E2(nv, R) == 0 for R in byp_dig),
    "FT.75(4): the 48 bypass digon-covers are killed by BOTH extensions")
chk(all(N_E2(nv, R) == 0 for R in lock_dig), "FT.75(4): E2 kills all 16 locked digon-covers")
chk(all(N_E1(nv, R) != 0 for R in lock_dig), "FT.75(4): E1 keeps all 16 locked digon-covers")
vals = {}
for R in lock_dig:
    vals.setdefault(len(centers_of(nv, R)), []).append(N_E1(nv, R) * eps(R))
chk(sorted(vals) == [2, 3], f"locked digon-cover |C| values {sorted(vals)}")
chk(len(vals[2]) == 12 and set(vals[2]) == {16}, f"a=2 instances: {len(vals[2])} at {set(vals[2])}")
chk(len(vals[3]) == 4 and set(vals[3]) == {128}, f"a=3 instances: {len(vals[3])} at {set(vals[3])}")
stamp("FT.75(4): digon-cover split 48 (both dead) / 16 (E2 dead, E1 = 12x16 + 4x128)")

# ================================================================ F. FT.75(2) floors + parity
floors = {'tetra': (complete_graph(4), 32, 2 ** 17),
          'cube': (cube_graph(), 2304, 2304 * 2 ** 24),
          'octa': (octa_graph(), 72384, 72384 * 2 ** 24)}
for name, ((nvv, DEF), nexp, vexp) in floors.items():
    RF = frozenset(DEF)
    t = types_of(nvv, RF)
    chk(all(x != (1, 1) for x in t), f"{name} floor: a type-(1,1) vertex exists")
    chk(cover_value(nvv, RF) == 0, f"{name} floor: literal amplitude nonzero")
    chk(N_E1(nvv, RF) == nexp, f"{name} floor: N_E1 {N_E1(nvv,RF)} != {nexp}")
    chk(N_E2(nvv, RF) == nexp, f"{name} floor: N_E2 != N_E1 (equality locus)")
    chk(N_E1(nvv, RF) * eps(RF) == vexp, f"{name} floor: value {N_E1(nvv,RF)*eps(RF)} != {vexp}")
stamp("FT.75(2): floor revival (tetra 32 = 2^17; cube 2304*2^24; octa 72384*2^24)")

par = {}
for L in range(3, 11):
    nvv, DEL = cycle_graph(L)
    RF = frozenset(DEL)
    n1, n2 = N_E1(nvv, RF), N_E2(nvv, RF)
    pred = 4 if L % 2 == 0 else 0
    chk(n1 == pred and n2 == pred, f"P_{L} floor: N = ({n1},{n2}) != {pred}")
    chk(n1 * eps(RF) == pred * 2 ** (2 * L), f"P_{L} floor value")
    chk(cover_value(nvv, RF) == 0, f"P_{L} floor: literal amplitude nonzero")
    par[L] = n1
chk([par[L] for L in range(3, 11)] == [0, 4, 0, 4, 0, 4, 0, 4], f"parity theorem row {par}")
stamp("FT.75(2): even-L parity theorem N = 4 / 0, values 4*2^{2L}, L = 3..10")

# pure-orientation / #FF = #BB witness at L = 4 (explicit thread enumeration)
nv4, DE4 = cycle_graph(4)
R4 = frozenset(DE4)
fwd = set((i, (i + 1) % 4) for i in range(4))
threads = []
E4 = sorted(R4); used = set()
def rec4(i, acc):
    while i < len(E4) and E4[i] in used: i += 1
    if i == len(E4):
        threads.append(tuple(acc)); return
    e = E4[i]; a, b = e
    for f in [x for x in E4 if x not in used and x[0] == b and x[1] != a]:
        used.add(e); used.add(f); rec4(i + 1, acc + [(e, f)]); used.discard(e); used.discard(f)
    for g in [x for x in E4 if x not in used and x != e and x[1] == a and x[0] != b]:
        used.add(e); used.add(g); rec4(i + 1, acc + [(g, e)]); used.discard(e); used.discard(g)
rec4(0, [])
chk(len(threads) == 4 == N_E1(nv4, R4), f"P_4 floor thread partitions {len(threads)}")
mixed = 0; ff_ok = 0
for th in threads:
    ors = []
    for (ei, eo) in th:
        if (ei in fwd) != (eo in fwd): ors.append('mixed')
        else: ors.append('FF' if ei in fwd else 'BB')
    if 'mixed' in ors: mixed += 1
    elif ors.count('FF') == 2 and ors.count('BB') == 2: ff_ok += 1
chk(mixed == 0, f"P_4 floor: {mixed} mixed-orientation threads")
chk(ff_ok == 4, f"P_4 floor: #FF = #BB = L/2 in {ff_ok} of 4 partitions")
stamp("FT.75(2) Pf witness: threads pure-orientation, #FF = #BB = L/2 at L = 4")

# ================================================================ G. FT.75(3) directed cycles
rowE1 = []
for L in range(3, 11):
    nvv, DEL = cycle_graph(L)
    RC = frozenset((i, (i + 1) % L) for i in range(L))
    v = dom_values(nvv, RC)
    pred = 2 * 2 ** L if L % 2 == 0 else 0
    chk(v == (0, 0, pred), f"C_{L}: (lit,E2,E1) = {v} != (0,0,{pred})")
    rowE1.append(v[2])
chk(rowE1 == [0, 32, 0, 128, 0, 512, 0, 2048], f"directed-cycle row {rowE1}")
v = dom_values(nv2, frozenset(DE2))
chk(v == (0, 0, 0), f"digon dead in all three domains: {v}")
stamp("FT.75(3): directed C_L family L=3..10; digon dead in every domain")

# ================================================================ H. FT.75(4) triangle census
nv, DE = complete_graph(4)
tri = [R for R in all_patterns(sorted(DE)) if any(len(c) == 3 for c in directed_cycles_canon(nv, R))]
chk(len(tri) == 2397, f"tetra patterns containing a directed 3-cycle: {len(tri)} != 2397")
cnt = [0, 0, 0]; cnt_b = [0, 0, 0]
for R in tri:
    v = dom_values(nv, R)
    lk = locked(nv, R)
    for i in range(3):
        if v[i]:
            cnt[i] += 1
            if not lk: cnt_b[i] += 1
chk(cnt == [0, 833, 1025], f"triangle census nonzero (lit/E2/E1) {cnt} != [0,833,1025]")
chk(cnt_b == [0, 40, 88], f"triangle census bypass-only {cnt_b} != [0,40,88]")
Rw = frozenset({(0, 1), (0, 3), (1, 2), (2, 0)})
chk(dom_values(nv, Rw) == (0, 0, 16), f"FT.75(4) exhibit: {dom_values(nv, Rw)}")
chk(brute_domain_sum(nv, Rw, 'E1') == 16 and brute_domain_sum(nv, Rw, 'E2') == 0,
    "FT.75(4) exhibit brute force")
chk(N_E1(nv, Rw) == 1, "FT.75(4) exhibit: unique thread partition")
stamp("FT.75(4): triangle census 2397 carriers; 0/833/1025 (bypass 0/40/88); exhibit 16")

# FT.68(1)/FT.69(4) census anchors (literal domain)
cens = [0, 0, 0]; surv = [0, 0, 0]
for R in all_patterns(sorted(DE)):
    if locked(nv, R): continue
    lens = {len(c) for c in directed_cycles_canon(nv, R)}
    nz = cover_value(nv, R) != 0
    for j, L in enumerate((2, 3, 4)):
        if L in lens:
            cens[j] += 1
            if nz: surv[j] += 1
chk(cens == [501, 252, 90], f"FT.68(1) census anchors {cens}")
chk(surv == [48, 0, 0], f"FT.69(4) nonzero subcounts {surv}")
stamp("FT.68(1)/FT.69(4) anchors reproduced: 501/252/90 carriers; 48/0/0 nonzero")

# ================================================================ I. FT.75(5) skeleton totals
def skeleton_totals(nvv, DEv, label):
    tot = [[0, 0, 0], [0, 0, 0]]; cnt = [[0, 0, 0], [0, 0, 0]]
    for R in all_patterns(sorted(DEv)):
        v = dom_values(nvv, R)
        row = 1 if locked(nvv, R) else 0
        for i in range(3):
            tot[row][i] += v[i]
            if v[i]: cnt[row][i] += 1
    return dict(label=label, byp=tot[0], lock=tot[1], nz_byp=cnt[0], nz_lock=cnt[1])

doc = {
 'tetra':      dict(byp=[1057, 5921, 6881], lock=[448, 966656, 1001536], nz_byp=[85, 173, 227], nz_lock=[16, 934, 1166]),
 'bidir_P3':   dict(byp=[25, 121, 121],  lock=[48, 0, 48],      nz_byp=[7, 13, 13],   nz_lock=[3, 0, 3]),
 'bidir_P4':   dict(byp=[353, 225, 289], lock=[64, 1536, 2112], nz_byp=[29, 21, 23],  nz_lock=[4, 9, 13]),
 'bidir_P5':   dict(byp=[1161, 361, 1801], lock=[80, 5760, 8400], nz_byp=[51, 31, 61], nz_lock=[5, 30, 60]),
 'bidir_P6':   dict(byp=[3121, 3697, 7985], lock=[1632, 50944, 80224], nz_byp=[97, 79, 135], nz_lock=[21, 67, 154]),
}
graphs = {'tetra': complete_graph(4), 'bidir_P3': cycle_graph(3), 'bidir_P4': cycle_graph(4),
          'bidir_P5': cycle_graph(5), 'bidir_P6': cycle_graph(6)}
for label, g in graphs.items():
    res = skeleton_totals(g[0], g[1], label)
    for key in ('byp', 'lock', 'nz_byp', 'nz_lock'):
        chk(res[key] == doc[label][key], f"FT.75(5) {label} {key}: {res[key]} != {doc[label][key]}")
    # literal anchors inside the table
    lit_total = res['byp'][0] + res['lock'][0]
    if label == 'tetra':
        chk(lit_total == 1505, f"tetra literal Z total {lit_total} != 1505 [FT.68(1)]")
    chk(lit_total == doc[label]['byp'][0] + doc[label]['lock'][0], f"{label} literal total consistency")
chk(doc['tetra']['byp'][0] == 1057 and doc['tetra']['lock'][0] == 448
    and 1057 + 448 == 1505, "FT.68(1) literal anchors Z = 1057/448/1505")
chk(doc['bidir_P3']['lock'] == [48, 0, 48], "P_3 locked row: E2 kills, E1 keeps all 48")
stamp("FT.75(5): skeleton totals (tetra, bidir P_3..P_6) in all three domains")

# ================================================================ J. FT.75(6) norm layer
def unit_weights_E1(nvv, R):
    Rs = sorted(R); m = len(Rs); idx = {e: i for i, e in enumerate(Rs)}
    cntw = 0
    for D in walk_partitions(Rs):
        rd = []
        for wk in D: rd.extend((a, b) for (v, a, b) in readings_of(wk))
        for bits in range(1 << m):
            w = (-1) ** m
            if bin(bits).count('1') % 2: w = -w
            for (a, b) in rd:
                sa = 1 - 2 * ((bits >> idx[a]) & 1); sb = 1 - 2 * ((bits >> idx[b]) & 1)
                if sa * sb < 0: w = -w
            chk(abs(w) == 1, f"|w| != 1 for R={Rs}, D={D}, bits={bits}")
            cntw += 1
    return cntw

nw = 0
for R in all_patterns(sorted(cycle_graph(3)[1])):
    nw += unit_weights_E1(cycle_graph(3)[0], R)
chk(nw > 5000, f"unit-weight sample {nw}")
for L, m in ((3, 6), (4, 8)):
    nvv, DEL = cycle_graph(L)
    cnt = sum(2 ** bin(bits).count('1') for bits in range(1 << m))
    chk(cnt == 3 ** m, f"FT.75(6): #{{(R,sigma)}} on P_{L} = {cnt} != 3^{m}")
nvt, DEt = complete_graph(4)
cnt = sum(2 ** bin(bits).count('1') for bits in range(1 << 12))
chk(cnt == 3 ** 12 == 531441, f"FT.75(6): tetra #{{(R,sigma)}} = {cnt}")
chk(sum(comb(8, k) * 2 ** k for k in range(9)) == 3 ** 8, "binomial identity sum_k C(m,k)2^k = 3^m")
stamp(f"FT.75(6): |w| = 1 on {nw} (R,D,sigma) triples; 3^|E_dir| counts 729/6561/531441")

# ================================================================ K. FT.75(8) counting side
# admissibility (cap census) is type-level: identical in every domain by construction.
def admissible(nvv, R):
    return all(a + b <= 3 for (a, b) in types_of(nvv, R))
for label, g in (('tetra', complete_graph(4)), ('P_4', cycle_graph(4))):
    nvv, DEv = g
    cK = {}
    for R in all_patterns(sorted(DEv)):
        if admissible(nvv, R): cK[len(R)] = cK.get(len(R), 0) + 1
    if label == 'tetra':
        chk(sum(cK.values()) == 1230, f"tetra admissible configurations {sum(cK.values())} != 1230")
        chk(cK.get(4, 0) == 435, f"tetra c_4 = {cK.get(4,0)} != 435 = C(12,4) - 4*C(6,4)")
        chk(comb(12, 4) - 4 * comb(6, 4) == 435, "tetra c_4 closed form")
    if label == 'P_4':
        chk(sum(cK.values()) == 207, f"P_4 admissible patterns {sum(cK.values())} != 207")
        chk(cK.get(8, 0) == 0, "P_4 floor (|R| = 8) is locked: c_8 = 0")
        chk(poly_brute_bypass(4) == 207, "P_4 admissible count vs the independent enumerator")
# the tetra cap row of FT.68(1): (1,12,66,220,435,408,88)
nvv, DEv = complete_graph(4)
rowK = [0] * 7
for R in all_patterns(sorted(DEv)):
    if admissible(nvv, R) and len(R) <= 6: rowK[len(R)] += 1
chk(rowK == [1, 12, 66, 220, 435, 408, 88], f"FT.68(1) tetra cap row {rowK}")
chk(sum(rowK) == 1230, "cap row total 1230")
stamp("FT.75(8): counting side (cap census / admissibility) domain-blind; tetra row 1230")

# ================================================================ L. regression anchors
chk([1 + 4 * 2 * 2, 1 + 4 * 2 * 3, 1 + 4 * 3 * 3] == [17, 25, 37], "FT.67(5) bypass closed form")
nvb, DEb = bidir_skeleton(2, [(0, 1)])
chk(dom_values(nvb, frozenset(DEb)) == (0, 0, 0), "Sigma_min pattern: dead in all domains")
# literal-domain floors dead (FT.67(3a)) on all three computed solids and even polygons
for name, ((nvv, DEF), _, _) in floors.items():
    chk(cover_value(nvv, frozenset(DEF)) == 0, f"{name} floor literal death")
stamp("regression anchors: literal record reproduced")

print(f"verify_H_extdomains: {N} checks green  ({time.time()-t0:.1f}s)")
