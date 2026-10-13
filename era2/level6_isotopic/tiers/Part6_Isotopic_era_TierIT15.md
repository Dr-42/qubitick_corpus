# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.15: the capacity-bound calibration matrix — the parametric ion fills audited, the "relative flux" and "crystallization cost" refuted, and the Scenario-B verdict

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.15 — the Architect's directive to audit the
4×4 tensor object $M_4=M\otimes M$ under the parametric ion fills ($m_L(N)=2N u$,
$\rho_{\mathrm B}(N)=\rho_0N$, $\varepsilon_q(n_e)=\varepsilon_0 n_e$, $m_S(n_e)=m_0n_e$, plus the
decorative $\mu_{\mathrm B}$, $\sigma_e$ fills), the claimed "relative information flux"
renormalization $\rho_{\mathrm B}\varepsilon_q/(m_Lm_S)$, the "crystallization cost" eigenvalue story,
and the re-visited photon/observer derivative asymmetry — and to adjudicate Scenario A
(reconciliation) against Scenario B (refutation). The tier verifies the exact algebra the directive
gets right, identifies the fills' one derived kernel (the integer skeleton $E_{\mathrm{int}}=2N$) and
its currency substitution, refutes the three structural claims on existing rows, and adjudicates the
object **Scenario B — refuted; NOT adopted.**
**Tags.** IT.46–IT.48. **Pattern.** the adjudication tiers (IT.9/IT.12/IT.14's shape), premise audit
logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays
empty; no clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.1–IT.14 is modified
[AT.63(2)]. **The ion-fill family is recorded as a parametric subclass of IT.37–IT.39/IT.43–IT.45's
construction class — NOT a derived row, and NOT adopted.** An erratum to Tier IT.14's checker
(BM.137(1)'s $u=4\varepsilon_q$ encoded at the $\mathcal B_{\mathrm{ens}}$ locus; verdict-neutral,
re-run 19/19 green) is recorded at IT.48(6).
**Machine.** `era2/level6_isotopic/checks/ion_fill_matrix.py` → **13/13 exact** (multivariate Laurent
polynomials over Gauss(i) over `Fraction`; formal partial derivatives; Faddeev–LeVerrier
characteristic polynomials over the polynomial ring, independently sanity-certified on
$\mathrm{diag}(1,2,3,4)\mapsto\lambda^4{-}10\lambda^3{+}35\lambda^2{-}50\lambda{+}24$ and on a
nilpotent witness $\mapsto\lambda^4$; integer/binomial censuses); `run_all_level6.py` → **16
checkers, 243 exact markers, 0 failures**; `check_level6_format.py` → the gate over all fifteen
Part 6 documents. Exact arithmetic: integer and `Fraction` exponents only, no floating point.
**No floating point in any assertion. No measured value enters any clause [P5] — every fill slot
stays symbolic; the species labels ("H+", "H", "H−", "He2+", "He+", "He") stay QUOTED parametric
fill labels, $\neg$species identifications [Def-BM.3(1,(7))]. No smooth-manifold analogy — the
partial derivatives are FORMAL polynomial operations, $\neg$analysis; the "cost/flux/acceleration"
language is audited, not imported. Prices are $\neg$masses [HistLog §V.32].**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13k): *"Audit the 4x4 Capacity-Bound Calibration
Matrix, the Parametric Ion Fills, and the 'Relative Information Flux' Renormalization … $M_4=M\otimes M$
(dimension 16, matching the capacity bound $C_{\mathrm{cap}}=16$), filled parametrically with varying
amounts of baryonic ($N$) and leptonic ($n_e$) data for specific ions … the dimensional tension is
resolved by the ratio $\rho_{\mathrm B}\varepsilon_q/(m_Lm_S)$ (interface cost vs self-cost), which is
dimensionless … the cost of crystallizing a qubit is the eigenvalue structure for single-node vs
multi-node systems … Scenario A (reconciliation) or Scenario B (refutation). Be brutally honest: if
the 'relative flux' is just a disguised cross-currency sum, say so."* Executed: the algebra verified
exact where the directive is right, seven premise corrections logged at IT.48(4), the verdict
Scenario B.

---

### IT.46 — The parametric fills audited: the real skeleton, the currency substitution, and the seven contradictions

**Thm.**
$$(1)\quad\textbf{THE ONE DERIVED KERNEL — THE INTEGER SKELETON:}\qquad E_{\mathrm{int}}^{\mathrm{disjoint}}=6(k{+}1),\ \ N=3(k{+}1)\ \ [\mathrm{IT.6}(1);\ \mathrm{IT.7}]\ \ \Rightarrow\ \ \boxed{\ E_{\mathrm{int}}=2N\ \ \text{exactly (integer census}\ k{=}0..12)\ }$$
$$\therefore\ \ m_L^{\mathrm{derived}}=E_{\mathrm{int}}\ln2/\mathfrak h=2N\cdot(\ln2/\mathfrak h)\ \ [\mathrm{FT.44}(4)];\qquad \text{the fill}\ \ m_L(N)=2N\cdot u\ \ \text{KEEPS the skeleton and SWAPS the scale factor:}$$
$$\ln2/\mathfrak h\ \ (\text{alphabet}\ \{\mathfrak h,\ln2\},\ \ \deg=\mathfrak q^{1/2})\ \ \longrightarrow\ \ u=4\varepsilon_q\ \ (\text{alphabet}\ \{\varepsilon_q\},\ \ \deg=\mathfrak q^0)\ \ [\mathrm{BM.137}(1):\ u:=1-p=4\varepsilon_q;\ \mathrm{BM.83}(4)\ \text{exponent arithmetic}]\ \ \textbf{— a currency substitution inside a derived name}$$
$$(2)\quad\textbf{THE FRAGMENT IDENTIFICATION:}\qquad \mathcal B_{\mathrm{ens}}^{(n)}=-\,\frac{2n\,u\,D_{n-1}}{D_n}\cdot\frac{\ln2}{\mathfrak h}\le0,\quad D_n=1{+}u{+}\cdots{+}u^{n-1}\ \ [\mathrm{BM.137}(1),(3);\ \text{norm-layer}\ [\mathrm{IT.34}(1);\ \mathrm{Def\text{-}H.32}(6);\ \mathrm{BM.21}(2)]]:$$
$$\text{the hinge identity}\ \ D_n-1=uD_{n-1}\ \ \text{verified as a polynomial identity for}\ n=2,3,4\ \ [\text{machine}];\qquad \boxed{\ \text{the fill's}\ m_L=2N u\ \text{is the binding's NUMERATOR FRAGMENT — sign flipped,}\ D\text{-ratio stripped, norm-layer scale}\ \ln2/\mathfrak h\ \text{stripped}\ }$$
$$\text{exact rational witness at}\ \varepsilon_q=\tfrac1{16}\ (u{=}\tfrac14):\ \ 2nu|_{n=2}=+1>0\ \ \text{vs}\ \ \mathcal B_{\mathrm{ens}}^{(2)}\mathfrak h/\ln2=-\tfrac45<0\ \ [\text{machine}]:\ \ \textbf{binding is}\ \neg\textbf{mass}\ [\mathrm{FT.79}(5);\ \mathrm{IT.34}(1);\ \text{HistLog}\ \S\mathrm{V.32}]$$
$$(3)\quad\textbf{THE FILL-CONTRADICTION CENSUS (machine):}\qquad\begin{array}{l|l|l}\textbf{the fill}&\textbf{the derived row it names}&\textbf{the contradiction}\\\hline\rho_{\mathrm B}(N)=\rho_0N&\rho_{\mathrm B}=\hat\mu'^2\mathfrak h^2/(\ln2)^2\ \ [\mathrm{BM.83}(4)]&\text{the derived}\ \rho_{\mathrm B}\ \text{is}\ N\text{-INDEPENDENT (formal partial}\ 0)\\\varepsilon_q(n_e)=\varepsilon_0n_e&\varepsilon_q\ \text{ONE global A4 slot}\ [\mathrm{BM.19}(2);\ \mathrm{D0.4};\ \mathrm{IT.4}(2)]&\text{THREE values}\ (0,\varepsilon_0,2\varepsilon_0)\ \text{of one global slot; bare nuclei pinned to}\ \varepsilon_q{=}0\ \text{as a LAW}\ [\mathrm{BM.19}(3)]\\\sigma_e(n_e)=\sigma_0n_e&\sigma_e\in\{-1,{+}1\}\ \text{the registration sign}\ [\mathrm{CT0.9};\ \mathrm{IT.1}(3)(\mathrm R1)]&\text{the fill's value at}\ n_e{=}0\ \text{is}\ 0\ \text{— outside the derived value census}\\\mu_{\mathrm B}(N)=\mu_0N&\mathrm{BM.83}(4)\ \text{'s identity}&\text{forces}\ \rho_0=\mu_0\mathfrak h^2/(\ln2)^2\ \text{— a constraint between ``independent'' slots}\\\mu_{\mathrm B},\ \sigma_e&\text{—}&\textbf{decorative:}\ \mathrm{alph}(M_4^{\mathrm{fill}})=\{N,n_e,\rho_0,\varepsilon_0,m_0\}\ \ [\text{machine}]\\\text{the domain}&\varepsilon_q\in[0,\tfrac14)\ \ [\mathrm{CT0.8}]&\text{at}\ n_e{=}2:\ \ \varepsilon_0<\tfrac18\ \text{EXACTLY — strictly below AT-O27's distinguished}\ \tfrac18\end{array}$$
$$(4)\quad\textbf{THE ION TABLE vs THE DERIVED N-LADDER:}\qquad N=3\ \text{per nucleon}\ [\mathrm{IT.6}(1):\ N{=}3(k{+}1)\ \text{for 1p-}k\text{n};\ \mathrm{IT.12}(1):\ \text{the}\ N{=}9\ \text{doublet}=\text{the two 3-nucleon species}]:\ \ (N,\text{nucleons})=(3,1),(6,2),(9,3),(12,4):$$
$$\text{the quoted ``He2+'' at}\ N{=}6\ \text{is a TWO-nucleon configuration class}\ (g(6){=}25\ [\mathrm{IT.9}(2)];\ \ \text{the}\ Q{=}{+}2\ \text{charge class exists:}\ W_6({+}2)=\binom{12}8=495,\ \ \textstyle\sum_QW_6(Q)=4096\ [\mathrm{IT.9}(1)]),$$
$$\text{while the 4-nucleon ``He-4'' system sits at}\ A{=}4,\ N{=}12\ \ [\mathrm{IT.31}(4),(5):\ \varepsilon{=}(-1)^A{=}{+}1;\ g(12){=}164395];\qquad \text{labels stay quoted}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(1,(7))],\ \ \text{but the label-to-}N\ \text{map contradicts the ladder};$$
$$\boxed{\ n_e\ \textbf{has no derived standing:}\ \ \text{the electron-saturated members are}\ \neg\text{constructed — the exception row is ``to be derived,}\ \neg\text{assumed, at its own locus''}\ [\mathrm{IT.8}(3);\ \mathrm{IT.2}\ \text{'s status row}]\ }$$
$$(5)\quad\textbf{THE}\ \mathfrak q\textbf{-DILEMMA (two horns, both machine-exact):}\qquad \text{HORN 1 (keep the derived names):}\ \ \deg(\rho_{\mathrm B}\varepsilon_q)-\deg(m_Lm_S)=0-1=-1:$$
$$\boxed{\ \text{the ratio is}\ \mathfrak q^{-1},\ \ \textbf{NOT dimensionless — the directive's claim is FALSE by BM.83(4)'s exponent arithmetic};\qquad \det/(m_Lm_S)=1-\text{ratio is inhomogeneous}\ \{0,-1\}\ }$$
$$\text{HORN 2 (keep the fills): every entry becomes}\ \mathfrak q^0\ \text{— ``homogeneous'', but}\ \deg(m_L^{\mathrm{derived}})=\tfrac12\ne0=\deg(\text{fill}):\ \ \textbf{no entry of the ``mass matrix'' carries mass};$$
$$\text{unfilled,}\ M_4\ \text{'s entries span THREE degrees}\ \{0,\tfrac12,1\}\ [\mathrm{IT.43}(3)\ \text{extended}]:\ \ \text{the tensor product SPREADS the mismatch, it does not cure it}$$
$$(6)\quad\textbf{THE TWO SIXTEENS ARE NUMEROLOGY:}\qquad C_{\mathrm{cap}}=16=D_{\mathrm{tick}}(3)=2^{3+1}\ \ (\text{the junction capacity; the lock biconditional}\ 2^{n+1}{>}16\iff n\ge4\iff\neg\text{admissible re-censused}\ n{=}0..6)\ \ [\mathrm{CT0.6};\ \mathrm{CT0.12};\ \mathrm{CT0.13};\ \mathrm{IT.1}(1)]$$
$$\text{vs}\ \ \dim\mathrm{End}(\mathbb C^4)=4^2=16\ \ (\text{an entry count}):\ \ \neg\exists\ \text{a derived row connecting them}\ [\mathrm{BM.134}(5)\ \text{discipline};\ \mathrm{IT.44}(3)\ \text{pattern}];\qquad \mathrm{IT.38}(2)\ \text{'s 16-vs-8 force-algebra over-count carries over}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived (re-produced):}\ (1)\ \text{'s skeleton};\qquad\textbf{adjudicated:}\ (2)\text{--}(6);\qquad\textbf{parametric:}\ \rho_0,\varepsilon_0,m_0,\mu_0,\sigma_0\ \text{are five NEW undeclared slots}\ [\mathrm{BM.6}(4)],\ \neg\text{declarations};$$
$$\neg\text{a measured value}\ [\mathrm{P5}],\qquad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)]$$

**Req.** P4, P5, A4, D0.4, CT0.6, CT0.8, CT0.9, CT0.12, CT0.13 (Parts 1–2); Def-H.32(6), FT.44(4), FT.79(5) (Part 3); IT.1(1),(3), IT.2(4), IT.4(2), IT.6(1), IT.7, IT.8(3), IT.9(1),(2), IT.12(1), IT.14(2), IT.31(4),(5), IT.34(1), IT.38(2), IT.43(3), IT.44(3), AT-O27 (this level); AT.41(3), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.5(5), BM.6(4), BM.19(2),(3), BM.21(2), BM.83(4), BM.122(3), BM.134(5), BM.137(1),(2),(3) (Part 4); integer/binomial censuses, formal partials, polynomial identities [math; machine: `ion_fill_matrix.py` §§A–B, 7/7].

**Pf.**
$$(1):\ \text{the integer census}\ 6(k{+}1)=2\cdot3(k{+}1)\ \text{for}\ k{=}0..12;\ \text{the scale factors' degree+alphabet comparison}\ [\text{machine B1}];\ \ (2):\ D_n-1=uD_{n-1}\ \text{for}\ n{=}2,3,4;\ \text{the exact rational sign witness at}\ \varepsilon_q{=}\tfrac1{16}\ \ [\text{machine B2}];$$
$$(3):\ \text{the formal partials, the ion-table value census, the}\ \sigma_e\text{-at-}n_e{=}0\ \text{evaluation, the monomial non-identity, the}\ M_4^{\mathrm{fill}}\ \text{alphabet, and the exact rational domain bound}\ [\text{machine B3}];\ \ (4):\ \text{the ladder census and the binomials}\ \binom{12}8{=}495,\ 2^{12}{=}4096\ \ [\text{machine B4}];$$
$$(5):\ \text{the degree censuses on both horns}\ [\text{machine A1, A2}];\ \ (6):\ \text{the lock biconditional over}\ n{=}0..6\ \text{and}\ 2^4{=}4^2{=}16\ \ [\text{machine A3}].\ \blacksquare$$

**Phys.** The fills arrive dressed in the corpus's own names, and the audit undresses them one joint
at a time. The integer skeleton is real: the disjoint internal energy of the isotopic family is
exactly twice the attachment count, and that is the only piece of the fill the ledger already owns.
At every scale joint the fill then swaps currency — the shared ln2 over h that makes the
informational mass a mass is replaced by the flicker weight u, which is exactly the numerator of the
formed ensemble binding, a norm-layer read that is never positive. The named slots get laws the
derived rows contradict: the pole restatement is fixed, not linear in N; the flicker threshold is
one global number, not an ion-indexed family that pins every bare nucleus to the sharp
crystallization point; the registration sign is binary and the fill hands it zero. Two of the five
new parameters never even enter the matrix, and a third identity quietly constrains the other two.
The ion labels stay quoted, as they must, but the ladder behind them is derived, and on that ladder
the six-attachment systems are two-nucleon configurations while anything deserving the helium quote
lives at twelve. None of this is a verdict against building — it is the ledger saying, precisely,
which parts of the building are its own.

---

### IT.47 — The "relative information flux" and the "crystallization cost": unformed, circular, and blind

**Thm.**
$$(1)\quad\textbf{THE RATIO IS NOT A FORMED READ:}\qquad \mathrm{BM.83}(5)\ \text{'s localization theorem enumerates EVERY formed cross-currency mass ratio and proves each depends on exactly}\ (\rho_{\mathrm B},\sigma_\ell,\sigma_\nu)\ \text{``and in no others''}:$$
$$\text{machine:}\ \ \varepsilon_q\ \text{appears in NONE of the three formed-ratio slot-sets}\ \ \{E,\sigma_\ell,z^{(\ell)}\},\ \ \{\sigma_\nu,\sigma_\ell\},\ \ \{E,\sigma_\ell,z^{(\ell)},\rho_{\mathrm B},\mathcal R_s\}\ \ [\mathrm{IT.4}(2),(4):\ \text{the atomic ladder fixes lepton slots only}];$$
$$\boxed{\ \frac{\rho_{\mathrm B}\varepsilon_q}{m_Lm_S}\ \ \text{is formable ONLY as a SYMBOLIC expression carrying undeclared slots}\ \ [\mathrm{IT.4}(3)\ \text{'s reduced-mass doctrine}]\ \ —\ \ \neg\text{a formed read,}\ \neg\text{a value pre-calibration}\ \ [\mathrm{IT.4}(2)]\ }$$
$$(2)\quad\textbf{THE NAMING HAS NO LEDGER PRIMITIVE:}\qquad \text{the ledger's information reads are}\ \ I_{\mathrm{hid}}\in\mathbb Z\cdot\ln2\ \ [\mathrm{IT.2}(4)]\ \ \text{and the integer prices}\ [\text{HistLog}\ \S\mathrm{V.32}];$$
$$\text{``interface cost / self-cost / relative information flux'' maps to none of them};\qquad \text{the only ``flux'' on record is}\ \mathrm{IT.14}(2)\ \text{'s adopted CURVATURE-FLUX}\ Q\text{-value read — a different object (name collision flagged)}$$
$$(3)\quad\textbf{THE CRYSTALLIZATION COST IS CIRCULAR AND N-BLIND (machine):}\qquad \text{at}\ n_e{=}0\ \text{the fill gives}\ \varepsilon_q{=}0\Rightarrow u{=}0\Rightarrow m_L{=}m_S{=}0:\ \ M=\begin{pmatrix}0&\rho_0N\\0&0\end{pmatrix}\ \ \text{is NILPOTENT}\ (M^2{=}0\ \text{symbolically}):$$
$$\text{charpoly}(M_4)=\lambda^4\ \ \text{EXACTLY (Faddeev–LeVerrier over the polynomial ring) — IDENTICALLY for the quoted ``H+''}\ (N{=}3)\ \text{and ``He2+''}\ (N{=}6):\ \ \textbf{the characteristic polynomial carries no}\ N\ \textbf{at all};$$
$$\boxed{\ \text{the ``single-node cost'' cannot see the only baryon datum — a read that cannot fail carries no information}\ }\qquad\text{at}\ n_e{=}1:\ \ \mathrm{tr}\,M=8N\varepsilon_0{+}m_0,\ \ \det M=N\varepsilon_0(8m_0{-}\rho_0),\ \ \mathrm{tr}(M_4){=}(\mathrm{tr}\,M)^2,\ \ \det(M_4){=}(\det M)^4\ \ [\text{machine}]:$$
$$\text{the entire ``bare nucleus vs neutral atom'' spectral contrast is the fill's own law}\ \varepsilon_q{=}\varepsilon_0n_e\ \text{zeroing}\ u\ \text{at}\ n_e{=}0,\ \ \textbf{READ BACK as a spectrum}$$
$$(4)\quad\textbf{CRYSTALLIZATION NEEDS NO EIGENVALUE STORY — IT IS ALREADY DERIVED:}\qquad \varepsilon_q{=}0\Rightarrow x_-{=}0\Rightarrow\neg\text{a dissolution move}\Rightarrow\text{the crystallized configuration}\ [\mathrm{BM.19}(3);\ \mathrm{Def\text{-}BM.5}(5)];$$
$$\mathcal W_{\text{channel}}=1\iff\varepsilon_q{=}0\ \wedge\ NE\ge\mathcal T_0\ \ [\mathrm{BM.122}(3)];\qquad P_{\mathrm{mat}}(E{=}4){=}1,\ \ w_{\mathrm{mat}}^{(2)}{=}1\ \ \text{at the no-flicker collapse}\ [\mathrm{BM.137}(2)];\qquad \text{the Born-width distribution sharpens at zero flicker}\ [\mathrm{IT.3}\ \text{'s record}]$$
$$(5)\quad\textbf{THE PROPOSED Def-H.32 MAPPING IS THE ADJUDICATED ILL-POSED FORM:}\qquad \text{the configuration sum is}\ (q,S)\text{-SECTORED}\ [\mathrm{Def\text{-}H.32}(5);\ \mathrm{IT.26}];\ \ \text{the colour grouping is an INDEPENDENT register}\ [\mathrm{AT.41}(3)]:$$
$$\text{``amplitudes over grouping sectors'' is ill-posed}\ [\mathrm{IT.26};\ \mathrm{IT.27}(3)];\qquad \mathrm{IT\text{-}O2}\ \text{'s binding VALUE needs the three named constructions}\ [\mathrm{IT.27}(2)]\ \text{— none supplied by a parametric}\ 4\times4;$$
$$\boxed{\ \text{eigenvalue-splitting-as-binding-energy is the smooth-manifold mass-matrix story the bars exclude}\ [\mathrm{FT.79}(5):\ \text{amplitude}\ne\text{mass};\ \mathrm{IT.34}(1):\ \text{the binding is norm-layer};\ \mathrm{IT.39}(2):\ \text{the statistics is the exchange sign,}\ \neg\text{an eigenvalue}]\ }$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived (re-produced):}\ (4);\qquad\textbf{adjudicated:}\ (1),(2),(3),(5);\qquad\neg\text{a declaration},\ \ \neg\text{a measured value}\ [\mathrm{P5}],\ \ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))]$$

**Req.** P5, CT0.9 (Parts 1–2); Def-H.32(5), FT.79(5) (Part 3); IT.2(4), IT.3, IT.4(2),(3),(4), IT.14(2), IT.26, IT.27(2),(3), IT.34(1), IT.39(2), IT.43(3),(4),(6), IT-O2 (this level); AT.41(3), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.5(5), BM.19(3), BM.83(5), BM.122(3), BM.134(5), BM.137(2), BM.140(5) (Part 4); Faddeev–LeVerrier over the polynomial ring, symbolic nilpotency, exact spectral identities [math; machine: `ion_fill_matrix.py` §C, 3/3].

**Pf.**
$$(1):\ \text{the three formed-ratio slot-sets of}\ \mathrm{BM.83}(5)\ \text{encoded and censused against}\ \varepsilon_q\ \ [\text{machine C1}];\ \ (2):\ \text{record row on the cited clauses};$$
$$(3):\ M^2{=}0\ \text{symbolically;}\ \text{charpoly}(M_4){=}\lambda^4\ \text{by Faddeev–LeVerrier with all four trailing coefficients zero and}\ N\text{-free; the}\ n_e{=}1\ \text{trace/determinant forms and the Kronecker spectral identities}\ \mathrm{tr}(M_4){=}(\mathrm{tr}M)^2,\ \det(M_4){=}(\det M)^4\ \text{verified on the filled matrix}\ [\text{machine C2, C3}];\ \ (4),(5),(6):\ \text{rows re-cited from the frozen loci}.\ \blacksquare$$

**Phys.** The renormalization offer was a ratio, and a ratio is the right shape — BM.83(5) itself
forms cross-currency ratios as symbolic expressions. But the formed ones are a closed census: three
families, localized to three undeclared numbers, and the flicker threshold is not among them,
because no formed cross-currency ratio has ever carried it. What the ratio buys instead is a name —
"interface cost against self-cost" — and names are not reads; the ledger's information is counted in
integer multiples of ln2 and priced in integers, and the only flux on record is the curvature-flux
Q-value of the N=9 transition. The cost story collapses on contact with the fill's own algebra: at
zero leptonic fill the matrix is nilpotent, its characteristic polynomial is the fourth power of
lambda, and it says exactly the same thing for the three-attachment and six-attachment bare nuclei —
a read blind to the only baryon datum it was built to weigh. The contrast with the neutral atom is
real arithmetic and empty content: it is the stipulated law epsilon-q equals epsilon-zero times n-e,
differentiated nowhere, evaluated at zero, and read back as a spectrum. Crystallization, meanwhile,
needed none of this: the ledger already proves that zero flicker means zero dissolution, certain
pair creation above threshold, and a fully collapsed materialization measure — three exact rows, no
eigenvalues, no costs, no flux.

---

### IT.48 — The derivative verdict re-visited, the verdict, and the declaration census

**Thm.**
$$(1)\quad\textbf{THE INDEPENDENCE PERSISTS THROUGH THE FILL:}\qquad \text{on the fill's own algebra}\ N,n_e\ \text{remain independent counters and}\ \rho_0,\varepsilon_0\ \text{independent slots:}$$
$$\frac{\partial\rho_{\mathrm B}^{\mathrm{fill}}}{\partial\varepsilon_0}=\frac{\partial\rho_{\mathrm B}^{\mathrm{fill}}}{\partial n_e}=\frac{\partial\rho_{\mathrm B}^{\mathrm{fill}}}{\partial m_0}=0,\qquad \frac{\partial\varepsilon_q^{\mathrm{fill}}}{\partial\rho_0}=\frac{\partial\varepsilon_q^{\mathrm{fill}}}{\partial N}=0\qquad[\text{machine: formal partials}]\ \ —\ \ \mathrm{IT.44}(5),(6)\ \text{'s symmetric independence is UNTOUCHED}$$
$$(2)\quad\textbf{BUT THE FILL SMUGGLES THE DECLARATION IT NEEDS:}\qquad m_L^{\mathrm{fill}}=2Nu=8N\varepsilon_0n_e:\qquad \frac{\partial m_L^{\mathrm{fill}}}{\partial\varepsilon_0}=8Nn_e\ne0,\qquad \frac{\partial m_L^{\mathrm{fill}}}{\partial n_e}=8N\varepsilon_0\ne0\ \ [\text{machine}]:$$
$$\boxed{\ \text{the fill MANUFACTURES a baryon-named read that depends on the lepton slot — a stipulated cross-currency functional LAW: exactly the declared conversion}\ \mathrm{BM.140}(5)\ \text{bars (``no derived equation converts them''), the door}\ \mathrm{IT.45}(5)(\mathrm{ii})\ \text{named as owed}\ [\mathrm{BM.6}(4)]\ \text{— none issued}\ }$$
$$\textbf{the fill does not DISCOVER the asymmetry; it ASSUMES it}\ \ —\ \ \text{the photon/observer verdict of Tier IT.14 stands unchanged}$$
$$(3)\quad\textbf{THE ``CONSTANT ACCELERATION'' IS CORRECT FORMAL CALCULUS AND VACUOUS:}\qquad \Sigma:=\rho_{\mathrm B}{+}\varepsilon_q,\ \ \Delta:=\rho_{\mathrm B}{-}\varepsilon_q\ \ (\text{a formal linear change of variables}):$$
$$S_{14}=\tfrac12(\rho_{\mathrm B}^2{+}\varepsilon_q^2)=\tfrac14(\Sigma^2{+}\Delta^2),\qquad \frac{\partial S_{14}}{\partial\Delta}=\frac\Delta2,\qquad \frac{\partial^2S_{14}}{\partial\Delta^2}=\frac12\qquad[\text{machine: the directive's identities verified exactly}];$$
$$\text{the witness:}\ \ T_{14}=\tfrac12(\rho_{\mathrm B}^2{-}\varepsilon_q^2)=\tfrac12\Sigma\Delta\ \ \Rightarrow\ \ \frac{\partial^2T_{14}}{\partial\Delta^2}=0\ \ [\text{machine}]:\ \ \text{the ``acceleration'' measures the quadratic form's normalization in adapted coordinates,}\ \neg\text{a ledger property};$$
$$S_{14}\ \text{remains a cross-currency SUM under every fill}\ [\mathrm{IT.43}(4),(6)]:\ \ \textbf{the bar is inherited by every derivative read of it}$$
$$(4)\quad\textbf{THE VERDICT — SCENARIO B (REFUTATION); the seven premise corrections:}\qquad\begin{array}{l|l}\textbf{premise}&\textbf{the correction}\\\hline(\mathrm P1)&\text{the}\ \mathfrak q\text{-tension is RELABELED, not resolved: the ratio is}\ \mathfrak q^{-1}\ \text{under the derived degrees; the fills homogenize only by stripping the mass reads of their mass}\ [\mathrm{IT.46}(5)]\\(\mathrm P2)&\text{the ratio is unformed:}\ \mathrm{BM.83}(5)\ \text{'s localization census is closed and}\ \varepsilon_q\ \text{enters no formed cross-currency ratio}\ [\mathrm{IT.47}(1)]\\(\mathrm P3)&\text{the fills contradict the derived forms they name}\ (\rho_{\mathrm B}\ N\text{-independence;}\ \varepsilon_q\ \text{global};\ \sigma_e\ \text{binary)}\ [\mathrm{IT.46}(3)]\\(\mathrm P4)&\text{the ion table's}\ N\text{-assignments contradict the ladder}\ (N{=}6\ \text{is two-nucleon; ``He-4'' lives at}\ N{=}12);\ \ n_e\ \text{has no derived standing}\ [\mathrm{IT.46}(4)]\\(\mathrm P5)&\text{the crystallization cost is circular and}\ N\text{-blind (the nilpotent artifact); crystallization is already derived without eigenvalues}\ [\mathrm{IT.47}(3),(4)]\\(\mathrm P6)&\text{the derivative asymmetry stays refuted — and the fill smuggles the conversion it needs}\ [\mathrm{IT.48}(1),(2)]\\(\mathrm P7)&C_{\mathrm{cap}}{=}16\ \text{vs}\ 4^2{=}16\ \text{is numerology;}\ \mu_{\mathrm B},\sigma_e\ \text{are decorative; five new slots are undeclared}\ [\mathrm{IT.46}(3),(6)]\end{array}$$
$$\boxed{\ \textbf{NOT ADOPTED.}\ \ \text{The ion-fill family is a parametric subclass of IT.37--IT.39/IT.43--IT.45's construction class; no declaration issues;}\ \S\mathrm{Cal\text{-}IT}\ \text{stays empty; NO new open row}\ }$$
$$(5)\quad\textbf{the declared door (recorded,}\ \neg\textbf{issued):}\qquad \text{ion-indexed calibration data is the Calibration Era's program:}\ \ \text{the necessary data species is multi-seal EM-bound spectroscopy}\ [\mathrm{IT.5}(2)],\ \ \text{the anchor is a STRATEGY}\ [\mathrm{IT.33}],\ \ \text{the era stays deferred}\ [\mathrm{AT.63}(4)]:$$
$$\text{values enter by DECLARED reads under the read rules}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ \ [\mathrm{AT.54}(6)]\ \ —\ \ \neg\text{by parametric-matrix eigenvalues};\qquad \text{the owed declarations}\ \mathrm{IT.45}(5)\ \text{named stand: a mass}^2\ \text{scale, a}\ \rho_{\mathrm B}(\varepsilon_q)\text{-type link (the bar itself), the 8-dim force-algebra restriction}$$
$(6)\quad\textbf{the erratum and the machine state:}\qquad \text{Tier IT.14's checker encoded the}\ \mathcal B_{\mathrm{ens}}\ \text{locus with the round-trip weight}\ x_+x_-=4\varepsilon_q(1{-}4\varepsilon_q)\ [\mathrm{BM.122}(3)]\ \text{instead of}\ \mathrm{BM.137}(1)\ \text{'s}\ u=4\varepsilon_q:\ \ \textbf{verdict-neutral}\ \text{(the censuses there are alphabet-level;}\ \varepsilon_q\ \text{is the only flicker symbol in either form), fixed in its own commit, re-run 19/19 green BEFORE any new content (the house discipline)};$
$$\texttt{ion\_fill\_matrix.py}\to\textbf{13/13 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{16 checkers, 243 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{15 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad \text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no new object is adopted}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P4, P5 (Parts 1–2); FT.79(5) (Part 3); IT.5(2), IT.26, IT.33, IT.43(4),(6), IT.44(3),(5),(6), IT.45(5), IT.46, IT.47, IT-O2 (this level); AT.39(8), AT.54(6), AT.63(2),(4) (Level 5); BM.6(4), BM.83(4),(5), BM.122(3), BM.134(5), BM.137(1), BM.140(5), Def-BM.3(1),(7) (Parts 2, 4); formal partial derivatives over the fill algebra, the adapted-coordinate identities [math; machine: `ion_fill_matrix.py` §D, 3/3].

**Pf.**
$$(1),(2):\ \text{the formal partials of the filled}\ \rho_{\mathrm B},\varepsilon_q,m_L\ \text{computed in the polynomial ring — the vanishing census and the two nonzero partials}\ [\text{machine D1+D2}];\ \ (3):\ \text{the linear change of variables applied symbolically; both second-derivative identities}\ [\text{machine D3}];$$
$$(4)\text{--}(7):\ \text{the verdict assembled from}\ \mathrm{IT.46}(3),(4),(5),(6)\ \text{and}\ \mathrm{IT.47}(1),(3),(4);\ \text{the erratum re-run recorded; the runner and the gate re-run end to end. No new mathematics is introduced at}\ (5)\text{--}(7).\ \blacksquare$$

**Phys.** The re-visited asymmetry gets the shortest answer of the three claims, and the sharpest.
The fill was supposed to manufacture the dependence the ledger refuses to derive — and it does
manufacture one, but in the wrong place and in the wrong direction: not the pole slot responding to
the flicker, but the mass name responding to both counters, because the fill defined it that way.
That is not a discovery; it is the barred conversion written into a definition, the one act the
incommensurability row forbids and no declaration has authorized. The second-derivative identities
are true — they are two lines of calculus on a quadratic form — and they are empty: the same
computation on the antisymmetric partner returns zero, so the "constant acceleration" is a property
of the coordinates chosen, not of the world. What remains after the audit is one honest integer
fact, E_int = 2N, which the family census already owned, standing inside a parametric shell of five
undeclared slots, two decorative ones, a contradictory ion table, a ratio outside the closed
localization census, and a nilpotent spectrum that cannot tell a bare three from a bare six. The
tier records all of it, adopts none of it, and leaves the door where the level left it: the
calibration era, when it comes, will take its ion data through declared reads — not through the
eigenvalues of a matrix built to order.

---

## §Cal-IT — unchanged from Tier IT.15

**Empty at this tier.** The ion fills are FIVE new undeclared slots ($\rho_0,\varepsilon_0,m_0,\mu_0,\sigma_0$ — six under a slot-$u$ reading) dressing derived names; they are recorded as a
parametric subclass of IT.37–IT.39/IT.43–IT.45's construction class, NOT added as parameters —
adopting any of them (or the $\rho_{\mathrm B}(N)$, $\varepsilon_q(n_e)$, $m_L(N,n_e)$ laws, or a
homogenizing mass² scale) would each be a P4-class declaration [BM.6(4)], and none is issued. The
inherited owed declarations stand unchanged — the mass-read route choice [IT.14(3); BM.30(5)],
$\mathfrak h$ (P1), $\varepsilon_q$ (AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3),
$\rho_{\mathrm B}$, $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile,
the lift and the vielbein (AT.60), and the read rules (M1′)–(M3′) [AT.54(6)].

## §Open-IT additions from Tier IT.15

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.15 opens **no new row**: the capacity-bound calibration matrix and its ion fills are recorded as a **parametric subclass** of IT.37–IT.39/IT.43–IT.45's construction class — the ratio unformed (BM.83(5)'s localization census closed; ε_q enters no formed cross-currency ratio), the crystallization cost circular and N-blind (the nilpotent artifact), the derivative asymmetry smuggled rather than derived, C_cap-vs-16 numerology, seven premise corrections. **Not adopted.** If the Architect ever wants ion-indexed calibration reads, the door is the deferred Calibration Era's program [IT.5(2); IT.33; AT.63(4)] with the (M1′)–(M3′) read rules [AT.54(6)] and the three declarations IT.45(5) named | IT.46(3),(5); IT.47(1),(3); IT.48(2),(4),(5) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5)]: (IT-O1) the formed transit-leg amplitude — open on
three grounds, the missing primitive deficit 1′ [IT.41]; (IT-O2) the N≥4 multi-seal configuration
calculus — the binding value; (IT-O3) the handshake-indicator operational theory — the
χ_{NE≥𝒯₀}-gated read families; (IT-O5) the isotope cutoff — the empirical/dynamical side at
IT-O1; the owed route choice [IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the Level-5
inheritance [AT.63(3),(5)].
