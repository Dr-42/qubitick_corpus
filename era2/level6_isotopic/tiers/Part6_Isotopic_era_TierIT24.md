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
