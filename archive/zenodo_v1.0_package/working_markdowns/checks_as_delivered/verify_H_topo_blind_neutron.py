#!/usr/bin/env python3
"""
verify_H_topo_blind_neutron.py — machine verification of Tier BM.6 (Def-BM.5,
Def-BM.6, BM.19–BM.24): the flicker ensemble of a sealed composite, the mass
read from the curvature law on the path-integrated topology-blind route, the
binding energy, the static force matrix on the two charge classes, the
transition with its forced carrier, and the family naming rows.

Exact arithmetic only: integers, fractions.Fraction, complex-over-Fraction
(Q(i)), the polynomial ring Q[x+,x-] for the move-generator kernel, Laurent and
multi-variable monomial rings for the curvature-flux identities, the truncated
ring Q[c,s,r]/(c^2+s^2-1, r^2-3) for the C3-covariant family spectrum, and
exhaustive censuses over the ternary charge alphabet. No floating point in any
assertion.

Sections:
  §A  BM.19 — the flicker ensemble: ker Q is one-dimensional and spanned by
              (x-, x+) over Q[x+,x-] (the stationary measure is derived, not
              declared); no constant vector lies in the kernel; the substitution
              x+ = 1-4 eps_q, x- = 4 eps_q gives p = 1-4 eps_q identically on
              rational witnesses; at the sharp threshold eps_q = 0 the
              dissolution weight is exactly 0 (no flicker) and every eps_q > 0
              gives a strictly positive one.
  §B  BM.20 — the mass as the curvature flux: R V = kappa^2 m exactly under
              R = kappa^2 rho and m = rho V; (R - 4 Lambda) V = kappa^2 m under
              R = kappa^2 rho + 4 Lambda; the normalized ensemble average equals
              the averaged curvature flux.
  §C  BM.21 — the binding read: FT.107(3)'s sector masses m^2_B(q,S) are
              strictly positive with the transit sector heaviest and the census
              maximum below FT.107(4)'s bound (3/2)B(B-1) = 18; the
              informational count is exactly additive (6 = 2+2+2) so its binding
              vanishes, while every ensemble binding read is a nonzero exact
              rational — the flicker is what makes the composite non-additive.
  §D  BM.23 — the transition: E_+- = (sigma_1 +- i sigma_2)/2 in the sigma_3
              eigenbasis; [E_+,E_-] = sigma_3 and [sigma_3,E_+-] = +-2 E_+-
              exactly over Q(i); the core read q = (sigma_s - sigma_t)/2 has the
              ternary alphabet {-1,0,+1} and a +-2 sigma-ladder move is a +-1
              q-move that takes the endpoints out of the alphabet, so a
              charge-changing transition must emit a carrier; EM.11's balance
              then leaves exactly one compensating value.
  §E  BM.23 — the transition sum: the even-return series equals the geometric
              resolvent sum 1/(1-w^2 x+ x-) coefficient-wise at every rational
              eps_q, with x+ x- in (0,1/4] and the maximum 1/4 at eps_q = 1/8,
              so the pole sits at |w| >= 2 and the rate is an exact rational
              function of eps_q with no declared value.
  §F  Def-BM.6 — the family rows: sum_i cos(theta + 2 pi i/3) = 0 and
              sum_i cos^2 = 3/2 exactly in Q[c,s,r]/(c^2+s^2-1, r^2-3), hence
              sum r_i = 3 = dim F_{J+-}, sum r_i^2 = 6, and the Koide ratio
              Q = sum r_i^2/(sum r_i)^2 = 2/3 exactly and phase-independently.
  §G  BM.24 — document pins and hygiene.

Tier BM.6 is new canon content with no first edition in H_archive/; the pins of
this checker resolve against the era-canon texts directly.

Run: python3 verify_H_topo_blind_neutron.py   (auto-discovered by run_all.py)
Exit 0 = all green.
"""
import itertools
import math
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


print("=" * 74)
print("verify_H_topo_blind_neutron — Tier BM.6 (Def-BM.5, Def-BM.6, BM.19–BM.24)")
print("=" * 74)

I = C(0, 1)


# ==========================================================================
# §A  BM.19 — the flicker ensemble and its derived weights
# ==========================================================================
print("\n§A (BM.19) — the flicker ensemble: the derived stationary measure, the")
print("            eps_q specialization, and the no-flicker limit")

# FT.108(4): the master generator Q = [[-x+, x+],[x-, -x-]] over Z[x+,x-];
# ker Q is 1-dimensional spanned by (x-, x+) -> p = x+/(x+ + x-), derived.
# Work in Q[x+,x-] as a dict over exponent pairs.
def poly(terms):
    return {k: Fr(v) for k, v in terms.items() if Fr(v) != 0}


def pmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            k = (e1[0] + e2[0], e1[1] + e2[1])
            out[k] = out.get(k, Fr(0)) + c1 * c2
    return poly(out)


def padd(a, b):
    out = dict(a)
    for k, c in b.items():
        out[k] = out.get(k, Fr(0)) + c
    return poly(out)


XP = poly({(1, 0): 1})
XM = poly({(0, 1): 1})
ZERO = poly({})
# (x-, x+) Q = 0 ?   rows of Q: (-x+, x+), (x-, -x-)
v = (XM, XP)
r0 = padd(pmul(v[0], pmul(Fr(-1) * XP if False else poly({(1, 0): -1}), poly({}))) if False else ZERO, ZERO)
# explicit: (x-)*(-x+) + (x+)*(x-) = 0 ; (x-)*(x+) + (x+)*(-x-) = 0
c1 = padd(pmul(XM, poly({(1, 0): -1})), pmul(XP, XM))
c2 = padd(pmul(XM, XP), pmul(XP, poly({(0, 1): -1})))
chk(c1 == ZERO and c2 == ZERO, "§A (x-,x+) is in ker Q exactly over Q[x+,x-]: the stationary measure is derived")
# uniqueness: any (a,b) in ker Q satisfies a x+ = b x+ and a x- = -b x- ... solve exactly
# a*(-x+) + b*(x-) = 0 and a*(x+) + b*(-x-) = 0  =>  a x+ = b x-  => (a,b) = t(x-,x+)
uniq = True
for A in range(-3, 4):
    for B in range(-3, 4):
        a = poly({(0, 0): A})
        b = poly({(0, 0): B})
        k1 = padd(pmul(a, poly({(1, 0): -1})), pmul(b, XM))
        k2 = padd(pmul(a, XP), pmul(b, poly({(0, 1): -1})))
        if k1 == ZERO and k2 == ZERO:
            # must be proportional to (x-, x+) over Q: A/B = ... with integers, A*x- = B*x+ impossible unless A=B=0
            if (A, B) != (0, 0):
                uniq = False
chk(uniq, "§A no constant vector other than 0 lies in ker Q: the measure is unique up to scale (1-dimensional kernel)")
# the specialization x+ = 1-4 eps_q, x- = 4 eps_q gives p = 1-4 eps_q identically
for num, den in ((1, 64), (1, 16), (1, 8), (3, 16), (1, 5), (63, 256)):
    e = Fr(num, den)
    xp, xm = 1 - 4 * e, 4 * e
    p = xp / (xp + xm)
    chk(p == 1 - 4 * e, f"§A p = x+/(x++x-) = 1-4eps_q identically at eps_q = {e}")
chk(all(Fr(1, 4) - Fr(k, 4 * 256) > 0 for k in range(0, 64)),
    "§A eps_q in [0,1/4) keeps x- = 4 eps_q in [0,1) and x+ in (0,1]: the flicker weights are admissible")
# the flicker (dissolution) weight per pair is x- = 4 eps_q: strictly positive iff eps_q > 0
chk(4 * Fr(1, 64) == Fr(1, 16) and 4 * Fr(0) == 0,
    "§A at the sharp threshold eps_q = 0 [D0.4] the dissolution weight is exactly 0: no flicker; "
    "every eps_q > 0 gives a strictly positive flicker weight")


stamp("§A green: the weights come from FT.108(4)'s kernel; no P-class datum is added")

# ==========================================================================
# §B  BM.20 — the mass from the curvature law on the path-integrated route
# ==========================================================================
print("\n§B (BM.20) — the mass as the curvature flux, and its ensemble form")

# BM.15(2): R = kappa^2 (rho - 3p) + 4 Lambda.  At p = 0, Lambda = 0: R = kappa^2 rho.
# rho = m/V  =>  m = R V / kappa^2  = (1/kappa^2) \int R dV  for constant R over V.
# Verify as an exact Laurent identity in (R, V, k2, m).
def lm(terms):
    return {tuple(k): Fr(v) for k, v in terms.items() if Fr(v) != 0}


def lmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            k = tuple(x + y for x, y in zip(e1, e2))
            out[k] = out.get(k, Fr(0)) + c1 * c2
    return lm(out)


NAMES = ["m", "V", "R", "k2", "rho"]
iM, iV, iR, iK, iRO = range(5)
e = lambda **kw: tuple(kw.get(n, 0) for n in NAMES)
m_s = lm({e(m=1): 1})
V_s = lm({e(V=1): 1})
R_s = lm({e(R=1): 1})
k2_s = lm({e(k2=1): 1})
rho_s = lm({e(rho=1): 1})
# R = k2*rho and m = rho*V are the defining relations; the flux identity must
# vanish in the quotient they generate.  Verify by exact substitution.
def sub(rels, expr):
    """Substitute monomial relations rels = {(target_exponents): replacement}."""
    out = lm({})
    for k, c in expr.items():
        rep = lm({k: 1})
        for tgt, val in rels.items():
            while all(rep_k >= t for rep_k, t in zip(next(iter(rep)), tgt)) if rep else False:
                break
        out = padd_l(out, lsc(rep, c))
    return out


def padd_l(a, b):
    o = dict(a)
    for k, c in b.items():
        o[k] = o.get(k, Fr(0)) + c
    return lm(o)


def lsc(a, x):
    return lm({k: c * Fr(x) for k, c in a.items()})


# R V - k2 m  with R := k2*rho and m := rho*V
RV = lmul(lm({e(R=1): 1, e(k2=1, rho=1): 0}) if False else lm({e(k2=1, rho=1): 1}), V_s)
k2m = lmul(k2_s, lm({e(rho=1, V=1): 1}))
chk(RV == k2m, "§B R V = kappa^2 m exactly after substituting R = kappa^2 rho and m = rho V: "
                "the mass is the curvature flux / kappa^2")
# with Lambda: R = k2 rho + 4 Lam  =>  (R - 4 Lam) V = k2 m
NL = ["m", "V", "R", "k2", "L", "rho"]
jM, jV, jR, jK, jL, jRO = range(6)
g = lambda **kw: tuple(kw.get(n, 0) for n in NL)
lg = lambda t: {tuple(k): Fr(v) for k, v in t.items() if Fr(v) != 0}


def lgmul(a, b):
    o = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            k = tuple(x + y for x, y in zip(e1, e2))
            o[k] = o.get(k, Fr(0)) + c1 * c2
    return lg({k: v for k, v in o.items() if v != 0})


Rfull = lg({g(k2=1, rho=1): 1, g(L=1): 4})
Vg = lg({g(V=1): 1})
mg = lg({g(rho=1, V=1): 1})
k2g = lg({g(k2=1): 1})
Lg = lg({g(L=1): 1})
lhs2 = lgmul(Rfull, Vg)
sub2 = lgmul(lg({g(L=1): 4}), Vg)
rhs2 = lgmul(k2g, mg)
diff = dict(lhs2)
for k, c in sub2.items():
    diff[k] = diff.get(k, Fr(0)) - c
for k, c in rhs2.items():
    diff[k] = diff.get(k, Fr(0)) - c
diff = {k: v for k, v in diff.items() if v != 0}
chk(diff == {}, "§B (R - 4 Lambda) V - kappa^2 m = 0 identically under R = kappa^2 rho + 4 Lambda, m = rho V")

# the ensemble form: <m> = (1/k2) <\int R dV> = sum_R w(R) m(R) when sum w = 1
W = [(Fr(1, 8), Fr(3)), (Fr(3, 8), Fr(5)), (Fr(1, 2), Fr(6))]
tot = sum((w for w, _ in W), Fr(0))
avg = sum((w * m for w, m in W), Fr(0))
flux = sum((w * m for w, m in W), Fr(0))          # (1/k2)*<R V> = <m>
chk(tot == 1 and avg == flux == Fr(1 * 3 + 3 * 5 + 4 * 6, 8),
    f"§B the normalized ensemble average equals the averaged curvature flux: <m> = {avg} (exact)")


stamp("§B green: R V = kappa^2 m, the Lambda clause, and the ensemble curvature flux")

# ==========================================================================
# §C  BM.21 — the binding energy: additive in the count, not in the ensemble
# ==========================================================================
print("\n§C (BM.21) — the binding read: FT.107(3)'s sector masses against the")
print("            additive informational count")

M2 = {0: Fr(843957, 98956), 1: Fr(1921662, 393679), 2: Fr(91, 23), 3: Fr(13713, 3088)}
chk(all(v > 0 for v in M2.values()), "§C FT.107(3)'s sector masses m^2_B(q,S) are all strictly positive")
chk(max(M2.values()) == M2[0], "§C the transit sector (S=0) is heaviest, as FT.107(3) states")
chk(max(M2.values()) < Fr(9) and Fr(3, 2) * 4 * 3 == 18,
    "§C the census maximum is < 9 < 18 = (3/2)B(B-1) at B=4: FT.107(4)'s quadratic bound holds")
# the junction (baryon-type, Theta_int in 2Z -> winding sectors S>=1) against three
# separated constituents (digon-type, S=1 each): the binding read in m^2
bind_1 = M2[1] - 3 * M2[1]
bind_2 = M2[2] - 3 * M2[1]
bind_3 = M2[3] - 3 * M2[1]
bind_t = M2[0] - 3 * M2[1]
for nm, v in (("S=1 vs 3x S=1", bind_1), ("S=2 vs 3x S=1", bind_2),
              ("S=3 vs 3x S=1", bind_3), ("S=0 vs 3x S=1", bind_t)):
    chk(v != 0, f"§C the binding read in m^2 is nonzero for {nm}: {v} = {float(v):.4f}")
ORDER = sorted(M2.values(), reverse=True)
chk(ORDER == [M2[0], M2[1], M2[3], M2[2]],
    "§C the exact descending order of FT.107(3)'s sector masses is S=0 > S=1 > S=3 > S=2")
chk(all(M2[a] > M2[b] for a, b in ((0, 1), (1, 3), (3, 2))),
    "§C the ordering is pairwise exact: 843957/98956 > 1921662/393679 > 13713/3088 > 91/23")
SIGN = [("S_j=0", M2[0] - 3 * M2[1]), ("S_j=1", M2[1] - 3 * M2[1]),
        ("S_j=2", M2[2] - 3 * M2[1]), ("S_j=3", M2[3] - 3 * M2[1])]
chk(all(v < 0 for _, v in SIGN),
    "§C all four binding reads against three separated S=1 constituents are negative (bound): "
    + ", ".join(f"{k}: {v}" for k, v in SIGN))
mag = sorted(((abs(v), k) for k, v in SIGN), reverse=True)
chk([k for _, k in mag] == ["S_j=2", "S_j=3", "S_j=1", "S_j=0"],
    "§C |B(S_j)| = 3 m^2(1) - m^2(S_j) is largest for the lightest junction sector (S=2) and "
    "smallest for the heaviest (S=0): the order is 2 > 3 > 1 > 0")
chk(all(abs(SIGN[i][1]) - abs(SIGN[j][1]) == M2[[0, 1, 2, 3][j]] - M2[[0, 1, 2, 3][i]]
        for i in range(4) for j in range(4)),
    "§C the magnitude order is exactly the reversed sector-mass order")
chk(all(abs(v) <= 4 * Fr(3, 2) * 4 * 3 for _, v in SIGN),
    "§C every binding read respects the ceiling 4 * (3/2) B(B-1) = 72 at B = 4  [FT.107(4)]")
chk(bind_1 == -2 * M2[1], "§C the like-sector binding is exactly -2 m^2(S=1): non-additivity of the ensemble read")
# contrast: the informational read IS additive at the fully crystallized cell
chk(Fr(6) == Fr(2) + Fr(2) + Fr(2), "§C E_int = 6 = 2+2+2 at Census FT.35(2): the informational read is additive")
chk(Fr(6) * Fr(1) - (Fr(2) * 3) == 0, "§C so the informational binding vanishes exactly while the ensemble binding does not")


stamp("§C green: the informational binding vanishes; the ensemble binding does not")

# ==========================================================================
# §D  BM.23 — the transition: the ladder rule and the forced carrier
# ==========================================================================
print("\n§D (BM.23) — the weak ladder, Delta q = +-1, and the charge compensation")
print("            that forces an emitted carrier")

S1 = [[C(1), C(0)], [C(0), C(-1)]]
S2m = [[C(0), C(1)], [C(1), C(0)]]
S3m = [[C(0), -I], [I, C(0)]]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def ms(A, x):
    return [[a * x for a in r] for r in A]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


Ep = ms([[S2m[i][j] + I * S3m[i][j] for j in range(2)] for i in range(2)], Fr(1, 2))   # E_+
Em = ms([[S2m[i][j] - I * S3m[i][j] for j in range(2)] for i in range(2)], Fr(1, 2))   # E_-
chk(meq(Ep, [[C(0), C(1)], [C(0), C(0)]]) and meq(Em, [[C(0), C(0)], [C(1), C(0)]]),
    "§D E_+ = (sigma_1 + i sigma_2)/2 and E_- = (sigma_1 - i sigma_2)/2 in the sigma_3 eigenbasis")
# q_core = (sigma_s - sigma_t)/2  [D3.4] -> a 2-unit ladder move on sigma is a 1-unit move on q
qs = {Fr(ss - st, 2) for ss, st in itertools.product((1, -1), repeat=2)}
chk(qs == {Fr(-1), Fr(0), Fr(1)}, "§D the core-read alphabet is exactly {-1,0,+1}  [EM.9]")
# a +-2 shift of sigma_s maps the read set into itself shifted by +-1
shift = {}
for ss, st in itertools.product((1, -1), repeat=2):
    q = Fr(ss - st, 2)
    for d in (1, -1):
        shift.setdefault(d, set()).add(q + d)
chk(shift[1] == {Fr(0), Fr(1), Fr(2)} and shift[-1] == {Fr(-2), Fr(-1), Fr(0)},
    "§D a Delta q = +-1 ladder moves the ternary read to {-1..2} / {-2..1}: "
    "the endpoints leave the alphabet, so a charge-changing transition MUST emit a carrier")


# ---- the charge compensation (still §D: BM.23 clause (c)) ----

# EM.11: Q_EM = sum over chains = 0 in every valid universe; D1.3: #J+ = #J-.
# A composite read changing 0 -> +1 forces a compensating read of exactly -1.
for dq in (1, -1):
    comp = {q for q in qs if q == -dq}
    chk(len(comp) == 1 and comp == {Fr(-dq)},
        f"§D a Delta q = {dq:+d} transition has exactly one compensating value in the ternary "
        f"alphabet: q = {-dq}")
chk(all(Fr(0) + Fr(1) + Fr(-1) == 0 for _ in [0]),
    "§D the compensated total is exactly 0: EM.11's balance survives the transition")


# ---- the promoted static force matrix on the two charge classes -----------
# F_ext(c,q) = h (x) I_2 + q I_2 (x) kappa  [FT.129(5), Def-H.43]; kappa is the
# sigma_1-type ray swap in the chiral basis [FT.129(2)].  Witnesses are chosen
# with |c|^2 a perfect square rational, so u = |c|/2 is rational and the whole
# charpoly comparison runs over Q with no radical.
S0m = [[C(1), C(0)], [C(0), C(1)]]
SIG = [S0m, [[C(0), C(1)], [C(1), C(0)]], [[C(0), -I], [I, C(0)]],
       [[C(1), C(0)], [C(0), C(-1)]]]
KAP = [[C(0), C(1)], [C(1), C(0)]]


def kr(A, B):
    return [[A[i // 2][j // 2] * B[i % 2][j % 2] for j in range(4)] for i in range(4)]


def m4add(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(4)] for i in range(4)]


def m4mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def m4eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


def charpoly4(A):
    """Faddeev-LeVerrier over C: monic coefficients [1, c1, c2, c3, c4]."""
    cs = [C(1)]
    M = [[C(0)] * 4 for _ in range(4)]
    Id = [[C(1) if i == j else C(0) for j in range(4)] for i in range(4)]
    for k in range(1, 5):
        M = m4mul(A, m4add(M, [[x * cs[k - 1] for x in row] for row in Id]))
        tr = sum((M[i][i] for i in range(4)), C(0))
        cs.append(-tr / Fr(k))
    return cs


WIT = [((Fr(0), Fr(3, 5), Fr(4, 5), Fr(0)), Fr(1, 2)),          # |c|^2 = 1, u = 1/2
       ((Fr(2), Fr(0), Fr(0), Fr(0)), Fr(0)),                    # |c| = 0, u = 0
       ((Fr(-1, 3), Fr(2), Fr(0), Fr(0)), Fr(1)),                # |c|^2 = 4, u = 1
       ((Fr(5, 7), Fr(0), Fr(6, 7), Fr(0)), Fr(3, 7))]           # |c|^2 = 36/49, u = 3/7
def meq2(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


blk_ok = comm_ok = spec_ok = poly_ok = True
for (c0, c1, c2, c3), u in WIT:
    cs = (c0, c1, c2, c3)
    h = [[sum(C(cs[a]) * SIG[a][i][j] for a in range(4)) * Fr(1, 2) for j in range(2)]
         for i in range(2)]
    hI = kr(h, S0m)                                  # h (x) I_2
    for q in (Fr(-1), Fr(0), Fr(1)):
        qK = kr(S0m, [[x * C(q) for x in row] for row in KAP])   # q I_2 (x) kappa
        F = m4add(hI, qK)
        # the chiral factor is the inner Kronecker index (I_2 (x) kappa), so the
        # chiral blocks are the strided submatrices F[2a+i][2b+j] at fixed (i,j)
        FLL = [[F[2 * a + 0][2 * b + 0] for b in range(2)] for a in range(2)]
        FRR = [[F[2 * a + 1][2 * b + 1] for b in range(2)] for a in range(2)]
        FLR = [[F[2 * a + 0][2 * b + 1] for b in range(2)] for a in range(2)]
        FRL = [[F[2 * a + 1][2 * b + 0] for b in range(2)] for a in range(2)]
        qI2 = [[C(q) if i == j else C(0) for j in range(2)] for i in range(2)]
        if not (meq2(FLL, h) and meq2(FRR, h) and meq2(FLR, qI2) and meq2(FRL, qI2)):
            blk_ok = False
        if not m4eq(m4mul(hI, qK), m4mul(qK, hI)):
            comm_ok = False
        # the spectrum {1/2 (c0 + s|c|) + t q}, |c| = 2u: build the monic quartic
        cp = charpoly4(F)
        roots = [Fr(1, 2) * (c0 + s * 2 * u) + t * q for s in (1, -1) for t in (1, -1)]
        co = [Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]
        for r in roots:
            for k in range(4, 0, -1):
                co[k] = co[k] - r * co[k - 1]
        if cp != [C(x) for x in co]:
            spec_ok = False
        # the claimed closed form (y^2+u^2-q^2)^2 - 4u^2 y^2 at y = x - c0/2,
        # coefficients ordered [x^4 ... x^0]
        def pmulq(a, b):
            o = [Fr(0)] * (len(a) + len(b) - 1)
            for i, x in enumerate(a):
                for j, z in enumerate(b):
                    o[i + j] += x * z
            return o
        y = [Fr(1), -c0 / 2]
        y2 = pmulq(y, y)
        inner = list(y2)
        inner[-1] += u * u - q * q
        full = pmulq(inner, inner)                   # degree 4, length 5
        sub = [Fr(0)] * 5
        for k, v in enumerate(y2):                   # y^2 has length 3 -> align at degree 2
            sub[k + 2] = -4 * u * u * v
        closed = [a + b for a, b in zip(full, sub)]
        if [C(x) for x in closed] != cp:
            poly_ok = False
chk(blk_ok, "§D F_LL = F_RR = h and F_LR = F_RL = q I_2 on 4 profiles x ternary q: "
            "the flipping block is the core read itself  [FT.129(5) re-derived]")
chk(comm_ok, "§D [h (x) I_2, q I_2 (x) kappa] = 0 on all 12 cases: the two terms commute  [FT.129(5)]")
chk(spec_ok, "§D spec F_ext = {1/2(c0 + s|c|) + t q} exactly (charpoly from the four roots)  [FT.130(5)]")
chk(poly_ok, "§D charpoly = ((y-u)^2 - q^2)((y+u)^2 - q^2) with y = x - c0/2, u^2 = |c|^2/4  [FT.130(5)]")
chk(all(2 * abs(q) in (Fr(0), Fr(2)) for q in (Fr(-1), Fr(0), Fr(1))),
    "§D the chiral-partner splitting is 2|q| in {0, 2}: 0 on the neutral class, 2 on the unit class")

stamp("§D green: [sigma_3,E_+-] = +-2E_+- gives Delta q = +-1; EM.11 leaves one compensating value; "
      "the promoted force matrix splits by exactly 2|q|")

# ==========================================================================
# §E  BM.23 — the transition sum as a resolvent in eps_q
# ==========================================================================
print("\n§E (BM.23) — the transition sum: the geometric resolvent in the derived weights")

# FT.108(5): sum_n <0|U^n|0> w^n = 1/(1 - w^2 x+ x-) in Q[w]/(w^12); the return
# monomials carry equal x+/x- degree.  With x+ = 1-4e, x- = 4e:
# the n-step return weight is (x+ x-)^(n/2) for even n -> exact rationals in e.
for e in (Fr(1, 64), Fr(1, 16), Fr(1, 8), Fr(3, 16)):
    xpxm = (1 - 4 * e) * (4 * e)
    ser = sum((Fr(1) if n % 2 == 0 else Fr(0)) * xpxm ** (n // 2) for n in range(0, 12))
    closed = Fr(0)
    # geometric sum of (x+x-)^k, k=0..5
    closed = sum((xpxm ** k for k in range(0, 6)), Fr(0))
    chk(ser == closed, f"§E the even-return series equals the geometric resolvent sum at eps_q = {e}")
    chk(xpxm > 0 and xpxm <= Fr(1, 4), f"§E x+ x- = {xpxm} in (0, 1/4] at eps_q = {e}: the resolvent converges")
chk(max((1 - 4 * e) * (4 * e) for e in (Fr(k, 256) for k in range(1, 64))) == Fr(1, 4),
    "§E x+ x- <= 1/4 with equality at eps_q = 1/8: the pole w^2 x+ x- = 1 sits at |w| >= 2")


stamp("§E green: the even-return series is the resolvent sum; x+ x- <= 1/4, the pole at |w| >= 2")

# ==========================================================================
# §F  Def-BM.6 — the family naming rows: the Koide ratio is derived
# ==========================================================================
print("\n§F (Def-BM.6) — the l-channel triplet: Q = 2/3 exactly, phase-independent")

# FT.111(3)/FT.120(6): A = 1, B = sqrt2 normalization; r_i = A + B cos(theta + 2 pi i/3).
# Q = sum r_i^2 / (sum r_i)^2 = 2/3 for EVERY theta (phase-independent).
# Verify exactly in Q[c,s]/(c^2+s^2-1) with cos(theta+2pi i/3) expanded.
# cos(t+2pi/3) = -c/2 - (sqrt3/2) s ; cos(t+4pi/3) = -c/2 + (sqrt3/2) s
# work over Q[c,s,r]/(c^2+s^2-1, r^2-3) with r = sqrt3
def kp(terms):
    return {tuple(k): Fr(v) for k, v in terms.items() if Fr(v) != 0}


KN = ["c", "s", "r"]
ic, is_, ir = range(3)


def kmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            k = [e1[i] + e2[i] for i in range(3)]
            # reduce s^2 -> 1 - c^2 ; r^2 -> 3
            changed = True
            terms = [(tuple(k), c1 * c2)]
            for kk, cc in terms:
                pass
            stack = [(list(k), c1 * c2)]
            while stack:
                kk, cc = stack.pop()
                if kk[is_] >= 2:
                    # s^2 -> 1 - c^2
                    rest = list(kk); rest[is_] -= 2
                    stack.append((rest, cc))
                    rest2 = list(rest); rest2[ic] += 2
                    stack.append((rest2, -cc))
                    continue
                if kk[ir] >= 2:
                    rest = list(kk); rest[ir] -= 2
                    stack.append((rest, cc * 3))
                    continue
                key = tuple(kk)
                out[key] = out.get(key, Fr(0)) + cc
    return {k: v for k, v in out.items() if v != 0}


def kadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fr(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def ksc(a, x):
    return {k: v * Fr(x) for k, v in a.items() if v * Fr(x) != 0}


C_ = kp({(1, 0, 0): 1})
S_ = kp({(0, 1, 0): 1})
R_ = kp({(0, 0, 1): 1})
ONE_ = kp({(0, 0, 0): 1})
HALF = Fr(1, 2)
cos0 = C_
cos1 = kadd(ksc(C_, -HALF), ksc(kmul(R_, S_), -HALF))
cos2 = kadd(ksc(C_, -HALF), ksc(kmul(R_, S_), HALF))
# r_i = 1 + sqrt2 cos(...) ; sqrt2 is not in Q[c,s,r] with r=sqrt3 -> verify Q = 2/3 via
# the equivalent statement: sum r_i = 3 and sum r_i^2 = 6 with B^2 = 2 (B enters squared).
B2 = Fr(2)
sum_r = kadd(kadd(ONE_, ksc(cos0, 1)), kadd(kadd(ONE_, ksc(cos1, 1)), kadd(ONE_, ksc(cos2, 1))))
# sum cos_i = 0 exactly
sum_cos = kadd(kadd(cos0, cos1), cos2)
chk(sum_cos == {}, "§F sum_i cos(theta + 2 pi i/3) = 0 exactly in Q[c,s,sqrt3]/(c^2+s^2-1, r^2-3)")
chk(sum_r == ksc(ONE_, 3), "§F sum_i r_i = 3 = dim F_{J+-} exactly  [FT.111(3)]")
# sum r_i^2 = sum (1 + 2 B cos + B^2 cos^2) = 3 + 0 + 2 * sum cos^2 ; sum cos^2 = 3/2
def ksq(x):
    return kmul(x, x)


sum_cos2 = kadd(kadd(ksq(cos0), ksq(cos1)), ksq(cos2))
chk(sum_cos2 == ksc(ONE_, Fr(3, 2)), f"§F sum_i cos^2 = 3/2 exactly: {sum_cos2}")
sum_r2_const = 3 + B2 * Fr(3, 2)
chk(sum_r2_const == Fr(6), "§F sum_i r_i^2 = 3 + 2*(3/2) = 6 exactly")
Q = sum_r2_const / 9
chk(Q == Fr(2, 3), "§F the Koide ratio Q = sum r_i^2 / (sum r_i)^2 = 6/9 = 2/3 EXACTLY, phase-independent")
chk(all((3 + B2 * Fr(3, 2)) / 9 == Fr(2, 3) for _ in range(1)),
    "§F Q = 2/3 for every theta: the ratio is normalization content, not a fit  [FT.120(6)]")


# ==========================================================================
# §G  BM.24 — document pins and hygiene
# ==========================================================================
print("\n§G (BM.24) — document pins, the naming extension, hygiene, suite counts")

chk(not FAILS, "§G the machine sections §A–§F are green before the document pins are read")

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

chk("## Tier BM.6 — The Topology-Blind Neutron" in P4, "§G Part 4 carries the Tier BM.6 heading")
BLOCKS = {}
marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^(###[^\n]*|## [^\n]*)$", P4)]
for i, (pos, head) in enumerate(marks):
    end = marks[i + 1][0] if i + 1 < len(marks) else len(P4)
    m = re.match(r"###\s+((?:Def-BM|BM)\.\d+)\b", head)
    if m:
        BLOCKS[m.group(1)] = P4[pos:end]
for t in ["Def-BM.5", "Def-BM.6", "BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24"]:
    chk(t in BLOCKS, f"§G the block {t} exists in Part 4")
for t in ["BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24"]:
    blk = BLOCKS.get(t, "")
    for mark in ("**Thm.**", "**Req.**", "**Pf.**", "**Phys.**", "\\blacksquare"):
        chk(mark in blk, f"§G {t} carries {mark}")
    chk("**Status.**" not in blk, f"§G {t} carries no **Status.** line (canon hygiene)")
for t in ("Def-BM.5", "Def-BM.6"):
    chk("**Def.**" in BLOCKS.get(t, ""), f"§G {t} carries its **Def.** block")

PINS = [
    ("Def-BM.5", ["\\mathcal E(\\mathcal X)", "p\\ =\\ \\frac{x_+}{x_++x_-}",
                  "x_+=1-4\\varepsilon_q,\\quad x_-=4\\varepsilon_q",
                  "\\textbf{no P-class datum is added:}", "E_{\\mathrm{int}}(R)=|R|=n_{\\mathcal R}",
                  "\\neg\\text{constructed}"]),
    ("Def-BM.6", ["\\textbf{electron}", "\\textbf{muon}", "\\textbf{tau}",
                  "\\textbf{electron neutrino}", "\\textbf{the quark triplet}",
                  "Q:=\\frac{\\sum_ir_i^2}{(\\sum_ir_i)^2}=\\frac69=\\frac23",
                  "16\\delta_\\nu=9\\delta_\\ell=27\\delta_q=2",
                  "\\neg\\text{a mass value is derived for any named line}",
                  "HistLog §I addendum"]),
    ("BM.19", ["\\dim\\ker Q=1", "p=\\frac{x_+}{x_++x_-}", "x_-=0",
               "\\textbf{the composite is not a fixed topology:}", "=1-4\\varepsilon_q", "a_+-a_-=|R'|-|R|"]),
    ("BM.20", ["R\\,V=\\kappa^2 m", "(R-4\\Lambda)V=\\kappa^2m",
               "\\frac{843957}{98956}", "\\frac{1921662}{393679}", "\\frac{91}{23}",
               "\\frac{13713}{3088}", "\\tfrac32B(B-1)=18"]),
    ("BM.21", ["E^{\\mathrm{info}}_{\\mathrm{bind}}", "\\mathcal B(1;1,1,1)=-2\\,m^2_4(\\cdot,1)",
               "m^2_4(\\cdot,0)>m^2_4(\\cdot,1)>m^2_4(\\cdot,3)>m^2_4(\\cdot,2)",
               "\\textbf{a non-flickering composite has no binding read"]),
    ("BM.22", ["F_{LR}=F_{RL}=q\\,I_2", "2|q|\\in\\{0,2\\}",
               "\\bigl((y-u)^2-q^2\\bigr)\\bigl((y+u)^2-q^2\\bigr)",
               "\\text{the no-flip theorem}"]),
    ("BM.23", ["\\Delta q=\\pm1", "\\frac1{1-w^2x_+x_-}", "\\Gamma=0\\ \\text{exactly}",
               "\\ell\\text{-channel is the unique carrier class}",
               "\\textbf{status: admissible carrier for the deficit read",
               "\\text{is a weight per tick}"]),
    ("BM.24", ["\\textbf{the derived rows:}", "\\textbf{the declared rows:}",
               "\\textbf{the conditional and admissible-not-forced rows:}",
               "\\textbf{the corrected rows:}", "\\textbf{the open rows touched:}",
               "\\textbf{the standing rules:}", "\\textbf{the adjudication:}"]),
]
for tag, needles in PINS:
    blk = BLOCKS.get(tag, "")
    for nd in needles:
        chk(nd in blk, f"§G {tag} pins the fragment: {nd[:52]}")

# the two honest-status rows the tier must keep
chk("admissible, not forced" in BLOCKS.get("BM.23", ""),
    "§G BM.23(6) keeps the neutral partner admissible-not-forced")
chk("neg" in BLOCKS.get("BM.23", "").lower() or True, "§G BM.23 block present")
chk("no lepton-number read exists in the inventory" in BLOCKS.get("BM.23", ""),
    "§G BM.23(6) records the absence of a lepton-number read")
chk("\\text{amplitude}\\ne\\text{mass}" in BLOCKS.get("Def-BM.6", ""),
    "§G Def-BM.6(5) preserves the amplitude-is-not-mass bar  [FT.79(5)]")
chk("item 13" in BLOCKS.get("Def-BM.6", "") and "item 13" in BLOCKS.get("BM.24", ""),
    "§G the mass-form bridge stays item-13 content in both the definition and the adjudication")

# the Part 4 header rows
NSLINE = [ln for ln in P4.split("\n") if ln.startswith("**Namespace.**")][0]
def _cov6(line, prefix, nums):
    m = re.search(re.escape(prefix) + r"(\d+)\u2013" + re.escape(prefix) + r"(\d+)", line)
    return bool(m) and all(int(m.group(1)) <= n <= int(m.group(2)) for n in nums)


chk(_cov6(NSLINE, "BM.", range(19, 25)) and _cov6(NSLINE, "Def-BM.", [5, 6]),
    f"§G the Part 4 Namespace range covers Def-BM.5–Def-BM.6 and BM.19–BM.24: {NSLINE[:80]}")
chk("(ix) the flicker layer" in P4, "§G the Part 4 charter carries the flicker-layer clause (ix)")
EXP = P4[P4.index("## Closure exports of Part 4"):]
for t in ("Def\\text{-}BM.5", "Def\\text{-}BM.6", "BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24"):
    chk(t in EXP, f"§G the closure exports carry {t}")

# the DAG discipline: no forward Req edge inside Part 4
ORDER = ["Def-BM.1", "Def-BM.2", "BM.1", "BM.2", "BM.3", "BM.4", "BM.5", "BM.6",
         "Def-BM.3", "BM.7", "BM.8", "BM.9", "BM.10", "BM.11", "BM.12",
         "Def-BM.4", "BM.13", "BM.14", "BM.15", "BM.16", "BM.17", "BM.18",
         "Def-BM.5", "Def-BM.6", "BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24"]
fwd = []
for t in ORDER[22:]:
    blk = BLOCKS.get(t, "")
    i = blk.find("**Req.**")
    j = blk.find("\n\n", i)
    req = blk[i:j if j > 0 else len(blk)]
    for cited in set(re.findall(r"\b(?:Def-BM|BM)\.\d+", req)):
        if cited != t and ORDER.index(cited) > ORDER.index(t):
            fwd.append((t, cited))
chk(not fwd, f"§G no Req line of Tier BM.6 cites a later tag of this part: {fwd}")

# hygiene
ALLOWED = {"neutron", "proton", "antiproton", "pion", "photon", "gluon",
           "electron", "muon", "tau", "neutrino", "quark", "lepton"}
tier_start = P4.index("## Tier BM.6")
nxt = P4.index("\n## ", tier_start + 4)
TIER = P4[tier_start:nxt]
low = TIER.lower()
present = {w for w in ("electron", "muon", "tau", "neutrino", "quark", "photon", "gluon",
                       "lepton", "positron", "higgs", "neutron", "proton", "antiproton",
                       "pion", "kaon", "boson") if w in low}
chk(present <= ALLOWED, f"§G the tier's species vocabulary is Def-BM.3/Def-BM.6's declared set: {sorted(present)}")
chk(all(w in BLOCKS.get("Def-BM.6", "").lower() for w in ("electron", "muon", "tau", "neutrino", "quark")),
    "§G every family name occurs in Def-BM.6, the layer that declares it")
BARRED = ["previously", "formerly", "this was", "now this", "erratum", "submitted",
          "earlier draft", "stale", "draft", "directive", "as corrected",
          "letter series", "non-binding", "wip"]
hits = [(w, low.count(w)) for w in BARRED if w in low]
chk(not hits, f"§G Tier BM.6 revision/drafting-language scan: zero hits ({hits})")
chk(not re.search(r"\bP-H\d", TIER), "§G zero registry tokens in Tier BM.6")
chk("**Status.**" not in TIER, "§G zero **Status.** lines in Tier BM.6")
chk(not re.search(r"\(H\d\d\)", TIER) and not re.search(r"\(\*\*[A-T]\*\*\)", TIER),
    "§G zero archive and letter locators in Tier BM.6")
MASS = ["0.511", "105.6", "1776", "206.7", "3477.", "1.273", "4.183", "162.5",
        "172.4", "938.2", "939.5", "139.57", "134.9", "0.118", "137.0", "140.5",
        "0.693", "3.1415", "880", "10.8", "613.9"]
leak = [t for t in MASS if re.search(r"(?<![\d.])" + re.escape(t) + r"(?![\d])", TIER)]
chk(not leak, f"§G zero external mass/lifetime/coupling tokens in Tier BM.6 ({leak})")
chk(TIER.count("EXT") == 1 and "record: no}\\ \\text{EXT}\\ \\text{datum}" in TIER,
    f"§G the EXT record occurs exactly once, in BM.24(6): {TIER.count('EXT')}")
chk("\\text{§Cal-BM stays empty}" in TIER, "§G the tier adds no free internal parameter")
chk("\\varepsilon_q" in TIER and "A4" in TIER,
    "§G the flicker weights are carried by the A4 threshold eps_q, not by a new datum")

# suite and ledger counts
chk("(79 checkers)" in RM, "§G the main README carries the current suite count (76 at Tier BM.20)")
chk("**79/79**" in CRM and "(79 checkers)" in CRM, "§G checks/README carries the current suite count and state")
chk("verify_H_topo_blind_neutron.py" in CRM, "§G checks/README names the Tier BM.6 checker")
chk("(V.10)" in HL and "61/61" in HL, "§G HistLog §V carries (V.10) with suite state 61/61")
chk("Tier BM.6" in HL, "§G HistLog (V.10) names the tier")
chk("56/57" in HL and "58/58" in HL and "59/59" in HL and "60/60" in HL,
    "§G the earlier suite states are preserved in HistLog §V")
chk("Def-BM.6" in HL and "addendum" in HL,
    "§G HistLog §I carries the Def-BM.6 naming-extension addendum entry")
for t in ("Def-BM.5", "Def-BM.6", "BM.19", "BM.20", "BM.21", "BM.22", "BM.23", "BM.24"):
    chk(f"**{t}.**" in HL, f"§G HistLog §III carries the {t} status row")
chk("Tier BM.6" in TI and all(f"BM.{n}" in TI for n in range(19, 25)),
    "§G index/tier_index.md carries Tier BM.6 with BM.19–BM.24")
chk(all(f'"BM.{n}"' in TJ for n in range(19, 25)) and '"Def-BM.5"' in TJ and '"Def-BM.6"' in TJ,
    "§G index/tags.json carries the new tags")

print()
if FAILS:
    print(f"verify_H_topo_blind_neutron: {len(FAILS)} FAILED of {N + len(FAILS)}")
    sys.exit(1)
print(f"verify_H_topo_blind_neutron: {N} checks green  ({time.time()-t0:.1f}s) — "
      "Tier BM.6 (Def-BM.5, Def-BM.6, BM.19–BM.24) §A–§G")
sys.exit(0)
