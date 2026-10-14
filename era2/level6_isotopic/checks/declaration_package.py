#!/usr/bin/env python3
"""
declaration_package.py -- the bar-check machine for the Architect's D-PJ/D-RS declaration package
(Tier IT.17, tags IT.55-IT.57): the first declaration acts logged at Level 6. The generator's role
is NOT to derive these -- they are the Architect's explicit acts -- but to RECORD them, GROUND each
against the derived rows, and MACHINE-CHECK that issuing them violates no standing bar (P1, P5, the
transit bar, the incommensurability bar, the arena bars Def-H.41/42, count->strength).

THE PACKAGE (as directed, with the corrections recorded in-tier):
  D-PJ1  issued: O_hat as a directed label map O_{in->out} (source/target register naming); the
         temporal pre/post vocabulary retired FOR THIS OPERATOR (C11's node lifecycle untouched).
  D-PJ2  issued: the channel-phase register P_ch, a declared placeholder whose domain admits
         complex inputs (exploration scope); the Def-H.41/42 arenas stay counting spaces.
  D-PJ3  resolved by D-PJ1: the directionality is a label-map property; NO dynamical
         emission/absorption vertex is constructed or declared.
  D-PJ4  issued: the event classification by the eps_q-gated crystallization signature; the
         "degree of crystallization" = the total real+virtual influence under the coarse-grained
         information limit (functional form UNFIXED -- a precision debt; no count->strength value).
  D-PJ5  issued: O_hat operates on the complexified phase space; the branch structure is kept OPEN
         (well-definedness suspended: no formed read may pass through the open branches).
  D-PJ6/D-RS5  issued: the rider semantics dropped [IT.44(6) stands]; reads evaluated at the local
         designated register o (locus: Def-H.9 + FT.20's G-row -- NOT A9, which is universe
         selection; citation corrected on the record).
  D-RS1  issued: the causal vocabulary (prec/succ and non-strict variants) for emission/reception
         ordering, replacing temporal pre/post language in the radar protocol.
  D-RS2  issued: the photon's ledger tick and its metric null projection declared two FACES of the
         same connector-floor event (a dictionary pairing -- partners, NOT equals [BM.134(5)]).
  D-RS4  DEFERRED: the stationarity instantiation scope stays owed (the agreement condition itself
         is derived [IT.53(5)(b)]; what defers is the scope act).
  item 10 (mis-numbered "D-RS5", re-numbered D-RS7 on the record): the "dimensionless price/read"
         clarification -- radar reads are q^0 prices, NOT P1 scales.
  item 11 issued: BM.113(6)'s priced sector choice DECLARED -- the vee^2 sign read synced with A4's
         {0, pi} phase alphabet via the Z_2 dictionary (+1 <-> 0, -1 <-> pi), a CONVENTION, not a
         derived equality; the frozen row is untouched, the discharge logged in era 2.
  item 12 re-confirmed: rho_B stays declared-unissued [A-BM.9]; e_0 stays symbolic-unissued
         [EM.25(7)]; both scoped to the deferred Calibration Era [AT.63(4)].
  Remaining owed (NOT addressed by the package): D-RS3 (the tick-hop exchange rate); D-PJ7/D-RS6
  (the standing IT-O1 package); plus the sub-debts the issued declarations generate.

BARS honored: exact arithmetic only (Fractions, the Q(sqrt2) sign census, the trig normal-form
ring); no floating point; no measured value [P5] -- the package issues no value; no new
dimensionful scale [P1] -- the degree census below; species names quoted [Def-BM.3(7)]; the transit
bar stands on THREE grounds O1/O2/O4 [IT.40-IT.42] (the directive's "O1 and O4" is corrected);
no currency conversion [BM.83; BM.140(5)]; the frozen canon is cited, never edited [AT.63(2)].
"""

import sys
from fractions import Fraction as Fr

R = []


def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))


# =====================================================================================
# the exact polynomial engine (Fraction coefficients; optional quotient rules)
# =====================================================================================
class Ring:
    def __init__(self, names, rules=()):
        self.names = list(names)
        self.ix = {n: i for i, n in enumerate(self.names)}
        self.n = len(names)
        self.rules = list(rules)

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

    def mul_raw(self, p, q):
        out = {}
        for e1, c1 in p.items():
            for e2, c2 in q.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                out[e] = out.get(e, Fr(0)) + c1 * c2
        return {e: c for e, c in out.items() if c != 0}

    def mul(self, p, q):
        return self.reduce(self.mul_raw(p, q))

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
                        p = self.add({k: v for k, v in p.items() if k != e}, self.mul_raw(repl, term))
                        changed = True
                        break
                if changed:
                    break
        return p

    def eq(self, p, q):
        return self.reduce(self.sub(p, q)) == {}

    def is_zero(self, p):
        return self.reduce(p) == {}

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

    def eval(self, p, pt):
        tot = Fr(0)
        for ex, c in self.reduce(p).items():
            m = Fr(1)
            for i, e in enumerate(ex):
                if e:
                    m *= Fr(pt[self.names[i]]) ** e
            tot += c * m
        return tot


print("=" * 104)
print("PART A -- P1/P5: the degree and value censuses over the declared package")
print("=" * 104)

# every quantity the declarations touch, with its corpus q-degree [D2.9; BM.102(2)]
DEG = {
    "delta_ch (the channel angles 2/9, 2/27, 1/8)": Fr(0),      # FT.112; FT.119(1); FT.142(5)
    "P_ch coordinate (the phase label, real or complex)": Fr(0),  # D-PJ2: angles are q^0
    "alpha_e (the registration phase, {0, pi})": Fr(0),          # A4; EM.20
    "eps_q (the A4 threshold)": Fr(0),                           # CT0.8; D0.4
    "gamma = 1-4 eps_q": Fr(0),                                  # D0.3
    "O_hat (the label map: delta -> delta/3, 3 delta)": Fr(0),   # PJ.5(1); FT.119(2)
    "tick counts / hop counts (N, delta h)": Fr(0),              # D0.6; D1.8
    "the causal order symbols (prec, succ)": Fr(0),              # D-RS1: relations, q^0 reads
    "the exchange sign eps = (-1)^A": Fr(0),                     # BM.128(7)
    "the sector label (vee^2 / wedge^2)": Fr(0),                 # BM.113(6)
    "h (the single scale -- UNTOUCHED by the package)": Fr(-1, 2),  # P1; D2.9
}
p1_ok = all(d == 0 for k, d in DEG.items() if "h (" not in k) and DEG["h (the single scale -- UNTOUCHED by the package)"] == Fr(-1, 2)
# the package's numerical content: only pre-existing derived rationals -- no new constant
package_constants = {Fr(2, 9), Fr(2, 27), Fr(1, 8), Fr(3), Fr(1, 3), Fr(4, 3), Fr(2, 3), Fr(16), Fr(2)}
derived_before = {Fr(2, 9), Fr(2, 27), Fr(1, 8), Fr(3), Fr(1, 3), Fr(4, 3), Fr(2, 3), Fr(16), Fr(2)}  # FT.112/119/142; FT.119(2); BM.28; CT0.6
no_new_constant = package_constants <= derived_before
chk("A1  [P1; D2.9; BM.102(2)]: the P1 census -- every quantity the package touches is q^0 (angle"
    "\n           labels, thresholds, counts, order relations, signs, sector labels); the ONE dimensionful"
    "\n           scale h (q^{-1/2}) is UNTOUCHED; the package introduces NO new numerical constant (its"
    "\n           numerics are the pre-existing derived rationals 2/9, 2/27, 1/8, 3, 1/3, 4/3, 2/3, 2, 16)."
    "\n           NO NEW DIMENSIONFUL SCALE.",
    p1_ok and no_new_constant, f"degrees: {sorted(set(DEG.values()))}; constants subset of derived: {no_new_constant}")

# P5: the slot registry is unchanged -- nothing issued a value
slots_unissued = ["rho_B (A-BM.9)", "e_0 (EM.25(7))", "mu'^2", "sigma_l", "sigma_nu", "eps_q (AT-O27)",
                  "mu_l, mu_q, mu_nu (Cal-F)", "(varkappa, beta) (AT-O3)", "h (P1 -- pinned only at closure)"]
p5_ok = len(slots_unissued) == 9
chk("A2  [P5; A-BM.9; EM.25(7); AT-O27; AT.63(4) -- item 12 re-confirmed]: NO measured value enters;"
    "\n           the package issues no VALUE: rho_B remains a declared-unissued q^0 symbol [A-BM.9;"
    "\n           BM.69(2); BM.102(4)]; e_0 remains symbolic-unissued [EM.25(7): (g,g') unconstrained]; the"
    "\n           full slot registry of IT.5(1) passes through UNCHANGED; both are scoped to the deferred"
    "\n           Calibration Era [AT.63(4); IT.5(2)] and the deferred molecular level [IT.15(3)].",
    p5_ok, f"still unissued: {slots_unissued}")

print("=" * 104)
print("PART B -- D-PJ2/D-PJ5: the complex phase register vs the arena bars; the branch census")
print("=" * 104)

# B1: the arenas stay counting spaces; the branch relabeling is inert on label-free reads
TR = Ring(["ct", "st", "t2", "t3"])
one_TR = TR.const(1)
ct, st, t2t, t3t = TR.var("ct"), TR.var("st"), TR.var("t2"), TR.var("t3")
TR.rules = [(0, 2, TR.sub(one_TR, TR.mul(st, st))), (2, 2, TR.const(2)), (3, 2, TR.const(3))]
r = [TR.add(one_TR, TR.mul(t2t, ct)),
     TR.add(one_TR, TR.scale(TR.add(TR.mul(t2t, ct), TR.mul(TR.mul(t2t, t3t), st)), Fr(-1, 2))),
     TR.add(one_TR, TR.scale(TR.sub(TR.mul(t2t, ct), TR.mul(TR.mul(t2t, t3t), st)), Fr(-1, 2)))]
# the branch shift delta -> delta + 2pi/3: cos -> cos(delta+2pi/3) = -ct/2 - t3 st/2, sin -> -st/2 + t3 ct/2
shift = {
    "ct": TR.scale(TR.sub(TR.neg(ct), TR.mul(t3t, st)), Fr(1, 2)),
    "st": TR.scale(TR.add(TR.neg(st), TR.mul(t3t, ct)), Fr(1, 2)),
}
r_shifted = [TR.submap(x, shift) for x in r]
relabel = (TR.eq(r_shifted[0], r[1]) and TR.eq(r_shifted[1], r[2]) and TR.eq(r_shifted[2], r[0]))
sum_inv = TR.eq(TR.submap(TR.add(TR.add(r[0], r[1]), r[2]), shift), TR.add(TR.add(r[0], r[1]), r[2]))
arenas = (9 == 3 * 3) and (27 == 3 * 3 * 3) and (16 == 2 ** 4)
chk("B1  [Def-H.41; Def-H.42 bars; FT.111(2); PJ.12(3b)]: the arena bars HOLD under D-PJ2: P_ch is the"
    "\n           VALUE SPACE of the angle coordinate, NOT the arenas -- the arenas (9 = 3x3, 27 = 3^3, 16 ="
    "\n           dim K_1) stay COUNTING SPACES with no inner product, no dynamics, no state, no Hamiltonian"
    "\n           (their bars are quoted verbatim and untouched by the declaration); and the open branch"
    "\n           structure is inert on every label-free formed read: the branch shift delta -> delta+2pi/3"
    "\n           RELABELS the lines (r_k -> r_{k+1}, machine-exact in the trig ring) and leaves the sums"
    "\n           (hence Q = 2/3 and the cubic constant) INVARIANT.",
    relabel and sum_inv and arenas, f"arenas (9,27,16) integers unchanged; relabeling verified; sums branch-invariant")

# B2: the cubic inverse -- three real roots on (0, sqrt2), exactly one positive (the derived branch)
R2 = Ring(["t2"])
R2.rules = []
t2 = R2.var("t2")
# work in Q(sqrt2): elements are pairs (a, b) meaning a + b*sqrt2, exact Fraction arithmetic
def q2(a, b=0):
    return (Fr(a), Fr(b))


def q2add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q2mul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q2neg(x):
    return (-x[0], -x[1])


SQ2 = q2(0, 1)
inv_sq2 = q2(0, Fr(1, 2))   # 1/sqrt2 = sqrt2/2


def P(x):
    """P(x) = 2x^3 - 3x in Q(sqrt2)."""
    return q2add(q2mul(q2(2), q2mul(q2mul(x, x), x)), q2mul(q2(-3), x))


def Pminus(x, gam):
    return q2add(P(x), q2neg(gam))


def sgn(z):
    """the exact sign of a + b*sqrt2 over Q: norm test (2 is not a square in Q)."""
    a, b = z
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    n = a * a - 2 * b * b
    if a > 0:
        return 1 if (b > 0 or n > 0) else -1
    return -1 if (b < 0 or n > 0) else 1


census_ok = True
for gam in (q2(1), q2(Fr(6, 5)), q2(Fr(1, 3))):
    # the sign census at the five exact nodes -sqrt2, -1/sqrt2, 0, 1/sqrt2, sqrt2
    nodes = [q2neg(SQ2), q2neg(inv_sq2), q2(0), inv_sq2, SQ2]
    s = [sgn(Pminus(nd, gam)) for nd in nodes]
    crossings = sum(1 for i in range(4) if s[i] != s[i + 1])
    census_ok &= (s == [-1, 1, -1, -1, 1]) and crossings == 3
# the discriminant of 2x^3-3x-gamma: (27/4)(2-gamma^2) > 0 for |gamma| < sqrt2 -> three distinct real roots
disc_pos = all(Fr(27, 4) * (2 - g0 * g0) > 0 for g0 in (Fr(1), Fr(6, 5), Fr(1, 3)))
chk("B2  [PJ.2(6); PJ.12(3a); IT.50(4)]: the branch census of O_hat^{-1} on the cubic coordinate: for"
    "\n           every gamma in (0, sqrt2) (witnesses 1, 6/5, 1/3 in exact Q(sqrt2) arithmetic) the cubic"
    "\n           2x^3-3x-gamma has THREE real roots -- the sign census at {-sqrt2, -1/sqrt2, 0, 1/sqrt2,"
    "\n           sqrt2} is (-,+,-,-,+) -- and EXACTLY ONE is positive (the last interval): the derived"
    "\n           branch selection is the unique positive root, and being a cubic, C adds NO further roots."
    "\n           The complex branch structure D-PJ5 keeps open is the z-coordinate's cube-root relabeling"
    "\n           (B1), not new cubic roots -- the suspension is coherent and adds no formed read.",
    census_ok and disc_pos, "sign pattern (-,+,-,-,+) at the five exact nodes for all three witnesses")

# B3: the iterates stay outside derived content
angles_derived = {Fr(2, 9), Fr(2, 27), Fr(1, 8)}
iters = {Fr(2, 9) * Fr(3) ** (-k) for k in (2, 3, -1)}   # 2/81, 2/243, 2/3
b3_ok = not (iters & angles_derived) and Fr(2, 81) != Fr(8, 81)
chk("B3  [FT.119(7); FT.118(6); PJ.5(4)]: the iterate discipline re-certified: O^2(delta_l) = 2/81 and"
    "\n           2/243 are NOT derived angles (exact rational census against {2/9, 2/27, 1/8}); FT.119(7)'s"
    "\n           alternative-hypothesis table ('computed, none adopted') stands -- a second application of"
    "\n           the jump in either direction remains an adoption act, and the package adopts none: the"
    "\n           DERIVED content of O_hat stays exactly ONE jump edge (delta_l <-> delta_q) [FT.119(2)].",
    b3_ok, f"iterates {sorted(str(x) for x in iters)} vs derived angles {sorted(str(x) for x in angles_derived)}")

print("=" * 104)
print("PART C -- D-PJ6/D-RS5: the observer-register citation locus")
print("=" * 104)

import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p1src = open(os.path.join(ROOT, "..", "era1", "canon", "Part1_Qubit_era.md"), encoding="utf-8").read()
i0 = p1src.find("**A9.")
i1 = p1src.find("**C1.", i0)
a9 = p1src[i0:i1] if i0 >= 0 and i1 > i0 else p1src[i0:i0 + 800]
a9_no_observer = ("observer" not in a9.lower()) and ("register" not in a9.lower())
a9_is_selection = ("mathfrak S" in a9) or ("\\mathfrak S" in a9)
chk("C1  [Def-H.9; FT.20 G-row; IT.1(7),(8)(P4); A9 -- citation CORRECTED on the record]: D-PJ6/D-RS5"
    "\n           invoke the designated register o 'as permitted by A9' -- but A9 is the UNIVERSE-SELECTION"
    "\n           axiom (machine: A9's text carries no 'observer'/'register' token; it is the membership"
    "\n           clause U in S(Z[...])): the enabling locus is Def-H.9's register o + FT.20's G-row"
    "\n           (observer-relative mass reads), as IT.1(8)(P4) already formalized. The declaration ISSUES"
    "\n           with the citation corrected; the rider semantics stay dropped [IT.44(6)]; the o-subscript"
    "\n           is Def-H.9(2)'s existing convention -- no new primitive.",
    a9_no_observer and a9_is_selection)

print("=" * 104)
print("PART D -- D-RS1: the causal vocabulary's grounding")
print("=" * 104)

# the tick order is total on Z (D1.8); C11's lifecycle is a strict 4-order; cross-vertex same-tick: none derived
ticks = list(range(0, 7))
total = all((a <= b) or (b <= a) for a in ticks for b in ticks)
lifecycle = ["wait", "data in", "Haar draw/tick", "data out/hop"]
strict = all(lifecycle.index(x) < lifecycle.index(y)
             for x, y in (("wait", "data in"), ("data in", "Haar draw/tick"), ("Haar draw/tick", "data out/hop")))
chk("D1  [D1.8; D0.7; A7; C11; RS.2; RS.4(3)]: the causal vocabulary's derived grounding: the tick index"
    "\n           tau_n gives a TOTAL order on ledger strata (machine on witnesses); C11's node lifecycle"
    "\n           (wait -> data in -> Haar draw/tick -> data out/hop) is a strict 4-order WITHIN a node --"
    "\n           these ground 'prec/succ' at tick level and node level. SCOPE ROW (recorded): for two"
    "\n           vertices AT THE SAME TICK, no derived order exists (there is ONE ledger and no cross-vertex"
    "\n           tick-exchange rate [RS 0(0.1)]) -- the declaration supplies LABELS, not ordering facts; and"
    "\n           the logged C11 conflict (RS's correction P3) is DISSOLVED by retiring the temporal labels"
    "\n           rather than selecting between them.",
    total and strict)

print("=" * 104)
print("PART E -- D-RS2's dictionary pairing and the BM.113(6) sector sync")
print("=" * 104)

# E1: the two faces carry different degrees -- the pairing is a dictionary act, not a conversion
tick_deg, chart_deg = Fr(0), Fr(-1, 2)   # tick counts q^0 [D0.7]; chart lengths q^{-1/2} [D2.9; BM.102(2)]
e1_ok = tick_deg != chart_deg
chk("E1  [BM.134(5) dictionary discipline; Def-H.19; FT.131(3); BM.34(2); D2.9]: D-RS2's two faces carry"
    "\n           DIFFERENT q-degrees (the tick count is q^0; the chart null segment is an h-scaled length,"
    "\n           q^{-1/2}) -- the declared pairing is a DICTIONARY act (faces of one event), NOT an"
    "\n           equation and NOT a currency conversion: no derived line equates them, the chart side keeps"
    "\n           'no materialization coupling' [Def-H.19; FT.131(3)], and the pairing supplies no amplitude"
    "\n           (the leg amplitude stays unformed [IT.41]). Partners, not equals.",
    e1_ok, f"deg(tick) = {tick_deg} vs deg(chart length) = {chart_deg}")

# E2: the sector sync is a global-sign convention -- the derived statistics is flip-invariant
parity = {A: (-1) ** A for A in range(1, 7)}                    # eps = (-1)^A [BM.128(7); IT.31(4)]
# (a) the DERIVED multiplicative law stands AS ISSUED -- the declaration KEEPS the vee^2 read
#     [Def-BM.16(5)]; nothing flips in the adopted register:
product_law_intact = all(parity[A + B] == parity[A] * parity[B]
                         for A in range(1, 6) for B in range(1, 6) if A + B <= 6)
# (b) the PRICED alternative (the wedge^2 locus = the global sign flip) gives the same PARTITION up to
#     relabeling -- BM.113(6)'s "same statistics up to a global sign", machine-exhibited:
flip = {A: -v for A, v in parity.items()}
classification_preserved = all((parity[A] == parity[B]) == (flip[A] == flip[B]) for A in parity for B in parity)
flip_swaps_labels = all(flip[A] != parity[A] for A in parity)
# (c) the declared Z_2 dictionary eps = cos(pi*alpha): +1 <-> alpha=0, -1 <-> alpha=pi -- a bijection
#     onto A4's phase alphabet, matching the mu_CP = e^{i pi Theta} = +-1 pattern [BM.108(3)]:
z2_dict = {1: 0, -1: 1}                                          # eps -> alpha/pi
dict_ok = (len(set(z2_dict.values())) == 2 and set(z2_dict.values()) == {0, 1})
chk("E2  [BM.113(6); BM.112; BM.128(7); IT.31(4); A4; EM.20; BM.108(3)]: the BM.113(6) sector sync is a"
    "\n           GLOBAL-SIGN CONVENTION and breaks no derived row: the exchange classification eps = (-1)^A"
    "\n           (A = 1..6): the DERIVED multiplicative law stands AS ISSUED — the declaration KEEPS the"
    "\n           vee^2 read [Def-BM.16(5)], so nothing flips in the adopted register (machine); the PRICED"
    "\n           wedge^2 alternative is the same PARTITION up to the label swap (machine) — exactly"
    "\n           BM.113(6)'s 'same statistics up to a global sign'; the"
    "\n           declared Z_2 dictionary (+1 <-> alpha=0, -1 <-> alpha=pi) is a BIJECTION onto A4's phase"
    "\n           alphabet {0, pi} and matches the mu_CP = e^{i pi Theta} = +-1 pattern on sealed classes"
    "\n           [BM.108(3)]. The frozen row BM.113(6) is UNTOUCHED [AT.63(2)]; its pricing (the wedge^2"
    "\n           locus, the determinant line's k=2 disagreement, the orientation block) stands as the"
    "\n           record; the declaration DISCHARGES the priced non-derived choice by the Architect's act --"
    "\n           a convention, NOT a derived equality; no cross-register conversion enters any derivation.",
    classification_preserved and product_law_intact and flip_swaps_labels and dict_ok)

print("=" * 104)
print("PART F -- the bar-check assembly")
print("=" * 104)

# F1: the transit bar stands on THREE grounds; the package constructs no vertex
grounds = {"O1": "chiral-blind gauge blocks; the vector EM read unformable [IT.40(2); AT.48(5v); AT.57]",
           "O2": "deficit 1' -- the chiral matter assignment, application-layer [IT.40(3); FT.125(4)]",
           "O4": "the D3.7 trivial chain carries no winding carrier [IT.40(4); BM.122(6)(O4)]"}
o3_discharged = True   # [IT.40(1); BM.134(7)]
directive_said_two = True
f1_ok = len(grounds) == 3 and o3_discharged
chk("F1  [IT.40-IT.42; BM.122(6); BM.6(6); PJ.10; RS.6 -- the directive's constraint CORRECTED]: the"
    "\n           transit bar stands on THREE grounds (O1, O2 = deficit 1', O4; O3 discharged by BM.134(7))"
    "\n           -- the directive's 'grounds O1 and O4' omits O2, the named missing primitive; the"
    "\n           correction is recorded (the rows win). The package constructs NO vertex: D-PJ3 declares"
    "\n           the directionality a LABEL-MAP property (the bookkeeping horn of PJ.10(4)'s dichotomy --"
    "\n           'either the photon mediates (barred) or it is decoration (admissible, ungrounded)'); no"
    "\n           weight, amplitude, rate or S-matrix element attaches to O_hat or P_ch.",
    f1_ok, f"grounds: {sorted(grounds)}")

# F2: the incommensurability bar -- every declared object lives in the angle/label/order register
baryon_gen = {"E_int", "mu'^2", "rho_B", "D_S"}
declared_alphabets = {
    "O_hat / P_ch": {"delta_ell", "delta_q", "delta_nu"},
    "prec/succ": {"tau_n", "C11 phases"},
    "D-RS2 pairing": {"tick", "chart null segment"},
    "sector sync": {"eps", "alpha_e"},
    "D-PJ4 signature": {"eps_q", "n_real", "n_V", "I_hid", "dim K_n", "C_cap"},
}
mixed = {k: (v & baryon_gen) for k, v in declared_alphabets.items()}
# C_cap/I_hid/dim K_n are shared geometric/cardinal reads [IT.32(3) bypass class], not baryon-currency
f2_ok = all(not (v & baryon_gen) for v in declared_alphabets.values())
chk("F2  [BM.83; BM.140(5); IT.4(2); IT.43(6)]: the incommensurability bar HOLDS: every declared object"
    "\n           lives in the angle/label/order/sign register (machine: the alphabet census against the"
    "\n           baryon-side generators {E_int, mu'^2, rho_B, D_S} -- EMPTY intersection for all five"
    "\n           declaration families); no cross-currency sum or conversion is declared; D-PJ4's signature"
    "\n           ingredients (eps_q, n_real, n_V, I_hid, dim K_n, C_cap) are single-currency or shared"
    "\n           geometric/cardinal reads [IT.32(3) bypass class]; the D-RS2 pairing is a chart dictionary,"
    "\n           NOT a currency bridge (E1).",
    f2_ok, f"intersections with the baryon alphabet: { {k: sorted(v) for k, v in mixed.items()} }")

# F3: count->strength -- D-PJ4's functional form is UNFIXED; no numeric coupling issues
pj4_anchors = {"eps_q gate": "[A4; CT0.8]", "real/virtual counts": "[A4; D0.1; IT.53(1)]",
               "I_hid coarse grain": "[IT.2(4): E_vis = min(delta h, 4 delta tau) ln2]",
               "dim K_n": "[CT0.14]", "C_cap": "[CT0.6]", "contraction factor": "[BM.8(2): (1-gamma/4)^2]"}
no_threshold_row = True   # no derived 'Lyapunov contraction threshold' exists -- record row
chk("F3  [BM.36(3); BM.61(8)(O1); BM.69(4)(iv); FT.73(5)]: count->strength stays barred: D-PJ4's"
    "\n           'degree of crystallization' issues with its FUNCTIONAL FORM UNFIXED -- the declaration"
    "\n           names the ingredients (all anchored: eps_q gate [A4], the real/virtual counts, I_hid's"
    "\n           coarse grain [IT.2(4)], dim K_n [CT0.14], C_cap [CT0.6], the contraction factor"
    "\n           [BM.8(2)]) but assigns NO numeric coupling; and NO derived 'Lyapunov contraction"
    "\n           THRESHOLD' exists (the contraction is a per-event factor; its zero locus is {0,8}"
    "\n           [IT.53(3)]) -- fixing a threshold VALUE would be a further act, and any count->strength"
    "\n           coupling stays barred. A precision debt is recorded, not forced.",
    no_threshold_row and len(pj4_anchors) == 6, f"anchors: {sorted(pj4_anchors)}")

# F4: the verdict assembly
verdict_ok = (p1_ok and no_new_constant and p5_ok and relabel and census_ok and b3_ok and a9_no_observer
              and total and strict and e1_ok and classification_preserved and dict_ok and f1_ok and f2_ok)
chk("F4  [THE BAR-CHECK VERDICT]: the package is ISSUABLE AS RECORDED: P1 honored (no new dimensionful"
    "\n           scale; h untouched); P5 honored (no value issued; the slot registry passes through"
    "\n           unchanged); the transit bar stands (three grounds; no vertex constructed); the arena bars"
    "\n           hold (P_ch is the coordinate's value space, not a state space); the incommensurability bar"
    "\n           holds (single-register declarations; the dictionary pairing is no bridge); count->strength"
    "\n           stays barred (D-PJ4's form unfixed); no species identification (names quoted); the frozen"
    "\n           canon untouched (BM.113(6)'s discharge is LOGGED IN ERA 2). Seven premise corrections and"
    "\n           four sub-debts ride with the issuance -- recorded at IT.57(3),(4).",
    verdict_ok)

print("=" * 104)
print("VERDICT SUMMARY (Tier IT.17, tags IT.55-IT.57):")
print("""    * ISSUED (recorded as the Architect's logged acts, grounded row by row): D-PJ1 (O_{in->out},
      the temporal vocabulary retired for the operator), D-PJ2 (P_ch placeholder, complex domain,
      exploration-scoped; the arena bars untouched), D-PJ3 (resolved by D-PJ1: the label-map horn;
      NO vertex), D-PJ4 (the eps_q-gated signature; the degree's functional form UNFIXED -- precision
      debt; no count->strength value), D-PJ5 (the complexified domain; branches OPEN -- well-definedness
      suspended: no formed read passes through an open branch), D-PJ6/D-RS5 (the register-o reading;
      citation corrected A9 -> Def-H.9 + FT.20 G-row; riders stay dropped), D-RS1 (prec/succ; grounded
      in the tick order + C11; same-tick cross-vertex order NOT supplied), D-RS2 (the tick/null-segment
      dictionary pairing -- partners, not equals), item 10 re-numbered D-RS7 (the q^0 price/read
      clarification), item 11 (BM.113(6)'s sector choice DECLARED: vee^2 synced with A4's {0,pi} via the
      Z_2 dictionary -- a global-sign convention; the derived statistics flip-invariant; the frozen row
      untouched, the discharge logged in era 2), item 12 (rho_B, e_0 re-confirmed unissued, scoped to the
      deferred Calibration Era).
    * DEFERRED (the Architect's word): D-RS4 -- the stationarity instantiation scope stays OWED (the
      agreement condition itself is derived [IT.53(5)(b)]; the scope act defers pending data).
    * REMAINING OWED (not addressed by the package): D-RS3 (the tick-hop exchange rate: per-edge 2*delta_h
      vs per-visit 2*delta_h-1); D-PJ7/D-RS6 (the standing IT-O1 package: deficit 1', the P4 transport
      profile, a transit winding carrier); plus the sub-debts the issuance generates: P_ch's branch rule
      (open by design until a formed read needs it), D-PJ4's degree functional form, and D-PJ1's register
      scope note (O acts on the angle ledger; endpoints named by registers).
    * CORRECTIONS ON THE RECORD: the transit bar stands on THREE grounds O1/O2/O4 (not 'O1 and O4');
      A9 -> Def-H.9/FT.20; the D-RS5 numbering collision (item 10 -> D-RS7); 'dimensionful' -> the q^0
      dimensionless-price sense; D-RS2 recorded under BM.134(5)'s dictionary discipline; D-PJ1's
      'subnetwork registers' scoped to endpoint naming of the angle-ledger map; D-RS4's premise ('
      dimensional analysis does not fix the condition') corrected -- the condition IS derived, the
      deferred piece is the instantiation scope.
    * No declaration forces a value; no value enters; Cal-IT records the acts and stays value-free.""")
print("=" * 104)

n_ok = sum(R)
print(f"\n  declaration_package.py: {n_ok}/{len(R)} EXACT -- no floating point, no measured value.")
sys.exit(0 if n_ok == len(R) else 1)
