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
