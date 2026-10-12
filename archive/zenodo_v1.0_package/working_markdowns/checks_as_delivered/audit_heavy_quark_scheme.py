#!/usr/bin/env python3
"""audit_heavy_quark_scheme.py — floating-point companion to verify_H_colour_channel.py §E.

AUDIT-ONLY.  This script is numerical: it cross-checks the exact rational ledger of
verify_H_colour_channel.py §E (H17/FT.120) in floating point, and tabulates the scheme
dependence of the heavy-triplet audit rows.  No assertion here is load-bearing for the
corpus; the exact-arithmetic script is.  External data ([EXT], PDG-2024-class) enter
here for comparison only — never as inputs to any corpus result (P1, P5).

Derived side (from FT.119, delta_q = 2/27, A=1, B=sqrt2):
    r_i   = 1 + sqrt2 cos(2/27 + 2 pi i / 3)
    m_i   ∝ r_i^2
    ratios: r2^2/r1^2 = 3.563695074946..., r0^2/r1^2 = 139.3386880284...
    anchored: r2^2/r0^2 = 0.025575776..., r1^2/r0^2 = 0.007176757...

Ledger side ([EXT]): three scheme columns S1/S2/S3 (see FT.120), the Koide-type
invariant Q = sum(m)/(sum sqrt(m))^2, B^2/A^2 = 6Q - 2, shortfalls, the light-triplet
ratio box, the remaining quark triplets, and the established-hadron range.

Run: python3 audit_heavy_quark_scheme.py     (exit 0 = windows reproduce the exact ledger)
"""
import math

# ------------------------- derived channel values (FT.119) -------------------------
DQ = 2.0 / 27.0
r = [1.0 + math.sqrt(2.0) * math.cos(DQ + 2.0 * math.pi * i / 3.0) for i in (0, 1, 2)]
r0, r1, r2 = r
RM = (r2 / r1) ** 2          # mid ratio  m2/m1
RO = (r0 / r1) ** 2          # top ratio  m3/m1
BT = (r2 / r0) ** 2          # anchored   m2/m3
CT = (r1 / r0) ** 2          # anchored   m1/m3

def Q_of(ms):
    s = sum(math.sqrt(m) for m in ms)
    return sum(ms) / (s * s)

print("=" * 92)
print("audit_heavy_quark_scheme — floating-point companion to verify_H_colour_channel.py §E")
print("=" * 92)
print(f"derived (delta_q = 2/27):  r = ({r1:.15f}, {r2:.15f}, {r0:.15f})   [sorted: r1 < r2 < r0]")
print(f"  sum r = {r0+r1+r2:.15f} (exact 3)   sum r^2 = {r0*r0+r1*r1+r2*r2:.15f} (exact 6)")
print(f"  ratios m1 : m2 : m3 = 1 : {RM:.12f} : {RO:.10f}")
print(f"  anchored:  m2/m3 = {BT:.12f}   m1/m3 = {CT:.12f}")
print(f"  channel invariant Q = sum r^2 / (sum r)^2 = {6/9:.15f} = 2/3 for every delta (normalization content)")
print()

# ------------------------- [EXT] scheme ledger (FT.120) -------------------------
EXT = {   # scheme column: (m1, m2, m3) in GeV  [EXT: supplied measured data, PDG-2024 class]
    "S1 own-scale MSbar     ": (1.273, 4.183, 162.5),
    "S2 MSbar c,b + pole t  ": (1.273, 4.183, 172.4),
    "S3 pole-type           ": (1.67,  4.78,  172.4),
}
print("[EXT] scheme ledger (audit-only; values enter no derivation):")
print(f"  {'scheme':24s} {'m2/m1':>10s} {'m3/m1':>11s} {'short_mid':>10s} {'short_top':>10s} {'Q':>9s} {'6Q-2':>8s} {'|Q-2/3|':>8s}")
ok = True
for name, (m1, m2, m3) in EXT.items():
    omid, otop = m2 / m1, m3 / m1
    smid, stop = omid / RM, otop / RO
    Q = Q_of((m1, m2, m3))
    b2 = 6.0 * Q - 2.0
    print(f"  {name:24s} {omid:10.6f} {otop:11.4f} {smid:10.6f} {stop:10.6f} {Q:9.6f} {b2:8.5f} {abs(Q-2/3):8.5f}")
    ok &= (0.0 < smid < 1.0) and (0.0 < stop < 1.0) and (1.7 < b2 < 2.1)
# anchored rows (S1 column)
m1, m2, m3 = EXT["S1 own-scale MSbar     "]
rel_b = abs(m2 / m3 - BT) / (m2 / m3)
rel_c = abs(m1 / m3 - CT) / (m1 / m3)
print(f"  anchored (S1):  m2/m3 obs = {m2/m3:.6f} vs derived {BT:.6f}  -> relative margin {rel_b:.4f}  (< 1% required)")
print(f"                  m1/m3 obs = {m1/m3:.6f} vs derived {CT:.6f}  -> relative margin {rel_c:.4f}  (> 5% expected: the inner member is the outlier)")
ok &= rel_b < 0.01 and rel_c > 0.05
print()

# ------------------------- Q is scheme-scale invariant below thresholds -------------------------
eta = 0.53   # arbitrary uniform rescaling (illustrative running factor)
Qa, Qb = Q_of((1.273, 4.183, 162.5)), Q_of((1.273*eta, 4.183*eta, 162.5*eta))
print(f"scale-invariance check: Q(m) = {Qa:.12f},  Q(eta*m) = {Qb:.12f}  (identical: Q is invariant under m -> eta*m)")
ok &= abs(Qa - Qb) < 1e-12
print()

# ------------------------- the remaining SM quark triplets ([EXT]) -------------------------
OTHER = {
    "light  (u,d,s) @2 GeV  ": (0.00216, 0.00470, 0.0935),
    "down-type (d,s,b) @2GeV": (0.00470, 0.0935, 4.183),
    "up-type (u,c,t) MSbar t": (0.00216, 1.273, 162.5),
    "up-type (u,c,t) pole t ": (0.00216, 1.273, 172.4),
    "(c,s,b) mixed           ": (1.273, 0.0935, 4.183),
}
print("[EXT] the remaining quark triplets (context census; audit-only):")
print(f"  {'triplet':24s} {'Q':>9s} {'|Q-2/3|':>9s}   verdict vs the channel surface Q = 2/3")
for name, ms in OTHER.items():
    Q = Q_of(ms)
    verdict = "ON the surface (within 1%)" if abs(Q - 2/3) < 0.01 else "off the surface"
    print(f"  {name:24s} {Q:9.5f} {abs(Q-2/3):9.5f}   {verdict}")
    if "light" in name or "down-type" in name or "up-type" in name:
        ok &= abs(Q - 2/3) > 0.06
print()

# ------------------------- light-triplet obstruction box (FT.120(6)) -------------------------
print("[EXT] light-triplet ratio box (m_u/m_d = 0.462 +/- 0.020; m_s/m_d in [17,22]):")
qs = []
for ru in (0.442, 0.462, 0.482):
    row = []
    for rs in (17.0, 19.9, 22.0):
        Q = Q_of((ru, 1.0, rs))
        row.append(Q); qs.append(Q)
    print(f"  r_u = {ru:.3f}:  Q = " + "  ".join(f"{q:.5f}" for q in row))
print(f"  box range: [{min(qs):.5f}, {max(qs):.5f}]  < 3/5 < 2/3  ->  B^2/A^2 = 6Q-2 in [{6*min(qs)-2:.4f}, {6*max(qs)-2:.4f}] vs derived 2")
ok &= max(qs) < 0.6 and min(qs) > 0.54
print()

# ------------------------- hadron range obstruction (FT.120(7)) -------------------------
pi0 = 0.1349768          # GeV [EXT]
span = 11.0 / pi0        # heaviest established hadron below ~11 GeV
print(f"[EXT] established-hadron span: 11 GeV / m_pi0 = {span:.3f} < 82 << derived top ratio {RO:.4f} (and << FT.113's 3477.47)")
ok &= span < 82.0 < RO
print()

# ------------------------- illustrative common-scale column (S4; audit-only, no running model declared) --
# What the derived channel would require of the inner and outer member given the S1 middle mass:
mb = 4.183
mc_star = mb / RM          # inner member demanded by the derived mid ratio
mt_star = mb / BT          # outer member demanded by the derived anchored ratio
print("illustrative S4 (what the derived channel asks of a common-scale column, given m2 = 4.183):")
print(f"  m1* = m2 / {RM:.6f} = {mc_star:.5f} GeV   (vs own-scale 1.273: {(mc_star/1.273-1)*100:+.2f}% — the size of a modest MSbar running step)")
print(f"  m3* = m2 / {BT:.9f} = {mt_star:.3f} GeV  (vs own-scale MSbar 162.5: {(mt_star/162.5-1)*100:+.2f}%)")
print(f"  the S1/S2 Q values bracket 2/3 from below and above (0.66260 / 0.66911): surface membership is scheme-robust;")
print(f"  the position on the surface (delta) is scheme-sensitive, and no canonical renormalization point is derivable")
print(f"  in the corpus (item 20 deficit 7: no second dimensionful scale). Recorded, not adopted.")
ok &= 1.10 < mc_star < 1.25 and 160.0 < mt_star < 170.0
print()

# ------------------------- alternative-hypothesis table (FT.119(7); none adopted) -------------------------
print("alternative delta hypotheses (computed, NOT adopted — FT.118(6)/FT.119(7)):")
for nm, dl in (("2/81 (per-baryon arena 3*27)", 2/81), ("1/36 = 2/72 (arena 9 x adjoint 8)", 1/36), ("8/81 (adjoint-dressed numerator)", 8/81)):
    rr = sorted(1.0 + math.sqrt(2.0) * math.cos(dl + 2.0 * math.pi * i / 3.0) for i in range(3))
    print(f"  delta = {nm:34s} -> 1 : {(rr[1]/rr[0])**2:.4f} : {(rr[2]/rr[0])**2:.3f}")
print()

print("audit_heavy_quark_scheme:", "ALL WINDOWS REPRODUCE THE EXACT LEDGER (§E)" if ok else "WINDOW MISMATCH — see above")
raise SystemExit(0 if ok else 1)
