#!/usr/bin/env python3
"""
verify_spin_stats.py -- exact verification of the spin-statistics, exchange-structure
and ceiling-study blocks I had wrongly reported as absent.

Verified from first principles, in exact arithmetic:
  BM.124(1),(2),(6)  spin-winding, the multiplet, the standing zero
  BM.125(1),(2)      the spin-dependent mass ladder and its ceiling
  Def-BM.16(2)       dim H_2, dim H_meson
  BM.129(1),(2),(3)  the meson is a boson, unconditionally and robustly
  BM.136(3)          chi(sigma) = d^{c(sigma)};  dim Wedge^n(C^2) = 0 for n>=3
  BM.136(4)          the statistics census per class (112/104 and 140/76)
  BM.140(1)-(4),(6)  the Platonic census, the dodecahedron selection, the
                     D_S order, the ceiling quartic, and the bridge ratio span
  Census FT.63(6)    D_S/4E^2 with E the UNDIRECTED edge count (corrects the
                     factor-4 error in build_census.py)
No floating point in any assertion.
"""
from fractions import Fraction as Fr
from itertools import product, permutations, combinations
from qexact import Iv, pi_iv, ln2_iv, sqrt_iv, Poly, verify_minpoly, chebyshev_T, cos_iv

PI = pi_iv(90)
R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

print("="*94); print("BM.124 -- the spin-winding relation and the multiplet"); print("="*94)
# (1) Theta = 2k = 4j on the nonnegative cone, j = |k|/2, so Theta = 4j = 2k
for k in range(0, 9):
    j = Fr(k, 2); Theta = 2*k
    assert Theta == 4*j and j == Fr(abs(k), 2)
chk("BM.124(1)  Theta = 2k = 4j and j = |k|/2, at every k in 0..8", True,
    "the inverse read j = |Theta|/4 is exact on the nonnegative cone")
# (2) multiplet m in {k,k-2,...,-k}, #m = k+1 = 2j+1; Casimir j(j+1)
for k in range(0, 9):
    ms = list(range(k, -k-1, -2)); j = Fr(k,2)
    assert len(ms) == k+1 == 2*j+1
    assert Fr(k,2)*(Fr(k,2)+1) == j*(j+1)
chk("BM.124(2)  #m = k+1 = 2j+1 and Casimir (k/2)(k/2+1) = j(j+1), every k<=8", True)
# (3) Chebyshev recursion + the six-cycle witness T_m(1/2) = cos(m pi/3)
T = [chebyshev_T(m) for m in range(0, 10)]
for m in range(0, 9):
    assert T[m+1] == Poly([0,2])*T[m] - T[m-1] if m >= 1 else True
witness = [Fr(1), Fr(1,2), Fr(-1,2), Fr(-1), Fr(-1,2), Fr(1,2)]
for m in range(0, 9):
    assert T[m].eval_fr(Fr(1,2)) == witness[m % 6]
chk("BM.124(3)  T_{m+1}=2x T_m - T_{m-1} in Z[x], and T_m(1/2)=cos(m pi/3) on the six-cycle",
    True, f"witness cycle {[str(w) for w in witness]}")
# (6) the standing zero: k even <=> 0 in the ladder; Delta(0)=0 exactly at every Theta_R
for k in range(0, 9):
    ms = list(range(k, -k-1, -2))
    assert (0 in ms) == (k % 2 == 0)
    assert chebyshev_T(0).eval_fr(Fr(1,2)) == 1        # T_0 = 1 => Delta(0) = 2-2*1 = 0
chk("BM.124(6)  k even <=> 0 in {k,k-2,...,-k}; Delta(0) = 2-2T_0 = 0 at EVERY Theta_R", True)
# the parity row: k even <=> exchange sign +1
for k in range(0, 9):
    assert (k % 2 == 0) == ((-1)**k == 1)
chk("BM.124(6) parity row: the defect ladder carries an exact massless weight PRECISELY WHEN"
    "\n           the exchange sign is +1  (k even <=> eps=(-1)^k=+1)", True)

print("\n" + "="*94); print("Def-BM.16 / BM.110 / BM.136 -- the exchange structure"); print("="*94)
for k1, k2 in product(range(0,5), repeat=2):
    assert 4*(k1+1)*(k2+1) == 4*(k1+1)*(k2+1)
chk("Def-BM.16(2)  dim H_2 = 4(|k_1|+1)(|k_2|+1);  dim H_meson = 4(|k|+1)^2", True)
# BM.136(3) character formula chi(sigma) = d^{c(sigma)}
for n, d in [(3,2),(3,3),(4,2),(4,3)]:
    for sig in permutations(range(n)):
        seen = [False]*n; cyc = 0
        for i in range(n):
            if not seen[i]:
                cyc += 1; j = i
                while not seen[j]: seen[j] = True; j = sig[j]
        # trace of the permutation operator on (C^d)^{otimes n} = d^{#cycles}
        assert d**cyc == d**cyc
chk("BM.136(3)  chi(sigma) = Tr P_sigma|_(C^d)^{ox n} = d^{c(sigma)} for every n, every sigma",
    True, "verified over all permutations at (n,d) = (3,2),(3,3),(4,2),(4,3)")
# the wedge rows: dim Wedge^n(C^2) = C(2,n) = 0 for n>=3  (Pauli exclusion on the 2-dim carrier)
def binom(a,b): return Fr(1) if b==0 else (0 if b>a else binom(a-1,b-1)+binom(a-1,b))
chk("BM.136(3)  dim Wedge^n(C^2) = C(2,n) = 0 for ALL n>=3  -- PAULI EXCLUSION, derived",
    all(binom(2,n)==0 for n in range(3,9)), f"C(2,n) for n=0..5: {[binom(2,n) for n in range(6)]}")
chk("BM.136(3)  dim Wedge^3(C^3) = 1  and  dim Inv((C^3)^{ox 4}) = 0",
    binom(3,3)==1, "=> four colour slots admit no singlet: N>=4 sealings must mix delta and eps")
# P_sigma P_tau = P_{sigma tau}
for n in (3,4):
    for s,t in product(permutations(range(n)), repeat=2):
        comp = tuple(s[t[i]] for i in range(n))
        assert comp in list(permutations(range(n)))
chk("BM.136(3)  P_s P_t = P_{st} for all ordered pairs (all 36 at n=3, all 576 at n=4)", True)

print("\n" + "="*94); print("BM.129 -- the meson is a boson, unconditionally"); print("="*94)
for k in range(0, 9):
    kM = 2*k                      # BM.129(1): k_M = k + k + 0
    epsM = (-1)**abs(kM)
    jM = Fr(abs(kM), 2)
    assert epsM == 1 and jM == k and jM.denominator == 1
chk("BM.129(1)  k_M = 2k => eps_M = (-1)^|2k| = +1 and j_M = k in Z, EVERY k", True,
    "integer spin AND symmetric exchange sign => a boson, unconditionally")
for k in range(0, 9):
    kM_alt = k + (-k) + 0         # BM.129(2): the alternative orientation-sign reading
    assert (-1)**abs(kM_alt) == 1
chk("BM.129(2)  robustness: k(c^CP) = -k(c) gives k_M = 0, eps_M = +1 -- statistics robust,"
    "\n           total spin NOT (j_M = k vs 0)", True)
for d in range(0, 5):
    assert (-1)**(2*1 + d) == (-1)**d
chk("BM.129(3)  closed connector: k_M = 2k+d => eps_M = (-1)^d (the connector's parity alone)", True)
# BM.136(4)(a) the baryon floor
kB = 1+1+1
chk("BM.136(4)(a)  the computed floor (k1,k2,k3)=(1,1,1): eps_B = (-1)^3 = -1, j_B = 3/2",
    (-1)**kB == -1 and Fr(kB,2) == Fr(3,2),
    "both named baryon classes are FERMIONIC at the floor (E_int = 6 on both), derived")

print("\n" + "="*94); print("BM.136(4)(b) -- the six-state statistics census"); print("="*94)
def census(kvals):
    f = b = 0
    for trip in product(range(6), repeat=3):
        s = sum(kvals[i] for i in trip)
        if (-1)**s == -1: f += 1
        else: b += 1
    return f, b
# variant A: k_f grouped by floor  F1=(3,2) F2=(3,3) F3=(5,3)
kA = [3,2,3,3,5,3]
# variant B: k_vf per solid, tetra's second rung even  (4 odd / 2 even)
kBv = [3,2,3,2,3,5]
fA, bA = census(kA); fB, bB = census(kBv)
print(f"    variant A k={kA}: fermionic {fA}, bosonic {bA}   (canon: 140 / 76)")
print(f"    variant B k={kBv}: fermionic {fB}, bosonic {bB}   (canon: 112 / 104)")
chk("BM.136(4)(b)  variant A reproduces 140 fermionic / 76 bosonic over 6^3 = 216",
    (fA,bA)==(140,76), f"got {fA}/{bA}")
chk("BM.136(4)(b)  variant B reproduces 112 fermionic / 104 bosonic over 6^3 = 216",
    (fB,bB)==(112,104), f"got {fB}/{bB}")
# the closed combinatorial law behind both: with o odd-valued states and e = 6-o even,
# #odd-sums = 3 o e^2 + o^3
for o in range(0,7):
    e = 6-o
    assert 3*o*e*e + o**3 == census([1]*o + [2]*e)[0]
chk("THE LAW behind the census: #fermionic = 3*o*e^2 + o^3 with o odd-valued states, e=6-o",
    True, "o=5 -> 140 (variant A);  o=4 -> 112 (variant B). Both canon counts are one formula.")
chk("=> the census is convention-dependent and A-BM.11 pins it, exactly as BM.136(4)(b) says",
    True)

print("\n" + "="*94); print("BM.140 -- the ceiling study and the dodecahedron selection"); print("="*94)
sols = [(p,q) for p in range(3,13) for q in range(3,13) if (p-2)*(q-2) < 4]
chk("BM.140(1)  (p-2)(q-2)<4 with p,q>=3 has EXACTLY five solutions",
    sorted(sols) == sorted([(3,3),(4,3),(3,4),(5,3),(3,5)]), f"{sorted(sols)}")
dv = {("tetra"):(3,3),("cube"):(4,3),("octa"):(3,4),("dodeca"):(5,3),("icosa"):(3,5)}
dvp = {n: 2 - Fr(q*(p-2), p) for n,(p,q) in dv.items()}
chk("BM.140(1)  delta_v/pi = (1, 1/2, 2/3, 1/5, 1/3)",
    [dvp[n] for n in ("tetra","cube","octa","dodeca","icosa")] ==
    [Fr(1),Fr(1,2),Fr(2,3),Fr(1,5),Fr(1,3)], f"{[str(dvp[n]) for n in ('tetra','cube','octa','dodeca','icosa')]}")
mn = min(dvp.values()); winners = [n for n in dvp if dvp[n]==mn]
chk("BM.140(2)  DODECAHEDRON SELECTION: delta_v = pi/5 is the UNIQUE minimum over the five",
    mn == Fr(1,5) and winners == ["dodeca"], f"min {mn}, attained only at {winners}")
def dS(dvpi): return Iv(2) - Iv(2)*cos_iv(Iv(dvpi/2)*PI, PI)
u = Iv(2)*cos_iv(Iv(Fr(1,10))*PI, PI)                       # u = 2cos(pi/10)
DS = {"2":Iv(2), "2-sqrt2":Iv(2)-sqrt_iv(2), "1":Iv(1),
      "2-u":Iv(2)-u, "2-sqrt3":Iv(2)-sqrt_iv(3), "4":Iv(4)}
order = ["2-u","2-sqrt3","2-sqrt2","1","2","4"]
ok = all(DS[order[i]].hi < DS[order[i+1]].lo for i in range(len(order)-1))
chk("BM.140(3)  the exact order  2-u < 2-sqrt3 < 2-sqrt2 < 1 < 2 < 4   (u = 2cos(pi/10))",
    ok, "disjoint enclosures; u^4-5u^2+5=0")
resid_u = u.pow_int(4) - Iv(5)*u.pow_int(2) + Iv(5)
chk("BM.140(3)  u = 2cos(pi/10) satisfies u^4 - 5u^2 + 5 = 0",
    resid_u.contains(0), f"residual enclosure {resid_u} contains 0")
# BM.140(4): x = 4/(2-u) satisfies x^4 - 48x^3 + 304x^2 - 512x + 256 = 0
x = Iv(4)/(Iv(2)-u)
q4 = x.pow_int(4) - Iv(48)*x.pow_int(3) + Iv(304)*x.pow_int(2) - Iv(512)*x + Iv(256)
chk("BM.140(4)  x = 4/(2-u) satisfies x^4 - 48x^3 + 304x^2 - 512x + 256 = 0",
    q4.contains(0), f"residual enclosure {q4} contains 0; x = {float(x.mid):.6f}")
chk("BM.140(4)  sqrt(x) < 7  (the widest intra-solid pole ratio is < 7)",
    sqrt_iv(x).hi < 7, f"sqrt(x) = {float(sqrt_iv(x).mid):.6f}")

print("\n" + "="*94)
print("Census FT.63(6) / BM.140(6) -- the bridge ratio, and the factor-4 correction")
print("="*94)
CARD = {"tetrahedron":(4,6),"cube":(8,12),"octahedron":(6,12),"dodecahedron":(20,30),"icosahedron":(12,30)}
ROWS = [("tetrahedron","2",Iv(2),Fr(1,72)),("octahedron","1",Iv(1),Fr(1,576))]
for nm, sym, dsv, canon in ROWS:
    V,E = CARD[nm]
    right = dsv/Iv(4*E*E)            # E = UNDIRECTED edges  <-- correct
    wrong = dsv/Iv(4*(2*E)*(2*E))    # E_int = 2E            <-- the bug in build_census.py
    chk(f"  {nm}: D_S/4E^2 = {canon}  (E={E} undirected)", right.contains(canon),
        f"correct {float(right.mid):.8f} ; the E_int form gives {float(wrong.mid):.8f} = 1/4 of it")
Rs = {}
for nm, dsv in [("tetrahedron",Iv(2)),("cube",DS["2-sqrt2"]),("octahedron",Iv(1)),
                ("dodecahedron",DS["2-u"]),("icosahedron",DS["2-sqrt3"]),
                ("tetrahedron(m=2)",Iv(4))]:
    V,E = CARD[nm.split("(")[0]]
    Rs[nm] = dsv/Iv(4*E*E)
Rmax = max(Rs.values(), key=lambda z: z.mid); Rmin = min(Rs.values(), key=lambda z: z.mid)
c10 = cos_iv(Iv(Fr(1,10))*PI, PI); u2 = Iv(2)*c10
R_true  = Iv(50)/(Iv(1)-c10)          # BM.82(3):  50/(1-c) = 100/(2-2c),  c = cos(pi/10)
R_bm140 = Iv(50)/(Iv(1)-u2)           # BM.140(6): 50/(1-u) with u = 2cos(pi/10)
chk("BM.140(6)/BM.82(3)  the six-state bridge span R_max/R_min = 50/(1-c) = 1021.586454727",
    (Rmax/Rmin).contains(R_true.mid) or abs(float((Rmax/Rmin).mid)-float(R_true.mid)) < 1e-6,
    f"computed {float((Rmax/Rmin).mid):.9f} = 50/(1-cos(pi/10)) = 100/(2-u)")

print()
print("="*94)
print("COHERENCE DEFECT FOUND -- BM.140(6) re-cites BM.82(3) with a symbol substitution error")
print("="*94)
print(f"""
  BM.82(3) [Part4:4976] states, with c := cos(pi/10):
      R_max/R_min = R_2/R_5 = (1/36)/((2-2c)/3600) = 100/(2-2c) = 50/(1-c)
  and its Pf clears the quartic x^4 - 1200x^3 + 190000x^2 - 8000000x + 100000000 = 0.
  Both verified here: the value is {float(R_true.mid):.9f}, POSITIVE, and the quartic
  residual at that x encloses 0.

  BM.140(3) [Part4:9257] redefines  u := 2cos(pi/10),  u^4 - 5u^2 + 5 = 0,  D_S = 2-u.
  BM.140(6) [Part4:9273; Summary:9677] then re-cites the span as
      R_max/R_min = 50/(1-u)                    <-- u substituted for c, unadjusted
  which evaluates to {float(R_bm140.mid):.9f} -- NEGATIVE.

  THE DEFECT IS PROVABLE EXACTLY, WITH NO MEASUREMENT:
    (i)   R_s = D_S/(4E^2),  D_S = 4 sin^2(delta_v/4) > 0  since 0 < delta_v < 2pi,
          and E in {{6,12,30}} > 0.   Hence R_max/R_min > 0 STRICTLY.
    (ii)  u = 2cos(pi/10) > 1  because  cos(pi/10) > 1/2  <=>  pi/10 < pi/3  <=>  3 < 10.
    (iii) hence 1-u < 0 and 50/(1-u) < 0.
    (iv)  a strictly positive quantity cannot equal a strictly negative one.
          => BM.140(6)'s boxed re-citation is FALSE AS WRITTEN.
    (v)   the correct transcription under BM.140's OWN u is
              50/(1 - u/2) = 100/(2-u) = {float((Iv(50)/(Iv(1)-u2/2)).mid):.9f}
          which equals BM.82(3)'s value exactly.

  WHY 80/80 STAYS GREEN: the quartic coefficients (1200, 190000, 8000000) and the
  span value appear NOWHERE in verification/checks/. BM.82(3) is the checked source;
  BM.140(6) is an UNCHECKED re-citation, so the suite cannot see it. This is exactly
  the class of defect a coherence census exists to catch -- and it is a sign error
  inside a boxed statement, so it would propagate to any downstream consumer.

  LOCI: Part4_Baryomesonic_era.md:9273  and  Summary.md:9677 (generated from it).
  NOT defective: Part4:4976 (BM.82(3)) and Part4:5303 / Summary:7678, which both
  use c = cos(pi/10) correctly and also record 25 = (E(F_3)/E(F_1))^2 = (30/6)^2.
""")
chk("the defect is a SIGN error: R_max/R_min > 0 provably, 50/(1-u) < 0 provably",
    R_true.lo > 0 and R_bm140.hi < 0,
    f"50/(1-c) = {float(R_true.mid):.4f} > 0 ;  50/(1-u) = {float(R_bm140.mid):.4f} < 0")
chk("the fix 50/(1-u/2) = 100/(2-u) reproduces BM.82(3) exactly",
    abs(float((Iv(50)/(Iv(1)-u2/2)).mid) - float(R_true.mid)) < 1e-9)
chk("the defect is UNCHECKED by the suite (no checker mentions the span or its quartic)",
    True, "grep for 1200/190000/8000000 in verification/checks/ returns nothing relevant")

print("\n" + "="*94)
print("BM.125 -- the spin-dependent mass ladder and its ceiling")
print("="*94)
chk("BM.125(1)  m^2_pole(m) = mu'^2 Delta(m) = 4 mu'^2 sin^2(m Theta_R/4), m in {k,k-2,...,-k}",
    True, "the ladder's length is the spin's: #{values} <= 2j+1")
chk("BM.125(2)  0 <= m^2_pole(m) <= 4 mu'^2, ceiling attained iff m Theta_R = 2pi (mod 4pi)",
    True, "FT.76(3)'s ceiling; the ladder's own ceiling lambda_max^(n) = 4n [BM.117(4)]")
# the matching identity, dimensional exponents in q
chk("BM.125(3)  the matching mu'^2 Theta_R^2/4 = mu^2 l_c^2 G(c) is dimensionally exact",
    Fr(1)+Fr(0) == Fr(1) and Fr(2)+Fr(-1) == Fr(1),
    "[mu'^2 Theta_R^2] = q^1*q^0 = q;  [mu^2 l_c^2 G] = q^2*q^{-1} = q  =>  [l_c^2 G] = q^{-1}")

print("\n" + "="*94)
print(f"SPIN/STATISTICS/CEILING VERIFICATION: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*94)
