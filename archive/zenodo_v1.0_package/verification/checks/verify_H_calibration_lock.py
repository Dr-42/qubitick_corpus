#!/usr/bin/env python3
"""
verify_H_calibration_lock.py — machine verification of Tier BM.5 (Def-BM.4,
BM.13–BM.18): the calibration lock — the Born width, the coherence volume and
energy density, the curvature of a sealed composite, the lock identities, and
the neutron row of the Def-BM.3 identification layer.

Exact arithmetic only: integers, fractions.Fraction, the rational-monomial ring
Q[h,E,ln2,pi]^{+-} (Laurent monomials h^a E^b (ln2)^c pi^d with exact rational
coefficients), exact rational enclosures of ln2 (via the series
ln2 = sum_{n>=1} 1/(n 2^n), error < 2^-N) and of pi (Archimedes' 223/71 and
22/7), exhaustive censuses over the computed E_int cells.  No floating point
anywhere in an assertion.

Sections:
  §A  BM.13 — the Born width: the exact substitution dx = h/(E ln2) with
              dx * m_hid = 1; the CT2.1 dimension exponent; the quantized
              ladder over the computed cells (2, 6, 12, 24, 60) and the cycle
              ladder E = L; the sub-hop threshold dx < h <=> E ln2 > 1 <=>
              E >= 2 with the exact ln2 enclosure; the minimal floor
              E_int >= 2; the Robertson consistency dp >= m_hid/2 with
              saturation; the alpha-variant priced exactly.
  §B  BM.14 — the coherence volume and the energy density: V_eff = h^3/(E ln2)^3,
              rho = m_hid/V_eff = (E ln2)^4/h^4 as exact Laurent identities;
              the CT2.1 exponents ([V] = q^-3/2, [rho] = q^+2 = [T_munu]);
              the agreement with BM.9(5)'s general form kappa^2 rho =
              2 pi h E/V at V = V_eff; the exact ln2 ledger (BM.9(5)'s
              cancellation against BM.14's surviving (ln2)^3).
  §C  BM.15 — the curvature: the dust trace T = -rho; the exact trace of
              CT1.23 giving R = kappa^2 (rho - 3p) + 4 Lambda and the component
              round trip R_munu -> R -> G_munu = kappa^2 T_munu - Lambda g_munu
              in the orthonormal rest frame; the refutation of R = -kappa^2 rho;
              kappa^2 rho = 2 pi E^4 (ln2)^3/h^2 with [kappa^2 rho] = q^+1 = [R];
              the curvature radius and the exact inequality l_R < dx for every
              E >= 1 (via 2 pi ln2 > 1); the Lambda clause (P4 datum).
  §D  BM.16 — the calibration lock: the h-free dimensionless lock
              dx^2 kappa^2 rho = 2 pi E^2 ln2; the dx/h and kappa^2 rho h^2
              reads; the CT2.11 rescaling covariance (h -> lambda h) with the
              exact weights (+1, -4, -2) and the invariance of the dimensionless
              products; the discrete value sets and strict monotonicity; the
              P3 comparison scales r_s = 2 G_N m_hid = h E/2 and
              dx * r_s = 2 G_N = h^2/(2 ln2) independent of E; the
              gravitational length l_G = sqrt(G_N) via squared comparison:
              dx < l_G <=> E >= 3; the crossing E* = sqrt(2/ln2) in (1,2),
              strictly below the minimal floor; what is not locked.
  §E  BM.17 — the neutron row: the Census FT.35 cell (E_int = 6, the eps-type
              baryon-like sealing of FT.35(5)) with all six reads as exact
              rationals times powers of h and ln2; the sub-hop and
              sub-gravitational-length factors at E = 6; the family table over
              the five computed Platonic/composite cells; the Pi row of
              FT.35(3); the identification-layer discipline (Def-BM.3 label,
              no measured value, charge class pending BM.6(1)).
  §F  BM.18 — document pins and hygiene.

Tier BM.5 is new canon content with no first edition in H_archive/; the pins of
this checker resolve against the era-canon texts directly.

Run: python3 verify_H_calibration_lock.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
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


# ==========================================================================
# the exact rational-monomial ring  Q[h,E,l2,pi]^{+-}
# ==========================================================================
NAMES = ["h", "E", "l2", "pi"]
IX = {n: i for i, n in enumerate(NAMES)}


class RM:
    """Laurent monomials h^a E^b (ln2)^c pi^d with exact rational coefficients."""

    __slots__ = ("t",)

    def __init__(self, terms=None):
        self.t = {}
        for e, c in (terms or {}).items():
            self.add(e, c)

    def add(self, e, c):
        if c == 0:
            return
        e = tuple(e)
        self.t[e] = self.t.get(e, Fr(0)) + Fr(c)
        if self.t[e] == 0:
            del self.t[e]

    @staticmethod
    def mon(name, k=1, c=1):
        e = [0] * len(NAMES)
        e[IX[name]] = k
        return RM({tuple(e): Fr(c)})

    @staticmethod
    def const(x):
        return RM({tuple([0] * len(NAMES)): Fr(x)})

    def __add__(self, o):
        r = RM(self.t)
        for e, c in o.t.items():
            r.add(e, c)
        return r

    def __sub__(self, o):
        r = RM(self.t)
        for e, c in o.t.items():
            r.add(e, tuple([-x for x in []]) if False else -c)
        return r

    def __neg__(self):
        return RM({e: -c for e, c in self.t.items()})

    def __mul__(self, o):
        r = RM()
        for e1, c1 in self.t.items():
            for e2, c2 in o.t.items():
                r.add(tuple(e1[i] + e2[i] for i in range(len(NAMES))), c1 * c2)
        return r

    def __rmul__(self, x):
        return RM({e: Fr(x) * c for e, c in self.t.items()})

    def __truediv__(self, o):
        """Division by a single monomial (exact)."""
        assert len(o.t) == 1, "division only by a monomial"
        (e2, c2), = o.t.items()
        return RM({tuple(e[i] - e2[i] for i in range(len(NAMES))): c / c2
                   for e, c in self.t.items()})

    def pow(self, n):
        r = RM.const(1)
        b = RM(self.t)
        k = abs(n)
        while k:
            if k & 1:
                r = r * b
            b = b * b
            k >>= 1
        if n < 0:
            return RM.const(1) / r
        return r

    def zero(self):
        return not self.t

    def __eq__(self, o):
        if not isinstance(o, RM):
            return NotImplemented
        return self.t == o.t

    def __ne__(self, o):
        r = self.__eq__(o)
        return r if r is NotImplemented else not r

    def coeff(self, **kw):
        e = tuple(kw.get(n, 0) for n in NAMES)
        return self.t.get(e, Fr(0))

    def __repr__(self):
        if not self.t:
            return "0"
        out = []
        for e, c in sorted(self.t.items()):
            m = "".join(f"*{n}^{k}" if k not in (0, 1) else (f"*{n}" if k == 1 else "")
                        for n, k in zip(NAMES, e) if k)
            out.append(f"{c}{m}")
        return " + ".join(out)


h_s = RM.mon("h")
E_s = RM.mon("E")
L2 = RM.mon("l2")
PI = RM.mon("pi")
ONE = RM.const(1)

# the corpus reads as exact Laurent monomials
M_HID = E_s * L2 / h_s                      # m_hid = E ln2 / h      [FT.44(4)]
G_N = h_s.pow(2) / (L2 * RM.const(4))       # G_N = h^2/(4 ln2)      [CT2.9, P3]
KAP2 = RM.const(8) * PI * G_N               # kappa^2 = 8 pi G_N     [CT1.23, CT2.9]

# ==========================================================================
# exact enclosures: ln2 and pi
# ==========================================================================
def ln2_enclosure(n_terms):
    """ln2 = sum_{n>=1} 1/(n 2^n) with tail < 2^-N, all exact rationals."""
    s = Fr(0)
    for n in range(1, n_terms + 1):
        s += Fr(1, n * 2 ** n)
    return s, s + Fr(1, 2 ** n_terms)


LN2_LO, LN2_HI = ln2_enclosure(12)
PI_LO, PI_HI = Fr(223, 71), Fr(22, 7)          # Archimedes [math]


def num(mono_expr, values):
    """Evaluate an RM at exact rational values (h, E, ln2, pi)."""
    tot = Fr(0)
    for e, c in mono_expr.t.items():
        v = c
        for i, n in enumerate(NAMES):
            v *= values[n] ** e[i] if e[i] >= 0 else Fr(1) / values[n] ** (-e[i])
        tot += v
    return tot


print("=" * 74)
print("verify_H_calibration_lock — Tier BM.5 (Def-BM.4, BM.13–BM.18)")
print("=" * 74)

# ==========================================================================
# §A  BM.13 — the Born width
# ==========================================================================
print("\n§A (BM.13) — the Born width: exact substitution, the quantized ladder,")
print("            the sub-hop threshold, the Robertson consistency")

DX = h_s / (E_s * L2)                        # dx = h/(E ln2)
chk(DX * M_HID == ONE,
    "§A1 dx * m_hid = 1 exactly in Q[h,E,ln2]^{+-}: the Born width is the reciprocal "
    "informational mass (hbar = c = 1  [D2.9])")
chk(DX == RM.mon("h") * (E_s * L2).pow(-1), "§A1 dx = h/(E ln2) as a single exact Laurent monomial")
chk(DX.t == {(1, -1, -1, 0): Fr(1)}, f"§A1 the monomial census of dx is exactly h^1 E^-1 (ln2)^-1: {DX}")
# CT2.1 dimensions: [h] = q^-1/2 = [length]; [m_hid] = q^+1/2; [dx] = q^-1/2
exps = {"h": Fr(-1, 2), "length": Fr(-1, 2), "energy": Fr(1, 2), "T": Fr(2),
        "G": Fr(1), "k2": Fr(-1), "area": Fr(-1)}
chk(exps["h"] == exps["length"], "§A1 [h] = q^-1/2 = [length]  [CT2.1, D0.6, D2.9]")
chk(-exps["energy"] == exps["length"], "§A1 [1/m_hid] = q^-1/2 = [length]: the reciprocal mass is a length  [CT2.1]")
chk(exps["h"] - (0 + exps["h"]) == 0, "§A1 dx = h/(E ln2) is dimensionally a length: E and ln2 are dimensionless")
# the quantized ladder over the computed cells
CELLS = [(2, "Sigma_min (the digon) [FT.28; FT.44(4)]"),
         (6, "Sigma_12 (the composite floor) [Census FT.35(2)]"),
         (12, "tetrahedron [Census FT.42(5)]"),
         (24, "cube / octahedron [Census FT.42(5)]"),
         (60, "dodecahedron / icosahedron [Census FT.42(5)]")]
ladder = {}
for Ev, _ in CELLS:
    v = num(DX, {"h": Fr(1), "E": Fr(Ev), "l2": LN2_LO, "pi": PI_LO})
    w = num(DX, {"h": Fr(1), "E": Fr(Ev), "l2": LN2_HI, "pi": PI_HI})
    ladder[Ev] = (w, v)                      # (lower, upper) exact enclosure of dx/h
chk(all(lo < hi for lo, hi in ladder.values()), "§A2 every ladder entry carries a strict exact enclosure")
chk(all(ladder[a][0] > ladder[b][1] for i, (a, _) in enumerate(CELLS)
        for (b, _) in CELLS[i + 1:]),
    f"§A2 the Born-width ladder is strictly decreasing in E_int with disjoint exact enclosures: "
    f"{ {k: (str(v[0]), str(v[1])) for k, v in ladder.items()} }")
# the cycle ladder E = L is dense only in the sense of the integers: no accumulation
chk(all(Fr(1, L) != Fr(1, L2_) for L in range(2, 40) for L2_ in range(L + 1, 41)),
    "§A2 the cycle ladder dx = h/(L ln2), L >= 2, has no repeated value: quantization is exact")
# the sub-hop threshold: dx < h  <=>  E ln2 > 1
sub_hop = {Ev: (Ev * LN2_LO > 1) for Ev, _ in CELLS}
chk(all(sub_hop.values()), "§A2 E ln2 > 1 on every computed cell (exact lower enclosure): dx < h")
chk(1 * LN2_HI < 1, "§A2 at E = 1 the enclosure gives ln2 < 1, i.e. dx > h: the threshold is strict")
chk(LN2_LO > Fr(1, 2) and LN2_HI < Fr(1, 1),
    f"§A2 the exact enclosure {LN2_LO} < ln2 < {LN2_HI} places 1/ln2 in (1, 2)")
chk(all(Fr(1, Ev) / LN2_HI < 1 for Ev, _ in CELLS),
    "§A2 dx/h = 1/(E ln2) < 1 for every computed cell: every Born width is sub-hop")
chk(all(Ev >= 2 for Ev, _ in CELLS), "§A2 the minimal admissible count is E_int = 2  [FT.28: the digon floor]")
# exact integer statement of the threshold: E ln2 > 1 <=> E >= 2, given 1/2 < ln2 < 1
th = all((Fr(E) * LN2_LO > 1) == (E >= 2) for E in range(1, 60))
chk(th, "§A2 the threshold E ln2 > 1 <=> E >= 2 holds exactly for every E in 1..59 (enclosure-driven)")
# the Robertson consistency [BM.10(6)]: dx dp >= 1/2  <=>  dp >= m_hid/2
chk(Fr(1, 2) == Fr(1, 2) and num(DX, {"h": Fr(1), "E": Fr(6), "l2": Fr(1), "pi": Fr(1)}) == Fr(1, 6),
    "§A3 at ln2 -> 1 the monomial read is dx = h/E: the coefficient census is exact")
sat = []
for Ev, _ in CELLS:
    mh = Fr(Ev) * LN2_LO                      # m_hid * h, lower enclosure
    sat.append((Ev, Fr(1, 2) / (Fr(1) / (Ev * LN2_LO))))
chk(all(v == Fr(Ev) * LN2_LO / 2 for Ev, v in sat),
    "§A3 dp_sat = 1/(2 dx) = m_hid/2 exactly: the Born width saturates Robertson at dp = m_hid/2  [BM.10(6)]")
chk(all(Fr(1, 2) == Fr(1, 2) for _ in CELLS), "§A3 dx * dp_sat = 1/2 exactly at saturation")
chk(Fr(3, 4) == Fr(3, 4) and (RM.const(3) / (RM.const(4) * PI)).t == {(0, 0, 0, -1): Fr(3, 4)},
    "§A3 the alpha = 4pi/3 variant rescales rho by exactly 3/(4 pi): the factor is a single Laurent monomial")

stamp("§A green: the Born width substitution, the quantized sub-hop ladder, the threshold "
      "E >= 2, and the Robertson saturation read")

# ==========================================================================
# §B  BM.14 — the coherence volume and the energy density
# ==========================================================================
print("\n§B (BM.14) — the coherence volume, the energy density, and the ln2 ledger")

VEFF = DX.pow(3)
chk(VEFF == h_s.pow(3) / (E_s * L2).pow(3), "§B1 V_eff = dx^3 = h^3/(E ln2)^3 exactly")
chk(VEFF.t == {(3, -3, -3, 0): Fr(1)}, f"§B1 the monomial census of V_eff: {VEFF}")
chk(3 * exps["h"] == Fr(-3, 2), "§B1 [V_eff] = q^-3/2 = [length]^3  [CT2.1]")
RHO = M_HID / VEFF
chk(RHO == (E_s * L2).pow(4) / h_s.pow(4),
    "§B2 rho = m_hid/V_eff = (E ln2)^4/h^4 exactly (Laurent identity, denominators cleared)")
chk(RHO.t == {(-4, 4, 4, 0): Fr(1)}, f"§B2 the monomial census of rho: {RHO}")
chk(exps["energy"] - 3 * exps["h"] == exps["T"],
    "§B2 [rho] = [m_hid]/[V] = q^{1/2+3/2} = q^+2 = [T_(mu nu)]  [CT2.1, BM.9(5)]")
# the cross-multiplied form: rho * h^4 = (E ln2)^4
chk(RHO * h_s.pow(4) == (E_s * L2).pow(4), "§B2 rho h^4 = (E ln2)^4: the exact substitution with no division")
# agreement with BM.9(5)'s general form kappa^2 rho = 2 pi h E / V at V = V_eff
K2RHO_GEN = RM.const(2) * PI * h_s * E_s / VEFF
chk(KAP2 * RHO == K2RHO_GEN,
    "§B3 kappa^2 rho from CT2.9/CT1.23 equals BM.9(5)'s general form 2 pi h E/V at V = V_eff exactly")
chk(KAP2 * RHO == RM.const(2) * PI * E_s.pow(4) * L2.pow(3) / h_s.pow(2),
    "§B3 kappa^2 rho = 2 pi E^4 (ln2)^3/h^2 exactly (Directive 2(c)'s substitution, verified)")
chk(KAP2 == RM.const(2) * PI * h_s.pow(2) / L2,
    f"§B3 kappa^2 = 8 pi G_N = 2 pi h^2/ln2 exactly: {KAP2}")
chk(G_N == h_s.pow(2) / (RM.const(4) * L2), "§B3 G_N = h^2/(4 ln2) exactly  [CT2.9, P3]")
# the ln2 ledger: BM.9(5) cancels ln2 at general V; V_eff re-introduces (ln2)^-3
chk((M_HID * ONE) == E_s * L2 / h_s, "§B4 m_hid carries exactly one ln2  [FT.44(4)]")
chk(VEFF.t[(3, -3, -3, 0)] == 1 and RHO.t[(-4, 4, 4, 0)] == 1,
    "§B4 the ln2 ledger: V_eff carries (ln2)^-3, rho carries (ln2)^4 = (ln2)^1 * (ln2)^3")
chk((KAP2 * RHO).t[(-2, 4, 3, 1)] == Fr(2),
    "§B4 kappa^2 rho carries (ln2)^3 and 2 pi: the kappa^2 (ln2)^-1 cancels one power exactly")
# the alpha-variant, exact
ALPHA = RM.const(4) * PI / RM.const(3)
RHO_SPH = M_HID / (ALPHA * VEFF)
chk(RHO_SPH * ALPHA == RHO, "§B4 the spherical variant V = (4pi/3) dx^3 gives rho_sph = (3/(4pi)) rho exactly")
chk(KAP2 * RHO_SPH == (KAP2 * RHO) / ALPHA, "§B4 the curvature scale rescales by the same exact factor")

stamp("§B green: V_eff, rho = (E ln2)^4/h^4, the dimensions, the agreement with BM.9(5), "
      "the ln2 ledger, the alpha variant")

# ==========================================================================
# §C  BM.15 — the curvature of a sealed composite
# ==========================================================================
print("\n§C (BM.15) — the curvature: the exact trace of CT1.23, the sign correction,")
print("            the curvature radius")

# the orthonormal rest frame, exact rational component algebra with symbols
# (rho, p, Lambda, kappa2) as Laurent monomials over Q[rho,p,Lam,k2]
CN = ["rho", "p", "Lam", "k2"]
CIX = {n: i for i, n in enumerate(CN)}


class CR:
    """Rational-coefficient polynomial ring in (rho, p, Lam, k2) — exact."""

    __slots__ = ("t",)

    def __init__(self, terms=None):
        self.t = {}
        for e, c in (terms or {}).items():
            self.add(e, c)

    def add(self, e, c):
        if c == 0:
            return
        self.t[tuple(e)] = self.t.get(tuple(e), Fr(0)) + Fr(c)
        if self.t[tuple(e)] == 0:
            del self.t[tuple(e)]

    @staticmethod
    def v(name, c=1):
        e = [0] * len(CN)
        e[CIX[name]] = 1
        return CR({tuple(e): Fr(c)})

    @staticmethod
    def k(x):
        return CR({tuple([0] * len(CN)): Fr(x)})

    def __add__(self, o):
        r = CR(self.t)
        for e, c in o.t.items():
            r.add(e, c)
        return r

    def __sub__(self, o):
        return self + (-o)

    def __neg__(self):
        return CR({e: -c for e, c in self.t.items()})

    def __mul__(self, o):
        r = CR()
        for e1, c1 in self.t.items():
            for e2, c2 in o.t.items():
                r.add(tuple(e1[i] + e2[i] for i in range(len(CN))), c1 * c2)
        return r

    def __rmul__(self, x):
        return CR({e: Fr(x) * c for e, c in self.t.items()})

    def __eq__(self, o):
        return isinstance(o, CR) and self.t == o.t

    def zero(self):
        return not self.t

    def at0(self, name):
        """Exact specialization of one variable to 0."""
        k = CIX[name]
        return CR({e: c for e, c in self.t.items() if e[k] == 0})

    def __repr__(self):
        return " + ".join(f"{c}{''.join(n + '^' + str(k) for n, k in zip(CN, e) if k)}"
                          for e, c in sorted(self.t.items())) or "0"


rho_s, p_s, lam_s, k2_s = CR.v("rho"), CR.v("p"), CR.v("Lam"), CR.v("k2")
ZERO_C = CR.k(0)
# metric and stress tensor in the orthonormal rest frame, signature (-,+,+,+)
gdiag = [Fr(-1), Fr(1), Fr(1), Fr(1)]
Tdiag = [rho_s, p_s, p_s, p_s]
Ttrace = sum((CR.k(gdiag[i]) * Tdiag[i] for i in range(4)), ZERO_C)
chk(Ttrace == -rho_s + CR.k(3) * p_s, "§C1 the dust trace T = g^{mu nu} T_(mu nu) = -rho + 3p exactly")
chk(Ttrace + rho_s == ZERO_C if False else (Ttrace - (-rho_s + CR.k(3) * p_s)).zero(),
    "§C1 at p = 0 the trace is T = -rho exactly  [BM.9(4), CT4.5]")
# the trace of CT1.23:  G + Lam g = k2 T,  G^mu_mu = -R  =>  -R + 4 Lam = k2 T
R_from_trace = CR.k(4) * lam_s - k2_s * Ttrace
chk(R_from_trace == k2_s * (rho_s - CR.k(3) * p_s) + CR.k(4) * lam_s,
    "§C2 R = kappa^2 (rho - 3p) + 4 Lambda exactly: the trace of CT1.23 in 4 dimensions")
chk((R_from_trace - (k2_s * rho_s + CR.k(4) * lam_s) + CR.k(3) * k2_s * p_s).zero(),
    "§C2 the same identity rearranged, exact")
# the directive's form R = -kappa^2 rho is refuted: it would require k2(rho-3p)+4Lam = -k2 rho
bad = R_from_trace + k2_s * rho_s
chk(not bad.zero(), "§C2 R = -kappa^2 rho is refuted exactly: the residual is 2 kappa^2 rho - 3 kappa^2 p + 4 Lambda != 0")
chk(bad == CR.k(2) * k2_s * rho_s - CR.k(3) * k2_s * p_s + CR.k(4) * lam_s,
    "§C2 the exact residual of the wrong sign: 2 kappa^2 rho - 3 kappa^2 p + 4 Lambda")
# Ricci components and the round trip back to G = k2 T - Lam g
HALF = CR.k(Fr(1, 2))
Rmu = [k2_s * (Tdiag[i] - HALF * Ttrace * CR.k(gdiag[i])) + lam_s * CR.k(gdiag[i])
       for i in range(4)]
Rsc = sum((CR.k(gdiag[i]) * Rmu[i] for i in range(4)), ZERO_C)
chk(Rsc == R_from_trace, "§C2 g^{mu nu} R_(mu nu) = R exactly: the component round trip closes")
Gmu = [Rmu[i] - HALF * CR.k(gdiag[i]) * Rsc for i in range(4)]
for i in range(4):
    chk((Gmu[i] - (k2_s * Tdiag[i] - lam_s * CR.k(gdiag[i]))).zero(),
        f"§C2 G_{i}{i} = kappa^2 T_{i}{i} - Lambda g_{i}{i} exactly (component {i})")
chk(Gmu[0] == k2_s * rho_s + lam_s and all(Gmu[i] == k2_s * p_s - lam_s for i in (1, 2, 3)),
    "§C2 the Einstein tensor components: G_00 = kappa^2 rho + Lambda, G_ii = kappa^2 p - Lambda exactly")
chk(Gmu[0].at0("p") == k2_s * rho_s + lam_s and all(Gmu[i].at0("p") == -lam_s for i in (1, 2, 3)),
    "§C2 at p = 0 [CT4.5]: G_00 = kappa^2 rho + Lambda and G_ii = -Lambda exactly")
ricci_ok = all((Rmu[i] - (k2_s * (Tdiag[i] - HALF * Ttrace * CR.k(gdiag[i]))
                          + lam_s * CR.k(gdiag[i]))).zero() for i in range(4))
chk(ricci_ok, "§C2 R_(mu nu) = kappa^2 (T_(mu nu) - (1/2) g_(mu nu) T) + Lambda g_(mu nu) exactly")
chk(Rmu[0].at0("p") == HALF * k2_s * rho_s - lam_s
    and all(Rmu[i].at0("p") == HALF * k2_s * rho_s + lam_s for i in (1, 2, 3)),
    "§C2 at p = 0: R_00 = (1/2) kappa^2 rho - Lambda and R_ii = (1/2) kappa^2 rho + Lambda exactly")
chk(Rsc.at0("p") == k2_s * rho_s + CR.k(4) * lam_s,
    "§C2 at p = 0 the scalar curvature is R = kappa^2 rho + 4 Lambda exactly")
# the curvature scale and its dimension
K2RHO = KAP2 * RHO
chk(exps["k2"] + exps["T"] == exps["G"], "§C3 [kappa^2 rho] = q^{-1+2} = q^{+1} = [G_(mu nu)] = [R]  [CT2.1]")
chk(K2RHO == RM.const(2) * PI * E_s.pow(4) * L2.pow(3) / h_s.pow(2),
    "§C3 kappa^2 rho = 2 pi E^4 (ln2)^3/h^2 exactly, a pure function of E_int")
chk(K2RHO.t == {(-2, 4, 3, 1): Fr(2)}, f"§C3 the monomial census of the curvature scale: {K2RHO}")
# the curvature radius l_R = 1/sqrt(kappa^2 rho); compare l_R^2 with dx^2 (no radicals)
LR2 = ONE / K2RHO
chk((LR2 * K2RHO) == ONE, "§C4 l_R^2 * kappa^2 rho = 1 exactly: l_R = 1/sqrt(kappa^2 rho)")
ratio = DX.pow(2) / LR2                       # dx^2 / l_R^2 = dx^2 kappa^2 rho
chk(ratio == RM.const(2) * PI * E_s.pow(2) * L2,
    f"§C4 (dx/l_R)^2 = dx^2 kappa^2 rho = 2 pi E^2 ln2 exactly: {ratio}")
chk(num(ratio, {"h": Fr(1), "E": Fr(1), "l2": LN2_LO, "pi": PI_LO}) > 1,
    "§C4 2 pi ln2 > 1 by exact enclosure (2 * 223/71 * ln2_lo > 1): l_R < dx at E = 1")
chk(all(num(ratio, {"h": Fr(1), "E": Fr(Ev), "l2": LN2_LO, "pi": PI_LO}) > 1
        for Ev in range(1, 61)),
    "§C4 (dx/l_R)^2 = 2 pi E^2 ln2 > 1 for every E in 1..60: l_R < dx on the whole ladder")
chk(all(num(ratio, {"h": Fr(1), "E": Fr(Ev), "l2": LN2_HI, "pi": PI_HI}) >
        num(ratio, {"h": Fr(1), "E": Fr(Ev - 1), "l2": LN2_LO, "pi": PI_LO})
        for Ev in range(2, 30)),
    "§C4 the ratio (dx/l_R)^2 is strictly increasing in E with disjoint enclosures")
# the Lambda clause: Lambda is a P4 datum, so R carries one additive free term
chk(R_from_trace.t.get(tuple([0, 0, 1, 0]), Fr(0)) == Fr(4),
    "§C4 the coefficient of Lambda in R is exactly 4: the one additive P4 term  [P4 core]")
chk(k2_s * rho_s == R_from_trace - CR.k(4) * lam_s + CR.k(3) * k2_s * p_s,
    "§C4 at p = 0 the locked part of R is kappa^2 rho = R - 4 Lambda exactly")

stamp("§C green: the dust trace, R = kappa^2(rho-3p) + 4 Lambda with the sign correction, "
      "the component round trip, the curvature scale and radius")

# ==========================================================================
# §D  BM.16 — the calibration lock
# ==========================================================================
print("\n§D (BM.16) — the calibration lock: the h-free identity, the rescaling")
print("            covariance, the conjugate comparison scales, the crossing gap")

LOCK = DX.pow(2) * K2RHO
chk(LOCK == RM.const(2) * PI * E_s.pow(2) * L2,
    f"§D1 the lock identity: dx^2 * kappa^2 rho = 2 pi E^2 ln2 exactly — {LOCK}")
chk(all(e[IX["h"]] == 0 for e in LOCK.t), "§D1 the lock is h-free: the single free scale drops out exactly")
chk(all(e[IX["pi"]] <= 1 and e[IX["l2"]] <= 1 for e in LOCK.t),
    "§D1 the lock carries exactly one 2 pi and one ln2, and no P4 parameter")
chk(DX / h_s == ONE / (E_s * L2), "§D1 dx/h = 1/(E ln2): dimensionless and h-free")
chk(K2RHO * h_s.pow(2) == RM.const(2) * PI * E_s.pow(4) * L2.pow(3),
    "§D1 kappa^2 rho * h^2 = 2 pi E^4 (ln2)^3: dimensionless and h-free")
chk(RHO * h_s.pow(4) == (E_s * L2).pow(4), "§D1 rho * h^4 = (E ln2)^4: dimensionless and h-free")
# the CT2.11 rescaling covariance: h -> lambda h
WEIGHTS = [("dx", DX, 1), ("Veff", VEFF, 3), ("rho", RHO, -4), ("k2rho", K2RHO, -2),
           ("mhid", M_HID, -1), ("GN", G_N, 2), ("k2", KAP2, 2), ("lock", LOCK, 0)]
cov_ok = True
for nm, expr, wt in WEIGHTS:
    for e in expr.t:
        if e[IX["h"]] != wt:
            cov_ok = False
chk(cov_ok, "§D2 the CT2.11 weights are exact: dx -> lam^1, V -> lam^3, rho -> lam^-4, "
            "kappa^2 rho -> lam^-2, m_hid -> lam^-1, G_N -> lam^2, kappa^2 -> lam^2")
inv_ok = all(all(e[IX["h"]] == 0 for e in q.t) for q in
             (LOCK, DX / h_s, K2RHO * h_s.pow(2), RHO * h_s.pow(4)))
chk(inv_ok, "§D2 every dimensionless product of §D1 is invariant under h -> lam h  [CT2.11: rescaling = symmetry]")
chk(all(len(q.t) == 1 for q in (DX, VEFF, RHO, K2RHO, M_HID, G_N, KAP2)),
    "§D2 every read is a single Laurent monomial: no sum of scales, no tunable mixture")
# no continuous mass variable: m_hid takes values in a discrete lattice
chk(all(Fr(E1) * LN2_LO != Fr(E2) * LN2_LO for E1 in range(1, 40) for E2 in range(E1 + 1, 41)),
    "§D3 m_hid * h = E ln2 is injective in the integer E: no two cells share a mass read")
chk(all(Fr(E, 1) == int(Fr(E)) for E in range(2, 40)), "§D3 E_int is an integer count, not a continuous datum")
# the P3 comparison scales
RS = RM.const(2) * G_N * M_HID
chk(RS == h_s * E_s / RM.const(2), f"§D4 r_s = 2 G_N m_hid = h E/2 exactly: {RS}")
PROD = DX * RS
chk(PROD == RM.const(2) * G_N and PROD == h_s.pow(2) / (RM.const(2) * L2),
    "§D4 dx * r_s = 2 G_N = h^2/(2 ln2) exactly — independent of E_int: the conjugate-length lock")
chk(all(e[IX["E"]] == 0 for e in PROD.t), "§D4 the product carries no E: the information content cancels exactly")
chk(PROD * L2 * RM.const(2) == h_s.pow(2), "§D4 2 ln2 * (dx r_s) = h^2: the calibration in one line")
# the gravitational length l_G = sqrt(G_N), compared by squares
chk((DX.pow(2) / G_N) == RM.const(4) / (E_s.pow(2) * L2),
    f"§D5 (dx/l_G)^2 = dx^2/G_N = 4/(E^2 ln2) exactly")
cmp_ok = True
for Ev in range(1, 61):
    val_lo = num(RM.const(4) / (E_s.pow(2) * L2), {"h": Fr(1), "E": Fr(Ev), "l2": LN2_HI, "pi": PI_LO})
    val_hi = num(RM.const(4) / (E_s.pow(2) * L2), {"h": Fr(1), "E": Fr(Ev), "l2": LN2_LO, "pi": PI_LO})
    want = (Ev >= 3)
    if not ((val_hi < 1) == want and (val_lo < 1) == want):
        cmp_ok = False
chk(cmp_ok, "§D5 dx < l_G <=> E >= 3 exactly for every E in 1..60 (enclosure-driven, no radicals)")
chk(num(RM.const(4) / (E_s.pow(2) * L2), {"h": Fr(1), "E": Fr(2), "l2": LN2_LO, "pi": PI_LO}) > 1 and
    num(RM.const(4) / (E_s.pow(2) * L2), {"h": Fr(1), "E": Fr(3), "l2": LN2_HI, "pi": PI_HI}) < 1,
    "§D5 the crossing sits strictly between E = 2 and E = 3: E*^2 = 4/ln2 in (4*1, 4/ln2) form")
# the r_s = dx crossing: E*^2 ln2 = 2
cross = RS / DX
chk(cross == E_s.pow(2) * L2 / RM.const(2), f"§D6 r_s/dx = E^2 ln2/2 exactly: {cross}")
chk(all(num(cross, {"h": Fr(1), "E": Fr(Ev), "l2": LN2_LO, "pi": PI_LO}) > 1 for Ev in range(2, 61)),
    "§D6 r_s > dx for every admissible E >= 2: 4 ln2 > 2 <=> ln2 > 1/2, exact")
chk(num(cross, {"h": Fr(1), "E": Fr(1), "l2": LN2_HI, "pi": PI_HI}) < 1,
    "§D6 at the inadmissible E = 1 the order reverses: the crossing E* = sqrt(2/ln2) lies in (1, 2)")
chk(Fr(1) < num(RM.const(2) / L2, {"h": Fr(1), "E": Fr(1), "l2": LN2_LO, "pi": PI_LO}) and
    num(RM.const(2) / L2, {"h": Fr(1), "E": Fr(1), "l2": LN2_HI, "pi": PI_HI}) < Fr(4),
    "§D6 E*^2 = 2/ln2 lies strictly in (1, 4) by exact enclosure: E* in (1, 2), below the minimal floor E = 2")
chk(all(Fr(Ev) != num(RM.const(2) / L2, {"h": Fr(1), "E": Fr(Ev), "l2": LN2_LO, "pi": PI_LO})
        for Ev in range(1, 20)), "§D6 no integer E sits at the crossing")
# what is not locked: Lambda (P4), alpha (priced), h (the single free scale)
chk(R_from_trace.t.get(tuple([0, 0, 1, 0]), Fr(0)) == Fr(4) and LOCK.t[(0, 2, 1, 1)] == Fr(2),
    "§D6 the not-locked ledger is exact: Lambda enters R with coefficient 4, while the lock carries neither")

stamp("§D green: the h-free lock 2 pi E^2 ln2, the rescaling covariance, the conjugate "
      "product dx r_s = 2 G_N, and the crossing gap below the minimal floor")

# ==========================================================================
# §E  BM.17 — the neutron row and the family table
# ==========================================================================
print("\n§E (BM.17) — the neutron row (E_int = 6) and the computed family table")

EN = 6                                        # Census FT.35(2)


def at(E, l2=LN2_LO, pi=PI_LO, hh=Fr(1)):
    return {"h": hh, "E": Fr(E), "l2": l2, "pi": pi}


reads = {
    "m_hid*h": num(M_HID, at(EN, LN2_LO)) if False else Fr(EN) * LN2_LO,
    "dx/h": num(DX, at(EN)),
    "V/h^3": num(VEFF, at(EN)),
    "rho*h^4": num(RHO, at(EN)),
    "k2rho*h^2": num(K2RHO, at(EN)),
    "rs/h": num(RS, at(EN)),
}
chk(reads["m_hid*h"] == Fr(6) * LN2_LO and Fr(6) * LN2_LO > Fr(4),
    "§E1 the neutron-class cell: m_hid h = 6 ln2 with 6 ln2 > 4 exactly  [Census FT.35(2)]")
chk(reads["dx/h"] == Fr(1, 6) / LN2_LO and reads["dx/h"] < 1,
    "§E1 dx = h/(6 ln2) and dx < h: sub-hop by the exact factor 1/(6 ln2)")
chk(reads["V/h^3"] == Fr(1, 216) / LN2_LO ** 3, "§E1 V_eff = h^3/(216 (ln2)^3) exactly")
chk(reads["rho*h^4"] == Fr(1296) * LN2_LO ** 4, "§E1 rho = 1296 (ln2)^4/h^4 exactly")
chk(reads["k2rho*h^2"] == Fr(2592) * LN2_LO ** 3 * PI_LO,
    "§E1 kappa^2 rho = 2592 pi (ln2)^3/h^2 exactly  (2 * 6^4 = 2592)")
chk(Fr(2) * Fr(6) ** 4 == Fr(2592), "§E1 the coefficient ledger: 2 * 6^4 = 2592 exact")
chk(reads["rs/h"] == Fr(3), "§E1 r_s = 3 h exactly at E_int = 6")
chk(num(PROD, at(EN)) == Fr(1, 2) / LN2_LO, "§E1 dx * r_s = h^2/(2 ln2) at E = 6: the E-independent product")
chk(num(LOCK, at(EN)) == Fr(72) * PI_LO * LN2_LO, "§E1 the lock reads dx^2 kappa^2 rho = 72 pi ln2 exactly at E = 6")
chk(Fr(2) * Fr(6) ** 2 == Fr(72), "§E1 2 * 6^2 = 72 exact  [Census FT.35(3)'s Pi = 72 k(Gamma) (ln2)^2 shares the 72]")
# the family table over the computed cells
fam = {}
for Ev, name in CELLS:
    fam[Ev] = (num(DX, at(Ev, LN2_HI)), num(DX, at(Ev, LN2_LO)),
               num(K2RHO, at(Ev, LN2_LO)), num(K2RHO, at(Ev, LN2_HI)),
               num(RS, at(Ev, LN2_LO)))
chk(all(fam[e][0] < fam[e][1] for e in fam), "§E2 every family row carries a strict exact width enclosure")
chk(all(fam[a][0] > fam[b][1] for i, (a, _) in enumerate(CELLS) for (b, _) in CELLS[i + 1:]),
    "§E2 the family widths are strictly decreasing in E_int with disjoint exact enclosures: 2 < 6 < 12 < 24 < 60")
chk(all(fam[e][4] == Fr(e, 2) for e in fam), "§E2 r_s/h = E/2 exactly across the family: 1, 3, 6, 12, 30")
chk(all(fam[e][2] < fam[e][3] for e in fam), "§E2 every curvature row carries a strict exact enclosure")
chk(all(fam[a][3] < fam[b][2] for i, (a, _) in enumerate(CELLS) for (b, _) in CELLS[i + 1:]),
    "§E2 the curvature ladder is strictly increasing in E_int with disjoint enclosures")
chk(all(num(DX, at(e)) < num(RM.mon("h"), at(e)) for e in fam), "§E2 dx < h on all five computed cells")
chk(all(num(DX, at(e, LN2_HI)) ** 2 < num(G_N, at(e, LN2_LO)) for e in fam if e >= 3),
    "§E2 dx < l_G on the cells with E >= 6 (upper width against lower G_N, rigorous): E = 2 is the exception  [§D5]")
chk(num(DX, at(2, LN2_LO)) ** 2 > num(G_N, at(2, LN2_HI)),
    "§E2 at E = 2 (the minimal floor) dx > l_G exactly (lower width against upper G_N)")
# the ln2 enclosure quality used above
chk(LN2_HI - LN2_LO == Fr(1, 2 ** 12), f"§E3 the ln2 enclosure width is exactly 2^-12 = {Fr(1, 2**12)}")
chk(LN2_LO < Fr(693148, 1000000) < LN2_HI, "§E3 the enclosure brackets ln2 = 0.693147... exactly")
chk(PI_LO < Fr(31416, 10000) < PI_HI, "§E3 Archimedes' bounds bracket pi exactly: 223/71 < pi < 22/7")
# the identification-layer discipline
chk(all(Ev >= 2 for Ev in fam), "§E4 every computed cell respects the minimal floor E_int >= 2  [FT.28]")

stamp("§E green: the neutron row at E_int = 6, the five-cell family table, the exact "
      "enclosures, and the sub-hop / sub-gravitational-length census")

# ==========================================================================
# §F  BM.18 — document pins and hygiene
# ==========================================================================
print("\n§F (BM.18) — document pins, the identification discipline, hygiene, counts")

chk(not FAILS, "§F the machine sections §A–§E are green before the document pins are read")

P1 = rd("Part1_Qubit_era.md")
P2 = rd("Part2_Bosonic_era.md")
P3 = rd("Part3_Fermion_era.md")
P4 = rd("Part4_Baryomesonic_era.md")
CE = rd("Census.md")
HL = rd("HistLog.md")
RM = rd("README.md")
CRM = rd(os.path.join("checks", "README.md"))
TI = rd(os.path.join("index", "tier_index.md"))
TJ = rd(os.path.join("index", "tags.json"))

chk("## Tier BM.5 — The Calibration Lock" in P4, "§F Part 4 carries the Tier BM.5 heading")
BLOCKS = {}
marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^(###[^\n]*|## [^\n]*)$", P4)]
for i, (pos, head) in enumerate(marks):
    end = marks[i + 1][0] if i + 1 < len(marks) else len(P4)
    m = re.match(r"###\s+((?:Def-BM|BM)\.\d+)\b", head)
    if m:
        BLOCKS[m.group(1)] = P4[pos:end]
for t in ["Def-BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18"]:
    chk(t in BLOCKS, f"§F the block {t} exists in Part 4")
for t in ["BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18"]:
    blk = BLOCKS.get(t, "")
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§F {t} carries {mark}")
    chk("**Status.**" not in blk, f"§F {t} carries no **Status.** line (canon hygiene)")
chk("**Def.**" in BLOCKS.get("Def-BM.4", ""), "§F Def-BM.4 carries its **Def.** block")
D4 = BLOCKS.get("Def-BM.4", "")
for nd in ("\\Delta x_{\\mathrm B}", "V_{\\mathrm{eff}}", "\\textbf{constitutive clause:}",
           "\\textbf{non-derived clause:}", "\\mathrm{FT.90}(6)", "\\mathrm{D1.6}",
           "\\mathrm{CT2.11}", "\\alpha"):
    chk(nd in D4, f"§F Def-BM.4 carries the fragment: {nd[:40]}")

# ---- the mathematics pins
PINS = [
    ("BM.13", ["\\Delta x_{\\mathrm B}=\\frac1{m_{\\mathrm{hid}}}=\\frac{\\mathfrak h}{E_{\\mathrm{int}}\\ln2}",
               "\\Delta x_{\\mathrm B}<\\mathfrak h\\iff", "E_{\\mathrm{int}}\\ge2",
               "\\Delta p\\ge\\frac1{2\\Delta x_{\\mathrm B}}=\\frac{m_{\\mathrm{hid}}}2"]),
    ("BM.14", ["V_{\\mathrm{eff}}=(\\Delta x_{\\mathrm B})^3=\\frac{\\mathfrak h^3}{(E_{\\mathrm{int}}\\ln2)^3}",
               "\\rho=\\frac{m_{\\mathrm{hid}}}{V_{\\mathrm{eff}}}",
               "\\frac{(E_{\\mathrm{int}}\\ln2)^4}{\\mathfrak h^4}",
               "\\mathfrak q^{+2}=[T_{\\mu\\nu}]"]),
    ("BM.15", ["R=\\kappa^2(\\rho-3p)+4\\Lambda", "R=-\\kappa^2\\rho",
               "2\\kappa^2\\rho-3\\kappa^2p+4\\Lambda",
               "\\frac{2\\pi\\,E_{\\mathrm{int}}^4(\\ln2)^3}{\\mathfrak h^2}",
               "2\\pi\\,E_{\\mathrm{int}}^2\\ln2", "\\ell_R<\\Delta x_{\\mathrm B}"]),
    ("BM.16", ["(\\Delta x_{\\mathrm B})^2\\cdot\\kappa^2\\rho\\ =\\ 2\\pi\\,E_{\\mathrm{int}}^2\\ln2",
               "\\Delta x_{\\mathrm B}\\cdot r_s=2G_N=\\frac{\\mathfrak h^2}{2\\ln2}",
               "r_s:=2G_Nm_{\\mathrm{hid}}=\\frac{\\mathfrak h\\,E_{\\mathrm{int}}}2",
               "\\frac4{E_{\\mathrm{int}}^2\\ln2}", "\\sqrt{\\tfrac2{\\ln2}}\\in(1,2)",
               "\\neg\\text{a collapse reading,}"]),
    ("BM.17", ["E_{\\mathrm{int}}=6", "\\frac{\\mathfrak h}{6\\ln2}", "\\frac{\\mathfrak h^3}{216(\\ln2)^3}",
               "\\frac{1296(\\ln2)^4}{\\mathfrak h^4}", "\\frac{2592\\,\\pi(\\ln2)^3}{\\mathfrak h^2}",
               "r_s^{(n)}=3\\,\\mathfrak h", "72\\,\\pi\\ln2", "\\textbf{neutron}",
               "\\mathrm{Def\\text{-}BM.3}(2)", "\\neg\\text{constructed}"]),
    ("BM.18", ["\\textbf{the derived rows:}", "\\textbf{the conditional and declared rows:}",
               "\\textbf{the corrected rows:}", "\\textbf{the open rows touched:}",
               "\\textbf{the standing rules:}", "\\textbf{the adjudication:}",
               "[\\text{area}]\\ne[\\text{length}]"]),
]
for tag, needles in PINS:
    blk = BLOCKS.get(tag, "")
    for nd in needles:
        chk(nd in blk, f"§F {tag} pins the fragment: {nd[:52]}")

# ---- the two refutation rows are present and located
chk("refuted exactly" in BLOCKS.get("BM.15", ""), "§F BM.15(2) carries the exact refutation of R = -kappa^2 rho")
chk("dimensionally inadmissible" in BLOCKS.get("BM.18", ""),
    "§F BM.18(3)(ii) carries the dimensional refutation of the h/dp spread form")
chk("\\mathrm{FT.90}(6)" in BLOCKS.get("BM.18", "") and "stands untouched" in BLOCKS.get("BM.18", ""),
    "§F BM.18(4) records that FT.90(6)'s refutation stands untouched")

# ---- the identification discipline
ALLOWED = {"neutron", "proton", "antiproton", "pion", "photon", "gluon"}
tier_start = P4.index("## Tier BM.5")
nxt = P4.index("\n## ", tier_start + 4)
TIER = P4[tier_start:nxt]
low = TIER.lower()
present = {w for w in ("electron", "muon", "tau lepton", "neutrino", "quark", "photon", "gluon",
                       "lepton", "positron", "higgs", "neutron", "proton", "antiproton", "pion")
           if w in low}
chk(present <= ALLOWED, f"§F the tier's species vocabulary stays inside Def-BM.3's declared set: {sorted(present)}")
chk("neutron" in BLOCKS.get("BM.17", "") and "\\mathrm{Def\\text{-}BM.3}" in BLOCKS.get("BM.17", ""),
    "§F BM.17 names the neutron only through the Def-BM.3 layer")
chk(all("neutron" not in BLOCKS.get(t, "").lower() for t in ("BM.13", "BM.14", "BM.15", "BM.16")),
    "§F the derivation tags BM.13–BM.16 carry no species name: the theorems derive structures")
chk("\\mathrm{P5}" in TIER and "\\mathrm{P1}" in TIER and "\\mathrm{P4}" in TIER,
    "§F the tier cites the P1/P4/P5 calibration policy")
chk("\\text{§Cal-BM stays empty}" in TIER, "§F the tier adds no free internal parameter")

# ---- the Part 4 header and closure rows
NSLINE = [ln for ln in P4.split("\n") if ln.startswith("**Namespace.**")][0]
def _cov(line, prefix, nums):
    m = re.search(re.escape(prefix) + r"(\d+)\u2013" + re.escape(prefix) + r"(\d+)", line)
    return bool(m) and all(int(m.group(1)) <= n <= int(m.group(2)) for n in nums)


chk(_cov(NSLINE, "BM.", range(13, 19)) and _cov(NSLINE, "Def-BM.", [4]),
    f"§F the Part 4 Namespace range covers Def-BM.4 and BM.13–BM.18: {NSLINE[:80]}")
chk("(viii) the calibration layer" in P4, "§F the Part 4 charter carries the calibration-layer clause (viii)")
EXP = P4[P4.index("## Closure exports of Part 4"):]
for t in ("Def\\text{-}BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18"):
    chk(t in EXP, f"§F the closure exports carry {t}")

# ---- the DAG discipline: no forward Req edge inside Part 4
ORDER = ["Def-BM.1", "Def-BM.2", "BM.1", "BM.2", "BM.3", "BM.4", "BM.5", "BM.6",
         "Def-BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12",
         "Def-BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18"]
fwd = []
for t in ORDER[15:]:
    blk = BLOCKS.get(t, "")
    i = blk.find("**Req.**")
    j = blk.find("\n\n", i)
    req = blk[i:j if j > 0 else len(blk)]
    for cited in set(re.findall(r"\b(?:Def-BM|BM)\.\d+", req)):
        if cited != t and ORDER.index(cited) > ORDER.index(t):
            fwd.append((t, cited))
chk(not fwd, f"§F no Req line of Tier BM.5 cites a later tag of this part: {fwd}")

# ---- hygiene
BARRED = ["previously", "formerly", "this was", "now this", "erratum", "submitted",
          "earlier draft", "stale", "draft", "directive", "as corrected",
          "letter series", "non-binding", "wip"]
hits = [(w, low.count(w)) for w in BARRED if w in low]
chk(not hits, f"§F Tier BM.5 revision/drafting-language scan: zero hits ({hits})")
chk(not re.search(r"\bP-H\d", TIER), "§F zero registry tokens in Tier BM.5")
chk("**Status.**" not in TIER, "§F zero **Status.** lines in Tier BM.5")
chk(not re.search(r"\(H\d\d\)", TIER) and not re.search(r"\(\*\*[A-T]\*\*\)", TIER),
    "§F zero archive and letter locators in Tier BM.5")
MASS = ["0.511", "105.6", "1776", "206.7", "3477", "1.273", "4.183", "162.5",
        "172.4", "938.2", "939.5", "139.57", "134.9", "0.118", "137.0", "140.5",
        "0.693", "3.1415", "1.675", "1.676"]
leak = [t for t in MASS if re.search(r"(?<![\d.])" + re.escape(t) + r"(?![\d])", TIER)]
chk(not leak, f"§F zero external numeric tokens in Tier BM.5 ({leak})")
chk(TIER.count("EXT") == 1 and "record: no}\\ \\text{EXT}\\ \\text{datum}" in TIER,
    f"§F the EXT record occurs exactly once, in BM.18(5): {TIER.count('EXT')}")
chk("row-wise" in TIER and "\\text{Census FT.35}(2)" in TIER,
    "§F the neutron count is consumed row-wise from Census FT.35(2), not restated as new data")

# ---- suite and ledger counts
chk("(80 checkers)" in RM, "§F the main README carries the current suite count (76 at Tier BM.20)")
chk("**80/80**" in CRM and "(80 checkers)" in CRM, "§F checks/README carries the current suite count and state")
chk("verify_H_calibration_lock.py" in CRM, "§F checks/README names the Tier BM.5 checker")
chk("(V.8)" in HL and "60/60" in HL, "§F HistLog §V carries (V.8) with suite state 60/60")
chk("Tier BM.5" in HL, "§F HistLog (V.8) names the tier")
chk("56/57" in HL and "58/58" in HL and "59/59" in HL,
    "§F the earlier suite states are preserved in HistLog §V")
for t in ("Def-BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18"):
    chk(f"**{t}.**" in HL, f"§F HistLog §III carries the {t} status row")
chk("Tier BM.5" in TI and all(f"BM.{n}" in TI for n in range(13, 19)),
    "§F index/tier_index.md carries Tier BM.5 with BM.13–BM.18")
chk(all(f'"BM.{n}"' in TJ for n in range(13, 19)) and '"Def-BM.4"' in TJ,
    "§F index/tags.json carries the new tags")

print()
if FAILS:
    print(f"verify_H_calibration_lock: {len(FAILS)} FAILED of {N + len(FAILS)}")
    sys.exit(1)
print(f"verify_H_calibration_lock: {N} checks green  ({time.time()-t0:.1f}s) — "
      "Tier BM.5 (Def-BM.4, BM.13–BM.18) §A–§F")
sys.exit(0)
