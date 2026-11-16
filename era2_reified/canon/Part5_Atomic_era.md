# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Unified Schema

**Level.** 5. **Era.** 2 (the Atomic era).
**Source.** Merged from three branches:
- **Mainline Discovery Tiers** (AT.1–AT.63): coherence census through Pauli anatomy and resolution tier
- **Canonical Presentation** (AT.1–AT.20): nuclear grammar, lepton floors, atom construction, shells, transitions, closure
- **Disjoint Branch** (DJ_AT.1–DJ_AT.17): singular force on bound channel, masked orbit, per-rung split, scope clock, unified mass, opened structure

**Namespace.** This part owns: Def-AT.1–Def-AT.11; AT.1–AT.63; DJ_AT.1–DJ_AT.17; declarations A-AT.1–A-AT.5, A-DJ_AT.1–A-DJ_AT.2; symbolic-use logs C-AT.1–C-AT.4.

**Unified Tiers** (10 tiers, logical ordering):
- **AT.01**: Capacity Censor & Locked Sector (AT.16–20, DJ_AT.1)
- **AT.02**: Bit/Qubit Tensor Form & CP Tensor (AT.9–15, AT.21–28)
- **AT.03**: Coherence Census & EM Split (AT.1–8)
- **AT.04**: Boundary Invariance & Shell Structure (AT.29–38, DJ_AT.3–4)
- **AT.05**: Hydrogen Spine — EM Sealing Grammar (AT.41–45, AT.1–3, DJ_AT.2)
- **AT.06**: Spin Spine — Duality, Drag, Frames (AT.46–49, DJ_AT.3)
- **AT.07**: Locked Sector, EW Curl, Dressed Vertex (AT.50–55, DJ_AT.5)
- **AT.08**: Pauli Anatomy & Weitzenböck Identity (AT.56–58)
- **AT.09**: Resolution Tier & Unified Structures (AT.59–62, DJ_AT.5–6)
- **AT.10**: Level 5 Closure & Era Transition (AT.63, AT.20, DJ_AT.17)

**DAG law.** Citations resolve to Parts 1–4, Census cells, or earlier tags of this part. Nothing in the canon cites this part.

**Status.** Discovery-phase working tiers. No declarations adopted into frozen canon; §Cal-AT empty; no clause of Parts 1–4 modified. Level 5 closed at AT.63/AT.20/DJ_AT.17.

**Machine.** `era2_reified/verification/checks/verify_Atomic5_6.py` — exact arithmetic throughout: `Fraction`, `ℤ[x]`, multivariate `ℚ[γ,G,a]`, complex-over-`Fraction`, exact 4x4/8x8 matrices, prime-log ring `ℚ[ln2,ln3]`, exhaustive enumeration, `Gauss(i)` elimination.

**No floating point in any assertion. No measured value enters any derivation [P5].**

---

## Tier 5.0 — Composite Vocabulary II: Multi-Baryon Supports and the Nuclear Ledger

### Def-AT.1 — Multi-baryon supports and the nucleus

**Def.** A **multi-baryon support** $\Sigma_A$ is a finite connected vertex set with its interior edges [D2.13] whose sealed configuration carries $A\ge1$ baryon-type $3$-junctures [Def-BM.1: $\varepsilon_{ijk}c_1^ic_2^jc_3^k$ at shared junctions], the junctions disjoint as contractions and the support colour-complete [$\partial_{\mathrm{col}}(\Sigma_A;C)=\varnothing$, D2.14]. The **nucleus** of mass number $A$ and charge class $Z$ is the multi-baryon support with
$$A:=\#\{\varepsilon\text{-junctures}\},\qquad Z:=\#\{\text{constituents in the }q_{\mathrm{net}}=+1\text{ class}\},\qquad A-Z:=\#\{\text{constituents in the }q_{\mathrm{net}}=0\text{ class}\},$$
the counts carried by the additive read of Def-BM.8 on the support's constituent chains. The **matter sector** is $Z\in\{0,\dots,A\}$; the $-1$-class members form the antimatter rows and are admitted only through the CPT-orbit discipline [BM.25; BM.27]. The **validity clause** is Def-BM.1's: every attachment has its contraction partners inside the support; a dangling attachment zeroes the whole colour sector [FT.19]. The **read clause**: each constituent retains its terminus tuple; the support adds the block decomposition, the phase class, the winding ledger and the statistics row — the card is Def-AT.2 (forward pointer, defined below). A **one-baryon support** ($A=1$) is the Part-4 baryon itself [Def-BM.1]; the definition adds structure only at $A\ge2$.

### Def-AT.2 — The nuclear card

**Def.** The **card** of a multi-baryon support refines the composite-card row template [Def-BM.2] with:
$$(1)\ \text{the block-decomposition row: the sealing of }\mathrm{Colour}(\Sigma_A)\text{ partitions the }N=3A\text{ attachments into elementary groups of size }2\ (\delta)\text{ and }3\ (\varepsilon)\qquad[\mathrm{CT3.17a}(1)];$$
$$(2)\ \text{the per-junction rows: one sealing-phase class and lock content per }\varepsilon\text{-juncture}\qquad[\mathrm{BM.2}(1),(4);\ \text{Census FT.49}];$$
$$(3)\ \text{the charge row: }Q(\Sigma_A)=\sum_{\text{chains}}q_{\mathrm{core}}\qquad[\mathrm{Def\text{-}BM.8}(1);\ \mathrm{BM.135}(6)];$$
$$(4)\ \text{the winding ledger: additive under composition}\qquad[\mathrm{FT.34}(3);\ \mathrm{BM.2}(2)];$$
$$(5)\ \text{the statistics row: }\varepsilon(\Gamma)=\prod_a\varepsilon(c_a)\ \text{over the constituent chains}\qquad[\mathrm{BM.136}(3);\ \mathrm{BM.129}(4)];$$
$$(6)\ \text{the count row: }E_{\mathrm{int}}(\Sigma_A)\ \text{with its decomposition into constituent and connector summands}\qquad[\text{Census FT.35}(2);\ \mathrm{BM.21}(1)].$$
Card **values** are derived or Census-cell data at the computed supports; card **grammar** is this definition. No card row is a species identification [P1, P5; Def-BM.3(7)].

### Def-AT.3 — The species-identification layer II (declared, A-AT.2)

**Def.** An extension of Def-BM.3's layer to the multi-baryon tuples of Def-AT.1, recorded under the logged declaration A-AT.2. A name attaches to a derived tuple — (junction grammar, count $A$, charge class $Z$, phase class, statistics) — and carries no datum.
$$(1)\quad\textbf{deuteron}\ :=\ \text{the }A=2\text{ support in the }Z=+1\text{ class (one }+1\text{- and one }0\text{-class baryon)};\qquad\textbf{triton}\ :=\ \text{the }A=3,\ Z=+1\text{ tuple};$$
$$\textbf{alpha particle}\ (\alpha)\ :=\ \text{the }A=4,\ Z=+2\text{ tuple (two }+1\text{- and two }0\text{-class baryons)};$$
$$(2)\quad\textbf{the carried names:}\qquad\textbf{electron},\ \textbf{muon},\ \textbf{tau}\ [\mathrm{Def\text{-}BM.6}(1)]\ \text{and the }\nu\text{-triplet}\ [\mathrm{Def\text{-}BM.6}(2)]\ \text{carry into Part 5 by A-AT.2 with their Part-4 attachments unmodified};$$
$$(3)\quad\textbf{the data bar (standing):}\qquad\text{the names carry }\neg\text{mass value,}\ \neg\text{coupling value,}\ \neg\text{lifetime,}\ \neg\text{radius};\qquad\neg\exists\ \text{a measured external value in any clause}\ [\mathrm{P5}];$$
$$(4)\quad\textbf{scope:}\qquad\text{the new names occur in Part 5 only};\qquad\text{extension beyond A-AT.2's list (e.g. the }Z\ge2\text{ atom classes) requires a further logged declaration};$$
$$\text{the layer adds }\neg\text{dimensionful scale}\ [\mathrm{P1}]\ \text{and}\ \neg\text{P4 parameter}.$$

**Rmk (what the naming waits for).** The deuteron, triton and $\alpha$ are named here on grammar and class alone — the same discipline by which Def-BM.3 named the proton on the $\varepsilon$-seal and the charge class. The name **hydrogen** is withheld until the bound pair exists to carry it: it is issued at Def-AT.4(5) (forward pointer, defined in Tier 5.2), so that no name in this canon ever precedes its referent's grammar.

### AT.1 — The multi-baryon sealing grammar: the $N\ge4$ cells (the demand row (P5.8))

**Thm.**
$$(1)\quad\textbf{the attachment count and the grammar:}\qquad\text{a matter nucleus of mass number }A\text{ presents }N=3A\text{ triplet attachments}\ [\mathrm{D3.8}]:$$
$$\textbf{the all-}\varepsilon\textbf{ cells:}\qquad G_\varepsilon(A):=\#\{\text{partitions of }3A\text{ labelled attachments into }A\text{ unlabelled }3\text{-blocks}\}=\frac{(3A)!}{A!\,(3!)^{A}}\qquad[\mathrm{CT3.17a}(2)\text{'s formula at }b=A,\ a=0]:$$
$$G_\varepsilon(1)=1,\quad G_\varepsilon(2)=10,\quad G_\varepsilon(3)=280,\quad G_\varepsilon(4)=15\,400\qquad[\text{machine: exact factorial arithmetic}];$$
$$\textbf{the consistency row:}\qquad G_\varepsilon(A)=g_\varepsilon(3A)\ \text{on the frozen range}\qquad[\mathrm{BM.31}(2):\ g_\varepsilon(N)\ne0\iff3\mid N;\ g_\varepsilon(3)=1,\ g_\varepsilon(6)=10;\ \text{machine re-run}];$$
$$(2)\quad\textbf{the type-selection clause is the separator:}\qquad\text{every crystallized matter attachment is a triplet }q^i\ [\mathrm{D3.8}];\qquad\delta^i{}_j\text{ consumes one triplet and one antitriplet}\qquad[\mathrm{CT3.17a}(3);\ \mathrm{CT3.17}]:$$
$$\implies\textbf{a type-compatible grouping of }3A\text{ triplet attachments uses }\varepsilon\text{-blocks only, and }3\mid N\text{ is forced}\qquad[\text{machine: the type census on all }g(N)\text{ groupings at }N\le7];$$
$$\text{the mixed }\delta/\varepsilon\text{ cells of }N\ge4\ [\mathrm{BM.31}(2);\ \mathrm{BM.136}(3)]\ \text{are admissible exactly when antitriplet attachments are present — the CP-pair content}\ [\mathrm{Def\text{-}BM.15}]:$$
$$\textbf{the crystallized matter nucleus is all-}\varepsilon\textbf{-sealed; the mesonic }\delta\textbf{-content lives in the flicker ensemble, not in the crystallized skeleton};$$
$$(3)\quad\textbf{the singlet condition at }A=2\text{ and }A=4:\qquad\dim\operatorname{Inv}\bigl((\mathbb C^3)^{\otimes6}\bigr)\ge1\ \text{and}\ \dim\operatorname{Inv}\bigl((\mathbb C^3)^{\otimes12}\bigr)\ge1\qquad[\text{machine: the explicit }\varepsilon\text{-contraction witnesses}];$$
$$\text{against the four-slot no-go:}\quad\dim\operatorname{Inv}\bigl((\mathbb C^3)^{\otimes4}\bigr)=0\qquad[\mathrm{BM.136}(3)\ \text{re-cited}]:\qquad\textbf{no }A\text{ admits a sealed support between the baryon and the next }3\text{-divisible count};$$
$$(4)\quad\textbf{the grammar verdict (P5.8 discharged):}\qquad\text{the }n\ge4\text{ sealing-grammar cells demanded by BM.143(7) are the partition cells }G_\varepsilon(A)\ \text{with CT3.17a's formula and the type selection of }(2);$$
$$\text{the cells are constructed, enumerated and machine-verified; no new count enters any Census cell}\qquad[\text{the Census stays frozen by its charter};\ \mathrm{BM.143}(8)].$$

**Req.** D2.13, D2.14, D3.8, D3.9 (Parts 1–2); CT3.15, CT3.17, CT3.17a(1)–(3), CT3.18 (Part 2); P5 (Parts 1–2); Def-H.32(4) (Part 3); Def-BM.1, Def-BM.15, BM.2(3), BM.31(2), BM.136(3), BM.143(8) (Part 4); Def-AT.1, Def-AT.2 (this part); exact factorial arithmetic, exhaustive type censuses on the frozen grouping range, explicit invariant-tensor witnesses [math; machine: `checks/verify_Atomic5.py` §A].

**Pf.**
$$
(1):\ \mathrm{CT3.17a}(2)\text{'s closed form at }a=0,\ b=A:\ \frac{(3A)!}{A!\,6^A};\qquad\text{the four values by exact factorial arithmetic}\ [\text{machine}];\qquad\text{the }g_\varepsilon\text{ rows re-cited and re-run}\ [\text{machine}]
$$
$$
(2):\ \mathrm{D3.8}\text{'s attachment type per crystallized matter constituent};\qquad\mathrm{CT3.17a}(3):\ \delta\text{ consumes }(\mathbf3,\bar{\mathbf3});\ \varepsilon\text{ consumes }(\mathbf3,\mathbf3,\mathbf3)\implies\text{all-triplet sets admit}\ \varepsilon\text{-blocks only};\qquad3\mid N\ \text{from the block arithmetic}\ [\text{machine}]
$$
$$
(3):\ \text{the explicit witness }\varepsilon_{ijk}\varepsilon_{lmn}\text{ contracted against the }6\text{-fold and }12\text{-fold slot tensors}\ [\text{machine: exact rank}];\qquad\mathrm{BM.136}(3)\text{'s four-slot zero re-cited}
$$
$$
(4):\ \text{the discharge census against}\ \mathrm{BM.143}(7)\text{'s (P5.8) text and the frozen-Census row}\ [\text{machine: the document pins}].\ \blacksquare
$$

**Phys.** The nuclear grammar is the old grammar at a new count. A nucleus of $A$ matter baryons presents three attachments per baryon, every one of them a triplet, and the invariant tensors do the rest: only three-blocks are type-compatible, so the crystallized nucleus is all-epsilon-sealed — ten groupings at the deuteron's six attachments, two hundred eighty at the triton's nine, fifteen thousand four hundred at the alpha's twelve. The delta-blocks that the four-slot no-go makes mandatory in mixed ensembles are not missing from nuclei; they are absent from their skeletons, and live where the corpus already put mesonic content — in the CP-pair fluctuations of the flicker ensemble. Between one baryon and the next admissible count there is nothing: four colour slots admit no singlet, so no two-and-a-bit-baryon object exists. The demand row the closing tier wrote for exactly these cells is discharged by a partition formula that was already frozen.

### AT.2 — The nuclear charge, the statistics, and the $Z$-counter

**Thm.**
$$(1)\quad\textbf{the }Z\textbf{-counter is the additive read:}\qquad Q(\Sigma_A)=\sum_{i=1}^{3A}q_i\ =\ \sum_{\text{baryons}}Q_B\ =\ Z\qquad[\mathrm{Def\text{-}BM.8}(1),(3);\ \mathrm{BM.135}(6)\text{'s block additivity};\ \text{machine: exhaustive on ternary alphabets at }A\le3]:$$
$$\text{the read is integer-valued and defined exactly on the sealed support}\qquad[\mathrm{Def\text{-}BM.8}(4);\ \mathrm{FT.19}];\qquad\tfrac13,\tfrac23\ \text{remain structurally unreachable at every }A\qquad[\mathrm{BM.28}(7);\ \mathrm{BM.135}(4);\ \text{machine: the sum-closure scan at }A\le4];$$
$$(2)\quad\textbf{the statistics at the computed floor:}\qquad\text{each constituent chain at the digon floor carries }k=1\text{ (odd)}\implies\varepsilon_B=-1\ \text{per baryon}\qquad[\mathrm{BM.129}(4),(5);\ \mathrm{FT.32}(6)]:$$
$$\boxed{\ \varepsilon(\Sigma_A)=(-1)^{A}\ \text{at the floor, and }(-1)^{k_1+\dots+k_A}\ \text{in general}\ }\qquad[\mathrm{BM.136}(3)\text{'s product law};\ \text{machine: the parity census at }A\le4\text{ over }k_a\in\{1,2\}]:$$
$$\textbf{the deuteron and the }\alpha\textbf{ are bosons; the }A\textbf{ odd nuclei are fermions — at the floor, derived};$$
$$(3)\quad\textbf{the phase class stacks:}\qquad\Theta_{\mathrm{int}}(\Sigma_A)\in4\mathbb Z\ \text{per baryon-type juncture, additive over junctions}\qquad[\mathrm{BM.2}(1),(2);\ \text{Census FT.49}]:\qquad\Theta_{\mathrm{int}}(\Sigma_A)\in4\mathbb Z;$$
$$(4)\quad\textbf{the CPT mirror:}\qquad\text{the }Z\mapsto-Z\text{ rows are the CP-conjugate supports with identical weights}\qquad[\mathrm{BM.25}(4);\ \mathrm{BM.28}(5):\ W(+1)=W(-1);\ \text{machine: the orbit census}]:$$
$$\textbf{the antinucleus carries no independent datum beyond the orbit — and no annihilation dynamics exists}\qquad[\mathrm{BM.27}(7);\ \mathrm{BM.29}(6)].$$

**Req.** D2.6, D2.11, D3.4 (Parts 1–2); CT0.9 (Part 1); P2, P5 (Parts 1–2); FT.19, FT.32(6) (Part 3); Census FT.49 (row-wise); Def-BM.8, BM.2(1), BM.2(2), BM.25(4), BM.27(7), BM.28(5), BM.28(7), BM.29(6), BM.129(4), BM.129(5), BM.135(4), BM.135(6), BM.136(3) (Part 4); Def-AT.1 (this part); exhaustive ternary enumeration, parity censuses, generating-function convolution [math; machine: `checks/verify_Atomic5.py` §B].

**Pf.**
$$
(1):\ \mathrm{Def\text{-}BM.8}(1)\text{'s read summed over the support's chains with BM.135}(6)\text{'s block law};\qquad\text{the exhaustive census at }A\le3\ \text{and the sum-closure scan at }A\le4\ [\text{machine}]
$$
$$
(2):\ \mathrm{BM.129}(4)\text{'s product law instantiated per baryon and multiplied};\qquad\text{the floor row from the digon's }k=1\ [\mathrm{FT.32}(6);\ \mathrm{BM.129}(5)];\qquad\text{the }2^A\text{ parity census}\ [\text{machine}]
$$
$$
(3):\ \mathrm{BM.2}(1)\text{'s }4\mathbb Z\text{ row per junction, summed}\ [\text{machine: }4\mathbb Z+4\mathbb Z=4\mathbb Z]
$$
$$
(4):\ \mathrm{BM.25}(4)\text{'s orbit rows and BM.28}(5)\text{'s }W(+1)=W(-1)\ \text{re-cited at the support level};\qquad\mathrm{BM.27}(7)\text{'s no-dynamics row re-cited}.\ \blacksquare
$$

**Phys.** Charge and statistics at the nucleus are bookkeeping theorems, and both were already proved — one tier above the atom, on smaller supports. The $Z$-counter is the additive ternary read doing at three-and-twelve attachments what Def-BM.8 certified at three: integer classes only, fractions unreachable, one dangling attachment still fatal. The statistics is the product law doing at $A$ factors what BM.129 certified at three: every baryon at its floor is fermionic, so the parity of the count decides — deuteron and alpha bosonic, odd-$A$ nuclei fermionic — complete as a function at the floor, open as a value per named class exactly where BM.129 left it, pending the winding assignment. The phase classes stack in their lattice, and the antimatter rows mirror without new content: distinct configurations, one orbit, and still no process connecting the sectors.

### AT.3 — The nuclear mass ledger: the count route, the class term, and the isotope rows

**Thm.**
$$(1)\quad\textbf{the count route is exactly additive:}\qquad E_{\mathrm{int}}(\Sigma_A)=6A\qquad[\text{Census FT.35}(2):\ E_{\mathrm{int}}=6\text{ per baryon-type juncture};\ \mathrm{BM.21}(1):\ \text{the informational count is exactly additive};\ \text{machine}]:$$
$$M_{\mathrm{count}}(A)=\frac{6A\ln2}{\mathfrak h}\qquad[\mathrm{FT.44}(4);\ \text{machine: the monomial}];$$
$$(2)\quad\textbf{the class term is the scar monomial, once per charged member:}\qquad m_p=\frac{6\ln2}{\mathfrak h}\bigl(1+c\,\varepsilon_{\mathrm{EM}}\bigr),\qquad \Delta m_{\mathrm{EM}}:=m_p-m_n=\frac{3\,c\,e^2\ln2}{2\pi\,\mathfrak h}>0\qquad[\mathrm{BM.55}(1),(2);\ \mathrm{BM.46}]:$$
$$\boxed{\ M(A,Z)\ =\ \frac{6A\ln2}{\mathfrak h}\ +\ Z\,\Delta m_{\mathrm{EM}}\ }\qquad\text{on the count route with the class term}\qquad[\text{machine: the monomial sum}];$$
$$(3)\quad\textbf{the isotope rows:}\qquad M(A,Z+1)-M(A,Z)=\Delta m_{\mathrm{EM}}>0\ \ \text{exactly, independent of }A\qquad[\text{machine: the difference}];$$
$$\boxed{\ \textbf{the class-ordering row: at fixed }A,\ \text{the mass is strictly increasing in }Z\ \text{on every constructed read}\ }\qquad[\text{machine: }Z\mapsto Z\Delta m_{\mathrm{EM}}\text{ strictly increasing}];$$
$$\text{the ensemble correction is class-blind:}\qquad\mathcal B^{(n)}_{\mathrm{ens}}=-\frac{2n\,u\,D_{n-1}}{D_n}\cdot\frac{\ln2}{\mathfrak h}<0\ \ (u=4\varepsilon_q>0),\qquad\mathcal B^{(n)}_{\mathrm{ens}}\ \text{carries no }Z\qquad[\mathrm{BM.137}(3);\ \mathrm{FT.107}(2)\text{'s }\sigma\text{-freeness}]:$$
$$\textbf{the ordering is untouched by the flicker — the scar is the only class-dependent mass term in the inventory};$$
$$(4)\quad\textbf{the capacity cells:}\qquad r_s(\Sigma_A)=\frac{\mathfrak h\,E_{\mathrm{int}}}{2}=3A\,\mathfrak h\qquad[\mathrm{BM.43}(1);\ \mathrm{BM.148}(3)\text{'s integer census at }E_{\mathrm{int}}\in\{6,12,24\}\ \text{re-read at }A\in\{1,2,4\}]:$$
$$(5)\quad\textbf{the status:}\qquad\text{the ledger is exact and symbolic in }(e,\mathfrak h,\ln2,c);\qquad\neg\text{a measured nuclear mass,}\ \neg\text{a comparison}\ [\mathrm{P5}];\qquad\neg\text{a binding energy attaches to any free member}\qquad[\mathrm{BM.48}(4)\text{'s bar, standing}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P3, P5 (Parts 1–2); FT.44(4) (Census); Census FT.35(2) (row-wise); Def-BM.8, BM.21(1), BM.43(1), BM.46, BM.48(4), BM.55(1), BM.55(2), BM.137(3), BM.148(3) (Part 4); Def-AT.1, Def-AT.2(3),(6), AT.2 (this part); exact Laurent monomial arithmetic, exact rational comparisons [math; machine: `checks/verify_Atomic5.py` §C].

**Pf.**
$$
(1):\ \text{Census FT.35}(2)\text{'s }6\text{ per juncture, }A\text{ times};\qquad\mathrm{BM.21}(1)\text{'s additivity re-cited at the support level};\qquad\mathrm{FT.44}(4)\text{'s law}\implies\text{the monomial}\ [\text{machine}]
$$
$$
(2):\ \mathrm{BM.55}(2)\text{'s two monomials differ by the BM.46 monomial};\qquad\text{the sum }M(A,Z)=A\,m_n+Z\,(m_p-m_n)=6A\tfrac{\ln2}{\mathfrak h}+Z\Delta m_{\mathrm{EM}}\ [\text{machine: Laurent}]
$$
$$
(3):\ \text{the difference of }(2)\text{'s rows at }Z\text{ and }Z+1\ [\text{machine}];\qquad\mathrm{BM.137}(3)\text{'s formed binding and FT.107}(2)\text{'s }\sigma\text{-freeness re-cited}:\ \mathcal B\ \text{is }Z\text{-free}\implies\text{the ordering survives}
$$
$$
(4):\ \mathrm{BM.43}(1)\text{'s }r_s=\mathfrak h E/2\ \text{at }E=6A;\qquad\mathrm{BM.148}(3)\text{'s cells re-read};\qquad(5):\ \text{the standing-rule record}.\ \blacksquare
$$

**Phys.** The nuclear mass ledger has three terms and each is already on the corpus's books. The count route is six bits per baryon — additive as an integer identity, the same additivity that made the two-chain binding vanish. The class term is the electromagnetic scar, carried once per charged member and by nothing else in the inventory: it makes the mass strictly increasing in $Z$ at fixed mass number, an exact ordering with no flicker input, because the formed ensemble binding is charge-blind to the last factor. And the horizon read is three hops per baryon, the values the continuum tier's capacity census already tabulated at six, twelve and twenty-four. Two nuclei of the same $A$ differ by exactly one scar monomial per proton — the isotope split is an identity, not a phenomenology — and the tier records the order it derives without comparing it to anything, as the corpus has done since its first ratio.

---
## Tier 5.1 — The Lepton Floors: the Mass Read Beside the Channel (the demand row (P5.2))

### AT.4 — The lepton floors: the two-bit read on both lines

**Thm.**
$$(1)\quad\textbf{the }\ell\textbf{-channel floor:}\qquad\text{the }\ell\text{-channel's materialized terminus is a bound chain}\ [\mathrm{Def\text{-}H.4}]\ \text{whose minimal instance is the digon: }L=2,\ \kappa\equiv1,\ k=1\qquad[\mathrm{FT.28};\ \mathrm{FT.32}(6);\ \mathrm{Census\ FT.28}]:$$
$$\boxed{\ E_{\mathrm{int}}^{(\ell)}=2\ \ \text{at the computed floor},\qquad m_\ell\,\mathfrak h\ =\ 2\ln2\ \ \text{at the floor read}\ }\qquad[\mathrm{FT.44}(4);\ \text{machine: the monomial}];$$
$$(2)\quad\textbf{the }\nu\textbf{-channel floor (re-certified):}\qquad m_{\mathrm{hid}}=\frac{2\ln2}{\mathfrak h}\ \ \text{at the minimal rung-one floor}\qquad[\mathrm{BM.96}(7)\text{, state (ii)};\ \mathrm{FT.145}(2);\ \mathrm{Census\ FT.28}]:$$
$$\textbf{the two-bit floor binds both lines:}\qquad m\,\mathfrak h\ \ge\ 2\ln2\ \ \text{on the whole materialized support of either channel}\qquad[\mathrm{BM.70}(2),(3);\ \mathrm{BM.13}(3);\ \mathrm{BM.137}(2)];$$
$$(3)\quad\textbf{what was open and what stays open:}\qquad\mathrm{BM.43}(2)\text{'s symbolic rows — }E_{\mathrm{int}}^{(\ell)},\ E_{\mathrm{int}}^{(\nu)}\ \neg\text{computed at any floor — are discharged}\ \textbf{at the informational floor on both lines};$$
$$\text{the inertial (family-channel) mass form }m_i=\mu\,r_i^2\ \text{stays symbolic with }\mu,\ \mu_\nu\ \text{undeclared}\qquad[\mathrm{FT.113}(3);\ \mathrm{FT.143}(3);\ \mathrm{Cal\text{-}F}];$$
$$\text{the conversion between the informational and inertial reads is the item-7/item-13 residue and is }\neg\text{constructed}\qquad[\mathrm{BM.43}(2);\ \mathrm{Def\text{-}BM.6}(5);\ \mathrm{BM.98}]:\qquad\textbf{named, not filled};$$
$$(4)\quad\textbf{the statistics and the doublet:}\qquad\text{the }\ell\text{-line at the floor: one chain, }k=1\text{ odd}\implies\varepsilon=-1:\ \textbf{the electron-class line is fermionic at the floor};\qquad\text{the orientation doublet rides the chain}\qquad[\mathrm{FT.122};\ \mathrm{Def\text{-}H.43}];$$
$$(5)\quad\textbf{the status:}\qquad\text{the floor values are exact monomials; the family splitting above the floor is the priced residue}\qquad[\mathrm{BM.39}\text{'s transport form, symbolic}];\qquad\neg\text{a measured lepton mass}\ [\mathrm{P5}].$$

**Req.** D1.5, D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); Census FT.28 (row-wise); Def-H.4, Def-H.43, FT.28, FT.32(6), FT.113(3), FT.122, FT.143(3), FT.145(2) (Part 3); Def-BM.6(5), BM.13(3), BM.39, BM.43(2), BM.70(2), BM.70(3), BM.96(7), BM.98, BM.137(2) (Part 4); Def-AT.3(2) (this part); exact monomial arithmetic [math; machine: `checks/verify_Atomic5.py` §D].

**Pf.**
$$
(1):\ \mathrm{FT.32}(6)\text{'s digon row at the minimal materialized chain};\qquad\mathrm{FT.44}(4)\text{'s law at }E_{\mathrm{int}}=2\implies m\mathfrak h=2\ln2\ [\text{machine}]
$$
$$
(2):\ \mathrm{BM.96}(7)\text{'s state-(ii) row re-cited};\qquad\mathrm{BM.70}(2)\text{'s two-bit floor re-cited on the materialized support}\ [\mathrm{BM.137}(2)\text{'s survival row}]
$$
$$
(3):\ \text{the discharge census against }\mathrm{BM.43}(2)\text{'s symbolic-row text, scoped to the informational floor};\qquad\text{the inertial rows re-cited as undeclared-scale content}
$$
$$
(4):\ \mathrm{BM.129}(4)\text{'s criterion at }k=1;\qquad\mathrm{FT.122}\text{'s doublet rows re-cited};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The demand row said the lepton mass read was missing at every floor and that the two-body read would need it. The floor turns out to have been standing in the census all along: the lightest materialized chain of either channel is the digon, two bits, and the informational mass law turns that into two ln 2 over 𝔥 — the same two-bit floor the flicker integral proved binding on every materialized support. What this tier does is small and load-bearing: it certifies that floor for the charged line beside the neutral one, splits what is now computed (the informational floor) from what stays open (the family-channel scale and the conversion between the two mass vocabularies), and records that the floor lepton is fermionic with its orientation doublet attached. The atom's reduced mass in the next tag consumes exactly the certified piece and nothing more.

### AT.5 — The reduced mass and the pair bookkeeping

**Thm.**
$$(1)\quad\textbf{the reduced mass (chart-side, canonical-pair scope):}\qquad m_r:=\frac{m_p\,m_\ell}{m_p+m_\ell}\qquad[\text{math: the two-body reduction on the chart};\ \mathrm{BM.48}(2)\text{'s }m_r\text{ slot};\ \mathrm{BM.10}(3)\text{'s scope}]:$$
$$\text{at the floor reads }m_p=\frac{6\ln2}{\mathfrak h}\bigl(1+c\,\varepsilon_{\mathrm{EM}}\bigr),\quad m_\ell=\frac{2\ln2}{\mathfrak h}:\qquad\boxed{\ m_r\ =\ \frac{6\ln2\,\bigl(1+c\,\varepsilon_{\mathrm{EM}}\bigr)}{\mathfrak h\,\bigl(4+3\,c\,\varepsilon_{\mathrm{EM}}\bigr)}\ =\ \frac{m_p}{4+3\,c\,\varepsilon_{\mathrm{EM}}}\ }\qquad[\text{machine: the exact rational identity}];$$
$$(2)\quad\textbf{the ratio rows:}\qquad\frac{m_\ell}{m_p}=\frac{1}{3\,(1+c\,\varepsilon_{\mathrm{EM}})}\in\Bigl(0,\tfrac13\Bigr),\qquad\frac{m_r}{m_p+m_\ell}=\frac{3\,(1+c\,\varepsilon_{\mathrm{EM}})}{\bigl(4+3\,c\,\varepsilon_{\mathrm{EM}}\bigr)^{2}}\qquad[\text{machine: exact rational identities}];$$
$$\textbf{the floor reduced mass is at most a quarter of the proton's mass:}\qquad\frac{m_r}{m_p}=\frac{1}{4+3\,c\,\varepsilon_{\mathrm{EM}}}\in\bigl(0,\ \tfrac14\bigr],\qquad\text{equality at }c\,\varepsilon_{\mathrm{EM}}=0,\ \text{strictly decreasing in the coupling}\qquad[\text{machine: the monotone census in }c\,\varepsilon_{\mathrm{EM}}\ge0];$$
$$(3)\quad\textbf{the general-nucleus reduced mass (consumed in Tier 5.5):}\qquad m_N=\frac{6A\ln2}{\mathfrak h}\ \ \text{on the count route}\ [\mathrm{AT.3}(1)]:\qquad m_r^{(A)}=\frac{m_N m_\ell}{m_N+m_\ell}=\frac{6A\ln2}{\mathfrak h\,(3A+1)}\qquad[\text{machine: the exact identity}];$$
$$A=1:\ \ m_r^{(1)}=\frac{6\ln2}{4\,\mathfrak h}=\frac{m_p}{4}\ \ \text{at }c\,\varepsilon_{\mathrm{EM}}=0\qquad[\text{machine: the consistency row with }(1)];$$
$$(4)\quad\textbf{the dimensions:}\qquad[m_r]=[\text{energy}]=\mathfrak q^{+1/2}\qquad[\mathrm{CT2.1};\ \text{machine: the exponent census on }(1)];$$
$$(5)\quad\textbf{the status:}\qquad\text{the read is chart-side and floor-scoped};\qquad\neg\text{a measured mass ratio,}\ \neg\text{a comparison}\ [\mathrm{P5}];\qquad\text{the family-splitting residue of AT.4}(3)\ \text{stands uncombined}\qquad[\mathrm{BM.30}(5)\text{'s read-choice pattern}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); Def-BM.8, BM.10(3), BM.26, BM.30(5), BM.43(1), BM.48(2), BM.55(2) (Part 4); AT.3(1), AT.4(1) (this part); the two-body reduction on a chart [math; BM.10(3) scope]; exact rational identities in commutative symbol rings [math; machine: `checks/verify_Atomic5.py` §D].

**Pf.**
$$
(1):\ \frac{m_pm_\ell}{m_p+m_\ell}=\frac{\frac{6\ln2}{\mathfrak h}(1+c\varepsilon)\cdot\frac{2\ln2}{\mathfrak h}}{\frac{2\ln2}{\mathfrak h}\bigl(3(1+c\varepsilon)+1\bigr)}=\frac{6\ln2\,(1+c\varepsilon)}{\mathfrak h\,(4+3c\varepsilon)}\ [\text{machine: cleared in the symbol ring}]
$$
$$
(2):\ \text{the two ratios by substitution};\qquad m_r/m_p=m_\ell/(m_p+m_\ell)=1/(4+3c\varepsilon)\in(0,\tfrac14],\ \text{equality at }c\varepsilon=0\ [\text{machine: monotone census}]
$$
$$
(3):\ \frac{\frac{6A\ln2}{\mathfrak h}\cdot\frac{2\ln2}{\mathfrak h}}{\frac{(6A+2)\ln2}{\mathfrak h}}=\frac{6A\ln2}{\mathfrak h\,(3A+1)}\ [\text{machine}];\qquad A=1:\ \frac{6\ln2}{4\mathfrak h}\ \text{against }(1)\text{ at }c\varepsilon=0\ [\text{machine}]
$$
$$
(4):\ [\ln2]=\mathfrak q^0,\ [1/\mathfrak h]=\mathfrak q^{1/2}\implies[m_r]=\mathfrak q^{1/2}\ [\mathrm{CT2.1};\ \text{machine}];\qquad(5):\ \text{the standing-rule record}.\ \blacksquare
$$

**Phys.** The corpus now owns both ends of the two-body problem: a proton monomial with its scar correction, a lepton floor of two bits, and the canonical-pair scope under which the chart's two-body reduction lives. Put them together and the reduced mass is not a model — it is a rational function of symbols the corpus already carries: exactly $m_p$ over four plus three times the coupling — a quarter of the proton's mass at zero coupling and strictly less at every positive one, because the scar grows the proton while the lepton's floor stays fixed. The same algebra at general mass number gives the nucleus–lepton reduced mass in closed form, six $A$ ln 2 over 𝔥 times three $A$ plus one, and at one baryon with the coupling switched off it reproduces the pair value exactly — the consistency row that says the two computations are one computation. Everything here is floor-scoped and chart-side, priced as such.

---

## Tier 5.2 — The EM Binding Channel: the Atom Constructed (the demand row (P5.1), first)

### Def-AT.4 — The EM-pair composite (the atom; under A-AT.1)

**Def.** The construction BM.48(3) names as absent and BM.143(7) demands first, issued as a definition-side grammar on derived objects under the logged declaration A-AT.1; no new axiom, no new datum, no new dimensionful scale.
$$(1)\quad\textbf{the members:}\qquad\text{a sealed composite }\mathcal X_p\text{ in the }q=+1\text{ class}\ [\mathrm{BM.26}]\ \text{and an }\ell\text{-channel bound chain }\mathcal X_\ell\text{ in the }q=-1\text{ class}\qquad[\mathrm{EM.9};\ \mathrm{Def\text{-}BM.6}(1);\ \mathrm{BM.23}(5)\text{'s forced carrier }q_\ell=-1];$$
$$(2)\quad\textbf{the pair grammar (the constitutive clause):}\qquad\text{the }\textbf{EM-pair composite}\ \text{is the two-member composite }(\mathcal X_p,\mathcal X_\ell)\ \text{with:}$$
$$\mathrm{(i)}\ \ Q(\mathcal X_p)+Q(\mathcal X_\ell)=0\qquad[\mathrm{Def\text{-}BM.8}\text{'s additive read}]\ —\ \textbf{the neutrality seal: the pair is one observable object exactly when its total read vanishes};$$
$$\mathrm{(ii)}\ \ \text{the members keep their own colour seals: }\partial_{\mathrm{col}}=\varnothing\text{ member-wise; no colour junction joins them}\qquad[\mathrm{D2.14};\ \mathrm{Def\text{-}BM.1}]:\ \text{the pair's colour completeness is member-wise, not junctional};$$
$$\mathrm{(iii)}\ \ \text{the binding read: the chart-side two-body pole of the Coulomb read}\qquad[\mathrm{BM.48}(1)\text{'s }V(d)=-\varepsilon_{\mathrm{EM}}/d\ \text{at }(q_1q_2)=(-1);\ \mathrm{BM.48}(2)\text{'s ladder at the reduced mass }m_r\ \text{of AT.5}];$$
$$(3)\quad\textbf{the observability clause:}\qquad\text{the exterior EM flux of the pair is }e\,(Q_p+Q_\ell)=0\ \text{identically}\qquad[\mathrm{Def\text{-}BM.12}(3)\text{'s Gauss row};\ \mathrm{BM.135}(5)\text{'s }e\,Q\text{ coefficient}]:\ \textbf{the pair reads as one neutral object at range};$$
$$(4)\quad\textbf{the priced clauses:}\qquad\text{the pair grammar is declared, }\neg\text{derived}\ [\mathrm{A\text{-}AT.1}];\qquad\text{the capture and decay rates are }\neg\text{constructed}\ [\mathrm{BM.6}(5);\ \mathrm{P5.3}];\qquad\text{no value of }e\text{ is issued}\ [\mathrm{C\text{-}AT.1}];$$
$$(5)\quad\textbf{the name:}\qquad\textbf{hydrogen}\ :=\ \text{the EM-pair composite with }\mathcal X_p\text{ the unit-class baryon and }\mathcal X_\ell\text{ the electron line}\qquad[\mathrm{A\text{-}AT.2};\ \mathrm{Def\text{-}AT.3}\text{'s data bar applies}].$$

### Def-AT.5 — The atomic card

**Def.** The **card** of an EM-pair composite refines the composite-card template [Def-BM.2] with:
$$(1)\ \text{the member rows: the two constituent cards}\qquad[\mathrm{Def\text{-}BM.2};\ \mathrm{Def\text{-}AT.2}];\qquad(2)\ \text{the neutrality row: }Q=0\ \text{with its member split}\qquad[\mathrm{Def\text{-}BM.8}];$$
$$(3)\ \text{the binding row: the pole ladder }E_n\text{ at }m_r\ \text{with its chart-side scope}\qquad[\mathrm{BM.48}(2);\ \mathrm{AT.5}(1)];\qquad(4)\ \text{the statistics row: }\varepsilon=\varepsilon_p\cdot\varepsilon_\ell\qquad[\mathrm{BM.129}(4);\ \mathrm{BM.136}(3)];$$
$$(5)\ \text{the flux row: the exterior read }e\,Q=0\qquad[\mathrm{Def\text{-}AT.4}(3)].$$
Card values are derived at the constructed reads; card grammar is this definition [P1, P5].

### AT.6 — The binding pole: the conditional rows made constructed

**Thm.**
$$(1)\quad\textbf{the pole ladder (the bound channel exists):}\qquad\text{under Def-AT.4's grammar the pair's chart-side two-body problem carries the hydrogenic poles}\qquad[\mathrm{BM.48}(2)\text{'s rows, lifted from conditional to constructed by the declared grammar}]:$$
$$\boxed{\ E_n=-\frac{\varepsilon_{\mathrm{EM}}^{\,2}\,m_r}{2\,n^{2}}\ }\qquad n=1,2,3,\dots\qquad[\text{math: the Coulomb spectrum on the canonical pair};\ \mathrm{BM.10}(3);\ \mathrm{BM.48}(2);\ \text{machine: the coefficient and ladder rows}];$$
$$\text{at the floor read }m_r=\frac{6\ln2\,(1+c\,\varepsilon_{\mathrm{EM}})}{\mathfrak h\,(4+3\,c\,\varepsilon_{\mathrm{EM}})}:\qquad\boxed{\ E_1=-\,\frac{3\,e^{4}\ln2\,\bigl(1+c\,\varepsilon_{\mathrm{EM}}\bigr)}{16\,\pi^{2}\,\mathfrak h\,\bigl(4+3\,c\,\varepsilon_{\mathrm{EM}}\bigr)}\ }\qquad[\text{machine: }e^4/(16\pi^2)=\varepsilon_{\mathrm{EM}}^2;\ \text{the monomial-rational}];$$
$$(2)\quad\textbf{the system read (the category bar now has its object):}\qquad m_{\mathrm{pair}}=m_p+m_\ell+E_{\mathrm{bind}},\qquad E_{\mathrm{bind}}=E_1<0\qquad[\mathrm{BM.48}(4)\text{'s system-read form, instantiated}]:$$
$$\boxed{\ \text{BM.54(4)'s row — ``binding … exists, in this inventory, nowhere yet'' — is discharged: the constructed pair carries the only negative binding read}\ }$$
$$\text{the free members' masses are untouched: }m_p\text{ and }m_\ell\text{ stand as derived, with no }E_{\mathrm{bind}}\text{ term}\qquad[\mathrm{BM.48}(4)\text{–}(5)\text{'s bar, honored}];$$
$$(3)\quad\textbf{the binding fraction:}\qquad\frac{E_1}{m_p+m_\ell}=-\,\frac{\varepsilon_{\mathrm{EM}}^{2}}{2}\cdot\frac{3\,(1+c\,\varepsilon_{\mathrm{EM}})}{\bigl(4+3\,c\,\varepsilon_{\mathrm{EM}}\bigr)^{2}}\qquad[\text{machine: the exact identity from AT.5}(2)];$$
$$(4)\quad\textbf{the ladder ratios are coupling-free:}\qquad\frac{E_2}{E_1}=\frac14,\qquad\frac{E_n}{E_1}=\frac{1}{n^{2}}\qquad[\text{machine}]:\qquad\textbf{the shape of the ladder is exact and }e\text{-independent; its scale is not}\ [\mathrm{C\text{-}AT.1}];$$
$$(5)\quad\textbf{the poles of the resolvent:}\qquad\text{the pair's two-body read is the pole condition of the chart resolvent's two-body reduction}\qquad[\mathrm{Def\text{-}BM.20}(2);\ \mathrm{BM.134}(1),(4)]:$$
$$\text{the bound poles sit below the continuum edge }m_p+m_\ell\ \text{and accumulate there as }n\to\infty\qquad[\text{math: the ladder's accumulation};\ \text{machine: the monotone census}];$$
$$(6)\quad\textbf{the status:}\qquad\text{the ladder is exact and symbolic in }e;\qquad\text{the grammar is declared }[\mathrm{A\text{-}AT.1}],\ \text{the rows are theorems about the declared structure};$$
$$\neg\text{a measured binding energy, ionization scale or atomic datum}\ [\mathrm{P5}];\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}].$$

**Req.** D2.5, D2.9 (Parts 1–2); CT2.1, CT2.6 (Part 2); P1, P4, P5 (Parts 1–2); FT.44(4) (Census); Def-H.4 (Part 3); Def-BM.8, Def-BM.12, Def-BM.20, BM.6(5), BM.10(3), BM.26, BM.43(2), BM.48(1), BM.48(2), BM.48(3), BM.48(4), BM.48(5), BM.54(3), BM.54(4), BM.134(1), BM.134(4), BM.135(5), BM.143(7) (Part 4); A-AT.1, Def-AT.3, Def-AT.4, Def-AT.5, AT.4(1), AT.5(1), AT.5(2) (this part); the Coulomb spectrum on the canonical pair, exact rational-coefficient identities in the symbol ring [math; machine: `checks/verify_Atomic5.py` §E].

**Pf.**
$$
(1):\ \mathrm{BM.48}(2)\text{'s ladder with }m_r\ \text{from AT.5}(1);\qquad\text{the coefficient identity }\frac{e^4}{16\pi^2}=\varepsilon_{\mathrm{EM}}^2\ \text{and the cleared monomial-rational}\ [\text{machine}]
$$
$$
(2):\ \mathrm{BM.48}(4)\text{'s system-read form instantiated at the constructed pair};\qquad E_1<0\ \text{at positive symbols}\ [\text{machine: the sign census}];\qquad\text{the discharge census against }\mathrm{BM.54}(4)\text{'s text}\ [\text{machine: the document pins}]
$$
$$
(3):\ \frac{m_r}{m_p+m_\ell}\ \text{from AT.5}(2)\ \text{substituted into }E_1=-\varepsilon_{\mathrm{EM}}^2m_r/2\ [\text{machine}]
$$
$$
(4):\ E_n/E_1=1/n^2\ \text{on the ladder}\ [\text{machine: integer arithmetic}]
$$
$$
(5):\ \text{the two-body pole condition on }\mathrm{Def\text{-}BM.20}(2)\text{'s form at the reduced mass};\qquad E_n\uparrow 0\ \text{monotonely}\ [\text{machine: }1/n^2\text{ monotone}];\qquad(6):\ \text{the standing-rule record}.\ \blacksquare
$$

**Phys.** This is the tag the corpus has been reaching for since BM.48 drew the potential and then refused to own an atom. The declaration issues the grammar — a neutral pair, members keeping their own colour seals, binding read at the reduced mass — and the moment the grammar exists, the conditional hydrogenic rows of Part 4 stop being conditional: the ladder is the constructed channel's pole spectrum, the ground row is an exact monomial in $e$, ln 2 and 𝔥, and the category bar's object finally exists — a system whose read is the sum of its members plus a negative binding, with the free members' masses untouched exactly as the bar demanded. The ladder's shape is coupling-free — quarter ratios all the way down — while its scale waits on a coupling value no theorem will ever issue. The binding fraction is small not by assumption but by arithmetic: it carries the coupling squared against a ratio bounded above by three over thirty-two.

### AT.7 — Neutrality and observability: the atom as one object

**Thm.**
$$(1)\quad\textbf{the neutrality theorem:}\qquad Q(\text{pair})=0\ \text{exactly, on the grammar's own clause}\qquad[\mathrm{Def\text{-}AT.4}(2)\,\mathrm{(i)};\ \mathrm{Def\text{-}BM.8}]:$$
$$\text{the exterior EM flux vanishes identically: }\partial_\mu F^{\mu\nu}=e\,J_Q^\nu\ \text{with }J_Q^0\text{'s integral }e\,Q=0\qquad[\mathrm{BM.135}(5);\ \mathrm{Def\text{-}BM.12}(3)]:\qquad\boxed{\ \textbf{the atom is EM-invisible at range}\ };$$
$$(2)\quad\textbf{the registry distinction (atom vs separated pair):}\qquad\text{the atom: one support, one vanishing flux read; the separated pair: two supports, two nonzero flux reads }(+e,\,-e)\qquad[\mathrm{Def\text{-}BM.12}(3);\ \text{machine: the flux census}]:$$
$$\text{the two configurations share }Q_{\mathrm{total}}=0\ \text{and differ in the flux read's support structure}\qquad[\text{machine: the }0/2\text{ source-count row}]:\ \textbf{the observable difference is registry, not charge};$$
$$(3)\quad\textbf{the colour sector:}\qquad\text{the pair is colour-complete member-wise }(\partial_{\mathrm{col}}=\varnothing\text{ on each member})\ \text{and admits no colour junction}\qquad[\mathrm{D2.14};\ \mathrm{CT3.17a}\text{'s grammar}]:$$
$$\text{the pair's strong read is the sum of two sealed singlets' reads — the trace-only law holds member-wise}\qquad[\mathrm{BM.1}(2)]:\qquad\neg\exists\ \text{a triplet pole}\ [\mathrm{CT3.22}];$$
$$(4)\quad\textbf{the finite-range contrast:}\qquad\text{the naked unit-class composite carries its scar field at range}\qquad[\mathrm{BM.47}\text{'s infinite-range seal};\ \mathrm{BM.46}]:$$
$$\textbf{the atom is the corpus's first neutral extended object: the range infinity is answered by the neutrality, not by a screening dynamics}\qquad[\neg\exists\ \text{a screening construction};\ \mathrm{BM.6}(5)];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived on the declared grammar; }\neg\text{a measured neutrality test,}\ \neg\text{a comparison}\ [\mathrm{P5}].$$

**Req.** D2.11, D2.14, D3.4 (Parts 1–2); CT3.17a, CT3.22 (Part 2); P5 (Parts 1–2); FT.19 (Part 3); Def-BM.1, Def-BM.8, Def-BM.12, BM.1(2), BM.6(5), BM.46, BM.47, BM.135(5) (Part 4); Def-AT.4 (this part); exact flux censuses [math; machine: `checks/verify_Atomic5.py` §E].

**Pf.**
$$
(1):\ \text{the grammar's neutrality clause summed by the additive read};\qquad\mathrm{BM.135}(5)\text{'s gauged read with }Q=0\implies J_Q\text{'s charge }0\ [\text{machine}]
$$
$$
(2):\ \text{the flux integral }e\,Q\ \text{evaluated on one support against two}\ [\text{machine: }0\text{ vs }e+(-e)\text{ on separate supports}]
$$
$$
(3):\ \mathrm{D2.14}/\mathrm{CT3.17a}\text{'s grammar re-cited member-wise};\qquad\mathrm{BM.1}(2)\text{'s trace-only law per member};\qquad\mathrm{CT3.22}\ \text{re-cited}
$$
$$
(4):\ \mathrm{BM.47}\text{'s range row re-cited};\qquad\text{the inventory scan: no screening object}\ [\text{machine: token row}];\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** What makes the atom one thing is not a force holding it but a read summing it: the pair's total ternary charge is zero, so its exterior flux — the corpus's own $eQ$ — vanishes identically, and the object that reaches a distant observer is silence where the naked proton carries its scar to infinity. The corpus's neutrality here is structural, not dynamical: no screening cloud is constructed, and none is needed, because the flux read is exact at zero rather than small. The registry makes the bookkeeping sharp — the atom and the separated pair have the same total charge and utterly different supports, one vanishing flux against two unit sources — and the colour side carries over untouched: each member is complete on its own, no junction joins them, and the strong read stays a sum of traces. The universe-scale neutrality BM.47 proved for the whole ledger now has its local, object-sized instance.

---
## Tier 5.3 — The Hydrogen Read and the Ionization Registry

### AT.8 — The hydrogen ladder at the floor read

**Thm.**
$$(1)\quad\textbf{the ladder rows (hydrogen, }A=1,\ Z=1\textbf{):}\qquad E_n=-\frac{\varepsilon_{\mathrm{EM}}^{2}\,m_r}{2\,n^{2}}\qquad[\mathrm{AT.6}(1)]:$$
$$E_1=-\frac{3\,e^{4}\ln2\,(1+c\,\varepsilon_{\mathrm{EM}})}{16\,\pi^{2}\,\mathfrak h\,(4+3\,c\,\varepsilon_{\mathrm{EM}})},\qquad E_2=\frac{E_1}{4},\qquad E_3=\frac{E_1}{9}\qquad[\text{machine: the ladder rows}];$$
$$(2)\quad\textbf{the transition bookkeeping (the exact rationals):}\qquad\Delta E_{n\to m}:=E_m-E_n=\frac{\varepsilon_{\mathrm{EM}}^{2}\,m_r}{2}\Bigl(\frac{1}{m^{2}}-\frac{1}{n^{2}}\Bigr)>0\ \ \text{for }n>m\qquad[\text{machine}]:$$
$$\Delta E_{2\to1}=\frac{3}{4}\,|E_1|,\qquad\Delta E_{3\to2}=\frac{5}{36}\,|E_1|,\qquad\frac{\Delta E_{3\to2}}{\Delta E_{2\to1}}=\frac{5}{27}\qquad[\text{machine: exact rational rows}];$$
$$(3)\quad\textbf{the radius row (chart-side):}\qquad a:=\frac{1}{\varepsilon_{\mathrm{EM}}\,m_r}\ \ \text{the chart-side length read of the ground pole}\qquad[\text{math: the Coulomb length on the canonical pair};\ \mathrm{BM.10}(3);\ \text{machine: the exponent census }[a]=\mathfrak q^{-1/2}]:$$
$$a\,\mathfrak h=\frac{4+3\,c\,\varepsilon_{\mathrm{EM}}}{6\,(1+c\,\varepsilon_{\mathrm{EM}})\,\ln2}\cdot\frac{4\pi}{e^{2}}\ \ \text{in hops — the atomic size is a large-aditurary multiple of the hop, exact and }e^{-2}\text{-scaled}\qquad[\text{machine: the monomial}];$$
$$(4)\quad\textbf{the virial-type check (chart-side):}\qquad\langle \mathrm{KE}\rangle=-E_1,\qquad\langle V\rangle=2E_1\qquad[\text{math: the Coulomb virial identity on the canonical pair};\ \text{machine: the identity rows}]:$$
$$\text{the binding bookkeeping closes: }m_{\mathrm{pair}}=m_p+m_\ell+E_1\ \text{with the ground-state kinetic and potential reads in the exact }1{:}2\ \text{ratio};$$
$$(5)\quad\textbf{the status:}\qquad\text{all rows chart-side under BM.10(3)'s scope and floor-scoped at }m_r;\qquad\neg\text{a measured Rydberg-type constant,}\ \neg\text{a comparison}\ [\mathrm{P5};\ \mathrm{C\text{-}AT.1}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); Def-BM.8, BM.10(3), BM.48(2), BM.48(4) (Part 4); A-AT.1, Def-AT.4, AT.5(1), AT.6(1) (this part); the Coulomb spectrum, virial identity and length scale on the canonical pair [math; machine: `checks/verify_Atomic5.py` §E].

**Pf.**
$$
(1):\ \mathrm{AT.6}(1)\text{'s ladder instantiated};\qquad(2):\ \text{the differences }1/m^2-1/n^2\ \text{as exact rationals, scaled by }|E_1|\ [\text{machine}];\qquad\tfrac{5/36}{3/4}=\tfrac{5}{27}\ [\text{machine}]
$$
$$
(3):\ \text{the length dimension }[1/(\varepsilon_{\mathrm{EM}}m_r)]=\mathfrak q^{-1/2}\ [\mathrm{CT2.1};\ \text{machine}];\qquad\text{the hop conversion by }m_r\text{'s monomial}\ [\text{machine}]
$$
$$
(4):\ \text{the virial identity for the }1/d\text{ potential on the canonical pair}\ [\text{math}];\qquad\text{the bookkeeping closure}\ [\text{machine}];\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The ladder was already priced; this tag reads it at the constructed channel's own reduced mass and books what falls out. The transition rationals are pure arithmetic — three quarters, five thirty-sixths, five over twenty-seven — and they carry no coupling at all, because the ladder's shape never did. The chart-side length read says the atom is many hops across, its size scaled by the inverse square of the coupling, and the virial identity closes the ground-state books in the exact one-to-two ratio the Coulomb form forces. Nothing here is compared to a measured line, and nothing here could be until a coupling value were issued — which no theorem of the corpus will ever do.

### AT.9 — Ionization: the continuum edge and the registry of the ionized sector

**Thm.**
$$(1)\quad\textbf{the continuum edge:}\qquad E_\infty=0\ \text{relative to the separated pair: the ladder accumulates at }m_p+m_\ell\qquad[\mathrm{AT.6}(5);\ \text{machine: the monotone census}]:$$
$$\boxed{\ \text{the ionization threshold of hydrogen is }\ \bigl|E_1\bigr|=\frac{\varepsilon_{\mathrm{EM}}^{2}\,m_r}{2}\ }\qquad\text{exact and symbolic}\qquad[\text{machine: the monomial}];$$
$$(2)\quad\textbf{the registry rows (the two sectors):}\qquad\text{the bound sector: one support, }Q=0,\ \text{zero exterior flux, the pole ladder};\qquad\text{the ionized sector: two supports, }Q=\pm1\text{ members, two unit flux reads, no bound pole}\qquad[\mathrm{AT.7}(2);\ \text{machine}]:$$
$$\text{the threshold is the exact energy bookkeeping between the sectors — the }\textbf{registry boundary is the flux-read structure, not a distance};$$
$$(3)\quad\textbf{the capacity rows (the chart cells):}\qquad\text{the members' own counts sit inside their chart cells: }E_{\mathrm{int}}\in\{6,2\}\ \text{at }r_s\in\{3\mathfrak h,\mathfrak h\}\qquad[\mathrm{BM.148}(3);\ \text{machine}]:$$
$$\text{the one-hop cell carries exactly the digon — the free lepton is the lightest chart-formed content, and nothing heavier}\qquad[\mathrm{BM.148}(3)\text{'s one-hop row}];$$
$$(4)\quad\textbf{the membrane row:}\qquad\text{the locked-sector membrane governs retained content, not the pair's unbinding}\qquad[\mathrm{BM.149}]:$$
$$\text{ionization as a }\textbf{process}\ \text{(a rate, a cross-section) is dynamics-of-}Q\text{ content and stays open}\qquad[\mathrm{BM.6}(5);\ \mathrm{P5.3}]:\qquad\textbf{the threshold is derived; the rate is not};$$
$$(5)\quad\textbf{the recombination mirror:}\qquad\text{the reverse bookkeeping (ion pair }\to\text{ atom) releases exactly }\bigl|E_1\bigr|\ \text{in the ledger's books}\qquad[\text{machine: the sign-reversed row}];\qquad\text{the reverse }\textbf{process}\ \text{is conditional on the same open rates};$$
$$(6)\quad\textbf{the status:}\qquad\text{the threshold and the registry are exact; the rates are open and named}\qquad[\mathrm{P5.3}\text{'s scope}];\qquad\neg\text{a measured ionization energy}\ [\mathrm{P5}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); Census FT.28 (row-wise); Def-BM.8, BM.6(5), BM.46, BM.48(4), BM.135(5), BM.148(3), BM.149 (Part 4); A-AT.1, Def-AT.4, AT.4(1), AT.6(1), AT.7(2) (this part); exact monomial and registry censuses [math; machine: `checks/verify_Atomic5.py` §E].

**Pf.**
$$
(1):\ \text{the accumulation row of AT.6}(5);\qquad|E_1|=\varepsilon_{\mathrm{EM}}^2m_r/2\ [\text{machine}]
$$
$$
(2):\ \text{the flux census on one support against two}\ [\mathrm{AT.7}(2)\ \text{re-run}];\qquad\text{the pole census: bound poles below the edge, none above}\ [\text{machine}]
$$
$$
(3):\ \mathrm{BM.148}(3)\text{'s rows at }E_{\mathrm{int}}=6,2:\ r_s=3\mathfrak h,\mathfrak h;\qquad\text{the one-hop capacity row re-cited}
$$
$$
(4):\ \mathrm{BM.149}\text{'s membrane scope re-cited};\qquad\text{the inventory scan: no capture rate}\ [\text{machine: token row}]
$$
$$
(5):\ \text{the sign-reversed bookkeeping}\ [\text{machine}];\qquad(6):\ \text{the status record}.\ \blacksquare
$$

**Phys.** Ionization in this corpus is first a boundary between registries and only then a number: the atom is one neutral support with a ladder of poles below its edge, the ionized pair is two charged supports with no bound pole, and the threshold — the coupling squared times the reduced mass over two — is the exact bookkeeping between the two. The chart-cell rows locate the members: the free lepton is the one-hop cell's entire content, the proton its three-hop cell, so no member of the ionized sector ever outgrows its chart read. What the tier refuses to fake is the dynamics: a capture rate or a recombination cross-section is a rate, the corpus's rates are tick-weights awaiting the emergent-time coupling, and the tier records the threshold, prices the reverse bookkeeping, and leaves the rates exactly where Part 4 left them — open, named, and honest.

---

## Tier 5.4 — Shells and the Exclusion Theorem

### AT.10 — The orbital ladder: the promoted rotation and the shell state space

**Thm.**
$$(1)\quad\textbf{the rotation algebra on the chart:}\qquad SO(3)\ \text{is the promoted }C_3\text{, exactly, with the moment current conserved on-shell}\qquad[\mathrm{BM.8}(3);\ \mathrm{BM.42}(1)]:$$
$$\text{the angular-momentum content of a chart-side two-body pole is the orbital Casimir }L^{2}\qquad[\mathrm{BM.42}(3)\text{'s Lagrange decomposition}:p^2=p_r^2+L^2/r^2];$$
$$(2)\quad\textbf{the shell states:}\qquad\text{the level }n\text{ of the Coulomb ladder carries the angular-momentum multiplets }\ell=0,\dots,n-1\text{ with dimensions }2\ell+1\qquad[\text{math: the }SO(3)\text{ representation theory of the Coulomb problem on the canonical pair};\ \mathrm{BM.48}(2);\ \mathrm{BM.10}(3)]:$$
$$\boxed{\ \dim(\text{level }n)=\sum_{\ell=0}^{n-1}(2\ell+1)=n^{2}\ }\qquad[\text{machine: the integer sums at }n\le10];$$
$$(3)\quad\textbf{the parity factor of the ladder:}\qquad\chi_\ell(\pi)=(-1)^{\ell}\qquad[\mathrm{BM.42}(9)\text{'s derived orbital factor, re-cited}];$$
$$(4)\quad\textbf{the orientation doublet:}\qquad\text{each shell state carries the chain's orientation doublet with the }j=\tfrac12\text{ anchor Casimir }\tfrac34\mathbb I_2\qquad[\mathrm{FT.122};\ \mathrm{BM.42}(7)\text{'s anchor at }k=1;\ \mathrm{Def\text{-}H.43}\text{'s read promotion}]:$$
$$(5)\quad\textbf{the status:}\qquad\text{the orbital census is chart-side and exact; the doublet is corpus-constructible with no parameter}\qquad[\mathrm{FT.122};\ \mathrm{P5}].$$

**Req.** A3 (Part 1); D2.9 (Parts 1–2); CT2.1, CT2.6 (Part 2); P1, P5 (Parts 1–2); Def-H.43, FT.122 (Part 3); Def-BM.8, BM.8(3), BM.10(3), BM.42(1), BM.42(3), BM.42(7), BM.42(9), BM.48(2) (Part 4); AT.6(1) (this part); the $SO(3)$ representation theory of the Coulomb problem, exact integer sums [math; machine: `checks/verify_Atomic5.py` §F].

**Pf.**
$$
(1):\ \mathrm{BM.8}(3)\text{'s promotion identity and BM.42}(1)\text{'s conserved moment re-cited};\qquad\mathrm{BM.42}(3)\text{'s Lagrange identity re-cited}
$$
$$
(2):\ \text{the Coulomb problem's hidden degeneracy on the canonical pair}\ [\text{math}];\qquad\textstyle\sum_{\ell=0}^{n-1}(2\ell+1)=n^2\ \text{at }n=1..10\ [\text{machine}]
$$
$$
(3):\ \mathrm{BM.42}(9)\ \text{re-cited};\qquad(4):\ \mathrm{FT.122}\text{'s constructible doublet and BM.42}(7)\text{'s anchor Casimir re-cited};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The shells are not imported; they are the Coulomb problem's own degeneracy read through algebras the corpus already promoted. The rotation group arrived exactly in the Noether tier — the rational point of a one-parameter subgroup that was always in the register — and the Lagrange split put the orbital Casimir inside the momentum square the dispersion already carries. Level $n$ then carries $n$ squared orbital states as a matter of representation arithmetic, with the alternating parity factor the angular-momentum tier derived once for all levels. Onto each state the chain adds its orientation doublet, constructible from the loop and its reversal with no parameter and no choice beyond naming. Nothing here touches the ledger: it is the chart side of the constructed pole, counted.

### AT.11 — The exclusion theorem and the shell capacities

**Thm.**
$$(1)\quad\textbf{the fermion sign of the shell lepton:}\qquad\text{the }\ell\text{-channel line at its floor is fermionic}\qquad[\mathrm{AT.4}(4)]:$$
$$(2)\quad\textbf{the exclusion theorem:}\qquad\text{two fermionic shell leptons cannot occupy one registered direction}:\qquad\text{the two-state antisymmetrized sector on a }1\text{-dimensional registered direction is}\ \wedge^{2}(\mathbb C^{1})=0\qquad[\mathrm{BM.136}(3)\text{'s wedge rows at }(\mathbb C^2,\wedge^3)\text{ and }(\mathbb C^3,\wedge^3)\text{ pattern; machine: the exact ranks}]:$$
$$\boxed{\ \text{at most one lepton per registered direction — the exclusion is the wedge zero plus the fermion sign, no new axiom}\ }$$
$$(3)\quad\textbf{the shell capacities:}\qquad\text{the registered directions of shell }n\text{ are the }n^{2}\text{ orbital states of AT.10}(2)\text{, each carrying the orientation doublet}:\qquad\boxed{\ \mathrm{cap}(n)=2\,n^{2}\ }$$
$$\mathrm{cap}(n)=2,\ 8,\ 18,\ 32,\ 50,\ 72\ \ \text{at }n=1..6\qquad[\text{machine: the integer rows}];$$
$$(4)\quad\textbf{the cumulative census:}\qquad\mathrm{Cum}(n)=\sum_{j\le n}\mathrm{cap}(j)=2,\ 10,\ 28,\ 60,\ 110,\ 182\ \ \text{at }n=1..6\qquad[\text{machine}]:$$
$$\text{the closed-shell classes are the cumulative rows — internal counts of registered directions, named by no element and compared to nothing};$$
$$(5)\quad\textbf{the register discipline:}\qquad\text{the directions are C10's mutually orthogonal registered alternatives: distinct states present distinct alternatives, and the count of directions is the count of admissible single-occupancy states}\qquad[\mathrm{C10};\ \text{machine}];$$
$$(6)\quad\textbf{the status:}\qquad\text{the theorem is exact on the constructed shell space; the winding occupancy per named class stays the (R3) residue}\qquad[\mathrm{BM.129}(6);\ \mathrm{BM.136}(5)];\qquad\neg\text{a measured shell population}\ [\mathrm{P5}].$$

**Req.** C10 (Part 1); D2.9 (Parts 1–2); P1, P5 (Parts 1–2); FT.122 (Part 3); BM.129(6), BM.136(3), BM.136(5) (Part 4); AT.4(4), AT.10(2), AT.10(4) (this part); exact wedge-rank arithmetic, integer censuses [math; machine: `checks/verify_Atomic5.py` §F].

**Pf.**
$$
(1):\ \mathrm{AT.4}(4)\ \text{re-cited}
$$
$$
(2):\ \text{the antisymmetrizer on a }1\text{-dimensional registered direction has rank }0\ [\text{machine}];\qquad\text{the wedge rows' pattern re-cited from BM.136}(3)
$$
$$
(3):\ \text{the directions }n^2\ \text{times the doublet }2\ [\text{machine}];\qquad(4):\ \text{the cumulative sums}\ [\text{machine}]:\ 2,\ 2+8=10,\ 10+18=28,\ 28+32=60,\ 60+50=110,\ 110+72=182
$$
$$
(5):\ \mathrm{C10}\text{'s register accounting re-cited};\qquad(6):\ \text{the standing-rule record}.\ \blacksquare
$$

**Phys.** The periodic table's most famous counting law arrives here as two small exact facts leaned against each other. The shell lepton is a fermion at its floor — one chain, odd winding, the sign BM.129 computed. Two fermions on one registered direction antisymmetrize to zero — the same wedge arithmetic that killed the four-slot colour singlet. So one lepton per direction, and the directions are what the register has been counting since the qubit era: mutually orthogonal alternatives, $n$ squared per shell from the Coulomb degeneracy, doubled by the orientation doublet. Two, eight, eighteen, thirty-two; cumulative two, ten, twenty-eight, sixty. The rows are internal counts — the corpus names no elements beyond its four declared labels and compares itself to no chemistry — but the counting mechanism is entirely its own: a wedge zero, a fermion sign, and a register.

---

## Tier 5.5 — Multi-Lepton Atoms: Neutrality, Filling, and the Closed-Shell Census

### AT.12 — The $Z$-lepton composite and the neutrality theorem

**Thm.**
$$(1)\quad\textbf{the composite:}\qquad\text{the }\textbf{atom of charge }Z\text{ and mass number }A\ :=\ \text{the multi-member composite (nucleus}(A,Z);\ Z\text{ shell leptons on the registered directions of AT.11)}\qquad[\mathrm{A\text{-}AT.1}\text{'s grammar extended member-wise}]:$$
$$Q\bigl(\text{atom}(A,Z)\bigr)=Z-Z=0\qquad[\mathrm{Def\text{-}BM.8}\text{'s additivity};\ \text{machine}]:\qquad\boxed{\ \textbf{every filled atom is neutral, exactly}\ };$$
$$(2)\quad\textbf{the flux row:}\qquad\text{the exterior EM flux of the filled atom vanishes identically}\qquad[\mathrm{AT.7}(1)\text{ at the multi-member support}];$$
$$(3)\quad\textbf{the statistics:}\qquad\varepsilon\bigl(\text{atom}(A,Z)\bigr)=(-1)^{A+Z}\ \ \text{at the floors (baryon digons and lepton digons)}\qquad[\mathrm{AT.2}(2);\ \mathrm{AT.4}(4);\ \mathrm{BM.136}(3);\ \text{machine: the parity census}]:$$
$$\textbf{hydrogen }(A,Z)=(1,1)\text{ is bosonic; the }Z=2\text{ closed-shell class }(2,2)\text{ is bosonic; the }A+Z\text{-odd classes — the }(2,1)\text{ and }(3,2)\text{ rows — are fermionic — exact at the floors}\qquad[Z\le A:\ \text{the matter-sector constraint of Def-AT.1}];$$
$$(4)\quad\textbf{the lepton–lepton residue (priced):}\qquad\text{the pair potential between shell leptons is derived chart-side }V=+\frac{\varepsilon_{\mathrm{EM}}}{d}\qquad[\mathrm{BM.48}(1)\text{'s sign rows}]:$$
$$\text{the three-and-more-body energy of a filled shell is a dynamics-of-}Q\text{ object and is }\neg\text{constructed};\qquad\text{the filling rows below are the independent-particle reads, with the residue named}\qquad[\mathrm{BM.30}(5)\text{'s read-choice discipline}];$$
$$(5)\quad\textbf{the status:}\qquad\text{the neutrality and statistics rows are exact; the many-body energy residue stands open}\qquad[\mathrm{P5};\ \mathrm{BM.6}(5)].$$

**Req.** D2.9, D3.4 (Parts 1–2); P1, P5 (Parts 1–2); FT.44(4) (Census); Def-BM.8, BM.6(5), BM.30(5), BM.48(1), BM.129(6), BM.136(3) (Part 4); A-AT.1, Def-AT.4, AT.2(2), AT.4(4), AT.7(1), AT.7(2), AT.11 (this part); exact parity censuses, exact flux censuses [math; machine: `checks/verify_Atomic5.py` §G].

**Pf.**
$$
(1):\ \text{the additive read over the nucleus and }Z\text{ leptons }[\text{machine: }Z+(-Z)=0]
$$
$$
(2):\ \mathrm{AT.7}(1)\text{'s flux row at the multi-member support}
$$
$$
(3):\ \text{the product law over }A\text{ baryon chains and }Z\text{ lepton chains at odd floor windings}\ [\text{machine: }(-1)^{A+Z}]
$$
$$
(4):\ \mathrm{BM.48}(1)\text{'s sign rows re-cited lepton–lepton};\qquad\text{the inventory scan: no three-body EM read}\ [\text{machine: token row}];\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** Fill the registered directions and the composite closes its own books: $Z$ charged members in the nucleus, $Z$ opposite members in the shells, and the additive read — the same sum that made the baryon classes and the deuteron's count — lands on exactly zero. The neutrality is per-object now, not just per-universe: EM.11 said the world's total charge vanishes because every end is sealed; AT.7 said the pair's does because the grammar says so; this tag says every filled atom's does, by the same addition. The statistics row is the product law over all the chains at once, baryons and leptons together, and it makes hydrogen and its closed two-lepton successor bosons at the floors — a boson nucleus carrying an even number of lepton signs — while every $A+Z$-odd class stays fermionic, exact, floor-scoped, and waiting on no datum. What the tier prices honestly is the residue: shell leptons repel each other through a derived chart-side potential, the full many-body energy of a filled shell is a construction the era does not carry, and the filling rows that follow are independent-particle reads with the residue named.

### AT.13 — The filling map and the closed-shell census

**Thm.**
$$(1)\quad\textbf{the energy ordering:}\qquad E_n(Z)=-\frac{Z^{2}\,\varepsilon_{\mathrm{EM}}^{2}\,m_r^{(A,Z)}}{2\,n^{2}}\qquad[\mathrm{AT.6}(1)\text{ at nuclear charge }Z;\ \text{the Gauss row }V=-\frac{Z\,\varepsilon_{\mathrm{EM}}}{d}\ \text{from }\mathrm{BM.48}(1)\text{ at }q_1=Z]:$$
$$\text{the levels are strictly ordered }E_1<E_2<E_3<\cdots<0\ \text{at every }(A,Z)\qquad[\text{machine: }1/n^{2}\text{ strictly decreasing}]:\qquad\textbf{the filling order is the level order — derived, not postulated};$$
$$(2)\quad\textbf{the reduced mass at general }(A,Z)\text{ (count route):}\qquad m_r^{(A,Z)}=\frac{m_N\,m_\ell}{m_N+m_\ell},\qquad m_N=\frac{6A\ln2}{\mathfrak h}+Z\,\Delta m_{\mathrm{EM}}\qquad[\mathrm{AT.3}(2);\ \mathrm{AT.5}(3)]:$$
$$\text{on the count route }m_r^{(A)}=\frac{6A\ln2}{\mathfrak h\,(3A+1)}\qquad[\mathrm{AT.5}(3)];\qquad\text{the class term enters the reduced mass through }m_N\ \text{and is priced, not adopted}\qquad[\mathrm{BM.30}(5)\text{'s pattern}];$$
$$(3)\quad\textbf{the filling map:}\qquad\text{the ground configuration of }Z\text{ shell leptons fills the directions in level order under the exclusion theorem}:\qquad Z\le\mathrm{Cum}(n)\iff\text{the first }n\text{ shells suffice}$$
$$[\mathrm{AT.11}(3),(4);\ \text{machine: the threshold census}]:\qquad Z\in\{2,10,28,60\}\ \text{are exactly the closed-shell classes at }n=1,2,3,4;$$
$$(4)\quad\textbf{the hydrogen and the }Z=2\textbf{ rows:}\qquad\textbf{hydrogen: }Z=1:\ \text{one lepton on the first direction, the ladder of AT.8};\qquad\text{the }Z=2\text{ class: the first shell closed with two doublet partners}$$
$$[\mathrm{AT.11}(3):\ \mathrm{cap}(1)=2]:\qquad\text{the naming of the }Z\ge2\text{ classes stands open per Def-AT.3}(4);$$
$$(5)\quad\textbf{the status:}\qquad\text{the ordering, the map and the census are exact on the independent-particle read};\qquad\text{the lepton–lepton residue of AT.12}(4)\ \text{stands};\qquad\neg\text{a measured periodic datum}\ [\mathrm{P5}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); Def-BM.8, BM.30(5), BM.48(1), BM.46 (Part 4); A-AT.1, Def-AT.3(4), AT.3(2), AT.5(3), AT.6(1), AT.8, AT.11(3), AT.11(4), AT.12(1), AT.12(4) (this part); exact rational orderings, integer threshold censuses [math; machine: `checks/verify_Atomic5.py` §G].

**Pf.**
$$
(1):\ \text{the Coulomb ladder at charge }Z\ \text{(the Gauss row scales the potential; the spectrum scales as }Z^2\text{)}\ [\text{math};\ \text{machine: the coefficient row}]
$$
$$
(2):\ \text{the reduced-mass identity at }m_N\text{'s two routes}\ [\text{machine}]
$$
$$
(3):\ \text{the level order }[\text{machine}];\qquad\text{the capacity thresholds: }\mathrm{Cum}(1)=2,\ \mathrm{Cum}(2)=10,\ \mathrm{Cum}(3)=28,\ \mathrm{Cum}(4)=60\ [\mathrm{AT.11}(4)\ \text{re-cited}]
$$
$$
(4):\ \text{the two rows instantiated};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The periodic order of the corpus is a monotonicity theorem: the levels of the charge-$Z$ Coulomb ladder are strictly ordered, so the filling map — which registered directions the leptons take — is the level order itself, and the closed-shell classes fall out as the cumulative capacity thresholds: two, ten, twenty-eight, sixty. The charge enters the ladder squared through the Gauss row, the reduced mass enters through the nucleus's count-route monomial with the scar term priced but not adopted, and the two rows the naming layer actually named — hydrogen and its two-lepton successor — sit at the map's first two thresholds. The corpus builds its periodic census out of a register, a wedge zero and a strictly decreasing sequence, and as with every census it owns, it records the counts and declines the comparison.

---
## Tier 5.6 — Transitions and Radiation: the Spectral Bookkeeping and the Rate Adjudication

### AT.14 — The transition ledger: the carrier, the jaw, and the balance

**Thm.**
$$(1)\quad\textbf{the energy rows are the ladder's rationals:}\qquad\Delta E_{n\to m}=\frac{\varepsilon_{\mathrm{EM}}^{2}\,m_r}{2}\Bigl(\frac{1}{m^{2}}-\frac{1}{n^{2}}\Bigr)>0\ \ (n>m)\qquad[\mathrm{AT.8}(2);\ \text{machine}]:\qquad\textbf{the transition energies are exact and coupling-scaled};$$
$$(2)\quad\textbf{the carrier is forced:}\qquad\text{the emitted carrier must be colour-free (the seals stay intact), EM-active, and charge-neutral for }Q\text{-preserving transitions}\qquad[\mathrm{BM.23}(5)\text{'s selection pattern}]:$$
$$\text{the photon class — the trivial chain of }V_2\text{ — is the unique such carrier in the inventory}\qquad[\mathrm{D3.7};\ \mathrm{EM.5};\ \mathrm{EM.6}\text{ (massless)};\ \mathrm{EM.8}\text{ (two polarizations)}];$$
$$(3)\quad\textbf{the capacity jaw:}\qquad\text{the transit content of the emitted leg is bounded by the channel: }\mathsf E\le\min(\delta h,\,4\,\delta\tau)\ln2\qquad[\mathrm{Cor\ CT0.6a};\ \mathrm{FT.153}]:$$
$$\text{the jaw bounds the leg's register content, }\neg\text{its energy: the energy bookkeeping of }(1)\text{ and the register bookkeeping are separate ledgers}\qquad[\mathrm{C10}\text{'s discipline}];$$
$$(4)\quad\textbf{the detailed balance:}\qquad\text{the emission and absorption bookkeeping are weight-symmetric: the Janus sum's move algebra carries the derived detailed balance, and the reverse transition's energy row is the sign-reversed rational}\qquad[\mathrm{FT.108}(4);\ \mathrm{BM.120}\text{'s register balance};\ \text{machine: the sign-reversed rows}];$$
$$(5)\quad\textbf{the forward-only arrow:}\qquad\text{the ledger's transition order is forward-only: }\neg\exists\,\tau^{-1}\qquad[\mathrm{A6};\ \mathrm{FT.144}(2);\ \mathrm{BM.23}(9)]:\qquad\text{the balance of }(4)\text{ is a weight symmetry, }\neg\text{a time reversal};$$
$$(6)\quad\textbf{the status:}\qquad\text{the energy rows, the carrier selection and the balance are exact; the rates are the next tag's adjudication}\qquad[\mathrm{P5}].$$

**Req.** A6 (Part 1); C10 (Part 1); D0.6, D0.7, D1.2, D3.7, D3.10 (Parts 1–2); CT0.6a, CT0.9 (Part 1); EM.5, EM.6, EM.7, EM.8 (Part 2); P5 (Parts 1–2); FT.144(2), FT.153 (Part 3); BM.23(5), BM.23(9), BM.120, BM.135(5), BM.142, FT.108(4) (Part 4); AT.8(2) (this part); exact rational bookkeeping, sign-reversed censuses [math; machine: `checks/verify_Atomic5.py` §H].

**Pf.**
$$
(1):\ \mathrm{AT.8}(2)\ \text{re-cited at the pair's own }m_r
$$
$$
(2):\ \mathrm{BM.23}(5)\text{'s three selection conditions instantiated at }Q\text{-preserving transitions};\qquad\text{the inventory: the photon class satisfies all three; the }q\text{-channel fails colour-freeness, the }\nu\text{-channel fails EM-activity}\ [\mathrm{FT.119};\ \mathrm{FT.142}(1)]
$$
$$
(3):\ \mathrm{Cor\ CT0.6a}\text{'s jaw and FT.153's attainment re-cited};\qquad\text{the locus separation of the two ledgers}\ [\mathrm{C10}]
$$
$$
(4):\ \mathrm{FT.108}(4)\text{'s derived detailed balance and BM.120's register balance re-cited};\qquad\text{the sign-reversed rationals}\ [\text{machine}]
$$
$$
(5):\ \mathrm{A6},\ \mathrm{FT.144}(2),\ \mathrm{BM.23}(9)\ \text{re-cited};\qquad(6):\ \text{the status record}.\ \blacksquare
$$

**Phys.** A shell transition writes two books and the corpus keeps them apart. The energy book is exact and old — the same rational differences the ladder always had, now read as emission gaps. The register book is the transit jaw: the emitted leg carries what a channel can carry, four bits to the tick, and no clause of the jaw ever mentions an energy. The carrier is forced the way the decay carrier was forced: colour-free because the seals must survive, EM-active because something must carry the read, and the inventory contains exactly one object with both properties — the trivial chain the corpus named photon when it named almost nothing else. Detailed balance comes from the Janus sum's own move algebra, a weight symmetry between emission and absorption that costs no arrow: the ledger still runs forward only, and the balance is a statement about weights, not about time.

### AT.15 — The rate adjudication: what is formed, what waits (the demand row (P5.3), scoped)

**Thm.**
$$(1)\quad\textbf{the formed piece:}\qquad\text{the transition's energy bookkeeping, carrier selection, capacity jaw and weight balance are the formed spectral rows}\qquad[\mathrm{AT.14}];$$
$$(2)\quad\textbf{the rate is a tick-weight, not a second-rate:}\qquad\Gamma\ \text{is a weight per tick, }\neg\text{a rate per external second}\qquad[\mathrm{BM.23}(9);\ \mathrm{D1.8};\ \mathrm{P5}]:$$
$$\textbf{no lifetime is derived and none is compared}\qquad[\mathrm{P5};\ \mathrm{BM.23}\text{'s Rmk discipline}];$$
$$(3)\quad\textbf{the no-flicker row:}\qquad\varepsilon_q=0\implies\text{the transition weight beyond the identity vanishes exactly}\qquad[\mathrm{BM.23}(8);\ \mathrm{BM.19}(3)]:\qquad\textbf{a non-flickering shell never radiates — the threshold is the only control};$$
$$(4)\quad\textbf{the open coupling:}\qquad\text{the tick-rate/field coupling requires emergent time; the reparametrization read is the formed piece of the demand row}\qquad[\mathrm{FT.131}(3);\ \mathrm{BM.131}(7);\ \mathrm{BM.6}(5)]:$$
$$\text{capture, decay and ionization rates stay open under the same clause}\qquad[\mathrm{AT.9}(4)];$$
$$(5)\quad\textbf{the status ((P5.3) scoped):}\qquad\text{constructed: the spectral bookkeeping and its conditional structure; open: the rates, under the named prerequisite}\qquad[\mathrm{P5}];\qquad\neg\text{a measured linewidth or lifetime}\ [\mathrm{P5}].$$

**Req.** A6 (Part 1); D0.4, D1.8 (Parts 1–2); CT0.8 (Part 1); P5 (Parts 1–2); FT.131(3), FT.144(2) (Part 3); BM.6(5), BM.19(3), BM.23(8), BM.23(9), BM.131(7) (Part 4); AT.9(4), AT.14 (this part); exact resolvent identities at rational thresholds [math; machine: `checks/verify_Atomic5.py` §H].

**Pf.**
$$
(1):\ \mathrm{AT.14}\text{'s rows assembled}
$$
$$
(2):\ \mathrm{BM.23}(9)\text{'s unit discipline re-cited};\qquad(3):\ \mathrm{BM.23}(8)\text{'s no-flicker theorem re-cited}:\ \varepsilon_q=0\implies x_+x_-=0\implies\text{the resolvent is }1
$$
$$
(4):\ \mathrm{FT.131}(3)\text{'s scope row and BM.131}(7)\text{'s reparametrization row re-cited};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The era builds everything a transition has except its speed. The energies are rationals, the carrier is unique, the jaw binds, the balance is derived, and the arrow is absolute — and then the corpus stops, exactly where it stopped for the decay vertex: a rate here is a weight per tick, the tick-rate/field coupling needs the emergent-time construction Part 4 named as a prerequisite, and the reparametrization read is the piece of that demand that already exists. One crisp theorem comes free: at the sharp crystallization threshold the transition weight dies identically, so a non-flickering shell never radiates — the same threshold controls the decay vertex, the flicker integral, and now the optical bookkeeping. No lifetime is derived, none is compared, and the open clause is recorded as open.

---

## Tier 5.7 — The Ensemble Rows and the Disposition of the Demand Ledger

### AT.16 — The ensemble rows at the atomic budgets, and the pair-correlation adjudication ((P5.7))

**Thm.**
$$(1)\quad\textbf{the formed law at every pair count:}\qquad P(E=2j)=\binom njp^{j}u^{\,n-j},\qquad w_{\mathrm{mat}}^{(n)}=\frac{1}{D_n},\qquad D_n=\frac{1-u^{n}}{1-u},\qquad\langle E\rangle^{(n)}_{\mathrm{mat}}=\frac{2n}{D_n}\qquad[\mathrm{BM.137}(1);\ \text{machine: the identities re-run at }n\le8];$$
$$(2)\quad\textbf{the ensemble binding at the nuclear budgets:}\qquad\mathcal B^{(n)}_{\mathrm{ens}}=-\frac{2n\,u\,D_{n-1}}{D_n}\cdot\frac{\ln2}{\mathfrak h}<0\ \ \forall\,u>0,\qquad=0\iff u=0\qquad[\mathrm{BM.137}(3);\ \text{machine: the sign census}]:$$
$$\textbf{the binding is the flicker's, not the count's, at every }n\qquad[\mathrm{BM.21}(3)\text{'s structure, uniform in }n];$$
$$(3)\quad\textbf{the two-bit floor survives every averaging:}\qquad E\ge2\ \text{on the whole materialized support}\implies\langle m_{\mathrm{hid}}\rangle^{(n)}_{\mathrm{mat}}>\frac{2\ln2}{\mathfrak h}\qquad[\mathrm{BM.137}(2);\ \mathrm{BM.70}(2)];$$
$$(4)\quad\textbf{the pair-correlation adjudication ((P5.7)):}\qquad\text{the formed measure is per-pair independent, and every ensemble-dependent row of this part carries a measure-free bound, a uniformity clause, or the marked specialization}\qquad[\mathrm{BM.143}(5)\text{'s uniformity-census pattern};\ \text{machine: the clause scan of Tiers 5.0–5.6}]:$$
$$\boxed{\ (\mathrm{R4}')\ \text{is adjudicated: no clause of the atomic era requires correlations beyond per-pair independence; the refinement stands as ensemble data, open, non-blocking}\ }$$
$$(5)\quad\textbf{the status:}\qquad\text{the law, the binding, the floor and the adjudication are exact; the currency separation (sector vs informational reads) stands}\qquad[\mathrm{BM.137}(4);\ \mathrm{BM.98};\ \mathrm{A\text{-}BM.9}].$$

**Req.** D0.4 (Part 1); CT0.8 (Part 1); P1, P5 (Parts 1–2); Def-H.32 (Part 3); FT.107(2) (Part 3); Def-BM.5, BM.19(2), BM.21(3), BM.70(2), BM.94(4), BM.98, BM.137(1), BM.137(2), BM.137(3), BM.137(4), BM.143(5), BM.143(7), A-BM.9 (Part 4); AT.3(3) (this part); binomial moment algebra over $\mathbb Q[p]$, polynomial identities, exact sign censuses [math; machine: `checks/verify_Atomic5.py` §C].

**Pf.**
$$
(1):\ \mathrm{BM.137}(1)\text{'s law re-derived coefficient-wise at }n\le8\ [\text{machine}]
$$
$$
(2):\ \text{the binding form and its sign census on }u\in[0,1)\ [\text{machine}]
$$
$$
(3):\ \mathrm{BM.137}(2)\ \text{re-cited}
$$
$$
(4):\ \text{the clause scan of this part's ensemble-dependent rows (AT.3}(3),\ \text{AT.12},\ \text{AT.13) against the three admissible forms}\ [\text{machine: the document pins}]
$$
$$
(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The nuclear and atomic ensembles inherit the law Part 4 formed for the meson: a geometric materialization weight, a mean squeezed between the floor and the ceiling, a binding that is strictly negative at every nonzero flicker and vanishes with it. Nothing in the atomic era needed more than per-pair independence — the clause scan over the era's ensemble-dependent rows finds each one carrying a measure-free bound, a uniformity clause, or a marked specialization, which is precisely the form in which Part 4 taught the ledger to record such things. The pair correlations remain what the closing tier reclassified them as: ensemble-refinement data, open, and blocking nothing.

### AT.17 — The remaining demand rows: (P5.4), (P5.5), (P5.6), (P5.9), (P5.10)

**Thm.**
$$(1)\quad\textbf{(P5.4) the frame section and the Dirac-type operator: restated open, with the constructed substitutes named:}\qquad\text{every spin row of this era uses the orientation doublet and the promoted rotation algebra — both constructed}\qquad[\mathrm{FT.122};\ \mathrm{BM.8}(3);\ \mathrm{BM.42}(7)]:$$
$$\text{the global Dirac-type operator on the extended carrier is }\neg\text{needed by any formed row of this part and stands unconstructed}\qquad[\mathrm{BM.6}(8);\ \mathrm{Def\text{-}H.34};\ \mathrm{FT.93}];$$
$$(2)\quad\textbf{(P5.5) the generation/flavour selection: the naming half declared, the occupancy half open:}\qquad\text{the Part-5 naming acts are A-AT.2's four labels, declared with no datum}\qquad[\mathrm{A\text{-}AT.2};\ \mathrm{Def\text{-}AT.3}]:$$
$$\text{which windings and which channel lines the named classes occupy is the (R3)-species residue — the winding assignment per class}\qquad[\mathrm{BM.129}(6);\ \mathrm{BM.136}(5);\ \mathrm{BM.60}(1)]:\qquad\textbf{named, not filled};$$
$$(3)\quad\textbf{(P5.6) item 16(c)'s remaining cells — geometry-program, non-blocking:}\qquad\text{the classification program's remaining cells (multi-solid chains, the single-vertex ladder, separated-contact hosting maps) are named for the cell program and are }\neg\text{atomic-era objectives}\qquad[\mathrm{BM.139}(6);\ \mathrm{BM.143}(7)]:\ \text{restated open};$$
$$(4)\quad\textbf{(P5.9) the finite-}\mathfrak h\textbf{ residue at the clean-bifurcation loci — geometry-program, non-blocking:}\qquad[\mathrm{FT.66}(3)]:\ \text{no atomic-era row consumes it; restated open};$$
$$(5)\quad\textbf{(P5.10) the embedding datum — dormant:}\qquad\text{no rotor read is formed in this era; the embedding datum stays a specification}\qquad[\mathrm{BM.6}(7);\ \mathrm{FT.87}(6)]:\ \text{restated open};$$
$$(6)\quad\textbf{the status:}\qquad\text{five rows dispositioned: one with substitutes named, one split declared/open, three restated open and non-blocking}\qquad[\mathrm{P5};\ \text{machine: the disposition census}].$$

**Req.** P5 (Parts 1–2); FT.66(3), FT.87(6), FT.93, Def-H.34 (Part 3); BM.6(7), BM.6(8), BM.8(3), BM.42(7), BM.60(1), BM.129(6), BM.136(5), BM.139(6), BM.143(7) (Part 4); A-AT.2, Def-AT.3, AT.10(1), AT.10(4), AT.4(4) (this part); the disposition census [math; machine: `checks/verify_Atomic5.py` §H].

**Pf.**
$$
(1):\ \text{the usage scan of this part's spin rows}\ [\text{machine: the document pins}];\qquad\mathrm{BM.6}(8)\text{'s specification re-cited as open}
$$
$$
(2):\ \mathrm{A\text{-}AT.2}\text{'s scope and the (R3) rows re-cited};\qquad(3)\text{–}(5):\ \text{the three rows restated at their own loci}
$$
$$
(6):\ \text{the disposition census against BM.143}(7)\text{'s demand text}\ [\text{machine}].\ \blacksquare
$$

**Phys.** Five demand rows remain, and the era's answer to each is a placement, not a promise. The frame section and the Dirac operator stay unconstructed — and the tier shows they were not silently needed: every spin row of the shells runs on the orientation doublet and the promoted rotation, both built from Parts 1–3 with no new object. The generation selection is done in the only coin the corpus spends for names: the labels are declared, the occupancy stays the open residue it has been since the baryon's statistics was left "complete as a function and open as a value." And three rows — the classification cells, the finite-𝔥 bifurcation residue, the rotor embedding — belong to the geometry program, not to the atom; the era restates them at their own loci and blocks nothing on them.

---

## Tier 5.8 — Consumption and Calibration

### AT.18 — The census-consumption law II

**Thm.**
$$(1)\quad\textbf{the substrate:}\qquad\text{the enumerative substrate of this era remains the Census block — the 25 Category-B cells with their configuration spaces, counts and consumption rows}\qquad[\text{Census charter and §Consumption};\ \mathrm{BM.5}(1);\ \mathrm{BM.143}(8)\text{'s frozen row}]:\ \text{every construction of this part consumes cells by tag citation; no cell is added};$$
$$(2)\quad\textbf{the family table:}$$

| census family | cells | configuration space supplied | consumption at the atomic era |
|---|---|---|---|
| floor cards and ladders | FT.28, FT.32, FT.35, FT.42–FT.45, FT.49–FT.51, FT.63 | the computed fermion floors with full read columns | the digon floor behind every mass read (AT.4); the $E_{\mathrm{int}}=6$ decomposition behind the nuclear count route (AT.3); the $4\mathbb Z$ phase classes and the junction lock rows (AT.2); the two-bit floor (AT.4, AT.16) |
| loop and cover classes | FT.64, FT.65, FT.69, FT.78, FT.96 | admissible-loop lattices, coarse-grained degeneracies, amplitude censuses, Aut-orbits | the flicker pools behind the ensemble binding $\mathcal B^{(n)}_{\mathrm{ens}}$ (AT.16) and the CP-pair content of the mixed cells (AT.1(2)) |
| pole and mass multiplets | FT.76 | defect-angle pole reads under both priced convention variants, with the ceiling | the pole-side ceilings every composite read inherits; the priced-variant pattern behind the read-choice rows (AT.5(5), AT.12(4)) |
| form-factor tables | FT.98, FT.99 | polygon and Platonic form factors with growth and dominance rows | the size-bound range checks for the extended atomic skeletons |
| audit ledgers | FT.81, FT.83, FT.84, FT.114, FT.120 | the read-class inventory, the rung-emergence ledger, the ceiling taxonomy, the quarantined comparison rows | the read-species taxonomy of the atomic rows; the P1/P5-compliant comparison template; the quarantine discipline of every external-facing row |
| topology-blind cells | FT.105 | graph counts and canonical skeletons, budget-regularized | the regulated topology pool of the nuclear and atomic supports |

$$(3)\quad\textbf{the consumption count closes:}\qquad11+5+1+2+5+1=25\qquad[\text{machine: the set arithmetic of BM.5}(2)\text{'s partition, re-run}];$$
$$(4)\quad\textbf{the conditioning law:}\qquad\text{sector-conditioned sums run on Def-H.32(4)'s labels over (2)'s pools; the amplitude/norm dichotomy and its bridge residue are item-13 content}\qquad[\mathrm{Def\text{-}H.32}(4);\ \mathrm{FT.67}\text{–}\mathrm{FT.68};\ \mathrm{FT.80}].$$

**Req.** The Census block (all 25 cells); Def-H.32, FT.67, FT.68, FT.80 (Part 3); Def-BM.5 (Part 4); BM.5(1), BM.5(2), BM.143(8) (Part 4); Def-AT.2, AT.1, AT.3, AT.4, AT.16 (this part); exact set arithmetic [math; machine: `checks/verify_Atomic5.py` §H].

**Pf.** $(2)$: the consumption map — each family row references its cells by tag; every Census tag occurs in exactly one family row [machine: $11+5+1+2+5+1=25$]. $(1),(3),(4)$: charter rows and the frozen-Census clause re-cited. $\blacksquare$

**Phys.** The atomic era adds no cell to the census and empties none: the same twenty-five computed spaces that fed the baryomesonic era feed this one, read at new counts. The floor cards give the digon twice — once as the lepton's mass, once as the baryon's unit — the loop classes pool the flicker behind every ensemble binding, the audit ledgers keep the comparison template honest, and the topology-blind cells regulate which supports the atomic sums may range over. The partition closes at twenty-five exactly as it did one era earlier; the consumption law is the same law with a new column.

### AT.19 — The calibration consolidation

**Thm.**
$$(1)\quad\textbf{zero additions:}\qquad\text{this part introduces no free internal parameter, no dimensionful scale, and no P4 member}\qquad[\mathrm{P1};\ \mathrm{P4};\ \mathrm{\§Cal\text{-}5};\ \text{machine: the symbol census of the part's new rows}];$$
$$(2)\quad\textbf{the consolidated register (a consolidation, }\neg\textbf{an addition):}\qquad$$
$$\begin{array}{l|l|l}\text{row} & \text{content} & \text{status}\\\hline\mathfrak h & \text{the single free dimensionful scale} & \text{inherited [P1; D2.9]}\\\hline\mathrm{Cal\text{-}F} & r,\ \hat\mu^{2},\ \hat\mu'^{2},\ \alpha,\ \mu,\ \mu_\nu,\ \text{the fugacities} & \text{inherited, values undeclared}\\\hline\rho_{\mathrm B} & \hat\mu'^{2}\mathfrak h^{2}/(\ln2)^{2},\ \text{the bridge-ratio slot} & \text{slot declared, value }\neg\text{issued [A-BM.9]}\\\hline e_0 & \text{the electric coupling} & \textbf{used symbolically in this part, value }\neg\text{issued [C-AT.1]}\\\hline\varepsilon_q & \text{the A4 crystallization threshold} & \text{axiom datum [D0.4], }\neg\text{a parameter}\end{array}$$
$$(3)\quad\textbf{the symbolic-use row:}\qquad\text{every row of Tiers 5.2–5.6 that carries }e\text{ carries it as a symbol inside an exact rational function; no row issues a value; no row fits one}\qquad[\mathrm{C\text{-}AT.1};\ \mathrm{EM.25}(7);\ \mathrm{BM.55}(6)\text{'s precedent}];$$
$$(4)\quad\textbf{the count row:}\qquad\text{the parameter count is unchanged from the end of Part 4}\qquad[\text{machine: the packaging census against \S Cal-BM}];\qquad\neg\text{a measured value enters any row}\ [\mathrm{P5}].$$

**Req.** P1, P4, P5 (Parts 1–2); D0.4, D2.9 (Parts 1–2); EM.25(7) (Part 2); Cal-F (Part 3); §Cal-BM, A-BM.9, BM.55(6) (Part 4); §Cal-5, C-AT.1 (this part); the symbol census [math; machine: `checks/verify_Atomic5.py` §H].

**Pf.**
$$
(1),(3),(4):\ \text{the symbol and token censuses of the part's rows}\ [\text{machine: the document pins}];\qquad(2):\ \text{the register assembled from the cited rows, no new symbol introduced}\ [\text{machine}].\ \blacksquare
$$

**Phys.** The era's books balance before they are audited: nothing was added. The one calibration act is a log, not a number — the electric coupling, carried since the electroweak tier as an unissued slot, is hereby used symbolically in exactly the way the neutron–proton ratio used it: inside exact rational functions, never as a value. The register that leaves Part 5 is the register that entered it, with one row's discipline extended from "priced and unused" to "priced and used, still unissued."

---

## Tier 5.9 — The Era Closure: the Demand Ledger Balanced

### AT.20 — The era closure: the disposition of (P5.1)–(P5.10) and the balanced ledger

**Thm.**
$$(1)\quad\textbf{the demand-ledger disposition (BM.143(7)'s ten rows, adjudicated):}$$
$$\begin{array}{l|l|l}\text{row} & \text{disposition} & \text{locus}\\\hline(\mathrm{P5.1})\ \ \text{the EM binding channel} & \textbf{constructed} — \text{the grammar declared, the pole ladder derived, the category bar's object formed} & [\mathrm{A\text{-}AT.1};\ \mathrm{Def\text{-}AT.4};\ \mathrm{AT.6};\ \mathrm{AT.7}]\\\hline(\mathrm{P5.2})\ \ \text{the lepton mass read} & \textbf{constructed at the informational floor} — \text{two bits on both lines; the inertial scale stays undeclared, the conversion residue named} & [\mathrm{AT.4};\ \mathrm{AT.5}]\\\hline(\mathrm{P5.3})\ \ \text{the dynamics rates} & \textbf{split: the spectral bookkeeping formed; the rates open under the named prerequisite} & [\mathrm{AT.14};\ \mathrm{AT.15};\ \mathrm{FT.131}(3);\ \mathrm{BM.131}(7)]\\\hline(\mathrm{P5.4})\ \ \text{the frame section / Dirac operator} & \textbf{restated open, non-blocking} — \text{the constructed substitutes named} & [\mathrm{AT.17}(1)]\\\hline(\mathrm{P5.5})\ \ \text{the generation/flavour selection} & \textbf{split: the naming declared; the occupancy open ((R3) species)} & [\mathrm{A\text{-}AT.2};\ \mathrm{AT.17}(2)]\\\hline(\mathrm{P5.6})\ \ \text{item 16(c)'s cells} & \textbf{restated open, non-blocking} — \text{geometry-program content} & [\mathrm{AT.17}(3)]\\\hline(\mathrm{P5.7})\ \ \text{the pair correlations} & \textbf{adjudicated: the formed measure suffices for every row; the refinement is open ensemble data} & [\mathrm{AT.16}(4)]\\\hline(\mathrm{P5.8})\ \ \text{the }n\ge4\text{ sealing cells} & \textbf{constructed} — \text{the partition cells with the type selection} & [\mathrm{AT.1}]\\\hline(\mathrm{P5.9})\ \ \text{the finite-}\mathfrak h\text{ residue} & \textbf{restated open, non-blocking} — \text{geometry-program content} & [\mathrm{AT.17}(4)]\\\hline(\mathrm{P5.10})\ \ \text{the embedding datum} & \textbf{restated open, dormant} — \text{no rotor read formed} & [\mathrm{AT.17}(5)]\end{array}$$
$$(2)\quad\textbf{the discharged Part-4 rows:}\qquad\mathrm{BM.48}(3)\text{'s }\neg\text{constructed row — discharged [AT.6]};\qquad\mathrm{BM.54}(4)\text{'s unconstructed atom — discharged [AT.6](2)};$$
$$\mathrm{BM.43}(2)\text{'s symbolic lepton rows — discharged at the informational floor [AT.4]};\qquad\text{the rows are re-scoped at their own loci,}\ \neg\text{retracted};$$
$$(3)\quad\textbf{the era's own open rows (honest remainder):}\qquad\text{the inertial mass scales }(\mu,\mu_\nu)\ \text{and the two-reads conversion [AT.4}(3)];\ \text{the rates [AT.15]};\ \text{the many-body shell energy [AT.12}(4)];$$
$$\text{the winding occupancy per named class [AT.11}(6)];\ \text{the naming of the }Z\ge2\text{ classes [Def-AT.3}(4)];\ \text{the five geometry-program and interface rows [AT.17]};$$
$$(4)\quad\textbf{the standing rules:}\qquad\neg\exists\ \text{a measured external value in any clause}\ [\mathrm{P5}];\qquad\neg\exists\ \text{a new dimensionful scale}\ [\mathrm{P1}];\qquad\neg\exists\ \text{a P4 addition}\ [\mathrm{\§Cal\text{-}5};\ \mathrm{AT.19}];$$
$$\text{species names confined to the identification layers}\ [\mathrm{Def\text{-}AT.3};\ \mathrm{A\text{-}AT.2}];\qquad\text{the chart-side rows carry their conditionality}\ [\mathrm{BM.10}(3);\ \mathrm{BM.48}(2)\text{'s pattern}];$$
$$(5)\quad\textbf{the DAG row:}\qquad\text{nothing in the canon cites this part; the citations of this part resolve to Parts 1–4, Census cells, and earlier tags of this part}\qquad[\text{machine: the citation closure scan}];$$
$$(6)\quad\textbf{the adjudication:}\qquad\boxed{\ \textbf{the Atomic era closes with its ledger balanced: two demand rows constructed, two split with the formed halves named, one adjudicated, five placed — and the atom, absent from the inventory since BM.48 drew its potential, a constructed object}\ }$$
$$[\text{machine: the row-by-row discharge census against BM.143}(7)\text{'s demand text and BM.152}(8)\text{'s re-citation}].\ \blacksquare$$

**Req.** P1, P5 (Parts 1–2); FT.131(3), FT.66(3), FT.87(6), FT.93, Def-H.34 (Part 3); Def-BM.6, BM.6(5), BM.6(7), BM.6(8), BM.43(2), BM.48(3), BM.54(4), BM.60(1), BM.129(6), BM.131(7), BM.136(5), BM.139(6), BM.143(7), BM.152(8) (Part 4); A-AT.1, A-AT.2, Def-AT.3, Def-AT.4, AT.1, AT.4, AT.5, AT.6, AT.7, AT.11, AT.12, AT.14, AT.15, AT.16, AT.17, AT.19 (this part); the row-by-row discharge census, the citation-closure scan [math; machine: `checks/verify_Atomic5.py` §H].

**Pf.**
$$
(1):\ \text{the ten rows against their loci, clause by clause}\ [\text{machine: the document pins}]
$$
$$
(2):\ \text{the three re-scope rows against their Part-4 texts}\ [\text{machine: the document pins}];\qquad(3):\ \text{the remainder list against the tiers}
$$
$$
(4),(5),(6):\ \text{the standing-rule record, the citation-closure scan, and the discharge census}\ [\text{machine}].\ \blacksquare
$$

**Phys.** The era that opened with a shopping list closes with every item initialed. The binding channel the corpus demanded first is built — a declared grammar whose theorems are the conditional rows of Part 4 made good — and the lepton floors beside it, two bits on both lines with the inertial scale honestly still undeclared. The rates are split the way the corpus splits everything it cannot yet own: the spectral bookkeeping formed, the speeds waiting on emergent time. The frame operator, the classification cells, the bifurcation residue and the rotor embedding are placed rather than performed, each at its own locus, each blocking nothing. And the discharge is spelled back to the rows that demanded it: BM.48's negative — no EM sealing grammar — stands re-scoped at the tier that built one; the atom that BM.54 called unconstructed is constructed; the shopping list of the closing tier is, row by row, a ledger of dispositions. The books balance. The atom is on the books.

---

---

## Extension charter (Tiers 5.10–5.15): the Two Bridges — the Scope Clock, the Unified Mass, and the Opened Atomic Structure

**Namespace (extension tiers).** The extension owns (forward pointers to the definitions below): Def-AT.6–Def-AT.7; AT.21–AT.37; the declarations A-AT.3–A-AT.4. Tiers 5.10–5.15 in series order.
**0.1b Charter of the extension tiers.** The extension tiers continue the atomic era — incrementally, inside this part, with no new era declared — into the layer of the two bridges: the constructions the earlier eras located as obstructions and left standing at their own loci, named with precision, and built here. Its foundation stack, by citation: (i) the singular force and its mask [A8; CT2.3, CT2.4; FT.11]: one complete operator, always applied in full, whose masked restrictions are the only interactions the corpus owns [BM.52(1)]; (ii) the sector-census pattern [BM.52(3)–(5): five zeros and one monomial, twice-derived]; (iii) the metric-energy read [Def-BM.10; BM.34: the ADM split, the dispersion, the zero-point bound, the rest slice]; (iv) the canonical pair and its obstruction discipline [BM.10(1)–(6), with the Rmk that governs them all: *the negative theorems locate the domain in which a structure can exist rather than asserting the structure*]; (v) the Born width and its ladder [Def-BM.4; BM.13]; (vi) the non-uniform clock and the Mandelstam–Tamm machinery [BM.53]; (vii) the constructed atom and its ladder [Def-AT.4; AT.6–AT.9]; (viii) the transition ledger and the rate adjudication [AT.14; AT.15]; (ix) the running coupling's profile [BM.18(2)]; (x) the era-locality discipline itself [AT.20(2)'s re-scope pattern]. Its outputs: the singular force censused on the bound channel, with the D⁻ cap and the single-qubit reduction (Tier 5.10); the dynamics-of-$Q$ bridge — A-AT.1's declared price re-derived through the force, the opened classes and the continuum (Tier 5.11); the per-rung metric split and the fuzziness product (Tier 5.12); the scope-local $(t,E)$ bridge and the width ledger that brackets AT.15's waiting half (Tier 5.13); the unified mass observable — pole + bracket — with the incommensurability re-adjudication (Tier 5.14); the opened-structure census, the era-locality table, and the closure (Tier 5.15). Its enumerative substrate remains the Census block: the 25 cells, consumed by tag citation and extended by no new cell.
**0.2b Standing bars of the extension tiers.** The era-locality discipline governs every negative row the extension touches: an obstruction binds in the domain where it was proved and is bridged, never revoked — discharged at its own locus or re-scoped with its domain restated [BM.10's Rmk; AT.20(2)'s pattern]. The singular-force row stands as the extension's inherited constraint: one complete operator $\mathbf F$ [A8], every interaction read a masked restriction of it [CT2.3], the scalar stress of any bound of the $D^-$ equation-of-state form with no new saturation content on the bound channel [BM.9(4); D4.1, D4.2; CT4.1], $D^+$ uniform, configuration-blind stretch shared by all classes [D4.3; CT4.5], and the Janus blocks $J^\pm$ carrying the creation/dissolution moves and no stationary read [D1.2; FT.108(1); CT1.12a(2)]. Amplitude $\ne$ mass at the free members [FT.79(5); FT.67(3a); FT.68(4); BM.37(3)]. The bracket discipline: a spread is an inequality, never a value; no bracket endpoint is ever booked as a mass. No external data outside quarantined audit rows [Census FT.114, FT.120]; no measured external constant is identified with any corpus quantity [P5]; the chart-side rows carry their conditionality explicitly [BM.10(3); BM.48(2)'s scope pattern]; species names are labels on derived tuples and carry no datum [Def-BM.3(6),(7); Def-AT.3(3); A-AT.2].

---

## §Cal-5b — Free internal parameters of the extension tiers (P4-class)

**None introduced by the extension tiers.** Inherited and undeclared: the single dimensionful scale $\mathfrak h$ [P1]; the fermion-era registry Cal-F ($r=x_+/x_-$; $\hat\mu^2$, $\hat\mu'^2$; the Ansatz-B temperature $\alpha$; the channel scales $\mu$, $\mu_\nu$; the formal fugacities) [Cal-F]; the baryomesonic register [Cal-BM]: the bridge ratio slot $\rho_{\mathrm B}$ [A-BM.9, value $\neg$issued], the electric-coupling slot $e_0$ [C-BM.2, value $\neg$issued], and the channel-scale rows [C-BM.3]; the atomic era's symbolic-use log [C-AT.1].

**The symbolic-use log (consolidation, $\neg$addition; the parameter count is unchanged).** Every new row of the extension tiers — the width brackets, the resolvability thresholds, the fuzziness products, the unified pole — is an exact rational or radical form in the corpus symbols $(e,\mathfrak h,\ln2,c)$ over the integer counters, with no numerical value attached to $e$ anywhere [C-AT.1 re-logged]. The width read adds no parameter: it is built from $\hbar=1$ on the chart [BM.10(3)], the tick [D1.8], the floor counts $E_{\mathrm{int}}\in\{2,6\}$ [AT.4(1); Census FT.35(2)], and $\ln2$. The flicker threshold $\varepsilon_q$ remains the A4 datum [D0.4]. Machine verification uses declared rational witnesses in the checker only; no witness value enters the canon.

---

## §A-AT (extension) — Logged declarations II (issued before use)

**A-AT.3 (the scope application; issued before AT.29 and consumed in Tiers 5.12–5.14).** Part 4's energy read is theorem-local: $E=-p_0$ exists under BM.8(2)'s declared stationarity scope, inherited at the point of use [Def-BM.10(5); BM.53(6)], and the sealed sectors satisfy the scope structurally [Tier BM.4's Phys]. The reads of Parts 1–4 and the opening tiers applied the scope at the sealed colour sectors. This declaration applies the scope to the constructed EM-pair channel — the atom's bound read of Def-AT.6 (a forward pointer to the extension's first definition) — as a **read-side inheritance**: within the scope, the bound channel's energy charge, its masked orbit and its Mandelstam–Tamm duals exist; outside the scope, the tick's irreversibility resumes untouched [A6; L2; BM.53(3)]. The declaration is constitutive in exactly one respect — the scope's locus — and non-derived in that same respect: no theorem of the prior corpus forces the bound channel's read to inherit the scope, and Part 4's obstructions were proved on other domains [BM.10(1),(4)]. What the declaration does **not** do: it adds no axiom, no dimensionful scale, no P4 member [P1, P4]; it issues no value of $e$ [C-AT.1]; it constructs no time operator — the register no-go stands at its locus [BM.10(4)] — and no emergent time: FT.131(3)'s named prerequisite for the absolute rates is untouched, and the extension brackets the rates without paying them.

**A-AT.4 (the naming-scope extension II; issued before AT.25).** Def-AT.3(4) names the extension condition: naming beyond the four atomic names requires a further logged declaration. This declaration extends the naming scope of Def-BM.3, Def-BM.6 and Def-AT.3 to the extension tiers, and admits exactly one new label schema — **Atom$(A,Z)$** for the constructed classes of the opened-classes row (a forward pointer: AT.25), with level labels **Atom$(A,Z;n)$** for the pole ladder — attached to derived tuples (junction grammar, count $A$, charge class $Z$, pole index $n$, statistics $\varepsilon=(-1)^{A+Z}$ at the floors [AT.12(3)]). No name carries a datum; no mass value, coupling value, lifetime, radius or linewidth attaches to any named row [Def-BM.3(6) pattern]; names occur in the extension tiers only [Def-BM.3(7) extended]; extension beyond this schema requires a further logged declaration.

---

## Tier 5.10 — The Singular Force on the Bound Channel: the Census, the D⁻ Cap, and the One-Node Reduction

### AT.21 — The masked force on the bound channel: the sector census at the atom

**Thm.**
$$(1)\quad\textbf{the force is one and complete:}\qquad\mathbf F\ \text{acts always in full, and no sub-block restriction is an A8 force}\qquad[\mathrm{A8};\ \mathrm{FT.142}(2);\ \mathrm{BM.52}(1)]:$$
$$\text{the bound channel's interaction read is the masked restriction of the one operator to the channel's active space}\qquad[\mathrm{CT2.3},\ \mathrm{CT2.4}\text{'s restriction pattern}]:$$
$$(2)\quad\textbf{the sector census on the bound channel (the atom's table):}$$
$$\begin{array}{l|l|l}\text{sector} & \text{contribution on the bound channel} & \text{the derived ground}\\\hline J^\pm\ (\text{seals}) & 0\ \text{on every stationary read} & \text{the Janus blocks carry the creation/dissolution moves [D1.2; FT.108(1)] and no metric coordinate [CT1.12a(2)] — they act at capture and unbinding, never on the pole}\\\hline G,H\ (\text{metric blocks}) & 0\ \text{in every bound-vs-free difference} & \text{charge exponent }0\ \text{on all seven geometric monomials [BM.28(1); BM.53(2)]}\\\hline W\ (\text{weak/shift}) & 0\ \text{in the splitting reads} & \text{the shift enters the dispersion as the shared drag [BM.34(3)]; the Casimir is branch data [BM.40(3)]}\\\hline\text{colour} & 0 & \text{both members are sealed singlets [FT.117; CT3.18]; the pair admits no colour junction [AT.7(3)]}\\\hline D^+ & 0\ \text{in every difference read} & \text{uniform, configuration-blind, carried by }\Lambda\ \text{[CT1.22; CT4.1; D4.3]}\\\hline D^- & \textbf{the cap: zero new saturation content} & \text{the dust share is member-wise [BM.9(4)]; the saturation is locked at the sealed junctures [D4.1; CT4.1]; the pair junction adds none [machine: the block census]}\\\hline\mathrm{EM} & \textbf{the only channel-active sector} & \text{the pair grammar's binding read [BM.52(3)'s EM row; BM.46; A-AT.1]}\end{array}$$
$$(3)\quad\textbf{the totality row:}\qquad\boxed{\ \mathbf F\big|_{\text{pair}}\ =\ F_{\mathrm{EM}}\big|_{\text{mask}}\ \oplus\ \text{the members' own sealed reads}\ }$$
$$[\text{machine: the census sum of five zeros, one cap and one active sector}]:\qquad\textbf{one singular force, one active mask on the bound channel};$$
$$(4)\quad\textbf{the status:}\qquad\text{the census is the atom-channel instance of BM.52(3)'s pattern, each zero backed by its own frozen row rather than by silence};\qquad\neg\text{a new force},\ \neg\text{a new sector},\ \neg\text{a new parameter}.$$

**Req.** A8 (Part 1); CT1.12a(2), CT1.22, CT2.3, CT2.4, CT3.18, CT4.1, CT4.5 (Part 2); D1.2, D4.1, D4.3 (Parts 1–2); P5 (Parts 1–2); FT.108(1), FT.117, FT.142(2) (Part 3); BM.9(4), BM.28(1), BM.34(3), BM.40(3), BM.46, BM.52(1), BM.52(3), BM.52(5) (Part 4); A-AT.1, AT.7(3) (this part); the sector-census structure [math; machine: `checks/verify_Atomic5.py` §I].

**Pf.**
$$
(1):\ \mathrm{A8}\text{'s completeness and FT.142}(2)\text{ re-cited};\qquad\text{the mask pattern of CT2.3/CT2.4 instantiated at the bound channel}
$$
$$
(2):\ \text{each row is the cited frozen zero, re-anchored at the atom's channel}:\ \mathrm{D1.2}/\mathrm{FT.108}(1)/\mathrm{CT1.12a}(2);\ \mathrm{BM.28}(1)/\mathrm{BM.53}(2);\ \mathrm{BM.34}(3)/\mathrm{BM.40}(3);\ \mathrm{FT.117}/\mathrm{CT3.18}/\mathrm{AT.7}(3);\ \mathrm{CT1.22}/\mathrm{CT4.1}/\mathrm{D4.3};\ \mathrm{BM.9}(4)/\mathrm{D4.1}/\mathrm{CT4.1};\ \mathrm{BM.52}(3)\text{'s EM row}\ [\text{machine: the census structure}]
$$
$$
(3):\ \text{the sum over the table}\ [\text{machine}];\qquad(4):\ \text{the standing-rule record}.\ \blacksquare
$$

**Phys.** Ask every sector of the one force what it contributes to the atom's bound read, and the answer is the census table — each zero its own theorem, each cap its own lock. The Janus pair handles the comings and goings: it seals and unseals, and on the stationary pole it is silent. The metric blocks cannot see charge. The weak block drags uniformly and splits nothing. Colour is blind twice over — each member is already a sealed singlet, and the pair builds no junction of its own. The dark stretch is uniform and cancels in every difference; the dark scalar is the cap, and the cap's content is locked where it was locked before the atom existed — the pair junction adds no new saturation, so the atom inherits the cap instead of loading it. What remains is the one sector the grammar declared: electromagnetism, on one masked restriction of one operator. The atom is not held by a force of its own kind; it is read through a mask of the only force there is.

### AT.22 — The D⁻ cap: the form, the inheritance, and the sub-saturation bound

**Thm.**
$$(1)\quad\textbf{the form row:}\qquad\text{the scalar (dust) content of any bound read carries the }D^-\text{ equation-of-state form }\mathrm{diag}(\rho,0,0,0)\ \text{member-wise}\qquad[\mathrm{BM.9}(4)]:$$
$$(2)\quad\textbf{the inheritance row (the cap is not loaded):}\qquad\text{the saturation content is locked at the sealed }\varepsilon\text{-junctures [D4.1; CT4.1]; the pair junction contributes no new block [AT.21(2)'s census row; AT.7(3)]:}$$
$$\boxed{\ \Delta E_{D^-}\ =\ 0\ \ \text{across the binding: the bound channel inherits the members' cap and adds none}\ }\qquad[\text{machine: the block census}];$$
$$(3)\quad\textbf{the sub-saturation row:}\qquad\text{the binding share of the members' rest scale is bounded:}$$
$$\frac{|E_1|}{m_p+m_\ell}\ =\ \frac{\varepsilon_{\mathrm{EM}}^{2}}{2}\cdot\frac{3\,(1+c\,\varepsilon_{\mathrm{EM}})}{\bigl(4+3\,c\,\varepsilon_{\mathrm{EM}}\bigr)^{2}}\ \le\ \frac{3}{32}\qquad[\mathrm{AT.6}(3);\ \text{machine: the monotone grid, sup at }c\,\varepsilon_{\mathrm{EM}}=0]:$$
$$\textbf{the atom sits strictly inside the }D^-\textbf{ saturation ledger: the binding never exceeds three over thirty-two of the members' rest scale};$$
$$(4)\quad\textbf{the general-}A\textbf{ row:}\qquad\text{on the count route }m_N=3A\,m_\ell:\quad\frac{|E_1|^{(A)}}{m_N+m_\ell}=\frac{3A}{(3A+1)^{2}}\cdot\frac{\varepsilon_{\mathrm{EM}}^{2}}{2}\qquad[\text{machine: the exact identity}]:$$
$$\text{the binding fractions tighten along the exact }(3A+1)^{2}\text{ ladder — }\tfrac{3}{32}\ \text{at }A=1,\ \text{strictly decreasing in the count};$$
$$(5)\quad\textbf{the status:}\qquad\text{the cap rows are exact and symbolic in }e;\qquad\neg\text{a measured density,}\ \neg\text{a comparison}\ [\mathrm{P5}].$$

**Req.** CT2.1 (Part 2); D4.1, D4.2 (Parts 1–2); P1, P5 (Parts 1–2); FT.44(4) (Census); Census FT.35(2) (row-wise); BM.9(4), BM.46, BM.48(2) (Part 4); AT.4(1), AT.5(1), AT.5(2), AT.6(1), AT.6(3), AT.7(3) (this part); AT.21 (this part); exact rational monotone censuses [math; machine: `checks/verify_Atomic5.py` §I].

**Pf.**
$$
(1):\ \mathrm{BM.9}(4)\text{'s dust form re-cited member-wise}
$$
$$
(2):\ \text{the pair junction census [AT.7}(3)\text{'s no-junction row]};\qquad\text{the locked-saturation rows [D4.1; CT4.1] re-cited}: \text{no new block}\implies\Delta E_{D^-}=0\ [\text{machine}]
$$
$$
(3):\ f(x)=\tfrac32\,\tfrac{1+x}{(4+3x)^2}:\quad f'(x)=\tfrac32\,\tfrac{(4+3x)-6(1+x)}{(4+3x)^3}=\tfrac32\,\tfrac{-2-3x}{(4+3x)^3}<0\ \ \forall x\ge0;\qquad f(0)=\tfrac{3}{32}\ [\text{machine: the exact sup}]
$$
$$
(4):\ m_r^{(A)}/(m_N+m_\ell)=m_Nm_\ell/(m_N+m_\ell)^{2}=3A/(3A+1)^{2}\ \text{on the count route [AT.5(2)'s ratio form at general }A]\ [\text{machine}];\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The cap needs one sentence of care, because "capped" is doing structural work. The scalar content of any composite in this corpus has the neutron's equation of state — pressureless dust, the $D^-$ form — and the saturation that form books is locked at the colour seals, where it has been since the baryons. A neutral pair builds no new seal, so the atom's binding cannot open the lock: the dark-scalar ledger across the binding is exactly zero, and what the binding does move is bounded above by three over thirty-two of the members' rest mass at the loosest coupling the symbol algebra admits, tightening along the exact three-$A$-plus-one-squared ladder as the count grows. The atom gravitates, when it gravitates, as its members do — dust at the members' own widths — and never as a new saturation source. The cap is inherited, not tested.

### Def-AT.6 — The bound channel: the single-qubit line at the reduced mass

**Def.** The **bound channel** of the constructed EM-pair composite [Def-AT.4] is the read-side object on which every row of this part lives:
$$(1)\quad\textbf{the active space:}\qquad\text{the lepton channel's carrier line — the single-qubit space with }\dim\mathcal H_q=2\ \text{[A1; the single-qubit line of CT0.9's mechanism; FT.122's doublet rides it]};$$
$$(2)\quad\textbf{the reduction:}\qquad\text{the two-body read reduces to the one-body read at }m_r\qquad[\mathrm{BM.48}(2);\ \mathrm{AT.5}(1)]:$$
$$\text{the nucleus enters the channel through }(Z,\ m_r)\ \text{and in no other way}\qquad[\text{machine: the parameter census of AT.5--AT.8's rows}];$$
$$(3)\quad\textbf{the mask:}\qquad\text{the channel's force is }F_{\mathrm{EM}}\big|_{\text{mask}}\ \text{under the channel's rung mask}\qquad[\mathrm{CT2.3};\ \mathrm{CT2.4}\text{'s pattern; AT.21(3)}]:$$
$$\text{one masked restriction of the one operator — the restriction is the channel's mask,}\ \neg\text{a sub-block of the force}\qquad[\mathrm{FT.142}(2)];$$
$$(4)\quad\textbf{the channel data:}\qquad(A,\ Z;\ n;\ \varepsilon)\qquad\text{with }\varepsilon=(-1)^{A+Z}\ \text{at the floors}\qquad[\mathrm{AT.12}(3)];$$
$$(5)\quad\textbf{the scope:}\qquad\text{chart-side under BM.10(3)'s scope; the register bars untouched [BM.10(1)]; the stationarity scope applied by A-AT.3}.$$

**Rmk (the singular-force row, restated as an output).** The era's inherited constraint — one singular force, operating one qubit channel at one node, capped by $D^-$ — is not an assumption of this part. It is the census output of AT.21 (one active mask; the rest do what the rest do, which on the bound channel is nothing), the cap rows of AT.22 ($D^-$ inherited, never loaded; $D^+$ uniform and cancelled in every difference), and the reduction of this definition (one qubit line; the nucleus a parameter, not a second node). $J^\pm$ handle creation and dissolution and enter no stationary read; $D^+$ stretched the fabric and stretches it still, uniformly, for every class alike.

---

## Tier 5.11 — The Dynamics-of-Q Bridge: A-AT.1 Re-Priced, the Opened Classes, and the Continuum

### AT.23 — The masked orbit: the ladder derived from the force

**Thm.**
$$(1)\quad\textbf{the orbit:}\qquad\text{under A-AT.3's scope the masked EM force on the bound channel generates the phase orbit of the chart's canonical pair}\qquad[\mathrm{BM.10}(3);\ \mathrm{BM.8}(1)\text{'s promotion pattern at the channel's locus}]:$$
$$\text{a one-parameter read on the chart, }\neg\text{in the register}\qquad[\mathrm{BM.10}(1)\ \text{stands at its locus}];$$
$$(2)\quad\textbf{the spectrum:}\qquad\text{the orbit's stationary phases are the poles: the eigenvalue problem of }F_{\mathrm{EM}}\big|_{\text{mask}}\ \text{at }m_r\ \text{carries exactly the hydrogenic ladder}\qquad[\text{math: the Coulomb spectrum on the canonical pair, with the uniqueness row of the spherically symmetric problem at prescribed flux}]:$$
$$\boxed{\ E_n=-\frac{\varepsilon_{\mathrm{EM}}^{\,2}\,m_r}{2\,n^{2}}\qquad\text{derived from the force, } \neg\text{priced beside it}\ }\qquad[\mathrm{AT.6}(1);\ \text{machine: the coefficient identities}];$$
$$(3)\quad\textbf{the two routes:}\qquad\text{BM.48(2)'s priced rows and the masked orbit's spectrum are one spectrum, term by term}\qquad[\text{machine: the ladder rows}]:$$
$$\text{the conditionality that remained at the opening tiers was the grammar's; the grammar is declared [A-AT.1]; the conditionality that remains now is only the scope's [A-AT.3] — the same conditionality every chart-side row carries [BM.34's Rmk discipline]};$$
$$(4)\quad\textbf{the status:}\qquad\text{the ladder's shape stays coupling-free }[E_n/E_1=1/n^{2}]\ \text{and its scale symbolic [C-AT.1]};\qquad\neg\text{a measured spectral constant}\ [\mathrm{P5}].$$

**Req.** A6 (Part 1); CT2.1, CT2.6 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); BM.8(1), BM.10(1), BM.10(3), BM.34 Rmk, BM.48(2) (Part 4); A-AT.3, Def-AT.6, AT.5(1), AT.6(1), AT.6(4) (this part); the Coulomb spectrum and its uniqueness on the canonical pair [math; machine: `checks/verify_Atomic5.py` §J].

**Pf.**
$$
(1):\ \text{the promotion pattern instantiated at the bound channel under A-AT.3};\qquad\mathrm{BM.10}(1)\ \text{re-cited for the register's silence}
$$
$$
(2):\ \text{the Coulomb eigenproblem on the canonical pair at }m_r\ \text{[math; the uniqueness row BM.48's Req carried]};\qquad\text{the coefficient identity }e^{4}/16\pi^{2}=\varepsilon_{\mathrm{EM}}^{2}\ \text{and the ladder rows}\ [\text{machine}]
$$
$$
(3):\ \text{term-by-term agreement with AT.6}(1)\text{'s rows}\ [\text{machine}];\qquad(4):\ \text{the standing-rule record}.\ \blacksquare
$$

**Phys.** The opening tiers built the atom by declaring a grammar and then proving theorems about what the grammar declared. This tier goes one level deeper and asks what the force itself does on the declared channel — and the answer is the same ladder. The masked restriction of the one complete operator, evolving under the scope, has exactly one stationary spectrum, and it is the hydrogenic one; the rows Part 4 priced conditionally and the opening tiers adopted structurally are now the orbit's own stationary phases. Nothing new enters: no new operator, no new parameter, no new axiom — the dynamics-of-$Q$ route turns out to be a re-derivation of the corpus's own pricing from the corpus's own force. The declaration is not weakened by this; it is what gave the force a channel to act on.

### AT.24 — The price identity: A-AT.1's declared scar re-derived through the force

**Thm.**
$$(1)\quad\textbf{the declared price:}\qquad\Delta m_{\mathrm{EM}}=\frac{3\,c\,e^{2}\ln2}{2\pi\,\mathfrak h}>0\qquad[\mathrm{BM.46}(4);\ \mathrm{AT.3}(2)];$$
$$(2)\quad\textbf{the force routes:}\qquad\text{the scar's exterior field energy is the same monomial [BM.46(1)]; the sector census agrees [BM.52(5)]; and the width-locus row: the running profile vanishes at the member's own Born width and grows with scale [BM.18(2)] — so the declared price is the width-locus read of the masked force:}$$
$$\boxed{\ \Delta m_{\mathrm{EM}}\big|_{\text{census}}=\Delta m_{\mathrm{EM}}\big|_{\text{field integral}}=\Delta m_{\mathrm{EM}}\big|_{\text{width-locus orbit read}}\ }\qquad[\text{machine: the monomials identical — three routes, one monomial}];$$
$$(3)\quad\textbf{the discharge:}\qquad\text{BM.49's Rmk — ``an electromagnetic atom is a dynamics-of-}Q\text{ construction nobody has built'' — is discharged: built}$$
$$\text{the grammar declared [A-AT.1]; the force censused [AT.21]; the spectrum derived from the orbit [AT.23]; the price re-derived through the force [(2)]}:$$
$$\textbf{the declaration is backed, } \neg\text{revoked — the re-scope discipline [AT.20(2)'s pattern] applied to the era's own founding act};$$
$$(4)\quad\textbf{the status:}\qquad\neg\text{a new declaration};\qquad\neg\text{a value of }e\ \text{issued}\ [\mathrm{C\text{-}AT.1}];\qquad\text{the identity is monomial-exact at every admissible symbol value}.$$

**Req.** P1, P5 (Parts 1–2); FT.44(4) (Census); BM.18(2), BM.46(1), BM.46(4), BM.49 Rmk, BM.52(5), BM.55(1), BM.55(2) (Part 4); A-AT.1, AT.3(2), AT.6(1) (this part); AT.21, AT.23 (this part); exact Laurent monomial identities [math; machine: `checks/verify_Atomic5.py` §J].

**Pf.**
$$
(1):\ \mathrm{BM.46}(4)\text{'s monomial re-cited}
$$
$$
(2):\ \mathrm{BM.46}(1)\text{'s integral}=\mathrm{BM.52}(5)\text{'s census entry [the agreement row re-cited]};\qquad\mathrm{BM.18}(2)\text{'s vanishing-at-the-width profile re-cited}: \text{the orbit's width-locus expectation is the exterior monomial}\ [\text{machine: Laurent}]
$$
$$
(3):\ \text{the discharge census against BM.49's Rmk text}\ [\text{machine: the document pins}];\qquad(4):\ \text{the standing-rule record}.\ \blacksquare
$$

**Phys.** The proton's extra mass has been computed twice before — once as a field integral, once as a sector census — and the two agreed monomial for monomial. The masked orbit gives a third reading: at the member's own Born width, where the running profile dies, the orbit's self-read is the same Laurent monomial. Three routes, one answer, and the route that nobody had built — the dynamics of the charge on the bound channel — turns out to land exactly where the static declarations always said it would. The corpus's first atomic declaration now stands on three legs instead of one, and the Rmk that named the missing construction is discharged at its own locus: the construction exists, and it agrees.

### AT.25 — The opened classes: the $Z\ge2$ ladders and the continuum

**Thm.**
$$(1)\quad\textbf{the class ladders:}\qquad\text{the same mask at the counter's values: for the constructed classes } (A,Z)\ \text{with } Z\le A\ \text{[Def-AT.1's matter sector]:}$$
$$E_n^{(A,Z)}=-\frac{\varepsilon_{\mathrm{EM}}^{\,2}\,m_r^{(A,Z)}}{2\,n^{2}},\qquad m_r^{(A,Z)}=\frac{m_N\,m_\ell}{m_N+m_\ell},\qquad m_N=\frac{6A\ln2}{\mathfrak h}+Z\,\Delta m_{\mathrm{EM}}\qquad[\mathrm{AT.3}(2);\ \mathrm{AT.5}(3)\text{'s count-route row; A-AT.4's schema}]:$$
$$\text{the shape is universal: }E_n^{(A,Z)}/E_1^{(A,Z)}=1/n^{2}\ \text{at every class}\qquad[\text{machine: the }A\le4,\ Z\le A\text{ census}];$$
$$(2)\quad\textbf{the binding fractions tighten:}\qquad\frac{|E_1|^{(A)}}{m_N+m_\ell}=\frac{3A}{(3A+1)^{2}}\cdot\frac{\varepsilon_{\mathrm{EM}}^{2}}{2}\ \ \text{on the count route}\qquad[\text{machine};\ \mathrm{AT.22}(4)]:\qquad\textbf{the class ladder of binding fractions tightens along the exact }(3A+1)^{2}\text{ form};$$
$$(3)\quad\textbf{the continuum:}\qquad\text{the ionized sector's content above the edge is the unbounded ladder with its spectral bound}\qquad[\mathrm{BM.24}\text{'s derivation of CT2.6(ii)--(iii): the unbounded ladder and the }\sqrt3\text{ bound}]:$$
$$\text{the continuum exists as the ladder's completion; the registry boundary between the sectors is the flux-read structure [AT.9(2)], } \neg\text{a distance};$$
$$(4)\quad\textbf{the naming:}\qquad\text{the classes are named by A-AT.4's schema — labels on derived tuples, no datum};\qquad\neg\text{a measured class ladder,}\ \neg\text{a comparison}\ [\mathrm{P5}];$$
$$(5)\quad\textbf{the status:}\qquad\text{constructed by the one mask of AT.21 at the counter's values; } \neg\text{a new grammar, } \neg\text{a new declaration beyond A-AT.4}.$$

**Req.** P1, P5 (Parts 1–2); CT2.6 (Part 2); FT.44(4) (Census); Def-BM.8, BM.24, BM.46 (Part 4); Def-AT.1, A-AT.2, AT.3(2), AT.5(3), AT.9(2), AT.12(3) (this part); AT.21, AT.23 (this part); exact rational identities on the class grid [math; machine: `checks/verify_Atomic5.py` §J].

**Pf.**
$$
(1):\ \text{the reduced mass at the class term [AT.5(3)'s algebra with AT.3(2)'s }m_N];\qquad\text{the shape row }1/n^{2}\ \text{at }A\le4,\ Z\le A\ [\text{machine}]
$$
$$
(2):\ m_r^{(A)}/(m_N+m_\ell)=3A/(3A+1)^{2}\ \text{on the count route [AT.22(4)'s row]};\qquad|E_1|=\varepsilon^{2}m_r/2\implies\text{the fraction}\ [\text{machine}]
$$
$$
(3):\ \mathrm{BM.24}\text{'s unbounded-ladder derivation re-cited};\qquad\mathrm{AT.9}(2)\text{'s registry rows re-cited};\qquad(4),(5):\ \text{the naming and status records}.\ \blacksquare
$$

**Phys.** One mask, applied at every value of the charge counter, is the whole spectroscopic zoo below the continuum: the ladder shape never changes — one over $n$ squared at every class — while the scale tightens with the reduced mass and the binding fractions walk the exact ladder one over three-$A$-plus-one. Above the edge, the corpus's continuum-limit tier already derived what the ionized sector is: the unbounded ladder with its spectral bound, the completion the bound poles accumulate toward. Nothing here is a new construction; it is one construction finally read at all of the counter's values, with names issued as labels and nothing more. The atomic era's "one ladder" was the first row of a family whose remaining rows were waiting for exactly this re-derivation.

---

## Tier 5.12 — The Per-Rung Metric Split: the Rest Slice Locked, the Kinetic Share, and the Fuzziness Product

### AT.26 — The split at level $n$: rest locked, kinetic on the ladder

**Thm.**
$$(1)\quad\textbf{the system read at every pole:}\qquad\mathfrak M_n\ =\ M(A,Z)+m_\ell+E_n\qquad[\mathrm{AT.6}(2)\text{'s system read instantiated at the pole }n;\ \text{machine}];$$
$$(2)\quad\textbf{the metric split (chart-side, vacuum gauge [BM.34(4)'s gauges]):}\qquad\textbf{the rest slice: the members' locked ledger }M(A,Z)+m_\ell\qquad[\mathrm{BM.34}(7)\text{'s rest read; BM.35's reframing}]:$$
$$\textbf{the kinetic share: the virial split at every rung}\qquad\langle\mathrm{KE}\rangle_n=|E_n|,\qquad\langle V\rangle_n=2E_n,\qquad\langle\mathrm{KE}\rangle_n+\langle V\rangle_n=E_n\qquad[\mathrm{AT.8}(4)\text{'s virial identity at every }n;\ \text{machine: the }n\text{-grid}];$$
$$(3)\quad\textbf{the locally-locked row:}\qquad\text{the rest slice rides the Born-width hyperbola and does not move along the ladder}\qquad[\mathrm{BM.16}(1),(4)];$$
$$\text{the kinetic share walks the ladder's shape: }|E_n|/|E_1|=1/n^{2}\qquad[\text{machine}]:\qquad\textbf{the split's shape is the ladder's shape; the split's floor is the lock};$$
$$(4)\quad\textbf{the status:}\qquad\text{chart-side under the scope; } \neg\text{a measured split, } \neg\text{a comparison}\ [\mathrm{P5}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); BM.16(1), BM.16(4), BM.34(4), BM.34(7), BM.35, BM.48(2) (Part 4); A-AT.3, AT.5(1), AT.6(2), AT.8(4) (this part); AT.23 (this part); the virial identity on the canonical pair, exact rational grids [math; machine: `checks/verify_Atomic5.py` §J].

**Pf.**
$$
(1):\ \text{AT.6(2)'s form at the pole index }n\ [\text{machine}]
$$
$$
(2):\ \text{the rest slice at }p=0\ \text{[BM.34(7)]};\qquad\text{the virial identities at }n=1..8\ \text{as exact rational rows in }\kappa:=\varepsilon_{\mathrm{EM}}^{2}m_r\ [\text{machine}]
$$
$$
(3):\ \mathrm{BM.16}\text{'s lock rows re-cited};\qquad|E_n|/|E_1|=1/n^{2}\ [\text{machine}];\qquad(4):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The user of the corpus asked for the total energy first and the rest-versus-kinetic split second, and the corpus's answer is that both were already in its books — the metric's dispersion read supplies the split for any composite, and the Coulomb virial supplies the shares at every rung. What the era adds is the discipline of the two loci: the rest slice is lock-level, riding the width–curvature hyperbola, identical at every rung of the ladder; the kinetic share is rung-level, walking the exact one-over-$n$-squared shape. "Locally locked" is not a metaphor here — the rest read is pinned by the calibration hyperbola and the kinetic read is the only thing that moves, which is why the ladder's spectroscopy never disturbs the masses underneath it.

### AT.27 — The fuzziness product: the exact information row

**Thm.**
$$(1)\quad\textbf{the moments (chart-side, canonical-pair scope):}\qquad\langle x\rangle=\langle p\rangle=0\ \ \text{[math: parity]};\qquad(\Delta p)^{2}=\langle p^{2}\rangle=2\,m_r\,|E_n|\qquad[\text{math: the virial share }\langle\mathrm{KE}\rangle=\langle p^{2}\rangle/2m_r;\ \text{machine}]:$$
$$\langle r^{2}\rangle_{nS}=a^{2}\,n^{2}\,\frac{5n^{2}+1}{2},\qquad a:=\frac{1}{\varepsilon_{\mathrm{EM}}\,m_r}\qquad[\mathrm{AT.8}(3)\text{'s length; math: the hydrogenic moment}];\qquad(\Delta x)^{2}=\langle r^{2}\rangle/3\ \ \text{[math: isotropy]};$$
$$(2)\quad\textbf{the product:}$$
$$\boxed{\ \bigl(\Delta x_n\,\Delta p_n\bigr)^{2}\ =\ \frac{5n^{2}+1}{6}\ }\qquad[\text{machine: the exact census }n\le7]:\qquad\ge1\ \text{with equality only at }n=1;\qquad\text{strictly increasing in }n;$$
$$\textbf{the Robertson floor is exceeded by the exact factor 2 at the ground pole}\qquad[\mathrm{BM.10}(3)\text{'s floor }\tfrac12;\ \text{machine: }1=2\cdot\tfrac12];$$
$$(3)\quad\textbf{the shell row:}\qquad\langle r^{2}\rangle_{n\ell}=a^{2}n^{2}\,\frac{5n^{2}+1-3\ell(\ell+1)}{2}\qquad[\text{math}]:\qquad\text{the }s\text{-state minimizes the product on each shell; positivity on the whole shell}\qquad[\text{machine: }5n^{2}+1-3\ell(\ell+1)>0,\ 0\le\ell\le n-1,\ n\le6];$$
$$(4)\quad\textbf{the velocity row:}\qquad\Delta v=\Delta p/m_r\qquad[\text{the chart's kinematics; D2.9}]:\qquad\Delta x\,\Delta v=\frac{1}{m_r}\sqrt{\frac{5n^{2}+1}{6}}\qquad[\text{machine: the exact radical form}]:$$
$$\textbf{the position--velocity fuzziness is determined exactly on the ladder — never saturating, never below the floor};$$
$$(5)\quad\textbf{the status:}\qquad\text{the fuzziness is a theorem about the bound channel's states — a spread, never a value [the bracket discipline]};\qquad\neg\text{a measured }\Delta x\,\Delta p\ [\mathrm{P5}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); BM.10(3), BM.48(2) (Part 4); AT.5(1), AT.8(3), AT.8(4) (this part); AT.26 (this part); the hydrogenic moment identities and the Robertson bound on the canonical pair [math; machine: `checks/verify_Atomic5.py` §K].

**Pf.**
$$
(1):\ \langle p^{2}\rangle=2m_r|E_n|\ \text{from the virial share};\qquad\langle r^{2}\rangle_{nS}\ \text{and the isotropy row [math]};\qquad\text{the product cleared: }\Delta x^{2}\Delta p^{2}=\frac{a^{2}n^{2}(5n^{2}+1)}{6}\cdot\frac{\varepsilon^{2}m_r^{2}}{n^{2}}=\frac{5n^{2}+1}{6}\ \ [\text{machine: }a=1/(\varepsilon m_r)]
$$
$$
(2):\ \text{the squared census as exact Fractions at }n=1..7:\ 1,\ \tfrac72,\ \tfrac{23}{3},\ \tfrac{27}{2},\ 21,\ \tfrac{181}{6},\ 41\ [\text{machine}];\qquad\text{monotonicity and the }n=1\text{ equality}\ [\text{machine}]
$$
$$
(3):\ \text{the }\ell\text{-census at }n\le6\ [\text{machine}];\qquad(4):\ \text{the velocity form [D2.9's chart kinematics]};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** This is the row the era was asked for: the fuzziness between the information that locates the lepton and the information that moves it, determined exactly rather than bounded loosely. On the Coulomb channel the product never reaches the Robertson floor — the ground pole sits at exactly twice it, one, and every higher rung sits higher still, as the square of one over six times five-$n$-squared-plus-one, an exact radical per shell with the $s$-state the quietest member. The form is worth pausing on: the position spread carries the ladder's length scale, the momentum spread carries the ladder's energy scale, and the two conspire to leave a product that knows the rung but not the coupling — the shape of the uncertainty on the atomic ladder is as coupling-free as the ladder's own spectrum. What the quantum of the chart bounds from below, the corpus's own states sit above by exact rational factors; nothing here is a value, and every row is an inequality with an exact square.

### AT.28 — The envelope row: the two widths and their exact ratio

**Thm.**
$$(1)\quad\textbf{the two widths:}\qquad\text{the constituent's Born width }\Delta x_{\mathrm B}^{(\ell)}=\frac{\mathfrak h}{2\ln2}\qquad[\mathrm{Def\text{-}BM.4}(1);\ \mathrm{AT.4}(1)\text{'s }E_{\mathrm{int}}=2];\qquad\text{the orbital envelope }a=\frac{1}{\varepsilon_{\mathrm{EM}}\,m_r}\qquad[\mathrm{AT.8}(3)];$$
$$(2)\quad\textbf{the ratio:}\qquad\boxed{\ \frac{a}{\Delta x_{\mathrm B}^{(\ell)}}=\frac{4+3\,c\,\varepsilon_{\mathrm{EM}}}{3\,\varepsilon_{\mathrm{EM}}\,(1+c\,\varepsilon_{\mathrm{EM}})}\ }\qquad[\text{machine: the exact monomial-rational}]:$$
$$\text{exact and symbolic in the coupling — the orbital envelope and the constituent width are separated by the inverse coupling at the floor reads};$$
$$(3)\quad\textbf{the consistency:}\qquad\text{the zero-point bound applies at the constituent's width [BM.34(6)]; the orbital read applies at the envelope [AT.27]; the two loci are distinct and their ratio is the monomial above — no double occupation of one locus}\qquad[\mathrm{Def\text{-}BM.4}(5)\text{'s envelope discipline}];$$
$$(4)\quad\textbf{the status:}\qquad\neg\text{a measured radius; the row is an identity, } \neg\text{an inequality claimed beyond it [the coupling's value is } \neg\text{issued, C-AT.1]}.$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); Def-BM.4(1), Def-BM.4(5), BM.34(6) (Part 4); AT.4(1), AT.5(1), AT.8(3) (this part); exact monomial identities [math; machine: `checks/verify_Atomic5.py` §K].

**Pf.**
$$
(1):\ \text{the two width rows re-cited}
$$
$$
(2):\ \frac{a}{\Delta x_{\mathrm B}}=\frac{2\ln2}{\mathfrak h\,\varepsilon_{\mathrm{EM}}\,m_r}=\frac{2\ln2}{\mathfrak h\,\varepsilon_{\mathrm{EM}}}\cdot\frac{\mathfrak h\,(4+3c\varepsilon)}{6\ln2\,(1+c\varepsilon)}=\frac{4+3c\varepsilon}{3\,\varepsilon_{\mathrm{EM}}(1+c\varepsilon)}\ [\text{machine}]
$$
$$
(3):\ \text{the envelope discipline re-cited};\qquad(4):\ \text{the status record}.\ \blacksquare
$$

**Phys.** Two lengths live on the bound channel and the corpus keeps them apart on purpose. The constituent's Born width is the Compton-like envelope of the lepton's own density read — hops over two $\ln2$, fixed at the floor, insensitive to everything the atom does. The orbital envelope is the ladder's length, inverse-coupling large, the thing that makes the atom many hops across. Their ratio is an exact monomial in the coupling, and the discipline that separates them is Def-BM.4's own: the zero-point bound is booked at the constituent's locus, the orbital moments at the envelope's locus, and no row of this part reads one as the other. The atom is big because its envelope is inverse-coupling, not because its lepton swelled; the lepton's width never moved.

---

## Tier 5.13 — The Scope-Local $(t,E)$ Bridge and the Width Ledger: AT.15's Waiting Half, Bracketed

### AT.29 — The scope clock: what exists, what stays barred, and what the bridge is

**Thm.**
$$(1)\quad\textbf{the no-gos stand at their loci:}\qquad\neg\exists\ \text{a self-adjoint time operator at finite dimension}\qquad[\mathrm{BM.10}(4);\ \text{the trace obstruction}];\qquad\text{the tick has no inverse and the dynamics contracts}\qquad[\mathrm{A6};\ \mathrm{L2};\ \mathrm{BM.51}(2),(3)]:$$
$$\text{the re-scope discipline: these rows locate domains — the finite register, the irreversible tick — and assert nothing beyond them [BM.10's Rmk]};$$
$$(2)\quad\textbf{the scope:}\qquad\text{under A-AT.3 the bound channel's read carries BM.8(2)'s theorem-local stationarity scope}\qquad[\mathrm{Def\text{-}BM.10}(5)\text{'s inheritance pattern; BM.53(6)}]:\qquad\text{the energy charge exists within the scope};$$
$$(3)\quad\textbf{the bridge:}\qquad\text{the masked orbit's phase parameter [AT.23(1)] is the Mandelstam--Tamm form's }\Delta t:\qquad\boxed{\ \Delta t\,\Delta E\ \ge\ \tfrac12\ }\qquad[\mathrm{BM.10}(4);\ \mathrm{BM.53}(4)]:$$
$$\text{the two-level saturation witness is exact over }\mathbb Q(i)\qquad[\mathrm{BM.53}(4);\ \text{machine re-run}]:\qquad\textbf{the bridge is a pairing — the orbit supplies the parameter, the scope the stationarity, the MT form the duality};$$
$$(4)\quad\textbf{what is and is not constructed:}\qquad\text{constructed: a scope-local clock read, with its duality bounds; } \neg\text{constructed: a time operator [BM.10(4) stands], an emergent time [FT.131(3)'s prerequisite stands], a second-denomination rate [P5]};$$
$$(5)\quad\textbf{the status:}\qquad\text{the bridge is a read-side object under the scope's conditionality, like every chart row before it}.$$

**Req.** A6 (Part 1); D1.8, D2.9 (Parts 1–2); CT2.6 (Part 2); P1, P5 (Parts 1–2); L2 (Part 1); FT.131(3) (Part 3); BM.8(2), BM.10(1), BM.10(4), BM.10 Rmk, BM.34(5), BM.51(2), BM.51(3), BM.53(4), BM.53(6) (Part 4); A-AT.3, AT.23 (this part); exact $\mathbb Q(i)$ witness algebra [math; machine: `checks/verify_Atomic5.py` §L].

**Pf.**
$$
(1):\ \mathrm{BM.10}(4)\text{'s trace obstruction and A6/L2's irreversibility re-cited at their loci};\qquad\text{the Rmk's domain-locator reading applied}
$$
$$
(2):\ \text{A-AT.3's scope row applied to Def-AT.6's channel};\qquad\mathrm{BM.53}(6)\text{'s inheritance pattern re-cited}
$$
$$
(3):\ \mathrm{BM.53}(4)\text{'s MT row and its exact witness re-cited and re-run}\ [\text{machine: }(\Delta A)^{2}=(\Delta E)^{2}=\tfrac14,\ \Delta t=1,\ \Delta t\,\Delta E=\tfrac12];\qquad(4),(5):\ \text{the construction and status records}.\ \blacksquare
$$

**Phys.** The corpus has been honest about time since the Noether tier: the tick runs forward, the dynamics contracts, and no self-adjoint time operator exists at any finite dimension — and it has been equally honest that these are domain statements. Inside the stationarity scope, on the chart, the energy charge exists and the Mandelstam–Tamm bound is its admissible dual, saturated by a two-level witness the corpus can write down over the Gaussian rationals. What this tier adds is the pairing: the masked orbit of Tier 5.11 supplies the phase parameter, the scope supplies the stationarity that makes the parameter a clock read, and the duality is the bridge. No time operator is constructed; none was available. No emergent time is declared; its prerequisite stands exactly where Part 4 named it. What exists is narrower and exactly what the width ledger needs.

### AT.30 — The width ledger: the two-sided bracket on every level

**Thm.**
$$(1)\quad\textbf{the floor:}\qquad\text{any level-}n\text{ scope read with energy spread }\Delta E_n\text{ and characteristic tick count }\tau_n\text{ satisfies}\qquad\Delta E_n\cdot\tau_n\ \ge\ \tfrac12\qquad[\mathrm{MT},\ \mathrm{AT.29}(3);\ \mathrm{D1.8}\text{: the chart time is the tick count}];$$
$$(2)\quad\textbf{the tick floor:}\qquad\tau\ge3\ \text{ticks for any decay-style transition}\qquad[\mathrm{BM.53}(3);\ \mathrm{BM.44}(2);\ \mathrm{BM.21}\text{'s lifetime floor}]:\qquad\text{the universal width floor sits at } \tfrac16\ \text{in the chart's energy currency}\qquad[\text{machine: }1/(2\cdot3)];$$
$$(3)\quad\textbf{the registry ceiling:}\qquad\text{the pole's spread cannot cross the continuum edge without dissolving the registry distinction [AT.9(2)]:}\qquad\boxed{\ 1/(2\tau_n)\ \le\ \Delta E_n\ \le\ |E_n|\ }\qquad[\text{machine: the ladder rows}]:$$
$$\textbf{the width is bracketed — two-sided, exact, tick-denominated; the bracket is nonempty iff }\tau_n\ \ge\ n^{2}/\kappa\ \text{with }\kappa:=\varepsilon_{\mathrm{EM}}^{2}m_r\qquad[\text{machine: the threshold census at witness }\kappa];$$
$$(4)\quad\textbf{the no-flicker consistency:}\qquad\varepsilon_q=0\implies\text{the transition content vanishes identically}\qquad[\mathrm{AT.15}(3);\ \mathrm{BM.23}(8)]:\qquad\text{the bracket survives as the resolvability structure — the floor is all that remains};$$
$$(5)\quad\textbf{the status:}\qquad\text{brackets are inequalities, never values [the bracket discipline]};\qquad\neg\text{a measured linewidth, } \neg\text{a lifetime in seconds}\ [\mathrm{P5};\ \mathrm{BM.53}(3)].$$

**Req.** D0.4, D1.8 (Parts 1–2); CT2.6 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); BM.21, BM.23(8), BM.44(2), BM.53(3) (Part 4); AT.9(2), AT.15(3), AT.6(1) (this part); A-AT.3, AT.26, AT.29 (this part); exact rational threshold censuses [math; machine: `checks/verify_Atomic5.py` §L].

**Pf.**
$$
(1):\ \text{the MT form at the level read};\qquad(2):\ \tau\ge3\implies1/(2\tau)\le\tfrac16\ [\text{machine}]
$$
$$
(3):\ |E_n|=\kappa/(2n^{2})\ \text{monotone decreasing in }n;\qquad\text{the registry row [AT.9(2)] re-cited}: \text{the spread books inside the bound sector};\qquad\text{nonemptiness: }1/(2\tau_n)\le\kappa/(2n^{2})\iff\tau_n\ge n^{2}/\kappa\ [\text{machine}]
$$
$$
(4):\ \mathrm{AT.15}(3)\text{'s no-flicker theorem re-cited};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** A level's width is not a number in this corpus and never will be — it is a bracket, and the bracket has a floor and a ceiling, both exact. The floor is the Mandelstam–Tamm duality at the scope clock: a level that is to be probed on $\tau_n$ ticks cannot carry an energy spread narrower than one over twice that. The tick's own irreversibility sets the universal floor at one over six, because no decay-style transition completes in fewer than three ticks. The ceiling is the registry: a pole's fuzziness that reached past the continuum edge would book ionized content inside a bound read, and the flux structure that makes the atom one object forbids the bookkeeping. Between them the width lives as an interval whose endpoints are exact rational forms in the coupling and the tick count — and at the sharp threshold where the flicker dies, the interval's content dies with it, leaving only the resolvability structure. The corpus brackets what it cannot yet value, and the bracket is honest.

### AT.31 — The resolvability of the ladder: the spectroscopic depth as a coupling step-function

**Thm.**
$$(1)\quad\textbf{the spacing rows:}\qquad\Delta_n:=E_n-E_{n+1}=\frac{\varepsilon_{\mathrm{EM}}^{2}\,m_r\,(2n+1)}{2\,n^{2}(n+1)^{2}}\qquad[\text{machine: }n\le8];\qquad\frac{\Delta E_{3\to2}}{\Delta E_{2\to1}}=\frac{5}{27}\qquad[\mathrm{AT.8}(2)\ \text{re-run}];$$
$$(2)\quad\textbf{the clock bound:}\qquad\text{resolving levels }n\text{ and }n+1\text{ requires a scope clock finer than }1/(2\Delta_n)\ \text{ticks}\qquad[\mathrm{MT};\ \mathrm{BM.53}(5)\text{'s pattern}];$$
$$(3)\quad\textbf{the depth row:}\qquad\text{a 3-tick clock resolves the }(n,n+1)\text{ pair iff }\kappa\ \ge\ \frac{2\,n^{2}(n+1)^{2}}{3\,(2n+1)}\qquad[\text{machine: the exact threshold table }n\le6]:$$
$$\frac{8}{9},\quad\frac{24}{5},\quad\frac{96}{7},\quad\frac{800}{27},\quad\frac{600}{11},\quad\frac{1176}{13}\qquad(n=1,\dots,6):\qquad\boxed{\ \textbf{the spectroscopic depth is a step function of the coupling with exact rational thresholds}\ };$$
$$(4)\quad\textbf{the level row:}\qquad\text{a 3-tick clock resolves level }n\text{'s own width iff }\kappa\ \ge\ \frac{n^{2}}{3}\qquad[\text{machine: from AT.30(3)'s ceiling at the floor}];$$
$$(5)\quad\textbf{the regularity:}\qquad\text{the threshold ratios inherit the transition rationals' structure}\qquad[\text{machine: the ratio rows}]:\qquad\text{the spectroscopic regularity the era reads, in ticks, } \neg\text{seconds}\qquad[\mathrm{BM.53}(3);\ \mathrm{P5}];$$
$$(6)\quad\textbf{the disposition (AT.15's waiting half):}\qquad\text{the width/resolution structure is }\textbf{formed};\qquad\text{the absolute transition weight stays under the named prerequisite}\qquad[\mathrm{FT.131}(3);\ \mathrm{BM.131}(7)]:$$
$$\mathrm{(P5.3)}\ \text{re-scoped at its own locus: from ``open'' to ``\textbf{open with formed brackets}'' — the split discipline [AT.20(1)'s (P5.3) row] carried forward};$$
$$(7)\quad\textbf{the status:}\qquad\neg\text{a measured resolution; the thresholds are conditional rows in }\kappa\text{, exact at every admissible symbol value}.$$

**Req.** D1.8 (Parts 1–2); CT2.6 (Part 2); P1, P5 (Parts 1–2); FT.131(3), FT.144(2) (Part 3); BM.44(2), BM.53(3), BM.53(5), BM.131(7) (Part 4); AT.8(2), AT.15(3), AT.20(1) (this part); AT.29, AT.30 (this part); exact rational spacing and threshold tables [math; machine: `checks/verify_Atomic5.py` §L].

**Pf.**
$$
(1):\ \Delta_n=\kappa\bigl(\tfrac{1}{2n^{2}}-\tfrac{1}{2(n+1)^{2}}\bigr)=\kappa\,\tfrac{2n+1}{2n^{2}(n+1)^{2}}\ [\text{machine}];\qquad\tfrac{5/36}{3/4}=\tfrac{5}{27}\ [\text{machine}]
$$
$$
(2):\ \text{the MT form inverted at the spacing read [BM.53(5)'s pattern]};\qquad(3):\ \Delta_n\ge\tfrac16\iff\kappa\ge\tfrac{2n^{2}(n+1)^{2}}{3(2n+1)};\ \text{the table as exact Fractions}\ [\text{machine}]
$$
$$
(4):\ \kappa/(2n^{2})\ge\tfrac16\iff\kappa\ge n^{2}/6\ [\text{machine}];\qquad(5):\ \text{the ratio rows}\ [\text{machine}]
$$
$$
(6):\ \text{the disposition census against AT.15(4)'s open-clause text}\ [\text{machine: the document pins}];\qquad(7):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The atomic era left its rates open under a named prerequisite, and the honest question for this extension was what could be formed without paying that prerequisite. The answer is a spectroscopy of brackets. Adjacent levels are separated by exact rational spacings; the Mandelstam–Tamm duality converts each spacing into a clock requirement; and the tick's three-count floor converts the clock requirement into a coupling threshold — a step function with six exact rational treads in the table, each tread the exact answer to "how strong must the coupling be before a three-tick clock can tell these two levels apart". Below the tread, the levels are one unresolved line; above it, the ladder's depth opens rung by rung as the coupling strengthens. The absolute rates wait still — the corpus does not fake the emergent-time construction — but "how fine a clock does the spectrum need" is now a derived, tabulated, exact structure, and the demand row that waited is re-scoped, not forgotten: open with formed brackets.

---

## Tier 5.14 — The Unified Mass Observable: the Pole and the Bracket, and the Incommensurability Re-Adjudication

### Def-AT.7 — The unified mass read: pole + bracket on the constructed bound

**Def.** For the constructed bound channel [Def-AT.6] at level $n$ of class $(A,Z)$:
$$(1)\quad\textbf{the read:}\qquad\textbf{the unified mass read is the pair}\ \bigl(\text{pole},\ \text{bracket}\bigr):$$
$$\textbf{the pole:}\qquad\mathfrak M_n(A,Z)\ :=\ \text{the pole of the bound channel's resolvent}\qquad[\mathrm{BM.23}(4)\text{'s pole reads; Def-BM.20}(2);\ \mathrm{AT.6}(5)]:$$
$$\mathfrak M_n(A,Z)\ =\ M(A,Z)+m_\ell+E_n^{(A,Z)}\qquad\text{exactly}\qquad[\text{machine: the identity at declared witnesses}];$$
$$(2)\quad\textbf{the value component:}\qquad\text{exact monomial-rational in }(e,\mathfrak h,\ln2,c)\ \text{over the integer counters }(A,Z,n)\qquad[\mathrm{AT.3}(2);\ \mathrm{AT.6}(1)];$$
$$(3)\quad\textbf{the spread component:}\qquad\text{the tick interval}\qquad\bigl[\,1/(2\tau_n),\ |E_n^{(A,Z)}|\,\bigr]\qquad[\mathrm{AT.30}(3)\text{'s bracket}]:\qquad\text{inequalities, never values [the bracket discipline]};$$
$$(4)\quad\textbf{the category row:}\qquad\text{the amplitude layer supplies the bracket's existence and endpoints, never a summand of the pole}\qquad[\mathrm{FT.79}(5)\ \text{at the free members; the bracket discipline}];$$
$$(5)\quad\textbf{the scope:}\qquad\text{constructed bounds only; the free members' reads are untouched}\qquad[\mathrm{BM.48}(4)\text{--}(5)\text{ honored}].$$

### AT.32 — The bridge row: what "bridging the amplitude→mass gap" means here

**Thm.**
$$(1)\quad\textbf{the no-go's locus:}\qquad\text{``no bridge carries an amplitude into a mass'' bound the free members' reads}\qquad[\text{Tier BM.10's verdict context; FT.67(3a); FT.68(4); BM.37(3)}]:\qquad\text{there it stands, re-scoped } \neg\text{revoked};$$
$$(2)\quad\textbf{the bound locus:}\qquad\text{the mass read is two-component [Def-AT.7]; the width is the spread \emph{of the mass read} under the scope's fuzziness [AT.27; AT.30]}:$$
$$\text{no amplitude becomes a mass value; the amplitude layer's fuzziness becomes the read's second component — an interval with exact endpoints};$$
$$(3)\quad\textbf{the verdict:}\qquad\boxed{\ \text{the bridge is built in exactly the sense the discipline admits: pole + bracket}\ }\qquad[\text{machine: the bracket endpoints exact at the witnesses}];$$
$$(4)\quad\textbf{the status:}\qquad\text{the era-locality discipline's first full payment: an obstruction bridged by constructing the domain it left open, at the object it named}.$$

**Req.** P1, P5 (Parts 1–2); FT.44(4) (Census); FT.67(3a), FT.68(4), FT.79(5) (Part 3); BM.10 Rmk, BM.23(4), BM.37(3), BM.48(4), BM.48(5) (Part 4); Def-BM.20 (Part 4); A-AT.3, Def-AT.4, AT.6(2), AT.6(5), AT.9(2) (this part); Def-AT.6, AT.27, AT.30 (this part); exact witness identities [math; machine: `checks/verify_Atomic5.py` §M].

**Pf.**
$$
(1):\ \text{the locus record against FT.67(3a)/FT.68(4)'s free-member rows};\qquad\mathrm{BM.10}\text{'s Rmk applied}
$$
$$
(2):\ \text{the two-component read [Def-AT.7] with the bracket endpoints from AT.30(3) — exact Fractions at the declared witnesses}\ [\text{machine}]
$$
$$
(3),(4):\ \text{the verdict and status records}.\ \blacksquare
$$

**Phys.** The corpus refused, correctly, to let the flicker's amplitudes masquerade as masses — that bar protected the free-member reads through two eras, and it still stands there. What the constructed bound changes is the shape of the question: at the atom, the mass observable is not a scalar but a pair — where the pole sits, and how widely the scope's own fuzziness spreads it. The first component is amplitude-free by construction: it is the resolvent's pole condition, the same exact monomial the ladder always carried. The second component is amplitude-shaped but never amplitude-valued: the Born fuzziness and the tick floor fix an interval, and an interval is a claim about spreads, not a claim about mass. The bridge the corpus named as missing is built by refusing to build the forbidden version of it.

### AT.33 — The incommensurability re-adjudication: no fractional values at the unified read

**Thm.**
$$(1)\quad\textbf{the value ledger's inventory:}\qquad\text{the counters }(A,Z,n,\text{shell counts})\in\mathbb Z\qquad[\mathrm{Def\text{-}BM.8};\ \mathrm{AT.2};\ \mathrm{AT.11}];$$
$$\text{the masses, poles, thresholds and spacings are exact monomial-rationals in }(e,\mathfrak h,\ln2,c)\qquad[\mathrm{AT.3}(2);\ \mathrm{AT.6}(1);\ \mathrm{AT.9}(1);\ \mathrm{AT.31}(1);\ \text{machine: the witness identities}]:$$
$$\boxed{\ \neg\exists\ \text{a third kind in the value ledger}\ }\qquad[\text{machine: the token census of this part}];$$
$$(2)\quad\textbf{the addresses:}\qquad\text{the running profile vanishes at the member's own Born width and grows with scale [BM.18(2)]: every fractional appearance is a scale read above the width locus —}$$
$$\text{at the bound's own width the read returns the integer counter and the exact pole; the fractions live in the running, ensemble and ratio reads, never in the value ledger};$$
$$(3)\quad\textbf{the proved incommensurabilities re-addressed:}\qquad\text{BM.17's inter-family ratios (the cubic form's three roots) and the neutron--proton critical locus are incommensurabilities \emph{between formed ratio reads across currencies}}\qquad[\mathrm{BM.17};\ \mathrm{BM.18}\text{'s ensemble-robustness}]:$$
$$\text{the unified read does not rationalize them — it re-addresses them: they localize at the poles and critical loci of the reads, and the fractional appearances around them demote to widths — spreads, never values};$$
$$(4)\quad\textbf{the verdict:}\qquad\boxed{\ \neg\exists\ \text{a fractional mass value at the unified read: the values are integers and exact monomials; the fractions are addresses (scales, widths, ratios of reads)}\ };$$
$$(5)\quad\textbf{the status:}\qquad\neg\text{a comparison to any measured value}\ [\mathrm{P5}];\qquad\text{the adjudication is about the ledger's own grammar, } \neg\text{about the world's numbers}.$$

**Req.** P1, P5 (Parts 1–2); FT.44(4) (Census); Def-BM.8 (Part 4); BM.17, BM.18(2), BM.28(7), BM.135(4) (Part 4); AT.2, AT.3(2), AT.6(1), AT.9(1), AT.11 (this part); AT.30, AT.31, AT.32 (this part); exact witness identities and the token census [math; machine: `checks/verify_Atomic5.py` §M].

**Pf.**
$$
(1):\ \text{the inventory census: every value row of Tiers 5.10–5.14 is an integer counter or a monomial-rational}\ [\text{machine: the witness identities at the class grid}]
$$
$$
(2):\ \mathrm{BM.18}(2)\text{'s vanishing-at-the-width row re-cited at the bound channel};\qquad(3):\ \mathrm{BM.17}/\mathrm{BM.18}\text{'s incommensurability and robustness rows re-cited at their loci}
$$
$$
(4),(5):\ \text{the verdict and status records}.\ \blacksquare
$$

**Phys.** The corpus proved its incommensurabilities honestly: the inter-family mass ratios are roots of a cubic, the neutron–proton critical locus is irrational, and no ensemble reading smooths either away. What this era adds is the address theory. The value ledger has two rooms — the integer counters and the exact monomial-rationals — and nothing else has ever been admitted to either; the fractional appearances that motivated the question live in a third place that was never a room at all: the scale-dependent reads, which vanish at each member's own Born width and grow only as the read moves above it. Ask for a mass at the unified read and the answer is an integer or a monomial; ask where the fractions went and the answer is that they were never values — they were addresses: scales, widths, ratios of reads taken at levels the unified read does not occupy. The incommensurability of the ratios survives untouched, as the robustness rows said it would; what dissolves is the thought that it ever lived in the masses.

### AT.34 — The decomposition row: the unified pole and the free sum

**Thm.**
$$(1)\quad\textbf{the gap:}\qquad\bigl(M(A,Z)+m_\ell\bigr)-\mathfrak M_n(A,Z)\ =\ |E_n^{(A,Z)}|\ >\ 0\qquad[\text{machine: the sign census at the witnesses}]:$$
$$\textbf{the decomposition-level sum of the free members exceeds the unified pole by exactly the binding share};$$
$$(2)\quad\textbf{the bar honored both ways:}\qquad\text{the free members carry no binding [BM.48(4)--(5)]; the bound carries the only negative read [AT.6(2)]};$$
$$(3)\quad\textbf{the four-slot row:}\qquad\text{the no-go [BM.136(3)] stands at its colour locus, untouched; the atom bridges nothing there — the channel change [AT.21's census] is why no bridge was needed};$$
$$(4)\quad\textbf{the status:}\qquad\text{the era's diagnosis row: the fractional and decomposition-level reads were the artifact; the unified pole is the object}.$$

**Req.** P1, P5 (Parts 1–2); FT.44(4) (Census); BM.48(4), BM.48(5), BM.136(3) (Part 4); AT.6(2) (this part); AT.21, Def-AT.7 (this part); exact sign censuses [math; machine: `checks/verify_Atomic5.py` §M].

**Pf.**
$$
(1):\ \mathfrak M_n=M+m_\ell+E_n\ \text{with }E_n<0\ \text{at positive symbols}\ [\text{machine}]
$$
$$
(2):\ \text{the bar rows re-cited};\qquad(3):\ \mathrm{BM.136}(3)\text{'s zero re-cited at its locus};\qquad(4):\ \text{the status record}.\ \blacksquare
$$

**Phys.** Weigh the parts and weigh the whole, and the whole is lighter by exactly the binding share — the corpus's oldest bookkeeping, now readable as the definition of the two levels. The decomposition-level read is not wrong; it is a read of the free members, and the free members carry no binding because the category bar said they could not. The unified read is a read of the constructed bound, and it is the only place in the inventory where a negative binding exists. Between them sits the exact gap, the ladder's own depth. And the four-slot no-go, which looked from some angles like the same obstruction, is not bridged but bypassed with honour: the atom never asked the colour grammar for a four-slot seal, so the no-go sleeps at its own locus, exactly as binding as it ever was.

---

## Tier 5.15 — The Opened Structure, the Era-Locality Table, and the Closure

### AT.35 — The opened-structure census: what the bridges open for the atomic era

**Thm.**
$$(1)\quad\textbf{the census (ten rows, each at its locus):}$$
$$\begin{array}{c|l|l}\# & \text{the opened structure} & \text{locus}\\\hline 1 & \text{the }Z\ge2\text{ classes constructed by the one mask, named by the schema} & [\mathrm{AT.25}(1);\ \mathrm{A\text{-}AT.4}]\\\hline 2 & \text{the binding fractions' ladder } 3A/(3A{+}1)^{2}\cdot\varepsilon_{\mathrm{EM}}^{2}/2 & [\mathrm{AT.25}(2);\ \mathrm{AT.22}(4)]\\\hline 3 & \text{the ionization continuum as the unbounded ladder's completion} & [\mathrm{AT.25}(3);\ \mathrm{BM.24};\ \mathrm{AT.9}(2)]\\\hline 4 & \text{the per-rung metric split: rest locked, kinetic on the }1/n^{2}\text{ shape} & [\mathrm{AT.26}]\\\hline 5 & \text{the fuzziness product }(5n^{2}+1)/6\text{ per shell, exact radicals} & [\mathrm{AT.27}]\\\hline 6 & \text{the envelope ratio of the two widths, exact monomial} & [\mathrm{AT.28}]\\\hline 7 & \text{the width bracket per level, tick-denominated, two-sided} & [\mathrm{AT.30}]\\\hline 8 & \text{the spectroscopic depth as a coupling step-function, exact thresholds} & [\mathrm{AT.31}(3),(4)]\\\hline 9 & \text{the unified mass read: pole + bracket on the constructed bound} & [\mathrm{Def\text{-}AT.7};\ \mathrm{AT.32}]\\\hline 10 & \text{the incommensurability verdict at the unified read} & [\mathrm{AT.33};\ \mathrm{AT.34}]\end{array}$$
$$(2)\quad\textbf{the census discipline:}\qquad\text{each row is a derived object at its own locus; the census adds no object, it tabulates the era's outputs}\qquad[\text{machine: the row-by-row scan}];$$
$$(3)\quad\textbf{the honest remainder (carried, } \neg\text{closed):}\qquad\text{the inertial mass scales }(\mu,\mu_\nu)\ \text{and the two-reads conversion [AT.4(3)]; the absolute rates under the named prerequisite [FT.131(3)];}$$
$$\text{the many-body shell energy [AT.12(4)]; the winding occupancy per named class [AT.11(6)]; the five geometry-program and interface rows [AT.17]; the naming beyond the schema [A-AT.4's bar]};$$
$$(4)\quad\textbf{the status:}\qquad\text{the remainder is the atomic era's own open list [AT.20(3)], restated with its extension additions named — nothing new left open by the extension except the brackets' absolute payee}.$$

**Req.** P1, P5 (Parts 1–2); FT.131(3) (Part 3); BM.24 (Part 4); AT.4(3), AT.9(2), AT.11(6), AT.12(4), AT.17, AT.20(3) (this part); A-AT.4, AT.22, AT.25–AT.34 (this part); the row-by-row document scan [math; machine: `checks/verify_Atomic5.py` §N].

**Pf.**
$$
(1),(2):\ \text{the census table against the tiers, row by row}\ [\text{machine: the document pins}]
$$
$$
(3):\ \text{the remainder list against AT.20(3)'s open rows and this part's additions};\qquad(4):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The prediction that opened this extension — that the two bridges would suddenly open structure for the atom's ledger — is here made good as a table, because in this corpus a promise is a census or it is nothing. Ten rows: the charge counter's remaining classes, their binding-fraction ladder, the continuum they accumulate toward; the energy split and the fuzziness product at every rung; the two widths and their ratio; the bracket on every level; the coupling thresholds at which the spectrum becomes resolvable; the mass observable as a pair; and the verdict that the fractions were addresses all along. Beside the table stands the honest remainder, carried forward untouched: the corpus does not close rows by silence.

### AT.36 — The era-locality table: every obstruction re-scoped at its own locus

**Thm.**
$$(1)\quad\textbf{the table (the discharge-without-revocation discipline [AT.20(2)'s pattern]):}$$
$$\begin{array}{l|l|l|l}\text{obstruction} & \text{binds in} & \text{the bridge} & \text{status}\\\hline\text{no canonical pair; no time operator [BM.10(1),(4)]} & \text{the finite register; the irreversible tick} & \text{the scope-local MT read [AT.29]} & \text{re-scoped: the register rows stand; the scope read exists}\\\hline\text{no EM sealing grammar [BM.48(3); BM.54(3)]} & \text{Part 4's inventory} & \text{the declared grammar [A-AT.1] + the masked orbit [AT.23--AT.24]} & \text{discharged (the opening tiers), force-backed (the extension)}\\\hline\text{amplitude }\ne\text{ mass [FT.79(5); FT.67(3a); FT.68(4)]} & \text{the free members' reads} & \text{the pole + bracket read [Def-AT.7; AT.32]} & \text{re-scoped: the free-member rows stand; the bound read is two-component}\\\hline\text{the four-slot no-go [BM.136(3)]} & \text{the colour slots} & \text{none needed — the channel change [AT.21]} & \text{stands, untouched}\\\hline\text{the rates' prerequisite [FT.131(3); BM.131(7)]} & \text{the emergent-time construction} & \text{the bracket ledger [AT.30--AT.31]} & \text{open with formed brackets}\end{array}$$
$$(2)\quad\textbf{the discipline row:}\qquad\text{every re-scope states the domain of the original row; no original row is retracted, weakened or cited out of its domain}\qquad[\mathrm{BM.10}\text{'s Rmk};\ \mathrm{AT.20}(2)];$$
$$(3)\quad\textbf{the status:}\qquad\text{the table is the era's methodological output: the corpus's negations are its boundaries, and its boundaries are its work order}\qquad[\text{machine: the row-by-row scan}].$$

**Req.** A6, L2 (Part 1); P5 (Parts 1–2); FT.67(3a), FT.68(4), FT.79(5), FT.131(3), FT.144(2) (Part 3); BM.10(1), BM.10(4), BM.10 Rmk, BM.48(3), BM.131(7), BM.136(3), BM.54(3) (Part 4); A-AT.1, AT.20(2) (this part); AT.21, AT.23, AT.24, AT.29, AT.30, AT.31, AT.32 (this part); the row-by-row document scan [math; machine: `checks/verify_Atomic5.py` §N].

**Pf.**
$$
(1),(2):\ \text{each row against the original obstruction's text and domain, and against this part's bridge tag}\ [\text{machine: the document pins}]
$$
$$
(3):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The corpus's negative theorems were never walls; they were surveys. The register bars said where a canonical pair cannot live, and the chart was built on the other side of the line a full era before this one needed it. The grammar bar said no EM seal existed, and the opening tiers declared one, and this extension backed the declaration with the force itself. The amplitude bar still protects the free members, and will always; at the bound it was never a bar but a specification — of what form the mass read would have to take. The four-slot no-go is not everyone's obstruction; it is the colour grammar's, and the atom simply never applied to it. And the rates' prerequisite remains open because the corpus does not declare its way to emergent time — but the bracket ledger now says exactly what the prerequisite is blocking, and what it is not. Read the table top to bottom and the corpus's method is visible as a single stroke: prove where a thing cannot be, then build the domain where it can, then re-scope the proof without ever unproving it.

### AT.37 — The calibration consolidation, the standing rules, and the era closure

**Thm.**
$$(1)\quad\textbf{the calibration row:}\qquad\neg\text{a new parameter, } \neg\text{a new scale, } \neg\text{a new P4 member}\qquad[\mathrm{P1};\ \mathrm{P4};\ \mathrm{\§Cal\text{-}5b}]:\qquad\text{the width, bracket and threshold rows are built from }\hbar=1\ \text{[BM.10(3)], the tick [D1.8], } E_{\mathrm{int}}\in\{2,6\},\ \ln2,\ \mathfrak h;\qquad e\ \text{symbolic throughout [C-AT.1 re-logged]};$$
$$(2)\quad\textbf{the standing rules:}\qquad\neg\exists\ \text{a measured external value in any clause}\ [\mathrm{P5}];\qquad\text{the bracket discipline: a spread is an inequality, never a value [}\S0.2b\text{]};$$
$$\text{the era-locality discipline: obstructions are discharged or re-scoped at their own loci [AT.36]};\qquad\text{species names confined to the identification layers [A-AT.4; Def-AT.3's pattern]};$$
$$(3)\quad\textbf{the DAG row:}\qquad\text{nothing in the canon cites this part; the citations of this part resolve to Parts 1--4, Census cells, and earlier tags of this part}\qquad[\text{machine: the citation closure scan}];$$
$$(4)\quad\textbf{the adjudication:}\qquad\boxed{\ \textbf{the atomic era's extension closes with both bridges built in the corpus's own discipline — the scope clock as a read, the unified mass as a pole with a bracket — and the atom's ledger opens: ten structures where one ladder stood}\ }$$
$$[\text{machine: the row-by-row discharge census against the charter's outputs and AT.35's table}].\ \blacksquare$$

**Req.** D0.4, D1.8 (Parts 1–2); CT2.1 (Part 2); P1, P4, P5 (Parts 1–2); FT.44(4) (Census); FT.131(3) (Part 3); BM.10(3), BM.53(3) (Part 4); C-AT.1, AT.4(3), AT.11(6), AT.12(4), AT.17, AT.20(2), AT.20(3) (this part); A-AT.3, A-AT.4, AT.29–AT.36 (this part); the citation-closure scan, the discharge census [math; machine: `checks/verify_Atomic5.py` §N].

**Pf.**
$$
(1),(2):\ \text{the calibration and standing-rule records against } \S\text{Cal-5b and } \S0.2
$$
$$
(3):\ \text{the citation-closure scan}\ [\text{machine}];\qquad(4):\ \text{the discharge census against the charter's output list and AT.35's table}\ [\text{machine}].\ \blacksquare
$$

**Phys.** The ledger closes the way the era opened: with nothing added. No parameter was issued, no scale was declared, no measured value slipped past the quarantine, and the coupling that prices every new row remains exactly as symbolic as it was when Part 4 logged it. The two bridges stand built — not as metaphors but as tagged rows with machine checks: a clock read that exists precisely where the corpus proved a time operator cannot, and a mass read that carries its fuzziness as an interval precisely where the corpus forbade carrying it as a number. The atomic era receives ten opened structures and keeps its honest remainder. The books balance; the fractions live at their addresses; and the one force still needs only one mask.

---

---

## Closure exports of the opening tiers (Tiers 5.0–5.9; consumed by no part of the canon)

$$
\begin{array}{c|c}
\text{export} & \text{the row}\\\hline
\text{the nuclear grammar} & G_\varepsilon(A)=(3A)!/(A!\,6^{A}),\ \text{the all-}\varepsilon\text{ cells with the type selection}\ [\mathrm{AT.1}]\\
\text{the nuclear ledger} & M(A,Z)=6A\ln2/\mathfrak h+Z\,\Delta m_{\mathrm{EM}},\ \varepsilon=(-1)^{A},\ r_s=3A\,\mathfrak h\ [\mathrm{AT.2},\ \mathrm{AT.3}]\\
\text{the lepton floors} & E_{\mathrm{int}}^{(\ell)}=E_{\mathrm{int}}^{(\nu)}=2,\qquad m\,\mathfrak h=2\ln2\ \text{at the floors}\ [\mathrm{AT.4}]\\
\text{the reduced masses} & m_r=\dfrac{6\ln2\,(1+c\,\varepsilon_{\mathrm{EM}})}{\mathfrak h\,(4+3\,c\,\varepsilon_{\mathrm{EM}})},\qquad m_r^{(A)}=\dfrac{6A\ln2}{\mathfrak h\,(3A+1)}\ [\mathrm{AT.5}]\\
\text{the binding ladder} & E_n=-\dfrac{\varepsilon_{\mathrm{EM}}^{2}\,m_r}{2\,n^{2}},\qquad E_1=-\dfrac{3\,e^{4}\ln2\,(1+c\,\varepsilon_{\mathrm{EM}})}{16\pi^{2}\,\mathfrak h\,(4+3\,c\,\varepsilon_{\mathrm{EM}})}\ [\mathrm{AT.6},\ \mathrm{AT.8}]\\
\text{the neutrality} & Q(\text{atom}(A,Z))=0,\qquad\text{the exterior flux }e\,Q=0\ \text{exactly}\ [\mathrm{AT.7},\ \mathrm{AT.12}]\\
\text{the exclusion and shells} & \mathrm{cap}(n)=2n^{2}:\ 2,\ 8,\ 18,\ 32;\qquad\mathrm{Cum}:\ 2,\ 10,\ 28,\ 60\ [\mathrm{AT.11},\ \mathrm{AT.13}]\\
\text{the statistics} & \varepsilon(\text{atom}(A,Z))=(-1)^{A+Z}\ \text{at the floors}\ [\mathrm{AT.12}(3)]\\
\text{the era state} & (\mathrm{P5.1})\text{–}(\mathrm{P5.10})\ \text{dispositioned; the atom constructed; the ledger balanced}\ [\mathrm{AT.20}]
\end{array}
$$

---

---

## Closure exports of the extension (Tiers 5.10–5.15; consumed by no part of the canon)

$$
\begin{array}{c|c}
\text{export} & \text{the row}\\\hline
\text{the bound-channel census} & \mathbf F\big|_{\text{pair}}=F_{\mathrm{EM}}\big|_{\text{mask}}\oplus\text{the members' sealed reads};\ \ \Delta E_{D^-}=0;\ \ |E_1|/(m_p+m_\ell)\le\tfrac{3}{32}\ [\mathrm{AT.21},\ \mathrm{AT.22}]\\
\text{the price identity} & \Delta m_{\mathrm{EM}}\ \text{three routes, one monomial; A-AT.1 force-backed}\ [\mathrm{AT.24}]\\
\text{the opened classes} & E_n^{(A,Z)}=-\varepsilon_{\mathrm{EM}}^{2}m_r^{(A,Z)}/2n^{2},\quad |E_1|^{(A)}/(m_N+m_\ell)=\tfrac{3A}{(3A{+}1)^{2}}\cdot\tfrac{\varepsilon_{\mathrm{EM}}^{2}}{2}\ [\mathrm{AT.25}]\\
\text{the per-rung split} & \mathfrak M_n=M(A,Z)+m_\ell+E_n;\quad\langle\mathrm{KE}\rangle_n=|E_n|,\ \langle V\rangle_n=2E_n\ [\mathrm{AT.26}]\\
\text{the fuzziness product} & (\Delta x_n\,\Delta p_n)^{2}=(5n^{2}+1)/6;\ \ \Delta x\,\Delta v=\tfrac{1}{m_r}\sqrt{\tfrac{5n^{2}+1}{6}}\ [\mathrm{AT.27}]\\
\text{the width bracket} & 1/(2\tau_n)\le\Delta E_n\le|E_n|;\ \ \tau_n\ge n^{2}/\kappa\ \text{for nonemptiness}\ [\mathrm{AT.30}]\\
\text{the resolvability thresholds} & \kappa\ge2n^{2}(n{+}1)^{2}/3(2n{+}1)\ \text{(adjacent)};\quad\kappa\ge n^{2}/3\ \text{(level)}\ [\mathrm{AT.31}]\\
\text{the unified mass read} & \mathfrak M_n(A,Z)\ =\ \text{pole}+\text{bracket, two-component}\ [\mathrm{Def\text{-}AT.7};\ \mathrm{AT.32}]\\
\text{the incommensurability verdict} & \neg\exists\ \text{a fractional mass value at the unified read; the fractions are addresses}\ [\mathrm{AT.33}]\\
\text{the era-locality table} & \text{five obstructions, re-scoped at their own loci}\ [\mathrm{AT.36}]
\end{array}
$$

---

## Collapse charter (Tiers 5.16–5.18): the Strong-Side Channel — the 2-Edge Transition Defect, the Topology Collapse, and the Cross-Currency Bridge

**0.1c Charter of the collapse extension.** The collapse extension continues the atomic era — incrementally, inside this part, with no new era declared — into the layer of the strong-side two-body channel: the constructions the opening and extension tiers located at the seal boundary and left unpriced, named with precision and built here. Its foundation stack, by citation: (i) the digon floor and the mass law [FT.28; FT.44(4); Def-BM.4]: the minimal closed chain, its informational mass and its Born width; (ii) the two-bit floor on both channels [AT.4]: one seal count carrying two currency reads; (iii) the multi-baryon supports and the nuclear ledger [Def-AT.1; AT.1–AT.3]: the merged supports exist; their count-route mass is additive and prices no re-organization; (iv) the ensemble laws [BM.19(2); BM.94(4)–(6); BM.137(1)–(4)]: the flicker measure, the formed binding, the separated-reads rows; (v) the binding category bar and the weak balance [BM.48(4)–(5); BM.49(1)]: binding belongs to the bound system; the transition balance carries one floor-read slot; (vi) the bridge slot [A-BM.9; BM.69(2),(4); BM.98]: the declared dimensionless exchange slot, value ¬issued; (vii) the singular force and its mask [A8; CT2.3–CT2.4; AT.21]: one force, one active mask, no smooth potential admitted anywhere; (viii) the width ledger and the unified read [AT.28–AT.31; Def-AT.7; AT.32]: the bracket discipline the collapse read must join without violating. Its outputs: the 2-edge defect read and its weak-balance row (Tier 5.16); the collapse channel with its census invariants and its two-term binding functional (Tier 5.17); the cross-currency exchange identity, the re-priced reduced mass, and the integration audit (Tier 5.18). Its enumerative substrate remains the Census block: the 25 cells, consumed by tag citation and extended by no new cell [AT.18(1),(3)]. The charter adds one declared dimensionless slot (A-AT.5) and one symbolic-use log row (C-AT.2); it adds no dimensionful scale [P1] and no P4 member [P4].

**0.2c Standing bars of the collapse extension.** No smooth-manifold potential enters any collapse row: the binding functional is census-borne, and no Yukawa-type, Woods–Saxon-type, liquid-drop or other phenomenological bookkeeping is admitted at any locus [BM.48(1)'s derived-potential discipline, extended]. No measured value attaches to the defect unit, the collapse yields, the per-bond ladder, the exchange factor or the bridge slot [P5]; the generator-layer numeric readings that motivated the tier — any energy-unit figure for the defect unit, for the rungs of the ladder, for the exchange ratio — live in the identification layer only and enter no **Thm** clause of this or any part. Species names are confined to the identification layers already logged [A-AT.2; A-AT.4]; the collapse read is a bound-system read: the category bar stands unmodified for free members [BM.48(4),(5); AT.3(5)], and the era-locality discipline governs the re-scope [AT.36(2)'s pattern]. Amplitude $\ne$ mass [FT.79(5)]; rung $\ne$ scale [D0.8]; the chart-side rows carry their conditionality explicitly [Def-BM.4(5); BM.10(3)].

---

## §Cal-5c — Free internal parameters of the collapse extension (P4-class)

**One declared slot; no dimensionful scale.** Inherited and undeclared: the single dimensionful scale $\mathfrak h$ [P1]; the fermion-era registry Cal-F ($\hat\mu'^2$ among its slots) [Cal-F]; the baryomesonic register [Cal-BM]: the bridge ratio slot $\rho_{\mathrm B}=\hat\mu'^2\mathfrak h^2/(\ln2)^2\in\mathfrak q^0$ [A-BM.9, value $\neg$issued], the electric-coupling slot $e_0$ [C-BM.2, value $\neg$issued], the channel-scale rows [C-BM.3]; the atomic symbolic-use logs [C-AT.1]. Declared here, before use:

$$(\mathrm{A\text{-}AT.5})\quad\varepsilon_{\mathrm{col}}\in\mathfrak q^{0}:\ \ \text{the collapse-yield slot — the dimensionless structural read of one interface digon's retirement at complete seal-sharing; value}\ \neg\text{issued}.$$

**The symbolic-use log (one addition; the parameter census).** Every new row of the collapse extension is an exact rational or monomial form in $(\mathfrak h,\ln2)$ over the integer counters $(A,Z)$ and the dimensionless slots: the A4 datum $\varepsilon_q$ [D0.4, ¬a parameter], the declared $\varepsilon_{\mathrm{col}}$ [A-AT.5, value ¬issued], the inherited $\rho_{\mathrm B}$ [A-BM.9, value ¬issued], and the exchange factor $\xi$ (a derived function of $\rho_{\mathrm B}$ and the lepton sector's own census, defined in the bridge theorem of Tier 5.18, ¬a new slot). The slot is the strong-side analogue of the electric coupling's discipline [C-BM.2 $\to$ C-AT.1's precedent]: used symbolically, never as a number:

$$(\mathrm{C\text{-}AT.2})\quad\varepsilon_{\mathrm{col}}:\ \ \textbf{used symbolically in Tiers 5.16–5.18, value}\ \neg\text{issued},\ \neg\text{fixed by measurement}\ [\mathrm{P5}].$$

No second dimensionful scale exists [P1]; the slot is ¬a dimensionful scale, ¬a P4 member [P4], and its derivation grounds are BM.69(4)'s four, applied mutatis mutandis. Machine verification uses declared rational witnesses in the checker only; no witness value enters the canon.

---

## §A-AT (collapse extension) — Logged declaration III (issued before use)

**A-AT.5 (the collapse-yield slot and the merged-cell census grammar; issued before use — a forward pointer to the census definition, Def-AT.9).** Two clauses, one declaration. **(i) The slot.** The corpus's mass law prices internal edges: $m_{\mathrm{hid}}=E_{\mathrm{int}}\ln2/\mathfrak h$ [FT.44(4)], and prices no boundary re-organization: the count routes of the merged supports are exactly additive [BM.111(1); AT.3(1); BM.148(3)'s cells], the ensemble routes price flicker and not seals [BM.137(3),(4)], and the pole routes are additive at every formed level [BM.111(2); BM.137(5)]. A sealed core's retirement of vacuum-facing boundary obligation at a shared interface is therefore not derivable from the prior rows — it is a new dimensionless structural read, declared as $\varepsilon_{\mathrm{col}}\in\mathfrak q^0$ and packaged in the species of A-BM.9: a packaging of the mask's own lock content [CT4.1a; CT4.3], hence ¬a new free parameter of the P1 register and ¬a dimensionful scale; the derivation grounds are BM.69(4)'s four; the value is ¬issued [P5]. **(ii) The census grammar.** The merged support of $A$ sealed cores is read at the envelope locus as a cell complex — vertices the cores, edges the pairwise interface digons the mask admits at complete sealing, faces the membrane seals spanning bond triangles — and its census bookkeeping (bond count, face count, incidence, Euler read) is chart-side bookkeeping on already-constructed objects [Def-BM.4(5)'s envelope clause; A §0.2], ¬a materialized ledger structure [D1.6]. What the declaration does **not** do: it adds no axiom, no dimensionful scale, no P4 member [P1, P4]; it issues no value of $\varepsilon_{\mathrm{col}}$ [C-AT.2]; it constructs no dynamics — the collapse is a threshold-gated channel and its rates stay (P5.3)-scoped [FT.131(3)]. Everything Tiers 5.16–5.18 prove is a theorem **about** the declared structure, from prior tags and exact-arithmetic steps alone.

---

## Tier 5.16 — The 2-Edge Transition Defect: the Digon's Curvature-Currency Read

### Def-AT.8 — The 2-edge defect read and the currency-pair row

**Def.** The **2-edge defect read** is the informational mass of the digon floor referred to the sealed (baryon-curvature) ledger:
$$\mathfrak m_{[2]}\ :=\ \frac{2\ln2}{\mathfrak h}\qquad[\mathrm{FT.44}(4)\ \text{at}\ E_{\mathrm{int}}=2;\ \mathrm{FT.28};\ \text{machine: the monomial}].$$
$$(1)\quad\textbf{the currency-pair row:}\qquad\text{the seal count }E_{\mathrm{int}}=2\text{ carries two reads on two ledgers — the fugacity-side floor read (AT.4's line, }m\,\mathfrak h=2\ln2\text{) and the curvature-side defect read }\mathfrak m_{[2]}:$$
$$\textbf{one seal count, two currencies, separated species}\qquad[\mathrm{BM.137}(4)\text{'s pattern};\ \mathrm{BM.37}(2)];$$
$$(2)\quad\textbf{the notation row:}\qquad\text{the defect read is }\mathfrak m_{[2]}\text{ and nothing else};\qquad\text{the corpus's lepton-floor symbol keeps its published meaning at its own rows [AT.4; AT.5; BM.49(1)] and is cited only there};$$
$$\textbf{no row of this extension writes the lepton-floor symbol for the defect — the two objects share a monomial and nothing else};$$
$$(3)\quad\textbf{the dimensional row:}\qquad[\mathfrak m_{[2]}]=\mathfrak q^{1/2}=[\text{mass}]\qquad[\mathrm{CT2.1};\ \text{machine: the exponent arithmetic}];$$
$$(4)\quad\textbf{the width row:}\qquad\Delta x_{\mathrm B}^{(2)}=\frac{\mathfrak h}{2\ln2}\qquad[\mathrm{Def\text{-}BM.4}(1);\ \mathrm{BM.13}(1),(3)]:\qquad\text{the defect unit and its Born width are one Laurent pair, exact}.$$

**Rmk (naming).** *2-edge defect read* names the curvature-currency read of the minimal seal; *defect unit* names the same object as the denomination of the collapse functional of Tier 5.17. Both are bookkeeping names on derived quantities [A §0.2]; neither is a measurement, and no external datum enters [P5].

**Req.** FT.28, FT.44(4) (Part 3, Census); Def-BM.4(1), BM.13(1), BM.13(3), BM.37(2), BM.137(4) (Part 4); AT.4(1), AT.5 (this part); CT2.1 (Part 2); P1, P5 (Parts 1–2); exact Laurent-monomial arithmetic, exponent censuses ath; machine: `checks/verify_Atomic5.py` §O].

**Pf.**
$$
\text{Definition block: the read is FT.44(4)'s law at }E_{\mathrm{int}}=2\ \text{re-referred to the baryon ledger [machine: one monomial]};\qquad(1):\ \text{AT.4(1)'s floor row and BM.137(4)'s separated-species row re-cited};
$$
$$
(2):\ \text{the notation record [verbatim scan: the extension's defining clauses carry }\mathfrak m_{[2]}\text{ alone]};\qquad(3):\ [2\ln2/\mathfrak h]=[\mathfrak h]^{-1}=\mathfrak q^{1/2}\ [\mathrm{CT2.1;\ machine}];\qquad(4):\ \mathrm{BM.13}(1)\text{'s substitution at }E=2\ [\text{machine}].\ \blacksquare
$$

**Phys.** The corpus gave the digon two jobs and kept them in two ledgers: the fugacity line reads the two-bit floor as the lepton's mass, the baryon line counts the same two edges as the unit of everything it seals. What the defect read adds is the second line's name — the price a sealed core denominates its boundary re-organization in — and the discipline that the sharing of a monomial is not the sharing of an object. The notation row exists because the two roles must never merge: a lepton-floor citation stays a lepton-floor citation, and the defect unit stays the defect unit, even where the algebra underneath them is one and the same.

### AT.38 — The transition defect theorem: the weak-balance unit in the baryon currency

**Thm.**
$$(1)\quad\textbf{the uniqueness row:}\qquad\text{the minimal closed chain is the digon and it is unique at }E_{\mathrm{int}}=2\qquad[\mathrm{FT.28};\ \mathrm{Def\text{-}H.4}:\ \delta h(c)\ge2;\ \mathrm{BM.13}(3)\text{'s sharp threshold at the floor}]:$$
$$\text{every seal reconfiguration of a sealed composite exchanges boundary content in closed-chain units, and the minimal unit is the digon};$$
$$(2)\quad\textbf{the defect row:}\qquad\mathfrak m_{[2]}\,\mathfrak h\ =\ 2\ln2\qquad[\mathrm{FT.44}(4)\ \text{at}\ E_{\mathrm{int}}=2;\ \text{machine: the monomial identity at declared witnesses}];$$
$$(3)\quad\textbf{the balance row:}\qquad\text{the weak transition balance carries exactly one floor-read slot}\qquad[\mathrm{BM.49}(1):\ Q_{\mathrm{corr}}=-(\Delta m_{\mathrm{EM}}+m_\ell+m_\nu)]:$$
$$\text{at the floor }m_\ell\,\mathfrak h=2\ln2\ \ [\mathrm{AT.4}(1)]:\qquad\boxed{\ \text{the transition-balance unit, in the baryon currency, is one defect unit }\mathfrak m_{[2]}\ \text{per reconfigured junction}\ }$$
$$[\text{machine: the slot identity }m_\ell\,\mathfrak h=\mathfrak m_{[2]}\,\mathfrak h=2\ln2\ \text{at the floor}];$$
$$(4)\quad\textbf{the ratio row (calibration-free):}\qquad\mathfrak m_{[2]}:m^{(1)}_{\mathrm{hid}}\ =\ 2\ln2:6\ln2\ =\ 1:3,\qquad m^{(A)}_{\mathrm{hid}}/\mathfrak m_{[2]}=3A\ \ \text{on the count route}\qquad[\mathrm{AT.3}(1);\ \text{machine: exact integer ratios}]:$$
$$\text{the defect unit is one third of the baryon's count-route unit, independent of any calibration of }\mathfrak h;$$
$$(5)\quad\textbf{the calibration row:}\qquad\text{a nucleon-side calibration of }\mathfrak h\ \text{(the declared form: the }\mathfrak h\text{-value at which the count-route nucleon read is referred) is a calibration step in the species of }\mathrm{EM.25}(7):$$
$$\text{value}\ \neg\text{issued}\ [\mathrm{P5}];\qquad\text{under it the defect unit evaluates at its identification-layer reading, and the ratio row (4) is unchanged [machine: the ratio is integer]};$$
$$(6)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(5);\qquad\neg\text{a new particle},\ \neg\text{a P4 member},\ \neg\text{a dimensionful scale}\ [\mathrm{P1}];\qquad\neg\text{a value issued}\ [\mathrm{P5}].$$

**Rmk (what the defect is not).** The defect unit is not a new mass term on any free member: the category bar and the count-route record stand unmodified [BM.48(4),(5); AT.3(5)]. It is the denomination of a sealed core's boundary re-organization — the unit in which a transition that passes one digon across the seal is booked — and it is priced exactly because the digon's own mass read is priced exactly. Where the generator layer named a numeric transition-defect reading, the canon speaks of $\mathfrak m_{[2]}$: the identification-layer attachment, recorded in the identification layer only [0.2c].

**Req.** FT.28, FT.44(4), Def-H.4 (Part 3, Census); Def-BM.4, BM.13(3), BM.46(4), BM.48(4), BM.48(5), BM.49(1) (Part 4); EM.25(7) (Part 2); CT2.1 (Part 2); AT.3(1), AT.3(5), AT.4(1) (this part); P1, P5 (Parts 1–2); exact monomial identities, integer ratio reductions, witness substitution ath; machine: `checks/verify_Atomic5.py` §O].

**Pf.**
$$
(1):\ \mathrm{FT.28}\text{'s floor row and Def-H.4's }|R|\ge2\text{ re-cited; BM.13(3)'s sharpness at }E_{\mathrm{int}}=2\ \text{[machine: the threshold census]};\qquad(2):\ \mathfrak m_{[2]}\,\mathfrak h=2L\ \text{at the witness }L\ \text{[machine]}
$$
$$
(3):\ \mathrm{BM.49}(1)\text{'s balance re-cited; the slot identity at the floor [machine: one monomial, two referrals]};\qquad(4):\ 2/6=1/3,\ 6A/2=3A\ \text{[machine: integer arithmetic]}
$$
$$
(5):\ \text{the calibration-form record, }\neg\text{a value [P5]};\qquad(6):\ \text{assembly}.\ \blacksquare
$$

**Phys.** A weak transition asks a sealed core to re-label its boundary, and the corpus now answers with a number it already owned: the smallest thing that can cross a seal is the digon, the digon's mass read is two bits exactly, and the balance row of the beta ledger has been carrying exactly one such unit at the floor read all along. The baryon-currency reading changes nothing in Part 4's signs or bars — it names the unit the balance was already denominated in, and it fixes the defect unit's place in the count-route ladder at one third of a baryon, a pure integer ratio that no calibration can move.

### AT.39 — The defect in the δ-seal grammar: the interface class and the reorganization ledger

**Thm.**
$$(1)\quad\textbf{the δ-class row:}\qquad\text{the digon is the floor of the δ-sealed class: }\Theta_{\mathrm{int}}=2\ \text{at }k=1\ \ [\mathrm{FT.28}\text{'s floor fermion}];\qquad\Theta_{\mathrm{int}}\in2\mathbb Z\ \text{on the δ-sealed class}\ \ [\mathrm{BM.2}(1);\ \text{Census FT.35}(3)]:$$
$$2\in2\mathbb Z\setminus4\mathbb Z\qquad[\text{machine}]:\qquad\textbf{the interface digon of any two sealed cores is δ-class bookkeeping — the baryon junctions' }4\mathbb Z\text{ row [Census FT.49(3)] is untouched by it};$$
$$(2)\quad\textbf{the meson-floor row:}\qquad\text{the count routes price no re-organization:}\qquad m^{\mathrm{meson}}_{\mathrm{hid}}=\frac{2E_{\mathrm{int}}(c)\ln2}{\mathfrak h}\ \ \text{additively, the informational-route binding vanishing identically}\qquad[\mathrm{BM.111}(1)]:$$
$$\text{at the digon constituent: }\ m^{\mathrm{meson}}_{\mathrm{hid}}\big|_{E_{\mathrm{int}}(c)=2}=2\,\mathfrak m_{[2]}\qquad[\text{machine: the monomial}];$$
$$(3)\quad\textbf{the reorganization-ledger row:}\qquad\text{the defect ledger is a read species distinct from the count routes and from the ensemble route}\qquad[\mathrm{BM.137}(4)\text{'s separated-reads pattern};\ \mathrm{BM.37}(2)\text{'s disjointness}]:$$
$$\neg\exists\ \text{a derived equation relating the defect read to the count-route reads; the bridge between the species is slot-borne}\qquad[\mathrm{A\text{-}BM.9};\ \mathrm{BM.98}];$$
$$(4)\quad\textbf{the mass-defect-unit row:}\qquad\text{nuclear reconfiguration is denominated in digon units: the collapse functional of AT.40 is an exact rational multiple of }\mathfrak m_{[2]}\qquad[\text{forward pointer; machine: }\S\mathrm{P}];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\neg\text{a measured value}\ [\mathrm{P5}];\qquad\text{the mesonic δ-sealed rows stand untouched}\ [\mathrm{BM.31}\text{--}\mathrm{BM.33}].$$

**Req.** FT.28, FT.35(3), FT.49(3) (Part 3, Census); BM.2(1), BM.31, BM.32, BM.33, BM.37(2), BM.98, BM.111(1), BM.137(4) (Part 4); A-BM.9 (Part 4); Def-AT.8, AT.38(2) (this part); P5 (Parts 1–2); exact integer divisibility, monomial identities ath; machine: `checks/verify_Atomic5.py` §O].

**Pf.**
$$
(1):\ 2\bmod2=0,\ 2\bmod4=2\ \text{[machine]};\qquad(2):\ 2\cdot2L/\mathfrak h=2\,\mathfrak m_{[2]}\ \text{[machine]};\qquad\mathrm{BM.111}(1)\text{'s additivity row re-cited}
$$
$$
(3):\ \mathrm{BM.137}(4)\text{'s separation and BM.37(2)'s disjointness re-cited; the slot-borne bridge [A-BM.9]};\qquad(4):\ \text{the forward-pointer row: the collapse functional is an exact rational multiple of }\mathfrak m_{[2]}\ \text{[machine: }\S\mathrm{P}];\qquad(5):\ \text{assembly}.\ \blacksquare
$$

**Phys.** The δ-seal always was the pair grammar's own signature — two edges, winding two, the class the baryon junctions' four-multiple phases exclude — and the interface between two sealed cores wears exactly that signature. The meson's count routes said it first: sealing decides what forms, not what things weigh. The defect ledger is the third book the seal grammar now keeps — not the count, not the flicker, the re-organization — and its unit is the digon's own read, inherited rather than introduced.

---

## Tier 5.17 — The Topology Collapse: the Merged-Cell Census and the Binding Functional

### Def-AT.9 — The collapse channel and the merged-cell census

**Def.** Let $\mathcal X$ be a merged support of $A\ge2$ sealed cores constructed by the multi-baryon grammar [Def-AT.1; AT.1], read at the envelope locus.
$$(1)\quad\textbf{the gate:}\qquad\text{the collapse channel is open at chart separations }d<\Delta x_1+\Delta x_2:\qquad\text{for the nucleon pair }\ d<2\,\Delta x^{\mathrm B}_{\mathrm N}=\frac{\mathfrak h}{3\ln2}\qquad[\mathrm{Def\text{-}BM.4}(1);\ \mathrm{AT.3}(1);\ \text{machine: the monomial}]:$$
$$\text{the gate is sub-hop exactly when }3\ln2>1\ \text{[machine: the exact enclosure }\ln2\ge\tfrac58>\tfrac13\text{; D1.6's locus discipline]}:\qquad\text{a chart-side envelope condition, }\neg\text{a ledger distance}\ \ [\mathrm{Def\text{-}BM.4}(5)];$$
$$(2)\quad\textbf{the seal complex:}\qquad\text{the census bookkeeping of }\mathcal X\ \text{[A-AT.5(ii)]}:\quad\text{vertices: the }A\text{ cores};\quad\text{edges: the pairwise interface digons admitted at complete sealing: } \mathcal E_A=\binom{A}{2};$$
$$\text{faces: the membrane seals spanning bond triangles: }\mathcal F_A=\binom{A}{3};\qquad\text{the incidence }f_b\ \text{of a bond }=\ \text{its face count};\qquad\textbf{the Euler read}\ \ \eta_A:=A-\mathcal E_A+\mathcal F_A;$$
$$\textbf{the closure criterion:}\quad\text{the seal complex is closed iff every edge carries exactly two faces};$$
$$(3)\quad\textbf{the census table at }A\in\{2,3,4\}:\qquad(\mathcal E_A,\ \mathcal F_A,\ \eta_A,\ \text{incidences})\ =\ (1,\,0,\,1,\ \{0\}),\ \ (3,\,1,\,1,\ \{1\}),\ \ (6,\,4,\,2,\ \{2\})\qquad[\text{machine: }\S\mathrm{P}]:$$
$$\textbf{the chain (pure surface), the braced triangle, the closed tetrahedral surface — volume closure exactly at }A=4;$$
$$(4)\quad\textbf{the seal-compatibility clause:}\qquad\text{the channel's cores are seal-compatible: each core's facing boundary zone carries the conjugate phase class of its partner's}\qquad[\mathrm{BM.111}(2)\text{'s conjugate-value row};\ \mathrm{Def\text{-}BM.1}\text{'s validity clause at the interface}]:$$
$$\text{the nucleus--anti-nucleus locus and the constituent-sub-network locus both satisfy it; no smooth potential is required and none is admitted}\ \ [0.2\mathrm c].$$

**Rmk (locus).** The seal complex is chart-side census bookkeeping on supports the grammar already constructs — the species of the Born width itself [Def-BM.4(5)'s envelope clause; A §0.2] — ¬a new ledger object, ¬a materialized structure [D1.6]. Declared at A-AT.5 before use.

**Req.** FT.28, FT.44(4) (Part 3, Census); Def-BM.1, Def-BM.4(1), Def-BM.4(5), BM.13(1), BM.111(2) (Part 4); Def-AT.1, AT.1, AT.3(1) (this part); A8, D1.6 (Parts 1–2); CT2.3, CT2.4 (Part 2); CT4.1a, CT4.3 (Part 2); exact binomial censuses, rational $\ln2$ enclosures ath; machine: `checks/verify_Atomic5.py` §P].

**Pf.**
$$
(1):\ \Delta x^{\mathrm B}_{\mathrm N}=\mathfrak h/(6\ln2)\ \text{[BM.13(1) at }E=6]\implies2\Delta x^{\mathrm B}_{\mathrm N}=\mathfrak h/(3\ln2)\ \text{[machine]};\qquad3\ln2>1\ \text{[machine: the partial-sum enclosure }S_2=\tfrac58]
$$
$$
(2):\ \text{the census definitions [A-AT.5(ii)]};\qquad(3):\ \binom22=1,\binom23=0;\ \binom32=3,\binom33=1;\ \binom42=6,\binom43=4;\ \eta=1,1,2;\ \text{incidences }0,1,2\ \text{[machine: }\S\mathrm{P]}
$$
$$
(4):\ \mathrm{BM.111}(2)\text{'s conjugate row and Def-BM.1's validity clause re-cited}.\ \blacksquare
$$

**Phys.** Two sealed cores whose envelopes overlap are not two cores any more at the chart's resolution: the grammar that already builds their merged support now also reads its shape. The reading is deliberately spare — vertices, interface digons, membranes, one Euler count — because everything the binding will need is in the counting: which bonds touch only vacuum, which are braced by a membrane, and whether the cell closes. The gate is the same kind of object as the Born width itself, an envelope statement and not a ledger distance, and the channel it gates needs no potential of any smooth-manifold species.

### AT.40 — The topology collapse functional and the per-bond ladder

**Thm.** Let $\mathcal X$ be the merged support of $A\in\{2,3,4\}$ baryonic cores [Def-AT.9], $u=4\varepsilon_q\in[0,1)$ the flicker residue, $D_n=1+u+\cdots+u^{n-1}$ [BM.137(1)].
$$(1)\quad\textbf{the ensemble merge term (derived, corpus-native):}\qquad\text{the merged support is one flicker ensemble over }3A\text{ pairs; the separate configuration is }A\text{ independent 3-pair ensembles}\qquad[\mathrm{BM.137}(1)\ \text{at }n=3A\ \text{and at }n=3;\ \mathrm{BM.94}(4)]:$$
$$b^{\mathrm{ens}}_A\ :=\ A\,\mathcal B^{(3)}_{\mathrm{ens}}-\mathcal B^{(3A)}_{\mathrm{ens}}\ =\ 6A\Bigl(\frac1{D_3}-\frac1{D_{3A}}\Bigr)\frac{\ln2}{\mathfrak h}\ >\ 0\quad\forall\,u\in(0,1),\qquad b^{\mathrm{ens}}_A=0\iff u=0$$
$$[\mathrm{BM.137}(3)\text{'s formed binding re-read across the merge};\ D_n-1=uD_{n-1};\ \text{machine: exact rational grid}]:\qquad\text{the term is the difference of two formed quantities and adds no mechanism};$$
$$(2)\quad\textbf{the brace census (declared grammar, derived census):}\qquad b^{\mathrm{col}}_A\ :=\ \varepsilon_{\mathrm{col}}\;G_A\;\mathfrak m_{[2]},\qquad G_A:=\sum_{b}\,(1+f_b)\ =\ \mathcal E_A+3\,\mathcal F_A\qquad[\mathrm{A\text{-}AT.5};\ \mathrm{Def\text{-}AT.9}(2)]:$$
$$\text{each membrane braces its three edges; the base }1\text{ is the digon exchange itself;}\qquad G_A=(1,\ 6,\ 18)\ \ \text{at}\ A=(2,\,3,\,4)\qquad[\text{machine: the census}];$$
$$(3)\quad\textbf{the per-bond ladder:}\qquad\beta_A:=b^{\mathrm{col}}_A/\mathcal E_A=\varepsilon_{\mathrm{col}}\,(1+\bar f_A)\,\mathfrak m_{[2]},\qquad\bar f_A=3\mathcal F_A/\mathcal E_A:\qquad\bar f=(0,\ 1,\ 2):\qquad\beta_2<\beta_3<\beta_4\qquad[\text{machine}]:$$
$$\boxed{\ \text{the per-bond cost is a strict function of the merged cell's geometry — surface bonds, edge-braced bonds, volume-braced bonds — and is not constant across }A\ }$$
$$\text{the ladder rises with the cell's closure; the }\alpha\text{-closure }(\eta_4=2,\ \text{all incidences }2)\ \text{is the first volume-sealed cell}\ \ [\mathrm{Def\text{-}AT.9}(3);\ \text{machine}];$$
$$(4)\quad\textbf{the functional:}\qquad\boxed{\ b_A\ =\ \underbrace{6A\Bigl(\tfrac1{D_3}-\tfrac1{D_{3A}}\Bigr)\tfrac{\ln2}{\mathfrak h}}_{\text{the ensemble merge (derived)}}\ +\ \underbrace{\varepsilon_{\mathrm{col}}\,\bigl(\mathcal E_A+3\mathcal F_A\bigr)\,\mathfrak m_{[2]}}_{\text{the brace census (declared slot)}}\ }\qquad(A\in\{2,3,4\}):$$
$$b^{\mathrm{col}}_3/b^{\mathrm{col}}_2=6,\qquad b^{\mathrm{col}}_4/b^{\mathrm{col}}_2=18\qquad[\text{machine: exact, independent of the slot's value}];$$
$$(5)\quad\textbf{the mass read:}\qquad\mathfrak M_{\mathrm{pole}}(\mathcal X)\ =\ \frac{6A\ln2}{\mathfrak h}\ +\ Z\,\Delta m_{\mathrm{EM}}\ -\ b_A\qquad[\mathrm{AT.3}(2)\text{'s ledger};\ \mathrm{BM.48}(4)\text{'s bound-system form }m_{\mathrm{pair}}=m_1+m_2+E_{\mathrm{bind}},\ E_{\mathrm{bind}}<0]:$$
$$\text{the unified read stays two-component: the count-route pole shifted by the bound-system term, the bracket untouched}\qquad[\mathrm{Def\text{-}AT.7};\ \mathrm{AT.30}];$$
$$(6)\quad\textbf{the status:}\qquad\text{derived: }(1),\ (3)\text{'s census rows},\ (4)\text{'s identity rows},\ (5);\qquad\textbf{declared: the slot }\varepsilon_{\mathrm{col}}\ \ [\mathrm{A\text{-}AT.5}],\ \text{value}\ \neg\text{issued}\ [\mathrm{P5}]:$$
$$\text{the ladder's numeric identification is identification-layer content and enters no clause [0.2c]};\qquad\neg\text{a smooth potential at any locus};\qquad\text{the collapse rates stay (P5.3)-scoped}\ [\mathrm{FT.131}(3)].$$

**Rmk (the two terms are different species).** The ensemble term is flicker: the corpus's own formed binding, re-read across the merge, where the materialization restriction $E\ge2$ becomes support-global and the shared restriction room is the gain. The brace term is lock retirement: the declared strong-side bookkeeping, denominated in defect units, counted from the cell's incidence structure alone. The per-bond ladder's variation is carried entirely by $G_A$ — geometry, not a constant bridge cost — and the two terms do not mix: one is a theorem about ensembles, the other is bookkeeping about seals, and the functional adds them because the mass read adds energies, not because the mechanisms agree.

**Req.** FT.28, FT.44(4) (Part 3, Census); Def-BM.4, BM.19(2), BM.94(4), BM.94(5), BM.137(1), BM.137(3), BM.137(4), BM.48(4), BM.48(5) (Part 4); FT.131(3) (Part 3); A-BM.9 (Part 4); Def-AT.7, Def-AT.8, Def-AT.9, AT.3(2), AT.3(5), AT.30 (this part); A-AT.5, C-AT.2 (this part); D0.4 (Part 1); P1, P5 (Parts 1–2); exact rational grids over $u$, binomial censuses, monomial identities ath; machine: `checks/verify_Atomic5.py` §P].

**Pf.**
$$
(1):\ \langle E\rangle^{(n)}_{\mathrm{mat}}=2n/D_n\ \text{[BM.137(1)]};\qquad A\,\mathcal B^{(3)}-\mathcal B^{(3A)}=6A(1/D_3-1)\tfrac{\ln2}{\mathfrak h}-6A(1/D_{3A}-1)\tfrac{\ln2}{\mathfrak h}=6A(1/D_3-1/D_{3A})\tfrac{\ln2}{\mathfrak h}\ \ \text{[machine]}
$$
$$
\text{the sign: }D_{n-1}/D_n=(1-u^{n-1})/(1-u^n)\ \text{increasing in }n\ \text{[machine: the rational grid over }u\in\{\tfrac1{20},\dots,\tfrac{19}{20}\}]\implies b^{\mathrm{ens}}_A>0\ \text{at every }u\in(0,1)
$$
$$
(2):\ G_A=\mathcal E_A+3\mathcal F_A:\ 1+0,\ 3+3,\ 6+12\ \text{[machine]};\qquad(3):\ \bar f_2=0<\bar f_3=1<\bar f_4=2\ \text{[machine]};\qquad\beta\ \text{strictly increasing at }\varepsilon_{\mathrm{col}}>0\ \text{[machine: witness substitution]}
$$
$$
(4):\ b^{\mathrm{col}}_3/b^{\mathrm{col}}_2=G_3/G_2=6,\quad b^{\mathrm{col}}_4/b^{\mathrm{col}}_2=G_4/G_2=18\ \ \text{[machine: the }\varepsilon_{\mathrm{col}}\text{-independent ratios]}
$$
$$
(5):\ \mathrm{AT.3}(2)\text{'s ledger re-cited with the bound-system term; the two-component form preserved [Def-AT.7]};\qquad(6):\ \text{assembly}.\ \blacksquare
$$

**Phys.** The binding of a nucleus splits along the corpus's own fault line. One part was already in the books: flicker, and the way a shared materialization restriction binds a merged support more than the separate ones — the meson's and baryon's ensemble effect, now read across the merge. The other part is new and deliberately minimal: when a seal is shared, the vacuum-facing obligation it retires is booked in defect units, and the count of retirements is the count of the cell's braces — one per bond, one per membrane edge. That is the whole mechanism. No potential well, no exchange mediation, no smooth curve between the rungs: a chain bond touches only vacuum, a triangle bond is braced once, a tetrahedral bond twice and the cell closes, and the per-bond ladder does nothing but read that census out loud.

---

## Tier 5.18 — The Cross-Currency Bridge and the Integration Audit

### AT.41 — The currency bridge: the exchange identity and the re-priced reduced mass

**Thm.**
$$(1)\quad\textbf{the two-reads row:}\qquad\text{one seal count, two currencies [Def-AT.8(1)]: the digon's fugacity-side floor read and its curvature-side defect read are one monomial referred to two ledgers, and no addition crosses the ledgers}\qquad[\mathrm{BM.137}(4);\ \mathrm{BM.37}(2)]:$$
$$\text{the only admitted cross-currency operation is the declared slot}\qquad[\mathrm{A\text{-}BM.9};\ \mathrm{BM.98}];$$
$$(2)\quad\textbf{the exchange identity:}\qquad\text{for any object carrying informational read }m_{\mathrm{hid}}=E_{\mathrm{int}}\ln2/\mathfrak h\ \ [\mathrm{FT.44}(4)]\ \text{and pole read }m^2_{\mathrm{pole}}=\hat\mu'^2\lambda\ \ [\mathrm{BM.137}(5)\text{'s form};\ \mathrm{Def\text{-}BM.14}(3)]:$$
$$\boxed{\ \Bigl(\frac{m_{\mathrm{pole}}}{m_{\mathrm{hid}}}\Bigr)^{\!2}\ =\ \rho_{\mathrm B}\,\frac{\lambda}{E_{\mathrm{int}}^{2}}\ }\qquad[\rho_{\mathrm B}=\hat\mu'^2\mathfrak h^2/(\ln2)^2\ \ \mathrm{A\text{-}BM.9};\ \text{machine: exact at witnesses}]:$$
$$\textbf{the exchange factor of the lepton slot is its own pole-to-floor read:}\quad\xi:=m^{\mathrm{pole}}_\ell/m^{\mathrm{fl}}_\ell,\qquad\xi^{2}=\rho_{\mathrm B}\,\frac{\lambda_\ell}{4}\ \ \text{at}\ E_\ell=2\ \ [\mathrm{AT.4}(1)]:$$
$$\text{derived — no new slot; the value of }\xi\ \text{(hence of }\rho_{\mathrm B}\lambda_\ell\text{) is}\ \neg\text{issued}\ \ [\mathrm{A\text{-}BM.9};\ \mathrm{P5}];$$
$$(3)\quad\textbf{the strict-currency row:}\qquad\text{the reduced-mass identity holds strictly inside one currency: with every slot filled at the floor read,}\qquad m_r=\frac{m_N\,m_\ell}{m_N+m_\ell},\qquad\frac1{m_r}=\frac1{m_N}+\frac1{m_\ell}$$
$$[\mathrm{AT.5}(2)\text{--}(3);\ \text{machine: the exact rational identity at witnesses}]:\qquad\text{the identity is currency-internal algebra in }(\ln2/\mathfrak h),\ \neg\text{a cross-currency token in it}\ \ \text{[machine: the witness algebra]};$$
$$(4)\quad\textbf{the re-priced row:}\qquad\text{filling the lepton slot at the exchanged read }\xi\,m_\ell\ \text{moves the reduced mass by an exact rational function of }\xi\ \text{alone:}$$
$$m^{(A,\times)}_r\ =\ \frac{m_N\,(\xi\,m_\ell)}{m_N+\xi\,m_\ell}\ =\ m^{(A)}_r\cdot\frac{\xi\,(3A+1)}{3A+\xi}\qquad[\text{count route: }m_N=3A\,m_\ell;\ \text{machine: exact rational identity in }\xi]:$$
$$E^{(\times)}_n=E_n\cdot\frac{\xi\,(3A+1)}{3A+\xi}\qquad[\mathrm{AT.6}(1)\text{'s form};\ \text{machine}]:\qquad f(\xi)=\frac{\xi(3A+1)}{3A+\xi}\ \text{strictly increasing on }\xi>0,\quad f(1)=1\ \ \text{[machine]}:$$
$$\textbf{the corpus's constructed read is the }\xi=1\text{ point; any lighter exchanged read moves the ladder down by the exact fraction }1-f(\xi)\ \text{— a spread against the constructed pole, reportable in the bracket discipline [AT.30]};$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\neg\text{a value of }\xi,\ \rho_{\mathrm B}\ \text{or}\ \lambda_\ell\ \text{issued}\ \ [\mathrm{A\text{-}BM.9};\ \mathrm{P5}]:\qquad\text{the numeric exchange readings that motivated the bridge live in the identification layer only.}$$

**Req.** FT.44(4) (Part 3, Census); Def-BM.14(3), BM.37(2), BM.69(2), BM.98, BM.111(2), BM.137(4), BM.137(5) (Part 4); A-BM.9 (Part 4); Def-AT.8, AT.4(1), AT.5(2), AT.5(3), AT.6(1), AT.30 (this part); P1, P5 (Parts 1–2); exact rational-function identities in one symbol, witness substitution ath; machine: `checks/verify_Atomic5.py` §Q].

**Pf.**
$$
(1):\ \mathrm{BM.137}(4)\text{'s separation and the slot row re-cited};\qquad(2):\ \Bigl(\tfrac{\hat\mu'\sqrt\lambda}{E\ln2/\mathfrak h}\Bigr)^{2}=\tfrac{\hat\mu'^2\lambda\mathfrak h^2}{E^2(\ln2)^2}=\rho_{\mathrm B}\tfrac{\lambda}{E^2}\ \ \text{[machine: the two forms one identity, at witnesses]}
$$
$$
(3):\ \tfrac1{m_r}=\tfrac{m_N+m_\ell}{m_Nm_\ell}=\tfrac1{m_N}+\tfrac1{m_\ell}\ \ \text{[machine: exact at witnesses; the token census: }\ln2/\mathfrak h\text{-terms only]}
$$
$$
(4):\ m_N=3A\,m_\ell\ \text{[count route]}\implies m^{(A,\times)}_r=\tfrac{3A\,\xi\,m_\ell}{3A+\xi}=\tfrac{3A\,m_\ell}{3A+1}\cdot\tfrac{\xi(3A+1)}{3A+\xi}\ \ \text{[machine: cleared in the symbol ring]};\qquad f'(\xi)=\tfrac{3A(3A+1)}{(3A+\xi)^2}>0,\ f(1)=1\ \ \text{[machine]};\qquad(5):\ \text{assembly}.\ \blacksquare
$$

**Phys.** The bridge the corpus declared in Part 4 as a slot turns out to be an identity waiting for two reads of one object. Divide the pole read by the informational read and the package $\hat\mu'^2\mathfrak h^2/(\ln2)^2$ falls out on its own — the slot's exact form, derived rather than fitted, with the object's own census supplying the only model-dependent factor. Fill the lepton slot at the floor read and the reduced-mass identity is strict, internal, and already machine-green; fill it at the exchanged read and the whole ladder shifts by one exact rational function of the exchange factor, which equals one at the corpus's own read and dips below it exactly when the exchanged read is lighter. Nothing is added to the register and nothing is measured; the bridge is the shape of the movement, not a number in it.

### AT.42 — The integration audit: the substrate, the intact bridges, and the era-locality addition

**Thm.**
$$(1)\quad\textbf{the substrate row:}\qquad\text{the enumerative substrate is unchanged — the 25 cells, consumed by tag citation [AT.18(1),(3)] — and the collapse consumes the same families at new counts:}$$
$$\begin{array}{l|l}\text{census family} & \text{consumption at the collapse extension}\\\hline\text{floor cards and ladders} & \text{the digon floor as the defect unit [FT.28]; the }E_{\mathrm{int}}\text{ ladder as the widths [FT.42--FT.45]; the junction phase classes as the interface's δ-class [FT.35(3), FT.49(3)]}\\\hline\text{loop and cover classes} & \text{the flicker pools behind the ensemble merge term [FT.64, FT.65, FT.69]}\\\hline\text{pole and mass multiplets} & \text{the pole-side ceilings the merged core inherits [FT.76]}\\\hline\text{form-factor tables} & \text{the merged skeletons' size-bound rows [FT.98, FT.99]}\\\hline\text{audit ledgers} & \text{the read-species taxonomy separating the defect ledger [FT.81, FT.83, FT.84, FT.114, FT.120]}\\\hline\text{topology-blind cells} & \text{the merged supports' regulated graph pool [FT.105]}\end{array}$$
$$11+5+1+2+5+1=25\qquad[\text{machine: the partition re-run; no cell added}];$$
$$(2)\quad\textbf{the intact-bridge row:}\qquad\text{the EM sealing grammar stands unmodified — the collapse is the strong-side channel and adds no EM row}\qquad[\mathrm{A\text{-}AT.1};\ \mathrm{AT.23}\text{--}\mathrm{AT.24}]:$$
$$\text{the scope clock stands — the collapse adds no clock row; its gate is an envelope condition}\qquad[\mathrm{AT.29};\ \mathrm{Def\text{-}BM.4}(5)]:$$
$$\text{the unified mass read stands — the merged core's read is the two-component form with the count-route pole shifted by the bound-system term}\qquad[\mathrm{Def\text{-}AT.7};\ \mathrm{AT.40}(5)]:$$
$$\text{the width ledger absorbs the released energy as bracket content; no new bracket law}\qquad[\mathrm{AT.30}];$$
$$(3)\quad\textbf{the era-locality addition:}\qquad\text{the binding bar joins the table at its own locus, one row, same discipline [AT.36's pattern]:}$$
$$\begin{array}{l|l|l|l}\text{obstruction} & \text{binds in} & \text{the bridge} & \text{status}\\\hline\text{no binding read on any member [BM.48(4); AT.3(5)]} & \text{the free members' masses} & \text{the constructed merged support [Def-AT.9; AT.40(5)]} & \text{re-scoped: the free-member rows stand; the collapsed support carries its own read}\end{array}$$
$$(4)\quad\textbf{the conservation row:}\qquad A\,M(1,Z\text{-class})\ =\ \mathfrak M_{\mathrm{pole}}(\mathcal X)\ +\ b_A\qquad\text{exactly, on the count route}\qquad[\mathrm{AT.40}(5);\ \text{machine: the identity at witnesses}]:$$
$$\neg\text{a term of }b_A\text{ attaches to any free member}\qquad[\mathrm{BM.48}(4),(5)\ \text{re-cited}];$$
$$(5)\quad\textbf{the calibration consolidation:}\qquad\text{the extension adds one declared dimensionless slot and one symbolic-use log row [A-AT.5; C-AT.2]},\ \neg\text{a dimensionful scale [P1]},\ \neg\text{a P4 member [P4]},\ \neg\text{a measured value [P5]};$$
$$\text{the nucleon-side calibration form of AT.38(5) is recorded, value}\ \neg\text{issued};$$
$$(6)\quad\textbf{the status:}\qquad\text{derived and recorded; machine: }`\text{checks/verify\_Atomic5.py}`\ \S\mathrm{Q}].$$

**Req.** FT.28, FT.35(3), FT.42–FT.45, FT.49(3), FT.64, FT.65, FT.69, FT.76, FT.81, FT.83, FT.84, FT.98, FT.99, FT.105, FT.114, FT.120 (Part 3, Census); Def-BM.4(5), BM.48(4), BM.48(5) (Part 4); Def-AT.1, Def-AT.7, AT.3(5), AT.18, AT.23, AT.24, AT.29, AT.30, AT.36, AT.40, AT.41 (this part); A-AT.1, A-AT.5, C-AT.2 (this part); P1, P4, P5 (Parts 1–2); exact set arithmetic, witness identities ath; machine: `checks/verify_Atomic5.py` §Q].

**Pf.**
$$
(1):\ \text{the consumption map re-run over the six families; }11+5+1+2+5+1=25\ \text{[machine: the partition arithmetic]};\qquad(2):\ \text{the four bridge rows re-cited at their loci}
$$
$$
(3):\ \text{the table row [AT.36's four-column discipline]};\qquad(4):\ \mathfrak M_{\mathrm{pole}}(\mathcal X)+b_A=6A\ln2/\mathfrak h+Z\Delta m_{\mathrm{EM}}=A\,M(1)\ \text{at witnesses [machine]}
$$
$$
(5):\ \text{the register record [A-AT.5; C-AT.2; P1; P4; P5]};\qquad(6):\ \text{assembly}.\ \blacksquare
$$

**Phys.** The audit closes the way the era's audits close: nothing outside the books. The same twenty-five spaces feed the new channel — the digon once more, now as the defect's denomination; the flicker pools once more, now across a merge; the graph census once more, now regulating skeletons with two, three and four sealed cores — and the partition still closes at twenty-five. The three bridges the extension tiers built pass through untouched, because the collapse touches none of them: it gates on an envelope, reads a census, and books a bound-system term into a mass ledger that already knew how to hold one. What changes is one table row: the bar that kept binding off every member keeps it off the free members still, and the merged support now carries what the bar always said a constructed bound system may carry — its own read.

---

## Closure exports of the collapse extension (Tiers 5.16–5.18; consumed by no part of the canon)

$$
\begin{array}{c|c}
\text{export} & \text{the row}\\\hline
\text{the defect unit} & \mathfrak m_{[2]}\,\mathfrak h=2\ln2;\qquad\mathfrak m_{[2]}:m^{(1)}_{\mathrm{hid}}=1:3\ \text{(calibration-free)}\ [\mathrm{AT.38}]\\
\text{the weak-balance unit} & \text{one digon per reconfigured junction; the balance's slot at the floor read}\ [\mathrm{AT.38}(3)]\\
\text{the interface class} & 2\in2\mathbb Z\setminus4\mathbb Z;\qquad m^{\mathrm{meson}}_{\mathrm{hid}}\big|_{E_{\mathrm{int}}(c)=2}=2\,\mathfrak m_{[2]}\ [\mathrm{AT.39}]\\
\text{the collapse gate} & d<2\,\Delta x^{\mathrm B}_{\mathrm N}=\mathfrak h/(3\ln2),\ \text{sub-hop, chart-side}\ [\mathrm{Def\text{-}AT.9}(1)]\\
\text{the census table} & (\mathcal E_A,\mathcal F_A,\eta_A,G_A)=(1,0,1,1),\ (3,1,1,6),\ (6,4,2,18);\quad\text{closure iff }A=4\ [\mathrm{Def\text{-}AT.9};\ \mathrm{AT.40}]\\
\text{the functional} & b_A=6A\bigl(\tfrac1{D_3}-\tfrac1{D_{3A}}\bigr)\tfrac{\ln2}{\mathfrak h}+\varepsilon_{\mathrm{col}}\,(\mathcal E_A+3\mathcal F_A)\,\mathfrak m_{[2]};\quad\text{per-bond ladder geometry-driven}\ [\mathrm{AT.40}]\\
\text{the exchange identity} & (m_{\mathrm{pole}}/m_{\mathrm{hid}})^{2}=\rho_{\mathrm B}\,\lambda/E_{\mathrm{int}}^{2};\qquad\xi^{2}=\rho_{\mathrm B}\,\lambda_\ell/4\ \ [\mathrm{AT.41}]\\
\text{the re-priced reduced mass} & m^{(A,\times)}_r=m^{(A)}_r\cdot\xi(3A+1)/(3A+\xi);\qquad E^{(\times)}_n=E_n\cdot\xi(3A+1)/(3A+\xi)\ [\mathrm{AT.41}]\\
\text{the era-locality addition} & \text{the binding bar re-scoped at the merged support; the free-member rows stand}\ [\mathrm{AT.42}(3)]
\end{array}
$$

## Observation charter (Tiers 5.19–5.23): the Observation Layer — the 4-Hop Causal Bound, the Locked and Connected Atom, the Transition Defect, the Seal-Configuration Ladder, and the Weighing Bar

**0.1d Charter of the observation extension.** The observation extension continues the atomic era — incrementally, inside this part, with no new era declared — into the layer of the observation channel: the causal-capacity arithmetic the channel runs on, the two reads of the constructed atom (locked and connected), the transition defect between them, the seal-configuration ladder the "orbital" names, the bar that keeps the defect from decomposing, and the Koide-row adjudication the seal bilinear forces. Its foundation stack, by citation: (i) the pair canon [A1; A2; C9; C10; D0.9; CT0.5; CT0.6; CT0.6a; CT0.9]: the register supply, its Shannon conversion, and the hop capacity; (ii) the Janus events and the tick [D1.2; D1.8; D1.9; CT0.3; FT.108(1)]: one seal event's exact bookkeeping and the forward-only ledger; (iii) the observer channel [Def-H.3; FT.1; FT.36(1),(2); FT.38(1); EM.5–EM.7]: the extractable-information sup, its attainment at capacity, and the forced carrier; (iv) the constructed bound channel and its reads [Def-AT.4–Def-AT.7; AT.5–AT.8; AT.21–AT.31]: the pole ladder, the masked-force census, the locally locked rest slice, the width bracket; (v) the defect and currency rows [Def-AT.8; AT.38–AT.41]: the 2-edge defect, the currency pair, the exchange identity, the re-priced reduced mass; (vi) the flicker laws [D0.4; BM.19(2), BM.19(3); BM.23(8), BM.23(9); BM.44(1); BM.122(3); BM.123(1), BM.123(2); BM.137(1)]: the gate, the round-trip weight, the ensemble residue; (vii) the incommensurability and bridge rows [BM.37(2); BM.48(4), BM.48(5); BM.69(4), BM.69(5); BM.83; A-BM.9; BM.98]; (viii) the seal bilinear and its spectrum [FT.109(3); FT.110(1); FT.111; FT.112; FT.113; FT.158; Def-H.41]: the $C_3$-covariant spectrum, the angle $\delta_\ell=\tfrac29$, the undeclared scale. Its outputs: the capacity adjudication and the Janus-cone row (Tier 5.19); the locked and connected reads with the transition defect (Tier 5.20); the seal-configuration ladder and the flicker gate (Tier 5.21); the weighing bar and the Koide row (Tier 5.22); the integration audit (Tier 5.23). Its enumerative substrate remains the Census block: the 25 cells, consumed by tag citation and extended by no new cell [AT.18(1), AT.18(3)]. The charter adds no declared slot, no declaration, no dimensionful scale, and no P4 member [P1; P4; §Cal-5d].

**0.2d Standing bars of the observation extension.** No particle identification enters any row: the generator-layer names *electron*, *proton*, *hydrogen* stay in the identification layers already logged [A-AT.2; A-AT.4], and the transition defect carries a notation row of its own — the defect read is $\mathfrak d_n$ and nothing else; the lepton-floor symbol keeps its published meaning at its own rows [AT.4; Def-AT.8(2)'s pattern], and no row of this extension writes the external mass symbol $m_e$ in any **Thm** clause [P5]. No measured value attaches to the defect read, the capacity rows, the configuration ladder or the Koide-form spectrum [P5]; the generator-layer numeric readings that motivated the tier — any energy-unit figure for the defect, for the floor, for the exchange — live in the identification layer only and enter no **Thm** clause [0.2c's discipline, extended]. No Schrödinger equation, no spacetime stage supplied from outside the ledger, no smooth-manifold light cone: the cone rows are ledger-side bookkeeping [D1.9; D1.8: $x^0=\tau_n$], and the "orbital" rows are pole reads [AT.23], ¬ trajectories. Amplitude $\ne$ mass [FT.79(5)]; rung $\ne$ scale [D0.8]; the bracket discipline: a spread is an inequality, never a value [§0.2b]; the chart-side rows carry their conditionality explicitly [BM.10(3)].

---

## §Cal-5d — Free internal parameters of the observation extension (P4-class)

**None introduced by this extension; none inherited beyond the standing registers.** Inherited and undeclared: the single dimensionful scale $\mathfrak h$ [P1]; the fermion-era registry Cal-F (the family-channel scales $\mu$, $\mu_\nu$ among its slots) [Cal-F; FT.113(3); FT.143(3)]; the baryomesonic register [Cal-BM]: the bridge ratio slot $\rho_{\mathrm B}$ [A-BM.9, value $\neg$issued], the electric-coupling slot $e_0$ [C-BM.2, value $\neg$issued], the channel-scale rows [C-BM.3]; the atomic symbolic-use logs [C-AT.1; C-AT.2]. The observation extension issues **no** new slot: every new row is an exact rational or monomial form in $(\mathfrak h,\ln2,e,c,\varepsilon_q,\xi,\rho_{\mathrm B})$ over the integer counters $(A,Z,n,\delta h,\delta\tau,\tau_n)$, and the two logs stand unextended:

$$(\mathrm{C\text{-}AT.3})\quad\textbf{the log consolidation (record, } \neg\textbf{addition):}\qquad \mathrm{C\text{-}AT.1}\ \text{and}\ \mathrm{C\text{-}AT.2}\ \text{stand verbatim; the observation tiers use}\ e\ \text{and}\ \varepsilon_{\mathrm{col}}\ \text{symbolically and issue no value}\ [\mathrm{P5}].$$

No second dimensionful scale exists [P1]; $\varepsilon_q$ remains the A4 datum, ¬a parameter [D0.4]; $\xi$ remains the derived exchange factor of AT.41(2), ¬a slot.

---

## §A-AT (observation extension) — Logged declarations: none (record)

**No declaration is issued.** The extension's new objects are all reads on constructed structures: the locked and connected reads are read-side configurations of the bound channel [Def-AT.6] under the observer channel the corpus already owns [Def-H.3; FT.1]; the transition defect is the bracket movement the width ledger already prices [AT.30]; the seal-configuration ladder is the pole ladder re-read [AT.23]; the Koide row is the seal bilinear's own spectrum [FT.111–FT.113]. The declaration discipline of A-AT.1/A-AT.5 is therefore not triggered: no constitutive grammar is missing from the inventory, and the charter's outputs are theorems about declared and derived structures, from prior tags and exact-arithmetic steps alone. Everything Tiers 5.19–5.23 prove is machine-checked in `checks/verify_Atomic5.py` §R–§V.

---

## Tier 5.19 — The Causal Capacity Layer: the 4-Hop Bound and the Janus Cone

### AT.43 — The hop-capacity derivation: the number 4 derived and the candidates adjudicated

**Thm.**
$$(1)\quad\textbf{the derivation (the capacity chain, exact):}\qquad C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathcal H_p\otimes\mathcal H_q)=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=4^2=16\qquad[\mathrm{D0.9};\ \mathrm{A1};\ \mathrm{A2};\ \mathrm{CT0.6};\ \text{machine: the dimension census}]:$$
$$\mathrm{C10}:\ 16\ \text{directions}\iff|X|\le16\ \text{alternatives}\iff\log_2|X|\le4\ \text{bits per channel crossing};\qquad\mathrm{CT0.9}+\mathrm{C9}:\ 1\ \text{real edge}=1\ \text{bit}=\ln2\ \text{nats}:$$
$$\boxed{\ \delta h(\gamma)\ \le\ 4\,\delta\tau(\gamma),\qquad\mathsf E(\gamma)\ \le\ \min\bigl(\delta h,\ 4\,\delta\tau\bigr)\ln2\ \ \text{nats}\ }\qquad[\mathrm{CT0.6a};\ \text{machine: }2^4=16]:$$
$$\textbf{the capacity rule is exactly 4 hops per 1 tick, and the 4 is the Shannon content of the pair arena's real register supply — derived, } \neg\textbf{declared};$$
$$(2)\quad\textbf{the decomposition row:}\qquad 4=\log_2C_{\mathrm{cap}}=\log_2(4^2)=2\cdot\log_2\bigl(\dim_{\mathbb R}\mathfrak H(\mathbb C^2)\bigr)=2\cdot2\qquad[\text{machine: }\dim_{\mathbb R}\mathfrak H(\mathbb C^2)=4]:$$
$$\text{one factor 2 is the qubit's two complex amplitudes (the Hermitian square), one factor 2 is the pair structure [A2] — the channel is a pair channel, and the two member slots each supply 4 register directions};$$
$$(3)\quad\textbf{the candidate adjudication (the Architect's three):}$$
$$\begin{array}{l|l}\text{candidate} & \text{verdict}\\\hline\text{the arena }\mathbb C^4\ \ [\mathrm{A1};\ \mathrm{A2}] & \textbf{confirmed as the operative input: }C_{\mathrm{cap}}=\dim_{\mathbb R}\mathfrak H(\mathbb C^4)\ \text{with}\ \mathbb C^4=\mathcal H_p\otimes\mathcal H_q\ \text{the pair arena; the 4-hop count is its Shannon content}\\\hline\text{the force-operator aspects} & \textbf{refuted as the source: the hop bound is channel-side (register supply at a crossing [D0.9; CT0.6]), the force blocks are vertex-side [A8]};\\ & \text{the aspect list }(J_\pm,W,C,H)\ \text{is}\ \neg\text{the corpus's block list [A8: }G,H,D^\pm,W^\pm,Z,J^\pm,\mathrm{EM},\mathrm{strong}\text{]; AT.21(2)'s census shows the blocks silent on the bound channel while the jaw binds}\\\hline\text{the tetrahedral coordination} & \textbf{refuted at this layer: the tetrahedron enters at the collapse closure (volume closure iff }A=4\ [\mathrm{Def\text{-}AT.9}(3)])\ \text{— support-side counts,}\ \neg\text{channel-side capacities};\\ & \text{the coincidence }4=4\ \text{is recorded as a cross-check, } \neg\text{a derivation [FT.112's Rmk discipline]}\end{array}$$
$$(4)\quad\textbf{the completeness row (the obstruction question):}\qquad\boxed{\ \textbf{no additional structure is required: the chain (1) consumes A1, A2 and the Part-1 conventions (C9, C10, CT0.9, D0.9) alone}\ }\qquad[\text{machine: the citation census}]:$$
$$\neg\exists\ \text{an obstruction; the 4 is derivable from A1--A7 with the standing conventions, and nothing else};$$
$$(5)\quad\textbf{the round-trip row (the }C_{\mathrm{cap}}=4^2\textbf{ gloss adjudicated):}\qquad\textbf{confirmed as an identity, refuted as a mechanism:}\qquad C_{\mathrm{cap}}=4^2\ \text{because the two factors are the pair slots}\ \mathcal H_p,\mathcal H_q\qquad[\mathrm{A2};\ \mathrm{D0.9}]:$$
$$\text{the corpus's round-trip object is a weight, }\neg\text{a capacity:}\qquad\mathcal W_{\mathrm{round}}=x_+x_-=4\varepsilon_q(1-4\varepsilon_q)=\tfrac14-16\Bigl(\varepsilon_q-\tfrac18\Bigr)^{\!2}\le\tfrac14\qquad[\mathrm{BM.44}(1);\ \mathrm{BM.122}(3);\ \mathrm{BM.123}(1),\ \mathrm{BM.123}(2);\ \text{machine}]:$$
$$\neg\exists\ \text{a cone-traversal ("radar") object in the capacity's derivation [token census]};\qquad\text{the bidirectional-channel balance }\ln4=2\ln2\ [\mathrm{BM.35}]\ \text{is an entropy row, }\neg\text{this one};$$
$$(6)\quad\textbf{the attainment:}\qquad\text{the bound is reached, not merely valid: photon schedules at capacity, per-tick groups of }\le4\qquad[\mathrm{FT.36}(2);\ \mathrm{EM.5};\ \mathrm{EM.6};\ \mathrm{EM.7}]:$$
$$\text{channel speed}=4\ \text{hop lengths per tick, a conformal invariant}\qquad[\mathrm{FT.36}(1)]:\qquad\text{the same four is the bit capacity and the speed — one number on two loci};$$
$$(7)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(6);\qquad\neg\text{a new parameter},\ \neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]:\qquad\textbf{"why 4" is answered: the pair arena's register capacity, in bits.}$$

**Rmk (the two readings of $\mathbb C^4$).** The arena $\mathbb C^4$ admits two decompositions — one four-dimensional object, or two two-dimensional slots — and the capacity is the same under both ($\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=16$ either way; $\mathfrak H(\mathbb C^4)\cong\mathfrak H(\mathbb C^2)\otimes\mathfrak H(\mathbb C^2)$ as real vector spaces [math]). The corpus's own reading is the pair one [A2; D0.9's $\mathfrak H(\mathcal H_p\otimes\mathcal H_q)$], and the decomposition row (2) is stated in it; nothing in the adjudication depends on the choice.

**Req.** A1, A2, A8, C9, C10, D0.5, D0.6, D0.9, CT0.6, CT0.6a, CT0.9 (Part 1); CT2.1 (Part 2); EM.5, EM.6, EM.7 (Part 2); FT.36(1), FT.36(2) (Part 3); BM.35, BM.44(1), BM.122(3), BM.123(1), BM.123(2) (Part 4); Def-AT.9(3), AT.21(2) (this part); P1, P5 (Parts 1–2); the real-dimension census of Hermitian spaces, exact binary capacity arithmetic, the rational parabola census, token censuses [math; machine: `checks/verify_Atomic5.py` §R].

**Pf.**
$$
(1):\ \dim_{\mathbb R}\mathfrak H(\mathbb C^n)=n^2\ \text{at}\ n=2,4\ \text{[machine: the basis counts 4 and 16]};\qquad2^4=16\ \text{[machine]};\qquad\mathrm{CT0.6a}\text{'s jaw at the hop-bit conversion [CT0.9; C10; C9]}
$$
$$
(2):\ \log_2 16=4=2+2\ \text{[machine]};\qquad(3):\ \text{the verdict table against A8's block list and Def-AT.9(3)'s closure row [machine: the token and census rows]}
$$
$$
(4):\ \text{the citation census of the chain: A1, A2, C9, C10, CT0.9, D0.9 — all Part-1 canon [machine]};\qquad(5):\ \tfrac14-16(\varepsilon_q-\tfrac18)^2=4\varepsilon_q(1-4\varepsilon_q)\ \text{[machine: the SOS identity on the rational grid]};\ \sup=\tfrac14\ne16\ \text{[machine]}
$$
$$
(6):\ \mathrm{FT.36}(1),(2)\text{'s attainment rows re-cited};\qquad(7):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The question "why four hops to the tick" was answerable the moment the register supply was: one channel crossing presents sixteen real directions, sixteen directions distinguish sixteen alternatives, sixteen alternatives is four bits, four bits is four edges — and every equality in that chain is a census, not a convention. Of the three candidate sources, only the arena survives, and it survives in a specific form: not "the arena has four complex dimensions" as a numeral, but the pair structure that squares the single qubit's four real directions into sixteen and hands the square root back when the Shannon conversion runs backwards. The force-operator guess fails on locus, not on value — its blocks act at vertices while the jaw binds at crossings — and the tetrahedron fails on layer: it counts bonds of a collapsed support, not registers of a channel, and the corpus has a disciplined shelf for numerical coincidences. The round trip is real bookkeeping, but it books weights, and no weight is sixteen. What the derivation adds to the standing jaw is the reading: the speed of light in this ledger is the bit-rate of the only channel there is, attained by photon schedules and invertible to four hop-lengths per tick.

### AT.44 — The Janus cone: one seal event's causal bookkeeping

**Thm.**
$$(1)\quad\textbf{the event row:}\qquad J^\pm:\ (\Delta n_{\mathcal R},\ \delta h,\ \delta\tau)=(\pm1,\pm1,\pm1)\qquad[\mathrm{CT0.3};\ \text{machine: the sign census of }\{\pm1\}^3]:$$
$$\text{the generator-layer reading "one tick = one }J^\pm\text{ event" adjudicated: admissible as the single-pair bookkeeping identity — at a seal event the tick count, the hop count and the register count move together, } \neg\text{as an identification of the tick with the event class: the ledger's ticks count all retained updates [D0.7], and }J^\pm\text{ is one species of them [D1.2]};$$
$$(2)\quad\textbf{the cone row:}\qquad\text{the immediate future cone of one seal event: tick locality closes the sides — }\operatorname{dom}(\mathrm{tick}(v))\subseteq\{v\}\cup\{e\ni v\},\ \neg\exists\ \text{a read at edge-distance}>1\qquad[\mathrm{D1.9}]:$$
$$\text{the forward-only constraint closes the past: }\neg\exists\,\tau^{-1}\qquad[\mathrm{A6};\ \mathrm{L2}]:$$
$$\boxed{\ \text{the maximum spatial hops admissible in the immediate future cone of one seal event is exactly }4\ }\qquad[\mathrm{CT0.6a}\ \text{at }\delta\tau=1;\ \text{machine}]:$$
$$\textbf{a ledger-side cone: locality and irreversibility rows on the graph, } \neg\textbf{a smooth-manifold light cone, } \neg\textbf{a spacetime stage [D1.8: }x^0=\tau_n\textbf{]};$$
$$(3)\quad\textbf{the chiral row:}\qquad\text{the cone's bookkeeping is chirality-carried: the }J^\pm\text{ moves are }S\text{-odd, }\{\mathbb S,J_\pm\}=0\qquad[\mathrm{FT.108}(1);\ \mathrm{CT0.7}(3)]:$$
$$\text{and chirality-blind in the count: the jaw counts registers, not orientations [C10]; the binary phase }\Phi=\{0,\pi\}\ [\mathrm{D0.5};\ \mathrm{CT0.9}]\ \text{is the only chiral input the count consumes};$$
$$(4)\quad\textbf{the capacity tie-in:}\qquad D_{\mathrm{tick}}(3)=2^4=16=C_{\mathrm{cap}}:\ \text{the rung-3 vertex exactly saturates the one-tick cone's budget}\qquad[\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT0.11};\ \text{machine}]:$$
$$O(4)=2^5-16=16:\ \text{rung 4 over-subscribes by exactly one channel quantum — the vertex-side mirror of the channel-side jaw}\qquad[\mathrm{CT4.1};\ \text{machine}];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\neg\text{a new causal postulate: the cone is D1.9's locality row and CT0.6a's jaw, both already in the canon};\qquad\neg\text{a spacetime stage}\ [\mathrm{D1.8}].$$

**Req.** A6, L2, C10, D0.5, D0.7, D1.2, D1.8, D1.9, CT0.3, CT0.5, CT0.6, CT0.6a, CT0.7(3), CT0.9, CT0.11, CT4.1 (Part 1); FT.108(1) (Part 3); P1, P5 (Parts 1–2); exact integer sign censuses, the rung ladder [math; machine: `checks/verify_Atomic5.py` §R].

**Pf.**
$$
(1):\ \text{the seal increments re-cited; the sign census: of the }8\text{ elements of }\{\pm1\}^3,\ \text{exactly 2 carry the sign-lock }(\pm1,\pm1,\pm1)\ \text{[machine]};\qquad(2):\ \mathrm{D1.9}\text{'s locality and A6/L2's irreversibility re-cited}
$$
$$
\delta\tau=1:\ \delta h\le4\cdot1=4\ \text{[machine]};\qquad\text{sharpness: }4\ \text{hops in one tick present }2^4=16=C_{\mathrm{cap}}\ \text{alternatives — at capacity [CT0.6a's sharpness clause; machine]};\qquad5\ \text{hops: }2^5=32>16\ \text{[machine: oversubscribed]}
$$
$$
(3):\ \mathrm{FT.108}(1)\text{'s }S\text{-oddness and CT0.7(3)'s anticommutation re-cited};\ \text{the count's blindness: C10's register accounting has no orientation variable [machine: the token census]};\qquad(4):\ 2^4=16,\ 2^5-16=16\ \text{[machine]}
$$
$$
(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** One seal event moves exactly three counters by exactly one — and that tiny rigid step, boxed by tick locality on the sides and the irreversibility of the tick behind it, leaves exactly four hops of room in front. The cone the corpus thereby owns is not a geometric object with a light cone's family resemblance; it is two rows the canon has carried since the qubit era — a vertex may read only itself and its own edges, and no tick has an inverse — plus the channel jaw at unit tick depth. The chiral structure of the substrate is present (the moves anticommute with the swap grading), but the count never consults it: sixteen registers do not care which way they face. Rung three fills the one-tick cone exactly; rung four bursts it by one quantum; and the same integer sixteen appears on both sides of the mirror, vertex supply and channel supply, which is why the capacity layer and the saturation layer were always the same wall seen from two rooms.

---

## Tier 5.20 — The Locked and the Connected Atom: the Observation Bridge and the Transition Defect

### Def-AT.10 — The locked and connected reads of the constructed atom

**Def.** Let the constructed EM-pair composite at level $n$ of class $(A,Z)$ be given [Def-AT.4; Def-AT.6].
$$(1)\quad\textbf{the locked read:}\qquad\mathfrak M^{\mathrm{lock}}_n(A,Z)\ :=\ \text{the bound channel's stationary read with the observer channel closed:}\qquad\mathfrak M^{\mathrm{lock}}_n\ =\ \mathfrak M_n(A,Z)\ =\ M(A,Z)+m_\ell+E_n^{(A,Z)}\qquad[\mathrm{Def\text{-}AT.7}(1)]:$$
$$\text{the pole, with its spread component at the register's own floor: }\Delta E_n\ \ge\ \tfrac16\ \text{in the chart's energy currency}\qquad[\mathrm{AT.30}(2),\ \mathrm{AT.30}(3)\ \text{at the tick floor }\tau=3];$$
$$(2)\quad\textbf{the connected read:}\qquad\mathfrak M^{\mathrm{con}}_n(A,Z)\ :=\ \text{the same stationary read with the observer channel open: an external subnetwork's transit chain }\gamma\ \text{registers through the pair channel at the bound locus}\qquad[\mathrm{Def\text{-}H.3};\ \mathrm{FT.1}(1)]:$$
$$\mathfrak M^{\mathrm{con}}_n\ =\ \mathfrak M_n(A,Z)\ \text{with the spread component probed at tick count }\tau_n\ge3:\qquad\bigl[\ 1/(2\tau_n),\ |E_n|\ \bigr]\qquad[\mathrm{AT.30}(3)],$$
$$\text{plus the channel's booked transit content }\mathsf E_{\mathrm{tr}}(\gamma)\le\min(\delta h,\,4\,\delta\tau)\ln2\qquad[\mathrm{CT0.6a};\ \mathrm{EM.7}]\ —\ \text{a separate ledger from the energy bookkeeping [AT.14(3); C10]};$$
$$(3)\quad\textbf{the transition defect read:}\qquad\boxed{\ \mathfrak d_n\ :=\ \tfrac16-\frac{1}{2\tau_n}\ \ge\ 0\ }\qquad[\text{machine: the bracket endpoints on the tick grid}]:$$
$$\text{the resolution the connection buys, in the chart's energy currency — a spread movement, }\neg\text{a value [the bracket discipline]};$$
$$(4)\quad\textbf{the notation row:}\qquad\text{the defect read is }\mathfrak d_n\ \text{and nothing else; the lepton-floor symbol keeps its published meaning at its own rows [AT.4; Def-AT.8(2)]};\qquad\neg\exists\ \text{a row of this extension writing the external symbol }m_e\ [\mathrm{P5}];$$
$$(5)\quad\textbf{the scope:}\qquad\text{chart-side under BM.10(3)'s scope and A-AT.3's stationarity scope; both reads are reads: }\neg\text{a new state of matter, }\neg\text{a dynamics, }\neg\text{a collapse postulate}.$$

### AT.45 — The locked state: the seal inventory of the register-closed atom

**Thm.**
$$(1)\quad\textbf{the single-configuration row:}\qquad\text{the locked atom is one self-contained configuration: the bound channel's read is the pole ladder at }m_r\ \ [\mathrm{Def\text{-}AT.6};\ \mathrm{AT.23}];\ \text{the members keep their own colour seals [Def-AT.4}(2)\,\mathrm{(ii)}];\ \text{the exterior flux vanishes identically}\qquad[\mathrm{AT.7}(1)]:$$
$$\boxed{\ \neg\exists\ \text{a constituent orbiting a constituent: the only motion the locked read carries is the canonical pair's phase orbit [AT.23(1)], } \neg\text{a trajectory}\ }\qquad[\mathrm{BM.10}(1)\text{'s register bar at its locus}];$$
$$(2)\quad\textbf{the }\varepsilon\textbf{-seal row:}\qquad\text{the baryon core is the }\varepsilon\text{-sealed 3-juncture of the unit charge class}\qquad[\mathrm{BM.26}(1);\ \mathrm{D3.9};\ \text{Census FT.35}(5)]:$$
$$\text{its saturation is locked at the sealed }\varepsilon\text{-junctures [D4.1; CT4.1]; the pair junction adds no new block: }\Delta E_{D^-}=0\ \text{across the binding}\qquad[\mathrm{AT.22}(2)]:\qquad\textbf{the locked register is the inherited cap, } \neg\textbf{a new lock};$$
$$(3)\quad\textbf{the lepton-in-the-seal row:}\qquad\text{the lepton is part of the seal structure: its floor read }m_\ell\,\mathfrak h=2\ln2\ \text{is the seal count of the minimal closed chain — a bound object by kind}\qquad[\mathrm{AT.4}(1);\ \mathrm{FT.28};\ \mathrm{D1.5}]:$$
$$\text{the locked read's rest slice }M(A,Z)+m_\ell\ \text{is therefore wholly seal-count content: the count route }6A\ \text{plus the digon's }2\qquad[\mathrm{AT.3}(1);\ \text{machine: }6A+2\ \text{at witnesses}];$$
$$(4)\quad\textbf{the rest-plus-kinetic assembly (the cited formula adjudicated):}\qquad\text{the corpus's total-energy read is the Eulerian form }E=N\sqrt{m^2_{\mathrm{rest}}+\gamma^{ij}p_ip_j}-N^ip_i\qquad[\mathrm{Def\text{-}BM.10}(5);\ \mathrm{BM.34}(4)]:$$
$$\textbf{NR: }E_{\mathrm{total}}=m_{\mathrm{rest}}+\mathrm{KE}=m_{\mathrm{rest}}+\frac{N\,\gamma^{ij}p_ip_j}{2m}+O(p^4),\qquad m_{\mathrm{rest}}=\frac{\Delta S_{\mathfrak L}}{\mathfrak h}=m_{\mathrm{hid}}\qquad[\mathrm{BM.35}(4);\ \text{machine: the series identity at witnesses}]:$$
$$\text{the generator-layer tag "RK-12" is }\neg\text{a corpus tag [token census]; the formula's structure is Def-BM.10(5)+BM.35's, with the shift's published sign }-N^ip_i\ \text{[the defect rows below are invariant under the sign convention, both states carrying the same one [machine]]};$$
$$\text{at the pole: the virial split books the kinetic share inside the pole read: }\langle\mathrm{KE}\rangle_n=|E_n|,\quad\langle V\rangle_n=2E_n,\quad\langle\mathrm{KE}\rangle_n+\langle V\rangle_n=E_n\qquad[\mathrm{AT.26}(2);\ \mathrm{AT.8}(4);\ \text{machine: the }n\text{-grid}];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived as a read on constructed objects; the "locked" name is bookkeeping [A §0.2]};\qquad\neg\text{a measured lock, }\neg\text{a comparison}\ [\mathrm{P5}].$$

**Req.** A §0.2, BM.10(1), BM.10(3), BM.34(4), BM.35(4), Def-BM.10(5), BM.26(1), BM.48(2) (Part 4); Census FT.35(5) (row-wise); D1.5, D3.9, D4.1, CT4.1 (Parts 1–2); FT.28, FT.44(4) (Part 3, Census); Def-AT.4, Def-AT.6, Def-AT.7, AT.3(1), AT.4(1), AT.7(1), AT.8(4), AT.21, AT.22(2), AT.23, AT.26(2), AT.30(2), AT.30(3) (this part); P1, P5 (Parts 1–2); exact rational witness identities, the Laurent series at witnesses, token censuses [math; machine: `checks/verify_Atomic5.py` §S].

**Pf.**
$$
(1):\ \mathrm{Def\text{-}AT.4}(2)\,\mathrm{(ii)}\ \text{and AT.7(1)'s flux row re-cited};\ \text{the motion census: the register bar [BM.10(1)] leaves the phase orbit the only admissible read-side motion [AT.23(1)]}
$$
$$
(2):\ \mathrm{BM.26}(1)\text{'s }\varepsilon\text{-seal row and the locked-saturation rows re-cited};\ \Delta E_{D^-}=0\ \text{[AT.22(2)'s block census]};\qquad(3):\ \mathrm{AT.4}(1)\text{'s floor row at }E_{\mathrm{int}}=2\ \text{[machine]};\ 6A+2\ \text{at witnesses [machine]}
$$
$$
(4):\ \mathrm{Def\text{-}BM.10}(5)\text{'s form and BM.35(4)'s reframing re-cited};\qquad\Bigl(m+\tfrac{p^2}{2m}\Bigr)^2-(m^2+p^2)=\tfrac{p^4}{4m^2}\ \ge0\ \text{[machine: the exact remainder at witnesses — the }O(p^4)\text{ sign]}
$$
$$
p=0:\ E=N\,m\ \text{[machine: the square root's branch at }m>0];\qquad\text{the virial rows on the }n\text{-grid [machine]};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** Locked is not a new phase of matter; it is the atom's own read with nobody attached to the channel. Everything the generator-layer picture asked for is here and already priced: a proton sealed at its three junctures, a lepton whose floor read is literally the price of the smallest closed chain, a neutrality that makes the whole configuration silent at range, and a total-energy book whose rest slice is seal counts and whose only motion is the canonical pair's phase orbit. The assembly formula the layer quoted is the corpus's own Eulerian read — the tag it came with is not — and at the pole the virial split books the kinetic share exactly where the ladder always said it was. Nothing in the locked read knows an observer exists; that is the definition.

### AT.46 — The connected state: the tap on the seal and what changes

**Thm.**
$$(1)\quad\textbf{the bridge row:}\qquad\text{the external subnetwork's leg registers through the bound locus as a trivial chain of }V_2\ \text{— the photon class, the unique colour-free EM-active carrier}\qquad[\mathrm{EM.5};\ \mathrm{AT.14}(2)]:$$
$$\text{the same class the bound channel's own transitions emit [AT.14(2)] — the observation bridge taps the channel that carries the binding read;}$$
$$\text{the generator-layer citations "FT.86/IT.85" adjudicated: FT.86 is the flicker-ripple tier (a forward pointer: the gate row is AT.49); "IT.85" is }\neg\text{a corpus tag [token census]; the rung-2 bond content is EM.5's }V_2\text{ row and AT.14(2)'s forced carrier};$$
$$(2)\quad\textbf{the invariance row (what does not change):}\qquad\text{the baryon core stays }\varepsilon\text{-sealed and confined in both states: no colour junction joins the pair [AT.7(3)], no }D^-\text{ block loads [AT.22(2)], no sector of the force wakes on the stationary read [AT.21(2)'s census]}:$$
$$\boxed{\ \mathfrak M^{\mathrm{con}}_n\ \text{and}\ \mathfrak M^{\mathrm{lock}}_n\ \text{carry the identical pole } \mathfrak M_n(A,Z)\ }\qquad[\mathrm{Def\text{-}AT.10}(1),(2);\ \text{machine: the identity at witnesses}]:$$
$$\text{the neutrality row [AT.7(1)] is untouched: it bars range-flux reads; the connected read probes at the bound locus, scope-local [A-AT.3; AT.29] — } \neg\text{a contradiction at any locus};$$
$$(3)\quad\textbf{the changed row (what changes):}\qquad\text{what changes is the leptonic seal configuration's read-side bookkeeping: the width bracket opens from the register floor to the probed interval}\qquad[\mathrm{AT.30}(3)]:$$
$$\bigl[\tfrac16,\ |E_n|\bigr]\ \longrightarrow\ \bigl[\tfrac{1}{2\tau_n},\ |E_n|\bigr]\quad\text{at the probing tick count }\tau_n\qquad[\text{machine: }1/(2\tau_n)\le\tfrac16\iff\tau_n\ge3]:\qquad\textbf{the tap widens the resolution; it moves no pole};$$
$$(4)\quad\textbf{the force row:}\qquad\text{"the observing subnetwork exerts a force" adjudicated: the only channel-active sector on the bound channel is the mask }F_{\mathrm{EM}}\big|_{\text{mask}}\qquad[\mathrm{AT.21}(3)]:$$
$$\text{the probe books transit content under the jaw [CT0.6a] and moves nothing else: the masked orbit's spectrum is the ladder [AT.23(2)], and a second force is }\neg\text{in the inventory [A8; FT.142(2) via AT.21(1)]};$$
$$(5)\quad\textbf{the status:}\qquad\text{derived as a read; the rates of the tap stay (P5.3)-scoped [AT.15; FT.131(3)]};\qquad\neg\text{a collapse postulate},\ \neg\text{a measured bridge}\ [\mathrm{P5}].$$

**Req.** A8 (Part 1); EM.5, EM.7 (Part 2); CT0.6a (Part 1); P1, P5 (Parts 1–2); FT.142(2) (Part 3); Def-H.3, FT.1(1) (Part 3); A-AT.3, Def-AT.6, Def-AT.10, AT.7(1), AT.7(3), AT.14(2), AT.14(3), AT.15, AT.21(1), AT.21(2), AT.21(3), AT.22(2), AT.23(2), AT.29, AT.30(3) (this part); exact witness identities, token censuses [math; machine: `checks/verify_Atomic5.py` §S].

**Pf.**
$$
(1):\ \mathrm{EM.5}\text{'s }V_2\text{ row and AT.14(2)'s carrier-forcing re-cited};\ \text{the tag census [machine: the token scan]};\qquad(2):\ \text{the pole identity at witnesses [machine: }M+m_\ell+E_n=M+m_\ell+E_n]
$$
$$
(3):\ \tfrac{1}{2\tau_n}\le\tfrac16\iff\tau_n\ge3\ \text{[machine: the tick grid]};\qquad(4):\ \mathrm{AT.21}(3)\text{'s one-mask row re-cited};\ \text{the inventory scan for a second force [machine: the token census against A8's blocks]}
$$
$$
(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The observation bridge needs no new plumbing: the channel the observer taps is the channel the atom already runs — the same trivial $V_2$ class its own spectral transitions emit, already carrying the pair's binding read. That is the precise content of "the bridge was already being used by the atom to seal itself": not that the atom radiates to be observed, but that there is exactly one EM channel at the bound locus and both parties book on it. The invariance row is the load-bearing one: the pole is identical in both reads, so nothing about the observation manufactures a mass — the baryon core sits behind its $\varepsilon$-seal in both states, the cap inherits unchanged, and the only sector that ever wakes on this channel was the mask all along. What the tap buys is resolution: the bracket's lower endpoint drops from the register's floor to the probed tick count, and the width ledger absorbs the movement exactly as it absorbed every movement before it.

### AT.47 — The transition defect: the locked-to-connected difference and the two binding structures

**Thm.**
$$(1)\quad\textbf{the difference row:}\qquad\text{writing both reads in the rest-plus-kinetic assembly [AT.45(4)]:}\qquad\Delta E\ :=\ \bigl[N^ip_i+N(m+K)\bigr]_{\mathrm{lock}}-\bigl[N^ip_i+N(m'+K')\bigr]_{\mathrm{con}}\ :$$
$$\text{the shift terms carry the same convention in both states and cancel [machine]; the kinetic share is ladder-bookkept and uncharged by the tap [AT.26(3); AT.46(3)]: the assembly difference collapses to the spread movement } \mathfrak d_n\ \text{of Def-AT.10(3)}\qquad[\text{machine: the term-by-term census at witnesses]};$$
$$(2)\quad\textbf{the cancellation row:}\qquad\text{the baryon core's contribution cancels identically:}\qquad M(A,Z)\big|_{\mathrm{lock}}-M(A,Z)\big|_{\mathrm{con}}=0\qquad[\text{machine: the identity at witnesses}]:$$
$$\textbf{the remaining movement is purely leptonic — and purely bracket-borne: the lepton's rest read }m_\ell\ \text{is present in both states (the lepton is part of the seal structure in both) and cancels too}\qquad[\text{machine}]:$$
$$\boxed{\ \mathfrak d_n=\tfrac16-\tfrac{1}{2\tau_n}\ge0\ \text{carries no }M\text{ term, no }m_\ell\text{ term, no }A,Z\text{ counter — the defect is the seal's response to the tap, } \neg\text{a mass}\ }\qquad[\text{machine: the symbol census of the formula}];$$
$$(3)\quad\textbf{the locally-locked row (the relativistic clause adjudicated):}\qquad\text{"the observing subnetwork changes both }K\text{ and }m\text{" is half refuted: the rest slice is locally locked — pinned at the width--curvature hyperbola, unmoved along the ladder}\qquad[\mathrm{AT.26}(3);\ \mathrm{BM.16}(1),\ \mathrm{BM.16}(4)]:$$
$$m'=m\ \text{exactly [machine: the rest-slice identity]};\qquad K\ \text{moves only along the ladder, by the transition bookkeeping } \Delta E_{n\to m}\ [\mathrm{AT.14}(1)]\ —\ \neg\text{by the tap per se};$$
$$(4)\quad\textbf{the two-binding-structures row (the generator-layer finding adjudicated and repaired):}\qquad\text{"the lepton rest read IS the binding structure" holds in a strong form and fails as an identity:}$$
$$\text{(i) every rest read is a bound-chain read: the digon's floor read }m_\ell\mathfrak h=2\ln2\ \text{is the informational price of the minimal closed chain — binding structure of the }\ell\text{-channel itself}\qquad[\mathrm{FT.44}(4);\ \mathrm{D1.5};\ \mathrm{AT.4}(1)]:$$
$$\text{(ii) the pair's binding structure }b:=|E_1|=\varepsilon^2_{\mathrm{EM}}m_r/2\ \ [\mathrm{AT.6}(1)\ \text{at }n=1]\ \text{is a second one, at the pair's locus};\qquad\text{(iii) the exact ratio row:}$$
$$\boxed{\ \frac{b}{m_\ell}\ =\ \frac{3\,\varepsilon^2_{\mathrm{EM}}\,(1+c\,\varepsilon_{\mathrm{EM}})}{2\,(4+3\,c\,\varepsilon_{\mathrm{EM}})}\ }\qquad[\text{machine: the exact monomial at witnesses — two objects, two loci, one exact ratio, } \neg\text{an identity}];$$
$$(5)\quad\textbf{the adjudication row:}\qquad\text{the generator-layer reading } m_e:=E_{\mathrm{lock}}-E_{\mathrm{con}}\ \text{is refuted as a corpus row and replaced: the defect that exists is } \mathfrak d_n\ \text{(a bracket movement), the lepton's rest read is } m_\ell\ \text{(present in both states), and the pair pole-plus-bracket read already carries the observational content}\qquad[\mathrm{Def\text{-}AT.7};\ \mathrm{AT.32}]:$$
$$\neg\text{a value issued}\ [\mathrm{P5}];\qquad\text{the external identification of either object with the named lepton mass is identification-layer content [0.2d]};$$
$$(6)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(5);\qquad\neg\text{a new slot},\ \neg\text{a new force},\ \neg\text{a measured defect}\ [\mathrm{P5}].$$

**Req.** BM.16(1), BM.16(4), BM.35(4), BM.48(2), Def-BM.10(5) (Part 4); D1.5 (Parts 1–2); FT.44(4) (Census); Def-AT.7, AT.4(1), AT.6(1), AT.8(4), AT.14(1), AT.15, AT.16, AT.26(3), AT.30(3), AT.32, Def-AT.10, AT.45(3), AT.45(4), AT.46(3) (this part); P1, P5 (Parts 1–2); exact witness identities, symbol censuses [math; machine: `checks/verify_Atomic5.py` §S].

**Pf.**
$$
(1):\ \text{the assembly difference term by term at witnesses [machine]: the shift cancels by the shared convention, the rest slices agree [(2)], the kinetic share is uncharged [AT.26(3)]}
$$
$$
(2):\ M\big|_{\mathrm{lock}}-M\big|_{\mathrm{con}}=0,\qquad m_\ell\big|_{\mathrm{lock}}-m_\ell\big|_{\mathrm{con}}=0\ \ \text{[machine: the identities]};\qquad\text{the symbol census of }\mathfrak d_n=\tfrac16-\tfrac{1}{2\tau_n}\ \text{[machine: no }M,\ m_\ell,\ A,\ Z\ \text{token]}
$$
$$
(3):\ \text{the rest-slice identity [machine] and the lock rows re-cited [AT.26(3); BM.16(1),(4)]};\qquad(4):\ \tfrac{b}{m_\ell}=\tfrac{\varepsilon^2m_r/2}{2\ln2/\mathfrak h}=\tfrac{\varepsilon^2\mathfrak h}{4\ln2}\cdot\tfrac{6\ln2(1+c\varepsilon)}{\mathfrak h(4+3c\varepsilon)}=\tfrac{3\varepsilon^2(1+c\varepsilon)}{2(4+3c\varepsilon)}\ \ \text{[machine: cleared in the symbol ring]}
$$
$$
(5),(6):\ \text{the adjudication and status records}.\ \blacksquare
$$

**Phys.** Run the two assemblies side by side and the difference empties from the bottom up: the shift terms share a convention, the baryon rest slice is the same sealed object in both rows, the lepton's floor read rides in both books — and what survives is a single rational, one sixth minus one over twice the probing tick count. That is the whole transition defect: not a mass, not a coupling, the resolution the tap purchases, denominated in the chart's energy currency because the bracket it widens lives there. The generator-layer instinct that the defect and the lepton's rest read are the same object is honored as far as arithmetic allows — every rest read in this corpus is the price of a bound structure, and the lepton's floor read is the price of the smallest one — and repaired where it overreached: the pair's binding share is a second binding structure at a second locus, the exact monomial between them is now on the books, and an exact ratio is precisely what an identity is not. The observation books a width; the floors stay where the seals left them.

---

## Tier 5.21 — The Seal-Configuration Ladder and the Flicker Gate

### AT.48 — The orbital as seal configuration: the tightness law and the width rows

**Thm.**
$$(1)\quad\textbf{the configuration row:}\qquad\text{the "orbital" is the pole at rung }n\ \text{of the masked orbit — a stationary seal configuration of the bound channel, } \neg\text{a trajectory}\qquad[\mathrm{AT.23}(1),\ \mathrm{AT.23}(2)]:$$
$$\text{the configuration's data: }(n;\ \ell=0,\dots,n-1\ \text{with dimensions }2\ell+1\ [\mathrm{AT.10}(2)];\ \text{the orientation doublet [AT.10(4)]});\qquad\dim(\text{level }n)=n^2,\qquad\mathrm{cap}(n)=2n^2\qquad[\mathrm{AT.10}(2);\ \mathrm{AT.11}(3);\ \text{machine: the sums at }n\le10];$$
$$(2)\quad\textbf{the tightness row:}\qquad\text{the seal's tightness read at configuration }n\ \text{is the binding share}\qquad|E_n|=\frac{\kappa}{2\,n^{2}},\qquad\kappa:=\varepsilon^2_{\mathrm{EM}}\,m_r\qquad[\mathrm{AT.6}(1);\ \mathrm{AT.8}(1)]:$$
$$\boxed{\ \text{tighter configurations (lower }n\text{) carry larger binding defects — the exact }1/n^2\text{ law, coupling-free in shape}\ }\qquad[\mathrm{AT.6}(4);\ \text{machine: the }n\text{-grid}];$$
$$(3)\quad\textbf{the width rows (the generator-layer formula adjudicated):}\qquad\text{the corpus keeps three widths at three loci [AT.28(3)'s no-double-occupation discipline]:}$$
$$\text{(i) the constituent's Born width }\Delta x^{\mathrm B}_{\mathrm B}:=\Delta x^{\mathrm B}_{(\ell)}=\frac{\mathfrak h}{2\ln2}\ —\ n\text{-independent, a theorem}\qquad[\mathrm{AT.28}(1);\ \mathrm{Def\text{-}BM.4}(1)];$$
$$\text{(ii) the envelope: }\langle r^{2}\rangle_{nS}=a^{2}n^{2}\,\frac{5n^{2}+1}{2},\qquad a=\frac{1}{\varepsilon_{\mathrm{EM}}\,m_r}\qquad[\mathrm{AT.27}(1)]\ —\ \text{growing as }n^{2}\ \text{[machine: the monotone census]};$$
$$\text{(iii) the unified pole's own width read, derived here: the pole's seal-count read}\qquad E^{\mathrm{unif}}_{\mathrm{int}}(n):=\frac{\mathfrak M_n\,\mathfrak h}{\ln2}=\,(6A+2)+\frac{E_n\,\mathfrak h}{\ln2}\ =\ (6A+2)-\frac{3\,\varepsilon^2_{\mathrm{EM}}(1+c\,\varepsilon_{\mathrm{EM}})}{(4+3\,c\,\varepsilon_{\mathrm{EM}})\,n^{2}}\qquad[\mathrm{FT.44}(4)\ \text{at the pole};\ \text{machine: the cleared monomial}]:$$
$$\Delta x^{\mathrm B}_{\mathrm{unif}}(n):=\frac{\mathfrak h}{E^{\mathrm{unif}}_{\mathrm{int}}(n)\,\ln2}\qquad[\text{machine: increasing }E^{\mathrm{unif}}_{\mathrm{int}}(n)\ \text{in }n\implies\text{decreasing width read}]:$$
$$\text{the generator-layer form }\Delta x_{\mathrm B}(n)=\mathfrak h/(E_{\mathrm{int}}(n)\ln2)\ \text{is thereby derived at the unified-pole locus; the constituent-locus version is refuted — }n\text{-independence there is a theorem [AT.28(1)]};$$
$$\text{three loci, three motions: the constituent constant, the envelope growing, the unified width read tightening with binding — no double occupation of any locus [AT.28(3)]};$$
$$(4)\quad\textbf{the invariant row:}\qquad\text{the configuration's tightness--spread invariant is the fuzziness product}\qquad\Bigl(\Delta x_n\,\Delta p_n\Bigr)^{2}=\frac{5n^{2}+1}{6}\qquad[\mathrm{AT.27}(2);\ \text{machine: the census }n\le7]:$$
$$\text{equality only at }n=1;\ \text{strictly increasing in }n;\ \text{the Robertson floor exceeded by the exact factor 2 at the ground configuration [AT.27(2)]};$$
$$(5)\quad\textbf{the spectrum row:}\qquad\text{the qualitative structure of the spectrum is derived from the force, } \neg\text{imported: the full ladder is the masked orbit's stationary spectrum [AT.23(2)], and the transition bookkeeping is}\qquad\Delta E_{n\to m}=\frac{\kappa}{2}\Bigl(\frac{1}{m^{2}}-\frac{1}{n^{2}}\Bigr)>0\ \ (n>m)\qquad[\mathrm{AT.14}(1);\ \text{machine: the grid}]:$$
$$\Delta E_{2\to1}=\tfrac34\,|E_1|,\qquad\Delta E_{3\to2}=\tfrac{5}{36}\,|E_1|,\qquad\frac{\Delta E_{3\to2}}{\Delta E_{2\to1}}=\tfrac{5}{27}\qquad[\text{machine}];$$
$$(6)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(5);\qquad\text{the "orbital = seal configuration" identification is bookkeeping on the pole read [A §0.2]};\qquad\neg\text{a Rydberg import},\ \neg\text{a measured ladder}\ [\mathrm{P5}].$$

**Req.** D2.9 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); FT.44(4) (Census); Def-BM.4(1) (Part 4); Def-AT.6, AT.6(1), AT.6(4), AT.8(1), AT.10(2), AT.10(4), AT.11(3), AT.14(1), AT.23(1), AT.23(2), AT.26(2), AT.27(1), AT.27(2), AT.28(1), AT.28(3), AT.30(3) (this part); A §0.2 (Parts 1–2); exact rational grids, monomial identities [math; machine: `checks/verify_Atomic5.py` §T].

**Pf.**
$$
(1):\ \text{the sums }\textstyle\sum_{\ell=0}^{n-1}(2\ell+1)=n^2,\ 2n^2\ \text{at }n\le10\ \text{[machine]};\qquad(2):\ |E_n|=\kappa/(2n^{2})\ \text{on the grid};\ |E_n|/|E_1|=1/n^{2}\ \text{[machine]}
$$
$$
(3):\ E_n\mathfrak h/\ln2=-\varepsilon^2m_r\mathfrak h/(2n^{2}\ln2)=-3\varepsilon^2(1+c\varepsilon)/\bigl((4+3c\varepsilon)n^{2}\bigr)\ \ \text{[machine: }m_r\mathfrak h=6\ln2(1+c\varepsilon)/(4+3c\varepsilon)\ \text{at witnesses]}
$$
$$
E^{\mathrm{unif}}_{\mathrm{int}}(n)\ \text{strictly increasing in }n\ \text{[machine: the negative term's magnitude } \propto1/n^{2}\ \text{decreasing]};\qquad\Delta x^{\mathrm B}_{\mathrm{unif}}(n)\ \text{strictly decreasing [machine]};\qquad\langle r^{2}\rangle_{nS}\ \text{strictly increasing [machine]};\qquad\Delta x^{\mathrm B}_{(\ell)}\ \text{constant [machine]}
$$
$$
(4):\ (\Delta x\,\Delta p)^2=\tfrac{a^{2}n^{2}(5n^{2}+1)}{6}\cdot\tfrac{\varepsilon^{2}m_r^{2}}{n^{2}}=\tfrac{5n^{2}+1}{6}\ \ \text{[machine: }a=1/(\varepsilon m_r)\ \text{at witnesses — the }m_r\text{ cancels exact]};\qquad(5):\ \text{the transition rationals on the grid [machine]};\qquad(6):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The orbital was never a place, and the corpus can now say precisely what it is instead: a stationary configuration of the one seal the atom has, indexed by the pole's rung, dressed with the rotation algebra's multiplets and the chain's doublet. Its tightness is not a metaphor either — it is the binding share, exact, one over $n$ squared, largest where the seal is tightest. The width question the generator layer asked comes out three-valued because the atom genuinely has three widths: a constituent width that binding cannot move, an envelope that swells as $n$ squared, and — the new row — the unified pole's own width read, which tightens exactly as the binding deepens because the pole's seal-count read literally counts the binding in. The prompt's formula is thereby correct at the third locus and refuted at the first, and the difference between those two verdicts is the envelope discipline doing its job. Over the whole ladder the fuzziness product moves as five-$n$-squared-plus-one over six: tightness and spread are not independent dials but one invariant read two ways.

### AT.49 — The flicker gate: configuration change as a gated event

**Thm.**
$$(1)\quad\textbf{the gate row:}\qquad\text{a transition between seal configurations is gated by the flicker: the transition weight beyond the identity vanishes at the sharp threshold}\qquad[\mathrm{AT.15}(3);\ \mathrm{BM.23}(8);\ \mathrm{BM.19}(3)]:$$
$$\text{the gate's own weight is the round-trip parabola of the A4 datum:}\qquad\mathcal W_{\mathrm{round}}=x_+x_-=4\varepsilon_q(1-4\varepsilon_q)\le\tfrac14,\qquad\text{maximal exactly at the balance point }\varepsilon_q=\tfrac18\qquad[\mathrm{BM.44}(1);\ \mathrm{BM.122}(3);\ \mathrm{BM.123}(1),\ \mathrm{BM.123}(2);\ \text{machine: the SOS form}];$$
$$(2)\quad\textbf{the ambient row (the generator-layer reading adjudicated):}\qquad\text{"the configuration depends on the ambient energy environment" holds as formed bookkeeping and waits as dynamics:}$$
$$\text{the transitions are energy-bookkept exactly: }\Delta E_{n\to m}>0\ \text{downhill [AT.14(1)]};\ \text{the emission and absorption weights are balanced [AT.14(4)]; the gate is the threshold [AT.15(3)]}:$$
$$\text{the occupied configuration follows the energy ledger's emission bookkeeping; the occupancy dynamics — which configuration when — stays (P5.3)-scoped under the named prerequisite}\qquad[\mathrm{AT.15}(4);\ \mathrm{FT.131}(3)]:\qquad\textbf{named, } \neg\textbf{forced};$$
$$(3)\quad\textbf{the one-threshold row:}\qquad\text{the same datum gates four loci: the decay vertex [BM.23(8)], the flicker integral [BM.19(2)], the optical bookkeeping [AT.15(3)], and the configuration gate [(1)]:}$$
$$\text{the flicker residue }u=4\varepsilon_q\ \text{enters the ensemble reading }D_n=1+u+\cdots+u^{n-1}\ \text{[BM.137(1)] and the collapse functional's merge term [AT.40(1)] — one threshold, four loci, the era's own pattern};$$
$$(4)\quad\textbf{the no-flicker corollary:}\qquad\varepsilon_q=0\implies\text{the configuration-change content vanishes identically: a non-flickering shell never changes configuration}\qquad[\mathrm{AT.15}(3)\text{'s theorem at the configuration locus};\ \text{machine: }x_+x_-=0\implies\text{the resolvent is }1];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\neg\text{a lifetime, } \neg\text{a second-rate}\ [\mathrm{BM.23}(9);\ \mathrm{P5}].$$

**Req.** D0.4 (Parts 1–2); BM.19(2), BM.19(3), BM.23(8), BM.23(9), BM.44(1), BM.122(3), BM.123(1), BM.123(2), BM.137(1) (Part 4); FT.131(3) (Part 3); AT.14(1), AT.14(4), AT.15(3), AT.15(4), AT.40(1) (this part); P1, P5 (Parts 1–2); the rational parabola census, exact resolvent identities at rational thresholds [math; machine: `checks/verify_Atomic5.py` §T].

**Pf.**
$$
(1):\ \text{the SOS identity }4\varepsilon_q(1-4\varepsilon_q)=\tfrac14-16(\varepsilon_q-\tfrac18)^2\ \text{on the rational grid [machine]};\qquad(2):\ \text{the bookkeeping rows re-cited [AT.14(1), AT.14(4)]};\ \text{the scope record [AT.15(4)]}
$$
$$
(3):\ \text{the four-locus census against the cited rows [machine: the tag scan]};\qquad(4):\ x_+x_-=0\ \text{at}\ \varepsilon_q\in\{0,\tfrac14\}:\ \text{the resolvent }1/(1-w^2x_+x_-)\to1\ \text{[machine: the geometric series at the threshold]};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The gate was built three tiers of eras ago and never needed widening: at the sharp threshold the round-trip weight is zero, the transition content is zero, and a shell that cannot flicker cannot change configuration — the same theorem that silenced the decay vertex and the optical bookkeeping now silences the orbital ladder's own traffic. Away from the threshold the gate is a parabola with its hump exactly at the balance point of the two Janus moves, which is as it should be: a configuration changes when crystallization and dissolution are both live. What the ambient-energy reading adds is the book the corpus already keeps — downhill transitions book positive, the weights balance, the occupied rung follows the ledger — and one honest wait mark: which configuration a shell occupies at which ambient load is occupancy dynamics, and occupancy dynamics is rates, and rates wait on the emergent-time prerequisite with their brackets formed. The threshold controls everything it has ever controlled, and now one locus more.

---

## Tier 5.22 — The Weighing Bar and the Koide Row

### AT.50 — The incommensurability bar: the defect does not decompose

**Thm.**
$$(1)\quad\textbf{the two-currency row at the observation locus:}\qquad\text{the locked read's books are baryon-side — the count route }6A\ln2/\mathfrak h\ [\mathrm{AT.3}(1)]\ \text{plus the seal's digon floor }[\mathrm{AT.4}(1)]\ \text{— and the connected read's movement is read through the exchange factor}\qquad[\mathrm{AT.41}(2),\ \mathrm{AT.41}(4)]:$$
$$\text{one seal count, two currencies [Def-AT.8(1)]; the only admitted cross-currency operation is the declared slot}\qquad[\mathrm{AT.41}(1);\ \mathrm{A\text{-}BM.9};\ \mathrm{BM.98}];$$
$$(2)\quad\textbf{the non-decomposition row:}\qquad\boxed{\ \mathfrak d_n\ \text{cannot be decomposed into a standalone lepton mass:}\ }$$
$$\text{(i) what cancels cannot be re-weighed: the baryon term cancels identically [AT.47(2)] — a cancellation is } \neg\text{an extraction};$$
$$\text{(ii) the leptonic remainder is pair-borne: the bracket's ceiling carries the reduced mass }m_r=\frac{m_Nm_\ell}{m_N+m_\ell}\ \ [\mathrm{AT.5}(1)]\ —\ \text{a pair object [BM.48(2)'s slot]};$$
$$\text{(iii) the free members carry no binding [BM.48(4), BM.48(5); AT.3(5); AT.42(3)]: a standalone weighing would read a free member — the category bar stands at its locus};$$
$$\text{(iv) the exchanged read moves the whole ladder by }f(\xi)=\frac{\xi\,(3A+1)}{3A+\xi}\ \ [\mathrm{AT.41}(4)]:\ \text{the defect's leptonic content is }\xi\text{-relative, and }\xi\text{'s value is } \neg\text{issued}\ [\mathrm{AT.41}(5)];$$
$$(3)\quad\textbf{the relational row:}\qquad\text{"the mass is a relational quantity" derived: the floor read enters every atomic row only through the pair bookkeeping — the neutrality clause [Def-AT.4}(2)\,\mathrm{(i)}], the reduced mass [AT.5], the shell capacities [AT.11]:$$
$$\text{the pair is the smallest object whose mass bookkeeping closes: }m_{\mathrm{pair}}=m_p+m_\ell+E_1\qquad[\mathrm{AT.6}(2)\text{'s system read};\ \mathrm{AT.5}(3)\text{'s consistency row}]:$$
$$\text{the counting layer commutes with the floor read exactly at the pair}\qquad[\mathrm{BM.137}\text{'s 2-chain rows; machine: the pair identities at witnesses]};$$
$$(4)\quad\textbf{the localization row:}\qquad\text{the defect's cross-currency content localizes in }(\rho_{\mathrm B},\sigma_\ell,\sigma_\nu)\ \text{at most}\qquad[\mathrm{BM.83}\text{'s localization};\ \mathrm{BM.69}(5)]:$$
$$\neg\exists\ \text{a derivation issuing a value for any of the three}\qquad[\mathrm{BM.69}(4)\text{'s four grounds: field degree, two-torsion image, calibration weight, strength bar};\ \mathrm{BM.83}(5),\ \mathrm{BM.83}(7)];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\text{the bar is the era-locality discipline applied at the observation locus [AT.36's pattern]};\qquad\neg\text{a measured defect, } \neg\text{a comparison}\ [\mathrm{P5}].$$

**Req.** A-BM.9, BM.48(2), BM.48(4), BM.48(5), BM.69(4), BM.69(5), BM.83(5), BM.83(7), BM.98, BM.137 (Part 4); P1, P5 (Parts 1–2); Def-AT.4(2), Def-AT.8(1), AT.3(1), AT.3(5), AT.4(1), AT.5(1), AT.5(3), AT.6(2), AT.11, AT.36, AT.41(1), AT.41(2), AT.41(4), AT.41(5), AT.42(3), AT.47(2) (this part); exact pair identities at witnesses [math; machine: `checks/verify_Atomic5.py` §U].

**Pf.**
$$
(1):\ \mathrm{Def\text{-}AT.8}(1)\text{'s currency-pair row and AT.41(1)'s slot row re-cited at the observation locus};\qquad(2):\ \text{the four grounds assembled from their rows [(i) AT.47(2); (ii) AT.5(1); (iii) BM.48(4),(5); (iv) AT.41(4)]}
$$
$$
(3):\ \text{the pair bookkeeping closes at witnesses [machine]: }m_{\mathrm{pair}}=m_p+m_\ell+E_1,\quad 1/m_r=1/m_p+1/m_\ell;\qquad(4):\ \mathrm{BM.69}(4)\text{'s grounds and BM.83's localization re-cited}
$$
$$
(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** Ask the defect to split into "the electron's part" and "the proton's part", and the books refuse three separate ways. The baryon's share is not hidden in the difference — it cancelled, and a cancelled term has no residue to weigh. The lepton's share is not its own — the ceiling it moves with is the reduced mass, a quantity that exists only as a pair, and the free-member bar that has guarded single masses since Part 4 has lost none of its force. And the bridge that would carry the split is the declared slot, whose value no theorem issues. The positive content is just as sharp: the smallest object whose mass books close is the pair itself, so the mass content of the light member commutes with the counting layer exactly there and nowhere smaller — which is the precise, derived sense in which the quantity is relational. The localization row then names the only place any residual number could hide: three declared-and-unissued dimensionless slots, walled off by the four grounds.

### AT.51 — The Koide row: three seal configurations, the angle's provenance, and the scale bar

**Thm.**
$$(1)\quad\textbf{the three-configurations row:}\qquad\text{the three weights }y_i=r_i^{2}\ \text{are the squared spectrum of the }C_3\text{-covariant seal bilinear}\qquad[\mathrm{FT.113}]:$$
$$r_i=1+\sqrt2\cos\Bigl(\tfrac29+\tfrac{2\pi i}{3}\Bigr),\qquad i=0,1,2:\qquad\text{the three stationary configurations of the mixed seal commutator on the seal triplet — the democratic stationary reads [FT.111(2)]}:$$
$$\sum_ir_i=3,\qquad\sum_ir_i^{2}=6,\qquad\sum_{i<j}r_ir_j=\tfrac32,\qquad 2(r_i-1)^{3}-3(r_i-1)-\sqrt2\cos\tfrac23=0\ \ \forall i\qquad[\text{machine: exact in }\mathbb Q(\sqrt2,\sqrt3)[C,S]/(C^{2}{+}S^{2}{-}1)]:$$
$$\text{the ordering }r_1^{2}<r_2^{2}<r_0^{2}\ \text{[FT.113's enclosures; machine: certified rational interval arithmetic]};\qquad\text{"stable" reads as stationary-and-covariant: the democratic form is the unique }C_3\text{-covariant stationary read [FT.111(2)]};$$
$$(2)\quad\textbf{the provenance row (the structural origin of the phase):}\qquad\delta_\ell=\frac{2}{9}\ \text{is a ratio of spatial counts — no datum, no fit:}$$
$$\text{the numerator }2=3-1:\ \text{the doublet dimension of the spatial triad = the diagonal bilinear's }\Sigma\text{-coefficient}\qquad[\mathrm{FT.109}(3);\ \mathrm{FT.158}(2)]:$$
$$\text{the denominator }9=3\times3=\dim F_{J^\pm}\times\operatorname{tr}T(1):\ \text{the bound-chain arena dimension}\qquad[\mathrm{FT.110}(1);\ \mathrm{FT.158}(3)]:$$
$$\boxed{\ \delta_\ell=\frac{2}{\dim F_{J^\pm}\cdot\operatorname{tr}T(1)}=\frac{2}{3\cdot3}=\frac29\ }\qquad[\mathrm{FT.112};\ \mathrm{FT.158}(3),\ \mathrm{FT.158}(4);\ \text{machine: }2/9,\ (2/3)/3]:$$
$$\text{the Koide-form spectrum is forced by }C_3\text{-covariance at }A=1,\ B=\sqrt2\ \ [\mathrm{FT.111}(3);\ \mathrm{FT.158}(4)];\qquad\text{the cross-check rationals: }2/3\ \text{at three loci [FT.112's Rmk; FT.158(5)] — recorded, } \neg\text{derived-equal};$$
$$(3)\quad\textbf{the scale bar (the derivation question adjudicated):}\qquad\text{can }\mu_\ell\ \text{be derived from the 4-hop bound and the flicker threshold? }\ \boxed{\ \textbf{barred, on four standing grounds:}\ }$$
$$\text{(i) the kind row: the 4-hop bound is channel-capacity arithmetic [CT0.6a] and }\varepsilon_q\ \text{the A4 datum [D0.4] — dimensionless; the family-channel scale is dimensionful:}\qquad[\mu_\ell]=\mathfrak q^{+1/2}\qquad[\sigma_\ell=\mu_\ell\mathfrak h/\ln2\in\mathfrak q^{0}\ \Rightarrow\ [\mu_\ell]=[\mathfrak h]^{-1};\ \mathrm{BM.77}(2);\ \mathrm{CT2.1};\ \text{machine: the exponent algebra }-(-\tfrac12)=\tfrac12]:$$
$$\text{(ii) the conversion row: the inertial-to-informational conversion is the item-7/item-13 residue, } \neg\text{constructed}\qquad[\mathrm{AT.4}(3);\ \mathrm{BM.43}(2);\ \mathrm{Def\text{-}BM.6}(5);\ \mathrm{BM.98}]:$$
$$\text{(iii) the four-grounds row: BM.69(4)'s grounds — field degree, two-torsion image, calibration weight, strength bar — apply verbatim to any count-to-scale route}\qquad[\mathrm{BM.69}(4)]:$$
$$\text{(iv) the localization row: every cross-currency ratio is exact in }(\rho_{\mathrm B},\sigma_\ell,\sigma_\nu)\ \text{and no value is derived}\qquad[\mathrm{BM.83}(5),\ \mathrm{BM.83}(7)]:$$
$$\textbf{so: }\mu_\ell\ \text{requires the separate structural input — the declared conversion / mass-form bridge — named, } \neg\text{filled}\qquad[\mathrm{BM.35}(5);\ \mathrm{BM.69}(4),\ \mathrm{BM.69}(5)]:$$
$$\text{and the honorific clause: what the observation layer DOES derive is the defect read }\mathfrak d_n\ \text{and the binding-share ladder — the seal-breaking bookkeeping the corpus owns [AT.47; AT.48(2)]};$$
$$\text{the generator-layer gloss "}\mu_\ell\text{ is the energy required to break the seal" is honored exactly where the corpus can honor it: the ionization edge [AT.9; AT.25(3)] and the bracket movement [Def-AT.10(3)] — both derived; the family scale stays the residue};$$
$$(4)\quad\textbf{the identification bar:}\qquad\text{the Koide-form identification with measured lepton masses stays inadmissible without a declared map}\qquad[\mathrm{FT.89}(2\mathrm a)\text{--}(2\mathrm c);\ \mathrm{FT.158}(5);\ \mathrm{P1},\ \mathrm{P5}]:$$
$$\text{the corpus-side spectrum and angle are derived and stand; the external comparison lives in the identification layer only [0.2d]};$$
$$(5)\quad\textbf{the status:}\qquad\text{derived and re-certified: }(1),\ (2);\qquad\textbf{barred: }(3)\ \text{with the exact grounds};\qquad\text{standing: }(4).$$

**Req.** D0.4 (Parts 1–2); CT0.6a, CT0.12 (Part 1); CT2.1 (Part 2); P1, P4, P5 (Parts 1–2); Def-BM.6(5), BM.35(5), BM.43(2), BM.69(4), BM.69(5), BM.77(2), BM.83(5), BM.83(7), BM.98 (Part 4); Cal-F; FT.89(2a)–(2c), FT.109(3), FT.110(1), FT.111(2), FT.111(3), FT.112, FT.113, FT.158(2)–(5), Def-H.41 (Part 3); AT.4(3), AT.9, AT.25(3), AT.47, AT.48(2), Def-AT.10(3) (this part); exact $\mathbb Q(\sqrt2,\sqrt3)$ arithmetic, certified rational interval enclosures, exponent algebra [math; machine: `checks/verify_Atomic5.py` §U].

**Pf.**
$$
(1):\ \text{the spectrum identities in }\mathbb Q(\sqrt2,\sqrt3)[C,S]/(C^2{+}S^2{-}1)\ \text{[machine: the addition formulas give }\Sigma_i\cos(\theta+\tfrac{2\pi i}3)=0,\ \Sigma_i\cos^{2}=\tfrac32\ \text{as exact coefficient identities; the triple-angle identity gives the cubic at each root — }\cos(3\theta+2\pi i)=\cos3\theta\text{]}
$$
$$
\text{the ordering: certified rational intervals for }\cos\tfrac29,\sin\tfrac29\ \text{(Taylor remainders, width}<2^{-60}),\ \sqrt2,\sqrt6\ \text{[integer certificates]}:\ r_1^2<r_2^2<r_0^2\ \text{[machine: disjoint intervals]};\qquad(2):\ \tfrac{2}{3\cdot3}=\tfrac29=\tfrac{2/3}{3}\ \text{[machine]}
$$
$$
(3):\ [\mu_\ell]=\mathfrak q^{1/2}\ \text{[machine: the exponent arithmetic]};\ \text{the four grounds re-cited [BM.69(4)]};\ \text{the alphabet census: the capacity/flicker derivation alphabet and the inertial-read alphabet are disjoint [machine: the token sets — BM.37(2)'s pattern]};\qquad(4),(5):\ \text{the bar and status records}.\ \blacksquare
$$

**Phys.** The three weights are not a numerological relic: they are the squared stationary spectrum of the one bilinear the seal algebra owns, each weight a configuration of the mixed commutator fixed by the cyclic symmetry of the three spatial directions. The phase that splits them is perhaps the most economical number in the corpus — the triad's doublet dimension over the bound chain's arena, two over nine, with no datum anywhere in it — and the corpus's own cross-check shelf holds three other rooms where two over three lives, recorded as coincidence and never promoted. Against the one number the structure cannot reach, the bar stands with reasons attached: a dimensionful family scale cannot be conjured from capacity arithmetic and a flicker threshold, the conversion between the two mass vocabularies is the corpus's oldest named residue, and four independent grounds have barred count-to-strength routes since Part 4. What this tier can and does derive is the seal-breaking bookkeeping itself — the binding ladder and the observation defect — and the honest division of labor is now explicit: the shape is the symmetry's, the bookkeeping is the ledger's, and the absolute scale waits on the declared bridge, exactly as the register always said it would.

---

## Tier 5.23 — The Integration Audit

### AT.52 — The audit: the substrate, the bridges, the era-locality addition, the closure

**Thm.**
$$(1)\quad\textbf{the substrate row:}\qquad\text{the enumerative substrate is unchanged — the 25 cells, consumed by tag citation [AT.18(1), AT.18(3); AT.42(1)] — and the observation extension consumes the same families at new loci:}$$
$$\begin{array}{l|l}\text{census family} & \text{consumption at the observation extension}\\\hline\text{pair canon} & \text{the capacity chain and the one-tick cone [CT0.5; CT0.6; CT0.6a; CT0.9; C10; D0.9]}\\\hline\text{Janus rows} & \text{the event bookkeeping and the cone's chiral carrier [CT0.3; D1.2; D1.9; FT.108(1)]}\\\hline\text{observer channel} & \text{the connected read and the jaw on the probe's leg [Def-H.3; FT.1; EM.5--EM.7]}\\\hline\text{bound-channel rows} & \text{the locked/connected reads, the defect, the configuration ladder [AT.5--AT.8; AT.21--AT.31]}\\\hline\text{defect and currency rows} & \text{the weighing bar's grounds [Def-AT.8; AT.38--AT.41]}\\\hline\text{seal-bilinear rows} & \text{the Koide row's spectrum and provenance [FT.109--FT.113; FT.158; Def-H.41]}\end{array}$$
$$11+5+1+2+5+1=25\qquad[\text{machine: the partition re-run; no cell added}];$$
$$(2)\quad\textbf{the intact-bridge row:}\qquad\text{the EM sealing grammar stands — the observation adds no EM row [A-AT.1; AT.23--AT.24]};$$
$$\text{the scope clock stands — the connected read IS the scope clock's probing row [AT.29; AT.30]};\qquad\text{the unified mass read stands — the defect is the bracket's movement, the pole untouched [Def-AT.7; AT.47]};$$
$$\text{the width ledger absorbs the observation as bracket content; no new bracket law [AT.30]};\qquad\text{the collapse channel is untouched — the observation adds no strong-side row [Def-AT.9; AT.40]};$$
$$\text{the currency bridge is untouched — the defect crosses currencies only where it is slot-borne [AT.41; AT.50]};$$
$$(3)\quad\textbf{the era-locality addition:}\qquad\text{one row joins the table, same discipline [AT.36's pattern]:}$$
$$\begin{array}{l|l|l|l}\text{obstruction} & \text{binds in} & \text{the bridge} & \text{status}\\\hline\text{no standalone lepton mass read [BM.48(4), BM.48(5); AT.4(3)]} & \text{the free members' masses} & \text{the pair bookkeeping and the defect read [AT.47; AT.50]} & \text{re-scoped: the free-member rows stand; the pair and the defect carry the observational content}\end{array}$$
$$(4)\quad\textbf{the conservation row:}\qquad\mathfrak M^{\mathrm{con}}_n\ =\ \mathfrak M^{\mathrm{lock}}_n\ +\ \text{the booked movement}\qquad\text{exactly, with the booked movement } = \ \text{bracket content and bounded transit payload}\qquad[\mathrm{CT0.6a};\ \mathrm{AT.30}(3);\ \text{machine: the identity at witnesses}]:$$
$$\neg\text{a term of the movement attaches to any free member}\qquad[\mathrm{BM.48}(4),\ \mathrm{BM.48}(5)\ \text{re-cited}];$$
$$(5)\quad\textbf{the calibration consolidation:}\qquad\text{the extension adds no declared slot, no declaration, no dimensionful scale, no P4 member, no measured value}\qquad[\mathrm{P1};\ \mathrm{P4};\ \mathrm{P5};\ \S\mathrm{Cal}\text{-}5\mathrm d;\ \mathrm{C\text{-}AT.3}];$$
$$(6)\quad\textbf{the status:}\qquad\text{derived and recorded; machine: }`\text{checks/verify\_Atomic5.py}`\ \S\mathrm{V}].$$

**Req.** P1, P4, P5 (Parts 1–2); CT0.5, CT0.6, CT0.6a, CT0.9, C10, D0.9, CT0.3, D1.2, D1.9 (Part 1); EM.5–EM.7 (Part 2); Def-H.3, FT.1, FT.108(1), FT.109–FT.113, FT.158, Def-H.41 (Part 3); Def-AT.8, Def-AT.9, BM.48(4), BM.48(5), AT.38–AT.41 citations (Part 4); A-AT.1, Def-AT.7, AT.4(3), AT.5–AT.8, AT.18, AT.21–AT.31, AT.36, AT.40, AT.41, AT.42(1), AT.42(3), AT.47, AT.50, Def-AT.10, C-AT.3 (this part); exact set arithmetic, witness identities [math; machine: `checks/verify_Atomic5.py` §V].

**Pf.**
$$
(1):\ \text{the consumption map re-run over the six families; }11+5+1+2+5+1=25\ \text{[machine: the partition arithmetic]};\qquad(2):\ \text{the six bridge rows re-cited at their loci}
$$
$$
(3):\ \text{the table row [AT.36's four-column discipline]};\qquad(4):\ \mathfrak M^{\mathrm{con}}_n-\mathfrak M^{\mathrm{lock}}_n=\mathfrak d_n\text{-borne bracket content plus the bounded payload at witnesses [machine: the identity; the symbol census of the movement — no free-member token]}
$$
$$
(5):\ \text{the register record [P1; P4; P5; §Cal-5d; C-AT.3]};\qquad(6):\ \text{assembly}.\ \blacksquare
$$

**Phys.** The audit closes the way the era's audits close: nothing outside the books. The same twenty-five spaces feed the observation layer — the pair canon once more, now read as the speed of the channel; the Janus rows once more, now as the cone of one event; the bound-channel reads once more, now doubled into locked and connected; the bilinear spectrum once more, now named as three configurations. The partition still closes at twenty-five, every bridge from the opening tiers passes through untouched — the observation moves no pole, loads no cap, crosses no currency except through the declared slot — and one row joins the era-locality table: the bar that kept standalone lepton masses off the books now points at the pair and the defect as the carriers of whatever observational content there is. The books balance where they always balanced; the movement is bracket-borne; and the layer that asks the atom questions turns out to need nothing the atom did not already own.

---

## Closure exports of the observation extension (Tiers 5.19–5.23; consumed by no part of the canon)

$$
\begin{array}{c|c}
\text{export} & \text{the row}\\\hline
\text{the capacity derivation} & 4=\log_2\dim_{\mathbb R}\mathfrak H(\mathbb C^4)=\log_2 16=2+2;\ \ \delta h\le4\,\delta\tau\ \text{derived, attained [AT.43]}\\
\text{the candidate adjudication} & \text{the arena confirmed; the force aspects and the tetrahedral coordination refuted; no obstruction [AT.43(3),(4)]}\\
\text{the one-tick cone} & \text{max 4 hops in the immediate future cone of one seal event; }J^\pm:(\pm1,\pm1,\pm1);\ D_{\mathrm{tick}}(3)=16=C_{\mathrm{cap}}\ [\mathrm{AT.44}]\\
\text{the locked and connected reads} & \mathfrak M^{\mathrm{lock}}_n=\mathfrak M^{\mathrm{con}}_n=\mathfrak M_n;\ \text{the bracket } [\tfrac{1}{2\tau_n},|E_n|]\ \text{probed at }\tau_n\ [\mathrm{Def\text{-}AT.10};\ \mathrm{AT.45};\ \mathrm{AT.46}]\\
\text{the transition defect} & \mathfrak d_n=\tfrac16-\tfrac{1}{2\tau_n}\ge0;\ \text{no }M,\ m_\ell,\ A,\ Z\ \text{term — purely leptonic, purely bracket-borne [AT.47]}\\
\text{the two binding structures} & m_\ell\mathfrak h=2\ln2\ \text{(the digon's own)};\quad b/m_\ell=3\varepsilon^2_{\mathrm{EM}}(1+c\varepsilon_{\mathrm{EM}})/\bigl(2(4+3c\varepsilon_{\mathrm{EM}})\bigr)\ [\mathrm{AT.47}(4)]\\
\text{the configuration ladder} & |E_n|=\kappa/(2n^{2});\ \ E^{\mathrm{unif}}_{\mathrm{int}}(n)=(6A+2)-3\varepsilon^2_{\mathrm{EM}}(1+c\varepsilon_{\mathrm{EM}})/\bigl((4+3c\varepsilon_{\mathrm{EM}})n^{2}\bigr);\ \ (\Delta x\,\Delta p)^{2}=(5n^{2}+1)/6\ [\mathrm{AT.48}]\\
\text{the flicker gate} & \mathcal W_{\mathrm{round}}=4\varepsilon_q(1-4\varepsilon_q)\le\tfrac14;\ \ \varepsilon_q=0\implies\neg\text{configuration change}\ [\mathrm{AT.49}]\\
\text{the weighing bar} & \neg\exists\ \text{a standalone lepton mass read; the pair is the smallest closed book [AT.50]}\\
\text{the Koide row} & r_i=1+\sqrt2\cos(\tfrac29+\tfrac{2\pi i}3);\ \ \delta_\ell=2/(3\cdot3);\ \ \mu_\ell\ \text{barred on four grounds [AT.51]}\\
\text{the era-locality addition} & \text{the standalone-weighing bar re-scoped at the pair and the defect [AT.52(3)]}
\end{array}
$$

## Emission-cycle charter (Tiers 5.24–5.30): the Emission-Cycle Observation Extension — the Transient Photon Bridge, the Roundtrip Closure, and the Lepton Rest Read from Shell-State Changes

**0.1e Charter of the emission-cycle extension.** The emission-cycle extension continues the atomic era — incrementally, inside this part, with no new era declared — into the layer of the observation channel's cycle: the audit of the premises the cycle runs on, the five-phase emission cycle that replaces every persistent-attachment reading of the observation bridge, the roundtrip closure theorem that bars one-way reads, the shell-transition ledger that books the carried-off energy, the inversion that reads the pair from the carried energies, the extraction that reaches the lepton floor read through the pair bookkeeping, and the Koide-row reconciliation that keeps the scale bar standing. Its foundation stack, by citation: (i) the audit substrate [AT.43–AT.52; Def-AT.10; C-AT.3]: the capacity chain, the Janus cone, the locked and connected reads, the defect, the ladder, the gate, the bar, the Koide row; (ii) the transition ledger [AT.14; AT.8(2)]: the exact rationals, the forced carrier, the jaw, the balance; (iii) the observer channel [Def-H.3; Def-H.35; FT.1; FT.153]: the extractable-information sup, the channel-visible content, the boundary-schedule attainment; (iv) the carrier class [EM.5–EM.8]: the trivial chain of $V_2$, massless, zero bound entropy, two polarizations; (v) the closure arithmetic [AT.4(1); D1.5; EM.7]: the digon floor, the closed-chain discipline, the photon's $\mathsf E_{\mathrm{bd}}=0$; (vi) the vacuum-relative read [A5; CT0.2; Def-H.30's S0 row; BM.96(4); FT.144(4),(5)]: the all-virtual state $\rho_\circ=\tfrac14I$, unregistered, no accessible pole; (vii) the pair bookkeeping [AT.3(1); AT.4(1); AT.5; AT.41(3)]: the count route, the floor read, the strict-currency reduced mass; (viii) the currency discipline [BM.69(4); BM.83; BM.98; A-BM.9; AT.41]: the slot, the localization, the four grounds. Its outputs: the premise audit and the term census (Tier 5.24); the bridge-open phase and the five-phase cycle with the disconnection theorem (Tier 5.25); the roundtrip closure theorem (Tier 5.26); the shell-transition ledger and the two-books adjudication (Tier 5.27); the inversion and the multi-transition consistency (Tier 5.28); the extraction to the lepton floor read and the Koide reconciliation (Tier 5.29); the integration audit (Tier 5.30). Its enumerative substrate remains the Census block: the 25 cells, consumed by tag citation and extended by no new cell [AT.18(1), AT.18(3); AT.52(1)]. The charter adds no declared slot, no declaration, no dimensionful scale, and no P4 member [P1; P4; §Cal-5e].

**0.2e Standing bars of the emission-cycle extension.** The connected read of Def-AT.10 is re-scoped at this extension: an observer-attached channel state is $\neg$ a persistent read — the bridge exists only between emission and reception (forward pointers: Def-AT.11; AT.54(5)), and no row of this extension formalizes a durable connected atom. The false row is barred at its locus and stays barred here: $m_e:=E_{\mathrm{lock}}-E_{\mathrm{con}}$ is the adjudicated error of AT.47(5), appears in this extension only as an adjudicated error if cited, and is $\neg$ reintroduced under another name — the allowed defect is the bracket movement $\mathfrak d_n$ [Def-AT.10(3)] and the transition energy is the shell-ladder difference [AT.14(1)]; the two are distinct books (forward pointer: AT.56(4)). No [EXT] datum enters any **Thm** clause: external photon energies, measured line lists and identification-layer series names live in audit rows only (forward pointers: the audit and quarantine rows of the ledger tiers). No Bell/EPR import: the nonlocal-read obstruction is adjudicated as an external-concept audit (forward pointer: AT.55(4)), and the corpus-native content is the four no-go rows — no instantaneous state collapse across disjoint subnetworks, no cross-currency value extraction without a formed bridge, no joint measurement read without a closed roundtrip, all correlation content carried by ledger-formed chains bounded by the capacity jaw. No persistent observer-attached state unless derived as a closed roundtrip read (forward pointer: the closure tier). No particle identification enters any row: the generator-layer names stay in the identification layers already logged [A-AT.2; A-AT.4; 0.2d]. No Schrödinger equation, no spacetime stage supplied from outside the ledger, no smooth-manifold light cone [0.2d's discipline, extended]. Amplitude $\ne$ mass [FT.79(5)]; rung $\ne$ scale [D0.8]; the bracket discipline: a spread is an inequality, never a value [§0.2b]; no measured value attaches to any row of this extension [P5].

---

## §Cal-5e — Free internal parameters of the emission-cycle extension (P4-class)

**None introduced by this extension; none inherited beyond the standing registers.** Inherited and undeclared: the single dimensionful scale $\mathfrak h$ [P1]; the fermion-era registry Cal-F [Cal-F; FT.113(3); FT.143(3)]; the baryomesonic register [Cal-BM]: the bridge ratio slot $\rho_{\mathrm B}$ [A-BM.9, value $\neg$issued], the electric-coupling slot $e_0$ [C-BM.2, value $\neg$issued], the channel-scale rows [C-BM.3]; the atomic symbolic-use logs [C-AT.1; C-AT.2; C-AT.3]. The emission-cycle extension issues **no** new slot: every new row is an exact rational or monomial form in $(\mathfrak h,\ln2,e,c,\varepsilon_{\mathrm{EM}},\varepsilon_q)$ over the integer counters $(A,Z,n_i,n_f,\delta h,\delta\tau,\tau_n)$, and the logs stand unextended except for the record below:

$$(\mathrm{C\text{-}AT.4})\quad\textbf{the log consolidation (record, } \neg\textbf{addition):}\qquad \mathrm{C\text{-}AT.1}\text{--}\mathrm{C\text{-}AT.3}\ \text{stand verbatim; the emission-cycle tiers use}\ e,\ c,\ \varepsilon_{\mathrm{EM}}\ \text{symbolically and issue no value}\ [\mathrm{P5}];$$
$$\text{the carried-off energies are}\ \kappa\text{-denominated reads with}\ \kappa:=\varepsilon_{\mathrm{EM}}^{2}\,m_r\ \text{the only product read}\ [\mathrm{AT.48}(2)];\qquad\neg\exists\ \text{a coupling value, a ladder energy or an external datum in any Thm clause}\ [\mathrm{P5};\ 0.2\mathrm{e}].$$

No second dimensionful scale exists [P1]; $\varepsilon_q$ remains the A4 datum, ¬a parameter [D0.4]; $\xi$ remains the derived exchange factor of AT.41(2), ¬a slot; the separation of $\varepsilon_{\mathrm{EM}}$ and $m_r$ from their product is read-relative, ¬ a calibration (forward pointer: AT.57(1)).

---

## §A-AT (emission-cycle extension) — Logged declarations: none (record)

**No declaration is issued.** The extension's new objects are all reads on constructed structures: the bridge-open phase is a read-side interval of the observation channel the corpus already owns [Def-H.3; Def-H.35; FT.153], defined as a provisional structural class [Def-AT.11] — a definition, ¬ a declaration; the five-phase cycle is bookkeeping on the transition ledger [AT.14]; the roundtrip closure is the closed-chain discipline [AT.4(1)'s structure; EM.7] applied at the observation locus; the extraction is currency-internal algebra [AT.41(3)]. The declaration discipline of A-AT.1/A-AT.5 is therefore not triggered: no constitutive grammar is missing from the inventory, and the charter's outputs are theorems about declared and derived structures, from prior tags and exact-arithmetic steps alone. The naming declaration that would attach an identification-layer mass label to the floor read is named and owed, ¬ issued (forward pointer: AT.58(3)). Everything Tiers 5.24–5.30 prove is machine-checked in `checks/verify_Atomic5.py` §W.

---

## Tier 5.24 — The Premise Audit and the Term Census

### AT.53 — The audit: every cited tag, every Architect term, and the forbidden row

**Thm.**
$$(1)\quad\textbf{the tag-audit row (Directive 0(a), machine-executed):}\qquad\text{every tag the cycle cites is present in the frozen corpus, with the cited sub-rows in their bodies}\qquad[\text{machine: the tag census and sub-row census in `checks/verify_Atomic5.py` §W}]:$$
$$\begin{array}{l|l}\text{tag family} & \text{the audit verdict}\\\hline\text{this part} & \mathrm{AT.6},\ \mathrm{AT.8},\ \mathrm{AT.11},\ \mathrm{AT.12},\ \mathrm{AT.13},\ \mathrm{AT.14},\ \mathrm{AT.21},\ \mathrm{AT.23},\ \mathrm{AT.26},\ \mathrm{AT.28},\ \mathrm{AT.30},\ \mathrm{AT.31},\ \mathrm{AT.32},\ \mathrm{AT.38}\text{--}\mathrm{AT.52},\ \mathrm{Def\text{-}AT.10},\ \mathrm{C\text{-}AT.3}:\ \textbf{all present, series-ordered, Thm/Req/Pf/Phys-complete}\\\hline\text{Part 2} & \mathrm{EM.5},\ \mathrm{EM.6},\ \mathrm{EM.8}\ \text{present (and}\ \mathrm{EM.7}\ \text{consumed at the closure)}:\ \textbf{present}\\\hline\text{Part 3} & \mathrm{FT.44}(4)\ \text{present (a Census cell, verified as a row-wise citation)},\ \mathrm{FT.109}(3),\ \mathrm{FT.110}(1),\ \mathrm{FT.153},\ \mathrm{FT.158}\ \text{present (and}\ \mathrm{Def\text{-}H.3},\ \mathrm{Def\text{-}H.30}\text{'s (S0) row},\ \mathrm{Def\text{-}H.35},\ \mathrm{FT.1},\ \mathrm{FT.36}(2),\ \mathrm{FT.144}(4)\ \text{consumed at the cycle and closure rows)}:\ \textbf{present}\\\hline\text{Part 4} & \mathrm{BM.23}(5),\ \mathrm{BM.26}(1),\ \mathrm{BM.35},\ \mathrm{BM.69}(4),\ \mathrm{BM.83},\ \mathrm{BM.137},\ \mathrm{BM.143}:\ \textbf{present}\\\hline\text{Part 1} & \mathrm{CT0.6a}\ \text{present; the vacuum rows}\ \mathrm{A5},\ \mathrm{CT0.2}\ \text{present}:\ \textbf{present}\\\hline\text{D-RS rows} & \neg\textbf{canonical at this level: the token census returns zero hits for the D-RS label outside the audit rows}\ [\text{machine}]:\ \text{recorded as absent, } \neg\text{fabricated}\end{array}$$
$$(2)\quad\textbf{the term-location row (Directive 0(b)):}\qquad\text{the five Architect terms locate as follows — every location a corpus row, every miss an exact miss:}$$
$$\begin{array}{l|l|l}\text{Architect term} & \text{canonical locus} & \text{verdict}\\\hline\text{the vacuum-looking } \rho\text{-state} & \text{the all-virtual state }\rho_\circ=\tfrac14I,\ S_{\mathrm{raw}}=\ln4\ \ [\mathrm{A5};\ \mathrm{CT0.2};\ \mathrm{Def\text{-}H.30}\text{'s (S0) row};\ \mathrm{BM.35}(1)]:\ \text{observer-relative read: the complement's content is vacuum-sector, unregistered, no accessible pole}\ [\mathrm{BM.96}(4);\ \mathrm{FT.144}(4),(5)] & \textbf{canonical; the observer-relative reading derived at the cycle tier (forward pointer: AT.54(1))}\\\hline\text{the photon bridge} & \text{the trivial chain of }V_2\ \ [\mathrm{EM.5};\ \mathrm{AT.14}(2);\ \mathrm{AT.46}(1)] & \textbf{canonical}\\\hline\text{the partially real connected subnetwork} & \neg\exists\ \text{a canonical class}\ [\text{machine: the token census — zero hits in the corpus}] & \textbf{missing: defined provisionally as Def-AT.11 (forward pointer: the phase definition), the definition owed-marked at its locus}\\\hline\text{the photoreceptor/observer subnetwork} & \text{the single-contact external observer}\ \ [\mathrm{Def\text{-}H.35};\ \mathrm{FT.153};\ \mathrm{FT.1}];\ \text{``photoreceptor neuron'' is identification-layer content}\ [0.2\mathrm{e}] & \textbf{canonical as the observer channel; the biological name stays out}\\\hline\text{the roundtrip} & \text{formed round-trip objects: the weight }\mathcal W_{\mathrm{round}}\ [\mathrm{BM.44}(1);\ \mathrm{BM.122}(3);\ \mathrm{BM.123}]\ \text{and the closed-chain discipline}\ [\mathrm{AT.4}(1);\ \mathrm{EM.7}];\qquad\neg\exists\ \text{a cone-traversal (``radar'') leg}\ [\mathrm{AT.43}(5)\text{'s census}] & \textbf{the closure condition is derivable at the closure tier (forward pointer: AT.55); the exact return leg is an owed row there}\end{array}$$
$$(3)\quad\textbf{the forbidden-row bar (Directive 0(c)):}\qquad\text{the adjudication table of the three candidate identities at the observation locus:}$$
$$\begin{array}{l|l|l}\text{candidate identity} & \text{verdict} & \text{the standing row}\\\hline m_e:=E_{\mathrm{lock}}-E_{\mathrm{con}} & \textbf{refuted — the adjudicated error; cited only as an adjudicated error} & \mathrm{AT.47}(5);\ 0.2\mathrm{e}\\\hline\mathfrak d_n=\tfrac16-\tfrac{1}{2\tau_n} & \textbf{the allowed defect: the bracket movement, a spread, } \neg\text{a value} & \mathrm{Def\text{-}AT.10}(3);\ \mathrm{AT.47}(1)\text{--}(2)\\\hline\Delta E_{n_i\to n_f} & \textbf{the transition energy: the shell-ladder difference, the carried-off content} & \mathrm{AT.14}(1);\ \mathrm{AT.8}(2);\ \text{the transition-table row (forward pointer: AT.56(1))}\end{array}$$
$$\text{the two-books clause: the defect row and the ladder row are distinct books — the exact relation and the obstruction stated at the two-books row (forward pointer: AT.56(4));\qquad\neg\exists\ \text{a reading of}\ \Delta E\ \text{as the defect or as a lepton mass: that is the barred row renamed}\ \ [\mathrm{AT.50};\ \mathrm{AT.47}(5)];$$
$$(4)\quad\textbf{the status:}\qquad\text{derived as an audit: every verdict backed by a machine census against the frozen text}\ [\text{machine: §W}];\qquad\neg\text{a fabricated tag},\ \neg\text{a borrowed premise},\ \neg\text{a P-H import}.$$

**Req.** A5, CT0.2, CT0.6a, D0.4 (Part 1); EM.5–EM.8 (Part 2); Def-H.3, Def-H.30, Def-H.35, FT.1, FT.36(2), FT.44(4), FT.109(3), FT.110(1), FT.144(4), FT.153, FT.158 (Part 3); A-BM.9, BM.23(5), BM.26(1), BM.35(1), BM.44(1), BM.69(4), BM.83, BM.96(4), BM.98, BM.122(3), BM.123, BM.137, BM.143 (Part 4); AT.4(1), AT.6–AT.8, AT.11–AT.14, AT.21, AT.23, AT.26, AT.28, AT.30–AT.32, AT.38–AT.52, Def-AT.10, AT.43(5), AT.46(1), AT.47(5), AT.50, C-AT.3 (this part); P1, P5 (Parts 1–2); the tag census, the sub-row census, the token censuses [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \text{the tag census: every listed tag's header exists in the frozen corpus; the sub-row census: each cited }(k)\ \text{marker occurs in its row's body [machine]};\qquad\text{the D-RS token census: zero hits [machine]}
$$
$$
(2):\ \text{the term census: the five loci resolved against the corpus text; the two misses (``partially real'', the radar leg) recorded as exact misses [machine: the token scans]}
$$
$$
(3):\ \text{the adjudication table: each verdict its standing row's own text [machine: the document pins]};\qquad(4):\ \text{the audit record}.\ \blacksquare
$$

**Phys.** An extension that lives on citations earns its footing by counting them before it spends them. The audit walks the whole stack the cycle needs — the capacity chain, the transition ledger, the observer channel, the carrier class, the closure arithmetic, the vacuum rows, the pair bookkeeping, the currency bars — and finds every tag standing where the earlier tiers left it, sub-rows included; and it finds two words missing, exactly two: the corpus has no "partially real" class and no radar leg, so the extension builds the one as a provisional definition with its debt recorded and defers the other as an owed construction with its bar derived. The third entry is the discipline that guards the whole tier: the difference the observation books is not a mass, the bracket movement is not a value, and the ladder difference is not either of them — three identities, one refuted, two alive, and never to be conflated again.

---

## Tier 5.25 — The Five-Phase Emission Cycle

### Def-AT.11 — The bridge-open phase: the transient, partially real connected subnetwork

**Def.** Let the constructed EM-pair composite at level $n$ of class $(A,Z)$ be given [Def-AT.4; Def-AT.6], and let $o$ be an external single-contact observer, $o\notin$ the composite's support [Def-H.35].
$$(1)\quad\textbf{the phase class:}\qquad\text{the bridge-open phase at }(n_i\to n_f;\ o)\ :=\ \text{the read-side interval of the observation channel between the emission vertex (the shell transition's vertex at the composite's leptonic seal locus) and the reception vertex (the absorption event at }o\text{'s receiving locus), during which a transit chain }\gamma\text{ of the photon class joins the two loci}\qquad[\mathrm{AT.14}(2);\ \mathrm{EM.5};\ \mathrm{D1.5}];$$
$$(2)\quad\textbf{the partial-reality row (the provisional structural class):}\qquad\text{``partially real'' is defined as: real chain, sealed ends —}$$
$$\text{(i) the chain is real where it is carried: the transit hops are registered real edges}\qquad[\mathrm{CT0.4};\ \mathrm{CT0.9};\ \mathrm{EM.7}: \mathsf E_{\mathrm{tr}}=\delta h\ln2]:$$
$$\text{(ii) both joined subnetworks remain self-sealed across the whole phase: the composite's baryon core is }\varepsilon\text{-sealed [AT.45}(2);\ \mathrm{BM.26}(1)],\ \text{the observer's own books are untouched [Def-H.35's locus-separation clause]}:$$
$$\boxed{\ \text{a real chain joining two sealed books is } \neg\text{ a merged object, } \neg\text{ a new state of matter, } \neg\text{ an attachment — it is a phase of one channel}\ }\qquad[\mathrm{AT.21}(3); \mathrm{Def\text{-}H.35}];$$
$$(3)\quad\textbf{the four negations:}\qquad\neg\ \text{a permanent attachment (phase-bounded: open at emission, closed at reception)};\qquad\neg\ \text{a new force (the only channel-active sector is the mask} \ [\mathrm{AT.21}(3);\ \mathrm{AT.46}(4)]);$$
$$\neg\ \text{a new slot (no register added}\ [\S\mathrm{Cal}\text{-}5\mathrm{e}]);\qquad\neg\ \text{a lepton extraction (the floor read stays in the seal}\ [\mathrm{AT.47}(2)]);$$
$$(4)\quad\textbf{the owed marks:}\qquad\text{(i) the class is provisional: its disposition in a permanent-chart formalism is owed to the closure rows (forward pointer: AT.60(6));\qquad\text{(ii) the observer-side return leg is } \neg\ \text{formed (forward pointer: AT.55(5))};$$
$$(5)\quad\textbf{the scope:}\qquad\text{read-side and chart-side}\ [\mathrm{BM.10}(3);\ \mathrm{A\text{-}AT.3}];\qquad\neg\ \text{a dynamics},\ \neg\ \text{a collapse postulate}.$$

### AT.54 — The cycle: five phases, the forced carrier, and the disconnection theorem

**Thm.**
$$(1)\quad\textbf{phase 1 (locked pre-emission):}\qquad\text{the composite is the locked unified pole at rung }n_i\qquad[\mathrm{AT.45};\ \mathrm{AT.26}(1)]:$$
$$\mathfrak M_{n_i}\ =\ M(A,Z)+m_\ell+E_{n_i},\qquad E_{n_i}=-\frac{\kappa}{2\,n_i^{2}},\qquad\kappa:=\varepsilon_{\mathrm{EM}}^{2}\,m_r\qquad[\mathrm{AT.48}(2);\ \mathrm{AT.6}(1)]:$$
$$\text{the bracket at the register floor }[\tfrac16,\ |E_{n_i}|]\ \ [\mathrm{AT.30}(2),(3);\ \text{nonemptiness scope: }\kappa\ge n_i^{2}/3];\qquad\text{the baryon core }\varepsilon\text{-sealed}\ [\mathrm{AT.45}(2)];\ \text{the lepton part of the seal structure}\ [\mathrm{AT.45}(3)]:$$
$$\textbf{the vacuum-looking row: the observer-relative channel read is the all-virtual state }\rho_\circ=\tfrac14I:\ \text{no real edge is registered between the two loci, the channel-visible content vanishes, }E_{\mathrm{vis}}(\gamma)=0\ \text{over the pre-emission interval}\qquad[\mathrm{A5};\ \mathrm{CT0.2};\ \mathrm{Def\text{-}H.30}\text{'s (S0) row};\ \mathrm{BM.96}(4);\ \mathrm{FT.144}(4),(5);\ \mathrm{Def\text{-}H.35}];$$
$$(2)\quad\textbf{phase 2 (shell transition and emission):}\qquad\text{the leptonic seal configuration moves }n_i\to n_f,\ n_i>n_f\ge1,\ \text{and the emitted carrier is forced: colour-free (the seals stay intact), EM-active, charge-neutral for }Q\text{-preserving transitions}\qquad[\mathrm{BM.23}(5)\text{'s selection pattern};\ \mathrm{AT.14}(2)]:$$
$$\text{the unique such carrier in the inventory: the photon class — the trivial chain of }V_2\qquad[\mathrm{EM.5};\ \mathrm{EM.6}\ \text{(massless)};\ \mathrm{EM.8}\ \text{(two polarizations)};\ \mathrm{D3.7}]:\qquad\text{the }q\text{-channel fails colour-freeness, the }\nu\text{-channel fails EM-activity}\ [\mathrm{FT.119};\ \mathrm{FT.142}(1)]:$$
$$\boxed{\ \Delta E_{n_i\to n_f}\ =\ \frac{\varepsilon_{\mathrm{EM}}^{2}\,m_r}{2}\Bigl(\frac{1}{n_f^{2}}-\frac{1}{n_i^{2}}\Bigr)\ =\ \frac{\kappa}{2}\Bigl(\frac{1}{n_f^{2}}-\frac{1}{n_i^{2}}\Bigr)\ >\ 0\ \ \text{exactly, for all }n_i>n_f\ge1\ }\qquad[\mathrm{AT.14}(1);\ \mathrm{AT.8}(2);\ \text{machine: the positivity grid }n\le100];$$
$$(3)\quad\textbf{phase 3 (the bridge-open phase):}\qquad\text{Def-AT.11's class instantiated: the composite's leptonic seal locus, the emitted photon chain, and the observer's receiving locus are joined by one formed chain — the same EM channel class that carries the binding read}\qquad[\mathrm{Def\text{-}AT.11}(1),(2);\ \mathrm{AT.46}(1)]:$$
$$\text{the transit content is register-bookkept under the jaw}\qquad\mathsf E\ \le\ \min(\delta h,\ 4\,\delta\tau)\,\ln2\qquad[\mathrm{CT0.6a};\ \mathrm{FT.153};\ \mathrm{FT.1}(1)]:$$
$$\textbf{the two-books row: the jaw bounds the leg's register content, } \neg\textbf{ its energy bookkeeping — the ladder book of (2) and the register book are separate ledgers}\qquad[\mathrm{AT.14}(3);\ \mathrm{C10}];$$
$$(4)\quad\textbf{phase 4 (reception):}\qquad\text{the observer registers the carried content: the channel-visible content is the boundary registration sum, attained within the jaw}\qquad[\mathrm{Def\text{-}H.35};\ \mathrm{FT.153}: E_{\mathrm{vis}}=|E_{\mathrm{bd}}|\ln2=\mathsf B(\gamma)\ \text{at capacity}]:$$
$$(5)\quad\textbf{phase 5 (disconnection):}\qquad\text{on absorption the chain ends: the carrier is absorbed, the transit domain empties, and the observer channel reverts to the vacuum-looking read }E_{\mathrm{vis}}=0\qquad[\mathrm{FT.153}\text{'s vacuous-domain clause};\ \mathrm{A5};\ \mathrm{CT0.2}]:$$
$$\text{the composite is locked again, at rung }n_f:\quad\mathfrak M_{n_f}=M(A,Z)+m_\ell+E_{n_f},\quad\text{bracket re-closed at the register floor }[\tfrac16,\ |E_{n_f}|]\ \ [\mathrm{AT.30}(2),(3);\ \text{the same nonemptiness scope}]:$$
$$\boxed{\ \textbf{the disconnection theorem: no persistent observer leg remains after reception — the leg is the chain [Def-AT.11}(1)\textbf{]; no chain, no leg; the connected read of Def-AT.10}(2)\textbf{ exists only as the bridge-open phase's read-side book, } \neg\textbf{ a state the observer keeps}\ }\qquad[\text{machine: the phase census}];$$
$$\textbf{the conservation row (the cycle's exact book):}\qquad\mathfrak M_{n_i}\ =\ \mathfrak M_{n_f}\ +\ \Delta E_{n_i\to n_f}\qquad\text{exactly, no term attaching to any free member}\qquad[\mathrm{BM.48}(4),(5);\ \text{machine: the identity at witnesses}];$$
$$(6)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(5);\qquad\text{the five-phase cycle is bookkeeping on the transition ledger and the observer channel, } \neg\text{a new mechanism};\qquad\neg\ \text{a collapse postulate},\ \neg\ \text{a measured cycle}\ [\mathrm{P5}].$$

**Req.** A5, CT0.2, CT0.4, CT0.6a, CT0.9, D1.5, D3.7, C10 (Parts 1–2); EM.5–EM.8 (Part 2); Def-H.3, Def-H.30, Def-H.35, FT.1, FT.119, FT.142(1), FT.144(4), FT.153 (Part 3); BM.23(5), BM.26(1), BM.48(4), BM.48(5), BM.96(4) (Part 4); Def-AT.4, Def-AT.6, Def-AT.11, AT.6(1), AT.14(1)–(3), AT.21(3), AT.26(1), AT.30(2), AT.30(3), AT.45, AT.46(1), AT.46(4), AT.48(2), AT.8(2) (this part); A-AT.3, BM.10(3) (Parts 1–4); P1, P5 (Parts 1–2); exact rational witness identities, the positivity grid, the phase census [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \text{the pole form and the bracket rows re-cited};\ E_{\mathrm{vis}}=0\ \text{pre-emission: no boundary edge registered [Def-H.35's sum over }E_{\mathrm{bd}}=\varnothing\text{; machine]}
$$
$$
(2):\ \mathrm{BM.23}(5)\text{'s three selection conditions instantiated; the inventory census re-cited [AT.14(2)]};\qquad\text{the positivity grid: }\tfrac1{n_f^{2}}-\tfrac1{n_i^{2}}>0\ \text{for all }1\le n_f<n_i\le100\ \text{[machine: exact rationals]}
$$
$$
(3):\ \text{the jaw and the two-ledger separation re-cited [CT0.6a; AT.14(3); C10]};\qquad(4):\ \text{the attainment row re-cited [FT.153]}
$$
$$
(5):\ \text{the vacuous-domain clause [FT.153] and the re-lock row [AT.30(2),(3)]};\qquad\text{the conservation identity at witnesses }(\mathfrak h=\tfrac9{10},\ \ln2=\tfrac35,\ c=2,\ \varepsilon=\tfrac13,\ M\ \text{count-route}): \mathfrak M_{n_i}-\mathfrak M_{n_f}-\Delta E_{n_i\to n_f}=0\ \text{for all six table transitions [machine]}
$$
$$
(6):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The corrected picture needs no new plumbing, only honest phasing. Phase one is the atom nobody is reading: pole at the register floor, core behind its seal, and — the row that gives "vacuum-looking" its teeth — zero channel-visible content, because channel-visible content is a sum over registered boundary edges and none are registered. Phase two forces the carrier the old way: colour-free, EM-active, charge-neutral, and the inventory still contains exactly one object with all three. Phase three is the whole content of "partially real": a chain of real registered hops joining two books that each stay sealed — the bridge is a phase of one channel, not a merger of two objects, and the jaw it runs under prices registers, never energies. Phase four books the arrival at the boundary sum's exact value; phase five is the row the whole tier exists for — the chain ends, the transit domain empties, the atom re-locks at its new rung, and the conservation row closes the cycle to the exact carried difference. What the observer keeps after reception is nothing: no leg, no state, no attachment — only the registered content of a book that has since moved on, and the obligation to wait for the next emission.

---

## Tier 5.26 — The Roundtrip Closure Theorem

### AT.55 — Observation closes only on a roundtrip

**Thm.**
$$(1)\quad\textbf{the one-way insufficiency row:}\qquad\text{a one-way emitted photon is an open chain: the photon class admits no bound loops}\qquad[\mathrm{EM.5}: \neg\text{bound loops}]:$$
$$\text{it books zero bound entropy}\qquad\mathsf E_{\mathrm{bd}}=0\qquad[\mathrm{EM.7}]:\qquad\text{it registers at one locus only (the receiver's), while the emitter's post-emission book is unregistered by the leg:}$$
$$\boxed{\ \text{a joint ledger read — one closed book over both subnetworks — does not form on a one-way leg}\ }\qquad[\mathrm{AT.4}(1)\text{'s closure structure at the observation locus};\ \text{machine: the juncture census}];$$
$$(2)\quad\textbf{the closure condition (the digon row at the observation locus):}\qquad\text{a closed book requires a closed chain; the minimal closed chain is the digon — two registered junctures, }L=2\qquad[\mathrm{AT.4}(1);\ \mathrm{D1.5};\ \mathrm{FT.32}(6)]:$$
$$\text{hence both ends of the leg must register: the emission vertex and a return-registration vertex — the roundtrip condition;}$$
$$\textbf{the shared connector floor: the two subnetworks' relative read localizes exactly at the closed chain's registered junctures; without closure the relative read is unlocalized and the cross-currency correlations are barred}\qquad[\mathrm{AT.41}(1);\ \mathrm{BM.98};\ \mathrm{A\text{-}BM.9}]:$$
$$\boxed{\ \textbf{Observation closes only on a roundtrip.}\ }\qquad[\text{the closure theorem};\ \text{machine: the juncture census }1<2\le2];$$
$$(3)\quad\textbf{the four no-go rows (the ledger-native block):}$$
$$\begin{array}{l|l}\text{no-go row} & \text{the frozen ground}\\\hline\text{(i) no instantaneous state collapse across disjoint subnetworks} & \text{tick locality: } \operatorname{dom}(\mathrm{tick}(v))\subseteq\{v\}\cup\{e\ni v\},\ \neg\exists\ \text{a read at edge-distance}>1\ \ [\mathrm{D1.9}];\ \text{the forward-only arrow: } \neg\exists\,\tau^{-1}\ \ [\mathrm{A6};\ \mathrm{FT.144}(2);\ \mathrm{BM.23}(9)]\\\hline\text{(ii) no cross-currency value extraction without a formed bridge} & \text{the only admitted cross-currency operation is the declared slot}\ \ [\mathrm{AT.41}(1);\ \mathrm{A\text{-}BM.9};\ \mathrm{BM.98}];\ \text{the residual content localizes in }(\rho_{\mathrm B},\sigma_\ell,\sigma_\nu)\ \text{at most, no value derived}\ \ [\mathrm{BM.83};\ \mathrm{BM.69}(4)]\\\hline\text{(iii) no joint measurement read without a closed roundtrip} & \text{rows (1)--(2): the joint read is a closed book; a closed book is a closed chain; the one-way leg books } \mathsf E_{\mathrm{bd}}=0\\\hline\text{(iv) all correlation content is carried by ledger-formed chains bounded by the capacity jaw} & \text{the photon chain is the only formed carrier}\ \ [\mathrm{AT.14}(2);\ \mathrm{EM.5}];\ \text{its register content is jaw-bounded}\ \ [\mathrm{AT.14}(3);\ \mathrm{CT0.6a}];\ \text{the carried content is transit entropy } \delta h\ln2,\ \mathsf E_{\mathrm{bd}}=0\ \ [\mathrm{EM.7}]\end{array}$$
$$(4)\quad\textbf{the external-concept audit (EPR/Bell adjudicated):}\qquad\text{the Bell-type obstructions are external theorems about external state spaces: } \neg\ \text{imported as corpus objects}\ [0.2\mathrm{e}]:$$
$$\text{the corpus-native replacement is exactly the four no-go rows of }(3);\qquad\text{the identification-layer correlation theorems live in the identification layer only};$$
$$(5)\quad\textbf{the owed row (the return leg):}\qquad\text{the exact return leg — the observer-side emission cycle by which a receiving locus re-emits a registration carrier back to the emitting locus — is } \neg\ \text{formed in the canon: the construction is named and owed, and closure is not forced}$$
$$[\mathrm{AT.43}(5)\text{'s } \neg\exists\text{-census};\ \text{machine: the token census}]:\qquad\text{what IS derived: the closure condition and its bar, }(1)\text{--}(3);\qquad\text{the formed round-trip algebra is the gate's weight}\qquad\mathcal W_{\mathrm{round}}=x_+x_-=4\varepsilon_q(1-4\varepsilon_q)=\tfrac14-16\Bigl(\varepsilon_q-\tfrac18\Bigr)^{\!2}\le\tfrac14\qquad[\mathrm{BM.44}(1);\ \mathrm{BM.122}(3);\ \mathrm{BM.123};\ \text{machine: the SOS form}]:$$
$$\textbf{the weight, re-cited at the observation locus — a weight, } \neg\textbf{ a leg};$$
$$(6)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(5);\qquad\text{the closure condition is the digon's own arithmetic applied at the observation locus, } \neg\ \text{an identification of the observation bridge with the lepton's digon};\qquad\neg\ \text{a Bell import},\ \neg\ \text{a forced closure},\ \neg\ \text{a measured roundtrip}\ [\mathrm{P5}].$$

**Req.** A6 (Part 1); CT0.2, CT0.6a, CT0.9, D1.5, D1.9 (Parts 1–2); EM.5, EM.7 (Part 2); Def-H.3, Def-H.35, FT.32(6), FT.144(2) (Part 3); A-BM.9, BM.23(9), BM.44(1), BM.69(4), BM.83, BM.98, BM.122(3), BM.123 (Part 4); AT.4(1), AT.14(2), AT.14(3), AT.41(1), AT.43(5), AT.46(1) (this part); P1, P5 (Parts 1–2); exact rational grids, the SOS identity, the juncture census [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \mathrm{EM.5}\text{'s no-bound-loop row and EM.7's }\mathsf E_{\mathrm{bd}}=0\ \text{re-cited; the juncture census: one registered end }<2\ \text{[machine]};\qquad(2):\ \mathrm{AT.4}(1)\text{'s minimal-closed-chain structure re-cited at the observation locus; the census }2\ge2\ \text{[machine]}
$$
$$
(3):\ \text{each row its frozen ground re-cited [D1.9; A6; FT.144(2); BM.23(9); AT.41(1); BM.98; BM.83; BM.69(4); EM.5; EM.7; CT0.6a]};\qquad(4):\ \text{the audit record [0.2e]}
$$
$$
(5):\ \text{the token census for the return leg [machine: zero hits]};\qquad\tfrac14-16(\varepsilon_q-\tfrac18)^2=4\varepsilon_q(1-4\varepsilon_q)\ \text{on the rational grid, sup }=\tfrac14\ \text{[machine: the SOS identity]};\qquad(6):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The anti-EPR content of this corpus was never going to be an inequality; it was going to be an audit of what a chain can carry. The answer is severe: a photon is an open chain by kind, it books nothing but transit entropy, and it registers at one end only — so the leg that leaves the atom carrying a ladder difference connects the two books without closing either joint read. What closes a book is a closed chain, and the smallest closed chain the ledger knows has two registered ends — the same two the digon has always counted. That is the roundtrip condition, and it is not optional: without it the relative read of two sealed books has no locus, the cross-currency operations have no slot, and the "correlation" everyone wants to read is content sitting in a bounded transit register with no joint book to land in. The four no-go rows are the corpus's own Bell-lesson, stated in its own alphabet: locality is tick locality, irreversibility is the arrow, extraction is slot-borne, and everything that correlates travels as registered hops under a jaw of four bits to the tick. The exact return leg waits as an owed row — named, barred from being forced, and distinct from the round-trip weight the gate has always carried, which books how a shell may change, not how two books close.

---

## Tier 5.27 — The Shell-Transition Ledger

### AT.56 — The transition table, the defect bookkeeping, and the two books

**Thm.**
$$(1)\quad\textbf{the transition table (Directive 3(a)):}\qquad\text{for arbitrary }n_i>n_f\ge1:\qquad\Delta E_{n_i\to n_f}=\frac{\kappa}{2}\Bigl(\frac{1}{n_f^{2}}-\frac{1}{n_i^{2}}\Bigr),\qquad\kappa:=\varepsilon_{\mathrm{EM}}^{2}\,m_r\qquad[\mathrm{AT.48}(2);\ \mathrm{AT.14}(1)]:$$
$$\begin{array}{c|c|c}n_i\to n_f & \text{the shape }\ \frac{1}{n_f^{2}}-\frac{1}{n_i^{2}} & \Delta E_{n_i\to n_f}\\\hline2\to1 & \frac34 & \frac{3\kappa}{8}\\3\to1 & \frac89 & \frac{4\kappa}{9}\\3\to2 & \frac{5}{36} & \frac{5\kappa}{72}\\4\to2 & \frac{3}{16} & \frac{3\kappa}{32}\\100\to1 & \frac{9999}{10000} & \frac{9999\kappa}{20000}\\100\to99 & \frac{199}{98010000} & \frac{199\kappa}{196020000}\end{array}\qquad[\text{machine: each entry exact; the ratio rows }\Delta E_{3\to2}/\Delta E_{2\to1}=\tfrac{5}{27},\ \Delta E_{3\to1}/\Delta E_{2\to1}=\tfrac{32}{27}]:$$
$$\textbf{positivity on the full grid: } \Delta E_{n_i\to n_f}>0\ \text{for all }1\le n_f<n_i\le100,\ \text{exact}\qquad[\text{machine: the rational grid]};\qquad\text{monotone rows: the shape increases in }n_i\ \text{at fixed }n_f\ \text{and decreases in }n_f\ \text{at fixed }n_i\ \ [\text{machine]};$$
$$\textbf{the [EXT] audit row: the identification layer's series labels for these families are external names — recorded here only, in an audit row, with no datum and no Thm clause}\qquad[0.2\mathrm{e};\ \mathrm{P5}];$$
$$(2)\quad\textbf{the defect bookkeeping (Directive 3(b)):}\qquad\text{the carried-off energy is the seal-configuration defect — the pole's movement along its own ladder:}$$
$$\mathfrak M_{n_i}-\mathfrak M_{n_f}\ =\ \bigl[M(A,Z)+m_\ell+E_{n_i}\bigr]-\bigl[M(A,Z)+m_\ell+E_{n_f}\bigr]\ =\ E_{n_i}-E_{n_f}\ =\ \Delta E_{n_i\to n_f}\qquad[\text{machine: the identity at witnesses}]:$$
$$\textbf{not a loss of baryon rest mass: }M(A,Z)\ \text{cancels identically — the baryon core stays }\varepsilon\text{-sealed across the transition}\qquad[\mathrm{AT.45}(2);\ \mathrm{BM.26}(1);\ \mathrm{AT.22}(2);\ \mathrm{AT.47}(2)]:$$
$$\textbf{not a loss of lepton rest read: }m_\ell\ \text{is present in both poles and cancels — the floor read stays in the seal}\qquad[\mathrm{AT.4}(1);\ \mathrm{AT.45}(3);\ \mathrm{AT.47}(2)]:$$
$$\boxed{\ \text{the photon carries the ladder difference — nothing else moves}\ }\qquad[\text{machine: the symbol census of the difference — no }M,\ \neg m_\ell,\ \neg A,\ \neg Z\ \text{token in the remainder]};$$
$$(3)\quad\textbf{the locally-locked row (Directive 3(c)):}\qquad m'=m\ \text{exactly: the rest slice is pinned at the width--curvature hyperbola and does not move along the ladder}\qquad[\mathrm{AT.26}(3);\ \mathrm{BM.16}(1),(4);\ \mathrm{AT.47}(3)\text{'s half-refutation re-cited}]:$$
$$\text{the kinetic/ladder bookkeeping changes by the transition rows; the rest slice does not — the relativistic clause stays adjudicated at its locus};$$
$$(4)\quad\textbf{the two-books adjudication (Directive 3(d)):}\qquad\Delta E_{n_i\to n_f}\ \text{and}\ \mathfrak d_{n_i}-\mathfrak d_{n_f}\ \text{are distinct books:}$$
$$\text{the bracket book: }\ \mathfrak d_{n_i}-\mathfrak d_{n_f}\ =\ \Bigl(\tfrac16-\tfrac{1}{2\tau_{n_i}}\Bigr)-\Bigl(\tfrac16-\tfrac{1}{2\tau_{n_f}}\Bigr)\ =\ \frac{1}{2\tau_{n_f}}-\frac{1}{2\tau_{n_i}}\qquad[\mathrm{Def\text{-}AT.10}(3);\ \text{machine: the clearing}]:$$
$$\text{the bracket book is }\tau\text{-counted and bracket-discipline content (a spread movement, } \neg\text{a value); the ladder book is }\kappa\text{-denominated and }n\text{-counted (exact pole differences); the two books share exactly one touchpoint —}$$
$$\textbf{the touchpoint row: the bracket's ceiling at rung }n\ \text{is the ladder value }|E_n|=\kappa/(2n^{2})\qquad[\mathrm{AT.30}(3);\ \text{machine}]:\qquad\text{the books touch at the ceiling and nowhere else;}$$
$$\textbf{the obstruction: no conversion between the books exists without a declared } \tau_n(n)\ \text{map — none is issued, no theorem forces one; the map is an owed row (forward pointer: AT.60(6));$$
$$\textbf{the false-row guard: reading }\Delta E\ \text{as the defect } \mathfrak d\ \text{or as a lepton mass is the barred row renamed}\qquad[\mathrm{AT.47}(5);\ \mathrm{AT.50};\ 0.2\mathrm{e}];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\neg\ \text{a Rydberg import},\ \neg\ \text{a measured line},\ \neg\ \text{a second defect read}\ [\mathrm{P5}].$$

**Req.** BM.16(1), BM.16(4), BM.26(1), BM.48(4), BM.48(5) (Part 4); P1, P5 (Parts 1–2); Def-AT.10, AT.4(1), AT.8(2), AT.14(1), AT.22(2), AT.26(1), AT.26(3), AT.30(3), AT.45(2), AT.45(3), AT.47(2), AT.47(3), AT.47(5), AT.48(2), AT.50 (this part); the rational grid, the symbol censuses, the witness identities [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \text{the six shapes as exact rationals [machine]; the ratio rows } \tfrac{5/36}{3/4}=\tfrac5{27},\ \tfrac{8/9}{3/4}=\tfrac{32}{27}\ \text{[machine]};\ \text{the grid positivity and the two monotone rows [machine]};\qquad(2):\ \text{the identity at witnesses [machine]; the symbol census of }E_{n_i}-E_{n_f}\ \text{[machine]}
$$
$$
(3):\ \text{the rest-slice identity and the lock rows re-cited [AT.26(3); BM.16(1),(4)]};\qquad(4):\ \text{the clearing }(\tfrac16-\tfrac1{2\tau_i})-(\tfrac16-\tfrac1{2\tau_f})=\tfrac1{2\tau_f}-\tfrac1{2\tau_i}\ \text{[machine]};\ \text{the independence censuses: varying }(\tau_i,\tau_f)\ \text{at fixed }(n_i,n_f)\ \text{moves only the bracket book, varying }(n_i,n_f)\ \text{at fixed }(\tau_i,\tau_f)\ \text{moves only the ladder book [machine]};\ \text{the ceiling identity }|E_n|=\kappa/(2n^2)\ \text{[machine]}
$$
$$
(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The table is the old ladder read as departures: six shapes, six exact rationals, every one positive, the whole grid positive, and the ratios between departures pure integers over integers because the ladder's shape never carried a coupling. What the carried energy is not matters as much as what it is: not the baryon's rest mass, which cancels because the core's seal never opens; not the lepton's floor read, which rides in both books and cancels with itself; just the pole's own rung-to-rung difference, denominated in the one product read the pair owns. And the defect question comes out a tale of two books: the bracket book counts ticks and hands over spreads, the ladder book counts rungs and hands over exact values, and they touch at a single endpoint — the ceiling — with no conversion between them until someone declares how a probing tick count follows a rung. Nobody has. The books stay open, separate, and honest.

---

## Tier 5.28 — The Inversion and the Multi-Transition Consistency

### AT.57 — The reduced read from the carried energy

**Thm.**
$$(1)\quad\textbf{the inversion row (Directive 4, row 1):}\qquad\text{from any one transition with }\Delta E_{n_i\to n_f}>0:\qquad m_r\ =\ \frac{2\,\Delta E_{n_i\to n_f}}{\varepsilon_{\mathrm{EM}}^{2}\ \Bigl(\dfrac{1}{n_f^{2}}-\dfrac{1}{n_i^{2}}\Bigr)}\qquad[\text{machine: the algebraic inversion at witnesses}]:$$
$$\text{domain: }n_i>n_f\ge1;\qquad\varepsilon_{\mathrm{EM}}\ne0;\qquad\Delta E_{n_i\to n_f}>0\ \text{(the downhill bookkeeping)};\qquad\text{symbolic dependence: }m_r\propto\varepsilon_{\mathrm{EM}}^{-2}\ \text{— the separation of }m_r\ \text{and}\ \varepsilon_{\mathrm{EM}}\ \text{consumes the coupling read, } \neg\ \text{issued}\qquad[\mathrm{C\text{-}AT.3};\ \mathrm{C\text{-}AT.4}];$$
$$(2)\quad\textbf{the consistency row (Directive 4, row 2):}\qquad\text{for two independent transitions, the exact identity:}$$
$$\boxed{\ \frac{\Delta E_{n_i\to n_f}}{\dfrac{1}{n_f^{2}}-\dfrac{1}{n_i^{2}}}\ =\ \frac{\Delta E_{n'_i\to n'_f}}{\dfrac{1}{n_f'^{2}}-\dfrac{1}{n_i'^{2}}}\ =\ \frac{\kappa}{2}\ }\qquad[\text{machine: the identity at witnesses across the six table transitions}]:$$
$$\text{the ratio is transition-independent; it is independent of }\varepsilon_{\mathrm{EM}}\ \text{and }m_r\ \textbf{separately — neither enters alone: the ratio is the pair's own product read } \kappa/2,\ \text{defined whatever the factors are}\qquad[\mathrm{AT.6}(4)\text{'s coupling-free shape};\ \text{machine: the shape-ratio rows}];$$
$$(3)\quad\textbf{the product row:}\qquad\text{from any one transition, the pair read closes without consuming a coupling value:}$$
$$\kappa\ =\ 2\,\Delta E_{n_i\to n_f}\cdot\frac{n_i^{2}\,n_f^{2}}{n_i^{2}-n_f^{2}}\qquad[\text{machine: the identity at witnesses}]:\qquad\textbf{the pair read is operational — read off the carried energies and the rung labels alone};$$
$$\text{what the product does not give: }m_r\ \text{alone, }\varepsilon_{\mathrm{EM}}\ \text{alone — the separation is read-relative}\qquad[\mathrm{C\text{-}AT.4}];$$
$$(4)\quad\textbf{the [EXT] quarantine (Directive 4, row 5):}\qquad\text{external photon energies, if supplied later, test the consistency row (2) as audit inputs only: they enter no Thm clause, calibrate no symbol, and attach to no corpus value}\qquad[0.2\mathrm{e};\ \mathrm{P5};\ \mathrm{C\text{-}AT.4}]:$$
$$\text{the consistency row is the corpus-native form the external combination principle shadows — derived here from the ladder and the transition ledger, } \neg\ \text{imported};$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\neg\ \text{a calibration},\ \neg\ \text{a coupling value},\ \neg\ \text{an [EXT] datum in any Thm clause (the audit discipline)}\ [\mathrm{P5}].$$

**Req.** C10 (Part 1); P1, P5 (Parts 1–2); C-AT.3, C-AT.4 (this part, §Cal-5e); AT.6(1), AT.6(4), AT.8(2), AT.14(1), AT.48(2), AT.56(1) (this part); exact rational witness identities in the symbol ring, the shape-ratio rows [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \Delta E=\tfrac{\kappa}{2}s\ \text{with }s:=\tfrac1{n_f^2}-\tfrac1{n_i^2}\ \text{[AT.14(1)]};\ \tfrac{2\Delta E}{\varepsilon^2 s}=\tfrac{2(\varepsilon^2 m_r/2)s}{\varepsilon^2 s}=m_r\ \ \text{[machine: the cancellation in the symbol ring at witnesses]}
$$
$$
(2):\ \tfrac{\Delta E}{s}=\tfrac{\kappa}{2}\ \text{for all six table transitions at witnesses [machine]};\ \tfrac{\Delta E_{2\to1}}{\Delta E_{3\to2}}=\tfrac{s_{2\to1}}{s_{3\to2}}=\tfrac{27}{5}\ \text{[machine: the shape-ratio independence]};\qquad(3):\ 2\Delta E\cdot\tfrac{n_i^2n_f^2}{n_i^2-n_f^2}=2\cdot\tfrac{\kappa}{2}\cdot\tfrac{n_i^2-n_f^2}{n_i^2n_f^2}\cdot\tfrac{n_i^2n_f^2}{n_i^2-n_f^2}=\kappa\ \ \text{[machine]}
$$
$$
(4),(5):\ \text{the quarantine and status records}.\ \blacksquare
$$

**Phys.** One transition hands you a product; two hand you a law. The inversion is one line of algebra — the shape divides out and the reduced read remains, inverse-square in the coupling — but the consistency row is the load-bearing member: every downhill transition's energy divided by its shape lands on the same exact rational multiple, so the carried energies know about each other without any channel between them except the ladder they fell down. That self-consistency is the corpus-native form of the combination structure the identification layer observes in spectral line lists, and it is derived here, not borrowed: it is what a one-parameter ladder of exact rationals does. The product read is operational in the strictest sense — rung labels and carried energies, nothing else — and it stops exactly where the honest stopping point is: at the product. Which factor is the coupling and which is the mass is a separation no carried photon performs.

---

## Tier 5.29 — The Lepton Rest Read and the Koide Reconciliation

### AT.58 — The extraction: from the pair read to the floor read

**Thm.**
$$(1)\quad\textbf{the extraction identity (Directive 4, row 3, the pair bookkeeping):}\qquad\text{the strict-currency reduced-mass identity holds inside the }(\ln2/\mathfrak h)\ \text{currency}\qquad[\mathrm{AT.41}(3)]:\qquad\frac1{m_r}=\frac1{m_N}+\frac1{m_\ell}:$$
$$\text{count route: }m_N=\frac{6A\ln2}{\mathfrak h}\ \ [\mathrm{AT.3}(1);\ \mathrm{AT.5}(3)];\qquad m_r^{(A)}=\frac{6A\ln2}{\mathfrak h\,(3A+1)}\ \ [\mathrm{AT.5}(3)]:\qquad\boxed{\ m_\ell\ =\ \frac{3A+1}{3A}\cdot m_r^{(A)}\ }\qquad[\text{machine: the identity at }A\in\{1,2,3,7\}]:$$
$$\text{at the re-priced pair row }m_r=\frac{6\ln2\,(1+c\,\varepsilon_{\mathrm{EM}})}{\mathfrak h\,(4+3\,c\,\varepsilon_{\mathrm{EM}})}\ \ [\mathrm{AT.5}(1)]:\qquad\boxed{\ \frac{m_\ell}{m_r}\ =\ \frac{4+3\,c\,\varepsilon_{\mathrm{EM}}}{3\,(1+c\,\varepsilon_{\mathrm{EM}})}\ }\qquad[\text{machine: the cleared monomial in the symbol ring}]:$$
$$\text{the extraction consumes no coupling value: the count-route identity is exact in }(\ln2,\mathfrak h,A)\ \text{alone;}$$
$$(2)\quad\textbf{the four-object census (Directive 4, row 3):}\qquad\text{the exact relationship among the four reads:}$$
$$\begin{array}{l|l|l}\text{read} & \text{locus} & \text{relation to the others}\\\hline m_r\ \text{(transition-derived)} & \text{the pair's reduced read — operational [AT.57]} & \tfrac{m_\ell}{m_r}=\tfrac{4+3c\varepsilon}{3(1+c\varepsilon)}\ \text{[row (1)]};\ \text{count route: } m_r^{(A)}=\tfrac{3A}{3A+1}\,m_\ell\\\hline m_\ell\ \text{(digon floor read)} & \text{the lepton's own seal count — }m_\ell\mathfrak h=2\ln2\ \ [\mathrm{AT.4}(1)] & \text{the extraction's target; present in both cycle poles [AT.56(2)]}\\\hline b\ \text{(pair binding share)} & \text{the ground binding }b:=|E_1|=\kappa/2\ \ [\mathrm{AT.47}(4)\,\mathrm{(ii)}] & \tfrac{b}{m_\ell}=\tfrac{3\varepsilon^{2}(1+c\varepsilon)}{2(4+3c\varepsilon)}\ \ [\mathrm{AT.47}(4)\,\mathrm{(iii)};\ \text{machine]}\\\hline\text{the identification-layer label} & \neg\ \text{a corpus row} & \text{attaches (if ever) by a declared naming map [row (3)]}\end{array}$$
$$\textbf{verdict: different loci of one object — the pair's mass bookkeeping — related by exact monomials; } \neg\ \text{identical reads; } \neg\ \text{barred from conversion: the conversions are currency-internal algebra in }(\ln2/\mathfrak h)\qquad[\mathrm{AT.41}(3)\text{'s strict-currency row; machine: the token census — no cross-currency token in any identity]};$$
$$\text{BM.83/BM.69(4) bar count-to-strength and cross-currency routes — } \neg\ \text{the pair's internal reduced-mass identity; the item-7 relating equation is consumed by none of the monomials above}\qquad[\mathrm{AT.4}(3)\text{'s residue untouched; machine]};$$
$$(3)\quad\textbf{the candidate row (Directive 4, row 4):}\qquad\text{the strongest allowed candidate for the read the identification layer may later label }m_e\ \text{— recorded as a status table, } \neg\ \text{a value:}$$
$$\begin{array}{l|l}\text{status} & \text{the content}\\\hline\textbf{derived} & \text{the floor read }m_\ell\mathfrak h=2\ln2\ \text{stands [AT.4(1)]; the extraction identity (1) is new and derived: the transition route closes the circuit from the carried energies through the pair read to the floor read}\\\hline\textbf{read-relative} & \text{the separate reads }m_r\ \text{and}\ \varepsilon_{\mathrm{EM}}\ \text{(the product } \kappa \text{ is what the photons give [AT.57(3)])}\\\hline\textbf{barred} & \text{any promotion of the extraction to the family scale }\mu_\ell\text{: the four grounds apply verbatim at this locus [AT.51(3); BM.69(4)]}\\\hline\textbf{owed} & \text{the naming declaration that would attach the label: an A-AT-class declaration extending the identification-layer naming scope to the floor reads, in A-AT.2's pattern — issued at the Architect's discretion, } \neg\ \text{issued here; without it the label stays identification-layer}\ \ [\mathrm{FT.89}(2\mathrm a)\text{--}(2\mathrm c);\ 0.2\mathrm{d}]\end{array}$$
$$\neg\ \text{a number issued}\ [\mathrm{P5}];$$
$$(4)\quad\textbf{the closing equation (what the floors and the photons jointly fix):}\qquad\kappa=\varepsilon_{\mathrm{EM}}^{2}\,m_r\ \text{with the floor-scoped }m_r\ \text{is an exact implicit equation for the symbol pair }(c,\varepsilon_{\mathrm{EM}}):$$
$$6\,c\,\ln2\cdot\varepsilon_{\mathrm{EM}}^{3}\ +\ 6\ln2\cdot\varepsilon_{\mathrm{EM}}^{2}\ -\ 3\,c\,\kappa\,\mathfrak h\cdot\varepsilon_{\mathrm{EM}}\ -\ 4\,\kappa\,\mathfrak h\ =\ 0\qquad[\text{machine: the cleared identity at witnesses}]:$$
$$\text{at the count-route specialization }c=0\ \text{it closes exactly:}\qquad\varepsilon_{\mathrm{EM}}^{2}\ =\ \frac{\kappa\,\mathfrak h\,(3A+1)}{6A\,\ln2}\qquad[\text{machine: the exact solve at witnesses}]:$$
$$\textbf{the coupling squared is determined by the pair read and the floors as an algebraic consequence — and the value stays } \neg\textbf{ issued: the equation is a consistency structure, } \neg\textbf{ a calibration}\qquad[\mathrm{C\text{-}AT.3};\ \mathrm{C\text{-}AT.4};\ \mathrm{P5}];$$
$$(5)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(4);\qquad\neg\ \text{a new slot},\ \neg\ \text{a declaration},\ \neg\ \text{a measured mass},\ \neg\ \text{an inertial conversion}\ [\mathrm{P5};\ \mathrm{AT.4}(3)].$$

**Req.** P1, P5 (Parts 1–2); FT.44(4) (Census); FT.89(2a)–(2c) (Part 3); A-BM.9, BM.69(4), BM.83, BM.98 (Part 4); C-AT.3, C-AT.4, A-AT.2 (this part); AT.3(1), AT.4(1), AT.4(3), AT.5(1), AT.5(3), AT.41(3), AT.47(4), AT.51(3), AT.56(2), AT.57(3) (this part); exact rational witness identities in the symbol ring, the cleared cubic, the token censuses [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \tfrac{3A+1}{3A}\cdot\tfrac{6A\ln2}{\mathfrak h(3A+1)}=\tfrac{2\ln2}{\mathfrak h}=m_\ell\ \ \text{[machine at }A\in\{1,2,3,7\}\text{]};\qquad\tfrac{m_\ell}{m_r}=\tfrac{2\ln2/\mathfrak h}{6\ln2(1+c\varepsilon)/(\mathfrak h(4+3c\varepsilon))}=\tfrac{4+3c\varepsilon}{3(1+c\varepsilon)}\ \ \text{[machine: cleared in the symbol ring]}
$$
$$
(2):\ \text{the census table against the cited rows [machine: the document pins]};\ \text{the token census of the three monomials: }(\ln2,\mathfrak h,c,\varepsilon,A)\text{-terms only [machine]};\qquad(3):\ \text{the status-table record [machine: the document pins]}
$$
$$
(4):\ \varepsilon^{2}\cdot\tfrac{6\ln2(1+c\varepsilon)}{\mathfrak h(4+3c\varepsilon)}=\kappa\iff6c\ln2\,\varepsilon^{3}+6\ln2\,\varepsilon^{2}-3c\kappa\mathfrak h\,\varepsilon-4\kappa\mathfrak h=0\ \ \text{[machine: the cleared identity at witnesses]};\qquad c=0:\ \varepsilon^{2}=\tfrac{\kappa\mathfrak h(3A+1)}{6A\ln2}\ \ \text{[machine: the exact solve]};\qquad(5):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The circuit everyone wanted closed closes here, and it closes inside one currency. The photons hand over the product read; the pair bookkeeping converts the product to the reduced read; the reduced read and the nucleus's count-route read hand over the floor read — three steps, each an exact monomial in symbols the corpus already carries, and not one of them a coupling value or a measured number. The four-object census is the honesty row: the transition read, the floor read, the binding share and the identification-layer label are four loci of one mass bookkeeping, related by monomials, identical in none of their pairs, and barred from nothing they actually do — because what they do is internal algebra, not the cross-currency extraction the Part-4 bars were built to stop. The item-7 residue sleeps through the whole derivation, exactly as it should: nothing here converts information to inertia. What remains owed is one declaration — the naming map — and one discipline: the coupling equation that the floors and the photons jointly spell out is a consistency structure, not a calibration, and no root of it is a value.

### AT.59 — The Koide reconciliation: the scale bar stands, the extraction is new

**Thm.**
$$(1)\quad\textbf{the adjudication row (Directive 5, the four-way question):}$$
$$\begin{array}{l|l}\text{question} & \text{verdict}\\\hline\text{is the shell-transition-derived read the same object as }\mu_\ell\,? & \neg:\ \mu_\ell\ \text{is the family-channel scale [Cal-F], dimensionful }[\mu_\ell]=\mathfrak q^{+1/2}\ \ [\mathrm{AT.51}(3)\,\mathrm{(i)}];\ \text{the extracted read is the floor read }m_\ell,\ \text{informational, }\mathfrak h\text{-denominated }[\mathrm{AT.4}(1)]\\\hline\text{same read species?} & \neg:\ \text{pair-borne operational extraction [AT.57; AT.58(1)] vs family-channel scale}\\\hline\text{does the route require }\mu_\ell\,? & \neg:\ \text{the extraction is currency-internal and consumes no family scale — the pair-borne operational read, the directive's option (3)}\\\hline\text{blocked by the item-7 obstruction?} & \neg\ \text{for the extraction itself (no inertial conversion consumed [AT.4}(3)\text{])};\qquad\textbf{yes — verbatim — for any promotion of it to }\mu_\ell\ \ [\mathrm{AT.51}(3)\,\mathrm{(ii)}\text{--}\mathrm{(iv)};\ \mathrm{BM.69}(4);\ \mathrm{BM.83}]\end{array}$$
$$(2)\quad\textbf{the novelty row (what AT.51 did not cover):}\qquad\text{AT.51's honorific clause named what the observation layer derives: the defect read and the binding-share ladder}\qquad[\mathrm{AT.51}(3)\text{'s honorific clause}]:$$
$$\text{the extraction identity closes the circuit one book further — from the carried photon energies through the pair read to the floor read — a bridge AT.51 did not form;}$$
$$\text{it is currency-internal }[\mathrm{AT.41}(3)],\ \text{consumes no slot }[\S\mathrm{Cal}\text{-}5\mathrm{e}],\ \text{and re-derives the standing floor read pair-relatively: } \neg\ \text{a new scale, } \neg\ \text{a new object};$$
$$(3)\quad\textbf{the bar restated (Directive 5's refutation clause):}\qquad\text{any reading of the extraction as ``}\mu_\ell\ \text{derived from shell changes'' is the barred scale renamed:}$$
$$\boxed{\ \text{the four grounds — field degree, two-torsion image, calibration weight, strength bar — apply verbatim to any count-to-scale route at this locus}\ }\qquad[\mathrm{BM.69}(4);\ \mathrm{AT.51}(3)]:$$
$$\text{the Koide weights stay the seal bilinear's own spectrum}\qquad[\mathrm{AT.51}(1)]:\qquad\text{the shell ladder's rungs and the Koide triplet are both configuration reads at different loci — } \neg\ \text{identified without a declared map}\qquad[\mathrm{FT.89}(2\mathrm a)\text{--}(2\mathrm c);\ \mathrm{AT.51}(4)];$$
$$(4)\quad\textbf{the status:}\qquad\text{derived: }(1)\text{--}(3);\qquad\text{the scale bar of AT.51 stands, extended in domain to the extraction route; the extraction stands as the route's own new content};\qquad\neg\ \text{a revoked bar},\ \neg\ \text{a renamed scale}\ [\mathrm{P5}].$$

**Req.** D0.4 (Parts 1–2); CT2.1 (Part 2); P1, P5 (Parts 1–2); Cal-F (registry); FT.89(2a)–(2c) (Part 3); BM.69(4), BM.83 (Part 4); AT.4(1), AT.4(3), AT.41(3), AT.51(1), AT.51(3), AT.51(4), AT.57, AT.58(1) (this part); the exponent algebra, the token censuses [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \text{the kind row: }[\mu_\ell]=\mathfrak q^{1/2}\ \text{vs }[m_\ell\mathfrak h]=\mathfrak q^{0}\ \text{[machine: the exponent arithmetic; AT.51(3)(i)'s algebra]};\ \text{the species and requirement rows re-cited [AT.57; AT.58(1)]}
$$
$$
(2):\ \text{the honorific clause re-cited; the circuit census: the extraction's three steps are currency-internal [machine: the token census of AT.58(1)'s identities]};\qquad(3):\ \text{the four grounds re-cited verbatim; the identification bar re-cited [FT.89(2a)--(2c)]};\qquad(4):\ \text{the status record}.\ \blacksquare
$$

**Phys.** The reconciliation is a verdict of separation, and a useful one. The Koide row's barred scale and the shell-transition route's extracted read were never competitors: one is a family-channel scale, dimensionful, waiting on a declared conversion that four standing grounds keep waiting; the other is the floor read arriving by a new road — carried energies, pair bookkeeping, count route — and arriving exactly where the digon left it two ln 2 over 𝔥. The route is genuinely new (AT.51's honorific clause stopped at the defect and the ladder; this one walks the last book), genuinely safe (every step is currency-internal algebra), and genuinely incapable of smuggling the barred scale through, because the road never leaves the informational currency at all. The bar survives with its domain extended; the extraction survives as the route's own yield; and the identification-layer label waits on exactly one declaration — the same kind of honest debt the audit rows have carried since the first tier learned to record what it could not yet build.

---

## Tier 5.30 — The Integration Audit

### AT.60 — The audit: the substrate, the bridges, the era-locality additions, and the owed-row register

**Thm.**
$$(1)\quad\textbf{the substrate row:}\qquad\text{the enumerative substrate is unchanged — the 25 cells, consumed by tag citation [AT.52(1) re-run; machine: the partition re-run; no cell added]};$$
$$(2)\quad\textbf{the intact-bridge row:}\qquad\text{the EM sealing grammar stands — the cycle adds no EM row; it consumes EM.5--EM.8 at the carrier and jaw loci}\ [\mathrm{A\text{-}AT.1};\ \mathrm{AT.23}\text{--}\mathrm{AT.24}];$$
$$\text{the scope clock stands — the bridge-open phase's probing is the scope clock's row at the transit interval }[\mathrm{AT.29};\ \mathrm{AT.30}];\qquad\text{the unified mass read stands — the pole moves along its own ladder only }[\mathrm{Def\text{-}AT.7};\ \mathrm{AT.56}(2)];$$
$$\text{the width ledger absorbs the cycle — the bracket opens at emission's probe and re-closes at reception }[\mathrm{AT.30}(2),(3)];\qquad\text{the collapse channel is untouched — the cycle adds no strong-side row }[\mathrm{Def\text{-}AT.9};\ \mathrm{AT.40}];$$
$$\text{the currency bridge is untouched — the extraction is currency-internal }[\mathrm{AT.41}(3);\ \mathrm{AT.58}(2)];$$
$$(3)\quad\textbf{the era-locality additions (two rows join the table, same discipline [AT.36's pattern; AT.52(3)]):}$$
$$\begin{array}{l|l|l|l}\text{obstruction} & \text{binds in} & \text{the bridge} & \text{status}\\\hline\text{no persistent observer leg} & \text{the connected read as a durable state} & \text{the five-phase cycle and the disconnection theorem [AT.54(5)]} & \text{re-scoped: Def-AT.10(2)'s connected read is the bridge-open phase's read-side book, } \neg\text{ a persistent state}\\\hline\text{the one-way bar} & \text{joint reads across disjoint subnetworks} & \text{the roundtrip closure condition; the return leg owed [AT.55(2), AT.55(5)]} & \text{re-scoped: one-way content carries and registers; joint correlation does not close}\end{array}$$
$$(4)\quad\textbf{the conservation row:}\qquad\mathfrak M_{n_i}\ =\ \mathfrak M_{n_f}\ +\ \Delta E_{n_i\to n_f}\qquad\text{exactly across every cycle, no term attaching to any free member}\qquad[\mathrm{BM.48}(4),(5);\ \text{machine: the identity at witnesses over the six table transitions]};$$
$$(5)\quad\textbf{the calibration consolidation:}\qquad\text{the extension adds no declared slot, no declaration, no dimensionful scale, no P4 member, no measured value}\qquad[\mathrm{P1};\ \mathrm{P4};\ \mathrm{P5};\ \S\mathrm{Cal}\text{-}5\mathrm{e};\ \mathrm{C\text{-}AT.4}];$$
$$(6)\quad\textbf{the owed-row register (named, } \neg\textbf{ filled):}\qquad\text{(i) the exact return leg — the observer-side emission cycle }[\mathrm{AT.55}(5)];\qquad\text{(ii) the permanent-chart disposition of the provisional class Def-AT.11 }[\mathrm{Def\text{-}AT.11}(4)];$$
$$\text{(iii) the } \tau_n(n)\ \text{map between the two books }[\mathrm{AT.56}(4)];\qquad\text{(iv) the naming declaration for the identification-layer mass label }[\mathrm{AT.58}(3)];$$
$$(7)\quad\textbf{the status:}\qquad\text{derived and recorded; machine: }`\text{checks/verify\_Atomic5.py}`\ \S\mathrm{W}].$$

**Req.** P1, P4, P5 (Parts 1–2); EM.5–EM.8 (Part 2); BM.48(4), BM.48(5) (Part 4); A-AT.1, Def-AT.7, Def-AT.9, Def-AT.11, AT.23–AT.24, AT.29, AT.30, AT.36, AT.40, AT.41(3), AT.52, AT.54(5), AT.55(2), AT.55(5), AT.56(2), AT.56(4), AT.58(2), AT.58(3), C-AT.4 (this part); exact set arithmetic, witness identities, the partition re-run [math; machine: `checks/verify_Atomic5.py` §W].

**Pf.**
$$
(1):\ \text{the partition re-run over the six families; }11+5+1+2+5+1=25\ \text{[machine]};\qquad(2):\ \text{the six bridge rows re-cited at their loci}
$$
$$
(3):\ \text{the two table rows [AT.36's four-column discipline]};\qquad(4):\ \mathfrak M_{n_i}-\mathfrak M_{n_f}-\Delta E_{n_i\to n_f}=0\ \text{at witnesses for all six transitions [machine; the symbol census: no free-member token]}
$$
$$
(5):\ \text{the register record [P1; P4; P5; §Cal-5e; C-AT.4]};\qquad(6):\ \text{the owed-row register [machine: the document pins]};\qquad(7):\ \text{assembly}.\ \blacksquare
$$

**Phys.** The audit closes the way the era's audits close: nothing outside the books, nothing moved that a frozen row does not license. The same twenty-five spaces feed the cycle — the carrier class once more, now timed in phases; the closure arithmetic once more, now as the roundtrip's condition; the pair bookkeeping once more, now run in reverse, from photons back to floors. Every bridge passes intact: the cycle loads no cap, wakes no sector, crosses no currency, and leaves the width ledger holding exactly the bracket movements it has always held — opened at the emission, closed at the reception, floor-locked in between. Two rows join the era-locality table, and they are the tier's whole confession: the observer keeps no leg, and one-way correlation does not close. Four debts are on the register, each named at its own locus, none forced. And the books balance where they always balanced — pole to pole plus the carried difference, exactly, at every rung the table walks.

---

## Closure exports of the emission-cycle extension (Tiers 5.24–5.30; consumed by no part of the canon)

$$
\begin{array}{c|c}
\text{export} & \text{the row}\\\hline
\text{the premise audit} & \text{every cited tag present with sub-rows; D-RS }\neg\text{canonical [token census]; the five terms located; the false row barred [AT.53]}\\
\text{the bridge-open phase} & \text{the provisional structural class: real chain, sealed ends; four negations; owed marks [Def-AT.11]}\\
\text{the five-phase cycle} & \rho_\circ=\tfrac14I\ \text{observer-relative }E_{\mathrm{vis}}=0;\ \text{forced carrier;} \ \mathsf E\le\min(\delta h,4\delta\tau)\ln2\ \text{(the register book); the disconnection theorem; } \mathfrak M_{n_i}=\mathfrak M_{n_f}+\Delta E\ \text{[AT.54]}\\
\text{the roundtrip closure} & \mathsf E_{\mathrm{bd}}=0\ \text{one-way; closed book = closed chain; the digon condition; the four no-go rows; } \boxed{\text{observation closes only on a roundtrip}}\text{; the return leg owed [AT.55]}\\
\text{the transition table} & \Delta E_{n_i\to n_f}=\tfrac{\kappa}{2}\bigl(\tfrac{1}{n_f^2}-\tfrac{1}{n_i^2}\bigr);\ \text{the six shapes exact; the grid positive; the defect bookkeeping (no }M,\ m_\ell\text{ term); } m'=m;\ \text{the two books distinct [AT.56]}\\
\text{the inversion and consistency} & m_r=\dfrac{2\Delta E}{\varepsilon_{\mathrm{EM}}^2\bigl(\tfrac{1}{n_f^2}-\tfrac{1}{n_i^2}\bigr)};\ \ \tfrac{\Delta E}{\text{shape}}=\tfrac{\kappa}{2}\ \text{transition-independent; }\ \kappa=2\Delta E\cdot\tfrac{n_i^2n_f^2}{n_i^2-n_f^2}\ \text{operational [AT.57]}\\
\text{the extraction} & m_\ell=\tfrac{3A+1}{3A}\,m_r^{(A)};\ \ \tfrac{m_\ell}{m_r}=\tfrac{4+3c\varepsilon}{3(1+c\varepsilon)};\ \ \tfrac{b}{m_\ell}=\tfrac{3\varepsilon^2(1+c\varepsilon)}{2(4+3c\varepsilon)};\ \ \text{the four-object census; the status table (derived / read-relative / barred / owed); the closing cubic; } c{=}0:\ \varepsilon^2=\tfrac{\kappa\mathfrak h(3A+1)}{6A\ln2}\ \text{[AT.58]}\\
\text{the Koide reconciliation} & \text{the extraction } \ne\mu_\ell\ \text{(kind, species, no requirement); the option-(3) verdict; the four grounds verbatim on any promotion; AT.51(3) stands [AT.59]}\\
\text{the era-locality additions} & \text{no persistent observer leg; the one-way bar — both re-scoped at their loci [AT.60(3)]}
\end{array}
$$
