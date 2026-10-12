"""bypasscore.py — exact model core (shared by the bypass suites) for Def-H.25 / FT.67 / FT.68,
cover-counting DP, cap-DP, transfer matrices, Burnside helpers. Exact ints/Fractions only.

Literal (S2) domain, scopes (S1)-(S4):
  pattern R subset of directed edges; type(v) = (in_R, out_R) [D0.8];
  center := type (1,1) [D3.3 literal domain];
  w(R,sigma) = prod_e(-sigma_e) * prod_{centers}(-1)^{|f_v|}, f_v = (s_out - s_in)/2;
  FT.67(2): sum_sigma w = 2^{|R|}(-1)^{sum kappa} iff cov(e)=1 for all e in R, else 0.
Cover = (center set C, per center its forced in/out read) with:
  * every edge of R claimed (read) exactly once, R = claimed set;
  * non-center type != (1,1); center type == (1,1) (automatic);
  * an edge between two centers is never claimed (cov=2) => virtual.
"""
from fractions import Fraction as Fr
from itertools import combinations

# ---------------------------------------------------------------- skeletons
def bidir_skeleton(nv, undirected_edges):
    de = []
    for (a, b) in undirected_edges:
        de.append((a, b)); de.append((b, a))
    de.sort()
    return nv, de

def cycle_graph(n):
    return bidir_skeleton(n, [(i, (i + 1) % n) for i in range(n)])

def complete_graph(n):
    return bidir_skeleton(n, list(combinations(range(n), 2)))

def cube_edges():
    V = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    return [(i, j) for i in range(8) for j in range(i + 1, 8)
            if sum(x != y for x, y in zip(V[i], V[j])) == 1]

def cube_graph():
    return bidir_skeleton(8, cube_edges())

def octa_edges():
    V = []
    for ax in range(3):
        for s in (-1, 1):
            v = [0, 0, 0]; v[ax] = s; V.append(tuple(v))
    return [(i, j) for i in range(6) for j in range(i + 1, 6)
            if V[i] != tuple(-x for x in V[j])]

def octa_graph():
    return bidir_skeleton(6, octa_edges())

def icosa_edges():
    def mul(x, y):
        a, b = x; c, d = y
        return (a * c + b * d, a * d + b * c + b * d)
    def add(x, y): return (x[0] + y[0], x[1] + y[1])
    def sub(x, y): return (x[0] - y[0], x[1] - y[1])
    PH = (0, 1); ONE = (1, 0); ZERO = (0, 0); MONE = (-1, 0)
    verts = []
    for s1 in (ONE, MONE):
        for s2 in (ONE, MONE):
            verts.append((ZERO, s1, mul(s2, PH)))
            verts.append((s1, mul(s2, PH), ZERO))
            verts.append((mul(s2, PH), ZERO, s1))
    assert len(verts) == 12
    def d2(u, v):
        s = ZERO
        for a, b in zip(u, v):
            dd = sub(a, b); s = add(s, mul(dd, dd))
        return s
    FOUR = (4, 0)
    E = [(i, j) for i in range(12) for j in range(i + 1, 12) if d2(verts[i], verts[j]) == FOUR]
    assert len(E) == 30
    return E

def icosa_graph():
    return bidir_skeleton(12, icosa_edges())

def dodeca_edges():
    ic = icosa_edges()
    adj = [set() for _ in range(12)]
    for a, b in ic:
        adj[a].add(b); adj[b].add(a)
    faces = [(a, b, c) for a in range(12) for b in sorted(adj[a]) for c in sorted(adj[b])
             if c in adj[a] and a < b < c]
    assert len(faces) == 20
    E = []
    for i in range(20):
        for j in range(i + 1, 20):
            if len(set(faces[i]) & set(faces[j])) == 2:
                E.append((i, j))
    assert len(E) == 30
    deg = [0] * 20
    for a, b in E:
        deg[a] += 1; deg[b] += 1
    assert all(d == 3 for d in deg)
    return E

def dodeca_graph():
    return bidir_skeleton(20, dodeca_edges())

# ---------------------------------------------------------------- graph helpers
def undirected_from(nv, dir_edges):
    s = set()
    for (a, b) in dir_edges:
        s.add((min(a, b), max(a, b)))
    return sorted(s)

def elim_order(nv, undirected):
    """greedy min-degree elimination order (small frontier)."""
    nbrs = [set() for _ in range(nv)]
    for a, b in undirected:
        nbrs[a].add(b); nbrs[b].add(a)
    remaining = set(range(nv))
    order = []
    while remaining:
        v = min(remaining, key=lambda u: (len(nbrs[u] & remaining), u))
        order.append(v); remaining.discard(v)
    return order

# ---------------------------------------------------------------- pattern primitives
def types_of(nv, R):
    t = [[0, 0] for _ in range(nv)]
    for (a, b) in R:
        t[a][1] += 1
        t[b][0] += 1
    return [tuple(x) for x in t]

def centers_of(nv, R):
    t = types_of(nv, R)
    C = {}
    for v in range(nv):
        if t[v] == (1, 1):
            C[v] = ([e for e in R if e[1] == v][0], [e for e in R if e[0] == v][0])
    return C

def is_cover(nv, R):
    C = centers_of(nv, R)
    cov = {e: 0 for e in R}
    for v, (ie, oe) in C.items():
        cov[ie] += 1; cov[oe] += 1
    return len(R) > 0 and all(c == 1 for c in cov.values()) or (len(R) == 0)

def is_cover_strict(nv, R):
    """cover including the vacuum (|C|=0, value 1)."""
    C = centers_of(nv, R)
    if not R:
        return True
    cov = {e: 0 for e in R}
    for v, (ie, oe) in C.items():
        cov[ie] += 1; cov[oe] += 1
    return all(c == 1 for c in cov.values())

def cover_value(nv, R):
    return ((-1) ** len(R)) * (2 ** len(R)) if is_cover_strict(nv, R) else 0

def brute_sign_sum(nv, R):
    """Ground truth from the definitions (D3.3 f_v / A8 G(e) at kappa=1); no FT.67 use."""
    R = sorted(R)
    m = len(R)
    t = types_of(nv, R)
    idx = {e: i for i, e in enumerate(R)}
    ctr = []
    for v in range(nv):
        if t[v] == (1, 1):
            ctr.append((idx[[e for e in R if e[1] == v][0]], idx[[e for e in R if e[0] == v][0]]))
    total = 0
    for bits in range(1 << m):
        w = (-1) ** m
        nb = 0
        for i in range(m):
            if (bits >> i) & 1:
                nb += 1
        if nb % 2: w = -w
        aleph = 0
        for (ii, io) in ctr:
            s_in = 1 - 2 * ((bits >> ii) & 1)
            s_out = 1 - 2 * ((bits >> io) & 1)
            aleph += abs(s_out - s_in) // 2
        if aleph % 2: w = -w
        total += w
    return total

# ---------------------------------------------------------------- cover enumeration (backtracking)
def enum_covers_bt(nv, undirected):
    """Enumerate literal-domain covers. Returns list of (claims, R)."""
    nbrs = [set() for _ in range(nv)]
    for a, b in undirected:
        nbrs[a].add(b); nbrs[b].add(a)
    order = elim_order(nv, undirected)
    pos = {v: i for i, v in enumerate(order)}
    inE = [[] for _ in range(nv)]
    outE = [[] for _ in range(nv)]
    for (a, b) in undirected:
        inE[b].append((a, b)); outE[a].append((a, b))
        inE[a].append((b, a)); outE[b].append((b, a))
    claimed = {}
    role = {}
    covers = []

    def finalize_ok(u):
        i = sum(1 for e in inE[u] if e in claimed)
        o = sum(1 for e in outE[u] if e in claimed)
        if role[u] == 1:
            return (i, o) == (1, 1)
        return (i, o) != (1, 1)

    def rec(k):
        if k == nv:
            R = frozenset(claimed)
            covers.append((dict(claims), R))
            return
        v = order[k]
        completed_now = [u for u in order[:k] if u not in done and nbrs[u] <= set(order[:k + 1])]
        # option A: non-center
        role[v] = 0
        ok = all(finalize_ok(u) for u in completed_now + ([v] if nbrs[v] <= set(order[:k+1]) else []))
        if ok:
            if v in completed_now or nbrs[v] <= set(order[:k + 1]): done.add(v)
            dd = set(done)
            rec(k + 1)
            done.clear(); done.update(dd)
        del role[v]
        # option B: center with claims
        for ie in inE[v]:
            if ie in claimed: continue
            for oe in outE[v]:
                if oe in claimed or oe == ie: continue
                claimed[ie] = v; claimed[oe] = v
                claims[v] = (ie, oe); role[v] = 1
                ok = all(finalize_ok(u) for u in completed_now + ([v] if nbrs[v] <= set(order[:k+1]) else []))
                if ok:
                    if nbrs[v] <= set(order[:k + 1]): done.add(v)
                    dd = set(done)
                    rec(k + 1)
                    done.clear(); done.update(dd)
                del role[v]; del claims[v]
                del claimed[ie]; del claimed[oe]
    claims = {}
    done = set()
    rec(0)
    # independent post-filter
    good = []
    for cl, R in covers:
        t = types_of(nv, R)
        ok = True
        cnt = {e: 0 for e in R}
        for v, (ie, oe) in cl.items():
            cnt[ie] += 1; cnt[oe] += 1
        for v in range(nv):
            if v in cl:
                if t[v] != (1, 1): ok = False; break
            else:
                if t[v] == (1, 1): ok = False; break
        if ok and any(c != 1 for c in cnt.values()): ok = False
        if ok: good.append((cl, R))
    return good

def cover_polys_bt(nv, undirected):
    cov = enum_covers_bt(nv, undirected)
    pb = {}; pl = {}
    for cl, R in cov:
        t = types_of(nv, R)
        locked = any(a + b >= 4 for (a, b) in t)
        d = pl if locked else pb
        d[len(cl)] = d.get(len(cl), 0) + 1
    return pb, pl, cov

# ---------------------------------------------------------------- cover DP (counting, no enumeration)
def cover_dp(nv, undirected):
    """Exact counting of literal-domain covers by vertex-introduction DP.
    Returns (poly_byp, poly_lock): dict |C| -> count, split by lock status.
    Independent algorithm vs enum_covers_bt (cross-check target)."""
    nbrs = [set() for _ in range(nv)]
    for a, b in undirected:
        nbrs[a].add(b); nbrs[b].add(a)
    order = elim_order(nv, undirected)
    pos = {v: i for i, v in enumerate(order)}
    inE = [[] for _ in range(nv)]
    outE = [[] for _ in range(nv)]
    for (a, b) in undirected:
        inE[b].append((a, b)); outE[a].append((a, b))
        inE[a].append((b, a)); outE[b].append((b, a))
    # split at introduction
    pinE = [[e for e in inE[v] if pos[e[0]] < pos[v]] for v in range(nv)]
    finE = [[e for e in inE[v] if pos[e[0]] > pos[v]] for v in range(nv)]
    poutE = [[e for e in outE[v] if pos[e[1]] < pos[v]] for v in range(nv)]
    foutE = [[e for e in outE[v] if pos[e[1]] > pos[v]] for v in range(nv)]

    # active vertex entry: (v, role, pcin, pcout, inR, outR)
    #   role 1 (center): pcin bitmask over finE[v] (the claimed future in-edge, if future),
    #     pcout over foutE[v]; inR=outR=1 always.
    #   role 0: pcin=pcout=0; inR/outR = #R-edges at v resolved so far.
    def step(k, act, nC, lock, memo):
        if k == nv:
            assert not act
            return {(nC, lock): 1}
        key = (k, act, nC, lock)
        if key in memo: return memo[key]
        w = order[k]
        amap = {a[0]: a for a in act}
        # past-edge statuses
        pin_status = []   # (edge, claimed_by_tail)
        for e in pinE[w]:
            u = e[0]; st = amap.get(u)
            assert st is not None
            if st[1] == 1:
                cl = bool((st[3] >> foutE[u].index(e)) & 1)
            else:
                cl = False
            pin_status.append((e, cl, st[1]))
        pout_status = []
        for e in poutE[w]:
            u = e[1]; st = amap.get(u)
            assert st is not None
            if st[1] == 1:
                cl = bool((st[2] >> finE[u].index(e)) & 1)
            else:
                cl = False
            pout_status.append((e, cl, st[1]))
        any_claimed_past = any(cl for (_, cl, _) in pin_status + pout_status)
        res = {}
        def merge(d2):
            for kk, vv in d2.items():
                res[kk] = res.get(kk, 0) + vv
        # finalize helper: apply updates, complete vertices, recurse
        def proceed(newact_updates, w_entry, nC2, extra_lock=0):
            # newact_updates: dict v -> (din, dout) increments for active NC vertices
            newact = []
            lock2 = lock | extra_lock
            ok = True
            for a in act:
                v, r, pi, po, iR, oR = a
                din, dout = newact_updates.get(v, (0, 0))
                iR += din; oR += dout
                if nbrs[v] <= set(order[:k + 1]):
                    # v completes now
                    if r == 1:
                        if (iR, oR) != (1, 1): ok = False; break
                    else:
                        if (iR, oR) == (1, 1): ok = False; break
                        if iR + oR >= 4: lock2 = 1
                else:
                    newact.append((v, r, pi, po, iR, oR))
            if not ok: return
            # w completion / entry
            if w_entry is not None:
                v, r, pi, po, iR, oR = w_entry
                if nbrs[w] <= set(order[:k + 1]):
                    if r == 1:
                        if (iR, oR) != (1, 1): return
                    else:
                        if (iR, oR) == (1, 1): return
                        if iR + oR >= 4: lock2 = 1
                else:
                    newact.append(w_entry)
            newact.sort(key=lambda a: pos[a[0]])
            merge(step(k + 1, tuple(newact), nC2, lock2, memo))
        # option NC
        iR = sum(1 for (_, cl, _) in pin_status if cl)
        oR = sum(1 for (_, cl, _) in pout_status if cl)
        proceed({}, (w, 0, 0, 0, iR, oR), nC)
        # option C: requires no past edge at w claimed; choices from NC-past edges or future
        if not any_claimed_past:
            in_choices = ([('p', e) for (e, cl, r) in pin_status if r == 0]
                          + [('f', e) for e in finE[w]])
            out_choices = ([('p', e) for (e, cl, r) in pout_status if r == 0]
                           + [('f', e) for e in foutE[w]])
            for (ti, ie) in in_choices:
                for (to, oe) in out_choices:
                    pcin = 0; pcout = 0
                    if ti == 'f': pcin = 1 << finE[w].index(ie)
                    if to == 'f': pcout = 1 << foutE[w].index(oe)
                    upd = {}
                    if ti == 'p':
                        u = ie[0]; upd[u] = (0, 1)      # u's out-edge entered R
                    if to == 'p':
                        u = oe[1]
                        din, dout = upd.get(u, (0, 0))
                        upd[u] = (din + 1, dout)        # u's in-edge entered R
                    proceed(upd, (w, 1, pcin, pcout, 1, 1), nC + 1)
        memo[key] = res
        return res
    memo = {}
    out = step(0, tuple(), 0, 0, memo)
    pb = {}; pl = {}
    for (nC, lock), c in out.items():
        d = pl if lock else pb
        d[nC] = d.get(nC, 0) + c
    return pb, pl

# ---------------------------------------------------------------- cap DP (admissible patterns by K)
def cap_dp_by_K(nv, undirected, cap=3):
    """Count patterns R with k_v <= cap for every v, by K=|R|. Exact DP."""
    nbrs = [set() for _ in range(nv)]
    for a, b in undirected:
        nbrs[a].add(b); nbrs[b].add(a)
    order = elim_order(nv, undirected)
    pos = {v: i for i, v in enumerate(order)}
    # state: active degrees tuple (over active verts sorted by pos) ; value: dict K -> count
    states = {(tuple(),): {0: 1}}
    states = {tuple(): {0: 1}}
    for k in range(nv):
        w = order[k]
        past = [u for u in nbrs[w] if pos[u] < pos[w]]
        nxt = {}
        for act_key, kdist in states.items():
            # act_key: degrees of active vertices (those introduced, not completed)
            # we need the vertex list aligned with act_key: recompute active set at step k
            active = [v for v in order[:k] if not (nbrs[v] <= set(order[:k]))]
            # (all active have a future neighbour; w's past neighbours are all active)
            amap = {v: act_key[i] for i, v in enumerate(active)}
            for mask in range(1 << (2 * len(past))):
                # decide presence of both orientations for each past neighbour
                ok = True
                dinc = {}
                kk = 0
                deg_w = 0
                for pi, u in enumerate(past):
                    b1 = (mask >> (2 * pi)) & 1        # (u->w) present
                    b2 = (mask >> (2 * pi + 1)) & 1    # (w->u) present
                    if b1:
                        dinc[u] = dinc.get(u, 0) + 1
                        deg_w += 1; kk += 1
                    if b2:
                        dinc[u] = dinc.get(u, 0) + 1
                        deg_w += 1; kk += 1
                if deg_w > cap: continue
                newact = []
                newdegs = {}
                for v in active:
                    d = amap[v] + dinc.get(v, 0)
                    if d > cap: ok = False; break
                    if nbrs[v] <= set(order[:k + 1]):
                        pass  # completes now; degree final (<= cap checked)
                    else:
                        newdegs[v] = d
                if not ok: continue
                # w: completes now iff no future neighbours
                if nbrs[w] <= set(order[:k + 1]):
                    pass
                else:
                    newdegs[w] = deg_w
                newlist = sorted(newdegs.items(), key=lambda t: pos[t[0]])
                key2 = tuple(d for (_, d) in newlist)
                # must also carry which vertices: implied by step k+1's active set -> recompute
                # there; key2 alone is ambiguous unless vertex set is a function of k. It is:
                # active set at step k+1 = [v in order[:k+1] : nbrs(v) not subset order[:k+1]]
                d2 = nxt.get(key2, {})
                for K0, c in kdist.items():
                    d2[K0 + kk] = d2.get(K0 + kk, 0) + c
                nxt[key2] = d2
        states = nxt
    total = {}
    for key, kdist in states.items():
        for K, c in kdist.items():
            total[K] = total.get(K, 0) + c
    mx = max(total) if total else 0
    return [total.get(K, 0) for K in range(mx + 1)]

# ---------------------------------------------------------------- polygon transfer matrix
def poly_T(t=1):
    T = [[0] * 4 for _ in range(4)]
    for s in range(4):
        for sp in range(4):
            if bin(s).count('1') + bin(sp).count('1') <= 3:
                T[s][sp] = (t ** bin(sp).count('1'))
    return T

def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][t] * B[t][j] for t in range(n)) for j in range(n)] for i in range(n)]

def poly_B(n, t=1):
    T = poly_T(t)
    M = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    for _ in range(n):
        M = mat_mul(M, T)
    return sum(M[i][i] for i in range(4))

def poly_B_coeffs(n):
    """B_{P_n}(t) coefficient list (exact ints): B = tr T(t)^n."""
    def mk():
        T = [[None] * 4 for _ in range(4)]
        for s in range(4):
            for sp in range(4):
                if bin(s).count('1') + bin(sp).count('1') <= 3:
                    p = [0, 0, 0]
                    p[bin(sp).count('1')] = 1
                    T[s][sp] = p
        return T
    def pmul(A, B):
        C = [[None] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                acc = [0] * (2 * n + 1)
                for t in range(4):
                    if A[i][t] is None or B[t][j] is None: continue
                    for da, a in enumerate(A[i][t]):
                        if a == 0: continue
                        for db, b in enumerate(B[t][j]):
                            if b: acc[da + db] += a * b
                C[i][j] = acc
        return C
    T = mk()
    M = [[([1] + [0] * (2 * n)) if i == j else None for j in range(4)] for i in range(4)]
    for _ in range(n):
        M = pmul(M, T)
    tr = [0] * (2 * n + 1)
    for i in range(4):
        for d, c in enumerate(M[i][i]):
            tr[d] += c
    while len(tr) > 1 and tr[-1] == 0: tr.pop()
    return tr

def poly_brute_bypass(n):
    """exhaustive: admissible patterns on bidirectional C_n (all k_v<=3), n small."""
    cnt = 0
    for assign in range(4 ** n):
        s = [(assign >> (2 * i)) & 3 for i in range(n)]
        ok = True
        for i in range(n):
            if bin(s[i]).count('1') + bin(s[(i - 1) % n]).count('1') > 3:
                ok = False; break
        if ok: cnt += 1
    return cnt

# ---------------------------------------------------------------- Burnside helpers
def automorphisms(nv, undirected):
    adj = [set() for _ in range(nv)]
    for a, b in undirected:
        adj[a].add(b); adj[b].add(a)
    order = sorted(range(nv), key=lambda v: (-len(adj[v]), v))
    res = []
    mapping = {}
    def rec(k):
        if k == len(order):
            res.append(tuple(mapping[v] for v in range(nv))); return
        v = order[k]
        img = set(range(nv)) - set(mapping.values())
        for u in order[:k]:
            w = mapping[u]
            if u in adj[v]: img &= adj[w]
            else: img -= adj[w]
        for w in sorted(img):
            mapping[v] = w
            rec(k + 1)
            del mapping[v]
    rec(0)
    return res

def dir_edge_orbits(perm, undirected):
    de = []
    for (a, b) in undirected:
        de.append((a, b)); de.append((b, a))
    img = {(a, b): (perm[a], perm[b]) for (a, b) in de}
    seen = set(); orbits = []
    for e in sorted(de):
        if e in seen: continue
        orb = []; x = e
        while x not in seen:
            seen.add(x); orb.append(x); x = img[x]
        orbits.append(tuple(orb))
    return orbits

def fix_capped_by_K(nv, undirected, perm, cap=3):
    """#admissible (k_v<=cap) patterns fixed by perm, by K. Orbits-subset enumeration."""
    orbs = dir_edge_orbits(perm, undirected)
    res = {}
    for mask in range(1 << len(orbs)):
        deg = [0] * nv
        K = 0; ok = True
        for oi in range(len(orbs)):
            if (mask >> oi) & 1:
                for (a, b) in orbs[oi]:
                    deg[a] += 1; deg[b] += 1; K += 1
                    if deg[a] > cap or deg[b] > cap: ok = False; break
                if not ok: break
        if ok: res[K] = res.get(K, 0) + 1
    return res
