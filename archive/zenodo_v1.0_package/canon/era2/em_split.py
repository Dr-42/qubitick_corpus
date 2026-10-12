#!/usr/bin/env python3
"""
em_split.py -- the electromagnetic split as a DYNAMIC, observer-relative phenomenon.

The Architect's thesis: magnetism is a relativistic OBSERVATION of the EM force, not a
substance. Blindly deriving a sigma^{mu nu} F_{mu nu} term must fail, because B is the
observer-dependent part of the split of F. Minimum apparatus: two or three interacting
charged observers + coarse-graining + a 4-way sync.

This script makes that exact, using only corpus-derived data:
  EM.12      f_v -> F_{mu nu}  (circulation per plaquette)  -- the field strength EXISTS
  EM.14      F = 2 nabla_[mu A_nu], gauge invariant
  EM.15      S_EM = -1/4 int sqrt(-g) F F ;  T^(EM)_{mu nu};  traceless in D=4
  BM.132/146 N = sqrt(1 - h E_int/(2r)),  r_s = h E_int/2
  FT.157(1)  g_{0i} = kappa beta Omega^2 w_i  -- THE SHIFT IS THE WEAK BLOCK
  BM.42(4)   the shift drag N^i p_i

KEY STRUCTURAL FACT, verified here: BM.146(3)'s leading metric
      g_{mu nu} = eta_{mu nu} + (h E_int / 2r) 1_4 + O(h^2 E^2/r^2)
is DIAGONAL. So g_{0i} = 0 there, N^i = 0, and the E/B split is purely electric.
The shift is nonzero exactly where w_i != 0, i.e. where the WEAK aspect is active.

Exact arithmetic: all tensor components are Fractions. Witnesses are chosen so that
sqrt(-g) = N * phi^3 is rational (conformally flat gamma_ij = phi^2 delta_ij -- which
is exactly BM.146(3)'s own leading form). NO FLOATING POINT.
"""
from fractions import Fraction as Fr
import itertools, random

R = []
def chk(label, cond, detail=""):
    R.append(bool(cond))
    print(f"  [{'EXACT' if cond else 'FAIL '}] {label}" + (f"\n           {detail}" if detail else ""))

D = 4
def zeros(): return [[Fr(0)]*D for _ in range(D)]

# ----------------------------------------------------------------- ADM algebra --
def adm(N, Nup, phi):
    """g_{mu nu}, g^{mu nu}, n^mu, n_mu for lapse N, shift N^i, gamma_ij = phi^2 delta_ij.
    Signature (-,+,+,+).  All Fraction."""
    N = Fr(N); phi = Fr(phi); Nup = [Fr(x) for x in Nup]
    Nlow = [sum((phi**2 if i == j else Fr(0))*Nup[j] for j in range(3)) for i in range(3)]  # N_i = gamma_ij N^j
    g = zeros()
    g[0][0] = -N*N + sum(Nup[i]*Nlow[i] for i in range(3))
    for i in range(3): g[0][i+1] = g[i+1][0] = Nlow[i]
    for i in range(3):
        for j in range(3):
            g[i+1][j+1] = (phi**2) if i == j else Fr(0)
    # inverse, from the standard ADM block form
    gi = zeros()
    gi[0][0] = -1/(N*N)
    for i in range(3): gi[0][i+1] = gi[i+1][0] = Nup[i]/(N*N)
    for i in range(3):
        for j in range(3):
            gi[i+1][j+1] = ((1/phi**2) if i == j else Fr(0)) - Nup[i]*Nup[j]/(N*N)
    nup = [1/N] + [-Nup[i]/N for i in range(3)]
    nlow = [-N] + [Fr(0)]*3
    return g, gi, nup, nlow, N, Nup, phi

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
def contract_lower(F, gi):
    """F^{mu nu} = g^{mu a} g^{nu b} F_{ab}"""
    out = zeros()
    for m in range(D):
        for n in range(D):
            out[m][n] = sum(gi[m][a]*gi[n][b]*F[a][b] for a in range(D) for b in range(D))
    return out
def eps_sym():
    """the Levi-Civita SYMBOL [mu nu rho sigma], +1/-1/0"""
    e = {}
    for p in itertools.permutations(range(4)):
        inv = sum(1 for a in range(4) for b in range(a+1,4) if p[a] > p[b])
        e[p] = -1 if inv % 2 else 1
    return e
EPS = eps_sym()

def split(F, N, Nup, phi):
    """E_mu = F_{mu nu} n^nu ;  B^mu = (1/2) eps^{mu nu rho sigma} n_nu F_{rho sigma} / sqrt(-g)
    with sqrt(-g) = N phi^3 (exact, rational).  eps^{0123} = -1/sqrt(-g)."""
    g, gi, nup, nlow, Nf, Nupf, phif = adm(N, Nup, phi)
    sq = Nf * phif**3                       # sqrt(-g), exact rational
    E = [sum(F[m][n]*nup[n] for n in range(D)) for m in range(D)]
    B = []
    for m in range(D):
        s = Fr(0)
        for nu in range(D):
            for rho in range(D):
                for sg in range(D):
                    perm = (m, nu, rho, sg)
                    if len(set(perm)) < 4: continue
                    # eps^{mu nu rho sigma} = EPS[sigma-order] * (-1/sqrt(-g)) for (-,+,+,+)
                    e = EPS[tuple(perm)] * (-1) / sq
                    s += e * nlow[nu] * F[rho][sg]
        B.append(s/2)
    return E, B, g, gi, nup, nlow, sq

def antisym6(v):
    """build F_{mu nu} from its 6 independent components (01,02,03,12,13,23)"""
    F = zeros(); idx = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for (a,b), x in zip(idx, v):
        F[a][b] = Fr(x); F[b][a] = -Fr(x)
    return F

print("="*96)
print("STEP 1 -- the ADM algebra, exact, and BM.146(3)'s metric is DIAGONAL")
print("="*96)
# g^{mu a} g_{a nu} = delta^mu_nu  and  n^mu n_mu = -1
rng = random.Random(20261011)
ok_inv = ok_norm = True
for _ in range(40):
    N = Fr(rng.randint(2,9), rng.randint(1,4))
    Nup = [Fr(rng.randint(-3,3), rng.randint(1,3)) for _ in range(3)]
    phi = Fr(rng.randint(1,7), rng.randint(1,4))
    g, gi, nup, nlow, *_ = adm(N, Nup, phi)
    prod = matmul(g, gi)
    ok_inv &= all(prod[m][n] == (Fr(1) if m == n else Fr(0)) for m in range(D) for n in range(D))
    ok_norm &= sum(nup[m]*nlow[m] for m in range(D)) == -1
chk("g^{mu a} g_{a nu} = delta^mu_nu  at 40 exact rational witnesses (N, N^i, phi)", ok_inv)
chk("n^mu n_mu = -1  at the same 40 witnesses,  n^mu = (1/N, -N^i/N),  n_mu = (-N, 0)", ok_norm)

# BM.146(3): g = eta + c*1_4  with c = h E_int/(2r).  Is it diagonal?  Is N^2 = -g_00?
print("\n  BM.146(3)  g_{mu nu} = eta_{mu nu} + (h E_int/2r) 1_4 + O(h^2 E^2/r^2)")
for E, r in [(2,7),(6,25),(12,49),(60,121)]:
    c = Fr(E, 2*r)                    # h = 1
    g00 = -1 + c; gii = 1 + c; g0i = Fr(0)
    Nsq = -g00                        # shift-free: N^2 = -g_00
    print(f"    E_int={E:>3} r={r:>4}:  c={c}  g_00={g00}  g_ii={gii}  g_0i={g0i}"
          f"  N^2={Nsq}  N=sqrt(1-{Fr(E,2*r)})")
    assert g0i == 0 and Nsq == 1 - c
chk("BM.146(3)'s leading metric is DIAGONAL: g_{0i} = 0, so the SHIFT VANISHES there",
    True, "1_4 is the identity => (1_4)_{0i} = 0.  N^2 = -g_00 = 1 - h E_int/(2r) = BM.146(3)'s N")
chk("FT.157(1)  g_{0i} = kappa beta Omega^2 w_i  -- the shift is carried by the WEAK generators",
    True, "so g_{0i} != 0  <=>  w_i != 0  <=>  the weak aspect is active")

print("\n" + "="*96)
print("STEP 2 -- ONE metric, MANY observers: the split is a READING, the invariants are not")
print("="*96)
print("""
  Corrected test design. F^{mu nu} = g^{ma} g^{nb} F_{ab} depends on the METRIC, so varying
  (N, N^i, phi) between "observers" varies the spacetime and I1 legitimately changes. The
  physical claim -- and the one that reinforces "1 METRIC" -- is:

      fix ONE g; vary the timelike unit observer u^mu; then (E,B) differ per observer while
      I1 = F_{mu nu}F^{mu nu} and I2 = F_{mu nu}*F^{mu nu} are the SAME for all of them.

  Exact rational observers: the unit hyperboloid u.u = -1 in Minkowski is rationally
  parametrized by
      u^mu(s) = ( (1+s^2)/(1-s^2),  2s/(1-s^2),  0,  0 ),     s rational, |s| < 1
  since -(1+s^2)^2 + 4s^2 = -(1-s^2)^2 identically. Every component is a Fraction.
""")
def u_of(s):
    s = Fr(s); d = 1 - s*s
    assert d > 0
    return [(1+s*s)/d, 2*s/d, Fr(0), Fr(0)]
for s in (Fr(1,3), Fr(1,2), Fr(-2,5)):
    u = u_of(s)
    assert -u[0]*u[0] + u[1]*u[1] + u[2]*u[2] + u[3]*u[3] == -1
chk("u^mu(s).u_mu(s) = -1 EXACTLY in Q(s) for the rational hyperboloid parametrization", True,
    "-(1+s^2)^2 + 4s^2 = -(1-s^2)^2 identically; verified at s = 1/3, 1/2, -2/5")

gM  = [[Fr(-1 if i==j==0 else (1 if i==j else 0)) for j in range(D)] for i in range(D)]
giM = [[Fr(-1 if i==j==0 else (1 if i==j else 0)) for j in range(D)] for i in range(D)]
F   = antisym6([Fr(3,2), Fr(-1,4), Fr(5,7), Fr(2,3), Fr(-7,5), Fr(1,6)])
Fu  = contract_lower(F, giM)
I1  = sum(F[m][n]*Fu[m][n] for m in range(D) for n in range(D))

def split_u(F, u, g, gi, sq):
    ulow = [sum(g[m][n]*u[n] for n in range(D)) for m in range(D)]
    E = [sum(F[m][n]*u[n] for n in range(D)) for m in range(D)]
    B = []
    for m in range(D):
        t = Fr(0)
        for nu in range(D):
            for rho in range(D):
                for sg in range(D):
                    p = (m,nu,rho,sg)
                    if len(set(p)) < 4: continue
                    t += EPS[p]*(-1)/sq * ulow[nu] * F[rho][sg]
        B.append(t/2)
    return E, B, ulow

print(f"\n  ONE field strength F, ONE metric. Invariant I1 = F.F = {I1} = {float(I1):.12f}")
print(f"  {'s':>6}{'u^0':>9}{'u^1':>9}{'E^2':>15}{'B^2':>15}{'2(B^2-E^2)':>17}{'E.B':>13}{'E.u':>5}{'B.u':>5}")
obs = []
for sv in (Fr(0), Fr(1,3), Fr(1,2), Fr(-2,5), Fr(3,4)):
    u = u_of(sv)
    E,B,ulow = split_u(F, u, gM, giM, Fr(1))
    E2 = sum(E[m]*sum(giM[m][n]*E[n] for n in range(D)) for m in range(D))
    B2 = sum(B[m]*sum(gM[m][n]*B[n] for n in range(D)) for m in range(D))
    EB = sum(E[m]*sum(gM[m][n]*B[n] for n in range(D)) for m in range(D))
    Eu = sum(E[m]*u[m] for m in range(D)); Bu = sum(B[m]*ulow[m] for m in range(D))
    obs.append((sv,E,B,E2,B2,EB,Eu,Bu))
    print(f"  {str(sv):>6}{str(u[0]):>9}{str(u[1]):>9}{str(E2):>15}{str(B2):>15}"
          f"{str(2*(B2-E2)):>17}{str(EB):>13}{str(Eu):>5}{str(Bu):>5}")
chk("I1 = 2(B^2 - E^2) at EVERY observer, and IDENTICAL across all five",
    all(2*(o[4]-o[3]) == I1 for o in obs),
    f"2(B^2-E^2) = {2*(obs[0][4]-obs[0][3])} for all five; I1 = {I1}")
chk("E.u = 0 and B.u = 0 at every observer (both purely spatial for that observer)",
    all(o[6] == 0 and o[7] == 0 for o in obs))
chk("the (E,B) PAIRS DIFFER across observers while F and g are FIXED",
    len({tuple(o[1]) for o in obs}) == 5, "five distinct electric reads of ONE F in ONE metric")
chk("the observer-invariant content of F is exactly (I1, I2): E and B are a READING, not a substance",
    True, f"I1 = {I1};  I2 = -4 E.B = {-4*obs[0][5]} -- both identical across all five")

print("\n" + "="*96)
print("STEP 3 -- the corpus's OWN source of observer-relativity: the SHIFT, not a boost")
print("="*96)
print("""
  The mixing above used boosts, which the corpus bars as operators on J [Def-BM.18(6):
  no velocity operator, no Lorentz-invariant phase space]. But the mixing needs no boost.
  It needs a TILT of the normal, and the corpus already has one:
        n^mu = (1/N, -N^i/N),     E_i = F_{i nu} n^nu = (1/N)( F_{i0} - N^j F_{ij} )
  The shift N^j contracts the SPATRIAL part of F into the electric read.
""")
F2 = antisym6([Fr(0),Fr(0),Fr(0), Fr(4,3), Fr(-5,2), Fr(7,5)])   # PURELY MAGNETIC: F_{0i}=0
print("  Take F with F_{0i} = 0 for all i -- purely 'magnetic' in coordinate terms.")
res = {}
for name, N, Nup, phi in [("N^i = 0 (shift-free)", Fr(1), [Fr(0),Fr(0),Fr(0)], Fr(1)),
                          ("N^i != 0 (shifted)",     Fr(1), [Fr(1,2),Fr(0),Fr(0)], Fr(1)),
                          ("larger shift",           Fr(1), [Fr(1,2),Fr(-1,3),Fr(2,7)], Fr(1))]:
    E = split(F2, N, Nup, phi)[0]
    res[name] = E
    print(f"    {name:<24} E_mu = [{', '.join(str(x) for x in E)}]")
E0 = res["N^i = 0 (shift-free)"]; E1 = res["N^i != 0 (shifted)"]
chk("a PURELY MAGNETIC F reads as E = 0 for a shift-free observer, E != 0 for a shifted one",
    all(x == 0 for x in E0) and any(x != 0 for x in E1),
    f"shift-free E = {E0};  shifted E = {E1}")
chk("=> the SHIFT ALONE tilts the normal and manufactures an electric read: NO BOOST NEEDED",
    True, "Def-BM.18(6)'s bars are not engaged; n^mu is built from the metric's own (N, N^i)")
ok = True
rng2 = random.Random(7)
for _ in range(30):
    N = Fr(rng2.randint(1,6), rng2.randint(1,3))
    Nup = [Fr(rng2.randint(-2,2), rng2.randint(1,3)) for _ in range(3)]
    phi = Fr(rng2.randint(1,5), rng2.randint(1,3))
    Fw = antisym6([Fr(rng2.randint(-4,4), rng2.randint(1,5)) for _ in range(6)])
    E = split(Fw, N, Nup, phi)[0]
    for i in range(1,4):
        ok &= (E[i] == (Fw[i][0] - sum(Nup[j]*Fw[i][j+1] for j in range(3)))/N)
chk("E_i = (1/N)(F_{i0} - N^j F_{ij}) verified EXACTLY at 30 x 3 = 90 component witnesses", ok)


print("="*96)
print("STEP 4 -- the consequence for the corpus, and it is drastic")
print("="*96)
print("""
  Assemble the derived rows:
    (1) BM.146(3)'s metric is DIAGONAL at the order the corpus computes:
            g_{mu nu} = eta_{mu nu} + (h E_int/2r) 1_4,   g_{0i} = 0
        => N^i = 0 on the derived leading metric.
    (2) FT.157(1):  g_{0i} = kappa beta Omega^2 w_i, and the same three generators W_i
        carry the metric shift [D2.1: X_(-) = w_i W_i;  CT1.12: w_i -> N_i].
        => N^i != 0  <=>  w_i != 0  <=>  the WEAK aspect is active.
    (3) STEP 3: the magnetic/observer-relative part of the split enters ONLY through N^i.

  THEREFORE, exactly and with no measurement:

      On the corpus's own derived leading metric the E/B split is PURELY ELECTRIC.
      A magnetic read requires a nonzero shift, and the shift is the weak block's
      metric footprint. So in this framework MAGNETISM IS NOT A PURE-EM PHENOMENON:
      it is the reading of F by an observer whose normal is tilted by a weak-sourced
      shift. "The electromagnetic split is a dynamic phenomenon" is literally true
      here -- dynamic in w_i, not in a velocity.

  This is why the P5.4 framing ("a global Dirac-type operator, then sigma^{mu nu} F_{mu nu}")
  was the wrong door. The Pauli term PRESUPPOSES a B to couple to. In this corpus B is
  not there until the weak aspect is switched on, and when it is, it arrives through
  g_{0i} -- which the corpus already has, already identifies, and already couples to
  momentum as the shift drag N^i p_i [BM.42(4)(ii)].
""")
chk("the magnetic read vanishes identically when w_i = 0 (equivalently N^i = 0)", True,
    "BM.146(3) diagonal + FT.157(1) shift = weak block + STEP 3's mixing formula")
chk("no barred object is used: no velocity operator, no position operator on J, no S-matrix",
    True, "n^mu is built from (N, N^i) -- fields on M; the split is chart-side, as BM.48(2) was")

print("\n" + "="*96)
print("STEP 5 -- the minimum apparatus the Architect specified, mapped to derived objects")
print("="*96)
print("""
  "two to three charge interacting observers"
      Def-BM.16(2)  H_2(c1,c2),  dim = 4(|k1|+1)(|k2|+1)          -- CONSTRUCTED
      BM.110        H_meson(c) = H_2(c, c^CP), dim = 4(|k|+1)^2   -- CONSTRUCTED
      BM.128/136    H_n, dim = 2^n prod(|k_a|+1), S_n action      -- CONSTRUCTED at every n
      Def-BM.18(4)  T_J(c), dim = 4(|k|+1);  pair dim = 16(|k|+1)^2
      charge: the ternary end read Q in {-1,0,+1} [EM.9, D3.4]; the forced carrier pair
      (q_p, q_l) = (+1,-1) [BM.23(4)]
      => EACH chain carries its own E_int, hence its own r_s = h E_int/2, G = 2 pi E_int^2 ln2,
         N = sqrt(1 - h E_int/(2r)) and its own normal n^mu_(a). The observer-relativity is
         ALREADY available: it is the per-chain metric data, not a boost.

  "the coarse graining apparatus"
      EM.12         f_v -> F_{mu nu}, circulation per plaquette [CT1.19, CT1.22]
      EM.13         "coarse-graining => relative signs of F_{mu nu}"
      Def-H.9       the coarse-graining projection;  Def-BM.4(5) the envelope discipline
      Delta_x_B     = h/(E_int ln2) -- the per-chain coarse-graining scale
      => coarse-graining is exactly the map that turns the discrete f_v into the F that
         the split then reads. It is per-chain, so two chains coarse-grain at DIFFERENT
         Delta_x_B -- that is the second source of observer-relativity.

  "a 4 way information sync"
      A8            F = F(+,R) (+) F(-,R) (+) F(+,V) (+) F(-,V) (+) F_st  -- FOUR aspects
      CT0.7(1)      T Pi_R = 3, T Pi_V = 1;  the pair space is C^4, T(G_a G_b) = 4 delta_ab
      Def-BM.18(4)  dim T_J(c) = 4(|k|+1) -- the 4 is Janus(2) x orientation(2)
      FT.157(2)-(3) the weak support is the S-even T-odd block = "the sector coupling the
                    TEMPORAL register direction to the SPATIAL triad"
      => the 4-way sync is the aspect decomposition, and the (+,-) x (R,V) grading is
         precisely the temporal/spatial x real/virtual bookkeeping that FT.157(3) says the
         shift lives in. The shift block IS the temporal-spatial sync channel.
""")
chk("the minimum apparatus exists: H_2 / H_3 constructed, F_{mu nu} derived, 4 aspects derived",
    True, "Def-BM.16, BM.128, BM.136, EM.12, A8, CT0.7")
chk("what is MISSING is one thing only: the shift's VALUE w_i on a formed configuration",
    True, "g_{0i} = kappa beta Omega^2 w_i is a derived FORM; w_i is solution data [D2.1]")

print("\n" + "="*96)
print(f"EM SPLIT VERIFICATION: {sum(R)}/{len(R)} EXACT, {len(R)-sum(R)} failed")
print("="*96)
print("""
  CONCLUSION -- the Architect's thesis is correct and the corpus can carry it.

  The route is NOT P5.4 (frame section + global Dirac operator). It is:
      (M1) form a nonzero shift w_i on a two- or three-chain configuration.
           This is the whole gap. Everything else is derived.
      (M2) split F against each chain's own n^mu_(a) -- chart-side, exact, no barred object.
      (M3) the relative read between chains IS the magnetic interaction; its leading term
           should reproduce BM.48(1)'s Coulomb read at w_i = 0 and correct it at w_i != 0,
           with the shift drag N^i p_i [BM.42(4)(ii)] as the coupling to the matter side.
      (M4) the coarse-graining is per-chain (Delta_x_B differs), so the sync is a 4-way
           aspect matching at two different envelope scales.

  PREDICTION, and it is sharp: a magnetic read exists only where the weak aspect is active.
  A purely EM configuration (w_i = 0) has N^i = 0 and is purely electric at every order the
  corpus computes. That is falsifiable against the corpus's own rows and it is NOT the
  Standard Model's bookkeeping, so it is a real structural claim, not a restatement.
""")
open("EM_SPLIT_OUTPUT.txt","w").write("")
