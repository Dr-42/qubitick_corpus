# $\langle qu(b(i(t|t))ick)\rangle$ — **Part 5 · Atomic era** — Tier AT.7: the hydrogen spine

**Level.** 5. **Era.** 2 (the Atomic era). **Tier.** AT.7 — the EM sealing grammar, the dynamics
of Q as a universe-level Born-width distribution, the binding-scaling no-go, and the two-body
resolvent with its harmonic pole ladder.
**Tags.** AT.41–AT.45. **Pattern.** BM.130 / BM.144 / BM.152 — the construction tiers and the
status-and-closure tag of a tier.
**Status.** discovery-phase working tier, **closed at AT.45**. Nothing is adopted into the frozen
canon; no declaration issues; §Cal-AT stays empty; no clause of Parts 1–4 is modified, retracted
or renumbered.
**Machine.** `canon/era2/em_seal_grammar.py` → **19/19 exact** (AT.41); `canon/era2/q_dynamics.py`
→ **14/14 exact** (AT.42); `canon/era2/binding_scaling.py` → **13/13 exact** (AT.43);
`canon/era2/two_body_resolvent.py` → **16/16 exact** (AT.44); `canon/era2/check_era2_format.py` →
the format + citation gate for every Part 5 document. `canon/era2/run_all_era2.py` →
**28 checkers, 497 exact markers, 0 failures, exit 0**. Exact arithmetic throughout: `Fraction`,
integer binomials, exhaustive enumeration ($2^6$, $2^{3..9}$, the $27$-component colour tensor),
formal power series over $\mathbb Q$ with coefficient-wise equality, an SOS identity in
$\mathbb Q[\varepsilon_q]$, rigorous `Fraction` intervals. **No floating point in any assertion.
No measured value enters any derivation [P5].**
**Charter.** Part 5 cites Parts 1–4 and earlier AT-tags only.
**Mandate.** Three Architect directives, executed in order: **(i)** construct the EM sealing
grammar from the neutron template $\Sigma_{12}$ and extract the rule that determines $q$ from
topology and edge signs (AT-O4); **(ii)** formalize the dynamics of Q — the lepton–baryon
interaction — as a global, topology-blind configuration sum yielding a discrete universe-level
Born-width distribution, with no smooth-manifold concepts (BM.6(5)/BM.48(3)); **(iii)** compute
the two-body resolvent pole — the lepton mass read and the hydrogen spectrum — closing AT-O5 and
AT.43(R3) simultaneously, the $1/n^2$ falling out of the ledger's own move system.
**Discovery record.** `era2/EM_SEAL_GRAMMAR.md`, `era2/Q_DYNAMICS_BORNWIDTH.md`,
`era2/BINDING_SCALING_NOGO.md`, `era2/TWO_BODY_RESOLVENT.md` (the four working documents, with
the directive transcripts and the placement rows).

---

## Tier AT.7 — the hydrogen spine: grammar, dynamics, no-go, resolvent

### AT.41 — The EM sealing grammar, built from $\Sigma_{12}$: the proton is the neutron by a boundary flip, and the grammar factors

**Thm.**
$$(1)\quad\textbf{the cell and its census (re-produced from the neutron template):}\qquad\Sigma_{12}=\{p_1,q_1\}\cup\{p_2,q_2\},\ \text{two materialized 2-cycles joined by a bidirectional connector}\ [\mathrm{AT.31}(1);\ \mathrm{BM.17}(1)];$$
$$=\ \text{THREE bidirectional channels}\ =\ 6\ \text{directed edges},\qquad E_{\mathrm{int}}=6\ (c_1{:}\,2,\ c_2{:}\,2,\ \text{connector}{:}\,2);$$
$$\text{each channel's two edge signs}\ (a_i,b_i)\ \text{give}\ q_i=\tfrac12(a_i-b_i)\in\{-1,0,+1\}\ [\mathrm{D3.4};\ \mathrm{EM.9}],\qquad Q=q_1+q_2+q_3\ [\mathrm{Def\text{-}BM.8}(1)];$$
$$\textbf{the exhaustive }2^6=64\textbf{ census:}\qquad W_3(Q)=(1,6,15,20,15,6,1)=\binom{6}{Q+3}=[z^Q](2+z+z^{-1})^3\ [\mathrm{BM.135}(2);\ \mathrm{BM.28}(2)];$$
$$\boxed{\ W_3(+1)=15\ (\text{the proton class}),\qquad W_3(0)=20\ (\text{the neutron class}),\qquad \frac{W_3(0)}{W_3(\pm1)}=\frac{20}{15}=\frac43\ }$$
$$(2)\quad\textbf{(S1) the proton-from-neutron move is PURELY BOUNDARY:}\qquad\text{EM.9b telescoping}:\ \textstyle\sum_if_{v_i}=\tfrac12(\sigma_{\text{last}}-\sigma_{\text{first}})=-q_{\mathrm{EM}},$$
$$\text{verified on ALL }1016\ \text{sign assignments, chains of }3..9\ \text{edges};\qquad\text{flipping any INTERIOR edge sign leaves}\ q_{\mathrm{EM}}\ \textbf{invariant};$$
$$\boxed{\ q_{\mathrm{EM}}\ \textbf{is a function of the two end registers alone};\qquad\text{EM.9's end-pair table}\ (++{,}+-{,}-+{,}--)\mapsto(0,+1,-1,0),\quad m_q=(2,1,1)\ }$$
$$(3)\quad\textbf{(S3) the strong seal is a COLOUR partition, independent of the edge signs:}\qquad\mathcal C(\Sigma_{12};C)=1\iff\text{the three attachments seal as ONE }\varepsilon\text{-triple}\ [\mathrm{AT.31}(1);\ \mathrm{CT3.17a}(1)];$$
$$\varepsilon_{\sigma i\sigma j\sigma k}=\operatorname{sgn}(\sigma)\,\varepsilon_{ijk},\qquad\dim\wedge^3(\mathbb C^3)=\binom33=1\qquad[\mathrm{BM.136}(1);\ \text{machine: all }6\times27];$$
$$\textbf{the colour tensor carries NO edge-sign symbol}\implies\boxed{\ \mathcal C=1\ \text{on EVERY one of the }64\ \text{sign assignments; all }15\ \text{proton assignments are }\varepsilon\text{-sealable}\ }$$
$$\text{the seal GATES the read}\ (\mathcal C=0\implies Q\ \text{undefined; one dangling attachment zeroes the sector}\ [\mathrm{FT.19};\ \mathrm{Def\text{-}BM.8}(4)])\ \textbf{without constraining its value}$$
$$(4)\quad\textbf{(S2) minimality — }Q=+1\textbf{ does NOT select the proton; the SEAL does:}$$
$$\delta\text{-seal (meson, }k=2):\quad E_{\mathrm{int}}^{\min}=2\cdot2=4\ [\mathrm{BM.111}(1),(5);\ \mathrm{BM.110}(1)],\qquad W_2(Q)=\binom{4}{Q+2}=(1,4,6,4,1),\quad W_2(+1)=4;$$
$$\varepsilon\text{-seal (baryon, }k=3):\quad E_{\mathrm{int}}^{\min}=3\cdot2=6=\Sigma_{12}\ [\mathrm{BM.17}(1)];\qquad\text{a lone attachment is never sealed}\implies k\ge2\ \ \forall\,\text{seal}\ [\mathrm{CT3.17a}(1)];$$
$$\boxed{\ \textbf{minimal SEALED }Q=+1:\ \text{the charged meson,}\ E_{\mathrm{int}}=4\ (\text{boson}\ [\mathrm{BM.129}(1)],\ \Theta_{\mathrm{int}}\in2\mathbb Z)\ }\qquad\boxed{\ \textbf{minimal BARYON }Q=+1:\ \text{the proton,}\ E_{\mathrm{int}}=6\ (\text{fermion}\ [\mathrm{BM.136}(4)(\mathrm a)],\ \Theta_{\mathrm{int}}\in4\mathbb Z\ [\mathrm{BM.2}(1)])\ }$$
$$(5)\quad\textbf{THE EM SEALING GRAMMAR (the extracted rule), for a sealed composite}\ \Gamma:$$
$$(\mathrm{G1})\ \textbf{partition:}\ \ \mathrm{Colour}(\Gamma)\ \text{partitions into blocks of size }2\ (\delta)\ \text{and }3\ (\varepsilon/\bar\varepsilon);\quad\mathcal C=1\iff\neg\exists\,\text{lone attachment}\ [\mathrm{CT3.17a}(1);\ \mathrm{FT.19}];$$
$$(\mathrm{G2})\ \textbf{charge, boundary-exact:}\quad Q(\Gamma)=\sum_{\text{blocks}}\ \sum_{c\in\text{block}}\tfrac12\bigl(\sigma_{s(c)}-\sigma_{t(c)}\bigr);\quad\text{interior signs telescope out}\ [\mathrm{Def\text{-}BM.8}(1);\ \mathrm{BM.135}(6);\ \mathrm{EM.9b}];$$
$$(\mathrm{G3})\ \textbf{observability:}\quad Q\ \text{is defined only where}\ \mathcal C=1\ [\mathrm{FT.19};\ \mathrm{CT3.22}];\qquad(\mathrm{G4})\ \textbf{range + census:}\quad Q\in\{-k,\dots,k\};\quad W_k(Q)=\binom{2k}{Q+k};\quad\tfrac13,\tfrac23\ \text{unreachable}\ [\mathrm{Def\text{-}BM.8}(5),(6);\ \mathrm{BM.28}(7)]$$
$$(6)\quad\textbf{the answer to the directive's step 4/5:}\qquad\textbf{TRIVIAL for the observable:}\ Q\ \textbf{is boundary-exact — interior topology cannot change it;}$$
$$\textbf{NONTRIVIAL as a whole, in two rows the boundary cannot see:}\quad(\mathrm{N1})\ \text{the SEAL CLASS (G1) fixes}\ k,\ \text{hence the range of}\ Q,\ \text{the}\ E_{\mathrm{int}}\ \text{floor}\ 2k,\ \text{the statistics, the}\ \Theta_{\mathrm{int}}\ \text{class};$$
$$(\mathrm{N2})\ \text{the ASPECT MEMBERSHIP is interior-sensitive}\ [\mathrm{AT.30}(3):\ 14\ \text{of}\ 32\ \text{five-edge chains have}\ Q=0\ \wedge\ f_v\ne0\ \text{inside}];$$
$$\boxed{\ \textbf{THE SEALING RULE: the grammar FACTORS as}\ (\text{boundary signs}\to Q)\ \times\ (\text{interior colour partition}\to\text{seal class}),\ \textbf{two INDEPENDENT registers}\ }$$
$$\text{the proton}\ =\ (\varepsilon\text{-seal},\ 3\ \text{triplets})\ \wedge\ (Q=+1):\qquad\textbf{BOTH registers are required}\ —\ Q=+1\ \text{alone admits the}\ E_{\mathrm{int}}=4\ \text{charged meson}$$
$$(7)\quad\textbf{the sign-convention row (a presentational correction, offered):}\qquad\text{canon}\ [\mathrm{D3.4};\ \mathrm{EM.9}]:\ q_{\mathrm{EM}}=\tfrac12(\sigma_s-\sigma_t)=\tfrac12(\sigma_{\text{first}}-\sigma_{\text{last}});$$
$$\text{the telescoped sum of}\ \mathrm{AT.30}(2)\ \text{is}\ \tfrac12(\sigma_{\text{last}}-\sigma_{\text{first}})=-q_{\mathrm{EM}}\ [\mathrm{EM.9b}]:\qquad\text{an overall chain-orientation gauge;}\ W(+1)=W(-1)\ \text{so nothing downstream moves;}$$
$$\mathrm{AT.30}(2)\text{'s label}\ \text{``}\textstyle\sum_if_{v_i}=\dots=q\text{''}\ \text{should read}\ \text{``}=-q_{\mathrm{EM}}\text{''}\ —\ \text{recorded,}\ \neg\text{a retraction of any derived content}$$
$$(8)\quad\textbf{status:}\qquad\textbf{re-certified (}\neg\textbf{new):}\ \mathrm{Def\text{-}BM.8}(1),(5),(6),(7),\ \mathrm{BM.135}(2),(3),(6),\ \mathrm{BM.28}(2),\ \mathrm{EM.9}/\mathrm{EM.9b},\ \mathrm{AT.30}(2),\ \mathrm{BM.136}(1);$$
$$\textbf{sharpened (new at L5):}\ (\mathrm{S1}),(\mathrm{S2}),(\mathrm{S3}),\ (6),\ (7);\qquad\textbf{NOT crossed here:}\ \text{the dynamics of}\ Q\ [\mathrm{BM.6}(5)]\ —\ \text{constructed at AT.42};$$
$$\neg\text{a declaration},\quad\neg\text{a P4 addition},\quad\neg\text{a new dimensionful scale}\ [\mathrm{P1}],\quad\neg\text{a measured value}\ [\mathrm{P5}],\quad\neg\text{a species identification beyond}\ \mathrm{Def\text{-}BM.3}(7)$$

**Req.** D3.4, D3.9 (Parts 1–2); CT3.17a(1), CT3.22, EM.9, EM.9b, EM.12, EM.24(1), P2, P5 (Part 2); FT.19, FT.28, FT.40, FT.41, AT.30(2),(3), AT.31(1) (Part 3 / this level); Def-BM.3(2),(3),(7), Def-BM.8(1),(3),(4),(5),(6),(7), BM.2(1), BM.17(1), BM.26, BM.28(1),(2),(7), BM.30(2), BM.48(3),(4), BM.55, BM.110(1),(3),(4), BM.111(1),(5), BM.129(1), BM.135(2),(3),(6),(7), BM.136(1),(4) (Part 4); exhaustive enumeration of the $2^6$ and $2^4$ end-sign assignments, generating-function convolution on integer coefficients, the exact $27$-component Levi-Civita tensor, `Fraction` census arithmetic [math; machine: `em_seal_grammar.py` §§A–F, 19/19].

**Pf.**
$$(1):\ \text{the }2^6\ \text{enumeration};\ W_3(Q)=\binom{6}{Q+3}\ \text{matched coefficient-wise and against}\ (2+z+z^{-1})^3\ \text{convolved exactly}\ [\text{machine A1,A2}];\ 20/15=4/3\ [\text{machine A3}];\ W(+1)=W(-1)\ [\text{machine A4}]$$
$$(2):\ \textstyle\sum_i\tfrac12(\sigma_{i+1}-\sigma_i)=\tfrac12(\sigma_{\text{last}}-\sigma_{\text{first}})\ \text{telescopes}\ [\text{machine B1}];\ \sigma_j\mapsto-\sigma_j\ \text{interior leaves}\ \tfrac12(\sigma_{\text{first}}-\sigma_{\text{last}})\ \text{fixed}\ [\text{machine B2,B3}]$$
$$(3):\ \varepsilon_{\sigma i\sigma j\sigma k}=\operatorname{sgn}(\sigma)\varepsilon_{ijk}\ \text{over all}\ 6\sigma\ \text{and}\ 27\ \text{triples}\ [\text{machine C1}];\ \neg\exists\,\sigma\ \text{in}\ \varepsilon_{ijk}\implies\mathcal C\ \sigma\text{-blind}\ [\text{machine C2}];\ g(1)=0\ [\mathrm{CT3.17a}(2);\ \text{machine C3}]$$
$$(4):\ \text{the }2^4\ \text{census}\ [\text{machine D1}];\ E^{\min}(\delta)=4,\ E^{\min}(\varepsilon)=6\ [\mathrm{BM.111}(5);\ \mathrm{BM.17}(1);\ \text{machine D2,D3}];\ 4\mathbb Z\subsetneq2\mathbb Z\ [\mathrm{BM.110}(4);\ \text{machine D4}]$$
$$(5),(6):\ \text{block additivity exhaustive at}\ k\le4\ [\text{machine E1}];\ W_k(Q)=\binom{2k}{Q+k},\ \sum_QW_k=4^k,\ k=1..4\ [\text{machine E2}];\ \text{assembly}\ [\text{machine E3}];\ (7),(8):\ \text{the convention map and the status record}\ [\text{machine F1,F2}].\ \blacksquare$$

**Phys.** Asked to build the proton from the neutron, the ledger answers that they are the *same
graph*: the $\varepsilon$-sealed $3$-juncture $\Sigma_{12}$ at $E_{\mathrm{int}}=6$, whose geometric
reads are charge-blind [BM.28(1)]. The proton is the neutron with its two **end registers** flipped
into the $Q=+1$ class — fifteen of the sixty-four assignments — and *only* the ends matter, because
every interior sign telescopes away. That is the trivial half of the grammar. The nontrivial half is
that the strong seal is a **colour** partition and the colour tensor carries no edge-sign symbol, so
seal and charge are independent registers: the seal gates whether $Q$ is observable at all but never
constrains its value. The consequence is the minimality row: $Q=+1$ does **not** pick out the
proton — the smallest sealed object carrying it is the $\delta$-sealed **charged meson** at
$E_{\mathrm{int}}=4$, a boson, against the proton's $\varepsilon$-sealed fermion at
$E_{\mathrm{int}}=6$, with sealing phases in $2\mathbb Z$ against $4\mathbb Z$. The same integer
charge lives in two disjoint kinds, and only the interior colour partition tells them apart. What
this tag does *not* do is bind: the grammar is the gate, and the door — the dynamics of $Q$ — is
AT.42.

---

### AT.42 — The dynamics of Q: the lepton–baryon interaction is one global Janus configuration sum, infinite-ranged by the absence of a local EM seal, its "orbital" a discrete Born-width distribution

**Thm.**
$$(1)\quad\textbf{THE GLOBAL CONFIGURATION SUM.}\ \ \text{A sealed baryon register}\ (\Sigma_{12},\ Q{=}+1,\ \varepsilon\text{-sealed}\ [\mathrm{AT.31}])\ \text{and a lepton register}\ (Q{=}-1,\ \text{colour-singlet},\ \text{unsealed}\ [\mathrm{D3.8}])$$
$$\text{are ONE configuration}\ C=(R,\sigma)\ \text{in ONE topology-blind sum}\qquad Z=\sum_{\Gamma\in\mathcal G_B}\ \sum_{R\in\mathfrak C_B(\Gamma)}\ w(R,\sigma)\qquad[\mathrm{Def\text{-}H.32}(1),(2);\ \mathrm{A8}];$$
$$\text{the connector is an}\ n\text{-pair floor, each pair retained (weight }p)\ \text{or dissolved (weight }u)\ [\mathrm{BM.137}(1);\ \mathrm{BM.19}(1),(2)],\ \text{so the retained content}\ E_{\mathrm{int}}=|R|=2j\ \text{is distributed by}$$
$$\boxed{\ P_{\mathrm{mat}}(E_{\mathrm{int}}{=}2j)=\binom njp^ju^{n-j}\big/(1-u^n),\quad j\ge1,\qquad p=1-4\varepsilon_q,\quad u=4\varepsilon_q\ }\qquad[\text{machine A1,A2}]$$
$$(2)\quad\textbf{INFINITE RANGE = the unbounded geometric resolvent.}\ \ \text{The EM propagator is}\ \ \sum_{n\ge0}\langle\varnothing|\hat U^n|\varnothing\rangle\,w^n=\frac1{1-w^2x_+x_-}\ \ [\mathrm{FT.108}(5);\ \mathrm{BM.121}(2)];$$
$$(1-z)\sum_{n=0}^{N}z^n=1-z^{N+1}\ \text{coefficient-wise over}\ \mathbb Q\ [\text{machine B1}];\qquad\text{every order carries}\ (x_+x_-)^n\ \text{with coefficient}\ 1\implies\textbf{the sum NEVER terminates}\ [\text{machine B2}];$$
$$\textbf{the contrast:}\ \mathcal C=0\ \text{on ONE dangling colour attachment}\implies F^{\Sigma}_{\mathrm{strong}}=0\ [\mathrm{FT.19}]\ —\ \text{the strong sum TRUNCATES at the seal};\qquad\boxed{\ \textbf{infinite range IS the absence of a local EM seal}\ }\ [\text{machine B3}]$$
$$(3)\quad\textbf{THE DISCRETE 'ORBITAL' = a universe-level Born-width distribution.}\ \ \Delta x_{\mathrm B}(E_{\mathrm{int}})=\frac{\mathfrak h}{E_{\mathrm{int}}\ln2}=\frac1{m_{\mathrm{hid}}}\ \ [\mathrm{Def\text{-}BM.4}(1)],\qquad\text{support}\ \Bigl\{\tfrac{\mathfrak h}{2j\ln2}\Bigr\}_{j\ge1},\ \ \text{weights}\ P_{\mathrm{mat}}(2j);$$
$$\Sigma P=1\ \text{exactly}\ [\text{machine C-a,C-b}];\qquad\langle E_{\mathrm{int}}\rangle_{\mathrm{mat}}=\tfrac{2n}{D_n},\quad\operatorname{Var}(E_{\mathrm{int}})<\infty\implies\textbf{localized by binomial concentration, }\neg\textbf{by a}\ 1/r\ \textbf{well}\ [\mathrm{BM.137}(1);\ \text{machine C1}];$$
$$\boxed{\ \varepsilon_q=0\implies P_{\mathrm{mat}}(E_{\mathrm{int}}{=}2n)=1:\ \text{collapse to the single crystallized width}\ \tfrac{\mathfrak h}{2n\ln2}\ }\qquad[\mathrm{BM.19}(3);\ \mathrm{BM.137}(2)]$$
$$(4)\quad\textbf{THE SPECTRAL RATIO, geometric route.}\ \ \text{At the floors}\ E_{\mathrm{int}}=2n\ [\mathrm{FT.28};\ \mathrm{BM.137}(2)]:\qquad\Delta x_{\mathrm B}(2n)=\tfrac{\mathfrak h/\ln2}{2n}\propto\tfrac1n\qquad\implies\qquad\boxed{\ \Bigl(\tfrac{\Delta x_{\mathrm B}(2n)}{\Delta x_{\mathrm B}(2)}\Bigr)^{2}=\frac1{n^2}\ }\ [\text{machine D1}];$$
$$\frac{E_2}{E_1}=\frac14\ \text{three independent exact ways:}\quad\Bigl(\tfrac{\Delta x_{\mathrm B}(4)}{\Delta x_{\mathrm B}(2)}\Bigr)^{2};\qquad\frac{\nu(2)}{\nu(4)}=\frac{2^2}{2^4}\ [\mathrm{Def\text{-}H.32}(2)];\qquad\frac{1/4^2}{1/2^2}\qquad[\text{machine D2}]$$
$$(5)\quad\textbf{HONEST BOUNDARIES:}\qquad(\mathrm a)\ \ \text{the}\ B\to\infty\ \textbf{universe limit is}\ \neg\textbf{constructed}\ [\mathrm{Def\text{-}H.32}(1);\ \mathrm{FT.105}]:\ \ \text{``universe-level''}=\ \text{the budget filtration with NO local-seal truncation};$$
$$(\mathrm b)\ \ \text{BM.48(2)'s}\ E_n=-\varepsilon_{\mathrm{EM}}^2m_r(q_1q_2)^2/(2n^2)\ \text{splits as}\ [-\varepsilon^2m_r/2]\times[1/n^2]:\ \ \textbf{only the dimensionless}\ 1/n^2\ \textbf{is ledger-side};\ m_r\ \neg\text{derived},\ \neg\text{imported}\ [\text{machine D3};\ \mathrm{P5}];$$
$$(\mathrm c)\ \ \text{the level identification}\ n\leftrightarrow E_{\mathrm{int}}/2\ \text{and the energy read}\ E_n\propto-(\Delta x_{\mathrm B})^2\ \text{are a READ-SPECIFICATION at this tag}\ —\ \textbf{upgraded at AT.44(5),(6): the shape is derived from the move system}$$
$$(6)\quad\textbf{the bars, adjudicated:}\qquad\mathrm{BM.6}(5)\text{'s ``dynamics of}\ Q\ \neg\text{constructed''}\ \textbf{is level-local and superseded FOR THE STRUCTURE by}\ \mathrm{Def\text{-}H.32}(7)/\mathrm{FT.108}(2),(4),(5)/\mathrm{BM.137}(3)\ [\text{machine E1}];$$
$$\text{what stays calibration is the ABSOLUTE tick-rate}\ [\mathrm{CT0.3}];\qquad\mathrm{BM.48}(4)\text{'s category bar is STRICT and respected:}\ \mathcal B^{(2)}_{\mathrm{ens}}=-\tfrac45\tfrac{\ln2}{\mathfrak h}<0\ \text{is a SYSTEM read}\ [\mathrm{BM.137}(3);\ \text{machine E2,E3}]$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(2),(3),(4)\text{'s monomial ratios};\qquad\textbf{marked,}\neg\textbf{adopted:}\ (5\mathrm c);\qquad\textbf{superseded (level-local):}\ \mathrm{BM.6}(5)\ \text{for the structure};\qquad\textbf{respected (strict):}\ \mathrm{BM.48}(4)$$

**Req.** A8 (Part 1); D0.4, D0.8, D1.2, D3.4, D3.8 (Parts 1–2); CT0.8, CT0.9, CT3.17a(1), EM.9, EM.9b, FT.105, FT.108(2),(4),(5), Def-H.32(1),(2),(3),(4),(5),(6),(7), Def-H.4 (Part 3); AT.31, AT.41 (this level); Def-BM.3(7), Def-BM.4(1), Def-BM.5(1),(3),(4), Def-BM.8(4), BM.6(5), BM.13(3), BM.19(1),(2),(3), BM.48(2),(3),(4), BM.110(1), BM.111(5), BM.129(1), BM.136(4), BM.137(1),(2),(3), FT.19, FT.28, Census FT.35 (Part 4); CT0.3; exact formal-power-series coefficient comparison over $\mathbb Q$, integer binomials, `Fraction` moment algebra [math; machine: `q_dynamics.py` §§A–E, 14/14].

**Pf.**
$$(1):\ (x_-,x_+)Q=(0,0)\ \text{over}\ \mathbb Z[x_+,x_-],\ \dim\ker Q=1\implies p\ \text{unique}\ [\text{machine A1 at 25 thresholds}];\ \Sigma_{j\ge1}\binom njp^ju^{n-j}=1-u^n,\ (1-u)D_n=1-u^n\ [\text{machine A2}]$$
$$(2):\ \text{the geometric identity to order}\ 12\ [\text{machine B1}];\ \text{non-termination}\ [\text{machine B2}];\ g(1)=0\ \text{vs}\ \neg\exists\,\delta/\varepsilon\ \text{for charge}\ [\text{machine B3}];\ (3):\ \Sigma P=1,\ \text{the}\ \varepsilon_q{=}0\ \text{collapse},\ \langle E\rangle{=}2n/D_n\ [\text{machine C-a,C-b,C1}]$$
$$(4):\ ((2)/(2n))^2=1/n^2,\ n=1..12\ [\text{machine D1}];\ (1/2)^2=2^2/2^4=(1/16)/(1/4)=1/4\ [\text{machine D2}];\ (5),(6):\ \mathrm{Def\text{-}H.32}(1),\ \mathrm{BM.48}(2)\ \text{split},\ \text{the grade homomorphism}\ a_+-a_-=|R'|-|R|\ [\mathrm{FT.108}(2);\ \text{machine E1--E3}].\ \blacksquare$$

**Phys.** The corpus never had a Coulomb potential, and it does not need one. What it has is a move
system — retain an edge or dissolve it, weighted by $x_\pm$ — whose transition sum is a *geometric
resolvent* with a pole and no termination. That unbounded geometric direction **is** the infinite
range: because the electromagnetic charge read is additive and boundary-exact and carries no local
$\delta/\varepsilon$ contraction, nothing zeroes a distant $Q{=}+1\cdots Q{=}-1$ connector the way a
single dangling colour attachment zeroes the strong sector. Confinement is a local seal;
electromagnetism is the *absence* of one. Bind the two registers and the "orbital" is not a
wavefunction but a **distribution of Born widths**: the connector's retained content flickers over
$2\mathbb Z$ with the derived binomial weight, each value carrying its own width
$\mathfrak h/(E_{\mathrm{int}}\ln2)$; the distribution is normalized, discrete, localized by
concentration, and collapses at $\varepsilon_q=0$ to the single crystallized width. The electron is
"around" the proton because the flicker weight concentrates, not because a $1/r$ well holds it. And
the hydrogenic ratio is arithmetic: the Born widths run $\propto1/n$, their squares $\propto1/n^2$,
and $E_2/E_1=1/4$ on three independent exact readings. What stays honest is the scale and the
$B\to\infty$ limit — and the fact that, at this tag, the *level reading* is still a specification.
AT.44 removes that residue from the shape itself.

---

### AT.43 — The binding-scaling no-go: no derived sealed-currency functional is exactly $1/E_{\mathrm{int}}^2$ and the binding energy

**Thm.**
$$(1)\quad\textbf{THE EXACT}\ 1/E_{\mathrm{int}}^2\ \textbf{SLOT IS ONE GEOMETRIC OBJECT.}\ \ \text{Testing}\ F(2n)/F(2)=1/n^2\ \text{on exact rationals, precisely two derived functionals qualify:}$$
$$\boxed{\ (\Delta x_{\mathrm B})^2=\frac{\mathfrak h^2}{(E_{\mathrm{int}}\ln2)^2}\ \ [\mathrm{Def\text{-}BM.4}(1)]\qquad\text{and}\qquad\frac1G=\frac1{2\pi E_{\mathrm{int}}^2\ln2}\ \ [\mathrm{BM.88}(3)]\ }\qquad\text{and they are PROPORTIONAL:}\quad G\,(\Delta x_{\mathrm B})^2=\frac{2\pi\mathfrak h^2}{\ln2}=\ \text{const}$$
$$m_{\mathrm{hid}}\propto E_{\mathrm{int}};\quad\Delta x_{\mathrm B}\propto1/E_{\mathrm{int}};\quad G\propto E_{\mathrm{int}}^2:\qquad\text{none of these is}\ 1/E_{\mathrm{int}}^2\qquad[\text{machine A1,A2}]$$
$$(2)\quad\textbf{THE FOUR NAMED CANDIDATES, REFUTED BY EXACT COMPUTATION:}$$
$$\begin{array}{l|l}\textbf{candidate} & \textbf{exact scaling}\\\hline\text{resolvent pole shift}\ [\mathrm{FT.108}(5)] & E_{\mathrm{int}}\text{-FLAT: the pole sits at}\ w^2x_+x_-=1,\ \ x_+x_-=4\varepsilon_q(1{-}4\varepsilon_q)\ \text{is a function of}\ \varepsilon_q\ \textbf{alone}\\[2mm]\text{Janus binomial variance}\ [\mathrm{BM.137}(1)] & \operatorname{Var}(E_{\mathrm{int}})\ \text{absolute}\ \propto n;\quad\operatorname{Var}/\langle E\rangle^2\sim1/n\ —\ \neg\,1/n^2\\[2mm]\text{2nd-order Lyapunov contraction}\ [\mathrm{BM.51}(3)] & \text{EXPONENTIAL:}\ V_{E_{\mathrm{int}}}/V_0=(1-\gamma/4)^{2E_{\mathrm{int}}}\ —\ \neg\text{a power law}\\[2mm]\text{2nd-order flicker weight}\ [\mathrm{BM.137}(1)] & w_{\mathrm{mat}}^{(n)}=1/D_n\to(1-u)=p\ —\ \text{a CONSTANT saturation}\end{array}$$
$$(3)\quad\textbf{THE UNIQUE DERIVED BINDING IS LINEAR, OF OPPOSITE MONOTONICITY:}\qquad\mathcal B^{(n)}_{\mathrm{ens}}=-\frac{2n\,u\,D_{n-1}}{D_n}\cdot\frac{\ln2}{\mathfrak h}\ \ [\mathrm{BM.137}(3)]:$$
$$D_{n-1}/D_n\to1\implies|\mathcal B^{(n)}_{\mathrm{ens}}|\sim2nu\,\tfrac{\ln2}{\mathfrak h}\ \propto\ E_{\mathrm{int}}\ \ \textbf{INCREASES with}\ n;\qquad\text{the hydrogenic}\ |E_n|\sim1/n^2\ \ \textbf{DECREASES with}\ n;$$
$$\boxed{\ \neg\exists\ \text{a rescaling mapping a growing linear functional onto a shrinking}\ 1/n^2\ \text{one}\ }\qquad[\text{machine C1,C2}]$$
$$(4)\quad\textbf{THE DERIVED COUPLING MISSES THE EXACT}\ \tfrac14\ \textbf{BY AN ALGEBRAIC RESIDUE:}\qquad\mathsf g(G)=\tfrac1{1+G}\ \textbf{derived and selected}\ [\mathrm{BM.133}(4)],\quad G=2\pi E_{\mathrm{int}}^2\ln2\ [\mathrm{BM.88}(3)];$$
$$\text{under}\ n\leftrightarrow E_{\mathrm{int}}=2n:\quad G_n=n^2G_1,\qquad\frac{E_2}{E_1}=\frac{\mathsf g(G_2)}{\mathsf g(G_1)}=\frac{1+G_1}{1+4G_1}=\frac14+\frac{3}{4(1+4G_1)}\ >\ \frac14\qquad\forall\,G_1>0;$$
$$\textbf{the inequality is an identity in}\ \mathbb Q(G_1)\ —\ 4(1+G_1)-(1+4G_1)=3,\ \text{the}\ \pi\ln2\ \textbf{cancels};\qquad\text{rigorous enclosure}\ \tfrac{E_2}{E_1}\in[0.26061\dots],\ \text{disjoint from}\ \{\tfrac14\}\ [\text{machine D1,D2}]$$
$$\boxed{\ \textbf{the exact}\ 1/n^2\ \textbf{is the}\ G\to\infty\ \textbf{asymptote of the derived coupling, never exact at a finite level}\ }$$
$$(5)\quad\textbf{HARD NO-GO (Level 5):}\qquad\neg\exists\ \text{a derived functional in the sealed/geometric/informational currencies that is exactly}\ \propto1/E_{\mathrm{int}}^2\ \wedge\ \text{the lepton--baryon binding energy};$$
$$\text{the lepton--baryon binding-energy FUNCTIONAL is itself un-derived}\ [\mathrm{BM.48}(3)];\qquad\therefore\ \mathrm{AT.42}(5\mathrm c)\ \textbf{cannot be closed by a sealed-currency derivation}$$
$$(6)\quad\textbf{the reopening conditions (a no-go is level-local):}\qquad(\mathrm{R1})\ \text{derive that the bound-state read takes the asymptotic}\ 1/G,\ \text{dropping the}\ +1\ \text{— the obstruction is exactly the residue}\ \tfrac{3}{4(1+4G_1)};$$
$$(\mathrm{R2})\ \text{find a level index with a derived}\ 1/m^2\ \text{read};\qquad(\mathrm{R3})\ \text{construct the TWO-BODY resolvent pole}\ —\ \textbf{R3 is MET at AT.44, in the fifth (fugacity) currency}$$
$$(7)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(2),(3),(4),(5),(6);\qquad\textbf{a NO-GO row, the species of}\ \mathrm{BM.90},\ \mathrm{BM.125}(4),\ \mathrm{BM.126};\qquad\textbf{superseded at}\ (5)\text{'s clause (a) by}\ \mathrm{AT.44}\ \text{— a derived exact}\ 1/E_{\mathrm{int}}^2\ \text{functional DOES exist, in the fugacity currency}$$

**Req.** D0.4, D2.9 (Parts 1–2); FT.108(5), Def-H.32(4),(5) (Part 3); AT.42 (this level); Def-BM.4(1), BM.13(3), BM.15(2), BM.19(2), BM.48(2),(3), BM.51(3), BM.83(2), BM.88(3), BM.90, BM.125(4), BM.126, BM.133(4),(6), BM.137(1),(2),(3), BM.140(5), FT.28, Census FT.35 (Part 4); exact rational scaling tests, integer-binomial moment algebra, the symbolic identity $4(1+G_1)-(1+4G_1)=3$ in $\mathbb Q(G_1)$, rigorous `Fraction` $\pi/\ln2$ enclosures (Machin + the $\ln2$ series) [math; machine: `binding_scaling.py` §§A–F, 13/13].

**Pf.**
$$(1):\ (\Delta x_{\mathrm B}(2n))^2/(\Delta x_{\mathrm B}(2))^2=(2/2n)^2=1/n^2;\quad(1/G_{2n})/(1/G_2)=4/4n^2=1/n^2;\quad G(\Delta x_{\mathrm B})^2=2\pi\mathfrak h^2/\ln2\ \text{at}\ E_{\mathrm{int}}\in\{2,4,6,12,24,60\}\ [\text{machine A1,A2}]$$
$$(2):\ x_+x_-=4\varepsilon_q(1-4\varepsilon_q)\ \text{carries no}\ E_{\mathrm{int}}\ [\text{machine B1}];\ \operatorname{Var}=4n[(1+(n-1)p)D_n-n]/D_n^2\ \text{computed},\ n=2..8\ [\text{machine B2}];\ (1-\gamma/4)^{2E}\ \text{exponential}\ [\text{machine B3}];\ 1/D_n\to1-u\ [\text{machine B4}]$$
$$(3):\ |\mathcal B^{(2)}|<|\mathcal B^{(4)}|<|\mathcal B^{(6)}|\ \text{exact Fractions at}\ \varepsilon_q=\tfrac1{16}\ [\text{machine C1,C2}];\ (4):\ \text{the}\ \mathbb Q(G_1)\ \text{identity at five exact witnesses incl.}\ G_1=10^6;\ \text{the interval enclosure disjoint from}\ \{\tfrac14\}\ [\text{machine D1,D2}];\ (5)--(7):\ \text{assembly}.\ \blacksquare$$

**Phys.** The directive asked the ledger to *force* the hydrogenic $1/n^2$, and the honest answer at
this tag is that the sealed currencies do not — for a reason that is itself exact and informative.
There is precisely one $1/E_{\mathrm{int}}^2$ shape in the derived inventory, and it is geometry: the
square of the Born width, identical up to a constant to the inverse curvature lock. Everything
dynamical points the other way. The one binding the corpus derives — the flicker's attenuation of
the informational mass — *grows* with content, linearly, because more pairs flicker more; a
hydrogenic level *shrinks* as $1/n^2$. Opposite monotonicity is not a rescaling away. And the
coupling that carries the right asymptotics, the derived and selected $\mathsf g(G)=1/(1+G)$, misses
the exact quarter by a clean algebraic sliver, $3/(4(1+4G_1))$, with the $\pi\ln2$ cancelling out of
the comparison. That is the precise sense in which the spectrum was, at this tag, a
read-specification — and the no-go named exactly what would overturn it. The next tag does.

---

### AT.44 — The two-body zig-zag resolvent: the harmonic pole ladder, the lepton price at $k=1$, and the $1/d^2$ spectrum as a theorem of the move system

**Thm.**
$$(1)\quad\textbf{THE}\ k\textbf{-CHANNEL MOVE SYSTEM AND ITS RETURN CENSUS.}\ \ \text{On a}\ k\text{-pair connector floor}\ [\mathrm{BM.137}(1):\ \text{independent pairs}],\ \text{state}=\ \text{the retained set}\ \subseteq\{1..k\};$$
$$J^+_i:\ S\mapsto S\cup\{i\}\ [\text{weight}\ x_+],\qquad J^-_i:\ S\mapsto S\setminus\{i\}\ [\text{weight}\ x_-],\qquad\hat J_\pm^2=0\implies\text{strict alternation per channel}\ [\mathrm{BM.120}(1);\ \mathrm{BM.121}(1)];$$
$$\text{every length-}2m\ \text{return word carries}\ (x_+x_-)^m,\qquad\langle\varnothing|\hat U^{2m}|\varnothing\rangle=N_k(2m)\,(x_+x_-)^m,\qquad\boxed{\ N_k(2m)=\frac1{2^k}\sum_{j=0}^{k}\binom kj(2j-k)^{2m}\ \in\mathbb Z\ }$$
$$[\text{machine: brute-force word enumeration}\ \wedge\ \text{exact transfer DP}\ \wedge\ \text{the closed form},\ k\le6,\ 2m\le24];\qquad N_1\equiv1\ \text{recovers}\ \mathrm{BM.121}(1);\quad N_2=2^{2m-1};\quad\textbf{all odd elements vanish}$$
$$(2)\quad\textbf{THE TWO-BODY RESOLVENT PARTIAL-FRACTIONIZES EXACTLY:}\qquad\boxed{\ R_k(w)=\sum_{m\ge0}N_k(2m)(w^2x_+x_-)^m\ =\ \frac1{2^k}\sum_{j=0}^{k}\binom kj\,\frac1{1-(2j-k)^2\,w^2x_+x_-}\ }$$
$$[\text{machine: coefficient-wise over}\ \mathbb Q,\ k=1..6,\ \text{orders}\ 0..12];\qquad k=1:\ R_1=\tfrac1{1-w^2x_+x_-}\ \text{— the frozen zig-zag resolvent verbatim}\ [\mathrm{BM.121}(2);\ \mathrm{FT.108}(5)]$$
$$(3)\quad\textbf{THE HARMONIC POLE LADDER:}\qquad\text{poles at}\ z:=w^2x_+x_-=\tfrac1{d^2},\quad d\in\{k,k-2,\dots\}>0;\qquad\text{weights}\ \tfrac1{2^{k-1}}\binom k{(k+d)/2};\qquad R_k(0)=1;$$
$$\textbf{the dominant pole = the convergence radius:}\qquad\boxed{\ \mathrm{radius}(k)=\frac1{k\sqrt{x_+x_-}}\ \le\ \frac2k\ }\qquad[\text{machine:}\ d_{\max}=k\ \forall k]\ —\ \text{generalizes}\ \mathrm{BM.121}(5)\text{'s}\ |w|\ge2$$
$$(4)\quad\textbf{THE LEPTON MASS READ (}k=1\textbf{), NATIVE CURRENCY:}\qquad\boxed{\ w_c=\frac1{\sqrt{x_+x_-}}=\frac1{\sqrt{4\varepsilon_q(1-4\varepsilon_q)}}\ \ge\ 2,\qquad\text{equality}\iff\varepsilon_q=\tfrac18\ }$$
$$\textbf{the SOS certificate:}\quad\tfrac14-x_+x_-=\tfrac{(8\varepsilon_q-1)^2}4\ \ge0\ \ \text{in}\ \mathbb Q[\varepsilon_q];\qquad\textbf{the alphabet census:}\quad\mathrm{alph}(w_c)=\{\varepsilon_q\},\ \ \textbf{DISJOINT from every sealed currency}$$
$$\{E_{\mathrm{int}},\ln2,\pi,\kappa,\rho,\mathfrak h\}\ (\text{curvature}),\quad\{E_{\mathrm{int}},\ln2,\mathfrak h\}\ (\text{informational}),\quad\{\hat\mu'^2,D_S\}\ (\text{pole/defect});\qquad\boxed{\ \textbf{the curvature flux is bypassed exactly}\ }$$
$$w_c^2\ \text{on}\ \varepsilon_q\in(0,\tfrac14):\ \ \text{strictly}\ge4,\ \text{uniquely minimized at}\ \varepsilon_q=\tfrac18\ (w_c=2),\ \text{symmetric under}\ \varepsilon_q\leftrightarrow\tfrac14-\varepsilon_q,\ \text{divergent at both endpoints}\ [\text{machine D1--D3}]$$
$$(5)\quad\textbf{THE SPECTRUM — DERIVED FROM THE MOVE SYSTEM.}\ \ R_k\ \text{is EVEN}\ [(1)]\implies\text{its native variable is}\ W:=w^2;\qquad\text{in}\ W:\quad W_d=\frac1{d^2\,x_+x_-},\quad d=1,2,3,\dots$$
$$\boxed{\ \frac{W_d}{W_1}=\frac1{d^2}\ \ \textbf{EXACTLY in}\ \mathbb Q(x_+x_-);\qquad\frac{W_2}{W_1}=\frac14\ }\qquad[\text{machine:}\ d=1..12];\qquad\text{the read species is}\ \mathrm{BM.134}(1)\text{'s ``pole displacement'', rebuilt natively}$$
$$\textbf{at detailed balance}\ \varepsilon_q=\tfrac18:\quad x_+x_-=\tfrac14,\qquad w_d=\frac2d,\qquad W_d=\frac4{d^2}\ \ \textbf{RATIONAL — zero free parameters}\ [\text{machine C2}]$$
$$(6)\quad\textbf{TWO INDEPENDENT DERIVED ROUTES, ONE SHAPE:}\qquad\underbrace{W_d/W_1=1/d^2}_{\text{the move system},\ (5)}\quad=\quad\underbrace{\bigl(\Delta x_{\mathrm B}(2d)/\Delta x_{\mathrm B}(2)\bigr)^2=1/d^2}_{\text{the geometry}\ [\mathrm{AT.42}(4);\ \mathrm{Def\text{-}BM.4}(1)]}\qquad[\text{machine E1}]$$
$$\boxed{\ \textbf{the}\ 1/n^2\ \textbf{shape is a theorem with two ledger witnesses, imported from neither the chart nor a Born-width mapping}\ }\qquad\implies\ \mathrm{AT.42}(5\mathrm c)\ \textbf{shrinks to the read rule + the chart-side scale}$$
$$(7)\quad\textbf{THE INCOMMENSURABILITY ADJUDICATION.}\ \ \mathrm{BM.83}(2):\ \ln1280=8\ln2+\ln5\ \text{vs}\ \ln960=6\ln2+\ln3+\ln5\ —\ \text{the}\ \ln3\ \text{coefficient forces}\ p=0,\ \text{then}\ \ln5\ \text{forces}\ q=0;\ \ \mathrm{BM.140}(5)\ \text{applies it};$$
$$\text{its extension to the resolvent currency runs on the corpus's universal disjoint-ALPHABET mechanism}\ [\mathrm{BM.37}(2);\ \mathrm{BM.90}(\mathrm{O1})];\qquad\boxed{\ \textbf{the sealed (baryon) and unsealed-resolvent (lepton) mass reads are TWO SPECIES}\ }$$
$$\textbf{the bar STANDS}\ (\neg\text{a cross-currency equation is formed, and none may be})\ \textbf{and no longer BLOCKS:}\ \text{the lepton read never needed the conversion}\ [\mathrm{BM.96}\ \text{precedent: derived in form, undeclared in scale}]$$
$$(8)\quad\textbf{honest scope:}\qquad(\mathrm i)\ w_c\ \textbf{is generation-blind} — one price for the lepton species; the family splitting lives in the Gram/transport currency\ [\mathrm{FT.113};\ \mathrm{BM.96}]\ \text{and is}\ \neg\text{mixed in};$$
$$(\mathrm{ii})\ w_c\ \textbf{is a PRICE}\ (\mathfrak q^0,\ \text{dimensionless}),\ \neg\text{a mass in}\ \mathfrak h\text{-units};\qquad(\mathrm{iii})\ \textbf{cross-species identification is BARRED}\ [\mathrm{BM.134}(5):\ \text{the two resolvents meet only through}\ \chi_{\{NE\ge\mathcal T_0\}}]\ \text{and is}\ \neg\text{attempted};$$
$$(\mathrm{iv})\ \textbf{the read rule}\ (\text{level-}d\ \text{price}=\ \text{squared dominant pole in the native variable}\ W)\ \textbf{is the residual marked specification} — canonical\ (\text{evenness forces}\ W;\ \mathrm{BM.134}(1)\ \text{species}),\ \text{but}\ \neg\text{derived}$$
$$(9)\quad\textbf{status:}\qquad\textbf{derived:}\ (1),(2),(3),(4),(5),(6),\ (7)\text{'s disjointness};\qquad\textbf{marked,}\neg\textbf{adopted:}\ (8\mathrm{iv});\qquad\textbf{calibration, unchanged:}\ \varepsilon_q\ \text{value},\ -\varepsilon_{\mathrm{EM}}^2m_r/2\ [\mathrm{BM.48}(2)\ \text{symbolic}];$$
$$\textbf{CLOSES:}\ \mathrm{AT\text{-}O5}\ (\text{the mass read, in species}),\ \ \mathrm{AT.43}(\mathrm{R3});\qquad\textbf{UPGRADES:}\ \mathrm{AT.42}(5\mathrm c),\ \ \mathrm{AT.43}(5)\text{'s clause (a)}\ —\ W_k=4/(E_{\mathrm{int}}^2\,x_+x_-)\ \textbf{is a derived exact}\ 1/E_{\mathrm{int}}^2\ \textbf{functional, in the fifth currency}$$

**Req.** A2, A4, D0.4 (Part 1); BM.120(1), BM.121(1),(2),(4),(5), BM.123(2), CT0.8 (Part 4); FT.28, FT.108(3),(4),(5), FT.113, Def-H.32(7), Def-BM.14(6) (Parts 3–4); AT.42(4),(5), AT.43(1),(5),(6), AT-O19 (this level); Def-BM.4(1), BM.13(3), BM.15(2), BM.19(1),(2),(3), BM.37(2), BM.48(2), BM.83(2), BM.88(3), BM.90(O1), BM.96, BM.134(1),(5), BM.137(1),(2), BM.140(5) (Part 4); integer word enumeration, transfer-matrix DP over $\mathbb Z$, the parity-projection identity, coefficient-wise formal-power-series equality over $\mathbb Q$, the SOS certificate $(8\varepsilon_q-1)^2/4$ in $\mathbb Q[\varepsilon_q]$ [math; machine: `two_body_resolvent.py` §§A–F, 16/16].

**Pf.**
$$(1):\ \text{a return word needs equal}\ J^+_i,J^-_i\ \text{per channel, strict alternation}\implies\text{uniform weight}\ (x_+x_-)^m;\ \ N_k(2m)=\tfrac1{2^k}\Sigma_j\binom kj(2j-k)^{2m}\ \text{vs brute force}\ (k\le3)\ \text{and the DP}\ (k\le6)\ [\text{machine A1--A4}];$$
$$(2):\ [z^m]R_k=N_k(2m)=\tfrac1{2^k}\Sigma_j\binom kj((2j-k)^2)^m=[z^m]\tfrac1{2^k}\Sigma_j\binom kj\tfrac1{1-(2j-k)^2z}\ [\text{machine B1}];\ (3):\ |2j-k|\le k\ \text{with equality at}\ j\in\{0,k\}\ [\text{machine B2,B3}];$$
$$(4):\ \tfrac14-4\varepsilon_q(1-4\varepsilon_q)=(4\varepsilon_q-\tfrac12)^2=\tfrac{(8\varepsilon_q-1)^2}4\ [\text{machine C3,D1}];\ \text{the alphabet census}\ [\text{machine D1,D2}];\ (5):\ \text{evenness}\implies R_k=R_k(Wx_+x_-);\ W_d/W_1=1/d^2\ [\text{machine C1,C2}];$$
$$(6):\ \text{both sides}\ =\tfrac1{d^2}\ \text{as exact rationals},\ d\le12\ [\text{machine E1}];\ (7):\ \text{the alphabet intersections are empty}\ [\text{machine D1}];\ \mathrm{BM.83}(2)\text{'s proof re-cited};\ (8),(9):\ \text{the scope and status records}\ [\text{machine D3,E2,F1}].\ \blacksquare$$

**Phys.** The corpus's smallest dynamical object — a pair that flickers in and out of the record,
forward-only, one word at a time — already knew the hydrogen spectrum. Ask the move system for the
return sum of $k$ independent flickering channels and the answer is forced: strict alternation per
channel, interleavings counted by the parity-projected multinomial, and the sum
partial-fractionizes into geometric resolvents whose poles sit at $1/d^2$ — a *harmonic ladder in
the squared fugacity*, which is the resolvent's own native variable because every odd coefficient
vanishes. The dominant pole is the convergence radius, $1/(k\sqrt{x_+x_-})$, and it tightens
channel by channel: dressing costs convergence, exactly. Read the $k=1$ pole and you have the
lepton's price: $w_c\ge2$, a dimensionless read built from the crystallization threshold *alone* —
no edge count, no curvature lock, no $\mathfrak h$, no $\hat\mu$. The unsealed carrier was never
missing a mass read; it was missing a *currency*, and the zig-zag supplies one. Its canonical
minimum sits at $\varepsilon_q=\tfrac18$ — the fourth independent appearance of the same point
(self-adjointness, detailed balance, the round-trip maximum, and now the unique rational locus of
the whole pole ladder, $w_d=2/d$). And the two routes meet: the geometry said
$(\Delta x_{\mathrm B}(2d)/\Delta x_{\mathrm B}(2))^2=1/d^2$; the move algebra says $W_d/W_1=1/d^2$;
the agreement is exact and neither side was imported from the chart. What remains soft is small and
named: the read rule that calls the squared dominant pole a level price, the value of
$\varepsilon_q$, the chart-side scale, and every cross-species identification — which BM.134(5)
bars forever, not as a failure but as the discipline that keeps two resolvents honest.
Incommensurability stops being a wall the moment the lepton is read where it lives.

---

### AT.45 — The status of Tier AT.7: adjudication, the consolidated ledger, and the state of the Atomic era

**Thm.**
$$(1)\quad\textbf{DERIVED — the positive content of AT.41–AT.44:}\qquad\begin{array}{l|l}\textbf{the row} & \textbf{the locus}\\\hline\text{the EM sealing grammar FACTORS:}\ (\text{boundary signs}\to Q)\times(\text{interior colour partition}\to\text{seal class}) & \mathrm{AT.41}(5),(6)\\ Q\ \text{is boundary-exact;}\ W_3(+1)=15,\ W_3(0)=20,\ 4/3;\ \text{all }64\ \text{assignments}\ \varepsilon\text{-sealable} & \mathrm{AT.41}(1),(2),(3)\\ Q=+1\ \neg\text{selects the proton: minimal sealed}=\text{charged meson}\ E_{\mathrm{int}}{=}4;\ \text{proton}=\varepsilon\text{-seal}\wedge Q{=}{+1},\ E_{\mathrm{int}}{=}6 & \mathrm{AT.41}(4)\\ \text{the lepton--baryon interaction is ONE global Def-H.32 configuration sum} & \mathrm{AT.42}(1)\\ \textbf{infinite range}=\ \text{the unbounded geometric resolvent}\ \wedge\ \text{the absence of a local EM seal} & \mathrm{AT.42}(2)\\ \text{the 'orbital'}=\ \text{the discrete Born-width distribution; normalized; collapses at}\ \varepsilon_q{=}0 & \mathrm{AT.42}(3)\\ \text{the}\ k\text{-channel return census}\ N_k(2m)=\tfrac1{2^k}\Sigma_j\binom kj(2j-k)^{2m}\ \text{(brute force}\ \wedge\ \text{DP}\ \wedge\ \text{closed form)} & \mathrm{AT.44}(1)\\ \text{the two-body resolvent partial-fractionizes; the HARMONIC POLE LADDER}\ w_d=1/(d\sqrt{x_+x_-}) & \mathrm{AT.44}(2),(3)\\ \textbf{the lepton price}\ w_c=1/\sqrt{4\varepsilon_q(1-4\varepsilon_q)}\ge2,\ \text{SOS-certified, alphabet}\ \{\varepsilon_q\}\ \textbf{alone} & \mathrm{AT.44}(4)\\ \textbf{the}\ 1/d^2\ \textbf{spectrum is a theorem of the move system};\ \text{at}\ \varepsilon_q{=}\tfrac18:\ w_d{=}2/d,\ W_d{=}4/d^2\ \textbf{rational} & \mathrm{AT.44}(5)\\ \text{two independent derived routes agree on the shape: move system}\ =\ \text{geometry} & \mathrm{AT.44}(6)\\ \text{the sealed and resolvent mass reads are TWO SPECIES; the bar stands and no longer blocks} & \mathrm{AT.44}(7)\end{array}$$
$$(2)\quad\textbf{ONE NO-GO, measured:}\qquad\mathrm{AT.43}:\ \neg\exists\ \text{a derived SEALED-CURRENCY functional exactly}\ \propto1/E_{\mathrm{int}}^2\ \wedge\ \text{the binding energy};$$
$$\text{the exact obstruction:}\ \mathcal B_{\mathrm{ens}}\ \text{linear of opposite monotonicity}\ [\mathrm{BM.137}(3)];\qquad\mathsf g(G)=\tfrac1{1+G}\ \text{gives}\ \tfrac14+\tfrac{3}{4(1+4G_1)}>\tfrac14\ \ [\mathrm{BM.133}(4)];$$
$$\textbf{its (R3) is MET at AT.44:}\ \text{the two-body pole exists and}\ W_k=4/(E_{\mathrm{int}}^2x_+x_-)\ \textbf{is a derived exact}\ 1/E_{\mathrm{int}}^2\ \textbf{functional — in the fifth (fugacity) currency}$$
$$(3)\quad\textbf{MARKED,}\neg\textbf{ADOPTED — the residual read-specifications, in shrinking order:}\qquad(\mathrm a)\ \text{the level-price read rule: level-}d\ \text{price}=\ \text{the squared dominant pole in the native variable}\ W=w^2\ [\mathrm{AT.44}(8\mathrm{iv})];$$
$$(\mathrm b)\ \text{the chart-side scale}\ -\varepsilon_{\mathrm{EM}}^2m_r/2\ [\mathrm{BM.48}(2)\ \text{symbolic};\ m_r\ \neg\text{derived, item-7 bridge}];\qquad(\mathrm c)\ \text{the level index}\ n\leftrightarrow\text{the}\ n\text{-pair floor}\ E_{\mathrm{int}}=2n\ [\mathrm{BM.137}(1)\ \text{ladder};\ \mathrm{AT.42}(5\mathrm c)\ \text{as upgraded by}\ \mathrm{AT.44}(5),(6)]$$
$$(4)\quad\textbf{SUPERSEDED / RESCOPED, on the record:}\qquad\begin{array}{l|l}\textbf{the row} & \textbf{disposition}\\\hline\mathrm{BM.6}(5)\ \text{``the dynamics of}\ Q\ \neg\text{constructed''} & \textbf{level-local; superseded FOR THE STRUCTURE by}\ \mathrm{Def\text{-}H.32}(7),\ \mathrm{FT.108}(2),(4),(5),\ \mathrm{BM.137}(3)\ \text{assembled at}\ \mathrm{AT.42};\ \text{the absolute rate stays calibration}\ [\mathrm{CT0.3}]\\ \mathrm{BM.48}(3)\ \text{``}\neg\exists\ \text{an EM sealing grammar''} & \textbf{level-local; superseded for the CHARGE READ by}\ \mathrm{Def\text{-}BM.8}/\mathrm{BM.135}\ (\text{re-produced}\ \wedge\ \text{sharpened at}\ \mathrm{AT.41});\ \text{the binding dynamics constructed at}\ \mathrm{AT.42}/\mathrm{AT.44};\ \text{the scale}\ \wedge\ \text{identification remain}\\ \mathrm{AT.43}(5)\text{'s clause (a)} & \textbf{superseded at}\ \mathrm{AT.44}(9):\ \text{a derived exact}\ 1/E_{\mathrm{int}}^2\ \text{functional exists, in the fugacity currency}\\ \mathrm{AT.42}(5\mathrm c) & \textbf{upgraded at}\ \mathrm{AT.44}(5),(6):\ \text{the SHAPE is derived from the move system with the geometry as an independent witness}\\ \mathrm{AT.30}(2)\text{'s label}\ \text{``}\Sigma f=q\text{''} & \textbf{presentational correction:}\ \text{``}=-q_{\mathrm{EM}}\text{''}\ \text{per}\ \mathrm{EM.9b}\ [\mathrm{AT.41}(7)];\ \neg\text{a retraction of derived content}\end{array}$$
$$(5)\quad\textbf{CLOSED by this tier:}\qquad\mathrm{AT\text{-}O4}\ (\text{the EM sealing grammar})\ —\ \textbf{CLOSED as structure:}\ \text{grammar}\ \mathrm{AT.41}(5),\ \text{dynamics}\ \mathrm{AT.42},\ \text{spectrum}\ \mathrm{AT.44}(5);\ \text{residual}\ =\ \text{calibration species}\ (3);$$
$$\mathrm{AT\text{-}O5}\ (\text{the lepton mass read})\ —\ \textbf{CLOSED in species:}\ w_c\ \text{formed natively}\ [\mathrm{AT.44}(4)];\ \varepsilon_q\text{'s value and the family splitting stay calibration/Gram-currency};\qquad\mathrm{AT.43}(\mathrm{R3})\ —\ \textbf{MET}$$
$$(6)\quad\textbf{THE OPEN LEDGER at this closure, with the reason each is not closable now:}\qquad\begin{array}{l|l}\textbf{row} & \textbf{why}\\\hline(\mathrm{AT\text{-}O2})\ w_i^\perp\ \text{gauge} & \textbf{BY NATURE:}\ N_i\ \text{is the momentum constraint's Lagrange multiplier}\ —\ \text{fixed by a coordinate choice},\ \neg\text{derived}\\ (\mathrm{AT\text{-}O3})\ (\varkappa,\beta) & \textbf{BY DESIGN:}\ \text{P4 core, values}\ \neg\text{issued}\ [\mathrm{C4};\ \text{§Cal-2}];\ \text{calibration after all era closures}\\ (\mathrm{AT\text{-}O6})\ \text{the anomalous moment} & \textbf{REAL CONSTRUCTION, UNCHANGED:}\ \text{the spin--field coupling needs the frame section}\ [\mathrm{BM.6}(8)];\ \mathrm{AT.44}\text{'s resolvent is }\neg\text{spin-carrying};\ \mathrm{BM.125}(4)\text{'s three grounds stand}\\ (\mathrm{AT\text{-}O11})\ \text{the dictionary at}\ n{=}4 & \textbf{SHARPENED at AT.40:}\ 13\ \text{invariants vs}\ 10\ \text{coordinates};\ \text{needs}\ \dim\mathcal K_{n\ge4}\\ (\mathrm{AT\text{-}O13})\ \text{the Kerr route} & \textbf{ONE NUMBER AWAY:}\ \text{needs}\ (\mathrm{AT\text{-}O3})\ \text{and nothing structural}\ [\mathrm{AT.34}]\\ (\mathrm{AT\text{-}O14/O16})\ \text{the locked sector} & \textbf{BLOCKED BY A MISSING DIMENSION:}\ \mathrm{CT0.14}\ \text{silent at}\ n\ge4\\ \textbf{new}\ (\mathrm{AT\text{-}O26})\ \text{the read-rule declaration} & \textbf{CLOSURE-PHASE ACT:}\ \mathrm{AT.44}(8\mathrm{iv})\text{'s level-price rule, if ever adopted, is a logged declaration}\ [\mathrm{BM.30}(5)\ \text{pattern}]\\ \textbf{new}\ (\mathrm{AT\text{-}O27})\ \varepsilon_q\text{'s value} & \textbf{CALIBRATION:}\ \tfrac18\ \text{is derived as the unique distinguished point (four ways}\ [\mathrm{AT.40}(1);\ \mathrm{AT.44}(4),(5)]),\ \text{its ADOPTION is}\ \neg\text{issued}\ [\mathrm{P5}]\end{array}$$
$$(7)\quad\textbf{the declaration census:}\qquad\textbf{the declarations this tier adds: none.}\qquad\neg\text{a P4 addition},\ \neg\text{a new dimensionful scale}\ [\mathrm{P1}],\ \neg\text{a measured value}\ [\mathrm{P5}],\ \neg\text{a species identification beyond}\ \mathrm{Def\text{-}BM.3}(7);$$
$$\text{calibration parameters added:}\ 0;\qquad\text{marked specializations:}\ 1\ (3\mathrm a\ \text{and its siblings}),\ \neg\text{adopted};\qquad\text{claims withdrawn by this tier:}\ 0\ \text{(the corrections are presentational}\ (4)\ \text{and recorded at their loci)}$$
$$(8)\quad\textbf{the machine state and the house cleaning:}\qquad\texttt{canon/era2/run\_all\_era2.py}\to\textbf{28 checkers, 497 exact markers, 0 failures, exit 0};$$
$$\textbf{NEW GATE:}\ \texttt{check\_era2\_format.py}\ —\ \text{the era2 analogue of}\ \texttt{verification/checks/check\_format.py}:\ \ \text{display-math balance, math-brace balance, per-block}\ \textbf{Thm/Req/Pf/Phys}\ +\ \backslash\text{blacksquare},\ \textbf{and citation accuracy against the canon registry};$$
$$\textbf{three format defects found and fixed in the prior tier files, content-preserving, on the record:}\quad\texttt{TierAT3}\ \text{one unclosed}\ \$\$;\quad\texttt{TierAT4}\ \text{one stray}\ \};\quad\texttt{TierAT6}\ (\text{then}\ \texttt{CLOSURE.md})\ \text{AT.39's Req/Pf/Phys moved into its block};$$
$$\text{the folder remains deliberately NOT wired into}\ \texttt{verification/run\_all.py};\ \texttt{index/},\ \texttt{tags.json},\ \texttt{Summary.md}\ \neg\text{regenerated}\ —\ \text{promotion to canon tags stays a closure-phase act}$$
$$(9)\quad\textbf{the era chain:}\qquad\text{every AT-tag of this tier cites Parts 1--4 and earlier AT-tags only.}\ \neg\exists\ \text{a forward pointer used as a premise.}\ \neg\exists\ \text{a circular citation. Acyclic by construction}\ [\text{machine:}\ \texttt{check\_era2\_format.py}\ \text{F3}]$$
$$(10)\quad\textbf{THE STATE OF THE ATOMIC ERA:}\qquad\textbf{the structural agenda is derived to the calibration boundary}\ —\ \text{the BM.23 closure shape}:$$
$$\text{grammar}\ [\mathrm{AT.41}]\ \to\ \text{dynamics}\ [\mathrm{AT.42}]\ \to\ \text{the no-go measured}\ [\mathrm{AT.43}]\ \to\ \text{the resolvent, the lepton price, the spectrum}\ [\mathrm{AT.44}];$$
$$\text{what remains between Level 5 and contact is exactly what the corpus says is calibration's:}\ \varepsilon_q,\ e_0,\ (\varkappa,\beta),\ \text{the chart-side scales, and the two read-rule declarations}\ (6);$$
$$\boxed{\ \textbf{coherence is}\ \neg\textbf{contact, and this tier makes no contact claim}\ }\qquad[\mathrm{AT.39}(8)\text{'s standing row, re-cited and unchanged}]$$

**Req.** AT.41, AT.42, AT.43, AT.44 (this level); P1, P4, P5, C4, §Cal-2, §Cal-F, §Cal-BM, A4, A8, D0.4, D2.9, D3.4, D3.8 (Parts 1–2); CT0.3, CT0.8, CT3.17a, CT3.22, EM.9, EM.9b, EM.12, EM.24(1), FT.105, FT.108, FT.113, Def-H.32, Def-H.4 (Part 3); AT.19, AT.28, AT.30, AT.31, AT.34, AT.39, AT.40, AT-O2, AT-O3, AT-O4, AT-O5, AT-O6, AT-O11, AT-O13, AT-O14, AT-O16, AT-O19 (this level); Def-BM.3, Def-BM.4, Def-BM.5, Def-BM.8, Def-BM.14, BM.2, BM.6, BM.13, BM.15, BM.17, BM.19, BM.26, BM.28, BM.30, BM.37, BM.48, BM.51, BM.55, BM.83, BM.88, BM.89, BM.90, BM.96, BM.110, BM.111, BM.120, BM.121, BM.123, BM.125, BM.126, BM.129, BM.133, BM.134, BM.135, BM.136, BM.137, BM.140, BM.143, FT.19, FT.28, FT.40, FT.41, Census FT.35 (Part 4); row-wise assembly only — no new mathematics at this tag [math; machine: all five AT.7 checkers + `check_era2_format.py`].

**Pf.** Row-wise assembly of AT.41–AT.44, each row re-citing its own machine section and its own
locus; the format gate re-run over all nine Part 5 documents; the suite re-run end to end. No new
mathematics is introduced at this tag. $\blacksquare$

**Phys.** This tier set out to build the hydrogen spine and ended up moving the corpus's own
boundary between the derived and the specified — twice. The first move was negative and exact: the
sealed currencies do not force the $1/n^2$, and the obstruction was measured to the monomial
($3/(4(1+4G_1))$). The second was positive and combinatorial: the move system does. A word census
over flickering channels — brute-forced, DP'd, and closed-form'd into agreement — partial-fractionizes
into a harmonic pole ladder whose squared displacements are the hydrogenic shape, with the geometry
as an independent witness and no chart in sight. Along the way the lepton acquired a mass read it
never had: a price of $\varepsilon_q$ alone, curvature bypassed by an alphabet census rather than an
argument, minimized exactly at the detailed-balance point the corpus had already singled out three
times. Incommensurability, read correctly, turned from a wall into an address: the lepton is not a
failed baryon; it is a native of another currency. What Level 5 still has not done is make contact —
no number issued, nothing fitted, two read-rules marked, and the era's remaining rows are
calibration, gauge, or named constructions with their obstruction loci pinned. The spine is
complete from the seal grammar to the spectrum; the flesh — the values — waits for the calibration
era, exactly as the corpus has always said it would.
