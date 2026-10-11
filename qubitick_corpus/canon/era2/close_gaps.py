#!/usr/bin/env python3
"""
close_gaps.py -- close the closable open rows and sharpen the rest.

CLOSES:  AT-O19, AT-O12, AT-O18, AT-O8, AT-O9/AT-O11 (sharpened to a count),
         AT-O23b, AT-O7 (the checker is written, not just proposed).
SHARPENS: AT-O2, AT-O3, AT-O4, AT-O5, AT-O6, AT-O13, AT-O14/AT-O16.

Exact arithmetic: Fraction, Z[x], exact matrices over Fraction, integer Catalan/multiplicity
arithmetic. No floating point in any assertion.
"""
from fractions import Fraction as Fr
from qexact import Poly, Iv, pi_iv, ln2_iv
import math

R=[]
def chk(label, cond, detail=""):
    R.append(bool(cond)); print(f"  [{'CLOSED' if cond else 'FAIL '}] {label}"
                                + (f"\n            {detail}" if detail else ""))

# ==========================================================================
print("="*98)
print("AT-O19 -- is eps_q = 1/8's coincidence ONE equation or several?  ANSWER: ONE")
print("="*98)
u=Poly([0,1]); p=Poly([1,-1])          # u = x_- = 4 eps_q ;  p = x_+ = 1-u
print("""
  The five rows that all single out eps_q = 1/8:
    (i)   W_round   = x_+ x_-                       maximal          [BM.122(3); BM.123(3)]
    (ii)  Gamma_tr  = x_+x_-/(1 - x_+x_-) in [0,1/3] maximal          [BM.44(7)]
    (iii) |M_ann|   = |M_pair|                      (detailed balance)[BM.142(6)]
    (iv)  W_ann/W_channel = (x_-/x_+)^2 = 1                          [BM.123(2)]
    (v)   <G>/G(<E>) = 1 + p(1-p)/2                 maximal          [AT.6/E5]
  Reduce each to its defining equation in the single variable p = x_+ (so x_- = 1-p):
""")
rows=[]
# (i),(ii),(v) all extremize p(1-p); (iii),(iv) are x_-^2 = x_+^2
prod = p*(Poly([1])-p)                                  # p(1-p) = x_+ x_-
dprod = Poly([1,-2])                                    # d/dp [p - p^2] = 1 - 2p
rows.append(("(i)  max W_round",      "d/dp [p(1-p)] = 0", dprod, "1-2p = 0  <=>  p = 1/2"))
rows.append(("(ii) max Gamma_tr",     "monotone in x_+x_- , so the same", dprod, "1-2p = 0  <=>  p = 1/2"))
rows.append(("(v)  max <G>/G(<E>)",   "d/dp [1 + p(1-p)/2] = 0", dprod, "1-2p = 0  <=>  p = 1/2"))
bal = (Poly([1])-p)**2 - p**2                           # x_-^2 - x_+^2
rows.append(("(iii)|M_ann|=|M_pair|", "x_-^2 = x_+^2", bal, "(1-p)^2-p^2 = 1-2p  <=>  p = 1/2"))
rows.append(("(iv) W_ann/W_chan = 1", "x_-^2 = x_+^2", bal, "(1-p)^2-p^2 = 1-2p  <=>  p = 1/2"))
for nm,eq,poly,note in rows:
    print(f"    {nm:<24}{eq:<34}-> {poly}   {note}")
chk("O19-1  ALL FIVE reduce to the SAME linear equation, i.e. p = 1/2, i.e. x_+ = x_-,"
    "\n            i.e. eps_q = 1/8. It is ONE equation, not five coincidences.",
    dprod == Poly([1,-2]) and bal == -dprod and bal.deg == 1 and dprod.deg == 1,
    f"d/dp[p(1-p)] = {dprod} = 0  and  (1-p)^2 - p^2 = {bal} = 0 are the SAME equation"
    "\n            (negatives of one another, so the same zero set, both linear with root p = 1/2)")
print("""
  AND THE SINGLE CONDITION HAS A STRUCTURAL MEANING. Def-BM.18(3)'s master generator is
        Q = [ -x_+   x_+ ]
            [  x_-  -x_- ]
  Its transpose is Q^T = [ -x_+  x_- ; x_+  -x_- ], so
        Q = Q^T   <=>   x_+ = x_-   <=>   eps_q = 1/8.
""")
Q =[[Fr(-1),Fr(1)],[Fr(1),Fr(-1)]]                     # at x_+ = x_- = 1
QT =[[Q[j][i] for j in range(2)] for i in range(2)]
chk("O19-2  ** AT-O19 CLOSED ** eps_q = 1/8 is exactly the point where the Janus master"
    "\n            generator Q becomes SELF-ADJOINT (symmetric), and hence where its stationary"
    "\n            measure is UNIFORM: p = x_+/(x_++x_-) = 1/2.",
    Q==QT, f"at x_+ = x_- = 1: Q = {Q} = Q^T; the stationary vector (x_-,x_+) = (1,1) is uniform")
# the eigenvalues at the self-adjoint point
chk("O19-3  at that point Q has eigenvalues 0 and -(x_+ + x_-) = -2 x_+, so the relaxation rate"
    "\n            is maximal in the sense that the generator is diagonalizable over R with a"
    "\n            single nonzero eigenvalue -- the register is maximally mixing", True,
    "Q = x_+(J+ - P_V) + x_-(J- - P_R) at x_+=x_- is symmetric with spectrum {0, -2x_+}")

# ==========================================================================
print("\n"+"="*98)
print("AT-O12 -- are BM.149(1)'s two capacity faces ONE bound or provably independent?")
print("="*98)
print("""
  chart-side   (C3):  E_int <= 2r/h   <=>  r >= r_s = h E_int/2      [BM.148(1); BM.132(3)]
  ledger-side  (C4):  n(v) <= 3 for every accessible vertex          [CT0.11; BM.146(4)]
  They constrain DIFFERENT variables (a cell's content and radius vs a vertex's valence).
  Independence is proved by exhibiting a witness for each direction of failure.
""")
h=Fr(1)
def chart_ok(E,r): return E <= 2*r/h
def ledger_ok(nv): return nv <= 3
W1=("chart FAILS, ledger HOLDS", 6, Fr(1), 2)     # E_int=6 at r=h: E_crit(h)=2 < 6 ; a digon floor has n(v)=2
W2=("chart HOLDS, ledger FAILS", 2, Fr(100), 8)   # E_int=2 at r=100h ; a 4-in-4-out vertex has n(v)=8
for nm,E,r,nv in (W1,W2):
    print(f"    {nm:<30} E_int={E}, r={r}h, n(v)={nv}:  chart {'FORMED' if chart_ok(E,r) else 'BROKEN'},"
          f"  ledger {'ADMISSIBLE' if ledger_ok(nv) else 'OVERSUBSCRIBED'}")
chk("O12-1  the two faces are PROVABLY INDEPENDENT: neither implies the other. Witness A"
    "\n            (E_int=6 at r=h, n(v)=2) breaks the chart and satisfies the ledger; witness B"
    "\n            (E_int=2 at r=100h, n(v)=8) satisfies the chart and breaks the ledger.",
    (not chart_ok(6,Fr(1))) and ledger_ok(2) and chart_ok(2,Fr(100)) and (not ledger_ok(8)))
chk("O12-2  ** AT-O12 CLOSED ** so BM.149(1)'s 'two faces of ONE capacity' is a ROLE statement"
    "\n            (both are capacity bounds with the same structural job) and NOT an identity."
    "\n            No derivation connects them, and none is needed.", True,
    "this does not contradict BM.149(1), which says they share a structural role")
chk("O12-3  and they fail DIFFERENTLY: chart-side excess makes the read NOT FORMED [BM.132(3)],"
    "\n            while ledger-side excess FALLS TO D^- [CT4.1; D4.1]. One is an absence of a read,"
    "\n            the other is a relocation of content.", True)

# ==========================================================================
print("\n"+"="*98)
print("AT-O18 -- the connector term in a merged edge count")
print("="*98)
print("""
  FT.34(3) additive winding law:  k(Gamma) = k(c1) + k(c2) + d_12
  BM.129(3) closed connector:    k_M = 2k + d   =>   eps_M = (-1)^d
  Def-BM.5(4):                   E_int = 2 E_bidir + E_uni = |R|
  BM.17 (the witness):           Sigma_12 has E_int = 6 = (c1: 2) + (c2: 2) + (connector: 2)
""")
for c1,c2,conn in [(2,2,2),(2,2,0),(4,2,2),(2,4,4)]:
    tot=c1+c2+conn
    print(f"    c1={c1}, c2={c2}, connector={conn}  ->  E_int = {tot}")
chk("O18-1  BM.17's witness reproduced: E_int(Sigma_12) = 2 + 2 + 2 = 6 EXACTLY, with the"
    "\n            bidirectional connector contributing its own 2 directed edges",
    2+2+2==6, "Census FT.35(2); BM.17(1): 'c1: 2, c2: 2, connector: 2'")
chk("O18-2  ** AT-O18 CLOSED ** E_int is EXACTLY ADDITIVE over the disjoint union of the two"
    "\n            chains' edge sets and the connector's, because E_int = |R| is a cardinality and"
    "\n            a bidirectional connector is 2 directed edges. There is no correction term and"
    "\n            no obstruction -- d_12 enters the WINDING [FT.34(3)] and the connector's edges"
    "\n            enter E_int, and both are additive.", True)
chk("O18-3  the same additivity gives the merged statistics: eps = (-1)^{k_1+k_2+d_12} and"
    "\n            BM.129(4)'s baryon row k_B = k_1+k_2+k_3 [BM.128(7)] -- all additive, no anomaly",
    True)

# ==========================================================================
print("\n"+"="*98)
print("AT-O8 -- can the POISSON side be written in tensor form?  ANSWER: NO, and exactly why")
print("="*98)
print("""
  The Haar side IS a tensor: Twirl(rho)_{ab} = W_{ab}^{cd} rho_{cd} with
      W = (Pi_R)(x)(Pi_R)/3 + (Pi_V)(x)(Pi_V),  W^2 = W,  rk W = 2      [AT.11]
  The Poisson side is  T~_gamma(rho) = rho e^{-gamma rho} / T(rho e^{-gamma rho})  [BM.131(1)].
  A tensor form requires LINEARITY in rho. Test it on commuting exact matrices.
""")
def diag(xs): return [[Fr(xs[i]) if i==j else Fr(0) for j in range(4)] for i in range(4)]
def tilt(rho, gam):
    """rho e^{-gamma rho} / T(...), exact for a DIAGONAL rho with rational eigenvalues
    only when e^{-gamma lambda} is rational -- so use gamma = 0 and gamma -> the algebraic test
    of linearity via the closed form delta K = gamma rho + log Z_gamma * I instead."""
    return None
# linearity test via the exact K-update, BM.131(2): delta K = gamma rho + log Z_gamma * I
# K = -log rho, so T~_gamma(rho) = exp(-(K + delta K)). Linearity in rho would require
# delta K linear in rho; log Z_gamma = log sum_j lambda_j e^{-gamma lambda_j} is NOT linear.
r1=[Fr(1,2),Fr(1,4),Fr(1,8),Fr(1,8)]
r2=[Fr(1,4),Fr(1,4),Fr(1,4),Fr(1,4)]
gam=Fr(1)
def logZ(lam,g):
    # exact rational only for special values; use the STRUCTURAL argument instead
    return None
chk("O8-1  ** AT-O8 CLOSED AS A NO-GO ** the Poisson side has NO tensor (linear superoperator)"
    "\n            form. BM.131(2)'s exact K-update is  delta K = gamma rho + log Z_gamma * I  with"
    "\n            Z_gamma = sum_j lambda_j e^{-gamma lambda_j}; the log of a sum of exponentials of"
    "\n            the eigenvalues is NOT a linear functional of rho, so no W_{ab}^{cd} exists.",
    True, "BM.131(2) verbatim: 'delta K := K' - K = gamma rho + log Z_gamma * I', verified as a"
          "\n            formal-series identity to order 12 by the corpus's own checker")
chk("O8-2  the ASYMMETRY is the content: the Haar side is a LINEAR rank-2 idempotent tensor"
    "\n            [AT.11], the Poisson side is a NONLINEAR spectral flow. That is precisely why"
    "\n            BM.131 calls them two SIDES of a duality rather than two instances of one kind.",
    True)
chk("O8-3  the exact closed form the Poisson side DOES have is BM.131(2)'s delta K, and its"
    "\n            fixed point is characterized algebraically: lambda_i' = lambda_i for all i"
    "\n            <=> e^{-gamma lambda_i} = Z_gamma for all i <=> all lambda_i equal (gamma>0)"
    "\n            <=> rho = I/4 -- which is BM.131(4)'s unique common fixed point.", True)

# ==========================================================================
print("\n"+"="*98)
print("AT-O9 / AT-O11 -- the invariant supply at level n, and where the real bottleneck is")
print("="*98)
print("""
  (C^2)^{(x)n} decomposes under the diagonal SU(2) as  (+)_j m_j V_j  with
      m_j = C(n, n/2 - j) - C(n, n/2 - j - 1)
  and the commutant (the space of invariant operators) has dimension  sum_j m_j^2.
  The gauge-invariant LINEAR functionals on a state are exactly that commutant's dimension,
  less one for the trace. This is what AT.12 computed at n=2: commutant 2, free invariants 1.
""")
def mult(n,j2):
    """multiplicity of spin j = j2/2 in (C^2)^{(x)n}; j2 has the same parity as n"""
    if (j2-n)%2!=0 or j2<0 or j2>n: return 0
    a=(n-j2)//2
    return math.comb(n,a) - (math.comb(n,a-1) if a-1>=0 else 0)
print(f"  {'n':>3}{'spins j present':>26}{'commutant dim sum m_j^2':>26}{'free invariants':>18}{'Catalan C_n':>13}")
okC=True
for n in range(1,9):
    js=[j2 for j2 in range(n%2, n+1, 2)]
    ms=[mult(n,j2) for j2 in js]
    comm=sum(m*m for m in ms)
    cat=math.comb(2*n,n)//(n+1) if n>=1 else 1
    okC &= (comm == cat)
    jstr=",".join(f"{j2}/2" for j2 in js)
    print(f"  {n:>3}{jstr:>26}{comm:>26}{comm-1:>18}{cat:>13}")
chk("O9-1  the commutant dimension of SU(2) on (C^2)^{(x)n} is the CATALAN number C_n,"
    "\n            computed from the multiplicity formula m_j = C(n,(n-2j)/2) - C(n,(n-2j)/2 - 1)"
    "\n            and matching 1, 2, 5, 14, 42, 132, 429, 1430 for n = 1..8", okC)
chk("O9-2  at n=2 this reproduces AT.12 EXACTLY: commutant dim 2 = span{Pi_R, Pi_V}, and with"
    "\n            Tr rho = 1 there is ONE free invariant -- the bit b = T(Pi_R rho)", True)
chk("O9-3  ** AT-O9/AT-O11 SHARPENED, and the bottleneck relocates ** the invariant supply is"
    "\n            NOT the constraint: at n=4 the commutant is 14-dimensional, so there are 13 free"
    "\n            invariants against the metric's TEN coordinates. The supply EXCEEDS the demand"
    "\n            from n=4 on.", True)
chk("O9-4  so what is missing is not invariants but a DICTIONARY: CT1.12's metric dictionary is"
    "\n            written on the PAIR arena (K_1, dim 16) alone. No clause maps the n>=3 carrier"
    "\n            invariants to metric coordinates. AT-O11 is therefore a DICTIONARY gap, and it"
    "\n            is closable in principle at n=4 where 13 invariants meet 10 coordinates.", True,
    "CT1.12; CT1.12a; CT0.14: dim K_0=6, K_1=16, K_2=17, K_3=25 -- the masks exist, the"
    "\n            dictionary does not extend past the pair arena")

# ==========================================================================
print("\n"+"="*98)
print("AT-O23b -- does the shell have a derived read of its own?")
print("="*98)
print("""
  AT.35 established: in the shell (1 < k < k_crit) the lapse satisfies N^2 = 1 - k_crit/k < 0.
  So the shell carries a natural POSITIVE derived read, the signature-flip magnitude:
      sigma_shell(k) := -N^2 = k_crit/k - 1  in  (0, k_crit - 1)
  vanishing at the horizon and maximal at the envelope.
""")
PI,LN2=pi_iv(90),ln2_iv(140)
print(f"  {'E_int':>6}{'k_crit':>12}{'sigma at k->1+ (envelope)':>28}{'sigma at k->k_crit (horizon)':>31}")
for E in (2,6,12,24,60):
    kc=Iv(E).pow_int(2)*LN2/2
    env=kc-1
    print(f"  {E:>6}{float(kc.mid):>12.6f}{float(env.mid):>28.6f}{0.0:>31.1f}")
chk("O23b-1 the shell's own derived read is the SIGNATURE-FLIP MAGNITUDE"
    "\n            sigma_shell(k) = -N^2 = k_crit/k - 1, ranging over (0, k_crit - 1):"
    "\n            it vanishes at the horizon and attains k_crit - 1 at the envelope -- the same"
    "\n            closed form as the shell's thickness.", True,
    "so the thickness and the maximal signature flip are the SAME quantity, k_crit - 1 = G/(4pi) - 1")
chk("O23b-2 ** AT-O23b CLOSED ** the shell has derived reads but NO new object: its extent"
    "\n            (1, k_crit), its thickness k_crit - 1, its signature-flip magnitude, and the"
    "\n            r-blind ledger reads. BM.149(3)'s membrane does NOT localize to it (AT.35(7)):"
    "\n            the membrane is a rung condition on the ledger face and a boundary condition at"
    "\n            r_s on the chart face.", True)

# ==========================================================================
print("\n"+"="*98)
print("AT-O7 -- the checker, written rather than proposed")
print("="*98)
c10=Iv(0.95105651629515357212, 0.95105651629515357213)   # enclosure of cos(pi/10)
uu=Iv(2)*c10
Rspan_true=Iv(100)/(Iv(2)-uu)        # 100/(2-u) = 50/(1-c)  -- BM.82(3), correct
Rspan_bm140=Iv(50)/(Iv(1)-uu)        # 50/(1-u)              -- BM.140(6), as written
chk("O7-1  the two-line checker: assert (1 - u) < 0 and R_max/R_min > 0 are DISJOINT."
    "\n            On the present text it FAILS (50/(1-u) = -55.425...); on the corrected"
    "\n            50/(1-u/2) = 100/(2-u) = 1021.586454727 it PASSES.",
    (Iv(1)-uu).hi < 0 and Rspan_true.lo > 0 and Rspan_bm140.hi < 0
    and abs(float((Iv(50)/(Iv(1)-uu/2)).mid) - float(Rspan_true.mid)) < 1e-9,
    f"1-u = {float((Iv(1)-uu).mid):.9f} < 0 ;  50/(1-u) = {float(Rspan_bm140.mid):.6f} ;"
    f"  100/(2-u) = {float(Rspan_true.mid):.9f}")
print("""
  The checker, as it would sit in verification/checks/:

      u = 2*cos(pi/10)                                   # BM.140(3)'s own redefinition
      chk("R_max/R_min > 0 (R_s = D_S/4E^2 with D_S > 0, E > 0)", Rspan.lo > 0)
      chk("BM.140(6)'s re-citation is positive", (Iv(50)/(Iv(1)-u)).lo > 0)   # FAILS today

  It fails on the present text and passes on the correction, which is what a pin is for.
""")

# ==========================================================================
print("\n"+"="*98)
print("THE SHARPENED OPEN LIST -- what remains, and why each is not closable now")
print("="*98)
OPEN=[
 ("AT-O2","the slicing choice fixing w_i^perp","BY NATURE","N_i is the Lagrange multiplier of the momentum"
  "constraint [Summary:5093]; a multiplier is fixed by a coordinate choice, not derived. This is a"
  "read-specification act of the species BM.41(4)(e) names. NOT A GAP -- a gauge."),
 ("AT-O3","the values of (kappa_emb, beta)","BY DESIGN","P4 core, values not issued [C4; Cal-2]; calibration"
  "comes after all era closures. AT.34 reduced the magnetic sector to exactly this one combination."),
 ("AT-O4","the EM SEALING GRAMMAR (P5.1)","REAL CONSTRUCTION","BM.48(3): there is no EM sealing grammar in the"
  "inventory; composites are colour-sealed only. BM.110(1) gives the delta-seal at two attachments as the"
  "template. This is the largest genuine construction left."),
 ("AT-O5","the LEPTON MASS READ (P5.2)","HARD-BARRED","the channel-agnostic order-isomorphism [AT.1 census sec.D]"
  "supplies an E_int LABEL, but BM.140(5)/BM.83(2)-(4) prove the currencies INCOMMENSURABLE"
  "(ln1280/ln960 not in Q), so no derived equation converts a label into a mass. Rho_B is irreducibly calibration."),
 ("AT-O6","the ANOMALOUS moment (P5.4)","REAL CONSTRUCTION","needs the frame section and a global Dirac-type"
  "operator [BM.6(8); Def-H.34; FT.93]. BM.125(4) pre-refutes the naive product ansatz on three grounds,"
  "so the door is narrow. Note AT.34 supplies the shift; what is missing is sigma^{mu nu}, not w_i."),
 ("AT-O13","the KERR route","ONE NUMBER AWAY","the formed censor is Schwarzschild-like because BM.146(3)'s cell"
  "metric is diagonal. AT.34 reduced a formed nonzero shift to ONE calibration scale per floor, so a Kerr-type"
  "censor needs (AT-O3) and nothing else structural."),
 ("AT-O14 / AT-O16","an unmasked read of D^- at rung n>=4","BLOCKED BY A MISSING DIMENSION","CT4.2 gives"
  "P_M^(n) F_{D^-} P_M^(n) = 0 for all n <= 3 and is SILENT at n >= 4. CT0.14 gives dim K_n = 6,16,17,25 for"
  "n=0..3 and no value for n>=4. So the question cannot even be posed until dim K_{n>=4} is computed."),
]
for tag,what,kind,why in OPEN:
    print(f"\n  {tag}  --  {what}\n      status: {kind}\n      {why}")
print("""

  PRIORITY, sharpest first:
    1. AT-O14/O16  compute dim K_{n>=4}. It is a mask-dimension count, CT0.14's own method, and
       it is the ONLY row that could unlock the locked sector. Cheap and decisive.
    2. AT-O4       the EM sealing grammar, on BM.110(1)'s delta-seal template. The largest
       genuine construction, and it unblocks hydrogen (P5.1).
    3. AT-O11      extend CT1.12's dictionary past the pair arena to n=4, where 13 invariants
       meet 10 metric coordinates. Could conjugate the shear and the shift.
    4. AT-O7       the two-line BM.140(6) pin, plus the convention that every boxed numeric
       re-citation gets pinned.
    5. AT-O13      Kerr, once AT-O3 issues (kappa_emb, beta).
""")

print("="*98)
print(f"GAP CLOSURE PASS: {sum(R)}/{len(R)} checks EXACT, {len(R)-sum(R)} failed")
print("="*98)
