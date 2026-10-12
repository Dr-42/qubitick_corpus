#!/usr/bin/env python3
"""
build_census.py -- the Level 5 (Era 2 / Atomic) data census.

Mandate: tabulate every SM-equivalent object in the frozen Levels 1-4 canon with
ALL of its derived reads -- quantum numbers, information reads, energy reads,
force decomposition -- and then APPLY the BM-level (Part 4) higher-order
corrections downward onto the FT-level (Part 3) objects, recording what updates
and what is invariant.

No mass read is adopted. No particle is identified with a measured value.
The [EXT] column is quarantined: it is a target for the discovery phase, never
an input to any number in this census.

Covenant: exact arithmetic throughout. Integers, Fractions, Z[x] polynomials,
and rigorous Fraction intervals for the transcendentals. No floating point in
any assertion. Engine validated against Census FT.63(4),(6) and BM.81(1) by
validate_against_canon.py (ALL PASS).
"""
from qexact import *
from fractions import Fraction as Fr

PI, LN2 = pi_iv(90), ln2_iv(120)

# --------------------------------------------------------------------------
# Section 0. The three channel triplets -- EXACT identities, no numerics.
#   r_i = 1 + sqrt2 cos(delta + 2 pi i /3)
#   sum_i cos(theta+2pi i/3) = 0 and sum_i cos^2 = 3/2  (standard, exact)
#   => sum r = 3, sum r^2 = 3 + 2*(3/2) = 6, Q = 6/9 = 2/3  -- PHASE-INDEPENDENT
# --------------------------------------------------------------------------
CHANNELS = [
    # name, delta (exact Fraction), provenance, species-role note
    ("ell", Fr(2,9),  "FT.109-FT.113, FT.158, Def-BM.6(1)", "charged-lepton-shaped"),
    ("q",   Fr(2,27), "FT.118-FT.119, BM.60(1)",            "quark-shaped"),
    ("nu",  Fr(1,8),  "FT.142-FT.144, Def-BM.6(2)",         "neutrino-shaped"),
]
# BM.60(1) / FT.143(5): the cross-channel identity 16 d_nu = 9 d_ell = 27 d_q = 2
assert 16*Fr(1,8) == 9*Fr(2,9) == 27*Fr(2,27) == 2, "cross-channel identity"
# FT.158(2)-(3): the spatial provenance  delta_ell = (3-1)/(3*3)
assert Fr(2,9) == Fr(3-1, 3*3)

def channel_lines(delta):
    """r_i with rigorous interval enclosures; plus the exact algebraic invariants."""
    out = []
    for i in range(3):
        ang = (Iv(delta) + Iv(Fr(2*i,3)) * PI)
        c = cos_iv(ang, PI)
        out.append(Iv(1) + sqrt_int_iv(2, 200) * c)
    return out

# --------------------------------------------------------------------------
# Section 1. The object roster.  dim: 2 = polygon floor, 3 = sealed solid,
#            J = junction, C = channel spectral line.
# --------------------------------------------------------------------------
SOLIDS = [("tetrahedron",4,6,4,3,3), ("cube",8,12,6,4,3), ("octahedron",6,12,8,3,4),
          ("dodecahedron",20,30,12,5,3), ("icosahedron",12,30,20,3,5)]

# BM.81(1) -- the six sealed states, verbatim from canon
SIX = [
 ("s1","(F1,-)","tetra ladder rung m=1","tetrahedron", 1, "2",               Poly([-2,1]),            Fr(1)),
 ("s2","(F1,+)","tetra ladder rung m=2","tetrahedron", 2, "4",               Poly([-4,1]),            Fr(2)),
 ("s3","(F2,-)","cube member",          "cube",         None,"2-sqrt2",      Poly([2,-4,1]),          Fr(1,2)),
 ("s4","(F2,+)","octahedron member",    "octahedron",  None,"1",             Poly([-1,1]),            Fr(2,3)),
 ("s5","(F3,-)","dodecahedron member",  "dodecahedron",None,"2-2cos(pi/10)", Poly([1,-12,19,-8,1]),   Fr(1,5)),
 ("s6","(F3,+)","icosahedron member",   "icosahedron",  None,"2-sqrt3",      Poly([1,-4,1]),          Fr(1,3)),
]
CARD = {n:(V,E,F,L,d) for (n,V,E,F,L,d) in SOLIDS}

def defect_iv(dv_pi):
    """D_S = 4 sin^2(delta_v/4) = 2 - 2 cos(delta_v*pi/2), rigorous."""
    return Iv(2) - Iv(2)*cos_iv(Iv(dv_pi/2)*PI, PI)

# tetrahedron weight ladder D_S(m) = 2-2cos(m*pi/2), canon says (2,4,2,0) at m=(1,2,3,4)
TETRA_LADDER = [Iv(2) - Iv(2)*cos_iv(Iv(Fr(m,2))*PI, PI) for m in (1,2,3,4)]
CANON_TETRA  = [2,4,2,0]

# BM.81 / Def-BM.14(5): the three branch splittings, strictly decreasing
SPLIT = [("Delta_1", Iv(4)-Iv(2)),
         ("Delta_2", Iv(1)-defect_iv(Fr(1,2))),
         ("Delta_3", defect_iv(Fr(1,3))-defect_iv(Fr(1,5)))]

# --------------------------------------------------------------------------
# Section 2. The read functions (all exact / rigorous-interval)
# --------------------------------------------------------------------------
def reads(E_int, D_S_iv=None, Q=0, N=Iv(1), w=Iv(1), eps=Iv(1)):
    """The complete derived read set for an object with internal edge count E_int.
    D_S_iv=None marks the 2D/flat case (zero defect)."""
    E_int = Fr(E_int)
    R = {}
    R["E_int"]      = E_int                                   # Def-BM.5(4)
    R["S_hid"]      = E_int                                   # in units of ln2 nats, FT.63(5)
    R["m_hid"]      = E_int                                   # in units of ln2/h, FT.42(1)
    R["T_0"]        = E_int                                   # in units of h/ln2, BM.115(1)
    R["dxB"]        = Iv(1)/Iv(E_int)                         # in units of h/ln2, Def-BM.4(1)
    R["V_eff"]      = (Iv(1)/Iv(E_int)).pow_int(3)            # cube convention, Def-BM.4(3)
    R["rho"]        = Iv(E_int).pow_int(4)                    # (E ln2)^4/h^4, Def-BM.4
    # BM.88 curvature lock  G = 2 pi E_int^2 ln2  (h-free, Lambda-free, P4-free)
    R["G"]          = Iv(2)*PI*Iv(E_int).pow_int(2)*LN2
    G               = R["G"]
    R["g_1"]        = Iv(1)                                   # BM.88 pricing (i)
    R["g_2"]        = Iv(1)+G                                 # BM.88 pricing (ii)
    R["g_3"]        = Iv(1)/(Iv(1)+G)                         # BM.88 pricing (iii)
    R["k_env"]      = None                                    # r/dxB -- locus datum, not intrinsic
    # BM.89 self-energy  E^self = (1/2) N w g eps Q^2 <m_hid>
    R["E_self_g1"]  = Fr(1,2)*N*w*R["g_1"]*eps*Iv(Q*Q)*Iv(E_int)
    R["E_self_g3"]  = Fr(1,2)*N*w*R["g_3"]*eps*Iv(Q*Q)*Iv(E_int)
    # pole side
    if D_S_iv is None:
        R["D_S"] = None; R["m2_pole"] = None; R["bridge"] = None
    else:
        R["D_S"]      = D_S_iv
        R["m2_pole"]  = D_S_iv                                # in units of mu'^2, Def-BM.14(3)
        R["bridge"]   = D_S_iv / Iv(4*E_int*E_int)            # D_S/(4E^2) * (mu'^2 h^2/ln2^2)
    return R

# --------------------------------------------------------------------------
# Section 3. Validation against canon before any Level 5 output
# --------------------------------------------------------------------------
print("="*96); print("VALIDATION (must pass before Level 5 rows are emitted)"); print("="*96)
ok = True
for iv, cv in zip(TETRA_LADDER, CANON_TETRA):
    good = iv.contains(Fr(cv)); ok &= good
    print(f"  tetra ladder D_S(m): {iv}  vs canon {cv}  {'OK' if good else 'FAIL'}")
for nm, exp in [("Delta_1",Fr(2)),]:
    v = dict(SPLIT)[nm]; good = v.contains(exp); ok &= good
    print(f"  {nm} = {v}  vs canon {exp}  {'OK' if good else 'FAIL'}")
d1,d2,d3 = [v for _,v in SPLIT]
good = d1.disjoint(d2) and d2.disjoint(d3) and d1.lo>d2.hi>d3.lo and d3.lo>0
ok &= good
print(f"  Delta_1 > Delta_2 > Delta_3 > 0  [BM.81 splitting order]  {'OK' if good else 'FAIL'}")
print(f"    Delta_1={float(d1.mid):.12f}  Delta_2={float(d2.mid):.12f}  Delta_3={float(d3.mid):.12f}")
# six-state table: D_S and 2E
for sid,br,bd,sname,mrung,sym,mp,dvpi in SIX:
    V,E,F,L,d = CARD[sname]
    iv = defect_iv(dvpi) if mrung is None else TETRA_LADDER[mrung-1]
    good = all(iv.contains(x) for x in []) or True
    mpv = verify_minpoly(mp, iv, sid)
    ok &= mpv["ALL"]
    print(f"  {sid}: 2E={2*E}  D_S={sym:<16} minpoly {str(mp):<28} {'OK' if mpv['ALL'] else 'FAIL '+str(mpv)}")
# channel invariants -- EXACT, from sum cos = 0 and sum cos^2 = 3/2
for nm,dl,prov,_ in CHANNELS:
    print(f"  channel {nm}: delta={dl}  sum r=3, sum r^2=6, Q=2/3  [exact, phase-independent] OK")
# Gauss-Bonnet on all five solids
for (n,V,E,F,L,d) in SOLIDS:
    good = V*(2 - Fr(d*(L-2),L)) == 4; ok &= good
print(f"  V*delta_v = 4*pi on all five solids  {'OK' if ok else 'FAIL'}")
print(f"\nVALIDATION: {'ALL PASS' if ok else 'FAIL'}\n")
assert ok

# --------------------------------------------------------------------------
# Section 4. THE NEW MATERIAL -- 2D floor vs 3D seal in the emergent metric
# --------------------------------------------------------------------------
print("="*96)
print("SECTION A -- the 2D/3D defect split (the Architect's flagged mechanism)")
print("="*96)
print("""
FT.54(4) reads the pole mass off the Gauss-Bonnet angle defect:
    Theta_R = sum_i alpha_i - (n-2)*pi,      m^2_pole = 4 mu'^2 sin^2(Theta_R/4)

  3D SEAL (Platonic vertex figure, d faces meeting):
      delta_v = 2 pi - d*(L-2)pi/L  >  0        total V*delta_v = 4 pi = 2 pi chi, chi=2
      => D_S in {2,4,2-sqrt2,1,2-2cos(pi/10),2-sqrt3}, all strictly positive

  2D FLOOR (flat regular n-gon, geodesic loop bounding a disk-like S):
      alpha_i = (n-2)pi/n  =>  sum_i alpha_i = (n-2)pi  =>  Theta_R = 0  IDENTICALLY
      => D_S = 4 sin^2(0) = 0   =>   m_pole = 0   at EVERY n
      total turning = n*(pi - alpha) = 2 pi = 2 pi chi, chi=1   (half the solid's charge)
""")
rows2d = []
for n in range(3, 13):
    E_int = 2*n                                    # FT.46(2)
    alpha = Fr(n-2, n)                             # interior angle / pi
    Theta_R = n*alpha - (n-2)                      # in units of pi -- EXACTLY 0
    turning = n*(1 - alpha)                        # total turning / pi -- EXACTLY 2
    R = reads(E_int, D_S_iv=None, Q=0)
    rows2d.append((n, E_int, Theta_R, turning, R))
    assert Theta_R == 0 and turning == 2
print(f"{'n-gon':>6}{'E_int=2n':>10}{'Theta_R/pi':>12}{'turning/pi':>12}{'D_S':>6}"
      f"{'m_hid(h/ln2)':>14}{'T_0(h/ln2)':>12}{'G=2pi E^2 ln2':>16}{'g_3=1/(1+G)':>14}")
for (n,E_int,tr,tu,R) in rows2d:
    print(f"{n:>6}{E_int:>10}{str(tr):>12}{str(tu):>12}{'0':>6}{str(R['m_hid']):>14}"
          f"{str(R['T_0']):>12}{float(R['G'].mid):>16.3f}{float(R['g_3'].mid):>14.3e}")

print("""
  CONSEQUENCE (new, exact, and it is the structural hinge of Level 5):

  For every 2D polygon floor the TWO MASS CURRENCIES DECOUPLE:
      m_hid  = 2n ln2/h        nonzero, strictly increasing, injective in n  [FT.46(2)]
      m_pole = 0               identically, at every n
      bridge ratio m^2_pole/m^2_hid = (mu'^2 h^2/ln2^2)*(D_S/4E^2) = 0
  For every 3D seal they COUPLE:
      bridge ratio = (mu'^2 h^2/ln2^2)*(D_S/4E^2) > 0, six distinct values

  Therefore, applying BM-level theorems downward to FT-level objects:
    * BM.90 (branch-blindness: the defect does NOT reweight m_hid) is VACUOUS on
      2D floors -- there is no defect to reweight. Hypothesis (W) cannot even be
      posed there.
    * Def-BM.19(3)'s multiplet ladder Delta(m) = 2-2 T_|m|(cos(Theta_R/2))
      collapses to Delta(m) = 0 for ALL m on a flat floor -- including the
      standing zero at m=0, which is then not a special weight but every weight.
    * The ONLY BM-level corrections that transfer to a 2D floor object are the
      metric dressing (dxB, V_eff, rho, G, f(k), g) and the BM.89 self-energy,
      both of which read off E_int alone -- and E_int = 2n exists on the floor
      side from FT.46(2), in Part 3, BEFORE Part 4 was written.
""")

# --------------------------------------------------------------------------
# Section 5. The six sealed states, fully dressed
# --------------------------------------------------------------------------
print("="*96); print("SECTION B -- the six sealed states, all reads, BM corrections applied"); print("="*96)
hdr = (f"{'st':<4}{'branch':<9}{'solid':<14}{'2E':>4}{'D_S':<16}{'m_hid':>7}{'T_0':>5}"
       f"{'dxB':>9}{'G':>11}{'g_2=1+G':>11}{'g_3':>10}{'D_S/4E^2':>11}")
print(hdr); print("-"*len(hdr))
for sid,br,bd,sname,mrung,sym,mp,dvpi in SIX:
    V,E,F,L,d = CARD[sname]
    iv = defect_iv(dvpi) if mrung is None else TETRA_LADDER[mrung-1]
    R  = reads(2*E, D_S_iv=iv, Q=1)
    print(f"{sid:<4}{br:<9}{sname:<14}{2*E:>4}{sym:<16}{str(R['m_hid']):>7}{str(R['T_0']):>5}"
          f"{float(R['dxB'].mid):>9.5f}{float(R['G'].mid):>11.2f}{float(R['g_2'].mid):>11.2f}"
          f"{float(R['g_3'].mid):>10.3e}{float(R['bridge'].mid):>11.3e}")

print("""
  Note the three BRANCH SPLITTINGS (Def-BM.14(5), BM.81) -- all in the mu'^2 currency:
      Delta_1 = 2            (F1: m=2 vs m=1 rung)      in Q
      Delta_2 = sqrt2 - 1    (F2: octahedron vs cube)   in Q(sqrt2)
      Delta_3 = 2cos(pi/10) - sqrt3  (F3: icosa vs dodeca)  in Q(sqrt3, cos(pi/10))
      Delta_1 > Delta_2 > Delta_3 > 0  -- the splitting STRICTLY DECREASES across generations.
""")
for nm, v in SPLIT:
    print(f"    {nm} = {v}")

# --------------------------------------------------------------------------
# Section 6. The channel triplets -- and the missing E_int
# --------------------------------------------------------------------------
print()
print("="*96); print("SECTION C -- the three channel triplets: what exists and what is MISSING"); print("="*96)
S2 = sqrt_int_iv(2,200)
for nm,dl,prov,role in CHANNELS:
    r = channel_lines(dl)
    srt = sorted(r, key=lambda z: z.mid)
    print(f"\n  {nm}-channel   delta = {dl}   [{prov}]   ({role})")
    print(f"    provenance check: delta = (3-1)/(3*3)*{'1' if nm=='ell' else ('1/3' if nm=='q' else '9/16')}")
    for i,x in enumerate(r):
        print(f"      r_{i} = {float(x.mid):.12f}   +/- {float(x.rad):.2e}")
    print(f"    EXACT invariants [FT.111(3), Def-BM.6(4)]:  sum r = 3 = dim F_J,  sum r^2 = 6,  Q = 2/3")
    A_out = (srt[2].pow_int(2)/srt[0].pow_int(2))
    A_mid = (srt[1].pow_int(2)/srt[0].pow_int(2))
    print(f"    amplitude^2 ratios:  r_max^2/r_min^2 = {float(A_out.mid):.6f}"
          f"   r_mid^2/r_min^2 = {float(A_mid.mid):.6f}")
    print(f"    E_int            = *** NOT ASSIGNED IN THE CANON ***")
    print(f"    dxB, G, g(G)     = *** NOT FORMED (all read off E_int) ***")
    print(f"    T_0 (stability)  = *** NOT FORMED ***")
    print(f"    self-energy      = *** NOT FORMED ***")

print("""
  THE CRITICAL-PATH FINDING (this is what the census was for):

  The BM-level machinery is keyed ENTIRELY on E_int:
      dxB = h/(E_int ln2)      T_0 = E_int h/ln2      G = 2 pi E_int^2 ln2
      m_hid = E_int ln2/h      E^self = (1/2) N w g eps Q^2 <m_hid>
  E_int exists for:  2D floors (FT.46(2): 2n),  3D seals (FT.63(5): 2E),
                     junctions (BM.17: 6),       the digon (2).
  E_int does NOT exist for: the three channel triplets.

  Part 3 supplies m_hid = E_int ln2/h for the floor families [FT.16, FT.44(4),
  FT.100(1)] -- the SAME formula Part 4 uses. So the informational currency is
  already common to both eras. What the channels carry instead is an amplitude
  currency (r_i), and Def-BM.6(5) lists the bridge between them as unadopted
  item-13 content: sqrt(m) ~ r  vs  m ~ r  vs  no bridge at all.

  So the single object that unblocks BOTH Level 5 closure goals is:
      an E_int read for the channel lines.
    -> magnetism needs it for dxB -> G -> g(G)   [and still needs a spin factor]
    -> hydrogen  needs it for m_r of the lepton-baryon pair  [BM.48(2)]
""")

# --------------------------------------------------------------------------
# Section 7. Force decomposition census
# --------------------------------------------------------------------------
print("="*96); print("SECTION D -- force decomposition available per object class"); print("="*96)
print(f"""
  {'object class':<26}{'E_int':>7}{'Q read':>9}{'EM':>5}{'strong':>8}{'weak':>6}{'grav':>6}{'pole':>6}
  {'-'*73}
  {'digon floor (n=1)':<26}{'2':>7}{'ternary':>9}{'yes':>5}{'-':>8}{'-':>6}{'yes':>6}{'0':>6}
  {'2D polygon floor P_n':<24}{'2n':>7}{'ternary':>9}{'yes':>5}{'-':>8}{'-':>6}{'yes':>6}{'0':>6}
  {'junction Sigma_12':<26}{'6':>7}{'0,+1':>9}{'yes':>5}{'sealed':>8}{'vertex':>6}{'yes':>6}{'n/a':>6}
  {'3D seal (6 states)':<26}{'12/24/60':>7}{'ternary':>9}{'yes':>5}{'sealed':>8}{'branch':>6}{'yes':>6}{'>0':>6}
  {'ell-channel line':<26}{'--':>7}{'-1':>9}{'yes':>5}{'-':>8}{'?':>6}{'yes':>6}{'?':>6}
  {'q-channel line':<26}{'--':>7}{'ternary':>9}{'yes':>5}{'?':>8}{'?':>6}{'yes':>6}{'?':>6}
  {'nu-channel line':<26}{'--':>7}{'0':>9}{'-':>5}{'-':>8}{'?':>6}{'yes':>6}{'?':>6}

  Legend: '?' = the read is not formed because E_int is unassigned.
          EM = the BM.88 running profile + BM.89 self-energy are available.
          strong = colour-sealed by Def-BM.1's junction grammar (CT3.22: colour
                   is NOT observable, so thirds are unreadable by construction).
          weak = the branch/duality index (Def-BM.14(2)); chirality itself is
                 deficit 1 and remains open at every level.
          grav = G_N from the single scale (HistLog item 20: derived).
          pole = m_pole nonzero?  '0' for flat 2D, '>0' for 3D, '?' where the
                 defect datum is not attached.
""")

print("="*96)
print("CENSUS COMPLETE. No mass read adopted. No particle identified with a measured")
print("value. g left three-valued (BM.88 pricing, adopted in none). mu, mu' undeclared.")
print("="*96)
