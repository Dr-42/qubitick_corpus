# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.11: the resolution tier

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.11 — the four-row resolution: the metric
dictionary at every carrier level (AT-O11), the global Dirac-type operator on the first
arc-transitive floor (AT-O28), the fine-structure-type grammar and the exhaustive seat census of
the moment sector (AT-O31, AT-O6).
**Tags.** AT.59–AT.62. **Pattern.** BM.130 / BM.144 / BM.152 — the construction tiers and the
status-and-closure tag of a tier.
**Status.** discovery-phase working tier, **closed at AT.62**. Nothing is adopted into the frozen
canon; no declaration issues; §Cal-AT stays empty; no clause of Parts 1–4 is modified, retracted
or renumbered. Session 7's record: `era2/level5_atomic/discovery/RESOLUTION_TIER.md`.
**Machine.** `era2/level5_atomic/checks/dict_nfolds.py` → **13/13 exact** (AT.59);
`era2/level5_atomic/checks/global_dirac.py` → **12/12 exact** (AT.60);
`era2/level5_atomic/checks/fine_structure.py` → **8/8 exact** (AT.61);
`era2/level5_atomic/checks/run_all_era2.py` → **37 checkers, 643 exact markers, 0 failures,
exit 0**; `era2/level5_atomic/checks/check_era2_format.py` → the format + citation gate over all
thirteen Part 5 documents. Exact arithmetic: `Gauss(i)` matrices up to 32×32, exact Lagrange
interpolation and isotypic projectors over `Fraction`, exact ranks by elimination over $\mathbb Q$,
integer permutation and group tables ($S_n$ to $n=4$; the 24-element binary tetrahedral lift),
multivariate-free polynomial identities. **No floating point in any assertion. No calibration
parameter receives a value. No measured value enters [P5].**
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.
**Mandate.** The Architect's directive: *"Please proceed to resolve AT-O11, 28, 06, and 31 for
the next tier."* All four rows are resolved: AT-O11 **CLOSED** (the conjugacy table complete at
every level); AT-O28 **CLOSED AS CONSTRUCTION** (the operator built; one slot dissolved as
derived gauge, one proven physical, one discovered and named); AT-O31 **RESOLVED AS GRAMMAR**
(the fine-structure-type splitting grammar derived and quantized; values behind (M1′)–(M3′)
[AT.54(6)]); AT-O6 **CLOSED OUTRIGHT** (the exhaustive seat census). One new row opens:
(AT-O32), the per-floor extension census, blocking nothing.
**Notation.** $\mathcal H_n=(\mathbb C^2)^{\otimes n}$ the $n$-fold carrier with its $S_n$ action
[BM.128(8)]; $S_a=\tfrac12\sum_i\sigma_a^{(i)}$ the diagonal generators; $\Sigma_{(ij)}$ the
H-generator embedded on the pair $(ij)$; $\mathfrak D_{\mathrm{floor}}$ the global operator of
AT.60; $\Phi$ the S-transform automorphism of AT.60(4). The symbols $\mathfrak F,\mathfrak B,\mathfrak E,\mathsf S^\pm$ keep AT.57/AT.56's meanings; $\Pi_k$ keeps BM.131(6)'s.

---

### AT.59 — AT-O11 RESOLVED: the metric dictionary at every carrier level — the conjugacy theorem, the pair bits, and the exchange-fed kernel

**Thm.**
$$(1)\quad\textbf{THE SQUEEZE (the commutant, without heavy elimination):}\qquad\text{on}\ \mathcal H_n,\ n=2,3,4:\ \ S^2_{\mathrm{tot}}=\sum_aS_a^2\ \text{has minimal polynomial}\ \prod_j\bigl(S^2_{\mathrm{tot}}-j(j{+}1)\bigr)=0;$$
$$\text{the isotypic projectors}\ \Pi_j\ \text{(exact Lagrange interpolation; idempotent, orthogonal,}\ \textstyle\sum_j\Pi_j=I,\ \ \mathfrak T\Pi_j=m_j(2j{+}1))\ \text{give}\ m_j=(1,1),\ (2,1),\ (2,3,1);$$
$$\boxed{\ \dim\operatorname{End}_{\mathrm{SU}(2)}(\mathcal H_n)=\textstyle\sum_jm_j^2=2,\ 5,\ 14\ \ \textbf{— the Catalan numbers}\ [\mathrm{AT.40}(5)\ \text{reproduced}]\ }$$
$$\text{EVERY}\ S_n\ \text{permutation operator commutes with the diagonal action}\ [\text{machine: all}\ \pi,\ \text{all}\ n]\ \text{and their span has rank EXACTLY}\ \textstyle\sum_jm_j^2;$$
$$\therefore\ \textbf{the commutant IS the permutation span}\ [\text{math: End of the isotypic decomposition; the decomposition machine-verified}]\ \text{— the gauge-invariant reads are exactly the EXCHANGE reads}\ \mathfrak T(\pi\rho)$$
$$(2)\quad\textbf{the}\ n{=}2\ \textbf{specialization, matrix-for-matrix:}\qquad\mathrm{SWAP}=\tfrac12(E_0+\Sigma),\quad\Pi_{\mathcal R}=\tfrac34E_0+\tfrac14\Sigma,\quad\Pi_{\mathcal V}=\tfrac14E_0-\tfrac14\Sigma\qquad[\mathrm{AT.12}(2);\ \mathrm{AT.15}(1)\ \text{reproduced}]$$
$$(3)\quad\textbf{THE CENTRE = THE ISOTYPIC WEIGHTS:}\ \ \text{every}\ \Pi_j\ \text{commutes with every permutation (all}\ n,\ \text{all}\ j\ \text{— exhaustive)}\implies Z\bigl(\operatorname{End}_{\mathrm{SU}(2)}(\mathcal H_n)\bigr)=\mathrm{span}\{\Pi_j\}\ (\dim\ 2,2,3);$$
$$\text{the off-central content is the multiplicity coherence (the}\ \operatorname{Mat}_{m_j}\ \text{off-diagonals) — EXCHANGE content between isomorphic spin blocks}$$
$$(4)\quad\textbf{THE CONJUGACY THEOREM (the answer to AT-O11):}\qquad\text{embed every CT1.2 aspect generator}\ [\mathrm{CT0.12}\ \text{'s blocks}]\ \text{on every pair}\ (ij)\ \text{of}\ \mathcal H_n\ \text{and apply AT.12(1)'s own criterion}\ [X^{(ij)},S_a]=0\ \forall a:$$
$$\boxed{\ \textbf{EXACTLY}\ \Sigma^{(ij)}\ \textbf{(the H aspect — the volume mode)}\ \text{passes, plus}\ E_0^{(ij)}=I\ \text{(trace-fixed, ZERO free content) — at EVERY}\ n,\ \text{EVERY pair}\ }$$
$$W\text{-embeddings FAIL because}\ W_i^{(12)}=S_i\ \textbf{IS the gauge generator}\ [\text{machine: exact matrix identity at}\ n{=}2];\quad G\text{-embeddings transform as spin-}2;\quad J^\pm\text{-embeddings as spin-}1/\text{adjoint};$$
$$\textbf{the AT.15(5) ``none'' rows are THEOREMS AT EVERY LEVEL: conformal, shear and shift NEVER acquire carrier conjugates}\ (160\ \text{exact commutator tests; pass census}\ 1{+}1/3{+}3/6{+}6);$$
$$\mathrm{AT.15}(4)\ \text{'s T-parity mismatch is the}\ n{=}2\ \textbf{shadow of the commutant failure — one theorem, two faces}\ [\mathrm{C13}\ \text{'s}\ \eta\ \text{rows re-certified}]$$
$$(5)\quad\textbf{THE POSITIVE SUPPLY — the volume conjugates MULTIPLY, one per pair:}\qquad\Pi_{\mathcal R}^{(ij)}=\tfrac34I+\tfrac14\Sigma_{(ij)}\ \ \text{is an idempotent of trace}\ 3\cdot2^{n-2}\ \ \forall(ij),\ \forall n\ \ [\mathrm{AT.15}(1),(2)\ \text{generalized}];$$
$$b_{(ij)}(\rho)=\tfrac34+\tfrac14\langle\Sigma_{(ij)}\rangle:\ \ n(n{-}1)/2\ \textbf{gauge-invariant pair-bit reads}\ (1,\ 3,\ 6\ \text{at}\ n{=}2,3,4);$$
$$\boxed{\ \textbf{THE CASIMIR IDENTITY:}\ \ \textstyle\sum_{i<j}\Sigma_{(ij)}=2S^2_{\mathrm{tot}}-\tfrac{3n}2I\ }\qquad\text{the TOTAL volume read IS the isotypic-weight (central) read;}$$
$$\text{rank census:}\ \ r_n:=\operatorname{rk}\mathrm{span}\{\Sigma_{(ij)}\}=1,\ 3,\ 6;\qquad\mathrm{span}\{\Sigma\}\cap Z=\text{the Casimir line, EXACTLY 1-dimensional};\qquad\text{the differences are provably non-central (permutation witnesses)}$$
$$(6)\quad\textbf{THE ACCOUNTING (the ``13 vs 26'' framing corrected on the record):}\qquad\text{the carrier invariants and the mask space}\ \mathcal K_n\ \textbf{are different currencies}\ [\mathrm{BM.83};\ \mathrm{BM.134}(5)\ \text{discipline}]\ \text{— the count comparison was}\ \neg\text{a conjugacy question};$$
$$\text{the dictionary map:}\quad\textbf{IMAGE}=\text{the volume coordinate alone};\qquad\textbf{GENUS}=r_n\ \text{pair bits};\qquad\textbf{KERNEL}=\text{the multiplicity coherences}+\text{the non-Casimir central line};$$
$$n{=}4:\ \ 13=6\ \text{volume-conjugate}\ (1\ \text{central Casimir}+5\ \text{exchange-resolved})\ +\ 7\ \text{metric-blind};\qquad n{=}3:\ \ 4=3+1\qquad[\text{machine: union ranks}\ r_n{+}\#j{-}1];$$
$$\boxed{\ \textbf{the Catalan growth feeds the exchange reads, never new metric coordinates: the higher carriers see MORE OF EACH OTHER, not more of the metric}\ }$$
$$(7)\quad\textbf{SCOPE — the admissibility row:}\qquad D_{\mathrm{tick}}(n)=2^{n+1}\le16=C_{\mathrm{cap}}\iff n\le3\ \ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT0.11};\ \mathrm{AT.16}(4),(5);\ \mathrm{AT.50}(3)]\ \text{— exhaustive}\ n{=}0..8;$$
$$\text{the}\ n{=}3\ \text{dictionary is ACCESSIBLE (the highest standing rung); the}\ n{=}4\ \text{table is a FORMAL object at every accessible rung — AT.50(5)'s third-branch discipline verbatim}$$
$$(8)\quad\textbf{BM.131(6) consistent and re-seated:}\ \ \Pi_k=\tfrac1{k!}\sum_\sigma\hat P_\sigma\ \text{re-certified}\ (\Pi_k^2=\Pi_k,\ \operatorname{rk}=k{+}1,\ k{=}2,3,4)\ \textbf{and shown to BE the top isotypic projector}\ \Pi_{j=k/2}\ [\text{machine: matrix equality at every}\ k];$$
$$\text{its ``}k\ \text{invariants'' suggestion stays SUPERSEDED by AT.40(5)'s Catalan count (the symmetrizer is ONE read,}\ \neg k)\ \text{— recorded,}\ \neg\text{retracted, the frozen locus untouched};$$
$$(9)\quad\textbf{status:}\qquad\boxed{\ \textbf{AT-O11 CLOSED}\ }\qquad\text{the conjugacy table is complete: volume}\ \leftrightarrow\ \text{pair bits at every level; nine coordinates}\ \neg\text{conjugate at any level (theorem, not census absence)};$$
$$(\mathrm{R7}')\ \text{receives the permutation-span census as Level-5 data (contributes,}\ \neg\text{closes the Part-4 row}\ [\mathrm{BM.128}(8)]);\qquad\neg\text{a declaration},\ \neg\text{a P4 addition},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** A1, A3, A8, C13 (Part 1); P5, CT0.5, CT0.6, CT0.11, CT0.12, CT1.1, CT1.2, CT1.12, CT1.12a(2) (Parts 1–2); AT.2(3),(4), AT.12(1),(2), AT.15(1),(2),(3),(4),(5), AT.16(4),(5), AT.40(5), AT.50(3),(5),(6) (this level); AT-O11 (this level); BM.83, BM.128(5),(8), BM.131(6), BM.134(5) (Part 4); Schur–Weyl duality and the End-dimension theorem for isotypic decompositions, Lagrange interpolation, exact elimination over $\mathbb Q$ [math; machine: `dict_nfolds.py` §§A–E, 13/13].

**Pf.**
$$(1):\ \text{the minimal polynomial, the four projector laws and the traces entrywise per}\ n;\ \text{the}\ [\hat P_\pi,S_a]=0\ \text{census};\ \text{the span rank by exact}\ (\mathrm{re},\mathrm{im})\ \text{elimination};\ \text{the squeeze}\ [\text{machine B1}];$$
$$(2):\ \text{the three}\ 4\times4\ \text{identities and the rank-2 row}\ [\text{machine B2}];\ (3):\ \text{the 80 commutators}\ [\text{machine B3}];$$
$$(4):\ \text{the 160 embedding tests (16 generators}\times\text{pairs}\times3\ \text{levels); the}\ W_i^{(12)}{=}S_i\ \text{identity; the}\ \eta\ \text{parity rows}\ [\text{machine C1,C2}];$$
$$(5):\ \text{the idempotent and trace census (6 pairs); the Casimir identity as}\ 16\times16\ \text{matrices at}\ n{=}4;\ \text{the rank and intersection censuses}\ [\text{machine D1--D3}];$$
$$(6):\ \text{the union-rank identity}\ r_n{+}\#j{-}1\ \text{and the blind-count decomposition}\ [\text{machine D4}];\ (7):\ \text{the}\ 2^{n+1}\ \text{census}\ [\text{machine E1}];\ (8):\ \text{the matrix equality against}\ (1)\ \text{'s projectors}\ [\text{machine E2}];\ (9):\ \text{assembly}.\ \blacksquare$$

**Phys.** The question was whether the metric's nine invisible coordinates become visible to a
bigger carrier, and the answer is a theorem with a clean shape: visibility is the commutant
test, and only the volume generator passes it — at level two, three, four, and by the same
argument any level. The shift cannot pass because its generator *is* the gauge; the shear cannot
pass because it transforms; the conformal cannot pass because it is the trace everybody already
fixed. What grows with the carrier is not metric vision but mutual vision: the Catalan supply is
exchange content — reads that distinguish the copies inside one spin block, invisible to every
metric coordinate. The positive side grows too, and elegantly: every pair of carriers contributes
its own bit, the same affine read of the same Σ, and the sum of all pair bits is exactly the
total-spin Casimir — the central read the isotypic projectors already owned. So the dictionary's
image is one coordinate, its genus is the pair bits, its kernel is the exchange algebra, and the
old "13 against 26" tension dissolves as a currency mix-up the corpus's own commensurability bar
had already warned about. One honesty row: level four, where the count 13 lives, is a rung no
subnetwork can stand on — the n=4 table is formal, exactly like the rung-4 mask, and the highest
accessible dictionary is the triple's: four free reads, three of them volume, one of them pure
exchange.

---

### AT.60 — AT-O28 RESOLVED AS CONSTRUCTION: the global Dirac-type operator on the tetrahedral floor — the chirality dichotomy of the lift, the dissolved base frame, and the discovered vielbein

**Thm.**
$$(1)\quad\textbf{GATES (re-produced,}\ \neg\textbf{new):}\qquad\text{the }30\ \text{native frames and the }6\text{-frame weak-scalar shortlist}\ [\mathrm{FT.93}(1),(2);\ \mathrm{AT.47}(1),(4)];$$
$$\text{the binary tetrahedral lift}\ 2T:\ 24\ \text{elements, closed under all}\ 576\ \text{products,}\ \det=1\ [\mathrm{AT.10};\ \mathrm{AT.47}(5)];\qquad\text{the Ad-map}\ 2T\to\mathrm{Rot}\ \text{is TWO-TO-ONE onto the }12\ \text{integer rotations and SIGN-FREE}\ (R_{-U}=R_{U});$$
$$\mathrm{Rot}\ \text{acts SIMPLY TRANSITIVELY on the }12\ \text{arcs — exactly one}\ R_e\ \text{per arc}\ e\ \ [\mathrm{AT.34}(1)\text{--}(3)\ \text{re-produced, exhaustive}];$$
$$\textbf{MARKED ROW: the lift stays Def-H.37(2)'s DECLARED identification (Open Gaps 19), inherited at use —}\ \neg\textbf{derived,}\ \neg\textbf{adopted here}$$
$$(2)\quad\textbf{THE OPERATOR:}\qquad\mathfrak D_{\mathrm{floor}}=\sum_{\{v,w\}\in E(\Gamma_S)}\Bigl(E_{vw}\otimes\gamma_{a(e)}(\mathcal F_e)\otimes T_e\ +\ E_{wv}\otimes\gamma_{a(e)}(\mathcal F_e)\otimes T_e^\dagger\Bigr)\qquad\text{on}\ \ \mathbb C^4_v\otimes\mathcal H_{\mathrm{ext}}\otimes\mathbb C^2_T\ \ (32\ \text{dimensions});$$
$$\mathcal F_e:\ \text{the frame section per arc (the two lift readings below)};\qquad a(e):\ \text{the edge}\to\text{gamma-index labeling (the vielbein,}\ (9));\qquad T_e:\ \text{the transport profile (P4-class data, censused}\ \neg\text{chosen)};$$
$$\textbf{Hermitian BY CONSTRUCTION for unitary profiles (reverse arc = dagger) — verified on all}\ 72+\ \text{censured operators}\ [\text{machine}]$$
$$(3)\quad\textbf{THE SECTION CENSUS (both marked-lift readings):}\qquad\textbf{seed-only}\ \mathrm{Ad}(U\otimes I):\ \text{all }6\ \text{shortlist frames are FIXED POINTS}\ (144\ \text{checks})\implies\textbf{the section is CONSTANT}\ [\mathrm{AT.47}(5)\ \text{'s singleton row reproduced}];$$
$$\textbf{diagonal}\ \mathrm{Ad}(U\otimes U):\ \text{the shortlist splits into}\ 2\ \text{orbits}\times3\ [\mathrm{AT.47}(5)\ \text{reproduced}];\qquad\text{the section}\ \mathcal F_e=\mathrm{Ad}_{U_e\otimes U_e}\mathcal F_0\ \text{runs through}\ 3\ \text{frames}\ (12\ \text{distinct signed Pauli directions})\ \text{over the}\ 12\ \text{arcs}$$
$$(4)\quad\textbf{THE CHIRALITY DICHOTOMY — THE LIFT SLOT IS PHYSICAL:}\qquad\text{the grading nullity}\ \dim\{M:\{M,\gamma\}=0\ \forall\gamma\ \text{in the section}\}\ \text{is a similarity invariant, hence GAUGE-INVARIANT; exact elimination:}$$
$$\boxed{\ \textbf{seed-only: nullity EXACTLY}\ 1\ \text{(the unique grading}=\pm\ \text{the frame's own pseudoscalar}\ \sigma_0\otimes\sigma_i\ [\mathrm{FT.93}(1);\ \mathrm{AT.47}(3)];\ 6\ \text{frames}\to3\ \text{directions}\times2\ \text{signs)}\ }\qquad\boxed{\ \textbf{diagonal: nullity EXACTLY}\ 0\ }\qquad(2\ \text{orbits, both});$$
$$\textbf{seed-only}\implies\{\mathfrak D_{\mathrm{floor}},\Gamma\}=0,\ \ \Gamma=I_v\otimes\gamma_{\mathcal F}\otimes I_T,\ \ \Gamma^2=I_{32}:\ \ \textbf{CHIRAL-ODD, spectrum}\ \pm\textbf{-PAIRED, kernel reads exact};\qquad\textbf{diagonal}\implies\neg\exists\ \text{a global grading};$$
$$\boxed{\ \textbf{the two readings of the marked lift are}\ \neg\textbf{gauge-equivalent: THE LIFT DECLARATION DECIDES WHETHER THE GLOBAL OPERATOR HAS AN INDEX}\ }\qquad\text{Open Gaps 19's exact physical content, derived}$$
$$(5)\quad\textbf{SLOT (b) DISSOLVES — THE BASE FRAME IS A DERIVED GAUGE:}\qquad\Phi(M)=VMV^{-1},\ \ V=I_2\otimes S,\ \ S=\bigl(\begin{smallmatrix}1&1\\-i&i\end{smallmatrix}\bigr)\ [\mathrm{Def\text{-}H.34}\ \text{'s S-transform; exact over}\ \mathbb Q(i),\ SS^{-1}=I]:$$
$$\Phi\ \text{is an algebra automorphism}\ (105\ \text{Pauli-pair identities});\qquad\textbf{the}\ \Phi\text{-orbit on the shortlist FRAMES has size}\ 3\ \text{(cycling the grading directions)},\ \text{and the menu's other factor is the frame-reversal SIGN involution:}\ \ 6=3\times2;$$
$$(V\otimes I_T)\,\mathcal D(\mathcal F,T)\,(V^{-1}\otimes I_T)=\mathcal D(\Phi\mathcal F,\ T)\ \ \textbf{EXACTLY — all 6 frames, mixed lattice profile}\ [\text{machine: }8\times8\ \text{identities}];$$
$$\boxed{\ \textbf{all six base-frame choices give unitarily equivalent operators up to profile signs — the base-frame slot is a derived gauge,}\ \neg\textbf{a physical choice}\ }\qquad[\mathrm{AT.47}(4)\ \text{'s row SHARPENED at the frame-element level}]$$
$$(6)\quad\textbf{THE GLOBAL WEITZENBÖCK:}\qquad\boxed{\ \mathfrak D_{\mathrm{floor}}^2=3\cdot I_{32}\ +\ \text{(triangle blocks)}\ }\qquad\text{every diagonal}\ 8\times8\ \text{block}=\ \text{the degree Laplacian of}\ K_4\ (3\text{-regular)}\times\ \text{identity — TRANSPORT-INDEPENDENT}\ (\gamma^2{=}I,\ TT^\dagger{=}I);$$
$$\text{every off-diagonal block}=\ \textbf{exactly the TWO triangle 2-path terms}\ \gamma_a\gamma_b\otimes T_{vw}T_{wz}\ \ (4\ \text{profiles}\times6\ \text{blocks, entrywise});$$
$$\boxed{\ \textbf{ALL curvature content of the global square lives on the 2-simplices}\ }\qquad\text{the global born term localizes on the triangles, where the floor's holonomy lives}\ [\mathrm{AT.46};\ \mathrm{AT.57}(2)\ \text{'s fiber identity is its local factor}]$$
$$(7)\quad\textbf{THE TRIANGLE HOLONOMY CENSUS:}\qquad\text{drag profile:}\ \ T_{vw}T_{wz}T_{zv}=\mathrm{diag}(i^{\pm\Theta},i^{\mp\Theta}),\ \ \Theta\in\{\pm1,\pm3\}\ \textbf{INTEGER windings}\ (4\ \text{triangles}\times2\ \text{orientations})\ [\mathrm{AT.46}(5)\ \text{'s}\ \widehat D_{\mathrm{drag}}\ \text{on the floor's 2-simplices}];$$
$$\text{EW fourth-root lattice: Gaussian-integer entries throughout}\ [\mathrm{AT.57}(7)\ \text{'s economy at the global level}];\qquad\textbf{no continuous locus, no eighth root — globally as locally}$$
$$(8)\quad\textbf{THE INDEX READS (seed-only branch):}\qquad\Gamma^2=I_{32},\ \ \{\mathfrak D_{\mathrm{floor}},\Gamma\}=0\ \text{re-verified at}\ 32\times32\implies\text{the spectrum is}\ \pm\text{-paired, the kernel}\ \Gamma\text{-stable};$$
$$\text{kernel nullities on the four witness profiles:}\ \ \{\mathrm{flat}{:}0,\ \mathrm{drag}{:}0,\ \mathrm{ewlat}{:}0,\ \mathrm{pyth}{:}0\}\ \ [\text{exact ranks by elimination over}\ \mathbb Q(i)]\ \text{— the witnesses are invertible; the pairing theorem is the structural content};$$
$$\text{the DIAGONAL branch provably has none of these reads}\ ((4)\ \text{'s nullity 0): no grading, no pairing, no index}$$
$$(9)\quad\textbf{THE VIELBEIN SLOT (new, named):}\qquad\mathrm{Rot}\ \text{acts TRANSITIVELY on the}\ 6\ \text{undirected edges}\ (72\ \text{rotation-edge images, one orbit)}\implies\text{an equivariant labeling}\ a(e)\ \textbf{is CONSTANT, and a constant labeling degenerates the Clifford structure};$$
$$\boxed{\ \textbf{the global operator NECESSARILY breaks the floor symmetry to the labeling's stabilizer: the discrete vielbein is a THIRD enumerated datum}\ (4^6=4096\ \text{labelings on}\ K_4)\ }\qquad\text{derived rows verified labeling-independent}\ (3\ \text{witnesses: modular, perfect-matching, asymmetric)}$$
$$(10)\quad\textbf{status:}\qquad\boxed{\ \textbf{AT-O28 CLOSED AS CONSTRUCTION}\ }\qquad\text{the operator is built as an explicit finite family}\ (2\ \text{lift readings}\times6\ \text{frames}\times4096\ \text{vielbeins}\times\ \text{P4-class profiles)};\ \text{slot (b) dissolved}\ (5);\ \text{slot (a) physical and dichotomous}\ (4);\ \text{slot (c) discovered and named}\ (9);$$
$$\textbf{residue (declaration/calibration species,}\ \neg\textbf{math): the lift declaration itself}\ [\mathrm{Def\text{-}H.37}(2)],\ \text{the vielbein choice},\ \text{the P4 transport profile}\ (\ell_c,\mathbf c)\ [\mathrm{AT.47}(6),(9)(\mathrm{iii})],\ \text{and the per-floor extension census}\ (\text{new}\ \mathrm{AT\text{-}O32});$$
$$\text{the recipe is derived for EVERY arc-transitive floor}\ [\mathrm{AT.34}(3)];\qquad\text{the smooth Dirac operator stays a dictionary partner,}\ \neg\text{an equal}\ [\mathrm{BM.134}(5)];\qquad\neg\text{a declaration issued},\ \neg\text{a P4 value},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** A3, A8 (Part 1); P1, P4, P5, CT1.1, EW.32 (Part 2); Def-H.33, Def-H.34, Def-H.37(2), FT.93(1),(2),(3),(4),(7), FT.157(1) (Part 3); AT.10, AT.34(1),(2),(3),(4), AT.46(5),(6), AT.47(3),(4),(5),(6),(8),(9), AT.48(3), AT.56(4),(6), AT.57(2),(4),(7), AT.58 (this level); AT-O28 (this level); BM.134(5) (Part 4); exact $32\times32$ `Gauss(i)` arithmetic, $\mathbb Z[i]/2$ group tables, exact nullities by elimination, Kronecker block algebra [math; machine: `global_dirac.py` §§A–E, 12/12].

**Pf.**
$$(1):\ \text{the frame enumeration, the}\ 2T\ \text{closure and determinants, the}\ 24\ \text{Ad-images matched 2-to-1 onto}\ \texttt{tet\_rotations()},\ \text{the}\ 12/12\ \text{arc bijection}\ [\text{machine A1--A3}];$$
$$(2),(3):\ \text{the 144 fixed-point checks; the orbit census}\ 2\times3;\ \text{the section's 12-direction image; Hermiticity on every censured operator}\ [\text{machine B1, D1}];$$
$$(4):\ \text{the nullity systems}\ (6+2)\ \text{by exact elimination over}\ \mathbb Q(i);\ \text{the grading-direction census via fourth-root normalization}\ [\text{machine B2}];\ \text{gauge-invariance: nullity is a similarity invariant}\ [\text{math}];$$
$$(5):\ \text{the 105 automorphism identities; the}\ \Phi\text{-orbit walk; the}\ 6\ \text{conjugation identities at}\ 8\times8\ [\text{machine C1,C2}];$$
$$(6):\ \text{the}\ 24\ \text{diagonal and}\ 48\ \text{off-diagonal block identities across}\ 4\ \text{profiles; the flat-vs-Pythagorean diagonal equality}\ [\text{machine D2}];$$
$$(7):\ \text{the}\ 16\ \text{closed-triangle holonomies}\ [\text{machine D3}];\ (8):\ \Gamma^2,\ \text{the anticommutators, the}\ 4\ \text{exact ranks}\ [\text{machine D1, D4}];\ (9):\ \text{the edge-orbit census}\ [\text{machine E1}];\ (10):\ \text{assembly}.\ \blacksquare$$

**Phys.** The corpus's oldest declared slot just paid rent. The global Dirac-type operator — the
object three tiers had circled, "two slots away" since the frame section — is built: a
32-dimensional Hermitian operator on the tetrahedral floor, a finite explicit family over the
two lift readings, the six-frame menu, the labelings and the transport profiles, every derived
property verified entrywise. And building it adjudicated the slots with unexpected sharpness.
The base frame turned out not to matter at all: the S-transform — derived, not declared — walks
the menu in one orbit of three times a sign, and conjugates any choice's operator into any
other's, so the six-frame menu collapses to a single unitary class. The lift turned out to matter
maximally: the space of global gradings is a gauge invariant, and it is one-dimensional for the
seed-only reading and empty for the diagonal one — the first gives a chiral-odd operator with a
±-paired spectrum and honest kernel reads, the second gives no grading, no pairing, no index. The
declaration the corpus has owed since Open Gaps 19 is no longer a formality: *it decides whether
the global operator has an index.* And the construction exposed a third datum nobody had named —
the edge labeling, the discrete vielbein — which cannot be made equivariant because the rotation
group moves every edge to every other: the global operator necessarily breaks the floor's
symmetry. Its square is the cleanest row of the tier: the degree Laplacian, transport-blind, plus
pure triangle blocks — all the curvature of the global square lives on the 2-simplices, with the
drag profile reading integer windings on the closed triangles and the electroweak lattice reading
Gaussian integers, exactly the local economy of the previous tier, now on the floor. What
remains is declaration and calibration, named to the symbol, and one census row for the other
floors.

---

### AT.61 — AT-O31 resolved as grammar and AT-O6 closed outright: the fine-splitting law, the composed read, and the exhaustive seat census

**Thm.**
$$(1)\quad\textbf{GATES (re-produced,}\ \neg\textbf{new):}\qquad\mathsf S^\pm_i=\mp(\sigma_i\otimes I_2)P_\pm,\ \ [\mathsf S^\pm,\mathsf S^\pm]=\mp2i\varepsilon\mathsf S^\pm,\ \ [\mathsf S^+,\mathsf S^-]=0,\ \ P_+P_-=0\ [\mathrm{AT.56}(6)];\qquad\hat\omega\hat\kappa\hat\omega=-\hat\kappa,\ \ \{\hat\kappa,\hat\chi\}=0\ [\mathrm{Def\text{-}H.34}];$$
$$\widehat M=-q(I\otimes\hat\kappa),\quad\{\widehat M,\hat\chi\}=0,\quad\widehat M^2=q^2I_4\ \ [\mathrm{AT.48}(2\mathrm a),(4),(5\mathrm i)\ \text{re-certified at}\ q{=}1]$$
$$(2)\quad\textbf{THE CASIMIR PER RAY:}\qquad\boxed{\ \textstyle\sum_i(\mathsf S^\pm_i)^2=3\,P_\pm\ \ \textbf{EXACTLY}\ }\qquad\text{each ray of the orientation doublet carries a full spin-}\tfrac12\ \ \mathfrak{su}(2)\ \text{at scale}\ {-}2\ \ (\text{Casimir}\ 4\cdot\tfrac34=3,\ \text{an INTEGER});$$
$$\text{identification with any measured multiplet QUARANTINED}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7);\ \mathrm{BM.124}(4)\ \text{'s ladder untouched}]$$
$$(3)\quad\textbf{THE SPLITTING LAW:}\qquad P_+e_aP_+=-(\sigma_a\otimes P_+)\ \ \text{vs}\ \ P_-e_aP_-=+(\sigma_a\otimes P_-)\ \ \text{— the electric ray blocks are}\ \hat\omega\text{-CONJUGATE NEGATIVES};\qquad P_\pm W_cP_\pm=W_cP_\pm\ \ \text{— the magnetic channel acts IDENTICALLY within both rays};$$
$$\boxed{\ \textbf{the born Pauli term}\ [\mathrm{AT.57}(2),(4)]\ \textbf{SPLITS the two rays in OPPOSITE directions through its electric curvature feed}\ \mathfrak E_a\ \textbf{and SHIFTS them COMMONLY through its magnetic curl feed}\ \mathfrak B_c\ }$$
$$\textbf{— the ledger's}\ j=l\pm\tfrac12\textbf{-type DOUBLET GRAMMAR: a structural parallel, FLAGGED,}\ \neg\textbf{IDENTIFIED}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)]$$
$$(4)\quad\textbf{THE WITNESS (the AT.57(E4ii) profile}\ T=(i\sigma_1,i\sigma_2,I,i\sigma_3),\ \text{rebuilt from scratch):}\qquad\text{the born term is BLOCK-DIAGONAL on the rays}\ (\text{cross blocks zero};\ \mathrm{born}=\mathrm{born}_++\mathrm{born}_-\ \text{exactly});$$
$$\mathrm{born}_\pm=\mathrm{mag}_\pm+\mathrm{ele}_\pm\ \ \text{with the conjugation laws}\ \ \mathrm{mag}_-=+\hat\omega\,\mathrm{mag}_+\hat\omega,\quad\mathrm{ele}_-=-\hat\omega\,\mathrm{ele}_+\hat\omega\qquad[\text{exact}\ 8\times8\ \text{integer identities}];$$
$$\text{the spectrum of the electric half is EXACTLY NEGATED between the rays}$$
$$(5)\quad\textbf{THE QUANTIZED SPLITTING CENSUS:}\qquad\text{over the fourth-root transport lattice}\ [\mathrm{AT.57}(7)]:\ 12\ \text{live electric feeds}\ \mathfrak E_a=[T_a,T_4]\ (66\ \text{pairs, zero criterion exact}),\ \textbf{EVERY ray-splitting value a Gaussian integer}\times2;$$
$$\boxed{\ \textbf{NO CONTINUOUS SPLITTING LOCUS before any measure}\ }\qquad[\mathrm{AT.54}(6)\ \text{'s no-go at the splitting level; the eighth root never appears}\ [\mathrm{Def\text{-}BM.16}(5)]]$$
$$(6)\quad\textbf{THE COMPOSED FINE GRAMMAR (AT-O31 resolved):}\qquad\text{a ladder level of the hydrogen connector carries the product structure}$$
$$\bigl(\text{position}\ W_d=1/(d^2x_+x_-),\ \textbf{UNMOVED}\ [\mathrm{AT.44}(5);\ \mathrm{AT.54}(3)]\bigr)\ \times\ \bigl(\text{ray phases}\ i^{\Theta_\pm}\ [\mathrm{AT.46}(5),(6)]\bigr)\ \times\ \bigl(\text{common magnetic shift}\ \pm\ \text{opposite electric splitting}\ (3),(4)\bigr)\ \times\ \bigl(\text{sector intensities}\ [\mathrm{AT.52}(1);\ \mathrm{AT.54}(1),(2)]\bigr);$$
$$\textbf{witness cell (exact):}\ \ (\Theta_+,\Theta_-)=(18,24)\to(i^{18},i^{24})=(-1,+1)\ \text{— OPPOSITE STATISTICS CLASSES on one materialized geometry}\ [\mathrm{AT.46}(6)\ \text{'s witness B}];$$
$$\text{the theta-cell intensities}\ Z^{\mathrm{amp}}/Z^{\mathrm{norm}}=(128,256,128)/(288,576,288)=\tfrac49\ \textbf{UNIFORMLY — a}\ q\text{-blind attenuation}\ [\mathrm{AT.54}(2)\ \text{'s frozen integers, re-cited}];$$
$$\boxed{\ \textbf{fine structure in this corpus is a RAY/SECTOR SPLITTING AT UNMOVED PRICES — AT.54(3)'s Lamb-analog logic one level down}\ }\qquad\text{values behind}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ [\mathrm{AT.54}(6)]:\ \neg\text{converted},\ \neg\text{compared}\ [\mathrm{P5}]$$
$$(7)\quad\textbf{THE EXHAUSTIVE SEAT CENSUS (AT-O6):}\qquad\text{the Pauli algebra's 8 directions}\ [\mathrm{AT.56}(7)];\ \ I_4\ \text{spectrally inert (adding}\ cI_4\ \text{leaves the splitting set}\ \{0,\pm2\}\ \text{EXACTLY — four}\ c\ \text{witnesses});\ \text{the contraction image re-censured: hit directions EXACTLY the 3 magnetic + 3 electric,}\ (0,3)\ \text{and}\ (0,0)\ \text{components zero in every contraction, and}\ \widehat M\ \text{purely}\ (0,3);$$
$$\begin{array}{l|l|l}\textbf{the seat}&\textbf{the feed}&\textbf{status}\\\hline\kappa\ \text{(boundary moment}\ \widehat M)&\text{the scalar EM boundary read}\ q\ [\mathrm{AT.48}(2\mathrm a);\ \mathrm{EM.9b}]&\textbf{constructed}\\(-1)^{\aleph}\ \text{(dressing)}&\text{the frozen A8 weight}\ [\mathrm{Def\text{-}H.32}(2);\ \mathrm{AT.48}(2\mathrm b);\ \mathrm{AT.53}(5)]&\textbf{constructed}\\W_c\ \text{(magnetic functional, 3)}&\text{the shift}\ w_i\ \text{alone}\ [\mathrm{AT.2}(4);\ \mathrm{FT.157}(1);\ \mathrm{AT.6}\ \text{up to}\ \varkappa\beta,\ \mathrm{AT.34}]&\textbf{constructed (marked (S))}\\e_a\ \text{(born Pauli, 3)}&\text{the transport curvature}\ \mathfrak E_a=[T_a,T_4]\ [\mathrm{AT.57}(4)]&\textbf{constructed (marked profile)}\\\sigma_c\otimes I_2\ (3)&\neg\text{a linear seat: products}\ e_a\kappa\ \text{and}\ \mathsf S^\pm\ \text{supports only}\ [\mathrm{AT.56}(3),(6)]&\textbf{proved absent}\end{array}$$
$$(8)\quad\textbf{the impossibility rows close the census:}\ \ \neg\text{a native index-carrying EM read}\ [\mathrm{AT\text{-}O29};\ \mathrm{AT.48}(3);\ \text{the grade reason}\ \mathrm{AT.56}(5)];\quad\neg\widehat M\ \text{from any bivector contraction (grade separation}\ [\mathrm{AT.56}(5)]);$$
$$\neg\text{a third channel}\ [\mathrm{AT.56}(4)];\qquad\neg\text{loops}\ [\mathrm{BM.88}(1)];\qquad e\ \neg\text{issued}\ [\mathrm{EM.25}(7)];\qquad\neg\text{a continuous locus}\ [\mathrm{AT.53}(3);\ \mathrm{AT.54}(6);\ \mathrm{AT.57}(7);\ (5)\ \text{here}];$$
$$\boxed{\ \textbf{FOUR SEATS, ALL CONSTRUCTED, NO UNNAMED DIRECTION LEFT — AT-O6 CLOSED OUTRIGHT}\ }\qquad\text{the continuous anomaly number remains calibration-species BY DESIGN}\ [\mathrm{P5}]$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (2)\text{--}(8);\qquad\textbf{resolved as grammar:}\ \mathrm{AT\text{-}O31}\ (\text{values behind}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ \text{and the AT-O28 declaration residue});\qquad\textbf{closed outright:}\ \mathrm{AT\text{-}O6};$$
$$\textbf{untouched:}\ \mathrm{BM.125}(4)\ \text{(the new objects are operator-valued, dimensionless,}\ \neg\text{mass-products)},\ \mathrm{BM.126}(1)\ \text{(the}\ \{\varepsilon_q\}\ \text{alphabet unrewighted)},\ \mathrm{FT.55}(1),\ \mathrm{BM.134}(5)\ (\text{dictionary partners only});\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** A8 (Part 1); P4, P5, CT1.1, EW.32, EM.9b, EM.25(7) (Part 2); Def-H.32(2), Def-H.33, Def-H.34, FT.93(1),(2), FT.157(1) (Part 3); AT.2(4), AT.6, AT.34, AT.44(5), AT.46(5),(6), AT.47(3),(7), AT.48(2),(3),(4),(5), AT.52(1), AT.53(3),(5), AT.54(1),(2),(3),(6), AT.56(3),(4),(5),(6),(7), AT.57(2),(4),(7), AT.60 (this level); AT-O6, AT-O29, AT-O31 (this level); Def-BM.3(7), Def-BM.5(1), Def-BM.16(5), BM.88(1), BM.124(4), BM.125(4), BM.126(1), BM.134(5) (Part 4); exact `Gauss(i)` ray-block algebra, integer Casimir census, `Fraction` weights [math; machine: `fine_structure.py` §§A–D, 8/8].

**Pf.**
$$(1):\ \text{the ray supports and commutators, the triple's rows,}\ \widehat M^2\ \text{and the chirality flip entrywise}\ [\text{machine A1,A2}];\ (2):\ \text{the two}\ 4\times4\ \text{Casimir identities}\ [\text{machine B1}];$$
$$(3):\ \text{the 12 ray-block identities (electric conjugate-antisymmetry, magnetic symmetry)}\ [\text{machine B2}];\ (4):\ \text{the witness born term rebuilt via}\ \sigma^{ab}\ \text{from scratch; block-diagonality; the two conjugation laws}\ [\text{machine B3}];$$
$$(5):\ \text{the 66-pair lattice census with the ray-block integrality test}\ [\text{machine B4}];\ (6):\ \text{the fourth-root phase arithmetic}\ i^{18}{=}{-}1,\ i^{24}{=}{+}1;\ \text{the uniform}\ \tfrac49\ \text{row from the frozen integers}\ [\text{machine C1}];$$
$$(7),(8):\ \text{the image re-census (6 decompositions}\times16\ \text{coefficients), the inertness witnesses, the seat table assembly}\ [\text{machine D1}];\ (9):\ \text{the record rows}.\ \blacksquare$$

**Phys.** Fine structure asked for a number and got a grammar — and the grammar is the honest
answer at this side of the calibration boundary. The ledger's rays, which the boundary moment
flips and the born Pauli term never crosses, each carry their own closed spin algebra with an
integer Casimir; the electric half of the curvature coupling treats the two rays as exact
ω̂-conjugate negatives while the magnetic half treats them alike — so every live curvature on the
fourth-root lattice splits the doublet in opposite integer steps and shifts it commonly, the
structural shadow of a j-doublet, flagged and never named. Composed with the statistics phases —
witnessed at the very lattice point where one geometry's two orientations sit in opposite
statistics classes — and with the measure's uniform four-ninths attenuation on the theta cell,
the level read is fourth-root times integer times rational at prices the dressing provably never
moves: fine structure here is a ray/sector splitting at unmoved positions, the Lamb-analog logic
of the previous tier applied one level down. The second verdict closes the era's founding
question outright. The moment sector's seat census is now exhaustive: of the Pauli algebra's
eight directions one is inert, three have no linear seat by theorem, and the remaining four are
the constructed seats — the boundary charge, the A8 dressing sign, the shift-fed magnetic
functional, and the curvature-born Pauli channel — each with its native feed named and every
alternative excluded with its ground. There is no unnamed place left for an anomalous moment to
hide; what remains missing is a read rule, a threshold value and a scale, and those are
declarations, not structures.

---

### AT.62 — The status of Tier AT.11: the four resolutions, the corrected framings, and the state of the Atomic era

**Thm.**
$$(1)\quad\textbf{the consolidated ledger of the tier:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{the disposition}\\\hline(\mathrm{AT\text{-}O11})\ \text{the dictionary}&\textbf{CLOSED: the conjugacy table complete at every level — image = volume alone; genus = the}\ r_n\ \text{pair bits}\ (1,3,6);\ \text{kernel = exchange coherences; the nine ``none'' rows are theorems}\ [\mathrm{AT.59}]\\(\mathrm{AT\text{-}O28})\ \text{the global Dirac operator}&\textbf{CLOSED AS CONSTRUCTION: built on the tetrahedral floor as an explicit finite family; slot (b) DISSOLVED (derived gauge); slot (a) PHYSICAL (the index dichotomy); slot (c) the vielbein DISCOVERED AND NAMED; residue = declarations + calibration +}\ (\mathrm{AT\text{-}O32})\ [\mathrm{AT.60}]\\(\mathrm{AT\text{-}O31})\ \text{the fine-structure read}&\textbf{RESOLVED AS GRAMMAR: the composed splitting law derived and quantized; values behind}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ [\mathrm{AT.54}(6)]\ +\ \text{the AT-O28 residue}\ [\mathrm{AT.61}]\\(\mathrm{AT\text{-}O6})\ \text{the anomalous moment}&\textbf{CLOSED OUTRIGHT: the seat census exhaustive — four constructed seats, every other direction impossible with its ground}\ [\mathrm{AT.61}(7),(8);\ \text{structure}\ \mathrm{AT.48};\ \text{dressed}\ \mathrm{AT.53}/\mathrm{AT.54};\ \text{anatomy}\ \mathrm{AT.56}/\mathrm{AT.57}]\\\textbf{new}\ (\mathrm{AT\text{-}O32})&\text{the per-floor extension census of}\ \mathfrak D_{\mathrm{floor}}\ \text{(the other four platonic floors + the polygon ladder; the recipe is derived}\ [\mathrm{AT.60}(10);\ \mathrm{AT.34}(3)]);\ \textbf{blocking nothing}\end{array}$$
$$(2)\quad\textbf{THE PROVED ABSENCES (each with its ground):}\qquad\begin{array}{l|l}\textbf{absence}&\textbf{the ground}\\\hline\neg\text{a carrier conjugate for conformal/shear/shift at ANY level}&\text{the embedding census: only}\ \Sigma\ \text{and the trace-fixed}\ E_0\ \text{pass AT.12(1)'s test}\ [\mathrm{AT.59}(4)]\\ \neg\text{new metric coordinates from the Catalan growth}&\text{the supply is exchange content: the commutant IS the permutation span}\ [\mathrm{AT.59}(1),(6)]\\ \neg\text{a gauge equivalence of the two lift readings}&\text{the grading nullity is a similarity invariant:}\ 1\ \text{vs}\ 0\ [\mathrm{AT.60}(4)]\\ \neg\text{an equivariant vielbein on}\ K_4&\mathrm{Rot}\ \text{transitive on the edges}\ [\mathrm{AT.60}(9)]\\ \neg\text{transport content in the global square's diagonal}&\gamma^2=I\ \wedge\ TT^\dagger=I\ \text{blockwise}\ [\mathrm{AT.60}(6)]\\ \neg\text{a continuous splitting locus}&\text{the lattice census: Gaussian integers}\times2\ [\mathrm{AT.61}(5)]\\ \neg\text{a linear seat for}\ \sigma_c\otimes I_2&\text{the contraction image census}\ [\mathrm{AT.56}(4);\ \mathrm{AT.61}(7)]\\ \neg\text{an unnamed moment seat}&\text{the exhaustive census of}\ \mathrm{AT.61}(7),(8)\end{array}$$
$$(3)\quad\textbf{CORRECTED / SHARPENED ON THE RECORD:}\qquad\begin{array}{l|l}\textbf{the row}&\textbf{the disposition}\\\hline\text{the ``13 free invariants vs 26-dimensional mask space'' framing}\ [\mathrm{AT.40}(5);\ \mathrm{AT.50}(6)]&\textbf{CORRECTED: a cross-currency count}\ [\mathrm{BM.83}\ \text{discipline}]\ \text{— the conjugacy question runs through the embedded generators, and its answer is AT.59(4)'s table; both frozen loci stand untouched}\\ \mathrm{AT.47}(4)\ \text{'s ``one S-orbit''}&\textbf{SHARPENED at the frame-element level: the}\ \Phi\text{-orbit on FRAMES has size 3; the menu is}\ 3\times2\ \text{(orbit}\times\text{sign involution)}\ [\mathrm{AT.60}(5)]\\ \mathrm{AT.15}(5)\ \text{'s ``none'' rows}&\textbf{PROMOTED from pair-arena census to theorem at every level}\ [\mathrm{AT.59}(4)]\\ \mathrm{AT.56}(6)\ \text{'s ray blocks}&\textbf{corrected in-session before record: the electric ray blocks are}\ \hat\omega\text{-conjugate negatives,}\ \neg\text{summing to zero}\ [\mathrm{AT.61}(4)\ \text{'s witness form}]\\\texttt{frame\_section}\ \text{'s residue (iv)}&\textbf{DISCHARGED: the evaluation gap it named is now the declaration residue of}\ \mathrm{AT.60}(10)\ [\mathrm{AT.58}(3)\ \text{'s rescope, completed}]\end{array}$$
$$(4)\quad\textbf{MARKED,}\ \neg\textbf{ADOPTED (unchanged; none new adopted):}\qquad(\mathrm a)\ \ \text{the lift}\ \triangleright\ [\mathrm{AT.47}(5);\ \mathrm{Def\text{-}H.37}(2)\ \text{— now with its exact physical content, AT.60(4)}];\qquad(\mathrm b)\ \ \text{the vielbein}\ a(e)\ [\mathrm{AT.60}(9),\ \textbf{new enumerated datum,}\ \neg\textbf{adopted}];$$
$$(\mathrm c)\ \ \text{the P4 transport profile}\ (\ell_c,\mathbf c)\ [\mathrm{AT.47}(6),(9)(\mathrm{iii})];\qquad(\mathrm d)\ \ (S)\ \text{and AT.6's functional up to}\ \varkappa\beta\ [\mathrm{AT.34}(7)];\qquad(\mathrm e)\ \ \text{the level-price read rule}\ [\mathrm{AT.44}(8\mathrm{iv})]$$
$$\text{the base frame per floor is REMOVED from the marked list: DISSOLVED as derived gauge}\ [\mathrm{AT.60}(5)]\ \text{— the first slot ever retired by construction}$$
$$(5)\quad\textbf{THE OPEN LEDGER at this closure — the shortest of the era:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{why}\\\hline(\mathrm{AT\text{-}O2})\ w_i^\perp\ \text{gauge}&\textbf{BY NATURE}\ [\mathrm{AT.5}(4),\ \text{unchanged}]\\(\mathrm{AT\text{-}O3})\ (\varkappa,\beta)&\textbf{BY DESIGN: P4 core},\ \neg\text{issued}\ [\mathrm{AT.49}(5),\ \text{unchanged}]\\(\mathrm{AT\text{-}O7})\ \mathrm{BM.140}(6)\ \text{'s pin}&\textbf{the convention row}\ [\mathrm{AT.7};\ \mathrm{AT.40}(7),\ \text{unchanged}]\\(\mathrm{AT\text{-}O13})\ \text{the Kerr route}&\textbf{ONE NUMBER AWAY: needs}\ (\mathrm{AT\text{-}O3})\ [\mathrm{AT.34},\ \text{unchanged}]\\(\mathrm{AT\text{-}O26})\ \text{the read-rule declaration}&\textbf{CLOSURE-PHASE ACT}\ [\mathrm{AT.44}(8\mathrm{iv})];\ \text{the gate of}\ (\mathrm{M1'})\ [\mathrm{AT.54}(6)]\\(\mathrm{AT\text{-}O27})\ \varepsilon_q\ \text{'s value}&\textbf{CALIBRATION:}\ \tfrac18\ \text{distinguished five ways}\ [\mathrm{AT.40}(1);\ \mathrm{AT.44}(4),(5);\ \mathrm{AT.54}(1)],\ \text{adoption}\ \neg\text{issued}\ [\mathrm{P5}]\\(\mathrm{AT\text{-}O29})\ \text{a native vector EM read}&\textbf{BY NATURE (proved absence)}\ [\mathrm{AT.48}(3);\ \mathrm{AT.56}(5)\ \text{'s grade reason}]\\(\mathrm{AT\text{-}O30})\ \text{the}\ B\ge5\ \text{cover census}&\textbf{OPEN, blocking nothing}\ [\mathrm{AT.52}(4)\text{--}(6);\ \mathrm{AT.55}(5)]\\\textbf{new}\ (\mathrm{AT\text{-}O32})\ \text{the per-floor extension census}&\textbf{OPEN, blocking nothing: the recipe is derived}\ [\mathrm{AT.60}(10);\ \mathrm{AT.34}(3)]\end{array}$$
$$\textbf{CLOSED at this tier:}\ (\mathrm{AT\text{-}O6})\ \text{outright},\ (\mathrm{AT\text{-}O11}),\ (\mathrm{AT\text{-}O28})\ \text{as construction},\ (\mathrm{AT\text{-}O31})\ \text{as grammar};\qquad\textbf{closed earlier:}\ \mathrm{AT\text{-}O1},\ \mathrm{O4},\ \mathrm{O5},\ \mathrm{O8},\ \mathrm{O9},\ \mathrm{O10},\ \mathrm{O12},\ \mathrm{O14},\ \mathrm{O15},\ \mathrm{O16},\ \mathrm{O17},\ \mathrm{O18},\ \mathrm{O19},\ \mathrm{O20},\ \mathrm{O21},\ \mathrm{O22},\ \mathrm{O23},\ \mathrm{O23b},\ \mathrm{O24},\ \mathrm{O25},\ \mathrm{AT.43}(\mathrm{R3})$$
$$(6)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)];$$
$$\text{calibration parameters added:}\ 0;\qquad\text{marked rows:}\ (4)\ \text{'s five}\ (\text{one added — the vielbein — one retired — the base frame});\qquad\text{claims withdrawn:}\ 0;\qquad\text{rows closed:}\ 4;\qquad\text{new open rows:}\ 1\ (\mathrm{AT\text{-}O32})$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{era2/level5\_atomic/checks/run\_all\_era2.py}\to\textbf{37 checkers, 643 exact markers, 0 failures, exit 0};\qquad\texttt{check\_era2\_format.py}\to\textbf{13 Part 5 documents PASS};$$
$$\text{the shared libraries:}\ \texttt{qexact.py},\ \texttt{duality.py}\ (\text{its}\ \texttt{tet\_rotations}/\texttt{tet\_arcs}\ \text{now load-bearing at AT.60});\qquad\text{the folder remains deliberately NOT wired into}\ \texttt{verification/run\_all.py};\ \ \texttt{index/},\ \texttt{tags.json},\ \texttt{Summary.md}\ \neg\text{regenerated}$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every AT-tag of this tier cites Parts 1--4 and earlier AT-tags only.}\ \neg\exists\ \text{a forward pointer used as a premise.}\ \neg\exists\ \text{a circular citation. Acyclic by construction}\ [\text{machine: the format gate's F3}]$$
$$(9)\quad\textbf{THE STATE OF THE ATOMIC ERA:}\qquad\text{the era chain, fifth consolidation:}$$
$$\text{grammar}\ [\mathrm{AT.41}]\to\text{dynamics}\ [\mathrm{AT.42}]\to\text{resolvent, price, spectrum}\ [\mathrm{AT.44}]\to\text{drag, statistics flip}\ [\mathrm{AT.46}]\to\text{frame section}\ [\mathrm{AT.47}]\to\text{moment coupling}\ [\mathrm{AT.48}]\to\text{curl}\ [\mathrm{AT.51}]\to\text{dressed vertex}\ [\mathrm{AT.53},\mathrm{AT.54}]\to\text{Pauli anatomy}\ [\mathrm{AT.56},\mathrm{AT.57}]$$
$$\to\textbf{the resolutions:}\ \text{the dictionary complete}\ [\mathrm{AT.59}],\ \text{the global operator built}\ [\mathrm{AT.60}],\ \text{the fine grammar composed and the moment sector sealed}\ [\mathrm{AT.61}];$$
$$\textbf{the open ledger now contains NO structural row:}\ \text{two by-nature/by-design}\ (\mathrm{AT\text{-}O2},\mathrm{O3}),\ \text{one convention}\ (\mathrm{AT\text{-}O7}),\ \text{one calibration-gated}\ (\mathrm{AT\text{-}O13}),\ \text{two closure-phase declarations}\ (\mathrm{AT\text{-}O26},\mathrm{O27}),\ \text{one proved absence}\ (\mathrm{AT\text{-}O29}),\ \text{two censuses}\ (\mathrm{AT\text{-}O30},\mathrm{O32});$$
$$\text{between Level 5 and contact stand exactly:}\ \varepsilon_q,\ e_0,\ (\varkappa,\beta),\ \text{the chart-side scales},\ \text{the read rules}\ (\mathrm{M1'})\text{--}(\mathrm{M3'}),\ \text{and the lift declaration — ALL declaration/calibration species};$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and this tier makes no contact claim}\ }\qquad[\mathrm{AT.39}(8)\ \text{'s standing row, re-cited and unchanged}]$$

**Req.** AT.59, AT.60, AT.61 (this level); AT.5(4), AT.7, AT.34(3),(7), AT.39(8), AT.40, AT.44(5),(8), AT.46, AT.47, AT.48, AT.49(5), AT.50(5),(6), AT.52, AT.53, AT.54, AT.55(5), AT.56, AT.57, AT.58(3), AT-O1 … AT-O32 (this level, row-wise); P1, P4, P5, A3, A8, CT0.5, CT0.6, CT0.11, CT0.12, CT1.1, CT1.2, CT1.12, EW.32, EM.9b, EM.25(7) (Parts 1–2); Def-H.32(2), Def-H.33, Def-H.34, Def-H.37(2), FT.93, FT.157(1) (Part 3); Def-BM.3(7), Def-BM.5(1), Def-BM.16(5), BM.83, BM.88(1), BM.124(4), BM.125(4), BM.126(1), BM.128(8), BM.131(6), BM.134(5) (Part 4); row-wise assembly only — no new mathematics at this tag [math; machine: the three session checkers (13/13, 12/12, 8/8) + the suite + the format gate].

**Pf.** Row-wise assembly of AT.59–AT.61, each row re-citing its own machine section and its own
locus; the format gate re-run over all thirteen Part 5 documents; the suite re-run end to end. No
new mathematics is introduced at this tag. $\blacksquare$

**Phys.** Four rows went in and one came out. The dictionary question — the era's oldest count —
resolved into a single theorem with a table: only volume has conjugates, one pair bit per pair of
carriers, their sum exactly the total-spin Casimir, and all the Catalan surplus flowing into
exchange reads no metric coordinate can see; the higher carriers see more of each other, not more
of the metric. The global operator — the object three tiers had circled — got built, and building
it adjudicated its slots: the base frame dissolved into derived gauge, the marked lift turned out
to carry exact physical weight (one reading leaves a global grading and a ±-paired spectrum, the
other leaves nothing, and nullity is a gauge invariant), and a third datum showed up that no
earlier tier had named, because only the global object needs it: the vielbein, which cannot be
made symmetric because the floor's rotations move every edge. Its square is the floor's own
geometry — a transport-blind degree Laplacian and pure triangle curvature, integer windings on
the drag triangles and Gaussian integers on the electroweak ones. Fine structure resolved the
only way this corpus resolves anything before calibration: as a grammar — rays split oppositely
under electric curvature, shift commonly under magnetic, phases and intensities multiply in exact
fourth roots and rationals, and the prices never move. And the moment sector closed outright,
because the census finally has no unnamed cell: four seats, four feeds, every other direction
impossible with its ground. The open ledger of the Atomic era now holds no structural row at all
— only natures, designs, conventions, declarations and two censuses. The contact claim remains,
deliberately, unmade.
