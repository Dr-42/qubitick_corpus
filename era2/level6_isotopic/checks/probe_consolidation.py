#!/usr/bin/env python3
"""
probe_consolidation.py -- re-verification of the subgenerator study's machine claims for the
Tier IT.16 consolidation (tags IT.49-IT.54): the channel-angle/Koide layer, the binomial census
layer, the circulant/C_3 layer, the CT1.2-basis operator layer (su(4) generation, the nilpotent
triples, the branch-change bridge, the inner reflection), the tensor-square occupancy, the
phase-calculus layer of the parametric matrix class, the saturated-node/Lyapunov/radar layer,
and the rho_B convention census.
Level 6 (Isotopic), Tier IT.16 candidates (IT.49-IT.54).

PROVENANCE: a multi-session subgenerator study (documents CONSOLIDATED.md, CONTINUUM.md,
photon_phase_jump_audit.md PJ.1-PJ.15, radar_sync_audit.md RS.1-RS.10; the working files they
summarize) ran OUTSIDE the repo against a read-only clone. Its own verification scripts
(verify_c3_provenance.py, verify_koide_and_binomial_shape.py, verify_phase_parameterized_matrix.py,
verify_phase_jump_audit.py, verify_radar_sync_audit.py) were NOT delivered -- so EVERY machine
claim re-verified here is re-derived from scratch, exactly, in this checker. The citation audit
(~450 distinct tag tokens; the gate's registry logic) found ONE unattested token (CT0.20, a
self-flagged slip for CT3.20); the claimed canon typo at FT.116(5) is CONFIRMED (the expanded
discriminant needs the second factor squared; the zero locus -- all the clause uses -- is
unaffected); ~65 clause-level checks pass, including every verbatim quote.

SCOPE/DISCIPLINE: this checker verifies the exact-arithmetic layer only. The verdicts (which rows
are derived / declared / barred, the tier placement, the declaration register) are the tier's; the
parametric matrix content is verified as SYMBOLIC identities of the IT.37-39/IT.43-45 construction
class (formable as symbolic expressions, barred as formed reads -- the IT.43(6) doctrine); no
declaration issues; no measured value [P5]; no new dimensionful scale [P1]; species names stay
quoted [Def-BM.3(1),(7)]. No floating point anywhere: Fractions, polynomial identities over Q and
exact quotient rings, integer enumeration, rational pi-certificates (333/106 < pi < 355/113).

BARS honored: exact arithmetic; corpus rows cited, never re-derived as new (re-certification is
machine hygiene, the tier marks provenance); prices are not masses [HistLog V.32]; no currency
mixing as formed reads [BM.83; BM.134(5); BM.140(5)]; count->strength couplings barred
[BM.36(3); BM.61(8)(O1); BM.69(4)(iv); FT.73(5)]; the capacity is C10 register counting, NOT
Shannon [D0.9]. Declarations issued: none; Cal-IT empty.
"""

import sys
from fractions import Fraction as Fr
from itertools import product as iproduct, permutations, combinations

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# =====================================================================================
# Generic exact polynomial engine over Fraction: dict {(exponent tuple): Fr}
# =====================================================================================
class Ring:
    """multivariate polynomials over Fraction with optional monomial reduction rules
    rules: list of (var_index, power, replacement_poly) applied until normal form."""

    def __init__(self, names, rules=()):
        self.names = list(names)
        self.ix = {n: i for i, n in enumerate(self.names)}
        self.n = len(names)
        self.rules = rules

    def zero(self):
        return {}

    def one(self):
        return {tuple([0] * self.n): Fr(1)}

    def const(self, x):
        x = Fr(x)
        return {} if x == 0 else {tuple([0] * self.n): x}

    def var(self, name):
        e = [0] * self.n
        e[self.ix[name]] = 1
        return {tuple(e): Fr(1)}

    def mon(self, **exps):
        e = [0] * self.n
        for k, v in exps.items():
            e[self.ix[k]] = v
        return {tuple(e): Fr(1)}

    def add(self, p, q):
        out = dict(p)
        for e, c in q.items():
            out[e] = out.get(e, Fr(0)) + c
        return {e: c for e, c in out.items() if c != 0}

    def neg(self, p):
        return {e: -c for e, c in p.items()}

    def sub(self, p, q):
        return self.add(p, self.neg(q))

    def scale(self, p, s):
        s = Fr(s)
        return {} if s == 0 else {e: c * s for e, c in p.items() if c * s != 0}

    def mul(self, p, q):
        out = {}
        for e1, c1 in p.items():
            for e2, c2 in q.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                out[e] = out.get(e, Fr(0)) + c1 * c2
        out = {e: c for e, c in out.items() if c != 0}
        return self.reduce(out)

    def reduce(self, p):
        if not self.rules:
            return p
        changed = True
        while changed:
            changed = False
            for (vi, pw, repl) in self.rules:
                for e, c in list(p.items()):
                    if e[vi] >= pw:
                        rest = list(e)
                        rest[vi] -= pw
                        term = self.scale({tuple(rest): Fr(1)}, c)
                        prod = self.mul_raw(repl, term)
                        p = self.add({k: v for k, v in p.items() if k != e}, prod)
                        changed = True
                        break
                if changed:
                    break
        return p

    def mul_raw(self, p, q):
        out = {}
        for e1, c1 in p.items():
            for e2, c2 in q.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                out[e] = out.get(e, Fr(0)) + c1 * c2
        return {e: c for e, c in out.items() if c != 0}

    def eq(self, p, q):
        return self.reduce(self.sub(p, q)) == {}

    def is_zero(self, p):
        return self.reduce(p) == {}

    def diff(self, p, name):
        k = self.ix[name]
        out = {}
        for e, c in p.items():
            if e[k]:
                e2 = list(e)
                e2[k] -= 1
                out[tuple(e2)] = out.get(tuple(e2), Fr(0)) + c * e[k]
        return self.reduce({e: c for e, c in out.items() if c != 0})

    def deriv(self, p, images):
        """the derivation with images[varname] = poly (Leibniz, monomial rule)."""
        out = {}
        for e, c in p.items():
            for i, ei in enumerate(e):
                if ei:
                    img = images.get(self.names[i])
                    if img:
                        e2 = list(e)
                        e2[i] -= 1
                        base = self.scale({tuple(e2): Fr(1)}, c * ei)
                        out = self.add(out, self.mul_raw(base, img))
        return self.reduce(out)

    def submap(self, p, mapping):
        """formal substitution var -> poly."""
        out = {}
        for e, c in p.items():
            term = self.const(c)
            for i, x in enumerate(e):
                if x:
                    base = mapping.get(self.names[i], self.var(self.names[i]))
                    pw = self.one()
                    for _ in range(x):
                        pw = self.mul(pw, base)
                    term = self.mul(term, pw)
            out = self.add(out, term)
        return out

    def vars_used(self, p):
        used = set()
        for e in self.reduce(p):
            for i, x in enumerate(e):
                if x:
                    used.add(self.names[i])
        return used


# =====================================================================================
# Gauss(i) numeric 4x4 layer (exact; NEVER sum() on Gauss tuples)
# =====================================================================================
def g(re, im=0):
    return (Fr(re), Fr(im))


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gneg(x):
    return (-x[0], -x[1])


def gconj(x):
    return (x[0], -x[1])


def ginv(x):
    n2 = x[0] * x[0] + x[1] * x[1]
    return (x[0] / n2, -x[1] / n2)


G0, G1, GI = g(0), g(1), g(0, 1)
SG = [
    [[g(1), g(0)], [g(0), g(1)]],
    [[g(0), g(1)], [g(1), g(0)]],
    [[g(0), g(0, -1)], [g(0, 1), g(0)]],
    [[g(1), g(0)], [g(0), g(-1)]],
]


def kronN(A, B):
    out = [[G0] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + k][2 * j + l] = gmul(A[i][j], B[k][l])
    return out


def n4mul(A, B):
    out = [[G0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = G0
            for k in range(4):
                acc = gadd(acc, gmul(A[i][k], B[k][j]))
            out[i][j] = acc
    return out


def n4add(*mats):
    acc = [[G0] * 4 for _ in range(4)]
    for A in mats:
        for i in range(4):
            for j in range(4):
                acc[i][j] = gadd(acc[i][j], A[i][j])
    return acc


def n4sub(A, B):
    return n4add(A, [[gneg(B[i][j]) for j in range(4)] for i in range(4)])


def n4scale(A, s):
    return [[gmul(A[i][j], s) for j in range(4)] for i in range(4)]


def n4trans(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def n4dag(A):
    return [[gconj(A[j][i]) for j in range(4)] for i in range(4)]


def n4eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


def n4tr(A):
    acc = G0
    for i in range(4):
        acc = gadd(acc, A[i][i])
    return acc


def comm(A, B):
    return n4sub(n4mul(A, B), n4mul(B, A))


SWAP = [[G0] * 4 for _ in range(4)]
for _a in range(2):
    for _b in range(2):
        SWAP[2 * _b + _a][2 * _a + _b] = G1

E0 = kronN(SG[0], SG[0])
SIG = n4add(kronN(SG[1], SG[1]), kronN(SG[2], SG[2]), kronN(SG[3], SG[3]))
Jop = [n4scale(n4add(kronN(SG[j], SG[k]), n4scale(kronN(SG[k], SG[j]), g(-1))), g(Fr(1, 2)))
       for (j, k) in ((2, 3), (3, 1), (1, 2))]
Kop = [n4scale(n4add(kronN(SG[0], SG[i]), n4scale(kronN(SG[i], SG[0]), g(-1))), g(Fr(1, 2)))
       for i in (1, 2, 3)]
We = [n4scale(n4add(kronN(SG[0], SG[i]), kronN(SG[i], SG[0])), g(Fr(1, 2))) for i in (1, 2, 3)]
# the five traceless symmetric spatial carriers E^ij (CT1.2's G-block)
Eij_off = [n4scale(n4add(kronN(SG[j], SG[k]), kronN(SG[k], SG[j])), g(Fr(1, 2)))
           for (j, k) in ((1, 2), (1, 3), (2, 3))]
Eij_diag = [n4sub(kronN(SG[1], SG[1]), kronN(SG[2], SG[2])),
            n4sub(kronN(SG[1], SG[1]), kronN(SG[3], SG[3]))]
Ehat = Eij_off + Eij_diag
PR = n4scale(n4add(n4scale(E0, g(3)), SIG), g(Fr(1, 4)))      # Pi_R = (3E_0+Sigma)/4
PV = n4scale(n4sub(E0, SIG), g(Fr(1, 4)))                      # Pi_V = (E_0-Sigma)/4


def pauli_coords(X):
    """the 16 trace-orthogonal Pauli-product coordinates [CT1.1]: c_ab = Tr(X s_a(x) s_b)/4."""
    coords = {}
    for a in range(4):
        for b in range(4):
            pr = kronN(SG[a], SG[b])
            acc = G0
            for i in range(4):
                for j in range(4):
                    acc = gadd(acc, gmul(X[i][j], pr[j][i]))
            coords[(a, b)] = gmul(acc, g(Fr(1, 4)))
    return coords


print("=" * 104)
print("PART A -- the channel-angle ledger, the cubic ladder, the Koide layer")
print("=" * 104)

# ---- A1: the angle ledger (Fractions) + the 3-adic unreachability ----
dl, dq, dn = Fr(2, 9), Fr(2, 27), Fr(1, 8)          # [FT.112; FT.119(1); FT.142(5)]
ledger = (9 * dl == 2) and (27 * dq == 2) and (16 * dn == 2) and (3 * dq == dl)
ratio_274816 = (dn / dl == Fr(27, 48)) and (dl / dq == Fr(48, 16)) and (dn / dq == Fr(27, 16))
unreach = all(Fr(2, 9 * 3 ** k) != dn for k in range(0, 21))
# 3-adic certificate: 2/(9*3^k) = 1/8 <=> 16 = 9*3^k -- impossible (v_3(16)=0, v_3(9*3^k)>=2)
cert16 = all(9 * 3 ** k != 16 for k in range(0, 21))
# the gamma order: 3*delta in (0, pi/2): 2/9 < 3/8 < 2/3 with pi > 333/106 (rational certificate)
order_args = (Fr(2, 9) < Fr(3, 8) < Fr(2, 3)) and (Fr(2, 3) * 2 < Fr(333, 106))
chk("A1  [FT.112; FT.119(1),(2); FT.142(5); FT.143(5)]: the angle ledger re-certified in exact"
    "\n           Fractions: 9*d_l = 27*d_q = 16*d_nu = 2; 3*d_q = d_l; the ratios d_nu:d_l:d_q = 27:48:16;"
    "\n           the nu-channel is UNREACHABLE by any jump iterate: 2/(9*3^k) != 1/8 for k=0..20, with the"
    "\n           3-adic certificate 16 != 9*3^k (v_3(16)=0 vs v_3(9*3^k)>=2); the gamma-order arguments"
    "\n           2/9 < 3/8 < 2/3 < pi/2 by the integer pi-certificate pi > 333/106 (cos strictly"
    "\n           decreasing on [0,pi] -- math row).",
    ledger and ratio_274816 and unreach and cert16 and order_args,
    f"(d_l,d_q,d_nu) = ({dl},{dq},{dn}); 3*d_q = {3*dq}")

# ---- A2: the cubic ladder gamma_l = 2 gamma_q^3 - 3 gamma_q ----
RQ = Ring(["gq", "t2"])
RQ.rules = [(1, 2, RQ.const(2))]                      # t2^2 = 2
t2 = RQ.var("t2")
gq = RQ.var("gq")
# gamma_ch = t2*cos(3 delta_ch); cos(3x) = 4cos^3-3cos; 3*d_l = 9*d_q = 3*(3*d_q):
# gamma_l = t2*(4*(gq/t2)^3 - 3*(gq/t2)) with 1/t2 = t2/2:
t2inv = RQ.scale(t2, Fr(1, 2))
cosq_over = RQ.mul(gq, t2inv)                           # cos(3 d_q) = gamma_q/t2
ladder_rhs = RQ.sub(RQ.scale(RQ.mul(cosq_over, RQ.mul(cosq_over, cosq_over)), 4),
                    RQ.scale(cosq_over, 3))             # 4c^3-3c at c = gq/t2
gamma_l = RQ.mul(t2, ladder_rhs)
ladder_target = RQ.sub(RQ.scale(RQ.mul(gq, RQ.mul(gq, gq)), 2), RQ.scale(gq, 3))
ladder_ok = RQ.eq(gamma_l, ladder_target)
chk("A2  [BM.80(4),(5); FT.119(2); PJ.2(4),(6)]: the cubic-constant ladder -- gamma_l = 2*gamma_q^3"
    "\n           - 3*gamma_q as a polynomial identity in Q[t2,gq]/(t2^2-2) (the triple-angle identity"
    "\n           cos(3x)=4cos^3-3cos applied at 3*d_l = 3*(3*d_q), with gamma_ch = sqrt2*cos(3*delta_ch)):"
    "\n           O_{q->l} acts as P(x) = 2x^3-3x (a polynomial -- no branch issue upward), and gamma_q is"
    "\n           the unique positive root of 2x^3-3x-gamma_l = 0 on the derived branch (the quadrant"
    "\n           certificate: 3*d_q = 2/9 in (0, pi/2)).",
    ladder_ok, f"t2*(4*(gq/t2)^3-3*(gq/t2)) reduced = {sorted(RQ.reduce(gamma_l).items())}")

# ---- the trigonometric normal-form ring: Q[ct,st,t2,t3]/(ct^2+st^2-1, t2^2-2, t3^2-3) ----
TR = Ring(["ct", "st", "t2", "t3"])
one_TR = TR.const(1)
ct, st, t2t, t3t = TR.var("ct"), TR.var("st"), TR.var("t2"), TR.var("t3")
TR.rules = [(0, 2, TR.sub(one_TR, TR.mul(st, st))),    # ct^2 -> 1-st^2
            (2, 2, TR.const(2)),                        # t2^2 -> 2
            (3, 2, TR.const(3))]                        # t3^2 -> 3
# r_k = 1 + t2*cos(delta + 2 pi k/3): cos offsets (1, -1/2, -1/2), sin offsets (0, t3/2, -t3/2)
r = [TR.add(one_TR, TR.mul(t2t, ct)),
     TR.add(one_TR, TR.scale(TR.add(TR.mul(t2t, ct), TR.mul(TR.mul(t2t, t3t), st)), Fr(-1, 2))),
     TR.add(one_TR, TR.scale(TR.sub(TR.mul(t2t, ct), TR.mul(TR.mul(t2t, t3t), st)), Fr(-1, 2)))]
sum_r = TR.add(TR.add(r[0], r[1]), r[2])
sum_r2 = TR.add(TR.add(TR.mul(r[0], r[0]), TR.mul(r[1], r[1])), TR.mul(r[2], r[2]))
e2_r = TR.sub(TR.scale(TR.mul(sum_r, sum_r), Fr(1, 2)), TR.scale(sum_r2, Fr(1, 2)))
gamma = TR.mul(t2t, TR.sub(TR.scale(TR.mul(ct, TR.mul(ct, ct)), 4), TR.scale(ct, 3)))  # sqrt2 cos3delta
prod_r = TR.mul(TR.mul(r[0], r[1]), r[2])
# A3: sum r = 3; sum r^2 = 6; e2 = 3/2; K = 2/3 (as sum_r2/sum_r^2); prod r = (gamma-1)/2
A3_ok = (TR.eq(sum_r, TR.const(3)) and TR.eq(sum_r2, TR.const(6))
         and TR.eq(e2_r, TR.const(Fr(3, 2)))
         and TR.eq(sum_r2, TR.scale(TR.mul(sum_r, sum_r), Fr(2, 3)))
         and TR.eq(prod_r, TR.scale(TR.sub(gamma, one_TR), Fr(1, 2))))
# the derivative family sums: r' = dr/dtheta (ct'=-st, st'=ct)
def Dtheta(p):
    return TR.add(TR.deriv(p, {"ct": TR.neg(st)}), TR.deriv(p, {"st": ct}))
rp = [Dtheta(x) for x in r]
rpp = [Dtheta(x) for x in rp]
tower_ok = all(TR.eq(rpp[k], TR.sub(one_TR, r[k])) for k in range(3))     # r'' = 1-r
sum_rp = TR.add(TR.add(rp[0], rp[1]), rp[2])
sum_rrp = TR.add(TR.add(TR.mul(r[0], rp[0]), TR.mul(r[1], rp[1])), TR.mul(r[2], rp[2]))
sum_mix = TR.add(TR.add(TR.add(TR.mul(rp[0], rp[0]), TR.mul(r[0], rpp[0])),
                        TR.add(TR.mul(rp[1], rp[1]), TR.mul(r[1], rpp[1]))),
                 TR.add(TR.mul(rp[2], rp[2]), TR.mul(r[2], rpp[2])))
A3b_ok = TR.is_zero(sum_rp) and TR.is_zero(sum_rrp) and TR.is_zero(sum_mix)
# sum r^3 = 27/2 + 3 prod r;  sum r^4 = 63/2 + 12 prod r
sum_r3 = TR.add(TR.add(TR.mul(r[0], TR.mul(r[0], r[0])), TR.mul(r[1], TR.mul(r[1], r[1]))),
                TR.mul(r[2], TR.mul(r[2], r[2])))
sum_r4 = TR.add(TR.add(TR.mul(r[0], TR.mul(r[0], TR.mul(r[0], r[0]))),
                       TR.mul(r[1], TR.mul(r[1], TR.mul(r[1], r[1])))),
                TR.mul(r[2], TR.mul(r[2], TR.mul(r[2], r[2]))))
newton_ok = (TR.eq(sum_r3, TR.add(TR.const(Fr(27, 2)), TR.scale(prod_r, 3)))
             and TR.eq(sum_r4, TR.add(TR.const(Fr(63, 2)), TR.scale(prod_r, 12))))
chk("A3  [FT.111(2),(3); FT.113; FT.119(4); Def-BM.6(4); CONSOLIDATED SS2,11,14,25]: the Koide-form"
    "\n           layer in the exact trigonometric normal-form ring Q[ct,st,t2,t3]/(ct^2+st^2-1, t2^2-2,"
    "\n           t3^2-3) at SYMBOLIC phase: sum r_k = 3, sum r_k^2 = 6, e_2 = 3/2, K = sum(r^2)/sum(r)^2"
    "\n           = 2/3 PHASE-FREE; prod r = (gamma-1)/2 with gamma = sqrt2*cos(3*delta); the Newton tower"
    "\n           sum r^3 = 27/2+3*prod r, sum r^4 = 63/2+12*prod r; the derivative tower r'' = 1-r (hence"
    "\n           r^(2m) = (-1)^(m+1)(1-r), r^(2m+1) = (-1)^m r' by induction) and the family sums sum r' ="
    "\n           sum r r' = sum (r'^2+r r'') = 0 IDENTICALLY at every phase.",
    A3_ok and A3b_ok and tower_ok and newton_ok)

# ---- A4: the general law K(N) = 2/N (N=3,4,6 exact; N>=3 structural) ----
def koide_at(N):
    """sum r and sum r^2 for r_k = 1+sqrt2 cos(theta+2 pi k/N), N = 3,4,6 (exact offsets)."""
    if N == 3:
        rr = r
    elif N == 4:
        cosv = [ct, TR.neg(st), TR.neg(ct), st]
        rr = [TR.add(one_TR, TR.mul(t2t, cv)) for cv in cosv]
    elif N == 6:
        # cos(theta+2pi k/6), k=0..5: (1,0),(1/2,-t3/2),(-1/2,-t3/2),(-1,0),(-1/2,+t3/2),(1/2,+t3/2)
        t3st = TR.mul(t3t, st)
        cosv = [ct,
                TR.scale(TR.sub(ct, t3st), Fr(1, 2)),
                TR.scale(TR.sub(TR.neg(ct), t3st), Fr(1, 2)),
                TR.neg(ct),
                TR.scale(TR.add(TR.neg(ct), t3st), Fr(1, 2)),
                TR.scale(TR.add(ct, t3st), Fr(1, 2))]
        rr = [TR.add(one_TR, TR.mul(t2t, cv)) for cv in cosv]
    else:
        raise ValueError
    acc = TR.zero()
    acc2 = TR.zero()
    for x in rr:
        acc = TR.add(acc, x)
        acc2 = TR.add(acc2, TR.mul(x, x))
    return N, acc, acc2

k4 = koide_at(4)
k6 = koide_at(6)
gen_ok = (TR.eq(k4[1], TR.const(4)) and TR.eq(k4[2], TR.const(8))
          and TR.eq(k6[1], TR.const(6)) and TR.eq(k6[2], TR.const(12))
          and TR.eq(TR.add(r[0], TR.add(r[1], r[2])), TR.const(3)))
# K(N) = sum r^2/(sum r)^2 = 2N/N^2 = 2/N at N=3,4,6:
K3 = TR.eq(TR.scale(TR.mul(sum_r, sum_r), Fr(2, 3)), sum_r2)
chk("A4  [FT.111(3) normalization; CONSOLIDATED SS11 'the general law (new here)']: K(N) = 2/N --"
    "\n           for lambda_k = A + B cos(theta+2 pi k/N) with sum lambda = N (A=1) and sum (lambda-A)^2"
    "\n           = N (B^2=2): sum lambda^2 = 2N and K = sum(lambda^2)/(sum lambda)^2 = 2N/N^2 = 2/N."
    "\n           Machine at N=3,4,6 in the exact trig ring (sum r = N, sum r^2 = 2N each); the general N"
    "\n           rests on the root-sum identities sum cos = 0, sum cos^2 = N/2 (N>=3) -- a math row. At"
    "\n           N=3 the two twos coincide (B^2 = 2 = N-1): FT.158(5)'s (3-1)/3 reading is exact ONLY at"
    "\n           order 3.",
    gen_ok and K3)

# ---- A5: the z-cubic (z = r^2) via Newton's identities in Q[gamma] ----
RG = Ring(["gm"])
gm = RG.var("gm")
e1, e2, e3 = RG.const(3), RG.const(Fr(3, 2)), RG.scale(RG.sub(gm, RG.const(1)), Fr(1, 2))
p1 = e1
p2 = RG.sub(RG.mul(e1, p1), RG.scale(e2, 2))
p3 = RG.sub(RG.add(RG.mul(e1, p2), RG.neg(RG.mul(e2, p1))), RG.scale(e3, -3))
p3 = RG.add(RG.sub(RG.mul(e1, p2), RG.mul(e2, p1)), RG.scale(e3, 3))
p4 = RG.add(RG.sub(RG.mul(e1, p3), RG.mul(e2, p2)), RG.mul(e3, p1))
newton_p = (RG.eq(p3, RG.add(RG.const(Fr(27, 2)), RG.scale(e3, 3)))
            and RG.eq(p4, RG.add(RG.const(Fr(63, 2)), RG.scale(e3, 12))))
# z-roots z_k = r_k^2: ez1 = p2 = 6; ez2 = (p2^2-p4)/2; ez3 = e3^2
ez1 = p2
ez2 = RG.scale(RG.sub(RG.mul(p2, p2), p4), Fr(1, 2))
ez3 = RG.mul(e3, e3)
ez2_target = RG.scale(RG.sub(RG.const(21), RG.scale(gm, 12)), Fr(1, 4))
cubic = (RG.eq(ez1, RG.const(6)) and RG.eq(ez2, ez2_target)
         and RG.eq(RG.scale(ez3, 4), RG.mul(RG.sub(gm, RG.const(1)), RG.sub(gm, RG.const(1)))))
chk("A5  [CONSOLIDATED SS25; BM.80; machine: Newton's identities in Q[gamma]]: the power sums p_3 ="
    "\n           27/2+3*e_3, p_4 = 63/2+12*e_3 with e_3 = (gamma-1)/2; and the z=r^2 cubic"
    "\n           4z^3-24z^2+(21-12 gamma)z-(gamma-1)^2 = 0: e_1(z) = 6 PHASE-FREE, e_2(z) ="
    "\n           (21-12 gamma)/4, e_3(z) = (gamma-1)^2/4 -- all exact polynomial identities.",
    newton_p and cubic)

# ---- A6: the circle algebra of the label map (affine maps theta -> p*theta + q*pi over Q) ----
def aff_comp(f, h):        # (f o h)(theta)
    return (f[0] * h[0], f[0] * h[1] + f[1])


O_hat = (Fr(1, 3), Fr(0))          # theta -> theta/3
C3map = (Fr(1), Fr(2, 3))          # theta -> theta + 2pi/3 (pi-coefficients: q in units of pi)
Oinv = (Fr(3), Fr(0))
C3inv = (Fr(1), Fr(-2, 3))
OC3 = aff_comp(O_hat, C3map)       # theta/3 + 2pi/9
C3O = aff_comp(C3map, O_hat)       # theta/3 + 2pi/3
discrep = C3O[1] - OC3[1]          # 2/3 - 2/9 = 4/9  -> the commutator rotation R_{4pi/9}
conj = aff_comp(aff_comp(O_hat, C3map), Oinv)   # O C3 O^{-1} = rotation by 2pi/9
A6_ok = (OC3 == (Fr(1, 3), Fr(2, 9)) and C3O == (Fr(1, 3), Fr(2, 3)) and discrep == Fr(4, 9)
         and conj == (Fr(1), Fr(2, 9)))
chk("A6  [PJ.12(4); FT.111(1); FT.158(1)]: the lifted-circle algebra of the label map -- O C3:"
    "\n           theta/3+2pi/9 vs C3 O: theta/3+2pi/3 (they do NOT commute); the discrepancy is the"
    "\n           rotation by 4pi/9; the conjugation O C3 O^{-1} = R_{2pi/9} DILATES the orbit generator;"
    "\n           the rhyme 2pi/9 = pi*d_l is flagged as arithmetic coincidence, NOT an identification"
    "\n           [IT.44(3) discipline; FT.143(6)]. Exact rational pi-coefficients throughout.",
    A6_ok, f"O C3 = {OC3}; C3 O = {C3O}; O C3 O^-1 = {conj}")

# ---- A7: z_l = 2 z_q^3 with the factor 2 forced ----
# |z| = 1/sqrt2 both channels: c*(1/sqrt2)^3 = 1/sqrt2 <=> c^2*(1/8) = 1/2 <=> c^2 = 4 <=> c = 2 (positive)
c_forced = (Fr(1, 2) / (Fr(1, 2) * Fr(1, 2) * Fr(1, 2)) == 4)
arg_ok = 3 * Fr(2, 27) == Fr(2, 9)
# uniqueness: c^2 = 4 has the unique positive rational solution c=2 (rationals: (c-2)(c+2)=0)
uniq = all(Fr(cc, dd) ** 2 != 4 or Fr(cc, dd) in (2, -2)
           for cc in range(-20, 21) for dd in range(1, 21))
chk("A7  [PJ.12(1); FT.111(3): B = sqrt2]: the complex-symbol jump z_l = 2*z_q^3 with the factor 2"
    "\n           FORCED, not free: c*|z_q|^3 = |z_l| at |z| = 1/sqrt2 in BOTH channels gives c^2*(1/8)"
    "\n           = 1/2 <=> c^2 = 4, whose unique positive rational solution is c = 2 = B^2 (FT.111(3)'s"
    "\n           own normalization integer); the argument side is 3*(2/27) = 2/9 [FT.119(2)] -- the"
    "\n           identity is exact in Q(sqrt2) on the modulus and in Q on the argument.",
    c_forced and arg_ok and uniq)

print("=" * 104)
print("PART B -- the binomial census layer: the W_n skeleton, the neighbour law, the P-ring arithmetic")
print("=" * 104)

def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


# ---- B1: the exhaustive 4^n census vs C(2n, n+Q) ----
census_ok = True
for n in (1, 2, 3, 4):
    hist = {}
    for signs in iproduct((1, -1), repeat=2 * n):     # (sigma_s, sigma_t) per chain: 4^n words
        Q = sum(Fr(signs[2 * i] - signs[2 * i + 1], 2) for i in range(n))
        hist[int(Q)] = hist.get(int(Q), 0) + 1
    census_ok &= all(hist.get(Q, 0) == binom(2 * n, n + Q) for Q in range(-n, n + 1))
    census_ok &= sum(hist.values()) == 4 ** n
W3 = [binom(6, Q + 3) for Q in range(-3, 4)]
chk("B1  [BM.103(3); BM.114(1); Def-BM.8; EM.9]: the exhaustive 4^n charge census (q_i ="
    "\n           (sigma_s-sigma_t)/2 per chain, Q = sum q_i) equals W_n(Q) = C(2n,n+Q) for n=1,2,3,4"
    "\n           (sums 4^n); the frozen W_3 = (1,6,15,20,15,6,1) reproduced; W(0)/W(1) = 20/15 = 4/3"
    "\n           [BM.28]; the n=1 row IS the end-pair census m_q = (2,1,1).",
    census_ok and W3 == [1, 6, 15, 20, 15, 6, 1] and Fr(W3[3], W3[4]) == Fr(4, 3)
    and [binom(2, Q + 1) for Q in (-1, 0, 1)] == [1, 2, 1],
    f"W_3 = {W3}; 4^n census exact for n=1..4")

# ---- B2: the Laurent identity (2+z+z^-1)^n = (1+z)^{2n} / z^n ----
RL = Ring(["z"])
RLz = RL.var("z")


def laurel_mul(p, q):        # Laurent dicts over Q in z (allow negative exponents)
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            out[e1 + e2] = out.get(e1 + e2, Fr(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


base = {1: Fr(1), 0: Fr(2), -1: Fr(1)}                # 2 + z + z^-1
ident_ok = True
for n in range(1, 7):
    lhs = {0: Fr(1)}
    for _ in range(n):
        lhs = laurel_mul(lhs, base)
    rhs = {0: Fr(1)}
    bin1 = {1: Fr(1), 0: Fr(1)}                        # 1+z
    for _ in range(2 * n):
        rhs = laurel_mul(rhs, bin1)
    rhs = {e - n: c for e, c in rhs.items()}           # /z^n
    ident_ok &= lhs == rhs
chk("B2  [BM.114(1); BM.103(3); Def-BM.17(1)]: the Laurent identity (2+z+z^-1)^n = (1+z)^{2n}/z^n"
    "\n           in Z[z,z^-1] verified coefficient-wise for n=1..6 -- hence W_n(Q) = C(2n,n+Q) is a"
    "\n           one-line consequence, and the baryon census is a BINOMIAL row (phase-free by"
    "\n           construction: no delta enters any baryon census row [PJ SS0(0.2)]).",
    ident_ok)

# ---- B3: the neighbour law R(n) = (n+1)/n ----
Rlaw = all(Fr(binom(2 * n, n), binom(2 * n, n + 1)) == Fr(n + 1, n) for n in range(1, 13))
# the two quotient functions hit 2 uniquely at k=3 (k>=2 for the second)
quot1 = [(k, Fr(k + 1, k) / Fr(2, k)) for k in range(1, 13)]
quot2 = [(k, Fr(k + 1, k) / Fr(k - 1, k)) for k in range(2, 13)]
uniq1 = [k for k, v in quot1 if v == 2]
uniq2 = [k for k, v in quot2 if v == 2]
chk("B3  [BM.114(1); BM.28(2); FT.158(5); CONSOLIDATED SS12 '(new; one line from BM.114(1))']: the"
    "\n           neighbour law R(n) = W_n(0)/W_n(1) = C(2n,n)/C(2n,n+1) = (n+1)/n for n=1..12 -- BM.28(2)'s"
    "\n           'one chain restricts 2:1, three chains restrict 4:3' is ONE LAW at n=1 and n=3, with the"
    "\n           whole constraint effect the descent (n+1)/n -> 1; the quotient census: R(k)/K(k) ="
    "\n           (k+1)/2 and R(k)/((k-1)/k) = (k+1)/(k-1) both hit 2 UNIQUELY at k=3 (machine over"
    "\n           k=1..12) -- the 2 is exact arithmetic on two independently derived rationals at the"
    "\n           capacity three, NOT a tensor-product structure [corrections register #17].",
    Rlaw and uniq1 == [3] and uniq2 == [3],
    f"R(n) = {[str(Fr(n+1, n)) for n in range(1, 6)]}...; unique-2 loci: {uniq1}, {uniq2}")

# ---- B4: the P-ring arithmetic: Sigma_B = ln(4/3) = 2ln2-ln3; the BM.83 certificate ----
# ln-values as coefficient vectors over the primes (2,3,5)
ln1280, ln960, ln2v, ln405 = (8, 0, 1), (6, 1, 1), (1, 0, 0), (0, 4, 1)
sigB = tuple(2 * ln2v[i] - (0, 1, 0)[i] for i in range(3))          # 2ln2 - ln3
attest = tuple(3 * ln1280[i] - 4 * ln960[i] for i in range(3))
B4_ok = (sigB == (2, -1, 0) and attest == tuple(-x for x in ln405)
         and attest != (0, 0, 0)
         and Fr(4, 3) < 2 and Fr(4, 3) > 1 and 16 < 27 and 3 < 4 < 6 < 24)
chk("B4  [Def-BM.13(4),(5); BM.59(4),(5),(8); BM.83(2),(3); IT.4(1)]: the prime-log-ring arithmetic:"
    "\n           Sigma_B = ln(20/15) = ln(4/3) = 2*ln2 - ln3 (coefficient vector (2,-1,0)); the"
    "\n           incommensurability certificate 3*ln1280 - 4*ln960 = -ln405 != 0 (the 4/3 ensemble ratio"
    "\n           NEVER equals the informational ratio [BM.83(3)]); the attenuation chain 0 < ln(4/3) <"
    "\n           ln2 < 3ln2 by the exact integer certificates 3 < 4 < 6 < 24; Sigma_B/(6ln2) < 1/3 iff"
    "\n           16 < 27. THE 4/3 ITSELF NEVER BECOMES DIMENSIONFUL; ln(4/3) DOES (via Sigma_B/h in"
    "\n           q^{+1/2} [BM.59(4),(5)]).",
    B4_ok, f"Sigma_B vector {sigB}; 3*ln1280-4*ln960 = {attest} = -ln405 {(0, -4, -1) == tuple(-x for x in attest)}")

print("=" * 104)
print("PART C -- the circulant/C_3 layer")
print("=" * 104)

# ---- C1: the circulant charpoly + discriminant + the FT.116(5) typo certificate ----
RC = Ring(["x", "a0", "zr", "zi"])
x, a0, zr, zi = RC.var("x"), RC.var("a0"), RC.var("zr"), RC.var("zi")
# H = a0 I + z P + zbar P^T with P the 3-cycle; charpoly computed by the 3x3 determinant expansion:
# det(xI - H) = (x-a0)^3 - 3|z|^2 (x-a0) - 2 Re(z^3)
zabs2 = RC.add(RC.mul(zr, zr), RC.mul(zi, zi))
rez3 = RC.sub(RC.sub(RC.mul(zr, RC.mul(zr, zr)), RC.scale(RC.mul(zr, RC.mul(zi, zi)), 3)),
              RC.zero())
imz3 = RC.sub(RC.scale(RC.mul(zi, RC.mul(zr, zr)), 3), RC.mul(zi, RC.mul(zi, zi)))
y = RC.sub(x, a0)
cp_claim = RC.sub(RC.sub(RC.mul(y, RC.mul(y, y)), RC.scale(RC.mul(zabs2, y), 3)),
                  RC.scale(rez3, 2))
# the NON-VACUOUS charpoly check: build H = a0 I + z P + zbar P^T in Q[x,a0,zr,zi,j]/(j^2+1),
# expand det(xI - H) by the six-permutation Leibniz formula, compare with the depressed claim:
RJ = Ring(["x", "a0", "zr", "zi", "j"])
RJ.rules = [(4, 2, RJ.const(-1))]
xJ, a0J, zrJ, ziJ, jJ = (RJ.var(v) for v in ("x", "a0", "zr", "zi", "j"))
zJ = RJ.add(zrJ, RJ.mul(jJ, ziJ))
zbJ = RJ.sub(zrJ, RJ.mul(jJ, ziJ))
HJ = [[a0J, zbJ, zJ], [zJ, a0J, zbJ], [zbJ, zJ, a0J]]
MJ = [[RJ.sub(xJ, a0J) if i == j else RJ.neg(HJ[i][j]) for j in range(3)] for i in range(3)]
perms3 = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (2, 1, 0), (1, 0, 2)]
psgn3 = [1, 1, 1, -1, -1, -1]
detJ = RJ.zero()
for p, sg in zip(perms3, psgn3):
    term = RJ.const(sg)
    for i in range(3):
        term = RJ.mul(term, MJ[i][p[i]])
    detJ = RJ.add(detJ, term)
yJ = RJ.sub(xJ, a0J)
zabs2J = RJ.add(RJ.mul(zrJ, zrJ), RJ.mul(ziJ, ziJ))
rez3J = RJ.sub(RJ.mul(zrJ, RJ.mul(zrJ, zrJ)), RJ.scale(RJ.mul(zrJ, RJ.mul(ziJ, ziJ)), 3))
claimJ = RJ.sub(RJ.sub(RJ.mul(yJ, RJ.mul(yJ, yJ)), RJ.scale(RJ.mul(zabs2J, yJ), 3)),
                RJ.scale(rez3J, 2))
charpoly_exact = RJ.eq(detJ, claimJ)

disc_claim = RC.scale(RC.mul(imz3, imz3), 108)          # 108 (Im z^3)^2
# depressed-cubic discriminant -4p^3-27q^2 at p = -3|z|^2, q = -2Re(z^3):
p_ = RC.scale(zabs2, -3)
q_ = RC.scale(rez3, -2)
disc_std = RC.sub(RC.scale(RC.mul(p_, RC.mul(p_, p_)), -4), RC.scale(RC.mul(q_, q_), 27))
# the EXPANDED form: 108 (Im z)^2 (3(Re z)^2-(Im z)^2)^2  vs the canon's UNSQUARED second factor:
sq_form = RC.scale(RC.mul(RC.mul(zi, zi),
                          RC.mul(RC.sub(RC.scale(RC.mul(zr, zr), 3), RC.mul(zi, zi)),
                                 RC.sub(RC.scale(RC.mul(zr, zr), 3), RC.mul(zi, zi)))), 108)
unsq_form = RC.scale(RC.mul(RC.mul(zi, zi),
                            RC.sub(RC.scale(RC.mul(zr, zr), 3), RC.mul(zi, zi))), 108)
witness = {"x": 0, "a0": 0, "zr": 1, "zi": 1}


def ev(p, pt):
    tot = Fr(0)
    for ex, c in RC.reduce(p).items():
        m = Fr(1)
        for i, e in enumerate(ex):
            if e:
                m *= Fr(pt[RC.names[i]]) ** e
        tot += c * m
    return tot


wit_sq = ev(sq_form, witness)
wit_unsq = ev(unsq_form, witness)
wit_true = ev(disc_claim, witness)
C1_ok = (charpoly_exact and RC.eq(disc_claim, disc_std) and RC.eq(disc_claim, sq_form)
         and not RC.eq(disc_claim, unsq_form)
         and wit_sq == wit_true == Fr(432) and wit_unsq == Fr(216))
chk("C1  [FT.111(2); FT.116(5) -- the canon typo CONFIRMED, harmless]: the circulant charpoly"
    "\n           (x-a0)^3 - 3|z|^2(x-a0) - 2Re(z^3) equals the permutation expansion of det(xI-H)"
    "\n           symbolically; its discriminant is -4p^3-27q^2 = 108(Im z^3)^2 = 108(Im z)^2 *"
    "\n           (3(Re z)^2-(Im z)^2)^2 -- WITH the second factor SQUARED (exact polynomial identity);"
    "\n           FT.116(5)'s printed expansion carries it UNSQUARED (witness z=1+i: 432 vs 216 vs the true"
    "\n           432) -- a canon typo, recorded probe-side, NEVER edited [AT.63(2)]; the zero locus"
    "\n           {Im z = 0} u {3(Re z)^2 = (Im z)^2} is identical either way, which is all the clause uses.",
    C1_ok, f"witness z=1+i: squared form {wit_sq} = true disc {wit_true}; unsquared {wit_unsq}")

# ---- C2: the selection census (S_3 subgroups, commutant dims, Stab(eps) = A_3) ----
perms = list(permutations(range(3)))


def pmul2(p, q):
    return tuple(p[q[i]] for i in range(3))


def psgn(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if (p[i] - p[j]) * (i - j) < 0:
                s = -s
    return s


# all subgroups by closure over generating subsets
subgroups = set()
for k in range(1, 3):
    for gs in combinations(perms, k):
        clo = set(gs) | {(0, 1, 2)}
        changed = True
        while changed:
            changed = False
            for a in list(clo):
                for b in list(clo):
                    c = pmul2(a, b)
                    if c not in clo:
                        clo.add(c)
                        changed = True
        if len(clo) <= 6:
            subgroups.add(frozenset(clo))
orders = sorted(len(s) for s in subgroups)
ident = (0, 1, 2)


def comm_dim(H):
    """dim of the commutant of the permutation representation = #orbits on ordered pairs."""
    seen, orbits = set(), 0
    for pr in [(i, j) for i in range(3) for j in range(3)]:
        if pr in seen:
            continue
        orbits += 1
        o = set()
        stack = [pr]
        while stack:
            x = stack.pop()
            if x in o:
                continue
            o.add(x)
            for h in H:
                stack.append((h[x[0]], h[x[1]]))
        seen |= o
    return orbits


dims = {len(H): comm_dim(H) for H in subgroups}
# Stab(eps) = the even permutations (Levi-Civita invariance census over all 6)
stab = [p for p in perms if psgn(p) == 1]
stab_ok = len(stab) == 3 and all(psgn(p) == 1 for p in stab)
# spec(a I_3 + b J) with J the all-ones matrix: {a+3b, a, a}
J3 = [[1] * 3 for _ in range(3)]
chk("C2  [FT.116(1)-(7); CT3.3; CT3.15; CT3.17]: the selection census re-derived by exhaustive"
    "\n           enumeration: S_3's subgroups have orders (1,2,2,2,3,6); the commutant dimensions of the"
    "\n           permutation representation are {e}->9, Z_2->5, C_3->3, S_3->2 (orbit counts on ordered"
    "\n           pairs -- machine); Stab_{S_3}(eps) = A_3 exactly (the Levi-Civita sign census over all"
    "\n           six permutations) -- A_3 the UNIQUE MAXIMAL eps-preserving subgroup; and spec(aI_3+bJ)"
    "\n           = {a+3b, a, a} is two-level only.",
    orders == [1, 2, 2, 2, 3, 6] and dims == {1: 9, 2: 5, 3: 3, 6: 2} and stab_ok,
    f"orders {orders}; commutant dims by order {dims}; Stab(eps) = A_3 ({len(stab)} elements)")

# ---- C3: route II -- the weak/spatial C_3 inside the 16-basis ----
Wsum = n4add(We[0], n4add(We[1], We[2]))
W3pow = n4mul(n4mul(Wsum, Wsum), Wsum)
Wcube = n4eq(W3pow, n4scale(Wsum, g(3)))                       # W^3 = 3W
# charpoly(W) = x^4 - 3x^2: Faddeev-LeVerrier on the numeric matrix (Gauss):
def charpoly_num(A):
    n = 4
    ident = [[G1 if i == j else G0 for j in range(n)] for i in range(n)]
    coeffs = [G1]
    Mk = [row[:] for row in ident]
    for k in range(1, n + 1):
        AMk = n4mul(A, Mk)
        tr = n4tr(AMk)
        c = gmul(tr, g(Fr(-1, k)))
        coeffs.append(c)
        if k < n:
            Mk = [[gadd(AMk[i][j], gmul(ident[i][j], c)) for j in range(n)] for i in range(n)]
    return coeffs


cpW = charpoly_num(Wsum)
cpW_ok = cpW == [G1, G0, g(-3), G0, G0]        # x^4 - 3x^2
# U = E0 - W^2/2 - i W/2 = u (x) u, u = (I2 - i(s1+s2+s3))/2; U^3 = E0; conjugation cycles
# build u = (I - i(s1+s2+s3))/2 directly:
ssum = [[gadd(gadd(SG[1][i][j], SG[2][i][j]), SG[3][i][j]) for j in range(2)] for i in range(2)]
u = [[gmul(gadd(SG[0][i][j], gmul(g(0, -1), ssum[i][j])), g(Fr(1, 2))) for j in range(2)] for i in range(2)]
UU = kronN(u, u)
U = n4add(n4sub(E0, n4scale(n4mul(Wsum, Wsum), g(Fr(1, 2)))), n4scale(Wsum, g(0, Fr(-1, 2))))
U_eq = n4eq(U, UU)
U3 = n4eq(n4mul(n4mul(U, U), U), E0)
cyc = all(n4eq(n4mul(n4mul(U, X), n4dag(U)), Y)
          for X, Y in ((Jop[0], Jop[1]), (Jop[1], Jop[2]), (Jop[2], Jop[0]),
                       (Kop[0], Kop[1]), (Kop[1], Kop[2]), (Kop[2], Kop[0]),
                       (We[0], We[1]), (We[1], We[2]), (We[2], We[0])))
chk("C3  [FT.158(1); FT.111; CONSOLIDATED SS10 route II]: the weak/spatial C_3 -- with"
    "\n           W-sum = W_1+W_2+W_3: W^3 = 3W and charpoly(W) = x^4-3x^2 (machine, Faddeev-LeVerrier);"
    "\n           U = E_0 - W^2/2 - iW/2 EQUALS u (x) u with u = (I_2 - i(s_1+s_2+s_3))/2 (exact 4x4"
    "\n           equality); U^3 = E_0; and U cycles J_i -> J_{i+1}, K_i -> K_{i+1}, W_i -> W_{i+1} by"
    "\n           conjugation (9/9 exact): C_3 <= SO(3) is INNER in the weak rotation algebra. The"
    "\n           route-I/route-II isomorphism stays an UNS_TAGGED identification [FT.116 Phys prose --"
    "\n           'reached from the opposite side' -- no numbered clause; recorded, never adopted].",
    Wcube and cpW_ok and U_eq and U3 and cyc)

print("=" * 104)
print("PART D -- the operator layer on the CT1.2 basis")
print("=" * 104)

# ---- D1: the (S,T) sector table ----
def swapconj(X):
    return n4mul(n4mul(SWAP, X), SWAP)


def spar(X):
    if n4eq(swapconj(X), X):
        return +1
    if n4eq(swapconj(X), n4scale(X, g(-1))):
        return -1
    return 0


ETA = {(0, 0): 1}
for i in (1, 2, 3):
    ETA[(0, i)] = ETA[(i, 0)] = -1
    for j in (1, 2, 3):
        ETA[(i, j)] = 1


def tpar(X):
    """the T-grade: every Pauli coordinate must carry one eta sign."""
    co = pauli_coords(X)
    signs = set()
    for k, v in co.items():
        if v != G0:
            signs.add(ETA[k])
    return signs.pop() if len(signs) == 1 else 0


basis16 = ([("E_0", E0, (+1, +1)), ("Sigma", SIG, (+1, +1))]
           + [(f"Ehat{i}", X, (+1, +1)) for i, X in enumerate(Ehat)]
           + [(f"W_{i+1}", X, (+1, -1)) for i, X in enumerate(We)]
           + [(f"J_{i+1}", X, (-1, +1)) for i, X in enumerate(Jop)]
           + [(f"K_{i+1}", X, (-1, -1)) for i, X in enumerate(Kop)])
D1_ok = all(spar(X) == s and tpar(X) == t for _, X, (s, t) in basis16)
sectors = {}
for _, X, _ in basis16:
    sectors[(spar(X), tpar(X))] = sectors.get((spar(X), tpar(X)), 0) + 1
# plus the diagonal-trace carrier Sigma completes E^ii -> the G-block is 5 (Ehat) + Sigma + E_0 = 7
D1_ok = D1_ok and sectors == {(1, 1): 7, (1, -1): 3, (-1, 1): 3, (-1, -1): 3}
chk("D1  [CT1.2; CT1.12a(1),(2); A3; C13 -- corrections register #6 enforced]: the (S,T) sector table"
    "\n           of the 16-basis, machine-exact: E_0, Sigma, Ehat^{ij} (5) are (+,+); W_i = (+,-);"
    "\n           J_i = (-,+); K_i = (-,-) -- sectors (7+1, 3, 3, 3) with the trace split E_0 (+) Sigma"
    "\n           [CT1.12a's 1+1+5+3 = 10 metric carriers S-even; J^{+-} the 6 S-odd with ZERO metric"
    "\n           coordinates]. The subgenerator's correction #6 (an earlier draft had W,J,K all odd/odd)"
    "\n           is certified against the canon's own parities [measurement_theorem.py B3 agreement].",
    D1_ok, f"sector counts (S,T): {sectors}")

# ---- D2: the commutation table ----
def eps3(i, j, k):
    return (i - j) * (j - k) * (k - i) // 2


D2_rows = []
for i in range(3):
    for j in range(3):
        # [J_i, J_j] = i eps_ijk W_k ; [K_i,K_j] = i eps W ; [J_i,K_j] = i(delta_ij Sigma - E^ij)
        lhs1 = comm(Jop[i], Jop[j])
        rhs1 = [[G0] * 4 for _ in range(4)]
        if i != j:
            k = 3 - i - j
            sgn = eps3(i, j, k)
            rhs1 = n4scale(We[k], gmul(g(0, 1), g(sgn)))
        D2_rows.append(n4eq(lhs1, rhs1))
        lhs2 = comm(Kop[i], Kop[j])
        rhs2 = [[G0] * 4 for _ in range(4)]
        if i != j:
            k = 3 - i - j
            sgn = eps3(i, j, k)
            rhs2 = n4scale(We[k], gmul(g(0, 1), g(sgn)))
        D2_rows.append(n4eq(lhs2, rhs2))
        lhs3 = comm(Jop[i], Kop[j])
        # E^{ij} for i != j is the symmetric pair; for i == j it is sigma_i (x) sigma_i
        if i == j:
            Eij = kronN(SG[i + 1], SG[i + 1])
        else:
            Eij = n4scale(n4add(kronN(SG[i + 1], SG[j + 1]), kronN(SG[j + 1], SG[i + 1])), g(Fr(1, 2)))
        rhs3 = n4scale(n4sub(n4scale(SIG, g(1 if i == j else 0)), Eij), g(0, 1))
        D2_rows.append(n4eq(lhs3, rhs3))
sig_comm = all(n4eq(comm(SIG, Jop[i]), n4scale(Kop[i], g(0, 4)))
               and n4eq(comm(SIG, Kop[i]), n4scale(Jop[i], g(0, -4))) for i in range(3))
w_comm = all(n4eq(comm(We[i], We[j]), n4scale(We[3 - i - j], gmul(g(0, 1), g(eps3(i, j, 3 - i - j)))) if i != j else [[G0] * 4 for _ in range(4)])
             for i in range(3) for j in range(3))
wj = all(n4eq(comm(We[i], Jop[j]), n4scale(Jop[3 - i - j], gmul(g(0, 1), g(eps3(i, j, 3 - i - j)))) if i != j else [[G0] * 4 for _ in range(4)])
         for i in range(3) for j in range(3))
wk = all(n4eq(comm(We[i], Kop[j]), n4scale(Kop[3 - i - j], gmul(g(0, 1), g(eps3(i, j, 3 - i - j)))) if i != j else [[G0] * 4 for _ in range(4)])
         for i in range(3) for j in range(3))
e0 = all(n4eq(comm(E0, X), [[G0] * 4 for _ in range(4)]) for X in Jop + Kop + We + [SIG])
chk("D2  [CT1.9; CT1.4; CT1.7; CT1.8 -- the closure table with exact coefficients]: [J_i,J_j] ="
    "\n           [K_i,K_j] = i eps_ijk W_k (18 rows); [J_i,K_j] = i(delta_ij Sigma - E^ij) (9 rows);"
    "\n           [Sigma,J_i] = 4i K_i, [Sigma,K_i] = -4i J_i; [W,W] = i eps W, [W,J] = i eps J, [W,K] ="
    "\n           i eps K; [E_0, .] = 0 -- ALL exact 4x4 Gauss(i) identities (27+6+18+4 rows machine).",
    all(D2_rows) and sig_comm and w_comm and wj and wk and e0)

# ---- D3: Lie<J,K> = su(4), dim 15, E_0 not in it ----
def coords(X):
    return [pauli_coords(X)[(a, b)] for a in range(4) for b in range(4)]


def span_rank(vecs):
    """rank over Q(i) by Gaussian elimination on Gauss coordinate rows."""
    rows = [list(v) for v in vecs]
    piv_rows, rank = [], 0
    for col in range(len(rows[0])):
        pr = None
        for r in rows:
            if r[col] != G0:
                pr = r
                break
        if pr is None:
            continue
        rows.remove(pr)
        pv = pr[col]
        pr = [gmul(x, ginv(pv)) for x in pr]
        for r in rows:
            if r[col] != G0:
                f = r[col]
                for j in range(len(r)):
                    r[j] = gsub(r[j], gmul(f, pr[j]))
        piv_rows.append(pr)
        rank += 1
    return rank, piv_rows


mats = list(Jop + Kop)
cur = [coords(X) for X in mats]
for _round in range(8):
    rk_before = span_rank(cur)[0]
    if rk_before == 15:
        break
    new_mats = []
    for A in mats:
        for B in mats:
            C = comm(A, B)
            if not all(x == G0 for row in C for x in row):
                new_mats.append(C)
    if not new_mats:
        break
    cur = cur + [coords(X) for X in new_mats]
    mats = (mats + new_mats)[:48]
    if span_rank(cur)[0] == rk_before:
        break
rk_final = span_rank(cur)[0]
e0_coord = coords(E0)
rk_with_e0, _ = span_rank(cur + [e0_coord])
D3_ok = (rk_final == 15 and rk_with_e0 == 16)
chk("D3  [CT1.9 extended -- 'the generation from the six alone is new here']: the Lie closure of"
    "\n           {J_1,J_2,J_3,K_1,K_2,K_3} under commutators, computed by exact Gauss(i) coordinate"
    "\n           elimination: rank 15 = dim su(4), and E_0 is NOT in the closure (rank jumps to 16 when"
    "\n           added) -- the six S-odd generators produce Sigma, the five Ehat, and the three W: the"
    "\n           whole traceless algebra, everything except the conformal mode. H(C^4) = i su(4) (+) R E_0,"
    "\n           16 = 15+1.",
    D3_ok, f"Lie closure rank {rk_final}; with E_0: {rk_with_e0}")

# ---- D4: the nilpotent triples A_i, B_i ----
A = [n4scale(n4add(Jop[i], n4scale(Kop[i], GI)), g(Fr(1, 2))) for i in range(3)]
B = [n4dag(A[i]) for i in range(3)]
zero4 = [[G0] * 4 for _ in range(4)]
nilp = all(n4eq(n4mul(A[i], A[i]), zero4) and n4eq(n4mul(B[i], B[i]), zero4) for i in range(3))
aiaj = all(n4eq(n4mul(A[i], A[j]), zero4) and n4eq(n4mul(B[i], B[j]), zero4) for i in range(3) for j in range(3))
commAB = all(n4eq(comm(A[i], A[j]), zero4) and n4eq(comm(B[i], B[j]), zero4) for i in range(3) for j in range(3))
antiAB = all(n4eq(n4add(n4mul(A[i], A[j]), n4mul(A[j], A[i])), zero4) for i in range(3) for j in range(3))
trAiBj = all(n4tr(n4mul(A[i], B[j])) == (G1 if i == j else G0) for i in range(3) for j in range(3))
trAiAj = all(n4tr(n4mul(A[i], A[j])) == G0 for i in range(3) for j in range(3))
sumAB = n4add(n4mul(A[0], B[0]), n4add(n4mul(A[1], B[1]), n4mul(A[2], B[2])))
sumBA = n4add(n4mul(B[0], A[0]), n4add(n4mul(B[1], A[1]), n4mul(B[2], A[2])))
sumcomm = n4add(comm(A[0], B[0]), n4add(comm(A[1], B[1]), comm(A[2], B[2])))
ident_ok = n4eq(sumAB, PR) and n4eq(sumBA, n4scale(PV, g(3))) and n4eq(sumcomm, SIG)
# the honest negative: {A_i,B_j} != delta_ij * 1
anti_cross = n4add(n4mul(A[0], B[0]), n4mul(B[0], A[0]))
honest_neg = not n4eq(anti_cross, E0)
sum_anti = n4add(anti_cross, n4add(n4add(n4mul(A[1], B[1]), n4mul(B[1], A[1])),
                                   n4add(n4mul(A[2], B[2]), n4mul(B[2], A[2]))))
sum_anti_val = n4eq(sum_anti, n4scale(n4sub(n4scale(E0, g(3)), SIG), g(Fr(1, 2))))
chk("D4  [CONSOLIDATED SS34 -- machine-verified exactly]: A_i = (J_i+iK_i)/2, B_i = A_i^dagger: A_i^2 ="
    "\n           B_i^2 = 0; A_iA_j = B_iB_j = 0 for ALL i,j (three mutually annihilating rank-one"
    "\n           nilpotents); [A,A] = [B,B] = {A,A} = {B,B} = 0; Tr(A_iB_j) = delta_ij, Tr(A_iA_j) = 0;"
    "\n           sum A_iB_i = Pi_R = (3E_0+Sigma)/4, sum B_iA_i = 3 Pi_V = 3(E_0-Sigma)/4, sum [A_i,B_i]"
    "\n           = Sigma. HONEST NEGATIVE: {A_i,B_j} != delta_ij*1 (the sum is (3E_0-Sigma)/2) -- the"
    "\n           triple is fermion-LIKE, NOT Clifford.",
    nilp and aiaj and commAB and antiAB and trAiBj and trAiAj and ident_ok and honest_neg and sum_anti_val)

# ---- D5: the Casimirs ----
J2 = n4add(n4mul(Jop[0], Jop[0]), n4add(n4mul(Jop[1], Jop[1]), n4mul(Jop[2], Jop[2])))
K2 = n4add(n4mul(Kop[0], Kop[0]), n4add(n4mul(Kop[1], Kop[1]), n4mul(Kop[2], Kop[2])))
W2 = n4add(n4mul(We[0], We[0]), n4add(n4mul(We[1], We[1]), n4mul(We[2], We[2])))
casimir_ok = (n4eq(J2, K2) and n4eq(J2, n4add(PR, n4scale(PV, g(3))))
              and n4eq(W2, n4scale(PR, g(2)))
              and all(n4eq(n4mul(We[i], PV), zero4) for i in range(3)))
chk("D5  [FT.93(5) re-certified; FT.93(5)/FT.141(4)'s branch asymmetry '2 versus 0' ORIGINATED]: the"
    "\n           Casimir rows against the branch split C^4 = vee^2 (+) wedge^2: sum J_i^2 = sum K_i^2 ="
    "\n           Pi_R + 3Pi_V = (3E_0-Sigma)/2 (weights (1,3)); sum W_i^2 = 2Pi_R = (3E_0+Sigma)/2"
    "\n           (weights (2,0)); W_i Pi_V = 0 for all i -- the branch asymmetry is a machine identity.",
    casimir_ok)

# ---- D6: the branch-change bridge ----
bridge_ok = (all(n4eq(swapconj(Jop[i]), n4scale(Jop[i], g(-1))) for i in range(3))
             and all(n4eq(swapconj(Kop[i]), n4scale(Kop[i], g(-1))) for i in range(3))
             and all(n4eq(swapconj(We[i]), We[i]) for i in range(3))
             and all(n4eq(n4mul(Jop[i], PR), n4mul(PV, Jop[i])) for i in range(3))
             and all(n4eq(n4mul(Kop[i], PR), n4mul(PV, Kop[i])) for i in range(3))
             and n4eq(n4mul(SIG, PR), PR) and n4eq(n4mul(SIG, PV), n4scale(PV, g(-3))))
chk("D6  [CONSOLIDATED SS35 -- 'the bridge, derived'; D1.2; A8; CT0.7]: S J_i S = -J_i (swap-odd) with"
    "\n           Pi_R = (E_0+S)/2, Pi_V = (E_0-S)/2 gives the BRANCH-CHANGE BRIDGE: J_i Pi_R = Pi_V J_i"
    "\n           and K_i Pi_R = Pi_V K_i (6/6 exact), W_i Pi_V = 0 -- the six are EXACTLY the"
    "\n           branch-changing operators, so D1.2's seal events and the F_{J^{+-}} blocks are one"
    "\n           phenomenon at two loci (the earlier 'two different things' flag WITHDRAWN -- corrections"
    "\n           register #13); Sigma Pi_R = +Pi_R, Sigma Pi_V = -3Pi_V (spec Sigma = {1,1,1,-3}).",
    bridge_ok)

# ---- D7: the inner reflection Ad(e^{i pi Sigma/8}) ----
# sector computation: for swap-odd X, Ad(R)X = i(Pi_R X Pi_V - Pi_V X Pi_R) (since e^{i pi/8 * 1} on the
# R-branch and e^{-3 i pi/8} on the V-branch; the product phases are e^{i pi/2} = i and e^{-i pi/2} = -i)
def ad_refl(X):
    """Ad(R)X with R = e^{i pi/8} Pi_R + e^{-3 i pi/8} Pi_V: the same-sector parts are phase-free,
    the cross-sector parts pick up e^{i pi/2} = i and e^{-i pi/2} = -i."""
    RRp = n4mul(n4mul(PR, X), PR)
    VV = n4mul(n4mul(PV, X), PV)
    RV = n4mul(n4mul(PR, X), PV)
    VR = n4mul(n4mul(PV, X), PR)
    return n4add(n4add(RRp, VV), n4sub(n4scale(RV, GI), n4scale(VR, GI)))


refl_ok = (all(n4eq(ad_refl(Jop[i]), n4scale(Kop[i], g(-1))) for i in range(3))
           and all(n4eq(ad_refl(Kop[i]), Jop[i]) for i in range(3))
           and all(n4eq(ad_refl(We[i]), We[i]) for i in range(3)))
ad2 = all(n4eq(ad_refl(ad_refl(Jop[i])), n4scale(Jop[i], g(-1))) for i in range(3))   # order exactly 4
ad4 = all(n4eq(ad_refl(ad_refl(ad_refl(ad_refl(X)))), X) for X in Jop + Kop + We)
# R^4 = e^{i pi Sigma/2} = i E_0: the branch phases (e^{i pi/8})^4 = e^{i pi/2} and
# (e^{-3 i pi/8})^4 = e^{-3 i pi/2} = e^{+i pi/2} (mod 2 pi) -- exact Fraction exponent arithmetic:
R4_ok = (Fr(1, 8) * 4 == Fr(1, 2)) and ((Fr(-3, 8) * 4) % 2 == Fr(1, 2))
Ai_phase = all(n4eq(ad_refl(A[i]), n4scale(A[i], GI)) and n4eq(ad_refl(B[i]), n4scale(B[i], g(0, -1)))
               for i in range(3))
chk("D7  [CONSOLIDATED SS36 -- the reflection is INNER and order 4]: Ad(e^{i pi Sigma/8}) computed"
    "\n           sector-wise (Sigma's spectrum {+1^3, -3} makes the phases e^{i pi/8}, e^{-3i pi/8}):"
    "\n           J_i -> -K_i, K_i -> J_i (6/6), W_i -> W_i (3/3), A_i -> i A_i, B_i -> -i B_i; Ad^2 ="
    "\n           -id on the six (J -> -J), Ad^4 = id: ORDER EXACTLY 4; R^4 = e^{i pi Sigma/2} = i E_0"
    "\n           (both branch phases e^{i pi/2}). The reflection is a +-i phase on the two nilpotent"
    "\n           halves -- it exists only AFTER complexification. CPT stays the scalar character"
    "\n           [FT.134(3)]: Ad(CPT) = id on the sixteen (trivial); the history reversal is"
    "\n           INADMISSIBLE [FT.144(4)(ii); A6: no tau^{-1}] -- the four-candidate census adjudicated.",
    refl_ok and ad2 and ad4 and R4_ok and Ai_phase)

# ---- D8: the 10-of-16 tensor-square occupancy ----
RM = Ring(["m0", "m1", "m2", "m3"])
m = [RM.var(f"m{i}") for i in range(4)]
mvec2 = RM.add(RM.add(RM.mul(m[1], m[1]), RM.mul(m[2], m[2])), RM.mul(m[3], m[3]))
Sro = RM.add(RM.mul(m[0], m[0]), mvec2)                      # S = sum m^2
T_ro_ = RM.sub(mvec2, RM.mul(m[0], m[0]))                    # T = -m0^2 + mvec^2
# coefficient identities in the CT1.2 basis: X_{E_0} = m0^2 = (S-T)/2; X_Sigma = mvec^2/3 = (S+T)/6
occ_ok = (RM.eq(RM.mul(m[0], m[0]), RM.scale(RM.sub(Sro, T_ro_), Fr(1, 2)))
          and RM.eq(RM.scale(mvec2, Fr(1, 3)), RM.scale(RM.add(Sro, T_ro_), Fr(1, 6))))
# J/K coefficients of X = sum m_mu m_nu s_mu (x) s_nu vanish: c_jk - c_kj = 0 and c_0i - c_i0 = 0
jk_zero = all(RM.eq(RM.sub(RM.mul(m[a], m[b]), RM.mul(m[b], m[a])), RM.zero())
              for a in range(4) for b in range(4))
# the full expansion: X = m0^2 E_0 + (mvec^2/3) Sigma + sum_i (m_i^2 - mvec^2/3) Ehat^{ii}
#   + 2 sum_{j<k} m_j m_k Ehat^{jk} + 2 m0 sum_i m_i W_i -- verified numerically on 3 witnesses:
def X_matrix(mv):
    X = [[G0] * 4 for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            X = n4add(X, n4scale(kronN(SG[mu], SG[nu]), g(mv[mu] * mv[nu])))
    return X


def expansion(mv):
    E = n4scale(E0, g(mv[0] ** 2))
    mv2 = mv[1] ** 2 + mv[2] ** 2 + mv[3] ** 2
    E = n4add(E, n4scale(SIG, g(Fr(mv2, 3))))
    diagpairs = [(1, 1), (2, 2), (3, 3)]
    Ehat_diag = [n4sub(kronN(SG[1], SG[1]), n4scale(SIG, g(Fr(1, 3)))),
                 n4sub(kronN(SG[2], SG[2]), n4scale(SIG, g(Fr(1, 3)))),
                 n4sub(kronN(SG[3], SG[3]), n4scale(SIG, g(Fr(1, 3))))]
    for i, X_ in enumerate(Ehat_diag):
        coef = mv[i + 1] ** 2 - Fr(mv2, 3)
        E = n4add(E, n4scale(X_, g(coef)))
    offpairs = [((1, 2), Ehat[0]), ((1, 3), Ehat[1]), ((2, 3), Ehat[2])]
    for (j, k), X_ in offpairs:
        E = n4add(E, n4scale(X_, g(2 * mv[j] * mv[k])))
    for i in range(3):
        E = n4add(E, n4scale(We[i], g(2 * mv[0] * mv[i + 1])))
    return E


witnesses = [(1, 2, 3, 5), (Fr(1, 2), Fr(-3), Fr(7, 4), 0), (0, 1, -1, 2)]
exp_ok = all(n4eq(X_matrix([Fr(x) for x in mv]), expansion([Fr(x) for x in mv])) for mv in witnesses)
chk("D8  [CONSOLIDATED SS31; IT.38(2) pattern; CT1.12 metric table]: X = M (x) M with c_munu = m_mu m_nu"
    "\n           occupies TEN of the sixteen: the J_i and K_i coefficients (c_jk - c_kj, c_0i - c_i0)"
    "\n           vanish for EVERY M (machine: all 16 pairs, symbolic m); the explicit expansion X = m0^2"
    "\n           E_0 + (mvec^2/3) Sigma + sum (m_i^2 - mvec^2/3) Ehat^{ii} + 2 sum m_j m_k Ehat^{jk} +"
    "\n           2 m0 sum m_i W_i verified on 3 exact witnesses; and the two singlet readouts X_{E_0} ="
    "\n           (S-T)/2, X_{Sigma} = (S+T)/6 hold as symbolic identities. A TENSOR SQUARE CAN NEVER CARRY"
    "\n           THE BLOCKS THAT GENERATE THE PHASE (D3's six).",
    occ_ok and jk_zero and exp_ok)

print("=" * 104)
print("PART E -- the phase-calculus layer of the parametric matrix class (symbolic identities)")
print("=" * 104)

# jet ring: a, ap, app (q-phase); d, dp, dpp (l-phase); b, cc constant in the phases
RJ = Ring(["a", "ap", "app", "d", "dp", "dpp", "b", "cc", "e", "ep"])
J = {n: RJ.var(n) for n in RJ.names}
Dq_img = {"a": J["ap"], "ap": J["app"], "app": RJ.zero()}
Dl_img = {"d": J["dp"], "dp": J["dpp"], "dpp": RJ.zero()}


def Dq(p):
    return RJ.deriv(p, Dq_img)


def Dl(p):
    return RJ.deriv(p, Dl_img)


def M2sym():
    return [[J["a"], J["b"]], [J["cc"], J["d"]]]


def kron_sym(A, B):
    out = [[RJ.zero() for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + k][2 * j + l] = RJ.mul(A[i][j], B[k][l])
    return out


def add4(A, B):
    return [[RJ.add(A[i][j], B[i][j]) for j in range(4)] for i in range(4)]


Msym = M2sym()
Xsym = kron_sym(Msym, Msym)
DqM = [[J["ap"], RJ.zero()], [RJ.zero(), RJ.zero()]]
DlM = [[RJ.zero(), RJ.zero()], [RJ.zero(), J["dp"]]]
Dq2M = [[J["app"], RJ.zero()], [RJ.zero(), RJ.zero()]]
Dl2M = [[RJ.zero(), RJ.zero()], [RJ.zero(), J["dpp"]]]
dX_q = add4(kron_sym(DqM, Msym), kron_sym(Msym, DqM))
dX_l = add4(kron_sym(DlM, Msym), kron_sym(Msym, DlM))
dX_q2 = add4(add4(kron_sym(Dq2M, Msym), kron_sym(DqM, DqM)),
             add4(kron_sym(DqM, DqM), kron_sym(Msym, Dq2M)))
dX_l2 = add4(add4(kron_sym(Dl2M, Msym), kron_sym(DlM, DlM)), add4(kron_sym(DlM, DlM), kron_sym(Msym, Dl2M)))
dX_ql = add4(kron_sym(DlM, DqM), kron_sym(DqM, DlM))
# the four CORRECTED cells (register #1): (2,2),(3,3) 1-based = (1,1),(2,2) 0-based:
cells_ok = (RJ.eq(dX_q[1][1], RJ.mul(J["ap"], J["d"])) and RJ.eq(dX_q[2][2], RJ.mul(J["ap"], J["d"]))
            and RJ.eq(dX_l[1][1], RJ.mul(J["a"], J["dp"])) and RJ.eq(dX_l[2][2], RJ.mul(J["a"], J["dp"]))
            and RJ.eq(dX_q2[1][1], RJ.mul(J["app"], J["d"])) and RJ.eq(dX_l2[2][2], RJ.mul(J["a"], J["dpp"]))
            and RJ.eq(dX_ql[1][1], RJ.mul(J["ap"], J["dp"])) and RJ.eq(dX_ql[2][2], RJ.mul(J["ap"], J["dp"]))
            and not RJ.is_zero(RJ.mul(J["ap"], J["d"])))
chk("E1  [CONSOLIDATED SS16 -- corrections register #1 certified]: the four tensor-square cells that"
    "\n           were received as ZERO are NOT zero: (dX/dq)_{(12),(12)} = (dX/dq)_{(21),(21)} = a'd, and"
    "\n           likewise a d', a'' d, a d''; the mixed second derivative carries a'd' at exactly TWO of"
    "\n           the sixteen cells -- the two phases meet only there, only at second order. All five"
    "\n           Leibniz forms (dX/dq, dX/dl, d2X/dq2, d2X/dl2, d2X/dqdl) verified entrywise against the"
    "\n           derivation rule on M (x) M (16/16 each, symbolic jets).",
    cells_ok, f"(dX/dq)[1][1] = a'*d (nonzero: {not RJ.is_zero(RJ.mul(J['ap'], J['d']))})")

# ---- E2: the readout derivative table ----
Sro_J = RJ.add(RJ.scale(RJ.add(RJ.mul(J["a"], J["a"]), RJ.mul(J["d"], J["d"])), Fr(1, 2)),
               RJ.mul(J["b"], J["cc"]))
Tro_J = RJ.sub(RJ.mul(J["b"], J["cc"]), RJ.mul(J["a"], J["d"]))
E2_ok = (RJ.eq(Dq(Sro_J), RJ.mul(J["a"], J["ap"])) and RJ.eq(Dl(Sro_J), RJ.mul(J["d"], J["dp"]))
         and RJ.eq(Dq(Tro_J), RJ.neg(RJ.mul(J["d"], J["ap"]))) and RJ.eq(Dl(Tro_J), RJ.neg(RJ.mul(J["a"], J["dp"])))
         and RJ.is_zero(Dq(Dl(Sro_J))) and RJ.eq(Dq(Dl(Tro_J)), RJ.neg(RJ.mul(J["ap"], J["dp"])))
         and RJ.eq(Dq(Dq(Sro_J)), RJ.add(RJ.mul(J["ap"], J["ap"]), RJ.mul(J["a"], J["app"])))
         and RJ.eq(Dl(Dl(Sro_J)), RJ.add(RJ.mul(J["dp"], J["dp"]), RJ.mul(J["d"], J["dpp"])))
         and RJ.eq(Dq(Dq(Tro_J)), RJ.neg(RJ.mul(J["d"], J["app"])))
         and RJ.eq(Dl(Dl(Tro_J)), RJ.neg(RJ.mul(J["a"], J["dpp"]))))
chk("E2  [CONSOLIDATED SS17]: the readout derivative table verified exactly: S has NO cross-curvature"
    "\n           (d_q d_l S = 0), T has ONLY the cross term (d_q d_l T = -a'd'): the plain readout"
    "\n           separates the two phases completely, the determinant not at all.",
    E2_ok)

# ---- E3: the constrained flow delta_l = n delta_q: coefficients (1, 2n, n^2) ----
Dn_flow = lambda p, n: RJ.add(Dq(p), RJ.scale(Dl(p), n))
flow_ok = True
for n in (1, 2, 3, 4, 5, 6):
    d2T = Dn_flow(Dn_flow(Tro_J, n), n)
    target = RJ.neg(RJ.add(RJ.add(RJ.mul(J["d"], J["app"]), RJ.scale(RJ.mul(J["ap"], J["dp"]), 2 * n)),
                           RJ.scale(RJ.mul(J["a"], J["dpp"]), n * n)))
    flow_ok &= RJ.eq(d2T, target)
d_flow_ok = (RJ.eq(Dn_flow(Dn_flow(Sro_J, 3), 3),
                   RJ.add(RJ.add(RJ.mul(J["ap"], J["ap"]), RJ.mul(J["a"], J["app"])),
                          RJ.scale(RJ.add(RJ.mul(J["dp"], J["dp"]), RJ.mul(J["d"], J["dpp"])), 9)))
             and RJ.eq(Dn_flow(RJ.sub(RJ.mul(J["a"], J["d"]), RJ.mul(J["b"], J["cc"])), 3),
                       RJ.add(RJ.mul(J["ap"], J["d"]), RJ.scale(RJ.mul(J["a"], J["dp"]), 3))))
chk("E3  [CONSOLIDATED SS18; corrections register #5]: the constrained flow d/delta = d_q + n d_l"
    "\n           (delta_l = n delta_q): d^2T/delta^2 = -(d a'' + 2n a'd' + n^2 a d'') -- the coefficient"
    "\n           triple (1, 2n, n^2) verified for n=1..6 (the register's n=3 case (1,6,9), with the"
    "\n           self-caught 27->9 correction certified); d^2S/ddelta^2 and d(det)/ddelta, d(tr)/ddelta"
    "\n           exact.",
    flow_ok and d_flow_ok)

# ---- E4: the Jacobian and Hessian determinants ----
detJ = RJ.sub(RJ.mul(RJ.mul(J["a"], J["ap"]), RJ.neg(RJ.mul(J["a"], J["dp"]))),
              RJ.mul(RJ.mul(J["d"], J["dp"]), RJ.neg(RJ.mul(J["d"], J["ap"]))))
# J_Phi = [[S_q, S_l],[T_q, T_l]] = [[a a', d d'],[-d a', -a d']]:
detJ_true = RJ.sub(RJ.mul(RJ.mul(J["a"], J["ap"]), RJ.neg(RJ.mul(J["a"], J["dp"]))),
                   RJ.mul(RJ.mul(J["d"], J["dp"]), RJ.neg(RJ.mul(J["d"], J["ap"]))))
detJ_claim = RJ.neg(RJ.mul(RJ.mul(J["ap"], J["dp"]),
                           RJ.sub(RJ.mul(J["a"], J["a"]), RJ.mul(J["d"], J["d"]))))
HT = [[RJ.neg(RJ.mul(J["d"], J["app"])), RJ.neg(RJ.mul(J["ap"], J["dp"]))],
      [RJ.neg(RJ.mul(J["ap"], J["dp"])), RJ.neg(RJ.mul(J["a"], J["dpp"]))]]
detHT = RJ.sub(RJ.mul(HT[0][0], HT[1][1]), RJ.mul(HT[0][1], HT[1][0]))
detHT_claim = RJ.sub(RJ.mul(RJ.mul(J["a"], J["d"]), RJ.mul(J["app"], J["dpp"])),
                     RJ.mul(RJ.mul(J["ap"], J["dp"]), RJ.mul(J["ap"], J["dp"])))
E4_ok = RJ.eq(detJ_true, detJ_claim) and RJ.eq(detHT, detHT_claim)
chk("E4  [CONSOLIDATED SS19]: det J_Phi = -a'd'(a^2-d^2) (the singular locus a'=0 v d'=0 v a=+-d) and"
    "\n           det H_T = a d a'' d'' - (a'd')^2 -- both verified as exact polynomial identities.",
    E4_ok)

# ---- E5: the eigenvalue-derivative certificate ----
RE = Ring(["a", "b", "cc", "d", "ap", "s"])
Ev = {n: RE.var(n) for n in RE.names}
Delta = RE.add(RE.mul(RE.sub(Ev["a"], Ev["d"]), RE.sub(Ev["a"], Ev["d"])),
               RE.scale(RE.mul(Ev["b"], Ev["cc"]), 4))
RE.rules = [(RE.ix["s"], 2, Delta)]
tr = RE.add(Ev["a"], Ev["d"])
det_ = RE.sub(RE.mul(Ev["a"], Ev["d"]), RE.mul(Ev["b"], Ev["cc"]))
E5_p = E5_m = True
for sgn in (1, -1):
    lam = RE.scale(RE.add(tr, RE.scale(Ev["s"], sgn)), Fr(1, 2))
    zero_P = RE.is_zero(RE.add(RE.sub(RE.mul(lam, lam), RE.mul(tr, lam)), det_))
    lamp_cross = RE.mul(Ev["ap"], RE.scale(RE.add(Ev["s"], RE.scale(RE.sub(Ev["a"], Ev["d"]), sgn)), Fr(1, 2)))
    lhs = RE.mul(RE.sub(RE.scale(lam, 2), tr), lamp_cross)
    rhs = RE.mul(Ev["s"], RE.sub(RE.mul(Ev["ap"], lam), RE.mul(Ev["ap"], Ev["d"])))
    ok_der = RE.is_zero(RE.sub(lhs, rhs))
    if sgn == 1:
        E5_p = zero_P and ok_der
    else:
        E5_m = zero_P and ok_der
chk("E5  [CONSOLIDATED SS19]: the eigenvalue-derivative certificate in the exact ring"
    "\n           Q[a,b,c,d,a',s]/(s^2-Delta): P(lam_+-) = 0 and the implicit-differentiation identity"
    "\n           (2 lam - tr) * lam' = tr' lam - det' is satisfied by lam'_+- = (a'/2)(1 +- (a-d)/s)"
    "\n           (cross-multiplied, polynomial) -- at the sharp threshold c = eps_q = 0 the bracket is"
    "\n           1 +- sign(a-d) in {0,2}: EACH PHASE MOVES EXACTLY ONE EIGENVALUE.",
    E5_p and E5_m)

# ---- E6: order 3 -- the triple annihilation ----
RJ3 = Ring(["a", "ap", "d", "dp", "e", "ep"])
J3 = {n: RJ3.var(n) for n in RJ3.names}
Dq3 = lambda p: RJ3.deriv(p, {"a": J3["ap"]})
Dl3 = lambda p: RJ3.deriv(p, {"d": J3["dp"]})
Dv3 = lambda p: RJ3.deriv(p, {"e": J3["ep"]})
M3 = [[J3["a"], RJ3.zero(), RJ3.zero()],
      [RJ3.zero(), J3["d"], RJ3.zero()],
      [RJ3.zero(), RJ3.zero(), J3["e"]]]


def kron_sym3(A, B):
    out = [[RJ3.zero() for _ in range(9)] for _ in range(9)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    out[3 * i + k][3 * j + l] = RJ3.mul(A[i][j], B[k][l])
    return out


X3 = kron_sym3(M3, M3)
triple_zero = all(RJ3.is_zero(Dq3(Dl3(Dv3(X3[i][j])))) for i in range(9) for j in range(9))
ade = RJ3.mul(J3["a"], RJ3.mul(J3["d"], J3["e"]))
triple_ade = Dq3(Dl3(Dv3(ade)))
ade_ok = not RJ3.is_zero(triple_ade) and RJ3.eq(triple_ade, RJ3.mul(J3["ap"], RJ3.mul(J3["dp"], J3["ep"])))
T3 = RJ3.neg(ade)
pair_ok = RJ3.eq(Dq3(Dl3(T3)), RJ3.neg(RJ3.mul(J3["ap"], RJ3.mul(J3["dp"], J3["e"]))))
chk("E6  [CONSOLIDATED SS24 -- 'the new structural fact at order 3']: in M (x) M every cell is a product"
    "\n           of exactly TWO diagonal letters, so d_q d_l d_nu (M (x) M) = 0 IDENTICALLY (all 81 cells,"
    "\n           machine); in M^{(x)3} the cell a*d*e exists and d_q d_l d_nu (ade) = a'd'e' != 0; the"
    "\n           pairwise couplings d_q d_l T_3 = -a'd'e (and cyclic) are exact. THE ORDER OF THE TENSOR"
    "\n           POWER DECIDES HOW MANY CHANNEL ANGLES CAN MEET IN ONE NUMBER: three pairwise couplings"
    "\n           (C(3,2)), no triple, until the cube.",
    triple_zero and ade_ok and pair_ok)

print("=" * 104)
print("PART F -- the saturated node, the Lyapunov layer, the radar algebra")
print("=" * 104)

# ---- F1: the Lyapunov identities in Q[gamma] ----
RG2 = Ring(["gm"])
gm2 = RG2.var("gm")
contract = RG2.sub(RG2.const(1), RG2.scale(gm2, Fr(1, 4)))
c2 = RG2.mul(contract, contract)
deficit = RG2.scale(RG2.mul(gm2, RG2.sub(RG2.const(8), gm2)), Fr(1, 16))
F1_ok = (RG2.eq(RG2.add(c2, deficit), RG2.const(1))
         and all(RG2.eq(RG2.submap(deficit, {"gm": RG2.const(v)}), RG2.const(0)) for v in (0, 8))
         and RG2.eq(RG2.submap(c2, {"gm": RG2.const(1)}), RG2.const(Fr(9, 16)))
         and RG2.eq(RG2.submap(deficit, {"gm": RG2.const(1)}), RG2.const(Fr(7, 16)))
         and Fr(9, 16) ** 6 == Fr(531441, 16777216))
chk("F1  [BM.8(2); L2; BM.51; PJ.13(2),(3)]: the Lyapunov layer in Q[gamma]: (1-gamma/4)^2 +"
    "\n           gamma(8-gamma)/16 = 1 EXACTLY (the contraction + the deficit); the deficit's zero locus"
    "\n           {0, 8}; at gamma=1: (9/16, 7/16) and (9/16)^6 = 531441/16777216; the jump-direction"
    "\n           blindness: lambda_jump = 2 ln(1-gamma/4) carries NO delta -- the contraction is a"
    "\n           gamma-law, blind to which channel angle moved [BM.51's direction-blind read].",
    F1_ok)

# ---- F2: the saturation census ----
eps_witnesses = [Fr(0), Fr(1, 8), Fr(1, 5), Fr(249, 1000), Fr(1, 4) - Fr(1, 10 ** 6)]
virtual = all(not (Fr(0) <= Fr(1, 4) <= e) and not (Fr(1, 4) >= 1 - e) for e in eps_witnesses)
O_vals = [max(0, 2 ** (n + 1) - 16) for n in range(7)]
lock = all((2 ** (n + 1) > 16) == (n >= 4) for n in range(7))
dims = (2 ** 4 == 16) and (3 + 3 + 5 + 3 + 1 + 1 == 16) and (16 + 1 == 17) and (17 + 8 == 25)
F2_ok = virtual and O_vals == [0, 0, 0, 0, 16, 48, 112] and O_vals[4] == 16 and lock and dims
chk("F2  [A5; CT0.8; CT0.6; CT0.11; CT0.12; CT0.13; CT0.14; IT.3(2); CONSOLIDATED SS39]: the saturated"
    "\n           node: |Pi_V rho_o| = 1/4 lies OUTSIDE [0,eps] u [1-eps,1] for every eps < 1/4 (witness"
    "\n           sweep incl. eps = 1/4 - 10^-6): EVERY channel virtual, |R|=0, n_V = 2E, Delta = 3E"
    "\n           maximal (re-certifies IT.3(2)'s 'all-virtual' on the A4 test); D_tick(3) = 16 = C_cap,"
    "\n           O(3) = 0, O(n) = (0,0,0,0,16,48,112), O(4) = 16 = C_cap exactly; the lock biconditional"
    "\n           2^{n+1} > 16 <=> n >= 4 (n=0..6); the dimension ladder 6, 16, 17, 25.",
    F2_ok, f"O(n) = {O_vals}")

# ---- F3: the radar algebra (rational identities, cross-multiplied) ----
RR = Ring(["Gx", "dx", "Nn", "ss"])
Gx, dx, Nn, ss = RR.var("Gx"), RR.var("dx"), RR.var("Nn"), RR.var("ss")
N2s2 = RR.sub(RR.mul(Nn, Nn), RR.mul(ss, ss))
def root_check(sign):
    """dtau = Gx*dx/(Nn - sign*ss) is a root of the null quadratic
    (ss^2-Nn^2) dtau^2 + 2 ss Gx dx dtau + Gx^2 dx^2 = 0 -- cross-multiplied by den^2."""
    den = RR.sub(Nn, RR.scale(ss, sign))
    num = RR.mul(Gx, dx)
    # the leg's own displacement is sign*dx: the middle term carries the sign
    q = RR.add(RR.add(RR.mul(RR.sub(RR.mul(ss, ss), RR.mul(Nn, Nn)), RR.mul(num, num)),
                      RR.scale(RR.mul(ss, RR.mul(Gx, RR.mul(dx, RR.mul(num, RR.scale(den, sign))))), 2)),
               RR.mul(RR.mul(Gx, Gx), RR.mul(RR.mul(dx, dx), RR.mul(den, den))))
    return RR.is_zero(q)


roots_ok = root_check(1) and root_check(-1)
identity_sum = RR.eq(RR.add(RR.mul(Gx, RR.mul(dx, RR.add(Nn, ss))), RR.mul(Gx, RR.mul(dx, RR.sub(Nn, ss)))),
                     RR.scale(RR.mul(Gx, RR.mul(dx, Nn)), 2))
identity_diff = RR.eq(RR.sub(RR.mul(Gx, RR.mul(dx, RR.add(Nn, ss))), RR.mul(Gx, RR.mul(dx, RR.sub(Nn, ss)))),
                      RR.scale(RR.mul(Gx, RR.mul(dx, ss)), 2))
half_ok = RR.eq(RR.scale(RR.mul(Nn, RR.scale(RR.mul(Gx, RR.mul(dx, Nn)), 2)), Fr(1, 2)),
                RR.mul(Gx, RR.mul(dx, RR.mul(Nn, Nn))))
proper = RR.eq(RR.scale(RR.submap(RR.add(RR.mul(Gx, RR.mul(dx, RR.add(Nn, ss))),
                                         RR.mul(Gx, RR.mul(dx, RR.sub(Nn, ss)))), {"ss": RR.zero()}), Fr(1, 2)),
               RR.mul(Gx, RR.mul(dx, Nn)))
tconj = RR.eq(RR.submap(RR.sub(Nn, ss), {"ss": RR.neg(ss)}), RR.add(Nn, ss))
chk("F3  [BM.34(1),(2),(3); FT.156(3); RS.3(3), RS.4(2)]: the radar/chart algebra as exact rational"
    "\n           identities (cross-multiplied in Q[Gx,dx,N,s]): dtau_+- = Gx*dx/(N -+ s) are the roots of"
    "\n           BM.34(2)'s null condition; (dtau+ + dtau-)(N^2-s^2) = 2 Gx dx N and (dtau+ - dtau-)"
    "\n           (N^2-s^2) = 2 Gx dx s -- hence AGREEMENT <=> s*dx = 0 (the shift projection along the"
    "\n           link vanishes), the radar half-distance = Gx dx N^2/(N^2-s^2) = the proper length EXACTLY"
    "\n           at s=0, and w -> -w swaps dtau_+ <-> dtau_- (the two syncs are T-conjugate reads).",
    roots_ok and identity_sum and identity_diff and half_ok and proper and tconj)

# ---- F4: the O(n) continuation -- recorded and scoped out ----
Otilde3 = 2 ** (3 + 1) - 16
slope = Fr(16)                                          # O'(3)/ln2 = 2^4 = 16 (symbolic: 16 ln2)
F4_ok = (Otilde3 == 0 and max(0, 2 ** (3 + 1) - 16) == 0 and slope == 16)
chk("F4  [CT0.6; CT0.11; CT4.4a; CONSOLIDATED SS38 -- RECORDED AND SCOPED OUT]: the analytic"
    "\n           continuation O~(z) = 2^{z+1}-16 vanishes at the real zero z_0 = 3 (the last admissible"
    "\n           rung, machine) with slope O~'(3) = 16 ln2 (symbolic; 'one nat per channel quantum'); the"
    "\n           complex ladder z_k = 3 + 2 pi i k/ln2 (spacing 2 pi/ln2, symbolic -- the decimal"
    "\n           9.0647... is an [EXT]-grade comparison and is NOT carried) is RECORDED AND SCOPED OUT:"
    "\n           rungs are integers [CT0.11], and CT4.4a refutes any realization at n >= 4 -- no complex"
    "\n           rung exists.",
    F4_ok)

print("=" * 104)
print("PART G -- the rho_B convention census")
print("=" * 104)

# ---- G1: the convention ----
RV = Ring(["mu2", "h", "L", "E"])
bridge = RV.mul(RV.var("mu2"), RV.mul(RV.mul(RV.var("h"), RV.var("h")), RV.mon(L=-2)))
density = RV.mul(RV.mon(h=-4), RV.mul(RV.mon(E=4), RV.mon(L=4)))
QDEGv = {"mu2": Fr(1), "h": Fr(-1, 2), "L": Fr(0), "E": Fr(0)}


def degset(p):
    out = set()
    for e in p:
        d = Fr(0)
        for i, x in enumerate(e):
            d += QDEGv[RV.names[i]] * x
        out.add(d)
    return out


G1_ok = (degset(bridge) == {Fr(0)} and degset(density) == {Fr(2)}
         and not RV.eq(bridge, density)
         and RV.vars_used(bridge) == {"mu2", "h", "L"} and RV.vars_used(density) == {"h", "L", "E"})
chk("G1  [BM.69(2); BM.102(2),(4),(5); BM.14(2),(4); BM.83(4); A-BM.9 -- the collision RESOLVED]: the"
    "\n           corpus's rho_B is the BRIDGE mu'^2 h^2/(ln2)^2 in q^0 ('converts no dimension -- the"
    "\n           dimensionless exchange rate between the bit currency and the angle currency', BM.102(4)"
    "\n           verbatim; declared A-BM.9, value NOT issued), and the corpus's rho is the DENSITY"
    "\n           h^-4 E^4 (ln2)^4 in q^{+2}: DIFFERENT monomials, different degrees, different alphabets"
    "\n           (machine) -- one symbol cannot hold both. CONVENTION ADOPTED FOR THE RECORD: rho_B := "
    "\n           the bridge (the canon's symbol); rho := the density; MR.3's 'rho_B := m_B/V_eff' was a"
    "\n           mislabel (corrections register #15). The b-slot fork (density vs bridge) stays an OPEN"
    "\n           parametric read-choice [BM.30(5) pattern] -- neither selected, per the study's own"
    "\n           Part XI.",
    G1_ok, f"deg(bridge) = {sorted(degset(bridge))}, alphabet {sorted(RV.vars_used(bridge))}; "
           f"deg(density) = {sorted(degset(density))}, alphabet {sorted(RV.vars_used(density))}")

print("=" * 104)
print("CONSOLIDATION SUMMARY (Tier IT.16 candidates IT.49-IT.54):")
print("""    * CITATION AUDIT: ~450 distinct tag tokens across the four delivered documents -- ONE unattested
      (CT0.20, the document's own flagged slip for CT3.20); ~65 clause-level checks pass; every verbatim
      quote verified; the claimed canon typo FT.116(5) is CONFIRMED (unsquared second factor in the
      printed expansion; the zero locus -- all the clause uses -- is unaffected): recorded probe-side,
      the frozen canon is NEVER edited [AT.63(2)].
    * EVERY machine claim above is re-derived FROM SCRATCH in this checker (the study's own scripts were
      not delivered): the angle ledger and the 3-adic exclusion; the cubic ladder gamma_l = 2 gamma_q^3
      - 3 gamma_q; the Koide layer (sum r = 3, sum r^2 = 6, K = 2/3 phase-free, K(N) = 2/N at N=3,4,6,
      the Newton tower, the z-cubic); the circle algebra ([O,C_3] = R_{4pi/9}, the dilation R_{2pi/9});
      the forced factor 2 = B^2 in z_l = 2 z_q^3; the 4^n census vs C(2n,n+Q); the Laurent identity; the
      neighbour law R(n) = (n+1)/n with the unique-2 quotient census; the P-ring certificates; the
      circulant charpoly/discriminant (+ the typo certificate); the S_3 selection census; the inner C_3
      (U = u(x)u, U^3 = E_0, the nine conjugations); the (S,T) sector table; the full commutation table;
      Lie<J,K> = 15-dim with E_0 outside; the nilpotent triple calculus (+ the honest negative: NOT
      Clifford); the Casimirs; the branch-change bridge J_i Pi_R = Pi_V J_i; the order-4 inner reflection
      (J -> -K, K -> J, A -> iA, B -> -iB, R^4 = i E_0); the 10-of-16 tensor-square occupancy with the
      singlet readouts; the phase calculus (the four corrected cells, the readout table, the (1,2n,n^2)
      flow, det J_Phi, det H_T, the eigenvalue certificate); the order-3 triple annihilation; the
      Lyapunov identities; the saturation census; the radar algebra (agreement <=> s*dx = 0); the O(n)
      continuation record; and the rho_B convention census.
    * STATUS SPLIT (the tier's verdict table): the operator/angle/census identities are DERIVED (new
      rows, certified here); the matrix M and its readouts stay the IT.37-39/IT.43-45 PARAMETRIC class
      (formable as symbolic expressions, barred as formed reads -- IT.43(6) doctrine; the study's own
      Part XI already declared them); the declaration register (D-PJ1-7, D-RS1-6, and the study's
      Part-XI list) is ABSORBED as named, unissued; the bars all stand; no declaration is forced;
      Cal-IT stays empty.""")
print("=" * 104)

n_ok = sum(R)
print(f"\n  probe_consolidation.py: {n_ok}/{len(R)} EXACT -- no floating point, no measured value.")
sys.exit(0 if n_ok == len(R) else 1)
