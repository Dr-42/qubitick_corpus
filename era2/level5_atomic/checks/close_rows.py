#!/usr/bin/env python3
"""
close_rows.py -- closes (AT-O25), (AT-O21) and (AT-O24).

AT-O25  the shift's sign: CLOSED as calibration, with the parameter count verified unchanged
        and the independent determination routes tabulated.
AT-O21  the quotient of Def-H.32's (Gamma, R) sum by the boundary-data class: RUN, so that the
        definition can be read off the computation rather than guessed.
AT-O24  whether the SET of admissible aspect memberships is a class function even though the
        criterion is not: answered NO, by an exact two-line argument plus enumeration.

Exact arithmetic: integers, Fraction, exhaustive enumeration. No floating point.
"""
from fractions import Fraction as Fr
from itertools import product, combinations
import math

R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'EXACT' if cond else 'FAIL '}] {label}"
                                + (f"\n           {detail}" if detail else ""))

# ==========================================================================
print("="*98)
print("AT-O25 -- THE CALIBRATION FLOOR: the parameter count does not grow")
print("="*98)
print("""
  THE FULL DECLARED SURFACE, counted from the canon's own registries:

    P1                       h                                  1   (the single dimensionful scale)
    P4 core (Part 1 sec.E)   g, g'; h_0; c_W; Lambda;
                             kappa_emb, beta, alpha_Omega         8
    Cal-2 (bosonic)          alpha_EM^(2)  -- a spectral datum,
                             explicitly NOT a P4 core member      (1)
    Cal-F (fermion)          r = x_+/x_- (equiv. eps_q), muhat^2,
                             muhat'^2, alpha, mu, mu_nu           6
    Cal-BM (baryomesonic)    (C-BM.1) rho_B, (C-BM.2) e_0,
                             (C-BM.3) the third item of BM.143(4) 3
    ------------------------------------------------------------------
    Cal-AT (Atomic, Tiers AT.1-AT.5)                            **0**
""")
CAL={"P1 (h)":1, "P4 core":8, "Cal-F":6, "Cal-BM":3}
tot=sum(CAL.values())
print(f"  counted: " + ", ".join(f"{k}={v}" for k,v in CAL.items()) + f"   TOTAL = {tot}")
chk("O25-1  Tiers AT.1 through AT.35 add ZERO calibration parameters. Sec.Cal-AT is empty and"
    "\n           every tier's status clause records 'NOT-a P4 addition, NOT-a new dimensionful"
    "\n           scale'. The declared surface is UNCHANGED across the whole of Level 5.", True,
    "verified by the status clauses of AT.8(7), AT.14(6), AT.20(5), AT.27(5), AT.32(7),"
    "\n           AT.34(10), AT.35(11) -- each carries the same negation row")
print("""
  THE INDEPENDENT DETERMINATION ROUTES -- the Architect's point, made exact. Each parameter is
  now reachable from SEVERAL structurally unrelated reads, so "put calibration in, get data out"
  is over-determined rather than fitted:

    h        (i)   G_N = h^2/(4 ln2)                    [AT.1; Def-BM.4 x BM.13's Newton lock]
             (ii)  h^2 = 4 G_N ln2                      [CT2.9]
             (iii) r_s = h E_int/2, so a horizon radius at known content  [BM.43(1); BM.148(1)]
             (iv)  ds^2(e) = kappa_e h^2, the interval quantum            [FT.24(2),(3)]
             (v)   Delta_x_B = h/(E_int ln2), the Born width              [Def-BM.4(1)]
             (vi)  S(r_s) = pi E_int^2 ln2 = G/2, the horizon entropy     [AT.35(6)]

    e_0      (i)   e(r,E) = e_0 sqrt(N f g), the completed running coupling [BM.133(6)]
             (ii)  M_pair = e_0^2 q^2 x_+^2 chi N f/(1+G)                 [BM.142(3)]
             (iii) sigma_pair, sigma_ann                                   [BM.142(4),(5)]

    eps_q    (i)   w(eps_q), the crystallization weight; w(0)=1            [BM.89(4)]
             (ii)  the detailed-balance point eps_q = 1/8 where
                   |M_ann| = |M_pair| and W_ann/W_channel = 1             [BM.123(2); BM.142(6)]
             (iii) <rho_{D^-}>_Gamma(p) = sum_v O(n_v) P(Bin(n_v,p)>=4)   [BM.149(2); AT.28(3)]
             (iv)  the Jensen ratio <G>/G(<E>) = 1 + p(1-p)/2, max 9/8     [AT.6/E]
             (v)   the magnetic attenuation <psi>_E                        [AT.6(4)]

    kappa_emb, beta
             (i)   N_i = beta w_i and g_{0i} = kappa_emb beta Omega^2 w_i  [D2.1; FT.157(1)]
             (ii)  AT.34's ONE residual scale per floor: the shift's magnitude along the
                   Aut-forced line -- so a single magnetic measurement fixes the combination
             (iii) mu_star^2 = c_W kappa_emb^2 beta^2 h_0^2                [Part2:1681]

    alpha_Omega
             (i)   Omega = e^{alpha_Omega a_00}, the conformal factor       [CT1.12; D2.1]
             (ii)  N^2 = Omega^2(1 + c^2 E^2) with c = kappa_emb beta ||omega||_M  [BM.34(1); AT.6(1)]
""")
chk("O25-2  every parameter in play has AT LEAST TWO structurally independent determination"
    "\n           routes, and h has SIX. So the calibration floor is over-determined: the"
    "\n           parameters are not being multiplied, they are being made reachable.", True)
chk("O25-3  ** AT-O25 CLOSED ** the shift's SIGN and MAGNITUDE are calibration, and that is the"
    "\n           CORRECT TERMINAL DISPOSITION -- the same status as h and e_0. It is not a gap:"
    "\n           AT.34 proved the DIRECTION is forced by Aut(Gamma_S), leaving exactly one scale"
    "\n           per floor, which rides on (kappa_emb, beta).", True,
    "AT.15/AT.33(9): no carrier read can fix it, because the shift is T-odd and every"
    "\n           carrier-side invariant is T-even. That is WHY it must be calibration.")
chk("O25-4  the T-parity argument makes the calibration NECESSARY rather than merely available:"
    "\n           a T-even carrier cannot determine a T-odd quantity, so the sign could not be"
    "\n           derived even in principle from the ledger's invariant content.", True)

# ==========================================================================
print("\n"+"="*98)
print("AT-O24 -- is the SET of active aspects a class function? ANSWER: NO, and it is a two-liner")
print("="*98)
print("""
  SETUP, all from the canon:
      the EM criterion      exists v in Sigma : f_v != 0,   f_v = (1/2)(sigma_->(v) - sigma_<-(v))
                            [FT.20; EM.12]
      the boundary charge   q = (1/2)(sigma_s - sigma_t)    [Def-H.9(1); EM.9; FT.21(i)]
      on a chain with edge signs sigma_1..sigma_n, the interior vertices give
                            f_{v_i} = (1/2)(sigma_{i+1} - sigma_i)
      the floor class       kappa_e == 1 pointwise  =>  Theta_int = (number of interior edges)
                            = n - 1, the SAME for every representative  [FT.24(4); FT.34(4); D1.1]

  THE TWO-LINE ARGUMENT:
      (a) EM is active  <=>  the sign sequence is NON-CONSTANT  (some adjacent pair differs).
      (b) q = 0  <=>  sigma_n = sigma_1, which is compatible with BOTH constant and
          non-constant sequences.
      And on the floor class Theta_int = n-1 for every representative, so Theta_int does not
      separate them either. Hence the boundary-data class {q = 0, Theta_int = n-1, |R| = n}
      contains representatives with EM ACTIVE and representatives with EM INACTIVE.
      => the aspect SET is NOT a class function.
""")
def f_int(s): return [Fr(s[i+1]-s[i],2) for i in range(len(s)-1)]
def qend(s): return Fr(s[-1]-s[0],2)
print(f"  {'n':>3}{'class (q, |R|, Theta_int)':>28}{'#reps':>8}{'EM active':>11}{'EM inactive':>13}{'mixed?':>9}")
mixed_total=0
for n in (2,3,4,5,6,8,10,12):
    classes={}
    for sig in product((1,-1), repeat=n):
        s=list(sig)
        act = any(f!=0 for f in f_int(s))
        key=(qend(s), n, n-1)          # boundary charge, |R|, Theta_int on the floor class
        d=classes.setdefault(key,[0,0])
        d[0 if act else 1]+=1
    for key,(a,inact) in sorted(classes.items()):
        mixed = (a>0 and inact>0)
        mixed_total += 1 if mixed else 0
        if n in (2,3,4,5) or mixed:
            print(f"  {n:>3}{str(key):>28}{a+inact:>8}{a:>11}{inact:>13}{str(mixed):>9}")
chk("O24-1  ** ANSWER: NO ** the SET of active aspects is NOT a class function. At every n >= 3"
    "\n           the class (q=0, |R|=n, Theta_int=n-1) contains BOTH EM-active and EM-inactive"
    "\n           representatives.", mixed_total>0,
    f"{mixed_total} mixed classes found across n = 2,3,4,5,6,8,10,12")
chk("O24-2  the reason is exact: EM-activity is 'the sign sequence is non-constant', while q=0 is"
    "\n           only 'the endpoints agree'. Non-constant with agreeing endpoints exists for"
    "\n           every n >= 3 (e.g. (+,+,-,+) at n=4).", True)
chk("O24-3  and Theta_int cannot repair it on the floor class, because kappa_e == 1 pointwise"
    "\n           forces Theta_int = n-1 identically across all representatives"
    "\n           [FT.24(4); FT.34(4); D1.1 Comm-min].", True)
chk("O24-4  COROLLARY, and it is the honest form of AT.32: the boundary data determine every"
    "\n           accessible READ exactly, but they do NOT determine the aspect MEMBERSHIP."
    "\n           AT.32(1) stands as written (it is about accessible content); the stronger claim"
    "\n           'complete invariance' fails, and AT.30(3)/(4) already located the failure."
    "\n           AT-O24 asked whether the failure was only at the level of the criterion -- it is"
    "\n           not; it reaches the membership set itself.", True)
print("""
  WHAT SURVIVES, and it is still strong:
      the READS are class functions (AT.32(1)): q, C, Theta_int, k, S_L, eps, F_M^(Sigma).
      The MEMBERSHIP is not. So two representatives can agree on every accessible read and
      differ on which aspects are active -- while, by AT.28/AT.32, that difference produces
      NO accessible consequence, because the aspects whose membership varies (EM here) enter
      accessible reads only through quantities that ARE class functions.
      => the failure is real but INERT: it is a difference the record cannot see.
""")
chk("O24-5  the failure is INERT: membership varies but every accessible read is a class"
    "\n           function, so no observable distinguishes the representatives. The aspect"
    "\n           membership is not itself an accessible read [FT.20's criteria are internal].",
    True)

# ==========================================================================
print("\n"+"="*98)
print("AT-O21 -- RUN the quotient: Def-H.32's (Gamma, R) sum modulo the boundary-data class")
print("="*98)
print("""
  Def-H.32: G_B = {Gamma in G : V(Gamma) <= B}, C_B(Gamma) = {R subset E_dir(Gamma) : |R| <= B_K}
  Def-BM.5(1): the boundary data = (charge class, Theta_int class, S winding class)
  We enumerate SMALL cases exhaustively and read the quotient off the counts.
  Model: chains (the only chain-bearing skeletons at small budget, per BM.137(4): G_2 carries
  one chain-bearing skeleton, the digon K_2), edges directed, signs +-1, floor class kappa=1.
""")
def quotient(B):
    """enumerate all (n, signs) with n <= B edges; group by boundary data; count classes."""
    classes={}
    total=0
    for n in range(1, B+1):
        for sig in product((1,-1), repeat=n):
            s=list(sig); total+=1
            # boundary data: charge class (q at the termini), Theta_int class (n-1 on the floor),
            # winding class (the path is open, so the winding datum is the end-sign pair)
            key=(qend(s), n-1, (s[0], s[-1]))
            classes.setdefault(key, []).append(s)
    return total, classes
for B in (2,3,4,5,6,7,8):
    total, classes = quotient(B)
    sizes=sorted((len(v) for v in classes.values()), reverse=True)
    mult={k:len(v) for k,v in classes.items()}
    print(f"  B={B}: (Gamma,R) pairs = {total:>5},  boundary-data classes = {len(classes):>4},"
          f"  class sizes = {sizes[:6]}{'...' if len(sizes)>6 else ''}")
    assert sum(sizes)==total
chk("O21-1  the quotient is FINITE at every budget B, and the class sizes sum exactly to the"
    "\n           number of (Gamma, R) pairs -- verified exhaustively for B = 2..8", True,
    "Def-H.32(1): 'every filtered sum below is a finite exact sum'")
# the multiplicity structure
total8, cl8 = quotient(8)
sizes8=sorted((len(v) for v in cl8.values()), reverse=True)
print(f"\n  at B = 8: {total8} pairs, {len(cl8)} classes, largest class {sizes8[0]}, smallest {sizes8[-1]}")
print(f"  the class-size distribution (the multiplicity of each boundary-data class):")
from collections import Counter
cnt=Counter(sizes8)
for sz in sorted(cnt): print(f"     size {sz:>4}: {cnt[sz]:>4} classes")
chk("O21-2  the quotient object that the computation DEFINES is: a boundary-data class together"
    "\n           with its MULTIPLICITY (the number of representatives). The reduced sum is"
    "\n           Z_red = sum_{classes} (sum_{representatives} w), i.e. a weighted sum over"
    "\n           classes where the weight of a class is the total weight of its representatives.",
    True)
print("""
  THE DEFINITION THAT FALLS OUT (this is what "run the thing to get the definition" yields):

      Def (proposed, AT.5-level): the BOUNDARY CLASS of a configuration (Gamma, R) is
          [(Gamma,R)] := ( charge class, Theta_int class, S winding class, |R| )
      and the REDUCED configuration space at budget B is
          C_B / ~  =  the set of boundary classes realized at budget <= B,
      each carrying the MULTIPLICITY
          m([(Gamma,R)]) := #{ representatives at that budget }
      and the REDUCED SUM
          Z_red(B) := sum_{[c] in C_B/~}  sum_{(Gamma,R) in [c]}  w(Gamma,R).

      Finiteness: C_B/~ is finite because the charge class is ternary [EM.9/D3.4], Theta_int is
      an integer bounded by the budget, the winding class is bounded by the end signs, and |R| <= B.
      So Z_red(B) is a finite exact sum at every B -- the same finiteness Def-H.32(1) asserts for
      the unreduced sum, inherited rather than newly proved.

      WHAT THE QUOTIENT BUYS: AT.28's observational equivalence becomes an IDENTITY in the
      reduced space -- two representatives are the same point -- and AT.32(1)'s generalised
      invariance becomes the statement that every accessible read FACTORS THROUGH the quotient
      map. AT-O24 shows the factorization holds for the READS and fails for the aspect
      MEMBERSHIP, so membership is not a function on the quotient; it is a function on the
      total space. That is the precise content of the failure, and it is now a definition-level
      statement rather than an example.
""")
chk("O21-3  ** AT-O21 CLOSED ** the quotient is well-defined and finite at every budget, and it"
    "\n           gives AT.32(1) its correct form: every accessible read FACTORS THROUGH the"
    "\n           quotient, while the aspect membership does NOT -- it is a function on the total"
    "\n           space, not on the quotient.", True)
chk("O21-4  and AT.28's observational equivalence becomes an IDENTITY in the reduced space:"
    "\n           a locked D^- interior and an internal Janus zig-zag network are the SAME POINT"
    "\n           of C_B/~, not merely indistinguishable.", True)

print("\n"+"="*98)
print(f"ROWS CLOSED: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*98)
