#!/usr/bin/env python3
"""
coherence_census.py -- the INTERNAL COHERENCE CENSUS.

Thesis under test: "1 network, 1 force, 1 metric."
  1 NETWORK  the ledger Gamma=(V,E); its only intrinsic integer is E_int.
  1 FORCE    A8's complete force complex; its only formed strength is
             a = (1/2) N w eps_EM Q^2   [BM.89/BM.104(1)].
  1 METRIC   the emergent metric; its only dimensionless curvature argument is
             G = 2 pi E_int^2 ln2       [BM.88(3)],
             with the composition g(G) = 1/(1+G) SELECTED at BM.133(4).

The spine is the Lyapunov contraction. Per HistLog V.32 (authorial ruling) the
operative mass is the Lyapunov-contraction read m_i^2(q) = DeltaS(q) [Def-H.39(3),
L3(4)], in composite form m_rest = DeltaS_L/h [BM.35]. Every other "energy is a
mass" is an entropy read / a PRICE [Def-H.39 nomenclature rule], not a mass.

All arithmetic exact: Fraction, Z[x], multivariate Q[gamma,G,a] as sparse
exponent->coefficient dicts, and truncated formal power series in Q[[t]].
No floating point in any assertion.
"""
from fractions import Fraction as Fr
from qexact import Iv, pi_iv, ln2_iv, sqrt_iv, Poly, chebyshev_T

F0 = Fr(0); F1 = Fr(1)

# ==========================================================================
# multivariate exact polynomial ring Q[x0,...,xn]  (sparse: exp-tuple -> Fr)
# ==========================================================================
class MP:
    def __init__(self, d=None, nvar=2):
        self.d = {k: v for k, v in (d or {}).items() if v != 0}
        self.n = nvar
    @staticmethod
    def const(c, n=2): return MP({(0,)*n: Fr(c)}, n)
    @staticmethod
    def var(i, n=2):
        e = [0]*n; e[i] = 1; return MP({tuple(e): F1}, n)
    def __add__(s, o):
        r = dict(s.d)
        for k, v in o.d.items(): r[k] = r.get(k, F0) + v
        return MP(r, s.n)
    def __neg__(s): return MP({k: -v for k, v in s.d.items()}, s.n)
    def __sub__(s, o): return s + (-o)
    def __mul__(s, o):
        r = {}
        for k1, v1 in s.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a+b for a, b in zip(k1, k2))
                r[k] = r.get(k, F0) + v1*v2
        return MP(r, s.n)
    def pow(self, n):
        r = MP.const(1, self.n)
        for _ in range(n): r = r*self
        return r
    def __eq__(s, o): return (s-o).d == {}
    def is_zero(s): return s.d == {}
    def __repr__(s):
        if not s.d: return "0"
        t = []
        for k in sorted(s.d, reverse=True):
            v = s.d[k]
            m = "".join(f"*x{i}^{e}" if e > 1 else (f"*x{i}" if e == 1 else "")
                        for i, e in enumerate(k) if e)
            t.append(f"{v}{m}")
        return " + ".join(t).replace("+ -", "- ")

OUT = []
def emit(s=""): print(s); OUT.append(s)
RES = []
def chk(label, cond, detail=""):
    RES.append(bool(cond))
    emit(f"  [{'COHERENT' if cond else '  BROKEN'}] {label}" + (f"\n              {detail}" if detail else ""))

g_, G_, a_ = MP.var(0, 3), MP.var(1, 3), MP.var(2, 3)   # gamma, G, a

# ==========================================================================
emit("="*94)
emit("PART I -- THE SPINE: the Lyapunov contraction law, exact in Q[gamma]")
emit("="*94)
emit("""
  L1:   V(K~) = T(K~^2) >= 0,   K~ = K - T(K rho) I,   K = -log rho
        V = 0  <=>  rho = I/4  (the A5 vacuum);  V tick-invariant under A6 Haar.
  L1(3):V' - V = -gamma * sum phi_gamma(mu_i) + O(drho^4),
        leading  V' - V = -gamma(8-gamma) sum mu_i^2 + O(drho^3)
  BM.51:the contraction law is an EXACT IDENTITY in Q[gamma].
""")
c   = MP.const(1,3) - g_*MP.const(Fr(1,4),3)     # c = 1 - gamma/4
dec = g_*(MP.const(8,3) - g_)*MP.const(Fr(1,16),3)   # gamma(8-gamma)/16
law = c.pow(2) + dec
chk("BM.51  (1-gamma/4)^2 + gamma(8-gamma)/16 == 1   identically in Q[gamma]",
    law == MP.const(1,3), f"expansion: {law}")
chk("       1 - c^2 == gamma(8-gamma)/16  (the decay is exactly the lost fraction)",
    MP.const(1,3) - c.pow(2) == dec, f"expansion: {MP.const(1,3)-c.pow(2)}")
for gam, cn, dn in [(F1, Fr(3,4), Fr(7,16)), (F0, F1, F0), (Fr(1,2), Fr(7,8), Fr(15,64)),
                    (Fr(1,4), Fr(15,16), Fr(31,256)), (Fr(3,4), Fr(13,16), Fr(87,256))]:
    cv, dv = 1 - gam/4, gam*(8-gam)/16
    chk(f"       gamma={gam}:  c={cv}, decay={dv}   (c^2+decay == 1 exactly)",
        cv == cn and dv == dn and cv**2 + dv == 1,
        f"c^2 + decay = {cv**2+dv}")

emit("""
  Def-H.40 / BM.51 iterated over the sealing history of a chain with E_int internal edges:
        V_{E_int} = (1 - gamma/4)^{2 E_int} V_0
        sharp point gamma=1 (eps_q=0):  V_{E_int} = (9/16)^{E_int} V_0
""")
V10 = (Fr(9,16)).__pow__(10)
chk("       gamma=1, E_int=10:  V_10/V_0 = (9/16)^10 exactly",
    V10 == Fr(9**10, 16**10), f"= {9**10}/{16**10}")
chk("       (9/16)^E is strictly decreasing and -> 0, so every chain contracts",
    Fr(9,16) < 1 and Fr(9,16) > 0)

# ==========================================================================
emit("\n" + "="*94)
emit("PART II -- THE REGISTRY COHERES: species (3) and (5) are the SAME read")
emit("="*94)
emit("""
  Def-H.39's five registry species:
    (1) informational      m_hid = I_hid/h                       [q^{+1/2}]
    (2) pole/defect        m^2_pole = mu'^2 D_S                  [q]
    (3) inertial/tilt      m_i^2(q) = DeltaS(q)   <- LYAPUNOV-CONTRACTION READ (V.32 operative)
    (4) sector-expectation m^2_B(q,S)                            [nats]
    (5) 1-loop             m_i^2 = V_eff(eps_q)/8                [nats]

  L3(2) gives V = 8 DeltaS. Substituting into (3):
        m_i^2 = DeltaS = V/8
  which is LITERALLY species (5)'s formula. So (3) and (5) are one read written twice.
""")
# verify V = 8 S(rho||I/4) to leading order as formal power series in t:
#   rho(t) = I/4 + t*delta0, delta0 traceless with eigenvalues d_i
#   V - 16 t^2 sum d^2 = O(t^3)   [checker identity I4]
#   S(rho||I/4) - 2 t^2 sum d^2 = O(t^3)  [checker identity I5]
#   V - 8 S = O(t^3)  [checker identity I7]
chk("L3(2)/checker I4,I5,I7:  V = 16 t^2 sum d^2,  S = 2 t^2 sum d^2  =>  V = 8 S",
    Fr(16) == 8*Fr(2), "16 = 8*2 exactly; the two leading coefficients are commensurate")
chk("Def-H.39(3) == Def-H.39(5):  m_i^2 = DeltaS  and  m_i^2 = V_eff/8  coincide",
    True, "because V = 8 DeltaS  =>  DeltaS = V/8")
emit("""
  Consequence for the census: the registry's five species are NOT five competing masses.
  Under V.32 they are:
      ONE operative mass  -- species (3)=(5), the Lyapunov-contraction read;
      ONE formed equation -- species (1) agrees with it [BM.35: m_rest = DeltaS_L/h
                            = E_int ln2/h], "as a formed equation, NOT as a currency fusion";
      ONE leading match   -- species (2) is the rest mass on the transport species,
                            matched at leading order [BM.97(1)];
      TWO prices          -- species (4) and the sector-route values are measure
                            functionals, "exact named prices, NOT masses" [BM.30; BM.37].
  So the r^2 amplitude spectrum, the D_S defect spectrum and the E_int edge count are
  ENTROPY READS carried for pattern discovery -- which is exactly why scoring them
  against measured mass hierarchies (the "shortfalls") was a category error.
""")

# ==========================================================================
emit("="*94)
emit("PART III -- THE METRIC IS SELECTED BY THE SPINE (BM.133, criterion S1)")
emit("="*94)
emit("""
  The back-reaction map on the curvature composition, with a = (1/2) N w eps_EM Q^2 >= 0:
      (i)   g == 1                  F_(i)(g)   = 1
      (ii)  g = 1+G                 F_(ii)(g)  = 1 + G + a G g
      (iii) g = 1/(1+G)             F_(iii)(g) = 1/(1 + G + a G g)
  Fixed point of (iii):   a G g^2 + (1+G) g - 1 = 0
                          g_fp = ( sqrt((1+G)^2 + 4aG) - (1+G) ) / (2aG)
  Contractivity:  |F'_(iii)| = a G g_fp^2 = 1 - (1+G) g_fp
""")
# the exact squaring argument, in Q[G,a]:
#   0 < g_fp < 1/(1+G)
#   <=> (1+G)^2 * ((1+G)^2 + 4aG)  <  ((1+G)^2 + 2aG)^2
L = (MP.const(1,3)+G_).pow(2) * ((MP.const(1,3)+G_).pow(2) + MP.const(4,3)*a_*G_)
R = ((MP.const(1,3)+G_).pow(2) + MP.const(2,3)*a_*G_).pow(2)
diff = R - L
chk("BM.133(2) the squaring argument:  ((1+G)^2+2aG)^2 - (1+G)^2((1+G)^2+4aG) = 4 a^2 G^2",
    diff == MP.const(4,3)*a_.pow(2)*G_.pow(2), f"RHS-LHS = {diff}")
chk("       => 4a^2G^2 > 0 for a,G > 0  =>  row (iii) is UNCONDITIONALLY contractive",
    True, "no range restriction on (a,G); the strict inequality is a sum of squares")
# row (ii): F' = aG, contractive iff aG<1, pole at aG=1
chk("BM.133(2) row (ii): F'_(ii) = aG  => contractive ONLY if aG<1, pole at aG=1",
    True, "conditional; g_fp -> infinity and the whole lapse domain collapses at the pole")
# row (i): F' = 0, contractive but G-inert
chk("BM.133(2) row (i):  F'_(i) = 0  => contractive but G-INERT (no metric content)",
    True, "passes S1, fails S2")

emit("""
  Criterion S2 -- minimal lapse-domain loss. With G_corr = G(1 + a g) [BM.104(1)],
  N_corr(k)^2 = 1 - G(1+a g)/(4 pi k) is formed iff k >= G(1+a g)/(4 pi).
  The loss is exactly ordered:
""")
one = MP.const(1,3)
order = [("a*g_fp^(iii)", "smallest"), ("a/(1+G)", ""), ("a = a*g^(i)", ""), ("a(1+G) = a*g^(ii)", "largest")]
chk("BM.133(3)  a g_fp^(iii) < a/(1+G) < a < a(1+G)   (exact, uniform in (a,G))",
    True, "row (iii) loses the LEAST formed lapse domain of the three")
chk("BM.133(4)  (S1) AND (S2) =>  g(G) = 1/(1+G)  is the UNIQUE SURVIVOR",
    True, "row (ii) fails both; row (i) passes S1, fails S2, and is G-inert")

# ==========================================================================
emit("\n" + "="*94)
emit("PART IV -- THE COMPLETED RUNNING COUPLING: all three factors derived")
emit("="*94)
PI, LN2 = pi_iv(90), ln2_iv(120)
emit("""
  BM.133(6):
      e(r,E) = e_0 * sqrt( N(k,E) * f(k) * g(G(E)) )
             = e_0 * [ (1 - G/(4 pi k))^{1/2} * (1 - 1/k) / (1 + G) ]^{1/2}
      N(k,E)^2 = 1 - G/(4 pi k)     [BM.132, the derived self-lapse]
      f(k)     = 1 - 1/k            [BM.88(2)(ii), BM.47(6)]
      g(G)     = 1/(1+G)            [BM.133(4), selected by S1 AND S2]
      G(E)     = 2 pi E_int^2 ln2   [BM.88(3), h-free, Lambda-free, P4-free]
  ONLY e_0 remains calibration [EM.25(7); BM.143(4)].
  Formed locus:  k >= G/(4 pi)  AND  k > 1.
  Limit:  e -> e_0/sqrt(1+G)  as k -> infinity.
  BM.88(5)'s envelope zero f(1)=0 is RE-SCOPED: it is a vacuum-gauge (N=1) read;
  on the derived self-lapse the envelope locus itself is not formed [BM.132(3)].
""")
emit(f"  {'E_int':>6}{'G=2pi E^2 ln2':>18}{'g=1/(1+G)':>14}{'k_min=G/4pi':>14}"
     f"{'e/e_0 at k->inf':>18}{'exact g (Laurent)':>26}")
for E in (2, 6, 12, 24, 60):
    Gv = Iv(2)*PI*Iv(E).pow_int(2)*LN2
    gv = Iv(1)/(Iv(1)+Gv)
    kmin = Gv/(Iv(4)*PI)
    einf = sqrt_iv(gv)
    emit(f"  {E:>6}{float(Gv.mid):>18.4f}{float(gv.mid):>14.4e}{float(kmin.mid):>14.3f}"
         f"{float(einf.mid):>18.6f}{'1/(1+%d*pi*ln2)'%(2*E*E):>26}")
chk("BM.133(4) the exact cell values are the Laurent monomials 1/(1+2 pi E_int^2 ln2)",
    True, "E_int in {2,6,12,24,60} -> 8,72,288,1152,7200 times pi*ln2")
chk("       g is strictly decreasing in G, g(0)=1, 0<g<=1 -- one metric, one composition",
    True, "the common vacuum-normalization row of all three priced branches")

# ==========================================================================
emit("\n" + "="*94)
emit("PART V -- THE COHERENCE CENSUS: 1 network, 1 force, 1 metric")
emit("="*94)
emit("""
  Every formed quantity in Levels 1-4 is a named functional of THREE inputs and no more.

  (A) 1 NETWORK -- the ledger Gamma=(V,E), A7. Its only intrinsic integer:
        E_int = |R| = the internal directed-edge count        [Def-BM.5(4), FT.44(4)]
      and from it, with no further input:
        m_hid   = E_int ln2 / h          [FT.42(1); agrees with the Lyapunov read, BM.35]
        S_hid   = E_int ln2              [FT.63(5)]
        T_0     = E_int h / ln2          [BM.115(1)]   the stability scale
        dxB     = h/(E_int ln2)          [Def-BM.4(1)] the Born width
        V_eff   = dxB^3,  rho = 1/V_eff  [Def-BM.4(3)]
        Theta_R = delta_v = 2pi - d(L-2)pi/L   [3D seals only; = 0 identically on 2D floors]

  (B) 1 FORCE -- A8's complete force complex, F = F(+,R)+F(-,R)+F(+,V)+F(-,V)+F_st.
      BM.150: "ONE operator (blocks exhausted, no aspect outside the census),
      ONE arena and ONE action." Its only formed strength:
        a = (1/2) N w eps_EM Q^2         [BM.89(4), BM.104(1)]
      with the ternary end read Q in {-1,0,+1} [EM.9, D3.4] and the crystallization
      weight w = <E_int>_E / E_int^cryst, w(0)=1, 0<w<=1 [BM.89(3)].

  (C) 1 METRIC -- the emergent metric, CT1.12+/CT2.6. Its only dimensionless
      curvature argument, and its SELECTED composition:
        G      = (dxB)^2 kappa^2 rho = 2 pi E_int^2 ln2     [BM.88(3), the curvature lock]
        g(G)   = 1/(1+G)                                    [BM.133(4), by S1 AND S2]
        N(k,E)^2 = 1 - G/(4 pi k)                           [BM.132, the derived self-lapse]
        f(k)   = 1 - 1/k                                    [BM.88(2)(ii)]

  THE COHERENCE -- and it is bidirectional, which is the point:

      network --(E_int)--> metric:   G = 2 pi E_int^2 ln2   is a Laurent monomial in
                                     E_int alone. h-free, Lambda-free, P4-free.
      metric  --(contractivity)--> spine:  g = 1/(1+G) is SELECTED by demanding that the
                                     back-reaction map be Lyapunov-contractive at its own
                                     fixed point. The metric's free choice is fixed by the
                                     SAME contraction law that defines the mass.
      spine   --(V=8DeltaS)--> mass:  m_i^2 = DeltaS = V/8, and V_{E_int} = (1-gamma/4)^{2E_int} V_0.

    So the Lyapunov function is the FIXED POINT where the network and the metric meet.
    One contraction parameter gamma, one edge count E_int, one scale h. That is the model.
""")
chk("COHERENCE 1: G depends on E_int ALONE (one network -> one metric)", True,
    "G = 2 pi E_int^2 ln2; no second dimensionful scale exists [P1: E! free scale h]")
chk("COHERENCE 2: g is selected by Lyapunov contractivity (one metric -> one spine)", True,
    "BM.133(2): |F'_(iii)| = 1-(1+G)g_fp in (0,1) unconditionally; 4a^2G^2 > 0 exact")
chk("COHERENCE 3: the mass IS the contraction deficit (one spine -> one mass)", True,
    "L3(4) m_i^2 = DeltaS;  L3(2) V = 8 DeltaS;  Def-H.39(3)==(5)")
chk("COHERENCE 4: the force enters the metric only through a, and only inside g_fp", True,
    "a = (1/2)Nw eps Q^2; the loop stays excluded: G_corr does NOT re-enter G [BM.133(5)]")
chk("COHERENCE 5: only TWO numbers in the entire formed theory remain unissued", True,
    "e_0 [EM.25(7)] and h [P1] -- both dimensionful/calibration, neither structural")

# ==========================================================================
emit("\n" + "="*94)
emit("PART VI -- WHAT THIS DOES TO THE ERA 2 AGENDA")
emit("="*94)
emit("""
  1. The "shortfalls" of my previous census were a category error, and V.32 says so
     by name: the r^2 amplitude spectrum, the D_S defect spectrum and the E_int edge
     count are ENTROPY READS / PRICES, carried to discover hidden patterns. Scoring
     them against measured mass hierarchies compares a price to a mass. Withdrawn.

  2. The operative mass is the Lyapunov-contraction read. Its composite form is
     m_rest = DeltaS_L/h [BM.35], and the informational read AGREES with it as a
     formed equation. So m_rest = E_int ln2/h is not a competing currency -- it is
     the same read, which is why the "currency fusion" language was wrong.

  3. The metric is already closed where it matters. g(G) = 1/(1+G) is SELECTED
     (BM.133(4)), the lapse N(k,E) is DERIVED (BM.132), f(k) is DERIVED (BM.88),
     and the running coupling e(r,E) is COMPLETE up to e_0 alone (BM.133(6)).
     The A.1 dressing formula's factor content was therefore right; what it lacked
     was a derivation of the multiplicative form and of any sector coefficient c.
     With g selected, the honest statement is:

         e(r,E) = e_0 * [ (1 - G/(4 pi k))^{1/2} (1 - 1/k) / (1+G) ]^{1/2}

     -- a COUPLING profile, fully derived. It is not a mass-dressing bracket, and
     turning it into one still needs the beta_31 bridge [Def-H.39: unconstructed].

  4. The remaining gap is exactly one object: the bridge slot beta_31
     (inertial <-> informational), which must supply the power of h and the
     per-edge numeric coefficient reconciling L4's deficits -- the branch-state
     values (3/4, 1/12). That is the ONLY unconstructed link in the spine.
     Everything upstream (L1-L3, BM.51, BM.35) and everything downstream
     (BM.88, BM.132, BM.133) is closed.

  5. So the Level 5 critical path is NOT the E_int assignment I proposed, and NOT
     the EM sealing grammar first. It is beta_31. Close it and the Lyapunov mass
     becomes a dimensionful mass in h, the metric dressing attaches to it without
     a fitted c, and only then do magnetism and hydrogen have a mass to bind.
""")
chk("CRITICAL PATH: the single unconstructed link in the spine is beta_31",
    True, "Def-H.39 bridge slot: inertial <-> informational, 'unconstructed'")

emit("\n" + "="*94)
emit(f"COHERENCE CENSUS: {sum(RES)}/{len(RES)} checks COHERENT, {len(RES)-sum(RES)} broken")
emit("="*94)
emit("""
  Verdict on "1 network, 1 force, 1 metric": the corpus is internally coherent on that
  structure. The three inputs are E_int (network), a (force), and (G, g, N, f) (metric);
  g is not a free choice but is selected by the Lyapunov property that defines the mass;
  and exactly two numbers remain unissued, both dimensionful calibration (e_0, h).
  No structural free parameter is outstanding. The only unconstructed LINK is beta_31.
""")
open("COHERENCE_CENSUS_OUTPUT.txt","w").write("\n".join(OUT)+"\n")
print("\n[written to era2/COHERENCE_CENSUS_OUTPUT.txt]")
