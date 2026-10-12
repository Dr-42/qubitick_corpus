# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Molecular era** — Tier ML.2: the 1p-kn isotopic family and the contraction-grammar phase transitions

**Level.** 6. **Era.** 2 (the Molecular era). **Tier.** ML.2 — the 1p-$k$n family as support
classes: the triple-certified contraction grammar, the family census with its exact phase
structure, the $E_{\mathrm{int}}$ floors, the capacity/mask adjudication, and the lepton
saturation flag.
**Tags.** ML.6–ML.8. **Pattern.** the construction tiers (ML.1's shape) with the premise audit
logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-ML
stays empty; no clause of Parts 1–4 or of Level 5's closed record is modified [AT.63(2)].
**Machine.** `era2/level6_molecular/checks/isotopic_family.py` → **8/8 exact**;
`run_all_level6.py` → the level runner (gate first); `check_level6_format.py` → the gate over
both Part 6 documents. Exact arithmetic: integer set-partition enumeration (exhaustive to
$N=8$), the grammar recurrence, exact factorials/binomials, `Fraction` shares, polynomial
convolution (Vandermonde), symbolic multiples of $\ln2$ and $\pi$.
**No floating point in any assertion. No measured isotope datum enters any clause [P5]. No
species identification [Def-BM.3(1),(7)] — "protium/deuterium/tritium/hydrogen-4" stay quoted
labels of the identification layer; the derived objects are the SUPPORT CLASSES.**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier ML-tags only.
**Mandate.** The Architect's directive: *"Construct the 1p-kn Isotopic Family and the
Contraction Grammar Phase Transitions … at $k=3$ (1p3n, which has $N=4$ colour attachments) the
screen and the mask will close something … this aligns with the contraction grammar
[Def-BM.9(3), BM.31]: for $N\ge4$ the $\delta$-sealings enter the ensemble, breaking the pure
$\varepsilon$-protection of the $N=3$ baryon."* — executed with three premise corrections logged
at ML.8(2); the Architect's standing flag (ML.4 acquires an exception when multi-$(p,n,e)$
systems are calculated) is honored and recorded, $\neg$pre-empted.

---

### ML.6 — The contraction grammar, triple-certified; the 1p-kn family census; and the exact locus of the phase transition

**Thm.**
$$(1)\quad\textbf{THE GRAMMAR ENGINE (triple-certified):}\qquad g(N)=\#\{\text{partitions of}\ N\ \text{attachments into contraction groups of size}\ 2\ (\delta)\ \text{and}\ 3\ (\varepsilon)\}\ \ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{CT3.17a}(2);\ \mathrm{FT.41}(\mathrm b)]$$
$$\textbf{three independent machines agree entrywise:}\ \ \text{exhaustive enumeration}\ (N\le8),\qquad g(N)=(N{-}1)g(N{-}2)+\binom{N-1}2g(N{-}3),\qquad g(N)=\!\!\sum_{2a+3b=N}\!\!\frac{N!}{a!\,2^a\,b!\,6^b}\ \ \text{with the full}\ (a,b)\ \text{breakdown};$$
$$\textbf{the frozen rows reproduce EXACTLY:}\ \ g=(1,1,3,10,25,105),\quad g_\delta=(1,\mathbf0,3,10,15,105),\quad g_\varepsilon=(0,1,0,0,10,0)\ \ \text{for}\ N{=}2..7\ \ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{BM.31}(2)];$$
$$g_\delta+g_\varepsilon=g\ \ \forall N;\qquad g_\varepsilon(N)\ne0\iff3\mid N\ \ (N{=}2..18);\qquad g(1)=0\ \ \textbf{— the lone attachment is never sealed}\ [\mathrm{CT3.17a}]$$
$$(2)\quad\textbf{THE FAMILY, as support classes:}\qquad\text{the 1p-}k\text{n composite of}\ N_{\mathrm{nuc}}{=}k{+}1\ \text{nucleons carries}\ \boxed{\ N=3(k{+}1)\ \text{attachments}\ }\ \text{— each nucleon is an}\ \varepsilon\text{-sealed 3-juncture, its THREE attachments sealed inside as one}\ \varepsilon\text{-type triple}\ [\mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(5);\ \mathrm{D3.9}];$$
$$\text{the attachment count is BOUNDARY DATA,}\ \neg\text{a summed-over structure}\ [\mathrm{Def\text{-}BM.9}(4)];\qquad\text{each}\ N\ \text{is its own support class}\ [\mathrm{Def\text{-}BM.9}(5)];\qquad\text{junction fusion/sharing is}\ \neg\text{constructed}\ (\mathrm{ML\text{-}O4})$$
$$(3)\quad\textbf{THE FAMILY CENSUS}\ (k{=}0..5;\ \text{machine: closed form}=\text{recurrence at every member}):\qquad\begin{array}{c|cccccc}k&0&1&2&3&4&5\\\hline N&3&6&9&12&15&18\\ g(N)&1&25&1540&164395&\cdot&\cdot\\ g_\varepsilon&1&10&280&15400&\cdot&\cdot\\ g_\delta&0&15&1260&148995&\cdot&\cdot\\ \delta\ \text{share}&0&\tfrac35&\tfrac9{11}&\tfrac{387}{427}&\cdot&\cdot\\ (a,b)\ \text{blocks}&(0,1){:}1&(3,0){:}15,\ (0,2){:}10&(3,1){:}1260,\ (0,3){:}280&(6,0){:}10395,\ (3,2){:}138600,\ (0,4){:}15400&-&-\end{array}$$
$$g(12)=164395=10395+138600+15400\ \ \textbf{exactly};\qquad\text{the}\ \delta\ \text{share is STRICTLY INCREASING in}\ k;\qquad\text{the pure-}\varepsilon\ \text{sector NEVER vanishes}\ (g_\varepsilon(3m)>0\ \forall\ \text{members})$$
$$(4)\quad\textbf{THE PROTECTION AND THE FIRST MIXING:}\qquad k{=}0\ (N{=}3):\ \text{the UNIQUE grouping is the}\ \varepsilon\text{-triple — the protection is forced}\ [\mathrm{BM.31}(1):\ g(3){=}1,\ g_\delta(3){=}0;\ \text{a}\ \delta\text{-sub-pairing on a 3-support leaves one dangling}\implies\partial_{\mathrm{col}}\ne\varnothing\implies\mathcal C{=}0\ [\mathrm{D2.14};\ \mathrm{FT.19}]];$$
$$k{=}1\ (N{=}6):\ \textbf{the FIRST family member admitting}\ \delta\text{-sealings — BM.31(2)'s frozen mix re-derived exactly:}\ \ \tfrac{15}{25}=\tfrac35\ \delta\text{-containing vs}\ \tfrac{10}{25}=\tfrac25\ \text{pure-}\varepsilon$$
$$(5)\quad\textbf{THE PHASE TRANSITION, exactly located:}\qquad\boxed{\ \textbf{the grammar transition is at}\ N{=}4:\ \ g_\delta\ 0\to3,\ \ \text{``the protection is unique to}\ N{=}3\text{''}\ [\mathrm{BM.31}(2)]\ \text{— frozen and re-derived}\ }$$
$$\textbf{inside the family}\ (N\equiv0\ (\mathrm{mod}\ 3))\ \text{the transition falls at the DEUTERON}\ (N{=}6),\ \neg\text{at 1p3n};\qquad\text{the}\ N{=}4\ \text{support itself is the double-mesonic (``tetraquark-type'', quoted) support:}\ g(4){=}3\ \text{(the three perfect matchings), ALL}\ \delta,\ g_\varepsilon(4){=}0$$
$$(6)\quad\textbf{THE STATISTICS COMPOSITION}\ [\mathrm{BM.31}(4);\ \text{Census}\ \mathrm{FT.49}(3);\ \mathrm{FT.22};\ \mathrm{BM.129}]:\qquad\text{pure-}\varepsilon\ \text{groupings: baryon-type}\ \Theta_{\mathrm{int}}\in4\mathbb Z;\qquad\text{EVERY}\ \delta\text{-containing grouping: only the}\ 2\mathbb Z\ \text{class};\qquad4\mathbb Z\subsetneq2\mathbb Z\ (\Theta_{\mathrm{int}}{=}2\ \text{meson-admissible, baryon-excluded — the partial separator});$$
$$\text{sector counts per member:}\ \ k{=}0:\ 1\ \text{baryon-type};\quad k{=}1:\ 10\ \text{vs}\ 15;\quad k{=}2:\ 280\ \text{vs}\ 1260;\quad k{=}3:\ 15400\ \text{vs}\ 148995\ \ \text{— the ensemble carries BOTH statistics classes from the deuteron on, as grouping sectors}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(6);\qquad\textbf{re-produced frozen rows:}\ \mathrm{Def\text{-}BM.9}(3),\ \mathrm{BM.31}(1),(2),(4);\qquad\neg\text{a declaration},\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(7)],\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** A7 (Part 1); P5, CT0.5, CT0.6, CT3.11(1), CT3.17, CT3.17a(2), D2.13, D2.14, D3.1, D3.9, FT.19, FT.22, FT.41(b) (Parts 1–2); Def-H.32(1), FT.34(3),(5) (Part 3); ML.1(4), ML.4(5) (this level); AT.29, AT.32(1), AT.50(3),(4),(5), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.9(1),(2),(3),(4),(5), BM.2(1), BM.17(1), BM.28(4), BM.31(1),(2),(3),(4),(5),(6), BM.129, Census FT.35(5), FT.49(3) (Part 4); exhaustive set-partition enumeration, the partition recurrence, exact factorials and binomials [math; machine: `isotopic_family.py` §§A–C, 4/4].

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

### ML.7 — The family's prices, floors, charge, and the capacity adjudication: what closes, what never does

**Thm.**
$$(1)\quad\textbf{THE}\ E_{\mathrm{int}}\ \textbf{CENSUS (two derived readings):}\qquad\text{per nucleon}\ E_{\mathrm{int}}=6=2{+}2{+}2\ \ (\text{two materialized 2-cycles + the bidirectional connector})\ [\mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(2)];\qquad E_{\mathrm{int}}=|R|\ \text{is a cardinality, EXACTLY ADDITIVE over the disjoint union and the connector's edges}\ [\mathrm{AT.40}(3)];$$
$$\textbf{DISJOINT:}\ \ E_{\mathrm{int}}=6(k{+}1)=(6,12,18,24,30,36);\qquad\textbf{TREE-CONNECTED by}\ k\ \Sigma_{12}\text{-species bidirectional connectors (2 each):}\ \ E_{\mathrm{int}}=8k{+}6=(6,14,22,30,38,46);$$
$$\boxed{\ \textbf{the disjoint reading hits the computed-cell floors}\ \{2,6,12,24,60\}\ [\mathrm{BM.17}(4)]\ \textbf{at}\ k=0,\ 1,\ 3\ \text{— the 1p3n member lands EXACTLY on the 24 floor}\ }\qquad[\mathrm{Def\text{-}BM.14}(6)\ \text{'s order-isomorphism locus}\ 12/24/60:\ \text{an ORDER,}\ \neg\text{a number, no species identification}]$$
$$(2)\quad\textbf{the derived per-member rows (exact symbolic multiples, no values):}\qquad\frac G{2\pi\ln2}=E^2\ [\mathrm{BM.88}(3)];\qquad\frac{k_{\mathrm{crit}}}{\ln2}=\frac{E^2}2\ [\mathrm{AT.35}(1)];\qquad r_s=\tfrac{\mathfrak h E}2,\qquad\Delta x_{\mathrm B}=\tfrac{\mathfrak h}{E\ln2}\ [\mathrm{Def\text{-}BM.4}(1);\ \mathrm{BM.17}(3)\ \text{pattern}];$$
$$\boxed{\ \Delta x_{\mathrm B}\cdot r_s=\tfrac{\mathfrak h^2}{2\ln2}\ \ \textbf{E-INDEPENDENTLY}\ [\mathrm{BM.17}(3)]\ }\qquad\text{the shell is non-empty at EVERY member}\ (E^2\ln2>2\ \text{on the frozen}\ \ln16>2\ \text{certificate}\ [\mathrm{BM.148}(4);\ \mathrm{AT.35}(2)]);\qquad\textbf{the family scales the lock, the shell and the horizon by exact integers, and moves nothing else}$$
$$(3)\quad\textbf{CHARGE:}\qquad Q_{\mathrm{total}}=+1\ \ \text{for EVERY member}\ (k{=}0..5):\ \ \text{the proton member's class}\ {+}1\ [\mathrm{AT.41}(2)],\ \text{the neutrons'}\ q_{\mathrm{net}}=0\ [\mathrm{BM.17}(2)],\ \text{connector interiors telescope}\ [\mathrm{EM.9b}];$$
$$\textbf{the sign census convolves binomially:}\ \ W_3(Q)=\binom6{Q+3}=(1,6,15,20,15,6,1),\ \ \textstyle\sum=64=4^3\ [\mathrm{Def\text{-}BM.8}(6);\ \mathrm{AT.41}(2)]\ \ \text{and the}\ (k{+}1)\text{-fold convolution is}\ \binom{6(k+1)}{Q+3(k+1)}\ \ \textbf{exactly (Vandermonde, entrywise to}\ k{=}4);$$
$$\text{the charge classes overlap the mesonic ones at}\ Q\in\{0,+1\};\ \ \text{only}\ |Q|{=}3\ \text{is baryon-exclusive per nucleon}\ [\mathrm{BM.31}(3)]\ \text{— the family's}\ Q{=}+1\ \text{is a CLASS label, its census binomial}$$
$$(4)\quad\textbf{PHASE:}\qquad\Theta_{\mathrm{int}}=2k(\Gamma)\in2\mathbb Z\ \ \text{per materialized closed chain}\ [\mathrm{FT.22};\ \mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(3):\ \Pi=72k(\Gamma)(\ln2)^2];\qquad\text{baryon-type}\ 4\mathbb Z\ \text{per pure-}\varepsilon\ \text{sector}\ [\mathrm{ML.6}(6)];$$
$$\text{the connector winding enters via}\ k(\Gamma)=k_1{+}k_2{+}d_{12}\ [\mathrm{FT.34}(3)]\ \text{and stays PARAMETRIC in}\ d:\ \ \neg\text{a frozen nucleon--nucleon connector winding exists anywhere in the record}\ (\mathrm{ML\text{-}O4});\ \ \neg\text{one is invented here}$$
$$(5)\quad\textbf{CAPACITY NEVER BITES:}\qquad\text{colour slots exist at}\ n{=}3\ \text{only}\ [\mathrm{CT3.11}(1);\ \mathrm{D3.1}];\qquad\text{every junction of every member sits at}\ n{=}3,\ \text{where}\ D_{\mathrm{tick}}(3)=2^4=16=C_{\mathrm{cap}}\ \ \textbf{EXACTLY SATURATED and admissible}\ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT0.11}];$$
$$n{=}4\ \text{would give}\ 2^5=32>16\ \text{— inadmissible}\ [\mathrm{AT.50}(3)]:\ \ \textbf{hence the multi-junction spreading of an}\ N\ge4\ \text{support}\ [\mathrm{ML.6}(5)],\ \text{and NO member at any}\ k\ \text{trips capacity, the rung ladder, or the}\ D^-\text{lock}\ (D^-\ \text{activates only at rung}\ \ge4\equiv\neg\text{admissible — the lock biconditional}\ [\mathrm{AT.50}(4),(5)])$$
$$(6)\quad\textbf{WHAT DOES CLOSE — from}\ k{=}1\ \textbf{uniformly:}\qquad(\mathrm P1)\ \text{the visibility bound}\ I_{\mathrm{hid}}=E_{\mathrm{tot}}-E_{\mathrm{vis}}\ [\mathrm{AT.29}(1)];\quad(\mathrm P2)\ \text{the mask}\ \mathcal K_\Sigma\ [\mathrm{AT.29}(2)];\quad(\mathrm P3)\ \textbf{the VOID closure: the internal constituent states of a sealed composite are}\ \neg\text{knowable BY THEOREM — no construction could exist inside the bound}\ [\mathrm{BM.143}(1);\ \mathrm{AT.29}(3),(4)];$$
$$\text{the accessible content is EXACTLY}\ (\text{boundary triple},\ |R|,\ \text{rung})\ [\mathrm{AT.32}(1)]\ \text{— for the family:}\ (Q{=}{+}1,\ \Theta\text{-class},\ S,\ N{=}3(k{+}1),\ E_{\mathrm{int}}\text{-reading, rung}\ 3);\qquad\textbf{the first closure is the DEUTERON}\ (k{=}1),\ \neg\ k{=}3$$
$$(7)\quad\textbf{the exact content of ``the screen and the mask close something'' at}\ k{=}3\ \textbf{(the directive's prediction, adjudicated):}\qquad\text{(i) what closes at}\ N{=}4\ \text{is the}\ \varepsilon\text{-PROTECTION (grammar}\ [\mathrm{ML.6}(5)]),\ \neg\text{capacity};$$
$$\text{(ii) at}\ k{=}3\ \text{exactly: the disjoint}\ E_{\mathrm{int}}=24\ \text{lands on the floor}\ (1),\ \text{and the}\ \delta\ \text{share first exceeds}\ \tfrac9{10}\ \bigl(\tfrac{387}{427}\bigr)\ [\mathrm{ML.6}(3)];\qquad\text{(iii) the information closure}\ (6)\ \text{is uniform from}\ k{=}1\ \text{— nothing additional closes at}\ k{=}3$$
$$(8)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(7);\qquad\textbf{parametric residue: the connector species}\ (d,\ \text{count, fusion)}\ \to\ \mathrm{ML\text{-}O4};\qquad\textbf{prices,}\ \neg\textbf{masses throughout}\ [\text{HistLog}\ \S\mathrm{V.32};\ \mathrm{Def\text{-}BM.3}(7)\ \text{nomenclature}];\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT0.5, CT0.6, CT0.11, CT0.13, CT3.11(1), D3.1, EM.9b, FT.19, FT.22 (Parts 1–2); Def-H.32, FT.34(3),(5), FT.35 (Part 3); ML.6 (this level); AT.29(1),(2),(3),(4), AT.32(1), AT.35(1),(2), AT.40(3), AT.41(2),(3), AT.50(3),(4),(5), AT.63(2) (Level 5); Def-BM.3(7), Def-BM.4(1), Def-BM.8(1),(6), Def-BM.9(4), Def-BM.14(6), BM.2(1),(2), BM.17(1),(2),(3),(4), BM.31(3),(4), BM.83, BM.88(3), BM.134(5), BM.135, BM.143(1), BM.148(4), Census FT.35(2),(3),(4),(5), FT.42(5), FT.49(3) (Part 4); exact binomials, polynomial convolution (Vandermonde), integer floor census [math; machine: `isotopic_family.py` §§D–F, 3/3].

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

### ML.8 — The lepton saturation flag, the premise corrections, and the status of Tier ML.2

**Thm.**
$$(1)\quad\textbf{LEPTON SATURATION (flagged for the next step, per the directive):}\qquad\text{the unsealed lepton}\ (Q{=}{-}1\ \text{register})\ \text{couples to ANY family member through the ONE global Def-H.32 configuration sum}\ [\mathrm{AT.42}(2)]\ \text{by an open connector whose boundary read is}\ Q_{\mathrm{total}}{=}{+}1\ \text{— INVARIANT across every grouping (telescoping}\ [\mathrm{EM.9b};\ \mathrm{ML.7}(3)]):$$
$$\boxed{\ \textbf{the}\ \delta\text{-mixing CANNOT alter the connector's boundary condition}\ }\qquad\text{the lepton price}\ w_c=\bigl(4\varepsilon_q(1{-}4\varepsilon_q)\bigr)^{-1/2}\ge2\ [\mathrm{AT.44}(4)]\ \text{and the positions}\ W_d=1/(d^2x_+x_-)\ [\mathrm{AT.44}(5)]\ \text{carry the flicker alphabet ALONE — GRAMMAR-BLIND (symbol census)};$$
$$\textbf{what the mixing changes is the nuclear-side ensemble:}\ \ \text{it decomposes into grouping sectors}\ (\mathrm{BM.31}(6)\ \text{'s disjoint-union pattern})\ \text{with multiplicities}\ g(N)=1,25,1540,164395,\dots,\ \text{the}\ (-1)^{\aleph}\ \text{dressing}\ [\mathrm{Def\text{-}H.32}(2)]\ \text{and the}\ \Theta\text{-class composition}\ [\mathrm{ML.6}(6)]:\ \ \textbf{INTENSITIES AND STATISTICS COMPOSITION, never positions}\ [\mathrm{AT.54}(3)];$$
$$\boxed{\ \textbf{isotopy, ledger-natively: SAME boundary charge, DIFFERENT grammar multiplicities}\ }\qquad\text{the isotope family reads on the connector side as pure multiplicity/measure structure; chemical identification QUARANTINED}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)]$$
$$(2)\quad\textbf{THE PREMISE CORRECTIONS (on the record, the house discipline):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``1p3n has}\ N{=}4\ \text{colour attachments''}&\textbf{CORRECTED:}\ N{=}3(k{+}1){=}12\ \text{for}\ k{=}3\ \text{— a nucleon is a 3-attachment}\ \varepsilon\text{-triple}\ [\mathrm{BM.17}(1);\ \text{Census}\ \mathrm{FT.35}(5)];\ \text{fusion/sharing}\ \neg\text{constructed}\ (\mathrm{ML\text{-}O4})\\ \text{``}\delta\ \text{enters at}\ N{=}4\ \text{in the family''}&\textbf{RELOCATED: the grammar transition IS at}\ N{=}4\ (g_\delta{:}\ 0\to3,\ \text{frozen}\ [\mathrm{BM.31}(2)]),\ \text{but the family}\ (N\equiv0\ (3))\ \text{first admits}\ \delta\ \textbf{at the deuteron}\ (N{=}6,\ \tfrac35\text{--}\tfrac25);\ \text{at 1p3n}\ \delta\ \textbf{dominates}\ (\tfrac{387}{427})\\ \text{``the screen and mask close something at}\ k{=}3\text{''}&\textbf{ADJUDICATED}\ [\mathrm{ML.7}(7)]\text{: what closes at}\ N{=}4\ \text{is the}\ \varepsilon\text{-protection (grammar),}\ \neg\text{capacity (never bites:}\ n{=}3\ \text{saturated-admissible at every}\ k);\ \text{the}\ (\mathrm P1)\text{--}(\mathrm P3)\ \text{closure is uniform from}\ k{=}1;\ \text{at}\ k{=}3\ \text{exactly: the}\ E_{\mathrm{int}}{=}24\ \text{floor landing and the}\ \delta\text{-share crossing}\ \tfrac9{10}\\ \text{the}\ g_\delta/g_\varepsilon\ \text{values cited in the directive}&\textbf{CONFIRMED:}\ (1,0,3,10,15,105)\ \text{and}\ (0,1,0,0,10,0)\ \text{for}\ N{=}2..7\ \text{— reproduced triple-certified}\ [\mathrm{ML.6}(1)]\end{array}$$
$$(3)\quad\textbf{THE ARCHITECT'S STANDING FLAG, recorded}\ \neg\textbf{pre-empted:}\qquad\text{``ML.4 will soon get an exception when we calculate multi-}(p,n,e)\ \text{systems in the molecular''}\ \ [\mathrm{ML.1}\ \text{session record}]:$$
$$\text{this tier supplies the nuclear-side half of that calculus}\ (\text{the}\ (p,n)\ \text{supports});\ \text{when the electron-saturated members are constructed}\ (\mathrm{ML\text{-}O2}),\ \mathrm{ML.4}(4)\ \text{'s single-currency rows and}\ \mathrm{ML.4}(6)\ \text{'s minimality are expected to acquire their exception row — recorded here as an expectation, to be derived}\ \neg\text{assumed, at its own locus}$$
$$(4)\quad\textbf{THE OPEN ROWS:}\qquad\begin{array}{l|l}\textbf{row}&\textbf{content}\\\hline\textbf{new}\ (\mathrm{ML\text{-}O4})&\textbf{the nucleon--nucleon connector species:}\ \text{count per pair, winding}\ d\ [\mathrm{BM.2}(2)/(\mathrm{R10})\ \text{pattern}],\ \text{and whether junctions FUSE (attachment sharing) — the tree}\ E_{\mathrm{int}}\ \text{reading and the composite}\ \Theta_{\mathrm{int}}\ \text{stay parametric until constructed};\ \mathrm{FT.34}(3)\ \text{'s}\ k(\Gamma){=}k_1{+}k_2{+}d_{12}\ \text{is the frozen skeleton}\\\hline(\mathrm{ML\text{-}O2})&\text{the}\ N\ge4\ \text{multi-seal configuration calculus — absorbs the family's ensemble weights}\ (\text{sector sums over the}\ g(N)\ \text{groupings});\ \mathrm{AT.44}/\mathrm{AT\text{-}O30}\ \text{engines reusable}\\\hline(\mathrm{ML\text{-}O3})&\text{the handshake-indicator operational theory}\ [\mathrm{ML.1}\ \text{unchanged}];\qquad(\mathrm{ML\text{-}O1})\ \text{the transit-leg amplitude}\ [\mathrm{ML.3}(6)\ \text{unchanged}]\end{array}$$
$$(5)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured isotope value}\ [\mathrm{P5}],\ \neg\text{a species identification}\ [\mathrm{Def\text{-}BM.3}(1),(7)];\qquad\text{§Cal-ML stays empty};$$
$$\textbf{bars untouched:}\ \mathrm{BM.83}/\mathrm{BM.134}(5)\ (\text{the grammar census is pure seal combinatorics; the}\ E_{\mathrm{int}}\ \text{rows are informational-currency PRICES; the lepton rows stay in}\ \{\varepsilon_q\}),\ \mathrm{FT.55}(1),\ \mathrm{CT3.22}\ (\text{colour}\ \neg\text{observable — the grammar counts sealings, never reads colour}),\ \mathrm{BM.143}(1)$$
$$(6)\quad\textbf{the machine state:}\qquad\texttt{isotopic\_family.py}\to\textbf{8/8 exact};\qquad\texttt{run\_all\_level6.py}\to\textbf{3 checkers, 33 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{2 Part 6 documents PASS};\qquad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(7)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier ML-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no isotope is identified}\ }\qquad[\mathrm{AT.39}(8)\ \text{'s standing row;}\ \mathrm{ML.1}(8)\ \text{'s box, re-cited}]$$

**Req.** ML.1, ML.3(6), ML.4(4),(5),(6), ML.6, ML.7 (this level); P1, P4, P5, CT0.5, CT0.6, CT3.22, EM.9b, FT.22, FT.34(3) (Parts 1–2); Def-H.32(1),(2), FT.19 (Part 3); AT.40(3), AT.41, AT.42(2), AT.44(2),(4),(5), AT.50, AT.54(3), AT.63(2), AT-O30 (Level 5); Def-BM.3(1),(7), BM.2(2), BM.17, BM.31(2),(6), BM.83, BM.129, BM.134(5), BM.135, BM.137(1), BM.143(1) (Part 4); exact symbol-set censuses [math; machine: `isotopic_family.py` §G, 1/1 + the level runner + the level gate].

**Pf.** Row-wise assembly of ML.6–ML.7 with the lepton-side symbol census [machine G1]; the
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

## §Cal-ML — free internal parameters of the Molecular era

**Empty at this tier** (unchanged from ML.1). The family's parametric residues are recorded as
open rows, not parameters: the connector winding $d$ and count (ML-O4) join the inherited slots
[$\mathfrak h$ (P1); $\varepsilon_q$ (AT-O27); $e_0$ (EM.25(7), ¬issued); $(\varkappa,\beta)$
(AT-O3); $\rho_{\mathrm B}$, $\hat\mu'^2$, $\sigma_\ell$, $\sigma_\nu$ (¬declared); the P4
transport profile; the lift and the vielbein (AT.60)].

## §Open-ML additions from Tier ML.2

| row | content | locus |
|---|---|---|
| (ML-O4) | the **nucleon–nucleon connector species**: count per nucleon pair, winding $d$, and junction fusion/sharing (attachment-count reduction). Until constructed: the family's tree $E_{\mathrm{int}}$ reading and composite $\Theta_{\mathrm{int}}$ stay parametric; the disjoint reading and all grammar rows are unaffected. The frozen skeleton is $\mathrm{FT.34}(3)$'s $k(\Gamma)=k_1+k_2+d_{12}$; the pattern is BM.2(2)/(R10)'s connector-winding row; R3's flavor-composition item is adjacent | ML.7(1),(4),(8); BM.17(1); FT.34(3) |

Inherited unchanged [ML.1(5)]: (ML-O1) the transit-leg amplitude, (ML-O2) the $N\ge4$
configuration calculus (which absorbs the family's sector-weighted ensemble sums), (ML-O3) the
handshake-indicator operational theory; and the Level-5 ledger [AT.63(3),(5)].
