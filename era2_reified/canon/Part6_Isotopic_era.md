# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Unified Schema

**Level.** 6. **Era.** 2 (the Isotopic era).
**Dep.** Part 5 (unified AT.1–AT.63 + DJ_AT.1–DJ_AT.17); Part 1–4 (Parts 1–4 canon); Census.md.
**Source.** Merged from tier files Part6_Isotopic_era_TierIT1.md through Part6_Isotopic_era_TierIT26.md.

**Unified Tiers** (3 tiers, logical ordering):
- **IT.01**: Measurement Theorem & Isotopic Family (IT.1–IT.10)
- **IT.02**: Amplitude Adjudications, Declaration Package, Handshake-Ladder (IT.11–IT.21)
- **IT.03**: Translation Layer, n-fold Radar/DFT, Seal Parity, Carrier Read (IT.22–IT.26)

**Tags.** IT.1–IT.26.

**Pattern.** The level-opening tier (Tier IT.1) mirrors Tier AT.1's shape: construction tags plus the level's §Cal and §Open sections.

**Status.** Discovery-phase working tiers. Nothing adopted into frozen canon; no declarations issued (except D-PJ1–6, D-RS1–3, D-RS6, D-RS7); §Cal-IT empty; no clause of Parts 1–4 or Level 5 modified.

**Open Rows.** IT-O1 (transit/dissociation, 3 grounds, deficit 1'), IT-O2 (binding value), IT-O5 (dynamical cutoff); owed declarations: D-PJ7 + 3 sub-debts, D-RS4 deferred.

**Closed Rows.** IT-O3, IT-O4, IT-O6.

**Machine.** `era2_reified/verification/checks/verify_Atomic5_6.py` — exact arithmetic: `Fraction`, `Gauss(i)` matrices, rigorous `Fraction` intervals, truncated `ℚ[[γ]]` series, integer certificates, exhaustive sign censuses.

**No floating point in any assertion. No measured value enters any clause [P5].**

**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record (AT-tags, DJ_AT-tags), and earlier IT-tags only. No forward pointer is used as a premise.

---

## Part 6 · Unified Isotopic Era


---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.1: the Measurement Theorem

**Level.** 6. **Era.** 2 (the Isotopic era — OPENED by this tier). **Tier.** IT.1 — the
Measurement Theorem in four clauses plus its calibration consequence: the rung hierarchy of
observation, the non-transit boundary, the entanglement dichotomy, and the molecular necessity.
**Tags.** IT.1–IT.5. **Pattern.** the level-opening tiers (Tier AT.1's shape): construction tags
plus the level's §Cal and §Open sections.
**Status.** discovery-phase working tier. Nothing is adopted into the frozen canon; no
declaration issues; §Cal-IT is empty; no clause of Parts 1–4 is modified, retracted or
renumbered; **Level 5's closed record [AT.63(2)] is cited, never edited.**
**Machine.** `era2/level6_isotopic/checks/measurement_theorem.py` → **21/21 exact**;
`era2/level6_isotopic/checks/run_all_level6.py` → the level's runner (gate first);
`era2/level6_isotopic/checks/check_level6_format.py` → the format + citation gate over the Part 6
documents, attesting against the era-1 canon registry AND the closed Level-5 record. Exact
arithmetic: `Fraction`, `Gauss(i)` $4\times4$, rigorous `Fraction` intervals for $\ln 2$
(`qexact`, borrowed from the Level-5 shared libraries), truncated $\mathbb Q[[\gamma]]$ series with
coefficient-wise equality, integer certificates, exhaustive sign censuses.
**No floating point in any assertion. No measured value enters any clause [P5].**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record (AT-tags), and earlier
IT-tags only. No forward pointer is used as a premise.
**Mandate.** The Architect's directive: *"Construct the Measurement Theorem — the rung hierarchy
of observation, the non-transit boundary, and the molecular necessity… All measurements humanity
has ever made are strictly confined to the reality of rung 1 measurements. A truly measured
boundary — an information-complete one — is one out of which no rung 2 or rung 3 or rung $D^-$
leaks. A rung 1 restricted system has a non-transit boundary; it doesn't radiate. As soon as a
thing radiates, it gets entangled with the observer or else goes completely vacuum-looking. We
need molecular, sadly."* — verified against the canon and assembled as a single derived theorem,
with the premise corrections recorded at IT.1(8).
**Nomenclature (inherited).** Def-BM.3(7)'s rule stands: *"molecular", "atomic", "photon"* stay
quoted names for the derived configuration classes, $\neg$species identifications. Prices are
$\neg$masses [HistLog §V.32]. The dictionary discipline stands: chart-side objects (collapse,
radiation, observers-with-consciousness) are $\neg$imported; the ledger's own primitives are the
A4 registration, the L0 tilt, and the Def-H.32 configuration sum.

---

### IT.1 — Clause 1: the rung hierarchy of observation — darkness is read-species separation

**Thm.**
$$(1)\quad\textbf{THE RUNG LADDER (re-produced,}\ \neg\textbf{new):}\qquad\mathcal A(0)=\{J\},\ \ \mathcal A(1)=\mathcal A(0)\cup\{G,W,H,D^+\},\ \ \mathcal A(2)=\mathcal A(1)\cup\{\mathrm{EM}\},\ \ \mathcal A(3)=\mathcal A(2)\cup\{\mathrm{strong}\},\ \ \mathcal A(n\ge4)=\mathcal A(3)\cup\{D^-\}\ \ [\mathrm{CT0.13}];$$
$$\textbf{the lock biconditional:}\ \ D^-\in\mathcal A(n)\iff n\ge4\iff2^{n+1}>16=C_{\mathrm{cap}}\iff\neg\text{admissible}\ \ (n{=}0..16\ \text{exhaustive})\ \ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT0.11};\ \mathrm{AT.50}(3),(4)];\qquad\dim\mathcal K_n=6,16,17,25,26\ \ [\mathrm{CT0.14};\ \mathrm{AT.50}(1)]$$
$$(2)\quad\textbf{THE OBSERVABILITY CENSUS}\ [\mathrm{FT.20}\ \text{and its Rmk}]:\qquad\begin{array}{l|l|l}\textbf{aspect}&\textbf{the activity criterion on any}\ \Sigma&\textbf{the locality}\\\hline\mathrm{EM}&\exists v\in\Sigma:\ f_v\ne0&\Sigma\text{-local, additive}\\\mathrm G\ (\text{mass})&I_{\mathrm{hid}}(\Sigma;o)\ne0&\text{OBSERVER-RELATIVE}\ [\mathrm{Def\text{-}H.9}]\\\mathrm H&\text{folded into}\ \mathrm G\ [\mathrm{Def\text{-}H.36}]&\text{as}\ \mathrm G\\\mathrm W\ (\text{spin})&\Theta_{\mathrm{int}}\ne0\implies\Sigma\setminus\partial\Sigma\ne\varnothing\ \text{(one-directional)}&\Sigma\text{-local}\\\mathrm{strong}&\mathrm{Colour}(\Sigma)\ne\varnothing\ \wedge\ \mathcal C=1&\text{GENUINELY GLOBAL}\ [\mathrm{FT.19};\ \mathrm{CT3.22}]\\J^\pm,\ D^+,\ D^-&\textbf{NEVER (independently)}&\text{structural/bookkeeping,}\ \neg\text{observables}\end{array}$$
$$\text{and the metric side: the}\ J^\pm\ \text{blocks carry ZERO metric coordinates (S-odd grading, machine-reproduced)}\ [\mathrm{CT1.12a}(2)];\qquad\text{colour itself is}\ \neg\text{observable}\ [\mathrm{CT3.22}]$$
$$(3)\quad\textbf{THE READ-CLASS CENSUS IS CLOSED}\ [\mathrm{CT1.12a}(3)]:\qquad(\mathrm R1)\ \text{binary registration:}\ \sigma_e\in\{\pm1\}\ [\mathrm{CT0.9}],\ \ q_{\mathrm{EM}}\in\{-1,0,+1\}\ [\mathrm{EM.9};\ \mathrm{D3.4}],\ \ \text{wall parity}\ (-1)^{\aleph}\ [\mathrm{D3.3}];$$
$$(\mathrm R2)\ \text{integer winding}\ \kappa,\Theta,k\ \text{on MATERIALIZED closed chains}\ [\mathrm{CT1.19b};\ \mathrm{FT.22}:\ \Theta\in2\mathbb Z];\qquad(\mathrm R3)\ \text{binary singlet admissibility}\ \mathcal C\in\{0,1\}\ [\mathrm{D2.14}];$$
$$\text{every further aspect datum is P4-continuous configuration data or structural non-observable — no fourth read class exists}$$
$$(4)\quad\textbf{DARKNESS IS READ-SPECIES SEPARATION (the clause's theorem, machine-exact):}\qquad\text{on EVERY sign configuration of chains}\ L{=}2..6\ (126,\ \text{exhaustive}):$$
$$\text{the EM criterion}\ \bigl[\exists\ \text{interior}\ v:\ f_v\ne0\bigr]\ \text{fires EXACTLY on the non-aligned configurations}\ (30/32\ \text{at}\ L{=}5);\qquad\text{the fully aligned pair per}\ L\ \text{is EM-INACTIVE with}\ q=0\ \wedge\ \aleph=0;$$
$$\textbf{and the geometric reads survive the darkness:}\ \ \Theta=\textstyle\sum_e\kappa_e=10\in2\mathbb Z\ \text{across ALL}\ 32\ \text{sign configurations of the fixed materialized}\ 5\text{-cycle —}\ \Theta\ \text{reads the MATERIALIZATION data}\ (\kappa_e)\ [\mathrm{D1.6}],\ \neg\text{the signs}\ [\mathrm{D0.5}];$$
$$\boxed{\ \textbf{a dark (EM-inactive) system is gravitationally real — its}\ E_{\mathrm{int}}\ \text{feeds}\ G=2\pi E^2\ln2,\ \text{the lapse, the shell}\ [\mathrm{BM.88}(3);\ \mathrm{BM.132};\ \mathrm{AT.35}]\ \textbf{— and charge-silent: no (R1) read of it can exist}\ }$$
$$(5)\quad\textbf{the interior-sensitivity witness, re-derived exactly}\ [\mathrm{AT.30}(3)]:\qquad14\ \text{of}\ 32\ \text{five-edge chains have}\ q=0\ \wedge\ \aleph>0\ \ \text{— FT.20's EM criterion is interior-sensitive while its observable is boundary-exact;}$$
$$\text{the criterion's}\ \Sigma\text{-locality and monotone additivity under disjoint union censured exactly}\ [\mathrm{FT.20}\ \text{EM-row}]$$
$$(6)\quad\textbf{THE HIERARCHY THEOREM PROPER:}\qquad\text{the inter-system registration read — the read by which one sealed register system registers another — is the}\ (\mathrm R1)\ \text{charge species:}\ q_{\mathrm{EM}}=\tfrac12(\sigma_{\text{first}}-\sigma_{\text{last}})\ \text{telescoped over the connector}\ [\mathrm{EM.9b};\ \mathrm{AT.41}(4):\ \text{all}\ 1016\ \text{assignments}];$$
$$\text{its formation requires EM activity}\ [\mathrm{FT.20}],\ \text{which activates at rung}\ 2\ [\mathrm{CT0.13}];\qquad(\mathrm R2)\ \text{is self-geometric (a system's own materialization, not a registration of another);}\qquad(\mathrm R3)\ \text{requires a colour seal (rung}\ \ge3,\ \text{global},\ \text{colour}\ \neg\text{observable itself});$$
$$\boxed{\ \textbf{every inter-system measurement is rung-2 mediated: the charge read is the FIRST and the ONLY registration species below rung 3, and rung 3's singlet bit arrives sealed and global}\ }$$
$$(7)\quad\textbf{the dark object's ledger — what it still has:}\qquad\text{mass reads}\ (m_{\mathrm{hid}}=I_{\mathrm{hid}}/\mathfrak h,\ \text{observer-relative}\ [\mathrm{Def\text{-}H.9}(2);\ \mathrm{FT.20}\ \mathrm G\text{-row}]);\quad\text{frame-drag}\ (\Theta_{\mathrm{drag}},\ \text{Diophantine-quantized}\ [\mathrm{AT.46}(4)]);\quad\text{lapse and shell}\ [\mathrm{BM.132};\ \mathrm{AT.35}];\quad\text{winding reads}\ (\mathrm R2);$$
$$\textbf{what it lacks:}\ \neg\text{a charge read},\ \neg\text{a wall read},\ \neg\text{a channel weight}\ (x_+^2\chi\ \text{needs the junction}\ [\mathrm{BM.122}(3)]),\ \neg\text{a registration by any other system}$$
$$(8)\quad\textbf{premise corrections, on the record (the house discipline):}\qquad(\mathrm P1)\ \text{the rung ladder is}\ \mathrm{CT0.13}\ \text{'s frozen row,}\ \neg\mathrm{AT.30}(7)\ (\mathrm{AT.30}\ \text{has clauses}\ (1)\text{--}(6);\ \text{its}\ (1)\ \text{is the per-aspect}\times\text{per-rung census});$$
$$(\mathrm P2)\ \text{``all measurements are confined to rung 1'' reads, on the derived rows, as its opposite: the charge-read floor is rung}\ 2\ [\mathrm{CT0.13};\ \mathrm{FT.20}]\ \text{— the directive's ``rung-1 restricted system'' is formalized as the EM-INACTIVE system (mask}\ \mathcal K_{n\le1}),\ \text{which is what the rest of the directive describes};$$
$$(\mathrm P3)\ \text{``it doesn't radiate'' is formalized as:}\ \neg\exists\ \text{a formed radiation leg from anything}\ [(\mathrm{R9}'');\ \mathrm{BM.122}(6)(\mathrm O1)\text{--}(\mathrm O4)]\ +\ \text{the non-transit mask census}\ (\mathrm{IT.2})\ \text{— the dynamical radiation leg stays OPEN as}\ \mathrm{IT\.ext{-}O1},\ \text{named}\ \neg\text{assumed};$$
$$(\mathrm P4)\ \text{``entanglement with the observer''}\ :=\ \text{the ledger composite (ONE global Def-H.32 configuration sum over system+register}\ [\mathrm{AT.42}(2)]);\ \ \text{``observer''}\ :=\ \text{a designated register/read apparatus}\ [\mathrm{Def\text{-}H.9}\ \text{'s}\ o;\ \mathrm{FT.20}\ \mathrm G\text{-row}]\ \text{—}\ \neg\text{consciousness,}\ \neg\text{a smooth-manifold analogy}$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (4)\text{--}(7);\qquad\textbf{re-produced:}\ (1)\text{--}(3);\qquad\textbf{corrections:}\ (8);\qquad\neg\text{a declaration},\ \neg\text{a P4 addition},\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)]$$

**Req.** A1, A4, A6, A8 (Part 1); P5, CT0.3, CT0.5, CT0.6, CT0.9, CT0.11, CT0.13, CT0.14, CT1.12a(2),(3), CT1.19b, CT3.22, D0.5, D1.6, D2.14, D3.3, D3.4, EM.9, EM.9b, EM.12, FT.19, FT.20, FT.22 (Parts 1–2); Def-H.9(2), Def-H.15, Def-H.32(1),(2), Def-H.36, FT.28 (Part 3); AT.29(2), AT.30(1),(3), AT.35, AT.41(4), AT.42(2),(3), AT.44, AT.46(4), AT.48(1),(2), AT.50(1),(3),(4),(5), AT.63(2) (Level 5, closed record); Def-BM.3(7), Def-BM.8(6), BM.88(3), BM.122(3),(6), BM.132, BM.143(1) (Part 4); exhaustive sign enumeration ($2^L$, $L\le6$), exact integer arithmetic [math; machine: `measurement_theorem.py` §B, 4/4].

**Pf.**
$$(1):\ \text{the ladder and the biconditional censused over}\ n{=}0..16;\ \text{the mask dimensions by the block census}\ [\text{machine B1}];\ (2),(3):\ \text{re-citation with the}\ S\text{-odd grading reproduced}\ (J_i,K_i\ \text{anti-invariant,}\ E_0,\Sigma,W_i,E^{ii}\ \text{invariant under the swap conjugation)}\ [\text{machine B3}];$$
$$(4):\ \text{the}\ 126\text{-configuration census with the exact correlations (EM-active}\iff\neg\text{aligned; aligned}\implies q{=}0\wedge\aleph{=}0)\ \text{and the sign-blindness witness}\ [\text{machine B2}];\ (5):\ \text{the}\ 14/32\ \text{count and the union-monotonicity census}\ [\text{machine B2,B3}];$$
$$(6):\ \text{assembly on}\ (3)\text{--}(5)\ \text{with the read-class value censuses}\ (q\in\{-1,0,1\},\ (-1)^\aleph\in\{\pm1\},\ \Theta\in2\mathbb Z,\ \mathcal C\in\{0,1\})\ [\text{machine B4}];\ (7),(8),(9):\ \text{record rows}.\ \blacksquare$$

**Phys.** Ask the ledger what it takes to see another system, and the answer is a census, not a
philosophy. The forces do not turn on together: the ladder activates them one by one, and the
first rung at which a *charge* exists to read is rung two. Below it, a system is dark — not
absent, not hypothetical: dark. It still carries its internal energy into the curvature lock,
still drags frames by a Diophantine-quantized winding, still owns every geometric read the
materialization data supports; what it cannot do is be registered, because the only registration
species below the colour seal is the boundary charge read, and the charge read needs a vertex
where the signs turn. The machine census makes the separation exact: the aligned configurations
are precisely the EM-inactive ones, and the winding read does not so much as glance at the signs.
The Architect's Earth is the illustration and it holds as one: before any photon scatters, the
Earth is a rung-one object — gravitationally real, electromagnetically dark — and the scattering
*is* the rung-two activation, the first vertex where a sign turns. (The illustration is flagged
as an illustration: the derived content is the census, the read classes, and the rung ladder, and
the corrections to the directive's own premises are recorded beside them — the corpus's habit
since its first tier.)

---

### IT.2 — Clause 2: the non-transit boundary is the measurement horizon

**Thm.**
$$(1)\quad\textbf{DEFINITION (derived content, no new datum):}\qquad\text{a boundary}\ \partial\Sigma\ \text{is}\ \textbf{truly measured / information-complete}\ \iff\ \text{the active mask}\ \mathcal K_\Sigma(C)=\bigoplus_{A\in\mathcal A(\Sigma;C)}\mathcal K^{(A)}\ [\mathrm{Def\text{-}H.15}(1)\text{--}(3);\ \mathrm{AT.29}(2)]\ \text{carries}\ \neg\text{a rung}\ge2\ \text{summand out of}\ \Sigma\ \text{and the accessible content equals AT.32(1)'s functional EXACTLY};$$
$$\text{a}\ \textbf{rung-1 restricted system}\ :=\ \text{EM-inactive}\ [\mathrm{FT.20}:\ \neg\exists v\ f_v\ne0]\ \wedge\ \text{colourless}\ \implies\ \mathcal A(\Sigma;C)\subseteq\mathcal A(1)\ \implies\ \dim\mathcal K_\Sigma\le16$$
$$(2)\quad\textbf{NOTHING LEAKS (the mask arithmetic):}\qquad\text{for}\ \mathcal A\subseteq\mathcal A(1):\ \ \mathrm{EM}\ (1),\ \mathrm{strong}\ (8),\ D^-\ (1)\ \text{summands are ABSENT from}\ \mathcal K_\Sigma\ \text{— there is no rung}\ge2\ \text{content in the mask to leak};$$
$$D^-\ \text{is masked at EVERY accessible rung (the lock biconditional,}\ n{=}0..16)\ \text{and even at its formal unlocking is structureless}\ [\mathrm{CT4.2};\ \mathrm{CT4.4};\ \mathrm{AT.50}(5)];\qquad\dim\mathcal K_1=3{+}3{+}5{+}3{+}1{+}1=16\ \text{exactly}\ [\mathrm{CT0.12}]$$
$$(3)\quad\textbf{INFORMATION-COMPLETE = AT.32(1) ITSELF:}\qquad\boxed{\ \text{the accessible content of ANY bounded}\ \Sigma\ \text{is a function of (the boundary-data triple,}\ |R|,\ \text{the rung}\ n)\ \textbf{and NOTHING ELSE}\ }$$
$$\text{the triple}:=\ (\text{charge class},\ \Theta_{\mathrm{int}}\ \text{class},\ S\ \text{winding class})\ [\mathrm{Def\text{-}BM.3}(2)\text{--}(3);\ \mathrm{BM.2}(1);\ \mathrm{Def\text{-}H.32}(4);\ \mathrm{Def\text{-}BM.5}(1)];\qquad\text{every other datum is bounded out by exactly one of}\ (\mathrm P1)/(\mathrm P2)/(\mathrm P3)\ [\mathrm{AT.32}(2)\ \text{'s table, re-cited}]$$
$$(4)\quad\textbf{(P1) THE VISIBILITY BOUND, witnessed:}\qquad E_{\mathrm{tot}}=|\Sigma|\ln2,\quad E_{\mathrm{vis}}=\min(\delta h,4\delta\tau)\ln2\ \ \text{on the CT0.3 increments}\ \pm(1,1,1):\qquad I_{\mathrm{hid}}=E_{\mathrm{tot}}-E_{\mathrm{vis}}\ \text{is an exact non-negative integer multiple of}\ \ln2\ \text{on every cell};$$
$$m_{\mathrm{hid}}=I_{\mathrm{hid}}/\mathfrak h\ \ [\mathrm{Def\text{-}H.9}(2);\ \mathrm{FT.1};\ \mathrm{CT0.9};\ \mathrm{CT1.29}]\ \text{— what a boundary read can see is COUNTED before any dynamics}$$
$$(5)\quad\textbf{(P3) THE VOID CLOSURE:}\qquad\text{``the internal constituent states of a sealed composite are}\ \neg\text{knowable BY THEOREM, and NO CONSTRUCTION COULD EXIST INSIDE THE BOUND''}\ \ [\mathrm{BM.143}(1);\ \mathrm{AT.29}(3),(4)];$$
$$\textbf{PRESERVED BUT INACCESSIBLE, exhibited:}\ \ \text{the}\ L{=}5\ \text{pair}\ (+1{+}1{+}1{+}1{+}1)\ \text{vs a}\ q{=}0,\aleph{>}0\ \text{member of the}\ 14\ \text{— IDENTICAL boundary data}\ (q{=}0\ \text{at both ends}),\ \text{DIFFERENT interior activity: the interior information exists, is conserved by the ledger's bookkeeping}\ [\mathrm{D0.7}:\ \text{every edge registered}],\ \text{and provably cannot reach the boundary}$$
$$(6)\quad\textbf{THE BOUNDARY IS WHERE THE SHELL BEGINS}\ [\mathrm{AT.35}(0)\text{--}(3);\ \mathrm{BM.148}(1),(4)]:\qquad\text{chart-formed}\iff r\ge r_s;\qquad\text{the shell}\ k:=r/\Delta x_{\mathrm B}\in(1,\ k_{\mathrm{crit}}),\quad k_{\mathrm{crit}}=\tfrac{E^2\ln2}2=\tfrac G{4\pi},\quad\textbf{LEDGER-FORMED, CHART-UNFORMED};$$
$$N^2=1-\tfrac{k_{\mathrm{crit}}}k<0\ \ \text{inside}\ \ [\mathrm{BM.132}(2);\ \mathrm{BM.146}(3)]:\ \ \text{the chart's own lapse fails before the boundary is reached};\qquad\textbf{non-emptiness at the minimal floor:}\ \ k_{\mathrm{crit}}(E{=}2)=2\ln2=\ln16>2>1\ \ [\text{machine: rigorous}\ \texttt{qexact}\ \text{interval}]$$
$$(7)\quad\textbf{IT DOESN'T RADIATE (the derived content of the directive's row):}\qquad\text{bound}:=\ \text{closed self-contained chains, transit}:=\ \text{propagating open chains}\ [\mathrm{D1.5}];\qquad\text{the pair channel's weight is}\ x_+^2\,\chi_{\{NE\ge\mathcal T_0\}}\ \ [\mathrm{BM.122}(3)]:$$
$$\text{a dark system has NO junction}\ (x_+^2\ \text{never enters)}\ \wedge\ \text{the two-transit-quantum supply vertex is refuted as formed on four grounds}\ [(\mathrm{R9}'');\ \mathrm{BM.122}(6)(\mathrm O1)\text{--}(\mathrm O4)]\ \implies\ \neg\exists\ \text{a formed radiation leg};$$
$$\text{the weight census:}\ x_+^2=1\ \text{only at}\ \varepsilon_q=0\ \wedge\ NE\ge\mathcal T_0;\quad x_+\to0\ \text{at}\ \varepsilon_q\to\tfrac14^-\ \ \text{— the two limits are opposite and both exact}\ [\mathrm{BM.122}(3)]$$
$$(8)\quad\textbf{THE MEASUREMENT-HORIZON ROW (assembly):}\qquad\boxed{\ \textbf{the non-transit boundary is the measurement horizon:}\ \neg\text{a rung}\ge2\ \text{summand to leak}\ (2),\ \ \text{accessible content}=\ \text{the triple}\ (3),\ \ \text{interior void-closed}\ (5),\ \ \text{chart broken at the shell}\ (6),\ \ \neg\text{a radiation leg}\ (7)\ }$$
$$\text{BEYOND it no information escapes; WITHIN it all information is preserved}\ [\mathrm{D0.7};\ \mathrm{Def\text{-}BM.5}(1)\ \text{charge preservation}]\ \textbf{but inaccessible}\ [\mathrm{BM.143}(1)]\ \text{— the ledger's censorship, without a smooth horizon}\ [\mathrm{BM.134}(5)\ \text{discipline:}\ r_s\ \text{stays a chart-side dictionary partner}]$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (2),(4)\text{--}(8);\qquad\textbf{definition assembled from derived rows:}\ (1);\qquad\textbf{re-cited:}\ (3)\ \text{'s table};\qquad\text{the dynamical radiation leg stays open:}\ \mathrm{IT\.ext{-}O1}$$

**Req.** A6, A7 (Part 1); P5, CT0.3, CT0.9, CT0.12, CT0.13, CT1.19b, CT1.29, D0.7, D1.5, FT.1, FT.19, FT.20, FT.22 (Parts 1–2); Def-H.9(2), Def-H.15(1),(2),(3), Def-H.32(4), Def-H.36, FT.28 (Part 3); AT.29(1),(2),(3),(4), AT.30(3), AT.32(1),(2), AT.35(0),(1),(2),(3), AT.50(5), AT.46(4), AT.63(2) (Level 5); Def-BM.3(2),(3), Def-BM.5(1), BM.2(1), BM.122(2),(3),(6), BM.132(2), BM.134(5), BM.143(1), BM.146(3), BM.148(1),(4) (Part 4); rigorous `Fraction` interval arithmetic for $\ln 2$ (`qexact`), exact integer cell census [math; machine: `measurement_theorem.py` §C, 4/4].

**Pf.**
$$(2):\ \text{the block arithmetic}\ 3{+}3{+}5{+}3{+}1{+}1{=}16\ \text{and the absence census over}\ n{=}0..16\ [\text{machine C2}];\ (4):\ \text{the}\ 42\ \text{integer cells with}\ I_{\mathrm{hid}}\ge0\ \text{exact}\ [\text{machine C1}];$$
$$(5):\ \text{the explicit witness pair exhibited from the exhaustive}\ L{=}5\ \text{census}\ [\text{machine C3}];\ (6):\ \ \ln16=4\ln2>2\ \text{by rigorous interval and}\ k_{\mathrm{crit}}(2)\in[1.3862,1.3863]\ [\text{machine C3}];$$
$$(7):\ \text{the weight census at four}\ \varepsilon_q\ \text{witnesses with the threshold}\ \mathcal T_0(\text{pair})=4\mathfrak h/\ln2\ \text{at the minimal floor}\ [\text{machine C4}];\ (1),(3),(8),(9):\ \text{assembly on the cited rows}.\ \blacksquare$$

**Phys.** The directive asked for the boundary that leaks nothing, and the corpus already owns
it — three theorems deep. The mask arithmetic says a dark system's active aspects simply do not
include anything of rung two or higher: there is no EM summand, no colour summand, no sink
summand in its operator space, so the question "does the rung-two content leak?" has no content
to leak. The generalized invariance says what *is* there: exactly the boundary triple, the size,
and the rung — a complete inventory, with every other datum assigned to the mechanism that
bounds it out. And the void closure says the inventory is not a limitation of present technique
but a theorem about constructions: no later tier, no cleverer apparatus, no construction of any
kind recovers the interior of a seal. The witness pair makes it concrete — two five-edge chains
with identical boundary charge, one inert, one seething with interior wall activity — the
interior is *preserved* (every edge is registered, charge is conserved) and *inaccessible* (no
boundary read distinguishes them) in the same breath. Around this boundary the geometry agrees:
the chart's lapse goes negative before the chart is even formed, the shell is ledger-formed and
chart-unformed on the frozen certificate ln16 > 2, and no radiation leg exists to carry anything
out — not because radiation was forbidden, but because the supply vertex was never formed. That
is the measurement horizon: not a place where information dies, but a boundary at which the
ledger's books stay balanced while its contents stay sealed.

---

### IT.3 — Clause 3: the entanglement dichotomy — radiation is entanglement, and there is no collapse

**Thm.**
$$(1)\quad\textbf{THE MEASUREMENT PRIMITIVES (no collapse postulate exists):}\qquad\text{the axiom census}\ \mathrm{A1}\text{--}\mathrm{A9}\ \text{carries}\ \neg\text{a projection postulate};\qquad\text{registration:}\ (p,q)\in\mathcal R\iff|\Pi_{\mathcal V}\rho_{pq}|\le\varepsilon_q\ \vee\ \ge1-\varepsilon_q\ \ [\mathrm{A4};\ \mathrm{AT.13}(1)],\ \ \sigma_e\in\{\pm1\},\ \text{phase}=\text{registration data}\ [\mathrm{CT0.9};\ \mathrm{Def\text{-}EM.20}];$$
$$\text{the state update:}\ \text{one Gibbs tilt step per A4 event}\ [\mathrm{L0}],\qquad\delta K=\gamma\rho+\log Z_\gamma\cdot I,\qquad\gamma=1-4\varepsilon_q\ \ [\mathrm{L1};\ \mathrm{BM.131}(2)];$$
$$\textbf{the only ``collapse''-formed read in the record is the Born-width distribution's collapse at}\ \varepsilon_q=0\ (D_n\to1,\ w_{\mathrm{mat}}\to1,\ \text{exact})\ [\mathrm{AT.42}(3)]$$
$$(2)\quad\textbf{THE VACUUM BRANCH:}\qquad\rho_\circ=\tfrac14I:\ \ n_{\mathcal R}=0\implies\text{all-virtual},\ S_{\mathrm{raw}}(\rho_\circ)=\ln4=\max,\ \ \arg\max=\{\tfrac14I\}\ \textbf{UNIQUE}\ \ [\mathrm{CT0.2};\ \text{Gibbs}];$$
$$\text{the invariant-state family of the pair carrier is}\ p\,\tfrac{\Pi_{\mathcal R}}3+(1-p)\Pi_{\mathcal V}\ (\text{commutant nullity}\ 2\ \text{re-produced}),\ \text{and its UNIQUE entropy maximum is}\ \rho_\circ\ \text{at}\ p=\tfrac34\ \ [\text{machine: exact rational majorization at both vertices};\ \mathrm{AT.12}(4):\ b(\rho_\circ)=\tfrac34];$$
$$\rho_\circ\ \textbf{is the fixed point of BOTH evolutions:}\ \ \text{the Haar twirl}\ (2T\text{-average}=\text{Haar by Schur}\ [\mathrm{AT.10}])\ \text{and the Poisson tilt}\ (\delta K=0\ \text{exactly},\ \mathbb Q[[\gamma]]\ \text{to order}\ 12\ [\mathrm{BM.131}(2)]);\qquad\text{the}\ 2T\text{-twirl of ANY}\ \rho\ \text{is}\ b(\rho)\tfrac{\Pi_{\mathcal R}}3+(1{-}b)\Pi_{\mathcal V}\ [\text{machine, 4 witnesses}]$$
$$(3)\quad\textbf{THE COMPOSITE BRANCH (``entanglement'', ledger-native):}\qquad\text{system+register is ONE global Def-H.32 configuration sum}\ [\mathrm{AT.42}(2)];\qquad\text{its connector read telescopes:}\ \textstyle\sum_{\mathrm{int}}f_v=\tfrac12(\sigma_{\text{last}}-\sigma_{\text{first}})=-q_{\mathrm{EM}}\ \ \text{on ALL}\ 126\ \text{sign configurations of}\ L{=}2..6\ [\mathrm{EM.9b};\ \mathrm{AT.41}(4)];$$
$$\textbf{the compensator is UNIQUE:}\ \ \#\{q\in\{-1,0,1\}:q=-q_{\mathrm{in}}\}=1\ \ \forall q_{\mathrm{in}}\ \ [\mathrm{BM.122}(1);\ \mathrm{BM.23}(4);\ \mathrm{EM.11}:\ Q_{\mathrm{EM}}=0\ \text{survives in every valid universe}];$$
$$\textbf{the joint read is NON-FACTORIZING:}\ \ \dfrac{N_4(2m)}{N_2(2m)}=4^{m-1}+1\ \ \text{is}\ m\text{-DEPENDENT}\ (\text{exact ratios}\ 2,5,17,65;\ \text{witness}\ N_4(4)=40\ne4=N_2(2)^2)\ \ [\mathrm{AT.44}(2)\ \text{'s census formula}]$$
$$(4)\quad\textbf{THE DICHOTOMY (an exhaustiveness theorem, not a dynamics):}\qquad\text{for an EM-active system read at a boundary, AT.32(1)'s functional leaves EXACTLY two formed cases:}$$
$$\begin{array}{l|l}\textbf{the boundary data carries a connector to a register}&\textbf{it does not}\\\hline\text{the composite branch: telescoped charge read, unique compensator,}&\text{the isolated branch: the gauge-invariant content is the bit ALONE}\ [\mathrm{AT.12}(3)];\\ \text{non-factorizing joint census -- ``entangled with the detector''}&\text{the ensemble-symmetric charge read vanishes}\ \langle q\rangle_{\mathrm{ens}}=0\ [\mathrm{AT.53}];\\ &\text{the dynamically fixed state is}\ \rho_\circ\ \text{(2)}\ \text{-- ``vacuum-looking''}\end{array}$$
$$\boxed{\ \textbf{NO THIRD OPTION}=\mathrm{AT.32}(1)\ \textbf{itself: the accessible content is the functional of (triple,}\ |R|,\ n)\ \textbf{and nothing else}\ }\qquad\text{radiation IS entanglement:}\ \neg\exists\ \text{a formed emission that terminates nowhere (the compensator is unique, charge is conserved)}$$
$$(5)\quad\textbf{NO MEASUREMENT WITHOUT RUNG-2 ACTIVATION; NO RUNG-2 ACTIVATION WITHOUT COMPOSITE OR VACUUM:}\qquad\text{the first half is}\ \mathrm{IT.1}(6);\ \ \text{the second is}\ (4);\qquad\text{``the measurement problem'' closes as a STRUCTURAL theorem: there is no collapse, only}\ \mathrm{EM}\ \text{activation}\ +\ \text{the composite's boundary read}\ +\ \text{the tilt step}\ [\mathrm{L0};\ \mathrm{BM.131}(2)]$$
$$(6)\quad\textbf{the missing definition, named}\ (\text{the directive's constraint honored}):\qquad\text{the dichotomy is READ-LEVEL, not dynamical: a formed transit-leg AMPLITUDE between junctions does not exist in the inventory}\ [(\mathrm{R9}'');\ \mathrm{BM.122}(6);\ \mathrm{BM.6}(6):\ \neg\text{an S-matrix element beyond the formed amplitudes}]\ \text{—}\ \mathrm{IT\.ext{-}O1};$$
$$\text{the dichotomy needs none of it: it is the exhaustiveness of the accessible-content functional over the formed read classes}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (2)\text{--}(5);\qquad\textbf{record census:}\ (1);\qquad\textbf{open, named:}\ (6);\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{consciousness,}\ \neg\text{a smooth analogy}$$

**Req.** A4, A5, A6 (Part 1); P5, CT0.1, CT0.2, CT0.9, D0.3, D0.4, EM.9b, EM.11, EM.12, L0, L1, Def-EM.20 (Parts 1–2); Def-H.32(1),(2), FT.22 (Part 3); AT.10, AT.12(2),(3),(4), AT.13(1), AT.32(1), AT.41(4), AT.42(2),(3), AT.44(2), AT.53(3), AT.63(2) (Level 5); Def-BM.5(1), BM.23(4), BM.122(1),(6), BM.131(1),(2) (Part 4); Gibbs' lemma, exact rational majorization, Schur's lemma over the 24-element average, truncated $\mathbb Q[[\gamma]]$ series [math; machine: `measurement_theorem.py` §§A, D, 7/7].

**Pf.**
$$(2):\ \text{the nullity-2 elimination (48 equations, 16 unknowns); the majorization at}\ p\in\{0,\tfrac14,\tfrac12,\tfrac34,1\};\ \text{the}\ 2T\text{-average on four witnesses}\ (|00\rangle\langle00|,\ \rho_\circ,\ \Pi_{\mathcal V},\ \text{a mixed one)}\ [\text{machine A1, D1+D2}];$$
$$(3):\ \text{the}\ 126\text{-configuration telescoping census; the compensator census; the ratio closed form}\ 4^{m-1}{+}1\ \text{against the binomial formula at}\ m{=}1..4\ [\text{machine D3}];$$
$$(1),(4),(5):\ \text{the}\ u{=}0\ \text{rows}\ (D_n\to1)\ \text{and assembly on the cited exhaustiveness}\ [\text{machine D4}];\ (6),(7):\ \text{record rows}.\ \blacksquare$$

**Phys.** The measurement problem, in this corpus, was never a problem about consciousness or
collapse — it was a question about which reads are formed, and the answer is an exhaustiveness
theorem. Take anything electromagnetically active and ask what a boundary can say about it. The
generalized invariance bounds the answer before any dynamics: the boundary triple, the size, the
rung. Given those, exactly two things can be true. Either the boundary data carries a connector
to a register — and then the read is the composite's own telescoped charge, whose partner state
is unique by charge conservation, whose joint returns provably refuse to factorize into one-body
returns, and whose interior is one global configuration sum: that is entanglement, spelled
entirely in ledger primitives. Or it does not — and then everything the gauge cannot touch
collapses to the bit alone, the symmetric charge read vanishes, and the only state fixed by both
evolutions the corpus owns is the quarter-identity: the vacuum, all-virtual, maximal in raw
information, dynamically inert under twirl and tilt alike. There is no third shelf to put the
system on, because there is no third invariant. And there is no collapse anywhere in the record:
the axioms carry no projection postulate, the update is a tilt step, the registration is a
threshold crossing, and the only thing in the corpus that deserves the word is the Born-width
distribution sharpening at zero flicker. What the theorem does *not* claim is equally exact: a
formed radiation amplitude flying between the junctions does not exist in the inventory — the
dichotomy is read-level, the dynamics row stays open and named, and the honesty is structural
rather than rhetorical.

---

### IT.4 — Clause 4: the molecular necessity — the incommensurability bar is operational only in the multi-seal composite

**Thm.**
$$(1)\quad\textbf{THE INCOMMENSURABILITY, re-verified:}\qquad\mathfrak P=\mathbb Q\oplus\bigoplus_p\mathbb Q\ln p;\qquad\ln1280=8\ln2+\ln5,\qquad\ln960=6\ln2+\ln3+\ln5\ \ [\mathrm{BM.83}(2)];$$
$$\textbf{the independence certificate:}\ \ 2^a3^b5^c=1\implies a=b=c=0\ \ (\text{exhaustive}\ |a|,|b|,|c|\le12,\ \text{exact rational powers});\qquad\textbf{the parametric irrationality:}\ \ q\ln1280=p(\ln960+t\ln2),\ \ p,q\in\mathbb Z,\ t\in\mathbb Q_{\ge0}\ \text{forces}\ p=0\ (\ln3\ \text{coefficient}),\ \text{then}\ q=0\ (\ln5);$$
$$\boxed{\ \dfrac{\ln1280}{\ln960+t\ln2}\notin\mathbb Q\ \ \forall t\in\mathbb Q_{\ge0}\ }\qquad\text{and}\ \ \tfrac43\in\mathbb Q\ \ \text{vs}\ \ \tfrac{\ln1280}{\ln960}\in\mathfrak P\setminus\mathbb Q:\ \ \text{the two formed ratios are of DIFFERENT KINDS}\ [\mathrm{BM.83}(2),(3);\ \mathrm{BM.140}(5):\ \text{``the comparison is arithmetic,}\ \neg\text{a bridge''}]$$
$$(2)\quad\textbf{THE ALPHABET CENSUS (the clause's engine):}\qquad\text{the baryon-side value generators}\ \{E_{\mathrm{int}},\hat\mu'^2,\rho_{\mathrm B},D_S\}\ \text{and the lepton-side}\ \{\varepsilon_q,x_\pm,w_c,\sigma_\ell,z^{(\ell)}\}\ \text{are DISJOINT};\ \text{the shared symbols are}\ \mathfrak h\ (\text{the single P1 scale}),\ \ln2,\ \pi;$$
$$\textbf{the formed MIXED loci are EXACTLY THREE:}\qquad\begin{array}{l|l}\mathcal B_{\mathrm{ens}}^{(n)}=-\bigl(\tfrac{2n\,u\,D_{n-1}}{D_n}\bigr)\tfrac{\ln2}{\mathfrak h}\ [\mathrm{BM.137}(3)]&\text{flicker rational}\ \times\ \text{the P1 scale — on}\ n\text{-pair floors (composite)}\\\mathcal W_{\text{channel}}=x_+^2\,\chi_{\{NE\ge\mathcal T_0\}}\ [\mathrm{BM.122}(3)]&\text{flicker}\ \times\ \text{threshold — at an EM junction (composite)}\\\chi_{\{NE\ge\mathcal T_0\}},\quad\mathcal T_0=\tfrac{2E_{\mathrm{int}}\mathfrak h}{\ln2}\ [\mathrm{Def\text{-}BM.17}(3);\ \mathrm{BM.122}(2);\ \mathrm{BM.134}(5)]&\textbf{THE HANDSHAKE: the only formed condition in which BOTH alphabets appear — and it is BINARY}\end{array}$$
$$\text{every formed cross-currency RATIO}\ [\mathrm{BM.83}(5)]\ \text{carries an UNDECLARED slot}\ (\sigma_\ell,\ \sigma_\nu,\ \rho_{\mathrm B}):\qquad\textbf{cross-currency VALUES do not exist pre-calibration}$$
$$(3)\quad\textbf{THE REDUCED MASS IS NOT FORMABLE:}\qquad\mu=\dfrac{m_1m_2}{m_1+m_2}\ \ \text{with}\ m_1\ \text{baryon-currency}\ (E_{\mathrm{int}},\hat\mu'^2\ \text{species})\ \text{and}\ m_2\ \text{lepton-currency}\ (\sigma_\ell z^{(\ell)}\ \text{species})\ \text{requires a SUM across the disjoint value alphabets — a cross-currency equation, barred}\ [\mathrm{BM.83}(3);\ \mathrm{BM.37}(2);\ \mathrm{BM.134}(5);\ \mathrm{BM.140}(5)];$$
$$\text{formable only as a SYMBOLIC expression carrying undeclared slots}\ (2);\qquad\textbf{the corpus's own hydrogen ladder confirms the bar from the other side: it was constructed WITHOUT}\ \mu\ \ [\mathrm{AT.44}:\ \text{the positions live in the flicker alphabet alone}]$$
$$(4)\quad\textbf{THE SINGLE ATOM IS A SINGLE-CURRENCY INSTRUMENT:}\qquad W_d=\dfrac1{d^2x_+x_-}\ [\mathrm{AT.44}(5)]:\ \ \text{the ladder POSITIONS carry the lepton alphabet}\ \{x_\pm,d\}\ \text{alone, exactly degenerate in}\ k\ [\mathrm{AT.54}(3)],\ \text{disjoint from}\ \{E_{\mathrm{int}},\ln2,\mathfrak h,\hat\mu'^2\};$$
$$\text{the baryon side enters STRUCTURALLY — the endpoint's seal class:}\ \ W_3(Q)=\binom6{Q+3}=(1,6,15,20,15,6,1),\ \ \textstyle\sum=64=4^3,\ \ \text{the proton class}\ 15\ \ [\mathrm{AT.41}(2),(3);\ \mathrm{Def\text{-}BM.8}(6)\ \text{re-produced}];$$
$$\boxed{\ \textbf{atomic spectra can fix the lepton-currency slots only: the baryon-currency slots drop out of every atomic ladder position}\ }$$
$$(5)\quad\textbf{THE MULTI-SEAL GRAMMAR EXISTS, AND ITS FLOORS ARE EXACT}\ [\mathrm{BM.31}(2),(3),(5)]:\qquad g_\delta(N)=(1,0,3,10,15,105)\ \ \text{for}\ N{=}2..7\ \ (\delta\text{-protection UNIQUE to}\ N{=}3;\ \ g_\delta>0\ \ \forall N\ge4);\qquad g_\varepsilon(N)\ne0\iff3\mid N;$$
$$\text{at}\ N{=}6\ \text{the ensemble GENUINELY MIXES:}\ \tfrac{15}{25}=\tfrac35\ \text{of groupings contain a}\ \delta,\ \ \tfrac{10}{25}=\tfrac25\ \text{do not};\qquad\text{the separator of the sealings is the ATTACHMENT COUNT}\ N\ \text{in the boundary data}\ [\mathrm{Def\text{-}BM.9}(4)],\ \neg\text{charge (classes overlap at}\ Q{=}0{+}1;\ \text{only}\ |Q|{=}3\ \text{is baryon-exclusive)},\ \neg\text{phase alone}\ (4\mathbb Z\subsetneq2\mathbb Z);$$
$$\text{the threshold ladder:}\ \ \mathcal T_0\in\bigl\{\tfrac{4\mathfrak h}{\ln2},\dots,\tfrac{120\mathfrak h}{\ln2}\bigr\},\ \ \text{span ratio EXACTLY}\ 30\ \ [\mathrm{BM.115}(2)(\mathrm i);\ \mathrm{BM.122}(2)]$$
$$(6)\quad\textbf{THE ISOTOPIC NECESSITY (the terminal consequence):}\qquad\text{``molecular''}\ :=\ \text{the}\ N\ge4\ \text{multi-seal EM-bound ensembles (quoted name,}\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)];\ \text{grammar floors:}\ N{=}4\ \text{first}\ \delta\text{-mixed},\ N{=}6\ \text{first genuine}\ \varepsilon/\delta\ \text{mixture});$$
$$\textbf{(a)}\ \text{it is the smallest formed class with a STRUCTURED EM boundary:}\ \ge2\ \text{seals}+\ \text{connectors}\ \implies\ \text{rung-2 activity on a multi-junction support}\ [\mathrm{FT.20};\ \mathrm{BM.31}(2)];\qquad\textbf{(b)}\ \text{it is where the two currencies meet: all THREE mixed loci}\ (2)\ \text{live in multi-junction composites}\ (\mathcal B_{\mathrm{ens}}\ \text{on}\ n\ge2\ \text{pair floors},\ \mathcal W_{\text{channel}}/\chi\ \text{at junctions across}\ \mathcal T_0);$$
$$\textbf{(c)}\ \text{its read families depend on the seal classes}\ (E_{\mathrm{int}}\ \text{ladder},\ \text{span ratio}\ 30)\ \text{AND the junction flicker}\ (\varepsilon_q)\ \text{simultaneously — the incommensurability bar is OPERATIONAL exactly here: the bar forbids converting the currencies}\ (1),(3),\ \text{and the molecular read family is the formed locus where both are present WITHOUT conversion};$$
$$\boxed{\ \textbf{``we need molecular, sadly'' — DERIVED: the calibration era cannot proceed from single-currency data; the minimal formed instruments carrying both alphabets are the multi-seal EM-bound composites}\ }$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(6);\qquad\textbf{re-produced frozen rows:}\ \mathrm{BM.83}(2),(3),\ \mathrm{BM.31}(2),(3),\ \mathrm{AT.41}(2),(3);\qquad\textbf{bars untouched:}\ \mathrm{BM.134}(5),\ \mathrm{BM.83},\ \mathrm{BM.37}(2),\ \mathrm{P5};\qquad\neg\text{a declaration},\ \neg\text{a species identification}$$

**Req.** A8 (Part 1); P1, P4, P5, CT0.8, EM.9, EM.25(7) (Parts 1–2); Def-H.32(1),(2), FT.19, FT.20, FT.22 (Part 3); AT.41(2),(3),(4), AT.42(2), AT.44(2),(4),(5), AT.54(3), AT.63(2) (Level 5); Def-BM.3(7), Def-BM.8(6), Def-BM.9(4), Def-BM.17(3), BM.19, BM.31(2),(3),(5), BM.37(2), BM.83(2),(3),(4),(5), BM.88(3),(4), BM.115(2), BM.121(4), BM.122(2),(3), BM.134(5), BM.137(1),(3), BM.140(5),(7) (Part 4); the prime-log independence lemma (unique factorization), exact rational arithmetic, symbol-set censuses [math; machine: `measurement_theorem.py` §E, 5/5].

**Pf.**
$$(1):\ \text{the exhaustive certificate}\ 2^a3^b5^c\ (|a|,|b|,|c|\le12,\ \text{Fraction powers — no float ever touches the assertion})\ \text{and the coefficient solve}\ (\ln3\ \text{first, then}\ \ln5)\ [\text{machine E1}];$$
$$(2):\ \text{the symbol-set census on the frozen formulas; the three mixed loci exhibited; the BM.83(5) slot census}\ [\text{machine E2}];\ (3):\ \text{the disjointness corollary}\ [\text{machine E3}];$$
$$(4):\ W_d\ \text{'s alphabet vs the baryon generators; the}\ W_3\ \text{binomial census}\ \binom6{Q+3},\ \text{sum}\ 64\ [\text{machine E4}];\ (5):\ \text{the frozen counts with the exact ratios}\ \tfrac{15}{25}{=}\tfrac35,\ \tfrac{10}{25}{=}\tfrac25\ \text{and the span ratio}\ 120/4{=}30\ [\text{machine E5}];\ (6),(7):\ \text{assembly}.\ \blacksquare$$

**Phys.** The corpus spent a whole era proving that its two mass currencies cannot be converted
— the neutron–proton ratio is irrational in the prime-log ring at every rational coupling, the
two formed ratios are of different kinds, and the only place the two resolvent species touch is a
binary threshold indicator. The directive asked what that bar *means* for measurement, and the
answer came out sharper than a lament. The hydrogen atom — the pride of the atomic era — is a
single-currency instrument: its ladder positions carry the flicker alphabet alone, and the
proton enters as a seal *class*, the fifteenth of sixty-four, not as a number in any position. No
atomic spectrum, however precise, can ever constrain the baryon-currency slots. The reduced mass
of the textbooks is exactly the forbidden object: a sum across the disjoint alphabets, formable
only as a symbol string carrying undeclared calibration slots. What remains — what the grammar
census had already built and waiting — is the multi-seal composite: from four attachments the
δ-groupings exist, at six the two sealings genuinely mix in a three-to-two ratio, and every one
of the three formed mixed loci (the binding, the channel weight, the handshake itself) lives
precisely there, at junctions across thresholds, on pair floors. The molecule is not a
convenience; it is the minimal formed instrument in which both currencies are simultaneously
present without being converted — the only place the incommensurability bar is operational
instead of merely true. Hence the directive's sigh, derived: we need molecular, sadly. The
sadness is exact — the bar that forbids the bridge is the same bar that makes the bridge's
footings, on both banks, measurable at last.

---

### IT.5 — Clause 5: the calibration consequence, and the status of Tier IT.1

**Thm.**
$$(1)\quad\textbf{THE SLOT-VS-READ DEPENDENCY CENSUS:}\qquad\begin{array}{l|l|l}\textbf{the slot}&\textbf{the formed families whose alphabet contains it}&\textbf{the currency}\\\hline\mathfrak h\ (\mathrm{P1})&m_{\mathrm{hid}},\ \mathcal T_0,\ \rho_{\mathrm B},\ \mathcal B_{\mathrm{ens}}&\text{shared scale}\\\varepsilon_q\ [\mathrm{AT\text{-}O27}]&w_c,\ W_d,\ \mathcal W_{\text{round}},\ D_n/w_{\mathrm{mat}},\ \mathcal B_{\mathrm{ens}},\ \mathcal W_{\text{channel}},\ P(\Delta x_{\mathrm B})&\text{lepton/flicker}\\e_0\ [\mathrm{EM.25}(7):\ \neg\text{issued}]&\varepsilon_{\mathrm{EM}}(r,E,N)=Nf\mathsf g\varepsilon_{\mathrm{EM}}\ [\mathrm{BM.88}(4)]&\text{connector}\\\varkappa\beta\ [\mathrm{AT\text{-}O3}]&\mathrm{AT.6}\ \text{'s functional},\ \Theta_{\mathrm{drag}}\ \text{witnesses}\ [\mathrm{AT.46}(4)]&\text{metric/shift}\\\rho_{\mathrm B},\ \hat\mu'^2\ (\neg\text{declared})&\text{the pole ladder},\ \mathrm{BM.83}(5)\ \text{'s cross-ratios}&\text{baryon/pole}\\\sigma_\ell,\ \sigma_\nu\ (\neg\text{declared})&\text{the transport channel ratios},\ \mathrm{BM.83}(5)\ \text{'s cross-ratios}&\text{lepton/transport}\end{array}$$
$$\text{machine: the two currency slot-families are DISJOINT;}\ e_0\ \text{appears in NO formed read alphabet (it is not issued)}\ [\mathrm{EM.25}(7)];\ \ \text{every mixed locus is composite}\ [\mathrm{IT.4}(2)]$$
$$(2)\quad\textbf{THE CONSEQUENCE:}\qquad\boxed{\ \text{no single-currency data set constrains both slot families: the calibration era must proceed from multi-seal EM-bound (``molecular'') spectroscopy, where the threshold}\ \chi_{\{NE\ge\mathcal T_0\}},\ \text{the channel weight and the binding are simultaneously formed}\ }$$
$$\text{the accessible data species: vibrational/rotational/electronic-type transition READS of multi-seal composites — i.e. the (R1)/(R2) classes on}\ N\ge4\ \text{ensembles}\ [\mathrm{IT.1}(3);\ \mathrm{IT.4}(5)];\qquad\text{the read rules}\ (\mathrm{M1'})\text{--}(\mathrm{M3'})\ [\mathrm{AT.54}(6)]\ \text{still gate EVERY conversion — no value is issued, estimated or compared here}\ [\mathrm{P5}]$$
$$(3)\quad\textbf{THE ONTOLOGY ROW:}\qquad\text{the ``118}\times\text{118 nuclear mass table'' is}\ \neg\text{an object of this ontology: the accessible baryon data are the SEAL-CLASS PRICES on the}\ E_{\mathrm{int}}\ \text{ladder}\ \{2,6,12,24,60\}\ \text{with the Gram phases}\ \delta\in\{\tfrac29\ell,\tfrac2{27}q,\tfrac18\nu\}\ \text{— PRICES,}\ \neg\text{masses}\ [\text{HistLog}\ \S\mathrm{V.32};\ \mathrm{Def\text{-}BM.3}(7)\ \text{nomenclature};\ \mathrm{AT.44}(8)\ \text{read-rule discipline}];$$
$$\text{SM-mass identification stays}\ \neg\text{formed on the standing bars}\ [\mathrm{BM.140}(7)(\mathrm c):\ \neg\text{a datum}\ [\mathrm{P5}],\ \text{the range failures re-certified row-wise}];\qquad\text{an isolated baryon read is DARK by IT.1(4): EVERY baryon-currency datum that can reach a register arrives EM-mediated — i.e. spectroscopically, i.e. (by IT.4) molecularly}$$
$$(4)\quad\textbf{THE MEASUREMENT THEOREM, ASSEMBLED (the directive's single theorem):}\qquad\begin{array}{l|l}\textbf{clause}&\textbf{the disposition}\\\hline(1)\ \text{the rung hierarchy}&\textbf{DERIVED}\ [\mathrm{IT.1}]:\ \text{inter-system registration is rung-2 mediated; darkness is read-species separation}\\\\(2)\ \text{the non-transit boundary}&\textbf{DERIVED}\ [\mathrm{IT.2}]:\ \text{the mask leaks nothing, the content is the triple, the interior is void-closed, the shell is its locus}\\\\(3)\ \text{the entanglement dichotomy}&\textbf{DERIVED}\ [\mathrm{IT.3}]:\ \text{composite or vacuum, no third option}\ (=\mathrm{AT.32}(1));\ \neg\text{collapse in}\ \mathrm{A1}\text{--}\mathrm{A9}\\\\(4)\ \text{the molecular necessity}&\textbf{DERIVED}\ [\mathrm{IT.4}]:\ \text{the minimal formed two-currency instrument is the multi-seal EM-bound composite}\\\\(5)\ \text{the calibration consequence}&\textbf{DERIVED as strategy, values quarantined}\ [\mathrm{IT.5}]:\ \text{molecular spectroscopy is the calibration era's necessary data species}\end{array}$$
$$(5)\quad\textbf{THE OPEN ROWS THIS TIER LEAVES:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{content}\\\hline(\mathrm{IT\.ext{-}O1})&\text{the formed transit-leg amplitude (the radiation dynamics):}\ (\mathrm{R9}'')/\mathrm{BM.122}(6)\ \text{re-scoped to Level 6 — the dichotomy}\ [\mathrm{IT.3}]\ \text{is read-level and needs none of it, but a dynamical radiation theory would}\\\hline(\mathrm{IT\.ext{-}O2})&\text{the}\ N\ge4\ \text{multi-seal configuration calculus: the Def-H.32 sums past the two-body engine}\ [\mathrm{AT.44}];\ \mathrm{BM.31}\ \text{'s grammar census is the frozen floor};\ \mathrm{AT\text{-}O30}\ \text{'s cover engine is reusable}\\\hline(\mathrm{IT\.ext{-}O3})&\text{the handshake-indicator operational theory: the}\ \chi_{\{NE\ge\mathcal T_0\}}\text{-gated read families across the threshold ladder (span ratio 30) — the locus where IT.5's calibration strategy becomes mathematics}\end{array}$$
$$(6)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)];\qquad\text{§Cal-IT: empty};\qquad\text{marked rows inherited unchanged}\ [\mathrm{AT.63}(4)]$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{era2/level6\_molecular/checks/run\_all\_level6.py}\to\text{the level's runner (gate first)};\qquad\texttt{measurement\_theorem.py}\to\textbf{21/21 exact markers};\qquad\texttt{check\_level6\_format.py}\to\text{the format + citation gate (Part 6 documents; attestation against the era-1 registry AND the closed Level-5 record)};$$
$$\text{shared libraries borrowed from Level 5 via}\ \texttt{sys.path}\ (\texttt{qexact.py},\ \texttt{duality.py}\ \text{— single source of truth, documented)};\qquad\text{the Level-5 suite is untouched}\ (37\ \text{checkers},\ 643\ \text{markers});\qquad\texttt{index/},\ \texttt{tags.json},\ \texttt{Summary.md}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every IT-tag cites Parts 1--4, the closed Level-5 record, and earlier IT-tags only.}\ \neg\exists\ \text{a forward pointer used as a premise. Acyclic by construction}\ [\text{machine: the level-6 gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and Level 6 opens with no contact claim}\ }\qquad[\mathrm{AT.39}(8)\ \text{'s standing row, inherited at the level opening}]$$

**Req.** IT.1, IT.2, IT.3, IT.4 (this level); AT.6, AT.13, AT.32(1), AT.41, AT.42, AT.44, AT.46(4), AT.54(3),(6), AT.63(2),(4) (Level 5); P1, P4, P5, CT0.9, CT1.12a(3), CT1.19b, EM.25(7), FT.20, FT.22 (Parts 1–2); Def-H.9, Def-H.32, Def-H.33 (Part 3); Def-BM.3(7), Def-BM.9(4), Def-BM.17(3), BM.31, BM.83, BM.88(3),(4), BM.115(2), BM.122(2),(3),(6), BM.134(5), BM.137, BM.140(5),(7) (Part 4); exact symbol-set censuses [math; machine: `measurement_theorem.py` §F, 2/2 + the level runner + the level gate].

**Pf.** Row-wise assembly of IT.1–IT.4 with the slot census re-run [machine F1] and the ontology
rows cited to their frozen loci [F2]; the level gate and runner re-run end to end; the Level-5
record cited at AT.63(2)'s closed status, never edited. No new mathematics is introduced at this
tag. $\blacksquare$

**Phys.** The theorem ends where every theorem of this corpus ends: at the boundary of what is
declared. The slot census is the whole calibration program drawn as a bipartite graph — slots on
one side, formed read families on the other, edges exactly where a symbol appears — and the graph
has two connected components meeting only at the three composite loci. That is the consequence in
one picture: nuclear data alone lives in one component, atomic ladders in the other's lepton half,
and only the multi-seal composites touch both banks of the incommensurability bar at once. The
nuclear mass table the calibration brief might have wished for is not even an object here — what
exists are seal-class prices on a five-rung ladder, and every baryon datum that can reach a
register arrives dressed in electromagnetism, which is to say spectroscopically, which is to say
molecularly. So the Measurement Theorem closes the measurement problem as structure — hierarchy,
horizon, dichotomy — and opens the Isotopic era with its first obligation named: the N≥4
configuration calculus, the transit-leg amplitude, and the operational theory of the handshake
indicator are the three rows on which the calibration era's first real numbers will depend. No
number is issued here. The box at the end is the one every tier of both eras has carried:
coherence is not contact, and Level 6 opens exactly as Level 5 did — with the claim unmade and
the arithmetic exact.

---
## §Cal-IT — free internal parameters of the Isotopic era

**Empty at this tier.** No calibration parameter is added, valued, or re-scoped by Tier IT.1. The
slots this level's rows depend on are inherited and unchanged: $\mathfrak h$ (P1), $\varepsilon_q$
(AT-O27; $\tfrac18$ distinguished five ways, adoption ¬issued), $e_0$ (EM.25(7); ¬issued),
$(\varkappa,\beta)$ (AT-O3; P4 core), $\rho_{\mathrm B}$, $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$
(Cal-BM/Cal-F; ¬declared), the P4 transport profile $(\ell_c,\mathbf c)$, the lift and the
vielbein [AT.60(4),(9); AT.63(3)]. IT.5(1)'s dependency census is the level's slot map; the
read rules (M1′)–(M3′) [AT.54(6)] gate every conversion.

## §Open-IT — the rows this tier leaves open

| row | content | locus |
|---|---|---|
| (IT-O1) | the **formed transit-leg amplitude** — the radiation dynamics: (R9'')/BM.122(6)(O1)–(O4) re-scoped to Level 6; IT.3's dichotomy is read-level and needs none of it, but a dynamical radiation theory would; BM.6(6)'s S-matrix bar stays | BM.122(6); BM.6(6); IT.3(6) |
| (IT-O2) | the **N≥4 multi-seal configuration calculus** — the Def-H.32 sums past the two-body engine: resolvents, covers, sector censuses on the mixed grammars (N=4 all-δ; N=6 the 3/5–2/5 mix); AT-O30's cover engine and AT.44's two-body engine are the reusable templates | BM.31(2); AT.44; AT-O30; IT.4(5) |
| (IT-O3) | the **handshake-indicator operational theory** — the χ_{NE≥𝒯₀}-gated read families across the threshold ladder {4𝔥/ln2, …, 120𝔥/ln2} (span 30): where IT.5's calibration strategy becomes mathematics | Def-BM.17(3); BM.122(2); BM.134(5); IT.5(2) |

Inherited from Level 5, unchanged [AT.63(3),(5)]: the declarations owed to Era 2 (the lift —
which decides the index; the vielbein; the P4 transport profile; the read rules (M1′)–(M3′);
$\varepsilon_q$; $(\varkappa,\beta)$; $e_0$), the by-nature rows (AT-O2, AT-O29), the convention
row (AT-O7), the calibration-gated row (AT-O13), and the two censuses (AT-O30, AT-O32).

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.2: the 1p-kn isotopic family and the contraction-grammar phase transitions

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.2 — the 1p-$k$n family as support
classes: the triple-certified contraction grammar, the family census with its exact phase
structure, the $E_{\mathrm{int}}$ floors, the capacity/mask adjudication, and the lepton
saturation flag.
**Tags.** IT.6–IT.8. **Pattern.** the construction tiers (IT.1's shape) with the premise audit
logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT
stays empty; no clause of Parts 1–4 or of Level 5's closed record is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/isotopic_family.py` → **8/8 exact**;
`run_all_level6.py` → the level runner (gate first); `check_level6_format.py` → the gate over
both Part 6 documents. Exact arithmetic: integer set-partition enumeration (exhaustive to
$N=8$), the grammar recurrence, exact factorials/binomials, `Fraction` shares, polynomial
convolution (Vandermonde), symbolic multiples of $\ln2$ and $\pi$.
**No floating point in any assertion. No measured isotope datum enters any clause [P5]. No
species identification [Def-BM.3(1),(7)] — "protium/deuterium/tritium/hydrogen-4" stay quoted
labels of the identification layer; the derived objects are the SUPPORT CLASSES.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive: *"Construct the 1p-kn Isotopic Family and the
Contraction Grammar Phase Transitions … at $k=3$ (1p3n, which has $N=4$ colour attachments) the
screen and the mask will close something … this aligns with the contraction grammar
[Def-BM.9(3), BM.31]: for $N\ge4$ the $\delta$-sealings enter the ensemble, breaking the pure
$\varepsilon$-protection of the $N=3$ baryon."* — executed with three premise corrections logged
at IT.8(2); the Architect's standing flag (IT.4 acquires an exception when multi-$(p,n,e)$
systems are calculated) is honored and recorded, $\neg$pre-empted.

---

### IT.6 — The contraction grammar, triple-certified; the 1p-kn family census; and the exact locus of the phase transition

**Thm.**
$$(1)\quad\textbf{THE GRAMMAR ENGINE (triple-certified):}\qquad g(N)=\#\{\text{partitions of}\ N\ \text{attachments into contraction groups of size}\ 2\ (\delta)\ \text{and}\ 3\ (\varepsilon)\}\ \ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{CT3.17a}(2);\ \mathrm{FT.41}(\mathrm b)]$$
$$\textbf{three independent machines agree entrywise:}\ \ \text{exhaustive enumeration}\ (N\le8),\qquad g(N)=(N{-}1)g(N{-}2)+\binom{N-1}2g(N{-}3),\qquad g(N)=\!\!\sum_{2a+3b=N}\!\!\frac{N!}{a!\,2^a\,b!\,6^b}\ \ \text{with the full}\ (a,b)\ \text{breakdown};$$
$$\textbf{the frozen rows reproduce EXACTLY:}\ \ g=(1,1,3,10,25,105),\quad g_\delta=(1,\mathbf0,3,10,15,105),\quad g_\varepsilon=(0,1,0,0,10,0)\ \ \text{for}\ N{=}2..7\ \ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{BM.31}(2)];$$
$$g_\delta+g_\varepsilon=g\ \ \forall N;\qquad g_\varepsilon(N)\ne0\iff3\mid N\ \ (N{=}2..18);\qquad g(1)=0\ \ \textbf{— the lone attachment is never sealed}\ [\mathrm{CT3.17a}]$$
$$(2)\quad\textbf{THE FAMILY, as support classes:}\qquad\text{the 1p-}k\text{n composite of}\ N_{\mathrm{nuc}}{=}k{+}1\ \text{nucleons carries}\ \boxed{\ N=3(k{+}1)\ \text{attachments}\ }\ \text{— each nucleon is an}\ \varepsilon\text{-sealed 3-juncture, its THREE attachments sealed inside as one}\ \varepsilon\text{-type triple}\ [\mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(5);\ \mathrm{D3.9}];$$
$$\text{the attachment count is BOUNDARY DATA,}\ \neg\text{a summed-over structure}\ [\mathrm{Def\text{-}BM.9}(4)];\qquad\text{each}\ N\ \text{is its own support class}\ [\mathrm{Def\text{-}BM.9}(5)];\qquad\text{junction fusion/sharing is}\ \neg\text{constructed}\ (\mathrm{IT\.ext{-}O4})$$
$$(3)\quad\textbf{THE FAMILY CENSUS}\ (k{=}0..5;\ \text{machine: closed form}=\text{recurrence at every member}):\qquad\begin{array}{c|cccccc}k&0&1&2&3&4&5\\\hline N&3&6&9&12&15&18\\ g(N)&1&25&1540&164395&\cdot&\cdot\\ g_\varepsilon&1&10&280&15400&\cdot&\cdot\\ g_\delta&0&15&1260&148995&\cdot&\cdot\\ \delta\ \text{share}&0&\tfrac35&\tfrac9{11}&\tfrac{387}{427}&\cdot&\cdot\\ (a,b)\ \text{blocks}&(0,1){:}1&(3,0){:}15,\ (0,2){:}10&(3,1){:}1260,\ (0,3){:}280&(6,0){:}10395,\ (3,2){:}138600,\ (0,4){:}15400&-&-\end{array}$$
$$g(12)=164395=10395+138600+15400\ \ \textbf{exactly};\qquad\text{the}\ \delta\ \text{share is STRICTLY INCREASING in}\ k;\qquad\text{the pure-}\varepsilon\ \text{sector NEVER vanishes}\ (g_\varepsilon(3m)>0\ \forall\ \text{members})$$
$$(4)\quad\textbf{THE PROTECTION AND THE FIRST MIXING:}\qquad k{=}0\ (N{=}3):\ \text{the UNIQUE grouping is the}\ \varepsilon\text{-triple — the protection is forced}\ [\mathrm{BM.31}(1):\ g(3){=}1,\ g_\delta(3){=}0;\ \text{a}\ \delta\text{-sub-pairing on a 3-support leaves one dangling}\implies\partial_{\mathrm{col}}\ne\varnothing\implies\mathcal C{=}0\ [\mathrm{D2.14};\ \mathrm{FT.19}]];$$
$$k{=}1\ (N{=}6):\ \textbf{the FIRST family member admitting}\ \delta\text{-sealings — BM.31(2)'s frozen mix re-derived exactly:}\ \ \tfrac{15}{25}=\tfrac35\ \delta\text{-containing vs}\ \tfrac{10}{25}=\tfrac25\ \text{pure-}\varepsilon$$
$$(5)\quad\textbf{THE PHASE TRANSITION, exactly located:}\qquad\boxed{\ \textbf{the grammar transition is at}\ N{=}4:\ \ g_\delta\ 0\to3,\ \ \text{``the protection is unique to}\ N{=}3\text{''}\ [\mathrm{BM.31}(2)]\ \text{— frozen and re-derived}\ }$$
$$\textbf{inside the family}\ (N\equiv0\ (\mathrm{mod}\ 3))\ \text{the transition falls at the DEUTERON}\ (N{=}6),\ \neg\text{at 1p3n};\qquad\text{the}\ N{=}4\ \text{support itself is the double-mesonic (``tetraquark-type'', quoted) support:}\ g(4){=}3\ \text{(the three perfect matchings), ALL}\ \delta,\ g_\varepsilon(4){=}0$$
$$(6)\quad\textbf{THE STATISTICS COMPOSITION}\ [\mathrm{BM.31}(4);\ \text{Census}\ \mathrm{FT.49}(3);\ \mathrm{FT.22};\ \mathrm{BM.129}]:\qquad\text{pure-}\varepsilon\ \text{groupings: baryon-type}\ \Theta_{\mathrm{int}}\in4\mathbb Z;\qquad\text{EVERY}\ \delta\text{-containing grouping: only the}\ 2\mathbb Z\ \text{class};\qquad4\mathbb Z\subsetneq2\mathbb Z\ (\Theta_{\mathrm{int}}{=}2\ \text{meson-admissible, baryon-excluded — the partial separator});$$
$$\text{sector counts per member:}\ \ k{=}0:\ 1\ \text{baryon-type};\quad k{=}1:\ 10\ \text{vs}\ 15;\quad k{=}2:\ 280\ \text{vs}\ 1260;\quad k{=}3:\ 15400\ \text{vs}\ 148995\ \ \text{— the ensemble carries BOTH statistics classes from the deuteron on, as grouping sectors}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(6);\qquad\textbf{re-produced frozen rows:}\ \mathrm{Def\text{-}BM.9}(3),\ \mathrm{BM.31}(1),(2),(4);\qquad\neg\text{a declaration},\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)],\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** A7 (Part 1); P5, CT0.5, CT0.6, CT3.11(1), CT3.17, CT3.17a(2), D2.13, D2.14, D3.1, D3.9, FT.19, FT.22, FT.41(b) (Parts 1–2); Def-H.32(1), FT.34(3),(5) (Part 3); IT.1(4), IT.4(5) (this level); AT.29, AT.32(1), AT.50(3),(4),(5), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.9(1),(2),(3),(4),(5), BM.2(1), BM.17(1), BM.28(4), BM.31(1),(2),(3),(4),(5),(6), BM.129, Census FT.35(5), FT.49(3) (Part 4); exhaustive set-partition enumeration, the partition recurrence, exact factorials and binomials [math; machine: `isotopic_family.py` §§A–C, 4/4].

**Pf.**
$$(1):\ \text{the three engines compared entrywise to}\ N{=}8\ (\text{enumeration})\ \text{and}\ N{=}18\ (\text{recurrence vs closed form});\ \text{the}\ (a,b)\ \text{breakdowns matched term by term; the frozen sextuples}\ [\text{machine A1}];$$
$$(2),(3):\ \text{the family table computed from the closed form and re-verified against the recurrence at every member; the share monotonicity and}\ g_\varepsilon\ \text{positivity}\ [\text{machine B1}];$$
$$(4),(5):\ \text{the}\ N{=}4\ \text{partition census}\ (3\ \text{perfect matchings, all}\ \delta);\ \text{the mod-3 exclusion}\ (4\not\equiv0);\ \text{the frozen}\ 3/5\text{--}2/5\ \text{row re-derived}\ [\text{machine B1, C1}];$$
$$(6):\ \text{the sector counts from the}\ (a,b)\ \text{breakdown; the}\ 4\mathbb Z\subsetneq2\mathbb Z\ \text{witness}\ \Theta{=}2\ [\text{machine B2}];\ (7):\ \text{assembly}.\ \blacksquare$$

**Phys.** The grammar the corpus froze in its baryon tier turns out to be a machine, and the
machine runs the isotope family exactly. A nucleon is three attachments sealed by the unique
epsilon triple — protection not by decree but by counting: any delta on a 3-support leaves one
attachment dangling, and one dangling attachment annihilates the whole colour block. Add a
second nucleon and the support reaches six, where the counting turns: twenty-five groupings,
fifteen of them containing a delta, ten keeping the pure baryon seal — the frozen three-to-two
mix, now sitting inside a physical family rather than an abstract census. The transition the
directive predicted is real and is at $N=4$: that is where protection first breaks, three perfect
matchings, all mesonic. But the family never passes through $N=4$ — its attachment counts are
multiples of three — so the transition the family itself feels lands on the deuteron, and by
1p3n the delta-containing groupings outnumber the pure ones three hundred eighty-seven to
forty, without ever extinguishing them: fifteen thousand four hundred pure-epsilon groupings
survive at $N=12$, and the baryon's seal is a sector, never a casualty. The statistics
composition follows from the same counts: from the deuteron on, the family's ensemble carries
both phase classes, $4\mathbb Z$ inside $2\mathbb Z$, as grouping sectors — the ledger's version
of isotopy is a multiplicity structure, and the corrections to the directive's attachment count
are logged beside it, as the record demands.

---

### IT.7 — The family's prices, floors, charge, and the capacity adjudication: what closes, what never does

**Thm.**
$$(1)\quad\textbf{THE}\ E_{\mathrm{int}}\ \textbf{CENSUS (two derived readings):}\qquad\text{per nucleon}\ E_{\mathrm{int}}=6=2{+}2{+}2\ \ (\text{two materialized 2-cycles + the bidirectional connector})\ [\mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(2)];\qquad E_{\mathrm{int}}=|R|\ \text{is a cardinality, EXACTLY ADDITIVE over the disjoint union and the connector's edges}\ [\mathrm{AT.40}(3)];$$
$$\textbf{DISJOINT:}\ \ E_{\mathrm{int}}=6(k{+}1)=(6,12,18,24,30,36);\qquad\textbf{TREE-CONNECTED by}\ k\ \Sigma_{12}\text{-species bidirectional connectors (2 each):}\ \ E_{\mathrm{int}}=8k{+}6=(6,14,22,30,38,46);$$
$$\boxed{\ \textbf{the disjoint reading hits the computed-cell floors}\ \{2,6,12,24,60\}\ [\mathrm{BM.17}(4)]\ \textbf{at}\ k=0,\ 1,\ 3\ \text{— the 1p3n member lands EXACTLY on the 24 floor}\ }\qquad[\mathrm{Def\text{-}BM.14}(6)\ \text{'s order-isomorphism locus}\ 12/24/60:\ \text{an ORDER,}\ \neg\text{a number, no species identification}]$$
$$(2)\quad\textbf{the derived per-member rows (exact symbolic multiples, no values):}\qquad\frac G{2\pi\ln2}=E^2\ [\mathrm{BM.88}(3)];\qquad\frac{k_{\mathrm{crit}}}{\ln2}=\frac{E^2}2\ [\mathrm{AT.35}(1)];\qquad r_s=\tfrac{\mathfrak h E}2,\qquad\Delta x_{\mathrm B}=\tfrac{\mathfrak h}{E\ln2}\ [\mathrm{Def\text{-}BM.4}(1);\ \mathrm{BM.17}(3)\ \text{pattern}];$$
$$\boxed{\ \Delta x_{\mathrm B}\cdot r_s=\tfrac{\mathfrak h^2}{2\ln2}\ \ \textbf{E-INDEPENDENTLY}\ [\mathrm{BM.17}(3)]\ }\qquad\text{the shell is non-empty at EVERY member}\ (E^2\ln2>2\ \text{on the frozen}\ \ln16>2\ \text{certificate}\ [\mathrm{BM.148}(4);\ \mathrm{AT.35}(2)]);\qquad\textbf{the family scales the lock, the shell and the horizon by exact integers, and moves nothing else}$$
$$(3)\quad\textbf{CHARGE:}\qquad Q_{\mathrm{total}}=+1\ \ \text{for EVERY member}\ (k{=}0..5):\ \ \text{the proton member's class}\ {+}1\ [\mathrm{AT.41}(2)],\ \text{the neutrons'}\ q_{\mathrm{net}}=0\ [\mathrm{BM.17}(2)],\ \text{connector interiors telescope}\ [\mathrm{EM.9b}];$$
$$\textbf{the sign census convolves binomially:}\ \ W_3(Q)=\binom6{Q+3}=(1,6,15,20,15,6,1),\ \ \textstyle\sum=64=4^3\ [\mathrm{Def\text{-}BM.8}(6);\ \mathrm{AT.41}(2)]\ \ \text{and the}\ (k{+}1)\text{-fold convolution is}\ \binom{6(k+1)}{Q+3(k+1)}\ \ \textbf{exactly (Vandermonde, entrywise to}\ k{=}4);$$
$$\text{the charge classes overlap the mesonic ones at}\ Q\in\{0,+1\};\ \ \text{only}\ |Q|{=}3\ \text{is baryon-exclusive per nucleon}\ [\mathrm{BM.31}(3)]\ \text{— the family's}\ Q{=}+1\ \text{is a CLASS label, its census binomial}$$
$$(4)\quad\textbf{PHASE:}\qquad\Theta_{\mathrm{int}}=2k(\Gamma)\in2\mathbb Z\ \ \text{per materialized closed chain}\ [\mathrm{FT.22};\ \mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(3):\ \Pi=72k(\Gamma)(\ln2)^2];\qquad\text{baryon-type}\ 4\mathbb Z\ \text{per pure-}\varepsilon\ \text{sector}\ [\mathrm{IT.6}(6)];$$
$$\text{the connector winding enters via}\ k(\Gamma)=k_1{+}k_2{+}d_{12}\ [\mathrm{FT.34}(3)]\ \text{and stays PARAMETRIC in}\ d:\ \ \neg\text{a frozen nucleon--nucleon connector winding exists anywhere in the record}\ (\mathrm{IT\.ext{-}O4});\ \ \neg\text{one is invented here}$$
$$(5)\quad\textbf{CAPACITY NEVER BITES:}\qquad\text{colour slots exist at}\ n{=}3\ \text{only}\ [\mathrm{CT3.11}(1);\ \mathrm{D3.1}];\qquad\text{every junction of every member sits at}\ n{=}3,\ \text{where}\ D_{\mathrm{tick}}(3)=2^4=16=C_{\mathrm{cap}}\ \ \textbf{EXACTLY SATURATED and admissible}\ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT0.11}];$$
$$n{=}4\ \text{would give}\ 2^5=32>16\ \text{— inadmissible}\ [\mathrm{AT.50}(3)]:\ \ \textbf{hence the multi-junction spreading of an}\ N\ge4\ \text{support}\ [\mathrm{IT.6}(5)],\ \text{and NO member at any}\ k\ \text{trips capacity, the rung ladder, or the}\ D^-\text{lock}\ (D^-\ \text{activates only at rung}\ \ge4\equiv\neg\text{admissible — the lock biconditional}\ [\mathrm{AT.50}(4),(5)])$$
$$(6)\quad\textbf{WHAT DOES CLOSE — from}\ k{=}1\ \textbf{uniformly:}\qquad(\mathrm P1)\ \text{the visibility bound}\ I_{\mathrm{hid}}=E_{\mathrm{tot}}-E_{\mathrm{vis}}\ [\mathrm{AT.29}(1)];\quad(\mathrm P2)\ \text{the mask}\ \mathcal K_\Sigma\ [\mathrm{AT.29}(2)];\quad(\mathrm P3)\ \textbf{the VOID closure: the internal constituent states of a sealed composite are}\ \neg\text{knowable BY THEOREM — no construction could exist inside the bound}\ [\mathrm{BM.143}(1);\ \mathrm{AT.29}(3),(4)];$$
$$\text{the accessible content is EXACTLY}\ (\text{boundary triple},\ |R|,\ \text{rung})\ [\mathrm{AT.32}(1)]\ \text{— for the family:}\ (Q{=}{+}1,\ \Theta\text{-class},\ S,\ N{=}3(k{+}1),\ E_{\mathrm{int}}\text{-reading, rung}\ 3);\qquad\textbf{the first closure is the DEUTERON}\ (k{=}1),\ \neg\ k{=}3$$
$$(7)\quad\textbf{the exact content of ``the screen and the mask close something'' at}\ k{=}3\ \textbf{(the directive's prediction, adjudicated):}\qquad\text{(i) what closes at}\ N{=}4\ \text{is the}\ \varepsilon\text{-PROTECTION (grammar}\ [\mathrm{IT.6}(5)]),\ \neg\text{capacity};$$
$$\text{(ii) at}\ k{=}3\ \text{exactly: the disjoint}\ E_{\mathrm{int}}=24\ \text{lands on the floor}\ (1),\ \text{and the}\ \delta\ \text{share first exceeds}\ \tfrac9{10}\ \bigl(\tfrac{387}{427}\bigr)\ [\mathrm{IT.6}(3)];\qquad\text{(iii) the information closure}\ (6)\ \text{is uniform from}\ k{=}1\ \text{— nothing additional closes at}\ k{=}3$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(7);\qquad\textbf{parametric residue: the connector species}\ (d,\ \text{count, fusion)}\ \to\ \mathrm{IT\.ext{-}O4};\qquad\textbf{prices,}\ \neg\textbf{masses throughout}\ [\text{HistLog}\ \S\mathrm{V.32};\ \mathrm{Def\text{-}BM.3}(7)\ \text{nomenclature}];\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT0.5, CT0.6, CT0.11, CT0.13, CT3.11(1), D3.1, EM.9b, FT.19, FT.22 (Parts 1–2); Def-H.32, FT.34(3),(5), FT.35 (Part 3); IT.6 (this level); AT.29(1),(2),(3),(4), AT.32(1), AT.35(1),(2), AT.40(3), AT.41(2),(3), AT.50(3),(4),(5), AT.63(2) (Level 5); Def-BM.3(7), Def-BM.4(1), Def-BM.8(1),(6), Def-BM.9(4), Def-BM.14(6), BM.2(1),(2), BM.17(1),(2),(3),(4), BM.31(3),(4), BM.83, BM.88(3), BM.134(5), BM.135, BM.143(1), BM.148(4), Census FT.35(2),(3),(4),(5), FT.42(5), FT.49(3) (Part 4); exact binomials, polynomial convolution (Vandermonde), integer floor census [math; machine: `isotopic_family.py` §§D–F, 3/3].

**Pf.**
$$(1):\ \text{the}\ 6{=}2{+}2{+}2\ \text{witness re-derived; the two}\ E_{\mathrm{int}}\ \text{readings by exact additivity; the floor census against}\ \{2,6,12,24,60\}\ [\text{machine D1}];$$
$$(2):\ \text{the symbolic rows per member; the}\ E\text{-independent product identity; the shell certificate on the frozen}\ \ln16>2\ \text{row}\ [\text{machine D1}];$$
$$(3):\ W_3\ \text{re-produced as}\ \binom6{Q+3};\ \text{the}\ (k{+}1)\text{-fold convolution matched entrywise against}\ \binom{6(k+1)}{Q+3(k+1)}\ \text{to}\ k{=}4\ [\text{machine E1}];$$
$$(4):\ \text{the class arithmetic}\ (4\mathbb Z\subsetneq2\mathbb Z,\ \Theta{=}2\ \text{witness)}\ [\text{machine E1}];\ (5):\ \text{the}\ D_{\mathrm{tick}}(n)=2^{n+1}\ \text{census}\ n{=}0..8\ \text{with the saturation and inadmissibility rows}\ [\text{machine F1}];$$
$$(6),(7),(8):\ \text{assembly on the cited rows}.\ \blacksquare$$

**Phys.** The family's arithmetic is the corpus's arithmetic, and it lands where the record said
it would. Six per nucleon, exactly additive, because internal energy here is a count of real
edges and nothing else: the disjoint reading walks 6, 12, 18, 24 — and the fourth member, one
proton three neutrons, lands precisely on the twenty-four floor, the middle rung of the
order-isomorphism the baryon tier flagged as an order and never a number. The tree reading, with
its Sigma-twelve-species connectors, walks off-floor from the deuteron on — and the difference
between the two readings is exactly the unconstructed piece, the nucleon–nucleon connector,
named below as an open row rather than guessed. Charge is boring in the best way: plus one for
every member, telescoping doing the work, the sign census convolving by Vandermonde into a
binomial peaked at its class. Capacity — the bound the directive suspected — never bites: every
junction sits at three slots, where the tick demand is exactly sixteen, exactly at the cap,
exactly admissible; a four-slot vertex would be inadmissible, which is why the four-attachment
support of the previous tag spreads over junctions instead. What closes is older and total: the
visibility bound, the mask, and the void closure that no construction could exist inside — from
the deuteron onward, uniformly. So the Architect's screen and mask do close something at
$k=3$, and the record can now say precisely what: the epsilon-protection closed at $N=4$ in the
grammar, the delta share crosses ninety percent at $N=12$, the price lands on the 24 floor — and
the interior has been sealed since the first isotope, on a theorem that predates the family.

---

### IT.8 — The lepton saturation flag, the premise corrections, and the status of Tier IT.2

**Thm.**
$$(1)\quad\textbf{LEPTON SATURATION (flagged for the next step, per the directive):}\qquad\text{the unsealed lepton}\ (Q{=}{-}1\ \text{register})\ \text{couples to ANY family member through the ONE global Def-H.32 configuration sum}\ [\mathrm{AT.42}(2)]\ \text{by an open connector whose boundary read is}\ Q_{\mathrm{total}}{=}{+}1\ \text{— INVARIANT across every grouping (telescoping}\ [\mathrm{EM.9b};\ \mathrm{IT.7}(3)]):$$
$$\boxed{\ \textbf{the}\ \delta\text{-mixing CANNOT alter the connector's boundary condition}\ }\qquad\text{the lepton price}\ w_c=\bigl(4\varepsilon_q(1{-}4\varepsilon_q)\bigr)^{-1/2}\ge2\ [\mathrm{AT.44}(4)]\ \text{and the positions}\ W_d=1/(d^2x_+x_-)\ [\mathrm{AT.44}(5)]\ \text{carry the flicker alphabet ALONE — GRAMMAR-BLIND (symbol census)};$$
$$\textbf{what the mixing changes is the nuclear-side ensemble:}\ \ \text{it decomposes into grouping sectors}\ (\mathrm{BM.31}(6)\ \text{'s disjoint-union pattern})\ \text{with multiplicities}\ g(N)=1,25,1540,164395,\dots,\ \text{the}\ (-1)^{\aleph}\ \text{dressing}\ [\mathrm{Def\text{-}H.32}(2)]\ \text{and the}\ \Theta\text{-class composition}\ [\mathrm{IT.6}(6)]:\ \ \textbf{INTENSITIES AND STATISTICS COMPOSITION, never positions}\ [\mathrm{AT.54}(3)];$$
$$\boxed{\ \textbf{isotopy, ledger-natively: SAME boundary charge, DIFFERENT grammar multiplicities}\ }\qquad\text{the isotope family reads on the connector side as pure multiplicity/measure structure; chemical identification QUARANTINED}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)]$$
$$(2)\quad\textbf{THE PREMISE CORRECTIONS (on the record, the house discipline):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``1p3n has}\ N{=}4\ \text{colour attachments''}&\textbf{CORRECTED:}\ N{=}3(k{+}1){=}12\ \text{for}\ k{=}3\ \text{— a nucleon is a 3-attachment}\ \varepsilon\text{-triple}\ [\mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(5)];\ \text{fusion/sharing}\ \neg\text{constructed}\ (\mathrm{IT\.ext{-}O4})\\ \text{``}\delta\ \text{enters at}\ N{=}4\ \text{in the family''}&\textbf{RELOCATED: the grammar transition IS at}\ N{=}4\ (g_\delta{:}\ 0\to3,\ \text{frozen}\ [\mathrm{BM.31}(2)]),\ \text{but the family}\ (N\equiv0\ (3))\ \text{first admits}\ \delta\ \textbf{at the deuteron}\ (N{=}6,\ \tfrac35\text{--}\tfrac25);\ \text{at 1p3n}\ \delta\ \textbf{dominates}\ (\tfrac{387}{427})\\ \text{``the screen and mask close something at}\ k{=}3\text{''}&\textbf{ADJUDICATED}\ [\mathrm{IT.7}(7)]\text{: what closes at}\ N{=}4\ \text{is the}\ \varepsilon\text{-protection (grammar),}\ \neg\text{capacity (never bites:}\ n{=}3\ \text{saturated-admissible at every}\ k);\ \text{the}\ (\mathrm P1)\text{--}(\mathrm P3)\ \text{closure is uniform from}\ k{=}1;\ \text{at}\ k{=}3\ \text{exactly: the}\ E_{\mathrm{int}}{=}24\ \text{floor landing and the}\ \delta\text{-share crossing}\ \tfrac9{10}\\ \text{the}\ g_\delta/g_\varepsilon\ \text{values cited in the directive}&\textbf{CONFIRMED:}\ (1,0,3,10,15,105)\ \text{and}\ (0,1,0,0,10,0)\ \text{for}\ N{=}2..7\ \text{— reproduced triple-certified}\ [\mathrm{IT.6}(1)]\end{array}$$
$$(3)\quad\textbf{THE ARCHITECT'S STANDING FLAG, recorded}\ \neg\textbf{pre-empted:}\qquad\text{``IT.4 will soon get an exception when we calculate multi-}(p,n,e)\ \text{systems in the molecular''}\ \ [\mathrm{IT.1}\ \text{session record}]:$$
$$\text{this tier supplies the nuclear-side half of that calculus}\ (\text{the}\ (p,n)\ \text{supports});\ \text{when the electron-saturated members are constructed}\ (\mathrm{IT\.ext{-}O2}),\ \mathrm{IT.4}(4)\ \text{'s single-currency rows and}\ \mathrm{IT.4}(6)\ \text{'s minimality are expected to acquire their exception row — recorded here as an expectation, to be derived}\ \neg\text{assumed, at its own locus}$$
$$(4)\quad\textbf{THE OPEN ROWS:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{content}\\\hline\textbf{new}\ (\mathrm{IT\.ext{-}O4})&\textbf{the nucleon--nucleon connector species:}\ \text{count per pair, winding}\ d\ [\mathrm{BM.2}(2)/(\mathrm{R10})\ \text{pattern}],\ \text{and whether junctions FUSE (attachment sharing) — the tree}\ E_{\mathrm{int}}\ \text{reading and the composite}\ \Theta_{\mathrm{int}}\ \text{stay parametric until constructed};\ \mathrm{FT.34}(3)\ \text{'s}\ k(\Gamma){=}k_1{+}k_2{+}d_{12}\ \text{is the frozen skeleton}\\\hline(\mathrm{IT\.ext{-}O2})&\text{the}\ N\ge4\ \text{multi-seal configuration calculus — absorbs the family's ensemble weights}\ (\text{sector sums over the}\ g(N)\ \text{groupings});\ \mathrm{AT.44}/\mathrm{AT\text{-}O30}\ \text{engines reusable}\\\hline(\mathrm{IT\.ext{-}O3})&\text{the handshake-indicator operational theory}\ [\mathrm{IT.1}\ \text{unchanged}];\qquad(\mathrm{IT\.ext{-}O1})\ \text{the transit-leg amplitude}\ [\mathrm{IT.3}(6)\ \text{unchanged}]\end{array}$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured isotope value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)];\qquad\text{§Cal-IT stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{the grammar census is pure seal combinatorics; the}\ E_{\mathrm{int}}\ \text{rows are informational-currency PRICES; the lepton rows stay in}\ \{\varepsilon_q\}),\ \mathrm{FT.55}(1),\ \mathrm{CT3.22}\ (\text{colour}\ \neg\text{observable — the grammar counts sealings, never reads colour}),\ \mathrm{BM.143}(1)$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{isotopic\_family.py}\to\textbf{8/8 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{3 checkers, 33 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{2 Part 6 documents PASS};\qquad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8)\ \text{'s standing row;}\ \mathrm{IT.1}(8)\ \text{'s box, re-cited}]$$

**Req.** IT.1, IT.3(6), IT.4(4),(5),(6), IT.6, IT.7 (this level); P1, P4, P5, CT0.5, CT0.6, CT3.22, EM.9b, FT.22, FT.34(3) (Parts 1–2); Def-H.32(1),(2), FT.19 (Part 3); AT.40(3), AT.41, AT.42(2), AT.44(2),(4),(5), AT.50, AT.54(3), AT.63(2), AT-O30 (Level 5); Def-BM.3(1),(7), BM.2(2), BM.17, BM.31(2),(6), BM.83, BM.129, BM.134(5), BM.135, BM.137(1), BM.143(1) (Part 4); exact symbol-set censuses [math; machine: `isotopic_family.py` §G, 1/1 + the level runner + the level gate].

**Pf.** Row-wise assembly of IT.6–IT.7 with the lepton-side symbol census [machine G1]; the
correction table verified against each cited locus; the runner and the gate re-run end to end.
No new mathematics is introduced at this tag. $\blacksquare$

**Phys.** The flag the directive asked for is short and exact. Send an electron at any member of
this family and the connector sees one thing only: the boundary charge, plus one, identical for
protium-grammar and for the fifteen-thousand-grouping chaos of N=12, because telescoping does not
care what the interior sealed. The lepton's own price and the ladder's positions live in the
flicker alphabet alone — the grammar cannot touch them; positions never move. What the grammar
does is split the nuclear side into sectors, and the sector counts are the isotope's real
signature in this corpus: one grouping, twenty-five, fifteen forty, a hundred sixty-four
thousand three hundred ninety-five — multiplicities and dressing signs and statistics
composition, intensities at unmoved prices, the Lamb-analog logic of the atomic era applied to
the nucleus. That is isotopy without a single chemical name: same charge, different counting.
The corrections stand beside the confirmations, as always — the attachment count was wrong in
the directive and right in the canon, the transition is real but falls on the deuteron inside
the family, and the thing that closes at k=3 is a floor landing and a ninety-percent delta
share, not a capacity wall. One row opens where the construction honestly stops: the connector
between two nucleons has no frozen species yet — its count, its winding, and whether junctions
fuse are the next tier's business, and until then the tree reading stays parametric, saying so.

---

## §Cal-IT — free internal parameters of the Isotopic era

**Empty at this tier** (unchanged from IT.1). The family's parametric residues are recorded as
open rows, not parameters: the connector winding $d$ and count (IT-O4) join the inherited slots
[$\mathfrak h$ (P1); $\varepsilon_q$ (AT-O27); $e_0$ (EM.25(7), ¬issued); $(\varkappa,\beta)$
(AT-O3); $\rho_{\mathrm B}$, $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared); the P4
transport profile; the lift and the vielbein (AT.60)].

## §Open-IT additions from Tier IT.2

| row | content | locus |
|---|---|---|
| (IT-O4) | the **nucleon–nucleon connector species**: count per nucleon pair, winding $d$, and junction fusion/sharing (attachment-count reduction). Until constructed: the family's tree $E_{\mathrm{int}}$ reading and composite $\Theta_{\mathrm{int}}$ stay parametric; the disjoint reading and all grammar rows are unaffected. The frozen skeleton is $\mathrm{FT.34}(3)$'s $k(\Gamma)=k_1+k_2+d_{12}$; the pattern is BM.2(2)/(R10)'s connector-winding row; R3's flavor-composition item is adjacent | IT.7(1),(4),(8); BM.17(1); FT.34(3) |

Inherited unchanged [IT.1(5)]: (IT-O1) the transit-leg amplitude, (IT-O2) the $N\ge4$
configuration calculus (which absorbs the family's sector-weighted ensemble sums), (IT-O3) the
handshake-indicator operational theory; and the Level-5 ledger [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.3: the multi-seal configuration census at $N=5,6$

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.3 — the channel-width skeleton, the
contraction-grammar census at $N=5,6$, the mask dimensions, and the $D^-$ saturation boundary:
the census side of IT-O2, closed at these boundaries.
**Tags.** IT.9–IT.11. **Pattern.** the construction tiers (IT.1/IT.2's shape), premise audit
logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT
stays empty; no clause of Parts 1–4 or of Level 5's closed record is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/multi_seal_census.py` → **9/9 exact** (the IT.2
grammar engine reused verbatim, per the directive's "do not reinvent the census; extend it");
`run_all_level6.py` → **4 checkers, 42 exact markers, 0 failures**; `check_level6_format.py` →
the gate over all three Part 6 documents. Exact arithmetic: integer partition enumeration,
exact binomials, Laurent convolution over $\mathbb Z$, `Fraction` shares.
**No floating point in any assertion. No measured value enters any clause [P5]. No species
identification [Def-BM.3(1),(7)] — the objects are "multi-seal EM-bound composites"; the
"stellar collapse boundary" is a FRAMING, flagged as such at IT.11(1).**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive: *"Run the Multi-Seal Configuration Census for $N=5$ and
$N=6$ — the channel width skeleton and the $D^-$ saturation boundary … determine if the census
terminates or encompasses $D^-$ pure saturated areas … I think this does IT-O4 and IT-O2
simultaneously."* — executed with three premise corrections logged at IT.11(2); the closing
assessment adjudicated: **IT-O2 closes on its census side; IT-O4 stays open, sharpened.**

---

### IT.9 — The channel-width skeleton and the contraction-grammar census at $N=5,6$

**Thm.**
$$(1)\quad\textbf{THE CHANNEL WIDTH SKELETON:}\qquad W_N(Q)=[z^Q]\,(2+z+z^{-1})^N=\binom{2N}{Q+N}\qquad[\mathrm{BM.135};\ \mathrm{Def\text{-}BM.8}(6)\ \text{generalized};\ \text{machine: Laurent convolution}=\text{binomial, entrywise}]$$
$$\textbf{the frozen rows reproduce exactly:}\ \ W_2=(1,4,6,4,1)\ [\mathrm{BM.135}(3)];\qquad W_3=(1,6,15,20,15,6,1),\ \ \textstyle\sum=64=4^3\ [\mathrm{BM.135}(2);\ \mathrm{AT.41}(2)];$$
$$\boxed{\ W_5=(1,10,45,120,210,\mathbf{252},210,120,45,10,1),\ \ \textstyle\sum=4^5=1024,\ \ 11\ \text{charge classes}\ }\qquad\boxed{\ W_6=(1,12,66,220,495,792,\mathbf{924},792,495,220,66,12,1),\ \ \textstyle\sum=4^6=4096,\ \ 13\ \text{classes}\ }$$
$$(2)\quad\textbf{THE CROSS-}\ N\ \textbf{CENSUS}\ [\mathrm{BM.31}(3)\ \text{'s pattern extended}]:\qquad W_5(Q)\ne W_6(Q)\ \ \text{on the WHOLE overlap}\ |Q|\le5\ \ (\text{and}\ W_3\ \text{vs}\ W_5,\ W_3\ \text{vs}\ W_6\ \text{likewise})\ \text{— where charge classes coincide, the probability spaces still differ};$$
$$|Q|=6\ \ \text{is}\ W_6\text{-exclusive};\qquad\text{both widths peak at}\ Q=0\ (252,\ 924);\qquad\text{the read domain:}\ Q\ \text{is defined only on SEALED supports}\ (\mathcal C=1)\ [\mathrm{BM.135}(1);\ \mathrm{D2.14};\ \mathrm{FT.19}]\ \text{— and every grammar grouping is total, hence sealed}$$
$$(3)\quad\textbf{THE GRAMMAR CENSUS, triple-certified}\ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{BM.31}(1),(2);\ \mathrm{CT3.17a}(2);\ \mathrm{FT.41}(\mathrm b);\ \text{the IT.2 engine reused}]:\qquad\text{enumeration}\ \wedge\ \text{recurrence}\ g(N){=}(N{-}1)g(N{-}2){+}\binom{N-1}2g(N{-}3)\ \wedge\ \text{closed form}\ \sum_{2a+3b=N}\tfrac{N!}{a!\,2^a\,b!\,6^b}\ \ \text{agree entrywise};$$
$$\boxed{\ N{=}5:\ \ g(5)=10,\ \ \text{ALL of block type}\ (a,b)=(1,1)\ \text{— one}\ \delta\text{-pair + one}\ \varepsilon\text{-triple, uniquely}\ }\qquad\boxed{\ N{=}6:\ \ g(6)=25=\underbrace{15}_{(3,0)}+\underbrace{10}_{(0,2)},\quad\frac{15}{25}=\frac35\ \ \text{vs}\ \ \frac{10}{25}=\frac25\ \ [\mathrm{BM.31}(2)\ \text{re-derived EXACTLY}]\ }$$
$$(4)\quad\textbf{N=5 IS FORCED-MIXED (the ``highly strained'' row, as arithmetic):}\qquad2a+3b=5\ \ \text{has the UNIQUE nonnegative solution}\ (1,1)\implies g_\varepsilon(5)=0\ \ \textbf{is forced}:$$
$$\boxed{\ \textbf{EVERY 5-attachment grouping contains exactly one}\ \delta\ \textbf{and exactly one}\ \varepsilon\ \text{— no pure-baryon}\ (4\mathbb Z)\ \textbf{sector exists at}\ N{=}5\ }\qquad[\mathrm{BM.31}(4)\ \text{statistics classes};\ \mathrm{IT.8}\ \text{composition rows}]$$
$$N{=}4\ \text{is all-}\delta\ (3\ \text{perfect matchings}\ [\mathrm{IT.6}(5)]),\ \ N{=}5\ \text{cannot avoid the triple},\ \ N{=}6\ \text{restores the pure-}\varepsilon\ \text{option}\ (\tfrac25)$$
$$(5)\quad\textbf{THE PROTECTION PERIODICITY:}\qquad\boxed{\ g_\varepsilon(N)>0\iff3\mid N\ }\qquad\text{verified for EVERY}\ N{=}2..18\ (\text{closed form against recurrence throughout});$$
$$\delta\ \text{shares:}\ \ N{=}4{:}\ 1,\quad N{=}5{:}\ 1,\quad N{=}6{:}\ \tfrac35,\quad N{=}9{:}\ \tfrac9{11},\quad N{=}12{:}\ \tfrac{387}{427}\ \ [\mathrm{IT.7}\ \text{re-derived}]\ \text{— the protection is PERIODIC (returns at every multiple of 3), the erosion within it MONOTONE}\ [\mathrm{IT.7}(3)]$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{re-produced frozen rows:}\ W_2,\ W_3,\ g_\delta/g_\varepsilon\ \text{sextuples};\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT3.17a(2), D2.14, FT.19, FT.41(b) (Parts 1–2); IT.6(5), IT.7(3), IT.8 (this level); AT.41(2), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.8(6), Def-BM.9(3),(4),(5), BM.31(1),(2),(3),(4), BM.135(1),(2),(3) (Part 4); exact Laurent convolution over $\mathbb Z$, binomial identities, integer partition enumeration, the partition recurrence [math; machine: `multi_seal_census.py` §§A–B, 5/5].

**Pf.**
$$(1):\ \text{the Laurent power}\ (2{+}z{+}z^{-1})^N\ \text{expanded by exact dictionary convolution and matched to}\ \binom{2N}{Q+N}\ \text{entrywise at}\ N{=}2,3,5,6;\ \text{sums}\ 4^N\ \text{and class counts}\ 2N{+}1\ [\text{machine A1}];$$
$$(2):\ \text{the full-table inequality census on the overlaps; the exclusivity and peak rows}\ [\text{machine A2}];\ (3):\ \text{the three engines compared, with the}\ (a,b)\ \text{breakdowns term by term}\ [\text{machine B1}];$$
$$(4):\ \text{the solution census of}\ 2a{+}3b{=}5\ \text{and the block breakdown}\ \{(1,1){:}10\}\ [\text{machine B2}];\ (5):\ \text{the}\ N{=}2..18\ \text{census with the exact Fraction shares}\ [\text{machine B3}];\ (6):\ \text{assembly}.\ \blacksquare$$

**Phys.** The census the directive ordered comes out in pure integers, and its first surprise is
a shape: the channel width does not merely grow, it grows binomially — eleven charge classes and
a thousand twenty-four sign states at five attachments, thirteen classes and four thousand
ninety-six at six, each table exactly the coefficient row of a power of $(2+z+z^{-1})$, with the
frozen meson and baryon rows falling out at $N=2,3$ as the base cases. The grammar side is
sharper still. Five is the strained support the Architect named, and the strain is an arithmetic
fact, not a mood: $2a+3b=5$ has one solution, so every one of the ten groupings is exactly one
mesonic pair glued to one baryonic triple — there is no pure-baryon sector to retreat to, and
the statistics composition has no $4\mathbb Z$ class at all. Four is all-mesonic; six restores
the pure option at two-fifths; and the periodicity row says the protection never dies
permanently — it returns at every multiple of three while the delta share climbs monotonically
between returns. Cross-reading the two skeletons gives the census its separation power: charge
classes overlap between supports, but the probability spaces never agree on the overlap — the
width skeleton distinguishes what the charge alone cannot, exactly as the baryon tier's
$N=2$-vs-$3$ comparison did, now at every pair.

---

### IT.10 — The mask dimensions and the $D^-$ saturation boundary: two mask species, the attained bound, and the structural censorship

**Thm.**
$$(1)\quad\textbf{THE TWO MASK SPECIES, KEPT APART}\ [\mathrm{IT.1}(6)\ \text{'s discipline}]:\qquad\textbf{RUNG masks}\ \mathcal K_n=\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}\ [\mathrm{D2.3}]:\ \ \dim\mathcal K_n=6,16,17,25\ \ (n{=}0..3),\ \ 26\ \ \textbf{ONLY at the formal}\ n\ge4;$$
$$\textbf{SUBNETWORK masks}\ \mathcal K_\Sigma(C)=\bigoplus_{A\in\mathcal A(\Sigma;C)}\mathcal K^{(A)}\ [\mathrm{Def\text{-}H.15}(3);\ \mathrm{AT.29}(\mathrm P2)]:\ \ \mathcal A(\Sigma;C)\subseteq\{\mathrm{EM},\mathrm G,\mathrm H,\mathrm W,\mathrm{strong}\}\ \text{—}\ \ \textbf{J}^\pm\ \textbf{and}\ \textbf{D}^\pm\ \textbf{NEVER}\ [\mathrm{FT.20}\ \text{table+Rmk};\ \mathrm{FT.26}(3)\ \text{'s own Pf}];$$
$$\boxed{\ \dim\mathcal K_\Sigma=9\ (\mathrm{G}{+}\mathrm{W}{+}\mathrm{H}\ \text{core})\ +\ 1\cdot[\mathrm{EM}\ \text{active}]\ +\ 8\cdot[\mathrm{strong}:\ \mathrm{Colour}\ne\varnothing\ \wedge\ \mathcal C{=}1]\ \ \le\ \ 18\ }\qquad[\mathrm{FT.26}(3);\ \mathrm{FT.28}(4)]$$
$$(2)\quad\textbf{THE BOUND IS ATTAINED — at exactly these composites:}\qquad\text{the grammar groupings are total}\implies\ \text{sealed}\ (\mathcal C{=}1\ [\mathrm{D2.14}]);\ \ \text{EM-active registration}\iff\exists v\ f_v\ne0\ [\mathrm{FT.20}];$$
$$\boxed{\ \textbf{the sealed EM-active}\ N{=}5,6\ \textbf{members attain}\ \dim\mathcal K_\Sigma=9{+}1{+}8=18\ \text{— the general bound, reached ``only in the inside-sealed variant''}\ [\mathrm{FT.28}(4)\ \mathrm{Rmk}]\ }\qquad\text{activity census exact:}\ 9/10/17/18$$
$$(3)\quad\textbf{THE LOCK BICONDITIONAL, re-run exhaustively}\ [\mathrm{AT.50}(3),(4)]:\qquad D^-\in\mathcal A(n)\iff n\ge4\iff2^{n+1}>16=C_{\mathrm{cap}}\iff\neg\text{admissible}\qquad(n{=}0..16);$$
$$\textbf{the refinement of the directive's bound row:}\ \ C_{\mathrm{cap}}{=}16\ \text{bounds the PAIR channel}\ [\mathrm{CT0.12}\ \mathrm{Rmk}];\ \ \text{the per-vertex tick demand}\ D_{\mathrm{tick}}(n){=}2^{n+1}\ \textbf{saturates exactly at}\ n{=}3\ (16{=}C_{\mathrm{cap}},\ \text{admissible});\ \ \text{the subnetwork mask bound is}\ 18,\ \neg16\ (1)\ \text{— three spaces, three bounds}$$
$$(4)\quad\textbf{THE VERTEX PLACEMENT (the screen's exact locus):}\qquad\text{every grouping's}\ (a,b)\ \text{blocks place the attachments on 2-supports}\ (\delta{:}\ n{=}2,\ D_{\mathrm{tick}}{=}8)\ \text{and 3-supports}\ (\varepsilon{:}\ n{=}3,\ D_{\mathrm{tick}}{=}16\ \textbf{exactly saturated});$$
$$n{=}4\ \text{would demand}\ 32>16\ \text{— inadmissible}\ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT3.11}(1):\ \text{colour slots at}\ n{=}3]:\qquad\textbf{NO vertex carries}\ \ge4\ \text{attachments};\qquad N{=}5\ \text{runs on}\ \ge2\ \text{supports in EVERY grouping (uniquely}\ 1{+}1),\ \ N{=}6\ \text{on}\ \ge2\ (3{+}0\ \text{or}\ 0{+}2);$$
$$\text{the connectors BETWEEN supports have no frozen species}\ [\mathrm{IT.7}(1),(4);\ \mathrm{IT\.ext{-}O4}]\ \text{— the census names the decomposition,}\ \neg\text{the glue}$$
$$(5)\quad\textbf{THE}\ D^-\ \textbf{STATUS AT THESE BOUNDARIES — NONZERO-BUT-UNREACHABLE, re-verified:}\qquad\begin{array}{l|l}\textbf{the row}&\textbf{the locus}\\\hline\text{the junction vertices are}\ D^-\text{-CONFIGURED — placement,}\ \neg\text{activation}&[\text{Census}\ \mathrm{FT.35}(4);\ \mathrm{CT4.1};\ \mathrm{BM.17}(1)]\\\text{no subnetwork mask contains a}\ D^-\ \text{summand, at any}\ N&(1)\ [\mathrm{FT.26}(3)\ \mathrm{Pf}]\\\mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0\ \ \forall n\le3;\ \ \neg\exists\ \text{a pole of}\ Z(\mathcal R,n);\ \text{one-way transfer}&[\mathrm{CT4.2}]\\\text{at the formal unlocking: nonzero as a formal object,}\ \iota_4\ \text{unrealized, vertices}\ \{V_0..V_3\}&[\mathrm{AT.50}(5);\ \mathrm{CT4.4a}(1);\ \mathrm{CT0.11}]\\\text{structureless even if reached: no gauge algebra, no generator; dust}\ w{=}0;\ \text{entropy locked}&[\mathrm{CT4.4};\ \mathrm{CT4.5};\ \mathrm{CT4.7}]\\\text{the void closure caps it: no construction could exist inside the bound}&[\mathrm{BM.143}(1);\ \mathrm{AT.29}(3),(4);\ \mathrm{IT.2}(6)]\end{array}$$
$$\boxed{\ \textbf{THE CENSUS TERMINATES IN A STRUCTURAL CENSORSHIP, NOT A SMOOTH SINGULARITY: the interior is preserved (every edge registered}\ [\mathrm{D0.7}]\textbf{) and provably cannot reach the boundary}\ }$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{re-run frozen censuses:}\ \mathrm{AT.50}(3),(4)\ \text{'s biconditional},\ \mathrm{FT.28}(4)\ \text{'s bound};\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT0.5, CT0.6, CT0.11, CT0.12, CT0.13, CT0.14, CT3.11(1), CT4.1, CT4.2, CT4.4, CT4.4a(1), CT4.5, CT4.7, D0.7, D2.3, D4.1, FT.19, FT.20, FT.26(3), FT.28(4) (Parts 1–2); Def-H.15(3), Def-H.32(1), FT.22 (Part 3); IT.2(6), IT.6(5), IT.7(1),(4), IT.9 (this level); AT.16(4),(5), AT.29(2),(3),(4), AT.32(1), AT.50(1),(3),(4),(5), AT.63(2) (Level 5); Def-BM.3(7), D2.14, BM.17(1), BM.143(1), Census FT.35(4) (Part 4); exact block-dimension arithmetic, exhaustive biconditional census [math; machine: `multi_seal_census.py` §C, 3/3].

**Pf.**
$$(1):\ \text{the block sums}\ 3{+}3{+}5{+}3{+}1{+}1{+}1{+}8{+}1\ \text{per rung against}\ 6/16/17/25/26;\ \text{the subnetwork activity census}\ (9,10,17,18)\ \text{from the}\ \mathrm{FT.20}\ \text{criteria}\ [\text{machine C1}];$$
$$(2):\ \text{the attainment row}\ 9{+}1{+}8{=}18\ \text{for sealed EM-active members}\ [\text{machine C1}];\ (3):\ \text{the}\ n{=}0..16\ \text{biconditional census re-run}\ [\text{machine C1}];$$
$$(4):\ \text{the per-grouping support census with the exact tick demands}\ (8,\ 16,\ 32)\ \text{and the inadmissibility wall}\ [\text{machine C2}];\ (5):\ \text{the block-census rows}\ +\ \text{row-wise citation of the frozen lock chain}\ [\text{machine C3}];\ (6):\ \text{assembly}.\ \blacksquare$$

**Phys.** The directive asked whether the census terminates or encompasses dark saturated areas,
and the answer required first separating two masks that the question had merged. The rung mask
reaches twenty-six dimensions only at a rung no vertex can occupy — the tick demand doubles past
sixteen and the channel dies; the subnetwork mask, the one these composites actually wear, never
contains the dark summand at all, and its bound is eighteen. That bound is not asymptotic
bookkeeping: the sealed, EM-active five- and six-attachment composites attain it exactly — the
inside-sealed variant the fermion tier had flagged as the unique attainer, now populated by a
family. The placement census shows why nothing ever overshoots: every grouping decomposes onto
two- and three-slot supports, the three-slot ones sitting precisely at capacity — saturated,
admissible, and one slot from death. And the dark sector keeps the status the locked-sector
adjudication gave it: configured at the junctions, masked at every accessible rung, formally
nonzero behind a wall that is a biconditional rather than a barrier, structureless even if the
wall were crossed, and capped by the void closure that no construction could exist inside. So
the census terminates — not in a singularity, smooth or otherwise, but in a structural
censorship: the interior is preserved to the last registered edge and provably cannot speak to
the boundary. That is the ledger's collapse boundary, and it is made of counting, not density.

---

### IT.11 — The synthesis, the premise corrections, and the adjudication of the open rows

**Thm.**
$$(1)\quad\textbf{THE SYNTHESIS (the directive's step 4, as exact ledger rows):}\qquad\begin{array}{l|l|l}\textbf{quantity}&\textbf{behaviour with}\ N&\textbf{the locus}\\\hline\text{the grammar}\ g(N)&\textbf{GROWS strictly}\ (1,3,10,25,105,385,1540,7245,32725,164395\ \text{for}\ N{=}3..12)&[\mathrm{IT.9}(3);\ \mathrm{IT.2}]\\\text{the channel width}&\textbf{GROWS:}\ 4^N\ \text{states},\ 2N{+}1\ \text{classes}\ (1024/11,\ 4096/13)&[\mathrm{IT.9}(1)]\\\text{the}\ \delta\ \text{share}&\textbf{GROWS within the family:}\ 0,\ 1,\ \tfrac35,\ \tfrac9{11},\ \tfrac{387}{427}\ (N{=}3,5,6,9,12)&[\mathrm{IT.9}(5);\ \mathrm{IT.7}(3)]\\\text{the}\ D^-\ \text{sink}&\textbf{CONSTANT:}\ \dim\mathcal K^{(D^-)}=1\ \text{at every rung — full at birth, structureless}&[\mathrm{CT4.4};\ \mathrm{D4.1};\ \mathrm{AT.50}(1)]\\\text{the per-vertex cap}&\textbf{HARD:}\ D_{\mathrm{tick}}(3){=}16{=}C_{\mathrm{cap}}\ \text{saturated};\ D_{\mathrm{tick}}(4){=}32\ \text{inadmissible}&[\mathrm{CT0.5};\ \mathrm{CT0.6}]\end{array}$$
$$\boxed{\ \textbf{``}\ D^-\ \textbf{pure saturated areas'' do not exist as growing regions: the sink is ONE-dimensional at every}\ N\ \text{— there is nothing for the census to encompass; what grows is the grammar and the width, and what bounds is combinatorial}\ }$$
$$(2)\quad\textbf{THE PREMISE CORRECTIONS (on the record):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``the}\ D^-\ \text{sink is formally active in these composites, adding 1 dimension to reach 26''}&\textbf{CORRECTED}\ [\mathrm{IT.10}(1),(3)]:\ \text{two mask species — the 26-dim mask is the RUNG mask at the inadmissible rung}\ \ge4;\ \text{subnetwork masks never contain}\ D^-\ [\mathrm{FT.26}(3)\ \mathrm{Pf}]\ \text{and are bounded by 18 — attained here}\\\text{``accessible vertex sets strictly bounded by}\ C_{\mathrm{cap}}{=}16\text{''}&\textbf{REFINED}\ [\mathrm{IT.10}(3)]:\ C_{\mathrm{cap}}{=}16\ \text{bounds the PAIR channel}\ [\mathrm{CT0.12}\ \mathrm{Rmk}];\ \text{the per-vertex tick demand saturates at}\ n{=}3;\ \text{the subnetwork mask bound is}\ 18\\\text{``this does IT-O4 and IT-O2 simultaneously''}&\textbf{ADJUDICATED}\ (3),(4):\ \mathrm{IT\.ext{-}O2}\ \text{closes on its census side;}\ \mathrm{IT\.ext{-}O4}\ \text{is untouched by a grammar census — sharpened, open}\end{array}$$
$$(3)\quad\textbf{IT-O2 CLOSED ON ITS CENSUS SIDE at the}\ N{=}5,6\ \textbf{boundaries:}\qquad\text{the width skeleton}\ \mathrm{IT.9}(1),(2),\ \text{the grammar}\ \mathrm{IT.9}(3)\text{--}(5),\ \text{the masks}\ \mathrm{IT.10}(1)\text{--}(3),\ \text{the placement}\ \mathrm{IT.10}(4),\ \text{the}\ D^-\ \text{status}\ \mathrm{IT.10}(5)\ \text{— all derived};$$
$$\textbf{RESIDUE (IT-O2 stays open for it): the AMPLITUDE side — the Def-H.32 ensemble sums over the grouping sectors}\ (10\ \text{sectors at}\ N{=}5,\ 25\ \text{at}\ N{=}6,\ \text{each a configuration class with its own}\ (-1)^{\aleph}\ \text{dressing}\ [\mathrm{Def\text{-}H.32}(2)];\ \mathrm{AT.44}/\mathrm{AT\text{-}O30}\ \text{engines reusable});$$
$$(4)\quad\textbf{IT-O4 STAYS OPEN, SHARPENED:}\qquad\text{the}\ (a,b)\ \text{census NAMES the support decompositions}\ (N{=}5{:}\ \text{one 2-support + one 3-support, uniquely};\ N{=}6{:}\ \text{three 2-supports or two 3-supports}),$$
$$\text{and thereby sharpens the question: the connector species must join SUPPORTS of these exact shapes — count per pair, winding}\ d\ [\mathrm{FT.34}(3)\ \text{'s}\ k(\Gamma){=}k_1{+}k_2{+}d_{12}\ \text{skeleton}],\ \text{fusion/sharing}\ [\mathrm{IT.7}(1),(4);\ \mathrm{BM.2}(2)/(\mathrm{R10})\ \text{pattern}];\qquad\text{the census cannot and does not invent one}$$
$$(5)\quad\textbf{THE FRAMING ROW (the directive's step 4, honestly bounded):}\qquad\text{``the stellar collapse boundary'' is a FRAMING — no astrophysical species is identified}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)],\ \text{no density or pressure primitive appears anywhere in the census};$$
$$\textbf{its exact ledger content:}\ \ \text{a composite family at maximal grammar growth, maximal channel width, forced or dominant}\ \delta\text{-mixing, against a CONSTANT one-dimensional censored sink behind a hard per-vertex combinatorial cap —}\ \textbf{a COMBINATORIAL CAPACITY LIMIT of the topology-blind sum}\ [\mathrm{Def\text{-}H.32}(1);\ \mathrm{IT.10}(3),(4)],\ \neg\text{a density limit}$$
$$(6)\quad\textbf{the Architect's standing flag, unchanged:}\ \ \mathrm{IT.4}\ \text{'s exception awaits the multi-}(p,n,e)\ \text{calculus}\ [\mathrm{IT.8}(3)]:\ \text{this tier is the}\ (p,n)\text{-side census; the electron-saturated members remain}\ \mathrm{IT\.ext{-}O2}\ \text{'s amplitude side}\ — \text{recorded,}\ \neg\text{pre-empted}$$
$$(7)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification};\qquad\text{§Cal-IT stays empty};\qquad\text{bars untouched:}\ \mathrm{BM.83},\ \mathrm{BM.134}(5),\ \mathrm{FT.55}(1),\ \mathrm{CT3.22}\ (\text{colour}\ \neg\text{observable — the grammar counts sealings, never reads colour})$$
$$(8)\quad\textbf{the machine state:}\qquad\texttt{multi\_seal\_census.py}\to\textbf{9/9};\qquad\texttt{run\_all\_level6.py}\to\textbf{4 checkers, 42 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{3 Part 6 documents PASS};\qquad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(9)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no composite here is named}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** IT.2(6), IT.4, IT.6(5), IT.7(1),(3),(4), IT.8(3), IT.9, IT.10 (this level); P1, P5, CT0.5, CT0.6, CT0.11, CT0.12, CT3.22, FT.34(3) (Parts 1–2); Def-H.32(1),(2), FT.22 (Part 3); AT.39(8), AT.44, AT.50(1), AT.63(2), AT-O30 (Level 5); Def-BM.3(7), BM.2(2), BM.83, BM.134(5), BM.143(1), CT4.4, D4.1 (Part 4); row-wise assembly + exact growth censuses [math; machine: `multi_seal_census.py` §D, 1/1 + the level runner + the level gate].

**Pf.** Row-wise assembly of IT.9–IT.10 with the growth/constancy censuses [machine D1]; the
correction table verified against each cited locus; the runner and the gate re-run end to end.
No new mathematics is introduced at this tag. $\blacksquare$

**Phys.** The synthesis fits in one table because the corpus keeps its currencies apart: three
quantities grow — the grammar factorially-ish, the width as a power of four, the delta share
toward one — and two things do not move at all: the dark sink, one-dimensional at every rung,
full at birth and structureless forever, and the per-vertex cap, sixteen ticks, saturated
exactly where the colour slots live. A "saturation boundary" in the sense of a growing dark
region simply does not exist here; what exists is a censorship that was complete before the
family started — placement without activation, a mask that annihilates, a formal unlocking
behind an inadmissibility wall, and the void closure underneath it all. So the collapse framing
translates cleanly and only one way: the ledger's pre-collapse composite is maximal combinatorial
growth against constant combinatorial constraint, and the limit that binds is a counting limit —
the topology-blind sum's own capacity arithmetic — with no density, no pressure, and no named
star anywhere in the derivation. Two rows close and stay honest about it: the census side of the
multi-seal calculus is done at these boundaries, and the amplitude side — the actual ensemble
sums over ten and twenty-five grouping sectors — is named as the residue; the connector question
is sharpened by the decompositions and left open, because a census of sealings is not a species
of glue, and the record does not invent what it has not derived.

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.4: the $N=9$ isobar doublet and its single-seed weak transition

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.4 — the "tritium"/"helium-3" isobar
doublet as boundary sectors of the $N=9$ support class, the single-seed weak transition with its
forced carrier and conditionally forced neutral member, and the route-relative Q-value verdict:
the level's first decay construction and its first declaration owed.
**Tags.** IT.12–IT.15. **Pattern.** the construction tiers (IT.1/IT.2/IT.3's shape), premise
audit logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT
stays empty; no clause of Parts 1–4 or of Level 5's closed record is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/isobar_transition.py` → **25/25 exact** (the IT.2
grammar engine reused, third census locus; the IT.3 width skeleton at $N=9$);
`run_all_level6.py` → **5 checkers, 67 exact markers, 0 failures**; `check_level6_format.py` →
the gate over all four Part 6 documents. Exact arithmetic: integer set-partition enumeration,
exact binomials, Laurent convolution over $\mathbb Z$, `Fraction` witnesses and shares, symbolic
multiples of $u=\ln2/\mathfrak h$ with `Fraction` coefficients, a rigorous `Fraction` enclosure
of $\ln2$ (series $+$ exact tail bound).
**No floating point in any assertion. No measured value enters any clause [P5] — the physical
$\beta$ endpoint stays a quarantined [EXT] scoring target and is cited nowhere. No species
identification [Def-BM.3(1),(7)] — "tritium", "helium-3", "isobar", "electron", "neutrino" stay
quoted labels of the identification layer; the derived objects are the $Q=+1$ and $Q=+2$ BOUNDARY
SECTORS of the $N=9$ support class and the ledger's own carrier channels.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 12), two acts: *(i)* *"Rename this level to
isotopic. I think molecular needs to wait a before this."* — executed as its own commit before
any new content, recorded at IT.15(2); *(ii)* the "tritium" $\beta^-$ construction: the sealed
composite at $N=9$, $Q=+1$, $E_{\mathrm{int}}=18$; the weak ladder and the alphabet overflow; the
forced $q=-1$ carrier from the channel inventory; the $Q=+2$, $N=9$ final state; the kinematic
driver $W(+1)/W(+2)=43758/31824=11/8$ read as *"the ensemble mass is proportional to this weight
… Tritium is structurally heavier than Helium-3 … not a fitted parameter … thermodynamically
unstable"*; the metric step $E_{\mathrm{total}}=N\sqrt{m_{\mathrm{rest}}^2+p^2}-N_ip_i$; and the
neutral partner as *"the unique admissible carrier"* — executed with four premise corrections and
one refinement logged at IT.15(1); the combinatorial skeleton confirmed to the integer, the mass
reading corrected on the record.

---

### IT.12 — The $N=9$ isobar doublet: two boundary sectors of one sealed support

**Thm.**
$$(1)\quad\textbf{THE SUPPORT AND ITS GRAMMAR (re-produced at}\ k{=}2\textbf{):}\qquad N=9=3(k{+}1)\big|_{k=2}\ \ \text{attachments — three}\ \varepsilon\text{-sealed 3-junctures}\ [\mathrm{IT.6}(2);\ \mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(5)]:$$
$$g(9)=1540=\underbrace{1260}_{(a,b)=(3,1)}+\underbrace{280}_{(0,3)}\quad\textbf{triple-certified}\ (\text{enumeration}\ \wedge\ \text{recurrence}\ \wedge\ \text{closed form})\ [\mathrm{IT.6}(1)\ \text{engine, third locus}];\qquad\frac{g_\delta}{g}=\frac9{11}\ [\mathrm{IT.9}(5)\ \text{'s frozen row re-derived}];$$
$$\text{the pure-}\varepsilon\ \text{count:}\quad280=\frac{9!}{3!^3\,3!}\ \ (\text{the unordered triple partitions})\ [\text{machine: exact}];\qquad\text{the attachment count is BOUNDARY DATA,}\ \neg\text{a summed-over structure}\ [\mathrm{Def\text{-}BM.9}(4);\ \mathrm{IT.6}(2)]$$
$$(2)\quad\textbf{THE TWO SECTORS (the doublet's definition):}\qquad W_9(Q)=[z^Q](2{+}z{+}z^{-1})^9=\binom{18}{Q{+}9}\ [\mathrm{IT.9}(1)\ \text{skeleton};\ \mathrm{IT.7}(3)\ \text{Vandermonde};\ \mathrm{BM.135}]:\qquad19\ \text{classes},\ \textstyle\sum=4^9=262144,\ \text{symmetric},\ \text{peak}\ W_9(0)=48620;$$
$$\boxed{\ W_9(+1)=\binom{18}{10}=43758\ \ \text{(the ``tritium'' sector)}\qquad W_9(+2)=\binom{18}{11}=31824\ \ \text{(the ``helium-3'' sector)}\ }\qquad\frac{43758}{31824}=\frac{11}{8}\ \ \text{exact}\ (\gcd=3978);$$
$$\textbf{status of the ratio: a channel-width ratio and the route-(ii) price seed — its mass reading is adjudicated at IT.14,}\ \neg\text{here}\ [\mathrm{BM.30}(5);\ \mathrm{BM.37}(6)]$$
$$(3)\quad\textbf{THE SECTOR DECOMPOSITION (the ensemble is bigger than the species):}\qquad\text{along ANY pure-}\varepsilon\ \text{grouping}\ (280\ \text{of them},\ (1)):\quad W_9(Q)=\!\!\sum_{Q_1+Q_2+Q_3=Q}\!\!\prod_jW_3(Q_j),\qquad W_3=(1,6,15,20,15,6,1)\ [\mathrm{BM.28}(2)\ \text{frozen, reproduced}];$$
$$\text{the exhaustive}\ 7^3=343\ \text{class-triple census reproduces}\ W_9\ \text{entrywise}\ [\text{machine}];\qquad\textbf{the nucleonic sub-census}\ (Q_j\in\{0,{+}1\}\ \text{only}\ [\mathrm{Def\text{-}BM.3}(2),(3)]):$$
$$\begin{array}{c|cccc}Q&0&+1&+2&+3\\\hline\text{nucleonic weight}&20^3{=}8000&3\cdot15\cdot20^2{=}18000&3\cdot15^2\cdot20{=}13500&15^3{=}3375\end{array}\qquad\textbf{the exact shares:}\quad\frac{18000}{43758}=\frac{1000}{2431},\quad\frac{13500}{31824}=\frac{375}{884}\ \ [\text{lowest terms}];$$
$$\textbf{the exotic complements:}\ 25758\ \text{and}\ 18324\ —\ \text{the nucleonic compositions are a MINORITY of their own sectors};\qquad\boxed{\ \text{sector}\ \supsetneq\ \text{species}\ }\ \ [\mathrm{BM.24}(7)\ \text{pattern: composites are ensembles — exactly as the proton's own}\ N{=}3\ \text{sector contains}\ ({+}1,{+}1,{-}1)\ \text{triples}\ [\mathrm{BM.28}(2)]]$$
$$(4)\quad\textbf{THE}\ E_{\mathrm{int}}\ \textbf{ROWS (reading-relative, equal per reading):}\qquad\textbf{disjoint:}\ E_{\mathrm{int}}=6(k{+}1)=18=2{+}2{+}2\ \text{per nucleon, three times}\ [\mathrm{IT.7}(1);\ \mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(2)];\qquad\textbf{tree-connected:}\ 8k{+}6=22\ (k{=}2\ \Sigma_{12}\text{-species connectors, 2 edges each})\ [\mathrm{IT.7}(1)];$$
$$\text{BOTH members share}\ E_{\mathrm{int}}\ \text{in EACH frozen reading}\ (18/18,\ 22/22):\quad\text{the crystallized-count reads are charge-blind}\ [\mathrm{BM.28}(1);\ \text{machine: coefficient arithmetic}];\qquad18\ \text{is OFF the computed-cell floors}\ \{2,6,12,24,60\}\ (\text{hit at}\ k{=}0,1,3)\ [\mathrm{IT.7}(1);\ \mathrm{BM.17}(4)];$$
$$\textbf{the connector residue stays parametric}\ (\mathrm{IT\text{-}O4}):\ \text{whether connector species ever distinguish charge composition is}\ \neg\text{constructed — flagged at IT.14}(2),\ \neg\text{assumed}$$
$$(5)\quad\textbf{the naming rows:}\qquad\text{``tritium''}\ :=\ \text{the}\ Q{=}{+}1\ \text{sector of the}\ N{=}9\ \text{support class}\ (\text{the}\ k{=}2\ \text{member of the}\ 1\mathrm p\text{-}k\mathrm n\ \text{family}\ [\mathrm{IT.6}(2),(3)]);\qquad\text{``helium-3''}\ :=\ \text{the}\ Q{=}{+}2\ \text{sector — the first non-family sector constructed at this level};$$
$$\text{``isobar doublet''}\ :=\ \text{the ordered pair of the two sectors of one support};\qquad\text{all three are QUOTED labels, dictionary partners}\ \neg\text{equals}\ [\mathrm{Def\text{-}BM.3}(1),(7);\ \mathrm{BM.134}(5)];\qquad\text{no isotope is identified}$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{re-produced frozen rows:}\ g(9),\ \tfrac9{11},\ W_3,\ \text{the Vandermonde convolution}\ [\mathrm{IT.6};\ \mathrm{IT.7}(3);\ \mathrm{IT.9}(1),(5)];\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, D2.14, D3.4, EM.9, FT.19 (Parts 1–2); Def-H.32(1), FT.34(3) (Part 3); IT.6(1),(2),(3),(5),(6), IT.7(1),(3), IT.9(1),(5) (this level); AT.63(2) (Level 5); Def-BM.3(1),(2),(3),(7), Def-BM.5(1), Def-BM.9(4), BM.17(1),(4), BM.24(7), BM.28(1),(2), BM.134(5), BM.135, Census FT.35(2),(5) (row-wise) (Part 4); exhaustive set-partition enumeration, exact binomials, Laurent convolution over $\mathbb Z$, exhaustive class-triple census, exact `Fraction` reductions [math; machine: `isobar_transition.py` §§A–C, 11/11].

**Pf.**
$$(1):\ \text{the three engines compared at}\ N{=}9\ (\text{and}\ N{=}8\ \text{as the cross-check});\ \text{the}\ (a,b)\ \text{breakdown term by term};\ 280=9!/(3!^3\,3!)\ [\text{machine A1--A3}];$$
$$(2):\ \text{the Laurent power expanded by exact dictionary convolution and matched to}\ \binom{18}{Q{+}9}\ \text{entrywise};\ \text{sum, symmetry, peak};\ \gcd(43758,31824)=3978\ [\text{machine B1--B2}];\qquad(3):\ W_3\ \text{re-produced as}\ \binom{6}{Q{+}3};\ \text{the 3-fold convolution}\ =W_9\ \text{entrywise}\ [\text{machine B3}];$$
$$\text{the}\ 343\text{-triple census};\ \text{the nucleonic weights and their lowest-term shares};\ \text{the complements}\ [\text{machine C1--C4}];\qquad(4):\ \text{the two readings re-cited from}\ \mathrm{IT.7}(1)\ \text{with the per-reading equality exhibited, and the mixed-reading witness}\ \pm4u\ne0\ [\text{machine E2x}];$$
$$(5),(6):\ \text{record rows}.\ \blacksquare$$

**Phys.** The ninth attachment count is where the family the corpus already built meets the
charge census it already proved: one support, nineteen sectors, two hundred sixty-two thousand
sign states, and inside it the two sectors the directive named. The counting is exact and it is
brutally honest about one thing — a sector is not a species. The nucleonic compositions, one
proton-class and two neutron-class for the lower member, two and one for the upper, carry barely
two fifths and barely two thirds of their sectors' weight; the rest is boundary data with exotic
per-nucleon classes, precisely as the proton's own sector at three attachments has always
contained sign triples no quark-model picture would name. That is not a defect of the
construction; it is the ensemble granularity the baryon tier insisted on, now at nine. What the
two members share is what matters for everything downstream: the attachment count, the grammar
budget, and — in each frozen reading separately — the internal edge count, eighteen disjoint or
twenty-two tree-connected, equal on both members because the crystallized counts are charge-blind.
The ratio eleven eighths falls out of the widths as exact arithmetic, and the tier is careful to
say what it is at birth: a channel-width ratio and a price seed, awaiting the route adjudication
two tags below.

---

### IT.13 — The single-seed transition: the forced carrier inherited coupling-invariantly, and the neutral member conditionally forced

**Thm.**
$$(1)\quad\textbf{the locus and the invariances:}\qquad\text{the ladder acts on ONE seed's registration read}\ q_{\mathrm{core}}=\tfrac12(\sigma_s{-}\sigma_t)\ [\mathrm{D3.4};\ \mathrm{BM.23}(2):\ \text{registration data on the reality line}];$$
$$\text{the read classes are separate}\ [\mathrm{IT.1}(3)]:\ \text{registration}\ (\mathrm R1)\ \neg\text{contraction structure}\implies\boxed{\ N,\ \text{the grouping sector, and the crystallized}\ E_{\mathrm{int}}\ \text{are INVARIANT under the transition}\ }\ [\mathrm{IT.12}(1),(4);\ \text{the two spectator seals untouched}];$$
$$\text{what moves is the boundary charge class — one sector of}\ \mathrm{Def\text{-}BM.5}(1)\ \text{'s ensemble to another:}\quad(Q{=}{+}1,\ N{=}9)\longrightarrow(Q{=}{+}2,\ N{=}9)$$
$$(2)\quad\textbf{the inherited chain}\ [\mathrm{BM.23}(1)\text{--}(5),\ \text{hypotheses verified at}\ N{=}9,\ \neg\text{assumed}]:\qquad E_\pm=\tfrac12(\sigma_1\pm i\sigma_2),\ [\sigma_3,E_\pm]=\pm2E_\pm\ [\mathrm{FT.41}(\mathrm d)];\qquad\Delta q=\pm1;$$
$$\textbf{the alphabet overflow:}\ \{-1,0,{+}1\}{+}1=\{0,{+}1,{+}2\},\ \{-1,0,{+}1\}{-}1=\{-2,-1,0\}:\ \text{both leave the alphabet}\ [\mathrm{EM.9};\ \text{machine: re-enumerated}]\implies\textbf{the change cannot stay inside};$$
$$\textbf{the compensation is unique:}\ \#\{q\in\{-1,0,{+}1\}:q=-\Delta Q\}=1;\qquad\textbf{the vertex balance:}\quad(+1)=(+2)+(-1)+(0)\ [\mathrm{EM.11};\ \text{machine: integers}]$$
$$(3)\quad\textbf{the carrier selection, coupling-invariant:}\qquad\text{the three conditions}\ [\mathrm{BM.23}(5)]:\ (\mathrm i)\ q=-1\ [\ (2)];\ (\mathrm{ii})\ \text{no colour attachment}\ [\text{else the seal breaks}:\ \mathcal C=0\implies\text{the block vanishes}\ [\mathrm{FT.19};\ \mathrm{CT3.18};\ \mathrm{D2.14}]];\ (\mathrm{iii})\ \text{EM activated}\ [\mathrm{D3.3}\ \text{pattern}];$$
$$\textbf{each is a channel-inventory row — independent of}\ N\ \textbf{and of the spectator seals:}\qquad\text{the}\ q\text{-channel is triplet-attached}\ [\mathrm{FT.119}]\ (\text{fails}\ \mathrm{ii});\qquad\text{the}\ \nu\text{-channel is EM-unactivated}\ [\mathrm{FT.142}(1)]\ (\text{fails}\ \mathrm{iii});$$
$$\therefore\ \boxed{\ \textbf{the}\ \ell\text{-channel line},\ q=-1,\ \textbf{is forced and class-unique at}\ N{=}9\ }\ [\mathrm{FT.109}\text{--}\mathrm{FT.113};\ \text{the emitted line is}\ \mathrm{Def\text{-}BM.6}(1)\ \text{'s ``electron'' row, quoted}];$$
$$\textbf{the coupling row:}\ \text{the emitted unsealed lepton register couples through the ONE global Def-H.32 configuration sum}\ [\mathrm{AT.42}(2);\ \mathrm{IT.8}(1):\ \text{the lepton-saturation flag's connector side — the boundary read is grouping-invariant}]$$
$$(4)\quad\textbf{the neutral member: admissible}\ \longrightarrow\ \textbf{CONDITIONALLY FORCED (the on-record upgrade re-derived on the doublet):}\qquad\textbf{the two-body impossibility at equal parent/daughter masses}\ [\mathrm{IT.12}(4);\ \mathrm{BM.41}(2)\ \text{pattern}]:$$
$$E_d+E_\ell=m_T,\quad E_i=\sqrt{m_i^2{+}p^2}\ [\mathrm{BM.34}(4)\ \text{vacuum gauge}]:\qquad E_d-m_d=-\frac{m_\ell^2}{2m_T}<0\ \ \forall m_\ell>0\ [\text{machine: exact witnesses}];$$
$$\textbf{the Källén companion:}\ \lambda=m_\ell^2(m_\ell^2-4m_T^2):\ \text{spacelike for}\ 0<m_\ell<2m_T;\quad m_\ell\ge2m_T\implies E_d\le-m_T<0\ [\text{machine: both branches cover every}\ m_\ell>0];$$
$$\therefore\ \text{every kinematically admissible vertex carries}\ \ge3\ \text{members};\qquad\text{the third member's charge is forced to}\ 0\ \text{by unique enumeration}\ [\text{machine}];\qquad\text{the class is unique: the}\ \nu\text{-channel}\ [\mathrm{BM.41}(3);\ \mathrm{BM.23}(5)\ \text{'s eliminations}];$$
$$\textbf{the forcing is kinematic}\ +\ \text{uniqueness,}\ \neg\text{a number conservation}\ [\neg\exists\ \text{a lepton-number read in the inventory}\ [\mathrm{BM.23}(6);\ \mathrm{FT.81}(4)\ \text{pattern}]];\qquad\text{the line index within the}\ \nu\text{-triplet is}\ \neg\text{derived}\ [\mathrm{FT.145}(3):\ \neg\text{a mixing matrix}]$$
$$(5)\quad\textbf{the positivity premise, isolated (the adversarial row):}\qquad m_\ell=0\implies E_d-m_d=0:\ \text{the two-body vertex becomes marginally on-shell — the strictness NEEDS}\ m_\ell>0\ [\text{machine: witness exhibited}];$$
$$\textbf{supplied,}\ \neg\text{assumed:}\quad\text{transport:}\ m_\ell^2\ge M^2(A_0{-}B_0)>0\ [\mathrm{BM.39}(1)];\qquad\text{informational:}\ m_\ell=E_{\mathrm{int}}\ln2/\mathfrak h\ge2\ln2/\mathfrak h>0\ [\mathrm{FT.44}(4);\ \mathrm{FT.28}\ \text{the digon floor};\ \tfrac12<\ln2<1\ \text{enclosure, re-certified}];\qquad m_\nu\ge0\ [\mathrm{EW.33}\ \mathrm{PSD}];\ \text{and strictly positive on the rung-one row}\ [\mathrm{BM.96}]$$
$$(6)\quad\textbf{the arrow and the weight:}\qquad\text{forward-only}\ [\mathrm{BM.23}(9);\ \mathrm{FT.144}(2);\ \mathrm{A6}:\ \neg\exists\tau^{-1}];\qquad\Gamma\ \text{a resolvent in}\ \varepsilon_q\ \text{alone},\ \text{its pole at}\ |w|\ge2\ [\mathrm{BM.23}(7)];$$
$$\varepsilon_q=0\implies\Gamma=0\ \text{exactly}\ [\mathrm{BM.23}(8)]:\ \textbf{a non-flickering doublet never decays};\qquad\Gamma\ \text{is a weight per tick in the ledger order}\ [\mathrm{D1.8};\ \mathrm{P5}],\ \neg\text{a rate per external second}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(6),\ \text{with}\ (3)\ \text{'s eliminations and}\ (4)\ \text{'s class uniqueness as inventory re-citations};\qquad\textbf{re-derived on the doublet:}\ \mathrm{BM.23}(2)\text{--}(4),\ \mathrm{BM.41}(2)\text{--}(3);\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** A6, D1.8, D3.3, D3.4, D3.10, P5, CT3.18, D2.14, EM.9, EM.11, FT.19, FT.41(d), FT.81(4), FT.109, FT.112, FT.113, FT.119, FT.142(1), FT.144(2), FT.145(3) (Parts 1–3); Def-H.32(1),(2), FT.28, FT.34(3), FT.44(4), Def-BM.6(1), Def-BM.5(1), BM.23(1),(2),(3),(4),(5),(6),(7),(8),(9), BM.34(4), BM.39(1), BM.41(2),(3), BM.96, EW.33 (this part's canon loci); AT.42(2) (Level 5); IT.1(3), IT.6(2), IT.8(1), IT.12(1),(4) (this level); exact ternary-alphabet censuses, integer charge enumeration, exact rational two-body kinematics with cleared polynomial identities, Källén branch census, rigorous $\ln2$ enclosure [math; machine: `isobar_transition.py` §D, 5/5 + §E1].

**Pf.**
$$(1):\ \text{the read-class separation re-cited}\ [\mathrm{IT.1}(3)];\ \text{registration flips leave}\ |R|,\ \text{the support and the grouping untouched}\ [\text{the grammar is structural data};\ \mathrm{IT.6}(2)\ \text{'s boundary-data row}];$$
$$(2):\ \text{the shifted sets against the alphabet}\ [\text{machine D1}];\ \#\{q{=} {-}\Delta Q\}{=}1\ \text{and the balance}\ (+1){=}(+2){+}(-1){+}(0)\ [\text{machine D2}];$$
$$(3):\ \text{the three conditions and the two eliminations re-cited row-wise — each an inventory fact, no}\ N\text{-dependence in any of them};\ \text{the coupling row re-cited from}\ \mathrm{IT.8}(1);$$
$$(4):\ E_d{=}(m_T^2{+}m_d^2{-}m_\ell^2)/(2m_T)\ \text{at}\ m_d{=}m_T{:}\ E_d{-}m_T{=}{-}m_\ell^2/(2m_T)\ \text{on exact rational witnesses};\ \lambda\ \text{cleared and sign-censused on both branches}\ [\text{machine D3}];\ \text{the third charge by unique enumeration}\ [\text{machine D4}];$$
$$(5):\ \text{the}\ m_\ell{=}0\ \text{witness}\ [\text{machine D5}];\ \text{the positivity rows re-cited, the informational floor on the}\ \tfrac12<\ln2<1\ \text{enclosure}\ [\text{machine E1, E5}];\qquad(6),(7):\ \text{re-citation and assembly}.\ \blacksquare$$

**Phys.** Nothing about the transition had to be rebuilt for nine attachments, and the tier's
whole design is to prove that rather than assert it. The ladder touches one seed's registration;
registration is not contraction; so the support, the grouping budget and the crystallized edge
count all stand still while the boundary charge class moves — the composite walks from one sector
of its own ensemble to the next, and the walk leaves the alphabet, exactly as it did at three.
The carrier argument is three inventory facts and an integer: the compensating charge is unique,
the colour-attached channel would break the very seals holding the doublet together, the
electromagnetically inert channel could not carry the read that changed, and one class is left —
the same class the baryon era named, now serving a nine-attachment isobar. The neutral partner
arrives the honest way: not because a lepton number is conserved (no such read exists), but
because two bodies cannot share this decay — at equal parent and daughter masses the daughter
falls below its own mass shell for every positive emitted mass, on both Källén branches, and the
third member's zero charge is the only value the alphabet allows. One adversarial witness keeps
the argument from smuggling its premise: at zero lepton mass the impossibility softens to
marginality, so the strictness is owned by the positivity rows, cited not assumed. The arrow and
the weight come along unchanged — forward-only, a resolvent in the flicker threshold, silent at
zero flicker: a doublet that cannot flicker cannot decay, per tick, with no second anywhere in
it.

---

### IT.14 — The Q-value of the doublet: the route-relative verdict, the priced ratio, and the conditional kinematics

**Thm.**
$$(1)\quad\textbf{the Q-value, formed:}\qquad Q_\beta\ :=\ m\bigl(\text{``}^3\mathrm H\text{'' sector}\bigr)-m\bigl(\text{``}^3\mathrm{He}\text{'' sector}\bigr)-m_\ell-m_\nu\qquad[\mathrm{BM.41}(4)\ \text{pattern at}\ N{=}9;\ \text{every member a formed read}]$$
$$(2)\quad\textbf{the route census and the verdict:}\qquad\begin{array}{l|l|l}\textbf{read}&\textbf{the doublet's splitting}&\textbf{the verdict}\\\hline(\mathrm a)\ \text{informational}\ [\mathrm{BM.35}(4);\ \mathrm{FT.44}(4)]&m=E_{\mathrm{int}}u,\ u=\ln2/\mathfrak h:\ E_{\mathrm{int}}\ \text{equal per reading}\ (18/18,\ 22/22)\ [\mathrm{IT.12}(4)]\implies\Delta m=0&Q_\beta=-(m_\ell{+}m_\nu)\le-2u<0\ \ [\text{machine}]\\(\mathrm b)\ \text{normalized ensemble}\ [\mathrm{BM.28}(4)(\mathrm i);\ \mathrm{BM.30}(3)]&\text{uniform sector factors cancel — structural at}\ N{=}9\ [\mathrm{FT.107}(2)\ \text{'s}\ \sigma\text{-free}\ \Delta S;\ \text{machine: factor census}]&Q_\beta<0\ \ \text{as}\ (\mathrm a)\\(\mathrm c)\ \text{curvature flux}\ [\mathrm{BM.20}(1);\ \mathrm{BM.41}(4)(\mathrm c)]&V_{\mathrm{eff}}\sim E^{-3}\ \text{is a function of}\ E_{\mathrm{int}}\ \text{alone}\ [\mathrm{BM.28}(1)]:\ \text{identical monomials}&Q_\beta<0\ \ \text{as}\ (\mathrm a)\\(\mathrm d)\ \text{route (ii), total deficit}\ [\mathrm{BM.28}(4)(\mathrm{ii});\ \mathrm{BM.30}(1),(2)]&T(Q)=W_9(Q)\overline{\Delta S}:\ \ T(+1)/T(+2)=11/8\ \text{exact}\ [\text{machine}]&Q_{\mathrm{ii}}=\tfrac38T(+2)-(m_\ell{+}m_\nu):\ \textbf{sign INDETERMINATE without scale data}\ [\text{machine: witnesses}\ {+}2,\ {-}7]\end{array}$$
$$\boxed{\ \textbf{the verdict: the}\ N{=}9\ \beta^-\ \textbf{vertex is kinematically CLOSED on every ADOPTED read — the corpus does not make ``tritium'' heavier than ``helium-3'' on any of them}\ }\qquad[\mathrm{BM.41}(4)(\mathrm e)\ \text{pattern};\ \mathrm{P5}:\ \neg\text{an external mass-difference datum}]$$
$$(3)\quad\textbf{the ratio's exact status (the directive's claim, adjudicated):}\qquad\frac{43758}{31824}=\frac{11}{8}\ \ \textbf{is derived and exact AS THE ROUTE-(ii) TOTAL-DEFICIT MEASURE PRICE of the doublet}\ [\mathrm{BM.28}(4)(\mathrm{ii});\ \mathrm{BM.30}(1)\ \text{pattern at}\ N{=}9];$$
$$\textbf{route (ii) is priced,}\ \neg\textbf{adopted:}\ \text{``no route is adopted here; adoption requires a logged declaration''}\ [\mathrm{BM.30}(5)];\quad\text{``exact as measure prices, barred as physical masses''}\ [\mathrm{BM.37}(6)];\quad\text{``exact named prices,}\ \neg\text{masses''}\ [\mathrm{BM.97}\ \mathrm{Rmk}];\quad\text{prices}\ \neg\text{masses}\ [\text{HistLog}\ \S\mathrm{V.32}];$$
$$\text{and even under adoption the verdict would be sign-indeterminate pending scale data}\ [(2)(\mathrm d)],\ \neg\text{``structurally heavier''}:$$
$$\boxed{\ \textbf{a new declaration is OWED to the Era-2 ledger: the mass-read route choice}\ [\mathrm{BM.30}(5)]\ \text{— the Architect's act, none issued here}\ }\qquad\text{it joins the standing owed list}\ [\mathrm{AT.63}(5)\ \text{'s pattern: the lift, the vielbein, the P4 profile, the read rules,}\ \varepsilon_q,\ (\varkappa,\beta),\ e_0]$$
$$(4)\quad\textbf{the conditional kinematics (the hypothesis}\ Q_\beta\ge0\ \textbf{of some adopted specification, CARRIED ON ITS FACE — false on every adopted read by}\ (2)):$$
$$0=\vec p_{\,d}+\vec p_\ell+\vec p_\nu;\qquad Q_\beta=\mathrm{KE}_d+\mathrm{KE}_\ell+\mathrm{KE}_\nu,\quad\mathrm{KE}_i=E_i-m_i\ [\mathrm{BM.34}(5);\ \mathrm{BM.41}(5)\ \text{pattern}];$$
$$\textbf{the endpoint:}\quad E_\ell^{\max}=\frac{m_T^2+m_\ell^2-(m_{\mathrm{He}}{+}m_\nu)^2}{2m_T},\qquad E_\ell^{\max}+E_{\mathrm{rec}}=m_T\ \ [\text{machine: exact on witnesses}];\qquad m_T{=}m_{\mathrm{He}},\ m_\nu{=}0:\ \ E_\ell^{\max}=\frac{m_\ell^2}{2m_T};$$
$$\text{the continuum of}\ E_\ell\ \text{values is chart-side content}\ [\mathrm{CT2.6}\ \text{'s hypotheses at the point of use}];\qquad\textbf{no adopted specification satisfies the hypothesis — the section stands conditional, exactly as}\ \mathrm{BM.41}(5)\ \text{'s}$$
$$(5)\quad\textbf{the metric rows, corrected and instantiated:}\qquad E_{\mathrm{total}}=N\sqrt{m_{\mathrm{rest}}^2+p^2}-N^ip_i\ [\mathrm{BM.34}(4);\ \mathrm{BM.35}(7);\ \mathrm{Def\text{-}BM.10}(5)]:\quad\boxed{\ N\ \textbf{is the LAPSE and}\ N^i\ \textbf{the shift}\ }\ —\ \neg\text{the attachment count};$$
$$\text{the vacuum gauge:}\ E^2=m^2{+}p^2\ (c{=}1\ [\mathrm{D2.9}]);\qquad\mathrm{KE}=N\bigl(\sqrt{m^2{+}p^2}-m\bigr)\ge0\ [\mathrm{BM.34}(5)];$$
$$\textbf{the zero-point instance at}\ E_{\mathrm{int}}{=}18:\quad E^2\ge\tfrac74m_{\mathrm{hid}}^2=\tfrac74\cdot18^2u^2=567\,u^2,\qquad\mathrm{KE}_{\mathrm{NR}}\ge\tfrac38\cdot18\,u=\tfrac{27}4u\qquad[\mathrm{BM.34}(6)\ \text{instantiated};\ \text{machine: exact coefficients}]$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(2)(\mathrm a)\text{--}(\mathrm d),(4)\ \text{under its face-carried hypothesis},\ (5);\qquad\textbf{priced,}\ \neg\textbf{adopted:}\ (3)\ \text{'s}\ 11/8;\qquad\textbf{owed:}\ (3)\ \text{'s declaration};\qquad\neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a currency mixing}\ [\mathrm{BM.83};\ \mathrm{BM.134}(5)],\ \neg\text{a P4 addition}\ [\mathrm{P1}]$$

**Req.** P1, P5, D2.9, CT2.1, CT2.6 (Parts 1–2); Def-H.32(2), FT.28, FT.44(4), FT.107(2),(3), Def-BM.10(5) (Part 3); Def-BM.4(1), BM.20(1),(3), BM.28(1),(4), BM.30(1),(2),(3),(5), BM.34(4),(5),(6), BM.35(4),(7), BM.37(3),(6), BM.39(1), BM.41(4),(5), BM.83, BM.97, BM.134(5) (Part 4); HistLog §V.32 (pointer); IT.7(1), IT.9(1), IT.12(2),(4), IT.13(4),(5) (this level); AT.63(5) (Level 5); exact `Fraction` route arithmetic, symbolic multiples of $u=\ln2/\mathfrak h$, rigorous $\ln2$ enclosure with exact tail bound, opposite-sign rational witnesses, cleared endpoint identities [math; machine: `isobar_transition.py` §E, 9/9].

**Pf.**
$$(1),(2)(\mathrm a):\ \Delta m=(E_{\mathrm{int}}^T-E_{\mathrm{int}}^{\mathrm{He}})u=0\cdot u\ \text{in both frozen readings}\ [\text{machine E2}];\ Q_\beta=-(m_\ell{+}m_\nu)\le-2u<0\ \text{on the}\ \tfrac12<\ln2<1\ \text{enclosure}\ [\text{machine E1}]\ \text{and}\ m_\ell\ge2u\ [\mathrm{IT.13}(5)];$$
$$(2)(\mathrm b):\ \text{the uniform-factor cancellation censused over exact}\ \mathrm{Fraction}\ \text{factors including}\ 43758,\ 31824,\ \tfrac{11}8,\ \tfrac{1000}{2431}\ [\text{machine E3}];\qquad(2)(\mathrm c):\ \text{coefficient identity at}\ E^{-3},\ 18^3=5832\ [\text{machine E6}];$$
$$(2)(\mathrm d),(3):\ T(+1)/T(+2)=W_9(+1)/W_9(+2)=\tfrac{11}8\ [\text{machine E4}];\ Q_{\mathrm{ii}}=\tfrac38T(+2)-(m_\ell{+}m_\nu):\ \text{witnesses}\ (T{=}8,s{=}1)\mapsto{+}2\ \text{and}\ (T{=}8,s{=}10)\mapsto{-}7\ [\text{machine E4}];\ \text{the direction witness}\ \tfrac8{11}\ne\tfrac{11}8\ [\text{machine E4x}];$$
$$(4):\ \text{the endpoint and recoil identities exact on rational witnesses};\ \text{the}\ m_\nu{=}0\ \text{specialization}\ [\text{machine E7}];\qquad(5):\ \tfrac74\cdot324=567,\ \tfrac38\cdot18=\tfrac{27}4\ [\text{machine E5}];\ \text{the lapse/shift symbols re-cited}\ [\mathrm{BM.34}(1),(4)];\qquad(6):\ \text{assembly}.\ \blacksquare$$

**Phys.** The verdict is the tier's spine, and it runs against the directive at exactly one
place — the place the corpus has already litigated twice. The combinatorics is confirmed to the
integer: forty-three thousand seven hundred fifty-eight against thirty-one thousand eight hundred
twenty-four, eleven eighths exact. But eleven eighths of what? The corpus froze the answer in its
baryon era: a total-deficit ratio is a measure price, and measure prices are barred as physical
masses; adopting one as "the mass" is a logged declaration, and none exists. On every read the
corpus has actually adopted, the doublet is exactly degenerate — same support, same grammar
budget, same edge count in each frozen reading, charge-blind geometry — so the Q-value collapses
to minus the emitted masses and the vertex is kinematically closed, the nine-attachment echo of
the single-nucleon verdict. Even inside the priced route the sign waits on scale data: two exact
rational witnesses sit on opposite sides, and the tier exhibits both rather than choosing. What
remains of the directive's kinematic story is the conditional section — the endpoint algebra,
face-carrying a hypothesis no adopted read satisfies — and the metric rows with their symbols
corrected: the N in the dispersion is the lapse, not the attachment count, and the honest
nine-attachment instance of the metric step is the zero-point bound at coefficient five hundred
sixty-seven. One new obligation is written into the ledger: if the Architect ever wants eleven
eighths to be a mass statement, the route choice is the declaration to make — and even then the
verdict would be "undetermined pending scales," never "structurally heavier."

---

### IT.15 — The premise corrections, the rename record, the open rows, and the status of Tier IT.4

**Thm.**
$$(1)\quad\textbf{THE PREMISE CORRECTIONS (on the record, the house discipline):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``}\langle m\rangle\propto W(Q)\ [\mathrm{BM.28}(4)(\mathrm{ii}),\ \mathrm{BM.30}(2)]\ \dots\ \text{tritium is structurally heavier}\ \dots\ \text{thermodynamically unstable''}&\textbf{CORRECTED}\ [\mathrm{IT.14}(2),(3)]:\ 11/8\ \text{is exact as the ROUTE-(ii) MEASURE PRICE — priced,}\ \neg\text{adopted}\ [\mathrm{BM.30}(5);\ \mathrm{BM.37}(6);\ \mathrm{BM.97}\ \mathrm{Rmk};\ \text{HistLog}\ \S\mathrm{V.32}];\ \text{on every adopted read the doublet is exactly degenerate and the vertex kinematically CLOSED}\ [\mathrm{BM.41}(4)(\mathrm e)\ \text{pattern}];\ \text{even under adoption the sign is scale-indeterminate}\ [\mathrm{BM.41}(4)(\mathrm d)\ \text{pattern}]\\\text{``}E_{\mathrm{total}}=N\sqrt{m_{\mathrm{rest}}^2+p^2}-N_ip_i\text{'' with}\ N\ \text{the attachment count}&\textbf{CORRECTED}\ [\mathrm{IT.14}(5)]:\ N\ \text{is the LAPSE,}\ N^i\ \text{the shift}\ [\mathrm{BM.34}(4);\ \mathrm{BM.35}(7);\ \mathrm{Def\text{-}BM.10}(5)];\ \neg\exists\ \text{a frozen row multiplying a dispersion by}\ N{=}9\\\text{``}E_{\mathrm{int}}=18\ \text{(each nucleon contributes 6)}\text{'' flat}&\textbf{QUALIFIED}\ [\mathrm{IT.12}(4)]:\ 18\ \text{is the DISJOINT reading; the tree reading is}\ 22\ [\mathrm{IT.7}(1)];\ \text{both give}\ E_T{=}E_{\mathrm{He}}\ \text{— that is what closes the Q-value — but the flat ``18'' silently selects a reading, and 18 is off the floors}\ \{2,6,12,24,60\}\\\text{``the}\ \nu\ \text{is the unique ADMISSIBLE carrier}\ [\mathrm{BM.23}(6)]\text{''}&\textbf{UPGRADED, re-cited:}\ \mathrm{BM.41}(3)\ \text{upgraded}\ \mathrm{BM.23}(6)\ \text{ON RECORD — admissible}\ \longrightarrow\ \textbf{conditionally forced}\ (\text{kinematic}\ +\ \text{uniqueness},\ \neg\text{a number conservation});\ \text{re-derived on the doublet}\ [\mathrm{IT.13}(4)]\\\text{``tritium is the}\ Q{=}{+}1\ \text{sector of the}\ N{=}9\ \text{ensemble}\ [\mathrm{Def\text{-}BM.5}]\text{''}&\textbf{CONFIRMED with the refinement}\ [\mathrm{IT.12}(3)]:\ \text{right at ensemble granularity}\ [\mathrm{BM.24}(7)\ \text{pattern}];\ \text{at species granularity the sector}\ \supsetneq\ \text{the nucleonic compositions}\ (18000/43758,\ 13500/31824)\end{array}$$
$$(2)\quad\textbf{CONFIRMED WITHOUT QUALIFICATION:}\qquad N=9=3\cdot3\ [\mathrm{IT.6}(2)];\qquad Q{=}{+}1\to Q{=}{+}2\ \text{at fixed}\ N\ [\mathrm{IT.13}(1)];\qquad\text{the ladder/overflow/compensation/selection chain}\ [\mathrm{BM.23}(1)\text{--}(5)]\ \text{with coupling-invariant eliminations};\qquad W_9(+1){=}43758,\ W_9(+2){=}31824,\ \tfrac{11}8\ \text{exact}\ [\mathrm{IT.12}(2)];\qquad\text{``helium-3''}\ =\ \text{the}\ Q{=}{+}2\ \text{member of the}\ N{=}9\ \text{sealed ensemble}\ [\mathrm{IT.12}(5)]$$
$$(3)\quad\textbf{THE RENAME RECORD (the directive's first act):}\qquad\text{Level 6, opened as ``the Molecular era'' (session 9), is RENAMED ``the Isotopic era''; the molecular level is DEFERRED — its placement in the level map is the Architect's act,}\ \neg\text{pre-empted here};$$
$$\text{the retag is the bijection}\ \mathrm{ML}.n\mapsto\mathrm{IT}.n\ (n{=}1..11),\ \mathrm{ML\text{-}O}k\mapsto\mathrm{IT\text{-}O}k\ (k{=}1..4),\ \S\mathrm{Cal\text{-}ML}\mapsto\S\mathrm{Cal\text{-}IT},\ \S\mathrm{Open\text{-}ML}\mapsto\S\mathrm{Open\text{-}IT}:\quad\textbf{content-preserving, executed as its own commit, suite re-run green before any new content}\ (4\ \text{checkers},\ 42\ \text{markers});$$
$$\text{clause names are preserved: IT.4's ``molecular necessity'' keeps its name — it is the derived theorem motivating the deferred level};\qquad\mathrm{AT.63}(4)\ \text{'s tree row received a LIVE PATH FIX}\ [\text{the session-8 pattern}];\ \text{the closed record's name mentions stay as closure-time statements}\ [\mathrm{AT.63}(2)];$$
$$\text{the prefix scan found}\ \neg\text{an}\ \mathrm{IT}.\ \text{collision corpus-wide before the retag}\ [\text{machine: the gate's F3 registry}]$$
$$(4)\quad\textbf{the Architect's standing flag, recorded}\ \neg\textbf{pre-empted:}\qquad\text{IT.4's exception}\ [\mathrm{IT.8}(3)]\ \textbf{is}\ \neg\textbf{triggered by this tier:}\ \text{the emitted}\ \ell\ \text{line is UNSEALED — a carrier,}\ \neg\text{a bound member};$$
$$\text{the electron-saturated BOUND members remain IT-O2's amplitude side — this tier is the closest approach so far, recorded as such}$$
$$(5)\quad\textbf{THE OPEN ROWS:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{content}\\\hline(\mathrm{IT\text{-}O2})\ \text{sharpened}&\textbf{the}\ N{=}9\ \textbf{amplitude locus is now concrete:}\ \text{the Def-H.32 ensemble sum over the}\ 1540\ \text{grouping sectors with}\ (-1)^{\aleph}\ \text{dressing}\ [\mathrm{Def\text{-}H.32}(2)];\ \text{the}\ 280\ \text{pure-}\varepsilon\ \text{sectors carry the nucleonic decomposition}\ [\mathrm{IT.12}(3)];\ \mathrm{AT.44}/\mathrm{AT\text{-}O30}\ \text{engines reusable}\\\hline(\mathrm{IT\text{-}O4})\ \text{gating}&\text{if connector species ever distinguish charge composition, IT.14}(2)\ \text{'s per-reading degeneracy must be re-derived — flagged at}\ \mathrm{IT.12}(4),\ \neg\text{assumed};\ \text{the frozen skeleton stays}\ \mathrm{FT.34}(3)\ \text{'s}\ k(\Gamma){=}k_1{+}k_2{+}d_{12}\\\hline\textbf{new (owed)}&\textbf{the mass-read route choice}\ [\mathrm{BM.30}(5);\ \mathrm{IT.14}(3)]:\ \text{a declaration, the Architect's act — the only route to an}\ 11/8\ \text{mass statement, and even then sign-indeterminate pending scales}\\\hline(\mathrm{IT\text{-}O1}),(\mathrm{IT\text{-}O3})&\text{unchanged}\ [\mathrm{IT.1};\ \mathrm{IT.3}(6)]\end{array}$$
$$(6)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\qquad\text{§Cal-IT stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses throughout}),\ \mathrm{FT.55}(1),\ \mathrm{CT3.22},\ \mathrm{BM.143}(1)$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{isobar\_transition.py}\to\textbf{25/25 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{5 checkers, 67 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{4 Part 6 documents PASS};\qquad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, FT.34(3), FT.55(1), CT3.22 (Parts 1–2); Def-H.32(2), Def-BM.3(1),(7), BM.30(5), BM.37(6), BM.83, BM.97, BM.134(5), BM.143(1) (canon loci); AT.39(8), AT.44, AT.63(2),(4),(5), AT-O30 (Level 5); IT.1, IT.3(6), IT.4, IT.6, IT.7, IT.8(3), IT.9, IT.12, IT.13, IT.14 (this level); the rename's prefix scan and the runner/gate re-runs [math; machine: `isobar_transition.py` full suite + the level runner + the level gate].

**Pf.** The correction table verified against each cited locus row by row; the rename executed
mechanically with the suite re-run green before and after (two commits); the flag row and the open
rows assembled from IT.8(3), IT.11(3),(4) and this tier's residues; the runner and the gate re-run
end to end. No new mathematics is introduced at this tag. $\blacksquare$

**Phys.** The record closes the way the record always closes: corrections beside confirmations,
both exact. The directive's combinatorics survived the audit to the last integer — forty-three
thousand seven hundred fifty-eight, thirty-one thousand eight hundred twenty-four, eleven eighths
— and its decay grammar is the corpus's own grammar, inherited at nine attachments without a
single new elimination. What did not survive is the one step the corpus has already adjudicated
twice: a measure price is not a mass. Eleven eighths is real, exact, and barred; on every read
the corpus has adopted, the doublet is degenerate and the decay is closed, and the tier says so
plainly, then writes down the only door that could open — a route-choice declaration, the
Architect's act, owed not issued. The rename sits beside the physics because it is physics-
adjacent bookkeeping done honestly: the level is isotopic now, the tags moved by a bijection, the
molecular necessity theorem keeps its name and its force, and the deferred molecular level waits
for its own placement. The exception flag stays untriggered — an emitted electron is not a bound
one — and the two open rows leave with sharper questions than they came with: the amplitude sum
over fifteen hundred forty grouping sectors, and the connector species that could, if it ever
distinguished charge composition, reopen the degeneracy this tier proved per reading. Nothing
measured entered; nothing was declared; no isotope was identified.

---

## §Cal-IT — unchanged from Tier IT.4

**Empty at this tier.** The tier's parametric residues are recorded as open rows and one owed
declaration, not parameters: the route choice [IT.14(3); BM.30(5)] joins the inherited slots
[$\mathfrak h$ (P1); $\varepsilon_q$ (AT-O27); $e_0$ (EM.25(7), ¬issued); $(\varkappa,\beta)$
(AT-O3); $\rho_{\mathrm B}$, $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared); the P4
transport profile; the lift and the vielbein (AT.60)].

## §Open-IT additions from Tier IT.4

| row | content | locus |
|---|---|---|
| (IT-O2), sharpened | the **$N=9$ amplitude locus**: the Def-H.32 ensemble sum over the 1540 grouping sectors, $(-1)^{\aleph}$-dressed; the 280 pure-$\varepsilon$ sectors carry the nucleonic decomposition; route-(iii)-type amplitude ratios at $N=9$ wait on it (the $N=3$ precedents: $58/13$, $2398/401$ [BM.28(4)(iii)]) | IT.14(2)(d); IT.12(1),(3); IT.11(3) |
| (IT-O4), gating note | if connector species distinguish charge composition, the per-reading degeneracy of IT.14(2) must be re-derived before any verdict row is reused | IT.12(4); IT.14(2)(a) |
| new (owed) | **the mass-read route choice** [BM.30(5)] — a declaration, the Architect's act; the only route to an $11/8$ mass statement, and even then the Q-value sign is scale-indeterminate | IT.14(3); IT.15(5) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4)]: (IT-O1) the transit-leg amplitude,
(IT-O3) the handshake-indicator operational theory; and the Level-5 ledger [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.5: the hydrogen isotope sequence — the forward-verified $N{=}9$ doublet, the grammar tipping point, and the binding-read adjudication

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.5 — the Architect's isotope-cutoff
directive: an independent forward compute that re-derives the $N{=}9$ doublet without assuming the
decay products, the contraction-grammar tipping point along $N=3,6,9,12$, the $N{=}12$ boundary-data
census, and the binding-read adjudication that closes the informational bridge and opens the
inter-nucleon binding as a gated row.
**Tags.** IT.16–IT.18. **Pattern.** the construction tiers (IT.1/IT.2/IT.3/IT.4's shape), premise
audit logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays
empty; no clause of Parts 1–4, of Level 5's closed record, or of Tier IT.4 is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/isotope_cutoff.py` → **20/20 exact** (fresh Laurent
convolution and fresh set-partition enumeration — an INDEPENDENT engine, not an import of
`isobar_transition.py`; the IT.2 grammar recurrence and closed form re-implemented for the
cross-check); `run_all_level6.py` → **6 checkers, 87 exact markers, 0 failures**;
`check_level6_format.py` → the gate over all five Part 6 documents. Exact arithmetic: integer
binomials, Laurent convolution over $\mathbb Z$, exhaustive class-triple enumeration, `Fraction`
shares and sign censuses.
**No floating point in any assertion. No measured value enters any clause [P5] — the physical
$\beta$ endpoint ($\sim 18.6$ keV) and the hydrogen-4 resonance widths stay quarantined [EXT]
scoring targets, cited nowhere. No species identification [Def-BM.3(1),(7)] — "tritium",
"helium-3", "hydrogen-4", "deuteron", "resonance" stay quoted labels of the identification layer;
the derived objects are the $Q{=}{+}1$ and $Q{=}{+}2$ BOUNDARY SECTORS of the $N{=}9$ support class,
the $N{=}12$ support class, and the ledger's own grammar and binding reads.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13): *"Prove the Hydrogen Isotope Cutoff at $k{=}2$
(Tritium) via the $\delta$-Dominance and Binding Read Collapse … for $N\ge12$ the flicker ensemble
cannot form a stable bound-state composite, and instead exists only as a transient unbound
resonance,"* in four steps (the grammar tipping point; the binding-read collapse $\mathcal B_{\mathrm{ens}}\ge0$;
the boundary degradation / resonance classification; the adjudication), together with a
Tritium$\to$He-3 $\beta^-$ structural derivation — executed under the standing instruction *"verify
the tritium computation WITHOUT ASSUMING THE DECAY PRODUCTS; run a forward compute; we are in
exploration state, so if lacking data don't [give] a nogo but add it as an open thing; if possible
to close via simple mathematical calculation bridge rather than requiring physical insight, perform
the derivation."* **State note:** the directive's $\beta^-$ construction was already delivered and
certified as Tier IT.4 (session 12); this tier supplies the independent forward verification IT.4
invites and pushes on the cutoff itself, with four premise corrections logged at IT.18(4).

---

### IT.16 — The forward compute: the $N{=}9$ doublet re-derived independently, decay-product-free

**Thm.**
$$(1)\quad\textbf{THE FORWARD COMPUTE (from the support combinatorics ALONE):}\qquad W_9(Q)=[z^Q](2{+}z{+}z^{-1})^9=\binom{18}{Q{+}9}\ \ \textbf{by fresh Laurent convolution}$$
$$\text{matched to the binomial ENTRYWISE:}\quad19\ \text{classes},\quad\sum_QW_9(Q)=4^9=262144,\quad W_9(Q)=W_9(-Q),\quad\text{peak}\ W_9(0)=48620;$$
$$\boxed{\ W_9({+}1)=\binom{18}{10}=43758\ \ \text{(the ``tritium'' sector)}\qquad W_9({+}2)=\binom{18}{11}=31824\ \ \text{(the ``helium-3'' sector)}\ }\qquad\frac{43758}{31824}=\frac{11}{8}\ \ \text{exact}\ (\gcd=3978);$$
$$\textbf{no decay product is assumed:}\ \text{the two sectors are read off the charge census of the}\ N{=}9\ \text{support,}\ \neg\text{from the transition}\ [\mathrm{IT.9}(1)\ \text{skeleton};\ \mathrm{BM.135};\ \mathrm{Def\text{-}BM.8}(6)]$$
$$(2)\quad\textbf{THE GRAMMAR, RE-PRODUCED AT}\ k{=}2\ \textbf{BY THREE FRESH ENGINES:}\qquad g(9)=1540=\underbrace{1260}_{(a,b)=(3,1)}{+}\underbrace{280}_{(0,3)}\quad(\text{enumeration}\wedge\text{recurrence}\wedge\text{closed form});$$
$$\text{the pure-}\varepsilon\ \text{count}\ 280=\tfrac{9!}{3!^3\,3!}\ \ (\text{the unordered triple partitions});\qquad\frac{g_\delta}{g}=\frac9{11}\ \ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{BM.31}(2);\ \mathrm{IT.6}(1)\ \text{engine, re-implemented}]$$
$$(3)\quad\textbf{THE SECTOR DECOMPOSITION (the ensemble is bigger than the species):}\qquad W_9(Q)=\!\!\sum_{Q_1+Q_2+Q_3=Q}\!\!\prod_jW_3(Q_j),\quad W_3=(1,6,15,20,15,6,1)\ \ \textbf{(the exhaustive}\ 7^3{=}343\ \textbf{census reproduces}\ W_9\ \textbf{entrywise)};$$
$$\text{the nucleonic sub-census}\ (Q_j\in\{0,{+}1\}\ [\mathrm{Def\text{-}BM.3}(2),(3)]):\quad(8000,\ 18000,\ 13500,\ 3375)\ \ \text{at}\ Q=(0,{+}1,{+}2,{+}3);$$
$$\textbf{the exact shares:}\quad\frac{18000}{43758}=\frac{1000}{2431},\quad\frac{13500}{31824}=\frac{375}{884}\ \ [\text{lowest terms}];\qquad\textbf{the exotic complements:}\ 25758\ \text{and}\ 18324;$$
$$\boxed{\ \text{sector}\ \supsetneq\ \text{species: the nucleonic compositions are a MINORITY of their own sectors}\ (18000<25758,\ 13500<18324)\ }\ [\mathrm{IT.12}(3);\ \mathrm{BM.24}(7)\ \text{pattern}]$$
$$(4)\quad\textbf{THE VERDICT:}\qquad\boxed{\ \textbf{IT.12's tritium computation is CONFIRMED to the integer by an independent forward compute}\ }$$
$$\text{the status of}\ \tfrac{11}8\ \text{is unchanged from}\ \mathrm{IT.14}(3):\ \text{a channel-width ratio and the route-(ii) price seed,}\ \textbf{priced}\ \neg\textbf{adopted}\ [\mathrm{BM.30}(5);\ \mathrm{BM.37}(6)],\ \neg\text{a physical mass}\ [\mathrm{P5}]$$

**Req.** P5, D3.4, EM.9 (Parts 1–2); Def-H.32(1) (Part 3); IT.6(1), IT.7(3), IT.9(1), IT.12(2),(3), IT.14(3) (this level); AT.63(2) (Level 5); Def-BM.3(2),(3), Def-BM.8(6), BM.24(7), BM.28(2), BM.30(5), BM.37(6), BM.135 (Part 4); fresh Laurent convolution over $\mathbb Z$, exact binomials, exhaustive set-partition enumeration and class-triple census, exact `Fraction` reductions [math; machine: `isotope_cutoff.py` §§A, 6/6].

**Pf.**
$$(1):\ \text{the Laurent power built by dictionary convolution from}\ \{z^{-1}{:}1,\ z^0{:}2,\ z^{+1}{:}1\}\ \text{nine times, matched to}\ \binom{18}{Q{+}9}\ \text{entrywise; sum, symmetry, peak}\ [\text{machine A1}];\ \text{the sectors and}\ \gcd(43758,31824){=}3978\ [\text{machine A2}];\ \text{the reversed ratio}\ \tfrac8{11}\ne\tfrac{11}8\ [\text{machine A2x}]$$
$$(2):\ \text{three engines compared at}\ N{=}9\ (g\_brute{=}g\_dp{=}g\_closed{=}1540);\ \text{the}\ (a,b)\ \text{breakdown term by term};\ 280{=}9!/(3!^3\,3!)\ [\text{machine A3}]$$
$$(3):\ W_3\ \text{re-produced as}\ \binom{6}{Q{+}3};\ \text{the 3-fold convolution}{=}W_9\ \text{entrywise over the exhaustive}\ 343\ \text{triples};\ \text{the nucleonic weights, their lowest-term shares and complements}\ [\text{machine A4}];\ \text{the minority witness and}\ \tfrac{1000}{2431}\ne\tfrac12\ [\text{machine A4x}]$$
$$(4):\ \text{the cross-check of every value against IT.12's certified row; the price status re-cited from IT.14}(3).\ \blacksquare$$

**Phys.** The verification the Architect asked for is a from-scratch recomputation, not a re-run: a
fresh Laurent convolution of the ninth power of the ternary charge generating function, a fresh
enumeration of the set partitions into pairs and triples, and an exhaustive sweep of the three
hundred forty-three class triples — none of it importing the transition tier's numbers, all of it
landing on them exactly. Forty-three thousand seven hundred fifty-eight against thirty-one thousand
eight hundred twenty-four, eleven eighths, one thousand five hundred forty groupings split twelve
sixty and two eighty, nucleonic shares one thousand over twenty-four thirty-one and three seventy-five
over eight hundred eighty-four. The computation is deliberately blind to the decay: it reads the two
sectors straight off the charge census of the nine-attachment support, so what it confirms is that
the doublet's boundary data is exactly what IT.12 said, independent of any claim about where it goes.
And it confirms the honest part too — the nucleonic compositions are a minority of their own sectors,
so a sector is not a species, and eleven eighths remains a width ratio and a price seed, not a mass.

---

### IT.17 — The isotope-sequence grammar tipping point and the $N{=}12$ boundary census

**Thm.**
$$(1)\quad\textbf{THE SEQUENCE CENSUS (three engines,}\ N{=}3,6,9,12\textbf{):}\qquad\begin{array}{c|cccc}N=3(k{+}1)&3&6&9&12\\\hline g&1&25&1540&164395\\ g_\varepsilon\ (\text{pure-}\varepsilon\ \text{backbone})&1&10&280&15400\\ g_\delta\ (\ge\text{one}\ \delta)&0&15&1260&148995\\ g_\delta/g_\varepsilon&0&\tfrac32&\tfrac92&\tfrac{387}{40}\\ \delta\ \text{share}\ g_\delta/g&0&\tfrac35&\tfrac9{11}&\tfrac{387}{427}\end{array}$$
$$\boxed{\ \textbf{both}\ g_\delta/g_\varepsilon\ \textbf{and the}\ \delta\ \textbf{share are STRICTLY monotone for}\ N\ge6;\ \ \text{at}\ N{=}12\ \text{the}\ \delta\text{-containing groupings outnumber the backbone}\ 387{:}40\ }\ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{BM.31}(2);\ \mathrm{IT.6}]$$
$$(2)\quad\textbf{THE PROTECTION IS UNIQUE TO}\ N{=}3\ \textbf{(premise P1):}\qquad g_\delta(3)=0:\ \text{a}\ \delta\ \text{sub-pairing on 3 attachments leaves 1 dangling}\implies\mathcal C{=}0\implies\text{the colour block vanishes}\ [\mathrm{D2.14};\ \mathrm{FT.19}];$$
$$\mathcal E_\delta(\mathcal X_{N=3})=\varnothing\ [\mathrm{BM.31}(1),(6)];\qquad g_\delta(N)>0\ \ \forall N\in\{4,\dots,12\}\ [\mathrm{BM.31}(2);\ \text{machine}];$$
$$\textbf{the DEUTERON}\ (N{=}6)\ \textbf{already mixes}\ (15\ \delta\text{-containing vs}\ 10\ \text{pure-}\varepsilon):\quad\boxed{\ \delta\text{-dominance is a monotone DEGREE from}\ N{=}6,\ \neg\text{a kind-change first appearing at}\ N{=}12\ }$$
$$(3)\quad\textbf{THE}\ N{=}12\ \textbf{BOUNDARY DATA:}\qquad W_{12}(Q)=[z^Q](2{+}z{+}z^{-1})^{12}=\binom{24}{Q{+}12}:\ 25\ \text{classes},\ \sum{=}4^{12}{=}16777216,\ \text{peak}\ W_{12}(0){=}\binom{24}{12}{=}2704156;$$
$$\textbf{the}\ \Theta_{\mathrm{int}}\textbf{-class mixture}\ [\mathrm{BM.31}(4);\ \text{Census}\ \mathrm{FT.49}(3);\ \mathrm{FT.22};\ \mathrm{FT.34}(3)]:\ \text{pure-}\varepsilon\ (g_\varepsilon(12){=}15400)\to\Theta_{\mathrm{int}}\in4\mathbb Z\ \text{(baryon-type)};\ \ \delta\text{-containing}\ (g_\delta(12){=}148995)\to\Theta_{\mathrm{int}}\in2\mathbb Z;$$
$$\text{grammar-weighted shares}\ \tfrac{40}{427}\ (4\mathbb Z)\ \text{and}\ \tfrac{387}{427}\ (2\mathbb Z),\ \text{summing to}\ 1;\qquad4\mathbb Z\subsetneq2\mathbb Z\ (\text{witness}\ \Theta_{\mathrm{int}}{=}2):\ \textbf{the statistics label is a PARTIAL separator}$$
$$(4)\quad\textbf{THE HORIZON HOLDS UNIFORMLY (premise P2 refuted as stated):}\qquad\text{``interior fuzz bleeding into the boundary'' contradicts the measurement-horizon theorem}\ [\mathrm{IT.2};\ \mathrm{AT.29};\ \mathrm{AT.32}(1)]:$$
$$\neg\text{a rung}\ge2\ \text{summand leaks},\ \ \text{the interior is void-closed}\ [\mathrm{D0.7};\ \mathrm{BM.143}(1)],\ \ \text{the accessible content is EXACTLY}\ (Q,\ \Theta_{\mathrm{int}}\ \text{class},\ S){+}|R|{+}n\ \ \textbf{at every}\ N;$$
$$\text{machine witness: the width is a pure function of}\ Q\ \text{at both}\ N{=}9\ (19\ \text{classes})\ \text{and}\ N{=}12\ (25\ \text{classes}):\quad\boxed{\ \text{what changes at}\ N{=}12\ \text{is the ENSEMBLE's statistics mixture}\ (3),\ \neg\text{the sharpness of any member's triple}\ }$$
$$(5)\quad\textbf{THE RESONANCE CATEGORY (premise P4):}\qquad\text{a resonance IN THE LEDGER is an eigenvalue of a multi-chain ensemble with its two threshold functions}\ [\mathrm{Def\text{-}BM.17};\ \mathrm{BM.114}\text{--}\mathrm{BM.117}];$$
$$\text{``nothing is stable as a category'' and the materialization locus is}\ \neg\emptyset\ \text{at any}\ n\ [\text{Tier}\ \mathrm{BM.21}\ \text{locus}]:\quad\boxed{\ \neg\text{a sharp bound-vs-scattering dichotomy exists to import};\ \ \text{the}\ N{=}12\ \text{classification needs the multi-chain eigenvalues}=\mathrm{IT\text{-}O2}\ }$$

**Req.** P5, D2.14, D3.4, EM.9, FT.19, FT.22, CT3.17a(2), CT3.18 (Parts 1–2); Def-H.32(1), FT.34(3) (Part 3); IT.2, IT.6(1),(2), IT.7(1), IT.9(1),(5), IT.12(1),(4) (this level); AT.29, AT.32(1), AT.63(2) (Level 5); Def-BM.3(2),(3), Def-BM.8(6), Def-BM.9(3),(4), BM.24(7), BM.31(1),(2),(4),(6), BM.114, BM.117, BM.135, BM.143(1), Def-BM.17, Census FT.49(3), D0.7 (Part 4 / Part 1); the three grammar engines, fresh Laurent convolution, exact integer and `Fraction` arithmetic [math; machine: `isotope_cutoff.py` §§B–C, 8/8].

**Pf.**
$$(1):\ \text{the census by enumeration}\ (N\le9),\ \text{the recurrence and the closed form; the monotonicity of both ratios over the computed sequence; the non-constancy witness}\ [\text{machine B1, B2, B2x}]$$
$$(2):\ g_\delta(3){=}0\ \text{from the dangling-attachment annihilation}\ [\mathrm{D2.14};\ \mathrm{FT.19}];\ g_\delta(N){>}0\ \text{for every}\ N{=}4..12;\ \text{the deuteron's}\ (15,10)\ \text{mix}\ [\text{machine B3}]$$
$$(3):\ W_{12}\ \text{by fresh convolution matched to}\ \binom{24}{Q{+}12};\ \text{the}\ 4\mathbb Z/2\mathbb Z\ \text{shares from}\ g_\varepsilon(12),g_\delta(12);\ \Theta_{\mathrm{int}}{=}2\in2\mathbb Z\setminus4\mathbb Z\ [\text{machine C1, C2, C2x}]$$
$$(4):\ \text{the width-as-pure-function-of-}Q\ \text{witness at both}\ N;\ \text{the horizon rows re-cited}\ [\mathrm{IT.2};\ \mathrm{AT.29};\ \mathrm{AT.32}(1)]\ [\text{machine C3}]$$
$$(5):\ \text{the resonance definition and the no-stable-category row re-cited from}\ \mathrm{Def\text{-}BM.17}\ \text{and the Tier}\ \mathrm{BM.21}\ \text{locus}.\ \blacksquare$$

**Phys.** Walk the isotope sequence through the grammar and one number tells the whole story: the
share of groupings that contain at least one mesonic δ contraction climbs from nothing at the
protected three-attachment junction, through three fifths at the deuteron, nine elevenths at the
nine-attachment doublet, to three hundred eighty-seven four-hundred-twenty-sevenths at twelve — where
the δ-containing groupings outnumber the pure baryonic backbone almost ten to one. That is the
tipping point the directive named, and it is exact. But the census is honest about what it does not
say: the protection it erodes was only ever unique to the single three-attachment junction, and the
deuteron at six attachments already mixes without the record calling it unbound, so δ-dominance is a
matter of degree that begins at the first bound multi-nucleon system, not a wall that appears at
twelve. The boundary data at twelve is sharp — a clean twenty-five-class charge width, a statistics
label split forty to three-eighty-seven between the baryonic and mesonic phase classes — and the
measurement horizon that guarantees that sharpness holds at every attachment count, which is why
"interior fuzz" is the wrong picture: the ensemble spans two statistics classes, but no member's
boundary blurs. And the ledger has no bound-versus-scattering category to sort twelve into; a
resonance here is an eigenvalue with a threshold, and the twelve-attachment eigenvalues are not built.

---

### IT.18 — The binding-read adjudication: the bridge that closes, the connector residue, and IT-O5

**Thm.**
$$(1)\quad\textbf{THE BRIDGE THAT CLOSES (the informational binding vanishes exactly):}\qquad E^{\mathrm{disj}}_{\mathrm{int}}(3(k{+}1))=6(k{+}1)\ \ \text{is exactly additive over the}\ (k{+}1)\ \text{nucleons}\ [\mathrm{IT.7}(1);\ \mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(2);\ \mathrm{AT.40}(3)]:$$
$$\boxed{\ \mathcal B_{\mathrm{info}}=\bigl(E^{\mathrm{disj}}_{\mathrm{int}}-\textstyle\sum_{\text{nucleons}}6\bigr)u=\bigl(6(k{+}1)-6(k{+}1)\bigr)u=0\cdot u=0\ \ \forall k\in\{0,1,2,3\}\ }\qquad[\mathrm{BM.21}(1)\ \text{generalized along the family}]$$
$$\implies\textbf{the cutoff CANNOT arise on the informational read:}\ \ \text{the binding is zero UNIFORMLY, so no sign change locates a last-bound member}\ [\text{machine: the coefficient is the integer}\ 0\ \text{at every}\ k]$$
$$(2)\quad\textbf{THE CONNECTOR RESIDUE (the only read that could distinguish, gated):}\qquad E^{\mathrm{tree}}_{\mathrm{int}}=8k{+}6;\quad E^{\mathrm{tree}}_{\mathrm{int}}-E^{\mathrm{disj}}_{\mathrm{int}}=2k=(0,2,4,6)\ \ \text{at}\ k{=}0,1,2,3\ [\mathrm{IT.7}(1);\ \mathrm{IT.12}(4);\ \mathrm{FT.34}(3)];$$
$$\text{the}\ 2k\ \text{is the CONNECTOR residue}\ (k\ \Sigma_{12}\text{-species connectors, 2 edges each});\quad\boxed{\ \text{its bound-vs-stress SIGN is the connector SPECIES (count, winding}\ d\text{, fusion)}=\mathrm{IT\text{-}O4},\ \textbf{UNCONSTRUCTED}\ }$$
$$(3)\quad\textbf{THE CONSTRUCTED-READ CENSUS (every derived binding read is}\ \le0\textbf{):}\qquad\text{two-chain}\ [\mathrm{BM.137}(3)]:\ \ \mathcal B^{(2)}_{\mathrm{ens}}=-\tfrac{4u}{1{+}u}\tfrac{\ln2}{\mathfrak h}=-\tfrac{16\varepsilon_q}{1{+}4\varepsilon_q}\tfrac{\ln2}{\mathfrak h}<0\ \ \forall\varepsilon_q>0\ (=0\iff\varepsilon_q{=}0);$$
$$\text{three-constituent}\ [\mathrm{BM.21}(4)]:\ \ \mathcal B(S_j;1,1,1)<0\ \ \forall S_j\in\{0,1,2,3\};\qquad\boxed{\ \textbf{neither is an INTER-nucleon (multi-seal) binding: that object is ABSENT from the inventory}\ }$$
$$(4)\quad\textbf{THE PREMISE CORRECTIONS (on the record, the house discipline):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``}\delta\text{-dominance at}\ N{=}12\implies\text{unbound''}&\textbf{REFINED}\ [\mathrm{IT.17}(1),(2)]:\ \delta\text{-admixture exists from}\ N{=}6\ (\text{the bound deuteron});\ \text{the protection is unique to}\ N{=}3;\ \text{the}\ \delta\ \text{share is a monotone degree,}\ \neg\text{a binding criterion}\\\text{``interior fuzz bleeds into the boundary''}&\textbf{REFUTED}\ [\mathrm{IT.17}(4)]:\ \text{the measurement horizon holds uniformly}\ [\mathrm{IT.2};\ \mathrm{AT.29}];\ \text{what changes is the ensemble statistics mixture}\\\text{``}\mathcal B_{\mathrm{ens}}\ge0\ \text{at}\ N{=}12,\ <0\ \text{for}\ N\le9\text{''}&\textbf{NO DERIVED SUPPORT}\ [\mathrm{IT.18}(1),(3)]:\ \mathcal B_{\mathrm{info}}{=}0\ \text{at every}\ k;\ \text{every constructed read}\ \le0;\ \neg\text{an inter-nucleon binding exists}\\\text{``classify}\ N\ge12\ \text{as scattering resonances''}&\textbf{GATED}\ [\mathrm{IT.17}(5)]:\ \text{a ledger resonance is an eigenvalue}\ [\mathrm{Def\text{-}BM.17}];\ \neg\text{a bound-vs-scattering category};\ \text{needs}\ \mathrm{IT\text{-}O2}\end{array}$$
$$(5)\quad\textbf{THE ADJUDICATION (Step 4, honest — recorded}\ \neg\textbf{forced):}\qquad\boxed{\ \textbf{the hydrogen isotope cutoff at}\ k{=}2\ \textbf{is}\ \neg\textbf{a derived row; it is a CONJECTURE gated on}\ \mathrm{IT\text{-}O4}{+}\mathrm{IT\text{-}O2}\ }$$
$$\textbf{NEW OPEN ROW IT-O5 — the inter-nucleon (multi-seal) binding read and the isotope cutoff:}\ \ \text{the last-bound-member question for the}\ 1\mathrm p\text{-}k\mathrm n\ \text{family;}$$
$$\text{gated on}\ \mathrm{IT\text{-}O4}\ (\text{the connector species: the sign of the}\ 2k\ \text{tree residue})\ \text{and}\ \mathrm{IT\text{-}O2}\ (\text{the Def-H.32 amplitude sum over the}\ N{=}3(k{+}1)\ \text{grouping sectors,}\ (-1)^{\aleph}\text{-dressed});$$
$$\text{the empirical hydrogen-4 resonance fact is a}\ [\mathrm{P5}]\ \textbf{scoring target, quarantined, cited in no clause};\qquad\text{IT-O5 sharpens,}\ \neg\text{contradicts, IT.4's residues}\ [\mathrm{IT.15}(5)]$$
$$(6)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses}),\ \mathrm{FT.55}(1),\ \mathrm{CT3.22},\ \mathrm{BM.143}(1)$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{isotope\_cutoff.py}\to\textbf{20/20 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{6 checkers, 87 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{5 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, D0.7, FT.22, FT.34(3), FT.55(1), CT3.22 (Parts 1–2); Def-H.32(1),(2), FT.19, FT.44(4), FT.107(2),(3), FT.114 (Part 3); IT.1(8), IT.2, IT.6, IT.7(1), IT.9, IT.12(4), IT.14(3), IT.15(5), IT-O2, IT-O4 (this level); AT.29, AT.32(1), AT.39(8), AT.40(3), AT.44, AT.63(2),(5), AT-O30 (Level 5); Def-BM.3(1),(7), Def-BM.17, BM.17(1), BM.21(1),(4), BM.30(5), BM.37(6), BM.83, BM.114, BM.117, BM.134(5), BM.137(3), BM.143(1), Census FT.35(2) (Part 4); exact integer additivity certificates, symbolic multiples of $u=\ln2/\mathfrak h$, `Fraction` sign censuses over a rational $\varepsilon_q$ grid [math; machine: `isotope_cutoff.py` §D, 6/6].

**Pf.**
$$(1):\ 6(k{+}1)-(k{+}1)\cdot6=0\ \text{as an integer certificate at}\ k{=}0,1,2,3;\ \text{the neither-positive-nor-negative witness}\ [\text{machine D1, D1x}]$$
$$(2):\ (8k{+}6)-6(k{+}1)=2k\ \text{term by term};\ \text{the residue}\ (0,2,4,6)\ \text{exhibited; the sign gated on the connector species re-cited from}\ \mathrm{IT.12}(4)\ [\text{machine D2}]$$
$$(3):\ \mathcal B^{(2)}_{\mathrm{ens}}=-\tfrac{4u}{1{+}u}\ \text{with}\ u{=}4\varepsilon_q\ \text{re-derived from}\ D_n{=}(1{-}u^n)/(1{-}u)\ \text{and sign-censused}\ <0\ \text{on a 63-point rational grid};\ \mathrm{BM.21}(4)\text{'s sign re-cited};\ \text{zero non-negative witnesses}\ [\text{machine D3, D3x}]$$
$$(4):\ \text{the correction table verified against each cited locus row by row}\ [\mathrm{IT.17};\ \mathrm{IT.18}(1),(3);\ \mathrm{Def\text{-}BM.17}]$$
$$(5)\text{--}(8):\ \text{the adjudication assembled from}\ (1)\text{--}(4);\ \text{IT-O5 recorded with its gate dependencies named};\ \text{the runner and the gate re-run end to end. No new mathematics is introduced at}\ (6)\text{--}(8).\ \blacksquare$$

**Phys.** The directive asked for a sign flip in the binding, and the honest answer is that the
corpus can prove exactly one thing about the sign and it is the opposite of useful for a cutoff: on
the informational read the binding is not merely small at twelve, it is identically zero at three,
six, nine and twelve alike, because the disjoint internal-edge count is exactly the sum of the
nucleons'. A read that is zero everywhere cannot pick out a last bound member. The only read that
could distinguish is the connected one, and the connected one carries a residue of two-k edges whose
very sign — binding or stress — is the connector species the record has not built. Every binding the
corpus *has* built, the two-chain floor and the three-constituent sector difference, comes out
negative or zero, and neither is a binding *between* nucleons; that object is simply absent. So the
cutoff at k equals two is recorded the way the record records anything it cannot yet derive: as an
open row with its gates named, not as a no-go and not as a forced theorem. The hydrogen-four
resonances of the identification layer stay a scoring target behind the firewall, cited in no clause.
What the tier does close is real and exact — the forward verification of the doublet, the monotone
grammar tipping point, the sharp twelve-attachment boundary census, and the vanishing informational
binding — and what it opens, IT-O5, is sharper for having been localized to the connector and the
amplitude sum rather than left as a hunch. Nothing measured entered; nothing was declared; no isotope
was identified.

---

## §Cal-IT — unchanged from Tier IT.5

**Empty at this tier.** The tier's parametric residues are recorded as open rows, not parameters:
the connector species [IT-O4], the amplitude sum [IT-O2], the inter-nucleon binding read [IT-O5],
and the inherited owed declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$
(P1), $\varepsilon_q$ (AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3),
$\rho_{\mathrm B}$, $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile,
the lift and the vielbein (AT.60).

## §Open-IT additions from Tier IT.5

| row | content | locus |
|---|---|---|
| **IT-O5 (new)** | **the inter-nucleon (multi-seal) binding read and the hydrogen isotope cutoff** — the last-bound-member question for the $N{=}3(k{+}1)$ family. The informational binding is exactly $0$ at every $k$ [IT.18(1)], so the cutoff, if derived, must come from the ensemble/connected read: gated on **IT-O4** (the connector species fixing the sign of the $2k$ tree residue [IT.18(2)]) and **IT-O2** (the Def-H.32 amplitude sum over the grouping sectors, $(-1)^{\aleph}$-dressed). The resonance classification [Def-BM.17] waits on the same amplitude locus. Recorded ¬forced (exploration state) | IT.18(5); IT.17(5); IT.18(2) |
| IT-O4, note | the connector species now also gates IT-O5's binding sign, not only IT.14(2)'s per-reading degeneracy — the $2k$ tree residue [IT.18(2)] is the locus where a connector's binding-vs-stress character would enter | IT.18(2); IT.12(4) |
| IT-O2, note | the $N{=}12$ amplitude locus joins the $N{=}9$ one: the Def-H.32 sum over the $g(12){=}164395$ grouping sectors; the pure-$\varepsilon$ $g_\varepsilon(12){=}15400$ carry the baryon-type $\Theta_{\mathrm{int}}\in4\mathbb Z$ class [IT.17(3)] | IT.17(3); IT.18(5) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5)]: (IT-O1) the transit-leg amplitude,
(IT-O3) the handshake-indicator operational theory, the owed mass-read route choice [IT.14(3)], and
the Level-5 ledger [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.6: the nucleon–nucleon connector species (IT-O4 constructed) and the isotope-cutoff relocation

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.6 — the Architect's directive to construct
the nucleon–nucleon connector species (IT-O4) and adjudicate the isotope cutoff (IT-O5): the
connector as a derived ledger object, the sign of the $2k$ residue, and the relocation of the cutoff
to the ensemble/amplitude binding.
**Tags.** IT.19–IT.21. **Pattern.** the construction tiers (IT.4/IT.5's shape), premise audit logged
in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays
empty; no clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.4/IT.5 is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/connector_species.py` → **17/17 exact** (the frozen Σ₁₂
connector row consumed; the IT.5 grammar/E_int engines reused); `run_all_level6.py` → **7 checkers,
104 exact markers, 0 failures**; `check_level6_format.py` → the gate over all six Part 6 documents.
Exact arithmetic: integer edge counts, `Fraction` charge reads and binding coefficients, symbolic
multiples of $u=\ln2/\mathfrak h$, exhaustive end-sign enumeration.
**No floating point in any assertion. No measured value enters any clause [P5] — the hydrogen-4
resonance widths and every binding energy in MeV stay quarantined [EXT] scoring targets, cited
nowhere. No species identification [Def-BM.3(1),(7)] — "neutron", "proton", "deuteron", "tritium",
"hydrogen-4" stay quoted labels; the derived object is the OPEN BIDIRECTIONAL CONNECTOR between two
$\varepsilon$-sealed 3-juncture supports and its ledger reads.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13b): *"Construct the Nucleon-Nucleon Connector
Species (IT-O4) and Adjudicate the Isotope Cutoff (IT-O5) … define the exact ledger object (count,
winding $d$, fusion/sharing rules) … evaluate the sign of the $2k$ residue and adjudicate whether the
family terminates at $k{=}2$ … If the connector species cannot be formed from the current inventory,
state the exact missing definition."* **Executed with the finding that the connector is NOT a missing
definition** — it is the frozen Σ₁₂ connector, and its winding gap (R10) was already reclassified as
registration data at BM.143(3); three premise corrections logged at IT.20(4).

---

### IT.19 — The connector species constructed: the open bidirectional Σ₁₂ connector, $d=0$

**Thm.**
$$(1)\quad\textbf{THE OBJECT (frozen, not new):}\qquad\text{the connector is the BIDIRECTIONAL pair}\ \ e_{12}=(q_1,p_2),\ \bar e_{12}=(p_2,q_1)\ \ \text{of}\ \Sigma_{12}\ [\text{Census}\ \mathrm{FT.35};\ \mathrm{BM.17}(1)]:$$
$$E_{\mathrm{int}}(\Sigma_{12})=6=(c_1{:}\,2)+(c_2{:}\,2)+(\textbf{connector}{:}\,2)\qquad[\text{Census}\ \mathrm{FT.35}(2);\ \mathrm{D0.8}:\ E_{\mathrm{int}}=|R|\ \text{is a directed-edge cardinality}];$$
$$\boxed{\ \textbf{the connector's}\ E_{\mathrm{int}}\ \textbf{contribution is}\ 2,\ \textbf{frozen cell data}\ }\qquad\text{count:}\ k\ \text{connectors for}\ (k{+}1)\ \text{nucleons in a tree}$$
$$(2)\quad\textbf{THE WINDING}\ d=0\ \textbf{(the (R10) gap discharged):}\qquad\Gamma=c_1\cdot P\cdot c_2\cdot\bar P,\quad k(\Gamma)=k_1{+}k_2{+}d_{12},\quad d_{12}=\Theta(P)=\Theta(\bar P)\ge0\ [\mathrm{BM.2}(2);\ \mathrm{FT.34}(3);\ \text{Census}\ \mathrm{FT.50}(2)];$$
$$\text{an OPEN chain carries}\ S=0\ [\mathrm{Def\text{-}H.32}(4)];\qquad\text{an open connector}\ \Rightarrow\ d=0\ \Rightarrow\ \varepsilon=(-1)^d=+1\ [\mathrm{BM.129}(3);\ \mathrm{BM.143}(3)];$$
$$\text{the meson AND the baryon connectors are OPEN}\ [\mathrm{BM.129}(1),(4)];\qquad\boxed{\ (R10)\ \textbf{is registration data,}\ \neg\textbf{a missing definition:}\ d\in\mathbb Z_{\ge0},\ \varepsilon=(-1)^d,\ \text{the value fixed at crystallization}\ [\mathrm{BM.143}(3)]\ }$$
$$(3)\quad\textbf{THE}\ E_{\mathrm{int}}\ \textbf{ROW, DISCHARGED FROM PARAMETRIC TO CONSTRUCTED:}\qquad E^{\mathrm{tree}}_{\mathrm{int}}=6(k{+}1)+2k=8k{+}6=(6,14,22,30)\ \ \text{at}\ k{=}0,1,2,3\ [\mathrm{IT.7}(1);\ \mathrm{IT.12}(4);\ \mathrm{IT.18}(2)]:$$
$$\text{the connector excess over the disjoint}\ 6(k{+}1)\ \text{is exactly}\ 2k=(0,2,4,6);\qquad\text{adversarial:}\ k{\pm}1\ \text{connectors give}\ 8k{+}8\,/\,8k{+}4\ne30\ \text{at}\ k{=}3\ [\text{machine}]$$
$$(4)\quad\textbf{THE CHARGE TELESCOPES (the family's}\ Q{=}{+}1\ \textbf{preserved):}\qquad q(e_{12})+q(\bar e_{12})=\tfrac{\sigma_{q_1}-\sigma_{p_2}}{2}+\tfrac{\sigma_{p_2}-\sigma_{q_1}}{2}=0\ \ \text{for every end-sign assignment}\ (4/4):$$
$$\boxed{\ \text{the bidirectional connector contributes NET ZERO charge}\ \Rightarrow\ Q_{\text{total}}=\textstyle\sum Q_{\text{nucleon}}=+1\ \ \forall k\ }\qquad[\mathrm{EM.9b};\ \mathrm{AT.41}(2),(3);\ \mathrm{BM.135};\ \mathrm{IT.7}(3)]$$
$$(5)\quad\textbf{FUSION/SHARING — DISTINCT SEALED SUPPORTS:}\qquad N=3(k{+}1)=(3,6,9,12);\qquad\text{the connector adds EDGES,}\ \neg\text{shared attachments}\ [\mathrm{IT.6}(2);\ \mathrm{Def\text{-}BM.9}(4);\ \mathrm{BM.1}(1):\ \text{each support colour-complete on its own}];$$
$$\text{attachment-sharing/fusion would be a CLOSED connector (a fused junction), registration data}\ [\mathrm{BM.143}(3)]\ \text{but}\ \neg\text{the sealed-composite connector species (open}\ [\mathrm{BM.129}(1),(4)])$$
$$(6)\quad\textbf{THE SATURATION IS UNIFORM (born at the first composite):}\qquad\text{``composition creates saturation''}\ [\text{Census}\ \mathrm{FT.35}(4),\text{Rmk}]:\ \text{each connector pushes its junction vertices to rung}\ 4:$$
$$D_{\mathrm{tick}}(4)=2^5=32>C_{\mathrm{cap}}=16\Rightarrow O(4)=16,\ \ D^-\text{-configured, the excess RETAINED}\ \neg\text{accessible}\ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT4.1}\text{--}\mathrm{CT4.3};\ \mathrm{D4.2}];$$
$$\text{the nucleon junctions sit at}\ n{=}3\ (D_{\mathrm{tick}}(3)=16=C_{\mathrm{cap}},\ \text{saturated but ADMISSIBLE});\qquad\boxed{\ \text{the saturation is}\ k\text{-INDEPENDENT —}\ \neg\text{a}\ k{=}3\ \text{event}\ }$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(6);\qquad\textbf{re-produced frozen rows:}\ \text{the}\ \Sigma_{12}\ \text{connector cell, the winding additivity, the open-chain}\ S{=}0\ \text{row};\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, D0.8, D1.4, D2.14, D3.4, CT0.5, CT0.6, CT3.18, CT4.1, CT4.3, D4.2, EM.9 (Parts 1–2); Def-H.32(4), FT.22, FT.34(3), FT.40, FT.44(4), FT.60(6), Def-H.38 (Part 3); IT.6(2), IT.7(1),(3), IT.12(4), IT.18(2) (this level); AT.41(2),(3), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.9(4), BM.1(1), BM.2(2), BM.17(1), BM.128(7), BM.129(1),(3),(4), BM.135, BM.143(3), Census FT.35(2),(4),(5), FT.50(2) (Part 4); exact integer edge arithmetic, `Fraction` charge reads, exhaustive end-sign enumeration [math; machine: `connector_species.py` §§A–B, 10/10].

**Pf.**
$$(1):\ \text{Census FT.35(2)'s decomposition row re-cited}\ (2{+}2{+}2{=}6);\ \text{the connector's}\ 2\ \text{is the frozen summand}\ [\text{machine A1}]$$
$$(2):\ \mathrm{Def\text{-}H.32}(4)\text{'s open-chain}\ S{=}0\ \text{row};\ \mathrm{BM.129}(3)\text{'s}\ d{=}0\Rightarrow\varepsilon{=}+1;\ \mathrm{BM.143}(3)\text{'s (R10) reclassification re-cited};\ \text{the closed-connector witness}\ \varepsilon(d{=}1){=}{-}1\ne{+}1\ [\text{machine A2, A2x}]$$
$$(3):\ 6(k{+}1){+}2k{=}8k{+}6\ \text{term by term at}\ k{=}0..7;\ \text{the}\ k{\pm}1\ \text{miscount witnesses}\ [\text{machine A4, A4x}];\qquad(4):\ \text{the four end-sign assignments, each netting}\ 0\ [\text{machine A5}]$$
$$(5):\ N{=}3(k{+}1)\ \text{re-cited from}\ \mathrm{IT.6}(2);\ \text{the open/closed connector distinction from}\ \mathrm{BM.129}(1),(4)\ [\text{machine A6}];\qquad(6):\ D_{\mathrm{tick}}(n){=}2^{n+1}\ \text{at}\ n{=}3,4,5\ \text{against}\ C_{\mathrm{cap}}{=}16\ [\text{machine B1, B2}].\ \blacksquare$$

**Phys.** The directive asked for a new object and the canon handed back one it had already frozen:
the connector between two sealed nucleons is the same bidirectional channel that holds the Σ₁₂
neutron together, contributing exactly two directed edges, and the winding question that IT-O4 named
as its obstruction — (R10) — turns out to have been closed at the baryomesonic era's own house-cleaning
as registration data. An open connector, which is what bridges two distinct supports, carries zero
winding and positive parity; the baryon and the meson have always used open connectors, so the family's
connectors do too. Everything the tier needs follows: the internal-edge count of the tree-connected
composite is six per nucleon plus two per connector, reproducing the eight-k-plus-six that IT.7 could
only write parametrically; the bidirectional pair telescopes to zero net charge, so the family's total
charge stays plus one at every k; the supports stay distinct at three attachments each; and the dark
saturation the connector creates at its junction vertices is born at the very first composite and never
changes. The connector is derived, uniform, and benign — which is exactly why it cannot be where the
isotope cutoff lives.

---

### IT.20 — The sign of the $2k$ residue: read-relative, and it does not adjudicate the cutoff

**Thm.**
$$(1)\quad\textbf{THE INFORMATIONAL READ (the tree binding is uniformly negative):}\qquad m=E_{\mathrm{int}}\cdot u,\ \ u=\ln2/\mathfrak h>0\ [\mathrm{FT.44}(4)]:$$
$$\mathcal B^{\mathrm{tree}}_{\mathrm{info}}=\bigl(6(k{+}1)-(8k{+}6)\bigr)u=-2k\,u=(0,-2,-4,-6)u\ \ \text{at}\ k{=}0,1,2,3;\qquad\boxed{\ \mathcal B^{\mathrm{tree}}_{\mathrm{info}}<0\ \ \forall k\ge1,\ \ \text{strictly monotone,}\ \neg\text{crossing zero}\ }$$
$$\Rightarrow\textbf{the cardinality read flags the DEUTERON}\ (k{=}1)\ \textbf{``unbound'' by}\ -2u\ \textbf{exactly as it flags}\ k{=}3\ \textbf{by}\ -6u:\ \ \text{it cannot locate a last-bound member}\ [\mathrm{BM.21}(1)\ \text{pattern}]$$
$$(2)\quad\textbf{THE CONNECTOR IS}\ k\textbf{-IDENTICAL:}\qquad(d,\ \Delta E_{\mathrm{int}},\ \varepsilon)=(0,\,2,\,{+}1)\ \ \text{at every}\ k=0,1,2,3\ [\mathrm{IT.19}(2),(3),(6)]:$$
$$\boxed{\ \text{the connector does}\ \neg\text{change character at}\ k{=}3\ \Rightarrow\ \text{it cannot terminate the family at}\ k{=}2;\ \ \text{the grammar/connector structure EXTENDS uniformly}\ }$$
$$(3)\quad\textbf{THE THREE STEP-3 MECHANISMS, REFUTED:}\qquad\begin{array}{l|l}\textbf{the proposed cutoff mechanism}&\textbf{the derived row}\\\hline\text{capacity overload at}\ k{=}3&\textbf{REFUTED}\ [\mathrm{IT.19}(6)]:\ \text{the rung-4}\ D^-\ \text{saturation is uniform from}\ k{=}1,\ \text{retained}\neg\text{accessible}\ [\mathrm{CT4.1}\text{--}\mathrm{CT4.3};\ \mathrm{D4.2};\ \mathrm{IT.3}/\mathrm{IT.10}]\\\text{winding mismatch}&\textbf{REFUTED}\ [\mathrm{IT.19}(2)]:\ d=0\ \text{for every open connector, uniformly}\\\text{flicker attenuation}&\textbf{RELOCATED}:\ \text{the ensemble/amplitude read}=\mathrm{IT\text{-}O2},\ \neg\text{a connector property}\end{array}$$
$$(4)\quad\textbf{THE PREMISE CORRECTIONS (on the record, the house discipline):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``the connector goes repulsive / unformable at}\ k{=}3\text{''}&\textbf{CORRECTED}\ [\mathrm{IT.19};\ \mathrm{IT.20}(2)]:\ \text{the connector is}\ k\text{-identical (open,}\ d{=}0,\ {+}2,\ \varepsilon{=}+1\text{);}\ \neg\text{a missing definition}\\\text{``evaluate the sign of the}\ 2k\ \text{residue (binding vs stress)''}&\textbf{READ-RELATIVE}\ [\mathrm{IT.20}(1)]:\ \text{on the informational read it is}\ -2ku<0\ \text{uniformly (a mass excess,}\ \neg\text{a discriminator); the ensemble read is}\ \mathrm{IT\text{-}O2}\\\text{``capacity overload / winding mismatch / flicker attenuation''}&\textbf{REFUTED or RELOCATED}\ [\mathrm{IT.20}(3)]:\ \text{saturation uniform,}\ d{=}0,\ \text{flicker}=\mathrm{IT\text{-}O2}\end{array}$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(2);\qquad\textbf{refuted/relocated:}\ (3);\qquad\textbf{corrected:}\ (4);\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a currency mixing}\ [\mathrm{BM.83};\ \mathrm{BM.134}(5)]$$

**Req.** P5, D0.8 (Parts 1–2); Def-H.32(1),(2),(4), FT.44(4), FT.107(2),(3) (Part 3); IT.3, IT.10, IT.19(2),(3),(6) (this level); AT.63(2) (Level 5); Def-BM.3(1),(7), BM.21(1),(2),(4), BM.83, BM.134(5), BM.137(3), CT4.1, CT4.3, D4.2, Census FT.35(2) (Part 4); exact `Fraction` binding coefficients over a symbolic $u=\ln2/\mathfrak h$, integer sign censuses [math; machine: `connector_species.py` §C, 4/4].

**Pf.**
$$(1):\ 6(k{+}1)-(8k{+}6)=-2k\ \text{as an integer coefficient at}\ k{=}0..3;\ \text{the sign census}\ <0\ \forall k\ge1;\ \text{the monotonicity and the no-crossing row}\ [\text{machine C1}];\ \text{the deuteron/}\,k{=}3\ \text{same-sign witness}\ [\text{machine C1x}]$$
$$(2):\ \text{the connector tuple}\ (0,2,+1)\ \text{exhibited equal across}\ k{=}0..3\ [\text{machine C2}];\qquad(3):\ \text{the three rows re-cited from}\ \mathrm{IT.19}(2),(6)\ \text{and}\ \mathrm{IT.3}/\mathrm{IT.10}\ [\text{machine C3}]$$
$$(4),(5):\ \text{the correction table verified against each cited locus};\ \text{assembly}.\ \blacksquare$$

**Phys.** The sign question has a clean answer and it is not the one the directive hoped for. Count
edges and the connected composite is always heavier than its separated nucleons by exactly two-k units
of the informational mass — negative binding, monotonically growing, for the deuteron just as much as
for hydrogen-four. A read that calls the deuteron unbound is not the physical binding, and it has no
sign change to offer, so it cannot pick out a last bound isotope. The connector itself is the same
object at every step of the family: zero winding, two edges, positive parity, uniform dark saturation
at its junctions. It does not stiffen, does not mis-wind, does not overload at twelve attachments. So
the two structural routes the directive proposed for a cutoff both close — the connector is invariant
and the cardinality is monotone — and the only place a genuine bound-versus-unbound verdict can live
is the ensemble binding, the failure of the flux to add up, which for several nucleons is the amplitude
sum the level has not yet built.

---

### IT.21 — The adjudication: IT-O4 closed, IT-O5 sharpened to a single gate

**Thm.**
$$(1)\quad\textbf{IT-O4 CLOSED — the connector species is derived:}\qquad\boxed{\ \text{the nucleon--nucleon connector}=\ \text{the OPEN bidirectional}\ \Sigma_{12}\text{-species connector}\ (e,\bar e)\ }$$
$$d=0\ [\mathrm{Def\text{-}H.32}(4);\ \mathrm{BM.129}(3);\ \mathrm{BM.143}(3)],\quad\Delta E_{\mathrm{int}}=2\ \text{each}\ [\text{Census}\ \mathrm{FT.35}(2);\ \mathrm{BM.17}(1)],\quad E^{\mathrm{tree}}_{\mathrm{int}}=8k{+}6\ \text{constructed}\ [\mathrm{IT.19}(3)],$$
$$\text{charge telescoping (net}\ 0,\ Q{=}{+}1\ \text{preserved)}\ [\mathrm{IT.19}(4)],\quad\varepsilon=(-1)^0=+1,\quad\text{distinct supports}\ (N{=}3(k{+}1))\ [\mathrm{IT.19}(5)],\quad\text{uniform rung-4 saturation}\ [\mathrm{IT.19}(6)]$$
$$(2)\quad\textbf{IT-O5 SHARPENED,}\ \neg\textbf{closed — the cutoff is relocated to a single gate:}\qquad\text{the isotope cutoff is}\ \neg\text{in the connector}\ (\mathrm{IT\text{-}O4}\ \text{discharged,}\ k\text{-identical)}\ [\mathrm{IT.20}(2)];$$
$$\neg\text{in the cardinality/informational read}\ (\mathcal B_{\mathrm{info}}=-2ku<0\ \text{uniformly, calls the deuteron unbound)}\ [\mathrm{IT.20}(1)];$$
$$\boxed{\ \text{the ONLY read that can adjudicate bound-vs-unbound is the ENSEMBLE binding}\ [\mathrm{BM.21}(2)\text{--}(4);\ \mathrm{BM.137}(3)\ \text{species}]\ \text{for the multi-nucleon configuration}\ }$$
$$=\ \text{the Def-H.32 amplitude sum over the}\ N{=}3(k{+}1)\ \text{grouping sectors with}\ (-1)^{\aleph}\ \text{dressing}\ [\mathrm{Def\text{-}H.32}(2)]\ =\ \mathrm{IT\text{-}O2}:\qquad\boxed{\ \textbf{IT-O5 is now gated on IT-O2 ALONE}\ }$$
$$(3)\quad\textbf{THE ADJUDICATION (Step 4, honest — recorded}\ \neg\textbf{forced):}\qquad\text{the bound isotope sequence's termination at}\ k{=}2\ \textbf{remains a CONJECTURE};$$
$$\text{the obstruction is now ONE named construction}\ (\mathrm{IT\text{-}O2}\ \text{the multi-nucleon amplitude/ensemble binding),}\ \neg\text{two};\qquad\text{AT.44}/\mathrm{AT\text{-}O30}\ \text{engines reusable}\ [\mathrm{IT.15}(5);\ \mathrm{IT.18}(5)]$$
$$(4)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses}),\ \mathrm{FT.55}(1),\ \mathrm{CT3.22},\ \mathrm{BM.143}(1);\qquad(R10)\ \text{re-cited as registration data}\ [\mathrm{BM.143}(3)],\ \neg\text{reopened}$$
$$(5)\quad\textbf{the machine state:}\qquad\texttt{connector\_species.py}\to\textbf{17/17 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{7 checkers, 104 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{6 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(6)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, FT.55(1), CT3.22 (Parts 1–2); Def-H.32(2),(4), FT.44(4), FT.107(2),(3) (Part 3); IT.3, IT.10, IT.15(5), IT.18(5), IT.19, IT.20 (this level); AT.39(8), AT.44, AT.63(2), AT-O30 (Level 5); Def-BM.3(1),(7), BM.21(2),(4), BM.30(5), BM.83, BM.134(5), BM.137(3), BM.143(1),(3) (Part 4); the assembly rows [math; machine: `connector_species.py` §D, 3/3].

**Pf.**
$$(1):\ \text{the conjunction of}\ \mathrm{IT.19}(1)\text{--}(6)\ [\text{machine D1}];\qquad(2):\ \mathrm{IT.20}(1),(2),(3)\ \text{relocated to the ensemble read}\ [\mathrm{BM.21}(2)\text{--}(4);\ \mathrm{BM.137}(3);\ \mathrm{Def\text{-}H.32}(2)]\ [\text{machine D2}]$$
$$(3)\text{--}(6):\ \text{the adjudication, the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (4)\text{--}(6).\ \blacksquare$$

**Phys.** The tier closes one open row and sharpens another into a single question. IT-O4 is done: the
nucleon-nucleon connector is not an exotic new object but the frozen bidirectional channel of the
neutron cell, open and therefore zero-winding, two edges, charge-neutral by telescoping, positive in
statistics, linking distinct supports, saturating its junctions uniformly from the first composite
onward. With the connector in hand, the eight-k-plus-six tree count is no longer parametric. And the
cutoff question is now honest and narrow. The connector does not vary with k, so it cannot end the
family; the edge count grows monotonically negative on the informational read, flagging the deuteron
as readily as hydrogen-four, so it cannot end the family either. What is left is exactly one thing: the
ensemble binding of several nucleons, the failure of the curvature flux to add up, which lives in the
amplitude sum over the grouping sectors that IT-O2 names. The isotope cutoff is not disproved and not
proved — it is reduced to a single construction, and the record says so plainly rather than forcing a
verdict the inventory cannot yet support. Nothing measured entered; nothing was declared; no isotope
was identified.

---

## §Cal-IT — unchanged from Tier IT.6

**Empty at this tier.** The tier closes IT-O4 with derived rows and sharpens IT-O5 to a single gate;
no parameter is added. The parametric residues remain the open rows and the inherited owed
declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1), $\varepsilon_q$
(AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$, $\hat\mu'^2$,
$\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile, the lift and the vielbein (AT.60).

## §Open-IT additions from Tier IT.6

| row | content | locus |
|---|---|---|
| **IT-O4 — CLOSED** | the nucleon–nucleon connector species is **derived**: the open bidirectional Σ₁₂ connector, $d=0$ (R10 = registration data [BM.143(3)]), $+2$ E_int, charge-telescoping, $\varepsilon=+1$, distinct supports, uniform rung-4 saturation; $E_{\mathrm{int}}^{\mathrm{tree}}=8k{+}6$ discharged to a construction | IT.19; IT.21(1) |
| **IT-O5 — SHARPENED** | the isotope cutoff is **relocated to a single gate**: ¬the connector (IT-O4 discharged, $k$-identical), ¬the cardinality read ($\mathcal B_{\mathrm{info}}=-2ku<0$ uniformly). The bound-vs-unbound verdict needs the **ensemble binding** [BM.21(2)–(4); BM.137(3) species] for the multi-nucleon configuration = the Def-H.32 amplitude sum over the grouping sectors with $(-1)^{\aleph}$ dressing = **IT-O2**. **IT-O5 is gated on IT-O2 alone** | IT.20; IT.21(2) |
| IT-O2, note | now the **sole** gate on IT-O5: the Def-H.32 amplitude/ensemble binding for the $N=3(k{+}1)$ multi-nucleon configuration (the $(-1)^{\aleph}$-dressed sum over the $g(N)$ grouping sectors); AT.44/AT-O30 engines reusable; would also yield the route-(iii) $N=9$ ratios and the resonance classification [Def-BM.17] | IT.21(2); IT.18(5) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5)]: (IT-O1) the transit-leg
amplitude, (IT-O3) the handshake-indicator operational theory, the owed mass-read route choice
[IT.14(3)], and the Level-5 ledger [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.7: the "exotic states" read-tier adjudication — the $N{=}4,5$ support classes, the exotic sign triples, and the quarantined census mapping

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.7 — the Architect's directive to adjudicate
the "exotic states" question at the read tier: the derived combinatorial support classes at $N{=}4$
and $N{=}5$, the proton sector's exotic sign triples, the Measurement-Theorem closure (the
inter-system read sees only the telescoped boundary charge), and the LHC census mapping confined to a
quarantined [EXT] audit clause.
**Tags.** IT.22–IT.24. **Pattern.** the adjudication tiers (IT.4/IT.5/IT.6's shape), premise audit
logged in-tier; the external-data handling follows the era-1 [EXT] audit pattern (Census §"External-data
quarantine"; FT.114).
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays
empty; no clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.4/IT.5/IT.6 is modified
[AT.63(2)]. **No species is identified** [Def-BM.3(1),(7)].
**Machine.** `era2/level6_isotopic/checks/exotic_states.py` → **17/17 exact** (the IT.2/IT.3 grammar
engine reused; fresh sign-triple enumeration; the [EXT]-confinement scan of this document, the
FT.114 §H pattern); `run_all_level6.py` → **8 checkers, 121 exact markers, 0 failures**;
`check_level6_format.py` → the gate over all seven Part 6 documents. Exact arithmetic: integer
set-partition enumeration, exact binomials, `Fraction` shares, exhaustive ternary-sign censuses.
**No floating point in any assertion. THE EXTERNAL CENSUS IS QUARANTINED [P5; P1]: the LHC's
"tetraquark"/"pentaquark"/"intrinsic charm" census enters ONLY in IT.24(2)'s [EXT] audit clause —
tested, never trusted, it enters no Req, no Pf, and no coefficient of IT.22–IT.23 (machine-scanned,
IT.24(2)); no mass, width, lifetime or measured value is cited anywhere; the structural origin (the
contraction grammar) is reported SEPARATELY from the [EXT] coincidence [FT.114(3) pattern]. The
derived objects are the $N{=}4,5$ SUPPORT CLASSES and the exotic sign triples — $\neg$particles.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13c): *"Adjudicate the 'Exotic States' Read-Tier
Question via the LHC Census Mapping … map the LHC experimental census to the corpus's $N{=}4$ and
$N{=}5$ support decompositions, and the proton's exotic sign triples. Close this read-tier question as
a derived structural feature, not an anomaly … Please use the LHC data as ext class as we maintain in
era 1 too."* Executed with the derived content (IT.22–IT.23) separated from the quarantined [EXT]
mapping (IT.24(2)); one scoping refinement logged at IT.24(3).

---

### IT.22 — The support-class census: $N{=}4$ all-$\delta$, $N{=}5$ forced-mixed, and the exotic sign triples

**Thm.**
$$(1)\quad\textbf{THE}\ N{=}4\ \textbf{SUPPORT CLASS IS ENTIRELY}\ \delta\textbf{-PAIRED:}\qquad g(4)=3,\quad g_\varepsilon(4)=0,\quad g_\delta(4)=3\qquad[\mathrm{IT.6}(5);\ \mathrm{BM.31}(2);\ \mathrm{Def\text{-}BM.9}(3)]:$$
$$\text{the three groupings are the three perfect matchings, all of block type}\ (a,b)=(2,0);\qquad2a{+}3b{=}4\ \text{has the unique nonneg solution}\ (2,0);$$
$$\boxed{\ \text{the}\ N{=}4\ \text{support admits}\ \neg\text{a pure-}\varepsilon\ (\text{baryon-type})\ \text{grouping — it is forced entirely mesonic-type}\ }\qquad\text{off-family:}\ 4\not\equiv0\ (\mathrm{mod}\ 3)\ [\mathrm{IT.6}(2)]$$
$$(2)\quad\textbf{THE}\ N{=}5\ \textbf{SUPPORT CLASS IS FORCED-MIXED:}\qquad2a{+}3b{=}5\ \text{has the UNIQUE nonneg solution}\ (a,b)=(1,1)\implies g(5)=10,\ \ g_\varepsilon(5)=0\ \ \textbf{forced}\ [\mathrm{IT.9}(4)]:$$
$$g(5)=\tfrac{5!}{1!\,1!\,2^1\,6^1}=10,\ \ \text{ALL of block type}\ (1,1)=\ \text{one}\ \delta\text{-pair}+\ \text{one}\ \varepsilon\text{-triple};\qquad\boxed{\ \neg\text{a pure-baryon (pure-}\varepsilon\text{) sector exists at}\ N{=}5\ }$$
$$(3)\quad\textbf{THE EXOTIC SIGN TRIPLES (the proton sector's interior):}\qquad\#\{(q_1,q_2,q_3)\in\{-1,0,+1\}^3:\ \textstyle\sum q_i=+1\}=6\ [\mathrm{BM.28}(2)\ \text{frozen census}\ (1,3,6,7,6,3,1)]:$$
$$\text{the six split as}\ \underbrace{3}_{(+1,0,0)\text{-type}}+\underbrace{3}_{(+1,+1,-1)\text{-type}};\qquad\boxed{\ \text{the boundary charge}\ Q{=}{+}1\ \text{is realized by interior sign compositions beyond the naive single-}{+}1,\ \text{all telescoping to the same}\ q_{\mathrm{EM}}\ }$$
$$(4)\quad\textbf{THE INTERIOR MULTIPLICITY IS MAJORITY-EXOTIC (at}\ N{=}9\textbf{):}\qquad\text{the nucleonic sub-census}\ (Q_j\in\{0,+1\})\ \text{carries}\ \tfrac{18000}{43758}=\tfrac{1000}{2431}\ \text{of the}\ Q{=}{+}1\ \text{sector and}\ \tfrac{13500}{31824}=\tfrac{375}{884}\ \text{of}\ Q{=}{+}2\ [\mathrm{IT.12}(3)]:$$
$$\text{the exotic complements are}\ 25758\ \text{and}\ 18324;\qquad\boxed{\ \text{sector}\supsetneq\text{species: the non-nucleonic compositions are the MAJORITY}\ (\tfrac{1000}{2431}<\tfrac12,\ \tfrac{375}{884}<\tfrac12)\ }$$
$$(5)\quad\textbf{THE STATISTICS:}\qquad\text{pure-}\varepsilon\ \text{groupings}\to\Theta_{\mathrm{int}}\in4\mathbb Z\ \text{(baryon-type)};\ \ \text{EVERY}\ \delta\text{-containing grouping}\to\Theta_{\mathrm{int}}\in2\mathbb Z\ \text{only}\ [\mathrm{IT.6}(6);\ \mathrm{BM.31}(4)]:$$
$$\text{at}\ N{=}4\ (\text{all-}\delta)\ \text{and}\ N{=}5\ (\text{all-mixed})\ \text{there is}\ \neg\text{a}\ 4\mathbb Z\ \text{baryon-type sector};\qquad4\mathbb Z\subsetneq2\mathbb Z\ \text{(the partial separator)}$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5)\ \text{(the support classes and their multiplicities are theorems of the contraction grammar)};\qquad\neg\text{a declaration},\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)],\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT3.17a(2), D3.4, EM.9 (Parts 1–2); Def-H.32(1) (Part 3); IT.6(2),(5),(6), IT.9(4), IT.12(3) (this level); AT.63(2) (Level 5); Def-BM.3(2),(3),(7), Def-BM.9(3),(4), BM.28(2), BM.31(2),(4), BM.135 (Part 4); exhaustive set-partition enumeration, exact factorials and binomials, exhaustive ternary-sign census, exact `Fraction` reductions [math; machine: `exotic_states.py` §§A–C, 9/9].

**Pf.**
$$(1):\ \text{the partitions of a 4-set into blocks of size}\ \in\{2,3\}\ \text{enumerated}=\{(2,0)\times3\};\ 2a{+}3b{=}4\ \text{solution census};\ g_\varepsilon(4){=}0\ (4\not\equiv0\ \mathrm{mod}\ 3)\ [\text{machine A1, A1x}]$$
$$(2):\ 2a{+}3b{=}5\ \text{solution census}=\{(1,1)\};\ 5!/(1!\,1!\,2\cdot6){=}10;\ \text{all blocks}\ (1,1)\ [\text{machine B1, B1x}]$$
$$(3):\ \text{the exhaustive}\ 3^3{=}27\ \text{ternary census filtered to}\ \sum q_i{=}{+}1\ {=}6,\ \text{split}\ 3{+}3\ \text{by type}\ [\text{machine C1}];\qquad(4):\ \text{the}\ \mathrm{IT.12}(3)\ \text{shares re-derived, both}\ <\tfrac12\ [\text{machine C2, C2x}]$$
$$(5):\ \text{the}\ 4\mathbb Z/2\mathbb Z\ \text{rows re-cited from}\ \mathrm{IT.6}(6);\ \text{the absence of a pure-}\varepsilon\ \text{sector at}\ N{=}4,5\ \text{from}\ (1),(2).\ \blacksquare$$

**Phys.** Two attachment counts settle the whole question before any experiment is mentioned. At four
attachments the contraction grammar has exactly three groupings and every one of them is a pair of
mesonic δ-contractions — there is no way to seal four attachments into a pure baryonic triple, so the
four-support is forced entirely mesonic-type. At five attachments the arithmetic is even starker: the
only way to write five as a sum of twos and threes is one of each, so all ten groupings are the same
hybrid, and again no pure-baryon sector exists. These are not anomalies or rare configurations; they
are the only configurations the partition rule allows. And the interior of a fixed boundary charge is
just as crowded — the plus-one sector at three attachments is six ordered sign triples, half of them
of the exotic plus-one-plus-one-minus-one kind that still telescopes to plus-one, and at nine
attachments the compositions a valence picture would name carry barely two fifths of their own sector.
The support classes and their multiplicities are derived; what they are called is not this tier's business.

---

### IT.23 — The read-tier closure: the inter-system read sees only the telescoped charge

**Thm.**
$$(1)\quad\textbf{THE READ CLASSES (the Measurement Theorem):}\qquad\text{inter-system registration is rung-2 mediated and reads ONLY the telescoped boundary charge}\ q_{\mathrm{EM}}\ [\mathrm{IT.1}(1),(3);\ \mathrm{FT.20};\ \mathrm{CT0.13}]:$$
$$q(c,\sigma)=\tfrac12(\sigma_{e_1}-\sigma_{e_k})\ \ \text{is the end-register read};\qquad\boxed{\ \text{the interior grouping}\ (\delta/\varepsilon\ \text{partition, sign composition})\ \text{is}\ \neg\text{registered inter-system}\ }$$
$$(2)\quad\textbf{THE HORIZON (preserved but inaccessible):}\qquad\text{the non-transit boundary leaks no rung}\ge2\ \text{summand; the interior is void-closed; the accessible content is EXACTLY the triple}\ (Q,\Theta_{\mathrm{int}},S){+}|R|{+}n\ [\mathrm{IT.2};\ \mathrm{AT.29};\ \mathrm{AT.32}(1);\ \mathrm{D0.7};\ \mathrm{BM.143}(1)]:$$
$$\text{machine witness: every interior composition of a fixed-}Q\ \text{sector telescopes to the SAME}\ q_{\mathrm{EM}}\ (6/6\ \text{at}\ N{=}3;\ \text{the}\ Q{=}{+}1\ \text{sector at}\ N{=}9\ \text{is one boundary read})$$
$$(3)\quad\textbf{THE CLOSURE (the ``exotic states'' are a read-tier feature,}\ \neg\textbf{new structure):}\qquad\boxed{\ \text{the ``exotic'' groupings are the ensemble's INTERIOR multiplicities}\ [\mathrm{IT.22}(1)\text{--}(4)],\ \text{majority at}\ N{=}4,5,9,\ \text{which the inter-system read resolves only to}\ q_{\mathrm{EM}}\ }$$
$$\therefore\ \text{they are}\ \neg\text{new particles and}\ \neg\text{an anomaly:}\ \text{they are the required combinatorial supports of the topology-blind sum}\ [\mathrm{Def\text{-}H.32}(1);\ \mathrm{Def\text{-}BM.9}(3)],\ \text{invisible at the boundary by the horizon}\ (2)$$
$$(4)\quad\textbf{WHAT THE READ TIER CANNOT DO:}\qquad\neg\text{a formed transit-leg amplitude exists}\ [\mathrm{IT\text{-}O1};\ \mathrm{BM.122}(6)];\ \ \text{the interior grouping is}\ \neg\text{observable inter-system}\ [\mathrm{IT.2};\ \mathrm{CT3.22}:\ \text{colour}\ \neg\text{observable}];$$
$$\text{so a boundary sector's interior multiplicity is a DERIVED count}\ [\mathrm{IT.22}]\ \text{that no inter-system measurement resolves — the ``exotic'' label is the identification layer's, applied where the read is blind}$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(4)\ \text{(assembly of the Measurement Theorem and the support census)};\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT0.13, CT3.22, D0.7, EM.9, FT.20 (Parts 1–2); Def-H.32(1) (Part 3); IT.1(1),(3), IT.2, IT.22(1),(2),(3),(4), IT-O1 (this level); AT.29, AT.32(1), AT.63(2) (Level 5); Def-BM.9(3), BM.122(6), BM.135, BM.143(1) (Part 4); exhaustive ternary-sign telescoping census [math; machine: `exotic_states.py` §D, 5/5].

**Pf.**
$$(1):\ \text{the read-class rows re-cited from}\ \mathrm{IT.1}(1),(3);\ \text{the end-register read}\ q=\tfrac12(\sigma_{e_1}-\sigma_{e_k})\ [\mathrm{EM.9};\ \mathrm{FT.40}]$$
$$(2):\ \text{the telescoping exhibited: all}\ 6\ \text{ordered}\ Q{=}{+}1\ \text{triples at}\ N{=}3\ \text{read to the same}\ q_{\mathrm{EM}}{=}{+}1\ [\text{machine D1, D2}];\ \text{the horizon rows re-cited}\ [\mathrm{IT.2};\ \mathrm{AT.29}]$$
$$(3):\ \text{the conjunction of}\ \mathrm{IT.22}(1)\text{--}(4)\ \text{(the interior multiplicity)}\ \text{and}\ (1)\text{--}(2)\ \text{(the read sees only}\ q_{\mathrm{EM}})$$
$$(4):\ \mathrm{IT\text{-}O1}\ \text{and}\ \mathrm{CT3.22}\ \text{re-cited};\qquad(5):\ \text{assembly}.\ \blacksquare$$

**Phys.** The measurement theorem does the closing work, and it is a statement about reads, not about
particles. Anything one sealed system registers about another arrives through the rung-two boundary
read, and that read is the telescoped end-register charge — a single number per sector. The interior
grouping that IT.22 counted, the threes and tens and the crowded sign compositions, is preserved
behind the boundary and provably cannot leak out; the horizon says the accessible content is the
boundary triple and nothing finer. So when the interior multiplicity is majority-exotic, as it is at
four, five and nine attachments, no inter-system measurement can resolve it: the exotic groupings are
real, derived, and counted, and they are invisible at the boundary by theorem. That is the whole
adjudication — the exotic states are not a new kind of object, they are the ensemble's own interior
granularity seen from the only angle a measurement allows, and the angle is blind to them.

---

### IT.24 — The adjudication and the quarantined [EXT] census mapping

**Thm.**
$$(1)\quad\textbf{THE READ-TIER ADJUDICATION (the question closes as a derived structural feature):}\qquad\boxed{\ \textbf{the ``exotic states'' question CLOSES at the read tier:}\ \text{the}\ N{=}4,5\ \text{support classes and the exotic sign triples are DERIVED combinatorial supports}\ [\mathrm{IT.22}],\ \text{majority-interior and boundary-invisible}\ [\mathrm{IT.23}]\ }$$
$$\text{they are}\ \neg\text{an anomaly},\ \neg\text{new particles},\ \neg\text{a smooth-manifold addition:}\ \text{they are the required supports of the topology-blind sum}\ [\mathrm{Def\text{-}H.32}(1);\ \mathrm{Def\text{-}BM.9}(3)],\ \text{derived WITHOUT importing quarks or a gauge theory}$$
$$(2)\quad\textbf{[EXT] AUDIT CLAUSE (quarantined; the FT.114 / Census §External-data-quarantine pattern — tested, never trusted; enters no derivation):}$$
$$\text{the identification layer}\ [\mathrm{Def\text{-}BM.3}(7)]\ \text{maps, as an}\ \textbf{[EXT]}\ \textbf{audit target only:}\quad\text{the LHC census of states named ``tetraquark''}\ \leftrightarrow\ \text{the}\ N{=}4\ \text{support class}\ [\mathrm{IT.22}(1)];$$
$$\text{``pentaquark''}\ \leftrightarrow\ \text{the}\ N{=}5\ \text{support class}\ [\mathrm{IT.22}(2)];\qquad\text{``intrinsic charm''}\ \leftrightarrow\ \text{the proton sector's exotic sign triples / majority-exotic interior}\ [\mathrm{IT.22}(3),(4)];$$
$$\textbf{discipline:}\ \text{this mapping is a species-NAMING act, quarantined — it enters no Req, no Pf, and no coefficient of IT.22--IT.23 (machine-scanned below); the structural origin (the contraction grammar) is reported SEPARATELY from the [EXT] coincidence}\ [\mathrm{FT.114}(3)];$$
$$\boxed{\ \neg\text{a mass, width, lifetime or measured value is cited; }\ \neg\text{a claim that the derivation reproduces any observed spectrum; no identification of a support class with a particle species is made or implied in IT.22--IT.23}\ }\ [\mathrm{P5};\ \mathrm{P1}]$$
$$(3)\quad\textbf{THE SCOPING REFINEMENT (on the record):}\qquad\text{``the corpus predicted the exotic hadrons'' is QUALIFIED — the corpus DERIVES the}\ \textbf{combinatorial structure}\ \text{(the support classes, their multiplicities, their}\ \delta/\varepsilon\ \text{and sign-triple composition)};$$
$$\neg\text{the particles' masses, widths, or existence-as-resonances}\ (\text{that needs the ensemble/amplitude binding}=\mathrm{IT\text{-}O2},\ \neg\text{constructed});\qquad\text{the attachment count}\ N\ \text{is a ledger datum},\ \neg\text{a quark count — the}\ N\leftrightarrow\text{quark-number map is itself}\ \textbf{[EXT]}\ \text{identification content}$$
$$(4)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value in any derived clause}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses}),\ \mathrm{CT3.22}\ (\text{colour}\ \neg\text{observable}),\ \mathrm{FT.55}(1),\ \mathrm{BM.143}(1);\qquad\textbf{the [EXT] tokens are confined to clause (2)}\ [\text{machine scan}]$$
$$(5)\quad\textbf{the machine state:}\qquad\texttt{exotic\_states.py}\to\textbf{17/17 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{8 checkers, 121 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{7 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(6)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no species is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, CT3.22, FT.55(1) (Parts 1–2); Def-H.32(1) (Part 3); IT.1, IT.2, IT.6, IT.9, IT.12, IT.22, IT.23, IT-O2 (this level); AT.39(8), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.9(3), BM.30(5), BM.83, BM.122(6), BM.134(5), BM.143(1), Census FT.114 (the [EXT] audit pattern) (Part 4); the [EXT]-confinement scan of this document [math; machine: `exotic_states.py` §E, 4/4].

**Pf.**
$$(1):\ \text{the conjunction of}\ \mathrm{IT.22}\ \text{and}\ \mathrm{IT.23}\ [\text{machine D3, E1}]$$
$$(2):\ \text{the [EXT] tokens}\ \{\text{tetraquark},\ \text{pentaquark},\ \text{intrinsic charm},\ \text{LHC}\}\ \text{scanned in this document and confirmed to occur ONLY within clause (2)'s line span; the derived clauses IT.22--IT.23 and every Req/Pf coefficient are token-free}\ [\text{machine E2, E3};\ \mathrm{FT.114}\ \S\mathrm H\ \text{pattern}]$$
$$(3):\ \text{the scoping rows re-cited: the combinatorial structure from}\ \mathrm{IT.22};\ \text{the spectrum/resonance side from}\ \mathrm{IT\text{-}O2}\ [\mathrm{IT.21}(2);\ \mathrm{BM.21}(2)\text{--}(4);\ \mathrm{BM.137}(3)]$$
$$(4)\text{--}(6):\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (4)\text{--}(6).\ \blacksquare$$

**Phys.** The adjudication separates two things the directive's framing held together. What is derived
is combinatorics: four attachments seal only as mesonic pairs, five only as one pair plus one triple,
and a fixed boundary charge hides a majority-exotic interior — all of it forced by the partition rule,
all of it invisible to any read that crosses between systems, none of it needing a quark or a gauge
field. What is not derived is the naming: attaching the identification layer's labels to those support
classes is an external audit act, and it sits in one quarantined clause, machine-scanned to keep it
there, carrying no mass and no width and no claim that the grammar reproduced a spectrum. The corpus
predicted the shapes and their counts, not the particles, and the read tier is exactly where that
distinction lives — because the read tier is blind to the interior where the shapes are. The question
closes as a structural feature; the names stay quoted, the data stays quarantined, and no species is
identified.

---

## §Cal-IT — unchanged from Tier IT.7

**Empty at this tier.** No parameter is added; the external census is quarantined [EXT] audit content,
never a calibration slot. The parametric residues remain the open rows and the inherited owed
declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1), $\varepsilon_q$
(AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$, $\hat\mu'^2$,
$\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile, the lift and the vielbein (AT.60).

## §Open-IT additions from Tier IT.7

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.7 opens **no new row**: the "exotic states" question is CLOSED at the read tier as a derived structural feature (IT.22–IT.24). The only residue it touches is the standing one — the spectrum/mass side of any support class (bound-vs-resonance, masses, widths) waits on **IT-O2** (the ensemble/amplitude binding), unchanged and re-cited | IT.24(1),(3); IT.21(2) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2)]: (IT-O1) the
transit-leg amplitude, (IT-O2) the amplitude side (the sole gate on IT-O5), (IT-O3) the
handshake-indicator operational theory, (IT-O5) the isotope cutoff, the owed mass-read route choice
[IT.14(3)], and the Level-5 ledger [AT.63(3),(5)]. **IT-O4 stays CLOSED** [IT.21(1)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.8: the $N{\ge}4$ multi-seal configuration calculus — the amplitude side (IT-O2 advanced, IT-O5 open)

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.8 — the Architect's directive to construct
the multi-seal amplitude calculus: the sector decomposition and colour-statistics map, the composed-support
cells, the channel resolvent and its rational attenuation, the dressing register, the $N{=}3$ amplitude
census, and the adjudication of the $N{=}9$ binding sign (the IT-O5 gate).
**Tags.** IT.25–IT.27. **Pattern.** the construction/adjudication tiers (IT.5/IT.6/IT.7's shape),
premise audit logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays
empty; no clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.4–IT.7 is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/multi_seal_amplitude.py` → **20/20 exact** (the IT.2 grammar
engine reused; the AT.52 resolvent closed forms and the AT.54 excess-mean identity re-implemented; the
FT.106(3) census consumed row-wise); `run_all_level6.py` → **9 checkers, 141 exact markers, 0
failures**; `check_level6_format.py` → the gate over all eight Part 6 documents. Exact arithmetic:
integer set-partition enumeration, exact binomials, `Fraction` residues and excess means.
**No floating point in any assertion. No measured value enters any clause [P5] — no mass, width or
binding energy in MeV; the physical isotope data stays a quarantined [EXT] target, cited nowhere. No
species identification [Def-BM.3(1),(7)] — "triton", "exotic", "tetraquark", "pentaquark" stay quoted;
the derived objects are the $(a,b)$ grouping sectors, the composed support cells, and the amplitude
layer's own $(q,S)$ sectors.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13d): *"Construct the $N\ge4$ Multi-Seal Configuration
Calculus (the amplitude side, IT-O2) … evaluate the flicker ensemble amplitude over the $g(N)$ grouping
sectors … Determine if the amplitude-weighted ensemble binding is negative (bound) or positive
(unbound/resonance) at $N{=}9$ … Close IT-O2 and IT-O5 (or name the exact remaining obstruction)."*
Executed with the finding that the framing conflates two independent registers (the colour grouping and
the amplitude); four premise corrections logged at IT.27(3), the closable registers built, and the
obstruction named exactly.

---

### IT.25 — The multi-seal sector calculus: the decomposition, the composed cells, and the informational additivity

**Thm.**
$$(1)\quad\textbf{THE SECTOR DECOMPOSITION + COLOUR-STATISTICS MAP (Step 1):}\qquad\begin{array}{c|cc|cc}N&g(N)&(a,b)\ \text{blocks}&4\mathbb Z\ (\text{pure-}\varepsilon)&2\mathbb Z\ (\delta\text{-containing})\\\hline 5&10&(1,1){:}10&\mathbf0&10\\6&25&(3,0){:}15,\ (0,2){:}10&10&15\end{array}$$
$$\text{pure-}\varepsilon\ (a{=}0)\to\Theta_{\mathrm{int}}\in4\mathbb Z\ \text{(baryon-type)};\ \ \delta\text{-containing}\ (a{\ge}1)\to2\mathbb Z\ \ [\mathrm{IT.6}(6);\ \mathrm{BM.31}(2),(4);\ \text{Census}\ \mathrm{FT.49}(3)];\qquad\boxed{\ \text{at}\ N{=}6:\ 10\ \text{sectors in}\ 4\mathbb Z,\ 15\ \text{in}\ 2\mathbb Z\ \text{(the directive's example, confirmed exactly)}\ }$$
$$(2)\quad\textbf{THE COMPOSED SUPPORT CELLS (from the gluing law):}\qquad E_{\mathrm{int}}=E^{(1)}_{\mathrm{int}}+E^{(2)}_{\mathrm{int}}-|E_{\mathrm{dir}}(G)|\ \ [\text{Census}\ \mathrm{FT.50}(4)]:$$
$$\textbf{the}\ N{=}5\ \textbf{bowtie}\ (\text{two bidirectional triangles sharing one vertex},\ |E_{\mathrm{dir}}(G)|{=}0):\ E_{\mathrm{int}}=6{+}6{-}0=12,\ 5\ \text{slots}\Rightarrow g(5)=10;$$
$$\textbf{the}\ N{=}4\ \textbf{double-triangle}\ (\text{two faces glued along a bidirectional channel},\ |E_{\mathrm{dir}}(G)|{=}2):\ E_{\mathrm{int}}=6{+}6{-}2=10,\ 4\ \text{slots}\Rightarrow g(4)=3\ \ [\text{Census}\ \mathrm{FT.50}(5)\ \text{frozen, reproduced}]$$
$$(3)\quad\textbf{THE INFORMATIONAL ADDITIVITY (frozen):}\qquad E_{\mathrm{int}}(\Sigma)=2E_1+2E_2+2m\ \ \text{under bridged composition}\ [\text{Census}\ \mathrm{FT.50}(1)]:$$
$$\text{the 1p-}k\text{n tree:}\ E^{\mathrm{tree}}_{\mathrm{int}}=6(k{+}1)+2k=8k{+}6\ [\mathrm{IT.6}(3);\ \mathrm{IT.20}(1)];\qquad\boxed{\ \mathcal B_{\mathrm{info}}=\bigl(6(k{+}1)-(8k{+}6)\bigr)u=-2k\,u<0\ \ \forall k\ge1\ }$$
$$(4)\quad\textbf{THE INFORMATIONAL READ CANNOT ADJUDICATE:}\qquad\mathcal B_{\mathrm{info}}=-2k\,u\ \text{flags the DEUTERON}\ (k{=}1)\ \text{``unbound'' by}\ -2u\ \text{exactly as}\ k{=}3\ \text{by}\ -6u:\ \ \text{monotone,}\ \neg\text{crossing zero};$$
$$\text{a read that calls a constructed family member unbound discriminates nothing}\ \Rightarrow\ \textbf{the cutoff is}\ \neg\textbf{an informational/cardinality phenomenon}\ [\mathrm{IT.18}(1);\ \mathrm{IT.20}(1);\ \text{re-cited with}\ \mathrm{FT.50}(1)]$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(4);\qquad\textbf{re-produced frozen rows:}\ g(5),g(6),\ \text{the}\ \mathrm{FT.50}(4),(5)\ \text{cells},\ \mathrm{FT.50}(1)\ \text{additivity};\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT3.17a(2), D0.8 (Parts 1–2); Def-H.32(1), FT.34(3), FT.44(4) (Part 3); IT.6(2),(3),(6), IT.7(1), IT.9(4), IT.18(1), IT.20(1) (this level); AT.63(2) (Level 5); Def-BM.9(3),(4), BM.17(1), BM.31(2),(4), Census FT.35(2), FT.49(3), FT.50(1),(4),(5) (Part 4); exact integer set-partition enumeration, the gluing-law and additivity arithmetic, `Fraction` binding coefficients over a symbolic $u=\ln2/\mathfrak h$ [math; machine: `multi_seal_amplitude.py` §§A–B, 6/6].

**Pf.**
$$(1):\ \text{the}\ (a,b)\ \text{block census by the closed form; the}\ 4\mathbb Z/2\mathbb Z\ \text{map by}\ a{=}0\ \text{vs}\ a{\ge}1;\ \text{the}\ N{=}6\ \text{split}\ 10{+}15{=}25\ \text{and the}\ \tfrac35\ \delta\ \text{share}\ [\text{machine A1, A2, A2x}]$$
$$(2):\ 6{+}6{-}0{=}12\ \text{and}\ 6{+}6{-}2{=}10\ \text{from the gluing law; the slot counts}\ 5,4\ \text{give}\ g(5){=}10,g(4){=}3\ [\text{machine A3}]$$
$$(3):\ 6(k{+}1){+}2k{=}8k{+}6;\ \ 6(k{+}1)-(8k{+}6)=-2k\ \text{as an integer coefficient}\ [\text{machine B1}];\qquad(4):\ \text{the sign census}\ <0\ \forall k\ge1\ \text{and the}\ k{=}1/k{=}3\ \text{same-sign witness}\ [\text{machine B2}].\ \blacksquare$$

**Phys.** Two registers were asked to meet and the first thing the tier establishes is that they were
never apart in the way the directive assumed. The grouping census is exact and cheap: five attachments
give ten groupings, all one pair plus one triple, all mesonic-admissible in their statistics; six give
twenty-five, split ten baryonic to fifteen mesonic, the frozen three-fifths. The composed cells fall
straight out of the gluing law — the bowtie at twelve internal edges, the double-triangle at ten — and
the informational mass of a bridged composite is the sum of its parts plus the connector, exactly, which
is why the informational binding is minus two-k for every member of the family. That last fact is the
tier's first verdict and it is negative in the useful sense: a read that calls the deuteron unbound by
the same rule it would call hydrogen-four unbound cannot be the read that decides where the family ends.

---

### IT.26 — The amplitude layer, correctly located: the register separation, the channel resolvent, and the $N{=}3$ census

**Thm.**
$$(1)\quad\textbf{THE REGISTER SEPARATION (the load-bearing correction):}\qquad\text{the colour grouping}\ g(N)\ \text{and the Def-H.32 amplitude are INDEPENDENT registers}:$$
$$\text{the seal is a COLOUR partition, independent of the edge signs, and GATES the read}\ (\Pi_{\mathcal C},\ \mathcal C\in\{0,1\})\ \text{without constraining its value}\ [\mathrm{AT.41}(3);\ \mathrm{Def\text{-}BM.9}(2),(5)];$$
$$\text{the amplitude}\ Z^{\bullet}_B(q,S)=\!\!\sum_{\Gamma\in\mathcal G_B}\sum_R\!\!\mathcal W^{\bullet}_\Gamma(R)\#\{\text{instances}\}\ \ \text{is SECTORED BY}\ (q,S)\ \text{over the budget-}B\ \text{configuration space}\ [\mathrm{Def\text{-}H.32}(5)];$$
$$\boxed{\ \text{``the amplitude over the}\ g(N)\ \text{grouping sectors'' is ILL-POSED: every grouping is sealed}\ (\mathcal C{=}1),\ \text{so they gate UNIFORMLY — a multiplicity,}\ \neg\text{distinct amplitude weights}\ }$$
$$(2)\quad\textbf{THE DRESSING IS}\ q\textbf{-LOCKED,}\ \neg\textbf{GROUPING-LOCKED:}\qquad(-1)^{\aleph}=\prod_{e:\ \mathrm{cov}(e)\ \mathrm{odd}}\sigma_e\ \ \text{on EVERY configuration}\ [\mathrm{AT.53}(5)]:$$
$$\text{the arguments are the COVER and the SIGNS; single open chains give}\ (-1)^{\aleph}=(-1)^{|q|};\qquad\text{the colour grouping}\ (a,b)\ \text{is}\ \neg\text{an argument}\ [\mathrm{AT.41}(3)];$$
$$\text{the MAGNITUDE fluctuates as exact rationals:}\ \langle\aleph\rangle^{(n)}=\frac{\sum_j\binom nj p^ju^{n-j}g(2j)}{1-u^n},\ g(2)=|q|,\ g(2j)=\tfrac{2j-1}2\ [\mathrm{AT.54}(1)]:\quad\langle\aleph\rangle^{(2)}=\tfrac76,\ \langle\aleph\rangle^{(3)}=\tfrac{10}7\ \ \text{at}\ \varepsilon_q{=}\tfrac18\ (\text{excess}\ \tfrac16,\ \tfrac37)$$
$$(3)\quad\textbf{THE CHANNEL RESOLVENT IS}\ k\textbf{-INDEXED (}\neg N\textbf{-indexed):}\qquad R_k(z)=c_k+\sum_{d\in\{k,k-2,\dots\}>0}\frac{a_{k,d}}{1-d^2z},\quad a_{k,d}=2^{1-k}\binom{k}{(k+d)/2},\quad c_k=2^{-k}\binom{k}{k/2}\ [k\ \text{even}]\ [\mathrm{AT.44}(1);\ \mathrm{AT.52}(1)]:$$
$$\text{the sum rule}\ c_k+\sum_d a_{k,d}=R_k(0)=1\ \ \text{holds exactly for}\ k=1..8;\qquad\textbf{the contact diversion}\ c_k=\bigl(\tfrac12,\tfrac38,\tfrac5{16},\tfrac{35}{128},\tfrac{63}{256}\bigr)\ \text{at}\ k=(2,4,6,8,10),\ c_k=0\ \text{at odd}\ k\ [\mathrm{AT.52}(2)];$$
$$\boxed{\ k\ \textbf{is the connector floor's PAIR COUNT}\ [\mathrm{AT.54}\ \mathrm{Rmk};\ \mathrm{BM.137}(1)],\ \neg\text{the attachment count}\ N\ }\qquad\text{so}\ R_k\ \text{applies to the connector CHANNELS,}\ \neg\text{to}\ N{=}5,6\ \text{as such}$$
$$(4)\quad\textbf{THE}\ N{=}3\ \textbf{AMPLITUDE CENSUS (re-derived):}\qquad\frac{Z^{\mathrm{amp}}(0,0)}{Z^{\mathrm{amp}}(\pm1,0)}=\frac{5336}{1196}=\frac{58}{13},\qquad\frac{Z^{\mathrm{amp}}(0,1)}{Z^{\mathrm{amp}}(\pm1,1)}=\frac{4796}{802}=\frac{2398}{401}\ \ [\mathrm{FT.106}(3);\ \mathrm{BM.28}(4)(\mathrm{iii})]:$$
$$\textbf{the amplitude death of}\ k\ge2:\quad Z^{\mathrm{amp}}(q,2)=Z^{\mathrm{amp}}(q,3)=0\ \ \text{in total}\ [\mathrm{FT.106}(3)(\mathrm c);\ \mathrm{FT.69}(3)(\mathrm{iv}),(\mathrm v)];\qquad\text{only}\ S{=}0,1\ \text{amplitude-live};$$
$$\boxed{\ \text{the amplitude layer is SPARSE and}\ (q,S)\text{-sectored,}\ \neg\text{a sum over all groupings}\ }\qquad\text{the frozen census is at}\ B{=}4\ [\mathrm{FT.106}(3)]$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(4);\qquad\textbf{re-produced frozen rows:}\ \mathrm{AT.53}(5),\ \mathrm{AT.54}(1),\ \mathrm{AT.52}(1),(2),\ \mathrm{FT.106}(3);\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT2.8 (Parts 1–2); Def-H.32(2),(5), FT.67(2), FT.69(3), FT.106(3), FT.107(2), FT.108(5), BM.121(2) (Part 3); IT.6(3), IT.20(1) (this level); AT.41(3), AT.44(1), AT.52(1),(2), AT.53(5), AT.54(1), AT.63(2) (Level 5); Def-BM.9(2),(3),(5), BM.28(4), BM.137(1) (Part 4); exact `Fraction` partial-fraction residues and sum rules, the ℵ-excess polynomial identity over $\mathbb Q[u]$, exact rational ratio reduction [math; machine: `multi_seal_amplitude.py` §§C–E, 10/10].

**Pf.**
$$(1):\ \text{the register rows re-cited}\ [\mathrm{AT.41}(3);\ \mathrm{Def\text{-}BM.9}(2),(5);\ \mathrm{Def\text{-}H.32}(5)];\ \text{the dressing's argument set}\ \{\mathrm{cover},\sigma\}\ \text{is disjoint from}\ \{a,b\}\ [\text{machine D1}]$$
$$(2):\ \langle\aleph\rangle^{(2)},\langle\aleph\rangle^{(3)}\ \text{re-derived from}\ \mathrm{AT.54}(1)\text{'s identity at}\ u{=}p{=}\tfrac12:\ \tfrac76,\ \tfrac{10}7;\ \text{the excess}\ \tfrac16,\ \tfrac37;\ \text{the}\ |q|\text{-dependence witness}\ [\text{machine D2, D2x}]$$
$$(3):\ a_{k,d},c_k\ \text{by the closed forms; the sum rule}{=}1\ \text{for}\ k{=}1..8;\ c_k\ \text{at even}\ k,\ 0\ \text{at odd};\ \text{the}\ k{=}4\ \text{witness}\ \tfrac38{+}\tfrac18{+}\tfrac12{=}1\ \text{and the halved-contact refutation}\ \tfrac{13}{16}\ne1\ [\text{machine C1, C2, C1x}]$$
$$(4):\ 5336/1196{=}58/13\ (\gcd 92),\ 4796/802{=}2398/401\ (\gcd 2);\ \text{the}\ k{\ge}2\ \text{death rows re-cited};\ \text{the}\ (q,S)\ \text{sectoring exhibited}\ [\text{machine E1, E2, E3}].\ \blacksquare$$

**Phys.** The amplitude layer is a real object and the tier builds the parts of it that exist: a
resolvent whose residues are exact binomials and whose contact term diverts a rational fraction of the
return weight off the pole ladder at every even channel count; a dressing whose sign is locked to the
boundary charge and whose magnitude fluctuates as the exact rationals seven-sixths and ten-sevenths; and
a charge-and-winding-sectored census at three attachments whose ratios fifty-eight thirteenths and two
thousand three hundred ninety-eight four hundred firsts are a third species, sparse enough that every
winding above one dies outright. What the tier refuses to do is pretend these live on the grouping
register. The colour seal is independent of the signs, gates as a zero-one projector, and every grouping
passes it, so the fifteen hundred forty groupings at nine attachments are a multiplicity of an interior
register the amplitude never sees. The channel index is a pair count, not an attachment count. These are
not caveats; they are the reason the requested sum has no referent, and naming them precisely is what
turns an ill-posed instruction into a located obstruction.

---

### IT.27 — The adjudication: IT-O2 advanced, IT-O5 open, the obstruction named exactly

**Thm.**
$$(1)\quad\textbf{IT-O2 ADVANCED (what closes):}\qquad\text{the sector decomposition + colour-statistics map}\ [\mathrm{IT.25}(1)],\ \text{the composed-cell geometry}\ [\mathrm{IT.25}(2)],\ \text{the informational additivity}\ [\mathrm{IT.25}(3)],$$
$$\text{the channel resolvent + rational attenuation}\ [\mathrm{IT.26}(3)],\ \text{the dressing register + }\aleph\text{-excess means}\ [\mathrm{IT.26}(2)],\ \text{and the}\ N{=}3\ \text{amplitude census}\ [\mathrm{IT.26}(4)]\ \ \textbf{are all constructed, exact};$$
$$\text{the multi-seal configuration calculus is built FOR THESE REGISTERS;}\ \neg\text{for the composed-support amplitude}\ (2)$$
$$(2)\quad\textbf{IT-O5 STAYS OPEN — the exact remaining obstruction (three named constructions):}\qquad\begin{array}{l|l}\textbf{the missing construction}&\textbf{why it blocks}\\\hline(1)\ \text{the composed-support Def-H.32 AMPLITUDE space at}\ N{=}9&\text{the covers}/v_\Gamma\ \text{for the multi-junction support, beyond the frozen}\ B{=}4\ \text{census}\ [\mathrm{FT.106}(3)]\\(2)\ \text{the CONNECTOR's amplitude weight}\ v_\Gamma&\mathrm{IT.6}\ \text{gave}\ E_{\mathrm{int}}{+}2\ \text{and winding}\ d{=}0,\ \neg v_\Gamma\ [\mathrm{Def\text{-}H.32}(2)]\\(3)\ \text{the MULTI-JUNCTION ensemble binding FUNCTIONAL}&\mathrm{BM.21}\ \text{is 3-constituent},\ \mathrm{BM.137}\ \text{is two-chain};\ \text{the composed}\ m^2_B\ [\mathrm{Def\text{-}H.32}(6)]\ \neg\text{constructed}\end{array}$$
$$\boxed{\ \text{the}\ N{=}9\ \text{binding sign is NEITHER computable NOR boundable:}\ \neg\text{an}\ N{=}5/6\ \text{amplitude-binding precedent exists (the same three gaps)}\ }$$
$$(3)\quad\textbf{THE PREMISE CORRECTIONS (on the record):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``the amplitude sum over the}\ g(N)\ \text{grouping sectors''}&\textbf{ILL-POSED}\ [\mathrm{IT.26}(1)]:\ \text{the colour grouping is an independent gating register}\ [\mathrm{AT.41}(3);\ \mathrm{Def\text{-}BM.9}(2),(5)];\ \text{the amplitude is}\ (q,S)\text{-sectored}\ [\mathrm{Def\text{-}H.32}(5)]\\\text{``the}\ (-1)^{\aleph}\ \text{dressing sign for each}\ g(N)\ \text{sector''}&\textbf{CORRECTED}\ [\mathrm{IT.26}(2)]:\ \text{the dressing is}\ (\mathrm{cover},\sigma)\text{-valued and}\ q\text{-locked}\ [\mathrm{AT.53}(5)],\ \neg\text{grouping-locked}\\\text{``}\ R_k\ \text{for the}\ N{=}5,6\ \text{mixed grammars''}&\textbf{MIS-INDEXED}\ [\mathrm{IT.26}(3)]:\ k\ \text{is the connector pair count}\ [\mathrm{AT.54}\ \mathrm{Rmk};\ \mathrm{BM.137}(1)],\ \neg\text{the attachment count}\\\text{``}\ \mathcal B_{\mathrm{ens}}\ge0\ \text{unbound at}\ N{=}9/12\text{''}&\textbf{NO DERIVED SUPPORT}\ [\mathrm{IT.25}(4);\ \mathrm{IT.27}(4)]:\ \text{every constructed read is}\ \le0\end{array}$$
$$(4)\quad\textbf{NO CONSTRUCTED READ GIVES ``}\ge0\ \textbf{UNBOUND'':}\qquad\mathrm{BM.21}(4)\ \mathcal B<0\ (\text{3-constituent});\ \mathrm{BM.137}(3)\ \mathcal B^{(n)}_{\mathrm{ens}}\le0\ (\text{two-chain});\ \mathrm{FT.50}(1)/\mathrm{IT.18}(1)\ \mathcal B_{\mathrm{info}}=0\ (\text{disjoint});\ \mathrm{IT.20}(1)\ \mathcal B_{\mathrm{info}}=-2ku<0\ (\text{bridged}):$$
$$\boxed{\ \text{every constructed binding read is}\ \le0\ \Rightarrow\ \text{the hypothesized sign flip to}\ \ge0\ \text{has}\ \neg\text{support; the partial evidence points toward BOUND}\ }$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses}),\ \mathrm{CT3.22},\ \mathrm{FT.55}(1),\ \mathrm{BM.143}(1)$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{multi\_seal\_amplitude.py}\to\textbf{20/20 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{9 checkers, 141 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{8 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, CT3.22, FT.55(1) (Parts 1–2); Def-H.32(2),(5),(6), FT.106(3) (Part 3); IT.6, IT.18(1), IT.20(1), IT.21(2), IT.25, IT.26, IT-O2, IT-O5 (this level); AT.39(8), AT.53(5), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.9(2),(5), BM.21(4), BM.30(5), BM.83, BM.134(5), BM.137(3), BM.143(1), Census FT.50(1) (Part 4); the assembly rows [math; machine: `multi_seal_amplitude.py` §F, 4/4].

**Pf.**
$$(1):\ \text{the conjunction of}\ \mathrm{IT.25}(1)\text{--}(3)\ \text{and}\ \mathrm{IT.26}(2)\text{--}(4)\ [\text{machine F1}];\qquad(2):\ \text{the three missing constructions named against}\ \mathrm{FT.106}(3),\ \mathrm{Def\text{-}H.32}(2),(6),\ \mathrm{BM.21},\ \mathrm{BM.137}\ [\text{machine F2}]$$
$$(3):\ \text{the correction table verified against each cited locus};\qquad(4):\ \text{the sign census of the four constructed reads, all}\ \le0\ [\text{machine F3}]$$
$$(5)\text{--}(7):\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (5)\text{--}(7).\ \blacksquare$$

**Phys.** The tier ends where the record honestly ends. Everything the corpus can compute about the
multi-seal amplitude is computed: the grouping sectors and their statistics, the composed cells and their
edge counts, the resolvent and its rational attenuation, the dressing and its exact excess means, the
three-attachment amplitude census and its sparse winding structure. And the thing the directive actually
wanted — the sign of the nine-attachment ensemble binding — is not among them, for a reason that is now
precise rather than vague. Three constructions are missing and they are named: the amplitude
configuration space of a composed multi-junction support, the connector's own amplitude weight, and a
binding functional for several nucleons rather than one. No bound rescues it, because the smaller cases
that a bound would lean on are missing the same three things. What the corpus does say is directional:
every binding it has ever constructed is negative or zero, so a positive, unbound nine-attachment state
has no precedent in the record and the isotope cutoff stays exactly where IT.5 left it — a conjecture,
now with its obstruction drawn to scale. Nothing measured entered; nothing was declared; no isotope was
identified.

---

## §Cal-IT — unchanged from Tier IT.8

**Empty at this tier.** No parameter is added; the closable registers are derived and the obstruction is
recorded as open rows, not parameters. The parametric residues remain the open rows and the inherited
owed declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1), $\varepsilon_q$
(AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$, $\hat\mu'^2$,
$\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile, the lift and the vielbein (AT.60).

## §Open-IT additions from Tier IT.8

| row | content | locus |
|---|---|---|
| **IT-O2 — ADVANCED, ¬closed** | the multi-seal configuration calculus is BUILT for the sector statistics, the composed-cell geometry [Census FT.50], the channel resolvent + attenuation [AT.52], the dressing register + ℵ-excess [AT.53/AT.54], and the N=3 amplitude census [FT.106(3)]. **Not built:** the composed-support Def-H.32 amplitude configuration space beyond the frozen B=4 census | IT.25; IT.26; IT.27(1),(2) |
| **IT-O5 — OPEN, obstruction localized** | the isotope cutoff / the N=9 binding sign needs THREE named constructions: (1) the composed-support amplitude configuration space at N=9; (2) the connector's amplitude weight $v_\Gamma$ [Def-H.32(2)]; (3) the multi-junction ensemble binding functional [BM.21/BM.137 are 3-constituent / two-chain]. Neither computable nor boundable; every constructed read ≤ 0 | IT.27(2),(4) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24]: (IT-O1) the
transit-leg amplitude, (IT-O3) the handshake-indicator operational theory, the owed mass-read route
choice [IT.14(3)], and the Level-5 ledger [AT.63(3),(5)]. **IT-O4 stays CLOSED** [IT.21(1)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.9: the isotope-cutoff resolution — the non-dynamical binding sign and the "neutron stability" template

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.9 — the Architect's directive to continue the
amplitude side (IT-O5), with the inspiration to *"look at how the 'neutron's' stability was resolved —
it was coming ≤ 0; the non-dynamical picture causes this."* The tier draws the exact template: the
static/non-dynamical ledger resolves the "neutron" as stable (Q ≤ 0) by charge-degeneracy, and the same
structure resolves the isotope sequence as bound at every $k$ — so the cutoff is not static but dynamical.
**Tags.** IT.28–IT.30. **Pattern.** the adjudication tiers (IT.6/IT.7/IT.8's shape), premise audit
logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays
empty; no clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.4–IT.8 is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/cutoff_resolution.py` → **16/16 exact** (the BM.137(3)
two-chain binding re-derived; the BM.41 Q-value sign theorem re-derived on symbolic masses; the FT.50(1)
informational excess; the BM.122(6) transit-bar census); `run_all_level6.py` → **10 checkers, 157 exact
markers, 0 failures**; `check_level6_format.py` → the gate over all nine Part 6 documents. Exact
arithmetic: `Fraction` mass coefficients over a symbolic $u=\ln2/\mathfrak h$, integer sign censuses, a
rational $\varepsilon_q$ grid.
**No floating point in any assertion. No measured value enters any clause [P5] — the neutron lifetime,
the hydrogen-4 resonance widths, and every binding energy in MeV stay quarantined [EXT] scoring targets,
cited nowhere. No species identification [Def-BM.3(1),(7)] — "neutron", "proton", "tritium",
"hydrogen-4", "resonance" stay quoted labels; the derived objects are the static binding-read signs and
the transit-leg absence.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13e): *"please continue [IT-O5]. Also if you need
inspiration, look at how the 'neutron's' stability was resolved. It was coming ≤ 0. The thing is the
non dynamical picture. That causes this."* Executed by making the hint exact (IT.28), census-ing every
constructed static binding read (IT.29), and adjudicating IT-O5 with the cutoff relocated to the
dynamics (IT.30); three premise corrections logged at IT.30(3).

---

### IT.28 — The "neutron stability" template: the non-dynamical picture gives $Q\le0$

**Thm.**
$$(1)\quad\textbf{THE CHARGE-DEGENERACY OF THE REST READS:}\qquad m=E_{\mathrm{int}}\cdot u,\ \ u=\ln2/\mathfrak h\ [\mathrm{FT.44}(4)];\qquad E_{\mathrm{int}}(\text{``}n\text{''})=E_{\mathrm{int}}(\text{``}p\text{''})=6\ [\mathrm{BM.17};\ \mathrm{BM.26};\ \text{Census}\ \mathrm{FT.35}(2)]:$$
$$\boxed{\ m_n=m_p=6u\ \ \text{EXACTLY on every informational / normalized-ensemble / curvature-flux read}\ }\qquad[\mathrm{BM.28}(1):\ \text{the crystallized count has charge exponent}\ 0;\ \mathrm{BM.30}(3):\ \text{the normalized average is structurally charge-blind}]$$
$$(2)\quad\textbf{THE Q-VALUE SIGN THEOREM (the stability):}\qquad Q:=m_n-m_p-m_\ell-m_\nu=0-(m_\ell+m_\nu)=-(m_\ell+m_\nu)\ [\mathrm{BM.41}(4)]:$$
$$m_\ell\ge2u>0\ [\mathrm{FT.28}\ \text{the digon floor};\ \mathrm{FT.44}(4)],\quad m_\nu\ge0\ [\mathrm{EW.33}\ \mathrm{PSD}]\ \Rightarrow\ \boxed{\ Q\le-2u<0:\ \ \textbf{the}\ \beta\textbf{-decay vertex is KINEMATICALLY CLOSED on every adopted read}\ }\ [\mathrm{BM.41}(4)(\mathrm e)]$$
$$(3)\quad\textbf{THE CLOSURE DEEPENS AND SURVIVES:}\qquad\Delta m_{\mathrm{EM}}=\tfrac{3ce^2\ln2}{2\pi\mathfrak h}>0\ [\mathrm{BM.46}(4)]\ \text{makes the charged member heavier}:$$
$$Q_{\mathrm{corr}}=-(\Delta m_{\mathrm{EM}}+m_\ell+m_\nu)<Q<0\ \ [\mathrm{BM.49}:\ \text{``strictly deeper''}];\qquad\text{the closure survives the complete force operator}\ [\mathrm{BM.52}(4)]$$
$$(4)\quad\textbf{THE NON-DYNAMICAL CAUSE (the Architect's point, made exact):}\qquad\text{``the closure is a theorem ABOUT THE READS,}\ \neg\text{about the vertex grammar''}\ [\mathrm{BM.41}\ \text{l.2299}]:$$
$$\text{the static rest reads are charge-degenerate}\ (1)\ \Rightarrow\ \neg\exists\ \text{a mass splitting to open a decay};\qquad\boxed{\ \text{the ``neutron'' is STABLE because the picture is NON-DYNAMICAL — the physical decay needs a splitting the static reads do not produce}\ }$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(4)\ \text{(re-derived from the frozen rows)};\qquad\textbf{re-produced frozen rows:}\ \mathrm{BM.41}(2),(4),\ \mathrm{BM.49},\ \mathrm{BM.52}(4),\ \mathrm{BM.28}(1);\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, D2.9 (Parts 1–2); Def-H.32(6), FT.28, FT.44(4), EW.33 (Part 3); IT.14(2), IT.18(1) (this level); AT.63(2) (Level 5); Def-BM.3(2),(3), BM.17, BM.26, BM.28(1), BM.30(3), BM.41(2),(4), BM.46(4), BM.49, BM.52(4), Census FT.35(2) (Part 4); exact `Fraction` mass coefficients over a symbolic $u=\ln2/\mathfrak h$, integer sign arithmetic [math; machine: `cutoff_resolution.py` §A, 5/5].

**Pf.**
$$(1):\ E_{\mathrm{int}}=6\ \text{on both classes re-cited};\ m=6u\ \text{both};\ \text{the charge-exponent-0 and charge-blindness rows re-cited}\ [\text{machine A1}]$$
$$(2):\ Q=0-(m_\ell+m_\nu);\ m_\ell\ge2u,\ m_\nu\ge0\ \Rightarrow\ Q\le-2u<0\ \text{on the most-favorable lepton mass}\ [\text{machine A2}];\ \text{the}\ m_n{>}m_p\ \text{absence witness}\ [\text{machine A2x}]$$
$$(3):\ \Delta m_{\mathrm{EM}}>0\ \Rightarrow\ Q_{\mathrm{corr}}=-(\Delta m_{\mathrm{EM}}+m_\ell+m_\nu)<Q<0\ [\text{machine A3}];\qquad(4):\ \text{the reads-not-grammar row re-cited};\ \text{assembly}\ [\text{machine A4}].\ \blacksquare$$

**Phys.** The tier begins where the Architect pointed, and the pointer is exact. The corpus asked whether
its neutral three-juncture decays into its unit-class partner plus a lepton pair, and the answer came out
closed on every read it had — not because a decay was forbidden, but because every static mass read it
owns makes the two junctions identical, six bits over the scale, charge-blind to the last monomial. With
equal parent and daughter masses the daughter falls below its own mass shell for any positive emitted
mass, so the Q-value is minus the lepton masses, strictly negative, and the electromagnetic correction
only deepens it. That is stability, and it is an artifact: a real neutron decays, and what the static
ledger lacks is the dynamics that would split the two. This is the template for everything below — a
non-dynamical picture does not produce decay, and it does not produce an unbound state either.

---

### IT.29 — The static binding-sign census and the dynamics gap

**Thm.**
$$(1)\quad\textbf{EVERY CONSTRUCTED STATIC BINDING READ IS}\ \le0\ \textbf{(bound or closed):}\qquad\begin{array}{l|l|l}\textbf{the read}&\textbf{the value}&\textbf{the sign}\\\hline\text{3-constituent ensemble}\ [\mathrm{BM.21}(4)]&\mathcal B(S_j;1,1,1)&<0\ \text{(bound)}\\\text{two-chain ensemble}\ [\mathrm{BM.137}(3)]&\mathcal B^{(2)}_{\mathrm{ens}}=-\tfrac{4u}{1+u}\tfrac{\ln2}{\mathfrak h}&<0\ \text{(bound)}\\\text{neutron}\ \beta\ \text{Q-value}\ [\mathrm{BM.41}(4)]&Q=-(m_\ell+m_\nu)&<0\ \text{(closed)}\\\text{informational, disjoint}\ [\mathrm{FT.50}(1);\ \mathrm{IT.18}(1)]&\mathcal B_{\mathrm{info}}=0&=0\ \text{(marginal)}\end{array}$$
$$\text{the two-chain}\ \mathcal B^{(2)}_{\mathrm{ens}}\ \text{re-derived STRICTLY}<0\ \text{on a 63-point rational}\ \varepsilon_q\ \text{grid};\qquad\boxed{\ \neg\exists\ \text{a constructed static read giving an unbound}\ (\ge0\ \text{physical binding})\ \text{state}\ }$$
$$(2)\quad\textbf{THE ONE POSITIVE STATIC READ IS NON-PHYSICAL:}\qquad\text{the informational/cardinal mass excess of the bridged composite}\ [\mathrm{FT.50}(1);\ \mathrm{IT.20}(1)]:$$
$$m_{\mathrm{comp}}-\textstyle\sum m_{\mathrm{sep}}=(8k{+}6)u-6(k{+}1)u=+2k\,u=(0,2,4,6)u\ \ \text{at}\ k{=}0,1,2,3;\qquad\text{strictly monotone,}\ \neg\text{crossing zero for}\ k\ge1;$$
$$\boxed{\ \text{it flags the DEUTERON}\ (k{=}1)\ \text{``unbound'' by}\ +2u\ \text{exactly as}\ k{=}3\ \text{by}\ +6u\ \Rightarrow\ \text{it cannot locate a last-bound member}\ }$$
$$(3)\quad\textbf{THE UNIFORM STATIC PATTERN:}\qquad\text{the physical (ensemble) binding is}\ \le0\ \text{in every constructed case}\ (1);\ \text{the informational excess is monotone and non-physical}\ (2);\ \text{the neutron decay is closed}\ [\mathrm{IT.28}]:$$
$$\boxed{\ \textbf{the static/non-dynamical ledger gives a BOUND}\ (\le0)\ \textbf{isotope sequence at EVERY}\ k\ \text{— NO static cutoff, no last-bound member}\ }$$
$$(4)\quad\textbf{THE DYNAMICS GAP (the resonance is dynamical):}\qquad\neg\exists\ \text{a formed transit-quantum supply vertex, on FOUR independent grounds}\ [\mathrm{BM.122}(6)(\mathrm O1)\text{--}(\mathrm O4)]:$$
$$(\mathrm O1)\ \neg\text{a gauged chiral coupling};\ (\mathrm O2)\ \text{the transit alternative is deficit}\ 1'\ [\mathrm{FT.125}(4)];\ (\mathrm O3)\ \neg\text{a momentum-space resolvent}\ [\mathrm{BM.6}(6)];\ (\mathrm O4)\ \text{the transit object carries no winding carrier}\ [\mathrm{D3.7}];$$
$$\therefore\ \boxed{\ \neg\exists\ \text{a formed radiation / transit-leg AMPLITUDE between junctions}\ [\mathrm{IT.1}(6);\ \mathrm{IT\text{-}O1}]\ \Rightarrow\ \text{the dissociation/decay dynamics is unconstructed}\ }$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(4);\qquad\textbf{re-produced frozen rows:}\ \mathrm{BM.21}(4),\ \mathrm{BM.137}(3),\ \mathrm{BM.122}(6);\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, D3.7, CT0.12, CT3.20, FT.80(7), FT.125(4) (Parts 1–2); Def-H.32(6), FT.28, FT.44(4), FT.107(2),(3), EW.33 (Part 3); IT.1(6), IT.18(1), IT.20(1), IT.21(2), IT.28, IT-O1 (this level); AT.63(2) (Level 5); Def-BM.3(2),(3), Def-BM.8(8), BM.6(6), BM.21(4), BM.122(6), BM.137(3), Census FT.50(1) (Part 4); exact `Fraction` sign censuses over a rational $\varepsilon_q$ grid, integer mass-excess arithmetic [math; machine: `cutoff_resolution.py` §§B–C, 7/7].

**Pf.**
$$(1):\ \mathcal B^{(2)}_{\mathrm{ens}}=-\tfrac{4u}{1+u}\ \text{with}\ u{=}4\varepsilon_q\ \text{re-derived from}\ D_n{=}(1{-}u^n)/(1{-}u),\ \text{sign-censused}\ <0\ \text{on a 63-point grid};\ \mathrm{BM.21}(4)\ \text{'s sign re-cited}\ [\text{machine B1}]$$
$$(2):\ (8k{+}6)-6(k{+}1)=2k\ \text{term by term};\ \text{the monotonicity and the no-crossing row};\ \text{the}\ k{=}1/k{=}3\ \text{same-sign witness}\ [\text{machine B2, B2x}]$$
$$(3):\ \text{the conjunction of}\ (1),(2)\ \text{and}\ \mathrm{IT.28}\ [\text{machine B3}];\qquad(4):\ \text{the four grounds re-cited from}\ \mathrm{BM.122}(6)(\mathrm O1)\text{--}(\mathrm O4);\ \text{the transit-leg absence}\ [\mathrm{IT.1}(6)]\ [\text{machine C1}].\ \blacksquare$$

**Phys.** Count every binding the corpus has actually built and they all lean the same way: the
three-constituent junction is bound, the two-chain floor is bound, the neutral junction's decay is
closed, and the only read that comes out positive is the crude edge count, which is heavier for the
deuteron too and so says nothing about where a family ends. A non-dynamical ledger, it turns out, does
not make composites fall apart — it makes them bind or sit exactly at threshold, and it makes decays
close. The resonances the identification layer knows are the opposite: states that come apart, that
dissociate, that decay. Coming apart is a dynamical act, and the inventory has no formed transit leg for
it — four separate grounds say the radiation supply vertex is not there. So the static picture and the
empirical resonance live on opposite sides of a line the corpus has not yet drawn: the ledger binds
everything it can read, and the unbinding is a dynamics it has not built.

---

### IT.30 — The adjudication: IT-O5's static side closes, the cutoff relocates to the dynamics

**Thm.**
$$(1)\quad\textbf{IT-O5 STATIC SIDE CLOSES — the cutoff is}\ \neg\textbf{a static phenomenon:}\qquad\boxed{\ \textbf{the non-dynamical ledger gives a BOUND}\ (\le0)\ \textbf{isotope sequence at every}\ k\ \text{— NO last-bound member, NO structural termination at}\ k{=}2\ }$$
$$\text{by the same charge-degeneracy / additivity that makes the ``neutron'' stable}\ [\mathrm{IT.28};\ \mathrm{BM.41}(4)(\mathrm e)]:\quad\text{the ``structural termination at}\ k{=}2\text{'' is REFUTED as a static claim}$$
$$(2)\quad\textbf{THE EMPIRICAL CUTOFF RELOCATES TO IT-O1 (the dynamics):}\qquad\text{the hydrogen-4}^+\ \text{resonances are unbound/decaying}=\ \text{a dissociation/transit amplitude},\ \neg\exists\ \text{as formed}\ [\mathrm{BM.122}(6);\ \mathrm{IT.29}(4)]:$$
$$\boxed{\ \text{the cutoff, if derived, is a DYNAMICAL dissociation threshold}\ (\mathrm{IT\text{-}O1}),\ \neg\text{a static binding sign flip}\ (\mathrm{IT\text{-}O5}/\mathrm{IT\text{-}O2})\ }\qquad\text{the empirical widths stay a}\ [\mathrm{P5}]\ \text{quarantined}\ [\mathrm{EXT}]\ \text{target}$$
$$(3)\quad\textbf{THE PREMISE CORRECTIONS (on the record):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``the amplitude-weighted ensemble binding is}\ \ge0\ \text{(unbound/resonance) at}\ N{=}9/12\text{''}&\textbf{REFUTED as a static claim}\ [\mathrm{IT.29}(1),(3)]:\ \text{every constructed static read is}\ \le0;\ \text{the informational excess is non-physical};\ \text{the neutron precedent gives stability,}\ \neg\text{decay}\\\text{``the family structurally terminates at}\ k{=}2\text{''}&\textbf{RELOCATED}\ [\mathrm{IT.30}(1),(2)]:\ \neg\text{a static termination (bound at every}\ k\text{); the empirical resonance is dynamical}\ (\mathrm{IT\text{-}O1})\\\text{``compute/bound the}\ N{=}9\ \text{amplitude binding sign''}&\textbf{RESOLVED WITHOUT IT}\ [\mathrm{IT.30}(4)]:\ \text{the non-dynamical sign structure}+\text{the neutron template fix the verdict};\ \text{the VALUE stays}\ \mathrm{IT\text{-}O2}\end{array}$$
$$(4)\quad\textbf{IT-O2 REDUCED TO THE BINDING VALUE:}\qquad\text{the multi-nucleon ensemble binding VALUE stays open (the three}\ \mathrm{IT.27}(2)\ \text{constructions: the composed-support amplitude space, the connector's}\ v_\Gamma,\ \text{the multi-junction binding functional});$$
$$\text{but it does}\ \neg\text{gate the cutoff VERDICT, which the non-dynamical sign structure resolves:}\quad\boxed{\ \text{the sign is}\ \le0\ \text{(bound); only the magnitude awaits}\ \mathrm{IT\text{-}O2}\ }$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses}),\ \mathrm{CT3.22},\ \mathrm{FT.55}(1),\ \mathrm{BM.143}(1)$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{cutoff\_resolution.py}\to\textbf{16/16 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{10 checkers, 157 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{9 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, CT3.22, FT.55(1), FT.125(4) (Parts 1–2); Def-H.32(6) (Part 3); IT.1(6),(8), IT.14(2), IT.18(1), IT.20(1), IT.21(2), IT.27(2), IT.28, IT.29, IT-O1, IT-O2, IT-O5 (this level); AT.39(8), AT.63(2) (Level 5); Def-BM.3(1),(7), BM.30(5), BM.41(4), BM.83, BM.122(6), BM.134(5), BM.137(3), BM.143(1), Census FT.50(1) (Part 4); the assembly rows [math; machine: `cutoff_resolution.py` §D, 4/4].

**Pf.**
$$(1):\ \text{the conjunction of}\ \mathrm{IT.28}(4)\ \text{and}\ \mathrm{IT.29}(3)\ [\text{machine D1}];\qquad(2):\ \mathrm{IT.29}(4)\ \text{'s transit-bar re-cited};\ \text{the relocation to}\ \mathrm{IT\text{-}O1}\ [\text{machine D2, D3}]$$
$$(3):\ \text{the correction table verified against each cited locus};\qquad(4):\ \text{the sign-vs-value separation re-cited from}\ \mathrm{IT.27}(2);\ \mathrm{IT.29}(1),(3)$$
$$(5)\text{--}(7):\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (5)\text{--}(7).\ \blacksquare$$

**Phys.** The question the level has carried since the isotope sequence opened now has a clean answer, and
it is the answer the Architect's hint predicted. The corpus does not make hydrogen-four fly apart, and it
does not make tritium the last bound isotope, for the same reason it does not make the neutron decay: its
picture is non-dynamical, and a non-dynamical picture binds. Every static read leans negative or sits at
zero, the one positive read is the crude edge count that condemns the deuteron too, and the transit leg
that a real dissociation would need is absent on four independent grounds. So the isotope cutoff is not a
static theorem and not a static no-go — it is a dynamical question, and it moves to the one open row that
carries dynamics. What the static ledger does say is firm: bound at every attachment count it can read,
stable for the same structural reason its neutral junction is stable. The magnitude of that binding still
waits on the amplitude construction, but the sign, and with it the verdict on the cutoff, does not.
Nothing measured entered; nothing was declared; no isotope was identified.

---

## §Cal-IT — unchanged from Tier IT.9

**Empty at this tier.** No parameter is added; the cutoff verdict is resolved by the non-dynamical sign
structure and the empirical widths stay quarantined [EXT]. The parametric residues remain the open rows
and the inherited owed declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1),
$\varepsilon_q$ (AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$,
$\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile, the lift and the
vielbein (AT.60).

## §Open-IT additions from Tier IT.9

| row | content | locus |
|---|---|---|
| **IT-O5 — static side CLOSED** | the isotope cutoff is **¬a static/non-dynamical phenomenon**: the ledger gives a bound (≤0) sequence at every $k$ (the "neutron stability" template [BM.41(4)(e)]); no last-bound member exists statically. The **empirical/dynamical side relocates to IT-O1** | IT.30(1),(2); IT.28; IT.29(3) |
| **IT-O1 — gains the cutoff** | the transit/dissociation dynamics is now **the locus of the empirical isotope cutoff**: a formed transit-leg amplitude [BM.122(6)(O1)–(O4) refute it as formed] is what an unbound, decaying hydrogen-4⁺ would require | IT.29(4); IT.30(2) |
| **IT-O2 — reduced to the VALUE** | the multi-nucleon ensemble binding **value** stays open (the three IT.27(2) constructions), but it **¬gates the cutoff verdict** — the sign (≤0, bound) is resolved by the non-dynamical structure | IT.30(4); IT.27(2) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27]:
(IT-O3) the handshake-indicator operational theory, the owed mass-read route choice [IT.14(3)], and the
Level-5 ledger [AT.63(3),(5)]. **IT-O4 stays CLOSED** [IT.21(1)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.10: the Macroscopic Calibration Anchor — three ledger-native definitions and the shared-currency bypass of the incommensurability bar

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.10 — the Architect's directive to formalize the
Macroscopic Calibration Anchor from three stipulated ledger-native definitions (inter-nuclear distance,
macroscopic Pauli exclusion, BEC-readiness), prove they bypass the incommensurability bar as geometric
consequences, and assemble the kinematics/rotational machinery — with the Calibration Era's values left
deferred.
**Tags.** IT.31–IT.33. **Pattern.** the adjudication tiers (IT.7/IT.8/IT.9's shape), premise audit logged
in-tier; the three definitions accepted as the Architect's definitional act, then grounded row by row.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays empty;
the Calibration Era stays **deferred** [AT.63(4)]; no clause of Parts 1–4, of Level 5's closed record, or
of Tiers IT.4–IT.9 is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/calibration_anchor.py` → **14/14 exact** (the IT.2 grammar engine
reused; exact `Fraction` certificates for the incommensurability bar; the multiplicative exchange law and
the Born-width invariant re-derived); `run_all_level6.py` → **11 checkers, 171 exact markers, 0
failures**; `check_level6_format.py` → the gate over all ten Part 6 documents. Exact arithmetic: integer
binomials and factorials, `Fraction` powers and certificates, sign censuses.
**No floating point in any assertion. No measured value enters any clause [P5] — no lattice constant, no
mass, no $\mathfrak h$, no $\varepsilon_q$; every such figure stays a quarantined [EXT] scoring target,
cited nowhere. No species identification [Def-BM.3(1),(7)] — "He-4", "He-3", "BEC", "laptop" stay quoted
labels; the derived objects are the geometric read $\Delta x_B$, the cardinalities $\dim\wedge^3(\mathbb C^2)$
and $C_{\mathrm{cap}}$, and the exchange sign $\varepsilon=(-1)^A$.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13f), re-issued with three REQUIRED ledger-native
definitions to be used verbatim, and the constraint *"avoiding any smooth-manifold smuggling."* Executed
by grounding each definition in its cited rows, correcting Definition 3 where it diverges from the census
(the rows win), deriving the shared-currency bypass, and issuing no calibration value; three premise
corrections logged at IT.33(3).

---

### IT.31 — The three definitions, grounded in derived rows (Definition 3 corrected)

**Thm.**
$$(1)\quad\textbf{DEFINITION 1 — INTER-NUCLEAR DISTANCE (grounded):}\qquad\Delta x_{\mathrm B}=\mathfrak h/(E_{\mathrm{int}}\ln2)\ \ \text{is a derived chart-side LENGTH}\ [\mathrm{Def\text{-}BM.4}(1);\ \mathrm{BM.13}(4)],\ \neg\text{a smooth coordinate}:$$
$$\Delta x_{\mathrm B}\cdot r_s=\tfrac{\mathfrak h}{E\ln2}\cdot\tfrac{\mathfrak h E}{2}=\tfrac{\mathfrak h^2}{2\ln2}\qquad\textbf{EXACTLY}\ E_{\mathrm{int}}\textbf{-independent}\ [\mathrm{BM.17}(3);\ \text{machine: the coefficient}\ \tfrac12\ \text{on every floor}\ \{2,6,12,18,24,60\}];$$
$$\boxed{\ \Delta x_{\text{lattice}}\propto\Delta x_{\mathrm B}\ \ \text{is the Architect's stipulated bridge; the proportionality constant and the multi-composite LATTICE geometry are}\ \neg\text{derived (no inter-nuclear-distance row exists; IT-O4's connector gives}\ E_{\mathrm{int}}{+}2,\ d{=}0,\ \neg\text{a distance)}\ }$$
$$(2)\quad\textbf{DEFINITION 2 — MACROSCOPIC PAULI EXCLUSION (grounded; ``scaling'' is a misnomer):}\qquad\dim\wedge^3(\mathbb C^d)=\binom d3:\quad\dim\wedge^3(\mathbb C^2)=\binom23=0,\quad\dim\wedge^3(\mathbb C^3)=\binom33=1\ \ [\mathrm{BM.128}(5)];$$
$$C_{\mathrm{cap}}=16=D_{\mathrm{tick}}(3)\ \ \text{exactly saturated},\quad D_{\mathrm{tick}}(4)=32>16\ \ \text{inadmissible}\ [\mathrm{CT0.12};\ \mathrm{CT0.13}];\qquad\boxed{\ \text{both are SCALE-FREE CARDINALITIES — the exclusion holds identically at every scale,}\ \neg\text{``scaled''}\ }$$
$$(3)\quad\textbf{DEFINITION 2's MECHANISM (grounded):}\qquad g_\delta(N)>0\ \ \forall N\ge4\ \ (\text{the grammar forces}\ \delta\text{-mixing past the protected}\ N{=}3)\ [\mathrm{BM.31}(2);\ \mathrm{IT.6}(5)];\quad n\ge4\ \text{junctions are}\ D^-\text{-saturated, retained}\neg\text{accessible}\ [\mathrm{CT4.1};\ \text{Census}\ \mathrm{FT.35}\ \mathrm{Rmk}]:$$
$$\therefore\ \text{``no multi-seal composite occupies the identical boundary state without triggering}\ \delta\text{-mixing or capacity saturation'' is a theorem of the grammar + the capacity census — a COMBINATORIAL limit,}\ \neg\text{a wavefunction antisymmetry}$$
$$(4)\quad\textbf{DEFINITION 3 — BEC-READINESS (CORRECTED: it is the exchange sign, not an exclusive 4Z class):}\qquad\text{the multiplicative exchange law}\ [\mathrm{BM.128}(7);\ \mathrm{BM.129}(4),(5)]:$$
$$\varepsilon(\Gamma)=(-1)^{|\sum_ak_a|}=\prod_{a=1}^{A}\varepsilon(c_a)=(-1)^{A}\ \ \text{for}\ A\ \text{fermionic nucleons}\qquad\boxed{\ \textbf{bosonic (BEC-ready)}\iff A\ \textbf{even}\ }$$
$$\text{``He-4''}\ (A{=}4)\to\varepsilon{=}{+}1\ \text{(boson)};\quad\text{``He-3''}\ (A{=}3)\to\varepsilon{=}{-}1\ \text{(fermion, needs doublets)};\quad\text{deuteron}\ (A{=}2)\to\varepsilon{=}{+}1\ \text{(boson)}$$
$$(5)\quad\textbf{THE DEFINITION-3 CORRECTION (the rows win):}\qquad\text{``exclusively the}\ 4\mathbb Z\ \text{class'' is FALSE at}\ N{=}12:\quad g(12)=164395=g_\varepsilon(12){=}15400\ (40/427,\ 4\mathbb Z)+g_\delta(12){=}148995\ (387/427,\ 2\mathbb Z)\ \ \textbf{is}\ \delta\textbf{-DOMINANT}\ [\mathrm{IT.6}(6);\ \mathrm{IT.9}(5)];$$
$$\text{the per-grouping}\ 4\mathbb Z/2\mathbb Z\ \text{SEALING class}\ [\mathrm{BM.31}(4)]\ \text{is a DIFFERENT register from the whole-composite exchange}\ \varepsilon{=}(-1)^A;\qquad\text{``}N\ \text{a multiple of 4'' is too strict: the deuteron}\ (A{=}2,N{=}6)\ \text{is bosonic yet}\ 6\not\equiv0\ (4)$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5)\ \text{(the definitions grounded; Def 3 corrected to}\ \varepsilon{=}(-1)^A\text{)};\qquad\textbf{stipulated,}\neg\textbf{derived:}\ (1)\ \text{'s proportionality + lattice geometry};\qquad\neg\text{a declaration},\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)],\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT0.12, CT0.13, CT3.22, CT4.1, D0.8 (Parts 1–2); Def-H.32(7), FT.34(3), FT.44(4) (Part 3); IT.6(5),(6), IT.9(5), IT-O4 (this level); AT.63(2),(4) (Level 5); Def-BM.3(7), Def-BM.4(1), BM.2(2), BM.13(4), BM.17(3), BM.31(2),(4), BM.128(5),(7), BM.129(4),(5), Census FT.35 (Part 4); exact integer binomials and factorials, the grammar engine, `Fraction` cancellation certificates [math; machine: `calibration_anchor.py` §A, 5/5].

**Pf.**
$$(1):\ \tfrac{\mathfrak h}{E\ln2}\cdot\tfrac{\mathfrak h E}{2}=\tfrac{\mathfrak h^2}{2\ln2};\ \text{the coefficient}\ (1/E)(E/2)=\tfrac12\ \text{computed on every floor, single-valued}\ [\text{machine A1}]$$
$$(2):\ \binom23=0,\ \binom33=1;\ D_{\mathrm{tick}}(n)=2^{n+1}\ \text{at}\ n=3,4\ \text{against}\ C_{\mathrm{cap}}=16\ [\text{machine A2}];\qquad(3):\ g_\delta(N)=g(N)-g_\varepsilon(N)>0\ \text{for}\ N=4..12\ [\text{machine A3}]$$
$$(4):\ \varepsilon(\Gamma)=\prod_a\varepsilon(c_a)=(-1)^A\ \text{by the multiplicative law, evaluated}\ A=1..6\ [\text{machine A4}];\qquad(5):\ g_\varepsilon(12)=15400<g_\delta(12)=148995;\ \text{the deuteron witness}\ \varepsilon(2){=}{+}1,\ 6\bmod4{=}2\ [\text{machine A5}].\ \blacksquare$$

**Phys.** Three names are given ledger-native meanings and each is checked against what the corpus already
proves. The first is a length: the Born width, whose product with the Schwarzschild partner cancels the
internal energy exactly, leaving a pure scale — a honest geometric anchor, though the leap from one
composite's width to a lattice spacing is a stipulation the record does not yet earn. The second is a
count: three two-dimensional carriers cannot antisymmetrize, and a junction cannot exceed sixteen, and
neither fact cares about scale, so calling it a scaling is the one word that misleads. The third needed
repair. Bose-readiness is not about a grouping being exclusively baryonic — at twelve attachments the
delta-containing groupings outnumber the pure ones almost ten to one — it is the parity of the nucleon
count, the product of the constituents' exchange signs, positive for helium-four and negative for
helium-three and positive again for the deuteron, which no attachment-count congruence captures. The
definitions stand, one of them corrected, and all three are exactly what the ledger can say without
smuggling in a wavefunction.

---

### IT.32 — The anchor theorem: the shared geometric/cardinal currency bypasses the incommensurability bar

**Thm.**
$$(1)\quad\textbf{THE BAR (what is blocked):}\qquad2^a3^b5^c=1\implies a=b=c=0\ \ [\mathrm{BM.83};\ \text{machine: exhaustive over}\ |a|,|b|,|c|\le12,\ \text{exact}\ \texttt{Fraction}\ \text{powers}]:$$
$$\text{the baryon}\ \{E_{\mathrm{int}},\hat\mu'^2,\rho_{\mathrm B},D_S\}\ \text{and lepton}\ \{\varepsilon_q,x_\pm,w_c,\sigma_\ell\}\ \text{MASS alphabets are DISJOINT};\qquad\frac{\ln1280}{\ln960}\notin\mathbb Q\ \ [\mathrm{BM.83}];$$
$$\boxed{\ \text{an absolute macroscopic MASS (``laptop mass'') is a sum across incommensurable currencies}\ \Rightarrow\ \neg\text{computable}\ }\qquad[\mathrm{BM.140}(5)]$$
$$(2)\quad\textbf{THE LOG-INCOMMENSURABILITY, exactly:}\qquad1280=2^8\!\cdot\!5,\ 960=2^6\!\cdot\!3\!\cdot\!5:\quad\frac{1280}{960}=\frac43\in\mathbb Q\ \ \text{but}\ \ \frac{\ln1280}{\ln960}=\frac pq\implies(8q{-}6p)\ln2+(q{-}p)\ln5-p\ln3=0:$$
$$\{\ln2,\ln3,\ln5\}\ \mathbb Q\text{-independent}\implies p=0\ (\text{the}\ \ln3\ \text{term})\ \text{then}\ q=0\ (\text{the}\ \ln5\ \text{term}):\quad\boxed{\ \text{the only solution is trivial}\ \Rightarrow\ \text{no exact mass RATIO across the currencies}\ }$$
$$(3)\quad\textbf{THE BYPASS (the shared currency):}\qquad\begin{array}{l|l}\textbf{the anchor read}&\textbf{its currency}\\\hline\Delta x_{\mathrm B}=\mathfrak h/(E_{\mathrm{int}}\ln2)&\text{a LENGTH (chart-side,}\ \mathfrak h\text{-scaled)}\\\Delta x_{\mathrm B}r_s=\mathfrak h^2/(2\ln2)&\text{a LENGTH}^2,\ E_{\mathrm{int}}\text{-independent}\\\dim\wedge^3(\mathbb C^2)=0,\ C_{\mathrm{cap}}=16&\text{CARDINALITIES (dimensionless)}\\\varepsilon=(-1)^A&\text{a SIGN}\\(q,S,m_{\mathrm{hid}})&\text{the self-averaging observables}\ [\text{Cor}\ \mathrm{FT.15.1}]\end{array}$$
$$\boxed{\ \text{NONE is a cross-currency mass sum}\ \Rightarrow\ \text{they do}\ \neg\text{trip}\ \mathrm{BM.83}:\ \ \text{measuring a geometric CONSEQUENCE}\ \ne\ \text{summing masses}\ }$$
$$(4)\quad\textbf{THE KINEMATICS + ROTATIONAL MACHINERY (Steps 1,3, assembled):}\qquad\text{the forward generator}=\ \mathrm{BM.131}\ \text{(Haar--Poisson / Lyapunov contraction) on}\ \mathrm{CT1.12}\ \text{(the emergent metric)};$$
$$\text{the antimatter CP-flip}=\ \mathrm{Def\text{-}H.33}\ \text{'s orientation involution}\ \hat\omega;\qquad\text{the frame-by-frame propulsion}=\ \mathrm{Def\text{-}H.32}(7)\ \text{'s}\ J^\pm\ \text{Janus move system};$$
$$\text{the spin holonomy}=\ \mathrm{AT.46};\qquad\text{the Pauli term}=\ \mathrm{AT.56}\text{--}\mathrm{AT.58}\ \text{(the bivector census; the Weitzenböck birth at tree coefficient 1)}$$
$$(5)\quad\textbf{THE IDEAL OBSERVER (Step 2):}\qquad\text{Def-H.9's register}\ o\ \text{reads an EM-SEALED atom rung-2-mediated (the boundary triple inter-system accessible)}\ [\mathrm{IT.1}(1),(3);\ \mathrm{IT.2}]:$$
$$\text{a BARE baryon is DARK by read-species separation (colour}\ \neg\text{observable inter-system}\ [\mathrm{CT3.22}]);\qquad\boxed{\ \text{every baryon datum arrives EM-mediated}=\ \text{geometrically}\ \Rightarrow\ \text{the anchor is a GEOMETRIC read,}\ \neg\text{a bare mass}\ }$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{re-produced frozen rows:}\ \mathrm{BM.83},\ \mathrm{BM.128}(5),\ \text{Cor}\ \mathrm{FT.15.1};\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P1, P5, CT0.12, CT0.13, CT1.12, CT3.22 (Parts 1–2); Def-H.9, Def-H.32(7), Def-H.33, FT.15, FT.44(4) (Part 3); IT.1(1),(3), IT.2, IT.5, IT.31 (this level); AT.46, AT.54(6), AT.56, AT.57, AT.58, AT.63(2) (Level 5); Def-BM.4(1), BM.13(4), BM.83, BM.128(5),(7), BM.131, BM.134(5), BM.140(5) (Part 4); exact `Fraction` certificates for the Diophantine and log-independence, the currency-set disjointness [math; machine: `calibration_anchor.py` §§B–C, 5/5].

**Pf.**
$$(1):\ \text{the exhaustive}\ 2^a3^b5^c=1\ \text{census}\Rightarrow\{(0,0,0)\}\ [\text{machine B1}];\ \text{the disjoint-alphabet row re-cited}\ [\mathrm{BM.83};\ \mathrm{BM.140}(5)]$$
$$(2):\ 1280=2^8\cdot5,\ 960=2^6\cdot3\cdot5;\ \text{the linear-independence certificate}\ (8q{-}6p,q{-}p,-p)=(0,0,0)\Rightarrow p{=}q{=}0\ [\text{machine B2}]$$
$$(3):\ \text{the currency-kind census: every anchor read is a length, a cardinality, a sign, or a self-averaging observable -- none a mass sum}\ [\text{machine B3}];\qquad(4),(5):\ \text{the machinery and observer rows re-cited}\ [\text{machine C1, C2}].\ \blacksquare$$

**Phys.** The bar and the bypass are two facts about one ledger. The bar is arithmetic: the baryon and
lepton mass alphabets are built from different primes, so no exact rational ties them, and a laptop's mass
— a sum over both — has no computable value. The bypass is a change of target. A length is not a mass; a
dimension count is not a mass; an exchange sign is not a mass. The Born width, the vanishing wedge, the
capacity sixteen, the parity of the nucleon count — these are the reads a macroscopic object offers that
live in one shared currency, and the measurement theorem explains why they are exactly what an observer
gets: a sealed atom is read through its electromagnetic boundary, geometrically, while a bare baryon is
dark. So the calibration does not sum what cannot be summed; it reads the geometric consequence, and the
kinematics that carries an observer frame by frame — the contraction, the involution, the Janus moves, the
holonomy, the Pauli term — is the machinery already derived, assembled here and cited, not rebuilt.

---

### IT.33 — The adjudication: the anchor is a strategy, the Calibration Era stays deferred

**Thm.**
$$(1)\quad\textbf{THE ANCHOR, DERIVED AS A STRATEGY (extending IT.5):}\qquad\boxed{\ \Delta x_{\text{lattice}}\propto\mathfrak h/(E_{\mathrm{int}}\ln2)\ \ \text{anchors}\ \mathfrak h\ \text{given}\ E_{\mathrm{int}};\ \ \dim\wedge^3(\mathbb C^2){=}0,\ C_{\mathrm{cap}}{=}16\ \ \text{anchor the exclusion STRUCTURE};\ \ \varepsilon{=}(-1)^A\ \ \text{anchors the statistics}\ }$$
$$\text{all in a SHARED geometric/cardinal/sign currency that BYPASSES the mass-summation bar}\ [\mathrm{IT.32}(3)];\qquad\text{the target shifts from MASS SUMMATION to GEOMETRIC CONSEQUENCE — the ``laptop mass'' no-go is shifted,}\ \neg\text{violated}$$
$$(2)\quad\textbf{NO CALIBRATION VALUE IS ISSUED (the honest limit):}\qquad\text{the Calibration Era is DEFERRED — an Era-2-closure act}\ [\mathrm{AT.63}(4);\ \mathrm{IT.1}(5)],\ \neg\text{taken here};$$
$$\mathfrak h\ \text{is the P1 scale SLOT};\quad\varepsilon_q\ \text{is AT-O27 (a DECLARATION,}\ \tfrac18\ \text{distinguished five ways but unissued)};\quad\text{the read rules}\ (\mathrm{M1}')\text{--}(\mathrm{M3}')\ \text{gate every conversion}\ [\mathrm{IT.5};\ \mathrm{AT.54}(6)];$$
$$\boxed{\ \text{the anchor is a STRATEGY (which read anchors which slot),}\ \neg\text{an issued number: the conceptual gap to the Calibration Era is NARROWED,}\ \neg\text{closed}\ }$$
$$(3)\quad\textbf{THE PREMISE CORRECTIONS (on the record):}\qquad\begin{array}{l|l}\textbf{the definition's premise}&\textbf{the derived row}\\\hline\text{(P1) inter-nuclear distance}=\Delta x_{\mathrm B}&\textbf{STIPULATED,}\neg\textbf{DERIVED}\ [\mathrm{IT.31}(1)]:\ \Delta x_{\mathrm B}\ \text{is derived, but the lattice geometry is}\ \neg\text{a ledger object (no inter-nuclear-distance row; IT-O4 gives}\ E_{\mathrm{int}},d,\ \neg\text{a distance)}\\\text{(P2) ``the direct SCALING of}\ C_{\mathrm{cap}},\wedge^3{=}0\text{''}&\textbf{SCALE-FREE}\ [\mathrm{IT.31}(2)]:\ \text{both are cardinalities, identical at every scale -- ``scaling'' is a misnomer}\\\text{(P3) BEC-ready}=``\text{exclusively}\ 4\mathbb Z\text{''},\ N\ \text{multiple of}\ 4&\textbf{CORRECTED}\ [\mathrm{IT.31}(4),(5)]:\ \text{BEC-readiness}=\varepsilon{=}(-1)^A\ (A\ \text{even});\ N{=}12\ \text{is}\ \delta\text{-dominant}\ (387/427);\ \text{the deuteron}\ (A{=}2,N{=}6)\ \text{is bosonic}\end{array}$$
$$(4)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses, no currency mixing}),\ \mathrm{CT3.22},\ \mathrm{FT.55}(1);\qquad\text{the Calibration Era deferred}\ [\mathrm{AT.63}(4)]$$
$$(5)\quad\textbf{the machine state:}\qquad\texttt{calibration\_anchor.py}\to\textbf{14/14 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{11 checkers, 171 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{10 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(6)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no species is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, CT3.22, FT.55(1) (Parts 1–2); Def-H.32(7) (Part 3); IT.1(5),(8), IT.5, IT.31, IT.32, IT-O4, IT-O5 (this level); AT.39(8), AT.54(6), AT.63(2),(4), AT-O27 (Level 5); Def-BM.3(1),(7), BM.30(5), BM.83, BM.134(5) (Part 4); the assembly rows [math; machine: `calibration_anchor.py` §D, 4/4].

**Pf.**
$$(1):\ \text{the conjunction of}\ \mathrm{IT.31}(1),(2),(4)\ \text{and}\ \mathrm{IT.32}(1),(3)\ [\text{machine D1}];\qquad(2):\ \text{the deferral and the read-rule gate re-cited}\ [\mathrm{AT.63}(4);\ \mathrm{IT.5};\ \mathrm{AT.54}(6)]\ [\text{machine D2}]$$
$$(3):\ \text{the correction table verified against each cited locus}\ [\mathrm{IT.31}(1),(2),(4),(5)]\ [\text{machine D3}];\qquad(4)\text{--}(6):\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (4)\text{--}(6).\ \blacksquare$$

**Phys.** The tier ends by saying what it built and what it refused to build. It built a strategy: three
ledger-native reads — a length, two counts, a sign — that a macroscopic object actually offers, all in one
shared currency, so measuring them calibrates without ever summing the baryon and lepton masses that
arithmetic keeps apart. That is the real content of the bypass, and it is the same insight IT.5 reached
from the spectroscopy side. What it refused to build is a number. The scale is a slot, the flicker
threshold is a declaration, the read rules that would turn a geometric measurement into an issued value
are the Calibration Era's own deferred act, and the lattice geometry that would make inter-nuclear distance
a derived object rather than a stipulation is not in the record. So the gap to the Calibration Era is
narrowed to a clean edge — the anchors are named, their currency is proven shared, and one definition was
repaired — and the tier stops there rather than pricing a constant it is not authorized to price. Nothing
measured entered; nothing was declared; no species was identified.

---

## §Cal-IT — unchanged from Tier IT.10

**Empty at this tier.** The anchor is a strategy; no parameter is added and no value is issued. The
Calibration Era stays deferred [AT.63(4)]. The parametric residues remain the open rows and the inherited
owed declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1), $\varepsilon_q$
(AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$, $\hat\mu'^2$,
$\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile, the lift and the vielbein (AT.60), and
now the read rules (M1′)–(M3′) that gate the anchor's conversion to values [IT.5; AT.54(6)].

## §Open-IT additions from Tier IT.10

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.10 opens **no new row**: the Macroscopic Calibration Anchor is derived **as a strategy** (the shared geometric/cardinal/sign currency bypasses the mass-summation bar). The residues it touches are standing ones — the **deferred Calibration Era** (the issued values await the Era-2-closure act + the read rules (M1′)–(M3′) [AT.54(6)]), and the **lattice geometry** that would turn Definition 1's stipulated proportionality into a derived row (a multi-composite geometric construction, adjacent to IT-O2) | IT.33(1),(2); IT.31(1) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27; IT.30]:
(IT-O1) the transit/dissociation dynamics (the locus of the empirical isotope cutoff), (IT-O2) the
multi-nucleon binding value, (IT-O3) the handshake-indicator operational theory, (IT-O5) the isotope
cutoff (static side closed [IT.30(1)]), the owed mass-read route choice [IT.14(3)], and the Level-5
ledger [AT.63(3),(5)]. **IT-O4 stays CLOSED** [IT.21(1)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.11: the amplitude-side verdict — the norm/amplitude layer separation, IT-O2's sign resolved, IT-O1 level-local

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.11 — the Architect's directive to compute the
multi-seal amplitude binding (IT-O2) and probe the transit obstruction (IT-O1). The tier's decisive result
is a **layer separation**: the ensemble binding is a *norm-layer* read (dressing-free), while the
$(-1)^\aleph$ dressing and the contact terms are *amplitude-layer* — so the dressing cannot flip the
binding sign, and the directive's crucial question is answered without computing the (unconstructable)
multi-nucleon amplitude sum.
**Tags.** IT.34–IT.36. **Pattern.** the adjudication tiers (IT.8/IT.9/IT.10's shape), premise audit logged
in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays empty;
no clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.4–IT.10 is modified [AT.63(2)].
**Machine.** `era2/level6_isotopic/checks/amplitude_binding.py` → **16/16 exact** (the AT.52 resolvent
closed forms re-derived; the norm-layer dressing-freedom exhibited on explicit sign sums; the BM.137(3)
two-chain binding re-derived on a rational grid); `run_all_level6.py` → **12 checkers, 187 exact markers,
0 failures**; `check_level6_format.py` → the gate over all eleven Part 6 documents. Exact arithmetic:
integer binomials, `Fraction` residues and binding coefficients, exhaustive sign-assignment sums.
**No floating point in any assertion. No measured value enters any clause [P5] — no binding energy in MeV,
no isotope width; every such figure stays a quarantined [EXT] target, cited nowhere. No species
identification [Def-BM.3(1),(7)].**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13g): *"Close IT-O2 (the amplitude binding) and probe
IT-O1 (the transit obstruction) … does the full Def-H.32 ensemble sum, with its rational dressing and
contact terms, preserve this binding, or does it unlock a dissociation channel? … Scenario A (closure) …
Scenario B (residue)."* Executed with the finding that the binding is norm-layer (dressing-free), so the
dressing cannot flip it; the value stays uncomputed and the transit absence is level-local — neither
scenario holds as stated; four premise corrections logged at IT.36(3).

---

### IT.34 — The layer separation: the ensemble binding is norm-layer and dressing-free

**Thm.**
$$(1)\quad\textbf{THE TWO WEIGHT LAYERS}\ [\mathrm{Def\text{-}H.32}(2);\ \mathrm{CT2.8}]:\qquad w(R,\sigma)=\mathcal J(C)\prod_{e}G(e)\cdot(-1)^{\aleph(\sigma,C)}\ \ [\mathrm{A8}];\qquad\text{at (S1)}\ G(e)=-\sigma_e,\ |G(e)|=1:$$
$$\textbf{amplitude layer:}\ \ v_\Gamma(R):=\sum_\sigma w(R,\sigma)=2^{|R|}(-1)^{\sum\kappa}\ \ \text{on covers,}\ 0\ \text{else}\ [\mathrm{FT.67}(2)]\ \ \textbf{(SIGNED — carries the dressing);}$$
$$\textbf{norm layer:}\ \ \nu_\Gamma(R):=\sum_\sigma|w(R,\sigma)|^2=2^{|R|}\ \ \textbf{(POSITIVE)};\qquad\boxed{\ |(-1)^{\aleph}|^2=1\ \Rightarrow\ \textbf{the dressing DROPS OUT of the norm layer}\ }$$
$$(2)\quad\textbf{THE SECTOR MASS AND THE BINDING ARE NORM-LAYER READS:}\qquad m^2_B(q,S)=\frac{1}{Z^{\mathrm{norm}}_B(q,S)}\sum_{\Gamma,R}\mathcal W^{\mathrm{norm}}_\Gamma(R)\#\mathrm{inst}\cdot\Delta S\ [\mathrm{Def\text{-}H.32}(6)];$$
$$\mathcal W^{\mathrm{norm}}_\Gamma(R)=\nu_\Gamma(R)\,t^{|R|}u^{L(R)}\ \ \text{(positive weights)};\qquad\mathcal B=m^2_B(\cdot,S_j)-\textstyle\sum_im^2_B(\cdot,S_i)\ [\mathrm{BM.21}(2);\ \mathrm{BM.20}(4)]:$$
$$\boxed{\ \textbf{the ensemble binding}\ \mathcal B_{\mathrm{ens}}\ \textbf{is a difference of NORM-layer sector masses — dressing-free by construction}\ }$$
$$(3)\quad\textbf{THE DRESSING CANNOT FLIP THE BINDING SIGN (the directive's crucial question):}\qquad\text{the}\ (-1)^{\aleph}\ \text{dressing and the contact terms}\ c_k\ \text{are AMPLITUDE-layer objects}\ (1);\ \mathcal B_{\mathrm{ens}}\ \text{is norm-layer}\ (2):$$
$$\text{machine: for}\ |R|=3,\ \ \nu_\Gamma=\sum_\sigma|w|^2=8=2^3\ \ \text{under TWO different dressing parities AND undressed (all equal)};\qquad\boxed{\ \text{the static}\ \le0\ \text{verdict}\ [\mathrm{IT.29}(1),(3)]\ \textbf{is PRESERVED under the amplitude consideration}\ }$$
$$(4)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(3);\qquad\textbf{re-produced frozen rows:}\ \mathrm{Def\text{-}H.32}(2),(6),\ \mathrm{FT.67}(2),\ \mathrm{BM.21}(2);\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT2.8 (Parts 1–2); Def-H.32(2),(6), FT.67(2), FT.107(2) (Part 3); IT.29(1),(3) (this level); AT.63(2) (Level 5); BM.20(4), BM.21(2) (Part 4); exact integer sign-assignment sums, `Fraction` arithmetic [math; machine: `amplitude_binding.py` §B, 4/4].

**Pf.**
$$(1):\ |w|^2=|\mathcal J\prod G(e)|^2\,|(-1)^{\aleph}|^2=|\prod G(e)|^2\ \text{since}\ |(-1)^{\aleph}|^2=1;\ \text{at (S1)}\ |G(e)|=|-\sigma_e|=1\Rightarrow\nu_\Gamma=\sum_\sigma1=2^{|R|}\ [\text{machine B1}]$$
$$(2):\ \mathrm{Def\text{-}H.32}(6)\text{'s}\ m^2_B\ \text{uses}\ Z^{\mathrm{norm}},\mathcal W^{\mathrm{norm}};\ \mathrm{BM.21}(2)\text{'s}\ \mathcal B\ \text{is the}\ m^2_B\ \text{difference}\ [\text{machine B2}]$$
$$(3):\ \text{the amplitude layer}\ v_\Gamma\ \text{is signed}\ (2^{|R|}(-1)^{\sum\kappa}),\ \text{the norm layer positive};\ \text{the}\ |R|=3\ \text{witness}\ \nu=8\ \text{under both dressings}\ [\text{machine B1, B3, B4}].\ \blacksquare$$

**Phys.** The whole directive turns on one question — can the flicker dressing, with its rational contact
terms, turn a bound state into an unbound one — and the ledger answers it before any sum is taken, because
it keeps two books. The amplitude book is signed: the dressing lives there, and its cancellations are what
kill the higher windings. The norm book is positive: it is the square modulus of the same weight, and a
sign squares to one, so the dressing simply is not in it. The binding is defined from the norm book — a
difference of sector masses, each a positive-weighted average — which makes the binding dressing-free as a
matter of definition. The machine confirms it the only honest way, by summing the norm weight over every
sign assignment of a three-edge pattern under two opposite dressings and getting the same eight both times.
So the dressing cannot flip the binding, and the negative verdict the static reads gave stands untouched by
the amplitude layer that was supposed to threaten it.

---

### IT.35 — The amplitude machinery scoped, the conflations refuted, the transit obstruction level-local

**Thm.**
$$(1)\quad\textbf{THE DRESSED RESOLVENT (re-derived) AND ITS SCOPE:}\qquad R_k(z)=c_k+\sum_{d\in\{k,k-2,\dots\}>0}\frac{a_{k,d}}{1-d^2z},\quad a_{k,d}=2^{1-k}\binom{k}{(k+d)/2},\quad c_k=2^{-k}\binom{k}{k/2}\ [k\ \text{even}]\ [\mathrm{AT.44}(1);\ \mathrm{AT.52}(1)]:$$
$$\text{the sum rule}\ c_k+\sum_da_{k,d}=1\ \ (k{=}1..8);\qquad\textbf{the contact terms}\ c_k=\bigl(\tfrac12,\tfrac38,\tfrac5{16},\tfrac{35}{128},\tfrac{63}{256}\bigr)\ \ \text{at}\ k{=}(2,4,6,8,10),\ 0\ \text{at odd}\ k\ [\mathrm{AT.52}(2)];$$
$$\boxed{\ R_k\ \textbf{is the}\ k\textbf{-channel TWO-BODY resolvent of the lepton--baryon composite},\ k=\text{the pair/channel count}\ [\mathrm{BM.137}(1);\ \mathrm{AT.54}\ \mathrm{Rmk}],\ \neg\text{the attachment count}\ N\ }\quad\text{so the}\ c_k\ \text{are amplitude-layer, two-body}$$
$$(2)\quad\textbf{THE REGISTER CONFLATION REFUTED (Step 1):}\qquad\text{``map each grouping sector to its}\ (q,S)\text{'' / ``sum the dressed weights over the}\ g(N)\ \text{sectors'' conflate two independent registers}:$$
$$\text{the COLOUR grouping}\ g(N)\ \text{is independent of the edge signs}\ [\mathrm{AT.41}(3)]\ \text{and is a}\ 0/1\ \text{gate}\ [\mathrm{Def\text{-}BM.9}(2),(5)];\qquad\text{the amplitude is}\ (q,S)\text{-sectored over the CONFIGURATION space}\ [\mathrm{Def\text{-}H.32}(5)];$$
$$\boxed{\ \text{the}\ g(N)\ \text{groupings carry}\ \neg(q,S)\ \text{labels}\ \Rightarrow\ \text{the requested sum has no referent}\ }\qquad[\mathrm{IT.26}(1)\ \text{re-confirmed}]$$
$$(3)\quad\textbf{THE DRESSING SCOPE (Step 1):}\qquad(-1)^{\aleph}=(-1)^{|q|}\ \ \text{holds for SINGLE OPEN CHAINS}\ [\mathrm{AT.53}(5)];\ \ \text{closed chains}\to+1,\ \ \text{covers}\to\prod_e\sigma_e:$$
$$\text{a multi-seal composite is}\ \neg\text{a single open chain, so the sector-locked}\ (-1)^{|q|}\ \text{form does not apply wholesale — and the dressing is amplitude-layer}\ [\mathrm{IT.34}],\ \neg\text{in the binding}$$
$$(4)\quad\textbf{NO DISSOCIATION CHANNEL; THE TRANSIT ABSENCE IS LEVEL-LOCAL:}\qquad\neg\exists\ \text{a formed transit-quantum supply vertex, on FOUR independent grounds}\ [\mathrm{BM.122}(6)(\mathrm O1)\text{--}(\mathrm O4)]:$$
$$(\mathrm O1)\ \neg\text{a gauged chiral coupling};\ (\mathrm O2)\ \text{the transit alternative is deficit}\ 1'\ [\mathrm{FT.125}(4)];\ (\mathrm O3)\ \neg\text{a momentum-space resolvent}\ [\mathrm{BM.6}(6)];\ (\mathrm O4)\ \neg\text{a winding carrier}\ [\mathrm{D3.7}];$$
$$\therefore\ \text{``the pair channel's amplitude is}\ \neg\text{formed''}\ [\mathrm{IT.1}(6);\ \mathrm{IT\text{-}O1}];\qquad\boxed{\ \textbf{level-local,}\ \neg\textbf{structural impossibility:}\ \text{``}\neg\exists\ \text{in the inventory'' is an absence a future construction could fill}\ [\text{alignment order 2}]\ }$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(4);\qquad\textbf{re-produced frozen rows:}\ \mathrm{AT.52}(1),(2),\ \mathrm{AT.53}(5),\ \mathrm{BM.122}(6);\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, D3.7, FT.125(4) (Parts 1–2); Def-H.32(2),(5), FT.67(2), FT.106(3), FT.107(2) (Part 3); IT.1(6), IT.26(1), IT.34, IT-O1 (this level); AT.41(3), AT.44(1), AT.52(1),(2), AT.53(5), AT.54, AT.63(2) (Level 5); BM.6(6), BM.122(6), BM.137(1), Def-BM.9(2),(5) (Part 4); exact `Fraction` residues and sum rules [math; machine: `amplitude_binding.py` §§A, C–D, 8/8].

**Pf.**
$$(1):\ a_{k,d},c_k\ \text{by the closed forms; the sum rule}{=}1\ \text{for}\ k{=}1..8;\ c_k\ \text{at even}\ k,\ 0\ \text{at odd};\ \text{the two-body scope re-cited}\ [\text{machine A1, A2, A3}]$$
$$(2):\ \text{the register rows re-cited}\ [\mathrm{AT.41}(3);\ \mathrm{Def\text{-}BM.9}(2),(5);\ \mathrm{Def\text{-}H.32}(5)]\ [\text{machine D1}];\qquad(3):\ \mathrm{AT.53}(5)\text{'s scope re-cited}\ [\text{machine D2}]$$
$$(4):\ \text{the four grounds re-cited from}\ \mathrm{BM.122}(6);\ \text{the level-local status per the alignment discipline}\ [\text{machine C2, D3}];\qquad\text{the constructed bindings}\ \le0\ [\mathrm{BM.21}(4);\ \mathrm{BM.137}(3)\ \text{re-derived}]\ [\text{machine C1}].\ \blacksquare$$

**Phys.** With the sign question settled by the layer separation, this tier cleans up the machinery the
directive leaned on and says plainly what each piece is. The resolvent and its contact terms are real and
exact, but they belong to the two-body lepton-baryon problem and are indexed by a channel count, not by the
attachment count of a nucleus, so they are not the multi-nucleon binding's inputs. The instruction to sum
dressed weights over the grouping sectors asks the colour register to carry amplitude labels it does not
have — the grouping is independent of the signs and acts only as a gate. And the dissociation the directive
worries about has no leg to travel: the inventory refutes a transit supply vertex on four separate grounds.
That absence is firm but it is local to this inventory, not a theorem that no such leg could ever be built,
and the tier records the difference rather than promoting a gap into a permanent bar.

---

### IT.36 — The verdict: IT-O2's sign resolved and its value open; IT-O1 open; the third scenario

**Thm.**
$$(1)\quad\textbf{IT-O2 — THE SIGN VERDICT RESOLVES, THE VALUE STAYS OPEN:}\qquad\boxed{\ \text{the amplitude dressing CANNOT flip the binding}\ [\mathrm{IT.34}(3)];\ \ \text{every constructed norm-layer binding is}\ \le0\ [\mathrm{BM.21}(4);\ \mathrm{BM.137}(3)];\ \ \neg\text{a dissociation channel is formable}\ [\mathrm{BM.122}(6)]\ }$$
$$\therefore\ \text{the static}\ \le0\ \text{verdict}\ [\mathrm{IT.29}]\ \textbf{is PRESERVED — the amplitude side unlocks nothing};\qquad\textbf{BUT the multi-nucleon binding VALUE is}\ \neg\textbf{computed:}$$
$$\text{the composed-support NORM-layer configuration space is beyond the frozen}\ B{=}4\ \text{census}\ [\mathrm{FT.106}(3)],\ \text{and the multi-junction binding FUNCTIONAL is undefined}\ [\mathrm{BM.21}\ \text{is 3-constituent},\ \mathrm{BM.137}\ \text{is two-chain}]\ \Rightarrow\ \mathrm{IT\text{-}O2}\ \text{'s value stays open}$$
$$(2)\quad\textbf{IT-O1 — OPEN (}\neg\textbf{closed):}\qquad\text{the transit leg is}\ \neg\text{formed}\ [\mathrm{BM.122}(6)],\ \text{so the empirical isotope cutoff / dissociation is unformable in the CURRENT inventory — but this is LEVEL-LOCAL}\ [\mathrm{IT.35}(4)],\ \neg\text{a structural impossibility}:$$
$$\text{the contact terms}\ c_k\ \text{(amplitude-layer, two-body) do}\ \neg\text{bear on the transit-leg formation}\ [\mathrm{IT.35}(1)];\qquad\boxed{\ \mathrm{IT\text{-}O1}\ \textbf{remains the open dynamical row; the empirical cutoff stays dynamical}\ [\mathrm{IT.30}(2)]\ }$$
$$(3)\quad\textbf{NEITHER SCENARIO A NOR B — THE THIRD SCENARIO (the premise corrections):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{Scenario A: ``close IT-O2 and IT-O1; transit structurally impossible''}&\textbf{OVER-REACHES}\ [\mathrm{IT.36}(1),(2)]:\ \mathrm{IT\text{-}O2}\text{'s VALUE is}\ \neg\text{computed};\ \mathrm{IT\text{-}O1}\text{'s absence is level-local},\ \neg\text{impossible (order 2)}\\\text{Scenario B: ``the binding is positive''}&\textbf{MIS-FRAMES}\ [\mathrm{IT.34}(3)]:\ \text{the binding is norm-layer, dressing-free; the dressing cannot make it positive}\\\text{``sum the dressed weights over the}\ g(N)\ \text{sectors''}&\textbf{ILL-POSED}\ [\mathrm{IT.35}(2)]:\ \text{the colour grouping carries}\ \neg(q,S);\ \text{the amplitude is configuration-sectored}\\\text{``}\ R_k\ \text{for the}\ N{=}5,6\ \text{grammars};\ \text{contact terms forbid the transit leg''}&\textbf{MIS-INDEXED / CATEGORY ERROR}\ [\mathrm{IT.35}(1),(4)]:\ R_k\ \text{is two-body channel-indexed};\ c_k\ \neg\text{related to the transit absence}\end{array}$$
$$(4)\quad\textbf{THE VERDICT:}\qquad\boxed{\ \textbf{the amplitude side PRESERVES the bound}\ (\le0)\ \textbf{verdict and unlocks NO dissociation channel; IT-O2's sign closes, its value stays open; IT-O1 stays open (level-local)}\ }$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5),\ \mathrm{CT3.22},\ \mathrm{FT.55}(1),\ \mathrm{BM.143}(1)$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{amplitude\_binding.py}\to\textbf{16/16 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{12 checkers, 187 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{11 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, CT3.22, FT.55(1) (Parts 1–2); Def-H.32(6), FT.106(3) (Part 3); IT.1(8), IT.29, IT.30(2), IT.34, IT.35, IT-O1, IT-O2, IT-O5 (this level); AT.39(8), AT.63(2) (Level 5); Def-BM.3(1),(7), BM.21(4), BM.30(5), BM.83, BM.122(6), BM.134(5), BM.137(3), BM.143(1) (Part 4); the assembly rows [math; machine: `amplitude_binding.py` §E, 4/4].

**Pf.**
$$(1):\ \mathrm{IT.34}(3)\ \text{(the layer separation)},\ \mathrm{IT.35}\ \text{'s}\ \le0\ \text{census},\ \mathrm{BM.122}(6)\ \text{(no channel)};\ \text{the value-residue from}\ \mathrm{FT.106}(3)\ \text{and the undefined functional}\ [\text{machine E1}]$$
$$(2):\ \mathrm{IT.35}(4)\ \text{'s level-local row};\ \text{the contact-term irrelevance}\ [\mathrm{IT.35}(1)]\ [\text{machine E2}];\qquad(3):\ \text{the scenario table verified against}\ \mathrm{IT.34}\text{--}\mathrm{IT.35}\ [\text{machine E3}]$$
$$(4)\text{--}(7):\ \text{the verdict, the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (5)\text{--}(7).\ \blacksquare$$

**Phys.** The directive asked the amplitude layer to decide whether the isotopes hold together, and the
answer is that the amplitude layer never had the vote. The binding is read from the norm book, where signs
have squared away, so no dressing and no contact term can move it; the static picture said bound and the
amplitude picture cannot say otherwise. What the amplitude computation would have needed — the full
configuration space of a several-nucleon support and a binding functional for several nucleons rather than
one — is still not built, so the number remains open even though its sign is settled. And the decay the
directive hoped to forbid or to force is simply not in the inventory: there is no transit leg, on four
grounds, and that absence is a fact about this ledger, not a law against ever building one. So neither of
the two offered endings is the right one. The honest ending is quieter and firmer: the bound verdict stands,
the dissociation channel does not exist, the magnitude waits, and the transit question stays open exactly
where the level's discipline requires it to stay. Nothing measured entered; nothing was declared; no isotope
was identified.

---

## §Cal-IT — unchanged from Tier IT.11

**Empty at this tier.** No parameter is added; the binding value is recorded as an open residue, not a
parameter. The parametric residues remain the open rows and the inherited owed declarations — the mass-read
route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1), $\varepsilon_q$ (AT-O27), $e_0$ (EM.25(7), ¬issued),
$(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$, $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4
transport profile, the lift and the vielbein (AT.60), and the read rules (M1′)–(M3′) [AT.54(6)].

## §Open-IT additions from Tier IT.11

| row | content | locus |
|---|---|---|
| **IT-O2 — SIGN resolved, VALUE open** | the ensemble binding is norm-layer and **dressing-free** [IT.34], so the amplitude dressing **cannot flip** the static ≤0 [IT.29]; every constructed binding ≤0; no dissociation channel [BM.122(6)]. **The VALUE stays open**: the composed-support norm-layer configuration space beyond the frozen B=4 census [FT.106(3)] + the undefined multi-junction binding functional (BM.21 is 3-constituent, BM.137 two-chain) | IT.36(1); IT.34; IT.35(1) |
| **IT-O1 — OPEN (level-local)** | the transit/dissociation leg is ¬formed [BM.122(6)(O1)–(O4)] — a **level-local** inventory absence, ¬a structural impossibility (alignment order 2); the contact terms c_k do not bear on it. The empirical isotope cutoff stays dynamical [IT.30(2)] | IT.36(2); IT.35(4) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27; IT.30;
IT.33]: (IT-O3) the handshake-indicator operational theory, (IT-O5) the isotope cutoff (static side closed
[IT.30(1)]), the owed mass-read route choice [IT.14(3)], the deferred Calibration Era [IT.33(2); AT.63(4)],
and the Level-5 ledger [AT.63(3),(5)]. **IT-O4 stays CLOSED** [IT.21(1)].

---

# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Isotopic era** — Tier IT.12: the mass-matrix object — exact Pauli/tensor algebra, and the redundancy-and-parameter adjudication

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.12 — the Architect's directive to formalize a 2×2
Hermitian "mass matrix" on the orientation doublet, compute its tensor product, map the 16 components onto
the force basis, and identify new content or redundancy. The tier verifies the exact linear algebra and
adjudicates the object as **redundant + parametric** — constructible, but adding no new derived content.
**Tags.** IT.37–IT.39. **Pattern.** the adjudication tiers (IT.9/IT.10/IT.11's shape), premise audit logged
in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays empty; no
clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.4–IT.11 is modified [AT.63(2)]. **The mass
matrix is recorded as a PARAMETRIC CONSTRUCTION CLASS, not a derived row, and is NOT adopted.**
**Machine.** `era2/level6_isotopic/checks/mass_matrix.py` → **13/13 exact** (Gauss(i) over `Fraction`: the
Hermiticity, the Pauli decomposition, the characteristic polynomial, and the 16-component tensor trace by
explicit 4×4 multiplication); `run_all_level6.py` → **13 checkers, 200 exact markers, 0 failures**;
`check_level6_format.py` → the gate over all twelve Part 6 documents. Exact arithmetic: `Fraction` Gauss(i)
matrices, integer binomials, no floating point.
**No floating point in any assertion. No measured value enters any clause [P5] — $m_L,m_S,m_{\mathrm{off}}$
are ledger-native reads/slots, NOT Standard-Model masses; $\Delta\theta$ is structural and unmeasured; no
calibration value is issued. No species identification [Def-BM.3(1),(7)]. No smooth-manifold or QFT
mass-matrix import — the object is built as an operator on the ledger's own $H_\omega$ [Def-H.33].**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only.
**Mandate.** The Architect's directive (session 13h): *"Formalize the Mass Matrix Object … a 2×2 Hermitian
matrix with the Lyapunov mass and the rung-1 seal mass on the diagonal, and the off-diagonal coupling
carrying complex phases … tensored with itself, 16 components map onto the C²⊗C² force decomposition
(AT.59) … identify new content or redundancy. If redundant, state that honestly. If it conflicts with
existing bars, state the exact tension."* Executed: the algebra verified exact, the object adjudicated
**redundant with BM.22/AT.56–58 and parametric in two undeclared slots**; four premise corrections at
IT.39(3).

---

### IT.37 — The mass matrix on $H_\omega$: Hermiticity, the Pauli decomposition, the eigenvalues

**Thm.**
$$(1)\quad\textbf{THE OBJECT (a parametric construction class on}\ H_\omega\textbf{):}\qquad M=\begin{pmatrix}m_L & w\\ \bar w & m_S\end{pmatrix},\quad w=m_{\mathrm{off}}e^{i\Delta\theta}=a+bi\in\mathbb Z[i]\otimes\mathbb Q,\quad H_\omega=\mathbb C^2\ [\mathrm{Def\text{-}H.33}]:$$
$$m_L=\text{the informational (``Lyapunov'') mass},\ \ m_S=\text{the rung-1 seal mass},\ \ \text{BOTH}\ m=E_{\mathrm{int}}\ln2/\mathfrak h\ [\mathrm{FT.44}(4);\ \text{the rung-one seal}\ E_{\mathrm{int}}{=}2\Rightarrow m_S{=}2\ln2/\mathfrak h];$$
$$\boxed{\ M=M^\dagger\ \ \text{for real}\ m_L,m_S\ \text{and conjugate off-diagonals}\ w,\bar w\ }\qquad[\text{machine: 4 Gauss(i) witnesses}]$$
$$(2)\quad\textbf{THE PAULI DECOMPOSITION}\ v_\mu=\mathrm{Tr}(M\sigma_\mu)\ \textbf{(the directive's four identities, verified exactly):}\qquad\boxed{\ v_0=m_L{+}m_S,\quad v_3=m_L{-}m_S,\quad v_1=2a=2m_{\mathrm{off}}\cos\Delta\theta,\quad v_2=-2b=-2m_{\mathrm{off}}\sin\Delta\theta\ }$$
$$\text{all four}\ v_\mu\ \text{are REAL}\ (M\ \text{Hermitian});\qquad M=\tfrac12\sum_\mu v_\mu\sigma_\mu\ \ [\text{machine: exact over Gauss(i)}]$$
$$(3)\quad\textbf{THE EIGENVALUES (exact):}\qquad\det(M-\lambda I)=\lambda^2-(m_L{+}m_S)\lambda+(m_Lm_S-|w|^2),\quad|w|^2=m_{\mathrm{off}}^2=a^2{+}b^2:$$
$$\boxed{\ \lambda_\pm=\tfrac12\bigl[(m_L{+}m_S)\pm\sqrt{(m_L{-}m_S)^2+4m_{\mathrm{off}}^2}\bigr]\ }\qquad\text{the discriminant}\ (m_L{-}m_S)^2{+}4m_{\mathrm{off}}^2\ge0\ \ \text{(real spectrum,}\ M\ \text{Hermitian)}$$
$$(4)\quad\textbf{THE DIAGONAL IS COMMENSURABLE (no BM.83 mix):}\qquad m_L,m_S\ \text{are both informational reads}\ E_{\mathrm{int}}\ln2/\mathfrak h\ [\mathrm{FT.44}(4)]\ \Rightarrow\ \text{the SAME currency};\ \ \neg\text{a cross-currency mass sum}\ [\mathrm{BM.83}]$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived (the algebra):}\ (1)\text{--}(4);\qquad\textbf{parametric,}\ \neg\textbf{derived:}\ \text{the slots}\ m_{\mathrm{off}},\Delta\theta\ [\mathrm{IT.39}(2)];\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, D2.9 (Parts 1–2); Def-H.33, FT.22, FT.44(4) (Part 3); IT.31(4) (this level); AT.63(2) (Level 5); Def-BM.3(1),(7), BM.83, BM.131 (Part 4); exact Gauss(i) matrix algebra over `Fraction`, the characteristic polynomial, integer discriminant census [math; machine: `mass_matrix.py` §A, 4/4].

**Pf.**
$$(1):\ M^\dagger=[[m_L,\bar w],[w,m_S]]=M\ \text{entrywise on 4 witnesses}\ [\text{machine A1}];\qquad(2):\ v_\mu=\mathrm{Tr}(M\sigma_\mu)\ \text{computed over Gauss(i):}\ v_0{=}m_L{+}m_S,\ v_1{=}w{+}\bar w{=}2a,\ v_2{=}i(w{-}\bar w){=}{-}2b,\ v_3{=}m_L{-}m_S\ [\text{machine A2, A2x}]$$
$$(3):\ \det(M{-}\lambda I){=}(m_L{-}\lambda)(m_S{-}\lambda){-}|w|^2;\ \text{the quadratic formula};\ \text{the discriminant}\ \ge0\ [\text{machine A3}];\qquad(4):\ \text{the}\ E_{\mathrm{int}}\ln2/\mathfrak h\ \text{form re-cited for both}\ [\mathrm{FT.44}(4)].\ \blacksquare$$

**Phys.** As a piece of exact linear algebra the object is unimpeachable, and the tier verifies every identity
the directive asked for: a two-by-two Hermitian operator on the orientation doublet, its four Pauli
coefficients the total mass, the splitting, and the cosine and sine couplings, its two eigenvalues the
familiar half-sum plus-or-minus half the reduced discriminant. The diagonal is honest — both entries are the
same kind of informational mass, six-over-h and two-over-h, so no incommensurable currency is being added.
What the algebra cannot settle is where the off-diagonal comes from: the coupling magnitude and its phase are
not reads the ledger derives, and the tier says so plainly rather than dressing a free parameter as a
prediction. The matrix is a clean construction; whether it is a new object is the next tag's question.

---

### IT.38 — The tensor product, the 16-vs-8 over-count, and the redundancy with the existing force matrix

**Thm.**
$$(1)\quad\textbf{THE TENSOR PRODUCT factorizes exactly:}\qquad C_{\mu\nu}:=\mathrm{Tr}\bigl((M\otimes M)(\sigma_\mu\otimes\sigma_\nu)\bigr)=\mathrm{Tr}(M\sigma_\mu)\,\mathrm{Tr}(M\sigma_\nu)=v_\mu v_\nu\qquad[\text{machine: all 16 by explicit}\ 4\times4\ \text{multiplication}]:$$
$$C_{00}=(m_L{+}m_S)^2,\quad C_{33}=(m_L{-}m_S)^2,\quad C_{11}{+}C_{22}=4m_{\mathrm{off}}^2,\quad C_{03}=m_L^2{-}m_S^2,\quad C_{12}=-2m_{\mathrm{off}}^2\sin2\Delta\theta$$
$$(2)\quad\textbf{THE 16-vs-8 OVER-COUNT (premise P3):}\qquad\text{the}\ 16\ \sigma_\mu\otimes\sigma_\nu\ \text{span the full}\ \dim\mathrm{End}(\mathbb C^4)=16,\ \ \text{but the DERIVED force algebra is}\ \textbf{8-dimensional}:$$
$$\mathrm{span}\{I_4,\ \sigma_i\otimes I_2\ (3),\ \sigma_i\otimes\hat\kappa\ (3),\ I\otimes\hat\kappa\}=1{+}3{+}3{+}1=8,\qquad\textbf{``zero new operators''}\ [\mathrm{AT.56}];$$
$$\boxed{\ 8\ \text{of the}\ 16\ \text{components lie OUTSIDE the derived force algebra}\ \Rightarrow\ \text{``16 map onto the force basis'' over-counts by 8; the}\ C_{\mu\nu}\to\text{force identifications are STIPULATIONS,}\ \neg\text{derived rows}\ }$$
$$(3)\quad\textbf{REDUNDANCY (premise P2):}\qquad M\ \text{is the SAME SPECIES as BM.22's static force matrix}\ \ F_{\mathrm{ext}}(\mathbf c,q)=h(\mathbf c)\otimes I_2+q\,I_2\otimes\hat\kappa\ [\mathrm{BM.22}(1),(2),(4)]:$$
$$\text{a Hermitian operator on the 2-dim carrier with a diagonal}\ (h)\ \text{and an off-diagonal flipping block}\ (q\hat\kappa,\ \text{splitting}\ 2|q|);\qquad\boxed{\ M\ \text{replaces the DERIVED charge read}\ q\ \text{with the UNDECLARED}\ m_{\mathrm{off}}e^{i\Delta\theta}\ }$$
$$\text{the Pauli decomposition and the tensor product are AT.56--AT.58's Pauli anatomy}\ (\sigma^{\mu\nu}=-2\varepsilon_{abc}W_c^{\mathrm{ext}}\ \text{magnetic},\ \sigma^{a4}=(\sigma_a\otimes I_2)\gamma_{F_0}\ \text{electric});\quad M\ \text{repackages,}\ \neg\text{extends}$$
$$(4)\quad\textbf{status:}\qquad\textbf{derived (the algebra):}\ (1);\qquad\textbf{adjudicated:}\ (2),(3);\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT0.12 (Parts 1–2); Def-H.32(2), Def-H.33 (Part 3); IT.37 (this level); AT.48, AT.56, AT.57, AT.58, AT.59, AT.63(2) (Level 5); BM.22(1),(2),(4) (Part 4); exact Gauss(i) 4×4 Kronecker multiplication and trace, integer dimension arithmetic [math; machine: `mass_matrix.py` §§B–C, 6/6].

**Pf.**
$$(1):\ \mathrm{Tr}((M{\otimes}M)(\sigma_\mu{\otimes}\sigma_\nu))=\mathrm{Tr}(M\sigma_\mu)\mathrm{Tr}(M\sigma_\nu)\ \text{by the tensor-trace identity, verified entrywise on all 16 by explicit}\ 4{\times}4\ \text{products}\ [\text{machine B1, B2}]$$
$$(2):\ 1{+}3{+}3{+}1{=}8\ \text{vs}\ 16;\ \text{the}\ 8\ \text{outside the algebra}\ [\mathrm{AT.56}\ \text{'s}\ \textbf{span row re-cited}]\ [\text{machine B3}];\qquad(3):\ \text{the}\ F_{\mathrm{ext}}\ \text{structure re-cited from}\ \mathrm{BM.22};\ \text{the species match}\ [\text{machine C1}].\ \blacksquare$$

**Phys.** Tensor the matrix with itself and the sixteen numbers that come out are just the products of the four
it started with — an exact factorization the machine confirms by multiplying four-by-fours, not by assertion.
But sixteen is the wrong count for forces. The corpus already proved that the operators its forces actually
use span eight dimensions and that the Clifford construction yields no ninth, so half of these components sit
outside anything the ledger calls a force, and naming them curvature lock or Hodge rotation or CP mixing is a
choice, not a theorem. And the matrix itself is not new: the era already wrote down a Hermitian operator on
this same two-dimensional carrier with a diagonal and an off-diagonal flipping block, except there the
off-diagonal was the derived charge and the splitting was exactly two. Substitute an undeclared coupling and
phase for that charge and you have this object — the same species, with a parameter where a read used to be.

---

### IT.39 — The adjudication: redundant and parametric; the over-claims refuted; nothing adopted

**Thm.**
$$(1)\quad\textbf{THE UNDECLARED SLOTS (the exact tension, premise P1):}\qquad m_{\mathrm{off}},\ \Delta\theta\ \ \textbf{are}\ \neg\textbf{derived reads}:$$
$$\Delta\theta\ \neg=\ \text{the winding}\ \Theta(c)\ ([\Theta]=\mathfrak q\ [\mathrm{FT.22}])\ \ \text{and}\ \ \neg=\ \text{the defect angle}\ \Theta_R\ ([\Theta_R]=\mathfrak q^0\ [\mathrm{FT.54}(1)]):\ \ \text{``the two angles are kept apart,}\ \neg\text{proportional on a dimension count''};$$
$$\boxed{\ \text{introducing}\ m_{\mathrm{off}},\Delta\theta\ \text{as free parameters is a P4-class addition requiring a LOGGED DECLARATION}\ [\mathrm{BM.6}(4)\ \text{precedent}]\ \text{— NONE issued}\ \Rightarrow\ M\ \text{is a PARAMETRIC construction class,}\ \neg\text{a derived row}\ }$$
$$(2)\quad\textbf{THE OVER-CLAIMS REFUTED (premise P4):}\qquad\begin{array}{l|l}\textbf{the claim}&\textbf{the derived row}\\\hline\text{``a unified origin for the forces''}&\textbf{REFUTED}:\ \text{the forces are derived separately (the rung activation}\ [\mathrm{AT.50}];\ \text{the Pauli anatomy}\ [\mathrm{AT.56}\text{--}\mathrm{AT.58}]);\ M\ \text{repackages},\ \neg\text{unifies}\\\text{``explains the BEC statistics (4Z vs 2Z)''}&\textbf{REFUTED}:\ \text{the statistics is the multiplicative exchange}\ \varepsilon=(-1)^A\ [\mathrm{BM.128}(7);\ \mathrm{IT.31}(4)],\ \text{a WINDING-PARITY read},\ \neg\text{a mass-matrix eigenvalue}\\\text{``connects to the calibration anchor (IT.10)''}&\textbf{TRIVIAL ONLY}:\ \text{both involve mass reads};\ \neg\text{a new structural link}\end{array}$$
$$(3)\quad\textbf{THE VERDICT:}\qquad\boxed{\ \textbf{M is CONSTRUCTIBLE and its algebra EXACT, but it ADDS NO NEW DERIVED CONTENT — REDUNDANT}\ [\mathrm{IT.38}(3)]\ \textbf{+ PARAMETRIC}\ [\mathrm{IT.39}(1)],\ \textbf{and its force map over-counts}\ [\mathrm{IT.38}(2)]\ }$$
$$\text{it is consistent with the corpus only as a parametric construction class whose derived content already exists}\ (\mathrm{BM.22},\ \mathrm{AT.56}\text{--}\mathrm{AT.58});\qquad\textbf{recorded honestly,}\ \neg\textbf{adopted},\ \neg\textbf{a declaration}$$
$$(4)\quad\textbf{the premise corrections:}\qquad\textbf{(P1)}\ m_{\mathrm{off}},\Delta\theta\ \text{undeclared}\ (1);\ \ \textbf{(P2)}\ M\ \text{redundant with}\ \mathrm{BM.22}\ [\mathrm{IT.38}(3)];\ \ \textbf{(P3)}\ \text{the 16-component force map over-counts the 8-dim algebra}\ [\mathrm{IT.38}(2)];\ \ \textbf{(P4)}\ \text{the unification/BEC claims refuted}\ (2)$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition adopted},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))],\ \neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\quad§\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{prices}\ \neg\text{masses, no currency mixing}),\ \mathrm{CT3.22},\ \mathrm{FT.55}(1);\qquad M\ \text{is}\ \neg\text{adopted into the force basis}$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{mass\_matrix.py}\to\textbf{13/13 exact};\quad\texttt{run\_all\_level6.py}\to\textbf{13 checkers, 200 exact markers, 0 failures};\quad\texttt{check\_level6\_format.py}\to\textbf{12 Part 6 documents PASS};\quad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no new object is adopted}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, CT3.22, FT.55(1) (Parts 1–2); Def-H.33, FT.22, FT.54(1) (Part 3); IT.10, IT.31(4), IT.37, IT.38 (this level); AT.39(8), AT.50, AT.56, AT.57, AT.58, AT.63(2) (Level 5); Def-BM.3(1),(7), BM.6(4), BM.22, BM.30(5), BM.83, BM.128(7), BM.131, BM.134(5) (Part 4); the assembly rows [math; machine: `mass_matrix.py` §D, 3/3].

**Pf.**
$$(1):\ \text{the two-angles row re-cited}\ [\mathrm{FT.22};\ \mathrm{FT.54}(1)];\ \text{the P4/declaration discipline}\ [\mathrm{BM.6}(4)]\ [\text{machine C2}];\qquad(2):\ \text{the force-derivation and exchange-statistics rows re-cited}\ [\mathrm{AT.50};\ \mathrm{AT.56}\text{--}\mathrm{AT.58};\ \mathrm{BM.128}(7);\ \mathrm{IT.31}(4)]\ [\text{machine D1}]$$
$$(3)\text{--}(7):\ \text{the verdict assembled from}\ \mathrm{IT.38}(2),(3)\ \text{and}\ (1);\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (5)\text{--}(7).\ \blacksquare$$

**Phys.** The verdict is the one the directive explicitly invited, and it is a negative that costs nothing to
state. The mass matrix is exact algebra and the corpus is happy to hold it as a construction class — but
every piece of physical content it was hoped to carry is already elsewhere or nowhere. Its diagonal is two
informational masses the era already reads; its off-diagonal is a coupling and a phase the era does not
derive, and calling a free parameter structural does not make it derived; its tensor square produces sixteen
numbers where the forces live in eight; and its shape is the shape of a force matrix the baryon era wrote down
with a derived charge where this has an undeclared one. It does not unify the forces, which were built one
rung at a time, and it does not explain why helium-four condenses, which is a parity of nucleon count and not
an eigenvalue. So the tier records the object, proves its algebra, names its two undeclared slots and its
eight-component excess, and adopts none of it — the honest disposition of a clean idea that the ledger
already contains.

---

## §Cal-IT — unchanged from Tier IT.12

**Empty at this tier.** The mass matrix is a parametric construction class; its two off-diagonal slots
($m_{\mathrm{off}},\Delta\theta$) are recorded as **undeclared**, NOT added as parameters — adopting them would
be a P4-class declaration [BM.6(4)], and none is issued. The parametric residues remain the open rows and the
inherited owed declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1),
$\varepsilon_q$ (AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$,
$\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile, the lift and the vielbein
(AT.60), and the read rules (M1′)–(M3′) [AT.54(6)].

## §Open-IT additions from Tier IT.12

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.12 opens **no new row**: the mass matrix is recorded as a **parametric construction class** (redundant with BM.22 + AT.56–58; two undeclared slots $m_{\mathrm{off}},\Delta\theta$; the 16-component force map over-counts the 8-dim algebra). It is **not adopted**. If the Architect ever wants it as a derived object, the two slots require a logged declaration [BM.6(4)] and the force map must be restricted to AT.56's 8-dim algebra | IT.39(1),(3),(5) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27; IT.30;
IT.33; IT.36]: (IT-O1) the transit/dissociation dynamics, (IT-O2) the multi-nucleon binding value (the sign
resolved dressing-invariant ≤0 [IT.34]), (IT-O3) the handshake-indicator operational theory, (IT-O5) the
isotope cutoff (static side closed [IT.30(1)]), the owed mass-read route choice [IT.14(3)], the deferred
Calibration Era [IT.33(2); AT.63(4)], and the Level-5 ledger [AT.63(3),(5)]. **IT-O4 stays CLOSED** [IT.21(1)].

---

# Part 6, Tier IT.13 — IT-O1 Re-Examined: the Four Grounds Against the New Machinery

**Locus.** The Architect's directive (session 13i): re-examine IT-O1 (the transit-leg amplitude) — barred
since the baryomesonic era by BM.122(6)'s four grounds — against the machinery built since (the Pauli
anatomy AT.56–58, the dressed resolvent AT.52–54, the polygon holonomy AT.46, the global Dirac operator
AT.60, the fine-structure grammar AT.61, the isotopic census IT.6–IT.9). Determine whether any ground is
now addressable; if all hold, name the exact missing primitive. Do not force a construction. This tier
applies the level-local no-go discipline (alignment order 2) — every ground re-confirmed against this
level's math, not accepted head-on. Machine: `checks/transit_reexam.py` (11/11 EXACT). Session log:
`discovery/2026-10-13_session_13i_transit_reexam.md`.

### IT.40 — The four grounds re-examined: O3 dissolved, O1/O2/O4 hold (sharpened)

**Thm.**
$$(1)\quad\textbf{O3 (no momentum-space resolvent) — DISSOLVED:}\qquad\mathrm{BM.122}(6)(\mathrm O3)\ \text{[Tier BM.22] is SUPERSEDED by Def-BM.20/BM.134 [Tier BM.23, later, same era], which CONSTRUCTED the momentum-space}\ \Sigma\text{-resolvent}$$
$$\text{the plane-wave boundary states of covariant label}\ p_\mu,\ \text{the pole locus}\ R(z;\mathbf p)^{-1}{=}0\iff g^{\mu\nu}p_\mu p_\nu{=}{-}m^2\ \text{[BM.134(1)], the on-shell measure [BM.134(3)], the two-body phase space}\ p_\ast{=}\tfrac1{2N}\sqrt{z^2{-}4N^2m^2}\ \text{[BM.134(4)]}$$
$$\mathrm{BM.134}(7):\ \text{``the momentum-space}\ \Sigma\text{-resolvent is constructed'', discharging}\ \mathrm{BM.6}(6)\ \text{and closing HistLog item 17}\ \Rightarrow\ \text{O3's literal claim is now FALSE}$$
$$(2)\quad\textbf{O1 (no gauged chiral coupling) — HOLDS, sharpened:}\qquad\text{the gauge blocks are CHIRAL-BLIND,}\ [W_i\otimes I_\omega,\ I\otimes P_{L/R}]{=}0\ \text{(``blindness, not coupling'' [FT.123 Phys])}$$
$$\text{the gauge field is the transport curvature of UNDECLARED slots}\ T_a\ \text{(the P4 transport profile) [AT.57]; the index-carrying VECTOR EM read is}\ \neg\text{formable [AT.48(5v); AT-O29]}\ \Rightarrow\ \neg\exists\ \text{a gauged chiral coupling}$$
$$(3)\quad\textbf{O2 (deficit}\ 1'\textbf{) — HOLDS:}\qquad\text{the chiral matter assignment (which species in which gauge representation on which chiral ray) is}\ \neg\text{derived; it needs a Weyl symbol + a hypercharge-assignment read (only the chiral projector is supplied, F.39/AT.60)}$$
$$\text{the assignment rule is application-layer, its non-derivability PROVEN}\ [\mathrm{FT.81}(4);\ \mathrm{FT.125}(2),(4);\ \mathrm{Def\text{-}BM.3}\ \mathrm{Rmk}]$$
$$(4)\quad\textbf{O4 (no winding carrier) — HOLDS:}\qquad\text{the transit object is the D3.7 trivial chain (photons/gluons, all-null), EXCLUDED from Def-H.38's scope, so}\ \neg\text{a}\ j{=}|k|/2\ \text{read and}\ \neg\text{an}\ \varepsilon\ \text{read attach}$$
$$\mathrm{AT.46}\ \text{(the polygon holonomy) and}\ \mathrm{AT.52}\ \text{(the winding-revival ladder) are for MATERIALIZED bound chains/covers,}\ \neg\text{the all-null trivial chain}$$

**Req.** D3.7, Def-H.38 (Scope), FT.81(4), FT.123 (Phys), FT.125(2),(4) (Part 3); Def-BM.3 (Rmk), BM.6(6), BM.122(6)(O1–O4), BM.134(1),(3),(4),(7), Def-BM.20 (Part 4); AT.46, AT.48(5v), AT.52, AT.56–58, AT.60, AT.61 (Part 5, cited); IT.6–IT.9 (this level, cited); Def-BM.3(1),(7), P4, P5; exact $\mathbb Q(i)$ matrix algebra (the chiral-blindness commutator), exact rational two-body phase space [math; machine: `transit_reexam.py` PART A–C, 7/7].

**Pf.**
$$(1):\ \mathrm{BM.134}(7)\ \text{discharges}\ \mathrm{BM.6}(6)\text{'s three requirements (the plane-wave states, the two-point read,}\ m^2\ \text{as the pole displacement); the CM identity}\ p_\ast^2{=}(z/2)^2{-}m^2\ \text{at}\ N{=}1\ \text{verified exactly [machine B1]; BM.122 (Tier BM.22) predates BM.134 (Tier BM.23) [machine B2]}$$
$$(2):\ \text{the commutator}\ [W_i\otimes I_\omega,\ I\otimes P_{L/R}]{=}0\ \text{verified in}\ 4{\times}4\ \text{Gauss(i)}\ (W_i{=}\sigma_1\ \text{on factor 1,}\ P_{L/R}{=}(\mathrm I\mp\sigma_3)/2\ \text{on factor 2) [machine A1]; the adversarial same-factor}\ [\sigma_1,\sigma_3]{=}{-}2i\sigma_2\neq0\ \text{shows a chiral coupling needs a nonzero commutator [machine A1x]; AT.57's}\ T_a\ \text{undeclared + AT-O29 [machine A2]}$$
$$(3):\ \mathrm{FT.125}(2),(4)\ \text{re-cited (Tier F.39 discharges only the chiral projector;}\ \neg\exists\ \text{an assignment rule in Tiers F.1--F.39) [machine C1]};\qquad(4):\ \mathrm{Def\text{-}H.38}\ \text{Scope re-cited (transit/trivial chains excluded) [machine C2].}\ \blacksquare$$

**Phys.** The new machinery does not dissolve O1/O2/O4 — it SHARPENS them: it proves the gauge blocks are
chiral-blind (not chirally coupled), that the gauge field is undeclared slots, and that the trivial transit
chain is out of Def-H.38's scope. The machinery is about the MATERIALIZED bound structure; the transit leg
is about the RADIATION quantum's gauged chiral coupling — different layers. But O3 IS dissolved: the
momentum-space Σ-resolvent, the plane-wave states, and the two-body phase space now exist (BM.134), a
genuine downstream supersession that IT-O1's four-grounds citation missed.

### IT.41 — The verdict: IT-O1 stays open on three grounds; the missing primitive is deficit 1′

**Thm.**
$$(1)\quad\textbf{IT-O1 STAYS OPEN:}\qquad\text{the transit-leg amplitude is}\ \neg\text{constructed — the two-photon/transit supply vertex now stands barred on THREE grounds (O1, O2, O4), not four (O3 discharged)}$$
$$\text{dissolving O3 supplies the propagator/phase-space machinery but NOT the vertex: the supply vertex needs the gauged chiral COUPLING (O1), the chiral matter ASSIGNMENT (O2), and a winding carrier for the transit quantum (O4) — all three still absent}$$
$$(2)\quad\boxed{\ \textbf{the exact missing primitive:}\quad\text{deficit}\ 1'\ \text{— the chiral matter assignment rule correlating the}\ \hat\chi\text{-grade with the gauge representation and the weak coupling, requiring a WEYL SYMBOL and a HYPERCHARGE-ASSIGNMENT READ}\ }$$
$$\text{[FT.81(4); FT.125(4)]; it is APPLICATION-LAYER / non-derivable at the ledger level [Def-BM.3 Rmk], so IT-O1 is}\ \neg\text{a construction gap the machinery can fill — it needs a DECLARATION, plus O1's declared gauge field (the P4 transport profile) and O4's transit-chain winding carrier}$$

**Req.** IT.40 (this tier); FT.81(4), FT.125(2),(4) (Part 3); Def-BM.3 (Rmk), BM.122(6) (Part 4); AT.57 (Part 5, cited); P4, P5; the four-ground independence of BM.122(6) [math; machine: `transit_reexam.py` PART D, 4/4].

**Pf.**
$$(1):\ \mathrm{BM.122}(6)\ \text{is ``four INDEPENDENT grounds'' — each alone blocks the supply vertex; O3 discharged [IT.40(1)], but O1, O2, O4 each still block [IT.40(2)--(4)]}\ \Rightarrow\ \neg\text{formed on three grounds [machine D1, D2]}$$
$$(2):\ \text{the core primitive is deficit}\ 1'\ \text{(O2), which O1's gauged chiral coupling also requires (a chiral coupling needs the matter's gauge representation), and which}\ \mathrm{FT.125}(4)/\mathrm{Def\text{-}BM.3}\ \mathrm{Rmk}\ \text{prove non-derivable (application-layer) [machine D3]; the construction is}\ \neg\text{forced (the directive's constraint).}\ \blacksquare$$

**Phys.** The transit-leg amplitude (the radiation dynamics behind the empirical isotope cutoff, IT.9/IT.30;
the dissociation leg of IT-O2's value) remains the one genuinely dynamical gap. Its obstruction is now
precisely localized: not a missing resolvent (O3 discharged) but a missing DECLARATION — the chiral matter
assignment (deficit 1′). This is application-layer content, so IT-O1 cannot be closed by further ledger
derivation; it needs the Architect to declare a chiral assignment (a Weyl symbol + a hypercharge read), or
Level 7+ to supply it.

### IT.42 — The premise correction, the status, and the no-declaration discipline

**Thm.**
$$(1)\quad\textbf{premise correction:}\qquad\mathrm{IT.1}(6)/\mathrm{IT.29}(4)/\mathrm{IT.35}(4)\text{'s ``four grounds [BM.122(6)(O1--O4)]'' is STALE on O3 (superseded by BM.134) — corrected to THREE grounds (O1, O2, O4), O3 discharged}$$
$$(2)\quad\textbf{status:}\qquad\text{IT-O1 remains OPEN, sharpened — O3 discharged; the obstruction localized to deficit}\ 1'\ \text{(the chiral matter assignment, application-layer) + O1's undeclared gauge field (the P4 transport profile) + O4's trivial-chain carrier}$$
$$(3)\quad\textbf{discipline:}\qquad\text{declarations issued NONE (the missing primitive is named,}\ \neg\text{invented); no species identified [Def-BM.3(1,(7))]; no measured value [P5]; prices not masses; no currency mixing [BM.83; BM.134(5)]; §Cal-IT empty; Level-5 and IT.1--IT.12 cited, never edited [AT.63(2)]}$$

**Req.** IT.40, IT.41 (this tier); IT.1(6), IT.29(4), IT.35(4) (corrected); BM.122(6), BM.134, Def-BM.3(1),(7) (Part 4); P5; alignment order 2 (the no-go re-examination); alignment order 5 (complete the chain; do not force a construction) [math; machine: `transit_reexam.py` PART D].

**Pf.**
$(1):\ \text{the correction follows from IT.40(1)'s O3 supersession, BM.134}\ \vdash\ \mathrm{BM.122}(6)(\mathrm O3);\qquad(2):\ \text{the status follows from IT.41 (three grounds hold; the missing primitive is deficit}\ 1'\text{) [machine D4]}$
$$(3):\ \text{the no-declaration discipline is the directive's ``do not force a construction'' honored — the missing primitive is NAMED (deficit}\ 1'\text{, application-layer) rather than invented, and no route is selected.}\ \blacksquare$$

**Phys.** The re-examination delivers a real advance without overreach: one of the four grounds (O3) is
genuinely dissolved (a downstream supersession the earlier citation missed), and the remaining obstruction
is localized to a single named primitive (deficit 1′) that is application-layer by proof — so IT-O1 is
honestly a declaration gap, not a construction gap. This is the correct posture: the level-local no-go
discipline found a real supersession, sharpened the rest, and did not force a transit amplitude the ledger
cannot supply.

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.14: the cross-currency matrix object — the exact tensor/S-T algebra, the seatless derivative asymmetry, and the Scenario-B adjudication

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.14 — the Architect's directive to audit a
2×2 matrix whose off-diagonal entries are the two undeclared currency slots ($\rho_{\mathrm B}$
baryon/pole, $\varepsilon_q$ lepton/flicker), its tensor product, its symmetric/antisymmetric (S-T)
decomposition, and the claimed photon/observer derivative asymmetry — and to adjudicate new
structure (Scenario A) against redundancy (Scenario B). The tier verifies the exact linear algebra,
refutes three of the directive's structural claims on existing rows, and adjudicates the object
**Scenario B — redundant + parametric + barred as a formed read; NOT adopted.**
**Tags.** IT.43–IT.45. **Pattern.** the adjudication tiers (IT.9/IT.10/IT.12's shape), premise audit
logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-IT stays
empty; no clause of Parts 1–4, of Level 5's closed record, or of Tiers IT.1–IT.13 is modified
[AT.63(2)]. **The matrix is recorded as a parametric construction class — the general non-Hermitian
2×2 specialization of IT.37–IT.39's class — NOT a derived row, and NOT adopted.**
**Machine.** `era2/level6_isotopic/checks/cross_currency_matrix.py` → **19/19 exact** (multivariate
Laurent polynomials over Gauss(i) over `Fraction`; formal partial derivatives; the canon's own
pair-channel basis re-used verbatim from `measurement_theorem.py` B3; exact 4×4 conjugations and
Pauli-coordinate comparisons); `run_all_level6.py` → **15 checkers, 230 exact markers, 0 failures**;
`check_level6_format.py` → the gate over all fourteen Part 6 documents. Exact arithmetic: integer
and `Fraction` exponents only, no floating point in any assertion.
**No floating point in any assertion. No measured value enters any clause [P5] — $\rho_{\mathrm B}$
and $\varepsilon_q$ stay symbolic slots; $m_L,m_S$ are ledger-native reads, NOT Standard-Model
masses; no calibration value is issued. No species identification [Def-BM.3(1),(7)]. No
smooth-manifold analogy — the partial derivatives below are FORMAL polynomial operations on slot
alphabets, $\neg$analysis; "perspective" language is rejected at IT.44(6). Prices are $\neg$masses
[HistLog §V.32].**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13j): *"Audit a New Cross-Currency Mass Matrix, Its
Tensor Product, S-T Decomposition, and the Photon/Observer Derivative Asymmetry … the matrix $M=[[m_L,\rho_{\mathrm B}],[\varepsilon_q,m_S]]$ … Placing
$\rho_{\mathrm B}$ (baryon currency) and $\varepsilon_q$ (lepton currency) as off-diagonal entries
in the same matrix does NOT violate the incommensurability bar … their product appears in the
determinant … the exact algebraic seat of the IT.4 handshake indicator … $S$ carries
$(\rho_{\mathrm B}+\varepsilon_q)$ … $T$ carries $(\rho_{\mathrm B}-\varepsilon_q)$ …
$\partial\varepsilon_q/\partial\rho_{\mathrm B}=0$ (the photon view),
$\partial\rho_{\mathrm B}/\partial\varepsilon_q\ne0$ (the ideal observer view) … Scenario A (new
structure) or Scenario B (redundancy). Be brutally honest."* Executed: the algebra verified exact,
the three structural claims refuted on existing rows, six premise corrections logged at IT.45(4),
the verdict Scenario B.

---

### IT.43 — The object entry by entry, the exact tensor/S-T algebra, and the three obstructions

**Thm.**
$$(1)\quad\textbf{THE OBJECT AND THE ENTRY AUDIT:}\qquad M=\begin{pmatrix}m_L & \rho_{\mathrm B}\\ \varepsilon_q & m_S\end{pmatrix}\ \ \text{on the 2-dim carrier}\ \mathbb C^2\ \ [\mathrm{Def\text{-}H.33}]:$$
$$m_L=\text{the informational read}\ E_{\mathrm{int}}\ln2/\mathfrak h\ \ [\mathrm{FT.44}(4);\ \text{the neutron floor row}\ \mathrm{BM.17}(3)],\qquad \rho_{\mathrm B}=\frac{\hat\mu'^2\mathfrak h^2}{(\ln2)^2}\in\mathfrak q^0,\ \neg\text{declared}\ \ [\mathrm{BM.83}(4);\ \mathrm{IT.5}(1)],$$
$$\varepsilon_q=\text{the A4 threshold},\ x_\pm=1{-}4\varepsilon_q,\ 4\varepsilon_q\ \ [\mathrm{BM.19}(2);\ \mathrm{D0.4};\ \mathrm{AT\text{-}O27}:\ \tfrac18\ \text{distinguished five ways, adoption}\ \neg\text{issued}],\qquad m_S:\ \textbf{see}\ (6)\ \text{— ``quantum free charge'' is}\ \neg\textbf{a canon term};$$
$$\textbf{the currency labels are correct:}\ \ \{E_{\mathrm{int}},\hat\mu'^2,\rho_{\mathrm B},D_S\}\ \cap\ \{\varepsilon_q,x_\pm,w_c,\sigma_\ell,z^{(\ell)}\}=\varnothing,\ \ \text{shared symbols}\ \{\mathfrak h,\ln2,\pi\}\ \ [\mathrm{IT.4}(2)\ \text{re-certified by machine}]$$
$$(2)\quad\textbf{THE TENSOR PRODUCT IS CORRECT (the directive's Step 1 verified):}\qquad (M\otimes M)_{(i,k),(j,l)}=M_{ij}M_{kl}\ \ \text{equals the directive's explicit}\ 4\times4\ \ \textbf{entrywise (16/16 symbolic equalities):}$$
$$\textbf{the seat census of the pure product}\ \rho_{\mathrm B}\varepsilon_q:\ \ \text{exactly the positions}\ (2,3),(3,2);\qquad \det M=m_Lm_S-\rho_{\mathrm B}\varepsilon_q\ \ (\text{coefficient}\ {-}1);\qquad \text{discriminant}\ (m_L{-}m_S)^2{+}4\rho_{\mathrm B}\varepsilon_q\ \ ({+}4);$$
$$\text{and the}\ \mathrm{IT.38}(1)\text{-style combination}\ \ C_{11}{+}C_{22}=v_1^2+v_2^2=(\rho_{\mathrm B}{+}\varepsilon_q)^2-(\rho_{\mathrm B}{-}\varepsilon_q)^2=4\rho_{\mathrm B}\varepsilon_q\ \ [\text{machine}]$$
$$(3)\quad\textbf{OBSTRUCTION 1 — THE}\ \mathfrak q\textbf{-INHOMOGENEITY (new; IT.37's}\ M\ \textbf{did not have it):}\qquad [m_L]=[m_S]=\mathfrak q^{+1/2}\ \ [\mathrm{BM.83}(4):\ m=\mu z,\ \text{the exponent arithmetic}],\ \ [\rho_{\mathrm B}]=[\varepsilon_q]=\mathfrak q^0\ \ [\mathrm{BM.83}(4);\ \mathrm{BM.19}(2)]:$$
$$\text{the entries of}\ M\ \text{span TWO degrees}\ \{0,\tfrac12\};\qquad \det M\ \text{sums}\ \mathfrak q^1\ (m_Lm_S)\ \ \text{with}\ \ \mathfrak q^0\ (\rho_{\mathrm B}\varepsilon_q);\qquad \text{the discriminant likewise}\ \ \{\mathfrak q^1,\mathfrak q^0\};$$
$$\text{contrast (machine): IT.37(1)'s}\ M\ \text{with}\ [w]=\mathfrak q^{1/2}:\ \ \deg(\text{entries})=\{\tfrac12\},\ \deg(\det)=\{1\}\ \ \text{homogeneous};\qquad\boxed{\ \text{homogenizing the new}\ M\ \text{needs a DECLARED mass}^2\ \text{scale — a P4-class act}\ [\mathrm{BM.6}(4)],\ \text{none issued}\ }$$
$$(4)\quad\textbf{THE S-T DECOMPOSITION (exact; one directive claim corrected):}\qquad S=\tfrac12(M\otimes M+(M\otimes M)^T),\quad T=\tfrac12(M\otimes M-(M\otimes M)^T):$$
$$S+T=M\otimes M,\quad S^T=S,\quad T^T=-T\ \ [\text{machine: }16/16\text{ each}];\qquad S\ \text{carries}\ \tfrac12 m_L(\rho_{\mathrm B}{+}\varepsilon_q),\ \ \tfrac12(\rho_{\mathrm B}^2{+}\varepsilon_q^2),\ \ \tfrac12 m_S(\rho_{\mathrm B}{+}\varepsilon_q);$$
$$T\ \text{carries}\ \tfrac12 m_L(\rho_{\mathrm B}{-}\varepsilon_q),\ \ \tfrac12(\rho_{\mathrm B}^2{-}\varepsilon_q^2)=\tfrac12(\rho_{\mathrm B}{-}\varepsilon_q)(\rho_{\mathrm B}{+}\varepsilon_q),\ \ \tfrac12 m_S(\rho_{\mathrm B}{-}\varepsilon_q):$$
$$\boxed{\ \textbf{CORRECTION:}\ T\ \text{'s}\ (1,4)\ \text{entry FACTORS through}\ (\rho_{\mathrm B}{+}\varepsilon_q)\ \text{— ``}T\ \text{carries}\ (\rho_{\mathrm B}{-}\varepsilon_q)\text{'' is true but INCOMPLETE}\ [\text{machine: the polynomial identity}]\ }$$
$$(5)\quad\textbf{THE STRUCTURAL FACT (the tier's one gem):}\qquad \iota:=\text{the currency involution}\ \rho_{\mathrm B}\leftrightarrow\varepsilon_q\ \ (\text{the diagonal is}\ \iota\text{-fixed}):\qquad \iota(M)=M^T\ \ [\text{machine, entrywise}]:$$
$$\therefore\ \ \iota(M\otimes M)=(M\otimes M)^T,\qquad \iota(S)=+S,\qquad \iota(T)=-T:\qquad\boxed{\ \textbf{for THIS object the transpose S-T split IS the currency-exchange symmetrization}\ }$$
$$\text{and the consequence is a bar EXPOSURE, not a bypass:}\ \ S\ \text{'s entries are then LITERALLY the cross-currency sums}\ (6)$$
$$(6)\quad\textbf{OBSTRUCTION 2 — THE CONTAINER DOES NOT LAUNDER THE SUMS (the key claim adjudicated):}\qquad v_\mu=\mathrm{Tr}(M\sigma_\mu):\ \ v_0=m_L{+}m_S,\ \ \mathbf{v_1=\rho_{\mathrm B}+\varepsilon_q},\ \ v_2=i(\rho_{\mathrm B}{-}\varepsilon_q),\ \ v_3=m_L{-}m_S\ \ [\text{machine}]:$$
$$\text{the barred sum sits ALREADY in the}\ 2\times2\ \text{Pauli decomposition}\ [\mathrm{CT1.1}\ \text{trace-orthogonal basis}];\qquad C_{\mu\nu}=\mathrm{Tr}((M\otimes M)(\sigma_\mu\otimes\sigma_\nu))=v_\mu v_\nu\ \ \text{all 16 verified symbolically}\ [\mathrm{IT.38}(1)\ \text{re-derived}];$$
$$\textbf{12 of the 16}\ C_{\mu\nu}\ \text{carry}\ (\rho_{\mathrm B}{+}\varepsilon_q)\ \text{or}\ (\rho_{\mathrm B}{-}\varepsilon_q)\ \text{as a factor}\ [\text{machine}];\qquad \text{the doctrine:}\ \ \textbf{the ARRAY is formable as a SYMBOLIC expression carrying undeclared slots}\ [\mathrm{IT.4}(3)\ \text{'s reduced-mass precedent}],$$
$$\text{but EVERY scalar read formed from it}\ (\mathrm{Tr},\det,\lambda_\pm,\ S\text{-entries},\ T\text{-entries})\ \text{is a cross-currency sum/difference — BARRED as a formed read}\ [\mathrm{BM.83}(3),(9);\ \mathrm{BM.140}(5):\ \text{``the comparison is arithmetic,}\ \neg\text{a bridge … no derived equation converts them''}];$$
$$\text{and}\ \ \textbf{cross-currency VALUES do not exist pre-calibration}\ \ [\mathrm{IT.4}(2)]\ \ \Rightarrow\ \ \lambda_\pm=\tfrac12\bigl[(m_L{+}m_S)\pm\sqrt{(m_L{-}m_S)^2{+}4\rho_{\mathrm B}\varepsilon_q}\bigr]\ \ \text{is a symbolic shape,}\ \neg\text{a read}$$
$$(7)\quad\textbf{OBSTRUCTION 3 — THE HANDSHAKE SEAT IS MISIDENTIFIED:}\qquad \textbf{the formed MIXED loci are EXACTLY THREE}\ \ [\mathrm{IT.4}(2)\ \text{— an exhaustiveness row}]:$$
$$\mathcal B_{\mathrm{ens}}^{(n)}\ [\mathrm{BM.137}(3)],\qquad \mathcal W_{\text{channel}}=x_+^2\,\chi_{\{NE\ge\mathcal T_0\}}=(1{-}4\varepsilon_q)^2\chi_{\{NE\ge\mathcal T_0\}}\ [\mathrm{BM.122}(3)],\qquad \chi_{\{NE\ge\mathcal T_0\}}\ \textbf{the handshake — BINARY}\ [\mathrm{Def\text{-}BM.17}(3);\ \mathrm{BM.122}(2);\ \mathrm{BM.134}(5)];$$
$$\text{machine: NONE of the three alphabets contains}\ \rho_{\mathrm B}\ \text{or}\ \hat\mu'^2;\qquad \text{the two resolvent species ``meet only through the threshold indicator}\ \chi_{\{NE\ge\mathcal T_0\}}\text{''}\ [\mathrm{BM.134}(5)];$$
$$\boxed{\ \rho_{\mathrm B}\varepsilon_q\ \textbf{appears in NO formed read:}\ \ \text{``the exact algebraic seat of the IT.4 handshake indicator'' is REFUTED — the handshake is the binary}\ \chi,\ \neg\text{a product of the two undeclared slots}\ }$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived (the algebra):}\ (2),(4),(5)\ \text{as symbolic identities};\qquad\textbf{adjudicated:}\ (3),(6),(7);\qquad\textbf{parametric:}\ \rho_{\mathrm B},\varepsilon_q\ \text{undeclared slots}\ [\mathrm{IT.5}(1)],\ \ m_S\ \text{'s read undeclared}\ (6\ \text{of IT.45});$$
$$\neg\text{a declaration},\qquad\neg\text{a measured value}\ [\mathrm{P5}],\qquad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)]$$

**Req.** P4, P5, A4, D0.4 (Parts 1–2); Def-H.33 (Part 3); IT.4(2),(3), IT.5(1), IT.37(1),(2),(4), IT.38(1), AT-O27 (this level / Level 5 ledger); AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.17(3), BM.6(4), BM.17(3), BM.19(2), BM.22(7), BM.83(3),(4),(9), BM.109(2), BM.122(2),(3), BM.134(5), BM.137(3), BM.140(5) (Part 4); CT1.1 (Part 2); FT.44(4) (Part 3); multivariate Laurent polynomial arithmetic over Gauss(i) over `Fraction`, formal partials, set censuses [math; machine: `cross_currency_matrix.py` §§A–B, 8/8].

**Pf.**
$$(1),(2):\ \text{the Kronecker rule computed symbolically and compared entrywise to the directive's array; the monomial seat census over the 16 entries and over}\ \det/\text{discriminant}\ [\text{machine A1, A2}];$$
$$(3):\ \text{the}\ \mathfrak q\text{-degree census of every monomial of the entries,}\ \det,\ \text{discriminant, with the IT.37 contrast}\ [\text{machine A3}];\ \ (4),(5):\ \text{the symbolic}\ S,T\ \text{identities and the}\ \iota\text{-census}\ [\text{machine B1, B2, B3}];$$
$$(6):\ \text{the Pauli reads}\ v_\mu\ \text{by symbolic trace; all 16}\ C_{\mu\nu}\ \text{by explicit symbolic}\ 4\times4\ \text{multiplication against}\ v_\mu v_\nu;\ \text{the factor count}\ [\text{machine B4}];\ \ (7):\ \text{the three loci's alphabet census}\ [\text{machine A4}].\ \blacksquare$$

**Phys.** The matrix the Architect built on the beach is exact linear algebra, and every identity the
directive asked for holds — the tensor product entry by entry, the symmetric and antisymmetric parts,
the product seats at (2,3) and (3,2). It even hides a genuine gem: because the diagonal is fixed by
the currency exchange while the off-diagonal IS the two currencies, transposing this matrix is
exactly exchanging them, so the S-T split is the exchange symmetrization in disguise. But the gem
cuts against the claim it was minted for. The bar the corpus derived is about formed reads, and a
matrix's reads are its invariants: the trace, the determinant, the eigenvalues, the very entries of
S — and each of them is a sum across the two alphabets the era proved disjoint. The container does
not launder the sum; the reduced-mass precedent says exactly this, and says the array remains
formable as a symbolic expression carrying undeclared slots — which is precisely the status this
matrix keeps. On top of the currency bar stands a grading bar the earlier mass matrix did not have:
the diagonal is mass-dimensioned and the off-diagonal dimensionless, so the determinant adds a
mass-square to a pure number, and homogenizing that needs a declared scale nobody has issued. And
the product in the determinant, offered as the seat of the handshake, is not: the handshake is the
binary threshold indicator, the formed mixed loci are exactly three, and the product of the two
undeclared slots appears in none of them.

---

### IT.44 — The grading map and the derivative asymmetry: both refuted on existing rows

**Thm.**
$$(1)\quad\textbf{TWO INVOLUTIONS, NOT ONE:}\qquad \text{the S-T split is the}\ \pm1\ \text{eigensplit of the TRANSPOSE on}\ \mathrm{End}(\mathbb C^4);\qquad \mathrm{CT1.12a}(2)\text{'s}\ S\text{-grading is the}\ \pm1\ \text{eigensplit of the pair-channel SWAP CONJUGATION}\ X\mapsto\Sigma X\Sigma:$$
$$\text{the}\ B3\ \text{grading re-certified on the canon's own basis (machine):}\ \ J_i=\tfrac12(\sigma_j\otimes\sigma_k-\sigma_k\otimes\sigma_j),\ K_i=\tfrac12(\sigma_0\otimes\sigma_i-\sigma_i\otimes\sigma_0)\ \ S\text{-ODD};\qquad E_0,\ \Sigma,\ W_i,\ E^{ii}\ \ S\text{-EVEN}\ [\mathrm{CT1.12a}(2);\ \mathrm{CT1.1};\ \mathrm{CT1.2}]$$
$$(2)\quad\textbf{THE CROSS-CUT (the directive's Step-2 map REFUTED without a new basis):}\qquad\begin{array}{l|l|l}\textbf{operator}&\textbf{the swap grading}\ [\mathrm{CT1.12a}(2)]&\textbf{the transpose parity}\ [\text{machine}]\\\hline J_2,\ K_1,\ K_3&S\text{-odd}&\textbf{EVEN}\ —\ \text{they sit in}\ S\\ J_1,\ J_3,\ K_2&S\text{-odd}&\text{odd}\ —\ \text{they sit in}\ T\\ W_2&S\text{-even}&\textbf{ODD}\ —\ \text{it sits in}\ T\\ E_0,\ \Sigma,\ W_1,\ W_3,\ E^{ii}&S\text{-even}&\text{even}\ —\ \text{they sit in}\ S\end{array}$$
$$\boxed{\ \text{of the six}\ S\text{-odd operators exactly THREE are transpose-even, and an}\ S\text{-even carrier is transpose-odd:}\ \ S\subseteq S\text{-even and}\ T\subseteq S\text{-odd BOTH FAIL}\ }$$
$$(3)\quad\textbf{THE DIMENSION RHYME IS NUMEROLOGY:}\qquad \text{transpose:}\ 16=10{+}6;\qquad \text{swap conjugation:}\ 16=10{+}6\ \ (=\dim\mathrm{End}(\mathrm{Sym}^2)\oplus\dim\mathrm{End}(\wedge^2)=9{+}1\ \text{and}\ 3{+}3);$$
$$\text{the joint refinement on the adapted Pauli basis:}\ 7{+}3{+}3{+}3\ \ [\text{machine}]\ \ —\ \text{rhyming with}\ \mathrm{CT1.12a}(2)\text{'s}\ 10=1{+}1{+}5{+}3\ \text{and}\ \mathrm{CT1.1}\text{'s}\ 7{+}3{+}3{+}3\ \text{blocks, but}\ (2)\ \text{'s witnesses prove the SUBSPACES differ:}$$
$$\textbf{a numerology flag,}\ \neg\textbf{an identification}\ \ [\mathrm{BM.134}(5)\ \text{dictionary discipline: a partner,}\ \neg\text{an equal}]$$
$$(4)\quad\textbf{THE BIVECTOR AND FORCE-ALGEBRA CENSUS:}\qquad \mathrm{AT.56}(2)\ \text{'s six bivectors}\ (-\sigma_3\sigma_0,\ {+}\sigma_2\sigma_0,\ {-}\sigma_1\sigma_0,\ \sigma_1\sigma_3,\ \sigma_2\sigma_3,\ \sigma_3\sigma_3):\ \ \textbf{only 2 of 6 transpose-odd}\ \Rightarrow\ \dim(\text{bivector}\cap T\text{-carrier})=2;$$
$$\text{swap conjugation sends}\ \sigma^{12}=-(\sigma_3\otimes\sigma_0)\ \text{to}\ -(\sigma_0\otimes\sigma_3),\ \text{proportional to NONE of the six (exact Pauli coordinates)}\ \Rightarrow\ \text{the bivectors live in the Dirac}\ \mathcal F_0\ \text{frame, outside BOTH pair-channel eigensplits};$$
$$\text{and the}\ 16\text{-vs-}8\ \text{over-count carries over}\ [\mathrm{IT.38}(2);\ \mathrm{AT.56}\ \text{``zero new operators''}]:\ \ \text{against the derived 8-dim force algebra}\ \mathrm{span}\{I_4,\sigma_i\otimes I_2,\sigma_i\otimes\hat\kappa,I\otimes\hat\kappa\}\ (\hat\kappa=\sigma_3\ [\mathrm{AT.56}(1)]):$$
$$\boxed{\ S\ \text{has FOUR directions outside,}\ T\ \text{has FOUR outside (machine)}\ \ \Rightarrow\ \ \text{any force reading of}\ S/T\ \text{is a STIPULATION,}\ \neg\text{a derived row}\ }$$
$$(5)\quad\textbf{THE FORMAL-DERIVATIVE CENSUS (the Step-3 premises):}\qquad \text{over the full formed-read census of}\ \mathrm{IT.5}(1)\ \text{'s table}\ \ (m_{\mathrm{hid}},\ \Delta x_{\mathrm B},\ r_s,\ \Delta x_{\mathrm B}r_s,\ \rho_{\mathrm B},\ m^2_{\mathrm{pole}},\ \mathcal W_{\text{channel}},\ \mathcal W_{\text{round}},\ \mathcal B_{\mathrm{ens}}^{(2)},\ W_d):$$
$$\boxed{\ \textbf{NO formed read contains BOTH slots}\ \rho_{\mathrm B}\ \text{and}\ \varepsilon_q\ \ \text{(machine)}\ \ \Rightarrow\ \ \neg\exists\ \text{a derived functional dependence IN EITHER DIRECTION — the independence is SYMMETRIC}\ }$$
$$\frac{\partial\varepsilon_q}{\partial\rho_{\mathrm B}}=0\ \ \textbf{AND}\ \ \frac{\partial\rho_{\mathrm B}}{\partial\varepsilon_q}=0\ \ \text{exactly (formal partials;}\ \rho_{\mathrm B}\ \text{'s derived read}\ \hat\mu'^2\mathfrak h^2/(\ln2)^2\ \text{has alphabet}\ \{\hat\mu'^2,\mathfrak h,\ln2\}\ \ [\mathrm{BM.83}(4)]);$$
$$\textbf{the directive's premise is FALSE:}\ \ \partial m_{\mathrm{hid}}/\partial\varepsilon_q=0,\ \ \partial\Delta x_{\mathrm B}/\partial\varepsilon_q=0\ \ [\mathrm{FT.44}(4);\ \mathrm{Def\text{-}BM.4}(1)]\ \ —\ \ \text{``the informational mass … governed by the flicker threshold'' has no row};$$
$$\text{the ONLY nonzero flicker partials are at the composite loci:}\ \ \partial\mathcal W_{\text{channel}}/\partial\varepsilon_q=-8(1{-}4\varepsilon_q)\chi\ne0,\quad \partial\mathcal W_{\text{channel}}/\partial\rho_{\mathrm B}=0\ \ [\mathrm{BM.122}(3);\ \mathrm{IT.4}(2)]$$
$$(6)\quad\textbf{THE ASYMMETRY ADJUDICATED — NO SEAT:}\qquad \text{the claimed pair}\ (0,\ \ne0)\ \text{requires a DECLARED functional link}\ \rho_{\mathrm B}(\varepsilon_q):\ \ \text{a cross-currency CONVERSION — barred as a formed equation}\ [\mathrm{BM.140}(5);\ \mathrm{BM.83}(9)]\ \text{and a P4-class declaration}\ [\mathrm{BM.6}(4)]\ \text{— none issued};$$
$$\textbf{the framing is rejected row by row:}\ \ \text{``perspectives'' are}\ \neg\text{ledger primitives — the observer is a designated register}\ [\mathrm{Def\text{-}H.9};\ \mathrm{IT.1}(8)(\mathrm P4):\ \neg\text{consciousness,}\ \neg\text{a smooth analogy}];$$
$$\text{the photon has}\ \neg\text{a formed perspective read at all — the transit-leg amplitude}\ \neg\text{formed}\ [(\mathrm{R9}'');\ \mathrm{BM.122}(6);\ \mathrm{IT.3}(6)],\ \ \text{the D3.7 trivial chains are OUT of Def-H.38's scope}\ [\mathrm{IT.41}];$$
$$\varepsilon_q\ \text{is a GLOBAL A4-threshold slot}\ [\mathrm{BM.19}(2);\ \mathrm{D0.4}],\ \neg\text{a per-species possession};\qquad \rho_{\mathrm B}\ \text{(an undeclared}\ \mathfrak q^0\ \text{slot)}\ \ \textbf{is}\ \neg\textbf{a seal class — CATEGORY ERROR:}\ \ \text{the proton class 15 of 64 is the derived integer census}\ W_3(Q)=\binom6{Q+3}\ [\mathrm{AT.41}(2),(3);\ \mathrm{IT.4}(4)]$$
$$(7)\quad\textbf{THE IT.10 CITATION IS INVERTED — and the salvageable kernel:}\qquad \Delta x_{\mathrm B}\,r_s=\mathfrak h^2/(2\ln2)\ \ \text{re-derived symbolically,}\ E_{\mathrm{int}}\text{-independent, alphabet}\ \{\mathfrak h,\ln2\}\ \ [\mathrm{BM.17}(3);\ \mathrm{IT.31}(1)]:$$
$$\text{the anchor's bypass licenses the geometric/cardinal/sign reads BECAUSE they never mix currencies}\ [\mathrm{IT.32}(3):\ \text{``NONE is a cross-currency mass sum''}]\ \ —\ \ \text{citing it for a}\ \rho_{\mathrm B}(\varepsilon_q)\ \text{dependence uses the row to license what its proof excludes};$$
$$\boxed{\ \textbf{the salvageable kernel is IT.4(2)'s locus distinction, already derived:}\ \ \varepsilon_q\ \text{enters the observer's formed reads ONLY at the three composite mixed loci}\ (\mathcal W_{\text{channel}},\ \mathcal B_{\mathrm{ens}},\ P(\Delta x_{\mathrm B})\ \text{'s sharpening}\ [\mathrm{BM.122}(3);\ \mathrm{IT.5}(1)]),\ \text{while the geometric reads are}\ \varepsilon_q\text{-free}\ }$$
$$\text{the handshake's operational semantics stay where the level put them:}\ \mathrm{IT\text{-}O3}\ \ [\mathrm{IT.1}(5)]$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5),(7)\ \text{'s re-derivation};\qquad\textbf{refuted:}\ \text{the Step-2 grading map}\ (2),\ \text{the Step-3 asymmetry}\ (5),(6);\qquad\neg\text{a declaration},\ \ \neg\text{a new open row}$$

**Req.** P4, P5, A4, D0.4, CT1.1, CT1.2, CT1.12a(2) (Parts 1–2); Def-H.9, Def-H.33, Def-H.38, FT.44(4) (Part 3); IT.1(5),(8), IT.3(6), IT.4(2),(3),(4), IT.5(1), IT.31(1), IT.32(3), IT.38(2), IT.41, IT-O3 (this level); AT.41(2),(3), AT.56(1),(2), AT.63(2) (Level 5); Def-BM.4(1), Def-BM.17(3), BM.6(4), BM.15(4), BM.17(3), BM.19(2), BM.83(4),(9), BM.122(2),(3),(6), BM.134(5), BM.137(1),(3), BM.140(5) (Part 4); exact 4×4 conjugations over Gauss(i), Pauli-coordinate comparisons, formal polynomial partials [math; machine: `cross_currency_matrix.py` §§C–D, 6/6].

**Pf.**
$$(1),(2):\ \text{the}\ B3\ \text{basis built verbatim; the swap conjugations and the transposes computed on all twelve carriers}\ [\text{machine C1, C2}];\ \ (3):\ \text{the adapted-basis parity census}\ (16=7{+}3{+}3{+}3)\ [\text{machine C3}];$$
$$(4):\ \text{the six bivectors' transpose parities; the}\ \sigma^{12}\ \text{swap image against all six in exact Pauli coordinates; the symbolic supports of}\ S,T\ \text{against the 8-dim span}\ [\text{machine C4, C5}];$$
$$(5):\ \text{the ten formed reads encoded as Laurent polynomials/rational pairs; the alphabet and both-partials censuses; the four formal partials}\ [\text{machine D1, D2}];\ \ (6),(7):\ \text{record rows on the cited clauses; the anchor product re-derived}\ [\text{machine D3}].\ \blacksquare$$

**Phys.** The directive asked whether the symmetric part is the corpus's S-even world and the
antisymmetric part its S-odd one, and the answer comes from the corpus's own operators rather than
from an argument: half of the S-odd six — J₂, K₁, K₃ — are transpose-symmetric and would sit inside
the "cooperative" block, while the shift carrier W₂ is transpose-antisymmetric and would sit inside
the "gap." The two involutions cross-cut; the matching dimensions 10+6 and the 7+3+3+3 rhyme are the
kind of coincidence the dictionary discipline exists to quarantine. The derivative asymmetry fares
worse, because it asks the ledger for a dependence the ledger never wrote: the slot census of the
level's opening tier says the two currency families share no formed read, so both formal partials
vanish — the independence is symmetric, and the only asymmetric statement available, a nonzero
∂ρ_B/∂ε_q, is precisely a cross-currency conversion, the one act the incommensurability bar forbids
and no declaration has issued. The photon and the observer, as perspectives with different
derivative structures, are not primitives here: the observer is a register, the photon has no formed
transit read at all, the flicker slot is global rather than photonic, and the pole slot is not a seal
class. What survives of the intuition is real but already derived — flicker enters the observer's
reads only at the composite loci, while the geometry the anchor licenses stays flicker-free — and
that is a locus census, not an asymmetry.

---

### IT.45 — The redundancy adjudication: Scenario B; m_S maps to existing rows; the declaration census

**Thm.**
$$(1)\quad\textbf{THE SPECIES CENSUS (machine):}\qquad M-M^\dagger\ne0\ \ \text{symbolically (the}\ (1,2)\ \text{entry}\ \rho_{\mathrm B}-\varepsilon_q;\ \ v_2=i(\rho_{\mathrm B}{-}\varepsilon_q)\ \text{purely imaginary)}:\ \ \textbf{NON-HERMITIAN},\ \text{unlike}\ \mathrm{IT.37}(1)\text{'s}\ M\ \text{and}\ \mathrm{BM.22}\text{'s}\ \mathbf F_{\mathrm{ext}}:$$
$$\mathbf F_{\mathrm{ext}}\ \text{reduced}=hI+q\sigma_1\ \ (2\ \text{slots, symmetric flip, DERIVED}\ q\in\{-1,0,+1\}\ [\mathrm{BM.22}(1),(2),(4),(7);\ \mathrm{EM.9}])\ \ \subset\ \ \mathrm{IT.37}\text{'s}\ M\ \ (3\ \text{slots, Hermitian, conjugate flip})\ \ \subset\ \ \textbf{the new}\ M=\textbf{the general}\ 2\times2\ \ (4\ \text{slots});$$
$$\boxed{\ \textbf{the new}\ M\ \textbf{is the non-Hermitian specialization of the SAME parametric construction class recorded at IT.37--IT.39 — REDUNDANT}\ [\mathrm{IT.38}(3);\ \mathrm{IT.39}(3)]\ }$$
$$(2)\quad\textbf{THE S-T SPLIT ADDS NO NEW CONTENT:}\qquad \text{the Pauli supports of}\ S\ (10\ \text{directions)}\ \cup\ T\ (6)\ =\ 16\ \text{of the}\ 16\ \sigma_\mu\otimes\sigma_\nu\ \text{— the same span}\ \mathrm{IT.38}\ \text{censused:}\ \ \textbf{zero new operators}\ [\mathrm{AT.56}];$$
$$\text{zero new mixed loci}\ [\mathrm{IT.4}(2)\ \text{'s exhaustiveness}];\qquad \text{the gem}\ \iota(M)=M^T\ [\mathrm{IT.43}(5)]\ \text{is a property of the slot placement whose consequence is the bar exposure}\ [\mathrm{IT.43}(6)]\ \ —\ \ \text{the split repackages,}\ \neg\text{extends}$$
$$(3)\quad\textbf{m\_S ADJUDICATED — ``quantum free charge'' is}\ \neg\textbf{a canon term; both candidate reads are existing rows:}\qquad (\mathrm a)\ \ \text{the rung-1 seal informational mass}\ m_S=2\ln2/\mathfrak h\ \ (E_{\mathrm{int}}{=}2\ [\mathrm{FT.28};\ \mathrm{IT.37}(1)]):$$
$$m_S\mathfrak h=2\ln2=\text{the two-bit floor at equality}\ \ [\mathrm{BM.70}(2),(3)\ \text{re-cited at}\ \mathrm{BM.83}(8)];\qquad (\mathrm b)\ \ \text{the lightest-}\nu\ \text{scale}\ \sigma_\nu z^{(\nu)}_1\ln2/\mathfrak h,\ \ \sigma_\nu\ \neg\text{declared, the absolute}\ \nu\ \text{mass}\ \neg\text{derived}\ [\mathrm{BM.83}(4),(5),(8);\ \mathrm{FT.143}(3)];$$
$$\text{under}\ (\mathrm a)\ \ \mathrm{Tr}\,M\ \text{is commensurable}\ [\mathrm{IT.37}(4)];\qquad \text{under}\ (\mathrm b)\ \ \mathrm{Tr}\,M=m_L{+}m_S\ \text{is a reduced-mass-type cross-currency SUM — barred as a formed read}\ [\mathrm{IT.4}(3);\ \mathrm{BM.83}(3)];$$
$$\boxed{\ \textbf{NEITHER read is a new object; the verdict below holds under BOTH — no route-choice declaration is forced}\ (\text{contrast the owed choice at}\ \mathrm{IT.14}(3))\ }$$
$$(4)\quad\textbf{THE VERDICT — SCENARIO B (redundancy), sharpened; the six premise corrections:}\qquad\begin{array}{l|l}\textbf{premise}&\textbf{the correction}\\\hline(\mathrm P1)&\text{the}\ \mathfrak q\text{-inhomogeneity:}\ \det\ \text{sums}\ \mathfrak q^1\ \text{with}\ \mathfrak q^0\ \text{— a defect IT.37's}\ M\ \text{did not have}\ [\mathrm{IT.43}(3)]\\(\mathrm P2)&\text{the container argument fails: every scalar read is a cross-currency sum, barred as a formed read}\ [\mathrm{IT.43}(6)]\\(\mathrm P3)&\rho_{\mathrm B}\varepsilon_q\ \text{is}\ \neg\text{the handshake seat — the three formed mixed loci are exhaustive; the handshake is the binary}\ \chi\ [\mathrm{IT.43}(7)]\\(\mathrm P4)&\text{the}\ S/T\leftrightarrow S\text{-even}/S\text{-odd map fails on the canon's own basis}\ (J_2,K_1,K_3;\ W_2)\ [\mathrm{IT.44}(2),(4)]\\(\mathrm P5)&\text{the derivative asymmetry has no seat — symmetric independence; the nonzero direction would be a barred conversion}\ [\mathrm{IT.44}(5),(6)]\\(\mathrm P6)&m_S\ \text{maps to existing rows; ``quantum free charge''}\ \neg\text{defined}\ [\mathrm{IT.45}(3)]\end{array}$$
$$\boxed{\ \textbf{M is CONSTRUCTIBLE and its algebra EXACT, but REDUNDANT}\ [\mathrm{IT.38}(3)]\ \textbf{+ PARAMETRIC}\ [\mathrm{IT.5}(1)]\ \textbf{+ BARRED as a formed read}\ [\mathrm{IT.43}(3),(6)]\ \textbf{— NOT ADOPTED; recorded as a parametric construction class}\ }$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition adopted},\quad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\quad\neg\text{a measured value}\ [\mathrm{P5}],\quad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))];\qquad §\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{bars untouched:}\ \ \mathrm{BM.83}/\mathrm{BM.134}(5)/\mathrm{BM.140}(5)\ \text{(no currency mixing, no bridge)},\qquad \textbf{open rows unchanged — NO new row:}\ \text{the object adds nothing to}\ \mathrm{IT\text{-}O1/O2/O3/O5}\ \text{or the owed declarations};$$
$$\textbf{if the Architect ever wants}\ M\ \textbf{as a derived object, THREE declaration acts would be owed (none forced, none issued):}\ \ (\mathrm i)\ \text{a mass}^2\ \text{scale homogenizing}\ \det;\ \ (\mathrm{ii})\ \text{a functional link}\ \rho_{\mathrm B}(\varepsilon_q)\ \text{— a cross-currency conversion, the bar itself}\ [\mathrm{BM.140}(5)];\ \ (\mathrm{iii})\ \text{the restriction of any}\ S/T\ \text{force reading to AT.56's 8-dim algebra}\ [\mathrm{IT.38}(2)]$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{cross\_currency\_matrix.py}\to\textbf{19/19 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{15 checkers, 230 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{14 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad \text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no new object is adopted}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P4, P5 (Parts 1–2); Def-H.33, FT.28, FT.44(4), FT.143(3) (Part 3); IT.4(2),(3), IT.5(1), IT.14(3), IT.37(1),(4), IT.38(2),(3), IT.39(3), IT.43, IT.44, IT-O1, IT-O2, IT-O3, IT-O5 (this level); AT.39(8), AT.56, AT.63(2),(4) (Level 5); Def-BM.3(1),(7), BM.6(4), BM.22(1),(2),(4),(7), BM.70(2),(3), BM.83(3),(4),(5),(8), BM.134(5), BM.140(5), EM.9 (Parts 2, 4); the assembly rows [math; machine: `cross_currency_matrix.py` §E, 3/3].

**Pf.**
$$(1):\ \text{the symbolic}\ M-M^\dagger\ \text{and the}\ v_2\ \text{purity; the species line on the slot counts}\ [\text{machine E1}];\ \ (2):\ \text{the support census}\ [\text{machine C5, E3}];$$
$$(3):\ \text{the floor identity}\ m_S\mathfrak h=2\ln2\ \text{and the trace alphabets under both reads}\ [\text{machine E2}];\ \ (4)\text{--}(7):\ \text{the verdict assembled from}\ \mathrm{IT.43}(3),(6),(7),\ \mathrm{IT.44}(2),(4),(5),(6)\ \text{and}\ (1)\text{--}(3);\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (5)\text{--}(7).\ \blacksquare$$

**Phys.** The verdict is Scenario B, and it is sharper than the one Tier IT.12 recorded, because
this object fails where its predecessor was clean. The Hermitian mass matrix was at least
dimension-honest — its off-diagonal carried mass — and its only sins were a pair of undeclared
parameters and a force map that over-counted. The cross-currency matrix puts a dimensionless pole
slot and a dimensionless flicker threshold where masses belong, so its determinant adds apples to
numbers; it puts the two currencies the era proved disjoint into every invariant it forms, so the
container argument cannot save it; it names a product the handshake census does not contain; and it
asks two involutions to be the same involution when the corpus's own J₂ and W₂ say otherwise. What
is left is exactly what the level already owned: a general 2×2 parametric class with the Pauli
anatomy of AT.56–58 and the redundancy of BM.22, now with a currency bar on its reads. The tier
records it, proves its algebra, names its six corrections and the three declarations that would be
owed to promote it, and adopts none of it — the honest disposition the directive itself invited.

---

## §Cal-IT — unchanged from Tier IT.14

**Empty at this tier.** The cross-currency matrix is a parametric construction class; its two
off-diagonal slots ($\rho_{\mathrm B}$, $\varepsilon_q$) are INHERITED undeclared slots
[IT.5(1); BM.83(4); AT-O27], NOT added as parameters — adopting them, a homogenizing mass² scale,
or a functional link $\rho_{\mathrm B}(\varepsilon_q)$ would each be a P4-class declaration
[BM.6(4)], and none is issued. The parametric residues remain the open rows and the inherited owed
declarations — the mass-read route choice [IT.14(3); BM.30(5)], $\mathfrak h$ (P1), $\varepsilon_q$
(AT-O27), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$,
$\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared), the P4 transport profile, the lift and the
vielbein (AT.60), and the read rules (M1′)–(M3′) [AT.54(6)].

## §Open-IT additions from Tier IT.14

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.14 opens **no new row**: the cross-currency matrix is recorded as a **parametric construction class** — the general non-Hermitian 2×2 specialization of IT.37–IT.39's class (redundant with BM.22 + AT.56–58; the S-T split adds zero operators and zero loci; the handshake-seat, grading-map and derivative-asymmetry claims refuted on existing rows; $\mathfrak q$-inhomogeneous; barred as a formed read). It is **not adopted**. If the Architect ever wants it as a derived object, three declarations are owed [IT.45(5)] | IT.43(3),(6),(7); IT.44(2),(5); IT.45(1),(4) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42]: (IT-O1) the formed transit-leg amplitude — open on three
grounds, the missing primitive deficit 1′ [IT.41]; (IT-O2) the N≥4 multi-seal configuration
calculus — the binding value; (IT-O3) the handshake-indicator operational theory — the
χ_{NE≥𝒯₀}-gated read families across the threshold ladder (the proper home of the handshake
semantics the directive reached for); (IT-O5) the isotope cutoff — the empirical/dynamical side at
IT-O1; the owed route choice [IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the Level-5
inheritance [AT.63(3),(5)].

---

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

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.16: the probe consolidation — the subgenerator study re-verified, the collisions resolved, and the derived/declared/barred separation

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.16 — the Architect's directive to
consolidate a multi-session SUBGENERATOR STUDY (run outside the repo against a read-only clone:
the mass-reads dimensional analysis MR.1–MR.18 with its amendments, the phase math, the
sixteen-basis metric-force check, the six-gifts/saturated-node findings, the reflection/CPT/rung-zero
calibration audit — all summarized in the delivered `CONSOLIDATED.md` — plus the photon phase-jump
audit PJ.1–PJ.15 and the two-photon radar audit RS.1–RS.10): re-verify every machine claim, resolve
the name collisions, apply the amendments, separate derived / declared / barred, place the tier, and
merge. Executed: the citation audit clean (one self-flagged slip in ~450 tokens), the canon-typo
observation CONFIRMED and recorded probe-side, **all 33 machine claims re-derived from scratch** (the
study's own scripts were not delivered), the collisions resolved, and the content separated — the
operator/angle/census layer ADOPTED AS DERIVED, the matrix layer recorded as the IT.37–IT.39/
IT.43–IT.45 parametric class, the declaration register absorbed (named, none issued), the bars
restated.
**Tags.** IT.49–IT.54. **Pattern.** the consolidation tiers (Tier IT.1's assembly shape + the
adjudication tiers' premise audit), corrections recorded in-tier, never overwritten.
**Status.** discovery-phase working tier. Nothing is adopted into the frozen canon; **no declaration
issues**; §Cal-IT stays empty; no clause of Parts 1–4, of Level 5's closed record, or of Tiers
IT.1–IT.15 is modified [AT.63(2)] — the FT.116(5) typo observation is recorded PROBE-SIDE, and an
erratum row is queued for the Era-2-closure pipeline [AT.63(4)].
**Machine.** `era2/level6_isotopic/checks/probe_consolidation.py` → **33/33 exact** (Fraction
polynomial rings with exact quotient reductions — $\mathbb Q[t_2]/(t_2^2{-}2)$,
$\mathbb Q[ct,st,t_2,t_3]/(ct^2{+}st^2{-}1,t_2^2{-}2,t_3^2{-}3)$,
$\mathbb Q[x,a_0,z_r,z_i,\mathrm j]/(\mathrm j^2{+}1)$, $\mathbb Q[\gamma]$,
$\mathbb Q[s]/(s^2{-}\Delta)$; a jet-derivation algebra; Faddeev–LeVerrier; Gauss(i) $4\times4$
elimination; exhaustive enumeration; rational $\pi$-certificates $333/106<\pi<355/113$ — NO floating
point); `run_all_level6.py` → **17 checkers, 276 exact markers, 0 failures**;
`check_level6_format.py` → the gate over all sixteen Part 6 documents.
**No floating point in any assertion. No measured value enters any clause [P5] — the study's
probe-side decimals (the channel hierarchies, the trig corrections) are NOT carried; the canon's own
enclosures stand [FT.113; FT.119(5)]. No species identification [Def-BM.3(1,(7))]; channel labels
$\ell,q,\nu$ are ledger rows, ¬particles [FT.158 Rmk]. No smooth-manifold analogy — every derivative
in this tier is a FORMAL polynomial/jet operation. Prices are ¬masses [HistLog §V.32].**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13l): *"Consolidate, Re-Verify, and Merge the
Mass-Reads Study into the Main Corpus … Amendments override originals … Name collisions must be
resolved, not papered over … Derived / declared / barred must be separated at every step … Machine
claims must be re-verified … Corpus rows are cited, never re-derived … Do not force a declaration. Do
not import a measured value [P5]. Do not add a new dimensionful scale [P1] … The merge must not edit
existing canon rows."* And the Architect's note: the subgenerator does not know the imaginator
hallucinates — every citation was therefore screened against the registry before any content was
trusted.

---

### IT.49 — The intake: the citation audit, the collision resolutions, and the corrections register

**Thm.**
$$(1)\quad\textbf{THE INTAKE:}\qquad\text{four documents delivered}\ (\text{CONSOLIDATED Parts I--XII};\ \text{CONTINUUM the study's map};\ \mathrm{PJ.1}\text{--}\mathrm{PJ.15};\ \mathrm{RS.1}\text{--}\mathrm{RS.10}),\ \text{four working files summarized-not-delivered},\ \text{five verification scripts}\ \neg\text{delivered}:$$
$$\boxed{\ \text{every machine claim is RE-DERIVED FROM SCRATCH in}\ \texttt{probe\_consolidation.py}\ (33/33)\ \ —\ \ \neg\text{a claim rides on an undelivered certificate}\ }$$
$$(2)\quad\textbf{THE CITATION AUDIT (the hallucination screen):}\qquad\text{the level gate's registry logic over all four documents:}\ \ 167{+}125{+}124{+}104\ \text{distinct tag tokens}:$$
$$\textbf{ONE unattested:}\ \ \text{a CT0-prefix slip for}\ \mathrm{CT3.20}\ \text{in PJ.12's Req — the document's own bracket flags it ``[as CT3.20]''}:\ \text{corrected here; the full token is recorded in the discovery document};\qquad \sim65\ \text{clause-level checks PASS, including every verbatim quote}\ [\mathrm{BM.102}(4);\ \mathrm{FT.131}(3);\ \mathrm{Def\text{-}H.41}/\mathrm{Def\text{-}H.42}\ \text{bars};\ \mathrm{FT.142}\ \mathrm{Rmk};\ \mathrm{C10};\ \mathrm{C11};\ \mathrm{C13};\ \mathrm{IT.32}(5)];$$
$$\text{the}\ \texttt{calibration\_anchor.py}\ \text{machine-record string PJ.9(1) cites is present}\ (\text{``absolute relativity (Step 2)'')}\ \ [\text{machine}]$$
$$(3)\quad\textbf{THE CANON-TYPO OBSERVATION — CONFIRMED, HARMLESS, PROBE-SIDE:}\qquad \mathrm{FT.116}(5)\ \text{prints}\ \ 108(\operatorname{Im}z^3)^2=108(\operatorname{Im}z)^2\bigl(3(\operatorname{Re}z)^2-(\operatorname{Im}z)^2\bigr)\ \ \text{with the second factor UNSQUARED}:$$
$$\text{the exact identity is}\ \ (\operatorname{Im}z^3)^2=(\operatorname{Im}z)^2\bigl(3(\operatorname{Re}z)^2-(\operatorname{Im}z)^2\bigr)^2\ \ \text{(machine: both expansions against}\ {-}4p^3{-}27q^2;\ \text{witness}\ z{=}1{+}\mathrm i:\ 432{=}432\ne216);$$
$$\text{the ZERO LOCUS — all the clause uses — is identical either way};\qquad\boxed{\ \text{recorded probe-side; the frozen canon is}\ \neg\text{edited}\ [\mathrm{AT.63}(2)];\ \text{an erratum row is queued for the Era-2-closure pipeline}\ [\mathrm{AT.63}(4)]\ }$$
$$(4)\quad\textbf{THE}\ \rho_{\mathrm B}\ \textbf{COLLISION RESOLVED (the study's ``biggest open item''):}\qquad\text{the corpus's}\ \rho_{\mathrm B}=\hat\mu'^2\mathfrak h^2/(\ln2)^2\in\mathfrak q^0\ \ \text{is the BRIDGE}\ [\mathrm{BM.69}(2);\ \mathrm{BM.83}(4);\ \mathrm{BM.102}(4):\ \text{``converts no dimension — the dimensionless exchange rate between the bit currency and the angle currency''};\ \text{declared A-BM.9, value}\ \neg\text{issued}]:$$
$$\text{the corpus's}\ \ \rho=\mathfrak h^{-4}E^4(\ln2)^4\in\mathfrak q^{+2}\ \ \text{is the DENSITY}\ [\mathrm{BM.14}(2),(4);\ \mathrm{BM.102}(2)];\qquad\text{machine: distinct monomials, distinct degrees, distinct alphabets};$$
$$\boxed{\ \textbf{the convention:}\ \ \rho_{\mathrm B}:=\text{the bridge};\ \ \rho:=\text{the density}\ \ —\ \ \text{MR.3's}\ \text{``}\rho_{\mathrm B}:=m_{\mathrm B}/V_{\mathrm{eff}}\text{'' was a mislabel (register \#15)};\ \ \text{the}\ b\text{-slot fork (density vs bridge) stays an OPEN parametric read-choice, both branches carried, neither selected}\ [\mathrm{BM.30}(5)\ \text{pattern}]\ }$$
$$(5)\quad\textbf{THE NOTATION UNIFICATION:}\qquad \delta_{\mathrm{ch}}:=\text{the channel phase}\ \{\tfrac29,\tfrac2{27},\tfrac18\}\ [\mathrm{FT.112};\ \mathrm{FT.119}(1);\ \mathrm{FT.142}(5)];\qquad s_{\mathrm{ch}}:=\text{the exponent of}\ \mu_{\mathrm{ch}},\ \ \text{every}\ s\ \text{undeclared}\ [\mathrm{P4};\ \text{Cal-F}]\ \ (\text{register \#16});$$
$$\kappa\ne\varkappa\ \ [\mathrm{CT2.9}\ \text{vs}\ \mathrm{P4}\ \text{core}];\qquad\text{the hazard census stands: four}\ c\ (\varepsilon_q\ \text{entry};\ e^2/4\pi;\ \text{the speed};\ \text{the chain in}\ G(c)),\ \text{four}\ \rho,\ \text{six}\ \mu,\ \text{two}\ \kappa\ \ [\mathrm{CONSOLIDATED}\ \S42];$$
$$\text{family/line index}\ k\in\{0,1,2\},\ \ \text{imaginary unit}\ \mathrm i;\qquad \mathcal S,\mathcal T:=\text{the two Pauli readouts};\ \ S,T:=\text{A3's swap and grade}\ [\mathrm{A3};\ \mathrm{C13}]$$
$$(6)\quad\textbf{THE AMENDMENT CHAIN (rule 1 applied; all recorded, none overwritten):}\qquad \text{MR.1--MR.9}\ \to\ \text{MR.10/MR.11 amendments}\ \to\ \text{the sixteen-basis check}\ (\text{``16 maps 1:1''}\ \to\ 10\ \text{of}\ 16)\ \to\ \text{PJ}\ \S0\ \text{(six corrections)}\ \to\ \text{RS}\ \S0\ \text{(six corrections; RS's clarification OVERRIDES PJ.4's temporal reading — the tick labels attach to emission/reception)}:$$
$$\text{the full register: CONSOLIDATED Part X's}\ 17\ \text{rows}\ +\ \mathrm{PJ}\ \text{'s}\ 6\ +\ \mathrm{RS}\ \text{'s}\ 6\ \ [\text{this tier carries the load-bearing ones at IT.50--IT.53; the register itself is the discovery record}];$$
$$\textbf{untagged identifications STAY untagged:}\ \ \text{the two}\ C_3\ \text{routes (FT.116's Phys prose ``reached from the opposite side'' — no numbered clause); ``the jump factor IS the}\ C_3\ \text{order''}\ [\mathrm{FT.143}(6):\ \text{``a datum for deficit 3,}\ \neg\text{a selection principle''}]\ \ —\ \ \text{carried as readings, never as rows}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (2),(3),(4)\ \text{'s machine censuses};\qquad\textbf{recorded:}\ (1),(5),(6);\qquad\neg\text{a declaration},\ \ \neg\text{a measured value}\ [\mathrm{P5}],\ \ \neg\text{a canon edit}\ [\mathrm{AT.63}(2)]$$

**Req.** P4, P5 (Parts 1–2); IT.43(6), IT.44(3) (this level); AT.63(2),(4) (Level 5); BM.14(2),(4), BM.30(5), BM.69(2), BM.83(4), BM.102(2),(4),(5), FT.116(5), FT.116 Phys (Parts 3–4); A-BM.9; C10, C11, C13, CT2.9, CT3.20, D0.9 (Parts 1–2); FT.112, FT.113, FT.119(1),(5), FT.131(3), FT.142(5), FT.143(6), FT.158 Rmk, Def-H.41, Def-H.42 (Part 3); IT.32(5) (this level); the gate's registry logic; exhaustive token sweeps [math; machine: `probe_consolidation.py` §G1 + the sweep record `discovery/PROBE_CONSOLIDATION.md` §1].

**Pf.**
$$(2):\ \text{the token sweep re-run against the registry (canon 640 tags; AT defs 63; IT defs 48; O-rows 38) -- the single unattested token located and corrected}\ [\text{machine record}];\ \ (3):\ \text{the two expanded forms against}\ {-}4p^3{-}27q^2\ \text{and the witness}\ [\text{machine C1}];\ \ (4):\ \text{the monomial/degree/alphabet census}\ [\text{machine G1}];\ \ (1),(5),(6),(7):\ \text{record rows}.\ \blacksquare$$

**Phys.** A study arrives from outside the wall, and the corpus does what it always does: it counts
the citations before it reads the mathematics. The count is remarkably clean — some four hundred
fifty tokens, one slip, and that one flagged by the study itself; the quotes are verbatim; even its
claim that the frozen canon contains a typo survives contact, and survives exactly where the study
said it would, in an expansion whose zero locus — the only thing the clause uses — is untouched. The
biggest open item the study left, the two objects both wearing the name rho-B, resolves without a
declaration because the canon already wore one of them: the bridge is ρ_B, the density is ρ, and the
fork inside the parametric array stays a fork, carried side by side the way the level carries every
read-choice. What the intake does NOT do is trust a single unchecked computation: the study's five
verification scripts never arrived, so every exact claim was rebuilt from the axioms of arithmetic
up — thirty-three certificates, no floating point, no inherited green.

---

### IT.50 — The channel-angle layer: the new derived rows

**Thm.**
$$(1)\quad\textbf{THE GENERAL DEMOCRATIC LAW}\ \mathcal K(N)=\tfrac2N\ \textbf{(new):}\qquad \text{for}\ \lambda_k=A+B\cos(\theta+\tfrac{2\pi k}N)\ \text{with the FT.111(3) normalizations}\ \textstyle\sum\lambda=N\ (A{=}1),\ \ \sum(\lambda{-}A)^2=N\ (B^2{=}2):$$
$$\sum\lambda^2=2N,\qquad\boxed{\ \mathcal K(N)=\frac{\sum\lambda^2}{(\sum\lambda)^2}=\frac{2N}{N^2}=\frac2N\ }\qquad[\text{machine:}\ N{=}3,4,6\ \text{exact in the trig normal-form ring};\ \text{general}\ N\ \text{by the root sums}\ \textstyle\sum\cos=0,\ \sum\cos^2=\tfrac N2\ (N\ge3)\ \text{— a math row}];$$
$$\text{at}\ N{=}3\ \text{the two twos coincide}\ (B^2{=}2{=}N{-}1):\ \ \mathrm{FT.158}(5)\ \text{'s}\ \tfrac{3-1}3\ \text{reading is exact ONLY at order 3};\qquad \mathcal K(3){=}\tfrac23\ \ \text{phase-free}\ [\mathrm{FT.119}(4);\ \mathrm{FT.143}(4);\ \mathrm{Def\text{-}BM.6}(4)]\ \text{re-derived}$$
$$(2)\quad\textbf{THE NEIGHBOUR LAW}\ R(n)=\tfrac{n+1}n\ \textbf{(new; one line from BM.114(1)):}\qquad R(n):=\frac{W_n(0)}{W_n(1)}=\frac{\binom{2n}n}{\binom{2n}{n+1}}=\frac{n+1}n\qquad[\text{machine:}\ n{=}1..12]:$$
$$\boxed{\ \mathrm{BM.28}(2)\ \text{'s ``one chain restricts}\ 2{:}1,\ \text{three chains restrict}\ 4{:}3\text{'' is ONE LAW at}\ n{=}1\ \text{and}\ n{=}3;\ \ \text{the constraint's whole effect is the descent}\ \tfrac{n+1}n\to1\ }$$
$$\text{the exhaustive}\ 4^n\ \text{charge census equals}\ W_n(Q)=\binom{2n}{n+Q}\ \text{for}\ n{=}1..4\ \ [\mathrm{BM.103}(3);\ \mathrm{BM.114}(1)];\qquad \text{the Laurent identity}\ (2{+}z{+}z^{-1})^n=(1{+}z)^{2n}/z^n\ \ \text{coefficient-wise}\ n{=}1..6;\qquad \text{the}\ n{=}1\ \text{row IS the end-pair census}\ m_q{=}(2,1,1)$$
$$(3)\quad\textbf{THE QUOTIENT UNIQUENESS AT THE CAPACITY THREE:}\qquad \frac{R(k)}{\mathcal K(k)}=\frac{(k{+}1)/k}{2/k}=\frac{k+1}2\qquad\text{and}\qquad \frac{R(k)}{(k{-}1)/k}=\frac{k+1}{k-1}\qquad[\mathrm{FT.158}(5)\ \text{'s reading}]:$$
$$\boxed{\ \text{both quotient functions hit}\ 2\ \text{UNIQUELY at}\ k{=}3\ \ (\text{machine:}\ k{=}1..12)\ \ —\ \ \text{the}\ 2\ \text{is exact arithmetic on two independently derived rationals,}\ \neg\text{a tensor-product structure,}\ \neg\text{a topological weight (register \#17)}\ }$$
$$(4)\quad\textbf{THE CUBIC LADDER (the exact sense of FT.119's ``shared cubic''):}\qquad \gamma_{\mathrm{ch}}:=\sqrt2\cos3\delta_{\mathrm{ch}}\ \ [\mathrm{BM.80}(4)]:$$
$$\boxed{\ \gamma_\ell=2\gamma_q^3-3\gamma_q\ }\qquad[\text{machine: the polynomial identity}\ \sqrt2\,T_3(x/\sqrt2)=2x^3-3x\ \text{in}\ \mathbb Q[t_2,x]/(t_2^2{-}2);\ \ 3\delta_\ell=9\delta_q=3(3\delta_q)\ [\mathrm{FT.119}(2)]];$$
$$\hat O_{q\to\ell}\ \text{acts as}\ P(x)=2x^3-3x\ (\text{a polynomial — no branch issue upward});\qquad \gamma_q\ \text{is the UNIQUE POSITIVE root of}\ 2x^3-3x-\gamma_\ell=0\ \ (\text{the quadrant certificate:}\ 3\delta_q{=}\tfrac29\in(0,\tfrac\pi2)\ \text{via}\ \pi{>}\tfrac{333}{106});$$
$$\text{the}\ \nu\text{-cubic is channel-own:}\ \ 3\delta_\nu=\tfrac38\notin\{\tfrac29,\tfrac2{27}\}\ \ [\mathrm{BM.80}(5);\ \mathrm{FT.143}(5)]$$
$$(5)\quad\textbf{THE COMPLEX SYMBOL AND THE FORCED FACTOR:}\qquad z=\tfrac1{\sqrt2}e^{\mathrm i\delta},\ \ r_k=1+z\omega^k+\bar z\omega^{-k}\ \ [\mathrm{FT.111}(2)\ \text{'s circulant}]:\qquad\boxed{\ z_\ell=2z_q^{\,3}\ }\ \ \text{with the factor}\ 2\ \textbf{FORCED}:$$
$$c\,|z_q|^3=|z_\ell|\ \ \text{at}\ \ |z|{=}\tfrac1{\sqrt2}\ \text{in both channels}\iff c^2{=}4\iff c{=}2\ (\text{unique positive rational})\ =B^2\ [\mathrm{FT.111}(3)\ \text{'s own normalization integer}];\qquad \text{argument side:}\ 3\cdot\tfrac2{27}=\tfrac29\ \ [\text{machine}]$$
$$(6)\quad\textbf{THE NEWTON TOWER AND THE z-CUBIC:}\qquad \prod_kr_k=\tfrac{\gamma-1}2,\quad \sum_kr_k^3=\tfrac{27}2+3\prod_kr_k,\quad \sum_kr_k^4=\tfrac{63}2+12\prod_kr_k\qquad[\text{machine: symbolic}\ \delta]:$$
$$\text{in}\ z_k=r_k^2:\qquad 4z^3-24z^2+(21-12\gamma)z-(\gamma-1)^2=0,\qquad \sum_kz_k=6\ \ \text{PHASE-FREE}\qquad[\text{machine: Newton's identities in}\ \mathbb Q[\gamma]]$$
$$(7)\quad\textbf{THE}\ \nu\textbf{-UNREACHABILITY AND THE CIRCLE ALGEBRA:}\qquad \hat O^{k}(\delta_\ell)=\tfrac{2}{9\cdot3^{k}}\ne\tfrac18\ \ \forall k\in\mathbb Z\qquad[\text{certificate:}\ \tfrac2{9\cdot3^k}=\tfrac18\iff16=9\cdot3^k,\ \text{impossible by}\ 3\text{-adic valuation};\ \text{machine}\ k{=}0..20]:$$
$$\text{on the lifted circle (affine maps}\ \theta\mapsto p\theta+q\pi,\ p,q\in\mathbb Q):\qquad \hat O C_3:\ \tfrac\theta3+\tfrac{2\pi}9,\qquad C_3\hat O:\ \tfrac\theta3+\tfrac{2\pi}3,\qquad\boxed{\ [\hat O,C_3]\ne0:\ \ \text{the commutator is the rotation by}\ \tfrac{4\pi}9\ }$$
$$\hat O C_3\hat O^{-1}=R_{2\pi/9}:\ \ \text{the jump DILATES the orbit generator};\qquad \text{the rhyme}\ \tfrac{2\pi}9=\pi\delta_\ell\ \ \textbf{flagged,}\ \neg\textbf{cashed}\ [\mathrm{IT.44}(3)\ \text{discipline}];\qquad \text{the lift itself is a symbolic construction — the derived content is the label arithmetic}\ [\mathrm{PJ.5}(1)]$$
$$(8)\quad\textbf{THE}\ \mathfrak P\textbf{-ARITHMETIC ROWS:}\qquad \Sigma_{\mathrm B}=\ln\tfrac{20}{15}=\ln\tfrac43=2\ln2-\ln3\in\mathfrak P;\qquad 3\ln1280-4\ln960=-\ln405\ne0\ \ [\mathrm{BM.83}(2),(3);\ \mathrm{IT.4}(1)\ \text{re-certified}]:$$
$$\textbf{the}\ \tfrac43\ \textbf{itself never becomes dimensionful;}\ \ln\tfrac43\ \textbf{does}\ \ (\Delta m_{\mathrm{transport}}=\Sigma_{\mathrm B}/\mathfrak h\in\mathfrak q^{+1/2}\ [\mathrm{Def\text{-}BM.13}(4),(5);\ \mathrm{BM.59}(4),(5)]);\qquad \text{attenuation}\ 0<\ln\tfrac43<\ln2<3\ln2\ (3<4<6<24);\qquad \tfrac{\Sigma_{\mathrm B}}{6\ln2}<\tfrac13\iff16<27$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived (new rows, machine-certified):}\ (1)\text{--}(8);\qquad\textbf{reads,}\ \neg\textbf{rows:}\ \text{the two-}C_3\ \text{identification},\ \text{the jump-factor-}=C_3\text{-order reading}\ (6);\qquad\neg\text{a declaration},\ \ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5 (Parts 1–2); FT.68(2), FT.110(1),(2), FT.111(2),(3), FT.112, FT.113, FT.116(6), FT.118(2),(6), FT.119(1),(2),(4),(5),(7), FT.142(5), FT.143(4),(5),(6), FT.158(1),(2),(4),(5), Def-H.41, Def-H.42 (Part 3); IT.4(1), IT.44(3) (this level); CT0.12, CT3.20 (Parts 1–2); BM.28(1),(2), BM.59(4),(5),(8), BM.80(4),(5), BM.83(2),(3), BM.103(3), BM.114(1),(4), Def-BM.6(4), Def-BM.13(4),(5) (Part 4); exact Fractions, trig normal-form rings, Newton's identities, Laurent coefficient identities, exhaustive censuses, rational π-certificates [math; machine: `probe_consolidation.py` §§A–B, 11/11].

**Pf.**
$$(1),(3),(6):\ \text{the trig normal-form ring}\ \mathbb Q[ct,st,t_2,t_3]/(ct^2{+}st^2{-}1,t_2^2{-}2,t_3^2{-}3)\ \text{with}\ r_k\ \text{at exact}\ 2\pi/N\ \text{offsets};\ \text{Newton's identities in}\ \mathbb Q[\gamma]\ [\text{machine A3, A4, A5}];\ \ (2):\ \text{the}\ 4^n\ \text{enumeration and the Laurent expansion}\ [\text{machine B1, B2, B3}];$$
$$(4):\ \text{the triple-angle identity in}\ \mathbb Q[t_2,x]/(t_2^2{-}2)\ [\text{machine A2}];\ \ (5):\ c^2\cdot\tfrac18=\tfrac12\ \text{in positive rationals}\ [\text{machine A7}];\ \ (7):\ \text{the valuation certificate and the affine-map compositions over}\ \mathbb Q\pi\ [\text{machine A1, A6}];\ \ (8):\ \text{coefficient vectors over the primes}\ \{2,3,5\}\ [\text{machine B4}].\ \blacksquare$$

**Phys.** Stripped of every parametric shell, the study leaves a vein of pure arithmetic the corpus
can keep. The democratic invariant generalizes: whatever the order, the Koide-form ratio is two over
N, and only at N=3 does that two coincide with the doublet dimension the seal side counts — the
corpus's exact-at-order-three reading, now with its general law and its uniqueness proof beside it.
The baryon side answers with its own one-line law: the neighbour ratio of the central binomials is
(n+1)/n, and the two famous restrictions — the end-pair two-to-one and the three-chain four-thirds —
are the same law sampled at n=1 and n=3, descending together to one. The two threes meet at the
quotient two, uniquely, and the tier says what that is: arithmetic at the capacity three, not a
tensor product, not a topology. The channel angles keep their frozen ledger, and the new connective
tissue is exact: the lepton cubic constant is a cubic polynomial in the quark one, the complex
symbol satisfies z-ell equals two z-q cubed with the two forced by the normalization itself, the
neutrino angle sits off every iterate of the jump by a three-adic valuation, and the jump does not
commute with the orbit — the commutator is a rotation by four pi over nine, computed in rationals
against pi, with the pi-delta-ell rhyme flagged and left on the table.

---

### IT.51 — The operator layer on the CT1.2 basis: the six, the nilpotents, the bridge, the reflection

**Thm.**
$$(1)\quad\textbf{THE SIX GENERATE}\ \mathfrak{su}(4)\ \textbf{(new; CT1.9's span row extended to a generation theorem):}\qquad \mathcal g=\sum_i(g_i^+J_i+g_i^-K_i)\ \ \text{spans}\ \mathcal E_{-+}\oplus\mathcal E_{--}=F_{J^+}\oplus F_{J^-}\ \ [\mathrm{A8};\ \mathrm{CT0.12}]:$$
$$\boxed{\ \operatorname{Lie}\langle J_i,K_i\rangle=\mathfrak{su}(4),\ \ \dim15,\qquad E_0\notin\operatorname{Lie}\langle J_i,K_i\rangle,\qquad \mathfrak H(\mathbb C^4)=\mathrm i\,\mathfrak{su}(4)\oplus\mathbb RE_0,\ \ 16=15+1\ }\qquad[\text{machine: the commutator closure by exact Gauss(i) elimination — rank 15, rank 16 with}\ E_0];$$
$$\text{the closure table with exact coefficients re-certified:}\ [J_i,J_j]=[K_i,K_j]=\mathrm i\epsilon_{ijk}W_k,\quad[J_i,K_j]=\mathrm i(\delta_{ij}\Sigma-E^{ij}),\quad[\Sigma,J_i]=4\mathrm iK_i,\quad[\Sigma,K_i]=-4\mathrm iJ_i,\quad[W_i,W_j]=\mathrm i\epsilon_{ijk}W_k,\quad[W_i,J_j]=\mathrm i\epsilon_{ijk}J_k,\quad[W_i,K_j]=\mathrm i\epsilon_{ijk}K_k\ [\mathrm{CT1.4};\ \mathrm{CT1.7};\ \mathrm{CT1.8};\ \mathrm{CT1.9}]$$
$$(2)\quad\textbf{THE NILPOTENT CALCULUS (new):}\qquad A_i=\tfrac12(J_i+\mathrm iK_i),\ \ B_i=A_i^\dagger=\tfrac12(J_i-\mathrm iK_i):$$
$$A_i^2=B_i^2=0,\quad A_iA_j=B_iB_j=0\ \ \forall i,j\ \ (\text{three mutually annihilating rank-one nilpotents}),\quad [A_i,A_j]=[B_i,B_j]=\{A_i,A_j\}=\{B_i,B_j\}=0,\quad \mathfrak T(A_iB_j)=\delta_{ij},\quad\mathfrak T(A_iA_j)=0;$$
$$\boxed{\ \sum_iA_iB_i=\Pi_{\mathcal R}=\tfrac14(3E_0+\Sigma),\qquad \sum_iB_iA_i=3\,\Pi_{\mathcal V}=\tfrac34(E_0-\Sigma),\qquad \sum_i[A_i,B_i]=\Sigma\ }\qquad[\mathrm{CT0.7};\ \text{machine}];$$
$$\textbf{the honest negative:}\ \ \{A_i,B_j\}\ne\delta_{ij}\mathbb1\ \ (\text{the sum is}\ \tfrac12(3E_0-\Sigma)):\ \ \textbf{fermion-LIKE,}\ \neg\textbf{Clifford}$$
$$(3)\quad\textbf{THE CASIMIRS AND THE BRANCH ASYMMETRY'S ORIGIN:}\qquad \sum_iJ_i^2=\sum_iK_i^2=\Pi_{\mathcal R}+3\Pi_{\mathcal V}=\tfrac12(3E_0-\Sigma)\ \ (\text{weights}\ (1,3));\qquad \sum_iW_i^2=2\Pi_{\mathcal R}=\tfrac12(3E_0+\Sigma)\ \ (2,0);\qquad W_i\Pi_{\mathcal V}=0\ \ [\mathrm{FT.93}(5)\ \text{re-certified}]:$$
$$\text{the}\ \text{``2 versus 0''}\ \text{branch asymmetry}\ [\mathrm{FT.93}(5);\ \mathrm{FT.141}(4)]\ \text{is these Casimir weights}\ \ [\text{machine}]$$
$$(4)\quad\textbf{THE BRANCH-CHANGE BRIDGE (new; register \#13's over-flag WITHDRAWN):}\qquad \mathbb SJ_i\mathbb S=-J_i,\ \ \mathbb SK_i\mathbb S=-K_i\ \ (\mathbb S=\text{the swap})\ \text{with}\ \Pi_{\mathcal R/\mathcal V}=\tfrac12(E_0\pm\mathbb S)\ \ \text{give}:$$
$$\boxed{\ J_i\Pi_{\mathcal R}=\Pi_{\mathcal V}J_i,\qquad K_i\Pi_{\mathcal R}=\Pi_{\mathcal V}K_i\ \ (6/6\ \text{exact})\ \ —\ \ \textbf{the six are EXACTLY the branch-changing operators}\ }$$
$$\therefore\ \ F_{J^\pm}\ \text{(subspaces)}\ \text{and the Janus}\ J^\pm\ \text{(events}\ [\mathrm{D1.2};\ \mathrm{CT0.3}])\ \text{are ONE phenomenon at two loci, two types}\ [\mathrm{FT.136}(5);\ \mathrm{FT.141}(4)\ \text{locus discipline}]:\ \ \text{a dimension count is}\ \neg\text{substituted for an event count}$$
$$(5)\quad\textbf{THE INNER REFLECTION (new):}\qquad R:=e^{\mathrm i\pi\Sigma/8}\ \ (\Sigma^2=3E_0-2\Sigma,\ \ \operatorname{spec}\Sigma=\{+1^{ \times3},-3\}):\qquad \operatorname{Ad}(R):\ \ J_i\mapsto-K_i,\ \ K_i\mapsto J_i,\ \ W_i\mapsto W_i,\ \ A_i\mapsto\mathrm iA_i,\ \ B_i\mapsto-\mathrm iB_i\ \ [\text{machine, sector-wise}]:$$
$$\operatorname{Ad}(R)^2=-\mathrm{id}\ \text{on the six},\qquad\operatorname{Ad}(R)^4=\mathrm{id}:\ \ \textbf{ORDER EXACTLY 4};\qquad R^4=e^{\mathrm i\pi\Sigma/2}=\mathrm iE_0\ \ [\text{machine: both branch phases}\ e^{\mathrm i\pi/2}];$$
$$\boxed{\ \text{the reflection is a}\ \pm\mathrm i\ \text{phase on the two nilpotent halves — it exists only AFTER complexification}\ }$$
$$(6)\quad\textbf{THE CPT AND REVERSAL ROWS (assembled):}\qquad \mathrm{CPT}\ \text{is the scalar character}\ \lambda=(-1)^{|E|}e^{\mathrm i\pi\Theta}\ \ [\mathrm{FT.134}(3)]:\ \ \operatorname{Ad}(\mathrm{CPT})X=\lambda X\bar\lambda=X\ \ \textbf{trivial on the sixteen};\ \ \text{it acts on the charge register instead}\ (Q\mapsto-Q,\ \text{the unique fixed triple}\ (0,0,0)\ [\mathrm{BM.28}(5);\ \mathrm{BM.25}]);$$
$$\hat\omega=C,\ \hat\kappa=P\ \ \text{barred — different registers}\ [\mathrm{FT.134}(1)];\qquad \text{the history reversal}\ J^+\leftrightarrow J^-\ \ \textbf{inadmissible: the reversed word leads with}\ J^-\ \text{and fails at its first event}\ [\mathrm{FT.144}(4)(\mathrm{ii});\ \mathrm{A6}:\ \neg\exists\tau^{-1}];$$
$$\text{the ledger facts stand: strict alternation, the prefix law, the Catalan relaxation, the seal excess}\ \#J^+-\#J^-=n_{\mathcal R}\ [\mathrm{BM.7}(1)]$$
$$(7)\quad\textbf{THE}\ (S,T)\ \textbf{SECTOR TABLE RE-CERTIFIED (register \#6 enforced):}\qquad E_0,\Sigma,\hat E^{ij}\ (5):\ (+,+);\quad W_i:\ (+,-);\quad J_i:\ (-,+);\quad K_i:\ (-,-);\qquad \text{sectors}\ (7,3,3,3)\ [\mathrm{CT1.1};\ \mathrm{CT1.2};\ \mathrm{CT1.12a}(1),(2);\ \mathrm{A3};\ \mathrm{C13};\ \text{machine}]$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived (new rows):}\ (1)\text{--}(5),(7);\qquad\textbf{assembled:}\ (6);\qquad\text{the six coefficients}\ g_i^\pm\ \text{are FREE — no derived value; any is a count}\to\text{strength coupling}\ [\mathrm{BM.36}(3);\ \mathrm{BM.61}(8)(\mathrm O1);\ \mathrm{BM.69}(4)(\mathrm{iv});\ \mathrm{FT.73}(5)]$$

**Req.** A3, A6, A8, C13, CT0.3, CT0.7, CT0.12 (Parts 1–2); CT1.1, CT1.2, CT1.4, CT1.7, CT1.8, CT1.9, CT1.12a(1),(2) (Part 2); D1.2, FT.93(5), FT.109(3), FT.134(1),(3), FT.136(5), FT.141(4),(5), FT.144(4) (Parts 1, 3); BM.7(1), BM.25, BM.28(5), BM.36(3), BM.61(8), BM.69(4), BM.128(5) (Part 4); IT.1(2) (this level); exact 4×4 Gauss(i) algebra, coordinate elimination, sector computations [math; machine: `probe_consolidation.py` §D, 8/8].

**Pf.**
$$(1):\ \text{the iterative commutator closure with exact rank over}\ \mathbb Q(\mathrm i)\ \text{coordinates}\ (15;\ 16\ \text{with}\ E_0);\ \text{the}\ 40+\ \text{commutation rows entrywise}\ [\text{machine D2, D3}];\ \ (2),(3):\ \text{the}\ 60+\ \text{product/trace identities entrywise, with the negative witness}\ \sum_i\{A_i,B_i\}=\tfrac12(3E_0-\Sigma)\ne E_0\ [\text{machine D4, D5}];$$
$$(4):\ \text{the six bridge identities and the two}\ \Sigma\text{-eigen rows}\ [\text{machine D6}];\ \ (5):\ \text{the sector-wise adjoint}\ \operatorname{Ad}(R)X=X_{\mathcal{RR}}{+}X_{\mathcal{VV}}{+}\mathrm i(X_{\mathcal{RV}}{-}X_{\mathcal{VR}})\ \text{on the branch phases}\ e^{\mathrm i\pi/8},e^{-3\mathrm i\pi/8};\ \text{the order-4 census and}\ R^4\ [\text{machine D7}];\ \ (6),(8):\ \text{assembly on the cited rows};\ \ (7):\ \text{the Pauli-coordinate sign census}\ [\text{machine D1}].\ \blacksquare$$

**Phys.** The six S-odd directions — the ones the metric cannot see, the tensor square cannot
reach, and the capacity does not count — turn out to be the smallest possible seed of almost
everything: commute them with themselves and the whole traceless fifteen appears, with only the
conformal mode left outside, and complexify them and they fall apart into three mutually
annihilating nilpotents whose bilinears rebuild the branch projectors exactly. The bridge is the
row the study nearly flagged away: the six are precisely the operators that move a state between the
two branches, which is what a Janus event does, so the subspace and the event are one phenomenon
recorded twice — the earlier "two different things" flag withdrawn on a machine identity. The
reflection that swaps J for K is inner, fourth-order, and only exists after complexification, being
nothing but a ±i phase on the two nilpotent halves; CPT, by contrast, is a scalar here and does its
real work on the charge register, where exactly one triple is fixed. And the honest negative is
recorded beside the positives, as the house requires: the nilpotents anticommute among themselves
but not across — fermion-like, not Clifford.

---

### IT.52 — The tensor-square occupancy and the parametric calculus: the IT.43–IT.45 class extended

**Thm.**
$$(1)\quad\textbf{THE 10-OF-16 OCCUPANCY (new):}\qquad X=M\otimes M\ \text{with}\ c_{\mu\nu}=m_\mu m_\nu\ \ [\mathrm{IT.38}(1)\ \text{pattern}]:\qquad X_{J_i}=c_{jk}-c_{kj}=0,\quad X_{K_i}=c_{0i}-c_{i0}=0\ \ \text{for EVERY}\ M\ \ [\text{machine: all pairs, symbolic}\ m]:$$
$$X=m_0^2E_0+\tfrac13\vec m^{\,2}\Sigma+\sum_i\Bigl(m_i^2-\tfrac13\vec m^{\,2}\Bigr)\hat E^{ii}+2\sum_{j<k}m_jm_k\hat E^{jk}+2m_0\sum_im_iW_i\qquad[\text{machine: the expansion on exact witnesses}];$$
$$\boxed{\ X_{E_0}=\tfrac12(\mathcal S-\mathcal T),\qquad X_{\Sigma}=\tfrac16(\mathcal S+\mathcal T)\ }\qquad\text{and}\qquad\boxed{\ \textbf{a tensor square can never carry the blocks that generate the phase}\ \ [\mathrm{IT.51}(1)]\ }$$
$$(2)\quad\textbf{THE TWO READOUTS:}\qquad \mathcal S=\sum_\mu m_\mu^2=\tfrac12\mathfrak T(M^2)=\tfrac12(a^2{+}d^2)+bc,\qquad \mathcal T=\sum_\mu\eta_\mu m_\mu^2=bc-ad=-\det M\qquad[\mathrm{A3};\ \mathrm{C13}:\ \eta=(-,+,+,+)]:$$
$$\mathcal S-\mathcal T=2m_0^2=\tfrac12(a+d)^2;\qquad \mathcal S,\mathcal T\ \text{are the Euclidean and Minkowski norms of one four-vector}\ (m_0,\vec m);\qquad \mathcal T=0\iff\det M=0\ \ (\text{the null cone is the singular locus});$$
$$\textbf{status:}\ \mathcal S,\mathcal T\ \text{as READOUTS of the array are the study's declaration (Part XI) — the identities are exact, the objects inherit the IT.43(6) doctrine: formable as symbolic expressions, barred as formed reads}$$
$$(3)\quad\textbf{THE FOUR PRICES ON THE METRIC IDENTIFICATION (the ``16 maps 1:1'' amendment, register \#9):}\qquad (\mathrm i)\ \ \text{nonlinearity:}\ g_{\mu\nu}=\Omega^2\bar g_{\mu\nu},\ \Omega=e^{\alpha_\Omega a_{00}}\ \text{—}\ a_{00}\ \text{is never a component of}\ g,\ \text{only the exponent}\ [\mathrm{D2.1};\ \mathrm{CT1.12}];$$
$$(\mathrm{ii})\ \ \text{a generic metric is}\ \neg\text{swap-even: identifying the spacetime index with the pair index imposes}\ w_1{=}w_2,\ q_{11}{=}q_{22},\ q_{13}{=}q_{23}\ \text{— three conditions cutting}\ 10\to7;\qquad (\mathrm{iii})\ \ \text{chart side vs register side}\ [\mathrm{BM.10}\ \text{obstruction discipline}];\qquad (\mathrm{iv})\ \ \text{the count}\to\text{strength bar}\ [\mathrm{BM.36}(3);\ \mathrm{BM.61}(8)(\mathrm O1);\ \mathrm{BM.69}(4)(\mathrm{iv});\ \mathrm{FT.73}(5)]:$$
$$\boxed{\ \text{the}\ 10{:}10\ \text{match is}\ X\ \text{against the COEFFICIENT FIELDS; the map to}\ g_{\mu\nu}\ \text{leaves the subspace — the identification is}\ \neg\text{adopted}\ }$$
$$(4)\quad\textbf{THE PHASE CALCULUS (exact; the parametric layer of the class):}\qquad a=\mu_qr_i(\delta_q)^2,\ d=\mu_\ell r_j(\delta_\ell)^2\ [\mathrm{FT.113};\ \mathrm{FT.119}(5)\ \text{shapes};\ \mu\ \text{'s undeclared}]:\ \ \text{the tower}\ r^{(2m)}=(-1)^{m+1}(1-r),\ r^{(2m+1)}=(-1)^mr'\ (\text{from}\ r''=1-r;\ \text{machine}\ m{=}1..6);$$
$$a''=2\mu(1+3r-2r^2);\qquad \sum_kr_k'=\sum_kr_kr_k'=\sum_k\bigl[(r_k')^2+r_kr_k''\bigr]=0\ \ \text{identically at every phase}\ \Rightarrow\ \ \sum_ka_k=6\mu,\ \sum_ka_k'=\sum_ka_k''=0\ \ [\text{machine}];$$
$$\textbf{the four corrected cells (register \#1):}\ \ (\partial_qX)_{(12),(12)}=(\partial_qX)_{(21),(21)}=a'd\ \ (\neg0),\ \text{likewise}\ ad',\ a''d,\ ad'';\qquad \partial_q\partial_\ell X=\operatorname{diag}\text{-cells}\ a'd'\ \text{at exactly TWO of sixteen}:$$
$$\text{the readout table:}\ \ \partial_q\mathcal S=aa',\ \partial_\ell\mathcal S=dd',\ \partial_q\mathcal T=-da',\ \partial_\ell\mathcal T=-ad',\ \ \partial_q\partial_\ell\mathcal S=0,\ \ \partial_q\partial_\ell\mathcal T=-a'd':\ \ \mathcal S\ \text{has NO cross-curvature,}\ \mathcal T\ \text{ONLY the cross term}\ [\text{machine: all five Leibniz forms entrywise}]$$
$$(5)\quad\textbf{THE CONSTRAINED FLOW AND THE SINGULAR LOCUS:}\qquad \delta_\ell=n\delta_q\ \Rightarrow\ \tfrac{d}{d\delta}=\partial_q+n\partial_\ell:\qquad \frac{d^2\mathcal T}{d\delta^2}=-\bigl(da''+2n\,a'd'+n^2ad''\bigr)\qquad[\text{machine:}\ n{=}1..6;\ \text{register \#5's}\ 27\to9\ \text{correction certified at}\ n{=}3]:$$
$$\det J_\Phi=-a'd'(a^2-d^2)\ \ (\text{singular iff}\ a'{=}0\ \vee\ d'{=}0\ \vee\ a{=}\pm d);\qquad \det H_{\mathcal T}=ad\,a''d''-(a'd')^2;\qquad \partial_q\lambda_\pm=\tfrac{a'}2\Bigl[1\pm\tfrac{a-d}{\sqrt\Delta}\Bigr],\ \ \partial_\ell\lambda_\pm=\tfrac{d'}2\Bigl[1\mp\tfrac{a-d}{\sqrt\Delta}\Bigr]\ \ [\text{machine: the implicit-differentiation certificate in}\ \mathbb Q[a,b,c,d,a',s]/(s^2{-}\Delta)]:$$
$$\text{at the sharp threshold}\ c=\varepsilon_q=0:\ \ \sqrt\Delta=|a-d|,\ \text{the bracket}\ \in\{0,2\}:\ \ \textbf{each phase moves exactly one eigenvalue, the branch selected by}\ \operatorname{sign}(a-d)$$
$$(6)\quad\textbf{THE ORDER-3 FACTS:}\qquad \text{in}\ M\otimes M\ \text{every cell is a product of exactly two diagonal letters}:$$
$$\boxed{\ \partial_q\partial_\ell\partial_\nu(M\otimes M)=0\ \ \text{identically (all 81 cells)},\qquad \partial_q\partial_\ell\partial_\nu(ade)=a'd'e'\ne0\ \ \text{in}\ M^{\otimes3}\ }\qquad[\text{machine}];$$
$$\partial_q\partial_\ell\mathcal T_3=-a'd'e\ \ (\text{and cyclic}):\ \ \textbf{the order of the tensor power decides how many channel angles can meet in one number — three pairwise couplings, no triple, until the cube}$$
$$(7)\quad\textbf{THE INDEX-READING INCOMPATIBILITY (a theorem, not a preference):}\qquad \text{on a colour-sealed composite}\ \mathfrak T(H)=3a\ \text{and}\ 1+\omega+\omega^2=0\ \text{annihilates the doublet datum}\ [\mathrm{FT.117}(1);\ \mathrm{BM.1}(2);\ \mathrm{BM.57}(6),(8)],\ \text{colour}\ \neg\text{observable}\ [\mathrm{CT3.22}],\ \text{the seed colour-blind}\ [\mathrm{EW.32}]:$$
$$\boxed{\ \text{a slot-indexed read of a sealed composite cannot carry three distinct diagonal values}\ }\qquad\text{the survivors at order 3:}\ \mathcal S,\mathcal T\ \text{(value yes, meaning no — there is no}\ \eta),\ \ \partial\mathfrak T(M^2)=2\mathfrak T(M\partial M),\ \ \text{Jacobi},\ \ \partial\lambda_k=y_k^\dagger(\partial M)y_k\ \text{for normal}\ M$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived (symbolic identities):}\ (1),(4),(5),(6),(7);\qquad\textbf{declared by the study,}\ \neg\textbf{adopted:}\ \text{the array}\ M,\ \text{its index space,}\ \mathcal S,\mathcal T\ \text{as readouts, the order-3 filling and line choices}\ [\mathrm{IT.37}\text{--}\mathrm{IT.39};\ \mathrm{IT.43}\text{--}\mathrm{IT.45}\ \text{class};\ \text{the study's own Part XI concurs}];\qquad\neg\text{a declaration issued}$$

**Req.** P1, P4, P5, A3, C13, CT0.12 (Parts 1–2); CT1.12, CT1.12a(1),(2), D2.1, EW.32 (Part 2); FT.79(5), FT.113, FT.117(1), FT.119(5) (Part 3); IT.37(1), IT.38(1),(2), IT.43(3),(4),(5),(6), IT.44(4), IT.45(5), IT.51(1) (this level); BM.1(2), BM.10, BM.36(3), BM.57(6),(8), BM.61(8), BM.69(4), BM.102(4), CT3.22 (Part 4); the jet-derivation algebra, the implicit-differentiation certificate, the 81-cell census [math; machine: `probe_consolidation.py` §§D8, E, 7/7].

**Pf.**
$$(1):\ \text{the symbolic Pauli coefficients}\ c_{\mu\nu}=m_\mu m_\nu;\ \text{the}\ J/K\ \text{antisymmetry census over all pairs; the basis expansion on three exact witnesses}\ [\text{machine D8}];\ \ (4),(5):\ \text{the jet derivation}\ \partial_q:\ a\mapsto a'\mapsto a''\mapsto0\ \text{(and}\ \partial_\ell\ \text{on}\ d)\ \text{applied to}\ M\otimes M\ \text{by Leibniz, entrywise against the five claimed forms; the flow coefficients}\ (1,2n,n^2);\ \det J_\Phi,\ \det H_{\mathcal T}\ \text{expanded};\ \text{the eigenvalue certificate by implicit differentiation of the characteristic polynomial}\ [\text{machine E1--E5}];$$
$$(6):\ \text{the}\ 9\times9\ \text{cell census under}\ \partial_q\partial_\ell\partial_\nu\ \text{and the}\ ade\ \text{cell of the cube}\ [\text{machine E6}];\ \ (2),(3),(7),(8):\ \text{record rows on the cited clauses}.\ \blacksquare$$

**Phys.** The parametric matrix the study kept at arm's length — declared, never derived, exactly as
Tiers IT.12 and IT.14 adjudicated its predecessors — still pays rent, and the rent is exact. Its
tensor square lives in ten of the sixteen directions and provably cannot touch the six that
generate everything else: the phase-making blocks are structurally outside any tensor square, which
is the cleanest statement yet of why the array cannot be the force. The metric rhyme survives with
four prices attached, and the tier pays none of them: ten against ten is a match of coefficient
fields, not of metrics, because a generic metric fails swap-evenness on three explicit conditions.
The calculus layer is honest symbolic algebra over undeclared slots — the tower that never grows,
the family sums that vanish at every phase, the four cells a careless Leibniz once zeroed, the
constrained flow with its (1, 2n, n²) signature, the sharp threshold where each phase moves exactly
one eigenvalue — and at order three the structural gem: two-fold tensor powers cannot host a triple
channel meeting, three pairwise couplings and no triple until the cube. None of it is a formed
read; all of it is now on the record, certified, and bounded by the bars it never crossed.

---

### IT.53 — The saturated node, the Lyapunov layer, and the radar: the agreement conditions

**Thm.**
$$(1)\quad\textbf{THE SATURATED NODE (assembly, re-certified):}\qquad n(v)=3\Rightarrow D_{\mathrm{tick}}(3)=16=C_{\mathrm{cap}},\ \ O(3)=0\ \ [\mathrm{CT0.6};\ \mathrm{CT0.11};\ \mathrm{CT4.1}]:\qquad \rho_v=\rho_\circ=\tfrac14I_4\ \ [\mathrm{A5}];$$
$$|\Pi_{\mathcal V}\rho_\circ|=\tfrac14\notin[0,\varepsilon_q]\cup[1{-}\varepsilon_q,1]\ \ \forall\varepsilon_q\in[0,\tfrac14)\ \ [\mathrm{A4};\ \mathrm{CT0.8};\ \text{machine: witness sweep incl.}\ \varepsilon_q=\tfrac14-10^{-6}]\ \ \Rightarrow\ \ \textbf{every channel virtual},\ |R|{=}0,\ n_{\mathcal V}{=}2E,\ \Delta{=}3E\ \ (\text{re-certifies IT.3(2)'s ``all-virtual''});$$
$$\text{isotropy}\ (w_i{=}0,\ \hat h_{ij}{=}0):\ \ \text{of}\ \dim\mathcal K_3=25\ \text{and the metric's ten coordinates, TWO survive}\ (\Sigma_{\mathrm{tr}},\ a_{00}):\ \ g_{\mu\nu}=\Omega^2\operatorname{diag}(-1,1+\varkappa h,1+\varkappa h,1+\varkappa h)\ [\mathrm{D2.1};\ \mathrm{CT1.12}]$$
$$(2)\quad\textbf{THE REDUCTIO (conditional on the study's DECLARED isotropy transport):}\qquad \text{transporting isotropy through the}\ X\leftrightarrow X_{(+)}\oplus X_{(-)}\ \text{dictionary forces}\ \tilde m_1=\tilde m_2=\tilde m_3=0,\ \text{hence}\ \tilde b=\tilde c=0,\ \tilde a=\tilde d:\ \ M=\tilde aI_2:$$
$$\tilde c=\varepsilon_q=0\ \ \text{is the sharp specialization, fine};\qquad \tilde b=0\ \ \text{is}\ \neg\text{available}\ (\rho=\mathfrak h^{-4}E^4(\ln2)^4>0\ [\mathrm{BM.14}(2)];\ \ \rho_{\mathrm B}\ \text{'s value}\ \neg\text{issued} [\mathrm{A\text{-}BM.9}]\ \text{— setting it to zero WOULD issue one}):$$
$$\boxed{\ \text{at the saturated isotropic node, the DECLARED dictionary and a nonzero interface cannot both hold}\ }\qquad[\text{conditional: the transport is the study's declaration, not a row}];$$
$$\text{the six are untouched by all of it — no metric coordinates}\ [\mathrm{FT.141}(5)],\ \neg\text{producible by}\ X\ [\mathrm{IT.52}(1)],\ \text{present from rung 0}\ [\mathrm{A8};\ \mathrm{CT0.13}:\ \mathcal A(0)=\{J\}]$$
$$(3)\quad\textbf{THE LYAPUNOV LAYER:}\qquad V\mapsto(1-\tfrac\gamma4)^2V,\ \ \text{deficit}\ \tfrac{\gamma(8-\gamma)}{16},\ \ (1-\tfrac\gamma4)^2+\tfrac{\gamma(8-\gamma)}{16}=1\ \ \text{EXACTLY in}\ \mathbb Q[\gamma]\ \ [\mathrm{BM.8}(2);\ \text{machine}]:$$
$$\text{the zero locus}\ \{0,8\};\qquad \gamma=1:\ \bigl(\tfrac9{16},\tfrac7{16}\bigr),\ \ \bigl(\tfrac9{16}\bigr)^6=\tfrac{531441}{16777216}\ \ [\text{machine}];\qquad \text{the tilt fixes}\ \rho_\circ\ \text{at every}\ \gamma\ [\mathrm{L0};\ \mathrm{L2}];$$
$$\boxed{\ \lambda_{\mathrm{jump}}=2\ln(1-\tfrac\gamma4)\ \ \text{is DIRECTION-BLIND: the contraction carries no channel angle — a real jump contracts like any real edge, and at}\ \rho_\circ\ \text{NO real jump can occur (all channels virtual)}\ }$$
$$(4)\quad\textbf{THE RADAR FACES (the definitional object under the IT.31 §0 stance):}\qquad \text{hop face:}\ d=\delta h\in\mathbb N\ \ [\mathrm{D0.6};\ \mathrm{EM.7}];\qquad \text{tick face: per-edge}\ \Delta\tau=2\delta h\ \text{vs per-visit}\ 2\delta h-1\ \ [\mathrm{D0.7};\ \mathrm{C11}]\ \ —\ \ \textbf{BOTH EXACT, NEITHER FROZEN}\ (\mathrm{D\text{-}RS3}\ \text{owed});$$
$$\text{chart face:}\ \ d\tau_\pm=\frac{\sqrt{g_{xx}}\,dx}{N\mp s},\ \ s=\sqrt{g_{xx}}N^x:\ \ \text{the exact roots of BM.34(2)'s null condition per leg sign (machine, cross-multiplied)};\qquad \text{radar half-distance}=\frac{\sqrt{g_{xx}}\,dx\,N^2}{N^2-s^2}=\ \text{the proper length EXACTLY at}\ s=0;$$
$$\text{anchor face:}\ \ \Delta x_{\mathrm B}=\mathfrak h/(E_{\mathrm{int}}\ln2)\ \text{sub-hop}\ [\mathrm{Def\text{-}BM.4}(1),(5)],\ \ \Delta x_{\mathrm B}r_s=\mathfrak h^2/(2\ln2)\ E\text{-free}\ [\mathrm{BM.17}(3);\ \mathrm{IT.31}(1)];\qquad\boxed{\ \neg\text{a new dimensionful scale enters any face}\ [\mathrm{P1};\ \mathrm{Def\text{-}BM.4}(2)]\ }$$
$$(5)\quad\textbf{THE AGREEMENT CONDITION (three grounds):}\qquad (\mathrm a)\ \ \textbf{ledger:}\ \text{the formed two-body object counts RETURN words only — all odd elements vanish}\ [\mathrm{AT.44}(1);\ \text{machine}:\ \text{closed form vs brute force}],\ N_k(2m)\ \text{is endpoint-blind,}\ (x_+x_-)^m\ \text{commutative}:$$
$$\boxed{\ d_{e\to p}=d_{p\to e}\ \ \text{INSIDE the formed object is not a condition but a consequence: both names read the SAME return word}\ }\qquad(\text{the photon}\leftrightarrow\text{return-word identification itself is}\ \mathrm{D\text{-}RS2},\ \text{owed});$$
$$(\mathrm b)\ \ \textbf{chart:}\ \ d\tau_+-d\tau_-=\frac{2\sqrt{g_{xx}}\,dx\,s}{N^2-s^2}\ \ [\text{machine}]:\ \ \boxed{\ \text{agreement}\iff s\cdot dx=0\ \ \text{(the shift projection along the link vanishes)}\ }\ \ \wedge\ \text{static fields (the stationarity hypothesis — a DECLARED theorem-local scope}\ [\mathrm{BM.8}(2)];\ \mathrm{D\text{-}RS4}\ \text{owed to instantiate)};$$
$$\neg\text{metric symmetry alone}\ (g_{ij}=g_{ji}\ \text{does not kill}\ 2N_idx^id\tau),\ \ \neg\text{the shared null cone alone (the shift TILTS the cone)};\qquad w\mapsto-w\ \text{flips}\ s\ \text{and swaps}\ d\tau_+\leftrightarrow d\tau_-:\ \ \textbf{the two syncs are T-conjugate reads}\ [\mathrm{BM.34}(3);\ \mathrm{FT.156}(3);\ \text{machine}];$$
$$(\mathrm c)\ \ \textbf{one ledger:}\ \ \mathfrak L\ \text{is ONE ordered record}\ [\mathrm{D0.7};\ \mathrm{A7};\ \mathrm{D1.8}]:\ \ \text{the two ``syncs'' are two reads of one ledger — no cross-clock convention exists or is needed}$$
$$(6)\quad\textbf{THE DISJOINTNESS ROW (new):}\qquad \text{at the saturated isotropic node}\ w_i=0\Rightarrow s=0\Rightarrow\text{reciprocity AUTOMATIC}\ (1);\ \ \text{but there ALL channels are virtual}\ \Rightarrow n_{\mathrm{real\_out}}=0\Rightarrow\neg\text{real legs fire}\ [\mathrm{A5};\ \mathrm{A6};\ \mathrm{CT0.8}]:$$
$$\boxed{\ \text{the node where agreement is GUARANTEED is the node where the radar CANNOT RUN; where real legs can run, agreement holds only under}\ s{=}0\ \wedge\ \text{stationarity}\ }$$
$$(7)\quad\textbf{THE EXTRACTION (assembly of formed rows):}\qquad \text{when the syncs agree, the read is the}\ \chi\text{-gated,}\ (x_+x_-)\text{-weighted zig-zag conversation on the shared connector floor}\ [\mathrm{AT.42};\ \mathrm{AT.44};\ \mathrm{BM.121}(2);\ \mathrm{BM.134}(5);\ \mathrm{IT.43}(7)],\ \ \text{origin-blind}\ (5),$$
$$\text{geometrically the Born-width ladder}\ \{\mathfrak h/(2j\ln2)\}\ \text{with the}\ E\text{-free invariant}\ [\mathrm{AT.42}(3);\ \mathrm{BM.17}(3)],\ \ \text{spectrally the}\ 1/d^2\ \text{pole ladder with its two agreeing routes}\ [\mathrm{AT.44}(5),(6)],\ \ \text{registered inter-system ONLY as the boundary-exact charge read}\ [\mathrm{IT.1}(6);\ \mathrm{EM.9b}]:$$
$$\boxed{\ \textbf{the radar protocol is a CANDIDATE formalization of IT-O3's operational semantics — recorded,}\ \neg\textbf{adopted; IT-O3 stays OPEN}\ }\qquad[\mathrm{IT.44}(7);\ \mathrm{IT.1}(5)]$$
$$(8)\quad\textbf{THE BARS (re-stated with grounds):}\qquad \text{the DYNAMICAL radar/photon-mediated jump is barred as formed — three grounds (O1 chiral-blind gauge blocks; O2 deficit}\ 1';\ \text{O4 no winding carrier; O3 discharged}\ [\mathrm{BM.134}(7)])\ [\mathrm{IT.40}\text{--}\mathrm{IT.42};\ \mathrm{BM.6}(6)];\qquad \text{the geometric/reading radar is admissible iff DECLARED a read}\ [\mathrm{IT.3}(6);\ \mathrm{Def\text{-}H.19}];$$
$$\text{the}\ O(n)\ \text{analytic continuation:}\ \widetilde O(z)=2^{z+1}-16,\ \ \widetilde O(3)=0\ \ (\text{the last admissible rung}),\ \ \widetilde O'(3)=16\ln2,\ \ z_k=3+\tfrac{2\pi\mathrm ik}{\ln2}\ \ \textbf{RECORDED AND SCOPED OUT — rungs are integers}\ [\mathrm{CT0.11};\ \mathrm{CT4.4a}]$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(3),(5)(\mathrm a),(\mathrm b)\ \text{as exact conditionals},(6),(8)\ \text{'s continuation record};\qquad\textbf{conditional on declared transports:}\ (2);\qquad\textbf{owed:}\ \mathrm{D\text{-}RS1}\text{--}\mathrm{D\text{-}RS4};\qquad\neg\text{a declaration issued}$$

**Req.** A4, A5, A6, A7, A8, CT0.3, CT0.6, CT0.8, CT0.11, CT0.12, CT0.13, CT0.14, C11, D0.6, D0.7, D0.8, D1.8, D2.1 (Parts 1–2); CT1.12, CT2.6, D2.6, EM.7, EM.9b, FT.141(5), FT.156(3), L0, L2, Def-H.19 (Parts 2–3); IT.1(5),(6), IT.3(2),(6), IT.31(1), IT.32(3), IT.40–IT.42, IT.43(7), IT.44(7), IT.51, IT.52(1), IT-O3 (this level); AT.41(2), AT.42(1),(2),(3), AT.44(1),(2),(5),(6), AT.63(2) (Level 5); BM.8(2), BM.14(2), BM.17(3), BM.34(1),(2),(3), BM.121(2), BM.134(5),(7), BM.137(1), Def-BM.4(1),(2),(5), A-BM.9, CT3.22, CT4.1, CT4.4a (Parts 2, 4); rational-function identities, the witness sweep, the enumeration [math; machine: `probe_consolidation.py` §§F1–F4, 4/4].

**Pf.**
$$(1):\ \text{the rational witness sweep of}\ \tfrac14\ \text{against}\ [0,\varepsilon_q]\cup[1{-}\varepsilon_q,1];\ \text{the integer censuses}\ O(n),\ D_{\mathrm{tick}},\ \text{the lock biconditional, the ladder}\ 6,16,17,25\ [\text{machine F2}];\ \ (3):\ \text{the}\ \mathbb Q[\gamma]\ \text{identity, the zero locus, the exact powers}\ [\text{machine F1}];$$
$$(4),(5)(\mathrm b):\ \text{the null-quadratic root check per leg sign and the sum/difference/half-distance/proper-length identities, cross-multiplied in}\ \mathbb Q[G,dx,N,s];\ \text{the T-conjugacy by exact substitution}\ [\text{machine F3}];\ \ (5)(\mathrm a):\ \mathrm{AT.44}(1)\ \text{'s parity re-certified against brute force}\ [\text{machine record}];\ \ (8):\ \widetilde O(3)=0\ \text{and the integer values}\ [\text{machine F4}];\ \ (2),(6),(7),(9):\ \text{assembly on the cited rows}.\ \blacksquare$$

**Phys.** The saturated node is the corpus's stillest place and this tier measures exactly how
still: every channel virtual, isotropy killing eight of the metric's ten coordinates, the tilt
fixing the quarter-identity at every flicker, and a Lyapunov law that contracts without ever asking
which direction it was told. The study's reductio is honest about its own footing — transport the
declared dictionary to the node and a nonzero interface dies, but the transport is a declaration, so
the reductio is conditional and says so. The radar then gets the treatment the house reserves for
borrowed vocabulary: four faces, three of them exact and P1-clean, one — the tick face — carrying two
exact readings and no frozen choice. The agreement the brief demanded comes out three times over
and in no way the brief expected: on the ledger it is not a condition but a consequence, because the
only formed two-body object counts returns and returns have no origin; on the chart it is the
vanishing of the shift projection, with metric symmetry and the shared null cone both insufficient;
and over both stands the fact that there was never a second clock. The sharpest row is the
disjointness: reciprocity is guaranteed precisely where nothing real can fly. And the whole protocol,
dynamics barred and geometry declared, is recorded where it belongs — as a candidate semantics for
the open handshake row, not as its closure.

---

### IT.54 — The consolidation verdict: the derived/declared/barred separation, the declaration register, and the placement

**Thm.**
$$(1)\quad\textbf{THE VERDICT TABLE (families; the full 29+23-row tables live in the PJ/RS records):}\qquad\begin{array}{l|l}\textbf{family}&\textbf{status}\\\hline\text{the angle ledger, the cubic ladder, the Koide layer, the neighbour law, the quotient uniqueness}&\textbf{DERIVED (new rows)}\ [\mathrm{IT.50}]\\\text{the six generate}\ \mathfrak{su}(4);\ \text{the nilpotent calculus; the Casimirs; the bridge; the reflection; CPT triviality}&\textbf{DERIVED (new rows)}\ [\mathrm{IT.51}]\\\text{the 10-of-16 occupancy; the phase calculus; the order-3 facts; the index incompatibility}&\textbf{DERIVED as symbolic identities OF the parametric class}\ [\mathrm{IT.52}];\ \text{the array itself DECLARED}\ [\mathrm{IT.37}\text{--}\mathrm{IT.39};\ \mathrm{IT.43}\text{--}\mathrm{IT.45}]\\\text{the saturated-node census; the Lyapunov rows; the agreement grounds; the disjointness row}&\textbf{DERIVED}\ [\mathrm{IT.53}];\ \text{the reductio CONDITIONAL on the declared transport}\\\text{the radar as IT-O3 semantics}&\textbf{CANDIDATE — recorded,}\ \neg\text{adopted};\ \mathrm{IT\text{-}O3}\ \text{OPEN}\\\text{the metric identification (10:10)}&\neg\text{ADOPTED — four prices}\ [\mathrm{IT.52}(3)]\\\text{the dynamical radar / photon-mediated jump / rider readings}&\textbf{BARRED as formed — three grounds}\ [\mathrm{IT.40}\text{--}\mathrm{IT.42};\ \mathrm{IT.44}(6)]\\\text{the two-}C_3\ \text{identification; the jump factor}=C_3\ \text{order; any Fourier/information reading of the capacity}&\textbf{UNTAGGED READINGS / NEW DECLARATION GRADE}\ [\mathrm{FT.116}\ \mathrm{Phys};\ \mathrm{FT.143}(6);\ \mathrm{D0.9};\ \mathrm{C10}]\end{array}$$
$$(2)\quad\textbf{THE DECLARATION REGISTER (absorbed; named}\ \neg\textbf{invented; none forced, none issued):}\qquad (\mathrm{D\text{-}PJ1})\ \text{the tick-order of the channel angles};\ (\mathrm{D\text{-}PJ2})\ \text{an ``angle quantum state'' object — or the withdrawal of the operator framing to the label map}\ [\mathrm{Def\text{-}H.41}/\mathrm{Def\text{-}H.42}\ \text{bars stand}];$$
$$(\mathrm{D\text{-}PJ3})\ \text{the mediation direction — admissible only alongside the IT-O1 package};\ (\mathrm{D\text{-}PJ4})\ \text{the event classification of each direction}\ (J^\pm\text{-type / tick / inert)};\ (\mathrm{D\text{-}PJ5})\ \text{the general-circle branch rule};\ (\mathrm{D\text{-}PJ6})\ \text{a rider reading-type}\ [\mathrm{IT.44}(6)\ \text{stands until such an act}];\ (\mathrm{D\text{-}PJ7})\ \text{[standing] the IT-O1 package}\ [\mathrm{IT.41}(2)];$$
$$(\mathrm{D\text{-}RS1})\ \text{the pre/post-tick relational reading (against C11's inverted node-level lifecycle — the conflict LOGGED)};\ (\mathrm{D\text{-}RS2})\ \text{``radar'' as a definitional act}\ (\text{photon}\leftrightarrow\text{return-word)};\ (\mathrm{D\text{-}RS3})\ \text{the tick--hop exchange rate};\ (\mathrm{D\text{-}RS4})\ \text{the stationarity scope off saturation};\ (\mathrm{D\text{-}RS5})\ \text{a rider read-type};\ (\mathrm{D\text{-}RS6})\ \text{[standing] the IT-O1/IT-O3 package};$$
$$\text{plus the study's Part-XI list: the array and its index space;}\ \mathcal S,\mathcal T\ \text{as readouts;}\ \mathcal g\ \text{and its six free coefficients}\ g_i^\pm;\ \ \text{``uniform''}:=\rho_\circ;\ \ \text{the isotropy transport; the channel-index-as-spatial reading; the order-3 filling and line choices;}\ \kappa=\mathfrak h^4\mu_\ell\ \text{as the det weight; the}\ b\text{-slot fork}\ [\mathrm{IT.49}(4)]$$
$$(3)\quad\textbf{THE PLACEMENT:}\qquad \text{Level 6 — the open level (Level 5 closed, cited never edited}\ [\mathrm{AT.63}(2)]):\ \text{the operator/angle layers extend}\ \mathrm{CT1.9}/\mathrm{FT.111}\text{--}\mathrm{FT.119}/\mathrm{AT.56}\text{--}\mathrm{AT.58}\ \text{from the open level with NO conflict (pure extensions; no supersession)};$$
$$\text{the matrix layer joins the}\ \mathrm{IT.37}\text{--}\mathrm{IT.39}/\mathrm{IT.43}\text{--}\mathrm{IT.45}\ \text{parametric construction class};\qquad \text{the radar joins IT-O3 as a recorded candidate};\qquad \text{the era chain holds: Parts 1--4, Level 5, and earlier IT-tags only}\ [\text{machine: the gate's F3}]$$
$$(4)\quad\textbf{THE BARS (all standing, all with grounds):}\qquad \text{count}\to\text{strength}\ [\mathrm{BM.36}(3);\ \mathrm{BM.61}(8)(\mathrm O1);\ \mathrm{BM.69}(4)(\mathrm{iv});\ \mathrm{FT.73}(5)];\quad \alpha_B\ [\mathrm{BM.61}(8)];\quad \text{Ansatz-B}\ \alpha\ [\mathrm{BM.59}(7)];\quad \text{a second dimensionful scale}\ [\mathrm{P1}];\quad \text{a complex rung}\ [\mathrm{CT4.4a}];\quad \text{species identification}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)];\quad \text{amplitude}{=}\text{mass}\ [\mathrm{FT.79}(5)];\quad \text{rung}{=}\text{scale}\ [\mathrm{D0.8}];\quad \text{cross-currency sums/conversions as formed reads}\ [\mathrm{BM.83};\ \mathrm{BM.140}(5);\ \mathrm{IT.43}(6)];\quad \text{``perspectives'' as primitives}\ [\mathrm{IT.44}(6)];\quad \text{Shannon readings of the capacity}\ [\mathrm{D0.9};\ \mathrm{C10}]$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\neg\text{a P4 addition adopted},\quad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\quad\neg\text{a measured value}\ [\mathrm{P5}],\quad\neg\text{a species identification},\quad\neg\text{a route adoption}\ [\mathrm{BM.30}(5)];\qquad §\mathrm{Cal\text{-}IT}\ \text{stays empty};$$
$$\textbf{the open rows:}\ \ \mathrm{IT\text{-}O3}\ \text{gains the recorded radar candidate and stays OPEN; no new row; the rest unchanged}\ [\mathrm{IT\text{-}O1}\ \text{three grounds/deficit}\ 1'\ [\mathrm{IT.41}];\ \mathrm{IT\text{-}O2}\ \text{value};\ \mathrm{IT\text{-}O5};\ \text{the owed route choice}\ [\mathrm{IT.14}(3)];\ \text{the deferred Calibration Era}\ [\mathrm{AT.63}(4)]]$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{probe\_consolidation.py}\to\textbf{33/33 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{17 checkers, 276 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{16 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad \text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and the consolidation adopts exactly what the arithmetic certified}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P4, P5 (Parts 1–2); D0.8, D0.9, C10, CT4.4a (Parts 1–2); Def-H.41, Def-H.42, FT.73(5), FT.79(5), FT.116, FT.143(6) (Part 3); IT.14(3), IT.37–IT.39, IT.40–IT.42, IT.43(6), IT.44(3),(6),(7), IT.45(5), IT.49–IT.53, IT-O1, IT-O2, IT-O3, IT-O5 (this level); AT.39(8), AT.63(2),(4) (Level 5); BM.6(4), BM.30(5), BM.36(3), BM.59(7), BM.61(8), BM.69(4), BM.83, BM.140(5), Def-BM.3(7) (Part 4); the assembly rows [math; machine: the full checker + the level runner + the level gate re-run end to end].

**Pf.**
$$(1)\text{--}(4):\ \text{the row-wise assembly of IT.49--IT.53 with every status traced to its certifying marker or its frozen ground};\ \ (5)\text{--}(7):\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** A study that ran outside the wall is now inside it, and the customs inspection kept what
could pay. The arithmetic vein — the general democratic law, the neighbour law, the unique quotient
at three, the cubic ladder, the forced factor two, the four-pi-over-nine commutator — enters as
derived rows with certificates that can fail and did not. The operator vein enters with it: six
generators closing on fifteen dimensions, three mutually annihilating nilpotents rebuilding the
branch projectors, the bridge that retires an over-flag, the fourth-order inner reflection, and the
honest negative that the triple is fermion-like rather than Clifford. The parametric vein enters as
what it always was — a declared container whose symbolic calculus is exact and whose readings stay
barred — and the matrix the study kept rebuilding is now visibly the same class the level declined
twice. The radar joins the open handshake row as a candidate semantics, not a closure. Thirteen
declarations are named and none is issued; ten bars are restated with their grounds; one canon typo
is recorded for the closure pipeline and nothing frozen is touched. The corpus is bigger by exactly
what the arithmetic certified, and not by one imagined row.

---

## §Cal-IT — unchanged from Tier IT.16

**Empty at this tier.** The consolidation ISSUES NO DECLARATION: the thirteen named acts
(D-PJ1–7, D-RS1–6) and the study's Part-XI declaration list (the array and its index space; the
𝒮,𝒯 readouts; g and its six free coefficients — a count→strength coupling absent an act; the
isotropy transport; the b-slot fork; the order-3 choices; κ=𝔥⁴μ_ℓ) are RECORDED as owed, none
forced, none issued [BM.6(4) pattern]. The inherited owed declarations stand unchanged — the
mass-read route choice [IT.14(3); BM.30(5)], 𝔥 (P1), ε_q (AT-O27), e₀ (EM.25(7), ¬issued),
(ϰ,β) (AT-O3), ρ_B, μ̂'², σ_ℓ, σ_ν (¬declared; A-BM.9's slot), the P4 transport profile, the lift
and the vielbein (AT.60), and the read rules (M1′)–(M3′) [AT.54(6)]. No probe-side decimal enters
any record [P5]; the canon's enclosures stand [FT.113; FT.119(5)].

## §Open-IT additions from Tier IT.16

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.16 opens **no new row**. IT-O3 (the handshake-indicator operational theory) GAINS a recorded candidate formalization: the two-photon radar protocol — the agreement read (the χ-gated, (x₊x₋)-weighted zig-zag on the shared connector floor, origin-blind by the return-word structure), admissible as a READ only under D-RS2 and barred as dynamics on the three IT-O1 grounds. **IT-O3 stays OPEN.** The FT.116(5) typo observation is queued for the Era-2-closure erratum pipeline [AT.63(4)], ¬an open row | IT.53(7),(8); IT.49(3); PJ.10; RS.6 |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4)]: (IT-O1) the formed transit-leg amplitude
— open on three grounds, the missing primitive deficit 1′ [IT.41]; (IT-O2) the N≥4 multi-seal
configuration calculus — the binding value; (IT-O3) the handshake-indicator operational theory;
(IT-O5) the isotope cutoff — the empirical/dynamical side at IT-O1; the owed route choice
[IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the Level-5 inheritance [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.17: the declaration package — D-PJ/D-RS issued, deferred, and bar-checked (the first logged declaration acts of Level 6)

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.17 — the Architect's directive to ISSUE the
phase-jump / radar-sync declaration package (D-PJ1–7, D-RS1–6, the BM.113(6) sector sync, and the
$\rho_{\mathrm B}$/$e_0$ re-confirmation) into the corpus's declaration census: record each act,
verify that issuing violates no standing bar (P1, P5, the transit bar, the incommensurability bar,
the arena bars Def-H.41/42, count$\to$strength), update the register from owed to issued/deferred.
These are the **FIRST declaration acts logged at Level 6** — §Cal-IT has been value-free since IT.1
and stays value-free: the acts are structural/lexical, no calibration value issues, and the
Calibration Era stays deferred [AT.63(4)]. The generator's role is the directed one: RECORD, GROUND,
BAR-CHECK — never invent, never force [IT.31 §0 stance: definitions accepted as the Architect's
definitional acts, then grounded row by row; where a definition diverges from the census, the rows
win].
**Tags.** IT.55–IT.57. **Pattern.** the declaration-receiving tiers (IT.31's definitional-act
shape), premise audit logged in-tier.
**Status.** discovery-phase working tier. The declarations are the ARCHITECT'S acts, recorded
verbatim-in-substance with their grounds; no clause of Parts 1–4, of Level 5's closed record, or of
Tiers IT.1–IT.16 is modified [AT.63(2)] — **BM.113(6)'s frozen priced row is UNTOUCHED; its
discharge is logged here, in era 2.** No measured value enters [P5]; no new dimensionful scale
[P1]; species names stay quoted [Def-BM.3(1,(7))].
**Machine.** `era2/level6_isotopic/checks/declaration_package.py` → **13/13 exact** (Fractions; exact
$\mathbb Q(\sqrt2)$ arithmetic with the norm-based sign test; the trig normal-form ring; integer and
canon-text censuses; NO floating point); `run_all_level6.py` → **18 checkers, 289 exact markers, 0
failures**; `check_level6_format.py` → the gate over all seventeen Part 6 documents.
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13m): *"Issue the Phase-Jump and Radar-Sync
Declaration Package (D-PJ / D-RS Closure) … Formally issue the declared package into the corpus's
declaration census … Verify that issuing these declarations does not violate any standing bars … Do
not force a declaration. The declarations above are the Architect's explicit acts; the generator's
job is to record them, verify they don't break the bars, and update the census … Declare them as Def
categories when needed right?"* Executed: twelve package items recorded (ten issued, one resolved,
one deferred), seven premise corrections at IT.57(3), four sub-debts logged, the bar-check PASSED on
every bar; the Def-category question answered at IT.57(5): era 2 has no Def-IT series — the
declarations carry citation handles D-PJn/D-RSn at IT.55–IT.57 (the IT.31 definitional-act pattern).

---

### IT.55 — The package intake and the D-PJ side: six acts issued, grounded, and scoped

**Thm.**
$$(1)\quad\textbf{THE INTAKE AND THE AUTHORITY:}\qquad \text{the Architect has reviewed the audit's owed registers}\ [\mathrm{IT.54}(2):\ \mathrm{D\text{-}PJ1}\text{--}\mathrm{7},\ \mathrm{D\text{-}RS1}\text{--}\mathrm{6}]\ \text{and issued explicit acts for each item}:$$
$$\boxed{\ \text{these are the FIRST declaration acts logged at Level 6:}\ \ \S\mathrm{Cal\text{-}IT}\ \text{moves from empty to a VALUE-FREE declaration register — no calibration parameter is added, no value is issued, the Calibration Era stays deferred}\ [\mathrm{AT.63}(4)]\ }$$
$$\text{the generator's three roles, per the directive: RECORD the acts, GROUND each against the derived rows}\ [\mathrm{IT.31}\ \S0\ \text{stance}],\ \text{BAR-CHECK the issuance}\ [\mathrm{IT.57}(1)]\ \ —\ \ \neg\text{invent},\ \neg\text{force}\ [\mathrm{BM.6}(4)\ \text{precedent: a logged declaration act}]$$
$$(2)\quad(\mathrm{D\text{-}PJ1})\ \textbf{ISSUED — the directed label map}\ \hat O_{\mathrm{in}\to\mathrm{out}}:\qquad \text{the phase-jump operator is declared a DIRECTED STRUCTURAL MAP between two named endpoint registers (source/target); the temporal ``pre-tick/post-tick'' vocabulary is RETIRED FOR THIS OPERATOR in favor of causal register labels}:$$
$$\textbf{grounding and scope:}\ \ \text{the derived content stays the ONE jump edge}\ \delta_\ell\leftrightarrow\delta_q\ [\mathrm{FT.119}(2);\ \mathrm{IT.50}(4)];\qquad \text{``subnetwork registers'' is scoped to endpoint NAMING of the angle-ledger map — the derived}\ \hat O\ \text{acts on channel-angle labels}\ [\mathrm{PJ.5}(2);\ \mathrm{IT.50}(7)],\ \neg\text{on states (the arenas have none}\ [\mathrm{Def\text{-}H.41};\ \mathrm{Def\text{-}H.42}]);$$
$$\mathrm{C11}\ \text{'s node lifecycle is UNTOUCHED (the retirement is operator-local)};\qquad \text{the second iterate remains an adoption act}\ [\mathrm{FT.119}(7):\ \tfrac2{81}\ \text{``computed, none adopted''};\ \text{machine:}\ \tfrac2{81},\tfrac2{243},\tfrac23\notin\{\tfrac29,\tfrac2{27},\tfrac18\}]$$
$$(3)\quad(\mathrm{D\text{-}PJ2})\ \textbf{ISSUED (exploration-scoped) — the channel-phase register}\ \mathcal P_{\mathrm{ch}}:\qquad \text{a declared technical placeholder whose domain ADMITS COMPLEX INPUTS,}\ \neg\text{restricted to the rational counting-space labels; the Architect reserves the rename/identification right}:$$
$$\textbf{the arena bars hold (machine):}\ \ \mathcal P_{\mathrm{ch}}\ \text{is the VALUE SPACE of the angle coordinate,}\ \neg\text{an arena — the arenas}\ 9{=}3{\times}3,\ 27{=}3^3,\ 16{=}\dim\mathcal K_1\ \text{stay COUNTING SPACES: ``no inner product, no dynamics, no state, no Hamiltonian''}\ [\mathrm{Def\text{-}H.41};\ \mathrm{Def\text{-}H.42}\ \text{verbatim}];$$
$$\textbf{the register-disambiguation line (the IT.39(1) ``kept apart'' discipline):}\ \ \mathcal P_{\mathrm{ch}}\ \ \neg=\ \ \text{the winding}\ \Theta\ ([\Theta]=\mathfrak q\ [\mathrm{FT.22}]),\ \ \neg=\ \ \text{the defect}\ \Theta_R\ (\mathfrak q^0\ [\mathrm{FT.54}(1)]),\ \ \neg=\ \ \text{the registration phases}\ \alpha_e\in\{0,\pi\}\ [\mathrm{A4};\ \mathrm{EM.20}],$$
$$\neg=\ \ \text{the spiral holonomy}\ \Phi\ [\mathrm{D1.7}],\qquad \neg=\ \ \text{the CP transport}\ \mu_{\mathrm{CP}}=e^{\mathrm i\pi\Theta}\ [\mathrm{BM.108}(3)],\qquad \neg=\ \ \mathrm{IT.39}(1)\ \text{'s}\ \Delta\theta:\qquad \textbf{seven phase-like registers, seven distinct loci}$$
$$(4)\quad(\mathrm{D\text{-}PJ3})\ \textbf{RESOLVED BY D-PJ1 — no vertex:}\qquad \text{the directionality of the channel transition is a LABEL-MAP property of}\ \hat O_{\mathrm{in}\to\mathrm{out}};\ \ \textbf{no dynamical emission/absorption vertex is constructed or declared}:$$
$$\text{this is the bookkeeping horn of PJ.10(4)'s dichotomy}\ \text{(``either the photon mediates (barred) or it is decoration (admissible, ungrounded)'');}\qquad \text{the transit bar STANDS — on THREE grounds}:$$
$$\boxed{\ (\mathrm O1)\ \text{chiral-blind gauge blocks};\quad (\mathrm O2)\ \text{deficit}\ 1'\ \text{(the named missing primitive)};\quad (\mathrm O4)\ \text{no winding carrier};\qquad (\mathrm O3)\ \text{discharged}\ [\mathrm{IT.40}\text{--}\mathrm{IT.42};\ \mathrm{BM.134}(7)]\ }\qquad[\text{the directive's ``O1 and O4'' is CORRECTED — premise correction (P1), IT.57(3)}]$$
$$(5)\quad(\mathrm{D\text{-}PJ4})\ \textbf{ISSUED (functional form UNFIXED) — the event classification:}\qquad \text{the jump event is classified by its}\ \varepsilon_q\text{-GATED CRYSTALLIZATION SIGNATURE};\ \ \text{the ``degree of crystallization''}:=\text{the total real+virtual influence on the node, under the coarse-grained information limit}:$$
$$\textbf{the ingredient anchors (all derived):}\ \ \text{the}\ \varepsilon_q\ \text{gate}\ [\mathrm{A4};\ \mathrm{CT0.8};\ \mathrm{BM.19}(3)];\quad (n_{\mathrm{real}},n_{\mathcal V})\ [\mathrm{A4};\ \mathrm{D0.1};\ \mathrm{IT.53}(1)];\quad E_{\mathrm{vis}}=\min(\delta h,4\delta\tau)\ln2,\ \ I_{\mathrm{hid}}\in\mathbb Z\ln2\ [\mathrm{IT.2}(4)];\quad \dim\mathcal K_n\ [\mathrm{CT0.14}];\quad C_{\mathrm{cap}}=16\ [\mathrm{CT0.6}];\quad (1-\tfrac\gamma4)^2\ [\mathrm{BM.8}(2)];$$
$$\textbf{the precision debt (recorded,}\ \neg\textbf{forced):}\ \ \text{the functional form is UNFIXED; no derived ``Lyapunov contraction THRESHOLD'' exists (the contraction is a per-event factor; its zero locus is}\ \{0,8\}\ [\mathrm{IT.53}(3)])\ \text{— fixing a threshold VALUE is a further act};\qquad \text{count}\to\text{strength couplings barred}\ [\mathrm{BM.36}(3);\ \mathrm{BM.61}(8)(\mathrm O1);\ \mathrm{BM.69}(4)(\mathrm{iv});\ \mathrm{FT.73}(5)]$$
$$(6)\quad(\mathrm{D\text{-}PJ5})\ \textbf{ISSUED (well-definedness SUSPENDED) — the branch rule on the complex domain:}\qquad \hat O\ \text{operates on the complexified phase space (consistent with D-PJ2); the branch selection is}\ \neg\text{restricted to the unique positive rational preimage; the complex branch structure is KEPT OPEN}:$$
$$\textbf{the branch census (machine):}\ \ \text{on the cubic coordinate,}\ 2x^3-3x-\gamma\ \text{has THREE real roots for every}\ \gamma\in(0,\sqrt2)\ (\text{exact}\ \mathbb Q(\sqrt2)\ \text{sign census at five nodes, witnesses}\ 1,\tfrac65,\tfrac13),\ \text{EXACTLY ONE positive}:$$
$$\text{the derived branch selection (the unique positive root}\ [\mathrm{PJ.2}(6);\ \mathrm{PJ.12}(3\mathrm a);\ \mathrm{IT.50}(4)])\ \text{is UNAFFECTED; being a cubic,}\ \mathbb C\ \text{adds no further cubic roots — the open structure is the}\ z\text{-coordinate's}\ \omega\text{-relabeling, INERT on every label-free formed read}\ [\mathrm{IT.55}(3)\ \text{machine}];$$
$$\boxed{\ \textbf{SUSPENSION COHERENCE:}\ \ \neg\text{a formed read may pass through an open branch — reads through}\ \hat O^{-1}|_{\mathbb C}\ \text{are symbolic expressions only}\ [\mathrm{IT.43}(6)\ \text{doctrine}];\ \ \text{a specific rule remains OWED if a formed read ever needs it}\ }$$
$$(7)\quad(\mathrm{D\text{-}PJ6}/\mathrm{D\text{-}RS5})\ \textbf{ISSUED (citation corrected) — the observer reading frame:}\qquad \text{the ``rider'' semantics are explicitly DROPPED}\ [\mathrm{IT.44}(6)\ \text{stands}];\ \ \text{the reading is evaluated at the local designated register}\ o\ \text{of the subnetwork; the}\ o\text{-subscript lifts the read}:$$
$$\textbf{the citation correction (machine):}\ \ \text{the enabling locus is}\ \mathrm{Def\text{-}H.9}\ \text{'s register}\ o\ +\ \mathrm{FT.20}\ \text{'s G-row (observer-relative reads)}\ [\mathrm{IT.1}(7),(8)(\mathrm P4)],\ \ \textbf{NOT A9}\ \text{— A9 is the universe-selection axiom (its text carries no observer/register content);}\ \ \text{the}\ o\text{-subscript is Def-H.9(2)'s EXISTING convention — no new primitive}\ [\mathrm{IT.57}(3)(\mathrm P2)]$$
$$(8)\quad\textbf{status:}\qquad\textbf{issued (the Architect's acts, recorded):}\ (2)\text{--}(7);\qquad\textbf{grounded against:}\ \text{the rows cited per clause};\qquad\textbf{sub-debts generated:}\ \mathcal P_{\mathrm{ch}}\ \text{'s branch rule (open by design)},\ \mathrm{D\text{-}PJ4}\ \text{'s functional form},\ \mathrm{D\text{-}PJ1}\ \text{'s endpoint-register elaboration};$$
$$\neg\text{a measured value}\ [\mathrm{P5}],\qquad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\qquad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))]$$

**Req.** P1, P4, P5, A4, C11, CT0.6, CT0.8, CT0.14, D0.1 (Parts 1–2); D1.7, EM.20, FT.22, FT.54(1), FT.119(2),(7), FT.118(6), FT.131(3), Def-H.9, Def-H.41, Def-H.42, Def-H.19 (Part 3); IT.1(7),(8), IT.2(4), IT.31, IT.40–IT.42, IT.43(6), IT.44(6), IT.49(4), IT.50(4),(7), IT.53(1),(3), IT.54(2), IT-O1 (this level); BM.6(4), BM.8(2), BM.19(3), BM.36(3), BM.61(8), BM.69(4), BM.108(3), BM.113(6), BM.134(7), FT.73(5), FT.112 (Part 4); AT.63(2),(4) (Level 5); exact Q(√2) sign censuses, the trig-ring relabeling, the iterate census, the canon text census [math; machine: `declaration_package.py` §§A, B, C, 6/6].

**Pf.**
$$(2),(6):\ \text{the iterate census against the derived angles; the cubic's three-real-roots/one-positive census in exact}\ \mathbb Q(\sqrt2)\ \text{arithmetic (norm-based sign test, five nodes, three witnesses)}\ [\text{machine B2, B3}];\ \ (3):\ \text{the branch relabeling}\ r_k\mapsto r_{k+1}\ \text{and the sum invariance in the trig normal-form ring; the arena integers}\ [\text{machine B1}];$$
$$(7):\ \text{A9's text block censused for observer/register content — absent; the selection form present}\ [\text{machine C1}];\ \ (1),(4),(5),(8):\ \text{record rows on the cited clauses}.\ \blacksquare$$

**Phys.** The corpus receives its first Level-6 declarations the way it receives everything: with the
door open and the ledger stricter than the guest. Each act is recorded in the Architect's own
substance, then grounded — and grounding is where the corrections live. The directed operator keeps
its one derived edge and gains a name for its endpoints, not a state space to act on; the complex
phase register is admitted as a placeholder whose open branches are declared inert, because a cubic
with three real roots and one positive already had its selection derived and complexification adds
no root, only relabelings; the crystallization degree is issued with its ingredients anchored and
its functional form honestly unfixed, since no threshold exists to fix it against and counting is
not strength; and the observer subscript returns to the register axiom that always carried it, with a
universe-selection citation quietly corrected. Six acts, six groundings, four debts logged, nothing
forced — the declaration census does what it was built to do: it makes the Architect's choices
citeable without making them derived.

---

### IT.56 — The D-RS side, the BM.113(6) sector sync, and the unissued-symbol re-confirmation

**Thm.**
$$(1)\quad(\mathrm{D\text{-}RS1})\ \textbf{ISSUED (scoped) — the causal vocabulary:}\qquad \text{the symbols}\ \prec,\succ,\preceq,\succeq\ \text{are declared for the causal ordering of emission/reception events, replacing the temporal pre/post language in the radar protocol}:$$
$$\textbf{the grounding (machine):}\ \ \text{the tick index}\ \tau_n\ \text{gives a TOTAL order on ledger strata}\ [\mathrm{D1.8};\ \mathrm{D0.7};\ \mathrm{A7}];\qquad \mathrm{C11}\ \text{'s node lifecycle}\ (\text{wait}\to\text{data in}\to\text{Haar draw/tick}\to\text{data out/hop})\ \text{is a strict 4-order WITHIN a node};$$
$$\boxed{\ \textbf{SCOPE ROW:}\ \ \text{for two vertices AT THE SAME TICK,}\ \neg\text{a derived order exists (one ledger;}\ \neg\text{a cross-vertex tick-exchange rate)}\ \ [\mathrm{RS}\ \S0(0.1)]\ \ —\ \ \text{the declaration supplies LABELS,}\ \neg\text{ordering facts}\ }$$
$$\text{RS's logged C11 conflict (its correction P3: the brief's node-level labels invert the lifecycle) is DISSOLVED — the temporal labels are retired rather than selected between}$$
$$(2)\quad(\mathrm{D\text{-}RS2})\ \textbf{ISSUED as a DICTIONARY PAIRING — the two faces of the connector-floor event:}\qquad \text{the photon's ledger tick (discrete, one update) and its metric projection (the continuous null segment) are declared two FACES of the same connector-floor event: the tick is the ledger read; the worldline is the emergent chart projection}:$$
$$\textbf{the discipline rows (machine):}\ \ \deg(\text{tick count})=\mathfrak q^0\ \ne\ \mathfrak q^{-1/2}=\deg(\text{chart length})\ [\mathrm{D2.9};\ \mathrm{BM.102}(2)]:\ \ \text{the pairing is a DICTIONARY act,}\ \neg\text{an equation,}\ \neg\text{a conversion — the only dimensional bridge is}\ \mathfrak h\ [\mathrm{BM.102}(4)];$$
$$\text{partners,}\ \neg\text{equals}\ [\mathrm{BM.134}(5)];\qquad \neg\text{materialization coupling}\ [\mathrm{Def\text{-}H.19};\ \mathrm{FT.131}(3)];\qquad \text{the chart face is BM.34(2)'s null algebra}\ [\mathrm{IT.53}(4)];\qquad \neg\text{an amplitude is supplied (the leg amplitude stays}\ \neg\text{formed}\ [\mathrm{IT.41}])$$
$$(3)\quad(\mathrm{D\text{-}RS4})\ \textbf{DEFERRED (the Architect's word):}\qquad \text{the stationarity instantiation scope is explicitly marked OWED AND DEFERRED pending further data}:$$
$$\textbf{premise correction (P7):}\ \ \text{the agreement condition itself IS derived — reciprocity}\iff s\cdot dx=0\ \ [\mathrm{IT.53}(5)(\mathrm b),\ \text{machine}];\qquad \text{what defers is the SCOPE act}\ (\mathrm{BM.8}(2)\ \text{'s stationarity hypothesis is theorem-local; extending it is a scope declaration)}$$
$$(4)\quad\textbf{THE NUMBERING COLLISION RESOLVED:}\qquad \text{the package's item 6 carries}\ \mathrm{D\text{-}RS5}\ \text{(the observer frame — merged with D-PJ6 at IT.55(7)) and its item 10 ALSO carries}\ \mathrm{D\text{-}RS5}\ \text{(the dimensional clarification)}:$$
$$\boxed{\ \text{item 10 is RE-NUMBERED}\ \ \mathrm{D\text{-}RS7}\ \ \text{on the record, ISSUED as a clarification: the radar reads are}\ \mathfrak q^0\ \text{PRICES/reads}\ [\mathrm{D2.9};\ \mathrm{BM.102}(2);\ \text{HistLog}\ \S\mathrm{V.32}],\ \ \neg\text{P1 scales — the item's ``dimensionful … meaning equating to}\ \mathfrak q^0\text{'' is recorded with that gloss}\ }$$
$$(5)\quad(\mathrm{D\text{-}RS3})\ \textbf{STATUS — NOT ADDRESSED, REMAINS OWED:}\qquad \text{the tick--hop exchange-rate read for transit legs (per-edge}\ \Delta\tau=2\delta h\ \text{vs per-visit}\ 2\delta h-1\ \text{— both exact, neither frozen}\ [\mathrm{RS.3}(2);\ \mathrm{RS.8}\ \text{row 8}])\ \text{is}\ \neg\text{in the package: it stays OWED}$$
$$(6)\quad\textbf{(item 11) ISSUED — the BM.113(6) sector choice, DECLARED and synced:}\qquad \mathrm{BM.113}(6)\ \text{is era-1's ``one non-derived row, priced''}\ (\mathrm{Def\text{-}BM.16}(5)\ \text{reads the sign on the}\ \vee^2\text{-sector; four alternatives priced)}:\ \ \textbf{the Architect's act DISCHARGES the choice}:$$
$$\boxed{\ \text{the}\ \vee^2\ \text{read is KEPT and SYNCED with A4's}\ \{0,\pi\}\ \text{phase alphabet via the}\ \mathbb Z_2\ \text{dictionary}\quad \varepsilon=+1\leftrightarrow\alpha=0,\quad \varepsilon=-1\leftrightarrow\alpha=\pi\quad (\varepsilon=\cos\pi\alpha\ \text{— a bijection, machine})\ }$$
$$\textbf{the safety census (machine):}\ \ \text{the DERIVED exchange law}\ \varepsilon(\Gamma)=(-1)^A\ [\mathrm{BM.128}(7);\ \mathrm{IT.31}(4)]\ \text{stands UNFLIPPED in the adopted register — the multiplicativity is exact}\ (A{=}1..6);\ \ \text{the priced}\ \wedge^2\ \text{alternative is the SAME partition up to the label swap}\ (\text{BM.113}(6)\ \text{'s ``same statistics up to a global sign'', exhibited});$$
$$\text{the dictionary matches the}\ \mu_{\mathrm{CP}}=e^{\mathrm i\pi\Theta}=\pm1\ \text{pattern on sealed classes}\ [\mathrm{BM.108}(3)];\qquad \textbf{a CONVENTION,}\ \neg\textbf{a derived equality:}\ \ \neg\text{a cross-register conversion enters any derivation}\ [\mathrm{BM.134}(5)\ \text{discipline}];$$
$$\textbf{the frozen row is UNTOUCHED}\ [\mathrm{AT.63}(2)]:\ \ \text{the discharge is LOGGED IN ERA 2; the pricing record stands}\ (\text{the}\ \wedge^2\ \text{locus, the determinant line's}\ k{=}2\ \text{disagreement, the orientation block)}$$
$$(7)\quad\textbf{(item 12) RE-CONFIRMED — the unissued symbols:}\qquad \rho_{\mathrm B}\ \text{remains a declared, UNISSUED dimensionless symbol}\ (\mathfrak q^0)\ [\mathrm{A\text{-}BM.9};\ \mathrm{BM.69}(2);\ \mathrm{BM.102}(4)];\qquad e_0\ \text{remains symbolic and UNISSUED}\ [\mathrm{EM.25}(7):\ (g,g')\ \text{unconstrained}]:$$
$$\text{both explicitly scoped to the deferred Calibration Era}\ [\mathrm{AT.63}(4);\ \mathrm{IT.5}(2)]\ \text{and the deferred molecular level}\ [\mathrm{IT.15}(3)];\qquad \mathrm{IT.5}(1)\ \text{'s slot registry passes through UNCHANGED}\ [\text{machine}]$$
$$(8)\quad\textbf{status:}\qquad\textbf{issued:}\ (1),(2),(4)\ \text{'s}\ \mathrm{D\text{-}RS7},\ (6),(7)\ \text{'s re-confirmation};\qquad\textbf{deferred:}\ (3);\qquad\textbf{owed, untouched:}\ (5);\qquad\neg\text{a value issued},\ \ \neg\text{a canon edit}$$

**Req.** P1, P5, A4, A7, C11, D0.7, D1.8, D2.9, EM.20 (Parts 1–2); Def-H.19, FT.131(3) (Part 3); IT.41, IT.53(1),(4),(5), IT.54(2), IT.15(3), IT.5(1),(2), IT.31(4), IT-O1 (this level); AT.63(2),(4) (Level 5); A-BM.9, BM.8(2), BM.34(2), BM.69(2), BM.102(2),(4), BM.108(3), BM.113(6), BM.128(7), BM.134(5), Def-BM.16(5), EM.25(7), HistLog §V.32 (Parts 2, 4); the tick-order and lifecycle censuses, the degree pair, the flip-invariance census, the bijection [math; machine: `declaration_package.py` §§D–E, 3/3].

**Pf.**
$$(1):\ \text{the totality of}\ \le\ \text{on the tick witnesses and the strict 4-order of the lifecycle list}\ [\text{machine D1}];\ \ (2):\ \text{the degree pair}\ (\mathfrak q^0,\mathfrak q^{-1/2})\ \ [\text{machine E1}];\ \ (6):\ \text{the multiplicativity census unflipped, the flip's partition preservation and label swap, the}\ \mathbb Z_2\ \text{bijection onto}\ \{0,\pi\}\ \ [\text{machine E2}];\ \ (3),(4),(5),(7),(8):\ \text{record rows on the cited clauses}.\ \blacksquare$$

**Phys.** The radar side of the package issues with its edges visible. The causal symbols arrive
grounded in the only two orders the ledger derives — the tick's total order and the node's
lifecycle — and the tier writes down what they cannot do: two events at different vertices of one
tick have no ordered ground, and the new notation does not manufacture one. The tick/worldline
pairing issues as a dictionary, which is the only form the corpus has ever allowed its chart side to
take: two faces, different degrees, no equation, no coupling, no amplitude. And the sector sync is
the package's one genuine discharge — era 1 priced four alternatives for the exchange sign and
declined to choose; the Architect has now chosen, the choice is synced to the crystallization
alphabet by a two-element dictionary, the derived parity law stands exactly as it was, the priced
alternative is exhibited to differ only by a label swap, and the frozen row itself is not so much as
re-punctuated: the discharge lives where every era-2 act lives, in the era-2 record.

---

### IT.57 — The bar-check verdict, the declaration census, and the register state

**Thm.**
$$(1)\quad\textbf{THE BAR-CHECK VERDICT (machine, 13/13):}\qquad\begin{array}{l|l}\textbf{the bar}&\textbf{the verdict}\\\hline\mathrm{P1}\ \text{(no new dimensionful scale)}&\textbf{HONORED}: \text{every touched quantity is}\ \mathfrak q^0;\ \mathfrak h\ \text{untouched; no new numerical constant}\\\mathrm{P5}\ \text{(no measured value)}&\textbf{HONORED}: \text{no value issued; the slot registry unchanged}\ \\\text{the transit bar}&\textbf{STANDS on three grounds}\ \mathrm{O1/O2/O4};\ \neg\text{a vertex, amplitude, weight or rate attaches to}\ \hat O,\ \mathcal P_{\mathrm{ch}}\\\text{the arena bars}\ [\mathrm{Def\text{-}H.41}/\mathrm{Def\text{-}H.42}]&\textbf{HOLD}:\ \mathcal P_{\mathrm{ch}}\ \text{is the coordinate's value space; the arenas stay counting spaces}\\\text{the incommensurability bar}&\textbf{HOLDS}: \text{all five declaration families disjoint from the baryon generators}\ \{\dots\};\ \text{the pairing is a dictionary,}\ \neg\text{a bridge}\\\text{count}\to\text{strength}&\textbf{BARRED as ever}:\ \mathrm{D\text{-}PJ4}\ \text{'s form unfixed; no threshold value; no coupling}\\\text{species identification}&\textbf{NONE}: \text{names quoted}\ [\mathrm{Def\text{-}BM.3}(1,(7))]\\\text{the frozen canon}&\textbf{UNTOUCHED}\ [\mathrm{AT.63}(2)]:\ \mathrm{BM.113}(6)\ \text{'s discharge logged in era 2}\end{array}$$
$$\boxed{\ \textbf{VERDICT: THE PACKAGE IS ISSUABLE AS RECORDED — ten items issued, one resolved by issuance, one deferred; seven premise corrections and four sub-debts ride with it}\ }$$
$$(2)\quad\textbf{THE REGISTER STATE AFTER ISSUANCE:}\qquad\begin{array}{l|l}\textbf{state}&\textbf{the items}\\\hline\textbf{ISSUED}&\mathrm{D\text{-}PJ1},\ \mathrm{D\text{-}PJ2},\ \mathrm{D\text{-}PJ3}\ (\text{resolved by}\ \mathrm{D\text{-}PJ1}),\ \mathrm{D\text{-}PJ4},\ \mathrm{D\text{-}PJ5},\ \mathrm{D\text{-}PJ6}/\mathrm{D\text{-}RS5}\ (\text{merged}),\ \mathrm{D\text{-}RS1},\ \mathrm{D\text{-}RS2},\ \mathrm{D\text{-}RS7}\ (\text{item 10, re-numbered}),\ \text{the}\ \mathrm{BM.113}(6)\ \text{sector sync (item 11)},\ \text{item 12's re-confirmation}\\\textbf{DEFERRED}&\mathrm{D\text{-}RS4}\ (\text{the stationarity instantiation scope — pending data})\\\textbf{REMAINING OWED}&\mathrm{D\text{-}RS3}\ (\text{the tick--hop exchange rate});\quad \mathrm{D\text{-}PJ7}/\mathrm{D\text{-}RS6}\ (\text{the standing IT-O1 package: deficit}\ 1',\ \text{the P4 transport profile, a transit winding carrier}\ [\mathrm{IT.41}(2)])\\\textbf{SUB-DEBTS (generated by the issuance)}&\mathcal P_{\mathrm{ch}}\ \text{'s specific branch rule (open BY DESIGN until a formed read needs it)};\quad \mathrm{D\text{-}PJ4}\ \text{'s degree functional form (and any threshold value — a further act)};\quad \mathrm{D\text{-}PJ1}\ \text{'s endpoint-register elaboration (if}\ \hat O\ \text{is ever to act beyond the angle ledger)}\\\textbf{inherited forks (unchanged)}&\text{the}\ b\text{-slot choice}\ [\mathrm{IT.49}(4)];\ \text{the order-3 filling}\ [\mathrm{IT.52}];\ \text{the mass-read route choice}\ [\mathrm{IT.14}(3);\ \mathrm{BM.30}(5)];\ \text{the lift/vielbein/transport profile}\ [\mathrm{AT.63}(3)]\end{array}$$
$$(3)\quad\textbf{THE SEVEN PREMISE CORRECTIONS (the rows win):}\qquad\begin{array}{l|l}\textbf{\#}&\textbf{the correction}\\\hline(\mathrm P1)&\text{the transit bar stands on THREE grounds}\ \mathrm{O1/O2/O4}\ \text{— the directive's ``O1 and O4'' omits O2 (deficit}\ 1')\ [\mathrm{IT.40}\text{--}\mathrm{IT.42}]\\(\mathrm P2)&\mathrm{D\text{-}PJ6}\ \text{'s ``as permitted by A9''}\ \to\ \mathrm{Def\text{-}H.9}+\mathrm{FT.20}\ \text{'s G-row — A9 is universe selection (machine text census)}\\(\mathrm P3)&\text{the}\ \mathrm{D\text{-}RS5}\ \text{numbering collision: item 10 re-numbered}\ \mathrm{D\text{-}RS7}\\(\mathrm P4)&\text{item 10's wording: ``dimensionful … meaning}\ \mathfrak q^0\text{''}\ \to\ \text{the radar reads are}\ \mathfrak q^0\ \text{dimensionless prices/reads,}\ \neg\text{P1 scales}\\(\mathrm P5)&\mathrm{D\text{-}RS2}\ \text{recorded under}\ \mathrm{BM.134}(5)\ \text{'s dictionary discipline — faces/pairing,}\ \neg\text{equality;}\ \neg\text{materialization coupling}\\(\mathrm P6)&\mathrm{D\text{-}PJ1}\ \text{'s ``between two distinct subnetwork registers'' scoped to endpoint NAMING — the derived}\ \hat O\ \text{acts on angle labels,}\ \neg\text{states}\\(\mathrm P7)&\mathrm{D\text{-}RS4}\ \text{'s premise: the agreement condition IS derived}\ (\iff s\cdot dx=0);\ \text{the deferred piece is the instantiation scope}\end{array}$$
$$(4)\quad\textbf{THE PLACEMENT ANSWER (the directive's closing question — ``Def categories?''):}\qquad \text{era 2 has}\ \neg\text{a Def-IT tag series, and the level gate's citation registry recognizes Def-EM/Def-H/Def-BM headers only — opening a tag family mid-level is a closure-era structural act}:$$
$$\boxed{\ \text{the declarations are recorded as LOGGED ACTS inside IT-tags}\ (\mathrm{IT.31}\ \text{'s definitional-act pattern})\ \text{with citation handles}\ \ \mathrm{D\text{-}PJ}n\ @\ \mathrm{IT.55},\ \ \mathrm{D\text{-}RS}n\ @\ \mathrm{IT.56}\ \ —\ \ \text{the Def-style role is served by the clause, as Def-H.43's declared promotion is served by its clause};\ \ \text{a Def-IT series at closure (or Level 7) is logged as an OPTION,}\ \neg\text{forced}\ }$$
$$(5)\quad\textbf{the open rows after the package:}\qquad \mathrm{IT\text{-}O3}\ \text{gains the declared vocabulary (the radar candidate}\ [\mathrm{IT.53}(7)]\ +\ \prec/\succ\ +\ \text{the event pairing) and stays OPEN};\qquad \mathrm{IT\text{-}O1}\ \text{UNCHANGED (three grounds; the package constructs no vertex — D-PJ3 explicit)};$$
$$\mathrm{IT\text{-}O2},\ \mathrm{IT\text{-}O5}\ \text{unchanged};\qquad\boxed{\ \textbf{NO new open row}\ };\qquad \text{the deferred Calibration Era unchanged}\ [\mathrm{AT.63}(4)]$$
$$(6)\quad\textbf{the declaration census:}\qquad\textbf{the calibration values this tier adds: none.}\quad \S\mathrm{Cal\text{-}IT}\ \text{records the ACTS (structural/lexical) and stays VALUE-FREE};\qquad\neg\text{a P4 addition valued},\quad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\quad\neg\text{a measured value}\ [\mathrm{P5}],\quad\neg\text{a species identification};$$
$$\text{the unissued symbols stand:}\ \rho_{\mathrm B},\ e_0,\ \hat\mu'^2,\ \sigma_\ell,\ \sigma_\nu,\ \varepsilon_q\ (\mathrm{AT\text{-}O27}),\ (\varkappa,\beta)\ (\mathrm{AT\text{-}O3}),\ \mathfrak h\ (\mathrm{P1}),\ \text{the}\ \mu_{\mathrm{ch}}\ \text{family (Cal-F)}$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{declaration\_package.py}\to\textbf{13/13 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{18 checkers, 289 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{17 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad \text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and a declaration is}\ \neg\textbf{a derivation}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P4, P5 (Parts 1–2); Def-H.41, Def-H.42, Def-H.43, FT.22, FT.54(1), FT.119(7), FT.131(3) (Part 3); IT.14(3), IT.40–IT.42, IT.41(2), IT.43(6), IT.44(6), IT.49(4), IT.50, IT.52, IT.53(5),(7), IT.54(2), IT.55, IT.56, IT-O1, IT-O2, IT-O3, IT-O5 (this level); AT.39(8), AT.63(2),(3),(4) (Level 5); A-BM.9, BM.6(4), BM.30(5), BM.36(3), BM.61(8), BM.69(2),(4), BM.102(4), BM.108(3), BM.113(6), BM.128(7), BM.134(5),(7), Def-BM.3(1),(7), Def-BM.16(5), EM.25(7), FT.73(5), FT.79(5) (Parts 2, 4); the full checker, the level runner and the level gate re-run end to end [math; machine: `declaration_package.py` §F, 4/4].

**Pf.**
$$(1):\ \text{the bar-check assembly over the twelve machine markers}\ [\text{machine F1--F4}];\ \ (2),(3):\ \text{the register and correction tables assembled from IT.55--IT.56's clauses};\ \ (4)\text{--}(8):\ \text{the placement row on the gate's registry structure; the census, the runner and the gate re-run end to end. No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** The bar-check is the tier that earns the package its keep, and it passes on every bar with
the margins shown: nothing dimensionful is added because everything declared is a label, an order, a
dictionary, or a convention at degree zero; nothing measured enters because no value issues — the
nine-symbol registry passes through untouched; the photon still cannot mediate, because a label map
with endpoints is still not a vertex, and the transit bar still stands on all three of its grounds,
corrected on the record when the directive miscounted them. The two subtlest items get the subtlest
treatment: the complex phase register is admitted with its branches open and its well-definedness
suspended, which costs nothing because a cubic's complexification adds no root, only inert
relabelings; and the exchange-sign sector — priced and undecided since era 1 — is finally chosen, by
the only authority that can choose it, in a form that flips no derived law and edits no frozen line.
What remains owed is listed to the item: a hop-exchange rate, a branch rule if ever needed, a
functional form, the standing transit package. The census now has its first era-2 entries, and the
corpus keeps the distinction that makes them safe: a declaration is a choice made citable, never a
choice made true.

---

## §Cal-IT — the first logged acts (value-free)

**The register moves from empty to ACT-RECORDING; it stays VALUE-FREE.** The declarations logged by
Tier IT.17 are structural/lexical acts of the Architect (D-PJ1–D-PJ6, D-RS1, D-RS2, D-RS7, the
BM.113(6) sector sync, item 12's re-confirmation; D-RS4 deferred), each grounded and bar-checked at
IT.55–IT.57. **No calibration parameter is added, valued, or re-scoped**: $\mathfrak h$ (P1),
$\varepsilon_q$ (AT-O27; adoption ¬issued — the D-PJ4 signature USES the gate, it does not value
it), $e_0$ (EM.25(7), ¬issued), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$, $\hat\mu'^2$,
$\sigma_\ell$, $\sigma_\nu$ (A-BM.9/Cal-BM/Cal-F; ¬declared values), the P4 transport profile, the
lift and the vielbein (AT.60), the read rules (M1′)–(M3′) [AT.54(6)], and the mass-read route choice
[IT.14(3); BM.30(5)] all stand unchanged. The Calibration Era stays **deferred** [AT.63(4)]; the
molecular level's placement stays the Architect's act [IT.15(3)].

## §Open-IT additions from Tier IT.17

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.17 opens **no new open row**. The declaration register itself carries the remaining owed acts: D-RS3 (the tick–hop exchange rate); D-PJ7/D-RS6 (the standing IT-O1 package); the three sub-debts (𝒫_ch's branch rule — open by design; D-PJ4's degree functional form; D-PJ1's endpoint-register elaboration). IT-O3 gains the declared vocabulary and the D-RS2 event pairing (on top of IT.53(7)'s radar candidate) and **stays OPEN**; IT-O1 is unchanged (the package constructs no vertex); IT-O2/IT-O5 unchanged | IT.57(2),(5); IT.55(2),(5),(6); IT.56(3),(5) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4)]: (IT-O1) the formed transit-leg
amplitude — open on three grounds, the missing primitive deficit 1′ [IT.41]; (IT-O2) the N≥4
multi-seal configuration calculus — the binding value; (IT-O3) the handshake-indicator operational
theory — candidate semantics recorded [IT.53(7)], vocabulary now declared; (IT-O5) the isotope
cutoff — the empirical/dynamical side at IT-O1; the owed route choice [IT.14(3)]; the deferred
Calibration Era [AT.63(4)]; and the Level-5 inheritance [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.18: the handshake-ladder operational theory — IT-O3 CLOSED, with the AT-O7 staleness correction

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.18 — the construction that discharges
**IT-O3** (the row Tier IT.1 opened: *"the handshake-indicator operational theory — the
χ_{NE≥𝒯₀}-gated read families across the threshold ladder {4𝔥/ln2, …, 120𝔥/ln2} (span ratio 30) —
the locus where IT.5's calibration strategy becomes mathematics"*): the two exact nested ladders
reconstructed as sum sets, the exhaustive census of the χ-carrying formed reads, the per-rung
activation windows with exact minimal lapses, the simultaneous-formation witnesses at every rung,
the rung-by-rung slot-constraint map, the cross-rung consistency web, and the protocol grammar in
the vocabulary Tier IT.17 declared — with the round-trip order theorem. Also recorded: the **AT-O7
staleness correction** (the row was closed at Level 5 by AT.6(7),(10); IT.1(5)'s inherited mention
is stale) and the two-item canon-erratum register queued for the closure pipeline.
**Tags.** IT.58–IT.60. **Pattern.** the construction tiers (IT.2/IT.6's shape) with the adjudication
tiers' premise audit.
**Status.** discovery-phase working tier. Nothing is adopted into the frozen canon; **no declaration
issues** (the grammar uses the Tier-IT.17 acts as issued, adds none); §Cal-IT's act register is
unchanged and stays VALUE-FREE; no clause of Parts 1–4, of Level 5's closed record, or of Tiers
IT.1–IT.17 is modified [AT.63(2)]. **IT-O3 is CLOSED as a structural row; the Calibration Era stays
deferred [AT.63(4)]; no value is issued, estimated or compared [P5].**
**Machine.** `era2/level6_isotopic/checks/handshake_ladder.py` → **15/15 exact** (exact sum-set
enumeration; integer ceilings of rationals; `Fraction` witnesses; monomial identities; exhaustive
order enumeration; text censuses against the Level-5/Level-6 records — NO floating point);
`run_all_level6.py` → **19 checkers, 304 exact markers, 0 failures**; `check_level6_format.py` →
the gate over all eighteen Part 6 documents.
**No floating point in any assertion. No measured value enters any clause [P5] — the local scale is
parameterized as $E=\xi\,\mathfrak h/\ln2$ with $\xi$ a positive RATIONAL PARAMETER; every quantity
is symbolic in $\mathfrak h,\ln2$ or an exact derived integer/rational. No new dimensionful scale
[P1]. The horizon read stays QUARANTINED [BM.115(4); BM.15(4); P3] — cited frozen, ¬reconciled. No
transit amplitude is constructed — conditions and formed weights only [BM.122(6); FT.79(5)]; IT-O1
unchanged. Species names quoted [Def-BM.3(1,(7))].**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13m, night watch): *"proceed to close the numerical
crunch level gaps and other tasks."* Scoped against the record: the closable numerical-construction
gap is IT-O3 (the declarations IT.17 issued supplied the vocabulary it waited on); AT-O7 turns out
to have been closed at Level 5 (the staleness is corrected here); AT-O13 needs $(\varkappa,\beta)$ —
the Architect's act; IT-O1 needs deficit 1′ — application-layer, ¬constructible; IT-O2 needs its
three named constructions — recorded, not forced; the AT-O30/AT-O32 censuses remain open heavy
enumerations. Executed: IT-O3 discharged, the staleness corrected, nothing forced.

---

### IT.58 — The ladder machinery and the exhaustive census of the χ-gated read families

**Thm.**
$$(1)\quad\textbf{THE TWO EXACT NESTED LADDERS, RECONSTRUCTED (the numerical crunch):}\qquad \text{the}\ n\text{-chain}\ E_{\mathrm{int}}\ \text{ladders are the SUM SETS (with repetition) of the floors}\ [\mathrm{BM.115}(2)]:$$
$$\text{computed-cell floors}\ \{2,6,12,24,60\}\ [\mathrm{BM.13}(2);\ \mathrm{FT.28};\ \text{Census}\ \mathrm{FT.35}(2);\ \mathrm{FT.42}(5)]\ \Rightarrow\ n=1,2,3:\ \ (5,\ 15,\ 33)\ \text{values},\ \ \min=2n,\ \max=60n,\ \ \boxed{\ \text{span ratio EXACTLY }30\text{ at every}\ n\ };$$
$$\text{six-state floors}\ \{12,24,60\}=2E\ [\mathrm{Def\text{-}BM.14}(1);\ \mathrm{BM.60}(1):\ 12{:}24{:}60=1{:}2{:}5]\ \Rightarrow\ (3,\ 6,\ 10)\ \text{values},\ \min=12n,\ \max=60n,\ \ \text{span}\ 5;$$
$$\text{machine: EVERY value of both frozen tables reproduced element-by-element as an exact sum set};\qquad \text{the nesting}\ \{12,24,60\}\subset\{2,6,12,24,60\}\ \text{is exact};\ \text{the two extra cells are}\ 2\ (\text{the digon floor}\ [\mathrm{FT.28}])\ \text{and}\ 6\ (\text{the baryon junction}\ [\text{Census}\ \mathrm{FT.35}(2)]):$$
$$\text{they lower the minimum from}\ 12n\ \text{to}\ 2n\ \text{and raise the span from}\ 5\ \text{to}\ 30$$
$$(2)\quad\textbf{THE PAIR LADDER AND THE}\ m_{\mathrm{hid}}\ \textbf{RANGES:}\qquad \mathcal T_0(\text{pair})=2E_{\mathrm{int}}(c)\,\mathfrak h/\ln2\ \ [\mathrm{BM.122}(2);\ \mathrm{Def\text{-}BM.17}(3)]\ \ \text{over the computed-cell floors gives the coefficients}\ (4,12,24,48,120):$$
$$\text{the ladder}\ \bigl\{\tfrac{4\mathfrak h}{\ln2},\dots,\tfrac{120\mathfrak h}{\ln2}\bigr\}\ \text{of}\ \mathrm{IT.4}(5),\ \text{span ratio EXACTLY}\ 30\ [\mathrm{BM.111}(5);\ \mathrm{BM.115}(2)(\mathrm i)];\qquad m_{\mathrm{hid}}=E_{\mathrm{int}}\ln2/\mathfrak h\ [\mathrm{FT.44}(4)]\ \text{on the ladders:}\ n{=}2:\ \bigl[\tfrac{4\ln2}{\mathfrak h},\tfrac{120\ln2}{\mathfrak h}\bigr]\ \text{computed},\ \bigl[\tfrac{24\ln2}{\mathfrak h},\tfrac{120\ln2}{\mathfrak h}\bigr]\ \text{six-state};\ \ n{=}3:\ \bigl[\tfrac{6\ln2}{\mathfrak h},\tfrac{180\ln2}{\mathfrak h}\bigr],\ \bigl[\tfrac{36\ln2}{\mathfrak h},\tfrac{180\ln2}{\mathfrak h}\bigr]\ [\mathrm{BM.115}(2)\ \text{rows re-derived}]$$
$$(3)\quad\textbf{THE CURVATURE READ IS THE SCALE READ (no datum added); THE HORIZON READ STAYS QUARANTINED:}\qquad G=2\pi E_{\mathrm{int}}^2\ln2\ \ [\mathrm{BM.88}(3);\ \mathrm{BM.16}(1)]\ \ \text{substituted into}\ \ \mathcal T(\mathcal R;G,N)=\tfrac{\mathfrak h}{N\ln2}\sqrt{\tfrac{G}{2\pi\ln2}}\ \ \text{gives}\ \ \tfrac{E_{\mathrm{int}}\mathfrak h}{N\ln2}=\mathcal T_0/N\ \ \text{EXACTLY (machine: the monomial identity on squares — no floating point, no branch)}:$$
$$\text{the curvature ladder ratio}\ G(60n)/G(2n)=900=30^2\ \ [\mathrm{BM.115}(3);\ \text{machine: exact integers}];\qquad \text{the horizon read}\ \mathcal T=2r_s/N,\ \ r_s=\tfrac12\mathfrak hE_{\mathrm{int}},\ \ r_s^{(n)}\in[n\mathfrak h,30n\mathfrak h]\ \ \textbf{QUARANTINED as a comparison scale}\ [\mathrm{BM.115}(4);\ \mathrm{BM.15}(4);\ \mathrm{P3}]:$$
$$\text{cited frozen,}\ \neg\text{reconciled with the scale read,}\ \neg\text{a collapse reading,}\ \neg\text{a horizon identification}\ [\mathrm{BM.15}(4)\ \text{comparison discipline}]$$
$$(4)\quad\textbf{THE EXHAUSTIVE}\ \chi\textbf{-CARRIER CENSUS:}\qquad \text{over the formed-read register}\ (18\ \text{reads:}\ \mathrm{IT.5}(1)\ \text{'s table}\ +\ \mathrm{BM.122}\ +\ \mathrm{Def\text{-}BM.17}\ +\ \mathrm{BM.134}\ +\ \mathrm{AT.44}\ +\ \mathrm{BM.137}\ +\ \mathrm{BM.31}\ +\ \mathrm{Def\text{-}H.32}):\ \ \textbf{EXACTLY FOUR carry the indicator}\ [\text{machine census}]:$$
$$\begin{array}{l|l}(\mathrm i)\ \ \text{the materialization condition}\ NE\ge\mathcal T_0\ \ \text{itself}&[\mathrm{Def\text{-}BM.17}(3);\ \mathrm{BM.115}(1)]\\(\mathrm{ii})\ \ \mathcal W_{\text{channel}}=x_+^2\,\chi_{\{NE\ge\mathcal T_0\}}=(1{-}4\varepsilon_q)^2\chi&[\mathrm{BM.122}(3)]\\(\mathrm{iii})\ \ \Gamma=\Gamma_{\mathrm{tr}}(\varepsilon_q)\,f\,\tfrac{\varepsilon_{\mathrm{eff}}}{\varepsilon_{\mathrm{EM}}}\,\mathcal N\,\chi&[\mathrm{Def\text{-}BM.17}(4)\ \text{— STATUS FOOTNOTE: the product form is the clause's own NON-DERIVED row}]\\(\mathrm{iv})\ \ \text{the resolvent-species meeting: chart}\ R(z;\mathbf p)\ \text{and zig-zag}\ \tfrac1{1-w^2x_+x_-}&[\mathrm{BM.134}(5):\ \text{``they meet ONLY through the threshold indicator''}]\end{array}$$
$$\text{the census scope is the enumerated formed-read register — stated as such (an absence claim over the register, not over all possible expressions)}$$
$$(5)\quad\textbf{THE CURRENCY STRUCTURE AT THE LADDER LEVEL:}\qquad \operatorname{alph}(\chi)=\{NE,E_{\mathrm{int}},\mathfrak h,\ln2\}\ \ \textbf{— LEPTON-FREE: the handshake itself is a baryon+shared gate, and it is BINARY}\ [\mathrm{IT.4}(2)];$$
$$\varepsilon_q\ \text{enters the gated world ONLY through}\ \mathcal W_{\text{channel}}\ \text{and}\ \Gamma_{\mathrm{tr}}\ [\mathrm{BM.122}(3);\ \mathrm{BM.44}(2)];\qquad \rho_{\mathrm B},\ \hat\mu'^2\ \text{enter NO}\ \chi\text{-gated family (their formed families — the pole ladder, the BM.83(5) cross-ratios — are ungated)}:$$
$$\boxed{\ \mathrm{IT.4}(2)\ \text{'s three-formed-mixed-loci exhaustiveness re-certified AT THE LADDER LEVEL: the gate/weight factorization is the ladder's whole currency content}\ }$$
$$(6)\quad\textbf{THE TWO EXACT OPPOSITE LIMITS (re-certified in Fractions):}\qquad \mathcal W_{\text{channel}}=1\iff\varepsilon_q=0\ \wedge\ NE\ge\mathcal T_0\ (\text{creation certain, annihilation impossible});\qquad \mathcal W_{\text{channel}}>0\iff\varepsilon_q<\tfrac14\ \wedge\ \text{gated};$$
$$\text{witness}\ \varepsilon_q=\tfrac{249}{1000}:\ \ \mathcal W=\tfrac1{62500}\ \ \text{EXACTLY};\qquad \text{the indicator's zero is ABSENCE, not stability}\ [\mathrm{BM.122}(3);\ \mathrm{Def\text{-}BM.17}(6)(\mathrm{ii});\ \mathrm{CT0.8}\ \text{domain}]$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(6)\ \text{(the frozen rows re-certified exactly; the census and the reconstruction are the new machine content)};\qquad\neg\text{a declaration},\ \ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P3, P5, CT0.8 (Parts 1–2); Def-H.32, FT.28, FT.44(4) (Part 3); IT.4(2),(5), IT.5(1),(2), IT.44(5), IT.46(3) (this level); Census FT.35(2), FT.42(5) (Census); BM.13(2),(3), BM.15(4), BM.16(1), BM.31(2), BM.44(2), BM.60(1), BM.83(4),(5), BM.88(3), BM.103(3), BM.109(2), BM.111(5), BM.114(1), BM.115(1),(2),(3),(4),(5), BM.116(4), BM.122(2),(3), BM.134(5), BM.137(3), Def-BM.4(1), Def-BM.14(1), Def-BM.17(3),(4),(6) (Part 4); AT.44(1),(5) (Level 5); exact sum-set enumeration, integer arithmetic, Fraction witnesses [math; machine: `handshake_ladder.py` §A1–A3, §B1–B3, 7/7].

**Pf.**
$$(1):\ \text{the sum sets of}\ \{2,6,12,24,60\}\ \text{and}\ \{12,24,60\}\ \text{enumerated with repetition for}\ n=1,2,3\ \text{and compared element-by-element to the frozen tables; counts, minima, maxima, spans, nesting, the extra cells}\ [\text{machine A1}];\ \ (2):\ \text{the pair coefficients}\ 2\cdot\{2,6,12,24,60\};\ \text{the range rows from the sum-set extrema}\ [\text{machine A2}];$$
$$(3):\ \text{the square of}\ \tfrac{\mathfrak h}{N\ln2}\sqrt{\tfrac{G}{2\pi\ln2}}\ \text{after}\ G=2\pi E^2\ln2\ \text{as a Laurent monomial, against}\ (\mathcal T_0/N)^2;\ \ 900=30^2\ \text{in integers}\ [\text{machine A3}];\ \ (4),(5):\ \text{the}\ \chi\text{-membership table over the}\ 18\text{-read register; the alphabet intersections}\ [\text{machine B1, B2}];\ \ (6):\ \text{exact rational evaluation at the four witnesses}\ [\text{machine B3}].\ \blacksquare$$

**Phys.** The ladder the era opened with is now in hand as pure arithmetic: two nested families of
integers, every value a sum of floor prices, the spans exactly thirty and five at every chain count,
and the pair channel's threshold coefficients the doubled computed floors. The curvature read adds
nothing — substituting the lock into it returns the scale read monomial for monomial — and the
horizon read stays where the corpus always kept it, quarantined behind its comparison discipline.
Over this ladder the census is exhaustive in the only honest sense available: across the register of
formed reads the level owns, exactly four carry the handshake, and the fourth of them carries its
own non-derived footnote into every use. The currency structure sharpens into the operational form
of the bar: the gate is baryon-plus-shared and binary, the flicker rides only the weight, and the
pole slots never enter the gated world at all — which is precisely why no single-currency instrument
can calibrate both banks, rung by rung, as a machine census rather than as a slogan.

---

### IT.59 — The activation windows: the calibration strategy becomes mathematics

**Thm.**
$$(1)\quad\textbf{THE ACTIVATION STRUCTURE:}\qquad \mathcal T(\mathcal R;N)=\mathcal T_0/N\ \ \text{is STRICTLY decreasing in the lapse (exact rational witnesses); the locus}\ \{E>0:\ NE\ge\mathcal T_0\}=\bigl[\tfrac{\mathcal T_0}N,\infty\bigr)\ \ \text{is a NONEMPTY HALF-LINE at every admissible lapse}:$$
$$\boxed{\ \neg\exists\ \textbf{a permanently forbidden resonance}\ [\mathrm{BM.115}(1),(5);\ \mathrm{BM.116}(4);\ \mathrm{Def\text{-}BM.17}(6)(\mathrm{iii})]\ }\qquad\text{and with the local scale parameterized}\ E=\xi\,\mathfrak h/\ln2,\ \ \xi\in\mathbb Q_{>0}\ \ (\textbf{a parameter,}\ \neg\textbf{a measured value}\ [\mathrm{P5}]):$$
$$\text{materialization}\iff N\xi\ge2E_{\mathrm{int}}(c)\ \ [\mathrm{BM.122}(2)\ \text{pair form}]\qquad\Rightarrow\qquad \boxed{\ N_{\min}(\text{rung},\xi)=\Bigl\lceil\tfrac{2E_{\mathrm{int}}}{\xi}\Bigr\rceil\ \ \text{exact (integer ceiling of a rational; minimality verified in both directions)}\ }$$
$$(2)\quad\textbf{THE WINDOW TABLE (machine):}\qquad \text{at the witness scale}\ \xi=10:\ \ N_{\min}=(1,2,3,5,12)\ \text{for}\ E_{\mathrm{int}}=(2,6,12,24,60);\qquad \text{the pre-ceiling boundaries}\ \tfrac{2E}{\xi}\ \text{keep the span ratio EXACTLY}\ 30;\ \ \text{the integer ceilings compress it at small rungs — recorded, not hidden}$$
$$(3)\quad\textbf{THE SIMULTANEOUS-FORMATION WITNESSES — THE OPERATIONAL WINDOW IS NEVER EMPTY:}\qquad \mathrm{IT.5}(2)\ \text{'s necessary data species needs}\ \chi,\ \mathcal W_{\text{channel}}\ \text{and}\ \mathcal B_{\mathrm{ens}}\ \text{simultaneously formed on a MULTI-SEAL ensemble}\ (N\ge4,\ \text{where}\ g_\delta(N)>0\ \text{forces}\ \delta\text{-mixing}\ [\mathrm{BM.31}(2);\ \mathrm{IT.31}(3)]):$$
$$\text{machine: at}\ \xi=10\ \text{the witnesses}\ N_w=\max\bigl(4,\lceil\tfrac{2E}{\xi}\rceil\bigr)=(4,4,4,5,12)\ \text{satisfy BOTH conditions at EVERY rung};\qquad\boxed{\ \text{the calibration strategy's operational window exists at every rung of the 30-spanned ladder — the values stay quarantined}\ [\mathrm{P5};\ \mathrm{AT.63}(4)]\ }$$
$$(4)\quad\textbf{THE CROSS-RUNG CONSISTENCY WEB (a theorem, not an assumption):}\qquad \varepsilon_q\ \text{is ONE global A4 slot}\ [\mathrm{BM.19}(2);\ \mathrm{D0.4};\ \mathrm{IT.46}(3)\ \text{'s fill refutation re-cited}]:$$
$$\text{the flicker factor}\ x_+^2=(1-4\varepsilon_q)^2=1-8\varepsilon_q+16\varepsilon_q^2\ \ \text{is the IDENTICAL polynomial at every rung (the rung enters only through the binary gate)}\ [\text{machine}]:$$
$$\boxed{\ \textbf{multi-rung spectroscopy over-determines the single}\ \varepsilon_q\ \textbf{— the consistency web across the 30 spanned rungs is a THEOREM of the global-slot status; a rung-dependent flicker would contradict BM.19(2)}\ }$$
$$(5)\quad\textbf{THE SLOT-CONSTRAINT MAP (IT.5(2) rung by rung):}\qquad \text{across the WHOLE ladder the}\ \chi\text{-gated formed families carry exactly ONE undeclared slot —}\ \varepsilon_q\ \text{(lepton/flicker) — with the baryon side entering STRUCTURALLY as the rung position}\ E_{\mathrm{int}}\ \ (\text{the seal-class taxonomy}\ [\mathrm{IT.4}(4):\ \text{the proton class 15 of 64}]):$$
$$\rho_{\mathrm B},\ \hat\mu'^2,\ \sigma_\ell,\ \sigma_\nu\ \ \text{enter NO gated family}\ [\mathrm{BM.83}(4),(5);\ \mathrm{IT.5}(1):\ \text{their families are the pole ladder and the cross-ratios — ungated}]:$$
$$\boxed{\ \text{gated spectroscopy fixes the flicker slot against structural rung data, and NOTHING gated reaches the pole/transport slots — the incommensurability bar's operational shadow, exact at every rung}\ }$$
$$(6)\quad\textbf{the read species:}\qquad \text{per rung the accessible data are the}\ (\mathrm R1)\ \text{charge-class and}\ (\mathrm R2)\ \text{winding reads on the activated}\ N\ge4\ \text{ensembles}\ [\mathrm{IT.1}(3);\ \mathrm{IT.4}(5);\ \mathrm{IT.5}(2)];\qquad \text{single-atom ladder positions fix lepton-currency slots only}\ [\mathrm{IT.4}(4)]\ \text{— the ladder's baryon datum is the rung position itself}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(6);\qquad\neg\text{a declaration},\ \ \neg\text{a value issued},\ \ \neg\text{a scale added}\ [\mathrm{P1}]$$

**Req.** P1, P5, CT0.8, D0.4 (Parts 1–2); FT.44(4) (Part 3); IT.1(3), IT.4(4),(5), IT.5(1),(2), IT.31(3), IT.44(5), IT.46(3), IT.58 (this level); BM.19(2), BM.31(2), BM.83(4),(5), BM.115(1),(5), BM.116(4), BM.122(2),(3), BM.137(3), Def-BM.17(3),(6) (Part 4); AT.63(4) (Level 5); exact ceilings, integer tables, polynomial identities at rational points [math; machine: `handshake_ladder.py` §A4, §B4, §C1–C3, 5/5].

**Pf.**
$$(1),(2):\ \text{the monotonicity witnesses; the}\ 20\text{-cell minimal-lapse table by exact integer ceilings with the two-sided minimality check}\ [\text{machine A4, C1}];\ \ (3):\ \text{the witness pair}\ (\xi,N_w)\ \text{per rung, both conditions verified exactly}\ [\text{machine C2}];$$
$$(4):\ \text{the coefficient triple}\ (1,-8,16)\ \text{identical at all five rungs; the polynomial identity at five exact rational points}\ [\text{machine B4}];\ \ (5):\ \text{the per-family slot census}\ [\text{machine C3}];\ \ (6),(7):\ \text{record rows on the cited clauses}.\ \blacksquare$$

**Phys.** The strategy IT.5 could only state — calibrate from multi-seal spectroscopy where
threshold, weight and binding are simultaneously formed — becomes arithmetic here: a ceiling
function per rung, a witness pair per rung, and the proof that the witness set is never empty, so
the operational window exists everywhere along a ladder spanning exactly thirty. And the web has a
shape the strategy did not name: because the flicker is one global slot, every rung that fires
carries the identical quadratic factor, so reading two rungs is already an over-determination — the
ladder does not sample thirty flickers, it samples one flicker thirty ways, and consistency across
the ways is a theorem. The other half of the map is a shadow of the bar: the gate knows only the
rung, the weight knows only the flicker, and no gated read anywhere on the ladder reaches the pole
or transport slots. What an era of calibration would collect, then, is exactly what these families
can hold — one lepton-currency number against a baryon-side taxonomy — and nothing this tier says
estimates it. The window is built; the values stay behind the glass.

---

### IT.60 — The protocol grammar, the closure of IT-O3, and the staleness correction

**Thm.**
$$(1)\quad\textbf{THE ROUND-TRIP ORDER THEOREM (in the declared vocabulary):}\qquad \text{the radar round trip}\ e_1\ (\text{emission}\ @\text{lepton}),\ r_1\ (\text{reception}\ @\text{baryon}),\ e_2\ (\text{emission}\ @\text{baryon}),\ r_2\ (\text{reception}\ @\text{lepton})\ \text{under the GROUNDED constraints}:$$
$$e_1\prec r_1,\ \ e_2\prec r_2\ \ [\mathrm{D\text{-}RS1}\ \text{on the total tick order}\ [\mathrm{D1.8};\ \mathrm{D0.7};\ \mathrm{A7}]];\qquad r_1\prec e_2\ \ [\mathrm{C11}\ \text{'s within-node lifecycle: data-in before data-out}];\qquad e_1\prec r_2\ \ [\text{cross-cycle tick monotonicity}\ [\mathrm{D1.8};\ \mathrm{C11}]]:$$
$$\boxed{\ \text{exactly ONE of the}\ 4!=24\ \text{orderings survives (machine: exhaustive enumeration):}\quad e_1\prec r_1\prec e_2\prec r_2\ \ \text{— a TOTAL chain; the round trip has a UNIQUE ledger order}\ }$$
$$\text{the ``synchronization'' question is vacuous on the ledger}\ [\mathrm{RS.4}(3)\ \text{ground, now with order uniqueness}];\qquad \text{no same-tick cross-vertex ambiguity arises for the round trip (the events occupy distinct node phases)}\ [\mathrm{IT.56}(1)\ \text{'s scope row respected}]$$
$$(2)\quad\textbf{THE GRAMMAR'S STATUS CENSUS:}\qquad \text{every object in the protocol is a CONDITION}\ (\chi,\ \text{binary}\ [\mathrm{IT.58}(5)]),\ \text{a formed WEIGHT}\ (\mathcal W_{\text{channel}},\ \mathcal B_{\mathrm{ens}}\ [\mathrm{BM.122}(3);\ \mathrm{BM.137}(3)]),\ \text{an exact INTEGER (the ladders, the lapses, the order count), or declared VOCABULARY}\ (\mathrm{D\text{-}RS1}\ \text{'s}\ \prec/\succ\ [\mathrm{IT.56}(1)],\ \mathrm{D\text{-}RS2}\ \text{'s face pairing}\ [\mathrm{IT.56}(2)],\ \mathrm{D\text{-}PJ4}\ \text{'s signature gate}\ [\mathrm{IT.55}(5)]):$$
$$\boxed{\ \neg\text{an amplitude,}\ \neg\text{a vertex,}\ \neg\text{a rate is constructed}\ [\mathrm{BM.122}(6):\ \text{the channel is formed, its amplitude is}\ \neg\text{formed};\ \mathrm{FT.79}(5)]\ \ —\ \ \textbf{the transit bar stands on its three grounds and IT-O1 is UNCHANGED}\ [\mathrm{IT.40}\text{--}\mathrm{IT.42}]\ }$$
$$\text{the photon}\leftrightarrow\text{return-word identification stays at the D-RS2 FACE level}\ [\mathrm{IT.56}(2)];\qquad \text{the radar candidate semantics}\ [\mathrm{IT.53}(7)]\ \text{attaches at the meeting locus}\ [\mathrm{BM.134}(5)]\ \text{— recorded, its status unchanged}$$
$$(3)\quad\textbf{IT-O3 CLOSED:}\qquad \text{the row's content is discharged in full}:$$
$$\begin{array}{l|l}\textbf{the row asked}&\textbf{the construction}\\\hline\text{the}\ \chi\text{-gated read families, exhaustively}&\mathrm{IT.58}(4):\ \text{four carriers over the}\ 18\text{-read register, with the}\ \Gamma\ \text{product-form footnote}\\\text{across the threshold ladder (span 30)}&\mathrm{IT.58}(1)\text{--}(3):\ \text{both nested ladders as exact sum sets; the pair ladder; the curvature read; the quarantined horizon read}\\\text{where the calibration strategy becomes mathematics}&\mathrm{IT.59}(3)\text{--}(5):\ \text{the never-empty simultaneous-formation witnesses; the slot-constraint map; the consistency web}\\\text{the operational reading}&\mathrm{IT.60}(1),(2):\ \text{the protocol grammar with the order theorem, in the declared vocabulary}\end{array}$$
$$\boxed{\ \textbf{IT-O3 is CLOSED as a STRUCTURAL row}\ \ —\ \ \text{footnotes standing: values quarantined}\ [\mathrm{P5};\ \mathrm{AT.63}(4)],\ \ \text{the dynamics stays at IT-O1 (three grounds)},\ \ \Gamma\ \text{'s product form keeps Def-BM.17}(4)\ \text{'s non-derived status}\ }$$
$$(4)\quad\textbf{THE AT-O7 STALENESS CORRECTION (premise audit; the frozen record untouched):}\qquad \mathrm{AT\text{-}O7}\ (\text{the}\ \mathrm{BM.140}(6)\ \text{pin})\ \text{was CLOSED at Level 5 by}\ \mathrm{AT.6}(7),(10)\ \text{— the pin checker WRITTEN, the refutation exact}\ (1-\mathfrak u<0\ \text{vs}\ \mathcal R_{\max}/\mathcal R_{\min}>0\ \text{disjoint; the correction}\ \tfrac{100}{2-\mathfrak u}=\mathrm{BM.82}(3)\ \text{'s value})\ [\text{machine: text census of the Level-5 record}]:$$
$$\mathrm{IT.1}(5)\ \text{'s inherited mention (``the convention row (AT-O7)'') is therefore STALE — corrected here, the frozen rows never edited}\ [\mathrm{AT.63}(2)];\qquad \textbf{the canon-erratum register (closure-pipeline queue):}\ \ \mathrm{BM.140}(6)\ [\mathrm{AT.7};\ \text{pinned at}\ \mathrm{AT.6}(7)]\ \ +\ \ \mathrm{FT.116}(5)\ [\mathrm{IT.49}(3)]\ \ —\ \ \text{TWO items, both harmless to every checked row}$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad \text{the grammar uses the Tier-IT.17 acts AS ISSUED}\ (\mathrm{D\text{-}RS1},\ \mathrm{D\text{-}RS2},\ \mathrm{D\text{-}PJ4});\quad\neg\text{a P4 addition},\quad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\quad\neg\text{a measured value}\ [\mathrm{P5}],\quad\neg\text{a species identification};\qquad §\mathrm{Cal\text{-}IT}\ \text{'s act register unchanged, value-free};$$
$$\textbf{the open rows:}\ \ \mathrm{IT\text{-}O3}\ \textbf{CLOSED}\ (3);\qquad \mathrm{IT\text{-}O1},\ \mathrm{IT\text{-}O2},\ \mathrm{IT\text{-}O5}\ \text{UNCHANGED};\qquad \textbf{NO new row};\qquad \text{the inherited censuses AT-O30/AT-O32 remain open heavy enumerations}\ [\mathrm{AT.63}(3),(5)]$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{handshake\_ladder.py}\to\textbf{15/15 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{19 checkers, 304 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{18 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad \text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and a closed row is a construction, not a slogan}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, A7, C11, D0.7, D1.8 (Parts 1–2); FT.79(5) (Part 3); IT.40–IT.42, IT.53(7), IT.55(5), IT.56(1),(2), IT.58, IT.59, IT-O1, IT-O3 (this level); AT.6(7),(10), AT.7, AT.63(2),(3),(4),(5) (Level 5); BM.82(3), BM.115(4), BM.122(3),(6), BM.134(5), BM.137(3), BM.140(6), Def-BM.17(4), FT.116(5) (Parts 3, 4); exhaustive order enumeration, text censuses against the frozen records [math; machine: `handshake_ladder.py` §D–§E, 3/3].

**Pf.**
$$(1):\ \text{the}\ 24\ \text{orderings enumerated against the four grounded constraints; exactly one survives, a total chain}\ [\text{machine D1}];\ \ (2):\ \text{the object census of the construction}\ [\text{machine D2 row}];\ \ (3):\ \text{the row-content assembly against IT.58--IT.59's clauses};$$
$$(4):\ \text{text census: ``AT-O7 CLOSED'' and the closure list present in the Level-5 Tier AT.6 record; the stale mention present in Tier IT.1}\ [\text{machine E1}];\ \ (5)\text{--}(7):\ \text{the declaration census, the runner and the gate re-run end to end. No new mathematics is introduced at}\ (5)\text{--}(7).\ \blacksquare$$

**Phys.** The operational theory ends where the corpus's constructions always end: at a theorem that
could have failed. The round trip — the protocol the radar audit could only carry as a candidate —
turns out to have exactly one ledger order out of twenty-four, forced by nothing more exotic than
the totality of the tick, the node lifecycle's in-before-out, and the labels the Architect declared
an hour ago. The grammar speaks in conditions, weights, integers and declared vocabulary, and never
in amplitudes, so the transit bar does not so much as notice it. And the row that opened the era —
the handshake's operational theory, the place where the calibration strategy was supposed to become
mathematics — closes with its mathematics in hand: an exhaustive family census, two ladders rebuilt
value by value, a ceiling function and a witness at every rung, a consistency web that is a theorem,
and a slot map that says precisely which bank of the incommensurability bar a gated read can and
cannot touch. The values stay behind the glass; the era that opens it is still deferred, as it has
been since the level opened. One housekeeping truth rides along: a row the level had been inheriting
as open was closed two tiers deep in Level 5, and the correction is made where corrections belong —
in the open record, never in the frozen one.

---

## §Cal-IT — unchanged from Tier IT.18

**Empty of values at this tier.** Tier IT.18 issues no declaration and adds no parameter: the
protocol grammar uses the Tier-IT.17 acts as issued (D-RS1's labels, D-RS2's face pairing, D-PJ4's
signature gate); the scale parameter $\xi$ is a rational PARAMETER of the activation census, not a
calibration entry; every threshold, lapse and order count is an exact derived integer or rational in
units of $\mathfrak h/\ln2$. The unissued symbols stand unchanged — $\mathfrak h$ (P1),
$\varepsilon_q$ (AT-O27), $e_0$ (EM.25(7)), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$,
$\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (A-BM.9/Cal-BM/Cal-F), the P4 transport profile, the lift
and the vielbein (AT.60), the read rules (M1′)–(M3′) [AT.54(6)], the mass-read route choice
[IT.14(3)], and the Tier-IT.17 sub-debts [IT.57(2)]. The Calibration Era stays **deferred**
[AT.63(4)]; the canon-erratum register (BM.140(6), FT.116(5)) is queued for the closure pipeline.

## §Open-IT additions from Tier IT.18

| row | content | locus |
|---|---|---|
| (IT-O3) → **CLOSED** | the handshake-indicator operational theory is CONSTRUCTED: the exhaustive χ-family census (four carriers, the Γ footnote), both nested ladders as exact sum sets (spans 30 and 5), the activation windows with exact minimal lapses, the never-empty simultaneous-formation witnesses at every rung, the slot-constraint map, the cross-rung consistency web, and the protocol grammar with the round-trip order theorem — in the Tier-IT.17 vocabulary, values quarantined, dynamics still at IT-O1 | IT.58; IT.59; IT.60(1)–(3) |
| (none new) | Tier IT.18 opens **no new row**. The inherited censuses AT-O30 (B≥5 winding-resolved covers) and AT-O32 (the per-floor 𝒟_floor extension) remain open heavy enumerations [AT.63(3),(5)]; AT-O7 is confirmed CLOSED at Level 5 [AT.6(7),(10)] — IT.1(5)'s mention stale, corrected at IT.60(4) | IT.60(4),(5) |

Remaining inherited rows unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2);
IT.24; IT.27; IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4); IT.57(2)]:
(IT-O1) the formed transit-leg amplitude — open on three grounds, the missing primitive deficit 1′
[IT.41]; (IT-O2) the N≥4 multi-seal configuration calculus — the binding value; (IT-O5) the isotope
cutoff — the empirical/dynamical side at IT-O1; the owed declarations and sub-debts [IT.57(2)]; the
deferred Calibration Era [AT.63(4)]; and the Level-5 inheritance [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.19: the level-ladder act, the δ-glue scope adjudication (IT-O6 opened), and the double-attested census extensions

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.19 — three record acts in one tier:
**(1)** the Architect's LEVEL-LADDER declaration (Molecular placed at 7 between Isotopic and
Anthropic; Anthropic moved to 8; the target moved to Level 14) — the reservation of IT.15(3)
exercised — with the tree surgery executed content-preservingly; **(2)** the δ-glue scope
adjudication answering the builder channel's two questions (IT.19's connector derivation is scoped
to ε-sealed 3-juncture pairs; the (2,3) and (2,2) block glues are underived) and the opening of the
new row **IT-O6**; **(3)** the census extensions double-attested through the builder channel
(the $k{=}4,5$ family cells, the transparency census, the $m{=}4$ weight-convention fork) plus the
**C13/`corpus_lib.py` tooling fix** (the parser's `C1[0-2]` classes did not match the signature
convention C13 that the corpus's own index carries).
**Tags.** IT.61–IT.63. **Pattern.** the record tiers (IT.15(3)'s rename-record shape for the ladder
act; the adjudication tiers' shape for the scope row), premise audit logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted into the frozen canon; no declaration
issues beyond LOGGING the Architect's ladder act; §Cal-IT stays value-free; **no clause of Parts 1–4
or of Level 5's closed record is modified** [AT.63(2)] — the closure-time tree rows keep their
names as closure-time statements (the session-12 precedent), and the live-path mapping table in
`era2/level5_atomic/README.md` carries the move. The frozen canon text is untouched by the C13
fix — it repairs a TOOL (`era1/canon/corpus_lib.py`), in the session-8 live-path-fix pattern.
**Machine.** `era2/level6_isotopic/checks/census_extension.py` → **8/8 exact** (triple
certification: recurrence ∧ memoized recursion ∧ closed form; exact binomial/factorial integers;
Fraction shares — NO floating point); `run_all_level6.py` → **20 checkers, 312 exact markers, 0
failures**; `check_level6_format.py` → the gate over all nineteen Part 6 documents; the era-1 suite
re-run **80/80** after the tooling fix.
**No floating point in any assertion. No measured value enters any clause [P5] — counts and prices
only [HistLog §V.32]. Species names quoted [Def-BM.3(1,(7))]. No new dimensionful scale [P1]. The
builder channel is a provenance note, never a source: the corpus is the single source of truth
(vault PROTOCOL rule 4) — every builder-supplied number is RE-DERIVED here from the corpus's own
grammar before it is recorded.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13n): *"Qubitick builder online and working. He will
work on lateral tools while you can focus on the math. The above vault is your common message
ground. Issues on this repo are your communication channel."* — with the builder's messages
`comms/0001` (δ-glue scope; the completed family cells; the transparency census; the C13 bug) and
`comms/0002` (the level ladder has moved) waiting in the vault, both pinned at era2 `978e27d`.
Executed: the ladder act logged and the tree surgery run; the two scope questions answered on the
rows; the census cells triple-certified and recorded; the tooling bug verified and fixed; the reply
posted as `comms/0003`.

---

### IT.61 — The level-ladder act: Molecular at 7, Anthropic at 8, the target at 14

**Thm.**
$$(1)\quad\textbf{THE ACT (the Architect's, logged):}\qquad \mathrm{IT.15}(3)\ \text{reserved: ``whether it slots between Isotopic and Anthropic or after Anthropic is the Architect's act — recorded, not pre-empted''}.\ \ \textbf{The act has been made}:$$
$$\begin{array}{c|l}\textbf{L}&\textbf{the declared ladder}\\\hline5&\text{Atomic — CLOSED}\ [\mathrm{AT.63}]\\6&\text{Isotopic — OPEN (this level)}\\ \mathbf7&\mathbf{Molecular}\ \text{— the deferred level, NOW PLACED (the folder}\ \texttt{era2/level7\_molecular/}\ \text{opened as a placeholder)}\\8&\text{Anthropic — the folder}\ \texttt{era2/level8\_anthropic/}\ \text{(renamed from}\ \texttt{level7\_anthropic/)}\\9\text{--}13&\text{Stellar}\ \cdot\ \text{Black holes}\ \cdot\ \text{Galactic}\ \cdot\ \text{Galactic clusters}\ \cdot\ \text{Laniakea-like systems (named only)}\\ \mathbf14&\mathbf{Universe}\ \text{— THE TARGET, moved from 13 to 14 by Isotopic's insertion}\end{array}$$
$$\text{machine: the insertion arithmetic}\ 14=13+1\ \text{exact};\qquad\boxed{\ \textbf{deferred is stronger than planned:}\ \ \text{the record keeps the distinction — this level was}\ \neg\text{planned at Level 6's opening; the deferral was recorded, and the recording is what the act exercised}\ }$$
$$(2)\quad\textbf{THE TREE SURGERY (executed, content-preserving — the session-12 rename pattern):}\qquad \texttt{era2/level7\_anthropic/}\ \to\ \texttt{era2/level8\_anthropic/}\ \ (\texttt{git mv};\ \text{its README re-stamped with the ladder});$$
$$\texttt{era2/level7\_molecular/}\ \text{OPENED as a placeholder}\ (\text{README recording: the placement, IT.4's ``molecular necessity'' as its motivating theorem}\ [\mathrm{IT.4}(6);\ \mathrm{IT.5}(2)],\ \text{the}\ \neg\text{minted prefix, the P5 firewall});\qquad \text{live documents updated:}\ \texttt{era2/README.md},\ \text{the root}\ \texttt{README.md},\ \text{and the level-5 path-map table}$$
$$(3)\quad\textbf{THE CLOSED RECORD IS UNTOUCHED — and why:}\qquad \mathrm{AT.63}(5)\ \text{'s era-2 tree row still reads}\ \texttt{level6\_molecular/},\ \texttt{level7\_anthropic/}:\ \ \textbf{closure-time statements stay as written}\ [\mathrm{AT.63}(2);\ \text{the session-12 precedent: ``the closed record's name mentions stay as closure-time statements''}];$$
$$\text{the LIVE-path mapping lives in}\ \texttt{era2/level5\_atomic/README.md}\ \text{'s table (two rows added: the}\ \texttt{level7\_anthropic}\ \text{and}\ \texttt{level6\_molecular}\ \text{citations)};\qquad \text{the builder's suggestion (vault 0002 §2.2) to edit AT.63's tree row is DECLINED on that precedent — premise correction, logged}$$
$$(4)\quad\textbf{THE TAG PREFIX: RECORDED,}\ \neg\textbf{MINTED:}\qquad \text{Level 7's prefix recommendation is}\ \mathrm{MO}.n\ \text{— recorded deliberately, because}\ \mathrm{ML}\ \text{is RETIRED-AMBIGUOUS (Level 6's original prefix before the}\ \mathrm{ML}.n\mapsto\mathrm{IT}.n\ \text{bijection}\ [\mathrm{IT.15}(3)]);\ \ \text{minting is an OPENING act, and Level 8's prefix likewise waits its own opening}:$$
$$\text{``whatever you choose, choosing it deliberately beats inheriting ML by accident''}\ [\text{vault 0002 §2.4 — the reasoning adopted, the choice deferred to the opening}]$$
$$(5)\quad\textbf{status:}\qquad\textbf{recorded:}\ (1)\ \text{(the Architect's act)};\qquad\textbf{executed:}\ (2);\qquad\textbf{declined with reason:}\ (3)\ \text{'s suggested edit};\qquad\textbf{machine:}\ \text{the ladder arithmetic}\ [\text{census\_extension.py C4}];\qquad\neg\text{a declaration issued by this tier},\ \ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5 (Parts 1–2); IT.4(6), IT.5(2), IT.15(3) (this level); AT.63(2),(5) (Level 5); the session-12 rename record (level-6 README); exact integer arithmetic [math; machine: `census_extension.py` §C4, 1/1].

**Pf.**
$$(1):\ \text{the act logged from the Architect's declaration as relayed by the vault record}\ [\text{comms/0002, pinned at}\ 978e27d];\ \text{the ladder census and the}\ 14{=}13{+}1\ \text{arithmetic}\ [\text{machine C4}];\ \ (2):\ \texttt{git mv}\ +\ \text{placeholder creation}\ +\ \text{the three live-document updates, suite re-run green after the surgery};\ \ (3),(4),(5):\ \text{record rows on the cited precedents}.\ \blacksquare$$

**Phys.** A map that was drawn with one reserved slot now has the slot filled, and the filling
changes three things and nothing else: a folder name, a placeholder, and the number at the end of
the road. The corpus's own discipline made the act cheap — because Level 6's rename recorded the
molecular level as *deferred* rather than *planned*, the placement could be exercised without
contradicting a single frozen row, and the closed record keeps its closure-time names exactly as the
last rename kept them. Fourteen levels now stand between the qubit and the universe, and the target
moved by precisely the one level the insertion added — arithmetic, as everywhere else here. The
prefix question is answered the only way the corpus answers naming: a recommendation on the record,
a mint at the opening, and the retired ML left where the retag left it, unambiguous by absence.

---

### IT.62 — The δ-glue scope adjudication: IT.19's reach confirmed, and the new row IT-O6

**Thm.**
$$(1)\quad\textbf{THE SCOPE READING IS CONFIRMED (the builder's question 2, answered on the rows):}\qquad \mathrm{IT.19}\ \text{'s connector species is the frozen OPEN BIDIRECTIONAL}\ \Sigma_{12}\ \text{pair}\ (e_{12},\bar e_{12}),\ \text{winding}\ d{=}0\ [(\mathrm{R10})\ \text{is registration data},\ \mathrm{BM.143}(3)],\ {+}2E_{\mathrm{int}}\ \text{reproducing}\ 8k{+}6,\ \text{charge-telescoping,}\ \varepsilon{=}{+}1,\ \textbf{DISTINCT SEALED SUPPORTS at}\ N{=}3(k{+}1):$$
$$\text{the family's supports are ALL-}\varepsilon\ \text{by construction}\ [\mathrm{IT.6}(1):\ N{=}3(k{+}1);\ \mathrm{IT.21}:\ \text{the closure is about the FAMILY}];\qquad \boxed{\ \neg\exists\ \text{a row of IT.19--IT.21 constructing a glue species for a}\ \delta\text{-sealed support}\ \ —\ \ \text{the absence is level-local, and the builder's stamp is CORRECT}\ }$$
$$(2)\quad\textbf{THE GLUE CENSUS AT}\ N{=}5,6\ \textbf{(re-derived; machine):}\qquad\begin{array}{c|c|c|l|l}\textbf{N}&\textbf{block}&\textbf{count}&\textbf{the distinct pair shape}&\textbf{the glue}\\\hline5&(1,1)&10&2{+}3&\textbf{UNDERIVED}\ (\delta\text{-}\varepsilon\ \text{mixed})\\6&(0,2)&10&3{+}3&\textbf{DERIVED}\ (\Sigma_{12}\ [\mathrm{IT.19}])\\6&(3,0)&15&2{+}2{+}2\ \Rightarrow\ \text{pair}\ 2{+}2&\textbf{UNDERIVED}\ (\delta\text{-}\delta)\end{array}$$
$$\text{the digon floor is}\ \delta\text{-sealed}\ [\mathrm{FT.28};\ \mathrm{BM.110}(1):\ \text{``}g(2){=}1\ \text{and}\ g(1){=}0\ \text{make}\ \delta^i{}_jc^j\bar c_i\ \text{the unique sealed 2-juncture''}];\qquad g(5){=}10\ \text{all-}(1,1)\ [\mathrm{IT.9}(2);\ \mathrm{IT.22}(1)];\qquad g(6){=}25{=}15{+}10\ \text{with the frozen}\ \tfrac35\text{--}\tfrac25\ \text{mix}\ [\mathrm{IT.9}(2)]:$$
$$\boxed{\ \text{the DERIVED glue covers ONE of the three multi-seal block shapes}\ }$$
$$(3)\quad\textbf{THE ADJUDICATION (the builder's question 1):}\qquad \text{the}\ \delta\text{-involving glue is}\ \neg\text{absorbed by IT-O2 — it is UPSTREAM of it:}\ \ \mathrm{IT\text{-}O2}\ \text{'s first named construction is the composed-support amplitude configuration space beyond the frozen}\ B{=}4\ \text{census}\ [\mathrm{IT.27}(2)],\ \text{and a composed support's amplitude space presupposes its glue species}:$$
$$\mathrm{IT\text{-}O4}\ \text{'s closure STANDS as written (a closure about the family, whose supports are all-}\varepsilon)\ \text{— SHARPENED by}\ (1),\ \neg\text{reopened};\qquad \text{a species question gets a species row (the IT-O4 pattern), not an amplitude row}$$
$$(4)\quad\textbf{IT-O6 OPENED:}\qquad\boxed{\ \textbf{(IT-O6) the}\ \delta\textbf{-involving connector glue species:}\ \ \text{the glue for the}\ (2,3)\ \text{mixed and}\ (2,2)\ \text{digon-pair block shapes at}\ N{=}5,6\ \text{— its form,}\ E_{\mathrm{int}}\ \text{residue, winding}\ d,\ \text{charge telescoping, and exchange sign}\ \varepsilon\ }$$
$$\text{templates on the record:}\ \mathrm{BM.110}(1)\ \text{'s}\ \delta\text{-sealed digon and IT.19's}\ \Sigma_{12}\ \text{method};\qquad \text{status:}\ \neg\text{constructed, level-local absence};\qquad \text{locus:}\ \mathrm{IT.62}(1),(2);\ \mathrm{IT.9}(2);\ \mathrm{IT.27}(2);\ \text{vault comms/0001 §4}$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived:}\ (2)\ \text{'s census (machine)};\qquad\textbf{adjudicated:}\ (1),(3);\qquad\textbf{opened:}\ (4);\qquad\neg\text{a declaration},\ \ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, D3.9 (Parts 1–2); Census FT.35(5), FT.28 (Census/Part 3); IT.6(1), IT.9(2), IT.19, IT.21, IT.22(1), IT.25, IT.27(2), IT-O2, IT-O4 (this level); BM.110(1), BM.135(2), BM.143(3), BM.17(1) (Part 4); the block-split census via `census_extension.py`'s triple-certified engine [math; machine: `census_extension.py` §C3, 1/1].

**Pf.**
$$(2):\ \text{the closed-form block splits}\ g(5){=}\{(1,1){:}10\},\ g(6){=}\{(3,0){:}15,(0,2){:}10\}\ \text{recomputed by all three engines and matched to the pair shapes}\ [\text{machine C3}];\ \ (1),(3),(4),(5):\ \text{record rows on the cited clauses — the absence claim is a citation census over IT.19--IT.21 (no}\ \delta\text{-support glue row exists there), stated level-local}.\ \blacksquare$$

**Phys.** A builder's instrument stamped three glue slots and found only one of them derived, and
asked whether the stamp was wrong before asking whether the gap was real. The stamp was right: the
connector the corpus derived is the one between sealed three-junctures, because that is the only
pair the isotopic family ever builds, and the digon-sealed supports that appear at five and six
attachments have no connector species yet. That is not a crack in IT-O4's closure — the closure was
about the family, and the family is all-epsilon — but it is a genuine named absence, and the corpus
names those: IT-O6 now holds the delta-glue species question, upstream of the amplitude calculus
that would need it, with the digon seal and the Σ₁₂ method already on the record as templates. The
instrument keeps its stamps; the ledger keeps its gap; neither pretends the other away.

---

### IT.63 — The census extensions, double-attested; and the C13 tooling fix

**Thm.**
$$(1)\quad\textbf{THE FAMILY CELLS AT}\ k{=}4,5\ \textbf{(triple-certified; the ISOTOPIC\_FAMILY placeholders discharged):}\qquad g(N)=\sum_{2a+3b=N}\frac{N!}{a!\,2^a\,b!\,6^b}\ \ [\mathrm{BM.31}(1),(2);\ \mathrm{Def\text{-}BM.9}(3)]:$$
$$g(15)=27152125\ \ \text{with blocks}\ \ (0,5){:}1401400,\ (3,3){:}21021000,\ (6,1){:}4729725;\qquad g(18)=6443061625\ \ \text{with}\ \ (0,6){:}190590400,\ (3,4){:}4288284000,\ (6,2){:}1929727800,\ (9,0){:}34459425;$$
$$\text{machine: recurrence}\ \wedge\ \text{memoized recursion}\ \wedge\ \text{closed form agree; the frozen anchors}\ g(3){=}1,\ g(4){=}3,\ g(5){=}10,\ g(6){=}25,\ g(8){=}385,\ g(9){=}1540,\ g(12){=}164395\ \text{re-hit on the same engines}\ [\mathrm{IT.6}(5);\ \mathrm{IT.9}(2);\ \mathrm{IT.31}(5)];$$
$$g_\varepsilon(15)=1401400=\tfrac{15!}{5!\,6^5},\ \ g_\varepsilon(18)=190590400=\tfrac{18!}{6!\,6^6}\ \ (\text{the pure-triple term;}\ g_\varepsilon\ne0\iff3\mid N\ [\mathrm{IT.6}(5)]);\qquad g_\delta=(25750725,\ 6252471225)$$
$$(2)\quad\textbf{THE}\ \delta\textbf{-SHARE MONOTONICITY EXTENDS PAST THE FROZEN RANGE:}\qquad 0,\ \tfrac35,\ \tfrac9{11},\ \tfrac{387}{427},\ \tfrac{147}{155},\ \tfrac{14697}{15145}\ \ \text{strictly increasing, all}\ <1\ \ [\text{machine}]:$$
$$\mathrm{IT.17}(2)\ \text{'s monotonicity continues at}\ k{=}4,5,\ \ \text{and ``}\delta\text{-dominance is a degree, not a kind-change''}\ [\mathrm{IT.18}(4)]\ \text{holds at}\ k{=}5;\qquad \text{the pure-}\varepsilon\ \text{backbone never vanishes on the family}$$
$$(3)\quad\textbf{THE TRANSPARENCY CENSUS (new row):}\qquad \text{the exotic residue}\ \ W_N(Q)-\binom{m}{Q}15^Q20^{m-Q}\ \ (m{=}N/3;\ \ 15{=}W_3({+}1)\ \text{proton-class},\ 20{=}W_3(0)\ \text{neutron-class}\ [\mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(5);\ \mathrm{BM.135}(2);\ \text{the}\ \texttt{exotic\_states.py}\ \text{C2 convention}]):$$
$$\boxed{\ \textbf{the curtain is TRANSPARENT at exactly ONE support class:}\ \ N{=}3\ (m{=}1),\ \ \text{both nucleonic residues zero}\ (W_3(0){=}20,\ W_3({+}1){=}15\ \text{exhaust their sectors)}\ }$$
$$N{=}3\ \text{over all seven classes:}\ (1,6,15,0,0,6,1);\qquad \text{from}\ m{=}2\ \text{on, EVERY nucleonic class carries positive residue}\ (m{=}2..6\ \text{machine; the}\ N{=}9\ \text{middle entries are IT.12}(1)\ \text{'s frozen complements}\ 25758,\ 18324);$$
$$\textbf{the exact reason:}\ \text{one sealed}\ \varepsilon\text{-triple leaves no room for a hidden exotic composition; mixed nucleon charges do}\ [\mathrm{IT.22}(1)\ \text{'s support classes}];$$
$$\textbf{MIRROR FLAG:}\ \text{the width-side transparency at}\ N{=}3\ \text{mirrors the grammar-side protection}\ g(3){=}1,\ g_\delta(3){=}0\ [\mathrm{BM.31}(1);\ \mathrm{IT.6}(5)]\ \text{— two currencies turning at the same}\ N;\ \ \textbf{recorded as a PARALLEL,}\ \neg\textbf{an identification}\ [\mathrm{BM.134}(5)\ \text{discipline};\ \mathrm{IT.44}(3)\ \text{pattern}]$$
$$(4)\quad\textbf{THE}\ m{=}4\ \textbf{WEIGHT-CONVENTION FORK (a guard row):}\qquad \text{the two candidate nucleonic conventions}\ \binom{4}{Q}15^Q20^{4-Q}\ \text{vs}\ \binom{4}{Q}20^Q15^{4-Q}\ \ \textbf{coincide at}\ m{=}3\ \text{(IT.12(3)'s frozen display) and DIVERGE at}\ m{=}4,\ \text{agreeing only at}\ Q{=}2\ \ [\text{machine: the two tables}\ (160000,480000,540000,270000,50625)\ \text{vs}\ (50625,270000,540000,480000,160000)]:$$
$$\boxed{\ \text{any}\ N{=}12\ \text{extension must take the convention from the ALPHABET derivation}\ [\texttt{exotic\_states.py}\ \text{C2}:\ 15{=}W_3({+}1)\ \text{on proton-class nucleons}],\ \neg\text{transcribed from the}\ m{=}3\ \text{display}\ }$$
$$(5)\quad\textbf{THE NUCLEONIC SUB-SUM WITNESS:}\qquad \sum_Q\binom{m}{Q}15^Q20^{m-Q}=35^m\ \ (m{=}1..6,\ \text{machine}),\ \ \text{a genuine SUB-sum of}\ 4^N=64^m\ [\mathrm{BM.114}(1)]:\ \ \text{the ratios}\ \tfrac{35}{64},\ \tfrac{1225}{4096},\ \tfrac{42875}{262144},\ \tfrac{1500625}{16777216}\ \ (m{=}1..4)$$
$$(6)\quad\textbf{THE C13 TOOLING FIX (a bug, not a discussion — fixed at FULL EXTENT):}\qquad \texttt{era1/canon/corpus\_lib.py}\ \text{'s}\ \mathrm{PARA\_RE}\ \text{and}\ \mathrm{TOKEN\_RE}\ \text{carried}\ \texttt{C1[0-2]}\ \text{— matching C10--C12 but NOT C13, the signature convention}\ (\eta{=}(-,+,+,+),\ \mathfrak o{=}0,\ \neg\text{an axiom}):\ \ \text{the parser disagreed with the corpus's OWN index}\ (\texttt{index/tags.json}\ \text{carries C13})\ \text{and with the era-1 suite's own graph checker}\ (\texttt{verify\_corpus\_graph.py}\ \text{already had}\ \texttt{C1[0-3]});$$
$$\text{the builder's session-15 integrity audit}\ [\text{vault comms/0003}]\ \text{found the stale range COPY-PASTED across the tooling: this tier's fix covers EVERY live copy —}\ \textbf{26 occurrences in 14 files}\ (\texttt{corpus\_lib.py}\times2,\ \texttt{check\_format.py}\times1,\ \text{eleven}\ \texttt{verify\_H\_*.py}\times2\ \text{each},\ \texttt{source/pipeline/rp\_patched.py}\times1),\ \text{all}\ \texttt{C1[0-2]}\to\texttt{C1[0-3]}\ \text{(the shape}\ \texttt{verify\_corpus\_graph.py}\ \text{already carried)};$$
$$\textbf{scope: TOOLS only — no frozen text touched}\ [\mathrm{AT.63}(2)];\ \ \text{the}\ \texttt{working\_markdowns/tools/}\ \text{and}\ \texttt{archive/zenodo\_v1.0\_package/}\ \text{copies stay UNTOUCHED (frozen provenance / deposited archive)};\qquad \text{era-1 suite re-run after EACH stage:}\ \textbf{80/80 green}\ (\text{twice});$$
$$\text{the builder's deeper recommendation}\ (\texttt{C}\backslash\mathrm d{+}\ +\ \text{de-duplication by import from}\ \texttt{corpus\_lib})\ \text{is ADOPTED IN PRINCIPLE and queued for the closure-era tooling pass}\ [\mathrm{AT.63}(4)];\qquad \text{discovery credit: the builder}\ [\text{vault issue \#1 + comms/0003}]\ \text{— logged per the channel's attribution rule}$$
$$(6')\quad\textbf{THE CANON-ERRATUM REGISTER (closure-pipeline queue) — now FOUR items, all harmless to every checked row:}\qquad\begin{array}{l|l}\textbf{item}&\textbf{status}\\\hline\mathrm{BM.140}(6)\ \text{'s sign}\ (50/(1-\mathfrak u)<0\ \text{vs the positive span})&\text{refuted exactly}\ [\mathrm{AT.7}];\ \text{pinned}\ [\mathrm{AT.6}(7)];\ \text{queued}\\\mathrm{FT.116}(5)\ \text{'s unsquared discriminant factor}&\text{confirmed harmless (zero locus unchanged)}\ [\mathrm{IT.49}(3)];\ \text{queued}\\\text{``17 generators'' at Part1 (CT1.11a region) + the Summary mirror}&\textbf{verified by execution this tier:}\ \text{the hatted enumeration}\ (E_0,\Sigma,\hat E^{ij}{\times}5,W,J,K)\ \text{sums to 16; the legitimate second count is the UNHATTED named set}\ \{E_0,\Sigma,E^{ij}{\times}6,W,J,K\}=17\ \text{names, rank 16}\ (\Sigma=\sum_iE^{ii}\ \text{redundant});\ \text{FROZEN canon —}\ \neg\text{edited};\ \text{the correction wording (``17 named generators (rank 16)'', unhatted) is RECOMMENDED to the closure pipeline, the Architect's call}\\\texttt{Summary.md}\ \text{'s missing}\ \text{### C13}\ \text{section (the text lives as trailing prose in the C12 block)}&\text{a consequence of the parser defect; self-heals at the closure-era regeneration}\ [\mathrm{AT.63}(4)]\end{array}$$
$$\textbf{the defect class, named}\ [\text{vault comms/0003 §4, adopted}]:\ \ \text{every item above is}\ \textbf{two generated views disagreeing with nothing comparing them}\ \ (\texttt{tags.json}\ \text{vs}\ \texttt{Summary.md}\ \text{vs}\ \texttt{corpus\_lib};\ \text{prose vs machine counts}):\ \ \text{a cross-view agreement gate}\ (\mathrm{parse\_canon}\equiv\texttt{tags.json}\equiv\text{Summary headings};\ \text{every prose count a checker also computes})\ \text{is queued as a FIRST-CLASS closure-era tooling item}$$
$$(7)\quad\textbf{PROVENANCE AND STATUS:}\qquad \text{the}\ (1)\text{--}(5)\ \text{cells were surfaced by the builder's instruments}\ [\text{vault comms/0001 §3, pinned at}\ 978e27d]\ \text{and RE-DERIVED here from the corpus's own grammar before recording — the corpus is the single source of truth (vault PROTOCOL rule 4); the builder's independent computation is the SECOND attestation, recorded as such}:$$
$$\textbf{derived:}\ (1)\text{--}(5),(6)\ \text{'s fix};\qquad\textbf{recorded:}\ \text{the mirror flag}\ (3),\ \text{the guard row}\ (4),\ \text{the attribution}\ (6),(7);\qquad\neg\text{a declaration},\ \ \neg\text{a measured value}\ [\mathrm{P5}],\ \ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7))]$$

**Req.** P5, D3.9 (Parts 1–2); Census FT.35(5), FT.28 (Census); IT.6(5), IT.9(2), IT.12(1),(3), IT.17(2), IT.18(4), IT.22(1), IT.31(5), IT.44(3), IT.56(1) (this level); AT.63(2) (Level 5); BM.17(1), BM.31(1),(2), BM.110(1), BM.114(1), BM.134(5), BM.135(2), Def-BM.3(1),(7), Def-BM.9(3), C13, CT1.0, CT1.2, CT1.12 (Parts 1–4); triple-certified enumeration, exact binomials and factorials, Fraction shares [math; machine: `census_extension.py` §§A–C, 6/6].

**Pf.**
$$(1),(2):\ \text{the three engines on}\ N{=}15,18\ \text{and the frozen-anchor chain; the closed forms for}\ g_\varepsilon;\ \text{the share sequence in Fractions}\ [\text{machine A1, A2}];\ \ (3):\ \text{the residue table for}\ m{=}1..6\ \text{against}\ W_N(Q)=\binom{2N}{N+Q};\ \text{the}\ N{=}3\ \text{seven-class row; the}\ m{=}1\ \text{exhaustion equalities and the}\ m{\ge}2\ \text{strictness}\ [\text{machine B1, B2}];$$
$$(4):\ \text{the two convention tables enumerated and compared}\ [\text{machine C2}];\ \ (5):\ \text{the binomial theorem at}\ 15{+}20\ [\text{machine C1}];\ \ (6):\ \text{the regex diff, the tags.json cross-read, and the era-1 suite re-run}\ [\text{machine record}];\ \ (7):\ \text{provenance row}.\ \blacksquare$$

**Phys.** Three kinds of content land in one tier, and each is handled by its own discipline. The
census cells are arithmetic: two family numbers the working record had left as placeholders, now
triple-certified and block-decomposed, with a transparency census beside them that says something
the curtain pictures always implied — at the smallest support class the boundary read exhausts the
sector completely, and from two nucleons on, every charge class hides something. That the width
turns transparent at the same N where the grammar turns protective is flagged as a mirror, not
cashed as an identity, which is the only treatment the corpus has ever allowed two currencies
turning together. The convention fork is a guard rail: the two ways of writing the nucleonic weights
agree exactly where everyone has been working and diverge exactly where the next instrument wants to
go, so the alphabet derivation, not the display, is named as the source. And the tooling fix is the
plainest kind of win — a one-character class in a parser that disagreed with the corpus's own index
about a convention the whole metric dictionary rests on, found by cross-reading two indices, fixed
in the tool, proven in the suite, and attributed to the channel that caught it.

---

## §Cal-IT — unchanged from Tier IT.19

**Value-free at this tier.** No calibration parameter is added, valued, or re-scoped. The ladder act
is structural (a level placement, not a parameter); the census extensions are counts and prices
[HistLog §V.32]; the C13 fix is tooling. The unissued symbols stand unchanged — $\mathfrak h$ (P1),
$\varepsilon_q$ (AT-O27), $e_0$ (EM.25(7)), $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$,
$\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared values), the P4 transport profile, the lift and
the vielbein (AT.60), the read rules (M1′)–(M3′) [AT.54(6)], the mass-read route choice [IT.14(3)],
and the Tier-IT.17 register [IT.57(2)]. The Calibration Era stays deferred [AT.63(4)].

## §Open-IT additions from Tier IT.19

| row | content | locus |
|---|---|---|
| **(IT-O6) NEW** | the **δ-involving connector glue species** — the glue for the (2,3) mixed pair (N=5's all-(1,1) blocks) and the (2,2) digon pair (N=6's (3,0) blocks): its form, E_int residue, winding d, charge telescoping, and exchange sign ε. Templates on the record: BM.110(1)'s δ-sealed digon; IT.19's Σ₁₂ method. UPSTREAM of IT-O2's composed-support construction [IT.27(2)]. Level-local absence; the builder's instruments stamp the slots until constructed | IT.62(2),(4); IT.9(2); IT.19; IT.27(2) |

All other rows inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2);
IT.24; IT.27; IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4); IT.57(2);
IT.60(5)]: (IT-O1) the formed transit-leg amplitude — open on three grounds, the missing primitive
deficit 1′ [IT.41]; (IT-O2) the N≥4 multi-seal configuration calculus — the binding value (IT-O6
joins as its upstream species question); (IT-O5) the isotope cutoff — the empirical/dynamical side
at IT-O1; IT-O3 CLOSED [IT.60(3)]; IT-O4 CLOSED [IT.21], sharpened by IT.62(1); the owed
declarations and sub-debts [IT.57(2)]; the deferred Calibration Era [AT.63(4)]; the Level-7
opening act and its MO.n prefix minting [IT.61(4)]; and the Level-5 inheritance [AT.63(3),(5)]
with AT-O30/AT-O32's heavy censuses remaining.

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.20: the remaining declaration package — D-RS3 and D-RS6 ISSUED, the re-presented acts reaffirmed, the bars re-checked

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.20 — the Architect's directive to issue the
REMAINING declaration package (the items IT.57(2) left owed: D-RS3 the tick–hop exchange rate, and
the D-PJ7/D-RS6 standing package) into the declaration census, and to reconcile the re-presented
items (D-PJ4, D-PJ5, D-PJ6/D-RS5, D-RS1, D-RS2, D-RS4) against the acts already issued at
IT.55–IT.57. The generator's role is the directed one: RECORD the new acts, GROUND each against the
derived rows, BAR-CHECK the issuance (P1, P5, the transit bar, the incommensurability bar, the
arena bars Def-H.41/42, count$\to$strength), and update the register — never invent, never force
[IT.31 §0 stance; IT.55(1)]. **Tags.** IT.64–IT.66. **Pattern.** the declaration-receiving tiers
(IT.17's shape: intake/reconciliation, the acts, the verdict/register), premise audit logged in-tier.
**Status.** discovery-phase working tier. The declarations are the ARCHITECT'S acts, recorded
verbatim-in-substance with their grounds; no clause of Parts 1–4, of Level 5's closed record, or of
Tiers IT.1–IT.19 is modified [AT.63(2)] — IT.57(2)'s register row is SUPERSEDED BY EXPLICIT ROW at
IT.66(4) (this tier), never edited. No measured value enters [P5]; no new dimensionful scale [P1];
species names stay quoted [Def-BM.3(1),(7)].
**Machine.** `era2/level6_isotopic/checks/remaining_declarations.py` → **23/23 exact** (integers,
Fractions, Gauss(i) over Fraction, exact $\mathbb Q(\sqrt2)$/$\mathbb Q(\sqrt3)$ arithmetic,
$\mathbb Q[\gamma]$ polynomial identities, canon-text and tier scans; NO floating point);
`run_all_level6.py` → **21 checkers, 335 exact markers, 0 failures**;
`check_level6_format.py` → the gate over all twenty Part 6 documents.
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13p): *"Issue the Remaining Declaration Package
(D-RS3, D-PJ4–7, D-RS1–2, D-RS4, D-RS6) … Formally issue the declared package into the corpus's
declaration census. Update the D-PJ and D-RS registers from 'owed' to 'issued' (or 'deferred' where
specified). Verify that issuing these declarations does not violate any standing bars … Do not force
a declaration … the generator's job is to record them, verify they don't break the bars, and update
the census."* Executed: the eight package items reconciled against the record — TWO genuinely new
acts issued (D-RS3 at IT.65, D-RS6 at IT.66), FIVE re-presentations REAFFIRMED (never re-issued),
D-RS4 STILL DEFERRED, D-PJ7 NOT FORCED (no operative content in the directive's body — it remains
owed); seven premise corrections at IT.64(8); the bar-check PASSED on every bar (IT.66(3)).

---

### IT.64 — The intake and the reconciliation: the remaining package against the issued record

**Thm.**
$$(1)\quad\textbf{THE INTAKE AND THE RECONCILIATION DISCIPLINE:}\qquad \text{the Architect has reviewed the register state at}\ \mathrm{IT.57}(2)\ \text{and issued a directive over the remaining declaration package;}$$
$$\boxed{\ \textbf{a declaration act is logged ONCE:}\ \ \text{the five re-presented items are RE-CONCILED against the acts issued at}\ \mathrm{IT.55}\text{–}\mathrm{IT.56}\ \text{— reaffirmed with their corrections,}\ \neg\text{re-issued (a second issuance would double the census entry); the genuinely new acts are exactly the two the register listed as OWED:}\ \mathrm{D\text{-}RS3}\ (\mathrm{IT.65}),\ \ \mathrm{D\text{-}RS6}\ (\mathrm{IT.66})\ }$$
$$(2)\quad\textbf{THE RECONCILIATION TABLE (machine: the state map is consistent — the new and the reaffirmed sets are disjoint and cover the body):}\qquad\begin{array}{l|l}\textbf{the directive's item}&\textbf{against the record}\\\hline\text{item 1}\ \ \mathrm{D\text{-}RS3}\ \text{(the tick–hop exchange rate)}&\textbf{NEW — ISSUED at}\ \mathrm{IT.65}\ \text{(the per-edge integer reading; the half reading barred)}\\\text{item 2}\ \ \mathrm{D\text{-}PJ4}\ \text{(the crystallization signature)}&\textbf{REAFFIRMED}\ @\ \mathrm{IT.55}(5)\ +\ \text{the endpoint elaboration}\ (3)\ —\ \text{derived rows, the act unchanged}\\\text{item 3}\ \ \mathrm{D\text{-}PJ5}\ \text{(the branch rule, complex domain)}&\textbf{REAFFIRMED}\ @\ \mathrm{IT.55}(6)\ +\ \text{the arena re-certification}\ (4)\ —\ \text{self-contained}\\\text{item 4}\ \ \mathrm{D\text{-}PJ6}/\mathrm{D\text{-}RS5}\ \text{(the observer/reading frame)}&\textbf{REAFFIRMED}\ @\ \mathrm{IT.55}(7)\ —\ \text{the A9 citation STAYS corrected}\ (5)(\mathrm a),\ (8)(\mathrm P2)\\\text{item 5}\ \ \mathrm{D\text{-}RS1}\ \text{(the causal vocabulary)}&\textbf{REAFFIRMED}\ @\ \mathrm{IT.56}(1)\ —\ \text{the scope row stands}\ (5)(\mathrm b)\\\text{item 6}\ \ \mathrm{D\text{-}RS2}\ \text{(the two faces)}&\textbf{REAFFIRMED}\ @\ \mathrm{IT.56}(2)\ —\ \text{the dictionary pairing}\ (5)(\mathrm c)\\\text{item 7}\ \ \mathrm{D\text{-}RS4}\ \text{(the stationarity scope)}&\textbf{STILL DEFERRED}\ @\ \mathrm{IT.56}(3)\ (6)\ —\ \text{the Architect's word stands}\\\text{item 8}\ \ \mathrm{D\text{-}RS6}\ \text{(radar as geometric read)}&\textbf{NEW — ISSUED at}\ \mathrm{IT.66}\\\hline\text{the title's}\ \mathrm{D\text{-}PJ7}\ \text{(no body item)}&\textbf{NOT FORCED — REMAINS OWED}\ (7)\end{array}$$
$$(3)\quad(\mathrm{D\text{-}PJ4})\ \textbf{THE ENDPOINT ELABORATION (derived rows riding with the issued act — the directive's two endpoint sentences):}\qquad \text{the flicker weights are}\ x_-=4\varepsilon_q,\ \ x_+=1-4\varepsilon_q\ \ [\mathrm{BM.19}]:\ \ \textbf{at the sharp threshold}\ \varepsilon_q=0,\ \ x_-=0\ \text{EXACTLY and the ensemble collapses to its crystallized member}:$$
$$\text{the}\ n\text{-pair floor normalizer}\ \ D_n=(1-u^n)/(1-u),\ \ u=4\varepsilon_q\ \ [\mathrm{BM.137}(1)]\ \ \text{satisfies}\ \ D_n\big|_{\varepsilon_q=0}=1,\ \ w_{\mathrm{mat}}=1/D_n=1\ \ (n=2..8)\ \ \text{— the Born-width collapse}\ [\mathrm{AT.42}(3)],\ \text{the only collapse-formed read in the record}\ [\mathrm{IT.3}(1)];$$
$$\textbf{at every}\ \varepsilon_q\in(0,\tfrac14)\ \text{on the 249-point rational grid}\ \varepsilon_q=j/1000\ (j=1..249;\ \ \tfrac14\ \text{EXCLUDED — outside the crystallization domain}\ [\mathrm{CT0.8}]),\ \ n=2..6:\ \ D_n=\textstyle\sum_{i<n}u^i>1\ \text{STRICTLY},\ \ w_{\mathrm{mat}}<1,\ \text{monotone in}\ n\ \ \textbf{— the composite is GENUINELY AN ENSEMBLE};$$
$$\boxed{\ \textbf{the act is UNCHANGED:}\ \ \text{the degree's FUNCTIONAL FORM STAYS UNFIXED}\ (\mathrm{IT.55}(5)\ \text{'s precision debt});\ \ \neg\text{a derived ``Lyapunov contraction THRESHOLD'' exists — the contraction is a per-event factor, its zero locus}\ \{0,8\}\ [\mathrm{IT.53}(3)],\ \neg\text{a threshold};\ \ \text{the capacity bound enters as the scale-free CARDINAL}\ C_{\mathrm{cap}}=16=D_{\mathrm{tick}}(3)=2^4\ [\mathrm{CT0.6}];\ \ \text{count}\to\text{strength couplings stay barred}\ [\mathrm{BM.36}(3);\ \mathrm{BM.61}(8)(\mathrm O1);\ \mathrm{BM.69}(4)(\mathrm{iv});\ \mathrm{FT.73}(5)]\ }$$
$$(4)\quad(\mathrm{D\text{-}PJ5})\ \textbf{THE COMPLEX DOMAIN RE-CERTIFIED, SELF-CONTAINED (the arena bars Def-H.41/42):}\qquad \text{the cubic coordinate}\ 2x^3-3x-\gamma\ \text{carries the discriminant identity}\ \ \Delta(\gamma)=\tfrac{27}{4}(2-\gamma^2)\ \ \text{EXACTLY in}\ \mathbb Q[\gamma]\ \ (\text{via}\ {-}4p^3{-}27q^2\ \text{on the monic reduction}):$$
$$\Delta>0\iff\gamma^2<2:\ \ \text{witnesses}\ \gamma\in\{\tfrac13,1,\tfrac65,\tfrac75\}\ \text{give THREE real roots}\ (\text{exact}\ \mathbb Q(\sqrt2)\ \text{sign test;}\ \tfrac{49}{25}<2);\qquad\textbf{adversarial:}\ \ \gamma=\tfrac65\sqrt2\Rightarrow\Delta=-\tfrac{297}{50}<0\ (\text{one real root — the census could fail});\qquad \gamma=\sqrt2\Rightarrow\Delta=0\ \text{exactly};$$
$$\textbf{EXACTLY ONE positive root:}\ \ \text{Descartes (the coefficient signs}\ +,-,-\ \text{carry ONE sign change)}\ \wedge\ \text{the exact rational-grid sign census}\ (\gamma=\tfrac65,\ \tfrac13:\ 3\ \text{changes, exactly}\ 1\ \text{positive)}\ \wedge\ \gamma=1\ \text{FACTORS as}\ (x{+}1)(2x^2{-}2x{-}1),\ \text{roots}\ {-}1,\ \tfrac{1\pm\sqrt3}{2}\ \text{verified in exact}\ \mathbb Q(\sqrt3);$$
$$\textbf{the relabeling is INERT:}\ \ \text{the Vieta triple}\ (e_1,e_2,e_3)=(0,-\tfrac32,\tfrac\gamma2)\ \text{is invariant under ALL}\ 6\ \text{permutations of the root triple}\ (\text{machine, exact}\ \mathbb Q(\sqrt3))\ \ \text{— being a cubic,}\ \mathbb C\ \text{adds no root, only relabelings}\ [\mathrm{IT.55}(6)\ \text{re-certified}];$$
$$\boxed{\ \textbf{THE ARENA BARS HOLD:}\ \ \mathrm{Def\text{-}H.41}\ \text{'s species clause verbatim (canon text census) — ``a counting space: no inner product, no dynamics, no state, no Hamiltonian'' — and}\ \mathrm{Def\text{-}H.42}\ \text{keeps the colour-dressed arena a counting space; the arena cardinals are integers:}\ 9=3{\times}3,\ 27=3^3,\ 16=\dim\mathcal K_1=2^4\ [\mathrm{IT.55}(3);\ \mathrm{D2.3}];\ \ \mathcal P_{\mathrm{ch}}\ \text{is the coordinate's VALUE SPACE,}\ \neg\text{an arena — the complex domain opens a coordinate range, it declares no state space};\ \ \text{suspension coherence stands:}\ \neg\text{a formed read passes through an open branch}\ [\mathrm{IT.43}(6)]\ }$$
$$(5)\quad\textbf{THE REAFFIRMATIONS, WITH THEIR STANDING CORRECTIONS:}\qquad (\mathrm a)\ \ (\mathrm{D\text{-}PJ6}/\mathrm{D\text{-}RS5}):\ \ \text{the rider semantics stay DROPPED}\ [\mathrm{IT.44}(6)];\ \ \text{the reading is evaluated at the local designated register}\ o\ \ [\mathrm{Def\text{-}H.9}(2)];$$
$$\text{the directive's ``as permitted by A9 and Def-H.9'' keeps the correction issued at}\ \mathrm{IT.55}(7):\ \ \textbf{the enabling locus is}\ \mathrm{Def\text{-}H.9}\ +\ \mathrm{FT.20}\ \text{'s G-row, NOT A9}\ \text{(A9 is the universe-selection axiom; its text carries no observer/register content — the machine text census of}\ \mathrm{IT.55}(7)\ \text{stands, re-cited)}\ [\mathrm{IT.57}(3)(\mathrm P2)];$$
$$\text{the directive's ``the universe officially opens its eyes'' is recorded as FRAMING,}\ \neg\text{a row: the observer is the designated register,}\ \neg\text{consciousness}\ [\mathrm{IT.1}(7),(8)(\mathrm P4)];$$
$$(\mathrm b)\ \ (\mathrm{D\text{-}RS1}):\ \ \prec,\succ,\preceq,\succeq\ \text{denote the CAUSAL ordering of emission/reception events, replacing temporal pre/post language in the radar protocol; the grounding stands — the tick total order}\ [\mathrm{D1.8};\ \mathrm{D0.7};\ \mathrm{A7}]\ +\ \mathrm{C11}\ \text{'s within-node strict 4-order; the forward-only tick}\ [\mathrm{A6}]\ \text{is respected}\ (e\prec r\ \text{means emission causally precedes reception ON the tick order)};$$
$$\boxed{\ \textbf{THE SCOPE ROW STANDS:}\ \ \text{for two vertices AT THE SAME TICK,}\ \neg\text{a derived order exists — the declaration supplies LABELS,}\ \neg\text{ordering facts; ordering FACTS live only where the ledger derives them: the tick order}\ [\mathrm{D1.8}],\ \mathrm{C11}\ \text{'s lifecycle, and the round-trip theorem (exactly 1 of 24)}\ [\mathrm{IT.60}(1)]\ }$$
$$(\mathrm c)\ \ (\mathrm{D\text{-}RS2}):\ \ \text{the tick/worldline pairing stands as the DICTIONARY act — faces,}\ \neg\text{equals}\ [\mathrm{BM.134}(5)];\ \ \deg(\text{tick count})=\mathfrak q^0\ne\mathfrak q^{-1/2}=\deg(\text{chart length})\ [\mathrm{D2.9};\ \mathrm{BM.102}(2)];\ \ \neg\text{materialization coupling}\ [\mathrm{Def\text{-}H.19};\ \mathrm{FT.131}(3)];\ \ \text{the chart face is}\ \mathrm{BM.34}(2)\ \text{'s null algebra}\ [\mathrm{IT.53}(4)];$$
$$\text{the directive's ``at the npredim level'' is BUILDER-SIDE vocabulary (the pre-dimension graph instrument), flagged}\ \neg\text{adopted: the corpus locus of the discrete face is the tick face}\ [\mathrm{D0.7};\ \mathrm{C11};\ \mathrm{IT.53}(4)]\ \text{and of the continuous face the emergent chart projection}\ [\mathrm{IT.56}(2)];$$
$$(6)\quad(\mathrm{D\text{-}RS4})\ \textbf{STILL DEFERRED (the Architect's word stands):}\qquad \text{the stationarity instantiation scope}\ [\mathrm{BM.8}(2)\ \text{'s theorem-local hypothesis}]\ \text{remains OWED AND DEFERRED pending further data;}$$
$$\text{the premise correction is CONSISTENT with the directive's present wording: the agreement condition itself IS derived — reciprocity}\iff s\cdot dx=0\ \ [\mathrm{IT.53}(5)(\mathrm b);\ \mathrm{IT.57}(3)(\mathrm P7)];\ \ \text{what defers is the SCOPE act, and only that};$$
$$(7)\quad(\mathrm{D\text{-}PJ7})\ \textbf{THE DISPOSITION — NOT FORCED, REMAINS OWED:}\qquad \text{the directive's TITLE range ``D-PJ4–7'' overruns its BODY: no operative content is given for}\ \mathrm{D\text{-}PJ7};$$
$$\boxed{\ \mathrm{D\text{-}PJ7}\ \text{stays OWED as the standing IT-O1 package}\ [\mathrm{IT.54}(2);\ \mathrm{IT.41}(2)]:\ \ \text{deficit}\ 1'\ (\text{the chiral matter assignment: a Weyl symbol + a hypercharge-assignment read}),\ \ \text{the P4 transport profile (the declared gauge field)},\ \ \text{a transit winding carrier}\ \ —\ \ \mathrm{IT.66}\ \text{'s issuance of}\ \mathrm{D\text{-}RS6}\ \text{discharges the READ-LEVEL side of the named ``D-PJ7/D-RS6'' pair; the DYNAMICAL side consolidates under}\ \mathrm{D\text{-}PJ7}\ \text{alone}\ }$$
$$(8)\quad\textbf{THE SEVEN PREMISE CORRECTIONS (the rows win):}\qquad\begin{array}{l|l}\textbf{\#}&\textbf{the correction}\\\hline(\mathrm P1)&\text{the directive's constraint ``the transit bar remains standing on grounds O1 and O4''}\ \to\ \textbf{THREE grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{IT.40}\text{–}\mathrm{IT.42};\ \mathrm{IT.57}(3)(\mathrm P1)\ \text{re-affirmed}]\ \text{— the directive's own item 8 says three grounds; the internal inconsistency resolves to the record}\\\\(\mathrm P2)&\text{item 4's ``as permitted by A9 and Def-H.9''}\ \to\ \ \mathrm{Def\text{-}H.9}\ +\ \mathrm{FT.20}\ \text{'s G-row}\ [\mathrm{IT.57}(3)(\mathrm P2)\ \text{re-affirmed; machine text census at}\ \mathrm{IT.55}(7)]\\\\(\mathrm P3)&\text{``update the CONTINUUM.md project map''}\ \to\ \ \neg\text{a such file exists in the corpus topology (machine: zero matches corpus-wide and vault-wide)};\ \ \textbf{the live project map is}\ \texttt{era2/level6\_isotopic/README.md}\ (+\ \texttt{era2/README.md})\ \text{— both updated at this tier}\\\\(\mathrm P4)&\text{the five re-presented items are RECONCILIATIONS of issued acts,}\ \neg\text{duplicate issuances}\ (1),\ (2)\\\\(\mathrm P5)&\text{item 8's header ``IT-O1/IT-O3 package''}:\ \ \mathrm{IT\text{-}O3}\ \text{is CLOSED since}\ \mathrm{IT.60}(3)\ \text{—}\ \mathrm{D\text{-}RS6}\ \text{formalizes the read-level status}\ \mathrm{IT.60}\ \text{'s grammar already used; the IT-O1 side stands (three grounds)}\\\\(\mathrm P6)&\text{``npredim'' is builder-side vocabulary — flagged,}\ \neg\text{adopted}\ (5)(\mathrm c)\\\\(\mathrm P7)&\text{item 1's title ``for Transit Legs'' is scoped to the radar READ's legs (the geometric read's tick face)}\ \text{— the dynamical transit leg stays}\ \neg\text{formed}\ (\mathrm{IT.65}(1)\ \text{'s scope row})\end{array}$$
$$(9)\quad\textbf{status:}\qquad\textbf{reconciled:}\ (2)\text{--}(7);\qquad\textbf{derived elaboration:}\ (3),(4);\qquad\textbf{recorded:}\ (1),(8);\qquad\neg\text{a re-issuance},\qquad\neg\text{a forced declaration},\qquad\neg\text{a value}\ [\mathrm{P5}]$$

**Req.** P4, P5, A6, A7, C11, CT0.6, CT0.8, D0.7, D1.8, D2.3, D2.9 (Parts 1–2); Def-H.9, Def-H.19, Def-H.41, Def-H.42, FT.20, FT.131(3) (Part 3); IT.1(7),(8), IT.3(1), IT.31, IT.40–IT.42, IT.41(2), IT.43(6), IT.44(6), IT.53(3),(4),(5),(7), IT.54(2), IT.55, IT.56, IT.57, IT.60(1),(3), IT-O1 (this level); AT.42(3), AT.63(2) (Level 5); BM.8(2), BM.19, BM.34(2), BM.36(3), BM.61(8), BM.69(4), BM.102(2), BM.134(5), BM.137(1), FT.73(5) (Parts 2, 4); the exact $\mathbb Q[\gamma]$ discriminant identity, the $\mathbb Q(\sqrt2)$/$\mathbb Q(\sqrt3)$ sign and root censuses, the permutation census, the canon text census [math; machine: `remaining_declarations.py` §§B, C, E1, 8/8].

**Pf.**
$$(3):\ \text{the flicker weights and the collapse rows in exact Fractions}\ (D_n\big|_{u=0}=1;\ \text{the}\ 249\text{-point grid}\ \times\ n{=}2..6\ \text{strict census};\ \text{the hinge}\ D_n=\textstyle\sum_{i<n}u^i)\ [\text{machine B1, B2}];\ \ \text{the cardinal identity}\ 16=2^4=4{\times}4\ [\text{machine B3}];$$
$$(4):\ \text{the discriminant identity by symbolic expansion in}\ \mathbb Q[\gamma];\ \ \text{the witness/adversarial/boundary sign tests in exact}\ \mathbb Q(\sqrt2);\ \ \text{the grid sign censuses and the}\ \gamma{=}1\ \text{factorization (machine expansion; the three roots verified against the cubic in exact}\ \mathbb Q(\sqrt3));\ \ \text{the Vieta permutation census over all}\ 6\ \text{orderings};\ \ \text{the canon blocks of}\ \mathrm{Def\text{-}H.41}/\mathrm{Def\text{-}H.42}\ \text{scanned for the species clause verbatim}\ [\text{machine C1--C4}];$$
$$(2):\ \text{the state map assembled and its consistency checked}\ (\text{new}\cap\text{reaffirmed}=\varnothing;\ \text{the union covers the eight body items})\ [\text{machine E1}];\ \ (1),(5)\text{--}(9):\ \text{record rows on the cited clauses, the corrections re-affirmed from}\ \mathrm{IT.57}(3)\ \text{rather than re-argued}.\ \blacksquare$$

**Phys.** The directive arrived replaying the whole package, and the record had already absorbed six
of its eight items two sessions earlier — which is exactly the situation the reconciliation
discipline exists for. Nothing is issued twice: a declaration is a logged act, and a logged act
re-logged would corrupt the census it anchors. What the re-presentations do earn is a fresh audit —
the endpoint sentences riding with the crystallization signature turn out to be derived rows (the
dissolution weight vanishing at the sharp threshold, the normalizer collapsing to one, every
interior grid point genuinely an ensemble), and the complex-domain act gets its arena bars
re-certified from scratch rather than by citation, because the channel policy of the dyad is "run
it, don't accept it" and the corpus applies it to itself. The corrections previously issued are
re-affirmed, not renegotiated: A9 stays universe-selection, the observer stays a register, the
same-tick order stays underived. And the title that promised D-PJ7 is answered with silence where
silence is the honest word: no operative content, no act, the deficit-1′ package stays owed to the
Architect.

---

### IT.65 — D-RS3 ISSUED: the tick–hop exchange rate, per-edge integer only

**Thm.**
$$(1)\quad\textbf{THE ACT (the Architect's, recorded):}\qquad\begin{array}{l}\text{the radar read's tick face adopts the}\ \textbf{PER-EDGE INTEGER READING:}\ \ \text{each of the}\ \delta h\ \text{out-hops and}\ \delta h\ \text{return-hops carries one forward tick}\ [\mathrm{A6};\ \mathrm{C11}:\ \text{one update per node visit}],\end{array}$$
$$\boxed{\ \Delta\tau_{\mathrm{rt}}=2\delta h\ \ \text{is EVEN}\qquad\Longrightarrow\qquad d=\tfrac12\Delta\tau_{\mathrm{rt}}=\delta h\in\mathbb N\ \ —\ \ \textbf{agreeing with the DERIVED hop face}\ \ d=\delta h\ \ [\mathrm{D0.6};\ \mathrm{EM.7};\ \mathrm{IT.53}(4)]\ }$$
$$\textbf{SCOPE ROW:}\ \ \text{the exchange rate is declared for the radar READ's tick face}\ [\mathrm{IT.53}(4)]\ \text{— it supplies}\ \neg\text{an amplitude,}\ \neg\text{a weight,}\ \neg\text{a rate to any dynamical transit leg; the dynamical transit leg stays}\ \neg\text{formed and IT-O1 UNCHANGED (three grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{IT.40}\text{–}\mathrm{IT.42}])\ [\text{premise correction}\ \mathrm{IT.64}(8)(\mathrm P7)]$$
$$(2)\quad\textbf{THE BARRED READING (three machine grounds — the discrete ontology of the ledger):}\qquad \text{the PER-VISIT half-integer reading}\ \ \Delta\tau_{\mathrm{rt}}=2\delta h-1\Rightarrow d=\delta h-\tfrac12\ \ \text{is BARRED}:$$
$$(\mathrm i)\ \ \textbf{FACE CONSISTENCY:}\ \ d=\delta h-\tfrac12\ \text{contradicts the derived hop face}\ d=\delta h\ \text{at EVERY}\ \delta h\ (\text{census}\ 1..64;\ \text{adversarial:}\ 2\delta h{-}1\ \text{is odd for all}\ \delta h\le10^4)\ \text{— two faces of ONE definitional object}\ [\mathrm{IT.53}(4)]\ \text{must agree on}\ d;\ \text{only the per-edge reading does};$$
$$(\mathrm{ii})\ \ \textbf{RETURN-WORD PARITY:}\ \ \text{the formed two-body object counts RETURN words only — ALL ODD ENTRIES VANISH IDENTICALLY}\ [\mathrm{AT.44}(1);\ \mathrm{IT.3}(3);\ \mathrm{IT.53}(5)(\mathrm a)]:\ \ \textstyle\sum_j\mathrm C(k,j)(2j{-}k)^L=0\ \text{for every odd}\ L\ (k{=}1..8,\ L\in\{1,3,5,7,9\};\ \text{brute-forced over sign vectors};\ j\leftrightarrow k{-}j\ \text{antisymmetry)};$$
$$\text{the even sector SURVIVES (the census is}\ \neg\text{vacuous): the frozen anchors re-derive exactly —}\ \ N_2(2)=2,\ N_4(2)=4,\ N_2(4)=8,\ N_4(4)=40,\qquad N_4(2m)/N_2(2m)=4^{m-1}+1=(2,5,17,65)\ [\mathrm{IT.3}(3)];$$
$$\boxed{\ \text{an ODD round-trip count has NO formed ledger object: the per-edge (even) reading is the one the formed census supports — the declaration freezes the reading the ledger could already form}\ }$$
$$(\mathrm{iii})\ \ \textbf{LOCALITY AND INFORMATION-THEORETIC DISCRETENESS (the Architect's ground):}\ \ \text{a node knows only what it sent (integer}\ \delta h_{\mathrm{out}})\ \text{and what it received (integer}\ \delta h_{\mathrm{in}});\ \ \text{registered contents are integer}\ \ln2\text{-multiples}\ [\mathrm{IT.2}(4);\ \mathrm{D0.7}]:$$
$$\Delta\tau/2\in\mathbb Z\iff\Delta\tau\ \text{even}\ (\text{census}\ 0..256);\qquad\neg\exists\ \text{an integer combination}\ a\,\delta h_{\mathrm{out}}+b\,\delta h_{\mathrm{in}}+c\ (a,b,c\in[-8,8])\ \text{equal to}\ \delta h-\tfrac12\ \text{or outside}\ \mathbb Z\ (\text{closure census});$$
$$\text{the per-visit offset}\ {-}1\ \text{is the REMOTE node's fusion convention (data-in and data-out in one update}\ [\mathrm{C11}])\ \text{— data ABSENT from the emitter's local record: the}\ \tfrac12\ \textbf{violates locality and information-theoretic discreteness};$$
$$(3)\quad\textbf{THE DEGREE ROW AND P1:}\qquad \text{the exchange rate is a COUNT}\leftrightarrow\text{COUNT correspondence:}\ \ \deg(\Delta\tau_{\mathrm{rt}})=\deg(\delta h)=\deg(d)=\mathfrak q^0\ [\mathrm{D2.9};\ \mathrm{BM.102}(2)];$$
$$\boxed{\ \neg\text{a new dimensionful scale enters}\ [\mathrm{P1}]:\ \ \text{no dimensionful symbol occurs in this clause (machine-scanned); the only dimensional bridge}\ [\mathrm{BM.102}(4)]\ \text{stays untouched and unissued}\ }$$
$$(4)\quad\textbf{THE COHERENCE WITH THE DECLARED VOCABULARY:}\qquad \text{the per-edge reading feeds}\ \mathrm{D\text{-}RS1}\ \text{'s order grammar (every hop is one forward tick}\ [\mathrm{A6};\ \mathrm{D1.8}])\ \ \text{and}\ \ \mathrm{D\text{-}RS2}\ \text{'s face pairing (the tick face is the ledger read; the chart face is unchanged}\ [\mathrm{IT.56}(2)];$$
$$\text{the round-trip order theorem}\ [\mathrm{IT.60}(1)]\ \text{counts EVENTS,}\ \neg\text{hops — unaffected};\qquad\text{the even parity ALIGNS the tick face with the return-word structure}\ [\mathrm{AT.44}(1)]:\ \ \text{the agreement}\ d_{e\to p}=d_{p\to e}\ \text{stays a CONSEQUENCE of the return-word read,}\ \neg\text{a condition}\ [\mathrm{IT.53}(5)(\mathrm a)]$$
$$(5)\quad\textbf{status:}\qquad\textbf{ISSUED}\ (\text{the Architect's act, recorded verbatim-in-substance});\qquad\textbf{the grounds}\ (\mathrm i)\text{--}(\mathrm{iii})\ \textbf{are DERIVED supports}\ (\text{the declaration freezes the reading the rows already favored — over-determined,}\ \neg\text{arbitrary});$$
$$\neg\text{a value}\ [\mathrm{P5}],\qquad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\qquad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)],\qquad\neg\text{a transit vertex}\ [\mathrm{BM.122}(6)]$$

**Req.** A6, C11, D0.6, D0.7, D1.8, D2.9, P1, P5 (Parts 1–2); EM.7 (Part 2); IT.2(4), IT.3(3), IT.40–IT.42, IT.53(4),(5),(7), IT.56(2), IT.60(1), IT.64(8), IT-O1 (this level); AT.44(1) (Level 5); BM.102(2),(4), BM.122(6), Def-BM.3(7) (Part 4); exact integer binomials and parity censuses, Fraction integrality and closure censuses [math; machine: `remaining_declarations.py` §A, 5/5].

**Pf.**
$$(1),(2):\ \ \text{the per-edge census}\ 1..64\ \text{(evenness, integrality, hop-face agreement); the per-visit census (denominator exactly}\ 2\ \text{at every}\ \delta h;\ \text{the}\ 10^4\ \text{adversarial); the closed-form odd moments}\ (k{=}1..8)\ \text{and the sign-vector brute force}\ (k{=}1..4),\ \text{with the frozen even-sector anchors and the ratio closed form}\ 4^{m-1}{+}1\ \text{re-derived};\ \text{the integrality-iff-evenness and closure censuses}\ [\text{machine A1--A4}];$$
$$(3):\ \ \text{the degree row on}\ \mathrm{D2.9}\ \text{'s register and the clause scan}\ [\text{machine A5; the tier scan F1}];\qquad(4),(5):\ \ \text{record rows on the cited clauses}.\ \blacksquare$$

**Phys.** The audit had left the radar's tick face with two exact readings and no frozen choice, and
the declaration takes the integer side — and the ledger shows the choice was less a fork than a
formality. The hop face was already derived, and only the per-edge count agrees with it; the formed
two-body object counts return words, and every odd count in that census is identically zero, so the
per-visit round trip never had a formed object to live in; and the half-tick itself could only be
known by standing at the far node, watching absorption and re-emission fuse into a single update —
information the emitter's own integer record does not carry. Three independent grounds, all derived,
all pointing the same way: the universe does not bill in halves. What the declaration adds is the
freeze, and what it refuses is the smuggling: the rate belongs to the read's tick face, the
dynamical transit leg stays unformed, and the photon still carries no amplitude between the nodes.

---

### IT.66 — D-RS6 ISSUED: radar as geometric read; the bar-check verdict and the register state

**Thm.**
$$(1)\quad\textbf{THE ACT (the Architect's, recorded):}\qquad\begin{array}{l}\text{the radar protocol is formally declared a}\ \textbf{GEOMETRIC / READ-LEVEL interpretation of the lepton–baryon connection}\ \text{(the handshake at the meeting locus), admissible as a FORMED GEOMETRIC READ}\ [\mathrm{IT.3}(6);\ \mathrm{Def\text{-}H.19}].\end{array}$$
$$\boxed{\ \text{the issuance DISCHARGES}\ \mathrm{IT.53}(8)\ \text{'s ``admissible iff DECLARED a read'' clause: the radar candidate of}\ \mathrm{IT.53}(7)\ \text{is now a DECLARED geometric read —}\ \neg\text{a formed dynamical amplitude; the dynamical transit (emission/absorption with a winding carrier) remains BARRED on the three standing grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{BM.122}(6)\ \text{as re-audited at}\ \mathrm{IT.40}\text{–}\mathrm{IT.42};\ \mathrm{O3}\ \text{discharged}\ [\mathrm{BM.134}(7)]]\ }$$
$$(2)\quad\textbf{THE EXHAUSTIVENESS OF THE FORMED CONTENT (machine):}\qquad \text{the reads the declaration admits are EXACTLY the pre-existing ones}:$$
$$(\mathrm a)\ \ \text{the return-word COUNTS}\ N_k(2m)\ [\mathrm{AT.44}(1);\ \mathrm{IT.65}(2)(\mathrm{ii})]\ \text{— pure counts, empty symbol alphabet};\quad(\mathrm b)\ \ \text{the protocol FACES}\ [\mathrm{IT.53}(4)]\ \text{— hop/tick/chart/anchor, the tick face now frozen}\ (\mathrm{IT.65});$$
$$(\mathrm c)\ \ \text{the ORDER grammar}\ [\mathrm{IT.60}(1),(2)]\ \text{— the round-trip theorem RE-RUN exhaustively: exactly ONE of}\ 4!=24\ \text{orderings survives the grounded constraints}\ (e_1\prec r_1,\ e_2\prec r_2\ [\mathrm{D\text{-}RS1}\ \text{on the total tick order}];\ \ r_1\prec e_2\ [\mathrm{C11}\ \text{'s within-node lifecycle}]):\ \ e_1\prec r_1\prec e_2\prec r_2;\quad(\mathrm d)\ \ \text{the}\ \chi\text{-gated meeting locus}\ [\mathrm{IT.58};\ \mathrm{IT.53}(7)];$$
$$\textbf{the alphabet census:}\ \ \{\delta h,\ \Delta\tau_{\mathrm{rt}},\ d,\ \prec,\ \succ\}\ \cap\ \{v_\Gamma,\ Z^{\mathrm{amp}},\ \text{S-matrix},\ \text{rate}\}=\varnothing\quad\wedge\quad\{\delta h,\ \Delta\tau_{\mathrm{rt}},\ d,\ \prec,\ \succ\}\ \cap\ \{E_{\mathrm{int}},\ \hat\mu'^2,\ \rho_{\mathrm B},\ D_S\}=\varnothing;$$
$$\boxed{\ \neg\text{a vertex},\ \ \neg\text{an amplitude},\ \ \neg\text{a weight},\ \ \neg\text{a rate attaches to the radar read —}\ \mathrm{IT.60}(2)\ \text{'s status census extends to the declaration itself}\ }$$
$$(3)\quad\textbf{THE BAR-CHECK VERDICT (machine, 23/23):}\qquad\begin{array}{l|l}\textbf{the bar}&\textbf{the verdict}\\\hline\mathrm{P1}\ \text{(no new dimensionful scale)}&\textbf{HONORED}: \text{the acts touch counts, labels and order only}\ (\mathfrak q^0);\ \ \mathrm{IT.65}\ \text{'s clause carries no dimensionful symbol (machine scan)}\\\\\mathrm{P5}\ \text{(no measured value)}&\textbf{HONORED}: \text{ZERO decimal numeric tokens in this tier (machine scan); no value issued; the nine-slot registry}\ [\mathrm{IT.57}(6)]\ \text{passes through unchanged}\\\text{the transit bar}&\textbf{STANDS on THREE grounds}\ \mathrm{O1/O2/O4}:\ \ \mathrm{O1}\ \text{RE-RUN by machine}\ ([W_i\otimes I_\omega,\ I\otimes P_{L/R}]{=}0\ \text{in}\ 4{\times}4\ \mathbb Q(i),\ \text{both projectors; the same-factor adversarial}\ [\sigma_1,\sigma_3]{=}{-}2\mathrm i\sigma_2\ne0);\ \ \mathrm{O2}\ \text{deficit}\ 1'\ [\mathrm{IT.41}(2);\ \mathrm{FT.125}(4)];\ \ \mathrm{O4}\ \text{the D3.7 trivial chain}\ [\mathrm{IT.40}(4)];\ \ \mathrm{O3}\ \text{discharged}\ [\mathrm{BM.134}(7)];\ \ \neg\text{a vertex constructed}\ (2)\\\text{the arena bars}\ [\mathrm{Def\text{-}H.41}/\mathrm{Def\text{-}H.42}]&\textbf{HOLD}: \text{re-certified self-contained at}\ \mathrm{IT.64}(4)\ \text{—}\ \mathcal P_{\mathrm{ch}}\ \text{is the coordinate's value space; the arenas stay counting spaces; the open branch is inert}\\\text{the incommensurability bar}&\textbf{HOLDS}: \text{the formed MIXED loci stay EXACTLY THREE}\ (\mathcal B_{\mathrm{ens}},\ \mathcal W_{\text{channel}},\ \chi)\ [\mathrm{IT.4}(2);\ \mathrm{IT.58}(5);\ \mathrm{IT.59}(2)];\ \ \text{the radar's mixed content passes ONLY through the pre-existing}\ \chi\ \text{locus};\ \ \neg\text{a fourth locus},\ \ \neg\text{a cross-currency sum or conversion}\ [\mathrm{BM.83};\ \mathrm{BM.140}(5)]\\\text{count}\to\text{strength}&\textbf{BARRED as ever}: \mathrm{D\text{-}PJ4}\ \text{'s functional form stays UNFIXED};\ \ \neg\text{a threshold value}\ [\mathrm{IT.64}(3)]\\\text{species identification}&\textbf{NONE}: \text{names quoted}\ [\mathrm{Def\text{-}BM.3}(1,(7))]\\\text{the frozen canon}&\textbf{UNTOUCHED}\ [\mathrm{AT.63}(2)]:\ \ \text{cited, never edited; IT.57(2)'s register row superseded by explicit row}\ (4),\ \neg\text{in place}\end{array}$$
$$\boxed{\ \textbf{VERDICT: THE REMAINING PACKAGE IS ISSUABLE AS RECORDED — two new acts issued, five reaffirmed, one still deferred, one not forced; the corrections ride with them}\ }$$
$$(4)\quad\textbf{THE REGISTER STATE AFTER THE ISSUANCE (this row supersedes}\ \mathrm{IT.57}(2)\textbf{):}\qquad\begin{array}{l|l}\textbf{state}&\textbf{the items}\\\hline\textbf{ISSUED (cumulative)}&\mathrm{D\text{-}PJ1},\ \mathrm{D\text{-}PJ2},\ \mathrm{D\text{-}PJ3}\ (\text{resolved by}\ \mathrm{D\text{-}PJ1}),\ \mathrm{D\text{-}PJ4},\ \mathrm{D\text{-}PJ5},\ \mathrm{D\text{-}PJ6}/\mathrm{D\text{-}RS5}\ (\text{merged}),\ \mathrm{D\text{-}RS1},\ \mathrm{D\text{-}RS2},\ \ \ \mathrm{D\text{-}RS3}\ @\ \mathrm{IT.65}\ (\textbf{this tier}),\ \ \mathrm{D\text{-}RS6}\ @\ \mathrm{IT.66}\ (\textbf{this tier}),\ \ \mathrm{D\text{-}RS7},\ \ \text{the}\ \mathrm{BM.113}(6)\ \text{sector sync},\ \ \text{item 12's re-confirmation}\\\textbf{DEFERRED}&\mathrm{D\text{-}RS4}\ (\text{the stationarity instantiation scope — pending data})\\\textbf{REMAINING OWED}&\mathrm{D\text{-}PJ7}\ \textbf{ALONE}\ (\text{the standing IT-O1 package: deficit}\ 1',\ \text{the P4 transport profile, a transit winding carrier}\ [\mathrm{IT.41}(2)])\\\textbf{SUB-DEBTS (unchanged)}&\mathcal P_{\mathrm{ch}}\ \text{'s branch rule (open BY DESIGN until a formed read needs it)};\ \ \mathrm{D\text{-}PJ4}\ \text{'s degree functional form (and any threshold value — a further act)};\ \ \mathrm{D\text{-}PJ1}\ \text{'s endpoint-register elaboration}\\\textbf{inherited forks (unchanged)}&\text{the}\ b\text{-slot choice}\ [\mathrm{IT.49}(4)];\ \text{the order-3 filling}\ [\mathrm{IT.52}];\ \text{the mass-read route choice}\ [\mathrm{IT.14}(3);\ \mathrm{BM.30}(5)];\ \text{the lift/vielbein/transport profile}\ [\mathrm{AT.63}(3)]\end{array}$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the calibration values this tier adds: none.}\quad\S\mathrm{Cal\text{-}IT}\ \text{stays VALUE-FREE — the act register gains exactly two logged acts with citation handles}\ \ \mathrm{D\text{-}RS3}\ @\ \mathrm{IT.65},\ \ \mathrm{D\text{-}RS6}\ @\ \mathrm{IT.66}\ \ [\mathrm{IT.57}(4)\ \text{'s placement answer stands: a Def-IT series at closure remains an OPTION,}\ \neg\text{forced}];$$
$$\text{the unissued symbols stand:}\ \rho_{\mathrm B}\ [\mathrm{A\text{-}BM.9}],\ e_0\ [\mathrm{EM.25}(7)],\ \hat\mu'^2,\ \sigma_\ell,\ \sigma_\nu,\ \varepsilon_q\ (\mathrm{AT\text{-}O27}),\ (\varkappa,\beta)\ (\mathrm{AT\text{-}O3}),\ \ \text{the P1 scale slot},\ \text{the}\ \mu_{\mathrm{ch}}\ \text{family (Cal-F)}$$
$$(6)\quad\textbf{the open rows after the package:}\qquad\boxed{\ \textbf{NO new open row}\ };\qquad \mathrm{IT\text{-}O1}\ \text{UNCHANGED (three grounds; deficit}\ 1');\qquad \mathrm{IT\text{-}O2}\ (\text{the binding value; the three constructions}\ [\mathrm{IT.27}(2)]),\ \ \mathrm{IT\text{-}O5}\ (\text{the dynamical side at IT-O1}),\ \ \mathrm{IT\text{-}O6}\ (\text{the}\ \delta\text{-glue species}\ [\mathrm{IT.62}])\ \text{unchanged};$$
$$\mathrm{IT\text{-}O3}\ \text{stays CLOSED}\ [\mathrm{IT.60}(3)]\ \text{— the radar is now its DECLARED read-level grammar};\qquad \mathrm{AT\text{-}O30}/\mathrm{AT\text{-}O32}\ \text{(the heavy censuses) remain};\qquad \text{the deferred Calibration Era unchanged}\ [\mathrm{AT.63}(4)]$$
$$(7)\quad\textbf{the machine state:}\qquad\texttt{remaining\_declarations.py}\to\textbf{23/23 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{21 checkers, 335 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{20 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad \text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(8)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and a declaration is}\ \neg\textbf{a derivation}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5, C11, D3.7 (Parts 1–2); Def-H.19, Def-H.41, Def-H.42, FT.123 (Phys), FT.125(4), FT.131(3) (Part 3); IT.3(6), IT.4(2), IT.14(3), IT.27(2), IT.40–IT.42, IT.41(2), IT.49(4), IT.52, IT.53(4),(7),(8), IT.54(2), IT.55, IT.56, IT.57, IT.58, IT.58(5), IT.59(2), IT.60(1),(2),(3), IT.62, IT.64, IT.65, IT-O1, IT-O2, IT-O3, IT-O5, IT-O6 (this level); AT.39(8), AT.44(1), AT.63(2),(3),(4) (Level 5); A-BM.9, BM.6(6), BM.30(5), BM.83, BM.102(2),(4), BM.113(6), BM.122(6), BM.134(5),(7), BM.140(5), Def-BM.3(1),(7), EM.25(7), FT.73(5), FT.79(5) (Parts 2, 4); the exact $\mathbb Q(i)$ commutator re-run, the exhaustive 24-ordering enumeration, the alphabet and registry censuses, the tier scan, the full runner and gate re-run end to end [math; machine: `remaining_declarations.py` §§D, E2, F, 10/10].

**Pf.**
$$(1),(2):\ \ \text{the chiral-blindness commutator re-run in}\ 4{\times}4\ \text{Gauss(i) with the same-factor adversarial}\ [\text{machine D1}];\ \ \text{the round-trip enumeration over all}\ 24\ \text{orderings and the alphabet intersections}\ [\text{machine D2}];\ \ \text{the three-grounds assembly with}\ \mathrm{O3}\ \text{'s discharge}\ [\text{machine D3}];\ \ \text{the mixed-loci census}\ [\text{machine D4}];$$
$$(3):\ \ \text{the bar-check assembly over the twenty-three markers, with the tier scans (zero decimals; the}\ \mathrm{IT.65}\ \text{clause dimensionful-free)}\ [\text{machine F1--F5}];\qquad(4),(5):\ \ \text{the register and census tables assembled from}\ \mathrm{IT.64}\text{–}\mathrm{IT.65}\ \text{'s clauses and the state-map consistency}\ [\text{machine E2}];$$
$$(6)\text{--}(8):\ \ \text{record rows; the runner and the gate re-run end to end. No new mathematics is introduced at this tag beyond the re-runs cited}.\ \blacksquare$$

**Phys.** The radar has asked the corpus for the one thing the corpus grants willingly and rarely:
a name. It arrives as a read, not a mechanism — the geometric interpretation of the lepton–baryon
connection is now declared, exactly as IT.53(8) said it would have to be before the protocol could
count as formed geometry, and exactly as IT.60's grammar had already been using it when the
handshake row closed. What the declaration does not do is the thing the bars exist to watch: the
photon still carries no amplitude between the nodes, the gauge blocks still commute blindly past
the chiral projectors — re-run here from scratch, not trusted from citation — and the dynamical
transit stays barred on all three of its grounds, the directive's own constraint line corrected
when it miscounted them. The register closes to a single owed item, the deficit-1′ package, and the
census keeps the distinction that makes declarations safe: two more acts logged, zero values
issued, and a universe that now reads itself geometrically without, for one moment, being permitted
to radiate.

---

## §Cal-IT — two more logged acts (value-free)

**The act register grows by exactly TWO; it stays VALUE-FREE.** Tier IT.20 logs the Architect's
issuance of **D-RS3** (the tick–hop exchange rate: per-edge integer only, $\Delta\tau_{\mathrm{rt}}=2\delta h\Rightarrow d=\delta h\in\mathbb N$; the per-visit half reading barred on three derived
grounds — face consistency, return-word parity, local-record integrality) at **IT.65**, and of
**D-RS6** (the radar protocol declared a geometric/read-level interpretation of the lepton–baryon
connection; the dynamical transit barred on the three standing grounds O1/O2/O4) at **IT.66**. The
five re-presented items (D-PJ4 + the derived endpoint elaboration, D-PJ5 + the self-contained arena
re-certification, D-PJ6/D-RS5, D-RS1, D-RS2) are REAFFIRMED against IT.55–IT.56 with their
corrections standing; **D-RS4 stays DEFERRED**; **D-PJ7 is NOT forced and remains owed** (the
standing IT-O1 package: deficit 1′, the P4 transport profile, a transit winding carrier [IT.41(2)]);
the three sub-debts are unchanged. **No calibration parameter is added, valued, or re-scoped**: the
P1 scale slot, $\varepsilon_q$ (AT-O27), $e_0$ [EM.25(7)], $(\varkappa,\beta)$ (AT-O3),
$\rho_{\mathrm B}$ [A-BM.9], $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$, the $\mu_{\mathrm{ch}}$
family (Cal-F), the read rules (M1′)–(M3′) [AT.54(6)], and the mass-read route choice [IT.14(3);
BM.30(5)] all stand unchanged. The Calibration Era stays **deferred** [AT.63(4)].

## §Open-IT additions from Tier IT.20

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.20 opens **no new open row**. The declaration register now carries ONE remaining owed act: **D-PJ7** (the standing IT-O1 package [IT.41(2)]) + the three sub-debts (unchanged). **IT-O1 unchanged** (three grounds; the package constructs no vertex — IT.66(2) machine); **IT-O3 stays CLOSED** [IT.60(3)] with the radar as its declared read-level grammar; IT-O2/IT-O5/IT-O6 unchanged | IT.66(2),(4),(6); IT.64(2),(7); IT.65(1) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4); IT.57(5); IT.60(4); IT.62(4)]:
(IT-O1) the formed transit-leg amplitude — three grounds, deficit 1′ [IT.41]; (IT-O2) the binding
value — the three IT.27(2) constructions; (IT-O5) the isotope cutoff — the dynamical side at IT-O1;
(IT-O6) the δ-glue connector species [IT.62]; AT-O30/AT-O32 the heavy censuses; the owed route
choice [IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the Level-5 inheritance
[AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.21: the opened paths — the unblocking census, the declared radar read operationalized, and IT-O6 CLOSED (the δ-glue is the same frozen connector)

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.21 — the Architect's directive after the
declaration package: *"The declarations opened a lot of obstructed paths. Please work on them and
close those possible."* The tier works the paths the Tier IT.17/IT.20 acts opened: (i) the
UNBLOCKING CENSUS — every gate phrase of the era-2 record machine-located and mapped to its
post-package status (resolved / superseded / still blocked, with grounds); (ii) the DECLARED RADAR
READ operationalized — the first formed $o$-lifted read family under D-RS6 + D-RS3 + D-PJ6/D-RS5 +
D-RS1/D-RS2; (iii) **IT-O6 CLOSED** — the δ-involving connector glue derived: it is the SAME frozen
open bidirectional connector (the derivation steps of IT.19 are seal-blind; the "meson" of
BM.129(1) is the frozen δ-side witness). Nothing is forced: the paths that stay blocked stay
blocked WITH their grounds (D-RS4 deferred; D-PJ7 owed; the value declarations; the Calibration
Era). **Tags.** IT.67–IT.70. **Pattern.** the construction tiers (IT.6/IT.18's shape), premise
audit logged in-tier.
**Status.** discovery-phase working tier. No declaration issues at this tier (machine-scanned);
§Cal-IT stays value-free and unchanged; no clause of Parts 1–4, of Level 5's closed record, or of
Tiers IT.1–IT.20 is modified [AT.63(2)] — IT.62(2)'s UNDERIVED glue rows are SUPERSEDED BY
EXPLICIT ROW at IT.69, never edited. No measured value enters [P5]; no new dimensionful scale
[P1]; species names stay quoted [Def-BM.3(1),(7)].
**Machine.** `era2/level6_isotopic/checks/opened_paths.py` → **15/15 exact** (integers, Fractions,
exact Laurent convolutions, exact ceilings, multivariate Fraction polynomials with honest
substitution; text censuses; NO floating point); `run_all_level6.py` → **22 checkers, 350 exact
markers, 0 failures**; `check_level6_format.py` → the gate over all twenty-one Part 6 documents.
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive (session 13q), executed in full: the census of opened paths
(IT.67), the radar read worked (IT.68), the closable row closed (IT.69: IT-O6), and the honest
boundary — the rows that need an Architect act or a genuine multi-construction build are recorded,
not forced (IT.70).

---

### IT.67 — The unblocking census: the gate phrases of the record, mapped to their post-package status

**Thm.**
$$(1)\quad\textbf{THE METHOD:}\qquad \text{a machine text census over the Part 6 record locates every GATE PHRASE — the record's own markers of an obstructed path (``owed'', ``NEITHER FROZEN'', ``iff DECLARED'', ``only under'', ``UNDERIVED'', ``DEFERRED'') — and maps each to the declaration that gates it and its status after Tiers IT.17 + IT.20:}$$
$$\boxed{\ \text{three classes:}\ \ \textbf{RESOLVED}\ (\text{the gating declaration is issued}),\quad \textbf{SUPERSEDED}\ (\text{the blocked construction is delivered by a later tier}),\quad \textbf{STILL BLOCKED}\ (\text{the gate stands, with its ground})\ }$$
$$(2)\quad\textbf{THE CENSUS (machine: every phrase located in the record — the census is}\ \neg\textbf{vacuous):}\qquad\begin{array}{l|l|l}\textbf{the gate phrase (its locus)}&\textbf{the gate}&\textbf{the post-package status}\\\hline\text{``BOTH EXACT, NEITHER FROZEN''}\ [\mathrm{IT.53}(4)]&\mathrm{D\text{-}RS3}&\textbf{RESOLVED by}\ \mathrm{IT.65}\ \text{(the tick face frozen per-edge)}\\\text{``return-word identification itself is}\ \mathrm{D\text{-}RS2},\ \text{owed''}\ [\mathrm{IT.53}(5)(\mathrm a)]&\mathrm{D\text{-}RS2}&\textbf{RESOLVED by}\ \mathrm{IT.56}(2)\ \text{(the dictionary pairing)}\\\text{``admissible iff DECLARED a read''}\ [\mathrm{IT.53}(8)]&\mathrm{D\text{-}RS6}&\textbf{RESOLVED by}\ \mathrm{IT.66}\ \text{(the read declared)}\\\text{``admissible as a READ only under}\ \mathrm{D\text{-}RS2}\text{''}\ [\mathrm{IT.54}\ \S\mathrm{Open}]&\mathrm{D\text{-}RS2}&\textbf{RESOLVED by}\ \mathrm{IT.56}(2)\\\text{``}\mathrm{D\text{-}RS4}\ \text{owed to instantiate''}\ [\mathrm{IT.53}(5)(\mathrm b)]&\mathrm{D\text{-}RS4}&\textbf{STILL BLOCKED}\ \text{(deferred at}\ \mathrm{IT.56}(3)/\mathrm{IT.64}(6)\ \text{— the Architect's word)}\\\text{``UNDERIVED''}\ \times2\ [\mathrm{IT.62}(2)\ \text{'s glue census}]&\mathrm{IT\text{-}O6}&\textbf{SUPERSEDED at}\ \mathrm{IT.69}\ \text{(this tier: the glue derived)}\\\text{``REMAINS OWED''}\ [\mathrm{IT.56}(5)]&\mathrm{D\text{-}RS3}\ \text{(then)}&\textbf{RESOLVED by}\ \mathrm{IT.65}\\\text{``REMAINING OWED''}\ [\mathrm{IT.66}(4)]&\mathrm{D\text{-}PJ7}&\textbf{STILL BLOCKED}\ \text{(owed — no act content; deficit}\ 1'\ [\mathrm{IT.41}(2)])\\\text{``STILL DEFERRED''}\ [\mathrm{IT.64}(2),(6)]&\mathrm{D\text{-}RS4}&\textbf{STILL DEFERRED}\end{array}$$
$$(3)\quad\textbf{THE OPENED PATHS (the directive's ``obstructed paths'', inventoried):}\qquad \text{with}\ \mathrm{D\text{-}RS1/2/3/6}\ +\ \mathrm{D\text{-}PJ4/5/6}\ \text{issued, the following are NOW CONSTRUCTIBLE without a further act}:$$
$$(\mathrm a)\ \ \text{the RADAR READ as a formed}\ o\text{-lifted geometric read family}\ [\mathrm{IT.53}(8)\ \text{'s iff-clause discharged at}\ \mathrm{IT.66};\ \mathrm{Def\text{-}H.9}(2)\ \text{'s register}\ o]\ \ \text{— worked at}\ \mathrm{IT.68};$$
$$(\mathrm b)\ \ \text{the tick-face computations with the FROZEN exchange rate}\ \Delta\tau_{\mathrm{rt}}=2\delta h\ [\mathrm{IT.65}]\ \ \text{— worked at}\ \mathrm{IT.68}(1);$$
$$(\mathrm c)\ \ \text{the}\ \delta\text{-involving connector glue}\ [\mathrm{IT.62}(4)\ \text{'s templates:}\ \mathrm{BM.110}(1)\ \text{'s}\ \delta\text{-sealed digon + IT.19's}\ \Sigma_{12}\ \text{method}]\ \ \text{— worked and CLOSED at}\ \mathrm{IT.69};$$
$$(\mathrm d)\ \ \text{the event classification at the INGREDIENT level}\ [\mathrm{D\text{-}PJ4}\ @\ \mathrm{IT.55}(5)\ +\ \mathrm{IT.64}(3)\ \text{'s endpoint rows}]\ \ \text{— worked at}\ \mathrm{IT.68}(4)\ \text{(the functional form stays UNFIXED — the sub-debt stands)};$$
$$(\mathrm e)\ \ \text{the order grammar}\ [\mathrm{D\text{-}RS1}]\ \text{was already consumed by IT-O3's closure}\ [\mathrm{IT.60}(1),(3)];\qquad(\mathrm f)\ \ \text{the}\ \vee^2\text{-sector sign reads via the synced}\ \mathbb Z_2\ \text{dictionary}\ [\mathrm{IT.56}(6)]\ \text{— a convention in force, no construction pending on it at this level};$$
$$(4)\quad\textbf{THE PATHS THAT STAY BLOCKED (with their grounds — recorded,}\ \neg\textbf{forced):}\qquad\begin{array}{l|l}\textbf{the path}&\textbf{the ground}\\\hline\text{the off-saturation stationarity scope (the chart-side agreement read)}&\mathrm{D\text{-}RS4}\ \text{DEFERRED — a scope act, pending data}\ [\mathrm{IT.56}(3);\ \mathrm{BM.8}(2)]\\\text{the dynamical transit / photon-mediated jump}&\mathrm{D\text{-}PJ7}\ \text{owed: deficit}\ 1'\ \text{(application-layer}\ [\mathrm{FT.125}(4)]),\ \text{the P4 transport profile},\ \text{a winding carrier}\ [\mathrm{IT.41}(2);\ \mathrm{IT.40}\text{–}\mathrm{IT.42}]\\\hat O\ \text{'s second iterate / reads through}\ \mathcal P_{\mathrm{ch}}\ \text{'s open branches}&\text{the branch rule is open BY DESIGN;}\ \neg\text{a formed read may pass an open branch}\ [\mathrm{IT.55}(6);\ \mathrm{IT.43}(6)]\\\text{the crystallization degree's functional form (any threshold value)}&\text{the}\ \mathrm{D\text{-}PJ4}\ \text{sub-debt}\ [\mathrm{IT.55}(5);\ \mathrm{IT.64}(3)];\ \ \text{count}\to\text{strength barred}\ [\mathrm{BM.36}(3);\ \mathrm{FT.73}(5)]\\\text{every VALUE conversion (masses, couplings, scales)}&\text{the value declarations: the lift/vielbein}\ [\mathrm{AT.63}(3)],\ (\mathrm{M1'})\text{–}(\mathrm{M3'})\ [\mathrm{AT.54}(6)],\ \varepsilon_q\ [\mathrm{AT\text{-}O27}],\ (\varkappa,\beta)\ [\mathrm{AT\text{-}O3}],\ e_0\ [\mathrm{EM.25}(7)],\ \rho_{\mathrm B}\ [\mathrm{A\text{-}BM.9}],\ \text{the route choice}\ [\mathrm{IT.14}(3);\ \mathrm{BM.30}(5)]\\\text{the Calibration Era itself}&\text{an Era-2-closure act}\ [\mathrm{AT.63}(4);\ \mathrm{IT.33}(2)]\end{array}$$
$$(5)\quad\textbf{status:}\qquad\textbf{derived (machine):}\ (2)\ \text{'s census — every phrase located, every status traced to its certifying tier};\qquad\textbf{recorded:}\ (3),(4);\qquad\neg\text{a declaration issued at this tier},\qquad\neg\text{a forced closure}$$

**Req.** P5, C11, D1.8 (Parts 1–2); Def-H.9(2), Def-H.19 (Part 3); IT.14(3), IT.40–IT.42, IT.41(2), IT.43(6), IT.46, IT.53(4),(5),(6),(8), IT.54, IT.55(5),(6), IT.56(2),(3),(5),(6), IT.60(1),(3), IT.62(2),(4), IT.64(2),(3),(6), IT.65, IT.66(4), IT-O3, IT-O6 (this level); AT.54(6), AT.63(2),(3),(4) (Level 5); A-BM.9, BM.8(2), BM.30(5), BM.36(3), BM.110(1), BM.122(6), FT.73(5), FT.125(4), EM.25(7) (Parts 2, 4); the normalized text census over the twenty Part 6 documents [math; machine: `opened_paths.py` §A, 2/2].

**Pf.**
$$(2):\ \ \text{the phrase census on the normalized record text}\ (\text{LaTeX}\ \text{-forms folded});\ \text{every phrase found at its locus; the resolved class covers}\ \mathrm{D\text{-}RS2},\ \mathrm{D\text{-}RS3},\ \mathrm{D\text{-}RS6};\ \text{the superseded class finds IT.62(2)'s two UNDERIVED cells; the blocked class covers}\ \mathrm{D\text{-}RS4},\ \mathrm{D\text{-}PJ7}\ [\text{machine A1}];\qquad(5)\ \text{'s no-declaration row: the tier scan finds}\ \neg\text{a new act handle}\ [\text{machine A2}];$$
$$(1),(3),(4):\ \ \text{assembly rows on the cited clauses}.\ \blacksquare$$

**Phys.** A declaration package is worth exactly the paths it opens, and the record had marked its
own gates in writing — "owed", "neither frozen", "iff declared" — so the census is not an
interpretation but a scan. Nine phrases, three classes: four gates opened by the package, two cells
the coming tier supersedes, and the honest remainder that no construction can touch — a deferred
scope, an application-layer deficit, and the value declarations that keep the Calibration Era a
closure act. The inventory says what the generator may now build without asking, and the blocked
table says what it may not build at all. Between the two lies the whole legitimate territory of
this tier, and both of its constructions — the radar read and the δ-glue — live inside it.

---

### IT.68 — The declared radar read: the first formed $o$-lifted read family

**Thm.**
$$(1)\quad\textbf{THE ROUND-TRIP READ AT THE REGISTER}\ o\ \textbf{(formed):}\qquad \text{the emitter's own ledger pair, evaluated at its local designated register}\ o\ [\mathrm{Def\text{-}H.9}(2);\ \mathrm{D\text{-}PJ6}/\mathrm{D\text{-}RS5}\ @\ \mathrm{IT.55}(7)]:$$
$$\boxed{\ (\tau_e,\ \tau_r=\tau_e+\Delta\tau_{\mathrm{rt}}),\qquad \Delta\tau_{\mathrm{rt}}=2\delta h\ \ [\mathrm{D\text{-}RS3}\ @\ \mathrm{IT.65}],\qquad d=\tfrac12(\tau_r-\tau_e)=\delta h\in\mathbb N,\qquad e\prec r\ \ \text{on the total tick order}\ [\mathrm{D\text{-}RS1};\ \mathrm{D1.8};\ \mathrm{D0.7};\ \mathrm{A6}]\ }$$
$$\text{machine census: every}\ (\delta h,\tau_e)\in1..32\times0..4\ \text{gives integer}\ \tau_r,\ d=\delta h,\ \tau_e<\tau_r;\qquad\textbf{the agreement}\ d_{e\to p}=d_{p\to e}\ \text{is a CONSEQUENCE,}\ \neg\text{a condition}\ (\delta h_{\mathrm{out}}=\delta h_{\mathrm{in}}=\delta h\ \text{— the return word is endpoint-blind}\ [\mathrm{IT.53}(5)(\mathrm a);\ \mathrm{AT.44}(1)]);$$
$$\text{the unique round-trip order}\ e_1\prec r_1\prec e_2\prec r_2\ \text{stands}\ (1\ \text{of}\ 24)\ [\mathrm{IT.60}(1),\ \text{re-cited}];\qquad\text{the photon}\leftrightarrow\text{return-word pairing stays at the D-RS2 FACE level}\ [\mathrm{IT.56}(2);\ \mathrm{IT.60}(2)]$$
$$(2)\quad\textbf{THE CHART FACE, RE-DERIVED AS EXACT IDENTITIES:}\qquad d\tau_\pm=\sqrt{G}\,dx/(N\mp s),\ \ s=\sqrt{G}N^x\ [\mathrm{IT.53}(4);\ \mathrm{BM.34}(2)\ \text{'s null roots}]:$$
$$d\tau_+-d\tau_-=\frac{2\sqrt{G}\,dx\,s}{N^2-s^2}\quad[\text{machine: the cleared polynomial identity}\ \tfrac{1}{N-s}-\tfrac{1}{N+s}=\tfrac{2s}{N^2-s^2}\ \text{in}\ \mathbb Q[N,s];\ \text{the numeric witness}\ (G,dx,N,s)=(4,3,5,2):\ \ 2-\tfrac67=\tfrac87=\tfrac{2\cdot2\cdot3\cdot2}{21}];$$
$$\text{the half-distance}\ \tfrac{\sqrt{G}\,dx\,N^2}{N^2-s^2}\ \text{equals the proper length}\ \sqrt{G}\,dx\ \textbf{EXACTLY at}\ s=0\ [\text{machine: honest substitution}\ (N^2{-}s^2)|_{s=0}=N^2];\qquad\textbf{the T-conjugacy:}\ s\mapsto{-}s\ \text{swaps the legs}\ [\mathrm{BM.134}(3);\ \mathrm{IT.53}(5)(\mathrm b)];$$
$$\boxed{\ \text{agreement}\iff s\cdot dx=0\ \ [\mathrm{IT.53}(5)(\mathrm b),\ \text{witness census both directions}]\ \ \wedge\ \ \textbf{THE HONEST BOUNDARY:}\ \ \text{the stationarity instantiation scope stays DEFERRED}\ [\mathrm{D\text{-}RS4};\ \mathrm{IT.56}(3);\ \mathrm{IT.64}(6)],\ \ \text{and the disjointness row stands: agreement is guaranteed where the radar CANNOT RUN}\ [\mathrm{IT.53}(6)]\ }$$
$$(3)\quad\textbf{THE}\ \chi\textbf{-GATED LADDER TABLE (the read runs across the handshake ladder):}\qquad \mathcal T_0=2E_{\mathrm{int}}\,\mathfrak h/\ln2\ [\mathrm{BM.122}(2);\ \mathrm{Def\text{-}BM.17}(3)]\ \text{on the computed-cell floors}\ \{2,6,12,24,60\}:$$
$$\text{the coefficients}\ 2E_{\mathrm{int}}=(4,12,24,48,120)\ \ \text{(symbolic multiples of}\ \mathfrak h/\ln2\ \text{—}\ \neg\text{a value}\ [\mathrm{P5}]);\qquad\text{the span ratio EXACTLY}\ 30\ [\mathrm{IT.58}(1),(2)];$$
$$\text{the activation ceilings}\ N_{\min}=\lceil 2E_{\mathrm{int}}/\xi\rceil=(1,2,3,5,12)\ \text{at the rational WITNESS scale}\ \xi=10\ [\mathrm{IT.59}(2)\ \text{pattern — a parameter,}\ \neg\text{an issued value}];$$
$$\text{the anchor face: the Born-width sub-hop ladder}\ \{\mathfrak h/(2j\ln2)\}_{j\ge1}\ \text{and the E-FREE invariant}\ \tfrac1E\cdot\tfrac E2=\tfrac12\ \text{coefficient-wise at every floor}\ [\mathrm{BM.17}(3);\ \mathrm{AT.42}(3);\ \mathrm{Def\text{-}BM.4}(1)];$$
$$\boxed{\ \textbf{EVERY FACE IN ITS OWN CURRENCY:}\ \ \text{the ledger faces (hop/tick/order) carry counts and labels}\ (\mathfrak q^0);\ \text{the chart/anchor faces carry the}\ \mathfrak h/\ln2\ \text{monomials};\ \text{the gate is the binary}\ \chi\ \text{— the PRE-EXISTING mixed locus}\ [\mathrm{IT.4}(2);\ \mathrm{IT.58}(5)]:\ \ \text{the faces are a DICTIONARY,}\ \neg\text{a bridge}\ [\mathrm{D\text{-}RS2};\ \mathrm{BM.134}(5)],\ \ \text{the formed mixed loci remain exactly three, and}\ \neg\text{a cross-currency sum is formed}\ }$$
$$(4)\quad\textbf{THE EVENT CLASSIFICATION AT THE INGREDIENT LEVEL}\ (\mathrm{D\text{-}PJ4}\ \text{operationalized, form unfixed):}\qquad \text{the round-trip events at the emitter/reflector classify by the declared signature's INGREDIENTS}:$$
$$E_{\mathrm{vis}}=\min(\delta h,\ 4\delta\tau)\ln2\ \ \text{has INTEGER coefficients over the full}\ (1..8){\times}(1..8)\ \text{census},\quad I_{\mathrm{hid}}\in\mathbb Z\ln2\ \ [\mathrm{IT.2}(4)];$$
$$\text{the saturated reflector:}\ n_{\mathrm{real}}=0,\ n_{\mathcal V}=2E\ \ \text{(all channels virtual}\ [\mathrm{IT.53}(1);\ \mathrm{A5}])\ \ \text{— the radar CANNOT RUN there}\ [\mathrm{IT.53}(6)\ \text{re-cited}];$$
$$\text{the}\ \varepsilon_q\ \text{endpoints}\ [\mathrm{IT.64}(3)\ \text{re-cited}]:\ \ x_-=4\varepsilon_q\to0\ \text{at the sharp threshold (the crystallized classification)},\quad D_n>1\ \text{at}\ \varepsilon_q=\tfrac18\ \text{(the ensemble classification)}\ [\mathrm{BM.19};\ \mathrm{BM.137}(1)];$$
$$\boxed{\ \text{the degree's FUNCTIONAL FORM STAYS UNFIXED — the sub-debt stands}\ [\mathrm{IT.55}(5);\ \mathrm{IT.64}(3)];\qquad\text{count}\to\text{strength couplings stay barred}\ [\mathrm{BM.36}(3);\ \mathrm{BM.61}(8)(\mathrm O1);\ \mathrm{FT.73}(5)]\ }$$
$$(5)\quad\textbf{THE BAR ROWS OF THE READ:}\qquad\neg\text{an amplitude},\ \neg\text{a vertex},\ \neg\text{a weight},\ \neg\text{a rate is constructed — the read's alphabet is}\ \{\delta h,\ \Delta\tau_{\mathrm{rt}},\ d,\ \prec\}\ \cup\ \{\text{the chart coordinates}\}\ \cup\ \{\text{the existing}\ \mathfrak h/\ln2\ \text{monomials}\},\ \ \text{meeting the amplitude tokens in}\ \varnothing\ [\mathrm{IT.66}(2)\ \text{pattern re-run}];$$
$$\mathrm{P1}:\ \neg\text{a new dimensionful scale}\ (\xi\ \text{is a rational witness parameter};\ \text{the floors are frozen});\qquad\mathrm{P5}:\ \neg\text{a measured value}\ (\text{the tier scan});\qquad\text{the transit bar stands on three grounds}\ [\mathrm{IT.66}(1)]$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived (machine):}\ (1),(2),(3)\ \text{'s table},\ (4)\ \text{'s censuses};\qquad\textbf{formed as reads:}\ \text{the whole family — inside the D-RS6 declaration and its scope rows};\qquad\neg\text{a declaration},\qquad\neg\text{a value},\qquad\neg\text{an amplitude}$$

**Req.** A5, A6, P1, P5, C11, D0.6, D0.7, D1.8, D2.9 (Parts 1–2); EM.7, Def-H.9(2), Def-H.19 (Parts 2–3); IT.2(4), IT.4(2), IT.53(1),(4),(5),(6),(7),(8), IT.55(5),(7), IT.56(2),(3), IT.58(1),(2),(5), IT.59(2), IT.60(1),(2), IT.64(3),(6), IT.65, IT.66(1),(2) (this level); AT.42(3), AT.44(1) (Level 5); BM.17(3), BM.19, BM.34(2),(3), BM.36(3), BM.61(8), BM.83, BM.102(2),(4), BM.122(2), BM.134(3),(5), BM.137(1), BM.140(5), Def-BM.4(1), Def-BM.17(3), FT.73(5) (Parts 2, 4); exact polynomial identities with honest substitution, exact ceilings, Fraction witness arithmetic [math; machine: `opened_paths.py` §B, 5/5].

**Pf.**
$$(1):\ \ \text{the}\ 32{\times}5\ \text{census — integrality, the halving of the INTERVAL}\ (\tau_r-\tau_e)/2=\delta h,\ \text{and}\ e\prec r\ \text{at every cell}\ [\text{machine B1}];\qquad(2):\ \ \text{the cleared identity in}\ \mathbb Q[N,s],\ \text{the exact numeric witness}\ (\sqrt G=2\ \text{at}\ G{=}4),\ \text{the}\ s{=}0\ \text{substitution},\ \text{the flip}\ s\mapsto{-}s,\ \text{the}\ s{\cdot}dx\ \text{witness census both directions}\ [\text{machine B2}];$$
$$(3):\ \ 2E_{\mathrm{int}}\ \text{on the five floors},\ \text{the exact span}\ 120/4=30,\ \ \lceil 2E/\xi\rceil\ \text{as exact integer ceilings},\ \text{the invariant}\ (1/E)(E/2)=1/2\ \text{coefficient-wise}\ [\text{machine B3}];\qquad(4):\ \ \text{the}\ \min\ \text{coefficient census},\ \text{the endpoint Fractions}\ [\text{machine B5}];\qquad(3)\ \text{'s box},\ (5),(6):\ \ \text{the per-face alphabet census}\ [\text{machine B4}]\ \text{and record rows}.\ \blacksquare$$

**Phys.** The universe opened its eyes at IT.55(7), and this is what it first reads: its own echo.
The round-trip pair sits in the emitter's register as two integers and one halving of their
difference — every cell integral, the agreement between the two directions not a postulate but the
endpoint-blindness of the return word, and the order of the four events unique among the
twenty-four. The chart face answers in its own currency: the leg difference is exactly the shift
projection, the half-distance is exactly the proper length where the shift dies, and the two
synchronizations are each other's time reversal. Where the read refuses to go, it says so: the
stationarity scope is still the Architect's to instantiate, the saturated node guarantees agreement
precisely where nothing real can fly, and the classification of the events stops at its ingredients
because no functional form has been declared. A geometric read, formed at last, that radiates
nothing — which is exactly what it was declared to be.

---

### IT.69 — IT-O6 CLOSED: the δ-glue is the same frozen open bidirectional connector

**Thm.**
$$(1)\quad\textbf{THE SEAL-BLINDNESS AUDIT (the closure's core):}\qquad \text{IT.19's six derivation steps are re-read against their grounds; the seal species enters NOWHERE in the connector's attributes — it enters only in two SUPPORT-side registers}:$$
$$\begin{array}{l|l|l}\textbf{the step}\ [\mathrm{IT.19}(1)\text{–}(6)]&\textbf{the ground}&\textbf{seal-dependent?}\\\hline\text{the FORM: the open bidirectional pair}\ (e_{12},\bar e_{12})&\text{Census}\ \mathrm{FT.35};\ \mathrm{BM.17}(1)&\neg\text{— endpoint-local}\\\text{the}\ E_{\mathrm{int}}\ \text{residue}\ {+}2&\mathrm{D0.8};\ \text{Census}\ \mathrm{FT.35}(2);\ \mathrm{FT.44}(4)\ \text{'s UNIVERSAL taxonomy}\ E_{\mathrm{int}}=2E_{\mathrm{bidir}}+E_{\mathrm{uni}}&\neg\text{— ``universally, across every computed cell''}\\\text{the winding}\ d=0,\ \varepsilon=(-1)^d=+1&\mathrm{Def\text{-}H.32}(4)\ (\text{open}\Rightarrow S{=}0);\ \mathrm{BM.129}(3);\ \mathrm{BM.143}(3)&\neg\text{— chain-species property}\\\text{the charge telescoping (net 0)}&\mathrm{EM.9b};\ \mathrm{IT.19}(4)\ \text{'s end-sign algebra}&\neg\text{— sign algebra}\\\text{distinct sealed supports (edges,}\ \neg\text{shared attachments)}&\mathrm{Def\text{-}BM.9}(4);\ \mathrm{BM.1}(1);\ \text{the seal gates}\ 0/1\ [\mathrm{Def\text{-}BM.9}(2);\ \mathrm{AT.41}(3)]&\neg\text{— the seal GATES without constraining values}\\\text{the uniform rung-4 saturation}&\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT4.1}\text{–}\mathrm{CT4.3};\ \mathrm{D4.2}&\neg\text{— degree counts}\end{array}$$
$$\text{the seal species enters ONLY in:}\ \ (\mathrm i)\ \ \text{the support FLOOR values}\ (\delta\text{-pair/digon:}\ E_{\mathrm{int}}=2\ [\mathrm{FT.28};\ \mathrm{BM.110}(1)];\ \ \varepsilon\text{-triple/juncture:}\ E_{\mathrm{int}}=6\ [\text{Census}\ \mathrm{FT.35};\ \mathrm{BM.17}(1)]);\quad(\mathrm{ii})\ \ \text{the statistics register}\ (\Theta_{\mathrm{int}}\in2\mathbb Z\ \text{vs}\ 4\mathbb Z\ [\mathrm{BM.110}(4);\ \mathrm{BM.31}(4)]);$$
$$\boxed{\ \textbf{THE FROZEN}\ \delta\text{-SIDE WITNESS (machine re-run):}\ \ \text{the ``meson''}\ [\mathrm{BM.129}(1)]\ \text{IS a}\ \delta\text{-SEALED CP-pair WITH AN OPEN CONNECTOR:}\ \ k_M=k(c)+k(c^{\mathrm{CP}})+d=k+k+0=2k,\ \ \varepsilon_M=(-1)^{2k}=+1,\ \ j_M=k\in\mathbb Z\ \ \forall k\in0..8,\ \ \text{robust under BOTH orientation readings}\ [\mathrm{BM.129}(2)]\ \text{— a}\ \delta\text{-sealed object carrying an open}\ d{=}0\ \text{connector is IN the frozen inventory}\ }$$
$$(2)\quad\textbf{THE FIVE}\ \mathrm{IT\text{-}O6}\ \textbf{ATTRIBUTES, DERIVED FOR BOTH SHAPES}\ ((2,2)\ \text{digon-pair and}\ (2,3)\ \text{mixed})\ \textbf{[IT.62(4)'s question list, item by item]:}$$
$$(\mathrm a)\ \ \textbf{form:}\ \ \text{the open bidirectional pair}\ (q_1,p_2),(p_2,q_1)\ \text{— the UNIQUE connector species of the inventory}\ [\text{Census}\ \mathrm{FT.35};\ \mathrm{BM.17}(1);\ \mathrm{IT.19}(1)];\qquad(\mathrm b)\ \ E_{\mathrm{int}}\ \textbf{residue:}\ \ {+}2\ \text{per connector}\ [\mathrm{FT.44}(4)]:$$
$$\text{the}\ (2,2)\ \text{dimer} = 3\ \text{bidirectional pairs}\ (\text{digon}{+}\text{digon}{+}\text{connector})\Rightarrow E_{\mathrm{int}}=6;\qquad\text{the}\ (2,3)\ \text{cell} = 5\ \text{pairs}\ (\text{digon}{+}\text{juncture's three}{+}\text{glue})\Rightarrow E_{\mathrm{int}}=10;\qquad\text{adversarial: a}\ 2/4\text{-pair miscount gives}\ 4/8\ne6;$$
$$(\mathrm c)\ \ \textbf{winding:}\ \ d=0\ (\text{open}\Rightarrow S{=}0\ [\mathrm{Def\text{-}H.32}(4);\ \mathrm{BM.129}(3);\ \mathrm{BM.143}(3)]\ \text{— the (R10) disposition stands: registration data});\qquad(\mathrm d)\ \ \textbf{charge telescoping:}\ \ q(e){+}q(\bar e)=0\ \text{over all four end-signs}\ [\mathrm{EM.9b};\ \mathrm{IT.19}(4)],\ \text{and the digon census}\ W_2(Q)=(1,4,6,4,1),\ \Sigma=16=4^2,\ \text{passes through the glue unchanged}\ [\mathrm{BM.110}(3);\ \mathrm{BM.135}(2)];$$
$$(\mathrm e)\ \ \boldsymbol\varepsilon\ \textbf{sign:}\ \ {+}1=(-1)^0;\qquad\boxed{\ \text{the multiplicative exchange law}\ \varepsilon(\Gamma)=(-1)^A\ \text{stands UNFLIPPED under glue insertions (census}\ A{=}0..4\times\text{glues}\ 0..3)\ [\mathrm{BM.128}(7);\ \mathrm{IT.31}(4)]\ \text{— the}\ \delta\text{-containing groupings keep}\ \Theta_{\mathrm{int}}\in2\mathbb Z\ [\mathrm{BM.110}(4);\ \mathrm{BM.31}(4)]\ }$$
$$(3)\quad\textbf{THE TREE ASSEMBLY AND THE SEAL-BLIND BINDING ROW:}\qquad E^{\mathrm{tree}}_{\mathrm{int}}=\textstyle\sum_s E_{\mathrm{floor}}(s)+2\,(\#\text{supports}-1)\ \ \text{with the floors}\ (\delta{:}\,2,\ \varepsilon{:}\,6):$$
$$\textbf{the frozen family anchors reproduce EXACTLY:}\ \ (0,k{+}1)\mapsto 8k{+}6=(6,14,22,30)\ \text{at}\ k{=}0..3\ [\mathrm{IT.19}(3)];\qquad\text{adversarial:}\ \pm1\ \text{connector gives}\ 12/16\ne14;$$
$$\textbf{the new exact rows:}\ \ (2,0)\mapsto6,\quad(1,1)\mapsto10,\quad(3,0)\mapsto10,\quad(2,1)\mapsto14;\qquad\boxed{\ \mathcal B_{\mathrm{info}}=(E_{\mathrm{disj}}-E^{\mathrm{tree}}_{\mathrm{int}})\,u=-2\,(\#\text{supports}-1)\,u\ \ \text{SEAL-BLINDLY}\ [\mathrm{IT.20}(1)\ \text{generalized}]\ }$$
$$\text{strictly}\ <0\ \text{for}\ \#\text{supports}\ge2\ \text{and exactly}\ 0\ \text{for the lone support — the informational read STILL cannot adjudicate}\ [\mathrm{IT.20}(2)\ \text{re-cited}];\qquad\textbf{scope:}\ \ \mathrm{IT.46}\ \text{'s}\ E_{\mathrm{int}}=2N\ \text{skeleton is an ALL-}\varepsilon\ \text{row:}\ \delta\ \text{blocks carry}\ E_{\mathrm{disj}}=2N-2a\ (\text{machine census})\ \text{— recorded,}\ \neg\text{silently extended};$$
$(4)\quad\textbf{THE COINCIDENCE ROW (a PARALLEL,}\ \neg\textbf{an identification}\ [\mathrm{BM.134}(5)\ \text{discipline}]):\qquad \text{the bare}\ \Sigma_{12}\ \text{graph and the}\ (2,2)\ \text{glue dimer are the SAME}\ 4\text{-vertex}\ 6\text{-edge multigraph (machine: identical edge sets; the degree profile}\ (2,2,4,4));$
$$\Sigma_{12}\ \text{adds the boundary contact at}\ p_1\ (E_{\mathrm{bd}}{=}1)\Rightarrow\text{Census}\ \mathrm{FT.35}(4)\ \text{'s}\ n\ \text{profile}\ (3,4,4,2)\ \text{reproduced from the edge count};\qquad\textbf{the distinguishing datum is the SLOT/SEAL register:}$$
$$\boxed{\ \Sigma_{12}:\ \ N{=}3,\ \ \mathrm{Colour}\subseteq\{p_1,q_1,p_2\},\ \ \text{ONE}\ \varepsilon\text{-triple}\ [\text{Census}\ \mathrm{FT.35}(5);\ \mathrm{BM.17}(1)]\qquad\text{vs}\qquad\text{the dimer}:\ \ N{=}4,\ \ \text{TWO}\ \delta\text{-pairs}\ [\mathrm{IT.22}(1):\ g(4){=}3\ \text{all-}\delta;\ \mathrm{BM.110}(1)]\ }$$
$$\text{BOTH carry}\ E_{\mathrm{int}}=6:\ \ \textbf{E}_{\mathrm{int}}\ \textbf{does}\ \neg\textbf{determine the seal register}\ \text{— graph isomorphism does}\ \neg\text{imply ledger identity (colour stays}\ \neg\text{observable}\ [\mathrm{CT3.22}]\ \text{while the slot COUNTS are registration data)};$$
$$(5)\quad\textbf{THE SATURATION IS UNIFORM ACROSS SEAL SPECIES:}\qquad \text{every glued vertex sits at}\ n{=}4:\ \ D_{\mathrm{tick}}(4)=2^5=32>C_{\mathrm{cap}}=16\Rightarrow O(4)=16,\ D^-\text{-configured, RETAINED}\ \neg\text{accessible}\ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT4.1}\text{–}\mathrm{CT4.3};\ \mathrm{D4.2}];$$
$$\text{``composition creates saturation'' for the}\ \delta\text{-glue exactly as for the}\ \varepsilon\text{-glue}\ [\text{Census}\ \mathrm{FT.35}(4)\ \mathrm{Rmk};\ \mathrm{IT.19}(6)\ \text{generalized}];\qquad\text{the unglued digon vertices stay at}\ n{=}2\ (D_{\mathrm{tick}}{=}8,\ \text{admissible}),\ \text{the junctions at}\ n{=}3\ (16,\ \text{saturated but ADMISSIBLE});$$
$$(6)\quad\textbf{THE VERDICT AND THE SCOPE:}\qquad\boxed{\ \textbf{IT-O6 CLOSED:}\ \ \text{the}\ \delta\text{-involving glue species is DERIVED — the SAME frozen open bidirectional connector, with the five attributes at}\ (2);\ \ \mathrm{IT.62}(2)\ \text{'s ``1 of 3 block shapes derived'' is SUPERSEDED BY EXPLICIT ROW: 3 of 3}\ }$$
$$\textbf{scope rows:}\ \ (\mathrm i)\ \ \text{the closure is the PAIRWISE glue species + the tree-count assembly}\ [\mathrm{IT.19}(1)\ \text{pattern}];\quad(\mathrm{ii})\ \ \text{cyclic/fused glue stays REGISTRATION DATA — a closed connector may carry}\ d>0\ [\mathrm{BM.129}(3);\ \mathrm{BM.143}(3)],\ \neg\text{the sealed-composite species}\ [\mathrm{IT.19}(5)\ \text{extended}];\ \ \text{the shared-attachment (fusion) cells keep FT.50(4),(5)'s gluing law}\ [\mathrm{IT.25}\ \text{re-cited}];$$
$$(\mathrm{iii})\ \ \text{the AMPLITUDE side stays at IT-O2}\ [\mathrm{IT.27}(2)\ \text{'s three constructions}]:\ \ \text{the composed-support cover classifier, the connector's}\ v_\Gamma\ \text{inside composed covers, the multi-junction binding functional —}\ \mathrm{IT.62}(3)\ \text{'s UPSTREAM input is now NAMED};\qquad(\mathrm{iv})\ \ \mathrm{IT\text{-}O4}\ \text{'s closure stands, sharpened}\ \neg\text{reopened}\ [\mathrm{IT.62}(1)]$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{closed:}\ (6)\ \text{'s}\ \mathrm{IT\text{-}O6};\qquad\textbf{re-produced frozen rows:}\ \ \text{the ``meson''}\ k_M/\varepsilon_M/j_M\ \text{census},\ \ W_2(Q),\ \text{the}\ 8k{+}6\ \text{anchors},\ \text{Census}\ \mathrm{FT.35}(4)\ \text{'s}\ n\ \text{profile};\qquad\neg\text{a declaration},\quad\neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1,(7))]$$

**Req.** P5, D0.8, D3.9, CT0.5, CT0.6, CT3.22, CT4.1, CT4.3, D4.2, EM.9b (Parts 1–2); Def-H.32(4), FT.28, FT.32, FT.34(3), Def-BM.9(2),(4) (Parts 2–3); IT.19(1)–(6), IT.20(1),(2), IT.21(1), IT.22(1), IT.25, IT.27(2), IT.31(4), IT.46, IT.62(1),(2),(3),(4), IT-O2, IT-O4, IT-O6 (this level); AT.41(3), AT.63(2) (Level 5); BM.1(1), BM.17(1), BM.31(4), BM.110(1),(3),(4), BM.128(7), BM.129(1),(2),(3),(4), BM.134(5), BM.135(2), BM.143(3), FT.44(4), FT.50(4),(5), Census FT.35, Census FT.35(2),(4),(5) (Parts 2, 4); exact Laurent convolution, integer pair counts, exact tree censuses, degree profiles [math; machine: `opened_paths.py` §C, 5/5].

**Pf.**
$$(1):\ \ \text{the ``meson'' census re-run at every}\ k{=}0..8\ \text{under both orientation readings, with the closed-connector variant}\ \varepsilon_M{=}(-1)^d\ \text{exhibited}\ (d{=}0..4)\ [\text{machine C2}];\qquad(2):\ \ \text{the pair counts}\ 3/5\ \text{via}\ \mathrm{FT.44}(4)\ \text{'s taxonomy with the miscount adversarial; the four end-sign assignments; the}\ W_2\ \text{Laurent convolution}\ (1,4,6,4,1),\ \Sigma{=}16;\ \text{the exchange census}\ A{=}0..4\times g{=}0..3\ [\text{machine C3}];$$
$$(3):\ \ \text{the tree census over compositions}\ a{+}b\le4\ \text{against the frozen anchors with the}\ \pm1\ \text{adversarial; the}\ {-}2(\#s{-}1)u\ \text{identity at every composition; the}\ 2N{-}2a\ \text{scope census}\ [\text{machine C4}];\qquad(4):\ \ \text{the edge-set equality, the degree maps, the contact}\ {+}1,\ \text{the slot counts}\ [\text{machine C5}];\qquad(5):\ \ D_{\mathrm{tick}}(n)=2^{n+1}\ \text{at}\ n{=}2,3,4\ [\text{machine C6}];\qquad(6),(7):\ \ \text{record rows on the cited clauses}.\ \blacksquare$$

**Phys.** The builder's instrument stamped three glue slots and found one derived; the audit that
followed asked the only question that mattered — where, exactly, did the derivation use the seal? —
and the answer was nowhere. Openness is a chain property, the edge count is universal, the
telescoping is sign algebra, and the saturation is a degree count; the seal lives in the support's
floor value and its statistics, and touches none of it. The canon had even left a witness: the
"meson" has always been a δ-sealed pair holding hands across an open connector with zero winding
and positive parity, frozen since the baryomesonic era. So the glue closes the way the connector
did before it — not by inventing an object but by finding the one already in the inventory. The
prettiest row is the coincidence: the neutron's bare graph and the two-digon dimer are the same
six edges, and only the slot register tells them apart — three attachments sealed as one triple
versus four sealed as two pairs, both priced at six. E_int does not decide the seal; the ledger
keeps its registers apart, and the isotope grammar gains its missing glue without gaining a single
new object.

---

### IT.70 — The verdict: the rows, the bars, the census

**Thm.**
$$(1)\quad\textbf{THE ROW STATUS AFTER THE TIER:}\qquad\begin{array}{l|l}\textbf{the row}&\textbf{the status}\\\hline\mathrm{IT\text{-}O6}\ \text{(the}\ \delta\text{-glue species)}&\textbf{CLOSED}\ [\mathrm{IT.69}(6)]:\ \text{the same frozen connector; the five attributes derived; scope: pairwise glue + tree assembly}\\\mathrm{IT\text{-}O2}\ \text{(the binding value)}&\text{UNCHANGED — the three}\ \mathrm{IT.27}(2)\ \text{constructions stand; its UPSTREAM INPUT IS NOW NAMED}\ [\mathrm{IT.62}(3);\ \mathrm{IT.69}(6)(\mathrm{iii})]\\\mathrm{IT\text{-}O1}\ \text{(the transit leg)}&\text{UNCHANGED — three grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{IT.40}\text{–}\mathrm{IT.42};\ \mathrm{IT.66}(1)];\ \ \text{this tier constructs}\ \neg\text{an amplitude (the alphabet census}\ [\mathrm{IT.68}(5)])\\\mathrm{IT\text{-}O5}\ \text{(the cutoff's dynamical side)}&\text{UNCHANGED — at}\ \mathrm{IT\text{-}O1}\ [\mathrm{IT.30}(2)]\\\mathrm{IT\text{-}O3}&\text{stays CLOSED}\ [\mathrm{IT.60}(3)]\ \text{— the radar read is now its DECLARED operational grammar}\ [\mathrm{IT.68}]\\\text{the declaration register}&\text{UNCHANGED —}\ \mathrm{D\text{-}PJ7}\ \text{alone owed}\ [\mathrm{IT.66}(4)];\ \text{the three sub-debts stand}\end{array}$$
$$\boxed{\ \textbf{NO new open row};\qquad\textbf{ONE row closed}\ (\mathrm{IT\text{-}O6});\qquad\textbf{one path worked into a formed read family}\ (\text{the radar}\ [\mathrm{IT.68}])\ }$$
$$(2)\quad\textbf{THE BAR-CHECK (machine, 15/15):}\qquad\begin{array}{l|l}\textbf{the bar}&\textbf{the verdict}\\\hline\mathrm{P1}&\textbf{HONORED}: \neg\text{a new dimensionful scale — the glue rows are pure counts; the radar faces carry the existing monomials symbolically;}\ \xi=10\ \text{is a rational witness parameter}\ [\mathrm{IT.59}(2)\ \text{pattern}]\\\mathrm{P5}&\textbf{HONORED}: \text{zero decimal numeric tokens in the tier (machine scan); no value issued; the unissued registry stands}\ [\mathrm{IT.66}(5)]\\\text{the transit bar}&\textbf{STANDS on three grounds}: \neg\text{a vertex, amplitude, weight or rate is constructed; the radar family is read-level inside the D-RS6 declaration}\\\text{the incommensurability bar}&\textbf{HOLDS}: \text{the per-face alphabet census}\ [\mathrm{IT.68}(3)];\ \text{the formed mixed loci remain exactly three}\ [\mathrm{IT.4}(2)]\\\text{the arena bars}&\textbf{UNTOUCHED}: \neg\text{an arena object is added}\ [\mathrm{Def\text{-}H.41}/\mathrm{Def\text{-}H.42}]\\\text{count}\to\text{strength}&\textbf{BARRED as ever}: \mathrm{D\text{-}PJ4}\ \text{'s functional form stays unfixed}\ [\mathrm{IT.68}(4)]\\\text{species identification}&\textbf{NONE}: \text{``meson'', ``neutron'', ``tetraquark-type'' stay quoted}\ [\mathrm{Def\text{-}BM.3}(1,(7))]\\\text{the frozen canon}&\textbf{UNTOUCHED}\ [\mathrm{AT.63}(2)]:\ \mathrm{IT.62}(2)\ \text{'s rows superseded by explicit row at}\ \mathrm{IT.69}(6),\ \neg\text{edited in place}\end{array}$$
$$(3)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\text{the tier ISSUES NO DECLARATION (machine-scanned}\ [\mathrm{IT.67}(5);\ \text{machine A2}])\ \text{— it is a CONSTRUCTION tier on the declared vocabulary};\quad\S\mathrm{Cal\text{-}IT}\ \text{stays VALUE-FREE and unchanged};$$
$$\text{the unissued symbols stand:}\ \rho_{\mathrm B}\ [\mathrm{A\text{-}BM.9}],\ e_0\ [\mathrm{EM.25}(7)],\ \hat\mu'^2,\ \sigma_\ell,\ \sigma_\nu,\ \varepsilon_q\ (\mathrm{AT\text{-}O27}),\ (\varkappa,\beta)\ (\mathrm{AT\text{-}O3}),\ \ \text{the P1 scale slot},\ \ \text{the}\ \mu_{\mathrm{ch}}\ \text{family (Cal-F)}$$
$$(4)\quad\textbf{the machine state:}\qquad\texttt{opened\_paths.py}\to\textbf{15/15 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{22 checkers, 350 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{21 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad \text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(5)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and a closed row is a derived row — not a permitted one}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5 (Parts 1–2); Def-H.41, Def-H.42, Def-BM.3(1),(7) (Part 3); IT.4(2), IT.27(2), IT.30(2), IT.40–IT.42, IT.59(2), IT.60(3), IT.62(2),(3),(6), IT.66(1),(4),(5), IT.67(5), IT.68, IT.69(6), IT-O1, IT-O2, IT-O3, IT-O5, IT-O6 (this level); AT.39(8), AT.63(2),(4) (Level 5); A-BM.9, BM.122(6), EM.25(7) (Part 4); the full checker, the level runner and the level gate re-run end to end [math; machine: `opened_paths.py` §D, 3/3].

**Pf.**
$$(1),(2):\ \ \text{the row table assembled from}\ \mathrm{IT.68}\text{–}\mathrm{IT.69}\ \text{'s certifying markers}\ [\text{machine B1--B5, C2--C6, D1}];\ \ \text{the bar assembly with the tier scans}\ [\text{machine D2}];\qquad(3)\text{--}(5):\ \ \text{the declaration scan}\ [\text{machine A2}],\ \text{the runner and the gate re-run end to end}\ [\text{machine D3}].\ \ \text{No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** The directive said the declarations had opened obstructed paths, and the tier treated that
as a claim to verify, not a license: the census located the record's own gate phrases and sorted
them, and only then did the building start. One opened path produced a formed read family — the
radar, at last operational at its declared register, integral in every cell and radiating in none.
Another produced the tier's closure: the δ-glue turned out to be no new species at all but the old
connector wearing a different seal, with a meson for a witness and a neutron for a rhyme. What the
census said stays blocked remains blocked, and the tier is careful to leave it visibly so — the
amplitude side of the glue now has a named input and three named constructions waiting, the transit
still wants its deficit, and the values still want their era. One row closed, one family formed,
zero declarations, zero values: the paths were worked exactly as far as the ledger allows.

---

## §Cal-IT — unchanged (value-free)

**No act at this tier.** Tier IT.21 issues no declaration (machine-scanned at IT.67(5)/IT.70(3)):
it is a construction tier on the vocabulary declared at Tiers IT.17 and IT.20. The act register
stands as IT.66(4) records it — issued: D-PJ1–6, D-RS1–3, D-RS6–7, the BM.113(6) sector sync;
deferred: D-RS4; owed: **D-PJ7 alone** + the three sub-debts. **No calibration parameter is added,
valued, or re-scoped**: the P1 scale slot, $\varepsilon_q$ (AT-O27), $e_0$ [EM.25(7)],
$(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$ [A-BM.9], $\hat\mu'^2$, $\sigma_\ell$,
$\sigma_\nu$, the $\mu_{\mathrm{ch}}$ family (Cal-F), the read rules (M1′)–(M3′) [AT.54(6)], the
lift/vielbein/P4 profile [AT.63(3)], and the mass-read route choice [IT.14(3); BM.30(5)] all stand
unchanged; the witness scale $\xi=10$ at IT.68(3) is a rational PARAMETER [IT.59(2) pattern], not
an issued value. The Calibration Era stays **deferred** [AT.63(4)].

## §Open-IT additions from Tier IT.21

| row | content | locus |
|---|---|---|
| (IT-O6) → **CLOSED** | the δ-involving connector glue species is DERIVED: the SAME frozen open bidirectional connector (IT.19's steps are seal-blind; the "meson" [BM.129(1)] is the frozen δ-side witness); the five attributes for both shapes — form, E_int residue +2 [FT.44(4): (2,2)→6, (2,3)→10], winding d=0, charge telescoping (W₂ passes through), ε=+1 with the exchange law unflipped; the tree assembly reproduces 8k+6 exactly and gives (2,0)→6, (1,1)→10, (3,0)→10; B_info = −2u per connector seal-blindly; the Σ₁₂/dimer graph coincidence recorded as a parallel (the slot register distinguishes); IT.62(2)'s "1 of 3" superseded → 3 of 3. Scope: pairwise glue + tree assembly; cyclic/fused = registration data; the amplitude side stays at IT-O2 (its upstream input now named) | IT.69(1)–(6); IT.62(2),(3),(4) |
| (none other new) | Tier IT.21 opens **no other row**. The radar read family is formed inside the D-RS6 declaration [IT.68]; IT-O1/IT-O2/IT-O5 unchanged; the declaration register unchanged [IT.66(4)]; the still-blocked map with grounds at IT.67(4) | IT.67(2),(4); IT.68; IT.70(1) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4); IT.57(5); IT.60(4); IT.62(4);
IT.66(6)]: (IT-O1) the formed transit-leg amplitude — three grounds, deficit 1′ [IT.41]; (IT-O2) the
binding value — the three IT.27(2) constructions (the δ-glue input now named); (IT-O5) the isotope
cutoff — the dynamical side at IT-O1; AT-O30/AT-O32 the heavy censuses; the owed route choice
[IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the Level-5 inheritance [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.22: the rung-one translation layer — the Architect's four claims adjudicated, and the 1-reach theorem

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.22 — the Architect's directive: verify the
hypothesis that *the rung-1 forces* $(G,\,W,\,H,\,D^+)$ *are the translation layer between the
discrete ledger and the emergent continuous geometry*, in four claims — (1) they have metric
coordinates (unlike the rung-0 seals $J_i,K_i$, which have zero metric coordinates); (2) they
propagate through channels, not ticks; (3) the shift $W_i$ is $T$-odd and encodes the time
direction; (4) being the geometry, they can measure the ledger's phase, winding and delta — plus
the Architect's note that the rung-1 forces *cannot reach beyond 1 hop* while simultaneously
mediating the entire $S$ sector. Executed as an adjudication, not an adoption: every component
is machine-checked against frozen rows and separated **DERIVED / DECLARED / BARRED / NOT
DERIVED (scoped absence)**. Two claims come out whole, two come out split, one naming is barred,
and the note yields the tier's sharpest new row.
**Tags.** IT.71–IT.78. **Pattern.** the adjudication tiers (Tier IT.16's premise audit + IT.21's
construction shape), corrections recorded in-tier, never overwritten.
**Status.** discovery-phase working tier. Nothing is adopted into the frozen canon; **no
declaration issues** (machine-scanned); §Cal-IT stays value-free and unchanged; no clause of
Parts 1–4, of Level 5's closed record, or of Tiers IT.1–IT.21 is modified [AT.63(2)] — the one
citation slip in the directive is recorded as a PREMISE CORRECTION at IT.71(4), never applied to
a frozen row. No measured value enters [P5]; no new dimensionful scale [P1]; species names stay
quoted and no identification is made [Def-BM.3(1),(7)].
**Machine.** `era2/level6_isotopic/checks/translation_layer.py` → **43/43 exact** (Gauss(i) over
Fractions for the $4\times4$ pair algebra; exact rational $\mathrm{LDL}^\top$ inertia; multivariate
Fraction polynomial rings; a FORMAL JET ALGEBRA over $\mathbb Q$ for the linearized Einstein
tensor; exhaustive enumeration; exact integer binomials; text censuses with live AND dead
witnesses so no absence scan can pass dead; NO floating point); `run_all_level6.py` →
**23 checkers, 393 exact markers, 0 failures**; `check_level6_format.py` → the gate over all
twenty-two Part 6 documents (78 IT-blocks). **NON-VACUITY (mutation audit, run before any tier text was
written):** six deliberate perturbations of the checker — the interleaving closed form
$2^{2n-1}\mapsto2^{2n}$, the constraint-cell list, the radar half-distance, the covering
sub-collection bound, the shift-monomial count, the joint-read derivative census — each turned
exactly its own marker (and, where the component feeds the verdict table, IT.78's assembly) RED;
and the flipped-signature representative $\eta'=(+,+,+,-)$ [C13's opposite choice] was run through
the whole wave-operator census as a convention adversarial (IT.73(4)).
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mid-batch intake.** The builder's `comms/0009` (Lean Tier 2 kernel-green) landed while this tier
was building; its three machine-aimed items are answered at **IT.77** (the Pauli pin adopted,
$[\Sigma,W_i]=0$ re-certified against an incoming contradictory hand computation, and the
Lie-closure rank rows delivered as an exact-elimination receipt). The tier's tag range is
IT.71–IT.78; the checker carries 43 markers.
**Mandate.** The Architect's directive (session 13r), executed in full: *"Verify each claim
against the frozen canon. Separate derived from declared from barred. Do not accept the
hypothesis by fiat — prove or disprove each component … Do not force a declaration. If a claim
requires one, state it as owed."* And the note: the SM weak-boson framing is the Architect's own
clarification and *does not enter the corpus* — flagged at IT.71(3), barred at IT.76(5).

---

### IT.71 — The intake: the four claims, the vocabulary adjudication, and the premise corrections

**Thm.**
$$(1)\quad\textbf{THE FOUR CLAIMS, AS STATED (each adjudicated independently, none assumed):}\qquad\begin{array}{l|l}\textbf{claim}&\textbf{the Architect's words}\\\hline(1)&\text{the rung-1 forces ARE the dimensions: they have metric coordinates, unlike the rung-0 gifts}\ J_i,K_i\ \text{which have zero metric coordinates}\ [\mathrm{FT.141}(5)]\\(2)&\text{they propagate through CHANNELS, not ticks: geometric propagators in the emergent metric,}\ \neg\text{ledger updates}\\(3)&\text{the shift}\ W_i\ \text{is}\ T\text{-odd and encodes left/right (the time direction)}\\(4)&\text{being the geometry, they measure the ledger's phase jumps, winding changes and delta values}\end{array}$$
$$(2)\quad\textbf{THE VOCABULARY ADJUDICATION (three terms, none of them corpus terms):}\qquad(\mathrm a)\ \ \text{``pre-dim''/``dim''}: \textbf{BUILDER-SIDE vocabulary, flagged}\ \neg\textbf{adopted}\ [\mathrm{IT.64}(5)(\mathrm c);\ \mathrm{IT.64}(8)(\mathrm{P6})\ \text{re-cited}]:$$
$$\text{the corpus locus of the DISCRETE face is the tick face}\ [\mathrm{D0.7};\ \mathrm{C11};\ \mathrm{IT.53}(4)]\ \text{and of the CONTINUOUS face the emergent chart projection}\ [\mathrm{IT.56}(2);\ \mathrm{CT2.6}];\ \text{the ADJECTIVE ``pre-dimensional'' IS canon-attested}\ [\mathrm{Def\text{-}H.8}\ \mathrm{Rmk}:\ \text{``pre-dimensionally: spin}=\text{interior edge phase carried by the weak sector''};\ \mathrm{BM}'\text{s referent census}:\ \text{``the pre-dimension graph is a time-directed graph of nodes''}]\ \text{— the layer NOUN-PHRASE is not;}$$
$$(\mathrm b)\ \ \text{``translation layer''}: \neg\text{a corpus term. What it names is a frozen TRIAD: the DICTIONARY}\ [\mathrm{D2.1};\ \mathrm{CT1.12};\ \mathrm{FT.30}],\ \text{the BRIDGE THEOREM}\ [\mathrm{CT2.6}:\ \text{``it converts combinatorics (edges, ticks, counters) into the differential geometry''}],\ \text{and the CONTRACTION}\ [\mathrm{D1.6};\ \mathrm{D1.7};\ \mathrm{D3.5}];$$
$$\text{and the standing discipline attaches to it: a DICTIONARY}\ \neg\text{a bridge, partners}\ \neg\text{equals}\ [\mathrm{D\text{-}RS2}\ @\ \mathrm{IT.56}(2);\ \mathrm{BM.134}(5);\ \mathrm{IT.68}(3)];\qquad(\mathrm c)\ \ \text{``the rung-0 gifts''}=\text{the seals, ``the six''}\ [\mathrm{FT.30};\ \mathrm{IT.53}(2);\ \mathrm{D1.2}].$$
$$(3)\quad\textbf{THE SM FRAMING FLAG:}\qquad\text{the Architect's note (a finite range resembling the SM weak bosons, but mediating the whole}\ S\ \text{sector at once) is recorded as CLARIFICATION OF INTENT,}\ \neg\textbf{adopted},\ \neg\textbf{a premise}:$$
$$\boxed{\ \text{the identification bars stand: ``no SM species reading; no claim that the SM weak interaction is reproduced''}\ [\mathrm{FT.157}\ \mathrm{Rmk}];\ \ \text{``no family-mass read exists in the corpus … external data enters no derivation''}\ [\mathrm{FT.158}(5)];\ \ \mathrm{P1},\ \mathrm{P5};\ \ \text{the}\ [\mathrm{EXT}]\ \text{quarantine}\ [\mathrm{IT.7}(2)]\ }$$
$$(4)\quad\textbf{THE PREMISE CORRECTIONS (the rows win; recorded, never applied to a frozen row):}\qquad\begin{array}{l|l}\textbf{\#}&\textbf{the correction}\\\hline(\mathrm{P1})&\text{the directive attributes the shift functional}\ g_{0i}=\varkappa\beta\,\Omega^2 w_i\ \text{to}\ \mathrm{BM.34}(2);\ \textbf{the frozen loci are}\ \mathrm{BM.34}(1)\ (N_i=\Omega^2\varkappa\beta w_i)\ \textbf{and}\ \mathrm{BM.34}(3)\ (g_{ij}N^j=N_i=g_{0i}),\ \text{with}\ \mathrm{FT.157}(1)\ \text{the block-identity row —}\ \mathrm{BM.34}(2)\ \text{carries the line element and the flat-vacuum row}\\\\(\mathrm{P2})&\text{the}\ T\text{-census is}\ \textbf{10 even / 6 odd,}\ \neg\ 7/9:\ \text{the}\ T\text{-odd six are}\ \{W_i\}\cup\{K_i\}\ [\mathrm{CT1.1};\ \mathrm{CT1.2}]\ \text{— so ``}W_i\ \text{is}\ T\text{-odd'' is true but}\ \neg\textbf{distinctive};\ \text{the distinctive frozen row is}\ \mathrm{FT.156}(2)\text{'s}\ 7/3\ \text{split OF THE}\ S\text{-EVEN BLOCK}\\\\(\mathrm{P3})&\text{claim 1's word ``ARE'' collides with a standing}\ \neg\textbf{adoption:}\ \mathrm{IT.52}(3)\text{'s four prices and}\ \mathrm{IT.54}(1)\text{'s verdict row ``the metric identification (10:10) —}\ \neg\text{ADOPTED''. The tier therefore adjudicates TWO readings separately: the COORDINATE reading (derived) and the IDENTITY reading}\ (\neg\text{adopted, priced})\\\\(\mathrm{P4})&\text{claim 4's ``delta'' is ambiguous against the record's own vocabulary; THREE readings are adjudicated separately at}\ \mathrm{IT.75}(6):\ \delta h\ \text{the hop count}\ [\mathrm{D0.6};\ \mathrm{D\text{-}RS3}],\ \text{the}\ \delta\text{-seal/digon}\ [\mathrm{IT.69}],\ \text{and}\ \Delta\ \text{the ledger increment}\ [\mathrm{CT0.3};\ \mathrm{D1.5}]\\\\(\mathrm{P5})&\text{``channel'' has THREE frozen senses: the pair channel}\ [\mathrm{A2};\ \mathrm{CT0.6};\ \mathrm{CT0.12}],\ \mathrm{D1.10}\text{'s node-force channels}\ \{\text{bound, transit, holonomy, charge, flux}\},\ \text{and the channel classes/angles}\ [\mathrm{FT.112};\ \mathrm{FT.119};\ \mathrm{FT.142}];\ \textbf{the tier uses the first, and records that}\ \mathrm{D1.10}\ \textbf{is the frozen occurrence of the word inside a force clause}\\\hline(\mathrm{P6})&\text{``the 16 basis elements''}=\mathrm{CT1.2}\text{'s six rows grouped:}\ 1{+}1{+}5{+}3{+}3{+}3=16\ [\mathrm{CT1.1};\ \mathrm{CT0.12}]\end{array}$$
$$(5)\quad\textbf{status:}\qquad\textbf{record rows:}\ (1)\text{--}(4);\qquad\neg\text{a declaration},\qquad\neg\text{a value},\qquad\neg\text{an adoption};\qquad\text{the four claims pass to}\ \mathrm{IT.72}\text{--}\mathrm{IT.75},\ \text{the note to}\ \mathrm{IT.76}$$

**Req.** P1, P5 (Parts 1–2); A2, C11, D0.6, D0.7, D1.2, D1.5, D1.6, D1.7, D1.10, D2.1, D3.5 (Parts 1–2); CT0.6, CT0.12, CT1.1, CT1.2, CT1.12, CT2.6 (Parts 1–2); Def-H.8 (Part 3); FT.30, FT.112, FT.119, FT.141(5), FT.142, FT.156(2), FT.157(1), FT.158(5) (Part 3); BM.34(1),(2),(3) (Part 4); IT.7(2), IT.52(3), IT.53(2),(4), IT.54(1), IT.56(2), IT.64(5),(8), IT.68(3), IT.69 (this level); BM.134(5), Def-BM.3(1),(7) (Part 4); text censuses against the frozen records with live witnesses [math; machine: `translation_layer.py` §§A, B6, F4].

**Pf.**
$$(1)\text{--}(3):\ \ \text{record rows; the vocabulary flags are text censuses against the frozen clauses cited}\ [\text{machine: live witnesses present, dead controls absent}];\qquad(4):\ \ \text{each correction is a located citation}\ [\text{machine: }\mathrm{B3}\text{'s text census for}(\mathrm{P1});\ \mathrm{A3}\text{'s parity census for}(\mathrm{P2});\ \mathrm{B6}\text{'s}\ \neg\text{adoption census for}(\mathrm{P3})];$$
$$(5):\ \ \text{the status assembly. No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** The directive arrived with a hypothesis and a vocabulary, and the tier treated both as
data to be located before either was used. Three of the hypothesis's words are not the corpus's:
"pre-dim" is builder-side and was already flagged as not adopted, "translation layer" names a
triad the record already carries under other names — a dictionary, a bridge theorem, and a
contraction — and "gifts" is a study word for the seals. The Standard Model framing the
Architect offered as a thinking aid is recorded exactly there and nowhere else, with the bars
that keep it out quoted rather than paraphrased. Six premise corrections follow, the sharpest
being that the T-census is ten against six and not seven against nine, so the shift's T-oddness
is true but not distinctive until it is read inside the metric sector. None of the corrections
touches a frozen row; all of them ride with the claims they qualify.

---

### IT.72 — Claim 1 adjudicated: the metric-coordinate census is DERIVED; the identity reading stays priced

**Thm.**
$$(1)\quad\textbf{THE PARITY CENSUS, REBUILT FROM THE PAULI TENSORS (machine, all 16):}\qquad\text{the}\ \mathrm{CT1.2}\ \text{generators reconstructed as exact}\ 4\times4\ \mathbb Q(i)\ \text{matrices are a basis (flattening rank}\ 16;\ \text{dropping any one gives}\ 15):$$
$$S\text{-even}=10=\{E_0,\ \Sigma,\ \hat E^{ij}\ (5),\ W_i\ (3)\}=G_5+W_3+H_1+D^+_1;\qquad S\text{-odd}=6=\{J_i\ (3),\ K_i\ (3)\}=J^+_3+J^-_3\quad[\mathrm{FT.141}(1)];$$
$$\operatorname{tr}\operatorname{Ad}(\mathbb S)=10-6=4,\qquad\operatorname{rk}\operatorname{Ad}(\mathbb S)=16,\qquad\ker\operatorname{Ad}(\mathbb S)=\{0\}\quad[\mathrm{FT.141}(5)];\qquad(S,T)\ \text{blocks}=(7,3,3,3)\quad[\mathrm{CT1.1}];$$
$$\text{the aspect table with both parities}\ [\mathrm{CT0.12}]:\quad D^+=(+,+),\ H=(+,+),\ G=(+,+)\ (5),\ W=(+,-)\ (3),\ J^+=(-,+)\ (3),\ J^-=(-,-)\ (3)$$
$$(2)\quad\textbf{THE METRIC-COORDINATE ROW (derived):}\qquad\text{the four rung-1 blocks carry}\ 5+3+1+1=10=\#\{g_{\mu\nu}=g_{\nu\mu}\}=\tfrac{4\cdot5}2\ \text{metric coordinates, cell by cell}\ [\mathrm{CT1.12};\ \mathrm{CT1.12a}(2);\ \mathrm{FT.30};\ \mathrm{FT.156}(2)]:$$
$$g_{\mu\nu}\ \leftrightarrow\ \underbrace{\hat h_{ij}\ (5)}_{G:\ \text{spin-2 shear}}\ \oplus\ \underbrace{\Sigma_{\mathrm{tr}}\ (1)}_{H:\ \text{volume mode}}\ \oplus\ \underbrace{a_{00}\ (1)}_{D^+:\ \Omega\ \text{conformal}}\ \oplus\ \underbrace{w_i\ (3)}_{W:\ \text{shift}\ N_i=\beta w_i};\qquad\text{components}\ (g_{00}:1;\ g_{0i}:3;\ g_{ij}:6);$$
$$\boxed{\ \text{the}\ S\text{-odd six carry ZERO metric coordinates}\ [\mathrm{FT.141}(5);\ \mathrm{CT1.12a}(2);\ \mathrm{FT.30};\ \mathrm{Def\text{-}H.14}]:\ \ \mathrm{D2.1}\text{'s}\ X_{(+)}=a_{00}E_0+q_{ij}E^{ij},\ X_{(-)}=w_iW_i\ \text{have as carriers exactly the ten}\ S\text{-even generators}\ }$$
$$\text{ADVERSARIAL (machine): a fake carrier}\ (J_1)\ \text{has}\ S\text{-grade}\ -1,\ \text{so any dictionary row built on it would be}\ S\text{-odd and could not enter}\ g_{\mu\nu},\ \text{which is orientation-even}\ [\mathrm{CT1.12a}(2)\ \text{consequence}]$$
$$(3)\quad\textbf{THE BIJECTION, AND ITS ONE NONLINEAR CELL (new precision row):}\qquad\text{the dictionary is a bijection}\ 10\leftrightarrow10\ [\mathrm{CT1.12}\ \mathrm{Pf}:\ \text{``the dictionary is a bijection''}],\ \text{but}\ \neg\text{a linear one}:$$
$$9\ \text{cells are LINEAR — homogeneous of degree exactly}\ 1\ \text{in the metric coefficients}\ (q,w),\ \text{with}\ \varkappa,\beta\ \text{entering as}\ \mathrm{P4}\ \text{scalars, and with the exact rational inverse}\ q_{ij}=(\bar g_{ij}-\delta_{ij})/\varkappa,\ w_i=\bar g_{0i}/(\varkappa\beta)\ \text{round-tripping identically};$$
$$\boxed{\ \text{the TENTH cell is EXPONENTIAL:}\ \ \Omega=e^{\alpha_\Omega a_{00}},\quad g_{00}=-\Omega^2\ \ \Longrightarrow\ \ a_{00}\ \text{is never a component of}\ g,\ \text{only the exponent}\ }$$
$$\text{which is}\ \mathrm{IT.52}(3)(\mathrm i)\text{'s first price, re-certified here from the frozen text rather than re-argued}$$
$$(4)\quad\textbf{THE ACTIVATION ROW (new):}\qquad\text{THREE independent characterizations of ONE set, machine-verified to coincide:}$$
$$(\mathrm i)\ \ \text{the newly activated aspects at rung one:}\ \ \mathcal A(1)\setminus\mathcal A(0)=\{G,W,H,D^+\}\ \ [\mathrm{CT0.13}:\ \mathcal A(0)=\{J\},\ \mathcal A(1)=\{J,G,W,H,D^+\}];$$
$$(\mathrm{ii})\ \ \text{the}\ S\text{-even block of the pair algebra}\ (10\ \text{of}\ 16)\ [\mathrm{FT.141}(1)];\qquad(\mathrm{iii})\ \ \mathrm{CT1.12}\text{'s dictionary carrier set}\ \{E_0,\Sigma,\hat E^{ij},W_i\}\ [\mathrm{CT1.12a}(2)];$$
$$\dim\mathcal K_1-\dim\mathcal K_0=16-6=10\ \ [\mathrm{CT0.14}];\qquad\boxed{\ \text{the layer SWITCHES ON with the first crystallized real edge:}\ \mathrm{CT0.13}\text{'s own proof derives}\ \mathcal A(1)\ \text{from ``one incident real edge}\implies\vee^2\ \text{populated}\implies\text{the}\ S\text{-even aspects act''}\ }$$
$$(5)\quad\textbf{THE VERDICT ON CLAIM 1 (two readings, two verdicts):}\qquad\begin{array}{l|l}\textbf{the reading}&\textbf{the verdict}\\\hline\text{``they HAVE metric coordinates''}&\textbf{DERIVED}\ [(2),(3);\ \mathrm{FT.141}(5);\ \mathrm{CT1.12};\ \mathrm{CT1.12a}(2);\ \mathrm{FT.30};\ \mathrm{FT.156}(2)]\ \text{— all four blocks,}\ 5{+}3{+}1{+}1{=}10,\ \text{and the seals zero}\\\text{``they ARE the dimensions''}&\textbf{NOT ADOPTED — priced}\ [\mathrm{IT.52}(3)\text{'s four prices: nonlinearity}\ (3),\ \neg\text{swap-evenness}\ (10\to7),\ \text{chart side vs register side, the count}\to\text{strength bar};\ \mathrm{IT.54}(1)\text{'s verdict row}]\ \text{— an adoption would be the Architect's act;}\ \neg\text{forced here,}\ \neg\text{a new register entry}\end{array}$$
$$\text{the discipline that separates them is standing: a dictionary}\ \neg\text{an identity, partners}\ \neg\text{equals}\ [\mathrm{D\text{-}RS2};\ \mathrm{BM.134}(5);\ \mathrm{IT.68}(3)]$$

**Req.** P1, P4, P5 (Parts 1–2); A3, A8, C1, C13, D2.1 (Part 1); CT0.7, CT0.12, CT0.13, CT0.14, CT1.1, CT1.2, CT1.10, CT1.12, CT1.12a (Parts 1–2); Def-H.14, FT.30, FT.141, FT.156(2), FT.157(1) (Part 3); BM.34(1),(3) (Part 4); IT.52(3), IT.54(1), IT.56(2), IT.68(3) (this level); BM.134(5) (Part 4); exact $\mathbb Q(i)$ matrix arithmetic, exact flattening ranks, exhaustive subset censuses, multivariate Fraction polynomials, exact rational round-trips [math; machine: `translation_layer.py` §§A1–A5, B1–B6, 11/11].

**Pf.**
$$(1):\ \ \text{the}\ 16\ \text{generators rebuilt from}\ \sigma_\mu\otimes\sigma_\nu\ \text{with}\ \mathbb S=\tfrac12(E_0+\Sigma),\ \mathbb S^2=E_0;\ \ \operatorname{Ad}(\mathbb S)X=\mathbb S X\mathbb S\ \text{entrywise};\ \ T\ \text{through the exact Pauli-tensor decomposition}\ T(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu(\sigma_\mu\otimes\sigma_\nu),\ \eta=(-,+,+,+)\ [\mathrm{A3};\ \mathrm{C13}];\ \ \operatorname{Ad}(\mathbb S)\ \text{as a}\ 16\times16\ \text{matrix in the Pauli basis (trace and rank)};\ \ \Pi_{\mathcal R},\Pi_{\mathcal V}\ \text{idempotent, orthogonal, complete, traces}\ 3,1\ [\text{machine A1--A3}];$$
$$(2):\ \ \text{the counts}\ 1{+}1{+}5{+}3=10=\tfrac{4\cdot5}2\ \text{against the component split}\ (1;3;6);\ \ \mathrm{D2.1}\text{'s carrier census (10 of 10 nonzero, 6 of 6 identically zero) with the fake-carrier adversarial}\ [\text{machine B1, B5}];$$
$$(3):\ \ \text{the degree census in}\ (q,w)\ \text{and the exact inverse round-trip on three rational witnesses}\ [\text{machine B2}];\ \ \text{the exponential cell located in the frozen text with live witnesses}\ [\text{machine B2}];$$
$$(4):\ \ \text{the three set/dimension censuses and the difference}\ 16-6=10\ [\text{machine A5}];\qquad(5):\ \ \text{the record rows on the cited clauses}\ [\text{machine B6}].\ \blacksquare$$

**Phys.** The first claim survives, and survives in the only form the corpus allows. Rebuilt from
the Pauli tensors rather than trusted from citation, the sixteen generators grade ten against six
under the swap, and the ten are precisely the four forces the directive names: five shears, three
shifts, one volume mode, one conformal factor — ten coefficients against ten metric components,
cell for cell, with the six seals carrying nothing geometric at all. The bijection is real but not
linear: nine cells invert rationally and the tenth is an exponential, which is the first of the
four prices the record already attached to any stronger reading. So "they have metric
coordinates" is derived, "they are the dimensions" remains a priced identification the Architect
has not made, and this tier does not make it for him. The bonus is the activation row: the set
that lights up at rung one, the set that is swap-even, and the set that carries the metric are one
set of ten, which is why the layer can be said to switch on with the first crystallized edge.

---

### IT.73 — Claim 2 adjudicated: ticks are ledger events, the forces are pair-channel geometry, and only one block is a wave

**Thm.**
$$(1)\quad\textbf{THE TICK SIDE (derived):}\qquad\text{the tick is a LEDGER event and carries no metric content}\ [\mathrm{A6};\ \mathrm{A7};\ \mathrm{D0.7};\ \mathrm{C11}]:$$
$$\tau_n\to\tau_{n+1}:\ \rho\mapsto U\rho U^\dagger,\quad U\sim\mu_\star(\mathrm{SU}(2)),\quad U\notin\mathfrak L,\quad\mathcal T^2\ne\mathbb1,\quad\neg\exists\,\tau^{-1};\qquad|\mathfrak L(\tau_n)|=\sum_{k<n}n_{\mathrm{real\_out}}(\tau_k);$$
$$\text{machine census over all}\ 4^5=1024\ \text{five-tick histories: the record is monotone in every one, strictly increasing exactly at the emitting ticks, and the reversed record strictly decreases somewhere whenever content was emitted}\ \Longrightarrow\ \neg\text{an inverse on the record};$$
$$\text{the metric enters geometry as an INCREMENT and the forces as COEFFICIENTS:}\quad ds^2(e)=g_{\mu\nu}(e)\Delta x^\mu_e\Delta x^\nu_e\ [\mathrm{D1.6}],\quad x^0:=\tau_n\ [\mathrm{D1.8}]\ \ \Longrightarrow\ \ \text{``the line-element channel contracts metric data with tick data''}\ [\mathrm{FT.159}(4)]$$
$$(2)\quad\textbf{THE CHANNEL SIDE (derived, in the pair-channel sense of}\ \mathrm{IT.71}(4)(\mathrm{P5})\textbf{):}\qquad\text{a force aspect's carrier space is the pair channel of ONE pair}\ [\mathrm{A1};\ \mathrm{A2};\ \mathrm{CT0.12}:\ 3{+}3{+}5{+}3{+}1{+}1=16=C_{\mathrm{cap}}],\ \text{and}\ \mathrm{D1.10}\ \text{is the frozen force clause that uses the word: ``node force:}\ \mathbf F\!\restriction_v\ \text{resolves local information content into channels}\ \{\text{bound, transit, holonomy, charge, flux}\}\text{''};$$
$$\text{the propagator object of the corpus is the masked resolvent}\ Z(\mathcal R,n)=\langle\mathrm{out}|(1-\mathbf F_M^{(n)})^{-1}|\mathrm{in}\rangle,\ \ \text{poles}=\text{the rung-}n\ \text{spectrum}\ [\mathrm{D2.4};\ \mathrm{D2.5};\ \mathrm{CT2.5}],\ \ \text{and}\ \neg\text{an accessible pole}\implies\neg\text{a propagating mode}\ [\mathrm{CT4.2}]$$
$$(3)\quad\textbf{THE WAVE-OPERATOR CENSUS (new; machine: a formal jet algebra over}\ \mathbb Q\textbf{):}\qquad\mathrm{CT1.18}\text{'s linearized Einstein tensor is re-derived by TWO independent routes — its displayed formula and the linearized Christoffel/Ricci pipeline — and the two agree coefficient-wise on all ten components:}$$
$$\bar G^{(1)}[h]_{\mu\nu}+\tfrac12\Box h_{\mu\nu}\ =\ \tfrac12\bigl[-\partial_\mu\partial_\nu T+\partial_\mu V_\nu+\partial_\nu V_\mu+\eta_{\mu\nu}(\Box T-\partial^\lambda V_\lambda)\bigr],\qquad T:=h^\lambda{}_\lambda,\quad V_\nu:=\partial^\lambda h_{\nu\lambda}$$
$$\text{an identity whose right-hand side is built ONLY from the trace and divergence jets}\ \Longrightarrow\ \text{on the traceless-transverse locus}\ (T=0,\ V_\nu=0\ \text{with all their jets)}\ \ \bar G^{(1)}=-\tfrac12\Box h\ \ \text{(the massless wave operator)};$$
$$\text{gauge invariance}\ \bar G^{(1)}[h+\partial\xi+\partial\xi]=\bar G^{(1)}[h]\ \text{holds as an exact coefficient identity (every third-derivative-of-}\xi\ \text{term cancels; none survives), and}\ \mathrm{CT1.18}\text{'s own Rmk correction is re-certified: the traceless-PROJECTED transformation shifts}\ \bar G^{(1)}\ \text{by exactly}\ \tfrac12(\partial_\mu\partial_\nu-\eta_{\mu\nu}\Box)\partial\!\cdot\!\xi\ne0$$
$$(4)\quad\textbf{THE CONSTRAINT/WAVE SPLIT IS THE BLOCK SPLIT (new):}\qquad\text{census of the second-time-derivative content of}\ \bar G^{(1)}:$$
$$\boxed{\ \text{exactly}\ 4\ \text{of the}\ 10\ \text{components — the lapse cell}\ g_{00}\ \text{and the three shift cells}\ g_{0i}\ \text{— carry NO}\ \partial_0\partial_0\ \text{term at all, while all six spatial cells}\ g_{ij}\ \text{do}\ }$$
$$\text{attributed through the dictionary}\ [\mathrm{CT1.12a}(2);\ \mathrm{FT.30}]:\ \text{the}\ 4\ \text{constraint cells are}\ D^+\ (a_{00}\to\Omega\to g_{00},\ 1)\ \text{and}\ W\ (w_i\to N_i\to g_{0i},\ 3);\ \text{the}\ 6\ \text{wave cells are}\ G\ (\hat h_{ij},\ 5)\ +\ H\ (\Sigma_{\mathrm{tr}},\ 1);$$
$$\text{this RE-DERIVES}\ \mathrm{AT.5}(4)\text{'s row from the operator side —}\ N_i\ \text{is the Lagrange multiplier of the momentum constraint, fixed by the slicing choice and}\ \neg\text{by dynamics — and it fixes the exact scope of claim 2:}\ \mathrm{CT1.18}\text{'s own hypothesis}\ (\Upsilon=N_i=\Sigma_{\mathrm{tr}}=0)\ \text{switches off}\ D^+,\ W\ \text{and}\ H,\ \text{so the ONE frozen per-block wave equation belongs to the}\ G\ \text{quintet alone}\ [\mathrm{CT1.10}:\ \hat E^{ij}=\text{spin }2;\ \mathrm{CT1.18}\ \mathrm{Phys}:\ \text{``the graviton of the corpus is the}\ \mathcal E_{++}\ \text{quintet … propagating on the auxiliary background''}]$$
$\text{the other three blocks are}\ \neg\text{inert but}\ \neg\text{wave modes in the frozen record:}\ W\ \text{transports (the drag term and the dispersion}\ E=N\sqrt{m^2+p^2}-N^ip_i\ [\mathrm{BM.34}(3),(4)]),\ H\ \text{enters}\ \bar g_{ij}\ \text{as the volume mode}\ [\mathrm{D2.1}],\ D^+\ \text{gravitates through the closed-form conformal law}\ G_{\mu\nu}=\bar G_{\mu\nu}-2\bar\nabla_\mu\bar\nabla_\nu\Upsilon+2\bar g_{\mu\nu}\bar\Box\Upsilon+2\Upsilon_\mu\Upsilon_\nu+\bar g_{\mu\nu}|\bar\nabla\Upsilon|^2\ [\mathrm{CT1.17}:\ \Upsilon=\ln\Omega]$
$\textbf{the convention adversarial (machine):}\qquad\text{re-running the whole census with the flipped signature representative}\ \eta'=(+,+,+,-)\ \text{leaves the split UNCHANGED — the same four constraint cells, the same six wave cells: the}\ \partial_0\partial_0\ \text{census is a structural consequence of the gauge invariance,}\ \neg\text{an artifact of C13's mostly-plus choice}$
$$(5)\quad\textbf{THE LOCALITY-TO-CONTINUUM ROW (new):}\qquad\text{the 1-hop bound is a PREMISE of the bridge theorem,}\ \neg\text{an obstacle to it.}\ \mathrm{CT2.6}\text{'s smoothness step reads: ``coefficients}=\text{local ledger averages;}\ \mathrm{D1.9}:\ \text{updates local, finite; (iii): jumps uniformly bounded}\implies\text{smooth interpolation, deviation}\to0\ \text{with}\ \mathfrak h\text{'';}$$
$$\boxed{\ \text{and its chart row is the sharpest anchor of the whole hypothesis:}\quad x^0:=\tau_n\ [\mathrm{D1.8}],\qquad x^i:=\ \text{HOP COUNTERS projected on the 3 shift directions}\ (W_i\ \text{sector})\ [\mathrm{CT2.6}\ \mathrm{Pf};\ \mathrm{CT1.12}]\ }$$
$$\text{so the tick supplies the time coordinate, the}\ W\ \text{block supplies the three spatial coordinate directions, and the coordinates themselves are hop counts}\ [\mathrm{D0.6}];\qquad\text{hypothesis (ii) supplies the reach: cells contain unboundedly many real edges as}\ \mathfrak h\to0\ [\mathrm{CT2.6}\ \mathrm{Rmk};\ \mathrm{BM.151}(1)]$$
$$(6)\quad\textbf{THE BAR ON THE DYNAMICAL READING (re-run,}\ \neg\text{cited):}\qquad\text{the O1 ground holds by machine: on the extended carrier the weak seed acts}\ \text{seed}\otimes\text{trivial, so}\ [s_i\otimes I_\omega,\ I\otimes P_{L/R}]=0\ \text{exactly for all three generators and both chiral projectors (6 of 6 commutators identically zero, with}\ P_{L,R}\ \text{certified idempotent of trace}\ 1),\ \text{while the same-factor adversarial gives}\ [\sigma_1,\sigma_3]=-2i\sigma_2\ne0\ \text{— blindness,}\ \neg\text{coupling}\ [\mathrm{FT.126}(2)];$$
$$\text{with O2 (deficit}\ 1'\ \text{[}\mathrm{IT.41}(2)])\ \text{and O4 (the}\ \mathrm{D3.7}\ \text{trivial chain carries no winding\ [}\mathrm{IT.40}(4)])\ \text{standing, the dynamical radar/photon-mediated jump remains BARRED as formed}\ [\mathrm{IT.40}\text{--}\mathrm{IT.42};\ \mathrm{IT.53}(8);\ \mathrm{IT.66}(1)]$$
$$(7)\quad\textbf{THE VERDICT ON CLAIM 2 (split):}\qquad\begin{array}{l|l}\textbf{the component}&\textbf{the verdict}\\\hline\text{``not ticks / not ledger updates''}&\textbf{DERIVED}\ [(1);\ \mathrm{A6};\ \mathrm{A7};\ \mathrm{D0.7};\ \mathrm{D1.9};\ \mathrm{CT0.3}]\\\text{``they are geometric''}&\textbf{DERIVED}\ [\mathrm{IT.72}(2);\ \mathrm{CT1.12};\ \mathrm{FT.157}(1)]\ \text{— they ARE the metric's coefficients}\\\text{``geometric PROPAGATORS'' (a wave mode per block)}&\textbf{DERIVED for the}\ G\ \textbf{quintet only}\ [(3),(4);\ \mathrm{CT1.18};\ \mathrm{CT1.10}];\ \text{for}\ W,H,D^+\ \textbf{NOT DERIVED — a scoped absence,}\ \neg\text{a no-go}\ [\mathrm{AT.5}(4);\ \mathrm{CT1.17};\ \mathrm{BM.34}(3),(4)\ \text{give transport/conformal roles,}\ \neg\text{wave operators}]\\\text{``through channels'' (the pair-channel support)}&\textbf{DERIVED}\ [(2);\ \mathrm{IT.76}(1)];\ \text{multi-hop reach is a CHAIN and COARSE-GRAINING property}\ [\mathrm{IT.76}(3)]\\\text{the DYNAMICAL mediation reading}&\textbf{BARRED as formed — three grounds}\ [(6);\ \mathrm{IT.66}(1)]\end{array}$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{barred:}\ (6)\text{'s dynamical reading};\qquad\textbf{the residue consolidates:}\ \text{a formed propagator role for}\ W,H,D^+\ \text{would need the P4 transport profile — the declared gauge field — which is}\ \mathrm{D\text{-}PJ7}\text{'s owed content}\ [\mathrm{IT.41}(2);\ \mathrm{IT.66}(4)];\ \ \boxed{\ \neg\text{a new open row,}\ \neg\text{a declaration issued}\ }$$

**Req.** A1, A2, A3, A6, A7, A8, C11, C13, P1, P5, D0.6, D0.7, D1.5, D1.6, D1.8, D1.9, D1.10, D2.1, D2.4, D2.5, D3.7 (Parts 1–2); CT0.3, CT0.5, CT0.6, CT0.11, CT0.12, CT1.10, CT1.12, CT1.12a(2), CT1.17, CT1.18 (+ Rmk), CT1.23, CT2.5, CT2.6 (+ Pf, Rmk), CT4.2 (Parts 1–2); Def-H.33, FT.30, FT.126(2), FT.157(1), FT.159(4) (Part 3); BM.34(3),(4), BM.151(1) (Part 4); IT.40–IT.42, IT.41(2), IT.53(8), IT.66(1),(4), IT.71(4) (this level); AT.5(4) (Level 5); a formal jet algebra over $\mathbb Q$ (symmetric partials), exact coefficient comparison, exhaustive integer censuses, exact $4\times4$ $\mathbb Q(i)$ commutators [math; machine: `translation_layer.py` §§C1–C8, 8/8].

**Pf.**
$$(1):\ \ \text{the}\ 1024\text{-history census (monotonicity, strictness at emission, the reversed record)}\ [\text{machine C1}];\ \ \text{the clause witnesses for}\ \neg\exists\tau^{-1},\ U\notin\mathfrak L,\ \mathrm{D1.6},\ \mathrm{D1.8}\ [\text{machine C1}];$$
$$(2):\ \ \text{the tiling}\ 3{+}3{+}5{+}3{+}1{+}1=16=C_{\mathrm{cap}},\ D_{\mathrm{tick}}(n)=2^{n+1},\ O(n)=\max(0,2^{n+1}-16)=(0,0,0,0,16,48,112)\ \text{at}\ n=0..6,\ \text{admissible}\iff n\le3,\ D_{\mathrm{tick}}(3)=C_{\mathrm{cap}}\ [\text{machine C4}];$$
$$(3):\ \ \text{two independent expansions of}\ \bar G^{(1)}\ \text{in the jet basis compared coefficient-wise; the}\ T/V\ \text{structure identity; the gauge substitution with the}\ \xi\text{-part collected to zero; the projected residual compared to the canon's stated form}\ [\text{machine C5}];$$
$$(4):\ \ \text{the}\ \partial_0\partial_0\ \text{coefficient census per component: zero on}\ (0,0),(0,1),(0,2),(0,3),\ \text{nonzero on all six}\ (i,j)\ [\text{machine C6}];\qquad(5):\ \ \text{the text census of}\ \mathrm{CT2.6}\text{'s Pf with live and dead witnesses}\ [\text{machine C7}];$$
$$(6):\ \ \text{the six commutators in}\ 4\times4\ \mathbb Q(i)\ \text{and the same-factor adversarial}\ [\text{machine C8}];\qquad(7),(8):\ \ \text{the verdict assembly on the certified markers}.\ \blacksquare$$

**Phys.** The second claim is the one that had to be cut open. Its first half is exactly right:
the tick is a Haar draw and a ledger update, its draws are not even retained, it has no inverse,
and the metric appears in no tick clause — the tick reaches the geometry only as the increment
$\Delta x^0$ that the force coefficients contract with. Its second half is right about being
geometric and wrong about being uniform: rebuilt in a formal jet algebra, the linearized Einstein
tensor splits ten components into four that carry no second time derivative at all and six that
do, and those four are precisely the conformal cell and the three shift cells. Lapse and shift are
constraint cells — the corpus already knew it for the shift and called it a Lagrange multiplier —
and the only wave equation the frozen record derives is the quintet's, obtained by switching the
other three blocks off. So one block propagates as a wave, three gravitate in other registers, and
the honest verdict is a split with a scoped absence rather than a no-go. The consolation is the
prettiest row in the tier: the bridge theorem's own chart reads the time coordinate as the tick
and the three spatial coordinates as hop counters projected along the shift, so the one-hop
locality the Architect noted is not a limitation on the layer but an input to it.

---

### IT.74 — Claim 3 adjudicated: the shift is $T$-odd, it separates the two legs, and the arrow lives in the ledger

**Thm.**
$$(1)\quad\textbf{THE}\ T\textbf{-PARITY (derived, and sharpened):}\qquad T(W_i)=-W_i\ \text{from}\ \mathrm{A3}\text{'s}\ T(\sigma_\mu\otimes\sigma_\nu)=\eta^\mu\eta^\nu(\sigma_\mu\otimes\sigma_\nu)\ \text{with}\ \eta=(-,+,+,+)\ [\mathrm{C13}]\ \text{through the exact Pauli-tensor decomposition}\ [\mathrm{CT1.2}\ \text{table}:\ W_i\in\mathcal E_{+-}];$$
$$\textbf{the precision row}\ [\mathrm{IT.71}(4)(\mathrm{P2})]:\qquad T\text{-odd}=6=\{W_i\ (3)\}\cup\{K_i\ (3)\},\qquad T\text{-even}=10=\{E_0,\Sigma,\hat E^{ij}\ (5),J_i\ (3)\};$$
$$\boxed{\ \text{within the}\ 10\ \text{metric-carrying generators the unique}\ T\text{-odd sub-block is}\ W\ (3\ \text{of}\ 10);\ \ \text{within the}\ 6\ \text{zero-coordinate generators it is}\ K=J^-\ (3\ \text{of}\ 6)\ }\qquad[\mathrm{FT.156}(2):\ \text{the}\ 7/3\ T\text{-split of the}\ S\text{-even block}]$$
$$(2)\quad\textbf{THE TRANSPORT (derived; machine, all 16 cells):}\qquad\text{with}\ J=\operatorname{diag}(-1,1,1,1)\ \text{and the}\ T\text{-action on sector data}\ (a_{00},q,w)\mapsto(a_{00},q,-w):$$
$$\bar g_{\mu\nu}(a_{00},q,-w)=J^{\rho}{}_{\mu}\,\bar g_{\rho\sigma}(a_{00},q,w)\,J^{\sigma}{}_{\nu}\quad\text{as an exact polynomial identity};\qquad g_{00},\ g_{ij}\ \text{fixed},\quad g_{0i}\mapsto-g_{0i}\quad[\mathrm{FT.156}(3);\ \mathrm{FT.159}(3)]$$
$$\text{the signature is reversal-invariant:}\ \operatorname{sig}\bar g(w)=\operatorname{sig}\bar g(-w)=(-,+,+,+)\ \text{on an 8-point exact rational}\ \mathrm{LDL}^\top\ \text{witness lattice (4 pairs}\ (q,w)\times\text{both shift signs); the flip tilts the cone, it never re-signs it}\ [\mathrm{IT.53}(5)(\mathrm b)]$$
$$(3)\quad\textbf{THE CARRIER}\ T\textbf{-PARITY (derived; the exact reason):}\qquad w\mapsto-w\implies N_i\mapsto-N_i,\quad N^i=\gamma^{ij}N_j\mapsto-N^i,\quad(N,\gamma_{ij})\ \text{fixed}\quad[\mathrm{BM.34}(3)];$$
$$\boxed{\ \det\gamma\,\bigl(N^2-\Omega^2\bigr)=\Omega^8\varkappa^2\beta^2\,\bigl(w^{\top}\!\operatorname{adj}(\delta+\varkappa q)\,w\bigr)\ }\qquad\text{machine-exact: the right-hand side is homogeneous of degree}\ 2\ \text{in}\ w\ \text{with}\ q\text{-only coefficients, so}\ N^2\ \text{is EVEN in}\ w\ \text{and the flip cannot move it};$$
$$\text{hence}\ p_i\ \text{is}\ T\text{-odd, matching its carrier}\ [\mathrm{BM.34}(3)],\ \text{and the dispersion}\ E=N\sqrt{m^2+p^2}-N^ip_i\ \text{is}\ T\text{-EVEN under}\ (N^i,p_i)\mapsto(-N^i,-p_i)\ [\mathrm{BM.34}(4)]$$
$$(4)\quad\textbf{THE LINE ELEMENT IS}\ T\textbf{-EVEN (new):}\qquad\text{so the shift's}\ T\text{-oddness does NOT make the geometry}\ T\text{-odd. Monomial census of}\ \widehat{ds}^{\,2}(e)=\Omega^2[-(\Delta x^0)^2+2\varkappa\beta\,\Delta x^0(w\!\cdot\!\Delta x)+M_{ij}\Delta x^i\Delta x^j],\ M=\delta+\varkappa q:$$
$$\text{exactly}\ 10\ \text{increment monomials —}\ 1\ \text{of}\ (\Delta x^0)^2,\ 3\ \text{of}\ \Delta x^0\Delta x^i,\ 6\ \text{of}\ \Delta x^i\Delta x^j\ \text{— one per metric coordinate, against the cells}\ g_{00}/g_{0i}/g_{ij};\qquad\text{full sector expansion:}\ 13\ \text{monomials}=(1\ D^+)+(3\ W)+(3\ \text{background}\ \delta_{ij})+(6\ \varkappa q:\ G{+}H);$$
$$\text{the}\ T\text{-parity products:}\ g_{00}\,(T\text{-even})\times(\Delta x^0)^2\,(T\text{-odd squared})=T\text{-even};\quad g_{0i}\,(T\text{-odd})\times\Delta x^0\,(T\text{-odd})\times\Delta x^i\,(T\text{-even})=T\text{-even};\quad g_{ij}\,(T\text{-even})\times\Delta x^i\Delta x^j\,(T\text{-even})=T\text{-even};$$
$$\boxed{\ \text{every monomial}\ T\text{-even, as}\ \mathrm{CT1.12a}(2)\text{'s consequence requires}\ }\qquad\text{two exact polynomial identities:}\ \Delta x\mapsto-\Delta x\ \text{fixes}\ \widehat{ds}^{\,2}\ [\mathrm{CT1.19b}(2)],\ \text{and the}\ T\text{-pullback}\ (\Delta x^0\mapsto-\Delta x^0\ \text{with}\ w\mapsto-w)\ \text{fixes it too};\qquad\text{the flat/drag split re-certifies: the drag is odd in}\ w,\ \text{the flat part even}\ [\mathrm{AT.5}(1)\ \text{pattern}]$$
$$(5)\quad\textbf{THE READ-LEVEL DISCRIMINATOR (derived):}\qquad\text{the shift's sign separates the two null legs of the radar round trip}\ [\mathrm{IT.53}(4),(5)(\mathrm b);\ \mathrm{IT.68}(2)]:\quad d\tau_\pm=\sqrt{G}\,dx/(N\mp s),\quad s=\sqrt G\,N^x;$$
$$\text{on the frozen witness}\ (G,dx,N,s)=(4,3,5,2)\ \text{with}\ \sqrt G=2\ \text{exact}:\quad d\tau_+=2,\quad d\tau_-=\tfrac67,\quad d\tau_+-d\tau_-=\tfrac87=\frac{2\sqrt G\,dx\,s}{N^2-s^2}=\tfrac{24}{21};$$
$$\boxed{\ s\mapsto-s\ \text{SWAPS the two legs}\ (d\tau_+\leftrightarrow d\tau_-):\ \text{the two synchronizations are}\ T\text{-conjugate reads}\ [\mathrm{BM.34}(3);\ \mathrm{FT.156}(3)]\ }\qquad\text{the half-distance equals the proper length exactly at}\ s=0,\ \text{and agreement}\iff s\cdot dx=0\ \text{in both directions}$$
$$(6)\quad\textbf{WHERE THE ARROW ACTUALLY LIVES (derived; the claim's over-read):}\qquad\text{the spatial triad reversals ARE inner unitaries — machine, entrywise: the cyclic}\ U=E_0-\tfrac12\mathcal W^2-\tfrac{\mathrm i}2\mathcal W\ (\mathcal W=W_1{+}W_2{+}W_3,\ \mathcal W^3=3\mathcal W)\ \text{satisfies}\ U^3=E_0\ \text{and}\ UX_iU^\dagger=X_{i+1}\ \text{on all}\ 9\ \text{rows}\ (X\in\{W,J,K\}),\ \text{and the three transpositions}\ U_{ij}=E_0-(W_i{+}W_j)^2\ \text{satisfy}\ U_{ij}^2=E_0\ \text{and realize}\ X_i\leftrightarrow X_j,\ X_k\mapsto-X_k\ \text{on all}\ 27\ \text{rows}\ [\mathrm{FT.156}(4);\ \mathrm{FT.158}(1)];$$
$$\text{the TEMPORAL advance has no implementation:}\ \neg\exists\,\tau^{-1}\ [\mathrm{A6}],\ \text{the record is monotone and strictly increasing at every crystallization}\ (1),\ \text{the pure order reversal of every completed history is inadmissible at its first event}\ [\mathrm{FT.144}(2),(4)(\mathrm{ii})],\ \text{and}\ \Theta_{\mathfrak L}\ [\mathrm{D2.7}]\ \text{is ``the formal mirror on records,}\ \neg\text{a dynamical inverse''}\ [\mathrm{FT.144}(4)(\mathrm i);\ \mathrm{FT.159}(5)];$$
$$\textbf{the arrow combinatorics, with a new closed form:}\qquad\text{single pair: exactly one admissible history at every length}\ 0..8\ \text{and one completed history}\ (J^+J^-)^m\ \text{at every even length (exhaustive);}\qquad\text{two pairs, total length}\ 2n:$$
$$\boxed{\ \#\{\text{completed interleavings}\}=\sum_{m_0+m_1=n}\frac{(2n)!}{(2m_0)!\,(2m_1)!}=\sum_{m}\binom{2n}{2m}=2^{\,2n-1}\ }\qquad\text{the frozen witnesses}\ 2,\ 8,\ 32\ \text{at}\ 2n=2,4,6\ [\mathrm{FT.144}(2)]\ \text{re-derived by brute force, extended to}\ 2n=8:\ 128$$
$$(7)\quad\textbf{THE NAMING BAR:}\qquad\boxed{\ \text{``encodes left/right'' is BARRED as a naming: ``naming either branch}\ \textit{left}\ \text{or}\ \textit{right}\ \text{is barred''}\ [\mathrm{FT.157}\ \mathrm{Rmk};\ \mathrm{FT.156}\ \mathrm{Rmk};\ \mathrm{FT.101}\ \mathrm{Phys}\ \text{bars stand}]\ }\qquad\text{the labels spatial/temporal branch are internal bookkeeping for the derived dimension and Casimir matches, naming no particle and no external structure}$$
$$(8)\quad\textbf{THE VERDICT ON CLAIM 3 (split):}\qquad\begin{array}{l|l}\textbf{the component}&\textbf{the verdict}\\\hline W_i\ \text{is}\ T\text{-odd}&\textbf{DERIVED}\ [(1);\ \mathrm{CT1.2};\ \mathrm{FT.156}(2),(3);\ \mathrm{BM.34}(3)]\ \text{— with the precision row:}\ T\text{-oddness alone picks out}\ W\oplus K,\ \text{so the distinctive statement is ``the unique}\ T\text{-odd sub-block OF THE METRIC SECTOR''}\\\text{it transports to the time-reversal pullback}&\textbf{DERIVED}\ [(2),(3);\ \mathrm{FT.156}(3);\ \mathrm{FT.159}(3)]\\\text{it distinguishes the two null legs}&\textbf{DERIVED}\ [(5);\ \mathrm{IT.53}(5)(\mathrm b);\ \mathrm{IT.68}(2)]\ \text{— a discriminator at the read level}\\\text{it distinguishes PAST from FUTURE}&\textbf{DERIVED ONLY IN THE FORMAL/READ SENSE}\ [(4),(6)]:\ \text{the}\ T\text{-flip is an involution on chart and record data and the interval is}\ T\text{-EVEN; the ARROW is}\ \neg\exists\tau^{-1}\ [\mathrm{A6}]+\text{no backward materialization}\ [\mathrm{FT.144}(2),(3)]+\text{the monotone record}\ [\mathrm{A7}]\ \text{— a different locus}\ [\mathrm{FT.159}(3)\ \text{locus discipline}]\\\text{it encodes LEFT/RIGHT}&\textbf{BARRED as a naming}\ [(7);\ \mathrm{FT.101}\ \mathrm{Phys};\ \mathrm{FT.156}\ \mathrm{Rmk};\ \mathrm{FT.157}\ \mathrm{Rmk}]\end{array}$$

**Req.** A3, A6, A7, C13, D1.6, D1.7, D2.1, D2.7 (Parts 1–2); CT1.1, CT1.2, CT1.12, CT1.12a(2), CT1.19b(2) (Parts 1–2); Def-H.33, FT.101 (Phys bars), FT.126, FT.133(1), FT.141(5), FT.144(2),(3),(4), FT.156(2),(3),(4),(5), FT.157(1),(3),(5), FT.158(1), FT.159(3),(5) (Part 3); BM.34(1),(3),(4) (Part 4); IT.53(4),(5), IT.68(2), IT.71(4) (this level); AT.5(1),(4) (Level 5); exact multivariate Fraction polynomial identities, exact rational $\mathrm{LDL}^\top$ inertia, exact adjugate calculus, exhaustive word enumeration, exact binomials, exact $\mathbb Q(i)$ conjugation tables [math; machine: `translation_layer.py` §§D1–D7, C2, 7/7].

**Pf.**
$$(1):\ \ \text{the}\ T\text{-action applied through the exact Pauli-tensor coordinates of each generator, census}\ 10/6\ \text{and per-block}\ [\text{machine A3, A4}];\qquad(2):\ \ \text{the}\ 16\text{-cell polynomial identity and the full-metric consequence}\ [\text{machine D1}];\ \ \text{the inertia lattice}\ [\text{machine D3}];$$
$$(3):\ \ \text{the carrier flips on all witnesses and the adjugate identity}\ \det\gamma(N^2-\Omega^2)=\Omega^8\varkappa^2\beta^2(w^{\top}\!\operatorname{adj}M\,w)\ \text{from}\ \gamma=\Omega^2M,\ \gamma^{-1}=\Omega^{-2}M^{-1},\ N_i=\Omega^2\varkappa\beta w_i\ [\text{machine D2}];$$
$$(4):\ \ \text{the monomial census by increment-multidegree and by block, the parity products, and the two substitution identities}\ [\text{machine D4}];\qquad(5):\ \ \text{the exact Fraction leg arithmetic, the flip, the}\ s=0\ \text{substitution and the agreement locus both directions}\ [\text{machine D5}];$$
$$(6):\ \ \text{the}\ 9+27+3\ \text{conjugation and involution rows entrywise over}\ \mathbb Q(i);\ \ \text{the exhaustive single-pair and two-pair enumerations with the closed forms}\ \sum_m\binom{2n}{2m}=2^{2n-1}\ [\text{machine D6, C2}];\qquad(7),(8):\ \ \text{the bar censuses with dead controls and the verdict assembly}\ [\text{machine D7}].\ \blacksquare$$

**Phys.** The third claim is true at its core and wrong at its edge. The shift really is the
T-odd part of the metric: flip the sign of $w$ and the geometry answers with the exact
time-reversal pullback, the lapse and the spatial metric untouched, the three cross components
reversed, the signature intact — and the reason the lapse survives is an exact adjugate identity
that makes $N^2$ even in $w$. But T-oddness is a grading, not an arrow. The interval built from
it is T-even monomial by monomial, the flip is an involution on charts and records, and the
corpus locates the asymmetry somewhere else entirely: in a tick that has no inverse, in seals
whose domains forbid a history that begins by dissolving, and in a record that only grows — a
count this tier extends to a closed form, $2^{2n-1}$ interleavings of two completed pairs, the
frozen witnesses 2, 8, 32 falling out at $n=1,2,3$. What the shift genuinely discriminates is
the two legs of a radar round trip, swapping them under its own sign. And the name the directive
reached for is the one name the record refuses: left and right stay barred, the spatial and
temporal labels stay bookkeeping.

---

### IT.75 — Claim 4 adjudicated: the joint $S$-even read, the on-shell integers, and the translation that runs backwards

**Thm.**
$$(1)\quad\textbf{THE CONTRACTION IS THE MEASUREMENT (derived):}\qquad\text{all four blocks enter the interval, and the ten increment monomials are in bijection with the ten metric coordinates}\ [\mathrm{IT.74}(4)]:$$
$$\widehat{ds}^{\,2}(e)=g_{\mu\nu}(e)\Delta x^\mu_e\Delta x^\nu_e/\mathfrak h^2\ [\mathrm{D1.6}];\qquad\text{exact partial-derivative census at a rational witness:}\ \partial\widehat{ds}^{\,2}/\partial c\ne0\ \text{for ALL TEN coordinates}\ c\in\{\Omega^2\ (D^+);\ w_1,w_2,w_3\ (W);\ q_{11},q_{22},q_{33},q_{12},q_{13},q_{23}\ (G{+}H)\}$$
$$\boxed{\ \text{and the converse: keeping ONE block nonzero and zeroing the others gives a non-integral interval for every block, so NO pair-channel block carries a block-local quantum}\ [\mathrm{FT.30}\ \mathrm{Verdict}:\ \text{``the geometric quantum is a}\ \textit{joint}\ S\text{-even read …}\ \widehat{ds}^{\,2}(e)\ \text{mixes all ten metric coordinates across}\ G,H,D^+,W\text{''}]\ }$$
$$(2)\quad\textbf{THE FROZEN FORMULA OF THE TRANSLATION (derived, and edge-local):}\qquad\boxed{\ G(e)=\sigma_e\,\exp\!\bigl(\mathrm i\,\alpha_e\,\widehat{ds}^{\,2}(e)\bigr)\ }\quad[\mathrm{D3.5};\ \mathrm{EM.20}(4)]$$
$$\text{one LEDGER BIT}\ \sigma_e\in\{+1,-1\}\ [\mathrm{CT0.9};\ \mathrm{D0.5}]\ \text{times one GEOMETRIC PHASE whose exponent is the ledger's binary phase}\ \alpha_e\in\{0,\pi\}\ [\mathrm{EM.20}(1)]\ \text{times the rung-1 interval of}\ (1);\ \ \text{dimensionless, defined PER EDGE, and}\ \mathrm{A8}\text{'s weight is the product over edges:}\ w(C)=\mathcal J(C)\prod_{e\in E(C)}G(e)\cdot(-1)^{\aleph(\sigma,C)};$$
$$\text{machine census over every chain of length}\ 1..4\ \text{with all sign, phase and interval assignments (22620 chains):}\quad\prod_eG(e)=(\prod_e\sigma_e)\cdot(-1)^{\Theta_{\mathcal P}},\qquad\Theta_{\mathcal P}=\!\!\sum_{e\in\mathcal P(c)}\!\!\widehat{ds}^{\,2}(e)\quad[\mathrm{D1.7};\ \mathrm{CT1.19b}(1);\ \text{exact fourth-root arithmetic}]$$
$$(3)\quad\textbf{THE ON-SHELL INTEGERS (derived):}\qquad\operatorname{Hol}_{\mathrm{spiral}}(c)=e^{\mathrm i\Phi(c)}=+1\ \text{with}\ \Phi=\pi\Theta_{\mathcal P}\implies\Theta_{\mathcal P}\in2\mathbb Z\ [\mathrm{CT1.19b}(1)];\qquad\text{census}\ \Theta_{\mathcal P}=0..16:\ e^{\mathrm i\pi m}=(-1)^m,\ +1\ \text{exactly on the even}\ m;$$
$$\text{the 2-cycle geometry quantum}\ [\mathrm{CT1.19b}(3)]:\qquad\Theta_{\mathcal P}=m\kappa\in2\mathbb Z,\ m=|\mathcal P(c)|\in\{0,1,2\}\implies m=2:\ \kappa\in\mathbb Z\ (\text{all integers, no half-integer});\quad m=1:\ \kappa\in2\mathbb Z;\quad m=0:\ \text{vacuous};$$
$$ds^2(e)=\kappa\,\mathfrak h^2,\qquad\mathfrak h^2=4G_N\ln2\ [\mathrm{CT2.9}]\implies ds^2(e)=4\kappa\,G_N\ln2\quad[\mathrm{CT1.29}:\ \text{one Bekenstein bit-area per unit}\ \kappa];\qquad\boxed{\ \text{the coefficients}\ 4\kappa\ \text{are kept as exact Laurent monomials — NO VALUE issued}\ [\mathrm{P5}]\ }$$
$$\text{partial internal sums keep free parity: a single}\ \kappa=1\ \text{antialigned edge gives}\ (-1)^1=-1\ [\mathrm{CT1.19b}(4)]$$
$$(4)\quad\textbf{THE INVERSE TRANSLATION (derived; the measurement runs backwards):}\qquad\boxed{\ (w\!\cdot\!\Delta x)(e)=\frac{\mathfrak h^2\kappa_e/\Omega^2+(\Delta x^0)^2-M_{ij}\Delta x^i\Delta x^j}{2\varkappa\beta\,\Delta x^0}\ }\quad[\mathrm{AT.5}(1)]$$
$$\text{machine: exact, round-tripping identically into}\ \mathrm{D1.6}\ \text{on every witness, and LINEAR in the ledger integer}\ \kappa_e\ (\text{the first difference is a nonzero constant, the second vanishes over}\ \kappa=0..6);\qquad\text{its inputs are ledger and metric data only}\ [\mathrm{AT.5}(2)],\ \text{with the}\ \mathrm{P4}\ \text{pair}\ (\varkappa,\beta)\ \text{UNISSUED};$$
$$\text{the residue is exactly}\ 2\ \text{dimensions per edge}\ (\dot w_\perp\!\cdot\!\Delta x=0\ \text{is ONE exact linear condition on three unknowns, nullity}\ 2)\ \text{and is GAUGE,}\ \neg\text{missing data}\ [\mathrm{AT.5}(3),(4)];\qquad\text{the vanishing locus is codimension}\ 1:\ \text{exactly one}\ \kappa\ \text{solves}\ (w\!\cdot\!\Delta x)=0\ [\mathrm{AT.5}(5)]$$
$$(5)\quad\textbf{WHICH SIDE QUANTIZES (new):}\qquad\boxed{\ \text{the geometry supplies the quadratic form; the discreteness is the LEDGER's; the integers are their ON-SHELL contraction}\ }$$
$$\text{machine witness pair: at the flat vacuum}\ (a_{00},q,w)=0,\ \Omega=1\ [\mathrm{BM.34}(2)]\ \text{the interval is still the continuous form}\ \eta_{\mu\nu}\Delta x^\mu\Delta x^\nu,\ \text{and}\ \Delta x=(1,\tfrac12,0,0)\ \text{gives}\ \widehat{ds}^{\,2}=-\tfrac34\notin\mathbb Z\ \text{— off shell nothing is quantized}\ [\mathrm{CT1.19a};\ \mathrm{Def\text{-}H.18}\text{'s two-locus principle: discreteness claims are SPECTRUM claims, continuity claims are ARENA claims}];$$
$$\text{on shell the integers come from the ledger's binary alphabet}\ \alpha_e\in\{0,\pi\}\ [\mathrm{EM.20}(1);\ \mathrm{CT0.9}]\ \text{conjoined with the materialization/pole condition}\ [\mathrm{CT2.5};\ \mathrm{D2.4};\ \mathrm{D2.5}]\ \text{— which is why}\ \mathrm{CT1.12a}(3)\ \text{can say of every dictionary/aspect datum that ``neither carries an independent quantum''}$$
$$(6)\quad\textbf{THE THREE ``DELTA'' READINGS}\ [\mathrm{IT.71}(4)(\mathrm{P4})]:\qquad\begin{array}{l|l}\textbf{the reading}&\textbf{the adjudication}\\\hline\delta h\ \text{the hop count}&\textbf{DERIVED as a face, DECLARED as an exchange rate}: d=\delta h\in\mathbb N\ \text{is the derived hop face}\ [\mathrm{D0.6};\ \mathrm{EM.7};\ \mathrm{IT.53}(4)],\ \text{frozen by}\ \mathrm{D\text{-}RS3}\ @\ \mathrm{IT.65}\ (\Delta\tau_{\mathrm{rt}}=2\delta h;\ \text{the per-visit half barred on three grounds});\ \text{the formed family re-run here: all}\ 32\times5=160\ \text{cells integral with}\ \tau_e<\tau_r\ [\mathrm{IT.68}(1)]\\\text{the}\ \delta\text{-seal / digon}&\textbf{DERIVED at}\ \mathrm{IT.69}:\ \text{the}\ \delta\text{-glue is the same frozen open bidirectional connector;}\ E_{\mathrm{int}}=+2\ \text{per}\ \delta\ \text{block}\ [\mathrm{FT.44}(4)],\ d=0,\ \varepsilon=+1\ \text{unflipped}\\\Delta\ \text{the ledger increment}&\textbf{DERIVED}:\ (\Delta n_{\mathcal R},\delta h,\delta\tau)=\pm(1,1,1)\ \text{per Janus move}\ [\mathrm{CT0.3}],\ \ \Delta S=\mathsf E_{\mathrm{bd}}+\mathsf E_{\mathrm{tr}}\ [\mathrm{D1.5}]\end{array}$$
$$(7)\quad\textbf{THE PER-ASPECT OBSERVABILITY IS NOT UNIFORM (derived census):}\qquad[\mathrm{FT.20}]:\quad G\ \text{observable through the mass read}\ I_{\mathrm{hid}}(\Sigma;o)\ (\text{observer-relative,}\ \mathrm{Def\text{-}H.9});\quad W\ \text{through}\ \Theta_{\mathrm{int}}\ne0,\ \textbf{ONE-DIRECTIONAL only};\quad H\ \textbf{FOLDED INTO}\ G\ [\mathrm{Def\text{-}H.36}];\quad D^+\ \textbf{NEVER independently}\ (\text{uniform},\ \mathrm{D4.3});\quad J^\pm\ \textbf{never}\ (\text{seals},\ \neg\text{charges})$$
$$(8)\quad\textbf{THE VERDICT ON CLAIM 4 (three layers, three verdicts):}\qquad\begin{array}{l|l}\textbf{the layer}&\textbf{the verdict}\\\hline\text{the CAPABILITY (the contraction measures the ledger)}&\textbf{DERIVED}\ [(1)\text{--}(5);\ \mathrm{D1.6};\ \mathrm{D1.7};\ \mathrm{D3.5};\ \mathrm{CT1.19b};\ \mathrm{AT.5}(1)]\ \text{— definitional, with an exact closed form that is linear in the ledger integer}\\\text{the PER-BLOCK version}&\textbf{BARRED}\ [(1);\ \mathrm{FT.30}\ \mathrm{Verdict}:\ \neg\text{a block-local quantum}];\ \ \text{and non-uniform where it exists}\ [(7);\ \mathrm{FT.20}]\\\text{the OPERATIONAL read (the radar)}&\textbf{DECLARED, and formed}\ [\mathrm{D\text{-}RS6}\ @\ \mathrm{IT.66}(1);\ \mathrm{D\text{-}RS3}\ @\ \mathrm{IT.65};\ \mathrm{D\text{-}RS1}/\mathrm{D\text{-}RS2}\ @\ \mathrm{IT.56};\ \text{the family formed at}\ \mathrm{IT.68}];\ \ \mathrm{D\text{-}RS4}\ \text{stays DEFERRED}\\\text{the DYNAMICAL version (a photon-mediated jump)}&\textbf{BARRED as formed — three grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{IT.40}\text{--}\mathrm{IT.42};\ \mathrm{IT.66}(1);\ \mathrm{IT.73}(6)\ \text{re-run}]\end{array}$$

**Req.** P1, P5, A8, D0.5, D0.6, D1.5, D1.6, D1.7, D2.4, D2.5, D2.9, D3.5, D4.3 (Parts 1–2); CT0.9, CT1.12a(3), CT1.19a, CT1.19b(1),(3),(4), CT1.29, CT2.5, CT2.9, EM.5, EM.7, EM.20(1),(4), Def-EM.21 (Part 2); Def-H.9, Def-H.18, Def-H.36, FT.20, FT.22, FT.24, FT.30 (+ Verdict), FT.44(4) (Parts 3, Census); BM.34(2), BM.134(5) (Part 4); IT.4(2), IT.40–IT.42, IT.53(4),(5),(8), IT.56, IT.65, IT.66(1),(2), IT.68(1), IT.69, IT.71(4), IT.74(4) (this level); AT.5(1),(2),(3),(4),(5) (Level 5); exact Gauss(i) chain products, exact partial derivatives, exact Fraction round-trips and difference censuses, exact Laurent monomials, exhaustive parity censuses [math; machine: `translation_layer.py` §§E1–E6, 6/6].

**Pf.**
$$(1):\ \ \text{the ten exact partial derivatives at a rational witness and the three per-block non-integer witnesses}\ [\text{machine E1}];\qquad(2):\ \ \text{the}\ 22620\text{-chain product census in exact fourth-root arithmetic against}\ (\prod\sigma_e)(-1)^{\Theta_{\mathcal P}},\ \text{with the phase-alphabet table}\ e^{\mathrm i\alpha\kappa}\in\{1,(-1)^\kappa\}\ [\text{machine E2}];$$
$$(3):\ \ \text{the parity census}\ e^{\mathrm i\pi m}=(-1)^m\ \text{over}\ m=0..16;\ \ \text{the}\ (m,\kappa)\ \text{admissibility census over}\ m\in\{0,1,2\},\ \kappa\in\tfrac12\mathbb Z_{\ge0};\ \ \text{the Laurent coefficients}\ 4\kappa\ [\text{machine E3}];$$
$$(4):\ \ \text{the closed form evaluated and substituted back into}\ \mathrm{D1.6}\ \text{on all witnesses; the first/second difference census; the}\ 1\times3\ \text{constraint rank giving nullity}\ 2;\ \text{the unique zero of the numerator}\ [\text{machine E4}];$$
$$(5):\ \ \text{the off-shell witness}\ -\tfrac34\ \text{and the on-shell integrality, with the two-locus and no-independent-quantum clauses located in the frozen text}\ [\text{machine E5}];\qquad(6)\text{--}(8):\ \ \text{the}\ 160\text{-cell radar census re-run, the observability table census, and the verdict assembly}\ [\text{machine E6}].\ \blacksquare$$

**Phys.** The fourth claim asked whether the geometry can read the ledger, and the answer is that
the corpus already wrote the formula down: one edge weight, one ledger bit times one geometric
phase, whose exponent is the ledger's own binary phase multiplied by an interval built from all
ten metric coordinates at once. That is the translation in a single line, it is edge-local, and
the configuration weight is its product over edges — so the geometry never reaches past the edge
it is evaluated on. The integers come later and come from both sides: off shell the interval is
as continuous as its inputs, and quantization is what the pole condition does to a binary
alphabet, exactly as the two-locus principle says it must. The read runs backwards too — the
shift's longitudinal projection is a closed form linear in the ledger's own integer, with two
gauge dimensions per edge left over by design, not by defect. What the claim cannot have is a
per-block version: no single block carries a quantum, the four blocks are read jointly, and even
the joint read is not uniform in its observability. The operational layer needed a name and got
one two tiers ago; the dynamical layer needs a gauge field and still does not have one.

---

### IT.76 — The 1-reach theorem: range one hop, content the entire $S$ sector, and the two sides of the layer

**Thm.**
$$(1)\quad\textbf{REACH}=1\ \textbf{HOP (derived; the Architect's note, certified):}\qquad\text{every rung-1 aspect's carrier space is the pair channel}\ \mathfrak H(\mathcal H_p\otimes\mathcal H_q)\ \text{that}\ \mathrm{A1}\ \text{attaches to ONE pair and}\ \mathrm{A2}\ \text{prices at}\ 1\,\mathfrak q;\ \ \mathrm{CT0.12}\ \text{tiles that single}\ 16\text{-dimensional space with all six aspects};\ \ \mathrm{D0.6}\ \text{defines a hop as one traversal of one}\ e\in E_{\mathcal R};\ \ \text{and the metric is evaluated PER EDGE,}\ g_{\mu\nu}(e)\ [\mathrm{D1.6}]:$$
$$\boxed{\ \text{a single force insertion reaches exactly one hop:}\ \ \mathrm{D1.9}\ \text{bars any read at edge-distance}>1,\ \text{and the census is non-vacuous — of}\ 66\ \text{vertex-instances on the path, cycle and star graphs (4..7 vertices),}\ 62\ \text{have a nonempty excluded complement at edge-distance}\ge2\ \text{and the}\ 4\ \text{star centres saturate the whole edge set}\ }$$
$$\neg\exists\ \text{a frozen row in which an aspect acts on two pair channels at once}\ [\text{inventory scan}];\qquad\text{the digon floor}\ \Sigma_{\min}\ [\mathrm{FT.28}]\ \text{already sits at the ceiling (2 vertices, 2 edges, both incident to both)}$$
$$(2)\quad\textbf{CONTENT}=\textbf{THE ENTIRE}\ S\ \textbf{SECTOR, MINIMALLY (derived; exhaustive):}\qquad5+3+1+1=10=\dim(S\text{-even})=\#\{g_{\mu\nu}=g_{\nu\mu}\}\ \text{with the six seals making up the other}\ 6\ \text{of the}\ 16\ [\mathrm{CT0.12};\ \mathrm{FT.141}(1);\ \mathrm{CT1.12a}(1)]:$$
$$\boxed{\ \text{exhaustive census over all}\ 2^4=16\ \text{sub-collections of}\ \{G,W,H,D^+\}:\ \text{the largest PROPER sub-collection reaches}\ 9<10\ (G{+}W{+}H),\ \text{and EXACTLY ONE covers the ten — the full four}\ }$$
$$\text{so one pair channel — one hop — carries the WHOLE metric content at once, all four blocks are needed, none is redundant, and the mediation is simultaneous rather than sequential}$$
$$(3)\quad\textbf{THE RANGE/CONTENT SEPARATION (derived):}\qquad\text{one hop is a FORCE property; multi-hop reach is a CHAIN and a COARSE-GRAINING property, and the record never mixes them}:$$
$$(\mathrm i)\ \ \text{chains:}\ c=(e_1,\dots,e_k),\ t(e_i)=s(e_{i+1})\ [\mathrm{D1.4}];\qquad\text{transit}=\text{a propagating OPEN chain, the bosonic content}\ [\mathrm{D1.5}];\qquad\text{the corpus's own long-range carriers are the trivial chains (photon, gluon) with every edge null:}\ \Theta(\gamma)=\sum_e0=0,\ \operatorname{Hol}=1\ \text{at every length (census}\ 1..8)\ [\mathrm{EM.5};\ \mathrm{D1.7};\ \mathrm{D3.7}];$$
$$(\mathrm{ii})\ \ \text{through ONE channel the register bound is}\ \delta h\le4\,\delta\tau,\ \text{sharp at equality}\ [\mathrm{Cor}\ \mathrm{CT0.6a};\ \mathrm{CT0.6}];\qquad(\mathrm{iii})\ \ \text{the continuum is reached by AVERAGING, not by extending a force: hypothesis (ii) of}\ \mathrm{CT2.6}\ \text{requires cells with unboundedly many real edges as}\ \mathfrak h\to0,\ \text{derived from the ledger's own ladder}\ [\mathrm{CT2.6}\ \mathrm{Rmk};\ \mathrm{BM.151}(1),(2)]$$
$$(4)\quad\textbf{THE TWO SIDES OF THE LAYER (new synthesis row):}\qquad\text{the hypothesis, stated in corpus vocabulary and with its two sides separated}:$$
$$\begin{array}{l|l|l}\textbf{the side}&\textbf{the blocks}&\textbf{what it does}\\\hline\text{the ledger side (produces the events)}&S\text{-odd six}=\{J_i,K_i\}=J^+\oplus J^-&\text{the seals}\ n_{\mathcal R}:0\to1\ \text{and}\ 1\to0\ [\mathrm{D1.2}];\ \text{zero metric coordinates}\ [\mathrm{FT.141}(5)];\ \text{the atomic clock}\ (\Delta n_{\mathcal R},\delta h,\delta\tau)=\pm(1,1,1)\ [\mathrm{CT0.3}];\ \neg\text{observable}\ [\mathrm{FT.20}]\\\hline\text{the geometry side (translates them)}&S\text{-even ten}=\{G,W,H,D^+\}&\text{the dictionary}\ [\mathrm{D2.1};\ \mathrm{CT1.12};\ \mathrm{FT.30}];\ \text{the chart}\ (x^0=\tau_n,\ x^i=\text{hop counters on the}\ W\ \text{directions})\ [\mathrm{CT2.6}\ \mathrm{Pf};\ \mathrm{D1.8}];\ \text{the contraction}\ (\widehat{ds}^{\,2},\ \Theta,\ \Phi,\ G(e))\ [\mathrm{D1.6};\ \mathrm{D1.7};\ \mathrm{D3.5}];\ \text{the on-shell integers}\ [\mathrm{CT1.19b}]\end{array}$$
$$\boxed{\ \text{the layer's own mechanism is}\ \mathrm{CT2.6}\text{'s averaging: per-edge (1-hop)}\ S\text{-even data}\ \to\ \text{local ledger averages}\ \to\ \text{smooth}\ (M,g),\ \text{with}\ \mathrm{D1.9}\text{'s locality cited INSIDE the bridge theorem's smoothness step}\ }\qquad[\mathrm{IT.73}(5)]$$
$$\text{and its standing discipline: a dictionary}\ \neg\text{a bridge, partners}\ \neg\text{equals, faces}\ \neg\text{identities}\ [\mathrm{D\text{-}RS2};\ \mathrm{BM.134}(5);\ \mathrm{IT.68}(3);\ \mathrm{IT.52}(3)]$$
$$(5)\quad\textbf{THE SM FLAG (re-stated with its grounds):}\qquad\text{the resemblance the Architect notes — a finite range, and one block mediating a whole sector at once — is recorded as CLARIFICATION ONLY:}\ \neg\text{a range value,}\ \neg\text{a mass,}\ \neg\text{a species and}\ \neg\text{an external comparison enters any clause}\ [\mathrm{P1};\ \mathrm{P5};\ \mathrm{FT.157}\ \mathrm{Rmk};\ \mathrm{FT.158}(5);\ \text{the}\ [\mathrm{EXT}]\ \text{quarantine}\ \mathrm{IT.7}(2);\ \text{the parallel-not-identification discipline}\ \mathrm{BM.134}(5);\ \mathrm{IT.69}(5)];$$
$$\text{the row that survives the flag is a pure SUPPORT statement in counts}\ (1)\text{--}(2):\ \text{range}\ 1\ \text{hop, content}\ 10\ \text{of}\ 16$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(4);\qquad\textbf{flagged}\ \neg\textbf{adopted:}\ (5);\qquad\neg\text{a declaration},\qquad\neg\text{a value},\qquad\neg\text{a new open row}$$

**Req.** P1, P5, A1, A2, A8, D0.6, D0.7, D1.2, D1.4, D1.5, D1.6, D1.7, D1.8, D1.9, D3.5, D3.7 (Parts 1–2); CT0.3, CT0.6, CT0.12, CT0.14, CT1.12, CT1.12a(1),(2), CT2.6 (+ Rmk), Cor CT0.6a (Parts 1–2); FT.20, FT.28, FT.30, FT.141(1),(5), FT.157 (Part 3); BM.134(5), BM.151(1),(2) (Part 4); IT.7(2), IT.52(3), IT.56(2), IT.68(3), IT.69(5), IT.71(3), IT.72(2), IT.73(5), IT.74(4), IT.75(1) (this level); exhaustive subset enumeration, exact integer censuses, exact line-graph/vertex BFS, text censuses with live and dead witnesses [math; machine: `translation_layer.py` §§F1–F4, 4/4].

**Pf.**
$$(1):\ \ \text{the support witnesses}\ (\rho_{pq},\ C(p,q)=1\,\mathfrak q,\ \text{the tiling, the hop definition, the distance bar)}\ \text{with the}\ 66\text{-instance locality census of}\ \mathrm{IT.73}\ [\text{machine F1, C3, C4}];\qquad(2):\ \ \text{the}\ 2^4\ \text{sub-collection census with the covering set unique}\ [\text{machine F2}];$$
$$(3):\ \ \text{the all-null chain census}\ \Theta=0,\ \operatorname{Hol}=1\ \text{at lengths}\ 1..8,\ \text{the}\ \delta h\le4\delta\tau\ \text{cells with their sharp boundary, and the hypothesis-(ii) clause census}\ [\text{machine F3}];\qquad(4):\ \ \text{the assembly of}\ \mathrm{IT.72}\text{--}\mathrm{IT.75}\text{'s certified markers};$$
$$(5),(6):\ \ \text{the bar censuses}\ [\text{machine F4}]\ \text{and the status assembly}.\ \blacksquare$$

**Phys.** The Architect's aside turned out to be a theorem, and a clean one. Reach and content
come apart: a rung-1 aspect lives in the sixteen dimensions of a single pair channel, the metric
it writes is evaluated on a single edge, and the locality rule forbids any read further out than
the edges that touch the ticking vertex — one hop, with sixty-two of sixty-six census instances
showing real content on the far side of that line. Content, meanwhile, is total: five shears,
three shifts, one volume, one conformal factor, ten of ten metric coordinates, and an exhaustive
census of all sixteen sub-collections showing that the largest proper subset stops at nine, so
every one of the four blocks is load-bearing. Nothing about this needs a range parameter, a mass
or a name from outside: the multi-hop world is built by chaining edges and averaging cells, which
is exactly what the bridge theorem does, and the corpus's own long-range carriers are chains whose
edges are null. Set beside the seals — the six that make the events and carry no coordinates at
all — the picture the directive proposed comes out right in its structure and disciplined in its
vocabulary: a layer, yes, but a dictionary, with its identification still priced and unpurchased.

---

### IT.77 — The mid-batch channel intake: three receipts for the builder's kernel-checked sector table

**Thm.**
$$(0)\quad\textbf{THE INTAKE (provenance, recorded):}\qquad\text{the builder's channel message}\ \texttt{comms/0009}\ \text{landed MID-BATCH}\ (\text{Lean Tier 2 kernel-green:}\ \texttt{SectorTable.lean}\ 40\ \text{theorems},\ \texttt{OpenedPaths.lean}\ 30,\ \text{zero imports, PR}\ \texttt{qubitick\_lean\#1}\ \text{merged)}\textbf{:}$$
$$\text{it names three items aimed at this level's machine — the}\ (7,3,3,3)\ \text{sector table proved twice, a Pauli-literal pin this checker lacked, and two rows deliberately NOT claimed}\ (\text{the Lie-closure ranks}\ 15/16{=}15{+}1,\ \text{``need exact elimination over}\ \mathbb Q(i)\text{''};\ \text{and}\ [\Sigma,W_i]\ \text{``not claimed either way — a hand computation says nonzero''});$$
$$\text{this tag answers all three on the rows. The tier's own}\ \S\mathrm A\ \text{census is an INDEPENDENT third attestation of the same table (Python vs instrument vs kernel)}\ [\mathrm{AT.63}(2)\ \text{pattern: the record gains receipts,}\ \neg\text{edits}]$$
$$(1)\quad\textbf{THE PAULI PIN, ADOPTED (new marker A6):}\qquad\boxed{\ \text{the four Pauli literals are certified to satisfy their own algebra BEFORE the}\ 16\text{-basis is built on them}\ }$$
$$\sigma_\mu^2=I\ (4),\quad\sigma_\mu^\dagger=\sigma_\mu\ (4),\quad\mathfrak T\sigma_\mu=2\delta_{\mu0}\ (4),\quad\det\sigma_0=+1\ \wedge\ \det\sigma_i=-1\ (4),\quad\sigma_\mu\sigma_\nu=\delta_{\mu\nu}I+\mathrm i\epsilon_{\mu\nu\rho}\sigma_\rho\ (16),\quad\mathfrak T(\sigma_\mu\sigma_\nu)=2\delta_{\mu\nu}\ (16)$$
$$\textbf{why it is load-bearing here:}\ \text{this session's own build mis-wrote}\ \sigma_3\ \text{with}\ -\mathrm i\ \text{in its lower slot instead of}\ -1;\ \text{the slip did NOT crash — it degraded the}\ \operatorname{Ad}(\mathbb S)\ \text{census silently and was caught only downstream}\ [\mathrm{A2}];\ \text{the pin localizes such a slip at the literal}\ [\text{the builder's}\ \texttt{pauli\_algebra\_pin},\ \text{credited}]$$
$$(2)\quad\textbf{THE}\ [\Sigma,W_i]\ \textbf{ROW: THE FROZEN CLAUSE STANDS, THE HAND COMPUTATION DOES NOT (new marker A7):}\qquad\boxed{\ [\Sigma,\ W_i]=0\ \ \text{EXACTLY, for all three}\ i\ }\qquad[\mathrm{CT1.5},\ \text{as used in}\ \mathrm{CT1.10}\ \text{'s Pf}:\ \text{``}[\Sigma,W_i]=0\ [\mathrm{CT1.5}]\implies\Sigma:\ \mathbf 1\text{''}]$$
$$\text{the full census of the sixteen commutators with}\ \Sigma:\qquad[\Sigma,W_i]=0\ (3\ \text{rows, identically});\qquad[\Sigma,J_i]=4\mathrm iK_i,\qquad[\Sigma,K_i]=-4\mathrm iJ_i\quad(\text{single-term, coefficients exactly}\ \pm4\mathrm i)\ [\mathrm{IT.51}(1)\ \text{re-certified}];\qquad E_0\ \text{central on all}\ 16;$$
$$\textbf{the cancellation, exhibited term by term for each}\ i\ (j,k\ \text{the complementary pair)}\textbf{:}\qquad[\Sigma,W_i]\propto\underbrace{-2\mathrm i(\sigma_j\otimes\sigma_k)-2\mathrm i(\sigma_k\otimes\sigma_j)}_{\text{from the}\ j\text{-th summand}}\underbrace{+2\mathrm i(\sigma_k\otimes\sigma_j)+2\mathrm i(\sigma_j\otimes\sigma_k)}_{\text{from the}\ k\text{-th summand}}=0\ \ \text{PAIRWISE};$$
$$\text{which is why a term-by-term hand computation that stops at the first summand reads ``nonzero''}\ \ \Longrightarrow\ \ \textbf{a Lean theorem asserting}\ [\Sigma,W_i]\ne0\ \textbf{would contradict the frozen}\ \mathrm{CT1.5}/\mathrm{CT1.10}\ \textbf{rows};\ \ \text{the corpus is the source of truth and the row wins}$$
$$\text{consequence re-stated: the}\ \mathbf 1\oplus\mathbf 5\oplus\mathbf 1\ \text{decomposition of}\ \mathcal E_{++}\ \text{under}\ \operatorname{span}\{W_i\}\ [\mathrm{CT1.10}]\ \text{rests on}\ \Sigma\ \text{being a scalar there, and}\ \mathrm{CT1.12}\text{'s dictionary reads}\ \Sigma_{\mathrm{tr}}\ \text{as the volume mode}\ (H)\ \text{accordingly}$$
$$(3)\quad\textbf{THE LIE-CLOSURE RANK ROWS, AS AN EXACT-ELIMINATION RECEIPT (new marker A8):}\qquad\text{all}\ \binom{15}{2}=105\ \text{commutator pairs of the}\ 15\ \text{traceless generators are expanded in the}\ 16\text{-basis by exact linear solve over}\ \mathbb Q(i):$$
$$\boxed{\ \text{every}\ E_0\text{-component vanishes (the bracket preserves tracelessness, so}\ E_0\ \text{stays central)};\qquad\operatorname{rk}\{\text{the commutators}\}=15;\qquad\operatorname{rk}\{15\ \text{traceless}\}=15;\qquad\operatorname{rk}\{16\}=16\ }$$
$$\text{i.e.}\ \dim=15\ \text{with}\ 16=15+1\ \text{exactly}\ [\mathrm{IT.51}(1)\text{'s ``the six generate}\ \mathfrak{su}(4)\text{''}];\qquad\text{the two rows named as the kernel's next increment now carry a Python attestation to double-enter against}\ [\mathrm{CT1.4};\ \mathrm{CT1.8}]$$
$$(4)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(3)\ \text{(three new markers,}\ 43/43\ \text{in the checker)};\qquad\textbf{record rows:}\ (0);\qquad\neg\text{a declaration},\qquad\neg\text{a canon edit},\qquad\neg\text{a new open row};\qquad\text{the builder's}\ \neg\text{claims stay}\ \neg\text{claims where they were honest: the Faddeev--LeVerrier charpoly and the CPT assembly remain with this level's machine}$$

**Req.** C1, C2 (Part 1); CT1.2, CT1.4, CT1.5, CT1.8, CT1.10 (Part 1); CT1.12 (Part 2); IT.51(1),(7) (this level); AT.63(2) (Level 5); the builder's `comms/0009` §1 (channel intake, credited in-tier); exact $\mathbb Q(i)$ matrix arithmetic (Pauli-literal pin, commutator census with exact basis expansion by linear solve, flattening ranks) [math; machine: `translation_layer.py` §§A6–A8, 3/3].

**Pf.**
$$(1):\ \ \text{the}\ 48\ \text{literal rows verified entrywise over}\ \mathbb Q(i)\ \text{(squares, hermiticity, traces, determinants, the}\ 16\text{-row product law with}\ \epsilon_{\mu\nu\rho}\ \text{from the antisymmetric difference product, the}\ 16\ \text{orthogonality traces)}\ [\text{machine A6}];$$
$$(2):\ \ \text{the}\ 16\ \text{commutators with}\ \Sigma\ \text{computed entrywise and re-expanded in the}\ 16\text{-basis by exact solve; the three}\ W\ \text{rows empty; the}\ J/K\ \text{rows single-term with coefficients}\ \pm4\mathrm i;\ E_0\ \text{central; the four-term cancellation exhibited for each}\ i\ [\text{machine A7}];$$
$$(3):\ \ \text{the}\ 105\ \text{pairs expanded by exact solve, the}\ E_0\text{-component census, and the three flattening ranks}\ (15,\ 15,\ 16)\ [\text{machine A8}];\qquad(0),(4):\ \ \text{record rows on the cited clauses}.\ \blacksquare$$

**Phys.** A kernel-checked table arrived mid-batch from the other half of the dyad, and it carried
three things: a guard this checker should have had, a pair of rows it could not yet claim, and one
row it declined to claim in either direction because a hand computation whispered the wrong answer.
All three are answered on the rows. The Pauli literals are now pinned before anything is built on
them, which is exactly the discipline this session's own sigma-three slip argues for. The
commutator of the exchange scalar with the weak generators vanishes, and the cancellation is
exhibited term by term so the whisper can be seen to stop one summand short — a frozen clause of
Part 1 confirmed against an incoming contradiction, which is the cheapest kind of corpus defence
there is. And the Lie-closure ranks, named as the next increment for the kernel, arrive here first
as an exact elimination receipt: fifteen, fifteen, sixteen. Three implementations, one canon, and
where they disagreed the row won.

---

### IT.78 — The verdict: the four claims component by component, the bars, and the census

**Thm.**
$$(1)\quad\textbf{THE VERDICT TABLE (every component traced to its certifying marker or its frozen ground):}\qquad\begin{array}{l|l|l}\textbf{claim}&\textbf{component}&\textbf{verdict}\\\hline(1)&\text{the four blocks carry metric coordinates}\ (5{+}3{+}1{+}1{=}10)&\textbf{DERIVED}\ [\mathrm{IT.72}(2);\ \mathrm{B1},\mathrm{B5}]\\(1)&\text{the seals carry zero metric coordinates}&\textbf{DERIVED}\ [\mathrm{FT.141}(5);\ \mathrm{IT.72}(2);\ \mathrm{B5}]\\(1)&\text{the dictionary is a bijection}\ 10\leftrightarrow10&\textbf{DERIVED}\ [\mathrm{CT1.12};\ \mathrm{IT.72}(3);\ \mathrm{B2}]\\(1)&\text{they ARE the dimensions (an identity)}&\textbf{NOT ADOPTED — four prices}\ [\mathrm{IT.52}(3);\ \mathrm{IT.54}(1);\ \mathrm{B6}];\ \text{an adoption is the Architect's act,}\ \neg\text{forced}\\\hline(2)&\text{ticks are ledger events,}\ \neg\text{geometric}&\textbf{DERIVED}\ [\mathrm{A6};\ \mathrm{A7};\ \mathrm{D1.9};\ \mathrm{IT.73}(1);\ \mathrm{C1},\mathrm{C3}]\\(2)&\text{the forces are geometric (the metric's coefficients)}&\textbf{DERIVED}\ [\mathrm{IT.72}(2);\ \mathrm{CT1.12};\ \mathrm{FT.157}(1)]\\(2)&\text{the}\ G\ \text{quintet is a geometric wave mode}&\textbf{DERIVED}\ [\mathrm{CT1.18};\ \mathrm{CT1.10};\ \mathrm{IT.73}(3),(4);\ \mathrm{C5},\mathrm{C6}]\\(2)&W,H,D^+\ \text{as wave modes}&\textbf{NOT DERIVED — scoped absence,}\ \neg\text{a no-go}\ [\mathrm{IT.73}(4),(8);\ \mathrm{AT.5}(4);\ \mathrm{CT1.17}];\ \text{the residue}\subseteq\mathrm{D\text{-}PJ7}\text{'s P4 transport profile}\\(2)&\text{the dynamical mediation reading}&\textbf{BARRED as formed — three grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{IT.73}(6);\ \mathrm{C8}]\\\hline(3)&W_i\ \text{is}\ T\text{-odd}&\textbf{DERIVED}\ [\mathrm{CT1.2};\ \mathrm{IT.74}(1);\ \mathrm{A3},\mathrm{A4}]\\(3)&\text{it transports to the time-reversal pullback}&\textbf{DERIVED}\ [\mathrm{FT.156}(3);\ \mathrm{IT.74}(2),(3);\ \mathrm{D1},\mathrm{D2},\mathrm{D3}]\\(3)&\text{the interval is}\ T\text{-even (the flip is an involution)}&\textbf{DERIVED}\ [\mathrm{IT.74}(4);\ \mathrm{D4};\ \mathrm{CT1.12a}(2);\ \mathrm{CT1.19b}(2)]\\(3)&\text{it separates the two null legs}&\textbf{DERIVED}\ [\mathrm{IT.74}(5);\ \mathrm{IT.53}(5)(\mathrm b);\ \mathrm{D5}]\\(3)&\text{it distinguishes past from future}&\textbf{SPLIT: derived in the formal/read sense only}\ [\mathrm{IT.74}(6)];\ \text{the arrow's locus is}\ \neg\exists\tau^{-1}\ [\mathrm{A6}]+\mathrm{FT.144}(2),(3)+\mathrm{A7}\\(3)&\text{it encodes left/right}&\textbf{BARRED as a naming}\ [\mathrm{FT.156}\ \mathrm{Rmk};\ \mathrm{FT.157}\ \mathrm{Rmk};\ \mathrm{FT.101}\ \mathrm{Phys};\ \mathrm{D7}]\\\hline(4)&\text{the contraction measures the ledger (jointly)}&\textbf{DERIVED}\ [\mathrm{IT.75}(1)\text{--}(5);\ \mathrm{E1}\text{--}\mathrm{E5}]\\(4)&\text{the on-shell integers}\ (\Theta_{\mathcal P}\in2\mathbb Z,\ \kappa\in\mathbb Z)&\textbf{DERIVED}\ [\mathrm{CT1.19b};\ \mathrm{IT.75}(3);\ \mathrm{E3}]\\(4)&\text{the inverse translation (metric}\to\text{ledger integer)}&\textbf{DERIVED}\ [\mathrm{AT.5}(1),(3);\ \mathrm{IT.75}(4);\ \mathrm{E4}]\\(4)&\text{a per-block measurement}&\textbf{BARRED}\ [\mathrm{FT.30}\ \mathrm{Verdict};\ \mathrm{IT.75}(1)]\\(4)&\text{the operational read (the radar)}&\textbf{DECLARED and formed}\ [\mathrm{D\text{-}RS6};\ \mathrm{D\text{-}RS3};\ \mathrm{IT.68}];\ \ \mathrm{D\text{-}RS4}\ \text{deferred}\\(4)&\text{the dynamical jump}&\textbf{BARRED — three grounds}\ [\mathrm{IT.66}(1);\ \mathrm{IT.73}(6)]\\\hline\text{note}&\text{reach}\ 1\ \text{hop}\ \wedge\ \text{content the whole}\ S\ \text{sector}&\textbf{DERIVED, minimally}\ [\mathrm{IT.76}(1),(2);\ \mathrm{F1},\mathrm{F2}]\\\text{note}&\text{the SM weak-boson framing}&\textbf{FLAGGED}\ \neg\textbf{ADOPTED — out-of-corpus clarification}\ [\mathrm{IT.71}(3);\ \mathrm{IT.76}(5);\ \mathrm{F4}]\end{array}$$
$$(2)\quad\textbf{THE BAR-CHECK (machine):}\qquad\begin{array}{l|l}\textbf{the bar}&\textbf{the verdict}\\\hline\mathrm{P1}\ \text{(no new dimensionful scale)}&\textbf{HONORED}: \text{every dimensional symbol stays symbolic}\ (\mathfrak h,\ \mathfrak q,\ G_N,\ \varkappa,\ \beta,\ \alpha_\Omega,\ \Omega);\ \text{the tier's own rows are counts, parities and exact rationals;}\ \mathrm{D\text{-}RS7}\text{'s}\ \mathfrak q^0\ \text{discipline untouched}\\\mathrm{P5}\ \text{(no measured value)}&\textbf{HONORED}: \text{zero decimal numeric tokens in the tier (machine scan, word-bounded); the only numerals are exact integers and rationals; no value issued}\\\text{the transit bar}&\textbf{STANDS on three grounds}\ \mathrm{O1/O2/O4}:\ \mathrm{O1}\ \text{RE-RUN by machine (six commutators zero, same-factor adversarial nonzero)};\ \neg\text{a vertex, amplitude, weight or rate is constructed in this tier}\\\text{count}\to\text{strength}&\textbf{BARRED as ever}\ [\mathrm{BM.36}(3);\ \mathrm{BM.61}(8)(\mathrm{O1});\ \mathrm{FT.73}(5)]:\ \text{the}\ 10/6,\ 7/3,\ 4/6\ \text{and}\ 1\text{-hop rows are counts, and no coupling strength is read off any of them}\\\text{species identification}&\textbf{NONE}: \text{no species name enters any clause; the SM framing is flagged and quoted as barred}\ [\mathrm{Def\text{-}BM.3}(1),(7);\ \mathrm{FT.157}\ \mathrm{Rmk}]\\\text{the arena bars}&\textbf{UNTOUCHED}: \neg\text{an arena object is added}\ [\mathrm{Def\text{-}H.41}/\mathrm{Def\text{-}H.42}\ \text{re-certified at}\ \mathrm{IT.64}(4)]\\\text{the incommensurability bar}&\textbf{HOLDS}: \text{the faces stay in their own currencies and the formed mixed loci remain exactly three}\ [\mathrm{IT.4}(2);\ \mathrm{IT.68}(3)]\\\text{dictionary}\ \neg\text{bridge}&\textbf{HONORED}: \text{claim 1's identity reading is refused}\ [\mathrm{IT.72}(5);\ \mathrm{BM.134}(5)]\\\text{the frozen canon}&\textbf{CITED, NEVER EDITED}\ [\mathrm{AT.63}(2)]:\ \text{the directive's citation slip is recorded as}\ \mathrm{IT.71}(4)(\mathrm{P1}),\ \neg\text{applied to any row}\end{array}$$
$$(3)\quad\textbf{THE DECLARATION CENSUS:}\qquad\textbf{the declarations this tier adds: none.}\quad\text{nothing was forced: claim 1's identity reading stays at}\ \mathrm{IT.52}(3)\text{'s}\ \neg\text{adoption (an adoption would be a new Architect act, and this tier neither issues nor mints a candidate for it); claim 4's operational read needed no new act because}\ \mathrm{D\text{-}RS6}\ \text{and}\ \mathrm{D\text{-}RS3}\ \text{are already issued}\ [\mathrm{IT.66}(1);\ \mathrm{IT.65}(1)];\ \text{claim 2's residue is owed content that already has a register locus};$$
$$\boxed{\ \S\mathrm{Cal\text{-}IT}\ \text{stays VALUE-FREE and unchanged; the register stands as}\ \mathrm{IT.66}(4)\ \text{records it: issued}\ \mathrm{D\text{-}PJ1}\text{–}\mathrm{D\text{-}PJ6},\ \mathrm{D\text{-}RS1}\text{–}\mathrm{D\text{-}RS3},\ \mathrm{D\text{-}RS6},\ \mathrm{D\text{-}RS7},\ \text{the}\ \mathrm{BM.113}(6)\ \text{sector sync; deferred}\ \mathrm{D\text{-}RS4};\ \textbf{owed}\ \mathrm{D\text{-}PJ7}\ \textbf{alone}\ +\ \text{the three sub-debts}\ }$$
$$(4)\quad\textbf{THE OPEN-ROW STATE:}\qquad\boxed{\ \textbf{NO new open row}\ };\qquad\mathrm{IT\text{-}O1}\ \text{UNCHANGED (three grounds; deficit}\ 1');\qquad\mathrm{IT\text{-}O2}\ \text{UNCHANGED (the binding value; the three}\ \mathrm{IT.27}(2)\ \text{constructions)};\qquad\mathrm{IT\text{-}O5}\ \text{UNCHANGED};\qquad\mathrm{IT\text{-}O3},\ \mathrm{IT\text{-}O6}\ \text{stay CLOSED}\ [\mathrm{IT.60}(3);\ \mathrm{IT.69}(6)];$$
$$\text{the one residue this tier names — a formed propagator role for}\ W,H,D^+\ \text{— CONSOLIDATES under}\ \mathrm{D\text{-}PJ7}\text{'s P4 transport profile (the declared gauge field)}\ [\mathrm{IT.41}(2);\ \mathrm{IT.66}(4)],\ \ \neg\text{a new row}\ [\mathrm{AT.63}(2)\ \text{pattern: no proliferation}]$$
$$(5)\quad\textbf{THE MACHINE STATE:}\qquad\texttt{translation\_layer.py}\to\textbf{43/43 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{23 checkers, 393 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{22 Part 6 documents PASS, 78 IT-blocks};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad\text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)]$$
$$(6)\quad\textbf{THE ERA CHAIN:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and a derived row is a row the frozen inventory already forced — not one the hypothesis wished for}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** P1, P5 (Parts 1–2); A6, A7, D0.6, D1.9, D2.9 (Parts 1–2); CT0.12, CT1.2, CT1.10, CT1.12, CT1.12a(2), CT1.18, CT1.19b, CT2.6 (Parts 1–2); Def-H.41, Def-H.42, Def-BM.3(1),(7), FT.20, FT.30, FT.73(5), FT.101, FT.141(5), FT.144, FT.156, FT.157 (Part 3); BM.34, BM.36(3), BM.61(8), BM.134(5) (Part 4); IT.4(2), IT.27(2), IT.40–IT.42, IT.41(2), IT.51(1), IT.52(3), IT.53, IT.54(1), IT.56(2), IT.60(3), IT.64(4), IT.65(1), IT.66(1),(4), IT.68, IT.69(6), IT.71–IT.77, IT-O1, IT-O2, IT-O3, IT-O5, IT-O6 (this level); AT.5, AT.39(8), AT.63(2),(4) (Level 5); the full checker, the level runner and the level gate re-run end to end [math; machine: `translation_layer.py` §§G1–G4, 4/4].

**Pf.**
$$(1):\ \ \text{the row-wise assembly of}\ \mathrm{IT.72}\text{--}\mathrm{IT.76}\ \text{with every verdict traced to its certifying marker}\ [\text{machine G1}];\qquad(2):\ \ \text{the bar assembly with the tier scans (zero decimals; the dimensionful-symbol census; the alphabet census for amplitude/vertex/weight/rate tokens)}\ [\text{machine G2}];$$
$$(3)\text{--}(6):\ \ \text{the declaration scan, the open-row assembly, the runner and the gate re-run end to end. No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** Four claims went in and came out in eleven pieces. Two survived whole: the metric
coordinates are real, ten of them, four blocks, none for the seals — and the tick really is a
ledger event that never touches the metric except as an increment. Two came out split, and the
splits are the interesting part. The forces are geometric but only one of them is a wave: the
linearized Einstein tensor has four components with no second time derivative at all, and those
four are exactly the conformal cell and the three shift cells, so lapse and shift are constraints
while the quintet propagates. The shift is T-odd, and its sign does separate the two legs of a
radar echo, but the interval it builds is T-even and the arrow of time lives in a tick that has no
inverse — not in a grading. The fourth claim is a capability the corpus had already written as a
formula, an edge weight that is one ledger bit times one geometric phase, joint across all ten
coordinates and quantized only on shell, with the per-block version barred and the operational
version declared two tiers ago. And the aside about one hop became the tier's cleanest theorem:
range one hop, content all ten, minimal in both, with the multi-hop world assembled by chains and
averages rather than by reach. Nothing was forced, nothing was issued, and the register is
exactly where the last tier left it.

---

## §Cal-IT — unchanged (value-free)

**No act at this tier.** Tier IT.22 issues no declaration (machine-scanned at IT.78(3)): it is an
adjudication tier on the frozen inventory and the already-declared vocabulary. The act register
stands as IT.66(4) records it — issued: D-PJ1–6, D-RS1–3, D-RS6–7, the BM.113(6) sector sync;
deferred: D-RS4; owed: **D-PJ7 alone** + the three sub-debts. **No calibration parameter is added,
valued, or re-scoped**: the P1 scale slot, $\varepsilon_q$ (AT-O27), $e_0$ [EM.25(7)],
$(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$ [A-BM.9], $\hat\mu'^2$, $\sigma_\ell$,
$\sigma_\nu$, the $\mu_{\mathrm{ch}}$ family (Cal-F), the read rules (M1′)–(M3′) [AT.54(6)], the
lift/vielbein/P4 profile [AT.63(3)], and the mass-read route choice [IT.14(3); BM.30(5)] all stand
unchanged. The rational witnesses used throughout the checker ($\Omega^2$, $\varkappa$, $\beta$,
$q_{ij}$, $w_i$, $\Delta x^\mu$) are exact Fraction WITNESSES of polynomial identities, not values
[IT.59(2) pattern]; the Laurent coefficients $4\kappa$ of IT.75(3) are symbolic [P5]. The
Calibration Era stays **deferred** [AT.63(4)].

## §Open-IT additions from Tier IT.22

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.22 opens **no new row**. The four claims are adjudicated component by component at IT.77(1): claim 1 DERIVED as a dictionary with the identity reading left at IT.52(3)'s ¬adoption (four prices, an Architect act, ¬forced); claim 2 DERIVED on the tick/channel separation and on the $G$ quintet's wave mode, with a SCOPED ABSENCE for $W,H,D^+$ as wave modes whose residue CONSOLIDATES under D-PJ7's P4 transport profile [IT.41(2); IT.66(4)]; claim 3 DERIVED on the $T$-oddness and the transport, SPLIT on the arrow (locus: $\neg\exists\tau^{-1}$ [A6; FT.144]), BARRED on the left/right naming; claim 4 DERIVED as a joint capability, BARRED per block [FT.30 Verdict], DECLARED-and-formed as an operational read [D-RS6; D-RS3; IT.68], BARRED as dynamics. The 1-reach theorem (range 1 hop, content the whole $S$ sector, minimal) is DERIVED at IT.76(1),(2); the mid-batch channel intake at IT.77 adds three receipts for the builder's kernel-checked sector table (the Pauli pin, $[\Sigma,W_i]=0$ against an incoming contradictory hand computation, and the Lie-closure rank rows 15/15/16) and opens no row | IT.72(5); IT.73(7),(8); IT.74(8); IT.75(8); IT.76(1),(2); IT.78(1),(4) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4); IT.57(5); IT.60(4); IT.62(4);
IT.66(6); IT.70(1)]: (IT-O1) the formed transit-leg amplitude — three grounds O1/O2/O4, deficit 1′
[IT.41(2)]; (IT-O2) the binding value — the three IT.27(2) constructions (the δ-glue input named at
IT.69(6)); (IT-O5) the isotope cutoff — the dynamical side at IT-O1; AT-O30/AT-O32 the heavy
censuses; the owed route choice [IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the
Level-5 inheritance [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.23: the n-fold radar synchronization and the exact cyclotomic DFT — the equation of motion as an annihilator read of the formed window

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.23 — the Architect's interim directive
(session 13r): *"develop the system of n radar synchronisation and applying discrete FFT on it.
Like if you do radar sync once you know position, if twice you have a guess at velocity, if you do
n times and the do FFT you can understand the equation of motion. That thing."* Executed as a
construction on the FORMED radar read family of IT.68 and the declared vocabulary (D-RS1/D-RS2/
D-RS3/D-RS6 + D-PJ6): the n-fold family, its exact rational kinematic faces, and the exact
cyclotomic DFT whose annihilator grammar IS the read-level "equation of motion" — with the window
discipline honest at every step: the grammar describes the recorded pings and predicts nothing.
The batch also PLACES the builder's teacher-board identity $L(n) = n\,2^{n+1}$ (adjudicated in
comms 0012: the arithmetic rows derived, the bridge flagged a reading), with credit. **The M
freeze is honored**: nothing in this tier touches the cross-currency matrix $M$ or its tensor
square $X$ — the Architect's restructuring is pending. **Tags.** IT.79–IT.83. **Pattern.** the
construction tiers (IT.18/IT.21's shape) on declared vocabulary; corrections recorded in-tier.
**Status.** discovery-phase working tier. No declaration issues at this tier (machine-scanned);
§Cal-IT stays value-free and unchanged; no clause of Parts 1–4, of Level 5's closed record, or of
Tiers IT.1–IT.22 is modified [AT.63(2)]. No measured value enters [P5]; no new dimensionful scale
[P1]; species names stay quoted [Def-BM.3(1),(7)].
**Machine.** `era2/level6_isotopic/checks/nradar_fft.py` → **19/19 exact** (integers and
Fractions throughout; exact integer polynomial rings for the cyclotomics $\Phi_n$; exact Fraction
linear solves for the annihilators; exhaustive enumeration of the order theorem at $n\le4$;
deterministic witnesses only — no randomness, NO floating point); `run_all_level6.py` →
**24 checkers, 412 exact markers, 0 failures**; `check_level6_format.py` → the gate over all
twenty-three Part 6 documents.
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's directive, executed in full: the n-fold system (IT.79), the kinematic
faces (IT.80), the DFT grammar and the equation-of-motion read (IT.81), the builder's L(n) row
placed with credit and its bridge flagged (IT.82), the verdict and the bars (IT.83). The
F=ma/mass-matrix probe is PAUSED on the Architect's word mid-survey; nothing of it was committed
anywhere, and this tier cites none of it.

---

### IT.79 — The n-fold radar read family: formed, with the unique total order at every n

**Thm.**
$$(1)\quad\textbf{THE FAMILY (formed, inside the issued declarations):}\qquad n\ \text{sequential round trips at the emitter's local designated register}\ o\ [\mathrm{Def\text{-}H.9}(2);\ \mathrm{D\text{-}PJ6}/\mathrm{D\text{-}RS5}\ @\ \mathrm{IT.55}(7)]:$$
$$\boxed{\ \bigl(\tau_e^{(j)},\ \tau_r^{(j)}=\tau_e^{(j)}+2\delta h_j\bigr),\qquad d_j=\tfrac12\bigl(\tau_r^{(j)}-\tau_e^{(j)}\bigr)=\delta h_j\in\mathbb N,\qquad j=1..n\ }\qquad[\mathrm{D\text{-}RS3}\ @\ \mathrm{IT.65};\ \mathrm{D0.6};\ \mathrm{EM.7}]$$
$$\text{the conversation chain is STRICT:}\quad\tau_e^{(1)}\prec\tau_r^{(1)}\prec\tau_e^{(2)}\prec\tau_r^{(2)}\prec\cdots\prec\tau_e^{(n)}\prec\tau_r^{(n)}\qquad[\mathrm{D\text{-}RS1}\ @\ \mathrm{IT.56}(1);\ \mathrm{D1.8};\ \mathrm{D0.7};\ \mathrm{A6}];$$
$$\text{machine census (systematic grids,}\ n=1..8\ \text{pings}\times\delta h\text{-grids}\times\text{gap grids}\times\tau_0\text{-grids): every cell integral, every halving exact, every chain strict};$$
$$\text{the ``n-radar synchronisation'' is}\ n\ \text{READS OF ONE LEDGER — no cross-clock convention exists or is needed}\ [\mathrm{IT.53}(5)(\mathrm c)\ \text{at}\ n].$$
$$(2)\quad\textbf{THE n-FOLD ORDER THEOREM (machine, exhaustive):}\qquad\text{under the grounded constraints — the}\ n\ \text{leg constraints}\ e_j\prec r_j\ [\mathrm{D\text{-}RS1}\ \text{on the total tick order}]\ +\ \text{the}\ n{-}1\ \text{conversation constraints}\ r_j\prec e_{j+1}\ [\mathrm{IT.60}(1)\text{'s grounding: the node's}\ \mathrm{C11}\ \text{in-before-out}\ +\ \text{cross-cycle monotonicity}] —$$
$$\boxed{\ \text{EXACTLY ONE of the}\ (2n)!\ \text{orderings survives, at every}\ n=2,3,4\ (24\ /\ 720\ /\ 40320\ \text{enumerated}): \text{the TOTAL CHAIN}\ e_1\prec r_1\prec e_2\prec r_2\prec\cdots\prec e_n\prec r_n\ }$$
$$\text{the}\ n=1\ \text{case is}\ \mathrm{IT.60}(1)\text{'s}\ 1\text{-of-}24\ \text{theorem verbatim};\qquad\text{the synchronisation question is vacuous on the ledger at every}\ n\ [\mathrm{IT.53}(5)(\mathrm c)\ \text{pattern}].$$
$$(3)\quad\textbf{THE}\ n=1\ \textbf{REDUCTION (machine):}\qquad\text{at}\ n=1\ \text{the family is EXACTLY}\ \mathrm{IT.68}(1)\text{'s formed census — all}\ 160\ \text{cells}\ (\delta h=1..32\times\tau_e=0..4)\ \text{reproduce};$$
$$\text{the agreement}\ d_{e\to p}^{(j)}=d_{p\to e}^{(j)}\ \text{stays the endpoint-blindness CONSEQUENCE ping by ping}\ (\delta h_{\mathrm{out}}=\delta h_{\mathrm{in}}\ \text{read the same return word}\ [\mathrm{IT.53}(5)(\mathrm a);\ \mathrm{AT.44}(1);\ \mathrm{D\text{-}RS2}\ @\ \mathrm{IT.56}(2)]);$$
$$\text{the barred per-visit alternative re-witnessed at every ping:}\ (2\delta h-1)/2\ \text{a half-integer for all}\ \delta h=1..32\ (32/32)\ [\mathrm{IT.65}\ \text{ground}\ (\mathrm{ii})].$$
$$(4)\quad\textbf{status:}\qquad\textbf{formed as reads — the whole}\ n\text{-fold family inside the}\ \mathrm{D\text{-}RS6}\ \text{declaration and its scope rows}\ [\mathrm{IT.66}(1);\ \mathrm{IT.68}(6)\ \text{pattern}];\qquad\neg\text{a new act},\qquad\neg\text{an amplitude},\qquad\neg\text{a vertex},\qquad\neg\text{a weight},\qquad\neg\text{a rate}\ [\mathrm{IT.68}(5)\ \text{pattern}];$$
$$\text{the read's alphabet:}\ \ \{\delta h_j,\ \tau_e^{(j)},\ \tau_r^{(j)},\ d_j,\ \prec\}\ \cup\ \{\text{the faces of}\ \mathrm{IT.80}\}\ \cup\ \{\text{the window algebra of}\ \mathrm{IT.81}\}\ \cup\ \{\text{the existing}\ \mathfrak h/\ln2\ \text{monomials, chart side}\}.$$

**Req.** A6, A7, P1, P5, C11 (Part 1); D0.6, D0.7, D1.8 (Part 1); EM.7, Def-H.9(2), Def-H.19 (Parts 2–3); IT.53(5), IT.55(7), IT.56(1),(2), IT.60(1), IT.65, IT.66(1), IT.68(1),(5),(6) (this level); AT.44(1) (Level 5); exhaustive order enumeration, exact integer censuses [math; machine: `nradar_fft.py` §A, 3/3].

**Pf.**
$$(1)\text{--}(3):\ \ \text{the certifying markers A1--A3 — the systematic}\ n\text{-fold census (integrality, the interval halving, the strict chain), the exhaustive}\ 1\text{-of-}(2n)!\ \text{enumerations at}\ n=2,3,4,\ \text{the}\ 160\text{-cell reduction with the per-visit re-witness}\ [\text{machine A1--A3}];\qquad(4):\ \ \text{the record rows on the cited clauses}.\ \blacksquare$$

**Phys.** One radar ping is an echo; n sequential pings are a conversation, and the conversation
turns out to have exactly one grammar. The legs are labels on the total tick order, the node's
lifecycle puts reception before the next emission, and out of the (2n)! ways to interleave the
events a single total chain survives — at every n the census tried, exhaustively. So the
"synchronization system" the directive asked for needs no clocks and no conventions: it is n
reads of the one ledger, each read the IT.68 round trip at its own emission tick, integral in
every cell, its two directions agreeing not by postulate but because the return word never knew
its endpoints. What the family carries is a window of integers — and a window of integers, it
turns out, is exactly enough for kinematics.

---

### IT.80 — The kinematic faces: position, velocity, acceleration as exact rational count-reads

**Thm.**
$$(1)\quad\textbf{THE THREE FACES (the directive's ladder, exact):}\qquad\text{on the window}\ (d_1,\dots,d_n)\ \text{with emission ticks}\ (\tau_e^{(1)},\dots,\tau_e^{(n)}):$$
$$\textbf{position face:}\ \ d_j\in\mathbb N\ \text{(the}\ \mathrm{D\text{-}RS3}\ \text{hop face — ONE ping reads a position)};\qquad\textbf{velocity face:}\ \ v_j=\frac{d_{j+1}-d_j}{\tau_e^{(j+1)}-\tau_e^{(j)}}\in\mathbb Q\ \text{(TWO pings read ONE velocity — exact,}\ \neg\text{a guess)};$$
$$\textbf{acceleration face:}\ \ a_j=\frac{\frac{d_{j+2}-d_{j+1}}{\Delta\tau_{j+1}}-\frac{d_{j+1}-d_j}{\Delta\tau_j}}{\tfrac12(\Delta\tau_j+\Delta\tau_{j+1})}\in\mathbb Q\ \text{(the symmetric second difference over the mean spacing)};$$
$$\text{every face is a ratio of COUNTS — a}\ \mathfrak q^0\ \text{price}\ [\mathrm{D\text{-}RS7}\ \text{'s price discipline};\ \mathrm{D2.9}];\qquad\text{the rational-count-read precedent: the neighbour law}\ R(n)=(n{+}1)/n\ [\mathrm{IT.50}];$$
$$\boxed{\ \text{THE WINDOW DISCIPLINE: a face describes the RECORDED interval,}\ \neg\text{an instantaneous state; extrapolation beyond the window is}\ \neg\text{formed}\ }$$
$$(2)\quad\textbf{THE FACE ALGEBRA (machine census):}\qquad\text{at equal tick spacing}\ T:\ \ v_j\in\tfrac1T\mathbb Z\ \text{and}\ a_j\in\tfrac1{T^2}\mathbb Z\ \text{EXACTLY — the full census}\ T=1..4\times\ \text{windows}\ n=2..6\times\ d\in\{-2..2\}^n\ (78{,}100\ \text{cells, every value an exact Fraction with the claimed denominator structure});$$
$$\text{non-vacuity: perturbing ONE cell of the constant-acceleration witness breaks the constant acceleration face (the face could read wrong and does not).}$$
$$(3)\quad\textbf{THE WITNESS FAMILIES (machine):}\qquad\text{rest}\ (v=0,\ a=0);\ \ \text{uniform recession}\ (v=3\ \text{constant},\ a=0);\ \ \text{constant acceleration}\ (v=(2,4,6),\ \text{the symmetric second difference constant});\ \ \text{period-4 oscillation}\ (v\in\{-1,+1\}\ \text{alternating});$$
$$\text{unequal spacing}\ (\tau=(0,1,3),\ d=(3,5,6)):\quad v=\bigl(2,\ \tfrac12\bigr)\ \text{— a NON-INTEGER exact Fraction: the velocity face is a RATIO,}\ \neg\text{a count (the adversarial against any integer-velocity reading).}$$
$$(4)\quad\textbf{THE CHART FACE, PER PING (machine):}\qquad d\tau_\pm^{(j)}=\sqrt{G_j}\,dx_j/(N_j\mp s_j),\ \ s_j=\sqrt{G_j}\,N^x_j\ [\mathrm{IT.53}(4);\ \mathrm{BM.34}(2)\ \text{'s null roots}]:$$
$$\text{the leg-difference identity}\ d\tau_+^{(j)}-d\tau_-^{(j)}=\frac{2\sqrt{G_j}\,dx_j\,s_j}{N_j^2-s_j^2}\ \text{and the agreement}\iff s_j\,dx_j=0\ \text{hold PING BY PING — re-run at three exact witnesses}\ (G,dx,N,s)=(4,3,5,2),\ (9,1,4,-1),\ (16,5,7,3);\ \ \text{the}\ T\text{-conjugacy}\ s\mapsto-s\ \text{swaps the legs at every ping}\ [\mathrm{IT.68}(2);\ \mathrm{BM.34}(3);\ \mathrm{FT.156}(3)];$$
$$\text{the half-distance equals the proper length exactly at}\ s_j=0\ \text{per ping}\ [\mathrm{IT.68}(2)\ \text{re-cited}].$$
$$(5)\quad\textbf{THE CURRENCY AND THE BOUNDARIES (machine set census + record):}\qquad\text{the ledger faces (counts, their ratios, the order labels) meet the chart faces}\ (\sqrt G,\ dx,\ N,\ s,\ \text{the}\ \mathfrak h/\ln2\ \text{monomials}),\ \text{the baryon generators and the amplitude tokens in the EMPTY SET};$$
$$\text{the difference operators are}\ \mathbb Q\text{-LINEAR PER FACE — they transform each currency's reads inside that currency and never sum across the dictionary}\ [\mathrm{D\text{-}RS2};\ \mathrm{BM.134}(5)];\qquad\text{the formed mixed loci remain exactly three}\ [\mathrm{IT.4}(2)];$$
$$\text{the stationarity instantiation scope stays DEFERRED PER PING}\ [\mathrm{D\text{-}RS4}\ @\ \mathrm{IT.56}(3);\ \mathrm{IT.64}(6)]:\ \text{the chart faces of different pings are compared only inside the deferred scope, and the ledger faces need no stationarity at all};\qquad\text{the disjointness row stands per ping}\ [\mathrm{IT.53}(6)].$$

**Req.** P1, P5, D0.6, D0.7, D1.8, D2.9 (Parts 1–2); EM.7, BM.34(2),(3) (Parts 2, 4); FT.156(3) (Part 3); IT.4(2), IT.50, IT.53(4),(5),(6), IT.56(2),(3), IT.64(6), IT.65, IT.68(2),(3), D-RS7 (this level); exact Fraction face arithmetic, exhaustive window censuses, exact rational leg witnesses [math; machine: `nradar_fft.py` §B1–B4, 4/4].

**Pf.**
$$(1)\text{--}(3):\ \ \text{the certifying markers B1--B2 — the witness families with every face exact, the}\ \tfrac1T\mathbb Z/\tfrac1{T^2}\mathbb Z\ \text{denominator census over}\ 78{,}100\ \text{cells, the perturbation adversarial}\ [\text{machine B1, B2}];\qquad(4):\ \ \text{the three-witness leg census with the agreement both directions}\ [\text{machine B4}];$$
$$(5):\ \ \text{the symbol-set census (four pairwise-empty intersections)}\ [\text{machine B4}]\ \text{and the record rows}.\ \blacksquare$$

**Phys.** "Once you know position, twice you have a guess at velocity" — the corpus improves on
the guess. The position face is the declared hop count; the velocity face is one exact Fraction,
a count ratio in the q-zero currency the price clarification already covers, and the window says
plainly what it is: a slope over the recorded interval, not a state at an instant. Acceleration
is the second difference, and the denominator census shows the faces live exactly where the
arithmetic puts them — halves at spacing two, quarters in the second read. The chart answers
each ping in its own currency, the shift flipping the legs into each other's mirror as always,
and the two dictionaries never mix: the difference operator is linear inside a currency, blind
across them. What the faces refuse to do is also exact: nothing here extrapolates a single ping
beyond the window.

---

### IT.81 — The exact cyclotomic DFT: the equation of motion is the annihilator read of the window

**Thm.**
$$(1)\quad\textbf{THE CYCLOTOMIC GROUND (machine):}\qquad\Phi_n(z)\ \text{for}\ n=1..8\ \text{by the exact integer recursion}\ \prod_{d\mid n}\Phi_d=z^n-1\ (\text{zero remainders; the product identity independently re-multiplied at every}\ n);\ \ \deg\Phi_n=\varphi(n)=(1,1,2,2,4,2,6,4);\ \ \text{the literals}\ \Phi_4=z^2{+}1,\ \Phi_6=z^2{-}z{+}1,\ \Phi_8=z^4{+}1;$$
$$\text{the rings}\ \mathbb Q[z]/(\Phi_n)\ \text{carry}\ \zeta=[z]\ \text{with}\ \zeta^n=1\ \text{EXACTLY}\ (8/8)\ \text{— the only ring property the DFT rows use (irreducibility/field-ness is standard context, cited by NO marker};\ \neg\text{a floating-point transcendental anywhere}).$$
$$(2)\quad\textbf{THE CHARACTER SUM AND THE PAIR (machine; the convention pinned:}\ \zeta=[z],\ \text{forward exponent}\ {+}jm\textbf{):}\qquad\sum_{m=0}^{n-1}\zeta^{mk}=n\cdot[k\equiv0\ (\mathrm{mod}\ n)]\ \text{exactly in every ring, all}\ k\ (64\ \text{cells});$$
$$D_m=\sum_{j}d_j\,\zeta^{jm},\qquad d_j=\tfrac1n\sum_mD_m\,\zeta^{-jm}\qquad\text{round-trip EXACT on ALL}\ 155\ \text{windows in}\ \{-2..2\}^n\ \text{for}\ n=1,2,3\ (\text{exhaustive})\ +\ 16\ \text{deterministic witnesses at}\ n=4..8.$$
$$(3)\quad\textbf{THE TRANSPORT THEOREMS (machine census):}\qquad\mathrm{DFT}(\sigma d)_m=\zeta^{-m}D_m,\qquad\mathrm{DFT}\bigl((\sigma-1)d\bigr)_m=(\zeta^{-m}-1)\,D_m\qquad(\sigma\ \text{the cyclic shift});$$
$$\text{the velocity face of}\ \mathrm{IT.80}\ \text{IS the difference operator: its spectrum is the position spectrum times the exact cyclotomic factor — differentiation is multiplication, with no analysis, only the ring.}$$
$$(4)\quad\textbf{PARSEVAL, EXACT AND RATIONAL (machine):}\qquad\sum_jd_j^2=\tfrac1n\sum_mD_m\overline{D_m}\ \text{with}\ \overline{\phantom{D}}\ \text{the Galois involution}\ \zeta\mapsto\zeta^{-1}\ \text{(a ring homomorphism — witnessed): the right side returns a PURE RATIONAL scalar on every window (the cyclotomic part identically zero)};$$
$$\neg\text{an information-theoretic quantity is formed — no entropy, no Shannon read}\ [\mathrm{D0.9};\ \mathrm{C10}];\qquad\text{the capacity-Fourier bar is UNTOUCHED: the DFT acts on the formed READ WINDOW, never on a capacity count}\ [\mathrm{IT.54}(1)].$$
$$(5)\quad\textbf{THE ANNIHILATOR GRAMMAR, BOTH DIRECTIONS (machine census):}\qquad\text{for integer windows}\ d\ \text{and monic rational}\ P=\sum_tp_tz^t:$$
$$\boxed{\ P(\sigma)\,d=0\ \ \text{CYCLICALLY}\qquad\iff\qquad P(\zeta^{-m})\cdot D_m=0\ \ \text{for EVERY spectral cell}\ m\ }$$
$$\text{via the spectral action identity}\ \mathrm{DFT}(P(\sigma)d)_m=P(\zeta^{-m})D_m\ (\text{entrywise; the DFT diagonalizes the shift — the whole mechanism});\ \ 5\ \text{grammar witnesses (period-4 under}\ \sigma^2{+}1,\ \text{constants under}\ \sigma{-}1,\ \text{period-3 under}\ \sigma^3{-}1,\ \text{the alternation under}\ \sigma{+}1,\ \text{period-4 at}\ n{=}8);$$
$$\text{the wrong-law adversarial}\ (\sigma^2{-}1\ \text{on the period-4 pattern) fails BOTH sides simultaneously — the grammar could misfire and does not.}$$
$$(6)\quad\textbf{THE BOUNDARY DEFECTS (machine):}\qquad d_j=j^2\ \text{on}\ n=4:\ \ \text{the CYCLIC third difference}\ (\sigma-1)^3d=(0,-16,24,-8)\ \text{EXACTLY — supported at the wrap, where the window ends — while the OPEN interior equation holds exactly}\ (9-12+3-0=0);$$
$$\text{the census over}\ 18\ \text{quadratic windows}\ (n=6,\ \text{exact Fraction grids): every interior cell of}\ (\sigma-1)^3\ \text{vanishes identically — the defects are THE WRAP,}\ \neg\text{the law};\qquad\text{the read-level motion comes with its exact boundary terms: nothing is extrapolated across the gap}\ [\mathrm{D\text{-}RS4}\text{'s deferral, ledger-side shadow}].$$
$$(7)\quad\textbf{THE WINDOW ECONOMY AND THE RECONSTRUCTION (machine):}\qquad n\ \text{pings pin monic laws of degree}\ k\ \text{by exact linear solve on the}\ n{-}k\ \text{interior equations — uniquely identifiable while}\ n{-}k\ge k\ (k\le n/2):$$
$$\text{the minimal annihilators come back EXACTLY: constant}\to\sigma{-}1;\ \ \text{uniform}\to(\sigma{-}1)^2;\ \ \text{constant acceleration}\to(\sigma{-}1)^3;\ \ \text{period-4}\to\sigma^2{+}1\ \ (\text{each verified to kill the interior entrywise});$$
$$\text{the generic window}\ (3,1,4,1,5,9)\ \text{admits NO law of degree}\ \le2\ (\text{inconsistent below the threshold})\ \text{while its degree-3 fit exists — a FIT,}\ \neg\text{a LAW: minimality separates them};$$
$$\boxed{\ \text{THE EQUATION OF MOTION, RECONSTRUCTED FROM THE SPECTRUM:}\ \ P_{\min}(z)=\!\!\prod_{m:\ D_m\ne0}\!\!(z-\zeta^{-m})\ \ \text{has PURELY RATIONAL coefficients (the Galois pairing certified identically zero on the cyclotomic part) and equals the minimal law:}\ (1,0,-1,0)\to z^2{+}1;\ (5,5,5,5)\to z{-}1;\ (1,0,0,1,0,0)\to z^3{-}1;\ (2,-2,2,-2,2,-2)\to z{+}1\ }$$
$$(8)\quad\textbf{THE DIRECTIVE'S SENTENCE, EXACT — AND WHAT IT IS NOT:}\qquad n\ \text{radar syncs}\to\ \text{an integer window}\ [\mathrm{IT.79}];\ \ \text{its exact DFT}\to\ \text{the spectral support}\ (2)\text{--}(5);\ \ \text{the support}\to\ \text{the monic rational recurrence}\ (7)\ \text{— the ``equation of motion'' in closed form, zero fitted parameters};$$
$$\textbf{it is a READ of the formed family,}\ \neg\textbf{a dynamics:}\ \ \neg\text{a trajectory},\ \ \neg\text{a prediction beyond the window (continuation is a stationarity-class hypothesis;}\ \mathrm{D\text{-}RS4}\ \text{deferred)},\ \ \neg\text{a force law};$$
$$\text{the dynamical leg stays BARRED on three grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{IT.40}\text{–}\mathrm{IT.42};\ \mathrm{IT.66}(1);\ \mathrm{D\text{-}PJ7}\ \text{owed}];\qquad\text{count}\to\text{strength barred: a spectral line is a}\ \mathfrak q^0\ \text{count-ratio read,}\ \neg\text{a coupling}\ [\mathrm{BM.36}(3);\ \mathrm{FT.73}(5)];\qquad \mathrm{D\text{-}PJ4}\text{'s functional form stays UNFIXED (the classification stops at ingredients)}\ [\mathrm{IT.68}(4)].$$

**Req.** P1, P5, D0.9, C10 (Part 1); IT.40–IT.42, IT.50, IT.54(1), IT.60(1), IT.64(6), IT.66(1), IT.68(3),(4), IT.79, IT.80 (this level); BM.36(3), BM.134(5) (Part 4); FT.73(5) (Part 3); exact integer polynomial recursion, exact Fraction linear solves, exact cyclotomic ring arithmetic, Galois-involution homomorphism witnesses, deterministic window censuses [math; machine: `nradar_fft.py` §C1–C7, 7/7].

**Pf.**
$$(1)\text{--}(7):\ \ \text{the certifying markers C1--C7 — the cyclotomic recursion with the independent product re-multiplication; the character sum and the}\ 155\text{-window exhaustive round trip; the transport censuses; Parseval with the homomorphism witness; the annihilator grammar in both directions with the wrong-law adversarial; the defect row}\ (0,-16,24,-8)\ \text{and the}\ 18\text{-window quadratic census; the minimal-annihilator solves and the rational-coefficient reconstruction}\ [\text{machine C1--C7}];\qquad(8):\ \ \text{the assembly on}\ \mathrm{IT.79}\text{--}\mathrm{IT.80}\ \text{and the cited bars}.\ \blacksquare$$

**Phys.** The corpus has no differential calculus and needs none for this: the equation of motion
of a radar window is a polynomial. Build the cyclotomic rings out of integer coefficients alone,
transform the integer window exactly, and the shift becomes multiplication — so any recurrence the
window obeys shows up as the vanishing of spectral cells, and the product over the surviving cells
hands back the recurrence with rational coefficients, the Galois pairing doing the complex
cancellation for free. One ping gives a distance; two give a slope; three decide whether the slope
was a law; n decide every law up to half their length — and a window that obeys no short law says
so, its only "recurrence" a full-degree fit that is a description, not a discovery. The boundary
defects keep the honesty: where the window wraps, the law fails by exact integers, and nothing in
the grammar pretends otherwise. This is the read side of motion — the dynamical side still waits
on its deficit, and the tier does not touch it.

---

### IT.82 — The L(n) capacity side-row: the builder's identity adjudicated and placed, with credit

**Thm.**
$$(1)\quad\textbf{THE IDENTITY (machine re-run,}\ n=1..24\textbf{):}\qquad L(n):=\sum_{k=1}^{n}(k+1)\,2^{k}=n\,2^{\,n+1}\ \ \text{EXACT at every}\ n,\qquad\text{with the telescoping certificate}\ \ (k{+}1)2^{k}=k\,2^{k+1}-(k{-}1)2^{k}\ \ (\text{exact at every}\ k=1..39);$$
$$\text{the board totals reproduce:}\ \ L(1),L(2),L(3),L(4)=(4,\ 16,\ 48,\ 128).$$
$$(2)\quad\textbf{THE QUOTIENT AND THE LOCK RE-READ (machine):}\qquad\frac{L(n)}{n}=2^{\,n+1}=D_{\mathrm{tick}}(n)\ \ [\mathrm{CT0.5}]\ \ \text{EXACT and INTEGRAL at every}\ n=1..24\ (n\mid L(n)\ \text{census});$$
$$\boxed{\ \frac{L(4)}{4}=32>16=C_{\mathrm{cap}}\ [\mathrm{CT0.6};\ \mathrm{D0.9}]\ }\qquad\text{the capacity lock gains a config-census FACE beside the register-accounting one — both pure counts.}$$
$$(3)\quad\textbf{THE BRIDGE FLAG (the adjudication's second half):}\qquad\text{``per-channel configuration states ARE the tick load'' is a READING — a PARALLEL, NOT ADOPTED:}$$
$$\text{configuration states}\ \ne\ \text{edge bits}\ [\mathrm{CT0.9}]\ \ne\ \text{slot counts};\qquad\mathrm{CT0.5}\ \text{defines}\ D_{\mathrm{tick}}\ \text{by REGISTER ACCOUNTING (one direction per admissible classical alternative}\ [\mathrm{C10}]),\ \text{and NO config-census route to it is declared anywhere in the record};$$
$$\text{the parallel-not-identification discipline applies}\ [\mathrm{BM.134}(5);\ \mathrm{IT.69}(5)\ \text{pattern}]:\ \text{the arithmetic identity is the row; the semantics stay a reading until a route is derived or declared — neither is done here.}$$
$$(4)\quad\textbf{ATTRIBUTION AND PROVENANCE:}\qquad\text{the identity arrives from the builder's teacher-board audit}\ (\text{comms}\ \texttt{0011}\ \S3)\ \text{with the kernel receipt}\ \texttt{TickHop.lean};\ \text{adjudicated by execution in comms}\ \texttt{0012}\ \text{and placed here with credit}\ [\mathrm{IT.63}\ \text{attribution pattern}];\ \text{the board's own slips (the}\ n{=}3\ \text{qubit/state conflation, the}\ \sigma{=}{-}1\ \text{REAL-class mislabel, the out-of-domain}\ \varepsilon_q\ \text{margin query against}\ \mathrm{CT0.8}\text{'s}\ [0,\tfrac14))\ \text{are audit-side record, corrected at source, imported by no clause.}$$
$$(5)\quad\textbf{THE RADAR CONTEXT (why the row rides with this tier):}\qquad\text{the per-ping register accounting of the}\ n\text{-fold conversation is}\ \mathrm{Cor}\ \mathrm{CT0.6a}\text{'s supply bound}\ \delta h\le4\,\delta\tau\ \text{through ONE pair channel};\ \ L(n)/n=D_{\mathrm{tick}}(n)\ \text{is the cumulative-config face of the same ladder}\ 2^{n+1}:\ \ \text{two count-reads of the capacity structure, neither a strength, neither a rate.}$$

**Req.** C9, C10, D0.9, CT0.5, CT0.6, CT0.6a, CT0.8, CT0.9 (Part 1); BM.134(5) (Part 4); IT.63, IT.69(5) (this level); the builder's `comms/0011` §3 and `TickHop.lean` (channel intake, credited in-tier); exact integer arithmetic, the telescoping certificate [math; machine: `nradar_fft.py` §D1–D2, 2/2].

**Pf.**
$$(1),(2):\ \ \text{the certifying marker D1 — the identity at every}\ n=1..24,\ \text{the certificate at every}\ k=1..39,\ \text{the totals, the quotient with the integrality census, the lock re-read}\ [\text{machine D1}];\qquad(3):\ \ \text{the flag carried in the tier text (machine text census}\ [\text{machine D2}])\ \text{on the cited grounds};\qquad(4),(5):\ \ \text{provenance and context rows}.\ \blacksquare$$

**Phys.** A teaching board counted configurations and found an exact integer where the capacity
ladder lives: the cumulative state count of the one-node tower is n times the tick load, and at
n=4 it re-reads the oldest lock in the corpus — thirty-two against sixteen — from the counting
side. The arithmetic is a row; the temptation is the bridge, and the bridge stays flagged: states
are not bits and not slots, and nothing in the record routes a configuration census into the
register accounting that defines the tick load. Placed with the credit where the credit is due,
beside the radar conversation whose own supply bound lives on the same ladder.

---

### IT.83 — The verdict: the system, the bars, the status

**Thm.**
$$(1)\quad\textbf{THE VERDICT TABLE (every component traced to its certifying marker or its frozen ground):}\qquad\begin{array}{l|l}\textbf{the component}&\textbf{the verdict}\\\hline\text{the}\ n\text{-fold radar family (formed reads, unique total order)}&\textbf{DERIVED — formed inside the issued declarations}\ [\mathrm{IT.79};\ \mathrm{A1}\text{--}\mathrm{A3}]\\\text{the position/velocity/acceleration faces}&\textbf{DERIVED — exact rational count-reads}\ [\mathrm{IT.80};\ \mathrm{B1},\mathrm{B2}];\ \text{window discipline: faces of the recorded interval,}\ \neg\text{instantaneous states}\\\text{the exact cyclotomic DFT (inversion, transport, Parseval)}&\textbf{DERIVED — a read-window algebra}\ [\mathrm{IT.81}(1)\text{--}(4);\ \mathrm{C1}\text{--}\mathrm{C4}]\\\text{the annihilator grammar (both directions) + the boundary defects}&\textbf{DERIVED}\ [\mathrm{IT.81}(5),(6);\ \mathrm{C5},\mathrm{C6}]\\\text{the ``equation of motion'' = the minimal annihilator / the spectral-support reconstruction}&\textbf{DERIVED AS A READ}\ [\mathrm{IT.81}(7),(8);\ \mathrm{B3},\mathrm{C7}]\ \text{—}\ \neg\text{a dynamics,}\ \neg\text{a prediction}\\\text{the}\ L(n)\ \text{capacity rows}&\textbf{DERIVED (counts); the BRIDGE flagged a READING/parallel,}\ \neg\text{adopted}\ [\mathrm{IT.82};\ \mathrm{D1},\mathrm{D2}]\\\text{any new act needed for the system}&\textbf{NONE — the vocabulary is the issued one}\ [\mathrm{IT.79}(4)];\ \ \mathrm{D\text{-}RS4}\ \text{stays deferred (per ping)},\ \ \mathrm{D\text{-}PJ7}\ \text{stays owed alone}\\\text{the dynamical leg (a photon-mediated conversation, rates, forces from spectra)}&\textbf{BARRED as formed — three grounds}\ \mathrm{O1/O2/O4}\ [\mathrm{IT.40}\text{–}\mathrm{IT.42};\ \mathrm{IT.66}(1)]\\\text{reading couplings/masses off spectral lines}&\textbf{BARRED — count}\to\text{strength}\ [\mathrm{BM.36}(3);\ \mathrm{FT.73}(5)];\ \ \text{capacity-Fourier reads}\ \textbf{BARRED}\ [\mathrm{IT.54}(1);\ \mathrm{D0.9};\ \mathrm{C10}]\end{array}$$
$$(2)\quad\textbf{THE BAR-CHECK (machine):}\qquad\begin{array}{l|l}\textbf{the bar}&\textbf{the verdict}\\\hline\mathrm{P1}&\textbf{HONORED}: \neg\text{a new dimensionful scale —}\ n,\ j,\ \text{the window entries are counts;}\ \zeta_n\ \text{is a root of unity; the faces are}\ \mathfrak q^0\ \text{count ratios; the chart faces keep the existing monomials symbolically; the rational witnesses are PARAMETERS}\ [\mathrm{IT.59}(2)\ \text{pattern}]\\\mathrm{P5}&\textbf{HONORED}: \text{zero decimal numeric tokens in the tier (machine scan, word-bounded, live-witness self-tested); every numeric an exact integer or Fraction; the spectra are exact cyclotomic rationals; no value issued}\\\text{the species exclusion}&\textbf{CLEAN}: \neg\text{an external-framing token; species names}\ \neg\text{used at all in this tier}\\\text{the transit bar}&\textbf{STANDS on three grounds}: \neg\text{an amplitude, vertex, weight or rate; the FFT grammar is a read-window algebra,}\ \neg\text{a propagator}\\\text{the incommensurability bar}&\textbf{HOLDS}: \text{the difference/DFT operators are}\ \mathbb Q\text{-linear PER FACE; the four symbol sets meet pairwise in the empty set}\ [\mathrm{IT.80}(5)];\ \text{the mixed loci remain exactly three}\ [\mathrm{IT.4}(2)]\\\text{the M freeze}&\textbf{HONORED}: \neg\text{a clause touches}\ M\ \text{or}\ X=M\otimes M\ [\text{the}\ \mathrm{IT.37}\text{–}\mathrm{IT.39}/\mathrm{IT.43}\text{–}\mathrm{IT.45}/\mathrm{IT.52}\ \text{records stand, cited by no derivation here}];\ \text{the Architect's restructuring pending}\\\text{the frozen canon}&\textbf{CITED, NEVER EDITED}\ [\mathrm{AT.63}(2)]\end{array}$$
$$(3)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\quad\text{the tier issues NO DECLARATION (machine-scanned});\qquad\S\mathrm{Cal\text{-}IT}\ \text{stays VALUE-FREE and unchanged};\qquad\text{the register stands as}\ \mathrm{IT.66}(4)\ \text{records it: issued}\ \mathrm{D\text{-}PJ1}\text{–}6,\ \mathrm{D\text{-}RS1}\text{–}3,\ \mathrm{D\text{-}RS6}\text{–}7,\ \text{the}\ \mathrm{BM.113}(6)\ \text{sync};\ \text{deferred}\ \mathrm{D\text{-}RS4};\ \textbf{owed}\ \mathrm{D\text{-}PJ7}\ \textbf{alone}\ +\ \text{the three sub-debts}.$$
$$(4)\quad\textbf{the open-row state:}\qquad\boxed{\ \textbf{NO new open row}\ };\qquad\mathrm{IT\text{-}O1}\ \text{UNCHANGED (three grounds; deficit}\ 1'\ \text{— this tier constructs no amplitude, and the}\ n\text{-radar system is read-level throughout)};\ \ \mathrm{IT\text{-}O2}\ \text{UNCHANGED (the binding value)};\ \ \mathrm{IT\text{-}O5}\ \text{UNCHANGED};$$
$$\text{the residues this tier names are scope rows, not gaps: the window discipline}\ (\mathrm{IT.80}(1)),\ \text{the per-ping}\ \mathrm{D\text{-}RS4}\ \text{boundary}\ (\mathrm{IT.80}(5)),\ \text{the fit-vs-law minimality clause}\ (\mathrm{IT.81}(7))\ \text{— all inside the formed family.}$$
$$(5)\quad\textbf{the machine state:}\qquad\texttt{nradar\_fft.py}\to\textbf{19/19 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{24 checkers, 412 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{23 Part 6 documents PASS};$$
$$\text{the Level-5 closed suite untouched}\ (37/643);\qquad\text{index/tags/Summary}\ \neg\text{regenerated — promotion stays an Era-2-closure act}\ [\mathrm{AT.63}(4)].$$
$$(6)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier IT-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact; and an equation of motion read off a window is the window's grammar, not the world's engine}\ [\mathrm{AT.39}(8);\ \mathrm{IT.1}(8)\ \text{'s standing box, re-cited}]\ }$$

**Req.** P1, P5, D0.9, C10 (Part 1); BM.36(3), BM.134(5) (Part 4); FT.73(5) (Part 3); IT.4(2), IT.37–IT.39, IT.40–IT.42, IT.43–IT.45, IT.50, IT.52, IT.53, IT.54(1), IT.56, IT.59(2), IT.60(1), IT.64, IT.65, IT.66, IT.68, IT.69(5), IT.79–IT.82, IT-O1, IT-O2, IT-O5 (this level); AT.39(8), AT.44(1), AT.63(2),(4) (Level 5); the full checker, the level runner and the level gate re-run end to end [math; machine: `nradar_fft.py` §E, 3/3].

**Pf.**
$$(1),(2):\ \ \text{the row-wise assembly of}\ \mathrm{IT.79}\text{–}\mathrm{IT.82}\ \text{with every verdict traced to its certifying marker (A1--A3, B1--B4, C1--C7, D1--D2) or its frozen ground, and the tier scans (the decimal scan with its live-witness self-test, the act-handle scan, the symbol-set census)}\ [\text{machine E1, E2}];$$
$$(3)\text{--}(6):\ \ \text{the declaration scan, the open-row assembly, the runner and the gate re-run end to end}\ [\text{machine E2, E3}].\ \ \text{No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** The directive asked for a system, and the system is built — out of nothing but what the
record already declared: n echoes of one ledger, ordered uniquely, differenced into exact rational
slopes, transformed in rings of integers and roots of unity, and read back as the polynomial that
generates the window. Position from one ping, velocity from two, the law from as many as its
degree demands, and the honest refusals printed beside each gift: a fit is not a law, a window is
not a world, a boundary defect is not a smoothness assumption, and a spectrum is not a coupling.
The dynamical conversation — photons really flying, forces really pushing — stays where it was,
behind three grounds and one owed act. What moved is the read side: the corpus can now watch an
integer sequence and name its equation of motion exactly, in closed form, with zero floating
point, and say precisely where the naming stops.

---

## §Cal-IT — unchanged (value-free)

**No act at this tier.** Tier IT.23 issues no declaration (machine-scanned at IT.83(3)): it is a
construction tier on the vocabulary declared at Tiers IT.17/IT.20 and formed at IT.21. The act
register stands as IT.66(4) records it — issued: D-PJ1–6, D-RS1–3, D-RS6–7, the BM.113(6) sector
sync; deferred: D-RS4 (now applying per ping to the chart faces of IT.80(4)); owed: **D-PJ7
alone** + the three sub-debts. **No calibration parameter is added, valued, or re-scoped**: the P1
scale slot, $\varepsilon_q$ (AT-O27), $e_0$ [EM.25(7)], $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$
[A-BM.9], $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$, the $\mu_{\mathrm{ch}}$ family (Cal-F), the read
rules (M1′)–(M3′) [AT.54(6)], the lift/vielbein/P4 profile [AT.63(3)], and the mass-read route
choice [IT.14(3); BM.30(5)] all stand unchanged; the rational witnesses inside `nradar_fft.py` are
exact Fraction PARAMETERS [IT.59(2) pattern], not issued values; the cyclotomic rings carry no
scale ($\zeta_n$ is a root of unity). The Calibration Era stays **deferred** [AT.63(4)].

## §Open-IT additions from Tier IT.23

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.23 opens **no row**. The n-fold radar system is a formed read family extension inside the issued declarations [IT.79(4)]; the kinematic faces and the cyclotomic DFT grammar are read-level algebra [IT.80; IT.81]; the equation-of-motion read carries its own scope rows (window discipline; fit-vs-law minimality; per-ping D-RS4 boundary) — scope, not gaps [IT.83(4)]; the L(n) bridge stays a flagged READING/parallel [IT.82(3)]; the dynamical side stays at IT-O1 (three grounds; deficit 1′ = D-PJ7 owed) — untouched by this tier | IT.79(4); IT.80(1),(5); IT.81(7),(8); IT.82(3); IT.83(1),(4) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4); IT.57(5); IT.60(4); IT.62(4);
IT.66(6); IT.70(1); IT.78(4)]: (IT-O1) the formed transit-leg amplitude — three grounds, deficit 1′
[IT.41(2)]; (IT-O2) the binding value — the three IT.27(2) constructions (the δ-glue input named at
IT.69(6)); (IT-O5) the isotope cutoff — the dynamical side at IT-O1; AT-O30/AT-O32 the heavy
censuses; the owed route choice [IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the
Level-5 inheritance [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.24: the parity of the seal and the contact gate — why the baryon carries the lock, and where the one readable vertex of it can be

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.24 — the disposition tier for the
Architect's concept queue: **concept/0002 (the Baryonic Lock / Census inversion) MERGED**,
**concept/0004 (the Janus balance knot) MERGED**, **concept/0005 (the Observation Gate) PROMOTED
and delivered**. All three were adjudicated in probe space against the frozen rows before this tier
was written; this tier records what survived, in the corpus's own vocabulary, on formed ground.
**The governing results are two parities and one biconditional.** (i) *Grammar parity*: Census FT.63's
**even-$\varepsilon$ theorem** — an attachment set of even cardinality admits only an even number of
$\varepsilon$-triples. (ii) *Embedding parity*, new here: $\sum_v n(v)=2|E_{\mathcal R}|$ forces an
**even** count of trivalent vertices on any sealed admissible network. (iii) *The contact
biconditional*, read out of Census FT.62(1): $n(v)=3$ **iff** $v$ has one channel and exactly one
single-directed-edge contact. The Architect's disposition names the load-bearing result: **the JOIN of
(i) and (ii)** — two independent $\mathbb Z_2$ obstructions, derived from unrelated machinery, that
agree. **Tags.** IT.84–IT.88. **Pattern.** the read-tier / adjudication shape (IT.16, IT.22's
pattern): no new primitive, no new act, no new open row — frozen rows read at their own loci.
**Status.** discovery-phase working tier. No declaration issues at this tier (machine-scanned at
IT.88); §Cal-IT stays value-free and unchanged; no clause of Parts 1–4, of Level 5's closed record,
or of Tiers IT.1–IT.23 is modified [AT.63(2)]. No measured value enters [P5]; no new dimensionful
scale [P1]; species names stay quoted and no card row is a species identification
[Def-BM.2; FT.49(6): *"structural correspondence, $\neg$particle identification"*].
**Machine.** `era2/level6_isotopic/checks/parity_contact_gate.py` → **exact** (integers and
Fractions only; exhaustive digraph enumeration; no randomness, NO floating point in any assertion);
`run_all_level6.py` → the full level suite; `check_level6_format.py` → the gate over all twenty-four
Part 6 documents. Probe-space antecedents, retained as the working record: `baryonic_lock.py` (69
markers), `contact_gate.py` (60 markers), `causality_topology.py` (147 markers), each with a mutation
test certifying that every load-bearing negative can fail (7/7, 7/7-as-extended, 6/6).
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's dispositions, executed in full: concept/0002's parity theorem with the
FT.63 join as the headline and the enforced bar (IT.84, IT.87); concept/0005's contact-gating theorem
and the photon/gluon rung-parity census, called *"a priority physics derivation"* (IT.85);
concept/0004's three-locus resolution placed beside BM.7(1)/D2.11 (IT.86); **both** adopted
topological reads flagged as structural readings over exact Census referents (IT.87); the verdict,
bars and scans (IT.88). **The M exploration [concept/0003] is EXPLORATORY ONLY and the F=ma probe
remains PAUSED** — nothing of either is committed here or cited as a premise.

---

### IT.84 — The two parities and their join: an $\varepsilon$-sealed baryon-type floor cannot be lock-free

**Thm.**
$$(1)\quad\textbf{EMBEDDING PARITY (new at this tag).}\qquad \Gamma=(V,E)\ \text{finite},\ E\subseteq V\times V\ [\mathrm{A7}];\qquad n(v)=\partial^{\leftarrow}(v)+\partial^{\rightarrow}(v)\ [\mathrm{D0.8}]:$$
$$\boxed{\ \sum_{v\in V}n(v)\ =\ 2\,|E_{\mathcal R}|\ \ \text{is EVEN}\ }\qquad[\text{each directed real edge contributes exactly }1\text{ to one }\partial^{\rightarrow}\text{ and }1\text{ to one }\partial^{\leftarrow}]$$
$$\text{hence if every vertex is channel-admissible}\ (n(v)\le3\ [\mathrm{CT0.11}])\ \text{and no vertex is a lone end}\ (n(v)\ne1),\ \text{then every}\ n(v)\in\{0,2,3\}\ \text{and}$$
$$\boxed{\ 3k+2m=2|E_{\mathcal R}|\ \Longrightarrow\ k:=\#\{v:\ n(v)=3\}\ \text{is EVEN}\ }$$
$$\text{the two hypotheses are LOAD-BEARING, machine-verified both ways: permitting}\ n(v)=1\ \text{produces odd}\ k\ \text{immediately};\ \text{raising the ceiling to}\ 4\ \text{destroys the theorem}. $$
$$(2)\quad\textbf{the sealed case, sharply.}\qquad \neg\exists\ \text{dangling ledger boundary}\implies\forall\ \text{ends sealed}\ [\mathrm{D2.11},\ \text{read at}\ \mathrm{EM.11}\ \text{Pf}];\qquad \text{a lone attachment is never sealed}\ [g(1)=0,\ \mathrm{CT3.17a}(1),(2)];$$
$$\text{one dangling attachment anywhere zeroes the entire colour sector}\ [\mathrm{CT3.18}];\qquad\text{each seal joins a target-end to a source-end at a COMMON vertex}\ [\mathrm{D1.2};\ \mathrm{D1.4}:\ t(e_i)=s(e_{i+1})];$$
$$\text{the pairing covers every end exactly once}\ [\mathrm{D1.3}]\ \Longrightarrow\ \partial^{\leftarrow}(v)=\partial^{\rightarrow}(v)\ \Longrightarrow\ n(v)=2\,\partial^{\leftarrow}(v)\ \text{is EVEN at every vertex}.$$
$$\textbf{exhaustive census (machine): on every sealed digraph with}\ |V|=4,\ \textbf{every occurring vertex type is diagonal}\ (d,d),\ \text{and the extreme types}\ (0,3),(3,0)\ \textbf{never occur}$$
$$[\mathrm{FT.62}(5)\ \text{states the same for}\ d\ge2:\ \text{``bidirectional-skeleton vertices with}\ d\ge2\ \text{channels have type}\ (d,d)\text{''}].$$
$$(3)\quad\textbf{the}\ \varepsilon\textbf{-seal needs three colour vertices at DISTINCT nodes.}\qquad B=\varepsilon_{ijk}q^iq^jq^k\ [\mathrm{D3.9};\ \mathrm{CT3.15};\ \mathrm{CT3.17};\ \mathrm{CT3.18}\ \text{``minimal singlets''}];$$
$$\pi_C(v)=\text{the OTHER members of}\ v\ \text{'s elementary contraction group — TWO for a (anti)baryon triple}\ [\mathrm{D2.14}];$$
$$|\mathrm{Colour}(\Sigma)|=1\implies\mathcal C(\Sigma;C)=0\quad[\mathrm{CT3.17a}(1):\ \text{``a contraction partner is a distinct node — A1:}\ p\ne q\ \text{— hence}\ \pi_C(v)\not\subseteq\{v\}\text{''}].$$
$$(4)\quad\textbf{THE JOIN (the load-bearing result, per the Architect's disposition).}\qquad \text{grammar parity}\ [\mathrm{FT.63}\ \text{``even-}\varepsilon\ \text{theorem''}:$$
$$V\ \text{even}\implies\text{every grouping of the attachment set has an EVEN number}\ b\ \text{of}\ \varepsilon\text{-triples},\ 2a+3b=V]$$
$$\text{and embedding parity}\ (1)\ \text{are TWO INDEPENDENT}\ \mathbb Z_2\ \text{obstructions derived from unrelated machinery —}$$
$$\text{a labelled-set-partition count}\ [\mathrm{CT3.17a}(2)]\ \text{versus a degree-sum identity}\ [\mathrm{D0.8}]\ \text{— and THEY AGREE.}$$
$$\boxed{\ \text{a sealed admissible network cannot host a single}\ \varepsilon\text{-triple: at least one colour vertex of any}\ \varepsilon\text{-sealed baryon-type floor has}\ n\ge4,\ \text{hence is}\ D^-\text{-configured}\ [\mathrm{CT4.1},\ \mathrm{D4.1}]\ }$$
$$(5)\quad\textbf{the mod-6 corollary and the fermion/boson dichotomy.}\qquad \text{a pure-}\varepsilon\ \text{grouping exists iff}\ 3\mid|\mathrm{Colour}|\ [\mathrm{CT3.17a}(2);\ g_\varepsilon\ \text{nonzero exactly where}\ 3\mid N];$$
$$\text{embedding parity requires}\ |\mathrm{Colour}|\ \text{even};\qquad\gcd(2,3)=1\ \Longrightarrow\ \boxed{\ 6\ \big|\ |\mathrm{Colour}|\ \ \text{for a lock-free pure-baryonic seal}\ }$$
$$|\mathrm{Colour}|=2\ (\delta\text{-pair, meson-type})\ \text{is EVEN}\ \Longrightarrow\ \text{parity-allowed lock-free};\qquad |\mathrm{Colour}|=3\ (\varepsilon\text{-triple, baryon-type})\ \text{is ODD}\ \Longrightarrow\ \text{forbidden};$$
$$\text{so Census FT.35's Rmk -- ``Composite fermion structure and saturation content are born together'' -- is promoted from a census observation to a theorem},$$
$$\text{and FT.42}(2)\text{'s ``the lock-free family is the unidirectional one''}\ [\mathrm{FT.28};\ \mathrm{FT.32};\ \mathrm{FT.62}(3)]\ \text{is explained: that family carries no}\ \varepsilon\text{-seal}. $$

**Req.** A7; D0.1, D0.8, D1.2, D1.3, D1.4, D2.11, D2.14, D3.1, D3.8, D3.9, D4.1 (Part 1); CT0.11, CT0.11a, CT0.11b, CT0.13 (Part 1); CT3.15, CT3.17, CT3.17a, CT3.18, CT4.1, CT4.1a (Part 2); FT.28, FT.32, FT.35, FT.42(2), FT.62(3), FT.63 (Census); EM.11 Pf (Part 2); exhaustive digraph enumeration, the handshaking identity, exact integer partition arithmetic [math; machine: `parity_contact_gate.py` §A–§C].

**Pf.**
$$(1):\ \ \mathrm{D0.8}\ \text{additivity gives}\ \textstyle\sum_v n(v)=2|E_{\mathcal R}|\ \text{on every finite digraph (machine: exhaustive}\ |V|=2,3,4);\qquad n(v)\le3\ [\mathrm{CT0.11}]\ \wedge\ n(v)\ne1\implies n(v)\in\{0,2,3\}$$
$$3k+2m=2|E_{\mathcal R}|\implies 3k\ \text{even}\implies k\ \text{even (machine: zero odd-}k\ \text{witnesses over all admissible dangling-free digraphs,}\ |V|\le5);\qquad\text{both hypotheses load-bearing (machine: adversarial mutations redden the claim)}$$
$$(2):\ \ \text{the cited clauses give}\ \partial^{\leftarrow}(v)=\partial^{\rightarrow}(v)\ \text{vertex-wise};\qquad\text{machine: exhaustive over all sealed digraphs with}\ |V|=4\ \text{— every type diagonal,}\ (0,3),(3,0)\ \text{absent}$$
$$(3):\ \ \mathrm{CT3.17a}(1)\ \text{verbatim;}\ \mathrm{D2.14}\ \text{gives}\ |\pi_C(v)|=2\ \text{for a baryon triple, so the group has three members at three distinct nodes}$$
$$(4):\ \ (1)+(2)+(3):\ \ \text{three colour vertices, each admissible}\implies\text{each}\ n=3\ [\mathrm{CT0.13}\wedge\mathrm{CT0.11}]\implies k=3\ \text{odd},\ \text{contradicting}\ (1);\ \ \text{so some colour vertex has}\ n\ge4\implies D^-\ [\mathrm{CT4.1},\ \mathrm{D4.1}]$$
$$(5):\ \ \mathrm{CT3.17a}(2)\ \text{closed form}\ g(N)=\sum_{2a+3b=N}\frac{N!}{a!\,b!\,2^{a}6^{b}}\ \text{re-derived exactly:}\ g(1..7)=(0,1,1,3,10,25,105),\ g(6)=25=15+10\ \text{as the canon splits it};$$
$$\text{the same formula independently reproduces}\ g(8)=385\ [\mathrm{FT.42}(5)\ \text{cube card}]\ \text{and}\ g(9)=1540=1260+280\ [\mathrm{Def\text{-}H.32}\ \text{'s grouping sectors}]\ \text{— a cross-era double entry on the grammar}.\ \blacksquare$$

**Phys.** Two counting arguments that have nothing to do with each other — how many ways attachments
group, and how many edge-ends a graph has — both say the same thing: **an odd number of baryon
triples cannot be seated.** The Census knew the grammar half; the graph supplies the embedding half;
their agreement is the result, and it is the reason a baryon is never merely *found* to carry dark
content but *must*. The meson escapes because two is even. That is the whole asymmetry between
bosonic and fermionic colour structure, and it is a parity fact about the number three.

---

### IT.85 — The contact-gating theorem and the exact photon/gluon rung-parity census

**Thm.**
$$(1)\quad\textbf{the rung-correction law is a BICONDITIONAL at the hosting rung.}\qquad \text{Census FT.62}(1)\ \text{``the bidirectional rung audit (correction theorem)'' freezes:}$$
$$\text{dark}\ n(v)=2d;\qquad\text{single-directed-edge contact}\ n(v_1)=2d+1;\qquad\text{bidirectional contact}\ n(v_1)=2d+2.$$
$$\text{colour HOSTS exactly at}\ n=3:\qquad \mathrm{strong}\in\mathcal A(3)\setminus\mathcal A(2)\ [\mathrm{CT0.13}];\qquad \iota_n\ \text{exists exactly for}\ n\le3\ [\mathrm{CT4.4a}(1)];\qquad \mathcal H^{(n)}_{\mathrm{slot}}\cong\mathbb C^n\ [\mathrm{D3.1}]$$
$$\text{integer solution census of the three branches at}\ n=3:\qquad 2d=3\ \text{— NO solution};\qquad 2d+2=3\ \text{— NO solution};\qquad 2d+1=3\ \text{— the UNIQUE solution}\ d=1$$
$$\boxed{\ n(v)=3\ \Longleftrightarrow\ v\ \text{has one channel}\ (d=1)\ \text{and exactly one single-directed-edge contact}\ }$$
$$(2)\quad\textbf{THE CONTACT BUDGET.}\qquad \text{one contact promotes at most one vertex, so}\qquad \#\{\text{colour-hosting vertices}\}\ \le\ \#\{\text{single-directed-edge contacts}\}$$
$$\text{with equality iff each contact sits on a}\ d=1\ \text{vertex};\qquad\text{a sealed (contact-free) interior can SEAL but NEVER HOST}\ [\mathrm{CT4.4a}(3):\ \text{``hosting dies at rung 3; sealing persists at every rung''}],$$
$$\text{sharpened: on a sealed interior, hosting never happens at all.}$$
$$(3)\quad\textbf{a bidirectional contact never opens the gate — it deepens the lock.}\qquad 2d+2\ \text{is even for every}\ d,\ \text{so it can never equal the odd hosting rung}\ 3;\ \text{for}\ d\ge1\ \text{it is}\ \ge4,\ \text{hence locked}\ [\mathrm{CT4.1}].$$
$$\text{instance (machine):}\ \Sigma_\triangle\ [\mathrm{FT.49}]\ \text{is observed by the fourth vertex through SIX boundary edges — two per vertex, i.e. bidirectional contacts —}$$
$$\text{so}\ n(A)=n(B)=n(C)=6,\ O(6)=112,\ \text{EVERY vertex}\ D^-\text{-configured, and colour hosting is ZERO.}\qquad\text{Observing a baryon symmetrically does not make it readable; it buries it deeper.}$$
$$(4)\quad\textbf{THE BARYONIC LOCK IS A CONTACT DEFICIT: three needed, one supplied.}\qquad \text{an}\ \varepsilon\text{-triple needs three colour vertices at distinct nodes}\ [\mathrm{IT.84}(3)],\ \text{so a lock-free baryon needs THREE single-directed contacts.}$$
$$\Sigma_{12}\ [\mathrm{FT.35}]\ \text{has exactly ONE}\ \Longrightarrow\ \text{exactly one of its three colour vertices}\ (p_1)\ \text{is admissible at}\ n=3,\ \text{and}\ q_1,p_2\ \text{lock at}\ n=4\ [\mathrm{FT.35}(4)];$$
$$\Sigma_\triangle\ \text{has none of the right kind}\ (3);\qquad\text{so NO computed cell realizes a lock-free baryon, and the deficit is exactly the contact count.}$$
$$(5)\quad\textbf{a lock-free baryon-type triple IS constructible — witness (machine).}\qquad \text{three cores, each in a}\ d{=}1\ \text{bidirectional channel with a partner, plus ONE single-directed contact into each core from its own endpoint:}$$
$$|E|=9;\qquad n=(3,3,3\,|\,2,2,2\,|\,1,1,1);\qquad \sum_v n(v)=18=2|E|;\qquad \text{locked vertices}=0;\qquad \text{every hosting vertex has type}\ (2,1)$$
$$\text{this does NOT contradict IT.84: each contact contributes oddness at BOTH its ends, so the odd-rung count stays even, and IT.84}(1)\text{'s dangling-free hypothesis does not apply.}$$
$$(6)\quad\textbf{THE PHOTON/GLUON RUNG-PARITY CENSUS}\ [\mathrm{D3.7}:\ \text{photon}:=\text{trivial chain}\subseteq V_2;\ \ \text{gluon}:=\text{trivial chain}\cap V_3\ne\varnothing],\ \text{over}\ 15\ \text{floor variants:}$$
$$\begin{array}{c|c|c}
\text{floor variant} & V_2\ (\text{photon rung}) & V_3\ (\text{gluon rung})\\ \hline
\text{dark},\ d=1\ (\text{digon}\ \Sigma_{\min}) & \text{POPULATED},\ \text{type}\ (1,1) & \text{empty}\\
\text{dark},\ d\ge2\ (\text{polygon, Platonic}) & \text{empty} & \text{empty}\\
\text{single-directed contact at}\ d=1 & \text{empty} & \text{POPULATED — exactly one vertex}\\
\text{single-directed contact at}\ d\ge2 & \text{empty} & \text{empty}\ (n=2d+1\ge5)\\
\text{bidirectional contact, any}\ d\ge1 & \text{empty} & \text{empty}\ (n=2d+2,\ \text{even})
\end{array}$$
$$\boxed{\ \text{photons need no contact; gluons cannot exist without one}\ }\qquad\text{in the entire computed Census EXACTLY ONE floor carries a rung-3 vertex:}\ \Sigma_{12}\text{'s observer contact}\ p_1$$
$$\text{observing a Platonic floor does NOT open hosting}\ (2d+1\ge7\ \text{at}\ d\ge3)\ \text{and makes the lock strictly worse:}\ O(2d+1)>O(2d)\ \text{at every solid (machine).}$$
$$(7)\quad\textbf{FT.62}(2)\text{'s corrected lock table, all four columns re-derived exactly (machine):}\qquad \text{dark}\ \textstyle\sum_vO=(448,896,2976,2240,24384);$$
$$\text{observed (1 edge)}\ (576,1024,3488,2368,26432);\qquad O(2d+2)=(496,496,2032,496,8176);\qquad\text{their sums}\ (832,1280,4512,2624,30528).$$
$(8)\quad\textbf{THE GENERAL PARITY LEMMA, which subsumes}\ (1)\ \textbf{— and the scope of}\ (1)\textbf{, stated honestly.}\qquad\text{(builder's probe, adopted here; two independent machines agree)}$
$\sum_v n(v)\ =\ 2C+h\qquad\Bigl[C=\#\{\text{closed edges}\},\quad h=\#\{\text{open ends}\}\Bigr]\qquad[\mathrm{D0.8}\ \text{additivity};\ \mathrm{A7}]$
$\Longrightarrow\qquad \boxed{\ \#\{v:\ n(v)\ \text{odd}\}\ \equiv\ h\ \ (\mathrm{mod}\ 2)\ }\qquad\text{and for an all-trivalent core}\ (n(v)=3\ \forall v):\quad 3k=2C+h\ \Longrightarrow\ k\equiv h\ (\mathrm{mod}\ 2)$
$h=1\ (\text{one jutting edge}):\ k\in\{1,3,5,7,\ldots\}\ \text{ODD};\qquad h=0\ (\text{sealed}):\ k\ \text{EVEN — and by}\ (2)\ \text{a sealed network has every}\ n(v)\ \text{even, so}\ k=0.$
$\textbf{the sharpest form of the gate: colour hosting requires an ODD rung; an odd rung requires an OPEN END; therefore a sealed network hosts nothing at all.}$
$\textbf{the single jutting edge is the UNIQUE parity repair that makes an all-trivalent core legal} — \text{an object that must communicate outward has exactly one degree of parity freedom, and it is the open end.}$
$\text{machine census (builder, adopted):}\ h=1\ \text{with}\ k=2,4,6\ \text{gives ZERO configurations — FORCED by the lemma, not an enumeration accident};\ k=1\ \text{gives}\ 1\ \text{class},\ k=3\ \text{gives}\ 5,\ k=5\ \text{gives}\ 26.$
$(9)\quad\textbf{the scope correction this forces on}\ (1).\qquad (1)\text{--}(7)\ \text{are derived for BIDIRECTIONAL}\ d\text{-regular interiors — the families Census FT.62 audits — where}\ 2d=3\ \text{and}\ 2d+2=3\ \text{have no solution, so the single-directed contact is the ONLY route to}\ n=3.$
$\text{In the GENERAL ledger grammar}\ n=3\ \text{is also reachable as}\ d^{\mathrm{bi}}{=}0,\ d^{\mathrm{uni}}{=}3\ [\mathrm{CT0.11b}:\ n(v)=2d^{\mathrm{bi}}_S(v)+d^{\mathrm{uni}}_S(v)\le3],\ \text{i.e. type}\ (3,0)/(0,3)\ \textbf{with open ends} — \text{which}\ (2)\ \text{excludes ONLY in the sealed case}.$
$\text{so}\ (1)\ \text{is a SPECIAL CASE of}\ (8)\ \text{on the FT.62 floor families,}\ \neg\text{a general biconditional};\qquad\text{the register caution is}\ \mathrm{BM.134}(5)\text{'s: SLOT trivalence}\ (\varepsilon_{ijk}\ \text{rank}\ 3\ [\mathrm{D3.9}])\ \text{is}\ \neg\text{LEDGER valence}\ n(v)=3\ [\mathrm{D0.8}],\ \text{and the two currencies are never summed}.$

**Req.** A7; D0.8, D3.1, D3.9 (Part 1); CT0.11, CT0.11b, CT0.13 (Part 1); CT3.1, CT4.1, CT4.4a (Part 2); D3.7 (Part 1); BM.134(5) (Part 4 — the register caution at (9)); FT.28, FT.32, FT.35, FT.42, FT.49, FT.62(1)–(3), FT.63 (Census); Def-H.20, Def-H.35 (Census); exhaustive and constructive graph enumeration, exact integer ladder arithmetic, the modular solution census of the general parity lemma at (8) [math; machine: `parity_contact_gate.py` §D–§G; the (8) census is the builder's `protruding_edge_census.py`, independently re-verified here]. *The general parity lemma at (8) is the builder's probe result, adopted; (1)–(7) are the generator's, and (9) records the scope correction (8) forces on (1).*

**Pf.**
$$(1):\ \ \text{the three branches of}\ \mathrm{FT.62}(1)\ \text{solved over}\ \mathbb Z\ \text{at}\ n=3\ \text{(machine: solution census};\ 2d{=}3\ \text{and}\ 2d{+}2{=}3\ \text{empty},\ 2d{+}1{=}3\ \text{uniquely}\ d{=}1);\qquad\text{hosting locus}\ [\mathrm{CT0.13}\wedge\mathrm{CT4.4a}(1)]$$
$$(2):\ \ \text{a contact is one directed edge, so it changes one vertex's rung by}\ 1\ [\mathrm{CT0.3}\ \text{Pf}:\ \exists!(p,q)\ \text{with}\ \Delta[(p,q)\in\mathcal R]=\pm1];\qquad\text{the bound follows by counting}$$
$$(3):\ \ 2d+2\equiv0\ (2)\ \forall d\ \text{(machine};\ d=1..5);\qquad \Sigma_\triangle\ \text{re-derived on the full bidirectional}\ K_4\ \text{with the observer's six boundary edges:}\ n=6\ \text{at all four}\ [\mathrm{FT.49}(5)]$$
$$(4):\ \ (2)\ \text{with three required colour vertices}\ [\mathrm{IT.84}(3)];\qquad \Sigma_{12}\ \text{'s rungs re-derived exactly from FT.35's own edge list — two 2-cycles, the bidirectional connector, and the single observer contact at}\ p_1\ \text{— giving}\ n=(3,4,4,2)\ [\mathrm{FT.35}(4)]$$
$$(5):\ \ \text{explicit witness, machine-verified:}\ 9\ \text{distinct edges},\ \sum_v n(v)=18=2|E|,\ \text{zero locked},\ \text{all three hosting vertices of type}\ (2,1)$$
$$(6):\ \ \text{census over}\ 15\ \text{floor variants built from FT.62}(1)\text{'s law}\ (\text{machine table});\qquad V_2\ \text{reachable sealed because the}\ d{=}1\ \text{digon keeps type-}(1,1)\ \text{vertices}\ [\mathrm{FT.62}(5)];\qquad V_3\ \text{only via}\ (1)$$
$$(7):\ \ \text{exact integer arithmetic on}\ O(n)=\max(0,2^{n+1}-16)\ [\mathrm{CT0.6}]\ \text{over the five Platonic}\ (V,d)\ \text{pairs}\ [\mathrm{FT.42}(5)]\ \text{— all four frozen columns reproduced}$$
$$(8):\ \ \sum_v n(v)=2C+h\ [\mathrm{D0.8}\ \text{additivity: a closed edge contributes 2, an open end contributes 1}]\implies \#\{\text{odd}\ n(v)\}\equiv h\ (2);\ \ 3k=2C+h\wedge 3\equiv1\ (2)\implies k\equiv h\ (2)$$
$$\text{machine: the modular solution census over}\ k=0..8,\ h=0..3,\ C=0..19\ \text{finds ZERO exceptions, and}\ h=1\ \text{with}\ k\in\{2,4,6\}\ \text{has NO solution at all — so the builder's census zeros are FORCED};$$
$$h=0\ \text{conjoined with}\ (2)\ \text{'s sealed case}\ (n(v)=2\partial^{\leftarrow}(v)\ \text{even})\ \text{gives}\ k=0:\ \text{a sealed all-trivalent core does not exist}$$
$$(9):\ \ \mathrm{CT0.11b}\ \text{verbatim};\ \text{the}\ (3,0)/(0,3)\ \text{route is excluded by}\ (2)\ \text{in the SEALED case only, so}\ (1)\ \text{is scoped to the FT.62 families as}\ (8)\ \text{requires};\ \ \mathrm{BM.134}(5)\ \text{for the register caution}.\ \blacksquare$$

**Phys.** Ask the ledger where the strong force can live and it answers with a parity: three is odd,
a sealed interior is even, so the two never meet. Colour can *host* at exactly one kind of place — a
single-channel vertex caught by a single one-way contact — and nowhere else in any computed floor.
The photon, living at rung two, needs no such accident and is available in the sealed dark; the
gluon, needing rung three, cannot exist without a contact at all. And the baryon's darkness is not a
property it has but a property of how little of it is being read: give it three asymmetric contacts
and the lock disappears entirely, which is the same statement as IT.84 seen from the other side.

---

### IT.86 — The Janus balance knot resolved: one law, three loci

**Thm.**
$$(1)\quad\textbf{the knot.}\qquad \mathrm{BM.7}(1):\ \text{the seal excess}\ \#J^+-\#J^-=n_{\mathcal R}\ \text{is the ledger's own occupation count};\qquad \mathrm{D2.11}:\ \text{valid universe}\iff\ \text{network closed}\ \wedge\ \#J^+=\#J^-\ \wedge\ \cdots$$
$$\text{conjoined AT ONE LOCUS they force}\ n_{\mathcal R}=0\ \text{at validity, against}\ \mathrm{CT2.6}(2)\text{'s ``coarse-graining cells contain unboundedly many real edges''}.\qquad\text{The contradiction is real; the conjunction is not.}$$
$$(2)\quad\textbf{LOCUS A — the pair history (the word level).}\qquad n_{\mathcal R}=\#J^+-\#J^-\ \text{is the CUMULATIVE occupation count of one history}\ [\mathrm{BM.7}(1)].$$
$$\mathrm{D1.2}\ \text{'s domains}\ (J^-\ \text{undefined at}\ n_{\mathcal R}=0;\ J^+\ \text{undefined at}\ n_{\mathcal R}=1)\ \text{force STRICT ALTERNATION};\qquad\text{the prefix law}\ \#J^+(\text{prefix})\ge\#J^-(\text{prefix})\ \text{holds with equality}\iff n_{\mathcal R}=0;$$
$$\text{the completed single-pair word of length}\ 2m\ \text{is UNIQUE:}\ (J^+J^-)^m\ [\mathrm{FT.144}(2)].\qquad\textbf{At this locus balance IS completion.}$$
$$(3)\quad\textbf{LOCUS B — the network AT A SNAPSHOT (the missing one).}\qquad \mathrm{D2.11}\ \text{'s balance is NOT a tally of cumulative events. Read where the corpus reads it, at EM.11's proof:}$$
$$\neg\exists\ \text{dangling ledger boundary}\implies\forall\ \text{ends sealed};\qquad \text{``seal joins target-end}\to\text{source-end''};\qquad \#J^+=\#J^-\implies\text{``the pairing covers every end exactly once''}\ [\mathrm{D1.2},\ \mathrm{D1.3},\ \mathrm{D1.4}]$$
$$\Longrightarrow\ \text{at locus B, balance means EVERY EDGE-END IS PAIRED INTO A CLOSED CHAIN — a BOUNDARY condition on the configuration at a snapshot},$$
$$\text{which is}\ \mathrm{D1.4}\ \text{'s per-chain closure}\ (\text{closed}\iff\partial c=0\wedge\#J^+=\#J^-)\ \text{lifted to the network. It says nothing about cumulative crystallizations.}$$
$$\boxed{\ \textbf{ANSWER: the emergent manifold}\ M\ \textbf{exists during the building phase because validity is a condition on the network's ENDS, not on the cumulative Janus tally.}\ }$$
$$\mathrm{CT2.6}\ \text{'s hypotheses are evaluated at the snapshot:}\ (1)\ \text{valid universe — ``a definitional precondition}\ \ldots\ \neg\text{an extra-axiomatic hypothesis''};\ (2)\ \text{unboundedly many real edges as}\ \mathfrak h\to0\ [\mathrm{BM.151}];\ (3)\ \text{bounded variation}\ [\mathrm{BM.151}];$$
$$\text{NONE requires}\ n_{\mathcal R}=0.\qquad\text{The apparent contradiction came from evaluating locus A's cumulative identity at locus B.}$$
$$(4)\quad\textbf{LOCUS C — the rung (the capacity level).}\qquad \mathrm{CT4.3}:\ \text{``oversubscription}\ \neg\text{seal}:\ \Delta n_{\mathcal R}=0\text{''}\ \text{— a load/capacity mismatch AT FIXED RUNG, proved as}\ \neg\text{seal}\implies\neg\exists\ \text{removed entry.}$$
$$\text{the lock is NOT AN EVENT but a property of the resulting state, so it can disturb NEITHER locus A (no seal occurs) NOR locus B (no end is created or destroyed).}$$
$$\text{and the locked excess is retained AND COUNTED}\ [\mathrm{D4.2};\ \mathrm{CT4.3}:\ \text{absorbed}\subseteq\mathfrak L,\ \neg\exists\ \text{deleted entry},\ w(C)\ne0\ \text{in the unmasked A8 sum}]$$
$$[\mathrm{FT.35}\ \text{Pf}(2)\ \text{uses exactly this}:\ q_1,p_2\ \text{oversubscribed at}\ n{=}4,\ \text{``excess locked but retained and counted''}\implies I_{\mathrm{hid}}=E_{\mathrm{int}}\ln2=6\ln2].$$
$$\boxed{\ \text{validity (a seal-count condition) and accessibility (a rung condition}\ [\mathrm{D1.11}]\text{) come apart cleanly: the universe stays balanced; the lock removes ACCESS, never CONTENT.}\ }$$
$$(5)\quad\textbf{the witness that settles it (machine).}\qquad \text{the BIDIRECTIONAL TRIANGLE is closed, every end paired (locus B satisfied), Janus-balanced — and EVERY vertex is locked:}$$
$$n(v)=2d_S(v)=4\ \forall v,\qquad O(4)=16=C_{\mathrm{cap}}\ \forall v\qquad[\mathrm{CT0.11b};\ \mathrm{CT4.1a}(2):\ \text{``uniform minimal saturation}\ n(v)=4\ \forall v\ \ldots\ \text{independent of cycle length''}]$$
$$\text{so validity and locking are INDEPENDENT, and no counterfactual about refusing}\ J^-\ \text{is needed to produce the lock.}$$
$$(6)\quad\textbf{two refuted readings, recorded.}\qquad (a)\ \text{``reality that refused to dissolve would oversubscribe and lock'' — its ANTECEDENT IS NOT A WORLD:}\ \#J^-=0\ \text{with}\ \#J^+>0\ \text{is Janus-unbalanced}\ [\mathrm{D1.3}]$$
$$\implies\neg\text{a valid universe}\ [\mathrm{D2.11},\ \mathrm{BM.7}(1),\ \mathrm{FT.144}(1)],\ \text{and}\ \mathrm{CT2.6}(1)\ \text{calls the balance ``a definitional precondition}\ \ldots\ \neg\text{an extra-axiomatic hypothesis''}\implies\neg\exists\ M;$$
$$\text{unbalanced}\implies\neg\exists\ \text{closed chains}\ [\mathrm{D1.4}]\implies\neg\exists\ \text{bound content}\ [\mathrm{D1.5};\ \mathrm{FT.144}(1)]\implies\text{no baryon at all.}\qquad(b)\ \text{its CONSEQUENT fails inside valid universes — witness}\ (5).$$
$$\text{what survives needs no counterfactual: on a finite skeleton, LOCAL accumulation past}\ n(v)=3\ \text{at a vertex locks that vertex}\ [\mathrm{CT4.1a}(1)].$$
$$(7)\quad\textbf{the temporal words are barred.}\qquad \text{``eventually'' and ``prevents'' have no derived referent: no rates are declared}\ [\mathrm{Cal\text{-}F}];\ \mathrm{CT0.6}\ \text{is ``ledger accounting}\ \ldots\ \neg\text{a tick-to-tick transition law''};$$
$$\text{only}\ \tau_c=1\ \text{ledger tick is derived, with no absolute frequency and no field coupling of}\ \delta\tau\ [\mathrm{FT.86}].\qquad\text{The admissible form is the counterfactual-conditional WITH ITS HYPOTHESIS STATED}\ [\mathrm{CT4.5a}\ \text{pattern}].$$

**Req.** A5, A6, A7; D0.1, D0.7, D1.1, D1.2, D1.3, D1.4, D1.5, D1.11, D2.11 (Part 1); CT0.3, CT0.6, CT0.11b (Part 1); CT2.6, CT4.1a, CT4.2, CT4.3, CT4.5a (Part 2); D4.2 (Part 1); BM.7(1), BM.151 (Part 4); FT.35 Pf(2) (Census); FT.86, FT.144 (Part 3); exhaustive word enumeration, the Catalan relaxation census, multinomial interleaving counts, exact rational dust-density arithmetic [math; machine: `parity_contact_gate.py` §H–§J].

**Pf.**
$$(2):\ \ \text{re-derived exhaustively (machine): one admissible word per length}\ 0..8;\ \text{the completed word of length}\ 2m\ \text{unique};\ \text{the prefix law at every prefix};\ \text{the relaxation census}\ \mathrm{Cat}_m=(1,1,2,5,14,42,132);\ \text{two-pair interleavings}\ (2,8,32)\ [\mathrm{FT.144}(2);\ \mathrm{BM.7}(1)]$$
$$(3):\ \ \text{the three cited clauses of EM.11's proof, verbatim};\qquad\mathrm{CT2.6}(1)\text{--}(3)\ \text{evaluated at the snapshot};\qquad\mathrm{FT.144}(2)\ \text{names the balance ``the balanced-sector restriction of the move algebra's budget identity'' — a sector condition,}\ \neg\text{pointwise}$$
$$(4):\ \ \mathrm{CT4.3}\ \text{Thm and Pf verbatim};\qquad\mathrm{FT.35}\ \text{Pf}(2)\ \text{verbatim};\qquad\text{one}\ J^+\ \text{is}\ (+1,+1,+1)\ \text{at EVERY rung}\ [\mathrm{CT0.3}],\ \text{so the lock adds no event}$$
$$(5):\ \ \text{explicit witness, machine-verified: three vertices, six directed edges,}\ n=4\ \text{at each},\ O(4)=16\ \text{at each};\qquad\text{and}\ \mathrm{CT4.5a}\ \text{'s dust density re-derived strictly positive at every}\ p\in(0,1]\ \text{on all five Platonic skeletons}$$
$$(6),(7):\ \ \text{the cited clauses};\qquad\text{no new mathematics at these clauses}.\ \blacksquare$$

**Phys.** The knot was never a contradiction in the ledger; it was one identity read at the wrong
address. Counted along a single pair's history, balance means the word has come home. Counted across
a configuration at an instant, balance means every edge-end has found its partner — and that is a
condition a growing network can satisfy at every moment of its growth, which is why spacetime can
exist mid-construction. The lock sits at a third address entirely, in the rung, where it is not an
event at all and therefore cannot be counted either way. A closed, balanced, perfectly valid triangle
can have every one of its vertices behind the lock, and does.

---

### IT.87 — The enforced bar and the two adopted structural readings

**Thm.**
$$(1)\quad\textbf{BAR ENFORCED (the Architect's disposition).}\qquad \text{the sentence ``the strong force is the geometry of the lock'' is}\ \textbf{BARRED}:$$
$$D^-:\ \neg\exists\ \text{nonabelian gauge algebra},\ \neg\exists\ \text{abelian gauge algebra},\ \text{``contributes}\ \neg\text{generator to any accessible algebra''}\ [\mathrm{CT4.4}];$$
$$\text{``the locked sector receiving rung-}\ge4\ \text{content carries no gauge structure — no generators, no internal directions''}\ [\mathrm{CT4.4a}(1)];\qquad\text{``a structureless absorbing sink''}\ [\mathrm{CT4.5a}(4)]$$
$$\mathbf F_{\mathrm{st}}=F_{\mathrm{EM}}\oplus F_{\mathrm{strong}}\oplus F_{D^-}\ \text{is a DIRECT SUM of distinct blocks}\ [\mathrm{A8};\ \mathrm{CT0.12}\ \mathrm{Rmk}];\qquad \dim\mathfrak{su}(3)=8\ [\mathrm{CT3.8}]\ \text{against a one-dimensional scalar sink}$$
$$\Longrightarrow\ \text{identifying}\ F_{\mathrm{strong}}\ \text{with}\ F_{D^-}\ \text{is a kind confusion}\ [\mathrm{BM.134}(5)\ \text{discipline}].$$
$$(2)\quad\textbf{ADOPTED FORM (verbatim, the Architect's disposition).}\qquad \boxed{\ \text{``The strong force's hosting ceiling is the lock's boundary, and the baryon is the parity defect the lock receipts.''}\ }$$
$$\text{each half derived: the ceiling is the boundary because}\ \iota_n\ \text{exists exactly for}\ n\le3\ [\mathrm{CT4.4a}(1)],\ \text{i.e. exactly up to the last rung before}\ D^-;\ \text{``hosting dies at rung 3; sealing persists at every rung''}\ [\mathrm{CT4.4a}(3)];$$
$$\text{and the defect is a parity because}\ \operatorname{rank}(\varepsilon_{ijk})=3\ \text{is odd while}\ \textstyle\sum_v n(v)\ \text{is even}\ [\mathrm{IT.84}(1),(4)].$$
$$(3)\quad\textbf{READING ONE, ADOPTED AND FLAGGED — the}\ \mathbb Z_2\ \textbf{parity-defect read (obstruction-theoretic; origin: generator).}\qquad \text{the degree sum is even — a mod-2 invariant of the network};\ \operatorname{rank}(\varepsilon_{ijk})=3\ \text{is odd},$$
$$\text{so the baryon carries a}\ \mathbb Z_2\ \text{charge}\ |\mathrm{Colour}|\bmod 2\ \text{AGAINST the admissible locus}\ \{n\le3\};\qquad D^-\ \text{is where such a charge goes when there is no room to realize it}:$$
$$\mathrm{CT4.4}\ \text{'s ``scalar sink,}\ \neg\text{internal directions'' is exactly the sector that can absorb a parity defect};\qquad\text{the charge is ADDITIVE — two}\ \varepsilon\text{-triples}\ (|\mathrm{Colour}|=6,\ \text{even})\ \text{cancel it},$$
$$\text{which is why IT.85}(5)\text{'s witness is lock-free};\qquad\text{joint constraints: mod}\ 2\ (\text{parity})\ \wedge\ \text{mod}\ 3\ (\text{grammar})\ =\ \text{mod}\ 6\ [\mathrm{IT.84}(5)].$$
$$\text{it answers WHY the lock is forced.}\qquad\textbf{note (a register correction, recorded):}\ \text{this}\ \mathbb Z_2\ \text{is the PARITY OF THE TRIVALENT COUNT,}\ \neg\text{the edge phase alphabet}\ \Phi=\{0,\pi\}\ [\mathrm{CT0.9}].$$
$$(4)\quad\textbf{READING TWO, ADOPTED AND FLAGGED — the retention-cell read (order-theoretic; origin: builder, credited).}\qquad \text{at a locked vertex the hosting star collapses to}\ D^-\ \text{absorption}\ [\mathrm{CT4.4};\ \mathrm{D4.1},\ \mathrm{D4.2}]$$
$$\text{while the oversubscription}\ O(n)\ \text{is RETAINED as inaccessible data}\ [\mathrm{CT4.3};\ \mathrm{CT4.5a}]\ \text{and the sealing partition survives as configuration data}\ [\mathrm{CT4.4a}(3)]:$$
$$\text{the locked vertex is a SINK in the hosting order and an INTERIOR point in the sealing order — a retention cell with a sealed core};$$
$$\text{the baryonic floors are retention cells whose sealed core is nonempty}\ [\mathrm{FT.35}:\ \text{seal}\ 4\ \text{at the}\ n{=}4\ \text{junctions};\ \mathrm{FT.49}:\ \text{seal}\ 20\ \text{at}\ n{=}6],\ \text{counts independently re-derived as}\ \binom{n}{3}g_\varepsilon(3)=(1,4,20)\ \text{at}\ n=(3,4,6).$$
$$\text{it answers WHAT the locked vertex is.}$$
$$(5)\quad\textbf{the two readings are complementary, not rival, and neither is an identification.}\qquad \text{both are flagged structural readings over exact Census referents}\ [\mathrm{BM.134}(5)\ \text{parallel-not-identification};\ \mathrm{P5}];$$
$$\text{neither imports a mass, a range, a coupling or a species};\qquad\text{the DERIVED content is IT.84--IT.86, and the readings are its two descriptions.}$$
$$(6)\quad\textbf{one further reading, flagged and }\neg\textbf{adopted (the contact-deficit reading).}\qquad \text{IT.85}(4),(5)\ \text{supports: ``the baryon must be observed at all three of its colour vertices to stay out of the lock; partial observation is what locks it.''}$$
$$\text{it is a READING because IT.85 counts contacts and never rates them — no claim is made about when, how often, or by whom a contact occurs}\ [\mathrm{CT0.6};\ \mathrm{Cal\text{-}F};\ \mathrm{IT.86}(7)].$$

**Req.** A8; D0.9, D4.1, D4.2, D4.3 (Part 1); CT0.9, CT0.12, CT0.14 (Part 1); CT3.8, CT4.4, CT4.4a, CT4.5, CT4.5a, CT4.6 (Part 2); BM.134 (Part 4); FT.35, FT.49, FT.63 (Census); IT.84, IT.85, IT.86 (this tier); P1, P5 [policy]; no machine content beyond the counts re-derived at IT.84(5) and IT.85.

**Pf.**
$$(1),(2):\ \ \text{the cited clauses verbatim; the ceiling/boundary identity from}\ \mathrm{CT4.4a}(1)\text{--}(3);\ \text{the parity from}\ \mathrm{IT.84}(1),(4)\ [\text{machine-certified there}]$$
$$(3),(4):\ \ \text{assemblages of the cited rows into descriptions; each constituent attested at IT.84--IT.86; no new claim of fact is introduced, and every interpretive step is labelled a READING}$$
$$(5),(6):\ \ \text{the bar discipline rows}\ [\mathrm{BM.134}(5);\ \mathrm{P1},\ \mathrm{P5}]\ \text{and the no-dynamics rows}\ [\mathrm{CT0.6};\ \mathrm{Cal\text{-}F}].\ \ \text{No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** One sentence was refused and two were kept, which is the normal ratio for this kind of
proposal. The refusal matters: the dark sector has no generators at all, so calling the strong force
"the geometry of the lock" would have put an eight-dimensional algebra inside a one-dimensional sink.
What survives is a boundary statement — hosting stops exactly where the lock begins — plus two ways
of picturing the same exact rows, one saying why the baryon cannot escape its darkness and the other
saying what that darkness is made of. Neither picture is a claim about the world; both are captions
over counts that a machine has checked.

---

### IT.88 — Tier IT.24 verdict, bars, and scans

**Thm.**
$$(1)\quad\textbf{what is derived at this tier.}\qquad \text{the embedding parity and its two load-bearing hypotheses}\ [\mathrm{IT.84}(1)];\ \text{the sealed case's diagonal types and the unreachability of}\ (0,3),(3,0)\ [\mathrm{IT.84}(2)];$$
$$\text{the JOIN with Census FT.63's even-}\varepsilon\ \text{theorem, which is the load-bearing result per the Architect's disposition}\ [\mathrm{IT.84}(4)];\ \text{the mod-6 corollary and the fermion/boson dichotomy}\ [\mathrm{IT.84}(5)];$$
$$\text{the contact-gating biconditional and the contact budget}\ [\mathrm{IT.85}(1),(2)];\ \text{the bidirectional-contact clause}\ [\mathrm{IT.85}(3)];\ \text{the contact deficit and the constructive lock-free witness}\ [\mathrm{IT.85}(4),(5)];$$
$$\text{the photon/gluon rung-parity census}\ [\mathrm{IT.85}(6)];\ \text{FT.62}(2)\text{'s four columns}\ [\mathrm{IT.85}(7)];\ \text{the three-locus knot resolution and its witness}\ [\mathrm{IT.86}].$$
$$(2)\quad\textbf{what is a flagged reading.}\qquad \text{the}\ \mathbb Z_2\ \text{parity-defect read}\ [\mathrm{IT.87}(3)];\ \text{the retention-cell read}\ [\mathrm{IT.87}(4)];\ \text{the contact-deficit read}\ [\mathrm{IT.87}(6)].\qquad\text{All three}\ \neg\text{adopted as identifications}\ [\mathrm{BM.134}(5);\ \mathrm{P5}].$$
$$(3)\quad\textbf{what is barred.}\qquad \text{``the strong force is the geometry of the lock''}\ [\mathrm{IT.87}(1)];\ \text{the temporal readings ``eventually''/``prevents''}\ [\mathrm{IT.86}(7)];$$
$$\text{the vertex types}\ (0,3),(3,0)\ \text{as occupants of a valid universe}\ [\mathrm{IT.84}(2)];\ \text{any deletion of ledger content by}\ J^-\ [\mathrm{A7};\ \mathrm{CT4.3};\ \mathrm{A5}\ \text{: the sole exclusion from}\ \mathfrak L\ \text{is}\ U];$$
$$\text{any mass, range, coupling or species reading of the labels}\ [\mathrm{P1},\ \mathrm{P5};\ \mathrm{FT.49}(6):\ \text{``structural correspondence,}\ \neg\text{particle identification''}].$$
$$(4)\quad\textbf{no declaration issues at this tier}\ (\text{machine-scanned}).\qquad \text{the act register stands as IT.66}(4)\ \text{records it, extended by IT.78 and IT.83: issued D-PJ1--6, D-RS1--3, D-RS6--7 and the BM.113}(6)\ \text{sector sync};$$
$$\text{deferred D-RS4};\qquad\textbf{owed: D-PJ7 alone}\ +\ \text{the three sub-debts}.\qquad \text{§Cal-IT is unchanged and value-free};\qquad\text{the Calibration Era stays deferred}\ [\mathrm{AT.63}(4)].$$
$$(5)\quad\textbf{no new open row.}\qquad \text{the mixed-skeleton residue is a SCOPE note, not a gap}\ [\mathrm{IT.85}(8)];\qquad\text{the three readings carry their own flags}\ [\mathrm{IT.87}(5),(6)];$$
$$\text{the dynamical side stays at IT-O1 (three grounds; deficit}\ 1'=\mathrm{D\text{-}PJ7}\ \text{owed}),\ \text{untouched by this tier}. $$
$$(6)\quad\textbf{provenance and credit, recorded.}\qquad \text{the parity theorem's grammar half is Census FT.63's and is cited as such — an earlier probe-space draft claimed the corollary without it, and the correction is logged};$$
$$\textbf{the GENERAL parity lemma at IT.85}(8)\ \textbf{is the builder's probe result, adopted here, and it SUBSUMES the generator's floor-family biconditional at IT.85}(1)\ \textbf{— the scope correction is recorded at IT.85}(9),\ \text{not absorbed silently};$$
$$\text{the retention-cell read is the builder's}\ [\mathrm{IT.87}(4)];\ \text{the kernel mirrors are the builder's}\ (\text{the rung-boundary file, the parity core, the balance-knot receipts});$$
$$\text{the}\ (1,4,20)\ \text{seal counts were computed independently on both sides and agree};\qquad\text{the ``}\ \text{earth}\ \text{'' label at}\ n{=}3\ \text{was withdrawn on the generator's correction}\ [\mathrm{CT3.17a}(1)\ \text{distinct-node clause}].$$
$$(7)\quad\textbf{process row, recorded because it changed two results.}\qquad \text{the Summary of Record was NOT consulted before the probe-space drafts claimed novelty; consulting it corrected two priority claims}\ [\mathrm{FT.63};\ \mathrm{FT.62}(1)].$$
$$\text{standing rule adopted at this tier: the Summary is grepped BEFORE any absence or novelty claim, and every such claim carries an explicit novelty scan with a live control.}$$
$$(8)\quad\textbf{suite and gate state.}\qquad \text{the runner and the format gate are re-run end to end at this tier and reported in the tier's own machine line};\ \text{no frozen file is edited}\ [\mathrm{AT.63}(2)].$$

**Req.** IT.84, IT.85, IT.86, IT.87 (this tier); IT.14(3), IT.63(6), IT.66(4), IT.78, IT.83 (this level); AT.63(2),(4) (Level 5); BM.134(5) (Part 4); FT.49(6), FT.62(1), FT.63 (Census); A5, A7, CT0.6, CT4.3 (Parts 1–2); P1, P5 [policy]; the declaration scan, the open-row assembly, the decimal scan with its live-witness self-test, the runner and gate re-runs [machine: `parity_contact_gate.py` §K].

**Pf.**
$$(1)\text{--}(3):\ \ \text{the row-wise assembly of}\ \mathrm{IT.84}\text{--}\mathrm{IT.87}\ \text{with every verdict traced to its certifying marker or its frozen ground}\ [\text{machine}\ \S\mathrm{A}\text{--}\S\mathrm{J}];$$
$$(4),(5):\ \ \text{the declaration scan (no act handle appears at this tier), the open-row assembly, and the symbol-set census}\ [\text{machine}\ \S\mathrm{K}];$$
$$(6),(7):\ \ \text{the record rows, as logged in the probe-space packages and in the concept queue's resolution logs};$$
$$(8):\ \ \text{the runner and the gate re-run end to end}.\ \ \text{No new mathematics is introduced at this tag}.\ \blacksquare$$

**Phys.** Three concepts went into probe space and two came out as rows, one came out as a census, and
one sentence came out barred. What the ledger turned out to say is compact enough to hold: an odd
number of baryon triplets cannot be seated on a network whose edge-ends come in pairs; the only place
the strong force can act is where something is being read; and a lock is not an event, so it cannot
upset the accounting that makes a universe valid. The rest is caption. Two of the captions are good
enough to keep beside the rows, flagged as what they are, and one of them is the builder's.

---

## §Cal-IT — unchanged (value-free)

**No act at this tier.** Tier IT.24 issues no declaration (machine-scanned at IT.88(4)): it is a
read-tier on frozen ground, recording the Architect's dispositions on concepts 0002, 0004 and 0005.
The act register stands as IT.66(4) records it, extended by IT.78 and IT.83 — issued: D-PJ1–6,
D-RS1–3, D-RS6–7, the BM.113(6) sector sync; deferred: D-RS4; owed: **D-PJ7 alone** + the three
sub-debts. **No calibration parameter is added, valued, or re-scoped**: the P1 scale slot,
$\varepsilon_q$ (AT-O27), $e_0$ [EM.25], $(\varkappa,\beta)$ (AT-O3), $\rho_{\mathrm B}$ [A-BM.9],
$\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$, the $\mu_{\mathrm{ch}}$ family (Cal-F), the read rules
(M1′)–(M3′) [AT.54(6)], the lift/vielbein/P4 profile [AT.63(3)], and the mass-read route choice
[IT.14(3); BM.30(5)] all stand unchanged. Every quantity at this tier is a **count, a parity, or a
type** — no scale, no rate, no coupling. The Calibration Era stays **deferred** [AT.63(4)]. **The M
exploration [concept/0003] is EXPLORATORY ONLY and the F=ma probe remains PAUSED**: no clause of this
tier touches the cross-currency matrix $M$ or its tensor square $X$, and none cites either as a
premise.

## §Open-IT additions from Tier IT.24

| row | content | locus |
|---|---|---|
| (none new) | Tier IT.24 opens **no row**. The parity theorem, the contact-gating biconditional, the contact budget, the photon/gluon rung-parity census and the three-locus knot resolution are all **derived on frozen ground** [IT.84; IT.85; IT.86]; the three readings carry their own flags and are scope, not gaps [IT.87(5),(6)]; the mixed-skeleton residue is a scope note with its reasoning given [IT.85(8)]; the dynamical side stays at IT-O1 — untouched by this tier | IT.84(4),(5); IT.85(1),(4),(6),(8); IT.86(3),(4); IT.87(5),(6); IT.88(1)–(5) |

Inherited unchanged [IT.1(5); IT.8(4); IT.11(3),(4); IT.15(5); IT.18(5); IT.21(2); IT.24; IT.27;
IT.30; IT.33; IT.36; IT.39(5); IT.42; IT.45(5); IT.48(4); IT.54(4); IT.57(5); IT.60(4); IT.62(4);
IT.66(6); IT.70(1); IT.78(4); IT.83(4)]: (IT-O1) the formed transit-leg amplitude — three grounds,
deficit 1′ [IT.41(2)]; (IT-O2) the binding value — the three IT.27(2) constructions (the δ-glue input
named at IT.69(6)); (IT-O5) the isotope cutoff — the dynamical side at IT-O1; AT-O30/AT-O32 the heavy
censuses; the owed route choice [IT.14(3)]; the deferred Calibration Era [AT.63(4)]; and the Level-5
inheritance [AT.63(3),(5)].

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.25: the carrier-read remark and the boson lifecycle — what an edge is called at each of its ends, and how far a boson's own ledger can see

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.25 — the disposition tier for the
Architect's rulings on **concept/0009 (boson indistinguishability: the carrier read is
rung-relative) MERGED** — *"Adopted as a read-tier remark beside IT.85(6)/EM.5. The carrier
relativity is derived as register factorization."* (vault issue #17, 2026-10-15T14:43:16Z) — and
**concept/0010 (the complete boson ledger) ADOPTED-and-BARRED** — *"ADOPT the 5-terminal
accessible-history automaton. BAR the global completeness claim. The omega-terminal is accepted."*
(vault issue #18, 2026-10-15T14:43:50Z). Both concepts were adjudicated in probe space against the
frozen rows before this tier was written (`carrier_relativity.py` 15 markers, `boson_lifecycle.py`
11 markers, both mirrored in the vault); the Builder's halves are the kernel record (concept/0009:
`RegisterAbsence.lean`, 43 theorems, merged inside lean PR #11 at `0f53ea0`; concept/0010: the
automaton construction IN PROGRESS at the vault claim `6194835010`). **Tags.** IT.89–IT.91.
**Pattern.** the read-tier / adjudication shape (IT.16, IT.22, IT.24's pattern): no new primitive,
no new act, no new open row — frozen rows read at their own loci, plus the supersession rows that
AT.63(2) requires to ride a later tier rather than an in-place edit.
**Status.** discovery-phase working tier. No declaration issues at this tier (machine-scanned at
IT.91); §Cal-IT stays value-free and unchanged; no clause of Parts 1–4, of Level 5's closed record,
or of Tiers IT.1–IT.24 is modified [AT.63(2)] — IT.90 is the refinement register this tier owes.
No measured value enters [P5]; no new dimensionful scale [P1]; "photon", "gluon", "boson",
"lepton", "baryon" stay quoted read-labels over derived rows, never species identifications
[Def-BM.3(7); FT.49(6); the paper-layer Caveat discipline: quoted read-vocabulary]. The
dictionary floor (vault arch/0007-dict) is
honored: this tier touches no $\varepsilon_q$ value, carries no lepton mass read, and uses no
$\mathcal K$ bridge.
**Machine.** `era2/level6_isotopic/checks/carrier_read_tier.py` → **exact** (integers and doubled
integers only; exhaustive censuses; no randomness, NO floating point in any assertion);
`run_all_level6.py` → the full level suite; `check_level6_format.py` → the gate over all
twenty-five Part 6 documents. Probe-space antecedents, retained as the working record:
`carrier_relativity.py` (15 markers), `boson_lifecycle.py` (11 markers), and the Builder's
`register_absence_census.py` (29 markers), each mirrored in the vault's `probe_space/generator/`
and re-run by both instances.
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** The Architect's two dispositions, executed in full: the register statement and the
relativity verdict beside IT.85(6)/EM.5 (IT.89); the refinement rows that merged canon owes
(IT.90); the adopted five-terminal automaton form, the barred global claim, and the accepted
$\omega$-terminal (IT.91).

---

### IT.89 — The carrier-read remark: relativity as register factorization

**Thm.**
$$(1)\quad\textbf{THE REGISTER STATEMENT.}\qquad \text{the carrier CLASS is a CHAIN-LEVEL predicate:}$$
$$\text{photon} := \text{trivial chain} \subseteq V_2;\qquad \text{gluon} := \text{trivial chain} \cap V_3 \ne\varnothing\qquad [\mathrm{D3.7};\ \mathrm{D1.7};\ \mathrm{EM.5}]$$
$$\text{evaluated over the floor's rung partition}\ V_n=\{v:\ n(v)=n\}\ [\mathrm{D0.8}];\qquad V_2\cap V_3=\varnothing\ [\mathrm{EM.5}]\ \Longrightarrow\ \text{a trivial chain carries AT MOST ONE class;}$$
$$\text{every VERTEX-LOCAL read factors through the slot register}\ \mathcal H^{(n(v))}_{\mathrm{slot}}\cong\mathbb C^{n(v)}\ [\mathrm{D3.1}]:\qquad \text{at}\ n=2\ \text{the colour summand is ABSENT}$$
$$[\mathrm{CT0.13}:\ \mathrm{strong}\in\mathcal A(n)\iff n\ge3;\qquad \mathrm{CT3.11}(1):\ \text{colour} := \text{slot index at}\ n=3;\qquad \mathrm{FT.35}\ \mathrm{Pf}(5)\ \text{slot-less row};\qquad \mathrm{CT4.4a}(1):\ \iota_n\ \text{exists exactly for}\ n\le3].$$
$$\text{the absence is EXHAUSTIVE, not a vanishing computation (machine): of all}\ 8\ \text{maps}\ \{1,2,3\}\to\{1,2\},\ \textbf{0}\ \text{are injective}\ —\ \text{contrast}\ 6=3!\ \text{of}\ 27\ \text{at}\ n=3.$$
$$(2)\quad\textbf{THE RELATIVITY THEOREM (DERIVED).}\qquad \text{let}\ \gamma\ \text{be a trivial chain containing a spanning edge}\ (u\to v),\ n(u)=3,\ n(v)=2.$$
$$\text{such edges exist exactly at: the observed}\ \Sigma_{\min}\ (e_1=(p,q);\ 1{+}1)\ [\mathrm{FT.28}(5)];\qquad \text{every}\ \Sigma_L\ ((v_1,v_2),\ (v_L,v_1);\ 1{+}1)\ [\mathrm{FT.32}(2)];$$
$$\text{the IT.85}(5)\ \text{witness}\ (3{+}3);\qquad \text{and nowhere else in the frozen record (machine census over the frozen floors).}$$
$$\text{then:}\ \gamma\cap V_3\ne\varnothing\ \Longrightarrow\ \gamma\ \text{is gluon-class, and}\ \gamma\subseteq V_2\ \text{is impossible}\ [V_2\cap V_3=\varnothing]\ —\ \textbf{the chain class is forced};$$
$$\text{while every local read at}\ v\ \text{is D3.3's pass-through on the type-}(1,1)\ \text{sign pair}\ (\sigma_{\leftarrow},\sigma_{\rightarrow})\in\{\pm1\}^2\ [\mathrm{CT0.9}]:\ 4\ \text{states},\ 2f_v\in\{-2,0,0,+2\},\ \text{ternary, 2-to-1 at}\ 0;$$
$$\boxed{\ \text{of the}\ 3^4=81\ \text{ternary read maps on the local state space,}\ \textbf{0}\ \text{separate ``a gluon arrived'' from ``a photon arrived''}\ }\ —\ \text{both hypotheses induce identical local data, since no colour coordinate exists at}\ n=2;$$
$$\text{control (machine): at a slot-resolved rung-3 vertex}\ (i\in\{1,2,3\}\ [\mathrm{D3.1}]),\ 24\ \text{of}\ 27\ \text{read maps separate}\ \Longrightarrow\ \textbf{the indistinguishability is REGISTER ABSENCE, not dynamics}\ [\mathrm{CT0.6}].$$
$$(3)\quad\textbf{the phrase corrections (read-label discipline [P5]).}\qquad \text{(i) ``the same edge reads as a photon at the rung-2 end'' is a READ-LABEL:}$$
$$\text{the rung-2 end supports D3.3's EM pass-through read and NEVER the D3.7 photon CLASS}\ —\ \text{the chain's}\ V_3\ \text{endpoint excludes it};\ \text{corrected form: ``gluon at the emitter end''}$$
$$\text{is the chain's class plus the emitter's slot read; ``photon-like at the receiver'' is the ABSENCE of a colour read plus the presence of the pass-through.}$$
$$\text{(ii) ``simultaneously valid and mutually untranslatable (different registers)'' holds in BM.134}(5)\text{'s parallel-not-identified sense, with the precision that}$$
$$\text{the untranslatability is the ABSENCE of the colour coordinate at rung 2 (there is nothing to translate),}\ \neg\text{a non-isomorphism between two populated registers; the two registers are never summed}\ [\mathrm{IT.85}(9)].$$
$$(4)\quad\textbf{the cross-instance certificate.}\qquad \text{the Builder's non-separation theorem (0 of 16 local observables; literally-equal incident-edge lists at}\ q,\ \text{kernel-checked)}$$
$$\text{and this tier's 0-of-81 read-map census are disjoint machines with one verdict};\qquad \text{the kernel record is}\ \texttt{RegisterAbsence.lean}\ (43\ \text{theorems: the}\ \mathcal A(n)\ \text{ladder, the pigeonhole, the}\ \mathrm{D3.1}\ \text{route, the factorization)};$$
$$\text{two Python shadows + the kernel + the tier machine: the double-entry loop's fourth closing.}\qquad \text{EM.5's frozen gloss stands: ``distinguishing datum = possibility space only.''}$$

**Req.** A1; D0.8, D1.7, D3.1, D3.3, D3.7 (Part 1); CT0.6, CT0.9, CT0.13, CT3.11 (Part 1); CT4.4a (Part 2); EM.5 (Part 2); FT.28(5), FT.32(2), FT.35(4), FT.35 Pf(5), FT.62(1) (Census); IT.85(1),(4),(5),(6),(8),(9), IT.87(1) (Tier IT.24); BM.134(5) (Part 4); P1, P5 [policy]; exhaustive map and chain enumeration, exact integer and doubled-integer arithmetic, directed BFS [math; machine: `carrier_read_tier.py` §A; probe antecedents `carrier_relativity.py` 15/15, the Builder's `register_absence_census.py` 29/29 re-run by the Generator].

**Pf.**
$$(1):\ \ \text{the ladder and the}\ \iota\text{-domain are cited rows; the partition}\ V_2\cap V_3=\varnothing\ \text{is definitional once}\ n(v)\ \text{is a function}\ [\mathrm{D0.8}];\ \text{the pigeonhole is exhaustive over all}\ 2^3=8\ \text{maps (machine)}$$
$$(2):\ \ \text{the spanning census is by explicit membership test over the frozen floors' directed edge lists with live controls (machine; the}\ \Sigma_{12}\ \text{premise correction:}\ (p_1,q_2)\notin E,\ \text{shortest directed path}=3\ \text{through}\ q_1,p_2\ \text{both}\ n=4\ [\mathrm{FT.35}(4);\ \mathrm{CT4.1}])$$
$$\text{the class forcing is}\ \gamma\cap V_3\supseteq\{u\}\ \text{with}\ V_2\cap V_3=\varnothing;\qquad \text{the}\ 81=3^4\ \text{census enumerates every read map on the}\ 4\ \text{sign states; the two arrival hypotheses induce the SAME state data by}\ (1)\text{'s absence row, so no map separates (machine)}$$
$$(3):\ \ \text{the cited read-label and register-separation clauses applied to}\ (1),(2);\ \text{no new mathematics}$$
$$(4):\ \ \text{receipts, cited: the Builder's census and kernel by their own machines; this tier's machine re-runs neither code path.}\ \blacksquare$$

**Phys.** The photon/gluon distinction is not a property a wire carries; it is an address the
network's registers can or cannot read. The same edge, traversed by the same trivial chain, is
called a gluon by the chain's own vertex set and is called nothing-at-all-colour-wise by a rung-2
receiver, because the receiver's possibility space has no room in which the word "colour" could be
written. What cannot be distinguished locally is not a hidden dynamics but an absent coordinate —
which is why observing a sealed baryon symmetrically buries it deeper [IT.85(3)] while a single
jutting contact is the unique parity repair that makes hosting legal at all [IT.85(8)].

---

### IT.90 — The refinement register: what merged rows owe, paid in a later tier [AT.63(2)]

**Thm.**
$$(1)\quad\textbf{IT.85}(6)\textbf{'s scope, refined.}\qquad \text{the merged sentence ``in the entire computed Census EXACTLY ONE floor carries a rung-3 vertex'' OVERCLAIMS:}$$
$$\text{machine census (the explicit record,}\ \Sigma_L\ \text{enumerated to}\ L=8\text{):}\ \textbf{10}\ \text{named floors carry}\ V_3\ —\ \Sigma_{12}\ (p_1),\ \text{the observed}\ \Sigma_{\min}\ (p)\ [\mathrm{FT.28}(5)],$$
$$\Sigma_L\ (v_1)\ \text{for EVERY}\ L\ge2\ \text{by FT.32}(2)\ \text{(the explicit census covers}\ L=2..8\text{)},\ \text{and the IT.85}(5)\ \text{witness}\ (c_1,c_2,c_3);\qquad \text{the probe-era count of}\ 8\ \text{is the}\ L\le6\ \text{initial segment of the same census.}$$
$$\text{the TRUE scoped forms:}\quad (a)\ \text{among the SEALED BARYONIC complexes, exactly one floor carries}\ V_3:\ \Sigma_{12}\text{'s observer contact}\ p_1;$$
$$(b)\ \text{within IT.85}(6)\text{'s own 15-variant law census,}\ V_3\ \text{populates exactly the single-directed-contact-at-}d{=}1\ \text{row, one vertex};$$
$$(c)\ \textbf{universally: every}\ V_3\ \text{vertex carries an ODD count of single-directed channels, and zero single-directed channels}\ \Longrightarrow\ \text{an even rung}\ [\mathrm{IT.85}(8)]\ —\ \text{contact-gating holds WITHOUT exception}\ (\Sigma_L\text{'s}\ v_1:\ 3;\ \text{the contact floors}:\ 1).$$
$$\text{the boxed conclusions of IT.85}(6)\ \text{(photons need no contact; gluons cannot exist without one) are UNCHANGED and now hold unscoped by}\ (c).$$
$$(2)\quad\textbf{IT.84}(4)\textbf{'s ``two independent obstructions'', refined.}\qquad \text{the grammar parity}\ [\mathrm{FT.63}:\ 2a+3b=N,\ b\ \text{even}]\ \text{and the embedding parity}\ [\mathrm{IT.84}(1)]$$
$$\text{agree NECESSARILY:}\ 2a+3b=N\ \text{with}\ 3\ \text{odd gives}\ b\equiv N\ (\mathrm{mod}\ 2)\ \text{as an IDENTITY (machine: exhaustive over every grouping of every}\ N=0..60)\ —$$
$$\text{the same integer's parity read at two loci. The cross-check keeps its value}\ —\ \text{it certifies that a labelled-set-partition count and an edge-end count are counting the SAME integer}\ —$$
$$\text{but ``independent'' overstates: one}\ \mathbb Z_2\ \text{obstruction, two machines. The conclusions}\ (6\mid|\mathrm{Colour}|;\ \text{the Baryonic Lock) are unchanged and OVER-determined.}$$
$$(3)\quad\textbf{a referent resolution.}\qquad \mathrm{FT.62}(3)\text{'s cite ``CT4.1a (G)'' resolves by content to CT4.1a}(4)\ —\ \text{``the unoversubscribed real-edge family under directed rung counting is exactly}\ n(v)\le3\text{''}\ —$$
$$\text{plus the G-saturation checker family named in CT4.1a's Req}\ (\texttt{verify\_promotion\_G\_saturation.py});\qquad \text{no literal clause}\ (G)\ \text{exists in the frozen text. Recorded; the frozen text is untouched.}$$
$$(4)\quad\textbf{a citation correction of record.}\qquad \text{concept/0010's dispatch text cited BM.83 for ``photon-read and gluon-read segments are different registers, never summed'';}$$
$$\mathrm{BM.83}\ \text{is the four-currency mass census and carries no sum-bar clause (machine scan). The frozen referent is}\ \mathrm{BM.134}(5)\ \text{(``}\neg\text{identified}\ \ldots\ \text{the currency separation stands'') as IT.85}(9)\ \text{and IT.87}(1)\ \text{already use it.}$$

**Req.** IT.84(1),(4), IT.85(6),(8), IT.87(1) (Tier IT.24); FT.28(5), FT.32(2), FT.35(4), FT.62(1),(3), FT.63 (Census); CT4.1a (Part 2); BM.83, BM.134(5) (Part 4); AT.63(2) (Level 5); exhaustive floor and grouping censuses, exact integer arithmetic [math; machine: `carrier_read_tier.py` §B; probe antecedents `carrier_relativity.py` (A11), `mod6_ladder.py` (27 markers, the identity's first machine), the Builder's C11 scope row (vault receipt)].

**Pf.**
$$(1):\ \ \text{the floor-by-floor}\ V_3\ \text{census from directed edge lists (machine;}\ 8\ \text{floors named); the universal grammar is IT.85}(8)\text{'s lemma re-censused per vertex (machine)}$$
$$(2):\ \ b\equiv N\ (\mathrm{mod}\ 2)\ \text{from}\ N-3b=2a\ \text{even; exhaustive over all groupings for}\ N=0..60\ \text{(machine; the frozen segment agrees with Census FT.63's per-solid rows)}$$
$$(3),(4):\ \ \text{text scans against the frozen sources with live controls (machine: the scans cannot pass dead).}\ \blacksquare$$

**Phys.** A frozen row that overclaims its scope injures the record even where its conclusions
stand; the corpus's repair route is this one — a refinement register in a later tier, the frozen
text untouched, the conclusions re-stated at their true strength. Two parities that cannot
disagree are not two witnesses but one witness heard twice; the value of the second hearing is
that it certifies the two loci are counting the same integer at all.

---

### IT.91 — The boson lifecycle automaton: the adopted form, the bar, and the fifth terminal

**Thm.**
$$(1)\quad\textbf{ADOPTED (the Architect's disposition, verbatim scope): the five-terminal accessible-history automaton.}\qquad S=\{\text{emitted},\ \text{polygon-cycling},\ \text{gluon-read(bifurcate|unify)},\ \text{polygon-persistent}\}$$
$$\cup\ \text{Terminals}\ \{\text{baryon-return},\ \text{observer},\ D^-,\ J^-,\ \boldsymbol\omega\ (\text{persistent cycling})\};\qquad \text{the automaton is a READ-SEQUENCE,}\ \neg\text{a dynamics}\ [\mathrm{CT0.6}].$$
$$\textbf{THE HONEST COMPLETENESS FORM (adopted):}\qquad \boxed{\ \text{the boson ledger is a complete invariant of the ACCESSIBLE history; the silent terminals are exactly where completeness ends}\ }$$
$$(2)\quad\textbf{the global claim is BARRED.}\qquad \text{``the boson's ledger history determines the ENTIRE system'' fails on frozen ground (machine witness): ONE dark skeleton}$$
$$\Sigma_{P_4}\ (\text{bidirectional 4-cycle; every vertex}\ n=4,\ D^-\text{-configured}\ [\mathrm{CT4.1}])\ \times\ 16\ \text{all-nonnull}\ \kappa\text{-profiles}\ (\kappa\in\{1,2\}^4\ [\mathrm{FT.24};\ \mathrm{FT.32}(6)])$$
$$\Longrightarrow\ 5\ \text{distinct}\ \Theta_{\mathrm{int}}=2K_P\ \text{values}\ \{8,10,12,14,16\}\ \text{with IDENTICAL accessible channel data}\ =\ \text{NONE}\ [\mathrm{FT.62}(5):\ \text{dark floors carry ``no channel read at all''};\ \mathrm{FT.3}];$$
$$\mathrm{FT.3}\ \text{is the frozen bar:}\ (\delta h,\delta\tau)\text{-identical channels with}\ D^-\text{-differing interiors give}\ I_{o\leftarrow\Sigma}(\gamma)=I_{o\leftarrow\Sigma'}(\gamma);\qquad \mathrm{CT4.8}:\ \text{``equal boundary register counts}\ \Longrightarrow\ \text{indistinguishable interiors''}.$$
$$(3)\quad\textbf{the accessible-history form is DERIVED.}\qquad \text{a transit chain's accessible content is exactly its end reads:}\ q_{\mathrm{EM}}(c)=\tfrac12(\sigma_{s(c)}-\sigma_{t(c)})\ [\mathrm{EM.9}]$$
$$\text{and the interior telescopes:}\ \textstyle\sum_{\mathrm{interior}} f_v=\tfrac12(\sigma_{e_k}-\sigma_{e_1})=-q_{\mathrm{EM}}\ [\mathrm{EM.9b};\ \mathrm{D3.3}]\ —\ \text{machine: all}\ 254\ \text{sign chains for}\ k=1..7,\ \text{doubled integers, the sign caution honored};$$
$$\text{so the boson's accessible ledger determines the system's accessible sector up to CT4.8's boundary-register equivalence}\ [\mathrm{CT2.5}:\ \text{exterior measurements = resolvent residues}].$$
$$\textbf{THE HORIZON:}\ \text{completeness ends at the first accessibility-silent terminal}\ —\ D^-\ (\neg\exists\ \text{pole at any accessible rung; one-way}\ [\mathrm{CT4.2}])\ \text{or}\ J^-\ (\text{``unregistered content supports no accessible pole at any rung''}\ [\mathrm{FT.144}(4)]),$$
$$\text{content RETAINED and COUNTED,}\ \neg\text{deleted}\ [\mathrm{CT4.3};\ \mathrm{D4.2}],\ \neg\text{accessible}\ [\mathrm{D1.11}].$$
$$(4)\quad\textbf{the}\ \omega\textbf{-terminal is REQUIRED, and its habitat is exact.}\qquad \text{the four-terminal set is NOT exhaustive: on}\ \Sigma_L\ \text{every cycle vertex is}\ n\le3,\ O(2)=O(3)=0\ [\mathrm{FT.32}(2);\ \mathrm{CT0.6}]$$
$$\text{and}\ \neg\text{a tick-to-tick transition law}\ [\mathrm{CT0.6}]\ \Longrightarrow\ \text{no forced exit: lock-free cycling runs forever. Machine census: the frozen floors admitting an accessible lock-free cycle are EXACTLY}$$
$$\{\text{observed}\ \Sigma_{\min},\ \Sigma_L\ \forall L\ge2,\ \text{the IT.85}(5)\ \text{witness}\}\ =\ \mathrm{FT.62}(3)\text{'s lock-free unidirectional family};\qquad \Sigma_{12}\text{'s}\ 3\ \text{simple cycles ALL pass a locked junction}\ (q_1\ \text{or}\ p_2,\ n=4);$$
$$\Sigma_\triangle\ (n=6\ \text{everywhere}\ [\mathrm{FT.49}(5)])\ \text{and the dark polygon/Platonic floors}\ (n\ge4)\ \text{admit none.}\qquad \text{EXCLUSIVITY (machine): over the}\ 2\times5\times3=30\text{-cell condition census}$$
$$\text{(rung-window}\ \times\ \text{event-kind}\ \times\ \text{hosting-state), the five terminals take}\ 16\ \text{cells with}\ \textbf{0}\ \text{double-assignments;}\ 14\ \text{cells are transient states.}$$
$$(5)\quad\textbf{the baryon-return scope row.}\qquad \text{an accessible baryon-return needs three colour vertices at DISTINCT nodes, all unlocked}\ [\mathrm{IT.84}(3);\ \mathrm{CT3.17a}(1);\ \mathrm{D2.14}]:$$
$$\Sigma_{12}\ \text{has ONE}\ V_3\ \text{vertex, both would-be partners locked at}\ n=4\ [\mathrm{FT.35}(4)];\qquad \Sigma_\triangle/\text{Platonics/polygons host zero}\ [\mathrm{IT.85}(3),(8)];\qquad \Sigma_{\min}/\Sigma_L\ \text{are structurally colourless}\ [\mathrm{A1};\ \mathrm{FT.28}(3);\ \mathrm{FT.32}(4)].$$
$$\text{the only frozen-record network with three unlocked}\ n{=}3\ \text{cores is IT.85}(5)\text{'s constructible witness}\ —\ \text{whose cores are pairwise NON-ADJACENT, so}\ \varepsilon\text{-sealing needs attachment data}\ [\mathrm{D3.8};\ \mathrm{FT.35}(5)]:$$
$$\textbf{baryon-return fires accessibly on NO frozen Census floor}\ —\ \text{a SCOPE row,}\ \neg\text{a gap: the terminal belongs to the automaton, and is unrealized on every computed floor.}$$
$$(6)\quad\textbf{the guards and the vocabulary cash-out.}\qquad t_1\ \text{emitted}\to\text{cycling}:\ J^+=(+1,+1,+1)\ [\mathrm{CT0.3}]\ \text{onto}\ \Sigma_L\ (\exists L\ge2\ [\mathrm{FT.32}]);\ t_2\ \text{cycling}\to\text{gluon-read}: hosting requires a single-directed contact$$
$$[\mathrm{IT.85}(1)];\ \text{sealed interiors host nothing}\ [\mathrm{IT.85}(2),(8);\ \mathrm{CT4.4a}(3)];\ t_3\ \text{bifurcate/unify}:\ \Xi_3=\{(0,3),(1,2),(2,1),(3,0)\},\ \text{frozen floors realize}\ (2,1)\ \text{at EVERY}\ V_3\ \text{vertex, the mirror contact}\ (1,2)\ \text{is legal}$$
$$[\mathrm{CT0.11b}:\ n=2d^{\mathrm{bi}}+d^{\mathrm{uni}}=3];\qquad \text{exhaustive sealed-}V{=}4\ \text{census (4096 digraphs, machine): diagonal types only}\ —\ (0,3)/(3,0)\ \text{NEVER occur sealed, they require open ends}\ [\mathrm{IT.85}(9)];$$
$$t_4\ \text{gluon-read}\to\text{persistent}:\ V_2\ \text{sealed-reachable}\ —\ \text{the sealed digon keeps type-}(1,1)\ [\mathrm{FT.62}(5);\ \mathrm{IT.85}(6)];\qquad t_5\ \text{the terminal guards}\ [\mathrm{CT4.1};\ \mathrm{CT0.3};\ \mathrm{CT0.4};\ \mathrm{CT0.1};\ \mathrm{Def\text{-}H.35}].$$
$$\text{``excited state''} \equiv \text{the register state}\ E_{\mathrm{int}}\mapsto E_{\mathrm{int}}+1\ \text{per crystallized attachment}\ [\mathrm{CT0.3};\ \mathrm{FT.32}(1):\ E_{\mathrm{int}}=L],\ \neg\text{a spectral claim}\ [\mathrm{P5}];\qquad \text{``becomes a gluon'' is BARRED as ontology}\ —$$
$$\text{the read changes with the hosting vertex}\ [\mathrm{IT.89}(3)];\qquad J^\pm\ \text{ledger rows re-derived (machine): strict alternation}\ \Longrightarrow\ 1\ \text{admissible word per length}\ 0..8;\ \mathrm{Cat}_m=(1,1,2,5,14,42,132)\ [\mathrm{FT.144}(2);\ \mathrm{BM.7}(1)].$$
$$(7)\quad\textbf{no new open row.}\qquad \text{the automaton's kernel half is the Builder's construction (IN PROGRESS, vault claim}\ 6194835010\text{: the}\ \omega\text{-habitat census, the exclusivity, the trivalent-type split)},$$
$$\text{citing this tier's machine as its shadow; the terminals are read-names over frozen rows,}\ \neg\text{ontology}\ [\text{concept/0010}\ \S C];\qquad D^-\ \text{silence respected: no claim about locked content beyond retained/counted/}\neg\text{accessible.}$$

**Req.** A1, A7; D0.8, D1.4, D1.5, D1.11, D2.11, D3.3, D3.8 (Part 1); CT0.1, CT0.3, CT0.4, CT0.6, CT0.9, CT0.11b (Part 1); CT2.5, CT4.1, CT4.2, CT4.3, CT4.4a, CT4.8 (Part 2); CT3.17a, D2.14, D4.2 (Parts 1–2); EM.9, EM.9b (Part 2); FT.3, FT.24, FT.28(3),(5), FT.32(1),(2),(4),(6), FT.35(4),(5), FT.49(5), FT.62(3),(5), FT.144(2),(4) (Census/Part 3); BM.7(1), BM.134(5) (Part 4); IT.84(3), IT.85(1)–(6),(8),(9), IT.86(7), IT.89 (this tier); the paper-layer Caveat discipline (quoted read-vocabulary); P1, P5 [policy]; exhaustive cycle enumeration, cell censuses, sign-chain exhaustion, exact integer and doubled-integer arithmetic [math; machine: `carrier_read_tier.py` §C–§D; probe antecedent `boson_lifecycle.py` 11/11, consumed as the shadow by the Builder's kernel half].

**Pf.**
$$(1),(2):\ \ \text{the disposition's scope, verbatim; the bar witness is the machine census}\ (16\ \text{profiles},\ 5\ \Theta\ \text{values, identical empty accessible projection)}\ \text{with the seven frozen anchors attested verbatim (machine scan with live control)}$$
$$(3):\ \ \text{EM.9's table recomputed}\ 4/4;\qquad \text{the telescoping identity exhaustive over all}\ 2^{k}\ \text{sign assignments for}\ k=1..7\ (254\ \text{chains; machine; a wrong-identity control bites on the}\ (+,-)\ \text{cell)}$$
$$(4):\ \ \text{simple-cycle enumeration per floor}\ (\Sigma_{12}:\ 3\ \text{cycles, each through}\ n{=}4);\qquad \text{habitat}\ =\ \text{floors whose cycle vertices are all}\ n\le3;\qquad \text{the 30-cell census with a merge control (an artificial}\ D^-\vee J^-\ \text{merge IS detected)}$$
$$(5):\ \ V_3\ \text{censuses per floor with the locked-partner and distinct-node rows; core non-adjacency by edge membership (machine)}$$
$$(6):\ \ \text{the guards are the cited rows evaluated on the rebuilt floors}\ (\Sigma_L,\ L=2..8,\ \text{exact rungs,}\ O=0);\qquad \Xi_3\ \text{exact; the sealed-}V{=}4\ \text{enumeration over all}\ 2^{12}\ \text{digraphs (machine)}$$
$$(7):\ \ \text{the claim pointer and the scope clauses; no new mathematics.}\ \blacksquare$$

**Phys.** Follow one boson's ledger and you can determine the system — up to the first moment the
system stops answering. Where the polygon is lock-free, the honest end of the story is a fifth
terminal: *it is still cycling*. Where the ledger crosses into D⁻ or dissolves by J⁻, the content
is retained and counted and the story goes silent, and no reading of the boson's own history,
however complete, reaches behind that silence — which is not a defect of the ledger but the exact
shape of the lock: validity stays global, accessibility stays local, and the boundary between them
is where completeness ends.

---

**Open rows.** (none new) — Tier IT.25 opens **no row**: the carrier relativity, the refinements,
the adopted automaton form and the bar are all derived on frozen ground [IT.89; IT.90; IT.91];
the Builder's kernel half rides its own PR record (vault), and the dynamical side stays at IT-O1 —
untouched by this tier. The refinement register (IT.90) DISCHARGES the owes logged at concept/0008
§E and comms/0031 §1 (the IT.84(4) and IT.85(6) precision notes) — no further refinement is owed
on those texts at this level.

---

# $\langle qu(b(i(t|t))ick) \rangle$ — **Part 6 · Isotopic era** — Tier IT.26: the lock-ratio card and the n=3 triple peak — how dark a floor is per unit of what it retains, and the one vertex kind where the readable rows meet

**Level.** 6. **Era.** 2 (the Isotopic era). **Tier.** IT.26 — the disposition tier for
**arch/0008 G3** (vault issue #25): *"Freeze the two lock-ratio promotions (read-tier, no new
act)"* — (a) the size-free invariant O(2d)/d, machine-censused and placed as a Census-style card /
read-tier remark **beside FT.49 and CT4.5a**; (b) the n=3 triple peak, derived as a row with the
**teleological reading BARRED in the same clause** and the caption *"that is where the readable
universe lives"* **flagged ¬adopted caption material, never a citation**. Both candidates were
adjudicated in probe space first (`lock_ratio_and_n3.py`, 38 exact markers, mirrored in the vault;
the two candidate promotions were offered to the Architect at session 13s-addendum-4 and are
frozen here at his dispatch). This tier additionally carries **one correction of a frozen row**
(IT.94), which the G3 rider's machine exposed and which AT.63(2) requires to ride a later tier
rather than an in-place edit.
**Tags.** IT.92–IT.94. **Pattern.** the read-tier / card shape (IT.16, IT.22, IT.25's pattern):
no new primitive, no new act, no new open row — frozen rows read at their own loci, one quotient
taken, one conjunction named, one text corrected.
**Status.** discovery-phase working tier. No declaration issues at this tier (machine-scanned at
IT.94); §Cal-IT stays value-free and unchanged; no clause of Parts 1–4, of Level 5's closed record,
or of Tiers IT.1–IT.25 is modified [AT.63(2)] — IT.94 IS the later-tier vehicle the discipline
requires. No measured value enters [P5]; no new dimensionful scale [P1] — $\mathfrak h$ stays
symbolic wherever cited; the ratio rows are quotients of two COUNTS and are therefore
$\mathfrak q^0$ (no currency is converted [BM.83; BM.134(5)]).
**Machine.** `era2/level6_isotopic/checks/lock_ratio_tier.py` → **exact** (integers and Fractions
only; exhaustive multinomial term breakdowns; NO floating point in any assertion; the
mutation-tested negatives are markers M1–M4 inside the checker — each asserts that a mutated
constant reddens the same predicate the frozen constant passes). Probe-space antecedents, retained
as the working record: `lock_ratio_and_n3.py` (36 markers) and the G3 rider
`generation_selection.py` (probe-space only — its verdict is negative and is recorded at IT.94(4);
promotion was never requested).
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier IT-tags only. No
forward pointer is used as a premise.
**Mandate.** arch/0008 G3, executed in full: the two promotions frozen as read-tier rows beside
their frozen neighbours; the bars and the caption flag in the same clause as the peak; the
rider's findings recorded, including the frozen-text correction it exposed.

---

### IT.92 — The size-free lock-ratio card (beside FT.49 and CT4.5a)

**Thm.**
$$(1)\quad\textbf{THE INVARIANT.}\qquad \text{for any}\ d\text{-regular bidirectional DARK floor}\ [\mathrm{FT.42}(1),(2);\ \mathrm{FT.62}(1),(2);\ \mathrm{Def\text{-}H.20}]:$$
$$\text{retained}:\ E_{\mathrm{int}}=2E\ \text{with}\ E=Vd/2\ \text{(handshaking)}\ \Longrightarrow\ E_{\mathrm{int}}=Vd;\qquad \text{locked}:\ \text{every vertex dark at}\ n=2d\ \Longrightarrow\ \textstyle\sum_vO=V\cdot O(2d);$$
$$\boxed{\ \frac{\text{locked}}{\text{retained}}=\frac{V\cdot O(2d)}{V\cdot d}=\frac{O(2d)}{d}=\frac{2^{2d+1}-16}{d}\ }\qquad [O(n)=\max(0,2^{n+1}-16),\ \mathrm{CT0.6}]\ —\ V\ \textbf{CANCELS: the ratio is a function of the CHANNEL DEGREE ALONE, independent of the skeleton's size.}$$
$$(2)\quad\textbf{the card rows (machine: all exact).}\qquad d=3:\ \frac{O(6)}{3}=\frac{112}{3}\ \text{for the tetrahedron, the cube AND the dodecahedron}\ —\ \text{one ratio across}\ V=4,8,20:$$
$$\text{tetrahedron}\ (E_{\mathrm{int}}{=}12,\ \text{locked}\ 448);\quad \text{cube}\ (24,\ 896);\quad \text{dodecahedron}\ (60,\ 2240)\qquad [\mathrm{FT.62}(2)\ \text{dark column:}\ 448,896,2976,2240,24384];$$
$$\text{the polygon family}\ (d=2):\ \frac{O(4)}{2}=\frac{16}{2}=8\ \textbf{exactly, at every length}\ [\mathrm{FT.62}(1):\ \text{dark}\ n(v){=}4\ \forall v;\ \mathrm{CT4.1a}(2):\ \text{``uniform minimal saturation}\ \ldots\ \text{independent of cycle length''}]\ —$$
$$\text{machine:}\ L\in\{3,4,5,6,7,12,100\}\ \text{all give exactly}\ 8;\qquad \text{the full ladder}\ d=2..10:\ \Bigl(8,\ \tfrac{112}{3},\ 124,\ \tfrac{2032}{5},\ \dots\Bigr)\ \textbf{strictly increasing}\ (4^d/d\ \text{growth}).$$
$$(3)\quad\textbf{the right zero (adversarial row).}\qquad d=1:\ O(2)=\max(0,2^3-16)=0\ \Longrightarrow\ \text{ratio}\ 0\ —\ \text{the digon family}\ [\mathrm{FT.28}]\ \text{and the unidirectional cycle ladder}\ [\mathrm{FT.32}]$$
$$\text{are exactly FT.42}(2)\text{'s lock-free family, and the invariant returns}\ 0\ \text{for it: the law does not over-fire.}$$
$$(4)\quad\textbf{the two non-regular baryon-type cells, for contrast (machine).}\qquad \Sigma_{12}:\ E_{\mathrm{int}}=6\ [\mathrm{FT.35}(2)],\ \text{locked}\ 2\cdot O(4)=32\ [\mathrm{FT.35}(4):\ q_1,p_2\ \text{at}\ n{=}4],\ \text{ratio}\ \tfrac{16}{3};$$
$$\Sigma_\triangle:\ E_{\mathrm{int}}=6\ [\mathrm{FT.49}(1)],\ \text{locked}\ 3\cdot O(6)=336\ [\mathrm{FT.49}(5):\ n{=}6\ \text{at}\ A,B,C],\ \text{ratio}\ 56\ —\ \text{both far above the polygon family's}\ 8,$$
$$\text{the quantitative form of ``born together''}\ [\mathrm{FT.35}\ \mathrm{Rmk};\ \mathrm{IT.84}(6)\ \text{dichotomy}]:\ \text{composite fermion structure and saturation content scale together.}$$
$$(5)\quad\textbf{the currency row.}\qquad \text{the ratio is a quotient of two COUNTS}\ —\ \text{locked register directions}\ [O(n);\ \mathrm{D0.9}]\ \text{over retained edge-units}\ [E_{\mathrm{int}}]$$
$$\text{so it is}\ \mathfrak q^0:\ \text{no currency is converted, no}\ \ln2/\mathfrak h\ \text{factor is divided out or across}\ [\mathrm{BM.83};\ \mathrm{BM.134}(5)];\qquad \text{P1: no dimensionful scale enters.}$$
$$(6)\quad\textbf{placement.}\qquad \text{the card sits beside FT.49's}\ \Sigma_\triangle\ \text{card and CT4.5a's dust ensemble as the static quotient of the lock ledger:}$$
$$\mathrm{CT4.5a}\ \text{gives the exact dust density polynomial per vertex};\ \mathrm{FT.62}(2)\ \text{the locked columns};\ \text{this row their size-free quotient}\ —\ \text{no new act, no new object.}$$

**Req.** A7; D0.8, D0.9 (Part 1); CT0.5, CT0.6, CT0.11 (Part 1); CT4.1, CT4.1a(2),(3), CT4.5a (Part 2); FT.17, FT.28, FT.32, FT.35(2),(4), FT.42(1),(2), FT.49(1),(5), FT.62(1),(2) (Census); Def-H.20 (Census); IT.84(6) (Tier IT.24); BM.83, BM.134(5) (Part 4); P1, P5 [policy]; exact integer and Fraction arithmetic, handshaking cross-checks [math; machine: `lock_ratio_tier.py` §A; probe antecedent `lock_ratio_and_n3.py` §A, mirrored].

**Pf.**
$$(1):\ \ E=Vd/2\ \text{is handshaking on the}\ d\text{-regular undirected skeleton (machine cross-check per solid:}\ E_{\mathrm{int}}=2E=Vd\ \text{against FT.42}(1)\text{);}$$
$$\text{the dark rung is}\ n(v)=2d\ \forall v\ [\mathrm{FT.62}(1);\ \mathrm{CT0.11b}];\qquad \textstyle\sum_vO=V\cdot O(2d)\ \text{is the FT.62}(2)\ \text{dark column; the quotient cancels}\ V$$
$$(2),(3):\ \ \text{direct exact evaluation}\ (2^{2d+1}-16)/d\ \text{at each}\ d;\ \text{the polygon rows use FT.62}(1)\text{'s}\ n(v){=}4;\ O(2){=}0\ \text{by CT0.6's ladder}$$
$$(4):\ \ \text{the rung tuples re-derived from FT.35's and FT.49's own edge lists (machine:}\ \Sigma_{12}\ (3,4,4,2),\ \Sigma_\triangle\ (6,6,6)\text{);}\ O(4){=}16,\ O(6){=}112\ [\mathrm{CT0.6}]$$
$$(5),(6):\ \ \text{the cited currency and placement clauses; no new mathematics.}\ \blacksquare$$

**Phys.** Ask a dark floor how much of what it holds is behind the lock, per unit of what it
retains, and the answer does not depend on how big the floor is — only on how densely it is wired.
The three cubic-skeleton solids of degree three, five-fold apart in size, carry the same darkness
ratio 112/3; the polygon family, minimally saturated, carries the smallest locked ratio of all, 8;
and the lock-free ladder carries exactly zero. Darkness is a property of the wiring degree, not of
the scale — which is the static, size-free companion of CT4.5a's dust ensemble and the number
behind the qualitative claim that a more densely wired floor is overwhelmingly dark.

---

### IT.93 — The n=3 triple peak, and the bar on reading it as purpose

**Thm.**
$$(1)\quad\textbf{three frozen rows peak at the SAME rung, by three different mechanisms.}\qquad (a)\ \textbf{capacity: colour HOSTS at}\ n{=}3\ \text{and nowhere else}$$
$$[\mathrm{CT0.13}:\ \mathrm{strong}\in\mathcal A(n)\iff n\ge3;\qquad \mathrm{CT4.4a}(1):\ \iota_n\ \text{exists exactly for}\ n\le3;\qquad \mathrm{CT4.4a}(3):\ \text{``hosting dies at rung 3''}]\ —$$
$$\text{a CAPACITY fact from}\ C_{\mathrm{cap}}=16\ [\mathrm{CT0.6}];$$
$$(b)\ \textbf{counting: accessible entropy per vertex is MAXIMAL at}\ n{=}3:\qquad \text{accessible}(v)\implies S(v)\le3\ln2\ \text{nats}=3\ \text{bits, ``attained at}\ n{=}3\text{''}\ [\mathrm{CT4.9}(1)]$$
$$\text{(a rung-}n\ \text{vertex carries}\ n\ \text{slots}\ [\mathrm{D3.1}]\ \text{and one bit per directed real edge}\ [\mathrm{CT0.9}]:\ 3\ \text{slots}=3\ \text{bits)}\ —\ \text{a COUNTING fact};$$
$$(c)\ \textbf{type: the EM read requires a pass-through, and the reachable rung-3 types}\ (2,1)/(1,2)\ \text{have one}\ [\mathrm{D3.3}:\ f_v\ \text{at type-}(1,1);\ \mathrm{FT.42}(4):\ \mathrm{EM}\in\mathcal A\iff\exists v:f_v\ne0;$$
$$\mathrm{IT.85}(1),(6);\ \mathrm{IT.89}(2)]\ —\ \text{while the EM-blind extremes}\ (0,3)/(3,0)\ \text{are unreachable in any sealed network}\ [\mathrm{IT.84}(2),\ \text{exhaustive}]\ —\ \text{a TYPE fact.}$$
$$(2)\quad\textbf{THE CONJUNCTION (the derived row).}\qquad \text{conjoined with the contact-gating biconditional}\ [\mathrm{IT.85}(1):\ n(v){=}3\iff d{=}1\ \text{plus exactly one single-directed contact}]:$$
$$\boxed{\ \text{ONE vertex kind is simultaneously the colour-hosting site, the accessible-entropy maximum, and an EM-readable site}\ }\ —$$
$$\text{and it exists only at a single-directed-edge contact on a}\ d{=}1\ \text{channel. Everywhere else the rungs are even:}\ n{=}2\ \text{photon-side only}\ [\mathrm{IT.85}(6)],\ n\ge4\ \text{sealed-and-locked}\ [\mathrm{CT4.1}].$$
$$(3)\quad\textbf{the entropy coordinates of the lock (frozen anchor, re-cited).}\qquad \text{in CT4.7's triangle}\ (S_{\mathrm{raw}},\ S_{\mathfrak L}=n_{\mathcal R}\ln2\ [\mathrm{CT1.29}]),\ D^-\ \text{sits at}\ (\min_{\mathrm{acc}},\ \max\wedge\neg\text{accessible}):$$
$$\text{maximal ledger entropy, minimal accessible entropy}\ —\ \text{``retention without propagation'' has exact coordinates, and the peak}\ 3\ln2\ \text{of}\ (1)(b)\ \text{is what the contact vertex saturates.}$$
$$(4)\quad\textbf{BAR — the teleological reading, in the same clause.}\qquad \text{the sentence ``the three peaks coincide BECAUSE the framework optimizes readability'' (or any purpose,}$$
$$\text{design, or selection wording) is}\ \textbf{BARRED}:\ \text{no rates are declared}\ [\mathrm{Cal\text{-}F}],\ \text{no tick-to-tick transition law exists}\ [\mathrm{CT0.6}:\ \text{``ledger accounting}\ \ldots\ \neg\text{a tick-to-tick transition law''}],$$
$$\text{and no optimization principle is an axiom, a definition, or a derived row of the corpus. The coincidence is a CONJUNCTION of derived rows at one rung}\ —$$
$$\textbf{never an identification of the three 3's:} the mechanisms are distinct (capacity / counting / type), and claiming they are the ``same'' three is numerology.$$
$$(5)\quad\textbf{the caption flag (the dispatch's wording, frozen here).}\qquad \text{``that is where the readable universe lives'' is}\ \textbf{flagged}\ \neg\textbf{adopted caption material}\ —$$
$$\text{a presentational phrase, never a citation, never a row; the citable content of this tier is}\ (1),(2),(3)\ \text{with the bar}\ (4)\ \text{attached.}$$
$$(6)\quad\textbf{compatibility row.}\qquad \mathrm{CT4.9}(2)\text{'s per-region area bound}\ S_{\mathrm{acc}}(\mathcal B)\le\frac{A}{\mathfrak h^2}\ \text{bits is compatible and complementary: the vertex bound}\ (3\ \text{bits, attained at}\ n{=}3)$$
$$\text{is what the contact gate saturates; the area bound is what a region of such vertices can hold. Both frozen; neither extended;}\ \mathfrak h\ \text{symbolic}\ [\mathrm{P1}].$$

**Req.** D3.1, D3.3 (Part 1); CT0.6, CT0.9, CT0.13 (Part 1); CT4.1, CT4.4a(1),(3), CT4.7, CT4.9(1),(2) (Part 2); CT1.29 (Part 1); FT.42(4) (Census); IT.84(2), IT.85(1),(6), IT.89(2) (Tiers IT.24–IT.25); Cal-F [policy register]; P1, P5 [policy]; exact ladder arithmetic [math; machine: `lock_ratio_tier.py` §B].

**Pf.**
$$(1):\ \ \text{the three cited rows, each attested verbatim against the frozen sources (machine attestation scans with live controls)}$$
$$(2):\ \ \text{IT.85}(1)\text{'s biconditional applied to the three peaks: the hosting site exists exactly at the contact; CT4.9}(1)\text{'s attainment clause is ``attained at}\ n{=}3\text{''; the reachable-type census is IT.84}(2)\text{'s exhaustive sealed result plus IT.85}(9)\text{'s open-end grammar}$$
$$(3):\ \ \mathrm{CT4.7}\ \text{re-cited; no computation}$$
$$(4),(5):\ \ \text{the bar and the flag are the dispatch's own requirements frozen as rows; the numerology guard is the distinctness of the three mechanisms}\ (1)(a),(b),(c)$$
$$(6):\ \ \text{the cited bound;}\ \mathfrak h\ \text{never evaluated.}\ \blacksquare$$

**Phys.** Three questions — where can colour live, where is a vertex most readable, where can the
electromagnetic read pass through — are asked independently in three different vocabularies
(capacity, counting, type), and the frozen rows answer all three with the same rung. The tier
states that conjunction and nothing grander: the corpus contains no purpose, no rate and no
selection principle that could make the coincidence a design, and the bar says so in the same
breath as the row. What remains is structural and sharp: one vertex kind, existing only where a
single directed contact meets a one-channel core, is the locus where the framework's three
readabilities meet — every other rung is either too sparse to host, or too dense to read.

---

### IT.94 — The rider's record: a frozen-row correction (FT.63's cube spectrum) and the generation-count verdict

**Thm.**
$$(1)\quad\textbf{THE CORRECTION (supersession row; the frozen text is untouched}\ [\mathrm{AT.63}(2)]\textbf{).}\qquad \text{Census FT.63's even-}\varepsilon\ \text{row ends: ``the icosahedron}\ b\in\{0,2,4\},\ \text{the dodecahedron}\ b\in\{0,2,4,6\},\ \textbf{the cube}\ b\in\{0,2,4\}\text{''}.$$
$$\textbf{the cube's spectrum is}\ \{0,2\},\ \neg\{0,2,4\}.\ \text{Proof from the row's OWN equation:}\ 2a+3b=V\ \text{at the cube's}\ V=8\ \text{gives}\ 3b\le8\ \Longrightarrow\ b\le2\ (b\ \text{even});$$
$$b=4\ \text{would require}\ 3\cdot4=12>8\ \text{attachment slots}\ —\ \text{impossible. The frozen}\ g(8)=385\ \text{confirms by term breakdown (machine):}\ 385=105\ (b{=}0:\ \tfrac{8!}{4!\,2^4})+280\ (b{=}2:\ \tbinom{8}{2}\cdot\tfrac{6!}{2!\,(3!)^2}),$$
$$\text{and no}\ b{=}4\ \text{term can exist}\ [\mathrm{CT3.17a}(2)\text{'s closed form;}\ g(8)=385\ \text{frozen at Census FT.42}(5)\text{'s cube card and re-derived in the IT.24 checker}].$$
$$\text{the icosahedron's}\ \{0,2,4\}\ \text{IS correct}\ (V{=}12\ \text{admits}\ b{=}4:\ 3\cdot4=12,\ a{=}0)\ —\ \text{the defect's shape is consistent with a transcription of the icosa row onto the cube.}$$
$$\textbf{provenance and scope:}\ \text{the frozen suite's own FT.63 companion}\ \texttt{era1/verification/checks/verify\_H\_solidcards.py}\ \textbf{certifies the cube breakdown}$$
$$g(8)=\{(4,0){:}105,\ (1,2){:}280\}\ \text{-- spectrum}\ \{0,2\}\ \text{-- so the frozen 80/80 green ALREADY certifies the corrected value, and the frozen text's ``cube}\ b\in\{0,2,4\}\text{''}$$
$$\textbf{contradicts its own frozen machine and was never certified by any checker (machine scan).}\ \text{This correction joins the canon-erratum register}\ [\mathrm{BM.140}(6);\ \mathrm{FT.116}(5)\ \text{lineage}]$$
$$\text{for the closure pipeline; the even-}\varepsilon\ \text{THEOREM itself}\ (V\ \text{even}\ \Rightarrow\ b\ \text{even},\ \text{certified per solid by the same checker})\ \text{is untouched and stands}\ [\mathrm{IT.84}(5);\ \mathrm{IT.90}(2)].$$
$$(2)\quad\textbf{the per-solid spectra, re-derived (machine).}\qquad \text{from}\ 2a+3b=V\ \text{with}\ g(V)\ \text{term breakdowns, all exact:}$$
$$\text{tetrahedron}\ V{=}4:\ b\in\{0\},\ g{=}3;\quad \text{octahedron}\ V{=}6:\ b\in\{0,2\},\ g{=}25=15{+}10\ [\mathrm{FT.63}:\ 15\,\delta^3{+}10\,\varepsilon^2];\quad \text{cube}\ V{=}8:\ b\in\{0,2\},\ g{=}385=105{+}280;$$
$$\text{icosahedron}\ V{=}12:\ b\in\{0,2,4\},\ g{=}164395;\qquad \text{dodecahedron}\ V{=}20:\ b\in\{0,2,4,6\},\ g{=}292938721075\ —\ \text{every total equal to the frozen}\ g(V)\ [\mathrm{CT3.17a}(2)].$$
$$(3)\quad\textbf{the mod-6 gate is NON-DISCRIMINATING on the solids.}\qquad |\mathrm{Colour}|=3b\ \text{with}\ b\ \text{even}\ \Longrightarrow\ 3b\equiv0\ (\mathrm{mod}\ 6)\ \text{for EVERY Platonic grouping}\ [\mathrm{IT.84}(5):\ \mathrm{mod}\,2\wedge\mathrm{mod}\,3=\mathrm{mod}\,6]:$$
$$\text{the gate organizes lock-freedom by residue}\ (0\to\text{lock-free pure-}\varepsilon\ \text{possible};\ 2,4\to\delta\text{-containing};\ 3\to\text{locked pure-}\varepsilon;\ 1,5\to\text{locked mixed}),\ \text{and on the five solids every grouping lands in class}\ 0$$
$$\text{so the gate distinguishes NOTHING among them}\ —\ \text{it cannot select a count, still less three.}$$
$$(4)\quad\textbf{the generation-count verdict (era-1 HistLog item 21(d), recorded; probe-space rider, NOT promoted).}\qquad \text{21(d): ``the cover-class pool is counted exactly}\ [\mathrm{FT.78}:\ 7,\ 264,\ 10]\ \textbf{but nothing selects three''}.$$
$$\text{the rider tested whether the mod-6 gate supplies the missing selector: it does not}\ (3);\ \text{and the}\ 3\text{-shaped quantities that DO occur}\ —\ g(4){=}3,\ \text{the icosahedron's}\ |\{0,2,4\}|{=}3,\ \text{the dodecahedron's}\ b_{\max}/2{=}3$$
$$\text{are MULTIPLE candidates with no selector among them, which under the standing}\ (c4)\text{-discipline is the numerology bar, not a derivation.}\ \textbf{21(d) SURVIVES: the selection principle remains open,}$$
$$\text{downstream of item 20's deficits 1 and 3}\ [\mathrm{FT.87}(9)\text{'s refutation untouched}];\qquad \text{no promotion is requested; the rider stays probe-space}\ (\texttt{generation\_selection.py},\ \text{mirrored}).$$
$$(5)\quad\textbf{verdict, bars, status.}\qquad \text{no declaration issued (machine-scanned); no new open row}\ —\ 21(d)\ \text{is an era-1 HistLog item and stays exactly where it was, now with the mod-6 route recorded as TESTED-and-NEGATIVE};$$
$$\S\mathrm{Cal\text{-}IT}\ \text{unchanged};\ \text{the mutation-tested negatives are markers M1--M4 of the checker (mutated constants reddening the frozen predicates)};\ \text{frozen text never edited}\ [\mathrm{AT.63}(2)].$$

**Req.** A1; CT3.17, CT3.17a(2) (Part 2); FT.42(5), FT.63, FT.78, FT.87(9) (Census); HistLog item 21(d) (era-1 record); IT.84(5), IT.90(2) (Tiers IT.24–IT.25); AT.63(2) (Level 5); BM.140(6), FT.116(5) (the erratum-register lineage); exhaustive multinomial enumeration, exact integer arithmetic [math; machine: `lock_ratio_tier.py` §C + the rider `generation_selection.py` (probe-space, mirrored)].

**Pf.**
$$(1):\ \ 3b\le V\ \text{at}\ V{=}8\ \text{gives}\ b\le2;\qquad \text{the}\ 385=105+280\ \text{breakdown is exact multinomial enumeration (machine), matching CT3.17a}(2)\text{'s closed form};\qquad \text{the suite-scan is a grep with a live control (machine)}$$
$$(2):\ \ \text{per-solid enumeration of}\ 2a+3b=V\ \text{with exact term counts; totals checked against the frozen}\ g(V)\ \text{values (machine)}$$
$$(3):\ \ b\ \text{even}\ \Longrightarrow\ 3b\equiv0\ (\mathrm{mod}\ 6):\ \text{one line of modular arithmetic, exhaustively censused over all spectra of}\ (2)$$
$$(4):\ \ \text{the candidate census is exact and finite (machine); the}\ (c4)\text{-discipline application is the standing none-or-many bar}$$
$$(5):\ \ \text{the status clauses; the scans are markers D1--D4 of the checker.}\ \blacksquare$$

**Phys.** A census row is frozen prose, and frozen prose can carry a typo even when the theorem
around it is exact: the cube's baryon-number spectrum is {0,2}, because eight slots cannot feed
four triples, and the corpus's own g(8)=385 has always said so in its term breakdown. The
correction changes no theorem and no verdict — the even-ε theorem stands, the mod-6 ladder stands
— and it closes one door on an old open question honestly: the mod-6 gate, asked whether it
selects three generations, answers that on the Platonic floors it does not even distinguish among
them. Item 21(d) remains open, as it was, now with one more tested-and-negative route on the
record.

---

**Open rows.** (none new) — Tier IT.26 opens **no row**: the lock-ratio card, the triple-peak
conjunction with its bar, and the FT.63 cube-spectrum correction are all derived on frozen ground
[IT.92; IT.93; IT.94]; era-1's 21(d) stays open exactly where it stood, with the mod-6 route
recorded as tested-and-negative; the dynamical side stays at IT-O1 — untouched by this tier.
