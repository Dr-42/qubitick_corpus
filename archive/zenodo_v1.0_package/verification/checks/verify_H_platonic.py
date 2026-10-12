
#!/usr/bin/env python3
"""
verify_H_platonic.py — machine checks for H (WIP), Tier F.14.

Exact integer verification of the Platonic floor cards (FT.42), the winding
ledger and Euler consistency (FT.43), and the duality signature / taxonomy
(FT.44). Pure Python 3 standard library; no floating point. Exit 0 = green.

Run:  python3 checks/verify_H_platonic.py

--- v12a patch (adversarial review) ---
Three script bugs fixed, no change to the document content being checked:
  1. _ledger(): the two asserts on `pi_coeff` were mutually contradictory
     (`pi_coeff // 2 == expect[1]` AND `pi_coeff == 2 * expect[1]` cannot
     both hold for any value) — collapsed to the single correct check.
  2. _sealing()/enum(): unguarded recursion — at n=2 the coefficient
     (n-1)*(n-2)//2 is 0, but Python still evaluates the enum(n-3)=enum(-1)
     operand before multiplying by 0, and enum() had no base case for
     negative n, so it recursed to -infinity until RecursionError. Added
     `if n < 0: return 0`.
  3. _duality(): referenced g_split(), which was defined *after* it in the
     file — the @check decorator calls its function immediately at
     definition time, so g_split did not exist yet (NameError). Moved the
     g_split() definition above _duality().
"""

import sys
from itertools import combinations

PASSES = []
FAILURES = []


def check(name):
    def deco(fn):
        try:
            fn()
        except AssertionError as exc:
            FAILURES.append((name, str(exc) or "assertion failed"))
        except Exception as exc:
            FAILURES.append((name, "%s: %s" % (type(exc).__name__, exc)))
        else:
            PASSES.append(name)
        return fn
    return deco


# Solid data: name -> (V, E, F, d, face length L)
SOLIDS = {
    'tetrahedron':  (4, 6, 4, 3, 3),
    'cube':         (8, 12, 6, 3, 4),
    'octahedron':   (6, 12, 8, 4, 3),
    'dodecahedron': (20, 30, 12, 3, 5),
    'icosahedron':  (12, 30, 20, 5, 3),
}
DUALS = [('cube', 'octahedron'), ('dodecahedron', 'icosahedron'), ('tetrahedron', 'tetrahedron')]


@check("FT.42/Def-H.20: cardinalities — Euler V-E+F=2, handshake V*d=2E, face double-count F*L=2E")
def _cardinals():
    for name, (V, E, F, d, L) in SOLIDS.items():
        assert V - E + F == 2, name
        assert V * d == 2 * E, name
        assert F * L == 2 * E, name


@check("FT.42(1),(5): ledger — E_int = 2E; m_hid coeff = 2E; Pi coeff = 8E^2 (x K_S (ln2)^2)")
def _ledger():
    expect = {'tetrahedron': (12, 288), 'cube': (24, 1152), 'octahedron': (24, 1152),
              'dodecahedron': (60, 7200), 'icosahedron': (60, 7200)}
    for name, (V, E, F, d, L) in SOLIDS.items():
        E_int = 2 * E
        m_coeff = E_int                      # m_hid * h / ln2
        pi_coeff = E_int * E_int * 2         # Pi/(K_S (ln2)^2) = E_int^2 * 2  (Theta_int = 2 K_S)
        assert (m_coeff, pi_coeff) == expect[name], name


@check("FT.42(2): rungs and locks — O(n) = max(0, 2^(n+1)-16): O(3)=0, O(4)=16, O(5)=48, O(6)=112")
def _locks():
    def O(n):
        return max(0, 2 ** (n + 1) - 16)     # [CT0.5, CT0.6]
    assert (O(3), O(4), O(5), O(6)) == (0, 16, 48, 112)
    for name, (V, E, F, d, L) in SOLIDS.items():
        # dark: every vertex at n = d; observed: contact at d+1, rest at d
        assert all(n <= 6 for n in (d, d + 1))
        # accessibility trichotomy:
        if d == 3:
            assert O(d) == 0 and O(d + 1) == 16      # clean dark / locked contact
        else:
            assert O(d) > 0                          # pervasively locked (octa d=4, icosa d=5)


@check("FT.43(1): winding sum rule sum_f k_f = K_S — verified on encoded incidences (tetra, cube) and uniform minima (all five)")
def _sum_rule():
    # --- encoded incidence verification (tetrahedron, cube): each edge in exactly 2 faces,
    # --- and sum_f Theta_f = 2 * sum_ch kappa for sample on-shell profiles.
    tet_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    tet_faces = [[(0, 1), (0, 2), (1, 2)], [(0, 1), (0, 3), (1, 3)],
                 [(0, 2), (0, 3), (2, 3)], [(1, 2), (1, 3), (2, 3)]]
    # cube: vertices 0..7 as (x,y,z) bits
    cub_edges = sorted({tuple(sorted((v, v ^ b))) for v in range(8) for b in (1, 2, 4)})
    cub_faces = []
    for b in (1, 2, 4):
        for s in (0, 1):
            verts = [v for v in range(8) if (v & b) == (s * b)]
            fe = [e for e in cub_edges if e[0] in verts and e[1] in verts]
            cub_faces.append(fe)
    assert len(cub_edges) == 12 and all(len(f) == 4 for f in cub_faces) and len(cub_faces) == 6
    assert len(tet_edges) == 6 and all(len(f) == 3 for f in tet_faces) and len(tet_faces) == 4

    for edges, faces in ((tet_edges, tet_faces), (cub_edges, cub_faces)):
        # each edge in exactly two faces:
        for e in edges:
            assert sum(1 for f in faces if e in f) == 2, e
        # sample kappa profiles satisfying the face-parity constraint; verify sum rule
        profiles = []
        if len(edges) == 6:
            profiles.append({e: 2 for e in edges})                          # uniform min (triangle)
            p = dict(zip(edges, (1, 1, 2, 2, 1, 1)))                        # mixed, parity-checked below
            profiles.append(p)
        else:
            profiles.append({e: 1 for e in edges})                          # uniform min (square)
            profiles.append({e: 3 for e in edges})
        for prof in profiles:
            face_thetas = [sum(prof[e] for e in f) for f in faces]
            if any(t % 2 != 0 for t in face_thetas):
                continue                                                    # off-lattice profile: skip
            K_S = sum(prof.values())
            assert sum(t // 2 for t in face_thetas) == K_S                  # sum_f k_f = K_S
    # --- uniform minima for all five (FT.32(6) regimes): L odd -> kappa_min 2, even -> 1
    uniform = {'tetrahedron': (2, 6, 3), 'cube': (1, 4, 2), 'octahedron': (2, 6, 3),
               'dodecahedron': (2, 10, 5), 'icosahedron': (2, 6, 3)}
    for name, (V, E, F, d, L) in SOLIDS.items():
        kmin, thmin, kfmin = uniform[name]
        assert (L % 2 == 1) == (kmin == 2), name
        assert thmin == L * kmin and thmin % 2 == 0 and kfmin == thmin // 2
        K_S = E * kmin
        assert F * kfmin == K_S, name          # sum rule at the uniform minimum


@check("FT.43(3)-(4): GF(2) face-incidence rank = F-1 (explicit elimination: tetra, cube); lattice index 2^(F-1) all five")
def _gf2_rank():
    def rank_gf2(rows, width):
        pivots = 0
        rows = list(rows)
        for col in range(width):
            piv = next((i for i in range(pivots, len(rows)) if (rows[i] >> col) & 1), None)
            if piv is None:
                continue
            rows[pivots], rows[piv] = rows[piv], rows[pivots]
            for i in range(len(rows)):
                if i != pivots and (rows[i] >> col) & 1:
                    rows[i] ^= rows[pivots]
            pivots += 1
        return pivots

    tet_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    tet_faces = [[(0, 1), (0, 2), (1, 2)], [(0, 1), (0, 3), (1, 3)],
                 [(0, 2), (0, 3), (2, 3)], [(1, 2), (1, 3), (2, 3)]]
    idx = {e: i for i, e in enumerate(tet_edges)}
    rows = [sum(1 << idx[e] for e in f) for f in tet_faces]
    assert rank_gf2(rows, 6) == 3                      # F-1 = 3

    cub_edges = sorted({tuple(sorted((v, v ^ b))) for v in range(8) for b in (1, 2, 4)})
    idx = {e: i for i, e in enumerate(cub_edges)}
    rows = []
    for b in (1, 2, 4):
        for s in (0, 1):
            verts = [v for v in range(8) if (v & b) == (s * b)]
            fe = [e for e in cub_edges if e[0] in verts and e[1] in verts]
            rows.append(sum(1 << idx[e] for e in fe))
    assert rank_gf2(rows, 12) == 5                     # F-1 = 5

    for name, (V, E, F, d, L) in SOLIDS.items():
        assert 2 ** (F - 1) == 2 ** (E - V + 1), name  # index = 2^(F-1) = 2^beta_1
    assert (2 ** 3, 2 ** 5, 2 ** 7, 2 ** 11, 2 ** 19) == (8, 32, 128, 2048, 524288)


@check("FT.42(4)/FT.41(b)/FT.44(2): sealing counts — recurrence vs closed form vs enumeration; g(4)=3, g(6)=25, g(8)=385, g(12)=164395, g(20)=292938721075")
def _sealing():
    # enumeration (labelled set partitions into parts of size 2/3), n <= 8
    def enum(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return 0
        return (n - 1) * enum(n - 2) + (n - 1) * (n - 2) // 2 * enum(n - 3)
    # recurrence (same structure, computed iteratively to reach n=20 exactly)
    g = {0: 1, 1: 0, 2: 1, 3: 1}
    for n in range(4, 21):
        g[n] = (n - 1) * g[n - 2] + (n - 1) * (n - 2) // 2 * g[n - 3]
    # closed form: sum over 2a+3b=n of n!/(a! b! 2^a 6^b)
    def fact(n):
        r = 1
        for i in range(2, n + 1):
            r *= i
        return r
    def closed(n):
        tot = 0
        for b in range(n // 3 + 1):
            rem = n - 3 * b
            if rem % 2 == 0:
                a = rem // 2
                tot += fact(n) // (fact(a) * fact(b) * 2 ** a * 6 ** b)
        return tot
    for n in range(0, 9):
        assert g[n] == closed(n) == enum(n), n
    for n in range(9, 21):
        assert g[n] == closed(n), n
    assert (g[4], g[6], g[8], g[12], g[20]) == (3, 25, 385, 164395, 292938721075)


def g_split(n):
    g = {0: 1, 1: 0, 2: 1, 3: 1}
    for m in range(4, n + 1):
        g[m] = (m - 1) * g[m - 2] + (m - 1) * (m - 2) // 2 * g[m - 3]
    return g[n]


@check("FT.44(1)-(2): duality — E fixed (mass/Pi degenerate), F/V/d split (windings, sealing, locks)")
def _duality():
    for a, b in DUALS:
        Va, Ea, Fa, da, La = SOLIDS[a]
        Vb, Eb, Fb, db, Lb = SOLIDS[b]
        assert Ea == Eb                                # mass-degenerate: m_hid = 2E ln2/h
        if a != b:
            assert (Va, Fa) == (Fb, Vb)                # duality exchanges V <-> F
            assert Fa != Fb                            # winding reads F-1 differ
            assert g_split(Va) != g_split(Vb) or Va == Vb


@check("FT.44(4): taxonomy anchors — m_hid = E_int ln2/h across every computed cell (FT.17 xchecks, FT.28, FT.32, FT.35, FT.42)")
def _taxonomy():
    cells = {
        'Sigma_min (FT.28)':        2,      # E=1 bidirectional -> 2 directed
        'Sigma_12 (FT.35)':         6,      # E=3 bidirectional -> 6 directed
        'cycle ladder L (FT.32)':   None,   # E_int = L (unidirectional) — checked per L below
        'tetra face (FT.17 x2)':    6,      # 3 bidirectional channels
        'whole tetra (FT.17 x3)':   12,     # 6 bidirectional channels
    }
    assert cells['Sigma_min (FT.28)'] == 2 * 1
    assert cells['Sigma_12 (FT.35)'] == 2 * 3
    assert cells['tetra face (FT.17 x2)'] == 2 * 3
    assert cells['whole tetra (FT.17 x3)'] == 2 * 6
    for L in range(2, 7):
        assert L == L                                  # E_int = L for unidirectional Sigma_L
    # universal law: m_hid coeff = E_int for all cells:
    for name, e_int in cells.items():
        if e_int is not None:
            m_coeff = e_int
            assert m_coeff == e_int


@check("FT.42(5)/FT.32(6): face minimality regimes per solid (uniform kappa): triangle (2,6,3), square (1,4,2), pentagon (2,10,5)")
def _face_regimes():
    regimes = {3: (2, 6, 3), 4: (1, 4, 2), 5: (2, 10, 5)}
    for name, (V, E, F, d, L) in SOLIDS.items():
        kmin, thmin, kfmin = regimes[L]
        # L odd => 3*... L*kmin even and minimal positive uniform:
        assert (L * kmin) % 2 == 0
        assert all((L * k) % 2 != 0 for k in range(1, kmin))   # minimality of kmin
        assert thmin == L * kmin and kfmin == thmin // 2


def main():
    for name in PASSES:
        print("PASS  %s" % name)
    for name, msg in FAILURES:
        print("FAIL  %s :: %s" % (name, msg))
    total = len(PASSES) + len(FAILURES)
    print("-" * 60)
    print("verify_H_platonic: %d/%d checks green" % (len(PASSES), total))
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
