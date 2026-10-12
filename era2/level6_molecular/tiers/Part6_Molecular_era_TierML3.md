# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 6 · Molecular era** — Tier ML.3: the multi-seal configuration census at $N=5,6$

**Level.** 6. **Era.** 2 (the Molecular era). **Tier.** ML.3 — the channel-width skeleton, the
contraction-grammar census at $N=5,6$, the mask dimensions, and the $D^-$ saturation boundary:
the census side of ML-O2, closed at these boundaries.
**Tags.** ML.9–ML.11. **Pattern.** the construction tiers (ML.1/ML.2's shape), premise audit
logged in-tier.
**Status.** discovery-phase working tier. Nothing is adopted; no declaration issues; §Cal-ML
stays empty; no clause of Parts 1–4 or of Level 5's closed record is modified [AT.63(2)].
**Machine.** `era2/level6_molecular/checks/multi_seal_census.py` → **9/9 exact** (the ML.2
grammar engine reused verbatim, per the directive's "do not reinvent the census; extend it");
`run_all_level6.py` → **4 checkers, 42 exact markers, 0 failures**; `check_level6_format.py` →
the gate over all three Part 6 documents. Exact arithmetic: integer partition enumeration,
exact binomials, Laurent convolution over $\mathbb Z$, `Fraction` shares.
**No floating point in any assertion. No measured value enters any clause [P5]. No species
identification [Def-BM.3(1),(7)] — the objects are "multi-seal EM-bound composites"; the
"stellar collapse boundary" is a FRAMING, flagged as such at ML.11(1).**
**Charter (era chain).** Part 6 cites Parts 1–4, the Level-5 record, and earlier ML-tags only.
**Mandate.** The Architect's directive: *"Run the Multi-Seal Configuration Census for $N=5$ and
$N=6$ — the channel width skeleton and the $D^-$ saturation boundary … determine if the census
terminates or encompasses $D^-$ pure saturated areas … I think this does ML-O4 and ML-O2
simultaneously."* — executed with three premise corrections logged at ML.11(2); the closing
assessment adjudicated: **ML-O2 closes on its census side; ML-O4 stays open, sharpened.**

---

### ML.9 — The channel-width skeleton and the contraction-grammar census at $N=5,6$

**Thm.**
$$(1)\quad\textbf{THE CHANNEL WIDTH SKELETON:}\qquad W_N(Q)=[z^Q]\,(2+z+z^{-1})^N=\binom{2N}{Q+N}\qquad[\mathrm{BM.135};\ \mathrm{Def\text{-}BM.8}(6)\ \text{generalized};\ \text{machine: Laurent convolution}=\text{binomial, entrywise}]$$
$$\textbf{the frozen rows reproduce exactly:}\ \ W_2=(1,4,6,4,1)\ [\mathrm{BM.135}(3)];\qquad W_3=(1,6,15,20,15,6,1),\ \ \textstyle\sum=64=4^3\ [\mathrm{BM.135}(2);\ \mathrm{AT.41}(2)];$$
$$\boxed{\ W_5=(1,10,45,120,210,\mathbf{252},210,120,45,10,1),\ \ \textstyle\sum=4^5=1024,\ \ 11\ \text{charge classes}\ }\qquad\boxed{\ W_6=(1,12,66,220,495,792,\mathbf{924},792,495,220,66,12,1),\ \ \textstyle\sum=4^6=4096,\ \ 13\ \text{classes}\ }$$
$$(2)\quad\textbf{THE CROSS-}\ N\ \textbf{CENSUS}\ [\mathrm{BM.31}(3)\ \text{'s pattern extended}]:\qquad W_5(Q)\ne W_6(Q)\ \ \text{on the WHOLE overlap}\ |Q|\le5\ \ (\text{and}\ W_3\ \text{vs}\ W_5,\ W_3\ \text{vs}\ W_6\ \text{likewise})\ \text{— where charge classes coincide, the probability spaces still differ};$$
$$|Q|=6\ \ \text{is}\ W_6\text{-exclusive};\qquad\text{both widths peak at}\ Q=0\ (252,\ 924);\qquad\text{the read domain:}\ Q\ \text{is defined only on SEALED supports}\ (\mathcal C=1)\ [\mathrm{BM.135}(1);\ \mathrm{D2.14};\ \mathrm{FT.19}]\ \text{— and every grammar grouping is total, hence sealed}$$
$$(3)\quad\textbf{THE GRAMMAR CENSUS, triple-certified}\ [\mathrm{Def\text{-}BM.9}(3);\ \mathrm{BM.31}(1),(2);\ \mathrm{CT3.17a}(2);\ \mathrm{FT.41}(\mathrm b);\ \text{the ML.2 engine reused}]:\qquad\text{enumeration}\ \wedge\ \text{recurrence}\ g(N){=}(N{-}1)g(N{-}2){+}\binom{N-1}2g(N{-}3)\ \wedge\ \text{closed form}\ \sum_{2a+3b=N}\tfrac{N!}{a!\,2^a\,b!\,6^b}\ \ \text{agree entrywise};$$
$$\boxed{\ N{=}5:\ \ g(5)=10,\ \ \text{ALL of block type}\ (a,b)=(1,1)\ \text{— one}\ \delta\text{-pair + one}\ \varepsilon\text{-triple, uniquely}\ }\qquad\boxed{\ N{=}6:\ \ g(6)=25=\underbrace{15}_{(3,0)}+\underbrace{10}_{(0,2)},\quad\frac{15}{25}=\frac35\ \ \text{vs}\ \ \frac{10}{25}=\frac25\ \ [\mathrm{BM.31}(2)\ \text{re-derived EXACTLY}]\ }$$
$$(4)\quad\textbf{N=5 IS FORCED-MIXED (the ``highly strained'' row, as arithmetic):}\qquad2a+3b=5\ \ \text{has the UNIQUE nonnegative solution}\ (1,1)\implies g_\varepsilon(5)=0\ \ \textbf{is forced}:$$
$$\boxed{\ \textbf{EVERY 5-attachment grouping contains exactly one}\ \delta\ \textbf{and exactly one}\ \varepsilon\ \text{— no pure-baryon}\ (4\mathbb Z)\ \textbf{sector exists at}\ N{=}5\ }\qquad[\mathrm{BM.31}(4)\ \text{statistics classes};\ \mathrm{ML.8}\ \text{composition rows}]$$
$$N{=}4\ \text{is all-}\delta\ (3\ \text{perfect matchings}\ [\mathrm{ML.6}(5)]),\ \ N{=}5\ \text{cannot avoid the triple},\ \ N{=}6\ \text{restores the pure-}\varepsilon\ \text{option}\ (\tfrac25)$$
$$(5)\quad\textbf{THE PROTECTION PERIODICITY:}\qquad\boxed{\ g_\varepsilon(N)>0\iff3\mid N\ }\qquad\text{verified for EVERY}\ N{=}2..18\ (\text{closed form against recurrence throughout});$$
$$\delta\ \text{shares:}\ \ N{=}4{:}\ 1,\quad N{=}5{:}\ 1,\quad N{=}6{:}\ \tfrac35,\quad N{=}9{:}\ \tfrac9{11},\quad N{=}12{:}\ \tfrac{387}{427}\ \ [\mathrm{ML.7}\ \text{re-derived}]\ \text{— the protection is PERIODIC (returns at every multiple of 3), the erosion within it MONOTONE}\ [\mathrm{ML.7}(3)]$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{re-produced frozen rows:}\ W_2,\ W_3,\ g_\delta/g_\varepsilon\ \text{sextuples};\qquad\neg\text{a declaration},\ \neg\text{a species identification},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT3.17a(2), D2.14, FT.19, FT.41(b) (Parts 1–2); ML.6(5), ML.7(3), ML.8 (this level); AT.41(2), AT.63(2) (Level 5); Def-BM.3(1),(7), Def-BM.8(6), Def-BM.9(3),(4),(5), BM.31(1),(2),(3),(4), BM.135(1),(2),(3) (Part 4); exact Laurent convolution over $\mathbb Z$, binomial identities, integer partition enumeration, the partition recurrence [math; machine: `multi_seal_census.py` §§A–B, 5/5].

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

### ML.10 — The mask dimensions and the $D^-$ saturation boundary: two mask species, the attained bound, and the structural censorship

**Thm.**
$$(1)\quad\textbf{THE TWO MASK SPECIES, KEPT APART}\ [\mathrm{ML.1}(6)\ \text{'s discipline}]:\qquad\textbf{RUNG masks}\ \mathcal K_n=\bigoplus_{A\in\mathcal A(n)}\mathcal K^{(A)}\ [\mathrm{D2.3}]:\ \ \dim\mathcal K_n=6,16,17,25\ \ (n{=}0..3),\ \ 26\ \ \textbf{ONLY at the formal}\ n\ge4;$$
$$\textbf{SUBNETWORK masks}\ \mathcal K_\Sigma(C)=\bigoplus_{A\in\mathcal A(\Sigma;C)}\mathcal K^{(A)}\ [\mathrm{Def\text{-}H.15}(3);\ \mathrm{AT.29}(\mathrm P2)]:\ \ \mathcal A(\Sigma;C)\subseteq\{\mathrm{EM},\mathrm G,\mathrm H,\mathrm W,\mathrm{strong}\}\ \text{—}\ \ \textbf{J}^\pm\ \textbf{and}\ \textbf{D}^\pm\ \textbf{NEVER}\ [\mathrm{FT.20}\ \text{table+Rmk};\ \mathrm{FT.26}(3)\ \text{'s own Pf}];$$
$$\boxed{\ \dim\mathcal K_\Sigma=9\ (\mathrm{G}{+}\mathrm{W}{+}\mathrm{H}\ \text{core})\ +\ 1\cdot[\mathrm{EM}\ \text{active}]\ +\ 8\cdot[\mathrm{strong}:\ \mathrm{Colour}\ne\varnothing\ \wedge\ \mathcal C{=}1]\ \ \le\ \ 18\ }\qquad[\mathrm{FT.26}(3);\ \mathrm{FT.28}(4)]$$
$$(2)\quad\textbf{THE BOUND IS ATTAINED — at exactly these composites:}\qquad\text{the grammar groupings are total}\implies\ \text{sealed}\ (\mathcal C{=}1\ [\mathrm{D2.14}]);\ \ \text{EM-active registration}\iff\exists v\ f_v\ne0\ [\mathrm{FT.20}];$$
$$\boxed{\ \textbf{the sealed EM-active}\ N{=}5,6\ \textbf{members attain}\ \dim\mathcal K_\Sigma=9{+}1{+}8=18\ \text{— the general bound, reached ``only in the inside-sealed variant''}\ [\mathrm{FT.28}(4)\ \mathrm{Rmk}]\ }\qquad\text{activity census exact:}\ 9/10/17/18$$
$$(3)\quad\textbf{THE LOCK BICONDITIONAL, re-run exhaustively}\ [\mathrm{AT.50}(3),(4)]:\qquad D^-\in\mathcal A(n)\iff n\ge4\iff2^{n+1}>16=C_{\mathrm{cap}}\iff\neg\text{admissible}\qquad(n{=}0..16);$$
$$\textbf{the refinement of the directive's bound row:}\ \ C_{\mathrm{cap}}{=}16\ \text{bounds the PAIR channel}\ [\mathrm{CT0.12}\ \mathrm{Rmk}];\ \ \text{the per-vertex tick demand}\ D_{\mathrm{tick}}(n){=}2^{n+1}\ \textbf{saturates exactly at}\ n{=}3\ (16{=}C_{\mathrm{cap}},\ \text{admissible});\ \ \text{the subnetwork mask bound is}\ 18,\ \neg16\ (1)\ \text{— three spaces, three bounds}$$
$$(4)\quad\textbf{THE VERTEX PLACEMENT (the screen's exact locus):}\qquad\text{every grouping's}\ (a,b)\ \text{blocks place the attachments on 2-supports}\ (\delta{:}\ n{=}2,\ D_{\mathrm{tick}}{=}8)\ \text{and 3-supports}\ (\varepsilon{:}\ n{=}3,\ D_{\mathrm{tick}}{=}16\ \textbf{exactly saturated});$$
$$n{=}4\ \text{would demand}\ 32>16\ \text{— inadmissible}\ [\mathrm{CT0.5};\ \mathrm{CT0.6};\ \mathrm{CT3.11}(1):\ \text{colour slots at}\ n{=}3]:\qquad\textbf{NO vertex carries}\ \ge4\ \text{attachments};\qquad N{=}5\ \text{runs on}\ \ge2\ \text{supports in EVERY grouping (uniquely}\ 1{+}1),\ \ N{=}6\ \text{on}\ \ge2\ (3{+}0\ \text{or}\ 0{+}2);$$
$$\text{the connectors BETWEEN supports have no frozen species}\ [\mathrm{ML.7}(1),(4);\ \mathrm{ML\text{-}O4}]\ \text{— the census names the decomposition,}\ \neg\text{the glue}$$
$$(5)\quad\textbf{THE}\ D^-\ \textbf{STATUS AT THESE BOUNDARIES — NONZERO-BUT-UNREACHABLE, re-verified:}\qquad\begin{array}{l|l}\textbf{the row}&\textbf{the locus}\\\hline\text{the junction vertices are}\ D^-\text{-CONFIGURED — placement,}\ \neg\text{activation}&[\text{Census}\ \mathrm{FT.35}(4);\ \mathrm{CT4.1};\ \mathrm{BM.17}(1)]\\\text{no subnetwork mask contains a}\ D^-\ \text{summand, at any}\ N&(1)\ [\mathrm{FT.26}(3)\ \mathrm{Pf}]\\\mathcal P_M^{(n)}F_{D^-}\mathcal P_M^{(n)}=0\ \ \forall n\le3;\ \ \neg\exists\ \text{a pole of}\ Z(\mathcal R,n);\ \text{one-way transfer}&[\mathrm{CT4.2}]\\\text{at the formal unlocking: nonzero as a formal object,}\ \iota_4\ \text{unrealized, vertices}\ \{V_0..V_3\}&[\mathrm{AT.50}(5);\ \mathrm{CT4.4a}(1);\ \mathrm{CT0.11}]\\\text{structureless even if reached: no gauge algebra, no generator; dust}\ w{=}0;\ \text{entropy locked}&[\mathrm{CT4.4};\ \mathrm{CT4.5};\ \mathrm{CT4.7}]\\\text{the void closure caps it: no construction could exist inside the bound}&[\mathrm{BM.143}(1);\ \mathrm{AT.29}(3),(4);\ \mathrm{ML.2}(6)]\end{array}$$
$$\boxed{\ \textbf{THE CENSUS TERMINATES IN A STRUCTURAL CENSORSHIP, NOT A SMOOTH SINGULARITY: the interior is preserved (every edge registered}\ [\mathrm{D0.7}]\textbf{) and provably cannot reach the boundary}\ }$$
$$(6)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(5);\qquad\textbf{re-run frozen censuses:}\ \mathrm{AT.50}(3),(4)\ \text{'s biconditional},\ \mathrm{FT.28}(4)\ \text{'s bound};\qquad\neg\text{a declaration},\ \neg\text{a measured value}\ [\mathrm{P5}]$$

**Req.** P5, CT0.5, CT0.6, CT0.11, CT0.12, CT0.13, CT0.14, CT3.11(1), CT4.1, CT4.2, CT4.4, CT4.4a(1), CT4.5, CT4.7, D0.7, D2.3, D4.1, FT.19, FT.20, FT.26(3), FT.28(4) (Parts 1–2); Def-H.15(3), Def-H.32(1), FT.22 (Part 3); ML.2(6), ML.6(5), ML.7(1),(4), ML.9 (this level); AT.16(4),(5), AT.29(2),(3),(4), AT.32(1), AT.50(1),(3),(4),(5), AT.63(2) (Level 5); Def-BM.3(7), D2.14, BM.17(1), BM.143(1), Census FT.35(4) (Part 4); exact block-dimension arithmetic, exhaustive biconditional census [math; machine: `multi_seal_census.py` §C, 3/3].

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

### ML.11 — The synthesis, the premise corrections, and the adjudication of the open rows

**Thm.**
$$(1)\quad\textbf{THE SYNTHESIS (the directive's step 4, as exact ledger rows):}\qquad\begin{array}{l|l|l}\textbf{quantity}&\textbf{behaviour with}\ N&\textbf{the locus}\\\hline\text{the grammar}\ g(N)&\textbf{GROWS strictly}\ (1,3,10,25,105,385,1540,7245,32725,164395\ \text{for}\ N{=}3..12)&[\mathrm{ML.9}(3);\ \mathrm{ML.2}]\\\text{the channel width}&\textbf{GROWS:}\ 4^N\ \text{states},\ 2N{+}1\ \text{classes}\ (1024/11,\ 4096/13)&[\mathrm{ML.9}(1)]\\\text{the}\ \delta\ \text{share}&\textbf{GROWS within the family:}\ 0,\ 1,\ \tfrac35,\ \tfrac9{11},\ \tfrac{387}{427}\ (N{=}3,5,6,9,12)&[\mathrm{ML.9}(5);\ \mathrm{ML.7}(3)]\\\text{the}\ D^-\ \text{sink}&\textbf{CONSTANT:}\ \dim\mathcal K^{(D^-)}=1\ \text{at every rung — full at birth, structureless}&[\mathrm{CT4.4};\ \mathrm{D4.1};\ \mathrm{AT.50}(1)]\\\text{the per-vertex cap}&\textbf{HARD:}\ D_{\mathrm{tick}}(3){=}16{=}C_{\mathrm{cap}}\ \text{saturated};\ D_{\mathrm{tick}}(4){=}32\ \text{inadmissible}&[\mathrm{CT0.5};\ \mathrm{CT0.6}]\end{array}$$
$$\boxed{\ \textbf{``}\ D^-\ \textbf{pure saturated areas'' do not exist as growing regions: the sink is ONE-dimensional at every}\ N\ \text{— there is nothing for the census to encompass; what grows is the grammar and the width, and what bounds is combinatorial}\ }$$
$$(2)\quad\textbf{THE PREMISE CORRECTIONS (on the record):}\qquad\begin{array}{l|l}\textbf{the directive's premise}&\textbf{the derived row}\\\hline\text{``the}\ D^-\ \text{sink is formally active in these composites, adding 1 dimension to reach 26''}&\textbf{CORRECTED}\ [\mathrm{ML.10}(1),(3)]:\ \text{two mask species — the 26-dim mask is the RUNG mask at the inadmissible rung}\ \ge4;\ \text{subnetwork masks never contain}\ D^-\ [\mathrm{FT.26}(3)\ \mathrm{Pf}]\ \text{and are bounded by 18 — attained here}\\\text{``accessible vertex sets strictly bounded by}\ C_{\mathrm{cap}}{=}16\text{''}&\textbf{REFINED}\ [\mathrm{ML.10}(3)]:\ C_{\mathrm{cap}}{=}16\ \text{bounds the PAIR channel}\ [\mathrm{CT0.12}\ \mathrm{Rmk}];\ \text{the per-vertex tick demand saturates at}\ n{=}3;\ \text{the subnetwork mask bound is}\ 18\\\text{``this does ML-O4 and ML-O2 simultaneously''}&\textbf{ADJUDICATED}\ (3),(4):\ \mathrm{ML\text{-}O2}\ \text{closes on its census side;}\ \mathrm{ML\text{-}O4}\ \text{is untouched by a grammar census — sharpened, open}\end{array}$$
$$(3)\quad\textbf{ML-O2 CLOSED ON ITS CENSUS SIDE at the}\ N{=}5,6\ \textbf{boundaries:}\qquad\text{the width skeleton}\ \mathrm{ML.9}(1),(2),\ \text{the grammar}\ \mathrm{ML.9}(3)\text{--}(5),\ \text{the masks}\ \mathrm{ML.10}(1)\text{--}(3),\ \text{the placement}\ \mathrm{ML.10}(4),\ \text{the}\ D^-\ \text{status}\ \mathrm{ML.10}(5)\ \text{— all derived};$$
$$\textbf{RESIDUE (ML-O2 stays open for it): the AMPLITUDE side — the Def-H.32 ensemble sums over the grouping sectors}\ (10\ \text{sectors at}\ N{=}5,\ 25\ \text{at}\ N{=}6,\ \text{each a configuration class with its own}\ (-1)^{\aleph}\ \text{dressing}\ [\mathrm{Def\text{-}H.32}(2)];\ \mathrm{AT.44}/\mathrm{AT\text{-}O30}\ \text{engines reusable});$$
$$(4)\quad\textbf{ML-O4 STAYS OPEN, SHARPENED:}\qquad\text{the}\ (a,b)\ \text{census NAMES the support decompositions}\ (N{=}5{:}\ \text{one 2-support + one 3-support, uniquely};\ N{=}6{:}\ \text{three 2-supports or two 3-supports}),$$
$$\text{and thereby sharpens the question: the connector species must join SUPPORTS of these exact shapes — count per pair, winding}\ d\ [\mathrm{FT.34}(3)\ \text{'s}\ k(\Gamma){=}k_1{+}k_2{+}d_{12}\ \text{skeleton}],\ \text{fusion/sharing}\ [\mathrm{ML.7}(1),(4);\ \mathrm{BM.2}(2)/(\mathrm{R10})\ \text{pattern}];\qquad\text{the census cannot and does not invent one}$$
$$(5)\quad\textbf{THE FRAMING ROW (the directive's step 4, honestly bounded):}\qquad\text{``the stellar collapse boundary'' is a FRAMING — no astrophysical species is identified}\ [\mathrm{P5};\ \mathrm{Def\text{-}BM.3}(7)],\ \text{no density or pressure primitive appears anywhere in the census};$$
$$\textbf{its exact ledger content:}\ \ \text{a composite family at maximal grammar growth, maximal channel width, forced or dominant}\ \delta\text{-mixing, against a CONSTANT one-dimensional censored sink behind a hard per-vertex combinatorial cap —}\ \textbf{a COMBINATORIAL CAPACITY LIMIT of the topology-blind sum}\ [\mathrm{Def\text{-}H.32}(1);\ \mathrm{ML.10}(3),(4)],\ \neg\text{a density limit}$$
$$(6)\quad\textbf{the Architect's standing flag, unchanged:}\ \ \mathrm{ML.4}\ \text{'s exception awaits the multi-}(p,n,e)\ \text{calculus}\ [\mathrm{ML.8}(3)]:\ \text{this tier is the}\ (p,n)\text{-side census; the electron-saturated members remain}\ \mathrm{ML\text{-}O2}\ \text{'s amplitude side}\ — \text{recorded,}\ \neg\text{pre-empted}$$
$$(7)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification};\qquad\text{§Cal-ML stays empty};\qquad\text{bars untouched:}\ \mathrm{BM.83},\ \mathrm{BM.134}(5),\ \mathrm{FT.55}(1),\ \mathrm{CT3.22}\ (\text{colour}\ \neg\text{observable — the grammar counts sealings, never reads colour})$$
$$(8)\quad\textbf{the machine state:}\qquad\texttt{multi\_seal\_census.py}\to\textbf{9/9};\qquad\texttt{run\_all\_level6.py}\to\textbf{4 checkers, 42 exact markers, 0 failures};\qquad\texttt{check\_level6\_format.py}\to\textbf{3 Part 6 documents PASS};\qquad\text{the Level-5 closed suite untouched}\ (37/643)$$
$$(9)\quad\textbf{the era chain:}\qquad\text{every clause cites Parts 1--4, the Level-5 record, and earlier ML-tags only;}\ \neg\exists\ \text{a forward pointer used as a premise; acyclic}\ [\text{machine: the gate's F3}];$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and no composite here is named}\ }\qquad[\mathrm{AT.39}(8);\ \mathrm{ML.1}(8)\ \text{'s standing box, re-cited}]$$

**Req.** ML.2(6), ML.4, ML.6(5), ML.7(1),(3),(4), ML.8(3), ML.9, ML.10 (this level); P1, P5, CT0.5, CT0.6, CT0.11, CT0.12, CT3.22, FT.34(3) (Parts 1–2); Def-H.32(1),(2), FT.22 (Part 3); AT.39(8), AT.44, AT.50(1), AT.63(2), AT-O30 (Level 5); Def-BM.3(7), BM.2(2), BM.83, BM.134(5), BM.143(1), CT4.4, D4.1 (Part 4); row-wise assembly + exact growth censuses [math; machine: `multi_seal_census.py` §D, 1/1 + the level runner + the level gate].

**Pf.** Row-wise assembly of ML.9–ML.10 with the growth/constancy censuses [machine D1]; the
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
