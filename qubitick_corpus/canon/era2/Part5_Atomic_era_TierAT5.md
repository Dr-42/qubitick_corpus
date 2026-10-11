# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.5

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.5 — the boundary-invariance survey:
the coarse-graining principle, the per-aspect and per-rung census, and complete invariance tested.
**Tags.** AT.29–AT.34. **Status.** discovery-phase working tier. **No declaration issues;
§Cal-AT stays empty; no clause of Parts 1–4 is modified or retracted.**
**Machine.** `canon/era2/boundary_census.py` → **18/18 exact**; `canon/era2/ato22.py` → **16/16 exact** (AT.33); `canon/era2/ato1.py` → **14/14 exact** (AT.34). Exit 0. Arithmetic: integers,
`Fraction`, **exhaustive enumeration of all $2^n$ sign assignments**. No floating point.
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.

**Mandate.** Survey the "the boundary looks identical" phenomenon beyond AT.28's single case:
test the neutral baryon, state the coarse-graining principle, and test **complete invariance
over a generalised subnetwork across all forces and all rungs**.

---

## Tier AT.5 — the boundary-invariance survey

### AT.29 — The coarse-graining principle, in three exact levels

**Thm.** The principle the survey is asked for is already a theorem, at three levels:
$$(1)\quad\textbf{(P1) the visibility bound:}\qquad E_{\mathrm{tot}}(C)=|\Sigma|\ln2,\qquad E_{\mathrm{vis}}(\gamma)=\min\bigl(\delta h(\gamma),\ 4\,\delta\tau(\gamma)\bigr)\ln2\qquad[\mathrm{FT.1};\ \mathrm{CT0.9};\ \mathrm{CT1.29}];$$
$$\boxed{\ I_{\mathrm{hid}}:=E_{\mathrm{tot}}-E_{\mathrm{vis}},\qquad m_{\mathrm{hid}}:=I_{\mathrm{hid}}/\mathfrak h\ }\qquad[\mathrm{Def\text{-}H.9}(2)]$$
$$(2)\quad\textbf{(P2) the mask:}\qquad \mathcal K_\Sigma(C):=\bigoplus_{A\in\mathcal A(\Sigma;C)}\mathcal K^{(A)},\qquad \mathbf F_M^{(\Sigma)}(C):=\mathcal P_M^{(\Sigma)}\,\mathbf F\,\mathcal P_M^{(\Sigma)}\qquad[\mathrm{Def\text{-}H.15}(1)\text{--}(3)];$$
$$\text{with the strong summand admissibility-filtered:}\quad F_{\mathrm{strong}}\longmapsto\Pi_{\mathcal C}(\Sigma;C)\,F_{\mathrm{strong}}\big|_\Sigma\,\Pi_{\mathcal C}(\Sigma;C)\qquad[\mathrm{Def\text{-}H.10};\ \mathrm{FT.19}];$$
$$(3)\quad\textbf{(P3) the information-flux bound — and it is a VOID closure, not a limitation:}$$
$$\text{``sealing restricts every read to traces, ends and junctions: one dangling attachment zeroes the colour sector''}\qquad[\mathrm{FT.19};\ \mathrm{BM.143}(1)(\mathrm{iii})];$$
$$\boxed{\ \textbf{``the internal constituent states of a sealed composite are }\neg\textbf{knowable BY THEOREM, and (R5) is closed as VOID: coarse graining bounds the information flux, and NO CONSTRUCTION COULD EXIST INSIDE THE BOUND''}\ }\qquad[\mathrm{BM.143}(1)];$$
$$(4)\quad\textbf{the consequence for any future tier:}\qquad(\mathrm{P3})\ \textbf{is a }\neg\exists\textbf{-statement about constructions, not about present knowledge. No later tier can recover the interior of a sealed composite.}$$
$$(5)\quad\textbf{status: derived, re-cited.}$$

**Req.** A1, A2, A7, CT0.9, CT1.29, D1.11 (Part 1); CT1.22, CT2.3, CT3.22, FT.1, FT.19 (Part 2); Def-H.9(2), Def-H.10, Def-H.13, Def-H.15(1),(2),(3), Def-H.16, FT.20 (Part 3); BM.143(1), CT4.2 (Part 4) [math; machine: `boundary_census.py` §E].

**Pf.** Re-citation; the three levels are at their own loci and compose: (P1) bounds what a
subnetwork's own content read can see, (P2) bounds which aspects act on it, (P3) bounds what any
construction could recover. $\blacksquare$

**Phys.** The corpus does not merely fail to resolve interiors — it proves that no construction
could. That is the difference between a gap and a bound, and it is why the survey's negative
results below are *theorems* rather than absences. (P1) is an information count, (P2) is a
projection, (P3) is the statement that their composition leaves nothing to build.

---

### AT.30 — The per-aspect, per-rung boundary census, and the exact failure of completeness

**Thm.**
$$(1)\quad\textbf{the census (FT.20's criteria}\times\text{FT.21's boundary-exactness}\times\text{the (S,T) sectors}\times\text{CT0.13's rungs):}$$
$$\begin{array}{l|l|l|l|l|l}
\text{aspect} & \in\mathcal A(\Sigma;C)\iff & \text{boundary-exact?} & (S,T) & \text{metric} & \text{rung}\\ \hline
\mathrm{EM} & \exists v\in\Sigma:\ f_v\ne0 & \textbf{YES, telescopes} & \text{stack} & 0 & \mathcal A(2)\\
G\ (\text{mass}) & I_{\mathrm{hid}}(\Sigma;o)\ne0 & \textbf{OBSERVER-RELATIVE} & \mathcal E_{++} & 5\ \text{shear} & \mathcal A(1)\\
H & \text{folded into }G & \text{as }G & \mathcal E_{++} & 1\ \text{volume} & \mathcal A(1)\\
D^+ & \text{never (independently)} & \text{uniform} & \mathcal E_{++} & 1\ \text{conformal} & \mathcal A(1)\\
W\ (\text{spin}) & \Theta_{\mathrm{int}}\ne0\implies\Sigma\setminus\partial\Sigma\ne\varnothing & \textbf{ONE-DIRECTIONAL} & \mathcal E_{+-} & 3\ \text{shift} & \mathcal A(1)\\
J^\pm & \text{never} & — & \mathcal E_{-+},\mathcal E_{--} & 0 & \mathcal A(0)\\
D^- & \text{never (independently)} & — & \text{stack} & 0 & \mathcal A(n\ge4)\\
\text{strong} & \mathcal C(\Sigma;C)=1 & \textbf{ALL-OR-NOTHING} & \text{stack} & 0 & \mathcal A(3)\end{array}$$
$$(2)\quad\textbf{EM.9b's telescoping, verified exhaustively:}\qquad f_v=\tfrac12\bigl(\sigma_{\rightarrow}(v)-\sigma_{\leftarrow}(v)\bigr)\in\{-1,0,+1\}\qquad[\mathrm{EM.12}];$$
$$\text{on a directed chain }v_0\to\cdots\to v_n\ \text{with edge signs }\sigma_i:\qquad f_{v_i}=\tfrac12(\sigma_{i+1}-\sigma_i);$$
$$\boxed{\ \sum_{i}\,f_{v_i}\ =\ \tfrac12\bigl(\sigma_{\text{last}}-\sigma_{\text{first}}\bigr)\ =\ q\ }\qquad[\text{machine: ALL }1016\ \text{sign assignments on chains of }3..9\ \text{edges}];$$
$$(3)\quad\textbf{COMPLETENESS FAILS, exactly and constructively:}\qquad\text{FT.20's EM criterion }\bigl(\exists v:\ f_v\ne0\bigr)\ \textbf{is interior-sensitive while the observable }q\ \textbf{is boundary-exact};$$
$$\text{counterexample class: an interior sign flip }(+,-,+)\ \text{leaves }q=0\ \text{at the termini but makes }f_v\ne0\ \text{inside};$$
$$\boxed{\ 14\ \text{of the }32\ \text{five-edge sign assignments have }q=0\ \textbf{and}\ \text{nonzero interior activity}\ }\qquad[\text{machine: exhaustive}];$$
$$\text{e.g.}\ (++-++),\ (+++-+),\ (++--+)\ \text{— all with }q=0,\ \text{all EM-active};$$
$$(4)\quad\textbf{the distinction that resolves it:}\qquad\textbf{the OBSERVABLE is boundary-exact; the ASPECT MEMBERSHIP is not.}\ \ \text{FT.21(i)'s own caveat is the row: the criterion ``can exceed'' the boundary read};$$
$$\therefore\ \textbf{two subnetworks with identical boundary data can differ in aspect membership};$$
$$(5)\quad\textbf{the invariant and the non-invariant, across the whole census:}\qquad\begin{array}{l|l}
\textbf{INVARIANT on the boundary-data class} & \textbf{NOT invariant}\\ \hline
q=\tfrac12(\sigma_s-\sigma_t)\ \ [\mathrm{FT.21}(i);\ (2)] & \mathcal A(\Sigma;C)\ \text{— interior-sensitive}\ \ [(3)]\\
\mathcal C(\Sigma;C)\in\{0,1\},\ \mathcal C^2=\mathcal C\ \ [\mathrm{FT.19};\ \mathrm{CT3.22}] & I_{\mathrm{hid}}(\Sigma;o)\ \text{— observer-relative}\ [\mathrm{FT.20}\ G\text{-row}]\\
\Theta_{\mathrm{int}}\in2\mathbb Z,\ \mathrm{Hol}_{\mathrm{int}}=(-1)^{\Theta_{\mathrm{int}}}\ [\mathrm{Def\text{-}H.9}(3)] & \text{the interior vertex activity itself}\ [\mathrm{EM.9b};\ (3)]\\
k,\ \Theta(c)=2k\ \ [\mathrm{FT.22};\ \mathrm{FT.24}] & w_i^{\perp}\ \text{— }2E\ \text{transverse dims are gauge}\ [\mathrm{AT.5}]\\
S_{\mathfrak L}=|R|\ln2\ \ [\mathrm{CT1.29};\ \mathrm{CT4.3}] & \text{the per-vertex valence distribution of }O(n_v)\ [\mathrm{BM.149}(2)]\\
\varepsilon=(-1)^{|k|}=i^{\Theta}\ \ [\mathrm{Def\text{-}BM.16}(5);\ \mathrm{BM.113}(2)] & \\
\mathbf F_M^{(\Sigma)}\ \ [\mathrm{Def\text{-}H.15}(3)] & \end{array}$$
$$(6)\quad\textbf{the bounded-failure theorem:}\qquad\textbf{every non-invariant row is either observer-relative, gauge, or masked.}\ \ \neg\exists\ \textbf{an accessible read that differs between representatives};$$
$$(7)\quad\textbf{the rung census is finite:}\qquad \mathcal A(0)=\{J\},\ \mathcal A(1)=\{J,G,W,H,D^+\},\ \mathcal A(2)=\cup\{\mathrm{EM}\},\ \mathcal A(3)=\cup\{\mathrm{strong}\},\ \mathcal A(n\ge4)=\cup\{D^-\};$$
$$\dim\mathcal K_n=6,\ 16,\ 17,\ 25\ \ (\text{strictly nested});\qquad D^-\ \text{is masked at EVERY accessible rung}\ [\mathrm{CT4.2}];$$
$$(8)\quad\textbf{status: derived.}\qquad\textbf{Complete invariance is FALSE as stated and TRUE on the accessible sector, and both halves are exact.}$$

**Req.** A2, A8, CT0.7, CT0.9, CT0.12, CT0.13, CT0.14, CT1.29, CT3.22, CT4.2, D3.3, EM.9, EM.9b, EM.12, FT.1, FT.19 (Parts 1–2); AT.2(3),(4), AT.5(1),(3),(4), AT.16(4),(5), AT.28 (this tier); Def-H.9(1),(2),(3), Def-H.10, Def-H.13, Def-H.15, Def-H.16, Def-H.32(4), FT.13, FT.20, FT.21(i), FT.22, FT.24, FT.25, FT.30 (Part 3); Def-BM.3(2),(3), Def-BM.5(1), Def-BM.16(5), BM.2(1), BM.113(2), BM.143(1), BM.149(2) (Part 4); exhaustive enumeration of $2^n$ sign assignments, exact `Fraction` sums [math; machine: `boundary_census.py` §§A–B, D–E].

**Pf.**
$$(2):\ f_{v_i}=\tfrac12(\sigma_{i+1}-\sigma_i)\ \text{is a difference, so the sum telescopes:}\ \sum_{i=1}^{n-1}\tfrac12(\sigma_{i+1}-\sigma_i)=\tfrac12(\sigma_n-\sigma_1)\ [\text{machine: all }1016\ \text{assignments on chains of }3..9\ \text{edges, exact }`Fraction`\ \text{equality}];$$
$$(3):\ \sigma=(+,+,-,+,+)\ \text{gives}\ q=\tfrac12(1-1)=0\ \text{while}\ f_{v_3}=\tfrac12(\sigma_4-\sigma_3)=\tfrac12(1-(-1))=1\ne0;\ \text{exhaustive count over }2^5=32\ \text{gives }14;$$
$$(6):\ \text{row-wise from (5) and AT.28(1)'s three invisibility rows}. \blacksquare$$

**Phys.** The survey asked whether the boundary determines everything. It determines every
*accessible* read, exactly, and it does not determine the interior — and the second half is not a
defect. The cleanest case is electromagnetism: the interior vertex activity telescopes into the
end signs, so the charge is boundary-exact; but whether the EM aspect is *active at all* depends
on whether any interior vertex flips, which the ends cannot see. Fourteen of the thirty-two
five-edge chains have zero boundary charge and nonzero interior activity. So aspect membership is
interior-sensitive while every observable is not.

That is the precise sense in which "the boundary looks identical": identical for every read the
corpus can form, and free for every row that (P1)–(P3) already declare unknowable. The failure of
complete invariance is bounded by the coarse-graining principle itself.

---

### AT.31 — The neutral baryon: an observable seal with $D^-$ inside, and the envelope/horizon ordering

**Thm.**
$$(1)\quad\textbf{the cell, all exact:}\qquad \Sigma_{12}=\{p_1,q_1\}\cup\{p_2,q_2\},\ \text{materialized 2-cycles joined by a bidirectional connector, SINGLE OBSERVER CONTACT}\qquad[\mathrm{BM.17}(1);\ \text{Census FT.35}];$$
$$E_{\mathrm{int}}=6\ (c_1{:}2,\ c_2{:}2,\ \text{connector}{:}2),\quad I_{\mathrm{hid}}=6\ln2,\quad m_{\mathrm{hid}}=\tfrac{6\ln2}{\mathfrak h},\quad \Theta_{\mathrm{int}}=2k(\Gamma)\in2\mathbb Z,\quad \Pi=72\,k(\Gamma)(\ln2)^2;$$
$$\mathcal C(\Sigma_{12};C)=1\iff\text{all three attachments seal inside as ONE }\varepsilon\text{-type (baryon-like) triple}\qquad[\mathrm{D3.9};\ \mathrm{CT3.17};\ \mathrm{FT.34}(5)];$$
$$(2)\quad\textbf{the identification row:}\qquad\mathrm{Def\text{-}BM.3}(2)\ \text{labels the }\varepsilon\text{-sealed 3-juncture in the NEUTRAL charge class }q_{\mathrm{net}}=0\ \text{as the }\textbf{neutron};$$
$$\text{the theorem content is the tuple}\quad\bigl(\varepsilon\text{-junction},\ \Theta_{\mathrm{int}}\in2\mathbb Z,\ q_{\mathrm{net}}=0,\ E_{\mathrm{int}}=6,\ w=0\bigr);$$
$$(3)\quad\textbf{THE KEY ROW — the interior already carries }$D^-$\textbf{:}\qquad \boxed{\ \textbf{``the junction vertices are }D^-\textbf{-configured''}\ }\qquad[\text{Census FT.35}(4);\ \mathrm{CT4.1}];$$
$$\text{so the neutral baryon is an OBSERVABLE sealed composite}\ (\mathcal C=1,\ q_{\mathrm{net}}=0,\ \text{a named identification row})\ \textbf{whose interior contains locked content. It is AT.28's configuration, realized.}$$
$$(4)\quad\textbf{the derived metric rows at }E_{\mathrm{int}}=6:\qquad r_s=\tfrac12\mathfrak hE_{\mathrm{int}}=3\mathfrak h\ [\mathrm{BM.43}(1):\ r_s=(1,3,6,12,30)\mathfrak h];\qquad \Delta x_{\mathrm B}=\tfrac{\mathfrak h}{6\ln2};$$
$$\tfrac{G}{\pi\ln2}=2E_{\mathrm{int}}^2=72\ [\mathrm{BM.88}(3)];\qquad \mathcal T_0=\tfrac{6\mathfrak h}{\ln2}\ [\mathrm{BM.115}(1)];\qquad E_{\mathrm{crit}}(r)=\tfrac{2r}{\mathfrak h}\ [\mathrm{BM.148}(1)];$$
$$(5)\quad\textbf{the shatter is at the ENVELOPE, }\neg\textbf{at the subnetwork boundary:}\qquad\text{chart-formed}\iff r\ge r_s=\tfrac12\mathfrak hE_{\mathrm{int}}\ [\mathrm{BM.148}(1)];$$
$$\text{at the envelope }r=\Delta x_{\mathrm B}(E)=\tfrac{\mathfrak h}{E\ln2}:\quad E\le E_{\mathrm{crit}}\bigl(\Delta x_{\mathrm B}(E)\bigr)=\tfrac2{E\ln2}\iff E^2\ln2\le2;$$
$$E_{\mathrm{int}}\ge2\implies E^2\ln2\ge4\ln2=\ln16>2\qquad\Bigl[\ln16>2\iff16>e^2:\ e^2<\bigl(\tfrac{876809}{322560}\bigr)^2<8<16;\ \text{machine}\Bigr];$$
$$\boxed{\ \textbf{no materialized cell is chart-formed at its own envelope}\ }\qquad[\mathrm{BM.148}(4)];$$
$$(6)\quad\textbf{the envelope/horizon ordering — new, exact, and it is a discrete censorship theorem:}$$
$$\Delta x_{\mathrm B}=\frac{\mathfrak h}{E_{\mathrm{int}}\ln2}\ <\ \mathfrak h\ \le\ r_s=\frac{\mathfrak hE_{\mathrm{int}}}2\qquad\iff\qquad \frac1{E\ln2}<\frac E2\iff 2<E^2\ln2,$$
$$\text{and }E^2\ln2\ge4\ln2=\ln16>2\ \text{for every admissible }E_{\mathrm{int}}\ge2\qquad[\mathrm{BM.13}(3);\ \mathrm{BM.148}(4)\text{'s own certificate}];$$
$$\boxed{\ \textbf{the chart-breaking locus lies STRICTLY INSIDE the horizon at every admissible content}\ }$$
$$(7)\quad\textbf{so the answer to the survey's baryon question:}\qquad\text{the neutral baryon behaves as AT.28 predicts — an observable seal with locked content inside — and it does NOT shatter at the subnetwork boundary. The boundary at }r\ge r_s=3\mathfrak h\ \textbf{is chart-formed};\ \text{the shatter is at the envelope, strictly inside};$$
$$(8)\quad\textbf{status: derived.}\qquad\neg\text{a species identification is issued here: ``neutron'' is }\mathrm{Def\text{-}BM.3}(2)\text{'s label at its own locus, and its use is confined to the identification layers}\ [\mathrm{Def\text{-}BM.3}(7)].$$

**Req.** D1.6, D2.9, P1 (Part 1); CT3.17, D3.9 (Part 2); AT.1(3), AT.16, AT.28 (this tier); Def-BM.3(2),(7), Def-BM.4(1), BM.13(3), BM.17(1),(2), BM.43(1), BM.88(3), BM.115(1), BM.132(3), BM.146(3), BM.148(1),(3),(4), BM.149(2), Census FT.35(2),(3),(4),(5), FT.34(5), CT4.1 (Part 4); exact rational inequality arithmetic, the exact integer certificate $e^2<(876809/322560)^2<8<16$ [math; machine: `boundary_census.py` §C].

**Pf.**
$$(6):\ 1/(E\ln2)<E/2\iff2<E^2\ln2\ (\text{cross-multiplication},\ E>0);\ E\ge2\implies E^2\ln2\ge4\ln2=\ln16;\ \ln16>2\iff16>e^2,\ \text{certified by}\ e^2<(876809/322560)^2<8<16;\ \text{and }\mathfrak h\le\mathfrak hE/2\iff E\ge2\ [\text{machine at }E\in\{2,6,12,24,60\}]. \blacksquare$$

**Phys.** The neutral baryon is the survey's decisive case, and it was already in the canon: a
sealed, observable, charge-neutral composite whose *junction vertices are $D^-$-configured*. So
the phenomenon AT.28 identified is not exotic — it is the normal condition of a sealed
composite. The interior is locked; the seal, the charge class, the winding and the edge count are
what the outside sees.

The second result is the ordering. The chart breaks at the Born envelope and is restored at the
horizon, and the envelope is *strictly inside* the horizon for every admissible content, on the
corpus's own exact certificate that $\ln16>2$. So there is a shell — between $r_s$ and
$\Delta x_{\mathrm B}$, i.e. outside the horizon — where the chart read is formed, and the
breaking locus is never exposed. That is a discrete, integer-arithmetic statement of the same
shape as a censorship theorem, and it needs no smooth limit to state.

---

### AT.32 — The generalised invariance, stated exactly, and the tier's adjudication

**Thm.**
$$(1)\quad\textbf{THE GENERALISED SUBNETWORK INVARIANCE (all forces, all rungs):}\qquad\text{for any bounded subnetwork }\Sigma\ \text{with designated observer }o\ \text{and any ambient configuration }C,$$
$$\boxed{\ \text{the ACCESSIBLE content of }\Sigma\ \text{is a function of}\ \bigl(\ \text{the boundary-data triple},\ |R|,\ \text{the rung }n\ \text{of the active mask}\ \bigr)\ \text{and NOTHING ELSE}\ }$$
$$\text{the boundary-data triple}:=\bigl(\text{charge class}\ [\mathrm{Def\text{-}BM.3}(2)\text{--}(3)],\ \ \Theta_{\mathrm{int}}\ \text{class}\ [\mathrm{BM.2}(1)],\ \ S\ \text{winding class}\ [\mathrm{Def\text{-}H.32}(4)]\bigr)\qquad[\mathrm{Def\text{-}BM.5}(1)];$$
$$(2)\quad\textbf{every other datum is bounded out by exactly one of (P1), (P2), (P3):}\qquad\begin{array}{l|l}
\text{the datum} & \text{bounded out by}\\ \hline
\text{the interior vertex activity} & (\mathrm{P1})\ \text{and EM.9b's telescoping}\ [\mathrm{AT.30}(2)]\\
\text{the aspect membership beyond the telescoped ends} & (\mathrm{P2})\ \text{via FT.20's criteria}\ [\mathrm{AT.30}(3),(4)]\\
I_{\mathrm{hid}}(\Sigma;o)\ \text{as an absolute read} & (\mathrm{P1})\ \text{— it is observer-relative by construction}\ [\mathrm{FT.20}\ G\text{-row}]\\
w_i^{\perp}\ \text{(the transverse shift)} & \text{diffeomorphism gauge}\ [\mathrm{AT.5}(3),(4)]\\
\text{the locked }D^-\text{ distribution among vertices} & (\mathrm{P2})+(3)\ \text{— masked at every accessible rung}\ [\mathrm{CT4.2};\ \mathrm{AT.28}]\\
\text{the interior constituent states of a seal} & (\mathrm{P3})\ \textbf{VOID — no construction could exist}\ [\mathrm{BM.143}(1)]\end{array}$$
$$(3)\quad\textbf{the census is finite:}\qquad 9\ \text{aspects}\times5\ \text{rung levels},\qquad \dim\mathcal K_n=6,16,17,25,\qquad D^-\ \text{masked at every accessible rung};$$
$$\text{so ``taking in all forces and rungs'' adds exactly AT.30(1)'s rows and nothing further};$$
$$(4)\quad\textbf{the survey's verdict on ``complete invariance'':}\qquad\textbf{FALSE as stated, TRUE on the accessible sector, and both halves are exact.}$$
$$\text{The failure is }\neg\text{a gap: it is precisely the content of (P1)--(P3), and BM.143(1) makes it a }\neg\exists\text{-theorem rather than a limitation};$$
$$(5)\quad\textbf{what the survey adds to AT.28:}\qquad\begin{array}{l|l}
\text{AT.28} & \text{ONE case: a locked }D^-\ \text{interior}\ \equiv\ \text{an internal Janus network, at fixed boundary data}\\
\textbf{AT.32} & \textbf{ALL cases: every accessible read of ANY subnetwork is a function of the boundary triple, }|R|\textbf{, and the rung}\end{array}$$
$$\text{AT.28 is the }\mathcal D^-\text{/Janus instance; AT.32(1) is the general law, and AT.30(5) is its exact invariant/non-invariant split};$$
$$(6)\quad\textbf{the sharpened consequence for AT-O20:}\qquad\text{AT.30(6) shows every non-invariant row is observer-relative, gauge, or masked. AT.5's longitudinal }w\!\cdot\!\Delta x\ \text{reads off }(\kappa_e,\Delta x^0),\ \text{which are LEDGER data and hence class functions. So the invariance of }w\ \text{across representatives is not merely plausible — it is implied by AT.32(1) for the LONGITUDINAL part, and the transverse part is gauge.}\ \textbf{AT-O20 may already be a theorem.}$$
$$(7)\quad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition (§Cal-AT empty)},\ \neg\text{a new dimensionful scale},\ \neg\text{a measured value or an [EXT] datum},\ \neg\text{a species identification issued},\ \neg\text{an isolated aspect applied},\ \neg\text{a smooth-manifold analogy used};$$
$$(8)\quad\textbf{machine:}\qquad\texttt{canon/era2/boundary\_census.py}\to18/18\ \text{exact};\ \texttt{run\_all\_era2.py}\to\text{all green}. $$

**Req.** AT.5, AT.16, AT.28, AT.29, AT.30, AT.31 (this tier); Def-H.9(2), Def-H.15(3), Def-H.32(4), FT.20, FT.21(i), FT.19 (Part 3); Def-BM.3(2),(3), Def-BM.5(1), BM.2(1), BM.143(1), CT4.2, CT0.13, CT0.14 (Parts 1–4) [math; machine: `boundary_census.py` §§D–E].

**Pf.** Assembly of AT.29–AT.31; clause (2)'s table is a row-wise citation of which of
(P1)/(P2)/(P3) bounds each datum. $\blacksquare$

**Phys.** The survey's answer is a clean dichotomy. Everything the corpus can read from a
subnetwork is a function of three things: the boundary-data triple, the retained edge count, and
the rung of the active mask. Nothing else. That is the generalised invariance, over all nine
aspects and all five rung levels, and it is finite — there are no further rows to find.

And "complete invariance" fails, but only where the corpus has already proved nothing could
succeed. The interior vertex activity, the aspect membership, the absolute hidden information,
the transverse shift, the locked excess distribution and the constituent states of a seal are all
free between representatives — and every one of them is bounded out by the visibility bound, the
mask, or the flux bound, the last of which is a `¬∃`-theorem rather than a limitation. So the
boundary does not merely *look* identical from outside; on the accessible sector it *is*
identical, and the difference lives entirely inside a proven-unconstructible region.

The sharpest payoff is for the open row AT-O20. Since the longitudinal shift reads off
$(\kappa_e,\Delta x^0)$, which are ledger data and therefore class functions on the boundary-data
class, and since the transverse shift is diffeomorphism gauge, the invariance of $w_i$ across
observationally equivalent representatives follows from AT.32(1) rather than needing proof. If
that holds on inspection, specialization (S) retires and Tier AT.1's magnetic functional becomes
derived — which would be the last ansatz in the edifice removed.

---

### AT.33 — AT-O22 closed: $w_i$-invariance is $\neg$ a corollary, and AT.5's nullity is class-relative

**Thm.**
$$(1)\quad\textbf{the question:}\qquad\text{does }w_i\text{-invariance across observationally equivalent representatives follow from AT.32(1)? If so, specialization (S) retires.}$$
$$(2)\quad\textbf{AT.5's closed form has FIVE inputs, and exactly two are class functions:}\qquad (w\!\cdot\!\Delta x)(e)=\frac{\mathfrak h^2\kappa_e/\Omega^2+(\Delta x^0)^2-M_{ij}\Delta x^i\Delta x^j}{2\varkappa\beta\,\Delta x^0}$$
$$\begin{array}{l|l|l|l}
\text{the input} & \text{on the minimal-edge class} & \text{on the general all-nonnull class} & \text{a class function?}\\ \hline
\kappa_e & \equiv1\ \textbf{POINTWISE}\ [\mathrm{FT.24}(4);\ \mathrm{FT.34}(4);\ \mathrm{D1.1}\ \text{Comm-min}] & \text{free in }\mathbb Z_{\ge1}\ \text{per edge}\ [\mathrm{FT.34}\ \text{hyp (ii)}] & \text{floor: YES / general: NO}\\
\Delta x^0 & 1\ \text{tick}\ [\mathrm{D0.7};\ \mathrm{CT0.3}] & 1\ \text{tick} & \textbf{YES, universal}\\
\Omega=e^{\alpha_\Omega a_{00}} & \text{arena}\ [\mathrm{D2.1};\ \mathrm{CT1.12}] & \text{arena} & \textbf{NO}\\
M_{ij}=\delta_{ij}+\varkappa q_{ij} & \text{arena} & \text{arena} & \textbf{NO}\\
\Delta x^i & \text{the hop; }\kappa_e=g_{\mu\nu}\dot x^\mu\dot x^\nu+O(\mathfrak h)\ \text{SAMPLES it} & \text{the hop} & \textbf{NO}\end{array}$$
$$(3)\quad\textbf{the answer:}\qquad\boxed{\ \textbf{NO.}\ \ w_i\text{-invariance is }\neg\textbf{ a corollary of AT.32(1)}\ }$$
$$\mathrm{AT.32}(1)\ \text{makes the ACCESSIBLE CONTENT a class function};\qquad \Omega,\ M_{ij},\ \Delta x^i\ \textbf{are not accessible reads}\ [\mathrm{AT.30}(5)],$$
$$\text{so AT.32(1) does not constrain them, so }(w\!\cdot\!\Delta x)(e)\ \text{is }\neg\text{a class function, so }w_i\ \text{is }\neg\text{invariant across representatives};$$
$$(4)\quad\textbf{the consequence:}\qquad\boxed{\ \textbf{specialization (S) does NOT retire, and (AT-O1) remains genuinely needed}\ }$$
$$(5)\quad\textbf{the floor class is EXTREMAL, not arbitrary — three independent characterizations:}\qquad(\mathrm i)\ \kappa_e\equiv1\ \text{pointwise}\iff\bar\kappa=1\iff\mathrm{CT1.29}'\text{s rate}\ S=\tfrac{A}{\mathfrak h^2}\ln2\ \textbf{holds EXACTLY}\qquad[\mathrm{FT.34}(2)];$$
$$(\mathrm{ii})\ \ \Lambda_c:=\sum_{e\in c}\sqrt{\kappa_e},\qquad \Lambda_c^2\le L\,\Theta(c),\qquad \textbf{equality}\iff\kappa_e\ \textbf{uniform}\qquad[\mathrm{FT.33}(4);\ \text{machine: exact integer witnesses}];$$
$$(\mathrm{iii})\ \ \text{``at fixed }(\Theta,L)\ \textbf{uniform floors MAXIMIZE the bridge ratio}''\qquad[\mathrm{FT.33}(4)];\qquad \kappa=1\ \textbf{is attained, the floor is tight}\qquad[\mathrm{FT.24}(4)];$$
$$(6)\quad\textbf{the reduction on the floor class:}\qquad\kappa_e\equiv1,\ \Delta x^0=1\implies\boxed{\ (w\!\cdot\!\Delta x)(e)=\frac{\mathfrak h^2/\Omega^2+1-M_{ij}\Delta x^i\Delta x^j}{2\varkappa\beta}\ }$$
$$\textbf{three of the five inputs become class-universal; the residual arena dependence is only }(\Omega,\ M_{ij},\ \Delta x^i);$$
$$(7)\quad\textbf{REFINEMENT OF AT.5 — the nullity is CLASS-RELATIVE:}\qquad\begin{array}{l|l|l|l}
& \text{the constraints} & \text{rank} & \text{nullity}\\ \hline
\textbf{floor class}\ (\kappa_e\equiv1\ \text{known}) & \text{one equation PER EDGE, known RHS} & E & \mathbf{2E}\\
\textbf{general class}\ (\text{only sums accessible}) & \text{one per independent closed chain }+\Theta_{\mathrm{int}} & \beta_1+1 & \mathbf{3E-\beta_1-1}\end{array}$$
$$\begin{array}{c|ccccc}
& \text{tetra} & \text{cube} & \text{octa} & \text{dodeca} & \text{icosa}\\ \hline
E & 6 & 12 & 12 & 30 & 30\\
\beta_1=F-1 & 3 & 5 & 7 & 11 & 19\\
\text{floor-class nullity }2E & 12 & 24 & 24 & 60 & 60\\
\textbf{general-class nullity} & \mathbf{14} & \mathbf{30} & \mathbf{28} & \mathbf{78} & \mathbf{70}\end{array}\qquad\text{polygon }P_n:\ 2n\ \text{vs}\ 2n-2$$
$$\textbf{AT.5's nullity }2E\ \textbf{is correct ON THE FLOOR CLASS and understates the freedom on the general class. A scope correction, }\neg\textbf{a refutation.}$$
$$(8)\quad\textbf{(AT-O1) SHARPENS from an ansatz to a finite machine-checkable question:}$$
$$\boxed{\ \text{does }\operatorname{Aut}(\Gamma_S)\ \text{act on the directed edges with a COMMON spatial direction read?}\ }$$
$$\text{YES}\implies\omega_i\ \text{is forced up to the arena's own conformal and spatial modes, and (S) becomes a THEOREM on the floor class};$$
$$\text{NO}\implies\text{(S) is a genuine read-specification and must be logged as a Part-5 declaration requirement};$$
$$\text{either way it is FINITE: }\operatorname{Aut}(\Gamma_S)\ \text{is a known finite group on all five Platonic skeletons and the directed-edge orbits are enumerable}\ [\text{Census FT.66}(1)];$$
$$(9)\quad\textbf{the T-parity closure, and why the floor class still cannot fix the sign:}\qquad\Omega\ (D^+),\ M_{ij}\ (G,H)\ \text{are all T-EVEN};\qquad w_i\ \textbf{is T-ODD}\ [\mathrm{AT.2}(3),(4)];$$
$$\text{so (6)'s reduction relates a T-ODD quantity to T-EVEN arena data divided by }(\varkappa,\beta),\ \text{which are P4 core with values}\neg\text{issued};$$
$$\boxed{\ \textbf{the floor-class reduction does NOT determine the shift's SIGN}\ —\ \text{and that unfixed sign is exactly AT.3(6)'s new observable}\ }$$
$$(10)\quad\textbf{status:}\qquad\textbf{derived:}\ (2),(5),(6),(7),(9);\qquad\textbf{closed with answer NO:}\ \text{(AT-O22)};\qquad\textbf{corrected:}\ \mathrm{AT.5}(6)\text{'s rank statement, which now carries a class qualifier};\qquad\textbf{sharpened:}\ \text{(AT-O1)}. $$

**Req.** D0.7, D1.1, CT0.3 (Part 1); CT1.29, D2.1, CT1.12 (Part 2); AT.2(3),(4), AT.3(6), AT.5(1),(3),(4),(6), AT.6, AT.15(4),(5), AT.30(5), AT.32(1),(2) (this tier); Def-H.9(3), FT.22, FT.24(4), FT.33(1),(4), FT.34 hyp (ii), FT.34(2),(4), FT.46(2) (Part 3); Def-BM.4(1), Def-BM.5(1), BM.149(2), Census FT.63(2), Census FT.66(1) (Part 4); exact Cauchy–Schwarz certificates at integer witnesses, exact integer nullity arithmetic [math; machine: `ato22.py` 16/16].

**Pf.**
$$(3):\ \text{AT.32(1) constrains the accessible content; }\Omega,M_{ij},\Delta x^i\ \text{are absent from AT.30(5)'s invariant column and present in no accessible read, so two representatives may share the boundary triple, }|R|\ \text{and the rung while differing in them};$$
$$(5\mathrm{ii}):\ \Lambda_c^2=(\sum_e\sqrt{\kappa_e})^2\le L\sum_e\kappa_e=L\,\Theta(c)\ \text{by Cauchy–Schwarz, with equality}\iff\sqrt{\kappa_e}\ \text{proportional to }1\iff\kappa_e\ \text{uniform}\ [\text{machine: equality at }(1,1),(1,1,1,1),(4,4,4),(9,9,9),(4,4,4,4);\ \text{strict at }(1,4),(1,1,4),(1,4,9)];$$
$$(7):\ \text{the floor class supplies }E\ \text{equations with known RHS }(\kappa_e\equiv1);\ \text{the general class supplies only }\beta_1\ \text{chain windings plus }\Theta_{\mathrm{int}},\ \text{i.e. }\beta_1+1\ \text{sums},\ \text{against }3E\ \text{shift coordinates}. \blacksquare$$

**Phys.** The question was whether the last ansatz in the edifice could be retired by a
corollary. It cannot, and the reason is exact: the longitudinal shift is a closed-form function of
five inputs, and three of them — the conformal mode, the spatial metric and the hop direction —
are arena data that the generalised invariance leaves free. Making the accessible content a class
function does not make the arena a class function.

Two things improve anyway. The floor class is not a convenience; it is the *extremal* class,
characterized three independent ways — it is the unique class on which CT1.29's area-entropy rate
holds exactly, it is the Cauchy–Schwarz equality case, and it maximizes the bridge ratio at fixed
winding and length. On it, three of the five inputs become class-universal and the residual
freedom is just $(\Omega, M_{ij}, \Delta x^i)$. And AT.5's nullity needs a class qualifier: $2E$ on
the floor class, $3E-\beta_1-1$ on the general one — a scope correction, with the general class
strictly freer at every one of the five solids.

So (AT-O1) stops being a vague homogeneity assumption and becomes a finite question about
$\operatorname{Aut}(\Gamma_S)$'s action on directed edges: does it carry a common spatial direction
read? If yes, (S) is a theorem on the floor class; if no, (S) must be logged as a Part-5
declaration. Both are decidable by enumeration over five known finite groups.

One closure the reduction cannot reach, and it is the right one to leave open: all three residual
inputs are T-even while the shift is T-odd, so the floor-class formula relates a T-odd quantity to
T-even data over $(\varkappa,\beta)$, whose values are not issued. **The sign of the shift stays
unfixed** — which is precisely the freedom AT.3(6) identified as the magnetic read's new
observable content. A theory that fixed it here would have contradicted its own magnetism.

---

### AT.34 — (AT-O1) closed with answer YES: the homogeneity step is a theorem, and (S) is derived up to one calibration scale

**Thm.** *No group enumeration is used beyond the tetrahedron ($K_4$, all $4!=24$
permutations). Every input is a canon order.*
$$(1)\quad\textbf{the canon's own orders:}\qquad |\operatorname{Aut}(\Gamma_S)|=(24,48,48,120,120),\qquad |\operatorname{Rot}|=(12,24,24,60,60)\qquad[\text{Census FT.65}(1)];$$
$$E=(6,12,12,30,30)\qquad[\mathrm{Def\text{-}H.20}];\qquad \boxed{\ |\operatorname{Rot}|\ =\ 2E\ \ \textbf{EXACTLY, for all five}\ }\qquad |\operatorname{Aut}|=2|\operatorname{Rot}|;$$
$$(2)\quad\textbf{the arc stabilizer in the rotation group is TRIVIAL:}\qquad\text{a rotation fixing the directed edge }(u\to v)\ \text{must fix }u,v\ \text{individually and preserve direction;}$$
$$\text{the only rotation axis associated with an edge is the one through its midpoint and the centre, and the half-turn about it SWAPS }u\ \text{and}\ v\ —\ \textbf{it reverses the arc};$$
$$\therefore\ \operatorname{Stab}_{\operatorname{Rot}}(\text{arc})=\{\mathrm{id}\}\qquad[\text{machine: verified on }K_4];$$
$$(3)\quad\textbf{arc-transitivity, by orbit-stabilizer and arithmetic alone:}\qquad |\operatorname{orbit}(\text{arc})|=\frac{|\operatorname{Rot}|}{|\operatorname{Stab}_{\operatorname{Rot}}|}=\frac{2E}{1}=2E=\#\{\text{arcs}\};$$
$$\boxed{\ \operatorname{Rot}\ \textbf{acts SIMPLY TRANSITIVELY on the arcs};\qquad \operatorname{Aut}(\Gamma_S)\ \textbf{is ARC-TRANSITIVE, all five solids}\ }$$
$$(4)\quad\textbf{the arc stabilizer in the full group:}\qquad |\operatorname{Stab}_{\operatorname{Aut}}(\text{arc})|=\frac{|\operatorname{Aut}|}{2E}=2\qquad\text{for all five}\quad(24/12,\ 48/24,\ 48/24,\ 120/60,\ 120/60);$$
$$(5)\quad\textbf{the stabilizer element is a REFLECTION, not a half-turn:}\qquad\text{it has order }2\ \text{and is}\neg\text{a half-turn by (2), so it is orientation-reversing;}$$
$$\text{a reflection in }\mathbb R^3\ \text{has eigenvalues}(+1,+1,-1),\ \chi=+1,\ \text{and fixes its mirror PLANE};$$
$$\boxed{\ \dim(\mathbb R^3)^{\operatorname{Stab}(\text{arc})}=\frac{\chi(\mathrm{id})+\chi(h)}{|\operatorname{Stab}|}=\frac{3+1}2=2\ }\qquad[\text{machine on the tetrahedron: }\det=-1,\ \operatorname{tr}=+1,\ \dim\ker(M-I)=2,\ \text{exact over }\mathbb Q];$$
$$\textbf{the mirror plane CONTAINS the arc direction};$$
$$(6)\quad\textbf{the reduction, step by step:}\qquad\text{an }\operatorname{Aut}\text{-invariant per-edge shift assignment }w:\text{arcs}\to\mathbb R^3\ \text{is}$$
$$\begin{array}{l|l|l}
\text{the stage} & \text{the reason} & \text{free parameters}\\ \hline
\text{per arc, unrestricted} & 3\ \text{components}\times2E\ \text{arcs} & 6E\\
\text{floor-constant} & \text{arc-transitivity}\ (3) & 3\\
\text{in the mirror plane} & \text{the reflection stabilizer}\ (5) & 2\\
\textbf{on shell} & \text{AT.5's longitudinal }w\!\cdot\!\Delta x\ \text{constraint, and the mirror plane contains the arc direction} & \mathbf{1}\end{array}$$
$$\boxed{\ \textbf{ONE free parameter per floor: the SCALE of the shift along a DETERMINED line}\ }$$
$$(7)\quad\textbf{the verdict on (AT-O1) and on specialization (S):}\qquad\textbf{ANSWER YES on the floor class.}\ \ \text{The direction }\omega_i\ \textbf{is forced, up to scale, by}\ \operatorname{Aut}(\Gamma_S)\text{'s arc-transitivity}+\text{the reflection stabilizer}+\mathrm{AT.5}'\text{s longitudinal constraint};$$
$$\boxed{\ (\mathrm S)\ \textbf{is RECLASSIFIED from ``marked specialization,}\neg\textbf{adopted'' to ``DERIVED UP TO ONE CALIBRATION SCALE PER FLOOR''}\ }$$
$$(8)\quad\textbf{the remaining scale is calibration, not structure:}\qquad\text{it rides on }(\varkappa,\beta),\ \text{P4 core, values}\neg\text{issued}\ [\mathrm{C4};\ \mathrm{\S Cal\text{-}2}];$$
$$\text{and by AT.33(9)/AT.15 it CANNOT be fixed by any carrier read: the shift is T-ODD while every carrier-side invariant is T-EVEN};$$
$$\text{the same disposition as }\mathfrak h\ [\mathrm{P1}]\ \text{and}\ e_0\ [\mathrm{EM.25}(7)];$$
$$(9)\quad\textbf{the reduction table, exact:}\qquad\begin{array}{c|ccccc}
& \text{tetra} & \text{cube} & \text{octa} & \text{dodeca} & \text{icosa}\\ \hline
\mathrm{AT.33}\ \text{floor nullity}\ 2E & 12 & 24 & 24 & 60 & 60\\
\textbf{after (AT.34)} & \mathbf1 & \mathbf1 & \mathbf1 & \mathbf1 & \mathbf1\end{array}$$
$$(10)\quad\textbf{status:}\qquad\textbf{derived:}\ (1)\text{--}(7),(9);\qquad\textbf{closed with answer YES:}\ (\mathrm{AT\text{-}O1});\qquad\textbf{reclassified:}\ (\mathrm S);\qquad\textbf{calibration:}\ (8)\text{'s scale}. $$

**Req.** D0.7, D1.6, P1, P4 (Part 1); C4, §Cal-2, CT1.12, EM.25(7) (Part 2); AT.2(3),(4), AT.3(6), AT.5(1),(3), AT.15(4),(5), AT.33(6),(9) (this tier); Def-H.20, Census FT.63(2), Census FT.65(1), Census FT.66(1) (Parts 3–4); orbit-stabilizer, the character formula for a fixed subspace $\dim V^H=\frac1{|H|}\sum_{h\in H}\chi(h)$, exact $3\times3$ linear algebra over `Fraction`, exhaustive $K_4$ permutation census [math; machine: `ato1.py` 14/14].

**Pf.**
$$(1):\ \text{Census FT.65}(1)\text{'s orders against Def-H.20's cardinals: }2E=(12,24,24,60,60)=|\operatorname{Rot}|\ [\text{machine: exact integers}];$$
$$(2),(3):\ \text{the half-turn about the edge-midpoint axis maps }(u\to v)\ \text{to}\ (v\to u);\ \text{verified on }K_4\ \text{by exhaustive search over all }24\ \text{permutations, with the rotation subgroup identified as }A_4\ \text{by parity};\ \text{orbit-stabilizer then gives the whole arc set};$$
$$(5):\ \det=-1\ \text{and}\ \operatorname{tr}=+1\ \text{are the reflection invariants (a half-turn has }\operatorname{tr}=-1);\ \text{the tetrahedron's vertices }(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\ \text{are rational, so the realization is solved exactly over }\mathbb Q;\ \text{the dodecahedron and icosahedron share }\operatorname{Aut}=A_5\times\mathbb Z_2\ \text{and the same }|\operatorname{Aut}|/(2E)=2;$$
$$(6):\ \text{the mirror plane of the stabilizer reflection contains the arc direction, so AT.5's longitudinal constraint, which fixes }w\!\cdot\!\Delta x,\ \text{removes one of the plane's two dimensions}. \blacksquare$$

**Phys.** This closes the last ansatz in the edifice, and it closes it with arithmetic rather than
computation: the canon already records that each Platonic rotation group has exactly as many
elements as the skeleton has directed edges — $|\operatorname{Rot}| = 2E$ — and that single numerical
fact, with the observation that a half-turn reverses an arc, forces the rotation group to act
simply transitively on arcs. Arc-transitivity then collapses a per-edge vector field to one
vector; the stabilizer being a reflection confines that vector to a plane; and the on-shell
longitudinal condition, whose direction lies in that plane, confines it to a line.

So specialization (S) was never really an assumption. Its homogeneity step is a theorem, and what
it adds beyond the symmetry is a single number per floor — the magnitude of the shift along a
direction the symmetry has already fixed. That is the same status as $\mathfrak h$ and $e_0$:
dimensionful calibration, not structural freedom. And by AT.15/AT.33(9) no carrier read can fix
it, because the shift is T-odd and every carrier invariant is T-even — which is precisely why the
magnetic read is a new observable rather than a repackaging.

The whole Level 5 chain now runs with **one** calibration parameter in the magnetic sector
instead of an ansatz: network → spine → metric → shift direction (derived) → shift scale
(calibration) → the split → the magnetic functional and its attenuation theorem.

---

## §Open-AT additions from Tier AT.5

| row | content | locus |
|---|---|---|
| ~~(AT-O22)~~ | **CLOSED by AT.33, answer NO.** `Ω`, `M_ij`, `Δx^i` are arena data, not accessible reads, so AT.32(1) does not constrain them. (S) does **not** retire. Also **refines AT.5(6)**: the nullity is class-relative, `2E` on the floor class and `3E−β₁−1` on the general one | AT.33 |
| (AT-O23) | **the envelope/horizon shell**: AT.31(6) proves `Δx_B < 𝔥 ≤ r_s` for every admissible `E_int`, so there is a chart-formed shell strictly outside the breaking locus. Whether that shell has a derived read — an area, an entropy, or a membrane — is open, and BM.149(3)'s one-way membrane is the natural candidate | AT.31(6); BM.148(1),(4); BM.149(3) |
| ~~(AT-O1)~~ | **CLOSED by AT.34, answer YES.** `|Rot| = 2E` [Census FT.65(1)] + the half-turn reverses an arc ⟹ `Rot` acts **simply transitively on arcs** ⟹ `Aut` is arc-transitive; the stabilizer is a **reflection**, so `dim = 2`; AT.5's longitudinal constraint then leaves **ONE** parameter per floor. **(S) reclassified: derived up to one calibration scale.** No enumeration of the higher solids needed | AT.34 |
| (AT-O25) | **the sign of the shift** is unfixed by the floor-class reduction, since `Ω, M_ij, Δx^i` are T-even, `w_i` is T-odd, and `(ϰ,β)` are P4 core with values ¬issued. Whether any formed read fixes the sign — or whether it is irreducibly calibration — is open, and it is the same question as the magnetic observable's magnitude | AT.33(9); AT.3(6); §Cal-2 |
| (AT-O24) | **aspect membership as an interior-sensitive datum**: AT.30(3) shows 14 of 32 five-edge chains have `q=0` with nonzero interior activity. Whether that interior sensitivity is itself bounded — i.e. whether the *set* of admissible memberships is a class function even though the criterion is not — is open and is the sharpest form of the completeness question | AT.30(3),(4); FT.20; FT.21(i) |
