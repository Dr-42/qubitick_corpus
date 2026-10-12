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
