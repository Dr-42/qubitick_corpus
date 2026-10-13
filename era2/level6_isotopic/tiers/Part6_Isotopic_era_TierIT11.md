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
