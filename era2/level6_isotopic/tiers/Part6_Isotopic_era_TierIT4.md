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
