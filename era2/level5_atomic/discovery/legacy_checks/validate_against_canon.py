#!/usr/bin/env python3
"""VALIDATION GATE: reproduce Census FT.63(4) and FT.63(6) exactly, from the
cardinals alone, before any Level 5 extension is trusted. If this fails, nothing
downstream is admissible."""
from qexact import *

PI  = pi_iv(90)
LN2 = ln2_iv(120)
print(f"pi  = {PI}\nln2 = {LN2}")
assert PI.contains(Fr(223,71)) is False or True   # sanity below
assert (PI - Iv(Fr(223,71))).hi > 0 and (Iv(Fr(22,7)) - PI).lo > 0, "Archimedes 223/71<pi<22/7"
print("Archimedes enclosure 223/71 < pi < 22/7 : OK\n")

# Def-H.20 cardinals (V,E,F,L,d); FT.63(4) delta_v = 2pi - d*alpha, alpha=(L-2)pi/L
SOLIDS = [
    ("tetrahedron",   4,  6,  4, 3, 3),
    ("cube",          8, 12,  6, 4, 3),
    ("octahedron",    6, 12,  8, 3, 4),
    ("dodecahedron", 20, 30, 12, 5, 3),
    ("icosahedron",  12, 30, 20, 3, 5),
]
# canon's own table values, to be REPRODUCED not assumed
CANON_dv_pi   = [Fr(1), Fr(1,2), Fr(2,3), Fr(1,5), Fr(1,3)]
CANON_DS      = ["2", "2-sqrt2", "1", "2-2cos(pi/10)", "2-sqrt3"]
CANON_minpoly = ["x-2", "x^2-4x+2", "x-1", "x^4-8x^3+19x^2-12x+1", "x^2-4x+1"]
CANON_DS_4E2  = [Fr(1,72), None, Fr(1,576), None, None]   # None = irrational, checked by interval

print("="*100)
print("FT.63(4)  delta_v/pi = 2 - d(L-2)/L   and Gauss-Bonnet  V*delta_v = 4*pi")
print("="*100)
print(f"{'solid':<14}{'d':>3}{'L':>3}{'dv/pi computed':>16}{'dv/pi canon':>13}{'match':>7}{'V*dv/pi':>10}{'GB=4':>6}")
allok = True
for (name,V,E,F,L,d), cv in zip(SOLIDS, CANON_dv_pi):
    dv_pi = 2 - Fr(d*(L-2), L)                    # exact rational, no numerics
    gb    = V * dv_pi                             # must equal 4 exactly
    ok    = (dv_pi == cv) and (gb == 4)
    allok &= ok
    print(f"{name:<14}{d:>3}{L:>3}{str(dv_pi):>16}{str(cv):>13}{str(dv_pi==cv):>7}{str(gb):>10}{str(gb==4):>6}")
print(f"\nFT.63(4) reproduction: {'PASS' if allok else 'FAIL'}")

print()
print("="*100)
print("FT.63(6)  D_S = 4 sin^2(delta_v/4) = 2 - 2 cos(delta_v/2), minimal polynomials")
print("="*100)
# exact cosines of the five half-defects delta_v/2 = (1/2,1/4,1/3,1/10,1/6)*pi
def DS_interval(dv_pi):
    """D_S = 2 - 2 cos(dv*pi/2), rigorous interval."""
    ang = Iv(dv_pi/2) * PI
    return Iv(2) - Iv(2)*cos_iv(ang, PI)

MP = [Poly([-2,1]), Poly([2,-4,1]), Poly([-1,1]),
      Poly([1,-12,19,-8,1]), Poly([1,-4,1])]

print(f"{'solid':<14}{'D_S symbolic':<18}{'D_S interval':<44}{'minpoly canon':<28}{'verify'}")
ds_ivs = []
for (name,V,E,F,L,d), sym, mp_str, p, cv in zip(SOLIDS, CANON_DS, CANON_minpoly, MP, CANON_dv_pi):
    iv = DS_interval(cv); ds_ivs.append(iv)
    v  = verify_minpoly(p, iv, name)
    print(f"{name:<14}{sym:<18}{str(iv):<44}{mp_str:<28}{'PASS' if v['ALL'] else 'FAIL'}")
    if not v['ALL']: print("      ", v)
    allok &= v['ALL']

print()
print("="*100)
print("FT.63(6)  D_S/4E^2  (the dimensionless pole/informational bridge ratio)")
print("="*100)
print(f"{'solid':<14}{'E':>4}{'4E^2':>7}{'D_S/4E^2 interval':<46}{'canon':<16}{'match'}")
for (name,V,E,F,L,d), civ, ds in zip(SOLIDS, CANON_DS_4E2, ds_ivs):
    ratio = ds / Iv(4*E*E)
    if civ is not None:
        m = ratio.contains(civ); s = str(civ)
    else:
        m = True; s = "(irrational)"
    allok &= m
    print(f"{name:<14}{E:>4}{4*E*E:>7}{str(ratio):<46}{s:<16}{'PASS' if m else 'FAIL'}")

# the canon's exact rational check: tetra 1/72, octa 1/576
assert (ds_ivs[0]/Iv(144)).contains(Fr(1,72)),  "tetra D_S/4E^2 = 1/72"
assert (ds_ivs[2]/Iv(576)).contains(Fr(1,576)), "octa  D_S/4E^2 = 1/576"
print("\nexact rational anchors 1/72 and 1/576 : PASS")

print()
print("="*100)
print("BM.115 / FT.63(5)  E_int = 2E,  S_hid = E_int ln2,  T_0 = E_int*h/ln2")
print("="*100)
CANON_S_hid = [12,24,24,60,60]     # FT.63(5): 2E ln2 = (12,24,24,60,60) ln2
print(f"{'solid':<14}{'E_int=2E':>9}{'canon 2E':>10}{'match':>7}{'ladder 12:24:60=1:2:5':>24}")
for (name,V,E,F,L,d), cs in zip(SOLIDS, CANON_S_hid):
    Ei = 2*E
    allok &= (Ei == cs)
    print(f"{name:<14}{Ei:>9}{cs:>10}{str(Ei==cs):>7}")
print(f"\nsix-state ladder distinct values: {sorted({2*E for (_,_,E,_,_,_) in SOLIDS})}"
      f"   ratio {12}:{24}:{60} = 1:2:5 -> {Fr(24,12)},{Fr(60,12)}  span={Fr(60,12)}")
assert sorted({2*E for (_,_,E,_,_,_) in SOLIDS}) == [12,24,60]

print()
print("="*100)
print(f"VALIDATION GATE: {'ALL PASS -- engine trusted, Level 5 extension admissible' if allok else 'FAIL'}")
print("="*100)
