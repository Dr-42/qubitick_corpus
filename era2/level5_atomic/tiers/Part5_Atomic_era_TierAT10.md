# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.10: the Pauli term as a ledger object

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.10 — the Pauli tensor on the native
frame: the bivector census and the exact two-channel decomposition, the Weitzenböck identity
(the Pauli term born from the Dirac skeleton's square, slot-free), the transport-curvature
census on the two constructed families, and the structural $F_1/F_2$ dictionary.
**Tags.** AT.56–AT.58. **Pattern.** BM.130 / BM.144 / BM.152 — the construction tiers and the
status-and-closure tag of a tier.
**Status.** discovery-phase working tier, **closed at AT.58**. Nothing is adopted into the frozen
canon; no declaration issues; §Cal-AT stays empty; no clause of Parts 1–4 is modified, retracted
or renumbered. Session 6's record: `era2/level5_atomic/discovery/PAULI_TERM.md`.
**Machine.** `era2/level5_atomic/checks/pauli_term.py` → **23/23 exact** (AT.56–AT.58);
`era2/level5_atomic/checks/run_all_era2.py` → **34 checkers, 610 exact markers, 0 failures,
exit 0**; `era2/level5_atomic/checks/check_era2_format.py` → the format + citation gate over all
twelve Part 5 documents. Exact arithmetic: `Gauss(i)` 4×4 and 8×8 identities, exact multivariate
polynomial identities over $\mathbb Q(i)[t_1,\dots,t_{16}]$ (16 independent indeterminate
transport entries; 416 monomials generated and cancelled), `Fraction` phase pairs (Pythagorean
and quarter-turn), integer winding censuses, exact ranks by elimination.
**No floating point in any assertion. No calibration parameter receives a value. No measured
value enters [P5].**
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.
**Mandate.** The Architect's directive: *"Please continue on the Pauli things."* The record's
live Pauli threads at session start: **(i)** AT.48(3)'s DECOMPOSITION THEOREM — stated and
adjudicated, never mechanized as exact matrix identities; **(ii)** AT-O28 (priority 1) — the
global Dirac-type operator, "two slots away", whose skeleton's graded shape is derived for every
slot choice [AT.47(8)]; **(iii)** `frame_section.py`'s residue (iv) — "the $\sigma^{\mu\nu}F_{\mu\nu}$
moment coupling — needs (i)–(iii) AND the global operator". The tier executes all
three: the decomposition is mechanized and completed (two new rows: the Hodge row and the
ray-wise $\mathfrak{so}(4)$ split); the Pauli term's BIRTH from the skeleton's square is proved
slot-free and fully symbolically, so the two marked slots block its evaluation, never its
algebra; and residue (iv) is superseded in scope. The other Pauli — exclusion — is
re-certified as a gate and stands untouched [BM.128(5)].
**Notation.** $\mathfrak F_{ab}:=[T_a,T_b]$ is this tier's *transport curvature* — deliberately
$\neg\mathcal F$ (frames [FT.93]) and $\neg F_{\mu\nu}$ (the chart-side field strength
[EM.14; CT1.19/CT1.22], a dictionary partner only [BM.134(5)]); $\mathsf S^\pm_i$ are the
self-dual/anti-self-dual bivector combinations — deliberately $\neg\Sigma$ (CT1.2's named basis
element). All indices are frame indices on the Euclidean read of $\mathcal F_0$ [FT.93(1) note;
AT.47(1)]: A3's $\eta=(-,+,+,+)$ labels the $T$-involution only [CT1.1] and enters no Clifford
relation anywhere in this tier.

---

### AT.56 — The Pauli tensor on the native frame: the bivector census, the exact two-channel decomposition, the Hodge row, and the no-third-channel theorem

**Thm.**
$$(1)\quad\textbf{GATES (re-produced,}\ \neg\textbf{new):}\qquad\mathcal F_0=(\sigma_1\otimes\sigma_2,\ \sigma_2\otimes\sigma_2,\ \sigma_3\otimes\sigma_2,\ \sigma_0\otimes\sigma_1)\ \text{is a pairwise-anticommuting Clifford 4-frame,}\ \gamma_a^2=+I_4\ \ [\mathrm{FT.93}(1),(2);\ \mathrm{AT.47}(1)];$$
$$\gamma_{\mathcal F_0}=\gamma_1\gamma_2\gamma_3\gamma_4=\sigma_0\otimes\sigma_3=I\otimes\hat\kappa\ \ \textbf{AS MATRICES}\ \ [\mathrm{AT.47}(3)\ \text{relocation row}];\qquad(\hat\omega,\hat\chi,\hat\kappa)\ \text{quaternionic, gauge-trivial}\ [\mathrm{Def\text{-}H.34};\ \mathrm{AT.47}(2)];$$
$$\widehat M=-q_{\mathrm{EM}}(I\otimes\hat\kappa),\quad\{\widehat M,\hat\chi\}=0\ \ [\mathrm{AT.48}(2\mathrm a),(4)];\qquad\dim\wedge^2(\mathbb C^2)=1,\quad\dim\wedge^3(\mathbb C^2)=0\ \ \textbf{— the OTHER Pauli (exclusion) stands}\ [\mathrm{BM.128}(5)]$$
$$(2)\quad\textbf{THE BIVECTOR CENSUS:}\qquad\sigma^{\mu\nu}:=\tfrac i2[\gamma_\mu,\gamma_\nu]\ \ \text{on}\ \mathcal F_0:\ \ \text{all six are Hermitian, square to}\ +I_4,\ \text{traceless, and EACH IS}\ \pm1\times\text{ONE Pauli product}$$
$$\textbf{— six DISTINCT directions of the 15, species 3 mixed + 2 off-diagonal + 1 diagonal:}\qquad\sigma^{12}=-(\sigma_3\otimes\sigma_0),\quad\sigma^{13}=+(\sigma_2\otimes\sigma_0),\quad\sigma^{23}=-(\sigma_1\otimes\sigma_0);$$
$$\sigma^{14}=\sigma_1\otimes\sigma_3,\quad\sigma^{24}=\sigma_2\otimes\sigma_3,\quad\sigma^{34}=\sigma_3\otimes\sigma_3\qquad[\text{machine: exhaustive over the 6 bivectors}\times\text{the 15 directions}]$$
$$(3)\quad\textbf{THE CHANNEL IDENTITIES (exact matrix equalities):}\qquad\textbf{MAGNETIC:}\ \ \sigma^{ab}=-2\varepsilon_{abc}W_c^{\mathrm{ext}}\ \ [\mathrm{EW.32}\ \text{carrier};\ \mathrm{AT.47}(2)]$$
$$\textbf{— the magnetic bivectors ARE the gauge block of the extended carrier, index-carrying exactly as AT.47(2)'s maximality theorem demands;}$$
$$\textbf{ELECTRIC:}\ \ \sigma^{a4}=\sigma_a\otimes\hat\kappa=(\sigma_a\otimes I_2)\,\gamma_{\mathcal F_0}\ \ [\mathrm{AT.47}(3)];\qquad\textbf{BRIDGE:}\ \ \sigma^{a4}=-\varepsilon_{abc}\,\sigma^{bc}\gamma_{\mathcal F_0}$$
$$\boxed{\ \textbf{the two channels of AT.48(3)'s decomposition theorem are the two grades of ONE}\ \mathrm{Cl}(3,0)\ }\qquad\text{and}\ \gamma_{\mathcal F_0}\ \text{is}\ \widehat M\text{'s matrix}\ [\mathrm{AT.48}(2\mathrm a)]$$
$$(4)\quad\textbf{THE DECOMPOSITION THEOREM, MECHANIZED (AT.48(3) upgraded from stated to proved): for EVERY antisymmetric}\ F,$$
$$\boxed{\ \sigma^{\mu\nu}F_{\mu\nu}=-4\,\mathfrak B_c\,W_c^{\mathrm{ext}}+2\,\mathfrak E_a\,(\sigma_a\otimes\hat\kappa)\ }\qquad\mathfrak B_c:=\tfrac12\varepsilon_{cab}F_{ab},\quad\mathfrak E_a:=F_{a4}$$
$$[\text{machine: the 6 basis}\ F,\ 3\ \text{fixed integer trials, additivity against the basis expansion — exact}\ 4\times4\ \text{identities over}\ \mathbb Q];$$
$$\textbf{NO THIRD CHANNEL:}\ \ \text{the Pauli-basis decomposition}\ [\mathrm{CT1.1}\ \text{trace orthogonality}]\ \text{has ZERO components in the other 9 directions, in}\ I_4,\ \text{and in}\ I\otimes\hat\kappa;$$
$$\textbf{adversarial witnesses (non-vacuity):}\ \gamma_{\mathcal F_0}\ \text{itself carries}\ (0,3)\text{-component}\ 1;\ \ \text{a halved magnetic coefficient breaks the identity}$$
$$(5)\quad\textbf{THE GRADE SEPARATION AND THE HODGE ROW (new):}\qquad\mathfrak T\bigl(\sigma^{\mu\nu}F_{\mu\nu}\,\gamma_{\mathcal F_0}\bigr)=0\ \ \forall F\ \ \implies\ \ \widehat M\ \textbf{is NEVER a bivector contraction}$$
$$\textbf{— it is the electric channel's grade-4 partner, formable only by the SCALAR boundary read (the native index-carrying EM read is absent: AT-O29/AT.48(3), now with its exact grade reason);}$$
$$\sigma^{\mu\nu}\gamma_{\mathcal F_0}=-(*\sigma)^{\mu\nu},\qquad(*F)_{\mu\nu}:=\tfrac12\varepsilon_{\mu\nu\rho\sigma}F_{\rho\sigma},\quad\varepsilon_{1234}=+1\qquad\implies\qquad\boxed{\ \bigl(\sigma^{\mu\nu}F_{\mu\nu}\bigr)\circ\widehat M=q\cdot\sigma^{\mu\nu}(*F)_{\mu\nu}\ }$$
$$\textbf{THE BOUNDARY MOMENT OPERATOR IS}\ q\times\textbf{THE HODGE ROTATION of the Pauli tensor — it exchanges the electric and magnetic channels;}$$
$$\text{dictionary partner of the smooth EM duality rotation,}\ \neg\text{its equal}\ [\mathrm{BM.134}(5)\ \text{discipline}]$$
$$(6)\quad\textbf{THE RAY-WISE}\ \mathfrak{so}(4)\ \textbf{SPLIT (new):}\qquad\mathsf S^\pm_i:=\tfrac12\bigl(\sigma^{i4}\pm(*\sigma)^{i4}\bigr)=\mp(\sigma_i\otimes I_2)\,P_\pm\qquad[P_\pm:\ \mathrm{FT.93}(2)\ \text{ray projectors};\ \mathrm{Def\text{-}H.33}]$$
$$[\mathsf S^\pm_i,\mathsf S^\pm_j]=\mp2i\,\varepsilon_{ijk}\mathsf S^\pm_k,\qquad[\mathsf S^+,\mathsf S^-]=0\ \ \textbf{BECAUSE}\ \ P_+P_-=0$$
$$\boxed{\ \textbf{the two}\ \mathfrak{su}(2)\ \textbf{copies of the Pauli tensor live on the TWO RAYS of the orientation doublet}\ }\qquad\text{the born term (AT.57) acts ray-wise (grade-even);}\ \widehat M\ \text{flips rays}\ [\mathrm{AT.48}(4)]$$
$$(7)\quad\textbf{NO NEW OPERATOR CONTENT:}\ \ \text{the algebra generated by the six bivectors is EXACTLY the 8-dimensional span}\ \{I_4,\ \sigma_i\otimes I_2,\ \sigma_i\otimes\hat\kappa,\ I\otimes\hat\kappa\}\ \cong\mathrm{Cl}(3,0);$$
$$\text{Lie closure with Gaussian-integer constants:}\quad[W_1^{\mathrm{ext}},W_2^{\mathrm{ext}}]=iW_3^{\mathrm{ext}},\qquad[e_1,e_2]=4iW_3^{\mathrm{ext}},\qquad[W_1^{\mathrm{ext}},e_2]=ie_3\qquad[e_a:=\sigma_a\otimes\hat\kappa];$$
$$\text{64 products close in the span; real rank 8}\ \ [\text{machine}]\ \ \implies\ \ \textbf{the Pauli term adds ZERO new operators to the corpus — it is a re-grading of AT.47/AT.48's own algebra}$$
$$(8)\quad\textbf{THE GRADING TABLE:}\qquad[\sigma^{\mu\nu},\gamma_{\mathcal F_0}]=0\ \ \text{all six (grade-even)};\qquad[\sigma^{ab},\hat\chi]=0\ \ \text{(magnetic:}\ \hat\chi\text{-EVEN, acts within each ray)};\qquad\{\sigma^{a4},\hat\chi\}=0\ \ \text{(electric:}\ \hat\chi\text{-ODD, flips the doublet like}\ \widehat M\ [\mathrm{AT.48}(4)])$$
$$(9)\quad\textbf{THE NATIVE FEED (assembly):}\qquad\text{the magnetic side's index: the shift}\ w_i\ \textbf{alone}\ [\mathrm{AT.2}(4);\ \mathrm{FT.157}(1)]\implies\mathrm{AT.6}\ \text{'s functional, up to}\ \varkappa\beta\ [\mathrm{AT.34};\ (S)\ \text{derived up to scale per AT.34(7)}];$$
$$\text{the electric side's vector datum: no native feed}\ [\mathrm{AT\text{-}O29};\ \mathrm{AT.48}(3)]\implies\textbf{it collapses to the scalar boundary channel}\ \widehat M\ [\mathrm{AT.48}(2\mathrm a),\ \mathrm{EM.9b}\ \text{telescoping};\ q_{\mathrm{EM}}\in\{-1,0,1\}\ [\mathrm{EM.9},\ \mathrm{D3.4}]];$$
$$\boxed{\ \textbf{AT.48(3)'s decomposition is exact AND complete: two channels, no third, each with its native supply named}\ }$$
$$(10)\quad\textbf{status:}\qquad\textbf{derived:}\ (2)\text{--}(9);\qquad\textbf{re-produced gates:}\ (1);\qquad\neg\text{a declaration},\ \neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)]$$

**Req.** A3, A8 (Part 1); P1, P4, P5, CT1.1, CT1.2, CT1.12a(2) (Part 2); EW.32, EM.9, EM.9b, EM.12, EM.14, D3.4 (Part 2); Def-H.33, Def-H.34, FT.93(1),(2),(3),(4), FT.157(1) (Part 3); AT.2(3),(4), AT.3, AT.6, AT.34, AT.46, AT.47(1),(2),(3),(4), AT.48(2),(3),(4),(5), AT-O29 (this level); Def-BM.3(7), BM.128(5), BM.134(5) (Part 4); Levi-Civita contraction, Pauli-basis decomposition by CT1.1's trace orthogonality, Hodge duality in the frame's Euclidean read, exact elimination over $\mathbb Q$ and $\mathbb Q(i)$ [math; machine: `pauli_term.py` §§A–C, 13/13].

**Pf.**
$$(1):\ \text{the frame relations and the pseudoscalar entrywise; the triple's quaternion rows;}\ \widehat M\ \text{'s}\ (0,3)\ \text{decomposition};\ \text{the antisymmetrizer ranks}\ (4\times4\ \text{and}\ 8\times8)\ \text{by exact elimination}\ [\text{machine A1--A3}];$$
$$(2):\ \sigma^{\mu\nu}\ \text{built from the commutators; each matched against all}\ \pm15\ \text{Pauli directions, unique hit per bivector}\ [\text{machine B1}];\ (3):\ \text{the six equalities entrywise over}\ \mathbb Q(i)\ [\text{machine B2,B3}];$$
$$(4):\ \text{the identity on the 6 basis}\ F\ \text{plus 3 integer trials plus additivity}\ [\text{machine C1}];\ \text{the 16-coefficient decompositions with the two adversarial witnesses}\ [\text{machine C2}];$$
$$(5):\ \text{the trace rows; the 6 Hodge identities; the 6 duality rows at}\ q=1\ [\text{machine C3}];\ (6):\ \text{the}\ \mathsf S^\pm\ \text{reduction to the ray projectors and the 9 commutators}\ [\text{machine B5}];$$
$$(7):\ \text{the 64-product closure census and the real rank}\ [\text{machine B4,B6}];\ (8):\ \text{the 16 commutator/anticommutator rows}\ [\text{machine C4}];\ (9),(10):\ \text{assembly and the record rows}.\ \blacksquare$$

**Phys.** Ask the ledger for the Pauli tensor and it answers with a census: the six bivectors of
the native frame are signed Pauli products — three of them *are* the gauge block of the extended
carrier, exactly as AT.47's maximality theorem demanded (the spatial directions carry the gauge
index, and so do the spatial bivectors), and the other three are that block times the shortlist
pseudoscalar. One $\mathrm{Cl}(3,0)$, eight dimensions, no new operators: the Pauli term is a
re-grading of machinery the corpus already built. The decomposition theorem AT.48 stated is now
a machine identity with a zero-component census behind it — no third channel exists, and the
census knows it could have failed: the pseudoscalar itself carries the component the contraction
provably lacks. That grade separation is why $\widehat M$ is a *partner* of the electric channel
rather than a member of it, and the Hodge row says what the partner is: charge times the duality
rotation. The boundary moment operator of the hydrogen connector — charge read, flicker-immune,
Ward-protected — acts inside the Pauli algebra as the exchange of electric and magnetic, and its
splitting $2|q|$ is the spectrum of that exchange's generator. The deepest new row is the
ray-wise split: the two $\mathfrak{su}(2)$ copies of the Pauli tensor sit on the two rays of the
orientation doublet and commute because the rays are orthogonal — each traversal orientation
carries its own full internal spin algebra of curvature, while the boundary moment flips between
them. The born term and the boundary term are exact grade-conjugates, and the smooth
magnetic-even/electric-odd chirality pattern falls out of the ledger's own involutions with
nothing imported. What feeds the channels natively is named to the symbol: the shift for the
magnetic side (AT.6's functional, up to $\varkappa\beta$), the scalar charge read for the
electric side (the vector read is absent, AT-O29, now with its grade reason). Chart-side
$F_{\mu\nu}$ stays a dictionary partner, never an equal.

---

### AT.57 — The Weitzenböck identity: the Pauli term born from the skeleton's square at tree coefficient one, slot-free; the drag connection is fiber-abelian; the EW.32 curvature is Gaussian-integer valued

**Thm.**
$$(1)\quad\textbf{THE SETUP:}\qquad\mathcal D=\sum_{a=1}^{4}\gamma_a\otimes T_a\ \ \text{on}\ \ \mathcal H_{\mathrm{ext}}\otimes\mathbb C^2_T\qquad[\mathrm{AT.47}(8)\ \text{'s skeleton; the four transports}\ T_a\ \text{are the undeclared slots}\ [\mathrm{AT.47}(9)(\mathrm i)\text{--}(\mathrm{iii});\ \mathrm{AT\text{-}O28}]]$$
$$(2)\quad\textbf{THE WEITZENBÖCK IDENTITY (slot-free, FULLY SYMBOLIC — 16 independent indeterminate transport entries, exact multivariate polynomial identity over}\ \mathbb Q(i)[t_1,\dots,t_{16}]\textbf{, 416 monomials generated and cancelled):}$$
$$\boxed{\ \mathcal D^2=I\otimes\Bigl(\sum_a T_a^2\Bigr)-\tfrac i2\,\sigma^{\mu\nu}\otimes\mathfrak F_{\mu\nu}\ }\qquad\mathfrak F_{ab}:=[T_a,T_b]\ \ \text{(the transport curvature)}$$
$$\textbf{the square of the Dirac skeleton = the transport Laplacian + THE PAULI TERM AT TREE COEFFICIENT EXACTLY 1 — for EVERY choice of the undeclared slots;}$$
$$\gamma_a\gamma_b=-i\sigma^{ab}\ \ \text{re-certified entrywise};\qquad\textbf{AT-O28's two slots do NOT block the identity — they block its evaluation}$$
$$(3)\quad\textbf{THE CHIRALITY ROWS RIDE ALONG (symbolic):}\qquad\{\mathcal D,\ \gamma_{\mathcal F_0}\otimes I\}=0\ \ [\mathrm{AT.47}(8)\ \text{re-certified with general transports}];\qquad[\mathcal D^2,\ \gamma_{\mathcal F_0}\otimes I]=0$$
$$\textbf{the Pauli term is born INSIDE the doublet's ray algebra (grade-even), never across the rays}$$
$$(4)\quad\textbf{THE BORN TERM RE-SPLITS BY THE CHANNEL IDENTITIES (symbolic, fully general):}$$
$$-\tfrac i2\sigma^{\mu\nu}\otimes\mathfrak F_{\mu\nu}=2i\,W_c^{\mathrm{ext}}\otimes\mathfrak B_c-i\,(\sigma_a\otimes\hat\kappa)\otimes\mathfrak E_a\qquad\mathfrak B_c:=\tfrac12\varepsilon_{cab}[T_a,T_b],\quad\mathfrak E_a:=[T_a,T_4]$$
$$\textbf{the curvature feeds EXACTLY AT.56(3)'s two channels — the gauge block with the magnetic curvature curl, the pseudoscalar-twisted internal Pauli with the electric curvature; no third channel can be born}\ [\mathrm{AT.56}(4)]$$
$$(5)\quad\textbf{THE COEFFICIENT IS A THEOREM, NOT A CONVENTION:}\qquad T_1=T_2=T_3=T_4=T\ \ \text{(one generic transport)}\implies\mathfrak F\equiv0\ \ \wedge\ \ \mathcal D^2=\bigl(\sum_a\gamma_a\bigr)^2\otimes T^2\ \ \textbf{EXACTLY}$$
$$\text{the Pauli term vanishes while the skeleton stays nonzero: the coefficient 1 is forced by the Clifford relations alone, with no normalization choice left;}$$
$$\boxed{\ \textbf{the algebraic root of AT.48(5i)'s FLAGGED tree parallel: the coefficient is DERIVED; its identification with any measured}\ g\ \textbf{stays QUARANTINED}\ }\qquad[\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7);\ \mathrm{EM.25}(7)\ \text{'s}\ e_0\ \neg\text{issued}]$$
$$(6)\quad\textbf{THE DRAG CONNECTION IS FIBER-ABELIAN:}\qquad T(\Theta)=\mathrm{diag}(i^{+\Theta},i^{-\Theta})=\exp\bigl(i\tfrac\pi2\Theta\hat\kappa\bigr)\ \ [\mathrm{AT.46}(5);\ \mathrm{AT.47}(7)]\ \ =\ U\bigl(\tfrac\pi2\Theta,\ \hat z\bigr)\ \ [\mathrm{EW.32}]$$
$$\textbf{— the drag exponential IS the}\ \hat z\text{-axis member of the EW.32 family (9 integer windings, odd and even, entrywise); ALL drag transports COMMUTE (81 pairs)}\implies\mathfrak F\equiv0$$
$$\boxed{\ \textbf{the drag connection NEVER births a Pauli term; its whole contribution sits in}\ \textstyle\sum_aT_a^2\ \textbf{— diagonal fourth-root phases, the winding/statistics side}\ [\mathrm{AT.46}(6)]\ }$$
$$\textbf{frame-dragging changes how a polygon exchanges, not what moment it couples — the two AT.46 effects stay separated at the operator layer}$$
$$(7)\quad\textbf{THE EW.32 CURVATURE, CLOSED FORM AND LATTICE CENSUS:}\qquad[U_a,U_b]=-2i\sin\phi_a\sin\phi_b\,\bigl((\hat n_a\times\hat n_b)\cdot\vec\sigma\bigr)\qquad[\text{machine: }576\ \text{exact identities — 8 phase pairs incl.}\ (\tfrac35,\tfrac45),(\tfrac5{13},\tfrac{12}{13})\ \text{and the quarter turns}\times3\times3\ \text{axis pairs}]$$
$$\text{vanishing iff the axes align or either phase is a half-turn};\qquad\textbf{the fourth-root lattice:}\ \phi\in\tfrac\pi2\mathbb Z\times3\ \text{axes}=12\ \text{transports},\ 66\ \text{pairs}:$$
$$\boxed{\ \textbf{EXACTLY 12 nonzero curvatures, EVERY value}\ \pm2i\sigma_k\ \textbf{— GAUSSIAN INTEGERS, zero criterion exact}\ }\qquad\text{the eighth root never appears}\ [\mathrm{Def\text{-}BM.16}(5);\ \mathrm{AT.48}(5\mathrm{iii})]$$
$$\textbf{NO CONTINUOUS LOCUS at the operator layer — the connection-side confirmation of AT.54(6)'s measure-side no-go}$$
$$(8)\quad\textbf{TWO EXPLICIT}\ \mathbb C^8\ \textbf{WITNESSES (integer entries, direct 8}\times8\ \text{squaring vs the identity):}\qquad(\mathrm i)\ \ T=(i\sigma_1,\ i\sigma_2,\ I,\ I):\ \ \textstyle\sum_aT_a^2=0,\quad\mathcal D^2=2(\sigma_3\otimes I_2)\otimes\sigma_3$$
$$\text{— the PURE born Pauli term, magnetic channel alone, curvature}\ [T_1,T_2]=-2i\sigma_3;\qquad(\mathrm{ii})\ \ T=(i\sigma_1,\ i\sigma_2,\ I,\ i\sigma_3):$$
$$\mathcal D^2=-2I_8+2(\sigma_3\otimes I_2)\otimes\sigma_3+2(\sigma_1\otimes\hat\kappa)\otimes\sigma_2-2(\sigma_2\otimes\hat\kappa)\otimes\sigma_1\ \ \textbf{— BOTH channels live, the electric one switched on by}\ [T_a,T_4];$$
$$\text{the born term is}\ \gamma_{\mathcal F_0}\text{-even (ray-wise, AT.56(6)) with Gaussian-integer entries throughout}$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (2)\text{--}(8);\qquad\textbf{what the slots block: the evaluation,}\ \neg\textbf{the algebra};\qquad\textbf{marked,}\neg\textbf{adopted (unchanged): the lift and the base frame}\ [\mathrm{AT.47}(5);\ \mathrm{Def\text{-}H.37}(2)],\ \text{the P4 transport profile}\ (\ell_c,\mathbf c)\ [\mathrm{AT.47}(6),(9)(\mathrm{iii})]$$

**Req.** A3, A8 (Part 1); P1, P4, P5, CT1.1, EW.32, EM.25(7) (Part 2); Def-H.33, Def-H.34, Def-H.37(2), FT.22, FT.93(1),(2),(7) (Part 3); AT.2(4), AT.6, AT.34, AT.46(5),(6), AT.47(5),(6),(7),(8),(9), AT.48(5), AT.54(6), AT.56 (this level); AT-O28 (this level); Def-BM.3(7), Def-BM.16(5), BM.88(1), BM.125(4), BM.126(1), BM.134(5) (Part 4); multivariate polynomial identities over $\mathbb Q(i)[t_1,\dots,t_{16}]$ with coefficient-wise equality, exact $i^n$ arithmetic, `Fraction` Pythagorean and quarter-turn phase pairs, exhaustive pair censuses [math; machine: `pauli_term.py` §§D–E, 8/8].

**Pf.**
$$(2):\ \text{the identity entrywise as 64 zero polynomials in the 16 indeterminates}\ [\text{machine D1}];\ \gamma_a\gamma_b=-i\sigma^{ab}\ \text{entrywise}\ [\text{machine D1}];\ (3):\ \text{two zero-polynomial identities, fully general}\ [\text{machine D2}];$$
$$(4):\ \text{64 zero-polynomial entries after the channel substitution}\ [\text{machine D3}];\ (5):\ \text{the equal-transport specialization as a symbolic identity with generic}\ T\ [\text{machine D4}];$$
$$(6):\ T(\Theta)=U(\tfrac\pi2\Theta,\hat z)\ \text{on the 9 windings; the 81 commutators; the diagonal}\ \textstyle\sum T_a^2\ \text{on 4 assignments}\ [\text{machine E1}];\ (7):\ \text{the 576 commutator identities vs the closed form; the 66-pair lattice census with the iff criterion}\ [\text{machine E2,E3}];$$
$$(8):\ \text{the two direct squarings, the Laplacian-part rows, the grade-even row, the integrality census}\ [\text{machine E4}];\ (9):\ \text{the record row}.\ \blacksquare$$

**Phys.** The Pauli term is not added to this corpus; it is born, and the birth certificate is an
identity that holds before any slot is declared. Square the Dirac skeleton — the chiral-odd
operator AT.47 derived for every choice of the undeclared data — and the square splits, with
nothing left over, into a transport Laplacian and the Pauli tensor contracted with the transport
curvature, at coefficient exactly one. The machine proves it with the sixteen transport entries
as independent indeterminates, so no specialization hides in the argument: whatever the lift and
the base frame turn out to be, the Pauli term is already there with its tree coefficient, and
that coefficient is a theorem of the Clifford relations, not a convention anyone chose. This is
the exact seat of the tree parallel AT.48 flagged without identifying — the structure derived,
the value quarantined behind the unissued $e_0$. Then the census of the two connections the
corpus actually owns. The drag — the polygon spin connection, the quantized frame-dragging of the
tetrahedral floors — turns out to be the $\hat z$-axis member of the EW.32 transport family, and
fiber-abelian: every pair commutes, the curvature vanishes identically, and the drag can never
birth a Pauli term. Frame-dragging changes how a polygon exchanges, not what moment it couples;
the whole AT.46 story of windings and statistics flips lives in the Laplacian part, exactly where
the earlier tier left it. The electroweak transport family is the one that curves: the commutator
has a closed form — the axis cross product times the phase sines — and on the fourth-root
lattice it takes exactly twelve nonzero values across sixty-six pairs, every one a Gaussian
integer times two. The curvature-born Pauli read is quantized at the operator layer before any
measure is consulted: the no-continuous-locus verdict AT.54 reached on the measure side now
holds on the connection side too, and the eighth root never appears anywhere in the phase
economy. Two integer witnesses close the tier's calculation: one where the square is *purely*
the born Pauli term with the Laplacian exactly zero, and one where the electric channel switches
on through the fourth transport — both channels alive, both ray-wise, both integral.

---

### AT.58 — The status of Tier AT.10: the structural $F_1/F_2$ dictionary, the adjudication, and the state of the Atomic era

**Thm.**
$$(1)\quad\textbf{THE STRUCTURAL}\ F_1/F_2\ \textbf{DICTIONARY (seats derived; values stay behind}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ [\mathrm{AT.54}(6)]\textbf{):}\qquad\begin{array}{l|l|l}\textbf{smooth seat}&\textbf{the ledger seat}&\textbf{status}\\\hline F_1\text{-type (charge/vertex)}&\text{the BOUNDARY channel: the}\ q\ \text{read, flicker-immune}\ [\mathrm{Def\text{-}BM.5}(1);\ \mathrm{AT.48}(5\mathrm{ii})],\ \text{Ward-protected}\ \delta=0\ [\mathrm{AT.53}(3)],\ \text{splitting}\ 2|q|\ \neg\text{renormalized}\ [\mathrm{AT.54}(4)]&\textbf{constructed}\\ F_2\text{-type (anomalous)}&\text{the MEASURE dressing:}\ \langle\aleph\rangle\ \text{excess rationals}\ (\tfrac16\ \text{at}\ n{=}2,\ \tfrac37\ \text{at}\ n{=}3,\ \varepsilon_q{=}\tfrac18\ \text{witnesses})\ [\mathrm{AT.54}(1)];\ \text{residues/contacts redistribute intensity, positions unmoved (the Lamb analog)}\ [\mathrm{AT.54}(3)]&\textbf{constructed (measure-side)}\\ \sigma^{\mu\nu}F_{\mu\nu}\ \text{operator layer}&\text{the CURVATURE-BORN gauge channel}\ [\mathrm{AT.57}(2),(4),(7)]:\ \text{Gaussian-integer valued, slot-dependent in EVALUATION only}&\textbf{constructed (algebra);}\\ & &\text{evaluation behind AT-O28 + the P4 profile}\\ \text{tree}\ g{=}2&\mathrm{AT.57}(5)\ \text{'s coefficient-1 theorem}&\textbf{derived; identification QUARANTINED}\ [\mathrm{P5}]\end{array}$$
$$\text{machine rows:}\ \mathsf S^\pm\ \text{supported on single rays}\ (\mathsf S^+P_-=0,\ \mathsf S^-P_+=0),\ \widehat M\ \text{flips them — the born (ray-wise) and boundary (ray-flipping) terms are exact grade-conjugates}\ [\mathrm{AT.56}(6)]$$
$$(2)\quad\textbf{BM.125(4)'s THREE GROUNDS, RE-PASSED on the new objects}\ (\sigma^{\mu\nu},\mathfrak F,\mathfrak B,\mathfrak E,\mathsf S^\pm):\qquad(\mathrm i)\ \ \text{operator-valued — every row an exact matrix identity, no single}\ \Delta(j)\ \text{needed}\ [\mathrm{BM.124}(4)\ \text{untouched}];$$
$$(\mathrm{ii})\ \ \neg\text{a product of masses — no}\ m^4,\ \neg\hat\mu,\ \neg\ell_c:\ \text{the symbol census is dimensionless throughout (structure constants Gaussian integers,}\ \mathfrak q^0);$$
$$(\mathrm{iii})\ \ \text{dimensions close by census};\qquad\textbf{BM.126(1) untouched: the crossing-weight alphabet remains}\ \{\varepsilon_q\}\ \textbf{alone} — \text{the transports are P4-class PROFILE data (marked},\ \neg\text{reweightings)} [\mathrm{AT.47}(9)(\mathrm{iii})]$$
$$(3)\quad\textbf{THE ADJUDICATION:}\qquad\begin{array}{l|l}\textbf{the row}&\textbf{the disposition}\\\hline\mathrm{AT.48}(3)\ \text{'s decomposition theorem}&\textbf{MECHANIZED AND COMPLETED: exact contraction identity + zero-component census + Hodge row + native-feed rows}\ [\mathrm{AT.56}(4),(5),(9)]\\ \texttt{frame\_section}\ \text{'s residue (iv)}&\textbf{SUPERSEDED IN SCOPE: what needed the slots and the global operator was the EVALUATION, never the algebra}\ [\mathrm{AT.57}(2)]\\ \mathrm{AT\text{-}O28}&\textbf{ADVANCED,}\ \neg\textbf{CLOSED: the slot-free algebraic core is constructed (skeleton + square + born-term anatomy + curvature census); the GLOBAL operator still needs the two marked slots}\ [\mathrm{AT.47}(5);\ \mathrm{Def\text{-}H.37}(2)]\ \textbf{and the P4 transport profile}\\ \mathrm{AT.48}(5\mathrm i)\ \text{'s flagged tree parallel}&\textbf{its exact algebraic seat named: the coefficient-1 theorem}\ [\mathrm{AT.57}(5)];\ \text{the flag stays —}\ \neg\text{identified},\ \neg\text{compared}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)]\\ \text{the other Pauli (exclusion)}&\textbf{re-certified, standing, untouched:}\ \dim\wedge^2(\mathbb C^2)=1,\ \dim\wedge^3(\mathbb C^2)=0\ [\mathrm{BM.128}(5);\ \mathrm{AT.56}(1)]\end{array}$$
$$(4)\quad\textbf{THE PROVED ABSENCES (each with its ground):}\qquad\begin{array}{l|l}\textbf{absence}&\textbf{the ground}\\\hline\neg\text{a third channel of}\ \sigma^{\mu\nu}F_{\mu\nu}&\text{the 6-direction image census + trace orthogonality}\ [\mathrm{AT.56}(4)]\\ \neg\widehat M\ \text{as a bivector contraction}&\text{the grade separation:}\ \mathfrak T(\sigma^{\mu\nu}F_{\mu\nu}\gamma_{\mathcal F_0})=0\ \forall F\ [\mathrm{AT.56}(5)]\\ \neg\text{a Pauli term born from the drag}&\text{fiber-abelianity: all drag transports commute}\ [\mathrm{AT.57}(6)]\\ \neg\text{a continuous curvature locus on the lattice}&\text{Gaussian-integer census of all 66 pairs}\ [\mathrm{AT.57}(7)]\\ \neg\text{new operator content}&\text{the 8-dimensional closure}\ [\mathrm{AT.56}(7)]\\ \neg\text{a continuous}\ a=(g{-}2)/2&\neg\text{a loop}\ [\mathrm{BM.88}(1)];\ e\ \neg\text{issued}\ [\mathrm{EM.25}(7)];\ \neg\text{a continuous locus}\ [\mathrm{AT.53}(3);\ \mathrm{AT.54}(6);\ \mathrm{AT.57}(7)\ \text{connection-side}];\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\end{array}$$
$$(5)\quad\textbf{MARKED,}\ \neg\textbf{ADOPTED (unchanged, none new):}\qquad(\mathrm a)\ \ \text{the lift}\ \triangleright\ [\mathrm{AT.47}(5);\ \mathrm{Def\text{-}H.37}(2)];\qquad(\mathrm b)\ \ \text{the base frame per floor (the six-frame menu)}\ [\mathrm{AT.47}(4),(5)];$$
$$(\mathrm c)\ \ \text{the level-price read rule}\ [\mathrm{AT.44}(8\mathrm{iv})];\qquad(\mathrm d)\ \ (S)\ \text{and AT.6's functional up to}\ \varkappa\beta\ [\mathrm{AT.34}(7)];\qquad(\mathrm e)\ \ \text{the P4 transport profile}\ (\ell_c,\mathbf c),\ \text{the fourth-root lattice condition formal}\ [\mathrm{AT.47}(6),(9)(\mathrm{iii})]$$
$$(6)\quad\textbf{THE OPEN LEDGER at this closure:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{why}\\\hline(\mathrm{AT\text{-}O2})\ w_i^\perp\ \text{gauge}&\textbf{BY NATURE}\ [\mathrm{AT.5}(4),\ \text{unchanged}]\\(\mathrm{AT\text{-}O3})\ (\varkappa,\beta)&\textbf{BY DESIGN: P4 core},\ \neg\text{issued}\ [\mathrm{AT.49}(5),\ \text{unchanged}]\\(\mathrm{AT\text{-}O7})\ \mathrm{BM.140}(6)\ \text{'s pin}&\textbf{the convention row}\ [\mathrm{AT.7};\ \mathrm{AT.40}(7),\ \text{unchanged}]\\(\mathrm{AT\text{-}O11})\ \text{the dictionary at}\ n{=}4&\textbf{DECIDABLE}\ [\mathrm{AT.50}(6)],\ \text{undecided;}\ \neg\text{blocking}\ [\mathrm{AT.54}]\\(\mathrm{AT\text{-}O13})\ \text{the Kerr route}&\textbf{ONE NUMBER AWAY: needs}\ (\mathrm{AT\text{-}O3})\ [\mathrm{AT.34},\ \text{unchanged}]\\(\mathrm{AT\text{-}O26})\ \text{the read-rule declaration}&\textbf{CLOSURE-PHASE ACT}\ [\mathrm{AT.44}(8\mathrm{iv})];\ \text{the gate of}\ (\mathrm{M1'})\ [\mathrm{AT.54}(6)]\\(\mathrm{AT\text{-}O27})\ \varepsilon_q\ \text{'s value}&\textbf{CALIBRATION:}\ \tfrac18\ \text{distinguished five ways}\ [\mathrm{AT.40}(1);\ \mathrm{AT.44}(4),(5);\ \mathrm{AT.54}(1)],\ \text{adoption}\ \neg\text{issued}\ [\mathrm{P5}]\\(\mathrm{AT\text{-}O28})\ \text{the global Dirac-type operator}&\textbf{ADVANCED: the slot-free core is constructed}\ [\mathrm{AT.57}(2)\text{--}(5)];\ \textbf{the global evaluation needs the two slots + the P4 profile}\\(\mathrm{AT\text{-}O29})\ \text{a native vector EM read}&\textbf{BY NATURE (proved absence)}\ [\mathrm{AT.48}(3)];\ \text{sharpened by the grade reason}\ [\mathrm{AT.56}(5)]\\(\mathrm{AT\text{-}O30})\ \text{the}\ B\ge5\ \text{cover census}&\textbf{OPEN, blocking nothing}\ [\mathrm{AT.52}(4)\text{--}(6);\ \mathrm{AT.55}(5)]\\\textbf{new}\ (\mathrm{AT\text{-}O31})\ \text{the fine-structure-type read of the hydrogen connector}&\textbf{SEATS IDENTIFIED, blocked: the ray-wise}\ \mathsf S^\pm\ \mathfrak{su}(2)\ [\mathrm{AT.56}(6)],\ \text{the Hodge rotation}\ [\mathrm{AT.56}(5)],\ \text{the measure rationals}\ [\mathrm{AT.54}];\ \text{needs}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ [\mathrm{AT.54}(6)]\ +\ \mathrm{AT\text{-}O28}\ \text{'s slots};\ \text{blocking nothing}\end{array}$$
$$(7)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)];$$
$$\text{calibration parameters added:}\ 0;\qquad\text{marked rows:}\ (5)\ \text{'s five, none adopted (none new)};\qquad\text{claims withdrawn:}\ 0;\qquad\text{new open rows:}\ 1\ (\mathrm{AT\text{-}O31})$$
$$(8)\quad\textbf{the machine state:}\qquad\texttt{era2/level5\_atomic/checks/run\_all\_era2.py}\to\textbf{34 checkers, 610 exact markers, 0 failures, exit 0};\qquad\texttt{check\_era2\_format.py}\to\textbf{12 Part 5 documents PASS};$$
$$\text{the shared libraries:}\ \texttt{qexact.py},\ \texttt{duality.py};\qquad\text{the folder remains deliberately NOT wired into}\ \texttt{verification/run\_all.py};\ \ \texttt{index/},\ \texttt{tags.json},\ \texttt{Summary.md}\ \neg\text{regenerated — promotion stays a closure-phase act}$$
$$(9)\quad\textbf{THE STATE OF THE ATOMIC ERA:}\qquad\text{the era chain, fourth consolidation:}$$
$$\text{grammar}\ [\mathrm{AT.41}]\to\text{dynamics}\ [\mathrm{AT.42}]\to\text{resolvent, price, spectrum}\ [\mathrm{AT.44}]\to\text{duality, drag, statistics flip}\ [\mathrm{AT.46}]\to\text{frame section}\ [\mathrm{AT.47}]\to\text{moment coupling}\ [\mathrm{AT.48}]$$
$$\to\text{the locked sector and the curl}\ [\mathrm{AT.50},\mathrm{AT.51}]\to\text{the dressed vertex}\ [\mathrm{AT.52}\text{--}\mathrm{AT.54}]\to\textbf{the Pauli anatomy:}\ \text{two channels, the Hodge row, the ray-wise split, the born term at coefficient one}\ [\mathrm{AT.56},\mathrm{AT.57}];$$
$$\text{between Level 5 and contact stand exactly:}\ \varepsilon_q,\ e_0,\ (\varkappa,\beta),\ \text{the chart-side scales}\ [\mathrm{AT\text{-}O3},\mathrm{AT\text{-}O27}];\ \ \text{the two declared slots and the P4 profile}\ [\mathrm{AT\text{-}O28}];\ \ \text{the read rules}\ [\mathrm{AT\text{-}O26};\ (\mathrm{M1'})];\ \ \text{the censuses}\ [\mathrm{AT\text{-}O30},\mathrm{AT\text{-}O31}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and this tier makes no contact claim}\ }\qquad[\mathrm{AT.39}(8)\ \text{'s standing row, re-cited and unchanged}]$$

**Req.** AT.56, AT.57 (this level); AT.5(4), AT.6, AT.7, AT.34(7), AT.39(8), AT.40, AT.44(8), AT.46, AT.47, AT.48, AT.49(5), AT.50(6), AT.52, AT.53(3), AT.54, AT.55(5), AT-O2, AT-O3, AT-O6, AT-O7, AT-O11, AT-O13, AT-O26, AT-O27, AT-O28, AT-O29, AT-O30 (this level); P1, P4, P5, A3, A8, CT1.1, CT1.19, CT1.22, EW.32, EM.9b, EM.12, EM.25(7) (Parts 1–2); Def-H.33, Def-H.34, Def-H.37(2), FT.22, FT.55(1), FT.93, FT.157(1) (Part 3); Def-BM.3(7), Def-BM.5(1), Def-BM.16(5), BM.88(1), BM.124(4), BM.125(4), BM.126(1), BM.128(5), BM.134(5) (Part 4); row-wise assembly only — no new mathematics at this tag [math; machine: `pauli_term.py` §F, 2/2 + the suite + the format gate].

**Pf.** Row-wise assembly of AT.56–AT.57, each row re-citing its own machine section and its own
locus; the ray-support and grade-conjugate rows re-certified [machine F1]; the BM.125(4)/BM.126(1)
symbol census re-run over all new objects [machine F2]; the format gate re-run over all twelve
Part 5 documents; the suite re-run end to end. No new mathematics is introduced at this tag.
$\blacksquare$

**Phys.** This tier took the corpus's oldest deferral about magnetism — the Pauli term, the door
session 1 explicitly walked away from because a $B$ to couple to is a reading, not a substance —
and found that the walk-away was right about the substance and premature about the algebra. The
smooth Pauli term, pulled back to the native frame, is not one foreign object but two native
channels in a single eight-dimensional algebra the corpus had already built: the gauge block and
its pseudoscalar twist, exchanging roles under multiplication by the very operator AT.48 derived
from the boundary charge. The anomaly's structural dictionary is now complete on the ledger
side: the $F_1$-type seat is the flicker-immune boundary channel the discrete Ward identity
protects, the $F_2$-type seat is the measure dressing with its rational excesses, and the
operator-layer seat is the curvature-born gauge channel — Gaussian-integer valued, born at
coefficient exactly one from the square of the chiral-odd skeleton, before a single slot is
declared. The two connections the corpus owns divide the labor with perfect asymmetry: the drag,
which is the polygon's spin connection and the statistics-flip's engine, curves nothing in the
fiber and can never birth a moment; the electroweak transport family curves, and its curvature
on the fourth-root lattice is twelve Gaussian integers and nothing else. What remains missing is
named to the symbol as always — the slots, the profile, the read rules, the scale — and one new
row opens where the era's hydrogen target now points: the fine-structure-type read, whose seats
this tier identified and whose values wait, like everything else, on the calibration boundary.
No contact claim is made; the coherence stands on its own arithmetic.
